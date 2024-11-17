from django.contrib import admin
from.models import Employee,Department,EmpAttendence,EmpTraining,TrainingMaster,Company,Contact

# Register your models here.
class DepartmentadminModel(admin.ModelAdmin):
    list_display=('name','description')
    search_fields = ['name'] 


class EmployeeaminModel(admin.ModelAdmin):
    list_display=('firstname','lastname','gender','fathername','mothername','dob','email','department','working_time','salary')
    search_fields = ['firstname']

class EmpAttendenceadminModel(admin.ModelAdmin):
    list_display=('employee','department_name','date','present_status',)
    search_fields = ['department_name__name','date']
    list_editable=['present_status']
    list_filter=['date']

class TrainingMasteradminModel(admin.ModelAdmin):
    list_display=('trainingtype','trainingdescription','trainingduration')

class EmpTrainingadminModel(admin.ModelAdmin):
    list_display=('id','employee','department','trainingtype','startdate','enddate','purpose','remark')
    search_fields = ['trainingtype__trainingtype']

class CompanyadminModel(admin.ModelAdmin):
    list_display=('name','adress','contact','email','description')
    search_fields = ['name']

class ContactadminModel(admin.ModelAdmin):
    list_display=('name','email','phone','message')                        


admin.site.register(Department,DepartmentadminModel)
admin.site.register(Employee,EmployeeaminModel)
admin.site.register(TrainingMaster,TrainingMasteradminModel)
admin.site.register(Company,CompanyadminModel)
admin.site.register(EmpAttendence,EmpAttendenceadminModel)
admin.site.register(EmpTraining,EmpTrainingadminModel)
admin.site.register(Contact,ContactadminModel)

admin.site.site_header = "Employees Management System"

