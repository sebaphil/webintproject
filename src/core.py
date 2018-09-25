import pymongo
import json
from pymongo import MongoClient
from pprint import pprint
from url_retrieve_service import *
from services import *



client = MongoClient()
client.drop_database('stackoverflow')
stackoverflow_database = client.stackoverflow
questions_collection = stackoverflow_database.questions
users_collection = stackoverflow_database.users
answers_collection = stackoverflow_database.answers
comments_collection = stackoverflow_database.comments


questions_to_insert = retrieve_n_questions(10)
questions_collection.insert_many(questions_to_insert['items'])


questions_in_collection = questions_collection.find({})
#users = []
users_ids = []
answers = []
questions_ids = []
for question in questions_in_collection:
    user_id = question['owner']['user_id']
    is_answered = question['is_answered']
    question_id = question['question_id']

    if user_id not in users_ids:
        users_ids.append(user_id)
        #users.append(retrieve_single_user(user_id))

    if is_answered:
        question_id = question['question_id']
        answers += retrieve_answers_for_question(question_id)['items']
    
    questions_ids.append(question_id)

users = retrieve_multiple_users(users_ids)['items']
users_collection.insert_many(users)
answers_collection.insert_many(answers)


answers_in_collection = answers_collection.find({})
answers_ids = []
for answer in answers_in_collection:
    answer_id = answer['answer_id']
    answers_ids.append(answer_id)

posts_ids = questions_ids + answers_ids


comments = []
for post_id in posts_ids:
    comments += retrieve_comments_for_post(post_id)['items']

comments_collection.insert_many(comments)


users_ids_dict = {}
users_in_collection = users_collection.find({})
for user in users_in_collection:
    users_ids_dict[str(user['user_id'])] = 0

user_ids_have_questions_dict = users_ids_dict
questions_in_collection = questions_collection.find({})
for question in questions_in_collection:
    user_id = question['owner']['user_id']
    user_ids_have_questions_dict[str(user_id)] += 1

for user_id, number_of_documents in sorted(user_ids_have_questions_dict.iteritems(), key = lambda (k,v) : (v,k)):
    print('%s: %s', user_id, str(number_of_documents))

users_ids_have_answers_dict = users_ids_dict
answers_in_collection = answers_collection.find()
for answer in answers_in_collection:
    user_id = answer['owner']['user_id']
    users_ids_have_answers_dict[str(user_id)] += 1

for user_id, number_of_documents in sorted(users_ids_have_answers_dict.iteritems(), key = lambda (k,v) : (v,k)):
    print('%s: %s', user_id, str(number_of_documents))

users_ids_have_comments_dict = users_ids_dict
comments_in_collection = comments_collection.find()
for comment in comments_in_collection:
    user_id = comment['owner']['user_id']
    users_ids_have_comments_dict[str(user_id)] += 1

for user_id, number_of_documents in sorted(users_ids_have_comments_dict.iteritems(), key = lambda (k,v) : (v,k)):
    print('%s: %s', user_id, str(number_of_documents))





    





#question = url_retrieve_service.retrieve_single_question()

#questions_collection.insert_one(question)

#t = questions_collection.find_one()


#user_id = t['items'][0]['owner']['user_id']

#user_json = url_retrieve_service.retrieve_single_user(user_id)

#users_collection.insert_one(user_json)

#pprint(users_collection.find_one())

#question_id = t['items'][0]['question_id']

#answers_json = url_retrieve_service.retrieve_answers_for_question(question_id)

#answers_list = services.get_answers_list(answers_json)


#for answer in answers_list:
    #pprint(answer)
    #answers_collection.insert_one(answer)

#pprint(answers_json)
