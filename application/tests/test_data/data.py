def test_data_1():
    return {
        "userId": 1,
        "policyNumber": "6316-14738430-02-000",
        "nameOfInsured": "Kasim Sharif",
        "type": "MOTOR",
        "amountInsured": 10000,
        "startDate": 1598548397000,
        "expirationDate": 1630084360000
    }


def test_data_2():
    return {
        "userId": 1,
        "policyNumber": "6316-14738430-02-001",
        "nameOfInsured": "Kasim Sharif",
        "type": "MOTOR",
        "amountInsured": 10000,
        "startDate": 1598548397000,
        "expirationDate": 1630084360000
    }


def test_data_3():
    return {
        "userId": 2,
        "policyNumber": "6316-14738430-02-002",
        "nameOfInsured": "Hasan Sharif",
        "type": "TRAVEL",
        "amountInsured": 10000,
        "startDate": 1598548397000,
        "expirationDate": 1630084360000
    }


def test_data_4():
    return {
        "userId": 2,
        "policyNumber": "6316-14738430-02-003",
        "nameOfInsured": "Hasan Sharif",
        "type": "HEALTH",
        "amountInsured": 10000,
        "startDate": 1598548397000,
        "expirationDate": 1630084360000
    }


def invalid_insurance_type_data():
    return {
        "userId": 1,
        "policyNumber": "6316-14738430-02-004",
        "nameOfInsured": "Kasim Sharif",
        "type": "MOTR",
        "amountInsured": 10000,
        "startDate": 1598548397000,
        "expirationDate": 1630084360000
    }
