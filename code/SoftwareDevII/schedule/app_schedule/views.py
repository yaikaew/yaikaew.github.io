from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from app_select.models import Subjects_Test_Date
from app_schedule.models import Subjects_info , User_subjects
from app_select.views import start_times,user_data
from django.db.models import Q



# Create your views here.
@login_required(login_url='login')
def schedule_view(request):
    sub_date = Subjects_Test_Date.objects.all()
    sub_objects = Subjects_info.objects.all()
    user_id = request.user.id
    user = User_subjects.objects.filter(user_id_id = user_id)

    day_start_times_used = user_data[user_id]['day_start_times_used']
    
    days = {
    "M": "Monday",
    "T": "Tuesday",
    "W": "Wednesday",
    "H": "Thursday",
    "F": "Friday",
    "S": "Sunday",
}
    
    # The select button was clicked
    subject_id = request.POST.get('id')
    # insert name into user table using Django ORM
    User_subjects.objects.create(user_id_id=user_id, sub_id_id=subject_id)

    context = {'sub_date':sub_date, 
               'sub_objects':sub_objects,
               'users':user,
               'start_times':start_times,
               'day_start_times_used':day_start_times_used,
               'days':days}
    
    return render(request, 'schedule.html' , context)

def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def test(request):
    sub_objects = Subjects_info.objects.all()
    user_all = User_subjects.objects.all()

    if 'search_select' in request.GET:
        search2 = request.GET['search_select']
        multiple_search2 = Q(Q(name__icontains=search2) | Q(code__icontains=search2))
        sub_select = Subjects_info.objects.filter(multiple_search2)
    else:
        sub_select = Subjects_info.objects.none()



    context = { 'sub_objects':sub_objects,
                'user_all':user_all,
                'sub_select':sub_select,}


    return render(request, 'test.html' , context)