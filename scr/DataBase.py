import firebase_admin
import json
from firebase_admin import db

#Escribir en la base de datosa

databaseURL = "https://stats-tracker-6563e-default-rtdb.firebaseio.com/"
#cred_obj = firebase_admin.credentials.Certificate('stats-tracker-6563e-firebase-adminsdk-x2pev-964f37b0f7.json')
cred_obj = firebase_admin.credentials.Certificate('scr\stats-tracker-6563e-firebase-adminsdk-x2pev-964f37b0f7.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL' : databaseURL
})

ref = db.reference("/")



#with open("data2.json", "r") as f:
#    file_contents = json.load(f)
#    ref.set(file_contents)



# Leer de la base de datos

database = ref.get()



id_given = '02'
password_given = 'qwe'

for user in database['Basic Data']:
    if database['Basic Data'][user]['id'] == id_given and database['Basic Data'][user]['password'] == password_given:
        user_name = user
        user_id = database['Basic Data'][user]['id']
        print(user_name, user_id)
        break
else:
    print("Wrong user or password")


print(database['Games']['LoL'][user_id])

# Actualizar en la base de datos

def change_password(user_name_a):
    new_password = input('Insert new password: ')
    ref = db.reference("/")


    ref.child('Basic Data').child(user_name_a).update({'password':new_password})

#change_password(user_name)



# Sistema de login 2 simplificado
class LoginBase:
    def GetUserDatabase(self,username):
        user_ref = db.reference("/Basic Data/"+username)
        return user_ref

    def LoginUser(self,user_ref,password):
        user_database = user_ref.get()
        try:
            if user_database['password'] == password:
                print("Entrando")
            else:
                print("Contraseña Erronea")
        except:
            print("User Not Found")

    def RegisterUser(self,user_ref,username,password,id):
        user_database = user_ref.get()
        if user_database==None:
            print("No existe, lo registro")
            ref.child('Basic Data').update({username:{'id' : id, 'password' : password}})
        else:
            print("Ya existe el usuario, no se registrará")
          
            

