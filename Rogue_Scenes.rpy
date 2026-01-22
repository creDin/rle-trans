# Prologue //////////////////////////////////////////////////////////////////////

label Prologue:
    $ bg_current = "bg study"
    $ Time_Count = 2
    $ Current_Time = "Evening"
    call Display_Background
    # Modification mode
    scene
    # -----------------
    if "Historia" in Player.Traits: #Simulation haze
                show BlueScreen onlayer black
    $ RogueX.Name = "Роуг"
    $ RogueX.Name_rod = "Роуг"
    $ RogueX.Name_dat = "Роуг"
    $ RogueX.Name_vin = "Роуг"
    $ RogueX.Name_tvo = "Роуг"
    $ RogueX.Name_pre = "Роуг"
    "После того, как на ваш дом напал Страж, вы узнали, что являетесь мутантом.\n Тогда вас спас отряд Людей Икс, они же и дали вам этот адрес."
    "Поздним вечером вы прибыли в Институт Ксавье, где вам пообещали, что вы обретете новый дом."
    "С тех пор, как Апокалипсис был повержен, для мутантов настали трудные времена, хотя, будь иначе, вряд ли было бы лучше."
    if "Historia" not in Player.Traits:
            python:
                Player.Name  = renpy.input("Как вас зовут?", default="Зеро", length = 10)
                Player.Name  = Player.Name.strip()
                if not Player.Name :
                    Player.Name  = "Зеро"
                    Player.Name_rod  = "Зеро"
                    Player.Name_dat  = "Зеро"
                    Player.Name_vin  = "Зеро"
                    Player.Name_tvo  = "Зеро"
                    Player.Name_pre  = "Зеро"
                if Player.Name in ("хозяин", "господин", "любимый", "парень", "любовник", "ебарь", "хозяйка", "госпожа", "любимая", "девушка", "любовница", "ебунша"):
                    Line = "Хорошая попытка, умник."
                    Player.Name  = "Зеро"
                    Player.Name_rod  = "Зеро"
                    Player.Name_dat  = "Зеро"
                    Player.Name_vin  = "Зеро"
                    Player.Name_tvo  = "Зеро"
                    Player.Name_pre  = "Зеро"
                if Player.Name != "Зеро":
                    Player.Name_rod  = renpy.input("Имя в Р.п (у кого?)?", default=Player.Name, length = 10)
                    Player.Name_rod  = Player.Name_rod.strip()
                    Player.Name_dat  = renpy.input("Имя в Д.п (кому?)?", default=Player.Name, length = 10)
                    Player.Name_dat  = Player.Name_dat.strip()
                    Player.Name_vin  = renpy.input("Имя в В.п (кого?)?", default=Player.Name, length = 10)
                    Player.Name_vin  = Player.Name_vin.strip()
                    Player.Name_tvo  = renpy.input("Имя в Т.п (кем?)?", default=Player.Name, length = 10)
                    Player.Name_tvo  = Player.Name_tvo.strip()
                    Player.Name_pre  = renpy.input("Имя в П.п (о ком?)?", default=Player.Name, length = 10)
                    Player.Name_pre  = Player.Name_pre.strip()
                if Player.Name == "Зеро":
                    Player.Name_rod  = "Зеро"
                    Player.Name_dat  = "Зеро"
                    Player.Name_vin  = "Зеро"
                    Player.Name_tvo  = "Зеро"
                    Player.Name_pre  = "Зеро"
            if Line:
                "[Line]"
            menu:
                "Вы парень или девушка?"
                "Парень":
                        $ Player.Male = 1
                        $ Terms = Terms1
                        $ Loadout = Loadout1
                "Девушка":
                        $ Player.Male = 0
                        $ Terms = Terms0
                        $ Loadout = Loadout0
            menu:
                "Какого цвета ваша кожа?"
                "Зеленая":
                        $ Player.Color = "green"
                "Белая":
                        $ Player.Color = "pink"
                "Черная":
                        $ Player.Color = "brown"
                # Modification mode
                "Настроить":
                    $ Player.Color = "pink"
                    $ Player.Recolor.recolored = 1
                    $ Player.Recolor.screen_loop()
                # -----------------
    show Professor at SpriteLoc(StageLeft)
    with dissolve
    ch_x "Добро пожаловать в Институт Ксавье. Дом для всех мутантов, место, где они учатся и взрослеют."
    ch_x "Меня зовут Чарльз Ксавье. Я посвятил всю свою жизнь помощи мутантам, подобным тебе."
    ch_x "Я знаю, что последние несколько дней были трудными для тебя, но здесь ты в безопасности."
    ch_x "Здесь ты сможешь посещать занятия, на которых тебя обучат всему необходимому, а также приобрести в Комнате Опасности навыки самообороны."
    ch_x "Поскольку ты сирота, то мы предоставим тебе небольшую стипендию для твоих повседневных нужд."
    ch_x "У тебя есть какие-нибудь вопросы ко мне?"
    ch_p "Почему вы вообще меня сюда привели? У меня ведь нет никаких 'супер способностей'"
    ch_x "Глупости. У тебя есть одна неимоверно полезная способность. . ."
    ch_x "Ты обладаешь силой отменять способности других мутантов, включая мою."
    $ RogueX.Loc = bg_current
    $ RogueX.FaceChange("surprised")
    $ RogueX.SpriteLoc = StageFarRight
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)
    with easeinright
    if not Player.Male:
        ch_r "Это правда, профессор? На эту девушку не действуют способности других мутантов?"
    else:
        ch_r "Это правда, профессор? На этого парня не действуют способности других мутантов?"
    $ RogueX.Mouth = "normal"
    $ RogueX.SpriteLoc = StageRight
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) with ease
    ch_r "И моя?"
    if not Player.Male:
        ch_x "Верно, [RogueX.Name], хотя в настоящее время ее способности слабы и неконтролируемы."
        ch_x "Но придет день, когда, вероятно, она сможет навсегда лишить тебя способностей."
    else:
        ch_x "Верно, [RogueX.Name], хотя в настоящее время его способности слабы и неконтролируемы."
        ch_x "Но придет день, когда, вероятно, он сможет навсегда лишить тебя способностей."
    ch_r "! . . ."
    $ RogueX.FaceChange("smile")
    if not Player.Male:
        ch_x "Раз уж ты здесь, почему бы тебе не показать нашей новой гостье особняк?"
    else:
        ch_x "Раз уж ты здесь, почему бы тебе не показать нашему новому гостю особняк?"

    ch_x "Эту юную леди зовут [RogueX.Name], она одна из старших студентов."
    if not Player.Male:
        ch_x "[RogueX.Name], а эту юную леди зовут \"[Player.Name]\"."
    else:
        ch_x "[RogueX.Name], а этого молодого человека зовут \"[Player.Name]\"."

    hide Professor
    with easeoutright

    $ RogueX.SpriteLoc = StageCenter
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)
    with ease
    $ ActiveGirls.append(RogueX) if RogueX not in ActiveGirls else ActiveGirls

    menu:
        ch_r "Очень приятно с тобой познакомиться, [RogueX.Petname]. Давай-ка я расскажу, где тут самые злачные места."
        "Мне тоже очень приятно.":
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.FaceChange("smile", 1)
                if Player.Male:
                        ch_r "Ох, какой джентльмен. Думаю, мы с тобой поладим."
                else:
                        ch_r "Ох, ты настоящая леди. Думаю, мы с тобой поладим."
                $ RogueX.Blush = 0
                ch_r "Хорошо, давай пройдемся. . ."
        "\"Злачные\" места, значит?":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Brows = "normal"
                $ RogueX.Eyes = "surprised"
                $ RogueX.Mouth = "smile"
                $ RogueX.Blush = 1
                ch_r "Чт- что? Н-нет, я не это имела в виду! Я просто повожу тебя по кампусу!"
                $ RogueX.FaceChange("bemused")
                $ RogueX.Statup("Inbt", 200, 20)
                $ RogueX.Statup("Obed", 200, 20)
                ch_r "Хммм. . ."
                $ RogueX.Statup("Lust", 90, 3)
                $ RogueX.FaceChange("normal")
                $ RogueX.Eyes = "surprised"
                ch_r "Ладно, давай не будем отвлекаться. . ."
                $ RogueX.FaceChange("smile", 0)
        "Мне все равно.":
                $ RogueX.Statup("Obed", 200, 20)
                $ RogueX.FaceChange("sad")
                $ RogueX.Brows = "normal"
                ch_r "Тц, ну ладно, пошли."
        "Отвали.":
                $ RogueX.Statup("Love", 200, -30)
                $ RogueX.Statup("Obed", 200, 30)
                $ RogueX.FaceChange("angry")
                show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)
                with vpunch
                ch_r "Да что ты себе позволяешь!"
                ch_r "Пфф, мне все равно придется устроить тебе экскурсию, так что пошли. . ."


# End Prologue //////////////////////////////////////////////////////////////////////

# Tour //////////////////////////////////////////////////////////////////////
label tour_start:
    $ bg_current = "bg campus"
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)
    ch_r "Это площадь кампуса. Она объединяет все основные места и ты, скорее всего, будешь проходить через нее очень часто."


# Player's room
    $ bg_current = "bg player"
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)
    ch_r "А вот здесь твоя комната, теперь у каждого из нас есть свои личные комнаты, так как кампус расширили."
    menu:
        ch_r "Довольно уютно, правда?"
        "С тобой любая комната уютная.":
                $ RogueX.Blush = 1
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.Statup("Lust", 90, 5)
        "Сойдет.":
                $ RogueX.Statup("Obed", 200, 10)
    ch_p "А где ты живешь?"
    $ RogueX.Blush = 0
    ch_r "О, дальше по коридору, мимо не пройдешь, на каждой двери таблички с именами."
    if RogueX.Love <= 500:
            ch_r "Хотя, я бы посоветовала лишний раз не беспокоить меня."
    else:
            ch_r "Можешь как-нибудь заскочить, но только не после отбоя."

# Classrooms
    $ bg_current = "bg classroom"
    $ RogueX.Loc = bg_current
    call CleartheRoom("All",0,1)
    call Set_The_Scene(0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)
    ch_r "А это одна из наших самых современных аудиторий."
    ch_r "Она многоцелевая, поэтому здесь могут проходить какие угодно занятия."
    ch_r "Когда-то тут были помещения для внеучебных занятий, но за последние несколько лет это место превратилось в настоящий университет."


# Danger Room
    $ bg_current = "bg dangerroom"
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)
    ch_r "А это комната Опасности. Ее снабдили самой современной голографической техникой для проведения боевых симуляций, максимально приближенных к реальности."
    $ Count = 0
    while Count < 3:
        menu:
            extend ""
            "Зачем нужны эти боевые симуляции?" if Count != 1:
                    ch_r "Мир полон опасностей, [RogueX.Petname], особенно для нас, мутантов."
                    ch_r "Это место помогает нам тренироваться в использовании своих способностей. Посещение данного места, может помочь оценить свои силы."
                    $ Count = 3 if Count == 2 else 1
            "А это место умеет создать какие-нибудь. . . эротические симуляции?" if Count != 2:
                    $ RogueX.Eyes = "side"
                    $ RogueX.Mouth = "lipbite"
                    $ RogueX.Blush = 1
                    $ RogueX.Statup("Inbt", 200, 30)
                    $ RogueX.Statup("Lust", 200, 5)
                    ch_r "Ну. . . наверное. . . если кому-нибудь очень понадобится."
                    $ RogueX.FaceChange(B=0)
                    $ Count = 3 if Count == 1 else 2
            "Хорошо, пошли дальше.":
                    $ Count = 3
    $ Count = 0
    ch_r "Пойдем. . ."

label tour_end:
    $ bg_current = "bg campus"
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)
    ch_r "Ну, на этом краткий экскурс окончен, теперь ты знаешь, где что находится. . ."
    $ RogueX.Mouth = "normal"
    $ RogueX.Eyes = "normal"
    $ RogueX.Brows = "confused"
    menu:
        ch_r "Мне интересно узнать о твоих способностях. Правда ли, что силы других мутантов не действуют на тебя?"
        "Конечно.":
                ch_p "Ну, по крайней мере, мне так сказали, но, если честно, я мало что об этом знаю."
        "А тебе-то что?":
                ch_p "А тебе-то что?"
                $ RogueX.Eyes = "sexy"
                ch_r ". . ."
                $ RogueX.Statup("Love", 200, -30)
    ch_r "Видишь ли, моя сила позволяет мне поглощать способности и воспоминания тех мутантов, к которым я прикасаюсь."
    $ Head = 0
    ch_r "Вот только я все никак не могу взять эти силы под контроль. Я не могу прикоснуться к человеку, не навредив ему, а если буду неосторожна, то и вовсе могу отправить его в кому."
    ch_r "Поэтому я надеюсь, что раз ты владеешь такой силой. . ."
    $ RogueX.FaceChange("sexy")
    $ RogueX.Brows = "sad"
    menu:
        ch_r "Поэтому я надеюсь, что раз ты владеешь такой силой. . . Я могу прикоснуться к тебе?"
        "Хочешь поцеловать меня?":
            if RogueX.Love >= 500:
                    $ RogueX.Statup("Love", 200, 20)
                    $ RogueX.Statup("Obed", 200, 30)
                    $ RogueX.Statup("Inbt", 20, 20)
                    $ RogueX.FaceChange("surprised", 1)
                    if not Player.Male:
                        ch_r "А ты, я смотрю, очень уверена в себе."
                    else:
                        ch_r "А ты, я смотрю, очень уверен в себе."
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Mouth = "smile"
                    ch_r "Ладно, но только разочек."
                    $ RogueX.FaceChange("kiss")
                    call Girl_Smooch_Launch(RogueX)
                    "Она чмокает вас в щеку."
                    $ RogueX.FaceChange("smile")
            else:
                    $ RogueX.Statup("Love", 200, 30)
                    $ RogueX.FaceChange("bemused")
                    ch_r "Хех, [RogueX.Petname], тебе придется этого заслужить."
                    $ RogueX.Arms = 0
                    $ RogueX.ArmPose = 2
                    $ RogueX.FaceChange("sexy")
                    $ RogueX.Brows = "sad"
                    "Она снимает перчатку и касается вашего лица."
        "Без проблем, я в твоем распоряжении.":
                $ RogueX.Statup("Love", 200, 30)
                $ RogueX.FaceChange("smile")
                $ RogueX.Arms = 0
                $ RogueX.ArmPose = 2
                $ RogueX.FaceChange("sexy")
                $ RogueX.Brows = "sad"
                "Она снимает перчатку и касается вашего лица."
        "Нет, мне как-то стремно.":
                $ RogueX.Statup("Love", 200, -30)
                $ RogueX.Statup("Inbt", 200, 30)
                $ RogueX.FaceChange("sad")
                $ RogueX.Brows = "normal"
                ch_r "Извини, но мне уж слишком любопытно."
                $ RogueX.Arms = 0
                $ RogueX.ArmPose = 2
                "Она снимает перчатку и касается вашего лица."

    $ RogueX.FaceChange("surprised")
    ch_r "Ого."
    ch_r "Это потрясающе! Любого другого человека я бы уже истощила и он бы упал без сознания."
    $ RogueX.FaceChange("sexy")
    menu:
        ch_r "Знаешь, как давно я не могла ни к кому прикоснуться, не навредив?"
        "Рада, что смогла помочь." if not Player.Male:
                $ RogueX.Statup("Love", 200, 10)
        "Рад, что смог помочь." if Player.Male:
                $ RogueX.Statup("Love", 200, 10)
        "Думаю, очень и очень давно.":
                $ RogueX.Statup("Lust", 200, 5)
                $ RogueX.FaceChange("bemused", 1)
                ch_r ". . ."
    $ RogueX.FaceChange("smile")
    ch_r "Как быстро время пролетело. Ладно, на сегодня хватит, пора расходиться по комнатам, не задерживайся тут."
    $ RogueX.Blush = 0
    if RogueX.Love >= 500:
        ch_r "Может, как-нибудь пересечемся. Вот мой номер, позвони, как будет время."
        if "Historia" not in Player.Traits:
                $ Digits.append(RogueX)
    $ RogueX.Arms = "gloves"
    $ RogueX.ArmPose = 1
    $ RogueX.Addictionrate = 5

label tour_parting:
    $ RogueX.Emote = "normal"
    $ RogueX.Blush = 0
    if not RogueX.Kissed:
            $ Line = "Хочешь поцелуемся?"
    else:
            $ Line = "Хочешь еще поцелуемся?"
    menu:
        extend ""
        "Хорошо, увидимся позже.":
            "Вы возвращаетесь в свою комнату."
        "[Line]":
            if RogueX.Love >= 560:
                $ RogueX.FaceChange("bemused", 1)
                $ RogueX.Statup("Inbt", 10, 20)
                $ RogueX.Statup("Inbt", 50, 10)
                if "Historia" in Player.Traits:
                        return 1
                call Makeout
                if "angry" in RogueX.RecentActions:
                        $ RogueX.Statup("Love", 200, -10)
                        $ RogueX.Statup("Obed", 200, 30)
                        ch_r "Какого черта, [Player.Name]?!"
                        ch_r "Зачем так играться с чувствами девушки?!"
                        hide Rogue_Sprite with easeoutright
                        "[RogueX.Name] в слезах уходит, а возвращаетесь к себе в комнату."
                else:
                        $ RogueX.FaceChange("bemused", 1)
                        ch_r "Я бы еще хотела пообщаться с тобой, [RogueX.Petname], но на сегодня хватит. Увидимся."
                        hide Rogue_Sprite with easeoutright
                        "Вы возвращаетесь в свою комнату."
                        $ RogueX.Emote = "normal"
            else:
                if (RogueX.Love >= 530 or RogueX.Obed > 50) and not RogueX.Kissed:
                        $ RogueX.Addictionrate += 1
                        $ RogueX.Statup("Lust", 200, 5)
                        $ RogueX.Statup("Love", 200, 10)
                        $ RogueX.Kissed += 1
                        $ RogueX.FaceChange("bemused", 1)
                        ch_r "Ну, один поцелуй не повредит."
                        $ RogueX.FaceChange("kiss")
                        "Она быстро чмокает вас. Без языка."
                        jump tour_parting
                else:
                        $ RogueX.FaceChange("bemused")
                        ch_r "Нет, думаю, на сегодня с тебя хватит, [RogueX.Petname]."
                        "Вы возвращаетесь в свою комнату."
                        hide Rogue_Sprite
                        $ RogueX.Emote = "normal"

    $ RogueX.Loc = "bg rogue"
    if "Historia" in Player.Traits:
            return 0
    $ bg_current = "bg player"
    call Wait
    $ bg_current = "bg player"
    call Set_The_Scene
    "Это краткое руководство по особенностям данной игры. Если хотите, можете пропустить его, его всегда можно просмотреть позже в вашей комнате."
    call Tutorial
    jump Player_Room
return

# End Tour //////////////////////////////////////////////////////////////////////


# Event Rogue_Key /////////////////////////////////////////////////////
label Rogue_Key:
        call Shift_Focus(RogueX)
        $ RogueX.Loc = bg_current
        call Set_The_Scene
        $ RogueX.FaceChange("bemused")
        $ RogueX.ArmPose = 2
        $ Event_Queue = [0,0]
        if not Player.Male:
            ch_r "Я тут подумала, ты уже много раз ночевала у меня, может быть, тебе пригодится ключ от моей комнаты?"
        else:
            ch_r "Я тут подумала, ты уже много раз ночевал у меня, может быть, тебе пригодится ключ от моей комнаты?"
        ch_p "Спасибо."
        $ RogueX.ArmPose = 1
        $ Keys.append(RogueX) if RogueX not in Keys else Keys
        $ RogueX.Event[0] = 1
        return
# end Event Rogue_Key /////////////////////////////////////////////////////

# start Rogue_BF//////////////////////////////////////////////////////////
label Rogue_BF:

    if RogueX in Player.Harem:
            #if she somehow already ended up in the harem
            if "RogueYes" in Player.Traits:
                    $ Player.Traits.remove("RogueYes")
            if "boyfriend" not in RogueX.Petnames:
                    $ RogueX.Petnames.append("boyfriend")
            $ Event_Queue = [0,0]
            return

    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(RogueX,"bemused","краснеет. . .")
            return
    call Shift_Focus(RogueX)
    $ Player.AddWord(1,"interruption") #adds to Recent
    $ RogueX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    if RogueX.Loc != bg_current and RogueX not in Party:
        "Внезапно перед вами появляется [RogueX.Name] с явным желанием поговорить."

    $ Event_Queue = [0,0]
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.DailyActions.append("relationship")
    if not Player.Male and "girltalk" not in RogueX.History:
            call expression RogueX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
            return

    $ RogueX.FaceChange("bemused", 1)
    ch_r "Итак, [RogueX.Petname], мы уже довольно хорошо знаем друг друга."
    ch_r ". . ."
    $ RogueX.Eyes = "sexy"
    if not Player.Male:
        ch_r "Согласна?"
    else:
        ch_r "Согласен?"
    menu:
        extend ""
        "Ага, и это замечательно":
            $ RogueX.Statup("Love", 200, 20)
        "Ну да, пожалуй":
            $ RogueX.Statup("Love", 200, 10)
        "Эм, дааа?":
            $ RogueX.Statup("Love", 200, -10)
            $ RogueX.Statup("Obed", 200, 30)
    if RogueX.SEXP >= 10:
            ch_r "И мы кое-чем уже занимались. . ."
    if RogueX.SEXP >= 15:
            ch_r "Всякими {i}интимными{/i} штучками. . ."

    if len(Player.Harem) >= 2:
            ch_r "Я знаю, что ты уже какое-то время встречаешься с другими девушками, но мы поговорили и. . ."
    elif Player.Harem:
            ch_r "Я знаю, что тебе далеко не безразлична [Player.Harem[0].Name], но мы с ней поговорили и. . ."

    if not RogueX.Event[5]:
            ch_r "Да, поэтому я подумала. . ."
            ch_r "У меня ведь никогда раньше небыло настоящих отношений, ибо я не могла ни к кому прикасаться."
            ch_r "Это все для меня в новинку, но я хочу попробовать."
            if not Player.Male:
                ch_r "Давай закрепим наши отношения, ты согласишься стать моей девушкой?"
            else:
                ch_r "Давай закрепим наши отношения, ты согласишься стать моим парнем?"
    elif Player.Harem:
            ch_r "Я бы тоже хотела стать твоей девушкой."
    else:
            if not Player.Male:
                ch_r "Иногда ты, конечно, бываешь настоящей стервой, но. . . для меня это не так важно."
            else:
                ch_r "Иногда ты, конечно, бываешь настоящим засранцем, но. . . для меня это не так важно."
            ch_r "Думаю, я бы хотела стать твоей девушкой. . . "
    $ RogueX.Event[5] += 1
    menu:
        extend ""
        "С радостью!":
                $ RogueX.Statup("Love", 200, 30)
                "[RogueX.Name] подпрыгивает и страстно целует вас."
                $ RogueX.FaceChange("kiss")
                $ RogueX.Kissed += 1
        "Эм, ну ладно.":
                $ RogueX.Brows = "confused"
                "[RogueX.Name] немного ошарашена вашей реакцией, но воспринимает ваш ответ, как согласие и обнимает вас."

        "Я уже в отношениях." if Player.Harem:
                $ RogueX.FaceChange("sad",1)
                ch_r "Я знаю. . . знаю. Я просто подумала, может, ты сможешь встречаться и со мной?"
                menu:
                    extend ""
                    "Конечно.":
                            $ RogueX.Statup("Love", 200, 30)
                            "[RogueX.Name] подпрыгивает и страстно целует вас."
                            $ RogueX.FaceChange("kiss")
                            $ RogueX.Kissed += 1
                    "Она этого не поймет." if len(Player.Harem) == 1:
                            $ Line = "no."
                    "Им это не понравится." if len(Player.Harem) > 1:
                            $ Line = "no."
                    "Извини, но. . . нет." if RogueX.Event[5] != 20:
                            $ Line = "no."
                    "Ни за что.":
                            jump Rogue_BF_Jerk
                if Line == "no":
                            $ RogueX.Statup("Love", 200, -10)
                            ch_r "Я поняла. Все в порядке."
                            $ RogueX.Event[5] = 20
                            call Remove_Girl(RogueX)
                            $ Line = 0
                            return
        "Мне как-то этого не хочется.":
                jump Rogue_BF_Jerk
    $ RogueX.Petnames.append("boyfriend")
    if "Historia" not in Player.Traits:
            $ Player.Harem.append(RogueX)
            if "RogueYes" in Player.Traits:
                    $ Player.Traits.remove("RogueYes")
    $ RogueX.FaceChange("sexy")
    if not Player.Male:
        ch_r "А теперь. . . моя девушка. . . как бы ты хотела отпраздновать это событие?"
    else:
        ch_r "А теперь. . . мой парень. . . как бы ты хотел отпраздновать это событие?"
    if "Historia" in Player.Traits:
        return 1
    $ Tempmod = 10
    call SexMenu
    $ Tempmod = 0
    return

label Rogue_BF_Jerk:
    $ RogueX.FaceChange("angry", 1)
    ch_r "Ну и ладно!"
    $ Count = (20* RogueX.Event[5])
    $ RogueX.Statup("Obed", 50, 40)
    if RogueX.Event[5] != 20:
            $ RogueX.Statup("Obed", 200, (20* RogueX.Event[5]))
    if 20 > RogueX.Event[5] >= 3:
            $ RogueX.FaceChange("sad")
            ch_r "Пфф. Меня не волнует, чего ты хочешь, мы будем встречаться. Смирись."
            ch_r "А теперь мне нужно побыть одной."
            if "Historia" in Player.Traits:
                return 1
            $ RogueX.Petnames.append("boyfriend")
            $ Achievements.append("I am not your Boyfriend!")
            $ bg_current = "bg player"
            call Remove_Girl(RogueX)
            call Set_The_Scene
            return
    if 1 <  RogueX.Event[5] < 20:
            if not Player.Male:
                ch_r "Я не знаю, почему я постоянно спрашиваю. Мне следовало бы знать, что ты не изменилась."
            else:
                ch_r "Я не знаю, почему я постоянно спрашиваю. Мне следовало бы знать, что ты не изменился."
            $ RogueX.Statup("Love", 200, -(50* RogueX.Event[5]))
    else:
            $ RogueX.Statup("Love", 200, -50)

    if bg_current == RogueX.Home:
            if not Player.Male:
                ch_r "Убирайся! Дура!"
            else:
                ch_r "Придурок! Убирайся!"
    else:
            "[RogueX.Name] убегает."
    if "Historia" in Player.Traits:
        return 1
    $ RogueX.Loc = "bg rogue"
    $ bg_current = "bg player"
    call Remove_Girl(RogueX)
    call Set_The_Scene
    jump Misplaced

# end Rogue_BF//////////////////////////////////////////////////////////

# start Rogue_Love//////////////////////////////////////////////////////////
label Rogue_Love:
    call Shift_Focus(RogueX)
    $ RogueX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")

    if bg_current != "bg rogue":
        if RogueX.Loc == bg_current or RogueX in Party:
            "Вдруг [RogueX.Name] изъявляет желание поговорить с вами в своей комнате и отводит вас туда."
        else:
            "[RogueX.Name] появляется словно из ниоткуда и изъявляет желание поговорить с вами в своей комнате, а затем отводит вас туда."
    else:
            "[RogueX.Name] внезапно начинает пристально смотреть на вас."

    $ Player.AddWord(1,"interruption") #adds to Recent
    $ Event_Queue = [0,0]
    $ bg_current = "bg rogue"
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.DailyActions.append("relationship")
    $ RogueX.FaceChange("bemused", 1)
    if RogueX in Player.Harem:
            if not Player.Male:
                ch_r "Мы уже какое-то время встречаемся, и ты стала мне очень дорога."
            else:
                ch_r "Мы уже какое-то время встречаемся, и ты стал мне очень дорог."
    else:
            if not Player.Male:
                ch_r "Мы уже давно общаемся, и ты стала мне очень дорога."
            else:
                ch_r "Мы уже давно общаемся, и ты стал мне очень дорог."
    ch_r ". . ."
    $ RogueX.Eyes = "sexy"
    menu:
        ch_r "Ты ведь понимаешь, о чем я?"
        "Я люблю тебя, [RogueX.Name].":
                $ RogueX.Statup("Love", 200, 50)
                $ RogueX.Event[6] = 10
        "Ага, и это замечательно.":
                $ RogueX.Statup("Love", 200, 20)
        "Наверное, да.":
                $ RogueX.Statup("Love", 200, 10)
        "Эм, дааа?":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)
    if not RogueX.Event[6]:
            ch_r "Так вот, я тут подумала и. . ."
            ch_r "Я люблю тебя."
    elif RogueX.Event[6] == 10:
            $ RogueX.FaceChange("confused")
            ch_r "Так вот. . . подожди, что?"
            $ RogueX.FaceChange("smile",2)
            $RogueX.Brows = "surprised"
            ch_r "Я тоже тебя люблю!"
            $ RogueX.FaceChange("kiss")
            "В мгновение ока [RogueX.Name] обнимает вас и начинает целовать."
            $ RogueX.FaceChange("sexy",1)
            $ RogueX.Kissed += 1
    else:
            ch_r "Даже учитывая, что у нас бывают разногласия. . ."
            ch_r "Я все равно люблю тебя."
    $ RogueX.Event[6] += 1
    if RogueX.Event[6] < 10:
        menu:
            extend ""
            "Я тоже тебя люблю.":
                    $ RogueX.Statup("Love", 200, 50)
                    "[RogueX.Name] падает в ваши объятия."
            "Это же отлично!":
                    $ RogueX.Brows = "confused"
                    "[RogueX.Name] выглядит немного растерянной, но воспринимает это как положительный знак и обнимает вас."
            "Я знаю.":
                    $ RogueX.FaceChange("smile")
                    $ RogueX.Brows = "confused"
                    "[RogueX.Name] бьет вас по руке, а затем крепко обнимает."
            "И?":
                    jump Rogue_Love_Jerk
            "Не могу ответить тебе взаимностью.":
                    $ RogueX.Statup("Love", 200, -50)
                    $ RogueX.Statup("Obed", 200, 50)
                    jump Rogue_Love_Jerk
    $ RogueX.FaceChange("bemused",1,Eyes="side")
    $ RogueX.Petnames.append("lover")
    call Rogue_AnnaMarie        #plays new name dialog
    ch_r "В общем, я рада, что смогла поделиться этим с тобой."
    $ RogueX.FaceChange("sly")
    ch_r "Я бы хотела поделиться с тобой гораздо большим, если смогу. . ."
    if not RogueX.Sex:
        $ RogueX.Statup("Obed", 70, 10)
        if not Player.Male:
            ch_r "Итак. . . ты бы хотела. . . закрепить наши отношения?"
        else:
            ch_r "Итак. . . ты бы хотел. . . закрепить наши отношения?"
        menu:
            extend ""
            "Ага. . . [[заняться сексом]":
                    $ RogueX.Statup("Inbt", 30, 30)
                    ch_r "Ммм. . ."
                    if "Historia" in Player.Traits:
                        return 1
                    call SexAct("sex") # call Rogue_SexAct("sex")
                    jump Rogue_Room
            "У меня есть пара других идей. . .[[выбрать другое занятие]":
                    $ RogueX.Brows = "confused"
                    $ RogueX.Statup("Obed", 70, 20)
                    ch_r "Что ж, теперь мне интересно узнать, что у тебя на уме. . ."
            "Эм, пожалуй, нет. [[ничего не делать]":
                    $ RogueX.Statup("Love", 200, -10)
                    $ RogueX.Statup("Obed", 70, 40)
                    $ RogueX.FaceChange("perplexed",1)
                    ch_r "Ну ладно?"
                    ch_r "{size=-5}Что это, черт возьми, было?{/size}"          #fix test this
                    jump Rogue_Room
    else:
            if not Player.Male:
                ch_r "Ну а теперь, любимая. . . может, ты как-то хочешь это отпраздновать?"
            else:
                ch_r "Ну а теперь, любимый. . . может, ты как-то хочешь это отпраздновать?"
    if "Historia" in Player.Traits:
            return 1
    if "stockings and garterbelt" not in RogueX.Inventory:
            $ RogueX.Inventory.append("stockings and garterbelt")
    $ Tempmod = 20
    call SexMenu
    $ Tempmod = 0
    jump Rogue_Room

label Rogue_Love_Jerk:
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()
    $ RogueX.FaceChange("angry", 1)
    ch_r "Ну и ладно!"
    $ Count = (20* RogueX.Event[6])
    $ RogueX.Statup("Obed", 50, 40)
    $ RogueX.Statup("Obed", 200, Count)
    if RogueX.Event[6] == 3:
            $ RogueX.FaceChange("sad")
            ch_r "Меня. . . Меня это не волнует, я все равно очень сильно тебя люблю."
            ch_r "Но мне нужно немного побыть одной."
            if "Historia" in Player.Traits:
                    return 1
            $ RogueX.Petnames.append("lover")
            $ Achievements.append("One Sided Love")
            $ RogueX.Loc = "bg rogue"
            $ bg_current = "bg player"
            call Remove_Girl(RogueX)
            jump Player_Room
    if RogueX.Event[6] > 1:
            if not Player.Male:
                ch_r "И не стыдно тебе меня дурачить? Я думала ты повзрослела."
            else:
                ch_r "И не стыдно тебе меня дурачить? Я думала ты повзрослел."
    ch_r "Если ты больше ничего не хочешь мне сказать, убирайся!"
    $ Count = (100* RogueX.Event[6])
    $ RogueX.Statup("Love", 200, -Count)
    if "Historia" in Player.Traits:
            return 0
    $ RogueX.Loc = "bg rogue"
    $ bg_current = "bg player"
    call Remove_Girl(RogueX)
    jump Player_Room

label Rogue_AnnaMarie:
    call Shift_Focus(RogueX)
    ch_r "Думаю, тебе стоит знать, что при рождении у меня было другое имя, не \"Роуг.\""
    ch_r ". . ."
    $ RogueX.FaceChange("bemused",1)
    ch_r "В детстве меня звали \"Анна-Мария.\""
    $ RogueX.Names.append("Anna-Marie")
    $ RogueX.Names.append("Anna")
    $ RogueX.Names.append("Marie")
    menu:
        extend ""
        "Какое прекрасное имя.":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Statup("Obed", 50, 5)
                $ RogueX.Statup("Inbt", 70, 5)
                $ RogueX.FaceChange("smile",2)
                ch_r "Ох, большое спасибо. . ."
        "Хм, ладно.":
                $ RogueX.Statup("Obed", 80, 5)
                $ RogueX.FaceChange("confused",1)
                ch_r "Эм. . . ага."
        "Мне оно не нравится.":
                $ RogueX.Statup("Love", 200, -5)
                $ RogueX.Statup("Obed", 200, 10)
                $ RogueX.Statup("Inbt", 200, -5)
                $ RogueX.FaceChange("angry",1)
                ch_r "Ох. . . ладно. . ."
    menu:
        extend ""
        "Мне кажется, что \"Роуг\" подходит тебе больше.":
                $ RogueX.Name = "Роуг"
                $ RogueX.Name_rod = "Роуг"
                $ RogueX.Name_dat = "Роуг"
                $ RogueX.Name_vin = "Роуг"
                $ RogueX.Name_tvo = "Роуг"
                $ RogueX.Name_pre = "Роуг"
                $ RogueX.FaceChange("smile")
                ch_r "Ага, я уже привыкла к нему."
        "Слушай, а хорошо звучит. \"Анна-Мария.\"":
                $ RogueX.Name = "Анна-Мария"
                $ RogueX.Name_rod = "Анны-Марии"
                $ RogueX.Name_dat = "Анне-Марии"
                $ RogueX.Name_vin = "Анну-Марию"
                $ RogueX.Name_tvo = "Анной-Марией"
                $ RogueX.Name_pre = "Анне-Марии"
                $ RogueX.FaceChange("smile")
                ch_r "Было бы прикольно, снова вернуться к нему. . ."
        "\"Мария\", думаю, идеально тебе подходит.":
                $ RogueX.Name = "Мария"
                $ RogueX.Name_rod = "Марии"
                $ RogueX.Name_dat = "Марии"
                $ RogueX.Name_vin = "Марию"
                $ RogueX.Name_tvo = "Марией"
                $ RogueX.Name_pre = "Марии"
                $ RogueX.FaceChange("smile")
                ch_r "Ты правда так думаешь?"
        "\"Анна\" звучит неплохо.":
                $ RogueX.Name = "Анна"
                $ RogueX.Name_rod = "Анны"
                $ RogueX.Name_dat = "Анне"
                $ RogueX.Name_vin = "Анну"
                $ RogueX.Name_tvo = "Анной"
                $ RogueX.Name_pre = "Анне"
                $ RogueX.FaceChange("smile")
                if not Player.Male:
                    ch_r "Наверное, ты права. . ."
                else:
                    ch_r "Наверное, ты прав. . ."
    return
# end Rogue_Love//////////////////////////////////////////////////////////


# start Rogue_Sub//////////////////////////////////////////////////////////
label Rogue_Sub:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(RogueX,"bemused","кажется тихой. . .")
            return
    call Shift_Focus(RogueX)
    $ RogueX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    if RogueX.Loc != bg_current and RogueX not in Party:
            "Внезапно перед вами появляется [RogueX.Name] с явным желанием поговорить."

    $ Player.AddWord(1,"interruption") #adds to Recent
    $ RogueX.Loc = bg_current
    $ Event_Queue = [0,0]
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.DailyActions.append("relationship")
    if not Player.Male and "girltalk" not in RogueX.History:
            call expression RogueX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
            return
    $ RogueX.FaceChange("bemused", 1)
    ch_r ". . ."
    if RogueX in Player.Harem:
            ch_r "Мы уже какое-то время встречаемся."
    else:
            ch_r "Мы уже давненько проводим время вместе."
    if RogueX.FondleB or RogueX.FondleP or RogueX.FondleA:
            ch_r "Я позволила тебе касаться меня. . ."
    if RogueX.Hand or RogueX.Blow:
            ch_r "Я касалась тебя. . ."
    if RogueX.Love >= 900 and (RogueX in Player.Harem):
            ch_r "И я очень тебя люблю. . ."
    elif RogueX.Love >= 800:
            if not Player.Male:
                ch_r "И ты мне очень дорога."
            else:
                ch_r "И ты мне очень дорог."
    elif RogueX.Love >= 500:
            ch_r "Хотя у нас и бывают разногласия, но. . . мы справляемся с ними, я ведь права?"
    else:
            $ RogueX.Brows = "angry"
            ch_r "Хотя ты мне не особо нравишься, но что-то в тебе. . ."
            ch_r "притягивает меня."
    menu:
        extend ""
        "Ага, и это здорово.":
                $ RogueX.Statup("Love", 200, 20)
        "Ага.":
                $ RogueX.Statup("Love", 200, 10)
        "Эм, дааа?":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)
    if not RogueX.Event[7]:
            ch_r "Так вот, я тут подумала. . ."
            $ RogueX.Eyes = "sexy"
            ch_r "Я хотела бы придать небольшой . . . структурированности своей жизни."
    else:
            if not Player.Male:
                ch_r "Я хотела бы , чтобы ты еще раз подумала над тем предложением. . ."
            else:
                ch_r "Я хотела бы , чтобы ты еще раз подумал над тем предложением. . ."
            ch_r "сделать мою жизнь более. . . структурированной."
    $ RogueX.History.append("sir")
    $ RogueX.Event[7] += 1
    menu:
        extend ""
        "Ага, звучит интересно.":
                $ RogueX.Statup("Obed", 200, 100)
                $ RogueX.Petnames.append("sir")
                "[RogueX.Name] послушно кивает."
        "Что ты хочешь этим сказать?":
                $ RogueX.FaceChange("bemused")
                ch_r "Когда ты. . . побуждаешь меня пробовать что-то новое, это очень заводит."
                if not Player.Male:
                    ch_r "Я бы хотела, чтобы ты и дальше продолжала. . . побуждать меня."
                    ch_r "Точнее, я бы хотела, чтобы ты отдавала мне приказы, а я бы старалась их выполнять."
                else:
                    ch_r "Я бы хотела, чтобы ты и дальше продолжал. . . побуждать меня."
                    ch_r "Точнее, я бы хотела, чтобы ты отдавал мне приказы, а я бы старалась их выполнять."
                menu:
                    extend ""
                    "Ладно, звучит интересно.":
                            $ RogueX.Statup("Obed", 200, 100)
                            "[RogueX.Name] послушно кивает."
                    "Ох, ну ладно.":
                            "[RogueX.Name] немного расстраивается от такого ответа, но все равно принимает его положительно и кивает."
                    "Нет, спасибо. Не хочу в этом учавствовать.":
                            jump Rogue_Sub_Jerk
                $ RogueX.Petnames.append("sir")
        "Нет, меня это не касается.":
                jump Rogue_Sub_Jerk
    $ RogueX.FaceChange("sexy")
    if not Player.Male:
        ch_r "А теперь, госпожа. . . не желаешь немного отпраздновать?"
    else:
        ch_r "А теперь, господин. . . не желаешь немного отпраздновать?"
    if "Historia" in Player.Traits:
            return 1
    if "stockings and garterbelt" not in RogueX.Inventory:
            $ RogueX.Inventory.append("stockings and garterbelt")
    $ Tempmod = 10
    call SexMenu
    $ Tempmod = 0
    return

label Rogue_Sub_Jerk:
    $ RogueX.FaceChange("sad", 1)
    ch_r "Пфф!"
    $ Count = (20* RogueX.Event[7])
    $ RogueX.Statup("Inbt", 50, 30)
    $ RogueX.Statup("Inbt", 200, Count)
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()
    if RogueX.Event[7] == 2:
            $ RogueX.FaceChange("sad")
            ch_r "Мне нужно немного побыть одной."
            if "Historia" in Player.Traits:
                    return
            $ RogueX.Petnames.append("sir")
            $ Achievements.append("Nosiree")
            $ bg_current = "bg player"
            $ RogueX.Loc = "bg rogue"
            call Remove_Girl(RogueX)
            jump Player_Room
    if RogueX.Event[7] > 1:
            if not Player.Male:
                ch_r "А я то думала, что ты научилась уважать мои желания."
            else:
                ch_r "А я то думала, что ты научился уважать мои желания."
    ch_r "Если таков твой окончательный ответ, то я бы хотела побыть в одиночестве."
    $ Count = (20* RogueX.Event[7])
    $ RogueX.Statup("Obed", 200, -Count)
    if "Historia" in Player.Traits:
            return
    $ RogueX.Loc = "bg rogue"
    $ bg_current = "bg player"
    call Remove_Girl(RogueX)
    jump Player_Room

# end Rogue_Sub//////////////////////////////////////////////////////////


# start Rogue_Master//////////////////////////////////////////////////////////
label Rogue_Master:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(RogueX,"bemused","кажется необычайно покорной. . .")
            return
    call Shift_Focus(RogueX)
    $ RogueX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    if RogueX.Loc != bg_current and RogueX not in Party:
            "Внезапно перед вами появляется [RogueX.Name] с явным желанием поговорить."

    $ Event_Queue = [0,0]
    $ Player.AddWord(1,"interruption") #adds to Recent
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.DailyActions.append("relationship")
    $ RogueX.FaceChange("bemused", 1)
    ch_r ". . ."

    if RogueX in Player.Harem:
            ch_r "Знаешь, между нами образовалась ситуация, которая. . . добавила остринки нашим отношениям."
    else:
            ch_r "Знаешь, между нами образовались довольно. . . интересные отношения."
    if RogueX.Anal or RogueX.DildoA:
            ch_r "М мы даже игрались с моей попкой разными штучками."
    if RogueX.Love >= 900 and (RogueX in Player.Harem):
            ch_r "И я предана тебе. . ."
    elif RogueX.Love >= 800:
            ch_r "И ты очень много значишь для меня."
    elif RogueX.Love >= 500:
            ch_r "И я не могу без тебя."
    else:
            $ RogueX.Brows = "angry"
            ch_r "Хотя я терпеть не могу быть с тобой, но в то же время и без тебя мне невыносимо."
    menu:
        ch_r "Скажи, я радовала тебя, [RogueX.Petname]?"
        "Конечно.":
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.Statup("Obed", 200, 20)
        "Пожалуй.":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Statup("Obed", 200, 20)
        "Не особо.":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)
    if not RogueX.Event[8]:
                ch_r "Учитывая все это. . ."
                if not Player.Male:
                    ch_r "Я бы хотела, чтобы ты стала моим хозяином."
                else:
                    ch_r "Думаю, я хотела бы, чтобы ты стал моим хозяином."
    else:
                if not Player.Male:
                    ch_r "Я бы хотела, чтобы ты еще раз подумала над моим предложением. . ."
                    ch_r "пожалуйста, стань моим хозяином."
                else:
                    ch_r "Я бы хотела, чтобы ты еще раз подумал над моим предложением. . ."
                    ch_r "пожалуйста, стань моим хозяином."
    if not Player.Male:
                ch_r "Ну, или. . . \"хозяйков\", так, наверное, лучше звучит. . ."
    $ RogueX.Event[8] += 1
    $ RogueX.History.append("master")
    menu:
        extend ""
        "Хорошо.":
                $ RogueX.Statup("Obed", 200, 100)
                $ RogueX.Petnames.append("master")
                "[RogueX.Name] покорно кивает."
        "Что ты имеешь в виду?":
                $RogueX.Brows = "confused"
                ch_r "Ну, когда ты мне говоришь что-либо сделать. . ."
                $ RogueX.FaceChange("bemused", 1)
                ch_r "Я дико возбуждаюсь."
                if not Player.Male:
                    ch_r "Мне прямо необходимо, чтобы ты говорила мне, что делать."
                else:
                    ch_r "Мне прямо необходимо, чтобы ты говорил мне, что делать."
                menu:
                    ch_r "Я буду в точности следовать твоим указаниям до тех пор, пока могу."
                    "Ох, ну хорошо.":
                            "[RogueX.Name] покорно кивает."
                            $ RogueX.Petnames.append("master")
                    "Ты должна сама решать, что тебе делать. Не нужно, чтобы тебе указывали.":
                            $RogueX.Brows = "confused"
                            ch_r "Меня устроит такой ответ. . ."
                            $ RogueX.Statup("Inbt", 50, 100)
                            $ RogueX.Statup("Inbt", 90, 50)
                            ch_r "По крайней мере, пока. . ."
                            $ RogueX.Statup("Obed", 200, -200)
                            $ RogueX.Event[8] = 3
                    "Нее, это слишком сложно.":
                            jump Rogue_Obed_Jerk
        "Нет, я в этом не учавствую.":
                jump Rogue_Obed_Jerk
    $ RogueX.FaceChange("sexy")
    if not Player.Male:
        ch_r "А теперь, хозяйка. . . не хочешь это как-нибудь отпраздноват?"
    else:
        ch_r "А теперь, хозяин. . . не хочешь это как-нибудь отпраздноват?"
    if "Historia" in Player.Traits:
            return 1
    $ Tempmod = 20
    call SexMenu
    $ Tempmod = 0
    return

label Rogue_Obed_Jerk:
    $ RogueX.FaceChange("sad", 1)
    ch_r "Ну и ладно!"
    $ Count = (20* RogueX.Event[8])
    $ RogueX.Statup("Inbt", 50, 30)
    $ RogueX.Statup("Inbt", 200, Count)
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()
    if RogueX.Event[8] == 2:
            $ RogueX.FaceChange("sad")
            if not Player.Male:
                ch_r "Мне все равно, что ты говоришь, мне нужна. ХОЗЯЙКА."
            else:
                ch_r "Мне все равно, что ты говоришь, мне нужен. ХОЗЯИН."
            ch_r "Но сейчас мне нужно немного побыть одной."
            if "Historia" in Player.Traits:
                    return
            $ RogueX.Petnames.append("master")
            $ Achievements.append("Heavy is the Head")
            $ bg_current = "bg player"
            $ RogueX.Loc = "bg rogue"
            call Remove_Girl(RogueX)
            jump Player_Room
    if RogueX.Event[8] > 1:
            if not Player.Male:
                ch_r "А я то думала, что ты научилась уважать мои желания."
            else:
                ch_r "А я то думала, что ты научился уважать мои желания."
    ch_r "Если это твой окончательный ответ, то я бы хотела побыть в одиночестве."
    $ Count = (50* RogueX.Event[8])
    $ RogueX.Statup("Obed", 200, -Count)
    if "Historia" in Player.Traits:
        return
    $ RogueX.Loc = "bg rogue"
    $ bg_current = "bg player"
    call Remove_Girl(RogueX)
    jump Player_Room

# end Rogue_Slave//////////////////////////////////////////////////////////


# start Rogue_Sexfriend//////////////////////////////////////////////////////////
label Rogue_Sexfriend:
    call Shift_Focus(RogueX)
    $ Event_Queue = [0,0]
    $ RogueX.DailyActions.append("relationship")
    if RogueX in Player.Harem and (RogueX.Loc == bg_current or RogueX in Party):
            $ RogueX.DrainWord("asked meet")
            $ Player.DrainWord("meet girl")
            if "stockings and garterbelt" not in RogueX.Inventory:
                    $ RogueX.Inventory.append("stockings and garterbelt")
            $ RogueX.Petnames.append("sex friend")
            $ RogueX.Statup("Inbt", 200, 50)
#            if RogueX.Loc != bg_current and RogueX not in Party:
#                    return
            call Set_The_Scene(0)
            call Display_Girl(RogueX)
            "[RogueX.Name] слегка сжимает вашу задницу."
            return

    call Shift_Focus(RogueX)
    $ RogueX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    if RogueX.Loc != bg_current and RogueX not in Party:
        "Внезапно перед вами появляется [RogueX.Name] с явным желанием поговорить."

    if "stockings and garterbelt" not in RogueX.Inventory:
            $ RogueX.Inventory.append("stockings and garterbelt")
    $ RogueX.Petnames.append("sex friend")
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level

    if not Player.Male and "girltalk" not in RogueX.History:
            call expression RogueX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
    $ RogueX.FaceChange("smile", 1)
    ch_r ". . ."
    ch_r "Нам ведь было весело, правда?"
    if RogueX.SEXP >= 40:
            ch_r "Я про то, что мы занимались многими безумными вещами."
    if "ex" in RogueX.Traits:
            ch_r "И мы какое-то время встречались. . ."
    else:
            ch_r "Я, конечно, понимаю, что мы не \"встречались\", но. . ."
            menu:
                ch_r "Но разве мы не проводили весело время вместе?"
                "Ага, это было круто.":
                        $ RogueX.Statup("Love", 200, 20)
                        $ RogueX.Statup("Inbt", 200, 20)
                "Эммм. . . да?":
                        $ RogueX.Statup("Inbt", 200, 20)
                "Может быть. . .":
                        $ RogueX.Statup("Love", 200, -10)
                        $ RogueX.Statup("Obed", 200, 30)
    if RogueX in Player.Harem:
        ch_r "Я бы хотела -гораздо- больше секса. . ."
    elif not RogueX.Event[9]:
        ch_r "Хорошо, раз уж мы так весело проводим время. . ."
        if "ex" in RogueX.Traits:
                ch_r "Хоть мы уже и не встречаемся, но я бы все равно хотела проводить еще больше времени с тобой \"наедине\"."
        else:
                ch_r "Думаю, что готова стать твоей любовницей."
    else:
        if not Player.Male:
            ch_r "Я бы хотела, чтобы ты пересмотрела мое щедрое предложение. . ."
        else:
            ch_r "Я бы хотела, чтобы ты пересмотрел мое щедрое предложение. . ."
        ch_r "давай, станем любовниками? А?"
    $ RogueX.Event[9] += 1
    if RogueX not in Player.Harem:
            menu:
                extend ""
                "Звучит заманчиво!":
                        $ RogueX.Statup("Inbt", 200, 100)
                        $ RogueX.Petnames.append("sex friend")
                        "[RogueX.Name] послушно кивает."
                "Что ты имеешь в виду?":
                        $RogueX.Brows = "confused"
                        ch_r "Ну, знаешь, просто секс, без каких-либо обязательств, по крайней мере пока."
                        menu:
                            ch_r "Что скажешь?"
                            "Ну ладно.":
                                    "[RogueX.Name] послушно кивает."
                            "Нет, спасибо. Такое меня не интересует.":
                                    jump Rogue_Sexfriend_Jerk
                "Нет, я пас.":
                        jump Rogue_Sexfriend_Jerk
            $ RogueX.FaceChange("sexy")
            if not Player.Male:
                ch_r "А теперь, любовник. . . может, ты хочешь это как-то отпраздновать?"
            else:
                ch_r "А теперь, любовница. . . может, ты хочешь это как-то отпраздновать?"
            if "Historia" in Player.Traits:
                    return 1
    $ Player.AddWord(1,"interruption") #adds to Recent
    $ Tempmod = 25
    call SexMenu
    $ Tempmod = 0
    return

label Rogue_Sexfriend_Jerk:
    $ RogueX.FaceChange("sad", 1)
    $ RogueX.DailyActions.append("relationship")
    ch_r "Многое теряешь."
    $ RogueX.Statup("Obed", 50, 30)
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()
    if RogueX.Event[9] == 3:
            ch_r "Ну, это все равно не только тебе решать."
            ch_r "Дай мне знать, если захочешь покувыркаться."
            ch_r "А теперь мне нужно побыть одной."
            if "Historia" in Player.Traits:
                    return
            $ RogueX.Petnames.append("sex friend")
            $ Achievements.append("Man of Virtue")
            $ bg_current = "bg player"
            $ RogueX.Loc = "bg rogue"
            call Remove_Girl(RogueX)
            jump Player_Room
    $ Count = (10 * RogueX.Event[9])
    $ RogueX.Statup("Inbt", 200, -Count)
    if bg_current == "bg rogue":
            ch_r "Хорошо, теперь ты можешь идти."
            $ bg_current = "bg player"
    else:
            ch_r "Хорошо, я пошла."
            $ RogueX.Loc = "bg rogue"
    if "Historia" in Player.Traits:
            return
    call Remove_Girl(RogueX)
    jump Player_Room

# end Rogue_Sexfriend//////////////////////////////////////////////////////////


# start Rogue_Fuckbuddy//////////////////////////////////////////////////////////
label Rogue_Fuckbuddy:
    call Shift_Focus(RogueX)
    $ RogueX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    if RogueX in Player.Harem:
            $ Event_Queue = [0,0]
            if RogueX.Loc != bg_current and RogueX not in Party:
                    return
            $ RogueX.Petnames.append("fuck buddy")
            $ RogueX.Statup("Inbt", 200, 50)
            call Set_The_Scene(0)
            call Display_Girl(RogueX)
            "[RogueX.Name] резко наклоняется и слегка сжимает ваш пах."
            return

    if RogueX.Loc != bg_current and RogueX not in Party:
            "Внезапно перед вами появляется [RogueX.Name] с явным желанием поговорить."

    $ Event_Queue = [0,0]
    $ RogueX.Loc = bg_current
    call Shift_Focus(RogueX)
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.FaceChange("bemused", 1)
    ch_r ". . ."
    ch_r "Мне было очень весело быть твоей \"любовницей\"."
    if "exhibitionist" in RogueX.Traits:
            ch_r "Я получила огромное удовольствие от всего, чем мы занимались."
    menu:
        extend ""
        "Еще бы!":
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.Statup("Obed", 200, 20)
                $ RogueX.Statup("Inbt", 200, 30)
        "Да?":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Statup("Obed", 200, 20)
        "Мне все равно.":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)
    ch_r "Так вот, раз уж между нами все было хорошо. . ."
    $ RogueX.Event[10] += 1
    $ RogueX.Petnames.append("fuck buddy")
    if RogueX not in Player.Harem:
            ch_r "Я бы хотела, чтобы мы стали полноценными секс-партнерами."
            menu:
                extend ""
                "Хех, ладно.":
                        $ RogueX.Statup("Inbt", 200, 100)
                        $ RogueX.Petnames.append("fuck buddy")
                        $ RogueX.ArmPose = 2
                        ch_r "Ура!"
                        $ RogueX.Over = 0
                        $ RogueX.Chest = 0
                        if "Historia" in Player.Traits:
                                    return 1
                        call Girl_First_Topless(RogueX,1)
                        call Girl_Breasts_Launch(RogueX,0)#call Rogue_Breasts_Launch
                        "[RogueX.Name] раздевается по пояс, сближается с вами и засовывает вашу голову себе между сисек."
                        call Girl_Pos_Reset(RogueX) #call Girl_Pos_Reset(RogueX)
                "Что ты имеешь в виду?":
                    $RogueX.Brows = "confused"
                    menu:
                        ch_r "Ну знаешь, мы будем хорошими друзьями и будем часто трахаться."
                        "Ну ладно.":
                                call Girl_Kissing_Launch(RogueX)
                                "[RogueX.Name] заливается смехом и обнимает вас."
                                call Girl_Pos_Reset(RogueX) #call Girl_Pos_Reset(RogueX)
                        "Нее, такое не по мне.":
                                jump Rogue_Fuckbuddy_Jerk
                "Нет, спасибо.":
                    jump Rogue_Fuckbuddy_Jerk
            $ RogueX.FaceChange("sexy")
            if not Player.Male:
                ch_r "А теперь, -хех-, секс-партнерша. . . давай закрепим наши отношения!"
            else:
                ch_r "А теперь, -хех-, секс-партнер. . . давай закрепим наши отношения!"
    if "Historia" in Player.Traits:
            return 1
    $ Tempmod = 30
    $ Player.AddWord(1,"interruption") #adds to Recent
    call SexMenu
    $ Tempmod = 0
    return

label Rogue_Fuckbuddy_Jerk:
    $ RogueX.Statup("Obed", 50, 30)
    $ RogueX.FaceChange("bemused", 1)
    if RogueX.Event[10] > 1:
            $ RogueX.ArmPose = 2
            $ RogueX.Over = 0
            $ RogueX.Chest = 0
            ch_r "Блин, я тебе предлагаю ТАКОЕ, а ты отказываешься. . .!"
            $ RogueX.OutfitChange()
            ch_r "Слушай, мне наплевать, как ты будешь это называть. Просто дай мне знать, если захочешь потрахаться."
            if "Historia" in Player.Traits:
                    return 1
            call Girl_First_Topless(RogueX,1)
            $ RogueX.Petnames.append("fuck buddy")
            $ Achievements.append("Stalwart as the mount")
            return
    else:
            ch_r "Паршиво."
    if "Historia" in Player.Traits:
            return
    $ renpy.pop_call()
    $ Count = (10*RogueX.Event[10])
    $ RogueX.Statup("Inbt", 200, -Count)
    if bg_current == "bg rogue":
            ch_r "Ладно, можешь идти."
            $ bg_current = "bg player"
    else:
            ch_r "Ладно, я пошла."
            $ RogueX.Loc = "bg rogue"
    call Remove_Girl(RogueX)
    jump Player_Room
# end Rogue_Fuckbuddy//////////////////////////////////////////////////////////

# start Rogue_Daddy//////////////////////////////////////////////////////////
label Rogue_Daddy:
    $ RogueX.DailyActions.append("relationship")
    $ RogueX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    $ Event_Queue = [0,0]
    call Shift_Focus(RogueX)
    if RogueX.Loc != bg_current:
            $ RogueX.Loc = bg_current
            "[RogueX.Name] подходит к вам."
    call Set_The_Scene
    ch_r ". . ."
    if RogueX in Player.Harem:
            ch_r "Знаешь, несмотря на то, что мы встречаемся,"
    else:
            ch_r "Знаешь, несмотря на то, что мы частенько проводим время вместе,"
    if RogueX.Love > RogueX.Obed and RogueX.Love > RogueX.Inbt:
            if not Player.Male:
                ch_r "и ты очень мила со мной. . ."
            else:
                ch_r "и ты очень мил со мной. . ."
    elif RogueX.Obed > RogueX.Inbt:
            ch_r "и ты знаешь, что мне бывает нужно. . ."
    else:
            ch_r "и я прямо смогла расправить крылья. . ."
    if not Player.Male:
        ch_r "Думаю, я хотела бы звать тебя \"мамочкой.\""
    else:
        ch_r "Думаю, я хотела бы звать тебя \"папочкой.\""
        ch_r "Что ты на это скажешь?"
    menu:
        extend ""
        "Ладно, можешь начинать.":
                $ RogueX.FaceChange("smile")
                $ RogueX.Statup("Love", 90, 20)
                $ RogueX.Statup("Obed", 60, 10)
                $ RogueX.Statup("Inbt", 80, 30)
                ch_r "Ура!"
                if not Player.Male:
                    $ RogueX.Petname = "мамочка"
                    $ RogueX.Petname_rod = "мамочки"
                    $ RogueX.Petname_dat = "мамочке"
                    $ RogueX.Petname_vin = "мамочку"
                    $ RogueX.Petname_tvo = "мамочкой"
                    $ RogueX.Petname_pre = "мамочке"
                else:
                    $ RogueX.Petname = "папочка"
                    $ RogueX.Petname_rod = "папочки"
                    $ RogueX.Petname_dat = "папочке"
                    $ RogueX.Petname_vin = "папочку"
                    $ RogueX.Petname_tvo = "папочкой"
                    $ RogueX.Petname_pre = "папочке"
        "Что ты имеешь в виду?":
                $ RogueX.FaceChange("bemused")
                ch_r "Меня это ужасно заводит и, знаешь, будучи твоей малышкой. . ."
                ch_r "Мне бы очень хотелось так обращаться к тебе."
                menu:
                    extend ""
                    "Звучит интересно, я за.":
                            $ RogueX.FaceChange("smile")
                            $ RogueX.Statup("Love", 90, 15)
                            $ RogueX.Statup("Obed", 60, 20)
                            $ RogueX.Statup("Inbt", 80, 25)
                            if not Player.Male:
                                $ RogueX.Petname = "мамочка"
                                $ RogueX.Petname_rod = "мамочки"
                                $ RogueX.Petname_dat = "мамочке"
                                $ RogueX.Petname_vin = "мамочку"
                                $ RogueX.Petname_tvo = "мамочкой"
                                $ RogueX.Petname_pre = "мамочке"
                            else:
                                $ RogueX.Petname = "папочка"
                                $ RogueX.Petname_rod = "папочки"
                                $ RogueX.Petname_dat = "папочке"
                                $ RogueX.Petname_vin = "папочку"
                                $ RogueX.Petname_tvo = "папочкой"
                                $ RogueX.Petname_pre = "папочке"
                            ch_r "Отлично! . . [RogueX.Petname]."
                    "Можешь так меня не называть, пожалуйста?":
                            $ RogueX.Statup("Love", 90, 5)
                            $ RogueX.Statup("Obed", 80, 40)
                            $ RogueX.Statup("Inbt", 80, 20)
                            $ RogueX.FaceChange("sad")
                            ch_r "   . . .   "
                            ch_r "Ну ладно."
                    "Нет, меня аж в дрожь бросает от этого.":
                            $ RogueX.Statup("Love", 90, -10)
                            $ RogueX.Statup("Obed", 80, 45)
                            $ RogueX.Statup("Inbt", 70, 5)
                            $ RogueX.FaceChange("angry")
                            ch_r "Пфф."
        "Нет, меня это пугает.":
                $ RogueX.Statup("Love", 90, -5)
                $ RogueX.Statup("Obed", 80, 40)
                $ RogueX.Statup("Inbt", 70, 10)
                $ RogueX.FaceChange("angry")
                ch_r "Пфф."
    $ RogueX.Petnames.append("daddy")
    return

# end Rogue_Daddy//////////////////////////////////////////////////////////


label Rogue_Frisky_Class:
        $ Line = 0
        if EmmaX.Loc == "bg teacher":
            "[EmmaX.Name] читает лекцию об отношениях мутантов. Рядом с вами [RogueX.Name] неловко ерзает на стуле."
        elif StormX.Loc == "bg teacher":
            "[StormX.Name] читает лекцию по географии и политике. Рядом с вами [RogueX.Name] неловко ерзает на стуле."
        else:
            "Профессор МакКой читает лекцию о Гене Икс. Рядом с вами [RogueX.Name] неловко ерзает на стуле."
        "Время от времени вы ловите ее взгляд, направленный в вашу сторону."
        if not ApprovalCheck(RogueX, 600):
                jump Rogue_Frisky_Class_End

        "[RogueX.Name] открывает свой блокнот и начинает что-то строчить. Затем она вырывает лист, аккуратно складывает его и кладет перед вами."
        "Она смотрит, как вы разворачиваете записку. На листе написано: {i}Тебе нравится биология?{/i}"
        "Вы поворачиваетесь к ней и видите, что ее слегка кинуло в краску. Она двигает к вам ручку, чтобы вы могли написать ответ."
        menu:
            "Вы пишите в ответ. . ."
            "Ты о чем?":
                    pass

            "Да нет, не особо.":
                    $ RogueX.Statup("Love", 80, -3)
                    $ RogueX.Statup("Inbt", 60, -3)
                    $ RogueX.FaceChange("confused")

            "Это мой любимый предмет.":
                    $ RogueX.Statup("Love", 80, 5)
                    $ RogueX.FaceChange("smile")
                    "[RogueX.Name] читает вашу записку и на ее лице появляется улыбка. Она быстро набрасывает еще одну записку и снова кладет ее перед вами."
                    "Вы разворачиваете записку, стараясь, чтобы преподаватель вас не увидел. {i}\"Тогда, может быть, мы могли бы позаниматься вместе сегодня вечером?\"{/i}."
                    $ Line = "continue"

            "Да, если речь идет о тебе.":
                if ApprovalCheck(RogueX, 500, "I") or RogueX.SEXP >= 30:
                        $ RogueX.FaceChange("sly")
                        "[RogueX.Name] читает вашу записку и многозначительно улыбается вам."
                        $ Line = "flirt"
                elif ApprovalCheck(RogueX, 900):
                        $ RogueX.FaceChange("confused",2)
                        "[RogueX.Name] читает вашу записку, а затем сильно краснеет и опускает взгляд на свои записи."
                        $ RogueX.Blush = 1
                        $ Line = "flirt"
                else:
                        $ RogueX.FaceChange("perplexed",2)
                        "[RogueX.Name] читает вашу записку, а затем сильно краснеет. Она быстро набрасывает еще одну записку и снова кладет ее перед вами."
                        "Вы разворачиваете записку, стараясь, чтобы преподаватель вас не увидел. {i}\"Я имела в виду занятия! Может позанимаемся вместе сегодня вечером?\"{/i}."
                        $ RogueX.Blush = 1
                        $ Line = "continue"


        if Line == "continue":
                "[RogueX.Name] нарисовала маленькое сердечко вместо точки внизу вопросительного знака."
                "Она старается вести себя так, словно внимательно слушает лекцию, но скрыть широкую улыбку у нее не получается."
                menu:
                    "Вы пишите в ответ. . ."
                    "Может быть, в другой раз.":
                            $ RogueX.Statup("Love", 80, -3)
                            $ RogueX.Statup("Obed", 70, 5)
                            $ RogueX.Statup("Inbt", 60, -3)
                            $ RogueX.FaceChange("confused")
                            $ Line = 0
                    "Нет. У меня есть дела поважнее.":
                            $ RogueX.Statup("Love", 200, -15)
                            $ RogueX.Statup("Obed", 70, 5)
                            $ RogueX.Statup("Inbt", 60, -3)
                            $ Line = 0
                            $ RogueX.FaceChange("angry")
                            $ RogueX.DailyActions.append("angry")
                    "Конечно.":
                            "Она улыбается, когда читает ваш ответ, а затем подмигивает вам."
                            $ RogueX.DailyActions.append("studydate")
                            $ RogueX.FaceChange("smile")
                            jump Rogue_Frisky_Class_End
                    "Мы могли бы \"позаниматься\" прямо сейчас.":
                            if ApprovalCheck(RogueX, 1200):
                                    $ RogueX.FaceChange("sly",1)
                                    $ RogueX.Statup("Love", 80, 3)
                                    $ RogueX.Statup("Inbt", 60, 3)
                                    "На лице [RogueX.Name_rod] появляется озорная улыбка и она наклоняется к вам."
                                    $ Line = "flirt"
                            elif ApprovalCheck(RogueX, 700):
                                    $ RogueX.FaceChange("smile",1)
                                    $ RogueX.Statup("Inbt", 60, 2)
                                    "[RogueX.Name] краснеет и улыбается."
                                    $ Line = "flirt"
                            else:
                                    $ RogueX.FaceChange("confused",1)
                                    "[RogueX.Name] сперва кажется немного удивленной, затем хмурится."
                                    jump Rogue_Frisky_Class_End

        #End if Line == "continue"

        if Line == "flirt":
                $ Player.AddWord(1,"interruption") #adds to Recent
                $ D20 = renpy.random.randint(1, 20)
                $ RogueX.FaceChange("sly")
                "Вы замечаете, как один из ботинок [RogueX.Name_rod] соскользывает с ее ноги под столом. Она одаривает вас хитрой ухмылкой."
                if RogueX.Hose:
                        "Вы чувствуете, как ее гладкая ножка в чулке начинает медленно скользить вверх-вниз по всей вашей голени."
                else:
                        "Вы чувствуете, как ее гладкая голая ножка начинает медленно скользить вверх-вниз по всей вашей голени."

                while D20 <= 21:
                    menu:
                        extend ""
                        "Отодвинуться от нее.":
                                if Line == "fondle pussy":
                                        "Вы медленно убираете руку с ее колена и снова начинаете делать записи."
                                        $ Line = "tease"
                                elif Line == "fondle breast":
                                        "С последним сжатием вы перемещаете руку обратно на стол."
                                        $ Line = "tease"
                                else:
                                        $ Line = "rejected"
                                        $ RogueX.Statup("Love", 200, -15)
                                        $ RogueX.Statup("Obed", 70, 2)
                                        $ RogueX.Statup("Inbt", 60, -2)
                                jump Rogue_Frisky_Class_End

                        "Посмотреть ей в глаза и слегка улыбнуться." if Line == "flirt":
                                $ RogueX.FaceChange("smile")
                                $ RogueX.Statup("Love", 200, 5)
                                "[RogueX.Name] улыбается в ответ."
                                "Она оглядывается на переднюю часть аудитории, а ее рука в это время копошится под столом, пока не находит вашу руку."
                                $ Line = "handholding"
                        "Нежно взять и погладить ее по руке." if Line == "handholding":
                                $ RogueX.Statup("Love", 200, 5)
                                $ RogueX.FaceChange("smile")
                                "[RogueX.Name] удовлетворенно вздыхает и держит вас за руку до конца занятия."
                                jump Rogue_Frisky_Class_End

                        "Попробовать положить руку ей на колено." if Line != "fondle pussy":
                                $ Line = "fondle pussy"
                                if ApprovalCheck(RogueX, 1500) and RogueX.FondleP and RogueX.SEXP >= 40:
                                        $ RogueX.FaceChange("sly")
                                        $ RogueX.Statup("Love", 90, 5)
                                        $ RogueX.Statup("Obed", 70, 5)
                                        $ RogueX.Statup("Inbt", 60, 5)
                                        "[RogueX.Name] хитро улыбается и кладет свою руку на вашу."
                                elif ApprovalCheck(RogueX, 1800) and RogueX.FondleP:
                                        $ RogueX.FaceChange("smile")
                                        $ RogueX.Statup("Love", 80, 3)
                                        $ RogueX.Statup("Obed", 70, 7)
                                        $ RogueX.Statup("Inbt", 60, 3)
                                        "[RogueX.Name] слегка вздрагивает, когда ваша рука касается ее бедра, но затем на ее лице появляется легкая улыбка."
                                elif ApprovalCheck(RogueX, 2000):
                                        $ RogueX.FaceChange("perplexed",2)
                                        $ RogueX.Statup("Obed", 70, 10)
                                        $ RogueX.Statup("Inbt", 60, 3)
                                        "[RogueX.Name] смотрит на вас с тревогой, но вскоре немного успокаивается."
                                        $ RogueX.FaceChange("smile",1)
                                        $ D20 += 2
                                else:
                                        $ Line = "too far"

                                if Line == "fondle pussy":
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.Legs == "skirt":
                                            "Хитрая улыбка [RogueX.Name_rod] становится страстной, когда она чувствует, как ваши пальцы пробираются под ее юбку, а затем медленно обводят мягкие контуры ее холмика."
                                        elif RogueX.Legs == "pants":
                                            "Хитрая улыбка [RogueX.Name_rod] становится страстной, когда она чувствует, как ваши пальцы скользят под ее брюки, а затем медленно обводят мягкие контуры ее холмика."
                                        else: #No pants
                                            "Хитрая улыбка [RogueX.Name_rod] становится страстной, когда она чувствует, как ваши пальцы проскальзывают между ее бедер, а затем медленно обводят мягкие контуры ее холмика."

                                        if RogueX.Panties == "shorts":
                                            "Вы чувствуете, что ее шорты становятся влажными от ваших прикосновений через тонкий материал. Ее щеки заливаются краской, а дыхание становится все более глубоким и быстрым."
                                        elif RogueX.Panties:
                                            "Вы чувствуете, что ее трусики становятся влажными от ваших прикосновений через тонкий материал. Ее щеки заливаются краской, а дыхание становится все более глубоким и быстрым."
                                        elif RogueX.Pubes:
                                            "Вы чувствуете, что ее мохнатая киска становится влажной от ваших прикосновений. Ее щеки заливаются краской, а дыхание становится все более глубоким и быстрым."
                                        else:
                                            "Вы чувствуете, что ее гладкая киска становится влажной от ваших прикосновений. Ее щеки заливаются краской, а дыхание становится все более глубоким и быстрым."
                                        $ D20 += 5

                        "Продолжать ласкать ее киску." if Line == "fondle pussy":
                                $ RogueX.Statup("Obed", 70, 5)
                                $ RogueX.Statup("Inbt", 60, 3)
                                "Под звуки шумной аудитории вы продолжаете ласкать ее теплый пах."
                                $ D20 += 5

                        "Начать ласкать ее сиськи." if Line != "fondle breasts":
                                $ Line = "fondle breasts"
                                if ApprovalCheck(RogueX, 1500) and RogueX.FondleB and RogueX.SEXP >= 40:
                                        $ RogueX.Statup("Love", 80, 5)
                                        $ RogueX.Statup("Obed", 70, 5)
                                        $ RogueX.Statup("Inbt", 60, 3)
                                        $ RogueX.FaceChange("sly")
                                        "[RogueX.Name] закрывает глаза и начинает поглаживать вашу руку."
                                elif ApprovalCheck(RogueX, 1800) and RogueX.FondleB:
                                        $ RogueX.Statup("Love", 80, 3)
                                        $ RogueX.Statup("Obed", 70, 7)
                                        $ RogueX.Statup("Inbt", 60, 3)
                                        $ RogueX.FaceChange("smile",1)
                                        "[RogueX.Name] вздрагивает, когда ваша рука проходит по ее грудной клетке, но начинает улыбается, когда вы дотрагиваетесь до ее груди."
                                elif ApprovalCheck(RogueX, 2000):
                                        $ RogueX.Statup("Obed", 70, 10)
                                        $ RogueX.Statup("Inbt", 60, 3)
                                        $ RogueX.FaceChange("perplexed",2)
                                        "[RogueX.Name] смотрит на вас с тревогой, но вскоре немного успокаивается."
                                        $ RogueX.FaceChange("smile",2)
                                        $ D20 += 5
                                else:
                                        $ Line = "too far"

                                if Line == "fondle breasts":
                                        $ RogueX.FaceChange("sly")
                                        "Хитрые глаза [RogueX.Name_rod] загораются, когда ваша рука обхватывает ее грудь, нежно лаская."
                                        "Когда ее соски начинают твердеть, она издает легкий стон удовольствия."
                                        $ D20 += 7
                        "Продолжать ласкать ее сиськи." if Line == "fondle breasts":
                                $ RogueX.Statup("Obed", 70, 5)
                                $ RogueX.Statup("Inbt", 60, 2)
                                "Едва обращая внимание на лекцию, вы продолжаеште ласкать ее грудь своей ладонью."
                                $ D20 += 7

                    if Line == "too far":
                            $ RogueX.FaceChange("surprised",2)
                            $ RogueX.Statup("Love", 80, -5)
                            $ RogueX.Statup("Obed", 70, 7)
                            $ RogueX.Statup("Inbt", 50, -3)
                            "[RogueX.Name] начинает полушепотом ворчать на вас."
                            $ RogueX.FaceChange("angry",1)
                            "Ее ледяного взгляда, направленного на вас, достаточно, чтобы привлечь внимание ваших однокурсников."
                            $ D20 += 10

                #After D20:
                if Line not in ("rejected", "handholding", "tease"):
                    $ RogueX.Statup("Love", 80, -10)
                    $ RogueX.Statup("Obed", 70, -5)
                    $ RogueX.Statup("Inbt", 50, -10)
                    $ RogueX.FaceChange("surprised")
                    if EmmaX.Loc == "bg teacher":
                            "[EmmaX.Name] останавливает лекцию, когда замечает, что все в аудитории смотрят на вас двоих."
                            ch_e "[EmmaX.Petname], [RogueX.Name], лучше бы вы уделяли такое внимание лекции, а не телам друг друга?"
                            ch_e "Возможно, чтобы успокоиться, вам нужно посетить кабинет директора?"
                    elif StormX.Loc == "bg teacher":
                            "[StormX.Name] останавливает лекцию, когда замечает, что все в аудитории смотрят на вас двоих."
                            ch_s "[StormX.Petname], [RogueX.Name], я понимаю ваш задор, но могли бы вы заниматься подобным не при мне?"
                            ch_s "Думаю, вам стоит успокоиться и посетить кабинет Чарльза?"
                    else:
                            "Доктор Маккой останавливает лекцию, когда замечает, что все в аудитории смотрят на вас двоих."
                            ch_b "О, божечки-кошечки!"
                            ch_b "[Player.Name]!?! {b}ЧТО ВЫ ДЕЛАЕТЕ? ОБА, НЕМЕДЛЕННО В КАБИНЕТ ПРОФЕССОРА!{/b}"
                    if RogueX not in Rules:
                            call Girls_Caught(RogueX)
                    else:
                            "Поскольку Ксавье не заботят ваши дела, вы оба отправляетесь по своим комнатам."
                            $ RogueX.Loc = "bg player"
                            call CleartheRoom(RogueX,0,1)
                            jump Player_Room
        # end if Line == "flirt"


label Rogue_Frisky_Class_End:
        if not Line:
                $ RogueX.FaceChange("confused")
                "Она разворачивает записку и быстро ее перечитывает."
                $ RogueX.FaceChange("sad")
                "После этого, вы видитие разочарование, отразившееся на ее лице."
                "Она пишет ответ и кладет записку перед вами."
                "Вы открываете ее и читаете: {i}Тогда забудь.{/i}"
        elif Line == "tease":
                $ RogueX.FaceChange("sly",1)
                "[RogueX.Name] делает глубокий вдох, наклоняется к вам и шепчет с предыханием."
                ch_r "Вечерние \"занятия\" будут гораздо интереснее." # attempt smaller text?
        elif Line == "rejected":
                $ RogueX.FaceChange("sadside")
                "[RogueX.Name] выглядит удивленной и обиженной. До конца занятия она не произносит ни слова."
                "Похоже ей трудно смотреть вам в глаза."

        "В конце концов [RogueX.Name], кажется, успокаивается и переключает свое внимание на материалы занятия. Вы умудряетесь сделать то же самое, не заснув."
        return



# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Rogue_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        if "switched" in RogueX.History:
                jump Rogue_Switch2
        $ RogueX.FaceChange("smile", 1)
        ch_r "О, привет!"
        ch_r "Мы раньше, случайно, не встречались?"
        menu:
            extend ""
            "Это я, [Player.XName].":
                    $ RogueX.FaceChange("confused", 1)
                    ch_r "Что?"
                    $ RogueX.FaceChange("surprised", 1)
                    ch_r "Ах!"
                    $ RogueX.FaceChange("smile", 1)
                    ch_r "Жизнь, я смотрю, тебя совсем помотала, да?"
                    $ RogueX.AddWord(1,"switch") #recent

            "Нет.":
                    ch_r "Что ж, тогда приятно познакомиться."
                    ch_r "Кстати, меня зовут [RogueX.Name]."
            "Возможно?":
                    ch_r "Я, кажется, припоминаю кого-то, похожего на тебя. . ."

        if "switch" not in RogueX.RecentActions:
                    $ RogueX.FaceChange("confused", 1)
                    ch_r ". . ."
                    ch_r "Могу поклясться, что где-то тебя видела. . ."
                    $ RogueX.FaceChange("surprised", 1)
                    ch_r "Подождите-ка. . ."
                    ch_r "Ты, случаем, не [Player.XName]?"
                    $ RogueX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Ага, я [Player.XName].":
                                $ RogueX.Statup("Love", 90, 1)
                                $ RogueX.Statup("Obed", 70, 1)
                                ch_r "Ах!"
                                $ RogueX.FaceChange("smile", 1)
                                ch_r "Жизнь, я смотрю, тебя совсем помотала, да?"
                        "Нет.":
                                $ RogueX.FaceChange("angry", 1)
                                $ RogueX.Statup("Obed", 60, 1)
                                $ RogueX.Statup("Obed", 70, 1)
                                ch_r "Не ври, я узнала тебя, [Player.XName]."
                        "Возможно?":
                                $ RogueX.FaceChange("sly", 1)
                                $ RogueX.Statup("Love", 80, 1)
                                $ RogueX.Statup("Obed", 70, 1)
                                $ RogueX.Statup("Inbt", 60, 1)
                                ch_r "Ну значит это и правда ты, [Player.XName]."
                    ch_r "Зачем ты так со мной?"
                    ch_r "Почему не сказать прямо?"
                    menu:
                        extend ""
                        "Извини, захотелось пошутить.":
                                $ RogueX.FaceChange("sly", 1)
                                $ RogueX.Statup("Love", 70, 1)
                                ch_r "Да-да. . ."
                        "Даже не знаю, что ответить.":
                                $ RogueX.FaceChange("sly", 1)
                                $ RogueX.Statup("Obed", 70, 1)
                                $ RogueX.Statup("Inbt", 80, 1)
                                ch_r "Угу. . ."
                        "Хех.":
                                $ RogueX.FaceChange("sly", 1,Eyes="side")
                                $ RogueX.Statup("Love", 70, 1)
                                $ RogueX.Statup("Love", 90, 1)
                                $ RogueX.Statup("Inbt", 70, 1)
                                ch_r "Смейся-смейся. . ."
                    ch_r "Поскольку моя мама - перевертыш, я привыкла узнавать людей, независимо от того, насколько они похожи на себя."
        #end "tried to lie"
        $ RogueX.FaceChange("smile", 1)
        ch_r "Но к чему такие. . . перемены?"
        menu:
            extend ""
            "Да так, по приколу.":
                    $ RogueX.Statup("Inbt", 70, 1)
                    $ RogueX.FaceChange("surprised", 2)
                    ch_r "Ох, эм. . . ну, дело твое."
                    $ RogueX.FaceChange("sly", 1)
            "Я так себя сейчас ощущаю.":
                    ch_r "Oh. . . пожалуй, могу тебя понять."
            "У меня нет каких-то особых причин.":
                    ch_r "Ну ладно, дело твое. . ."

        if [Player.Name] != [Player.XName]:
                ch_p "А еще теперь меня зовут [Player.Name]."
                ch_r "Ох. . . что ж, приятно познакомиться, [Player.Name]."

        if RogueX.SEXP >= 15:
                $ RogueX.FaceChange("sad", 1,Mouth="smile")
                ch_r "Эм. . . а я тебе еще. . . интересна?"
                menu:
                    extend ""
                    "Конечно!":
                            $ RogueX.FaceChange("smile", 1)
                            $ RogueX.Statup("Love", 70, 2)
                            $ RogueX.Statup("Love", 90, 1)
                            ch_r "Оу, это так приятно. . ."
                    "Да не особо.":
                            $ RogueX.FaceChange("sad", 1)
                            $ RogueX.Statup("Love", 80, -2)
                            $ RogueX.Statup("Obed", 60, 2)
                            $ RogueX.Statup("Obed", 80, 2)
                            ch_r "Ох. . ."
                            $ RogueX.FaceChange("sadside", 1)
                            ch_r "Ясно. . ."
                            if ApprovalCheck(RogueX, 1500):
                                    $ RogueX.FaceChange("sadside", 1,Mouth="smirk")
                                    ch_r "Но мой интерес к тебе не угас. . ."
                    "А ты как думаешь?":
                            $ RogueX.FaceChange("sly", 1)
                            $ RogueX.Statup("Obed", 70, 1)
                            $ RogueX.Statup("Inbt", 70, 1)
                            ch_r "Я думаю, ты домогаешься до всего, что движется. . ."

        if not Player.Male and RogueX.Les > 5:
                $ RogueX.FaceChange("sly", 1)
                ch_r "Я довольно лояльна к подобным изменениям. . ."
        if ApprovalCheck(RogueX, 1500):
                ch_r "Думаю, к таким изменениям мне нужно немного привыкнуть."
                $ RogueX.AddWord(1,0,0,0,"girltalk") #history
        else:
                $ RogueX.FaceChange("normal", 1,Eyes="side")
                ch_r "Думаю, мне требуется немного времени, чтобы принять твой новый образ. . ."
        $ RogueX.Traits.remove("switchcheck")
        $ RogueX.AddWord(1,0,0,0,"switched") #history
        return

label Rogue_Switch2:
        #when you switch for a 2+ time
        $ RogueX.FaceChange("surprised", 1)
        ch_r "Ох!"
        $ RogueX.FaceChange("confused", 1)
        ch_r "Ты выглядишь. . . как раньше."
        $ RogueX.FaceChange("smile", 1)
        ch_r "Здорово."
        $ RogueX.Traits.remove("switchcheck")
        $ RogueX.History.remove("switched")
        $ RogueX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Rogue_Girltalk(Auto=0,Other=0):
        # if Auto Rogue starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in RogueX.History:
                return
        if "nogirls" in RogueX.History:
                jump Rogue_Girltalk_Redux
        if Auto:
                $ RogueX.FaceChange("sadside", 2)
                ch_r "Hey, [Player.Name]. . ."
                ch_r "Я тут подумала и. . . я тебе немного нравлюсь?"
        else:
                $ RogueX.FaceChange("confused", 1)
                ch_r "Что? Я тебе нравлюсь?"
        menu:
            extend ""
            "Да?":
                    $ RogueX.FaceChange("surprised", 2)
                    $ RogueX.Statup("Love", 70, 2)
                    $ RogueX.Statup("Love", 90, 2)
                    $ RogueX.Statup("Obed", 70, 1)
                    ch_r "Ох. . ."
                    $ RogueX.FaceChange("smile", 1, Eyes="side")
                    $ Auto = 0
            "Наверное?":
                    $ RogueX.FaceChange("confused", 2)
                    $ RogueX.Statup("Obed", 80, 2)
                    $ RogueX.Statup("Inbt", 80, 2)
                    ch_r "Ох. . ."
                    $ RogueX.FaceChange("sly", 1)
            "Не особо.":
                    $ RogueX.FaceChange("sadside", 2)
                    $ RogueX.Statup("Love", 50, -2)
                    $ RogueX.Statup("Love", 90, -2)
                    $ RogueX.Statup("Obed", 60, 2)
                    $ RogueX.Statup("Obed", 80, 2)
                    ch_r "Ох. . ."
        ch_r "Я и не знаю, как к этому относиться.. . ."
        if not RogueX.Les:
                ch_r "У меня не было раньше. . . опыта с девушкой. . ."
                $ RogueX.FaceChange("smile", 1)
                ch_r "Черт,"
                $ RogueX.FaceChange("surprised", 2)
                ch_r "- все-таки за всю жизнь я несколько раз целовалась с ними! . ."
        if not ApprovalCheck(RogueX, 1100) and not RogueX.Les:
                $ RogueX.FaceChange("sadside", 1)
                ch_r "Я не уверена. . . возможно, для меня это слишком. . ."
                $ RogueX.AddWord(1,0,0,0,"nogirls") #history
                call Girltalk_Check(RogueX)
                return
        $ RogueX.FaceChange("sly", 1)
        if Auto:
                ch_r "Ты мне, вроде как, нравишься. . ."
        else:
                ch_r "Ты мне тоже нравишься. . ."
        ch_r "Пожалуй, мы сможем что-нибудь придумать. . ."
        $ RogueX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(RogueX)
        return

label Rogue_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing
        if ApprovalCheck(RogueX, 1100):
                $ RogueX.FaceChange("sly", 1)
                if Other in TotalGirls and "nogirls" in Other.History:
                        ch_r "Я не уверена. . ."
                ch_r "Пожалуй, мы сможем что-нибудь придумать. . ."
                $ RogueX.DrainWord("nogirls",0,0,0,1) #history
                $ RogueX.AddWord(1,0,0,0,"girltalk") #history
        elif "nogirls" not in RogueX.History:
                $ RogueX.AddWord(1,0,0,0,"nogirls") #history
                $ RogueX.FaceChange("sadside", 1)
                ch_r "Я не знаю. . . Для меня это может быть слишком. . ."
        elif "nogirls" in RogueX.DailyActions:
                $ RogueX.FaceChange("angry", 1)
                if RogueX.Forced:
                        #if Forced, she will just go with it anyway
                        if "nogirls" not in RogueX.RecentActions:
                                $ RogueX.Statup("Love", 80, -2)
                                $ RogueX.Statup("Obed", 80, 2)
                                $ RogueX.AddWord(1,"nogirls",0,0,0) #recent
                        return
                ch_r "Хватит давить на меня. . ."
        else:
                $ RogueX.Statup("Inbt", 50, 2)
                ch_r "Как я уже сказала, я не думаю, что хочу таких отношений. . ."
                $ RogueX.AddWord(1,0,"nogirls",0,0) #daily
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Rogue_and_Kitty Dialogue / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_and_Kitty:
        #this scene is about Rogue and Kitty talking
        #Triggered in Study. If Rogue has "KittyPuss" in her history then she's cleared it.
        #If Rogue has "KittyTits" then she's done the tits part, "KittyKiss" she's done the kissing part
        #If she has none of these checks, it plays through from the start

        $ Line = 0
        call Shift_Focus(RogueX)
        show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 70:
                xzoom -1
        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder 75

        if "KittyKiss" in RogueX.History:
                #if you'd done this before. . .
                "Пока вы занимаетесь, [RogueX.Name] замечает, что [KittyX.Name] пристально смотрит на ее грудь. . ."
                call Rogue_Kitty_Breasts
                $ RogueX.FaceChange("sly",1,Eyes="side")
                $ KittyX.FaceChange("sexy",1,Eyes="side")
                ch_r "Так. . . ты разглядываешь мою грудь. . ."
                ch_r "Может. . . тебе что-то ещё приглянулось?"
                $ KittyX.FaceChange("sexy",2,Eyes="down")
                ch_k "Нууу. . ."
                ch_r "Да?"
                ch_r "Похоже, кое-что и правда привлекло твоё внимание. . ."
        if "KittyTits" in RogueX.History:
                call Rogue_Kitty_Pussy
                jump Rogue_Kitty_End

        $ RogueX.Arms = 0
        "Пока вы занимаетесь, [RogueX.Name] и [KittyX.Name] одновременно тянутся к еде, на мгновение их руки соприкасаются."
        $ RogueX.FaceChange("surprised",1)
        $ RogueX.ArmPose = 2
        "Вздрогнув, [RogueX.Name] отдергивает руку."
        if "touch" not in RogueX.Traits and "les Kitty" not in RogueX.History:
                #no les stuff, no powers off
                $ RogueX.FaceChange("surprised",2,Eyes="side")
                $ KittyX.FaceChange("surprised",1,Eyes="side")
                ch_r "Прости!"
                ch_k "Все нормально!"
                $ RogueX.FaceChange("sly",1,Eyes="side")
                $ KittyX.FaceChange("confused",Eyes="side")
                ch_r "Слушай, я знаю, что не могу прикоснуться к тебе, но. . ."
                ch_r "-ты когда-нибудь. . . думала, что было бы, не будь у меня моей силы?"
        else:
                #can touch
                $ RogueX.FaceChange("sly",2,Eyes="side")
                $ KittyX.FaceChange("smile",Eyes="side")
                ch_r "Прости, рефлекс."
                ch_k "Хех."
                ch_r "Слушай, раньше, когда я еще не могла к тебе прикоснуться. . . ты думала, что было бы, не будь у меня моей силы?"
        $ RogueX.FaceChange("sly",1,Eyes="side")
        $ KittyX.FaceChange("surprised",2,Eyes="side")
        ch_k "Ох! Нууу. . . "
        $ KittyX.FaceChange("sly",2,Eyes="leftside")
        ch_k ". . . возможно. . ."
        ch_r "И. . . "
        ch_r "-что ты думала?"
        ch_k "Эм. . . наверное. . ."

    #conditional on her inhibitions
        if "les Kitty" not in RogueX.History and KittyX.Inbt < 300:
                #very low inbt
                $ RogueX.FaceChange("surprised",Eyes="side")
                $ KittyX.FaceChange("smile",2,Eyes="leftside")
                ch_k "Что мы могли бы. . . пожать друг другу руки."
                $ RogueX.FaceChange("sly",Eyes="side")
                ch_r "Блин, и все, сладенькая?"
                $ RogueX.GirlLikeUp(KittyX,5)
                $ KittyX.GirlLikeUp(RogueX,5)
                ch_r "Признаюсь, я вот думала о чем-то большем."
                ch_k "Нууу. . . -может быть-, я думала не только об этом. . ."
        elif KittyX.Inbt < 500:
                #low inbt
                $ KittyX.FaceChange("sexy",2,Eyes="leftside")
                ch_k "Я не знаю. . ."
        else:
                #high inbt.
                $ KittyX.FaceChange("sexy",2,Eyes="side")
                $ RogueX.GirlLikeUp(KittyX,15)
                $ KittyX.GirlLikeUp(RogueX,15)
                $ Player.Statup("Focus", 50, 5)
                $ RogueX.Statup("Lust", 50, 5)
                $ KittyX.Statup("Lust", 50, 5)
                ch_k "О чем-то неприличном?"

        $ RogueX.FaceChange("sly",Eyes="side")
        ch_r "Вот как?"
        ch_r "А -поподробнее-?"
    #go to kissing scene
        call Rogue_Kitty_Kiss
        if not ApprovalCheck(KittyX, 300, "I") or not ApprovalCheck(KittyX,1050):
                #exits if not ready to continue
                $ KittyX.FaceChange("perplexed",2,Eyes="side")
                ch_k "Ох! Эм. . . больше ни о чем, только об этом. . ."
                jump Rogue_Kitty_End

        $ RogueX.FaceChange("sly",Eyes="side")
        $ KittyX.FaceChange("sly",2,Eyes="leftside")
        ch_k "Нууу[KittyX.like]когда мы вместе принимали душ. . ."
        ch_r "М?"
        ch_k "И я увидела твои. . . "
        ch_r "Мои \"что?\" . ."
        $ KittyX.FaceChange("sly",2,Eyes="side")
        $ Player.Statup("Focus", 60, 3)
        $ RogueX.Statup("Lust", 60, 3)
        $ KittyX.Statup("Lust", 60, 3)
        ch_k "Твои сиськи."
        ch_r "Значит, ты думала о них?"
        $ KittyX.FaceChange("sly",1,Eyes="side")
        ch_k "Мне. . . "
        ch_k "-кажется, они великолепны. . ."
        ch_r "Хм, не ожидала, что ты решишься это сказать. . ."
        ch_r "Я думаю, что у тебя тоже красивая грудь. . ."
        $ KittyX.FaceChange("sly",2,Eyes="leftside")
        ch_k ". . ."
    #go to breast portion
        call Rogue_Kitty_Breasts
        if not ApprovalCheck(KittyX, 400, "I") or not ApprovalCheck(KittyX,1350):
                jump Rogue_Kitty_End

        $ RogueX.FaceChange("sly",Eyes="side")
        ch_r "Итак. . . мы выяснили, что ты интересовалась моей грудью. . ."
        ch_r "А -еще- о чем-то. . . ты фантазировала?"
        $ KittyX.FaceChange("sly",2,Eyes="down")
        ch_k "Нууу, знаешь. . ."
        ch_r "М?"
        ch_r "Похоже, что да. . ."
    #go to pussy portion
        call Rogue_Kitty_Pussy


label Rogue_Kitty_End:
        $ RogueX.FaceChange("sly",Eyes="side")
        $ KittyX.FaceChange("sly",Eyes="side")
        if "KittyChat" not in RogueX.History:
                #only plays first time through
                ch_r "В общем, [KittyX.Name], должна сказать, я постоянно чувствовала на себе твой взгляд."
                $ KittyX.FaceChange("surprised",2,Eyes="side")
                ch_k "Правда? Все это время?"
                ch_r "Ну не прямо все время, но иногда. . ."
                $ KittyX.FaceChange("sly",1,Eyes="side")
                ch_r "И, конечно, я тоже не сводила с тебя глаз."
                $ KittyX.FaceChange("smile",Eyes="side")
                ch_k "Я. . . очень рада это слышать."
                $ RogueX.AddWord(1,0,0,0,"KittyChat")
        elif "KittyPuss" in RogueX.History:
                $ RogueX.DrainWord("KittyChat",0,0,0,1) #removes general "KittyChat" tag from History
        if "breasts" in RogueX.RecentActions or "pussy" in RogueX.RecentActions:
                #this activates if they got as far as the breasts phase, without triggering checks to see if they'd done it before
                $ RogueX.AddWord(1,0,0,0,"les Kitty")
                $ KittyX.AddWord(1,0,0,0,"les Rogue")
                $ RogueX.AddWord(1,"lesbian",0,0,0) #adds "lesbian" to recent actions for both girls
                $ KittyX.AddWord(1,"lesbian",0,0,0) #adds "lesbian" to recent actions for both girls
        show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 100:
                xzoom 1
        if "threeup" in RogueX.RecentActions:
                #if you asked to join in earlier
                $ RogueX.FaceChange("sly")
                if not Player.Male:
                    ch_r "Так, ты, вроде бы, тоже хотела поучаствовать?"
                else:
                    ch_r "Так, ты, вроде бы, тоже хотел поучаствовать?"
                call SexMenu
        elif "approval" in RogueX.RecentActions:
                menu:
                    "Мне бы хотелось присоединиться к вам.":
                            $ RogueX.Statup("Obed", 70, 2)
                            $ RogueX.Statup("Inbt", 80, 2)
                            $ KittyX.Statup("Obed", 70, 2)
                            $ KittyX.Statup("Inbt", 80, 2)
                            call SexMenu
                    "Это было ужасно сексуально.":
                            $ RogueX.FaceChange("sly")
                            $ RogueX.Statup("Inbt", 80, 5)
                            $ KittyX.Statup("Inbt", 80, 5)
                            menu:
                                ch_r "Хочешь тоже поучаствовать?"
                                "Ага.":
                                        $ RogueX.Statup("Love", 90, 2)
                                        $ RogueX.Statup("Inbt", 80, 3)
                                        $ KittyX.Statup("Love", 90, 2)
                                        $ KittyX.Statup("Inbt", 80, 3)
                                        ch_r "Супер."
                                        call SexMenu
                                "Нет, мне и так хорошо.":
                                        $ RogueX.FaceChange("sad")
                                        $ RogueX.Statup("Love", 80, -2)
                                        $ RogueX.Statup("Obed", 80, 2)
                                        $ KittyX.Statup("Love", 80, -2)
                                        $ KittyX.Statup("Obed", 80, 4)
                                        ch_r "Жаль. . ."
                                ". . .":
                                        $ RogueX.FaceChange("confused")
                                        $ RogueX.Statup("Love", 80, -2)
                                        $ KittyX.Statup("Love", 80, -2)
                                        ch_r "Ну ладно. . ."
                                        $ RogueX.FaceChange("normal")
                    ". . .":
                            pass
        call Sex_Over
        return
# End main portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Rogue_Kitty_Kiss:
        # called from Rogue_and_Kitty if she wants to kiss

        $ RogueX.FaceChange("sly",Eyes="side")
        $ KittyX.FaceChange("sly",1,Eyes="side")
        $ Player.Statup("Focus", 60, 3)
        $ RogueX.Statup("Lust", 60, 3)
        $ KittyX.Statup("Lust", 60, 3)
        ch_k "Нууу, что у тебя, наверное. . . мягкие губы. . ."
        if "les Kitty" not in RogueX.History:
                ch_r "Ох, -так- и есть."
        else:
                #some experience
                ch_r "Ох, -так- и есть, ты и сама это уже прекрасно знаешь."
        ch_r "Значит, ты думала поцеловать меня?"
        $ RogueX.GirlLikeUp(KittyX,15)
        $ KittyX.GirlLikeUp(RogueX,15)
        if "les Kitty" not in RogueX.History:
                $ KittyX.FaceChange("sly",2,Eyes="leftside")
                ch_k "Я. . . ага. . ."
                ch_r "Хочешь попробовать?"
                $ KittyX.FaceChange("surprised",2,Eyes="side")
                ch_k "Что? [KittyX.Like]сейчас?"
                $ KittyX.FaceChange("sly",2,Eyes="leftside")
                ch_k "Эм. . . да, но. . ."
                if not ApprovalCheck(KittyX, 500, "I") or ApprovalCheck(KittyX, 500, "O"):
                        call Rogue_Kitty_AboutZero
                if "approved" not in RogueX.RecentActions:
                        return
        else:
                #some experience
                $ KittyX.FaceChange("sly",1,Eyes="side")
                ch_k "Ага. . . они оказались такими, как я и представляла."
                ch_r "Кстати об этом. . ."
        $ RogueX.FaceChange("sly",Eyes="side")
        $ KittyX.FaceChange("sly",2,Eyes="side")
        show Rogue_Sprite:
                ease 1 pos(650,50)
        "[RogueX.Name] наклоняется к [KittyX.Name_dat]. . ."
        show Rogue_Sprite at SpriteLoc(650,50)
        $ Player.Statup("Focus", 60, 3)
        $ RogueX.Statup("Lust", 60, 3)
        $ KittyX.Statup("Lust", 60, 3)
        "Заведя руку [KittyX.Name_dat] за спину, [RogueX.Name] проводит рукой по ее щеке."
        $ RogueX.FaceChange("kiss")
        $ KittyX.FaceChange("kiss",2)
        $ Player.Statup("Focus", 60, 3)
        $ RogueX.Statup("Lust", 70, 5)
        $ KittyX.Statup("Lust", 70, 5)
        "Затем [RogueX.Name] наклоняется к ней еще больше и страстно целует."
        "По прошествии достаточного количества времени, которого хватило бы, чтобы оставить [KittyX.Name_vin] совсем без жизненных сил, если бы вы не оказали на них влияние, [RogueX.Name] отстраняется."
        show Rogue_Sprite:
                ease 1 pos(RogueX.SpriteLoc,50)
        $ RogueX.FaceChange("sly",1,Eyes="side")
        $ KittyX.FaceChange("surprised",1,Eyes="side")
        ch_k "Вау."
        show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc,50)
        $ KittyX.FaceChange("sexy",1,Eyes="side")
        ch_k "Примерно так все и было в моих мечтах."
        ch_r "Правда?"
        ch_r "Ты мечтала обо мне?"
        $ KittyX.FaceChange("sly",2,Eyes="leftside")
        ch_k "Может быть?"
        $ KittyX.FaceChange("sly",1,Eyes="side")
        $ RogueX.GirlLikeUp(KittyX,20)
        $ KittyX.GirlLikeUp(RogueX,20)
        ch_r "Теперь мне интересно. . ."
        ch_r "О чем еще ты могла \"мечтать\"."
        $ RogueX.AddWord(1,0,0,0,"KittyKiss")
        return
#End Rogue_Kitty_Kiss: / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Rogue_Kitty_Breasts:
        # called from Rogue_and_Kitty if she wants to discuss her breasts
        if "les Kitty" not in RogueX.History:
                $ RogueX.FaceChange("sly",Eyes="side")
                $ KittyX.FaceChange("sly",Eyes="side")
                ch_r "Ты когда-нибудь думала о том, чтобы. . . прикоснуться к ним?"
                $ KittyX.FaceChange("sexy",2,Eyes="leftside")
                ch_k ". . . ага, возможно. . ."
                ch_r "Ты бы хотела их помять?"
                $ KittyX.FaceChange("sexy",2,Eyes="side")
                $ Player.Statup("Focus", 60, 3)
                $ RogueX.Statup("Lust", 60, 3)
                $ KittyX.Statup("Lust", 60, 3)
                ch_k "Я надеялась, что однажды смогу их немного. . . -ощупать.-"
        else:
                #some experience
                $ RogueX.FaceChange("sly",Eyes="side")
                $ KittyX.FaceChange("sly",Eyes="side")
                ch_r "На ощупь они также хороши как и на вид?"
                $ KittyX.FaceChange("sly",1,Eyes="side")
                ch_k ". . . даже лучше. . ."
                ch_r "Ты бы хотела их снова помять?"
                $ Player.Statup("Focus", 60, 3)
                $ RogueX.Statup("Lust", 60, 3)
                $ KittyX.Statup("Lust", 60, 3)
                ch_k "Я надеялась, что однажды смогу их снова -ощупать.-"
        $ RogueX.GirlLikeUp(KittyX,15)
        $ KittyX.GirlLikeUp(RogueX,15)
        call Rogue_Kitty_AboutZero
        if "approved" not in RogueX.RecentActions:
                return
        $ Partner = KittyX
        $ KittyX.FaceChange("sly",Eyes="side")
        $ Player.Statup("Focus", 60, 3)
        $ RogueX.Statup("Lust", 60, 3)
        $ KittyX.Statup("Lust", 60, 3)
        $ KittyX.ArmPose = 2
        "[KittyX.Name] нерешительно протягивает руку и слегка касается груди [RogueX.Name_rod]."
        if RogueX.OverNum() or RogueX.ChestNum():
                $ RogueX.FaceChange("smile",Eyes="side")
                ch_r "Какой смысл делать это через одежду?"
                ch_r "Раз уж мы на это решились."
                $ RogueX.Uptop = 1
                $ Line = get_clothing_name(RogueX.Over_key, vin) if RogueX.Over else get_clothing_name(RogueX.Chest_key, vin)
                $ RogueX.FaceChange("sly",Eyes="side")
                $ Player.Statup("Focus", 70, 3)
                $ RogueX.Statup("Lust", 70, 3)
                $ KittyX.Statup("Lust", 70, 3)
                "С хитрой ухмылкой [RogueX.Name] приподнимает [Line], обнажая свою грудь."
                call Girl_First_Topless(RogueX,1)
                $ Line = 0
        else:
                $ RogueX.FaceChange("smile",Eyes="side")
                ch_r "Я не стеклянная, не нужно осторожничать."
        $ RogueX.FaceChange("sly",1,Eyes="down")
        $ KittyX.FaceChange("sly",2,Eyes="side")
        "[KittyX.Name] снова протягивает руку, нежно поглаживая пальцем одну грудь, пока сосок [RogueX.Name_rod] не затвердевает."
        $ KittyX.Offhand = 'fondle girl breasts'
        "Затем она проводит рукой снизу и нежно обхватывает ее ладонью."
        $ RogueX.Offhand = 'fondle girl breasts'
        "Она медленно двигает играет с ней одной рукой, бессознательно проделывая то же самое со своей грудью."
        if KittyX.OverNum() or KittyX.ChestNum():
                $ RogueX.FaceChange("sly",1,Eyes="side")
                ch_r "Слушай, будет справедливо, если и ты покажешь мне свои восхитительные сиськи."
                $ KittyX.FaceChange("sexy",2,Eyes="side")
                ch_k "Хех, ладно. . ."
                $ Line = get_clothing_name(KittyX.Over_key, dat) if KittyX.Over else get_clothing_name(KittyX.Chest_key, dat)
                $ KittyX.Over = 0
                $ KittyX.Chest = 0
                $ Player.Statup("Focus",70, 3)
                $ RogueX.Statup("Lust", 70, 3)
                $ KittyX.Statup("Lust", 70, 3)
                "[KittyX.Name] позволяет упасть [Line] на пол."
                call Girl_First_Topless(KittyX,1)
                $ Line = 0
        ch_r "Знаешь, я всегда немного завидовала тому, какие у тебя аккуратные сиськи."
        $ KittyX.FaceChange("surprised",2,Eyes="side")
        ch_k "Не может быть! У тебя отличная грудь!"
        $ RogueX.FaceChange("sly")
        ch_r "[RogueX.Petname], а ты что думаешь?"
        $ KittyX.FaceChange("sly",1)
        $ Line = 0
        menu:
            ch_r "Чья грудь лучше? Ее или моя?"
            "Грудь [RogueX.Name_rod].":
                    $ RogueX.Statup("Love", 90, 5)
                    $ RogueX.Statup("Inbt", 70, 5)
                    $ KittyX.Statup("Obed", 80, 5)
                    $ KittyX.Statup("Love", 80, -2)
                    $ KittyX.FaceChange("sexy",2,Eyes="side")
                    $ KittyX.GirlLikeUp(RogueX,5)
                    ch_k "Ага, она как два спелых яблочка. . . Эм, то есть-"
                    $ Line = "Rogue"
            "Грудь [KittyX.Name_rod].":
                    $ KittyX.Statup("Love", 90, 5)
                    $ KittyX.Statup("Inbt", 70, 5)
                    $ RogueX.Statup("Obed", 80, 5)
                    $ RogueX.Statup("Love", 80, -2)
                    $ RogueX.GirlLikeUp(KittyX,5)
                    $ RogueX.FaceChange("sexy",2,Eyes="side")
                    ch_r "Ага, она такая очаровательная. . ."
                    $ Line = "Kitty"
            "Моя." if Player.Male != 1:
                    $ RogueX.Statup("Obed", 80, 5)
                    $ KittyX.Statup("Obed", 80, 5)
                    if ApprovalCheck(RogueX, 800):
                        $ RogueX.Statup("Obed", 70, 7)
                        $ RogueX.FaceChange("sly",1)
                        $ KittyX.FaceChange("sly",1)
                        ch_r "Тут не поспоришь. . ."
                    else:
                        $ RogueX.Statup("Love", 90, -2)
                        $ KittyX.Statup("Love", 90, -2)
                        $ RogueX.FaceChange("sly",1,Brows="angry")
                        $ KittyX.FaceChange("sly",1,Brows="angry")
                    $ Line = "Me"
            "Меня в это не втягивайте.":
                    $ RogueX.Statup("Love", 90, 1)
                    $ RogueX.Statup("Inbt", 80, 5)
                    $ KittyX.Statup("Love", 90, 2)
                    $ RogueX.FaceChange("smile",1)
                    ch_r "Ха! Извини, [RogueX.Petname], не удержалась."
            ". . .":
                    $ RogueX.Statup("Obed", 70, 2)
                    $ RogueX.Statup("Inbt", 80, 5)
                    $ RogueX.FaceChange("smile",1)
                    ch_r "Хех, извини, [RogueX.Petname], думаю, я поставила тебя в неловкое положение."
        menu:
            extend ""
            "-но у тебя тоже отличная грудь." if Line in ("Kitty","Rogue"):
                $ RogueX.GirlLikeUp(KittyX,5)
                $ KittyX.GirlLikeUp(RogueX,5)
                if Line == "Rogue":
                    $ RogueX.Statup("Love", 90, 3)
                    $ RogueX.Statup("Inbt", 70, 2)
                    $ RogueX.FaceChange("smile",1)
                    $ KittyX.FaceChange("sly",1,Eyes="side")
                    ch_r "Пытаешься никого не обидеть?"
                elif Line == "Kitty":
                    $ KittyX.Statup("Love", 90, 2)
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ RogueX.FaceChange("sly",1,Eyes="side")
                    $ KittyX.FaceChange("smile",1)
                    ch_k "Хех, конечно."
                else:
                    $ RogueX.Statup("Love", 90, 2)
                    $ RogueX.Statup("Inbt", 70, 4)
                    $ KittyX.Statup("Love", 90, 2)
                    $ KittyX.Statup("Inbt", 70, 3)
                    $ RogueX.FaceChange("smile",1)
                    $ KittyX.FaceChange("smile",1)
                    ch_r "Конечно!"
                    ch_k "Ага!"
            "-но у вас тоже отличная грудь." if Line == "Me":
                $ RogueX.GirlLikeUp(KittyX,5)
                $ KittyX.GirlLikeUp(RogueX,5)
                $ RogueX.Statup("Love", 90, 2)
                $ RogueX.Statup("Inbt", 70, 4)
                $ KittyX.Statup("Love", 90, 2)
                $ KittyX.Statup("Inbt", 70, 3)
                $ RogueX.FaceChange("smile",1)
                $ KittyX.FaceChange("smile",1)
                ch_r "Конечно!"
                ch_k "Ага!"
            "Извини." if Line in ("Kitty","Rogue"):
                $ RogueX.FaceChange("sly",1,Eyes="leftisde")
                $ KittyX.FaceChange("sly",1,Eyes="leftisde")
                if Line == "Rogue":
                    $ KittyX.Statup("Love", 90, 2)
                    $ KittyX.Statup("Obed", 80, 4)
                    $ KittyX.Statup("Inbt", 70, 2)
                    ch_k "Я все понимаю. . ."
                else:
                    $ RogueX.Statup("Love", 90, 2)
                    $ RogueX.Statup("Obed", 80, 4)
                    $ RogueX.Statup("Inbt", 70, 2)
                    if not Player.Male:
                        ch_r "Ты просто высказала свое мнение. . ."
                    else:
                        ch_r "Ты просто высказал свое мнение. . ."
            "Извините." if Line not in ("Kitty","Rogue") or not Line:
                $ RogueX.FaceChange("sly",1,Eyes="leftisde")
                $ KittyX.FaceChange("sly",1,Eyes="leftisde")
                if Line == "Rogue":
                    $ KittyX.Statup("Love", 90, 2)
                    $ KittyX.Statup("Obed", 80, 4)
                    $ KittyX.Statup("Inbt", 70, 2)
                    ch_k "Я все понимаю. . ."
                else:
                    $ RogueX.Statup("Love", 90, 2)
                    $ RogueX.Statup("Obed", 80, 4)
                    $ RogueX.Statup("Inbt", 70, 2)
                    if not Player.Male:
                        ch_r "Ты просто высказала свое мнение. . ."
                    else:
                        ch_r "Ты просто высказал свое мнение. . ."
            ". . .":
                    pass
        $ Line = 0
        $ RogueX.FaceChange("sly",Eyes="side")
        $ KittyX.FaceChange("sly",1,Eyes="side")
        show Kitty_Sprite:
                ease 1 pos(690,100)
        $ RogueX.Offhand = 0
        "В глазах [KittyX.Name_rod] появляется решимость, и она наклоняется ближе к [RogueX.Name_dat]."
        show Kitty_Sprite at SpriteLoc(690,100)
        $ RogueX.FaceChange("sly",1,Eyes="down")
        show Kitty_Sprite:
                ease 1 pos(540,170)
        "Она осторожно наклоняется все ближе и ближе к соску [RogueX.Name_rod]."
        show Kitty_Sprite at SpriteLoc(540,170)
        $ KittyX.FaceChange("tongue",2,Eyes="closed")
        $ Player.Statup("Focus",80, 3)
        $ RogueX.Statup("Lust", 80, 3)
        $ KittyX.Statup("Lust", 80, 3)
        "Как только ее дыхание касается соска [RogueX.Name_rod], [KittyX.Name] высовывает кончик язычка и проводит им по нему."
        $ KittyX.Offhand = 'suck girl breasts'
        $ RogueX.FaceChange("kiss",2)
        $ Player.Statup("Focus",80, 3)
        $ RogueX.Statup("Lust", 80, 3)
        $ KittyX.Statup("Lust", 80, 3)
        "[RogueX.Name] резко закатывает глаза, после чего [KittyX.Name] с улыбкой начинает работать язычком более энергично."
        $ KittyX.FaceChange("sly",1,Eyes="side")
        $ Player.Statup("Focus",80, 3)
        $ RogueX.Statup("Lust", 80, 3)
        $ KittyX.Statup("Lust", 80, 3)
        $ KittyX.Offhand = 0
        show Kitty_Sprite:
                ease 1 pos(KittyX.SpriteLoc,50)
        "Когда [KittyX.Name] уже готова жадно всосать сосок [RogueX.Name_rod], она вдруг одумывается и отстраняется."
        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc,50)
        $ RogueX.FaceChange("sly",1,Eyes="side")
        $ RogueX.GirlLikeUp(KittyX,25)
        $ KittyX.GirlLikeUp(RogueX,25)
        show Kitty_Sprite:
                ease 1 pos(600,50)
        "[RogueX.Name_dat] требуется мгновение, чтобы отдышаться, затем она притягивает [KittyX.Name_vin] ближе к себе."
        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc,50)
        $ RogueX.AddWord(1,"breasts",0,0,0) #adds "breasts" to recent actions
        $ RogueX.AddWord(1,0,0,0,"KittyTits")
        $ RogueX.DrainWord("KittyKiss",0,0,0,1) #removes this from history
        return
#End Rogue_Kitty_Breasts: / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Rogue_Kitty_Pussy:
        # called from Rogue_and_Kitty if she wants to discuss her pussy
        $ RogueX.FaceChange("sly",Eyes="side")
        $ KittyX.FaceChange("sly",Eyes="down")
        $ Player.Statup("Focus",90, 3)
        $ RogueX.Statup("Lust", 90, 3)
        $ KittyX.Statup("Lust", 90, 3)
        if RogueX.Pubes:
                ch_k "У тебя[KittyX.like]кое-какая милая маленькая полосочка. . ."
        else:
                #no pubes
                ch_k "У тебя[KittyX.like]была кое-какая милая маленькая полосочка. . ."
        $ RogueX.FaceChange("smile",2,Eyes="side")
        ch_r "Ты пялилась на мой лобок?"
        $ KittyX.FaceChange("smile",2,Eyes="side",Brows="surprised")
        ch_k "Нууу, я не могла ничего с собой поделать!"
        ch_r "Ха! Думаю, я не могу винить тебя за это, сладенькая."
        $ RogueX.FaceChange("sly",1,Eyes="side")
        $ KittyX.FaceChange("sly",1,Eyes="side")
        $ Player.Statup("Focus",90, 3)
        $ RogueX.Statup("Lust", 90, 3)
        $ KittyX.Statup("Lust", 90, 3)
        ch_r "Должна сказать,"
        $ KittyX.FaceChange("sly",2,Eyes="leftside")
        ch_r "Я тоже не могла не обратить внимания на твою маленькую кисоньку."
        ch_k ". . ."
        $ KittyX.FaceChange("sly",1,Eyes="side")
        ch_k "Мне. . . всегда хотелось посмотреть, что у тебя. . . там . . . поближе. . ."

        if "les Kitty" not in RogueX.History:
                ch_r "Ты все еще хочешь этого, сладенькая?"
                ch_k ". . ."
        else:
                #some experience
                ch_r "Да? Хочешь еще раз взглянуть?"

        $ Partner = KittyX
        $ RogueX.GirlLikeUp(KittyX,20)
        $ KittyX.GirlLikeUp(RogueX,20)
        $ Player.Statup("Focus",90, 3)
        $ RogueX.Statup("Lust", 90, 3)
        $ KittyX.Statup("Lust", 90, 3)
        ch_k "Думаю, ты знаешь мой ответ."

        if RogueX.PantiesNum() or RogueX.PantsNum() or RogueX.HoseNum():
                $ RogueX.Upskirt = 1
                $ RogueX.PantiesDown = 1
                "[RogueX.Name] показывает свою киску."
                call Girl_First_Bottomless(RogueX,1)
        if not RogueX.Pubes:
                $ RogueX.FaceChange("sly",Eyes="side")
                $ KittyX.FaceChange("sly",Eyes="side")
                menu:
                    ch_k "Знаешь, я очень скучаю по той полоске. . ."
                    "Извини.":
                            $ RogueX.FaceChange("sad",2,Eyes="leftside")
                            ch_r "Ага, извини нас за это, сладенькая."
                    "Честно говоря, я тоже.":
                            $ RogueX.FaceChange("confused",2)
                            ch_r "Правда? Тогда, возможно, пришло время перемен. . ."
                            $ RogueX.Todo.append("pubes")
                            $ RogueX.PubeC = 6
                    "Без нее мне больше нравится.":
                            $ RogueX.FaceChange("sad",2,Eyes="leftside")
                            ch_r "Ага, извини, сладенькая."
                    ". . .":
                            $ RogueX.FaceChange("sad",2,Eyes="leftside")
                            ch_r "Извини за это, сладенькая."
        $ RogueX.FaceChange("sly",Eyes="down")
        $ KittyX.FaceChange("sly",2,Eyes="side")
        $ Player.Statup("Focus",90, 3)
        $ RogueX.Statup("Lust", 90, 3)
        $ KittyX.Statup("Lust", 90, 3)
        show Kitty_Sprite:
                ease 1 pos(600,350)
        "[KittyX.Name], немного нервничая, медленно наклоняется, оказываясь на уровне талии [RogueX.Name_rod]."

        call Rogue_Kitty_AboutZero
        if "approved" not in RogueX.RecentActions:
                return

        show Kitty_Doggy_Animation at SpriteLoc(750,350) zorder 150:
                zoom .8
        hide Kitty_Sprite
        if RogueX.Pubes:
                "Она поднимает руку и медленно проводит большим пальцем по кустику [RogueX.Name_rod]."
                "Она осторожно приглаживает волосы, чтобы лучше рассмотреть киску [RogueX.Name_rod]."
        else:
                "Она поднимает руку и медленно проводит большим пальцем вдоль киски [RogueX.Name_rod]."
                "Кончики ее пальцев нежно поглаживают упругую плоть."
        show Kitty_Doggy_Animation:
                ease 1 pos (730,350)
        "Пока [KittyX.Name] занята этим, вы видите, как она наклоняется к киске [RogueX.Name_rod] все ближе и ближе, пока не задевает ее носом."
        show Kitty_Doggy_Animation:
                pos (730,350)
        ch_r "Теперь ты достаточно близко, сладенькая?"
        ch_k ". . ."
        $ RogueX.FaceChange("sly",2,Eyes="down")
        $ Player.Statup("Focus",90, 3)
        $ RogueX.Statup("Lust", 90, 3)
        $ KittyX.Statup("Lust", 90, 3)
        if KittyX.Legs or KittyX.Panties:
            $ Line = get_clothing_name(KittyX.Panties_key, vin) if not KittyX.Legs else get_clothing_name(KittyX.Legs_key, vin)
            menu:
                "Спустить с [KittyX.Name] [Line]":
                        $ KittyX.FaceChange("sly",1,Eyes="leftside")
                        $ KittyX.PantiesDown = 1
                        $ KittyX.Upskirt = 1
                        $ KittyX.Statup("Obed", 90, 3)
                        $ KittyX.Statup("Inbt", 90, 2)
                        "Вы протягиваете руку и спускаете с [KittyX.Name] [Line]."
                        ch_k "Нравится увиденное, [KittyX.Petname]?"
                        call Girl_First_Bottomless(KittyX,1)
                        $ RogueX.FaceChange("smile",1,Eyes="down")
                        ch_r "Хех."
                        $ RogueX.FaceChange("sly",1,Eyes="down")
                        ch_r "Ну так что. . ."
                "Ничего не делать.":
                        pass
        ch_r "Хочешь посмотреть еще. . . поближе?"
        $ KittyX.FaceChange("sly",2,Eyes="closed")
        ch_k ". . ."
        ch_k "-ага."
        ch_r "Тогда не стесняйся."
        $ RogueX.FaceChange("sly",Eyes="side")
        $ KittyX.FaceChange("tongue",Eyes="closed")
        $ KittyX.Offhand = 'lick girl pussy'
        if Trigger2:
                $ Player.Statup("Focus",99, 3)
        $ Player.Statup("Focus",90, 5)
        $ RogueX.Statup("Lust", 90, 5)
        $ KittyX.Statup("Lust", 90, 5)
        "[KittyX.Name] делает последний вдох и проводит язычком по клитору [RogueX.Name_rod]."
        $ RogueX.FaceChange("sly",Eyes="closed")
        "[RogueX.Name] слегка вздрагивает от такого, но вскоре успокаивается и начинает получать удовольствие."
        $ RogueX.Offhand = 'fondle breasts'
        if Trigger2:
                $ Player.Statup("Focus",99, 3)
        $ Player.Statup("Focus",95, 3)
        $ RogueX.Statup("Lust", 99, 3)
        $ KittyX.Statup("Lust", 99, 3)
        "[KittyX.Name] продолжает нежно лизать ее киску, в то время как [RogueX.Name] начинает играть со своими сиськами."
        if "les Kitty" not in RogueX.History:
                ch_r "Ты. . . на удивление хороша, сладенькая. . ."
        else:
                ch_r "Мне всегда нравилось, какая ты талантливая. . ."
        $ Trigger = 'lick pussy' #check to make sure this works
        $ KittyX.Offhand = "fondle pussy"
        $ RogueX.GirlLikeUp(KittyX,50)
        $ KittyX.GirlLikeUp(RogueX,50)
        if Trigger2:
                $ Player.Statup("Focus",99, 3)
        $ Player.Statup("Focus",99, 3)
        $ RogueX.Statup("Lust", 99, 3)
        $ KittyX.Statup("Lust", 95, 3)
        if RogueX.Pubes:
                "[KittyX.Name] что-то бормочет в влажные заросли [RogueX.Name_rod] и начинает ублажать себя пальцами."
        else:
                "[KittyX.Name] что-то бормочет в мокрую промежность [RogueX.Name_rod] и начинает ублажать себя пальцами."
        if Trigger2:
                $ Player.Statup("Focus",99, 3)
        $ Player.Statup("Focus",99, 5)
        $ RogueX.Statup("Lust", 200, 5)
        $ KittyX.Statup("Lust", 99, 5)
        "Через довольно продолжительное время, кажется, что они обе в шаге от оргазма."
        $ RogueX.DrainWord("gonnafap",1,1,0)  #removes these flags when you've had sex
        $ RogueX.DrainWord("wannafap",1,1,0)
        call Punch

        $ RogueX.FaceChange("surprised",2)
        $ RogueX.Offhand = 0 #stops fondling breast
        ch_r "Ох!"
        $ RogueX.FaceChange("sexy",2,Eyes="closed")

        $ RogueX.Thirst = int(RogueX.Thirst/2)
        $ RogueX.Thirst -= 5
        $ RogueX.OCount += 1
        $ RogueX.Lust = 30 if "hotblooded" in RogueX.Traits else 0
        $ RogueX.Lust += (RogueX.OCount * 5)
        $ RogueX.Lust = 60 if RogueX.Lust >= 60 else RogueX.Lust
        $ RogueX.Statup("Inbt", 50, 1)
        $ RogueX.Statup("Inbt", 70, 1)
        $ Player.Statup("Focus",99, 5)
        $ RogueX.Statup("Lust", 99, 2)
        $ KittyX.Statup("Lust", 200, 5)
        "В ответ [KittyX.Name] начинает лихорадочно лизать ее киску, пока сама не переступает черту."

        $ KittyX.DrainWord("gonnafap",1,1,0)  #removes these flags when you've had sex
        $ KittyX.DrainWord("wannafap",1,1,0)
        call Punch

        $ KittyX.FaceChange("surprised",2,Eyes="closed")
        ch_k "Мммм!"
        $ KittyX.Offhand = 0    #stops masturbating
        $ Trigger = 0           #stops licking pussy

        $ KittyX.Thirst = int(KittyX.Thirst/2)
        $ KittyX.Thirst -= 5
        $ KittyX.OCount += 1
        $ KittyX.Lust = 30 if "hotblooded" in KittyX.Traits else 0
        $ KittyX.Lust += (KittyX.OCount * 5)
        $ KittyX.Lust = 60 if KittyX.Lust >= 60 else KittyX.Lust
        $ KittyX.Statup("Inbt", 50, 1)
        $ KittyX.Statup("Inbt", 70, 1)
        $ Player.Statup("Focus",200, 20)
        if Trigger2:
            "Вы и сами примерно в таком же состоянии."
            menu:
                "Плыть по течению.":
                        $ KittyX.Spunk.append("back")
                        call Punch
                        $ Player.Focus = 0
                        "Вы кончаете на спину [KittyX.Name_rod]."
                        $ KittyX.Statup("Love", 90, 2)
                        $ KittyX.Statup("Obed", 90, 5)
                        $ KittyX.Statup("Inbt", 70, 2)
                "Постараться сдержаться.":
                        pass
        if Player.Focus > 80:
            #if you hadn't cum yet
            $ RogueX.FaceChange("sly",1,Eyes="down")
            $ KittyX.FaceChange("sly",1,Eyes="stunned")
            ch_r "Ах, [RogueX.Petname], да ты, похоже, вот-вот лопнешь от возбуждения."
            ch_r "Позволь мне помочь тебе."
            if "cockout" not in Player.RecentActions:
                    $ Player.RecentActions.append("cockout")
                    "[RogueX.Name] тянется вниз и расстегивает молнию на ваших брюках."
            $ RogueX.Layer = 160
            call Rogue_BJ_Launch
            $ Speed = 5
            $ RogueX.Spunk.append("mouth")
            $ RogueX.Spunk.append("chin")
            $ Player.Focus = 0
            $ RogueX.FaceChange("sly",1,Eyes="closed")
            $ RogueX.Statup("Lust", 60, 5)
            $ KittyX.Statup("Lust", 60, 5)
            if Player.Male:
                    "Она наклоняется и берет ваш член в рот, после чего вы кончаете в нее."
            else:
                    "Она наклоняется и прижимается ртом к вашей промежности, после чего вы кончаете."
            $ Speed = 0
            $ RogueX.Layer = 100
            call Rogue_BJ_Reset
            $ Player.Sprite = 0
            show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 70:
                    xzoom -1
        $ RogueX.FaceChange("sly",Eyes="side")
        $ KittyX.FaceChange("sly",2,Eyes="leftside")
        $ KittyX.Statup("Obed", 90, 3)
        $ KittyX.Statup("Inbt", 80, 3)
        ch_r "Слушай, [KittyX.Name], все было супер!"
        if "mouth" in RogueX.Spunk:
                $ RogueX.Spunk.append("mouth")
        if not RogueX.SeenPeen or not KittyX.SeenPeen:
                $ RogueX.FaceChange("sly",Eyes="down")
                $ KittyX.FaceChange("surprised",2,Eyes="down")
                ch_r "О, посмотрите-ка, кто у нас здесь есть. . ."
                call Seen_First_Peen(RogueX,KittyX)
        $ RogueX.FaceChange("sly",Eyes="side")
        $ KittyX.FaceChange("sly",Eyes="side")
        hide Kitty_Doggy_Animation
        show Kitty_Sprite at SpriteLoc(550,350) zorder 75:
                pos (550,350)
        if "les Kitty" not in RogueX.History:
                ch_r "Я ужасно жалею, что мы не смогли заняться этим раньше. . ."
        else:
                ch_r "Я никогда не устану заниматься этим с тобой, сладенькая. . ."
        $ RogueX.FaceChange("sly")
        $ RogueX.Statup("Love", 200, 5)
        $ RogueX.Statup("Obed", 80, 4)
        $ KittyX.Statup("Love", 90, 4)
        $ KittyX.Statup("Obed", 80, 5)
        show Kitty_Sprite:
                ease 1 pos (600,50)
        if "touch" in RogueX.Traits:
                ch_r "И без твоей помощи, [RogueX.Petname], мы бы не справились."
        else:
                ch_r "И мы не смогли бы прийти к этому, [RogueX.Petname], если бы не ты."
        show Kitty_Sprite at SpriteLoc(600,50)
        $ KittyX.FaceChange("sly",2)
        menu:
            "Да не за что.":
                    $ KittyX.FaceChange("smile")
                    $ RogueX.Statup("Love", 200, 3)
                    $ KittyX.Statup("Love", 90, 3)
                    ch_k "Ага, спасибо, [KittyX.Petname]."
            "Не забывайте об этом.":
                    $ KittyX.FaceChange("sly",2)
                    $ RogueX.Statup("Love", 80, -2)
                    $ RogueX.Statup("Obed", 60, 5)
                    $ KittyX.Statup("Obed", 60, 5)
                    ch_k "Ага, не забудем. . ."
                    $ RogueX.Statup("Obed", 200, 3)
                    $ KittyX.Statup("Obed", 90, 5)
            "Это того стоило.":
                    $ RogueX.Statup("Inbt", 80, 3)
                    $ KittyX.Statup("Love", 90, 2)
                    $ KittyX.Statup("Inbt", 70, 5)
                    $ KittyX.FaceChange("smile")
                    ch_k "Хихи."
            ". . .":
                    pass
        $ RogueX.AddWord(1,"pussy",0,0,0) #adds "breasts" to recent actions
        $ RogueX.AddWord(1,0,0,0,"KittyPuss")
        $ RogueX.DrainWord("KittyTits",0,0,0,1) #removes this from history
        # leads to ch_r "Anyways, [KittyX.Name], I gotta say, I always could feel your eyes on me."
        return
#End Rogue_Kitty_Pussy: / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Rogue_Kitty_AboutZero:
        # called from Rogue_and_Kitty if she wants to do stuff
        if "touch" not in RogueX.Traits:
                call Rogue_Kitty_AboutZeroHelp
                return
        if "approved" in RogueX.RecentActions:
                #checks to see if Kitty cares what you think.
                if ApprovalCheck(KittyX, 800, "O"):
                        $ KittyX.FaceChange("sly",Brows="sad")
                        ch_k "[KittyX.Petname], ты не против?"
                else:
                        menu:
                            "[[Продолжать смотреть]":
                                    pass
                            "Вам лучше прекратить.":
                                    $ RogueX.FaceChange("angry",2)
                                    $ KittyX.FaceChange("sad",2)
                                    $ RogueX.Statup("Love", 90, -3)
                                    $ RogueX.Statup("Obed", 90, 3)
                                    $ KittyX.Statup("Love", 80, -2)
                                    $ KittyX.Statup("Obed", 90, 4)
                                    ch_r "Вот можешь ты все испортить."
                                    $ RogueX.FaceChange("sad",1)
                                    $ KittyX.FaceChange("sad",1)
                                    jump Rogue_Kitty_End
                        call JackCheck
                        return
        else:
                $ KittyX.FaceChange("sly",2,Brows="sad")
                ch_k "А что насчет [Player.Name_rod]?"
                $ RogueX.FaceChange("sly")
                ch_r "Ага, [RogueX.Petname], что ты на это скажешь?"
        menu:
            extend ""
            "Я не против.":
                    $ RogueX.FaceChange("smile")
                    $ KittyX.FaceChange("smile")
                    $ RogueX.Statup("Love", 90, 3)
                    $ KittyX.Statup("Love", 90, 3)
                    ch_r "Это я и хотела услышать!"
                    $ RogueX.FaceChange("sly",Eyes="side")
                    $ KittyX.FaceChange("sly",Eyes="side")
                    $ RogueX.Statup("Obed", 80, 2)
                    $ KittyX.Statup("Obed", 80, 2)
                    ch_r "Ну, раз никто не против. . ."
            "Я вам разрешаю.":
                    if ApprovalCheck(RogueX, 500, "O"):
                            $ RogueX.FaceChange("smile")
                            $ KittyX.FaceChange("smile")
                            $ RogueX.Statup("Obed", 60, 2)
                            $ RogueX.Statup("Obed", 80, 4)
                            $ KittyX.Statup("Obed", 60, 3)
                            $ KittyX.Statup("Obed", 90, 5)
                            ch_r "Рада слышать."
                    else:
                            $ RogueX.FaceChange("sly",Brows="angry")
                            $ KittyX.FaceChange("smile")
                            $ RogueX.Statup("Love", 90, -3)
                            $ RogueX.Statup("Inbt", 70, 3)
                            $ KittyX.Statup("Love", 80, -2)
                            $ KittyX.Statup("Obed", 80, 5)
                            ch_r "О, правда что ли?"
                            $ RogueX.Statup("Obed", 80, 5)
            "Прекратите флиртовать.":
                    #high obit"
                    if ApprovalCheck(RogueX, 700, "O") or ApprovalCheck(KittyX, 700, "O"):
                            $ RogueX.FaceChange("sad",2,Eyes="leftside")
                            $ KittyX.FaceChange("sad",2,Eyes="leftside")
                            $ RogueX.Statup("Love", 80, -2)
                            $ RogueX.Statup("Obed", 60, 3)
                            $ KittyX.Statup("Love", 80, -2)
                            $ KittyX.Statup("Obed", 60, 3)
                            ch_r "Пожалуй, это может подождать. . ."
                            $ RogueX.FaceChange("sad",1,Eyes="side")
                            $ KittyX.FaceChange("sad",1,Eyes="side")
                            $ RogueX.Statup("Obed", 80, 3)
                            $ KittyX.Statup("Obed", 80, 3)
                            jump Rogue_Kitty_End
                    elif ApprovalCheck(RogueX, 500, "O") or ApprovalCheck(KittyX, 500, "O"):
                            #mid obit"
                            $ RogueX.FaceChange("angry",1)
                            $ KittyX.FaceChange("sad",2,Eyes="side")
                            $ RogueX.Statup("Love", 80, -3)
                            $ RogueX.Statup("Obed", 60, 3)
                            $ KittyX.Statup("Love", 80, -3)
                            $ KittyX.Statup("Obed", 60, 3)
                            ch_r "Вот можешь ты все настроение испортить. . ." #ends scene
                            $ RogueX.Statup("Obed", 80, 3)
                            $ KittyX.Statup("Obed", 80, 3)
                            jump Rogue_Kitty_End
                    else:
                            #low obit"
                            $ RogueX.FaceChange("angry")
                            $ KittyX.FaceChange("surprised",2,Eyes="side")
                            $ RogueX.Statup("Love", 80, -5)
                            $ RogueX.Statup("Inbt", 70, 5)
                            $ KittyX.Statup("Love", 80, -5)
                            $ KittyX.Statup("Inbt", 70, 5)
                            ch_r "Ладно, мы тут и без тебя разберемся. . ." #kicks you out.
                            $ RogueX.Statup("Obed", 80, 3)
                            $ KittyX.Statup("Obed", 80, 3)
                            if bg_current == "bg player":
                                    "Она выгоняет вас из комнаты, и вы ненадолго отправляетесь на площадь."
                                    $ bg_current = "bg campus"
                            else:
                                    "Она выгоняет вас из комнаты, и вы возвращаетесь к себе."
                                    $ bg_current = "bg player"
                            $ RogueX.FaceChange("normal",0)
                            $ KittyX.FaceChange("normal",0)
                            $ RogueX.Loc = "bg rogue"
                            $ KittyX.Loc = "bg rogue"
                            jump Misplaced

            ". . .":
                            $ RogueX.FaceChange("sly",1,Eyes="side")
                            $ KittyX.FaceChange("sly",1,Eyes="side")
                            $ RogueX.Statup("Inbt", 80, 2)
                            $ KittyX.Statup("Inbt", 80, 2)
                            ch_r "Как я понимаю, значит, ты \"не против\"?"
        $ RogueX.AddWord(1,"approved",0,0,0) #adds "approved" to recent actions for both girls
        $ Partner = KittyX
        call JackCheck
        return
#End  Rogue_Kitty_AboutZero: / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Rogue_Kitty_AboutZeroHelp:
        # called from "Rogue_Kitty_AboutZero" if Rogue_and_Kitty if she wants to do stuff, but needs your help
        if "touch" in RogueX.Traits or "approved" in RogueX.RecentActions:
                # if she has her powers off or you already agreed, return
                return
        $ KittyX.FaceChange("sly",2,Brows="sad")
        ch_k "[Player.Name]. . . можешь помочь?"
        $ RogueX.FaceChange("sly",1)
        ch_r "Ага, [RogueX.Petname], ты не против?"
        menu:
            extend ""
            "Конечно.":
                    $ RogueX.FaceChange("smile",1)
                    $ KittyX.FaceChange("smile",1)
                    $ RogueX.Statup("Love", 90, 3)
                    $ KittyX.Statup("Love", 90, 3)
                    ch_r "Это я и хотела услышать!"
                    $ RogueX.FaceChange("sly",Eyes="side")
                    $ KittyX.FaceChange("sly",Eyes="side")
                    $ RogueX.Statup("Obed", 80, 2)
                    $ KittyX.Statup("Obed", 80, 2)
                    ch_r "Ну, раз мы все уладили. . ."
            "Наверное, да.":
                    #high obit"
                    $ RogueX.FaceChange("sly")
                    $ KittyX.FaceChange("confused")
                    $ RogueX.Statup("Love", 80, 3)
                    $ KittyX.Statup("Love", 80, 3)
                    ch_r "Что-то не слышно в твоем голосе особого энтузиазма. . ."
                    $ RogueX.Statup("Obed", 80, 2)
                    $ KittyX.Statup("Obed", 80, 2)
                    $ RogueX.FaceChange("sly",Eyes="side")
                    $ KittyX.FaceChange("sly",Eyes="side")
            "Не хочу.":
                    #high inbt"
                    if ApprovalCheck(RogueX, 500, "I") and ApprovalCheck(KittyX, 500, "I"):
                        $ RogueX.FaceChange("sad",1)
                        $ KittyX.FaceChange("sad",2)
                        $ RogueX.Statup("Love", 90, -2)
                        $ RogueX.Statup("Obed", 80, 2)
                        $ KittyX.Statup("Love", 90, -2)
                        $ KittyX.Statup("Obed", 80, 2)
                        ch_r "Да ладно тебе, выручи милых девушек. . ."
                        ch_k "Ну пожалуйста?"
                        menu:
                            extend ""
                            "Эх, ладно.":
                                    $ RogueX.FaceChange("smile")
                                    $ KittyX.FaceChange("smile",1)
                                    $ RogueX.Statup("Love", 90, 2)
                                    $ KittyX.Statup("Love", 90, 2)
                                    if not Player.Male:
                                        ch_r "Видишь, она настоящая леди."
                                    else:
                                        ch_r "Видишь, он настоящий джентльмен."
                                    $ RogueX.Statup("Obed", 80, 1)
                                    $ KittyX.Statup("Obed", 80, 1)
                            "Нет, прекращайте.":
                                    $ RogueX.Statup("Love", 80, -1)
                                    $ RogueX.Statup("Obed", 80, 1)
                                    $ KittyX.Statup("Love", 80, -1)
                                    $ KittyX.Statup("Obed", 80, 1)
                                    ch_r "Эх, жаль, что мы не пришли к согласию. . ." #ends scene
                                    jump Rogue_Kitty_End

                            "Тогда дайте мне тоже поучаствовать.":
                                    $ RogueX.FaceChange("sly")
                                    $ KittyX.FaceChange("sly",1)
                                    $ RogueX.Statup("Love", 90, 2)
                                    $ RogueX.Statup("Obed", 80, 2)
                                    $ KittyX.Statup("Love", 90, 2)
                                    $ KittyX.Statup("Obed", 80, 2)
                                    ch_r "Думаю, это можно устроить. . ."
                                    $ RogueX.FaceChange("sly",Eyes="side")
                                    $ KittyX.FaceChange("sly",Eyes="side")
                                    ch_r "Только сначала я бы хотела посмотреть, чем у нас с ней все закончится."
                                    $ RogueX.AddWord(1,"threeup",0,0,0) #adds "approved" to recent actions
                    else:
                                    $ RogueX.Statup("Love", 80, -1)
                                    $ RogueX.Statup("Obed", 80, 1)
                                    $ KittyX.Statup("Love", 80, -1)
                                    $ KittyX.Statup("Obed", 80, 1)
                                    ch_r "Эх, жаль, что мы не пришли к согласию. . ." #ends scene
                                    jump Rogue_Kitty_End



            ". . .":
                        ch_r "Нам нужен ответ, [RogueX.Petname]."
                        menu:
                            extend ""
                            "Эх, ладно, я вам помогу.":
                                    $ RogueX.FaceChange("smile")
                                    $ KittyX.FaceChange("smile",1)
                                    $ RogueX.Statup("Love", 90, 2)
                                    $ KittyX.Statup("Love", 90, 2)
                                    if not Player.Male:
                                        ch_r "Видишь, она настоящая леди."
                                    else:
                                        ch_r "Видишь, он настоящий джентльмен."
                                    $ RogueX.Statup("Obed", 80, 1)
                                    $ KittyX.Statup("Obed", 80, 1)
                            "Вам лучше прекратить.":
                                    $ RogueX.FaceChange("sad",1)
                                    $ KittyX.FaceChange("sad",2)
                                    $ RogueX.Statup("Love", 80, -1)
                                    $ RogueX.Statup("Obed", 80, 1)
                                    $ KittyX.Statup("Love", 80, -1)
                                    $ KittyX.Statup("Obed", 80, 1)
                                    ch_r "Эх, жаль, что мы не пришли к согласию. . ." #ends scene
                                    jump Rogue_Kitty_End
                            "Тогда дайте мне тоже поучаствовать.":
                                    $ RogueX.FaceChange("sly")
                                    $ KittyX.FaceChange("sly",1)
                                    $ RogueX.Statup("Love", 90, 2)
                                    $ RogueX.Statup("Obed", 80, 2)
                                    $ KittyX.Statup("Love", 90, 2)
                                    $ KittyX.Statup("Obed", 80, 2)
                                    ch_r "Думаю, это можно устроить. . ."
        "Вы воздействуете своей силой на небольшую область, чтобы блокировать силы [RogueX.Name_rod]."
        $ Partner = KittyX
        $ RogueX.AddWord(1,"approved",0,0,0) #adds "approved" to recent actions for both girls
        call JackCheck
        return

label Rogue_and_Kitty_Redux:
        #this scene is about Rogue and Kitty talking, after the first time
        #Triggered in Study. If Rogue has "KittyPuss" in her history then she's cleared it.
        #If Rogue has "KittyTits" then she's done the tits part, "KittyKiss" she's done the kissing part
        #If she has none of these checks, it plays through from the start

        $ Line = 0
        call Shift_Focus(RogueX)
        show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 70:
                xzoom -1
        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder 75

        ch_p "В тот раз, когда вы с [KittyX.Name_tvo] говорили о прикосновениях к тебе. . ."
        $ RogueX.FaceChange("sly")
        $ KittyX.FaceChange("sly",1)
        if "KittyRedux" in RogueX.DailyActions:
                #you've done this bit today
                ch_r "[RogueX.Petname], мы немного устали разыгрывать эту сценку. . ."
                ch_k "Может, завтра?"
                return
        elif "KittyRedux" in RogueX.History:
                #you've done this bit too
                ch_r "О да, [RogueX.Petname], давай сделаем это."
        else:
                #first retry
                ch_r "Да, [RogueX.Petname]?"
                $ RogueX.FaceChange("sly")
                $ KittyX.FaceChange("sly",2)
                $ RogueX.Statup("Inbt", 90, 3)
                $ RogueX.Statup("Obed", 80, 2)
                $ KittyX.Statup("Inbt", 90, 3)
                $ KittyX.Statup("Obed", 80, 2)
                ch_r "Тебе понравилось за нами наблюдать?"
                menu:
                    extend ""
                    "Ага.":
                        $ RogueX.Statup("Love", 90, 2)
                        $ KittyX.Statup("Love", 90, 2)
                        $ KittyX.FaceChange("sly",2,Eyes="side")
                    "Типа того.":
                        $ RogueX.FaceChange("confused")
                        $ KittyX.FaceChange("confused",1)
                        $ RogueX.Statup("Love", 90, -1)
                        $ RogueX.Statup("Obed", 80, 2)
                        $ KittyX.Statup("Love", 90, -1)
                        $ KittyX.Statup("Obed", 80, 2)
                    "Да не особо.":
                        $ RogueX.FaceChange("confused")
                        $ KittyX.FaceChange("confused",1)
                        $ RogueX.Statup("Love", 90, -2)
                        $ RogueX.Statup("Obed", 80, 2)
                        $ KittyX.Statup("Love", 90, -2)
                        $ KittyX.Statup("Obed", 80, 2)
                        ch_r "Ох, ну ладно. . ."
                        return
                    ". . .":
                        $ RogueX.Statup("Obed", 80, 1)
                        $ KittyX.Statup("Obed", 80, 1)
                ch_r "Хочешь, мы проведем небольшую. . . \"реконструкцию\" того события?"
                menu:
                    extend ""
                    "Ага.":
                        $ KittyX.FaceChange("sly",2,Eyes="side")
                        $ RogueX.Statup("Inbt", 90, 2)
                        $ RogueX.Statup("Obed", 80, 2)
                        $ KittyX.Statup("Inbt", 90, 2)
                        $ KittyX.Statup("Obed", 80, 2)
                    "Типа того.":
                        $ RogueX.FaceChange("confused")
                        $ KittyX.FaceChange("confused",1)
                        $ RogueX.Statup("Love", 90, -1)
                        $ KittyX.Statup("Love", 90, -1)
                    "Да не особо.":
                        $ RogueX.FaceChange("confused")
                        $ KittyX.FaceChange("confused",1)
                        $ RogueX.Statup("Love", 90, -1)
                        $ RogueX.Statup("Obed", 80, 2)
                        $ KittyX.Statup("Love", 90, -1)
                        $ KittyX.Statup("Obed", 80, 3)
                        ch_r "Ох, ну ладно тогда. . ."
                        return
                    ". . .":
                        pass
                ch_r "Что скажешь, [KittyX.Name]?"
                $ KittyX.FaceChange("smile",1)
                ch_k "Я за!"
        $ RogueX.FaceChange("sly")
        $ KittyX.FaceChange("sadside",1)
        ch_k "Секундочку, сейчас войду в образ. . ."
        ch_r "[KittyX.Name], к чему бы ты хотела прикоснуться. . ?"
        $ RogueX.AddWord(1,0,0,0,"KittyRedux")
        $ RogueX.AddWord(1,0,"KittyRedux",0,0) #adds "KittyRedux" to daily actions
        call Rogue_Kitty_Kiss
        #if you'd done this before. . .
        "Пока вы занимаетесь, [RogueX.Name] замечает, что [KittyX.Name] пристально смотрит на ее грудь. . ."
        call Rogue_Kitty_Breasts
        $ RogueX.FaceChange("sly",1,Eyes="side")
        $ KittyX.FaceChange("sexy",1,Eyes="side")
        ch_r "Значит. . . тебя заинтересовала моя грудь. . ."
        ch_r "А -еще- что-нибудь. . . тебе интересно?"
        $ KittyX.FaceChange("sexy",2,Eyes="down")
        ch_k "Нууу. . ."
        ch_r "М?"
        ch_r "Похоже, что да. . ."
        call Rogue_Kitty_Pussy
        jump Rogue_Kitty_End
#End  Rogue_Kitty_AboutZeroHelp: / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# End Rogue_and_Kitty Dialogue / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Rogue_69_Intro:
        if "69" in RogueX.History:
                return
        if Trigger == "lick pussy" and RogueX.LickP:
                if RogueX.Blow or RogueX.CUN or (ApprovalCheck(RogueX, 1300) and RogueX.SeenPeen):
                        #if licking pussy but have gotten blowjob
                        $ RogueX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_r "Слушай, если ты хочешь сделать мне приятное, я должна отплатить тебе тем же. . ."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        if "cockout" not in Player.RecentActions:
                                $ Player.RecentActions.append("cockout")
                                if Player.Male:
                                        "Она вытаскивает ваш член и начинает его сосать."
                                else:
                                        "Она обнажает вашу киску и начинает ее лизать."
                        else:
                                if Player.Male:
                                        "Она хватает ваш член и располагается над ним."
                                else:
                                        "Она начинает лизать вашу киску."
                        $ RogueX.Pose = "69"
                        call Rogue_BJ_Launch
                        ch_r "Не хочешь начать. . ?"
                        menu:
                            extend ""
                            "Приступить к работе":
                                    $ Trigger2 = "lick pussy"
                                    $ RogueX.Statup("Love", 95, 3)
                                    $ RogueX.Statup("Inbt", 70, 2)
                                    $ RogueX.Statup("Inbt", 90, 1)
                                    ch_r "Спасибо, [RogueX.Petname]."
                            "Расслабиться, оставив ее киску без внимания":
                                    $ RogueX.Statup("Love", 80, -8)
                                    $ RogueX.Statup("Obed", 80, 3)
                                    $ RogueX.Statup("Obed", 90, 1)
                                    $ RogueX.Statup("Inbt", 70, -1)
                                    ch_r "А я-то надеялась. . ."
                        $ Situation = "69"
                        call SexAct("blow") # call Rogue_SexAct("blow")
                        $ renpy.pop_call() #causes it to skip past the Escalation
                        $ renpy.pop_call() #causes it to skip past the last activity
        elif (Trigger == "blow" or Trigger == "cun") and (RogueX.Blow or RogueX.CUN):
                        #if licked pussy
                        $ RogueX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_r "Слушай, пока я занята тобой. . ."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        $ RogueX.Pose = "69"
                        call Rogue_BJ_Launch
                        if Player.Male:
                                ch_r "-не мог бы ты тоже позаботиться обо мне. . ?"
                        else:
                                ch_r "-не могла бы ты тоже позаботиться обо мне. . ?"
                        menu:
                            extend ""
                            "Приступить к работе":
                                    $ Trigger2 = "lick pussy"
                                    $ RogueX.Statup("Love", 95, 3)
                                    $ RogueX.Statup("Inbt", 70, 2)
                                    $ RogueX.Statup("Inbt", 90, 1)
                                    ch_r "Спасибо, [RogueX.Petname]."
                                    if not RogueX.LickP:
                                        $ RogueX.LickP += 1
                            "Расслабиться, оставив ее киску без внимания":
                                    $ RogueX.Statup("Love", 80, -5)
                                    $ RogueX.Statup("Obed", 80, 3)
                                    $ RogueX.Statup("Obed", 90, 1)
                                    $ RogueX.Statup("Inbt", 70, -1)
                                    ch_r "А я-то надеялась. . ."
                        #returns to BJ already in progress
        return
