import pymongo
import json
import services
from pymongo import MongoClient
from pprint import pprint
from url_retrieve_service import *



client = MongoClient()
client.drop_database('stackoverflow')
stackoverflow_database = client.stackoverflow
questions_collection = stackoverflow_database.questions
users_collection = stackoverflow_database.users
answers_collection = stackoverflow_database.answers

questions_to_insert = retrieve_n_questions(10)
questions_collection.insert_many(questions_to_insert['items'])







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
