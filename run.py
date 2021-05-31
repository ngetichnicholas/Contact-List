#!/usr/bin/env python3.6
from contact import Contact

def create_contact(fname,lname,phone,email):
  '''
  Function to create a new contact
  '''
  new_contact = Contact(fname,lname,phone,email)
  return new_contact

def save_contact(contact):
  '''
  Function to save contact
  '''
  contact.save_contact()

def del_contact(contact):
  '''
  Function to delete a contact
  '''
  contact.delete_contact()

def copy_email(contact,number):
  '''
  Function to delete a contact
  '''
  contact.copy_email(number)

def find_contact(number):
  '''
  Function that finds a contact by number and returns the contact
  '''
  return Contact.find_by_number(number)

def check_existing_contact(number):
  '''
  Function that check if contact exists with number and returns a Boolean
  '''
  return Contact.contact_exist(number)

def display_contacts():
  '''
  Function that returns all the saved contacts
  '''
  return Contact.display_contacts()

def main():
  print("Hello Welcome to your contact list. What is your name?")
  user_name = input()

  print(f"Hello {user_name}. what would you like to do?")
  print('\n')

  while True:
    print("Use these short codes : \n cc - create a new contact \n dc - display contacts \n fc -find a contact \n dl -bto delete contact \n cp - to copy email address \n ex -exit the contact list ")

    short_code = input().lower()

    if short_code == 'cc':
      print("New Contact")
      print("-"*10)

      print ("First name ....")
      f_name = input()

      print("Last name ...")
      l_name = input()

      print("Phone number ...")
      p_number = input()

      print("Email address ...")
      e_address = input()


      save_contact(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
      print ('\n')
      print(f"New Contact {f_name} {l_name} created")
      print ('\n')

    elif short_code == 'dc':

      if display_contacts():
        print("Here is a list of all your contacts")
        print('\n')

        for contact in display_contacts():
          print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

        print('\n')
      else:
        print('\n')
        print("You dont seem to have any contacts saved yet")
        print('\n')

    elif short_code == 'fc':
      print("Enter the number you want to search for")

      search_number = input()
      if check_existing_contact(search_number):
        search_contact = find_contact(search_number)
        print(f"{search_contact.first_name} {search_contact.last_name}")
        print('-' * 20)

        print(f"Phone number.......{search_contact.phone_number}")
        print(f"Email address.......{search_contact.email}")
      else:
        print("That contact does not exist")


    elif short_code == 'dl':

      print("Enter the number you want to delete")

      delete_number = input()
      if check_existing_contact(delete_number):
        dl_contact = find_contact(delete_number)
        print(f"{dl_contact.first_name} {dl_contact.last_name} will be deleted")
        dl_contact = del_contact(dl_contact)
        print("Contact deleted successfully")

      else:
        print("That contact does not exist")

    elif short_code == 'cp':

      print("Enter the number you want to copy email from")

      find_number = input()
      if check_existing_contact(find_number):
        email_contact = find_contact(find_number)
        print(f"{email_contact.first_name} {email_contact.last_name}  {email_contact.email} email address will be copied")
        email_contact = copy_email(email_contact,find_number)
        print("Email address copied successfully")

      else:
        print("That contact does not exist")


    elif short_code == "ex":
      print("Bye .......")
      break
    else:
      print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

  main()