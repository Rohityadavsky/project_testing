
# users = []
# this is the list store all data from the form ..!

'''
userDetails =[
    name,email,contact,password
]
'''
def userExited(userData,cursor):

    # Execute sql quer

    sql_query = f'''

                     SELECT * FROM users;
                     
                '''
    # execute cursor 
    try:            
        cursor.execute(sql_query)

        users = cursor.fetchall()
    except Exception as e:
        print("Error",e)

    print("users:")
    print(users)

    # unique id take email !!
    email = userData['email']

    for user in users:
        if user[2] == email:
            # if email found !
            return {'response':True,'user':user}
     # if email not found !
    return {'response':False,'user': {} }

def registerUser(userData,cursor):

    checkUser = userExited(userData,cursor)

    if (checkUser['response']):
        # if already data presenet in list this message show 
        return {'statusCode':503,'message':'Already Registerd'}
        
    else:
        # data store in list
        # users.append(userData)
        sql_query = f'''

                        INSERT INTO users (name,email,contact,password) VALUES ('{userData['name']}','{userData['email']}','{userData['contact']}','{userData['password']}')
         
                    '''
        try:
            # executer sql query !!
            cursor.execute(sql_query)

        except Exception as e:
            print("Error :",e)

        return {'statusCode':200,'message':'succesfuly registerd'}


def loginUser(userData,cursor):

    checkUser = userExited(userData,cursor)

    if checkUser['response']:
        # register password and login password matched or not !!
        if userData['password'] == checkUser['user'][4]:
            return {'statusCode':200,'message':'succesfuly loggedIn'}
        else:
            return {'statusCode':503,'message':'passworderror'}

    else:
        return {'statusCode':503,'message':'already loggedIn'}






        



    

    

    




