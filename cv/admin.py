from django.contrib import admin
from cv.models import PersonalInformation, Education, Interest, Language, Experience, Projects, Skill, ResumePartView, ResumeView, ResumeUser, LimitedResumeUser, LimitationPolicy
from cv.forms import PersonalInformationForm, ResumeUserForm

# Register your models here.


class PersonalInformationAdmin(admin.ModelAdmin):
    form = PersonalInformationForm
    list_display = ('last_name', 'name', 'email', 'cv_name', 'is_main',)
    list_filter = ('last_name', 'name', 'email',)
    ordering = ('last_name', 'name', 'email',)
    search_fields = ('last_name', 'name', 'email', 'cv_name',)


class ResumeUserAdmin(admin.ModelAdmin):
    form = ResumeUserForm

admin.site.register(PersonalInformation, PersonalInformationAdmin)
admin.site.register(Education)
admin.site.register(Interest)
admin.site.register(Language)
admin.site.register(Experience)
admin.site.register(Projects)
admin.site.register(Skill)
admin.site.register(ResumePartView)
admin.site.register(ResumeView)
admin.site.register(ResumeUser, ResumeUserAdmin)
admin.site.register(LimitedResumeUser)
admin.site.register(LimitationPolicy)
