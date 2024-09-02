import mysql.connector

def connect_db():
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="Amaan@2005", database="student_management")
        if con.is_connected():
            return con
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
# Print data
def get_students():
    con = connect_db()
    if con:
        try:
            print("----STUDENTS----")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM student")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            con.close()
    else:
        print("Failed to connect db")

def get_courses():
    con = connect_db()
    if con:
        try:
            print("----COURSES----")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM courses")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            con.close()
    else:
        print("Failed to connect db!")

def get_enrollments():
    con = connect_db()
    if con:
        try:
            print("---- ENROLLMENTS----")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM enrollments")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            con.close()
    else:
        print("Failed to connect db!")

# Add data
def add_student(student_id, first_name, last_name, phone, email):
    con = connect_db()
    if con:
        try:
            cursor = con.cursor()
            query = "INSERT INTO student(student_id, first_name, last_name, phone, email) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (student_id, first_name, last_name, phone, email))
            con.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            con.rollback()
        finally:
            cursor.close()
            con.close()
    else:
        print("Failed connecting to database!")

def add_course(course_id, course_name):
    con = connect_db()
    if con:
        try:
            cursor = con.cursor()
            query = "INSERT INTO courses (course_id, course_name) VALUES (%s, %s)"
            cursor.execute(query, (course_id, course_name))
            con.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            con.rollback()
        finally:
            cursor.close()
            con.close()
    else:
        print("Failed to connect db!")

# Update data
def update_student(student_id, first_name=None, last_name=None, phone=None, email=None):
    con = connect_db()
    if con:
        try:
            cursor = con.cursor()
            query = "UPDATE student SET "
            values = []

            if first_name:
                query += "first_name = %s, "
                values.append(first_name)
            if last_name:
                query += "last_name = %s, "
                values.append(last_name)
            if phone:
                query += "phone = %s, "
                values.append(phone)
            if email:
                query += "email = %s, "
                values.append(email)

            query = query.rstrip(', ') + " WHERE student_id = %s"
            values.append(student_id)

            cursor.execute(query, tuple(values))
            con.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            con.rollback()
        finally:
            cursor.close()
            con.close()
    else:
        print("Failed to connect db!")

def update_courses(course_id, course_name):
    con = connect_db()
    if con:
        try:
            cursor = con.cursor()
            query = "UPDATE courses SET course_name = %s WHERE course_id = %s"
            cursor.execute(query, (course_name, course_id))
            con.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            con.rollback()
        finally:
            cursor.close()
            con.close()
    else:
        print("Failed to connect db!")

def update_enrollments( course_id,student_id, course_name):
    con = connect_db()
    if con:
        try:
            cursor = con.cursor()
            query = "UPDATE enrollments SET course_name = %s WHERE course_id = %s AND student_id = %s"
            values = (course_name, course_id, student_id)
            
            # Debugging: Print the query and values
            # print(f"Executing Query: {cursor.mogrify(query, values)}")
            
            cursor.execute(query, values)
            con.commit()

            # Check if any rows were affected
            if cursor.rowcount == 0:
                print("No rows were updated. Check if the course_id and student_id exist.")
            else:
                print(f"Updated {cursor.rowcount} rows successfully.")
                
        except Exception as e:
            print(f"An error occurred: {e}")
            con.rollback()
        finally:
            cursor.close()
            con.close()
    else:
        print("Failed to connect to the database!")


# Delete data
def delete_student(student_id):
    con = connect_db()
    if con:
        try:
            cursor = con.cursor()
            query = "DELETE FROM student WHERE student_id = %s"
            cursor.execute(query, (student_id,))
            con.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            con.rollback()
        finally:
            cursor.close()
            con.close()
    else:
        print("Failed to connect db!")

def delete_course(course_id):
    con = connect_db()
    if con:
        try:
            cursor = con.cursor()
            query = "DELETE FROM courses WHERE course_id = %s"
            cursor.execute(query, (course_id,))
            con.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            con.rollback()
        finally:
            cursor.close()
            con.close()
    else:
        print("Failed to connect db!")

def delete_enrollment(course_id, student_id):
    con = connect_db()
    if con:
        try:
            cursor = con.cursor()
            query = "DELETE FROM enrollments WHERE course_id = %s AND student_id = %s"
            cursor.execute(query, (course_id, student_id))
            con.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            con.rollback()
        finally:
            cursor.close()
            con.close()
    else:
        print("Failed to connect db!")

# Main menu loop
def menu():
    while True:
        print("\n1. Add student:")
        print("2. Print data:")
        print("3. Update table:")
        print("4. Exit:")
        print("5. Add course:")
        print("6. Delete data:")   
        choice = int(input(":"))
        if choice == 1:
            student_id = int(input("Enter student id:"))
            firstname = input("Enter first name:")
            lastname = input("Enter last name:")
            phone = int(input("Enter phone number:"))
            email = input("Enter email:")
            add_student(student_id, firstname, lastname, phone, email)
        elif choice == 2:
            print("\n1. Print students data:")
            print("2. Print courses data:")
            print("3. Print enrollments data:")
            innerchoice = int(input(":"))
            if innerchoice == 1:
                get_students()
            elif innerchoice == 2:
                get_courses()
            elif innerchoice == 3:
                get_enrollments()
            else:
                print("Invalid choice! Enter a valid choice.")
        elif choice == 3:
            print("\n1. Update students table:")
            print("2. Update courses table:")
            print("3. Update enrollments table:")
            innerChoice = int(input(":"))
            if innerChoice == 1:
                id = int(input("Enter student id:"))
                fname = input("Updated first name (leave blank if not required): ")
                lname = input("Updated last name (leave blank if not required): ")
                phone = input("Enter new phone no. (leave blank if not required): ")
                email = input("Update email (leave blank if not required): ")
                update_student(id, fname if fname else None, lname if lname else None, int(phone) if phone else None, email if email else None)
            elif innerChoice == 2:
                courseid = int(input("Enter course id:"))
                coursename = input("Enter updated course name:")
                update_courses(courseid, coursename)
            elif innerChoice == 3:
                course_id = int(input("Enter course id:"))
                student_id = int(input("Enter student id:"))
                course_name = input("Enter course name:")
                update_enrollments(course_id, student_id, course_name)
            else:
                print("Invalid choice! Enter a valid choice.")
        elif choice == 4:
            break
        elif choice == 5:
            course_id = int(input("Enter course id:"))
            course_name = input("Enter course name:")
            add_course(course_id, course_name)
        elif choice == 6:
            print("\n1. Delete student:")
            print("2. Delete course:")
            print("3. Delete enrollment:")
            deletechoice = int(input(":"))
            if deletechoice == 1:
                stu_id = int(input("Enter student id to delete:"))
                delete_student(stu_id)
            elif deletechoice == 2:
                crs_id = int(input("Enter course id to delete:"))
                delete_course(crs_id)
            elif deletechoice == 3:
                c_id = int(input("Enter course id:"))
                s_id = int(input("Enter student id:"))
                delete_enrollment(c_id, s_id)
            else:
                print("Invalid choice!")
        else:
            print("Invalid choice! Enter a valid choice.")

menu()
