from datetime import datetime
import os

def log_request(function_name, request_address):
    log = open(os.getcwd() + "/logs/requests.log", "a")
    log.write('\n' + str(datetime.now()) +" " + function_name + " - Request sent at: " + request_address)
    log.close()