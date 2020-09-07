import json
import unittest
from unittest.case import TestCase

from application.src.launcher import app
from application.tests.test_data.data import test_data_1, test_data_2, invalid_insurance_type_data, test_data_3, \
    test_data_4, invalid_start_date, invalid_expiration_date


class TestInsurancePolicy(TestCase):
    """Choice List Test Class"""

    def setUp(self):
        self.client = app.test_client
        self.test_data_1 = test_data_1()
        self.test_data_2 = test_data_2()
        self.test_data_3 = test_data_3()
        self.test_data_4 = test_data_4()
        self.invalid_start_date = invalid_start_date()
        self.invalid_expiration_date = invalid_expiration_date()
        self.invalid_data = invalid_insurance_type_data()

    def test_1_insurance_policy_creation(self):
        """Test Insurance Policy creation"""
        res = self.client().post('/insurance/policy/', data=json.dumps(self.test_data_1))
        response_data = json.loads(res.data)["responseData"]
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.test_data_1['userId'], response_data['userId'])
        self.assertEqual(self.test_data_1['policyNumber'], response_data['policyNumber'])

    def test_2_insurance_policy_duplicate_policy_number(self):
        """Test Insurance Policy creation"""
        res = self.client().post('/insurance/policy/', data=json.dumps(self.test_data_2))
        self.assertEqual(res.status_code, 200)
        res = self.client().post('/insurance/policy/', data=json.dumps(self.test_data_2))
        message = json.loads(res.data)["message"]
        self.assertEqual(res.status_code, 409)
        self.assertEqual(message, "Policy Number: 6316-14738430-02-001 ,already exists")

    def test_3_insurance_policy_invalid_insurance_type(self):
        """Test Insurance Policy creation"""
        res = self.client().post('/insurance/policy/', data=json.dumps(self.invalid_data))
        self.assertEqual(res.status_code, 400)
        message = json.loads(res.data)["message"]
        self.assertEqual(message, "Invalid Insurance Type, correct values [MOTOR / HEALTH / TRAVEL]")

    def test_4_get_insurance_policy_by_user_id(self):
        """Test Get Insurance policy by User Id """
        res = self.client().post('/insurance/policy/', data=json.dumps(self.test_data_3))
        self.assertEqual(res.status_code, 200)
        res = self.client().get('/insurance/policy/?userId=2')
        self.assertEqual(res.status_code, 200)
        response_data = json.loads(res.data)["responseData"]
        self.assertEqual(self.test_data_3['userId'], response_data[len(response_data) - 1]["userId"])
        self.assertEqual(self.test_data_3['policyNumber'], response_data[len(response_data) - 1]["policyNumber"])

    def test_5_get_insurance_policy_by_policy_number(self):
        """Test Get Insurance policy by policy number"""
        self.client().post('/insurance/policy/', data=json.dumps(self.test_data_4))
        res = self.client().get('/insurance/policy/6316-14738430-02-003/')
        self.assertEqual(res.status_code, 200)
        response_data = json.loads(res.data)["responseData"]
        self.assertEqual(self.test_data_4['userId'], response_data["userId"])
        self.assertEqual(self.test_data_4['policyNumber'], response_data["policyNumber"])

    def test_6_get_insurance_policy_csv_format(self):
        """Test Get Insurance policy csv format"""
        self.client().post('/insurance/policy/', data=json.dumps(self.test_data_1))
        res = self.client().get('/insurance/policy/?userId=1&format=csv')
        self.assertEqual(res.status_code, 200)
        content_type = res.headers['Content-Type']
        self.assertEqual(content_type, "Content-Type: text/csv; charset=utf-8")

    def test_7_invalid_start_date(self):
        """Test Invalid start date less then today's date"""
        res = self.client().post('/insurance/policy/', data=json.dumps(self.invalid_start_date))
        self.assertEqual(res.status_code, 400)
        message = json.loads(res.data)["message"]
        self.assertEqual(message, "Invalid Start date, it must be equal/greater then today's date")

    def test_8_invalid_expiration_date(self):
        """Test Expiration date less than start date"""
        res = self.client().post('/insurance/policy/', data=json.dumps(self.invalid_expiration_date))
        self.assertEqual(res.status_code, 400)
        message = json.loads(res.data)["message"]
        self.assertEqual(message, "Expiration date must be greater then start date")


if __name__ == '__main__':
    unittest.main()
