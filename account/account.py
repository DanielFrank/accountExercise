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
        self.created = self.convertToDate(dict["Created On"])
        """These next two we'll get from the API eventually so just set to None"""
        self.status = None
        self.status_date = None
        
    """
    Converts a MySQL formatted date into a date object
    @param String in format of YYYY-MM-DD (assumes in correct format)
    @return datetime.date object
    """
    def convertToDate(self, date_str):
        date_split = date_str.split("-")
        return date(int(date_split[0]), int(date_split[1]), int(date_split[2]))


    """
    Calls API and gets the status/status-date.
    If problem with API-call or ID not recognized by API, sets to None
    """
    def getStatus(self):
        url = "https://interview.wpengine.io/v1/accounts/" + str(self.account_id)
        """
        try:
            result = urllib.request.urlopen(url)
            json_str=result.read().decode("utf-8")
            
        """
        return
