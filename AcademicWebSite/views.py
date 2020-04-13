from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import AcademicGroupInformation, ResearchField, ContactRequest, Publications, Member


class AcademicWebExplanationPageView(TemplateView):
    template_name = 'academic_website.html'


class HomeAcademicWebPageView(TemplateView):
    template_name = 'home_academic_website.html'

    def group_information_list(self):
        return AcademicGroupInformation.objects.get(pk=1)


class PublicationsListAcademicWebPageView(ListView):
    model = Publications
    template_name = 'publications_academic_website.html'

    def group_information_list(self):
        return AcademicGroupInformation.objects.get(pk=1)

    def paperslists(self):
        return Publications.objects.filter(
            publication_type='Paper').order_by('-year')

    def reviewslists(self):
        return Publications.objects.filter(
            publication_type='Review').order_by('-year')

    def chapterslists(self):
        return Publications.objects.filter(
            publication_type='Chapter').order_by('-year')

    def proceedingslists(self):
        return Publications.objects.filter(
            publication_type='Proceeding').order_by('-year')


class MembersAcademicWebPageView(TemplateView):
    template_name = 'members_academic_website.html'

    def group_information_list(self):
        return AcademicGroupInformation.objects.get(pk=1)

    def currentmemberslist(self):
        return Member.objects.filter(
            final_year=0)

    def currentPI(self):
        return GroupInformation.objects.get(pk=1)

    def currentpostdocs(self):
        return Member.objects.filter(final_year=0, position='Postdoc')

    def currentphds(self):
        return Member.objects.filter(final_year=0, position='PhD')

    def currenttechnicians(self):
        return Member.objects.filter(final_year=0, position='Technician')

    def currentmasterstudents(self):
        return Member.objects.filter(final_year=0, position='MSc')

    def currentguestphdstudents(self):
        return Member.objects.filter(final_year=0, position='Guest_PhD')

    def currentgueststudents(self):
        return Member.objects.filter(final_year=0, position='Guest_Student')

    def previousmemberslist(self):
        return Member.objects.exclude(final_year=0).order_by('-initial_year')

    def previouspostdocs(self):
        return Member.objects.exclude(final_year=0).filter(position='Postdoc').order_by('-initial_year')

    def previousphds(self):
        return Member.objects.exclude(final_year=0).filter(position='PhD').order_by('-initial_year')

    def previoustechnicians(self):
        return Member.objects.exclude(final_year=0).filter(position='Technician').order_by('-initial_year')

    def previousmasterstudents(self):
        return Member.objects.exclude(final_year=0).filter(position='MSc').order_by('-initial_year')

    def previousguestphdstudents(self):
        return Member.objects.exclude(final_year=0).filter(position='Guest_PhD').order_by('-initial_year')

    def previousgueststudents(self):
        return Member.objects.exclude(final_year=0).filter(position='Guest_Student').order_by('-initial_year')


class ResearchAcademicWebPageView(ListView):
    model = ResearchField
    template_name = 'research_academic_website.html'

    def group_information_list(self):
        return AcademicGroupInformation.objects.get(pk=1)


class ResearchFieldAcademicWebPageView(DetailView):
    model = ResearchField
    template_name = 'researchfield_academic_website.html'

    def group_information_list(self):
        return AcademicGroupInformation.objects.get(pk=1)


class ContactAcademicWebPageView(CreateView):
    model = ContactRequest
    template_name = 'contact_academic_website.html'
    fields = '__all__'

    def group_information_list(self):
        return AcademicGroupInformation.objects.get(pk=1)


class RequestReceivedAcademicWebPageView(TemplateView):
    template_name = 'request_received_academic_website.html'

    def group_information_list(self):
        return AcademicGroupInformation.objects.get(pk=1)
