from Node_Tools import Node, LinkedList
import pip
import requests as requests
import json
import sys
import time

class LOL_Info:
    def __init__(self):
        self.api_key = str(input("Insert API Key: "))
        #self.isable = 1
        
    
    def start_Stats(self):
        self.__set_acc_info()
        self.__set_league_info()
        self.__set_match_list()

    def __receive_name(self):
        summoner_name = input("Insert a summoner name, or write !exit to exit of the application: ")
        return summoner_name
    


    # Reemplazar luego el summoner name con input y cambiar el api key a diario
    #summoner_name = input("Ingrese un nombre de invocador: ")
    #Aqui, a partir del summoner name obtendremos account id y summoner id
    #response = requests.get(
    #   "https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/+"+summoner_name+"?api_key="+api_key)
    def __set_acc_info(self):
        name = self.__receive_name()
        response = requests.get(
            "https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/+"+name+"?api_key="+self.api_key)
    #info_acc es un diccionario con toda la info de la cuenta a partir del nombre de invocador
        if response.status_code == 200:
            info_acc=response.json() 
            self.icon_id = info_acc["profileIconId"]
            #self.account_id = info_acc["accountId"]
            self.summoner_id = info_acc["id"]
            self.puuid = info_acc["puuid"]
            self.summoner_name = info_acc["name"]
        elif name == "!exit":
            sys.exit()

        else:
            print("Nombre inválido, intentalo de nuevo")
            self.__set_acc_info()
            
    
    #Response 2 obtendrá la información de la liga de cada invocador que se suministre
    def __set_league_info(self):
        response = requests.get(
            "https://la1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+self.summoner_id+"?api_key="+self.api_key
        )
        #info_ligas es un diccionario que muestra su clasificación en ranked, tanto en soloQ como en flexQ
        info_ligas = response.json()
        if len(info_ligas) == 0:

            self.type_queue_1 = "UNRANKED FLEX"
            self.league_atm_1 = ""
            self.division_atm_1 = ""
            self.type_queue_2 = "UNRANKED SOLOQ"
            self.league_atm_2 = ""
            self.division_atm_2 = ""

        elif len(info_ligas) == 1:
            self.type_queue_1 = info_ligas[0]["queueType"]
            self.league_atm_1 = info_ligas[0]["tier"]
            self.division_atm_1 = info_ligas[0]["rank"]
            self.type_queue_2 = ""
            self.league_atm_2 = ""
            self.division_atm_2 = ""
        else:
            self.type_queue_1 = info_ligas[0]["queueType"]
            self.league_atm_1 = info_ligas[0]["tier"]
            self.division_atm_1 = info_ligas[0]["rank"]
            self.type_queue_2 = info_ligas[1]["queueType"]
            self.league_atm_2 = info_ligas[1]["tier"]
            self.division_atm_2 = info_ligas[1]["rank"]

    #Response 3 obtendrá toda la match list de la persona a través de su account id
    def __set_match_list(self):

        response = requests.get(
        #"https://la1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+self.account_id+"?api_key="+self.api_key
        "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"+ self.puuid + "/ids?start=0&count=20"+"&api_key=" + self.api_key
        )
        temp=response.json()  
        self.match_list = LinkedList()
        for i in range(len(temp)):
            data=temp[i]
            self.match_list.insert_at_end(data)

    def find_match(self,match_code):
        response4 = requests.get(
            "https://americas.api.riotgames.com/lol/match/v5/matches/" + match_code + "?api_key=" + self.api_key
        )

        self.match_info = response4.json()
        if response4.status_code == 200:
            for i in range(len(self.match_info["info"]["participants"])):
                if self.puuid == self.match_info["info"]["participants"][i]["puuid"]:
                    game_mode = self.match_info["info"]["gameMode"]
                    queue_type = self.find_queue(self.match_info["info"]["queueId"])
                    champion_name = self.match_info["info"]["participants"][i]["championName"]
                    won = self.match_info["info"]["participants"][i]["win"]
                    assists = self.match_info["info"]["participants"][i]["assists"]
                    kills = self.match_info["info"]["participants"][i]["kills"]
                    deaths = self.match_info["info"]["participants"][i]["deaths"]
                    creep_score = self.match_info["info"]["participants"][i]["totalMinionsKilled"]
                    gold_earned = self.match_info["info"]["participants"][i]["goldEarned"]
                    if deaths != 0:
                        kda = (kills+assists)/deaths
                    else:
                        kda = (kills+assists)/(deaths+1)
                    kda = round (kda, 2)
                    if won == True:
                        return game_mode , queue_type, champion_name, "Kills: "+ str(kills), "Deaths: "+str(deaths), "Assists: "+str(assists), "Creep score: "+str(creep_score), "Gold earned: "+ str(gold_earned), "KDA: "+str(kda),"Victory"
                    else:
                        return game_mode , queue_type, champion_name, "Kills: "+ str(kills), "Deaths: "+str(deaths), "Assists: "+str(assists), "Creep score: "+str(creep_score), "Gold earned: "+ str(gold_earned), "KDA: "+str(kda),"Defeat"
        else:
            return ()
        
    def find_queue(self,queue_Id):
        with open('queues.json') as json_file:
            queues_data = json.load(json_file)
            for i in range(len(queues_data)):
                if queue_Id == queues_data[i]["queueId"]:
                    return(queues_data[i]["description"])
    
    #match_list muestra las partidas recientes jugadas por la cuenta
    '''
    def __find_champion(self,key):
        with open('champion.json', encoding="utf8") as json_file:
            champion_data = json.load(json_file)
        for champions_name in champion_data["data"]:
            if key == champion_data["data"][champions_name]["key"]:
                print(champion_data["data"][champions_name]["id"])
    '''
    def get_info(self):
        print(self.summoner_name)
        print(self.icon_id)
        #print("Flex: ",self.liga_actual_flex, self.division_actual_flex)
        #print("SoloQ: ",self.liga_actual_solo, self.division_actual_solo)
        '''
        for i in range(le):
            self.__find_champion(str(self.match_list["matches"][i]["champion"]))
        '''
        print("")
        #Marca un error muy xd
        # print("Ranked SOLO/DUO" if self.type_queue_1 == "RANKED_SOLO_5x5" else "Ranked FLEX 5v5" if self.type_queue_1 == "RANKED_FLEX_SR"  else "Unranked")
        if self.type_queue_1 == "RANKED_SOLO_5x5":
            print("Ranked SOLO/DUO", end = " ")
        elif self.type_queue_1 == "RANKED_FLEX_SR":
            print("Ranked FLEX", end = " ")
        else:
            print("Unranked")
        print(self.league_atm_1, self.division_atm_1)
        #print("Ranked SOLO/DUO" if self.type_queue_2 == "RANKED_SOLO_5x5" else "Ranked FLEX 5v5" if self.type_queue_2 == "RANKED_FLEX_SR" else "Unranked")
        if self.type_queue_2 == "RANKED_SOLO_5x5":
            print("Ranked SOLO/DUO", end = " ")
        elif self.type_queue_2 == "RANKED_FLEX_SR":
            print("Ranked FLEX", end = " ")
        else:
            print("Unranked")
        print(self.league_atm_2, self.division_atm_2)
        print("")
        print("LAST 20 GAMES PLAYED:")
        actual=self.match_list.head
        if (self.match_list.head==None) and (self.match_list.tail == None):
            print("\n"+
            "--------------------------------------------------------------------------------------------"
            +"\n"+
            "No recent matches found"
            +"\n"+
            "--------------------------------------------------------------------------------------------"
            +"\n")
        else:
            while True:
                print("\n"+
                "--------------------------------------------------------------------------------------------")
                current=self.find_match(actual.data)
                for i in range(len(current)):
                    print(current[i])
                print(
                "--------------------------------------------------------------------------------------------"
                +"\n"+"\n"+
                "Which game do you want to see?"
                +"\n"+
                "Previous, Next or List"
                +"\n"+
                "(Enter anything else to exit)"
                +"\n")
                des=input().lower()
                if des=="next":
                    actual=actual.next
                    if actual==None:
                        actual=self.match_list.head
                elif des=="previous":
                    actual=actual.back
                    if actual==None:
                        actual=self.match_list.tail
                elif des=="list":
                    con=1
                    inicio=self.match_list.head
                    while inicio != None:
                        current=self.find_match(inicio.data)
                        print(con)
                        for i in range(len(current)):
                            print(current[i])
                        print("--------------------------------------------------------------------------------------------"
                        +'\n')
                        inicio=inicio.next
                        con+=1
                elif des=="tlist":
                    ntests =  int(input("enter number of tests"+"\n"))
                    all_tests=[]
                    while ntests > 0:
                        startt=time.perf_counter()
                        con=1
                        inicio=self.match_list.head
                        while inicio != None:
                            current=self.find_match(inicio.data)
                            print(con)
                            for i in range(len(current)):
                                print(current[i])
                            print("--------------------------------------------------------------------------------------------"
                            +'\n')
                            inicio=inicio.next
                            con+=1
                        endt=time.perf_counter()
                        all_tests.append(endt-startt)
                        ntests-=1
                    time_passed=0
                    for w in range(len(all_tests)):
                        time_passed+=all_tests[w]
                    print(time_passed)
                    time_passed/=len(all_tests)
                    print(time_passed)
                else:
                    break

        

        

    #print(response1.json())
    #print(response2.json())
    #print(response3.json())