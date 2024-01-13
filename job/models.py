from django.db import models

# django-> models.Model why?? -> model fields:
#     -html widget
#     -validation
#     -db size

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    imagename, extention = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extention)

# Create your models here.
class Job(models.Model): #table
    #django will create id table by default unless we created another table has a primary key
    
    title = models.CharField(max_length=100) #column or field
    # location
    job_type=models.CharField(max_length=20,choices=JOB_TYPE)
    description=models.TextField()
    published_at=models.DateTimeField(auto_now=True) #this field doesn't show because it is automatically created
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    category=models.ForeignKey('Category',on_delete=models.CASCADE) #we put single qoutes because the Category model has not come yet , if we previosly defined it we can type Category without qoutes 
    experience=models.IntegerField(default=0)
    image=models.ImageField(upload_to=image_upload)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name=models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
