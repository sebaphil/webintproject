def get_answers_list(answers_json):
    return answers_json['items']

def remove_duplicates_from_list(l):
    return list(set(l))