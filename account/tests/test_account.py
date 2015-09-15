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
            "Created On": "2015-05-12"
        }
    
    def test_creation(self):
        account = Account(self.test_dict)
        self.assertEqual(account.account_name,self.test_dict["Account Name"])
        self.assertEqual(account.account_id,self.test_dict["Account ID"])
        self.assertEqual(account.first_name,self.test_dict["First Name"])
        self.assertEqual(account.created,date(2015,5,12))
