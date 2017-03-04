from django.db import models


# Create your models here.
class nomination(models.Model):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    firstyear = 1
    secondyear = 2
    thirdyear = 3
    POS_CHOICES = (('President', 'President/Vice President (Batch 2014-18)'), ('Tresurer', 'Tresurer (Batch 2014-18)'),
                   ('Secretary', 'Secretary (Batch 2015-19)'), ('Joint Secretary', 'Join Secretary (Batch 2016-20)'))

    rollno = models.CharField(max_length=8, null=True,)
    name = models.CharField(max_length=255)
    gender = models.IntegerField(choices=GENDER_CHOICES,default="Male")
    YEAR_CHOICES = (
    (firstyear, 'I (Batch 2016-20)'), (secondyear, 'II (Batch 2015-19)'), (thirdyear, 'III (Batch 2014-18)'))
    year = models.IntegerField(choices=YEAR_CHOICES, default=firstyear)
    BRANCH_CHOICES = (
    ('Aeronautical Engineering', 'Aeronautical Engineering'), ('Automobile Engineering', 'Automobile Engineering'),
    ('Bio-Technology', 'Bio-Technology'), ('Civil Engineering', 'Civil Engineering'),
    ('Computer Applications', 'Computer Applications'),
    ('Computer Science and Engineering', 'Computer Science and Engineering')
    , ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'),
    ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'),
    ('Electronics and Instrumentation Engineering', 'Electronics and Instrumentation Engineering'),
    ('Fashion Technology', 'Fashion Technology'),
    ('Information Technology', 'Information Technology'),
    ('Management Studies', 'Management Studies'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Mechatronics Engineering', 'Mechatronics Engineering'),
    ('Science and Humanities', 'Science and Humanities'),
    ('Textile Technology', 'Textile Technology'))
    branch = models.CharField(choices=BRANCH_CHOICES, default='Aernonautical Engineering', max_length=255)
    cgpa = models.FloatField(max_length=3)
    no_of_arrears = models.IntegerField()
    history_of_arrears = models.IntegerField(default=0)
    ADM_TYPE_CHOICES = (('Counselling', 'Counselling'), ('Management', 'Management'))
    admission_type = models.CharField(choices=ADM_TYPE_CHOICES, default='Counselling', max_length=255)
    RESIDENCE_CHOICES = (('Urban', 'Urban'), ('Rural', 'Rural'))
    area_of_residence = models.CharField(choices=RESIDENCE_CHOICES, default='Urban', max_length=255)
    TYPE_OF_ENTRY = (('Regular Entry', 'Regular Entry'), ('Lateral Entry', 'Lateral Entry'))
    type_of_entry = models.CharField(choices=TYPE_OF_ENTRY, default='Regular Entry', max_length=255)
    DISCIPLINARY_CHOICES = (('YES', 'YES'), ('NO', 'NO'))
    faced_disciplinary_action = models.CharField(default='NO', choices=DISCIPLINARY_CHOICES, max_length=255)
    mobile_No = models.CharField(max_length=10, help_text='Only 10 digits')
    email_id = models.CharField(max_length=255)
    req_posistion = models.CharField(choices=POS_CHOICES, max_length=255)
    change_in_dept = models.TextField(max_length=255, null=True)
    strengths = models.TextField(max_length=255, null=True)
    reference1 = models.CharField(max_length=255)
    reference2 = models.CharField(max_length=255)
    class_advisor = models.CharField(max_length=255)
    applied_at = models.DateTimeField(auto_now_add=True, null=True)
