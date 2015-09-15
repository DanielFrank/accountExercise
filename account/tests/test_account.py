import unittest
from unittest import mock
from datetime import date

from ..account import Account

class AccountTest(unittest.TestCase):

    def setUp(self):
        self.test_dict = {
            "Account ID": 12345,
            "Account Name": "Test Account",
            "First Name": "Daniel",
            "Created On": "2010-05-17"
        }
    
    def test_creation(self):
        account = Account(self.test_dict)
        self.assertEqual(account.account_name,self.test_dict["Account Name"])
        self.assertEqual(account.account_id,self.test_dict["Account ID"])
        self.assertEqual(account.first_name,self.test_dict["First Name"])
        self.assertEqual(account.created,date(2010,5,17))

    def test_get_status_gets_correct_info(self):
        account = Account(self.test_dict)
        account.getStatus()
        
        self.assertEqual(account.status,"good")
        self.assertEqual(account.status_date,date(2011,1,12))

    def test_get_status_when_account_id_not_valid(self):
        account = Account(self.test_dict)
        account.account_id = 1234
        account.getStatus()
        self.assertIsNone(account.status)
        self.assertIsNone(account.status_date)

    def test_get_status_when_status_was_set_and_account_id_not_valid(self):
        account = Account(self.test_dict)
        account.account_id = 1234
        account.status = "testing"
        account.status_date = date(2015,10,12)
        account.getStatus()
        self.assertIsNone(account.status)
        self.assertIsNone(account.status_date)
