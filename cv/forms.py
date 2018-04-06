from django import forms
from cv.models import PersonalInformation, ResumeUser


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class ResumeUserForm(forms.ModelForm):

    class Meta:
        model = ResumeUser
        fields = ('user', 'username', 'is_main_user')

    def clean_is_main_user(self):
        is_main = self.cleaned_data["is_main_user"]
        username = self.cleaned_data["username"]

        # Il n'y a pas encore d'utilisateur principal
        nb_elems = len(ResumeUser.objects.filter(is_main_user=True))
        if nb_elems == 0:
            return True
        
        # On sélectionne l'utilisateur principal
        main_username = ResumeUser.objects.filter(is_main_user=True)[0].username
        if is_main and username != main_username:
            raise forms.ValidationError("Il ne peut y avoir qu'un seul utilisateur principal")

        return is_main


class PersonalInformationForm(forms.ModelForm):

    cv_name = forms.CharField(required=False)
    website = forms.URLField(required=False)
    linkedin = forms.URLField(required=False)
    twitter_username = forms.CharField(required=False)
    github_username = forms.CharField(required=False)

    class Meta:
        model = PersonalInformation
        fields = ('user', 'cv_name', 'name', 'last_name', 'mobile_phone',
                  'email', 'position', 'website', 'linkedin', 'twitter_username',
                  'github_username', 'career_profile', 'is_main', 'auth_for_stats')

    def clean_is_main(self):
        is_main = self.cleaned_data["is_main"]
        user = self.cleaned_data["user"]

        nb_elems = len(PersonalInformation.objects.filter(user=user))
        if nb_elems == 0:
            return True

        if is_main:
            for p in PersonalInformation.objects.all().filter(is_main=True, user=user):
                p.is_main = False
                p.save()

        return is_main
