from django.contrib import admin
from core.models import Projects,\
                        Systems,\
                        Staff,\
                        Company,\
                        ProjectStaffJoint,\
                        ProjectSystemJoint,\
                        ProjectImages,\
                        SystemImages


admin.site.register(Projects)
admin.site.register(Systems)
admin.site.register(Staff)
admin.site.register(Company)
admin.site.register(ProjectStaffJoint)
admin.site.register(ProjectSystemJoint)
admin.site.register(ProjectImages)
admin.site.register(SystemImages)
