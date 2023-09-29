from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount,Course,Topic,Difficultylevel,Category,Message

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = UserAccount
    ordering =['email']

    list_display = ('id','email',"is_staff",'display_courses','registered_on')
 
 
 #displaying multiple courses in admin panel
    def display_courses(self, obj):
        return ', '.join([course.Title for course in obj.courses.all()])

    display_courses.short_description = 'Courses Taken'

    fieldsets = (
        (None, {'fields': ('email', 'password','is_superuser')}),
        ('Courses', {'fields': ('courses',)}),
        
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','is_superuser'),
        }),
        
    )
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # New user being added
            obj.is_staff = True  # Set is_staff to True for all new users
            if 'is_superuser' in form.data and form.data['is_superuser'] == 'True':  # Check if the user is being registered as a superuser
                obj.is_superuser = True
        return super().save_model(request, obj, form, change)


    readonly_fields=('registered_on',)

    

admin.site.register(UserAccount, CustomUserAdmin)



class TopicAdmin(admin.ModelAdmin):
    list_display = ('Title', 'course', 'level')
    list_filter = ('course',)
    search_fields = ('Title', 'course__Title')

admin.site.register(Topic, TopicAdmin)


class CourseAdmin(admin.ModelAdmin):

    list_display = ('Title', 'category', 'course_photo',)  
    list_filter = ('category',)  
    search_fields = ('Title',)  
admin.site.register(Course, CourseAdmin)






admin.site.register(Difficultylevel)    

admin.site.register(Category)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message','date')

admin.site.register(Message, MessageAdmin)

