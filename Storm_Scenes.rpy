# start StormMeet //////////////////////////////////////////////////////////
# Check  #Storm_Update   to see what needs fixing still


#    #Activates Storm meet
#        if StormX in ActiveGirls:
#                    if bg_current == "bg classroom" and StormX.Loc == "bg teacher" and "Peter" in StormX.History and "traveling" in Player.RecentActions:
#                            #if you told her your name was Peter Parker
#                            call Storm_Peter
#                            return


#        elif "met" not in StormX.History and "met" in JeanX.History:
#                    if bg_current == "bg classroom" and "attic" not in Player.History and "traveling" in Player.RecentActions:
#                            #You hadn't asked Emma yet
#                            call StormMeetAsk
#                            return
#                    elif bg_current == "bg player" and Time_Count < 2 and 0 < StormX.Break[0] <= 101 and "traveling" in Player.RecentActions:
#                            #Break is being used as a 3-day countdown to when you are forced to meet Storm.
#                            call StormMeetWater
#                            jump Misplaced
#                    elif bg_current == "bg player" and "noise" not in Player.History:
#                            #You hadn't heard the noise yet
#                            call StormMeetPrelude
#                            return
#    #End Storm meet


label StormMeetPrelude:
    "Вы слышите скрип, доносящийся откуда-то сверху. Вы отмечаете, что в последнее время это происходит все чаще и чаще."
    "Может быть, в следующий раз, когда вы будете в аудитории, вы сможете расспросить об этом [EmmaX.Name_vin]."
    $ Player.AddWord(1,0,0,0,"noise") #adds tag to History
    return

label StormMeetAsk:
#    $ bg_current = "bg classroom"
    if EmmaX.Loc == "bg teacher":
            $ Line = "bg teacher"
    $ EmmaX.Loc = bg_current
    call CleartheRoom(EmmaX,0,1)
    call Shift_Focus(EmmaX)
    call Set_The_Scene
    if Line == "bg teacher":
            "Перед занятием вы подходите к [EmmaX.Name_dat]."
#    else:
#            "You see [EmmaX.Name], catching up on some paperwork."
    ch_p "Я слышал над своей комнатой какой-то скрип, ты знаешь, что это может быть?"
    $ EmmaX.FaceChange("confused")
    ch_e "О. . ."
    $ EmmaX.FaceChange("sly")
    ch_e "Это всего лишь местный призрак."
    menu:
        ch_e "Это всего лишь местный призрак."
        "Призрак?":
            pass
        "Что?!":
            pass
        "Ты решила пошутить?":
            $ EmmaX.FaceChange("angry")
            ch_e "Я говорю серьезно."
            $ EmmaX.FaceChange("sly")
    ch_e "Это призрак живущий на чердаке, [EmmaX.Petname]."
    menu:
        extend ""
        "Он опасен?":
            pass
        "Ох, ну ладно.":
            $ EmmaX.FaceChange("confused")
            ch_e "Ладно?"
            $ EmmaX.FaceChange("angry",Eyes="side")
            ch_e ". . ."
            $ EmmaX.Statup("Love", 70, -2)
            $ EmmaX.Statup("Obed", 50, 1)
            ch_e "Пожалуй, я ожидала, что ты выкажешь больше заинтересованности. . ."
    $ EmmaX.FaceChange("normal")
    if not Player.Male:
        ch_e "Нет, скорее всего, он не опасен, но ты, возможно, захочешь удостовериться в этом сама. . ."
    else:
        ch_e "Нет, скорее всего, он не опасен, но ты, возможно, захочешь удостовериться в этом сам. . ."
    menu:
        extend ""
        "Спасибо, что уделила мне время.":
            $ EmmaX.FaceChange("smile")
            $ EmmaX.Statup("Love", 70, 3)
            $ EmmaX.Statup("Obed", 50, 1)
            ch_e "Рада была помочь."
        "Ладно.":
            ch_e "Ага. . ."
    $ Player.AddWord(1,0,0,0,"attic") #adds tag to History
    $ StormX.Break[0] = 104 #gives you three days to go to the attic
    $ Player.History.remove("noise")
    if Line == "bg teacher":
            ch_e "Ладно, а теперь займи свободное место, занятие вот-вот начнется."
            $ EmmaX.Loc = "bg teacher"
            $ Line = 0
    return

label StormMeetWater:
    #Scene plays if you avoid the attic for three days
    "Вы входите в свою комнату и замечаете на полу какуе-то лужу."
    "Похоже, капает из трещины в потолке."
    "Похоже, что призрак на чердаке может доставить вам больше хлопот, чем говорила [EmmaX.Name]."
    menu:
        "Погнали ловить призраков!":
            "О да."
        "П-п-п-призраки?!":
            if not Player.Male:
                "Яйца в зубы и вперед!"
            else:
                "Подбери свои яйца, ты ж мужик."
    if len(Party) > 1:
            call AnyLine(Party[0],"Я думаю, мы останемся здесь.")
            call Remove_Girl(Party[0])
            call AnyLine(Party[0],"Повеселись там.")
            call Remove_Girl(Party[0])
    elif Party:
            call AnyLine(Party[0],"Я думаю, я останусь здесь.")
            call AnyLine(Party[0],"Повеселись там.")
            call Remove_Girl(Party[0])
    "Вы направились искать дверь с надписью \"Чердак. . .\""
    $ Player.AddWord(1,"water",0,0,0) #adds "water" tag to Recent
    jump StormMeet


label StormMeet:
    if Time_Count > 2:
            if "noattic" in Player.DailyActions:
                    "Ни за что, слишком стремно."
            else:
                    "Когда вы поднимаетесь по лестнице, порыв холодного ветра устремляется вниз."
                    "О, посмотрите-ка на время, возможно, стоит подгадать более раннего времени суток. . ."
            "Вы возвращаетесь в свою комнату."
            $ bg_current = "bg player"
            $ Player.AddWord(1,0,"noattic",0,0) #adds "word" tag to Daily
            jump Misplaced

    $ Player.AddWord(1,0,"Intro",0,0) #adds tag to Daily
    $ Player.History.remove("attic")
    $ bg_current = "bg storm"
    $ StormX.OutfitDay = "casual1"
    $ StormX.Outfit = "casual1"
    $ StormX.OutfitChange("casual1")
    call CleartheRoom("All",0,1)
    $ StormX.Break[0] = 0            #resets counter
    $ StormX.Loc = 0
    $ StormX.Love = 500
    $ StormX.Obed = 0
    $ StormX.Inbt = 100
    $ StormX.Petname = 0
    $ StormX.Names = ["Ororo"]
    "Вы поднимаетесь по лестнице на чердак. Как только вы достигаете верха, вы отмечаете, что воздух там очень влажный."
    call Shift_Focus(StormX)
    call Set_The_Scene
    $ StormX.Loc = "bg storm"
    $ StormX.SpriteLoc = StageCenter
    "На верху вас приветствует то, что можно назвать крытым садом. Яркий солнечный свет проникает через окна."
    #attempt a silhouette effect here by creating a mask and then masking it with Storm's sprite like the display screen

    $ StormX.OutfitChange("nude")
    $ StormX.FaceChange("normal",Eyes="side")
#    show Silhouettes onlayer black
    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc)

    show expression AlphaMask("SilhouetteBase", At("Storm_Sprite", SpriteLoc(StormX.SpriteLoc))) as mask:
        offset (390,50)#(347,65)

    "В центре комнаты стоит женщина. . ."
    hide mask with fade
#    hide Silhouettes onlayer black with fade
#    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) with fade
    "И она голая."
    $ StormX.SeenChest += 1
    $ StormX.SeenPussy += 1
    $ StormX.FaceChange("normal")
    ch_u "О, здравствуй."
    menu:
            extend ""
            "Эм. . . здравствуй?":
                    $ StormX.Statup("Love", 70, 2)
                    if not Player.Male:
                        ch_u "Да, здравствуй. Не могла бы ты представиться?"
                    else:
                        ch_u "Да, здравствуй. Не мог бы ты представиться?"

            "Привет.":
                    $ StormX.Statup("Obed", 80, 2)
                    if not Player.Male:
                        ch_u "Привет? . . Не могла бы ты представиться?"
                    else:
                        ch_u "Привет? . . Не мог бы ты представиться?"

            "Ого.":
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 5)
                    $ StormX.Statup("Inbt", 200, 5)
                    ch_u "Похоже, я произвела на тебя впечатление."
                    if not Player.Male:
                        ch_u "Не могла бы ты представиться?"
                    else:
                        ch_u "Не мог бы ты представиться?"

            ". . .":
                    $ StormX.FaceChange("perplexed")
                    ch_u "Да?"
                    $ StormX.FaceChange("normal")

    menu:
            extend ""
            "Меня зовут [Player.Name].":
                    $ StormX.Petname = Player.Name
                    $ StormX.Petname_rod = Player.Name_rod
                    $ StormX.Petname_dat = Player.Name_dat
                    $ StormX.Petname_vin = Player.Name_vin
                    $ StormX.Petname_tvo = Player.Name_tvo
                    $ StormX.Petname_pre = Player.Name_pre
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 3)
                    ch_u "Приятно познакомиться с тобой, [Player.Name]."
            "Я \"Питер Паркер.\"" if Player.Male:
                    $ StormX.Petname = "Питер"
                    $ StormX.Petname_rod = "Питера"
                    $ StormX.Petname_dat = "Питеру"
                    $ StormX.Petname_vin = "Питера"
                    $ StormX.Petname_tvo = "Питером"
                    $ StormX.Petname_pre = "Питере"
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 3)
                    ch_u "Приятно познакомиться с тобой, Питер."
            "Я \"Сью Шторм.\"" if not Player.Male:
                    $ StormX.Petname = "Сью"
                    $ StormX.Petname_rod = "Сью"
                    $ StormX.Petname_dat = "Сью"
                    $ StormX.Petname_vin = "Сью"
                    $ StormX.Petname_tvo = "Сью"
                    $ StormX.Petname_pre = "Сью"
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 3)
                    ch_u "Приятно познакомиться с тобой, Сью, мне нравится твоя фамилия."
            "Ты первая.":
                    $ StormX.FaceChange("normal")
                    $ StormX.Statup("Love", 70, -2)
                    $ StormX.Statup("Obed", 80, 5)
                    ch_u "Пожалуй, я могу удовлетворить твою просьбу. . ."

    ch_u "Меня зовут \"Ороро Манро.\" Можешь звать меня просто \"Ороро.\""
    $ StormX.Name = "Ороро"
    $ StormX.Name_rod = "Ороро"
    $ StormX.Name_dat = "Ороро"
    $ StormX.Name_vin = "Ороро"
    $ StormX.Name_tvo = "Ороро"
    $ StormX.Name_pre = "Ороро"
    $ StormX.FaceChange("sly")
    ch_s "Или \"Мисс Манро\", если ты ужасный человек."
    $ StormX.Names.append("Ms. Munroe")

    menu:
        extend ""
        "Приятно познакомиться, Ороро.":
                $ StormX.FaceChange("smile")
                $ StormX.Statup("Love", 70, 3)
        "Приятно познакомиться, Мисс Манро.":
                $ StormX.Name = "Мисс Манро"
                $ StormX.Name_rod = "Мисс Манро"
                $ StormX.Name_dat = "Мисс Манро"
                $ StormX.Name_vin = "Мисс Манро"
                $ StormX.Name_tvo = "Мисс Манро"
                $ StormX.Name_pre = "Мисс Манро"
                $ StormX.FaceChange("surprised",Eyes="closed",Mouth="sucking")
                $ StormX.Statup("Love", 70, 5)
                $ StormX.Statup("Obed", 80, 3)
                $ StormX.Statup("Inbt", 200, 2)
                ch_s "Ха-ха-ха!"
                $ StormX.FaceChange("smile")
                ch_s "Прошу, прости меня за небольшую шутку."
                ch_s "Лучше зови меня \"Ороро\"."

        "Разве у тебя нет псевдонима?":
                $ StormX.Statup("Love", 70, 2)
                $ StormX.Statup("Obed", 80, 3)
        "Ладно, круто.":
                $ StormX.Statup("Obed", 80, 2)
        ". . .":
                $ StormX.FaceChange("normal")
                ch_s "Эм. . ."

    ch_s "Я также известна под именем \"Шторм\"."
    $ StormX.Names.append("Storm")

    if StormX.Petname == "Сью":
        menu:
            extend ""
            "Ооооох, у меня такая же. . .  фамилия. . .":
                $ StormX.FaceChange("smile")
                $ StormX.Statup("Love", 70, 2)
            ". . .":
                pass
    ch_p "Ну, тогда я буду звать тебя. . ."
    menu:
            extend ""
            "Ороро.":
                    $ StormX.Name = "Ороро"
                    $ StormX.Name_rod = "Ороро"
                    $ StormX.Name_dat = "Ороро"
                    $ StormX.Name_vin = "Ороро"
                    $ StormX.Name_tvo = "Ороро"
                    $ StormX.Name_pre = "Ороро"

            "Мисс Манро.":
                if StormX.Name != "Мисс Манро":
                        $ StormX.FaceChange("surprised",Eyes="closed",Mouth="sucking")
                        $ StormX.Statup("Love", 70, 5)
                        $ StormX.Statup("Obed", 80, 3)
                        $ StormX.Statup("Inbt", 200, 2)
                        ch_s "Хахаха!"
                        $ StormX.FaceChange("smile")
                        ch_s "Я лишь хотела пошутить!"
                $ StormX.Name = "Мисс Манро"
                $ StormX.Name_rod = "Мисс Манро"
                $ StormX.Name_dat = "Мисс Манро"
                $ StormX.Name_vin = "Мисс Манро"
                $ StormX.Name_tvo = "Мисс Манро"
                $ StormX.Name_pre = "Мисс Манро"
                $ StormX.Statup("Love", 70, 3)
                ch_s "Ха! Хорошо, тогда это будет нашей шуткой."
            "Шторм.":
                $ StormX.Name = "Шторм"
                $ StormX.Name_rod = "Шторм"
                $ StormX.Name_dat = "Шторм"
                $ StormX.Name_vin = "Шторм"
                $ StormX.Name_tvo = "Шторм"
                $ StormX.Name_pre = "Шторм"
                if StormX.Petname == "Сью":
                        $ StormX.FaceChange("smile")
                        ch_s "В этом есть что-то особенное."
                else:
                        $ StormX.Statup("Obed", 80, 5)
                        ch_s "О, так официально. Хорошо."

    if not StormX.Petname:
            #if you didn't tell her
            ch_p "А меня зовут [Player.Name]."
            $ StormX.Petname = Player.Name
            $ StormX.Petname_rod = Player.Name_rod
            $ StormX.Petname_dat = Player.Name_dat
            $ StormX.Petname_vin = Player.Name_vin
            $ StormX.Petname_tvo = Player.Name_tvo
            $ StormX.Petname_pre = Player.Name_pre
            $ StormX.Statup("Love", 70, 3)
            ch_s "Очень приятно с тобой познакомиться, [Player.Name]."


    $ StormX.FaceChange("confused")
    if not Player.Male:
        ch_s "Ты ведь проделала весь этот путь не просто так?"
    else:
        ch_s "Ты ведь проделал весь этот путь не просто так?"
    $ StormX.FaceChange("normal")
    $ Count = 3
    while Count > 0:
        menu:
            extend ""
            "Ты совсем голая." if "nudity" not in StormX.History:
                    $ StormX.FaceChange("smile",Eyes="down")
                    $ StormX.Statup("Love", 70, 2)
                    $ StormX.Statup("Obed", 80, 3)
                    $ StormX.Statup("Inbt", 200, 5)
                    ch_s "Да, именно так. . ."
                    $ StormX.FaceChange("normal")
                    call Storm_Nudity
            "Разве ты не хочешь что-нибудь надеть?" if "nudity" not in StormX.History:
                    $ StormX.FaceChange("confused", Mouth="sad")
                    $ StormX.Statup("Love", 70, -2)
                    $ StormX.Statup("Obed", 80, 5)
                    $ StormX.Statup("Inbt", 200, -3)
                    ch_s "Нет. Ну, только если тебе от этого станет спокойнее."
                    call Storm_Nudity

            "О том, почему я здесь. . .":
                menu:
                        extend ""
                        "Отсюда доносилось много шума." if "noise" not in StormX.RecentActions:
                                $ StormX.FaceChange("surprised",2)
                                $ StormX.Statup("Love", 70, 2)
                                $ StormX.Statup("Obed", 80, 5)
                                ch_s "Я слишком сильно шумела?"
                                $ StormX.FaceChange("smile",1,Eyes="down")
                                $ StormX.Statup("Obed", 80, 5)
                                ch_s "Пожалуй, мне нужно быть повнимательнее."
                                $ StormX.FaceChange("smile")
                                ch_s "Прошу, прими мои извинения."
                                $ StormX.AddWord(1,"noise",0,0,0) #adds "word" to Recent
                                menu:
                                    extend ""
                                    "Не стоит.":
                                        $ StormX.Statup("Love", 70, 5)
                                    "Как ты можешь загладить свою вину?":
                                        $ StormX.FaceChange("smile",Eyes="leftside")
                                        ch_s ". . ."
                                        $ StormX.FaceChange("smile")
                                        $ StormX.Statup("Obed", 80, 5)
                                        ch_s "Пожалуй, тем, что в будущем я буду более осторожной?"
                                    "Ладно.":
                                        pass
                        "Насчет протечки. . ." if "water" in Player.RecentActions:
                                $ Player.DrainWord("water")
                                "Вы показываете ей на лужи под несколькими растениями."
                                $ StormX.FaceChange("surprised",2,Eyes="leftside")
                                $ StormX.Statup("Obed", 80, 5)
                                ch_s "Ах, да. Прошу прощения."
                                $ StormX.FaceChange("smile",2,Brows="sad")
                                ch_s "Я поливала свои растения и, должно быть, что-то немного пошло не так."
                                $ StormX.FaceChange("smile",1)
                                ch_s "Один момент. . ."
                                $ StormX.FaceChange("smile",Eyes="white")
                                "Поднимаются ветряные вихри и высушивают лужи."
                                $ StormX.FaceChange("smile")

                        "У тебя прекрасные растения." if "plants" not in StormX.RecentActions:
                                $ StormX.FaceChange("smile")
                                $ StormX.Statup("Love", 70, 7)
                                $ StormX.Statup("Inbt", 200, 5)
                                ch_s "Благодарю."
                                $ StormX.FaceChange("smile",Eyes="leftside")
                                ch_s "Я делаю все возможное, чтобы привнести немного природы в это место."
                                $ StormX.FaceChange("smile")
                                $ StormX.AddWord(1,"plants",0,0,0) #adds "word" to Recent

                        "[EmmaX.Name] сказала, что ты призрак." if "ghost" not in StormX.RecentActions:
                                $ StormX.FaceChange("angry",Eyes="leftside")
                                ch_s "Ох, очень похоже на нее. . ."
                                $ StormX.FaceChange("smile")
                                ch_s "Но, очевидно, я такая же живая, как и ты."
                                ch_s "Я только недавно вернулась из творческого отпуск и готовлюсь присоединиться к преподавательскому составу."
                                $ StormX.AddWord(1,"ghost",0,0,0) #adds "word" to Recent
                        "Неважно.":
                                pass

            "Честно говоря, меня зовут не \"Питер Паркер\"." if StormX.Petname == "Питер" and Player.Name != "Питер Паркер":
                    ch_p "Мое настоящее имя - [Player.Name]."
                    $ StormX.FaceChange("surprised",Mouth="smile")
                    $ StormX.Statup("Love", 70, 3)
                    $ StormX.Statup("Obed", 80, 5)
                    ch_s "О? Значит, ты решил слегка подшутить."
                    $ StormX.FaceChange("smile")
                    ch_s "Ничего страшного, \"Питер.\""
                    $ StormX.Petname = Player.Name
                    $ StormX.Petname_rod = Player.Name_rod
                    $ StormX.Petname_dat = Player.Name_dat
                    $ StormX.Petname_vin = Player.Name_vin
                    $ StormX.Petname_tvo = Player.Name_tvo
                    $ StormX.Petname_pre = Player.Name_pre
            "Честно говоря, меня зовут не \"Сью Шторм.\"" if StormX.Petname == "Сью" and Player.Name != "Сью Шторм":
                    ch_p "Мое настоящее имя - [Player.Name]."
                    $ StormX.FaceChange("surprised",Mouth="smile")
                    $ StormX.Statup("Love", 70, 3)
                    $ StormX.Statup("Obed", 80, 5)
                    ch_s "О? Значит, ты решила слегка подшутить."
                    $ StormX.FaceChange("smile")
                    ch_s "Ничего страшного, \"Сью.\""
                    $ StormX.Petname = Player.Name
                    $ StormX.Petname_rod = Player.Name_rod
                    $ StormX.Petname_dat = Player.Name_dat
                    $ StormX.Petname_vin = Player.Name_vin
                    $ StormX.Petname_tvo = Player.Name_tvo
                    $ StormX.Petname_pre = Player.Name_pre
            "А какие у тебя силы?" if "powers" not in StormX.RecentActions:
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 3)
                    ch_s "Я обладаю способностью влиять на погоду вокруг себя."
                    $ StormX.FaceChange("smile", Eyes="white")
                    call Punch
                    ch_s "Я могу вызвать дождь, молнии и даже парить на ветру."
                    $ StormX.FaceChange("smile")
                    ch_s "Мне очень нравится свобода и связь с природой, которые дают мне мои способности."
                    $ StormX.AddWord(1,"powers",0,0,0) #adds "word" tag to Recent
            "У тебя прекрасный акцент." if "accent" not in StormX.RecentActions:
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 70, 5)
                    ch_s "Благодарю."
                    ch_s "Я родом из Штатов, но большую часть своей юности провела в Кении."
                    $ StormX.AddWord(1,"accent",0,0,0) #adds "word" tag to Recent
            "Пожалуй, мне пора идти. . .":
                    ch_s "Ох, пожалуй. . ."
                    $ Count = 0
    #end Q&A


    $ StormX.FaceChange("smile")
    ch_s "Что ж, было приятно познакомиться с тобой. . ."
    "Она протягивает вам руку для пожатия."
    menu:
        extend ""
        "Пожать":
                $ StormX.FaceChange("surprised",2)
                "Вы крепко пожимаете ее руку, и по ее телу пробегает дрожь."
                $ StormX.Addictionrate += 1 #starts her addiction path
                $ StormX.Statup("Lust", 70, 10)
                $ StormX.FaceChange("confused")
                ch_s "Что -это- было?"
                $ StormX.FaceChange("surprised",Brows = "sad")
                ch_s "Я потеряла связь с ветром вокруг себя!"
        "Пожалуй, не стоит.":
                $ StormX.FaceChange("confused")
                ch_s "Ох, почему нет?"

    ch_p "Мои способности позволяют мне лишать силы других мутантов."
    ch_p "Когда я прикасаюсь к ним, это оказывает. . . сильное влияние."
    if StormX.Addictionrate:
            $ StormX.FaceChange("sadside",1)
            $ StormX.Statup("Love", 70, -15)
            $ StormX.Statup("Obed", 80, 20)
            if not Player.Male:
                ch_s "Ох. Ты могла бы сразу сказать мне об этом. . ."
            else:
                ch_s "Ох. Ты мог бы сразу сказать мне об этом. . ."
    else:
            $ StormX.FaceChange("confused")
            $ StormX.Statup("Love", 70, 15)
            if not Player.Male:
                ch_s "Ох. . . что ж, спасибо, что сообщила мне об этом."
            else:
                ch_s "Ох. . . что ж, спасибо, что сообщил мне об этом."
    $ StormX.FaceChange("normal")

    if "powers" not in StormX.RecentActions:
            $ StormX.FaceChange("smile")
            ch_s "Пожалуй, тебе следует знать, что обычно у меня есть способность влиять на погоду вокруг себя."
            $ StormX.FaceChange("smile", Eyes="white")
            ch_s "Я могу вызвать дождь, молнии и даже парить на ветру."
            $ StormX.FaceChange("smile")
            ch_s "Мне очень нравится свобода и связь с природой, которые дают мне мои способности."

    if "ghost" not in StormX.RecentActions:
            ch_s "Полагаю, ты будешь видеть меня куда чаще, когда я начну работать преподавателем."

    ch_s "В общем, было приятно познакомиться с тобой. Полагаю, увидимся на занятиях, [StormX.Petname]."
    if "naked" in Player.RecentActions:
            $ StormX.Statup("Love", 70, 5)
            $ StormX.Statup("Lust", 70, 3)
            ch_s "Ох, [StormX.Petname]. . ."
            if not Player.Male:
                ch_s ". . .ты ничего не забыла?"
            else:
                ch_s ". . .ты ничего не забыл?"
            ch_p "А, да. . ."
            $ Player.DrainWord("naked")
            $ Player.DrainWord("cockout")
            "Вы снова одеваетесь и возвращаетесь в свою комнату."
    else:
            "Вы возвращаетесь в свою комнату."
    if (StormX.Petname == "Питер" and Player.Name != "Питер Паркер") or (StormX.Petname == "Сью" and Player.Name != "Сью Шторм"):

            $ StormX.History.append("Peter")
    $ StormX.History.append("met")
    $ StormX.Pet = StormX.Name
    $ StormX.Pet_rod = StormX.Name_rod
    $ StormX.Pet_dat = StormX.Name_dat
    $ StormX.Pet_vin = StormX.Name_vin
    $ StormX.Pet_tvo = StormX.Name_tvo
    $ StormX.Pet_rod = StormX.Name_rod
    $ ActiveGirls.append(StormX) if StormX not in ActiveGirls else ActiveGirls
    $ EmmaX.Schedule[1][0] = "bg emma" #TuesMorn
    $ EmmaX.Schedule[1][1] = "bg dangerroom" #TuesNoon
    $ EmmaX.Schedule[3][0] = "bg emma" #ThuMorn
    $ EmmaX.Schedule[3][1] = "bg dangerroom" #ThuNoon

    $ Round -= 20
    $ bg_current = "bg player"
    jump Misplaced

    return

label Storm_Nudity:
    #called when you comment on Storm's nudity
    ch_s "Меня это не беспокоит. Я не так высоко ценю скромность."
    ch_s "Это мое тело, мне не стыдно его показывать."
    $ StormX.FaceChange("normal")
    $ StormX.History.append("nudity")
    while True:
        menu:
                extend ""
                "Значит, ты не против, что я смотрю?" if "looking" not in StormX.RecentActions:
                        $ StormX.AddWord(1,"looking",0,0,0) #adds "word" tag to Recent
                        $ StormX.FaceChange("surprised")
                        $ StormX.Statup("Love", 70, 3)
                        $ StormX.Statup("Obed", 80, 2)
                        ch_s "Как я могу быть против? Это естественно."
                        $ StormX.FaceChange("normal",Eyes="side")
                        ch_s ". . ."
                        $ StormX.FaceChange("sly")
                        $ StormX.Statup("Inbt", 200, 10)
                        $ StormX.Statup("Lust", 50, 2)
                        ch_s "Только постарайся не слишком увлекаться. . ."
                        $ StormX.FaceChange("normal")
                        ch_s "Что-то еще насчет моего тела?"
                "Ты очень красивая." if "hot" not in StormX.RecentActions:
                        $ StormX.AddWord(1,"hot",0,0,0) #adds "hot" tag to Recent
                        $ StormX.FaceChange("smile")
                        $ StormX.Statup("Love", 70, 10)
                        $ StormX.Statup("Obed", 80, 2)
                        $ StormX.Statup("Inbt", 200, 10)
                        ch_s "Благодарю. . ."
                        ch_s "Что-то еще насчет моего тела?"
                "Ты очень сексуальная." if "hot" not in StormX.RecentActions:
                        $ StormX.AddWord(1,"hot",0,0,0) #adds "hot" tag to Recent
                        $ StormX.FaceChange("sly",Brows="confused")
                        $ StormX.Statup("Love", 70, 5)
                        $ StormX.Statup("Obed", 80, 10)
                        $ StormX.Statup("Inbt", 200, 10)
                        $ StormX.Statup("Lust", 50, 2)
                        ch_s ". . . Благодарю. . ."
                        if "nogirls" not in StormX.History:
                                call expression StormX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                        $ StormX.FaceChange("sly")
                        ch_s "Что-то еще насчет моего тела?"
                "У тебя фантастические буфера." if "tits" not in StormX.RecentActions:
                        $ StormX.AddWord(1,"tits",0,0,0) #adds "hot" tag to Recent
                        $ StormX.FaceChange("surprised",2)
                        ch_s ". . ."
                        $ StormX.FaceChange("sly",1,Brows="angry",Eyes="down")
                        $ StormX.Statup("Obed", 80, 15)
                        $ StormX.Statup("Inbt", 200, 15)
                        $ StormX.Statup("Lust", 50, 2)
                        ch_s "Да, пожалуй. . ."
                        ch_s ". . ."
                        $ StormX.FaceChange("sly",Brows="confused")
                        ch_s "Ты понимаешь, что это было немного неуместно?"
                        menu:
                            extend ""
                            "Извини.":
                                    $ StormX.FaceChange("smile",Eyes="stunned")
                                    $ StormX.Statup("Love", 70, 5)
                                    $ StormX.Statup("Obed", 80, -2)
                                    ch_s "Ничего страшного."
                                    $ StormX.FaceChange("smile")
                            "У тебя они намного симпатичнее, чем у [EmmaX.Name_vin].":
                                    $ StormX.FaceChange("perplexed",2)
                                    ch_s ". . ."
                                    $ StormX.Statup("Love", 70, 2)
                                    $ StormX.Statup("Obed", 80, 2)
                                    $ StormX.Statup("Inbt", 200, 5)
                                    ch_s "Благодарю?"
                                    $ StormX.FaceChange("smile",1)
                                    ch_s "По правде говоря, я так не считаю. . ."
                            "У тебя они намного больше, чем у [KittyX.Name_vin].":
                                    $ StormX.FaceChange("perplexed",2)
                                    ch_s ". . ."
                                    $ StormX.Statup("Love", 70, 3)
                                    $ StormX.Statup("Obed", 80, 2)
                                    $ StormX.Statup("Inbt", 200, 5)
                                    $ StormX.Statup("Inbt", 200, 5)
                                    $ StormX.FaceChange("smile",1,Eyes="side")
                                    ch_s "У [KittyX.Name_rod], безусловно, есть свое очарование. . ."
                                    $ StormX.FaceChange("smile")
                            "У тебя они намного красивее, чем у меня." if Player.Male != 1:
                                    $ StormX.FaceChange("perplexed",2)
                                    ch_s ". . ."
                                    $ StormX.Statup("Love", 70, 4)
                                    $ StormX.Statup("Obed", 80, 2)
                                    $ StormX.Statup("Inbt", 200, 5)
                                    ch_s "Не загоняй себя в рамки, мы все прекрасны. . ."
                                    $ StormX.FaceChange("smile",1,Eyes="side")
                                    ch_s "по-своему. . ."
                                    $ StormX.FaceChange("smile")
                            "Ага.":
                                    ch_s ". . ."
                                    $ StormX.FaceChange("smile")
                                    $ StormX.Statup("Obed", 80, 5)
                                    ch_s "Что ж, хорошо, что ты понимаешь."
                        ch_s "Что-то еще насчет моего тела?"

                "Могу я потрогать?" if "touching" not in StormX.RecentActions:
                        $ StormX.FaceChange("angry",2,Eyes="surprised")
                        $ StormX.Statup("Love", 70, -10)
                        $ StormX.Statup("Obed", 80, 10)
                        $ StormX.Statup("Lust", 50, 2)
                        ch_s ". . ."
                        call Storm_Touching
                "Может, займемся сексом на этом столе?" if "touching" not in StormX.RecentActions:
                        $ StormX.FaceChange("angry",2,Eyes="surprised")
                        $ StormX.Statup("Love", 70, -3)
                        $ StormX.Statup("Obed", 80, 5)
                        $ StormX.Statup("Lust", 50, 2)
                        ch_s ". . ."
                        call Storm_Touching

                "У тебя внизу настоящие джунгли." if "pubes" not in StormX.RecentActions:
                        $ StormX.AddWord(1,"pubes",0,0,0) #adds "word" tag to Recent
                        $ StormX.FaceChange("angry",2,Eyes="surprised")
                        $ StormX.Statup("Love", 70, -10)
                        $ StormX.Statup("Obed", 80, 5)
                        $ StormX.Statup("Inbt", 200, -5)
                        ch_s "Я не думаю, что это стоит обсуждать."
                        menu:
                            extend ""
                            "Если честно, мне нравится.":
                                    $ StormX.Statup("Love", 70, 10)
                                    $ StormX.Statup("Inbt", 200, 15)
                                    $ StormX.Statup("Lust", 50, 5)
                            ". . .":
                                pass
                        $ StormX.FaceChange("angry",2,Eyes="down")
                        ch_s "Я просто не вижу смысла следить за этим \"садом\". . ."
                        $ StormX.FaceChange("angry",1)

                "Не могла бы ты одеться?" if "nudity" in StormX.History and not StormX.Over:
                        $ StormX.FaceChange("sly")
                        $ StormX.Statup("Love", 70, -2)
                        $ StormX.Statup("Obed", 80, 5)
                        $ StormX.Statup("Inbt", 200, -3)
                        ch_s "Если так ты будешь чувствовать себя более комфортно, то я не против."
                        $ StormX.OutfitDay = "casual1"
                        $ StormX.Outfit = "casual1"
                        $ StormX.OutfitChange("casual1")

                "Может, мне тоже стоит раздеться?" if "naked" not in Player.RecentActions:
                        $ StormX.FaceChange("surprised",Mouth="sucking")
                        $ StormX.Statup("Love", 70, 3)
                        $ StormX.Statup("Obed", 80, 2)
                        $ StormX.Statup("Inbt", 200, 10)
                        $ StormX.Statup("Lust", 50, 5)
                        ch_s "Хаха!"
                        $ StormX.FaceChange("smile")
                        ch_s "Если тебе так будет комфортнее, я не возражаю."
                        call Girl_First_Peen(StormX,0,1)
                        $ StormX.FaceChange("smile")
                "Нет, я полагаю, что нет. . . [[вернуться]":
                        return

    return

label Storm_Touching:
    #called when you ask to touch Storm
    $ StormX.FaceChange("angry",1)
    if "nogirls" not in StormX.History:
            call expression StormX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
    ch_s "Не искажай мои слова."
    ch_s "Я не стыжусь своего тела, но оно и не достояние общественности."
    menu:
        extend ""
        "Извини, я не хотела тебя обидеть." if not Player.Male:
                $ StormX.FaceChange("angry",Eyes="side")
                $ StormX.Statup("Love", 70, 5)
                $ StormX.Statup("Obed", 80, -2)
                $ StormX.Statup("Inbt", 200, 5)
                ch_s "Все в порядке. Я не могу винить тебя за то, что ты спрашиваешь."
                $ StormX.FaceChange("normal")
                ch_s "Дети в наши дни очень импульсивные."
        "Извини, я не хотел тебя обидеть." if Player.Male:
                $ StormX.FaceChange("angry",Eyes="side")
                $ StormX.Statup("Love", 70, 5)
                $ StormX.Statup("Obed", 80, -2)
                $ StormX.Statup("Inbt", 200, 5)
                ch_s "Все в порядке. Я не могу винить тебя за то, что ты спрашиваешь."
                $ StormX.FaceChange("normal")
                ch_s "Дети в наши дни очень импульсивные."
        "Ну и я не \"общественность?\"":
                $ StormX.FaceChange("surprised",2,Mouth="sucking")
                $ StormX.Statup("Love", 70, 5)
                $ StormX.Statup("Obed", 80, 10)
                ch_s "Ха! У тебя отличное чувство юмора."
                $ StormX.FaceChange("sly",1)
                $ StormX.Statup("Love", 70, 3)
                ch_s "Безусловно, ты не \"общественность.\""
                $ StormX.Statup("Inbt", 200, 10)
                $ StormX.Statup("Lust", 50, 5)
                ch_s "-но боюсь, этого мало."
        "Что. . . у меня совсем нет шансов?":
                $ StormX.FaceChange("perplexed")
                $ StormX.Statup("Love", 70, 5)
                $ StormX.Statup("Obed", 80, 10)
                ch_s ". . ."
                $ StormX.FaceChange("sly",Eyes="side")
                $ StormX.Statup("Inbt", 200, 10)
                $ StormX.Statup("Lust", 50, 5)
                ch_s "Я бы не сказала, что -совсем-. . ."
                $ StormX.FaceChange("sly")
        "Ладно.":
                $ StormX.FaceChange("normal")
                $ StormX.Statup("Love", 70, 2)
                $ StormX.Statup("Obed", 80, -2)
                ch_s "Я рада, что мы достигли взаимопонимания."
    $ StormX.AddWord(1,"touching",0,0,0) #adds "touching" tag to Recent

    ch_s "Итак, у тебя остались еще вопросы насчет моего тела?"
    return

label Storm_Peter:
    #called if you told her your name was Peter Parker
    $ StormX.History.remove("Peter")
    if Player.Name == "Питер Паркер" or Player.Name == "Сью Шторм":
            return
    $ bg_current = "bg classroom"
    call CleartheRoom(StormX,0,1)
    "Перед началом занятий, [StormX.Name] подбегает к вам."
    $ StormX.Loc = "bg classroom"
    call Shift_Focus(StormX)
    call Set_The_Scene
    $ StormX.FaceChange("angry",2,Eyes="surprised")
    ch_s "[Player.Name]!"
    $ StormX.FaceChange("angry")
    if Player.Male:
            ch_s "Да, я узнала, что тебя зовут не \"Питер Паркер.\""
    else:
            ch_s "Да, я узнала, что тебя зовут не \"Сью Шторм.\""
    ch_s "Эмма рассказала мне об этом, когда я не смогла найти твое имя в списке."
    $ StormX.Statup("Love", 50, -5)
    $ StormX.Statup("Love", 60, -20)
    if not Player.Male:
        ch_s "Я не могу поверить, что ты выставила меня полной дурой."
    else:
        ch_s "Я не могу поверить, что ты выставил меня полной дурой."
    $ StormX.Statup("Love", 80, -50)
    $ StormX.Statup("Obed", 80, 5)
    ch_s "Я этого не забуду."
    $ StormX.Petname = Player.Name
    $ StormX.Petname_rod = Player.Name_rod
    $ StormX.Petname_dat = Player.Name_dat
    $ StormX.Petname_vin = Player.Name_vin
    $ StormX.Petname_tvo = Player.Name_tvo
    $ StormX.Petname_pre = Player.Name_pre
    $ bg_current = "bg teacher"
    call Set_The_Scene
    return

#End Storm introduction content





# Event Storm_Teacher_Caught /////////////////////////////////////////////////////
label Storm_Teacher_Caught(Girl = 0):
    #add this scene for when Storm is a teacher, and catches one of the girls fucking around in class.
    #add options for getting away with it
    if  "noticed " + Girl.Tag in StormX.RecentActions:
            return

    if "EmmaStorm" in EmmaX.History:
        if ApprovalCheck(EmmaX, 1200) and ApprovalCheck(StormX, 1200): #and "EmmaStormQueue" not in EmmaX.Traits:
            $ EmmaX.AddWord(1,0,0,"EmmaStormQueue") #adds to Traits, queuing up a redo of event
    elif len(Rules) >= 3 and "classcaught" in EmmaX.History and "met" in StormX.History and (EmmaX.SEXP >= 15 or StormX.SEXP >= 15):
            $ EmmaX.AddWord(1,0,0,"EmmaStormQueue") #adds to Traits, queuing up a redo of event
    if ApprovalCheck(StormX, 500, "I") and ApprovalCheck(StormX, 1500) and StormX.GirlLikeCheck(Girl) >= 500:
            "[StormX.Name] замечает вас двоих, она лишь кивает в знак одобрения, а затем продолжает занятие."
            $ StormX.GLG(Girl,800,3,1)
            $ Girl.GLG(StormX,800,3,1)
            $ StormX.RecentActions.append("noticed " + Girl.Tag)
            return

    ch_s "[Player.Name]? [Girl.Name]? Не могли бы вы прекратить?"
    call Checkout(1)

    $ Girl.FaceChange("bemused", 2, Eyes="side")
    call AllReset(Girl)
    if ApprovalCheck(Girl, 700, "I"):
            $ Girl.FaceChange("bemused", 1)
            "[Girl.Name] пожимает плечами и возвращается на свое место."
            call Partner_Like(StormX,2,-1,500,Girl) #if likes emma 500+, +2, else -1
    else:
            "[Girl.Name] вскакивает и выбегает из комнаты."
            call Partner_Like(StormX,-2,-3,500,Girl) #if likes emma 500+, -2, else -3
            call Remove_Girl(Girl)

    $ Girl.Rep -= 1
    call Partner_Like(Girl,3,2,800,StormX)  #if likes the girl 800+, +3, else +2
    $ StormX.GLG(Girl,800,3,1)

    $ Player.Rep -= 1
    ch_s "Благодарю."

    jump Misplaced

# end Storm_Teacher_Caught //////////////////////////////////////////////////////////

label Storm_Hairtalk:
    #called from Events after class is over
    call Shift_Focus(StormX)
    $ bg_current = "bg classroom"
    $ StormX.Loc = "bg classroom"
    call CleartheRoom(StormX,0,1)
    call Set_The_Scene
    call AltClothes(StormX,8)
    $ StormX.FaceChange("normal")
    "Когда занятия заканчиваются, [StormX.Name] вызывает вас к своему столу."
    if not Player.Male:
        ch_s "[StormX.Petname], я заметила, что в последнее время на занятиях ты выглядишь какой-то. . . отвлеченной."
        ch_s "Могу ли я что-нибудь сделать, чтобы помочь тебе оставаться внимательной?"
    else:
        ch_s "[StormX.Petname], я заметила, что в последнее время на занятиях ты выглядишь каким-то. . . отвлеченным."
        ch_s "Могу ли я что-нибудь сделать, чтобы помочь тебе оставаться внимательным?"
    menu:
        extend ""
        "Нет, я постараюсь более не отвлекаться.":
                $ StormX.Statup("Love", 50, 2)
                $ StormX.Statup("Love", 70, 2)
                ch_s ". . ."
                ch_s "Хорошо. . ."
        "Ты просто слишком красива.":
                $ StormX.Statup("Love", 60, 3)
                $ StormX.Statup("Love", 80, 2)
                $ StormX.FaceChange("surprised")
                ch_s ". . ."
                $ StormX.FaceChange("smile",Eyes="side")
                $ StormX.Statup("Obed", 80, 1)
                $ StormX.Statup("Inbt", 80, 2)
                ch_s "Как мило."
                $ StormX.FaceChange("bemused")
                ch_s "Но я бы не хотела брать на себя ответственность в твоей неуспеваемости."
        "Я не могу перестать смотреть на твои сиськи.":
                $ StormX.Statup("Obed", 80, 2)
                $ StormX.Statup("Inbt", 80, 2)
                $ StormX.FaceChange("surprised")
                ch_s ". . ."
                if ApprovalCheck(StormX, 700):
                    $ StormX.FaceChange("confused",Eyes="side")
                    $ StormX.Statup("Love", 70, 2)
                    ch_s "Это. . . мило."
                else:
                    $ StormX.FaceChange("angry")
                    $ StormX.Statup("Love", 70, -2)
                    ch_s "Это было совершенно неуместно."
                call expression StormX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                $ StormX.FaceChange("bemused")
                ch_s "И я не хотела бы брать на себя ответственность в твоей неуспеваемости."
        "Не знаю.":
                $ StormX.Statup("Love", 50, -1)
                $ StormX.Statup("Obed", 80, -2)
                $ StormX.FaceChange("confused")
                ch_s ". . ."
                $ StormX.FaceChange("bemused")
                $ StormX.Statup("Inbt", 80, 2)
                ch_s "Что ж, возможно, мы могли бы что-нибудь придумать?"
    ch_s "Думаю, за это я, возможно, могла бы тебя как-нибудь. . . вознаградить."
    $ StormX.AddWord(1,"uninterrupted",0,0,0) #adds "word" tag to Recent
    $ Player.AddWord(1,"interruption") #adds to Recent
    menu:
        extend ""
        "Все в порядке, не беспокойся об этом.":
                $ StormX.Statup("Love", 70, 1)
                $ StormX.Statup("Obed", 80, -1)
                $ StormX.FaceChange("confused")
                ch_s ". . ."
                $ StormX.FaceChange("sad")
                if not Player.Male:
                    ch_s ". . . Если ты так в этом уверена. . ."
                else:
                    ch_s ". . . Если ты так в этом уверен. . ."
        "Может, ты могла бы дать мне взглянуть на твои сиськи?":
                $ StormX.Statup("Obed", 80, 2)
                if "nogirls" not in StormX.History:
                        call expression StormX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                        ch_p "Так что насчет одежды?"
                $ StormX.FaceChange("bemused", 1,Eyes="side")
                pause 0.4
                $ StormX.Eyes = "leftside"
                pause 0.4
                $ StormX.Eyes = "squint"
                if ApprovalCheck(StormX, 700):
                    $ StormX.Statup("Love", 70, 2)
                    $ StormX.Statup("Inbt", 60, 1)
                    ch_s "Я. . . пожалуй, я могла бы это устроить. . ."
                    $ StormX.Statup("Inbt", 80, 2)
                    $ StormX.Uptop = 1 #Uptop up
                    $ StormX.Upskirt = 1 #Upskirt up
                    pause 1
                    $ StormX.Uptop = 0 #Uptop up
                    $ StormX.Upskirt = 0 #Upskirt up
                    ch_s ". . ."
                else:
                    $ StormX.Statup("Love", 70, -2)
                    $ StormX.Statup("Inbt", 80, 1)
                    ch_s "Хоть я и не стыжусь своего тела, но это неуместная просьба."
        "Может, снимешь с себя что-нибудь?":
                $ StormX.Statup("Obed", 50, 2)
                $ StormX.Statup("Obed", 80, 1)
                if "nogirls" not in StormX.History:
                        call expression StormX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                        ch_p "Так что насчет одежды?"
                $ StormX.FaceChange("bemused", 1,Eyes="side")
                pause 0.4
                $ StormX.Eyes = "leftside"
                pause 0.4
                $ StormX.Eyes = "squint"
                if ApprovalCheck(StormX, 800):
                    $ StormX.Statup("Inbt", 50, 1)
                    $ StormX.Statup("Inbt", 80, 2)
                    $ Taboo = 0
                    $ StormX.Taboo = 0
                    ch_s "Я. . . пожалуй, я могла бы это устроить. . ."
                    call Girl_Undress(StormX)
                    $ Taboo = 40
                    $ StormX.Taboo = 40
                else:
                    $ StormX.Statup("Love", 70, -2)
                    $ StormX.Statup("Inbt", 200, 5)
                    ch_s "Хоть я и не стыжусь своего тела, но это неуместная просьба."
        "Может, поцелуешь меня?":
                $ StormX.Statup("Love", 70, 1)
                if "nogirls" not in StormX.History:
                        call expression StormX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                        ch_p "Так что насчет поцелуя?"
                $ StormX.FaceChange("bemused")
                if ApprovalCheck(StormX, 700) or StormX.Kissed:
                    $ StormX.Statup("Love", 80, 3)
                    $ StormX.Statup("Obed", 80, 1)
                    $ StormX.Statup("Inbt", 80, 1)
                    ch_s "Я. . . пожалуй, я могла бы это устроить. . ."
                    call SexAct("kissing") # call Storm_SexAct("kissing")
                else:
                    $ StormX.Statup("Obed", 80, -1)
                    ch_s "Я не думаю, что мне следует это делать. . ."
        "Может, дашь мне немного поласкать тебя?":
                $ StormX.Statup("Obed", 80, 2)
                if "nogirls" not in StormX.History:
                        call expression StormX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                        ch_p "Так что насчет. . . ласк?"
                if ApprovalCheck(StormX, 900) or ((StormX.FondleB + StormX.FondleP + StormX.FondleA) > 0):
                    $ StormX.FaceChange("bemused", 1,Eyes="side")
                    pause 0.4
                    $ StormX.Eyes = "leftside"
                    pause 0.4
                    $ StormX.Eyes = "squint"
                    $ StormX.Statup("Inbt", 80, 2)
                    ch_s "Я. . . пожалуй, это можно устроить. . ."
                    $ StormX.Statup("Obed", 50, 2)
                    $ StormX.Statup("Obed", 80, 1)
                    call Girl_FB_Prep
                else:
                    $ StormX.FaceChange("angry", 2)
                    ch_s "[StormX.Petname]!"
                    $ StormX.FaceChange("angry", 1)
                    $ StormX.Statup("Love", 70, -3)
                    $ StormX.Statup("Obed", 50, -1)
                    ch_s "Это было бы крайне неуместно!"

    $ StormX.DrainWord("uninterrupted")
    ch_s "Ладно, думаю, этого пока достаточно."
    "Когда вы поворачиваетесь, чтобы уйти, вы замечаете фотографию на столе."
    show Storm_Photo zorder 150 with easeinbottom
    $ StormX.FaceChange("bemused")
    ch_s "О, это фото было сделано во время моей бунтарской юности."
    hide Storm_Photo with easeoutbottom
    $ StormX.History.append("mohawk")
    menu:
        extend ""
        "Ты отлично выглядишь в таком образе.":
                $ StormX.Statup("Love", 70, 2)
                $ StormX.FaceChange("smile")
                ch_s "Ох, думаешь, мне стоит вернуться к старому имиджу?"
                menu:
                    extend""
                    "Конечно.":
                            $ StormX.Statup("Love", 50, 1)
                            $ StormX.Statup("Love", 70, 1)
                            $ StormX.Statup("Obed", 80, 2)
                            if ApprovalCheck(StormX, 700):
                                ch_s "Пожалуй, тогда так и сделаю."
                                $ StormX.Todo.append("hair")
                            else:
                                ch_s "Возможно, в будущем я подумаю об этом. . ."
                    "Не совсем, ты и сейчас отлично выглядишь.":
                                $ StormX.Statup("Love", 50, 1)
                                $ StormX.Statup("Love", 70, 2)
                                $ StormX.Statup("Inbt", 80, 2)
                                ch_s "Благодарю, я ценю твои слова. . ."
                    "Нет.":
                                $ StormX.Statup("Love", 70, -1)
                                $ StormX.FaceChange("sadside")
                                ch_s ". . ."
                                $ StormX.Statup("Obed", 50, 2)
                                $ StormX.Statup("Obed", 80, 1)
                                ch_s "Пожалуй, я могу это понять. . ."
                                $ StormX.FaceChange("bemused")
                                ch_s "Мне нравится мой нынешний стиль. . ."
        "Я не думаю, что этот образ тебе подходит.":
                                $ StormX.Statup("Love", 50, -2)
                                $ StormX.FaceChange("sadside")
                                ch_s ". . ."
                                $ StormX.Statup("Obed", 50, 1)
                                $ StormX.Statup("Obed", 80, 2)
                                ch_s "Пожалуй, я могу это понять. . ."
                                $ StormX.FaceChange("bemused")
                                ch_s "Мне нравится мой нынешний стиль. . ."
        "Ладно.":
            $ StormX.Statup("Obed", 50, 2)
    ch_s "Пожалуй, это все, что мне нужно было тебе сказать. . ."
    return

# Event Storm_Detention  /////////////////////////////////////////////////////

label Storm_Detention:
            #This label is called from a Location
            call Shift_Focus(StormX)
            call CleartheRoom(StormX,0,1)
            if "traveling" in Player.RecentActions:
                    "Вы входите в комнату [StormX.Name_rod], ждущую вас в дальнем конце комнаты."
            else:
                    "После занятий студенты расходятся, вы ждете несколько минут, пока они все не уйдут."
                    "Как только последний студент уходит, [StormX.Name] подходит к вам."
            show blackscreen onlayer black
            $ bg_current = "bg classroom"
            $ StormX.Loc = "bg classroom"
            $ StormX.OutfitChange()
            call Set_The_Scene
            $ StormX.FaceChange("sly")
            $ StormX.ArmPose = 2
            $ Count = 0
            call CleartheRoom(StormX,0,1)
            hide blackscreen onlayer black
            $ Line = 0
            if "detention" in Player.DailyActions:
                    ch_s "Я рада, что ты серьезно относишься к своему. . . образованию."
            else:
                    #if you skipped detention
                    $ StormX.FaceChange("surprised")
                    if not Player.Male:
                        ch_s "Ох, [StormX.Petname], ты не должна пропускать свое наказание. . ."
                    else:
                        ch_s "Ох, [StormX.Petname], ты не должен пропускать свое наказание. . ."
            $ Player.Traits.remove("detention")
            $ StormX.RecentActions.append("detention")
            $ StormX.DailyActions.append("detention")
            $ StormX.FaceChange("sly")
            $ StormX.Statup("Lust", 80, 3)
            if not Player.Male:
                ch_s "Ты была такой непослушной студенткой. . ."
            else:
                ch_s "Ты был таким непослушным студентом. . ."
            $ StormX.ArmPose = 1
            $ StormX.FaceChange("sadside", Brows="normal")
            $ StormX.Statup("Lust", 80, 5)
            ch_s "ухлестывая за теми девочками. . ."
            $ StormX.FaceChange("sly")
            $ StormX.Statup("Lust", 80, 3)
            if "detention" in StormX.History:
                    ch_s "И чем мы займемся на этот раз?"
            else:
                    #first time
                    ch_s "И что же мне с тобой делать. . ."
                    $ StormX.History.append("detention")

            "[StormX.Name] подходит к двери и запирает ее."
            $ Taboo = 0
            $ StormX.Taboo = 0
            $ Player.Traits.append("locked")
            menu:
                extend ""
                "Думаю, мне стоит сосредоточиться на учебе.":
                        if ApprovalCheck(StormX, 900) and "classcaught" in StormX.History:
                                $ StormX.FaceChange("perplexed")
                                $ StormX.Statup("Inbt", 70, -3)
                                $ StormX.Statup("Lust", 80, 5)
                                ch_s "О. Серьезно? Я была уверена, что мы займемся более. . . интересным \"наказанием\"."
                                menu:
                                    extend ""
                                    "Шучу, конечно, чем займемся? [[Сексуальные действия]":
                                        $ StormX.FaceChange("sly")
                                        $ StormX.Statup("Love", 90, 3)
                                        $ StormX.Statup("Obed", 60, 5)
                                        $ StormX.Statup("Inbt", 70, 5)
                                        $ StormX.DrainWord("nogirls",0,0,0,1) #history
                                        $ StormX.AddWord(1,0,0,0,"girltalk") #history
                                        ch_s "И зачем я только тебя терплю?"
                                        call SexMenu
                                    "Нет, ты права, я слишком легкомысленно отношусь к своему образованию.":
                                        $ StormX.Statup("Love", 80, 1)
                                        $ StormX.Statup("Inbt", 70, -2)
                                        $ StormX.Statup("Lust", 80, 5)
                                        ch_s "Ох. Хорошо. Эм. . ."
                                        $ StormX.FaceChange("sad")
                                        $ StormX.Statup("Obed", 60, 5)
                                        $ StormX.Statup("Lust", 80, 5)
                                        ch_s "Пожалуй, тогда мы могли бы пройтись по нескольким темам сегодняшнего занятия. . ."
                                        $ StormX.Statup("Lust", 80, 5)
                                        $ Player.XP += 10
                        else:
                                        #She's not into you yet.
                                        $ StormX.FaceChange("sad", Mouth="normal")
                                        $ StormX.Statup("Love", 50, 5)
                                        $ StormX.Statup("Love", 80, 5)
                                        $ StormX.Statup("Obed", 60, 5)
                                        $ StormX.Statup("Lust", 80, 5)
                                        ch_s "Да. . . Именно. . ."
                                        $ StormX.Statup("Inbt", 50, 5)
                                        $ StormX.Statup("Lust", 80, 5)
                                        ch_s "Пожалуй, тогда мы могли бы пройтись по нескольким темам сегодняшнего занятия. . ."
                                        $ StormX.Statup("Inbt", 70, 5)
                                        $ StormX.Statup("Lust", 80, 5)
                                        $ Player.XP += 10
                "У меня есть пара идей. . . [[Сексуальные действия]":
                        if "nogirls" not in StormX.History:
                                call expression StormX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                                ch_p "Так вот. . . Я все еще в состоянии придумать, чем мы могли бы заняться. . ."
                        if ApprovalCheck(StormX, 900) and "classcaught" in StormX.History:
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Lust", 80, 5)
                                $ StormX.Statup("Love", 90, 5)
                                $ StormX.Statup("Obed", 60, 5)
                                $ StormX.Statup("Inbt", 70, 5)
                                ch_s "Уверена, что так и есть. . ."
                                call SexMenu
                        else:
                                #She's not into you yet.
                                $ StormX.FaceChange("sad", Mouth="smirk")
                                $ StormX.Statup("Love", 80, 5)
                                $ StormX.Statup("Obed", 60, 5)
                                $ StormX.Statup("Lust", 80, 5)
                                ch_s "Уверена, так и есть. . . но, к сожалению, сейчас не время для этого."
                                $ StormX.Statup("Inbt", 50, 5)
                                $ StormX.Statup("Inbt", 70, 5)
                                $ StormX.Statup("Lust", 80, 5)
                                ch_s "Нам нужно пройтись по нескольким темам сегодняшнего занятия. . ."
                                $ StormX.Statup("Inbt", 50, 5)
                                $ StormX.Statup("Lust", 80, 5)
                                $ Player.XP += 10
            $ Round = 20 if Round > 20 else Round
            ch_s "Ладно, пожалуй, на сегодня достаточно. . ."
            ch_s "Уверена, ты не хочешь, чтобы это вошло в привычку. . ."
            $ Tempmod = 0
            $ StormX.OutfitChange()
            $ Player.DrainWord("locked",0,0,1)
            return

# end Storm_Detention/////////////////////////////////////////////////////


# Event Storm_Key /////////////////////////////////////////////////////

#Not updated

label Storm_Key: #Storm_Update
        call Shift_Focus(StormX)
        $ StormX.Loc = bg_current
        call Shift_Focus(StormX)
        call Set_The_Scene
        $ StormX.FaceChange("bemused")
        $ StormX.ArmPose = 2
        $ Event_Queue = [0,0]
        if not Player.Male:
            ch_s "Ты стала появляться все чаще. . ."
        else:
            ch_s "Ты стал появляться все чаще. . ."
        ch_s ". . . возможно, тебе пригодится ключ. . ."
        "Она вручает вам ключ от своей комнаты."
        ch_p "Спасибо."
        $ StormX.ArmPose = 1
        $ Keys.append(StormX) if StormX not in Keys else Keys
        $ StormX.Event[0] = 1
        return
# end Event Storm_Key /////////////////////////////////////////////////////


# start Storm_BF//////////////////////////////////////////////////////////


label Storm_BF:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(StormX,"bemused","краснеет. . .")
                return
        call Shift_Focus(StormX)
        if StormX.Loc != bg_current:
            $ StormX.Loc = bg_current
            if StormX not in Party:
                "[StormX.Name] подходит к вам и спрашивает, можете ли вы поговорить."
            else:
                "[StormX.Name] поворачивается к вам и спрашивает, можете ли вы поговорить."
        $ StormX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")

        $ Event_Queue = [0,0]
        call Set_The_Scene(0)
        call Display_Girl(StormX)
        call Taboo_Level
        call CleartheRoom(StormX)
        call Shift_Focus(StormX)
        $ StormX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in StormX.History:
                call expression StormX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return

        $ StormX.FaceChange("smile")
        if "asked boyfriend" not in StormX.DailyActions:
                ch_s "[StormX.Petname]. . . Я надеюсь, мы можем поговорить. . ."
                menu:
                    extend ""
                    "Да?":
                        pass
                    "Я вроде как занята." if not Player.Male:
                        $ StormX.FaceChange("sadside")
                        $ StormX.Statup("Love", 90, -5)
                        $ StormX.Statup("Obed", 50, 2)
                        ch_s "Тогда я не отниму у тебя больше времени, чем это необходимо."
                        $ StormX.FaceChange("smile",Mouth="grimace")
                    "Я вроде как заняа." if Player.Male:
                        $ StormX.FaceChange("sadside")
                        $ StormX.Statup("Love", 90, -5)
                        $ StormX.Statup("Obed", 50, 2)
                        ch_s "Тогда я не отниму у тебя больше времени, чем это необходимо."
                        $ StormX.FaceChange("smile",Mouth="grimace")

        $ StormX.Event[5] = 20

        ch_s "Мне нравится время, что мы проводим вместе."
        ch_s "И мне нравишься ты."
        $ StormX.FaceChange("smile",Eyes="side")
        ch_s ". . ."
        $ StormX.FaceChange("smile")
        ch_s "Могу я рассказать тебе одну историю?"
        menu:
            extend ""
            "Конечно.":
                    pass
            "Может, не надо?":
                    $ StormX.Statup("Love", 90, -5)
                    $ StormX.Statup("Obed", 50, 3)
                    $ StormX.Statup("Inbt", 70, -2)
                    $ StormX.FaceChange("confused")
                    ch_s "Думаю, тебе не помешает ее услышать."
            "Как я уже сказала, у меня сейчас действительно есть важные дела." if not Player.Male:
                    $ StormX.FaceChange("sadside")
                    $ StormX.Statup("Love", 90, -5)
                    $ StormX.Statup("Obed", 60, 5)
                    $ StormX.Statup("Inbt", 70, -2)
                    ch_s "Тогда больше не буду отнимать у тебя время."
                    ch_s "Дай мне знать, когда будешь. . . не так сильно занята."
                    call Remove_Girl(StormX)
                    $ Player.History.append("story")
                    return
            "Как я уже сказал, у меня сейчас действительно есть важные дела." if Player.Male:
                    $ StormX.FaceChange("sadside")
                    $ StormX.Statup("Love", 90, -5)
                    $ StormX.Statup("Obed", 60, 5)
                    $ StormX.Statup("Inbt", 70, -2)
                    ch_s "Тогда больше не буду отнимать у тебя время."
                    ch_s "Дай мне знать, когда будешь. . . не так сильно занят."
                    call Remove_Girl(StormX)
                    $ Player.History.append("story")
                    return

label Storm_BF_Story:
        $ StormX.FaceChange("smile")
        ch_s "Когда я была ребенком, я проводила много времени в одиночестве."
        ch_s "Я была брошена на произвол судьбы на улицах Каира и была вынуждена заботиться о себе сама. . ."
        $ StormX.FaceChange("sadside")
        ch_s ". . . в итоге, я не нашла ничего лучше, чем заниматься карманными кражами."
        ch_s "Много лет спустя я отправилась на юг, в Кению, но большую часть времени у меня не было никого, на кого я могла бы положиться."
        $ StormX.FaceChange("smile")
        ch_s "С тех пор, как я прибыла сюда, я научилась ценить крепкие узы товарищества."
        if Player.Harem:
                if len(Player.Harem) >= 2:
                        ch_s "Я, конечно, знаю, что ты проводишь много времени с другими девушками,"
                else:
                        ch_s "Я, конечно, знаю, что ты проводишь много времени с [Player.Harem[0].Name_tvo],"
                if ApprovalCheck(StormX, 1500):
                        $ StormX.Statup("Obed", 60, 2)
                        $ StormX.Statup("Inbt", 70, 2)
                        ch_s ". . . но я могу с этим смириться."
                else:
                        ch_s ". . . но мы можем это обсудить. . ."
        $ StormX.FaceChange("sly")
        if not Player.Male:
            ch_s "Я лишь хочу, чтобы ты всегда была рядом."
        else:
            ch_s "Я лишь хочу, чтобы ты всегда был рядом."
        menu:
            extend ""
            "Конечно.":
                    $ StormX.FaceChange("smile")
                    $ StormX.Statup("Love", 90, 7)
                    $ StormX.Statup("Obed", 60, 2)
                    $ StormX.Statup("Inbt", 70, 2)
                    ch_s "Приятно слышать."
            "Я не особо люблю обязательства. . .":
                    $ StormX.FaceChange("sadside")
                    $ StormX.Statup("Love", 90, -5)
                    $ StormX.Statup("Obed", 60, 5)
                    $ StormX.Statup("Inbt", 70, -2)
                    ch_s ". . . как жаль."
                    $ StormX.FaceChange("sad")
                    ch_s "Тогда дай мне знать, если передумаешь."
                    return
            "Ладно. . .":
                    $ StormX.FaceChange("sadside")
                    $ StormX.Statup("Love", 90, -3)
                    $ StormX.Statup("Obed", 60, 1)
                    $ StormX.Statup("Inbt", 70, -2)
                    ch_s "Это. . . не совсем тот ответ, который я ждала. . ."

        if StormX in Player.Harem:
                #if she somehow already ended up in the harem
                ch_s "Пожалуй, этого достаточно."
                if "StormYes" in Player.Traits:
                        $ Player.Traits.remove("StormYes")
                if "boyfriend" not in StormX.Petnames:
                        $ StormX.Petnames.append("boyfriend")
                return

        if Player.Harem:
                if ApprovalCheck(StormX, 1500):
                        #if she would be ok with the harem life. . .
                        $ StormX.FaceChange("sly",Eyes="side")
                        $ StormX.Statup("Obed", 80, 5)
                        $ StormX.Statup("Inbt", 80, 5)
                        ch_s "Я была бы счастлива присоединиться к твоему маленькому \"гарему.\""
                        $ StormX.FaceChange("sly")
                        ch_s "Если ты согласишься принять меня."

                else:
                    ch_s "Я бы предпочла быть твоей единственной и неповторимой. . ."
                    menu:
                        extend ""
                        "Я могу порвать с ними. . ." if len(Player.Harem) >= 2:
                                $ StormX.FaceChange("smile")
                                $ StormX.Statup("Love", 90, 10)
                                $ StormX.Statup("Obed", 60, 5)
                                $ StormX.Statup("Inbt", 70, 5)
                                ch_s "Превосходно!"
                                ch_s "Осторожно подготовь их к этому. . ."
                                return
                        "Я могу порвать с ней. . ." if len(Player.Harem) == 1:
                                $ StormX.FaceChange("smile")
                                $ StormX.Statup("Love", 90, 10)
                                $ StormX.Statup("Obed", 60, 5)
                                $ StormX.Statup("Inbt", 70, 5)
                                ch_s "Превосходно!"
                                ch_s "Осторожно подготовь ее к этому. . ."
                                return
                        "Я не могу на это согласиться.":
                                $ StormX.FaceChange("sadside")
                                $ StormX.Statup("Love", 90, -5)
                                $ StormX.Statup("Obed", 60, 5)
                                $ StormX.Statup("Obed", 80, 5)
                                $ StormX.Statup("Inbt", 70, -3)
                                ch_s ". . .ох."
                                ch_s "Что ж, какое разочарование."
                                if not ApprovalCheck(StormX, 1000):
                                        ch_s "Пожалуй, тогда на этом все."
                                        call Remove_Girl(StormX)
                                        return
                                else:
                                        $ StormX.Statup("Obed", 80, 5)
                                        $ StormX.Statup("Inbt", 60, 3)
                                        $ StormX.Statup("Inbt", 70, 2)
                                        ch_s ". . . Пожалуй, тогда мне придется принять такой. . . исход."
                menu:
                    extend ""
                    "С удовольствием!" if "StormYes" in Player.Traits:
                            $ StormX.Statup("Love", 90, 20)
                            $ StormX.Statup("Inbt", 70, 5)
                            ch_s "Превосходно!"
                            jump Storm_BF_End
                    "Я бы с удовольствием. . . но. . ." if "StormYes" not in Player.Traits:
                            $ StormX.FaceChange("confused")
                            $ StormX.Statup("Love", 90, 5)
                            $ StormX.Statup("Obed", 60, 5)
                            ch_s ". . . но?"
                            if len(Player.Harem) >= 2:
                                    ch_p "Остальным это не понравится. . ."
                            else:
                                    ch_p "[Player.Harem[0].Name_dat] это не понравится. . ."
                            $ StormX.FaceChange("sadside")
                            ch_s ". . .ох."
                            ch_s "Что ж, какое разочарование."
                            ch_s "Дай мне знать, если ситуация. . . прояснится."
                    "Нет, спасибо.":
                            $ StormX.FaceChange("sadside")
                            $ StormX.Statup("Love", 90, -25)
                            $ StormX.Statup("Obed", 60, 10)
                            ch_s ". . .ох."
                            ch_s "Хорошо."
                            ch_s "Тогда я больше не буду отнимать у тебя время."
        #End "if harem"

        else:
                if not Player.Male:
                    ch_s "Итак, ты не будешь возражать, если я буду считать тебя своей. . . \"девушкой?\""
                else:
                    ch_s "Итак, ты не будешь возражать, если я буду считать тебя своим. . . \"парнем?\""
                menu:
                    extend ""
                    "Я буду только рада!" if not Player.Male:
                            $ StormX.Statup("Love", 90, 20)
                            $ StormX.Statup("Inbt", 70, 5)
                            $ StormX.FaceChange("smile")
                            ch_s "Превосходно!"
                            jump Storm_BF_End
                    "Я буду только рад!" if Player.Male:
                            $ StormX.Statup("Love", 90, 20)
                            $ StormX.Statup("Inbt", 70, 5)
                            $ StormX.FaceChange("smile")
                            ch_s "Превосходно!"
                            jump Storm_BF_End
                    "Я бы предпочла, чтобы ты этого не делала." if not Player.Male:
                            $ StormX.Statup("Love", 90, -20)
                            $ StormX.Statup("Obed", 50, 5)
                            $ StormX.Statup("Obed", 70, 5)
                            $ StormX.FaceChange("sadside")
                            ch_s ". . .ох."
                            ch_s "Что ж, какое разочарование."
                    "Я бы предпочел, чтобы ты этого не делала." if Player.Male:
                            $ StormX.Statup("Love", 90, -20)
                            $ StormX.Statup("Obed", 50, 5)
                            $ StormX.Statup("Obed", 70, 5)
                            $ StormX.FaceChange("sadside")
                            ch_s ". . .ох."
                            ch_s "Что ж, какое разочарование."
                    "Как хочешь.":
                            $ StormX.Statup("Love", 90, -5)
                            if ApprovalCheck(StormX, 1000):
                                    $ StormX.FaceChange("confused")
                                    $ StormX.Statup("Obed", 50, 5)
                                    $ StormX.Statup("Obed", 80, 5)
                                    ch_s ". . .хорошо. Тогда все решено. . ."
                                    jump Storm_BF_End
                            else:
                                    $ StormX.FaceChange("sadside")
                                    $ StormX.Statup("Obed", 60, 5)
                                    ch_s ". . . не такой реакции я ожидала. . ."
                                    ch_s "Возможно, тогда мне стоит все лучше обдумать. . ."
                #end if not harem
        return
label Storm_BF_End:
        $ StormX.Petnames.append("boyfriend")
        #$ StormX.Traits.append("dating")
        if "Historia" not in Player.Traits:
                $ Player.Harem.append(StormX)
                if "StormYes" in Player.Traits:
                        $ Player.Traits.remove("StormYes")
        return

## End Storm_BF//////////////////////////////////////////////////////////



## start Storm_Love//////////////////////////////////////////////////////////
label Storm_Love:
        # StormX.Event[6] += 1 if you're being a jerk
        $ StormX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        if StormX.Loc == bg_current or StormX in Party:
                "[StormX.Name] оценивающе смотрит на вас."
        else:
                "[StormX.Name] выходит из-за угла и замечает вас."
        if bg_current != "bg storm" and bg_current != "bg player":
                "Не говоря ни слова, она берет вас за руку и отводит в свою комнату."
                $ bg_current = "bg storm"
        $ Event_Queue = [0,0]
        $ StormX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(StormX)
        call Taboo_Level
        call Shift_Focus(StormX)
        $ StormX.DailyActions.append("relationship")

        $ StormX.FaceChange("sadside",1)
        ch_s "[StormX.Petname]. . . У меня небольшая проблема. . ."
        menu:
            extend ""
            "Что такое?":
                    $ StormX.Statup("Love", 200, 2)
                    $ StormX.Statup("Inbt", 80, 1)
                    $ StormX.FaceChange("smile")
            "Я могу чем-то помочь?":
                    $ StormX.Statup("Love", 200, 2)
                    $ StormX.Statup("Obed", 50, 2)
                    $ StormX.FaceChange("smile")
                    ch_s "Возможно. . ."
            "Паршиво.":
                    $ StormX.Statup("Love", 200, -5)
                    $ StormX.Statup("Inbt", 90, 2)
                    $ StormX.Event[6] += 1
                    $ StormX.FaceChange("angry",2)
                    ch_s ". . ."
                    $ StormX.FaceChange("normal",1)
            "Ладно.":
                    $ StormX.Statup("Love", 200, -3)
                    $ StormX.FaceChange("confused",1)
                    if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.Event[6] += 1
                            $ StormX.Statup("Love", 200, -2)
                    ch_s ". . ."
        if len(Player.Harem) >= 2:
                ch_s "Я знаю, что тебе приходится делить себя между несколькими женщинами. . ."
        elif StormX in Player.Harem:
                ch_s "До сих пор мы были довольно милой парой. . ."
        $ StormX.FaceChange("sad",1)
        ch_s "Я обдумывала свои чувства к тебе. . ."
        $ StormX.FaceChange("sadside",1)
        ch_s "И я пришла к неприятному выводу."
        ch_s "Я чувствую, что в какой-то степени \"обязана\" тебе. . ."
        menu:
            extend ""
            "Что ты хочешь этим сказать?":
                    $ StormX.Statup("Love", 200, 2)
                    $ StormX.Statup("Inbt", 80, 1)
                    $ StormX.FaceChange("normal",1)
                    ch_s "Позволь мне объяснить. . ."
            "Я сделала что-то не так?" if not Player.Male:
                    $ StormX.Statup("Love", 200, -1)
                    $ StormX.Statup("Inbt", 60, -2)
                    $ StormX.FaceChange("surprised",1)
                    ch_s "О, нет, по крайней мере, не намеренно. . ."
                    $ StormX.FaceChange("normal",1)
            "Я сделал что-то не так?" if Player.Male:
                    $ StormX.Statup("Love", 200, -1)
                    $ StormX.Statup("Inbt", 60, -2)
                    $ StormX.FaceChange("surprised",1)
                    ch_s "О, нет, по крайней мере, не намеренно. . ."
                    $ StormX.FaceChange("normal",1)
            "Странно.":
                    $ StormX.Statup("Obed", 90, 3)
                    $ StormX.Statup("Inbt", 80, 5)
                    $ StormX.FaceChange("confused",1)
                    if not ApprovalCheck(StormX, 600, "OI"):
                            $ StormX.Statup("Love", 200, -3)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("sly",1)
                    ch_s ". . . это. . . не та реакция, которую я ожидала. . ."
                    $ StormX.FaceChange("normal",1)
            "Ладно":
                    $ StormX.Statup("Obed", 70, 2)
                    $ StormX.FaceChange("confused",1)
                    if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.Statup("Love", 200, -2)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("angry",1)
                    ch_s ". . ."
        ch_s "Мое беспокойство уходит корнями в мое детство."
        $ StormX.FaceChange("sadside",1)
        ch_s "Когда я была совсем маленькой, здание, в котором я тогда находилась, подверглось атаке террористов."
        ch_s "Оно рухнуло, завалив меня обломками."
        $ StormX.Eyes = "closed"
        ch_s "В течение нескольких дней я была окружена землей, едва способная двигаться."
        ch_s ". . . я едва могла дышать."
        menu:
            extend ""
            "Какой ужас!":
                    $ StormX.Statup("Love", 200, 4)
                    $ StormX.FaceChange("normal",1)
                    ch_s "Да, но я справилась."
            "Должно быть, тебе пришлось тяжело.":
                    $ StormX.Statup("Love", 200, 5)
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 80, 2)
                    $ StormX.FaceChange("smile",1,Eyes="side")
                    ch_s "Благодарю, да, но я справилась"
            "Ого.":
                    $ StormX.Statup("Obed", 90, 2)
                    $ StormX.FaceChange("confused",1)
                    if not ApprovalCheck(StormX, 600, "OI"):
                            $ StormX.Statup("Love", 200, -3)
                            $ StormX.Statup("Inbt", 80, -2)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("angry",1)
                    ch_s ". . ."
                    ch_s "Да. \"Ого.\""
            "Круто!":
                    $ StormX.Statup("Love", 200, -5)
                    $ StormX.Event[6] += 1
                    $ StormX.FaceChange("surprised",2)
                    ch_s ". . ."
                    $ StormX.FaceChange("angry",1)
                    if not Player.Male:
                        ch_s "Может, постараешься не выглядеть такой радостной?"
                    else:
                        ch_s "Может, постараешься не выглядеть таким радостным?"
            "Ладно.":
                    $ StormX.Statup("Love", 200, -2)
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 80, 1)
                    $ StormX.FaceChange("sadside",1)
                    if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.Statup("Love", 200, -3)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("angry",1)
                    ch_s ". . ."
                    ch_s "У ожидала большего \"участия\". . ."
        ch_s "В конце третьего дня бетонный обломок над моей головой сдвинулся, и появилась чья-то рука."
        $ StormX.FaceChange("smile",1)
        ch_s "Рабочие сумели найти меня и прокопаться ко мне."
        $ StormX.FaceChange("sadside",1)
        ch_s "Даже после того, как я оправилась от физических травм, полученных в результате этого события, я не была полностью исцелена."
        ch_s "Я обнаружила, что от пережитого у меня остались душевные раны. . ."
        menu:
            extend ""
            "Я понимаю.":
                    $ StormX.Statup("Love", 200, 5)
                    $ StormX.Statup("Obed", 80, 1)
                    $ StormX.FaceChange("smile",1)
                    ch_s "Мне это в тебе и нравится. . ."
            "Какого рода?":
                    $ StormX.Statup("Love", 200, 4)
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 80, 2)
                    $ StormX.FaceChange("normal",1)
            "Ага, не сомневаюсь.":
                    $ StormX.Statup("Love", 200, -2)
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.FaceChange("angry",1,Brows="confused")
                    ch_s ". . ."
            "Значит, ты свихнулась?":
                    $ StormX.Statup("Love", 200, -5)
                    $ StormX.Statup("Obed", 80, 5)
                    $ StormX.Statup("Inbt", 80, -5)
                    $ StormX.Event[6] += 2
                    $ StormX.FaceChange("angry",2)
                    ch_s "Конечно, нет!"
                    ch_s "Какой отвратительный вопрос."
                    $ StormX.Blush = 1
            "Ладно.":
                    $ StormX.Statup("Love", 200, -5)
                    $ StormX.Event[6] += 1
                    $ StormX.FaceChange("angry",1,Eyes="side")
                    if not Player.Male:
                        ch_s "Почему мне кажется, что ты не слушала меня?"
                    else:
                        ch_s "Почему мне кажется, что ты не слушал меня?"

        ch_s "Этот опыт развил у меня сильнейшую \"клаустрофобию\"."
        ch_s "Я пытаюсь теперь находится лишь в открытых пространствах, в местах, из которых, как я чувствую, всегда могу убежать."
        $ StormX.FaceChange("bemused",1)
        if not Player.Male:
            ch_s "Поэтому я надеюсь, что ты понимаешь, какие трудности ты мне доставила. . ."
        else:
            ch_s "Поэтому я надеюсь, что ты понимаешь, какие трудности ты мне доставил. . ."
        $ Line = 1
        while Line > 0:
            $ Line -= 1
            menu:
                extend ""
                "Ага, я понимаю." if "iknow" not in StormX.RecentActions:
                        $ StormX.Statup("Love", 200, 2)
                        $ StormX.Statup("Obed", 80, 2)
                        $ StormX.AddWord(1,"iknow",0,0,0)
                        $ StormX.FaceChange("smile",1,Brows = "confused")
                        $ Line += 1
                        ch_s "Да?"
                "Боюсь, что нет. . .":
                        if "iknow" in StormX.RecentActions and "strong" not in StormX.RecentActions:
                                #if you have declared that you know, but haven't guessed "strong" yet
                                $ StormX.Statup("Love", 200, -2)
                                $ StormX.Statup("Obed", 80, -5)
                                $ StormX.Statup("Inbt", 80, 2)
                                ch_s ". . ."
                                $ StormX.FaceChange("sadside",1)
                                if not Player.Male:
                                    ch_s "Ты казалась такой понимающей. . ."
                                else:
                                    ch_s "Ты казался таким понимающим. . ."
                        else:
                                $ StormX.Statup("Love", 200, 5)
                                $ StormX.Statup("Obed", 80, -2)
                                $ StormX.Statup("Inbt", 80, 5)
                                $ StormX.FaceChange("smile",1)
                                ch_s "Зато честно. . ."
                "Ты чувствуешь, словно я заманила тебя в ловушку." if not Player.Male:
                        $ StormX.Statup("Love", 200, 7)
                        $ StormX.Statup("Obed", 80, 2)
                        $ StormX.FaceChange("sad",1)
                        ch_s "Да. . . Боюсь, что да. . ."
                "Ты чувствуешь, словно я заманил тебя в ловушку." if Player.Male:
                        $ StormX.Statup("Love", 200, 7)
                        $ StormX.Statup("Obed", 80, 2)
                        $ StormX.FaceChange("sad",1)
                        ch_s "Да. . . Боюсь, что да. . ."
                "Ты думаешь, что я слишком сильна." if "strong" not in StormX.RecentActions and not Player.Male:
                        $ StormX.FaceChange("confused",1)
                        ch_s "Что?"
                        menu:
                            extend ""
                            "Ничего! Забудь.":
                                    $ StormX.Statup("Obed", 80, -2)
                                    ch_s "Хорошо. . ."
                            "Ну, типа. . . я могу обнять тебя, и ты не сможешь вырваться.":
                                    $ StormX.Statup("Love", 200, -3)
                                    $ StormX.Statup("Obed", 80, -1)
                                    $ StormX.FaceChange("surprised",1)
                                    ch_p "Потому что я сильная."
                                    $ StormX.Statup("Obed", 80, -1)
                                    $ StormX.Statup("Inbt", 80, -2)
                                    $ StormX.FaceChange("angry",1)
                                    ch_s ". . ."
                                    ch_s "Нет."
                        $ StormX.AddWord(1,"strong",0,0,0)
                        $ Line +=1
                "Ты думаешь, что я слишком силен." if "strong" not in StormX.RecentActions and not Player.Male:
                        $ StormX.FaceChange("confused",1)
                        ch_s "Что?"
                        menu:
                            extend ""
                            "Ничего! Забудь.":
                                    $ StormX.Statup("Obed", 80, -2)
                                    ch_s "Хорошо. . ."
                            "Ну, типа. . . я могу обнять тебя, и ты не сможешь вырваться.":
                                    $ StormX.Statup("Love", 200, -3)
                                    $ StormX.Statup("Obed", 80, -1)
                                    $ StormX.FaceChange("surprised",1)
                                    ch_p "Потому что я сильный."
                                    $ StormX.Statup("Obed", 80, -1)
                                    $ StormX.Statup("Inbt", 80, -2)
                                    $ StormX.FaceChange("angry",1)
                                    ch_s ". . ."
                                    ch_s "Нет."
                        $ StormX.AddWord(1,"strong",0,0,0)
                        $ Line +=1
                "Нет.":
                        $ StormX.Statup("Love", 200, -5)
                        $ StormX.Statup("Obed", 80, -2)
                        $ StormX.Event[6] += 1
                        $ StormX.FaceChange("angry",1)
                        ch_s ". . ."
                        $ StormX.Eyes = "side"
                        ch_s "Пожалуй, я не должна удивляться. . ."
                "У тебя сейчас \"эти дни,\" да?":
                        $ StormX.Statup("Love", 200, -10)
                        $ StormX.Event[6] += 2
                        $ StormX.FaceChange("surprised",2)
                        ch_s ". . ."
                        $ StormX.Statup("Obed", 80, -2)
                        $ StormX.Statup("Inbt", 80, -2)
                        $ StormX.FaceChange("angry",2)
                        ch_s ". . .Нет."
                        $ StormX.Blush = 1
                        ch_s "Не. . . \"эти дни.\""
                "[[пожать плечами]":
                        $ StormX.Statup("Love", 200, -3)
                        if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.Statup("Love", 200, -2)
                            $ StormX.Event[6] += 2
                        $ StormX.FaceChange("angry",1)
                        ch_s ". . ."
        if StormX.Event[6] >= 5:
                #you've pissed her off
                jump Storm_Love_Badend
            #end "do you understand" loop.
label Storm_Love_Redux:
        #starting point on second try
        call Shift_Focus(StormX)
        ch_s "Чем ближе мы друг к другу, тем меньше я чувствую, что могу. . ."
        $ StormX.FaceChange("sadside",1)
        ch_s ". . . -освободиться- от тебя."
        menu:
            extend ""
            "Значит, ты этого хочешь? Свободы?":
                    $ StormX.Statup("Love", 200, 1)
                    $ StormX.FaceChange("surprised",2)
                    ch_s "Нет!"
                    $ StormX.Statup("Love", 200, 2)
                    $ StormX.FaceChange("smile",1,Eyes="side")
                    ch_s ". . . нет. . ."
                    $ StormX.Statup("Love", 200, 3)
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 80, 2)
                    $ StormX.FaceChange("smile",1)
                    ch_s "Полагаю, что нет. . ."
            "Могу ли я что-нибудь сделать?":
                    $ StormX.Statup("Love", 200, 5)
                    $ StormX.Statup("Inbt", 80, 4)
                    $ StormX.FaceChange("smile",1)
                    ch_s "Я не считаю, что здесь нужно что-то делать."
                    ch_s "Я довольна этим. . ."
            "Ага, вот так я влияю на женщин.":
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 90, 3)
                    $ StormX.FaceChange("sly",1)
                    if not ApprovalCheck(StormX, 600, "OI"):
                            $ StormX.Statup("Love", 200, -3)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("angry",1,Mouth="smile")
                    ch_s "Постарайся не зазнаваться, [StormX.Petname]"
            "Круто!":
                    $ StormX.Statup("Love", 200, -5)
                    $ StormX.Event[6] += 2
                    $ StormX.FaceChange("angry",1)
                    ch_s "Рада, что тебе нравятся мои страдания."
            "Ладно.":
                    $ StormX.Statup("Love", 200, -2)
                    $ StormX.FaceChange("bemused",1)
                    if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.Statup("Love", 200, -3)
                            $ StormX.Event[6] += 1
                            $ StormX.FaceChange("angry",2)
                            if not Player.Male:
                                ch_s "Ничего лучше не могла ответить?"
                            else:
                                ch_s "Ничего лучше не мог ответить?"
                            $ StormX.Blush = 0
                    ch_s "И зачем я только тебя терплю?"

        if StormX.Event[6] >= 5:
                #you've pissed her off
                jump Storm_Love_Badend

        ch_s "Полагаю, мне просто нужно принять правду. . ."
        $ StormX.FaceChange("smile",1)
        if not Player.Male:
            ch_s "Я люблю тебя, возлюбленная моя."
        else:
            ch_s "Я люблю тебя, возлюбленный мой."
        $ StormX.Petnames.append("lover")
        menu:
            extend ""
            "Я тоже тебя люблю!":
                    $ StormX.Statup("Love", 200, 10)
                    $ StormX.Eyes = "surprised"
                    pause .2
                    $ StormX.Eyes = "normal"
                    ch_s "Я рада это слышать."
            "Клево.":
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 80, -2)
                    $ StormX.FaceChange("confused",1)
                    if not ApprovalCheck(StormX, 1200):
                            $ StormX.Statup("Love", 200, -5)
                            $ StormX.Event[6] += 1
                    ch_s "Кроме этого тебе больше нечего добавить?"
            "Мне бы не хотелось заходить так далеко.":
                    $ StormX.Statup("Love", 200, -10)
                    $ StormX.Statup("Obed", 90, 5)
                    $ StormX.Statup("Inbt", 90, -5)
                    $ StormX.Event[6] += 2
                    $ StormX.FaceChange("angry",1,Eyes="side")
                    if not Player.Male:
                        ch_s "Нет, полагаю, ты и не должна."
                    else:
                        ch_s "Нет, полагаю, ты и не должен."
            "Наверное, я тоже. . .":
                    $ StormX.Statup("Obed", 90, 5)
                    $ StormX.Statup("Inbt", 80, -2)
                    $ StormX.FaceChange("bemused",1)
                    if not ApprovalCheck(StormX, 1200):
                            $ StormX.FaceChange("angry",1)
                            $ StormX.Event[6] += 1
                    ch_s "Пожалуйста, не подавляй меня своими чувствами. . ."
            "Ладно.":
                    if not ApprovalCheck(StormX, 800, "OI"):
                            $ StormX.FaceChange("angry",1)
                            $ StormX.Statup("Love", 200, -2)
                            $ StormX.Event[6] += 1
                    ch_s ". . ."

        if StormX.Event[6] >= 6:
                #you've pissed her off
                jump Storm_Love_Badend

        if len(Player.Harem) >= 2:
                ch_s "Я не собираюсь оставлять тебя только для себя. . ."
                $ StormX.FaceChange("smile",1,Eyes="side")
                ch_s "Другие тоже очень тебя любят. . ."
                ch_s ". . . но та часть тебя, которая меня манит, принадлежит мне."
        $ StormX.FaceChange("smile",1)
        if not Player.Male:
            ch_s "Я так рада, что встретила тебя, возлюбленная."
        else:
            ch_s "Я так рада, что встретила тебя, возлюбленный."
        menu:
            extend ""
            "Я тоже рада, что встретила тебя." if not Player.Male:
                    $ StormX.Statup("Love", 200, 5)
                    $ StormX.Statup("Obed", 90, 5)
                    $ StormX.Statup("Inbt", 80, 5)
                    $ StormX.Petname = "возлюбленная"
                    $ StormX.Petname_rod = "возлюбленной"
                    $ StormX.Petname_dat = "возлюбленной"
                    $ StormX.Petname_vin = "возлюбленную"
                    $ StormX.Petname_tvo = "возлюбленной"
                    $ StormX.Petname_pre = "возлюбленной"
            "Я тоже рад, что встретил тебя." if Player.Male:
                    $ StormX.Statup("Love", 200, 5)
                    $ StormX.Statup("Obed", 90, 5)
                    $ StormX.Statup("Inbt", 80, 5)
                    $ StormX.Petname = "возлюбленная"
                    $ StormX.Petname_rod = "возлюбленной"
                    $ StormX.Petname_dat = "возлюбленной"
                    $ StormX.Petname_vin = "возлюбленную"
                    $ StormX.Petname_tvo = "возлюбленной"
                    $ StormX.Petname_pre = "возлюбленной"
            "Я тоже, но насчет этого прозвища. . .":
                    $ StormX.Statup("Love", 200, 5)
                    $ StormX.Statup("Obed", 90, 7)
                    $ StormX.Statup("Inbt", 80, 3)
                    ch_p "Не могла бы ты продолжать звать меня \"[StormX.Petname]?\""
                    ch_s "Пожалуй, что могу. . ."
            "Мне не нравится это прозвище.":
                    $ StormX.Statup("Love", 200, 3)
                    $ StormX.Statup("Obed", 80, 10)
                    $ StormX.Statup("Inbt", 80, -2)
                    $ StormX.FaceChange("bemused",1)
                    if not Player.Male:
                        ch_s "Что ж, пожалуй, ты права, [StormX.Petname] подходит тебе больше. . ."
                    else:
                        ch_s "Что ж, пожалуй, ты прав, [StormX.Petname] подходит тебе больше. . ."
            "Ладно.":
                    $ StormX.Statup("Obed", 80, 5)
                    $ StormX.Statup("Inbt", 80, 2)
                    $ StormX.FaceChange("confused",1)
                    ch_s ". . ."
                    if not ApprovalCheck(StormX, 900, "L"):
                            $ StormX.Statup("Love", 200, (901-StormX.Love))
                    $ StormX.FaceChange("smile",1,Eyes="side")
                    ch_s "Ладно."
                    if not Player.Male:
                        $ StormX.Petname = "возлюбленная"
                        $ StormX.Petname_rod = "возлюбленной"
                        $ StormX.Petname_dat = "возлюбленной"
                        $ StormX.Petname_vin = "возлюбленную"
                        $ StormX.Petname_tvo = "возлюбленной"
                        $ StormX.Petname_pre = "возлюбленной"
                    else:
                        $ StormX.Petname = "возлюбленный"
                        $ StormX.Petname_rod = "возлюбленного"
                        $ StormX.Petname_dat = "возлюбленному"
                        $ StormX.Petname_vin = "возлюбленного"
                        $ StormX.Petname_tvo = "возлюбленным"
                        $ StormX.Petname_pre = "возлюбленном"

        jump Misplaced
        return

label Storm_Love_Badend:
        #you've pissed her off
        $ StormX.FaceChange("angry",1)
        if not Player.Male:
            ch_s "Знаешь, я не думаю, что ты готова к этому разговору."
        else:
            ch_s "Знаешь, я не думаю, что ты готов к этому разговору."
        $ StormX.RecentActions.append("angry")
        $ StormX.DailyActions.append("angry")
        call Remove_Girl(StormX)
        jump Misplaced
        return


# start Storm_Sub//////////////////////////////////////////////////////////

label Storm_Sub:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(StormX,"bemused","выглядит тихой. . .")
                return
        call Shift_Focus(StormX)
        $ StormX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")

        $ StormX.Loc = bg_current
        $ Event_Queue = [0,0]
        call Set_The_Scene
        if StormX.Loc != bg_current and StormX not in Party:
                "[StormX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить."
        else:
                "[StormX.Name] подходит к вам с явным желанием поговорить."
        call CleartheRoom(StormX)
        call Taboo_Level
        $ StormX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in StormX.History:
                call expression StormX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return

        $ StormX.FaceChange("sly")
        $ Line = 0
        ch_s "[StormX.Petname]. . . Я заметила, что когда мы вместе. . ."
        if not Player.Male:
            ch_s ". . . ты склонна. . . самоутверждаться. . ."
        else:
            ch_s ". . . ты склонен. . . самоутверждаться. . ."
        menu:
            extend ""
            "Правда?":
                    $ StormX.FaceChange("confused")
                    $ StormX.Statup("Obed", 90, -2)
                    ch_s "Да. . ."
            "Да, ты права.":
                    $ StormX.Statup("Obed", 90, 10)
                    $ StormX.Statup("Inbt", 90, 3)
                    $ StormX.Statup("Lust", 70, 5)
                    if not Player.Male:
                        ch_s "Я рада, что ты тоже это заметила. . ."
                    else:
                        ch_s "Я рада, что ты тоже это заметил. . ."
            "Да ладно?":
                    $ StormX.FaceChange("confused")
                    $ StormX.Statup("Obed", 90, -1)
                    ch_s ". . ."
                    ch_s ". . . да, что ж. . ."
        if not Player.Male:
            ch_s "Я надеюсь, что ты заметила. . ."
        else:
            ch_s "Я надеюсь, что ты заметил. . ."
        $ StormX.FaceChange("sly")
        ch_s ". . . как это влияет на меня. . ."
        menu:
            extend ""
            "Тебе. . . это нравится?":
                    $ StormX.Statup("Obed", 90, 3)
                    $ Line = ". . . Да, пожалуй, что так."
            "Тебя это заводит?":
                    $ StormX.FaceChange("bemused",Eyes="side")
                    $ StormX.Statup("Obed", 90, 2)
                    ch_s ". . ."
                    $ StormX.Statup("Obed", 90, 3)
                    $ StormX.Statup("Inbt", 90, 5)
                    $ StormX.Statup("Lust", 90, 5)
                    $ Line = ". . . да."
            "Извини?":
                    $ StormX.FaceChange("perplexed",2)
                    $ StormX.Statup("Obed", 90, -5)
                    $ StormX.Statup("Inbt", 90, -5)
                    ch_s "Ох, в этом нет необходимости-"
                    ch_s "Я не это имела в виду. . ."
            "Я думаю, от этого ты становишься мокрой.":
                    $ StormX.FaceChange("surprised",2)
                    $ StormX.Statup("Obed", 90, 3)
                    $ StormX.Statup("Lust", 90, 5)
                    $ StormX.Statup("Lust", 60, 5)
                    ch_s ". . ."
                    $ StormX.Statup("Inbt", 90, 7)
                    $ StormX.Statup("Lust", 70, 5)
                    $ StormX.FaceChange("bemused",2,Eyes="side")
                    $ Line = ". . .иногда. . ."
        while Line:
            menu:
                ch_s "[Line]"
                "Круто.":
                        $ StormX.FaceChange("perplexed",1)
                        $ Line = 0
                "Повтори.":
                    $ StormX.FaceChange("perplexed",Eyes="side")
                    ch_s ". . ."
                    if "repeat" not in StormX.RecentActions:
                            $ StormX.Statup("Obed", 90, 5)
                            $ StormX.Statup("Lust", 60, 5)
                            $ StormX.AddWord(1,"repeat",0,0,0)
                            $ StormX.FaceChange("bemused",2,Eyes="side")
                    else:
                            $ StormX.FaceChange("bemused")
                            $ StormX.Statup("Love", 80, 2)
                            $ StormX.Statup("Obed", 90, -2)
                            ch_s ". . . Думаю, возможно, на сегодня хватит этих разговоров. . ."
                            menu:
                                "Ладно.":
                                        $ StormX.Statup("Love", 70, 2)
                                        $ StormX.Statup("Obed", 90, 2)
                                "Я решаю, когда хватит.":
                                        $ StormX.FaceChange("angry",1)
                                        $ StormX.Statup("Love", 90, -5)
                                        $ StormX.Statup("Obed", 90, 2)
                                        ch_s "Возможно, ты заходишь слишком далеко."
                                "Ладно. . . на сегодня.":
                                        $ StormX.Statup("Love", 90, 3)
                                        $ StormX.Statup("Obed", 90, 3)
                                        $ StormX.Statup("Inbt", 90, 2)
                                        ch_s "Благодарю."
                            $ Line = 0
                            $ StormX.FaceChange("sly",1)
                "Я рада." if not Player.Male:
                        $ Line = 0
                        $ StormX.FaceChange("bemused",1)
                        $ StormX.Statup("Love", 90, 3)
                        $ StormX.Statup("Inbt", 90, 2)
                "Я рад." if Player.Male:
                        $ Line = 0
                        $ StormX.FaceChange("bemused",1)
                        $ StormX.Statup("Love", 90, 3)
                        $ StormX.Statup("Inbt", 90, 2)
                "Меня это тоже заводит.":
                        $ Line = 0
                        $ StormX.FaceChange("sly",1,Mouth="smile")
                        $ StormX.Statup("Love", 90, 2)
                        $ StormX.Statup("Obed", 90, 5)
                        $ StormX.Statup("Inbt", 90, 3)
                        $ StormX.Statup("Lust", 90, 5)
        ch_s "В общем. . ."
        ch_s "Надеюсь, что ты будешь продолжать. . . и дальше. . ."
        menu:
            extend ""
            "Наверное, можно. . .":
                    $ StormX.FaceChange("sly",1)
                    $ StormX.Statup("Love", 90, 2)
                    $ StormX.Statup("Obed", 90, 2)
            "Это я могу.":
                    $ StormX.FaceChange("sly",1)
                    $ StormX.Statup("Obed", 90, 5)
            "Мне бы не хотелось.":
                    $ StormX.FaceChange("perplexed",1)
                    $ StormX.Statup("Love", 80, -5)
                    $ StormX.Statup("Obed", 90, -5)
                    $ StormX.Statup("Inbt", 90, -5)
                    ch_s "Ох?"
                    $ StormX.FaceChange("sadside",1)
                    $ StormX.Statup("Obed", 90, -5)
                    ch_s ". . .хорошо."
                    $ StormX.Statup("Obed", 90, -10)
                    ch_s "Возможно, когда-нибудь ты передумаешь. . ."
                    call Remove_Girl(StormX)
                    $ StormX.FaceChange("normal",1)
                    $ StormX.History.append("sir")
                    return
            "Конечно.":
                    $ StormX.FaceChange("sly",1)
                    $ StormX.Statup("Obed", 90, 10)
                    $ StormX.Statup("Inbt", 60, 5)
            "Ладно.":
                    $ StormX.FaceChange("perplexed",1)
                    $ StormX.Statup("Obed", 90, -3)
                    ch_s ". . . хорошо."

        if not Player.Male:
            ch_s "я могла бы обращаться к тебе. . . госпожа?"
        else:
            ch_s "я могла бы обращаться к тебе. . . господин?"
        $ StormX.Petnames.append("sir")
        menu:
            extend ""
            "Ты этого хочешь?":
                    $ StormX.FaceChange("perplexed",1,Eyes="side")
                    $ StormX.Statup("Love", 80, 3)
                    ch_s ". . . верно. . ."
                    $ StormX.Statup("Inbt", 90, -2)
                    ch_s ". . ."
                    $ StormX.Statup("Obed", 90, -5)
                    if not Player.Male:
                        ch_s "хотя я и не уверена, что ты правильно меня поняла. . ."
                    else:
                        ch_s "хотя я и не уверена, что ты правильно меня понял. . ."
                    ch_s ". . ."
                    $ StormX.FaceChange("normal",1)
                    ch_s "Но ладно. . ."
                    if not Player.Male:
                        $ StormX.Petname = "госпожа"
                        $ StormX.Petname_rod = "госпожи"
                        $ StormX.Petname_dat = "госпоже"
                        $ StormX.Petname_vin = "госпожу"
                        $ StormX.Petname_tvo = "госпожой"
                        $ StormX.Petname_pre = "госпоже"
                    else:
                        $ StormX.Petname = "господин"
                        $ StormX.Petname_rod = "господина"
                        $ StormX.Petname_dat = "господину"
                        $ StormX.Petname_vin = "господина"
                        $ StormX.Petname_tvo = "господином"
                        $ StormX.Petname_pre = "господине"
            "Можешь.":
                    $ StormX.FaceChange("sly",1)
                    if not Player.Male:
                        $ StormX.Petname = "госпожа"
                        $ StormX.Petname_rod = "госпожи"
                        $ StormX.Petname_dat = "госпоже"
                        $ StormX.Petname_vin = "госпожу"
                        $ StormX.Petname_tvo = "госпожой"
                        $ StormX.Petname_pre = "госпоже"
                    else:
                        $ StormX.Petname = "господин"
                        $ StormX.Petname_rod = "господина"
                        $ StormX.Petname_dat = "господину"
                        $ StormX.Petname_vin = "господина"
                        $ StormX.Petname_tvo = "господином"
                        $ StormX.Petname_pre = "господине"
                    $ StormX.Statup("Love", 90, 5)
                    $ StormX.Statup("Obed", 90, 10)
                    $ StormX.Statup("Inbt", 90, 5)
            "Мне бы хотелось, чтобы ты продолжала звать меня [StormX.Petname]." if StormX.Petname == Player.Name:
                    $ StormX.FaceChange("sly",1)
                    $ StormX.Statup("Obed", 90, 15)
                    $ StormX.Statup("Inbt", 90, 3)
                    ch_s "Хорошо. . ."
            "Мне бы хотелось, чтобы ты звала меня [Player.Name]." if StormX.Petname != Player.Name:
                    $ StormX.FaceChange("sly",1)
                    $ StormX.Statup("Obed", 90, 15)
                    $ StormX.Statup("Inbt", 90, 3)
                    ch_s "Хорошо. . ."
            "Ладно.":
                    $ StormX.FaceChange("confused",1)
                    $ StormX.Statup("Obed", 90, 5)
                    ch_s ". . . хорошо. . ."
                    $ StormX.FaceChange("normal",1)
                    if not Player.Male:
                        $ StormX.Petname = "госпожа"
                        $ StormX.Petname_rod = "госпожи"
                        $ StormX.Petname_dat = "госпоже"
                        $ StormX.Petname_vin = "госпожу"
                        $ StormX.Petname_tvo = "госпожой"
                        $ StormX.Petname_pre = "госпоже"
                    else:
                        $ StormX.Petname = "господин"
                        $ StormX.Petname_rod = "господина"
                        $ StormX.Petname_dat = "господину"
                        $ StormX.Petname_vin = "господина"
                        $ StormX.Petname_tvo = "господином"
                        $ StormX.Petname_pre = "господине"
        ch_s "Это должно быть весело, [StormX.Petname]. . ."
        return


label Storm_Sub_Asked: #Storm_Update
        $ Line = 0
        $ StormX.FaceChange("sadside", 1)
        call Shift_Focus(StormX)
        ch_s "Я припоминаю что-то подобное. . ."
        if not Player.Male:
            ch_s "Ты сказала, что тебе это неинтересно. . ."
        else:
            ch_s "Ты сказал, что тебе это неинтересно. . ."
        menu:
            extend ""
            "Я хочу извиниться. Надеяюсь, мы можем попробовать еще раз.":
                    if "sir" in StormX.Petnames and ApprovalCheck(StormX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(StormX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            ch_s "Я передумала. . . по крайней мере, на данный момент. . ." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ StormX.Statup("Love", 90, 10)
                            $ StormX.FaceChange("sly", 1)
                            if not Player.Male:
                                ch_s "Я ценю, что ты признаешь, что допустила ошибку. . ."
                            else:
                                ch_s "Я ценю, что ты признаешь, что допустил ошибку. . ."
                            ch_s "Ладно, мы можем попробовать еще раз."
            "Теперь я все осознала." if not Player.Male:
                    if "sir" in StormX.Petnames and ApprovalCheck(StormX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(StormX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            ch_s "Что ж. . ."
                            ch_s "Я передумала. . . по крайней мере, на данный момент. . ." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ StormX.Statup("Obed", 200, 10)
                            ch_s ". . ."
                            $ StormX.FaceChange("sly",1)
                            ch_s "Посмотрим."
            "Теперь я все осознал." if Player.Male:
                    if "sir" in StormX.Petnames and ApprovalCheck(StormX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(StormX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            ch_s "Что ж. . ."
                            ch_s "Я передумала. . . по крайней мере, на данный момент. . ." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ StormX.Statup("Obed", 200, 10)
                            ch_s ". . ."
                            $ StormX.FaceChange("sly",1)
                            ch_s "Посмотрим."
            "Ты знаешь, что хочешь этого.":
                    if "sir" in StormX.Petnames and ApprovalCheck(StormX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(StormX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            $ StormX.FaceChange("sly",1)
                            $ StormX.Statup("Love", 200, 5)
                            $ StormX.Statup("Obed", 90, 5)
                            ch_s ". . . д-"
                            $ StormX.FaceChange("angry",1,Eyes="side")
                            $ StormX.Statup("Obed", 90, -3)
                            $ StormX.Statup("Inbt", 90, 5)
                            ch_s "-нет. . ."
                            ch_s "Я передумала. . . по крайней мере, на данный момент. . ." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ StormX.Statup("Love", 200, 5)
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Inbt", 90, 5)
                            $ StormX.Statup("Lust", 90, 5)
                            ch_s ". . ."
                            $ StormX.FaceChange("sly",1)
                            ch_s ". . . да. Я этого хочу."

        $ StormX.RecentActions.append("asked sub")
        $ StormX.DailyActions.append("asked sub")
        if Line == "rude":
                #If line hasn't been set to "rude" by something above, then it skips right past this
                hide Storm_Sprite with easeoutright
                call Remove_Girl(StormX)
                $ StormX.RecentActions.append("angry")
                $ renpy.pop_call()
                "[StormX.Name] выходит за дверь, оставляя вас в одиночестве. Она выглядела очень расстроенной."
        elif "sir" in StormX.Petnames:
                #it didn't fail and "sir" was covered
                $ StormX.Statup("Obed", 200, 30)
                $ StormX.Petnames.append("master")
                if not Player.Male:
                    $ StormX.Petname = "хозяйка"
                    $ StormX.Petname_rod = "хозяйки"
                    $ StormX.Petname_dat = "хозяйке"
                    $ StormX.Petname_vin = "хозяйку"
                    $ StormX.Petname_tvo = "хозяйкой"
                    $ StormX.Petname_pre = "хозяйке"
                else:
                    $ StormX.Petname = "хозяин"
                    $ StormX.Petname_rod = "хозяина"
                    $ StormX.Petname_dat = "хозяину"
                    $ StormX.Petname_vin = "хозяина"
                    $ StormX.Petname_tvo = "хозяином"
                    $ StormX.Petname_pre = "хозяине"
                $ StormX.Eyes = "sly"
                if not Player.Male:
                    ch_s ". . . хозяйка. . ."
                else:
                    ch_s ". . . хозяин. . ."
        else:
                #it didn't fail
                $ StormX.Statup("Obed", 200, 30)
                $ StormX.Petnames.append("sir")
                if not Player.Male:
                    $ StormX.Petname = "госпожа"
                    $ StormX.Petname_rod = "госпожи"
                    $ StormX.Petname_dat = "госпоже"
                    $ StormX.Petname_vin = "госпожу"
                    $ StormX.Petname_tvo = "госпожой"
                    $ StormX.Petname_pre = "госпоже"
                else:
                    $ StormX.Petname = "господин"
                    $ StormX.Petname_rod = "господина"
                    $ StormX.Petname_dat = "господину"
                    $ StormX.Petname_vin = "господина"
                    $ StormX.Petname_tvo = "господином"
                    $ StormX.Petname_pre = "господине"
                $ StormX.Eyes = "sly"
                if not Player.Male:
                    ch_s ". . . госпожа."
                else:
                    ch_s ". . . господин."
        return

# end Storm_Sub//////////////////////////////////////////////////////////


# start Storm_Master//////////////////////////////////////////////////////////

label Storm_Master:  #Storm_Update
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(StormX,"bemused","выглядит необычайно покорной. . .")
                return
        $ StormX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(StormX)
        $ StormX.Loc = bg_current
        $ Event_Queue = [0,0]
        call Set_The_Scene
        if StormX.Loc != bg_current and StormX not in Party:
            "[StormX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить."
        else:
            "[StormX.Name] подходит к вам с явным желанием поговорить."
        call CleartheRoom(StormX)
        $ StormX.DailyActions.append("relationship")
        call Taboo_Level
        $ Line = 0
        $ Options = TotalGirls[:]
        while Options:
                #sorts through all girls, if any call you "master," it spits a 1
                if "master" == Options[0].Petname:
                        $ Line = 2
                elif "хозяин" == Options[0].Petname:
                        $ Line = 2
                elif "хозяйка" == Options[0].Petname:
                        $ Line = 2
                elif "master" in Options[0].Petnames:
                        $ Line = 1 if not Line else Line
                $ Options.remove(Options[0])
        $ StormX.FaceChange("bemused", 1)
        if Line:
                #if any girl calls you "master."
                ch_s "Я слышала кое-какие разговоры между другими девушками. . ."
                if Line == 2:
                        #if at least one girl calls you master
                        ch_s "Похоже, кое-кто из них зовет тебя. . . "
                        $ StormX.FaceChange("sly", 1)
                        if not Player.Male:
                            ch_s "\"Хозяйкой?\""
                        else:
                            ch_s "\"Хозяином?\""
                else:
                        #if none actually call you that
                        ch_s "Похоже, кое-кто из них хочет звать тебя. . . "
                        $ StormX.FaceChange("sly", 1)
                        if not Player.Male:
                            ch_s "\"Хозяйкой?\""
                        else:
                            ch_s "\"Хозяином?\""
        else:
                        #if none of the girls are high obedience yet
                        ch_s "В последнее время я много думала. . ."
                        ch_s "Тебе нравится. . . доминировать над теми, кто тебя окружает?"
                        ch_s "Тебе нравится, когда девушка зовет тебя. . ."
                        $ StormX.FaceChange("sly", 1)
                        if not Player.Male:
                            ch_s "\"Хозяйкой?\""
                        else:
                            ch_s "\"Хозяином?\""
        menu:
            extend ""
            "Не знаю, но это может быть весело.":
                    $ StormX.Statup("Obed", 200, 2)
                    $ StormX.Statup("Inbt", 90, 2)
                    ch_s ". . ."
                    $ StormX.FaceChange("bemused", 1)
                    ch_s "Представляю насколько. . ."
            "Я не особо поощряю подобное.":
                $ StormX.FaceChange("confused", 1)
                $ StormX.Statup("Obed", 200, -2)
                $ StormX.Statup("Inbt", 90, -2)
                if Line == 2:
                    ch_s "Серьезно? . ."
                    $ StormX.FaceChange("sly", 1)
                    $ StormX.Statup("Love", 90, -5)
                    ch_s "Я не это хотела услышать. . ."
                else:
                    ch_s "Хмммм. . . Не такой ответ я ожидала. . ."

            "Да. Мне нравится.":
                    $ StormX.FaceChange("sly", 1)
                    $ StormX.Statup("Love", 90, 2)
                    $ StormX.Statup("Obed", 200, 5)
                    $ StormX.Statup("Inbt", 90, 3)
                    ch_s "Я ждала такого ответа. . ."
            "А что насчет тебя?":
                    $ StormX.FaceChange("sly", 1,Eyes="side")
                    $ StormX.Statup("Love", 90, 1)
                    $ StormX.Statup("Obed", 200, 2)
                    $ StormX.Statup("Inbt", 70, 3)
                    $ StormX.Statup("Inbt", 90, 2)
                    ch_s "Я не знаю. . ."
                    $ StormX.AddWord(1,"aboutyou",0,0,0)
            "Нe-а.":
                $ StormX.FaceChange("confused", 1)
                $ StormX.Statup("Obed", 200, -5)
                $ StormX.Statup("Inbt", 90, -2)
                if Line:
                    $ StormX.Statup("Love", 90, -5)
                    ch_s "Тебе не нужно скрывать от меня такие вещи. . ."
                else:
                    ch_s "Хммм. . . Не такой ответ я ожидала. . ."


        menu:
            extend ""
            "Значит, тебе это понравилось бы.":
                    $ StormX.FaceChange("bemused", 1)
                    $ StormX.Statup("Love", 90, 3)
                    $ StormX.Statup("Obed", 200, 5)
                    $ StormX.Statup("Inbt", 70, 3)
                    $ StormX.Statup("Inbt", 90, 2)
            "Тебе бы это понравилось?" if "aboutyou" not in StormX.RecentActions:
                    $ StormX.FaceChange("sly", 1,Eyes="side")
                    $ StormX.Statup("Love", 90, 1)
                    $ StormX.Statup("Obed", 200, 2)
                    $ StormX.Statup("Inbt", 70, 3)
                    $ StormX.Statup("Inbt", 90, 2)
                    ch_s "Я не знаю. . ."
            "Тебе бы это не понравилось, так?":
                    $ StormX.FaceChange("surprised", 1)
                    $ StormX.Statup("Love", 90, -2)
                    $ StormX.Statup("Obed", 200, -2)
                    ch_s "Ох, твои слова ранят меня. . ."
                    $ StormX.FaceChange("sly", 1,Eyes="side")
                    ch_s "Возможно, ты слишком много на себя берешь. . ."
            "Я знаю, что ты хочешь звать меня \"Хозяйкой\"." if not Player.Male:
                    $ StormX.FaceChange("sly", 1,Eyes="side")
                    $ StormX.Statup("Obed", 200, 5)
                    $ StormX.Statup("Inbt", 90, 2)
                    $ StormX.Statup("Lust", 80, 5)
                    ch_s "Что ж. . ."
            "Я знаю, что ты хочешь звать меня \"Хозяином\"." if Player.Male:
                    $ StormX.FaceChange("sly", 1,Eyes="side")
                    $ StormX.Statup("Obed", 200, 5)
                    $ StormX.Statup("Inbt", 90, 2)
                    $ StormX.Statup("Lust", 80, 5)
                    ch_s "Что ж. . ."
            "Да?":
                    $ StormX.FaceChange("sly", 1,Eyes="side")
                    $ StormX.Statup("Love", 90, -3)
                    $ StormX.Statup("Obed", 200, -3)
                    ch_s "Хмм. . ."
        $ StormX.FaceChange("sly", 1)
        ch_s "Возможно. . ."
        $ Line = 1
        while Line:
                menu:
                    extend ""
                    "Зови меня \"Хозяйкой.\"" if "master" not in StormX.Petnames:
                            $ StormX.FaceChange("surprised", 2)
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Lust", 70, 5)
                            ch_s "Ох. . ."
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Statup("Obed", 200, 5)
                            ch_s "Это я могу. . ."
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Inbt", 90, 3)
                            $ StormX.Statup("Lust", 90, 5)
                            ch_s "Хозяйка."
                            $ StormX.Petnames.append("master")
                    "Зови меня \"Хозяином.\"" if "master" not in StormX.Petnames:
                            $ StormX.FaceChange("surprised", 2)
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Lust", 70, 5)
                            ch_s "Ох. . ."
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Statup("Obed", 200, 5)
                            ch_s "Это я могу. . ."
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Inbt", 90, 3)
                            $ StormX.Statup("Lust", 90, 5)
                            ch_s "Хозяин."
                            $ StormX.Petnames.append("master")
                    "Как ты хочешь звать меня?" if "master" not in StormX.Petnames:
                            $ StormX.FaceChange("sly", 1,Eyes="side")
                            $ StormX.Statup("Love", 90, 3)
                            $ StormX.Statup("Obed", 200, 7)
                            $ StormX.Statup("Lust", 70, 5)
                            ch_s "Хмммм. . ."
                            $ StormX.Statup("Obed", 200, 3)
                            ch_s "Думаю, я хочу звать тебя. . ."
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Inbt", 90, 5)
                            $ StormX.Statup("Lust", 90, 5)
                            if not Player.Male:
                                ch_s ". . . Хозяйкой."
                            else:
                                ch_s ". . . Хозяином."
                            $ StormX.Petnames.append("master")
                    "Скажи это." if "master" not in StormX.Petnames:
                            $ StormX.Statup("Obed", 200, 12)
                            $ StormX.Statup("Lust", 90, 5)
                            ch_s ". . ."
                            $ StormX.FaceChange("sly", 1,Eyes="side")
                            $ StormX.Statup("Obed", 200, 7)
                            $ StormX.Statup("Lust", 94, 5)
                            ch_s ". . ."
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Statup("Obed", 200, 10)
                            $ StormX.Statup("Inbt", 90, 3)
                            $ StormX.Statup("Lust", 200, 5)
                            if not Player.Male:
                                ch_s "Хозяйка."
                            else:
                                ch_s "Хозяин."
                            $ StormX.Petnames.append("master")
                    "Скажи это снова." if "master" in StormX.Petnames and Line < 3:
                            if Line < 2:
                                    $ StormX.Statup("Obed", 200, 2)
                                    $ StormX.Statup("Inbt", 80, 2)
                                    $ StormX.FaceChange("sly", 2,Eyes="side")
                                    ch_s ". . ."
                                    $ StormX.Statup("Lust", 200, 5)
                            else:
                                    $ StormX.FaceChange("smile", 1)
                                    $ StormX.Statup("Love", 90, 3)
                                    $ StormX.Statup("Inbt", 80, 3)
                                    ch_s "Ладно, пожалуй, я уже много раз это сказала. . ."
                            $ StormX.FaceChange("sly", 2,Eyes="side")
                            if not Player.Male:
                                ch_s "Хозяйка."
                            else:
                                ch_s "Хозяин."
                            $ Line += 1
                    "Да, с этого момента зови меня так." if "master" in StormX.Petnames:
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Statup("Obed", 200, 5)
                            $ StormX.Statup("Inbt", 90, 2)
                            if not Player.Male:
                                ch_s "Конечно. . . Хозяйка"
                            else:
                                ch_s "Конечно. . . Хозяин"
                            if not Player.Male:
                                $ StormX.Petname = "хозяйка"
                                $ StormX.Petname_rod = "хозяйки"
                                $ StormX.Petname_dat = "хозяйке"
                                $ StormX.Petname_vin = "хозяйку"
                                $ StormX.Petname_tvo = "хозяйкой"
                                $ StormX.Petname_pre = "хозяйке"
                            else:
                                $ StormX.Petname = "хозяин"
                                $ StormX.Petname_rod = "хозяина"
                                $ StormX.Petname_dat = "хозяину"
                                $ StormX.Petname_vin = "хозяина"
                                $ StormX.Petname_tvo = "хозяином"
                                $ StormX.Petname_pre = "хозяине"
                            $ Line = 0
                    "Мне бы хотелось, чтобы ты звала меня [StormX.Petname_tvo]." if "master" in StormX.Petnames:
                            $ StormX.FaceChange("sad", 1)
                            $ StormX.Statup("Love", 90, 3)
                            $ StormX.Statup("Obed", 200, 3)
                            ch_s "Хорошо. . . [StormX.Petname]"
                            $ Line = 0
                    "Я не знаю, будет ли мне приятно от этого. . ." if "context" not in StormX.RecentActions and "master" not in StormX.Petnames:
                            $ StormX.Statup("Love", 90, 2)
                            $ StormX.Statup("Obed", 200, -3)
                            $ StormX.Statup("Inbt", 90, -2)
                            $ Line = "context"
                    "Я не могу просить тебя обращаться ко мне так." if "context" not in StormX.RecentActions and "master" not in StormX.Petnames:
                            $ StormX.Statup("Obed", 200, -5)
                            $ StormX.Statup("Inbt", 90, -3)
                            $ Line = "context"
                    "Мне все же хотелось бы, чтобы ты не звала меня так." if "context" in StormX.RecentActions and "master" not in StormX.Petnames:
                            $ StormX.FaceChange("sad", 1,Mouth="smile")
                            $ StormX.Statup("Love", 90, 5)
                            $ StormX.Statup("Obed", 200, 5)
                            ch_s "Понимаю."
                            $ StormX.FaceChange("smile", 1)
                            ch_s "Считай, что я не спрашивала."
                            ch_s ". . ."
                            $ StormX.FaceChange("sly", 1)
                            ch_s "Хотя если ты передумаешь. . ."
                            $ Line = 0
                    #end menu items

                if Line == "context":
                            #zero expressed hesitancy
                            $ StormX.FaceChange("surprised", 2)
                            ch_s "Ох."
                            $ StormX.FaceChange("sad", 1)
                            ch_s "Я, конечно, знаю, что есть некий. . ."
                            $ StormX.FaceChange("sadside", 1)
                            ch_s ". . . исторический багаж, связанный с этим термином."
                            ch_s "Я не могу сказать, что я полностью невосприимчива к этой концепции. . ."
                            ch_s "Но я не думаю, что это беспоколо бы меня."
                            $ StormX.Statup("Obed", 200, 2)
                            $ StormX.Statup("Inbt", 90, 2)
                            $ StormX.Statup("Lust", 90, 2)
                            if not Player.Male:
                                ch_s ". . . если бы это была ты. . ."
                            else:
                                ch_s ". . . если бы это был ты. . ."
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.AddWord(1,"context",0,0,0)
                            $ Line = 1
                #End final question loop
        $ StormX.FaceChange("sly", 1)
        $ StormX.History.append("master")
        $ Line = 0
        return

# end Storm_Master//////////////////////////////////////////////////////////


# start Storm_Sexfriend//////////////////////////////////////////////////////////

label Storm_Sexfriend:   #Storm_Update
        "Вы получаете сообщение от [StormX.Name_rod]:"
        "\"Жду тебя у бассейна сегодня вечером. . .\""
        $ Event_Queue = [0,0]
        $ Player.AddWord(1,0,0,0,"poolnight") #adds tag to History
        $ StormX.DailyActions.append("relationship")
        $ StormX.Event[9] = 1
        return


label Storm_Poolnight:
        call Shift_Focus(StormX)
        call Set_The_Scene
        call CleartheRoom(StormX,1,1)
        call Set_The_Scene
        $ StormX.Loc = "bg pool"
        call ShowPool([StormX])
        $ Taboo = 0
        $ StormX.Taboo = 0
        $ StormX.FaceChange("sly", 1)
        $ StormX.OutfitChange("nude")
        $ StormX.RecentActions.append("poolnight")
        $ StormX.DrainWord("nogirls",0,0,0,1) #history
        $ StormX.AddWord(1,0,0,0,"girltalk") #history
        if "no poolnight" in StormX.RecentActions:
                if not Player.Male:
                    ch_s "Ох, ты что, передумала?"
                else:
                    ch_s "Ох, ты что, передумал?"
        elif "sexfriend" not in StormX.Petnames:
                #first time through. . ."
                show Storm_Sprite:
                    yoffset 200
                "Когда вы подходите в назначенное место, вы находите бассейн совершенно пустым, если не считать небольшой ряби на его поверхности."
                show Storm_Sprite:
                    ease 1 yoffset 0
                pause 1
                show Storm_Sprite at Pool_Bob(500) zorder 50
                "[StormX.Name] выныривает из-под воды."
                ch_s "Ах, я надеялась, что ты присоединишься ко мне, [StormX.Petname]. . ."
                if StormX not in Player.Harem and StormX.Petname not in ("господин","госпожа","хозяин","хозяйка"):
                        ch_s "Я знаю, что наша ситуация ни к чему не обязывает. . ."
                        ch_s "Меня это вполне устраивает."
                        $ StormX.Statup("Inbt", 200, 25)
                        ch_s "Мы можем просто продолжать взаимодействовать как. . . секс-партнеры. . ."
                        $ StormX.Petnames.append("sex friend")
        else:
                ch_s "Ох, здравствуй, [StormX.Petname]."
                ch_s "Хочешь присоединиться ко мне?"
        menu:
            extend ""
            "Конечно":
                    $ StormX.Statup("Love", 200, 2)
                    $ StormX.Statup("Inbt", 200, 2)
                    "Вы присоединяетесь к ней в бассейне и немного плаваете."
                    $ StormX.Statup("Lust", 90, 3)
                    "Вы подплываете все ближе и ближе друг к другу. . ."
                    $ Round -= 10 if Round >= 10 else Round
                    "Наконец, она притягивает вас к себе и шепчет на ухо. . ."
                    $ StormX.Statup("Lust", 90, 5)
                    ch_s "Не хочешь выйти из воды и заставить меня намокнуть полностью?"
                    "Вы оба вылезаете из бассейна на бортик."
            "Не могла бы ты просто подойти ко мне?":
                    $ StormX.Statup("Obed", 70, 1)
                    $ StormX.Statup("Obed", 90, 2)
                    $ StormX.Statup("Inbt", 200, 2)
                    $ StormX.Statup("Lust", 90, 3)
                    ch_s "Что ж, можно и так. . ."
                    "Она вылезает из бассейна."
            "Может в другой раз. [[уйти]":
                    $ StormX.FaceChange("sad", 1)
                    if "no poolnight" in StormX.RecentActions:
                            ch_s "Тебе стоит уже определиться."
                    else:
                            $ StormX.Statup("Obed", 90, 3)
                            ch_s "Ох, как жаль. . ."
                            ch_s "Что ж, не скучай там. . ."
                    $ Round -= 10
                    $ StormX.AddWord(1,"no poolnight") #recent
                    "Вы возвращаетесь в свою комнату."
                    $ bg_current = "bg player"
                    jump Misplaced
        hide Storm_Sprite
        hide FullPool
        call Set_The_Scene(Dress=0)
        $ StormX.FaceChange("sly", 1,Eyes="leftside")
        ch_s "Теперь, когда у тебя есть я, [StormX.Petname]. . ."
        $ StormX.FaceChange("sly", 1)
        ch_s "Что ты собираешься со мной делать. . ?"
        call SexMenu
        return


# end Storm_Sexfriend//////////////////////////////////////////////////////////


# start Storm_Fuckbuddy//////////////////////////////////////////////////////////

label Storm_Fuckbuddy:   #Storm_Update
        $ StormX.DailyActions.append("relationship")
        $ StormX.Loc = "bg classroom"
        $ bg_current = "bg classroom"
        $ Event_Queue = [0,0]
        call CleartheRoom(StormX,1,1)
        call Set_The_Scene(Dress=0)
        call Shift_Focus(StormX)
        $ Player.Traits.append("locked")
        $ Nearby = []
        call Taboo_Level
        $ StormX.FaceChange("sly", 1,Eyes="side")
        $ StormX.Statup("Inbt", 200, 5)
        "После занятия [StormX.Name] проходит мимо вас и кладет руку вам на грудь, пока вы выходите."
        $ StormX.Statup("Inbt", 200, 5)
        "Она немного отходит назад и запирает дверь."
        $ StormX.FaceChange("sly", 1,Eyes="down")
        $ StormX.Statup("Inbt", 200, 10)
        ch_s "Ты же знаешь, что у меня есть потребности."
        $ StormX.Petnames.append("fuck buddy")
        $ StormX.Event[10] += 1
        $ StormX.FaceChange("sly", 1)
        $ StormX.Statup("Inbt", 200, 10)
        if not Player.Male:
            ch_s "Не могла бы ты мне с ними помочь? . . "
        else:
            ch_s "Не мог бы ты мне с ними помочь? . . "
        call SexMenu
        return
# end Storm_Fuckbuddy//////////////////////////////////////////////////////////

# start Storm_Daddy//////////////////////////////////////////////////////////

label Storm_Daddy:       #Storm_Update
        $ StormX.DailyActions.append("relationship")
        call Shift_Focus(StormX)
        $ Event_Queue = [0,0]
        if StormX.Loc != bg_current:
                $ StormX.Loc = bg_current
                "[StormX.Name] подходит к вам."
        call Set_The_Scene
        ch_s ". . ."
        $ Line = 0
        $ Options = TotalGirls[:]
        while Options:
                #sorts through all girls, if any call you "master," it spits a 1
                if "daddy" == Options[0].Petname:
                        $ Line = 2
                elif "папочка" == Options[0].Petname:
                        $ Line = 2
                elif "мамочка" == Options[0].Petname:
                        $ Line = 2
                elif "daddy" in Options[0].Petnames:
                        $ Line = 1 if not Line else Line
                $ Options.remove(Options[0])


        if StormX in Player.Harem:
                ch_s "Я разговаривала с другими девушками. . ."
        else:
                ch_s "Я кое-что слышала от студентов. . ."
        if Line:
                if not Player.Male:
                    ch_s "Видимо, некоторые из них зовут тебя. . . \"мамочкой?\""
                else:
                    ch_s "Видимо, некоторые из них зовут тебя. . . \"папочкой?\""
        else:
                if not Player.Male:
                    ch_s "Видимо, некоторые женщины в отношениях. . ."
                    ch_s ". . . зовут своего партнера. . . \"папочкой?\""
                    ch_s ". . . или, если партнер другая женщина. . . \"мамочкой?\""
                else:
                    ch_s "Видимо, некоторые женщины в отношениях. . ."
                    ch_s ". . . зовут своего партнера. . . \"папочкой?\""
        menu:
            extend ""
            "Да?":
                    ch_s "Как я и думала. . ."
            "Я не понимаю, о чем ты говоришь.":
                    ch_s "Я думаю, это просто ласковое обращение. . ."
                    ch_s "Ласковое, но. . . покорное?"
            "Я тебя не понимаю.":
                    ch_s "Ох. Видимо, я ошиблась."
        $ Line = 1
        $ StormX.Petnames.append("daddy")
        while Line:
            menu:
                extend ""
                "Ты хочешь звать меня так?" if "callyouthat" not in StormX.RecentActions:
                        $ StormX.Statup("Love", 70, 1)
                        $ StormX.Statup("Inbt", 90, 2)
                        ch_s ". . ."
                        $ StormX.Statup("Love", 95, 2)
                        $ StormX.Statup("Inbt", 70, 1)
                        ch_s "Пожалуй. . ."
                        $ StormX.RecentActions.append("callyouthat")
                "Наверное, я не против, чтобы ты звала меня так. . ." if "callyouthat" in StormX.RecentActions or "whycare" in StormX.RecentActions:
                        $ StormX.Statup("Love", 70, 2)
                        $ StormX.Statup("Obed", 200, 5)
                        $ StormX.Statup("Inbt", 70, 1)
                        ch_s ". . ."
                        $ StormX.Statup("Love", 200, 5)
                        $ StormX.Statup("Inbt", 90, 3)
                        if not Player.Male:
                            ch_s "Конечно. . . мамочка."
                        else:
                            ch_s "Конечно. . . папочка."
                        $ Line = 0
                "Зови меня \"Мамочкой.\"" if not Player.Male:
                        $ StormX.Statup("Love", 90, 2)
                        $ StormX.Statup("Obed", 80, 3)
                        ch_s ". . ."
                        $ StormX.Statup("Obed", 200, 5)
                        $ StormX.Statup("Inbt", 90, 2)
                        $ StormX.Statup("Lust", 90, 3)
                        ch_s "Конечно. . . мамочка."
                        $ Line = 0
                "Зови меня \"Папочкой.\"" if Player.Male:
                        $ StormX.Statup("Love", 90, 2)
                        $ StormX.Statup("Obed", 80, 3)
                        ch_s ". . ."
                        $ StormX.Statup("Obed", 200, 5)
                        $ StormX.Statup("Inbt", 90, 2)
                        $ StormX.Statup("Lust", 90, 3)
                        ch_s "Конечно. . . папочка."
                        $ Line = 0
                "Почему тебя это волнует?" if "whycare" not in StormX.RecentActions:
                        $ StormX.Statup("Love", 90, 2)
                        $ StormX.Statup("Obed", 80, -1)
                        $ StormX.Statup("Inbt", 90, -1)
                        ch_s "Ох, что ж, мне просто хочется так к тебе обращаться. . ."
                        $ StormX.RecentActions.append("whycare")
                "Это странно, тебе не кажется?":
                        $ StormX.Statup("Love", 90, -3)
                        $ StormX.Statup("Obed", 90, -5)
                        $ StormX.Statup("Inbt", 90, -15)
                        ch_s "Ох. . . "
                        ch_s ". . . полагаю, это так."
                        ch_s "Забудь. . ."
                        call Remove_Girl(StormX)
                        $ Line = 0
                "Мне бы этого не хотелось." if "callyouthat" in StormX.RecentActions or "whycare" in StormX.RecentActions:
                        $ StormX.Statup("Love", 90, -2)
                        $ StormX.Statup("Obed", 90, 3)
                        $ StormX.Statup("Inbt", 90, -5)
                        ch_s "Ох. . . "
                        ch_s ". . . хорошо."
                        ch_s "Забудь. . ."
                        call Remove_Girl(StormX)
                        $ Line = 0
        return

# end Storm_Daddy//////////////////////////////////////////////////////////


# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Storm_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        if "switched" in StormX.History:
                jump Storm_Switch2
        $ StormX.FaceChange("smile", 1)
        ch_s "О, здравствуй."
        ch_s "Мы встречались?"
        menu:
            extend ""
            "Это я, [Player.XName].":
                    $ StormX.FaceChange("confused", 1)
                    ch_s "Хмм?"
                    $ StormX.FaceChange("surprised", 1)
                    ch_s "Ох!"
                    $ StormX.FaceChange("smile", 1)
                    ch_s "Как интересно."
                    $ StormX.AddWord(1,"switch") #recent

            "Нет.":
                    ch_s "Меня зовут [StormX.Name]."
            "Возможно?":
                    ch_s "Хм, мне кажешься, я тебя где-то видела. . ."

        if "switch" not in StormX.RecentActions:
                    $ StormX.FaceChange("confused", 1)
                    ch_s ". . ."
                    ch_s "Должно быть, я уже видела тебя в аудитории. . ."
                    $ StormX.FaceChange("surprised", 1)
                    ch_s "Подожди-ка. . ."
                    ch_s "Ты, случайно, не [Player.XName]?"
                    $ StormX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Ага, это я, [Player.XName].":
                                $ StormX.Statup("Love", 90, 1)
                                $ StormX.Statup("Obed", 70, 1)
                                ch_s "Ох!"
                                $ StormX.FaceChange("smile", 1)
                                ch_s "Вот это метамофозы."
                        "Нет.":
                                $ StormX.FaceChange("angry", 1)
                                $ StormX.Statup("Obed", 60, 1)
                                $ StormX.Statup("Obed", 70, 1)
                                ch_s "Не пытайся меня обмануть, [Player.XName]."
                        "Возможно?":
                                $ StormX.FaceChange("sly", 1)
                                $ StormX.Statup("Love", 80, 1)
                                $ StormX.Statup("Obed", 70, 1)
                                $ StormX.Statup("Inbt", 60, 1)
                                ch_s "Я уверена, это ты, [Player.XName]."
                    ch_s "Зачем лгать мне?"
                    menu:
                        extend ""
                        "Извини, хотелось пошутить.":
                                $ StormX.FaceChange("sly", 1)
                                $ StormX.Statup("Obed", 70, 1)
                                ch_s "Хорошо, я забуду про этот случай. . ."
                        "Молодец, ты все поняла.":
                                $ StormX.FaceChange("sly", 1)
                                $ StormX.Statup("Love", 70, -1)
                                $ StormX.Statup("Obed", 70, 1)
                                $ StormX.Statup("Inbt", 80, 1)
                                ch_s "Да."
                        "Хех.":
                                $ StormX.FaceChange("sly", 1,Eyes="side")
                                $ StormX.Statup("Love", 70, 1)
                                $ StormX.Statup("Love", 90, 1)
                                $ StormX.Statup("Inbt", 70, 1)
                                ch_s "Захотелось пошутить, значит. . ."
                    ch_s "У меня большой опыт общения как с шулерами, так и с перевертышами."
        #end "tried to lie"
        $ StormX.FaceChange("smile", 1)
        ch_s "Зачем такие изменения?"
        menu:
            extend ""
            "Да так, по приколу.":
                    $ StormX.Statup("Inbt", 70, 1)
                    $ StormX.FaceChange("surprised", 2)
                    ch_s "Что ж, жизнь подобна приключению."
                    $ StormX.FaceChange("sly", 1)
            "Я так себя сейчас ощущаю.":
                    ch_s "Ох. . . что ж, тогда поздравляю."
            "У меня не было каких-то особых причин.":
                    ch_s "Понятно. . ."

        if [Player.Name] != [Player.XName]:
                ch_p "А еще теперь меня зовут [Player.Name]."
                ch_s "Рада снова с тобой познакомиться, [Player.Name]."

        if StormX.SEXP >= 15:
                $ StormX.FaceChange("sad", 1,Mouth="smile")
                ch_s "Я тебе еще. . . интересна?"
                menu:
                    extend ""
                    "Конечно!":
                            $ StormX.FaceChange("smile", 1)
                            $ StormX.Statup("Love", 70, 2)
                            $ StormX.Statup("Love", 90, 1)
                            ch_s "Восхитительно. . ."
                    "Да не особо.":
                            $ StormX.Statup("Love", 80, -2)
                            $ StormX.Statup("Obed", 60, 2)
                            $ StormX.Statup("Obed", 80, 2)
                            $ StormX.FaceChange("sadside", 1)
                            ch_s "Ну хорошо. . ."
                    "А ты как думаешь?":
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Statup("Obed", 70, 1)
                            $ StormX.Statup("Inbt", 70, 1)
                            ch_s "Я сомневаюсь, что такие изменения повлияли на твое либидо. . ."

        if not Player.Male and StormX.Les > 5:
                $ StormX.FaceChange("sly", 1)
                ch_s "В прошлом у меня были кое-какие. . . близкие отношения с женщинами. . ."
        if ApprovalCheck(StormX, 1500):
                ch_s "Я была бы не против продолжить наши отношения."
                $ StormX.AddWord(1,0,0,0,"girltalk") #history
        else:
                $ StormX.FaceChange("normal", 1,Eyes="side")
                ch_s "Пожалуй, мне понадобится какое-то время, чтобы принять твои изменения. . ."
        $ StormX.Traits.remove("switchcheck")
        $ StormX.AddWord(1,0,0,0,"switched") #history
        return

label Storm_Switch2:
        #when you switch for a 2+ time
        $ StormX.FaceChange("surprised", 1)
        ch_s "Ох!"
        $ StormX.FaceChange("confused", 1)
        ch_s "Ты выглядишь как прежде."
        $ StormX.FaceChange("smile", 1)
        ch_s "Замечательно."
        $ StormX.Traits.remove("switchcheck")
        $ StormX.History.remove("switched")
        $ StormX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Storm_Girltalk(Auto=0,Other=0):
        # if Auto Storm starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in StormX.History:
                return
        if "nogirls" in StormX.History:
                jump Storm_Girltalk_Redux
        if Auto:
                $ StormX.FaceChange("sadside", 2)
                ch_s "[Player.Name]. . ."
                ch_s "Я заметила. . . как ты смотришь на меня. . ."
                ch_s "Я тебе привлекаю?"
        else:
                $ StormX.FaceChange("confused", 1)
                ch_s "Ох? Я тебе привлекаю?"
        menu:
            extend ""
            "Да?":
                    $ StormX.FaceChange("surprised", 1)
                    $ StormX.Statup("Love", 70, 2)
                    $ StormX.Statup("Love", 90, 2)
                    $ StormX.Statup("Obed", 70, 1)
                    ch_s "Ох. . ."
                    $ StormX.FaceChange("smile", 1, Eyes="side")
            "Наверное?":
                    $ StormX.FaceChange("confused", 1)
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 80, 2)
                    ch_s "Ох. . ."
                    $ StormX.FaceChange("sly", 1)
            "Не особо.":
                    $ StormX.FaceChange("sadside", 1)
                    $ StormX.Statup("Love", 90, -1)
                    $ StormX.Statup("Obed", 60, 2)
                    $ StormX.Statup("Obed", 80, 2)
                    ch_s "Ох. . ."
                    ch_s "Пожалуй, это нормально. . ."
        if not ApprovalCheck(StormX, 900):
                $ StormX.FaceChange("sad", 1)
                ch_s "Я не уверена, дай мне немного времени все обдумать. . ."
                $ StormX.AddWord(1,0,0,0,"nogirls") #history
                call Girltalk_Check(StormX)
                return
        ch_s "Я думаю, что ты мне очень нравишься. . ."
        $ StormX.FaceChange("smile", 1)
        ch_s "Может, мы и обе женщины, но у меня есть кое-какой опыт в этом деле. . ."
        $ StormX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(StormX)
        return

label Storm_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing
        if ApprovalCheck(StormX, 900):
                $ StormX.FaceChange("sly", 1)
                if Other in TotalGirls and "nogirls" in Other.History:
                        ch_s "Я не уверена. . ."
                ch_s "Может, мы и обе женщины, но у меня есть кое-какой опыт в этом деле. . ."
                $ StormX.DrainWord("nogirls",0,0,0,1) #history
                $ StormX.AddWord(1,0,0,0,"girltalk") #history
        elif "nogirls" not in StormX.History:
                $ StormX.AddWord(1,0,0,0,"nogirls") #history
                $ StormX.FaceChange("sad", 1)
                ch_s "Я не уверена, дай мне немного времени все обдумать. . ."
        elif "nogirls" in StormX.DailyActions:
                $ StormX.FaceChange("angry", 1)
                if StormX.Forced:
                        #if Forced, she will just go with it anyway
                        if "nogirls" not in StormX.RecentActions:
                                $ StormX.Statup("Love", 80, -2)
                                $ StormX.Statup("Obed", 80, 2)
                                $ StormX.AddWord(1,"nogirls",0,0,0) #recent
                        return
                ch_s "Не дави на меня. . ."
        else:
                $ StormX.Statup("Inbt", 50, 2)
                ch_s "Как я уже сказала, я не уверена, что хочу таких отношений. . ."
                $ StormX.AddWord(1,0,"nogirls",0,0) #daily
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Storm_69_Intro:
        if "69" in StormX.History:
                return
        if Trigger == "lick pussy" and StormX.LickP:
                if StormX.Blow or StormX.CUN or (ApprovalCheck(StormX, 1300) and StormX.SeenPeen):
                        #if licking pussy but have gotten blowjob
                        $ StormX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_s "Я должна отплатить тебе тем же. . ."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        if "cockout" not in Player.RecentActions:
                                $ Player.RecentActions.append("cockout")
                                if Player.Male:
                                        "Она вытаскивает ваш член и начинает его сосать."
                                else:
                                        "Она обнажает вашу киску и начинает лизать ее."
                        else:
                                if Player.Male:
                                        "Она берет в руки ваш член и располагается над ним."
                                else:
                                        "Она начинает лизать вашу киску."
                        $ StormX.Pose = "69"
                        call Storm_BJ_Launch
                        if not Player.Male:
                            ch_s "[StormX.Petname], не могла бы ты, пожалуйста, приступить. . ?"
                        else:
                            ch_s "[StormX.Petname], не мог бы ты, пожалуйста, приступить. . ?"
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ StormX.Statup("Love", 95, 3)
                                    $ StormX.Statup("Inbt", 70, 2)
                                    $ StormX.Statup("Inbt", 90, 1)
                                    ch_s "Восхитительно."
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ StormX.Statup("Love", 80, -8)
                                    $ StormX.Statup("Obed", 80, 3)
                                    $ StormX.Statup("Obed", 90, 1)
                                    $ StormX.Statup("Inbt", 70, -1)
                                    ch_s "Очень жаль."
                        $ Situation = "69"
                        call SexAct("blow") # call Storm_SexAct("blow")
                        $ renpy.pop_call() #causes it to skip past the Escalation
                        $ renpy.pop_call() #causes it to skip past the last activity
        elif (Trigger == "blow" or Trigger == "cun") and (StormX.Blow or StormX.CUN):
                        #if licked pussy
                        $ StormX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_s "Пока я занята тобой. . ."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        $ StormX.Pose = "69"
                        call Storm_BJ_Launch
                        if not Player.Male:
                            ch_s ". . . не могла бы и ты позаботиться обо мне? . ."
                        else:
                            ch_s ". . . не мог бы и ты позаботиться обо мне? . ."
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ StormX.Statup("Love", 95, 3)
                                    $ StormX.Statup("Inbt", 70, 2)
                                    $ StormX.Statup("Inbt", 90, 1)
                                    ch_s "Восхитительно."
                                    if not StormX.LickP:
                                        $ StormX.LickP += 1
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ StormX.Statup("Love", 80, -5)
                                    $ StormX.Statup("Obed", 80, 3)
                                    $ StormX.Statup("Obed", 90, 1)
                                    $ StormX.Statup("Inbt", 70, -1)
                                    ch_s "Очень жаль."
                        #returns to BJ already in progress
        return
