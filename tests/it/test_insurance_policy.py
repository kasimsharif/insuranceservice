import json
from django.test import TestCase

from application.src.launcher import app


class TestInsurancePolicy(TestCase):
    """Choice List Test Class"""

    def setUp(self):
        self.client = app.test_client
        self.test_data_1 = {
            "userId": 1,
            "policyNumber": "ABCD",
            "nameOfInsured": "Kasim Sharif",
            "type": "MOTOR",
            "amountInsured": 10000,
            "startDate": 1598548397000,
            "expirationDate": 1630084360000
        }
        self.test_data_2 = {
            "userId": 1,
            "policyNumber": "ABCD",
            "nameOfInsured": "Kasim Sharif",
            "type": "MOTOR",
            "amountInsured": 10000,
            "startDate": 1598548397000,
            "expirationDate": 1630084360000
        }

    def test_insurance_policy_creation(self):
        """Test Insurance Policy creation"""
        res = self.client().post('/insurance/policy/', data=json.dumps(self.test_data_1))
        response_data = json.loads(res.data)["responseData"]
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.test_data_1['userId'], response_data['userId'])
        self.assertEqual(self.test_data_1['policyNumber'], response_data['policyNumber'])

    def test_insurance_policy_duplicate_policy_number(self):
        """Test Insurance Policy creation"""
        res = self.client().post('/insurance/policy/', data=json.dumps(self.test_data_2))
        self.assertEqual(res.status_code, 200)
        res = self.client().post('/insurance/policy/', data=json.dumps(self.test_data_2))
        message = json.loads(res.data)["message"]
        self.assertEqual(res.status_code, 409)
        self.assertEqual(message, "Policy Number: ABCD ,already exists")

    def test_get_insurance_policy_by_user_id(self):
        """Test Get Insurance policy by User Id """
        res = self.client().post('/insurance/policy/', data=json.dumps(self.test_data_1))
        self.assertEqual(res.status_code, 200)
        res = self.client().get('/insurance/policy/?userId=1')
        self.assertEqual(res.status_code, 200)
        response_data = json.loads(res.data)["responseData"]
        self.assertEqual(self.test_data_1['userId'], response_data[0]["userId"])
        self.assertEqual(self.test_data_1['policyNumber'], response_data[0]["policyNumber"])

    def test_get_insurance_policy_by_policy_number(self):
        """Test Get Insurance policy by policy number"""
        res = self.client().post('/insurance/policy/', data=json.dumps(self.test_data_1))
        self.assertEqual(res.status_code, 200)
        res = self.client().get('/insurance/policy/ABCD/')
        self.assertEqual(res.status_code, 200)
        response_data = json.loads(res.data)["responseData"]
        self.assertEqual(self.test_data_1['userId'], response_data["userId"])
        self.assertEqual(self.test_data_1['policyNumber'], response_data["policyNumber"])

    def test_get_insurance_policy_csv_format(self):
        """Test Get Insurance policy csv format"""
        res = self.client().post('/insurance/policy/', data=json.dumps(self.test_data_1))
        self.assertEqual(res.status_code, 200)
        res = self.client().get('/insurance/policy/?userId=1&format=csv')
        self.assertEqual(res.status_code, 200)
        content_type = res.headers['Content-Type']
        self.assertEqual(content_type, "Content-Type: text/csv; charset=utf-8")

if __name__ == '__main__':
    unittest.main()
