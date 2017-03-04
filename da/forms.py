from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import nomination


class nominationform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(nominationform, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit("submit", "Submit"))

    class Meta:
        model = nomination
        exclude = ()
        labels = {'name': 'Name', 'rollno': 'Roll No', 'gender': 'Gender', 'year': 'Year',
                  'branch': 'Branch', 'cgpa': 'CGPA upto current semester','history_of_arrears':'History of Arrears', 'no_of_arrears': 'No of Standing Arrears',
                  'admission_type': 'Admission Type', 'area_of_residence': 'Area of Residence',
                  'type_of_entry': 'Type of Entry', 'faced_disciplinary_action': 'Faced Any Disciplinary Action?',
                  'mobile_No': 'Mobile Number', 'email_id': 'Email',
                  'req_posistion': 'Position for which you would like to be considered',
                  'change_in_dept': 'List any two points that you would like to implement/change, if you are selected',
                  'strengths': 'List your strengths (any 2) which you think makes you an ideal candidate:',
                  'reference1': 'Reference Faculty 1', 'reference2': 'Reference Faculty 2',
                  'class_advisor': 'Name of the Class Advisor'}
