# import mysql connector

import dbconn

def update_employee(empid, employee):
    # get connection
    conn = dbconn.get_connection()

    # form a query
    query = f"update employee SET salary = %s where empidid = %s;"
    val = (empid, employee)

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



update_employee(41, 50000)












