def test_data_1():
    return {
        "userId": 1,
        "policyNumber": "ABCD",
        "nameOfInsured": "Kasim Sharif",
        "type": "MOTOR",
        "amountInsured": 10000,
        "startDate": 1598548397000,
        "expirationDate": 1630084360000
    }


def test_data_2():
    return {
        "userId": 1,
        "policyNumber": "ABCD",
        "nameOfInsured": "Kasim Sharif",
        "type": "MOTOR",
        "amountInsured": 10000,
        "startDate": 1598548397000,
        "expirationDate": 1630084360000
    }


def invalid_insurance_type_data():
    return {
        "userId": 1,
        "policyNumber": "ABCD",
        "nameOfInsured": "Kasim Sharif",
        "type": "MOTR",
        "amountInsured": 10000,
        "startDate": 1598548397000,
        "expirationDate": 1630084360000
    }
