import gzip
import json
import urllib
import logger
import requests
import time

def request_to_api(url):
    time.sleep(1)
    filename, _ = urllib.urlretrieve(url)
    return json.loads(gzip.GzipFile(filename).read())

def retrieve_n_questions():
    result = []
    for i in range(100):
        url = 'https://api.stackexchange.com/2.2/questions?tagged=postgres&filter=withbody&page=' + str(i+1) + '&pagesize=100&order=asc&sort=creation&site=stackoverflow'
        result.append(request_to_api(url))
        logger.log_request(retrieve_n_questions.__name__, url)
    return result

def retrieve_multiple_users(users_ids_list):
    users_string = ';'.join(users_ids_list)
    url = 'https://api.stackexchange.com/2.2/users/' + users_string + '?page=1&pagesize=100&order=desc&sort=reputation&site=stackoverflow'
    result = request_to_api(url)
    logger.log_request(retrieve_multiple_users.__name__, url)
    return result

def retrieve_answers_for_questions(questions_ids):
    questions_string = ';'.join(questions_ids)
    url = 'https://api.stackexchange.com/2.2/questions/' + questions_string + '/answers?order=desc&sort=activity&site=stackoverflow'
    result = request_to_api(url)
    logger.log_request(retrieve_answers_for_questions.__name__, url)
    return result

def retrieve_comments_for_post(post_id):
    url = 'https://api.stackexchange.com/2.2/posts/' + str(post_id) + '/comments?order=desc&sort=creation&site=stackoverflow'
    result = request_to_api(url)
    logger.log_request(retrieve_comments_for_post.__name__, url)
    return result
