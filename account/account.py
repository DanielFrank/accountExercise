import urllib,json
from datetime import date


class Account:
    """Given a dict, define the element
    Assumes dict has fields Account ID,Account Name,First Name,Created On
    """
    def __init__(self, dict):
        self.account_name = dict["Account Name"]
        self.account_id = dict["Account ID"]
        self.first_name = dict["First Name"]
        self.created = convertToDate(dict["Created On"])
        """These next two we'll get from the API eventually so just set to None"""
        self.status = None
        self.status_date = None
        
    """
    Converts a MySQL formatted date into a date object
    @param String in format of YYYY-MM-DD (assumes in correct format)
    @return datetime.date object
    """
    def convertToDate(self, date_str):
        my date_split = date_str.split("-")
        return date(int(year), int(month), int(day))
