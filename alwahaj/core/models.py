from django.db import models

isLeaderChoices=(("Yes","Yes"),
                ("No","No"))

statusChoices=(("Completed","Completed"),
                ("In-Progress","In-Progress"))

class Company(models.Model):
    class Meta:
        verbose_name_plural="Companies"

    name = models.CharField(max_length=45,unique=True)
    url = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Staff(models.Model):
    class Meta:
        verbose_name_plural="Staff"

    name = models.CharField(max_length=45,unique=True)
    position = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    education = models.CharField(max_length=100)
    payroll = models.DecimalField(max_digits=19, decimal_places=3)
    image= models.ImageField(upload_to='media/staff', blank=True, null=True)

    def __str__(self):
        return self.name

class Systems(models.Model):
    class Meta:
        verbose_name_plural="Systems"

    name = models.CharField(max_length=45,unique=True)
    description = models.CharField(max_length=500)
    cost = models.DecimalField(max_digits=19, decimal_places=3)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    image= models.ImageField(upload_to='media/systems', blank=True, null=True)

    def __str__(self):
        return self.name

class SystemImages(models.Model):
    system=models.ForeignKey(Systems,on_delete=models.CASCADE)
    image= models.ImageField(upload_to="media/systems", blank=True, null=True)

    def __str__(self):
        return self.system.name + "Image"


class Projects(models.Model):
    class Meta:
        verbose_name_plural="Projects"
    name = models.CharField(max_length=45,unique=True)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    beneficiary = models.CharField(max_length=500)
    status = models.CharField(max_length=45,choices=statusChoices)
    budget = models.DecimalField(max_digits=19, decimal_places=3)
    image= models.ImageField(upload_to='media/projects', blank=True, null=True)
    PojectSystemJoint = models.ManyToManyField(Systems, through='ProjectSystemJoint', related_name='projectSystems')
    ProjectStaffJoint = models.ManyToManyField(Staff, through='ProjectStaffJoint', related_name='projectStaff')

    def __str__(self):
        return self.name

class ProjectImages(models.Model):
    project=models.ForeignKey(Projects,on_delete=models.CASCADE)
    image= models.ImageField(upload_to="media/projects", blank=True, null=True)

    def __str__(self):
        return self.project.name + "Image"

class ProjectSystemJoint(models.Model):
    class Meta:
        verbose_name_plural="PojectSystemJoint"
    Projects = models.ForeignKey(Projects,on_delete=models.CASCADE)
    Systems = models.ForeignKey(Systems,on_delete=models.CASCADE)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

class ProjectStaffJoint(models.Model):
    class Meta:
        verbose_name_plural="ProjectStaffJoint"
    Projects = models.ForeignKey(Projects,on_delete=models.CASCADE)
    Staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    isLeader = models.CharField(max_length=45,choices=isLeaderChoices)
