""" Project 1 + 2 CRUD Python Module
    Joseph Kim """

from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint 

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    """authentication to MongoDB"""
    def __init__(self, username= None, password= None):
        #Initialzes the MongoClient
        #Helps access the MongoDB databases and collections
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@127.0.0.1:33725/AAC' %(username, password),authSource="AAC")
           # print("authenticated")
        else:
            self.client = MongoClient('mongodb://localhost:33725')   
        self.database = self.client["AAC"]
        #print(self.database)


    """the Create implementation of CRUD"""
    #creates a document based off the data supplied to the animals collection
    #data must be in dictionary format and returns true if found, else false
    def create(self, data):
        if data is not None and type(data) is dict:
            insert_result = self.database.animals.insert(data) 
            if insert_result:
                return True
            else: 
                return False
        else:
            raise Exception("Nothing to save as data parameter is empty or wrong format")

    """the Read implementation of CRUD"""
    #reads a document based off the data supplied to the animals collection
    #function takes in a data argument that must be in dictionary form
    #returns the cursor to the document if successful, else returns error message

    def read(self, data: dict):
        if data is not None:
            results = self.database.animals.find(data, {"_id": False})
            return results
        else:
            raise Exception("Error, please check that search criteria is valid")
    
    #reads a document based off the data supplied to the animals collection
    #function takes in a data argument that must be in dictionary form
    #returns the document in JSON format if successful, else returns error message
    def read_show_result(self, data):
        if data is not None and type(data) is dict:
            results = self.database.animals.find_one(data)   
        else:
            results = "No data supplied to search or wrong format"
        return results
    
    #reads the document to display information based off filter information provided
    #function takes in animal type, breeds, preferred sex, and ages in weeks
    #returns a cursor to the document if successful, else returns error message
    def read_filtered(self, animalType, breed, sex, minAge, maxAge):
        if animalType and breed and sex and minAge and maxAge is not None:
            results = self.database.animals.find({"animal_type": animalType, "breed":{"$in":breed}, 
                                                      "sex_upon_outcome": sex,"age_upon_outcome_in_weeks":{"$gte":minAge,
                                                                                                           "$lte":maxAge}},
                                                 {"_id":False})
            
            return results
        else:
            raise Exception("Error, please check that search criteria is valid")
    
    """The Update implementation of CRUD"""
    #updates the first document found based off the data supplied to the animals collection
    #function takes in data arguments that must be in dictionary form
    #1st argument must be the key:value pair for the lookup of the document
    #2nd argument must be the key:value pair to be applied for the matched document
    #returns the document in JSON format if successful, else returns an error message
    
    def update(self, docData, updateData):
        if docData is not None and type(docData) is dict:
            if updateData is not None and type(updateData) is dict:
                cursor = self.database.animals.update_one(docData, {"$set": updateData}) #save cursor to doc if needed
                result = self.database.animals.find_one(docData) #use find_one to store the document data
                return result
            else:
                result = "No update data supplied or update data argument in wrong format."            
        else:
            result = "No document data supplied or document data argument in wrong format"
        return result
    
    
    """The delete implementation of CRUD"""
    #delete the first document found based off the data supplied to the animals collection
    #function takes in a data argument that must be in dictionary form
    #argument must be the key:value pair for the lookup of the document
    #returns the deleted document in JSON format if successful, else returns an error message
    
    def delete(self, data):
        if data is not None and type(data) is dict:
            result = self.database.animals.find_one_and_delete(data)
            return result
        else:
            result = "No delete data supplied or delete data argument in wrong format."
            return result
    #delete all documents based on the data supplied to the animals collection
    #function takes in a data argument that must be in dictionary form
    #argument must be the key:value pair for the lookup of the document
    
    def delete_many(self, data):
        if data is not None and type(data) is dict:
            result = self.database.animals.delete_many(data)
            return result.deleted_count
        else:
            result = "No delete data supplied or delete data argument in wrong format."
            return result
        

                

