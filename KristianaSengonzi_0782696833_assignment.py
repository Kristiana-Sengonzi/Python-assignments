

def get_phone(prompt):
    while True:
        phone = input(prompt)

        valid = True

        for char in phone:
            if not (char.isdigit() or char == "-"):
                valid = False

        if valid:
            return phone

        print("Invalid phone number")

def get_text(prompt):
    return input(prompt)

def get_email(prompt):
   while True:
      suggested_email=input(prompt)
      if "@" in suggested_email and "." in suggested_email:
         return suggested_email
      else:
         print("Please enter a valid email")

      

class ContactManager:
    def __init__(self):
       self.contacts={}
    def add_contact(self,name,tel_no,email):
       self.contacts[name]={
          "phone":tel_no,
           "email":email
       }
       print("Contact added ")
    def view_contact(self,name):
      if name in self.contacts:
        print("Name:", name)
        print("Phone:", self.contacts[name]["phone"])
        print("Email:", self.contacts[name]["email"])
      else:
        print("Contact not found")
       
    def update_contact(self,name,newtel_no,newemail):
       self.contacts[name]["phone"]=newtel_no
       self.contacts[name]["email"]=newemail

    def delete_contact(self,name):
        if name in self.contacts:
         del self.contacts[name]
         print("Contact deleted")
        else:
         print("Contact not found")

    def search_contacts(self, searchKey):
     found = False

     for name, details in self.contacts.items():

        if (
            searchKey in name
            or searchKey in str(details["phone"])
            or searchKey in details["email"]
        ):
            self.view_contact(name)
            found = True

     if not found:
        print("Contact not found")

    def list_all_contacts(self):
       for name,details in self.contacts.items():
          print("Name : ",name)
          print("Phone number : ",details["phone"])
          print("Email : ",details["email"])
          print("-----------------------------------------------------------------------------")

       


def main():
    manager=ContactManager()

    options=["1","2","3","4","5","6","7"]
    while True:
     print("=== Contact Manager Menu ===")
     print("1. Add Contact")
     print("2. View Contact")
     print("3. Update Contact")
     print("4. Delete Contact")
     print("5. Search Contacts")
     print("6. List All Contacts")
     print("7. Exit")

     selection=input("Choose an option (1-7):")
     if selection in options:
         if selection=="1":
             name=get_text("Enter contact name")
             tel_no=get_phone("Enter phone number")
             email=get_email("Enter email")
             manager.add_contact(name,tel_no,email)

         elif selection=="2":
             name=get_text("Enter contact name")
             manager.view_contact(name)

         elif selection=="3":
            name=get_text("Enter contact name")
            manager.view_contact(name)
            tel_no=get_phone("Enter phone number")
            email=get_email("Enter email")
            manager.update_contact(name,tel_no,email)
            manager.view_contact(name)

         elif selection=="4":
            name=get_text("Enter contact name")
            manager.delete_contact(name)

         elif selection=="5":
            searchKey=get_text("Search by  name,email or phone")
            manager.search_contacts(searchKey)

         elif selection=="6":
            manager.list_all_contacts()


        
         elif selection=="7":
             print("Exiting contact management menu")
             break
     else:
       print("Invalid input.Select Again") 
       continue
     
if __name__=="__main__":
    main()
       

        


