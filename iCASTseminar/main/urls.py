from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('CallForPapers/', views.CallForPapers, name='CallForPapers'),
    path('PaperSubmission/', views.PaperSubmission, name='PaperSubmission'),
    path('SpecialSessionSubmission/', views.SpecialSessionSubmission, name='SpecialSessionSubmission'),
    path('Publication/', views.Publication, name='Publication'),
    path('ImportantDates/', views.ImportantDates, name='ImportantDates'),
    path('CameraReadyPaperSubmission/', views.CameraReadyPaperSubmission, name='CameraReadyPaperSubmission'),
    path('Registration/', views.Registration, name='Registration'),
    path('OrganizingCommittee/', views.OrganizingCommittee, name='OrganizingCommittee'),
    path('ConferenceProgram/', views.ConferenceProgram, name='ConferenceProgram'),
    path('KeynoteSpeakers/', views.KeynoteSpeakers, name='KeynoteSpeakers'),
    path('Sponsors/', views.Sponsors, name='Sponsors'),
    path('BestPaperAward/', views.BestPaperAward, name='BestPaperAward'),
    path('AboutChaoyangUniversityofTechnology/', views.AboutChaoyangUniversityofTechnology, name='AboutChaoyangUniversityofTechnology'),
    path('VenueAndAccommodation/', views.VenueAndAccommodation, name='VenueAndAccommodation'),
]