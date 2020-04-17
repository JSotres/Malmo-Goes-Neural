from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import ContactRequest, Project


class HomePageView(TemplateView):
    template_name = 'home.html'


class ProjectListView(ListView):
    model = Project
    template_name = 'projectlist.html'

    def django_list(self):
        return Project.objects.filter(
            project_type='ML & Django')

    def cv_list(self):
        return Project.objects.filter(
            project_type='Computer_Vision')

    def other_list(self):
        return Project.objects.filter(
            project_type='Other')

    def __str__(self):
        return self.name


class ProjectView(DetailView):
    model = Project
    template_name = 'project.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(CreateView):
    model = ContactRequest
    template_name = 'contact.html'
    fields = '__all__'


class RequestReceivedPageView(TemplateView):
    template_name = 'request_received.html'

