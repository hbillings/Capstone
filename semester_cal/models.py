from django.db import models

class Semester(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('semester', [self.pk,])

class Activity(models.Model):
    name = models.CharField(max_length=50)
    semester = models.ForeignKey(Semester)
    description = models.TextField()
    link = models.URLField(verify_exists=False, max_length=200)
    image = models.ImageField(upload_to='semester_cal', blank=True, null=True)
    tease = models.TextField(null=True,)
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.name
        return self.description
        
    class Meta:
        verbose_name_plural = "activities"