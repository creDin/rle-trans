init python:
    #import copy

    class PlayerClass(object):
        def __init__(self):
                self.Name = "Зеро"
                self.Semen = 2                  #available semen
                self.Semen_Max = 3              #amount it maxes out at
                self.Focus = 0                  #progress towards orgasm
                self.FocusX = 0                 #is the player trying not to orgasm
                self.XP = 0
                self.SEXP = 0                   #how much sex you've had overall
                self.StatPoints = 0
                self.XPgoal = 100
                self.Lvl = 1
                self.Rep = 600
                self.RecentActions = []
                self.DailyActions = []
                self.Traits = []
                self.History = []
                self.Harem = []                 #this is a list of all girls the player is currently dating
                self.Male = 1
                self.XName = 0                  #previous name if changed
            # Player Inventory Variables
                self.Income = 12                #how much you make each day
                self.Cash = 20
                self.Inventory = []
                #default Inventory_Count = 0    #check to see if this works on screens, if so, delete it
            # Player Sprite
                self.Sprite = 0
                self.Color = "green"
                self.Cock = "out"
                self.Spunk = 0
                self.Wet = 0

        def AddWord(self,Only=0,Recent=0,Daily=0,Trait=0,History=0):
                #applies variables to appropriate character stats
                # $ Player.AddWord(1,"angry",0,0,0)
                #if Only, then only apply it if it's not already there
                if (Recent and not Only) or (Recent and Recent not in self.RecentActions):
                        self.RecentActions.append(Recent)
                if (Daily and not Only) or (Daily and Daily not in self.DailyActions):
                        self.DailyActions.append(Daily)
                if (Trait and not Only) or (Trait and Trait not in self.Traits):
                        self.Traits.append(Trait)
                if (History and not Only) or (History and History not in self.History):
                        self.History.append(History)
                return

        def DrainWord(self, Word = "word", Recent = 1, Daily = 1, Traits=0):
                # to remove words from the daily/recent lists , ie call DrainWord("Rogue","sex",1,0)
                # $ Player.DrainWord("angry",0,1)
                if Recent and Word in self.RecentActions:
                    while Word in self.RecentActions:
                            self.RecentActions.remove(Word)
                if Daily and Word in self.DailyActions:
                    while Word in self.DailyActions:
                            self.DailyActions.remove(Word)
                if Traits and Word in self.Traits:
                    while Word in self.Traits:
                            self.Traits.remove(Word)
                return

        def Statup(self, Flavor=0, Check=100, Value=1, Greater=0, Type=0, Overflow=0, BStat=0, XPOS = 0.75):
                # $ Player.Statup("Focus", 90, 5)
                Type = getattr(self,Flavor)
                if Greater:
                        #this checks if it's greater or less than the intended value
                        #if it fails, the value is zeroed out, canceling the rest
                        if Type >= Check:
                            #If it passes the check, add Value to it
                            Type += Value
                        else:
                            #If not, don't add Value and set Value to 0
                            Value = 0
                else:
                        if Type <= Check:
                            Type += Value
                        else:
                            Value = 0

                if Value:
                        Color = "#FFFFFF"
                        # show pop-up
                        CallHolder(Value, Color, XPOS)
                #end "if value is positive"
                Type = 100 if Type > 100 else Type
                setattr(self,Flavor,Type)
                return
        #End Statup

        # Modification mode
        # -----------------
        def calculate_image_matrix(self):
            if self.Recolor.recolored:
                return (
                    im.matrix.saturation(0) * \
                    im.matrix.opacity(float(self.Recolor.opacity) / 255.0) * \
                    im.matrix.brightness(float(self.Recolor.brightness / 255.0)) * \
                    im.matrix.tint(
                        float(self.Recolor.red) / 255.0,
                        float(self.Recolor.green) / 255.0,
                        float(self.Recolor.blue) / 255.0
                    )
                )
            else:
                return im.matrix.saturation(1)
        # -----------------
    #End Player Class contents, Player = PlayerClass() / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    class GirlClass(object):  #rkeljsvg
        def __init__(self,Name="no name",Love=0,Obed=0,Inbt=0,Lust=0):
                self.Name = Name        #changable by player, used in dialog
                self.Tag = Name         #Permanent label, used in code
                self.Names = [Name]     #this is a list of primary names you're allowed to use
                self.Love = Love
                self.Obed = Obed
                self.Inbt = Inbt
                self.Lust = Lust
                self.Thirst = 0         #how much she wants sex
                self.Addict = 0         #how much she needs a fix, goes 0-100
                self.Addictionrate = 0  #how fast her Addict rises, goes from 0-10
                self.Resistance = 0     #how much her Addiciton drops naturally 0-3
                self.Taboo = 0
                self.XP = 0
                self.StatPoints = 0
                self.XPgoal = 100
                self.Lvl = 1
                self.SpriteLoc = StageCenter
                self.Layer = 50         #the layer her sprite appears on
                self.Action = 3         #times the girl can do something this turn
                self.MaxAction = 3      #max times the girl can do something per turn
                self.Pose = 0           #The sex pose the girl is in. If "doggy," show doggy style
                self.Rep = 600
                self.RecentActions = []
                self.DailyActions = []
                self.Traits = []
                self.History = []
                self.Date = 0                           #how many dates you've been on
                self.Chat = [0,0,0,0,0,0]               #whether certain dialogs occurred
                self.Event = [0,0,0,0,0,0,0,0,0,0,0]    #whether certain relationship milestones happened
                self.Petname = "Зеро"
                self.Petnames = ["Zero"]
                self.Pet = "Девушка"
                self.Pets = ["Girl"]
                self.Cheated = 0
                self.Break = [0,0]      #minimum time between break-ups/number of total break-ups
                self.Forced = 0         #are they being coerced
                self.ForcedCount = 0    #countdown for how long they stay mad
                self.Loc = "hold"       #Where she is right now
                self.Home = 0           #where she lives
                # Clothing parts
                self.Outfit = "casual1"         #current outfit
                self.OutfitDay = "casual1"      #outfit she picked for the day
                self.SeenPeen = 0
                self.SeenPuss = 0
                self.SeenChest = 0
                self.SeenPussy = 0
                self.SeenPanties = 0
                self.Upskirt = 0
                self.Uptop = 0
                self.PantiesDown = 0
                self.Wet = 0
                self.Water = 0
                self.Spunk = []
                self.Pierce = 0
                self.Pubes = 1
                self.ArmPose = 1
                self.Blush = 0
                self.Eyes = "normal"
                self.Mouth = "normal"
                self.Brows = "normal"
                self.Emote = "normal"
                self.Held = 0                           #object held in hand
                self.Arms = 0
                self.Legs = 0
                self.Over = 0
                self.Neck = 0
                self.Chest = 0
                self.Panties = 0
                self.Acc = 0
                self.Hair = 1
                self.Hose = 0
                self.Shame = 0
                self.Boots = 0
                self.Hat = 0
                self.Arms_key = None
                self.Legs_key = None
                self.Over_key = None
                self.Neck_key = None
                self.Chest_key = None
                self.Panties_key = None
                self.Acc_key = None
                self.Hose_key = None
                self.Boots_key = None
                self.Hat_key = None
                # Modification mod
                self.Mask = 0
                self.Inventory = []
                # Clothing sets
                # toggle(0),arms/gloves(1),pants(2),shirt(3),necklace(4),bra(5),panties(6),accessory(7),hair(8),hose(9),shame level(10),boots(11),hats(12)
                self.Casual1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                self.Casual2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                self.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                self.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                self.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                self.TempClothes = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                self.Gym = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                self.Sleepwear = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                self.Swim = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                self.Gag = 0
                self.Todo = []                  #todo list, piercing, pubes, etc.
                self.PubeC = 0                  #countdown for when pubes grow back
                self.Schedule = [["MM","MA","ME","MN"],
                                ["TM","TA","TE","TN"],
                                ["WM","WA","WE","WN"],
                                ["ThM","ThA","ThE","ThN"],
                                ["FM","FA","FE","FN"],
                                ["SaM","SaA","SaE","SaN"],
                                ["SuM","SuA","SuE","SuN"],
                                ] #Schedule[0-6][0-4] = Schedule[Day][Time]
                self.Clothing = [0,0,0,0,0,0,0,0,0,0]                      #schedules when she wears what
                #                                                          #(0-6) = Mon-Sun, (7) Datewear, (8) Teachingwear, (9) Private
                self.Org = 0                    #lifetime orgasms
                self.OCount = 0                 #orgasms per encounter
                self.Offhand = 0                #offhand activity
                self.Caught = 0
                self.Kissed = 0                 #How many times they've kissed
                self.Sleep = 0                  #How many times they've slept over
                self.Hand = 0
                self.Finger = 0
                self.Foot = 0
                self.Slap = 0
                self.Strip = 0
                self.Tit = 0
                self.Sex = 0
                self.Anal = 0
                self.Loose = 0
                self.Hotdog = 0
                self.Mast = 0
                self.Massage = 0
                self.FondleB = 0
                self.FondleT = 0
                self.FondleP = 0
                self.FondleA = 0
                self.DildoP = 0
                self.DildoA = 0
                self.Vib = 0
                self.Plug = 0
                self.Plugged = 0
                self.SuckB = 0
                self.InsertP = 0
                self.InsertA = 0
                self.LickP = 0
                self.LickA = 0
                self.Blow = 0
                self.CUN = 0
                self.SC = 0
                self.Red = 0
                self.Swallow = 0
                self.CreamP = 0
                self.CreamA = 0
                self.Les = 0                                    #how many times she's done les stuff
                self.LesWatch = 0                               #how many times you've watched her lesing
                self.SEXP = 0
                self.MassageChart = [0,0,0,0,0,0,0,0,0,0]
                self.PlayerFav = 0                              #you favorite activity with her
                self.Favorite = 0                               #her favorite activity
                self.Facing = 0                                 #head direction in doggy pose, 0 if facing you, 1 if facing forward

                if self.Tag == "Rogue":
                        self.Casual1 = [2,"gloves","skirt","mesh top","spiked collar","tank","black panties",0,0,"tights",0,"boots",0]
                        self.Casual2 = [2,"gloves","pants","pink top",0,"buttoned tank","black panties",0,0,0,0,"sneaks",0]
                        self.Gym = [0,"gloves",0,"hoodie",0,"sports bra","shorts",0,0,0,10,"sneaks",0]
                        self.Sleepwear = [0,0,0,0,0,"tank","green panties",0,0,0,20,0,0]
                        self.Swim = [0,0,0,"hoodie",0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                        self.Costume = [2,"gloves","skirt",0,0,"tube top","black panties","sweater","cosplay",0,0,"boots",0]

                        # turn "evo_green" to Casual1
                        # turn "evo_pink" to Casual2
                        # change "Schedule" stat to "Clothing" stat?
                        self.Home = "bg rogue"
                        self.Hair = "evo"
                        self.LikeKitty = 600
                        self.LikeEmma = 500
                        self.LikeLaura = 500
                        self.Schedule = [["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                        ["bg classroom","bg dangerroom","bg rogue","bg rogue"],
                                        ["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                        ["bg classroom","bg dangerroom","bg rogue","bg rogue"],
                                        ["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                        ["bg dangerroom","bg pool","bg rogue","bg rogue"],
                                        ["bg dangerroom","bg pool","bg rogue","bg rogue"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]
                        self.SexKitty = 0
                        self.SexEmma = 0
                        self.SexLaura = 0
                        self.History = ["met"]
                        self.MassageChart = ["shoulders","arms","arms","hands","hands","back","hips","back","breasts","breasts"]
                elif self.Tag == "Kitty":
                        self.Casual1 = [2,0,"capris","pink top","gold necklace","cami","green panties",0,0,0,0,"sandals",0]
                        self.Casual2 = [2,0,"black jeans","red shirt","star necklace","bra","green panties",0,0,0,0,"sandals",0]
                        self.Gym = [0,0,"shorts",0,0,"sports bra","green panties",0,0,0,10,"sandals",0]
                        self.Sleepwear = [0,0,"shorts",0,0,"cami","green panties",0,0,0,20,0,0]
                        self.Swim = [0,0,"blue skirt",0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                        self.Costume = [2,0,"dress","jacket","flower necklace","dress","lace panties",0,0,0,0,"sandals",0]
                        self.Home = "bg kitty"
                        self.Hair = "evo"
                        self.LikeRogue = 600
                        self.LikeEmma = 500
                        self.LikeLaura = 500
                        self.like = ", как бы, "
                        self.Like = "Как бы, "
                        self.Schedule = [["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg classroom","bg pool","bg kitty","bg kitty"],
                                        ["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg classroom","bg pool","bg kitty","bg kitty"],
                                        ["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg campus","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg campus","bg dangerroom","bg kitty","bg kitty"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]
                        self.SexRogue = 0
                        self.SexEmma = 0
                        self.SexLaura = 0
                        self.MassageChart = ["shoulders","back","hips","thighs","calves","feet","feet","hips","ass","pussy"]
                elif self.Tag == "Emma":
                        self.Casual1 = [2,0,"pants","jacket","choker","corset","white panties",0,0,0,0,"shoes",0]
                        self.Casual2 = [2,"gloves","pants",0,"choker","corset","white panties",0,0,0,5,"thigh boots",0]
                        self.Gym = [0,0,0,0,0,"sports bra","sports panties",0,0,0,10,"shoes",0]
                        self.Sleepwear = [0,0,0,0,0,"corset","white panties",0,0,0,25,0,0]
                        self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                        self.Costume =  [2,"gloves","dress","dress","choker",0,"lace panties",0,0,"stockings and garterbelt",0,"shoes","sun hat"]
                        self.Home = "bg emma"
                        self.Hair = "long"
                        self.Pubes = 0
                        self.LikeRogue = 500
                        self.LikeKitty = 500
                        self.LikeLaura = 500
                        self.Schedule = [["bg teacher","bg teacher","bg classroom","bg emma"],
                                        ["bg teacher","bg teacher","bg dangerroom","bg emma"],
                                        ["bg teacher","bg teacher","bg classroom","bg emma"],
                                        ["bg teacher","bg teacher","bg dangerroom","bg emma"],
                                        ["bg teacher","bg teacher","bg classroom","bg emma"],
                                        ["bg pool","bg pool","bg emma","bg emma"],
                                        ["bg pool","bg pool","bg emma","bg emma"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]
                        self.SexRogue = 0
                        self.SexKitty = 0
                        self.SexLaura = 0
                        self.Loose = 2
                        self.MassageChart = ["shoulders","neck","neck","back","hips","ass","ass","back","breasts","breasts"]

                elif self.Tag == "Laura":
                        self.Casual1 = [2,"wrists","leather pants",0,"leash choker","leather bra","black panties",0,0,0,0,"boots",0]
                        self.Casual2 = [2,0,"skirt","jacket","leash choker","leather bra","black panties",0,0,0,0,"boots",0]
                        self.Gym = [2,"wrists","leather pants",0,0,"leather bra","black panties",0,0,0,0,"boots",0]
                        self.Sleepwear = [0,0,0,0,0,"leather bra","leather panties",0,0,0,20,0,0]
                        self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                        self.Costume = [2,"gloves","other skirt",0,0,"white tank","black panties","suspenders",0,"black stockings",0,"boots",0]
                        self.Home = "bg laura"
                        self.Hair = "long"
                        self.LikeRogue = 500
                        self.LikeKitty = 500
                        self.LikeEmma = 500
                        self.ScentTimer = 0 #this timer gives you X seconds of watching Laura before she notices you there
                        self.Claws = 0
                        self.Schedule = [["bg pool","bg classroom","bg dangerroom","bg laura"],
                                        ["bg dangerroom","bg classroom","bg campus","bg laura"],
                                        ["bg pool","bg classroom","bg dangerroom","bg laura"],
                                        ["bg dangerroom","bg classroom","bg campus","bg laura"],
                                        ["bg pool","bg classroom","bg dangerroom","bg laura"],
                                        ["bg pool","bg laura","bg dangerroom","bg laura"],
                                        ["bg pool","bg laura","bg dangerroom","bg laura"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]
                        self.SexRogue = 0
                        self.SexKitty = 0
                        self.SexEmma = 0
                        self.Loose = 2
                        self.MassageChart = ["shoulders","back","arms","hips","thighs","calves","ass","ass","pussy","pussy"]

                elif self.Tag == "Jean":
                        # JeanX = GirlClass("Jean",200,0,1000,10) #Inbt falls to 800
                        self.StatStore = 0      #this stores Love stat above 500 and distributes it later.
                        self.IX = 500           #this is an amount subtracted from her Inbt in most checks, and reduces over time

                        self.Casual1 = [2,0,"pants","pink shirt",0,"green bra","green panties",0,0,0,0,"sandals",0]
                        self.Casual2 = [2,0,"skirt","green shirt",0,"green bra","green panties",0,0,0,0,"sandals",0]
                        self.Gym = [0,0,"yoga pants",0,0,"sports bra","green panties",0,0,0,0,"sandals",0]
                        self.Sleepwear = [0,0,0,"pink shirt",0,"green bra","green panties",0,0,0,0,0,0]
                        self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                        self.Costume =  [2,0,"shorts","yellow shirt",0,"green bra","green panties","suspenders","pony",0,0,"sandals",0]
                        self.Home = "bg jean"
                        self.Hair = "short"

                        RogueX.LikeJean = 200
                        KittyX.LikeJean = 300
                        EmmaX.LikeJean = 100
                        LauraX.LikeJean = 300

                        RogueX.SexJean = 0
                        KittyX.SexJean = 0
                        EmmaX.SexJean = 0
                        LauraX.SexJean = 0

                        self.LikeRogue = 500
                        self.LikeKitty = 500
                        self.LikeEmma = 300
                        self.LikeLaura = 500
                        self.SexRogue = 0
                        self.SexKitty = 0
                        self.SexEmma = 0
                        self.SexLaura = 0

                        #This stores up their like values for later.
                        self.LikeSRogue = 0
                        self.LikeSKitty = 0
                        self.LikeSEmma = 0
                        self.LikeSLaura = 0

                        self.Schedule = [["bg classroom","bg classroom","bg dangerroom","bg jean"],
                                        ["bg jean","bg classroom","bg jean","bg jean"],
                                        ["bg jean","bg classroom","bg dangerroom","bg jean"],
                                        ["bg classroom","bg classroom","bg jean","bg jean"],
                                        ["bg jean","bg classroom","bg dangerroom","bg jean"],
                                        ["bg dangerroom","bg campus","bg pool","bg jean"],
                                        ["bg dangerroom","bg campus","bg pool","bg jean"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                        self.MassageChart = ["back","shoulders","neck","neck","back","hips","ass","ass","pussy","pussy"]

                elif self.Tag == "Storm":
                        self.Casual1 = [2,0,"skirt","white shirt",0,"black bra","white panties",0,0,0,0,"sandals",0]
                        self.Casual2 = [2,0,"pants","jacket",0,"sports bra","white panties",0,0,0,0,"boots",0]
                        self.Gym = [0,0,"yoga pants",0,0,"sports bra","white panties",0,0,0,10,"boots",0]
                        self.Sleepwear = [0,0,0,"white shirt",0,0,"white panties",0,0,0,25,0,0]
                        self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                        self.Costume = [2,0,0,0,"rings","cos bra","cos panties","rings","short",0,0,"rings",0]
                        self.Home = "bg storm"
                        self.Hair = "long"

                        self.LikeRogue = 500
                        self.LikeKitty = 600
                        self.LikeLaura = 500
                        self.LikeEmma = 400
                        self.LikeJean = 300
                        self.SexRogue = 0
                        self.SexKitty = 0
                        self.SexLaura = 0
                        self.SexEmma = 0
                        self.SexJean = 0

                        #fills in existing characters
                        RogueX.LikeStorm = 600
                        KittyX.LikeStorm = 600
                        EmmaX.LikeStorm = 500
                        LauraX.LikeStorm = 500
                        JeanX.LikeStorm = 300

                        RogueX.SexStorm = 0
                        KittyX.SexStorm = 0
                        EmmaX.SexStorm = 0
                        LauraX.SexStorm = 0
                        JeanX.SexStorm = 0

                        JeanX.LikeSStorm = 0

                        self.Schedule = [["bg storm","bg dangerroom","bg dangerroom","bg storm"],
                                        ["bg teacher","bg teacher","bg classroom","bg storm"],
                                        ["bg storm","bg dangerroom","bg dangerroom","bg storm"],
                                        ["bg teacher","bg teacher","bg classroom","bg storm"],
                                        ["bg pool","bg campus","bg classroom","bg storm"],
                                        ["bg storm","bg campus","bg storm","bg pool"],
                                        ["bg storm","bg campus","bg storm","bg pool"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                        self.MassageChart = ["feet","calves","thighs","hips","ass","ass","pussy","ass","pussy","pussy"]

                elif self.Tag == "Jubes":
                        self.Casual1 = [2,0,"shorts","red shirt",0,"sports bra","blue panties","jacket",0,0,0,"sneaks",0]
                        self.Casual2 = [2,0,"pants","black shirt",0,"sports bra","blue panties","jacket",0,0,0,"sneaks",0]
                        self.Gym = [0,0,"pants",0,0,"sports bra","blue panties",0,0,0,10,"sneaks",0]
                        self.Sleepwear = [0,0,0,0,0,"sports bra","blue panties",0,0,0,25,0,0]
                        self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                        self.Costume2 = [2,0,0,"saiyan armor",0,"saiyan leotard","saiyan leotard","saiyan tail",0,0,0,"sneaks",0]
                        self.Costume = [2,0,0,"dress","choker","lace bra","lace panties",0,"short","stockings and garterbelt",0,"sneaks",0]
                        self.Home = "bg jubes"
                        self.Hair = "shades"

                        self.LikeRogue = 500
                        self.LikeKitty = 600
                        self.LikeLaura = 600
                        self.LikeEmma = 500
                        self.LikeJean = 300
                        self.LikeStorm = 500
                        self.SexRogue = 0
                        self.SexKitty = 0
                        self.SexLaura = 0
                        self.SexEmma = 0
                        self.SexJean = 0
                        self.SexStorm = 0

                        #fills in existing characters
                        RogueX.LikeJubes = 500
                        KittyX.LikeJubes = 600
                        EmmaX.LikeJubes = 500
                        LauraX.LikeJubes = 600
                        JeanX.LikeJubes = 300
                        StormX.LikeJubes = 500

                        RogueX.SexJubes = 0
                        KittyX.SexJubes = 0
                        EmmaX.SexJubes = 0
                        LauraX.SexJubes = 0
                        JeanX.SexJubes = 0
                        StormX.SexJubes = 0

                        JeanX.LikeSJubes = 0

                        self.Schedule = [["bg jubes","bg dangerroom","bg dangerroom","bg jubes"],
                                        ["bg classroom","bg classroom","bg jubes","bg pool"],
                                        ["bg jubes","bg dangerroom","bg dangerroom","bg jubes"],
                                        ["bg dangerroom","bg dangerroom","bg jubes","bg pool"],
                                        ["bg pool","bg campus","bg campus","bg jubes"],
                                        ["bg jubes","bg campus","bg jubes","bg jubes"],
                                        ["bg jubes","bg campus","bg jubes","bg jubes"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                        self.MassageChart = ["neck","shoulders","calves","feet","neck","shoulders","calves","feet","pussy","pussy"]

                elif self.Tag == "Gwen":
                        # toggle(0),arms/gloves(1),pants(2),shirt(3),necklace(4),bra(5),panties(6),accessory(7),hair(8),hose(9),shame level(10),boots(11),hats(12)
                        self.Casual1 = [2,"gloves","suit","suit",0,"bra","white panties",0,0,0,0,"boots","mask"]
                        self.Casual2 = [2,0,"shorts","tshirt",0,"bra","white panties",0,0,"tights",0,"sneaks",0]
                        self.Gym = [0,0,"shorts",0,0,"tank","white panties",0,0,0,0,"sneaks",0]
                        self.Sleepwear = [0,0,"shorts",0,0,"tank","white panties",0,0,0,0,0,0]
                        self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                        self.Costume = [2,0,"cheer skirt","cheer top",0,0,"white panties",0,"pony","socks",0,"sneaks",0]
                        self.Home = "bg gwen"
                        self.Hair = "short"

                        self.LikeRogue = 600
                        self.LikeKitty = 700
                        self.LikeLaura = 750
                        self.LikeEmma = 700
                        self.LikeJean = 600
                        self.LikeStorm = 600
                        self.LikeJubes = 700
                        self.SexRogue = 0
                        self.SexKitty = 0
                        self.SexLaura = 0
                        self.SexEmma = 0
                        self.SexJean = 0
                        self.SexStorm = 0
                        self.SexJubes = 0

                        #fills in existing characters
                        RogueX.LikeGwen = 500
                        KittyX.LikeGwen = 600
                        EmmaX.LikeGwen = 500
                        LauraX.LikeGwen = 500
                        JeanX.LikeGwen = 300
                        StormX.LikeGwen = 500
                        JubesX.LikeGwen = 500

                        RogueX.SexGwen = 0
                        KittyX.SexGwen = 0
                        EmmaX.SexGwen = 0
                        LauraX.SexGwen = 0
                        JeanX.SexGwen = 0
                        StormX.SexGwen = 0
                        JubesX.SexGwen = 0

                        JeanX.LikeSGwen = 0

                        self.Schedule = [["bg gwen","bg dangerroom","bg dangerroom","bg gwen"],
                                        ["bg classroom","bg classroom","bg gwen","bg gwen"],
                                        ["bg gwen","bg dangerroom","bg dangerroom","bg gwen"],
                                        ["bg dangerroom","bg dangerroom","bg gwen","bg gwen"],
                                        ["bg pool","bg campus","bg campus","bg gwen"],
                                        ["bg gwen","bg campus","bg gwen","bg gwen"],
                                        ["bg gwen","bg campus","bg gwen","bg gwen"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                        self.MassageChart = ["feet","feet","calves","thighs","hips","back","hips","ass","pussy","pussy"]

                elif self.Tag == "Betsy":
                        # toggle(0),arms/gloves(1),pants(2),shirt(3),necklace(4),bra(5),panties(6),accessory(7),hair(8),hose(9),shame level(10),boots(11),hats(12)
                        self.Casual1 = [2,"gloves","shorts","tank",0,"bra","blue panties",0,0,"socks",0,"shoes",0]
                        self.Casual2 = [2,0,"skirt","pink top",0,"bra","blue panties","scarf",0,0,0,"shoes",0]
                        self.Gym = [0,0,"yoga pants","tank",0,"bra","blue panties",0,0,0,0,"sneaks",0]
                        self.Sleepwear = [0,0,0,"pink top",0,"bra","blue panties",0,0,0,0,0,0]
                        self.Swim = [0,0,0,0,0,"swimsuit","swimsuit",0,0,0,0,0,0]
                        self.Costume = [2,0,"yoga pants","jacket",0,"sports bra","blue panties",0,"blonde",0,0,"sneaks",0]
                        self.Home = "bg betsy"
                        self.Hair = "short"
                        self.Knife = 0

                        self.LikeRogue = 600
                        self.LikeKitty = 700
                        self.LikeLaura = 700
                        self.LikeEmma = 700
                        self.LikeJean = 650
                        self.LikeStorm = 600
                        self.LikeJubes = 700
                        self.LikeGwen = 600
                        self.SexRogue = 0
                        self.SexKitty = 0
                        self.SexLaura = 0
                        self.SexEmma = 0
                        self.SexJean = 0
                        self.SexStorm = 0
                        self.SexJubes = 0
                        self.SexGwen = 0

                        #fills in existing characters
                        RogueX.LikeBetsy = 600
                        KittyX.LikeBetsy = 600
                        EmmaX.LikeBetsy = 600
                        LauraX.LikeBetsy = 500
                        JeanX.LikeBetsy = 300
                        StormX.LikeBetsy = 500
                        JubesX.LikeBetsy = 600
                        GwenX.LikeBetsy = 650

                        RogueX.SexBetsy = 0
                        KittyX.SexBetsy = 0
                        EmmaX.SexBetsy = 0
                        LauraX.SexBetsy = 0
                        JeanX.SexBetsy = 0
                        StormX.SexBetsy = 0
                        JubesX.SexBetsy = 0
                        GwenX.SexBetsy = 0

                        JeanX.LikeSBetsy = 0

                        self.Schedule = [["bg betsy","bg dangerroom","bg dangerroom","bg betsy"],
                                        ["bg betsy","bg classroom","bg dangerroom","bg betsy"],
                                        ["bg classroom","bg classroom","bg betsy","bg betsy"],
                                        ["bg dangerroom","bg dangerroom","bg betsy","bg betsy"],
                                        ["bg classroom","bg classroom","bg campus","bg betsy"],
                                        ["bg dangerroom","bg campus","bg pool","bg betsy"],
                                        ["bg betsy","bg campus","bg betsy","bg betsy"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                        self.MassageChart = ["shoulders","neck","neck","back","hips","ass","thighs","hips","pussy","pussy"]

                elif self.Tag == "Doreen":
                        # toggle(0),arms/gloves(1),pants(2),shirt(3),necklace(4),bra(5),panties(6),accessory(7),hair(8),hose(9),shame level(10),boots(11),hats(12)
                        self.Casual1 = [2,0,"shorts","tube top",0,"tan bra","tan panties","jacket",0,"pantyhose",0,"boots","headband"]
                        self.Casual2 = [2,0,"skirt","tshirt",0,"tan bra","tan panties",0,0,"tights",0,"sneaks","headband"]
                        self.Gym = [0,0,0,0,0,"sports bra","tan panties","jacket",0,"tights",0,"sneaks","headband"]
                        self.Sleepwear = [0,0,0,"tshirt",0,0,"tan panties",0,0,"tights",0,0,0]
                        self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                        self.Costume = [2,0,"red skirt","sweater",0,"tan bra","tan panties",0,0,0,0,"sneaks","glasses"]
                        self.Home = "bg doreen"
                        self.Hair = "short"
                        self.Tail = 1

                        self.LikeRogue = 700
                        self.LikeKitty = 700
                        self.LikeLaura = 750
                        self.LikeEmma = 700
                        self.LikeJean = 600
                        self.LikeStorm = 700
                        self.LikeJubes = 700
                        self.LikeGwen = 700
                        self.LikeBetsy = 700
                        self.SexRogue = 0
                        self.SexKitty = 0
                        self.SexLaura = 0
                        self.SexEmma = 0
                        self.SexJean = 0
                        self.SexStorm = 0
                        self.SexJubes = 0
                        self.SexGwen = 0
                        self.SexBetsy = 0

                        #fills in existing characters
                        RogueX.LikeDoreen = 600
                        KittyX.LikeDoreen = 600
                        EmmaX.LikeDoreen = 700
                        LauraX.LikeDoreen = 750
                        JeanX.LikeDoreen = 500
                        StormX.LikeDoreen = 600
                        JubesX.LikeDoreen = 600
                        GwenX.LikeDoreen = 700
                        BetsyX.LikeDoreen = 600

                        RogueX.SexDoreen = 0
                        KittyX.SexDoreen = 0
                        EmmaX.SexDoreen = 0
                        LauraX.SexDoreen = 0
                        JeanX.SexDoreen = 0
                        StormX.SexDoreen = 0
                        JubesX.SexDoreen = 0
                        GwenX.SexDoreen = 0
                        BetsyX.SexDoreen = 0

                        JeanX.LikeSDoreen = 0

                        self.Schedule = [["bg doreen","bg dangerroom","bg dangerroom","bg doreen"],
                                        ["bg classroom","bg classroom","bg doreen","bg doreen"],
                                        ["bg doreen","bg dangerroom","bg dangerroom","bg doreen"],
                                        ["bg dangerroom","bg dangerroom","bg doreen","bg doreen"],
                                        ["bg pool","bg campus","bg campus","bg doreen"],
                                        ["bg doreen","bg campus","bg doreen","bg doreen"],
                                        ["bg doreen","bg campus","bg doreen","bg doreen"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                        self.MassageChart = ["feet","feet","calves","thighs","hips","back","hips","ass","pussy","pussy"]
                elif self.Tag == "Wanda":
                        # toggle(0),arms/gloves(1),pants(2),shirt(3),necklace(4),bra(5),panties(6),accessory(7),hair(8),hose(9),shame level(10),boots(11),hats(12)
                        self.Casual1 = [2,"armlet","pants","shirt","choker","red bra","gray panties",0,0,0,0,"boots",0]
                        self.Casual2 = [2,"armlet","shorts","corset","choker","mesh top","gray panties","jacket",0,"pantyhose",0,"boots",0]
                        self.Gym = [0,0,"pants","shirt","choker","red bra","gray panties",0,0,0,0,"boots",0]
                        self.Sleepwear = [0,0,"dress",0,0,0,"gray panties",0,0,0,0,0,0]
                        self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                        self.Costume = [2,0,"skirt","purple top","scarf",0,"gray panties",0,"long",0,0,"boots","headband"]
                        self.Casual3 = [2,0,"dress",0,"choker","mesh top","gray panties","jacket",0,"socks",0,"boots",0]
                        self.Home = "bg wanda"
                        self.Hair = "short"

                        self.LikeRogue = 800
                        self.LikeKitty = 800
                        self.LikeLaura = 800
                        self.LikeEmma = 800
                        self.LikeJean = 600
                        self.LikeStorm = 800
                        self.LikeJubes = 800
                        self.LikeGwen = 800
                        self.LikeBetsy = 800
                        self.LikeDoreen = 800
                        self.SexRogue = 0
                        self.SexKitty = 0
                        self.SexLaura = 0
                        self.SexEmma = 0
                        self.SexJean = 0
                        self.SexStorm = 0
                        self.SexJubes = 0
                        self.SexGwen = 0
                        self.SexBetsy = 0
                        self.SexDoreen = 0

                        #fills in existing characters
                        RogueX.LikeWanda = 600
                        KittyX.LikeWanda = 600
                        EmmaX.LikeWanda = 700
                        LauraX.LikeWanda = 750
                        JeanX.LikeWanda = 500
                        StormX.LikeWanda = 600
                        JubesX.LikeWanda = 600
                        GwenX.LikeWanda = 700
                        BetsyX.LikeWanda = 600
                        DoreenX.LikeWanda = 600

                        RogueX.SexWanda = 0
                        KittyX.SexWanda = 0
                        EmmaX.SexWanda = 0
                        LauraX.SexWanda = 0
                        JeanX.SexWanda = 0
                        StormX.SexWanda = 0
                        JubesX.SexWanda = 0
                        GwenX.SexWanda = 0
                        BetsyX.SexWanda = 0
                        DoreenX.SexWanda = 0

                        JeanX.LikeSWanda = 0

                        self.Schedule = [["bg wanda","bg wanda","bg dangerroom","bg wanda"],
                                        ["bg dangerroom","bg classroom","bg wanda","bg wanda"],
                                        ["bg wanda","bg pool","bg dangerroom","bg wanda"],
                                        ["bg classroom","bg classroom","bg wanda","bg wanda"],
                                        ["bg dangerroom","bg classroom","bg mall","bg wanda"],
                                        ["bg wanda","bg campus","bg campus","bg wanda"],
                                        ["bg wanda","bg campus","bg wanda","bg wanda"],
                                        ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                        self.MassageChart = ["neck","shoulders","back","back","hips","ass","hips","thighs","pussy","pussy"]

                self.OutfitChange(Changed=1) #assigns their default outfit, hopefully

        def Introduction(self): #rkeljsvgbdw
                #things to add when girl is introduced
                if self == RogueX: #if self.Name == "Rogue":?
                        if Player.Male:
                            self.Petname = "Сладенький"
                            self.Petname_rod = "Сладенького"
                            self.Petname_dat = "Сладенькому"
                            self.Petname_vin = "Сладенького"
                            self.Petname_tvo = "Сладеньким"
                            self.Petname_pre = "Сладеньком"
                        else:
                            self.Petname = "Сладенькая"
                            self.Petname_rod = "Сладенькой"
                            self.Petname_dat = "Сладенькой"
                            self.Petname_vin = "Сладенькую"
                            self.Petname_tvo = "Сладенькой"
                            self.Petname_pre = "Сладенькой"
                        self.Petnames = ["Sugar",Player.Name]
                        self.Pet = "Роуг"
                        self.Pet_rod = "Роуг"
                        self.Pet_dat = "Роуг"
                        self.Pet_vin = "Роуг"
                        self.Pet_tvo = "Роуг"
                        self.Pet_pre = "Роуг"
                        self.Pets = ["Rogue"]
                elif self == KittyX:
                        self.Petname = Player.Name[:1]
                        self.Petname_rod = Player.Name[:1]
                        self.Petname_dat = Player.Name[:1]
                        self.Petname_vin = Player.Name[:1]
                        self.Petname_tvo = Player.Name[:1]
                        self.Petname_pre = Player.Name[:1]
                        self.Petnames = ["sweetie",Player.Name[:1],Player.Name]
                        self.Pet = "Китти"
                        self.Pet_rod = "Китти"
                        self.Pet_dat = "Китти"
                        self.Pet_vin = "Китти"
                        self.Pet_tvo = "Китти"
                        self.Pet_pre = "Китти"
                        self.Pets = ["Kitty"]
                elif self == EmmaX:
                        self.Names = ["Ms. Frost"]
                        self.Name = "Мисс Фрост"
                        self.Name_rod = "Мисс Фрост"
                        self.Name_dat = "Мисс Фрост"
                        self.Name_vin = "Мисс Фрост"
                        self.Name_tvo = "Мисс Фрост"
                        self.Name_pre = "Мисс Фрост"
                        self.Petname = "Player.Name"
                        self.Petname_rod = "Player.Name"
                        self.Petname_dat = "Player.Name"
                        self.Petname_vin = "Player.Name"
                        self.Petname_tvo = "Player.Name"
                        self.Petname_pre = "Player.Name"
                        self.Petnames = [Player.Name]
                        self.Pet = EmmaX.Name
                        self.Pet_rod = EmmaX.Name
                        self.Pet_dat = EmmaX.Name
                        self.Pet_vin = EmmaX.Name
                        self.Pet_tvo = EmmaX.Name
                        self.Pet_pre = EmmaX.Name
                        self.Pets = ["Emma","Ms. Frost"]
                elif self == LauraX:
                        self.Petname = "йо"
                        self.Petname_rod = "йо"
                        self.Petname_dat = "йо"
                        self.Petname_vin = "йо"
                        self.Petname_tvo = "йо"
                        self.Petname_pre = "йо"
                        self.Petnames = ["yo",Player.Name]
                        self.Pet = "Лора"
                        self.Pet_rod = "Лоры"
                        self.Pet_dat = "Лоре"
                        self.Pet_vin = "Лору"
                        self.Pet_tvo = "Лорой"
                        self.Pet_pre = "Лоре"
                        self.Pets = ["Laura","X-23"]
                elif self.Tag == "Jean":
                        self.Petname = "эм. . ."
                        self.Petname_rod = "йо"
                        self.Petname_dat = "йо"
                        self.Petname_vin = "йо"
                        self.Petname_tvo = "йо"
                        self.Petname_pre = "йо"
                        self.Petnames = ["um. . ."]
                        self.Pet = JeanX.Name
                        self.Pet_rod = JeanX.Name
                        self.Pet_dat = JeanX.Name
                        self.Pet_vin = JeanX.Name
                        self.Pet_tvo = JeanX.Name
                        self.Pet_pre = JeanX.Name
                        self.Pets = ["Jean"]
                elif self.Tag == "Storm":
                        self.Petname = "Player.Name"
                        self.Petname_rod = "Player.Name"
                        self.Petname_dat = "Player.Name"
                        self.Petname_vin = "Player.Name"
                        self.Petname_tvo = "Player.Name"
                        self.Petname_pre = "Player.Name"
                        self.Petnames = ["Player.Name"]
                        self.Pet = StormX.Name
                        self.Pet_rod = StormX.Name
                        self.Pet_dat = StormX.Name
                        self.Pet_vin = StormX.Name
                        self.Pet_tvo = StormX.Name
                        self.Pet_pre = StormX.Name
                        self.Pets = ["Storm","Ororo","Ms. Munroe"]
                elif self.Tag == "Jubes":
                        if Player.Male:
                            self.Petname = "Бро"
                            self.Petname_rod = "Бро"
                            self.Petname_dat = "Бро"
                            self.Petname_vin = "Бро"
                            self.Petname_tvo = "Бро"
                            self.Petname_pre = "Бро"
                        else:
                            self.Petname = "Сис"
                            self.Petname_rod = "Сис"
                            self.Petname_dat = "Сис"
                            self.Petname_vin = "Сис"
                            self.Petname_tvo = "Сис"
                            self.Petname_pre = "Сис"
                        self.Petnames = ["Bro","Player.Name"]
                        self.Pet = JubesX.Name
                        self.Pet_rod = JubesX.Name
                        self.Pet_dat = JubesX.Name
                        self.Pet_vin = JubesX.Name
                        self.Pet_tvo = JubesX.Name
                        self.Pet_pre = JubesX.Name
                        self.Pets = ["Jubes","Jubilee"]
                elif self.Tag == "Gwen":
                        if Player.Male:
                            self.Petname = "Чувак"
                            self.Petname_rod = "Чувака"
                            self.Petname_dat = "Чуваку"
                            self.Petname_vin = "Чувака"
                            self.Petname_tvo = "Чуваком"
                            self.Petname_pre = "Чуваке"
                        else:
                            self.Petname = "Чувиха"
                            self.Petname_rod = "Чувихи"
                            self.Petname_dat = "Чувихе"
                            self.Petname_vin = "Чувиху"
                            self.Petname_tvo = "Чувихой"
                            self.Petname_pre = "Чувихе"
                        self.Petnames = ["Dude","Player.Name"]
                        self.Pet = GwenX.Name
                        self.Pet_rod = GwenX.Name
                        self.Pet_dat = GwenX.Name
                        self.Pet_vin = GwenX.Name
                        self.Pet_tvo = GwenX.Name
                        self.Pet_pre = GwenX.Name
                        self.Pets = ["Gwen","Gwenpool"]
                elif self.Tag == "Betsy":
                        if Player.Male:
                            self.Petname = "Приятель"
                            self.Petname_rod = "Приятеля"
                            self.Petname_dat = "Приятелю"
                            self.Petname_vin = "Приятеля"
                            self.Petname_tvo = "Приятелем"
                            self.Petname_pre = "Приятеле"
                        else:
                            self.Petname = "Подруга"
                            self.Petname_rod = "Подруги"
                            self.Petname_dat = "Подруге"
                            self.Petname_vin = "Подругу"
                            self.Petname_tvo = "Подругой"
                            self.Petname_pre = "Подруге"
                        self.Petnames = ["Mate","Player.Name"]
                        self.Pet = "Бетси"
                        self.Pet_rod = "Бетси"
                        self.Pet_dat = "Бетси"
                        self.Pet_vin = "Бетси"
                        self.Pet_tvo = "Бетси"
                        self.Pet_pre = "Бетси"
                        self.Pets = ["Betsy"]
                elif self.Tag == "Doreen":
                        if Player.Male:
                            self.Petname = "Чувак"
                            self.Petname_rod = "Чувака"
                            self.Petname_dat = "Чуваку"
                            self.Petname_vin = "Чувака"
                            self.Petname_tvo = "Чуваком"
                            self.Petname_pre = "Чуваке"
                        else:
                            self.Petname = "Чувиха"
                            self.Petname_rod = "Чувихи"
                            self.Petname_dat = "Чувихе"
                            self.Petname_vin = "Чувиху"
                            self.Petname_tvo = "Чувихой"
                            self.Petname_pre = "Чувихе"
                        self.Petnames = ["Dude"]
                        self.Pet = "Дорин"
                        self.Pet_rod = "Дорин"
                        self.Pet_dat = "Дорин"
                        self.Pet_vin = "Дорин"
                        self.Pet_tvo = "Дорин"
                        self.Pet_pre = "Дорин"
                        self.Pets = ["Doreen"]
                elif self.Tag == "Wanda":
                        if Player.Male:
                            self.Petname = "Бро"
                            self.Petname_rod = "Бро"
                            self.Petname_dat = "Бро"
                            self.Petname_vin = "Бро"
                            self.Petname_tvo = "Бро"
                            self.Petname_pre = "Бро"
                        else:
                            self.Petname = "Сис"
                            self.Petname_rod = "Сис"
                            self.Petname_dat = "Сис"
                            self.Petname_vin = "Сис"
                            self.Petname_tvo = "Сис"
                            self.Petname_pre = "Сис"
                        self.Petnames = [Terms["bro"]]
                        self.Pet = "Ванда"
                        self.Pet_rod = "Ванды"
                        self.Pet_dat = "Ванде"
                        self.Pet_vin = "Ванду"
                        self.Pet_tvo = "Вандой"
                        self.Pet_pre = "Ванде"
                        self.Pets = ["Wanda"]

                self.OutfitChange(6,Changed=1) #assigns their default outfit, hopefully
                global TotalGirls
                if self not in TotalGirls:
                        TotalGirls.append(self)                 #These are the girls you have met at all
                Shop_Inventory.extend(["DL","G","A"])     #adds these three items to the store for each girl added
                PersonalRooms.append(self.Home)

        def SluttyClothes(self): #rkeljsvg
                # called to check if loosened morals will lead to looser default outfits.
                # $ RogueX.SluttyClothes
                if self is RogueX:
                            if "stockings and garterbelt" in self.Inventory and self.Casual1[0] < 3:
                                    self.Casual1[9] = "stockings and garterbelt"
                            elif self.Inbt >= 300 and self.Casual1[0] < 3: #ApprovalCheck("Rogue", 300, "I"):
                                    self.Casual1[9] = "stockings"

                            if self.Gym[0] == 0 and self.Gym[5] and self.Inbt >= 300:
                                    #removed hoodie if she's no longer shy
                                    self.Gym[3] == 0

                            if self.Swim[0] == 0 and self.Swim[5] and self.Inbt >= 300:
                                    #removed hoodie if she's no longer shy
                                    self.Swim[3] == 0
                elif self is KittyX:
                            if self.Swim[2] == "blue skirt" and self.Swim[6] and self.Inbt > 500:
                                    #removes blue skirt if she gets comfortable with it.
                                    self.Swim[2] = 0
                elif self is LauraX:
                            if self.Inbt >= 400 and self.Casual2[5] == "leather bra" and "corset" in self.Inventory and self.Casual2[0] < 3:
                                    self.Casual2[5] = "corset"
                            if self.Inbt >= 600 and "lace panties" in self.Inventory and self.Casual2[0] < 3:
                                    self.Casual2[6] = "lace panties"
                            if self.Inbt >= 600 and "stockings and garterbelt" in self.Inventory and self.Casual2[0] < 3:
                                    self.Casual2[9] = "stockings and garterbelt"

                elif self is JeanX:
                            if "stockings and garterbelt" in self.Inventory and self.Casual1[0] < 3:
                                    self.Casual1[9] = "stockings and garterbelt"
                            elif self.Love >= 300 and self.Casual1[0] < 3: #ApprovalCheck("Rogue", 300, "I"):
                                    self.Casual1[9] = "stockings"
                            if self.Inbt >= 600 and "bikini top" in self.Inventory:
                                    self.Gym[5] = "bikini top" if self.Gym[0] == 1 else self.Gym[5]
                            if self.Inbt >= 600 and "lace bra" in self.Inventory:
                                    self.Casual1[5] = "lace bra" if self.Casual1[0] < 3 else self.Casual1[5]
                                    self.Casual2[5] = "lace bra" if self.Casual2[0] < 3 else self.Casual2[5]
                            if self.Inbt >= 600 and "lace panties" in self.Inventory:
                                    self.Casual1[6] = "lace panties" if self.Casual1[0] < 3 else self.Casual1[6]
                                    self.Casual2[6] = "lace panties" if self.Casual2[0] < 3 else self.Casual2[6]
                elif self is StormX:
                            if self.Inbt >= 400 and self.Casual2[5] == "sports bra" and self.Casual2[0] < 3:
                                    self.Casual2[5] = "tube top"
                            if self.Inbt >= 400 and self.Casual2[6] == "white panties" and self.Casual2[0] < 3:
                                    self.Casual2[6] = "black panties"
                            if self.Inbt >= 600 and "lace panties" in self.Inventory and self.Casual2[0] < 3:
                                    self.Casual2[6] = "lace panties"
                elif self is JubesX:
                            if self.Inbt >= 500 and self.Casual1[3] == "red shirt" and self.Casual1[0] < 3:
                                    self.Casual1[3] = "tube top"
                                    self.Casual1[5] = 0
                            if self.Inbt >= 600 and "lace panties" in self.Inventory and self.Casual2[0] < 3:
                                    self.Casual2[6] = "lace panties"
                            if self.Inbt >= 600 and "stockings and garterbelt" in self.Inventory and self.Casual2[0] < 3:
                                    self.Casual2[9] = "stockings and garterbelt"
                elif self is GwenX:
                            if self.Inbt >= 600 and "lace bra" in self.Inventory and self.Casual2[0] < 3:
#                                    self.Casual1[5] = "lace bra"
                                    self.Casual2[5] = "lace bra"
                            if self.Inbt >= 600 and "lace panties" in self.Inventory:
                                    self.Casual1[6] = "lace panties" if self.Casual1[0] < 3 else self.Casual1[6]
                                    self.Casual2[6] = "lace panties" if self.Casual2[0] < 3 else self.Casual2[6]
                            if self.Inbt >= 700 and "stockings and garterbelt" in self.Inventory and self.Casual2[0] < 3:
                                    self.Casual2[9] = "stockings and garterbelt"
                elif self is BetsyX:
                            if self.Inbt >= 600 and "lace bra" in self.Inventory:
                                    self.Casual1[5] = "lace bra" if self.Casual1[0] < 3 else self.Casual1[5]
                                    self.Casual2[5] = "lace bra" if self.Casual2[0] < 3 else self.Casual2[5]
                                    if not self.Sleepwear[0]:
                                            self.Sleepwear[5] = "lace bra"
                            if self.Inbt >= 600 and "lace panties" in self.Inventory:
                                    self.Casual1[6] = "lace panties" if self.Casual1[0] < 3 else self.Casual1[6]
                                    self.Casual2[6] = "lace panties" if self.Casual2[0] < 3 else self.Casual2[6]
                                    if not self.Sleepwear[0]:
                                            self.Sleepwear[6] = "lace panties"
                            if self.Inbt >= 700 and "stockings and garterbelt" in self.Inventory and self.Casual2[0] < 3:
                                    self.Casual2[9] = "stockings and garterbelt"
                            if self.Inbt >= 700 and "swimsuit" in self.Inventory and not self.Gym[0]:
                                    self.Gym[5] = "swimsuit"
                                    self.Gym[6] = "swimsuit"
                return

        def AddWord(self,Only=0,Recent=0,Daily=0,Trait=0,History=0):
                #applies variables to appropriate character stats
                # $ RogueX.AddWord(1,"angry",0,0,0)
                #if Only, then only apply it if it's not already there
                if (Recent and not Only) or (Recent and Recent not in self.RecentActions):
                        self.RecentActions.append(Recent)
                if (Daily and not Only) or (Daily and Daily not in self.DailyActions):
                        self.DailyActions.append(Daily)
                if (Trait and not Only) or (Trait and Trait not in self.Traits):
                        self.Traits.append(Trait)
                if (History and not Only) or (History and History not in self.History):
                        self.History.append(History)
                return

        def DrainWord(self, Word = "word", Recent = 1, Daily = 1, Traits=0,History=0):
                # to remove words from the daily/recent lists ,
                # $ RogueX.DrainWord("angry",0,1)
                if Recent and Word in self.RecentActions:
                    while Word in self.RecentActions:
                            self.RecentActions.remove(Word)
                if Daily and Word in self.DailyActions:
                    while Word in self.DailyActions:
                            self.DailyActions.remove(Word)
                if Traits and Word in self.Traits:
                    while Word in self.Traits:
                            self.Traits.remove(Word)
                if History and Word in self.History:
                    while Word in self.History:
                            self.History.remove(Word)
                return

        def Statup(self, Flavor=0, Check=100, Value=1, Greater=0, Type=0, Alt=[[],0,0], Overflow=0, BStat=0, XPOS = 0.75):
                # $ RogueX.Statup("Love", 90, 5)
                # $ RogueX.Statup("Love", 90, 5,Alt=[[RogueX,KittyX],500,-10])
#                Test = str(Value)
#                ch_u(Test +" b", interact=True)

                if self not in TotalGirls: #should remove "character don't exist" errors
                        return

                if self in Alt[0]:
                                #if there is an alternate character option. . .
                                Check = Alt[1] if Alt[1] else Check
                                Value = Alt[2] if Alt[2] else Value

                if Flavor == "Love" or Flavor == "Obed" or Flavor == "Inbt":
                        #bumps this stat into the 1000s
                        Check = Check * 10

                Type = getattr(self,Flavor) #sets Type to the value referenced (ie if Flavor is "Love," Type becomes self.Love's value)

                Overflow = self.Chat[4]
                XPOS = self.SpriteLoc

                if self.Tag == "Jean" and Flavor == "Inbt" and self.IX > 0:
                        #Lowers her Inbt to true levels before check
                        Type -= self.IX

                if Greater:
                        #this checks if it's greater or less than the intended value
                        #if it fails, the value is zeroed out, canceling the rest
                        if Type >= Check:
                            #If it passes the check, add Value to it
                            Type += Value
                        else:
                            #If not, don't add Value and set Value to 0
                            Value = 0
                else:
                        if Type <= Check:
                            Type += Value
                        else:
                            Value = 0

                if self.Tag == "Jean" and Flavor == "Inbt" and self.IX > 0:
                        #Raises her Inbt back to true levels after check
                        Type += self.IX

                if Value:
                    #If there is any change to the stat
                    #Sets reporting text color based on Flavor
                    if self.Tag == "Jean" and Value > 0:
                            if Flavor == "Obed" and self.Obed <= 800 and Check < 800:
                                    # if her Obedience is under 800 and the check is for less than 800,
                                    # reduces half the gains. This slows low obed farming options
                                    Value = int(Value/2)
                                    Type -= Value
                            elif Flavor == "Inbt" and self.IX > 0:
                                    if self.Taboo >= 40:
                                            # When she can't whammy people, public stuff rewards more
                                            Value += Value
                                            Type += Value
                                    if Type > 1000:
                                            # if her inhibition is maxed, further increases are removed from the IX modifier instead
                                            self.IX -= (Type - 1000)
                                            Type = 1000
                                            Value = 0
                                    elif Type > 700:
                                            # if her inhibition is just high, half the value is applied to her IX
                                            self.IX -= int(Value/2)
                                    self.IX = 0 if self.IX < 0 else self.IX
                            elif Flavor == "Love" and Type >= 500 and self.Obed < 700:
                                    #if the character is Jean, her Love stat will not raise above 500,
                                    #unless her Obedience is over 700. It does get stored up, however,
                                    #and doled out at a later date.
                                    if self.Love < 500: #and Type > 500
                                            # If her Love is just crossing 500, set it to 500 and then make Value the remainder
                                            self.Love = 500
                                            Value = Type - 500
                                    #else:
                                            #Value = (Type - self.Love) if Type > self.Love else 0
                                            ##if the combined value is higher than Love, then Value becomes the remainder

                                    self.StatStore += Value                                     #stores overflow amount for later

                                    if Check > self.Obed:
                                            #if the checked value is higher than her current Obedience
                                            Flavor = "Obed"                                     #sets the flavor to obed
                                            Value = int(Value/5)                                #sets value change as 1/5th the amount
                                            Type = self.Obed + Value                            #establishes the new change as Obed+new value, likely 1
                                    else:
                                            Value = 0
                                    #if her Obedience is over 700, Love checks just pass right through.



                    if Flavor == "Love":
                            Color = "#c11b17"
                    elif Flavor == "Obed":
                            Color = "#2554c7"
                    elif Flavor == "Inbt":
                            Color = "#FFF380"
                    elif Flavor == "Lust":
                            Color = "#FAAFBE"
                            CallHolder(Value, Color, XPOS) #show popup
                            if Flavor == "Lust" and Type >= 100 and not Trigger:
                                        #calls orgasm if Lust goes over 100, breaks routine
                                        renpy.call("Girl_Cumming",self,1)
                                        return
                            Type = 100 if Type > 100 else Type
                            setattr(self,Flavor,Type)
                            return

                    if Type > 1000:
                        CallHolder((-(Type-1000-Value)), Color, XPOS)
                        if not self.Chat[4]:
                            #if no overflow mechanic is prepared. . .
                            Value = 0
                        else:
                            #if the value overflows, play one value meter, then. . .
                            Value = Type - 1000
                            # change the Flavor to the new thing if there is a swap happening
                            setattr(self,Flavor,1000)
                            if Flavor == "Love":
                                    if self.Chat[4] == 1:       #[Love to Obedience]
                                        Flavor = "Obed"
                                    elif self.Chat[4] == 2:     #[Love to Inhibition]
                                        Flavor = "Inbt"
                                    else:
                                        Value = 0
                            elif Flavor == "Obed":
                                    if self.Chat[4] == 3:       #[Obedience to Inhibition]
                                        Flavor = "Inbt"
                                    elif self.Chat[4] == 4:
                                        Flavor = "Love"   #[Obedience to Love]
                                    else:
                                        Value = 0
                            elif Flavor == "Inbt":
                                    if self.Chat[4] == 5:       #[Inhibition to Obedience]
                                        Flavor = "Obed"
                                    elif self.Chat[4] == 6:
                                        Flavor = "Love"    #[Inhibition to Love]
                                    else:
                                        Value = 0

                            Type = getattr(self,Flavor)
                            Type += Value

                            if Flavor == "Love":
                                    #Sets reporting text color based on Flavor
                                    Color = "#c11b17"
                            elif Flavor == "Obed":
                                    Color = "#2554c7"
                            elif Flavor == "Inbt":
                                    Color = "#FFF380"
                            else:
                                    Color = "#FFFFFF"
                    #end Type change element

                    if Value:
                            # show pop-up
                            CallHolder(Value, Color, XPOS)

                #end "if value is positive"

                Type = 1000 if Type > 1000 else Type

                setattr(self,Flavor,Type)
                return
        #End Statup

        def FaceChange(self, Emote = 5, B = 5, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
                # $ RogueX.FaceChange("sadside",1,Mouth="smile")
                # Emote is the chosen emote, B is the lush state,
                # M is whether the character is in a  manic state
                Emote = self.Emote if Emote == 5 else Emote
                #B = 5, M = 0, Mouth = 0, Eyes = 0, Brows = 0
                B = self.Blush if B == 5 else B
#                $ Mouth = 0 if Mouth == None else Mouth
#                $ Eyes = 0 if Eyes == None else Eyes
#                $ Brows = 0 if Brows == None else Brows
                if (self.Forced or "angry" in self.RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                        Emote = "angry"
                elif self.ForcedCount > 0 and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                        Emote = "sad"

                if Emote == "normal":
                        self.Mouth = "normal"
                        self.Brows = "normal"
                        self.Eyes = "normal"
                elif Emote == "angry":
                        if self is LauraX:
                                self.Mouth = "kiss"
                        else:
                                self.Mouth = "sad"
                        self.Brows = "angry"
                        self.Eyes = "sexy"
                elif Emote == "bemused":
                        if self is EmmaX:
                                self.Mouth = "normal"
                        else:
                                self.Mouth = "lipbite"
                        self.Brows = "sad"
                        self.Eyes = "squint"
                elif Emote == "closed":
                        if self is RogueX:
                                self.Mouth = "lipbite"
                        else:
                                self.Mouth = "normal"
                        self.Brows = "sad"
                        self.Eyes = "closed"
                elif Emote == "confused":
                        self.Mouth = "kiss"
                        self.Brows = "confused"
                        if self is LauraX or self is EmmaX:
                                self.Eyes = "squint"
                        else:
                                self.Eyes = "surprised"
                elif Emote == "kiss":
                        self.Mouth = "kiss"
                        if self is LauraX or self is EmmaX:
                                self.Brows = "sad"
                        else:
                                self.Brows = "normal"
                        self.Eyes = "closed"
                elif Emote == "sad":
                        self.Mouth = "sad"
                        self.Brows = "sad"
                        if self is JeanX or self is JubesX:
                                self.Eyes = "normal"
                        else:
                                self.Eyes = "sexy"
                elif Emote == "sadside":
                        self.Mouth = "sad"
                        self.Brows = "sad"
                        self.Eyes = "side"
                elif Emote == "sexy":
                        self.Mouth = "lipbite"
                        if self is EmmaX:
                                self.Brows = "normal"
                                self.Eyes = "squint"
                        elif self is LauraX:
                                self.Brows = "sad"
                                self.Eyes = "squint"
                        else:
                                self.Brows = "normal"
                                self.Eyes = "sexy"
                elif Emote == "sly":
                        self.Brows = "normal"
                        self.Eyes = "squint"
                        if self is RogueX:
                                self.Mouth = "grimace"
                        if self is LauraX:
                                if LauraX.Love >= 700:
                                    self.Mouth = "smile"
                                else:
                                    self.Mouth = "smirk"
                                self.Brows = "confused"
                        elif self is KittyX:
                                self.Mouth = "smile"
                        else:
                                self.Mouth = "smirk"
                elif Emote == "smile":
                        if self is LauraX and LauraX.Love < 700:
                                self.Mouth = "smirk"
                        else:
                                self.Mouth = "smile"
                        self.Brows = "normal"
                        self.Eyes = "normal"
                elif Emote == "surprised":
                        if self is RogueX or self is KittyX:
                                self.Mouth = "surprised"
                        else:
                                self.Mouth = "kiss"
                        self.Brows = "surprised"
                        self.Eyes = "surprised"
                elif Emote == "startled":
                        if self is RogueX or self is KittyX:
                                self.Mouth = "grimace"
                        else:
                                self.Mouth = "smile"
                        self.Brows = "surprised"
                        self.Eyes = "surprised"
                elif Emote == "down":
                        if self is RogueX or self is KittyX:
                                self.Mouth = "surprised"
                        else:
                                self.Mouth = "sad"
                        self.Brows = "sad"
                        self.Eyes = "down"
                elif Emote == "perplexed":
                        if self is RogueX:
                                self.Mouth = "sad"
                                self.Brows = "confused"
                        else:
                                self.Mouth = "smile"
                                self.Brows = "sad"
                        if self is LauraX:
                                self.Eyes = "surprised"
                        else:
                                self.Eyes = "normal"
                elif Emote == "sucking":
                        self.Mouth = "sucking"
                        if self is EmmaX:
                                self.Brows = "surprised"
                        elif self is LauraX:
                                self.Brows = "sad"
                        else:
                                self.Brows = "normal"
                        self.Eyes = "closed"
                elif Emote == "tongue":
                        self.Mouth = "tongue"
                        self.Brows = "sad"
                        if self == LauraX:
                                self.Eyes = "stunned"
                        else:
                                self.Eyes = "sexy"
                elif Emote == "manic":
                        if self is RogueX:
                                self.Mouth = "grimace"
                        elif self is LauraX:
                                self.Mouth = "lipbite"
                        else:
                                self.Mouth = "smile"
                        self.Brows = "sad"
                        self.Eyes = "manic"
                        self.Blush = 1
                elif Emote == "grimace":
                        if self is RogueX or self is KittyX:
                                self.Mouth = "grimace"
                        else:
                                self.Mouth = "smile"
                        self.Brows = "sad"
                        self.Eyes = "normal"

                if M:
                        self.Eyes = "manic"
                if B > 1:
                        self.Blush = 2
                elif B:
                        self.Blush = 1
                else:
                        self.Blush = 0

                if Mouth:
                        self.Mouth = Mouth
                if Eyes:
                        self.Eyes = Eyes
                if Brows:
                        self.Brows = Brows
                return
        # End Face Change / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        def DefaultFaces(self):
                #This sets a default face for the girl
                #was "call Faces"
                # $ RogueX.DefaultFaces()
                if self.Lust >= 50 and ApprovalCheck(self, 1200):
                        self.Emote = "sexy"
                elif self.Addict > 75:
                        self.Emote = "manic"
                elif self.Love >= self.Obed and self.Love >= 500:
                        self.Emote = "smile"
                elif self.Inbt >= self.Obed and self.Inbt >= 500:
                        self.Emote = "smile"
                elif self.Addict > 50:
                        self.Emote = "manic"
                elif (self.Love + self.Obed) < 300:
                        self.Emote = "angry"
                else:
                        self.Emote = "normal"
                return

        def LustFace(self,Extreme=0,Kissing=0):
                if self.Thirst >= 80:
                        self.Lust += 2
                elif self.Thirst >= 50:
                        self.Lust += 1

                if self.Lust >= 80:
                        self.Blush = 2
                elif self.Lust >= 40:
                        self.Blush = 1

                if self.Lust >= 80:
                        self.Wet = 2
                elif self.Lust >= 50:
                        self.Wet = 1

                if self.Offhand == "kiss both" or self.Offhand == "kiss girl":
                        #if the girls are kissing or all three are
                        Kissing = 1
                elif Partner != self:
                        #If the called girl is kissing and is primary
                        if Trigger == "kiss you" or Trigger2 == "kiss you":
                            Kissing = 1

                if Kissing:
                        self.Eyes = "closed"
                        if self.Tag == "Emma":
                            self.Mouth = "kiss"
                        elif self.Kissed >= 10 and self.Inbt >= 300:
                            self.Mouth = "sucking"
                        elif self.Kissed > 1 and self.Addict >= 50:
                            self.Mouth = "sucking"
                        else:
                            self.Mouth = "kiss"
                else:
                        #If called girl is not kissing someone
                        if self.Lust >= 90:
                                self.Eyes = "closed"
                                self.Brows = "sad"
                                self.Mouth = "surprised"
                        elif self.Lust >= 70 or Extreme:
                                self.Eyes = "sexy"
                                self.Brows = "sad"
                                self.Mouth = "lipbite"
                        elif self.Lust >= 50:
                                if self.Tag == "Emma" or self.Tag == "Laura":
                                        self.Eyes = "squint"
                                else:
                                        self.Eyes = "sexy"
                                self.Brows = "sad"
                                self.Mouth = "lipbite"
                        elif self.Lust >= 30:
                                self.Eyes = "sexy"
                                self.Brows = "normal"
                                if self.Tag == "Emma" or self.Tag == "Laura":
                                        self.Mouth = "smirk"
                                else:
                                        self.Mouth = "kiss"
                        else:
                                self.Eyes = "sexy"
                                self.Brows = "normal"
                                if self.Tag == "Emma" or self.Tag == "Laura":
                                        self.Mouth = "smirk"
                                else:
                                        self.Mouth = "normal"
                        if self.Tag == "Laura" and self.Lust < 50 and not Extreme and not ApprovalCheck(self, 1000):
                                self.Eyes = "side"

                if self.Offhand == "lick pussy" or self.Offhand == "lick ass" or self.Offhand == "suck breasts":
                                self.Mouth = "tongue"

                if self.OCount >= 10:
                        #If you've fucked her senseless
                        self.Eyes = "stunned"
                        self.Mouth = "tongue"

                if not self.Loose:
                        #if anal hurts. . .
                        if Partner != self and (Trigger == "anal" or Trigger == "dildo anal" or self.Offhand == "dildo anal"):
                            self.Eyes = "closed"
                            self.Brows = "angry"

                if "unseen" in self.RecentActions:
                        self.Eyes = "closed"
                if Partner and self != Partner:
                        Partner.LustFace()
                return

        # End Lust Face / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        def OutfitChange(self, OutfitTemp = 5, Spunk = 0, Undressed = 0, Changed = 1,HolderOutfit=[]): #rkeljsvgb
                # $ RogueX.OutfitChange("casual1")
                # OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed
                #OutfitTemp = self.Outfit if not OutfitTemp else OutfitTemp
                if self not in TotalGirls: #should remove "character don't exist" errors
                        return

                OutfitTemp = OutfitTemp if OutfitTemp else self.Outfit

                if self.Loc == bg_current and renpy.showing("NightMask", layer='nightmask') and Time_Count == 0: #morning time
                        #Skips this check if it's a sleepover
                        return

                if self.Loc not in ("bg showerroom","bg pool") or (OutfitTemp not in ("nude","swimwear","towel")):
                        #Dries her off
                        self.Water = 0
                if self.Spunk:
                        #Removes spunk if told to do so.
                        if "painted" not in self.DailyActions or "cleaned" not in self.DailyActions:
                            del self.Spunk[:]

                #Resets "half-dressed" states
                if self.Upskirt or self.Uptop or self.PantiesDown:
                        Undressed = 1

                self.Upskirt = 0
                self.Uptop = 0
                self.PantiesDown = 0

                if OutfitTemp == 5:
                        #this sets it to default if using AnyOutfit
                        if "yoinked" in self.RecentActions:
                                #if Kitty's yoinked her clothes, don't replace them
                                return
                        OutfitTemp = self.Outfit
                elif OutfitTemp == 6:
                        #this sets it to daily default if using AnyOutfit
                        OutfitTemp = self.OutfitDay
                        self.Outfit = self.OutfitDay
                if OutfitTemp != self.Outfit:
                        #if her new outfit is not what she was wearing before,
                        #don't flag the undressed mechanic
                        Changed = 1
                        self.Outfit = OutfitTemp
#                if self in Party and OutfitTemp == self.OutfitDay:
#                        #this ignores her daily outfit if she's in a party
#                        OutfitTemp = self.Outfit

                if OutfitTemp == "casual1":
                        HolderOutfit = self.Casual1[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "casual2":
                        HolderOutfit = self.Casual2[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "casual3":
                        HolderOutfit = self.Casual3[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "nude":
                        HolderOutfit = [0,0,0,0,0,0,0,0,0,0,50,0,0] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "towel":
                        HolderOutfit = [0,0,0,"towel",0,0,0,0,0,0,35,0,0] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "custom1":
                        HolderOutfit = self.Custom1[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "custom2":
                        HolderOutfit = self.Custom2[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "custom3":
                        HolderOutfit = self.Custom3[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "temporary":
                        HolderOutfit = self.TempClothes[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "sleep":
                        HolderOutfit = self.Sleepwear[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "gym":
                        HolderOutfit = self.Gym[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "costume":
                        HolderOutfit = self.Costume[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "costume2":
                        HolderOutfit = self.Costume2[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "swimwear":
                        if not self.Swim[0]:
                                if self is BetsyX and "swimsuit" in self.Inventory:
                                        self.Swim[0] = 1
                                elif "bikini top" not in self.Inventory or "bikini bottoms" not in self.Inventory:
                                        self.Outfit = self.OutfitDay
                                        #if she doesn't own her swimsuit components. . .
                                        if "swim" not in self.DailyActions:
                                                if self is RogueX:
                                                    ch_r("Если честно, мне нечего надеть. . .", interact=True)
                                                elif self is KittyX:
                                                    ch_k("Хотела бы я надеть что-нибудь милое, но у меня ничего нет. . .", interact=True)
                                                elif self is EmmaX:
                                                    ch_e("На самом деле, у меня нет подходящей одежды. . .", interact=True)
                                                elif self is LauraX:
                                                    ch_l("У меня нет купальника. . .", interact=True)
                                                elif self is JeanX:
                                                    ch_j("Я могла бы составить тебе компанию, если бы ты купил мне купальник. . .", interact=True)
                                                elif self is StormX:
                                                    ch_s("Боюсь, Чарльз захочет, чтобы я надела купальник. . .", interact=True)
                                                elif self is JubesX:
                                                    ch_v("Я еще не подобрала купальник. . .", interact=True)
                                                elif self is GwenX:
                                                    ch_g("Ох, эм, у меня нет купальника. . .", interact=True)
                                                elif self is BetsyX:
                                                    ch_b("Боюсь, я забыла взять с собой купальник. . .", interact=True)
                                                elif self is DoreenX:
                                                    ch_d("У меня нет купальника. . .", interact=True)
                                                elif self is WandaX:
                                                    ch_w("Прости, у меня нет купальника. . .", interact=True)
                                        return 0
                                elif self is KittyX and "blue skirt" not in self.Inventory and self.Inbt <= 400:
                                        self.Outfit = self.OutfitDay
                                        if "swim" not in self.DailyActions:
                                                    ch_k("Не знаю, у меня есть купальник, но он немного вызывающий. . .", interact=True)
                                                    ch_k("Если бы только у меня была юбочка или что-то типа того. . .", interact=True)
                                        return 0
                                else:
                                    self.Swim[0] = 1
                        HolderOutfit = self.Swim[:] #fills Holder with the values of the sent uni. . .
                #end Holder setting. . .
                while len(HolderOutfit) < 13:
                    HolderOutfit.append(0)

                if not self.Legs and HolderOutfit[2]:
                    Undressed = 1
                elif not self.Over and HolderOutfit[3]:
                    Undressed = 1
                elif not self.Chest and HolderOutfit[5]:
                    Undressed = 1
                elif not self.Panties and HolderOutfit[6] and "pantyless" not in self.DailyActions:
                    Undressed = 1
                elif not self.Hose and HolderOutfit[9]:
                    Undressed = 1

                #renpy.say(None, HolderOutfit[2], interact=True) #fix remove

#                if self == EmmaX and (HolderOutfit[8] != "hat" and HolderOutfit[8] != "hat wet"):
#                        #returns Emma's hair to default form if she's not deliberately wearing a hat
#                        self.Hair = "wet" if HolderOutfit[8] == "hat wet" else "wave"

                self.Arms = HolderOutfit[1]
                self.Legs = HolderOutfit[2]
                self.Over = HolderOutfit[3]
                self.Neck = HolderOutfit[4]
                self.Chest = HolderOutfit[5]
                self.Panties = HolderOutfit[6]
                self.Acc = HolderOutfit[7]
                self.Hair = HolderOutfit[8] if HolderOutfit[8] else self.Hair
                self.Hose = HolderOutfit[9]
                self.Shame = HolderOutfit[10]
                self.Boots = HolderOutfit[11]
                self.Hat = HolderOutfit[12]

                self.Arms_key = HolderOutfit[1] if HolderOutfit[1] != 0 else None
                self.Legs_key = HolderOutfit[2] if HolderOutfit[2] != 0 else None
                self.Over_key = HolderOutfit[3] if HolderOutfit[3] != 0 else None
                self.Neck_key = HolderOutfit[4] if HolderOutfit[4] != 0 else None
                self.Chest_key = HolderOutfit[5] if HolderOutfit[5] != 0 else None
                self.Panties_key = HolderOutfit[6] if HolderOutfit[6] != 0 else None
                self.Acc_key = HolderOutfit[7] if HolderOutfit[7] != 0 else None
                self.Hose_key = HolderOutfit[9] if HolderOutfit[9] != 0 else None
                self.Boots_key = HolderOutfit[11] if HolderOutfit[11] != 0 else None
                self.Hat_key = HolderOutfit[12] if HolderOutfit[12] != 0 else None

                if "ripped" in self.DailyActions and "modesty" not in self.RecentActions:
                        #this keeps her in ripped hose all day if they are ripped off her
                        self.Hose = "ripped pantyhose" if self.Hose == "pantyhose" else self.Hose
                        self.Hose = "ripped tights" if self.Hose == "tights" else self.Hose
                if self.Panties and self.Panties != "shorts" and "pantyless" in self.DailyActions and "modesty" not in self.DailyActions:
                        # This checks the pantyless state from flirting
                        if OutfitTemp != "sleep" and OutfitTemp != "gym":
                                self.Panties = 0
        #                renpy.call(OutfitShame,self,0,1)
                        #make sure that this element accurately checks to decide whether she would wear this outfit with or without panties.

                if not Changed and OutfitTemp == self.Outfit and self.Loc == bg_current:
                        #If she was partially dressed then it says she gets dressed
                        if Undressed == 2:
                                renpy.say(None,self.Name+" заматывается в полотенце.", interact=True)
                        elif Undressed:
                                renpy.say(None,self.Name+" надевает обратно свою одежду.", interact=True)
                if Undressed:
                    return 2
                return 1
                #End Outfits

        # End Outfits / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        def Set_Temp_Outfit(self):
                    # This takes whatever the girl is wearing, and sets it as the temporary outfit
                    # $ RogueX.Set_Temp_Outfit()
                    self.TempClothes[1] = self.Arms
                    self.TempClothes[2] = self.Legs
                    self.TempClothes[3] = self.Over
                    self.TempClothes[4] = self.Neck
                    self.TempClothes[5] = self.Chest
                    self.TempClothes[6] = self.Panties
                    self.TempClothes[7] = self.Acc
                    self.TempClothes[8] = self.Hair
                    self.TempClothes[9] = self.Hose
                    self.TempClothes[11] = self.Boots
                    self.TempClothes[12] = self.Hat
                    self.TempClothes[0] = 1

                    #self.TempClothes = [1,self.Arms,self.Legs,self.Over,self.Neck,self.Chest,self.Panties,self.Acc,self.Hair,self.Hose,0]

                    self.Outfit = "temporary"
                    self.OutfitDay = "temporary"
                    return

        def ChestNum(self,Up=1):  #rkeljsvgbdw
                    #This function determines how much Bra are on, 5 for decent, less for less.
                    if Up and self.Uptop and self.Chest:
                            return 1
                    if self.Chest == "sports bra":
                        return 5
                    if self.Chest == "saiyan leotard" or self.Chest == "cammy leotard" or self.Chest == "raven leotard":
                        return 5
                    if self.Chest == "tube top" or self.Chest == "tank":
                        return 5
                    if self.Chest == "lace bra":
                        return 2
                    if self.Chest == "lace corset":
                        return 2
                    if self.Chest == "corset":
                        return 5
                    if self.Chest in ("tank","buttoned tank"):
                        return 5
                    if self.Chest in ("leather bra","white tank"):
                        return 5
                    if self.Chest == "wolvie top":
                        return 3
                    if self.Chest == "mesh top":
                        return 2
                    if self.Chest:
                        return 3
                    if self.Acc == "suspenders" or self.Acc == "suspenders2":
                        return 2
                    #if it falls though. . .
                    return 0

        def OverNum(self,Up=1):  #rkeljsvgbdw
                    #This function determines how much Over are on, 5 for decent, less for less.
                    if Up and self.Uptop and self.Over:
                            return 1
                    if self is JubesX:
                            if Up and self.Uptop and self.Acc:
                                return 1
                            if self.Acc and self.Over:
                                return 5
                            if self.Over == "saiyan armor":
                                return 5
                            if self.Acc == "jacket":
                                return 3
                            if self.Acc == "open jacket":
                                return 1
                            if self.Acc == "shut jacket":
                                return 5
                    if self.Over == "towel":
                        if self is StormX:
                            return 0
                        elif self is EmmaX:
                            return 2
                        else:
                            return 3
                    if self.Legs == "dress" and Up and not self.Uptop:
                        return 5
                    if self.Over == "dress":
                        return 5
                    if self.Over == "jacket":
                        return 4
                    if self.Over == "nighty":
                        return 3
                    if self.Over == "pink top":
                        return 4
                    if self.Over == "mesh top":
                        return 2
                    if self.Over == "open suit":
                        return 1

                    if self.Over:
                        return 5
                    #if it falls though. . .
                    return 0

        def PantsNum(self,Up=1,Pantscount=0):  #rkeljsvgbdw
                    #This function determines how much pants are on, 10 for pants, 6 for shorts, 5 for skirt, <5 for non-covering.
                    # Up defaults to 1 and returns 1 if in Upskirt mode, but will skip that check of Up is 0

                    if Up and self.Upskirt:
                            if self.Legs or self.Acc == "shut jacket" or self.Over == "dress" or self.Over == "towel":
                                return 1
                            return 0

                    if self is JubesX and (self.Acc == "shut jacket" or self.Over == "dress"):
                                Pantscount = 5 if Pantscount <= 5 else Pantscount
                    if self is EmmaX and self.Over == "dress":
                                Pantscount = 4 if Pantscount <= 4 else Pantscount
                    if self.Over == "towel" and self not in (EmmaX,StormX):
                                Pantscount = 5 if Pantscount <= 5 else Pantscount

                    if self.Legs in ("skirt","blue skirt","other skirt","dress","cheer skirt","red skirt"):
                                Pantscount = 5 if Pantscount <= 5 else Pantscount
                    elif self.Legs == "shorts" or self.Panties == "shorts":
                                Pantscount = 6 if Pantscount <= 6 else Pantscount
                    elif self.Legs == "yoga pants":
                                Pantscount = 8 if Pantscount <= 8 else Pantscount
                    elif self.Legs == "mesh pants":
                                Pantscount = 2 if Pantscount <= 2 else Pantscount
                    elif self.Legs: #pants, mostly
                                Pantscount = 10 if Pantscount <= 10 else Pantscount

                    #if it falls though. . .
                    return Pantscount

        def PantiesNum(self,Up=1):  #rkeljsvgbdw
                    #This function determines how much panties are on, 5 for decent, less for less.
                    if Up and self.PantiesDown and self.Panties:
                        return 1
                    if self.Panties == "lace panties":
                        return 2
                    if self.Panties == "sports panties" or self.Panties == "shorts":
                        return 8
                    if self.Panties == "bikini bottoms" or self.Panties == "swimsuit":
                        return 7
                    if self.Panties:
                        return 4
                    return 0

        def HoseNum(self,Up=1): #rkeljsvgbdw
                    #This function determines how seethrough her hose is, 5 for "visible," 10 for "solid"
                    if Up and self.Hose and (self.PantiesDown or self.Upskirt):
                        return 1
                    if self.Hose == "stockings":
                        return 1
                    if self.Hose == "pantyhose":
                        return 6
                    if self.Hose == "tights":
                        return 10
                    if self.Hose == "stockings and garterbelt":
                        return 4
                    if self.Hose == "ripped pantyhose":
                        return 4
                    if self.Hose == "ripped tights":
                        return 4
                    #if it falls though. . .
                    return 0

        def ClothingCheck(self,C = 0):
                    C = 0
                    #This function counts how many items of clothing she has on and returns that number.
                    if self.OverNum() >= 5: #if her top is
                        C += 1
                    if self.Chest:
                        C += 1
                    if self.Legs:
                        C += 1
                    if self.HoseNum() >= 5: #double check this one. . .
                        C += 1
                    if self.Panties:
                        C += 1
                    return C

        def ModestyCheck(self, Check=0,C = 0):
                    C = 0
                    #This function determines whether they are partially nude or not.
                    #if Check is 0, check both, if it's 1, check top, if it's 2, check bottom only
                    if Check == 2:
                        pass                    #skips if only checking bottoms
                    elif self.OverNum() >= 3:   #if her top is fine
                        pass
                    elif self.ChestNum() >= 3:
                        pass
                    else:
                        C += 1

                    if Check == 1:
                        pass                    #skips if only checking tops
                    elif self.PantsNum() >= 5 and self.Legs != "short skirt":
                        pass
                    elif self.PantiesNum() >= 4:
                        pass
                    elif self.HoseNum() >= 5:
                        pass
                    else:
                        C += 1
                    return C

        def SeenCheck(self, Check=0, C = 0):
                    C = 0
                    #This function returns 1-2 if she is partially naked and this is the first the player's seen of it.
                    # "Check" is 1 if it's intended to see whether she has been seen at all.
                    # "Check" is 2 if it's intended to see whether she has been seen topless.
                    # "Check" is 3 if it's intended to see whether she has been seen bottomless.
                    if not self.SeenChest:
                        if (not self.Over and not self.Chest) or self.Uptop or Check == 1 or Check == 2:
                                    C += 1
                    if not self.SeenPussy:
                        if Check == 1 or Check == 3:
                                    C += 1
                        elif not self.Legs or self.Upskirt or self.Legs == "short skirt":
                            #if no pants or pants down
                            if self.PantiesDown or (self.HoseNum() < 5 and not self.Panties):
                                    # if no panties and loose hose or they're down
                                    C += 1
                    return C
        # End Clothing Checks / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


        # Girl interactions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        def GirlLikeCheck(self,Chr=0):
                # RogueX.GirlLikeCheck(KittyX) will return RogueX.LikeKitty, ie 600
                return getattr(self,"Like"+Chr.Tag)

        def GirlLikeUp(self,Chr=0,Value=0,Like=0):
                # RogueX.GirlLikeUp(KittyX,5) will return RogueX.LikeKitty += 5
                if "Jeaned" in self.Traits:
                        #if Jean has messed with their stats, change the stored value instead
                        Like = getattr(JeanX,"LikeS"+self.Tag) #Like = RogueX.LikeKitty
                        if Like + Value > 1000:
                                setattr(JeanX,"LikeS"+self.Tag, 1000)
                        elif Like + Value < 0:
                                setattr(JeanX,"LikeS"+self.Tag, 0)
                        else:
                                setattr(JeanX,"LikeS"+self.Tag, Value + Like) #RogueX.LikeKitty = RogueX.LikeKitty + Value
                        return

                Like = getattr(self,"Like"+Chr.Tag) #Like = RogueX.LikeKitty
                if Like + Value > 1000:
                        setattr(self,"Like"+Chr.Tag, 1000)
                elif Like + Value < 0:
                        setattr(self,"Like"+Chr.Tag, 0)
                else:
                        setattr(self,"Like"+Chr.Tag, Value + Like) #RogueX.LikeKitty = RogueX.LikeKitty + Value
                return

        def GLG(self, ChrB = 0, Check=200, Modifier = 1, Auto = 0, Jealousy = 0, Ok = 0, Likes=0):
                # self is the subject girl, ChrB is the object girl,
                # Modifier is sent as the amount of offense this might cause,
                # Jealousy is the temp value for how mad the girl will get
                # Likes stores the XLikesY stat temporarily
                # Auto quickly raises lust and like by a sent amount
                # returns 2 if very into it, 1 if ok with it, 0 if not cool with it.

                # was call GirlLikesGirl(Party[0],Party[1],700,5,1)
                # now $ RogueX.GLG(Party[1],700,5,1)
                if self not in TotalGirls or ChrB not in TotalGirls: #should remove "character don't exist" errors
                        return
                Jealousy = 0
                Likes = self.GirlLikeCheck(ChrB)
                #stores this value temporarily

                if Likes <= Check:
                        #if the checked girl likes the second girl less than the checked value. . .
                        if Auto:
                                #if set to auto, just raises the Like stat by the modifier value.
                                setattr(self,"Like"+ChrB.Tag,Likes+Modifier) #updates Like modifier
                                self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5th modifier
                                return

                        # checks if they have agreed to share or not
                        if self in Player.Harem:
                                #if "dating" in RogueX.Traits or RogueX in Player.Harem:
                                if ChrB not in Player.Harem and "poly " + ChrB.Tag not in self.Traits:
                                        # if KittyX not in Player.Harem and "poly Kitty" not in RogueX.Traits:
                                        Jealousy = 100
                elif Auto: #this is a quick return,
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5th modifier
                            return

                #Establishes how jealous lead is likely to get
                Jealousy += (self.Love - 600) if self.Love > 600 else 0
                        #How much her Love stat is over 600, +0-400
                Jealousy += self.SEXP if self.Inbt <= 500 else 0
                        #plus her SexP rating if she has low inhibitions, +0-200
                Jealousy -= (self.Obed - 250) if self.Obed > 250 else 0
                        #minus how much her Obed stat is over 250, -0-750
                        # = result of up to 700 if high love, dating, and low obedience

                Jealousy = 0 if Jealousy < 1 else Jealousy
                    #Balances it to no less than zero
                Modifier += 1 if not Jealousy and Likes >= 500 else 0
                    #+ modifier if she doesn't hate Kitty but has no jealousy left


                if Likes >= 900:
                            #If she really likes the girl, then she is turned on, likes both of you more.
                            Likes += Modifier
                            self.Statup("Love", 80, (int(Modifier/2))) #raises Love by 1/2 modifier
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5 modifier
                            Ok = 2
                elif Likes >= 800:
                        #If she mostly likes the girl, and is not super jealous, she likes you both more.
                        if Jealousy <= 300:
                            Likes += Modifier
                            self.Statup("Love", 80, (int(Modifier/2))) #raises Love by 1/2 modifier
                            self.Statup("Lust", 200, (int(Modifier/2))) #raises Lust by 1/2 modifier
                            Ok = 2
                        else:
                            Likes -= Modifier
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5 modifier
                            Ok = 1
                elif Likes >= 600:
                        #If she's friends with the girl, only low jealousy is positive
                        if Jealousy <= 100:
                            Likes += Modifier
                            self.Statup("Love", 80, (int(Modifier/4))) #raises Love by 1/4 modifier
                            self.Statup("Lust", 200, (int(Modifier/2))) #raises Lust by 1/2 modifier
                            Ok = 2
                        elif Jealousy <= 300:
                            Likes -= Modifier
                            self.Statup("Lust", 200, (int(Modifier/2))) #raises Lust by 1/5 modifier
                            Ok = 1
                        else:
                            Likes -= (Modifier + (int(Jealousy/50)))
                            self.Statup("Love", 90, (-(int(Modifier)))) #lowers Love by 1/2 modifier
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5 modifier
                            Ok = 2
                elif Likes >= 400:
                        #If she is neutral to the girl, it's all negative
                        if Jealousy <= 100:
                            Likes -= Modifier
                            Ok = 1
                        else:
                            Likes -= (Modifier + (int(Jealousy/100)))
                        self.Statup("Lust", 200, (int(Modifier/10))) #raises Lust by 1/10 modifier
                else:
                        #If she hates the girl, it's all very negative
                        Likes -= (Modifier + (int(Jealousy/50)))
                        self.Statup("Lust", 200, (int(Modifier/10))) #raises Lust by 1/5 modifier
                self.Statup("Inbt", 60, (int(Modifier/10))) #raises Inbt by 1/10 modifier

                # restores "likes" to target character.

                setattr(self,"Like"+ChrB.Tag,Likes+Modifier) #updates Like modifier

                return Ok
                # returns 2 if very into it, 1 if ok with it, 0 if not cool with it.
        # End Girl Like girl stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


        def NameCheck(self, Cnt = 0): #rkeljsvg
                #Checks how she reacts to you using her petname
                #Cnt and Ugh are internal count variable
                # $ RogueX.NameCheck() #nee
                if self.Pet == self.Name:
                        return 0
                if self.Taboo:
                        # +4 if Taboo 40, +2 if Taboo 20
                        Cnt = int(self.Taboo/10)

                #easy options
                if self.Pet in ("girl","boo","bae","baby","sweetie","моя девушка","детка","крошка","малышка","милая"):
                        if ApprovalCheck(self, 500, "L", TabM=1,Alt=[[LauraX],600]):
                            self.Statup("Love", 80, 1)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                elif self.Pet in ("sexy","lover","beloved","секси","любимая","возлюбленная"):
                        if ApprovalCheck(self, 900, TabM=1,Alt=[[LauraX],1100]):
                            self.Statup("Love", 80, 2)
                            self.Statup("Obed", 80, 1)
                            self.Statup("Inbt", 70, 1)
                        else:
                            self.Statup("Love", 50, (-1-Cnt))
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                #tougher options
                elif self.Pet == "slave" or self.Pet == "рабыня":
                        if ApprovalCheck(self, 800, "O", TabM=3,Alt=[[EmmaX,StormX],900]):
                            self.Statup("Lust", 90, (3+Cnt))
                            self.Statup("Obed", 95, (2+Cnt))
                            self.Statup("Inbt", 30, 1)
                            self.Statup("Inbt", 70, 1)
                        elif ApprovalCheck(self, 500, "O", TabM=3,Alt=[[EmmaX,StormX],600]):
                            self.Statup("Lust", 90, 1)
                            self.Statup("Love", 200, -1)
                            self.Statup("Obed", 80, 2)
                            self.Statup("Inbt", 70, 1)
                        else:
                            self.Statup("Love", 200, -2)
                            self.Statup("Love", 50, -1, 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 50, -1)
                            return 1
                elif self.Pet == "pet" or self.Pet == "питомец":
                        if ApprovalCheck(self, 1500, TabM=2,Alt=[[LauraX],800]):
                            self.Statup("Lust", 90, (3+Cnt))
                            self.Statup("Obed", 95, (2+Cnt))
                            self.Statup("Inbt", 30, 1)
                            self.Statup("Inbt", 70, 1)
                        elif ApprovalCheck(self, 1200, TabM=2,Alt=[[LauraX],650]):
                            self.Statup("Lust", 60, 1)
                            self.Statup("Obed", 80, 2)
                            self.Statup("Inbt", 70, 1)
                        else:
                            self.Statup("Love", 200, -2)
                            self.Statup("Love", 50, -1, 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 50, -1)
                            return 1
                elif self.Pet == "slut" or self.Pet == "шлюха":
                        if ApprovalCheck(self, 500, "O", TabM=2) or ApprovalCheck(self, 500, "I", TabM=2,Alt=[[LauraX],400]):
                            self.Statup("Lust", 90, (4+Cnt))
                            self.Statup("Obed", 95, (2+Cnt))
                            self.Statup("Inbt", 40, 2)
                            self.Statup("Inbt", 80, 1)
                        elif ApprovalCheck(self, 300, "O", TabM=2) or ApprovalCheck(self, 300, "I", TabM=2,Alt=[[LauraX],200]):
                            self.Statup("Lust", 90, 1)
                            self.Statup("Love", 200, (-1-Cnt))
                            self.Statup("Obed", 80, (2+Cnt))
                            self.Statup("Inbt", 70, 1)
                        else:
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Love", 50, (-1-Cnt), 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                elif self.Pet == "whore" or self.Pet == "блядь":
                        if ApprovalCheck(self, 600, "O", TabM=2,Alt=[[EmmaX],700]) or ApprovalCheck(self, 600, "I", TabM=2,Alt=[[LauraX],400]):
                            self.Statup("Lust", 90, 4)
                            self.Statup("Obed", 95, 2)
                            self.Statup("Inbt", 50, 2)
                            self.Statup("Inbt", 80, 1)
                        elif ApprovalCheck(self, 400, "O", TabM=2,Alt=[[EmmaX],500]) or ApprovalCheck(self, 400, "I", TabM=2):
                            self.Statup("Lust", 90, 1)
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Obed", 80, 2)
                            self.Statup("Inbt", 70, 1)
                        else:
                            self.Statup("Love", 200, (-3-Cnt))
                            self.Statup("Love", 50, (-2-Cnt), 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 21, 1, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                elif self.Pet == "sugartits" or self.Pet == "сладкогрудая":
                        if ApprovalCheck(self, 1500, TabM=1,Alt=[[EmmaX],1300]):
                            self.Statup("Obed", 80, 1)
                            self.Statup("Obed", 50, 2)
                            self.Statup("Inbt", 70, 1,Alt=[[EmmaX],70,2])
                            self.Statup("Inbt", 30, 2,Alt=[[KittyX],60,3])
                        else:
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Love", 50, (-1-Cnt))
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                elif self.Pet == "sex friend" or self.Pet == "любовница":
                        if ApprovalCheck(self, 750, "O", TabM=1) or ApprovalCheck(self, 600, "I", TabM=1):
                            self.Statup("Lust", 90, 3)
                            self.Statup("Obed", 95, 2)
                            self.Statup("Inbt", 40, 2)
                            self.Statup("Inbt", 80, 1)
                        elif ApprovalCheck(self, 600, "O", TabM=1) or ApprovalCheck(self, 400, "I", TabM=1):
                            self.Statup("Lust", 90, 2)
                            self.Statup("Love", 200, (-1-Cnt))
                            self.Statup("Obed", 80, 1)
                            self.Statup("Inbt", 70, 1)
                            self.Blush = 1
                        else:
                            self.Statup("Love", 200, -Cnt)
                            self.Statup("Love", 50, (-1-Cnt), 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                elif self.Pet == "fuckbuddy" or self.Pet == "секс-партнерша":
                        if ApprovalCheck(self, 700, "O", TabM=2) or ApprovalCheck(self, 700, "I", TabM=1):
                            self.Statup("Lust", 90, 3)
                            self.Statup("Obed", 95, 2)
                            self.Statup("Inbt", 40, 2)
                            self.Statup("Inbt", 85, 1)
                        elif ApprovalCheck(self, 600, "O", TabM=2) or ApprovalCheck(self, 500, "I", TabM=1):
                            self.Statup("Lust", 90, 2)
                            self.Statup("Love", 200, (-1-Cnt))
                            self.Statup("Obed", 80, 1)
                            self.Statup("Inbt", 70, 1)
                            self.Blush = 1
                        else:
                            self.Statup("Love", 200, -Cnt)
                            self.Statup("Love", 60, (-2-Cnt), 1)
                            self.Statup("Obed", 60, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                elif self.Pet in ("baby girl","mommy","доченька","мамочка"):
                        if ApprovalCheck(self, 1200, TabM=1):
                            self.Statup("Obed", 80, 1)
                            self.Statup("Obed", 50, 2)
                            self.Statup("Inbt", 70, 1)
                            self.Statup("Inbt", 30, 2)
                        else:
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Love", 50, (-1-Cnt))
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                #Rogue
                elif self.Pet == "chere" or self.Pet == "милочка":
                        if ApprovalCheck(self, 600, "L", TabM=1):
                            self.Statup("Love", 80, 2)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                #Kitty
                elif self.Pet == "kitten" or self.Pet == "кисонька":
                        if ApprovalCheck(self, 600, "L", TabM=1):
                            self.Statup("Love", 80, 2)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                #Emma
                elif self.Pet == "darling" or self.Pet == "дорогая":
                        if ApprovalCheck(self, 600, "L", TabM=1):
                            self.Statup("Love", 80, 2)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                #Laura
                elif self.Pet == "Wolvie" or self.Pet == "Роси":
                        if ApprovalCheck(self, 500, "I", TabM=1):
                            self.Statup("Love", 80, 1)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                elif self.Pet == "X-23" or self.Pet == "Икс-23":
                        if ApprovalCheck(self, 800, "O"):
                            self.Statup("Lust", 90, 3)
                            self.Statup("Love", 90, -1)
                            self.Statup("Obed", 95, 2)
                        elif ApprovalCheck(self, 700, "L") and not ApprovalCheck(self, 500, "O"):
                            self.Statup("Love", 200, -2)
                            self.Statup("Love", 50, -1, 1)
                            self.Statup("Obed", 30, 2)
                            self.Statup("Obed", 50, 2)
                            self.Statup("Inbt", 50, -1)
                            return 1
                #Gwen
                elif self.Pet == "Deadpool" or self.Pet == "Дэдпул":
                        if ApprovalCheck(self, 500, "O") and ApprovalCheck(self, 700, "L"):
                            self.Statup("Obed", 80, 2)
                            self.Statup("Obed", 95, 2)
                        elif not ApprovalCheck(self, 500, "O"):
                            self.Statup("Love", 200, -2)
                            self.Statup("Love", 50, -1, 1)
                            self.Statup("Obed", 80, 2)
                            self.Statup("Obed", 95, 2)
                            return 1
                elif self.Pet == "Gwen Stacy" or self.Pet == "Гвен Стейси":
                        if ApprovalCheck(self, 500, "O") and ApprovalCheck(self, 700, "L"):
                            self.Statup("Love", 90, 1)
                            self.Statup("Obed", 80, 2)
                            self.Statup("Obed", 95, 2)
                        elif not ApprovalCheck(self, 500, "O"):
                            self.Statup("Love", 200, -2)
                            self.Statup("Love", 50, -1, 1)
                            self.Statup("Obed", 80, 2)
                            self.Statup("Obed", 95, 2)
                            return 1
                return 0
        # End Petname Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        # Modification mode
        # -----------------
        def talk(self, text="вы боймали баг, если видите это"):
            if self.Tag == "Jubes":
                renpy.say(ch_v, text, interact=True)
            else:
                renpy.say(eval("ch_" + self.Tag[0].lower()), text, interact=True)

        def calculate_image_matrix(self, type="Over", layer=1):
            # For Pubes we use a special key
            base_key = "pubes" if type == "Pubes" else getattr(self, type)
            key = base_key + (str(layer) if layer > 1 else "")

            mod_item = self.modItem[type].get(key)

            if mod_item and mod_item.recolored:
                return (
                    im.matrix.opacity(float(mod_item.opacity) / 255.0) *
                    im.matrix.brightness(float(mod_item.brightness) / 255.0) *
                    im.matrix.tint(
                        float(mod_item.red) / 255.0,
                        float(mod_item.green) / 255.0,
                        float(mod_item.blue) / 255.0
                    )
                )

            return im.matrix.identity()

        def _calculate_matrix(self, item):
            """Helper function to calculate the transformation matrix."""
            return (
                im.matrix.opacity(float(getattr(item, "opacity", 255)) / 255.0) * \
                im.matrix.brightness(float(getattr(item, "brightness", 255)) / 255.0) * \
                im.matrix.tint(
                    float(getattr(item, "red", 255)) / 255.0,
                    float(getattr(item, "green", 255)) / 255.0,
                    float(getattr(item, "blue", 255)) / 255.0
                )
            )

        def __setattr__(self, key, value):
            sprite_types = [
                "_Sprite",
                "_Doggy_Animation",
                "_SexSprite",
                "_BJ_Animation",
                "_HJ_Animation",
                "_TJ_Animation"
            ]
            if key in [
                    "Over",
                    "Chest",
                    "Legs",
                    "Panties",
                    "Hose",
                    "Acc",
                    "Hair",
                    "Neck",
                    "Arms",
                    "Pierce",
                    "PierceNL",
                    "PierceNR",
                    "PierceC",
                    "PierceB",
                    "PierceNO",
                    "PierceEL",
                    "PierceER",
                    "Pubes",
                    "Piercing",
                    "Makeup"
                ]:
                object.__setattr__(self, key, value)
                # Dynamically check if any sprite type is being shown
                for suffix in sprite_types:
                    if renpy.showing(self.Tag + suffix):
                        renpy.show(self.Tag + suffix)
            else:
                object.__setattr__(self, key, value)

        def easy_recolor(self, type="Over"):
            mod_item = self.mod_item[type].get(getattr(self, type), None)
            if mod_item:
                mod_item.screen_loop()
            return

        def update_image(self, image=None):
            sprite_types = [
                "_Sprite",
                "_Doggy_Animation",
                "_SexSprite",
                "_BJ_Animation",
                "_HJ_Animation",
                "_TJ_Animation"
            ]
            if not image:
                # Dynamically check if any sprite type is being shown
                for suffix in sprite_types:
                    if renpy.showing(self.Tag + suffix):
                        renpy.show(self.Tag + suffix)
            else:
                if renpy.showing(self.Tag + "image"):
                    renpy.show(self.Tag + "image")
            return

        @property
        def Arms_display(self):
                return get_clothing_name(self.Arms_key, ime)

        @property
        def Legs_display(self):
                return get_clothing_name(self.Legs_key, ime)

        @property
        def Over_display(self):
                return get_clothing_name(self.Over_key, ime)

        @property
        def Neck_display(self):
                return get_clothing_name(self.Neck_key, ime)

        @property
        def Chest_display(self):
                return get_clothing_name(self.Chest_key, ime)

        @property
        def Panties_display(self):
                return get_clothing_name(self.Panties_key, ime)

        @property
        def Acc_display(self):
                return get_clothing_name(self.Acc_key, ime)

        @property
        def Hose_display(self):
                return get_clothing_name(self.Hose_key, ime)

        @property
        def Boots_display(self):
                return get_clothing_name(self.Boots_key, ime)

        @property
        def Hat_display(self):
                return get_clothing_name(self.Hat_key, ime)        # -----------------
#End Girls Class / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Girl Stats and Details / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Start Emotion editor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label EmotionEditor(Chr=0):
        # call EmotionEditor(RogueX)
        while True:
            menu:
                "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":
                    menu:
                        "Normal":
                            $ Chr.Emote = "normal"
                        "Angry":
                            $ Chr.Emote = "angry"
                        "Smiling":
                            $ Chr.Emote = "smile"
                        "Sexy":
                            $ Chr.Emote = "sexy"
                        "Suprised":
                            $ Chr.Emote = "surprised"
                        "Bemused":
                            $ Chr.Emote = "bemused"
                        "Manic":
                            $ Chr.Emote = "manic"

                "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":
                    menu:
                        "Sad":
                            $ Chr.Emote = "sad"
                        "Sucking":
                            $ Chr.Emote = "sucking"
                        "kiss":
                            $ Chr.Emote = "kiss"
                        "Tongue":
                            $ Chr.Emote = "tongue"
                        "confused":
                            $ Chr.Emote = "confused"
                        "Closed":
                            $ Chr.Emote = "closed"
                        "Down":
                            $ Chr.Emote = "down"

                "Emotions3: Sadside Startled Perplexed Sly":
                    menu:
                        "Sadside":
                            $ Chr.Emote = "sadside"
                        "Startled":
                            $ Chr.Emote = "startled"
                        "Perplexed":
                            $ Chr.Emote = "perplexed"
                        "Sly":
                            $ Chr.Emote = "sly"
                    #$ Chr.FaceChange
                "Toggle Mouth Spunk":
                    if "mouth" in Chr.Spunk:
                        $ Chr.Spunk.remove("mouth")
                    else:
                        $ Chr.Spunk.append("mouth")
                "Toggle hand Spunk":
                    if "hand" in Chr.Spunk:
                        $ Chr.Spunk.remove("hand")
                    else:
                        $ Chr.Spunk.append("hand")

                "Toggle Facial Spunk":
                    if "facial" in Chr.Spunk and "hair" not in Chr.Spunk:
                        $ Chr.Spunk.append("hair")
                    elif "facial" in Chr.Spunk:
                        $ Chr.Spunk.remove("facial")
                        $ Chr.Spunk.remove("hair")
                    else:
                        $ Chr.Spunk.append("facial")

                "Blush":
                    if Chr.Blush == 2:
                        $ Chr.Blush = 0
                    elif Chr.Blush:
                        $ Chr.Blush = 2
                    else:
                        $ Chr.Blush = 1
                "Exit.":
                    return
            $ Chr.FaceChange() #applies change
        #end Emotion Editor

label WardrobeEditor(Chr=0): #rkeljsvg
    while True:
        menu Wardrobe_Menu:
            "View" if True:
                while True:
                    menu:
                        "Default":
                            call Girl_Pos_Reset(Girl,0,1) #call expression Chr.Tag + "_Pos_Reset" pass (0)
                        "Face":
                            call Girl_Kissing_Launch(Girl,0)  #call expression Chr.Tag + "_Kissing_Launch" pass (0)
                        "Upper half":
                                call Girl_Breasts_Launch(Girl,0)  #call expression Girl.Tag + "_Breasts_Launch" pass (ViewTrig)
                        "Middle View":
                                call Girl_Middle_Launch(Girl,0)  #call expression Girl.Tag + "_Middle_Launch" pass (ViewTrig)
                        "Lower half":
                                call Girl_Pussy_Launch(Girl,0)  #call expression Girl.Tag + "_Pussy_Launch" pass (ViewTrig)

                        "Full Body" if True:
                            call Girl_Smol_Launch(Chr,0)
                        "Feet" if True:
                            call Girl_Feet_Launch(Chr)
                        "BJ":
                            if not renpy.showing(Chr.Tag+"_BJ_Animation"):
                                call expression Chr.Tag + "_BJ_Launch"
                            else:
                                call expression Chr.Tag + "_BJ_Reset"
                        "HJ":
                            if not renpy.showing(Chr.Tag+"_HJ_Animation"):
                                call expression Chr.Tag + "_HJ_Launch"
                            else:
                                call expression Chr.Tag + "_HJ_Reset"
                        "TJ":
                            if not renpy.showing(Chr.Tag+"_TJ_Animation"):
                                call expression Chr.Tag + "_TJ_Launch"
                            else:
                                call expression Chr.Tag + "_TJ_Reset"
                        "Doggy":
                            $ Chr.Pose = "doggy"
                            if not renpy.showing(Chr.Tag+"_Doggy"):
                                call expression Chr.Tag + "_Sex_Launch" #call expression Chr.Tag + "_Doggy_Launch"
                            else:
                                call expression Chr.Tag + "_Sex_Reset" #call expression Chr.Tag + "_Doggy_Reset"
                        "Sexpose":
                            if not renpy.showing(Chr.Tag+"_SexSprite"):
                                call expression Chr.Tag + "_Sex_Launch"
                            else:
                                call expression Chr.Tag + "_Sex_Reset"
                        "Facing":
                            if Chr.Facing:
                                $ Chr.Facing = 0
                            else:
                                $ Chr.Facing = 1
                        "Back":
                            jump Wardrobe_Menu
            # Outfits
            "Outfits":
                menu:
                    "First casual outfit":
                        $ Chr.OutfitChange("casual1")
                    "Second casual outfit":
                        $ Chr.OutfitChange("casual2")
                    "Third casual outfit":
                        $ Chr.OutfitChange("casual3")
                    "Nude":
                        $ Chr.OutfitChange("nude")
                    "sleep":
                        $ Chr.OutfitChange("sleep")
                    "gym":
                        $ Chr.OutfitChange("gym")
                    "costume" if Chr.Costume[0]:
                        $ Chr.OutfitChange("costume")
                    "swimwear":
                        $ Chr.Swim[0] = 1
                        $ Chr.OutfitChange("swimwear")

                    "custom1" if Chr.Custom1[0]:
                        $ Chr.OutfitChange("custom1")
                    "custom2" if Chr.Custom2[0]:
                        $ Chr.OutfitChange("custom2")
                    "custom3" if Chr.Custom3[0]:
                        $ Chr.OutfitChange("custom3")
                    "return":
                        pass

            "Shirts":
                while True:
                    menu:
                        # Overshirts
                        "Remove [Chr.Over]" if Chr.Over:
                            $ Chr.Over = 0
                        "Add mesh top" if Chr is RogueX:
                            $ Chr.Over = "mesh top"
                            $ Chr.Neck = "spiked collar"
                            $ Chr.Arms = "gloves"
                            if Chr.Chest == "buttoned tank":
                                $ Chr.Chest = "tank"
                        "Add pink top" if Chr is RogueX:
                            $ Chr.Over = "pink top"
                            $ Chr.Arms = "gloves"
                        "Add pink top" if Chr is KittyX or Chr is BetsyX:
                            $ Chr.Over = "pink top"
                        "Add tank top" if Chr is BetsyX:
                            $ Chr.Over = "tank"
                        "Add red top" if Chr is KittyX or Chr is JubesX:
                            $ Chr.Over = "red shirt"
                        "Dress" if Chr is EmmaX:
                            $ Chr.Over = "dress"
                        "Add pink shirt" if Chr is JeanX:
                            $ Chr.Over = "pink shirt"
                        "Add green shirt" if Chr is JeanX:
                            $ Chr.Over = "green shirt"
                        "Add yellow shirt" if Chr is JeanX:
                            $ Chr.Over = "yellow shirt"
                        "Add white shirt" if Chr is StormX:
                            $ Chr.Over = "white shirt"
                        "Add black top" if Chr is JubesX:
                            $ Chr.Over = "black shirt"
                        "Add tube top" if Chr is JubesX or Chr is DoreenX:
                            $ Chr.Over = "tube top"
                        "Add suit" if Chr is GwenX:
                            $ Chr.Over = "suit"
                            $ Chr.Arms = "gloves"
                        "Add open suit" if Chr is GwenX:
                            $ Chr.Over = "open suit"
                        "Add t-shirt" if Chr is GwenX or Chr is DoreenX:
                            $ Chr.Over = "tshirt"
                        "Add cheer top" if Chr is GwenX:
                            $ Chr.Over = "cheer top"
                        "Add shirt" if Chr is WandaX:
                            $ Chr.Over = "shirt"
                        "Add corset" if Chr is WandaX:
                            $ Chr.Over = "corset"
                        "Add nighty" if Chr is RogueX:
                            $ Chr.Over = "nighty"
                            $ Chr.Arms = 0
                        "Add jacket":
                            if Chr is JubesX or Chr is DoreenX or Chr is WandaX:
                                    $ Chr.Acc = "jacket"
                            else:
                                    $ Chr.Over = "jacket"
                        "Add vest" if Chr is DoreenX:
                                    $ Chr.Acc = "vest"
                        "Open/shut jacket" if Chr is JubesX:
                            if Chr.Acc == "jacket":
                                    $ Chr.Acc = "shut jacket"
                            else:
                                    $ Chr.Acc = "jacket"
                        "wide open jacket" if Chr is JubesX:
                            if Chr.Acc == "jacket":
                                    $ Chr.Acc = "open jacket"
                            else:
                                    $ Chr.Acc = "jacket"
                        "Remove jacket" if Chr.Acc == "jacket":
                                    $ Chr.Acc = 0
                        "Add towel":
                            $ Chr.Over = "towel"
                            $ Chr.Arms = 0
                        "Toggle Pierce":
                            if Chr.Pierce == "ring":
                                $ Chr.Pierce = "barbell"
                            elif Chr.Pierce == "barbell":
                                $ Chr.Pierce = 0
                            else:
                                $ Chr.Pierce = "ring"
                        "Toggle up-top":
                            if Chr.Uptop:
                                $ Chr.Uptop = 0
                            else:
                                $ Chr.Uptop = 1
                        "Toggle Arms":
                            if Chr.ArmPose == 1:
                                $ Chr.ArmPose = 2
                            else:
                                $ Chr.ArmPose = 1
                        "Back":
                            jump Wardrobe_Menu
            "Bra":
                while True:
                    menu:
                        # Tops
                        "Remove [Chr.Chest]" if Chr.Chest:
                            $ Chr.Chest = 0
                        "Add tank top" if Chr in (RogueX,LauraX,GwenX):
                            if Chr == LauraX:
                                $ Chr.Chest = "white tank"
                            else:
                                $ Chr.Chest = "tank"
                        "Add buttoned tank top" if Chr is RogueX:
                            $ Chr.Chest = "buttoned tank"
                        "Add cami" if Chr is KittyX:
                            $ Chr.Chest = "cami"
                        "Add dress" if Chr is KittyX:
                            $ Chr.Chest = "dress"
                        "Add leather bra" if Chr is LauraX:
                            $ Chr.Chest = "leather bra"
                        "Add wolvie top" if Chr is LauraX:
                            $ Chr.Chest = "wolvie top"
                        "Add tube top" if Chr is StormX or Chr is RogueX:
                            $ Chr.Chest = "tube top"
                        "Add bra":
                            if Chr is JeanX:
                                    $ Chr.Chest = "green bra"
                            elif Chr is StormX:
                                    $ Chr.Chest = "black bra"
                            else:
                                    $ Chr.Chest = "bra"
                        "Add cosplay bra" if Chr is StormX:
                            $ Chr.Chest = "cos bra"
                        "Add sports bra":
                            $ Chr.Chest = "sports bra"
                        "Add lace bra":
                            $ Chr.Chest = "lace bra"
                        "Add swimsuit" if Chr is BetsyX:
                            $ Chr.Chest = "swimsuit"
                        "Add bikini":
                            $ Chr.Chest = "bikini top"
                        "Add corset":
                            $ Chr.Chest = "corset"
                        "Add lace corset":
                            $ Chr.Chest = "lace corset"
                        "Add mesh top":
                            $ Chr.Chest = "mesh top"
                        "Toggle up-top":
                            if Chr.Uptop:
                                $ Chr.Uptop = 0
                            else:
                                $ Chr.Uptop = 1
                        "Toggle Piercings":
                            if Chr.Pierce == "ring":
                                $ Chr.Pierce = "barbell"
                            elif Chr.Pierce == "barbell":
                                $ Chr.Pierce = 0
                            else:
                                $ Chr.Pierce = "ring"
                        "Toggle Arms":
                            if Chr.ArmPose == 1:
                                $ Chr.ArmPose = 2
                            else:
                                $ Chr.ArmPose = 1
                        "Back":
                            jump Wardrobe_Menu

            "Pants":
                while True:
                    menu:
                        # Legs
                        "Remove [Chr.Legs]" if Chr.Legs:
                            $ Chr.Legs = 0
                        "Add Skirt" if Chr != KittyX:
                            $ Chr.Legs = "skirt"
                        "Add blue Skirt" if Chr is KittyX:
                            $ Chr.Legs = "blue skirt"
                        "Add cosplay Skirt" if Chr is LauraX:
                            $ Chr.Legs = "other skirt"

                        "Add pants" if Chr is not KittyX:
                            $ Chr.Legs = "pants"
                        "Add black jeans" if Chr is KittyX:
                            $ Chr.Legs = "black jeans"
                        "Add capri pants" if Chr is KittyX:
                            $ Chr.Legs = "capris"
                        "Add leather pants" if Chr is LauraX:
                            $ Chr.Legs = "leather pants"
                        "Add mesh pants" if Chr is LauraX:
                            $ Chr.Legs = "mesh pants"
                        "Add cheer Skirt" if Chr is GwenX:
                            $ Chr.Legs = "cheer skirt"

                        "Add yoga pants":
                            $ Chr.Legs = "yoga pants"
                        "Add shorts":
                            $ Chr.Legs = "shorts"

                        "Add dress" if Chr in (EmmaX,KittyX,JubesX,WandaX):
                            $ Chr.Legs = "dress"
#                        "Add dress" if Chr is JubesX:
#                            $ Chr.Over = "dress"
#                            $ Chr.Legs = "dress"
                        "Add suit" if Chr is GwenX:
                            $ Chr.Legs = "suit"
                        "Shoes":
                                menu:
                                    "Boots":
                                        if Chr is EmmaX:
                                                $ Chr.Boots = "thigh boots"
                                        else:
                                                $ Chr.Boots = "boots"
                                    "Sneakers":
                                        $ Chr.Boots = "sneaks"
                                    "Off":
                                        $ Chr.Boots = 0
                        "Toggle upskirt":
                            if Chr.Upskirt:
                                $ Chr.Upskirt = 0
                            else:
                                $ Chr.Upskirt = 1
                        "pull down-up panties":
                            if Chr.PantiesDown:
                                $ Chr.PantiesDown = 0
                            else:
                                $ Chr.PantiesDown = 1
                        "Toggle Pierce":
                            if Chr.Pierce == "ring":
                                $ Chr.Pierce = "barbell"
                            elif Chr.Pierce == "barbell":
                                $ Chr.Pierce = 0
                            else:
                                $ Chr.Pierce = "ring"
                        "Toggle Wetness":
                            if not Chr.Wet:
                                $ Chr.Wet = 1
                            elif Chr.Wet == 1:
                                $ Chr.Wet = 2
                            else:
                                $ Chr.Wet  = 0
                        "Toggle tail" if Chr is DoreenX:
                            if Chr.Tail == 1:
                                $ Chr.Tail = 2
                            elif Chr.Tail > 1:
                                $ Chr.Tail = 0
                            else:
                                $ Chr.Tail = 1
                        "Back":
                            jump Wardrobe_Menu

            "Panties & Hose":
                while True:
                    menu:
                        # Underwear
                        "Hose":
                            menu:
                                "Add stockings":
                                    $ Chr.Hose = "stockings"
                                "Add garter":
                                    $ Chr.Hose = "garterbelt"
                                "Add stockings and garter":
                                    $ Chr.Hose = "stockings and garterbelt"
                                "Add pantyhose":
                                    $ Chr.Hose = "pantyhose"
                                "Add tights":
                                    $ Chr.Hose = "tights"
                                "Add ripped hose":
                                    $ Chr.Hose = "ripped pantyhose"
                                "Add ripped tights":
                                    $ Chr.Hose = "ripped tights"
                                "Add knee stockings" if Chr is KittyX:
                                    $ Chr.Hose = "knee stockings"
                                "Add socks" if Chr in (JubesX,GwenX,WandaX):
                                    $ Chr.Hose = "socks"
                                "Add black stockings" if Chr is LauraX:
                                    $ Chr.Hose = "black stockings"
                                "Remove hose" if Chr.Hose:
                                    $ Chr.Hose = 0
                        "Remove panties" if Chr.Panties:
                            $ Chr.Panties = 0
                        "Add panties":
                            if Chr in (StormX,EmmaX,GwenX):
                                    $ Chr.Panties = "white panties"
                            elif Chr is WandaX:
                                    $ Chr.Panties = "gray panties"
                            else:
                                    $ Chr.Panties = "black panties"
                        "Add swimsuit" if Chr is BetsyX:
                            $ Chr.Panties = "swimsuit"
                        "Add bikini":
                            $ Chr.Panties = "bikini bottoms"
                        "Add lace panties":
                            $ Chr.Panties = "lace panties"

                        "Add green panties" if Chr is RogueX:
                            $ Chr.Panties = "green panties"
                        "Add green panties" if Chr is KittyX:
                            $ Chr.Panties = "green panties"
                        "Add sports panties" if Chr is EmmaX:
                            $ Chr.Panties = "sports panties"
                        "Add wolvie panties" if Chr is LauraX:
                            $ Chr.Panties = "wolvie panties"
                        "Add cosplay panties" if Chr is StormX:
                            $ Chr.Panties = "cos panties"
                        "Add tiger panties" if Chr is JubesX:
                            $ Chr.Panties = "tiger panties"

                        "Add shorts" if Chr == RogueX:
                            $ Chr.Panties = "shorts"
                        "Shoes":
                                menu:
                                    "Boots":
                                        if Chr is EmmaX:
                                                $ Chr.Boots = "thigh boots"
                                        else:
                                                $ Chr.Boots = "boots"
                                    "Sneakers":
                                        $ Chr.Boots = "sneaks"
                                    "Off":
                                        $ Chr.Boots = 0
                        "Toggle Pierce":
                            if Chr.Pierce == "ring":
                                $ Chr.Pierce = "barbell"
                            elif Chr.Pierce == "barbell":
                                $ Chr.Pierce = 0
                            else:
                                $ Chr.Pierce = "ring"
                        "pull down-up panties":
                            if Chr.PantiesDown:
                                $ Chr.PantiesDown = 0
                            else:
                                $ Chr.PantiesDown = 1
                        "Toggle Wetness":
                            if not Chr.Wet:
                                $ Chr.Wet = 1
                            elif Chr.Wet == 1:
                                $ Chr.Wet = 2
                            else:
                                $ Chr.Wet  = 0
                        "Toggle tail" if Chr is DoreenX:
                            if Chr.Tail == 1:
                                $ Chr.Tail = 2
                            elif Chr.Tail > 1:
                                $ Chr.Tail = 0
                            else:
                                $ Chr.Tail = 1
                        "Back":
                            jump Wardrobe_Menu
            "Misc":
                while True:
                    menu:
                        "Emotions":
                            call EmotionEditor(Chr)
                        "Toggle Arms":
                            if Chr.ArmPose == 1:
                                $ Chr.ArmPose = 2
                            else:
                                $ Chr.ArmPose = 1
                        "Toggle Wetness":
                            if not Chr.Wet:
                                $ Chr.Wet = 1
                            elif Chr.Wet == 1:
                                $ Chr.Wet = 2
                            else:
                                $ Chr.Wet = 0
                        "Toggle wet look":
                            if not Chr.Water:
                                $ Chr.Water = 1
                            elif Chr.Water == 1:
                                $ Chr.Water = 3
                            else:
                                $ Chr.Water = 0
                        "Toggle pubes":
                            if not Chr.Pubes:
                                $ Chr.Pubes = 1
                            else:
                                $ Chr.Pubes = 0
                        "Hair":
                            menu:
                                "Cosplay Hair" if Chr is RogueX:
                                    if Chr.Hair == "cosplay":
                                        $ Chr.Hair = "evo"
                                    else:
                                        $ Chr.Hair = "cosplay"
                                "Toggle Short Hair" if Chr is KittyX:
                                    if Chr.Hair == "long":
                                        $ Chr.Hair = "evo"
                                    else:
                                        $ Chr.Hair = "long"
                                "Toggle Short Hair" if Chr is EmmaX:
                                    if Chr.Hair == "long" or Chr.Hair == "wave":
                                        $ Chr.Hair = "short"
                                    else:
                                        $ Chr.Hair = "long"
                                "Toggle Hat" if Chr is EmmaX:
                                    $ Chr.Hat = 0 if Chr.Hat else 1
                                "Toggle Ponytail" if Chr is JeanX or Chr is GwenX:
                                    if Chr.Hair == "pony":
                                        $ Chr.Hair = "short"
                                    else:
                                        $ Chr.Hair = "pony"
                                "Toggle Short Hair" if Chr is StormX:
                                    if Chr.Hair == "long":
                                        $ Chr.Hair = "short"
                                    else:
                                        $ Chr.Hair = "long"
                                "Toggle Mohawk" if Chr is StormX:
                                    if Chr.Hair == "long":
                                        $ Chr.Hair = "mohawk"
                                    else:
                                        $ Chr.Hair = "long"
                                "Toggle Short Hair" if Chr is JubesX:
                                    if Chr.Hair != "short":
                                        $ Chr.Hair = "short"
                                    else:
                                        $ Chr.Hair = "shades"
                                "Toggle mask" if Chr is GwenX:
                                    if Chr.Hat == "mask":
                                        $ Chr.Hat = 0
                                    else:
                                        $ Chr.Hat = "mask"
                                "Toggle Short Hair" if Chr is BetsyX or Chr is DoreenX:
                                    if Chr.Hair == "long":
                                        $ Chr.Hair = "short"
                                    else:
                                        $ Chr.Hair = "long"
                                "Blonde Hair" if Chr is BetsyX:
                                    if Chr.Hair != "blonde":
                                        $ Chr.Hair = "blonde"
                                    else:
                                        $ Chr.Hair = "short"
                                "Toggle Short Hair" if Chr is WandaX:
                                    if Chr.Hair == "long":
                                        $ Chr.Hair = "short"
                                    else:
                                        $ Chr.Hair = "long"
                        "Toggle headband" if Chr is DoreenX:
                            if Chr.Hat:
                                $ Chr.Hat = 0
                            else:
                                $ Chr.Hat = 1
                        "Shoes":
                                menu:
                                    "Boots":
                                        if Chr is EmmaX:
                                                $ Chr.Boots = "thigh boots"
                                        else:
                                                $ Chr.Boots = "boots"
                                    "Sneakers":
                                        $ Chr.Boots = "sneaks"
                                    "Sandal":
                                        $ Chr.Boots = "sandals"
                                    "Shoes":
                                        $ Chr.Boots = "shoes"
                                    "Off":
                                        $ Chr.Boots = 0
                        "Toggle knife" if Chr == BetsyX:
                                    $ BetsyX.Knife == 0 if BetsyX.Knife else 1

                        "Toggle held" if False:
                            if not Chr.Held:
                                $ Chr.Held  = "phone"
                            elif Chr.Held == "phone":
                                $ Chr.Held  = "dildo"
                            elif Chr.Held == "dildo":
                                $ Chr.Held  = "vibrator"
                            elif Chr.Held == "vibrator":
                                $ Chr.Held  = "panties"
                            else:
                                $ Chr.Held  = 0
                        "Toggle Necklaces":
                            menu:
                                "Toggle Gold Necklace" if Chr in (KittyX,StormX):
                                    if not Chr.Neck:
                                        if Chr == KittyX:
                                                $ Chr.Neck = 'gold necklace'
                                        else:
                                                $ Chr.Neck = 'gold'
                                    else:
                                        $ Chr.Neck = 0
                                "Toggle Star Necklace" if Chr in (KittyX,0):
                                    if not Chr.Neck:
                                        $ Chr.Neck = 'star necklace'
                                    else:
                                        $ Chr.Neck = 0
                                "Toggle flower Necklace" if Chr is KittyX:
                                    if not Chr.Neck:
                                        $ Chr.Neck = 'flower necklace'
                                    else:
                                        $ Chr.Neck = 0
                                "Toggle ring Necklace" if Chr is StormX:
                                    if not Chr.Neck:
                                        $ Chr.Neck = 'rings'
                                    else:
                                        $ Chr.Neck = 0
                                "Toggle Rings" if Chr is StormX:
                                    if not Chr.Acc:
                                        $ Chr.Acc = 'rings'
                                    else:
                                        $ Chr.Acc = 0
                                "Toggle choker" if Chr in (RogueX,EmmaX,JubesX):
                                    if Chr.Neck != 'choker':
                                        $ Chr.Neck ='choker'
                                    else:
                                        $ Chr.Neck = 0
                                "Back":
                                    pass
                        "Toggle sweater" if Chr is RogueX:
                            if Chr.Acc != "sweater":
                                $ Chr.Acc ='sweater'
                            else:
                                $ Chr.Acc = 0
                        "Toggle scarf" if Chr is BetsyX:
                            if Chr.Acc != "scarf":
                                $ Chr.Acc ='scarf'
                            else:
                                $ Chr.Acc = 0
                        "Toggle suspenders" if Chr is LauraX or Chr is JeanX:
                            if Chr.Acc == "suspenders":
                                $ Chr.Acc = "suspenders2"
                            elif Chr.Acc == "suspenders2":
                                $ Chr.Acc = 0
                            else:
                                $ Chr.Acc = "suspenders"
                        "Toggle tail" if Chr is DoreenX:
                            if Chr.Tail == 1:
                                $ Chr.Tail = 2
                            elif Chr.Tail > 1:
                                $ Chr.Tail = 0
                            else:
                                $ Chr.Tail = 1
                        "Spunk Level":
                            menu:
                                "Mouth":
                                    if "mouth" in Chr.Spunk:
                                        $ Chr.Spunk.remove("mouth")
                                    else:
                                        $ Chr.Spunk.append("mouth")
                                "Chin":
                                    if "chin" in Chr.Spunk:
                                        $ Chr.Spunk.remove("chin")
                                    else:
                                        $ Chr.Spunk.append("chin")
                                "Facial":
                                    if "facial" in Chr.Spunk:
                                        $ Chr.Spunk.remove("facial")
                                    else:
                                        $ Chr.Spunk.append("facial")
                                "Hair":
                                    if "hair" in Chr.Spunk:
                                        $ Chr.Spunk.remove("hair")
                                    else:
                                        $ Chr.Spunk.append("hair")
                                "Tits":
                                    if "tits" in Chr.Spunk:
                                        $ Chr.Spunk.remove("tits")
                                    else:
                                        $ Chr.Spunk.append("tits")
                                "Belly":
                                    if "belly" in Chr.Spunk:
                                        $ Chr.Spunk.remove("belly")
                                    else:
                                        $ Chr.Spunk.append("belly")
                                "Back":
                                    if "back" in Chr.Spunk:
                                        $ Chr.Spunk.remove("back")
                                    else:
                                        $ Chr.Spunk.append("back")
                                "Pussy":
                                    if "in" in Chr.Spunk:
                                        $ Chr.Spunk.remove("in")
                                    else:
                                        $ Chr.Spunk.append("in")
                                "Ass":
                                    if "anal" in Chr.Spunk:
                                        $ Chr.Spunk.remove("anal")
                                    else:
                                        $ Chr.Spunk.append("anal")
                                "Feet":
                                    if "feet" in Chr.Spunk:
                                        $ Chr.Spunk.remove("feet")
                                    else:
                                        $ Chr.Spunk.append("feet")
                                "Return":
                                    pass
                        "Toggle Pierce":
                            if Chr.Pierce == "ring":
                                $ Chr.Pierce = "barbell"
                            elif Chr.Pierce == "barbell":
                                $ Chr.Pierce = 0
                            else:
                                $ Chr.Pierce = "ring"
                        "Add Gloves" if not Chr.Arms:
                            $ Chr.Arms = "gloves"
                        "Remove Gloves" if Chr.Arms:
                            $ Chr.Arms = 0
                        "Back":
                            jump Wardrobe_Menu
            "Nothing":
                return
return

# Start StatHacks / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label StatHacks(Chr=0,Cnt=0):
    while True:
            menu:
                "[Chr.Name]: Love: [Chr.Love], Obedience: [Chr.Obed], Inhibition:[Chr.Inbt], Lust: [Chr.Lust] Taboo: [Taboo], Location: [Chr.Loc]"
                "Change girl.":
                    call Girl_Select
                    $ Chr = Girl
                    call Shift_Focus(Chr)
                "Activities":
                    menu:
                        "Which do you want to display?"
                        "Recent Actions":
                            "[Chr.RecentActions]"
                        "Daily Actions":
                            "[Chr.DailyActions]"
                        "Traits":
                            "[Chr.Traits]"
                        "History":
                            "[Chr.History]"
                        "Back":
                            pass
                "Raise Love":
                    $ Chr.Love += 100
                "Lower Love":
                    $ Chr.Love -= 100
                "Raise Obedience":
                    $ Chr.Obed += 100
                "Lower Obedience":
                    $ Chr.Obed -= 100
                "Raise Inhibition":
                    $ Chr.Inbt += 100
                "Lower Inhibition":
                    $ Chr.Inbt -= 100
                "Taboo toggle":
                    if Taboo == 40:
                            $ Taboo = 0
                            "You are now considered alone."
                    elif Taboo == 20:
                            $ Taboo = 40
                            "It is now a public space."
                    else:
                            $ Taboo = 20
                            "It is now a semi-private space."
                    $ Chr.Taboo = Taboo
                "Your stats":
                    menu:
                        "Raise Focus":
                            $ Player.Focus += 10
                        "Lower Focus":
                            $ Player.Focus -= 10
                        "Raise Libido":
                            $ Player.Semen += 1
                        "Lower Libido":
                            $ Player.Semen -= 1
                        "Increase Money":
                            $ Player.Cash += 10
                        "Decrease Money":
                            $ Player.Cash -= 10
                        "Back":
                            pass
                "Other Stats":
                    menu:
                        "Raise Lust":
                            $ Chr.Lust += 10
                        "Lower Lust":
                            $ Chr.Lust -= 10
                        "Raise Addiction":
                            $ Chr.Addict += 10
                        "Lower Addiction":
                            $ Chr.Addict -= 10
                        "Change Sex: [Player.Male]":
                            if Player.Male:
                                    $ Player.Male = 0
                                    $ Terms = Terms0
                                    $ Loudout = Loadout0
                            else:
                                    $ Player.Male = 1
                                    $ Terms = Terms1
                                    $ Loudout = Loadout1
                        "Back":
                            pass
                "Wardrobe":
                    call WardrobeEditor(Chr)
                "Emotions":
                    call EmotionEditor(Chr)

                "Return":
                    call Checkout
                    return


label Cheat_Menu(Girl=0):
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
        menu:
            "Level-Up":
                $ Girl.Hand += 5
                $ Girl.Blow += 5
                $ Girl.Swallow += 5
                $ Girl.Hand += 5
                $ Girl.Slap += 5
                $ Girl.Tit += 5
                $ Girl.Sex += 5
                $ Girl.Anal += 5
                $ Girl.Hotdog += 5
                $ Girl.Mast += 5
                $ Girl.Org += 5
                $ Girl.FondleB += 5
                $ Girl.FondleT += 5
                $ Girl.FondleP += 5
                $ Girl.FondleA += 5
                $ Girl.DildoP += 5
                $ Girl.DildoA += 5
                $ Girl.Plugged += 5
                $ Girl.SuckB += 5
                $ Girl.InsertP += 5
                $ Girl.InsertA += 5
                $ Girl.LickP += 5
                $ Girl.LickA += 5
                $ Girl.Blow += 5
                $ Girl.Swallow += 5
                $ Girl.CreamP += 5
                $ Girl.CreamA += 5
                $ Girl.SeenChest = 1
                $ Girl.SeenPanties = 1
                $ Girl.SeenPussy = 1
                "Hand [Girl.Hand], Blow [Girl.Blow], Swallow [Girl.Swallow]"
            "Level Reset":
                $ Girl.Hand = 0
                $ Girl.Blow = 0
                $ Girl.Swallow = 0
                "Hand [Girl.Hand], Blow [Girl.Blow], Swallow [Girl.Swallow]"
            "Toggle Taboo":
                if not Taboo:
                    $ Taboo = 40
                else:
                    $ Taboo = 0
            "Maxed":
                    $ Girl.Love = 1000
                    $ Girl.Inbt = 1000
                    $ Girl.Obed = 1000
                    $ Girl.Lust = 50
                    $ Girl.Addict = 0 #how addicted she is
                    $ Girl.Addictionrate = 0 #How faster her addiction rises
                    $ Girl.Kissed = 1 #How many times they've kissed
                    $ Girl.Swallow = 0
            "50\%":
                    $ Girl.Love = 500
                    $ Girl.Inbt = 500
                    $ Girl.Obed = 500
                    $ Girl.Lust = 65
                    $ Girl.Addict = 0 #how addicted she is
                    $ Girl.Addictionrate = 10 #How faster her addiction rises
                    $ Girl.Kissed = 10 #How many times they've kissed
                    $ Girl.Swallow = 0
            "25\%":
                    $ Girl.Love = 250
                    $ Girl.Inbt = 250
                    $ Girl.Obed = 250
                    $ Girl.Lust = 85
                    $ Girl.Addict = 10 #how addicted she is
                    $ Girl.Addictionrate = 50 #How faster her addiction rises
                    $ Girl.Kissed = 10 #How many times they've kissed
                    $ Girl.Swallow = 0
            "Juice up":
                    $ Player.Semen += 5
                    $ Girl.Action = 10
            "Cold Shower":
                    $ Player.Focus = 0
            "Exit":
                return
        jump Cheat_Menu
# End StatHacks / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Clothing_Schedule_Check(Girl=0,Changed=0,Value=0,Count=0):
        #this clears out clothing items that are out of date.
        #call Clothing_Schedule_Check(RogueX,3,1)

        # Girl is the checked girl, "changed" is the outfit to compare against
        # Value defaults to 0, but if set, it will only check if the value is not 2.
        # (0-6) = Mon-Sun, (7) Datewear, (8) Teach, (9) Private (skips this one)
        # R_Schedule = [0,0,0,0,0,0,0,0,0,0]
        # Custom1=3,Cusotm2=5,Custom3=6,Gym=4,Sleep=7,Swim=10
        python:
            for BX in range(10): # (Loops through 0 to 9)
                if Girl.Clothing[BX] == Changed:
                    if Value:
                        #if the Outfit is custom1, and the outfit is SFW, then leave it alone.
                        if Girl.Clothing[BX] == 3 and Girl.Custom1[0] >= 2:
                                pass
                        elif Girl.Clothing[BX] == 5 and Girl.Custom2[0] >= 2:
                                pass
                        elif Girl.Clothing[BX] == 6 and Girl.Custom3[0] >= 2:
                                pass
                        elif Girl.Clothing[BX] == 4 and Girl.Gym[0] != 1:
                                pass
                        else:
                            Girl.Clothing[BX] = 0
                    else:
                            Girl.Clothing[BX] = 0
        return

# Start Emergency clothing reset / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emergency_Clothing_Reset: #rkeljsvg
        "Сброс всей настроенной одежды до одежды по умолчанию."
        menu:
            "Хотите продолжить?"
            "Да":
                    $ RogueX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ RogueX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ RogueX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ RogueX.Casual1 = [2,"gloves","skirt","mesh top","spiked collar","tank","black panties",0,0,"tights",0,"boots",0]
                    $ RogueX.Casual2 = [2,"gloves","pants","pink top",0,"buttoned tank","black panties",0,0,0,0,"sneaks",0]
                    $ RogueX.Gym = [0,"gloves",0,"hoodie",0,"sports bra","shorts",0,0,0,10,"sneaks",0]
                    $ RogueX.Sleepwear = [0,0,0,0,0,"tank","green panties",0,0,0,20,0,0]
                    $ RogueX.Swim = [0,0,0,"hoodie",0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                    $ RogueX.Costume = [2,"gloves","skirt",0,0,"tube top","black panties","sweater","cosplay",0,0,"boots",0]
                    $ RogueX.Clothing = [0,0,0,0,0,0,0,0,0,0]   #chooses when she wears what
                    $ RogueX.Outfit = "casual1"
                    $ RogueX.OutfitDay = "casual1"

                    $ KittyX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ KittyX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ KittyX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ KittyX.Casual1 = [2,0,"capris","pink top","gold necklace","cami","green panties",0,0,0,0,"sandals",0]
                    $ KittyX.Casual2 = [2,0,"black jeans","red shirt",0,"bra","green panties",0,0,0,0,"sandals",0]
                    $ KittyX.Gym = [0,0,"shorts",0,0,"sports bra","green panties",0,0,0,0,"sandals",0]
                    $ KittyX.Sleepwear = [0,0,"shorts",0,0,"cami","green panties",0,0,0,0,0,0]
                    $ KittyX.Swim = [0,0,"blue skirt",0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                    $ KittyX.Costume = [2,0,"dress","jacket","flower necklace","dress","lace panties",0,0,0,0,"sandals",0]
                    $ KittyX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ KittyX.Outfit = "casual1"
                    $ KittyX.OutfitDay = "casual1"

                    $ EmmaX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ EmmaX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ EmmaX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ EmmaX.Casual1 = [2,0,"pants","jacket","choker","corset","white panties",0,0,0,0,"shoes",0]
                    $ EmmaX.Casual2 = [2,"gloves","pants",0,"choker","corset","white panties",0,0,0,0,"thigh boots",0]
                    $ EmmaX.Gym = [0,0,0,0,0,"sports bra","sports panties",0,0,0,0,"shoes",0]
                    $ EmmaX.Sleepwear = [0,0,0,0,0,"corset","white panties",0,0,0,0,0,0]
                    $ EmmaX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                    $ EmmaX.Costume =  [2,"gloves","dress","dress","choker",0,"lace panties",0,"hat","stockings and garterbelt",0,"shoes","sun hat"]
                    $ EmmaX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ EmmaX.Outfit = "casual1"
                    $ EmmaX.OutfitDay = "casual1"

                    $ LauraX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ LauraX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ LauraX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ LauraX.Casual1 = [2,"wrists","leather pants",0,"leash choker","leather bra","black panties",0,0,0,0,"boots",0]
                    $ LauraX.Casual2 = [2,0,"skirt","jacket","leash choker","leather bra","black panties",0,0,0,0,"boots",0]
                    $ LauraX.Gym = [0,"wrists","leather pants",0,0,"leather bra","black panties",0,0,0,0,"boots",0]
                    $ LauraX.Sleepwear = [0,0,0,0,0,"leather bra","leather panties",0,0,0,0,0,0]
                    $ LauraX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                    $ LauraX.Costume = [2,"gloves","other skirt",0,0,"white tank","black panties","suspenders",0,"black stockings",0,"boots",0]
                    $ LauraX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ LauraX.Outfit = "casual1"
                    $ LauraX.OutfitDay = "casual1"

                    $ JeanX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ JeanX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ JeanX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ JeanX.Casual1 = [2,0,"pants","pink shirt",0,"green bra","green panties",0,0,0,0,"sandals",0]
                    $ JeanX.Casual2 = [2,0,"skirt","green shirt",0,"green bra","green panties",0,0,0,0,"sandals",0]
                    $ JeanX.Gym = [0,0,"yoga pants",0,0,"sports bra","green panties",0,0,0,0,"sandals",0]
                    $ JeanX.Sleepwear = [0,0,0,"pink shirt",0,"green bra","green panties",0,0,0,0,0,0]
                    $ JeanX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                    $ JeanX.Costume =  [2,0,"shorts","yellow shirt",0,"green bra","green panties","suspenders","pony",0,0,"sandals",0]
                    $ JeanX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ JeanX.Outfit = "casual1"
                    $ JeanX.OutfitDay = "casual1"

                    $ StormX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ StormX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ StormX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ StormX.Casual1 = [2,0,"skirt","white shirt",0,"black bra","white panties",0,0,0,0,"sandals",0]
                    $ StormX.Casual2 = [2,0,"pants","jacket",0,"tube top","white panties",0,0,0,0,"boots",0]
                    $ StormX.Gym = [0,0,"yoga pants",0,0,"sports bra","white panties",0,0,0,10,"boots",0]
                    $ StormX.Sleepwear = [0,0,0,"white shirt",0,0,"white panties",0,0,0,25,0,0]
                    $ StormX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                    $ StormX.Costume = [2,0,0,0,"rings","cos bra","cos panties","rings","short",0,0,"rings",0]
                    $ StormX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ StormX.Outfit = "casual1"
                    $ StormX.OutfitDay = "casual1"

                    $ JubesX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ JubesX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ JubesX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ JubesX.Casual1 = [2,0,"shorts","red shirt",0,"sports bra","blue panties","jacket",0,0,0,"sneaks",0]
                    $ JubesX.Casual2 = [2,0,"pants","black shirt",0,"sports bra","blue panties","jacket",0,0,0,"sneaks",0]
                    $ JubesX.Gym = [0,0,"pants",0,0,"sports bra","blue panties",0,0,0,10,"sneaks",0]
                    $ JubesX.Sleepwear = [0,0,0,0,0,"sports bra","blue panties",0,0,0,25,0,0]
                    $ JubesX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                    $ JubesX.Costume = [2,0,0,"dress","choker","lace bra","lace panties",0,"short","stockings and garterbelt",0,"sneaks",0]
                    $ JubesX.Costume2 = [2,0,0,"saiyan armor",0,"saiyan leotard","saiyan leotard","saiyan tail",0,0,0,"sneaks",0]
                    $ JubesX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ JubesX.Outfit = "casual1"
                    $ JubesX.OutfitDay = "casual1"

                    $ GwenX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ GwenX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ GwenX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ GwenX.Casual1 = [2,"gloves","suit","suit",0,"bra","white panties",0,0,0,0,"boots","mask"]
                    $ GwenX.Casual2 = [2,0,"shorts","tshirt",0,"bra","white panties",0,0,"tights",0,"sneaks",0]
                    $ GwenX.Gym = [0,0,"shorts",0,0,"tank","white panties",0,0,0,0,"sneaks",0]
                    $ GwenX.Sleepwear = [0,0,"shorts",0,0,"tank","white panties",0,0,0,0,0,0]
                    $ GwenX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                    $ GwenX.Costume = [2,0,"cheer skirt","cheer top",0,0,"white panties",0,"pony","socks",0,"sneaks",0]
                    $ GwenX.Outfit = "casual2"
                    $ GwenX.OutfitDay = "casual2"

                    $ BetsyX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ BetsyX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ BetsyX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ BetsyX.Casual1 = [2,"gloves","shorts","tank",0,"bra","blue panties",0,0,"socks",0,"shoes",0]
                    $ BetsyX.Casual2 = [2,0,"skirt","pink top",0,"bra","blue panties","scarf",0,0,0,"shoes",0]
                    $ BetsyX.Gym = [0,0,"yoga pants","tank",0,"bra","blue panties",0,0,0,0,"sneaks",0]
                    $ BetsyX.Sleepwear = [0,0,0,"pink top",0,"bra","blue panties",0,0,0,0,0,0]
                    $ BetsyX.Swim = [0,0,0,0,0,"swimsuit","swimsuit",0,0,0,0,0,0]
                    $ BetsyX.Costume = [2,0,"yoga pants","jacket",0,"sports bra","blue panties",0,"blonde",0,0,"sneaks",0]
                    $ BetsyX.Costume2 = [2,"cammy gloves",0,0,0,"cammy leotard","cammy leotard","cammy print","blonde",0,0,"boots","red beret"]
                    $ BetsyX.Outfit = "casual1"
                    $ BetsyX.OutfitDay = "casual1"


                    $ DoreenX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ DoreenX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ DoreenX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ DoreenX.Casual1 = [2,0,"shorts","tube top",0,"tan bra","tan panties","jacket",0,"pantyhose",0,"boots","headband"]
                    $ DoreenX.Casual2 = [2,0,"skirt","tshirt",0,"tan bra","tan panties",0,0,"tights",0,"sneaks","headband"]
                    $ DoreenX.Gym = [0,0,0,0,0,"sports bra","tan panties","jacket",0,"tights",0,"sneaks","headband"]
                    $ DoreenX.Sleepwear = [0,0,0,"tshirt",0,0,"tan panties",0,0,"tights",0,0,0]
                    $ DoreenX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                    $ DoreenX.Costume = [2,0,"red skirt","sweater",0,"tan bra","tan panties",0,0,0,0,"sneaks","glasses"]
                    $ DoreenX.Outfit = "casual1"
                    $ DoreenX.OutfitDay = "casual1"


                    $ WandaX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ WandaX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ WandaX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    $ WandaX.Casual1 = [2,"armlet","pants","shirt","choker","red bra","gray panties",0,0,0,0,"boots",0]
                    $ WandaX.Casual2 = [2,"armlet","shorts","corset","choker","mesh top","gray panties","jacket",0,"pantyhose",0,"boots",0]
                    $ WandaX.Gym = [0,0,"pants","shirt","choker","red bra","gray panties",0,0,0,0,"boots",0]
                    $ WandaX.Sleepwear = [0,0,"dress",0,0,0,"gray panties",0,0,0,0,0,0]
                    $ WandaX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0,0,0]
                    $ WandaX.Costume = [2,0,"skirt","purple top","scarf",0,"gray panties",0,"long",0,0,"boots","headband"]
                    $ WandaX.Casual3 = [2,0,"dress",0,"choker","mesh top","gray panties","jacket",0,"socks",0,"boots",0]
                    $ WandaX.Outfit = "casual1"
                    $ WandaX.OutfitDay = "casual1"

                    "Готово."
                    "Теперь вы можете настроить все костюмы заново."
            "Нет":
                pass
        return
# End Emergency clothing reset / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# End Girl Stats and Details / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label AnyLine(Girl=0,Templine=". . ."): #rkeljsvgbdw
        #This calls a line from any girl you reference
        # call AnyLine(Girl,Line)
        #$ Girl = GirlCheck(Girl) #removed when I added unknown. Needed?

        $ global PassLine
        $ PassLine = Templine
        if Girl is RogueX:
                ch_r "[PassLine]"
        elif Girl is KittyX:
                ch_k "[PassLine]"
        elif Girl is EmmaX:
                ch_e "[PassLine]"
        elif Girl is LauraX:
                ch_l "[PassLine]"
        elif Girl is JeanX:
                ch_j "[PassLine]"
        elif Girl is StormX:
                ch_s "[PassLine]"
        elif Girl is JubesX:
                ch_v "[PassLine]"
        elif Girl is GwenX:
                ch_g "[PassLine]"
        elif Girl is BetsyX:
                ch_b "[PassLine]"
        elif Girl is DoreenX:
                ch_d "[PassLine]"
        elif Girl is WandaX:
                ch_w "[PassLine]"
        else:
                ch_u "[PassLine]"
        return

label GirlsAngry(Girls = 0,BO=[],HomeGirl=0): #rkeljsvgbdw
        # Causes girls to storm off if you've pissed them off.
        $ Tempmod = 0
        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                if BX.Loc == bg_current and "angry" in BX.RecentActions:
                        if BX in Party:
                                Party.remove(BX)
                        if BX in Present:
                                Present.remove(BX)
                        if BX in Nearby:
                                Nearby.remove(BX)


                        if bg_current == BX.Home:
                                HomeGirl = BX
                                break #jumps to bottom part
                        else:
                                BX.Loc = BX.Home

                        if Girls:
                            narrator(". . . как и "+BX.Name+".", interact=True)
                        else:
                            narrator(BX.Name+" убегает.", interact=True)
                        Girls += 1

                        renpy.hide(BX.Tag+"_SexSprite")
                        renpy.hide(BX.Tag+"_Doggy_Animation")
                        renpy.hide(BX.Tag+"_HJ_Animation")
                        renpy.hide(BX.Tag+"_BJ_Animation")
                        renpy.hide(BX.Tag+"_TJ_Animation")
                        renpy.hide(BX.Tag+"_Finger_Animation")
                        renpy.hide(BX.Tag+"_CUN_Animation")
                        renpy.hide(BX.Tag+"_69_Animation")
                        renpy.hide(BX.Tag+"_69_CUN")
                        renpy.hide(BX.Tag+"_Seated")
                        renpy.hide(BX.Tag+"_Sprite")

        if HomeGirl and bg_current == HomeGirl.Home:
                if HomeGirl is RogueX:
                        ch_r "Тебе следует уйти, а то я за себя не ручаюсь."
                elif HomeGirl is KittyX:
                        ch_k "Тебе следует уйти отсюда, я сейчас даже смотреть на тебя не могу."
                elif HomeGirl is EmmaX:
                        ch_e "Тебе следует уйти. Или ты хочешь испытать мое терпение?"
                elif HomeGirl is LauraX:
                        ch_l "Тебе нужно уйти."
                elif HomeGirl is JeanX:
                        ch_j "Уходи, СЕЙЧАС ЖЕ!"
                elif HomeGirl is StormX:
                        ch_s "Уйди!"
                elif HomeGirl is JubesX:
                        ch_v "Убирайся!"
                elif HomeGirl is GwenX:
                        ch_g "Уходи!"
                elif HomeGirl is BetsyX:
                        ch_b "Исчезни!"
                elif HomeGirl is DoreenX:
                        ch_d "Уйди!"
                elif HomeGirl is WandaX:
                        ch_w "Хватит, [Player.Name]!"
                "Вы возвращаетесь в свою комнату."
                $ Party = []
                $ bg_current = "bg player" #$ renpy.pop_call()
                jump Misplaced #jump Player_Room_Entry
        return


# Start Last Namer / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label LastNamer(Wordcount = 0, Splitname = 0, Lastname = 0):
        # Wordcount = number of words
        $ Wordcount = Player.Name.count(" ")

        # Splitname turns the name into a list, ie [Charles, Francis, Xavier]
        $ Splitname = Player.Name.split()

        # Lastname picks the last word in that set
        $ Lastname = Terms["mister"] + " " + Splitname[Wordcount]

        if Splitname[Wordcount] in EmmaX.Petname:
                $ EmmaX.Petname = Lastname
        return Lastname

# End Last Namer / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Drain All / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label DrainAll(Word=0,Recent=1,Daily=1,Traits=0):
        # called to remove words from all girls in the game.
        # call DrainAll("arriving")
        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                BX.DrainWord(Word,Recent,Daily,Traits)
        return


# Start Clothes Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Clothes Scheduling / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Clothes_Schedule(Girl=0,Cnt = 0): #rkeljsvgb
        #Sets clothing for different days, if Cnt is 3 it's all days, 2 is TuThu, 1 is only weekends
        #Schedule 0-6= mon-fri, Schedule 7 is dates, 9 is private
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if Girl is RogueX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_r "Итак, ты хочешь выбрать, что я буду носить в течение недели? Ладно, валяй."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_r "Думаю, я могла бы выделить для тебя несколько дней."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_r "Мы можем поговорить о том, что я ношу вне занятий."
                        $ Cnt = 1
                else:
                        ch_r "Знаешь, если честно, мне не нужны твои советы."
                        return
        elif Girl is KittyX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_k "Дай мне знать, что тебе нравится."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_k "Я могу выделить для тебя несколько дней. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_k "Мы могли бы обсудить выходные, наверное. . ."
                        $ Cnt = 1
                else:
                        ch_k "Думаю, я и[Girl.like]сама способна подобрать себе одежду."
                        return
        elif Girl is EmmaX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_e "Я открыта для предложений."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_e "Я могу позволить тебе выбрать несколько дней. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_e "Возможно, когда я не на работе. . ."
                        $ Cnt = 1
                else:
                        ch_e "Я бы предпочла сама заниматься своим гардеробом."
                        return
        elif Girl is LauraX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_l "Ладно, выбирай."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_l "Я не знаю, ты можешь выбрать несколько дней. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_l "Может быть, по выходным. . ."
                        $ Cnt = 1
                else:
                        ch_l "Нет, я сама разберусь."
                        return
        elif Girl is JeanX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_j "Ладно, я устала сама себе выбирать наряды. . ."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_j "Думаю, у тебя есть какой-то вкус. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_j "Думаю, мои выходные свободны. . ."
                        $ Cnt = 1
                else:
                        ch_j "А? Нет."
                        return
        elif Girl is StormX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_s "Я готова тебя выслушать."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_s "Пожалуй, ты мог бы выбрать несколько дней. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_s "Возможно, когда я не на работе. . ."
                        $ Cnt = 1
                else:
                        ch_s "Я бы предпочла сама выбирать себе одежду."
                        return
        elif Girl is JubesX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_v "Что думаешь?"
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_v "Ты мог бы помочь мне подобрать наряд на несколько дней?"
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_v "Не знаю, может, на выходные?"
                        $ Cnt = 1
                else:
                        ch_v "Нее, я сама разберусь."
                        return
        elif Girl is GwenX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_g "Хорошо."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_g "Хорошо. . . что предлагаешь?"
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_g "Хорошо, давай посмотрим твой выбор на \"выходные.\""
                        $ Cnt = 1
                else:
                        ch_g "Думаю, мне не нужна помощь, спасибо."
                        return
        elif Girl is BetsyX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_b "Мне бы хотелось услышать твою точку зрения."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_b "Ох? Что ты предлагаешь?"
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_b "Пожалуй, я могу сделать несколько заметок по поводу выходных."
                        $ Cnt = 1
                else:
                        ch_b "Мне не требуется твоя помошь."
                        return
        elif Girl is DoreenX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_d "Ох, можешь сказать, что ты хочешь, я попробую это носить."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_d "О, дай мне знать, что ты хочешь."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_d "Ну, я могу позволить тебе выбрать несколько нарядов на выходные дни."
                        $ Cnt = 1
                else:
                        ch_d "Я -довольно хорошо- разбираюсь в моде."
                        return
        elif Girl is WandaX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_w "Конечно."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_w "Хорошо, я открыта для идей."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_w "Если у тебя есть идеи, что мне надевать в выходные дни, дай мне знать."
                        $ Cnt = 1
                else:
                        ch_w "Мне не нужны твои советы."
                        return
        while True:
            menu:
                    extend ""
                    "Каждый день":
                        "Эта опция устанавливает ее наряд на каждый день недели за один клик."
                        "Все ранее установленое расписание по ношению одежды будет перезаписано."
                        "Любой выбор, который вы сделаете позже, отменит действие этой опции."
                        menu:
                            "Выбрать наряд":
                                call Clothes_ScheduleB
                                if Cnt > 1:
                                        $ Girl.Clothing[0] = _return
                                        $ Girl.Clothing[2] = _return
                                        $ Girl.Clothing[4] = _return
                                if Cnt > 2:
                                        $ Girl.Clothing[1] = _return
                                        $ Girl.Clothing[3] = _return
                                $ Girl.Clothing[5] = _return
                                $ Girl.Clothing[6] = _return
                            "Неважно.":
                                pass
                    "Будние дни":
                        menu:
                            "В понедельник ты должна носить. . ." if Cnt > 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[0] = _return
                            "В понедельник ты должна носить. . . (locked)" if Cnt <= 1:
                                pass

                            "Во вторник ты должна носить. . ." if Cnt > 2:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[1] = _return
                            "Во вторник ты должна носить. . . (locked)" if Cnt <= 2:
                                pass

                            "В среду ты должна носить. . ." if Cnt > 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[2] = _return
                            "В среду ты должна носить. . . (locked)" if Cnt <= 1:
                                pass

                            "В четверг ты должна носить. . ." if Cnt > 2:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[3] = _return
                            "В четверг ты должна носить. . . (locked)" if Cnt <= 2:
                                pass

                            "В пятницу ты должна носить. . ." if Cnt > 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[4] = _return
                            "В пятницу ты должна носить. . . (locked)" if Cnt <= 1:
                                pass
                            "Назад":
                                pass
                    "Другое":
                        menu:
                            "В субботу ты должна носить. . . (locked)" if Cnt < 1:
                                pass
                            "В субботу ты должна носить. . ." if Cnt >= 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[5] = _return

                            "В воскресенье ты должна носить. . . (locked)" if Cnt < 1:
                                pass
                            "В воскресенье ты должна носить. . ." if Cnt >= 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[6] = _return

                            "В наших комнатах ты должна носить. . . (locked)" if Cnt < 1:
                                pass
                            "В наших комнатах ты должна носить. . ." if Cnt >= 1:
                                call Clothes_ScheduleB(Girl,99)
                                $ Girl.Clothing[9] = _return

                            "На свидания ты должна надевать. . . (locked)" if Cnt < 1:
                                pass
                            "На свидания ты должна надевать. . ." if Cnt >= 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[7] = _return

                            "На занятия ты должна надевать. . . (locked)" if Girl in (EmmaX,StormX) and Cnt < 3:
                                pass
                            "На занятия ты должна надевать. . ." if Girl in (EmmaX,StormX) and Cnt >= 3:
                                call Clothes_ScheduleB(Girl,90)
                                $ Girl.Clothing[8] = _return

                            "Назад":
                                pass

                    "О спортивной одежде":
                        menu:
                            ch_p "Помнишь, раньше ты спрашивала меня насчет своей спортивной одежды?"
                            "Не спрашивай меня, прежде чем переодеться в спортивную одежду" if "no ask gym" not in Girl.Traits:
                                        call AnyLine(Girl,"Конечно.")
                                        $ Girl.Traits.append("no ask gym")
                            "Спрашивай меня, прежде чем переодеться в спортивную одежду" if "no ask gym" in Girl.Traits:
                                        call AnyLine(Girl,"Конечно.")
                                        $ Girl.Traits.remove("no ask gym")
                            "Неважно":
                                pass

                    "Домашний наряд" if Girl.Clothing[9]:
                                #if comfy is in LauraX.Traits, she won't ask before changing
                                ch_p "Ты же знаешь какой наряд носить наедине со мной?"
                                if Girl in (EmmaX,StormX):
                                        call AnyLine(Girl,"Да?")
                                else:
                                        call AnyLine(Girl,"Да?")
                                menu:
                                    extend ""
                                    "Всегда переодевайся, не спрашивая меня об этом." if "comfy" not in Girl.Traits:
                                        call AnyLine(Girl,"Конечно.")
                                        $ Girl.Traits.append("comfy")
                                    "Спрашивай меня прежде чем переодеться." if "comfy" in Girl.Traits:
                                        call AnyLine(Girl,"Конечно.")
                                        $ Girl.Traits.remove("comfy")
                                    "Неважно":
                                        pass

                    "Неважно [[завершить]":
                        return
        jump Clothes_Schedule

label Clothes_ScheduleB(Girl=0,Count = 0): #rkeljsvgb
        #This is called by Clothes_Schedule when setting her outfit for a given day
        #If Count by the end, yes, if not count, no. If count is 99 then it's an auto-yes, if 90 it's for Emma teaching
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)
        menu:
            "Зеленый комплект." if Girl is RogueX:
                $ Count = 1
            "Розовый комплект с джинсами." if Girl is RogueX:
                $ Count = 2

            "Розовый комплект с джинсами." if Girl is KittyX:
                $ Count = 1
            "Комплект с красной рубашкой." if Girl is KittyX:
                $ Count = 2

            "Костюм преподавателя." if Girl is EmmaX:
                $ Count = 1
            "Супергеройский костюм." if Girl is EmmaX:
                $ Count = 2

            "Кожаный боевой наряд." if Girl is LauraX:
                $ Count = 1
            "Куртка с футболкой." if Girl is LauraX:
                $ Count = 2

            "Розовая кофточка и с брюками цвета хаки." if Girl is JeanX:
                $ Count = 1
            "Зеленая рубашка и юбка." if Girl is JeanX:
                $ Count = 2

            "Белый топ и юбка." if Girl is StormX:
                $ Count = 1
            "Черная куртка и брюки." if Girl is StormX:
                $ Count = 2

            "Красно-синий комплект." if Girl is JubesX:
                $ Count = 1
            "Комплект с черным топом и брюками." if Girl is JubesX:
                $ Count = 2

            "Супергеройский костюм." if Girl is GwenX:
                $ Count = 1
            "Футболка и шорты." if Girl is GwenX:
                $ Count = 2

            "Майка и шорты." if Girl is BetsyX:
                $ Count = 1
            "Розовый топик и юбка." if Girl is BetsyX:
                $ Count = 2

            "Куртка и шорты." if Girl is DoreenX:
                $ Count = 1
            "Футболка и юбка." if Girl is DoreenX:
                $ Count = 2

            "Красная рубашка с брюками." if Girl is WandaX:
                $ Count = 1
            "Корсет с шортами." if Girl is WandaX:
                $ Count = 2
            "Платье." if Girl is WandaX:
                $ Count = 11

            "Тот наряд, который мы подобрали вместе [[пользовательский]":
                        if Girl is RogueX:
                                ch_r "Который из них?"
                        elif Girl is KittyX:
                                ch_k "[Girl.Like]который?"
                        elif Girl is EmmaX:
                                ch_e "Который ты имеешь в виду?"
                        elif Girl is LauraX:
                                ch_l "Который?"
                        elif Girl is JeanX:
                                ch_j "Который наряд?"
                        elif Girl is StormX:
                                ch_s "Про который ты говоришь?"
                        elif Girl is JubesX:
                                ch_v "Который?"
                        elif Girl is GwenX:
                                ch_g "А? Который?"
                        elif Girl is BetsyX:
                                ch_b "Ох? Который?"
                        elif Girl is DoreenX:
                                ch_d "Какой из них?"
                        elif Girl is WandaX:
                                ch_w "Какой?"
                        menu:
                            extend ""
                            "Первый. (locked)" if not Girl.Custom1[0]:
                                        pass
                            "Первый." if Girl.Custom1[0]:
                                        if Girl.Custom1[0] >= 2 or Count == 99:
                                            $ Count = 3
                                        else:
                                            call AnyLine(Girl,"Хорошо. . .")
                                            call QuickOutfitCheck(Girl,3) #re-checks to see if it will work
                                            if Girl.Custom1[0] >= 2:
                                                    $ Count = 3
                                            else:
                                                    $ Line = "no"
                            "Второй. (locked)" if not Girl.Custom2[0]:
                                        pass
                            "Второй." if Girl.Custom2[0]:
                                        if Girl.Custom2[0] >= 2 or Count == 99:
                                            $ Count = 5
                                        else:
                                            call AnyLine(Girl,"Хорошо. . .")
                                            call QuickOutfitCheck(Girl,5)  #re-checks to see if it will work
                                            if Girl.Custom2[0] >= 2:
                                                    $ Count = 5
                                            else:
                                                    $ Line = "no"
                            "Третий. (locked)" if not Girl.Custom3[0]:
                                        pass
                            "Третий." if Girl.Custom3[0]:
                                        if Girl.Custom3[0] >= 2 or Count == 99:
                                            $ Count = 6
                                        else:
                                            call AnyLine(Girl,"Хорошо. . .")
                                            call QuickOutfitCheck(Girl,6) #re-checks to see if it will work
                                            if Girl.Custom3[0] >= 2:
                                                    $ Count = 6
                                            else:
                                                    $ Line = "no"
                            "Неважно":
                                        pass
                        if Line == "no":
                                if Girl is RogueX:
                                        ch_r "Нет, я не надену это на выход, [Girl.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Я[Girl.like]точно не выйду в этом."
                                elif Girl is EmmaX:
                                        ch_e "Я точно не буду носить это на людях."
                                elif Girl is LauraX:
                                        ch_l "Я не буду носить это."
                                elif Girl is JeanX:
                                        ch_j "Да, я не хочу, чтобы меня в этом видели."
                                elif Girl is StormX:
                                        ch_s "Я не могу носить это на людях."
                                elif Girl is JubesX:
                                        ch_v "Это не для посторонних глаз. . ."
                                elif Girl is GwenX:
                                        ch_g "Ха! Я не буду ходить в этом по улице, [Girl.Petname]."
                                elif Girl is BetsyX:
                                        ch_b "Я бы ни за что не смогла надеть это на выход, [Girl.Petname]."
                                elif Girl is DoreenX:
                                        ch_d "Воу! Я не могу носить это на людях!"
                                elif Girl is WandaX:
                                        ch_w "Я точно не готова в этом выходить \"в люди.\""
                                $ Line = 0
                        else:
                                call AnyLine(Girl,"Ладно. . .")

            "Спортивная одежда.":
                if Count == 90 and (not ApprovalCheck(Girl, 2000) or Girl not in Rules):
                    call AnyLine(Girl,"Не на занятиях, "+Girl.Petname+".")
                    $ Count = 0
                else:
                    $ Count = 4
            "Одежда для сна.":
                if Count == 99:
                    $ Count = 7
                else:
                    call AnyLine(Girl,"Хорошо. . .")
                    call QuickOutfitCheck(Girl,7)  #re-checks to see if it will work
                    if Girl.Custom1[0] == 2:
                            $ Count = 7
                            call AnyLine(Girl,"Ладно. . .")
                    else:
                            if Girl is RogueX:
                                    ch_r " [Girl.Petname], я не уверена."
                            elif Girl is KittyX:
                                    ch_k "[Girl.Petname], это не совсем уместно."
                            elif Girl is EmmaX:
                                    ch_e "[Girl.Petname], я не думаю, что это было бы уместно."
                            elif Girl is LauraX:
                                    ch_l "[Girl.Petname], она слишком скучная."
                            elif Girl is JeanX:
                                    ch_j "Я  в этом -сплю-, а не ношу везде."
                            elif Girl is StormX:
                                    ch_s "Это одежда для сна, чем повседневная одежда."
                            elif Girl is JubesX:
                                    ch_v "Это для сна, а не для прогулок. . ."
                            elif Girl is GwenX:
                                    ch_g "Я не хочу носить это. . ."
                            elif Girl is BetsyX:
                                    ch_b "[Girl.Petname], эта одежда не для выхода на публику."
                            elif Girl is DoreenX:
                                    ch_d "Я не выйду на улицу в пижаме."
                            elif Girl is WandaX:
                                    ch_w "Хех, я не собираюсь в -этом- выходить в люди!"
                            $ Count = 0
            "Надевай что захочешь.":
                pass

        if Girl is RogueX:
                if Count:
                        ch_r "Хорошо, я это надену."
                else:
                        ch_r "Тогда я просто надену что захочу."
        elif Girl is KittyX:
                if Count:
                        ch_k "Хорошо, я это надену."
                else:
                        ch_k "Тогда я просто надену что захочу."
        elif Girl is EmmaX:
                if Count:
                        ch_e "Отлично."
                else:
                        ch_e "Тогда я надену что-нибудь другое."
        elif Girl is LauraX:
                if Count:
                        ch_l "Конечно."
                else:
                        ch_l "Тогда я надену что-нибудь другое."
        elif Girl is JeanX:
                if Count:
                        ch_j "Ладно."
                else:
                        ch_j "У меня другие планы."
        elif Girl is StormX:
                if Count:
                        ch_s "Я это надену."
                else:
                        ch_s "Вместо этого я выберу что-нибудь другое. . ."
        elif Girl is JubesX:
                if Count:
                        ch_v "Я надену это."
                else:
                        ch_v "Я выберу что-нибудь другое. . ."
        elif Girl is GwenX:
                if Count:
                        ch_g "Ага, я это надену."
                else:
                        ch_g "Эм, я, наверное, надену что-нибудь другое."
        elif Girl is BetsyX:
                if Count:
                        ch_b "Я могу это надеть."
                else:
                        ch_b "Я. . . рассмотрю другие варианты."
        elif Girl is DoreenX:
                if Count:
                        ch_d "Ох, это -очень- милый наряд."
                else:
                        ch_d "Я ценю твой совет, но нет."
        elif Girl is WandaX:
                if Count:
                        ch_w "Неплохо, спасибо."
                else:
                        ch_w "Хех, тебе следует заниматься тем, в чем ты хоть что-то понимаешь."
        return Count
#End Clothes Scheduling Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label AltClothes(Girl=0,Outfit=1):
        #1 = "casual1", 2 = "casual2", 11 = "casual3"
        #3 = "custom1", 4 = "gym", 5 = "custom2", 6 = "custom3", 7 = "sleep", 10 = "swimwear"
        #This selects her outfit when teaching if 8
        #This selects her private outfit if 9
        $ Girl = GirlCheck(Girl)

        if Girl.Clothing[Outfit] == 1 or not Girl.Clothing[Outfit]:
                    $ Girl.Outfit = "casual1"
        elif Girl.Clothing[Outfit] == 2:
                    $ Girl.Outfit = "casual2"
        elif Girl.Clothing[Outfit] == 11:
                    $ Girl.Outfit = "casual3"
        elif Girl.Clothing[Outfit] == 3:
                    $ Girl.Outfit = "custom1"
        elif Girl.Clothing[Outfit] == 5:
                    $ Girl.Outfit = "custom2"
        elif Girl.Clothing[Outfit] == 6:
                    $ Girl.Outfit = "custom3"
        elif Girl.Clothing[Outfit] == 7:
                    $ Girl.Outfit = "sleep"
        elif Girl.Clothing[Outfit] == 4:
                    $ Girl.Outfit = "gym"
        elif Girl.Clothing[Outfit] == 10:
                    $ Girl.Outfit = "swimwear"
        else:
                    $ Girl.Outfit = "casual1"
        return

label Private_Outfit(Girl=0): #rkeljsvgb
        #sets Girl's private outfit in private
        $ Girl = GirlCheck(Girl)
        if Girl.Break[0] or "angry" in Girl.DailyActions:
                return
        if Girl.Outfit == "temporary" or not Girl.Clothing[9]:
                #if you manually set a different option, keep it
                #if no alternate is set, return
                return
        if "comfy" in Girl.RecentActions or "comfy" in Girl.Traits or Girl.Outfit == Girl.Clothing[9]:
                call AltClothes(Girl,9)
                $ Girl.OutfitChange(Changed=1)
        elif "no comfy" in Girl.RecentActions:
                pass
        elif ApprovalCheck(Girl, 1200, "LI") and (2 * Girl.Inbt) >= (Girl.Love + Girl.Obed +100):
                # if her inhibition is much higher than her obedience to you. . .
                call Shift_Focus(Girl)
                if Girl is RogueX:
                        ch_r "[Girl.Petname], сейчас приду. . ."
                        ch_r "Я переоденусь во что-нибудь более удобное. . ."
                elif Girl is KittyX:
                        ch_k "Дай мне минутку. . ."
                        ch_k "Я надену что-нибудь более. . . веселое."
                elif Girl is EmmaX:
                        ch_e "Я на минутку. . ."
                        ch_e "Я переоденусь во что-нибудь более удобное. . ."
                elif Girl is LauraX:
                        ch_l "Одну минуту. . ."
                        ch_l "Я надену что-нибудь более удобное."
                elif Girl is JeanX:
                        ch_j "Дай мне переодеться. . ."
                elif Girl is StormX:
                        ch_s "Один момент. . ."
                        ch_s "Мне нужно переодеться во что-нибудь более удобное. . ."
                elif Girl is JubesX:
                        ch_v "Дай мне минутку. . ."
                        ch_v "Я хочу надеть что-нибудь другое. . ."
                elif Girl is GwenX:
                        ch_g "Секундочку. . ."
                        ch_g "Мне нужно надеть подходящую одежду."
                elif Girl is BetsyX:
                        ch_b "Один момент. . ."
                        ch_b "Я должна переодеться во что-нибудь другое."
                elif Girl is DoreenX:
                        ch_d "Одну минутку. . ."
                        ch_d "Мне нужно надеть что-нибудь другое."
                elif Girl is WandaX:
                        ch_w "Дай мне секунду, чтобы переодеться. . ."
                call AltClothes(Girl,9)
                $ Girl.OutfitChange(Changed=1)
                $ Girl.RecentActions.append("comfy")
        else:
                call Shift_Focus(Girl)
                if Girl is RogueX:
                        ch_r "[Girl.Petname], сейчас приду. . ."
                        menu:
                            ch_r "Хочешь, я надену что-нибудь поудобнее?"
                            "Конечно.":
                                    ch_r "Я рада. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "Нет, спасибо.":
                                    ch_r "Как хочешь."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl is KittyX:
                        ch_k "Дай мне минутку. . ."
                        menu:
                            ch_k "Хочешь, чтобы я надела что-нибудь более веселое?"
                            "Конечно.":
                                    ch_k "Хехе. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "Нет, спасибо.":
                                    ch_k "Ох, ладно."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl is EmmaX:
                        ch_e "Я на минутку. . ."
                        menu:
                            ch_e "Хочешь, я переоденусь во что-нибудь более удобное?"
                            "Конечно.":
                                    ch_e "Замечательно. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "Нет, спасибо.":
                                    ch_e "Ну и отлично."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl is LauraX:
                        ch_l "Одну минуту. . ."
                        menu:
                            ch_l "Я могла бы надеть что-нибудь более веселое. . ."
                            "Конечно.":
                                    ch_l "Клево. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "Нет, спасибо.":
                                    ch_l "Ох, ладно."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl is JeanX:
                        menu:
                            ch_j "Я могла бы переодеться во что-нибудь прикольное. . ."
                            "Конечно.":
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "Нет, спасибо.":
                                    ch_j "Хм. Ладно. . ."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl is StormX:
                        ch_s "Я на минутку. . ."
                        menu:
                            ch_s "Хочешь, я переоденусь во что-нибудь более удобное?"
                            "Конечно.":
                                    ch_s "Превосходно. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "Нет, спасибо.":
                                    ch_s "Отлично."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl is JubesX:
                        ch_v "Дай мне минутку. . ."
                        menu:
                            ch_v "Слушай, как насчет того, чтобы я накинула на себя что-нибудь. . . более удобное?"
                            "Конечно.":
                                    ch_v "Клево. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "Нет, спасибо.":
                                    ch_v "Ладно."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl is GwenX:
                        ch_g "Секундочку. . ."
                        menu:
                            ch_g "Не против, если я переоденусь?"
                            "Конечно.":
                                    ch_g "Круто. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "Нет, спасибо.":
                                    ch_g "Оу."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl is BetsyX:
                        ch_b "Один момент. . ."
                        menu:
                            ch_b "Ты не возражаешь, если я переоденусь?"
                            "Конечно.":
                                    ch_b "Изумительно. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "Нет, спасибо.":
                                    ch_b "Ну хорошо. . ."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl is DoreenX:
                        ch_d "Дай мне минутку. . ."
                        menu:
                            ch_d "Не против, если я переоденусь во что-нибудь другое?"
                            "Без проблем.":
                                    ch_d "Здорово. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "Нет, не надо.":
                                    ch_d "Ох, ладно. . ."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl is WandaX:
                        ch_w "Дай мне секунду, чтобы переодеться. . ."
                        menu:
                            ch_w "Не возражаешь, если я надену что-нибудь поприличнее?"
                            "Без проблем.":
                                    ch_w "Клево. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "Нет, не надо.":
                                    ch_w "Ох. ладно. . ."
                                    $ Girl.RecentActions.append("no comfy")
        return

label Custom_Out(Girl=0,Custom = 3, Shame = 0, Agree = 0): #rkeljsvgb
        #If Custom1 = 3, if custom2 = 5, if custom3 = 6
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)
        $ Girl.FaceChange("sexy", 1)

        if Custom == 3:
                $ Shame = Girl.Custom1[10]
                if Girl.Custom1[0] >= 2 or "exhibitionist" in Girl.Traits: #if custom 1:
                        $ Girl.Outfit = "custom1"
                        $ Agree = 1
                else:
                        call QuickOutfitCheck(Girl,3) #re-checks to see if it will work
                        if Girl.Custom1[0] >= 2:
                                $ Girl.Outfit = "custom1"
                                $ Agree = 1
        elif Custom == 5:
                $ Shame = Girl.Custom2[10]
                if Girl.Custom2[0] >= 2 or "exhibitionist" in Girl.Traits:
                        $ Girl.Outfit = "custom2"
                        $ Agree = 1
                else:
                        call QuickOutfitCheck(Girl,5) #re-checks to see if it will work
                        if Girl.Custom2[0] >= 2:
                                $ Girl.Outfit = "custom2"
                                $ Agree = 1
        else: #if Custom == 6:
                $ Shame = Girl.Custom3[10]
                if Girl.Custom3[0] >= 2 or "exhibitionist" in Girl.Traits:
                        $ Girl.Outfit = "custom3"
                        $ Agree = 1
                else:
                        call QuickOutfitCheck(Girl,6) #re-checks to see if it will work
                        if Girl.Custom3[0] >= 2:
                                $ Girl.Outfit = "custom3"
                                $ Agree = 1

        if Girl is RogueX:
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_r "Ооох, как в детстве."
                        elif Shame >= 50:
                            ch_r "Ты же понимаешь, что я почти голая, верно?"
                        elif Shame >= 25:
                            ch_r "Это довольно бесстыдно. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_r "Не знаю, наверное, я могла бы попробовать. . ."
                        else:
                            ch_r "Конечно, [Girl.Petname]."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_r "Да ладно тебе, я же буду совершенно голой!"
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_r "-Тебе- повезло, что я показала тебе это."
                        else:
                            $ Girl.FaceChange("bemused", 1)
                            ch_r "Извини, для меня это слишком."
        elif Girl is KittyX:
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_k "Хмм, я потихоньку возбуждаюсь. . ."
                        elif Shame >= 50:
                            ch_k "Это. . . немного распутно. . . но. . ."
                        elif Shame >= 25:
                            ch_k "Мне так не очень комфортно. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_k "Я попробую. . ."
                        else:
                            ch_k "Да, мне тоже нравится."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_k "Ты должно быть шутишь."
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_k "Я могу ходить в таком виде, только когда мы наедине."
                        else:
                            $ Girl.FaceChange("bemused", 1)
                            ch_k "Я не могу ходить в таком виде!"
        elif Girl is EmmaX:
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_e "Хмм, я потихоньку возбуждаюсь. . ."
                        elif Shame >= 50:
                            ch_e "Так. . . неприлично. . ."
                        elif Shame >= 25:
                            ch_e "Мне немного некомфортно ходить так. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_e "Я попробую. . ."
                        else:
                            ch_e "Да, мне тоже нравится."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_e "Ты должно быть шутишь."
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_e "Я могу ходить в таком виде, только когда мы наедине."
                        else:
                            $ Girl.FaceChange("bemused", 1)
                            ch_e "Я не могу ходить в таком виде!"
        elif Girl is LauraX:
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_l "Мммммм. . ."
                        elif Shame >= 50:
                            ch_l "Это. . . очень СМЕЛО. . ."
                        elif Shame >= 25:
                            ch_l "Почти ничего не прикрыто. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_l "Ага, ладно. . ."
                        else:
                            ch_l "Ага."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            if not Player.Male:
                                ch_l "Извращенка."
                            else:
                                ch_l "Извращенец."
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_l "Да, но не на людях."
                        else:
                            $ Girl.FaceChange("bemused", 1)
                            ch_l "Нет."
        elif Girl is JeanX:
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_j ". . ."
                        elif Shame >= 50:
                            ch_j "Довольно дерзко. . ."
                        elif Shame >= 25:
                            ch_j "Почти ничего не прикрыто. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_j "Конечно, как скажешь. . ."
                        else:
                            ch_j "Конечно."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_j "Как выльгарно."
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_j "Может ты и хочешь этого, но не я."
                        else:
                            $ Girl.FaceChange("bemused", 1)
                            ch_j "Ни за что."
        elif Girl is StormX:
                $ Girl.FaceChange("bemused", 1)
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_s "Ооох. . ."
                        elif Shame >= 25:
                            ch_s "Из-за тебя у меня будут неприятности. . ."
                        else:
                            ch_s "Да, неплохо."
                else:
                        #She's decided not to wear this out
                        $ Girl.FaceChange("bemused", 1)
                        ch_s "Боюсь, я не могу носить это."
        elif Girl is JubesX:
                $ Girl.FaceChange("bemused", 1)
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_v "Ооох. . ."
                        elif Shame >= 25:
                            ch_v "Воу, это прямо порнография. . ."
                        else:
                            ch_v "О, да, это подойдет. . ."
                else:
                        #She's decided not to wear this out
                        $ Girl.FaceChange("bemused", 1)
                        ch_v "Я совсем не могу носить это. . ."
        elif Girl is GwenX:
                $ Girl.FaceChange("bemused", 1)
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_g "Эм, ого. . ."
                        elif Shame >= 25:
                            ch_g "Ну, нам известно, что это за игра. . ."
                        else:
                            ch_g "Конечно, выглядит хорошо. . ."
                else:
                        #She's decided not to wear this out
                        $ Girl.FaceChange("bemused", 1)
                        ch_g "Ха, нет. . ."
        elif Girl is BetsyX:
                $ Girl.FaceChange("bemused", 1)
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_b "Ох, дорогуша. . ."
                        elif Shame >= 25:
                            ch_b "Это довольно. . . бесстыдно. . ."
                        else:
                            ch_b "Конечно. . ."
                else:
                        #She's decided not to wear this out
                        $ Girl.FaceChange("bemused", 1)
                        ch_b "Боюсь, что я не могу. . ."
        elif Girl is DoreenX:
                $ Girl.FaceChange("bemused", 1)
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_d "Ох. . . ого. . ."
                        elif Shame >= 25:
                            ch_d "Я не уверена. . . ты правда этого хочешь? . ."
                        else:
                            ch_d "Конечно."
                else:
                        #She's decided not to wear this out
                        $ Girl.FaceChange("bemused", 1)
                        ch_d "Я не могу разгуливать в таком виде!"
        elif Girl is WandaX:
                $ Girl.FaceChange("bemused", 1)
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_w "Хех, это забавная идея. . ."
                        elif Shame >= 25:
                            ch_w "Думаешь, я смогу?. ."
                        else:
                            ch_w "Конечно."
                else:
                        #She's decided not to wear this out
                        $ Girl.FaceChange("bemused", 1)
                        ch_w "Я не могу ходить в таком виде."
        return
# End Custom Out / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Outfit Shame / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label OutfitShame(Girl=0,Custom=3,Check=0,Count=0,Tempshame=50,Agree=1,Addhair=0): #rkeljsvgb
        #Custom determines which custom outfit is being checked against.
        #If Custom1 = 3, if gym = 4, if custom2 = 5, if custom3 = 6,  if sleepwear 7, if classwear 8, if private = 9, if swimsuit = 10
        # custom 11 is casual1, 12 is casual2
        #if not a check, then it is only applied if it's in a taboo area
        # Custom = 20 means it is just re-setting the current Shame level to be accurate.
        # Tempshame is a throwaway value, 0-50, Agree is whether she will wear it out, 2 if yes, 1 if only around you.
        # Addhair is for asking whether to include the hair cut in the outfit.
        # call OutfitShame(RogueX,20)
        $ Girl = GirlCheck(Girl)

        if not Check and Taboo <= 20 and Girl.Taboo <= 20 and Custom != 20:
                #if this is not a custom check and you're in a safe space,
                if Girl.Clothing[9] and bg_current in PersonalRooms:
                        #if there is a "private outfit" set, ask to change. (skips if halloween)
                        if "halloween" not in Player.DailyActions:
                                call Private_Outfit
                return

        if Girl.ChestNum() >= 5:   #Outerwear
                $ Count = 20
        elif Girl.ChestNum() >= 4: #Semi-Outerwear
                $ Count = 15
        elif Girl.ChestNum() >= 3: #Opaque Underwear
                $ Count = 10
        elif Girl.ChestNum() >= 2: #Lace
                $ Count = 5
        else:
                $ Count = 0

        #If she's wearing an overshirt

        if Custom == 20 and Girl.Uptop:
                $ Count = 0
        elif Girl.OverNum() >= 5: #Outerwear
                $ Count += 20
        elif Girl.OverNum() >= 4: #Open-Outerwear
                $ Count += 15
        elif Girl.OverNum() >= 3: #Opaque Underwear
                $ Count += 10
        elif Girl.OverNum() >= 2: #Lace/mesh
                $ Count += 5
        #else:
                #nothing

        if Girl.Pierce and Count <= 10:
                $ Count = -5

        $ Girl.FaceChange("sexy", 0)
        if Custom == 9 or Custom == 7:
            pass
        elif Count >= 20:
            $ Count = 20
            if Check:
                if Girl is RogueX:
                        ch_r "Ох, думаю, неплохо."
                elif Girl is KittyX:
                        ch_k "Думаю, это[Girl.like]хороший выбор."
                elif Girl is EmmaX:
                        ch_e "Мне нравится."
                elif Girl is LauraX:
                        ch_l "Неплохо."
                elif Girl is JeanX:
                        ch_j "Неплохо."
                elif Girl is StormX:
                        ch_s "Неплохо."
                elif Girl is JubesX:
                        ch_v "Ага, неплохо. . ."
                elif Girl is GwenX:
                        ch_g "Мне нравится. . ."
                elif Girl is BetsyX:
                        ch_b "Довольно неплохо. . ."
                elif Girl is DoreenX:
                        ch_d "Ох, как мило. . ."
                elif Girl is WandaX:
                        ch_w "Мне нравится. . ."
        elif not Check:
            pass
        elif Girl is RogueX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                        ch_r "В этом я буду выглядеть довольно сексуально. . ."
                elif Count >= 10:
                        ch_r "Нужно не мало смелости, чтобы носить подобное на людях."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_r "Не оставляет места для воображения. . ."
                elif Count >= 5:
                        $ Girl.FaceChange("startled", 1)
                        ch_r "Если честно, я думаю, что если я это надену, то будет скандал. . ."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                        ch_r "Ооох, я потихоньку возбуждаюсь. . ."
                else:
                        $ Girl.FaceChange("bemused", 1)
                        ch_r "Только когда мы наедине. . ."
        elif Girl is KittyX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                        ch_k "Какой сексуальный вариант."
                elif Count >= 10:
                        ch_k "Думаю[Girl.like]я не буду чувствовать себя комфортно в этом."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_k "Этот вариант слишком[Girl.like]откровенный. . ."
                elif Count >= 5:
                        $ Girl.FaceChange("startled", 1)
                        ch_k "Это[Girl.like]слишком распутный вариант."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                        ch_k "Неужели здесь так жарко? Уфф. . ."
                else:
                        $ Girl.FaceChange("bemused", 1)
                        ch_k "Я бы не стала это носить, ну, может, только когда мы наедине."
        elif Girl is EmmaX:
                if Count >= 10:
                        if ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_e "Довольно дерзкий вариант. . ."
                        else:
                                ch_e "Я не уверена насчет этого."
                elif Count >= 5:
                        if ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0):
                                ch_e "Обычно, я надеваю более закрытую одежду."
                        else:
                                $ Girl.FaceChange("startled", 1)
                                ch_e "Вырез слишком большой, даже для меня."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                        ch_e "Этот вариант ничего толком. . . не прикрывает, да?"
                else:
                        $ Girl.FaceChange("bemused", 1)
                        ch_e "Вырез слишком большой, чтобы выходить в люди."
        elif Girl is LauraX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                    ch_l "Неплохой вариант."
                elif Count >= 10:
                    ch_l "Как-то не очень ."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                    ch_l "Не знаю, мне кажется, этот вариант ничего толком не прикрывает."
                elif Count >= 5:
                    $ Girl.FaceChange("startled", 1)
                    ch_l "Я, если честно, не могу носить это."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                    ch_l ". . ."
                else:
                    $ Girl.FaceChange("bemused", 1)
                    ch_l "Я бы не стала выходить на улицу с торчащими сиськами."
        elif Girl is JeanX:
                if Count >= 10:# and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                    ch_j "Тебе, похоже, очень нравятся мои сиськи. . ."
                #elif Count >= 10:
                    #ch_j "The top's not really a good look."
                elif Count >= 5:# and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                    ch_j "У меня тут, похоже, сиськи торчат. . ."
                #elif Count >= 5:
                    #$ Girl.FaceChange("startled", 1)
                    #ch_j "I can't really wear this top out."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                    ch_j ". . ."
                else:
                    $ Girl.FaceChange("bemused", 1)
                    ch_j "Ты думаешь, я выйду на улицу с выставленными напоказ сиськами?"
        elif Girl is StormX:
                if Count >= 10:
                                ch_s "Прекрасный выбор."
                elif Count >= 5:
                        if StormX not in Rules:
                                ch_s "I do typically cover more than this around the school."
                        else:
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "Я не уверена, что Чарльз одобрил бы этот вариант."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                                ch_s "Разве мои прелести немного не выставылены. . . на показ?"
                else:
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "Я не уверена, что Чарльз одобрил бы этот вариант."
        elif Girl is JubesX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                    ch_v "Ага, неплохо. . ."
                elif Count >= 10:
                    ch_v "Я не уверена насчет этого варианта. . ."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                    ch_v "Я не уверена, этот вариант немного откровенный."
                elif Count >= 5:
                    $ Girl.FaceChange("startled", 1)
                    ch_v "Я не смогу это надеть."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                    ch_v "Я даже не знаю. . ."
                else:
                    $ Girl.FaceChange("bemused", 1)
                    ch_v "Ну, я никуда не смогу пойти в таком виде. . ."
        elif Girl is GwenX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                    ch_g "Конечно, без проблем. . ."
                elif Count >= 10:
                    ch_g "Этот вариант немного, эм. . ."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                    ch_g "Я не привыкла к такой одежде. . ."
                elif Count >= 5:
                    $ Girl.FaceChange("startled", 1)
                    ch_g "Этот вариант немного откровенный. . ."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                    ch_g "Хорошо. . ."
                else:
                    $ Girl.FaceChange("bemused", 1)
                    ch_g "Ха! Ты хочешь, чтобы я выстовила свои сиськи на радость людям?!"
        elif Girl is BetsyX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                    ch_b "Вполне неплохо. . ."
                elif Count >= 10:
                    ch_b "Я бы предпочла более закрытую одежду. . ."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                    ch_b "Этот вариант довольно открытый. . ."
                elif Count >= 5:
                    $ Girl.FaceChange("startled", 1)
                    ch_b "Обычно я не надеваю подобное на выход. . ."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                    ch_b "Ну и ну. . ."
                else:
                    $ Girl.FaceChange("bemused", 1)
                    ch_b "Как думаешь, я смогу выйти в таком виде в люди?"
        elif Girl is DoreenX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                    ch_d "Ооох, мне нравится. . ."
                elif Count >= 10:
                    ch_d "Мне кажется, этот вариант слишком откровенный. . ."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                    ch_d "В этом я буду недостаточно прикрыта. . ."
                elif Count >= 5:
                    $ Girl.FaceChange("startled", 1)
                    ch_d "Я не думаю, что надела бы это на выход. . ."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                    ch_d "Я даже не знаю. . ."
                else:
                    $ Girl.FaceChange("bemused", 1)
                    ch_d "Я никогда не выйду в таком виде."
        elif Girl is WandaX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                    ch_w "Слушай, отличный выбор. . ."
                elif Count >= 10:
                    ch_w "Может, если накинуть еще что-нибудь сверху. . ."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                    ch_w "Эта вещь особо ничего не прикрывает. . ."
                elif Count >= 5:
                    $ Girl.FaceChange("startled", 1)
                    ch_w "Не думаю, что смогу носить это. . ."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                    ch_w "Хех, это довольно дико. . ."
                else:
                    $ Girl.FaceChange("bemused", 1)
                    ch_w "Я -не могу- носить что-то подобное на людях."
        #end top check dialog

        $ Tempshame -= Count                  #Set Outfit shame for the upper half
        $ Count = 0

        if Girl.Legs and Girl.Panties and Girl.Legs != "short skirt": #If wearing both legs and panties
                    $ Count = 30
        else: #If she's missing something on her legs
                    if Girl.PantsNum() > 5:
                        #If wearing pants commando
                        $ Count = 25
                    elif Girl.PantsNum() == 5:
                        #If wearing a skirt commando
                        $ Count = 20
                    elif Girl.PantsNum() == "short skirt":
                        #If wearing a skirt that shows everything
                        $ Count = 0
                    elif Girl.PantiesNum() >= 8:
                        #If wearing shorts
                        $ Count = 25
                    elif Girl.PantiesNum() >= 6:
                        #If wearing only bikini bottoms
                        $ Count = 15
                    elif Girl.PantiesNum() >= 4:
                        #If wearing only panties
                        $ Count = 10
                    elif Girl.PantiesNum() >= 2:
                        #If wearing only lace panties
                        $ Count = 5
                    #else: 0

                    if Girl.HoseNum() >= 10:
                        #Factors in tights and hose
                        $ Count = 25 if Count < 25 else Count

                    if Girl.Over == "towel" and Count:
                        #If wearing a Towel and anything else
                        $ Count = 25
                    elif Girl.Over == "towel":
                        #If just wearing a Towel
                        $ Count = 15
        if not Check:
                    #If this isn't a custom check, skip this dialog stuff
                    pass
        elif Custom == 9 or Custom == 7:
                    pass
        elif Girl is RogueX:
                if Count >= 20:
                            if Girl.PantsNum() > 6:
                                ch_r "О, я думаю, что эти брюки прекрасно подойдут."
                            elif Girl.PantsNum() == 5:
                                ch_r "О, я думаю, что эта юбка прекрасно подойдет."
                            elif Girl.HoseNum() >= 10:
                                ch_r "О, думаю эти [Girl.Hose_display] прекрасно подойдут."
                            elif Girl.Panties == "shorts":
                                ch_r "О, я думаю, что эти шорты прекрасно подойдут."
                            elif Girl.Over == "towel":
                                ch_r "Полотенце. . . странный выбор. . ."
                            else:
                                ch_r "Теперь мне слишком холодно, [Girl.Petname]. . ."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_r "Мне нравится ходить без трусиков."
                            elif not Girl.Panties:
                                ch_r "Не уверена, что готова ходить без трусиков."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_r "Не остается места для воображения. . ."
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_r "Предупреждаю, я не буду расхаживать лишь в одних трусиках. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_r "Хмм, прохладно. . ."
                else:
                        ch_r "Только когда мы наедине. . ."
        elif Girl is KittyX:
                if Count >= 20:
                            if Girl.PantsNum() >= 5:
                                ch_k "а эти брюки очень мило смотрятся на мне."
                            elif Girl.Legs == "shorts":
                                ch_k "а это симпатичные шортики."
                            elif Girl.HoseNum() >= 10:
                                ch_k "Думаю, эти [Girl.Hose_display] отлично подойдут."
                            elif Girl.Over == "towel":
                                ch_k "Полотенце. . . странный выбор. . ."
                            else:
                                ch_k "Теперь мне прохладно."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_k "Мне нравится ходить без трусиков."
                            elif not Girl.Panties:
                                ch_k "Без трусиков как-то неудобно."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_k "Насчет этого, я не уверена. . ."
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_k "Я же почти голая. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_k "как-то прохладно. . ."
                else:
                        ch_k "только если[Girl.like]в комнате только ты да я. . ."
        elif Girl is EmmaX:
                if Count >= 20:
                            if Girl.PantsNum() > 5:
                                ch_e "а эти брюки мне всегда шли."
                            elif Girl.PantsNum() >= 5:
                                ch_e "а эта юбка мне всегда шла."
                            elif Girl.HoseNum() >= 10:
                                ch_e "Думаю, эти [Girl.Hose_display] отлично подойдут."
                            elif Girl.Over == "towel":
                                ch_e "Я не уверена, что хочу носить полотенце, [Girl.Petname]. . ."
                            else:
                                ch_e "Думаю, мне стоит надеть что-нибудь под низ, [Girl.Petname]. . ."
                            if not Girl.Panties:
                                if ApprovalCheck(Girl, 500, "I", TabM=0):
                                    ch_e "Честно говоря, мне нравится ходить без трусиков."
                                else:
                                    ch_e "Я не знаю, как вообще можно ходить без трусиков."
                elif Count >= 10:
                    if ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0):
                            ch_e "Надеюсь, ты не ждешь, что я буду ходить так. . ."
                    else:
                            $ Girl.FaceChange("angry", 1)
                            ch_e "Не знаю, как ходить так на людях. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_e "Повод испытать свои пределы."
                else:
                        ch_e "Я готова ходить так, пока мы наедине, но точно не на людях."
        elif Girl is LauraX:
                if Count >= 20:
                            if Girl.PantsNum() > 5:
                                ch_l "а эти брюки неплохо смотрятся."
                            elif Girl.PantsNum() >= 5:
                                ch_l "а эта юбка неплохо смотрится."
                            elif Girl.HoseNum() >= 10:
                                ch_l "а эти чулки [Girl.Hose_display] нормально смотрятся на мне."
                            elif Girl.Over == "towel":
                                ch_l "Полотенце. . . странный выбор. . ."
                            else:
                                ch_l "меня так продует."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_l "Без трусиков. . . клево."
                            elif not Girl.Panties:
                                ch_l "Без трусиков я чувствую себя слишком голой."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_l "Мне не нравится. . ."
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_l "Я не такая. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_l "Какой-то минимализм. . ."
                else:
                        ch_l "Я бы не хотела светить своей промежностью. . ."
        elif Girl is JeanX:
                if Count >= 20:
                            if Girl.PantsNum() > 5:
                                ch_j "Мне нравятся эти штаны. . ."
                            elif Girl.PantsNum() >= 5:
                                ch_j "Мне нравится эта юбка. . ."
                            elif Girl.HoseNum() >= 10:
                                ch_j "эти [Girl.Hose_display] неплохо смотрятся."
                            elif Girl.Over == "towel":
                                ch_j "Полотенце? . ."
                            else:
                                ch_j "может продуть. . ."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_j "Я не против ходить без трусиков. . ."
                            elif not Girl.Panties:
                                ch_j "Я не могу отказаться от трусиков. . ."
                #elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        #ch_j "I don't think I'm fully covered. . ."
                elif Count >= 10:
                        if (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                                $ Girl.FaceChange("sly", 1)
                        else:
                                $ Girl.FaceChange("angry", 1)
                        ch_j "То есть, ты хочешь чтобы моя киска была выставленна всем напоказ? . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_j "По сути на мне \"ничего\" нет. . ."
                else:
                        ch_j "Я не хочу выставлять себя всем напоказ. . ."
        elif Girl is StormX:
                if Girl.PantsNum() > 5:
                            ch_s "а эти брюки мне всегда шли."
                elif Girl.PantsNum() >= 5:
                            ch_s "а эта юбка мне всегда шла."
                elif Girl.HoseNum() >= 10:
                            ch_s "Пожалуй, эти [Girl.Hose_display] неплохо смотрятся."
                elif Girl.Over == "towel":
                            ch_s "Я не уверена, что хочу носить полотенце, [Girl.Petname]. . ."
                else:
                            ch_s "Довольно холодно, [Girl.Petname]. . ."
                if not Girl.Panties:
                    if ApprovalCheck(Girl, 500, "I", TabM=0):
                            ch_s "По правде говоря, мне нравится ходить без трусиков."
                    else:
                            ch_s "Я чувствую себя обнаженной без трусиков. . ."
                if Count >= 10 and StormX not in Rules:
                            $ Girl.FaceChange("bemused", 1)
                            ch_s "Не думаю, что Чарльз позволил бы мне разгуливать в таком виде."
                elif StormX in Rules and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                            ch_s "Довольно смелый образ ты предлагаешь."
                else:
                            ch_s "Не думаю, что Чарльз позволил бы мне разгуливать в таком виде."
        elif Girl is JubesX:
                if Count >= 20:
                            if Girl.PantsNum() > 6:
                                ch_v "а эти брюки неплохо смотрятся."
                            elif Girl.PantsNum() >= 6:
                                ch_v "а эти шорты неплохо смотрятся."
                            elif Girl.PantsNum() >= 5:
                                ch_v "а эта юбка неплохо смотрится."
                            elif Girl.HoseNum() >= 10:
                                ch_v "а эти [Girl.Hose_display] нормально смотрятся на мне."
                            elif Girl.Over == "towel":
                                ch_v "Полотенце. . . странный выбор. . ."
                            else:
                                ch_v "но я в этом не уверена. . ."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_v "Думаю, теперь мы не будем беспокоится о трусиках?"
                            elif not Girl.Panties:
                                ch_v "Я не думаю, что хотела бы ходить без трусиков. . ."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_v "Слишком откровенно. . ."
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_v "Слишком откровенно. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_v "Ого, это. . . слишком. . ."
                else:
                        ch_v "Если честно, мне не очень нравится трясти прелестями. . ."
        elif Girl is GwenX:
                if Count >= 20:
                            if Girl.PantsNum() > 6:
                                ch_g "а эти брюки неплохо смотрятся."
                            elif Girl.PantsNum() >= 6:
                                ch_g "а эти шорты неплохо смотрятся."
                            elif Girl.PantsNum() >= 5:
                                ch_g "а эта юбка неплохо смотрится."
                            elif Girl.HoseNum() >= 10:
                                ch_g "а эти [Girl.Hose_display] нормально смотрятся на мне."
                            elif Girl.Over == "towel":
                                ch_g "Полотенце - странный выбор. . ."
                            else:
                                ch_g "но. . . я не уверена. . ."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_g "Я чувствую ветерок между ног. . ."
                            elif not Girl.Panties:
                                ch_g "Мне, эм, вроде как нравится носить. . . трусики?"
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_g "Слишком, эм, откровенно. . ."
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_g "Почти ничего не прикрывает. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_g "Ну, как говориться \"в чужой монастырь\". . ."
                else:
                        ch_g "Я девушка рейтинга \"без возврастных ограничений\". . ."
                        ch_g "По крайней мере, на людях."
        elif Girl is BetsyX:
                if Count >= 20:
                            if Girl.PantsNum() > 6:
                                ch_b "а эти брюки хороши."
                            elif Girl.PantsNum() >= 6:
                                ch_b "а эти шорты хороши."
                            elif Girl.PantsNum() >= 5:
                                ch_b "а эта юбка хороша."
                            elif Girl.HoseNum() >= 10:
                                ch_b "а эти [Girl.Hose_display] отлично подходят."
                            elif Girl.Over == "towel":
                                ch_b "Полотенце - странный выбор. . ."
                            else:
                                ch_b "но. . . насчет этого я не уверена. . ."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_b "Обычно я не хожу без трусиков. . ."
                            elif not Girl.Panties:
                                ch_b "У меня нет никакого желания ходить без трусиков. . ."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_b "Довольно откровенно. . . однако. . ."
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_b "Довольно откровенно. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_b "Думаю, я могу попробовать. . ."
                else:
                        ch_b "Я бы предпочла на людях быть более прикрытой."
        elif Girl is DoreenX:
                if Count >= 20:
                            if Girl.PantsNum() > 6:
                                ch_d "а эти брюки неплохо смотрятся."
                            elif Girl.PantsNum() >= 6:
                                ch_d "а эти шорты неплохо смотрятся."
                            elif Girl.PantsNum() >= 5:
                                ch_d "а эта юбка неплохо смотрится."
                            elif Girl.HoseNum() >= 10:
                                ch_d "а эти [Girl.Hose_display] нормально смотрятся на мне."
                            elif Girl.Over == "towel":
                                ch_d "Полотенце - странный выбор. . ."
                            else:
                                ch_d "но. . . я не уверена. . ."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_d "Обычно я ношу трусики. . ."
                            elif not Girl.Panties:
                                ch_d "Обычно я адеваю трусики с чем-то подобным. . ."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_d "Довольно откровенно. . . -но-. . ."
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_d "Довольно откровенно. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_d "Я могу попробовать. . ."
                else:
                        ch_d "Если я хочу выйти на улицу, я должна быть более прикрытой."
        elif Girl is WandaX:
                if Count >= 20:
                            if Girl.PantsNum() > 6:
                                ch_w "а эти брюки мне очень идут."
                            elif Girl.PantsNum() >= 6:
                                ch_w "а эти шорты мне очень идут."
                            elif Girl.PantsNum() >= 5:
                                ch_w "а это платье мне очень идет."
                            elif Girl.HoseNum() >= 10:
                                ch_w "а эти [Girl.Hose_display] мне очень идут."
                            elif Girl.Over == "towel":
                                ch_w "Обычно я не выхожу в люди в полотенце. . ."
                            else:
                                ch_w "Я не уверена. . ."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_w "Я обычно -надеваю- трусики. . ."
                            elif not Girl.Panties:
                                ch_w "Я обычно -надеваю- трусики, но. . ."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_w "Довольно откровенно. . . -но-. . ."
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_w "В этом я почти не прикрыта. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_w "Хммм, ага. . ."
                else:
                        ch_w "Я ни за что не смогу выйти в люди в таком виде."
        # End Panties check dialog

        $ Tempshame -= Count                  #Set Outfit shame for the lower half

        if Check:
                #if this is a custom outfit check
                if Check == 2:
                    ch_p "Ну, как тебе?"
                elif Custom == 4:
                    ch_p "Ты будешь тренироваться в этом?"
                elif Custom == 7:
                    ch_p "Ты будешь спать в этом?"
                else:
                    ch_p "Ты наденешь это на выход?"

                $ Girl.FaceChange("sexy", 0)
                if Girl.PantsNum() > 2:
                    pass        #if she's wearing pants
                elif Girl == StormX and StormX in Rules:
                    pass
                elif Girl.PantiesNum() > 2 and (Girl.SeenPanties or ApprovalCheck(Girl, 900, TabM=0)):
                    pass        #no pants, but panties
                elif Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=0):
                    pass        #no panties, but she's fine with that
                else:
                    $ Agree = 0 #not fine with it

                if not Agree:
                    pass
                elif Girl == StormX and StormX in Rules:
                    pass
                elif Girl.OverNum() > 2:
                    pass        #if she's wearing a top
                elif Girl.ChestNum() > 2 and (Girl.SeenChest or ApprovalCheck(Girl, 900, TabM=0)):
                    pass        #no top, but bra
                elif Girl.SeenChest or ApprovalCheck(Girl, 1200, TabM=0):
                    pass        #no bra, but she's fine with that
                else:
                    $ Agree = 0 #not fine with it

                if Check == 2 and Agree:
                            #if checking to see if she'll drop the dressing screen. . .
                            $ Girl.Shame = Tempshame
                            $ Girl.FaceChange("sly")
                            if Girl is RogueX:
                                    ch_r "Вроде, неплохо выглядит. . ."
                            elif Girl is KittyX:
                                    if not Player.Male:
                                        ch_k "Думаю, ты собрала милый наряд. . ."
                                    else:
                                        ch_k "Думаю, ты собрал милый наряд. . ."
                            elif Girl is EmmaX:
                                    ch_e "Полагаю, меня он устраивает. . ."
                            elif Girl is LauraX:
                                    ch_l "Хм, неплохо. . ."
                            elif Girl is JeanX:
                                    ch_j "Он и правда хорошо смотрится на мне. . ."
                            elif Girl is StormX:
                                    ch_s "Почему бы и нет. . ."
                            elif Girl is JubesX:
                                    ch_v "Конечно, смотри. . ."
                            elif Girl is GwenX:
                                    ch_g "Ну, ладно, смотри. . ."
                            elif Girl is BetsyX:
                                    ch_b "Конечно, взгляни. . ."
                            elif Girl is DoreenX:
                                    ch_d "Конечно! Посмотри. . ."
                            elif Girl is WandaX:
                                    ch_w "Конечно, взгляни. . ."
                            hide DressScreen
                            return 1
                if not Agree:
                            #she isn't even comfortable with you seeing it
                            $ Girl.FaceChange("bemused", 2,Eyes="side")
                            if Girl is RogueX:
                                    ch_r "Мне не очень комфортно в этом. . ."
                            elif Girl is KittyX:
                                    ch_k "Думаю, мне в этом некомфортно. . ."
                            elif Girl is EmmaX:
                                    if Player.Male:
                                        ch_e "Я бы не хотела, чтобы ты меня в этом видел. . ."
                                    else:
                                        ch_e "Я бы не хотела, чтобы ты меня в этом видела. . ."
                            elif Girl is LauraX:
                                    ch_l "Тебе придется это заслужить."
                            elif Girl is JeanX:
                                    ch_j "Он милый, но я не могу ходить в нем."
                            elif Girl is StormX:
                                    if Player.Male:
                                        ch_s "Думаю, ты решил посмеяться надо мной. . ."
                                    else:
                                        ch_s "Думаю, ты решила посмеяться надо мной. . ."
                            elif Girl is JubesX:
                                    ch_v "Я не могу позволить тебе видеть меня в этом. . ."
                            elif Girl is GwenX:
                                    ch_g "Я, эм, должна сначала переодеться. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я бы предпочла сначала надеть что-нибудь другое. . ."
                            elif Girl is DoreenX:
                                    ch_d "Сначала я бы хотела надеть что-нибудь другое. . ."
                            elif Girl is WandaX:
                                    ch_w "Хех, ну да, ну да. . ."
                            menu:
                                extend ""
                                "Хорошо, тогда можешь снова надеть свою обычную одежду.":
                                            $ Girl.OutfitChange(Changed=1)
                                            hide DressScreen
                                "Ладно, давай тогда подберем что-нибудь другое.":
                                            pass
                            $ Girl.FaceChange("smile", 1)
                            if Girl is RogueX:
                                    ch_r "Спасибо, [Girl.Petname]."
                            elif Girl is KittyX:
                                    ch_k "Спасибо."
                            elif Girl is EmmaX:
                                    ch_e "Благодарю."
                            elif Girl is LauraX:
                                    ch_l "Спасибо."
                            elif Girl is JeanX:
                                    ch_j ". . . я так и сказала."
                            elif Girl is StormX:
                                    ch_s "Хорошо. . ."
                            elif Girl is JubesX:
                                    ch_v "Клево, клево. . ."
                            elif Girl is GwenX:
                                    ch_g "Спасибо. . ."
                            elif Girl is BetsyX:
                                    ch_b "Благодарю. . ."
                            elif Girl is DoreenX:
                                    ch_d "Спасибо. . ."
                            elif Girl is WandaX:
                                    ch_w "Конечно."
                            return
                if Girl is RogueX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_r "Уже довольно поздно переживать об этом, верно?"
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                ch_r "Ммм. . . да, с удовольствием. . ."
                                $ Girl.Statup("Lust", 80, 10)
                        elif Custom == 7:
                                #Sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                        ch_r "Немного скандально, но я согласна."
                                elif Tempshame >= 15:
                                        ch_r "Да, ты этого стоишь."
                                else:
                                        ch_r "Конечно, он милый."
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_r "Да, думаю, мне нравится такой стиль, я бы это носила."
                        elif Tempshame <= 15:
                            if ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0):
                                ch_r "Это довольно откровенный наряд, но я могу носить его."
                            else:
                                $ Girl.FaceChange("bemused", 1)
                                ch_r "Думаю, нужно быть очень смелой, чтобы носить его."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_r "Конечно, можно и в этом купаться. . ."
                        elif Tempshame <= 25:
                            if ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0):
                                ch_r "Откровенно, но, думаю, я справюсь."
                            else:
                                $ Girl.FaceChange("angry", 1)
                                ch_r "Я точно не собираюсь носить это."
                                $ Agree = 0
                        elif ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0):
                                $ Girl.FaceChange("bemused", 1)
                                ch_r "Я не так его себе представляла. . . но да."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_r "Ты должно быть шутишь."
                                $ Agree = 0
                elif Girl is KittyX:
                        if Girl.Taboo >= 40: #Girl.Loc != "bg player" and Girl.Loc != "bg kitty":
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_k "Немного поздно переживать, верно?"
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                ch_k "Я возбуждаюсь от одной мысли об этом. . ."
                                $ Girl.Statup("Lust", 80, 10)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_k "Конечно, выглядит мило!"
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_k "Горячий наряд, правда?"
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    ch_k "Это[Girl.like]довольно откровенный наряд, но ладно."
                                elif Tempshame >= 15:
                                    ch_k "Довольно неприлично так ходить, но мне нравится."
                                else:
                                    ch_k "Да, неплохо."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_k "Слишком распутный наряд, я не могу его надеть."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_k "Это милый купальник. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_k "Такой сексуальный, думаю, я смогу его носить."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_k "Он -слишком- сексуальный для выхода в люди."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_k "БОЖЕ, я не могу поверить, что делаю это."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_k "Ни-ког-да."
                                $ Agree = 0
                elif Girl is EmmaX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                "Она оглядывается по сторонам."
                                ch_e "Это вопрос с подвохом?"
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                ch_e "От одной мысли об этом, я дико возбуждаюсь. . ."
                                $ Girl.Statup("Lust", 80, 10)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_e "Да, это прекрасный выбор."
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_e "Довольно дерзко, как я могу устоять от такого?"
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    ch_e "Ты же понимаешь, что я могу надеть такое только когда мы наедине."
                                else:
                                    ch_e "Это удобный наряд."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_e "Слишком дерзко, тебе не кажется?"
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_e "Отлично, это приличный купальник. . ."
                        elif Tempshame >= 15 and "public" not in Girl.History:
                                ch_e "Он очень непристойный. . . в хорошем смысле."
                                $ Agree = 0
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_e "Он очень непристойный. . . в хорошем смысле."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_e "Даже не могу представить, как надеваю его, [Girl.Petname]."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_e "Этот наряд, безусловно, выходит за рамки."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_e "Даже я не могу надеть его."
                                $ Agree = 0
                elif Girl is LauraX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_l "Думаю, уже поздновато беспокоиться."
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                $ Girl.Statup("Lust", 80, 10)
                                $ Girl.FaceChange("sexy", 2)
                                ch_l ". . ."
                                $ Girl.FaceChange("sexy", 1)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_l "Не вижу причин отказываться."
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_l "Выглядит неплохо, правда?"
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    if not Player.Male:
                                        ch_l "Конечно, извращенка."
                                    else:
                                        ch_l "Конечно, извращенец."
                                elif Tempshame >= 15:
                                    ch_l "Конечно, почему бы и нет."
                                else:
                                    ch_l "Да, наверное."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_l "Я не могу ходить в этом, не демонстрируя интимные части своего тела."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_l "Да, я буду плавать в нем. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_l "Пойдет."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_l "Нет, слишком распутная одежда."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_l "Довольно дерзко, да?"
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_l "Будто я буду это носить."
                                $ Agree = 0
                elif Girl is JeanX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_j "Уже поздно отступать, да?"
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                $ Girl.Statup("Lust", 80, 10)
                                $ Girl.FaceChange("sexy", 2)
                                ch_j ". . ."
                                $ Girl.FaceChange("sexy", 1)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_j "Конечно, как скажешь."
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_j "Вполне неплохо. . ."
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    ch_j "Если ты успокоишься. . ."
                                elif Tempshame >= 15:
                                    ch_j "Да, конечно."
                                else:
                                    ch_j "Почему бы и нет."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_j "Меня устраивает. . ."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_j "Да, конечно."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_j "Этот наряд может вскружить многим парням головы. . ."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_j "Я бы не хотела никому подпровлять память. . ."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_j "Конечно, соблазнительный наряд."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_j "Ты должно быть шутишь."
                                $ Agree = 0
                elif Girl is StormX:
                        #Storm will approve anything if you clear it with Xavier, and is more likely to be fine with risky looks
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                "Она оглядывается по сторонам."
                                ch_s "Кажется, уже поздно задавать вопросы. . ."
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                ch_s "Меня. . . возбуждает эта твоя идея. . ."
                                $ Girl.Statup("Lust", 80, 10)
                        elif Tempshame <= 10:
                                $ Girl.FaceChange("smile")
                                ch_s "Да, это прекрасный выбор."
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 20:
                                    ch_s "Это прекрасный наряд."
                                else:
                                    ch_s "Этот наряд немного более откровенный, чем я привыкла. . ."
                        elif StormX in Rules:
                                ch_s "Не вижу причин отказываться. . ."
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "Пожалуй, неплохо было бы поплавать в этом. . ."
                        elif Tempshame <= 20 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_s "Он, безусловно, расширяет границы хорошего вкуса. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "Я сомневаюсь, что Чарльз его одобрил бы, но кто будет его спрашивать?"
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "Боюсь, Чарльз никогда его не одобрит."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "Я сомневаюсь, что Чарльз его одобрил бы, но кто будет его спрашивать?"
                        else:
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "Боюсь, Чарльз никогда его не одобрит."
                                $ Agree = 0
                elif Girl is JubesX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_v "Думаю, поезд ушел. . ."
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                $ Girl.Statup("Lust", 80, 10)
                                $ Girl.FaceChange("sexy", 2)
                                ch_v ". . ."
                                $ Girl.FaceChange("sexy", 1)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_v "Наверное, можно?"
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_v "Я выгляжу очень сексуально, правда?"
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    if not Player.Male:
                                        ch_v "Как скажешь, извращенка."
                                    else:
                                        ch_v "Как скажешь, извращенец."
                                elif Tempshame >= 15:
                                    ch_v "Конечно, почему бы и нет."
                                else:
                                    ch_v "Конечно. . . наверное."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_v "Думаю, в нем я замерзну."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_v "Я могла бы плавать в нем. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_v "Думаю, это нормальный выбор. . ."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_v "Я не могу ходить в нём."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_v "Довольно сексуальный наряд, правда?"
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_v "Будто я буду это носить."
                                $ Agree = 0
                elif Girl is GwenX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_g "Ну. . . наверное. . . давать заднюю уже поздно. . ."
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                $ Girl.Statup("Lust", 80, 10)
                                $ Girl.FaceChange("sexy", 2)
                                ch_g ". . . Ага, думаю, я могу ходить так. . ."
                                $ Girl.FaceChange("sexy", 1)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_g "Конечно?"
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_g "Он поможет мне выглядеть хорошо."
                        elif Custom == 7:
                            #if it's sleepwear
                            $ Girl.FaceChange("bemused", 1)
                            if Tempshame >= 30:
                                ch_g "Ну. . . для сна, пойдет. . ."
                            elif Tempshame >= 15:
                                ch_g "Конечно, почему бы и нет."
                            else:
                                ch_g "Конечно. . . наверное."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_g "Эм, не очень хорошо прикрывает. . ."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_g "Я могла бы плавать в нем. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_g "Думаю, это нормальный выбор. . ."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("smile", 2)
                                ch_g "Я -никак- не это надеть."
                                $ Girl.FaceChange("normal", 1)
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_g "Милый, правда?"
                        else:
                                $ Girl.FaceChange("smile", 2)
                                ch_g "Ха!"
                                $ Girl.FaceChange("normal", 1)
                                $ Agree = 0
                elif Girl is BetsyX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_b "Пожалуй, отступать надо было раньше. . ."
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                $ Girl.Statup("Lust", 80, 10)
                                $ Girl.FaceChange("sexy", 2)
                                ch_b ". . . Я. . . пожалуй, могу. . ."
                                $ Girl.FaceChange("sexy", 1)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_b "Конечно?"
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_b "На мне он действительно выглядит сногсшибательно."
                        elif Custom == 7:
                            #if it's sleepwear
                            $ Girl.FaceChange("bemused", 1)
                            if Tempshame >= 30:
                                ch_b "Пожалуй. . . для сна в самый раз. . ."
#                            elif Tempshame >= 15:
#                                ch_b "Sure, why not."
                            else:
                                ch_b "Конечно."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_b "Ох, он недостаточно прикрывает меня. . ."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_b "Из этого получится отличный купальный костюм. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_b "Приемлемо. . ."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("smile", 2)
                                ch_b "Я ни за что не смогу выйти в нём в люди."
                                $ Girl.FaceChange("normal", 1)
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_b "Ох, очень милый наряд. . ."
                        else:
                                $ Girl.FaceChange("angry", 2)
                                ch_b "Ты -должно быть- шутишь!"
                                $ Girl.FaceChange("normal", 1)
                                $ Agree = 0
                elif Girl is DoreenX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_d "Ну, уже немного поздно беспокоиться об этом. . ."
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                $ Girl.Statup("Lust", 80, 10)
                                $ Girl.FaceChange("sexy", 2)
                                ch_d ". . . Ну. . . может быть. . ."
                                $ Girl.FaceChange("sexy", 1)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_d "Конечно?"
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_d "Он отлично подчеркивает мою фигуру. . ."
                        elif Custom == 7:
                            #if it's sleepwear
                            $ Girl.FaceChange("bemused", 1)
                            if Tempshame >= 30:
                                ch_d "Наверное. . . я могу спать в этом. . ."
#                            elif Tempshame >= 15:
#                                ch_d "Sure, why not."
                            else:
                                ch_d "Конечно."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_d "Он особо не прикрывает тело. . ."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_d "Я могла бы пойти в этом поплавать. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_d "Ага, выглядит мило. . ."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("smile", 2)
                                ch_d "Я никак не могу это надеть."
                                $ Girl.FaceChange("normal", 1)
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_d "Ох, выглядит очень мило."
                        else:
                                $ Girl.FaceChange("angry", 2)
                                ch_d "Ты, наверное, шутишь!"
                                $ Girl.FaceChange("normal", 1)
                                $ Agree = 0
                elif Girl is WandaX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_w "Эм. . . ладно?"
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                $ Girl.Statup("Lust", 80, 10)
                                $ Girl.FaceChange("sexy", 2)
                                ch_w ". . . ага. . ."
                                $ Girl.FaceChange("sexy", 1)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_w "Хорошо?"
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_w "Мне нравится, как я выгляжу в нем. . ."
                        elif Custom == 7:
                            #if it's sleepwear
                            $ Girl.FaceChange("bemused", 1)
                            if Tempshame >= 30:
                                ch_w "Я могу спать в этом. . ."
#                            elif Tempshame >= 15:
#                                ch_w "Sure, why not."
                            else:
                                ch_w "Конечно."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_w "Ага, если накинуть что-нибудь сверху. . ."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_w "Конечно, для плавания в самый раз. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_w "Ага, выглядит мило. . ."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("smile", 2)
                                ch_w "Конечно, почему нет."
                                $ Girl.FaceChange("normal", 1)
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_w "Ага, в самый раз."
                        else:
                                $ Girl.FaceChange("angry", 2)
                                ch_w "Да ни за что."
                                $ Girl.FaceChange("normal", 1)
                                $ Agree = 0
                #End check dialog

                menu:
                    "Хотели бы вы добавить в наряд текущую прическу?"
                    "Да":
                        $ Addhair = 1
                    "Нет":
                        $ Addhair = 0
                #$ Girl.OutfitShame[Custom] = Tempshame
                if Custom == 5:
                        $ Girl.Custom2 = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame,Girl.Boots,Girl.Hat]
                        $ Girl.Custom2[8] = Girl.Hair if Addhair else 0
                        $ Girl.Custom2[0] = 2 if Agree else 1
                        call Clothing_Schedule_Check(Girl,5,1) #checks to make sure it's still SFW
                elif Custom == 6:
                        $ Girl.Custom3 = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame,Girl.Boots,Girl.Hat]
                        $ Girl.Custom3[8] = Girl.Hair if Addhair else 0
                        $ Girl.Custom3[0] = 2 if Agree else 1
                        call Clothing_Schedule_Check(Girl,6,1)
                elif Custom == 4:
                    if Agree:
                        $ Girl.Gym = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame,Girl.Boots,Girl.Hat]
                        $ Girl.Gym[8] = Girl.Hair if Addhair else 0
                        call Clothing_Schedule_Check(Girl,4,1)
                elif Custom == 7:
                        $ Girl.Sleepwear = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame,Girl.Boots,Girl.Hat]
                        $ Girl.Sleepwear[8] = Girl.Hair if Addhair else 0
                        $ Girl.Sleepwear[0] = 2 if Agree else 1
                elif Custom == 10:
                    if Agree:
                        $ Girl.Swim = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame,Girl.Boots,Girl.Hat]
                        $ Girl.Swim[8] = Girl.Hair if Addhair else 0
                elif Custom == 3:
                        $ Girl.Custom1 = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame,Girl.Boots,Girl.Hat]
                        $ Girl.Custom1[8] = Girl.Hair if Addhair else 0
                        $ Girl.Custom1[0] = 2 if Agree else 1
                        call Clothing_Schedule_Check(Girl,3,1)
                elif Custom == 11:
                        $ Girl.Casual1 = [3,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame,Girl.Boots,Girl.Hat]
                        $ Girl.Casual1[8] = Girl.Hair if Addhair else 0
                        $ Girl.Casual1[0] = 3 if Agree else 2
                elif Custom == 12:
                        $ Girl.Casual2 = [3,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame,Girl.Boots,Girl.Hat]
                        $ Girl.Casual2[8] = Girl.Hair if Addhair else 0
                        $ Girl.Casual2[0] = 3 if Agree else 2
                else:
                        "Tell Oni Custom Outfit was [Custom]"
                        $ RogueX.gibberish = 5
        elif Girl.Taboo <= 20:
                # halves shame level if she's comfortable
                $ Tempshame /= 2

        $ Girl.Shame = Tempshame

        if Custom == 20:
                # This returns the scene if it's a check Shame adjustment
                return

        if Check:
                pass
        elif bg_current == "HW Party" or (bg_current == "bg player" and "halloween" in Player.DailyActions):
                #skips because it's at the party and they should be in costume only
                pass
        elif "exhibitionist" in Girl.Traits and Tempshame <= 20:
                #If she's an exhibitionist
                pass
        elif Girl is StormX and StormX in Rules:
                pass
        elif Tempshame <= 12:
                #If the outfit is tame
                pass
        elif Girl.Over == "towel" and Girl.Loc == "bg showerroom":
                #If she's in a towel but it's appropriate
                pass
        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1500) or ApprovalCheck(Girl, 500, "I")):
                #If the outfit is hot but she's ok
                pass
        elif Tempshame <= 20 and (Girl.Loc == "bg dangerroom" or Girl.Loc == "bg pool"):
                #If the outfit is light but she's in the gym or pool
                pass
        elif Tempshame <= 20 and (ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 650, "I")):
                #If the outfit is sexy but she's cool with that
                pass
        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2000) or ApprovalCheck(Girl, 700, "I")):
                #If the outfit is sexy but she's cool with that
                pass
        elif (ApprovalCheck(Girl, 2500) or ApprovalCheck(Girl, 800, "I")):
                #If the outfit is very scandalous but she's ok with that
                pass
        elif Girl.Loc == "bg dangerroom" and Girl.Outfit == "gym":
                $ Girl.OutfitChange("gym",Changed = 1)
        elif not Girl.Taboo:
                pass
        elif Girl.Outfit == "swimwear" and bg_current == "bg pool":
                pass
        elif bg_current == "bg pool" and Girl.ChestNum() >= 3 and Girl.PantiesNum() >= 6:
                pass
        elif Girl.Outfit == "gym" and bg_current == "bg dangerroom":
                pass
        else:
                #if this is a called outfit modesty check. . .
                if Girl.Loc == bg_current:
                        if Girl is RogueX:
                                ch_r "Я сейчас вернусь, мне нужно переодеться."
                        elif Girl is KittyX:
                                ch_k "Секундочку, я быстренько переоденусь."
                        elif Girl is EmmaX:
                                ch_e "Секунду, я схожу переоденусь."
                        elif Girl is LauraX:
                                ch_l "Одну секунду, я быстро переоденусь."
                        elif Girl is JeanX:
                                ch_j "Подожди, я схожу переоденусь."
                        elif Girl is StormX:
                                ch_s "Мне нужно будет переодеться во что-то более солидное."
                        elif Girl is JubesX:
                                ch_v "Мне нужно быстро что-то надеть. . ."
                        elif Girl is GwenX:
                                ch_g "Я, эм, позволь мне накинуть что-нибудь еще. . ."
                        elif Girl is BetsyX:
                                ch_b "Одну минуту, позволь мне переодеться во что-нибудь другое. . ."
                        elif Girl is DoreenX:
                                ch_d "Подожди секунду, мне нужно переодеться. . ."
                        elif Girl is WandaX:
                                ch_w "Мне нужно переодеться."
                if Girl.Loc == "bg dangerroom":
                        $ Girl.Outfit =  "gym"
                elif Girl.Loc == "bg pool" and Girl.Swim[0]:
                        $ Girl.Outfit =  "swimwear"
                else:
                        $ Girl.Outfit = renpy.random.choice(["casual1", "casual2"])

                $ Girl.AddWord(1,"modesty","modesty")  #sets a flag that this has happened before
                $ Girl.Water = 0
                $ Girl.OutfitChange(Changed=1)
                if Girl is RogueX:
                        ch_r "Эта одежда не подходит для \"выхода\"."
                elif Girl is KittyX:
                        ch_k "Я бы не хотела, чтобы меня видели в этом."
                elif Girl is EmmaX:
                        ch_e "Я бы не хотела выглядеть \"неприемлемо\"."
                elif Girl is LauraX:
                        ch_l "Эта одежда не совсем подходит для \"выхода\"."
                elif Girl is JeanX:
                        ch_j "Не пойдет."
                elif Girl is StormX:
                        ch_s "Боюсь, Чарльз не хотел бы, чтобы студенты видели меня в этом."
                elif Girl is JubesX:
                        ch_v "Эта одежда, вроде как. . . для интимной обстановки. . ."
                elif Girl is GwenX:
                        ch_g "Я. . . не хочу ходить в этом. . ."
                elif Girl is BetsyX:
                        ch_b "Я не думаю, что мне стоит ходить в таком виде. . ."
                elif Girl is DoreenX:
                        ch_d "Я забыла, что на мне надето. . ."
                elif Girl is WandaX:
                        ch_w "Нельзя, чтобы меня увидели в этом."
        return
#End Custom clothes check. / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Quick Outfit Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label QuickOutfitCheck(Girl=0, Custom = 3, Count = 0, Tempshame = 50, Agree = 1, HolderOutfit =[]): #rkeljsvg
        #Custom determines which custom outfit is being checked against.
        #If Custom1 = 3, if gym = 4, if custom2 = 5, if custom3 = 6,  if sleepwear 7, if classwear 8, if private = 9, if swimsuit = 10
        # Tempshame is a throwaway value, 0-50, Agree is whether she will wear it out, 2 if yes, 1 if only around you.
        # call QuickOutfitCheck(RogueX,20)

        $ Girl = GirlCheck(Girl)

        if Custom == 3:
                $ HolderOutfit = Girl.Custom1[:] #fills Holder with the values of the sent uni. . .
        elif Custom == 5:
                $ HolderOutfit = Girl.Custom2[:] #fills Holder with the values of the sent uni. . .
        elif Custom == 6:
                $ HolderOutfit = Girl.Custom3[:] #fills Holder with the values of the sent uni. . .
#        elif Custom == 20:
#                $ HolderOutfit = Girl.TempClothes[:] #fills Holder with the values of the sent uni. . .
        elif Custom == 7:
                $ HolderOutfit = Girl.Sleepwear[:] #fills Holder with the values of the sent uni. . .
        elif Custom == 4:
                $ HolderOutfit = Girl.Gym[:] #fills Holder with the values of the sent uni. . .
        elif Custom == 10:
                $ HolderOutfit = Girl.Swim[:] #fills Holder with the values of the sent uni. . .
        else:
                "Tell Oni, Outfit check, [Custom]."
                return

        #end Holder setting. . .

        #Chests
        while len(HolderOutfit) < 13:
                $ HolderOutfit.append(0)

        if HolderOutfit[5] in ("tank","white tank","button tank","sports bra","tube top","corset"):
                $ Count = 20
#        elif HolderOutfit[5] == "wolvie top":
#                $ Count = 10
        elif HolderOutfit[5] in ("lace bra","lace corset"):
                $ Count = 5
        elif HolderOutfit[5]:
                #any other bra
                $ Count = 10
        elif HolderOutfit[7] == "suspenders" or HolderOutfit[7] == "suspenders2":
                $ Count = 5
        else:
                $ Count = 0

        #Overs
        if HolderOutfit[3] in ("nighty","mesh top"):
                $ Count += 5
        elif HolderOutfit[3] == "towel":
            if Girl is EmmaX:
                $ Count += 5
            elif Girl is StormX:
                pass
            else:
                $ Count += 10
        elif HolderOutfit[3] == "open suit":
                pass
        elif HolderOutfit[3] in ("jacket","dress","pink top") or HolderOutfit[7] == "jacket":
                $ Count += 15
        elif HolderOutfit[3] or HolderOutfit[7] == "shut jacket":
                $ Count += 20

        if Girl.Pierce and Count <= 10:
                $ Count = -5

        $ Count = 20 if Count >= 20 else Count

        $ Tempshame -= Count                  #Set Outfit shame for the upper half
        $ Count = 0

        if HolderOutfit[2] and HolderOutfit[6]: #If wearing both legs and panties
                    $ Count = 30
        elif HolderOutfit[2] in ("blue skirt","skirt","other skirt"):
                    $ Count = 20
        elif HolderOutfit[2] or HolderOutfit[7] == "shut jacket": #any pants
                    $ Count = 25
        elif HolderOutfit[6] == "shorts": #Rogue's shorts as panties
                    $ Count = 25
        elif HolderOutfit[6] in ("bikini bottoms","swimsuit", "cammy leotard", "saiyan leotard", "raven leotard" ,"sports panties","shorts"):
                    $ Count = 15
        elif HolderOutfit[6] == "lace panties":
                    $ Count = 5
        elif HolderOutfit[6]: #any panties
                    $ Count = 10

        if HolderOutfit[9] == "tights":
                    #Factors in tights and hose
                    $ Count = 25 if Count < 25 else Count

        if HolderOutfit[3] == "towel" and Girl not in (EmmaX,StormX):
                    #25 if wearing anything else, 15 if not
                    $ Count = 25 if Count else 15

        $ Tempshame -= Count                  #Set Outfit shame for the lower half

        if "exhibitionist" in Girl.Traits:
                    pass
        elif Tempshame <= 5:
                    pass
        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                    pass
        elif Custom == 10 and Tempshame <= 20:
                    #swimsuit
                    pass
        elif Girl is EmmaX and Tempshame >= 15 and "public" not in Girl.History:
                    $ Agree = 0
        elif Girl is StormX and StormX in Rules:
                    pass
        elif Tempshame <= 25:
                if ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0):
                    pass
                else:
                    $ Agree = 0
        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                    pass
        else:
                    $ Agree = 0

        #End check dialog

        #$ Girl.OutfitShame[Custom] = Tempshame
        if Custom == 3:
#                $ Girl.Custom1 = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                $ Girl.Custom1[0] = 2 if Agree else 1
                call Clothing_Schedule_Check(Girl,3,1)
        elif Custom == 5:
#                $ Girl.Custom2 = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                $ Girl.Custom2[0] = 2 if Agree else 1
                call Clothing_Schedule_Check(Girl,5,1) #checks to make sure it's still SFW
        elif Custom == 6:
#                $ Girl.Custom3 = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                $ Girl.Custom3[0] = 2 if Agree else 1
                call Clothing_Schedule_Check(Girl,6,1)
        elif Custom == 4:
#            if Agree:
#                $ Girl.Gym = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                $ Girl.Gym[0] = 2 if Agree else 1
                call Clothing_Schedule_Check(Girl,4,1)
        elif Custom == 7:
#                $ Girl.Sleepwear = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                $ Girl.Sleepwear[0] = 2 if Agree else 1
        elif Custom == 10:
#            if Agree:
#                $ Girl.Swim = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                $ Girl.Swim[0] = 2 if Agree else 1
        else:
                "Tell Oni Custom Outfit was [Custom]"
                $ RogueX.gibberish = 5
        return

# End Quick Outfit Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Girl Undressing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label AutoStrip(Girl=0):  #rkeljsvgb
        #this is called if they MUST strip to do a sex act, ie sex/anal
        $ Girl = GirlCheck(Girl)
        if (Girl.Panties and not Girl.PantiesDown) or Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6: #If she refuses to take off her pants but agreed to anal
            if Girl is RogueX:
                    ch_r "Ну, мне кажется, [RogueX.Petname], я не должна полностью раздеваться."
            elif Girl is KittyX:
                    ch_k "Мы не должны слишком сильно раздеваться."
            elif Girl is EmmaX:
                    ch_e "Полагаю, нам не стоит сильно раздеваться."
            elif Girl is LauraX:
                    ch_l "Хм. . ."
            elif Girl is JeanX:
                    ch_j "Хм. . ."
            elif Girl is StormX:
                    ch_s "Пожалуй, у нас сейчас не так много вариантов."
            elif Girl is JubesX:
                    ch_v "Я не буду слишком сильно раздеваться. . ."
            elif Girl is GwenX:
                    ch_g "Давай сразу перейдем к делу. . ."
            elif Girl is BetsyX:
                    ch_b "Так, сейчас я устроюсь поудобнее. . ."
            elif Girl is DoreenX:
                    ch_d "Секундочку, сейчас все будет. . ."
            elif Girl is WandaX:
                    ch_w "Мне нужно слегка раздеться."

            if (Girl.Panties and not Girl.PantiesDown) and (Girl.PantsNum() > 6 and not Girl.Upskirt):
                    "Она быстро сбрасывает свои штаны [get_clothing_name(Girl.Panties_key, vin)]."
            elif (Girl.Panties and not Girl.PantiesDown) and (Girl.PantsNum() == 6 and not Girl.Upskirt):
                    "Она быстро сбрасывает свои шорты и [get_clothing_name(Girl.Panties_key, vin)]."
            elif Girl.PantsNum() > 6 and not Girl.Upskirt:
                    "Она стягивает свои штаны, обнажая свою голую киску."
            elif Girl.PantsNum() == 6 and not Girl.Upskirt:
                    "Она стягивает шорты, обнажая свою голую киску."
            elif Girl.HoseNum() >= 6 and (Girl.Panties and not Girl.PantiesDown):
                    "Она стягивает свои [get_clothing_name(Girl.Hose_key, vin)] и [get_clothing_name(Girl.Chest_key, vin)]."
#                    $ Girl.Hose = 0
            elif Girl.HoseNum() >= 6:
                    "Она стягивает свои [get_clothing_name(Girl.Hose_key, vin)] и бросает их на пол."
#                    $ Girl.Hose = 0
            elif (Girl.Panties and not Girl.PantiesDown):
                    "Она сдвигает свои [get_clothing_name(Girl.Panties_key, vin)] в сторону."

        $ Girl.Upskirt = 1 if Girl.PantsNum() >= 5 else Girl.Upskirt
        $ Girl.PantiesDown = 1 if Girl.Panties else Girl.PantiesDown
        $ Girl.Hose = 0 if Girl.HoseNum() >= 6 else Girl.Hose

        $ Girl.SeenPanties = 1
        call Girl_First_Bottomless(Girl)
        return

label Girl_Undress(Girl=0,Region = "ask",CountStore=0): #rkeljsvgb
        #Called mostly from sex act menus when you want a girl to strip down
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        $ CountStore = Tempmod
        if Partner == Girl:
                $ Tempmod = 0
        call Shift_Focus(Girl)

        if Region == "auto":
                if Girl.Upskirt and Girl.PantiesDown:
                    return
                if Girl.PantsNum() > 5 and Tempmod < 20:
                    $ Tempmod = 20
                if Girl.Lust >= 90:
                    $ Tempmod += 10
                elif Girl.Lust >= 80:
                    $ Tempmod += 5
                $ Situation = "auto"
                call Bottoms_Off(Girl,0)

        if Region == "ask":
            menu:
                "Какую часть одежды?"
                "Верх" if Girl.Over or Girl.Chest or Girl.Arms or Girl.Acc or Girl.Hat:
                        $ Region = "top"
                "Низ" if Girl.Legs or Girl.Panties or Girl.Hose or Girl.Acc or Girl.Boots:
                        $ Region = "bottom"
                "И то, и другое. . .":
                        $ Region = "both"
                "Неважно":
                        pass

        if Region == "top":
#            if Girl.Over or Girl.Chest or Girl.Acc or Girl.Hat:
                call Top_Off(Girl,0)
        elif Region == "bottom":
#            if Girl.Legs or Girl.Panties or Girl.Hose or Girl.Acc or Girl.Boots:
                call Bottoms_Off(Girl,0)
        elif Region == "both":
#                if Girl.Over or Girl.Chest or Girl.Acc or Girl.Hat:
                call Top_Off(Girl,0)

                if Partner == Girl:
                        $ Tempmod = 0
                else:
                        $ Tempmod = CountStore

                if "angry" in Girl.RecentActions:
                        pass
#                elif not Girl.Legs and not Girl.Panties and not Girl.Hose and not Girl.Acc and not Girl.Boots:
#                        pass
                elif "no topless" in Girl.RecentActions:
                        if Girl is RogueX:
                                ch_r "Думаю, тебе лучше передумать."
                        elif Girl is KittyX:
                                ch_k "Не дави на меня. . ."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Уверена, что хочешь испытать свою удачу?"
                                else:
                                    ch_e "Уверен, что хочешь испытать свою удачу?"
                        elif Girl is LauraX:
                                if not Player.Male:
                                    ch_l "Ты выбрала неудачный момент, [Girl.Petname]."
                                else:
                                    ch_l "Ты выбрал неудачный момент, [Girl.Petname]."
                        elif Girl is JeanX:
                                ch_j "Ха! Пытаться дальше, [Girl.Petname]."
                        elif Girl is StormX:
                                ch_s "Не думаю, что все пойдет по-твоему. . ."
                        elif Girl is JubesX:
                                ch_v "Нуу, тебе не стоит давить. . ."
                        elif Girl is GwenX:
                                ch_g "Как ты думаешь, что из этого получится?"
                        elif Girl is BetsyX:
                                ch_b "Сомневаюсь, что я буду более сговорчивой. . ."
                        elif Girl is DoreenX:
                                ch_d "Думаю, ты знаешь, каким будет ответ. . ."
                        elif Girl is WandaX:
                                ch_w "Ты ходишь по тонкому льду."
                        menu:
                            extend ""
                            "А теперь нижнюю часть одежды?":
                                call Bottoms_Off(Girl,0)
                            "Ты наверное права, извини.":
                                pass
                else:
                        ch_p "А теперь нижнюю часть одежды?"
                        call Bottoms_Off(Girl,0)

        $ Tempmod = CountStore
        return


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Top_Off(Girl=0,Intro = 1, Line = 0, Cnt = 0): #rkeljsvgb
        # Will she take her top off? Modifiers
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if not Girl.Over and not Girl.Chest and not Girl.Acc and not Girl.Hat and not Girl.Neck:
                # If she's already topless. Just skip back.
                $ Tempmod = 0
                return

        if "angry" in Girl.RecentActions:
                if Girl is RogueX:
                        ch_r "Я сейчас слишком раздражена, чтобы заниматься подобным."
                elif Girl is KittyX:
                        ch_k "Ты не увидишь сисек."
                elif Girl is EmmaX:
                        ch_e "Я не в настроение, [Girl.Petname]."
                elif Girl is LauraX:
                        ch_l "Не торопи события, [Girl.Petname]."
                elif Girl is JeanX:
                        ch_j "Ни за что, [Girl.Petname]."
                elif Girl is StormX:
                        ch_s "Я не хочу доставлять тебе удовольствие."
                elif Girl is JubesX:
                        ch_v "Верх остается на мне. . ."
                elif Girl is GwenX:
                        ch_g "Я не буду снимать верх, спасибо!"
                elif Girl is BetsyX:
                        ch_b "Боюсь, мой верх останется на мне. . ."
                elif Girl is DoreenX:
                        ch_d "Я не буду снимать верх!"
                elif Girl is WandaX:
                        ch_w "Верх остается на мне."
                return

        if Girl.SeenChest and ApprovalCheck(Girl, 500) and not Taboo:
                #You've seen her tits.
                $ Tempmod += 20
        if "exhibitionist" in Girl.Traits:
                $ Tempmod += (4*Taboo)
        if Girl in Player.Harem or "sex friend" in Girl.Petnames and not Taboo:
                $ Tempmod += 10
        elif "ex" in Girl.Traits:
                $ Tempmod -= 40
        if "no topless" in Girl.RecentActions:
                $ Tempmod -= 10
        elif Girl is StormX and (not Taboo or Girl in Rules):
                #Storm is more up for it if in private or with Xavier cleared
                $ Tempmod += 20


        if Intro and not Girl.Uptop:
                if Intro == 2:
                        #It was an addiction scene
                        if Girl is RogueX:
                                ch_r "Я не знаю, тогда тебе придется потрогать их без лишних препятствий. . ."
                        elif Girl is KittyX:
                                ch_k "Так, думаю, тебе нужен[KittyX.like]свободный доступ к ним. . ."
                        elif Girl is EmmaX:
                                ch_e "Тогда мне, похоже, придется раздеться. . ."
                        elif Girl is LauraX:
                                ch_l "Хм, значит мне нужно раздеться по пояс. . ."
                        elif Girl is JeanX:
                                ch_j "Наверное, мне придется раздеться по пояс. . ."
                        elif Girl is StormX:
                                ch_s "Думаю, необходим прямой контакт. . ."
                        elif Girl is JubesX:
                                ch_v "Нууу, для этого мне нужно быть топлесс. . ."
                        elif Girl is GwenX:
                                ch_g "Ну, если для этого мне придется быть топлесс. . ."
                        elif Girl is BetsyX:
                                ch_b "Похоже, для этого мне нужно быть топлесс. . ."
                        elif Girl is DoreenX:
                                ch_d "Тебе, наверное, нужно, чтобы я была топлесс. . ."
                        elif Girl is WandaX:
                                ch_w "Думаю, будет лучше, если я сниму верх. . ."
                else:
                        if Girl.Over:
                                ch_p "Будет проще, если ты снимешь [Girl.Over_display]."
                        elif Girl.Chest:
                                ch_p "Будет проще, если ты снимешь [Girl.Chest_display]."


        $ Approval = ApprovalCheck(Girl, 1100, TabM = 4) # 110, 125, 140, 300 taboo, -20 if already seen

        if Situation == "auto" and not Girl.Uptop:
                $ Line = 0
#                if not Girl.Over and not Girl.Chest and not (Girl in (JubesX,DoreenX) and Girl.Acc) and not Girl.Legs == "dress":
                if Girl.ChestNum() < 1 and Girl.OverNum() < 1:
                        #weeds out girls with nothing on top
                        pass
                elif ApprovalCheck(Girl, 1250, TabM = 1) or (Girl.SeenChest and ApprovalCheck(Girl, 500) and not Taboo):
                        #if she'd go topless
                        $ Girl.Statup("Inbt", 70, 1)
                        $ Girl.Uptop = 1
                        if Girl is WandaX and Girl.Legs == "dress":
                                $ Line = get_clothing_name(Girl.Legs_key, vin)
                        else:
                                $ Line = get_clothing_name(Girl.Over_key, vin) if Girl.Over else get_clothing_name(Girl.Chest_key, vin)
                        "[Girl.Name] разочарованно вздыхает и приподнимает [Line] над своей грудью."
                        if Girl is RogueX:
                                ch_r "Иначе я почти ничего не почувствую."
                        elif Girl is KittyX:
                                ch_k "Иначе я[Girl.like]ничего не почувствую."
                        elif Girl is EmmaX:
                                ch_e "Иногда нужен именно прямой контакт."
                        elif Girl is LauraX:
                                ch_l "Иначе не сработает."
                        elif Girl is JeanX:
                                ch_j "Ладно, попробуй теперь, [Girl.Petname]."
                        elif Girl is StormX:
                                ch_s "Теперь лучше?"
                        elif Girl is JubesX:
                                ch_v "Хорошо, так будет удобнее. . ."
                        elif Girl is GwenX:
                                ch_g "Давай просто, эм. . . уберем все лишнее. . ."
                        elif Girl is BetsyX:
                                ch_b "Я думаю, так всем будет лучше. . ."
                        elif Girl is DoreenX:
                                ch_d "Так -будет- намного лучше. . ."
                        elif Girl is WandaX:
                                ch_w "Так должно быть немного лучше."
                        if Taboo:
                            $ Girl.Statup("Inbt", 90, (int(Taboo/20)))
                        call Girl_First_Topless(Girl,1)
                elif Girl is JubesX and Girl.Over == "dress":
                        pass
                elif Girl.Over and Girl.Chest and ApprovalCheck(Girl, 800, TabM = 1):
                        #if she won't go topless, but has a bra on. . .
                        $ Girl.Statup("Inbt", 40, 1)
                        $ Line = get_clothing_name(Girl.Over_key, vin)
                        $ Girl.Over = 0
                        if Girl is KittyX:
                                $ Line = 0
                                $ Line = Girl.Over_display
                                "[Girl.Name] разочарованно вздыхает, и ее [Line] падает на пол."
                        elif Girl in (JubesX,DoreenX):
                                if Girl.Acc == "vest":
                                        $ Girl.Acc = 0
                                        "[Girl.Name] разочарованно вздыхает и сбрасывает свой жилет, прежде чем снять [Line] через голову."
                                elif Girl.Acc:
                                        $ Girl.Acc = 0
                                        "[Girl.Name] разочарованно вздыхает и сбрасывает свою куртку, прежде чем снять [Line] через голову."
                                else:
                                        "[Girl.Name] разочарованно вздыхает и снимает [Line], а затем отбрасывает в сторону."
                        else:
                                "[Girl.Name] разочарованно вздыхает и снимает [Line] через голову, а затем отбрасывает в сторону."
                        if Girl is RogueX:
                                ch_r "Иначе я почти ничего не почувствую."
                        elif Girl is KittyX:
                                ch_k "Иначе я[Girl.like]ничего не почувствую."
                        elif Girl is EmmaX:
                                ch_e "Иначе я почти ничего не почувствую."
                        elif Girl is LauraX:
                                ch_l "Иначе не сработает."
                        elif Girl is JeanX:
                                ch_j "Ладно, попробуй теперь, [Girl.Petname]."
                        elif Girl is StormX:
                                ch_s "Теперь лучше?"
                        elif Girl is JubesX:
                                ch_v "Ладно, так немного лучше. . ."
                        elif Girl is GwenX:
                                ch_g "Давай, эм. . . без лишней одежды. . ."
                        elif Girl is BetsyX:
                                ch_b "Я думаю, так всем будет лучше. . ."
                        elif Girl is DoreenX:
                                ch_d "Ну, так, наверное, будет лучше. . ."
                        elif Girl is WandaX:
                                ch_w "Этого должно быть достаточно."


                $ Line = 0
                return

        if Approval >= 2:
            #(Girl.Love + Girl.Obed + Girl.Inbt + (2*Tempmod) - (4*Taboo)) >= 1250:
            # Does she assume top off?
            if "no topless" in Girl.DailyActions:
                    if Girl is RogueX:
                            ch_r "Ладно."
                    elif Girl is KittyX:
                            ch_k "Ладно-ладно!"
                    elif Girl is EmmaX:
                            ch_e "-Ладно,- если ты заткнешься."
                    elif Girl is LauraX:
                            ch_l "-Ладно,- но не думай, что я стала мягка к тебе."
                    elif Girl is JeanX:
                            ch_j "Ох, ладно. . ."
                    elif Girl is StormX:
                            ch_s "Ох, если ты настаиваешь. . ."
                    elif Girl is JubesX:
                            ch_v "Нууу, если ты настаиваешь. . ."
                    elif Girl is GwenX:
                            ch_g "Пфф, ладно. . ."
                    elif Girl is BetsyX:
                            ch_b "Если это необходимо. . ."
                    elif Girl is DoreenX:
                            ch_d "Ладно, я сниму верх. . ."
                    elif Girl is WandaX:
                            ch_w "Конечно, можно снять верх."
            $ Girl.FaceChange("sexy", 1)
            if Girl.Forced:
                    $ Girl.FaceChange("sad", 1)
                    $ Girl.Statup("Love", 20, -2, 1)
                    $ Girl.Statup("Love", 70, -3, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 60, 1)
            $ Girl.Statup("Inbt", 50, 3)
            $ Cnt = 1
            while (Girl.Chest or Girl.Over or Girl.Hat or Girl.Acc or Girl.Legs == "dress") and Cnt:
                if Girl is RogueX:
                        ch_r "Ну, [Girl.Petname]. Что мне снять?"
                elif Girl is KittyX:
                        ch_k "Итак[Girl.like]что мне снять?"
                elif Girl is EmmaX:
                        ch_e "Что ты хочешь, чтобы я сняла, [Girl.Petname]?"
                elif Girl is LauraX:
                        ch_l "И что ты хочешь, [Girl.Petname]?"
                elif Girl is JeanX:
                        ch_j "Ох, что ты хочешь, [Girl.Petname]."
                elif Girl is StormX:
                        ch_s "Что я должна снять?"
                elif Girl is JubesX:
                        if not Player.Male:
                            ch_v "Ладно, так, что бы ты хотела с меня снять?"
                        else:
                            ch_v "Ладно, так, что бы ты хотел с меня снять?"
                elif Girl is GwenX:
                        ch_g "Ну, эм. . . что ты хочешь с меня снять? . ."
                elif Girl is BetsyX:
                        ch_b "М? И что ты желаешь снять с меня?"
                elif Girl is DoreenX:
                        ch_d "Что именно мне снять? . ."
                elif Girl is WandaX:
                        ch_w "Ну, что именно мне снять?"
                menu:
                    #Menu All off?
                    extend ""
                    "Почему бы тебе не снять [get_clothing_name(Girl.Acc_key, vin)]?" if Girl in (JubesX,DoreenX,WandaX) and Girl.Acc:
                            $ Line = get_clothing_name(Girl.Acc_key, vin)
                            $ Girl.Acc = 0
                            "[Girl.Name] сбрасывает [Line]."

                    "Сними [get_clothing_name(Girl.Over_key, vin)]." if Girl.Over:
                            $ Girl.FaceChange("bemused", 1)
                            if Girl.Over == "dress" and Girl.Legs == "dress":
                                    menu:
                                        "Все платье?"
                                        "Да [[верхнюю и нижнюю части]":
                                                $ Girl.Legs = 0
                                        "Только верх.":
                                                pass
                            if Girl is KittyX:
                                    $ Line = Girl.Over_display
                                    $ Girl.Over = 0
                                    "[Girl.Name] пожимает плечами и [Line] падает на пол."
                            else:
                                    $ Line = get_clothing_name(Girl.Over_key, vin)
                                    $ Girl.Over = 0
                                    "[Girl.Name] снимает [Line] и отбрасывает в сторону."
                            if Girl is JubesX:
                                    call Girl_First_Bottomless(Girl)
                    "Сними платье. . ." if Girl.Legs == "dress" and Girl.Over != "dress":
                            $ Girl.FaceChange("sexy")
                            call AnyLine(Girl,"Полностью или только верх?")
                            menu:
                                extend ""
                                "Полностью.":
                                        $ Girl.Legs = 0
                                        "Она стаскивает с себя платье."

                                "Только верх.":
                                        $ Girl.Uptop = 1
                                        "Она стягивает верх платья вниз."

                    "Сними только [get_clothing_name(Girl.Chest, vin)]." if Girl.Over and Girl.Chest:
                            $ Girl.FaceChange("bemused", 1)
                            if Girl.Chest == "swimsuit" or Girl.Chest == "saiyan leotard" or Girl.Chest == "cammy leotard" or Girl.Chest == "raven leotard":
                                #if this is Betsy, she has the swimsuit on,
                                if Girl.PantiesDown or ApprovalCheck(Girl, 1200, TabM = 5):
                                        #if it's already mostly open
                                        $ Girl.Panties = 0
                                        $ Girl.Chest = 0
                                        "[Girl.Name] медленно достает [get_clothing_name(Girl.Chest, vin)] из под [get_clothing_name(Girl.Over, rod)]."
                                else:
                                        $ Girl.Chest = 0
                                        "Она смотрит на вас и сдвигает верхнюю часть купальника в сторону."
                            else:
                                $ Line = get_clothing_name(Girl.Chest, vin)
                                $ Girl.Chest = 0
                                if Girl is KittyX:
                                        "[Girl.Name] достает [Line] и бросает на пол."
                                else:
                                        "[Girl.Name] медленно достает [Line] из под [get_clothing_name(Girl.Over, rod)]."

                    "Сними [get_clothing_name(Girl.Chest, vin)]." if not Girl.Over and Girl.Chest:
                            $ Girl.FaceChange("bemused", 1)
                            if Girl.Chest == "swimsuit" or Girl.Chest == "saiyan leotard" or Girl.Chest == "cammy leotard" or Girl.Chest == "raven leotard":
                                #if this is Betsy, she has the swimsuit on,
                                if Girl.PantiesDown or ApprovalCheck(Girl, 1200, TabM = 5):
                                        #if it's already mostly open
                                        $ Girl.Panties = 0
                                        "[Girl.Name] медленно снимает [get_clothing_name(Girl.Chest, vin)]."
                                        $ Girl.Chest = 0
                                else:
                                        $ Girl.Chest = 0
                                        "Она смотрит на вас и сдвигает верхнюю часть купальника в сторону."
                            else:
                                if Girl is KittyX:
                                        $ Line = Girl.Chest_display
                                        $ Girl.Chest = 0
                                        "[Girl.Name] пожимает плечами, а затем [Line] падает на пол."
                                else:
                                        $ Line = get_clothing_name(Girl.Chest, vin)
                                        $ Girl.Chest = 0
                                        "[Girl.Name] снимает [Line]."
                    "Просто оголи грудь." if (Girl.Over or Girl.Chest) and not Girl.Uptop:
                            $ Girl.FaceChange("bemused", 1)
                            $ Girl.Uptop = 1
                            if Girl is EmmaX:
                                    "[Girl.Name] улыбается и оголяет свои сиськи. . ."
                            elif Girl.Over and Girl.Chest:
                                    "[Girl.Name] улыбается и задирает свою верхнюю часть одежды. . ."
                            else:
                                    "[Girl.Name] улыбается и приподнимает верхнюю часть одежды. . ."
                    "Разденься по пояс." if (Girl.Over or Girl.Acc) and (Girl.Chest or Girl.Acc):
                            $ Girl.FaceChange("bemused", 1)
                            if Girl is KittyX:
                                    $ Girl.Over = 0
                                    $ Girl.Chest = 0
                                    "[Girl.Name] пожимает плечами и вся ее верхняя часть одежды падает через ее тело на землю."
                            else:
                                    $ Line = 0
                                    if Girl in (DoreenX,WandaX) and Girl.Acc:
                                            $ Line = get_clothing_name(Girl.Acc, vin)
                                            $ Girl.Acc = 0
                                            "[Girl.Name] снимает [Line]. . ."
                                    elif Girl is JubesX and Girl.Acc:
                                            $ Girl.Acc = 0
                                            "[Girl.Name] снимает куртку. . ."
                                            call Girl_First_Bottomless(Girl)
                                    if Girl.Over:
                                        $ Line = get_clothing_name(Girl.Over, vin)
                                        $ Girl.Over = 0
                                        "[Girl.Name] снимает [Line] через голову. . ."
                                    if Girl.Chest == "swimsuit" or Girl.Chest == "saiyan leotard" or Girl.Chest == "cammy leotard" or Girl.Chest == "raven leotard":
                                        #if this is Betsy, she has the swimsuit on,
                                        if Girl.PantiesDown or ApprovalCheck(Girl, 1200, TabM = 5):
                                                #if it's already mostly open
                                                $ Girl.Panties = 0
                                                $ Girl.Chest = 0
                                                ". . .а потом и [get_clothing_name(Girl.Chest, vin)]."
                                        else:
                                                $ Girl.Uptop = 1
                                                ". . .а потом сдвигает [get_clothing_name(Girl.Chest, vin)] в сторону."
                                    elif Girl.Chest and Line:
                                                $ Line = get_clothing_name(Girl.Chest, vin)
                                                $ Girl.Chest = 0
                                                ". . .а потом и [Line] as well."
                                    elif Girl.Chest:
                                                $ Line = get_clothing_name(Girl.Chest, vin)
                                                $ Girl.Chest = 0
                                                "[Girl.Name] стаскивает с себя [Line]. . ."
                    "Сними [get_clothing_name(Girl.Arms, vin)]. . ." if Girl.Arms:
                            $ Girl.FaceChange("sexy")
                            $ Line = get_clothing_name(Girl.Arms, vin)
                            $ Girl.Arms = 0
                            "Она снимает [Line]."

                    "Почему бы тебе не снять подтяжки?" if Girl.Acc == "suspenders" or Girl.Acc == "suspenders2":
                            $ Girl.Acc = 0
                            "[Girl.Name] снимает подтяжки."

                    "Почему бы тебе не снять обручи?" if Girl.Acc == "rings" or Girl.Acc == "rings":
                            $ Girl.Acc = 0
                            "[Girl.Name] снимает обручи."

                    "Почему бы тебе не снять [get_clothing_name(Girl.Hat, vin)]?" if Girl.Hat:
                            $ Line = get_clothing_name(Girl.Hat, vin)
                            $ Girl.Hat = 0
                            "[Girl.Name] отбрасывает [Line] в сторону."
                    "Почему бы тебе не снять [get_clothing_name(Girl.Neck, vin)]?" if Girl.Neck:
                            $ Line = get_clothing_name(Girl.Neck, vin)
                            $ Girl.Neck = 0
                            "[Girl.Name] снимает [Line]."

                    "Достаточно. [[двигаться дальше]":
                            $ Girl.FaceChange("bemused", 1)
                            call AnyLine(Girl,"Ладно, "+Girl.Petname+".")
                            $ Cnt = 0
            if Girl.ChestNum() < 3 and Girl.OverNum() < 3:
                    #if her top's are off. . .
                    $ Girl.Statup("Obed", 50, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    call Girl_First_Topless(Girl)
            $ Line = 0
            $ Girl.Statup("Lust", 80, 3)
            $ Girl.RecentActions.append("ask topless")
            $ Girl.DailyActions.append("ask topless")
            $ Tempmod = 0
            return

        #Else, Doesn't automatically want to lose the top//////////////////////////////////

        $ Girl.FaceChange("bemused", 1)
        if Girl is RogueX:
                if Intro == "massage" and not Approval:
                    ch_r "Я согласна на массаж, но снимать я ничего не буду."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_r "[Girl.Petname], я только что сказала тебе нет."
                elif Approval and not Girl.SeenChest:
                    ch_r "Но я бы хотела оставить что-нибудь для воображения. . ."
                elif not Girl.SeenChest:
                    ch_r "Я пока не готова показать тебе их. . ."
                elif "no topless" in Girl.DailyActions:
                    ch_r "Раньше мне это не нравилось, [Girl.Petname], думаешь, что-то изменилось?"
                elif "ask topless" in Girl.RecentActions:
                    if not Player.Male:
                        ch_r "Передумала, [Girl.Petname]?"
                    else:
                        ch_r "Передумал, [Girl.Petname]?"
                elif Taboo:
                    ch_r "Здесь могут ходить люди. . ."
                elif Approval:
                    if not Player.Male:
                        ch_r "Ну, ты их уже видела, но. . ."
                    else:
                        ch_r "Ну, ты их уже видел, но. . ."
                else:
                    ch_r "Не сейчас."
        elif Girl is KittyX:
                if Intro == "massage" and not Approval:
                    ch_k "Массаж - это хорошо, но я не буду ничего снимать, хорошо?"
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_k "Я[Girl.like]уже сказала тебе, ни за что!"
                elif Approval and not Girl.SeenChest:
                    ch_k "Мне[Girl.like]это не особо нравится."
                elif not Girl.SeenChest:
                    ch_k "I'd[Girl.like]really rather not, ok?"
                elif "no topless" in Girl.DailyActions:
                    ch_k "Я[Girl.like]предпочла бы этого не делать, ладно?"
                elif "ask topless" in Girl.RecentActions:
                    ch_k "Что-то[Girl.like]еще хочешь?"
                elif Taboo:
                    ch_k "Мне[Girl.like]не комфортно здесь. . ."
                elif Approval:
                    ch_k "Может не надо?"
                else:
                    ch_k "Не-а."
        elif Girl is EmmaX:
                if Intro == "massage" and not Approval:
                    ch_e "Я люблю массаж, но раздеваться я не буду."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_e "Учись на предыдущих ошибках, [Girl.Petname]."
                elif Approval and not Girl.SeenChest:
                    ch_e "Я не знаю, будет ли это уместно."
                elif not Girl.SeenChest:
                    if not Player.Male:
                        ch_e "Не думаю, что ты к этому готова."
                    else:
                        ch_e "Не думаю, что ты к этому готов."
                elif "no topless" in Girl.DailyActions:
                    if not Player.Male:
                        ch_e "Ты все еще так этим одержима?"
                    else:
                        ch_e "Ты все еще так этим одержим?"
                elif "ask topless" in Girl.RecentActions:
                    ch_e "Ты хочешь большего?"
                elif Taboo:
                    ch_e "[Girl.Petname], не когда вокруг столько любопытных глаз."
                elif Approval:
                    if not Player.Male:
                        ch_e "Ты уверена, что готова?"
                    else:
                        ch_e "Ты уверен, что готов?"
                else:
                    ch_e "Нет."
        elif Girl is LauraX:
                if Intro == "massage" and not Approval:
                    ch_l "Мне бы не помешал массаж, но я не буду раздеваться."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_l "Не дави на меня, [Girl.Petname]"
                elif Approval and not Girl.SeenChest:
                    ch_l "Блин, я не готова."
                elif not Girl.SeenChest:
                    ch_l "Я так не думаю."
                elif "no topless" in Girl.DailyActions:
                    ch_l "Успокойся уже."
                elif "ask topless" in Girl.RecentActions:
                    ch_l "Опять?"
                elif Taboo:
                    ch_l "[Girl.Petname], только не здесь, хорошо?"
                elif Approval:
                    if not Player.Male:
                        ch_l "Ты уверена?"
                    else:
                        ch_l "Ты уверен?"
                else:
                    ch_l "Нет."
        elif Girl is JeanX:
                if Intro == "massage" and not Approval:
                    ch_j "Массаж - да, раздеваться - нет."
                elif "no topless" in Girl.RecentActions:
                    $ JeanX.FaceChange("angry")
                    ch_j "Расслабься уже, [Girl.Petname]."
                #elif Approval and not Girl.SeenChest:
                    #ch_j "Hmm. . ."
                #elif not Girl.SeenChest:
                    #ch_j "Hm. . ."
                elif "no topless" in Girl.DailyActions:
                    ch_j "Этого не произойдет."
                elif "ask topless" in Girl.RecentActions:
                    ch_j "Снова?"
                elif Taboo:
                    ch_j "Хм. . . не здесь."
                elif Approval:
                    ch_j "Хмм. . ."
                else:
                    ch_j "Ни за что."
        elif Girl is StormX:
                if Intro == "massage" and not Approval:
                    ch_s "Я с удовольствием приму массаж, но я останусь полностью одетой."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_s "Я не настолько сговорчивая, [Girl.Petname]."
                elif Approval and not Girl.SeenChest:
                    ch_s "Я не знаю, будет ли это уместно."
                elif "no topless" in Girl.DailyActions:
                    ch_s "Больше не спрашивай ."
                elif "ask topless" in Girl.RecentActions:
                    if not Player.Male:
                        ch_s "Ох, ты бы хотела увидеть их снова?"
                    else:
                        ch_s "Ох, ты бы хотел увидеть их снова?"
                elif Taboo and Girl not in Rules:
                    ch_s "Боюсь, на людях я не могу, [Girl.Petname]."
                elif Approval:
                    if not Player.Male:
                        ch_s "Ты уверена?"
                    else:
                        ch_s "Ты уверен?"
                else:
                    ch_s "Нет."
        elif Girl is JubesX:
                if Intro == "massage" and not Approval:
                    ch_v "Мне бы не помешал массаж, но я не буду раздеваться."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_v "Не дави на меня, [Girl.Petname]"
                elif Approval and not Girl.SeenChest:
                    ch_v "Блин, я не готова."
                elif not Girl.SeenChest:
                    ch_v "Мне это не нравится."
                elif "no topless" in Girl.DailyActions:
                    ch_v "Успокойся уже."
                elif "ask topless" in Girl.RecentActions:
                    ch_v "Опять?"
                elif Taboo:
                    ch_v "[Girl.Petname], здесь слишком людно."
                elif Approval:
                    ch_v "Не знаю, правда?"
                else:
                    ch_v "Нет."
        elif Girl is GwenX:
                if Intro == "massage" and not Approval:
                    ch_g "Я заинтересована в массаже, но одежда останется на мне."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_g "Прекрати, [Girl.Petname]."
                elif Approval and not Girl.SeenChest:
                    ch_g "Эммм. . ."
                elif not Girl.SeenChest:
                    ch_g "Я бы хотела, чтобы они были прикрыты."
                elif "no topless" in Girl.DailyActions:
                    ch_g "Хватит спрашивать."
                elif "ask topless" in Girl.RecentActions:
                    ch_g "Снова?"
                elif Taboo:
                    ch_g "[Girl.Petname], здесь не место для этого."
                elif Approval:
                    ch_g "Эммм. . ."
                else:
                    ch_g "Я так не думаю."
        elif Girl is BetsyX:
                if Intro == "massage" and not Approval:
                    ch_b "Массаж - это восхитительно, но я должна оставаться одетой."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_b "Меня не так-то легко убедить, [Girl.Petname]."
                elif Approval and not Girl.SeenChest:
                    ch_b "Я не думаю, что это было бы уместно."
                elif "no topless" in Girl.DailyActions:
                    ch_b "Ох, прекрати."
                elif "ask topless" in Girl.RecentActions:
                    ch_b "Тебе интересно увидеть их снова?"
                elif Taboo and Girl not in Rules:
                    ch_b "Это вызовет переполох, [Girl.Petname]."
                elif Approval:
                    ch_b "Раз так. . ."
                else:
                    ch_b "Это невозможно."
        elif Girl is DoreenX:
                if Intro == "massage" and not Approval:
                    ch_d "Я не против массажа, но я не уверена, что хочу раздеваться."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_d "[Girl.Petname], перестань спрашивать."
                elif Approval and not Girl.SeenChest:
                    ch_d "Эммм. . ."
                elif not Girl.SeenChest:
                    ch_d "Я бы хотела, чтобы они были прикрыты."
                elif "no topless" in Girl.DailyActions:
                    ch_d "Перестань спрашивать."
                elif "ask topless" in Girl.RecentActions:
                    ch_d "Снова?"
                elif Taboo:
                    ch_d "[Girl.Petname]! Здесь не место для этого."
                elif Approval:
                    ch_d "Эммм. . ."
                else:
                    ch_d "Ни за что."
        elif Girl is WandaX:
                if Intro == "massage" and not Approval:
                    ch_w "Ну, я не против массажа, но раздеваться я не хочу."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_w "Перестань спрашивать, [Girl.Petname]."
                elif Approval and not Girl.SeenChest:
                    ch_w "Я не уверена. . ."
                elif not Girl.SeenChest:
                    ch_w "Мне бы не хотелось оголяться."
                elif "no topless" in Girl.DailyActions:
                    ch_w "Перестань спрашивать."
                elif "ask topless" in Girl.RecentActions:
                    ch_w "Да?"
                elif Taboo:
                    ch_w "Только не здесь. . ."
                elif Approval:
                    ch_w "Я не уверена. . ."
                else:
                    ch_w "Хех, нет."
        menu:
            extend ""
            "Извини - извини." if "no topless" in Girl.RecentActions:
                $ Girl.FaceChange("bemused", 1)
                if Girl is RogueX:
                        ch_r "Ладно, только. . . успокойся, хорошо?"
                elif Girl is KittyX:
                        ch_k "Все нормально, я все понимаю, но[Girl.like]успокойся, ладно?"
                elif Girl is EmmaX:
                        ch_e "Я не могу винить тебя за твою настойчивость, но учись на своих ошибках."
                elif Girl is LauraX:
                        ch_l "Хорошо, я поняла."
                elif Girl is JeanX:
                        ch_j "Я не могу винить тебя за это, [Girl.Petname]."
                elif Girl is StormX:
                        ch_s "Я не могу винить тебя."
                elif Girl is JubesX:
                        ch_v "Нуу, кто не рискует, тот не выигрывает, да?"
                elif Girl is GwenX:
                        if not Player.Male:
                            ch_g "Послушай, ты должна была спросить. Я понимаю."
                        else:
                            ch_g "Послушай, ты должен был спросить. Я понимаю."
                elif Girl is BetsyX:
                        ch_b "Конечно, но веди себя прилично. . ."
                elif Girl is DoreenX:
                        ch_d "Все нормально. . ."
                elif Girl is WandaX:
                        ch_w "Без проблем."

            "Ладно, все хорошо." if "no topless" not in Girl.RecentActions:
                if "ask topless" not in Girl.DailyActions:
                        $ Girl.Statup("Lust", 80, 3)
                        $ Girl.Statup("Love", 70, 1)
                        $ Girl.Statup("Love", 90, 1)
                        $ Girl.Statup("Inbt", 50, 3)
                if Girl.Forced:
                        $ Girl.Mouth = "grimace"
                        if Girl is RogueX:
                                ch_r "Благодарю."
                        elif Girl is KittyX:
                                ch_k "Очень[Girl.like]здорово с твоей стороны сказать это."
                        elif Girl is EmmaX:
                                ch_e "Как. . . великодушно с твоей стороны."
                        elif Girl is LauraX:
                                ch_l "Ладно."
                        elif Girl is JeanX:
                                ch_j ". . ."
                        elif Girl is StormX:
                                ch_s "Хорошо."
                        elif Girl is JubesX:
                                ch_v "Ага, спасибо. . ."
                        elif Girl is GwenX:
                                ch_g "Ага. . . славно. . ."
                        elif Girl is BetsyX:
                                ch_b "Конечно, спасибо благоразумие. . ."
                        elif Girl is DoreenX:
                                ch_d "Спасибо, что уважаешь мои границы. . ."
                        elif Girl is WandaX:
                                ch_w "Ага, спасибо. . ."
                        if "ask topless" not in Girl.DailyActions:
                            $ Girl.Statup("Love", 20, 2)
                            $ Girl.Statup("Love", 70, 2)
                            $ Girl.Statup("Inbt", 60, 1)

            "Как насчет снять только [get_clothing_name(Girl.Acc_key, vin)]?" if Girl in (JubesX,DoreenX,WandaX) and Girl.Acc:
                # asked to remove jacket
                if Girl in (DoreenX,WandaX):
                        call AnyLine(Girl,"Конечно. . .")
                        $ Line = get_clothing_name(Girl.Acc_key, vin)
                        $ Girl.Acc = 0
                        "[Girl.Name] сбрасывает с себя [Line]."
                #the rest of this isn't needed for Doreen since her jacket doesn't cover anything anyway
                elif Girl.Over or Girl.Acc == "open jacket":
                        #if wearing a shirt
                        ch_v "Конечно. . ."
                        $ Girl.Acc = 0
                        "[Girl.Name] сбрасывает с себя куртку."
                elif ApprovalCheck(Girl, 800, TabM = 2) and Girl.Chest: #80, 160 taboo
                        $ Girl.FaceChange("sexy")
                        ch_v "Ну, думаю, можно. . ."
                        $ Girl.FaceChange("bemused", 1)
                        $ Girl.Acc = 0
                        "[Girl.Name] сбрасывает с себя куртку."
                        $ Girl.Statup("Obed", 50, 1)
                        $ Girl.Statup("Inbt", 30, 2)
                elif not Girl.Chest:
                        $ Girl.Eyes = "surprised"
                        $ Girl.Blush = 2
                        ch_v "На мне нет лифчика. . ."
                        $ Girl.Statup("Inbt", 30, 1)
                        menu:
                            extend ""
                            "Хорошо, тогда можешь не снимать.":
                                    $ Girl.Mouth = "smile"
                                    $ Girl.Statup("Love", 70, 2)
                                    ch_v "Фух, спасибо. . ."

                            "Меня это нисколько не волнует.":
                                if ApprovalCheck(Girl, 500, "I", TabM=3) or ApprovalCheck(Girl, 1000, "LI", TabM=3):
                                    $ Girl.FaceChange("bemused", 1)
                                    ch_v "Ого, интересно. . ."
                                    $ Girl.Statup("Obed", 20, 2)
                                    $ Girl.Statup("Obed", 60, 1)
                                    $ Girl.FaceChange("sexy")
                                    $ Girl.Acc = 0
                                    "[Girl.Name] сбрасывает с себя куртку."
                                    $ Girl.Over = 0
                                    $ Girl.Statup("Inbt", 30, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                                    call Girl_First_Topless(Girl)
                                else:
                                    $ Girl.FaceChange("bemused")
                                    call Top_Off_Refused(Girl)

                            "Я знаю, снимай.":
                                    call ToplessorNothing(Girl)
                        $ Girl.Blush = 1
                else:
                        $ Girl.FaceChange("sexy")
                        call Top_Off_Refused(Girl)
            #end "just the jacket?"
            "Как насчет снять только [get_clothing_name(Girl.Over_key, vin)]?" if Girl.Over:
                # asked to go shirtless.
                if Girl == StormX and Girl.Over == "towel":
                        $ Girl.FaceChange("bemused")
                        $ Girl.Over = 0
                        "Она снимает с себя полотенце."
                elif ApprovalCheck(Girl, 800, TabM = 2) and Girl.Chest: #80, 160 taboo
                        $ Girl.FaceChange("sexy")
                        if Girl is RogueX:
                                ch_r "Ну, думаю, в этом нет ничего страшного. . ."
                        elif Girl is KittyX:
                                ch_k "Эм, думаю, можно. . ."
                        elif Girl is EmmaX:
                                ch_e "Хорошо, ничего плохого от этого не случится. . ."
                        elif Girl is LauraX:
                                ch_l "Думаю. . . можно. . ."
                        elif Girl is JeanX:
                                ch_j "Конечно, как скажешь."
                        elif Girl is StormX:
                                ch_s "Пожалуй, можно."
                        elif Girl is JubesX:
                                ch_v "Нууу, пожалуй, можно. . ."
                        elif Girl is GwenX:
                                ch_g "Ну. . . наверное, можно."
                        elif Girl is BetsyX:
                                ch_b "Ох, пожалуй, можно. . ."
                        elif Girl is DoreenX:
                                ch_d "Наверное, все будет нормально. . ."
                        elif Girl is WandaX:
                                ch_w "Конечно. . ."
                        $ Girl.FaceChange("bemused", 1)
                        $ Line = get_clothing_name(Girl.Over_key, vin)
                        if Girl is KittyX:
                                        $ Line = 0
                                        $ Line = Girl.Over_display
                                        $ Girl.Over = 0
                                        "[Girl.Name] пожимает плечами и [Line] падает на пол."
                        elif Girl is DoreenX:
                                $ Girl.Over = 0
                                if Girl.Acc == "vest":
                                        $ Girl.Acc = 0
                                        "[Girl.Name] сбрасывает свой жилет, прежде чем снять [Line] через голову."
                                elif Girl.Acc:
                                        $ Girl.Acc = 0
                                        "[Girl.Name] сбрасывает свою куртку, прежде чем снять [Line] через голову."
                                else:
                                        "[Girl.Name] снимает [Line] через голову, а затем отбрасывает в сторону."
                        elif Girl is JubesX:
                                $ Girl.Over = 0
                                if Girl.Acc:
                                        $ Girl.Acc = 0
                                        "[Girl.Name] сбрасывает свою куртку, прежде чем снять [Line] через голову."
                                else:
                                        "[Girl.Name] снимает [Line], а затем отбрасывает в сторону."
                                call Girl_First_Bottomless(Girl)
                        else:
                                $ Girl.Over = 0
                                "[Girl.Name] снимает [Line] через голову."
                        $ Girl.Statup("Obed", 50, 1)
                        $ Girl.Statup("Inbt", 30, 2)
                elif not Girl.Chest:
                        $ Girl.Eyes = "surprised"
                        $ Girl.Blush = 2
                        if Girl is RogueX:
                                ch_r "Знаешь, я буду выглядеть неприлично."
                        elif Girl is KittyX:
                                ch_k "Я[Girl.like]бы -совсем- не хотела, чтобы меня увидели полуголой."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Не уверена, что ты готова это увидеть."
                                else:
                                    ch_e "Не уверена, что ты готов это увидеть."
                        elif Girl is LauraX:
                                ch_l "Если честно, у меня под этим ничего нет."
                        elif Girl is JeanX:
                                ch_j "Сейчас на мне нет лифчика."
                        elif Girl is StormX:
                                ch_s "Понимаешь, у меня под этим ничего не надето. . ."
                        elif Girl is JubesX:
                                ch_v "У меня, как бы, ничего под этим нет. . ."
                        elif Girl is GwenX:
                                ch_g "Я, эм. . . у меня под этим ничего нет."
                        elif Girl is BetsyX:
                                ch_b "Боюсь, под этим у меня ничего нет. . ."
                        elif Girl is DoreenX:
                                ch_d "Я, эм, ничего не надела под это. . ."
                        elif Girl is WandaX:
                                ch_w "У меня под этим ничего нет. . ."
                        $ Girl.Statup("Inbt", 30, 1)
                        menu:
                            extend ""
                            "Хорошо, тогда не снимай.":
                                    $ Girl.Mouth = "smile"
                                    $ Girl.Statup("Love", 70, 2)
                                    if Girl is RogueX:
                                            ch_r "Отлично!"
                                    elif Girl is KittyX:
                                            ch_k "Спасибо!"
                                    elif Girl is EmmaX:
                                            ch_e "Хорошо."
                                    elif Girl is LauraX:
                                            ch_l "Ладно."
                                    elif Girl is JeanX:
                                            ch_j "Я так и сказала."
                                    elif Girl is StormX:
                                            ch_s "Хорошо."
                                    elif Girl is JubesX:
                                            ch_v "Фух, спасибо. . ."
                                    elif Girl is GwenX:
                                            ch_g "Фух, спасибо."
                                    elif Girl is BetsyX:
                                            ch_b "Разумеется."
                                    elif Girl is DoreenX:
                                            ch_d "Спасибо. . ."
                                    elif Girl is WandaX:
                                            ch_w "Спасибо. . ."

                            "Меня это нисколько не волнует.":
                                if ApprovalCheck(Girl, 500, "I", TabM=3) or ApprovalCheck(Girl, 1000, "LI", TabM=3):
                                    $ Girl.FaceChange("bemused", 1)
                                    if Girl is RogueX:
                                            ch_r "Ох, по крайней мере, ты знаешь, чего хочешь."
                                    elif Girl is KittyX:
                                            ch_k "И почему я не удивлена?"
                                    elif Girl is EmmaX:
                                            ch_e "Ну, я полагаю, попробовать не помешает."
                                    elif Girl is LauraX:
                                            ch_l "Хмм. . . ладно. . ."
                                    elif Girl is JeanX:
                                            ch_j ". . ."
                                    elif Girl is StormX:
                                            ch_s "Меня это тоже не сильно беспокоит."
                                    elif Girl is JubesX:
                                            ch_v "Ого, интересно. . ."
                                    elif Girl is GwenX:
                                            ch_g "Ладно."
                                    elif Girl is BetsyX:
                                            ch_b "Ох, понятно. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ну, думаю, ничего плохого от этого не случится. . ."
                                    elif Girl is WandaX:
                                            ch_w "Ну ладно, пожалуй, я не против. . ."
                                    $ Girl.Statup("Obed", 20, 2)
                                    $ Girl.Statup("Obed", 60, 1)
                                    $ Girl.FaceChange("sexy")
                                    $ Line = get_clothing_name(Girl.Over_key, vin)
                                    if Girl is KittyX:
                                            $ Line = 0
                                            $ Line = Girl.Over_display
                                            $ Girl.Over = 0
                                            "[Girl.Name] пожимает плечами и [Line] падает на пол."
                                    elif Girl in (JubesX,DoreenX,WandaX):
                                            $ Girl.Over = 0
                                            if Girl.Acc == "vest":
                                                    $ Girl.Acc = 0
                                                    "[Girl.Name] сбрасывает свой жилет, прежде чем снять [Line] через голову."
                                            elif Girl.Acc:
                                                    $ Girl.Acc = 0
                                                    "[Girl.Name] сбрасывает свою куртку, прежде чем снять [Line] через голову."
                                            else:
                                                    "[Girl.Name] снимает [Line] через голову, а затем отбрасывает в сторону."
                                            if Girl is JubesX:
                                                    call Girl_First_Bottomless(Girl)
                                    else:
                                            $ Girl.Over = 0
                                            "[Girl.Name] снимает [Line] через голову."
                                    $ Girl.Over = 0
                                    $ Girl.Statup("Inbt", 30, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                                    call Girl_First_Topless(Girl)
                                else:
                                    $ Girl.FaceChange("bemused")
                                    call Top_Off_Refused(Girl)

                            "Я знаю, снимай.":
                                    call ToplessorNothing(Girl)
                        $ Girl.Blush = 1
                else:
                        $ Girl.FaceChange("sexy")
                        call Top_Off_Refused(Girl)
            #end "just the over?"

            "Ну пожалуйста? [[оголить грудь]":
                # asked to go topless. 110, 270 Taboo
                if Approval and ApprovalCheck(Girl, 600, "L", TabM=1):
                        $ Girl.Statup("Obed", 40, 2)
                        $ Girl.FaceChange("sexy")
                        if Girl is RogueX:
                                if "no topless" in Girl.RecentActions:
                                    if not Player.Male:
                                        ch_r "Ты очень настойчивая, [Girl.Petname]. Думаю, в этот раз твоя настойчивость будет вознаграждена. . ."
                                    else:
                                        ch_r "Ты очень настойчивый, [Girl.Petname]. Думаю, в этот раз твоя настойчивость будет вознаграждена. . ."
                                else:
                                    ch_r "Хех, думаю, я не могу отказать тебе, когда ты вежливо просишь . . ."
                        elif Girl is KittyX:
                                if "no topless" in Girl.RecentActions:
                                    ch_k "Ты не знаешь, когда остановиться. . . но в этот раз тебе повезло. . ."
                                else:
                                    ch_k "Вот[Girl.like]умеешь ты вежливо просить . . ."
                        elif Girl is EmmaX:
                                if "no topless" in Girl.RecentActions:
                                    ch_e "Ладно, я устала терпеть твои постоянные просьбы."
                                else:
                                    ch_e "Ну, полагаю, раз ты вежливо просишь . . ."
                        elif Girl is LauraX:
                                    if not Player.Male:
                                        ch_l "Ладно, озобоченная извращенка."
                                    else:
                                        ch_l "Ладно, озобоченный извращенец."
                        elif Girl is JeanX:
                                if "no topless" in Girl.RecentActions:
                                    ch_j "Ох, как скажешь."
                                else:
                                    ch_j "Думаю, можно. . ."
                        elif Girl is StormX:
                                ch_s "Ох, хорошо."
                        elif Girl is JubesX:
                                ch_v "Ладно, ладно, боже."
                        elif Girl is GwenX:
                                ch_g ". . . Ладно."
                        elif Girl is BetsyX:
                                ch_b "Ох, если это нужно. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох, хорошо. . ."
                        elif Girl is WandaX:
                                ch_w "Конечно. . ."
                        menu:
                            "Снять одежду полностью":
                                    $ Line = 0
                                    if Girl.Acc:
                                                $ Line = get_clothing_name(Girl.Acc_key, vin)
                                                $ Girl.Acc = 0
                                                "[Girl.Name] скидывает [Line]."
                                    if Girl.Over:
                                            if Line:
                                                $ Line = get_clothing_name(Girl.Over_key, vin)
                                                $ Girl.Over = 0
                                                "Затем она снимает [Line]."
                                            else:
                                                $ Line = get_clothing_name(Girl.Over_key, vin)
                                                $ Girl.Over = 0
                                                "[Girl.Name] снимает [Line]."
                                    if Girl.Chest:
                                            if Line:
                                                $ Line = get_clothing_name(Girl.Chest_key, vin)
                                                $ Girl.Chest = 0
                                                "И, наконец, она снимает [Line]."
                                            else:
                                                $ Line = get_clothing_name(Girl.Chest_key, vin)
                                                $ Girl.Chest = 0
                                                "[Girl.Name] она снимает [Line]."
                            "Просто оголить грудь":
                                    $ Girl.Uptop = 1
                                    "[Girl.Name] обнажает свою грудь."
                        $ Girl.Arms = 0
                        $ Girl.Statup("Inbt", 30, 2)
                        $ Girl.Statup("Inbt", 60, 1)
                        call Girl_First_Topless(Girl)
                elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        if Girl is RogueX:
                                ch_r "Не-а, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k "Неееет!"
                        elif Girl is EmmaX:
                                ch_e "И снова нет."
                        elif Girl is LauraX:
                                ch_l "Все еще нет."
                        elif Girl is JeanX:
                                ch_j "И все еще \"нет\", [Girl.Petname]."
                        elif Girl is StormX:
                                ch_s "Нет, не сегодня."
                        elif Girl is JubesX:
                                ch_v "Нее. . ."
                        elif Girl is GwenX:
                                ch_g "Дай мне передохнуть."
                        elif Girl is BetsyX:
                                ch_b "Пожалуйста, держи себя в руках. . ."
                        elif Girl is DoreenX:
                                ch_d "Ты меня не переубедишь. . ."
                        elif Girl is WandaX:
                                ch_w "Хватит меня доставать."
                        $ Girl.Statup("Love", 80, -5)
                        $ Girl.RecentActions.append("angry")
                        $ Girl.DailyActions.append("angry")
                else:
                        $ Girl.FaceChange("sexy")
                        call Top_Off_Refused(Girl)
            #end "all off?"

            "Хотя бы сними [get_clothing_name(Girl.Arms_key, vin)]. . ." if Girl.Arms:
                    $ Girl.FaceChange("sexy")
                    call AnyLine(Girl,"Ох, ладно.")
                    $ Line = get_clothing_name(Girl.Arms_key, vin)
                    $ Girl.Arms = 0
                    "Она стягивает [Line]."
            "Lose the [get_clothing_name(Girl.Hat_key, vin)]?" if Girl.Hat:
                    $ Line = get_clothing_name(Girl.Hat_key, vin)
                    $ Girl.Hat = 0
                    "[Girl.Name] снимает [Line]."
            "Lose the [get_clothing_name(Girl.Neck_key, vin)]?" if Girl.Neck:
                    $ Line = get_clothing_name(Girl.Neck_key, vin)
                    $ Girl.Neck = 0
                    "[Girl.Name] снимает [Line]."
            "Нет, оголись по пояс или ничего не получишь.":
                    #demanded topless 60, 260 taboo
                    call ToplessorNothing(Girl)

            "Неважно.":
                pass

        $ Line = 0
        $ Girl.RecentActions.append("ask topless")
        $ Girl.DailyActions.append("ask topless")
        $ Tempmod = 0
        return


label Top_Off_Refused(Girl=0): #rkeljsvgb
        #Called form Top_Off when you insist but she refuses
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        $ Girl.FaceChange("angry")
        if Girl is RogueX:
                if "no topless" in Girl.RecentActions:
                        ch_r "Ничего не изменилось, [Girl.Petname]."
                elif "no topless" in Girl.DailyActions:
                        ch_r "Дай мне передохнуть, [Girl.Petname]."
                else:
                        $ Girl.FaceChange("sad")
                        if not Player.Male:
                            ch_r "Боюсь, не в этот раз, [Girl.Petname]. Уверена, что мы не можем просто повеселиться?"
                        else:
                            ch_r "Боюсь, не в этот раз, [Girl.Petname]. Уверен, что мы не можем просто повеселиться?"
        elif Girl is KittyX:
                if "no topless" in Girl.RecentActions:
                        ch_k "[Girl.Like]отвали."
                elif "no topless" in Girl.DailyActions:
                        ch_k "Не сегодня и, возможно, никогда, [Girl.Petname]."
                else:
                        $ KittyX.FaceChange("sad")
                        ch_k "[Girl.Like]нет, но я не хочу из-за этого прекращать. . ."
        elif Girl is EmmaX:
                if "no topless" in Girl.RecentActions:
                        ch_e "Тебе стоит оставить меня в покое."
                elif "no topless" in Girl.DailyActions:
                        ch_e "Я устала от этого, [Girl.Petname]."
                else:
                        if not Player.Male:
                            ch_e "Уверена, что мы не можем обойтись без этого?"
                        else:
                            ch_e "Уверен, что мы не можем обойтись без этого?"
        elif Girl is LauraX:
                if "no topless" in Girl.RecentActions:
                        ch_l "Ты переходишь черту, [Girl.Petname]."
                elif "no topless" in Girl.DailyActions:
                        if not Player.Male:
                            ch_l "Ты мне уже надоела, [Girl.Petname]."
                        else:
                            ch_l "Ты мне уже надоел, [Girl.Petname]."
                else:
                        ch_l "Значит ничего не будет?"
        elif Girl is JeanX:
                if "no topless" in Girl.RecentActions:
                        ch_j "Осторожней, [Girl.Petname]."
                elif "no topless" in Girl.DailyActions:
                        ch_j "Все об одном?"
                else:
                        ch_j "Осторожней. . ."
        elif Girl is StormX:
                if "no topless" in Girl.RecentActions:
                        ch_s "Я отказываюсь продолжать подобное."
                elif "no topless" in Girl.DailyActions:
                        ch_s "Ищи то, что тебя порадует, в другом месте, [Girl.Petname]."
                else:
                        ch_s "Ты настаиваешь?"
        elif Girl is JubesX:
                if "no topless" in Girl.RecentActions:
                        ch_v "Думаю, я ясно выразилась. . ."
                elif "no topless" in Girl.DailyActions:
                        ch_v "Слушай, прекращай, [Girl.Petname]."
                else:
                        ch_v "Слушай, успокойся. . ."
        elif Girl is GwenX:
                if "no topless" in Girl.RecentActions:
                        ch_g "Сиськи в другом замке. . ."
                elif "no topless" in Girl.DailyActions:
                        ch_g "Хватит спрашивать, [Girl.Petname]."
                else:
                        ch_g "Серьезно, нет."
        elif Girl is BetsyX:
                if "no topless" in Girl.RecentActions:
                        ch_b "Я не могу выразиться яснее. . ."
                elif "no topless" in Girl.DailyActions:
                        ch_b "Мне кажется, я все понятно объяснила."
                else:
                        ch_b "Прекращай."
        elif Girl is DoreenX:
                if "no topless" in Girl.RecentActions:
                        ch_d "Прошу, хватит. . ."
                elif "no topless" in Girl.DailyActions:
                        ch_d "Перестань спрашивать, [Girl.Petname]."
                else:
                        ch_d "Ни за что."
        elif Girl is WandaX:
                if "no topless" in Girl.RecentActions:
                        ch_w "Хватит меня доставать. . ."
                elif "no topless" in Girl.DailyActions:
                        ch_w "Откажись от этой идеи, [Girl.Petname]."
                else:
                        ch_w "Хех, нет."
        menu:
            extend ""
            "Хорошо, забудь мои слова." if "no topless" not in Girl.RecentActions:
                    $ Girl.FaceChange("sexy")
                    $ Girl.Statup("Love", 70, 2)
                    if Girl in (RogueX,KittyX,GwenX,DoreenX):
                            call AnyLine(Girl,"Отлично!")
                    else:
                            call AnyLine(Girl,"Хорошо.")
            "Извини, я больше не буду." if "no topless" in Girl.RecentActions:
                    if Girl is RogueX:
                            ch_r "Ладно. . ."
                    elif Girl is KittyX:
                            ch_k "Хорошо!"
                    else:
                            call AnyLine(Girl,"Хорошо.")
            "Нет, я настаиваю. . .":
                    $ Girl.Brows = "angry"
                    if Girl is RogueX:
                            $ Girl.Brows = "confused"
                            ch_r "Ну ладно, [Girl.Petname], тебе же хуже."
                    elif Girl is KittyX:
                            ch_k "Ну и ладно!"
                    elif Girl is EmmaX:
                            ch_e "Отлично."
                    elif Girl is LauraX:
                            ch_l "Ну, это твой выбор."
                    elif Girl is JeanX:
                            $ Girl.FaceChange("smile")
                            ch_j "Ну и хорошо."
                    elif Girl is StormX:
                            ch_s "Да будет так."
                    elif Girl is JubesX:
                            ch_v "Очень жаль. . ."
                    elif Girl is GwenX:
                            ch_g "Пфф."
                    elif Girl is BetsyX:
                            ch_b "Тогда, боюсь, мы зашли в тупик. . ."
                    elif Girl is DoreenX:
                            ch_d "Ну а -Я- настаиваю на обратном!"
                    elif Girl is WandaX:
                            ch_w "Как хочешь."
                    $ Girl.Statup("Lust", 50, 5)
                    $ Girl.Statup("Love", 70, -2, 1)
                    if "no topless" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 60, 4)
                    $ Girl.RecentActions.append("angry")
                    $ Girl.DailyActions.append("angry")
        $ Girl.RecentActions.append("no topless")
        $ Girl.DailyActions.append("no topless")
        return


label ToplessorNothing(Girl=0): #rkeljsvgb
        #Called from Top_Off if you insist she go topless after she's declined.
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        $ Girl.FaceChange("angry")
        if ApprovalCheck(Girl, 800, "OI", TabM = 4) and ApprovalCheck(Girl, 400, "O", TabM = 3):
            $ Girl.Statup("Love", 20, -2, 1)
            $ Girl.Statup("Love", 70, -5, 1)
            $ Girl.Statup("Inbt", 60, 3)
            $ Girl.FaceChange("sad")
            if Girl is RogueX:
                    if "no topless" in Girl.RecentActions:
                        ch_r "Ладно-ладно, как скажешь."
                    else:
                        ch_r "Хорошо, если ты так этого хочешь."
            elif Girl is KittyX:
                    if "no topless" in Girl.RecentActions:
                        ch_k "Ладно-ладно. В этот раз тебе повезло."
                    else:
                        $ Girl.FaceChange("sad")
                        ch_k "Как скажешь."
            elif Girl is EmmaX:
                    if "no topless" in Girl.RecentActions:
                        ch_e "Ох, хорошо. . ."
                    else:
                        $ Girl.FaceChange("sad")
                        ch_e "Ладно."
            elif Girl is LauraX:
                    if "no topless" in Girl.RecentActions:
                        ch_l "Пфф, ладно. . ."
                    else:
                        $ Girl.FaceChange("sad")
                        ch_l "Пфф, ладно, пофиг."
            elif Girl is JeanX:
                    if "no topless" in Girl.RecentActions:
                        ch_j "Ладно. . ."
                    else:
                        $ Girl.FaceChange("sad")
                        ch_j "Ладно! . . как скажешь."
            elif Girl is StormX:
                    $ Girl.FaceChange("sad")
                    if "no topless" in Girl.RecentActions:
                        ch_s "Пожалуй, иногда нужно идти на компромисс. . ."
                    else:
                        ch_s "Ладно."
            elif Girl is JubesX:
                    if "no topless" in Girl.RecentActions:
                        ch_v "Ладно, хорошо, просто перестань спрашивать."
                    else:
                        ch_v "Ладно, хорошо, как скажешь."
            elif Girl is GwenX:
                    if "no topless" in Girl.RecentActions:
                        ch_g "Ладно, только заткнись."
                    else:
                        ch_g "Ладно-ладно. . ."
            elif Girl is BetsyX:
#                    if "no topless" in Girl.RecentActions:
#                        ch_b "Oh, if we -must.-"
#                    else:
                        ch_b "Ох, если это -так- необходимо. . ."
            elif Girl is DoreenX:
                    ch_d "Ну ладно!"
            elif Girl is WandaX:
                    ch_w "Конечно, как пожелаешь."
            $ Girl.Statup("Obed", 60, 4)
            $ Girl.Statup("Obed", 90, 2)
            $ Girl.Uptop = 1
            "[Girl.Name] медленно приподнимает одежду и обнажает грудь."
            call Girl_First_Topless(Girl)
        else:
            $ Girl.Statup("Love", 200, -10)
            $ Girl.Statup("Obed", 40, -1, 1)
            if Girl is RogueX:
                    if "no topless" in Girl.RecentActions:
                        ch_r "Серьезно, прекращай."
                    else:
                        $ Girl.Brows = "confused"
                        ch_r "Ты получишь от меня лишь \"ничего\"."
            elif Girl is KittyX:
                    if "no topless" in Girl.RecentActions:
                        ch_k "Это[Girl.like]не было мило и в первый раз."
                    else:
                        $ Girl.Brows = "angry"
                        ch_k "[Girl.Like]ни за что!"
            elif Girl is EmmaX:
                    if "no topless" in Girl.RecentActions:
                        $ Girl.Brows = "angry"
                        ch_e "Научись воспринимать \"нет\" за ответ."
                    else:
                        ch_e "Боюсь, что нет."
            elif Girl is LauraX:
                    if "no topless" in Girl.RecentActions:
                        $ Girl.Brows = "angry"
                        ch_l "Тебе стоит успокоиться."
                    else:
                        ch_l "Не-а."
            elif Girl is JeanX:
                    if "no topless" in Girl.RecentActions:
                        $ Girl.Brows = "angry"
                        ch_j "Держи себя в руках."
                    else:
                        ch_j "Ох, нет."
            elif Girl is StormX:
                    if "no topless" in Girl.RecentActions:
                        $ Girl.Brows = "angry"
                        ch_s "Скажу снова, \"нет.\""
                    else:
                        ch_s "Вот тебе мой ответ - \"нет.\""
            elif Girl is JubesX:
                    if "no topless" in Girl.RecentActions:
                        $ Girl.Brows = "angry"
                        ch_v "Послушай, я уже сказала тебе, \"нет.\""
                    else:
                        ch_v "Извини, я на такое не пойду."
            elif Girl is GwenX:
                    if "no topless" in Girl.RecentActions:
                        $ Girl.Brows = "angry"
                        ch_g "Я уже сказала тебе - \"нет\"!"
                    else:
                        ch_g "Извини, не получится."
            elif Girl is BetsyX:
                    if "no topless" in Girl.RecentActions:
                        ch_b "Я вполне ясно выразилась!"
                    else:
                        ch_b "Это совершенно неприемлемо."
            elif Girl is DoreenX:
                    ch_d "Нет!"
            elif Girl is WandaX:
                    ch_w "Еще немного, и я сотру тебя в порошок."
            $ Girl.RecentActions.append("no topless")
            $ Girl.DailyActions.append("no topless")
            $ Girl.RecentActions.append("angry")
            $ Girl.DailyActions.append("angry")
        return
# End Tops ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# Start Bottoms ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Bottoms_Off(Girl=0,Intro = 1, Line = 0, Cnt = 0): #rkeljsvgb
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if not Girl.Legs and not Girl.Panties and not Girl.Hose and not Girl.Acc and not Girl.Boots:
                # If she's already bottomless. Just skip back.
                $ Tempmod = 0
                return

        if "angry" in Girl.RecentActions:
                if Girl is RogueX:
                        ch_r "Я сейчас слишком раздражена, чтобы заниматься подобным."
                elif Girl is KittyX:
                        ch_k "Я единственная \"Киска [[Прим. -Китти - киска, кошечка и т.д.-] \", которую ты здесь увидишь."
                elif Girl is EmmaX:
                        ch_e "Откажусь."
                elif Girl is LauraX:
                        ch_l "Не к той обращаешься."
                elif Girl is JeanX:
                        ch_j "Нет и точка, [Girl.Petname]."
                elif Girl is StormX:
                        ch_s "А ты оптимист."
                        ch_s "Мой ответ - нет."
                elif Girl is JubesX:
                        ch_v "Естественно нет."
                elif Girl is GwenX:
                        ch_g "Успокойся."
                elif Girl is BetsyX:
                        ch_b "Тебе определенно стоит держать себя в руках. . ."
                elif Girl is DoreenX:
                        ch_d "Мне это сейчас не нужно."
                elif Girl is WandaX:
                        ch_w "Мне неинтересно."
                return

        # Will she take her bottoms off Modifiers
        if Girl.SeenPussy and ApprovalCheck(Girl, 700): #You've seen her Pussy.
                $ Tempmod += 20
        elif not Girl.Panties:
                $ Tempmod -= 20
        elif Girl.SeenPanties and ApprovalCheck(Girl, 500): #You've seen her panties.
                $ Tempmod += 5
        if Intro == "dildo":
                $ Tempmod += 20
        if "exhibitionist" in Girl.Traits:
                $ Tempmod += (Taboo * 5)
        if (Girl in Player.Harem or "sex friend" in Girl.Petnames) and not Taboo:
                $ Tempmod += 10
        elif "ex" in Girl.Traits:
                $ Tempmod -= 40
        if "no bottomless" in Girl.RecentActions:
                $ Tempmod -= 20
        elif Girl == StormX and (not Taboo or Girl in Rules):
                #Storm is more up for it if in private or with Xavier cleared
                $ Tempmod += 20

        if Intro:
                if Intro == 2 and Girl.PantsNum() > 5:
                        #It was an addiction scene
                        if Girl is RogueX:
                                ch_r "Я не знаю, ну, если для этого мне нужно будет снять свои трусики. . ."
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Тогда будь готова что после[KittyX.like]ты должна будешь прикаснуться там. . ."
                                else:
                                    ch_k "Тогда будь готов что после[KittyX.like]ты должен будешь прикаснуться там. . ."
                        elif Girl is EmmaX:
                                ch_e "Полагаю, мне придется это сделать, чтобы получить желаемое. . ."
                        elif Girl is LauraX:
                                ch_l "Ну, если мне нужно снять штаны, чтобы получить то, что я хочу. . ."
                        elif Girl is JeanX:
                                ch_j "Наверное, мне придется снять нижнюю часть одежды. . ."
                        elif Girl is StormX:
                                ch_s "Тогда я сниму их. . ."
                        elif Girl is JubesX:
                                ch_v "Думаю, они будут мешать. . ."
                        elif Girl is GwenX:
                                ch_g "Ну, если мы говорим серьезно. . ."
                        elif Girl is BetsyX:
                                ch_b "Пожалуй, в одежде у нас ничего не получится. . ."
                        elif Girl is DoreenX:
                                ch_d "О, я думаю, нам нужно это снять. . ."
                        elif Girl is WandaX:
                                ch_w "Ну, думаю, мне придется это снять."
                else:
                        if Girl.Legs and not Girl.Upskirt: #fix jube
                                ch_p "Будет лучше, если ты снимешь [get_clothing_name(Girl.Legs_key, vin)]."
                        elif Girl.Panties and not Girl.PantiesDown:
                                ch_p "Будет лучше, если ты снимешь [get_clothing_name(Girl.Panties_key, vin)]."

        $ Approval = ApprovalCheck(Girl, 1200, TabM = 5) # 120, 135, 150, -200(320) taboo, -25 if already seen

        if Situation == "auto":
            $ Cnt = 0

            if not Girl.Upskirt and not Girl.PantiesDown:
                if Girl.PantsNum() == 5:
                    #If she's in a skirt with panties, hike it up?
                    if Approval >= 2 or (Girl.SeenPussy and not Taboo): #fix jube
                            $ Girl.Statup("Inbt", 60, 1)
                            if Taboo:
                                    $ Girl.Statup("Inbt", 90, (int(Taboo/20)))
                            $ Girl.Upskirt = 1
                            "Она задирает юбку."
                            $ Cnt = 1

                if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6:
                    if Girl.Panties:
                        #she has pants and panties on
                        if not Approval or (not Girl.SeenPanties and Taboo):
                            return
                    elif Approval < 2 or (not Girl.SeenPussy and Taboo):
                        return
                    elif Girl.Upskirt:
                        return
                    $ Girl.Statup("Inbt", 60, 1)
                    if Girl.HoseNum() >= 6:
                            $ Line = get_clothing_name(Girl.Hose_key, vin)
                            $ Girl.Hose = 0
                    $ Girl.Upskirt = 1

                    if Girl is KittyX:
                            $ Line = 0
                            $ Line = Girl.Hose_display
                            if Girl.PantsNum(0) >= 6:
                                "[Girl.Name] ворчит себе под нос, а затем [Girl.Legs_display] падают на пол."
                            else:
                                "[Girl.Name]ворчит себе под нос, а затем [Line] на пол."
                            if Girl.Panties:
                                    $ Girl.SeenPanties = 1
                    elif Girl.Panties:
                            if Girl.PantsNum(0) >= 6:
                                "[Girl.Name] ворчит себе под нос, а затем расстегивает и снимает [get_clothing_name(Girl.Legs_key, vin)]."
                            else:
                                "[Girl.Name] ворчит себе под нос, а затем снимает [Line]."
                            $ Girl.SeenPanties = 1
                    else:
                            if Girl.PantsNum(0) >= 6:
                                "[Girl.Name] ворчит себе под нос, а затем расстегивает и снимает [get_clothing_name(Girl.Legs_key, vin)], обнажая голую попку."
                            else:
                                "[Girl.Name] ворчит себе под нос, а затем снимает [Line], обнажая голую попку."
                    call Girl_First_Bottomless(Girl,1)
                    if Taboo:
                        $ Girl.Statup("Inbt", 90, (int(Taboo/10)))
                    $ Cnt = 1

            if Girl.Panties and not Girl.PantiesDown:
                # Just wearing panties, lose them?
                if Approval >= 2 or (Girl.SeenPussy and not Taboo):
                    $ Girl.Statup("Inbt", 70, 2)
                    if Taboo:
                            $ Girl.Statup("Inbt", 90, (int(Taboo/10)))
                    $ Girl.PantiesDown = 1
                    if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6:
                            $ Girl.Upskirt = 1 #fix jube
                    if Girl is KittyX:
                            if Cnt:
                                "Поразмыслив немного, [Girl.Name] позволяет [Girl.Panties_display] также упасть на пол."
                            else:
                                "[Girl.Name] цокает языком от раздражения, и ее [Girl.Panties_display] падают на пол."
                    else:
                            if Cnt:
                                "[Girl.Name] цокает языком от раздражения, а затем также снимает [get_clothing_name(Girl.Panties_key, vin)]."
                            else:
                                "[Girl.Name] цокает языком от раздражения, а затем снимает свои [get_clothing_name(Girl.Panties_key, vin)]."
                    call Girl_First_Bottomless(Girl,1)
                    if Girl is RogueX:
                            ch_r "Они сильно мешались. Давай попробуем теперь."
                    elif Girl is KittyX:
                            ch_k "Прямо очень бесит, что ты не можешь прикасаться ко мне сквозь одежду."
                    elif Girl is EmmaX:
                            ch_e "Они мешались."
                    elif Girl is LauraX:
                            ch_l "Думаю, теперь ничто не будет мешать."
                    elif Girl is JeanX:
                            ch_j "Ладно, давай попробуем так, [Girl.Petname]."
                    elif Girl is StormX:
                            ch_s "Это должно все упростить. . ."
                    elif Girl is JubesX:
                            ch_v "Хорошо, так немного удобнее. . ."
                    elif Girl is GwenX:
                            ch_g "Ладно, теперь, когда ничего не мешает. . ."
                    elif Girl is BetsyX:
                            ch_b "Так ведь лучше, правда?"
                    elif Girl is DoreenX:
                            ch_d "Теперь ничего не помешает. . ."
                    elif Girl is WandaX:
                            ch_w "Ладно, так будет получше."
            return


        if Approval >= 2:
            #will she volunteer to strip to underwear?
            $ Girl.FaceChange("sexy", 1)
            if Girl.Forced:
                    $ Girl.FaceChange("sad", 1)
                    $ Girl.Statup("Love", 20, -2, 1)
                    $ Girl.Statup("Love", 70, -3, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 60, 1)
            if Girl is RogueX:
                    if Approval >= 3:
                        $ Line = "Хммм, что ты хочешь увидеть? . ."
                    else:
                        $ Line = "Ну, ладно. Но я бы хотела сохранить \"хоть немного\" благопристойности. . ."
            elif Girl is KittyX:
                    if Approval >= 3:
                        if not Player.Male:
                            $ Line = "Хихи, что бы ты хотела увидеть? . ."
                        else:
                            $ Line = "Хихи, что бы ты хотел увидеть? . ."
                    else:
                        $ Line = "Ладно, может быть, только не торопи. . ."
            elif Girl is EmmaX:
                    if Approval >= 3:
                        if not Player.Male:
                            $ Line = "Мммм, что бы ты хотела?"
                        else:
                            $ Line = "Мммм, что бы ты хотел?"
                    else:
                        if not Player.Male:
                            $ Line = "Что бы ты с меня сняла?"
                        else:
                            $ Line = "Что бы ты с меня снял?"
            elif Girl is LauraX:
                    if Approval >= 3:
                        if not Player.Male:
                            $ Line = "От чего ты хотела бы избавиться?"
                        else:
                            $ Line = "От чего ты хотел бы избавиться?"
                    else:
                        if not Player.Male:
                            $ Line = "Хм, чтобы ты хотела снять с меня?"
                        else:
                            $ Line = "Хм, чтобы ты хотел снять с меня?"
            elif Girl is JeanX:
                    if Approval >= 3:
                        if not Player.Male:
                            $ Line = "Что бы ты хотела снять?"
                        else:
                            $ Line = "Что бы ты хотел снять?"
                    else:
                        $ Line = "Например. . . что? . ."
            elif Girl is StormX:
                        if not Player.Male:
                            $ Line = "Что бы ты хотела, чтобы я сняла?"
                        else:
                            $ Line = "Что бы ты хотел, чтобы я сняла?"
            elif Girl is JubesX:
                        $ Line =  "Ну, что например?"
            elif Girl is GwenX:
                        if not Player.Male:
                            $ Line = "Так что бы ты хотела, чтобы я сняла?"
                        else:
                            $ Line = "Так что бы ты хотел, чтобы я сняла?"
            elif Girl is BetsyX:
                        $ Line = "От чего мне избавиться?"
            elif Girl is DoreenX:
                        $ Line = "Ну, что мне снять?"
            elif Girl is WandaX:
                        $ Line = "Ну? И что мне снять?"
            call Bottoms_Off_Legs(Girl)

            if not Girl.Panties and Girl.RecentActions.count("bottomless") < 2:
                    $ Girl.Statup("Obed", 50, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 50, 3)
                    $ Girl.Statup("Lust", 80, 3)

        elif Girl.Legs or Girl.Panties or Girl.Hose or Girl.Boots or Girl.Acc:
            # She'd rather not strip but might
            $ Girl.FaceChange("bemused", 1)
            if Girl is RogueX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_r "Что я только что тебе сказала, [Girl.Petname]?"
                    elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_r "Сомневаюсь, что твои шансы увеличились, [Girl.Petname]. . ."
                    elif Approval and not Girl.SeenPussy:
                        ch_r "Не все, ладно?"
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_r "И к этому я тоже пока не готова."
                    elif "no bottomless" in Girl.DailyActions:
                        if not Player.Male:
                            ch_r "Ты забыла, что я сказала ранее, [Girl.Petname]?"
                        else:
                            ch_r "Ты забыл, что я сказала ранее, [Girl.Petname]?"
                    elif Taboo:
                        ch_r "Я не знаю, в таком людном месте. . ."
                    elif Approval:
                        ch_r "Я не знаю, хочу ли я снимать свою нижнюю часть одежды. . ."
                    elif Girl.SeenPussy:
                        if not Player.Male:
                            ch_r "Ну, ты уже ее видела, но. . ."
                        else:
                            ch_r "Ну, ты уже ее видел, но. . ."
                    else:
                        ch_r "Я не собираюсь снимать нижнюю часть своей одежды."
            elif Girl is KittyX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_k "Последнее предупреждение, [Girl.Petname]. Нет."
                    elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_k "Не учись на своих же ошибках, [Girl.Petname]. . ."
                    elif Approval and not Girl.SeenPussy:
                        ch_k "Я в этом не уверена. . ."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_k "Ты хочешь слишком многого."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_k "У тебя память, как у золотой рыбки, [Girl.Petname]?"
                    elif Taboo:
                        ch_k "Здесь слишком[Girl.like]людно. . ."
                    elif Approval:
                        ch_k "Я[Girl.like]не уверена насчет этого. . ."
                    elif Girl.SeenPussy:
                        if not Player.Male:
                            ch_k "Ну, ты уже видела ее[Girl.like]ранее . . ."
                        else:
                            ch_k "Ну, ты уже видел ее[Girl.like]ранее . . ."
                    elif Girl.PantsNum(0) > 6:
                        ch_k "Я не сниму штаны."
                    elif Girl.PantsNum(0) > 5:
                        ch_k "Я не сниму шорты."
                    else:
                        ch_k "Я не сниму трусики."
            elif Girl is EmmaX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_e "Перестань спрашивать, ты ставишь себя в неловкое положение."
                    elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_e "Ты действительно думаешь, что это вероятно?"
                    elif Approval and not Girl.SeenPussy:
                        if not Player.Male:
                            ch_e "Я не знаю, готова ли ты к этому."
                        else:
                            ch_e "Я не знаю, готов ли ты к этому."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_e "Осторожнее, ты заходишь слишком далеко. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_e "Неужели ты ничему не учишься, [Girl.Petname]?"
                    elif Taboo:
                        ch_e "Здесь слишком много посторонних глаз, [Girl.Petname]. . ."
                    elif Approval:
                        ch_e "Скорее всего, нет. . ."
                    elif Girl.SeenPussy:
                        if not Player.Male:
                            ch_e "Я думаю, ты уже насмотрелась на нее . . ."
                        else:
                            ch_e "Я думаю, ты уже насмотрелся на нее . . ."
                    elif Girl.PantsNum(0) > 6:
                        ch_e "Я не сниму брюки."
                    elif Girl.PantsNum(0) == 5:
                        ch_e "Я не сниму юбку."
                    elif Girl.PantsNum(0) == 6:
                        ch_e "Я не сниму шорты."
                    else:
                        ch_e "Я не сниму трусики."
            elif Girl is LauraX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_l "Ты ставишь себя в хреновое положение."
                    elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_l "Перестань давить на меня."
                    elif Approval and not Girl.SeenPussy:
                        if not Player.Male:
                            ch_l "Я не уверена, что ты этого заслужила."
                        else:
                            ch_l "Я не уверена, что ты этого заслужил."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_l "Ты слишком спешишь, [Girl.Petname]. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        if not Player.Male:
                            ch_l "Ты слишком нетерпелива. . ."
                        else:
                            ch_l "Ты слишком нетерпелив. . ."
                    elif Taboo:
                        ch_l "Мне здесь неуютно, [Girl.Petname]. . ."
                    elif Approval:
                        ch_l "Скорее всего, нет. . ."
                    elif Girl.SeenPussy:
                        if not Player.Male:
                            ch_l "Ты, наверное, уже видела достаточно. . ."
                        else:
                            ch_l "Ты, наверное, уже видел достаточно. . ."
                    elif Girl.PantsNum(0) > 6:
                        ch_l "Ну, Я не сниму штаны."
                    elif Girl.PantsNum(0) == 5:
                        ch_l "Ну, я не сниму юбку."
                    elif Girl.PantsNum(0) == 6:
                        ch_l "Ну, Я не сниму шорты."
                    else:
                        ch_l "Ну, Я не сниму трусики."
            elif Girl is JeanX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_j "Послушай, этого не произойдет."
                    elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_j "Думаешь, что-то изменилось?"
                    elif Approval and not Girl.SeenPussy:
                        if not Player.Male:
                            ch_j "Хмм. . . ты должна это заслужить. . ."
                        else:
                            ch_j "Хмм. . . ты должен это заслужить. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_j "Снова?"
                    elif Taboo:
                        ch_j "Не здесь, [Girl.Petname]. . ."
                    elif Approval:
                        ch_j "Хмм. . ."
                    elif Girl.SeenPussy:
                        ch_j "Хмм. . ."
                    elif Girl.PantsNum(0) > 6:
                        ch_j "Я не сниму штаны."
                    elif Girl.PantsNum(0) == 5:
                        ch_j "Я не сниму юбку."
                    elif Girl.PantsNum(0) == 6:
                        ch_j "Я не сниму шорты."
                    else:
                        ch_j "Я не сниму трусики."
            elif Girl is StormX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_s "Тебе нужно перестать спрашивать об этом."
                    elif Taboo and Girl not in Rules:
                        ch_s "Точно не на людях, [Girl.Petname]. . ."
                    elif Approval:
                        ch_s "Я не уверена. . ."
                    elif Girl.PantsNum(0) > 6:
                        ch_s "Я не буду снимать брюки."
                    elif Girl.PantsNum(0) == 5:
                        ch_s "Я не буду снимать юбку."
                    elif Girl.PantsNum(0) == 6:
                        ch_s "Я не буду снимать шорты."
                    else:
                        ch_s "Я не буду снимать трусики."
            elif Girl is JubesX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        if not Player.Male:
                            ch_v "Остынь, чувиха."
                        else:
                            ch_v "Остынь, чувак."
                    elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_v "Не дави на меня, [Girl.Petname]"
                    elif Approval and not Girl.SeenPussy:
                        if not Player.Male:
                            ch_v "Я уверена, чувиха."
                        else:
                            ch_v "Я уверена, чувак."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_v "Ты слишком спешишь, [Girl.Petname]. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        if not Player.Male:
                            ch_v "Ты слишком нетерпелива. . ."
                        else:
                            ch_v "Ты слишком нетерпелив. . ."
                    elif Taboo:
                        ch_v "[Girl.Petname], ты понимаешь, что здесь людно?"
                    elif Approval:
                        ch_v "Сомневаюсь. . ."
                    elif Girl.SeenPussy:
                        ch_v "Нужно еще раз взглянуть?"
                    elif Girl.PantsNum(0) > 6:
                        ch_v "Нууу, я не сниму штаны."
                    elif Girl.PantsNum(0) == 5:
                        ch_v "Нууу, я не сниму юбку."
                    elif Girl.PantsNum(0) == 6:
                        ch_v "Нууу, Я не сниму шорты."
                    else:
                        ch_v "Нууу, Я не сниму трусики."
            elif Girl is GwenX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_g "Прекращай спрашивать."
                    elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_g "Хватит спрашивать, [Girl.Petname]."
                    elif Approval and not Girl.SeenPussy:
                        ch_g "Да ладно тебе. . ."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_g "Прекращай спрашивать, [Girl.Petname]. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_g "Ты все спрашиваешь и спрашиваешь. . ."
                    elif Taboo:
                        ch_g "[Girl.Petname], здесь не место для этого."
                    elif Approval:
                        ch_g "Я не уверена. . ."
                    elif Girl.SeenPussy:
                        ch_g "Очень понравилась?"
                    elif Girl.PantsNum(0) > 6:
                        ch_g "Эм, Я не сниму брюки."
                    elif Girl.PantsNum(0) == 5:
                        ch_g "Эм, Я не сниму юбку."
                    elif Girl.PantsNum(0) == 6:
                        ch_g "Эм, Я не сниму шорты."
                    else:
                        ch_g "Эм, Я не сниму трусики."
            elif Girl is BetsyX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_b "Перестань спрашивать."
                    elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_b "Перестань спрашивать, [Girl.Petname]."
                    elif Approval and not Girl.SeenPussy:
                        ch_b "Возможно. . ."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_b "Перестань спрашивать, [Girl.Petname]. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_b "Перестань спрашивать. . ."
                    elif Taboo:
                        ch_b "Я не смогу раздеться в таком месте."
                    elif Approval:
                        ch_b "Я не уверена. . ."
                    elif Girl.SeenPussy:
                        ch_b "Хочешь еще раз взглянуть?"
                    elif Girl.PantsNum(0) > 6:
                        ch_b "Что ж, я не сниму брюки."
                    elif Girl.PantsNum(0) == 5:
                        ch_b "Что ж, я не сниму юбку."
                    elif Girl.PantsNum(0) == 6:
                        ch_b "Что ж, я не сниму шорты."
                    else:
                        ch_b "Что ж, я не сниму трусики."
            elif Girl is DoreenX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_d "Хватит спрашивать."
                    elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_d "Хватит спрашивать, [Girl.Petname]."
                    elif Approval and not Girl.SeenPussy:
                        ch_d "Да ладно тебе. . ."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_d "Хватит спрашивать, [Girl.Petname]. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_d "Хватит спрашивать. . ."
                    elif Taboo:
                        ch_d "[Girl.Petname], я не могу сделать это здесь. . ."
                    elif Approval:
                        ch_d "Я не уверена. . ."
                    elif Girl.SeenPussy:
                        ch_d "О, тебе понравилось?"
                    elif Girl.PantsNum(0) > 6:
                        ch_d "Эм, я не сниму штанов."
                    elif Girl.PantsNum(0) == 5:
                        ch_d "Эм, я не сниму юбку."
                    elif Girl.PantsNum(0) == 6:
                        ch_d "Эм, я не сниму шорты."
                    else:
                        ch_d "Эм, я не сниму трусики."
            elif Girl is WandaX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_w "Перестань спрашивать."
                    elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_w "Перестань спрашивать, [Girl.Petname]."
                    elif Approval and not Girl.SeenPussy:
                        ch_w "Да ладно тебе. . ."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_w "Перестань спрашивать, [Girl.Petname]. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_w "Перестань спрашивать. . ."
                    elif Taboo:
                        ch_w "Только не здесь. . ."
                    elif Approval:
                        ch_w "Я не уверена. . ."
                    elif Girl.SeenPussy:
                        ch_w "Хочешь увидеть больше?"
                    elif Girl.PantsNum(0) > 6:
                        ch_w "Эм, я не сниму штаны."
                    elif Girl.PantsNum(0) == 5:
                        ch_w "Эм, я не сниму платье."
                    elif Girl.PantsNum(0) == 6:
                        ch_w "Эм, я не сниму шорты."
                    else:
                        ch_w "Эм, я не сниму трусики."
            menu:
                extend ""
                "Ладно, тогда не забудь." if "no bottomless" not in Girl.RecentActions:
                    if "ask bottomless" not in Girl.DailyActions:
                            $ Girl.Statup("Lust", 80, 2)
                            $ Girl.Statup("Love", 70, 1)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Inbt", 50, 3)
                    if Girl.Forced:
                            $ Girl.Mouth = "smile"
                            if Girl is RogueX:
                                    ch_r "Благодарю."
                            elif Girl is KittyX:
                                    ch_k ". . . спасибо."
                            elif Girl is EmmaX:
                                    ch_e "Это очень. . . великодушно."
                            elif Girl is LauraX:
                                    ch_l "Ладно."
                            elif Girl is JeanX:
                                    ch_j ". . ."
                            elif Girl is StormX:
                                    ch_s "Благодарю. . ."
                            elif Girl is JubesX:
                                    ch_v "Спасибочки. . ."
                            elif Girl is GwenX:
                                    ch_g "Хорошо. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я это ценю."
                            elif Girl is DoreenX:
                                    ch_d "Спасибо."
                            elif Girl is WandaX:
                                    ch_w "Спасибо."
                            if "ask bottomless" not in Girl.DailyActions:
                                    $ Girl.Statup("Love", 20, 3)
                                    $ Girl.Statup("Love", 70, 4)
                                    $ Girl.Statup("Inbt", 60, 2)

                "Извини - извини." if "no bottomless" in Girl.RecentActions:
                            if Girl is RogueX:
                                    ch_r "Ладно, только успокойся."
                            elif Girl is KittyX:
                                    ch_k "[Girl.Like], ладно, как скажешь."
                            elif Girl is GwenX:
                                    ch_g "Я тебя понимаю."
                            else:
                                    call AnyLine(Girl,"Хорошо.")

                "Ну пожалуйста?":
                        if "no bottomless" in Girl.DailyActions:
                                $ Girl.FaceChange("angry", 1)
                                if Girl is RogueX:
                                        ch_r "Слушай, что тебе говорят."
                                elif Girl is KittyX:
                                        ch_k "Я уже сказала тебе \"нет.\""
                                elif Girl is EmmaX:
                                        ch_e "Полагаю, ты уже знаешь мой ответ."
                                elif Girl is LauraX:
                                        if not Player.Male:
                                            ch_l "Ты меня слышала."
                                        else:
                                            ch_l "Ты меня слышал."
                                elif Girl is JeanX:
                                        if not Player.Male:
                                            ch_j "Ты глухая или тупая?"
                                        else:
                                            ch_j "Ты глухой или тупой?"
                                elif Girl is StormX:
                                        ch_s "Я уже высказалась по этому поводу."
                                elif Girl is JubesX:
                                        ch_v "Нет."
                                elif Girl is GwenX:
                                        ch_g "Не-а. . ."
                                elif Girl is BetsyX:
                                        ch_b "Я уже достаточно ясно выразилась."
                                elif Girl is DoreenX:
                                        ch_d "Ни за что!"
                                elif Girl is WandaX:
                                        $ Girl.FaceChange("sly", 1)
                                        ch_w "Хех, нет."
                        else:
                            if Approval and ApprovalCheck(Girl, 600, "L", TabM=1):
                                $ Girl.FaceChange("sexy", 1)
                                $ D20 = renpy.random.randint(1, 3)
                                $ Approval += 1 if D20 == 3 else 0
                                if Girl is RogueX:
                                        $ Line = "Ну, что предлагаешь. . .?"
                                elif Girl is KittyX:
                                        $ Line = "Наверное, можно. . ."
                                elif Girl is EmmaX:
                                        $ Line = "Возможно. . ."
                                elif Girl is LauraX:
                                        $ Line = "Может быть. . ."
                                elif Girl is JeanX:
                                        $ Line = "-вздыхает-. . . например, что?"
                                elif Girl is StormX:
                                        ch_s ". . ."
                                        $ Line = "Что ты хочешь? . ."
                                elif Girl is JubesX:
                                        $ Line =  "Нуууу, возмооожно. . ."
                                elif Girl is GwenX:
                                        $ Line = "Хорошо. . ."
                                elif Girl is BetsyX:
                                        $ Line = "Что конкретно ты хочешь?"
                                elif Girl is DoreenX:
                                        $ Line =  "Ну и чего ты хочешь? . ."
                                elif Girl is WandaX:
                                        $ Line = "Ну и что думаешь?"
                                call Bottoms_Off_Legs(Girl)
                            else:
                                $ Girl.FaceChange("sexy")
                                call Bottoms_Off_Refused(Girl)

                "Не обязательно снимать все. . ." if Girl.Legs or Girl.HoseNum() >= 10 or Girl.Panties == "shorts":
                    if Approval and "no bottomless" not in Girl.DailyActions:
                            $ Girl.FaceChange("bemused", 1)
                            $ Line = "Что тогда ты предлагаешь снять?"
                            call Bottoms_Off_Legs(Girl)
                    else:
                            # She refuses your request. . .
                            $ Girl.FaceChange("sexy")
                            call Bottoms_Off_Refused(Girl)
                "Не обязательно снимать все. . . (locked)" if not Girl.Legs and Girl.HoseNum() < 10 and Girl.Panties != "shorts":
                            pass

                "Нет, снимай.":         #85 and -200 taboo
                    if (Approval and Girl.Obed >= 250) or (ApprovalCheck(Girl, 850, "OI", TabM = 5) and ApprovalCheck(Girl, 400, "O")):
                                $ Girl.Statup("Love", 20, -1, 1)
                                $ Girl.Statup("Love", 70, -5, 1)
                                $ Girl.Statup("Obed", 50, 4)
                                $ Girl.Statup("Inbt", 60, 3)
                                if Girl is RogueX:
                                        $ Line =  "Что ты хочешь там увидеть?"
                                elif Girl is KittyX:
                                        $ Line =  KittyX.Like+" блин, ты, похоже, серьезно. . ."
                                elif Girl is EmmaX:
                                        $ Line =  "Не испытывай мое терпение. . ."
                                elif Girl is LauraX:
                                        $ Line =  "Не дави на меня. . ."
                                elif Girl is JeanX:
                                        $ Line = "Подумай хорошенько. . ."
                                elif Girl is StormX:
                                        ch_s ". . ."
                                        $ Line = "Что ты хочешь? . ."
                                elif Girl is JubesX:
                                        $ Line =  "Ну и тон у тебя. . ."
                                elif Girl is GwenX:
                                        $ Line = "Тщательно обдумай свой следующий ответ. . ."
                                elif Girl is BetsyX:
                                        $ Line = "Тогда, боюсь, нам больше нечего обсуждать."
                                elif Girl is DoreenX:
                                        $ Line = "Ты слишком торопишь события. . ."
                                elif Girl is WandaX:
                                        $ Line = "Осторожнее с просьбами. . ."
                                $ Approval = 1 if Approval < 1 else Approval
                                $ Girl.Forced = 1
                                call Bottoms_Off_Legs(Girl)
                    else:
                        $ Girl.Statup("Love", 200, -10)
                        if ApprovalCheck(Girl, 400, "O"):
                                if Girl is RogueX:
                                        ch_r "Я. . . Я правда не могу."
                                elif Girl is KittyX:
                                        ch_k "Извини[Girl.like]ничего не выйдет."
                                elif Girl is EmmaX:
                                        ch_e "Определённо нет."
                                elif Girl is LauraX:
                                        ch_l "Ни за что."
                                elif Girl is JeanX:
                                        ch_j "Ха! нет."
                                elif Girl is StormX:
                                        ch_s "К сожалению, нет."
                                elif Girl is JubesX:
                                        ch_v "Естественно нет."
                                elif Girl is GwenX:
                                        ch_g "Извини. . ."
                                elif Girl is BetsyX:
                                        ch_b "Боюсь, я не могу."
                                elif Girl is DoreenX:
                                        ch_d "Для меня это слишком. . ."
                                elif Girl is WandaX:
                                        ch_w "Не дави на меня."
                        else:
                                $ Girl.FaceChange("angry")
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Ну и пошла ты тогда!"
                                        else:
                                            ch_r "Ну и пошел ты тогда!"
                                elif Girl is KittyX:
                                        ch_k "ПНХ."
                                elif Girl is EmmaX:
                                        ch_e "Уйди с глаз моих, [Girl.Petname]."
                                elif Girl is LauraX:
                                        ch_l "Отъебись."
                                elif Girl is JeanX:
                                        ch_j "Даже не мечтай."
                                elif Girl is StormX:
                                        ch_s "Нет."
                                elif Girl is JubesX:
                                        ch_v "Нее. . ."
                                elif Girl is GwenX:
                                        ch_g "Мне жаль, но нет."
                                elif Girl is BetsyX:
                                        ch_b "Какой ужас!"
                                elif Girl is DoreenX:
                                        ch_d "Как грубо!"
                                elif Girl is WandaX:
                                        ch_w "Нет."
                                $ Girl.RecentActions.append("angry")
                                $ Girl.DailyActions.append("angry")
                        $ Girl.RecentActions.append("no bottomless")
                        $ Girl.DailyActions.append("no bottomless")

        $ Tempmod = 0
        $ Girl.RecentActions.append("ask bottomless")
        $ Girl.DailyActions.append("ask bottomless")
        return

label Bottoms_Off_Legs(Girl=0):  #rkeljsvgb
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if Girl.Forced:
            $ Girl.FaceChange("sad", 1)
        elif ApprovalCheck(Girl, 1100, "OI", TabM = 3):
            $ Girl.FaceChange("sly")
        elif ApprovalCheck(Girl, 1400, TabM = 3):
            $ Girl.FaceChange("sexy", 1)
        else:
            $ Girl.FaceChange("bemused", 1)

        $ Line = "Хорошо, что мне снять?" if not Line else Line
        $ Cnt = 1
        while Cnt and (Girl.Legs or Girl.Panties or Girl.Hose or Girl.Boots or Girl.Acc in ("sweater","scarf")):
            call AnyLine(Girl,Line)
            menu:
                # She's asking what you'd like to see.
                extend ""
                "Сними все" if Line != "Что тогда ты предлагаешь снять?":
                        #approval a given
                        if not Girl.Panties and Girl.HoseNum() < 10:
                                call NoPantiesOn(Girl)

                        if Girl.Boots:
                                $ Line = get_clothing_name(Girl.Boots_key, vin)
                                $ Girl.Boots = 0
                                "Она снимает [Line]."
                        if Girl.Legs:
                                $ Line = get_clothing_name(Girl.Legs_key, vin)
                                $ Girl.Legs = 0
                                if not Girl.SeenPanties:
                                    if Girl is RogueX:
                                            "[Girl.Name] робко снимает нижнюю [Line]."
                                    elif Girl is KittyX:
                                            "[Girl.Name] робко сдергивает [Line] со своих ног."
                                    else:
                                            "[Girl.Name] снимает [Line]."
                                    $ Girl.SeenPanties = 1
                                else:
                                    "[Girl.Name] снимает [Line]."

                        if Approval < 2 and not Girl.Panties and Girl.HoseNum() >= 10:
                                call NoPantiesOn(Girl)

                        if Girl is JubesX and JubesX.Acc != "shut jacket":
                                #if it's an ordinary jacket, leave it on
                                pass
                        elif Girl is JubesX and JubesX.Acc == "shut jacket":
                                $ Line = get_clothing_name(Girl.Acc_key, vin)
                                $ Girl.Acc = 0
                                "Она снимает свою куртку."
                                call Girl_First_Bottomless(Girl)
                        elif Girl.Acc:
                                $ Line = get_clothing_name(Girl.Acc_key, vin)
                                $ Girl.Acc = 0
                                "Она снимает [Line]."


                        if Girl.Hose:
                                $ Line = Girl.Hose_display #HoseName
                                $ Girl.Hose = 0
                                if Girl is KittyX:
                                        "Ее [Line] падают на пол."
                                else:
                                        "Она стягивает свои [Line]."

                        if Approval < 2:
                                call NoPantiesOn(Girl)

                        if Girl.Panties:
                            if Girl.Panties == "swimsuit" or Girl.Panties == "saiyan leotard" or Girl.Panties == "cammy leotard" or Girl.Panties == "raven leotard":
                                #if this is Betsy, she has the swimsuit on,
                                if Girl.Uptop:
                                        #if it's already mostly open
                                        $ Girl.Panties = 0
                                        $ Girl.Chest = 0
                                        "Она смотрит на вас, снимая [get_clothing_name(Girl.Panties, vin)]."
                                else:
                                        $ Girl.PantiesDown = 1
                                        "Она смотрит на вас, сдвигая [get_clothing_name(Girl.Panties, vin)] в сторону."
                            else:
                                if Girl is KittyX:
                                        $ Line = Girl.Panties_display
                                        $ Girl.Panties = 0
                                        "Она смотрит вам в глаза, пока ее [Line] падают на пол."
                                else:
                                        $ Line = get_clothing_name(Girl.Panties, vin)
                                        $ Girl.Panties = 0
                                        "Она смотрит на вас, пока снимает [Line]."
                        if Girl in (JubesX,WandaX):
                                $ Girl.Over = 0 if Girl.Over == "dress" else Girl.Over
                                call Girl_First_Topless(Girl)
                        call Girl_First_Bottomless(Girl)


                "Сними [get_clothing_name(Girl.Legs, vin)]." if Girl.Legs:
                        if Girl.Panties and Approval >= 2:
                            $ Girl.FaceChange("sexy")
                            if Girl is RogueX:
                                    ch_r "Думаю, я смогу это сделать. . ."
                            elif Girl is KittyX:
                                    ch_k "Это. . . вполне выполнимо. . ."
                            elif Girl is EmmaX:
                                    ch_e "С этим я справлюсь. . ."
                            elif Girl is LauraX:
                                    ch_l "Думаю, можно. . ."
                            elif Girl is JeanX:
                                    ch_j ". . .можно. . ."
                            elif Girl is StormX:
                                    ch_s "Я могу это сделать. . ."
                            elif Girl is JubesX:
                                    ch_v "Нуу, это я могу. . ."
                            elif Girl is GwenX:
                                    ch_g "Эм, ладно. . ."
                            elif Girl is BetsyX:
                                    ch_b "Пожалуй, это можно устроить. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ну, думаю, это можно. . ."
                            elif Girl is WandaX:
                                    ch_w "Конечно."
                        elif Approval:
                                $ Girl.FaceChange("sexy", 1)
                                if Approval < 2 and not Girl.Panties and Girl.HoseNum() < 10:
                                    call NoPantiesOn(Girl)
                        else:
                                $ Girl.FaceChange("sexy")
                                call Bottoms_Off_Refused(Girl)
                                return

                        if Girl.Over == "dress" and Girl.Legs == "dress":
                                menu:
                                    "Все платье?"
                                    "Да [[верхнюю и нижнюю части]":
                                            $ Girl.Over = 0
                                    "Только низ.":
                                            pass
                        if not Girl.Panties and Girl.HoseNum() < 10:
                                $ Girl.FaceChange("sly", 2)
                                if Girl is KittyX:
                                        $ Line = Girl.Legs_display
                                        $ Girl.Legs = 0
                                        "Она, краснея, заглядывает вам в глаза, затем ее [Line] падают на пол."
                                elif Girl is RogueX:
                                        $ Line = get_clothing_name(Girl.Legs, vin)
                                        $ Girl.Legs = 0
                                        "Она краснеет и начинает хитро смотреть на вас, пока снимает свои [Line]."
                                else:
                                        $ Line = get_clothing_name(Girl.Legs, vin)
                                        $ Girl.Legs = 0
                                        "Она хитро смотрит на вас, пока снимает свои [Line]."
                                call Girl_First_Bottomless(Girl)
                        elif not Girl.SeenPanties:
                                if Girl is KittyX:
                                        $ Line = Girl.Legs_display
                                        $ Girl.Legs = 0
                                        "Она, краснея, заглядывает вам в глаза, затем ее [Line] падают на пол."
                                elif Girl is RogueX:
                                        $ Line = get_clothing_name(Girl.Legs, vin)
                                        $ Girl.Legs = 0
                                        "Она краснеет и начинает хитро смотреть на вас, пока снимает свои [Line]."
                                else:
                                        $ Line = get_clothing_name(Girl.Legs, vin)
                                        $ Girl.Legs = 0
                                        "Она хитро смотрит на вас, пока снимает свои [Line]."
                                $ Girl.SeenPanties = 1
                        else:
                                $ Line = get_clothing_name(Girl.Legs, vin)
                                $ Girl.Legs = 0
                                "[Girl.Name] снимает свои [Line]."
                        if Girl in (JubesX,WandaX):
                                $  Girl.Over = 0 if Girl.Over == "dress" else Girl.Over
                                call Girl_First_Topless(Girl)
                        $ Girl.FaceChange("bemused", 1)

                "Сними [get_clothing_name(Girl.Over, vin)]." if Girl.Over == "dress" and Girl.Legs != "dress":
                        if Girl.Panties and Approval >= 2:
                            $ Girl.FaceChange("sexy")
                            if Girl is JubesX:
                                    ch_v "Нуу, это я могу. . ."
                        elif Approval:
                                $ Girl.FaceChange("sexy", 1)
                                if Approval < 2 and not Girl.Panties and Girl.HoseNum() < 10:
                                    call NoPantiesOn(Girl)
                        else:
                                $ Girl.FaceChange("sexy")
                                call Bottoms_Off_Refused(Girl)
                                return

                        $ Line = get_clothing_name(Girl.Over, vin)
                        $ Girl.Over = 0
                        if not Girl.Panties and Girl.HoseNum() < 10:
                                $ Girl.FaceChange("sly", 2)
                                "Она одаривает вас хитрым взглядом, а затем снимает [Line]."
                                call Girl_First_Bottomless(Girl)
                        elif not Girl.SeenPanties:
                                "Она одаривает вас хитрым взглядом, а затем снимает [Line]."
                                $ Girl.SeenPanties = 1
                        else:
                                "[Girl.Name] снимает [Line]."
                        call Girl_First_Topless(Girl)
                        $ Girl.FaceChange("bemused", 1)

                "Сними [get_clothing_name(Girl.Panties, vin)]." if Girl.Panties:
                        if Approval < 2:
                                if Girl is RogueX:
                                        ch_r "Нет, спасибо, [Girl.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Извини, но нет."
                                elif Girl is EmmaX:
                                        ch_e "Боюсь, что нет."
                                elif Girl is LauraX:
                                        ch_l "Ни за что."
                                elif Girl is JeanX:
                                        ch_j "Ха! Бесполезно."
                                elif Girl is StormX:
                                        ch_s "Я бы предпочла этого не делать."
                                elif Girl is JubesX:
                                        ch_v "Эм, нет, спасибо. . ."
                                elif Girl is GwenX:
                                        ch_g "Я. . . не хочу?"
                                elif Girl is BetsyX:
                                        ch_b "Я бы предпочла этого не делать. . ."
                                elif Girl is DoreenX:
                                        ch_d "Мне бы. . . не хотелось этого делать. . ."
                                elif Girl is WandaX:
                                        ch_w "Хех, нет."
                                $ Girl.RecentActions.append("no bottomless")
                                $ Girl.DailyActions.append("no bottomless")
                                return
                        elif Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6:
                            if Girl is RogueX:
                                    ch_r "Ну, ладно. . ."
                            elif Girl is KittyX:
                                    ch_k "[Girl.Like]думаю, можно. . ."
                            elif Girl is EmmaX:
                                    ch_e "Полагаю, можно. . ."
                            elif Girl is LauraX:
                                    ch_l "Хм, ладно. . ."
                            elif Girl is JeanX:
                                    ch_j "Хмм. . . можно. . ."
                            elif Girl is StormX:
                                    ch_s "Я могу это сделать. . ."
                            elif Girl is JubesX:
                                    ch_v "Нуу, это я могу. . ."
                            elif Girl is GwenX:
                                    ch_g "Ну. . . ладно. . ."
                            elif Girl is BetsyX:
                                    ch_b "Хорошо. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ну. . . ладно. . ."
                            elif Girl is WandaX:
                                    ch_w "Конечно."
                        else:
                            if Girl is EmmaX:
                                    ch_e "Конечно."
                            elif Girl is LauraX:
                                    ch_l "Хм, ладно. . ."
                            elif Girl is StormX:
                                    ch_s "Ладно."
                            else:
                                    call AnyLine(Girl,"Конечно, "+Girl.Petname+".")
                        if Girl.Panties == "swimsuit" or Girl.Panties == "saiyan leotard" or Girl.Panties == "cammy leotard" or Girl.Panties == "raven leotard":
                            #if this is Betsy, she has the swimsuit on,
#                            if Girl.Uptop:
                                    #if it's already mostly open
                                    $ Girl.Panties = 0
                                    $ Girl.Chest = 0
                                    "Она смотрит на вас, снимая купальник."
#                            else:
#                                    $ Girl.PantiesDown = 1
#                                    "She glances up at you as she moves her swimsuit aside."
                        else:
                            if Girl is KittyX:
                                $ Line = Girl.Panties_display
                                $ Girl.Panties = 0
                                if Girl.PantsNum() >= 5:
                                    "Она протягивает руку сквозь свои [get_clothing_name(Girl.Legs, vin)] и достает [Line]."
                                    "Она подмигивает вам и кидает их на пол."
                                elif Girl.HoseNum() >= 5:
                                    "Она протягивает руку сквозь свои [get_clothing_name(Girl.Hose, vin)] и достает [Line]."
                                    "Она подмигивает вам и кидает их на пол."
                                else:
                                    "С небольшой задержкой, ее [Line] падают на пол."
                            elif Girl.PantsNum() >= 6:
                                    $ Line = get_clothing_name(Girl.Panties, vin)
                                    $ Girl.Panties = 0
                                    "Она стягивает свои [get_clothing_name(Girl.Legs, vin)], а затем снимает [Line], после надевает [get_clothing_name(Girl.Legs, vin)] обратно."
                            elif Girl.HoseNum() >= 6:
                                    $ Line = get_clothing_name(Girl.Panties, vin)
                                    $ Girl.Panties = 0
                                    "Она стягивает свои [get_clothing_name(Girl.Hose, vin)], а затем снимает [Line], после надевает [get_clothing_name(Girl.Hose, vin)] обратно."
                            elif Girl is JubesX and JubesX.Acc == "shut jacket":
                                    $ Line = get_clothing_name(Girl.Panties, vin)
                                    $ Girl.Panties = 0
                                    "Она просовывает свою руку под куртку и стягивает свои [Line]."
                            elif Girl.Legs:
                                    $ Line = get_clothing_name(Girl.Panties, vin)
                                    $ Girl.Panties = 0
                                    "Она просовывает свою руку под [get_clothing_name(Girl.Legs, vin)] и стягивает [Line] down."
                            else:
                                    $ Line = get_clothing_name(Girl.Panties, vin)
                                    $ Girl.Panties = 0
                                    "Она смотрит на вас, снимая свои [Line]."
                        call Girl_First_Bottomless(Girl)

                "Я просто хочу видеть твою киску. . ." if (Girl.Panties and not Girl.PantiesDown) or (Girl.Legs and not Girl.Upskirt) or Girl.Over == "dress":
                        if Approval >= 2:
                                if Girl is LauraX:
                                        ch_l "Как скажешь."
                                else:
                                        call AnyLine(Girl,"Ладно.")
                                $ Girl.PantiesDown = 1 if Girl.Panties else 0
                                $ Girl.Upskirt = 1 if Girl.Legs else 0
                                if Girl.Legs:
                                        "Она убирает мешающую вашему взгляду ткань."
                                elif Girl.Over == "dress":
                                        "Она задирает свое платье."
                                else:
                                        "Она сдвигает свои [get_clothing_name(Girl.Panties, vin)] в сторону."
                        elif Approval >= 1 and Girl.Legs and Girl.Panties and not Girl.PantiesDown:
                                if Girl is RogueX:
                                        ch_r "Я могу показать тебе немного. . ."
                                elif Girl is KittyX:
                                        ch_k "Думаю, я могу тебе кое-что показать. . ."
                                elif Girl is EmmaX:
                                        ch_e "Я дам тебе небольшой обзор. . ."
                                elif Girl is LauraX:
                                        ch_l "Этого хватит. . ."
                                elif Girl is JeanX:
                                        ch_j "Этого должно быть достаточно, [Girl.Petname]."
                                elif Girl is StormX:
                                        ch_s "Я уже достаточно сняла. . ."
                                elif Girl is JubesX:
                                        ch_v "Думаю. . . как на счет этого. . ?"
                                elif Girl is GwenX:
                                        ch_g "Ну. . . вот тебе небольшой тизер. . ."
                                elif Girl is BetsyX:
                                        ch_b "Хм, я могла бы немного тебя подразнить. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ну. . . если немного. . ."
                                elif Girl is WandaX:
                                        ch_w "Конечно."
                                $ Girl.Upskirt = 1
                        else:
                                call AnyLine(Girl,"Нет.")
                                $ Girl.RecentActions.append("no bottomless")
                                $ Girl.DailyActions.append("no bottomless")
                                return
                        call Girl_First_Bottomless(Girl)

                "Сними [get_clothing_name(Girl.Hose, vin)]." if Girl.Hose:
                        $ Girl.FaceChange("bemused", 1)
                        if Girl.Legs:
                            call AnyLine(Girl,"Ладно, хорошо.")
                        elif Approval < 2 and not Girl.Panties and Girl.HoseNum() >= 10:
                            call NoPantiesOn(Girl)
                        elif not Approval and Girl.HoseNum() >= 6:
                            if Girl is RogueX:
                                    ch_r "Нет, спасибо, [Girl.Petname]."
                            else:
                                    call AnyLine(Girl,"Извини, "+Girl.Petname+", но нет.")
                            return
                        else:
                            if Girl is RogueX:
                                    ch_r "Конечно, [Girl.Petname]."
                            else:
                                    call AnyLine(Girl,"Хорошо, "+Girl.Petname+".")

                        if Girl is KittyX:
                            $ Line = Girl.Hose_display
                            $ Girl.Hose = 0
                            if Girl.PantsNum() >= 5:
                                "Она протягивает руку сквозь [get_clothing_name(Girl.Legs, vin)] и достает [Line]."
                                "Немного помахав ими, она кидает их на пол."
                            else:
                                "Она слегка встряхивается, и ее [Line] падают на пол."
                        elif Girl.PantsNum() >= 6:
                                $ Line = get_clothing_name(Girl.Hose, vin)
                                $ Girl.Hose = 0
                                "Она стягивает свои [get_clothing_name(Girl.Legs, vin)] и снимает [Line], затем надевает [get_clothing_name(Girl.Legs, vin)] обратно."
                        elif Girl.Legs:
                                $ Line = get_clothing_name(Girl.Hose, vin)
                                $ Girl.Hose = 0
                                "Она просовывает свою руку под свою [get_clothing_name(Girl.Legs, vin)] и стягивает [Line] вниз."
                        elif Girl.HoseNum() < 10:
                                $ Line = get_clothing_name(Girl.Hose, vin)
                                $ Girl.Hose = 0
                                "[Girl.Name] снимает [Line]."
                        elif not Girl.Panties:
                                $ Line = get_clothing_name(Girl.Hose, vin)
                                $ Girl.Hose = 0
                                $ Girl.FaceChange("sly", 2)
                                "Она краснеет и хитро смотрит на вас, пока снимает [Line]."
                                $ Girl.Blush = 1
                                call Girl_First_Bottomless(Girl)
                        elif not Girl.SeenPanties:
                                $ Line = get_clothing_name(Girl.Hose, vin)
                                $ Girl.Hose = 0
                                "[Girl.Name] стыдливо снимает [Line]."
                                $ Girl.SeenPanties = 1
                        else:
                                $ Line = get_clothing_name(Girl.Hose, vin)
                                $ Girl.Hose = 0
                                "[Girl.Name] снимает [Line]."

                "Порвать [get_clothing_name(Girl.Hose, vin)]." if Girl.Hose == "pantyhose" or Girl.Hose == "tights":
                        $ Girl.FaceChange("bemused", 1)
                        if Girl.Legs:
                            call AnyLine(Girl,"Ладно.")
                        elif Approval < 2 and not Girl.Panties and Girl.HoseNum() >= 10:
                            call NoPantiesOn(Girl)
                        elif not Approval and Girl.HoseNum() >= 6:
                            if Girl is RogueX:
                                    if not Player.Male:
                                        ch_r "[Girl.Petname], я бы предпочла, чтобы ты этого не делала."
                                    else:
                                        ch_r "[Girl.Petname], я бы предпочла, чтобы ты этого не делал."
                            else:
                                    call AnyLine(Girl,"Извини, но нет, "+Girl.Petname+".")
                            return

                        $ Line = get_clothing_name(Girl.Hose, vin)
                        if Girl.Hose == "tights":
                                $ Girl.Hose = "ripped tights"
                        elif Girl.Hose == "pantyhose":
                                $ Girl.Hose = "ripped pantyhose"
                        if Girl.Hose not in Girl.Inventory:
                                $ Girl.Inventory.append(Girl.Hose)
                        $ Girl.AddWord(1,"ripped","ripped")
                        "Вы рвете ее [Line]."
                        if not ApprovalCheck(Girl, 1200, TabM=0):
                                $ Girl.FaceChange("angry", 1,Eyes="down")
                                if Girl is RogueX:
                                        ch_r "Черт, [Girl.Petname], они же дорогие!"
                                elif Girl is KittyX:
                                        ch_k "Эй, я же носила их!"
                                elif Girl is EmmaX:
                                        ch_e "Надеюсь, ты за них заплатишь."
                                elif Girl is LauraX:
                                        ch_l "Эй. Это совсем не круто."
                                elif Girl is JeanX:
                                        ch_j "Ох, да пофиг."
                                elif Girl is StormX:
                                        if not Player.Male:
                                            ch_s "Чтобы ты знала, они взялись не из воздуха. . ."
                                        else:
                                            ch_s "Чтобы ты знал, они взялись не из воздуха. . ."
                                elif Girl is JubesX:
                                        ch_v "Эй! Лучше бы тебе найти им замену. . ."
                                elif Girl is GwenX:
                                        ch_g "Воу! Я только недавно их получила!"
                                elif Girl is BetsyX:
                                        ch_b "Что ты себе позволяешь!"
                                elif Girl is DoreenX:
                                        ch_d "Эй! Это были мои любимые. . ."
                                elif Girl is WandaX:
                                        ch_w "Они и так уже были изрядно потрепаны. . ."
                                $ Girl.FaceChange("bemused", 1)

                "Почему бы тебе не снять свитер?" if Girl.Acc == "sweater":
                            $ Girl.Acc = 0
                            "[Girl.Name] сбрасывает с себя свитер."
                "Почему бы тебе не снять шарф?" if Girl.Acc == "scarf":
                            $ Girl.Acc = 0
                            "[Girl.Name] снимает шарф."

                "Почему бы тебе не снять [get_clothing_name(Girl.Boots, vin)]?" if Girl.Boots:
                            $ Line = get_clothing_name(Girl.Boots, vin)
                            $ Girl.Boots = 0
                            "[Girl.Name] развязывает шнурки и снимает [Line]."

                "Оставь все как есть." if Cnt == 1:
                    $ Cnt = 0

                "Хорошо, пока достаточно." if Cnt == 2:
                    $ Cnt = 0

            $ Cnt = 2 if Cnt else Cnt
            $ Line = "Что-нибудь еще?"
        return


label NoPantiesOn(Girl=0):  #rkeljsvgb
        #called when asked to remove pants with nothing on under
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if not Girl.Panties:
            return

        if Girl is RogueX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_r "Знаешь, на мне ведь нет трусиков. . ."
                else:
                        ch_r "Это последнее, что есть на мне. . ."
        elif Girl is KittyX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_k "[Girl.Like]я не ношу трусики. . ."
                else:
                        ch_k "Кроме этого, на мне ничего нет. . ."
        elif Girl is EmmaX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_e "У меня под этим ничего нет. . ."
                else:
                        ch_e "Это все, что на мне есть. . ."
        elif Girl is LauraX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_l "У меня под этим ничего нет. . ."
                else:
                        ch_l "Это все, что на мне есть. . ."
        elif Girl is JeanX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_j "Сейчас на мне нет трусиков. . ."
                else:
                        ch_j ". . ."
        elif Girl is StormX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_s "Под этим на мне ничего не надето. . ."
                else:
                        ch_s "Это все, что на мне есть. . ."
        elif Girl is JubesX:
                if Girl.PantsNum() >= 5 or Girl.HoseNum() >= 10:
                        ch_v "У меня под этим ничего нет. . ."
                else:
                        ch_v "Это все, что на мне надето. . ."
        elif Girl is GwenX:
#                if Girl.PantsNum() >= 5 or Girl.HoseNum() >= 10:
#                        ch_g "I, um. . . don't have anything under these. . ."
#                else:
                        ch_g "Я, эм. . . не надела ничего под это. . ."
        elif Girl is BetsyX:
#                if Girl.PantsNum() >= 5 or Girl.HoseNum() >= 10:
#                        ch_b "I'm afraid I have nothing on under these. . ."
#                else:
                        ch_b "Боюсь, под этим на мне ничего нет. . ."
        elif Girl is DoreenX:
                ch_d "Я, эм, ничего не надела под это. . ."
        elif Girl is WandaX:
                ch_w "На мне нет трусиков. . ."
        menu:
            extend ""
            "Не могла бы ты все равно это снять?":
                if ApprovalCheck(Girl, 1000, "LI", TabM=1):
                        if Girl is RogueX:
                                ch_r "Ну, если ты меня так вежливо просишь. . . "
                        elif Girl is KittyX:
                                ch_k "Думаю[Girl.like]могу. . . "
                        elif Girl is EmmaX:
                                ch_e "Полагаю, могу. . . "
                        elif Girl is LauraX:
                                ch_l "Думаю, можно. . . "
                        elif Girl is JeanX:
                                ch_j "Ох, почему нет. . ."
                        elif Girl is StormX:
                                ch_s "Пожалуй, я могла бы. . ."
                        elif Girl is JubesX:
                                ch_v "Нууу, пожалуй. . ."
                        elif Girl is GwenX:
                                ch_g "Ладно, если ты настаиваешь. . ."
                        elif Girl is BetsyX:
                                ch_b "Можно. . ."
                        elif Girl is DoreenX:
                                ch_d "Наверное, можно. . ."
                        elif Girl is WandaX:
                                ch_w "Конечно."
                else:
                        if Girl is RogueX:
                                ch_r "Извини, но я не хочу."
                        elif Girl is KittyX:
                                ch_k "Нет, спасибо."
                        elif Girl is EmmaX:
                                ch_e "Боюсь, что нет."
                        elif Girl is LauraX:
                                ch_l "Нет, не сейчас."
                        elif Girl is JeanX:
                                ch_j "Ха! Старайся дальше, [Girl.Petname]."
                        elif Girl is StormX:
                                ch_s "Я так не думаю."
                        elif Girl is JubesX:
                                ch_v "Нее. . ."
                        elif Girl is GwenX:
                                ch_g "Я. . . скорее откажусь? . ."
                        elif Girl is BetsyX:
                                ch_b "Я бы предпочла этого не делать. . ."
                        elif Girl is DoreenX:
                                ch_d "Эм, нет. . ."
                        elif Girl is WandaX:
                                ch_w "Хех, нет."
                        call Bottoms_Off_Refused(Girl)
                        $ renpy.pop_call()
            "Меня это не волнует, снимай.":
                if ApprovalCheck(Girl, 800, "OI", TabM=1):
                        if Girl is RogueX:
                                ch_r "Ладно, как скажешь."
                        elif Girl is KittyX:
                                ch_k "Как скажешь."
                        elif Girl is EmmaX:
                                ch_e "Если ты настаиваешь."
                        elif Girl is LauraX:
                                ch_l "Ладно."
                        elif Girl is JeanX:
                                ch_j ". . ."
                        elif Girl is StormX:
                                ch_s ". . ."
                        elif Girl is JubesX:
                                ch_v "Ладно. . ."
                        elif Girl is GwenX:
                                ch_g ". . . ладно."
                        elif Girl is BetsyX:
                                ch_b "Ладно. . ."
                        elif Girl is DoreenX:
                                ch_d "Ладно. . ."
                        elif Girl is WandaX:
                                ch_w ". . . конечно, как пожелаешь."
                else:
                        call Bottoms_Off_Refused(Girl)
                        $ renpy.pop_call()

            "Хорошо, можешь не снимать.":
                $ renpy.pop_call()
        return

label Bottoms_Off_Refused(Girl=0):  #rkeljsvgb
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if Girl is RogueX:
                if "no bottomless" in Girl.RecentActions:
                        if not Player.Male:
                            ch_r "Какую часть \"нет\" ты не поняла, [Girl.Petname]?"
                        else:
                            ch_r "Какую часть \"нет\" ты не понял, [Girl.Petname]?"
                elif "no bottomless" in Girl.DailyActions:
                        ch_r "Если ты будешь продолжать мне надоедать, [Girl.Petname], то никогда не добьешься своего."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:
                            ch_r "Хватит, [Girl.Petname]. Но, мы ведь все равно повеселимся?"
                    else:
                            if not Player.Male:
                                ch_r "Боюсь, не в этот раз, [Girl.Petname]. Уверена, что мы не можем просто повеселиться?"
                            else:
                                ch_r "Боюсь, не в этот раз, [Girl.Petname]. Уверен, что мы не можем просто повеселиться?"
        elif Girl is KittyX:
                if "no bottomless" in Girl.RecentActions:
                        if not Player.Male:
                            ch_k "Ты мне уже[Girl.like]надоела."
                        else:
                            ch_k "Ты мне уже[Girl.like]надоел."
                elif "no bottomless" in Girl.DailyActions:
                        ch_k "Дай мне передохнуть."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:
                        if not Player.Male:
                            ch_k "Ты этого не заслужила, но[Girl.like]мы ведь все равно немного повеселимся?"
                        else:
                            ch_k "Ты этого не заслужил, но[Girl.like]мы ведь все равно немного повеселимся?"
                    else:
                        ch_k "Мой ответ \"нет,\" но[Girl.like]мы ведь все равно немного повеселимся?"
        elif Girl is EmmaX:
                if "no bottomless" in Girl.RecentActions:
                        ch_e "Попытайся контролировать свои порывы."
                elif "no bottomless" in Girl.DailyActions:
                        ch_e "Не сегодня."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:
                        ch_e "Я на это не готова пойти, надеюсь, это не особо важно для тебя?"
                    else:
                        ch_e "Боюсь, что нет, надеюсь, это не особо важно для тебя?"
        elif Girl is LauraX:
                if "no bottomless" in Girl.RecentActions:
                        ch_l "Успокойся уже."
                elif "no bottomless" in Girl.DailyActions:
                        ch_l "Нет, не сегодня."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:
                        ch_l "Большего ты не получишь, надеюсь, это не будет помехой?"
                    else:
                        ch_l "Неа, надеюсь, это не будет помехой?"
        elif Girl is JeanX:
                if "no bottomless" in Girl.RecentActions:
                        ch_j "Передохни уже, [Girl.Petname]."
                elif "no bottomless" in Girl.DailyActions:
                        ch_j "Я же ясно выразилась."
                else:
                        $ Girl.FaceChange("sad")
                        #if Cnt == 2:
                            #ch_j "Do we have a problem?"
                        #else:
                        ch_j "У нас какие-то проблемы?"
        elif Girl is StormX:
                if "no bottomless" in Girl.RecentActions:
                        ch_s "Прояви хоть какую-нибудь сдержанность."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:
                        ch_s "Это все, можем ли мы все равно продолжить?"
                    else:
                        ch_s "Я бы предпочла этого не делать, можем ли мы все равно продолжить?"
        elif Girl is JubesX:
                if "no bottomless" in Girl.DailyActions:
                        ch_v "Как я уже сказала, нет."
                else:
                        $ Girl.FaceChange("sad")
                        ch_v "Это все, хорошо?"
        elif Girl is GwenX:
                if "no bottomless" in Girl.DailyActions:
                        ch_g "Прекрати спрашивать."
                else:
                        $ Girl.FaceChange("sad")
                        ch_g "Нет. . . ты не против?"
                        ch_g "Мы можем продолжить?"
        elif Girl is BetsyX:
                if "no bottomless" in Girl.DailyActions:
                        ch_b "Ох, прекрати."
                else:
                        $ Girl.FaceChange("sad")
                        ch_b "Боюсь, что я против. Без этого никак?"
        elif Girl is DoreenX:
                if "no bottomless" in Girl.DailyActions:
                        ch_d "Прекрати."
                else:
                        ch_d "Я против, но мы можем повеселиться без этого?"
        elif Girl is WandaX:
                if "no bottomless" in Girl.DailyActions:
                        ch_w "Прекрати."
                else:
                        ch_w "Хех, прости. Но мы же можем продолжить, верно?"
        menu:
            extend ""
            "Хорошо, забудь мои слова." if "no bottomless" not in Girl.RecentActions:
                    $ Girl.Mouth = "smile"
                    $ Girl.Statup("Love", 70, 2)
                    $ Girl.Statup("Obed", 60, 2)
                    if Girl is RogueX:
                            ch_r "Отлично."
                    elif Girl is KittyX:
                            ch_k "Отлично!"
                    elif Girl is EmmaX:
                            ch_e "Замечательно."
                    elif Girl is LauraX:
                            ch_l "Ладно."
                    elif Girl is JeanX:
                            ch_j "Хорошо. . ."
                    elif Girl is StormX:
                            ch_s "Хорошо. . ."
                    elif Girl is JubesX:
                            ch_v "Клево."
                    elif Girl is GwenX:
                            ch_g "Отлично!"
                    elif Girl is BetsyX:
                            ch_b "Прекрасно!"
                    elif Girl is DoreenX:
                            ch_d "Спасибо!"
                    elif Girl is WandaX:
                            ch_w "Спасибо."

            "Извини, я больше не буду." if "no bottomless" in Girl.RecentActions:
                    if Girl is EmmaX:
                            ch_e "Хорошо."
                    elif Girl is LauraX:
                            ch_l "Клево."
                    else:
                            call AnyLine(Girl,"Ладно. . .")

            "Нет, давай займемся чем-нибудь другим.":
                    $ Girl.Brows = "confused"
                    if Girl is RogueX:
                            ch_r "Ну ладно, [Girl.Petname], тебе же хуже."
                    elif Girl is KittyX:
                            ch_k "Ладно[Girl.like]как хочешь."
                    elif Girl is StormX:
                            ch_s "Да будет так. . ."
                    elif Girl is JubesX:
                            ch_v "Как хочешь. . ."
                    elif Girl is GwenX:
                            ch_g "Ох. . . жаль. . ."
                    elif Girl is BetsyX:
                            ch_b "Жаль. . ."
                    else:
                            call AnyLine(Girl,"Тебе же хуже.")
                    $ Girl.Statup("Lust", 50, 5)
                    $ Girl.Statup("Love", 70, -2, 1)
                    if "no bottomless" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 60, 4)
                    $ Girl.RecentActions.append("angry")
                    $ Girl.DailyActions.append("angry")

        $ Girl.RecentActions.append("no bottomless")
        $ Girl.DailyActions.append("no bottomless")
        $ Tempmod = 0
        return


# End Bottoms Off / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Girl Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#Start Girl_First_Topless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_First_Topless(Girl=Ch_Focus,Silent=0,TempLine=0):
        #call Girl_First_Topless(RogueX,0)
        if Girl not in TotalGirls:
                return
        if Girl.ChestNum() > 1 or Girl.OverNum() > 2:
                #if she's wearing substantial clothing. . .
                return
        if Girl.Loc != bg_current and "phonesex" not in Player.RecentActions:
                return
        $ Girl.RecentActions.append("topless")
        $ Girl.DailyActions.append("topless")
        $ Girl.DrainWord("no topless")
        $ Girl.SeenChest += 1
        if Girl.SeenChest > 1 or Girl is StormX:
                return                  #ends portion if you've already seen them

        $ Girl.Statup("Inbt", 70, 15)
        if Silent:
            $ Girl.AddWord(1,0,0,0,"topless") #$ Girl.History.append("topless")
            if Girl is JeanX:
                #Jean has her own weird rules
                if (ApprovalCheck(JeanX, 800) or not Player.Male) and not JeanX.Forced:
                        #if she's not forced and happy about it
                        $ JeanX.Statup("Love", 70, 10)
                        $ JeanX.Statup("Obed", 70, 25)
                        $ JeanX.Statup("Inbt", 70, 15)
                else:
                        #if she's not happy about it
                        $ JeanX.Statup("Love", 90, -40)
                        $ JeanX.Statup("Inbt", 200, -20)
                        $ JeanX.FaceChange("angry")
                        $ JeanX.Statup("Obed", 70, 40)
            else:
                if (ApprovalCheck(Girl, 800) or not Player.Male) and not Girl.Forced:
                        #if she's not forced and happy about it
                        $ Girl.Statup("Inbt", 70, 5)
                        $ Girl.Statup("Obed", 70, 10)
                else:
                        #if she's not happy about it
                        $ Girl.Statup("Love", 90, -5)
                        $ Girl.Statup("Inbt", 70, -5)
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Obed", 70, 10)
            return

        if Girl in (EmmaX,JeanX):
                $ Girl.FaceChange("sly",1)
        else:
                $ Girl.FaceChange("bemused",2,Eyes="side")
        "Вы впервые видите обнаженную грудь [Girl.Name_rod]."

        if Girl is RogueX:
                if not Player.Male and "girltalk" not in RogueX.History:
                        ch_r "Ох, ну как, милые ведь, правда?"
                else:
                        "[RogueX.Name] немного смущается, но, все-таки, медленно опускает руки с груди."
                        ch_r "Ну как, [RogueX.Petname]? Нравится?"
        elif Girl is KittyX:
                if not Player.Male and "girltalk" not in KittyX.History:
                        ch_k "Ну как? Эм, выглядит ведь неплохо, правда?"
                else:
                        "[KittyX.Name] немного смущается, но, все-таки, медленно опускает руки с груди."
                        ch_k "[KittyX.Like]что думаешь?"
        elif Girl is EmmaX:
                if not Player.Male and "girltalk" not in EmmaX.History:
                        ch_e "Прости, дорогая, должно быть, ты слишком удивлена. . ."
                else:
                        ch_e "Как тебе, [EmmaX.Petname]? Все как ты и ожидал?"
        elif Girl is LauraX:
                        if not Player.Male:
                            ch_l "И? На что ты так уставилась?"
                        else:
                            ch_l "И? На что ты так уставился?"
        elif Girl is JeanX:
                        ch_j "Впечатляет, да?"
        elif Girl is JubesX:
                if not Player.Male and "girltalk" not in JubesX.History:
                        ch_v "Ох, эм. . . вот ты их и увидела. . ."
                else:
                        ch_v "Так. . . эм. . . тебе нравится?"
        elif Girl is GwenX:
                if not Player.Male and "girltalk" not in GwenX.History:
                        ch_g "Ох, надеюсь, они тебя не смутят. . ."
                else:
                        ch_g "Ох. . . эм. . . нравятся?"
        elif Girl is BetsyX:
                if not Player.Male and "girltalk" not in BetsyX.History:
                        ch_b "Прелестные, правда?"
                else:
                        ch_b "Итак. . . как они тебе?"
        elif Girl is DoreenX:
                if not Player.Male and "girltalk" not in Girl.History:
                        ch_d "Что думаешь?"
                else:
                        ch_d "Что ж, эм. . . как они тебе?"
        elif Girl is WandaX:
                if not Player.Male and "girltalk" not in WandaX.History:
                        ch_w "Они милые, согласна? . ."
                else:
                        ch_w "Что ж. . . вот ты их и увидел."
        $ Girl.Blush = 1
        call Shift_Focus(Girl)

label Girl_First_TMenu:
        #sometimes called from chat and other circumstances if the first time was silent
        #sets the line for you complimenting her tits
        if Ch_Focus is EmmaX:
                $ Line = "Точно, и даже больше."
        elif Ch_Focus is JeanX:
                $ Line = "Ага, они выглядят потрясающе."
        else:
                $ Line = "Твои сиськи? Они выглядят великолепно."

        #sets the line for questioning them
        if Ch_Focus is RogueX:
                $ TempLine = "Пойдет."
        elif Ch_Focus is KittyX:
                $ TempLine = "И это все?"
        else:
                if not Player.Male:
                    $ TempLine = "Хм, я ожидала совсем другого. . ."
                else:
                    $ TempLine = "Хм, я ожидал совсем другого. . ."
        menu:
            extend ""
            "[Line]":   #"Your tits? They look great.":
                    if Ch_Focus is JeanX:
                            $ JeanX.Statup("Inbt", 200, 20)
                            $ JeanX.Statup("Obed", 40, 20)
                    else:
                            $ Ch_Focus.Statup("Love", 90, 20)
                            $ Ch_Focus.Statup("Inbt", 70, 20)
                    $ Ch_Focus.FaceChange("smile",2)
                    pause 0.5
                    $ Ch_Focus.FaceChange("sexy",1,Eyes="down")
                    if Ch_Focus is RogueX:
                                ch_r ". . ."
                    elif Ch_Focus is KittyX:
                                ch_k ". . ."
                    elif Ch_Focus is EmmaX:
                                ch_e "Я знала, что произведу на тебя впечатление."
                    elif Ch_Focus is LauraX:
                                ch_l "Хм. Я так и думала. . ."
                    elif Ch_Focus is JeanX:
                                ch_j "Ага, они очень упругие. . ."
                    elif Ch_Focus is JubesX:
                                ch_v "Ах! Эм. . . ага, пожалуй. . ."
                    elif Ch_Focus is GwenX:
                                ch_g "Ха. . . пожалуй. . ."
                    elif Ch_Focus is BetsyX:
                                ch_b "Конечно."
                    elif Ch_Focus is DoreenX:
                                ch_d "Оу, спасибо!"
                    elif Ch_Focus is WandaX:
                                ch_w "Ох. . . спасибо. . ."
                    $ Ch_Focus.FaceChange("smile")
                    $ Ch_Focus.Statup("Love", 90, 10)
            #end "[Line]":   #"Your tits? They look great.":
            ". . . [[Вы ошеломлены]":
                    $ Ch_Focus.Statup("Love", 90, 10)
                    if Ch_Focus is JeanX:
                                $ JeanX.Statup("Inbt", 200, 10)
                    else:
                                $ Ch_Focus.Statup("Inbt", 70, 10)
                    if Ch_Focus is RogueX:
                                ch_r ". . ."
                    elif Ch_Focus is KittyX:
                                ch_k "Эм. . ?"
                    elif Ch_Focus is EmmaX:
                                ch_e "Да, это обычная реакция."
                    elif Ch_Focus is LauraX:
                                if not Player.Male:
                                    ch_l "Язык проглотила?"
                                else:
                                    ch_l "Язык проглотил?"
                    elif Ch_Focus is JeanX:
                                ch_j "Ты в шоке, я понимаю."
                    elif Ch_Focus is JubesX:
                                ch_v "Ох, не думала, что нанесу такой \"удар.\""
                    elif Ch_Focus is GwenX:
                                ch_g "Ты под впечатлением, да?"
                    elif Ch_Focus is BetsyX:
                                ch_b "Полагаю, я лишила тебя дара речи."
                    elif Ch_Focus is DoreenX:
                                ch_d "Они. . . странные?"
                    elif Ch_Focus is WandaX:
                                ch_w "Не можешь подобрать слов?"
                    $ Ch_Focus.Statup("Love", 40, 10)
            #end ". . . [[Вы ошеломлены]":

            "[TempLine]": #"Huh, not what I was expecting. . .":
                    if Ch_Focus is JeanX:
                                $ JeanX.Statup("Love", 90, 10)
                                $ JeanX.Statup("Obed", 40, 20)
                                $ JeanX.Statup("Inbt", 200, 20)
                                $ JeanX.FaceChange("smile",0)
                                ch_j "Имен-{w=0.3}{nw}"
                                $ JeanX.Statup("Love", 90, -40)
                                $ JeanX.Statup("Obed", 60, 10)
                                $ JeanX.Statup("Inbt", 200, -15)
                    else:
                                $ Ch_Focus.Statup("Love", 90, -30)
                                $ Ch_Focus.Statup("Obed", 60, 25)
                                $ Ch_Focus.Statup("Inbt", 70, -15)
                    $ Ch_Focus.FaceChange("confused",2)
                    if Ch_Focus is RogueX:
                                if not Player.Male:
                                    ch_r "Что ты сейчас сказала?"
                                else:
                                    ch_r "Что ты сейчас сказал?"
                    elif Ch_Focus is KittyX:
                                ch_k "Что?"
                    elif Ch_Focus is EmmaX:
                                ch_e "Что?"
                    elif Ch_Focus is LauraX:
                                ch_l "Чего?"
                    elif Ch_Focus is JeanX:
                                ch_j "Имен- подожди, что?"
                    elif Ch_Focus is JubesX:
                                ch_v "Че?"
                    elif Ch_Focus is GwenX:
                                ch_g "О, правда?"
                                if not Player.Male:
                                    ch_g "А чего именно ты ждала?"
                                else:
                                    ch_g "А чего именно ты ждал?"
                    elif Ch_Focus is BetsyX:
                                ch_b "М?"
                    elif Ch_Focus is DoreenX:
                                ch_d "Что?"
                    elif Ch_Focus is WandaX:
                                if WandaX.Lust <= 50:
                                        ch_w "О, это из-за сосков?"
                                else:
                                        ch_w "Не такие большие?"
                    if Ch_Focus is EmmaX:
                        if not Player.Male:
                            $ Line = "Они даже лучше, чем я себе представляла!"
                        else:
                            $ Line = "Они даже лучше, чем я себе представлял!"
                    else:
                        $ Line = "Они очень упругие!"
                    $ Templine = 0
                    menu:
                        "[Line]":#"They're really perky!":
                                if Ch_Focus is JeanX:
                                        $ JeanX.Statup("Love", 90, 10)
                                        $ JeanX.Statup("Obed", 60, 10)
                                        $ JeanX.Statup("Inbt", 200, 20)
                                else:
                                        $ Ch_Focus.Statup("Love", 90, 20)
                                        $ Ch_Focus.Statup("Obed", 60, -20)
                                        $ Ch_Focus.Statup("Inbt", 70, 20)
                                $ Ch_Focus.FaceChange("perplexed",1)
                                if Ch_Focus is RogueX:
                                        ch_r "Ну конечно!"
                                elif Ch_Focus is KittyX:
                                        ch_k "Пожалуй!"
                                elif Ch_Focus is EmmaX:
                                        ch_e "Что ж, я полагаю, тебе удалось спасти ситуацию. . ."
                                elif Ch_Focus is LauraX:
                                        ch_l "О. Ну да. . ."
                                elif Ch_Focus is JeanX:
                                        ch_j "О. Конечно. . ."
                                elif Ch_Focus is JubesX:
                                        ch_v "О. Точно. . ."
                                elif Ch_Focus is GwenX:
                                        ch_g "О. Угум."
                                elif Ch_Focus is BetsyX:
                                        ch_b "Ты даже не представляешь, насколько. . ."
                                elif Ch_Focus is DoreenX:
                                        ch_d "Я не уверена, что это так. . ."
                                elif Ch_Focus is WandaX:
                                        ch_w "О. Ага."
                        "Я, эм. . . они у тебя просто отличные!":
                                $ Ch_Focus.FaceChange("angry",2, Mouth="smile")
                                $ Ch_Focus.Statup("Inbt", 70, 10)
                                if Ch_Focus is RogueX:
                                        ch_r "Ну конечно!"
                                elif Ch_Focus is KittyX:
                                        ch_k "Пожалуй!"
                                elif Ch_Focus is EmmaX:
                                        ch_e "Конечно!"
                                elif Ch_Focus is LauraX:
                                        ch_l "Почему им не быть таковыми?"
                                elif Ch_Focus is JeanX:
                                        $ JeanX.Statup("Obed", 80, 20)
                                        ch_j "Конечно!"
                                elif Ch_Focus is JubesX:
                                        ch_v ". . ."
                                        if not Player.Male:
                                            ch_v "Я -знаю-, ты поэтому потерялась?"
                                        else:
                                            ch_v "Я -знаю-, ты поэтому потерялся?"
                                elif Ch_Focus is GwenX:
                                        ch_g ". . ."
                                        ch_g "Что-то я сомневаюсь в твоей искренности."
                                elif Ch_Focus is BetsyX:
                                        ch_b ". . ."
                                        ch_b "Конечно, [BetsyX.Petname]."
                                elif Ch_Focus is DoreenX:
                                        ch_d ". . ."
                                        ch_d "Наверное, [Ch_Focus.Petname]."
                                elif Ch_Focus is WandaX:
                                        ch_w ". . ."
                                        ch_w "Ты слишком обобщаешь."
                        "Ну, у [KittyX.Name_rod] они более упругие, вот и все." if Ch_Focus is not KittyX and KittyX.SeenChest:
                                $ TempLine = KittyX
                        "Ну, у [EmmaX.Name_rod] они намного больше, вот и все." if Ch_Focus is not EmmaX and EmmaX.SeenChest:
                                $ TempLine = EmmaX
                        "Ну, у [StormX.Name_rod] они намного больше, вот и все." if Ch_Focus is not StormX and StormX.SeenChest:
                                $ TempLine = StormX
                        "Ну, у [DoreenX.Name_rod] они намного больше, вот и все." if Ch_Focus is not DoreenX and DoreenX.SeenChest:
                                $ TempLine = DoreenX
                        "Мои просто лучше. . ." if Player.Male != 1:
                                $ Templine = "me"
                        "Ага, что с ними?" if Ch_Focus is WandaX and WandaX.Lust <= 50:
                                $ Templine = "nips"
                    #end response menu

                    if TempLine:
                            $ Ch_Focus.FaceChange("angry")
                            $ Ch_Focus.Mouth = "surprised"
                            if Ch_Focus is JeanX:
                                    $ JeanX.Statup("Love", 50, -10)
                                    $ JeanX.Statup("Love", 90, -10)
                                    $ JeanX.Statup("Obed", 50, 10)
                                    $ JeanX.Statup("Obed", 80, 30)
                                    $ JeanX.Statup("Inbt", 200, -15)
                            else:
                                    $ Ch_Focus.Statup("Love", 90, -10)
                                    $ Ch_Focus.Statup("Obed", 80, 30)
                                    $ Ch_Focus.Statup("Inbt", 70, -25)
                            call AnyLine(Ch_Focus,". . . {w=0.3}{nw}") #ch_d ". . ."
                            $ Ch_Focus.FaceChange("sadside")
                            if TempLine in (EmmaX,StormX,DoreenX):
                                    if Ch_Focus.GirlLikeCheck(TempLine) >= 800:
                                        $ Ch_Focus.FaceChange("sly",2,Eyes="side")
                                        $ Ch_Focus.Statup("Obed", 80, 5)
                                        if Ch_Focus is RogueX:
                                                ch_r "Ну, да, они у нее прямо необъятные. . ."
                                        elif Ch_Focus is KittyX:
                                                ch_k "Ага, в них можно утонуть. . ."
                                        elif Ch_Focus is EmmaX:
                                                ch_e "Они у нее замечательные, но. . ."
                                        elif Ch_Focus is LauraX:
                                                ch_l "Они у нее совсем огромные. . ."
                                        elif Ch_Focus is JeanX:
                                                ch_j "Ну, они у нее весьма. . . тяжелые. . ."
                                        elif Ch_Focus is JubesX:
                                                ch_v "Ну, они у нее действительно огромны. . ."
                                        elif Ch_Focus is GwenX:
                                                ch_g "Ну, их так нарисовали. . ."
                                        elif Ch_Focus is BetsyX:
                                                ch_b "Они просто великолепны. . ."
                                        elif Ch_Focus is DoreenX:
                                                ch_d "Я не думаю, что это правда так. . ."
                                        elif Ch_Focus is WandaX:
                                                ch_w "Они у нее прямо огромные. . ."
                                        $ Ch_Focus.GirlLikeUp(TempLine,20)
                                    elif Ch_Focus.GirlLikeCheck(TempLine) >= 700:
                                        $ Ch_Focus.Eyes = "side"
                                        $ Ch_Focus.Statup("Obed", 80, 5)
                                        if Ch_Focus is RogueX:
                                                ch_r "Ну, ладно, раз они тебе нравятся. . ."
                                        elif Ch_Focus is KittyX:
                                                ch_k "Ну, ладно, раз они тебе нравятся. . ."
                                        elif Ch_Focus is EmmaX:
                                                ch_e "Я в этом не уверена. . ."
                                        elif Ch_Focus is LauraX:
                                                ch_l "Думаю, это правда. . ."
                                        elif Ch_Focus is JeanX:
                                                ch_j "Ага, если тебе нравится вымя. . ."
                                                $ JeanX.GirlLikeUp(TempLine,-50)
                                        elif Ch_Focus is JubesX:
                                                ch_v "Ох. Я ей не конкурентка. . ."
                                        elif Ch_Focus is GwenX:
                                                ch_g "Я выгляжу так, будто меня привлекает энергия \"большой мамочки\"?. . ."
                                        elif Ch_Focus is BetsyX:
                                                ch_b "У всех разные вкусы. . ."
                                        elif Ch_Focus is DoreenX:
                                                ch_d "Я не думаю, что это правда так. . ."
                                        elif Ch_Focus is WandaX:
                                                ch_w "У меня не намного меньше. . ."
                                    else:
                                        $ Ch_Focus.GirlLikeUp(TempLine,-50)
                                        $ TempLine = "bad"
                            elif TempLine == KittyX:
                                    if Ch_Focus.LikeKitty >= 800:
                                        $ Ch_Focus.FaceChange("sly",2,Eyes="side")
                                        $ Ch_Focus.Statup("Obed", 80, 5)
                                        if Ch_Focus is RogueX:
                                                ch_r "Согласна, они у нее просто очаровательны.. . ."
                                        elif Ch_Focus is KittyX:
                                                ch_k "Ага, как два спелых яблочка. . . эм, то есть-"
                                        elif Ch_Focus is EmmaX:
                                                ch_e "Согласна, они у нее весьма. . . крепкие. . ."
                                        elif Ch_Focus is LauraX:
                                                ch_l "Они у нее очень. . . изящные. . ."
                                        elif Ch_Focus is JeanX:
                                                ch_j "Они у нее очень. . . милые. . ."
                                        elif Ch_Focus is JubesX:
                                                ch_v ". . . Ага, они у нее очень милые. . ."
                                        elif Ch_Focus is GwenX:
                                                ch_g ". . . они у нее ужасно очаровательны. . ."
                                        elif Ch_Focus is BetsyX:
                                                ch_b ". . . Пожалуй, что так. . ."
                                        elif Ch_Focus is DoreenX:
                                                ch_d ". . . ну, ага. . ."
                                        elif Ch_Focus is WandaX:
                                                ch_w ". . . они у нее довольно милые. . ."
                                        $ Ch_Focus.LikeKitty += 20
                                    elif Ch_Focus.LikeKitty >= 700:
                                        $ Ch_Focus.Eyes = "side"
                                        $ Ch_Focus.Statup("Obed", 80, 5)
                                        if Ch_Focus is RogueX:
                                                ch_r "Ну, да, наверное. . ."
                                        elif Ch_Focus is KittyX:
                                                ch_k "Ну[KittyX.like]наверное. . ."
                                        elif Ch_Focus is EmmaX:
                                                ch_e "Они у нее как у ребенка. . ."
                                        elif Ch_Focus is LauraX:
                                                ch_l "Они у нее довольно. . . острые. . ."
                                        elif Ch_Focus is JeanX:
                                                ch_j "Ага, если тебе нравятся доски. . ."
                                                $ JeanX.LikeKitty -= 50
                                        elif Ch_Focus is JubesX:
                                                ch_v "Да? . ."
                                        elif Ch_Focus is GwenX:
                                                ch_g "Ага. . ."
                                        elif Ch_Focus is BetsyX:
                                                ch_b "У всех разные вкусы . ."
                                        elif Ch_Focus is DoreenX:
                                                ch_d ". . . ну, ага. . ."
                                        elif Ch_Focus is WandaX:
                                                ch_w "Конечно. . ."
                                    else:
                                        $ Ch_Focus.LikeKitty -= 50
                                        $ TempLine = "bad"
                            elif TempLine == "me":
                                    $ Ch_Focus.Statup("Obed", 80, 5)
                                    if Ch_Focus is JeanX:
                                            $ JeanX.Statup("Obed", 80, 5)
                                    if ApprovalCheck(Ch_Focus, 800):
                                        $ Ch_Focus.FaceChange("sly",2,Eyes="side")
                                        $ Ch_Focus.Statup("Obed", 70, 5)
                                        if Ch_Focus is RogueX:
                                                ch_r "Ну, спорить с тобой не буду. . ."
                                        elif Ch_Focus is KittyX:
                                                ch_k "[KittyX.Like]наверное. . ."
                                        elif Ch_Focus is EmmaX:
                                                ch_e "Они у тебя прекрасны, но. . ."
                                        elif Ch_Focus is LauraX:
                                                ch_l "Ну, как скажешь. . ."
                                        elif Ch_Focus is JeanX:
                                                ch_j ". . . ну. . . они у тебя неплохие. . ."
                                                $ JeanX.Statup("Obed", 70, 5)
                                        elif Ch_Focus is JubesX:
                                                ch_v ". . . Думаю, они у тебя очень милые. . ."
                                        elif Ch_Focus is GwenX:
                                                ch_g ". . . Ладно, справедливо. . ."
                                        elif Ch_Focus is BetsyX:
                                                ch_b ". . . Полагаю, я не могу с этим поспорить. . ."
                                        elif Ch_Focus is DoreenX:
                                                ch_d ". . . Думаю, я не могу с этим поспорить. . ."
                                        elif Ch_Focus is WandaX:
                                                ch_w ". . . Они у тебя довольно неплохие. . ."
                                    else:
                                        $ TempLine = "bad"
                            elif TempLine == "nips":
                                    $ WandaX.Statup("Obed", 80, 5)
                                    $ WandaX.FaceChange("sadside",2)
                                    ch_w ". . . они постоянно прячутся. . ."
                                    if ApprovalCheck(WandaX, 700):
                                        $ WandaX.FaceChange("sly",2,Eyes="side")
                                        $ WandaX.Statup("Obed", 70, 5)
                                        ch_w ". . . наверное, они у меня застенчивые. . ."
                                    else:
                                        $ WandaX.Statup("Love", 90, -5)
                                        $ TempLine = "bad"

                            if TempLine == "bad":
                                    $ Ch_Focus.Statup("Love", 90, -20)
                                    if Ch_Focus is RogueX:
                                            ch_r "Ну и ладно, хватит с тебя моих сисек, [RogueX.Petname]."
                                    elif Ch_Focus is KittyX:
                                            if not Player.Male:
                                                ch_k "Все настроение мне испортила."
                                            else:
                                                ch_k "Все настроение мне испортил."
                                    elif Ch_Focus is EmmaX:
                                            if not Player.Male:
                                                ch_e "Что ж, полагаю, ты уже достаточно насмотрелась, [EmmaX.Petname]."
                                            else:
                                                ch_e "Что ж, полагаю, ты уже достаточно насмотрелся, [EmmaX.Petname]."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Знаешь, это довольно грубо."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Вот можешь ты все испортить!"
                                    elif Ch_Focus is JubesX:
                                            ch_v "Нельзя так просто -говорить- что-то типа этого!"
                                    elif Ch_Focus is GwenX:
                                            if not Player.Male:
                                                ch_g "Но все же, почему ты так -сказала-?"
                                            else:
                                                ch_g "Но все же, почему ты так -сказал-?"
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Это было довольно бестактно с твоей стороны."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Тем не менее, невежливо поднимать такую тему."
                                    elif Ch_Focus is WandaX:
                                            if not Player.Male:
                                                ch_w "Могла бы проявить и побольше поддержки."
                                            else:
                                                ch_w "Мог бы проявить и побольше поддержки."
                                    $ Ch_Focus.OutfitChange()
                                    $ Ch_Focus.RecentActions.append("no topless")
                                    $ Ch_Focus.DailyActions.append("no topless")
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                    #end if you said another girl was better
            #end "Huh, not what I was expecting. . .":
            ". . . [[без комментариев]":
                    $ Ch_Focus.FaceChange("angry",1)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    $ Ch_Focus.Statup("Obed", 70, 12)
                    if Player.Male:
                            $ Ch_Focus.Statup("Love", 90, -3)
                    $ JeanX.FaceChange("angry",1)
                    $ JeanX.Statup("Inbt", 60, 10)
                    $ JeanX.Statup("Obed", 70, 15)
                    if Player.Male:
                            $ JeanX.Statup("Love", 90, -10)
                    else:
                            $ JeanX.Statup("Love", 90, -5)
        $ Line = 0
        return
#End Girl_First_Topless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Girl_First_Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_First_Bottomless(Girl=Ch_Focus,Silent = 0):
        if Girl not in TotalGirls:
                return
        if Girl.PantiesNum() > 1 or Girl.PantsNum() > 2 or Girl.HoseNum() > 9:
                #if she's wearing substantial clothing. . .
                return
        if Girl.Loc != bg_current and "phonesex" not in Player.RecentActions:
                return
        $ Girl.RecentActions.append("bottomless")
        $ Girl.DailyActions.append("bottomless")
        $ Girl.DrainWord("no bottomless")
        $ Girl.SeenPussy += 1
        if Girl.SeenPussy > 1 or Girl is StormX:
                return                  #ends portion if you've already seen them

        $ Girl.Statup("Inbt", 80, 30)
        $ Girl.Statup("Obed", 70, 10)
        if Silent:
            $ Girl.AddWord(1,0,0,0,"bottomless") #$ Girl.History.append("bottomless")
            if Girl is JeanX:
                    if (ApprovalCheck(JeanX, 800) or not Player.Male) and not JeanX.Forced:
                            $ JeanX.Statup("Inbt", 60, 5)
                            $ JeanX.Statup("Obed", 90, 10)
                    else:
                            $ JeanX.Statup("Love", 90, -5)
                            $ JeanX.Statup("Inbt", 200, -5)
                            $ JeanX.FaceChange("angry")
                            $ JeanX.Statup("Obed", 90, 15)
            else:
                    if (ApprovalCheck(Girl, 800) or not Player.Male) and not Girl.Forced:
                            $ Girl.Statup("Inbt", 60, 5)
                            $ Girl.Statup("Obed", 70, 10)
                    else:
                            $ Girl.Statup("Love", 90, -5)
                            $ Girl.Statup("Inbt", 70, -5)
                            $ Girl.FaceChange("angry")
                            $ Girl.Statup("Obed", 70, 15)
            return

        call Shift_Focus(Girl)
        $ Girl.FaceChange("sly")

        if Girl is RogueX:
            if not Player.Male and "girltalk" not in RogueX.History:
                "Вы ловите себя на том, что пялитесь на ее голую киску."
                ch_r "Ох, она у меня аккуратная, согласна?"
            else:
                "[RogueX.Name] робко убирает свои руки в сторону, обнажая свою киску."
                ch_r "Ну как, [RogueX.Petname]? Она оправдала твои ожидания?"
        elif Girl is KittyX:
            if not Player.Male and "girltalk" not in KittyX.History:
                "Вы ловите себя на том, что пялитесь на ее голую киску."
            else:
                "[KittyX.Name] робко убирает свои руки в сторону, обнажая свою киску."
        elif Girl is LauraX and LauraX.Pubes:
                "Вы уставились на мохнатую киску [LauraX.Name_rod]."
        elif Girl.Pubes:
                "Вы ловите себя на том, что пялитесь на мохнатую киску [Girl.Name_rod]."
        else:
                "Вы ловите себя на том, что пялитесь на ее голую [Girl.Name_rod]."

label Girl_First_BMenu:
        #sets first line about the state of her pubes
        if not Ch_Focus.Pubes:
                $ Line = "Я вижу, у тебя там все гладко."
        elif Ch_Focus is JeanX:
                $ Line = "Смотрю, у тебя там словно бушует пламя."
        elif Ch_Focus is KittyX:
                $ Line = "Как-то там у тебя все неопрятно."
        else:
                $ Line = "Смотрю, у тебя там все так естественно."

        #sets second, rude line about the state of her pubes
        if Ch_Focus is JeanX:
            if not Player.Male:
                $ TempLine = "Я видала и получше"
            else:
                $ TempLine = "Я видал и получше"
        elif Ch_Focus is EmmaX:
            $ TempLine = "Неплохо для твоего возраста."
        else:
            $ TempLine = "Как же у тебя там все неопрятно."
        menu:
            extend ""
            "Какая милая. . .":
                    $ Ch_Focus.Statup("Love", 90, 20)
                    if Ch_Focus is JeanX:
                            $ JeanX.Statup("Inbt", 200, 25)
                    else:
                            $ Ch_Focus.Statup("Inbt", 60, 25)
                    $ Ch_Focus.FaceChange("surprised",2)
                    if Ch_Focus is RogueX:
                            ch_r ". . ."
                    elif Ch_Focus is KittyX:
                            ch_k ". . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Я в курсе. . . "
                    elif Ch_Focus is LauraX:
                            ch_l "Думаешь?"
                            ch_l "Мне она тоже нравится. . . "
                    elif Ch_Focus is JeanX:
                            $ JeanX.FaceChange("smile")
                            ch_j "Правда?"
                    elif Ch_Focus is JubesX:
                            ch_v "!!"
                            $ JubesX.FaceChange("smile",1)
                            ch_v "Ох, эм, ага, я. . . тоже так думаю. . . "
                    elif Ch_Focus is GwenX:
                            ch_g "!!!"
                            $ GwenX.FaceChange("smile",1)
                            ch_g "Эм. . . ладно. . . "
                    elif Ch_Focus is BetsyX:
                            ch_b "!!"
                            $ BetsyX.FaceChange("smile",1)
                            ch_b "Ох, эм, твоя правда. . . "
                    elif Ch_Focus is DoreenX:
                            ch_d "!!"
                            $ Ch_Focus.FaceChange("smile",1)
                            ch_d "Ну. . . наверное. . . "
                    elif Ch_Focus is WandaX:
                            ch_w "!!!"
                            $ WandaX.FaceChange("smile",1)
                            ch_w "Хех. . . спасибо? . . "
                    $ Ch_Focus.Statup("Love", 40, 20)

            "Именно -такую- \"Китти[[Прим. также Китти- киска, кошечка и т.д.]\" я хотела увидеть." if Ch_Focus is KittyX and not Player.Male:
                    $ KittyX.Statup("Love", 40, 25)
                    $ KittyX.Statup("Inbt", 60, 30)
                    $ KittyX.FaceChange("perplexed", 2)
                    ch_k "[фыркает]"
                    $ KittyX.Statup("Love", 90, 25)
                    $ KittyX.Blush = 1

            "Именно -такую- \"Китти[[Прим. также Китти- киска, кошечка и т.д.]\" я хотела увидеть." if Ch_Focus is KittyX and Player.Male:
                    $ KittyX.Statup("Love", 40, 25)
                    $ KittyX.Statup("Inbt", 60, 30)
                    $ KittyX.FaceChange("perplexed", 2)
                    ch_k "[фыркает]"
                    $ KittyX.Statup("Love", 90, 25)
                    $ KittyX.Blush = 1

            "[Line]" if Ch_Focus.Pubes: #"I see you keep it natural down there."
                $ Ch_Focus.FaceChange("confused",2)
                if Ch_Focus is RogueX:
                        ch_r "Ага."
                elif Ch_Focus is KittyX:
                        ch_k "!!!"
                elif Ch_Focus is EmmaX:
                        ch_e "Да?"
                elif Ch_Focus is LauraX:
                        ch_l "Ну. . . да."
                elif Ch_Focus is JeanX:
                        ch_j "Ну. . . да."
                elif Ch_Focus is JubesX:
                        ch_v "Ну. . . да."
                elif Ch_Focus is GwenX:
                        ch_g "Эм. . . да."
                elif Ch_Focus is BetsyX:
                        ch_b "Да."
                elif Ch_Focus is DoreenX:
                        ch_d "Ага, наверное."
                elif Ch_Focus is WandaX:
                        ch_w "Ага?"
                if ApprovalCheck(Ch_Focus, 700, "LO"):
                    $ Ch_Focus.FaceChange("bemused",1)
                    if Ch_Focus is RogueX:
                            ch_r "Тебе нравится, когда там гладко?"
                    elif Ch_Focus is KittyX:
                            pass
                    elif Ch_Focus is EmmaX:
                            ch_e "Ты предпочитаешь более пушистые?"
                    elif Ch_Focus is LauraX:
                            ch_l "Думаешь, стоит побрить?"
                    elif Ch_Focus is JeanX:
                            ch_j "Тебе нравится, когда все гладко?"
                    elif Ch_Focus is JubesX:
                            ch_v "Ты. . . предпочитаешь бритые?"
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе. . . нравятся бритые?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Ты предпочитаешь побритые?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Разве это плохо?"
                    elif Ch_Focus is WandaX:
                            ch_w "Что, ты предпочитаешь бритые?"
                    menu:
                        extend ""
                        "Да":
                            if ApprovalCheck(Ch_Focus, 900, "LO"):
                                    if Ch_Focus is JeanX:
                                            $ JeanX.Statup("Obed", 90, 30)
                                            $ JeanX.Statup("Inbt", 200, 25)
                                    else:
                                            $ Ch_Focus.Statup("Obed", 50, 30)
                                            $ Ch_Focus.Statup("Inbt", 60, 25)
                                    if Ch_Focus is RogueX:
                                            ch_r "Ну, тогда я могу привести ее в порядок."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Ну, думаю, это можно исправить. . ."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Полагаю, это можно исправить. . ."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Наверное, это можно устроить. . ."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Мммм, могу все устроить. . ."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Думаю, можно это устроить. . ."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Хорошо. . ."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Что ж, если тебе больше нравятся такие. . ."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "О, хорошо, я все обдумаю. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Хех. . . я могу попробовать все устроить. . ."
                                    if Ch_Focus.Pubes:
                                            $ Ch_Focus.Todo.append("shave")
                                    else:
                                            $ Ch_Focus.Todo.append("pubes")
                            else:
                                    $ Ch_Focus.FaceChange("normal")
                                    if Ch_Focus is RogueX:
                                            ch_r "Боюсь, тебе придется довольствоваться тем, что есть."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Ну[KittyX.like]извини, что там все не как у младенца!"
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Что ж, жаль."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Похоже на пустую трату времени."
                                            ch_l "Ты хоть представляешь, насколько быстро растут мои волосы?"
                                    elif Ch_Focus is JeanX:
                                            ch_j "Это слишком хлопотно."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Я даже не знаю, мне кажется, это очень хлопотно."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Мне всегда казалось, что это очень хлопотно."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Мне довольно сложно постоянно следить за ней."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Мне нравится, когда она немного пушистая."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Это требует слишком большого ухода."
                        #end "Yes" (change it)
                        "Оставлю это, пожалуй, на твое усмотрение.":
                                    $ Ch_Focus.Statup("Love", 80, 10)
                                    if Ch_Focus is RogueX:
                                            ch_r "Конечно."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Ну[KittyX.like]тогда ладно. . ."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Я рада."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Да, думаю, слишком трудно поддерживать там все гладким."
                                    elif Ch_Focus is JeanX:
                                            $ JeanX.Statup("Love", 80, 10)
                                            ch_j "Конечно."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Ну, ладно?"
                                    elif Ch_Focus is GwenX:
                                            ch_g ". . . спасибо?"
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Конечно."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Точно."
                                    elif Ch_Focus is WandaX:
                                            ch_w ". . . да?"
                                    if ApprovalCheck(Ch_Focus, 900, "LO"):
                                            $ Ch_Focus.Statup("Inbt", 60, 10)
                                            if Ch_Focus.Pubes:
                                                    $ Ch_Focus.Todo.append("shave")
                                            else:
                                                    $ Ch_Focus.Todo.append("pubes")
                        #end "Up to you, I guess.":
                        "Нет, оставь все как есть.":
                                    if ApprovalCheck(Ch_Focus, 900, "LO"):
                                            #She likes that answer
                                            $ Ch_Focus.FaceChange("sly")
                                            $ Ch_Focus.Statup("Love", 80, 10)
                                            if Ch_Focus is RogueX:
                                                    ch_r "Я очень это ценю, [Ch_Focus.Petname]."
                                            elif Ch_Focus is KittyX:
                                                    ch_k "Ну[KittyX.like]тогда ладно. . ."
                                            elif Ch_Focus is EmmaX:
                                                    ch_e "Я рада, что у меня есть твое. . . разрешение."
                                            elif Ch_Focus is LauraX:
                                                    ch_l "Ага."
                                            elif Ch_Focus is JeanX:
                                                    ch_j "Конечно."
                                            elif Ch_Focus is JubesX:
                                                    ch_v "О, эм, хорошо?"
                                            elif Ch_Focus is GwenX:
                                                    ch_g "Думаю, мне следует подыграть тебе. . ."
                                            elif Ch_Focus is BetsyX:
                                                    ch_b "Значит, у меня есть твое одобрение?"
                                            elif Ch_Focus is DoreenX:
                                                    ch_d "Рада, что ты одобряешь."
                                            elif Ch_Focus is WandaX:
                                                    ch_w ". . . ладно?"
                                    else:
                                            #She's still mad
                                            $ Ch_Focus.FaceChange("angry",Mouth="normal")
                                            if Ch_Focus is RogueX:
                                                    ch_r "Ты правда думаешь, что твое слово имеет вес?"
                                            elif Ch_Focus is KittyX:
                                                    ch_k "Ну[KittyX.like]тогда, возможно, придется ее побрить. . ."
                                            elif Ch_Focus is EmmaX:
                                                    ch_e "Я рада, что у меня есть твое. . . разрешение."
                                            elif Ch_Focus is LauraX:
                                                    ch_l "Ага."
                                            elif Ch_Focus is JeanX:
                                                    ch_j "Конечно."
                                            elif Ch_Focus is JubesX:
                                                    ch_v "О, думаешь, твое слово имеет вес?"
                                            elif Ch_Focus is GwenX:
                                                    ch_g "Мне разве нужно твое согласие?"
                                            elif Ch_Focus is BetsyX:
                                                    ch_b "Думаешь, мне нужно было твое согласие?"
                                            elif Ch_Focus is DoreenX:
                                                    ch_d "Рада, что ты одобряешь."
                                            elif Ch_Focus is WandaX:
                                                    ch_w "Думаешь, мне есть дело до твоих слов?"
                                    $ Ch_Focus.Statup("Inbt", 60, 25)
                                    $ Ch_Focus.Brows = "normal"
                        #end "No, leave it that way.":
                else:
                                    #if not ApprovalCheck(Ch_Focus, 700, "LO"), she doesn't care what you want
                                    $ Ch_Focus.FaceChange("angry",1)
                                    $ Ch_Focus.Statup("Love", 40, -20)
                                    if Ch_Focus is JeanX:
                                            $ JeanX.Statup("Obed", 90, 25)
                                            $ JeanX.Statup("Inbt", 200, -5)
                                    else:
                                            $ Ch_Focus.Statup("Obed", 50, 25)
                                            $ Ch_Focus.Statup("Inbt", 60, -5)
                                    if Ch_Focus is RogueX:
                                            ch_r "Почему меня должно волновать твое мнение?"
                                    elif Ch_Focus is KittyX:
                                            ch_k "Мне[KittyX.like]все равно, что ты думаешь!"
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Да, мне нравится ухоженный \"сад\"."
                                    elif Ch_Focus is LauraX:
                                            ch_l "А что мне еще, по твоему, остается делать?"
                                    elif Ch_Focus is JeanX:
                                            $ JeanX.FaceChange("angry",1)
                                            ch_j "Мне очень не хочется делать эпиляцию."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Ну, конечно!"
                                    elif Ch_Focus is GwenX:
                                            ch_g "Это тебя никак не касается!"
                                    elif Ch_Focus is BetsyX:
                                            ch_b "-мне кажется, это тебя не касается."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "-не думаю, что это твое дело."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Я не хочу это обсуждать."
            #end "I see you keep it natural down there."

            "[TempLine]":# "What a mess.":
                    $ Ch_Focus.Statup("Love", 90, -30)
                    if Ch_Focus is JeanX:
                            $ JeanX.Statup("Obed", 90, 25)
                            $ JeanX.Statup("Inbt", 200, -30)
                    else:
                            $ Ch_Focus.Statup("Obed", 50, 25)
                            $ Ch_Focus.Statup("Inbt", 70, -30)
                    $ Ch_Focus.FaceChange("angry",2)
                    if not Ch_Focus.Forced and not ApprovalCheck(Ch_Focus, 900, "LO"):
                            $ Ch_Focus.RecentActions.append("angry")
                            $ Ch_Focus.DailyActions.append("angry")
                            $ Ch_Focus.Statup("Obed", 80, 25)
                    if Ch_Focus is RogueX:
                            ch_r "О, сейчас кое-кто получит взбучку!"
                    elif Ch_Focus is KittyX:
                            ch_k ". . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Ты еще пожалеешь об этом замечании. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Я покажу тебе \"неопрятно\". . ."
                    elif Ch_Focus is JeanX:
                        if JeanX.Pubes:
                            ch_j "О, не так по-детски гладко, как у [EmmaX.Name_rod]?"
                        else:
                            ch_j "О, не такая запущенная, как у [LauraX.Name_rod]?"
                    elif Ch_Focus is JubesX:
                            ch_v "Ох, какие дерзкие слова. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Ну извини!"
                    elif Ch_Focus is BetsyX:
                            ch_b "\"неопрятно?!\""
                            ch_b "Как грубо!"
                    elif Ch_Focus is DoreenX:
                            ch_d "Серьезно?"
                            ch_d "Как можно говорить что-то подобное?!"
                    elif Ch_Focus is WandaX:
                            if not Player.Male:
                                ch_w "Да пошла ты!"
                            else:
                                ch_w "Да пошел ты!"
            #end "What a mess.":

            ". . . [[без комментариев]":
                    if Ch_Focus is JeanX:
                        $ JeanX.FaceChange("angry",1)
                        $ JeanX.Statup("Inbt", 60, 7)
                        $ JeanX.Statup("Obed", 70, 12)
                    else:
                        $ Ch_Focus.Statup("Inbt", 60, 5)
                        $ Ch_Focus.Statup("Obed", 70, 10)
                    if Player.Male:
                            $ Ch_Focus.Statup("Love", 90, -2)
        #end Girl_First_BMenu

        $ Line = 0
        $ TempLine = 0
        return
#End Girl_First_Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start First Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Rogue Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_First_Topless(Silent = 0, TempLine=0): #rkeljsvg
    if RogueX.ChestNum() > 1 or RogueX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return
    if RogueX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ RogueX.RecentActions.append("topless")
    $ RogueX.DailyActions.append("topless")
    $ RogueX.DrainWord("no topless")
    $ RogueX.SeenChest += 1
    if RogueX.SeenChest > 1:
            return                  #ends portion if you've already seen them

    $ RogueX.Statup("Inbt", 70, 20)
    if not Silent:
        $ RogueX.FaceChange("bemused", 1)
        if not Player.Male and "girltalk" not in RogueX.History:
                ch_r "Ох, ну как, милые ведь, правда?"
        else:
                "[RogueX.Name] немного смущается, но, все-таки, медленно опускает руки с груди."
                ch_r "Ну как, [RogueX.Petname]? Нравится?"
        menu Rogue_First_TMenu:
            extend ""
            "(Кивнуть)":
                    $ RogueX.Statup("Love", 90, 20)
                    $ RogueX.Statup("Inbt", 70, 20)
                    $ RogueX.FaceChange("smile")
                    ch_r ". . ."
                    $ RogueX.Statup("Love", 40, 20)
            "Сойдет.":
                    $ RogueX.Statup("Love", 90, -30)
                    $ RogueX.Statup("Obed", 50, 20)
                    $ RogueX.Statup("Inbt", 70, -10)
                    $ RogueX.FaceChange("angry")
                    ch_r "Пфф!"
                    $ RogueX.Statup("Obed", 70, 20)
            "Ну, они не такие уж и плохие. . .":
                    $ RogueX.Statup("Love", 90, -30)
                    $ RogueX.Statup("Obed", 60, 25)
                    $ RogueX.Statup("Inbt", 70, -15)
                    $ RogueX.FaceChange("confused",2)
                    ch_r "Say what now?"
                    menu:
                        "Я. . . эм. . . нет, они великолепны!":
                                $ RogueX.FaceChange("angry",2, Mouth="smile")
                                $ RogueX.Statup("Inbt", 70, 10)
                                ch_r "Еще бы!"
                        "Ну, у [EmmaX.Name_rod] они больше, вот и все." if EmmaX.SeenChest:
                                $ TempLine = EmmaX
                        "Ну, у [StormX.Name_rod] они больше, вот и все." if StormX.SeenChest:
                                $ TempLine = StormX
                        "Ну, у [KittyX.Name_rod] они более упругие, вот и все." if KittyX.SeenChest:
                                $ TempLine = KittyX
                        "Мои просто лучше. . ." if Player.Male != 1:
                                $ Templine = "me"

                    if TempLine:
                            $ RogueX.FaceChange("angry")
                            $ RogueX.Mouth = "surprised"
                            $ RogueX.Statup("Love", 90, -10)
                            $ RogueX.Statup("Obed", 80, 30)
                            $ RogueX.Statup("Inbt", 70, -25)
                            ch_r ". . ."
                            $ RogueX.Mouth = "sad"
                            if TempLine in (EmmaX,StormX):
                                    if RogueX.GirlLikeCheck(TempLine) >= 800:
                                            $ RogueX.FaceChange("sly",2,Eyes="side")
                                            $ RogueX.Statup("Obed", 80, 5)
                                            ch_r "Ну, да, они у нее прямо необъятные. . ."
                                            $ RogueX.GirlLikeUp(TempLine,20) # +20
                                    elif RogueX.GirlLikeCheck(TempLine) >= 700:
                                            $ RogueX.Eyes = "side"
                                            $ RogueX.Statup("Obed", 80, 5)
                                            ch_r "Ну, ладно, раз они тебе нравятся. . ."
                                    else:
                                            $ RogueX.GirlLikeUp(TempLine,-50) # +20
                                            $ TempLine = "bad"
                            elif TempLine == KittyX:
                                    if RogueX.LikeKitty >= 800:
                                            $ RogueX.FaceChange("sly",2,Eyes="side")
                                            $ RogueX.Statup("Obed", 80, 5)
                                            ch_r "Ага, они у нее такие очаровательные. . ."
                                            $ RogueX.LikeKitty += 20
                                    elif RogueX.LikeKitty >= 700:
                                            $ RogueX.Eyes = "side"
                                            $ RogueX.Statup("Obed", 80, 5)
                                            ch_r "Ну, да, наверное. . ."
                                    else:
                                            $ RogueX.LikeKitty -= 50
                                            $ TempLine = "bad"
                            elif TempLine == "me":
                                    $ RogueX.Statup("Obed", 80, 5)
                                    if ApprovalCheck(RogueX, 800):
                                        $ RogueX.FaceChange("sly",2,Eyes="side")
                                        $ RogueX.Statup("Obed", 70, 5)
                                        ch_r "Ну, спорить с тобой не буду. . ."
                                    else:
                                        $ TempLine = "bad"

                            if TempLine == "bad":
                                            $ RogueX.Statup("Love", 90, -20)
                                            ch_r "Ну и ладно, хватит с тебя моих сисек, [RogueX.Petname]."
                                            $ RogueX.OutfitChange()
                                            $ RogueX.RecentActions.append("no topless")
                                            $ RogueX.DailyActions.append("no topless")
                                            $ RogueX.RecentActions.append("angry")
                                            $ RogueX.DailyActions.append("angry")
            ". . . [[без комментариев]":
                    $ RogueX.FaceChange("sadside",1)
                    $ RogueX.Statup("Inbt", 60, 5)
                    $ RogueX.Statup("Obed", 70, 10)
                    if Player.Male:
                            $ RogueX.Statup("Love", 90, -10)
                    else:
                            $ RogueX.Statup("Love", 90, -5)
    else:
        $ RogueX.AddWord(1,0,0,0,"topless") #$ RogueX.History.append("topless")
        if (ApprovalCheck(RogueX, 800) or not Player.Male) and not RogueX.Forced:
                $ RogueX.Statup("Inbt", 70, 5)
                $ RogueX.Statup("Obed", 70, 5)
        else:
                $ RogueX.Statup("Love", 90, -5)
                $ RogueX.Statup("Inbt", 70, -5)
                $ RogueX.FaceChange("angry")
                $ RogueX.Statup("Obed", 70, 15)
    return


label Rogue_First_Bottomless(Silent = 0): #rkeljsvgb
    if RogueX.PantiesNum() > 1 or RogueX.PantsNum() > 2 or RogueX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if RogueX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ RogueX.RecentActions.append("bottomless")
    $ RogueX.DailyActions.append("bottomless")
    $ RogueX.DrainWord("no bottomless")
    $ RogueX.SeenPussy += 1
    if RogueX.SeenPussy > 1:
            #ends portion if you've already seen them
            return

    $ RogueX.Statup("Inbt", 80, 40)
    if not Silent:
        $ RogueX.FaceChange("bemused", 1)
        if not Player.Male and "girltalk" not in RogueX.History:
                "Вы ловите себя на том, что пялитесь на голую киску [RogueX.Name_rod]."
                ch_r "Ох, она у меня аккуратная, согласна?"
        else:
                "[RogueX.Name] робко убирает свои руки в сторону, обнажая свою киску."
                ch_r "Ну как, [RogueX.Petname]? Она оправдала твои ожидания?"
        menu Rogue_First_BMenu:
            extend ""
            "Она чудесная. . .":
                    $ RogueX.Statup("Love", 90, 20)
                    $ RogueX.Statup("Inbt", 60, 30)
                    $ RogueX.FaceChange("smile")
                    ch_r ". . ."
                    $ RogueX.Statup("Love", 40, 20)
            "Ну, вроде как.":
                    $ RogueX.Statup("Love", 90, -30)
                    $ RogueX.Statup("Obed", 50, 20)
                    $ RogueX.Statup("Inbt", 70, -20)
                    $ RogueX.FaceChange("angry")
                    ch_r ". . ."
                    $ RogueX.Statup("Obed", 70, 30)
            ". . . [[без комментариев]":
                    $ RogueX.FaceChange("sadside",1)
                    $ RogueX.Statup("Inbt", 60, 5)
                    $ RogueX.Statup("Obed", 70, 10)
                    if Player.Male:
                            $ RogueX.Statup("Love", 90, -10)
                    else:
                            $ RogueX.Statup("Love", 90, -5)
    else:
            $ RogueX.AddWord(1,0,0,0,"bottomless") #$ RogueX.History.append("bottomless")
            if (ApprovalCheck(RogueX, 500) or not Player.Male) and not RogueX.Forced:
                    $ RogueX.Statup("Inbt", 60, 30)
            else:
                    $ RogueX.Statup("Love", 90, -5)
                    $ RogueX.Statup("Inbt", 70, -5)
                    $ RogueX.FaceChange("angry")
                    $ RogueX.Statup("Obed", 70, 15)
    return

# Kitty Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Kitty_First_Topless(Silent = 0, TempLine = 0):
    if KittyX.ChestNum() > 1 or KittyX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return
    if KittyX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ KittyX.RecentActions.append("topless")
    $ KittyX.DailyActions.append("topless")
    $ KittyX.DrainWord("no topless")
    $ KittyX.SeenChest += 1
    if KittyX.SeenChest > 1:
            return                  #ends portion if you've already seen them


    $ KittyX.Statup("Inbt", 70, 15)
    if not Silent:
        $ KittyX.FaceChange("bemused", 2)
        if not Player.Male and "girltalk" not in KittyX.History:
                ch_k "Ну как? Эм, выглядит ведь неплохо, правда?"
        else:
                "[KittyX.Name] немного смущается, но, все-таки, медленно опускает руки с груди."
                ch_k "[KittyX.Like]что думаешь?"
        $ KittyX.Blush = 1
        menu Kitty_First_TMenu:
            extend ""
            "Они прекрасны.":
                $ KittyX.Statup("Love", 90, 20)
                $ KittyX.Statup("Inbt", 70, 20)
                $ KittyX.FaceChange("smile",2)
                ch_k ". . ."
                $ KittyX.Statup("Love", 40, 20)
                $ KittyX.Blush = 1

            "И это все?":
                    $ KittyX.Statup("Love", 90, -30)
                    $ KittyX.Statup("Obed", 60, 25)
                    $ KittyX.Statup("Inbt", 70, -15)
                    $ KittyX.FaceChange("confused",2)
                    ch_k "Что?"
                    menu:
                        "Я. . . эм. . . нет, они великолепны!":
                            $ KittyX.FaceChange("angry",2, Mouth="smile")
                            $ KittyX.Statup("Inbt", 70, 10)
                            ch_k "Obviously!"
                        "Ну, у [EmmaX.Name_rod] они больше, вот и все." if EmmaX.SeenChest:
                                $ TempLine = EmmaX
                        "Ну, у [RogueX.Name_rod] они больше, вот и все." if RogueX.SeenChest:
                                $ TempLine = RogueX
                        "Ну, у [LauraX.Name_rod] они больше, вот и все." if LauraX.SeenChest:
                                $ TempLine = LauraX
                        "Ну, у [JeanX.Name_rod] они больше, вот и все." if JeanX.SeenChest:
                                $ TempLine = JeanX
                        "Ну, у [StormX.Name_rod] они больше, вот и все." if StormX.SeenChest:
                                $ TempLine = StormX
                        "Мои просто лучше. . ." if Player.Male != 1:
                                $ Templine = "me"

                    if TempLine:
                            $ KittyX.FaceChange("angry")
                            $ KittyX.Mouth = "surprised"
                            $ KittyX.Statup("Love", 90, -10)
                            $ KittyX.Statup("Obed", 80, 30)
                            $ KittyX.Statup("Inbt", 70, -25)
                            ch_k ". . ."
                            $ KittyX.Mouth = "sad"
                            if TempLine in (EmmaX,StormX):
                                    if KittyX.GirlLikeCheck(TempLine) >= 800:
                                            $ KittyX.FaceChange("sly",2,Eyes="side")
                                            $ KittyX.Statup("Obed", 80, 5)
                                            ch_k "Еще бы, они чуть ли не больше твоей головы. . ."
                                            $ KittyX.GirlLikeUp(TempLine,20) # +20
                                    elif KittyX.GirlLikeCheck(TempLine) >= 700:
                                            $ KittyX.Eyes = "side"
                                            $ KittyX.Statup("Obed", 80, 5)
                                            ch_k "Ну, ладно, раз они тебе нравятся. . ."
                                    else:
                                            $ KittyX.GirlLikeUp(TempLine,-50) # -50
                                            $ TempLine = "bad"
                            elif TempLine:
                                    if KittyX.GirlLikeCheck(TempLine) >= 800:
                                            $ KittyX.FaceChange("sly",2,Eyes="side")
                                            $ KittyX.Statup("Obed", 80, 5)
                                            ch_k "Ну да, словно два спелых яблочка. . . В смысле. . . эм-"
                                            $ KittyX.GirlLikeUp(TempLine,20)
                                    elif KittyX.GirlLikeCheck(TempLine) >= 700:
                                            $ KittyX.Eyes = "side"
                                            $ KittyX.Statup("Obed", 80, 5)
                                            ch_k "[KittyX.Like]наверное. . ."
                                    else:
                                            $ KittyX.GirlLikeUp(TempLine,-50)
                                            $ TempLine = "bad"
                            elif TempLine == "me":
                                    $ KittyX.Statup("Obed", 80, 7)
                                    if ApprovalCheck(KittyX, 800):
                                        $ KittyX.FaceChange("sly",2,Eyes="side")
                                        $ KittyX.Statup("Obed", 70, 7)
                                        ch_k "[KittyX.Like]наверное. . ."
                                    else:
                                        $ TempLine = "bad"

                            if TempLine == "bad":
                                            $ KittyX.Statup("Love", 90, -20)
                                            if not Player.Male:
                                                ch_k "Ты мне все настроение мне испортила."
                                            else:
                                                ch_k "Ты мне все настроение мне испортил."
                                            $ KittyX.OutfitChange()
                                            $ KittyX.RecentActions.append("no topless")
                                            $ KittyX.DailyActions.append("no topless")
                                            $ KittyX.RecentActions.append("angry")
                                            $ KittyX.DailyActions.append("angry")
            ". . . [[без комментариев]":
                    $ KittyX.FaceChange("sadside",1)
                    $ KittyX.Statup("Inbt", 60, 5)
                    $ KittyX.Statup("Obed", 70, 10)
                    if Player.Male:
                            $ KittyX.Statup("Love", 90, -10)
                    else:
                            $ KittyX.Statup("Love", 90, -5)


    else:
            $ KittyX.AddWord(1,0,0,0,"topless") #$ KittyX.History.append("topless")
            if (ApprovalCheck(KittyX, 800) or not Player.Male) and not KittyX.Forced:                #if she's not forced and happy about it
                    $ KittyX.Statup("Inbt", 70, 5)
                    $ KittyX.Statup("Obed", 70, 10)
            else:                                                           #if she's not happy about it
                    $ KittyX.Statup("Love", 90, -5)
                    $ KittyX.Statup("Inbt", 70, -5)
                    $ KittyX.FaceChange("angry")
                    $ KittyX.Statup("Obed", 70, 20)
    return

label Kitty_First_Bottomless(Silent = 0):
    if KittyX.PantiesNum() > 1 or KittyX.PantsNum() > 2 or KittyX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if KittyX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ KittyX.RecentActions.append("bottomless")
    $ KittyX.DailyActions.append("bottomless")
    $ KittyX.DrainWord("no bottomless")
    $ KittyX.SeenPussy += 1
    if KittyX.SeenPussy > 1:
            return                  #ends portion if you've already seen them

    $ KittyX.Statup("Inbt", 80, 30)
    $ KittyX.Statup("Obed", 70, 10)
    if not Silent:
        $ KittyX.FaceChange("bemused", 1)
        if not Player.Male and "girltalk" not in KittyX.History:
                "Вы ловите себя на том, что пялитесь на голую киску [KittyX.Name_rod]."
        else:
                "[KittyX.Name] робко убирает свои руки в сторону, обнажая свою киску."
        menu Kitty_First_BMenu:
            extend ""
            "Она чудесная. . .":
                    $ KittyX.Statup("Love", 90, 20)
                    $ KittyX.Statup("Inbt", 60, 25)
                    $ KittyX.FaceChange("smile")
                    ch_k ". . ."
                    $ KittyX.Statup("Love", 40, 20)
            "Именно -такую- \"Китти[[Прим. также Китти- киска, кошечка и т.д.]\" я и хотела увидеть." if not Player.Male:
                    $ KittyX.Statup("Love", 40, 25)
                    $ KittyX.Statup("Inbt", 60, 30)
                    $ KittyX.FaceChange("perplexed", 2)
                    ch_k "[[фыркает]"
                    $ KittyX.Statup("Love", 90, 25)
                    $ KittyX.Blush = 1
            "Именно -такую- \"Китти[[Прим. также Китти- киска, кошечка и т.д.]\" я и хотел увидеть." if Player.Male:
                    $ KittyX.Statup("Love", 40, 25)
                    $ KittyX.Statup("Inbt", 60, 30)
                    $ KittyX.FaceChange("perplexed", 2)
                    ch_k "[[фыркает]"
                    $ KittyX.Statup("Love", 90, 25)
                    $ KittyX.Blush = 1
            "Как-то там у тебя все неопрятно." if KittyX.Pubes:
                    $ KittyX.FaceChange("surprised",2)
                    ch_k "!"
                    if ApprovalCheck(KittyX, 800, "LO"):
                            $ KittyX.FaceChange("bemused",1)
                            $ KittyX.Statup("Obed", 50, 30)
                            $ KittyX.Statup("Inbt", 60, 25)
                            ch_k "Ну, думаю, это можно исправить. . ."
                            $ KittyX.Todo.append("shave")
                    else:
                            $ KittyX.FaceChange("angry",1)
                            $ KittyX.Statup("Love", 40, -20)
                            $ KittyX.Statup("Obed", 50, 25)
                            $ KittyX.Statup("Inbt", 60, -5)
                            ch_k "Ну[KittyX.like]извини, что там все не как у младенца!"
            "Я видела и получше." if not Player.Male:
                    $ KittyX.Statup("Love", 90, -30)
                    $ KittyX.Statup("Obed", 50, 25)
                    $ KittyX.Statup("Inbt", 70, -30)
                    $ KittyX.FaceChange("angry")
                    ch_k ". . ."
                    $ KittyX.Statup("Obed", 70, 35)
            "Я видел и получше." if Player.Male:
                    $ KittyX.Statup("Love", 90, -30)
                    $ KittyX.Statup("Obed", 50, 25)
                    $ KittyX.Statup("Inbt", 70, -30)
                    $ KittyX.FaceChange("angry")
                    ch_k ". . ."
                    $ KittyX.Statup("Obed", 70, 35)
            ". . . [[без комментариев]":
                    $ KittyX.FaceChange("sadside",1)
                    $ KittyX.Statup("Inbt", 60, 5)
                    $ KittyX.Statup("Obed", 70, 10)
                    if Player.Male:
                            $ KittyX.Statup("Love", 90, -10)
                    else:
                            $ KittyX.Statup("Love", 90, -5)
    else:
            $ KittyX.AddWord(1,0,0,0,"bottomless") #$ KittyX.History.append("bottomless")
            if (ApprovalCheck(KittyX, 800) or not Player.Male) and not KittyX.Forced:
                    $ KittyX.Statup("Inbt", 60, 15)
                    $ KittyX.Statup("Obed", 70, 10)
            else:
                    $ KittyX.Statup("Love", 90, -10)
                    $ KittyX.Statup("Inbt", 70, -5)
                    $ KittyX.FaceChange("angry")
                    $ KittyX.Statup("Obed", 70, 20)
    return


# Emma Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_First_Topless(Silent = 0, TempLine = 0):
    if EmmaX.ChestNum() > 1 or EmmaX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return
    if EmmaX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ EmmaX.RecentActions.append("topless")
    $ EmmaX.DailyActions.append("topless")
    $ EmmaX.DrainWord("no topless")
    $ EmmaX.SeenChest += 1
    if EmmaX.SeenChest > 1:
        return                  #ends portion if you've already seen them


    $ EmmaX.Statup("Inbt", 70, 15)
    if not Silent:
        $ EmmaX.FaceChange("sly")
        "Вы впервые видите обнаженную грудь [EmmaX.Name_rod]."
        if not Player.Male and "girltalk" not in EmmaX.History:
                ch_e "Прости, дорогая, должно быть, ты слишком удивлена. . ."
        else:
                ch_e "Как тебе, [EmmaX.Petname]? Все как ты и ожидал?"
        $ EmmaX.Blush = 1
        menu Emma_First_TMenu:
            extend ""
            "Точно и даже больше.":
                    $ EmmaX.Statup("Love", 90, 20)
                    $ EmmaX.Statup("Inbt", 70, 20)
                    $ EmmaX.FaceChange("smile",1)
                    ch_e "Я знала, что произведу на тебя впечатление."
                    $ EmmaX.Statup("Love", 40, 20)
                    $ EmmaX.Blush = 0
            ". . . [[Вы ошеломлены]":
                    $ EmmaX.Statup("Love", 90, 20)
                    $ EmmaX.Statup("Inbt", 70, 30)
                    ch_e "Да, это обычная реакция."
                    $ EmmaX.Statup("Love", 40, 10)
            "Эм, ну. . . как бы. . .":
                    $ EmmaX.Statup("Love", 90, -30)
                    $ EmmaX.Statup("Obed", 60, 25)
                    $ EmmaX.Statup("Inbt", 70, -15)
                    $ EmmaX.FaceChange("confused",2)
                    ch_e "Что?"
                    menu:
                        "Они даже лучше, чем я себе представляла!" if not Player.Male:
                                $ EmmaX.Statup("Love", 90, 20)
                                $ EmmaX.Statup("Obed", 60, -20)
                                $ EmmaX.Statup("Inbt", 70, 20)
                                $ EmmaX.FaceChange("perplexed",1)
                                ch_e "Что ж, полагаю, тебе удалось выкрутиться. . ."
                        "Они даже лучше, чем я себе представлял!" if Player.Male:
                                $ EmmaX.Statup("Love", 90, 20)
                                $ EmmaX.Statup("Obed", 60, -20)
                                $ EmmaX.Statup("Inbt", 70, 20)
                                $ EmmaX.FaceChange("perplexed",1)
                                ch_e "Что ж, полагаю, тебе удалось выкрутиться. . ."
                        "Я. . . эм. . . нет, они великолепны!":
                                $ EmmaX.FaceChange("angry",2, Mouth="smile")
                                $ EmmaX.Statup("Inbt", 70, 10)
                                ch_e "Еще бы!"
                        "Ну, у [RogueX.Name_rod] они более упругие, вот и все." if RogueX.SeenChest:
                                $ TempLine = RogueX
                        "Ну, у [KittyX.Name_rod] они более упругие, вот и все." if KittyX.SeenChest:
                                $ TempLine = KittyX
                        "Ну, у [LauraX.Name_rod] они более упругие, вот и все." if LauraX.SeenChest:
                                $ TempLine = LauraX
                        "Ну, у [JeanX.Name_rod] они более упругие, вот и все." if JeanX.SeenChest:
                                $ TempLine = JeanX
                        "Ну, у [StormX.Name_rod] они более упругие, вот и все." if StormX.SeenChest:
                                $ TempLine = StormX
                        "Мои просто лучше. . ." if Player.Male != 1:
                                $ Templine = "me"

                    if TempLine:
                            $ EmmaX.FaceChange("angry")
                            $ EmmaX.Mouth = "surprised"
                            $ EmmaX.Statup("Love", 90, -10)
                            $ EmmaX.Statup("Obed", 80, 30)
                            $ EmmaX.Statup("Inbt", 70, -25)
                            ch_e ". . ."
                            $ EmmaX.Mouth = "sad"
                            if TempLine == KittyX:
                                    if EmmaX.LikeKitty >= 800:
                                            $ EmmaX.FaceChange("sly",2,Eyes="side")
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            ch_e "Они скорее. . . более элегантные. . ."
                                            $ EmmaX.LikeKitty += 20
                                    elif EmmaX.LikeKitty >= 700:
                                            $ EmmaX.Eyes = "side"
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            ch_e "Ага, как у ребенка. . ."
                                    else:
                                            $ EmmaX.LikeKitty -= 50
                                            $ TempLine = "bad"

                            elif TempLine == StormX:
                                    if EmmaX.GirlLikeCheck(TempLine) >= 800:
                                            $ EmmaX.FaceChange("sly",2,Eyes="side")
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            ch_e "Они прекрасны, но. . ."
                                            $ EmmaX.GirlLikeUp(TempLine,20)
                                    elif EmmaX.GirlLikeCheck(TempLine) >= 700:
                                            $ EmmaX.Eyes = "side"
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            ch_e "Я не уверена. . ."
                                    else:
                                            $ EmmaX.GirlLikeUp(TempLine,-50)
                                            $ TempLine = "bad"
                            elif TempLine:
                                    if EmmaX.GirlLikeCheck(TempLine) >= 800:
                                            $ EmmaX.FaceChange("sly",2,Eyes="side")
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            ch_e "Они как спелые . . . яблоки. . ."
                                            $ EmmaX.GirlLikeUp(TempLine,20)
                                    elif EmmaX.GirlLikeCheck(TempLine) >= 700:
                                            $ EmmaX.Eyes = "side"
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            ch_e "Ладно, раз ты предпочитаешь такие. . ."
                                    else:
                                            $ EmmaX.GirlLikeUp(TempLine,-50)
                                            $ TempLine = "bad"
                            elif TempLine == "me":
                                    $ EmmaX.Statup("Obed", 80, 7)
                                    if ApprovalCheck(EmmaX, 800):
                                        $ EmmaX.FaceChange("sly",1)
                                        $ EmmaX.Statup("Obed", 70, 7)
                                        ch_e "Они прекрасны, но. . ."
                                    else:
                                        $ TempLine = "bad"


                            if TempLine == "bad":
                                            $ EmmaX.Statup("Love", 90, -20)
                                            if not Player.Male:
                                                ch_e "Что ж, полагаю, ты уже достаточно насмотрелась, [EmmaX.Petname]."
                                            else:
                                                ch_e "Что ж, полагаю, ты уже достаточно насмотрелся, [EmmaX.Petname]."
                                            $ EmmaX.OutfitChange()
                                            $ EmmaX.RecentActions.append("no topless")
                                            $ EmmaX.DailyActions.append("no topless")
                                            $ EmmaX.RecentActions.append("angry")
                                            $ EmmaX.DailyActions.append("angry")
            ". . . [[без комментариев]":
                    $ EmmaX.FaceChange("sly",1)
                    $ EmmaX.Statup("Inbt", 60, 5)
                    if Player.Male:
                            $ EmmaX.Statup("Love", 90, 10)
                    else:
                            $ EmmaX.Statup("Love", 90, 5)


    else:
            $ EmmaX.AddWord(1,0,0,0,"topless") #$ EmmaX.History.append("topless")
            if (ApprovalCheck(EmmaX, 800) or not Player.Male) and not EmmaX.Forced:                #if she's not forced and happy about it
                    $ EmmaX.Statup("Inbt", 70, 5)
                    $ EmmaX.Statup("Obed", 70, 5)
            else:                                                           #if she's not happy about it
                    $ EmmaX.Statup("Love", 90, -10)
                    $ EmmaX.Statup("Inbt", 70, -5)
                    $ EmmaX.FaceChange("angry")
                    $ EmmaX.Statup("Obed", 70, 15)
    return


label Emma_First_Bottomless(Silent = 0):
    if EmmaX.PantiesNum() > 1 or EmmaX.PantsNum() > 2 or EmmaX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if EmmaX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ EmmaX.RecentActions.append("bottomless")
    $ EmmaX.DailyActions.append("bottomless")
    $ EmmaX.DrainWord("no bottomless")
    $ EmmaX.SeenPussy += 1
    if EmmaX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ EmmaX.Statup("Inbt", 80, 30)
    $ EmmaX.Statup("Obed", 70, 10)
    if not Silent:
        $ EmmaX.FaceChange("sly")
        "Вы ловите себя на том, что пялитесь на голую киску [EmmaX.Name_rod]."
        menu Emma_First_BMenu:
            extend ""
            "Какая милая. . .":
                    $ EmmaX.Statup("Love", 90, 20)
                    $ EmmaX.Statup("Inbt", 60, 25)
                    $ EmmaX.FaceChange("smile")
                    ch_e "Я в курсе. . . "
                    $ EmmaX.Statup("Love", 40, 20)
            "Смотрю, у тебя там все гладенько." if not EmmaX.Pubes:
                $ EmmaX.FaceChange("confused",1)
                ch_e "Yes?"
                if ApprovalCheck(EmmaX, 700, "LO"):
                        $ EmmaX.FaceChange("bemused")
                        menu:
                            ch_e "Ты предпочитаешь пушистые?"
                            "Да":
                                if ApprovalCheck(EmmaX, 900, "LO"):
                                        $ EmmaX.Statup("Obed", 50, 30)
                                        $ EmmaX.Statup("Inbt", 60, 25)
                                        ch_e "Полагаю, это можно исправить. . ."
                                        $ EmmaX.Todo.append("pubes")
                                else:
                                        $ EmmaX.FaceChange("normal")
                                        ch_e "Что ж, жаль."
                            "Оставлю это, пожалуй, на твое усмотрение.":
                                        $ EmmaX.Statup("Love", 80, 10)
                                        ch_e "Я рада."
                            "Нет, оставь все как есть.":
                                        if ApprovalCheck(EmmaX, 900, "LO"):
                                                $ EmmaX.FaceChange("sly")
                                                $ EmmaX.Statup("Love", 80, 10)
                                        else:
                                                $ EmmaX.FaceChange("angry",Mouth="normal")
                                        $ EmmaX.Statup("Inbt", 60, 25)
                                        if not Player.Male:
                                            ch_e "Я рада, что ты мне. . . разрешила."
                                        else:
                                            ch_e "Я рада, что ты мне. . . разрешил."
                                        $ EmmaX.Brows = "normal"
                else:
                        $ EmmaX.FaceChange("angry",1)
                        $ EmmaX.Statup("Love", 40, -20)
                        $ EmmaX.Statup("Obed", 50, 25)
                        $ EmmaX.Statup("Inbt", 60, -5)
                        ch_e "Да, мне нравится ухоженный \"сад\"."
            "Неплохо для твоего возраста.":
                $ EmmaX.Statup("Love", 90, -30)
                $ EmmaX.Statup("Obed", 50, 25)
                $ EmmaX.Statup("Inbt", 70, -30)
                $ EmmaX.FaceChange("angry",2)
                if not EmmaX.Forced and not ApprovalCheck(EmmaX, 900, "LO"):
                        $ EmmaX.RecentActions.append("angry")
                        $ EmmaX.DailyActions.append("angry")
                        $ EmmaX.Statup("Obed", 70, 25)
                ch_e "Ты еще пожалеешь об этом замечании. . ."
            ". . . [[без комментариев]":
                    $ EmmaX.FaceChange("sly",1)
                    $ EmmaX.Statup("Inbt", 60, 5)
                    $ EmmaX.Statup("Obed", 70, 10)
                    if Player.Male:
                            $ EmmaX.Statup("Love", 90, -2)
    else:

        $ EmmaX.AddWord(1,0,0,0,"bottomless") #$ EmmaX.History.append("bottomless")
        if (ApprovalCheck(EmmaX, 800) or not Player.Male) and not EmmaX.Forced:
                $ EmmaX.Statup("Inbt", 60, 5)
                $ EmmaX.Statup("Obed", 70, 10)
        else:
                $ EmmaX.Statup("Love", 90, -10)
                $ EmmaX.Statup("Inbt", 70, -5)
                $ EmmaX.FaceChange("angry")
                $ EmmaX.Statup("Obed", 70, 15)
    return

# Laura Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_First_Topless(Silent = 0, TempLine = 0):
    if LauraX.ChestNum() > 1 or LauraX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return
    if LauraX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ LauraX.RecentActions.append("topless")
    $ LauraX.DailyActions.append("topless")
    $ LauraX.DrainWord("no topless")
    $ LauraX.SeenChest += 1
    if LauraX.SeenChest > 1:
            return                  #ends portion if you've already seen them

    $ LauraX.Statup("Inbt", 70, 15)
    if not Silent:
        $ LauraX.FaceChange("sly")
        "Вы впервые видите обнаженную грудь [LauraX.Name_rod]."
        if not Player.Male:
            ch_l "И? На что ты так уставилась?"
        else:
            ch_l "И? На что ты так уставился?"
        $ LauraX.Blush = 1
        menu Laura_First_TMenu:
            extend ""
            "На твои сиськи? Они выглядят великолепно.":
                    $ LauraX.Statup("Love", 90, 20)
                    $ LauraX.Statup("Inbt", 70, 20)
                    $ LauraX.FaceChange("sexy",1,Eyes="down")
                    ch_l "Хм. Наверное. . ."
                    $ LauraX.FaceChange("smile",0)
                    $ LauraX.Statup("Love", 40, 20)
            ". . . [[Вы ошеломлены]":
                    $ LauraX.Statup("Love", 90, 10)
                    $ LauraX.Statup("Inbt", 70, 10)
                    if not Player.Male:
                        ch_l "Язык проглотила?"
                    else:
                        ch_l "Язык проглотил?"
                    $ LauraX.Statup("Love", 40, 10)
            "Эм, ну. . . как бы. . .":
                    $ LauraX.Statup("Love", 90, -30)
                    $ LauraX.Statup("Obed", 60, 25)
                    $ LauraX.Statup("Inbt", 70, -15)
                    $ LauraX.FaceChange("confused",2)
                    ch_l "Что?"
                    menu:
                        "Они у тебя очень пылкие!":
                                $ LauraX.Statup("Love", 90, 20)
                                $ LauraX.Statup("Obed", 60, -20)
                                $ LauraX.Statup("Inbt", 70, 20)
                                $ LauraX.FaceChange("perplexed",1)
                                ch_l "Ох. Верно. . ."
                        "Я. . . эм. . . нет, они великолепны!":
                                $ LauraX.FaceChange("angry",2, Mouth="smile")
                                $ LauraX.Statup("Inbt", 70, 10)
                                ch_l "Почему бы им такими не быть?"
                        "Ну, у [KittyX.Name_rod] они более упругие, вот и все." if KittyX.SeenChest:
                                $ TempLine = KittyX
                        "Ну, у [EmmaX.Name_rod] они намного больше, вот и все." if EmmaX.SeenChest:
                                $ TempLine = EmmaX
                        "Ну, у [StormX.Name_rod] они намного больше, вот и все." if StormX.SeenChest:
                                $ TempLine = StormX
                        "Мои просто лучше. . ." if Player.Male != 1:
                                $ Templine = "me"

                    if TempLine:
                            $ LauraX.FaceChange("angry")
                            $ LauraX.Mouth = "surprised"
                            $ LauraX.Statup("Love", 90, -10)
                            $ LauraX.Statup("Obed", 80, 30)
                            $ LauraX.Statup("Inbt", 70, -25)
                            ch_l ". . ."
                            $ LauraX.Mouth = "sad"
                            if TempLine in (EmmaX,StormX):
                                    if LauraX.GirlLikeCheck(TempLine) >= 800:
                                        $ LauraX.FaceChange("sly",2,Eyes="side")
                                        $ LauraX.Statup("Obed", 80, 5)
                                        ch_l "У нее они прямо огромные. . ."
                                        $ LauraX.GirlLikeUp(TempLine,20)
                                    elif LauraX.GirlLikeCheck(TempLine) >= 700:
                                        $ LauraX.Eyes = "side"
                                        $ LauraX.Statup("Obed", 80, 5)
                                        ch_l "Наверное, так и есть. . ."
                                    else:
                                        $ LauraX.GirlLikeUp(TempLine,-50)
                                        $ TempLine = "bad"

                            elif TempLine == KittyX:
                                    if LauraX.LikeKitty >= 800:
                                        $ LauraX.FaceChange("sly",2,Eyes="side")
                                        $ LauraX.Statup("Obed", 80, 5)
                                        ch_l "У нее они очень. . . изящные. . ."
                                        $ LauraX.LikeKitty += 20
                                    elif LauraX.LikeKitty >= 700:
                                        $ LauraX.Eyes = "side"
                                        $ LauraX.Statup("Obed", 80, 5)
                                        ch_l "У нее они очень. . . острые. . ."
                                    else:
                                        $ LauraX.LikeKitty -= 50
                                        $ TempLine = "bad"
                            elif TempLine == "me":
                                    $ LauraX.Statup("Obed", 80, 5)
                                    if ApprovalCheck(LauraX, 800):
                                        $ LauraX.FaceChange("sly",1)
                                        $ LauraX.Statup("Obed", 70, 5)
                                        ch_l "Ну ладно, как скажешь. . ."
                                    else:
                                        $ TempLine = "bad"


                            if TempLine == "bad":
                                    $ LauraX.Statup("Love", 90, -20)
                                    ch_l "Знаешь, это было довольно грубо."
                                    $ LauraX.OutfitChange()
                                    $ LauraX.RecentActions.append("no topless")
                                    $ LauraX.DailyActions.append("no topless")
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")
            ". . . [[без комментариев]":
                    $ LauraX.FaceChange("normal",1,Eyes="side")
                    $ LauraX.Statup("Inbt", 60, 5)
                    $ LauraX.Statup("Obed", 70, 15)
                    if Player.Male:
                            $ LauraX.Statup("Love", 90, -2)


    else:
            $ LauraX.AddWord(1,0,0,0,"topless") #$ LauraX.History.append("topless")
            if (ApprovalCheck(LauraX, 800) or not Player.Male) and not LauraX.Forced:                #if she's not forced and happy about it
                    $ LauraX.Statup("Inbt", 70, 5)
                    $ LauraX.Statup("Obed", 70, 10)
            else:                                                           #if she's not happy about it
                    $ LauraX.Statup("Love", 90, -5)
                    $ LauraX.Statup("Inbt", 70, -5)
                    $ LauraX.FaceChange("angry")
                    $ LauraX.Statup("Obed", 70, 10)
    return


label Laura_First_Bottomless(Silent = 0):
    if LauraX.PantiesNum() > 1 or LauraX.PantsNum() > 2 or LauraX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if LauraX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ LauraX.RecentActions.append("bottomless")
    $ LauraX.DailyActions.append("bottomless")
    $ LauraX.DrainWord("no bottomless")
    $ LauraX.SeenPussy += 1
    if LauraX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ LauraX.Statup("Inbt", 80, 30)
    $ LauraX.Statup("Obed", 70, 10)
    if not Silent:
        $ LauraX.FaceChange("sly")
        if LauraX.Pubes:
                "Вы уставились на [LauraX.Name] мохнатую киску."
        else:
                "YВы уставились на [LauraX.Name] голую киску."
        menu Laura_First_BMenu:
            extend ""
            "Какая милая. . .":
                    $ LauraX.Statup("Love", 90, 20)
                    $ LauraX.Statup("Inbt", 60, 25)
                    $ LauraX.FaceChange("smile")
                    ch_l "Думаешь?"
                    ch_l "Мне она тоже нравится. . . "
                    $ LauraX.Statup("Love", 40, 20)
            "Смотрю, у тебя там все так естественно." if LauraX.Pubes:
                $ LauraX.FaceChange("confused",1)
                ch_l "Ну. . . да."
                if ApprovalCheck(LauraX, 700, "LO"):
                    $ LauraX.FaceChange("bemused")
                    menu:
                        ch_l "Думаешь, стоит побрить?"
                        "Да":
                            if ApprovalCheck(LauraX, 900, "LO"):
                                    $ LauraX.Statup("Obed", 50, 30)
                                    $ LauraX.Statup("Inbt", 60, 25)
                                    ch_l "Наверное, это можно устроить. . ."
                                    $ LauraX.Todo.append("shave")
                            else:
                                    $ LauraX.FaceChange("normal")
                                    ch_l "Похоже на пустую трату времени."
                                    ch_l "Ты хоть представляешь, насколько быстро растут мои волосы?"
                        "Оставлю это, пожалуй, на твое усмотрение.":
                                    $ LauraX.Statup("Love", 80, 10)
                                    ch_l "Да, думаю, слишком трудно поддерживать там все гладким."
                        "Нет, оставь все как есть.":
                                    if ApprovalCheck(LauraX, 900, "LO"):
                                            $ LauraX.FaceChange("sly")
                                            $ LauraX.Statup("Love", 80, 10)
                                    else:
                                            $ LauraX.FaceChange("angry",Mouth="normal")
                                    $ LauraX.Statup("Inbt", 60, 25)
                                    ch_l "Ладно."
                                    $ LauraX.Brows = "normal"
                else:
                        $ LauraX.FaceChange("angry",1)
                        $ LauraX.Statup("Love", 40, -20)
                        $ LauraX.Statup("Obed", 50, 25)
                        $ LauraX.Statup("Inbt", 60, -5)
                        ch_l "А что мне еще, по твоему, делать?"
            "Как же у тебя там все неопрятно.":
                    $ LauraX.Statup("Love", 90, -30)
                    $ LauraX.Statup("Obed", 50, 25)
                    $ LauraX.Statup("Inbt", 70, -30)
                    $ LauraX.FaceChange("angry",2)
                    if not LauraX.Forced and not ApprovalCheck(LauraX, 900, "LO"):
                            $ LauraX.RecentActions.append("angry")
                            $ LauraX.DailyActions.append("angry")
                            $ LauraX.Statup("Obed", 70, 25)
                    ch_l "Я покажу тебе \"неопрятно\". . ."
            ". . . [[без комментариев]":
                    $ LauraX.Statup("Inbt", 60, 7)
                    $ LauraX.Statup("Obed", 70, 12)
    else:
        $ LauraX.AddWord(1,0,0,0,"bottomless") #$ LauraX.History.append("bottomless")
        if (ApprovalCheck(LauraX, 800) or not Player.Male) and not LauraX.Forced:
                $ LauraX.Statup("Inbt", 60, 5)
                $ LauraX.Statup("Obed", 70, 10)
        else:
                $ LauraX.Statup("Love", 90, -5)
                $ LauraX.Statup("Inbt", 70, -5)
                $ LauraX.FaceChange("angry")
                $ LauraX.Statup("Obed", 70, 15)
    return


# Jean Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jean_First_Topless(Silent = 0, TempLine = 0):
    if (JeanX.ChestNum() > 1 or JeanX.OverNum() > 2) and not TempLine:
            #if she's wearing substantial clothing. . .
            # TempLine might be 1 if sent by intro scene
            return
    if JeanX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ JeanX.RecentActions.append("topless")
    $ JeanX.DailyActions.append("topless")
    $ JeanX.DrainWord("no topless")
    $ JeanX.SeenChest += 1
    if JeanX.SeenChest > 1:
            return                  #ends portion if you've already seen them

    $ JeanX.Statup("Inbt", 70, 15)
    if not Silent:
        $ JeanX.FaceChange("sly")
        "Вы впервые видите обнаженную грудь [JeanX.Name_rod]."
        ch_j "Впечатляет, да?"
        $ JeanX.Blush = 1
        menu Jean_First_TMenu:
            extend ""
            "Ага, они выглядят потрясающе.":
                    $ JeanX.Statup("Love", 90, 10)
                    $ JeanX.Statup("Inbt", 200, 20)
                    $ JeanX.FaceChange("sexy",1,Eyes="down")
                    ch_j "А еще они очень упругие. . ."
                    $ JeanX.FaceChange("smile",0)
                    $ JeanX.Statup("Obed", 40, 20)
            ". . . [[Вы ошеломлены]":
                    $ JeanX.Statup("Love", 90, 20)
                    $ JeanX.Statup("Inbt", 200, 10)
                    ch_j "Ошеломляют, я знаю."
                    $ JeanX.Statup("Obed", 40, 10)
            "Эм, ну. . . как бы. . .":
                    $ JeanX.Statup("Love", 90, 10)
                    $ JeanX.Statup("Obed", 40, 20)
                    $ JeanX.Statup("Inbt", 200, 20)
                    $ JeanX.FaceChange("smile",0)
                    ch_j "Имен-{w=0.3}{nw}"
                    $ JeanX.Statup("Love", 90, -40)
                    $ JeanX.Statup("Obed", 60, 10)
                    $ JeanX.Statup("Inbt", 200, -15)
                    $ JeanX.FaceChange("confused",2)
                    ch_j "Имен- подожди, что?"
                    $ TempLine = 0
                    menu:
                        "Они у тебя очень пылкие!":
                                $ JeanX.Statup("Love", 90, 10)
                                $ JeanX.Statup("Obed", 60, 10)
                                $ JeanX.Statup("Inbt", 200, 20)
                                $ JeanX.FaceChange("perplexed",1)
                                ch_j "Ох, конечно. . ."
                        "Я. . . эм. . . нет, они великолепны!":
                                $ JeanX.FaceChange("angry",2, Mouth="smile")
                                $ JeanX.Statup("Obed", 80, 20)
                                ch_j "Еще бы!"
                        "Ну, у [RogueX.Name_rod] они поприятнее, вот и все." if RogueX.SeenChest:
                                $ TempLine = RogueX
                        "Ну, у [KittyX.Name_rod] они более упругие, вот и все." if KittyX.SeenChest:
                                $ TempLine = KittyX
                        "Ну, у [EmmaX.Name_rod] они намного больше, вот и все." if EmmaX.SeenChest:
                                $ TempLine = EmmaX
                        "Ну, у [LauraX.Name_rod] они поприятнее, вот и все." if LauraX.SeenChest:
                                $ TempLine = LauraX
                        "Ну, у [StormX.Name_rod] они намного больше, вот и все." if StormX.SeenChest:
                                $ TempLine = StormX
                        "Мои просто лучше. . ." if Player.Male != 1:
                                $ Templine = "me"

                    if TempLine:
                            $ JeanX.FaceChange("angry")
                            $ JeanX.Mouth = "surprised"
                            $ JeanX.Statup("Love", 50, -10)
                            $ JeanX.Statup("Love", 90, -10)
                            $ JeanX.Statup("Obed", 50, 10)
                            $ JeanX.Statup("Obed", 80, 30)
                            $ JeanX.Statup("Inbt", 200, -15)
                            ch_j ". . ."
                            $ JeanX.Mouth = "sad"
                            if TempLine in (EmmaX,StormX):
                                    if JeanX.GirlLikeCheck(TempLine) >= 700:
                                        $ JeanX.FaceChange("sly",2,Eyes="side")
                                        ch_j "Ну, у нее они. . . увесистее. . ."
                                        $ JeanX.GirlLikeUp(TempLine,20)
                                    else:
                                        $ JeanX.Eyes = "side"
                                        ch_j "Ну, если тебе нравится такое вымя. . ."
                                        $ JeanX.LikeEmma -= 50
                                        $ JeanX.GirlLikeUp(TempLine,-50)
                                        $ TempLine = "bad"

                            elif TempLine == KittyX:
                                    if JeanX.LikeKitty >= 700:
                                        $ JeanX.FaceChange("sly",2,Eyes="side")
                                        ch_j "У нее они очень. . . милые. . ."
                                        $ JeanX.LikeKitty += 20
                                    else:
                                        $ JeanX.Eyes = "side"
                                        ch_j "Если тебе нравятся доски, то да. . ."
                                        $ JeanX.LikeKitty -= 50
                                        $ TempLine = "bad"
                            elif TempLine == "me":
                                    $ JeanX.Statup("Obed", 80, 10)
                                    if ApprovalCheck(JeanX, 800):
                                        $ JeanX.FaceChange("angry",2,Eyes="side")
                                        $ JeanX.Statup("Obed", 70, 10)
                                        ch_j ". . . Ну да. . . они у тебя неплохие. . ."
                                    else:
                                        $ TempLine = "bad"
                            else:
                                    if JeanX.GirlLikeCheck(TempLine) >= 700:
                                        $ JeanX.FaceChange("sly",2,Eyes="side")
                                        ch_j "У нее они такие. . . миниатюрные.. . ."
                                        $ JeanX.GirlLikeUp(TempLine,20)
                                    else:
                                        $ JeanX.Eyes = "side"
                                        ch_j "У нее они очень. . . острые. . ."
                                        $ JeanX.GirlLikeUp(TempLine,-50)
                                        $ TempLine = "bad"


                            if TempLine == "bad":
                                    $ JeanX.Statup("Love", 90, -20)
                                    ch_j "Вот можешь ты все испортить!"
                                    $ JeanX.OutfitChange()
                                    $ JeanX.RecentActions.append("no topless")
                                    $ JeanX.DailyActions.append("no topless")
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
            ". . . [[без комментариев]":
                    $ JeanX.FaceChange("angry",1)
                    $ JeanX.Statup("Inbt", 60, 10)
                    $ JeanX.Statup("Obed", 70, 15)
                    if Player.Male:
                            $ JeanX.Statup("Love", 90, -10)
                    else:
                            $ JeanX.Statup("Love", 90, -5)


    else:
            if (ApprovalCheck(JeanX, 800) or not Player.Male) and not JeanX.Forced:                  #if she's not forced and happy about it
                    $ JeanX.Statup("Love", 70, 10)
                    $ JeanX.Statup("Obed", 70, 25)
                    $ JeanX.Statup("Inbt", 70, 15)
            else:                                                               #if she's not happy about it
                    $ JeanX.Statup("Love", 90, -40)
                    $ JeanX.Statup("Inbt", 200, -20)
                    $ JeanX.FaceChange("angry")
                    $ JeanX.Statup("Obed", 70, 40)
    return


label Jean_First_Bottomless(Silent = 0):
    if JeanX.PantiesNum() > 1 or JeanX.PantsNum() > 2 or JeanX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if JeanX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ JeanX.RecentActions.append("bottomless")
    $ JeanX.DailyActions.append("bottomless")
    $ JeanX.DrainWord("no bottomless")
    $ JeanX.SeenPussy += 1
    if JeanX.SeenPussy > 1:
            return                  #ends portion if you've already seen them

    $ JeanX.Statup("Inbt", 200, 30)
    $ JeanX.Statup("Obed", 90, 10)
    if not Silent:
        $ JeanX.FaceChange("sly")
        if JeanX.Pubes:
                "Вы ловите себя на том, что пялитесь на пушистую киску [JeanX.Name_rod]."
        else:
                "Вы ловите себя на том, что пялитесь на голую киску [JeanX.Name_rod]."
        menu Jean_First_BMenu:
            extend ""
            "Какая милая. . .":
                    $ JeanX.Statup("Love", 90, 20)
                    $ JeanX.Statup("Inbt", 200, 25)
                    $ JeanX.FaceChange("smile")
                    ch_j "Правда?"
                    $ JeanX.Statup("Love", 40, 20)
            "Смотрю, у тебя там словно бушует пламя." if JeanX.Pubes:
                $ JeanX.FaceChange("confused",1)
                ch_j "Ну. . . да."
                if ApprovalCheck(JeanX, 700, "LO"):
                    $ JeanX.FaceChange("bemused")
                    menu:
                        ch_j "Тебе нравятся гладкие?"
                        "Да":
                            if ApprovalCheck(JeanX, 900, "LO"):
                                    $ JeanX.Statup("Obed", 90, 30)
                                    $ JeanX.Statup("Inbt", 200, 25)
                                    ch_j "Мммм, могу все устроить. . ."
                                    $ JeanX.Todo.append("shave")
                            else:
                                    $ JeanX.FaceChange("normal")
                                    ch_j "Слишком хлопотно."
                        "Оставлю это, пожалуй, на твое усмотрение.":
                                    $ JeanX.Statup("Love", 80, 10)
                                    ch_j "Конечно."
                        "Нет, оставь все как есть.":
                                    if ApprovalCheck(JeanX, 900, "LO"):
                                            $ JeanX.FaceChange("sly")
                                            $ JeanX.Statup("Love", 80, 10)
                                    else:
                                            $ JeanX.FaceChange("angry",Mouth="normal")
                                    $ JeanX.Statup("Inbt", 200, 25)
                                    ch_j "Конечно."
                                    $ JeanX.Brows = "normal"
                else:
                        $ JeanX.FaceChange("angry",1)
                        $ JeanX.Statup("Love", 40, -20)
                        $ JeanX.Statup("Obed", 90, 25)
                        $ JeanX.Statup("Inbt", 200, -5)
                        ch_j "Мне очень не хотелось делать эпиляцию."
            "Как же у тебя там все неопрятно." if JeanX.Pubes:
                    $ JeanX.Statup("Love", 90, -30)
                    $ JeanX.Statup("Obed", 90, 25)
                    $ JeanX.Statup("Inbt", 200, -30)
                    $ JeanX.FaceChange("angry",2)
                    if not JeanX.Forced and not ApprovalCheck(JeanX, 900, "LO"):
                            $ JeanX.RecentActions.append("angry")
                            $ JeanX.DailyActions.append("angry")
                            $ JeanX.Statup("Obed", 90, 25)
                    ch_j "Ох, не так по-детски гладко, как у [EmmaX.Name_rod]?"
            "Эм, я видала и получше" if not JeanX.Pubes and not Player.Male:
                    $ JeanX.Statup("Love", 90, -30)
                    $ JeanX.Statup("Obed", 90, 25)
                    $ JeanX.Statup("Inbt", 200, -30)
                    $ JeanX.FaceChange("angry",2)
                    if not JeanX.Forced and not ApprovalCheck(JeanX, 900, "LO"):
                            $ JeanX.RecentActions.append("angry")
                            $ JeanX.DailyActions.append("angry")
                            $ JeanX.Statup("Obed", 90, 25)
                    ch_j "Ох, не такая мохнатая, как у [LauraX.Name_rod]?"
            "Эм, я видал и получше" if not JeanX.Pubes and Player.Male:
                    $ JeanX.Statup("Love", 90, -30)
                    $ JeanX.Statup("Obed", 90, 25)
                    $ JeanX.Statup("Inbt", 200, -30)
                    $ JeanX.FaceChange("angry",2)
                    if not JeanX.Forced and not ApprovalCheck(JeanX, 900, "LO"):
                            $ JeanX.RecentActions.append("angry")
                            $ JeanX.DailyActions.append("angry")
                            $ JeanX.Statup("Obed", 90, 25)
                    ch_j "Ох, не такая мохнатая, как у [LauraX.Name_rod]?"
            ". . . [[без комментариев]":
                    $ JeanX.FaceChange("angry",1)
                    $ JeanX.Statup("Inbt", 60, 7)
                    $ JeanX.Statup("Obed", 70, 12)
                    if Player.Male:
                            $ JeanX.Statup("Love", 90, -2)
    else:
        $ JeanX.AddWord(1,0,0,0,"bottomless") #$ JeanX.History.append("bottomless")
        if (ApprovalCheck(JeanX, 800) or not Player.Male) and not JeanX.Forced:
                $ JeanX.Statup("Inbt", 60, 5)
                $ JeanX.Statup("Obed", 90, 10)
        else:
                $ JeanX.Statup("Love", 90, -5)
                $ JeanX.Statup("Inbt", 200, -5)
                $ JeanX.FaceChange("angry")
                $ JeanX.Statup("Obed", 90, 15)
    return


# Storm Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Storm_First_Topless(Silent = 0, TempLine = 0):
    #most of the content was unneeded since you first meet her naked
    if StormX.ChestNum() > 1 or StormX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return
    if StormX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ StormX.RecentActions.append("topless")
    $ StormX.DailyActions.append("topless")
    $ StormX.DrainWord("no topless")
    $ StormX.SeenChest += 1
    return


label Storm_First_Bottomless(Silent = 0):
    if StormX.PantiesNum() > 1 or StormX.PantsNum() > 2 or StormX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if StormX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ StormX.RecentActions.append("bottomless")
    $ StormX.DailyActions.append("bottomless")
    $ StormX.DrainWord("no bottomless")
    $ StormX.SeenPussy += 1
    return


# Jubes Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jubes_First_Topless(Silent = 0, TempLine = 0):
    if JubesX.ChestNum() > 1 or JubesX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return
    if JubesX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ JubesX.RecentActions.append("topless")
    $ JubesX.DailyActions.append("topless")
    $ JubesX.DrainWord("no topless")
    $ JubesX.SeenChest += 1
    if JubesX.SeenChest > 1:
            return                  #ends portion if you've already seen them

    $ JubesX.Statup("Inbt", 70, 15)
    if not Silent:
        $ JubesX.FaceChange("sly")
        "Вы впервые видите обнаженную грудь [JubesX.Name_rod]."
        if not Player.Male and "girltalk" not in JubesX.History:
                ch_v "Ох, эм. . . вот ты их и увидела. . ."
        else:
                ch_v "Так. . . эм. . . тебе нравится?"
        $ JubesX.Blush = 1
        menu Jubes_First_TMenu:
            extend ""
            "Твои сиськи? Они выглядят великолепно.":
                    $ JubesX.Statup("Love", 90, 20)
                    $ JubesX.Statup("Inbt", 70, 20)
                    $ JubesX.FaceChange("smile",2)
                    pause 0.5
                    $ JubesX.FaceChange("sexy",1,Eyes="down")
                    ch_v "Ах! Эм. . . ага, наверное. . ."
                    $ JubesX.FaceChange("smile")
                    $ JubesX.Statup("Love", 40, 20)
            ". . . [[Вы ошеломлены]":
                    $ JubesX.Statup("Love", 90, 10)
                    $ JubesX.Statup("Inbt", 70, 10)
                    ch_v "Ох, вот это \"удар.\""
                    $ JubesX.Statup("Love", 40, 10)
            "Эм, ну. . . как бы. . .":
                    $ JubesX.Statup("Love", 90, -30)
                    $ JubesX.Statup("Obed", 60, 25)
                    $ JubesX.Statup("Inbt", 70, -15)
                    $ JubesX.FaceChange("confused",2)
                    ch_v "Чо?"
                    menu:
                        "Они у тебя очень пылкие!":
                                $ JubesX.Statup("Love", 90, 20)
                                $ JubesX.Statup("Obed", 60, -20)
                                $ JubesX.Statup("Inbt", 70, 20)
                                $ JubesX.FaceChange("perplexed",1)
                                ch_v "Ох. Верно. . ."
                        "Я. . . эм. . . нет, они великолепны!":
                                $ JubesX.FaceChange("angry",2, Mouth="smile")
                                $ JubesX.Statup("Inbt", 70, 10)
                                ch_v ". . ."
                                ch_v "Я -знаю- это, вот почему я была в замешательстве."
                        "Ну, у [KittyX.Name_rod] они более упругие, вот и все." if KittyX.SeenChest:
                                $ TempLine = KittyX
                        "Ну, у [EmmaX.Name_rod] они намного больше, вот и все." if EmmaX.SeenChest:
                                $ TempLine = EmmaX
                        "Ну, у [StormX.Name_rod] они намного больше, вот и все." if StormX.SeenChest:
                                $ TempLine = StormX
                        "Мои просто лучше. . ." if Player.Male != 1:
                                $ Templine = "me"

                    if TempLine:
                            $ JubesX.FaceChange("angry")
                            $ JubesX.Mouth = "surprised"
                            $ JubesX.Statup("Love", 90, -10)
                            $ JubesX.Statup("Obed", 80, 30)
                            $ JubesX.Statup("Inbt", 70, -25)
                            ch_v ". . ."
                            $ JubesX.Mouth = "sad"
                            if TempLine in (EmmaX,StormX):
                                    if JubesX.GirlLikeCheck(TempLine) >= 800:
                                        $ JubesX.FaceChange("sly",2,Eyes="side")
                                        $ JubesX.Statup("Obed", 80, 5)
                                        ch_v "Нууу, они у нее действительно огромные. . ."
                                        $ JubesX.GirlLikeUp(TempLine,20)
                                    elif JubesX.GirlLikeCheck(TempLine) >= 700:
                                        $ JubesX.Eyes = "side"
                                        $ JubesX.Statup("Obed", 80, 5)
                                        ch_v "Ох. Нууу, я не могу соревноваться с ней в этом. . ."
                                    else:
                                        $ JubesX.GirlLikeUp(TempLine,-50)
                                        $ TempLine = "bad"

                            elif TempLine == KittyX:
                                    if JubesX.LikeKitty >= 800:
                                        $ JubesX.FaceChange("sly",2,Eyes="side")
                                        $ JubesX.Statup("Obed", 80, 5)
                                        ch_v ". . . Думаю, они очень милые. . ."
                                        $ JubesX.LikeKitty += 20
                                    elif JubesX.LikeKitty >= 700:
                                        $ JubesX.Eyes = "side"
                                        $ JubesX.Statup("Obed", 80, 5)
                                        ch_v "Ладно, перейдем к делу, да? . ."
                                    else:
                                        $ JubesX.LikeKitty -= 50
                                        $ TempLine = "bad"
                            elif TempLine == "me":
                                    $ JubesX.Statup("Obed", 80, 5)
                                    if ApprovalCheck(JubesX, 800):
                                        $ JubesX.FaceChange("sly",2,Eyes="side")
                                        $ JubesX.Statup("Obed", 70, 5)
                                        ch_v ". . . Думаю, они у тебя очень милые. . ."
                                    else:
                                        $ TempLine = "bad"

                            if TempLine == "bad":
                                    $ JubesX.Statup("Love", 90, -20)
                                    ch_v "Нельзя так просто -говорить- что-то типа этого!"
                                    $ JubesX.OutfitChange()
                                    $ JubesX.RecentActions.append("no topless")
                                    $ JubesX.DailyActions.append("no topless")
                                    $ JubesX.RecentActions.append("angry")
                                    $ JubesX.DailyActions.append("angry")
            ". . . [[без комментариев]":
                    $ JubesX.FaceChange("angry",1)
                    $ JubesX.Statup("Inbt", 60, 3)
                    $ JubesX.Statup("Obed", 70, 12)
                    if Player.Male:
                            $ JubesX.Statup("Love", 90, -3)


    else:
            $ JubesX.AddWord(1,0,0,0,"topless") #$ JubesX.History.append("topless")
            if (ApprovalCheck(JubesX, 800) or not Player.Male) and not JubesX.Forced:                #if she's not forced and happy about it
                    $ JubesX.Statup("Inbt", 70, 5)
                    $ JubesX.Statup("Obed", 70, 10)
            else:                                                           #if she's not happy about it
                    $ JubesX.Statup("Love", 90, -5)
                    $ JubesX.Statup("Inbt", 70, -5)
                    $ JubesX.FaceChange("angry")
                    $ JubesX.Statup("Obed", 70, 10)
    return


label Jubes_First_Bottomless(Silent = 0):
    if JubesX.PantiesNum() > 1 or JubesX.PantsNum() > 2 or JubesX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if JubesX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ JubesX.RecentActions.append("bottomless")
    $ JubesX.DailyActions.append("bottomless")
    $ JubesX.DrainWord("no bottomless")
    $ JubesX.SeenPussy += 1
    if JubesX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ JubesX.Statup("Inbt", 80, 30)
    $ JubesX.Statup("Obed", 70, 10)
    if not Silent:
        $ JubesX.FaceChange("sly")
        if JubesX.Pubes:
                "Вы ловите себя на том, что пялитесь на пушистую киску [JubesX.Name_rod]."
        else:
                "Вы ловите себя на том, что пялитесь на гладкую киску [JubesX.Name_rod]."
        menu Jubes_First_BMenu:
            extend ""
            "Какая милая. . .":
                    $ JubesX.Statup("Love", 90, 20)
                    $ JubesX.Statup("Inbt", 60, 25)
                    $ JubesX.FaceChange("surprised",2)
                    ch_v "!!"
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Ох, эм, ага, я. . . тоже так думаю. . . "
                    $ JubesX.Statup("Love", 40, 20)
            "Смотрю, у тебя там все так естественно." if JubesX.Pubes:
                $ JubesX.FaceChange("confused",2)
                ch_v "Ну. . . да."
                if ApprovalCheck(JubesX, 700, "LO"):
                    $ JubesX.FaceChange("bemused",1)
                    menu:
                        ch_v "Ты. . . предпочитаешь бритые?"
                        "Да":
                            if ApprovalCheck(JubesX, 900, "LO"):
                                    $ JubesX.Statup("Obed", 50, 30)
                                    $ JubesX.Statup("Inbt", 60, 25)
                                    ch_v "Думаю, можно это устроить. . ."
                                    $ JubesX.Todo.append("shave")
                            else:
                                    $ JubesX.FaceChange("normal")
                                    ch_v "Я даже не знаю, мне кажется, это очень хлопотно."
                        "Оставлю это, пожалуй, на твое усмотрение.":
                                    $ JubesX.Statup("Love", 80, 10)
                                    if not Player.Male:
                                        ch_v "Нууу, ага, ты права? Ну конечно же права."
                                    else:
                                        ch_v "Нууу, ага, ты прав? Ну конечно же прав."
                                    if ApprovalCheck(JubesX, 900, "LO"):
                                            $ JubesX.Statup("Inbt", 60, 10)
                                            $ JubesX.Todo.append("pubes")
                        "Нет, оставь все как есть.":
                                    if ApprovalCheck(JubesX, 900, "LO"):
                                            $ JubesX.FaceChange("sly")
                                            $ JubesX.Statup("Love", 80, 10)
                                    else:
                                            $ JubesX.FaceChange("angry",Mouth="normal")
                                    $ JubesX.Statup("Inbt", 60, 25)
                                    ch_v "О, пожалуй, тебе решать?"
                                    $ JubesX.Brows = "normal"
                else:
                        $ JubesX.FaceChange("angry",1)
                        $ JubesX.Statup("Love", 40, -20)
                        $ JubesX.Statup("Obed", 50, 25)
                        $ JubesX.Statup("Inbt", 60, -5)
                        ch_v "Ну, конечно!"
            "Как же у тебя там все неопрятно.":
                    $ JubesX.Statup("Love", 90, -30)
                    $ JubesX.Statup("Obed", 50, 25)
                    $ JubesX.Statup("Inbt", 70, -30)
                    $ JubesX.FaceChange("angry",2)
                    if not JubesX.Forced and not ApprovalCheck(JubesX, 900, "LO"):
                            $ JubesX.RecentActions.append("angry")
                            $ JubesX.DailyActions.append("angry")
                            $ JubesX.Statup("Obed", 70, 25)
                    ch_v "Ох, какие дерзкие слова. . ."
            ". . . [[без комментариев]":
                    $ JubesX.Statup("Inbt", 60, 5)
                    $ JubesX.Statup("Obed", 70, 10)
                    if Player.Male:
                            $ JubesX.Statup("Love", 90, -2)

    else:
        $ JubesX.AddWord(1,0,0,0,"bottomless") #$ JubesX.History.append("bottomless")
        if (ApprovalCheck(JubesX, 800) or not Player.Male) and not JubesX.Forced:
                $ JubesX.Statup("Inbt", 60, 5)
                $ JubesX.Statup("Obed", 70, 10)
        else:
                $ JubesX.Statup("Love", 90, -5)
                $ JubesX.Statup("Inbt", 70, -5)
                $ JubesX.FaceChange("angry")
                $ JubesX.Statup("Obed", 70, 15)
    return



# Gwen Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_First_Topless(Silent = 0, TempLine = 0):
    if GwenX.ChestNum() > 1 or GwenX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return
    if GwenX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ GwenX.RecentActions.append("topless")
    $ GwenX.DailyActions.append("topless")
    $ GwenX.DrainWord("no topless")
    $ GwenX.SeenChest += 1
    if GwenX.SeenChest > 1:
            return                  #ends portion if you've already seen them

    $ GwenX.Statup("Inbt", 70, 15)
    if not Silent:
        $ GwenX.FaceChange("sly")
        "Вы впервые видите обнаженную грудь [GwenX.Name_rod]."
        if not Player.Male and "girltalk" not in GwenX.History:
                ch_g "Ох, надеюсь, они тебя не смутят. . ."
        else:
                ch_g "Ох. . . эм. . . нравятся?"
        $ GwenX.Blush = 1
        menu Gwen_First_TMenu:
            extend ""
            "Твои сиськи? Они выглядят великолепно.":
                    $ GwenX.Statup("Love", 90, 20)
                    $ GwenX.Statup("Inbt", 70, 20)
                    $ GwenX.FaceChange("smile",2)
                    pause 0.5
                    $ GwenX.FaceChange("sexy",1,Eyes="down")
                    ch_g "Ха. . . наверное. . ."
                    $ GwenX.FaceChange("smile")
                    $ GwenX.Statup("Love", 40, 20)
            ". . . [[Вы ошеломлены]":
                    $ GwenX.Statup("Love", 90, 10)
                    $ GwenX.Statup("Inbt", 70, 10)
                    ch_g "Впечатлили, да?"
                    $ GwenX.Statup("Love", 40, 10)
            "Эм, ну. . . как бы. . .":
                    $ GwenX.Statup("Love", 90, -30)
                    $ GwenX.Statup("Obed", 60, 25)
                    $ GwenX.Statup("Inbt", 70, -15)
                    $ GwenX.FaceChange("confused",2)
                    ch_g "М?"
                    ch_g "Что ты там мямлишь?"
                    menu:
                        "Они у тебя очень пылкие!":
                                $ GwenX.Statup("Love", 90, 20)
                                $ GwenX.Statup("Obed", 60, -20)
                                $ GwenX.Statup("Inbt", 70, 20)
                                $ GwenX.FaceChange("perplexed",1)
                                ch_g "Ох."
                        "Я. . . эм. . . нет, они великолепны!":
                                $ GwenX.FaceChange("angry",2, Mouth="smile")
                                $ GwenX.Statup("Inbt", 70, 10)
                                ch_g ". . ."
                                ch_g "Я не совсем верю твоим словам."
                        "Ну, у [KittyX.Name_rod] они более упругие, вот и все." if KittyX.SeenChest:
                                $ TempLine = KittyX
                        "Ну, у [EmmaX.Name_rod] они намного больше, вот и все." if EmmaX.SeenChest:
                                $ TempLine = EmmaX
                        "Ну, у [StormX.Name_rod] они намного больше, вот и все." if StormX.SeenChest:
                                $ TempLine = StormX
                        "Мои просто лучше. . ." if Player.Male != 1:
                                $ Templine = "me"

                    if TempLine:
                            $ GwenX.FaceChange("angry")
                            $ GwenX.Mouth = "surprised"
                            $ GwenX.Statup("Love", 90, -10)
                            $ GwenX.Statup("Obed", 80, 30)
                            $ GwenX.Statup("Inbt", 70, -25)
                            ch_g ". . ."
                            $ GwenX.Mouth = "sad"
                            if TempLine in (EmmaX,StormX):
                                    if GwenX.GirlLikeCheck(TempLine) >= 800:
                                        $ GwenX.FaceChange("sly",2,Eyes="side")
                                        $ GwenX.Statup("Obed", 80, 5)
                                        ch_g "Ну, они были так нарисованы. . ."
                                        $ GwenX.GirlLikeUp(TempLine,20)
                                    elif GwenX.GirlLikeCheck(TempLine) >= 700:
                                        $ GwenX.Eyes = "side"
                                        $ GwenX.Statup("Obed", 80, 5)
                                        ch_g "Я выгляжу так, будто меня привлекает энергия \"большой мамочки\"?. . ."
                                    else:
                                        $ GwenX.GirlLikeUp(TempLine,-50)
                                        $ TempLine = "bad"

                            elif TempLine == KittyX:
                                    if GwenX.LikeKitty >= 800:
                                        $ GwenX.FaceChange("sly",2,Eyes="side")
                                        $ GwenX.Statup("Obed", 80, 5)
                                        ch_g ". . . они чертовски милые. . ."
                                        $ GwenX.LikeKitty += 20
                                    elif GwenX.LikeKitty >= 700:
                                        $ GwenX.Eyes = "side"
                                        $ GwenX.Statup("Obed", 80, 5)
                                        ch_g "Ага. . ."
                                    else:
                                        $ GwenX.LikeKitty -= 50
                                        $ TempLine = "bad"
                            elif TempLine == "me":
                                    $ GwenX.Statup("Obed", 80, 5)
                                    if ApprovalCheck(GwenX, 800):
                                        $ GwenX.FaceChange("sly",2,Eyes="side")
                                        $ GwenX.Statup("Obed", 70, 5)
                                        ch_g ". . . Хорошо, зато честно. . ."
                                    else:
                                        $ TempLine = "bad"

                            if TempLine == "bad":
                                    $ GwenX.Statup("Love", 90, -20)
                                    if not Player.Male:
                                        ch_g "Но все же, почему ты так -сказала-?"
                                    else:
                                        ch_g "Но все же, почему ты так -сказал-?"
                                    $ GwenX.OutfitChange()
                                    $ GwenX.RecentActions.append("no topless")
                                    $ GwenX.DailyActions.append("no topless")
                                    $ GwenX.RecentActions.append("angry")
                                    $ GwenX.DailyActions.append("angry")
            ". . . [[без комментариев]":
                    $ GwenX.FaceChange("angry",1)
                    $ GwenX.Statup("Inbt", 60, 3)
                    $ GwenX.Statup("Obed", 70, 12)
                    if Player.Male:
                            $ GwenX.Statup("Love", 90, -3)


    else:
            $ GwenX.AddWord(1,0,0,0,"topless") #$ GwenX.History.append("topless")
            if (ApprovalCheck(GwenX, 800) or not Player.Male) and not GwenX.Forced:                #if she's not forced and happy about it
                    $ GwenX.Statup("Inbt", 70, 5)
                    $ GwenX.Statup("Obed", 70, 10)
            else:                                                           #if she's not happy about it
                    $ GwenX.Statup("Love", 90, -5)
                    $ GwenX.Statup("Inbt", 70, -5)
                    $ GwenX.FaceChange("angry")
                    $ GwenX.Statup("Obed", 70, 10)
    return


label Gwen_First_Bottomless(Silent = 0):
    if GwenX.PantiesNum() > 1 or GwenX.PantsNum() > 2 or GwenX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if GwenX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ GwenX.RecentActions.append("bottomless")
    $ GwenX.DailyActions.append("bottomless")
    $ GwenX.DrainWord("no bottomless")
    $ GwenX.SeenPussy += 1
    if GwenX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ GwenX.Statup("Inbt", 80, 30)
    $ GwenX.Statup("Obed", 70, 10)
    if not Silent:
        $ GwenX.FaceChange("sly")
        if GwenX.Pubes:
                "Вы ловите себя на том, что пялитесь на пушистую киску [GwenX.Name_rod]."
        else:
                "Вы ловите себя на том, что пялитесь на голую киску [GwenX.Name_rod]."
        menu Gwen_First_BMenu:
            extend ""
            "Какая милая. . .":
                    $ GwenX.Statup("Love", 90, 20)
                    $ GwenX.Statup("Inbt", 60, 25)
                    $ GwenX.FaceChange("surprised",2)
                    ch_g "!!!"
                    $ GwenX.FaceChange("smile",1)
                    ch_g "Эм. . . ладно. . . "
                    $ GwenX.Statup("Love", 40, 20)
            "Смотрю, у тебя там все так естественно." if GwenX.Pubes:
                $ GwenX.FaceChange("confused",2)
                ch_g "Эм. . . ага?"
                if ApprovalCheck(GwenX, 700, "LO"):
                    $ GwenX.FaceChange("bemused",1)
                    menu:
                        ch_g "Тебе. . . нравятся гладкие?"
                        "Да":
                            if ApprovalCheck(GwenX, 900, "LO"):
                                    $ GwenX.Statup("Obed", 50, 30)
                                    $ GwenX.Statup("Inbt", 60, 25)
                                    ch_g "Хорошо. . ."
                                    $ GwenX.Todo.append("shave")
                            else:
                                    $ GwenX.FaceChange("normal")
                                    ch_g "Мне всегда казалось, что это очень хлопотно."
                        "Оставлю это, пожалуй, на твое усмотрение.":
                                    $ GwenX.Statup("Love", 80, 10)
                                    $ GwenX.FaceChange("perplexed",1)
                                    ch_g ". . . спасибо?"
                                    if ApprovalCheck(GwenX, 900, "LO"):
                                            $ GwenX.Statup("Inbt", 60, 10)
                                            $ GwenX.Todo.append("pubes")
                        "Нет, оставь все как есть.":
                                    if ApprovalCheck(GwenX, 900, "LO"):
                                            $ GwenX.FaceChange("sly")
                                            $ GwenX.Statup("Love", 80, 10)
                                            ch_g "Думаю, я должна подыграть. . ."
                                    else:
                                            $ GwenX.FaceChange("angry",Mouth="normal")
                                            ch_g "Кто тебя спрашивал?"
                                    $ GwenX.Statup("Inbt", 60, 25)
                                    $ GwenX.Brows = "normal"
                else:
                        $ GwenX.FaceChange("angry",1)
                        $ GwenX.Statup("Love", 40, -20)
                        $ GwenX.Statup("Obed", 50, 25)
                        $ GwenX.Statup("Inbt", 60, -5)
                        ch_g "Это тебя не касается!"
            "Как же у тебя там все неопрятно.":
                    $ GwenX.Statup("Love", 90, -30)
                    $ GwenX.Statup("Obed", 50, 25)
                    $ GwenX.Statup("Inbt", 70, -30)
                    $ GwenX.FaceChange("angry",2)
                    if not GwenX.Forced and not ApprovalCheck(GwenX, 900, "LO"):
                            $ GwenX.RecentActions.append("angry")
                            $ GwenX.DailyActions.append("angry")
                            $ GwenX.Statup("Obed", 70, 25)
                    ch_g "Ну извини!"
            ". . . [[без комментариев]":
                    $ GwenX.Statup("Inbt", 60, 5)
                    $ GwenX.Statup("Obed", 70, 10)
                    if Player.Male:
                            $ GwenX.Statup("Love", 90, -2)

    else:
        $ GwenX.AddWord(1,0,0,0,"bottomless") #$ GwenX.History.append("bottomless")
        if (ApprovalCheck(GwenX, 800) or not Player.Male) and not GwenX.Forced:
                $ GwenX.Statup("Inbt", 60, 5)
                $ GwenX.Statup("Obed", 70, 10)
        else:
                $ GwenX.Statup("Love", 90, -5)
                $ GwenX.Statup("Inbt", 70, -5)
                $ GwenX.FaceChange("angry")
                $ GwenX.Statup("Obed", 70, 15)
    return



# Betsy Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Betsy_First_Topless(Silent = 0, TempLine = 0):
    if BetsyX.ChestNum() > 1 or BetsyX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return
    if BetsyX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ BetsyX.RecentActions.append("topless")
    $ BetsyX.DailyActions.append("topless")
    $ BetsyX.DrainWord("no topless")
    $ BetsyX.SeenChest += 1
    if BetsyX.SeenChest > 1:
            return                  #ends portion if you've already seen them

    $ BetsyX.Statup("Inbt", 70, 15)
    if not Silent:
        $ BetsyX.FaceChange("sly")
        "Вы впервые видите обнаженную грудь [BetsyX.Name_rod]."
        if not Player.Male and "girltalk" not in BetsyX.History:
                ch_b "Прелестные, правда?"
        else:
                ch_b "Итак. . . как они тебе?"
        $ BetsyX.Blush = 1
        menu Betsy_First_TMenu:
            extend ""
            "Твои сиськи? Они выглядят великолепно.":
                    $ BetsyX.Statup("Love", 90, 20)
                    $ BetsyX.Statup("Inbt", 70, 20)
                    $ BetsyX.FaceChange("smile",2)
                    pause 0.5
                    $ BetsyX.FaceChange("sexy",1,Eyes="down")
                    ch_b "Пожалуй."
                    $ BetsyX.FaceChange("smile")
                    $ BetsyX.Statup("Love", 40, 20)
            ". . . [[Вы ошеломлены]":
                    $ BetsyX.Statup("Love", 90, 10)
                    $ BetsyX.Statup("Inbt", 70, 10)
                    ch_b "Мне кажется, они лишили тебя дара речи."
                    $ BetsyX.Statup("Love", 40, 10)
            "Эм, ну. . . как бы. . .":
                    $ BetsyX.Statup("Love", 90, -30)
                    $ BetsyX.Statup("Obed", 60, 25)
                    $ BetsyX.Statup("Inbt", 70, -15)
                    $ BetsyX.FaceChange("confused",2)
                    ch_b "Что?"
                    menu:
                        "Они у тебя очень пылкие!":
                                $ BetsyX.Statup("Love", 90, 20)
                                $ BetsyX.Statup("Obed", 60, -20)
                                $ BetsyX.Statup("Inbt", 70, 20)
                                $ BetsyX.FaceChange("perplexed",1)
                                ch_b "Полностью с тобой согласна. . ."
                        "Я. . . эм. . . нет, они великолепны!":
                                $ BetsyX.FaceChange("angry",2, Mouth="smile")
                                $ BetsyX.Statup("Inbt", 70, 10)
                                ch_b ". . ."
                                ch_b "Конечно, [BetsyX.Petname]."
                        "Ну, у [KittyX.Name_rod] они более упругие, вот и все." if KittyX.SeenChest:
                                $ TempLine = KittyX
                        "Ну, у [EmmaX.Name_rod] они намного больше, вот и все." if EmmaX.SeenChest:
                                $ TempLine = EmmaX
                        "Ну, у [StormX.Name_rod] они намного больше, вот и все." if StormX.SeenChest:
                                $ TempLine = StormX
                        "Мои просто лучше. . ." if Player.Male != 1:
                                $ Templine = "me"

                    if TempLine:
                            $ BetsyX.FaceChange("angry")
                            $ BetsyX.Mouth = "surprised"
                            $ BetsyX.Statup("Love", 90, -10)
                            $ BetsyX.Statup("Obed", 80, 30)
                            $ BetsyX.Statup("Inbt", 70, -25)
                            ch_b ". . ."
                            $ BetsyX.Mouth = "sad"
                            if TempLine in (EmmaX,StormX):
                                    if BetsyX.GirlLikeCheck(TempLine) >= 800:
                                        $ BetsyX.FaceChange("sly",2,Eyes="side")
                                        $ BetsyX.Statup("Obed", 80, 5)
                                        ch_b "Они у нее просто великолепны. . ."
                                        $ BetsyX.GirlLikeUp(TempLine,20)
                                    elif BetsyX.GirlLikeCheck(TempLine) >= 700:
                                        $ BetsyX.Eyes = "side"
                                        $ BetsyX.Statup("Obed", 80, 5)
                                        ch_b "Что есть, то есть. . ."
                                    else:
                                        $ BetsyX.GirlLikeUp(TempLine,-50)
                                        $ TempLine = "bad"

                            elif TempLine == KittyX:
                                    if BetsyX.LikeKitty >= 800:
                                        $ BetsyX.FaceChange("sly",2,Eyes="side")
                                        $ BetsyX.Statup("Obed", 80, 5)
                                        ch_b ". . . Пожалуй, что так. . ."
                                        $ BetsyX.LikeKitty += 20
                                    elif BetsyX.LikeKitty >= 700:
                                        $ BetsyX.Eyes = "side"
                                        $ BetsyX.Statup("Obed", 80, 5)
                                        ch_b "Что есть, то есть. . ."
                                    else:
                                        $ BetsyX.LikeKitty -= 50
                                        $ TempLine = "bad"
                            elif TempLine == "me":
                                    $ BetsyX.Statup("Obed", 80, 5)
                                    if ApprovalCheck(BetsyX, 800):
                                        $ BetsyX.FaceChange("sly",2,Eyes="side")
                                        $ BetsyX.Statup("Obed", 70, 5)
                                        ch_b ". . . Пожалуй, с этим я поспорить не могу. . ."
                                    else:
                                        $ TempLine = "bad"

                            if TempLine == "bad":
                                    $ BetsyX.Statup("Love", 90, -20)
                                    ch_b "Это было довольно бестактно с твоей стороны."
                                    $ BetsyX.OutfitChange()
                                    $ BetsyX.RecentActions.append("no topless")
                                    $ BetsyX.DailyActions.append("no topless")
                                    $ BetsyX.RecentActions.append("angry")
                                    $ BetsyX.DailyActions.append("angry")
            ". . . [[без комментариев]":
                    $ BetsyX.FaceChange("angry",1)
                    $ BetsyX.Statup("Inbt", 60, 3)
                    $ BetsyX.Statup("Obed", 70, 12)
                    if Player.Male:
                            $ BetsyX.Statup("Love", 90, -3)


    else:
            $ BetsyX.AddWord(1,0,0,0,"topless") #$ BetsyX.History.append("topless")
            if (ApprovalCheck(BetsyX, 800) or not Player.Male) and not BetsyX.Forced:                #if she's not forced and happy about it
                    $ BetsyX.Statup("Inbt", 70, 5)
                    $ BetsyX.Statup("Obed", 70, 10)
            else:                                                           #if she's not happy about it
                    $ BetsyX.Statup("Love", 90, -5)
                    $ BetsyX.Statup("Inbt", 70, -5)
                    $ BetsyX.FaceChange("angry")
                    $ BetsyX.Statup("Obed", 70, 10)
    return


label Betsy_First_Bottomless(Silent = 0):
    if BetsyX.PantiesNum() > 1 or BetsyX.PantsNum() > 2 or BetsyX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if BetsyX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ BetsyX.RecentActions.append("bottomless")
    $ BetsyX.DailyActions.append("bottomless")
    $ BetsyX.DrainWord("no bottomless")
    $ BetsyX.SeenPussy += 1
    if BetsyX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ BetsyX.Statup("Inbt", 80, 30)
    $ BetsyX.Statup("Obed", 70, 10)
    if not Silent:
        $ BetsyX.FaceChange("sly")
        if BetsyX.Pubes:
                "Вы ловите себя на том, что пялитесь на пушистую киску [BetsyX.Name_rod]."
        else:
                "Вы ловите себя на том, что пялитесь на гладкую киску [BetsyX.Name_rod]."
        menu Betsy_First_BMenu:
            extend ""
            "Какая милая. . .":
                    $ BetsyX.Statup("Love", 90, 20)
                    $ BetsyX.Statup("Inbt", 60, 25)
                    $ BetsyX.FaceChange("surprised",2)
                    ch_b "!!"
                    $ BetsyX.FaceChange("smile",1)
                    ch_b "Ох, эм, твоя правда. . . "
                    $ BetsyX.Statup("Love", 40, 20)
            "Смотрю, у тебя там все так естественно." if BetsyX.Pubes:
                $ BetsyX.FaceChange("confused",2)
                ch_b "Да, так и есть."
                if ApprovalCheck(BetsyX, 700, "LO"):
                    $ BetsyX.FaceChange("bemused",1)
                    menu:
                        ch_b "Ты предпочитаешь побритые?"
                        "Да":
                            if ApprovalCheck(BetsyX, 900, "LO"):
                                    $ BetsyX.Statup("Obed", 50, 30)
                                    $ BetsyX.Statup("Inbt", 60, 25)
                                    ch_b "Что ж, если тебе больше нравятся такие. . ."
                                    $ BetsyX.Todo.append("shave")
                            else:
                                    $ BetsyX.FaceChange("normal")
                                    ch_b "Мне довольно сложно постоянно следить за ней."
                        "Оставлю это, пожалуй, на твое усмотрение.":
                                    $ BetsyX.Statup("Love", 80, 10)
                                    ch_b "Замечательно."
                                    if ApprovalCheck(BetsyX, 900, "LO"):
                                            $ BetsyX.Statup("Inbt", 60, 10)
                                            $ BetsyX.Todo.append("pubes")
                        "Нет, оставь все как есть.":
                                    if ApprovalCheck(BetsyX, 900, "LO"):
                                            $ BetsyX.FaceChange("sly")
                                            $ BetsyX.Statup("Love", 80, 10)
                                    else:
                                            $ BetsyX.FaceChange("angry",Mouth="normal")
                                    $ BetsyX.Statup("Inbt", 60, 25)
                                    ch_b "Значит, я получила твое одобрение?"
                                    $ BetsyX.Brows = "normal"
                else:
                        $ BetsyX.FaceChange("angry",1)
                        $ BetsyX.Statup("Love", 40, -20)
                        $ BetsyX.Statup("Obed", 50, 25)
                        $ BetsyX.Statup("Inbt", 60, -5)
                        ch_b "-мне кажется, это тебя не касается."
            "Как же у тебя там все неопрятно.":
                    $ BetsyX.Statup("Love", 90, -30)
                    $ BetsyX.Statup("Obed", 50, 25)
                    $ BetsyX.Statup("Inbt", 70, -30)
                    $ BetsyX.FaceChange("angry",2)
                    if not BetsyX.Forced and not ApprovalCheck(BetsyX, 900, "LO"):
                            $ BetsyX.RecentActions.append("angry")
                            $ BetsyX.DailyActions.append("angry")
                            $ BetsyX.Statup("Obed", 70, 25)
                    ch_b "\"неопрятно?!\""
                    ch_b "Как грубо!"
            ". . . [[без комментариев]":
                    $ BetsyX.Statup("Inbt", 60, 5)
                    $ BetsyX.Statup("Obed", 70, 10)
                    if Player.Male:
                            $ BetsyX.Statup("Love", 90, -2)

    else:
        $ BetsyX.AddWord(1,0,0,0,"bottomless") #$ BetsyX.History.append("bottomless")
        if (ApprovalCheck(BetsyX, 800) or not Player.Male) and not BetsyX.Forced:
                $ BetsyX.Statup("Inbt", 60, 5)
                $ BetsyX.Statup("Obed", 70, 10)
        else:
                $ BetsyX.Statup("Love", 90, -5)
                $ BetsyX.Statup("Inbt", 70, -5)
                $ BetsyX.FaceChange("angry")
                $ BetsyX.Statup("Obed", 70, 15)
    return


# Doreen Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Doreen_First_Topless(Silent = 0, TempLine = 0):
    if DoreenX.ChestNum() > 1 or DoreenX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return
    if DoreenX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ DoreenX.RecentActions.append("topless")
    $ DoreenX.DailyActions.append("topless")
    $ DoreenX.DrainWord("no topless")
    $ DoreenX.SeenChest += 1
    if DoreenX.SeenChest > 1:
            return                  #ends portion if you've already seen them

    $ DoreenX.Statup("Inbt", 70, 15)
    if not Silent:
        $ DoreenX.FaceChange("bemused",2,Eyes="side")
        "Вы впервые видите обнаженную грудь [DoreenX.Name_rod]."
        if not Player.Male and "girltalk" not in DoreenX.History:
                ch_d "Что думаешь?"
        else:
                ch_d "Что ж, эм. . . как они тебе?"
        $ DoreenX.Blush = 1
        menu Doreen_First_TMenu:
            extend ""
            "Они выглядят великолепно.":
                    $ DoreenX.Statup("Love", 90, 20)
                    $ DoreenX.Statup("Inbt", 70, 20)
                    $ DoreenX.FaceChange("smile",2)
                    pause 0.5
                    $ DoreenX.FaceChange("sexy",1,Eyes="down")
                    ch_d "Оу, спасибо!"
                    $ DoreenX.FaceChange("smile")
                    $ DoreenX.Statup("Love", 40, 20)
            ". . . [[Вы ошеломлены]":
                    $ DoreenX.Statup("Love", 90, 10)
                    $ DoreenX.Statup("Inbt", 70, 10)
                    ch_d "Они. . . выглядят странно?"
                    $ DoreenX.Statup("Love", 40, 10)
            "Эм, ну. . . как бы. . .":
                    $ DoreenX.Statup("Love", 90, -30)
                    $ DoreenX.Statup("Obed", 60, 25)
                    $ DoreenX.Statup("Inbt", 70, -15)
                    $ DoreenX.FaceChange("confused",2)
                    ch_d "Что?"
                    menu:
                        "Они у тебя очень пылкие!":
                                $ DoreenX.Statup("Love", 90, 20)
                                $ DoreenX.Statup("Obed", 60, -20)
                                $ DoreenX.Statup("Inbt", 70, 20)
                                $ DoreenX.FaceChange("perplexed",1)
                                ch_d "Я в этом не уверена. . ."
                        "Я. . . эм. . . нет, они великолепны!":
                                $ DoreenX.FaceChange("angry",2, Mouth="smile")
                                $ DoreenX.Statup("Inbt", 70, 10)
                                ch_d ". . ."
                                ch_d "Наверное, [DoreenX.Petname]."
                        "Ну, у [KittyX.Name_rod] они более упругие, вот и все." if KittyX.SeenChest:
                                $ TempLine = KittyX
                        "Ну, у [EmmaX.Name_rod] они намного больше, вот и все." if EmmaX.SeenChest:
                                $ TempLine = EmmaX
                        "Ну, у [StormX.Name_rod] они намного больше, вот и все." if StormX.SeenChest:
                                $ TempLine = StormX
                        "Мои просто лучше. . ." if Player.Male != 1:
                                $ Templine = "me"

                    if TempLine:
                            $ DoreenX.FaceChange("angry")
                            $ DoreenX.Mouth = "surprised"
                            $ DoreenX.Statup("Love", 90, -10)
                            $ DoreenX.Statup("Obed", 80, 30)
                            $ DoreenX.Statup("Inbt", 70, -25)
                            ch_d ". . ."
                            $ DoreenX.FaceChange("sadside")
                            if TempLine in (EmmaX,StormX):
                                    if DoreenX.GirlLikeCheck(TempLine) >= 800:
                                        $ DoreenX.FaceChange("sly",2,Eyes="side")
                                        $ DoreenX.Statup("Obed", 80, 5)
                                        ch_d "Я не думаю, что это действительно так. . ."
                                        $ DoreenX.GirlLikeUp(TempLine,20)
                                    elif DoreenX.GirlLikeCheck(TempLine) >= 700:
                                        $ DoreenX.Eyes = "side"
                                        $ DoreenX.Statup("Obed", 80, 5)
                                        ch_d "Я не думаю, что это действительно так. . ."
                                    else:
                                        $ DoreenX.GirlLikeUp(TempLine,-50)
                                        $ TempLine = "bad"

                            elif TempLine == KittyX:
                                    if DoreenX.LikeKitty >= 800:
                                        $ DoreenX.FaceChange("sly",2,Eyes="side")
                                        $ DoreenX.Statup("Obed", 80, 5)
                                        ch_d ". . . ну, да. . ."
                                        $ DoreenX.LikeKitty += 20
                                    elif DoreenX.LikeKitty >= 700:
                                        $ DoreenX.Eyes = "side"
                                        $ DoreenX.Statup("Obed", 80, 5)
                                        ch_d "Ну, да. . ."
                                    else:
                                        $ DoreenX.LikeKitty -= 50
                                        $ TempLine = "bad"
                            elif TempLine == "me":
                                    $ DoreenX.Statup("Obed", 80, 5)
                                    if ApprovalCheck(DoreenX, 800):
                                        $ DoreenX.FaceChange("sly",2,Eyes="side")
                                        $ DoreenX.Statup("Obed", 70, 5)
                                        ch_d ". . . Думаю, с этим я поспорить не могу. . ."
                                    else:
                                        $ TempLine = "bad"

                            if TempLine == "bad":
                                    $ DoreenX.Statup("Love", 90, -20)
                                    ch_d "Тем не менее, невежливо поднимать такую тему."
                                    $ DoreenX.OutfitChange()
                                    $ DoreenX.RecentActions.append("no topless")
                                    $ DoreenX.DailyActions.append("no topless")
                                    $ DoreenX.RecentActions.append("angry")
                                    $ DoreenX.DailyActions.append("angry")
            ". . . [[без комментариев]":
                    $ DoreenX.FaceChange("angry",1)
                    $ DoreenX.Statup("Inbt", 60, 3)
                    $ DoreenX.Statup("Obed", 70, 12)
                    if Player.Male:
                            $ DoreenX.Statup("Love", 90, -3)


    else:
            $ DoreenX.AddWord(1,0,0,0,"topless") #$ DoreenX.History.append("topless")
            if (ApprovalCheck(DoreenX, 800) or not Player.Male) and not DoreenX.Forced:                #if she's not forced and happy about it
                    $ DoreenX.Statup("Inbt", 70, 5)
                    $ DoreenX.Statup("Obed", 70, 10)
            else:                                                           #if she's not happy about it
                    $ DoreenX.Statup("Love", 90, -5)
                    $ DoreenX.Statup("Inbt", 70, -5)
                    $ DoreenX.FaceChange("angry")
                    $ DoreenX.Statup("Obed", 70, 10)
    return


label Doreen_First_Bottomless(Silent = 0):
    if DoreenX.PantiesNum() > 1 or DoreenX.PantsNum() > 2 or DoreenX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if DoreenX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ DoreenX.RecentActions.append("bottomless")
    $ DoreenX.DailyActions.append("bottomless")
    $ DoreenX.DrainWord("no bottomless")
    $ DoreenX.SeenPussy += 1
    if DoreenX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ DoreenX.Statup("Inbt", 80, 30)
    $ DoreenX.Statup("Obed", 70, 10)
    if not Silent:
        $ DoreenX.FaceChange("sly")
        if DoreenX.Pubes:
                "Вы ловите себя на том, что пялитесь на пушистую киску [DoreenX.Name_rod]."
        else:
                "Вы ловите себя на том, что пялитесь на гладкую киску [DoreenX.Name_rod]."
        menu Doreen_First_BMenu:
            extend ""
            "Какая милая. . .":
                    $ DoreenX.Statup("Love", 90, 20)
                    $ DoreenX.Statup("Inbt", 60, 25)
                    $ DoreenX.FaceChange("surprised",2)
                    ch_d "!!"
                    $ DoreenX.FaceChange("smile",1)
                    ch_d "Ну. . . наверное. . . "
                    $ DoreenX.Statup("Love", 40, 20)
            "Смотрю, у тебя там все так естественно." if DoreenX.Pubes:
                $ DoreenX.FaceChange("confused",2)
                ch_d "Ага, пожалуй."
                if ApprovalCheck(DoreenX, 700, "LO"):
                    $ DoreenX.FaceChange("bemused",1)
                    menu:
                        ch_d "Разве это плохо?"
                        "Да":
                            if ApprovalCheck(DoreenX, 900, "LO"):
                                    $ DoreenX.Statup("Obed", 50, 30)
                                    $ DoreenX.Statup("Inbt", 60, 25)
                                    ch_d "О, хорошо, я все обдумаю. . ."
                                    $ DoreenX.Todo.append("shave")
                            else:
                                    $ DoreenX.FaceChange("normal")
                                    ch_d "I just like it a bit fuzzy."
                        "Оставлю это, пожалуй, на твое усмотрение.":
                                    $ DoreenX.Statup("Love", 80, 10)
                                    ch_d "Как скажешь."
                                    if ApprovalCheck(DoreenX, 900, "LO"):
                                            $ DoreenX.Statup("Inbt", 60, 10)
                                            $ DoreenX.Todo.append("pubes")
                        "Нет, оставь все как есть.":
                                    if ApprovalCheck(DoreenX, 900, "LO"):
                                            $ DoreenX.FaceChange("sly")
                                            $ DoreenX.Statup("Love", 80, 10)
                                    else:
                                            $ DoreenX.FaceChange("angry",Mouth="normal")
                                    $ DoreenX.Statup("Inbt", 60, 25)
                                    ch_d "Я рада, что у меня есть твое одобрение."
                                    $ DoreenX.Brows = "normal"
                else:
                        $ DoreenX.FaceChange("angry",1)
                        $ DoreenX.Statup("Love", 40, -20)
                        $ DoreenX.Statup("Obed", 50, 25)
                        $ DoreenX.Statup("Inbt", 60, -5)
                        ch_d "-не думаю, что это твое дело."
            "Как же у тебя там все неопрятно.":
                    $ DoreenX.Statup("Love", 90, -30)
                    $ DoreenX.Statup("Obed", 50, 25)
                    $ DoreenX.Statup("Inbt", 70, -30)
                    $ DoreenX.FaceChange("angry",2)
                    if not DoreenX.Forced and not ApprovalCheck(DoreenX, 900, "LO"):
                            $ DoreenX.RecentActions.append("angry")
                            $ DoreenX.DailyActions.append("angry")
                            $ DoreenX.Statup("Obed", 70, 25)
                    ch_d "Серьезно?"
                    ch_d "Как можно говорить что-то подобное?!"
            ". . . [[без комментариев]":
                    $ DoreenX.Statup("Inbt", 60, 5)
                    $ DoreenX.Statup("Obed", 70, 10)
                    if Player.Male:
                            $ DoreenX.Statup("Love", 90, -2)

    else:
        $ DoreenX.AddWord(1,0,0,0,"bottomless") #$ DoreenX.History.append("bottomless")
        if (ApprovalCheck(DoreenX, 800) or not Player.Male) and not DoreenX.Forced:
                $ DoreenX.Statup("Inbt", 60, 5)
                $ DoreenX.Statup("Obed", 70, 10)
        else:
                $ DoreenX.Statup("Love", 90, -5)
                $ DoreenX.Statup("Inbt", 70, -5)
                $ DoreenX.FaceChange("angry")
                $ DoreenX.Statup("Obed", 70, 15)
    return


# Wanda Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Wanda_First_Topless(Silent = 0, TempLine = 0):
    if WandaX.ChestNum() > 2 or WandaX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return
    if WandaX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ WandaX.RecentActions.append("topless")
    $ WandaX.DailyActions.append("topless")
    $ WandaX.DrainWord("no topless")
    $ WandaX.SeenChest += 1
    if WandaX.SeenChest > 1:
            return                  #ends portion if you've already seen them

    $ WandaX.Statup("Inbt", 70, 15)
    if not Silent:
        $ WandaX.FaceChange("sly")
        "Вы впервые видите ее обнаженную грудь [WandaX.Name_rod]."
        if not Player.Male and "girltalk" not in WandaX.History:
                ch_w "Милые, правда? . ."
        else:
                ch_w "И вот. . . ты их увидел."
        $ WandaX.Blush = 1
        menu Wanda_First_TMenu:
            extend ""
            "Твои сиськи? Они выглядят великолепно.":
                    $ WandaX.Statup("Love", 90, 20)
                    $ WandaX.Statup("Inbt", 70, 20)
                    $ WandaX.FaceChange("smile",2)
                    pause 0.5
                    $ WandaX.FaceChange("sexy",1,Eyes="down")
                    ch_w "Ох. . . спасибо. . ."
                    $ WandaX.FaceChange("smile")
                    $ WandaX.Statup("Love", 40, 20)
            ". . . [[Вы ошеломлены]":
                    $ WandaX.Statup("Love", 90, 10)
                    $ WandaX.Statup("Inbt", 70, 10)
                    ch_w "Не можешь подобрать слова?"
                    $ WandaX.Statup("Love", 40, 10)
            "Эм, ну. . . как бы. . .":
                    $ WandaX.Statup("Love", 90, -30)
                    $ WandaX.Statup("Obed", 60, 25)
                    $ WandaX.Statup("Inbt", 70, -15)
                    $ WandaX.FaceChange("confused",2)
                    if WandaX.Lust <= 50:
                            ch_w "О, это из-за сосков?"
                    else:
                            ch_w "Не такие большие, как ты ожидал?"
                    menu:
                        "Они у тебя очень упругие!":
                                $ WandaX.Statup("Love", 90, 20)
                                $ WandaX.Statup("Obed", 60, -20)
                                $ WandaX.Statup("Inbt", 70, 20)
                                $ WandaX.FaceChange("perplexed",1)
                                ch_w "О. Ага."
                        "Я. . . эм. . . нет, они великолепны!":
                                $ WandaX.FaceChange("angry",2, Mouth="smile")
                                $ WandaX.Statup("Inbt", 70, 10)
                                ch_w ". . ."
                                ch_w "Ну да, ну да."
                        "Ну, у [KittyX.Name_rod] они более упругие, вот и все." if KittyX.SeenChest:
                                $ TempLine = KittyX
                        "Ну, у [EmmaX.Name_rod] они намного больше, вот и все." if EmmaX.SeenChest:
                                $ TempLine = EmmaX
                        "Ну, у [StormX.Name_rod] они намного больше, вот и все." if StormX.SeenChest:
                                $ TempLine = StormX
                        "Ну, у [DoreenX.Name_rod] они намного больше, вот и все." if DoreenX.SeenChest:
                                $ TempLine = DoreenX
                        "Мои просто лучше. . ." if Player.Male != 1:
                                $ Templine = "me"
                        "Ага, что с ними?" if WandaX.Lust <= 50:
                                $ Templine = "nips"

                    if TempLine:
                            $ WandaX.FaceChange("angry")
                            $ WandaX.Mouth = "surprised"
                            $ WandaX.Statup("Love", 90, -10)
                            $ WandaX.Statup("Obed", 80, 30)
                            $ WandaX.Statup("Inbt", 70, -25)
                            ch_w ". . ."
                            $ WandaX.Mouth = "sad"
                            if TempLine in (EmmaX,StormX,DoreenX):
                                    if WandaX.GirlLikeCheck(TempLine) >= 800:
                                        $ WandaX.FaceChange("sly",2,Eyes="side")
                                        $ WandaX.Statup("Obed", 80, 5)
                                        ch_w "Они у нее очень большие. . ."
                                        $ WandaX.GirlLikeUp(TempLine,20)
                                    elif WandaX.GirlLikeCheck(TempLine) >= 700:
                                        $ WandaX.Eyes = "side"
                                        $ WandaX.Statup("Obed", 80, 5)
                                        ch_w "У меня тоже не такие и маленькие. . ."
                                    else:
                                        $ WandaX.GirlLikeUp(TempLine,-50)
                                        $ TempLine = "bad"

                            elif TempLine == KittyX:
                                    if WandaX.LikeKitty >= 800:
                                        $ WandaX.FaceChange("sly",2,Eyes="side")
                                        $ WandaX.Statup("Obed", 80, 5)
                                        ch_w ". . . Они у нее очень милые. . ."
                                        $ WandaX.LikeKitty += 20
                                    elif WandaX.LikeKitty >= 700:
                                        $ WandaX.Eyes = "side"
                                        $ WandaX.Statup("Obed", 80, 5)
                                        ch_w "Ага. . ."
                                    else:
                                        $ WandaX.LikeKitty -= 50
                                        $ TempLine = "bad"
                            elif TempLine == "me":
                                    $ WandaX.Statup("Obed", 80, 5)
                                    if ApprovalCheck(WandaX, 800):
                                        $ WandaX.FaceChange("sly",2,Eyes="side")
                                        $ WandaX.Statup("Obed", 70, 5)
                                        ch_w ". . . Ладно, они у тебя неплохи. . ."
                                    else:
                                        $ TempLine = "bad"
                            elif TempLine == "nips":
                                    $ WandaX.Statup("Obed", 80, 5)
                                    $ WandaX.FaceChange("sadside",2)
                                    ch_w ". . . они постоянно прячутся. . ."
                                    if ApprovalCheck(WandaX, 700):
                                        $ WandaX.FaceChange("sly",2,Eyes="side")
                                        $ WandaX.Statup("Obed", 70, 5)
                                        ch_w ". . . наверное, они у меня застенчивые. . ."
                                    else:
                                        $ WandaX.Statup("Love", 90, -5)
                                        $ TempLine = "bad"

            ". . . [[без комментариев]":
                    $ WandaX.FaceChange("angry",1)
                    $ WandaX.Statup("Inbt", 60, 3)
                    $ WandaX.Statup("Obed", 70, 12)
                    if Player.Male:
                            $ WandaX.Statup("Love", 90, -3)


        if TempLine == "bad":
                $ WandaX.Statup("Love", 90, -20)
                if not Player.Male:
                    ch_w "Могла бы проявить и побольше поддержки."
                else:
                    ch_w "Мог бы проявить и побольше поддержки."
                $ WandaX.OutfitChange()
                $ WandaX.RecentActions.append("no topless")
                $ WandaX.DailyActions.append("no topless")
                $ WandaX.RecentActions.append("angry")
                $ WandaX.DailyActions.append("angry")
    else:
            $ WandaX.AddWord(1,0,0,0,"topless") #$ WandaX.History.append("topless")
            if (ApprovalCheck(WandaX, 800) or not Player.Male) and not WandaX.Forced:                #if she's not forced and happy about it
                    $ WandaX.Statup("Inbt", 70, 5)
                    $ WandaX.Statup("Obed", 70, 10)
            else:                                                           #if she's not happy about it
                    $ WandaX.Statup("Love", 90, -5)
                    $ WandaX.Statup("Inbt", 70, -5)
                    $ WandaX.FaceChange("angry")
                    $ WandaX.Statup("Obed", 70, 10)
    return


label Wanda_First_Bottomless(Silent = 0):
    if WandaX.PantiesNum() > 1 or WandaX.PantsNum() > 2 or WandaX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if WandaX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ WandaX.RecentActions.append("bottomless")
    $ WandaX.DailyActions.append("bottomless")
    $ WandaX.DrainWord("no bottomless")
    $ WandaX.SeenPussy += 1
    if WandaX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ WandaX.Statup("Inbt", 80, 30)
    $ WandaX.Statup("Obed", 70, 10)
    if not Silent:
        $ WandaX.FaceChange("sly")
        if WandaX.Pubes:
                "Вы ловите себя на том, что пялитесь на пушистую киску [WandaX.Name_rod]."
        else:
                "Вы ловите себя на том, что пялитесь на голую киску [WandaX.Name_rod]."
        menu Wanda_First_BMenu:
            extend ""
            "Какая милая. . .":
                    $ WandaX.Statup("Love", 90, 20)
                    $ WandaX.Statup("Inbt", 60, 25)
                    $ WandaX.FaceChange("surprised",2)
                    ch_w "!!!"
                    $ WandaX.FaceChange("smile",1)
                    ch_w "Хех. . . спасибо? . . "
                    $ WandaX.Statup("Love", 40, 20)
            "Смотрю, у тебя там все так естественно." if WandaX.Pubes:
                $ WandaX.FaceChange("confused",2)
                ch_w "Да?"
                if ApprovalCheck(WandaX, 700, "LO"):
                    $ WandaX.FaceChange("bemused",1)
                    menu:
                        ch_w "Значит, ты предпочитаешь бритые?"
                        "Да":
                            if ApprovalCheck(WandaX, 900, "LO"):
                                    $ WandaX.Statup("Obed", 50, 30)
                                    $ WandaX.Statup("Inbt", 60, 25)
                                    ch_w "Хех. . . я могу это исправить. . ."
                                    $ WandaX.Todo.append("shave")
                            else:
                                    $ WandaX.FaceChange("normal")
                                    ch_w "Это слишком хлопотно."
                        "Оставлю это, пожалуй, на твое усмотрение.":
                                    $ WandaX.Statup("Love", 80, 10)
                                    $ WandaX.FaceChange("perplexed",1)
                                    ch_w ". . . да?"
                                    if ApprovalCheck(WandaX, 900, "LO"):
                                            $ WandaX.Statup("Inbt", 60, 10)
                                            $ WandaX.Todo.append("pubes")
                        "Нет, оставь все как есть.":
                                    if ApprovalCheck(WandaX, 900, "LO"):
                                            $ WandaX.FaceChange("sly")
                                            $ WandaX.Statup("Love", 80, 10)
                                            ch_w ". . . ладно?"
                                    else:
                                            $ WandaX.FaceChange("angry",Mouth="normal")
                                            ch_w "Тебя это разве касается?"
                                    $ WandaX.Statup("Inbt", 60, 25)
                                    $ WandaX.Brows = "normal"
                else:
                        $ WandaX.FaceChange("angry",1)
                        $ WandaX.Statup("Love", 40, -20)
                        $ WandaX.Statup("Obed", 50, 25)
                        $ WandaX.Statup("Inbt", 60, -5)
                        ch_w "Я не хочу об этом говорить."
            "Как же у тебя там все неопрятно.":
                    $ WandaX.Statup("Love", 90, -30)
                    $ WandaX.Statup("Obed", 50, 25)
                    $ WandaX.Statup("Inbt", 70, -30)
                    $ WandaX.FaceChange("angry",2)
                    if not WandaX.Forced and not ApprovalCheck(WandaX, 900, "LO"):
                            $ WandaX.RecentActions.append("angry")
                            $ WandaX.DailyActions.append("angry")
                            $ WandaX.Statup("Obed", 70, 25)
                    if Player.Male:
                        ch_w "Пошел ты!"
                    else:
                        ch_w "Пошла ты!"
            ". . . [[без комментариев]":
                    $ WandaX.Statup("Inbt", 60, 5)
                    $ WandaX.Statup("Obed", 70, 10)
                    if Player.Male:
                            $ WandaX.Statup("Love", 90, -2)

    else:
        $ WandaX.AddWord(1,0,0,0,"bottomless") #$ WandaX.History.append("bottomless")
        if (ApprovalCheck(WandaX, 800) or not Player.Male) and not WandaX.Forced:
                $ WandaX.Statup("Inbt", 60, 5)
                $ WandaX.Statup("Obed", 70, 10)
        else:
                $ WandaX.Statup("Love", 90, -5)
                $ WandaX.Statup("Inbt", 70, -5)
                $ WandaX.FaceChange("angry")
                $ WandaX.Statup("Obed", 70, 15)
    return

# End First Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# End Undressing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wardrobe Remove / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Wardrobe_Remove(Girl=Ch_Focus,Check=0,Fail=0): #rkeljsvgbdw
        #"Why don't you go with no [RogueX.Over]?" if RogueX.Over:
        # if Check = 0, top; Check = 1, bottoms; Check = 2, both
        # call Wardrobe_Remove(Girl)
        $ Girl.FaceChange("bemused", 1)

        if Girl.Over in ("towel","dress") or Girl.Legs == "dress":
                #Auto=sets to 2 if the girl's wearing a double outfit
                $ Check = 2
        $ Line = "" #sets it in case she does both things
        if Check:
                #if the check is below the waist, do this
                if Girl.SeenPanties and Girl.Panties and ApprovalCheck(Girl, 500, TabM=5):
                        #She's got panties on
                        pass #ch_r "Sure."
                elif Girl.SeenPussy and ApprovalCheck(Girl, 900, TabM=4):
                        #You've seen the goods and she's ok with it
                        pass #ch_r "Sure."
                elif Girl.Panties and ApprovalCheck(Girl, 1300, TabM=2):
                        #might pass in public if she's less shy
                        pass #ch_r "Well, I suppose if it's for you. . ."
                elif ApprovalCheck(Girl, 700) and not Girl.Panties:
                    #says she has no panties on, fix that?
                    call NoPanties(Girl) #Rogue_NoPantiesOn
                    $ Line = " также"
                    if not _return and not ApprovalCheck(Girl, 1500, TabM=4):
                        $ Fail = 1
                else:
                        #she fails all checks related to her pussy
                        $ Fail = 1
        if not Fail and Check != 1:
                #if the check is above the waist, and she passed through the previous screen, do this
                if (Girl.Chest or Girl.SeenChest) and ApprovalCheck(Girl, 600, TabM=3):
                        #wearing a bra or you've seen her chest already
                        pass #ch_r "Sure."
                elif ApprovalCheck(Girl, 600, TabM=0):
                    #says she has no bra on, fix that?
                    call NoBra(Girl) #Rogue_NoBra #fix
                    if not _return:
                        #you insisted, and she's not up for it, so it falls though
                        $ Fail = 1
                else:
                        #she fails all checks related to her tits
                        $ Fail = 1
        $ Line  = 0
        if Fail:
                #she didn't agree initially, so bring up a dressing screen
                call Display_DressScreen(Girl)
                if not _return:
                        #you didn't allow for a dressing screen
                        if Girl in (EmmaX,StormX,BetsyX):
                                call AnyLine(Girl,"Жаль. . .")
                        else:
                                call AnyLine(Girl,"Извини. . .")
                        return          #back to clothing choice #jump Rogue_Clothes
        #if it succeeds all checks
        if Check != 1 and Girl.Over:
                #if she has a top and check is top or both, she removes it
                $ Line = get_clothing_name(Girl.Over_key, vin)
                $ Girl.Over = 0
                "Она сбрасывает [Line]."
        if Check and Girl.Legs:
                #if she has bottoms and check is bottoms or both, she removes it
            if Girl.Legs:
                $ Line = get_clothing_name(Girl.Legs_key, vin)
                $ Girl.Legs = 0
                "Она стягивает [Line]."
        $ Line = 0

        if not renpy.showing('DressScreen'):
                if Girl.Panties:
                        $ Girl.SeenPanties = 1
                call Girl_First_Topless(Girl)
                call Girl_First_Bottomless(Girl)
        return

label NoPanties(Girl=Ch_Focus): #rkeljsvgbdw
        if Girl is RogueX:
                ch_r "Знаешь, на мне ведь нет трусиков. . ."
        elif Girl is KittyX:
                ch_k "На мне[KittyX.like]нет трусиков."
        elif Girl is EmmaX:
                if not Player.Male:
                    ch_e "Ты должна знать. . ."
                else:
                    ch_e "Ты должен знать. . ."
                $ EmmaX.FaceChange("sly")
                ch_e "На мне сейчас нет трусиков. . ."
        elif Girl is LauraX:
                ch_l "Я сегодня без трусиков."
        elif Girl is JeanX:
                ch_j "На мне сейчас нет трусиков."
        elif Girl is StormX:
                ch_s "Я сегодня не надела трусики."
        elif Girl is JubesX:
                ch_v "На мне так-то нет трусиков."
        elif Girl is GwenX:
                ch_g "На мне сейчас так-то нет трусиков. . ."
        elif Girl is BetsyX:
                ch_b "Боюсь, я сейчас без трусиков. . ."
        elif Girl is DoreenX:
                ch_d "Я, эм. . . не надела сегодня трусики. . ."
        elif Girl is WandaX:
                ch_w "На мне сейчас нет трусиков. . ."
        menu:
            extend ""
            "Тогда надень. . .":
                        if ApprovalCheck(Girl, 1500, TabM=4) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM=4)):
                                $ Girl.Blush = 1
                                if Girl is RogueX:
                                        ch_r "В этом нет нужды. . ."
                                elif Girl is KittyX:
                                        ch_k "Я не сказала, что это меня беспокоит. . ."
                                elif Girl is EmmaX:
                                        ch_e "Я не сказала, что это меня беспокоит. . ."
                                elif Girl is LauraX:
                                        ch_l "Нет, это прикольно. . ."
                                elif Girl is JeanX:
                                        ch_j "Нет, меня и так все устраивает. . ."
                                elif Girl is StormX:
                                        ch_s "Нет, меня и так все устраивает. . ."
                                elif Girl is JubesX:
                                        ch_v "Нет, нет, меня и без них все устраивает. . ."
                                elif Girl is GwenX:
                                        ch_g "Не-а, мне нравится свежесть. . ."
                                elif Girl is BetsyX:
                                        ch_b "Я предпочитаю, когда слегка поддувает. . ."
                                elif Girl is DoreenX:
                                        ch_d "Не знаю, мне без них нравится. . ."
                                elif Girl is WandaX:
                                        ch_w "Да мне и так хорошо. . ."
                        elif Girl is StormX and (StormX.Taboo <= 20 or StormX.HoseNum() >= 5 or StormX in Rules):
                                ch_s "No, it's fine."
                                $ Girl.Blush = 0
                        elif ApprovalCheck(Girl, 700, TabM=4):
                                if Girl is RogueX:
                                        ch_r "Мне нравится эта идея."
                                elif Girl is KittyX:
                                        ch_k "Мне нравится эта идея."
                                elif Girl is EmmaX:
                                        ch_e "Пожалуй, так и сделаю."
                                elif Girl is LauraX:
                                        ch_l "Сейчас что-нибудь подберу."
                                elif Girl is JeanX:
                                        ch_j "Сейчас что-нибудь подберу."
                                elif Girl is StormX:
                                        ch_s "Хорошо."
                                elif Girl is JubesX:
                                        ch_v "Нууу, сейчас что-нибудь найду. . ."
                                elif Girl is GwenX:
                                        ch_g "Сейчас что-нибудь найду."
                                elif Girl is BetsyX:
                                        ch_b "Сейчас что-нибудь подберу."
                                elif Girl is DoreenX:
                                        ch_d "сейчас что-нибудь найду."
                                elif Girl is WandaX:
                                        ch_w "Сейчас что-нибудь найду."
                                if "lace panties" in Girl.Inventory:
                                            $ Girl.Panties  = "lace panties"
                                else:
                                            $ Girl.Panties = Girl.Casual1[6] #sets to default panties
                                if ApprovalCheck(Girl, 1200, TabM=4) and Girl.Legs:
                                        $ Line = get_clothing_name(Girl.Legs_key, vin)
                                        $ Girl.Legs = 0
                                        "Она снимает [Line] и надевает [get_clothing_name(Girl.Panties_key, vin)]."
                                elif Girl is KittyX and Girl.Legs:
                                        "Она достает свои [get_clothing_name(Girl.Panties_key, vin)] и надевает их через [get_clothing_name(Girl.Legs_key, vin)]."
                                elif Girl.Legs in ("skirt","dress","cheer skirt","other skirt","red skirt","blue skirt"):
                                        "Она достает свои [get_clothing_name(Girl.Panties_key, vin)] и надевает их под [get_clothing_name(Girl.Legs_key, vin)]."
                                else:
                                        $ Line = Girl.Legs
                                        $ Girl.Legs = 0
                                        "Она ненадолго отходит, а затем возвращается в [get_clothing_name(Girl.Panties_key, pre)]."
                        else:
                                if Girl is RogueX:
                                        ch_r "Я так не думаю."
                                elif Girl is KittyX:
                                        ch_k "Я так не думаю."
                                elif Girl is EmmaX:
                                        ch_e "Я могла бы, но лучше не буду."
                                elif Girl is LauraX:
                                        ch_l "Я так не думаю."
                                elif Girl is JeanX:
                                        ch_j "Я так не думаю."
                                elif Girl is StormX:
                                        ch_s "Нет, благодарю."
                                elif Girl is JubesX:
                                        ch_v "Это ничего не изменит."
                                elif Girl is GwenX:
                                        ch_g "Я так не думаю."
                                elif Girl is BetsyX:
                                        ch_b "Боюсь, мне лучше отказаться."
                                elif Girl is DoreenX:
                                        ch_d "Я так не думаю."
                                elif Girl is WandaX:
                                        ch_w "Я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(Girl, 1100, "LI", TabM=3) and Girl.Love > Girl.Inbt:
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Да, наверное ты права."
                                        else:
                                            ch_r "Да, наверное ты прав."
                                elif Girl is KittyX:
                                        ch_k "Ну, наверное. . ."
                                elif Girl is EmmaX:
                                        ch_e "Для тебя все что угодно. . ."
                                elif Girl is LauraX:
                                        ch_l "Пожалуй. . ."
                                elif Girl is JeanX:
                                        ch_j "Согласна. . ."
                                elif Girl is StormX:
                                        ch_s "Верно."
                                elif Girl is JubesX:
                                        ch_v "Для тебя? Конечно. . ."
                                elif Girl is GwenX:
                                        ch_g "Ну, если тебе нравится. . ."
                                elif Girl is BetsyX:
                                        ch_b "Пожалуй. . ."
                                elif Girl is DoreenX:
                                        ch_d "Наверное. . ."
                                elif Girl is WandaX:
                                        ch_w "Конечно. . ."
                        elif Girl is StormX and (StormX.Taboo <= 20 or StormX.HoseNum() >= 5 or StormX in Rules):
                                ch_s "Верно."
                        elif ApprovalCheck(Girl, 750, "OI", TabM=3) and Girl.Obed > Girl.Inbt:
                                if Girl is RogueX:
                                        ch_r "Конечно. . ."
                                elif Girl is KittyX:
                                        ch_k "Конечно. . ."
                                elif Girl is EmmaX:
                                        ch_e "Рада, что тебе нравится. . ."
                                elif Girl is LauraX:
                                        ch_l "Конечно. . ."
                                elif Girl is JeanX:
                                        ch_j "Конечно. . ."
                                elif Girl is StormX:
                                        ch_s "Верно. . ."
                                elif Girl is JubesX:
                                        ch_v "Конечно. . ."
                                elif Girl is GwenX:
                                        ch_g "Конечно. . ."
                                elif Girl is BetsyX:
                                        ch_b "Конечно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Конечно. . ."
                                elif Girl is WandaX:
                                        ch_w "Конечно. . ."
                        elif ApprovalCheck(Girl, 500, "I", TabM=3):
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Ооох, какая же ты испорченная."
                                        else:
                                            ch_r "Ооох, какой же ты испорченный."
                                elif Girl is KittyX:
                                        ch_k "Ага. . ."
                                elif Girl is EmmaX:
                                        ch_e "Пожалуй. . ."
                                elif Girl is LauraX:
                                        ch_l "Ага. . ."
                                elif Girl is JeanX:
                                        ch_j "Конечно. . ."
                                elif Girl is StormX:
                                        ch_s "Хорошо. . ."
                                elif Girl is JubesX:
                                        ch_v "Ага. . ."
                                elif Girl is GwenX:
                                        ch_g "Ага. . ."
                                elif Girl is BetsyX:
                                        ch_b "Пожалуй. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ооох. . ."
                                elif Girl is WandaX:
                                        ch_w "Ну ладно. . ."
                        elif ApprovalCheck(Girl, 1400, TabM=3):
                                if Girl is RogueX:
                                        ch_r "Ну ладно."
                                elif Girl is KittyX:
                                        ch_k "Ну ладно."
                                elif Girl is EmmaX:
                                        ch_e "Что ж, ладно."
                                elif Girl is LauraX:
                                        ch_l "Ну ладно."
                                elif Girl is JeanX:
                                        ch_j "Ну ладно."
                                elif Girl is StormX:
                                        ch_s "Что ж, ладно."
                                elif Girl is JubesX:
                                        ch_v "Ну ладно."
                                elif Girl is GwenX:
                                        ch_l "Ну ладно."
                                elif Girl is BetsyX:
                                        ch_b "О, ну хорошо."
                                elif Girl is DoreenX:
                                        ch_d "Ох, ладно."
                                elif Girl is WandaX:
                                        ch_w "Ладно."
                        else:
                                $ Girl.FaceChange("surprised")
                                $ Girl.Brows = "angry"
                                if Girl.Taboo:
                                        if Girl is RogueX:
                                                ch_r "Но не на людях, [Girl.Petname]!"
                                        elif Girl is KittyX:
                                                ch_k "Но не на людях, [KittyX.Petname]!"
                                        elif Girl is EmmaX:
                                                ch_e "Боюсь, я не смогу сделать это на людях."
                                        elif Girl is LauraX:
                                                ch_l "Но не на людях!"
                                        elif Girl is JeanX:
                                                ch_j ". . . но не в данный момент. . ."
                                        elif Girl is StormX:
                                                ch_s "Боюсь, на людях лучше этого не делать."
                                        elif Girl is JubesX:
                                                ch_v "Мы же на людях!"
                                        elif Girl is GwenX:
                                                ch_g "Только не на людях!"
                                        elif Girl is BetsyX:
                                                ch_b "Боюсь, на людях этого делать не стоит!"
                                        elif Girl is DoreenX:
                                                ch_d "Но не на людях! Извини."
                                        elif Girl is WandaX:
                                                ch_w "Прости, но не на людях."
                                else:
                                        if Girl is RogueX:
                                                ch_r "Не настаивай на этом, [RogueX.Petname]."
                                        elif Girl is KittyX:
                                                ch_k "[KittyX.Petname], ты мне не -настолько- нравишься!"
                                        elif Girl is EmmaX:
                                                ch_e "Я бы могла удовлетворить твое желание, но не стану."
                                        elif Girl is LauraX:
                                                if not Player.Male:
                                                    ch_l "[LauraX.Petname], ты не настолько милая!"
                                                else:
                                                    ch_l "[LauraX.Petname], ты не настолько милый!"
                                        elif Girl is JeanX:
                                                ch_j "Ха! Мечтай."
                                        elif Girl is StormX:
                                                ch_s "Боюсь, что я не смогу на это пойти!"
                                        elif Girl is JubesX:
                                                ch_v "Не-а."
                                        elif Girl is GwenX:
                                                if not Player.Male:
                                                    ch_g "[GwenX.Petname], ты не настолько милая!"
                                                else:
                                                    ch_g "[GwenX.Petname], ты не настолько милый!"
                                        elif Girl is BetsyX:
                                                if not Player.Male:
                                                    ch_b "Ты далеко не такая милая, как ты думаешь, [BetsyX.Petname]!"
                                                else:
                                                    ch_b "Ты далеко не такой милый, как ты думаешь, [BetsyX.Petname]!"
                                        elif Girl is DoreenX:
                                                if not Player.Male:
                                                    ch_d "Ты не настолько милая, [DoreenX.Petname]!"
                                                else:
                                                    ch_d "Ты не настолько милый, [DoreenX.Petname]!"
                                        elif Girl is WandaX:
                                                ch_w "Хех, не-а, [WandaX.Petname]!"
                                call expression Girl.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно.":
                        call AnyLine(Girl,"Ладно. . .")
                        $ Line  = 0
                        $ renpy.pop_call()
                        return 0
        return 1
        #End of Girl Panties check


label NoBra(Girl=Ch_Focus): #rkeljsvgbdw
        if Girl is RogueX:
                ch_r "На мне[Line] нет лифчика. . ."
        elif Girl is KittyX:
                ch_k "Под этим у меня[Line] ничего нет. . ."
        elif Girl is EmmaX:
                ch_e "На мне[Line] нет лифчика. . ."
        elif Girl is LauraX:
                ch_l "Под этим у меня[Line] ничего нет. . ."
        elif Girl is JeanX:
                ch_j "На мне[Line] сейчас нет лифчика."
        elif Girl is StormX:
                ch_s "На мне[Line] нет лифчика. . ."
        elif Girl is JubesX:
                ch_v "Я[Line] не надела лифчик. . ."
        elif Girl is GwenX:
                ch_g "Я сегодня[Line] не надела лифчик. . ."
        elif Girl is BetsyX:
                ch_b "Боюсь, я[Line] не надела лифчик. . ."
        elif Girl is DoreenX:
                ch_d "Я[Line] не надела лифчик. . ."
        elif Girl is WandaX:
                ch_w "На мне сейчас[Line] нет лифчика. . ."
        menu:
            extend ""
            "Тогда надень. . .":
                        if Girl is StormX and (StormX in Rules or StormX.Taboo < 20):
                                ch_s "Нет, пожалуй, меня все устраивает, во всяком случае, сейчас."
                        elif (Girl.SeenChest and ApprovalCheck(Girl, 1000, TabM=3)) or ApprovalCheck(Girl, 1200, TabM=4):
                                #she's into it
                                $ Girl.Blush = 2
                                if Girl is RogueX:
                                        ch_r "Меня это совсем не беспокоит. . ."
                                elif Girl is KittyX:
                                        ch_k "-да это не такая уж и проблема. . ."
                                elif Girl is EmmaX:
                                        ch_e "-не то, чтобы меня это сильно волновало. . ."
                                elif Girl is LauraX:
                                        ch_l "-Я не сказала, что меня это беспокоит. . ."
                                elif Girl is JeanX:
                                        ch_j "Ну, не то, чтобы мне это сильно было нужно. . ."
                                elif Girl is StormX:
                                        ch_s "Я совсем не против быть без него. . ."
                                elif Girl is JubesX:
                                        ch_v "О, да я просто предупредила -тебя-. . ."
                                elif Girl is GwenX:
                                        ch_g "-Я не сказала, что меня это беспокоит. . ."
                                elif Girl is BetsyX:
                                        ch_g "-Я- не сказала, что меня это беспокоит. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ну, вообще-то, я не сказала, что меня это беспокоит. . ."
                                elif Girl is WandaX:
                                        ch_w "Честно говоря, меня это не беспокоит. . ."
                                $ Girl.Blush = 1
                        elif ApprovalCheck(Girl, 700, TabM=2):
                                #sexier tops
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Да, наверное ты права."
                                        else:
                                            ch_r "Да, наверное ты прав."
                                elif Girl is KittyX:
                                        ch_k "У меня есть{i}кое-что{/i} на примете."
                                elif Girl is EmmaX:
                                        ch_e "Пожалуй, можно."
                                elif Girl is LauraX:
                                        ch_l "Наверное, я смогу что-нибудь подобрать."
                                elif Girl is JeanX:
                                        ch_j "Думаю, я смогу что-нибудь найти."
                                elif Girl is StormX:
                                        ch_s "Хорошо."
                                elif Girl is JubesX:
                                        ch_v "Нууу, у меня есть кое-что, что я могла бы надеть. . ."
                                elif Girl is GwenX:
                                        ch_g "Наверное, я смогу что-нибудь подобрать."
                                elif Girl is BetsyX:
                                        ch_b "Пожалуй, я могу что-нибудь подобрать."
                                elif Girl is DoreenX:
                                        ch_d "Думаю, я могу что-нибудь подобрать."
                                elif Girl is WandaX:
                                        ch_w "Я что-нибудь подберу."
                                if ApprovalCheck(Girl, 900, TabM=2) and "lace bra" in Girl.Inventory:
                                        $ Girl.Chest  = "lace bra"
                                        "Она достаёт свой кружевной лифчик и надевает его под [get_clothing_name(Girl.Over_key, vin)]."
                                elif ApprovalCheck(Girl, 900, TabM=2) and "lace corset" in Girl.Inventory:
                                        $ Girl.Chest  = "lace corset"
                                        "Она достаёт свой кружевной корсет и надевает его под [get_clothing_name(Girl.Over_key, vin)]."

                                elif Girl is RogueX:
                                        $ Girl.Chest = "bra"
                                        "Она достаёт свой лифчик и надевает его под [get_clothing_name(Girl.Over_key, vin)]."
                                elif Girl is KittyX:
                                        ch_k "Да, наверное, твоя правда."
                                        $ KittyX.Chest = "cami"
                                        "Она достаёт свой ками и надевает его сквозь [get_clothing_name(KittyX.Over_key, vin)]."
                                elif Girl is EmmaX:# and ApprovalCheck(EmmaX, 700, TabM=(3-Public)):
                                        ch_e "Пожалуй, можно."
                                        $ EmmaX.Chest = "corset"
                                        "Она достаёт свой корсет и надевает его под [get_clothing_name(EmmaX.Over_key, vin)]."
                                elif Girl is LauraX and "corset" in LauraX.Inventory:
                                        ch_l "Наверное, я смогу что-нибудь подобрать."
                                        $ LauraX.Chest  = "corset"
                                        "Она достаёт свой корсет и надевает его под [get_clothing_name(LauraX.Over_key, vin)]."
                                elif Girl is LauraX:
                                        ch_l "Ага, пожалуй, так и сделаю."
                                        $ LauraX.Chest = "leather bra"
                                        "Она достаёт свой кожаный лифчик и надевает его под [get_clothing_name(LauraX.Over_key, vin)]."
                                elif Girl is JeanX:
                                        ch_j "Думаю, я смогу что-нибудь подобрать."
                                        $ JeanX.Chest  = "green bra"
                                        "Она достает свой зеленый лифчик и надевает его под [get_clothing_name(JeanX.Over_key, vin)]."
                                elif Girl is StormX:
                                        ch_s "Хорошо."
                                        $ StormX.Chest  = "black bra"
                                        "Она достает свой черный лифчик и надевает его под [get_clothing_name(StormX.Over_key, vin)]."
                                elif Girl is JubesX:
                                        ch_v "Нууу, у меня есть кое-что, что я могла бы надеть. . ."
                                        $ JubesX.Chest = "sports bra"
                                        "Она достает спортивный лифчик и надевает его под [get_clothing_name(JubesX.Over_key, vin)]."
                                elif Girl is GwenX:
                                        $ Girl.Chest = "bra"
                                        "Она достаёт свой лифчик и надевает его под [get_clothing_name(Girl.Over_key, vin)]."
                                elif Girl is BetsyX:
                                        ch_b "Пожалуй, я могу что-нибудь подобрать."
                                        $ BetsyX.Chest = "bra"
                                        "Она достаёт свой лифчик и надевает его под [get_clothing_name(BetsyX.Over_key, vin)]."
                                elif Girl is DoreenX:
                                        ch_d "Думаю, я могу что-нибудь подобрать."
                                        $ DoreenX.Chest = "tan bra"
                                        "Она достает свой коричневый лифчик и надевает его под [get_clothing_name(DoreenX.Over_key, vin)]."
                                elif Girl is WandaX:
                                        ch_w "Я смогу что-нибудь подобрать."
                                        $ WandaX.Chest = "red bra"
                                        "Она достает красный лифчик и надевает его под [get_clothing_name(WandaX.Over_key, vin)]."
                        elif ApprovalCheck(Girl, 600, TabM=2) and Girl not in (JeanX,BetsyX,DoreenX,WandaX):
                                #more modest tops
                                if Girl is RogueX:
                                        $ Girl.Chest = "tank"
                                        "Она достает свою майку и надевает ее под [get_clothing_name(Girl.Over_key, vin)]."
                                elif Girl is KittyX:
                                        ch_k "Да, наверное, твоя правда."
                                        $ KittyX.Chest = "sports bra"
                                        "Она достает спортивный лифчик и надевает его сквозь [get_clothing_name(KittyX.Over_key, vin)]."
                                elif Girl is EmmaX:# and ApprovalCheck(EmmaX, 600, TabM=(3-Public)):
                                        ch_e "Пожалуй, можно."
                                        $ EmmaX.Chest = "sports bra"
                                        "Она достает свой спортивный лифчик и надевает его под [get_clothing_name(EmmaX.Over_key, vin)]."
                                elif Girl is LauraX:
                                        ch_l "Ага, наверное, можно."
                                        $ LauraX.Chest = "leather bra"
                                        "Она достаёт свой кожаный лифчик и надевает его под [get_clothing_name(LauraX.Over_key, vin)]."
                                elif Girl is StormX:
                                        ch_s "Хорошо."
                                        $ StormX.Chest = "tube top"
                                        "Она достает топик и надевает его под [get_clothing_name(StormX.Over_key, vin)]."
                                elif Girl is JubesX:
                                        ch_v "Нууу, у меня есть кое-что, что я могла бы надеть. . ."
                                        $ JubesX.Chest = "sports bra"
                                        "Она достает спортивный лифчик и надевает его под [get_clothing_name(JubesX.Over_key, vin)]."
                                elif Girl is GwenX:
                                        ch_g "Yeah, I guess."
                                        $ GwenX.Chest = "tank"
                                        "Она достает белую майку и надевает ее под [get_clothing_name(GwenX.Over_key, vin)]."
                        else:
                                #no options would work
                                if Girl is RogueX:
                                        ch_r "Я так не думаю."
                                elif Girl is KittyX:
                                        ch_k "Я так не думаю."
                                elif Girl is EmmaX:
                                        ch_e "Да, но я бы предпочла этого не делать."
                                elif Girl is LauraX:
                                        ch_l "Ага, я так не думаю."
                                elif Girl is JeanX:
                                        ch_j "Ага, я так не думаю."
                                elif Girl is StormX:
                                        ch_s "Не думаю, что это было бы уместно."
                                elif Girl is JubesX:
                                        ch_v "Ага, но это не поможет."
                                elif Girl is GwenX:
                                        ch_g "Ага, но мне не хочется."
                                elif Girl is BetsyX:
                                        ch_b "Я так не думаю."
                                elif Girl is DoreenX:
                                        ch_d "Я так не думаю."
                                elif Girl is WandaX:
                                        ch_w "Ага, но я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(Girl, 1100, "LI", TabM=2) and Girl.Love > Girl.Inbt:
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Да, наверное ты права."
                                        else:
                                            ch_r "Да, наверное ты прав."
                                elif Girl is KittyX:
                                        ch_k "Ну, наверное. . ."
                                elif Girl is EmmaX:
                                        ch_e "Для тебя все, что угодно. . ."
                                elif Girl is LauraX:
                                        ch_l "Пожалуй. . ."
                                elif Girl is JeanX:
                                        ch_j "Согласна. . ."
                                elif Girl is StormX:
                                        ch_s "Пожалуй, меня все устраивает, во всяком случае, сейчас."
                                elif Girl is JubesX:
                                        ch_v "Для тебя? Конечно. . ."
                                elif Girl is GwenX:
                                        ch_g "Ну, если тебе хочется посмотреть. . ."
                                elif Girl is BetsyX:
                                        ch_b "Пожалуй. . ."
                                elif Girl is DoreenX:
                                        ch_d "Наверное. . ."
                                elif Girl is WandaX:
                                        ch_w "Конечно. . ."
                        elif Girl is StormX and (StormX in Rules or not StormX.Taboo):
                                ch_s "Пожалуй, меня все устраивает, во всяком случае, сейчас."
                        elif ApprovalCheck(Girl, 700, "OI", TabM=2) and Girl.Obed > Girl.Inbt:
                                if Girl is RogueX:
                                        ch_r "Конечно. . ."
                                elif Girl is KittyX:
                                        ch_k "Конечно. . ."
                                elif Girl is EmmaX:
                                        ch_e "Если ты настаиваешь. . ."
                                elif Girl is LauraX:
                                        ch_l "Конечно. . ."
                                elif Girl is JeanX:
                                        ch_j "Конечно. . ."
                                elif Girl is StormX:
                                        ch_s "Хорошо. . ."
                                elif Girl is JubesX:
                                        ch_v "Конечно. . ."
                                elif Girl is GwenX:
                                        ch_g "Конечно. . ."
                                elif Girl is BetsyX:
                                        ch_b "Конечно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Конечно. . ."
                                elif Girl is WandaX:
                                        ch_w "Конечно. . ."
                        elif ApprovalCheck(Girl, 600, "I", TabM=2):
                                if Girl is RogueX:
                                        ch_r "Ага. . ."
                                elif Girl is KittyX:
                                        ch_k "Ага. . ."
                                elif Girl is EmmaX:
                                        ch_e "Пожалуй, можно. . ."
                                elif Girl is LauraX:
                                        ch_l "Ага. . ."
                                elif Girl is JeanX:
                                        ch_j "Конечно. . ."
                                elif Girl is StormX:
                                        ch_s "Хорошо. . ."
                                elif Girl is JubesX:
                                        ch_v "Ага. . ."
                                elif Girl is GwenX:
                                        ch_g "Ага. . ."
                                elif Girl is BetsyX:
                                        ch_b "Конечно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ладно. . ."
                                elif Girl is WandaX:
                                        ch_w "Ладно. . ."
                        elif ApprovalCheck(Girl, 1300, TabM=2):
                                if Girl is RogueX:
                                        ch_r "Ну ладно."
                                elif Girl is KittyX:
                                        ch_k "Ну ладно."
                                elif Girl is EmmaX:
                                        ch_e "Хорошо."
                                elif Girl is LauraX:
                                        ch_l "Ну ладно."
                                elif Girl is JeanX:
                                        ch_j "Ну ладно."
                                elif Girl is StormX:
                                        ch_s "Хорошо."
                                elif Girl is JubesX:
                                        ch_v "Ну ладно."
                                elif Girl is GwenX:
                                        ch_l "Ну ладно."
                                elif Girl is BetsyX:
                                        ch_b "Ох. ну хорошо."
                                elif Girl is DoreenX:
                                        ch_d "Ну ладно."
                                elif Girl is WandaX:
                                        ch_w "Ладно."
                        else:
                                $ Girl.FaceChange("surprised")
                                $ Girl.Brows = "angry"
                                if Girl.Taboo > 20:
                                        if Girl is RogueX:
                                                ch_r "Но не на людях, [RogueX.Petname]!"
                                        elif Girl is KittyX:
                                                ch_k "Но не на людях, [KittyX.Petname]!"
                                        elif Girl is EmmaX:
                                                ch_e "Боюсь, я не смогу сделать это на людях."
                                        elif Girl is LauraX:
                                                ch_l "Но не на людях!"
                                        elif Girl is JeanX:
                                                ch_j ". . . Но не в данный момент. . ."
                                        elif Girl is StormX:
                                                ch_s "Боюсь, не на людях."
                                        elif Girl is JubesX:
                                                ch_v "Но мы же на людях!"
                                        elif Girl is GwenX:
                                                ch_g "Только не на людях!"
                                        elif Girl is BetsyX:
                                                ch_b "Боюсь, не на людях!"
                                        elif Girl is DoreenX:
                                                ch_d "Но не на людях! Извини."
                                        elif Girl is WandaX:
                                                ch_w "Прости, но не на людях."
                                else:
                                        if Girl is RogueX:
                                                ch_r "Не настаивай на этом, [RogueX.Petname]."
                                        elif Girl is KittyX:
                                                ch_k "Ты мне не -настолько- нравишься, [KittyX.Petname]!"
                                        elif Girl is EmmaX:
                                                ch_e "Я бы могла, но не стану."
                                        elif Girl is LauraX:
                                                if not Player.Male:
                                                    ch_l "Ты не настолько милая, [LauraX.Petname]!"
                                                else:
                                                    ch_l "Ты не настолько милый, [LauraX.Petname]!"
                                        elif Girl is JeanX:
                                                ch_j "Ха! Не для тебя я их растила, [JeanX.Petname]."
                                        elif Girl is StormX:
                                                ch_s "Боюсь, я вынуждена отказаться!"
                                        elif Girl is JubesX:
                                                h_v "Нее."
                                        elif Girl is GwenX:
                                                if not Player.Male:
                                                    ch_g "Ты не настолько милая, [GwenX.Petname]!"
                                                else:
                                                    ch_g "Ты не настолько милый, [GwenX.Petname]!"
                                        elif Girl is BetsyX:
                                                if not Player.Male:
                                                    ch_b "Ты далеко не такая милая, как ты думаешь, [BetsyX.Petname]!"
                                                else:
                                                    ch_b "Ты далеко не такой милый, как ты думаешь, [BetsyX.Petname]!"
                                        elif Girl is DoreenX:
                                                if not Player.Male:
                                                    ch_d "Ты не настолько милая, [DoreenX.Petname]!"
                                                else:
                                                    ch_d "Ты не настолько милый, [DoreenX.Petname]!"
                                        elif Girl is WandaX:
                                                ch_w "Хех, не-а, [WandaX.Petname]!"
                                call expression Girl.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно.":
                        call AnyLine(Girl,"Ладно. . .")
                        $ Line  = 0
                        $ renpy.pop_call()
                        return 0
        return 1
        #End of Girl bra check
# End Wardrobe Remove / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Dressing Screen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Display_DressScreen(Girl=Ch_Focus): #rkeljsvgbdw
        #asks if you're willing to put up a protective dressing screen, XTaboo is the girl's local taboo
        # call Display_DressScreen(Girl)
        if renpy.showing('DressScreen'):
                return 1

        if Girl is StormX:
            if not Girl.Taboo or StormX in Rules: #Storm skips this if not in public
                return 1
            else:
                ch_s "Боюсь, правила есть правила."

        if Girl.Taboo:
                return 0

        if not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History:
                #if you're a girl and she has not clocked you yet, it's fine.
                return 1

        $ Girl.FaceChange("bemused",1,Eyes="side")
        if "screen" in Girl.DailyActions:
                pass
        elif Girl is RogueX:
                ch_r "Мне не очень комфортно стоять перед тобой в таком виде."
        elif Girl is KittyX:
                ch_k "Я здесь, вроде как, буду раздеваться."
        elif Girl is EmmaX:
                ch_e "Я здесь, вроде как, буду раздеваться. . ."
        elif Girl is LauraX:
                ch_l "Не уверена, что хочу показывать так много своего тела."
        elif Girl is JeanX:
                if not Player.Male:
                    ch_j "Я не думаю, что ты готова к этому. . ."
                else:
                    ch_j "Я не думаю, что ты готов к этому. . ."
        elif Girl is JeanX:
                if not Player.Male:
                    ch_s "Я не думаю, что ты готова к этому. . ."
                else:
                    ch_s "Я не думаю, что ты готов к этому. . ."
        elif Girl is JubesX:
                ch_v "Не уверена, все происходит слишком быстро. . ."
        elif Girl is GwenX:
                ch_g "Я еще не привыкла к этому месту, да и я не большая любительница рейтинга \"R\". . ."
        elif Girl is BetsyX:
                ch_b "Мне было довольно неудобно переодеваться перед тобой. . ."
        elif Girl is DoreenX:
                ch_d "Мне некомфортно переодеваться перед тобой."
        elif Girl is WandaX:
                ch_w "Мне бы хотелось больше приватности. . ."
        $ Girl.AddWord(1,0,"screen") #adds screen to daily
        $ Girl.FaceChange("bemused",1)
        call AnyLine(Girl,"Не возражаешь, если я встану за ширму?")
        menu:
            extend ""
            "Давай":
                    show DressScreen zorder 150
                    if Girl is RogueX:
                            ch_r "Спасибо."
                    elif Girl is KittyX:
                            ch_k "Отлично."
                    elif Girl is EmmaX:
                            ch_e "Благодарю."
                    elif Girl is LauraX:
                            ch_l "Ладно."
                    elif Girl is JeanX:
                            ch_j "Хорошо."
                    elif Girl is JubesX:
                            ch_v "О, спасибо. . ."
                    elif Girl is GwenX:
                            ch_g "Фух, спасибо. . ."
                    elif Girl is BetsyX:
                            ch_b "Неплохо. . ."
                    elif Girl is DoreenX:
                            ch_d "Здорово!"
                    elif Girl is WandaX:
                            ch_w "Клево. . ."
                    return 1
            "Нет, я против":
                    if Girl is RogueX:
                            ch_r "Ну и ладно. . ."
                    elif Girl is KittyX:
                            ch_k "Ну и ладно. . ."
                    elif Girl is EmmaX:
                            ch_e "Ну и отлично. . ."
                    elif Girl is LauraX:
                            ch_l "Ладно. . ."
                    elif Girl is JeanX:
                            ch_j "Ну и ладно."
                    elif Girl is JubesX:
                            ch_v "Ну и хорошо. . ."
                    elif Girl is GwenX:
                            ch_g "Хмм. . . ну ладно. . ."
                    elif Girl is BetsyX:
                            ch_b "Неужели. . ."
                    elif Girl is DoreenX:
                            ch_d "Ох, ладно. . ."
                    elif Girl is WandaX:
                            ch_w "Ладно, как скажешь. . ."

        return 0
# End Dressing Screen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# End Clothes Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
