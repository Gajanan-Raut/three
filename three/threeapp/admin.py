from django.contrib import admin
from threeapp.models import Task,Course

# Register your models here.
#admin.site.register(Task)
#admin.site.register(Course)

'''
class CourseAdmin(admin.ModelAdmin):
    #list_display=['id','cname','cdur','ccat','cprice']
    #list_display=('id','cname','cdur','ccat','cprice')
    list_display=('id',)

admin.site.register(Course,CourseAdmin)

# Method 2: by using decorator
@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
    list_display=['id','cname','cdur','ccat','cprice']

    '''
class FeesFilter(admin.SimpleListFilter):
    title=''
    parameter_name=""
    def lookups(self,request,models_admin):
        return(('high','Fees>=20000'),('low','Fees<20000'))
    def queryset(self,request,queryset):
        if self.value()=='high':
            return queryset.filter(cprice__gte=20000)
        elif self.value()=='low':
            return queryset.filter(cprice__lt=20000)
        else:
            return queryset.all()
@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
    list_display=['id','cname','cdur','ccat','cprice']
    list_filter=['ccat',FeesFilter]



admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display=['id','title','details','date','is_deletes']
