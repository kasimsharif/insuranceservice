from application.src.db.insurance.models import InsurancePolicy


def create_new_insurance_policy(user_id, policy_number, name_of_insured, type, start_date, expiration_date, amount_insured):
    return InsurancePolicy.objects.create(
        user_id = user_id,
        policy_number = policy_number,
        name_of_insured = name_of_insured,
        type = type,
        start_date = start_date,
        expiration_date = expiration_date,
        amount_insured = amount_insured
    )


def get_insurance_by_policy_number(policy_number):
    return InsurancePolicy.objects.get(policy_number=policy_number)

def filter_insurance_policy(filters):
    return InsurancePolicy.objects.filter(**filters)