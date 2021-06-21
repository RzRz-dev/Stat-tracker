import firebase_admin, hashlib
import json
from firebase_admin import db

#Escribir en la base de datosa

databaseURL = "https://stats-tracker-6563e-default-rtdb.firebaseio.com/"
#cred_obj = firebase_admin.credentials.Certificate('stats-tracker-6563e-firebase-adminsdk-x2pev-964f37b0f7.json')
cred_obj = firebase_admin.credentials.Certificate('scr\stats-tracker-6563e-firebase-adminsdk-x2pev-964f37b0f7.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL' : databaseURL
})
'''




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
user_ref = db.reference("/Games/")
x=user_ref.get()
y=x.keys()
print(y)
'''


# Sistema de login 2 simplificado
class LoginBase:
    ref = db.reference("/")
    def GetUserDatabase(self,username):
        user_ref = db.reference("/Basic Data/"+username)
        return user_ref

    def GetId(self,username):
        x=self.GetUserDatabase(username)
        user_database = x.get()
        return user_database['id']
    def GetGamesNames(self):
        games_ref=db.reference("/Games/")
        lista=games_ref.get()
        lista=lista.keys()
        return lista

    def LoginUser(self,user_ref,password):
        user_database = user_ref.get()
        try:
            if user_database['password'] == password:
                return "Entrando"
            else:
                return "Contraseña Erronea"
        except:
            return "User Not Found"

    def RegisterUser(self,user_ref,username,password):
        user_database = user_ref.get()
        if user_database==None:
            newId = hashlib.sha1(username.encode('utf-8'))
            self.ref.child('Basic Data').update({username:{'id' : newId.hexdigest(), 'password' : password}})
            return True
        else:
            return False
    def GetPlayerInfo(self,id,ref):
        game_ref=db.reference("/Games/"+ref+"/"+id)
        lista=game_ref.get()
        return lista

          
            

