import gzip
import json
import urllib
import logger
import requests
import time
from bs4 import BeautifulSoup

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

def retrieve_comments_for_posts(posts_ids):
    posts_string = ';'.join(posts_ids)
    url = 'https://api.stackexchange.com/2.2/posts/' + posts_string + '/comments?order=desc&sort=creation&site=stackoverflow'
    result = request_to_api(url)
    logger.log_request(retrieve_comments_for_posts.__name__, url)
    return result

def retrieve_question_answers_and_comments_text(question_id):
    time.sleep(2)
    question_url = 'https://www.stackoverflow.com/questions/' + str(question_id) + '/'
    html_code = urllib.urlopen(question_url).read()
    logger.log_retrieve_text_from_posts(html_code)
    html_code_soup = BeautifulSoup(html_code, 'html.parser')
    code_tags = html_code_soup.find_all('code')

    for code_tag in code_tags:
        code_tag.extract()

    question_and_answers_html = html_code_soup.find_all('div', class_ = 'post-text')
    comments_html = html_code_soup.find_all('div', class_ = 'comment-body')
    question_answers_and_comments_text = []

    for element in question_and_answers_html:
        question_answers_and_comments_text.append(element.get_text())

    for element in comments_html:
        question_answers_and_comments_text.append(element.get_text())
    
    return question_answers_and_comments_text
