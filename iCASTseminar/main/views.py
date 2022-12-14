from django.shortcuts import render

def main(request):
    '''
    Render the main page
    '''
    context = {'like':'main'}
    return render(request, 'main/main.html', context)

def CallForPapers(request):
    '''
    Render the main page
    '''
    context = {'like':'CallForPapers'}
    return render(request, 'main/CallForPapers.html', context)

def PaperSubmission(request):
    context = {'like':'PaperSubmission'}
    return render(request, 'main/PaperSubmission.html', context)
    
def SpecialSessionSubmission(request):
    context = {'like':'SpecialSessionSubmission'}
    return render(request, 'main/SpecialSessionSubmission.html', context)

def Publication(request):
    context = {'like':'Publication'}
    return render(request, 'main/Publication.html', context)

def ImportantDates(request):
    context = {'like':'ImportantDates'}
    return render(request, 'main/ImportantDates.html', context)

def CameraReadyPaperSubmission(request):
    context = {'like':'CameraReadyPaperSubmission'}
    return render(request, 'main/CameraReadyPaperSubmission.html', context)

def Registration(request):
    context = {'like':'Registration'}
    return render(request, 'main/Registration.html', context)

def OrganizingCommittee(request):
    context = {'like':'OrganizingCommittee'}
    return render(request, 'main/OrganizingCommittee.html', context)

def ConferenceProgram(request):
    context = {'like':'ConferenceProgram'}
    return render(request, 'main/ConferenceProgram.html', context)

def KeynoteSpeakers(request):
    context = {'like':'KeynoteSpeakers'}
    return render(request, 'main/KeynoteSpeakers.html', context)

def Sponsors(request):
    context = {'like':'Sponsors'}
    return render(request, 'main/Sponsors.html', context)

def BestPaperAward(request):
    context = {'like':'BestPaperAward'}
    return render(request, 'main/BestPaperAward.html', context)

def PreviousConference(request):
    context = {'like':'PreviousConference'}
    return render(request, 'main/PreviousConference.html', context)

def AboutChaoyangUniversityofTechnology(request):
    context = {'like':'AboutChaoyangUniversityofTechnology'}
    return render(request, 'main/AboutChaoyangUniversityofTechnology.html', context)

def VenueAndAccommodation(request):
    context = {'like':'VenueAndAccommodation'}
    return render(request, 'main/VenueAndAccommodation.html', context)
 