from django.shortcuts import render,HttpResponse,redirect
from .utils import registerUser,loginUser
from django.contrib.sessions.backends.db import SessionStore # for sessions storage..!
import psycopg2

# s store key values pair data store in session !!
s = SessionStore()



# connection database !
try:
    connection = psycopg2.connect(
       host = "127.0.0.1",
       port = "5432",
       database = "memestore",
       user = "postgres",
       password = "csky@12345"
)   
    print("Database connection")
except Exception as e:
    print("Error :",e)
    print("Database connection Failed")

connection.autocommit= True
cursor = connection.cursor()


# Create your views here.

# home means main function page!!!
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')


# middleware function  work when api hit 
def checkSession():
    try:
        email = s['email']
        return True
    except Exception as e:
        print("Error :",e)
        return False

# registration function !!!!
def register(request):
    sessionExists = checkSession()

    if sessionExists == False:
    
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            password = request.POST['password']

            print(f'Name:{name}')
            print(f'Email:{email}')
            print(f'contact:{contact}')
            print(f'Password:{password}')

        

            # create dictionay !!!
            userData={
                'name':name,
                'email':email,
                'contact':contact,
                'password':password
            }

            response = registerUser(userData,cursor)

            print("response:")
            print(response)

        


            if response['statusCode']==200:
                # session sotre !!
                # s['name'] = userData['name']
                # s['contact'] = userData['contact']
            
                s['email'] = userData['email']
                s['password'] = userData['password']

                
                # return render(request,'register.html',{'message':'succesfuly registerd'})
                return redirect('/private/')

            else:
                return render (request,'register.html',{'message':'Already Registerd'})

        else:
            return render(request,'register.html')

    else:
        return redirect('/private/')

  # this is the login page       
def login(request):
    sessionExists = checkSession()
    if sessionExists == False:

    
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            print('email:')
            print(email)
            
            print('password:')
            print(password)

            # user dictonary create
            userData = {
                'email':email,
                'password':password
            }
            
            response = loginUser(userData,cursor)

            if response['statusCode']==200:
                # session sotre !!
                # s['name'] = userData['name']
                # s['contact'] = userData['contact']
                
                s['email'] = userData['email']
                s['password'] = userData['password']

               

                # return render(request,'login.html',{'message':'succesfuly loggedIn'})
                return redirect('/private/')

            elif response['statusCode']==503 and response['message']=='passworderror':
                return render(request,'login.html',{'message':'Password not matched'})

            else:
                return render(request,'login.html',{'message':'Not Registerd'})

        else:
            return render(request,'login.html')
    else:
        return redirect('/private/')


def logout(request):
    try:
        s.clear()
        return redirect('/login/')
    except:
        return redirect('/private/')
    # return render(request,'logout.html')
    
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')



def feedback(request):
    return render(request,'feedback.html')


def private(request):
    sessionExists = checkSession()

    if sessionExists == False:
        return redirect('/login/')

    else:
        return render(request,'private.html')
        