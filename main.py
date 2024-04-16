import pymongo

if __name__ == "__main__":

# To connect mongo you need to run this command:

    client = pymongo.MongoClient("mongodb+srv://ratulpal26:PikaChu%401997@cluster0.xfneeux.mongodb.net/")

    # To check the avilable databses:

    '''
    print(client.list_database_names())
    '''

# To create a database you need to run this command:

    database = client['Employees'] # This command means either you can use Employees databse or if it's not there then create it.
    collections = database['EmployeesCollection']

    # To check all the collection inside the database:

    '''
    print(database.list_collection_names())
    '''

    # You must create something inside the collection for creating the DB

    '''
    dictionary = {"Name":"Default","ID":000000}
    collections.insert_one(dictionary)
    '''

# If you want to add more user on the database:

# You can insert one by one like this. You can use a for loop and add all the documents.

    '''
    dictionary1 = {"Name":"Ratul Pal","ID":26081997,"Department":"Software Developer"}
    collections.insert_one(dictionary1)
    '''

# Or you can use incert many.

    '''
    incertAllThese = [
        {"Name":"Priya Pal","ID":15041991},
        {"Name":"Sayantan Choushury","ID":21071989}
    ]
    collections.insert_many(incertAllThese)
    '''

# You can also find a data from the database.

# To get only one user.
    '''
    one = collections.find_one({'Name':"Priya Pal"})
    print(one)
    '''

# To get multiple users output.

    '''
    allFind = collections.find({'Name':'Default'})
    for items in allFind:
        print(items)
    '''

# To get only specific field

    '''
    allFindSpecific = collections.find({'Name':'Default'},{'Name': 1, '_id': 0})
    for items in allFindSpecific:
        print(items)
    '''

    '''
    The concept is:
    Database --> Collections --> Documents
    Now you can use limit(), count() all these files there.
    '''

# To update a document

    '''
    prev = {"Name":"Priya Pal"}
    updated = {"$set":{"Department":"Manager"}}
    collections.update_one(prev,updated)

    '''

    # To update many documents at the same time:
    
    '''
    collections.update_many(prev,updated)
    # If you want to check how many documents are updated you can run the command:
    print(collections.update_one(prev,updated).modified_count)
    '''

# To delete a document

    '''
    collections.delete_one({"Name":"Default"})
    collections.delete_many({"Name":"Default"})
    '''