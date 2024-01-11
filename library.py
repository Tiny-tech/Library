class Pec:
    def __init__(self):
        self.student_login_details = {}
        self.book_names = [
    "The Hobbit","Harry Potter and the Sorcerer's Stone","To Kill a Mockingbird","1984","The Great Gatsby","Pride and Prejudice",
    "The Catcher in the Rye","The Lord of the Rings","The Chronicles of Narnia", "The Da Vinci Code","The Kite Runner",
    "The Grapes of Wrath"]

        print("""
              
           |===============================|      
           |   Welcome to PEC Library      |
           |-------------------------------|
           | 1. Create a Student Account   |
           | 2. Student Login              |   
           | 3. Exit                       |
           |===============================|    
        """)
        self.main_page()
   
    def main_page(self):
        student = int(input("Please Select the What you want: "))
        try:
            if student == 1:
                self.create_student_login()
            elif student == 2:
                self.student_login()
            else:
                print('Thanks for using our Library')
        except ValueError as e:
            print(f'Please Enter the Integer Value Only {e}')



    def create_student_login(self):
        self.student_name = input("Please Enter Your Name: ")
        self.register_num = int(input('Please Enter Your Register Number: '))
        self.user_name = input('Please Enter Your Username: ')
        self.password = input('Please Enter Your Password: ')
        self.student_login_details[self.register_num] = {'Student Name': self.student_name,"Username":self.user_name,"Password":self.password}
        print('Your Library Account Has been Created Successfully...')
        print(self.student_login_details)
        self.main_page()

    def student_login(self):
        username = input('Please Enter Your Username: ')
        passcode = input('Please Enter Your Password: ')
        user_info = self.student_login_details.get(self.register_num)
        if user_info['Username'] == username:
            if user_info and user_info['Password'] == passcode:
                print(f'Access Granted Welcome {self.student_name}')
                print("""
                      |===========================|
                      | 1. Show Books             |
                      | 2. Lend Books             |
                      | 3. Return Books           |
                      | 4. Exit                   |
                      |===========================|
                      """)
        choice = int(input('Enter a Number: '))
        try:
            if choice == 1:
                self.show_books()
            elif choice == 2:
                self.lend_books()
            elif choice == 3:
                self.return_books()
            else:
                print('Thank You...')
        except ValueError as e:
            print('Please Enter integer value only: ',e)

        else:
            print('error')
            self.student_login()
    def show_books(self):
        print('Welcome to PEC Library')
        print('List of books: \n')
        for book in self.book_names:
            print(book)
        self.student_login()
    def lend_books(self):
        print('Welcome to PEC Library')
        select_book = input('Please Enter a Book Name: ')
        try:
            if select_book in self.book_names:
                book_names = self.book_names.remove(select_book)
                print(f'Your {select_book} Book Has been Lend Successfully')
                choice = input('If you Want to Check the Book Status: Y/N ')
                if choice == 'y':
                    self.show_books()
                    
                else:
                    print('Thanks for using PEC Library')
        except ValueError as e:
            print('Please enter the listed book names',e)

    def return_books(self):
        print('Welcome to PEC Library')
        select_book = input('Please Enter a Book Name: ')
        try:
            if select_book not in self.book_names:
                book_name = self.book_names.append(select_book)
                print(f'Your Book {select_book} has been return successfully')
        except ValueError as e:
            print('The book is already present Please check the book name',e)
    

pec = Pec()

pec.main_page()