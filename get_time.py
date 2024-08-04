import ntplib
from datetime import datetime
import requests


def get_time_from_ntp():
    # Set the ntp server from which you want to take a time
    ntp_server = "tempus1.gum.gov.pl"

    ntp_client = ntplib.NTPClient()
    ntp_response = ntp_client.request(ntp_server, version=3)
    ntp_timestamp = ntp_response.tx_time

    datetime_object = datetime.fromtimestamp(ntp_timestamp)
    current_time = datetime_object.strftime('%H:%M:%S')
    current_date = datetime_object.strftime("%d.%m.%Y")
    sync_time = datetime_object.strftime('%H:%M')

    return current_time, current_date, sync_time

def get_time_from_datetime():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M:%S")
    current_date = current_datetime.strftime("%d.%m.%Y")
    return current_time, current_date

def check_network_connection():
    url = "https://www.google.com"
    timeout = 1
    try:
        request = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False