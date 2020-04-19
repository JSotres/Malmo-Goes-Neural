from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.views.generic import TemplateView, ListView
from .forms import SimpsonForm
from .models import SimpsonCharacter
from .local_python_scripts import ev_simpson


def SimpsonsGoNeuralApplicationView(request):
    if request.method == "POST":
        form = SimpsonForm(request.POST, request.FILES)
        print('aqui0')
        if form.is_valid():
            print('aqui')
            simpsonEx = SimpsonCharacter()
            # print(form.cleaned_data['simpson_input_picture'])
            # simpsonEx.simpson_input_picture = form.cleaned_data['simpson_input_picture']
            simpsonEx.simpson_input_picture = request.FILES['simpson_input_picture']
            simpsonEx.save()
            print(simpsonEx.simpson_input_picture.url)
            # simpsonEx.simpson_input_picture = form.simpson_input_picture
            #simpsonEx.save()
            simpsonEx.simpson_output_picture = ev_simpson(simpsonEx.simpson_input_picture.url,
                simpsonEx.pk)
            simpsonEx.save()
            print(simpsonEx.simpson_input_picture.url)
            print(simpsonEx.simpson_output_picture.url)
            # return redirect('simpsons_go_neural_application', pk=simpsonEx.pk)
            return render(request, 'simpsons_go_neural_application.html',
                {'simpsonEx': simpsonEx})
    else:
        return render(request, 'simpsons_go_neural_application.html',
            {'simpsonEx': SimpsonCharacter})
    
