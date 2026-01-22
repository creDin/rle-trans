#This is the core game code


image title card = "images/titleimage.png"
image NightMask = "images/nightmask.png"

image Crossroads_E = "images/Crossroads_Evening.jpg"
image Crossroads_N = "images/Crossroads_Night.jpg"
image Crossroads_D = "images/Crossroads_Day.jpg"

image UI_Backpack = "images/UI_Backpack_idle.png"
image UI_Dildo = "images/UI_Dildo.png"
image UI_VibA = "images/UI_VibA.png"
image UI_VibB = "images/UI_VibB.png"
image UI_Tongue = "images/UI_Tongue.png"
image UI_Finger = "images/UI_Finger.png"
image UI_Hand = "images/UI_Hand.png"
image UI_GirlFinger = "images/UI_GirlFinger.png"
image UI_GirlHand = "images/UI_GirlHand.png"
#image UI_PartnerFinger:
#    ConditionSwitch(
#            #hair back
#            "Partner == StormX", "images/UI_GirlFingerS.png",
#            "True", "images/UI_GirlFinger.png"
#            )
image UI_PartnerHand:
    ConditionSwitch(
            #hair back
            "Partner == StormX", "images/UI_GirlHandS.png",
            "True", "images/UI_GirlHand.png"
            )



image blackscreen:
    Solid("#000000")
    on show:
        alpha 1.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0
#rkeljsvg
define ch_r = Character('[RogueX.Name]', color="#85bb65", image = "arrow", show_two_window=True)
define ch_p = Character('[Player.Name]', color="#87CEEB", show_two_window=True)
define ch_x = Character('Профессор Икс', color="#a09400", image = "arrow", show_two_window=True)
define ch_k = Character('[KittyX.Name]', color="#F5A9D0", image = "arrow", show_two_window=True)
define ch_e = Character('[EmmaX.Name]', color="#98bee7", image = "arrow", show_two_window=True)
define ch_mc = Character('Др. МакКой', color="#1033b2", image = "arrow", show_two_window=True)
define ch_l = Character('[LauraX.Name]', color="#d8b600", image = "arrow", show_two_window=True)
define ch_j = Character('[JeanX.Name]', color="#b2d950", image = "arrow", show_two_window=True)
define ch_s = Character('[StormX.Name]', color="#b2d950", image = "arrow", show_two_window=True)
define ch_v = Character('[JubesX.Name]', color="#b2d950", image = "arrow", show_two_window=True) #fix, color change
define ch_u = Character('???', color="#85bb65", image = "arrow", show_two_window=True)
define ch_n = Character('Н', image = "arrow", show_two_window=True) #non-character, uses Ch_Focus #rmoved color, test that. . .
define ch_g = Character('[GwenX.Name]', color="#F08080", image = "arrowG", show_two_window=True,background=Frame("images/WordballoonG.png",50,50))
define ch_b = Character('[BetsyX.Name]', color="#4c2ac0", image = "arrow", show_two_window=True)
define ch_d = Character('[DoreenX.Name]', color="#ca9648", image = "arrow", show_two_window=True)
define ch_w = Character('[WandaX.Name]', color="#b30000", image = "arrow", show_two_window=True) #fix, color change
define ch_danger = Character('Комната Опасности:', color="#1033b2",what_color="#1033b2",what_font="dungeon.ttf",show_two_window=False)
#define e = Character("Eileen", what_color="#c8ffc8") #this sets the chat text color, handy


label splashscreen:
    if not config.developer:
        scene black onlayer backdrop
        with Pause(1)

        show image "images/Onirating.jpg"
        show text "Данная игра предназначена для лиц старше 18 лет." with dissolve
        with Pause(2)

        hide text with dissolve
        with Pause(1)

    return


init -1:
#World Stats
    default SaveVersion = 1640
    default Day = 1
    default Cheat = 0
    default Round = 100                 #Tracks time within a turn
    default Time_Options = ["Morning", "Afternoon", "Evening", "Night"]
    default Time_Count = 2
    default Time_Options_Rus = ["Утро", "Полдень", "Вечер", "Ночь"]
    default Current_Time_Rus = Time_Options_Rus[(Time_Count)]
    default Current_Time = Time_Options[(Time_Count)]
    default Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    default Weekday = 6
    default DayofWeek = Week[Weekday]
    default bg_current = "bg study"
    define Ch_Focus = 0
    default UI_Focus = 0
    default Party = []
    default TotalGirls = []
    default ActiveGirls = []
    default TotalSEXP = 0               #tallies the total combined SEXP daily
    default PersonalRooms = ["bg player"] #,"bg rogue","bg kitty","bg emma","bg laura"]
    default Taboo = 0
    default Rules = []
    default Digits = []
    default Keys = []
    default Line = 0
    default TempLine = 0
    default PassLine = 0                #used by AnyLine to pass lines around
    default Situation = 0               #Whether Auto/Shift
    default MultiAction = 1             #0 if the action cannot continue, 1 if it can
    default Target = 0                  #target of certain actions
    default Trigger = 0                 #Mainhand
    default Trigger2 = 0                #Offhand
    default Trigger3 = 0                #Girl's offhand
    default Trigger4 = 0                #this is the 4th sexual act performed by the second girl
    default Trigger5 = 0                #this is the 5th sexual act performed by the second girl if masturbating
    default ThreeCount = 100            #This is a timer for changing sexual positions on auto
#    default Adjacent = []              #this is the girl you're sitting next to in class
    default Nearby = []                 #this tracks girls in the same room, but distant from you
    default Present = []                #This list tracks which girls are in this scene
    default Shop_Inventory = []         #These are updated with books available for purchase       ["DL","DL","DL","DL","G","G","G","G","G","A","A","A","A"]
    default Inventory_Count = 0         #used in screens to keep track of inventory
    default StackDepth = 0
#    default LesFlag = 0                #This is triggered if a lesbian action is occurring
    default Partner = 0                 #this is the second character involved in a sex act, make sure to set Partner to 0 after each sex act
#    default Lead = 0
    default Events = []
    default Event_Queue = [0,0]  #girl chosen, event chosen
    default JumpQueue = []              #girl chosen for the Jumped event this time cycle
    default Addict_Queue = 0            #girl chosen for the Addict event this time cycle
    default LesQueue = []               #girl chosen as lead in a lesbian event this cycle
    default ShareQueue = []             #girls chosen to send you a message about whether they will join you
    default PunishmentX = 0             #countdown on your punishment
    default Tempmod = 0
    default Approval = 0                #for approval checks
    default Count = 0                   #For within an event
    default Count2 = 0                  #For between several events
    default CountStore = 0              #Stores values for after an event ends
    default Cnt = 0                     #a mini Count variable for discrete operations
    default Stealth = 0                 #How careful you're being
    default Speed = 0                   #pace of sex acts
    default Achievements = []
    default Options = []
    default Vibration = 0
    default Psychic = 0                 #this is an animation toggle for psychic sex. hand/blow/tit/pussy/ass
    default ShowFeet = 0
    default GhostTail = 0
    default RTR_Toggle = 1              #sets whether game asks if you want to return to your room when a girl asks you to
#    default UI_Girl = "Rogue"           #girl used in UI elements
    default TravelMode = 0              #used for wandering around, if 0, you use the worldmap
    default StageFarLeft = 150          #these are values for location points on the screen
    default StageLeft = 350
    default StageCenter = 550           #This is the default position for the lead
    define StageRight = 715            #This is the default position for second girl
    default StageFarRight = 900         #these are values for location points on the screen
    default OffStage = 1400         #these are values for location points on the screen
    default HolderCount = 1             #Used by the popup numbers
    default AlphaCock = 1             #the Alpha of the cock
    default CleanUp = 0                 #whether they will auto-clean you after sex
    default CleanUpDefault = 0          #whether they will auto-clean themselves after sex
#Xavier Sprite Variables
    default X_Brows = "happy"
    default X_Mouth = "happy"
    default X_Eyes = "happy"
    default X_Psychic = 0
    default X_Emote = "happy"
    default XSpriteLoc = StageCenter
    default GwenName = "????"
    default Load_Options = []
    default PlotBreak = 0       #When this is active, prevents new girls from appearing until deactivated.
    default Facing = 0 #manages whether doggy style looks to side or not

    #feminine
    default Terms0 = {'he':'she','him':'her','his':'her','man':'girl','men':'girls','guy':'gal','fella':'gal',
                'young man':'young lady','gentleman':'lady','gentlemanly':'ladylike','player':'slut',  'dude':'babe','mister':'miss',
                'sir':'ma\'am','master':'mistress','boy':'girl','daddy':'momma','bro':'babe','dick':'bitch'}
    #masculine
    default Terms1 = {'he':'he','him':'him','his':'his','man':'man','men':'men','guy':'guy','fella':'fella',
                'young man':'young man','gentleman':'gentleman','gentlemanly':'gentlemanly','player':'player', 'dude':'dude','mister':'mister',
                'sir':'sir','master':'master','boy':'boy','daddy':'daddy','bro':'bro','dick':'dick'}
    #neutral
    default Terms2 = {'he':'they','him':'them','his':'their','man':'person','men':'people','guy':'guy','fella':'folk',
                'young man':'young person','gentleman':'gentleperson','gentlemanly':'dignified','player':'player', 'dude':'dude','mister':'mix',
                'sir':'sir','master':'master','boy':'dear ','daddy':'daddy','bro':'dude','dick':'dick'}
    #Pussy
    default Loadout0 = {'spunk':'wetness', 'jiz':'fluids',' jiz':' pussy juice','cum':'juices','milk':'juice','semen':'secretions','you jiz':'you gush','eat':'drink','hungry':'thirsty',
                'suck':'lick','dick':'cunt','cock':'pussy','your cock':'your rubber cock','shaft':'slit','rigid':'rubber','balls':'mound',
                'handy':'fingering','handjob':'fingering','a blowjob':'you lick my pussy','sucking on':'licking at'}
    #Dick
    default Loadout1 = {'spunk':'spunk', 'jiz':'jiz',' jiz':' jiz','cum':'cum','milk':'milk','semen':'semen','you jiz':'you jiz','eat':'eat','hungry':'hungry',
                'suck':'suck','dick':'dick','cock':'cock','your cock':'your cock','shaft':'slit','rigid':'rigid','balls':'balls',
                'handy':'handy','handy':'handy','a blowjob':'a blowjob','sucking on':'sucking on'}

    default Terms = Terms1
    default Loadout = Loadout1


# Official game start  ////////////////////////////////////////////////////////////////////
label start:
    # Intitializes classes
    #$ import copy
    $ Player = PlayerClass()
    $ RogueX = GirlClass("Rogue",500,0,0,10)
    $ KittyX = GirlClass("Kitty",400,100,0,10)
    $ EmmaX = GirlClass("Emma",300,0,200,15)
    $ LauraX = GirlClass("Laura",400,0,200,10)
    $ JeanX = GirlClass("Jean",0,0,1000,10)
    $ StormX = GirlClass("Storm",500,0,100,10)
    $ JubesX = GirlClass("Jubes",500,50,50,10)
    $ GwenX = GirlClass("Gwen",400,100,100,10)
#    $ GwenlinX = GirlClass("Gwenlin",400,100,100,10)
    $ BetsyX = GirlClass("Betsy",400,100,100,10)
    $ DoreenX = GirlClass("Doreen",600,0,0,10)
    $ WandaX = GirlClass("Wanda",300,0,200,10)

    # Modification mode
    # -----------------
    call XmodMainVariables
    # -----------------

    $ RogueX.Introduction()
    $ KittyX.Introduction()
    $ EmmaX.Introduction()
    $ LauraX.Introduction()
    $ JeanX.Introduction()
    $ StormX.Introduction()
    $ JubesX.Introduction()
    $ GwenX.Introduction()
    $ BetsyX.Introduction()
    $ DoreenX.Introduction()
    $ WandaX.Introduction()

#    call Jubilee_Bootup

    $ RogueX.OutfitChange(6,Changed=1)
    $ KittyX.OutfitChange(6,Changed=1)
    $ EmmaX.OutfitChange(6,Changed=1)
    $ LauraX.OutfitChange(6,Changed=1)
    $ JeanX.OutfitChange(6,Changed=1)
    $ StormX.OutfitChange(6,Changed=1)
    $ JubesX.OutfitChange(6,Changed=1)
    $ GwenX.OutfitChange(6,Changed=1)
    $ BetsyX.OutfitChange(6,Changed=1)
    $ DoreenX.OutfitChange(6,Changed=1)
    $ WandaX.OutfitChange(6,Changed=1)


    $ Ch_Focus = RogueX
    $ UI_Focus = RogueX
    show screen Status_Screen
    show screen Inventorybutton

    if config.developer:
        jump Dev_Room
    jump Prologue


# After loading, this runs ////////////////////////////////////////////////////////////////
label after_load:
label VersionNumber:
    $ SaveVersion = 0 if "SaveVersion" not in globals().keys() else SaveVersion
#    if SaveVersion == 976: #error correction, remove this eventually
#            $ SaveVersion = 957

    # Modification mode
    # -----------------
    call XmodMainVariables
    # -----------------

    if SaveVersion >= 990:
        if SaveVersion < 1641:
            if SaveVersion <= 990:
                if "RogueX" in globals().keys():
                            if RogueX.Hair == "wet":
                                    $ RogueX.Hair = "evo"
                            if RogueX.Casual1[1] == "gloved":
                                    $ RogueX.Casual1[1] == "gloves"
                            if RogueX.Casual2[1] == "gloved":
                                    $ RogueX.Casual2[1] == "gloves"
                            if RogueX.Gym[1] == "gloved":
                                    $ RogueX.Gym[1] == "gloves"
                            if RogueX.Arms == "gloved":
                                    $ RogueX.Arms = "gloves"
                            if RogueX in TotalGirls:
                                    while RogueX in TotalGirls:
                                        $ TotalGirls.remove(RogueX)
                                    $ TotalGirls.append(RogueX)
                            if RogueX in ActiveGirls:
                                    while RogueX in ActiveGirls:
                                        $ ActiveGirls.remove(RogueX)
                                    $ ActiveGirls.append(RogueX)
                            if not hasattr(RogueX,'Cheated'):
                                    $ setattr(RogueX,"Cheated",0)
                            if RogueX in Player.Harem:
                                    $ RogueX.AddWord(1,0,0,"dating",0)
                if "KittyX" in globals().keys():
                            if KittyX in TotalGirls:
                                    while KittyX in TotalGirls:
                                        $ TotalGirls.remove(KittyX)
                                    $ TotalGirls.append(KittyX)
                            if KittyX in ActiveGirls:
                                    while KittyX in ActiveGirls:
                                        $ ActiveGirls.remove(KittyX)
                                    $ ActiveGirls.append(KittyX)
                            if KittyX.Home in PersonalRooms:
                                    while KittyX.Home in PersonalRooms:
                                        $ PersonalRooms.remove(KittyX.Home)
                                    $ PersonalRooms.append(KittyX.Home)
                            if not hasattr(KittyX,'Cheated'):
                                    $ setattr(KittyX,"Cheated",0)
                            if KittyX in Player.Harem:
                                    $ KittyX.AddWord(1,0,0,"dating",0)
                if "EmmaX" in globals().keys():
                            if EmmaX in TotalGirls:
                                    while EmmaX in TotalGirls:
                                        $ TotalGirls.remove(EmmaX)
                                    $ TotalGirls.append(EmmaX)
                            if EmmaX in ActiveGirls:
                                    while EmmaX in ActiveGirls:
                                        $ ActiveGirls.remove(EmmaX)
                                    $ ActiveGirls.append(EmmaX)
                            if EmmaX.Home in PersonalRooms:
                                    while EmmaX.Home in PersonalRooms:
                                        $ PersonalRooms.remove(EmmaX.Home)
                                    $ PersonalRooms.append(EmmaX.Home)
                            if not hasattr(EmmaX,'Cheated'):
                                    $ setattr(EmmaX,"Cheated",0)
                            if EmmaX in Player.Harem:
                                    $ EmmaX.AddWord(1,0,0,"dating",0)
                if "LauraX" in globals().keys():
                            if LauraX in TotalGirls:
                                    while LauraX in TotalGirls:
                                        $ TotalGirls.remove(LauraX)
                                    $ TotalGirls.append(LauraX)
                            if LauraX in ActiveGirls:
                                    while LauraX in ActiveGirls:
                                        $ ActiveGirls.remove(LauraX)
                                    $ ActiveGirls.append(LauraX)
                            if LauraX.Home in PersonalRooms:
                                    while LauraX.Home in PersonalRooms:
                                        $ PersonalRooms.remove(LauraX.Home)
                                    $ PersonalRooms.append(LauraX.Home)
                            if not hasattr(LauraX,'Cheated'):
                                    $ setattr(LauraX,"Cheated",0)
                            if LauraX in Player.Harem:
                                    $ LauraX.AddWord(1,0,0,"dating",0)
                $ Player.StatPoints = 0 if Player.StatPoints < 0 else Player.StatPoints
                if "Emma stockings and garterbelt" in Player.Inventory:
                        $ Player.Inventory.remove("Emma stockings and garterbelt")
                        $ Player.Inventory.append("stockings and garterbelt")
                while 0 in Party:
                        $ Party.remove(0)
                hide Laura
                $ SaveVersion = 990
                #End 0.990 updates
            if SaveVersion < 992:
                #changes for version 991, adds Jean to the game
                if "JeanX" not in globals().keys():
                        $ JeanX = GirlClass("Jean",0,0,1000,10)
                        $ JeanX.Introduction()
                if "met" in JeanX.History and JeanX not in ActiveGirls: #remove once stable
                        $ ActiveGirls.Append(JeanX)

                if "RogueX" in globals().keys() and "met" in RogueX.History:
                            if RogueX not in TotalGirls:
                                    $ TotalGirls.append(RogueX)
                if "KittyX" in globals().keys() and "met" in KittyX.History:
                            if KittyX not in TotalGirls:
                                    $ TotalGirls.append(KittyX)
                            if KittyX.Pet == KittyX:
                                $ KittyX.Pet = "Kitty"
                if "EmmaX" in globals().keys() and "met" in EmmaX.History:
                            if EmmaX not in TotalGirls:
                                    $ TotalGirls.append(EmmaX)
                if "LauraX" in globals().keys() and "met" in LauraX.History:
                            if LauraX not in TotalGirls:
                                    $ TotalGirls.append(LauraX)
                            if LauraX.Pet == LauraX:
                                    $ LauraX.Pet = "Laura"
                            if LauraX.Casual2[4] == "jacket":
                                    $ LauraX.Casual1 = [2,"wrists","leather pants",0,"leash choker","leather bra","leather panties",0,0,0,0]
                                    $ LauraX.Casual2 = [2,0,"skirt","jacket","leash choker","corset","leather panties",0,0,0,0]
                if "JeanX" in globals().keys() and "met" in JeanX.History:
                            if JeanX not in TotalGirls:
                                    $ TotalGirls.append(JeanX)
                            if JeanX.Pet == JeanX:
                                $ JeanX.Pet = "Jean"
                            if "exhibitionist" in JeanX.Traits and "nowhammy" not in JeanX.Traits:
                                    $ JeanX.Traits.remove("exhibitionist")
                $ SaveVersion = 992
                #End 0.992 updates

            if SaveVersion < 993:
                if "RogueX" in globals().keys():
                            if not hasattr(RogueX,'Pose'):
                                    $ setattr(RogueX,"Pose",0)
                if "KittyX" in globals().keys():
                            if not hasattr(KittyX,'Pose'):
                                    $ setattr(KittyX,"Pose",0)
                if "EmmaX" in globals().keys():
                            if not hasattr(EmmaX,'Pose'):
                                    $ setattr(EmmaX,"Pose",0)
                if "LauraX" in globals().keys():
                            if not hasattr(LauraX,'Pose'):
                                    $ setattr(LauraX,"Pose",0)
                if "JeanX" in globals().keys():
                            if not hasattr(JeanX,'Pose'):
                                    $ setattr(JeanX,"Pose",0)
                #End 0.993 updates

            if SaveVersion < 994:
                if "StormX" not in globals().keys():
                        $ StormX = GirlClass("Storm",500,0,100,10)
                        $ StormX.Introduction()
                python:
                    for LO in TotalGirls:
                        while "bf" in LO.Traits:
                                LO.Traits.remove("bf")
                        while "lov" in LO.Traits:
                                LO.Traits.remove("lov")
                        while "sb" in LO.Traits:
                                LO.Traits.remove("sb")
                        while "mstr" in LO.Traits:
                                LO.Traits.remove("mstr")
                        while "sxfrnd" in LO.Traits:
                                LO.Traits.remove("sxfrnd")
                        while "fkbd" in LO.Traits:
                                LO.Traits.remove("fkbd")
                        while "share" in LO.Traits:
                                LO.Traits.remove("share")
                        while "adfix" in LO.Traits:
                                LO.Traits.remove("adfix")
                        LO.DrainWord("asked meet")
                $ SaveVersion = 993
                #End 0.994 updates
            if SaveVersion < 995:
                python:
                    for LO in TotalGirls:
                        if "dating" in LO.Traits:
                            if LO not in Player.Harem:
                                    Player.Harem.append(LO) #adds girl to Harem if dating
                            LO.DrainWord("dating",0,0,1) #removes "dating" from traits
                $ SaveVersion = 995

            if SaveVersion < 996:
                $ Load_Options = TotalGirls[:]
                python:
                    for LO in Load_Options:
                        #removes girls with "poly themselves" in traits
                        if "poly " + LO.Tag in LO.Traits:
                                LO.Traits.remove("poly " + LO.Tag)
                        while TotalGirls.count(LO) >= 2: #removes any extra copies that might crop up
                                TotalGirls.remove(LO)
                        while ActiveGirls.count(LO) >= 2:
                                ActiveGirls.remove(LO)
                        if not hasattr(LO,'Costume'):
                                setattr(LO,"Costume",[])
                $ RogueX.Costume = [2,"gloves","skirt",0,0,"tube top","black panties","sweater","cosplay",0,0]
                $ KittyX.Costume = [2,0,"dress","jacket","flower necklace","dress","lace panties",0,0,0,0]
                $ EmmaX.Costume =  [2,"gloves","dress","dress","choker",0,"lace panties",0,"hat","stockings and garterbelt",0]
                $ LauraX.Costume = [2,"gloves","other skirt",0,0,"white tank","black panties","suspenders",0,"black stockings",0]
                $ JeanX.Costume =  [2,0,"shorts","yellow shirt",0,"green bra","green panties","suspenders","pony",0,0]
                $ StormX.Costume = [2,0,0,0,"ring necklace","cos bra","cos panties","rings","short",0,0]
                $ SaveVersion = 996
            if SaveVersion < 998:
                python:
                    for LO in TotalGirls:
                        #removes girls with "poly themselves" in traits
                        LO.Pose = "breasts" if LO.Pose == "breast" else LO.Pose
                if "partysolved" in LauraX.History:
                        $ LauraX.History.remove("partysolved")
                        $ LauraX.AddWord(1,0,0,0,"partyfoul") #adds "partyfoul" to History
                if "JubesX" not in globals().keys():
                        $ JubesX = GirlClass("Jubes",500,50,50,10)
                        $ JubesX.Introduction()
                if "bg teacher" in JubesX.Schedule:
                        $ JubesX.Schedule = [["bg jubes","bg dangerroom","bg dangerroom","bg jubes"],
                                        ["bg classroom","bg classroom","bg jubes","bg jubes"],
                                        ["bg jubes","bg dangerroom","bg dangerroom","bg jubes"],
                                        ["bg dangerroom","bg dangerroom","bg jubes","bg jubes"],
                                        ["bg pool","bg campus","bg campus","bg jubes"],
                                        ["bg jubes","bg campus","bg jubes","bg pool"],
                                        ["bg jubes","bg campus","bg jubes","bg pool"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]
                $ JubesX.Blow = 0
                $ JubesX.Hand = 0
                $ SaveVersion = 998
            if SaveVersion < 999:
                if "GwenX" not in globals().keys():
                        $ GwenX = GirlClass("Gwen",400,100,100,10)
                        $ GwenX.Introduction()
                if "sexfriend" in JeanX.Petnames:
                        $ JeanX.Petnames.remove("sexfriend")
                        $ JeanX.Petnames.append("sex friend")
                $ JubesX.Costume = [2,0,0,"dress","choker","lace bra","lace panties",0,"short","stockings and garterbelt",0]
                $ SaveVersion = 999

            if SaveVersion < 1000:
                if "GwenX" not in globals().keys():
                        $ GwenX = GirlClass("Gwen",400,100,100,10)
                        $ GwenX.Introduction()
                if not hasattr(Player,'XName'):
                        $ setattr(Player,"XName",0) #adds "XName" attribute to Player
                if not hasattr(Player,'Male'):
                        $ setattr(Player,"Male",1) #adds "Male" attribute to Player
                python:
                    for LO in TotalGirls:
                        if not hasattr(LO,'Finger'): #adds Fingering stat
                                setattr(LO,"Finger",0)
                        if not hasattr(LO,'CUN'): #adds cunnilingus stat
                                setattr(LO,"CUN",0)
                        if not hasattr(LO,'SeenPuss'): #adds seenpuss stat
                                setattr(LO,"SeenPuss",0)
                        if not hasattr(LO,'Red'): #adds red butt stat
                                setattr(LO,"Red",0)
                        if not hasattr(LO,'Plugged'): #adds Plugged stat
                                setattr(LO,"Plugged",0)
                $ Time_Options[1] = "Afternoon"
                $ Current_Time = "Afternoon" if Current_Time == "Midday" else Current_Time
                $ SaveVersion = 1000

            if SaveVersion < 1100:
                if "GwenX" not in globals().keys():
                        $ GwenX = GirlClass("Gwen",400,100,100,10)
                        $ GwenX.Introduction()

                #loads in new "terms"
                $ Terms0["him"] = "her"
                $ Terms1["him"] = "him"
                $ Terms2["him"] = "them"
                $ Terms0["dude"] = "babe"
                $ Terms1["dude"] = "dude"
                $ Terms2["dude"] = "dude"
                $ Terms0["mister"] = "miss"
                $ Terms1["mister"] = "mister"
                $ Terms2["mister"] = "mix"

                #Updates player's terms list to include new ones
                if Terms["he"] == "she":
                        $ Terms = Terms0
                elif Terms["he"] == "they":
                        $ Terms = Terms2
                else:
                        $ Terms = Terms1

                if JubesX.Petname == "bro" or JubesX.Petname == "бро" or JubesX.Petname == "сис":
                        $ JubesX.Petname = Terms["bro"]
                if "knee stockings" in KittyX.Inventory:
                        $ KittyX.Inventory.remove("knee stockings")
                        $ KittyX.Inventory.append("knee")
                python:
                    for LO in TotalGirls:
                        #this applies new outfit boot and hat options to existing outfits.
                        if len(LO.Costume) >= 13:
                            pass
                        else:
                            while len(LO.Casual1) < 13:
                                LO.Casual1.append(0)
                            while len(LO.Casual2) < 13:
                                LO.Casual2.append(0)
                            while len(LO.Custom1) < 13:
                                LO.Custom1.append(0)
                            while len(LO.Custom2) < 13:
                                LO.Custom2.append(0)
                            while len(LO.Custom3) < 13:
                                LO.Custom3.append(0)
                            while len(LO.TempClothes) < 13:
                                LO.TempClothes.append(0)
                            while len(LO.Gym) < 13:
                                LO.Gym.append(0)
                            while len(LO.Sleepwear) < 13:
                                LO.Sleepwear.append(0)
                            while len(LO.Swim) < 13:
                                LO.Swim.append(0)
                            while len(LO.Costume) < 13:
                                LO.Costume.append(0)
                        LO.Hat = 0
                        LO.Boots = 0
                if EmmaX.Hair == "hat":
                        $ EmmaX.Hair = "long"
                        $ EmmaX.Hat = "sun hat"
                if EmmaX.Hair == "hat wet":
                        $ EmmaX.Hair = "wet"
                        $ EmmaX.Hat = "sun hat"
                if EmmaX.Acc == "thigh boots":
                        $ EmmaX.Boots = "thigh boots"
                        $ EmmaX.Acc = 0

                $ EmmaX.Costume =  [2,"gloves","dress","dress","choker",0,"lace panties",0,0,"stockings and garterbelt",0,0,"sun hat"]

                #gives Rogue shoes
                $ RogueX.Casual1[11] = "boots"
                $ RogueX.Casual2[11] = "sneaks"
                $ RogueX.Gym[11] = "sneaks"
                $ RogueX.Costume[11] = "boots"

                $ ch_g = Character('[GwenX.Name]', color="#F08080", image = "arrowG", show_two_window=True,background=Frame("images/WordballoonG.png",50,50))
                $ SaveVersion = 1100
            if SaveVersion < 1101:
                if "GwenX" not in globals().keys():
                        $ GwenX = GirlClass("Gwen",400,100,100,10)
                        $ GwenX.Introduction()
                $ SaveVersion = 1101
            if SaveVersion < 1102:
                python:
                    for LO in TotalGirls:
                        if not hasattr(LO,'Hat'):
                                setattr(LO,"Hat",0)
                        if not hasattr(LO,'Boots'):
                                setattr(LO,"Boots",0)
                $ SaveVersion = 1102
            if SaveVersion < 1103:
                if GwenX.Swim[2] == "suit":
                    $ GwenX.Swim[2] = 0
                $ SaveVersion = 1103
        if SaveVersion < 1300:

            $ KittyX.Casual1[11] = "sandals"
            $ KittyX.Casual2[11] = "sandals"
            $ KittyX.Gym[11] = "sandals"
            $ KittyX.Costume[11] = "sandals"

            $ EmmaX.Casual1[11] = "shoes"
            $ EmmaX.Casual2[11] = "thigh boots"
            $ EmmaX.Gym[11] = "shoes"
            $ EmmaX.Costume[11] = "shoes"

            $ LauraX.Casual1[11] = "boots"
            $ LauraX.Casual2[11] = "boots"
            $ LauraX.Gym[11] = "boots"
            $ LauraX.Costume[11] = "boots"

            $ JeanX.Casual1[11] = "sandals"
            $ JeanX.Casual2[11] = "sandals"
            $ JeanX.Gym[11] = "sandals"
            $ JeanX.Costume[11] = "sandals"

            $ StormX.Casual1[11] = "sandals"
            $ StormX.Casual2[11] = "boots"
            $ StormX.Gym[11] = "boots"
            $ StormX.Costume[11] = "rings"

            $ JubesX.Casual1[11] = "sneaks"
            $ JubesX.Casual2[11] = "sneaks"
            $ JubesX.Gym[11] = "sneaks"
            $ JubesX.Costume[11] = "sneaks"
            python:
                for LO in TotalGirls:
                    if not hasattr(LO,'Facing'):
                            setattr(LO,"Facing",0)
            $ SaveVersion = 1300

        if SaveVersion < 1301:
            $ Loadout0["balls"] = "mound"
            $ Loadout1["balls"] = "balls"
            if Loadout["cock"] == "cock":
                    $ Loadout["balls"] = "balls"
            else:
                    $ Loadout["balls"] = "mound"
            $ SaveVersion = 1301

        if SaveVersion < 1302:
            if "White Queen" in EmmaX.Names and "White Queen" not in EmmaX.Petnames:
                    $ EmmaX.Petnames.append("White Queen")
            $ SaveVersion = 1302

        if SaveVersion < 1400:
            $ GwenX.Hair = "short" if GwenX.Hair == "long" else GwenX.Hair
            $ GwenX.Costume = [2,0,"cheer skirt","cheer top",0,0,"white panties",0,"pony","socks",0,"sneaks",0]
            $ SaveVersion = 1400

#        if SaveVersion < 1401:
#            if renpy.showing("PhoneSex"):
#                    hide PhoneSex
#                    if Girl is RogueX:
#                            show PhoneSex_Rogue zorder 150
#                    elif Girl is KittyX:
#                            show PhoneSex_Kitty zorder 150
#                    elif Girl is EmmaX:
#                            show PhoneSex_Emma zorder 150
#                    elif Girl is LauraX:
#                            show PhoneSex_Laura zorder 150
#                    elif Girl is JeanX:
#                            show PhoneSex_Jean zorder 150
#                    elif Girl is StormX:
#                            show PhoneSex_Storm zorder 150
#                    elif Girl is JubesX:
#                            show PhoneSex_Jubes zorder 150
#                    elif Girl is GwenX:
#                            show PhoneSex_Gwen zorder 150
#            $ SaveVersion = 1401

        if SaveVersion < 1500:
            if "BetsyX" not in globals().keys():
                    $ BetsyX = GirlClass("Betsy",400,100,100,10)
                    $ BetsyX.Introduction()
            if "DoreenX" not in globals().keys():
                    $ DoreenX = GirlClass("Doreen",400,100,100,10)
                    $ DoreenX.Introduction()

            $ ch_mc = Character('Дк. МакКой', color="#1033b2", image = "arrow", show_two_window=True)
            $ ch_b = Character('[BetsyX.Name]', color="#4c2ac0", image = "arrow", show_two_window=True)
            python:
                for LO in TotalGirls:
                    if not hasattr(LO,'Offhand'):
                            setattr(LO,"Offhand",0)
            $ SaveVersion = 1500
        if SaveVersion < 1501:
            if DoreenX.Tag == "Betsy":
                    $ DoreenX = GirlClass("Doreen",400,100,100,10)
                    $ DoreenX.Introduction()
            $ SaveVersion = 1501
        if SaveVersion < 1502:
            while len(TotalGirls) >= 10:
                    "[TotalGirls[9].Tag]"
                    $ TotalGirls.remove(TotalGirls[9])
            $ DoreenX = GirlClass("Doreen",400,100,100,10)
            $ DoreenX.Introduction()
            $ SaveVersion = 1502
        if SaveVersion < 1503:
            if "metall" in GwenX.History:
                    $ GwenX.History.remove("metall")
            if "Betsy" not in GwenX.History:
                    $ GwenX.History.append("Betsy")
            $ SaveVersion = 1503

        if SaveVersion < 1504:
            $ DoreenX.Casual1 = [2,0,"shorts","tube top",0,"tan bra","tan panties","jacket",0,"pantyhose",0,"boots","headband"]
            $ DoreenX.Casual2 = [2,0,"skirt","tshirt",0,"tan bra","tan panties",0,0,"tights",0,"sneaks","headband"]
            $ DoreenX.Gym = [0,0,0,0,0,"sports bra","tan panties","jacket",0,"tights",0,"sneaks","headband"]
            $ DoreenX.Sleepwear = [0,0,0,"tshirt",0,0,"tan panties",0,0,"tights",0,0,0]
            $ DoreenX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
            $ DoreenX.Shame = 0
            $ SaveVersion = 1504
        if SaveVersion < 1510:
            $ DoreenX.Casual1 = [2,0,"shorts","tube top",0,"tan bra","tan panties","jacket",0,"pantyhose",0,"boots","headband"]
            $ DoreenX.Casual2 = [2,0,"skirt","tshirt",0,"tan bra","tan panties",0,0,"tights",0,"sneaks","headband"]
            $ DoreenX.Gym = [0,0,0,0,0,"sports bra","tan panties","jacket",0,"tights",0,"sneaks","headband"]
            $ DoreenX.Sleepwear = [0,0,0,"tshirt",0,0,"tan panties",0,0,"tights",0,0,0]
            $ DoreenX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
            $ DoreenX.Schedule = [["bg doreen","bg dangerroom","bg dangerroom","bg doreen"],
                            ["bg classroom","bg classroom","bg doreen","bg doreen"],
                            ["bg doreen","bg dangerroom","bg dangerroom","bg doreen"],
                            ["bg dangerroom","bg dangerroom","bg doreen","bg doreen"],
                            ["bg pool","bg campus","bg campus","bg doreen"],
                            ["bg doreen","bg campus","bg doreen","bg doreen"],
                            ["bg doreen","bg campus","bg doreen","bg doreen"],
                            ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]
            $ DoreenX.MassageChart = ["feet","feet","calves","thighs","hips","back","hips","ass","pussy","pussy"]
            $ DoreenX.Tail = 1
            if not Player.Name:
                $ DoreenX.Petname = "Чувиха"
            else:
                $ DoreenX.Petname = "Чувак"
            $ DoreenX.Petnames = ["Dude"]
            $ DoreenX.Pet = "Дорин"
            $ DoreenX.Pets = ["Doreen"]

            $ SaveVersion = 1510
        if SaveVersion < 1511:
            if "met" in DoreenX.History:
                    $ DoreenX.Name = "Дорин" if DoreenX.Name == "? ? ?" else DoreenX.Name
                    $ DoreenX.Name_rod = "Дорин" if DoreenX.Name == "? ? ?" else DoreenX.Name_rod
                    $ DoreenX.Name_dat = "Дорин" if DoreenX.Name == "? ? ?" else DoreenX.Name_dat
                    $ DoreenX.Name_vin = "Дорин" if DoreenX.Name == "? ? ?" else DoreenX.Name_vin
                    $ DoreenX.Name_tvo = "Дорин" if DoreenX.Name == "? ? ?" else DoreenX.Name_tvo
                    $ DoreenX.Name_pre = "Дорин" if DoreenX.Name == "? ? ?" else DoreenX.Name_pre
            if "boyfriend" in DoreenX.Petnames:
                    $ DoreenX.Petnames.remove("boyfriend")
            if "lover" in DoreenX.Petnames:
                    $ DoreenX.Petnames.remove("lover")
            if "sir" in DoreenX.Petnames:
                    $ DoreenX.Petnames.remove("sir")
            if "master" in DoreenX.Petnames:
                    $ DoreenX.Petnames.remove("master")
            if "daddy" in DoreenX.Petnames:
                    $ DoreenX.Petnames.remove("daddy")
            if "sexfriend" in DoreenX.Petnames:
                    $ DoreenX.Petnames.remove("sexfriend")
            if "fuckbuddy" in DoreenX.Petnames:
                    $ DoreenX.Petnames.remove("fuckbuddy")
            $ DoreenX.Event[5] = 0
            $ DoreenX.Event[6] = 0
            $ DoreenX.Event[7] = 0
            $ DoreenX.Event[8] = 0
            $ DoreenX.Event[9] = 0
            $ DoreenX.Event[10] = 0
            $ SaveVersion = 1511
#        if SaveVersion < 1520:
#            $ SaveVersion = 1520
        if SaveVersion < 1540:
            $ BetsyX.Costume = [2,0,"yoga pants","jacket",0,"sports bra","blue panties",0,"blonde",0,0,"sneaks",0]
            $ DoreenX.Costume = [2,0,"red skirt","sweater",0,"tan bra","tan panties",0,0,0,0,"sneaks","glasses"]
            $ SaveVersion = 1540

        if SaveVersion < 1600:
            $ DoreenX.Pet = "Doreen" if DoreenX.Pet == "Dorren" else DoreenX.Pet
            if "Doreen" not in GwenX.History:
                    $ GwenX.History.append("Doreen")

            if "WandaX" not in globals().keys():
                    $ WandaX = GirlClass("Wanda",300,0,200,10)
                    $ WandaX.Introduction()

            $ SaveVersion = 1600
        if SaveVersion < 1601:
            if "witch" in WandaX.History:
                    $ WandaX.History.remove("witch")
            $ WandaX.Chest = "red bra" if WandaX.Chest == "black bra" else WandaX.Chest
            $ WandaX.Casual1[5] = "red bra" if WandaX.Casual1[5] == "black bra" else WandaX.Casual1[5]
            $ WandaX.Gym[5] = "red bra" if WandaX.Gym[5] == "black bra" else WandaX.Gym[5]
            $ WandaX.Petnames = [Terms["bro"]] if WandaX.Petnames == Terms["bro"] else WandaX.Petnames
            $ SaveVersion = 1601
        if SaveVersion < 1602:
            if "met" in EmmaX.History:
                    $ EmmaX.AddWord(1,0,0,0,"idiot") #adds "word" to Recent
                    $ EmmaX.AddWord(1,0,0,0,"loser") #adds "word" to Recent
            $ SaveVersion = 1602
        if SaveVersion < 1610:
            $ WandaX.Inventory.append("pantyhose") if "pantyhose" not in WandaX.Inventory else WandaX.Inventory
            $ JeanX.LikeSStorm = 0
            $ JeanX.LikeSJubes = 0
            $ JeanX.LikeSGwen = 0
            $ JeanX.LikeSBetsy = 0
            $ JeanX.LikeSDoreen = 0
            $ JeanX.LikeSWanda = 0
            $ SaveVersion = 1610
        if SaveVersion < 1620:
            $ UI_Focus = RogueX
            $ SaveVersion = 1620
        if SaveVersion < 1621:
            if "69" in RogueX.History or "69" in KittyX.History or "69" in EmmaX.History or "69" in BetsyX.History or "69" in DoreenX.History:
                    $ Player.AddWord(1,0,0,0,"69")
            $ EmmaX.Hair = "long" if EmmaX.Hair == "wave" else EmmaX.Hair
            $ EmmaX.Hair = "long" if EmmaX.Hair == "wavy" else EmmaX.Hair
            $ SaveVersion = 1621
        if SaveVersion < 1630:
            $ SaveVersion = 1630
        if SaveVersion < 1640:
            $ StormX.Neck = "rings" if StormX.Neck == "ring necklace" else StormX.Neck
            $ StormX.Costume[4] = "rings" if StormX.Costume[4] == "ring necklace" else StormX.Costume[4]
            $ WandaX.Costume = [2,0,"skirt","purple top","scarf",0,"gray panties",0,"long",0,0,"boots","headband"]
            $ SaveVersion = 1640
        if SaveVersion < 1641:
            $ WandaX.Costume[11] = "boots" if WandaX.Costume[11] == "sneaks" else WandaX.Costume[11]
            python:
                for LO in TotalGirls:
                    if not hasattr(LO,'SC'):
                            setattr(LO,"SC",0)
            $ SaveVersion = 1641

        #this section should return players to their room if it would otherwise fail to load a save properly
        $ StackDepth = renpy.call_stack_depth()
        $ Stack = renpy.get_return_stack()
        #"[Stack]"
        while StackDepth > 0:
                $ StackCheck = Stack[StackDepth-1]
                if not renpy.has_label(StackCheck):
                        #"[StackCheck]"
                        "С этим сохранением могут возникнуть проблемы, поэтому вас закинет в комнату игрока."
                        "Необходимо правильно сохранять свой прогресс, если вы решаете сохраниться в середине сцены какого-либо персонажа, в будущем могут возникнуть проблемы с загрузкой такого сохранения."
                        "Попытайтесь сохраняться только в нейтральных ситуациях, дабы исключить возможные ошибки."
                        "Вы можете попытать счастья и загрузить сохранение и убедиться в его работе, будет ли загружено сохранение или нет - это другой вопрос, скорее всего, вас вернет в Главное меню."
                        menu:
                            "Вернуться в комнату игрока [[безопастно]":
                                    $ bg_current = "bg player"
                                    jump Misplaced
                            "Проверить работоспособность [[скорее всего, работать не будет]":
                                    return
                $ StackDepth -= 1

        return
        #remove this later               #remove this later               #remove this later               #remove this later
    else:

            $ renpy.scene("screens")    #removes old screens
            $ Player = PlayerClass()
            $ RogueX = GirlClass("Rogue",500,0,0,10)
            $ KittyX = GirlClass("Kitty",400,100,0,10)
            $ EmmaX = GirlClass("Emma",300,0,200,15)
            $ LauraX = GirlClass("Laura",400,0,200,10)
            $ JeanX = GirlClass("Jean",0,0,1000,10)
            $ StormX = GirlClass("Storm",500,0,100,10)

            $ RogueX.Introduction()
            $ KittyX.Introduction()
            $ EmmaX.Introduction()
            $ LauraX.Introduction()
            $ JeanX.Introduction()
            $ StormX.Introduction()

            $ Ch_Focus = RogueX
            show screen Status_Screen
            show screen Inventorybutton

            show blackscreen onlayer black
            if SaveVersion < 984:
                    "You are loading a save from a version earlier than 0.984."
                    "This will not work with this build, but please pick up a copy of version 0.984h."
                    "Then move to the player's room, alone, and make a save file there."
                    "This save file -should- be able to be opened in version 0.990 and beyond."
                    $ StackDepth = renpy.call_stack_depth() #Count = number of items in the call stack
                    while StackDepth > 1:
                        $ StackDepth -= 1
                        $ renpy.pop_call()
                    return
            "You are loading a save from a version earlier than 0.990."
            if bg_current != "bg player":
                    "Your save is not in the player's room, which might cause errors due to missing local variables."
                    "You might want to load this save in version 0.984h, and move to the player's room before saving."
            "If you continue, know that this save migration is still being tested and may cause new errors."
            "Let me know if there are any clothing options behaving differently than expected, and stats that seem out of place,"
            "Anything unusual. I would recommend playing from this save file only a short distance, and not just continuing forward indefinitely,"
            "until we're fairly certain that the migration process is fully functional. Be careful of where you save."
            "that said, it shouldn't cause any harm to try it. :D"
            hide blackscreen onlayer black
    call Failsafe                #fix                #fix                #fix                #fix
    return                #fix                #fix                #fix                #fix


return
