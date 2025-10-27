import json

class Database:

    def add_data(self , name , email , password ):

        with open('db.json' , 'r') as rf:  #write mode me pura data replace ho jata h isleye ham phle read mode me on krenge
            database = json.load(rf) # jitne bhi user ka data h use hmne load kr lia

        if email in database:  # first we will check is there any same email or not
            return 0
        else:
            database[email] = [name , password]
            with open('db.json', 'w') as wf:
                json.dump(database, wf)
            return 1

    def search(self , email , password ):
        with open('db.json' , 'r') as rf:
            database = json.load(rf)
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
