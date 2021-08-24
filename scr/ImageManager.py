import  pyrebase

class ImageManager:
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
        self.localS="scr/Images/"
        self.cloudS="images/"
    '''
    def downloadImage (self,fileName):
        try:
            self.storage.child(self.cloudS+fileName).download(self.localS+"test.jpg")
        except:
            print("error de descarga")
    '''
    def uploadImage (self,filename,saveas):
        
            
        self.storage.child(self.cloudS+"juegos/"+saveas).put(self.localS+filename)
        '''
        except:
            print("error de descarga")
            '''
    

    def GetUrl_Image(self,ruta,nombre):
        path_on_cloud = "images/"+ruta+"/"+str(nombre)
        x=self.storage.child(path_on_cloud).get_url(1)
        return x
        
if __name__ == '__main__':
    x=ImageManager()
    x.uploadImage("Dark Souls.jpg","Dark Souls")
