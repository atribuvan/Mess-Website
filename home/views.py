from .models import Allocation, Cafeteria, Caterer, Contact, longRebate, Period, Rule, shortRebate, Student, Forms, Semester
from .models.messperiod import messPeriod
from django.shortcuts import render, redirect
import datetime
from datetime import timedelta
from django.db.models import F, Sum
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import logout
# from django.contrib.admin import 
# Create your views here.

def home(request):
    return render(request, "home.html")

def rules(request):
    rules = Rule.objects.all()
    params = {
        "rule": rules,
    }
    print(params)
    return render(request, "rules.html", params)

def services(request):
  all_cafeteria_items = Cafeteria.objects.all()
  context = {
    'cafeteria_items': all_cafeteria_items,
  }
  return render(request, "cafeteria.html", context)

def con(request):
    all_obj = Contact.objects.all()
    context = {
    'contact_items': all_obj,
    }
    return render(request, "contact.html", context)

def caterer(request):
    caterer = Caterer.objects.all()
    context = {
        'caterer': caterer,
    }
    return render(request, "caterer.html", context)

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None and user.is_active:
            auth_login(request,user)
            return render(request,'index.html')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request, "login.html")

def logout(request):
    if request.user.is_authenticated:
        logout(request)
    # logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

def links(request):
    links = Forms.objects.all()
    context = {
        'links': links,
    }
    return render(request, "forms.html", context)

@login_required
def profile(request):
    text = ""
    student = Student.objects.filter(email__iexact=str(request.user.email)).last()
    socialaccount_obj = SocialAccount.objects.filter(provider='google', user_id=request.user.id)
    picture = "not available"
    allocation = Allocation.objects.filter(email=student).last()
    # short_rebate = shortRebate.objects.filter(student=student).all()
    allocation_info = {}
    #improve this alignment of text to be shown on the profile section
    if allocation:
        allocation_info_list = [allocation.student_id, allocation.caterer.name]
        allocation_info = {
            "Allocation ID": allocation.student_id,
            "Caterer": allocation.caterer.name,
            "Jain": "Yes" if allocation.jain else "No",
        }

    try:
        if len(socialaccount_obj):
            picture = socialaccount_obj[0].extra_data['picture']
    except:
        picture = "not available"
    context = {
        "text": text,
        "student":student, 
        "picture":picture,
        "allocation_info":allocation_info,
        # "short_rebate":short_rebate
    }
    return render(request, "profile.html", context)

@login_required(login_url='/login/')
def allocationForm(request):
    if request.method == 'POST':
        # student_email = request.POST['email']
        choice1_id = request.POST['choice1']
        choice2_id = request.POST['choice2']
        choice3_id = request.POST['choice3']

        st = Student.objects.filter(email__iexact=str(request.user.email)).last()

        print(choice1_id)

        caterer_choices = [
            choice1_id, choice2_id, choice3_id
        ]

        for cat in caterer_choices:
            cat_from_db = Caterer.objects.get(name=cat)
            if cat_from_db.current_no_students < cat_from_db.student_limit:
                cat_from_db.current_no_students += 1
                cat_from_db.save()
                st.caterer_alloted = cat_from_db
                st.alloted_id = cat_from_db.id_tobe_alloted + str(cat_from_db.current_no_students)
                st.save()
                return redirect('/')

        # No space available in any of the choices
        return redirect("/")

    # Render the form if GET request
    cats = Caterer.objects.all()
    student = Student.objects.filter(email__iexact=str(request.user.email)).last()
    return render(request, 'allocation.html', {'caterers': cats})

@login_required(login_url='/login/')
def shortRebateForm (request):
    student = Student.objects.filter(email__iexact=str(request.user.email)).last()
    semesters = Semester.objects.all() 
    mess_periods = messPeriod.objects.all()  
    return render(request, "shortrebate.html", {"semesters": semesters, "mess_periods": mess_periods})

@login_required(login_url='/login/')
def longRebateForm(request):
    student_email = Student.objects.filter(email__iexact=str(request.user.email)).last()
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        # reason = request.POST['reason']
        file = request.FILES.get('file', None)
        
        st = Student.objects.get(email=student_email)

        # Convert start and end dates to datetime objects
        start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')

        # Calculate the number of days for the rebate
        days_diff = (end_date_obj - start_date_obj).days + 1

        if days_diff > 7:
            try:
                rebate = longRebate(
                    student=st,
                    start_date=start_date_obj,
                    end_date=end_date_obj,
                    days=days_diff,
                    # reason=reason,
                    file=file
                )
                rebate.save()
                
                print("longrebate submitted successfully")
            except:
                print("Some error occured")
                return redirect('failure', student_email=student_email)
    # Render the form if GET request
    return render(request, 'longrebate.html', {'student': Student.objects.get(email=student_email)})

@login_required(login_url='/login/')
def adminJobs(request):
    return render(request, 'adminjobs.html')

def accept_longrebate(request):
    rebate = longRebate.objects.all()
    return render(request, 'accept_longrebate.html', {'rebate': rebate})

def edit_caterer(request):
    caterer = Caterer.objects.all()
    return render(request, 'edit_caterers.html', {'caterers': caterer})

def edit_cafeteria(request):
    cafeteria = Cafeteria.objects.all()
    return render(request, 'edit_cafeteria.html', {'cafeterias': cafeteria})

def add_semester(request):
    return render(request, 'add_semester.html')

def add_messperiod(request):
    semesters = Semester.objects.all()
    return render(request, 'add_messperiod.html', {'semesters': semesters})

# @login_required(login_url='/login/')
def viewShortRebates(request):
    selected_semester = request.GET.get('semester', None)
    selected_mess_period = request.GET.get('mess_period', None)

    # Fetch students with aggregated rebate information
    aggregated_rebates = shortRebate.objects.all()
    
    if selected_semester:
        aggregated_rebates = aggregated_rebates.filter(semester_id=selected_semester)
    if selected_mess_period:
        aggregated_rebates = aggregated_rebates.filter(mess_period_id=selected_mess_period)

    # Fetch all semesters and mess periods for filters
    semesters = Semester.objects.all()
    mess_periods = messPeriod.objects.all()

    return render(request, 'view_shortrebates.html', {
        'semesters': semesters,
        'mess_periods': mess_periods,
        'selected_semester': int(selected_semester) if selected_semester else None,
        'selected_mess_period': int(selected_mess_period) if selected_mess_period else None,
        'aggregated_rebates': aggregated_rebates
    })

