import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root',password = '',database = 'bloodbankdb')
mycursor = mydb.cursor()
while True:
    print("Select  : ")
    print("""            1. Add details
            2. view details
            3. search details
            4. update details
            5. delete details
            6. exit
             """)
    choice = int(input("Enter your choice : "))
    if choice==1:
        print("add details selected")
        name = input("Enter the name : ")
        bloodgroup = input("Enter the blood group : ")
        unit = input("Enter the unit : ")
        phone = input("Enter phone number : ")
        place = input("Enter place : ")
        sql ='INSERT INTO `bloodbank`(`donor_name`, `blood_group`, `unit`, `donor_phone`, `donor_place`) VALUES (%s,%s,%s,%s,%s)'
        data =(name,bloodgroup,unit,phone,place)
        mycursor.execute(sql,data)
        mydb.commit()

    if choice==2:
        print("view details selected")
        
        sql = 'SELECT * FROM `bloodbank`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    if choice==3:
        print("search details selected")
        blood_group = input('enter the blood group to be searched: ')
        
        sql = "SELECT `id`, `donor_name`, `blood_group`, `unit`, `donor_phone`, `donor_place` FROM `bloodbank` WHERE `blood_group`='"+blood_group+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

    if choice==4:
        print("update details selected")
        
        name = input('enter the name: ')
        blood_group = input('enter the blood group to be updated: ')
        place = input('enter the place: ')
        phone = input('enter the phone number: ')
        unit= input('enter the total blood donated: ')
        sql = "UPDATE `bloodbank` SET `donor_name`='"+name+"',`blood_group`='"+blood_group+"',`unit`='"+unit+"',`donor_phone`='"+phone+"',`donor_place`='"+place+"' WHERE `donor_name`='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
    if choice==5:
        ("delete details selected")
    if choice==6:
        break