from django.shortcuts import render
from portfolio.models import Project
# Create your views here.


def landing_page(request):
    return render(request, "landing_page.html", {})


def project_index(request):
    projects = Project.objects.all()  # performing a query for CRUD
    context = {
        'projects': projects
    }  # assigning the query set into the dictionary to eventually send it to our template.
#  (ever view function need a context dict)
    return render(request, 'project_index.html', context)
    # any entry in the context dictionary is passed to the template via render function


def project_detail(request, pk):
    """pk: project id"""
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)



