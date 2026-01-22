
# start DoreenMeet//////////////////////////////////////////////////////////
# flow is, Prelude in which Storm asks you to look into other attic, then
# DoreenMeet in which you first meet, then you can either go to Storm to rat her out, go to Xavier to include her, or
# keep her secret for a bit. If you fail to keep her fed, she will get caught, if "SGattic" in Player.History, "SGattic" in DoreenX.History if she gets caught
# Player History: +"nightlight" if told to check on SQ but haven't yet
# Gorre History "bargain" if you leveraged her, "backsy" in history if you renegged


#    #Activates Doreen meet
#        if DoreenX in ActiveGirls:
#                    pass

#        elif "met" not in DoreenX.History and "met" in BetsyX.History:
#                    if Time_Count == 1 and "nightlight" not in Player.History:
#                            #You hadn't been told to check her yet
#                            call DoreenMeetPrelude
#                            return
#        else:
#            if "stormreport" in Player.History and bg_current == StormX.Loc or (StormX.Loc == "bg teacher" and bg_current == "bg classroom"):
#                            #if you see Storm without having reported to her, it happens
#                            call DoreenStormReport

#            elif "doreenafter" in Player.History and "doreenafter" not in Player.DailyActions and "traveling" in Player.RecentActions:
#                            #if you reported her to Storm yesterday
#                            call DoreenAftermath
#            elif "SGattic" in Player.History and "traveling" in Player.RecentActions and "Doreencheck" not in Player.DailyActions:
#                    if "stormreport" in Player.DailyActions:
#                            pass #if this all happened today, she's fine
#                    elif Time_Count == 1 and (D20 + (10*DoreenX.Event[2]) - DoreenX.Event[4]) < 18:
#                            #doreen gets caught, feeding her greatly reduces odds, odds go up over time
#                            $ Player.AddWord(1,0,"Doreencheck") #adds tag to Daily
#                            call DoreenAftermath
#    #End Doreen meet

label DoreenMeetPrelude(Teacher=0):
        #assumes Storm is in the same room as you
        if StormX.Loc == "bg teacher":
                $ Teacher = 1
        $ StormX.Loc = bg_current
        call Shift_Focus(StormX)
        call Set_The_Scene
        $ StormX.FaceChange("smile",1)
        call CleartheRoom(StormX)
        "[StormX.Name] подходит к вам."
        call Set_The_Scene
        if not Player.Male:
            ch_s "[StormX.Petname], я бы хотела, чтобы ты оказала мне одну услугу."
        else:
            ch_s "[StormX.Petname], я бы хотела, чтобы ты оказал мне одну услугу."
        ch_s "Я заметила, что последние несколько ночей на чердаке дома, что напротив моего, горит свет."
        ch_s "Насколько мне известно, там никого не должно быть."
        if not Player.Male:
            ch_s "Не могла бы ты, пожалуйста, разобраться в ситуации и доложить мне?"
        else:
            ch_s "Не мог бы ты, пожалуйста, разобраться в ситуации и доложить мне?"
        menu:
            extend ""
            "Конечно.":
                    $ StormX.Statup("Love", 70, 3)
                    $ StormX.Statup("Love", 90, 2)
                    ch_s "Благодарю, буду с нетерпением ждать твоего доклада."
            "Нет.":
                    $ StormX.FaceChange("sad",1)
                    $ StormX.Statup("Love", 80, -2)
                    $ StormX.Statup("Obed", 60, 3)
                    $ StormX.Statup("Obed", 80, 1)
                    ch_s "Что ж, жаль."
                    ch_s "Тогда, пожалуй, мне придется поискать кого-нибудь другого."
            "Что мне за это будет?":
                    $ StormX.Statup("Love", 70, -2)
                    $ StormX.Statup("Obed", 60, 2)
                    if not ApprovalCheck(StormX, 1200):
                            $ StormX.FaceChange("confused",1)
                            if not Player.Male:
                                ch_s "Ты меня разочаровала."
                            else:
                                ch_s "Ты меня разочаровал."
                            $ StormX.FaceChange("angry",1)
                            ch_s "Я просто попросила об одолжении."
                            ch_s "Как бы то ни было, я по-прежнему жду, что ты разберешься с этим."
                            if not Player.Male:
                                ch_s "Однако ты упустила возможность подружиться со мной."
                            else:
                                ch_s "Однако ты упустил возможность подружиться со мной."
                    else:
                            $ StormX.FaceChange("sly",1)
                            $ StormX.Statup("Obed", 80, 3)
                            ch_s "Это удивительно меркантильно с твоей стороны. . ."
                            ch_s "Давай посмотрим. . ."
                            if bg_current != "bg player" and bg_current != "bg storm":
                                    "Она приводит вас обратно в вашу комнату."
                                    $ bg_current = "bg player"
                            call CleartheRoom("All",0,1)
                            $ StormX.Loc = bg_current
                            call Set_The_Scene
                            $ Count2 = 2
                            $ StormX.Event[4] += 1
                            $ StormX.RecentActions.append("drugfree")
                            call Ultimatum(StormX,20)
                            $ StormX.RecentActions.remove("drugfree")
                            if "deal Storm" not in Player.RecentActions:
                                    $ StormX.FaceChange("angry",1)
                                    $ StormX.Statup("Love", 70, -3)
                                    $ StormX.Statup("Love", 85, -2)
                                    $ StormX.Statup("Obed", 50, -6)
                                    if not Player.Male:
                                        ch_s "Ты меня разочаровала."
                                    else:
                                        ch_s "Ты меня разочаровал."
                                    $ StormX.FaceChange("sly",1)
                                    $ StormX.Statup("Obed", 80, 3)
                                    ch_s "Мы оба могли получить свою. . . выгоду."
                                    $ StormX.FaceChange("angry",1)
                                    ch_s "Как бы то ни было, я по-прежнему жду, что ты разберешься с этим."
                                    $ StormX.FaceChange("sly",1)
                                    if not Player.Male:
                                        ch_s "Однако ты упустила возможность получить \"бонус\"."
                                    else:
                                        ch_s "Однако ты упустил возможность получить \"бонус\"."
                            else:
                                    if StormX.Forced:
                                        $ StormX.FaceChange("sly",1,Brows="angry")
                                        $ StormX.Statup("Love", 70, -2)
                                    else:
                                        $ StormX.FaceChange("sly",1)
                                    $ StormX.Statup("Obed", 80, 3)
                                    $ StormX.Statup("Obed", 95, 2)
                                    ch_s "Надеюсь, этого будет достаточно. . ."
                                    $ StormX.Statup("Obed", 60, 3)
                                    $ StormX.FaceChange("sly",1)
                                    ch_s "И надеюсь, что скоро узнаю результаты твоего расследования."
        $ Player.AddWord(1,0,0,0,"nightlight") #adds tag to History
        $ Player.AddWord(1,0,"Intro",0,0) #adds tag to Daily
        if Teacher:
                $ StormX.FaceChange("normal",1)
                $ StormX.Loc = "bg teacher"
                call Set_The_Scene
                if bg_current != "bg classroom":
                        "[StormX.Name] уходит."
        return

label DoreenMeet:
        #after DoreenMeetPrelude, you enter the attic. . .
        $ Player.History.remove("nightlight")
        $ Player.AddWord(1,0,"stormreport",0,"stormreport") #adds tag to History
        "Вы поднимаетесь по лестнице, расположенной с обратной стороны здания, на чердак."
        $ bg_current = "bg doreen"
        $ DoreenX.OutfitDay = "casual1"
        $ DoreenX.Outfit = "casual1"
        $ DoreenX.OutfitChange("casual1")
        call CleartheRoom("All",0,1)
        $ DoreenX.Break[0] = 0            #resets counter
        $ DoreenX.Loc = 0
        $ DoreenX.Love = 650
        $ DoreenX.Obed = 0
        $ DoreenX.Inbt = 0
        if not Player.Male:
            $ DoreenX.Petname = "Чувиха"
            $ DoreenX.Petname_rod = "Чувихи"
            $ DoreenX.Petname_dat = "Чувихе"
            $ DoreenX.Petname_vin = "Чувиху"
            $ DoreenX.Petname_tvo = "Чувихой"
            $ DoreenX.Petname_pre = "Чувихе"
        else:
            $ DoreenX.Petname = "Чувак"
            $ DoreenX.Petname_rod = "Чувака"
            $ DoreenX.Petname_dat = "Чуваку"
            $ DoreenX.Petname_vin = "Чувака"
            $ DoreenX.Petname_tvo = "Чуваком"
            $ DoreenX.Petname_pre = "Чуваке"
        $ DoreenX.Names = ["Doreen"]
        call Shift_Focus(DoreenX)
        call Set_The_Scene
        $ DoreenX.Loc = "bg doreen"
        $ DoreenX.SpriteLoc = StageCenter
        "Здесь довольно пусто, похоже, помещение используется в основном в качестве склада. В углу несколько коробок синих и желтых комбинезонов."
        menu:
            "Еще немного осмотреться.":
                    "Вы заглядываете за коробки."
            "Уйти":
                    pass
        "После этого из-за одной из них вылетает коричневое нечто и бросается прямиком в ваше лицо."
        menu:
            "Бежать!":
                    "Вы разворачиваетесь и начинаете убегать, но понимаете, что вы не знаете, в каком направлении находится дверь."
                    "В панике вы создаете ауру антиспособностей."
            "Сконцентрироваться на своей способности.":
                    "Вы концентрируетесь на своих силах и создаете ауру антиспособностей."

        $ DoreenX.FaceChange("normal",Eyes="side")

        show expression AlphaMask("SilhouetteBase", At("Doreen_Sprite", SpriteLoc(DoreenX.SpriteLoc))) as mask:
            offset (350,50)#(260,50)

        ch_u "! ! !"
        "Коричневое нечто на мгновение останавливается, а затем убегает."
        ch_u "Типпи, ты куда?!"
        "Вы поворачиваетесь в сторону голоса и видите темную фигуру, наблюдающую за вами из тени."
        $ DoreenX.FaceChange("surprised",1)
        ch_u "Эм, извини за это!"

        hide mask with fade
        show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc)


        menu:
            extend ""
            "Ты кто?":
                    pass
            "О, \"девушка-белка.\"":
                    $ DoreenX.Statup("Love", 80, -1)
                    $ DoreenX.Statup("Obed", 80, 2)
                    $ DoreenX.Statup("Inbt", 80, -1)
                    $ DoreenX.FaceChange("confused",2)
                    $ DoreenX.Names.append("Squirrel Girl")
                    ch_u "Эм. . ."
                    ch_u "Ага."
            "Грабитель!":
                    $ DoreenX.Statup("Obed", 80, 5)
                    $ DoreenX.Statup("Inbt", 70, 1)
                    $ DoreenX.FaceChange("surprised",1,Brows="sad")
                    ch_u "Нененене!"
                    ch_u "Я не грабитель!"
        $ DoreenX.FaceChange("smile",1)
        ch_u "Я просто. . . Хочу здесь учиться!"
        $ DoreenX.Armpose = 2
        ch_u "-и меня зовут Дорин!"
        $ DoreenX.Name = "Дорин"
        $ DoreenX.Name_rod = "Дорин"
        $ DoreenX.Name_dat = "Дорин"
        $ DoreenX.Name_vin = "Дорин"
        $ DoreenX.Name_tvo = "Дорин"
        $ DoreenX.Name_pre = "Дорин"
        ch_d "Дорин Грин, рада познакомиться!"
        $ DoreenX.AddWord(1,0,0,0,"met") #adds "word" tag to History
        $ Count2 = 3
        while Count2:
            $ Count -= 1
            menu:
                extend ""
                "Что это было за коричневое. . . нечто?" if "tippy" not in DoreenX.RecentActions:
                        $ DoreenX.Statup("Love", 80, 1)
                        $ DoreenX.FaceChange("bemused",2,Eyes="side")
                        ch_d "О, это была моя. . . подруга."
                        ch_d "Ее зовут Типпи То."
                        ch_d "Она белка."
                        $ DoreenX.FaceChange("smile",1)
                        ch_d "Я умею разговаривать с белками."
                        $ DoreenX.FaceChange("confused",1)
                        ch_d "Если подумать, почему минуту назад она не послушалась меня?"
                        ch_d "Это из-за твоей способности?"
                        ch_d "Ты -тоже- умеешь разговаривать с белками?"
                        $ DoreenX.Names.append("Squirrel Girl") if "Squirrel Girl" not in DoreenX.Names else 0
                        menu:
                            extend ""
                            "Да.":
                                    $ DoreenX.Statup("Love", 80, 5)
                                    $ DoreenX.Statup("Inbt", 200, 5)
                                    $ DoreenX.FaceChange("smile",1)
                                    ch_d "Здорово!"
                                    $ DoreenX.FaceChange("confused",1)
                                    ch_d "Нет, подожди. . . "
                                    if not Player.Male:
                                        ch_d "-если бы это было так, я бы услышала, что ты ей сказала."
                                    else:
                                        ch_d "-если бы это было так, я бы услышала, что ты ей сказал."
                                    $ DoreenX.Statup("Love", 80, -4)
                                    $ DoreenX.Statup("Obed", 80, 3)
                                    $ DoreenX.Statup("Inbt", 200, -2)
                                    $ DoreenX.FaceChange("smile",1)
                                    ch_d "Уверена, ты просто можешь блокировать другие способности."
                            ". . .":
                                    $ DoreenX.Statup("Obed", 80, 1)
                                    $ DoreenX.Statup("Inbt", 200, 3)
                                    if not Player.Male:
                                        ch_d "-если бы это было так, я бы услышала, что ты ей сказала."
                                    else:
                                        ch_d "-если бы это было так, я бы услышала, что ты ей сказал."
                                    $ DoreenX.FaceChange("smile",1)
                                    ch_d "Уверена, ты просто можешь блокировать другие способности."
                            "Я могу блокировать способности других мутантов.":
                                    $ DoreenX.Statup("Obed", 80, 2)
                                    $ DoreenX.FaceChange("smile",1)
                                    ch_d "О, тогда понятно."
                        $ DoreenX.RecentActions.append("tippy")
                "Что ты здесь делаешь?" if "why" not in DoreenX.RecentActions:
                        $ DoreenX.Statup("Love", 70, 3)
                        $ DoreenX.FaceChange("smile",1,Brows="sad")
                        ch_d "Я просто. . . пытаюсь получить образование."
                        $ DoreenX.FaceChange("sadside",1)
                        ch_d "С огромным хвостом ходить в большинство учебных заведений немного сложновато."
                        ch_d "И да, я не могу \"спрятать его в штанах,\" или типа того."
                        ch_d "Институт Ксавье - моя единственная надежда."
                        ch_d "К сожалению, я уже -целую вечность- в списке ожидания!"
                        $ DoreenX.FaceChange("angry",1)
                        $ DoreenX.Armpose = 1
                        ch_d "-поэтому я решила взять дело в свои руки!"
                        $ DoreenX.RecentActions.append("why")
                "[[Уйти]":
                        $ Count2 = 0
                        "Вы разворачиваетесь, чтобы уйти."
                        $ DoreenX.FaceChange("surprised",1,Brows="sad")
                        $ DoreenX.Statup("Love", 70, -2)
                        $ DoreenX.Statup("Obed", 80, 3)
                        "Дорин хватает вас за руку."
                        ch_d "Нет, подожди! Я просто хочу заниматься здесь!"
        menu:
            extend ""
            "В этом есть смысл. Тебе нужна помощь?":
                    $ DoreenX.Statup("Obed", 80, 1)
                    $ DoreenX.FaceChange("sadside",1)
                    ch_d "Я думаю, тебе придется отчита-"
                    $ DoreenX.FaceChange("surprised",1,Mouth="smile")
                    ch_d "Что, правда?!"
                    $ DoreenX.Statup("Love", 80, 10)
                    $ DoreenX.Statup("Inbt", 200, 3)
                    $ DoreenX.FaceChange("smile",1)
                    ch_d "Ты хочешь мне помочь?!"
                    menu:
                        extend ""
                        "Конечно, почему нет.":
                                $ DoreenX.Statup("Love", 80, 10)
                                ch_d "Спасибо! Это потрясающе!"
                                jump DoreenMeetEnd          #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
                        "Да я шучу, тебе место в тюрьме.":
                                $ DoreenX.Statup("Love", 80, -15)
                                $ DoreenX.Statup("Obed", 80, 5)
                                $ DoreenX.FaceChange("angry",1)
            "Извини, мне нужно сообщить о твоем присутствии.":
                    $ DoreenX.Statup("Love", 70, 2)
                    $ DoreenX.FaceChange("sad",1)
            "Ладно, мне пора сообщить о твоем присутствии.":
                    $ DoreenX.Statup("Love", 70, -5)
                    $ DoreenX.FaceChange("angry",1)
        $ DoreenX.Statup("Obed", 80, 3)
        $ DoreenX.Statup("Inbt", 200, 5)
        ch_d "Ненененене!"
        $ DoreenX.FaceChange("surprised",1,Brows="sad")
        ch_d "Пожалуйста, не выдавай меня!"
        ch_d "Я хорошая девочка, честно-честно!"
        ch_d "Позволь мне остаться здесь!"
        menu:
            extend ""
            "Думаю, я могу попытаться объяснить всю ситуацию Ксавье.":
                    $ DoreenX.Statup("Love", 70, 10)
                    $ DoreenX.Statup("Obed", 80, 2)
                    $ DoreenX.FaceChange("smile",1)
                    ch_d "Правда?! Спасибо!!!"
                    jump DoreenMeetEnd
            "Не, меня это не волнует.":
                    $ DoreenX.Statup("Love", 80, -3)
                    $ DoreenX.Statup("Obed", 80, 3)
                    $ DoreenX.Statup("Inbt", 200, 3)
                    ch_d "Оу, да ладно тебе! Может, я смогу тебя как-нибудь убедить?"
            "Что я с этого получу?":
                    $ DoreenX.Statup("Love", 70, -5)
                    $ DoreenX.Statup("Obed", 80, 7)
                    $ DoreenX.FaceChange("angry",1,Eyes="side")
                    ch_d "Ох, ну. . . надо подумать. . ."
        $ Count2 = 3
        $ DoreenX.Event[4] += 1
        $ DoreenX.RecentActions.append("drugfree")
        $ Player.AddWord(1,"interruption") #adds to Recent
        call Ultimatum(DoreenX,20)
        $ DoreenX.RecentActions.remove("drugfree")
        if "deal Doreen" in Player.RecentActions:
                #if she did anything for you
                $ DoreenX.Statup("Love", 80, -5)
                $ DoreenX.Statup("Obed", 80, 10)
                $ DoreenX.AddWord(1,0,0,0,"bargain") #history
        elif "backsy" in DoreenX.RecentActions:
                $ DoreenX.Statup("Love", 80, -15)
                $ DoreenX.Statup("Obed", 80, 5)
                $ DoreenX.Statup("Inbt", 200, 5)
                $ DoreenX.FaceChange("angry",1)
                if not Player.Male:
                    ch_d "Не могу поверить, что ты нарушил свое обещание, я это запомню!"
                else:
                    ch_d "Не могу поверить, что ты нарушил свое обещание, я это запомню!"
                $ DoreenX.AddWord(1,0,0,0,"bargain") #history
        ch_d "Ладно, и что дальше?"
        menu:
            extend""
            "Пойдем, пора зачислить тебя в институт.":
                    $ DoreenX.Statup("Love", 70, 5)
                    $ DoreenX.Statup("Obed", 80, 3)
                    $ DoreenX.FaceChange("smile",1)
                    if "backsy" in DoreenX.RecentActions:
                            $ DoreenX.Statup("Love", 80, 5)
                            $ DoreenX.Statup("Obed", 80, -2)
                            ch_d "Правда?! Спасибо!"
                            $ DoreenX.DrainWord("backsy",1,1,0,1) # removes from history
                    jump DoreenMeetEnd          #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
            "Я могу помочь тебе прятаться.":
                    $ DoreenX.Statup("Love", 70, 2)
                    $ DoreenX.Statup("Obed", 80, 3)
                    $ DoreenX.FaceChange("confused",1)
            "Я пойду.":
                    $ DoreenX.Statup("Love", 70, -5)
                    $ DoreenX.Statup("Obed", 80, 3)
                    $ DoreenX.FaceChange("surprised",1)
                    ch_d "Что?!"
                    if "deal Doreen" in Player.RecentActions:
                            $ DoreenX.FaceChange("angry",1)
                            if not Player.Male:
                                ch_d "Но ты обещала!"
                            else:
                                ch_d "Но ты обещал!"
                    menu:
                        extend ""
                        "Извини, пойдем, пора зачислить тебя в институт.":
                                $ DoreenX.Statup("Love", 70, 5)
                                $ DoreenX.Statup("Obed", 80, -1)
                                $ DoreenX.FaceChange("smile",1)
                                if "backsy" in DoreenX.RecentActions:
                                        $ DoreenX.Statup("Love", 70, 5)
                                        $ DoreenX.FaceChange("confused",1)
                                        ch_d "Правда?! Спасибо!"
                                        $ DoreenX.DrainWord("backsy",1,1,0,1) # removes from history
                                jump DoreenMeetEnd          #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
                        "Я могу помочь тебе прятаться.":
                                $ DoreenX.Statup("Love", 70, 3)
                                $ DoreenX.Statup("Obed", 80, 5)
                                $ DoreenX.FaceChange("confused",1)
                        "Ага, что я могу сказать, облом.":
                                $ DoreenX.Statup("Love", 70, -5)
                                $ DoreenX.Statup("Obed", 80, 3)
                                $ DoreenX.FaceChange("sadside",1)
                                ch_d "Черт!"
                                "Вы спускаетесь вниз по лестнице."
                                menu:
                                    extend ""
                                    "Сдать ее Шторм?":
                                            call DoreenStormReport          #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
                                    "Просто вернуться в свою комнату.":
                                            $ bg_current = "bg player"
                                            jump Misplaced          #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint

        #"I can help you hide out."
        ch_d "Что?"
        $ DoreenX.FaceChange("surprised",1)
        ch_d "Я надеялась, что ты просто замолвишь за меня словечко перед профессором Ксавье."
        $ DoreenX.FaceChange("perplexed",1)
        ch_d "Может, попробуем сперва сделать так?"
        menu:
            extend ""
            "Ох, ладно, пойдем.":
                    $ DoreenX.Statup("Love", 70, 5)
                    $ DoreenX.FaceChange("smile",1)
                    if "backsy" in DoreenX.RecentActions:
                            $ DoreenX.Statup("Love", 70, 5)
                            ch_d "Правда?! Спасибо!"
                            $ DoreenX.DrainWord("backsy",1,1,0,1) # removes from history
                    else:
                            $ DoreenX.Statup("Obed", 80, 5)
                            $ DoreenX.FaceChange("confused",1)
                            ch_d ". . . спасибо."
                    jump DoreenMeetEnd          #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
            "Не думаю, что это сработает.":
                    $ DoreenX.Statup("Obed", 80, 5)
                    $ DoreenX.Statup("Inbt", 200, 5)
                    $ DoreenX.FaceChange("sadside",1)
                    ch_d "Ох. . ."
        menu:
            extend ""
            "Ты можешь прятаться здесь, я тебя прикрою.":
                    $ DoreenX.Statup("Love", 70, 3)
                    $ DoreenX.Statup("Obed", 80, 10)
                    $ DoreenX.Statup("Inbt", 200, 5)
                    $ DoreenX.FaceChange("sad",1)
                    ch_d "Хорошо. . ."
            ". . .":
                    $ DoreenX.Statup("Love", 70, -2)
                    $ DoreenX.Statup("Inbt", 200, 5)
        if "backsy" in DoreenX.RecentActions:
                $ DoreenX.DrainWord("backsy",1,1,0,1) # removes from history
        $ DoreenX.FaceChange("sadside",1)
        $ DoreenX.Event[2] = 4
        ch_d "Думаю, я могу остаться здесь ненадолго."
        ch_d "Я так долго этого хотела. . ."
        call DoreenMeetShake
        "Вы спускаетесь по лестнице."
        menu:
            extend ""
            "Сдать ее Шторм?":
                    call DoreenStormReport          #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
            "Просто вернуться в свою комнату.":
                    $ bg_current = "bg player"
                    $ Player.AddWord(1,0,0,0,"SGattic") #adds tag to History
                    jump Misplaced          #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint

label DoreenStormReport(Deliberate=0,Teacher=0):
        #if you rat her out to Storm
        # Deliberate is called from Storm's chat menu,
        # if "SGattic" in Player.History:
        # call DoreenStormReport(1)
        $ bg_current = "bg campus"
        $ Player.History.remove("stormreport") if "stormreport" in Player.History else 0
        if StormX.Loc == "bg teacher":
                $ Teacher = 1
        $ StormX.Loc = bg_current
        call Shift_Focus(StormX)
        call Set_The_Scene
        "Вы видите [StormX.Name_vin] в коридоре."
        $ StormX.FaceChange("smile",0)
        if Deliberate:
                    ch_s "Можешь что-то добавить по поводу чердака?"
        else:
                    if not Player.Male:
                        ch_s "О, [StormX.Petname], ты изучила чердак?"
                    else:
                        ch_s "О, [StormX.Petname], ты изучил чердак?"
        menu:
            extend ""
            "Там живет девушка по имени Дорин.":
                    $ StormX.FaceChange("surprised")
                    $ StormX.Statup("Love", 80, 3)
            "Похоже, на всех чердаках живет странная девушка.":
                    $ StormX.FaceChange("surprised")
                    $ StormX.Statup("Obed", 80, 2)
                    $ StormX.Statup("Inbt", 70, 2)
            "Пока все нормально." if Deliberate:
                    ch_s "Что ж, ну хорошо. . ."
                    if Teacher:
                            $ StormX.Loc = "bg teacher"
                            call Set_The_Scene
                    return
            "Там что-то с проводкой. Я разберусь." if not Deliberate:
                    $ StormX.FaceChange("sly")
                    $ StormX.Statup("Love", 70, 3)
                    $ StormX.Statup("Obed", 80, 2)
                    ch_s "Ох, тогда оставляю это на тебе."
                    $ Player.AddWord(1,0,0,0,"SGattic") #adds tag to History
                    if Teacher:
                            $ StormX.Loc = "bg teacher"
                            call Set_The_Scene
                    return
        "Вы вкратце пересказываете ей разговор с Дорин."
        ch_s "Вот как? . ."
        $ StormX.FaceChange("bemused")
        ch_s "Что ж, пожалуй, у всех бывают сложные жизненные ситуации."
        ch_s "Я поговорю с ней и посмотрю, что мы можем сделать."
        if not Player.Male:
            ch_s "Спасибо, что все проверила."
        else:
            ch_s "Спасибо, что все проверил."
        if Teacher:
                $ StormX.Loc = "bg teacher"
        else:
                $ StormX.Loc = "bg storm"
        call Set_The_Scene
        "Она уходит, чтобы во всем разобраться."
        $ Player.AddWord(1,0,"doreenafter",0,"doreenafter") #adds tag to History
        jump Misplaced

label DoreenAftermath:
        #called the day after you rat her out to Storm
        $ ActiveGirls.append(DoreenX) if DoreenX not in ActiveGirls else ActiveGirls
        $ bg_current = "bg campus"
        $ DoreenX.Loc = bg_current
        $ DoreenX.FaceChange("smile",1)
        call Set_The_Scene
        "Когда вы проходите через площадь, [DoreenX.Name] натыкается на вас."
        ch_d "О, привет!"
        ch_d "[Player.Name]!"
        ch_d "Знаешь, что случилось?!"
        menu:
            extend ""
            "Тебе позволили остаться?":
                    $ DoreenX.Statup("Love", 70, 5)
                    $ DoreenX.Statup("Inbt", 60, 2)
                    ch_d "Ага!"
            "Что?":
                    $ DoreenX.Statup("Inbt", 60, 3)
                    ch_d "Мне сказали, что я могу остаться!"
            "А! Ты еще здесь!":
                    $ DoreenX.Statup("Obed", 80, 2)
                    ch_d "Ага!"
        if "SGattic" in Player.History:
                if not Player.Male:
                    ch_d "Спасибо, что поговорила от моего имени с мисс Манро!"
                else:
                    ch_d "Спасибо, что поговорил от моего имени с мисс Манро!"
                ch_d "Она пришла ко мне и сказала, что все понимает."
        else:
                ch_d "Я случайно наткнулась на мисс Манро и подумала, что все, это конец!"
                ch_d "Но потом я ей все объяснила, и она отнеслась к этому очень спокойно."
                ch_d "Похоже, мы зря беспокоились!"
        if Player.Name not in DoreenX.Petnames:
                $ DoreenX.Petnames.append(Player.Name)# if Player.Name not in DoreenX.Petnames else 0
                $ DoreenX.Statup("Love", 70, -5)
                ch_d "И да, кстати, она сказала мне твое имя."
        ch_d "Она поговорила с профессором Ксавье и теперь я официально студентка!"
        menu:
            extend ""
            "Это отлично!":
                    $ DoreenX.Statup("Love", 70, 5)
                    ch_d "Правда?!"
            "Хм.":
                    $ DoreenX.Statup("Obed", 80, 2)
                    ch_d "Да?!"
            "Какая досада.":
                    $ DoreenX.FaceChange("confused",1)
                    if "SGattic" in Player.History:
                            $ DoreenX.Statup("Love", 70, -5)
                            $ DoreenX.Statup("Obed", 80, 3)
                            $ DoreenX.Statup("Inbt", 70, 3)
                            ch_d "Ты не очень хороший человек, да?"
                    else:
                            $ DoreenX.Statup("Love", 70, -3)
                            $ DoreenX.Statup("Obed", 80, 3)
                            ch_d "Что?!"
                            ch_d "Я думала, ты порадуешься за меня!"
        $ DoreenX.FaceChange("smile",1)
        ch_d "В общем, мне нужно кое-что еще уладить."
        ch_d "Увидимся, [Player.Name]!"
        $ DoreenX.Loc = "bg doreen"
        call Set_The_Scene
        $ DoreenX.AddWord(1,0,0,0,"SGattic") #adds tag to History
        if "Doreen" not in GwenX.History:
                $ GwenX.History.append("Doreen")
        $ Player.History.remove("SGattic") if "SGattic" in Player.History else 0
        $ Player.History.remove("stormreport") if "stormreport" in Player.History else 0
        $ Player.History.remove("doreenafter") if "doreenafter" in Player.History else 0
        return

label DoreenMeetEnd:
        #if you take her to see Xavier
        $ bg_current = "bg study"
        $ DoreenX.Loc = bg_current
        $ Player.History.remove("SGattic") if "SGattic" in Player.History else 0
        $ Player.History.remove("stormreport") if "stormreport" in Player.History else 0
        $ Player.History.remove("doreenafter") if "doreenafter" in Player.History else 0
        call Set_The_Scene
        show Professor at SpriteLoc(StageLeft) zorder 25
        "Вы вдвоем отправляетесь в кабинет Ксавье."
        ch_x "О, мисс Грин. Я не ожидал увидеть вас сегодня."
        $ DoreenX.FaceChange("sadside",1,Mouth="smirk")
        ch_d "Ох, эм. . ."
        menu:
            extend ""
            "Я очень надеюсь, вы сможете принять ее к нам институт.":
                        $ DoreenX.Statup("Love", 80, 10)
                        $ DoreenX.Statup("Obed", 80, 3)
                        $ DoreenX.FaceChange("smile",1)
                        ch_d "Я думаю, из меня вышла бы отличная студентка, сэр!"
                        ch_x "Хм. . ."
            "Я нашла ее на чердаке, она там пряталась." if not Player.Male:
                        $ DoreenX.Statup("Love", 70, -7)
                        $ DoreenX.Statup("Obed", 80, 5)
                        $ DoreenX.Statup("Inbt", 70, 5)
                        $ DoreenX.FaceChange("angry",1)
                        if "deal Doreen" in Player.RecentActions:
                                $ DoreenX.Statup("Love", 70, -5)
                                $ DoreenX.Statup("Obed", 80, 3)
                                ch_d "Эй!"
                        $ DoreenX.RecentActions.append("betrayal")
                        ch_x "Значит, взлом и проникновение?"
            "Я нашел ее на чердаке, она там пряталась." if Player.Male:
                        $ DoreenX.Statup("Love", 70, -7)
                        $ DoreenX.Statup("Obed", 80, 5)
                        $ DoreenX.Statup("Inbt", 70, 5)
                        $ DoreenX.FaceChange("angry",1)
                        if "deal Doreen" in Player.RecentActions:
                                $ DoreenX.Statup("Love", 70, -5)
                                $ DoreenX.Statup("Obed", 80, 3)
                                ch_d "Эй!"
                        $ DoreenX.RecentActions.append("betrayal")
                        ch_x "Значит, взлом и проникновение?"
            "Ага, это очень странно.":
                        $ DoreenX.Statup("Love", 70, -3)
                        $ DoreenX.Statup("Obed", 80, 2)
                        $ DoreenX.Statup("Inbt", 70, 5)
                        $ DoreenX.FaceChange("angry",1)
                        if "deal Doreen" in Player.RecentActions:
                                $ DoreenX.Statup("Love", 70, -3)
                                $ DoreenX.Statup("Obed", 80, 5)
                                ch_d "Эй!"
                                $ DoreenX.RecentActions.append("betrayal")
                        ch_x "Данная \"неожиданность\" не обязательно является чем-то плохим. . ."
        $ DoreenX.FaceChange("smile",1,Eyes="side")
        ch_x "Мисс Грин, ваши действия демонстрируют определенный уровень. . . креативности."
        ch_x "Что до ваших достижений в учебе. . . что ж, они всегда были безупречны."
        ch_x "Я немного сомневался, сможете ли вы вписаться в нашу учебную программу."
        ch_x "Мне понравилась ваша настойчивость, пожалуй, я могу дать вам шанс проявить себя. . ."
        $ DoreenX.FaceChange("smile",1,Eyes="side",Brows="surprised")
        ch_x "Считайте, что вы приняты."
        $ DoreenX.FaceChange("smile",1,Eyes="side")
        ch_x "Вы можете оставить себе место на чердаке и переделать его по своему усмотрению."
        ch_x "Ждем вас на занятиях."
        ch_d "Спасибо вам, сэр!"
        ch_d "Вы об этом не пожалеете!"
        $ ActiveGirls.append(DoreenX) if DoreenX not in ActiveGirls else ActiveGirls
        if "betrayal"  in DoreenX.RecentActions:
                $ DoreenX.Statup("Love", 70, -5)
                $ DoreenX.FaceChange("angry",1)
                ch_d "Все получилось даже без твоей помощи-"
                ch_d "-подожди-ка. . ."
        else:
                $ DoreenX.Statup("Love", 80, 5)
                $ DoreenX.Statup("Inbt", 70, 5)
                $ DoreenX.FaceChange("smile",1)
                ch_d "И тебе тоже спасибо-"
                $ DoreenX.FaceChange("angry",1,Eyes="down")
                ch_d "-подожди-ка. . ."
                $ DoreenX.FaceChange("smile",1)
        ch_d "Я так и не узнала твоего имени."
        $ DoreenX.FaceChange("smile",1,Eyes="side")
        if not Player.Male:
            ch_x "Ее зовут [Player.Name]."
        else:
            ch_x "Его зовут [Player.Name]."
        $ DoreenX.Petnames.append(Player.Name) if Player.Name not in DoreenX.Petnames else 0
        if "betrayal"  in DoreenX.RecentActions:
                if not Player.Male:
                    ch_x "Боюсь, она может быть весьма. . . оригинальной."
                else:
                    ch_x "Боюсь, он может быть весьма. . . оригинальным."
        $ DoreenX.FaceChange("smile",1)
        if "betrayal"  in DoreenX.RecentActions:
            ch_d "Ну спасибо тебе, [Player.Name]."
        else:
            ch_d "Большое спасибо, [Player.Name]."
        call DoreenMeetShake
        ch_d "В общем. . . еще. . . увидимся. . ."
        $ DoreenX.Loc = "bg doreen"
        "Вы возращаетесь к себе."
        if "Doreen" not in GwenX.History:
                $ GwenX.History.append("Doreen")
        $ bg_current = "bg player"
        jump Misplaced          #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
        return

label DoreenXavierReport:
        #called from Xavier's study if you rat her out.
        #if you take her to see Xavier
        ch_x "Что ты хочешь мне сказать?"
        menu:
            extend ""
            "В кампусе есть девушка по имени [DoreenX.Name].":
                pass
            "Неважно.":
                ch_x "Что ж, хорошо. . ."
                return
        menu:
            extend ""
            "Я очень надеюсь, вы сможете принять ее к нам институт.":
                        ch_x "Хм. . ."
            "Я нашла ее на чердаке, она там пряталась." if not Player.Male:
                        ch_x "Значит, взлом и проникновение?"
            "Я нашел ее на чердаке, она там пряталась." if Player.Male:
                        ch_x "Значит, взлом и проникновение?"
            "Это очень странно.":
                        ch_x "Данная \"неожиданность\" не обязательно является чем-то плохим. . ."
        ch_x "Я провел краткое сканирование и обнаружил ее."
        ch_x "Мисс Грин продемонстрировала определенный уровень. . . креативности."
        ch_x "Что до ее достижений в учебе. . . что ж, они всегда были безупречны."
        ch_x "У немного сомневался, сможет ли она вписаться в нашу учебную программу."
        ch_x "Мне понравилась ее настойчивость, пожалуй, я могу дать ей шанс проявить себя. . ."
        ch_x "В общем, можешь считать, что она принята."
        ch_x "Она может оставить себе место на чердаке и переделать его по своему усмотрению."
        if "Doreen" not in GwenX.History:
                $ GwenX.History.append("Doreen")
        $ Player.History.remove("stormreport") if "stormreport" in Player.History else 0
        $ Player.AddWord(1,0,"doreenafter",0,"doreenafter") #adds tag to History
        return

label DoreenMeetShake:
        #at the end of the meeting, she shakes your hand
        if "deal Doreen" in Player.RecentActions:
                if "betrayal"  in DoreenX.RecentActions:
                        $ DoreenX.Statup("Love", 70, 2)
                        $ DoreenX.Statup("Obed", 80, 2)
                        $ DoreenX.FaceChange("sad",1)
                else:
                        $ DoreenX.Statup("Love", 80, 3)
                        $ DoreenX.Statup("Inbt", 70, 4)
                        $ DoreenX.FaceChange("smile",1)
                ch_d "В общем, я надеюсь, что мы сможем поладить."
                ch_d "Возможно, однажды мы сможем стать хорошими друзьями."
        else:
                $ DoreenX.Statup("Love", 80, 3)
                $ DoreenX.Statup("Inbt", 70, 3)
                $ DoreenX.FaceChange("smile",1)
                ch_d "В общем, было приятно с тобой познакомиться."
                ch_d "Надеюсь, однажды мы сможем стать хорошими друзьями."
        "Она крепко пожимает вам руку."
        $ DoreenX.Addictionrate += 2
        $ DoreenX.Statup("Lust", 90, 5)
        $ DoreenX.FaceChange("surprised",2,Eyes="down")
        "Зетем быстро отшатывается, словно ее ужалили."
        $ DoreenX.FaceChange("surprised",2)
        ch_d "Воу, что это было?"
        menu:
            extend ""
            "Извини, это все моя способность.":
                    $ DoreenX.Statup("Love", 80, 4)
                    $ DoreenX.Statup("Obed", 80, 3)
                    $ DoreenX.FaceChange("smile",2,Eyes="down")
                    ch_d "Ох, ладно. . ."
            "Это все моя способность.":
                    $ DoreenX.Statup("Love", 80, 2)
                    $ DoreenX.Statup("Obed", 80, 4)
                    $ DoreenX.FaceChange("smile",2,Eyes="down")
                    ch_d "Ох, ладно. . ."
            "Что поделать, животный магнетизм.":
                    $ DoreenX.Statup("Love", 70, 4)
                    $ DoreenX.Statup("Obed", 80, 2)
                    $ DoreenX.Statup("Inbt", 70, 3)
                    $ DoreenX.FaceChange("angry",2)
                    ch_d ". . ."
                    $ DoreenX.Statup("Lust", 90, 2)
                    $ DoreenX.FaceChange("sly",2)
                    ch_d "Хех, конечно. . ."
        ch_d "Значит, твои способности вызывают это. . . ощущение. . ."
        $ DoreenX.FaceChange("smile",1)
        ch_d "Неплохо. . ."
        return
# End Doreen Meet / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Doreen visit / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Doreen_Visit:
        #called when you visit Doreen if she's hiding out.
        # Event[2] tracks how hungry she is
        # Event[4] is the count of how many times you leverage her
        if "visit" in DoreenX.RecentActions:
                return
        elif "visit" in DoreenX.DailyActions:
                return
        else:
                $ bg_current = "bg doreen"
                $ DoreenX.Loc = bg_current
                call Set_The_Scene
                $ Player.AddWord(1,"interruption") #adds to Recent
                $ DoreenX.AddWord(1,"visit","visit",0,0) #adds tag to Recent/Daily
                $ DoreenX.FaceChange("smile",1)
                if not Player.Male:
                    ch_d "Ты что-нибудь мне принесла?"
                else:
                    ch_d "Ты что-нибудь мне принес?"
                menu:
                    extend ""
                    "Ага, вот, держи, тут немного еды.":
                            #you give it freely
                            $ DoreenX.Statup("Love", 80, 5)
                            $ DoreenX.Statup("Obed", 80, 3)
                            ch_d "Спасибо!"
                    "Для начала мне нужно что-нибудь взамен.":
                            #bargaining
                            $ Count2 = 3 - DoreenX.Event[2]
                            $ DoreenX.Event[4] += 1
                            if "backsy" in DoreenX.History:
                                    #You've backed out of deals before
                                    $ Count2 -= 1 if Count2 > 1 else 0
                                    $ DoreenX.Statup("Obed", 80, 2)
                                    $ DoreenX.FaceChange("angry",1)
                                    ch_d "Только не отворачивайся от меня снова!"
                                    ch_d "Чего ты хочешь?"
                            else:
                                    $ DoreenX.FaceChange("sad",1)
                                    ch_d "Эм. . . чего ты хочешь?"
                            $ DoreenX.RecentActions.append("drugfree")
                            call Ultimatum(DoreenX,10*(Count2))   #10-30
                            $ DoreenX.RecentActions.remove("drugfree")
                            if "deal Doreen" in Player.RecentActions:
                                    #You had a deal
                                    "Вы даете ей немного еды."
                                    $ DoreenX.AddWord(1,0,0,0,"bargain") #history
                                    $ DoreenX.Statup("Love", 70, 3)
                                    $ DoreenX.Statup("Obed", 80, 5)
                                    $ DoreenX.FaceChange("smile",1)
                                    ch_d "Спасибо. . ."
                            else:
                                    $ DoreenX.FaceChange("sadside",2)
                                    ch_d "Я не могу на это пойти. . ."
                                    if "backsy" in DoreenX.RecentActions:
                                            $ DoreenX.Statup("Love", 60, -2)
                                            if "backsy" in DoreenX.History:
                                                #You did something, but didn't agree to a deal, and had done so previously
                                                $ DoreenX.Statup("Love", 80, -5)
                                                $ DoreenX.Statup("Obed", 80, 2)
                                                $ DoreenX.FaceChange("angry",1)
                                                ch_d "Ты не заслуживаешь никакого доверия!"
                                            else:
                                                #You did something, but didn't agree to a deal
                                                $ DoreenX.Statup("Love", 80, -5)
                                                $ DoreenX.Statup("Obed", 80, 8)
                                                $ DoreenX.FaceChange("angry",1)
                                                if not Player.Male:
                                                    ch_d "Я не могу поверить, что ты нарушила свое обещание, я это запомню!"
                                                else:
                                                    ch_d "Я не могу поверить, что ты нарушил свое обещание, я это запомню!"
                                                $ DoreenX.AddWord(1,0,0,0,"bargain") #history
                                    menu:
                                        extend ""
                                        "Ладно, вот, держи. . .":
                                                #You give her something after trying to back out
                                                $ Player.AddWord(1,"deal Doreen") #recent
                                                $ DoreenX.DrainWord("backsy",1,1) # removes from recent/daily
                                                $ DoreenX.Statup("Love", 80, 5)
                                                $ DoreenX.Statup("Obed", 80, 1)
                                                $ DoreenX.Statup("Inbt", 70, 1)
                                                $ DoreenX.FaceChange("confused",1)
                                                ch_d "О? Спасибо!"
                                        "Не хочешь как хочешь.":
                                                #You refuse
                                                $ DoreenX.Statup("Love", 90, -5)
                                                $ DoreenX.Statup("Obed", 80, 1)
                                                $ DoreenX.Statup("Inbt", 70, 2)
                                                $ DoreenX.FaceChange("angry",1)
                                                return
                                        ". . .":
                                                #You refuse, but have nothing to say
                                                $ DoreenX.Statup("Love", 80, -3)
                                                $ DoreenX.Statup("Obed", 80, 1)
                                                $ DoreenX.Statup("Inbt", 70, 3)
                                                $ DoreenX.FaceChange("angry",1)
                                                return
                    "Я ничего не взяла с собой." if not Player.Male:
                            #you bring nothing
                            $ DoreenX.FaceChange("sad",1)
                            ch_d "Оу. . ."
                            if DoreenX.Event[2] == 0:
                                    $ DoreenX.Statup("Love", 80, -7)
                                    $ DoreenX.Statup("Obed", 80, 5)
                                    $ DoreenX.Statup("Inbt", 70, 3)
                                    ch_d "Я умираю с голода."
                            elif DoreenX.Event[2] == 1:
                                    $ DoreenX.Statup("Love", 80, -3)
                                    $ DoreenX.Statup("Obed", 80, 5)
                                    $ DoreenX.Statup("Inbt", 70, 2)
                                    ch_d "Я хочу кушац."
                            return
                    "Я ничего не взял с собой." if Player.Male:
                            #you bring nothing
                            $ DoreenX.FaceChange("sad",1)
                            ch_d "Оу. . ."
                            if DoreenX.Event[2] == 0:
                                    $ DoreenX.Statup("Love", 80, -7)
                                    $ DoreenX.Statup("Obed", 80, 5)
                                    $ DoreenX.Statup("Inbt", 70, 3)
                                    ch_d "Я умираю с голода."
                            elif DoreenX.Event[2] == 1:
                                    $ DoreenX.Statup("Love", 80, -3)
                                    $ DoreenX.Statup("Obed", 80, 5)
                                    $ DoreenX.Statup("Inbt", 70, 2)
                                    ch_d "Я хочу кушац."
                            return
        if DoreenX.Event[2] == 0:
                #She's almost starving
                $ DoreenX.Statup("Love", 80, 2)
                $ DoreenX.Statup("Obed", 80, 3)
                ch_d "Старайся каждый день приносить мне еду."
        elif DoreenX.Event[2] == 1:
                #she's missed a meal
                $ DoreenX.Statup("Love", 80, 4)
                $ DoreenX.Statup("Obed", 80, 2)
                ch_d "Фух, я проголодалась."
        $ DoreenX.Event[2] = 2
        call DoreenPlayerName #checks to see if you've told her your name yet
        return

#        $ DoreenX.Event[2] -= 1 if DoreenX.Event[2] > 0 else 0
# End Doreen visit / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Doreen player name / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label DoreenPlayerName:
        #called if you haven't told her your name
        if len(DoreenX.Petnames) > 1:
                #returns if she already has a name for you
                return
        ch_d "Кстати, как тебя зовут?"
        menu:
            extend ""
            "Я [Player.Name].":
                $ DoreenX.Statup("Love", 70, 5)
                $ DoreenX.Petnames.append(Player.Name) if Player.Name not in DoreenX.Petnames else 0
                ch_d "О, здорово, приятно познакомиться, [Player.Name]."
            "Можешь звать меня Эл." if Player.Name != "Эл":
                $ DoreenX.Statup("Love", 70, 5)
                $ DoreenX.Petnames.append("Al")
                ch_d "О, здорово, приятно познакомиться, Эл."
            "Зови меня \"Заклинатель Белок.\"" if Player.Name != "Заклинатель Белок":
                $ DoreenX.Statup("Love", 80, 2)
                $ DoreenX.Statup("Inbt", 70, 2)
                $ DoreenX.Petnames.append("Squirrel Whisperer")
                ch_d "Я думаю, что, возможно, ты забегаешь вперед, \"Заклинатель Белок\"."
            "Тень." if Player.Name != "Тень":
                $ DoreenX.Statup("Love", 80, -2)
                $ DoreenX.Statup("Obed", 50, 1)
                ch_d "Какое-то мрачноватое прозвище."
                ch_d "Ну да ладно, \"тень\", мутанту вполне подходит."
                menu:
                    extend ""
                    "Ага.":
                            $ DoreenX.Statup("Inbt", 70, 2)
                            $ DoreenX.Petnames.append("Shadow")
                    "Больше выражения, я тебе не какая-то простая тень.":
                            $ DoreenX.Statup("Love", 80, -2)
                            $ DoreenX.Statup("Obed", 80, 2)
                            $ DoreenX.Statup("Inbt", 70, 1)
                            ch_d "Ох, извини, я не хотела тебя обидеть. . ."
                            $ DoreenX.Petnames.append("The Shadow")
                    "Так звали мою бабушку.":
                            $ DoreenX.Statup("Love", 80, 4)
                            $ DoreenX.Statup("Obed", 50, 2)
                            ch_d "Ох, извини, я не хотела тебя обидеть. . ."
                            $ DoreenX.Petnames.append("Shadow")
            "Секрет." if Player.Name != "Секрет":
                $ DoreenX.Statup("Love", 80, 1)
                $ DoreenX.Statup("Obed", 60, 4)
                if not Player.Male:
                    ch_d "Как скажешь, мисс Секрет."
                else:
                    ch_d "Как скажешь, мистер Секрет."
                $ DoreenX.Petnames.append("Secret")
        return

# End Doreen player name / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Doreen_Key:
        call Shift_Focus(DoreenX)
        $ DoreenX.Loc = bg_current
        call Set_The_Scene
        $ DoreenX.FaceChange("bemused")
        $ Event_Queue = [0,0]
        ch_d "О, я тут подумала, раз уж ты постоянно заглядываешь ко мне. . ."
        ch_d "-у тебя должно быть это. . ."
        "Она вручает вам ключ с маленьким брелоком в виде желудя."
        $ Keys.append(DoreenX) if DoreenX not in Keys else Keys
        $ DoreenX.Event[0] = 1
        ch_p "Спасибо."
        return


label Doreen_BF(BO=[]):
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(DoreenX,"bemused","покраснела. . .")
                return
        call Shift_Focus(DoreenX)
        if DoreenX.Loc != bg_current:
            $ DoreenX.Loc = bg_current
            if DoreenX not in Party:
                "[DoreenX.Name] подходит к вам и изъявляет желание поговорить с вами наедине."
            else:
                "[DoreenX.Name] поворачивается к вам и показывает жестом, что хочет поговорить с вами наедине."
        $ Event_Queue = [0,0]
        $ DoreenX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene(0)
        call Display_Girl(DoreenX)
        $ DoreenX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in DoreenX.History:
                call expression DoreenX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        call CleartheRoom(DoreenX)
        $ DoreenX.FaceChange("normal",1)
        if "asked boyfriend" not in DoreenX.DailyActions:
                ch_d "Слушай, [DoreenX.Petname], у тебя есть минутка?"
        if DoreenX.Event[5]:
                $ DoreenX.FaceChange("sadside",1)
                if not Player.Male:
                    ch_d "В прошлый раз ты была очень груба со мной. . ."
                else:
                    ch_d "В прошлый раз ты был очень груб со мной. . ."
                ch_d "Но, думаю, я простила тебя. . ."
                ch_d "Частично. . ."
                ch_d "Знаешь, я тут продумала, может ты хочешь встречаться со мной или типа того. . ?"
                jump Doreen_BF_Redux
        $ DoreenX.Event[5] += 1
        $ DoreenX.FaceChange("smile",1)
        if not Player.Male:
            ch_d "Я просто хочу поблагодарить тебя за то, что ты помогла мне попасть сюда."
        else:
            ch_d "Я просто хочу поблагодарить тебя за то, что ты помог мне попасть сюда."
        if DoreenX.Event[4] > 2:
                $ DoreenX.FaceChange("bemused",1,Eyes="side")
                ch_d "Думаю, у тебя могли быть свои причины помочь мне, но. . ."
        ch_d "Я не знаю, куда бы я пошла, если бы не поступила."
        ch_d "Там, где я раньше обучалась, у ​​меня были серьезные проблемы."
        menu:
            extend ""
            "Потому что ты мутант?":
                    ch_d "Думаю, да."
                    ch_d "Я так и не смогла адаптироваться. . ."
            "Это из-за хвоста?":
                    ch_d "Ага, он мне точно не помогал. . ."
            "Потому что ты жирная?":
                    $ DoreenX.FaceChange("angry",2,Mouth="shocked")
                    $ DoreenX.Statup("Love", 200, -50)
                    $ DoreenX.Statup("Obed", 200, 20)
                    $ DoreenX.Statup("Inbt", 80, -10)
                    if not Player.Male:
                        ch_d "Что?! Я думала, мы подруги!"
                    else:
                        ch_d "Что?! Я думала, мы друзья!"
                    return #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
            "Потому что ты ботан?":
                    $ DoreenX.Statup("Love", 90, -5)
                    $ DoreenX.FaceChange("angry",1)
                    ch_d "Что? Нет!"
                    $ DoreenX.Statup("Inbt", 80, 5)
                    ch_d "STEM - это круто! [[STEM - Science, Technology, Engineering, Mathematics\естественные науки, технология, инженерия и математика]"
                    $ DoreenX.FaceChange("sly",1)
                    ch_d "По этой программе можно даже научиться программировать такие игры, как *неразборчиво*!"
                    ch_d "В общем. . ."
            ". . .":
                    pass
        ch_d "С огромным пушистым хвостом очень трудно вписаться в общество."
        menu:
            extend ""
            "Я думаю, он клевый.":
                    $ DoreenX.Statup("Love", 90, 5)
                    $ DoreenX.Statup("Inbt", 80, 5)
                    $ DoreenX.FaceChange("surprised",2)
                    ch_d "Правда?"
                    $ DoreenX.FaceChange("smile",1)
                    ch_d "Спасибо. . ."
            "Сочувствую.":
                    $ DoreenX.Statup("Love", 90, 6)
                    $ DoreenX.FaceChange("sadside",1,Mouth="smile")
                    ch_d "Спасибо. . ."
            "Понимаю, я тоже не люблю фурри.":
                    $ DoreenX.Statup("Love", 90, -4)
                    $ DoreenX.Statup("Obed", 200, 5)
                    $ DoreenX.FaceChange("angry",1)
                    ch_d "Ну. . . это было грубо."
            ". . .":
                    pass
        $ DoreenX.FaceChange("sadside",1,Mouth="smile")
        ch_d "В течение многих лет я мечтала избавиться от него. . ."
        if "tail" not in DoreenX.History:
                call Doreen_Tail
                if not DoreenX.Tail:
                    $ DoreenX.Statup("Love", 90, 1)
                    $ DoreenX.Statup("Obed", 200, 1)
                    $ DoreenX.FaceChange("smile",1)
                    ch_d "Ох, прямо гора с плечь."
                    ch_d "Тяжело постоянно таскать 3-4 кг меха."
        else:
                if not DoreenX.Tail:
                    ch_d "Но, думаю, мы уже это уладили. . ."
                else:
                    ch_d "Но, думаю, мы уже это обсуждали."
        ch_d "Хотя, наверное, дело было не только в хвосте."
        ch_d "Пожалуй, мне просто не подходило то место."
        ch_d "Даже если бы у меня не было хвоста, не думаю, что я могла бы вписаться."
        $ DoreenX.FaceChange("sad",1,Mouth="smile")
        ch_d "Но теперь я нашла свое место."
        ch_d "Спасибо. . ."
        menu:
            extend ""
            "Я очень рада за тебя." if not Player.Male:
                    $ DoreenX.Statup("Love", 90, 6)
                    $ DoreenX.FaceChange("smile",1)
            "Я очень рад за тебя." if Player.Male:
                    $ DoreenX.Statup("Love", 90, 6)
                    $ DoreenX.FaceChange("smile",1)
            "Конечно, без проблем.":
                    $ DoreenX.Statup("Love", 90, 3)
                    $ DoreenX.Statup("Inbt", 80, 2)
                    $ DoreenX.FaceChange("smile",1)
            "Ты странная, но ладно.":
                    $ DoreenX.Statup("Love", 90, -1)
                    $ DoreenX.Statup("Obed", 200, 3)
                    ch_d "-тц-"
            "Ладно.":
                    $ DoreenX.Statup("Love", 90, 2)
                    $ DoreenX.FaceChange("smile",1)
            ". . .":
                    pass

        if DoreenX in Player.Harem:
                #if she somehow already ended up in the harem
                if "DoreenYes" in Player.Traits:
                        $ Player.Traits.remove("DoreenYes")
                if "boyfriend" not in DoreenX.Petnames:
                        $ DoreenX.Petnames.append("boyfriend")
                return

        ch_d "Могу я. . . стать твоей девушкой или типа того?"
label Doreen_BF_Redux:
        $ Line = "start"
        call Shift_Focus(DoreenX)
        while Line != "yes":
            menu:
                extend ""
                "Конечно." if Line != "maybe":
                        $ DoreenX.FaceChange("smile",1)
                        $ DoreenX.Statup("Love", 200, 6)
                        $ DoreenX.Statup("Obed", 80, 2)
                        ch_d "Правда?!"
                        $ Line = "yes"
                "Ну ладно." if Line == "maybe":
                        $ DoreenX.FaceChange("normal",1)
                        $ DoreenX.Statup("Love", 200, 4)
                        $ DoreenX.Statup("Obed", 80, 2)
                        $ DoreenX.Statup("Inbt", 60, 1)
                        $ DoreenX.Statup("Inbt", 80, 2)
                        ch_d "Ох. . . хорошо."
                        $ Line = "yes"

                "Мне это не больно-то и интересно." if Line != "maybe":
                        $ DoreenX.FaceChange("sad",1)
                        $ DoreenX.Statup("Love", 200, -3)
                        $ DoreenX.Statup("Obed", 80, 3)
                        ch_d "Оу. . . даже немного?"
                        $ Line = "maybe"
                "Мне это -совсем- не интересно." if Line == "maybe":
                        $ DoreenX.FaceChange("sad",1)
                        $ DoreenX.Statup("Love", 200, -5)
                        $ DoreenX.Statup("Obed", 60, 1)
                        $ DoreenX.Statup("Obed", 80, 3)
                        ch_d "Ох. . ."
                        $ Line = "no"

                "Нет, я не думаю, что [Player.Harem[0].Name] поймет." if len(Player.Harem) == 1:
                        $ DoreenX.Statup("Love", 200, -15)
                        $ DoreenX.Statup("Obed", 80, 7)
                        $ DoreenX.FaceChange("sadside",1)
                        $ DoreenX.GLG(Player.Harem[0],800,-10,1)
                        ch_d "Ох. . . ага. . ."
                        $ Line = "no"
                "Не думаю, что другим это будет по душе." if len(Player.Harem) > 1:
                        $ DoreenX.Statup("Love", 200, -15)
                        $ DoreenX.Statup("Obed", 80, 7)
                        $ DoreenX.FaceChange("sad",1)
                        call HaremStatup(DoreenX,700,-10) #lowers like of all Harem girls by 10
                        ch_d "Оооох. . . ага. . ."
                        $ Line = "no"

            if Player.Harem and Line == "yes":
                #if you agreed, but have other girls. . .
                if not ApprovalCheck(DoreenX, 1400):
                    $ DoreenX.FaceChange("sadside",1)
                    ch_d "Но ты же, эм. . . с кем-то встречаешься, да? . ."
                    $ Line = "no"
                else:
                    if len(Player.Harem) >= 2:
                        ch_d "А другие девушки согласятся?"
                    else:
                        ch_d "А [Player.Harem[0].Name] согласится?"
                    menu:
                        extend ""
                        "Все хорошо, всех все устраивает." if "DoreenYes" in Player.Traits:
                                $ DoreenX.Statup("Love", 200, 5)
                                $ DoreenX.Statup("Obed", 80, 10)
                                $ DoreenX.Statup("Inbt", 80, 5)
                                $ DoreenX.FaceChange("surprised",1)
                                ch_d "Ох, здорово!"
                        "Нууу. . . это сперва еще нужно выяснить." if "DoreenYes" not in Player.Traits:
                                $ DoreenX.Statup("Love", 200, 3)
                                $ DoreenX.Statup("Obed", 80, 3)
                                $ DoreenX.Statup("Inbt", 80, 1)
                                $ DoreenX.Statup("Lust", 80, 1)
                                $ DoreenX.FaceChange("confused",1)
                                ch_d "Ох. . . тогда обсудим это позже? . ."
                                $ DoreenX.Event[5] = 20
                                call Remove_Girl(DoreenX)
                                $ Line = 0
                                return
                    call HaremStatup(DoreenX,900,20) #raises like of all Harem girls by 20

            if Line == "no":
                    $ DoreenX.FaceChange("sadside",1)
                    ch_d "Наверное. . . нам стоит оставить все как есть."
                    ch_d ". . . пока. . ."
                    "[DoreenX.Name] уходит в подавленном состоянии."
                    $ DoreenX.Event[5] = 20
                    call Remove_Girl(DoreenX)
                    $ Line = 0
                    return
            # end menu

        if "Historia" not in Player.Traits:
            $ Player.Harem.append(DoreenX)
            if "DoreenYes" in Player.Traits:
                    $ Player.Traits.remove("DoreenYes")
            $ DoreenX.Petnames.append("boyfriend")
            call Harem_Initiation
        $ DoreenX.Statup("Love", 200, 3)
        $ DoreenX.Statup("Obed", 80, 3)
        $ DoreenX.Statup("Inbt", 80, 1)
        $ DoreenX.Statup("Lust", 80, 1)
        $ DoreenX.FaceChange("sly",1)
        ch_d "Ну, раз уж мы поговорили и все такое. . ."
        if "Historia" in Player.Traits:
                return 1
        $ Tempmod = 10
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        $ Tempmod = 0
        return

label Doreen_Tail(Remove=0):
        ch_d "Ведь он не приносит никакой практической пользы."
        $ DoreenX.AddWord(1,"tail","tail",0,"tail") #adds tag to Recent/Daily
        menu:
            extend ""
            "Мне он нравится!":
                    $ DoreenX.Statup("Love", 80, 2)
                    $ DoreenX.Statup("Love", 200, 4)
                    $ DoreenX.FaceChange("smile",2)
                    ch_d "Правда?!"
                    $ DoreenX.Statup("Inbt", 80, 3)
                    $ DoreenX.FaceChange("smile",1,Eyes="side")
                    ch_d "Думаю, мне тоже. . ."
                    ch_d "Но я, наверное, все равно хочу узнать, есть ли возможность удалить его. . ."
            "Думаю, у доктора МакКоя есть для этого некое приспособление.":
                    $ DoreenX.Statup("Love", 90, 2)
                    $ DoreenX.Statup("Obed", 200, 2)
                    $ DoreenX.FaceChange("smile",1)
                    ch_d "Правда?"
                    $ DoreenX.Statup("Inbt", 80, 2)
                    ch_d "Наверное, тогда нам стоит его проверить. . ."
            "Это будет непросто. . .":
                    $ DoreenX.Statup("Love", 80, 2)
                    $ DoreenX.Statup("Love", 90, 1)
                    $ DoreenX.Statup("Obed", 70, 2)
                    ch_d "Возможно, у доктора МакКоя найдется какое-нибудь решение."
            ". . .":
                    ch_d "Возможно, у доктора МакКоя найдется какое-нибудь решение."
        "Вы вдвоем направляетесь в лабораторию МакКоя."
        ch_mc "Чем я могу вам помочь?"
        $ DoreenX.FaceChange("sadside",1)
        ch_d "Я надеялась, что вы сможете мне помочь избавиться от моего хвоста."
        ch_mc "О пресвятые небеса!"
        ch_mc "Это довольно радикальное решение, тебе так не кажется?"
        ch_d "Наверное, но. . ."
        ch_d "Но просто он мне сильно не нравится. . ."
        ch_mc "Что ж, я понимаю желание изменить свою внешность, чтобы лучше вписаться в общество. . ."
        ch_mc "Хммм. . ."
        ch_mc "Вот что я тебе скажу: у меня тут есть устройство, которое способно аккуратно переместить его в межпространственный карман."
        ch_mc "Он полностью исчезнет, даже не отделяясь от твоего тела."
        $ DoreenX.FaceChange("smile",1,Brows="surprised")
        ch_d "Правда?"
        ch_d "А это не больно? Можно будет вернуть все назад?"
        ch_mc "Ты не должна ничего почувствовать, и если хочешь, чтобы он вернулся, просто скажи мне."
        ch_d "Вау! Это слишком хорошо, чтобы быть правдой!"
        ch_mc "-Слишком,- ага."
        ch_mc "Итак, одно твое слово, и он испарится."
        menu:
            extend ""
            "Ты должна оставить хвост.":
                    $ DoreenX.Statup("Love", 80, 3)
                    $ DoreenX.Statup("Love", 200, 7)
                    $ DoreenX.FaceChange("smile",2,Brows="surprised")
                    ch_d "Правда? Хорошо, если тебе он нравится, я оставлю его."
                    $ DoreenX.Statup("Obed", 70, 4)
                    $ DoreenX.FaceChange("smile",1)
                    ch_mc "Вас понял. . ."
                    $ DoreenX.Statup("Obed", 200, 3)
                    ch_mc "Дайте мне знать, если передумаете. . ."
                    return
            "Ты должна избавиться от него":
                    $ DoreenX.Statup("Love", 90, 2)
                    $ DoreenX.Statup("Obed", 80, 3)
                    $ DoreenX.Statup("Obed", 200, 5)
                    $ DoreenX.FaceChange("sadside",1,Mouth="smile")
                    ch_d "Ты так думаешь? . ."
                    $ DoreenX.Statup("Inbt", 70, 2)
                    $ DoreenX.Statup("Inbt", 80, 2)
                    $ DoreenX.FaceChange("smile",1)
                    ch_d "Ага, пора попрощаться со старым другом."
            "Выбор за тобой.":
                    $ DoreenX.Statup("Love", 90, 4)
                    $ DoreenX.Statup("Obed", 80, 3)
                    $ DoreenX.FaceChange("sadside",1,Mouth="smile")
                    ch_d "Ох, ладно. . ."
                    $ DoreenX.Statup("Inbt", 80, 2)
                    $ DoreenX.Statup("Inbt", 200, 5)
                    $ DoreenX.FaceChange("smile",1)
                    if ApprovalCheck(DoreenX, 400, "I"):
                            ch_d "Наверное. . . я лучше оставлю его. . ."
                            ch_mc "Понял. . ."
                            ch_mc "Дай мне знать, если передумаешь. . ."
                            return
                    else:
                            ch_d "Наверное. . . я хочу избавиться от него. . ."
            ". . .":
                    $ DoreenX.Statup("Love", 90, -3)
                    $ DoreenX.FaceChange("sad",1,Mouth="smile")
                    ch_d "Ничего не посоветуешь? . ."
                    $ DoreenX.Statup("Inbt", 80, 4)
                    $ DoreenX.Statup("Inbt", 200, 7)
                    $ DoreenX.FaceChange("sadside",1,Mouth="smile")
                    ch_d "Ладно. . ."
                    $ DoreenX.FaceChange("smile",1)
                    if ApprovalCheck(DoreenX, 400, "I"):
                            ch_d "Наверное. . . я лучше оставлю его. . ."
                            ch_mc "Понял. . ."
                            ch_mc "Дай мне знать, если передумаешь. . ."
                            return
                    else:
                            ch_d "Наверное. . . я хочу избавиться от него. . ."
        ch_mc "Что ж, хорошо. . . за дело. . ."
        show blackscreen onlayer black
        "После нескольких минут калибровки МакКой активирует устройство."
        $ DoreenX.Tail = 0
        "Устройство тихонько гудит, затем следует вспышка, и хвост [DoreenX.Name_rod] исчезает."
        hide blackscreen onlayer black
        return



## start Doreen_Love//////////////////////////////////////////////////////////
label Doreen_Love(Shipping=[],Shipshape=0,Topics=[],BO=[]):
        # SHipping is used to track who else you're involved with
        # if DoreenX.Event[6] = 5, then it cleared
        # if DoreenX.Event[6] = 20, then it broke because you didn't love her
        # if DoreenX.Event[6] = 25, then it broke and you already went through the redux

        $ DoreenX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ BO = TotalGirls[:]
        $ BO.remove(DoreenX)
        while BO:
            if ApprovalCheck(BO[0], 1200, "LO"):
                    $ Shipping.append(BO[0])
            $ BO.remove(BO[0])
        $ Shipshape = len(Shipping)

        $ DoreenX.FaceChange("sad",1,Mouth="normal")
        if DoreenX.Loc == bg_current or DoreenX in Party:
                "[DoreenX.Name] бросает на вас обеспокоенный взгляд."
        else:
                "[DoreenX.Name] выходит из-за угла и замечает вас."
        if bg_current != "bg doreen" and bg_current != "bg player":
                "Она просит вас проследовать за ней в ее комнату и, похоже, ответ \"нет\" не принимается."
                $ bg_current = "bg doreen"
        $ Event_Queue = [0,0]
        $ DoreenX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(DoreenX)
        call Set_The_Scene
        call Taboo_Level
        call Shift_Focus(DoreenX)
        $ DoreenX.DailyActions.append("relationship")
        $ DoreenX.FaceChange("sad",1,Mouth="normal")
        ch_d "Я, эм. . ."
        ch_d "У белок, знаешь, все гораздо проще."
        menu:
            extend ""
            "Да?":
                    ch_d "Да!"
            "Я не хочу знать, о чем ты говоришь.":
                    $ DoreenX.Statup("Love", 90, -1)
                    $ DoreenX.Statup("Obed", 200, 2)
                    ch_d "Выслушай меня!"
            "Что?":
                    pass
            "О, я знаю, к чему все идет." if "sexfriend" in DoreenX.Petnames:
                    $ DoreenX.Statup("Love", 90, 1)
                    $ DoreenX.Statup("Obed", 80, 2)
                    ch_d "На этот раз все иначе!"
            ". . .":
                    pass

        if "sexfriend" not in DoreenX.Petnames:
                ch_d "Я про. . . отношения."
                ch_d "Честно говоря, им вообще такое не интересно. . ."
                ch_d "Они просто. . ."
                ch_d "Как бы. . ."
                ch_d "Переходят сразу. . . к делу."
                menu:
                    extend ""
                    "Ты этого хочешь?":
                            ch_d "Нет!"
                            $ DoreenX.Statup("Inbt", 80, 2)
                    "Конечно.":
                            pass
                    "И чем они отличаются от нас?":
                            $ DoreenX.Statup("Love", 90, 1)
                            $ DoreenX.Statup("Inbt", 80, 2)
                    ". . .":
                            pass
        ch_d "Я хотела сказать, что мы разные!"
        ch_d "Я другая. . ."
        ch_d "Я всегда хотела чего-то большего. . ."
        ch_d "-постоянного партнера. . ."
        if not Player.Male:
            ch_d "И я думаю, что нашла ее."
        else:
            ch_d "И я думаю, что нашла его."

        if len(Player.Harem) > 1:
                $ DoreenX.Statup("Inbt", 80, 2)
                if not Player.Male:
                    ch_d "Даже если мне придется делить ее с другими. . ."
                else:
                    ch_d "Даже если мне придется делить его с другими. . ."
        menu:
            extend ""
            "Да?":
                    ch_d "Да. . ."
            "Кого ты нашла?":
                    $ DoreenX.Statup("Love", 90, -1)
                    $ DoreenX.Statup("Obed", 200, 2)
                    $ DoreenX.Statup("Inbt", 80, 2)
                    if not Player.Male:
                        ch_d "Тебя, дурочка!"
                    else:
                        ch_d "Тебя, дурачок!"
            ". . .":
                    ch_d "Так вот. . ."
        $ DoreenX.FaceChange("sad",2)
        ch_d "Я. . ."
        $ DoreenX.FaceChange("sad",2,Mouth="normal")
        ch_d "-люблю тебя."
        menu:
            extend ""
            "Я тоже тебя люблю!":
                $ DoreenX.FaceChange("smile",1)
                $ DoreenX.Statup("Love", 200, 20)
                $ DoreenX.Statup("Inbt", 90, 5)
                ch_d "Правда?!"
                ch_d "Замечательно!"
                $ DoreenX.Petnames.append("lover")
                jump Doreen_Love_End
            "Я знаю.":
                $ DoreenX.FaceChange("confused",1)
                $ DoreenX.Statup("Love", 200, -5)
                $ DoreenX.Statup("Obed", 90, 5)
                $ DoreenX.Statup("Inbt", 90, 5)
                ch_d "А?"
                $ DoreenX.Statup("Love", 200, 20)
                $ DoreenX.FaceChange("smile",1)
                ch_d "О!"
                $ DoreenX.Statup("Inbt", 90, 5)
                $ DoreenX.FaceChange("normal",2,Mouth="smirk")
                ch_d "\"Я знаю\", что ты тоже меня любишь!"
                $ DoreenX.FaceChange("normal",1,Mouth="smirk")
                $ DoreenX.Petnames.append("lover")
                jump Doreen_Love_End
            "Это здорово?":
                $ DoreenX.FaceChange("confused",1,Mouth="smile")
                $ DoreenX.Statup("Obed", 90, 5)
                ch_d "Ага. . . здорово. . ."
            "Хм.":
                $ DoreenX.FaceChange("confused",1)
                $ DoreenX.Statup("Love", 200, -5)
                $ DoreenX.Statup("Obed", 90, 10)
                ch_d "Ты. . . не чувствуешь того же?"
        menu:
            extend ""
            "Ох, я тоже тебя люблю!":
                $ DoreenX.FaceChange("smile",1)
                $ DoreenX.Statup("Love", 200, 15)
                $ DoreenX.Statup("Obed", 90, 5)
                ch_d "Ох. . . "
                $ DoreenX.FaceChange("sly",1)
                $ DoreenX.Statup("Inbt", 90, 5)
                ch_d "Здорово!"
                $ DoreenX.Petnames.append("lover")
                jump Doreen_Love_End
            "Я. . . тоже тебя люблю?":
                $ DoreenX.FaceChange("confused",1)
                $ DoreenX.Statup("Love", 200, 5)
                $ DoreenX.Statup("Obed", 90, 5)
                ch_d "Ну. . . лучше поздно, чем никогда, [DoreenX.Petname]."
                $ DoreenX.FaceChange("bemused",1)
                $ DoreenX.Petnames.append("lover")
                jump Doreen_Love_End
            "Ну, это все, конечно, круто и все такое. . .":
                $ DoreenX.FaceChange("sad",1)
                $ DoreenX.Statup("Love", 200, -5)
                $ DoreenX.Statup("Obed", 90, 10)
                $ DoreenX.Statup("Inbt", 90, -5)
                ch_d ". . . но. . . ты не можешь ответить мне взаимностью. . ."
            "Теперь я чувствую себя. . . неуютно.":
                $ DoreenX.FaceChange("confused",1)
                $ DoreenX.Statup("Love", 200, -10)
                $ DoreenX.Statup("Obed", 90, 15)
                $ DoreenX.Statup("Inbt", 90, -5)
                ch_d "Ох. . ."
                $ DoreenX.FaceChange("sad",1)

        ch_d "Можешь сказать мне почему?"
        ch_d "Это из-за другой?"
        $ Line = 0
        menu:
                extend ""
                "Да, из-за другой." if Shipping and Shipshape < 3:
                    menu: #rkeljsvgb
                        "Из-за [RogueX.Name_rod]." if RogueX in Shipping:
                                $ Line = RogueX
                        "Из-за [KittyX.Name_rod]." if KittyX in Shipping:
                                $ Line = KittyX
                        "Из-за [EmmaX.Name_rod]." if EmmaX in Shipping:
                                $ Line = EmmaX
                        "Из-за [LauraX.Name_rod]." if LauraX in Shipping:
                                $ Line = LauraX
                        "Из-за [JeanX.Name_rod]." if JeanX in Shipping:
                                $ Line = JeanX
                        "Из-за [StormX.Name_rod]." if StormX in Shipping:
                                $ Line = StormX
                        "Из-за [JubesX.Name_rod]." if JubesX in Shipping:
                                $ Line = JubesX
                        "Из-за [GwenX.Name_rod]." if GwenX in Shipping:
                                $ Line = GwenX
                        "Из-за [BetsyX.Name_rod]." if BetsyX in Shipping:
                                $ Line = BetsyX
                        "Из-за [WandaX.Name_rod]." if WandaX in Shipping:
                                $ Line = WandaX
                        "Мне бы не хотелось произносить ее имя.":
                                $ DoreenX.Statup("Obed", 90, 15)
                                $ DoreenX.Statup("Inbt", 90, 5)
                                $ DoreenX.FaceChange("sadside",1)
                                ch_d "Думаю, это справедливо. . ."
                    if Line:
                        #If you called out a girl,
                        if DoreenX.GirlLikeCheck(Line) >= 800:
                            $ DoreenX.Statup("Love", 200, 5)
                            $ DoreenX.Statup("Obed", 90, 20)
                            $ DoreenX.Statup("Inbt", 90, 5)
                            $ DoreenX.FaceChange("sadside",1)
                            ch_d "Она. . . очень милая. . ."
                        else:
                            $ DoreenX.FaceChange("angry",Eyes="side")
                            $ DoreenX.Statup("Love", 200, -5)
                            $ DoreenX.Statup("Obed", 90, 20)
                            ch_d "Да, я понимаю. . ."
                            $ DoreenX.FaceChange("sadside",1)
                            $ DoreenX.GLG(Line,800,-50,1)

                "Да, из-за других" if Shipshape > 1:
                        $ DoreenX.Statup("Obed", 90, 15)
                        $ DoreenX.Statup("Inbt", 90, 5)
                        $ DoreenX.FaceChange("surprised",2)
                        ch_d "Ох. . . ."
                        $ DoreenX.FaceChange("sadside",1)
                        ch_d "-конечно. . ."
                "У меня никого нет.":
                        $ DoreenX.Statup("Love", 200, -15)
                        $ DoreenX.Statup("Obed", 90, 15)
                        $ DoreenX.Statup("Inbt", 90, 5)
                        $ DoreenX.FaceChange("sad",1)
                        ch_d "Ох. . . ну ладно. . ."
                "Дело в \"тебе\".":
                        $ DoreenX.FaceChange("sadside")
                        $ DoreenX.Statup("Love", 200, -25)
                        $ DoreenX.Statup("Obed", 90, 15)
                        ch_d "Ох. . . ."
                        $ DoreenX.Statup("Love", 200, -10)
        $ DoreenX.FaceChange("sad",1)
        ch_d "Наверное, я понимаю. . ."
        if "sexfriend" in DoreenX.Petnames:
                $ DoreenX.FaceChange("sly",1)
                ch_d "Мы все еще можем. . . \"спариваться\". . ."
        elif "sir" in DoreenX.Petnames:
                $ DoreenX.FaceChange("sad",1,Mouth="normal")
                ch_d "Но ты можешь продолжать. . . просить меня о разном. . ."
        else:
                $ DoreenX.FaceChange("sad",1)
                if not Player.Male:
                    ch_d "Но я думаю, мы все еще можем быть подругами. . ."
                else:
                    ch_d "Но я думаю, мы все еще можем быть друзьями. . ."
                $ DoreenX.FaceChange("sadside",1,Mouth="smirk")
                ch_d "-или типа того. . ."
        menu:
            extend ""
            "Ага. . .":
                    $ DoreenX.FaceChange("sad",1)
                    ch_d "Ну ладно. . ."
            ". . .":
                    $ DoreenX.FaceChange("sad",1)
            "Может, когда-нибудь все и изменится":
                    ch_d "Ну ладно. . ."
                    $ DoreenX.FaceChange("sad",1)
            "Я тоже люблю тебя!":
                    $ DoreenX.FaceChange("sad",1)
                    "Она уже уходила и не слышала вас."
        hide Doreen_Sprite with easeoutright
        call Remove_Girl(DoreenX)
        $ DoreenX.Loc = "hold" #puts her off the board for the day
        "Она уходит."
        $ DoreenX.Event[6] = 20
        $ Line = 0
        jump Misplaced
        return

label Doreen_Love_End:
        $ DoreenX.Event[6] = 5
        "[DoreenX.Name] заключает вас в крепкие объятия."
        $ DoreenX.Statup("Love", 200, 25)
        $ DoreenX.Statup("Lust", 90, 5)
        $ DoreenX.FaceChange("sly",1)
        ch_d "Ну ладно, с этим мы разобрались. . ."
        $ DoreenX.Statup("Lust", 90, 10)

        if not DoreenX.Sex:
                $ DoreenX.FaceChange("bemused",2)
                ch_d "Ты хочешь. . ."
        ch_d "\"Спариться\" со мной?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Конечно же хочу. . . [[секс]":   #fix, unlock once sex becomes an option
                    $ DoreenX.Statup("Inbt", 30, 20)
                    $ DoreenX.Statup("Obed", 70, 10)
                    ch_d "Хмм. . ."
                    if Player.Male:
                            call SexAct("sex") # call Doreen_SexAct("sex")
                    else:
                            call SexAct("blow") # call Doreen_SexAct("blow")
                "У меня есть другая идея. . .[[выбрать другое занятие]":
                    $ DoreenX.Brows = "confused"
                    $ DoreenX.Statup("Obed", 70, 25)
                    ch_d "Например? . ."
                    $ Tempmod = 20
                    call SexMenu
        jump Misplaced

label Doreen_Love_Redux:
         #this is for if you rejected her but want a second chance
        $ Line = 0
        call Shift_Focus(DoreenX)
        $ DoreenX.DailyActions.append("relationship")

        if DoreenX.Event[6] >= 25:
                #if this is the second time through
                ch_p "Надеюсь, ты меня простила, я все еще люблю тебя."
                $ DoreenX.Statup("Love", 95, 10)
                if "syke" in DoreenX.History:
                    $ DoreenX.Statup("Love", 200, -5)
                if ApprovalCheck(DoreenX, 950, "L"):
                    $ Line = "love"
                else:
                    $ DoreenX.FaceChange("sad",1)
                    ch_d "Я. . . я просто не могу. Пока не могу, [DoreenX.Petname]."
                    $ DoreenX.FaceChange("sadside",Mouth="lipbite")
                    ch_d ". . ."
                    ch_d "Но я. . . я тебя выслушаю. . ."
        else:
                    if not Player.Male:
                        ch_p "Помнишь, я сказала тебе, что не люблю тебя?"
                    else:
                        ch_p "Помнишь, я сказал тебе, что не люблю тебя?"
                    $ DoreenX.FaceChange("perplexed",1)
                    ch_d ". . ."
                    $ DoreenX.FaceChange("sadside",1)
                    ch_d "Я. . . помню. . ."

        if Line != "love":
                menu:
                    extend ""
                    "Прости, я не хотела." if not Player.Male:
                        $ DoreenX.FaceChange("confused",1)
                        ch_d ". . ."
                        ch_d "Ох. . ."
                        ch_p "Ага. То есть, да, я люблю тебя, [BetsyX.Name]."
                        $ DoreenX.Statup("Love", 200, 10)
                        if ApprovalCheck(DoreenX, 950, "L"):
                            $ Line = "love"
                            $ DoreenX.FaceChange("surprised",1,Mouth="normal")
                        else:
                            $ DoreenX.FaceChange("sadside")
                            ch_d "Ну. . . мне кажется, я тебя разлюбила. . ."
                    "Прости, я не хотел." if Player.Male:
                        $ DoreenX.FaceChange("confused",1)
                        ch_d ". . ."
                        ch_d "Ох. . ."
                        ch_p "Ага. То есть, да, я люблю тебя, [BetsyX.Name]."
                        $ DoreenX.Statup("Love", 200, 10)
                        if ApprovalCheck(DoreenX, 950, "L"):
                            $ Line = "love"
                            $ DoreenX.FaceChange("surprised",1,Mouth="normal")
                        else:
                            $ DoreenX.FaceChange("sadside")
                            ch_d "Ну. . . мне кажется, я тебя разлюбила. . ."
                    "Я передумала, я люблю тебя, так что. . ." if not Player.Male:
                        if ApprovalCheck(DoreenX, 950, "L"):
                            $ Line = "love"
                            $ DoreenX.FaceChange("surprised",1,Mouth="normal")
                            ch_d "Ох?"
                        else:
                            $ DoreenX.Mouth = "sad"
                            ch_d "Хм. . ."
                            $ DoreenX.Statup("Inbt", 90, 10)
                            $ DoreenX.FaceChange("sadside")
                            ch_d ". . . я не думаю, что еще люблю тебя. . ."
                    "Я передумал, я люблю тебя, так что. . ." if Player.Male:
                        if ApprovalCheck(DoreenX, 950, "L"):
                            $ Line = "love"
                            $ DoreenX.FaceChange("surprised",1,Mouth="normal")
                            ch_d "Ох?"
                        else:
                            $ DoreenX.Mouth = "sad"
                            ch_d "Хм. . ."
                            $ DoreenX.Statup("Inbt", 90, 10)
                            $ DoreenX.FaceChange("sadside")
                            ch_d ". . . я не думаю, что еще люблю тебя. . ."
                    "Эм, неважно.":
                            $ DoreenX.Statup("Love", 200, -30)
                            $ DoreenX.Statup("Obed", 50, 10)
                            $ DoreenX.FaceChange("angry")
                            ch_d "Ну тогда пожуй орехов!"
                            $ DoreenX.RecentActions.append("angry")
                            $ DoreenX.DailyActions.append("angry")
        if Line == "love":
                $ DoreenX.Statup("Love", 200, 40)
                $ DoreenX.Statup("Obed", 90, 10)
                $ DoreenX.Statup("Inbt", 90, 10)
                $ DoreenX.FaceChange("normal")
                if not Player.Male:
                    ch_d "Я. . . я рада, что ты все хорошо обдумала. . ."
                else:
                    ch_d "Я. . . я рада, что ты все хорошо обдумал. . ."
                ch_d "Я тоже тебя люблю, [DoreenX.Petname]!"
                $ DoreenX.Petnames.append("lover")
        $ DoreenX.Event[6] = 25
        jump Misplaced
        return

# end Doreen_Love//////////////////////////////////////////////////////////


# start Doreen_Sub//////////////////////////////////////////////////////////

label Doreen_Sub:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(DoreenX,"bemused","выглядит тихой. . .")
            return
    $ DoreenX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    call Shift_Focus(DoreenX)
    if DoreenX.Loc != bg_current and DoreenX not in Party:
        "Вдруг [DoreenX.Name] внезапно появляется перед вами и изъявляет желание поговорить."

    $ Event_Queue = [0,0]
    $ DoreenX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(DoreenX)
    call CleartheRoom(DoreenX)
    call Set_The_Scene
    call Taboo_Level
    $ DoreenX.DailyActions.append("relationship")
    $ DoreenX.FaceChange("bemused", 1)
    if not Player.Male and "girltalk" not in DoreenX.History:
            call expression DoreenX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
            return
    if "SGattic" in Player.History:
            $ DoreenX.FaceChange("sly",1)
            if not Player.Male:
                ch_d "Ты хорошо заботилась обо мне. . ."
            else:
                ch_d "Ты хорошо заботился обо мне. . ."
    elif "SGattic" in DoreenX.History:
            $ DoreenX.FaceChange("smile",1)
            if not Player.Male:
                ch_d "Ты очень хорошо заботилась обо мне, когда я только прибыла сюда. . ."
            else:
                ch_d "Ты очень хорошо заботился обо мне, когда я только прибыла сюда. . ."
    else:
            ch_d "Наверное, я очень уважаю тебя. . ."

    if DoreenX.Event[4] > 2:
            $ DoreenX.FaceChange("bemused",1,Eyes="side")
            if not Player.Male:
                ch_d "Ты получила от меня то, что хотела, но это был взаимовыгодный обмен. . ."
            else:
                ch_d "Ты получил от меня то, что хотел, но это был взаимовыгодный обмен. . ."
    ch_d "Я долго думала. . ."
    ch_d "Белки не являются \"стайными\" животными или типа того. . ."
    $ DoreenX.FaceChange("angry",1,Eyes="side")
    ch_d "Но думаю, что с моими способностями я \"главная белка.\""
    ch_d "Это большая ответственность. . ."
    $ DoreenX.FaceChange("sexy",2,Brows="sad")
    ch_d "Слушай, не хочешь ли ты стать \"главной белкой\" вместо меня?"
    $ DoreenX.History.append("sir")
    menu:
        extend ""
        "Я буду и выше тебя в иерархии белок?":
                $ DoreenX.Statup("Obed", 200, 5)
                $ DoreenX.Statup("Inbt", 70, 2)
                $ DoreenX.FaceChange("sly",1)
        "Конечно.":
                $ DoreenX.Statup("Obed", 200, 3)
                $ DoreenX.FaceChange("sly",1)
        "Звучит отвратительно.":
                $ DoreenX.Statup("Love", 80, -5)
                $ DoreenX.Statup("Obed", 200, 5)
                $ DoreenX.Statup("Inbt", 70, -2)
                $ DoreenX.FaceChange("sad",2)
                ch_d "Оу, тебе не нужно думать об этом в таком ключе. . ."
                $ DoreenX.FaceChange("sly",1)
        "Что это значит?":
                $ DoreenX.Statup("Love", 80, -2)
                $ DoreenX.Statup("Inbt", 70, -1)
                $ DoreenX.FaceChange("sly",1)
                ch_d "Это значит, что ты будешь боссом. . ."
        ". . .":
                $ DoreenX.Statup("Obed", 200, 1)
                $ DoreenX.FaceChange("sly",1)
    ch_d "Ты определенно будешь \"и выше меня.\""
    menu:
        extend ""
        "Меня все устраивает.":
                $ DoreenX.Statup("Obed", 200, 10)
                $ DoreenX.Statup("Inbt", 70, 2)
                $ DoreenX.FaceChange("smile",1)
                ch_d "Вот и хорошо."
                $ DoreenX.FaceChange("sly",1)
                if not Player.Male:
                    ch_d ". . . госпожа."
                else:
                    ch_d ". . . господин."
        "Ох, ладно.":
                $ DoreenX.Statup("Inbt", 70, 3)
                if not Player.Male:
                    ch_d "Приму твои слова за согласие. . . госпожа."
                else:
                    ch_d "Приму твои слова за согласие. . . господин."
        "Все равно звучит отвратительно.":
                $ DoreenX.Statup("Love", 80, -5)
                $ DoreenX.Statup("Obed", 200, -10)
                $ DoreenX.Statup("Inbt", 70, -2)
                $ DoreenX.FaceChange("sadside",2)
                ch_d "Ох. . . ладно. . ."
                return  #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
        "Мне это не интересно.":
                $ DoreenX.Statup("Obed", 200, -5)
                $ DoreenX.Statup("Inbt", 70, -2)
                $ DoreenX.FaceChange("sadside",2)
                ch_d "Ох. . . отстой."
                return  #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
        ". . .":
                $ DoreenX.Statup("Obed", 200, 2)
                $ DoreenX.Statup("Inbt", 70, 3)
                if not Player.Male:
                    ch_d "Приму твое молчание за согласие. . . госпожа."
                else:
                    ch_d "Приму твое молчание за согласие. . . господин."
    $ DoreenX.Petnames.append("sir")
    menu:
        extend ""
        "Ага, [DoreenX.Pet].":
                $ DoreenX.Statup("Love", 80, 2)
                $ DoreenX.Statup("Obed", 200, 10)
                $ DoreenX.Statup("Inbt", 70, 2)
                $ DoreenX.NameCheck() #checks reaction to petname
                if not Player.Male:
                    $ DoreenX.Petname = "госпожа"
                    $ DoreenX.Petname_rod = "госпожи"
                    $ DoreenX.Petname_dat = "госпоже"
                    $ DoreenX.Petname_vin = "госпожу"
                    $ DoreenX.Petname_tvo = "госпожой"
                    $ DoreenX.Petname_pre = "госпоже"
                else:
                    $ DoreenX.Petname = "господин"
                    $ DoreenX.Petname_rod = "господина"
                    $ DoreenX.Petname_dat = "господину"
                    $ DoreenX.Petname_vin = "господина"
                    $ DoreenX.Petname_tvo = "господином"
                    $ DoreenX.Petname_pre = "господине"
        ". . .":
                $ DoreenX.Statup("Obed", 200, 7)
                if not Player.Male:
                    $ DoreenX.Petname = "госпожа"
                    $ DoreenX.Petname_rod = "госпожи"
                    $ DoreenX.Petname_dat = "госпоже"
                    $ DoreenX.Petname_vin = "госпожу"
                    $ DoreenX.Petname_tvo = "госпожой"
                    $ DoreenX.Petname_pre = "госпоже"
                else:
                    $ DoreenX.Petname = "господин"
                    $ DoreenX.Petname_rod = "господина"
                    $ DoreenX.Petname_dat = "господину"
                    $ DoreenX.Petname_vin = "господина"
                    $ DoreenX.Petname_tvo = "господином"
                    $ DoreenX.Petname_pre = "господине"
        "Только не надо звать меня \"госпожа\"." if not Player.Male:
                $ DoreenX.Statup("Obed", 200, 10)
                $ DoreenX.Statup("Inbt", 70, -1)
                $ DoreenX.FaceChange("sadside",2)
                ch_d "Ох, ладно, [DoreenX.Petname]."
                $ DoreenX.FaceChange("sly",1)
        "Только не надо звать меня \"господин\"." if Player.Male:
                $ DoreenX.Statup("Obed", 200, 10)
                $ DoreenX.Statup("Inbt", 70, -1)
                $ DoreenX.FaceChange("sadside",2)
                ch_d "Ох, ладно, [DoreenX.Petname]."
                $ DoreenX.FaceChange("sly",1)
    ch_d "Итак. . . я могу что-нибудь для тебя сделать? . ."
    $ DoreenX.FaceChange("sly",2)
    ch_d "Я готова на -все- . ."
    $ DoreenX.FaceChange("sly",1)
    return

label Doreen_Sub_Asked:
    $ Line = 0
    call Shift_Focus(DoreenX)
    $ DoreenX.FaceChange("sadside", 1)
    if not Player.Male:
        ch_d "Ты. . . кажется, не хотела этого."
    else:
        ch_d "Ты. . . кажется, не хотел этого."
    menu:
        extend ""
        "Ну, я хочу извиниться. У меня еще есть возможность передумать?":
                if "sir" in DoreenX.Petnames and ApprovalCheck(DoreenX, 850, "O"):
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck(DoreenX, 550, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        pass
                else: #if it failed both those things,
                        $ DoreenX.FaceChange("angry", 1)
                        ch_d "Я. . . не думаю, что сейчас в этом имеет смысл." #Failed again. :(
                        $ Line = "rude"

                if Line != "rude":
                        $ DoreenX.Statup("Love", 90, 10)
                        $ DoreenX.FaceChange("sly", 1)
                        ch_d "Ну. . . мы можем попробовать еще раз. . ."

        "Я знаю, что ты этого хочешь. Хочешь попробовать еще раз или нет?":
                $ DoreenX.FaceChange("bemused", 1)
                if "sir" in DoreenX.Petnames:
                    if ApprovalCheck(DoreenX, 850, "O"):
                        if not Player.Male:
                            ch_d "Да, госпожа. . ."
                        else:
                            ch_d "Да, господин. . ."
                    else:
                        ch_d ". . . не сейчас."
                        $ Line = "rude"
                elif ApprovalCheck(DoreenX, 600, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        $ DoreenX.FaceChange("confused", 1)
                        ch_d "Ну. . ."
                        $ DoreenX.FaceChange("sly", 1)
                        ch_d ". . . может быть."
                        if not Player.Male:
                            ch_d "Ты уверена, что этого хочешь?"
                        else:
                            ch_d "Ты уверен, что этого хочешь?"
                        menu:
                            extend ""
                            "Да, извини, что я была двольно груба." if not Player.Male:
                                            $ DoreenX.Statup("Love", 90, 15)
                                            $ DoreenX.Statup("Inbt", 50, 10)
                                            $ DoreenX.FaceChange("bemused", 1)
                                            $ DoreenX.Eyes = "side"
                                            ch_d "Ну ладно."
                            "Да, извини, что я был двольно груб." if Player.Male:
                                            $ DoreenX.Statup("Love", 90, 15)
                                            $ DoreenX.Statup("Inbt", 50, 10)
                                            $ DoreenX.FaceChange("bemused", 1)
                                            $ DoreenX.Eyes = "side"
                                            ch_d "Ну ладно."
                            "Ты охуеть как права, сучка.":
                                    if "sir" in DoreenX.Petnames and ApprovalCheck(DoreenX, 900, "O"):
                                            $ DoreenX.Statup("Love", 200, -5)
                                            $ DoreenX.Statup("Obed", 200, 10)
                                            ch_d ". . ."
                                    elif ApprovalCheck(DoreenX,700, "O"):
                                            $ DoreenX.Statup("Love", 200, -5)
                                            $ DoreenX.Statup("Obed", 200, 10)
                                            ch_d ". . . Что?"
                                    else: #if it failed both those things,
                                            $ DoreenX.Statup("Love", 200, -10)
                                            $ DoreenX.Statup("Obed", 90, -10)
                                            $ DoreenX.Statup("Obed", 200, -10)
                                            $ DoreenX.Statup("Inbt", 50, -15)
                                            $ DoreenX.FaceChange("angry", 1)
                                            if not Player.Male:
                                                ch_d "Ты слишком груба!"
                                            else:
                                                ch_d "Ты слишком груб!"
                                            $ Line = "rude"
                            "Ладно, тогда не бери в голову.":
                                            $ DoreenX.FaceChange("angry", 1)
                                            $ DoreenX.Statup("Love", 200, -10)
                                            $ DoreenX.Statup("Obed", 90, -10)
                                            $ DoreenX.Statup("Obed", 200, -10)
                                            $ DoreenX.Statup("Inbt", 50, -15)
                                            ch_d ". . ."
                                            ch_d "Мне не нравятся такие игры."
                                            $ Line = "rude"

    $ DoreenX.RecentActions.append("asked sub")
    $ DoreenX.DailyActions.append("asked sub")
    if Line == "rude":
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Doreen_Sprite with easeoutright
            call Remove_Girl(DoreenX)
            $ DoreenX.RecentActions.append("angry")
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[DoreenX.Name] выбегает из комнаты."
    elif "sir" in DoreenX.Petnames:
            #it didn't fail and "sir" was covered
            $ DoreenX.Statup("Obed", 200, 50)
            $ DoreenX.Petnames.append("master")
            if not Player.Male:
                $ DoreenX.Petname = "хозяйка"
                $ DoreenX.Petname_rod = "хозяйки"
                $ DoreenX.Petname_dat = "хозяйке"
                $ DoreenX.Petname_vin = "хозяйку"
                $ DoreenX.Petname_tvo = "хозяйкой"
                $ DoreenX.Petname_pre = "хозяйке"
            else:
                $ DoreenX.Petname = "хозяин"
                $ DoreenX.Petname_rod = "хозяина"
                $ DoreenX.Petname_dat = "хозяину"
                $ DoreenX.Petname_vin = "хозяина"
                $ DoreenX.Petname_tvo = "хозяином"
                $ DoreenX.Petname_pre = "хозяине"
            $ DoreenX.Eyes = "sly"
            if not Player.Male:
                ch_d ". . . хозяйка. . ."
            else:
                ch_d ". . . хозяин. . ."
    else:
            #it didn't fail
            $ DoreenX.Statup("Obed", 200, 30)
            $ DoreenX.Petnames.append("sir")
            if not Player.Male:
                $ DoreenX.Petname = "госпожа"
                $ DoreenX.Petname_rod = "госпожи"
                $ DoreenX.Petname_dat = "госпоже"
                $ DoreenX.Petname_vin = "госпожу"
                $ DoreenX.Petname_tvo = "госпожой"
                $ DoreenX.Petname_pre = "госпоже"
            else:
                $ DoreenX.Petname = "господин"
                $ DoreenX.Petname_rod = "господина"
                $ DoreenX.Petname_dat = "господину"
                $ DoreenX.Petname_vin = "господина"
                $ DoreenX.Petname_tvo = "господином"
                $ DoreenX.Petname_pre = "господине"
            $ DoreenX.FaceChange("sly", 1)
            if not Player.Male:
                ch_d ". . . госпожа."
            else:
                ch_d ". . . господин."
    return

# end Doreen_Sub//////////////////////////////////////////////////////////


# start Doreen_Master//////////////////////////////////////////////////////////

label Doreen_Master:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(DoreenX,"bemused","выглядит необычайно покорной. . .")
            return
    $ DoreenX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    call Shift_Focus(DoreenX)
    if DoreenX.Loc != bg_current and DoreenX not in Party:
        "Вдруг [DoreenX.Name] появляется словно из ниоткуда и изъявляет желание поговорить."

    $ Event_Queue = [0,0]
    $ DoreenX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(DoreenX)
    call CleartheRoom(DoreenX)
    $ DoreenX.ArmPose = 2
    call Set_The_Scene
    $ DoreenX.DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ DoreenX.FaceChange("sly", 1)
    ch_d "Так вот. . . [DoreenX.Petname]. . ."
    if not Player.Male:
        ch_d "Ты была для меня замечательным боссом-белкой. . ."
    else:
        ch_d "Ты был для меня замечательным боссом-белкой. . ."
    menu:
        extend ""
        ". . .":
                pass
        "Так мы теперь это называем?":
                $ DoreenX.FaceChange("bemused",2,Eyes="side")
                $ DoreenX.Statup("Obed", 200, 1)
                $ DoreenX.Statup("Inbt", 80, 1)
                ch_d "Это белки придумали!"
        "Перестань называть меня так.":
                $ DoreenX.FaceChange("sadside",2)
                $ DoreenX.Statup("Obed", 200, 2)
                ch_d "Ох, ладно. . ."
        ". . . [[выразительно помолчать]":
                $ DoreenX.Statup("Obed", 200, 3)
                ch_d "Эм. . ."
    ch_d "В общем. . ."
    $ DoreenX.FaceChange("sly",1)
    ch_d "Это было очень весело, но мне хочется посмотреть, как далеко мы можем зайти. . ."
    if not Player.Male:
        ch_d "Не могла бы ты стать моей хозяйкой?"
    else:
        ch_d "Не мог бы ты стать моим хозяином?"
    $ DoreenX.History.append("master")
    while "master" not in DoreenX.Petnames:
        menu:
            extend ""
            "Конечно.":
                    $ DoreenX.Petnames.append("master")
                    $ DoreenX.Statup("Love", 200, 1)
                    $ DoreenX.Statup("Obed", 200, 2)
                    ch_d "Ох, потрясающе! . ."
            "Я ждала этого." if "expected" not in DoreenX.RecentActions and not Player.Male:
                    $ DoreenX.RecentActions.append("expected")
                    $ DoreenX.Statup("Obed", 200, 4)
                    $ DoreenX.Statup("Inbt", 70, 2)
                    ch_d "О. . . правда?"
            "Я ждал этого." if "expected" not in DoreenX.RecentActions and Player.Male:
                    $ DoreenX.RecentActions.append("expected")
                    $ DoreenX.Statup("Obed", 200, 4)
                    $ DoreenX.Statup("Inbt", 70, 2)
                    ch_d "О. . . правда?"
            "Агась.":
                    $ DoreenX.Petnames.append("master")
                    $ DoreenX.FaceChange("confused",1,Eyes="side")
                    $ DoreenX.Statup("Obed", 200, -1)
                    ch_d "Я. . . рада. . ."
                    $ DoreenX.FaceChange("normal",1)
            "Меня устраивают наши текущие отношения.":
                    $ DoreenX.FaceChange("sadside",2)
                    $ DoreenX.Statup("Love", 80, -1)
                    $ DoreenX.Statup("Obed", 200, -2)
                    $ DoreenX.Statup("Inbt", 70, -2)
                    ch_d "Ох. . . ладно. . ."
                    $ DoreenX.FaceChange("normal",1)
                    ch_d "Это тоже здорово. . ."
                    return
            "Не-а.":
                    $ DoreenX.FaceChange("sad",2,Eyes="surprised")
                    $ DoreenX.Statup("Love", 80, -1)
                    $ DoreenX.Statup("Obed", 200, -4)
                    $ DoreenX.Statup("Inbt", 70, -2)
                    ch_d "Ох. . ."
                    $ DoreenX.FaceChange("sad",2)
                    ch_d "Я все испортила, да. . ?"
                    hide Doreen_Sprite with easeoutright
                    call Remove_Girl(DoreenX)
                    $ DoreenX.FaceChange("normal",1)
                    $ DoreenX.Loc = "hold" #puts her off the board for the day
                    "Она уходит."
                    return
            "Что ты имеешь в виду?" if "what" not in DoreenX.RecentActions:
                    $ DoreenX.RecentActions.append("what")
                    $ DoreenX.Statup("Obed", 200, -1)
                    ch_d "Я просто подумала, что могла бы стать твоей. . .  слугой? . ."
            ". . ." if ". . ." not in DoreenX.RecentActions:
                    $ DoreenX.RecentActions.append(". . .")
                    $ DoreenX.Statup("Love", 90, -1)
                    $ DoreenX.Statup("Obed", 200, 5)
                    $ DoreenX.Statup("Inbt", 50, 1)
                    $ DoreenX.FaceChange("confused", 1)
                    ch_d "Эм. . ."
                    $ DoreenX.FaceChange("sly", 1)
                    ch_d "-мне становится как-то неловко . ."
            ". . ." if ". . ." in DoreenX.RecentActions:
                    $ DoreenX.Statup("Love", 90, -3)
                    $ DoreenX.Statup("Obed", 200, -1)
                    $ DoreenX.Statup("Inbt", 50, 2)
                    $ DoreenX.FaceChange("confused", 1)
                    ch_d "Ладно. . ."
                    $ DoreenX.FaceChange("sly", 1)
                    ch_d "Я думаю, это \"нет\". . ."
                    ch_d "Наверное, тебе нужно немного подумать. . ."
                    return

    if not Player.Male:
        ch_d ". . . хозяйка."
    else:
        ch_d ". . . хозяин."
    menu:
        extend ""
        ". . .":
                if not Player.Male:
                    $ DoreenX.Petname = "хозяйка"
                    $ DoreenX.Petname_rod = "хозяйки"
                    $ DoreenX.Petname_dat = "хозяйке"
                    $ DoreenX.Petname_vin = "хозяйку"
                    $ DoreenX.Petname_tvo = "хозяйкой"
                    $ DoreenX.Petname_pre = "хозяйке"
                else:
                    $ DoreenX.Petname = "хозяин"
                    $ DoreenX.Petname_rod = "хозяина"
                    $ DoreenX.Petname_dat = "хозяину"
                    $ DoreenX.Petname_vin = "хозяина"
                    $ DoreenX.Petname_tvo = "хозяином"
                    $ DoreenX.Petname_pre = "хозяине"
                $ DoreenX.FaceChange("smile", 2, Eyes="side")
                $ DoreenX.Statup("Obed", 200, 2)
        "Слушай, а хорошо звучит.":
                if not Player.Male:
                    $ DoreenX.Petname = "хозяйка"
                    $ DoreenX.Petname_rod = "хозяйки"
                    $ DoreenX.Petname_dat = "хозяйке"
                    $ DoreenX.Petname_vin = "хозяйку"
                    $ DoreenX.Petname_tvo = "хозяйкой"
                    $ DoreenX.Petname_pre = "хозяйке"
                else:
                    $ DoreenX.Petname = "хозяин"
                    $ DoreenX.Petname_rod = "хозяина"
                    $ DoreenX.Petname_dat = "хозяину"
                    $ DoreenX.Petname_vin = "хозяина"
                    $ DoreenX.Petname_tvo = "хозяином"
                    $ DoreenX.Petname_pre = "хозяине"
                $ DoreenX.FaceChange("normal", 1)
                $ DoreenX.Statup("Love", 90, 1)
                $ DoreenX.Statup("Obed", 200, 2)
                $ DoreenX.Statup("Inbt", 80, 2)
        "Мне не нравится, когда ты называешь меня \"хозяйка.\"" if not Player.Male:
                $ DoreenX.FaceChange("sad", 1,Mouth="smile")
                $ DoreenX.Statup("Love", 90, 2)
                $ DoreenX.Statup("Obed", 200, 3)
                ch_d "И \босс-белка?\" не нравится?"
                menu:
                    extend ""
                    "Не, это нравится.":
                            $ DoreenX.Petname = "Босс-Белка"
                            $ DoreenX.Petname_rod = "Босса-Белки"
                            $ DoreenX.Petname_dat = "Боссу-Белке"
                            $ DoreenX.Petname_vin = "Босса-Белку"
                            $ DoreenX.Petname_tvo = "Боссом-Белкой"
                            $ DoreenX.Petname_pre = "Боссе-Белке"
                            $ DoreenX.FaceChange("surprised", 1)
                            $ DoreenX.Statup("Love", 90, 1)
                            ch_d "Да?! Хорошо!"
                            $ DoreenX.FaceChange("sly", 1)
                            ch_d ". . . [DoreenX.Petname]."
                    "Нет.":
                            $ DoreenX.FaceChange("sad", 1)
                            ch_d "Ладно. . ."
                            $ DoreenX.FaceChange("sly", 1)
                            ch_d "Тогда буду звать тебя просто [DoreenX.Petname_tvo]."
                    ". . .":
                            $ DoreenX.FaceChange("sly", 1)
                            ch_d "Ладно, значит \"нет\". . ."
                            ch_d "Тогда буду звать тебя просто [DoreenX.Petname_tvo]."
        "Мне не нравится, когда ты называешь меня \"хозяин.\"" if Player.Male:
                $ DoreenX.FaceChange("sad", 1,Mouth="smile")
                $ DoreenX.Statup("Love", 90, 2)
                $ DoreenX.Statup("Obed", 200, 3)
                ch_d "И \босс-белка?\" не нравится"
                menu:
                    extend ""
                    "Не, это нравится.":
                            $ DoreenX.Petname = "Босс-Белка"
                            $ DoreenX.Petname_rod = "Босса-Белки"
                            $ DoreenX.Petname_dat = "Боссу-Белке"
                            $ DoreenX.Petname_vin = "Босса-Белку"
                            $ DoreenX.Petname_tvo = "Боссом-Белкой"
                            $ DoreenX.Petname_pre = "Боссе-Белке"
                            $ DoreenX.FaceChange("surprised", 1)
                            $ DoreenX.Statup("Love", 90, 1)
                            ch_d "Да?! Хорошо!"
                            $ DoreenX.FaceChange("sly", 1)
                            ch_d ". . . [DoreenX.Petname]."
                    "Нет.":
                            $ DoreenX.FaceChange("sad", 1)
                            ch_d "Ладно. . ."
                            $ DoreenX.FaceChange("sly", 1)
                            ch_d "Тогда буду звать тебя просто [DoreenX.Petname_tvo]."
                    ". . .":
                            $ DoreenX.FaceChange("sly", 1)
                            ch_d "Ладно, значит \"нет\". . ."
                            ch_d "Тогда буду звать тебя просто [DoreenX.Petname_tvo]."


    if "tail" not in DoreenX.History:
            ch_d "Кстати. . ."
            $ DoreenX.FaceChange("sadside",2)
            ch_d "Что ты думаешь о моем гигантском хвосте?"
            ch_d "Я тут подумываю о том, чтобы. . . удалить его. . ."
            call Doreen_Tail
            if not DoreenX.Tail:
                    $ DoreenX.FaceChange("smile",1)
                    $ DoreenX.Statup("Obed", 200, 3)
                    ch_d "Ох, прямо гора с плечь."
                    ch_d "Тяжело постоянно таскать 3-4 кг меха."
            ch_d "Теперь, когда мы с этим разобрались, что еще у тебя на уме?"
    $ DoreenX.FaceChange("sly",1)
    ch_d "Дай мне знать, если тебе что-нибудь понадобится."
    ch_d "Ты же знаешь, что я хороша. . ."
    return

# end Doreen_Master//////////////////////////////////////////////////////////



# start Doreen_Sexfriend//////////////////////////////////////////////////////////

label Doreen_Sexfriend:   #Doreen_Update
        $ DoreenX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ Event_Queue = [0,0]
        call Set_The_Scene
        $ Line = 0
        $ DoreenX.FaceChange("smile",2)
        if DoreenX.Loc != bg_current:
                $ DoreenX.Loc = bg_current
                "Появляется [DoreenX.Name]."
        else:
                "[DoreenX.Name] подходит к вам и отводит вас в сторону."
        call Display_Girl(DoreenX)
        $ DoreenX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in DoreenX.History:
                call expression DoreenX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        call Shift_Focus(DoreenX)
        $ DoreenX.Petnames.append("sex friend")
        ch_d "У белок, знаешь, все намного проще."
        menu:
            extend ""
            "Да?":
                    ch_d "Да!"
            "Я не хочу знать, о чем ты говоришь.":
                    ch_d "Выслушай меня!"
            "Что?":
                    pass
            "О, я знаю, к чему все идет." if "lover" in DoreenX.Petnames:
                    ch_d "На этот раз все иначе!"
            ". . .":
                    pass

        if "lover" not in DoreenX.Petnames:
                ch_d "Я про. . . отношения."
                ch_d "Честно говоря, им вообще такое не интересно. . ."
                ch_d "Они просто. . ."
                ch_d "Как бы. . ."
                ch_d "Переходят сразу. . . к делу."
                menu:
                    extend ""
                    "Ты этого хочешь?":
                            ch_d "Ты так хорошо меня знаешь. . ."
                    "Конечно.":
                            pass
                    "И чем они отличаются от нас?":
                            ch_d "Ох. . . может и ничем. . ."
                    ". . .":
                            pass
        else:
                if not Player.Male:
                    ch_d "Понимаешь, ты мне небезразлична."
                else:
                    ch_d "Понимаешь, ты мне небезразличен."
                ch_d "Но это не значит, что мы не можем получать -иного рода- удовольствие от \"общения\"."

        ch_d "Иногда мне хочется просто повеселиться, подобно животным, которыми мы и являемся. . ."
        if DoreenX in Player.Harem:
                ch_d "Как считаешь, если бы мы не были \"вместе\", мы могли бы быть. . . \"секс-партнерами?\""
        else:
                ch_d "Как считаешь, мы можем быть. . . \"секс-партнерами?\""
        $ DoreenX.Statup("Love", 90, 10)
        $ DoreenX.Statup("Obed", 90, 5)
        $ DoreenX.Statup("Inbt", 90, 15)
        if Taboo:
            ch_d "Не хочешь отойти в более укромное место?"
            menu:
                extend ""
                "Пошли":
                        $ DoreenX.Statup("Love", 90, 3)
                        $ DoreenX.Statup("Inbt", 200, 5)
                        ch_d "-Отлично.-"
                        if bg_current == "bg player":
                                $ bg_current = "bg doreen"
                        else:
                                $ bg_current = "bg player"
                        $ DoreenX.Loc = bg_current
                        $ Party = []
                        call Set_The_Scene
                        call CleartheRoom(DoreenX)
                        call Set_The_Scene
                        $ Taboo = 0
                        $ DoreenX.Taboo = 0

                "Нет, давай сделаем это здесь.":
                        $ DoreenX.Statup("Obed", 80, 5)
                        $ DoreenX.Statup("Inbt", 90, 15)
                        ch_d "Ооох. . . это -по-дикому.-"
                "Не сейчас.":
                        $ DoreenX.FaceChange("sad", 1)
                        $ DoreenX.Statup("Love", 90, -3)
                        $ DoreenX.Statup("Obed", 90, 5)
                        ch_d "Оу, облом. . ."
                        return
        else:
            ch_d "Думаю, сейчас самое подходящее время начать?"
            menu:
                extend ""
                "Конечно.":
                        $ DoreenX.Statup("Love", 90, 3)
                        $ DoreenX.Statup("Inbt", 90, 5)
                        ch_d "-Отлично.-"
                "Давай не сейчас.":
                        $ DoreenX.FaceChange("sad", 1)
                        $ DoreenX.Statup("Love", 90, -3)
                        $ DoreenX.Statup("Obed", 90, 5)
                        ch_d "Оу, облом. . ."
                        return
        $ Situation = DoreenX
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        #end "if no relationship"
        jump Misplaced
        return

# end Doreen_Sexfriend//////////////////////////////////////////////////////////


# start Doreen_Fuckbuddy//////////////////////////////////////////////////////////

label Doreen_Fuckbuddy:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(DoreenX,"sly","выглядит взволнованной. . .")
                return
        $ DoreenX.DailyActions.append("relationship")
        $ DoreenX.Lust = 60
        $ DoreenX.Wet = 2
        $ DoreenX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        #change Doreen's outfit to default
        $ DoreenX.Loc = bg_current
        call Shift_Focus(DoreenX)
        call Set_The_Scene(0)
        call Display_Girl(DoreenX)
        call Taboo_Level

        #$ DoreenX.Event[10] += 1

        $ Event_Queue = [0,0]
        if DoreenX.Loc != bg_current:
                $ DoreenX.Loc = bg_current
                "Появляется [DoreenX.Name]."
        else:
                "[DoreenX.Name] поворачивается к вам."
        $ DoreenX.Petnames.append("fuck buddy")
        $ DoreenX.FaceChange("sly",1,Eyes="surprised")
        ch_d "Слушай, помнишь, я говорила, что белки только и делают, что спариваются?"
        menu:
            extend ""
            "Да?":
                    $ DoreenX.Statup("Love", 90, 2)
                    $ DoreenX.Statup("Inbt", 90, 3)
            "А?":
                    pass
            "Ты слишком много говоришь о белках.":
                    $ DoreenX.FaceChange("angry",1)
                    $ DoreenX.Statup("Love", 90, -3)
                    ch_d "Нет, ты-"
                    $ DoreenX.Statup("Love", 90, 5)
                    $ DoreenX.Statup("Obed", 90, 5)
                    $ DoreenX.FaceChange("sly",2,Eyes="side")
                    ch_d "Ладно, может быть."
                    $ DoreenX.FaceChange("sly",1)
                    ch_d "В общем. . ."
            ". . .":
                    pass
        ch_d "Когда я думаю об этом, у меня немного мутнеет в голове."
        $ DoreenX.FaceChange("sly",2,Eyes="side")
        ch_d "И, эм. . . В такие моменты мне очень нужна помощь, сейчас, кстати, именно он."
        $ DoreenX.FaceChange("sly",1)
        if Taboo:
            if bg_current == "bg player":
                    ch_d "Может, эм, пойдем ко мне?"
            else:
                    ch_d "Может, эм, вернемся в твою комнату?"
            menu:
                extend ""
                "Ага":
                        $ DoreenX.FaceChange("smile",1)
                        $ DoreenX.Statup("Love", 80, 2)
                        $ DoreenX.Statup("Inbt", 200, 10)
                        ch_d "Потрясающе!"
                        if bg_current == "bg player":
                                $ bg_current = "bg doreen"
                        else:
                                $ bg_current = "bg player"
                        $ DoreenX.Loc = bg_current
                        call CleartheRoom(DoreenX)
                        call Set_The_Scene
                        $ Taboo = 0
                        $ DoreenX.Taboo = 0

                "Нет, давай сделаем это здесь.":
                        $ DoreenX.Statup("Obed", 80, 5)
                        $ DoreenX.Statup("Inbt", 200, 15)
                        ch_d "Ох, хорошо. . ."
                "Давай не сейчас.":
                        $ DoreenX.FaceChange("sad", 1)
                        $ DoreenX.Statup("Love", 90, -3)
                        $ DoreenX.Statup("Obed", 90, 5)
                        ch_d "Оу!"
                        return
        else:
            if not Player.Male:
                ch_d "Так вот. . . не могла бы ты меня. . . оттрахать?"
            else:
                ch_d "Так вот. . . не мог бы ты меня. . . оттрахать?"
            menu:
                extend ""
                "Конечно.":
                        $ DoreenX.Statup("Love", 90, 3)
                        $ DoreenX.Statup("Inbt", 200, 5)
                        ch_d "Здорово."
                "Давай не сейчас.":
                        $ DoreenX.FaceChange("sad", 1)
                        $ DoreenX.Statup("Love", 90, -3)
                        $ DoreenX.Statup("Obed", 90, 5)
                        ch_d "Оу!"
                        return
        $ DoreenX.Statup("Inbt", 200, 10)
        $ Situation = DoreenX
        $ Player.AddWord(1,"interruption") #adds to Recent
#        call Doreen_SexPrep              #she offers sex
        call SexMenu
        jump Misplaced
        return
# end Doreen_Fuckbuddy//////////////////////////////////////////////////////////

# start Doreen_Daddy//////////////////////////////////////////////////////////

#Not updated

label Doreen_Daddy:       #Doreen_Update
        $ DoreenX.DailyActions.append("relationship")
        $ DoreenX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(DoreenX)
        if DoreenX.Loc != bg_current:
                $ DoreenX.Loc = bg_current
                "[DoreenX.Name] подходит к вам."
        call Set_The_Scene
        $ Event_Queue = [0,0]
        $ DoreenX.FaceChange("sadside",1,Mouth="normal")
        ch_d ". . ."
        ch_d "У меня вопрос. . ."
        $ DoreenX.FaceChange("sadside",1,Mouth="smirk")
        ch_d "Мне. . . вроде бы хочется попробовать. . ."
        $ DoreenX.FaceChange("sadside",2,Mouth="smirk")
        ch_d "Кое-какую. . . \"ролевую игру.\" . ."
        ch_d "Ничего особенного, просто. . ."
        $ DoreenX.FaceChange("sad",2,Mouth="normal")
        ch_d ". . . мне бы хотелось звать тебя. . ."
        $ DoreenX.FaceChange("sadside",2,Mouth="normal")
        if not Player.Male:
            ch_d "\"мамочкой\", что скажешь?"
        else:
            ch_d "\"папочкой\", что скажешь?"
        menu:
            extend ""
            "Ладно, давай?":
                $ DoreenX.FaceChange("smile")
                $ DoreenX.Statup("Love", 90, 20)
                $ DoreenX.Statup("Obed", 60, 10)
                $ DoreenX.Statup("Inbt", 80, 30)
                ch_d "Ох. . . здорово."
            "Зачем?":
                $ DoreenX.FaceChange("bemused")
                ch_d "Ох, эм. . ."
                if DoreenX.Love > DoreenX.Obed and DoreenX.Love > DoreenX.Inbt:
                        ch_d "Я. . . посмотрела один фильм и. . . вот. . ."
                elif DoreenX.Obed > DoreenX.Inbt:
                        ch_d "Ты настоящий лидер, и. . . эм. . ."
                else:
                        ch_d "Это немного странно, да?"

                menu:
                    extend ""
                    "Звучит интересно, меня устраивает.":
                            $ DoreenX.FaceChange("smile")
                            $ DoreenX.Statup("Love", 90, 15)
                            $ DoreenX.Statup("Obed", 60, 20)
                            $ DoreenX.Statup("Inbt", 80, 25)
                            ch_d "Здорово!"
                            $ DoreenX.FaceChange("sly",2)
                            if not Player.Male:
                                ch_d " . . . мамочка."
                            else:
                                ch_d " . . . папочка."
                            $ DoreenX.FaceChange("sly",1)
                            if not Player.Male:
                                $ DoreenX.Petname = "мамочка"
                                $ DoreenX.Petname_rod = "мамочки"
                                $ DoreenX.Petname_dat = "мамочке"
                                $ DoreenX.Petname_vin = "мамочку"
                                $ DoreenX.Petname_tvo = "мамочкой"
                                $ DoreenX.Petname_pre = "мамочке"
                            else:
                                $ DoreenX.Petname = "папочка"
                                $ DoreenX.Petname_rod = "папочки"
                                $ DoreenX.Petname_dat = "папочке"
                                $ DoreenX.Petname_vin = "папочку"
                                $ DoreenX.Petname_tvo = "папочкой"
                                $ DoreenX.Petname_pre = "папочке"
                    "Может, лучше не надо, пожалуйста?":
                            $ DoreenX.Statup("Love", 90, 5)
                            $ DoreenX.Statup("Obed", 80, 40)
                            $ DoreenX.Statup("Inbt", 80, 20)
                            $ DoreenX.FaceChange("sad")
                            ch_d ". . ."
                            ch_d "Ладно. . ."
                    "У тебя серьезные проблемы с отцом, да?" if Player.Male:
                            $ DoreenX.Statup("Love", 90, -15)
                            $ DoreenX.Statup("Obed", 80, 45)
                            $ DoreenX.Statup("Inbt", 70, 5)
                            $ DoreenX.FaceChange("sadside",2)
                            ch_d "Ну. . . давай не будем об этом говорить. . ."
                            $ DoreenX.FaceChange("sadside",1)
                    "У тебя серьезные проблемы с матерью, да?" if not Player.Male:
                            $ DoreenX.Statup("Love", 90, -15)
                            $ DoreenX.Statup("Obed", 80, 45)
                            $ DoreenX.Statup("Inbt", 70, 5)
                            $ DoreenX.FaceChange("sadside",2)
                            ch_d "Ну. . . давай не будем об этом говорить. . ."
                            $ DoreenX.FaceChange("sadside",1)

            "У тебя серьезные проблемы с отцом, да?" if Player.Male:
                    $ DoreenX.Statup("Love", 90, -15)
                    $ DoreenX.Statup("Obed", 80, 45)
                    $ DoreenX.Statup("Inbt", 70, 5)
                    $ DoreenX.FaceChange("sadside",2)
                    ch_d "Ну. . . давай не будем об этом говорить. . ."
                    $ DoreenX.FaceChange("sadside",1,Mouth="normal")
            "У тебя серьезные проблемы с матерью, да?" if not Player.Male:
                    $ DoreenX.Statup("Love", 90, -15)
                    $ DoreenX.Statup("Obed", 80, 45)
                    $ DoreenX.Statup("Inbt", 70, 5)
                    $ DoreenX.FaceChange("sadside",2)
                    ch_d "Ну. . . давай не будем об этом говорить. . ."
                    $ DoreenX.FaceChange("sadside",1,Mouth="normal")
        $ DoreenX.Petnames.append("daddy")
        return

# end Doreen_Daddy//////////////////////////////////////////////////////////



# Start Character Meet Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gwen Meet Doreen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Doreen_Meet:
        # GwenX.Event[2] tracks number of girls she knows you're dating
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = bg_current
        $ DoreenX.Loc = bg_current
        call Shift_Focus(GwenX)
        $ GwenX.ArmPose = 2
        call Set_The_Scene
        $ GwenX.FaceChange("normal",1)
        $ DoreenX.FaceChange("smile",1)
        ch_d "Привет, [DoreenX.Petname]. . ."
        if DoreenX.Petname in ("хозяин", "господин", "хозяйка", "госпожа"):
                $ GwenX.Statup("Obed", 60, 2)
                $ GwenX.Statup("Obed", 80, 5)
        $ GwenX.ArmPose = 1
        $ DoreenX.ArmPose = 2
        hide Doreen_Seated
        show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc)
        hide Gwen_Seated
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom -1
        $ GwenX.Hat = 0
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_g "Подожди-ка. . . ты? . . "
        ch_g "-фурри?"
        $ DoreenX.FaceChange("confused",1)
        ch_d "Эм. . . я Дорин Грин. Можешь звать меня [DoreenX.Name_tvo]."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        $ DoreenX.FaceChange("confused",1,Eyes="surprised")
        ch_g "О! Конечно, Девушка-Белка. Я поняла."
        $ DoreenX.FaceChange("confused",1,Eyes="sexy")
        ch_g "Гвендолин Пул, зови меня [GwenX.Name]!"
        if "Squirrel Girl" not in DoreenX.Names:
                $ DoreenX.FaceChange("confused",1,Eyes="side")
                ch_d "Ладно. . . почему меня все так называют? . ."
                $ DoreenX.Names.append("Squirrel Girl") if "Squirrel Girl" not in DoreenX.Names else 0
                if DoreenX.Tail:
                        "[GwenX.Name] наклоняется к вам и шепчет:"
                        ch_g "[[Я думаю, это из-за хвоста. Это же хвост, правда?]"
                        $ DoreenX.FaceChange("angry",1,Eyes="side")
                        $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="sad")
        ch_d "О, я поняла."
        $ DoreenX.FaceChange("smile",1,Eyes="side")
        ch_d "Должно быть меня называют белкой из-за этого обруча с ушками."
        $ GwenX.FaceChange("confused",1,Eyes="side")
        menu:
            extend ""
            ". . .":
                    pass
            "Конечно.":
                    $ DoreenX.FaceChange("smile",1)
                    $ GwenX.FaceChange("smirk",1,Eyes="side")
                    $ DoreenX.Statup("Love", 80, 2)
                    ch_d "Не напоминай."
        $ DoreenX.FaceChange("smile",1,Eyes="side")
        $ GwenX.FaceChange("sad",1,Eyes="side",Mouth="open")
        ch_g "Извини! Я не должна была предполагать."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "А обезьянка Джо с тобой?"
        $ DoreenX.FaceChange("sad",1,Eyes="down")
        $ GwenX.FaceChange("sad",1,Eyes="side")
        ch_d "Он. . . скончался."
        ch_g "Ох! Прости! Я забыла. . ."
        ch_d "Откуда ты вообще о нем знаешь?"
        menu:
            extend ""
            "Она многое знает.":
                    $ GwenX.Statup("Love", 80, 2)
                    $ GwenX.Statup("Obed", 90, 2)
                    $ GwenX.FaceChange("smile",1,Mouth="open")
            "Она просто угадала.":
                    $ GwenX.Statup("Love", 80, -2)
                    $ GwenX.Statup("Obed", 80, 3)
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    ch_g "Эй!"
            "Она сумасшедшая.":
                    $ DoreenX.FaceChange("confused",1)
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    $ GwenX.Statup("Love", 80, -4)
                    $ GwenX.Statup("Obed", 90, 5)
                    ch_g "Эй!"
            ". . .":
                    pass
        $ DoreenX.FaceChange("confused",1,Eyes="side")
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "Я прочитала в комиксах?"
        ch_d "Что?"
        $ GwenX.FaceChange("confused",1,Eyes="side")
        ch_g "Я прибыла из настоящего мира, а это все видеоигра-"
        ch_g "В общем, это долгая история."
        $ DoreenX.FaceChange("smile",1,Eyes="side")
        ch_d "О, видеоигра. Понятно."
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_g "Ты мне веришь?"
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_d "Я верю в то, что -ты- в это веришь, какой смысл спорить?"
        ch_g "И правда. . ."
        $ DoreenX.FaceChange("smile",1,Eyes="side")
        ch_d "Кстати, [DoreenX.Petname], похоже, на тебя не жалуется."
        menu:
            extend ""
            "Ага, она клевая.":
                    $ GwenX.Statup("Love", 80, 3)
                    ch_g "Ага, я клевая!"
            "Ты привыкнешь к ней.":
                    $ GwenX.Statup("Love", 80, 2)
                    ch_g "Не сомневаюсь!"
            "Что? Нет.":
                    $ GwenX.Statup("Love", 80, -2)
                    $ GwenX.Statup("Obed", 90, 2)
                    $ GwenX.FaceChange("angry",2,Mouth="open")
                    ch_g "Эй!"
            ". . .":
                    $ GwenX.Statup("Love", 80, -1)
                    $ GwenX.Statup("Obed", 90, 2)
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    ch_g "Ничего не скажешь?!"

        $ GwenX.FaceChange("smile",1,Eyes="side")
        if not Player.Male:
            ch_g "Ты, наверное, хорошо знакома с ней? . ."
        else:
            ch_g "Ты, наверное, хорошо знакома с ним? . ."
        if DoreenX in Player.Harem:
                $ DoreenX.FaceChange("sly",1)
                $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
                $ DoreenX.Statup("Obed", 80, 1)
                $ DoreenX.Statup("Inbt", 80, 2)
                ch_d "Думаю, мы встречаемся. . ."
                $ GwenX.FaceChange("surprised",1,Eyes ="side")
                if GwenX.Event[2] > 1:
                        #if doreen heard you were dating two+ girls
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "Даже ты? . ."
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_d "Хехе. . . Ага-"
                        ch_d "Эй!"
                elif GwenX.Event[2]:
                        #if doreen heard you were dating someone else
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 3)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "Даже ты? . ."
                        $ GwenX.Statup("Obed", 50, 4)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_d "Хехе. . . Ага-"
                        ch_d "Эй!"
                else:
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Obed", 60, 2)
                        $ GwenX.Statup("Obed", 80, 2)
                        $ GwenX.FaceChange("sly",1)
                        ch_g "Ох. . . клево, клево. . ."
                $ GwenX.Event[2] += 1
        elif DoreenX.Petname in ("хозяин", "господин", "хозяйка", "госпожа"):
                $ DoreenX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                if not Player.Male:
                    ch_d "Ну, думаю, она моя [DoreenX.Petname]. . ."
                else:
                    ch_d "Ну, думаю, он мой [DoreenX.Petname]. . ."
        elif not ApprovalCheck(DoreenX, 500, "L"):
                $ DoreenX.FaceChange("normal",0)
                if not Player.Male:
                    ch_d "Ну, она. . . иногда мне помогает. . ."
                else:
                    ch_d "Ну, он. . . иногда мне помогает. . ."
        else:
                $ DoreenX.FaceChange("sad",1,Eyes="leftside")
                if not Player.Male:
                    ch_d "Ну, она. . . иногда прикрывает меня. . ."
                else:
                    ch_d "Ну, он. . . иногда прикрывает меня. . ."
        $ GwenX.FaceChange("normal",1,Eyes="side")
        $ DoreenX.FaceChange("smile",1,Eyes="side",Mouth="open")
        ch_g "Мне, эм. . . в общем, как-нибудь свидимся!"
        ch_d "Конечно! До встречи!"
        $ GwenX.FaceChange("normal",1)
        $ DoreenX.FaceChange("smile",1)
        $ DoreenX.GirlLikeUp(GwenX,100)
        $ GwenX.GirlLikeUp(DoreenX,100)
        $ GwenX.DrainWord("Doreen",0,0,0,1)
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
        return

# End Gwen Meet Doreen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# End Character Meet Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Doreen_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        if "switched" in DoreenX.History:
                jump Doreen_Switch2
        $ DoreenX.FaceChange("normal", 1)
        ch_d "Привет?"
        $ DoreenX.FaceChange("confused", 1)
        ch_d "Подожди-ка. . ."
        ch_d ". . ."
        ch_d "Вы, наверное, с [Player.XName_tvo] близнецы или типа того!"
        ch_d "Вы знакомы друг с другом?"
        menu:
            extend ""
            "Это я и есть, я [Player.XName].":
                    $ DoreenX.FaceChange("perplexed", 1)
                    ch_d "М?"
                    $ DoreenX.FaceChange("smile", 1)
                    ch_d "О!"
                    $ DoreenX.AddWord(1,"switch") #recent

            "Нет.":
                    ch_d "Хм. Вы действительно очень похожи, мне стоит как-нибудь вас познакомить."
                    ch_d "Кстати, меня зовут [DoreenX.Name]."
                    ch_d "А тебя как?"
            "Возможно?":
                    ch_d "\"Возможно?\" . ."

        if "switch" not in DoreenX.RecentActions:
                    $ DoreenX.FaceChange("confused", 1)
                    ch_d ". . ."
                    $ DoreenX.FaceChange("surprised", 1,Mouth= "open")
                    ch_d "Ты [Player.XName]!"
                    $ DoreenX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Ага, это я, [Player.XName].":
                                $ DoreenX.FaceChange("smile", 1)
                                $ DoreenX.Statup("Love", 90, 1)
                                $ DoreenX.Statup("Obed", 70, 1)
                                ch_d "Тебе удалось ненадолго меня запутать!"
                                $ DoreenX.FaceChange("normal", 1)
                        "Нет.":
                                $ DoreenX.FaceChange("bemused", 1)
                                $ DoreenX.Statup("Obed", 60, 1)
                                $ DoreenX.Statup("Obed", 70, 1)
                                ch_d "Угу-м."
                        "Возможно?":
                                $ DoreenX.FaceChange("sly", 1)
                                $ DoreenX.Statup("Love", 80, 1)
                                $ DoreenX.Statup("Obed", 70, 1)
                                $ DoreenX.Statup("Inbt", 60, 1)
                                ch_d "Да-да."
                    ch_d "Зачем ты надо мной издеваешься?"
                    menu:
                        extend ""
                        "Извини, хотелось пошутить.":
                                $ DoreenX.FaceChange("sly", 1)
                                $ DoreenX.Statup("Love", 70, 1)
                        "Молодец, ты все поняла.":
                                $ DoreenX.FaceChange("sly", 1)
                                $ DoreenX.Statup("Obed", 70, 1)
                                $ DoreenX.Statup("Inbt", 80, 1)
                                ch_d "Простая работенка для не самого лучшего детектива."
                        "Хех.":
                                $ DoreenX.FaceChange("sly", 1,Eyes="side")
                                $ DoreenX.Statup("Love", 70, 1)
                                $ DoreenX.Statup("Love", 90, 1)
                                $ DoreenX.Statup("Inbt", 70, 1)
                                ch_d "Миленько. . ."
                    ch_d "В общем, я тебя раскусила. . ."
        #end "tried to lie"
        $ DoreenX.FaceChange("smile", 1)
        ch_d "Не возражаешь, если я спрошу, почему тебе захотелось перемен?"
        menu:
            extend ""
            "Да так, по приколу.":
                    $ DoreenX.Statup("Inbt", 70, 1)
                    $ DoreenX.FaceChange("sly", 1)
                    ch_d "Ох, ну ладно."
            "Я так себя сейчас ощущаю.":
                    ch_d "Ладно, больше ничего не говори."
            "У меня не было каких-то особых причин.":
                    ch_d "Без причин люди не идут на перемены."

        if [Player.Name] != [Player.XName]:
                ch_p "А еще теперь меня зовут [Player.Name_tvo]."
                ch_d "Хорошо, приятно снова познакомиться с тобой, [Player.Name]."

        if DoreenX.SEXP >= 15:
                $ DoreenX.FaceChange("sad", 1,Mouth="normal")
                ch_d "Я тебе еще. . . \"нравлюсь\"?"
                menu:
                    extend ""
                    "Конечно!":
                            $ DoreenX.FaceChange("normal", 1)
                            $ DoreenX.Statup("Love", 70, 2)
                            $ DoreenX.Statup("Love", 90, 1)
                            ch_d "Ох! Отлично!"
                    "Да не особо.":
                            $ DoreenX.FaceChange("sad", 1)
                            $ DoreenX.Statup("Love", 80, -2)
                            $ DoreenX.Statup("Obed", 60, 2)
                            $ DoreenX.Statup("Obed", 80, 2)
                            ch_d ". . . я понимаю."
                    "А ты как думаешь?":
                            $ DoreenX.FaceChange("sadside", 1)
                            $ DoreenX.Statup("Obed", 70, 1)
                            $ DoreenX.Statup("Inbt", 70, 1)
                            ch_d "Я даже не знаю. . ."
                            $ DoreenX.FaceChange("sly", 1)
                            ch_d "но надежда умирает последней."

        if not Player.Male and DoreenX.Les > 5:
                $ DoreenX.FaceChange("sly", 1)
                ch_d "Думаю, мне все равно, в каком теле ты находишься. . ."
        if ApprovalCheck(DoreenX, 1200):
                ch_d "Думаю, мне интересен новый опыт. . ."
                $ DoreenX.AddWord(1,0,0,0,"girltalk") #history
        else:
                $ DoreenX.FaceChange("normal", 1,Eyes="side")
                ch_d "В общем, увидимся. . ."
        $ DoreenX.Traits.remove("switchcheck")
        $ DoreenX.AddWord(1,0,0,0,"switched") #history
        return

label Doreen_Switch2:
        #when you switch for a 2+ time
        $ DoreenX.FaceChange("smile", 1)
        ch_d "О, [Player.Name], ты выглядишь как раньше."
        $ DoreenX.Traits.remove("switchcheck")
        $ DoreenX.History.remove("switched")
        $ DoreenX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Doreen_Girltalk(Auto=0,Other=0):
        # if Auto Doreen starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in DoreenX.History:
                return
        if "nogirls" in DoreenX.History:
                jump Doreen_Girltalk_Redux
        $ DoreenX.FaceChange("normal", 1)
        if Auto:
                ch_d "[Player.Name]. . ."
        ch_d "Итак. . . мне кажется, тебе нравятся девушки?"
        ch_d "Мне любопытно. . . эм. . ."
        ch_d "А -я- тебе тоже нравлюсь?"
        menu:
            extend ""
            "Да?":
                    $ DoreenX.FaceChange("sly", 1)
                    $ DoreenX.Statup("Love", 70, 2)
                    $ DoreenX.Statup("Love", 90, 2)
                    $ DoreenX.Statup("Obed", 70, 1)
                    ch_d "Ох. . . ладно. . . здорово. . ."
            "Наверное?":
                    $ DoreenX.FaceChange("confused", 1)
                    $ DoreenX.Statup("Love", 70, 1)
                    $ DoreenX.Statup("Obed", 80, 2)
                    $ DoreenX.Statup("Inbt", 80, 2)
                    ch_d "Ох. . . ладно. . ."
            "Не особо.":
                    $ DoreenX.FaceChange("surprised", 1)
                    $ DoreenX.Statup("Love", 90, -1)
                    $ DoreenX.Statup("Obed", 60, 2)
                    $ DoreenX.Statup("Obed", 80, 2)
                    ch_d "Ох."
                    ch_d "Я понимаю. . ."
        $ DoreenX.FaceChange("sly", 1)
        if not DoreenX.Les:
                ch_d "У меня. . ."
                $ DoreenX.FaceChange("sly", 2,Eyes="side")
                ch_d "-недостаточно опыта с девушками. . ."
        if not ApprovalCheck(DoreenX, 900) and not ApprovalCheck(DoreenX, 600, "L") and not DoreenX.Les:
                ch_d "Я. . . я не знаю, что я чувствую. . ."
                $ DoreenX.AddWord(1,0,0,0,"nogirls") #history
                call Girltalk_Check(DoreenX)
                return

        ch_d "Наверное. . . почему бы не попробовать что-то новое?"
        $ DoreenX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(DoreenX)
        return

label Doreen_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing
        if ApprovalCheck(DoreenX, 1000) or ApprovalCheck(DoreenX, 600, "L"):
                $ DoreenX.FaceChange("sly", 1)
                if Other in TotalGirls and "nogirls" in Other.History:
                        ch_d "Ну. . ."
                ch_d "Наверное. . . почему бы не попробовать что-то новое?"
                $ DoreenX.DrainWord("nogirls",0,0,0,1) #history
                $ DoreenX.AddWord(1,0,0,0,"girltalk") #history
        elif "nogirls" not in DoreenX.History:
                $ DoreenX.AddWord(1,0,0,0,"nogirls") #history
                ch_d "Хмм. . . я даже не знаю. . ."
        elif "nogirls" in DoreenX.DailyActions:
                $ DoreenX.FaceChange("angry", 1)
                if DoreenX.Forced:
                        #if Forced, she will just go with it anyway
                        if "nogirls" not in DoreenX.RecentActions:
                                $ DoreenX.Statup("Love", 80, -2)
                                $ DoreenX.Statup("Obed", 80, 2)
                                $ DoreenX.AddWord(1,"nogirls",0,0,0) #recent
                        return
                ch_d "Перестань спрашивать."
        else:
                $ DoreenX.Statup("Inbt", 50, 2)
                ch_d "Я не думаю, что у нас что-то получится. . ."
                $ DoreenX.AddWord(1,0,"nogirls",0,0) #daily
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Doreen_69_Intro:
        if "69" in DoreenX.History:
                return
        if Trigger == "lick pussy" and DoreenX.LickP:
                if DoreenX.Blow or DoreenX.CUN or (ApprovalCheck(DoreenX, 1300) and DoreenX.SeenPeen):
                        #if licking pussy but have gotten blowjob
                        $ DoreenX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_d "Итак. . . раз уж ты мне помогаешь. . ."
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
                        $ DoreenX.Pose = "69"
                        call Doreen_BJ_Launch
                        if Player.Male:
                            ch_d "Не мог бы ты, эм. . ."
                        else:
                            ch_d "Не могла бы ты, эм. . ."
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ DoreenX.Statup("Love", 95, 3)
                                    $ DoreenX.Statup("Inbt", 70, 2)
                                    $ DoreenX.Statup("Inbt", 90, 1)
                                    ch_d "Хех, спасибо."
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ DoreenX.Statup("Love", 80, -8)
                                    $ DoreenX.Statup("Obed", 80, 3)
                                    $ DoreenX.Statup("Obed", 90, 1)
                                    $ DoreenX.Statup("Inbt", 70, -1)
                                    ch_d "Оу, жаль."
                        $ Situation = "69"
                        call SexAct("blow") # call Doreen_SexAct("blow")
                        $ renpy.pop_call() #causes it to skip past the Escalation
                        $ renpy.pop_call() #causes it to skip past the last activity
        elif (Trigger == "blow" or Trigger == "cun") and (DoreenX.Blow or DoreenX.CUN):
                        #if licked pussy
                        $ DoreenX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_d "Слушай, эм. . . пока я на коленях. . ."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        $ DoreenX.Pose = "69"
                        call Doreen_BJ_Launch
                        if Player.Male:
                            ch_d "Не мог бы ты, эм. . ."
                        else:
                            ch_d "Не могла бы ты, эм. . ."
                        ch_d "-сделать и мне приятно?"
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ DoreenX.Statup("Love", 95, 3)
                                    $ DoreenX.Statup("Inbt", 70, 2)
                                    $ DoreenX.Statup("Inbt", 90, 1)
                                    ch_d "Хех, спасибо."
                                    if not DoreenX.LickP:
                                        $ DoreenX.LickP += 1
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ DoreenX.Statup("Love", 80, -5)
                                    $ DoreenX.Statup("Obed", 80, 3)
                                    $ DoreenX.Statup("Obed", 90, 1)
                                    $ DoreenX.Statup("Inbt", 70, -1)
                                    ch_d "Оу, жаль."
                        #returns to BJ already in progress
        return
