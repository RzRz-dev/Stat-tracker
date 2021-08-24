import pyrebase

class FileManeger():
    def __init__(self):
        config={
            "apiKey": "AIzaSyBsWgNcaghiU_1R_1M9j6RLfyNLbeilfy4",
            "authDomain": "stats-tracker-6563e.firebaseapp.com",
            "databaseURL": "https://stats-tracker-6563e-default-rtdb.firebaseio.com",
            "projectId": "stats-tracker-6563e",
            "storageBucket": "stats-tracker-6563e.appspot.com",
            "messagingSenderId": "884010211496",
            "appId": "1:884010211496:web:993ed9c8d3219a7cf14a9d",
            "measurementId": "G-2B8PTPZQKN"
        }
        firebase=pyrebase.initialize_app(config)
        self.storage= firebase.storage()
        self.localS="scr/Datos/"
        self.cloudS="files/"
        
    def UploadFile(self,fileName="Some.json"):
        try:
            self.storage.child(self.cloudS+fileName).put(self.localS+fileName)
        except:
            print("error de subida")

    def DownloadFile(self,fileName="Some.json"):
        try:
            self.storage.child(self.cloudS+fileName).download("scr/Datos",fileName)
        except:
            print("error de descarga")

manager = FileManeger()
a = None
while a != "3":
    a = input()
    if a == "1":
        manager.UploadFile()
    elif a == "2":
        manager.DownloadFile()
