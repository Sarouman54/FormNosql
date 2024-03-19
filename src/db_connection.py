"""
Sarah Barrabé
db_connection.py
src

"""

import pymongo

url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)

db = client['survey_db']

#####  Collection models #####
collection_survey = db['surveys']

collection_response = db['responses']
collection_question = db['questions']

collection_user = db['users']
##############################
#####      List Data     #####
questions = [
    {
        "id_question": "Q1",
        "entitled": "Quel est le nom du premier magicien blanc ?" ,
        "type": "ouverte",
        "response": "Saruman"
    },
    {
        "id_question": "Q2",
        "entitled": "Quel est le nom de famille de Sam ?" ,
        "type": "choix multiples",
        "choice": ["Sacquet", "Gamegie", "Touque", "Brandibouc"],
        "response": "Gamegie"
    },
    {
        "id_question": "Q3",
        "entitled": "Le frère de Faramir est-il mort ?" ,
        "type": "fermée",
        "response": True
    }
]

users = [
    {
        "id_user": "U1",
        "pseudo": "Tauriel"
    },
    {
        "id_user": "U2",
        "pseudo": "Jackson"
    }
]

surveys = [
    {
        "id_survey": "S1",
        "name": "Sondage Connaissances Seigneur des Anneaux",
        "creator_id": {"id_user":"U1", "pseudo":"Tauriel"},
        "questions_id": questions
    }
]

responses = [
    {
        "user_id": {"id_user": "U2", "pseudo": "Jackson"},
        "sondage_id": {"id_survey": "S1", "name": "Sondage Connaissances Seigneur des Anneaux", "creator": {"id_user":"U1", "pseudo":"Tauriel"}, "questions": questions},
        "responses": [
            {
                "question_id": {
                    "id_question": "Q1",
                    "entitled": "Quel est le nom du premier magicien blanc ?" ,
                    "type": "ouverte",
                    "response": "Saruman"
                },
                "response": "Gandalf"
            },
            {
                "question_id": {
                    "id_question": "Q2",
                    "entitled": "Quel est le nom de famille de Sam ?" ,
                    "type": "choix multiples",
                    "choice": ["Sacquet", "Gamegie", "Touque", "Brandibouc"],
                    "response": "Gamegie"
                },
                "response": "Gamegie"
            },
            {
                "question_id": {
                    "id_question": "Q3",
                    "entitled": "Le frère de Faramir est-il mort ?" ,
                    "type": "fermée",
                    "response": True
                },
                "response": True
            }
        ]
    }
]
##############################
#####     Insert Data    #####
collection_user.insert_many(users)
collection_survey.insert_many(surveys)
collection_response.insert_many(responses)
collection_question.insert_many(questions)
##############################