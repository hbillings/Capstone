from models import *
from django.http import HttpResponse

def nav_context_processor(request):
    """make sure the things needed to render the nav are present in every page"""
    to_context = {}
    to_context['semesters'] = Semester.objects.all()
    return to_context