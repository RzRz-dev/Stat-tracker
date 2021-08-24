import os
import win32api
from bs4 import BeautifulSoup
import codecs
import datetime

class Find_path_to_file:
    def __init__(self, game_name, file_to_find):
        self._game_name = game_name
        self.file_to_find = file_to_find

    @property
    def game_name(self):
        return self._game_name

    @game_name.setter
    def game_name(self, game_name):
        self._game_name = game_name

    @property
    def file_to_find(self):
        return self._game_to_find

    @file_to_find.setter
    def file_to_find(self, file_to_find):
        self._game_to_find = file_to_find

    def find_drives(self):
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        return drives

    def all_paths_to_file(self, search_path):
        result = []
        filename = self.file_to_find
        for root, dir,files in os.walk(search_path):
            if filename in files:
                result.append(os.path.join(root, filename))
        return result

    def get_general_path(self):
        try:
            drives_list = self.find_drives()
            paths = []
            for i in range(len(drives_list)):
                paths_in_local = self.all_paths_to_file(drives_list[i])
                if len(paths_in_local) > 0:
                    paths.append(paths_in_local)
            return paths
        except:
            print('An error has occurred accessing to the path')


class Access_to_a_file(Find_path_to_file):
   def __init__(self, game_name, file_to_find, access_file_name):
        super().__init__(game_name, file_to_find)
        self.acces_file_name = access_file_name

   @property
   def access_file_name(self):
        return self._acces_file_name

   @access_file_name.setter
   def access_file_name(self, access_file_name):
        self._acces_file_name = access_file_name

   def get_path_to_file(self):
        with open(self.acces_file_name, 'a') as pathfile_for_write:
            try:
                with open(self.acces_file_name, 'r') as pathfile_for_read:
                    if len(pathfile_for_read.readlines()) == 0:
                        pathfile_for_write.write(self.get_general_path()[0][0])
                        pathfile_for_write.close()
                        with open(self.acces_file_name, 'r') as update_for_read:
                            file_path = str(update_for_read.readline())
                            return file_path
                    else:
                        pathfile_for_read.seek(0)
                        file_exact_path = str(pathfile_for_read.readline())
                        return file_exact_path
            except:
                print('An error has ocurred while accessing to the file that contains the path')
            finally:
                pathfile_for_read.close()
                pathfile_for_write.close()


   def time_to_secs_celeste(self,time):
         time = time/10e6
         time_in_min = time/60
         time_in_hour = time/60
         return time_in_hour

   def format_secs_general(self,time):
         time_in_min = time/60
         time_in_hour = time/60
         return time_in_hour


   def get_celeste_data(self,path):
      try:
         file = codecs.open(str(path), 'r', encoding='utf8')
         xmldata = BeautifulSoup(file, "xml")
         total_deaths = xmldata.find('TotalDeaths').string
         total_strawberries = xmldata.find('TotalStrawberries').string
         total_golden_strawberries = xmldata.find('TotalGoldenStrawberries').string
         unlocked_areas = xmldata.find('UnlockedAreas').string
         totaltime = self.time_to_secs_celeste(int(xmldata.find('Time').string))
         areastats = xmldata.find_all('AreaStats')
         areastatsfaces = []
         casettecounter = 0
         for areas in areastats:
            if areas['Cassette'] == 'true':
                  casettecounter += 1
         cassettes = str(casettecounter)
         return unlocked_areas,cassettes,total_strawberries,total_golden_strawberries,int(total_deaths),round(totaltime,2)
      except:
            print('An error has occurred while accessing to Celeste data file, this could happen because celeste is not installed on your device')

   def get_ror2_data_file(self,path):
         try:
            file = codecs.open(str(path), 'r', encoding='utf8')
            xmldata = BeautifulSoup(file, "xml")
            filename = xmldata.find('userProfileFileName').string
            return filename + '.xml'
         except:
            print("An error has occurred accessing to the steam container file, or the game is not installed on your device")

   def get_ror2_data(self,path):
         try:
            file = codecs.open(str(path), 'r', encoding='utf8')
            xmldata = BeautifulSoup(file, "xml")
            highestStagesCompleted = xmldata.find('stat', attrs={'name':'highestStagesCompleted'}).string
            highestLevel = xmldata.find('stat', attrs={'name':'highestLevel'}).string
            totalDeaths = xmldata.find('stat', attrs={'name':'totalDeaths'}).string
            longestrun = []
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name':'longestRun.EngiBody'}).string))))
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name': 'longestRun.Bandit2Body'}).string))))
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name': 'longestRun.CaptainBody'}).string))))
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name': 'longestRun.CommandoBody'}).string))))
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name': 'longestRun.CrocoBody'}).string))))
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name': 'longestRun.HereticBody'}).string))))
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name': 'longestRun.HuntressBody'}).string))))
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name': 'longestRun.LoaderBody'}).string))))
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name': 'longestRun.MageBody'}).string))))
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name': 'longestRun.MercBody'}).string))))
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name': 'longestRun.ToolbotBody'}).string))))
            longestrun.append(self.format_secs_general(int(float(xmldata.find('stat', attrs={'name': 'longestRun.TreebotBody'}).string))))
            maxOfLongestRun = (max(longestrun))
            totalGamesPlayed = xmldata.find('stat', attrs={'name':'totalGamesPlayed'}).string
            totalWins = 0
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.EngiBody'}).string)
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.Bandit2Body'}).string)
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.CaptainBody'}).string)
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.CommandoBody'}).string)
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.CrocoBody'}).string)
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.HereticBody'}).string)
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.HuntressBody'}).string)
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.LoaderBody'}).string)
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.MageBody'}).string)
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.MercBody'}).string)
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.ToolbotBody'}).string)
            totalWins += int(xmldata.find('stat', attrs={'name': 'totalWins.TreebotBody'}).string)
            return int(highestStagesCompleted), int(highestLevel), int(totalDeaths), int(maxOfLongestRun), int(totalGamesPlayed), totalWins
         except:
            print("An eror has occurred accessing to the game save file, this could happen because Risk of Rain 2 is not installed on this device")


"""
path_to_celeste_data = Access_to_a_file('celeste', '0.celeste', 'celestepath.txt')
print(get_celeste_data(path_to_celeste_data.get_path_to_file()))

path_to_riskofrain2_alfa = Access_to_a_file('riskofrain2', 'PreviousRun.xml', 'riskofrain2patha.txt')
data_file_name = get_ror2_data_file(path_to_riskofrain2_alfa.get_path_to_file())


path_to_riskofrain2_beta = Access_to_a_file('riskofrain2', data_file_name, 'riskofrain2pathb.txt')
print(get_ror2_data(path_to_riskofrain2_beta.get_path_to_file()))
"""



#Antes de ejecutar, en terminal importar 
"""
pip install pywin32
pip install beautifulsoup4
"""
"""
import os
import win32api
from bs4 import BeautifulSoup
import codecs
import datetime
class findpathtofile:
    
   def find_drives(self):
      drives = win32api.GetLogicalDriveStrings()
      drives = drives.split('\000')[:-1]
      return drives

   def find_files(self, filename, search_path):
      result = []
      for root, dir, files in os.walk(search_path):
         if filename in files:
            result.append(os.path.join(root, filename))
      return result


   def getpath(self):
      drives_list = self.find_drives()
      paths = []
      for i in range(len(drives_list)):
         paths_in_local = self.find_files("0.celeste", drives_list[i])
         if len(paths_in_local) > 0:
            paths.append(paths_in_local)
      return paths


   def getpathtofile(self):
      with open('celestepath.txt', 'a') as pathfile_forwrite:
         try:
            with open('celestepath.txt', 'r') as pathfile_forread:
               if len(pathfile_forread.readlines()) == 0:
                  pathfile_forwrite.write(self.getpath()[0][0])
                  pathfile_forwrite.close()
                  with open('celestepath.txt', 'r') as update_forread:
                     absolutepath = str(update_forread.readline())
                     return absolutepath
               else:
                  pathfile_forread.seek(0)
                  absolutepath = str(pathfile_forread.readline())
                  return absolutepath
         finally:
            #return absolutepath
            pathfile_forwrite.close()
            pathfile_forread.close()



def time_to_secs(time):
   time = time/10e6
   return str(datetime.timedelta(seconds=time))

   #Con este código retornará una lista con todos los datos que usaremos, y el tiempo en cada cara de la montaña, nivel por nivel siendo el primer valor cara A, el segundo B y el tercero C
def getcelestedata(path):
   file = codecs.open(str(path), 'r', encoding='utf8')
   xmldata = BeautifulSoup(file, "xml")
   total_deaths = xmldata.find('TotalDeaths').string
   total_strawberries = xmldata.find('TotalStrawberries').string
   total_golden_strawberries = xmldata.find('TotalGoldenStrawberries').string
   unlocked_areas = xmldata.find('UnlockedAreas').string
   totaltime = time_to_secs(int(xmldata.find('Time').string))
   areastats = xmldata.find_all('AreaStats')
   areastatsfaces = []
   casettecounter = 0
   for areas in areastats:
      if areas['Cassette'] == 'true':
         casettecounter += 1
      facestats = []
      for faces in areas.find_all('AreaModeStats'):
         facestats.append(time_to_secs(int(faces['TimePlayed'])))
      areastatsfaces.append(facestats)
   cassettes = str(casettecounter)
   return total_deaths, total_strawberries, total_golden_strawberries, unlocked_areas, totaltime, areastatsfaces, cassettes


def printcelestedata(path):
    file = codecs.open(str(path), 'r', encoding='utf8')
    xmldata = BeautifulSoup(file, "xml")
    print("Total Deaths: "+xmldata.find('TotalDeaths').string)
    print("Total Strawberries: "+xmldata.find('TotalStrawberries').string)
    print("Total Golden Strawberries: "+xmldata.find('TotalGoldenStrawberries').string)
    print("Completed Levels: "+xmldata.find('UnlockedAreas').string)
    totaltime = int(xmldata.find('Time').string)
    print("Total Time Played: " + time_to_secs(totaltime))
    areastats = xmldata.find_all('AreaStats')
    #print(type(areastats))
    casettecounter = 0
    for areas in areastats:
        print('Level: '+areas['ID'])
        if areas['Cassette'] == 'true':
            casettecounter += 1
        faces_id = 0
    for faces in areas.find_all('AreaModeStats'):
        print('Face ',faces_id, ': ', time_to_secs(int(faces['TimePlayed'])))
        faces_id += 1
    print("Casettes Obtained: " + str(casettecounter))
    
try:
    pathtofile = findpathtofile()
    getcelestedata(pathtofile.getpathtofile())
except:
    print("Celeste is not installed on your system")
"""


   



