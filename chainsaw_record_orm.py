from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import user_interface

from chainsaw_record_holder import Chainsaw


engine = create_engine('sqlite:///record_holder.db', echo=False)

# Creating a table for all the things that use Base
Base.metadata.create_all(engine)

#Making a Session class
Session = sessionmaker(bind=engine)



def setup():
    #TODO make this only enter this infromation ONCE!
    # setting up the first data
    record1 = Chainsaw(record_name='Ian Stewart', country="Canada", number_of_catches= 94)
    record2 = Chainsaw(record_name='Aaron Gregg', country="Canada", number_of_catches= 88)
    record3 = Chainsaw(record_name='Chad Taylor', country="USA", number_of_catches= 78)

    save_session = Session()

    save_session.add_all([ record1, record2, record3 ])

    save_session.commit()   # All data saved. Now nothing is new, or dirty

    save_session.close()


def handle_choice(choice):
    # menu handler
    if choice == '1':
        insert_row()

    elif choice == '2':
        view_records()

    elif choice == '3':
        delete_row()

    elif choice == '4':
        search_records()

    elif choice == '5':
       update_catches()

    elif choice == 'q':
        quit()

    else:
        print('Please enter a valid selection')

def insert_row():

    # Ask user for information
    name = input('Enter name of record holder: ')
    country = input('Enter the Country of the record holder: ')
    number_catches = int(input('Enter the number of catches (as an integer): '))
    # inserting the new row
    record = Chainsaw(record_name=name, country=country, number_of_catches=number_catches)

    save_session = Session()

    save_session.add(record)

    save_session.commit()

    save_session.close()

def view_records():
    # viewing all the records
    search_session = Session()

    for phone in search_session.query(Chainsaw):
        print(phone)

def search_records():
    search_session = Session()
    # getting the user input and showing the search results
    record_search = input('Please enter the name of the record holder you want to search for:')

    print(search_session.query(Chainsaw).filter_by(record_name= record_search).one())

def update_catches():

    update_session = Session()
    # getting the user input and updating the record
    record_name = input('Please enter the name of the record holder to update:')
    record_catches = input('Please enter the amount of catches you want to update:')
    old_record = update_session.query(Chainsaw).filter(Chainsaw.record_name == record_name)

    for record in old_record:
        record.number_of_catches = record_catches

    update_session.commit()

    update_session.close()

def delete_row():

    delete_session = Session()
    record_delete = input('Please enter the name of the record holder to delete:')
    # Query and deleting the user selected record holder
    for record_holder in delete_session.query(Chainsaw).filter_by(record_name=record_delete):
        delete_session.delete(record_holder)
    delete_session.commit()


def main():

    setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = user_interface.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()