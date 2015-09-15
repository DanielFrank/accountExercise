import json
from urllib import request
from datetime import date
import sys


class Account:
    """Given a dict, define the element
    Assumes dict has keys Account ID,Account Name,First Name,Created On
    """
    def __init__(self, dict):
        self.account_name = dict["Account Name"]
        self.account_id = dict["Account ID"]
        self.first_name = dict["First Name"]
        self.created = self.convertToDate(dict["Created On"])
        """These next two we'll get from the API eventually so just set to None"""
        self.status = None
        self.status_date = None

    """Return a dictionary with the values of self
    Set keys to Account ID,Account Name,First Name,Created On,Status,Status Set On
    """
    def makeDictionary(self):
        return {
            "Account ID": self.account_id,
            "Account Name": self.account_name,
            "First Name": self.first_name,
            "Created On": self.formatDate(self.created),
            "Status": self.status,
            "Status Set On": self.formatDate(self.status_date)
        }


    """Should probably create 'myDate' object which wraps around Date and does this stuff"""
    
    """
    Converts a MySQL formatted date into a date object
    @param String in format of YYYY-MM-DD (assumes in correct format)
    @return datetime.date object
    """
    def convertToDate(self, date_str):
        date_split = date_str.split("-")
        return date(int(date_split[0]), int(date_split[1]), int(date_split[2]))

    """
    Converts a MySQL formatted date into a date object
    @param Date object which might be None
    @return datetime.date object
    """
    def formatDate(self, date_param):
        if (date_param is None):
            return None
        return date_param.strftime("%Y-%m-%d")


    """
    Calls API and sets the status/status-date for self.
    If problem with API-call or ID not recognized by API, sets to None
    May eventually want to seperate API calls from Account
    """
    def getStatus(self):
        url = "https://interview.wpengine.io/v1/accounts/" + str(self.account_id)
        try:
            result = request.urlopen(url)
            json_str=result.read().decode("utf-8")
            json_obj=json.loads(json_str)
            if ("detail" in json_obj and json_obj["detail"] == "Not found"):
                self.status = None
                self.status_date = None                
                return
            self.status = json_obj["status"]
            self.status_date = self.convertToDate(json_obj["created_on"])
        except:
            self.status = None
            self.status_date = None
            return
        
            
