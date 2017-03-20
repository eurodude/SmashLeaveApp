"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from time import strptime

from LeaveApp.settings import LEAVE_TYPES_CHOICES
from LeaveApp.settings import EMPLOYEE_DEFAULT_DAY


class WorkDay(models.Model):
    work_start = models.TimeField(null=True,blank=True,default=strptime(EMPLOYEE_DEFAULT_DAY[0],"%H:%M"))
    lunch_start = models.TimeField(null=True,blank=True,default=strptime(EMPLOYEE_DEFAULT_DAY[1],"%H:%M"))
    lunch_length = models.IntegerField(null=True,blank=True,default=EMPLOYEE_DEFAULT_DAY[2])
    work_end = models.TimeField(null=True,blank=True,default=strptime(EMPLOYEE_DEFAULT_DAY[3],"%H:%M"))

class Schedule(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    s_monday = models.ForeignKey(WorkDay,related_name='schedule_monday',null=True,blank=True)
    s_tuesday = models.ForeignKey(WorkDay,related_name='schedule_tuesday',null=True,blank=True)
    s_wednesday = models.ForeignKey(WorkDay,related_name='schedule_wednesday',null=True,blank=True)
    s_thursday = models.ForeignKey(WorkDay,related_name='schedule_thursday',null=True,blank=True)
    s_friday = models.ForeignKey(WorkDay,related_name='schedule_friday',null=True,blank=True)
    s_saturday = models.ForeignKey(WorkDay,related_name='schedule_saturday',null=True,blank=True)
    s_sunday = models.ForeignKey(WorkDay,related_name='schedule_sunday',null=True,blank=True)
    class Meta:
        permissions = (
            ("schedule_can_edit", "Can edit a schedule"),
            ("schedule_can_create", "Can create a schedule"),
        )

class TicketResto(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_count = models.IntegerField(default=18)
    class Meta:
        permissions = (
            ("tr_can_edit","Can edit the number of ticket resto"),
        )
        
class PublicHoliday(models.Model):
    public_holiday_year = models.IntegerField()
    public_holiday_date = models.DateField()
    class Meta:
        permissions = (
            ("ph_can_edit","Can edit the official public holidays"),
            ("ph_can_create","Can create an official public holiday"),
        )
   
class LeavePeriod(models.Model):
    employee = models.ForeignKey(User,related_name='employee', on_delete=models.CASCADE)
    leave_appy_date = models.DateField()
    leave_approved = models.BooleanField(default=False)
    leave_approved_date = models.DateField()
    leave_approved_by = models.ForeignKey(User,related_name='coord_hr_ceo')

    class Meta:
        permissions = (
            ("leave_rq_can_validate", "Can validate a Leave Request"),
            ("leave_rq_can_edit_after_valid", "Can edit after validation"),
        )
        
class LeaveDay(models.Model):
    leave_period_id = models.ForeignKey(LeavePeriod, on_delete=models.CASCADE)
    leave_type = LEAVE_TYPES_CHOICES
    leave_day = models.DateField()
    leave_time = models.ForeignKey(WorkDay)