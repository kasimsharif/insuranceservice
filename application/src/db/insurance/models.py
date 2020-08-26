from django.db import models

class InsurancePolicies(models.Model):
    MOTOR = "MOTOR"
    HEALTH = "HEALTH"
    TRAVEL = "TRAVEL"
    insurance_type = (
        ("Motor", MOTOR),
        ("Health", HEALTH),
        ("Travel", TRAVEL)
    )
    user_id = models.IntegerField()
    policy_number = models.CharField(max_length=128, primary_key=True)
    name_of_insured = models.CharField(max_length=128)
    type = models.CharField(max_length=16, choices=insurance_type)
    start_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    amount_assured = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True, null=True)
