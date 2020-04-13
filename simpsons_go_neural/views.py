from django.views.generic import DetailView, TemplateView
# from ..main_pages.models import Project


class SimpsonsGoNeuralExplanationView(TemplateView):
#    model = Project
    template_name = 'simpsons_go_neural.html'


class SimpsonsGoNeuralApplicationView(TemplateView):
#    model = Project
    template_name = 'simpsons_go_neural_application.html'
