from ast import Global
import sqlite3

# functionality phase

class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = sqlite3.connect('couses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS curse(Id interger, PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is private BOOLEAN NOT NULL DEAFULT 1) ")
        except Exception:
            print(" sorry!, unable to create a database")

# insert data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data
                    )
                return True
        except Exception:
            return True

# fetch_data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()                 
        except Exception:
            return False

# delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = " DELETE FORM course whre id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False

### USER INTERFACE#####

def main():
    print("*" * 50)
    print("\n:::  COURSE MANAGEMENT :: \n")
    print("*" * 50)
    print("\n")

    db = DatabaseManage()

    print("#"*60)
    print("\n :::   user manual   ::: \n")
    print("#"*60)

    print('\n Press 1. Insert new curse')
    print(' Press 2. Show all course ')
    print(' Press 3. Delete a course (NEED ID OF COURSE)\n')
    print("#"*60)
    print("\n")

    choice = input("\n Enter a choice here: ")

    if choice == '1':
        name = input("\n Enter a course name here: ")
        description = input("\n Enter a course description here: ")
        price = input("\n Enter a course price here: ")
        private = input("\n is this course private (0/1): ")


        if db.insert_data([name, description, price, private]):
            print(" COURSE was added to the database succesfully")

        else:
            print("OOPS, there was an error while adding a course to the database")

    elif choice == '2':
        print("\n ::: COURSE LIST :::")

        for index, item in enumerate(db.fetch_data()):
            print("\n Sl no : " + str(index + 1))
            print("COURSE ID : " + str(item[0]))
            print("COURSE Name : " + str(item[1]))
            print("COURSE Description : " + str(item[2]))
            print("COUSE Price : " + str(item[3]))
            private = 'YES' if item[4] else 'NO'
            print("is private : " + private)
            print("\n")
    
    elif choice == '3':
        record_id = input("Enter a course ID: ")

        if db.delete_data(record_id):
            print("Course was deleted successfully")

        else:
            print("OOps, something went wrong in an attempt to delete a course from the database")

    else:
        print("\n BAD CHOICE")


if __name__ == '__main__':
    main()









