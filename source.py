import mysql.connector

con = mysql.connector.connect(  # use this to connect to the database
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()  # to navigate throughout the database

word = input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()  # to extract the data

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")
