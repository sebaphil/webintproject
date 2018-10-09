from datetime import datetime
from pprint import pprint
import os

def log_request(function_name, request_address):
    log = open(os.getcwd() + "/logs/requests.log", "a")
    log.write('\n' + str(datetime.now()) +" " + function_name + " - Request sent at: " + request_address)
    log.close()

def log_retrieve_from_question(question):
    log = open(os.getcwd() + "/logs/retrieve-from-question.log", "a")
    log.write('\n' + str(datetime.now()) +" " + "Error while retrieving information from a question." + " - Question body:")
    pprint(question, log)
    log.close()

def log_retrieve_users(user):
    log = open(os.getcwd() + "/logs/retrieve-users.log", "a")
    log.write('\n' + str(datetime.now()) +" " + "Error while retrieving information from users." + " - Response body:")
    pprint(user, log)
    log.close()

def log_retrieve_comments(comment):
    log = open(os.getcwd() + "/logs/retrieve-comments.log", "a")
    log.write('\n' + str(datetime.now()) +" " + "Error while retrieving information from comments." + " - Response body:")
    pprint(comment, log)
    log.close()

def log_retrieve_text_from_posts(text):
    log = open(os.getcwd() + "/logs/retrieve-text-from-posts.log", "a")
    log.write('\n' + str(datetime.now()) +" " + "Retrieved text:")
    log.write('\n')
    pprint(text, log)
    log.close()
