from django.shortcuts import render, redirect, get_object_or_404
from . models import Analytic, Team, Report
from django.http import JsonResponse
import os

#ensure the API key is loaded from the environment
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
#GEMINI_API_URL =   

# Create your views here.
def index(request):
    context = {}
    Analytics = Analytic.objects.all()
    context['analytics'] = Analytics

    """getting all team members"""
    Teams = Team.objects.all()
    context['Teams'] = Teams
    return render(request, 'index.html', context)


#report a missing updatedChild
def report(request):
    """define the report.html backend"""
    if request.method == 'POST':
        firstName = request.POST['firstName']
        middleName = request.POST['middleName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        gender = request.POST['gender']
        age = request.POST['age']
        height = request.POST['height']
        skinTone = request.POST['skinTone']
        location = request.POST['location']
        dressing = request.POST['dressing']
        profilePhoto = request.POST['profilePhoto']
        status = request.POST['status']
        #mapping each entry in a new report
        newReport = Report(firstName=firstName, middleName=middleName, lastName=lastName, email=email,\
                           gender=gender, age=age, height=height, skinTone=skinTone, location=location, dressing=dressing,\
                            profilePhoto=profilePhoto, status = status)
        
        newReport.save()

    return render(request, 'report.html')

def base(request):
    """rendering the base file for testing purposes"""
    return render(request, 'base.html')

#reported
def reportedChildren(request):
    """rendering all reported updatedChildren"""
    context = {}
    reportedChildren = Report.objects.all()
    context['reportedChildren'] =  reportedChildren
    return render(request, 'reportedChildren.html', context)

# reportedChildren search
def search(request):
    """logic for the search bar and button"""
    if request.method == 'GET':
        search = request.GET['search']
        posts = Report.objects.filter(firstName = search)
        return render(request, 'search.html', {'posts':posts})

#customAdmin
def customAdmin(request):
    reportedChildren = Report.objects.all()
    context = {'reportedChildren' : reportedChildren }
    return render(request, 'customAdmin.html', context)

#admin update button
def updateDetails(request, id): 
    updateChild = get_object_or_404(Report, id=id)
    reportedChildImage = updateChild.profilePhoto.url
    if request.method == 'POST':
        updateChild.firstName = request.POST.get('firstName')
        updateChild.middleName = request.POST.get('middleName')
        updateChild.lastName = request.POST.get('lastName')
        updateChild.email = request.POST.get('email')
        updateChild.gender = request.POST.get('gender')
        updateChild.age = request.POST.get('age')
        updateChild.height = request.POST.get('height')
        updateChild.skinTone = request.POST.get('skinTone')
        updateChild.location = request.POST.get('location')
        updateChild.dressing = request.POST.get('dressing')
        new_profile_photo = request.FILES.get('profilePhoto')  # Use FILES for image uploads

        if new_profile_photo:
            # If a new image is uploaded, update the field
            updateChild.profilePhoto = new_profile_photo
        else:
            # If no new image is provided, keep the existing image
            # This line isn't necessary unless you overwrite the field elsewhere
            pass
        updateChild.status = request.POST.get('status')
        updateChild.save()
    context = { 'updateChild':updateChild,'reportedChildImage': reportedChildImage }
    return render(request, 'update.html', context)

# customAdmin/delete
def delete(request, id):
    deleteChild = Report.objects.get(id=id)
    deleteChild.delete()
    return redirect('customAdmin')

#generateDetails
def generateDetails(request, id):
    """logic and back end for the generate Details button in reported page"""
    reportedChild = Report.objects.get(id=id)
    email = reportedChild.email
    context = {'reportedChild': reportedChild, 'email':email}

    return render(request, 'generateDetails.html', context)
