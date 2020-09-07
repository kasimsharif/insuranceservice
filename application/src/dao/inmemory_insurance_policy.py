class InsurancePolicy:
    MOTOR = "MOTOR"
    TRAVEL = "TRAVEL"
    HEALTH = "HEALTH"
    def __init__(self, user_id, policy_number, name_of_insured, type, start_date, expiration_date,
                 amount_insured):
        self.user_id = user_id
        self.policy_number = policy_number
        self.name_of_insured = name_of_insured
        self.type = type
        self.start_date = start_date
        self.expiration_date = expiration_date
        self.amount_insured = amount_insured


class InMemoryInsurancePolicy:
    insurance_policy = {}

    @staticmethod
    def create_new_insurance_policy(user_id, policy_number, name_of_insured, type, start_date, expiration_date,
                                    amount_insured):
        if InMemoryInsurancePolicy.insurance_policy.get(policy_number):
            return None
        insurance_policy_obj = InsurancePolicy(user_id, policy_number, name_of_insured, type, start_date, expiration_date, amount_insured)
        InMemoryInsurancePolicy.insurance_policy[policy_number] = insurance_policy_obj
        return InMemoryInsurancePolicy.insurance_policy[policy_number]

    @staticmethod
    def get_insurance_by_policy_number(policy_number):
        return InMemoryInsurancePolicy.insurance_policy.get(policy_number)

    @staticmethod
    def filter_insurance_policy(filters):
        filtered_policy = []
        if filters:
            for policy in InMemoryInsurancePolicy.insurance_policy.values():
                if int(filters["userId"]) == policy.user_id:
                    filtered_policy.append(policy)
            return filtered_policy
        else:
            return InMemoryInsurancePolicy.insurance_policy.values()

