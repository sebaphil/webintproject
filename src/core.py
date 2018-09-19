import pymongo
import url_retrieve_service

from pymongo import MongoClient

client = MongoClient()

stackoverflow_database = client.stackoverflow

questions_collection = stackoverflow_database.questions

question = url_retrieve_service.retrieve_single_question()

questions_collection.insert_one(question)