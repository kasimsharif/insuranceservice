from application.src.common.exceptions.custom_error import CustomError
from application.src.dao.inmemory_insurance_policy import InMemoryInsurancePolicy, InsurancePolicy
from application.src.utils.date_time import timestamp_to_datetime, date_to_utc


def get_insurance_policy_json(insurance_obj):
    return {
        "userId": insurance_obj.user_id,
        "policyNumber": insurance_obj.policy_number,
        "nameOfInsured": insurance_obj.name_of_insured,
        "type": insurance_obj.type,
        "amountInsured": insurance_obj.amount_insured,
        "startDate": date_to_utc(insurance_obj.start_date),
        "expirationDate": date_to_utc(insurance_obj.expiration_date)
    }


def get_insurance_policy_json_simple(insurance_obj):
    return {
        "policyNumber": insurance_obj.policy_number,
        "type": insurance_obj.type,
        "expirationDate": date_to_utc(insurance_obj.expiration_date)
    }


def create_insurance_policy(data):
    user_id = data["userId"]
    policy_number = data["policyNumber"]
    name_of_insured = data["nameOfInsured"]
    type = data["type"]
    if type not in [InsurancePolicy.MOTOR, InsurancePolicy.TRAVEL, InsurancePolicy.HEALTH]:
        raise CustomError(400, "Invalid Insurance Type, correct values [MOTOR / HEALTH / TRAVEL]")
    amount_insured = data["amountInsured"]
    start_date = timestamp_to_datetime(data["startDate"])
    expiration_date = timestamp_to_datetime(data["expirationDate"])
    insurance_obj = InMemoryInsurancePolicy.create_new_insurance_policy(user_id, policy_number, name_of_insured, type, start_date,
                                                expiration_date, amount_insured)
    if not insurance_obj:
        raise CustomError(409, "Policy Number: " + policy_number + " ,already exists")
    response = get_insurance_policy_json(insurance_obj)
    return response


def get_insurance_policy(params, policy_number=None):
    format = params.get("format", "json")
    if policy_number:
        try:
            insurance_obj = InMemoryInsurancePolicy.get_insurance_by_policy_number(policy_number)
            if format == "json_simple":
                return get_insurance_policy_json_simple(insurance_obj)
            return get_insurance_policy_json(insurance_obj)
        except:
            raise CustomError(400, "Policy Number: " + policy_number + " , does not exist")

    filters = {}
    if params.get("userId"):
        filters["userId"] = params["userId"]
    insurance_policies = InMemoryInsurancePolicy.filter_insurance_policy(filters)
    if format == "json_simple":
        response = [get_insurance_policy_json_simple(insurance_policy) for insurance_policy in insurance_policies]
    else:
        response = [get_insurance_policy_json(insurance_policy) for insurance_policy in insurance_policies]
    return response
