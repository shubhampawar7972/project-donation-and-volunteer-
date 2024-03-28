from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from .forms import UserForm, DonorSignupForm
from django.http import HttpResponseRedirect

class IndexView(View):
    def get(self, request):
        return render(request, "index.html")

class GalleryView(View):
    def get(self, request):
        return render(request, "gallery.html")

def index_admin():
    pass
class LoginAdminView(View):
    def get(self, request):
        return render(request, "login-admin.html")

class LoginDonorView(View):
    def get(self, request):
        return render(request, "login-donor.html")

class LoginVolunteerView(View):
    def get(self, request):
        return render(request, "login-volunteer.html")
def pending_donation():
    pass
def accepted_donation():
    pass
def rejected_donation():
    pass
def volunteerallocated_donation():
    pass
def donationnotrec_admin():
    pass
def donationrec_admin():
    pass
def donationdelivered_admin():
    pass
def all_donations():
    pass
def manage_donor():
    pass
def new_volunteer():
    pass

def accepted_volunteer():
    pass
def rejected_volunteer():
    pass
def all_volunteer():
    pass
def add_area():
    pass
def edit_area():
    pass    
def manage_area():
    pass
def changepwd_admin():
    pass
def logout(request):
    pass
'''def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('index') '''  
def logout_view(request):
    logout(request)
    # Redirect to a success page or the homepage
    return redirect('index')     
def accepted_donationdetail():
    pass      
def view_volunteerdetail():
    pass
def view_donordetail():
    pass
def view_donationdetail():
    pass
def index_donor(request): 
     return render(request, "index-donor.html")

def donate_now():
    pass
def donation_history():
    pass
def profile_donor():
    pass
def changepwd_donor():
    pass
def index_volunteer():
    pass
def collection_req():
    pass
def donationrec_volunteer():
    pass
def donationnotrec_volunteer():
    pass
def donationdelivered_volunteer():
    pass
def profile_volunteer():
    pass
def changepwd_volunteer():
    pass
def donationdetail_donor():
    pass
def donationrec_detail():
    pass
def donationcollection_detail():
    pass
'''def logout_view(request):
    pass'''



class SignupDonorView(View):
    def get(self, request):
        form1 = UserForm()
        form2 = DonorSignupForm()
        return render(request, "signup_donor.html", {'form1': form1, 'form2': form2})

    def post(self, request):
        # Handle form submission
        return render(request, "signup_donor.html")

class SignupVolunteerView(View):
    def get(self, request):
        # Your view logic here
        return render(request, "signup_volunteer.html")

class IndexAdminView(View):
    def get(self, request):
        return render(request, "index-admin.html")

# Define other views as needed...
