from bs4 import BeautifulSoup


def get_answers_list(answers_json):
    return answers_json['items']

def remove_duplicates_from_list(l):
    return list(set(l))

def remove_all_html_tags_from_text(body):
    soup = BeautifulSoup(body)
    text = soup.get_text()
    return text

def split_string_into_list_of_words(string_to_be_parsed):
    return string_to_be_parsed.split()