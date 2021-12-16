from django.utils import timezone
from django.db import models


class Enterprise(models.Model):
    registration_number = models.BigIntegerField(null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True)
    sector = models.ForeignKey(to='Sector', related_name='enterprise_sector', on_delete=models.CASCADE,default='Multiple')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number_of_employees = models.IntegerField(default=1)

    class Meta:
        db_table = 'enterprises'


class Sector(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sector'


class User(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False, default=None)
    mobile = models.BigIntegerField(unique=True, blank=False, null=False)
    city = models.ForeignKey(to='City', related_name='user_city',
                             blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    last_logged_in_time = models.DateTimeField(default=timezone.now)
    privilege = models.ForeignKey(to='Privilege', related_name='user_privilege', on_delete=models.CASCADE, default='User')
    enterprise = models.ForeignKey(to='Enterprise', related_name='user_enterprise', on_delete=models.CASCADE, default=None)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'users'


class City(models.Model):
    name = models.CharField(max_length=50, default=None)
    state = models.ForeignKey(to='State', related_name='city_state', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cities'


class State(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'state'


class Privilege(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'privileges'


class MobileOtpLogs(models.Model):
    mobile = models.BigIntegerField()
    otp = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'mobile_otp_logs'


class EmailOtpLogs(models.Model):
    email = models.EmailField()
    otp = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'email_otp_logs'