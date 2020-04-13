from django.urls import path
from .views import HomeAcademicWebPageView, ResearchAcademicWebPageView, PublicationsListAcademicWebPageView, MembersAcademicWebPageView, ContactAcademicWebPageView, ResearchFieldAcademicWebPageView, AcademicWebExplanationPageView

urlpatterns = [
    path('AcademicWebSite/academic_website', AcademicWebExplanationPageView.as_view(), name='academic_website'),
    path('AcademicWebSite/home_academic_website', HomeAcademicWebPageView.as_view(), name='home_academic_website'),
    path('AcademicWebSite/research_academic_website', ResearchAcademicWebPageView.as_view(), name='research_academic_website'),
    path('AcademicWebSite/publications_academic_website', PublicationsListAcademicWebPageView.as_view(), name='publications_academic_website'),
    path('AcademicWebSite/members_academic_website', MembersAcademicWebPageView.as_view(), name='members_academic_website'),
    path('AcademicWebSite/contact_academic_website', ContactAcademicWebPageView.as_view(), name='contact_academic_website'),
    path('AcademicWebSite/researchfield/<int:pk>/', ResearchFieldAcademicWebPageView.as_view(), name='researchfield_academic_website'),
    ]
