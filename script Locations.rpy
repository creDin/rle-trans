# //////////////////////////////////////////////////////////////////////                World Map Interface

label Worldmap:   #rkeljsvgb
    # Modification mode
    $ play_music()
    $ play_sound()
    # -----------------
    scene bg_campus onlayer backdrop
    scene
    scene onlayer black #removes MindFuck and black screen
    $ Taboo = 0
    menu:
        "Куда бы вы хотели пойти?"

        "Чердак" if "attic" in Player.History:
                    jump StormMeet

        "Чердак" if "nightlight" in Player.History:
                    jump DoreenMeet

        "Моя комната":
                    $ renpy.pop_call()
                    jump Player_Room_Entry
        "Testbed" if config.developer:
                    $ renpy.pop_call()
                    jump Rogue_Room_Test
        "Комнаты Девушек":
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            jump Worldmap
        "Площадь кампуса":
                    $ renpy.pop_call()
                    jump Campus_Entry
        "Аудитория":
            if Time_Count < 3: #not nighttime
                        $ renpy.pop_call()
                        jump Class_Room_Entry
            elif "Xavier" in Keys:
                        "Дверь заперта, но вы смогли воспользоваться ключом Ксавье, чтобы войти."
                        $ renpy.pop_call()
                        jump Class_Room_Entry
            else:
                        "Уже поздно для занятий, аудитории закрыты."
                        jump Worldmap
        "Комната Опасности":
                    $ renpy.pop_call()
                    jump Danger_Room_Entry
        "Душевые":
                    $ renpy.pop_call()
                    jump Shower_Room_Entry
        "Бассейн":
                    $ renpy.pop_call()
                    jump Pool_Entry
        "Кабинет Ксавье":
                    $ renpy.pop_call()
                    jump Study_Room_Entry

        "Сходить в торговый центр" if "mall" in Player.History and Time_Count < 3:
                    call Mall_Entry
                    jump Campus

        "Никуда не идти.":
                    return
    return

# end World Map Interface //////////////////////////////////////////////////////////////////////

# start Misplaced location checker  //////////////////////////////////////////////////////////////////////
label Misplaced: #rkeljsvgbdw
        if Trigger and Trigger in TotalGirls:
                #sent here by a broken sex action, Trigger should be girl's name
                call SexMenu # call expression  Trigger.Tag + "_SexMenu"
        #if "Historia" in Player.Traits:
                #call Historia_Clear
        scene onlayer black #removes MindFuck and black screen
        $ Player.DrainWord("locked",0,0,1)
        $ StackDepth = renpy.call_stack_depth() #Count = number of items in the call stack
        $ Player.DrainWord("sexit")
        scene
        call Clear_Nearby
        call Present_Check
        $ renpy.free_memory()
        while StackDepth > 0:
                $ StackDepth -= 1
                $ renpy.pop_call()
        if bg_current == "bg player":
                jump Player_Room
        if bg_current == "bg rogue":
                jump Rogue_Room
        if bg_current == "bg kitty":
                jump Kitty_Room
        if bg_current == "bg emma":
                jump Emma_Room
        if bg_current == "bg laura":
                jump Laura_Room
        if bg_current == "bg jean":
                jump Jean_Room
        if bg_current == "bg storm":
                jump Storm_Room
        if bg_current == "bg jubes":
                jump Jubes_Room
        if bg_current == "bg gwen":
                jump Gwen_Room
        if bg_current == "bg betsy":
                jump Betsy_Room
        if bg_current == "bg doreen":
                jump Doreen_Room
        if bg_current == "bg wanda":
                jump Wanda_Room
        if bg_current == "bg dangerroom":
                jump Danger_Room
        if bg_current == "bg classroom":
                jump Class_Room
        if bg_current == "bg showerroom":
                jump Shower_Room
        if bg_current == "bg study":
                jump Study_Room
        if bg_current == "bg pool":
                jump Pool_Entry
        if bg_current in ("bg mall","bg shop","bg dressing"):
                call Shopping_Mall
                return
        jump Campus

        return
# end Misplaced location checker  //////////////////////////////////////////////////////////////////////


# Player's Room Interface //////////////////////////////////////////////////////////////////////
label Player_Room_Entry:
    # Modification mode
    $ play_music()
    $ play_sound()
    # -----------------
    #call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
    call Drain_Nearby #empties .Loc "nearby"
    $ bg_current = "bg player"
    call Gym_Clothes_Off #call Gym_Clothes
    $ Player.RecentActions.append("traveling")
    $ Round -= 5 if Round >= 5 else Round
    if Round <= 10:
                call Round10
    call EventCalls
    call Set_The_Scene
    jump Clear_Stack #removes stray calls in the call stack

label Player_Room: #rkeljsvgb
    # Modification mode
    $ play_music()
    $ play_sound()
    # -----------------
    $ bg_current = "bg player"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    call GirlsAngry

# Player Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "Вы находитесь в своей комнате. Чем бы вы хотели заняться?"

        "Сходить на чердак" if TravelMode and "attic" in Player.History:
                    jump StormMeet
        "Сходить на чердак" if TravelMode and "nightlight" in Player.History:
                    jump DoreenMeet

        "Общаться":
                    call Chat

        "Заниматься":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level


        "Спать" if Time_Count >= 3: #night time
                    call Round10
#                    call Girls_Location
                    call EventCalls
        "Ждать" if Time_Count < 3: #not night time
                    "Вы решаете потратить время впустую."
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Сохранить или загрузить игру":
                    call screen save

        "Интернет-магазин":
                    call Shop
        "Специальные возможности":
                    call SpecialMenu #found in Rogue Scenes


        "Комнаты Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    jump Player_Room

# end Player's Room Interface //////////////////////////////////////////////////////////////////////


# University Square Interface //////////////////////////////////////////////////////////////////////

label Campus_Map:
    $ Line = 0
    $ Trigger = 0
    $ Trigger2 = 0
    call Clear_Offhands
#    $ Trigger3 = 0
#    $ Trigger4 = 0
#    $ Trigger5 = 0
    $ bg_current = "bg campus"
    $ Player.DrainWord("locked",0,0,1)
    call Set_The_Scene
    if not TravelMode:
        call Worldmap
    jump Campus

label Campus_Entry:
    # Modification mode
    $ play_music()
    # -----------------
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
    call Drain_Nearby #empties .Loc "nearby"
    $ bg_current = "bg campus"
    call Gym_Clothes_Off #call Gym_Clothes
    call Taboo_Level
    $ Player.RecentActions.append("traveling")
    if Round <= 10:
                call Round10
    call EventCalls
    call Set_The_Scene

label Campus: #rkeljsvgb
    # Modification mode
    $ play_music()
    # -----------------
    $ bg_current = "bg campus"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    call GirlsAngry
    if Time_Count == 2 and "yesdate" in Player.DailyActions: #evening
            #if it's evening and you have a date lined up. . .
            menu:
                "Вы готовы пойти на свидание?"
                "Да":
                        call DateNight
                        if "yesdate" in Player.DailyActions:
                                $ Player.DailyActions.remove("yesdate")
                "Пока нет. . .":
                        pass
    if Round <= 10:
                if Time_Count >= 3: #night time
                    "Вы возвращаетесь в свою комнату, ибо устали."
                    jump Player_Room
                call Wait
                call Girls_Location
                call EventCalls
    #End date code

# Uni Square Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "Вы находитесь на площади кампуса. Чем бы вы хотели заняться?"

        "Общаться":
            call Chat

        "Переместиться ближе к другим девушкам" if Nearby:
            call Swap_Nearby("menu")

        "Ждать" if Time_Count < 3: #not night time
            "Вы решаете потратить время впустую."
            call Wait
            call Girls_Location
            call EventCalls

        "Идти в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Отправиться в аудиторию" if TravelMode:
                    if Time_Count < 3: #not night time
                        jump Class_Room_Entry
                    elif "Xavier" in Keys:
                        "Дверь заперта, но вы смогли воспользоваться ключом Ксавье, чтобы войти."
                        jump Class_Room_Entry
                    else:
                        "Уже поздно для занятий, аудитории закрыты."
        "Отправиться в комнату Опасности" if TravelMode:
                    jump Danger_Room_Entry
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry
        "Отправиться к бассейну" if TravelMode:
                    jump Pool_Entry
        "Кабинет Ксавье" if TravelMode:
                    jump Study_Room_Entry
        "Сходить в торговый центр" if TravelMode and "mall" in Player.History:
                    call Mall_Entry

        "Уйти" if not TravelMode:
                    call Worldmap

    jump Campus

# end University Square Interface //////////////////////////////////////////////////////////////////////


# Classroom Interface //////////////////////////////////////////////////////////////////////

label Class_Room_Entry:
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
    $ Present = []
    call Drain_Nearby #empties .Loc "nearby"
    $ bg_current = "bg classroom"
    call Gym_Clothes_Off #call Gym_Clothes
    call Taboo_Level
    $ Player.RecentActions.append("traveling")
    $ Round -= 5 if Round >= 5 else Round
    if Round <= 10:
                call Round10
    call EventCalls
    call Events_Classroom
    call Set_The_Scene(0) #won't display characters yet)
    $ Line = "entry"

label Class_Room:
    $ bg_current = "bg classroom"
    if "goto" in Player.RecentActions or "traveling" in Player.RecentActions:
            $ Present = []
            if Time_Count < 2 and Weekday < 5:   #pre-evening
                    call Class_Room_Seating
            $ Player.DrainWord("goto",1,0)
            $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1,Class=1) #    call Set_The_Scene(Quiet=1,Class=1)
    call Class_Setting
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Time_Count >= 3: # night time
                    "Вы возвращаетесь в свою комнату, ибо устали."
                    jump Player_Room
                call Wait
                call Girls_Location
                call EventCalls
                call Class_Setting
                call Events_Classroom
    call GirlsAngry

    if Line == "entry":
            if EmmaX.Loc == "bg teacher":
                    $ Line = "Вы садитесь и видите "+ EmmaX.Name_vin +" на подиуме. Чем бы вы хотели заняться?"
            elif StormX.Loc == "bg teacher":
                    $ Line = "Вы садитесь и видите "+ StormX.Name_vin +" на подиуме. Чем бы вы хотели заняться?"
            elif Time_Count == 2 or Weekday > 5: #evening
                    $ Line = "Вы входите в аудиторию. Чем Вы хотели бы заняться?"
            else:
                    $ Line = "Вы садитесь за письменный стол. Чем Вы хотели бы заняться?"
    else:
            if Line != "Чем вы хотели бы заняться дальше?":
                    $ Line = "Вы сейчас в аудитории. Чем Вы хотели бы заняться?"
    #End Room Set-up

# Class Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "[Line]"
        "Посетить утреннее занятие" if Weekday < 5 and Time_Count == 0:
                if Round >= 30:
                    jump Take_Class
                else:
                    "Занятие подходит к концу. Вы можете подождать следующего."
        "Посетить дневное занятие" if Weekday < 5 and Time_Count == 1:
                if Round >= 30:
                    jump Take_Class
                else:
                    "Занятие подходит к концу. Вы можете находиться в аудитории, пока здание не закроют на ночь."
        "Сейчас нет занятий (locked)" if Weekday >= 5 or Time_Count >= 2:
                pass

        "Общаться":
                call Chat
                $ Line = "Вы сейчас в аудитории. Чем Вы хотели бы заняться?"

        "Переместиться ближе к другим девушкам" if Nearby:
                call Swap_Nearby("menu")

        "Запереть дверь (locked)" if "locked" not in Player.Traits and Time_Count < 2:
                    pass

        "Запереть дверь" if "locked" not in Player.Traits and Time_Count >= 2:
                    if Weekday >=5 or Time_Count >= 2: #evening+
                            "Вы запираете дверь."
                            $ Player.Traits.append("locked")
                            call Taboo_Level
                    else:
                            "Вы не можете этого сделать во время занятия."

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Ждать" if Time_Count < 3: #not night time
                "Вы решаете потратить время впустую."
                call Wait
                call Girls_Location
                call EventCalls
                call Class_Setting
                call Events_Classroom

                if Time_Count < 2: #not evening
                            $ Line = "Начинается новое занятие. Чем Вы хотели бы заняться?"
                else:
                            $ Line = "На сегодня занятия окончены. Чем Вы хотели бы заняться?"

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    $ Line = 0
    jump Class_Room

# End Core Classroom menu <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Take_Class:                       #Class events
    if EmmaX in Present:
            ch_e "Мне, наверное, лучше подождать до конца занятия, увидимся, когда оно закончится."
            $ Nearby.append(EmmaX)
            $ Present.remove(EmmaX)
            $ EmmaX.Loc = "nearby"
    if StormX in Present:
            ch_s "Я не хотела бы мешать, я вернусь, когда занятия закончатся."
            $ Nearby.append(StormX)
            $ Present.remove(StormX)
            $ StormX.Loc = "nearby"
    call Set_The_Scene(0)
    call Class_Setting

    if "class" in Player.DailyActions:
            $ Line = "Занятия начинаются."
    elif Round >= 80:
            $ Line = "Вы успеваете к началу занятия."
    elif Round >= 50:
            $ Line = "Вы приходите с небольшим опозданием, почти целое занятие впереди."
    elif Round >= 30:
            $ Line = "Вы приходите почти к самому концу занятия."
    $ Trigger = 0

    $ D20 = renpy.random.randint(1, 20)

#    if RogueX in Present and D20 > 10 and RogueX.Inbt >= 500 and RogueX.Loc == "bg classroom":
#        "[Line]"
#        call Rogue_Frisky_Class

    if D20 > 15 and Present and ApprovalCheck(Present[0], 300, "I"):
            #if there is another girl in the room, and she is reasonably loose, call Frisky Class
            "[Line]"
            call Frisky_Class(Present[0])
    else:
        $ Line = Line + renpy.random.choice([" Оно проходит довольно скучно.",
                " Занятие посвещяно биологии мутантов.",
                " Занятие посвещяно курс математики.",
                " На нем вы смотрели фильм про морских котиков.",
                " Оно проходит весело.",
                " Прикладная тригонометрия удивительно интересна, особенно когда Циклоп демонстрирует ее использование на примере показательных выстрелов.",
                " Геополитическая наука: от Латверии до Мадрипура.",
                " Сегодняшняя лекция посвящена чтению языка тела.",
                " \"Плащи: Что Ваше Имя и Костюм Говорят О Вас.\" На этой теме в аудитории становится оживленно, вы тоже принимаете активное участие в дебатах",
                " Тема дня - Мутанты и сверхчеловеческое сообщество.",
                " Тема \"Мутанты VS Мутировавшие.\" Как оказалось, термины не взаимозаменяемые.",
                " Сегодняшнее занятие посвящено тому, как представить себя публике. Она использует Человека-Паука в качестве примера того, как плохой пиар усложняет вашу жизнь.",
                " История мутантов, от Апокалипсиса до Темного Феникса.",
                " Вы проводите некоторое время, изучая политику. Сенатор Траск кажется настоящим произведением искусства.",
                " Вы проводите занятие, изучая философию Аристотеля. Ну, или сиськи Эммы",
                " Вы узнаете, как гражданские законы применимы к силам мутантов, изучив несколько громких примеров. Это, на удивление, интересно.",
                " Вы слушаете, как приглашенный оратор описывает работу с неправительственной организацией из Геноши, пытающейся реабилитировать мутантов в Штатах.",
                " Сегодня преподаватель описывает теорию о способностях мутантов. Почему-то создается впечатление, что она смотрит на вас во время лекции.",
                " Эм, игростроение для чайников?"])
        "[Line]"
    $ Player.RecentActions.append("class")
    $ Player.DailyActions.append("class")
    $ Player.XP += (5 + (int(Round / 10)))

    call Wait
    call Girls_Location
    call Set_The_Scene
    call EventCalls
    call Events_Classroom
    $ Line = "Чем вы хотели бы заняться дальше?"
    jump Class_Room

# End "Taking Class" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


label Class_Room_Seating(Girls=[],GirlB=0,GirlLike=0,Line=0,D20=0,BO=[]): #rkeljsvgbdw
    # Girls is the amount of girls in the room.
    # active ones get priority, then shuffled, then nearby girls
    if Party:
            $ Present = Party[:]
    else:
            $ Present = []

    $ BO = ActiveGirls[:]
    if len(Present) == 2: #removes Present girls from set
        $ BO.remove(Present[1])
    if Present:
        $ BO.remove(Present[0])
    python:
        for BX in BO:
            #fills the list with all girls in the room
            if BX.Loc == bg_current and BX not in Girls:
                    Girls.append(BX)

    $ renpy.random.shuffle(Girls)

    $ BO = Nearby[:]
    python:
        for BX in BO:
            # adds any girls nearby to the back of the list
            if BX not in Girls:
                    Girls.append(BX)
    if EmmaX in Girls:
            $ Girls.remove(EmmaX)
    if StormX in Girls:
            $ Girls.remove(StormX)
    #End Girl selections

    $ Nearby = []

    call Set_The_Scene(0) #won't display characters yet)
    if Present:
            pass
    elif len(Girls) == 2:
            # there are two girls
            $ D20 = renpy.random.randint(500, 1500)
            if (Girls[0].GirlLikeCheck(Girls[1]) + Girls[1].GirlLikeCheck(Girls[0])) >= D20:
                "Вы видите, как [Girls[0].Name] и [Girls[1].Name] сидят рядом друг с другом, с кем вы сядите рядом?"
            else:
                "Вы видите, что [Girls[0].Name] и [Girls[1].Name] сейчас находятся в аудитории, но далеко друг от друга."
                $ BO = Girls[:]
                python:
                    for BX in BO:
                        # adds both girls to Nearby
                        if BX not in Nearby:
                                Nearby.append(BX)
            menu:
                extend ""
                "С [Girls[0].Name_tvo]":
                        $ Present = [Girls[0]]
                        if Girls[0] in Nearby:
                                $ Nearby.remove(Girls[0])
                "С [Girls[1].Name_tvo]":
                        $ Present = [Girls[1]]
                        if Girls[1] in Nearby:
                                $ Nearby.remove(Girls[1])
                "Между ними." if not Nearby:
                        $ Present = [Girls[0],Girls[1]]
                        if Girls[1] in Nearby:
                                $ Nearby.remove(Girls[1])
                        if Girls[0] in Nearby:
                                $ Nearby.remove(Girls[0])
                "Ни с кем":
                        "Вы решаете сесть подальше от них."
                        $ BO = Girls[:]
                        python:
                            for BX in BO:
                                # adds both girls to Nearby
                                if BX not in Nearby:
                                        Nearby.append(BX)
    #end two-girl option
    elif len(Girls) > 2:
            # there are two+ girls
            "В комнате находятся несколько девушек, с кем бы вы хотели сесть рядом?"
            while len(Present) < 2:
                    menu:
                        "Можно выбрать до двух вариантов."
                        "Сесть рядом с [RogueX.Name_tvo]" if RogueX in Girls and RogueX not in Present:
                                $ Present.append(RogueX)
                        "Сесть рядом с [KittyX.Name_tvo]" if KittyX in Girls and KittyX not in Present:
                                $ Present.append(KittyX)
                        "Сесть рядом с [LauraX.Name_tvo]" if LauraX in Girls and LauraX not in Present:
                                $ Present.append(LauraX)
                        "Сесть рядом с [JeanX.Name_tvo]" if JeanX in Girls and JeanX not in Present:
                                $ Present.append(JeanX)
                        "Сесть рядом с [JubesX.Name_tvo]" if JubesX in Girls and JubesX not in Present:
                                $ Present.append(JubesX)
                        "Сесть рядом с [GwenX.Name_tvo]" if GwenX in Girls and GwenX not in Present:
                                $ Present.append(GwenX)
                        "Сесть рядом с [BetsyX.Name_tvo]" if BetsyX in Girls and BetsyX not in Present:
                                $ Present.append(BetsyX)
                        "Сесть рядом с [DoreenX.Name_tvo]" if DoreenX in Girls and DoreenX not in Present:
                                $ Present.append(DoreenX)
                        "Сесть рядом с [WandaX.Name_tvo]" if WandaX in Girls and WandaX not in Present:
                                $ Present.append(WandaX)
                        "Готово":
                                $ Present.append("junk")
                                $ Present.append("junk")

    #end two-girl option
    elif Girls:
            # there is one girl
            menu:
                "Вы видите [Girls[0].Name_vin], хотите сесть рядом с ней?"
                "Да":
                        $ Present.append(Girls[0])
                "Нет, лучше сяду немного подальше от нее.":
                        $ Nearby.append(Girls[0])
    #end one-girl option
    #else: no girls at all

    while "junk" in Present:
            $ Present.remove("junk")
    while len(Present) > 2:
            call Remove_Girl(Present[2],Hold=1)

    if len(Present) == 2:
            "Вы садитесь между [Present[0].Name_vin] и [Present[1].Name_vin]."
            $ Present[0].Loc = "bg classroom"
            $ Present[1].Loc = "bg classroom"
    elif Present:
            "Вы садитесь рядом с [Present[0].Name_tvo]."
            $ Present[0].Loc = "bg classroom"
    else:
            "Вы садитесь в стороне от всех."

    if len(Girls) > len(Present):
            #if there were girls not picked
            "Остальные разбросаны по разным местам."

    python:
        for BX in Girls:
            if BX not in Present:
                    #if she wasn't added to present, move her to Nearby
                    if BX not in Nearby:
                            Nearby.append(BX)
                    BX.Loc = "nearby"
                    if BX in Party:
                            Party.remove(BX)
    if Present:
            call Shift_Focus(Present[0])
#    call Set_The_Scene(Quiet=1)

    return

# end Class Room Interface //////////////////////////////////////////////////////////////////////


# Danger Room Interface //////////////////////////////////////////////////////////////////////

label Danger_Room_Entry:
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
    call Drain_Nearby #empties .Loc "nearby"
    $ bg_current = "bg dangerroom"
    call Taboo_Level
    $ Player.RecentActions.append("traveling")
    $ Round -= 5 if Round >= 5 else Round
    if Round <= 10:
                call Round10
    call EventCalls
    call Events_DangerRoom
    call Gym_Entry #call Gym_Clothes("pre")#Automatically puts them in gym clothes if they've been here
    call Set_The_Scene

label Danger_Room:
    $ bg_current = "bg dangerroom"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                "Похоже, смена меняется. . ."
                if Time_Count >=3: # night time
                    "Вы возвращаетесь в свою комнату, ибо устали."
                    jump Player_Room
                call Wait
                call Girls_Location
                call EventCalls
                call Gym_Clothes_Off #call Gym_Clothes
    call GirlsAngry
    #End Room Set-up

# Danger Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "Вы в Комнате Опасности. Чем вы хотели бы заняться?"
#        extend ""
        "Тренироваться":
                if Time_Count >= 3: #night time
                        "Комнату Опасности отключают на ночь, наверное, вам стоит пойти отдохнуть."
                elif Round >= 30:
                        jump Training
                else:
                        "Перед следующим циклом осталось немного времени, похоже, придется немного подождать."

        "Общаться":
                call Chat

        "Переместиться ближе к другим девушкам" if Nearby:
                call Swap_Nearby("menu")

        "Исторический симулятор":
                    ch_danger "Эта функция позволяет вам вернуться к предыдущим событиям в вашей истории."
                    ch_danger "К сожалению, эта функция временно отключена."
                    #call Danger_Room_Historia

        "Запереть дверь (locked)" if "locked" not in Player.Traits and Time_Count < 2:
                    pass

        "Запереть дверь" if "locked" not in Player.Traits and Time_Count >= 2:
                    if Time_Count >= 3: #night time
                            "Вы запираете дверь."
                            $ Player.Traits.append("locked")
                            call Taboo_Level
                    else:
                            "Вы не можете этого сделать в свободные для самостоятельных тренировок часы."

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Ждать (locked)" if Time_Count >= 3: #night time
                    pass
        "Ждать" if Time_Count < 3: #not night time
                    "Вы решаете потратить время впустую."
                    call Wait
                    call Girls_Location
                    call EventCalls
                    call Gym_Clothes_Off #call Gym_Clothes

        "Выйти" if not TravelMode:
                    call Gym_Exit  #call Gym_Clothes("change")
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    call Gym_Exit  #call Gym_Clothes("change")
                    jump Campus_Entry

        "Душевые" if TravelMode:
                    call Gym_Exit  #call Gym_Clothes("change")
                    jump Shower_Room_Entry
    jump Danger_Room

label Training:
    $ D20 = renpy.random.randint(1, 20)
#    if D20 > 10 and RogueX.Inbt >= 500:
#        call Rogue_Frisky_Danger

    $ Player.XP += (5 + (int(Round / 10)))
    $ Player.DailyActions.append("dangerroom")
    call Set_The_Scene

    if Round >= 80:
            $ Line = "Вас ждет долгая тренировка в комнате Опасности."
    elif Round >= 50:
            $ Line = "Вас ждет короткая тренировка в комнате Опасности."
    else:
            $ Line = "Вы успеваете на быструю тренировку в комнате Опасности."

    $ Trigger = 0
    if D20 >= 18:
            #if "cyclops":
            "[Line] Во время упражнения Циклоп случайно стреляет в вас."
            "К счастью, вы невосприимчивы к лучам, но вашей одежде везет меньше."
            call RoomStatboost("Love",80,2)
            call RoomStatboost("Lust",80,5)
    elif D20 >= 17:
            "[Line] Вы участвуете в тренировке рукопашного боя."
            "Прежде чем начать, Циклоп объясняет, что всегда полезно знать, как защитить себя, когда вы не можете полагаться на свои способности."
            "Похоже, у этих слов есть какая-то предыстория."
    elif D20 >= 16:
            "Несколько старших студентов подходят к вам, чтобы поговорить о ваших способностях."
            "Ночной Змей вслух задается вопросом, что произойдет, если он схватит вас и попытается телепортироваться, пока вы пытаетесь отключить его способности."
            "Вам удается напугать друг друга."
    else:
            $ Line = Line + renpy.random.choice([" Было довольно скучно.",
                    " Вы тренируетесь с обычным огнестрельным оружием.",
                    " Вы пробегаете полосу препятствий.",
                    " Вы сражаетесь в симулированной битве против Братства.",
                    " Вы помогаете завалить голографического Стража.",
                    " Вы участвуете в тренировочной схватке против Мстителей. Как будто Люди Икс и Мстители когда-нибудь выйдут друг против друга.",
                    " Вы и некоторые другие участвуете в тренировке на выживание. . . также известном как \"постарайтесь продержаться как можно дольше, пока Росомаха охотится за вами по одному.\"",
                    " Вы решаете проверить себя, сразившись с Магнето в одиночку. Все идет так хорошо, как вы и ожидали.",
                    " Вы используете голограммы комнаты Опасности, чтобы пережить некоторые из самых больших сражений первых Людей Икс. Вы узнаете довольно много о командной работе.",
                    " Зверь ведет занятия по паркуру. Вы принимаете участие и получаете несколько указаний. Вы, конечно, не Человек-Паук, но, по крайней мере, кое-что у вас получается.",
                    " Вы участвуете в тренировке на случай ЧП. Вы получите несколько советов по оказанию первой помощи, сортировке и правильному перемещению раненых.",
                    " Вы принимаете участие в городских учениях по ЧП. Циклоп тратит время, чтобы объяснить вам, как использовать укрытие, чтобы подобраться достаточно близко для использования своих способностей.",
                    " Вы участвуете в тренировке с симуляцией джунглей под руководством Росомахи. Вы изучаете некоторые базовые методы выживания, но втайне надеетесь, что они вам никогда не понадобятся.",
                    " Ваша команда сражается с симуляцией Магнето."])
            "[Line]"

    call Girl_TightsRipped
    call Wait
    call Girls_Location
    call Set_The_Scene
    $ Line = "Тренировка подходит к концу, чем вы хотели бы заняться дальше?"

    jump Danger_Room


# end Danger Room Interface //////////////////////////////////////////////////////////////////////


# Danger Room Interface //////////////////////////////////////////////////////////////////////

label Pool_Entry:
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
    call Drain_Nearby #empties .Loc "nearby"
    $ bg_current = "bg pool"
    call Taboo_Level
    $ Player.RecentActions.append("traveling")
    $ Round -= 5 if Round >= 5 else Round
    if Round <= 10:
                call Round10
    call EventCalls
    call Gym_Clothes_Off #call Gym_Clothes
    call SwimSuit #puts girls in swimsuits if already here
    call Set_The_Scene

label Pool_Room:
    $ bg_current = "bg pool"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1,Dress=0)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Time_Count >= 3: #night time
                    "Вы возвращаетесь в свою комнату, ибо устали."
                    jump Player_Room
                call Wait
                call Girls_Location
                call EventCalls
    call GirlsAngry
    #End Room Set-up

# Pool Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "Вы у бассейна. Чем вы хотели бы заняться?"

        "Общаться":
                call Chat

        "Переместиться ближе к другим девушкам" if Nearby:
                call Swap_Nearby("menu")

        "Позагорать?" if Time_Count < 2:
                call Pool_Sunbathe
                $ Round -= 20 if Round >= 20 else Round
                "Вы проводите немного времени за этим занятием."
        "Поплавать?":
            if Time_Count >= 3 and AloneCheck():
                "Как-то поздновато для купания."
            else:
                call Pool_Swim
        "Искупаться голышом?":
                call Pool_Skinnydip

        "Ждать (locked)" if Time_Count >= 3: #night
                pass
        "Ждать" if Time_Count < 3: #not night
                "Вы решаете потратить время впустую."
                call Wait
                call Girls_Location
                call EventCalls

        "Выйти" if not TravelMode:
                    call Girl_Dressed
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    call Girl_Dressed
                    jump Campus_Entry

        "Душевые" if TravelMode:
                jump Shower_Room_Entry
    jump Pool_Room

label Pool_Swim(Swimmers=[],BO=[]):
    $ D20 = renpy.random.randint(1, 20)

    $ Player.DailyActions.append("swim")
    call Set_The_Scene

    $ Line = ""
    $ PassLine = 0
    $ BO = TotalGirls[:]
    while BO:
            if bg_current == BO[0].Loc and ApprovalCheck(BO[0], 700):
                    if BO[0].Chest == BO[0].Swim[5] and BO[0].Panties == BO[0].Swim[6]:
                                # if she's already in swimwear . . .
                                $ Swimmers.append(BO[0])
                    elif not BO[0].ChestNum() and not BO[0].OverNum() and not BO[0].PantiesNum() and not BO[0].PantsNum() and not BO[0].HoseNum():
                                # or is nude. . .
                                $ Swimmers.append(BO[0])
                    else:
                        if Line or PassLine:
                                #if it's second time through
                                call Display_Girl(BO[0],0,0, BO[0].SpriteLoc,50)
                        else:
                                call Display_Girl(BO[0],0,0, BO[0].SpriteLoc,50)
                        if BO[0].OutfitChange("swimwear"):
                                #if changed into swimsuit. . .
                                $ Line = "" if Swimmers and not PassLine else "s" #whole point of this is to change the plurals
                                $ Swimmers.append(BO[0])
                        elif BO[0] is GwenX:
                                ch_g "Но мой супергеройский костюм что-то типа купальника!"
                                $ BO[0].OutfitChange("casual1") # puts on her swimsuit
                                $ BO[0].Panties = 0
                                $ BO[0].Boots = 0
                                $ BO[0].Hat = 0
                                $ Line = "" if Swimmers and not PassLine else "s" #whole point of this is to change the plaurals
                                $ Swimmers.append(BO[0])
                        else:
                                #If she doesn't swim. . .
                                $ Line = "" if PassLine and not Swimmers else "s"
                                $ PassLine = PassLine + " и " + BO[0].Name if PassLine else BO[0].Name
            $ BO.remove(BO[0])

    if len(Swimmers) >= 2:
            "Девчонки переодеваются и присоединяются к вам."
    elif Swimmers:
            "[Swimmers[0].Name] переодевается и присоединяется к вам."
    if PassLine:
            "[PassLine] расслабляются у бассейна."
    $ PassLine = 0
    $ Line = 0

    call ShowPool(Swimmers[:]) #displays pool graphics

    if D20 >= 15 and Swimmers:
            call Pool_Topless(Swimmers[0])
    if D20 >= 11:
            "Вы хорошо освежились."
    elif D20 == 2:
            "Вы присоединяетесь к другим в зажигательной игре Марко Поло."
    elif D20 == 3:
            "Вы взбираетесь на надувной матрац и лениво плаваете по воде."
    elif D20 == 4:
            "Вы взбираетесь на надувной матрац и лениво плаваете по воде."
            "До тех пор, пока Курт не телепортируется в воздух над бассейном и не ныряет, под улюлюканье толпы, бомбочкой."
            "Очень жаль, но он опрокидывает ваш матрац."
    elif D20 == 5:
            "Вы проверяете себя, переплывая от одного конца бассейна до другого."
    elif D20 == 6:
            "Вы пытаетесь произвести впечатление на нескольких девушек, нырнув в бассейн с разбега."
            "В итоге вы провоцируете соревнование по прыжкам бомбочкой, которое по иронии судьбы выигрывает не Пушечное Ядро, к его большому потрясению.[[ПП. cannonball - бомбочка, Cannonball - герой Пушечное Ядро]."
    elif D20 == 7:
            "Вы уже готовы войти в бассейн, когда слышите раздраженные возгласы и крики:\"Бобби!\""
            "Похоже, Айсмен снова создал свой -надувной- матрац."
            "Вы придерживаетесь дальнего конца бассейна, где не холодно."
    elif D20 == 8:
            "Вместо этого вы расслабляетесь на одном из шезлонгов у бассейна."
    elif D20 == 9:
            "Циклоп инструктирует нескольких студентов по спасению на воде."
            "Вы слушаете, как он говорит о приближении к тонущей жертве сзади, чтобы они в панике не причинили вам вреда."
    elif D20 == 10:
            "Вы решаете воспользоваться трамплином для прыжков в воду. Вы делаете пару подходов, прежде чем расслабиться и просто плавать."

    call GirlWaitUp(1,80,3) #makes any girls in the room like each other a bit more.
    call RoomStatboost("Love",80,3)
    call RoomStatboost("Lust",30,5)
    $ Round -= 20 if Round >= 20 else Round
    hide FullPool
    call Set_The_Scene(1,0,0)
    "Вы вылезаете из бассейна и немного отдыхаете."
    return

# end Pool Interface //////////////////////////////////////////////////////////////////////


label SwimSuit(BO=[]):
        # puts girls in swimsuit if applicable
        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                if (BX.Loc == bg_current or BX in Nearby) and BX.Swim[0] and BX not in Party and BX.Schedule[Weekday][Time_Count] == "bg pool":
                        #if she has a suit, is not in the party, is at this location, and is scheduled to be there, put her in a swimsuit.
#                        BX.Outfit = "swimwear" # puts on her swimsuit
                        BX.OutfitChange("swimwear") # puts on her swimsuit
                elif BX is GwenX and (BX.Loc == bg_current or BX in Nearby) and BX not in Party and BX.Schedule[Weekday][Time_Count] == "bg pool":
                        BX.OutfitChange("casual1") # puts on her swimsuit
                        BX.Panties = 0
                        BX.Boots = 0
                        BX.Hat = 0
        return

image FullPool:
        #water
        AlphaMask("bg_pool", "images/PoolMask.png")

label ShowPool(BO=[],PoolLoc=0): #rkeljsvgbdw
        #displays the pool with girls in it
        #if not BO:
                #$ BO = ActiveGirls[:]
        python:
            for BX in BO:
                if BX.Loc == bg_current:
                            BX.AddWord(0,"swim","swim",0,0) #adds "swim" tag to recent and daily actions
                            BX.Water = 1
                            BX.Spunk = []
                            PoolLoc = 650 if PoolLoc else 500  #should first be zeor, and set to 650, then to 500
                            renpy.show(BX.Tag+"_Sprite",at_list=[Pool_Bob(PoolLoc)],zorder=50)
#                            if BX is RogueX:
#                                    show Rogue_Sprite at Pool_Bob(PoolLoc) zorder 50  #BX.Layer
        show FullPool zorder 60        #should put masked pool above girls #175?
        return

transform Pool_Bob(PoolLoc=500):
        subpixel True
        pos (PoolLoc,450)
        alpha 1
        zoom .45
        offset (0,0)
        anchor (0.5, 0.0)
        xoffset 0
        yoffset 0
        choice:
            yoffset 0
        choice:
            pause .3
        choice:
            pause .5
        block:
            ease 1 yoffset 10
            ease 1.5 yoffset 0
            repeat

# Showers Interface //////////////////////////////////////////////////////////////////////
label Shower_Room_Entry: #rkeljsvgb
    # Modification mode
    $ play_music(name=audio.shower_location)
    # -----------------
    call Jubes_Entry_Check
    call Drain_Nearby #empties .Loc "nearby"
    $ bg_current = "bg showerroom"
    $ Player.DrainWord("locked",0,0,1)
    $ Present = []
    call Taboo_Level
    call Set_The_Scene(0,1,0)
    $ Round -= 5 if Round >= 5 else Round
    if Round <= 10:
            if Time_Count < 3:
                    call Wait
            else:
                    "Уже слишком поздно, вы быстро принимаете душ и возвращаетесь в свою комнату."
                    $ bg_current = "bg player"
                    jump Misplaced

    if Round <= 10 or len(Party) >= 2:
            jump Shower_Room

    #Activates Jean meet
    if Day >= 9 and "met" not in JeanX.History and "met" in EmmaX.History and "Intro" not in Player.DailyActions and not PlotBreak:
            call JeanMeet
            jump Shower_Room

    $ Options = []
    $ Line = ActiveGirls[:]   #make sure this is initialized
    python:
        for BX in Line:
            #loops through and adds populates Occupants with locals
            if BX not in Party and "showered" not in BX.DailyActions and (BX.Loc == BX.Home or BX.Loc == "bg dangerroom"):
                    #Checks if girl is in the shower
                    Options.append(BX)
    $ Line = 0

    if Options:
                $ renpy.random.shuffle(Options)

    $ D20 = renpy.random.randint(1, 20)
    # <5 is they show up late, 5-9 is they haven't showered yet, 10+ is they finished,
    # 13-15 is they are changing, 16+ is you walk in on them nude, 17+ they might be masturbating

    if D20 < 5 or (len(Options) + len(Party) > 2):  #not Options or
                # if < 5, they show up late, or if there are more potential girls than room for them
                while Options and (D20 < 5 or len(Options) + len(Party) > 2):
                        #Loops through while Options and Party are more than 2
                        $ Nearby.append(Options[0])     #adds this girl to the nearby roster
                        $ Options[0].Loc = "nearby"     #adds this girl to the nearby roster
                        $ Options.remove(Options[0])    #subs this girl from Options

    if not Party and Options and Options[0] in TotalGirls:
            if D20 > 15:
                    call Girl_Caught_Shower(Options[0])
                    jump Shower_Room
            elif D20 > 13:
                    $ Options[0].AddWord(1,"showered","showered",0,0)
                    call Girl_Caught_Changing(Options[0])
                    jump Shower_Room
    #End Caught Check

    # If none of the caught dialogs plays, checks to see if anyone is in the room, and allows them to be there if they are.
    $ Line = Options[:]
    python:
        for BX in Line:
            #loops through and adds populates nearby with locals
            BX.Loc = bg_current
    $ Line = 0

    call Present_Check(0)

    $ Line = Options[:]
    python:
        for BX in Line:
            #loops through and puts towels on them, maybe the "showered" trait
            if BX.Loc == bg_current and BX not in Party:
                    if D20 >= 10:
                            BX.AddWord(1,"showered","showered",0,0)
                    BX.OutfitChange("towel")
    $ Line = 0
    #End Count set-up

    call Set_The_Scene(Dress=0)
    if Party:
        $ Line = " с " + Party[0].Name_tvo
    else:
        $ Line = ""
    if len(Options) >= 2:
        "При входе вы[Line]видите стоящих там [Options[0].Name_vin] и [Options[1].Name_vin]."
    elif Options:
        "При входе вы[Line] видите стоящую там [Options[0].Name_vin]."
    $ Line = 0

    if Options:
            $ Line = 0
            if Options[0] is RogueX:
                    ch_r "Привет, [RogueX.Petname]."
                    if "showered" in RogueX.RecentActions:
                            ch_r "Я как раз собиралась выходить."
                    if not ApprovalCheck(Options[0], 900):
                            ch_r "Увидимся позже."
            elif Options[0] is KittyX:
                    ch_k "Привет, [KittyX.Petname]."
                    if "showered" in KittyX.RecentActions:
                            ch_k "Я только что закончила."
                    if not ApprovalCheck(Options[0], 900):
                            ch_k "Ох, эм. . . я должна идти. . ."
            elif Options[0] is EmmaX:
                    ch_e "О, здравствуй, [EmmaX.Petname]."
                    if "showered" in EmmaX.RecentActions:
                            ch_e "Я уже почти закончила."
                    if not ApprovalCheck(Options[0], 900):
                            ch_e "Мне пора идти."
            elif Options[0] is LauraX:
                    ch_l "О, привет."
                    if "showered" in LauraX.RecentActions:
                            ch_l "Я уже закончила."
                    if not ApprovalCheck(Options[0], 900):
                            ch_l "Увидимся позже."
            elif Options[0] is JeanX:
                    ch_j "Ох, привет. . . тебе."
                    if "showered" in JeanX.RecentActions:
                            ch_j "Я уже заканчиваю."
                    if not ApprovalCheck(Options[0], 900):
                            ch_j "Увидимся."
            elif Options[0] is StormX:
                    ch_s "О, здравствуй, [StormX.Petname]."
                    if "showered" in StormX.RecentActions:
                            ch_s "Я как раз заканчиваю."
                    if not ApprovalCheck(Options[0], 600):
                            ch_s "Мне пора идти."
            elif Options[0] is JubesX:
                    ch_v "Йо, [JubesX.Petname]."
                    if "showered" in JubesX.RecentActions:
                            ch_v "Я только что закончила."
                    if not ApprovalCheck(Options[0], 900):
                            ch_v "Мне пора, эм. . . идти. . ."
            elif Options[0] is GwenX:
                    ch_g "Привет, [GwenX.Petname]."
                    if "showered" in GwenX.RecentActions:
                            ch_g "Я как раз заканчиваю."
                    if not ApprovalCheck(Options[0], 900):
                            ch_g "Хорошо, я пошла. . ."
            elif Options[0] is BetsyX:
                    ch_b "О, привет, [BetsyX.Petname]."
                    if "showered" in BetsyX.RecentActions:
                            ch_b "Я только что закончила."
                    if not ApprovalCheck(Options[0], 900):
                            ch_b "Мне нужно идти. . ."
            elif Options[0] is DoreenX:
                    ch_d "Привет, [DoreenX.Petname]."
                    if "showered" in DoreenX.RecentActions:
                            ch_d "Я уже заканчиваю."
                    if not ApprovalCheck(Options[0], 900):
                            ch_d "Мне пора идти. . ."
            elif Options[0] is WandaX:
                    ch_w "Привет, [WandaX.Petname]."
                    if "showered" in WandaX.RecentActions:
                            ch_w "Я как раз заканчиваю."
                    if not ApprovalCheck(Options[0], 900):
                            ch_w "Мне пора идти. . ."

            if len(Options) >= 2:
                    if Options[1] is RogueX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    #if both decide to leave
                                    ch_r "Ага, до встречи."
                            elif not ApprovalCheck(Options[1], 900):
                                    #if only person 2 decides to leave
                                    ch_r "Ага, мне пора идти."
                            else:
                                    #if both stay
                                    ch_r "Ага, привет."
                    elif Options[1] is KittyX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_k "Ага, увидимся."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_k "Ох, ну. . . мне нужно идти."
                            else:
                                    ch_k "Ага, привет."
                    elif Options[1] is EmmaX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_e "Да, мне тоже пора идти."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_e "Такое ощущение, словно у вас есть неразрешенное дело. . ."
                            else:
                                    ch_e "Да, здравствуй."
                    elif Options[1] is LauraX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_l "Ага, я тоже ухожу."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_l "Ага, я пошла."
                            else:
                                    ch_l "Привет."
                    elif Options[1] is JeanX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_j "Ага, я тоже закончила."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_j "Я уже ухожу."
                            else:
                                    ch_j "Привет."
                    elif Options[1] is StormX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 600):
                                    ch_s "Да, я тоже ухожу."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_s "Не буду вам мешать. . ."
                            else:
                                    ch_s "Да, здравствуй."
                    elif Options[1] is JubesX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_v "Ага, увидимся."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_v "Ох, так вот. . . мне нужно идти."
                            else:
                                    ch_v "Ага, привет."
                    elif Options[1] is GwenX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_g "Ага, пока."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_g "Мне нужно идти. . ."
                            else:
                                    ch_g "Ага, привет."
                    elif Options[1] is BetsyX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_b "Я тоже пошла."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_b "Мне пора идти. . ."
                            else:
                                    ch_b "Ох, да, привет."
                    elif Options[1] is DoreenX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_d "Ага, мне тоже пора."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_d "Мне пора идти. . ."
                            else:
                                    ch_d "Ох, ага, привет."
                    elif Options[1] is WandaX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_w "Конечно, я тоже пошла."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_w "Мне пора идти. . ."
                            else:
                                    ch_w "Ага, привет."

                    if not ApprovalCheck(Options[1], 900):
                            call Remove_Girl(Options[1])
            if not ApprovalCheck(Options[0], 900):
                            call Remove_Girl(Options[0])
            # End welcomes
            if Options:
                    if RogueX in Party:
                            ch_r "Привет, [Options[0].Name]."
                    if KittyX in Party:
                            ch_k "Привет, [Options[0].Name]."
                    if EmmaX in Party:
                            ch_e "О, здравствуй, [Options[0].Name]."
                    if LauraX in Party:
                            ch_l "Привет."
                    if JeanX in Party:
                            ch_j "Ага, привет."
                    if StormX in Party:
                            ch_s "Здравствуй, [Options[0].Name]."
                    if JubesX in Party:
                            ch_v "Привет, [Options[0].Name]."
                    if GwenX in Party:
                            ch_g "Привет, [Options[0].Name]."
                    if BetsyX in Party:
                            ch_b "Ох, привет, [Options[0].Name]."
                    if DoreenX in Party:
                            ch_d "Привет, [Options[0].Name]."
                    if WandaX in Party:
                            ch_w "Привет, [Options[0].Name]."
    $ Line = 0
    # End Reply portion
    $ Options = []


# Shower Room Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Shower_Room: #rkeljsvgb
    # Modification mode
    if is_playing_music(name=audio.shower_location):
        $ play_music(name=audio.shower_location)
    # -----------------
    $ bg_current = "bg showerroom"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Dress=0)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Time_Count == 3: #night time
                        "Вы возвращаетесь в свою комнату, ибо устали."
                        jump Player_Room
                call Wait
                call Girls_Location
                call EventCalls
    call GirlsAngry
    #End Room Set-up

# Shower Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "Вы в душевой. Чем Вы хотели бы заняться?"

        "Общаться":
                call Chat

        "Принять душ" if Round > 30:
                call Showering
        "Принять душ [[нет времени] (locked)" if Round <= 30:
                pass

#        "Запереть дверь" if "locked" not in Player.Traits:
#                    "Вы запираете дверь."
#                    $ Player.Traits.append("locked")
#                    $ Nearby = []
#                    call Taboo_Level

#        "Отпереть дверь" if "locked" in Player.Traits:
#                    "Вы отпираете дверь."
#                    $ Player.Traits.remove("locked")
#                    call Taboo_Level

        "Ждать" if Time_Count < 3: #not night time
                "Вы решаете потратить время впустую."
                if Round > 30:
                        "Ждать, да в душевой."
                        "Это как-то стремно."
                call Wait
                call Girls_Location
                call EventCalls

                #this bit sets up drop-in characters
                if renpy.random.randint(1, 20) < 5:
                        $ Nearby = []
                        $ Line = ActiveGirls[:]   #make sure this is initialized
                        python:
                            for BX in Line:
                                #loops through and adds populates Occupants with locals
                                if BX.Loc != bg_current and "showered" not in BX.DailyActions and (BX.Loc == BX.Home or BX.Loc == "bg dangerroom"):
                                        #Checks if girl is in the shower
                                        Nearby.append(BX)
                        $ Line = 0
                        if Nearby:
                                $ renpy.random.shuffle(Nearby)
                                while len(Nearby) > 2:
                                            # culls out list to 2 if there is a party
                                            $ Nearby.remove(Nearby[0])
                                if len(Nearby) > 1:
                                        $ Nearby[1].Loc = "nearby"
                                $ Nearby[0].Loc = "nearby"
        "Ждать  [[нет времени] (locked)" if Time_Count >= 3: # night time
                pass

        "Отправиться в комнату Опасности" if TravelMode:
                call No_Towels
                jump Danger_Room_Entry
        "Вернуться в свою комнату" if TravelMode:
                call No_Towels
                jump Player_Room_Entry
        "Комнаты Девушек" if TravelMode:
            call Girl_Dressed
            menu:
                "Комната [RogueX.Name_rod]":
                            call No_Towels
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call No_Towels
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call No_Towels
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call No_Towels
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call No_Towels
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call No_Towels
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call No_Towels
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call No_Towels
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call No_Towels
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call No_Towels
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call No_Towels
                            call Girls_Room_Entry(WandaX)

                "Назад":
                            pass
        "Выйти" if not TravelMode:
                # Modification mode
                $ play_music()
                # -----------------
                call QuickEvents
                call No_Towels
                call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                # Modification mode
                $ play_music()
                #------------------
                call QuickEvents
                call No_Towels
                jump Campus_Entry

    jump Shower_Room

# Shower Room Menu End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label No_Towels:
    #Removes their towels if player is leaving the showers
    $ BO = TotalGirls[:]
    python:
        for BX in BO:
            #loops through and adds populates Occupants with locals
            if BX.Loc == "bg showerroom":
                    BX.AddWord(1,"showered","showered")
            if "met" in BX.History:
                if BX in Party:
                    BX.Loc = "bg campus"
                else:
                    BX.Loc = BX.Schedule[Weekday][Time_Count]
            BX.OutfitChange(BX.OutfitDay)
            BX.Set_Temp_Outfit() #sets current outfit as temporary
            if BX in Party:
                    BX.Loc = bg_current
    return

label Showering(Occupants = [], StayCount=[] , Showered = 0, Line = 0, BO=[]): #rkeljsvgb
    # Occupants tallies how many girls are here.
    # StayCount tallies how many girls are willing to stick around.
    $ BO = TotalGirls[:]
    python:
        for BX in BO:
            #loops through and adds populates Occupants with locals
            if BX not in ActiveGirls:
                    BX.Loc = "hold"
            if BX.Loc == "bg showerroom" and BX not in Occupants:
                    Occupants.append(BX)
    if Occupants:
            ch_p "Я в душ, не хочешь присоединиться ко мне?"
            if Occupants[0] is RogueX and "showered" in RogueX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_r "Вообще-то, мы уже закончили, так что мы пошли."
                    else:
                        ch_r "Вообще-то, я уже закончила, так что я пошла."
                    $ Showered = 1
            elif Occupants[0] is KittyX and "showered" in KittyX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_k "Вообще-то, мы уже приняли душ, так что мы пошли."
                    else:
                        ch_k "Вообще-то, я уже приняла душ, так что я пошла."
                    $ Showered = 1
            elif Occupants[0] is EmmaX and "showered" in EmmaX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_e "Мы уже закончили, так что мы пошли."
                    else:
                        ch_e "Я уже закончила, так что я пошла."
                    $ Showered = 1
            elif Occupants[0] is LauraX and "showered" in LauraX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_l "Вообще-то, мы уже закончили."
                    else:
                        ch_l "Я пошла."
                    $ Showered = 1
            elif Occupants[0] is JeanX and "showered" in JeanX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_j "Мы уже закончили."
                    else:
                        ch_j "Я пошла."
                    $ Showered = 1
            elif Occupants[0] is StormX and "showered" in StormX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_s "Думаю, мы уже почти закончили и скоро мы уйдем."
                    else:
                        ch_s "Я уже почти закончила и скоро уйду."
                    $ Showered = 1
            elif Occupants[0] is JubesX and "showered" in JubesX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_v "Мы закончили с душем, так что мы пошли."
                    else:
                        ch_v "Я закончила с душем, так что я пошла."
                    $ Showered = 1
            elif Occupants[0] is GwenX and "showered" in GwenX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_g "Мы все, ладно, мы пошли, увидимся позже."
                    else:
                        ch_g "Я все, ладно, я пошла, увидимся позже."
                    $ Showered = 1
            elif Occupants[0] is BetsyX and "showered" in BetsyX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_b "Мы уже закончили, пока."
                    else:
                        ch_b "Я уже закончила, пока."
                    $ Showered = 1
            elif Occupants[0] is DoreenX and "showered" in DoreenX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_d "Думаю, мы уже почти закончили, увидимся."
                    else:
                        ch_d "Думаю, я уже почти закончила, увидимся."
                    $ Showered = 1
            elif Occupants[0] is WandaX and "showered" in WandaX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_w "Мы закончили, увидимся."
                    else:
                        ch_w "Я закончила, увидимся."
                    $ Showered = 1
            else:
                #None of them have showered yet
                if Occupants[0] is RogueX:
                        if ApprovalCheck(RogueX, 1200) or (ApprovalCheck(RogueX, 600) and RogueX.SeenChest and RogueX.SeenPussy) or not Player.Male:
                                    # Rogue says yes
                                    ch_r "Думаю, я могу остаться. . ."
                                    $ StayCount.append(RogueX)
                        else:
                                    # Rogue says no
                                    ch_r "Нет, мне, пожалуй, пора идти."
                elif Occupants[0] is KittyX:
                        if ApprovalCheck(KittyX, 1400) or (ApprovalCheck(KittyX, 700) and KittyX.SeenChest and KittyX.SeenPussy) or not Player.Male:
                                    ch_k "Ага, я могу остаться."
                                    $ StayCount.append(KittyX)
                        else:
                                    ch_k "Мне нужно идти."
                elif Occupants[0] is EmmaX:
                        if not "classcaught" in EmmaX.History or "three" not in EmmaX.History:
                                ch_e "Думаю, я могу остаться, хотя бы ненадолго."
                        elif ApprovalCheck(EmmaX, 1400) or (ApprovalCheck(EmmaX, 700) and EmmaX.SeenChest and EmmaX.SeenPussy) or not Player.Male:
                                    ch_e "Полагаю, я могу остаться ненадолго. . ."
                                    $ StayCount.append(EmmaX)
                        else:
                                    ch_e "Боюсь, мне пора идти."
                elif Occupants[0] is LauraX:
                        if ApprovalCheck(LauraX, 1400) or (ApprovalCheck(LauraX, 700) and LauraX.SeenChest and LauraX.SeenPussy) or not Player.Male:
                                    ch_l "Ну, мне пока нечем заняться."
                                    $ StayCount.append(LauraX)
                        else:
                                    ch_l "Мне пора идти."
                elif Occupants[0] is JeanX:
                        if ApprovalCheck(JeanX, 1400) or (ApprovalCheck(JeanX, 700) and JeanX.SeenChest and JeanX.SeenPussy) or not Player.Male:
                                    ch_j "Конечно, почему бы и нет."
                                    $ StayCount.append(JeanX)
                        else:
                                    ch_j "Ха, нет."
                elif Occupants[0] is StormX:
                        if ApprovalCheck(StormX, 700) or not Player.Male:
                                    ch_s "Думаю, я могла бы остаться."
                                    $ StayCount.append(StormX)
                        else:
                                    ch_s "Честно говоря, у меня есть более важные дела, [StormX.Petname]."
                elif Occupants[0] is JubesX:
                        if ApprovalCheck(JubesX, 1400) or (ApprovalCheck(JubesX, 700) and JubesX.SeenChest and JubesX.SeenPussy) or not Player.Male:
                                    ch_v "Думаю, я могу задержаться ненадолго. . ."
                                    $ StayCount.append(JubesX)
                        else:
                                    ch_v "У меня дела, [JubesX.Petname]."
                elif Occupants[0] is GwenX:
                        if ApprovalCheck(GwenX, 1400) or (ApprovalCheck(GwenX, 700) and GwenX.SeenChest and GwenX.SeenPussy) or not Player.Male:
                                    ch_g "Я могу задержаться. . ."
                                    $ StayCount.append(GwenX)
                        else:
                                    ch_g "Вообще-то, [GwenX.Petname], у меня дела."
                elif Occupants[0] is BetsyX:
                        if ApprovalCheck(BetsyX, 1400) or (ApprovalCheck(BetsyX, 700) and BetsyX.SeenChest and BetsyX.SeenPussy) or not Player.Male:
                                    ch_b "Соблазнительное предложение. . ."
                                    $ StayCount.append(BetsyX)
                        else:
                                    ch_b "Боюсь, [BetsyX.Petname], мне пора."
                elif Occupants[0] is DoreenX:
                        if ApprovalCheck(DoreenX, 1400) or (ApprovalCheck(DoreenX, 700) and DoreenX.SeenChest and DoreenX.SeenPussy) or not Player.Male:
                                    ch_d "Наверное, можно. . ."
                                    $ StayCount.append(DoreenX)
                        else:
                                    ch_d "Мне правда пора идти, [DoreenX.Petname]."
                elif Occupants[0] is WandaX:
                        if ApprovalCheck(WandaX, 1200) or (ApprovalCheck(WandaX, 600) and WandaX.SeenChest and WandaX.SeenPussy) or not Player.Male:
                                    ch_w "Да? Что такое?"
                                    $ StayCount.append(WandaX)
                        else:
                                    ch_w "Нет, мне пора идти, [WandaX.Petname]."
                #end first girls

                if len(Occupants) >= 2:
                    #second girls
                    if Occupants[1] is RogueX:
                        if ApprovalCheck(RogueX, 1200) or (ApprovalCheck(RogueX, 600) and RogueX.SeenChest and RogueX.SeenPussy) or not Player.Male:
                                if StayCount:
                                    #If Rogue said yes
                                    ch_r "Я тоже могла бы остаться. . ."
                                else:

                                    ch_r "Ну, я, наверное, могла бы остаться."
                                $ StayCount.append(RogueX)
                        else:
                                if StayCount:#RogueCount > 1:
                                    #If Rogue said yes
                                    ch_r "А я не могу. . ."
                                else:

                                    ch_r "Я тоже должна идти."

                    elif Occupants[1] is KittyX:
                        if ApprovalCheck(KittyX, 1400) or (ApprovalCheck(KittyX, 700) and KittyX.SeenChest and KittyX.SeenPussy) or not Player.Male:
                                if StayCount:
                                    #If Kitty said yes
                                    ch_k "Думаю, я тоже могла бы остаться. . ."
                                else:

                                    ch_k "Ну, я могла бы остаться."
                                $ StayCount.append(KittyX)
                        else:
                                if StayCount:#RogueCount > 1:
                                    #If Kitty said yes
                                    ch_k "А мне нужно идти. . ."
                                else:

                                    ch_k "Да, мне тоже нужно идти."

                    elif Occupants[1] is EmmaX:
                        if not "classcaught" in EmmaX.History or "three" not in EmmaX.History:
                                    ch_e "Мне надо идти. . ."
                        elif ApprovalCheck(EmmaX, 1400) or (ApprovalCheck(EmmaX, 700) and EmmaX.SeenChest and EmmaX.SeenPussy) or not Player.Male:
                                if StayCount:
                                    #If Emma said yes
                                    ch_e "Полагаю, я тоже могла бы остаться. . ."
                                else:
                                    #If Emma said no
                                    ch_e "Но -я- могла бы остаться."
                                $ StayCount.append(EmmaX)
                        else:
                                if StayCount:
                                    #If Emma said yes
                                    ch_e "Ну а мне срочно нужно уйти. . ."
                                else:

                                    ch_e "Да, пойдем."

                    elif Occupants[1] is LauraX:
                        if ApprovalCheck(LauraX, 1400) or (ApprovalCheck(LauraX, 700) and LauraX.SeenChest and LauraX.SeenPussy) or not Player.Male:
                                if StayCount:
                                    #If Laura said yes
                                    ch_l "Я тоже могла бы остаться. . ."
                                else:

                                    ch_l "Я могла бы остаться."
                                $ StayCount.append(LauraX)
                        else:
                                if StayCount:
                                    #If Laura said yes
                                    ch_l "А я должна идти. . ."
                                else:

                                    ch_l "Да, я тоже."

                    elif Occupants[1] is JeanX:
                        if ApprovalCheck(JeanX, 1000) or (ApprovalCheck(JeanX, 600) and JeanX.SeenChest and JeanX.SeenPussy) or not Player.Male:
                                if StayCount:
                                    #If Jean said yes
                                    ch_j "Думаю, я тоже могла бы остаться. . ."
                                else:

                                    ch_j "Я могла бы остаться."
                                $ StayCount.append(JeanX)
                        else:
                                if StayCount:
                                    #If Jean said yes
                                    ch_j "А я ухожу. . ."
                                else:

                                    ch_j "Ага."

                    elif Occupants[1] is StormX:
                        if ApprovalCheck(StormX, 700) or not Player.Male:
                                if StayCount:
                                    #If Storm said yes
                                    ch_s "Я тоже могу остаться. . ."
                                else:

                                    ch_s "А я могла бы задержаться ненадолго. . ."
                                $ StayCount.append(StormX)
                        else:
                                if StayCount:
                                    #If Storm said yes
                                    ch_s "Что ж, боюсь, мне пора идти. . ."
                                else:

                                    ch_s "Да, пошли."

                    elif Occupants[1] is JubesX:
                        if ApprovalCheck(JubesX, 1400) or (ApprovalCheck(JubesX, 700) and JubesX.SeenChest and JubesX.SeenPussy) or not Player.Male:
                                if StayCount:
                                    #If Jubes said yes
                                    ch_v "Я тоже могу остаться. . ."
                                else:

                                    ch_v "Ну, а -я- не настолько занята. . ."
                                $ StayCount.append(JubesX)
                        else:
                                if StayCount:#RogueCount > 1:
                                    #If Jubes said yes
                                    ch_v "У меня сейчас очень много дел. . ."
                                else:

                                    ch_v "А, да, мне тоже пора. . ."

                    elif Occupants[1] is GwenX:
                        if ApprovalCheck(GwenX, 1400) or (ApprovalCheck(GwenX, 700) and GwenX.SeenChest and GwenX.SeenPussy) or not Player.Male:
                                if StayCount:
                                    #If Gwen said yes
                                    ch_g "Ладно, я посмотрю, чем это закончится. . ."
                                else:

                                    ch_g "Хорошо, тогда до встречи. . ."
                                $ StayCount.append(GwenX)
                        else:
#                                if StayCount:#RogueCount > 1:
#                                    #If Gwen said yes
#                                    ch_g "Sorry, can't stick around. . ."
#                                else:
#                                    #If Gwen said no
                                    ch_g "Прости, не могу остаться. . ."

                    elif Occupants[1] is BetsyX:
                        if ApprovalCheck(BetsyX, 1400) or (ApprovalCheck(BetsyX, 700) and BetsyX.SeenChest and BetsyX.SeenPussy) or not Player.Male:
                                if StayCount:
                                    #If BetsyX said yes
                                    ch_b "Пожалуй, я могла бы остаться ненадолго. . ."
                                else:
                                    #If BetsyX said no
                                    ch_b "Я, пожалуй, могу остаться. . ."
                                $ StayCount.append(BetsyX)
                        else:
                                if StayCount:#RogueCount > 1:
                                    #If BetsyX said yes
                                    ch_b "К сожалению, мне пора идти. . ."
                                else:
                                    #If BetsyX said no
                                    ch_b "У меня тоже остались кое-какие дела. . ."

                    elif Occupants[1] is DoreenX:
                        if ApprovalCheck(DoreenX, 1400) or (ApprovalCheck(DoreenX, 700) and DoreenX.SeenChest and DoreenX.SeenPussy) or not Player.Male:
                                if StayCount:
                                    #If DoreenX said yes
                                    ch_d "Думаю, я могла бы задержаться ненадолго. . ."
                                else:
                                    #If DoreenX said no
                                    ch_d "Я, наверное, могу остаться, [DoreenX.Petname]."
                                $ StayCount.append(DoreenX)
                        else:
                                if StayCount:#RogueCount > 1:
                                    #If DoreenX said yes
                                    ch_d "Ну, а мне пора идти."
                                else:
                                    #If DoreenX said no
                                    ch_d "Мне тоже пора идти. . ."

                    elif Occupants[1] is WandaX:
                        if ApprovalCheck(WandaX, 1400) or (ApprovalCheck(WandaX, 700) and WandaX.SeenChest and WandaX.SeenPussy) or not Player.Male:
                                if StayCount:
                                    #If WandaX said yes
                                    ch_w "Ладно, я могу остаться. . ."
                                else:
                                    #If WandaX said no
                                    ch_w "Я могу остаться, [WandaX.Petname]."
                                $ StayCount.append(WandaX)
                        else:
                                if StayCount:#RogueCount > 1:
                                    #If WandaX said yes
                                    ch_w "Ну, а мне действительно пора идти."
                                else:
                                    #If WandaX said no
                                    ch_w "Мне тоже пора идти."

                #end none have showered yet
            if len(Occupants) > len(StayCount):
                    #if either said no. If they're at StayCount = 2 here, they have already agreed.
                    menu:
                        extend ""
                        "Ладно, тогда увидимся позже.":
                                if RogueX.Loc == bg_current and RogueX not in StayCount:
                                    ch_r "Ага, до скорого."
                                if KittyX.Loc == bg_current and KittyX not in StayCount:
                                    ch_k "Пока!"
                                if EmmaX.Loc == bg_current and EmmaX not in StayCount:
                                    ch_e "Да, увидимся."
                                if LauraX.Loc == bg_current and LauraX not in StayCount:
                                    ch_l "Ага."
                                if JeanX.Loc == bg_current and JeanX not in StayCount:
                                    ch_j "Ладно."
                                if StormX.Loc == bg_current and StormX not in StayCount:
                                    ch_s "Да, увидимся."
                                if JubesX.Loc == bg_current and JubesX not in StayCount:
                                    ch_v "Увидимся!"
                                if GwenX.Loc == bg_current and GwenX not in StayCount:
                                    ch_g "Пока-пока!"
                                if BetsyX.Loc == bg_current and BetsyX not in StayCount:
                                    ch_b "Пока!"
                                if DoreenX.Loc == bg_current and DoreenX not in StayCount:
                                    ch_d "Увидимся!"
                                if WandaX.Loc == bg_current and WandaX not in StayCount:
                                    ch_w "Ага, увидимся."

                        "Уверена, что тщательно помылась?" if Showered:
                                $ Line = "spot"

                        #fix Add "Take off your own clothes" option.

                        "Может ты останешься и посмотришь?":
                                $ Line = "watch me"

                        "Но я не успела насмотреться." if Showered and not Player.Male:
                                $ Line = "watch you"

                        "Но я не успел насмотреться." if Showered and Player.Male:
                                $ Line = "watch you"
                    if Line:
                        $ BO = Occupants[:]
                        python:
                            for BX in BO:
                                #loops through and adds populates Occupants with locals
                                if BX.Loc == bg_current and BX not in StayCount:
                                        if BX is EmmaX and (not "classcaught" in EmmaX.History or (StayCount and "three" not in EmmaX.History)):
                                                #if it's Emma, and she isn't comfortable with threesomes or public stuff, skip her
                                                pass
                                        elif BX is JeanX and ApprovalCheck(BX, 600):
                                                StayCount.append(BX)
                                        elif BX is StormX or BX is WandaX:
                                            if ApprovalCheck(BX, 700, "LO"):
                                                StayCount.append(BX)
                                        elif ApprovalCheck(BX, 1200,Alt=[[KittyX],1400]) or (ApprovalCheck(BX, 600,Alt=[[KittyX],700]) and BX.SeenChest and BX.SeenPussy): #1400/700 for Kitty?
                                                StayCount.append(BX)
                                        elif Line == "spot" and ApprovalCheck(BX, 1000, "LI",Alt=[[KittyX],1200]):   #1200 for Kitty?
                                                StayCount.append(BX)
                                        elif Line == "watch you" and ApprovalCheck(BX, 600, "O",Alt=[[EmmaX],500]):   #500 for Emma?
                                                StayCount.append(BX)
                                        #else, she doesn't agree

                        if StayCount and not Player.Male:
                                # if you're a girl and they don't know you're into girls, it checks, and they leave if they aren't into that
                                if len(StayCount) > 1:
                                    call expression StayCount[1].Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                                    if "nogirls" in StayCount[1].History:
                                            $ StayCount.remove(StayCount[1])
                                call expression StayCount[0].Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                                if "nogirls" in StayCount[0].History:
                                        $ StayCount.remove(StayCount[0])
                        if Line == "spot":
                                #"Sure you got every spot?"
                                if StayCount:
                                        #if at least one girl agreed to stay
                                        if StayCount[0] is RogueX: #RogueCount == 2:
                                            #Rogue agreed
                                            ch_r "Ладно, мне не помешает еще немного помыться."
                                        elif StayCount[0] is KittyX:

                                            ch_k "Ох, думаю, я могу ненадолго задержаться."
                                        elif StayCount[0] is EmmaX:

                                            ch_e "Пожалуй, я могла бы задержаться. . ."
                                        elif StayCount[0] is LauraX:

                                            ch_l "Да, возможно. . ."
                                        elif StayCount[0] is JeanX:

                                            ch_j "Ладно, задержусь. . ."
                                        elif StayCount[0] is StormX:

                                            ch_s "Что ж, еще один заход не повредит. . ."
                                        elif StayCount[0] is JubesX:

                                            ch_v "Ну, никогда нельзя быть -слишком- чистым. . ."
                                        elif StayCount[0] is GwenX:

                                            ch_g "Думаю, я могу пойти еще раз. . ."
                                        elif StayCount[0] is BetsyX:
                                            #Betsy agreed
                                            ch_b "Пожалуй, никогда нельзя быть -слишком- чистым. . ."
                                        elif StayCount[0] is DoreenX:
                                            #Doreen agreed
                                            ch_d "Наверное. . . можно и еще раз помыться. . ."
                                        elif StayCount[0] is WandaX:
                                            #Wanda agreed
                                            ch_w "Конечно, это может быть интересно. . ."
                                if RogueX.Loc == bg_current and RogueX not in StayCount: #RogueCount == 1:
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Ну, [RogueX.Petname], думаю мое присутствие здесь будет лишним."
                                    else:
                                            ch_r "Нет, [RogueX.Petname], больше я здесь не задержусь."
                                if KittyX.Loc == bg_current and KittyX not in StayCount: # KittyCount == 1:
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Ох, думаю, тут и без меня[KittyX.like]все хорошо."
                                            ch_k "Увидимся позже, [KittyX.Petname]."
                                    else:
                                            ch_k "Ха, я безупречно чиста, [KittyX.Petname], увидимся позже."
                                if EmmaX.Loc == bg_current and EmmaX not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "Что ж, похоже, о тебе и без меня позаботятся."
                                            ch_e "Я пойду, [EmmaX.Petname]."
                                    else:
                                            ch_e "Боюсь, что нет, [EmmaX.Petname], я пойду."
                                if LauraX.Loc == bg_current and LauraX not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "Похоже, вы тут сами разберетесь."
                                            ch_l "Я пошла, [LauraX.Petname]."
                                    else:
                                            ch_l "Я пошла."
                                if JeanX.Loc == bg_current and JeanX not in StayCount:
                                    #Jean refused
                                    if StayCount:
                                            ch_j "Ну, похоже, вы, ребята, собираетесь повеселиться."
                                            ch_j "Я пойду, [JeanX.Petname]."
                                    else:
                                            ch_j "Я пойду."
                                if StormX.Loc == bg_current and StormX not in StayCount:
                                    #Storm refused
                                    if StayCount:
                                            ch_s "Похоже, вы сейчас будете заняты."
                                            ch_s "Я пойду, [StormX.Petname]."
                                    else:
                                            ch_s "Я очень сомневаюсь, что могла бы остаться, [StormX.Petname], Я пойду."
                                if JubesX.Loc == bg_current and JubesX not in StayCount: # JubesCount == 1:
                                    #Jubes refused
                                    if StayCount:
                                            ch_v "Нее, я думаю, вы и без меня справитесь."
                                            ch_v "Увидимся, ребята."
                                    else:
                                            ch_v "Нее, мне и так хорошо. Увидимся, [JubesX.Petname]."
                                if GwenX.Loc == bg_current and GwenX not in StayCount: # GwenCount == 1:
                                    #Gwen refused
                                    if StayCount:
                                            ch_g "Ладно, развлекайтесь, ребята."
                                            ch_g "Пока-пока."
                                    else:
                                            ch_g "Я так не думаю. Пока-пока, [GwenX.Petname]."
                                if BetsyX.Loc == bg_current and BetsyX not in StayCount: # BetsyCount == 1:
                                    #Betsy refused
                                    if StayCount:
                                            ch_b "Что ж, вы тут и без меня -хорошо- проведете время. . ."
                                    else:
                                            ch_b "Мне правда пора, [BetsyX.Petname]."
                                if DoreenX.Loc == bg_current and DoreenX not in StayCount: # DoreenCount == 1:
                                    #Doreen refused
                                    if StayCount:
                                            ch_d "Ладно, ребята, развлекайтесь. . ."
                                    else:
                                            ch_d "Нет, мне правда нужно идти, [DoreenX.Petname]."
                                if WandaX.Loc == bg_current and WandaX not in StayCount: # WandaCount == 1:
                                    #Wanda refused
                                    if StayCount:
                                            ch_w "Хех, веселитесь, ребята. . ."
                                    else:
                                            ch_w "Нет, мне действительно пора идти, [WandaX.Petname]."
                                #end "missed a spot?"

                        elif Line == "watch me":
                                #"Maybe you could stay and watch?"
                                if StayCount:
                                        if StayCount[0] is RogueX:
                                            #Rogue agreed
                                            ch_r "Да, думаю, мне понравится."
                                        elif StayCount[0] is KittyX:

                                            ch_k "Я. . . думаю, я не против. . ."
                                        elif StayCount[0] is LauraX:

                                            ch_l "Ладно, давай посмотрим, что ты можешь показать."
                                        elif StayCount[0] is JeanX:

                                            ch_j "Ох, это должно быть хорошо. . ."
                                        elif StayCount[0] is StormX:

                                            ch_s "Полагаю, можно. . ."
                                        elif StayCount[0] is JubesX:

                                            ch_v ". . . Ладно."
                                        elif StayCount[0] is GwenX:

                                            ch_g ". . . Ладно, я не против. . ."
                                        elif StayCount[0] is BetsyX:
                                            #Betsy agreed
                                            ch_b ". . . Это -может быть- интересно. . ."
                                        elif StayCount[0] is DoreenX:
                                            #Doreen agreed
                                            ch_d ". . . Это -может быть- весело. . ."
                                        elif StayCount[0] is WandaX:
                                            #Wanda agreed
                                            ch_w ". . . Лааааднооо. . ."

                                if RogueX.Loc == bg_current and RogueX not in StayCount: #RogueCount == 1:
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Ох, что ж, я лучше это пропущу, [RogueX.Petname]."
                                    else:
                                            ch_r "Мне лучше это пропустить, [RogueX.Petname]."
                                if KittyX.Loc == bg_current and KittyX not in StayCount: # KittyCount == 1:
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Ну[KittyX.like]мне не нужно этого видеть."
                                            ch_k "Увидимся, [KittyX.Petname]."
                                    else:
                                            ch_k "[KittyX.Like]мне не нужно этого видеть."
                                if EmmaX.Loc == bg_current and EmmaX not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "Похоже, у тебя и без меня достаточно зрителей."
                                            ch_e "Я пойду, [EmmaX.Petname]."
                                    else:
                                            ch_e "Думаю, я обойдусь без этого, [EmmaX.Petname], мне лучше уйти."
                                if LauraX.Loc == bg_current and LauraX not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "Она составит тебе компанию."
                                            ch_l "А я пошла, [LauraX.Petname]."
                                    else:
                                            ch_l "Я пошла."
                                if JeanX.Loc == bg_current and JeanX not in StayCount:
                                    #Jean refused
                                    if StayCount:
                                            ch_j "Ну, похоже, вы, ребята, собираетесь повеселиться."
                                            ch_j "Я лучше пойду отсюда, [JeanX.Petname]."
                                    else:
                                            ch_j "Я лучше пойду отсюда."
                                if StormX.Loc == bg_current and StormX not in StayCount:
                                    #Storm refused
                                    if StayCount:
                                            ch_s "Ох, я думаю, кому-то нетерпится увидеть шоу."
                                            ch_s "Я пойду, [StormX.Petname]."
                                    else:
                                            ch_s "Не понимаю, зачем мне это, [StormX.Petname]. Я пойду."
                                if JubesX.Loc == bg_current and JubesX not in StayCount: # JubesCount == 1:
                                    #Jubes refused
                                    if StayCount:
                                            ch_v "Эм, нет, спасибо. . ."
                                            ch_v "Увидимся позже, [JubesX.Petname]."
                                    else:
                                            ch_v "Эм, нет, спасибо."
                                if GwenX.Loc == bg_current and GwenX not in StayCount: # GwenCount == 1:
                                    #Gwen refused
                                    if StayCount:
                                            ch_g "Ага. . . Я так не думаю.. . ."
                                            ch_g "Увидимся позже, [GwenX.Petname]."
                                    else:
                                            ch_g "Спасибо за предложение, но. . . нет."
                                if BetsyX.Loc == bg_current and BetsyX not in StayCount: # BetsyCount == 1:
                                    #BetsyX refused
                                    if StayCount:
                                            ch_b "Хм. . . я бы не хотела этого видеть. . ."
                                            ch_b "Увидимся, [BetsyX.Petname]."
                                    else:
                                            ch_b "Я ценю твое предложение, но я вынуждена отказаться."
                                if DoreenX.Loc == bg_current and DoreenX not in StayCount: # DoreenCount == 1:
                                    #DoreenX refused
                                    if StayCount:
                                            ch_d "Ага. . . я так не думаю. . ."
                                            ch_d "Увидимся, [DoreenX.Petname]."
                                    else:
                                            ch_d "Спасибо за предложение, но я не могу, правда."
                                if WandaX.Loc == bg_current and WandaX not in StayCount: # WandaCount == 1:
                                    #WandaX refused
                                    if StayCount:
                                            ch_w "Эм. . . я не могу. . ."
                                            ch_w "Увидимся, [WandaX.Petname]."
                                    else:
                                            ch_w "Звучит весело, но я не могу."
                                #end "Watch me"

                        elif Line == "watch you":
                                #"But I didn't get to watch."
                                if StayCount:
                                        if StayCount[0] is RogueX:
                                            #Rogue agreed
                                            ch_r "Ну, я не против небольшого шоу."
                                        elif StayCount[0] is KittyX:

                                            ch_k "Ты хочешь поглазеть на меня. . ."
                                            ch_k "Ладно."
                                        elif StayCount[0] is EmmaX:

                                            ch_e "Полагаю, я не могу винить тебя за это. . ."
                                        elif StayCount[0] is LauraX:

                                            ch_l "А? Как хочешь."
                                        elif StayCount[0] is JeanX:

                                            ch_j "Ну, мы не можем оставить тебя без маленького представления. . ."
                                        elif StayCount[0] is StormX:

                                            ch_s ". . ."
                                        elif StayCount[0] is JubesX:

                                            ch_v "Ну. . . Думаю, мы должны это исправить. . ."
                                        elif StayCount[0] is GwenX:

                                            ch_g "О, хорошо. . ."
                                        elif StayCount[0] is BetsyX:
                                            #Betsy agreed
                                            ch_b ". . . что ж, я не хочу лишать тебя этого удовольствия. . ."
                                        elif StayCount[0] is DoreenX:
                                            #Doreen agreed
                                            ch_d ". . . Ох. . . ты, эм. . . хочешь посмотреть на меня. . ."
                                        elif StayCount[0] is WandaX:
                                            #Wanda agreed
                                            ch_w ". . . Ты хочешь понаблюдать за мной? . ."

                                if RogueX.Loc == bg_current and RogueX not in StayCount: #RogueCount == 1:
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Неужели? Давайте без меня."
                                            ch_r "Веселитесь, [RogueX.Petname]."
                                    else:
                                            ch_r "Мечтай, [RogueX.Petname]."
                                if KittyX.Loc == bg_current and KittyX not in StayCount: # KittyCount == 1:
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Серьезно?! Мне это не нравится."
                                            ch_k "Увидимся, [KittyX.Petname]."
                                    else:
                                            ch_k "[KittyX.Like]ни за что!"
                                if EmmaX.Loc == bg_current and EmmaX not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "Я не хочу вам мешать."
                                            ch_e "Я пойду."
                                    else:
                                            ch_e "Хм, сомневаюсь, что тебе это пойдет на пользу."
                                            ch_e "Я пойду."
                                if LauraX.Loc == bg_current and LauraX not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "Она составит тебе компанию."
                                            ch_l "А я пошла, [LauraX.Petname]."
                                    else:
                                            ch_l "Я пошла."
                                if JeanX.Loc == bg_current and JeanX not in StayCount:
                                    #Jean refused
                                    if StayCount:
                                            ch_j "Ну, похоже, вы, ребята, собираетесь повеселиться."
                                            ch_j "Я лучше пойду отсюда, [JeanX.Petname]."
                                    else:
                                            ch_j "Я лучше пойду отсюда."
                                if StormX.Loc == bg_current and StormX not in StayCount:
                                    #Storm refused
                                    if StayCount:
                                            ch_s "Что ж, развлекайтесь."
                                            ch_s "Я лучше пойду."
                                    else:
                                            ch_s "Я польщена, но нет."
                                            ch_s "Я лучше пойду."
                                if JubesX.Loc == bg_current and JubesX not in StayCount: # JubesCount == 1:
                                    #Jubes refused
                                    if StayCount:
                                            ch_v "Ладно, похоже, вам двоим будет весело и без меня."
                                            ch_v "Увидимся, [JubesX.Petname]."
                                    else:
                                            ch_v "Ага, этого не будет."
                                if GwenX.Loc == bg_current and GwenX not in StayCount: # GwenCount == 1:
                                    #Gwen refused
                                    if StayCount:
                                            ch_g "Ага. . . Я так не думаю.. . ."
                                            ch_g "Увидимся позже, [GwenX.Petname]."
                                    else:
                                            ch_g "О, мне жаль, но я пас. . ."
                                if BetsyX.Loc == bg_current and BetsyX not in StayCount: # BetsyCount == 1:
                                    #Betsy refused
                                    if StayCount:
                                            ch_b "Мне жаль, но я вынуждена тебя огорчить. . ."
                                            ch_b "Увидимся, [BetsyX.Petname]."
                                    else:
                                            ch_b "Ох, я вынуждена тебя огорчить. . ."
                                if DoreenX.Loc == bg_current and DoreenX not in StayCount: # DoreenCount == 1:
                                    #Doreen refused
                                    if StayCount:
                                            ch_d "Ты. . . хочешь посмотреть на нас? . ."
                                            ch_d "Нет. Увидимся, [DoreenX.Petname]."
                                    else:
                                            ch_d "Ты. . . хочешь посмотреть на меня? . ."
                                            ch_d "Нет. Увидимся, [DoreenX.Petname]."
                                if WandaX.Loc == bg_current and WandaX not in StayCount: # WandaCount == 1:
                                    #Wanda refused
#                                    if StayCount:
#                                            ch_w "Heh, you wanna watch? . ."
#                                            ch_w "Ha! See ya later, [WandaX.Petname]."
#                                    else:
                                            ch_w "Хех, хочешь понаблюдать? . ."
                                            ch_w "Ха! Увидимся позже, [WandaX.Petname]."
                                #end "Watch you?"

                    if len(StayCount) > 1:
                            #if there are multiple girls
                            if StayCount[1].GirlLikeCheck(StayCount[0]) > 500:
                                    #if she likes the other girl. . .
                                    if StayCount[1] is RogueX:
                                        ch_r "Наверное, я тоже могла бы."
                                    elif StayCount[1] is EmmaX:
                                        ch_e "Наверное, я не хочу оставаться в стороне. . ."
                                    elif StayCount[1] is JeanX:
                                        ch_j "Ну, это похоже будет весело.. . ."
                            else:
                                    if StayCount[1] is RogueX:
                                        ch_r "Ну, если она остается, то и я тоже!"
                                    elif StayCount[1] is EmmaX:
                                        ch_e "Я бы не хотела оставить тебя наедине. . . с ней."
                                    elif StayCount[1] is JeanX:
                                        ch_j "Хм, может и мне стоит остаться. . ."
                            if StayCount[1] is KittyX:
                                ch_k "Я. . . да, я тоже!"
                            elif StayCount[1] is LauraX:
                                ch_l "Ладно."
                            elif StayCount[1] is StormX:
                                ch_s "Что ж, полагаю, мне следует присоединиться к вам. . ."
                            elif StayCount[1] is JubesX:
                                ch_v "Эм, ага, давайте сделаем это."
                            elif StayCount[1] is GwenX:
                                ch_g "Ладно, я с вами."
                            elif StayCount[1] is BetsyX:
                                ch_b "Что ж, я бы не хотела оставаться в стороне. . ."
                            elif StayCount[1] is DoreenX:
                                ch_d "Думаю, я бы не хотела ничего пропустить. . ."
                            elif StayCount[1] is WandaX:
                                ch_w "Что ж, если никто не против. . ."
                    #end "if you asked then a question"
            $ BO = Occupants[:]
            while BO:
                    #loops through and adds populates Occupants with locals
                    #I'm leaving this one alone, because it's complicated
                    if BO[0].Loc == bg_current:
                            if BO[0] in StayCount:
                                    #If the girl Stays
                                    $ BO[0].OutfitChange("nude")
                                    $ BO[0].Water = 1
                                    $ BO[0].Spunk = []
                                    $ BO[0].RecentActions.append("showered")
                                    $ BO[0].DailyActions.append("showered")
                                    call Girl_First_Bottomless(BO[0],1)
                                    call Girl_First_Topless(BO[0],1)
                            else:
                                    #If the girl leaves
                                    call Remove_Girl(BO[0])
                            while BO[0] in Nearby:
                                    $ Nearby.remove(BO[0])
                    $ BO.remove(BO[0])

#/ / Pre-shower ends / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#/ / Showering begins / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    call Seen_First_Peen(0,0,0,1) #You get naked

    while len(StayCount) >= 2 and StayCount[1] in Nearby:
            # removes any staying characters from Nearby
            $ Nearby.remove(StayCount[1])
    while StayCount and StayCount[0] in Nearby:
            # removes any staying characters from Nearby
            $ Nearby.remove(StayCount[0])

    if Nearby and len(StayCount) < 2:
            # This value carries over from the Entry scene if there are girls who show up late
            $ renpy.random.shuffle(Nearby)

            while Nearby and (len(Nearby) + len(StayCount)) > 2:
                        # while Nearby is more than 2-Staying characters
                        $ Nearby.remove(Nearby[0]) #culls it to 1

            if len(Nearby) >= 2:
                "Как только вы заканчиваете раздеваться, [Nearby[0].Name] и [Nearby[1].Name_tvo] входят в комнату."
                $ Nearby[1].Loc = bg_current
            else:
                "Как только вы заканчиваете раздеваться, [Nearby[0].Name] входит в комнату."
            $ Nearby[0].Loc = bg_current

            $ BO = Nearby[:]

            #call Present_Check ?
            call Set_The_Scene(Dress=0)

            if RogueX in BO:# in Nearby:
                    call Seen_First_Peen(RogueX,0,1,1) #You get naked, silent reactions
                    if not Player.Male and "girltalk" not in RogueX.History and "nogirls" not in RogueX.History:
                            ch_r "Ох, привет, [RogueX.Petname]. . ."
                    elif RogueX.SeenPeen == 1:
                            $ RogueX.FaceChange("surprised",2,Eyes="down")
                            ch_r "Ох!"
                            $ RogueX.FaceChange("bemused",1,Eyes="side")
                            ch_r "Прости, я не должна была так врываться."
                    else:
                            $ RogueX.FaceChange("bemused",1,Eyes="side")
                            ch_r "Я должна быть более осторожной. . ."
            if KittyX in BO:
                    call Seen_First_Peen(KittyX,0,1,1) #You get naked, silent reactions
                    $ KittyX.FaceChange("bemused",2,Eyes="side")
                    if not Player.Male and "girltalk" not in KittyX.History and "nogirls" not in KittyX.History:
                            ch_k "Ох, привет, [KittyX.Petname]. . ."
                    elif KittyX.SeenPeen == 1:
                            ch_k "Прости! Прости! Мне надо перестать так небрежно влетать в разные места!"
                    else:
                            ch_k "Мне {i}нужно{/i} чаще стучаться. . ."
            if EmmaX in BO:
                    call Seen_First_Peen(EmmaX,0,1,1) #You get naked, silent reactions
                    if not Player.Male and "girltalk" not in EmmaX.History and "nogirls" not in EmmaX.History:
                            ch_e "Здравствуй, [EmmaX.Petname]. . ."
                    elif EmmaX.SeenPeen == 1:
                            $ EmmaX.FaceChange("surprised")
                            ch_e "Ох! Я дико извиняюсь."
                            $ EmmaX.FaceChange("sexy",Eyes="down")
                            ch_e "Надеюсь, что мы сможем встретиться снова при. . . других обстоятельствах."
                    else:
                            $ EmmaX.FaceChange("sexy",Eyes="down")
                            ch_e "Мне стоит быть внимательней. . ."
                    if "classcaught" not in EmmaX.History or ((StayCount or len(Nearby) >= 2) and "three" not in EmmaX.History):
                            #if Emma just showed up, but there are other girls around and she's not ok with that
                            "[EmmaX.Name] решает немедленно уйти."
                            call Remove_Girl(EmmaX)
                            $ BO.remove(EmmaX)
                            $ EmmaX.OutfitChange()
            if LauraX in BO:
                    call Seen_First_Peen(LauraX,0,1,1) #You get naked, silent reactions
                    if not Player.Male and "girltalk" not in LauraX.History and "nogirls" not in LauraX.History:
                            ch_l "Привет, [LauraX.Petname]. . ."
                    elif LauraX.SeenPeen == 1:
                            $ LauraX.FaceChange("surprised",Eyes="down")
                            ch_l "Оу. . . Интересно. . ."
                    else:
                            $ LauraX.FaceChange("normal",Eyes="down")
                            ch_l ". . ."
                            $ LauraX.FaceChange("normal")
                            ch_l "Думаю, мне нужно было сначала постучать."
            if JeanX in BO:
                    call Seen_First_Peen(JeanX,0,1,1) #You get naked, silent reactions
                    if not Player.Male and "girltalk" not in JeanX.History and "nogirls" not in JeanX.History:
                            pass
                    elif JeanX.SeenPeen == 1:
                            $ JeanX.FaceChange("surprised",Eyes="down")
                            ch_j "Что у нас здесь? . ."
                    else:
                            $ JeanX.FaceChange("normal",Eyes="down")
                            ch_j ". . ."
                            $ JeanX.FaceChange("normal")
                            ch_j "О, приятно было застать тебя. . . в таком виде. . ."
            if StormX in BO:
                    call Seen_First_Peen(StormX,0,1,1) #You get naked, silent reactions
                    if not Player.Male and "girltalk" not in StormX.History and "nogirls" not in StormX.History:
                            ch_s "О, здравствуй, [StormX.Petname]. . ."
                    elif StormX.SeenPeen == 1:
                            $ StormX.FaceChange("surprised")
                            ch_s "О! Приветствую."
                            $ StormX.FaceChange("sexy",Eyes="down")
                            ch_s "Вас двоих. . ."
                    else:
                            $ StormX.FaceChange("sexy",Eyes="down")
                            ch_s "Извини за вторжение. . ."
                    $ StormX.FaceChange("sexy")
            if JubesX in BO:
                    call Seen_First_Peen(JubesX,0,1,1) #You get naked, silent reactions
                    $ JubesX.FaceChange("bemused",2,Eyes="side")
                    if not Player.Male and "girltalk" not in JubesX.History and "nogirls" not in JubesX.History:
                            ch_v "О, как дела? . ."
                    elif JubesX.SeenPeen == 1:
                            ch_v "О, извини! Я была невнимательна."
                            $ JubesX.Eyes = "down"
                            pause 1
                            $ JubesX.Eyes = "side"
                            ch_v "Эм. . . привет. . ."
                    else:
                            ch_v "О, извини! Я была невнимательна."
            if GwenX in BO:
                    call Seen_First_Peen(GwenX,0,1,1) #You get naked, silent reactions
                    $ GwenX.FaceChange("bemused",2,Eyes="side")
                    if not Player.Male and "girltalk" not in GwenX.History and "nogirls" not in GwenX.History:
                            ch_g "Hey, [GwenX.Petname]. . ."
                    elif GwenX.SeenPeen == 1:
                            ch_g "Ох!"
                            $ GwenX.Eyes = "down"
                            ch_g "Оооохх. . .{w=1.0}{nw}"
                            $ GwenX.Eyes = "side"
                            ch_g "Оооохх. . . привет. . ."
                            ch_g "Извини за вторжение, но. . ."
                    else:
                            ch_g "Ох! Не волнуйся, я ничего не видела. . ."
            if BetsyX in BO:
                    call Seen_First_Peen(BetsyX,0,1,1) #You get naked, silent reactions
                    $ BetsyX.FaceChange("bemused",2,Eyes="side")
                    if not Player.Male and "girltalk" not in BetsyX.History and "nogirls" not in BetsyX.History:
                            ch_b "О, [BetsyX.Petname], приветствую. . ."
                    elif BetsyX.SeenPeen == 1:
                            $ BetsyX.FaceChange("surprised")
                            ch_b "Ох!"
                            $ BetsyX.Eyes = "side"
                            ch_b "Пардон. . ."
                    else:
                            ch_b "Ох! Пардон, я просто проходила мимо. . ."
            if DoreenX in BO:
                    call Seen_First_Peen(DoreenX,0,1,1) #You get naked, silent reactions
                    $ DoreenX.FaceChange("bemused",2,Eyes="side")
                    if not Player.Male and "girltalk" not in DoreenX.History and "nogirls" not in DoreenX.History:
                            ch_d "О, [DoreenX.Petname], привет. . ."
                    elif DoreenX.SeenPeen == 1:
                            $ DoreenX.FaceChange("surprised")
                            ch_d "Ох!"
                            $ DoreenX.Eyes = "side"
                            ch_d "Извини!"
                    else:
                            ch_d "Ох! Извини, я просто хотела. . . принять душ. . ."

            if WandaX in BO:
                    call Seen_First_Peen(WandaX,0,1,1) #You get naked, silent reactions
                    $ WandaX.FaceChange("bemused",1)
                    if not Player.Male and "girltalk" not in WandaX.History and "nogirls" not in WandaX.History:
                            ch_w "О, привет. . ."
                    elif WandaX.SeenPeen == 1:
                            $ WandaX.FaceChange("surprised")
                            ch_w "Ох."
                            $ WandaX.FaceChange("sly")
                            ch_w "Привет."
                    else:
                            ch_w "О, привет. . ."

            if EmmaX in StayCount and "three" not in EmmaX.History:
                            #if Emma was already here, but there are other girls around and she's not ok with that
                            if len(BO) >= 2:
                                    "Увидев, как заходят другие девушки, [EmmaX.Name] быстро извиняется и уходит."
                            else:
                                    "Увидев, как заходит [BO[0].Name], [EmmaX.Name] быстро извиняется и уходит."
                            $ StayCount.remove(EmmaX)
                            call Remove_Girl(EmmaX)
                            $ EmmaX.OutfitChange()

            if BO:
                #if there are still girls around to join in. . .
                if ApprovalCheck(BO[0], 1200) or (not Player.Male and "girltalk" not in BO[0].History and "nogirls" not in BO[0].History):
                        $ StayCount.append(BO[0])
                if len(BO) >=2  and len(StayCount) < 2 and (ApprovalCheck(BO[1], 1200) or (not Player.Male and "girltalk" not in BO[0].History and "nogirls" not in BO[0].History)):
                        $ StayCount.append(BO[1])

                if len(BO) >=2:
                        if BO[0] not in StayCount and BO[1] not in StayCount:
                                "Они обе разворачиваются и уходят."
                                call Remove_Girl(BO[0])
                                call Remove_Girl(BO[1])
                                $ BO = []
                        elif BO[0] not in StayCount:
                                "[BO[0].Name] разворачивается и уходит, но не [BO[1].Name]."
                                call Remove_Girl(BO[0])
                                $ BO.remove(BO[0])
                        elif BO[1] not in StayCount:
                                "[BO[1].Name] разворачивается и уходит, но не [BO[0].Name]."
                                call Remove_Girl(BO[1])
                                $ BO.remove(BO[1])
                elif BO[0] not in StayCount:
                                "Она разворачивается и уходит."
                                call Remove_Girl(BO[0])
                                $ BO.remove(BO[0])

                while BO:
                        #loops deals with "Nearby"s joining the party, removes others
                        #If Rogue Stays
                        $ BO[0].OutfitChange("nude")
                        $ BO[0].Water = 1
                        $ BO[0].Spunk = []
                        $ BO[0].RecentActions.append("showered")
                        $ BO[0].DailyActions.append("showered")
                        call Girl_First_Bottomless(BO[0],1)
                        call Girl_First_Topless(BO[0],1)
                        if BO[0] is RogueX:
                                    ch_r "Я не прочь остаться."
                        elif BO[0] is KittyX:
                                    ch_k "Я {i}могла бы{/i} присоединиться."
                        elif BO[0] is EmmaX:
                                    ch_e "Но мне бы не помешало немного пообщаться."
                        elif BO[0] is LauraX:
                                    ch_l "Подвинься."
                        elif BO[0] is JeanX:
                                    ch_j "Оставь и мне горячей воды."
                        elif BO[0] is StormX:
                                    ch_s "О, тогда до свидания. . ."
                        elif BO[0] is JubesX:
                                    ch_v "Ну, я всегда могу присоединиться к тебе."
                        elif BO[0] is GwenX:
                                    ch_g "Тебе потереть спинку?"
                        elif BO[0] is BetsyX:
                                    ch_b "Я не против составить тебе компанию. . ."
                        elif BO[0] is DoreenX:
                                    ch_d "Я могу остаться. . ."
                        elif BO[0] is WandaX:
                                    ch_w "Я не против присоединиться. . ."
                        $ BO.remove(BO[0])

    #End "girl crashes in"

    $ Round -= 30 if Round >= 30 else Round
    $ Trigger = 0

    if StayCount:
                #If at least one stays
                if len(StayCount) > 1 and StayCount[0] == StayCount[1]:
                        $ StayCount.remove(StayCount[0])
                if len(StayCount) > 1:
                        #If both stay
                        call Shift_Focus(StayCount[0], StayCount[1])
                        "Вы быстро принимаете душ с [StayCount[0].Name_tvo] и [StayCount[1].Name_tvo]."
                else:
                        call Shift_Focus(StayCount[0])
                        "Вы быстро принимаете душ с [StayCount[0].Name_tvo]."

                call Shower_Sex

                if StayCount[0] is RogueX:
                        #Rogue agreed
                        ch_r "Это было очень приятно, [RogueX.Petname]."
                elif StayCount[0] is KittyX:

                        ch_k "Это было. . . приятно."
                elif StayCount[0] is EmmaX:

                        ch_e "Это было. . . забавно."
                elif StayCount[0] is LauraX:

                        ch_l "Ну, это было весело."
                elif StayCount[0] is JeanX:

                        ch_j "Это было весело."
                elif StayCount[0] is StormX:

                        ch_s "Ах, это было расслабляюще."
                elif StayCount[0] is JubesX:

                        ch_v "Это было весело, [JubesX.Petname]."
                elif StayCount[0] is GwenX:

                        ch_g "Это было весело."
                elif StayCount[0] is BetsyX:
                        #Betsy agreed
                        ch_b "Это было очень приятно."
                elif StayCount[0] is DoreenX:
                        #Doreen agreed
                        ch_d "Это было весело!"
                elif StayCount[0] is WandaX:
                        #Wanda agreed
                        ch_w "Что ж, мне понравилось."


                if len(StayCount) > 1:
                        #if there are multiple girls
                        if StayCount[1] is RogueX:
                                #Rogue too
                                ch_r "Ага."
                        elif StayCount[1] is KittyX:

                                ch_k "Ага, мне было весело."
                        elif StayCount[1] is EmmaX:

                                ch_e "Действительно."
                        elif StayCount[1] is LauraX:

                                ch_l "Ага."
                        elif StayCount[1] is JeanX:

                                ch_j "Ага, согласна."
                        elif StayCount[1] is StormX:

                                ch_s "Конечно."
                        elif StayCount[1] is JubesX:

                                ch_v "Ага, точно."
                        elif StayCount[1] is GwenX:

                                ch_g "Ага."
                        elif StayCount[1] is BetsyX:
                                #Betsy too
                                ch_b "Действительно."
                        elif StayCount[1] is DoreenX:
                                #Doreen too
                                ch_d "Ага!"
                        elif StayCount[1] is WandaX:
                                #Wanda too
                                ch_w "Конечно."

    else:
                #solo shower
                $ Line = "Вы принимаете короткий душ" + renpy.random.choice([". Никто вас не беспокоит.",
                        ". Несколько человек приходят и уходят.",
                        ". Это было освежающе."])
                "[Line]"
    #insert random events here
    $ Player.RecentActions.append("showered")
    $ Player.DailyActions.append("showered")
    while "scent" in Player.DailyActions:
            $ Player.DailyActions.remove("scent")

    call Get_Dressed
    $ Options = TotalGirls[:]
    python:
        for BX in Options:
            #while there are still girls to do or the Mode is exit. . .
            if BX.Loc == bg_current:
                    BX.OutfitChange("towel")
    $ Options = []
#    if Round < 5:
#        if Current_Time != "Night":
#                call Wait
#                call Girls_Location
#                call Set_The_Scene
#        else:
#                $ renpy.pop_call()
#                "After the shower, it's getting late, you head back to your room."
#                jump Player_Room
    return
# End Showering / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Shower Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Shower_Sex(Options=0,Line=0):
        #called from showering if sex is on the table.
        if len(StayCount) > 1 and (ApprovalCheck(StayCount[1], 1800,Check=1) > ApprovalCheck(StayCount[0], 1800,Check=1)):
                $ renpy.random.shuffle(StayCount) #swaps girls if second girl likes you more
        call Shift_Focus(StayCount[0])

        $ D20 = renpy.random.randint(1,20)
        $ D20 += 5 if ApprovalCheck(StayCount[0], 1800) else 0 #bonus if girl really likes you

        if "showered" in Player.RecentActions:
                $ D20 = 0
        elif not Player.Male and "girltalk" not in StayCount[0].History and not ApprovalCheck(StayCount[0], 1200):
                # if you're a girl and they haven't talked about it yet. . .
                $ D20 = 0

        $ StayCount[0].FaceChange("sly")
        #A set
        if len(StayCount) > 1 and D20 >= 10:
                "При этом обе девушки прижимаются своими телами к ​​вашему."
                $ Line = StayCount[0].Name
                call Close_Launch(StayCount[0],StayCount[1])
        elif D20 >= 5:
                "При этом [StayCount[0].Name] прижимается своим телом к вашему."
                $ Line = "She"
                call Close_Launch(StayCount[0])
        else:
                $ Line = renpy.random.choice(["Никто вас не беспокоит.",
                    "Несколько человек приходят и уходят.",
                    "Это было освежающе."])
                "[Line]"
                if len(StayCount) > 1:
                        $ StayCount[0].Statup("Lust", 50, 15)
                        $ StayCount[1].Statup("Lust", 50, 15)
                        $ StayCount[0].Statup("Lust", 90, 10)
                        $ StayCount[1].Statup("Lust", 90, 10)
                        "Вы прекрасно видели, как они моются, но они, кажется, ни капли не возражали."
                        $ StayCount[0].GLG(StayCount[1],600,4,1)
                        $ StayCount[1].GLG(StayCount[0],600,4,1)
                        $ StayCount[0].GLG(StayCount[1],800,2,1)
                        $ StayCount[1].GLG(StayCount[0],800,2,1)
                else:
                        $ StayCount[0].Statup("Lust", 50, 15)
                        $ StayCount[0].Statup("Lust", 90, 10)
                        "Вы прекрасно видели, как она моется, но она, кажется, ни капли не возражала."
                return

        if Line:
            if len(StayCount) > 1:
                    $ StayCount[0].Statup("Lust", 50, 5)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ StayCount[1].Statup("Lust", 50, 5)
                    $ StayCount[1].Statup("Lust", 70, 3)
            else:
                    $ StayCount[0].Statup("Lust", 50, 6)
                    $ StayCount[0].Statup("Lust", 70, 3)
            $ Player.Statup("Focus", 50, 5)
            $ Player.Statup("Focus", 80, 2)
            menu:
                extend ""
                "Продолжать?":
                        call expression StayCount[0].Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                        if len(StayCount) > 1:
                                call expression StayCount[1].Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                "Остановить ее." if len(StayCount) < 2: #if one
                        $Line = 0
                        call Girl_Pos_Reset(StayCount[0]) #call expression StayCount[0].Tag + "_Pos_Reset"
                        "Вы делаете шаг назад, отстраняясь от нее."
                        $ StayCount[0].Statup("Love", 80, -1)
                        $ StayCount[0].Statup("Obed", 80, 5)
                        $ StayCount[0].Statup("Inbt", 80, -1)
                        $ StayCount[0].FaceChange("sad")
                        "Кажется, она немного расстроилась."
                "Остановить их." if len(StayCount) > 1: #if both
                        $Line = 0
                        call Girl_Pos_Reset(StayCount[1]) #call expression StayCount[1].Tag + "_Pos_Reset"
                        call Girl_Pos_Reset(StayCount[0]) #call expression StayCount[0].Tag + "_Pos_Reset"
                        "Вы делаете шаг назад, отстраняясь от них."
                        $ StayCount[0].Statup("Love", 80, -1)
                        $ StayCount[0].Statup("Obed", 80, 5)
                        $ StayCount[0].Statup("Inbt", 80, -1)
                        $ StayCount[1].Statup("Obed", 80, 5)
                        $ StayCount[1].Statup("Inbt", 80, -1)
                        $ StayCount[0].FaceChange("sad")
                        $ StayCount[1].FaceChange("sad")
                        "Кажется, они немного расстроились."
        if Line:
            #B set
            $ Options = [1]
            if len(StayCount) > 1:
                    if ApprovalCheck(StayCount[0], 1300) and StayCount[0].GirlLikeCheck(StayCount[1]) >= 800:
                        $ Options.append(2)     #"She reaches over to [StayCount[1]] and begins soaping up her pussy."
                    if ApprovalCheck(StayCount[0], 1200) and StayCount[0].GirlLikeCheck(StayCount[1]) >= 700:
                        $ Options.append(3)     #"She reaches over to [StayCount[1]] and begins soaping up her chest."

            if ApprovalCheck(StayCount[0], 1300):
                $ Options.append(4)     #"She reaches down and takes your cock in her hand, soaping it up."
            if ApprovalCheck(StayCount[0], 1400) and Player.Male:
                $ Options.append(5)     #"She kneels down and wraps her breasts around your cock, soaping it up."

            if ApprovalCheck(StayCount[0], 1300):
                $ Options.append(6)     #"She reaches down and begins fondling her own pussy, building a nice lather."
            if ApprovalCheck(StayCount[0], 1200):
                $ Options.append(7)     #"She begins rubbing her own breasts in circles, building a nice lather."

            if not ApprovalCheck(StayCount[0], 1400):
                #only adds these if there's not much in there.
                if ApprovalCheck(StayCount[0], 1000):
                    $ Options.append(8)         #"She draws her breasts up and down your arm, the soap bubbles squirting out."
                if ApprovalCheck(StayCount[0], 1100):
                    $ Options.append(9)         #"She kneels down and rubs her breasts against your leg, soaping it up."
                if ApprovalCheck(StayCount[0], 1000):
                    $ Options.append(10)        #"She presses against your back, her soapy breasts rubbing back and forth against it."
                if ApprovalCheck(StayCount[0], 1100):
                    $ Options.append(11)        #"She presses against your chest, her soapy breasts rubbing back and forth against it."

            $ renpy.random.shuffle(Options)

            #"Line" will be either the first girl's name, or "She"
            #lesbian
            if Options[0] == 2:
                    $ StayCount[0].Statup("Lust", 50, 5)
                    $ StayCount[0].Statup("Lust", 70, 2)
                    $ StayCount[1].Statup("Lust", 50, 7)
                    $ StayCount[1].Statup("Lust", 70, 3)
                    $ Player.Statup("Focus", 50, 8)
                    $ Player.Statup("Focus", 80, 4)
                    "[Line] тянется к [StayCount[1].Name_dat] и начинает намыливать ее грудь."
            elif Options[0] == 3:
                    $ StayCount[0].Statup("Lust", 50, 7)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ StayCount[1].Statup("Lust", 50, 8)
                    $ StayCount[1].Statup("Lust", 70, 4)
                    $ Player.Statup("Focus", 50, 8)
                    $ Player.Statup("Focus", 80, 5)
                    "[Line] тянется к [StayCount[1].Name_dat] и начинает намыливать ее киску."

            #fondling you
            elif Options[0] == 4:
                    if len(StayCount) > 1:
                            $ StayCount[0].Statup("Lust", 50, 10)
                            $ StayCount[0].Statup("Lust", 70, 7)
                    else:
                            $ StayCount[0].Statup("Lust", 50, 8)
                            $ StayCount[0].Statup("Lust", 70, 5)
                    $ Player.Statup("Focus", 50, 10)
                    $ Player.Statup("Focus", 80, 6)
                    if Player.Male:
                            "[Line] наклоняется и берет ваш член в руку, намыливая его."
                    else:
                            "[Line] наклоняется и начинает ласкать вашу киску, намыливая ек."
            elif Options[0] == 5:
                    if len(StayCount) > 1:
                            $ StayCount[0].Statup("Lust", 50, 12)
                            $ StayCount[0].Statup("Lust", 70, 8)
                    else:
                            $ StayCount[0].Statup("Lust", 50, 9)
                            $ StayCount[0].Statup("Lust", 70, 6)
                    $ Player.Statup("Focus", 50, 10)
                    $ Player.Statup("Focus", 80, 4)
                    "[Line] становится на колени и обнимает грудью ваш член, намыливая его."

            #mssturbation
            elif Options[0] == 6:
                    if len(StayCount) > 1:
                            $ StayCount[0].Statup("Lust", 50, 11)
                            $ StayCount[0].Statup("Lust", 70, 6)
                    else:
                            $ StayCount[0].Statup("Lust", 50, 9)
                            $ StayCount[0].Statup("Lust", 70, 5)
                    $ Player.Statup("Focus", 50, 9)
                    $ Player.Statup("Focus", 80, 4)
                    "[Line] наклоняется и начинает ласкать свою киску, создавая красивую пену."
            elif Options[0] == 7:
                    if len(StayCount) > 1:
                            $ StayCount[0].Statup("Lust", 50, 10)
                            $ StayCount[0].Statup("Lust", 70, 5)
                    else:
                            $ StayCount[0].Statup("Lust", 50, 9)
                            $ StayCount[0].Statup("Lust", 70, 4)
                    $ Player.Statup("Focus", 50, 8)
                    $ Player.Statup("Focus", 80, 3)
                    "[Line] начинает тереть свою грудь круговыми движениями, создавая красивую пену."

            #gentle tease
            elif Options[0] == 8:
                    $ StayCount[0].Statup("Lust", 50, 6)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ Player.Statup("Focus", 50, 7)
                    $ Player.Statup("Focus", 80, 3)
                    "[Line] трет своей грудью вашу руку вверх и вниз, намыливая ее."
            elif Options[0] == 9:
                    $ StayCount[0].Statup("Lust", 50, 8)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ Player.Statup("Focus", 50, 8)
                    $ Player.Statup("Focus", 80, 3)
                    "[Line] становится на колени и трет свою грудь о вашу ногу, намыливая ее."
            elif Options[0] == 10:
                    $ StayCount[0].Statup("Lust", 50, 7)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ Player.Statup("Focus", 50, 6)
                    $ Player.Statup("Focus", 80, 3)
                    "[Line] прижимается к вашей спине, ее мыльная грудь трется о нее взад и вперед."
            elif Options[0] == 11:
                    $ StayCount[0].Statup("Lust", 50, 7)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ Player.Statup("Focus", 50, 8)
                    $ Player.Statup("Focus", 80, 4)
                    "[Line] прижимается к вашей груди, ее мыльная грудь трется о нее взад и вперед."
            elif Options[0] == 1:
                    $ StayCount[0].Statup("Lust", 50, 5)
                    $ StayCount[0].Statup("Lust", 70, 2)
                    $ Player.Statup("Focus", 50, 6)
                    $ Player.Statup("Focus", 80, 3)
                    "[Line] молча смотрит на вас, двигая руками по мыльному телу. . ."
                    $ Line = 0

        if Line and len(StayCount) > 1:
            #C Set, check what the other girl thinks. . .
            $ D20 += 5 if ApprovalCheck(StayCount[1], 1800) else 0
            if StayCount[1].GirlLikeCheck(StayCount[0]) <= 800 and 2 <= Options[0] <=3:
                $ D20 -= 5
            if StayCount[1].GirlLikeCheck(StayCount[0]) <= 600:
                $ D20 -= 5

            if 2 <= Options[0] <= 3:
                # if it's lesbian stuff. . .
                if ApprovalCheck(StayCount[1], 1300) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 800:
                        $ StayCount[1].FaceChange("sexy",1)
                        $ StayCount[0].Statup("Lust", 50, 5)
                        $ StayCount[0].Statup("Lust", 70, 5)
                        $ StayCount[1].Statup("Lust", 50, 12)
                        $ StayCount[1].Statup("Lust", 70, 12)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].Name], похоже, в восторге от этого, она отвечает взаимностью."
                        $ Player.Statup("Focus", 50, 7)
                        $ Player.Statup("Focus", 80, 3)
                        $ Line = 4
                elif ApprovalCheck(StayCount[1], 1200) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 700:
                        $ StayCount[1].FaceChange("sexy",2,Eyes="closed")
                        $ StayCount[1].Statup("Lust", 50, 10)
                        $ StayCount[1].Statup("Lust", 70, 10)
                        $ Player.Statup("Focus", 50, 5)
                        $ Player.Statup("Focus", 80, 3)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].Name_dat], похоже, начинает понравиться."
                else:
                        $ StayCount[1].Statup("Lust", 50, 10)
                        $ StayCount[1].FaceChange("sadside",Brows="confused")
                        "[StayCount[1].Name_dat], похоже, это не нравится."
                        "Она отстраняется."
                        $ Line = 3
            else:
                # if it's not lesbian stuff. . .
                if (ApprovalCheck(StayCount[1], 1300) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 700) or ApprovalCheck(StayCount[1], 2000):
                    if Options[0] == 5: #titjob
                        $ StayCount[1].Statup("Lust", 50, 10)
                        $ StayCount[1].Statup("Lust", 70, 5)
                        $ Player.Statup("Focus", 50, 6)
                        $ Player.Statup("Focus", 80, 3)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].Name], похоже, в восторге от этого, она начинает медленно тереться о вас, пока другая девушка смотрит."
                    else:
                        $ StayCount[1].Statup("Lust", 50, 10)
                        $ StayCount[1].Statup("Lust", 70, 5)
                        $ Player.Statup("Focus", 50, 5)
                        $ Player.Statup("Focus", 80, 3)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].Name], похоже, в восторге от этого, она присоединяется к другой девушке с противоположной стороны."
                    $ Line = 4
                elif ((ApprovalCheck(StayCount[1], 1200) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 600)) or ApprovalCheck(StayCount[1], 1600):
                        $ StayCount[1].FaceChange("sexy",2,Eyes="down")
                        $ StayCount[1].Statup("Lust", 50, 10)
                        $ StayCount[1].Statup("Lust", 70, 5)
                        "[StayCount[1].Name], похоже, в восторге от этого, она наблюдает за действиями другой девушки."
                else:
                        $ StayCount[1].FaceChange("sadside",Brows="confused")
                        $ StayCount[1].Statup("Lust", 50, 5)
                        "[StayCount[1].Name_dat], похоже, это не нравится."
                        $ Line = 3
        if Line == 3:
                call Girl_Pos_Reset(StayCount[1]) #call expression StayCount[1].Tag + "_Pos_Reset"
        if Line:
            menu:
                extend ""
                "Продолжать?":
                    pass
                "Остановить ее." if len(StayCount) < 2: #if one
                    $ Line = 3 if Line == 3 else 0
                    call Girl_Pos_Reset(StayCount[0]) #call expression StayCount[0].Tag + "_Pos_Reset"
                    "Вы делаете шаг назад, отстраняясь от нее."
                    $ StayCount[0].Statup("Love", 80, -2)
                    $ StayCount[0].Statup("Obed", 80, 5)
                    $ StayCount[0].Statup("Inbt", 80, -2)
                    $ StayCount[0].FaceChange("sad")
                    "Кажется, она немного расстроилась."
                "Остановить их." if len(StayCount) > 1: #if both
                    call Girl_Pos_Reset(StayCount[1]) #call expression StayCount[1].Tag + "_Pos_Reset"
                    call Girl_Pos_Reset(StayCount[0]) #call expression StayCount[0].Tag + "_Pos_Reset"
                    "Вы делаете шаг назад, отстраняясь от них."
                    $ StayCount[0].FaceChange("sad")
                    $ StayCount[0].Statup("Love", 80, -2)
                    $ StayCount[0].Statup("Obed", 80, 5)
                    $ StayCount[0].Statup("Inbt", 80, -2)
                    if Line == 3:
                        $ StayCount[1].Statup("Love", 80, 4)
                        $ StayCount[1].Statup("Obed", 80, 5)
                        $ StayCount[1].FaceChange("bemused")
                        "[StayCount[0].Name] выглядит немного расстроенной, а [StayCount[1].Name], наоборот, довольной."
                    else:
                        $ StayCount[1].Statup("Love", 80, -1)
                        $ StayCount[1].Statup("Obed", 80, 5)
                        $ StayCount[1].Statup("Inbt", 80, -1)
                        $ StayCount[1].FaceChange("sad")
                        "Кажется, они немного расстроились."
                        $ Line = 0

        if Line:
            #D set, wrap-up
            if len(StayCount) > 1 and Line != 3: #if second didn't disapprove
                    $ StayCount[0].GLG(StayCount[1],600,4,1)
                    $ StayCount[1].GLG(StayCount[0],600,4,1)
                    $ StayCount[0].GLG(StayCount[1],800,3,1)
                    $ StayCount[1].GLG(StayCount[0],800,3,1)
                    $ StayCount[0].GLG(StayCount[1],900,1,1)
                    $ StayCount[1].GLG(StayCount[0],900,1,1)
            if 2 <= Options[0] <= 3 and D20 >= 15:
                    #if it's lesbian. . .
                    $ StayCount[1].GLG(StayCount[0],900,4,1)
                    $ Player.Statup("Focus", 50, 10)
                    $ Player.Statup("Focus", 80, 5)
                    "Через несколько минут после этого [StayCount[1].Name] отстраняется."
                    call Girl_Cumming(StayCount[1],1)
                    if Line == 4:
                            $ StayCount[0].GLG(StayCount[1],900,3,1)
                            "Похоже, что [StayCount[0].Name] положительно реагирует на это. . ."
                            call Girl_Cumming(StayCount[0],1)
                    if len(StayCount) > 1:
                            "Девочки делают шаг назад."
                            call Girl_Pos_Reset(StayCount[1]) #call expression StayCount[1].Tag + "_Pos_Reset"
                    else:
                            "[StayCount[0].Name] делает шаг назад."
                    call Girl_Pos_Reset(StayCount[0]) #call expression StayCount[0].Tag + "_Pos_Reset"

            elif 4 <= Options[0] <= 5 and D20 >= 10:
                    #if it's her fondling you
                    $ Player.Focus = 15
                    if Options[0] == 5: #if it was titjob
                            $ StayCount[0].Spunk.append("tits")

                    if Line == 4:
                            $ StayCount[0].Statup("Inbt", 90, 7)
                            $ StayCount[1].Statup("Inbt", 90, 4)
                            $ StayCount[0].GLG(StayCount[1],900,3,1)
                            $ StayCount[1].GLG(StayCount[0],900,3,1)
                            "Через несколько минут им двоим удается довести вас до оргазма."
                    else:
                            $ StayCount[0].Statup("Inbt", 90, 5)
                            "Через несколько минут ей удается довести вас до оргазма."
                    "Нужно еще немного времени, чтобы привести вас в порядок."
                    if Options[0] == 5: #if it was titjob
                            $ StayCount[0].Spunk = []
                    if len(StayCount) > 1:
                            "Девочки делают шаг назад."
                            call Girl_Pos_Reset(StayCount[1]) #call expression StayCount[1].Tag + "_Pos_Reset"
                    else:
                            "[StayCount[0].Name] делает шаг назад."
                    call Girl_Pos_Reset(StayCount[0]) #call expression StayCount[0].Tag + "_Pos_Reset"

            elif 6 <= Options[0] <= 7 and D20 >= 15:
                    #if it's her masturbation. . .
                    $ StayCount[0].Statup("Inbt", 90, 7)
                    $ Player.Statup("Focus", 50, 15)
                    $ Player.Statup("Focus", 80, 5)
                    "Через несколько минут после этого [StayCount[0].Name] отстраняется."
                    call Girl_Cumming(StayCount[0],1)
                    if Line == 4:
                            $ StayCount[1].Statup("Inbt", 90, 6)
                            $ StayCount[0].GLG(StayCount[1],900,3,1)
                            "Похоже, что [StayCount[1].Name] положительно реагирует на это. . ."
                            call Girl_Cumming(StayCount[1],1)
                    if len(StayCount) > 1:
                            $ StayCount[1].GLG(StayCount[0],900,3,1)
                            "Девочки делают шаг назад."
                            call Girl_Pos_Reset(StayCount[1]) #call expression StayCount[1].Tag + "_Pos_Reset"
                    else:
                            "[StayCount[0].Name] делает шаг назад."
                    call Girl_Pos_Reset(StayCount[0]) #call expression StayCount[0].Tag + "_Pos_Reset"
            else:
                #nobody got off
                if len(StayCount) > 1:
                        call Girl_Pos_Reset(StayCount[1])  #call expression StayCount[1].Tag + "_Pos_Reset"
                call Girl_Pos_Reset(StayCount[0]) #call expression StayCount[0].Tag + "_Pos_Reset"
                $ Player.Statup("Focus", 50, 15)
                $ Player.Statup("Focus", 80, 5)
                if D20 >= 15:
                    "Через минуту или две, вам кажется, что кто-то вот-вот войдет, так что вы расходитесь."
                    "Вы очень расстроены. . ."
                elif D20 >= 10:
                    "Через минуту или две она, удовлетворенная своими усилиями, она отстраняется."
                else:
                    "Примерно через минуту она отстраняется и заканчивает мыться."
                if 4 <= Options[0] <= 5:
                    if Player.Male:
                        "Вы остаетесь с диким стояком."
                    else:
                        "Ваша киска жаждет больше."
        call Shift_Focus(StayCount[0])
        return
# End Shower Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# end Shower Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Study Room Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Study_Room_Entry:  #rkeljsvgb
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
    call Drain_Nearby #empties .Loc "nearby"
    $ bg_current = "bg study"
    call Gym_Clothes_Off #call Gym_Clothes
    call Taboo_Level
    call Set_The_Scene(Entry = 1)
    $ Round -= 5 if Round >= 5 else Round
    if Round <= 10:
                call Round10
    menu:
            "Вы стоите у двери, ваши действия?"
            "Вежливо постучать":
                    $ Line = "knock"

            "Войти без стука":
                 if Time_Count >= 3: #night time
                         "Дверь заперта. Вы не можете просто взять и войти."
                         jump Study_Room_Entry

            "Воспользоваться ключом, чтобы войти" if Time_Count >= 3 and "Xavier" in Keys: #night
                    "Вы используете свой ключ."
                    $ Line = 0

            "Попросить [KittyX.Name_vin]" if Time_Count >= 3 and KittyX in Party: #night
                    $ Line = "kitty"
            "Попросить [StormX.Name_vin]" if Time_Count >= 3 and StormX in Party: #night
                    $ Line = "storm"

            "Уйти":
                    "Вы возвращаетесь назад."
                    jump Campus_Map

    if Line == "knock":
        if Time_Count >= 3: #night time
            "Ответа нет, наверное, он спит."
            jump Study_Room_Entry
        else:
            ch_x "Да, входите. . ."
            "Вы входите в комнату."
    elif Line == "kitty":
            ch_k "Да?"
            while True:
                menu:
                    extend ""
                    "Не могла бы ты пройти через дверь и открыть ее для меня?":
                            if "Sneakthief" in KittyX.Traits:
                                ch_k "Без проблем. . ."
                                jump Study_Room
                            elif "no thief" in KittyX.RecentActions:
                                ch_k "Я уже сказала тебе \"нет\"."
                            elif ApprovalCheck(KittyX, 400, "I") or ApprovalCheck(KittyX, 1400):
                                $ KittyX.Statup("Love", 90, 3)
                                $ KittyX.Statup("Obed", 50, 10)
                                $ KittyX.Statup("Inbt", 60, 10)
                                if not Player.Male:
                                    ch_k "Хихи, а ты плохая девочка. . ."
                                else:
                                    ch_k "Хихи, а ты плохиш. . ."
                                $ KittyX.Traits.append("Sneakthief")
                                jump Study_Room
                            else:
                                $ KittyX.Statup("Love", 90, -3)
                                $ KittyX.Statup("Obed", 50, 2)
                                $ KittyX.Statup("Inbt", 60, 2)
                                ch_k "Эм, мне, если честно, некомфортно это делать. . ."
                                $ KittyX.RecentActions.append("no thief")
                    "Открой дверь.":
                            if "Sneakthief" in KittyX.Traits:
                                ch_k "Без проблем. . ."
                                jump Study_Room
                            elif "no thief" in KittyX.RecentActions:
                                ch_k "Я уже сказала тебе \"нет\"."
                            elif ApprovalCheck(KittyX, 500, "O") or ApprovalCheck(KittyX, 1600):
                                $ KittyX.Statup("Obed", 50, 15)
                                $ KittyX.Statup("Inbt", 60, 10)
                                ch_k "Хихи, если ты так этого хочешь. . ."
                                $ KittyX.Traits.append("Sneakthief")
                                jump Study_Room
                            else:
                                $ KittyX.Statup("Love", 90, -5)
                                $ KittyX.Statup("Obed", 50, 2)
                                $ KittyX.Statup("Inbt", 60, 2)
                                ch_k "Эм, нет."
                                $ KittyX.RecentActions.append("no thief")
                    "Неважно. [[Уйти]":
                            "Вы возвращаетесь назад."
                            jump Campus_Map
            jump Study_Room_Entry
    elif Line == "storm":
            ch_s "Что такое?"
            while True:
                menu:
                    extend ""
                    "Как думаешь, сможешь ли ты взломать этот замок?" if "Sneakthief" not in StormX.Traits:
                            if "no thief" in StormX.RecentActions:
                                ch_s "Я же сказала, что не буду этого делать."
                            elif ApprovalCheck(StormX, 400, "I") or ApprovalCheck(StormX, 1400):
                                $ StormX.Statup("Love", 90, 3)
                                $ StormX.Statup("Obed", 80, 10)
                                $ StormX.Statup("Inbt", 60, 10)
                                $ StormX.FaceChange("sly")
                                ch_s "О, это должно быть интересно. . ."
                                "Она вытаскивает несколько отмычек из-за уха.."
                                ch_s "Так, ладно, сюда. . . теперь сюда..."
                                ch_s "Хорошо, вот так. . . еще немного. . . и. . . и мы внутри."
                                $ StormX.Traits.append("Sneakthief")
                                $ StormX.FaceChange("normal")
                                jump Study_Room
                            else:
                                $ StormX.Statup("Love", 90, -3)
                                $ StormX.Statup("Obed", 50, 2)
                                $ StormX.Statup("Inbt", 60, 2)
                                ch_s "Не думаю, что нам стоит это делать. . ."
                                $ StormX.RecentActions.append("no thief")
                    "Не могла бы ты снова взломать замок?" if "Sneakthief" in StormX.Traits:
                                ch_s "Без проблем. . ."
                                jump Study_Room
                    "Неважно. [[Уйти]":
                            "Вы возвращаетесь назад."
                            jump Campus_Map
            jump Study_Room_Entry

    elif Time_Count < 3: #not night time
            ch_x "Знаешь, [Player.Name], невежливо входить в комнату без предупреждения."
    $ Cnt = 0

label Study_Room: #rkeljsvgb
    $ bg_current = "bg study"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
            if Time_Count >= 3: #night time
                "Уже поздно, вы возвращаетесь в свою комнату."
                jump Player_Room
            else:
                call Wait
                call Girls_Location

    call GirlsAngry
    call XavierFace("happy")

# Study Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if Time_Count >= 3: # night time
        $ Line = "Вы находитесь в кабинете Ксавье, но сейчас его там нет. Что вы хотели бы сделать?"
    else:
        show Professor at SpriteLoc(StageLeft) zorder 25
        if "switchxavier" in Player.History:
                call Xavier_Switch
        $ Line = "Вы находитесь в кабинете Ксавье. Что вы хотели бы сделать?"
    menu:
        "[Line]"
        "Общаться" if Time_Count >= 3: #night time #fix, open up once sex while in office is fine
                    call Chat

        "План Омега!" if Time_Count < 3 and RogueX.Loc == bg_current and Player.Lvl >= 5:
                        call Xavier_Plan(RogueX) #Plan_Omega
        "План Каппа!" if Time_Count < 3 and KittyX.Loc == bg_current and Player.Lvl >= 5:
                        call Xavier_Plan(KittyX) #Plan_Kappa
        "План Псай!" if Time_Count < 3 and EmmaX.Loc == bg_current and Player.Lvl >= 5:
                        call Xavier_Plan(EmmaX) #Plan_Psi
        "План Хи!" if Time_Count < 3 and LauraX.Loc == bg_current and Player.Lvl >= 5:
                        call Xavier_Plan(LauraX) #Plan_Chi
        "План Альфа!" if Time_Count < 3 and JeanX.Loc == bg_current and Player.Lvl >= 5:
                        call Xavier_Plan(JeanX) #Plan_Chi
        "План Ро!" if Time_Count < 3 and StormX.Loc == bg_current and Player.Lvl >= 5:
                        call Xavier_Plan(StormX) #Plan_Rho
        "План Зета!" if Time_Count < 3 and JubesX.Loc == bg_current and Player.Lvl >= 5:
                        call Xavier_Plan(JubesX) #Plan_Zeta
        "План Гамма!" if Time_Count < 3 and GwenX.Loc == bg_current and Player.Lvl >= 5:
                        call Xavier_Plan(GwenX) #Plan_Gamma
        "План Бета!" if Time_Count < 3 and BetsyX.Loc == bg_current and Player.Lvl >= 5:
                        call Xavier_Plan(BetsyX) #Plan_Beta
        "План Дельта!" if Time_Count < 3 and DoreenX.Loc == bg_current and Player.Lvl >= 5:
                        call Xavier_Plan(DoreenX) #Plan_Delta
        "План Эпсилон!" if Time_Count < 3 and WandaX.Loc == bg_current and Player.Lvl >= 5:
                        call Xavier_Plan(WandaX) #Plan_Upsilon

        "Поговорить с ним о [DoreenX.Name_pre]" if "SGattic" in Player.History:
                    call DoreenXavierReport
        "Я слышал шум. . ." if "noise" in Player.History and Time_Count < 3:
                    #You hadn't asked Emma yet
                    if "creaking" in Player.DailyActions:
                        ch_x "Как я уже сказал, поговори с Эммой."
                    else:
                        ch_x "Шум над твоей комнатой? . . . ахах. . ."
                        ch_x ". . . Тебе, наверное, стоит спросить об этом Эмму. . ."
                        $ Player.AddWord(1,0,"creaking",0,0) #adds "word" to Daily
        "Исследовать" if Time_Count >= 3 and "explore" not in Player.RecentActions:
                    $ Cnt = 0
                    $ Player.RecentActions.append("explore")
                    jump Study_Room_Explore

        "Ждать":
                    if Time_Count >= 3: #night time
                            "Вы, вероятно, не захотите здесь находиться, когда Ксавье войдет."
                    elif Time_Count >=2: #evening time
                            ch_x "Если не возражаешь, я хотел бы закрыться на вечер."
                            "Вы возвращаетесь в свою комнату."
                            hide Professor
                            jump Player_Room
                    else:
                            call Wait
                            call Girls_Location
                            ch_x "Не то, чтобы я был против компании, но все-таки, чем я могу тебе помочь?"

        "Выйти" if not TravelMode:
                    hide Professor
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    hide Professor
                    jump Campus_Entry
        "Вернуться в свою комнату" if TravelMode:
                    hide Professor
                    jump Player_Room_Entry
    if Line == "plan":
        #if coming back from a failed Xavier Plan. . .
        ch_x "У меня нет времени на эти игры. Чего ты хочешь?"
        $ Line = "Вы находитесь в кабинете Ксавье. Что вы хотели бы сделать?"
    jump Study_Room


label Study_Room_Explore: #rkeljsvg
    $ Line = 0
    $ D20 = renpy.random.randint(1, 20)
    menu:
        "Где вы хотели бы поискать?"
        "Книжная полка":
            if D20 >= 5 + Cnt:
                    $ Line = "book"
            else:
                    "Когда вы обыскиваете книжную полку, вы случайно сбиваете одну из книг."
                    "Она с грохотом падает на пол, а на столе начинает мигать огонек."
        "Левый Ящик Стола":
            if KittyX.Loc != bg_current and StormX.Loc != bg_current:
                    "Кажется, вы не можете открыть его, было бы неплохо, если бы кто-то открыл защелку изнутри."
            elif D20 >= 10 + Cnt:
                    $ Line = "left"
            else:
                    "Вы открываете ящик с громким скрипом."
                    "Вы оглядываетесь и замечаете, что на столе начал мигать маленький огонек."
        "Средний Ящик Стола":
            if KittyX.Loc != bg_current and StormX.Loc != bg_current:
                    "Кажется, вы не можете открыть его, было бы неплохо, если бы кто-то открыл защелку изнутри."
            elif D20 >= 15 + Cnt:
                    $ Line = "mid"
            else:
                    "Вы открываете ящик с громким скрипом."
                    "Вы оглядываетесь и замечаете, что на столе начал мигать маленький огонек."
        "Правый Ящик Стола":
            if KittyX.Loc != bg_current and StormX.Loc != bg_current:
                    "Кажется, вы не можете открыть его, было бы неплохо, если бы кто-то открыл защелку изнутри."
            elif D20 >= 5 + Cnt:
                    $ Line = "right"
            else:
                    "Вы открываете ящик с громким скрипом."
                    "Вы оглядываетесь и замечаете, что на столе начал мигать маленький огонек."
        "Неважно [[назад]":
                    jump Study_Room

    $ D20 = renpy.random.randint(1, 20)
    if not Line:
                "Наверное, лучше уйти отсюда."
                "Вы ускользаете и возвращаетесь в свою комнату."
                jump Player_Room_Entry
    elif Line == "book":
            if D20 >= 15 and "Well Studied" not in Achievements:
                "Когда вы проверяете книги на полке, вы замечаете, что одна из них на самом деле представляет собой замаскированный мини сейф."
                if KittyX.Loc == bg_current:
                    menu:
                        "Раз [KittyX.Name] рядом, попросить ее заглянуть внутрь?"
                        "Заглянуть внутрь":
                            if ApprovalCheck(KittyX, 700, "I") or ApprovalCheck(KittyX, 1800):
                                if "Well Studied" not in Achievements:
                                        $ KittyX.Statup("Obed", 50, 10)
                                        $ KittyX.Statup("Inbt", 60, 15)
                                        ch_k "Звучит как план."
                                        "[KittyX.Name] проводит рукой по коробке и вытаскивает пачку банкнот."
                                        "Похоже Ксавье прятал здесь наличку на черный день."
                                        $ Player.Cash += 500
                                        "[[Получено $500.]"
                                        $ Achievements.append("Well Studied")
                                else:
                                        "Похоже, уже разграблено."
                            else:#Kitty doesn't approve
                                $ KittyX.Statup("Love", 90, -3)
                                $ KittyX.Statup("Obed", 50, 1)
                                $ KittyX.Statup("Inbt", 60, 2)
                                ch_k "Я, честно говоря, не думаю, что мы должны это делать."
                        "Вернуть на место":
                            "Вы кладете коробку обратно на полку."
                elif StormX.Loc == bg_current:
                    menu:
                        "Раз [StormX.Name] рядом, попросить ее заглянуть внутрь?"
                        "Заглянуть внутрь":
                            if ApprovalCheck(StormX, 700, "I") or ApprovalCheck(StormX, 1800):
                                if "Well Studied" not in Achievements:
                                        $ StormX.Statup("Obed", 50, 10)
                                        $ StormX.Statup("Inbt", 60, 15)
                                        ch_s "Полагаю, это я могу. . ."
                                        "[StormX.Name] взламывает замок на коробке и вытаскивает пачку банкнот."
                                        "Похоже Ксавье прятал здесь наличку на черный день. . ."
                                        $ Player.Cash += 500
                                        "[[Получено $500.]"
                                        $ Achievements.append("Well Studied")
                                else:
                                        "Похоже, уже разграблено."
                            else:#Storm doesn't approve
                                $ StormX.Statup("Love", 90, -3)
                                $ StormX.Statup("Obed", 50, 1)
                                $ StormX.Statup("Inbt", 60, 2)
                                ch_s "Я, честно говоря, не думаю, что мы должны это делать."
                        "Вернуть на место.":
                            "Вы кладете коробку обратно на полку."
                else:#[KittyX.Name]'s not there
                            "Вы не можете придумать, как открыть его, жаль, что вы не призрак или кто-то в этом роде."
                            "Вы кладете коробку обратно на полку."
            elif D20 >= 15:
                "Похоже, здесь больше нет ничего интересного."
            else:
                "Вы просматриваете книги несколько минут, но ничего не находите."
                "Вероятно, потребуются более тщательный поиск."
    elif Line == "left":
            if "Xavier's photo" not in Player.Inventory:
                if D20 >= 10:
                        "Под грудой документов вы находите распечатанную фотографию."
                        "Похоже, это селфи Мистик, целующейся с Ксавье."
                        "Она тянется вниз, чтобы поправить его. . . о, а {i}это{/i} интересно."
                        if StormX.Loc == bg_current:
                                ch_s "Тебе, наверное, стоит положить ее обратно, не стоит лезть в личную жизнь Чарьза."
                        else:
                                "[[Получено фото Ксавье.]"
                                $ Player.Inventory.append("Xavier's photo")
                                if "kappa" in Player.History:
                                        $ Player.History.remove("kappa")
                else:
                        "Вы просматриваете какие-то документы, но ничего не находите."
                        "Вероятно, потребуются более тщательный поиск."
            else:
                        "Похоже, здесь больше нет ничего интересного."
    elif Line == "mid":
            $ Options = TotalGirls[:]
            python:
                for BX in Options:
                    if BX not in Keys:
                            Keys.append(BX)
            $ Options = []
            if "All" not in Keys:
                "Под какими-то безделушками вы находите небольшой брелок."
                "[[Добавлен Брелок для ключей.]"
                if "Xavier" not in Keys:
                        $ Keys.append("Xavier")
                if "All" not in Keys:
                        $ Keys.append("All")
            else:
                "Похоже, здесь нет ничего интересного."

    elif Line == "right":
            if "Xavier's files" not in Player.Inventory:
                if D20 >= 10:
                        "Вы просматриваете какие-то документы, но ничего не находите."
                        if StormX.Loc == bg_current:
                                ch_s "Хмм. . ."
                                "Она залезает под какие-то документы и находит небольшую выемку."
                                "С мягким \"щелк\" открывается тайник в столе, открывая вам доступ к нескольким папкам с файлами."
                                "Внутри несколько довольно. . . подробных отчетов о девочках в институте."
                                $ StormX.FaceChange("surprised",2)
                                "К ним относятся параметры тела, сексуальные истории. . . склонности к мастурбации?"
                                $ StormX.Statup("Obed", 70, 5)
                                $ StormX.Statup("Inbt", 70, 5)
                                $ StormX.FaceChange("angry")
                                ch_s "Я не думаю, что у Чарльза должна находиться такая информация. . ."
                                $ StormX.FaceChange("normal",1)
                                "[[Добавлены файлы Ксавье.]"
                                $ Player.Inventory.append("Xavier's files")
                                if "rho" in Player.History:
                                        $ Player.History.remove("rho")
                else:
                        "Вы просматриваете какие-то документы, но ничего не находите."
                        "Вероятно, потребуются более тщательные поиски."
            else:
                        "Похоже, здесь больше нет ничего интересного."

    $ Cnt += 3
    jump Study_Room_Explore
# end Study's Room Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



label Rogue_Room_Entry:
        $ bg_current = RogueX.Home
        call Girls_Room_Entry(RogueX)
        $ bg_current = "bg campus"
        jump Misplaced
label Kitty_Room_Entry:
        $ bg_current = KittyX.Home
        call Girls_Room_Entry(KittyX)
        $ bg_current = "bg campus"
        jump Misplaced
label Emma_Room_Entry:
        $ bg_current = EmmaX.Home
        call Girls_Room_Entry(EmmaX)
        $ bg_current = "bg campus"
        jump Misplaced
label Laura_Room_Entry:
        $ bg_current = LauraX.Home
        call Girls_Room_Entry(LauraX)
        $ bg_current = "bg campus"
        jump Misplaced
label Jean_Room_Entry:
        $ bg_current = JeanX.Home
        call Girls_Room_Entry(JeanX)
        $ bg_current = "bg campus"
        jump Misplaced
label Storm_Room_Entry:
        $ bg_current = StormX.Home
        call Girls_Room_Entry(StormX)
        $ bg_current = "bg campus"
        jump Misplaced
label Jubes_Room_Entry:
        $ bg_current = JubesX.Home
        call Girls_Room_Entry(JubesX)
        $ bg_current = "bg campus"
        jump Misplaced
label Gwen_Room_Entry:
        $ bg_current = GwenX.Home
        call Girls_Room_Entry(GwenX)
        $ bg_current = "bg campus"
        jump Misplaced
label Betsy_Room_Entry:
        $ bg_current = BetsyX.Home
        call Girls_Room_Entry(BetsyX)
        $ bg_current = "bg campus"
        jump Misplaced
label Doreen_Room_Entry:
        $ bg_current = DoreenX.Home
        if "doreenafter" in Player.History:
                "Кажется, там очень шумно, но вы не можете войти."
        else:
                if "SGattic" in Player.History:
                        $ DoreenX.Loc = "bg doreen"
                call Girls_Room_Entry(DoreenX)
        $ bg_current = "bg campus"
        jump Misplaced
label Wanda_Room_Entry:
        $ bg_current = WandaX.Home
        call Girls_Room_Entry(WandaX)
        $ bg_current = "bg campus"
        jump Misplaced

label Girls_Room_Entry(Chr=0): #rkeljsvgb
        #Set Chr somehow. . .
        if Chr not in TotalGirls:
                return
        $ Player.DrainWord("locked",0,0,1)
        call Shift_Focus(Chr)
        call Drain_Nearby #empties .Loc "nearby"
        $ bg_current = Chr.Home
        call Gym_Clothes_Off #call Gym_Clothes
        call Set_The_Scene(Entry = 1)
        call Taboo_Level
        $ Player.RecentActions.append("traveling")
        $ D20 = renpy.random.randint(1, 20)

        $ Round -= 5 if Round >= 5 else Round
        if Round <= 10:
                    if Time_Count < 3:
                            call Wait
                    else:
                            "Уже слишком поздно, пора ложиться спать."
                            $ bg_current = "bg player"
                            jump Misplaced

        if Chr is DoreenX and "SGattic" in Player.History:
                #if she's in hiding,
                $ DoreenX.Loc == "bg doreen"

        if Chr in Party:
                        if Time_Count >= 3 or (Time_Count == 2 and Round <= 10):
                            if ApprovalCheck(Chr, 1000, "LI",Alt=[[JubesX],500]) or ApprovalCheck(Chr, 600, "OI",Alt=[[JubesX],300]):
                                    #It's late but she really likes you
                                    if Chr is RogueX:
                                            ch_r "Уже довольно поздно, [Chr.Petname], но ты можешь зайти ненадолго."
                                    elif Chr is KittyX:
                                            ch_k "Уже довольно поздно, [Chr.Petname], но ты можешь заглянуть на минутку."
                                    elif Chr is EmmaX:
                                            ch_e "Уже довольно поздно, [Chr.Petname], но я могу уделить тебе немного времени."
                                    elif Chr is LauraX:
                                            ch_l "Уже довольно поздно, но заходи."
                                    elif Chr is JeanX:
                                            ch_j "Уже поздно, но какая разница."
                                    elif Chr is StormX:
                                            if not Player.Male:
                                                ch_s "Ты пришла довольно поздно, [Chr.Petname], но входи."
                                            else:
                                                ch_s "Ты пришел довольно поздно, [Chr.Petname], но входи."
                                    elif Chr is JubesX:
                                            ch_v "Конечно, заходи."
                                    elif Chr is GwenX:
                                            ch_g "Уже довольно поздно, но ты можешь зайти ненадолго."
                                    elif Chr is BetsyX:
                                            ch_b "Уже довольно поздно, но ты можешь остаться."
                                    elif Chr is DoreenX:
                                            ch_d "Уже довольно поздно, я могу тебе как-нибудь помочь?"
                                    elif Chr is WandaX:
                                            ch_w "Уже поздно, но у меня есть немного времени."
                            elif Chr.Addict >= 50:
                                    if Chr is RogueX:
                                            ch_r "Эм, да, тебе лучше войти. . ."
                                    elif Chr is KittyX:
                                            ch_k "Я бы очень хотела с тобой повидаться. . ."
                                    elif Chr is EmmaX:
                                            ch_e "Да. . . Полагаю, тебе стоит войти. . ."
                                    elif Chr is LauraX:
                                            ch_l "Эм, да, тебе лучше войти. . ."
                                    elif Chr is JeanX:
                                            ch_j "Ох, эм, конечно, заходи."
                                    elif Chr is StormX:
                                            ch_s "Ох, да, входи."
                                    elif Chr is JubesX:
                                            ch_v "Ох, да, заходи. . ."
                                    elif Chr is GwenX:
                                            ch_g "О, да, заходи."
                                    elif Chr is BetsyX:
                                            ch_b "Уже довольно поздно, но. . . заходи."
                                    elif Chr is DoreenX:
                                            ch_d "Ох, эм, заходи."
                                    elif Chr is WandaX:
                                            ch_w "Конечно, заходи."
                            elif ApprovalCheck(Chr, 500, "LI") or ApprovalCheck(Chr, 300, "OI"):
                                    #she likes you well enough but it's late
                                    if Chr is RogueX:
                                            ch_r "Уже довольно поздно, [Chr.Petname]. Увидимся завтра."
                                    elif Chr is KittyX:
                                            ch_k "Уже довольно поздно, [Chr.Petname]. До завтра?"
                                    elif Chr is EmmaX:
                                            ch_e "Уже поздно, [Chr.Petname]. Увидимся завтра."
                                    elif Chr is LauraX:
                                            ch_l "Увидимся завтра."
                                    elif Chr is JeanX:
                                            ch_j "Уже поздно, увидимся."
                                    elif Chr is StormX:
                                            if not Player.Male:
                                                ch_s "Ты пришла довольно поздно, [Chr.Petname], тебе лучше заглянуть завтра."
                                            else:
                                                ch_s "Ты пришел довольно поздно, [Chr.Petname], тебе лучше заглянуть завтра."
                                    elif Chr is JubesX:
                                            ch_v "Нет, спасибо. . ."
                                    elif Chr is GwenX:
                                            ch_g "Уже довольно поздно, увидимся завтра."
                                    elif Chr is BetsyX:
                                            ch_b "Уже довольно поздно, твои дела ко мне подождут до завтра."
                                    elif Chr is DoreenX:
                                            ch_d "Уже довольно поздно, может, поговорим завтра?"
                                    elif Chr is WandaX:
                                            ch_w "Уже поздно, зайди завтра."
                                    $ Chr.RecentActions.append("noentry")
                                    $ Chr.DailyActions.append("noentry")
                                    if Chr in Party:
                                            $ Party.remove(Chr)
                                    "Она заходит и закрывает за собой дверь."
                                    return
                        else:
                                    #If Girl is in the party and it's not late in the day
                                    if Chr is RogueX:
                                            ch_r "Заходи, [Chr.Petname]."
                                    elif Chr is KittyX:
                                            ch_k "Заходи!"
                                    elif Chr is EmmaX:
                                            ch_e "Не стой в дверях."
                                    elif Chr is LauraX:
                                            ch_l "Заходи."
                                    elif Chr is JeanX:
                                            ch_j "Чувствуй себя, как дома."
                                    elif Chr is StormX:
                                            ch_s "Добро пожаловать."
                                    elif Chr is JubesX:
                                            ch_v "Присаживайся. . ."
                                    elif Chr is GwenX:
                                            ch_g "О, заходи."
                                    elif Chr is BetsyX:
                                            ch_b "Устраивайся поудобнее."
                                    elif Chr is DoreenX:
                                            ch_d "Ох, привет, добро пожаловать!"
                                    elif Chr is WandaX:
                                            ch_w "Заходи."
                        call EventCalls
                        if Chr is DoreenX and "SGattic" in Player.History and "visit" not in DoreenX.RecentActions:
                                #if she's in hiding,
                                call Doreen_Visit
                        jump expression Chr.Tag + "_Room"
        #End if Girl in Party


        if Round >= 10 and Chr.Loc == bg_current and "les" in Chr.RecentActions:
                call Girls_Caught_Lesing(Chr)
                if not _return:
                        jump expression Chr.Tag + "_Room"

        if bg_current == KittyX.Home and "dress2" in LauraX.History and not Party:
                        #if you helped buy clothes for Laura earlier. . .
                        call Laura_Dressup3
                        $ bg_current = "bg campus"
                        jump Misplaced

        if Round >= 10 and Chr.Loc == bg_current and "gonnafap" in Chr.DailyActions and D20 >= 5:
                        #girl caught fapping
                        call Girl_Caught_Mastubating(Chr)
        else:
                #not auto-caught fapping
                if Chr in Keys:
                    menu:
                        "У вас есть ключ, ваши действия?"
                        "Вежливо постучать":
                                $ Line = "knock"

                        "Воспользоваться ключем, чтобы войти.":
                                call Set_The_Scene

                if Line != "knock" and Chr in Keys:
                        if Chr.Loc == bg_current:
                                #if she's home. . .
                                if Round <= 10:        #add "no" condition here
                                        if  "noentry" in Chr.RecentActions or "angry" in Chr.RecentActions:
                                                $ Chr.FaceChange("angry")
                                                if Chr is RogueX:
                                                        ch_r "Проваливай."
                                                elif Chr is KittyX:
                                                        ch_k "ПНХ."
                                                elif Chr is EmmaX:
                                                        ch_e "Вон!"
                                                elif Chr is LauraX:
                                                        ch_l "Убирайся отсюда."
                                                elif Chr is JeanX:
                                                        ch_j "Вон!"
                                                elif Chr is StormX:
                                                        ch_s "Убирайся."
                                                elif Chr is JubesX:
                                                        ch_v "Вон!"
                                                elif Chr is GwenX:
                                                        ch_g "Уходи!"
                                                elif Chr is BetsyX:
                                                        ch_b "Прочь."
                                                elif Chr is DoreenX:
                                                        ch_d "Уходи!"
                                                elif Chr is WandaX:
                                                        ch_w "Вон!"
                                                "[Chr.Name] выталкивает вас обратно в коридор."
                                                return
                                        if Time_Count >= 3: #night time
                                                "Она спит в своей постели. Вы тихонько выходите." #fix add options here.
                                                return
                                elif "gonnafap" in Chr.DailyActions and D20 >= 5:
                                        #girl caught fapping
                                        call Girl_Caught_Mastubating(Chr)
                                elif D20 >=15 and Chr.Loc == bg_current and ApprovalCheck(Chr, 1200,TabM=0) and AloneCheck(Chr):
                                        #girl waiting for you
                                        call Girl_Waiting(Chr,0) #didn't knock
                                        jump Misplaced
                                elif D20 >=15 and (Time_Count >= 3 or Time_Count == 0):
                                        #girl caught changing
                                        call Girl_Caught_Changing(Chr)
                                        jump expression Chr.Tag + "_Room"
                #End "if you enter without knocking"

                else:
                            #You knocked
                            "Вы стучитесь в  дверь к [Chr.Name_dat]."
                            if Chr.Loc != bg_current:
                                        "Похоже ее сейчас нет в комнате."

                                        if Chr in Keys:
                                                menu:
                                                    "Войти и дождаться ее?"
                                                    "Да":
                                                            $ Line = 0
                                                            jump expression Chr.Tag + "_Room"
                                                    "Нет":
                                                            pass
                                        "Вы возвращаетесь назад."
                                        $ bg_current = "bg campus"
                                        call Set_The_Scene
                                        jump Misplaced

                            if Round <= 10:
                                    if Time_Count >= 3: #night time
                                        "Ответа нет, наверное, она спит."
                                        $ bg_current = "bg campus"
                                        call Set_The_Scene
                                        jump Misplaced

                            if (D20 >=19 and Chr.Lust >= 50) or (D20 >=15 and Chr.Lust >= 70) or (D20 >=10 and Chr.Lust >= 80):
                                    #Girl caught fapping
                                    "Вы слышите тихие стоны, за которыми следуют звуки, словно какие-то предметы падают на пол."
                                    "Через несколько секунд шебуршаний, [Chr.Name] подходит к двери."
                                    $ Chr.FaceChange("perplexed",2)
                                    call Set_The_Scene
                                    show bg_opendoor zorder 151
                                    if Chr is RogueX:
                                            ch_r "Извини за ожидание, [Chr.Petname], я. . . тренировалась."
                                    elif Chr is KittyX:
                                            ch_k "О, привет, [Chr.Petname], Я. . . а, неважно."
                                    elif Chr is EmmaX:
                                            ch_e "Привет. Я была немного. . . занята."
                                    elif Chr is LauraX:
                                            ch_l "Эм, привет, [Chr.Petname], я избавлялась от стресса."
                                    elif Chr is JeanX:
                                            ch_j "Ох, эм, привет."
                                    elif Chr is StormX:
                                            ch_s "Ах, [Chr.Petname], я была. . . занята."
                                    elif Chr is JubesX:
                                            ch_v "О, эм, [Chr.Petname]. Я просто. . . кое-что улаживала."
                                    elif Chr is GwenX:
                                            ch_g "О, я, эм. . . читала."
                                    elif Chr is BetsyX:
                                            ch_b "Извини. . . я была. . . очень занята."
                                    elif Chr is DoreenX:
                                            ch_d "Ох, эм. . . я. . . упражнялась."
                                    elif Chr is WandaX:
                                            ch_w "О, привет. . . я тут. . . кое-чем занималась."
                                    $ Chr.FaceChange("perplexed",1)
                                    $ Tempmod += 10
                            elif D20 >=15 and Chr.Loc == bg_current and ApprovalCheck(Chr, 1200,TabM=0) and AloneCheck(Chr):
                                    #girl waiting for you
                                    call Girl_Waiting(Chr,1) #did knock
                                    jump Misplaced
                            elif D20 >=15 and (Time_Count >= 3 or Time_Count == 0):
                                    #Girl caught changing
                                    "Вы слышите шорох ткани и какой-то стук, но через несколько секунд [Chr.Name] все-таки подходит к двери."
                                    call Set_The_Scene
                                    show bg_opendoor zorder 151
                                    if Chr is RogueX:
                                            ch_r "Извини за ожидание, [Chr.Petname], Я просто переодевалась."
                                    elif Chr is KittyX:
                                            ch_k "О, привет, [Chr.Petname], я просто переодевалась."
                                    elif Chr is EmmaX:
                                            ch_e "Ох, входи, [Chr.Petname], не обращай внимания, я просто переодевалась."
                                    elif Chr is LauraX:
                                            ch_l "Привет, [Chr.Petname], я как раз одевалась."
                                    elif Chr is JeanX:
                                            ch_j "Привет, [Chr.Petname], я одевалась."
                                    elif Chr is StormX:
                                            ch_s "Ох, здравствуй, [Chr.Petname], Я просто переодевалась."
                                    elif Chr is JubesX:
                                            ch_v "О, привет, [Chr.Petname], Я переодевалась."
                                    elif Chr is GwenX:
                                            ch_g "Привет, я переодевалась."
                                    elif Chr is BetsyX:
                                            ch_b "Ох, я переодевалась."
                                    elif Chr is DoreenX:
                                            ch_d "О, привет. . . я переодевалась."
                                    elif Chr is WandaX:
                                            ch_w "Я переодевалась."
                            elif "angry" in Chr.RecentActions:
                                    $ Chr.FaceChange("angry")
                                    if Chr is RogueX:
                                            ch_r "Мне сейчас не нужна твоя компания."
                                    elif Chr is KittyX:
                                            ch_k "Неее-а."
                                    elif Chr is EmmaX:
                                            ch_e "У меня нет на это времени."
                                    elif Chr is LauraX:
                                            ch_l "Нет."
                                    elif Chr is JeanX:
                                            ch_j "Вон!"
                                    elif Chr is StormX:
                                            ch_s "Убирайся."
                                    elif Chr is JubesX:
                                            ch_v "Вон!"
                                    elif Chr is GwenX:
                                            ch_g "Уходи!"
                                    elif Chr is BetsyX:
                                            ch_b "Прочь!"
                                    elif Chr is DoreenX:
                                            ch_d "Уходи!"
                                    elif Chr is WandaX:
                                            ch_w "Вон!"
                                    $ Trigger = 0
                                    "[Chr.Name] выталкивает вас обратно в коридор и захлопывает дверь."
                                    $ bg_current = "bg campus"
                                    jump Misplaced
                            else:
                                    call Set_The_Scene
                                    show bg_opendoor zorder 151
                                    "[Chr.Name] открывает дверь и высовывается наружу."
                                    "Вы спрашиваете, можете ли вы войти внутрь."
                #End "if you knocked"

                #if you reach this point then you've asked to enter.
                if Chr.Loc != bg_current:
                        show bg_opendoor zorder 151
                        "Похоже, ее сейчас нет в комнате."
                        if Chr in Keys:
                                menu:
                                    "Войти и дождаться ее?"
                                    "Да":
                                            $ Line = 0
                                            jump expression Chr.Tag + "_Room"
                                    "Нет":
                                            pass
                        "Вы возвращаетесь назад."
                        $ bg_current = "bg campus"
                        jump Misplaced
                elif Time_Count >= 3 and "noentry" in Chr.RecentActions:
                        if Chr is RogueX:
                                ch_r "Эй, я же сказала тебе, тебе здесь не рады. Увидимся завтра."
                        elif Chr is KittyX:
                                ch_k "Катись отсюда. Увидимся завтра."
                        elif Chr is EmmaX:
                                ch_e "В другой раз, [Chr.Petname]."
                        elif Chr is LauraX:
                                ch_l "Не сегодня, [Chr.Petname]."
                        elif Chr is JeanX:
                                ch_j "Нет, не сегодня."
                        elif Chr is StormX:
                                ch_s "Я уже ясно дала понять, [Chr.Petname], не сегодня."
                        elif Chr is JubesX:
                                ch_v "Не доставай меня по ночам, [Chr.Petname]. Уходи!"
                        elif Chr is GwenX:
                                ch_g "Как я уже сказала, не сегодня."
                        elif Chr is BetsyX:
                                ch_b "Сегодня тебе здесь не рады, увидимся завтра."
                        elif Chr is DoreenX:
                                ch_d "Я сказала, что уже слишком поздно, увидимся завтра."
                        elif Chr is WandaX:
                                ch_w "До завтра."
                        $ bg_current = "bg campus"
                        jump Misplaced
                elif "noentry" in Chr.RecentActions or "angry" in Chr.RecentActions:
                        $ Chr.FaceChange("angry")
                        if Chr is RogueX:
                                ch_r "Проваливай."
                        elif Chr is KittyX:
                                ch_k "ПНХ."
                        elif Chr is EmmaX:
                                ch_e "Вон!"
                        elif Chr is LauraX:
                                ch_l "Убирайся отсюда."
                        elif Chr is JeanX:
                                ch_j "Вон!"
                        elif Chr is StormX:
                                ch_s "Убирайся."
                        elif Chr is JubesX:
                                ch_v "Вон!"
                        elif Chr is GwenX:
                                ch_g "Уходи!"
                        elif Chr is BetsyX:
                                ch_b "Прочь."
                        elif Chr is DoreenX:
                                ch_d "Уходи!"
                        elif Chr is WandaX:
                                ch_w "Вон!"
                        $ bg_current = "bg campus"
                        jump Misplaced
                elif Time_Count >= 3 and (Chr.Sleep or Chr.SEXP >= 30 or ApprovalCheck(Chr, 1000, "LI") or ApprovalCheck(Chr, 600, "OI") or Chr is JubesX):
                        #It's late but she really likes you
                        if Chr is RogueX:
                                ch_r "Уже довольно поздно, [Chr.Petname], но мне всегда приятно тебя видеть."
                        elif Chr is KittyX:
                                if not Player.Male:
                                    ch_k "Уже поздно, [Chr.Petname], но ты такая милая."
                                else:
                                    ch_k "Уже поздно, [Chr.Petname], но ты такой милый."
                        elif Chr is EmmaX:
                                ch_e "Уже довольно поздно, [Chr.Petname]. . ."
                                if not Player.Male:
                                    ch_e "но ты такая очаровательная."
                                else:
                                    ch_e "но ты такой очаровательный."
                        elif Chr is LauraX:
                                ch_l "Уже поздно, но я надеялась, что ты заглянешь."
                        elif Chr is JeanX:
                                ch_j "Привет, [Chr.Petname], уже почти пора ложиться спать."
                        elif Chr is StormX:
                                ch_s "Здравствуй, [Chr.Petname], уже почти пора спать."
                        elif Chr is JubesX:
                                ch_v "О, привет, [Chr.Petname], заходи."
                        elif Chr is GwenX:
                                ch_g "Уже довольно поздно, но ты можешь зайти ненадолго."
                        elif Chr is BetsyX:
                                ch_b "Уже довольно поздно, но. . . заходи."
                        elif Chr is DoreenX:
                                ch_d "Уже довольно поздно, я могу тебе как-нибудь помочь?"
                        elif Chr is WandaX:
                                ch_w "Уже поздно, но у меня есть немного времени."
                elif Chr.Addict >= 50 or (Chr is DoreenX and "SGattic" in Player.History):
                        $ Chr.FaceChange("manic")
                        if Chr is RogueX:
                                ch_r "Эм, да, тебе лучше войти. . ."
                        elif Chr is KittyX:
                                ch_k "Мне нужно немного внимания. . ."
                        elif Chr is EmmaX:
                                if not Player.Male:
                                    ch_e "Я. . . ты должна войти. . ."
                                else:
                                    ch_e "Я. . . ты должен войти. . ."
                        elif Chr is LauraX:
                                if not Player.Male:
                                    ch_l "Ты должна войти. . ."
                                else:
                                    ch_l "Ты должен войти. . ."
                        elif Chr is JeanX:
                                ch_j "Ох, эм. . . привет. . ."
                        elif Chr is StormX:
                                ch_s "О, да, входи."
                        elif Chr is JubesX:
                                ch_v "О, да, заходи. . ."
                        elif Chr is GwenX:
                                ch_g "О, да, заходи."
                        elif Chr is BetsyX:
                                ch_b "Ох. . . заходи."
                        elif Chr is DoreenX:
                                ch_d "Ладно, заходи. . ."
                        elif Chr is WandaX:
                                ch_w "Ага, заходи."
                elif Time_Count >= 3 and (ApprovalCheck(Chr, 500, "LI") or ApprovalCheck(Chr, 300, "OI")):
                        if Chr is RogueX:
                                ch_r "Уже довольно поздно, [Chr.Petname]. Может быть завтра."
                        elif Chr is KittyX:
                                ch_k "Уже поздно [Chr.Petname]. До завтра?"
                        elif Chr is EmmaX:
                                ch_e "Уже поздно, [Chr.Petname]. Увидимся завтра."
                        elif Chr is LauraX:
                                ch_l "Уже поздно, [Chr.Petname]. Приходи завтра."
                        elif Chr is JeanX:
                                ch_j "Уже поздно, увидимся."
                        elif Chr is StormX:
                                if not Player.Male:
                                    ch_s "Ты пришла довольно поздно, [Chr.Petname], тебе лучше заглянуть в другое время."
                                else:
                                    ch_s "Ты пришел довольно поздно, [Chr.Petname], тебе лучше заглянуть в другое время."
                        elif Chr is JubesX:
                                ch_v "Не-а. . ."
                        elif Chr is GwenX:
                                ch_g "Уже довольно поздно, может быть завтра."
                        elif Chr is BetsyX:
                                ch_b "Уже довольно поздно. . . возможно, поговорим завтра?"
                        elif Chr is DoreenX:
                                ch_d "Уже довольно поздно, может, поговорим завтра?"
                        elif Chr is WandaX:
                                ch_w "Уже поздно, давай завтра?"
                        $ Chr.RecentActions.append("noentry")
                        $ Chr.DailyActions.append("noentry")
                        $ bg_current = "bg campus"
                        jump Misplaced
                elif ApprovalCheck(Chr, 600, "LI") or ApprovalCheck(Chr, 300, "OI"):
                        #She quite likes you and lets you in
                        if Chr is RogueX:
                                ch_r "Конечно, заходи [Chr.Petname]."
                        elif Chr is KittyX:
                                ch_k "Конечно, заходи [Chr.Petname]."
                        elif Chr is EmmaX:
                                ch_e "Заходи, [Chr.Petname]."
                        elif Chr is LauraX:
                                ch_l "Думаю, ты можешь чувствовать себя как дома."
                        elif Chr is JeanX:
                                ch_j "Привет, чувствуй себя как дома."
                        elif Chr is StormX:
                                ch_s "Ох, здравствуй, [Chr.Petname], входи."
                        elif Chr is JubesX:
                                ch_v "О, привет, [Chr.Petname], входи."
                        elif Chr is GwenX:
                                ch_g "О, привет, заходи."
                        elif Chr is BetsyX:
                                ch_b "Ох, пожалуйста, входи."
                        elif Chr is DoreenX:
                                ch_d "О, привет, добро пожаловать!"
                        elif Chr is WandaX:
                                ch_w "Привет! Заходи и присаживайся."
                else:
                        #She doesn't like you
                        if Chr is RogueX:
                                if not Player.Male:
                                    ch_r "Я бы предпочла, чтобы ты не входила, спасибо."
                                else:
                                    ch_r "Я бы предпочла, чтобы ты не входил, спасибо."
                        elif Chr is KittyX:
                                ch_k "Нет, оставайся снаружи."
                        elif Chr is EmmaX:
                                ch_e "Я не думаю, что это уместно."
                        elif Chr is LauraX:
                                ch_l "Нет."
                        elif Chr is JeanX:
                                ch_j "Нет, уходи уже."
                        elif Chr is StormX:
                                if not Player.Male:
                                    ch_s "Я бы предпочла, чтобы ты не входила."
                                else:
                                    ch_s "Я бы предпочла, чтобы ты не входил."
                        elif Chr is JubesX:
                                ch_v "Ох, нет, спасибо."
                        elif Chr is GwenX:
                                ch_g "Нет, оставайся снаружи. . ."
                        elif Chr is BetsyX:
                                if not Player.Male:
                                    ch_b "Я бы предпочла, чтобы ты осталась снаружи."
                                else:
                                    ch_b "Я бы предпочла, чтобы ты остался снаружи."
                        elif Chr is DoreenX:
                                ch_d "Эм, тебе, пожалуй, дучше остаться снаружи. . ."
                        elif Chr is WandaX:
                                ch_w "Тебе, пожалуй, лучше остаться снаружи."
                        $ Chr.RecentActions.append("noentry")
                        $ Chr.DailyActions.append("noentry")
                        $ bg_current = "bg campus"
                        jump Misplaced

        # If you get this far, she's allowed you in
        if "SGattic" in Player.History:
                $ DoreenX.Loc = "bg doreen"
        call EventCalls
        if Chr is DoreenX and "SGattic" in Player.History and "visit" not in DoreenX.RecentActions:
                #if she's in hiding,
                call Doreen_Visit
        if Chr.Loc == Chr.Home and "angry" in Chr.RecentActions:
                # if she's home and pissed, she kicks you out
                $ Line = 0
                $ Trigger = 0
                "[Chr.Name] выталкивает вас обратно в коридор и захлопывает дверь. Вы возвращаетесь в свою комнату."
                $ bg_current = "bg player"
                jump Misplaced
        jump Misplaced

# End Girls room entry / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Rogue's Room Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Rogue_Room: #rkeljsvgb
    $ bg_current = "bg rogue"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    call GirlsAngry

# Комната [RogueX.Name_rod] Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if RogueX.Loc == bg_current:
        $ Line = "Вы в комнате "+RogueX.Name_rod+". Чем займетесь?"
    else:
        $ Line = "Вы в комнате "+RogueX.Name_rod+" но ее самой здесь нет. Чем займетесь?"
    menu:
        "[Line]"

        "Общаться":
                    call Chat

        "Желаешь позаниматься?":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                if RogueX.Loc == bg_current and not ApprovalCheck(RogueX, 1000):
                    if not Player.Male:
                        ch_r "Эй, не могла бы ты оставить ее открытой, [RogueX.Petname]?"
                    else:
                        ch_r "Эй, не мог бы ты оставить ее открытой, [RogueX.Petname]?"
                else:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Спать" if Time_Count >= 3: #night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Ждать" if Time_Count < 3: #not night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Вернуться в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты других Девушек" if TravelMode:
            menu:
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    if "angry" in RogueX.RecentActions:
            $ RogueX.FaceChange("angry")
            ch_r "Я думаю, тебе следует уйти."
            "[RogueX.Name] выталкивает вас обратно в коридор и захлопывает дверь. Вы возвращаетесь в свою комнату."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Rogue_Room

# end Комната [RogueX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


# Комната [KittyX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


label Kitty_Room: #rkeljsvgb
    $ bg_current = "bg kitty"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    call GirlsAngry

# Комната [KittyX.Name_rod] Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if KittyX.Loc == bg_current:
        $ Line = "Вы находитесь в комнате "+KittyX.Name_rod+". Чем займетесь?"
    else:
        $ Line = "Вы находитесь в комнате "+KittyX.Name_rod+", но ее самой здесь нет. Чем займетесь?"
    menu:
        "[Line]"

        "Общаться":
                    call Chat

        "Желаешь позаниматься?":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                if KittyX.Loc == bg_current and not ApprovalCheck(KittyX, 1000):
                    if not Player.Male:
                        ch_k "Эм, я бы[KittyX.like]предпочла, чтобы ты не закрывала мою дверь, [KittyX.Petname]."
                    else:
                        ch_k "Эм, я бы[KittyX.like]предпочла, чтобы ты не закрывал мою дверь, [KittyX.Petname]."
                else:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Спать" if Time_Count >= 3: #night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Ждать" if Time_Count < 3: #not night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Вернуться в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты других Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    if "angry" in KittyX.RecentActions:
            $ KittyX.FaceChange("angry")
            ch_k "Уходи. Сейчас же."
            "[KittyX.Name] выталкивает вас обратно в коридор и захлопывает дверь. Вы возвращаетесь в свою комнату."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Kitty_Room

# end Комната [KittyX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


# Emma's Room Interface //////////////////////////////////////////////////////////////////////


label Emma_Room: #rkeljsvgb
    $ bg_current = "bg emma"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    call GirlsAngry

# Emma's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if EmmaX.Loc == bg_current:
        $ Line = "Вы находитесь в комнате "+EmmaX.Name_rod+". Чем займетесь?"
    else:
        $ Line = "Вы находитесь в комнате "+EmmaX.Name_rod+", но ее самой здесь нет. Чем займетесь?"
    menu:
        "[Line]"

        "Общаться":
                    call Chat

        "Желаешь позаниматься?":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                if EmmaX.Loc == bg_current and not ApprovalCheck(EmmaX, 1000):
                    ch_e "Ты правда думаешь, что тебе стоит закрывать дверь в мою комнату?"
                else:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Спать" if Time_Count >= 3 and EmmaX.Loc == bg_current:
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Ждать" if Time_Count < 3: #not night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Вернуться в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты других Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                            jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                            call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                            jump Campus_Entry

    if "angry" in EmmaX.RecentActions:
            $ EmmaX.FaceChange("angry")
            ch_e "Я думаю, тебе лучше уйти."
            "[EmmaX.Name] выталкивает вас обратно в коридор и захлопывает дверь. Вы возвращаетесь в свою комнату."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Emma_Room


# end Emma's Room Interface //////////////////////////////////////////////////////////////////////


# Laura's Room Interface //////////////////////////////////////////////////////////////////////

label Laura_Room: #rkeljsvgb
    $ bg_current = "bg laura"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    call GirlsAngry

# Laura's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if LauraX.Loc == bg_current:
        $ Line = "Вы находитесь в комнате "+LauraX.Name_rod+". Чем займетесь?"
    else:
        $ Line = "Вы находитесь в комнате "+LauraX.Name_rod+", но ее самой здесь нет. Чем займетесь?"
    menu:
        "[Line]"

        "Общаться":
                    call Chat

        "Желаешь позаниматься?":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                if LauraX.Loc == bg_current and not ApprovalCheck(LauraX, 1200):
                    ch_l "[LauraX.Petname], я не хочу чувствовать себя как в клетке."
                else:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Спать" if Time_Count >= 3: #night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Ждать" if Time_Count < 3: #not night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Вернуться в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты других Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    if "angry" in LauraX.RecentActions:
            $ LauraX.FaceChange("angry")
            $ Line = 0
            $ Trigger = 0
            ch_l "Убирайся, пока мы оба не пожалели об этом."
            "[LauraX.Name] выталкивает вас обратно в коридор и захлопывает дверь. Вы возвращаетесь в свою комнату."
            jump Player_Room
    jump Laura_Room
# End Laura's Room Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Jean's Room Interface //////////////////////////////////////////////////////////////////////

label Jean_Room: #rkeljsvgb
    $ bg_current = "bg jean"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    call GirlsAngry

# Jean's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if JeanX.Loc == bg_current:
        $ Line = "Вы находитесь в комнате "+JeanX.Name_rod+". Чем займетесь?"
    else:
        $ Line = "Вы находитесь в комнате "+JeanX.Name_rod+", но ее самой здесь нет. Чем займетесь?"
    menu:
        "[Line]"

        "Общаться":
                    call Chat

        "Желаешь позаниматься?":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                if JeanX.Loc == bg_current and not ApprovalCheck(JeanX, 1200):
                    ch_j "Эй, не закрывай дверь."
                else:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Спать" if Time_Count >= 3: #night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Ждать" if Time_Count < 3: #not night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Вернуться в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты других Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    if "angry" in JeanX.RecentActions:
            $ JeanX.FaceChange("angry")
            $ Line = 0
            $ Trigger = 0
            ch_j "Вон!"
            "[JeanX.Name] выталкивает вас обратно в коридор и захлопывает дверь. Вы возвращаетесь в свою комнату."
            jump Player_Room
    jump Jean_Room
# End Jean's Room Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Комната [StormX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


label Storm_Room: #rkeljsvgb
    $ bg_current = "bg storm"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    call GirlsAngry

# Комната [StormX.Name_rod] Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if StormX.Loc == bg_current:
        $ Line = "Вы находитесь в комнате "+StormX.Name_rod+". Чем займетесь?"
    else:
        $ Line = "Вы находитесь в комнате "+StormX.Name_rod+", но ее самой здесь нет. Чем займетесь?"
    menu:
        "[Line]"

        "Общаться":
                    call Chat

        "Желаешь позаниматься?":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                if StormX.Loc == bg_current and not ApprovalCheck(StormX, 1000):
                    if not Player.Male:
                        ch_s "Я бы предпочла, чтобы ты не запирала дверь, [StormX.Petname]."
                    else:
                        ch_s "Я бы предпочла, чтобы ты не запирал дверь, [StormX.Petname]."
                else:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Спать" if Time_Count >= 3 and StormX.Loc == bg_current:
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Ждать" if Time_Count < 3: #not night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Вернуться в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты других Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    if "angry" in StormX.RecentActions:
            $ StormX.FaceChange("angry")
            ch_s "Уходи. Сейчас же."
            "[StormX.Name] выталкивает вас на лестницу и захлопывает дверь. Вы возвращаетесь в свою комнату."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Storm_Room

# end Комната [StormX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


# Комната [JubesX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


label Jubes_Room: #rkeljsvgb
    $ bg_current = "bg jubes"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    call GirlsAngry

# Комната [JubesX.Name_rod] Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if JubesX.Loc == bg_current:
        $ Line = "Вы находитесь в комнате "+JubesX.Name_rod+". Чем займетесь?"
    else:
        $ Line = "Вы находитесь в комнате "+JubesX.Name_rod+", но ее самой здесь нет. Чем займетесь?"
    menu:
        "[Line]"

        "Общаться":
                    call Chat

        "Желаешь позаниматься?":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                if JubesX.Loc == bg_current and not ApprovalCheck(JubesX, 1000):
                    ch_v "Тебе не стоит запирать -мою- дверь, [JubesX.Petname]."
                else:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Спать" if Time_Count >= 3: #night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Ждать" if Time_Count < 3: #not night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Вернуться в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты других Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    if "angry" in JubesX.RecentActions:
            $ JubesX.FaceChange("angry")
            ch_v "Вон!"
            "[JubesX.Name] выталкивает вас обратно в коридор и захлопывает дверь. Вы возвращаетесь в свою комнату."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Jubes_Room

# end Комната [JubesX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


# Комната [GwenX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


label Gwen_Room: #rkeljsvgb
    $ bg_current = "bg gwen"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    call GirlsAngry

# Комната [GwenX.Name_rod] Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if GwenX.Loc == bg_current:
        $ Line = "Вы находитесь в комнате "+GwenX.Name_rod+". Чем займетесь?"
    else:
        $ Line = "Вы находитесь в комнате "+GwenX.Name_rod+", но ее самой здесь нет. Чем займетесь?"
    menu:
        "[Line]"

        "Общаться":
                    call Chat

        "Желаешь позаниматься?":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                if GwenX.Loc == bg_current and not ApprovalCheck(GwenX, 1000):
                    if not Player.Male:
                        ch_g "Почему это ты заперла меня в моей собственной комнате, [GwenX.Petname]?"
                    else:
                        ch_g "Почему это ты запер меня в моей собственной комнате, [GwenX.Petname]?"
                else:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Спать" if Time_Count >= 3: #night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Ждать" if Time_Count < 3: #not night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Вернуться в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты других Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    if "angry" in GwenX.RecentActions:
            $ GwenX.FaceChange("angry")
            ch_g "Уходи!"
            "[GwenX.Name] выталкивает вас обратно в коридор и захлопывает дверь. Вы возвращаетесь в свою комнату."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Gwen_Room

# end Комната [GwenX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


# Комната [BetsyX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


label Betsy_Room: #rkeljsvgb
    $ bg_current = "bg betsy"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    call GirlsAngry

# Комната [BetsyX.Name_rod] Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if BetsyX.Loc == bg_current:
        $ Line = "Вы находитесь в комнате "+BetsyX.Name_rod+". Чем займетесь?"
    else:
        $ Line = "Вы находитесь в комнате "+BetsyX.Name_rod+", но ее самой здесь нет. Чем займетесь?"
    menu:
        "[Line]"

        "Общаться":
                    call Chat

        "Желаешь позаниматься?":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                if BetsyX.Loc == bg_current and not ApprovalCheck(BetsyX, 1000):
                    ch_b "Мне не нравится, что ты запираешь меня в моей собственной комнате."
                else:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Спать" if Time_Count >= 3: #night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Ждать" if Time_Count < 3: #not night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Вернуться в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты других Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    if "angry" in BetsyX.RecentActions:
            $ BetsyX.FaceChange("angry")
            ch_b "Прочь!"
            "[BetsyX.Name] выталкивает вас обратно в коридор и захлопывает дверь. Вы возвращаетесь в свою комнату."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Betsy_Room

# end Комната [BetsyX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


# Комната [DoreenX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


label Doreen_Room: #rkeljsvgb
    $ bg_current = "bg doreen"
    $ Player.DrainWord("traveling",1,0)
    if "SGattic" in Player.History:
            $ DoreenX.Loc = "bg doreen"
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    if "SGattic" in Player.History:
            $ DoreenX.Loc = "bg doreen"
    call GirlsAngry

# Комната [DoreenX.Name_rod] Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if DoreenX.Loc == bg_current:
        $ Line = "Вы находитесь в комнате "+DoreenX.Name_rod+". Чем займетесь?"
    else:
        $ Line = "Вы находитесь в комнате "+DoreenX.Name_rod+", но ее самой здесь нет. Чем займетесь?"
    menu:
        "[Line]"

        "Общаться":
                    call Chat

        "Желаешь позаниматься?":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                if DoreenX.Loc == bg_current and not ApprovalCheck(DoreenX, 1000):
                    ch_d "Не следует запирать людей в их собственных комнатах. . ."
                else:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Спать" if Time_Count >= 3: #night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Ждать" if Time_Count < 3: #not night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Вернуться в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты других Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [WandaX.Name_rod]" if "met" in WandaX.History:
                            call Girls_Room_Entry(WandaX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    if "angry" in DoreenX.RecentActions:
            $ DoreenX.FaceChange("angry")
            ch_d "Уходи!"
            "[DoreenX.Name] выталкивает вас обратно в коридор и захлопывает дверь. Вы возвращаетесь в свою комнату."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Doreen_Room

# end Комната [DoreenX.Name_rod] Interface //////////////////////////////////////////////////////////////////////

# Комната [WandaX.Name_rod] Interface //////////////////////////////////////////////////////////////////////


label Wanda_Room: #rkeljsvgb
    $ bg_current = "bg wanda"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
#                call Girls_Location
                call EventCalls
    call GirlsAngry

# Комната [WandaX.Name_rod] Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if WandaX.Loc == bg_current:
        $ Line = "Вы находитесь в комнате "+WandaX.Name_rod+". Чем займетесь?"
    else:
        $ Line = "Вы находитесь в комнате "+WandaX.Name_rod+", но ее самой здесь нет. Чем займетесь?"
    menu:
        "[Line]"

        "Общаться":
                    call Chat

        "Желаешь позаниматься?":
                    call Study_Session

        "Запереть дверь" if "locked" not in Player.Traits:
                if WandaX.Loc == bg_current and not ApprovalCheck(WandaX, 1000):
                    ch_w "Мне не нравится, когда кто-то запирает мою дверь."
                else:
                    "Вы запираете дверь."
                    $ Player.Traits.append("locked")
                    call Taboo_Level

        "Отпереть дверь" if "locked" in Player.Traits:
                    "Вы отпираете дверь."
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Спать" if Time_Count >= 3: #night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Ждать" if Time_Count < 3: #not night time
                    call Round10
#                    call Girls_Location
                    call EventCalls

        "Вернуться в свою комнату" if TravelMode:
                    jump Player_Room_Entry
        "Комнаты других Девушек" if TravelMode:
            menu:
                "Комната [RogueX.Name_rod]":
                            call Girls_Room_Entry(RogueX)
                "Комната [KittyX.Name_rod]" if "met" in KittyX.History:
                            call Girls_Room_Entry(KittyX)
                "Комната [EmmaX.Name_rod]" if "met" in EmmaX.History:
                            call Girls_Room_Entry(EmmaX)
                "Комната [LauraX.Name_rod]" if "met" in LauraX.History:
                            call Girls_Room_Entry(LauraX)
                "Комната [JeanX.Name_rod]" if "met" in JeanX.History:
                            call Girls_Room_Entry(JeanX)
                "Комната [StormX.Name_rod]" if "met" in StormX.History:
                            call Girls_Room_Entry(StormX)
                "Комната [JubesX.Name_rod]" if "met" in JubesX.History:
                            call Girls_Room_Entry(JubesX)
                "Комната [GwenX.Name_rod]" if "met" in GwenX.History:
                            call Girls_Room_Entry(GwenX)
                "Комната [BetsyX.Name_rod]" if "met" in BetsyX.History:
                            call Girls_Room_Entry(BetsyX)
                "Комната [DoreenX.Name_rod]" if "met" in DoreenX.History:
                            call Girls_Room_Entry(DoreenX)
                "Назад":
                            pass
        "Душевые" if TravelMode:
                    jump Shower_Room_Entry

        "Выйти" if not TravelMode:
                    call Worldmap
        "Выйти [[Перейти на площадь кампуса]" if TravelMode:
                    jump Campus_Entry

    if "angry" in WandaX.RecentActions:
            $ WandaX.FaceChange("angry")
            ch_w "Хватит с меня мутантов!"
            "[WandaX.Name] выталкивает вас обратно в коридор и захлопывает дверь. Вы возвращаетесь в свою комнату."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Wanda_Room

# end Комната [WandaX.Name_rod] Interface //////////////////////////////////////////////////////////////////////
