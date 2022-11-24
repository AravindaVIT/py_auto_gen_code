# test.py

# # table querry :
# patient_id	bigint	NO	PRI		
# first_name	varchar(100)	YES			
# last_name	varchar(100)	YES			
# gender	varchar(10)	YES			
# aadhaar_uid	varchar(12)	YES			
# phone_no	varchar(10)	YES			
# dob	varchar(15)	YES			
# pincode	int	YES			
# score	int	YES			
# screening	varchar(5)	YES			



import mysql.connector
import random
from random import randint
import datetime
import string
dic={}
end='f'
counter=0
while(end!='t'):
  if counter==100000:
    end='t'
  patient_id = random.randint(10000000000000,99999999999999)
  if patient_id in dic.keys():
    continue
  dob=datetime.date(randint(1930,1992), randint(1,12),randint(1,28))
  aadhaar_uid=random.randint(100000000000,999999999999)
  phone_no=random.randint(1000000000,9999999999)
  pincode=random.randint(100000,999999)
  first_name= ''.join(random.choices(string.ascii_lowercase , k=6))
  last_name= ''.join(random.choices(string.ascii_lowercase , k=6))
  gen_list= ['MALE','FEMALE','OTHER']
  gender=random.choice(gen_list)
  score=random.randint(0,10)
  if score>4:
    screening="yes"
  else:
    screening="no"
  
  mydb = mysql.connector.connect(
  host="localhost",
  user="ara1",
  password="1234",
  database="ncdw"
  )

  mycursor = mydb.cursor()
    #dic[patient_id]=[first_name,last_name,gender,aadhar_id,date,phone_number,pin,score,screening]

  sql = "INSERT INTO patient (patient_id,first_name,last_name,gender,aadhaar_uid,dob,phone_no,pincode,score,screening) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = ( patient_id,first_name,last_name,gender,aadhaar_uid,dob,phone_no,pincode,score,screening)

  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  counter=counter+1
#   dic[patient_id]=[first_name,last_name,gender,aadhar_id,date,phone_number,pin,score,screening]
# print(dic)


