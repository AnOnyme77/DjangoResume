from django.shortcuts import render, get_object_or_404
from cv.models import PersonalInformation, Skill, Projects, Experience, Language, Education, Interest, ResumeView, ResumePartView, ResumeUser
from cv.forms import ConnexionForm
from django.http import HttpResponse, Http404
import datetime
import itertools
from django.contrib.auth import authenticate, login as auth_login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def login(request):
    connexion = ConnexionForm(request.POST or None)

    if request.method == "POST":
        connexion = ConnexionForm(request.POST)
        if connexion.is_valid():
            username = connexion.cleaned_data["username"]
            password = connexion.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                auth_login(request, user)  # nous connectons l'utilisateur
                return redirect(reverse(admin))
            else: # sinon une erreur sera affichée
                error = True
    else:
        if request.user.is_authenticated():
            return redirect(reverse(admin))
        else:
            connexion = ConnexionForm()

    return render(request, 'cv/user_login.html', locals())


@login_required(login_url="/admin/login")
def admin(request):
    resumes = PersonalInformation.objects.filter(user=request.user.resumeuser)
    return render(request, 'cv/user_admin.html', locals())


def main_cv(request):
    found = True
    try:
        cv = ResumeUser.objects.filter(is_main_user=True)[0].personalinformation_set.filter(is_main=True)[0]

        if cv is None:
            found = False
    except:
        found = False

    if not found:
        raise Http404()
    
    ResumeView.objects.create(resume=cv)

    skills = Skill.objects.filter(cv=cv)
    projects = Projects.objects.filter(cv=cv)
    experiences = Experience.objects.filter(cv=cv)
    languages = Language.objects.filter(cv=cv)
    educations = Education.objects.filter(cv=cv)
    interests = Interest.objects.filter(cv=cv)
    return render(request, 'cv/index.html', locals())


def usercv(request, username):
    found = True
    try:
        cv = ResumeUser.objects.filter(username=username)[0].personalinformation_set.filter(is_main=True)[0]

        if cv is None:
            found = False
    except:
        found = False

    if not found:
        raise Http404()

    ResumeView.objects.create(resume=cv)

    skills = Skill.objects.filter(cv=cv)
    projects = Projects.objects.filter(cv=cv)
    experiences = Experience.objects.filter(cv=cv)
    languages = Language.objects.filter(cv=cv)
    educations = Education.objects.filter(cv=cv)
    interests = Interest.objects.filter(cv=cv)

    return render(request, 'cv/index.html', locals())


def cv(request, cvId):
    cv = get_object_or_404(PersonalInformation, id=cvId)
    ResumeView.objects.create(resume=cv)

    skills = Skill.objects.filter(cv=cv)
    projects = Projects.objects.filter(cv=cv)
    experiences = Experience.objects.filter(cv=cv)
    languages = Language.objects.filter(cv=cv)
    educations = Education.objects.filter(cv=cv)
    interests = Interest.objects.filter(cv=cv)
    return render(request, 'cv/index.html', locals())


def main_resume_stats(request):
    found = True
    try:
        cv = ResumeUser.objects.filter(is_main_user=True)[0].personalinformation_set.filter(is_main=True)[0]

        if cv is None:
            found = False
    except:
        found = False

    if not found:
        raise Http404()

    views = ResumeView.objects.filter(resume=cv)
    parts_hover = ResumePartView.objects.filter(resume=cv)

    if cv.auth_for_stats and not request.user.is_authenticated():
        raise Http404

    grouped = itertools.groupby(views, lambda record: record.date.strftime("%Y-%m-%d"))
    visits_by_day = [(day, len(list(jobs_this_day))) for day, jobs_this_day in grouped]
    days, visits = zip(*visits_by_day)
    days = list(days)
    visits = list(visits)

    counts = dict()
    for partview in parts_hover:
        key = partview.part.split("-")[0]
        if key not in counts.keys():
            counts[key] = 0
        counts[key] += 1
    parts = list(counts.keys())
    nbhover = list(counts.values())

    return render(request, 'cv/stats.html', locals())


def resume_cv(request):
    cv_id = request.GET.get('cv_id', '')
    event = request.GET.get('event', '')

    cv = get_object_or_404(PersonalInformation, id=cv_id)
    ResumePartView.objects.create(resume=cv, part=event)

    return HttpResponse("")
