from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from home.models import longRebate, Caterer, Cafeteria, Semester, Student, shortRebate
from home.models.messperiod import messPeriod
import json
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import F, Sum

def update_rebate_status(request):
    if request.method == 'POST':
        rebate_id = request.POST.get('id')
        action = request.POST.get('action')

        try:
            rebate = longRebate.objects.get(id=rebate_id)
            
            if action == 'accept':
                rebate.approved = True
            elif action == 'reject':
                rebate.approved = False
            
            rebate.save()
            
            return JsonResponse({'success': True})
        except longRebate.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Rebate does not exist'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def add_caterer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        student_limit = request.POST.get('student_limit')
        rebate_rate = request.POST.get('rebate_rate')
        id_tobe_alloted = request.POST.get('id_tobe_alloted')
        amount_tobe_paid = request.POST.get('amount_tobe_paid')
        image = request.FILES.get('image')

        caterer = Caterer.objects.create(
            name=name,
            email=email,
            student_limit=student_limit,
            rebate_rate=rebate_rate,
            id_tobe_alloted=id_tobe_alloted,
            amount_tobe_paid=amount_tobe_paid,
            image=image
        )

        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def update_caterer_info(request):
    if request.method == 'POST':
        caterer_id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        student_limit = request.POST.get('student_limit')
        rebate_rate = request.POST.get('rebate_rate')
        id_tobe_alloted = request.POST.get('id_tobe_alloted')
        amount_tobe_paid = request.POST.get('amount_tobe_paid')
        image = request.FILES.get('image')

        caterer = Caterer.objects.get(id=caterer_id)
        caterer.name = name
        caterer.email = email
        caterer.student_limit = student_limit
        caterer.rebate_rate = rebate_rate
        caterer.id_tobe_alloted = id_tobe_alloted
        caterer.amount_tobe_paid = amount_tobe_paid
        caterer.image = image

        caterer.save()

        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def get_caterer_info(request, caterer_id):
    caterer = Caterer.objects.get(id=caterer_id)
    data = {
        'success': True,
        'caterer': {
            'name': caterer.name,
            'email': caterer.email,
            'student_limit': caterer.student_limit,
            'rebate_rate': caterer.rebate_rate,
            'id_tobe_alloted': caterer.id_tobe_alloted,
            'amount_tobe_paid': caterer.amount_tobe_paid,
        }
    }
    return JsonResponse(data)

def add_cafeteria(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        phone_number = request.POST.get('phone_number', '')
        image = request.FILES.get('image')

        cafeteria = Cafeteria.objects.create(
            name=name,
            description=description,
            phone_number=phone_number,
            image=image
        )

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

# @csrf_exempt
def get_cafeteria(request, id):
    cafeteria = Cafeteria.objects.get(id=id)
    data = {
        'success': True,
        'cafeteria': {
            'name': cafeteria.name,
            'description': cafeteria.description,
            'phone_number': cafeteria.phone_number,
            # 'image':cafeteria.image.url    Need to fix this
        }
    }
    return JsonResponse(data)

def update_cafeteria(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        phone_number = request.POST.get('phone_number', '')
        image = request.FILES.get('image')

        cafeteria = Cafeteria.objects.get(id=id)
        cafeteria.name = name
        cafeteria.description = description
        cafeteria.phone_number = phone_number
        if image:
            cafeteria.image = image

        cafeteria.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def add_semester(request):
    if request.method == 'POST':
        semester_name = request.POST.get('semester')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        try:
            semester = Semester.objects.create(
                name=semester_name,
                start_date=start_date,
                end_date=end_date
            )
            return JsonResponse({'success': True})
        except Exception as e:
            print(e)  # Log the error for debugging
            return JsonResponse({'success': False})

def add_mess_period(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        semester_id = request.POST.get('semester')

        try:
            semester = Semester.objects.get(id=semester_id)
            mess_period = messPeriod.objects.create(
                start_date=start_date,
                end_date=end_date,
                semester=semester
            )
            return JsonResponse({'success': True})
        except Exception as e:
            print(e)  # Log the error for debugging
            return JsonResponse({'success': False})

def get_dates(request, semester_id, mess_period_id):
    try:
        semester = Semester.objects.get(id=semester_id)
        mess_period = messPeriod.objects.get(id=mess_period_id, semester=semester)

        data = {
            'min_date': str(mess_period.start_date),
            'max_date': str(mess_period.end_date)
        }

        return JsonResponse(data)

    except (Semester.DoesNotExist, messPeriod.DoesNotExist):
        return JsonResponse({'error': 'Semester or mess period not found'}, status=404)
    

def shortRebateForm (request):
    now = datetime.datetime.now()
    if request.method == "POST":
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        semester_id = request.POST.get("semester")
        mess_period_id = request.POST.get("mess_period")

        student = Student.objects.filter(email__iexact=str(request.user.email)).last()

        # Retrieve the selected semester and mess period
        try:
            semester = Semester.objects.get(id=semester_id)
            mess_period = messPeriod.objects.get(id=mess_period_id)
        except (Semester.DoesNotExist, messPeriod.DoesNotExist):
            return JsonResponse({"error": "Invalid semester or mess period."})

        print(semester, mess_period)

        # Convert start and end dates to datetime objects
        start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        now_obj = datetime.datetime.strptime(now.strftime('%Y-%m-%d'), '%Y-%m-%d')

        print(mess_period.end_date, mess_period.start_date, now_obj)
        print(start_date_obj, end_date_obj, now_obj)

        if start_date_obj.month != end_date_obj.month:
            return JsonResponse({"error": "Rebate duration should be within a single month. If you want to apply for application spanning multiple months, please apply separately for each month."})

        if start_date_obj < now_obj:
            return JsonResponse({"error": "Start date cannot be in the past."})
        
        if end_date_obj < start_date_obj:
            return JsonResponse({"error": "End date cannot be before start date."})
        
        if start_date_obj > end_date_obj:
            return JsonResponse({"error": "Start date cannot be after end date."})
        
        if (start_date_obj - now_obj).days < 2:
            return JsonResponse({"error": "Start date should be at least 2 days after the present date."})

        # Calculate the number of days for the rebate
        days_difference = (end_date_obj - start_date_obj).days + 1
        
        if days_difference < 2 or days_difference > 7:
            return JsonResponse({"error": "Short term rebate should be applied for 2-7 consecutive days."})

        # Validate maximum days per month
        rebates = shortRebate.objects.filter(
            student_applied=student,
            mess_period=mess_period
        ).annotate(
            days_difference=F('end_date') - F('start_date')
        ).aggregate(
            total_days=Sum('days_difference')
        )['total_days']
        
        if rebates and (rebates.days + days_difference) > 8:
            return JsonResponse({"error": "Maximum of 8 days/month of rebate can be availed."})
        
        existing_rebate = shortRebate.objects.filter(
            student_applied=student,
            start_date=start_date,
            end_date=end_date
        ).exists()

        if existing_rebate:
            return JsonResponse({"error": "You have already applied for rebate for the selected dates."})

        amount = student.caterer_alloted.rebate_rate * days_difference
        student.rebate_amount += amount
        student.shortrebate_days += days_difference
        student.save()

        student.caterer_alloted.amount_tobe_paid -= amount
        student.caterer_alloted.save()

        # Save the rebate application
        rebate = shortRebate(
            student_applied=student,
            rebating_caterer=student.caterer_alloted,  
            start_date=start_date,
            end_date=end_date,
            mess_period=mess_period,
            semester=semester,
            days_applied=days_difference,
            amount=amount
        )
        rebate.save()

        return JsonResponse({"success": "Rebate applied successfully!"})

    student = Student.objects.filter(email__iexact=str(request.user.email)).last()
    semesters = Semester.objects.all()  # Assuming Student has a ManyToManyField to Semester
    mess_periods = messPeriod.objects.all()  # Assuming Student has a ManyToManyField to MessPeriod
    return render(request, "shortrebate.html", {"semesters": semesters, "mess_periods": mess_periods})
