import sqlite3
from peewee import *
db = SqliteDatabase('record.sqlite')

class RecordError(Exception):
    pass
class Juggler(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()
##juggler class, these are going to be part of the database
    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} is from {self.country} and had {self.catches} catches'

db.connect()
db.create_tables([Juggler])
#connecting and creating table
def addJuggler():
    name = input("Enter the name of the juggler \n ")
    country = input("Enter their Country \n ")
    catches = float(input("Enter the number of catches \n "))
    add_record_holder(name, country, catches)
    ##function to add juggler, calls record holder with name country and catches
def add_record_holder(name, country, catches):

    if not name:
        raise RecordError('Provide a record holder name')
    if not country:
        raise RecordError('Provide a Country')
    if not isinstance(catches, (int, float)) or catches < 0:
        raise RecordError('Provide a positive number for catches')
    name = Juggler(name = name, country = country, catches = catches)
    name.save()
##adding juggler to db
def searchName():
    search_name = input("Enter the name to search for \n")
    searchedName = Juggler.get_or_none(Juggler.name == search_name)
    try:
        print(search_name +" recorded "+str(searchedName.catches)+" catches")
    except:
        print("No record for "+search_name)
##searching for juggler, returning none if none found
def deleteName():
    delete_name = input("Enter a name to delete")
    rows_deleted = Juggler.delete().where(Juggler.name == delete_name).execute()
    if rows_deleted >= 1:
        print(delete_name+" deleted")
    else:
        print("No record found for "+delete_name)
##deleting jugglers, returning none if none found
def main():

    while True:
        choice =int(input("MENU \n1: Add juggler \n2: Search by name \n3: Delete by name \n4: Exit  \n"))
        if choice == 1:
            addJuggler()
        elif choice == 2:
            searchName()
        elif choice == 3:
            deleteName()
        elif choice == 4:
            break
        else:
            print("Unknown option selected")
##menu
if __name__ == '__main__':
    main()


