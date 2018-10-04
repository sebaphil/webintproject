import pymongo
import json
from pymongo import MongoClient
from pprint import pprint
from url_retrieve_service import *
from services import *
from logger import *
from nltk import *



client = MongoClient()
# client.drop_database('stackoverflow')
stackoverflow_database = client.stackoverflow
questions_collection = stackoverflow_database.questions
users_collection = stackoverflow_database.users
answers_collection = stackoverflow_database.answers
comments_collection = stackoverflow_database.comments

# PART A
# list_of_questions_to_insert = retrieve_n_questions()
# for list_item in list_of_questions_to_insert:
#     questions_collection.insert_many(list_item['items'])


questions_in_collection = questions_collection.find({})
users_ids = []
questions_ids = []
# answers = []
# answered_questions_ids = []
for question in questions_in_collection:
    try:
        user_id = question['owner']['user_id']
#         is_answered = question['is_answered']
        question_id = question['question_id']
        questions_ids.append(str(question_id))

        if user_id not in users_ids:
            users_ids.append(str(user_id))

#         if is_answered:
#             answered_questions_ids.append(question_id)
    except KeyError:
        log_retrieve_from_question(question)

# number_of_retrieved_answers = 0
# question_ids_to_use_for_request = []
# answers_to_be_inserted = []    
# for answered_question_id in answered_questions_ids:
#     if number_of_retrieved_answers < 100:
#         question_ids_to_use_for_request.append(str(answered_question_id))
#         number_of_retrieved_answers += 1
#     else:
#         answers_to_be_inserted += retrieve_answers_for_questions(question_ids_to_use_for_request)['items']
#         question_ids_to_use_for_request = []
#         question_ids_to_use_for_request.append(str(answered_question_id))
#         number_of_retrieved_answers = 1

# answers_collection.insert_many(answers_to_be_inserted)


answers_in_collection = answers_collection.find({})
answers_ids = []
for answer in answers_in_collection:
    if answer['owner']['user_type'] != 'does_not_exist':
        user_id = answer['owner']['user_id']
        if user_id not in users_ids:
            users_ids.append(str(user_id))

    answer_id = answer['answer_id']
    answers_ids.append(str(answer_id))


number_of_retrieved_users = 0
users_ids_to_use_for_request = []
users_to_be_inserted = []
for user_id in users_ids:
    if number_of_retrieved_users < 100:
        users_ids_to_use_for_request.append(user_id)
        number_of_retrieved_users += 1
    else:
        users_request_response = {}
        try:
            users_request_response = retrieve_multiple_users(users_ids_to_use_for_request)
            users_to_be_inserted += users_request_response['items']
            users_ids_to_use_for_request = []
            users_ids_to_use_for_request.append(user_id)
            number_of_retrieved_users = 1
        except KeyError:
            log_retrieve_users(users_request_response)

users_collection.insert_many(users_to_be_inserted)

posts_ids = questions_ids + answers_ids


number_of_posts_to_retrieve_comments_for = 0
posts_ids_to_use_for_request = []
comments_to_be_inserted = []
for post_id in posts_ids:
    if number_of_posts_to_retrieve_comments_for < 100:
        posts_ids_to_use_for_request.append(post_id)
        number_of_posts_to_retrieve_comments_for += 1
    else:
        comments_request_response = {}
        try:
            comments_request_response = retrieve_comments_for_posts(posts_ids_to_use_for_request)
            comments_to_be_inserted += comments_request_response['items']
            posts_ids_to_use_for_request = []
            posts_ids_to_use_for_request.append(post_id)
            number_of_posts_to_retrieve_comments_for = 1
        except KeyError:
            log_retrieve_comments(comments_request_response)
            
comments_collection.insert_many(comments_to_be_inserted)

# # PART B

# user_words_dict = {}
# users_ids_dict = {}
# users_in_collection = users_collection.find({})
# for user in users_in_collection:
#     user_words_dict[str(user['user_id'])] = []
#     users_ids_dict[str(user['user_id'])] = 0

# user_ids_have_questions_dict = users_ids_dict
# questions_in_collection = questions_collection.find({})
# for question in questions_in_collection:
#     user_words_dict[str(question['owner']['user_id'])] += split_string_into_list_of_words(remove_all_html_tags_from_text(question['body']))
#     user_id = question['owner']['user_id']
#     user_ids_have_questions_dict[str(user_id)] += 1
# print('top questioners')
# for user_id, number_of_documents in sorted(user_ids_have_questions_dict.iteritems(), key = lambda (k,v) : (v,k)):
#     print('%s: %s', user_id, str(number_of_documents))

# users_ids_have_answers_dict = users_ids_dict
# answers_in_collection = answers_collection.find()
# for answer in answers_in_collection:
#     user_words_dict[str(answer['owner']['user_id'])] += split_string_into_list_of_words(remove_all_html_tags_from_text(answer['body']))
#     user_id = answer['owner']['user_id']
#     users_ids_have_answers_dict[str(user_id)] += 1
# print('top answerers')
# for user_id, number_of_documents in sorted(users_ids_have_answers_dict.iteritems(), key = lambda (k,v) : (v,k)):
#     print('%s: %s', user_id, str(number_of_documents))

# users_ids_have_comments_dict = users_ids_dict
# comments_in_collection = comments_collection.find()
# for comment in comments_in_collection:
#     user_id = comment['owner']['user_id']
#     users_ids_have_comments_dict[str(user_id)] += 1
# print('top commenters')
# for user_id, number_of_documents in sorted(users_ids_have_comments_dict.iteritems(), key = lambda (k,v) : (v,k)):
#     print('%s: %s', user_id, str(number_of_documents))





    





