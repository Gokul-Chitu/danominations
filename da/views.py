from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import nominationform
from .models import nomination
import csv
from django.utils.encoding import smart_str
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def nominationfields(request):
    form = nominationform()
    if request.method == "POST":
        form = nominationform(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data['mobile_No']
            if len(mobile) > 10 or len(mobile) < 10:
                errors = 1
                return render(request, 'nomination_templates/nominationform.html', {'form': form, 'error': errors})
            else:
                nomi = form.save()
                success = 1
                usermail = nomi.email_id
                sendmail(usermail)
                queryset = nomination.objects.filter(rollno=nomi.rollno).order_by('-applied_at')[0]
                form = nominationform()
                return render(request, 'nomination_templates/nominationform.html',
                              {'success': success, 'form': form, 'id': queryset.id})
    return render(request, 'nomination_templates/nominationform.html', {'form': form})


@login_required
def profile(request, pk):
    form = nomination.objects.get(id=pk)
    return render(request, 'nomination_templates/profile.html', {'form': form})


@login_required
def registration(request):
    form = nomination.objects.all()
    count_president = form.filter(req_posistion='President').count()
    count_treasurer = form.filter(req_posistion='Treasurer').count()
    count_secretary = form.filter(req_posistion='Secretary').count()
    count_joint = form.filter(req_posistion='Joint Secretary').count()
    return render(request, 'nomination_templates/registration.html',
                  {'form': form, 'cp': count_president, 'cs': count_secretary, 'cj': count_joint,
                   'ct': count_treasurer})


@login_required
def presidentview(request):
    form = nomination.objects.filter(req_posistion='President')
    page = request.GET.get('page',1)
    paginator = Paginator(form, 10)
    try:
        num = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        num = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        num = paginator.page(paginator.num_pages)
    return render(request, 'nomination_templates/participant.html', {'num':num})


@login_required
def treasurerview(request):
    form = nomination.objects.filter(req_posistion='Treasurer')
    page = request.GET.get('page',1)
    paginator = Paginator(form, 10)
    try:
        num = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        num = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        num = paginator.page(paginator.num_pages)
    return render(request, 'nomination_templates/participant.html', {'num': num})


@login_required
def secretaryview(request):
    form = nomination.objects.filter(req_posistion='Secretary')
    page = request.GET.get('page',1)
    paginator = Paginator(form, 10)
    try:
        num = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        num = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        num = paginator.page(paginator.num_pages)
    return render(request, 'nomination_templates/participant.html', {'num': num})


@login_required
def jointsecretaryview(request):
    form = nomination.objects.filter(req_posistion='Joint Secretary')
    page = request.GET.get('page',1)
    paginator = Paginator(form, 10)
    try:
        num = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        num = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        num = paginator.page(paginator.num_pages)
    return render(request, 'nomination_templates/participant.html', {'num': num})

@login_required
def download(request):
    return render(request, 'nomination_templates/download.html')


@login_required
def export_csv(request):
    form = nomination.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=nominations.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)
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
            smart_str(obj.history_of_arrears),
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
            smart_str(obj.applied_at),

        ])
    return response


export_csv.short_description = u"Export CSV"


def signout(request):
    logout(request)
    return redirect('login')

def sendmail(usermail):
    htmly = get_template('nomination_templates/email.html')
    text_content = ''
    html_content = htmly.render()
    subject = 'KCT DA | Nominations'
    from_email = 'da.nomination@kct.ac.in'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [usermail])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

