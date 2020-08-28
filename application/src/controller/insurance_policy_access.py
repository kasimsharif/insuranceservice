from application.src.common.exceptions.custom_error import CustomError
from application.src.dao.insurance_policy import create_new_insurance_policy, get_insurance_by_policy_number, \
    filter_insurance_policy
from application.src.db.insurance.models import InsurancePolicy
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

    try:
        insurance_obj = create_new_insurance_policy(user_id, policy_number, name_of_insured, type, start_date,
                                                    expiration_date, amount_insured)
    except:
        raise CustomError(409, "Policy Number: " + policy_number + " ,already exists")
    response = get_insurance_policy_json(insurance_obj)
    return response


def get_insurance_policy(params, policy_number=None):
    format = params.get("format", "json")
    if policy_number:
        try:
            insurance_obj = get_insurance_by_policy_number(policy_number)
            if format == "json_simple":
                return get_insurance_policy_json_simple(insurance_obj)
            return get_insurance_policy_json(insurance_obj)
        except:
            raise CustomError(400, "Policy Number: " + policy_number + " , does not exist")
    filter = {}
    if params.get("userId"):
        filter["user_id"] = params["userId"]
    insurance_policies = filter_insurance_policy(filter)
    if format == "json_simple":
        response = [get_insurance_policy_json_simple(insurance_policy) for insurance_policy in insurance_policies]
    else:
        response = [get_insurance_policy_json(insurance_policy) for insurance_policy in insurance_policies]
    return response
