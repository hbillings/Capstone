from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail
from semester_cal.models import *
import os
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

semesters = Semester.objects.all()

urlpatterns = patterns('',
    # Example:
    # (r'^capstone/', include('capstone.foo.urls')),
    (r'^$', direct_to_template, 
        {
            'template' : 'index.html',
        },
        'home',),
    (r'^calendar/$', direct_to_template, 
            {
                'template' : 'semester_index.html',
            },
            'calendar',),
            
    (r'^calendar/(?P<object_id>\d+)/$', object_detail, 
	        {
	            'queryset' : semesters,
	            'template_name' : 'semester_detail.html',
	            'template_object_name' : 'semester',
	        },
	        'semester',
	),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^files/(.*)$', 'django.views.static.serve', 
        {'document_root': os.path.join(settings.PROJECT_PATH, 
        'media/')}, 'images'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
