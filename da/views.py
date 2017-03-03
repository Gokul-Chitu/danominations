from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import nominationform
from .models import nomination
import csv
from django.utils.encoding import smart_str


def nominationfields(request):
    form = nominationform()
    if request.method=="POST":
        form =nominationform(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data['mobile_No']
            if len(mobile) > 10 or len(mobile) < 10:
                errors = 1
                return render(request,'nomination_templates/nominationform.html',{'form':form,'error':errors})

            else:
                rollno = form.cleaned_data['rollno']
                form.save()
                form =nominationform()
                queryset = nomination.objects.get(rollno =rollno )
                return redirect('send_email')
    return render(request,'nomination_templates/nominationform.html',{'form':form})

@login_required
def profile(request,pk):
    form =nomination.objects.get(id=pk)
    return render(request,'nomination_templates/profile.html',{'form':form})


@login_required
def registration(request):
    form = nomination.objects.all()
    count_president = form.filter(req_posistion='President').count()
    count_treasurer = form.filter(req_posistion='Treasurer').count()
    count_secretary = form.filter(req_posistion='Secretary').count()
    count_joint = form.filter(req_posistion='Joint Secretary').count()

    return render(request,'nomination_templates/registration.html',{'form':form,'cp':count_president,'cs':count_secretary,'cj':count_joint,'ct':count_treasurer})

@login_required
def presidentview(request):
    form = nomination.objects.filter(req_posistion='President')
    return render(request,'nomination_templates/participant.html',{'form':form})

@login_required
def treasurerview(request):
    form = nomination.objects.filter(req_posistion='Treasurer')
    return render(request,'nomination_templates/participant.html',{'form':form})

@login_required
def secretaryview(request):
    form = nomination.objects.filter(req_posistion='Secretary')
    return render(request,'nomination_templates/participant.html',{'form':form})

@login_required
def jointsecretaryview(request):
    form = nomination.objects.filter(req_posistion='Joint Secretary')
    return render(request,'nomination_templates/participant.html',{'form':form})

@login_required
def download(request):
    return render(request,'nomination_templates/download.html')

@login_required
def export_csv(request):
    form = nomination.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=nominations.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"Refernce Id"),
        smart_str(u"Roll No"),
        smart_str(u"Name"),
        smart_str(u"Gender"),
        smart_str(u"Year"),
        smart_str(u"Quota"),
        smart_str(u"Branch"),
        smart_str(u"CGPA"),
        smart_str(u"No of Arrears"),
        smart_str(u"Area of Residence"),
        smart_str(u"Type of Entry"),
        smart_str(u"Disciplinary Action Faced?"),
        smart_str(u"Mobile Number"),
        smart_str(u"Email"),
        smart_str(u"Position Applied"),
        smart_str(u"Things to be Implemented or Changed, If selected "),
        smart_str(u"Strengths"),
        smart_str(u"Reference Faculty 1	"),
        smart_str(u"Reference Faculty 2"),
        smart_str(u"Name of the Class Advisor"),




    ])
    for obj in form:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.rollno),
            smart_str(obj.name),
            smart_str(obj.gender),
            smart_str(obj.year),
            smart_str(obj.admission_type),
            smart_str(obj.branch),
            smart_str(obj.cgpa),
            smart_str(obj.no_of_arrears),
            smart_str(obj.area_of_residence),
            smart_str(obj.type_of_entry),
            smart_str(obj.faced_disciplinary_action),
            smart_str(obj.mobile_No),
            smart_str(obj.email_id),
            smart_str(obj.req_posistion),
            smart_str(obj.change_in_dept),
            smart_str(obj.strengths),
            smart_str(obj.reference1),
            smart_str(obj.reference2),
            smart_str(obj.class_advisor),

        ])
    return response
export_csv.short_description = u"Export CSV"

def signout(request):
    logout(request)
    return redirect('login')



from django.core.mail import EmailMessage, send_mail


def send_email(request):
    id = 7
    body = render_to_string('nomination_templates/email.html',{'id':id})
    send_mail(
        subject='Hello from SparkPost',
        message='Woo hoo! Sent from Django!',
        from_email='sandbox@sparkpostbox.com',
        recipient_list=['sagar.vidhya816@gmail.com'],
        html_message='<p>Hello Rock stars!</p>',
    )
    form = nominationform()
    return render(request,'nomination_templates/nominationform.html',{'form':form,'success':1})