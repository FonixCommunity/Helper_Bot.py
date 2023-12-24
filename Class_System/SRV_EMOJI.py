
emoji1 = "<a:9410pinkarrow:1144772451973218314>" # Pink Arrow
emoji2 = "<:8580adminbadgedarkblue:1163619476131029083>" # Devloper Badge
emoji3 = "<:7721botbadge:1163619463774601347>" # Bot Badge
emoji4 = "<:7253staffbadge:1163619459232169985>" # Staff Badge
emoji5 = "<:1763botdeveloperbadge:1144773439043944562>" # Bot Icon
emoji6 = "<:4739stafficonpurple:1144773322337423531>" # Staff Icon Purple
emoji7 = "<a:6186developerbot:1062384688146169947>" # Developer Icon
emoji8 = "<:PL:1062372330283745320>" # Arrow Red
emoji9 = "<a:engrenagesslider:1062504692418105427>" # Engrenagesslider
emoji10 = "<a:WeeWoo:1007701512031572088>" # Alarm
emoji11 = "<:5736_thinkingkurapika:1163620071034335333>" # Waiting
emoji12 = "<:8391ownerbadge:1144773484891865268>" # Owner Badge
emoji13 = "<:7045managerbadge:1144773462402023586>" # Manager Badge
emoji14 = "<a:3416catspin:1144773864153432164>" # Cat Spin
emoji15 = "<a:7781meongcute:1163619316193824788>" # Cute Cat

class Emojis_Server :
    def __init__(self, 
                 emoji1= emoji1, 
                 emoji2= emoji2, 
                 emoji3= emoji3, 
                 emoji4= emoji4, 
                 emoji5= emoji5, 
                 emoji6= emoji6, 
                 emoji7= emoji7, 
                 emoji8= emoji8, 
                 emoji9= emoji9, 
                 emoji10= emoji10, 
                 emoji11= emoji11, 
                 emoji12= emoji12,
                 emoji13= emoji13,
                 emoji14= emoji14,
                 emoji15= emoji15,
                 visibility: tuple = False):
        
        if visibility == True :
            self.Pink_Arrow = emoji1
            self.Dev_Badge = emoji2
            self.Bot_Badge = emoji3
            self.Staff_Badge = emoji4
            self.Bot_Icon = emoji5
            self.Staff_Icon = emoji6
            self.Dev_Icon = emoji7
            self.Red_Arrow = emoji8
            self.Engrenage = emoji9
            self.Alarm = emoji10
            self.Waiting = emoji11
            self.Owner_Badge = emoji12
            self.Manager_Badge = emoji13
            self.Cat_Spin = emoji14
            self.Cute_Cat = emoji15
        else :
            nul = "￼"
            self.Pink_Arrow = nul
            self.Dev_Badge = nul
            self.Bot_Badge = nul
            self.Staff_Badge = nul
            self.Bot_Icon = nul
            self.Staff_Icon = nul
            self.Dev_Icon = nul
            self.Red_Arrow = nul
            self.Engrenage = nul
            self.Alarm = nul
            self.Waiting = nul
            self.Owner_Badge = nul 
            self.Manager_Badge = nul
            self.Cat_Spin = nul
            self.Cute_Cat =  nul
