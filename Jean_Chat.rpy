# star Jean chat interface
#Jean Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Jean_Relationship: #rkelj
    while True:
        menu:
            ch_j "О чем ты хочешь поговорить?"
            "Хочешь стать моей девушкой?" if JeanX not in Player.Harem and "ex" not in JeanX.Traits:
                    $ JeanX.DailyActions.append("relationship")
                    if "asked boyfriend" in JeanX.DailyActions and "angry" in JeanX.DailyActions:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Опять начинаешь? Нет!"
                            return
                    elif "asked boyfriend" in JeanX.DailyActions:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Все еще нет."
                            return
                    elif JeanX.Break[0]:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Ты, должно быть, шутишь."
                            if Player.Harem:
                                    $ JeanX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    if not Player.Male:
                                        ch_p "Я серьезна как никогда."
                                    else:
                                        ch_p "Я серьезен как никогда."

                    $ JeanX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "JeanYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_j "Смотри, очевидно, что это может быть проблемой для остальных девушек, [JeanX.Petname]."
                        else:
                            ch_j "Смотри, очевидно,что это может быть проблемой для [Player.Harem[0].Name_rod], [JeanX.Petname]."
                        return

                    if JeanX.Event[5]:
                            $ JeanX.FaceChange("bemused", 1)
                            if not Player.Male:
                                ch_j "Смотри, в прошлый раз это ты ответила \"нет\". . ."
                            else:
                                ch_j "Смотри, в прошлый раз это ты ответил \"нет\". . ."
                    else:
                            $ JeanX.FaceChange("surprised", 2)
                            ch_j "Что? Зачем?"
                            $ JeanX.FaceChange("smile", 1)

                    call Jean_OtherWoman

                    if JeanX.Love >= 800:
                            $ JeanX.FaceChange("surprised", 1)
                            $ JeanX.Mouth = "smile"
                            if not JeanX.Event[5]:
                                    $ JeanX.Statup("Love", 200, 10)
                                    call Jean_BF
                                    return
                            $ JeanX.Statup("Love", 200, 40)
                            ch_j "Хм. Ладно."
                            if "boyfriend" not in JeanX.Petnames:
                                    $ JeanX.Petnames.append("boyfriend")
                            if "JeanYes" in Player.Traits:
                                    $ Player.Traits.remove("JeanYes")
                            $ Player.Harem.append(JeanX)
                            call Harem_Initiation
                            "[JeanX.Name] подходит и страстно целует вас."
                            $ JeanX.FaceChange("kiss", 1)
                            $ JeanX.Kissed += 1
                    elif JeanX.Obed >= 500:
                            $ JeanX.FaceChange("perplexed")
                            ch_j "\"Встречаться\". . . Хм. . ."
                            ch_j "Думаю, это не про нас. . ."
                    elif JeanX.Inbt >= 500:
                            $ JeanX.FaceChange("smile")
                            ch_j "-Нет-."
                    else:
                            $ JeanX.FaceChange("perplexed", 1)
                            ch_j "Успокойся уже, [JeanX.Petname]."

            "Может, начнем все сначала?" if "ex" in JeanX.Traits:
                    $ JeanX.DailyActions.append("relationship")
                    if "asked boyfriend" in JeanX.DailyActions and "angry" in JeanX.DailyActions:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Опять начинаешь? Нет!"
                            return
                    elif "asked boyfriend" in JeanX.DailyActions:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Я все еще не согласна."
                            return

                    $ JeanX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "JeanYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_j "Смотри, очевидно, что это может быть проблемой для остальных девушек, [JeanX.Petname]."
                            else:
                                ch_j "Смотри, очевидно,что это может быть проблемой для [Player.Harem[0].Name_rod], [JeanX.Petname]."
                            return

                    $ Cnt = 0
                    call Jean_OtherWoman

                    if JeanX.Love >= 800:
                            $ JeanX.FaceChange("surprised", 1)
                            $ JeanX.Mouth = "smile"
                            $ JeanX.Statup("Love", 90, 5)
                            ch_j "О, ладно, как скажешь."
                            if "boyfriend" not in JeanX.Petnames:
                                        $ JeanX.Petnames.append("boyfriend")
                            $ JeanX.Traits.remove("ex")
                            if "JeanYes" in Player.Traits:
                                        $ Player.Traits.remove("JeanYes")
                            $ Player.Harem.append(JeanX)
                            call Harem_Initiation
                            "[JeanX.Name] подходит и целует вас."
                            $ JeanX.FaceChange("kiss", 1)
                            $ JeanX.Kissed += 1
                    elif JeanX.Love >= 600 and ApprovalCheck(JeanX, 1500):
                            $ JeanX.FaceChange("smile", 1)
                            $ JeanX.Statup("Love", 90, 5)
                            ch_j "Конечно."
                            if "boyfriend" not in JeanX.Petnames:
                                    $ JeanX.Petnames.append("boyfriend")
                            $ JeanX.Traits.remove("ex")
                            if "JeanYes" in Player.Traits:
                                    $ Player.Traits.remove("JeanYes")
                            $ Player.Harem.append(JeanX)
                            call Harem_Initiation
                            $ JeanX.FaceChange("kiss", 1)
                            "[JeanX.Name] дарит вам легкий поцелуй."
                            $ JeanX.FaceChange("sly", 1)
                            $ JeanX.Kissed += 1
                    elif JeanX.Obed >= 500:
                            $ JeanX.FaceChange("sad")
                            ch_j "Не думаю, что нам стоит."
                    elif JeanX.Inbt >= 500:
                            $ JeanX.FaceChange("perplexed")
                            ch_j "Это совсем не весело."
                    else:
                            $ JeanX.FaceChange("perplexed", 1)
                            ch_j "Эм, нет."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if JeanX in Player.Harem:
                            call AskDateOther

            "Думаю, мы должны расстаться." if JeanX in Player.Harem:
                            if "breakup talk" in JeanX.RecentActions:
                                    ch_j "Я практически уверена, что мы уже обсуждали это."
                            elif "breakup talk" in JeanX.DailyActions:
                                    if not Player.Male:
                                        ch_j "Дурочка."
                                    else:
                                        ch_j "Дурачок."
                                    ch_j "Не сегодня, [JeanX.Petname]."
                            else:
                                    call Breakup(JeanX)

            "О разговоре, который у нас был ранее. . .":
                menu:
#                    "When you said you loved me. . ." if "lover" not in JeanX.Traits and JeanX.Event[6] >= 20 and JeanX.Event[6] != 23:
#                            call Jean_Love_Redux

#                    "When you were telling me all that stuff about yourself. . ." if "lover" not in JeanX.Traits and JeanX.Event[6] == 23:
#                            call Jean_Love_Redux

#                    "You said you wanted me to be more in control?" if "sir" not in JeanX.Petnames and "sir" in JeanX.History:
#                            if "asked sub" in JeanX.RecentActions:
#                                    ch_j "I'm pretty sure we already covered that."
#                            elif "asked sub" in JeanX.DailyActions:
#                                    ch_j "Maybe later. . ."
#                            else:
#                                    call Jean_Sub_Asked
#                    "You said you wanted me to be your Master?" if "master" not in JeanX.Petnames and "master" in JeanX.History:
#                            if "asked sub" in JeanX.RecentActions:
#                                    ch_j "I'm pretty sure we already covered that."
#                            elif "asked sub" in JeanX.DailyActions:
#                                    ch_j "Maybe later. . ."
#                            else:
#                                    call Jean_Sub_Asked
                    "Неважно":
                            pass

            "Неважно":
                return

    return

label Jean_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((JeanX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ JeanX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_j "Разве ты сейчас не с [Player.Harem[0].Name_tvo]?"
        ch_j "И, если я правильно все понимаю, не только с ней."
    else:
        ch_j "Разве ты сейчас не с [Player.Harem[0].Name_tvo]?"
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "JeanYes" in Player.Traits:
                if ApprovalCheck(JeanX, 1800, Bonus = Cnt):
                    $ JeanX.FaceChange("smile", 1)
                    if JeanX.Love >= JeanX.Obed:
                            ch_j "О, ну тогда ладно."
                    elif JeanX.Obed >= JeanX.Inbt:
                            if not Player.Male:
                                ch_j "Хмм. Уже все уладила."
                            else:
                                ch_j "Хмм. Уже все уладил."
                    else:
                            ch_j "О, здорово."
                else:
                    $ JeanX.FaceChange("smile", 1)
                    ch_j "Ха, ей нравятся куколды."
                    #$ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return, disabled on Jean

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "JeanYes" not in Player.Traits and not Player.Male:
                if ApprovalCheck(JeanX, 1800, Bonus = Cnt):
                        $ JeanX.FaceChange("smile", 1)
                        if JeanX.Love >= JeanX.Obed:
                            ch_j "Наверное, это неплохая идея."
                        elif JeanX.Obed >= JeanX.Inbt:
                            ch_j "Угу. . ."
                        else:
                            ch_j "Бла-бла-бла."
                        ch_j "Хорошо, спроси ее, передашь мне ее ответ утром."
                else:
                        $ JeanX.FaceChange("smile", 1)
                        ch_j "Ха, готова поспорить, она согласится. . ."
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "JeanYes" not in Player.Traits and Player.Male:
                if ApprovalCheck(JeanX, 1800, Bonus = Cnt):
                        $ JeanX.FaceChange("smile", 1)
                        if JeanX.Love >= JeanX.Obed:
                            ch_j "Наверное, это неплохая идея."
                        elif JeanX.Obed >= JeanX.Inbt:
                            ch_j "Угу. . ."
                        else:
                            ch_j "Бла-бла-бла."
                        ch_j "Хорошо, спроси ее, передашь мне ее ответ утром."
                else:
                        $ JeanX.FaceChange("smile", 1)
                        ch_j "Ха, готова поспорить, она согласится. . ."
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
#                if not ApprovalCheck(JeanX, 1800, Bonus = -Cnt): #checks if Jean likes you more than the other girl
#                        $ JeanX.FaceChange("angry", 1)
#                        if not ApprovalCheck(JeanX, 1800):
#                                ch_j "Well it'd hurt me."
#                        else:
#                                ch_j "I don't like the sound of that."
#                        $ renpy.pop_call()
#                else:
                        $ JeanX.FaceChange("smile", 1)
                        if JeanX.Love >= JeanX.Obed:
                                ch_j "Верно. . ."
                        elif JeanX.Obed >= JeanX.Inbt:
                                ch_j "Хмм. . ."
                        else:
                                ch_j "Ха, верно."
                        $ JeanX.Traits.append("downlow")

        "Я могу порвать с ней.":
                    $ JeanX.FaceChange("sad")
                    ch_j "Ага, давай."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ JeanX.FaceChange("sad")
                    ch_j "Точно."
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ JeanX.FaceChange("sad")
                    ch_j "Точно."
                    $ renpy.pop_call()

    return


label Jean_About(Check=0): #rkeljsvg
    if Check not in TotalGirls:
            ch_j "Это кто?"
            return
    ch_j "Что я думаю о [Check.Name_pre]? Хм. . ."
    if Check == RogueX:
            if "poly Rogue" in JeanX.Traits:
                ch_j "Хочу отметить, из нее хороший любовник. . ."
            elif JeanX.LikeRogue >= 900:
                ch_j "Она очень сексуальная. . ."
            elif JeanX.LikeRogue >= 800:
                ch_j "Не знаю, она нормальная. . ."
            elif JeanX.LikeRogue >= 700:
                ch_j "Она хороша в учебе или что-то вроде того?"
            elif JeanX.LikeRogue >= 600:
                ch_j "Она везучая, так?"
            elif JeanX.LikeRogue >= 500:
                ch_j "Это кто?"
            elif JeanX.LikeRogue >= 400:
                ch_j "Я никогда не думаю о ней."
            elif JeanX.LikeRogue >= 300:
                ch_j "Да пошла она к черту."
            else:
                ch_j "Она сучка."
    elif Check == KittyX:
            if "poly Kitty" in JeanX.Traits:
                ch_j "Хочу отметить, из нее хороший любовник. . ."
            elif JeanX.LikeKitty >= 900:
                ch_j "Она очень милая. . ."
            elif JeanX.LikeKitty >= 800:
                ch_j "Не знаю, она нормальная. . ."
            elif JeanX.LikeKitty >= 700:
                ch_j "Она, эм, спортсменка или что-то типа того?"
            elif JeanX.LikeKitty >= 600:
                ch_j "У нее еще такие маленькие сиськи, да? Девочка-призрак?"
            elif JeanX.LikeKitty >= 500:
                ch_j "Это кто?"
            elif JeanX.LikeKitty >= 400:
                ch_j "Я никогда не думаю о ней."
            elif JeanX.LikeKitty >= 300:
                ch_j "Да пошла она к черту."
            else:
                ch_j "Она сучка."
    elif Check == EmmaX:
            if "poly Emma" in JeanX.Traits:
                ch_j "Хочу отметить, она потрясающая любовница. . ."
            elif JeanX.LikeEmma >= 900:
                ch_j "У нее хорошие формы. . ."
            elif JeanX.LikeEmma >= 800:
                ch_j "Не знаю, она нормальная. . ."
            elif JeanX.LikeEmma >= 700:
                ch_j "Она очень сексуальная, для старушки."
            elif JeanX.LikeEmma >= 600:
                ch_j "Она ведь преподаватель, да?"
            elif JeanX.LikeEmma >= 500:
                ch_j "Это кто? А, она преподаватель, верно?"
            elif JeanX.LikeEmma >= 400:
                ch_j "Я бы хотела, чтобы она обращала на меня меньше внимания."
            elif JeanX.LikeEmma >= 300:
                ch_j "Ей не стоит лезть в чужие дела."
            else:
                ch_j "Грррр."
    elif Check == LauraX:
            if "poly Laura" in JeanX.Traits:
                ch_j "Хочу отметить, из нее хороший любовник. . ."
            elif JeanX.LikeLaura >= 900:
                ch_j "Она очень подтянутая. . ."
            elif JeanX.LikeLaura >= 800:
                ch_j "Не знаю, она нормальная. . ."
            elif JeanX.LikeLaura >= 700:
                ch_j "Она хороша в учебе или что-то вроде того?"
            elif JeanX.LikeLaura >= 600:
                ch_j "Эта которая с когтями, да?"
            elif JeanX.LikeLaura >= 500:
                ch_j "Это кто?"
            elif JeanX.LikeLaura >= 400:
                ch_j "Я никогда не думала о ней."
            elif JeanX.LikeLaura >= 300:
                ch_j "Да пошла она к черту."
            else:
                ch_j "Она сучка."
    elif Check == StormX:
            if "poly Storm" in JeanX.Traits:
                ch_j "Она такая мягонькая!"
            elif JeanX.LikeStorm >= 900:
                ch_j "Она. . . горяча."
            elif JeanX.LikeStorm >= 800:
                ch_j "Не знаю, она нормальная. . ."
            elif JeanX.LikeStorm >= 700:
                ch_j "Она очень сексуальная, для старушки."
            elif JeanX.LikeStorm >= 600:
                ch_j "Она ведь преподаватель, да?"
            elif JeanX.LikeStorm >= 500:
                ch_j "Это кто? А, она преподаватель, верно?"
            elif JeanX.LikeStorm >= 400:
                ch_j "Я бы хотела, чтобы она обращала на меня меньше внимания."
            elif JeanX.LikeStorm >= 300:
                ch_j "Ей не стоит лезть в чужие дела."
            else:
                ch_j "Грррр."
    elif Check == JubesX:
            if "poly Jubes" in JeanX.Traits:
                ch_j "Хочу отметить, из нее хороший любовник. . ."
            elif JeanX.LikeJubes >= 900:
                ch_j "Она очень милая. . ."
            elif JeanX.LikeJubes >= 800:
                ch_j "Не знаю, она нормальная. . ."
            elif JeanX.LikeJubes >= 700:
                ch_j "Мне кажется, я ее где-то видела. . ."
            elif JeanX.LikeJubes >= 600:
                ch_j "Она же вампир, да?"
            elif JeanX.LikeJubes >= 500:
                ch_j "Это кто?"
            elif JeanX.LikeJubes >= 400:
                ch_j "Я никогда не думаю о ней."
            elif JeanX.LikeJubes >= 300:
                ch_j "Ее стоит проткнуть колом."
            else:
                ch_j "Она сучка."
    elif Check == GwenX:
            if "poly Gwen" in JeanX.Traits:
                ch_j "Хочу отметить, из нее хороший любовник. . ."
            elif JeanX.LikeGwen >= 900:
                ch_j "Она очень милая. . ."
            elif JeanX.LikeGwen >= 800:
                ch_j "Не знаю, она нормальная. . ."
            elif JeanX.LikeGwen >= 700:
                ch_j "Она, эм, где-то тут?"
            elif JeanX.LikeGwen >= 600:
                ch_j "Это она так сильно любит. . . розовый?"
            elif JeanX.LikeGwen >= 500:
                ch_j "Это кто?"
            elif JeanX.LikeGwen >= 400:
                ch_j "Я никогда не думала о ней."
            elif JeanX.LikeGwen >= 300:
                ch_j "Да пошла она к черту."
            else:
                ch_j "Она сучка."
    elif Check == BetsyX:
            if "poly Betsy" in JeanX.Traits:
                ch_j "Хочу отметить, из нее хороший любовник. . ."
            elif JeanX.LikeBetsy >= 900:
                ch_j "Она очень сексуальная. . ."
            elif JeanX.LikeBetsy >= 800:
                ch_j "Не знаю, она нормальная. . ."
            elif JeanX.LikeBetsy >= 700:
                ch_j "Это которая, эм, австрийка или типа того?"
            elif JeanX.LikeBetsy >= 600:
                ch_j "Это у которой фиолетовые волосы, да?"
            elif JeanX.LikeBetsy >= 500:
                ch_j "Кто это?"
            elif JeanX.LikeBetsy >= 400:
                ch_j "Я никогда не думала о ней."
            elif JeanX.LikeBetsy >= 300:
                ch_j "Да пошла она к черту."
            else:
                ch_j "Она сучка."
    elif Check == DoreenX:
            if "poly Doreen" in JeanX.Traits:
                ch_j "Хочу отметить, из нее хороший любовник. . ."
            elif JeanX.LikeDoreen >= 900:
                ch_j "Она очень милая. . ."
            elif JeanX.LikeDoreen >= 800:
                ch_j "Не знаю, она нормальная. . ."
            elif JeanX.LikeDoreen >= 700:
                ch_j "Она, эм, где-то тут?"
            elif JeanX.LikeDoreen >= 600:
                ch_j "Это она такая. . . кругленькая?"
            elif JeanX.LikeDoreen >= 500:
                ch_j "Кто это?"
            elif JeanX.LikeDoreen >= 400:
                ch_j "Я никогда не думала о ней."
            elif JeanX.LikeDoreen >= 300:
                ch_j "Да пошла она к черту."
            else:
                ch_j "Она сучка."
    elif Check == WandaX:
            if "poly Wanda" in JeanX.Traits:
                ch_j "Пожалуй, она довольно хороша в постели. . ."
            elif JeanX.LikeWanda >= 900:
                ch_j "Она довольно сексуальна. . ."
            elif JeanX.LikeWanda >= 800:
                ch_j "Я не уверена, но думаю, она нормальная. . ."
            elif JeanX.LikeWanda >= 700:
                ch_j "Она хороша в учебе или типа того?"
            elif JeanX.LikeWanda >= 600:
                ch_j "Это ведь она \"еще одна рыжая,\" да?"
            elif JeanX.LikeWanda >= 500:
                ch_j "Это кто?"
            elif JeanX.LikeWanda >= 400:
                ch_j "Я никогда не думала о ней."
            elif JeanX.LikeWanda >= 300:
                ch_j "Чтоб ее черти отжарили."
            else:
                ch_j "Она ведьма."
    else:
                ch_j "Это тебя не касается."
    return
#End Jean_AboutEmma

label Jean_Monogamy:  #rkelj
        #called from Jean_Settings to ask her not to hook up with other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in JeanX.Traits:
                    if JeanX.Thirst >= 60 and not ApprovalCheck(JeanX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ JeanX.FaceChange("sly",1)
                            if "mono" not in JeanX.DailyActions:
                                    $ JeanX.Statup("Obed", 90, -2)
                            ch_j "Извини, это не входит в мои планы."
                            return
                    elif ApprovalCheck(JeanX, 1200, "LO", TabM=0) and JeanX.Love >= JeanX.Obed:
                            #she cares
                            $ JeanX.FaceChange("sly",1)
                            if "mono" not in JeanX.DailyActions:
                                    $ JeanX.Statup("Love", 90, 1)
                            ch_j "О, ревнуешь?"
                            if not Player.Male:
                                ch_j "Ладно, хорошо, но ты будешь должна. . ."
                            else:
                                ch_j "Ладно, хорошо, но ты будешь должен. . ."
                    elif ApprovalCheck(JeanX, 700, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side")
                            ch_j "Ну. . . ладно."
                    else:
                            #she doesn't care
                            $ JeanX.FaceChange("sly",1)
                            ch_j "Ха!"
                            return
                    if "mono" not in JeanX.DailyActions:
                            $ JeanX.Statup("Obed", 90, 3)
                    $ JeanX.AddWord(1,0,"mono") #Daily
                    $ JeanX.Traits.append("mono")
            "Не встречайся с другими девушками." if "mono" not in JeanX.Traits:
                    if ApprovalCheck(JeanX, 900, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side")
                            ch_j "Ну. . . ладно."
                    elif JeanX.Thirst >= 60 and not ApprovalCheck(JeanX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ JeanX.FaceChange("sly",1)
                            if "mono" not in JeanX.DailyActions:
                                    $ JeanX.Statup("Obed", 90, -2)
                            ch_j "Извини, это не входит в мои планы."
                            return
                    elif ApprovalCheck(JeanX, 600, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side")
                            ch_j "Ну. . . ладно."
                    elif ApprovalCheck(JeanX, 1400, "LO", TabM=0):
                            #she cares
                            $ JeanX.FaceChange("sly",1)
                            ch_j "О, ревнуешь?"
                            if not Player.Male:
                                ch_j "Ладно, хорошо, но ты будешь должна. . ."
                            else:
                                ch_j "Ладно, хорошо, но ты будешь должен. . ."
                    else:
                            #she doesn't care
                            $ JeanX.FaceChange("sly",1,Brows="confused")
                            ch_j "Ха!"
                            return
                    if "mono" not in JeanX.DailyActions:
                            $ JeanX.Statup("Obed", 90, 3)
                    $ JeanX.AddWord(1,0,"mono") #Daily
                    $ JeanX.Traits.append("mono")
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in JeanX.Traits:
                    if ApprovalCheck(JeanX, 700, "O", TabM=0):
                            $ JeanX.FaceChange("sly",1,Eyes="side")
                            ch_j ". . . хорошо."
                    elif ApprovalCheck(JeanX, 800, "L", TabM=0):
                            $ JeanX.FaceChange("sly",1)
                            ch_j "Ладно. . ."
                    else:
                            $ JeanX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in JeanX.DailyActions:
                                    $ JeanX.Statup("Love", 90, -2)
                            ch_j "Приятно знать. . ."
                    if "mono" not in JeanX.DailyActions:
                            $ JeanX.Statup("Obed", 90, 3)
                    if "mono" in JeanX.Traits:
                            $ JeanX.Traits.remove("mono")
                    $ JeanX.AddWord(1,0,"mono") #Daily
            "Неважно.":
                pass
        return

# end Jean monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Jean_Jumped: #rkelj
        #called from Jean_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ JeanX.FaceChange("sly",1,Brows="confused")
        ch_j "Я бы сказала это подругому, но. . . да?"
        menu:
            ch_j ". . . да?"
            "На будущее, можешь сначала спрашивать?" if "chill" not in JeanX.Traits:
                    if JeanX.Thirst >= 60 and not ApprovalCheck(JeanX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ JeanX.FaceChange("sly",1)
                            if "chill" not in JeanX.DailyActions:
                                    $ JeanX.Statup("Obed", 90, -2)
                            ch_j "Зачем тратить время?"
                            ch_j "В этом случае ты не скажешь \"нет.\""
                            return
                    elif ApprovalCheck(JeanX, 1000, "LO", TabM=0) and JeanX.Love >= JeanX.Obed:
                            #she cares
                            $ JeanX.FaceChange("surprised",1)
                            if "chill" not in JeanX.DailyActions:
                                    $ JeanX.Statup("Love", 90, 1)
                            ch_j "Тогда я была очень возбуждена. . ."
                            $ JeanX.FaceChange("sly",1,Eyes="side")
                            ch_j "Я подумаю. . ."
                    elif ApprovalCheck(JeanX, 500, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side")
                            ch_j "Может быть. . ."
                    else:
                            #she doesn't care
                            $ JeanX.FaceChange("sly",1)
                            ch_j "Зачем тратить время?"
                            ch_j "В этом случае ты не скажешь \"нет.\""
                            return
                    if "chill" not in JeanX.DailyActions:
                            $ JeanX.Statup("Obed", 90, 3)
                    $ JeanX.AddWord(1,0,"chill") #Daily
                    $ JeanX.Traits.append("chill")
            "Больше так не делай." if "chill" not in JeanX.Traits:
                    if ApprovalCheck(JeanX, 800, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side")
                            ch_j ". . . хорошо. . ."
                    elif JeanX.Thirst >= 60 and not ApprovalCheck(JeanX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ JeanX.FaceChange("sly",1)
                            if "chill" not in JeanX.DailyActions:
                                    $ JeanX.Statup("Obed", 90, -2)
                            ch_j "Зачем тратить время?"
                            ch_j "В этом случае ты не скажешь \"нет.\""
                            return
                    elif ApprovalCheck(JeanX, 400, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side")
                            ch_j "Ну. . . ладно. . ."
                    elif ApprovalCheck(JeanX, 500, "LO", TabM=0) and not ApprovalCheck(JeanX, 500, "I", TabM=0):
                            #she cares
                            $ JeanX.FaceChange("sly",1)
                            ch_j "Фи."
                            ch_j "Ладно, думаю, я могу попробовать. . ."
                    else:
                            #she doesn't care
                            $ JeanX.FaceChange("sly",1)
                            ch_j "Зачем тратить время?"
                            ch_j "В этом случае ты не скажешь \"нет.\""
                            return
                    if "chill" not in JeanX.DailyActions:
                            $ JeanX.Statup("Obed", 90, 3)
                    $ JeanX.AddWord(1,0,"chill") #Daily
                    $ JeanX.Traits.append("chill")
            "Делай что хочешь.":
                    if ApprovalCheck(JeanX, 800, "L", TabM=0):
                            $ JeanX.FaceChange("sly",1)
                            ch_j "Ха, думаю, ты знаешь, чего я хочу. . ."
                    elif ApprovalCheck(JeanX, 700, "O", TabM=0):
                            $ JeanX.FaceChange("sly",1,Eyes="side")
                            ch_j "Приятно знать."
                    else:
                            $ JeanX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in JeanX.DailyActions:
                                    $ JeanX.Statup("Love", 90, -2)
                            ch_j "Посмотрим. . ."
                    if "chill" not in JeanX.DailyActions:
                            $ JeanX.Statup("Obed", 90, 3)
                    if "chill" in JeanX.Traits:
                            $ JeanX.Traits.remove("chill")
                    $ JeanX.AddWord(1,0,"chill") #Daily
            "Эм, неважно.":
                pass
        return

# end Jean jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start laura hungry //////////////////////////////////////////////////////////
label Jean_Hungry: #rkelj
    if JeanX.Chat[3]:
        ch_j "Слушай, дай мне попробовать. . ."
    elif JeanX.Chat[2]:
        ch_j "Слушай, мне бы не помешало немного этой твоей. . . сыворотки. . ."
    else:
        ch_j "Мне очень нравится. . . твой вкус. . ."
    $ JeanX.Traits.append("hungry")
return


# end laura hungry //////////////////////////////////////////////////////////

# Jean Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Jean_SexChat: #rkelj
    $ Line = "Ага, о чем ты хочешь поговорить?" if not Line else Line
    while True:
            menu:
                ch_j "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in JeanX.DailyActions:
                        ch_j "Я помню."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "sex":
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Ага, я знаю. . ."
                                        elif JeanX.Favorite == "sex":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 10)
                                            ch_j "Мне тоже очень нравится!"
                                        elif JeanX.Sex >= 5:
                                            ch_j "Я не против."
                                        elif not JeanX.Sex:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "О? И с кем?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Ха, эм. . . да, это приятно. . ."
                                        $ JeanX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "anal":
                                            $ JeanX.Statup("Lust", 80, 5)
                                            if not Player.Male:
                                                ch_j "Ты уже говорила. . ."
                                            else:
                                                ch_j "Ты уже говорил. . ."
                                        elif JeanX.Favorite == "anal":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 10)
                                            ch_j "Мне тоже нравится!"
                                        elif JeanX.Anal >= 10:
                                            ch_j "Ага, это. . . приятно. . ."
                                        elif not JeanX.Anal:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "О? И с кем?"
                                        else:
                                            $ JeanX.FaceChange("bemused",Eyes="side")
                                            ch_j "Ха, ага. . . эм, я не против. . ."
                                        $ JeanX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "blow":
                                            $ JeanX.Statup("Lust", 80, 3)
                                            ch_j "Ага, я знаю."
                                        elif JeanX.Favorite == "blow":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Не могу сказать, что мне не нравится. . ."
                                        elif JeanX.Blow >= 10:
                                            ch_j "Ага, ты на удивление вкусный."
                                        elif not JeanX.Blow:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "О? И с кем?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Тебе повезло, что ты такой вкусный."
                                        $ JeanX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "cun":
                                            $ JeanX.Statup("Lust", 80, 3)
                                            ch_j "Ага, я знаю."
                                        elif JeanX.Favorite == "cun":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Не могу сказать, что мне не нравится. . ."
                                        elif JeanX.CUN >= 10:
                                            ch_j "Ага, ты на удивление вкусная."
                                        elif not JeanX.CUN:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "О? И с кем?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Тебе повезло, что ты такая вкусная."
                                        $ JeanX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "titjob":
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Ага, мы уже это обсуждали. . ."
                                        elif JeanX.Favorite == "titjob":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 7)
                                            ch_j "Ага, мне тоже нравится. . ."
                                        elif JeanX.Tit >= 10:
                                            ch_j "Приятно, да?"
                                        elif not JeanX.Tit:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "О? И с кем?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Еще бы, они ведь идеальны. . ."
                                            $ JeanX.Statup("Love", 80, 5)
                                            $ JeanX.Statup("Inbt", 50, 10)
                                        $ JeanX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "foot":
                                            $ JeanX.Statup("Lust", 80, 5)
                                            if not Player.Male:
                                                ch_j "Ага, ты уже говорила. . ."
                                            else:
                                                ch_j "Ага, ты уже говорил. . ."
                                        elif JeanX.Favorite == "foot":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 7)
                                            ch_j "Мне нравится использовать свои ножки. . ."
                                        elif JeanX.Foot >= 10:
                                            ch_j "Мне тоже нравится . . ."
                                        elif not JeanX.Foot:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "О? И с кем?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Ага, это приятно. . ."
                                        $ JeanX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "hand":
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Ага, ты уже говорил. . ."
                                        elif JeanX.Favorite == "hand":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 7)
                                            ch_j "Да, я неплохо работаю рукой. . ."
                                        elif JeanX.Hand >= 10:
                                            ch_j "Мне тоже нравится. . ."
                                        elif not JeanX.Hand:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "О? И с кем?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Ага, это приятно. . ."
                                        $ JeanX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "finger":
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Ага, ты уже говорила. . ."
                                        elif JeanX.Favorite == "finger":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 7)
                                            ch_j "Да, я неплохо работаю пальчиками. . ."
                                        elif JeanX.Finger >= 10:
                                            ch_j "Мне тоже нравится. . ."
                                        elif not JeanX.Finger:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "О? И с кем?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Ага, это приятно. . ."
                                        $ JeanX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = JeanX.FondleB + JeanX.FondleT + JeanX.SuckB + JeanX.Hotdog
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "fondle":
                                            $ JeanX.Statup("Lust", 80, 3)
                                            ch_j "Ага, я уже в курсе. . ."
                                        elif JeanX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Мне нравится, когда ты прикасаешься ко мне. . ."
                                        elif Cnt >= 10:
                                            ch_j "Ага, это очень приятно . . ."
                                        elif not Cnt:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "О? И с кем?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Мне нравятся эти ощущения. . ."
                                        $ JeanX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "kiss you":
                                            $ JeanX.Statup("Love", 90, 3)
                                            ch_j "Зануда. . ."
                                        elif JeanX.Favorite == "kiss you":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Мне. . . тоже? . ."
                                        elif JeanX.Kissed >= 10:
                                            ch_j "Ага, это весело . . ."
                                        elif not JeanX.Kissed:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "О? И с кем?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Мне тоже. . ."
                                        $ JeanX.PlayerFav = "kiss you"

                        $ JeanX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(JeanX, 800):
                                        $ JeanX.FaceChange("perplexed")
                                        ch_j ". . ."
                                else:
                                        if JeanX.SEXP >= 50:
                                            $ JeanX.FaceChange("perplexed")
                                            if not Player.Male:
                                                ch_j "Ты уже должна знать. . ."
                                            else:
                                                ch_j "Ты уже должен знать. . ."
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            $ JeanX.Eyes = "side"
                                            ch_j "Хмм. . ."


                                        if not JeanX.Favorite or JeanX.Favorite == "kiss you":
                                            ch_j "Поцелуи?"
                                        elif JeanX.Favorite == "anal":
                                                ch_j "Наверное, анал."
                                        elif JeanX.Favorite == "lick ass":
                                                ch_j "Когда ты вылизаешь мою попку."
                                        elif JeanX.Favorite == "insert ass":
                                                ch_j "Наверное, когда ты засовываешь палец мне в попку."
                                        elif JeanX.Favorite == "sex":
                                                ch_j "Когда ты меня трахаешь."
                                        elif JeanX.Favorite == "lick pussy":
                                                ch_j "Когда ты вылизываешь мою киску."
                                        elif JeanX.Favorite == "fondle pussy":
                                                ch_j "Когда ты трахаешь меня пальцем."
                                        elif JeanX.Favorite == "blow":
                                                ch_j "Мне нравится вкус твоего члена. . ."
                                        elif JeanX.Favorite == "cun":
                                                ch_j "Мне нравится вкус твоей киски. . ."
                                        elif JeanX.Favorite == "tit":
                                                ch_j "Когда я использую свою грудь."
                                        elif JeanX.Favorite == "foot":
                                                ch_j "Дрочить ногами очень весело."
                                        elif JeanX.Favorite == "hand":
                                                ch_j "Мне нравится дрочить тебе рукой."
                                        elif JeanX.Favorite == "finger":
                                                ch_j "Мне нравится ласкать твою киску."
                                        elif JeanX.Favorite == "hotdog":
                                                ch_j "Когда ты трешься о меня."
                                        elif JeanX.Favorite == "suck breasts":
                                                ch_j "Когда ты сосешь мою грудь."
                                        elif JeanX.Favorite == "fondle breasts":
                                                ch_j "Когда ты массируешь мою грудь."
                                        elif JeanX.Favorite == "fondle thighs":
                                                ch_j "Когда ты массируешь мои ножки."
                                        else:
                                                ch_j "Я не знаю, удиви меня."

                                # End Jean's favorite things.

                "Не болтай так много во время секса." if "vocal" in JeanX.Traits:
                        if "setvocal" in JeanX.DailyActions:
                                $ JeanX.FaceChange("perplexed")
                                ch_j "Не морочь мне голову, [JeanX.Petname]."
                        else:
                            if ApprovalCheck(JeanX, 1000) and JeanX.Obed <= JeanX.Love:
                                $ JeanX.FaceChange("bemused")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j ". . . ладно."
                                $ JeanX.Traits.remove("vocal")
                            elif ApprovalCheck(JeanX, 700, "O"):
                                $ JeanX.FaceChange("sadside")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j ". . ."
                                $ JeanX.Traits.remove("vocal")
                            elif ApprovalCheck(JeanX, 600):
                                $ JeanX.FaceChange("sly")
                                $ JeanX.Statup("Love", 90, -3)
                                $ JeanX.Statup("Obed", 50, -1)
                                $ JeanX.Statup("Inbt", 90, 5)
                                ch_j "Ох, я буду болтать, а тебе придется слушать, [JeanX.Petname]."
                            else:
                                $ JeanX.FaceChange("angry")
                                $ JeanX.Statup("Love", 90, -5)
                                $ JeanX.Statup("Obed", 60, -3)
                                $ JeanX.Statup("Inbt", 90, 10)
                                ch_j "Ага, когда-нибудь наступит этот день. . ."

                            $ JeanX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in JeanX.Traits:
                        if "setvocal" in JeanX.DailyActions:
                                $ JeanX.FaceChange("perplexed")
                                ch_j "Не морочь мне голову, [JeanX.Petname]."
                        else:
                            if ApprovalCheck(JeanX, 1000) and JeanX.Obed <= JeanX.Love:
                                $ JeanX.FaceChange("sly")
                                $ JeanX.Statup("Obed", 90, 2)
                                ch_j "Думаю, можно. . ."
                                $ JeanX.Traits.append("vocal")
                            elif ApprovalCheck(JeanX, 700, "O"):
                                $ JeanX.FaceChange("sadside")
                                $ JeanX.Statup("Obed", 90, 2)
                                ch_j "Будет сделано, [JeanX.Petname]."
                                $ JeanX.Traits.append("vocal")
                            elif ApprovalCheck(JeanX, 600):
                                $ JeanX.FaceChange("sly")
                                $ JeanX.Statup("Obed", 90, 3)
                                ch_j "Конечно, как скажешь."
                                $ JeanX.Traits.append("vocal")
                            else:
                                $ JeanX.FaceChange("angry")
                                $ JeanX.Statup("Inbt", 90, 5)
                                ch_j ". . ."

                            $ JeanX.DailyActions.append("setvocal")
                        # End Jean Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in JeanX.Traits:
                        if "initiative" in JeanX.DailyActions:
                                $ JeanX.FaceChange("perplexed")
                                ch_j "Не морочь мне голову, [JeanX.Petname]."
                        else:
                            if ApprovalCheck(JeanX, 1200) and JeanX.Obed <= JeanX.Love:
                                $ JeanX.FaceChange("bemused")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j "Стать \"пассивной?\" Посмотрим, что можно сделать. . ."
                                $ JeanX.Traits.append("passive")
                            elif ApprovalCheck(JeanX, 700, "O"):
                                $ JeanX.FaceChange("sadside")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j ". . . ага, ладно. . ."
                                $ JeanX.Traits.append("passive")
                            elif ApprovalCheck(JeanX, 600):
                                $ JeanX.FaceChange("sly")
                                $ JeanX.Statup("Love", 90, -3)
                                $ JeanX.Statup("Obed", 50, -1)
                                $ JeanX.Statup("Inbt", 90, 5)
                                ch_j "Хм, -НЕТ.-"
                            else:
                                $ JeanX.FaceChange("angry")
                                $ JeanX.Statup("Love", 90, -5)
                                $ JeanX.Statup("Obed", 60, -3)
                                $ JeanX.Statup("Inbt", 90, 10)
                                ch_j "Это твои проблемы."

                            $ JeanX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in JeanX.Traits:
                        if "initiative" in JeanX.DailyActions:
                                $ JeanX.FaceChange("perplexed")
                                ch_j "Не морочь мне голову, [JeanX.Petname]."
                        else:
                            if ApprovalCheck(JeanX, 1000) and JeanX.Obed <= JeanX.Love:
                                $ JeanX.FaceChange("bemused")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j "Черт возьми, я обеими руками за."
                                $ JeanX.Traits.remove("passive")
                            elif ApprovalCheck(JeanX, 700, "O"):
                                $ JeanX.FaceChange("sadside")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j ". . . хорошо. . ."
                                $ JeanX.Traits.remove("passive")
                            elif ApprovalCheck(JeanX, 600):
                                $ JeanX.FaceChange("sly")
                                $ JeanX.Statup("Obed", 90, 3)
                                ch_j "Конечно."
                                $ JeanX.Traits.remove("passive")
                            else:
                                $ JeanX.FaceChange("angry")
                                $ JeanX.Statup("Inbt", 90, 5)
                                ch_j "Пфф, не приставай ко мне."

                            $ JeanX.DailyActions.append("initiative")

                "О том, как ты накидываешься" if "jumped" in JeanX.History:
                        call Jean_Jumped

                "О \"изоляции разума\"" if "screen" in JeanX.Traits or "noscreen" in JeanX.Traits:
                        ch_j "Ты про то, что я могу иногда блокировать Чака?"
                        menu:
                            extend ""
                            "Ага, делай это." if "noscreen" in JeanX.Traits:
                                ch_j "Хорошо. . ."
                                $ JeanX.Traits.append("screen")
                                $ JeanX.Traits.remove("noscreen")
                            "Не делай этого больше, я хочу, чтобы он знал." if "screen" in JeanX.Traits:
                                ch_j "Как непристойно. . ."
                                if ApprovalCheck(JeanX, 900, "OI"):
                                        $ JeanX.FaceChange("sad")
                                        ch_j "Хорошо, не буду."
                                        $ JeanX.FaceChange("bemused")
                                        $ JeanX.Traits.append("noscreen")
                                        $ JeanX.Traits.remove("screen")
                                else:
                                        ch_j "И все же, мне не нравится, что он может побеспокоить нас."
                                        ch_j "Я все равно буду блокировать его."
                            "Неважно.":
                                pass
                #end mental screen talk

                "О \"стирание памяти\"" if "whammy" in JeanX.Traits or "nowhammy" in JeanX.Traits:
                        ch_j "Ты про то, что я могу стирать память других студентов, чтобы они не знали, что я творю?"
                        menu:
                            extend ""
                            "И это круто":
                                if "whammytalk" not in JeanX.Chat:
                                        $ JeanX.Statup("Love", 60, 10)
                                        $ JeanX.Statup("Love", 90, 5)
                                        $ JeanX.Statup("Obed", 60, 10)
                                        $ JeanX.Statup("Obed", 80, 5)
                                        $ JeanX.Statup("Inbt", 90, 10)
                                ch_j "Я знаю."
                                $ JeanX.Chat.append("whammytalk")
                            "Ага, думаю, стоит начать делать это снова." if "nowhammy" in JeanX.Traits:
                                ch_j "Ну, что ж. . ."
                                if "Alpha" not in Player.Traits:
                                            #you haven't done the Plan Alpha yet
                                            $ JeanX.FaceChange("sad")
                                            ch_j "Я бы тоже этого хотела, но Чак возьмет меня за хвост. . ."
                                elif ApprovalCheck(JeanX, 800, "I"):
                                    if "whammytalk" not in JeanX.DailyActions:
                                            $ JeanX.Statup("Love", 80, 10)
                                            $ JeanX.Statup("Obed", 60, 5)
                                            $ JeanX.Statup("Inbt", 90, 10)
                                    if not ApprovalCheck(JeanX, 800, "LO"):
                                            #she's sluttier than she likes you
                                            $ JeanX.FaceChange("sad")
                                            ch_j "Мне нравятся твои слова."
                                    else:
                                            #she's slutty but likes you enough to stop
                                            $ JeanX.FaceChange("sad")
                                            ch_j "Ладно. . ."
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Хотя, мне, вроде как, нравились острые ощущения. . ."
                                else:
                                            #she's not that slutty
                                            if "whammytalk" not in JeanX.DailyActions:
                                                    $ JeanX.Statup("Love", 90, 5)
                                                    $ JeanX.Statup("Obed", 60, 3)
                                            ch_j "Ладно, спасибо. . ."
                                            $ JeanX.Traits.append("whammy")
                                $ JeanX.DailyActions.append("whammytalk")
                            "Не делай этого больше, я хочу, чтобы они все помнили." if "whammy" in JeanX.Traits:
                                if "whammytalk" not in JeanX.DailyActions:
                                            $ JeanX.Statup("Obed", 60, 5)
                                            $ JeanX.Statup("Obed", 85, 5)
                                            $ JeanX.Statup("Inbt", 90, 10)
                                ch_j "Ну, что ж. . ."
                                if ApprovalCheck(JeanX, 1500):
                                            $ JeanX.FaceChange("sad")
                                            ch_j "Ладно, думаю, с этим я справлюсь. . ."
                                            $ JeanX.Traits.append("nowhammy")
                                else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "У меня для тебя плохие новости. . ."
                                $ JeanX.DailyActions.append("whammytalk")
                            "Неважно.":
                                pass
                #end Whammy talk

                "О твоей мастурбации":
                    call NoFap(JeanX)

                "Всегда носи вибратор" if "dailyvibe" not in JeanX.Traits:
                        call Daily_Vibrator(JeanX)
                "Перестань всегда носить вибратор" if "dailyvibe" in JeanX.Traits:
                        ch_j "Ладно. . ."
                        $ JeanX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи анальную пробку" if "dailyplug" not in JeanX.Traits:
                        call Daily_Plug(JeanX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in JeanX.Traits:
                        ch_j "Ладно. . ."
                        $ JeanX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Неважно" if Line == "Ага, о чем ты хочешь поговорить?":
                        return
                "На этом все." if Line != "Ага, о чем ты хочешь поговорить?":
                        return
            if Line == "Ага, о чем ты хочешь поговорить?":
                $ Line = "Что-нибудь еще?"
    return
# End Jean Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Jean Chitchat /////////////////// #Work in progress
label Jean_Chitchat(O=0, Options = ["default","default","default"]): #rkel
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if JeanX not in Digits:
                if ApprovalCheck(JeanX, 500, "L") or ApprovalCheck(JeanX, 250, "I"):
                    ch_j "Вот мой номер, позвони мне как-нибудь."
                    $ Digits.append(JeanX)
                    return
                elif ApprovalCheck(JeanX, 250, "O"):
                    ch_j "Думаю, у тебя должен быть мой номер телефона. . ."
                    $ Digits.append(JeanX)
                    return

        if "hungry" not in JeanX.Traits and (JeanX.Swallow + JeanX.Chat[2]) >= 10 and JeanX.Loc == bg_current:  #She's swallowed a lot
                    call Jean_Hungry
                    return

        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(JeanX, 800, "I")):
                    if JeanX.Loc == bg_current and JeanX.Thirst >= 30 and "refused" not in JeanX.DailyActions and "quicksex" not in JeanX.DailyActions:
                            $ JeanX.FaceChange("sly",1)
                            if not Player.Male:
                                ch_j "Мне бы не помешала небольшая разрядка, ты сейчас не занята?"
                            else:
                                ch_j "Мне бы не помешала небольшая разрядка, ты сейчас не занят?"
                            call Quick_Sex(JeanX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
        if PunishmentX and "caught chat" not in JeanX.DailyActions:
            $ Options.append("caught")
        if JeanX.Event[0] and "key" not in JeanX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in JeanX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in JeanX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in JeanX.DailyActions:
            $ Options.append("corruption")

        if JeanX.Date >= 1 and bg_current != "bg restaurant":
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in JeanX.DailyActions and "cheek" not in JeanX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if JeanX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in JeanX.DailyActions and (Player.Male or "girltalk" in JeanX.History):
            #If you've caught Jean showering today
            $ Options.append("showercaught")
        if "fondle breasts" in JeanX.DailyActions or "fondle pussy" in JeanX.DailyActions or "fondle ass" in JeanX.DailyActions:
            #If you've fondled Jean today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in JeanX.Inventory and "256 Shades of Grey" in JeanX.Inventory and "Avengers Tower Penthouse" in JeanX.Inventory:
            #If you've given Jean the books
            if "book" not in JeanX.Chat:
                $ Options.append("booked")
        if "lace bra" in JeanX.Inventory or "lace panties" in JeanX.Inventory:
            #If you've given Jean the lingerie
            if "lingerie" not in JeanX.Chat:
                $ Options.append("lingerie")
        if "boyfriend" not in JeanX.Petnames and "lover" in JeanX.Petnames and JeanX in Player.Harem:
                $ JeanX.Petnames.append("boyfriend")
        if JeanX.Hand and Player.Male:
            #If Jean's given a handjob
            $ Options.append("handy")
        if JeanX.Blow and Player.Male:
            #If Jean's given a blowjob
            $ Options.append("blow")
        if JeanX.Swallow:
            #If Jean's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in JeanX.DailyActions or "painted" in JeanX.DailyActions:
            #If Jean's been facialed
            $ Options.append("facial")
        if JeanX.Sleep:
            #If Jean's slept over
            $ Options.append("sleep")
        if (JeanX.CreamP or JeanX.CreamA) and Player.Male:
            #If Jean's been creampied
            $ Options.append("creampie")
        if JeanX.Sex or JeanX.Anal:
            #If Jean's been sexed
            $ Options.append("sexed")
        if JeanX.Anal:
            #If Jean's been analed
            $ Options.append("anal")

        if "seenpeen" in JeanX.History and Player.Male:
            $ Options.append("seenpeen")
        if "topless" in JeanX.History:
            $ Options.append("topless")
        if "bottomless" in JeanX.History:
            $ Options.append("bottomless")

        if not ApprovalCheck(JeanX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ JeanX.DailyActions.append("cologne chat")
        $ JeanX.FaceChange("confused")
        if not Player.Male:
            ch_j "(нюх, нюх). . . ты трахнула Хэнка? . ."
        else:
            ch_j "(нюх, нюх). . . ты трахнул Хэнка? . ."
        $ JeanX.FaceChange("sexy", 2)
        ch_j ". . . Тем не менее, ты хорошо пахнешь. . ."
    elif Options[0] == "purple":
        $ JeanX.DailyActions.append("cologne chat")
        $ JeanX.FaceChange("sly",1)
        ch_j "(нюх, нюх). . . что это за запах? . ."
        $ JeanX.FaceChange("normal",0)
        if not Player.Male:
            ch_j ". . . ты чего то хотела?"
        else:
            ch_j ". . . ты чего то хотел?"
    elif Options[0] == "corruption":
        $ JeanX.DailyActions.append("cologne chat")
        $ JeanX.FaceChange("confused")
        ch_j "(нюх, нюх). . . какой сильный аромат. . ."
        $ JeanX.FaceChange("angry")
        ch_j ". . . опасный аромат. . ."
        $ JeanX.FaceChange("sly")

    elif Options[0] == "caught": # Xavier's caught you
            $ JeanX.FaceChange("angry")
            if "caught chat" in JeanX.Chat:
                    ch_j "Этот засранец Чак."
                    ch_j "Я устала, что он сует свой нос туда, куда не следует."
            else:
                    ch_j "Этот засранец Чак."
                    ch_j "Я устала, что он сует свой нос туда, куда не следует."
                    $ JeanX.FaceChange("surprised")
                    ch_j "О!"
                    $ JeanX.FaceChange("sly")
                    ch_j "У меня появилась идея."
                    ch_j "Я могу воспользоваться своими способностями, чтобы слегка подавить его силы. Думаю, это поможет нам укрыться от его \"взгляда\"."
                    menu:
                        "Я только за.":
                            ch_j "Замечательно. . ."
                            $ JeanX.Traits.append("screen")
                        "Нет, я хочу, чтобы он знал.":
                            if not Player.Male:
                                ch_j "Ха, ты такой развратница."
                            else:
                                ch_j "Ха, ты такой развратник."
                            if ApprovalCheck(JeanX, 900, "OI"):
                                    $ JeanX.FaceChange("sad")
                                    ch_j "Хорошо, мы не будем этого делать."
                                    $ JeanX.FaceChange("bemused")
                                    $ JeanX.Traits.append("noscreen")
                            else:
                                    ch_j "И все же, мне не нравится, что он сует свой нос в чужие дела."
                                    ch_j "Думаю, я все равно буду блокировать его."
                                    $ JeanX.Traits.append("screen")
                    $ JeanX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if JeanX.SEXP <= 15:
                ch_j "Не используй этот ключ слишком свободно. . ."
            else:
                ch_j "У тебя есть мой ключ, но ты редко заходишь. . ."
            $ JeanX.Chat.append("key")

#    elif Options[0] == "cheek":
#            #Jean's response to having her cheek touched.
#            ch_j "So,[JeanX.Petname]. . .y'know how you[JeanX.like]kinda just brushed my cheek before?"
#            ch_p "Yeah?  Was that okay?"
#            $ JeanX.FaceChange("smile",1)
#            ch_j "More than just {i}okay{/i}."
#            $ JeanX.Chat.append("cheek")

    elif Options[0] == "dated":
            #Jean's response to having gone on a date with the Player.
            ch_j "Мне было весело прошлой ночью, мы должны когда-нибудь повторить."

    elif Options[0] == "kissed":
            #Jean's response to having been kissed by the Player.
            $ JeanX.FaceChange("normal",1)
            ch_j "Хочу отметить, ты хорошо целуешься, [JeanX.Petname]."
            menu:
                extend ""
                "Эй. . . Да я лучшая." if not Player.Male:
                        $ JeanX.FaceChange("smile",1)
                        ch_j "Где-то я уже это слышала. . ."
                "Эй. . . Да я лучший." if Player.Male:
                        $ JeanX.FaceChange("smile",1)
                        ch_j "Где-то я уже это слышала. . ."
                "Ты правда так думаешь?":
                        ch_j "Будь иначе, я бы вообще этого не сказала."

    elif Options[0] == "dangerroom":
            #Jean's response to Player working out in the Danger Room while Jean is present
            $ JeanX.FaceChange("sly",1)
            ch_j "Знаешь, [JeanX.Petname], я видела, как ты тренируешься в комнате Опасности."
            if not Player.Male:
                ch_j "Ты на удивление хороша, для человека с такими. . . ограниченными возможностями."
            else:
                ch_j "Ты на удивление хорош, для человека с такими. . . ограниченными возможностями."

    elif Options[0] == "showercaught":
            #Jean's response to being caught in the shower.
            if "shower" in JeanX.Chat:
                ch_j "Я снова видела тебя в душевой. . ."
            else:
                ch_j "Ты всегда так просто врываешься в душевую?"
                $ JeanX.Chat.append("shower")
                menu:
                    extend ""
                    "Это чистая случайность! Клянусь!":
                            $ JeanX.Statup("Love", 50, 5)
                            $ JeanX.Statup("Love", 90, 2)
                            if ApprovalCheck(JeanX, 1200):
                                $ JeanX.FaceChange("sly",1)
                                ch_j "Ну, я не против."
                            $ JeanX.FaceChange("smile")
                            ch_j "Думаю, мы все способны ошибаться. . ."
                    "Только если там ты.":
                            $ JeanX.Statup("Obed", 40, 5)
                            if ApprovalCheck(JeanX, 1000) or ApprovalCheck(JeanX, 700, "L"):
                                    $ JeanX.Statup("Love", 90, 3)
                                    $ JeanX.FaceChange("sly",1)
                                    ch_j "О, прелестно. . ."
                            else:
                                    $ JeanX.Statup("Love", 70, -5)
                                    $ JeanX.FaceChange("angry")
                                    ch_j "Ну конечно. . ."
                    "Я заглянула умышленно. Но я ни о чем не жалею." if not Player.Male:
                            if ApprovalCheck(JeanX, 800):
                                    $ JeanX.Statup("Obed", 60, 5)
                                    $ JeanX.Statup("Inbt", 50, 5)
                                    $ JeanX.FaceChange("perplexed",2)
                                    h_j "Зато честно."
                                    $ JeanX.Blush = 1
                            else:
                                    $ JeanX.Statup("Love", 50, -10)
                                    $ JeanX.Statup("Love", 80, -10)
                                    $ JeanX.Statup("Obed", 50, 10)
                                    $ JeanX.FaceChange("angry")
                                    ch_j "Извращюга."
                    "Я заглянул умышленно. Но я ни о чем не жалею." if Player.Male:
                            if ApprovalCheck(JeanX, 800):
                                    $ JeanX.Statup("Obed", 60, 5)
                                    $ JeanX.Statup("Inbt", 50, 5)
                                    $ JeanX.FaceChange("perplexed",2)
                                    h_j "Зато честно."
                                    $ JeanX.Blush = 1
                            else:
                                    $ JeanX.Statup("Love", 50, -10)
                                    $ JeanX.Statup("Love", 80, -10)
                                    $ JeanX.Statup("Obed", 50, 10)
                                    $ JeanX.FaceChange("angry")
                                    ch_j "Извращюга."

    elif Options[0] == "fondled":
            #Jean's response to being felt up.
            if JeanX.FondleB + JeanX.FondleP + JeanX.FondleA >= 15:
                ch_j "Слушай, сделай мне хороший, жесткий массаж. . ."
            else:
                ch_j "Слушай, сделай мне еще раз массаж. . . "
                ch_j ". . . в лучшем виде. . ."

    elif Options[0] == "booked":
            #Jean's response after a Player gives her the books from the shop.
            if not Player.Male:
                ch_j "Знаешь, я прочитала те книги, что ты мне дала."
            else:
                ch_j "Знаешь, я прочитала те книги, что ты мне дал."
            menu:
                extend ""
                "Да? Они тебе понравились?":
                        $ JeanX.FaceChange("sly",2)
                        ch_j "Они были довольно пикантными."
                "Хорошо. Пожалуй, ты могла бы чему-нибудь из них научиться.":
                        $ JeanX.Statup("Obed", 70, 5)
                        $ JeanX.Statup("Inbt", 50, 5)
                        $ JeanX.FaceChange("angry")
                        ch_j "Ага, точно."
            $ JeanX.Blush = 1
            $ JeanX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Jean's response to being given lingerie.
            $ JeanX.FaceChange("sly",2)
            if not Player.Male:
                ch_j "Мне очень нравится то шелковое нижнее белье, что ты мне подарила. . ."
            else:
                ch_j "Мне очень нравится то шелковое нижнее белье, что ты мне подарил. . ."
            $ JeanX.Blush = 1
            $ JeanX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Jean's response after giving the Player a handjob.
            $ JeanX.FaceChange("sly",1)
            ch_j "Я вспоминала о твоем члене в своей руке. . ."
            ch_j "Думаю, мы должны заняться чем-то подобным снова. . ."
            $ JeanX.Blush = 0

    elif Options[0] == "blow":
            if "blow" not in JeanX.Chat:
                    #Jean's response after giving the Player a blowjob.
                    $ JeanX.FaceChange("sly",2)
                    ch_j "Слушай, тебе понравился минет?"
                    menu:
                        extend ""
                        "Ты была великолепна.":
                                    $ JeanX.Statup("Love", 90, 5)
                                    $ JeanX.Statup("Obed", 60, 15)
                                    $ JeanX.Statup("Inbt", 60, 10)
                                    $ JeanX.FaceChange("normal",1)
                                    ch_j "Знаешь. . ."
                                    $ JeanX.FaceChange("sexy",1)
                                    ch_j "Я не против попробовать еще раз. . ."
                        "Честно? Все было хорошо. . . но, думаю, тебе не помешает еще немного попрактиковаться.":
                                if ApprovalCheck(JeanX, 300, "I") or not ApprovalCheck(JeanX, 800):
                                    $ JeanX.Statup("Love", 90, -5)
                                    $ JeanX.Statup("Obed", 60, 10)
                                    $ JeanX.Statup("Inbt", 50, 10)
                                    $ JeanX.FaceChange("perplexed",1)
                                    ch_j "Серьезно? Раньше никто не жаловался. . ."
                                else:
                                    $ JeanX.Statup("Obed", 70, 15)
                                    $ JeanX.Statup("Inbt", 50, 5)
                                    $ JeanX.FaceChange("sexy",1)
                                    ch_j "Тебе просто не с чем сравнивать."
                        "Угу, если бы мне нравились стремные звуки и шкрябанье зубов по члену, но это далеко не так.":
                                $ JeanX.Statup("Love", 90, -10)
                                $ JeanX.Statup("Obed", 60, -5)
                                $ JeanX.FaceChange("angry",2)
                                ch_j "Ты просто ничего не понимаешь."
                    $ JeanX.Blush = 1
                    $ JeanX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["Должна сказать тебе, твой член на вкус великолепен.",
                            "Кажется, в прошлый раз я чуть не вывихнула челюсть.",
                            "Дай знать, если захочешь еще один минет.",
                            "Хммм. . . [стучит языком по внутренней стороне щеки.]"])
                    ch_j "[Line]"

    elif Options[0] == "swallowed":
            #Jean's response after swallowing the Player's cum.
            if "swallow" in JeanX.Chat:
                ch_j "Знаешь, я бы не отказалась попробовать еще раз. . ."
            else:
                ch_j "Знаешь. . . на днях. . ."
                if not Player.Male:
                    ch_j "Я оценила твои соки на вкус."
                    ch_j "Они -очень- хороши."
                else:
                    ch_j "Я оценила твою сперму на вкус."
                    ch_j "Она -очень- хороша."
                $ JeanX.FaceChange("sly",1)
                ch_j "Я приятно удивлена."
                $ JeanX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Jean's response after taking a facial from the Player.
            ch_j "Ладно, так вот. . ."
            if not Player.Male:
                ch_j "Помнишь, как кончила мне на лицо?"
            else:
                ch_j "Помнишь, как кончил мне на лицо?"
            $ JeanX.FaceChange("sexy",2)
            ch_j "По какой-то причине это было -очень- приятно. . ."
            $ JeanX.Blush = 1

    elif Options[0] == "sleepover":
            #Jean's response after sleeping with the Player.
            ch_j "Мне очень понравилась прошлая ночь."
            ch_j "Как и компания."

    elif Options[0] == "creampie":
            #Another of Jean's responses after having sex with the Player.
            "[JeanX.Name] подходит вплотную к вам и шепчет на ухо:"
            ch_j "Из меня все еще вытекает частичка тебя. . ."

    elif Options[0] == "sexed":
            #A final response from Jean after having sex with the Player.
            ch_j "Так. . . тебе следует знать. . ."
            $ JeanX.FaceChange("sexy",2)
            ch_j ". . .в последнее время, когда я мастурбирую. . ."
            ch_j "Я представляю, что ты внутри меня."
            $ JeanX.Blush = 1

    elif Options[0] == "anal":
            #Jean's response after getting anal from the Player.
            $ JeanX.FaceChange("sly")
            ch_j "Я не очень люблю анал."
            $ JeanX.FaceChange("sexy",1)
            ch_j "Но заниматься подобным с тобой довольно весело."

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ JeanX.FaceChange("sly",1, Eyes="down")
            ch_j "О, я забыла упомянуть, у тебя красивое хозяйство. . ."
            $ JeanX.FaceChange("bemused",1)
            $ JeanX.Statup("Love", 50, 5)
            $ JeanX.Statup("Love", 60, 10)
            $ JeanX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            if not Player.Male:
                ch_j "Так что, ты хорошо рассмотрела мои сиськи? Очень красивые, правда?"
            else:
                ch_j "Так что, ты хорошо рассмотрел мои сиськи? Очень красивые, правда?"
            call Girl_First_TMenu
            $ JeanX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            if not Player.Male:
                ch_j "Так что, ты хорошо рассмотрела мою киску? Она милая, правда?"
            else:
                ch_j "Так что, ты хорошо рассмотрел мою киску? Она милая, правда?"
            call Girl_First_BMenu
            $ JeanX.History.remove("bottomless")

#    elif Options[0] == "boyfriend?":
#        call Jean_BF
#    elif Options[0] == "lover?":
#        call Jean_Love
#    elif Options[0] == "sir?":
#        call Jean_Sub
#    elif Options[0] == "master?":
#        call Jean_Master
#    elif Options[0] == "sexfriend?":
#        call Jean_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Jean_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Jean_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Отойди от меня.",
                "Я не хочу чувствовать твой запах рядом с собой.",
                "Отвали.",
                "Свали."])
        ch_j "[Line]"

    else: #all else fell through. . .
            if not Player.Male:
                ch_j "Ох, ты хотела сказать что-то интересное?"
            else:
                ch_j "Ох, ты хотел сказать что-то интересное?"

            $ D20 = renpy.random.randint(1, 20)
            if D20 == 1:
                    $ JeanX.FaceChange("normal")
                    ch_j "Слушай, дай мне свои конспекты по физике."
                    $ JeanX.FaceChange("angry",Eyes="down")
                    ch_j ". . ."
                    $ JeanX.FaceChange("angry")
                    ch_j "Твои записи - хрень. Старайся лучше."
            elif D20 == 2:
                    $ JeanX.FaceChange("angry")
                    ch_j "Куда делся Лэнс? Я давно его не видела."
            elif D20 == 3:
                    $ JeanX.FaceChange("normal",Eyes="side")
                    ch_j ". . ."
                    $ JeanX.FaceChange("surprised")
                    if not Player.Male:
                        ch_j "Ох, о чем ты там говорила?"
                    else:
                        ch_j "Ох, о чем ты там говорил?"
                    $ JeanX.FaceChange("normal")
            elif D20 == 4:
                    $ JeanX.FaceChange("sad")
                    ch_j "Не знаю, почему я до сих пор посещаю эти занятия. Я уже знаю все, что мне нужно."
            elif D20 == 5:
                    $ JeanX.FaceChange("smile")
                    ch_j "Нет ничего лучше быстрого сна для \"подзарядки\"."
            elif D20 == 6:
                    $ JeanX.FaceChange("perplexed")
                    ch_j "О, я только что заметила твой наряд. . . интересный выбор."
            elif D20 == 7:
                    $ JeanX.FaceChange("smile")
                    if not Player.Male:
                        ch_j "Ты видела, как я недавно разгромила комнату Опасности?"
                    else:
                        ch_j "Ты видел, как я недавно разгромила комнату Опасности?"
                    ch_j "Я хочу повторить!"
            elif D20 == 8:
                    $ JeanX.FaceChange("angry")
                    ch_j "Тихо."
                    $ JeanX.FaceChange("angry",Eyes="side")
                    ch_j "Пришло время подумать."
                    $ JeanX.FaceChange("smile")
                    ch_j "Хорошо, готово."
            elif D20 == 9:
                    $ JeanX.FaceChange("confused")
                    ch_j "Я только что уловила несколько мыслей профессора МакКоя."
                    ch_j "Они не совсем. . . здоровые."
            elif D20 == 10:
                    $ JeanX.FaceChange("smile")
                    ch_j "Я слышала, девочки собираются за мороженым, угости меня."
            elif D20 == 11:
                    $ JeanX.FaceChange("smile")
                    ch_j "Я скорее всего попозже схожу поплавать. Обязательно возьми с собой полотенце."
            elif D20 == 12:
                    $ JeanX.FaceChange("smile")
                    ch_j "Мне вполне нравится общаться с тобой. . ."
                    if not Player.Male:
                        ch_j "Ты такая. . ."
                        ch_j "Простая."
                    else:
                        ch_j "Ты такой. . ."
                        ch_j "Простой."
            elif D20 == 13:
                    $ JeanX.FaceChange("smile")
                    ch_j "Одно мое слово подобно тысяче. . ."
                    ch_j "Ну. . . ты знаешь!"
            elif D20 == 14:
                    $ JeanX.FaceChange("smile")
                    ch_j "Миссии - это настоящая мука, но, по крайней мере, я могу немного поработать."
            elif D20 == 15:
                    $ JeanX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_j "Ты не видела странную девушку. . ?"
                        ch_j "Ее мысли. . . розовые. . ."
                    else:
                        ch_j "Ты не видел странную девушку. . ?"
                        ch_j "Ее мысли. . . розовые. . ."
            elif D20 == 16:
                    $ JeanX.FaceChange("perplexed")
                    ch_j "Я давно не была дома. Я почти забыла, где он находится."
            elif D20 == 17:
                    $ JeanX.FaceChange("perplexed")
                    ch_j "Эмма ведь сучка, да?"
                    ch_j "Дело же не только во мне?"
            elif D20 == 18:
                    $ JeanX.FaceChange("smile")
                    ch_j "Знаешь, иногда я думаю, что мне нужно хобби."
                    ch_j "А потом я просто поручаю это кому-нибудь другому."
            else:
                    $ JeanX.FaceChange("smile")
                    ch_j "С тобой весело проводить время."

    $ Line = 0
    return

# start Jean_Names//////////////////////////////////////////////////////////
label Jean_Names:     #rkelj
    menu:
        ch_j "А? Как мне тебя звать?"
        "Зови по инициалам.":
            $ JeanX.Petname = Player.Name[:1]  #fix test this
            $ JeanX.Petname_rod = Player.Name[:1]
            $ JeanX.Petname_dat = Player.Name[:1]
            $ JeanX.Petname_vin = Player.Name[:1]
            $ JeanX.Petname_tvo = Player.Name[:1]
            $ JeanX.Petname_pre = Player.Name[:1]  #fix test this
            ch_j "Хорошо, [JeanX.Petname]."
        "Зови меня по имени.":
            if Player.Name in JeanX.Petnames:
                    $ JeanX.Petname = Player.Name
                    $ JeanX.Petname_rod = Player.Name_rod
                    $ JeanX.Petname_dat = Player.Name_dat
                    $ JeanX.Petname_vin = Player.Name_vin
                    $ JeanX.Petname_tvo = Player.Name_tvo
                    $ JeanX.Petname_pre = Player.Name_pre
                    ch_j "Конечно, [JeanX.Petname]."
            else:
                    ch_j "Конечно, [JeanX.Petname]."
                    menu:
                        extend ""
                        "Ладно, как хочешь.":
                                pass
                        "Нет, по -настоящему- имени, [Player.Name].":
                                if ApprovalCheck(JeanX, 700, "LO"):
                                        $ JeanX.Petname = Player.Name
                                        $ JeanX.Petname_rod = Player.Name_rod
                                        $ JeanX.Petname_dat = Player.Name_dat
                                        $ JeanX.Petname_vin = Player.Name_vin
                                        $ JeanX.Petname_tvo = Player.Name_tvo
                                        $ JeanX.Petname_pre = Player.Name_pre
                                        $ JeanX.Petnames.append(Player.Name)
                                        ch_j "Ладно, хорошо, придется его запомнить. . . [JeanX.Petname]."
                                else:
                                        call JeanName(1) #picks a random new name
                                        if not Player.Male:
                                            ch_j "Ладно, тут ты права. . . [JeanX.Petname]!"
                                        else:
                                            ch_j "Ладно, тут ты прав. . . [JeanX.Petname]!"
                                        menu:
                                            extend ""
                                            "Ладно, как хочешь.":
                                                    pass
                                            "Нет, зови меня [Player.Name]!":
                                                    call JeanName #picks a random new name
                                                    ch_j "Хорошо, не кричи. . . [JeanX.Petname], вот."
            #end real name
        "Зови меня \"моя девушка\"." if "boyfriend" in JeanX.Petnames and not Player.Male:
            $ JeanX.Petname = "моя девушка"
            $ JeanX.Petname_rod = "моей девушки"
            $ JeanX.Petname_dat = "моей девушке"
            $ JeanX.Petname_vin = "мою девушку"
            $ JeanX.Petname_tvo = "моей девушкой"
            $ JeanX.Petname_pre = "моей девушке"
            ch_j ". . . ладно, [JeanX.Petname]."
        "Зови меня \"мой парень\"." if "boyfriend" in JeanX.Petnames and Player.Male:
            $ JeanX.Petname = "мой парень"
            $ JeanX.Petname_rod = "моего парня"
            $ JeanX.Petname_dat = "моему парню"
            $ JeanX.Petname_vin = "моего парня"
            $ JeanX.Petname_tvo = "моим парнем"
            $ JeanX.Petname_pre = "моем парне"
            ch_j ". . . ладно, [JeanX.Petname]."
        "Зови меня \"любимая\"." if "lover" in JeanX.Petnames and not Player.Male:
            $ JeanX.Petname = "любимая"
            $ JeanX.Petname_rod = "любимой"
            $ JeanX.Petname_dat = "любимой"
            $ JeanX.Petname_vin = "любимую"
            $ JeanX.Petname_tvo = "любимой"
            $ JeanX.Petname_pre = "любимой"
            ch_j ". . ."
            ch_j ". . . ладно, [JeanX.Petname]."
        "Зови меня \"любимый\"." if "lover" in JeanX.Petnames and Player.Male:
            $ JeanX.Petname = "любимый"
            $ JeanX.Petname_rod = "любимого"
            $ JeanX.Petname_dat = "любимому"
            $ JeanX.Petname_vin = "любимого"
            $ JeanX.Petname_tvo = "любимым"
            $ JeanX.Petname_pre = "любимом"
            ch_j ". . ."
            ch_j ". . . ладно, [JeanX.Petname]."
        "Зови меня \"госпожа\"." if "sir" in JeanX.Petnames and not Player.Male:
            $ JeanX.Petname = "госпожа"
            $ JeanX.Petname_rod = "госпожи"
            $ JeanX.Petname_dat = "госпоже"
            $ JeanX.Petname_vin = "госпожу"
            $ JeanX.Petname_tvo = "госпожой"
            $ JeanX.Petname_pre = "госпоже"
            ch_j "Ха, конечно, [JeanX.Petname]."
        "Зови меня \"господин\"." if "sir" in JeanX.Petnames and Player.Male:
            $ JeanX.Petname = "господин"
            $ JeanX.Petname_rod = "господина"
            $ JeanX.Petname_dat = "господину"
            $ JeanX.Petname_vin = "господина"
            $ JeanX.Petname_tvo = "господином"
            $ JeanX.Petname_pre = "господине"
            ch_j "Ха, конечно, [JeanX.Petname]."
        "Зови меня \"хозяйка\"." if "master" in JeanX.Petnames and not Player.Male:
            $ JeanX.Petname = "хозяйка"
            $ JeanX.Petname_rod = "хозяйки"
            $ JeanX.Petname_dat = "хозяйке"
            $ JeanX.Petname_vin = "хозяйку"
            $ JeanX.Petname_tvo = "хозяйкой"
            $ JeanX.Petname_pre = "хозяйке"
            ch_j "Эм. . . да, [JeanX.Petname]."
        "Зови меня \"хозяин\"." if "master" in JeanX.Petnames and Player.Male:
            $ JeanX.Petname = "хозяин"
            $ JeanX.Petname_rod = "хозяина"
            $ JeanX.Petname_dat = "хозяину"
            $ JeanX.Petname_vin = "хозяина"
            $ JeanX.Petname_tvo = "хозяином"
            $ JeanX.Petname_pre = "хозяине"
            ch_j "Эм. . . да, [JeanX.Petname]."
        "Зови меня \"любовница\"." if "sex friend" in JeanX.Petnames and not Player.Male:
            $ JeanX.Petname = "любовница"
            $ JeanX.Petname_rod = "любовницы"
            $ JeanX.Petname_dat = "любовнице"
            $ JeanX.Petname_vin = "любовницу"
            $ JeanX.Petname_tvo = "любовницей"
            $ JeanX.Petname_pre = "любовнице"
            ch_j "Ха, ладно, [JeanX.Petname]."
        "Зови меня \"любовник\"." if "sex friend" in JeanX.Petnames and Player.Male:
            $ JeanX.Petname = "любовник"
            $ JeanX.Petname_rod = "любовника"
            $ JeanX.Petname_dat = "любовнику"
            $ JeanX.Petname_vin = "любовника"
            $ JeanX.Petname_tvo = "любовником"
            $ JeanX.Petname_pre = "любовнике"
            ch_j "Ха, ладно, [JeanX.Petname]."
        "Зови меня \"секс-партнерша\"." if "fuck buddy" in JeanX.Petnames and not Player.Male:
            $ JeanX.Petname = "секс-партнерша"
            $ JeanX.Petname_rod = "секс-партнерши"
            $ JeanX.Petname_dat = "секс-партнерше"
            $ JeanX.Petname_vin = "секс-партнершу"
            $ JeanX.Petname_tvo = "секс-партнершей"
            $ JeanX.Petname_pre = "секс-партнерше"
            ch_j "Хах, ладно, [JeanX.Petname]."
        "Зови меня \"секс-партнер\"." if "fuck buddy" in JeanX.Petnames and Player.Male:
            $ JeanX.Petname = "секс-партнер"
            $ JeanX.Petname_rod = "секс-партнера"
            $ JeanX.Petname_dat = "секс-партнеру"
            $ JeanX.Petname_vin = "секс-партнера"
            $ JeanX.Petname_tvo = "секс-партнером"
            $ JeanX.Petname_pre = "секс-партнере"
            ch_j "Хах, ладно, [JeanX.Petname]."
        "Зови меня \"мамочка\"." if "daddy" in JeanX.Petnames and not Player.Male:
            $ JeanX.Petname = "мамочка"
            $ JeanX.Petname_rod = "мамочки"
            $ JeanX.Petname_dat = "мамочке"
            $ JeanX.Petname_vin = "мамочку"
            $ JeanX.Petname_tvo = "мамочкой"
            $ JeanX.Petname_pre = "мамочке"
            ch_j "Хмм. . . [JeanX.Petname]."
        "Зови меня \"папочка\"." if "daddy" in JeanX.Petnames and Player.Male:
            $ JeanX.Petname = "папочка"
            $ JeanX.Petname_rod = "папочки"
            $ JeanX.Petname_dat = "папочке"
            $ JeanX.Petname_vin = "папочку"
            $ JeanX.Petname_tvo = "папочкой"
            $ JeanX.Petname_pre = "папочке"
            ch_j "Хмм. . . [JeanX.Petname]."
        "Неважно.":
            return
    return
# end Jean_Names//////////////////////////////////////////////////////////

label Jean_Pet: #rkelj
    while True:
        menu:
            extend ""
            "Обходительно":
                menu:
                    extend ""
                    "Думаю, буду звать тебя просто Джин.":
                        $ JeanX.Pet = "Джин"
                        $ JeanX.Pet_rod = "Джин"
                        $ JeanX.Pet_dat = "Джин"
                        $ JeanX.Pet_vin = "Джин"
                        $ JeanX.Pet_tvo = "Джин"
                        $ JeanX.Pet_pre = "Джин"
                        ch_j "Ладно."

                    "Думаю, буду звать тебя \"моя девушка\".":
                        if "boyfriend" in JeanX.Petnames:
                            $ JeanX.Pet = "моя девушка"
                            $ JeanX.Pet_rod = "моей девушки"
                            $ JeanX.Pet_dat = "моей девушке"
                            $ JeanX.Pet_vin = "мою девушку"
                            $ JeanX.Pet_tvo = "моей девушкой"
                            $ JeanX.Pet_pre = "моей девушке"
                            $ JeanX.FaceChange("sexy", 1)
                            ch_j "Ага, ладно, [JeanX.Petname]."
                        else:
                            $ JeanX.FaceChange("angry")
                            ch_j "Я НЕ твоя девушка, [JeanX.Petname]."

                    "Думаю, буду звать тебя \детка\".":
                        if "boyfriend" in JeanX.Petnames or ApprovalCheck(JeanX, 700, "L"):
                            $ JeanX.FaceChange("sexy", 1)
                            $ JeanX.Pet = "детка"
                            $ JeanX.Pet_rod = "детки"
                            $ JeanX.Pet_dat = "детке"
                            $ JeanX.Pet_vin = "детку"
                            $ JeanX.Pet_tvo = "деткой"
                            $ JeanX.Pet_pre = "детке"
                            ch_j "Наверное так, я твоя детка, [JeanX.Petname]."
                        else:
                            $ JeanX.FaceChange("angry")
                            ch_j "Я тебе НЕ детка, [JeanX.Petname]."

                    "Думаю, буду звать тебя \"крошка\".":
                        if "boyfriend" in JeanX.Petnames or ApprovalCheck(JeanX, 600, "L"):
                            $ JeanX.Pet = "крошка"
                            $ JeanX.Pet_rod = "крошки"
                            $ JeanX.Pet_dat = "крошке"
                            $ JeanX.Pet_vin = "крошку"
                            $ JeanX.Pet_tvo = "крошкой"
                            $ JeanX.Pet_pre = "крошке"
                            $ JeanX.FaceChange("sexy", 1)
                            ch_j "Наверное так, я твоя крошка, [JeanX.Petname]."
                        else:
                            $ JeanX.FaceChange("angry")
                            ch_j "Я тебе НЕ крошка, [JeanX.Petname]."

                    "Думаю, буду звать тебя \"малышка\".":
                        if "boyfriend" in JeanX.Petnames or ApprovalCheck(JeanX, 500, "L"):
                            $ JeanX.Pet = "малышка"
                            $ JeanX.Pet_rod = "малышки"
                            $ JeanX.Pet_dat = "малышке"
                            $ JeanX.Pet_vin = "малышку"
                            $ JeanX.Pet_tvo = "малышкой"
                            $ JeanX.Pet_pre = "малышке"
                            $ JeanX.FaceChange("sexy", 1)
                            ch_j "Мило, [JeanX.Petname]."
                        else:
                            $ JeanX.FaceChange("angry")
                            ch_j "Я не малышка."


                    "Думаю, буду звать тебя \"милая\".":
                        if "boyfriend" in JeanX.Petnames or ApprovalCheck(JeanX, 600, "L"):
                            $ JeanX.Pet = "милая"
                            $ JeanX.Pet_rod = "милой"
                            $ JeanX.Pet_dat = "милой"
                            $ JeanX.Pet_vin = "милую"
                            $ JeanX.Pet_tvo = "милой"
                            $ JeanX.Pet_pre = "милой"
                            ch_j "Хорошо звучит, [JeanX.Petname]."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Слишком приторно, [JeanX.Petname]."

                    "Думаю, буду звать тебя \"секси\".":
                        if "lover" in JeanX.Petnames or ApprovalCheck(JeanX, 800):
                            $ JeanX.Pet = "секси"
                            $ JeanX.Pet_rod = "секси"
                            $ JeanX.Pet_dat = "секси"
                            $ JeanX.Pet_vin = "секси"
                            $ JeanX.Pet_tvo = "секси"
                            $ JeanX.Pet_pre = "секси"
                            $ JeanX.FaceChange("sexy", 1)
                            ch_j "Я за, ты же знаешь, [JeanX.Petname]."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Это верно, но немного грубовато, [JeanX.Petname]."

                    "Думаю, буду звать тебя \"любимая\".":
                        if "lover" in JeanX.Petnames or ApprovalCheck(JeanX, 1200):
                            $ JeanX.Pet = "любимая"
                            $ JeanX.Pet_rod = "любимой"
                            $ JeanX.Pet_dat = "любимой"
                            $ JeanX.Pet_vin = "любимую"
                            $ JeanX.Pet_tvo = "любимой"
                            $ JeanX.Pet_pre = "любимой"
                            $ JeanX.FaceChange("sexy", 1)
                            ch_j "Ха, ладно."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Я так не думаю, [JeanX.Petname]."

                    "Назад":
                        pass

            "Грубо":
                menu:
                    "Думаю, буду звать тебя \"рабыня\".":
                        if "master" in JeanX.Petnames or ApprovalCheck(JeanX, 800, "O"):
                            $ JeanX.Pet = "рабыня"
                            $ JeanX.Pet_rod = "рабыни"
                            $ JeanX.Pet_dat = "рабыне"
                            $ JeanX.Pet_vin = "рабыню"
                            $ JeanX.Pet_tvo = "рабыней"
                            $ JeanX.Pet_pre = "рабыне"
                            $ JeanX.FaceChange("bemused", 1)
                            ch_j ". . . ладно, [JeanX.Petname]."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Я тебе не рабыня, [JeanX.Petname]."

                    "Думаю, буду звать тебя \"питомец\".":
                        if "master" in JeanX.Petnames or ApprovalCheck(JeanX, 650, "O"):
                            $ JeanX.FaceChange("bemused", 1)
                            $ JeanX.Pet = "питомец"
                            $ JeanX.Pet_rod = "питомце"
                            $ JeanX.Pet_dat = "питомцу"
                            $ JeanX.Pet_vin = "питомца"
                            $ JeanX.Pet_tvo = "питомцем"
                            $ JeanX.Pet_pre = "питомце"
                            ch_j ". . . ладно, [JeanX.Petname]."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Я не твой -питомец,- [JeanX.Petname]."

                    "Думаю, буду звать тебя \"шлюха\".":
                        if "sex friend" in JeanX.Petnames or ApprovalCheck(JeanX, 900, "OI"):
                            $ JeanX.Pet = "шлюха"
                            $ JeanX.Pet_rod = "шлюхи"
                            $ JeanX.Pet_dat = "шлюхе"
                            $ JeanX.Pet_vin = "шлюху"
                            $ JeanX.Pet_tvo = "шлюхой"
                            $ JeanX.Pet_pre = "шлюхе"
                            $ JeanX.FaceChange("sexy")
                            ch_j "Ну. . . да."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            $ JeanX.Mouth = "surprised"
                            ch_j "Ты хоть знаешь, что это за слово?"

                    "Думаю, буду звать тебя \"блядь\".":
                        if "fuckbuddy" in JeanX.Petnames or ApprovalCheck(JeanX, 1000, "OI"):
                            $ JeanX.Pet = "блядь"
                            $ JeanX.Pet_rod = "бляди"
                            $ JeanX.Pet_dat = "бляде"
                            $ JeanX.Pet_vin = "блядь"
                            $ JeanX.Pet_tvo = "блядью"
                            $ JeanX.Pet_pre = "бляде"
                            $ JeanX.FaceChange("sly")
                            ch_j ". . ."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Лучше не надо. . ."

                    "Думаю, буду звать тебя \"сладкогрудая\".":
                        if "sex friend" in JeanX.Petnames or ApprovalCheck(JeanX, 1400):
                            $ JeanX.Pet = "сладкогрудая"
                            $ JeanX.Pet_rod = "сладкогрудой"
                            $ JeanX.Pet_dat = "сладкогрудой"
                            $ JeanX.Pet_vin = "сладкогрудую"
                            $ JeanX.Pet_tvo = "сладкогрудой"
                            $ JeanX.Pet_pre = "сладкогрудой"
                            $ JeanX.FaceChange("sly", 1)
                            ch_j ". . . ладно."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Это не круто."

                    "Думаю, буду звать тебя \"любовница\".":
                        if "sex friend" in JeanX.Petnames or ApprovalCheck(JeanX, 600, "I"):
                            $ JeanX.Pet = "любовница"
                            $ JeanX.Pet_rod = "любовницы"
                            $ JeanX.Pet_dat = "любовнице"
                            $ JeanX.Pet_vin = "любовницу"
                            $ JeanX.Pet_tvo = "любовницей"
                            $ JeanX.Pet_pre = "любовнице"
                            $ JeanX.FaceChange("sly")
                            ch_j "Ага. . ."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Полегче, [JeanX.Petname]."

                    "Думаю, буду звать тебя \"секс-партнерша\".":
                        if "fuckbuddy" in JeanX.Petnames or ApprovalCheck(JeanX, 700, "I"):
                            $ JeanX.Pet = "секс-партнерша"
                            $ JeanX.Pet_rod = "секс-партнерши"
                            $ JeanX.Pet_dat = "секс-партнерше"
                            $ JeanX.Pet_vin = "секс-партнершу"
                            $ JeanX.Pet_tvo = "секс-партнершей"
                            $ JeanX.Pet_pre = "секс-партнерше"
                            $ JeanX.FaceChange("sly")
                            ch_j "Ага."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            $ JeanX.Mouth = "surprised"
                            ch_j "Не смей так шутить, [JeanX.Petname]."

                    "Думаю, буду звать тебя \"доченька\".":
                        if "daddy" in JeanX.Petnames or ApprovalCheck(JeanX, 1200):
                            $ JeanX.Pet = "доченька"
                            $ JeanX.Pet_rod = "доченьки"
                            $ JeanX.Pet_dat = "доченьке"
                            $ JeanX.Pet_vin = "доченьку"
                            $ JeanX.Pet_tvo = "доченькой"
                            $ JeanX.Pet_pre = "доченьке"
                            $ JeanX.FaceChange("smile", 1)
                            ch_j "Можно и так."
                        else:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Это очень странно."

                    "Назад":
                        pass

            "Неважно.":
                return
    return

#label Jean_Namecheck(JeanX.Pet = JeanX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname


# start Jean_Rename//////////////////////////////////////////////////////////
label Jean_Rename:   #rkelj
        #Sets alternate names from Jean
        $ JeanX.Mouth = "smile"
        ch_j "Да?"
        menu:
            extend ""
            "Я думаю, \"Джин\" красивое имя." if JeanX.Name != "Джин" and "Jean" in JeanX.Names:
                    $ JeanX.Name = "Джин"
                    $ JeanX.Name_rod = "Джин"
                    $ JeanX.Name_dat = "Джин"
                    $ JeanX.Name_vin = "Джин"
                    $ JeanX.Name_tvo = "Джин"
                    $ JeanX.Name_pre = "Джин"
                    ch_j "Ну да. Мне оно нравится."
            "Неважно.":
                    pass
        $ JeanX.AddWord(1,0,"namechange")
        return
# end Jean_Rename//////////////////////////////////////////////////////////


# start Jean_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jean_Personality(Cnt = 0):    #rkelj
    if not JeanX.Chat[4] or Cnt:
        "Поскольку у вас все хорошо получается в одной области, вы можете убедить Джин сосредоточиться на любой другой."
        "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
        "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
    menu:
        ch_j "Yeah?"
        "Больше Послушания. [[Любовь в Послушание]" if JeanX.Love > 900:
            ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
            ch_j "Ох, ладно, Я попробую. . ."
            $ JeanX.Chat[4] = 1
        "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if JeanX.Love > 900:
            ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
            ch_j "Ох, если ты просишь. . ."
            $ JeanX.Chat[4] = 2

        "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if JeanX.Obed > 900:
            ch_p "Я хочу, чтобы ты была более раскрепощенной."
            ch_j "Я попробую. . ."
            $ JeanX.Chat[4] = 3
        "Больше Любви. [[Повиновение в Любовь]" if JeanX.Obed > 900:
            ch_p "Я хочу, чтобы ты училась любить меня."
            ch_j "Ну. . . ладно. . ."
            $ JeanX.Chat[4] = 4

        "Больше Повиновения. [[Раскрепощенность в Повиновение]" if (JeanX.Inbt - JeanX.IX) > 900:
            ch_p "Я знаю, что нам и так весело, но разве ты не можешь иногда слушаться меня?"
            ch_j "Хмм. . . звучит своеобразно. . ."
            $ JeanX.Chat[4] = 5

        "Больше Любви. [[Раскрепощенность в Любовь]" if (JeanX.Inbt - JeanX.IX) > 900:
            ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
            ch_j "Ох, ладно. . ."
            $ JeanX.Chat[4] = 6

        "Просто делай то, что тебе нравится. . .[[Сбросить]" if JeanX.Chat[4]:
            ch_p "Помнишь, что мы обсуждали? Забудь."
            ch_j "Эм, как скажешь. . ."
            $ JeanX.Chat[4] = 0
        "Повторить правила":
            call Jean_Personality(1)
            return
        "Неважно.":
            return
    return
# end Jean_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Jean_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jean_Summon(Tempmod=Tempmod): #rkelj
    $ JeanX.OutfitChange()
    if "no summon" in JeanX.RecentActions:
                if "angry" in JeanX.RecentActions:
                    ch_j "Уходи!"
                elif JeanX.RecentActions.count("no summon") > 1:
                    ch_j "Я хочу побыть в одиночестве!"
                    $ JeanX.RecentActions.append("angry")
#                elif Current_Time == "Night":
#                    ch_j "Like I said, it's too late for that."
                else:
                    ch_j "Я же сказала, что занята!"
                $ JeanX.RecentActions.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if JeanX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif JeanX.Loc == "bg jean":
        $ Tempmod = -10
    elif JeanX.Loc == "bg showerroom":
        $ Tempmod = -30

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"
    if Time_Count >= 3: #night time
                if ApprovalCheck(JeanX, 500, "L") or ApprovalCheck(JeanX, 400, "O"):
                        #It's night time but she likes you.
                        ch_j "Ты тоже не спишь? Отлично."
                        $ JeanX.Loc = bg_current
                        call Taboo_Level
                        call Set_The_Scene
                else:
                        #It's night time and she isn't into you
                        ch_j "Лучше не стоит. . ."
                        $ JeanX.RecentActions.append("no summon")
                return
    elif "les" in JeanX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(JeanX, 2000):
                    ch_j "Я тут с одной девушкой. Хочешь к нам?"
                    menu:
                        extend ""
                        "Конечно.":
                            $ Line = "go to"
                        "Нет, спасибо.":
                            ch_j "Ха, ладно. . ."
                            return
            else:
                    ch_j "Я сейчас. . . немного занята."
                    ch_j "Поговорим позже."
                    $ JeanX.RecentActions.append("no summon")
                    return
    elif not ApprovalCheck(JeanX, 700, "L") or not ApprovalCheck(JeanX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(JeanX, 300):
                ch_j "Я занята, [JeanX.Petname]."
                $ JeanX.RecentActions.append("no summon")
                return


        if "summoned" in JeanX.RecentActions:
                pass
        elif "goto" in JeanX.RecentActions:
                if not Player.Male:
                    ch_j "Ты только что ушла. . ."
                else:
                    ch_j "Ты только что ушел. . ."
        elif JeanX.Loc == "bg classroom":
                ch_j "Я сейчас в аудитории."
        elif JeanX.Loc == "bg dangerroom":
                ch_j "Я в комнате Опасности, [JeanX.Petname]."
        elif JeanX.Loc == "bg campus":
                ch_j "Я сейчас отдыхаю на площаде."
        elif JeanX.Loc == "bg jean":
                ch_j "Я в своей комнате, [JeanX.Petname]."
        elif JeanX.Loc == "bg player":
                if not Player.Male:
                    ch_j "Я в твоей комнате, [JeanX.Petname], а ты сама где?"
                else:
                    ch_j "Я в твоей комнате, [JeanX.Petname], а ты сам где?"
        elif JeanX.Loc == "bg showerroom":
            if ApprovalCheck(JeanX, 1600):
                ch_j "Я сейчас в душе."
            else:
                ch_j "Я сейчас в душе, [JeanX.Petname]."
                ch_j "Не входи без стука."
                $ JeanX.RecentActions.append("no summon")
                return
        elif JeanX.Loc == "hold":
                ch_j "Я сейчас занята."
                $ JeanX.RecentActions.append("no summon")
                return
        else:
                ch_j "Почему бы тебе не прийти ко мне?"


        if "summoned" in JeanX.RecentActions:
            ch_j "Опять? Ну, хорошо."
            $ Line = "yes"
        elif "goto" in JeanX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
#                                ch_j "Ok then."
                                $ Line = "go to"
                "Нет.":
                                ch_j "Ну хорошо."
                "Мне бы {i}очень{/i} хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(JeanX, 600, "L") or ApprovalCheck(JeanX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(JeanX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(JeanX, 1400):
                                #she is generally favorable
                                ch_j "Хорошо. . ."
                                $ Line = "yes"
                        elif ApprovalCheck(JeanX, 200, "O"):
                                #she is not obedient
                                ch_j "Меня не волнует, что ты сказала."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(JeanX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(JeanX, 1400):
                                #she is generally favorable
                                ch_j "Хорошо. . ."
                                $ Line = "yes"
                        elif ApprovalCheck(JeanX, 200, "O"):
                                #she is not obedient
                                ch_j "Меня не волнует, что ты сказал."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Ладно, я сейчас приду.":
                    $ JeanX.Statup("Love", 55, 1)
                    $ JeanX.Statup("Inbt", 30, 1)
#                    ch_j "Good."
                    $ Line = "go to"

                "Ладно, тогда поговорим позже.":
                    $ JeanX.Statup("Obed", 50, 1)
                    $ JeanX.Statup("Obed", 30, 2)
                    ch_j "Ладно."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                    if ApprovalCheck(JeanX, 650, "L") or ApprovalCheck(JeanX, 1500):
                        $ JeanX.Statup("Love", 70, 1)
                        $ JeanX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ JeanX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                        ch_j "Прямо очень?"

                "Давай, будет весело.":
                    if ApprovalCheck(JeanX, 400, "L") and ApprovalCheck(JeanX, 800):
                        $ JeanX.Statup("Love", 70, 1)
                        $ JeanX.Statup("Obed", 50, 1)
                        $ Line = "fun"
                    else:
                        $ JeanX.Statup("Inbt", 30, 1)
                        $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                    if ApprovalCheck(JeanX, 600, "O"):
                        #she is obedient
                        $ JeanX.Statup("Love", 50, 1, 1)
                        $ JeanX.Statup("Love", 40, -1)
                        $ JeanX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(JeanX, 1500):
                        #she is generally favorable
                        $ JeanX.Statup("Love", 70, -2)
                        $ JeanX.Statup("Love", 90, -1)
                        $ JeanX.Statup("Obed", 50, 2)
                        $ JeanX.Statup("Obed", 90, 1)
                        ch_j "Ладно."
                        $ Line = "yes"

                    elif ApprovalCheck(JeanX, 200, "O"):
                        #she is not obedient
                        $ JeanX.Statup("Love", 60, -4)
                        $ JeanX.Statup("Love", 90, -3)
                        ch_j "A я говорю \"нет.\""
                        $ JeanX.Statup("Inbt", 40, 2)
                        $ JeanX.Statup("Inbt", 60, 1)
                        $ JeanX.Statup("Obed", 70, -3)
                        ch_j "Я останусь здесь."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ JeanX.Statup("Inbt", 30, 1)
                        $ JeanX.Statup("Inbt", 50, 1)
                        $ JeanX.Statup("Love", 50, -1, 1)
                        $ JeanX.Statup("Obed", 70, -1)
                        $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                    if ApprovalCheck(JeanX, 600, "O"):
                        #she is obedient
                        $ JeanX.Statup("Love", 50, 1, 1)
                        $ JeanX.Statup("Love", 40, -1)
                        $ JeanX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(JeanX, 1500):
                        #she is generally favorable
                        $ JeanX.Statup("Love", 70, -2)
                        $ JeanX.Statup("Love", 90, -1)
                        $ JeanX.Statup("Obed", 50, 2)
                        $ JeanX.Statup("Obed", 90, 1)
                        ch_j "Ладно."
                        $ Line = "yes"

                    elif ApprovalCheck(JeanX, 200, "O"):
                        #she is not obedient
                        $ JeanX.Statup("Love", 60, -4)
                        $ JeanX.Statup("Love", 90, -3)
                        ch_j "A я говорю \"нет.\""
                        $ JeanX.Statup("Inbt", 40, 2)
                        $ JeanX.Statup("Inbt", 60, 1)
                        $ JeanX.Statup("Obed", 70, -3)
                        ch_j "Я останусь здесь."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ JeanX.Statup("Inbt", 30, 1)
                        $ JeanX.Statup("Inbt", 50, 1)
                        $ JeanX.Statup("Love", 50, -1, 1)
                        $ JeanX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if JeanX.Love > JeanX.Obed:
            ch_j "Ладно."
        else:
            ch_j "Хорошо, если ты настаиваешь. . ."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ JeanX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            ch_j "Извини, [JeanX.Petname], я немного занята."
            $ JeanX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ JeanX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            $ Line = 0
            $ Nearby = []
            $ Party = [JeanX]
            if JeanX.Loc == "bg classroom":
                    ch_j "Хорошо."
                    jump Class_Room
            elif JeanX.Loc == "bg dangerroom":
                    ch_j "Я постараюсь дождаться тебя."
                    jump Danger_Room
            elif JeanX.Loc == "bg jean":
                    ch_j "Не заставляй меня ждать."
                    jump Jean_Room
            elif JeanX.Loc == "bg player":
                    ch_j "Не заставляй меня ждать."
                    jump Player_Room
            elif JeanX.Loc == "bg showerroom":
                    ch_j "Тогда скоро увидимся."
                    jump Shower_Room
            elif JeanX.Loc == "bg campus":
                    ch_j "Ладно."
                    jump Campus
            elif JeanX.Loc != "hold":
                    ch_j "Ага, увидимся."
                    $ bg_current = JeanX.Loc
                    jump Misplaced
            else:
                    ch_j "Встретимся в моей комнате."
                    $ JeanX.Loc = "bg jean"
                    jump Jean_Room

    #She's agreed to come over
    elif Line == "lonely":
            ch_j "Ох. . . хорошо. . ."
    elif Line == "command":
            ch_j "Хорошо, [JeanX.Petname]."
    elif Line == "fun":
            ch_j "Конечно."

    $ JeanX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(JeanX)
            return
    $ JeanX.Loc = bg_current
    call Taboo_Level(0)
    $ JeanX.OutfitChange()
    call Set_The_Scene
    return

# End Jean Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Jean_Leave(Tempmod=Tempmod, GirlsNum = 0):   #rkelj
    if "leaving" in JeanX.RecentActions:
        $ JeanX.DrainWord("leaving")
    else:
        return

    if JeanX.Loc == "hold":
            # Activates if she's being moved out of play
            ch_j "Ладно, думаю, у меня еще остались дела."
            return

    if JeanX in Party or "lockedtravels" in JeanX.Traits:
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ JeanX.Loc = bg_current
            return

    elif "freetravels" in JeanX.Traits or not ApprovalCheck(JeanX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.
            $ JeanX.OutfitChange()
            if GirlsNum: #if someone left before her
                        ch_j "Я тоже ухожу."

            if JeanX.Loc == "bg classroom":
                        ch_j "У меня занятия."
            elif JeanX.Loc == "bg dangerroom":
                        ch_j "Я пойду немного потренируюсь."
            elif JeanX.Loc == "bg campus":
                        ch_j "У меня перерыв на площаде."
            elif JeanX.Loc == "bg jean":
                        ch_j "Я возвращаюсь в свою комнату."
            elif JeanX.Loc == "bg player":
                        ch_j "Я немного побуду в твоей комнате."
            elif JeanX.Loc == "bg pool":
                        ch_j "Я собираюсь заскочить в бассейн."
            elif JeanX.Loc == "bg showerroom":
                if ApprovalCheck(JeanX, 1400):
                        ch_j "Я иду в душ."
                else:
                        ch_j "Я уже ухожу."
            else:
                        ch_j "Я уже ухожу."
            hide Jean_Sprite
            hide Jean_Seated
            return
            #End Free Travels

    if bg_current == "bg dangerroom":
            call Gym_Exit([JeanX])

    $ JeanX.OutfitChange()

    if "follow" not in JeanX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ JeanX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    # Sets her preferences
    if JeanX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif JeanX.Loc == "bg showerroom":
        $ Tempmod = 40


    if GirlsNum: #if someone left before her
                ch_j "Ага, я тоже ухожу."

    if JeanX.Loc == "bg classroom":
        ch_j "У меня занятия."
    elif JeanX.Loc == "bg dangerroom":
        ch_j "У меня запланирована тренировка в комнате Опасности."
    elif JeanX.Loc == "bg campus":
        ch_j "Пойду гулять по площади."
    elif JeanX.Loc == "bg jean":
        ch_j "Я направляюсь обратно в свою комнату."
    elif JeanX.Loc == "bg player":
        ch_j "Я собираюсь немного побыть в твоей комнате."
    elif JeanX.Loc == "bg mall":
        ch_j "Я собираюсь в торговый центр."
    elif JeanX.Loc == "bg showerroom":
        if ApprovalCheck(JeanX, 1600):
            ch_j "Я иду в душ."
        else:
            ch_j "Я иду в душ, может быть, немного задержусь."
            return
    elif JeanX.Loc == "bg pool":
            ch_j "Я в бассейне."
    else:
            ch_j "Составишь компанию?"


    menu:
        extend ""
        "Ладно, я догоню.":
                if "followed" not in JeanX.RecentActions:
                    $ JeanX.Statup("Love", 55, 1)
                    $ JeanX.Statup("Inbt", 30, 1)
                $ Line = "go to"

        "Ладно, поговорим позже.":
                if "followed" not in JeanX.RecentActions:
                    $ JeanX.Statup("Obed", 50, 1)
                    $ JeanX.Statup("Obed", 30, 2)
                ch_j "Ладно, как хочешь."

        "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                if ApprovalCheck(JeanX, 650, "L") or ApprovalCheck(JeanX, 1500):
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Love", 70, 1)
                        $ JeanX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else:
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Inbt", 30, 1)
                    $ Line = "no"
                    ch_j "Прямо очень?"

        "Давай, будет весело.":
                if ApprovalCheck(JeanX, 400, "L") and ApprovalCheck(JeanX, 800):
                    $ JeanX.Statup("Love", 70, 1)
                    $ JeanX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else:
                    $ JeanX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Нет, останься здесь.":
                if ApprovalCheck(JeanX, 600, "O"):
                    #she is obedient
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Love", 40, -2)
                        $ JeanX.Statup("Obed", 90, 1)
                    $ Line = "command"

                elif D20 >= 7 and ApprovalCheck(JeanX, 1400):
                    #she is generally favorable
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Love", 70, -2)
                        $ JeanX.Statup("Love", 90, -1)
                        $ JeanX.Statup("Obed", 50, 2)
                        $ JeanX.Statup("Obed", 90, 1)
                    ch_j ". . . ладно."
                    $ Line = "yes"

                elif ApprovalCheck(JeanX, 200, "O"):
                    #she is not obedient
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Love", 70, -4)
                        $ JeanX.Statup("Love", 90, -2)
                    ch_j "Ты мне не указ."
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Inbt", 40, 2)
                        $ JeanX.Statup("Inbt", 60, 1)
                        $ JeanX.Statup("Obed", 70, -2)
                    ch_j "Ха!"
                else:
                    #she is obedient, but you failed to meet the checks
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Inbt", 30, 1)
                        $ JeanX.Statup("Inbt", 50, 1)
                        $ JeanX.Statup("Love", 50, -1, 1)
                        $ JeanX.Statup("Love", 90, -2)
                        $ JeanX.Statup("Obed", 70, -1)
                    $ Line = "no"
                #End ordered to stay

    call Taboo_Level(0)
    $ JeanX.RecentActions.append("followed")
    if not Line:
            #You end the dialog neutrally
            hide Jean_Sprite
            hide Jean_Seated
            call Gym_Clothes_Off([JeanX])
            return

    if Line == "no":
            # She's refused, context based dialog
            ch_j "Лучше не стоит."
            hide Jean_Sprite
            hide Jean_Seated
            call Gym_Clothes_Off([JeanX])
            return

    elif Line == "go to":
            #You agreed to go to her instead
            #$ Party.append(JeanX)
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")
            $ JeanX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            hide Jean_Sprite
            hide Jean_Seated
            $ Nearby = []
            $ Party = [JeanX]
            call Gym_Clothes_Off([JeanX])
            if JeanX.Loc == "bg classroom":
                ch_j "Ладно."
                jump Class_Room_Entry
            elif JeanX.Loc == "bg dangerroom":
                ch_j "Я пока пойду разомнусь."
                jump Danger_Room_Entry
            elif JeanX.Loc == "bg jean":
                ch_j "Ладно."
                jump Jean_Room
            elif JeanX.Loc == "bg player":
                ch_j "Хорошо."
                jump Player_Room
            elif JeanX.Loc == "bg showerroom":
                ch_j "Ладно, хорошо."
                jump Shower_Room_Entry
            elif JeanX.Loc == "bg campus":
                ch_j "Ладно."
                jump Campus_Entry
            elif JeanX.Loc == "bg pool":
                ch_j "Отлично."
                jump Pool_Entry
            elif JeanX.Loc == "bg mall":
                ch_j "Круто."
                jump Mall_Entry
            else:
                ch_j "Встретимся в твоей комнате."
                $ JeanX.Loc = "bg player"
                jump Player_Room
            #End "goto" where she's at

    #She's agreed to come over
    elif Line == "lonely":
            ch_j "Хорошо, составлю тебе компанию. . ."
    elif Line == "command":
            ch_j "Хорошо, [JeanX.Petname]. . ."
    elif Line:
            ch_j "Конечно."

    $ Line = 0
    ch_j "Я задержусь."
    $ JeanX.Loc = bg_current
    call Taboo_Level(0)
    return

# End Jean Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

### Jean's Clothes  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jean_Clothes:    #rkelj
    if JeanX.Taboo:
            if "exhibitionist" in JeanX.Traits:
                ch_j "Да? . ."
            elif ApprovalCheck(JeanX, 900, TabM=4) or ApprovalCheck(JeanX, 400, "I", TabM=3):
                ch_j "Думаю, можно. . ."
            else:
                ch_j "Мне не нравится это место. . ."
                ch_j "Можем поговорить в одной из наших комнат?"
                return
    elif ApprovalCheck(JeanX, 900, TabM=4) or ApprovalCheck(JeanX, 600, "L") or ApprovalCheck(JeanX, 300, "O"):
                ch_j "А? Что то не так с моей одеждой?"
    else:
                ch_j "Наслаждайся, а не советуй."
                return

    if Girl != JeanX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = JeanX
    call Shift_Focus(Girl)

label Jean_Wardrobe_Menu:
    $ JeanX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .
    while True:
        menu:
            ch_j "Что там насчет моей одежды?"
            "Верх":
                        call Jean_Clothes_Over
            "Низ":
                        call Jean_Clothes_Legs
            "Нижнее белье":
                        call Jean_Clothes_Under
            "Аксессуары":
                        call Jean_Clothes_Misc
            "Управление нарядами":
                        call Jean_Clothes_Outfits
            "Давай поговорим о том, что ты носишь.":
                        call Clothes_Schedule(JeanX)

            "Могу я посмотреть?" if JeanX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(JeanX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_j "Мило, да?"
                    hide PhoneSex
            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(JeanX,0,2)
                    if _return:
                        hide DressScreen
            "Может, тебе будет комфортнее за ширмой? (locked)" if JeanX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if JeanX.Loc == bg_current and not JeanX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she wants a screen
                    if not Player.Male and "girltalk" not in JeanX.History and "nogirls" not in JeanX.History:
                            ch_j "Не тупи."
                    elif ApprovalCheck(JeanX, 1500) or (JeanX.SeenChest and JeanX.SeenPussy):
                            ch_j "Не понимаю, почему ты спрашиваешь."
                    else:
                            show DressScreen zorder 150
                            ch_j "Ага, будет в самый раз."

            "У меня есть подарок для тебя (locked)" if JeanX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if JeanX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(JeanX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ JeanX.OutfitChange()
                    $ JeanX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != JeanX:
                            ch_p "Я хочу поговорить о твоей одежде."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = JeanX
                    call Shift_Focus(Girl)

            "Сменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current:
                    pass
            "Сменить вид" if Girl.Loc == bg_current:
                    call WardrobeView(JeanX)

            "Неважно, ты и так хорошо выглядишь":
                    call Girl_Pos_Reset(JeanX)
                    if "wardrobe" not in JeanX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if JeanX.Chat[1] <= 1:
                                    $ JeanX.Statup("Love", 70, 15)
                                    $ JeanX.Statup("Obed", 40, 20)
                                    ch_j "Разумеется."
                            elif JeanX.Chat[1] <= 10:
                                    $ JeanX.Statup("Love", 70, 5)
                                    $ JeanX.Statup("Obed", 40, 7)
                                    ch_j "Правда?"
                            elif JeanX.Chat[1] <= 50:
                                    $ JeanX.Statup("Love", 70, 1)
                                    $ JeanX.Statup("Obed", 40, 1)
                                    ch_j "Угу."
                            else:
                                    ch_j "Конечно."
                            $ JeanX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(JeanX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ JeanX.OutfitChange()
                    $ JeanX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ JeanX.Chat[1] += 1
                    $ Trigger = 0
                    if JeanX.Panties and "pantyless" in JeanX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ JeanX.DailyActions.remove("pantyless")
                    return

        #Loops back up
        #return #jump Jean_Clothes
        #End of Jean Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jean_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(JeanX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(JeanX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(JeanX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(JeanX,4,1)
                    "Одежда для сна":
                                call OutfitShame(JeanX,7,1)
                    "Купальник":
                                call OutfitShame(JeanX,10,1)

                    "Повседневка 1" if ApprovalCheck(JeanX, 2500):
                                call OutfitShame(JeanX,11,1)
                    "Повседневка 2" if ApprovalCheck(JeanX, 2500):
                                call OutfitShame(JeanX,12,1)
                    #8 is Emma's teaching clothes,
                    "Неважно":
                                pass

        "Примерь розовую рубашку и брюки":
                $ JeanX.OutfitChange("casual1")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                            $ JeanX.Outfit = "casual1"
                            $ JeanX.Shame = 0
                            ch_j "Ага, я уже давно ношу их."
                    "Давай попробуем что-нибудь другое.":
                            ch_j "Конечно. . ."

        "Примерь зелёную футболку и юбку":
                $ JeanX.OutfitChange("casual2")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                            $ JeanX.Outfit = "casual2"
                            $ JeanX.Shame = 0
                            ch_j "Ладно, мне нравится ходить в этом. . ."
                    "Давай попробуем что-нибудь другое.":
                            ch_j "Конечно. . ."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not JeanX.Custom1[0] and not JeanX.Custom2[0] and not JeanX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if JeanX.Custom1[0] or JeanX.Custom2[0] or JeanX.Custom3[0]:
                $ Cnt = 0
                while 1:
                    menu:
                        "Надень Пользовательский 1 (locked)" if not JeanX.Custom1[0]:
                                pass
                        "Надень Пользовательский 1" if JeanX.Custom1[0]:
                                $ JeanX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Надень Пользовательский 2 (locked)" if not JeanX.Custom2[0]:
                                pass
                        "Надень Пользовательский 2" if JeanX.Custom2[0]:
                                $ JeanX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Надень Пользовательский 3 (locked)" if not JeanX.Custom3[0]:
                                pass
                        "Надень Пользовательский 3" if JeanX.Custom3[0]:
                                $ JeanX.OutfitChange("custom3")
                                $ Cnt = 6

                        "Ты должна одеваться так, когда мы наедине (locked)" if not Cnt:
                                pass
                        "Ты должна одеваться так, когда мы наедине" if Cnt:
                                if Cnt == 5:
                                    $ JeanX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ JeanX.Clothing[9] = "custom3"
                                else:
                                    $ JeanX.Clothing[9] = "custom1"
                                ch_j "Конечно."

                        "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                menu:
                                    "Пользовательский 1 [[очистить слот 1]" if JeanX.Custom1[0]:
                                        ch_j "Ладно."
                                        $ JeanX.Custom1[0] = 0
                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not JeanX.Custom1[0]:
                                        pass
                                    "Пользовательский 2 [[очистить слот 2]" if JeanX.Custom2[0]:
                                        ch_j "Ладно."
                                        $ JeanX.Custom2[0] = 0
                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not JeanX.Custom2[0]:
                                        pass
                                    "Пользовательский 3 [[очистить слот 3]" if JeanX.Custom3[0]:
                                        ch_j "Ладно."
                                        $ JeanX.Custom3[0] = 0
                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not JeanX.Custom3[0]:
                                        pass
                                    "Неважно [[назад].":
                                        pass

                        "Тебе следует надеть его. [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                pass
                        "Тебе следует надеть его." if Cnt:
                                call Custom_Out(JeanX,Cnt)
                        "Ладно, вернемся к началу нашего разговора. . .":
                                $ Cnt = 0
                                return #jump Jean_Clothes

        "Наденешь спортивную одежду?" if not JeanX.Taboo or bg_current == "bg dangerroom":
                $ JeanX.OutfitChange("gym")

        "Наденешь одежду для сна?" if not JeanX.Taboo:
                if ApprovalCheck(JeanX, 1200):
                        $ JeanX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(JeanX)
                        if _return:
                            $ JeanX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (JeanX.Taboo and bg_current != "bg pool" and not ApprovalCheck(JeanX, 800, TabM=2)) or not JeanX.Swim[0]:
                $ JeanX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not JeanX.Taboo or bg_current == "bg pool" or ApprovalCheck(JeanX, 800, TabM=2)) and JeanX.Swim[0]:
                $ JeanX.OutfitChange("swimwear")

        "Наденешь хэллоуинский костюм?" if "halloween" in JeanX.History:
                ch_j "Ладно."
                $ JeanX.OutfitChange("costume")

        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ JeanX.FaceChange("sexy", 1)
                $ Line = 0
                if not JeanX.Chest and not JeanX.Panties and not JeanX.Over and not JeanX.Legs and not JeanX.Hose:
                    ch_j "А то."
                elif JeanX.SeenChest and JeanX.SeenPussy and ApprovalCheck(JeanX, 1200, TabM=4):
                    ch_j "Ясно, на что ты намекаешь. . ."
                    $ Line = 1
                elif ApprovalCheck(JeanX, 2000, TabM=4):
                    ch_j "Ох. . ."
                    $ Line = 1
                elif JeanX.SeenChest and JeanX.SeenPussy and ApprovalCheck(JeanX, 1200, TabM=0):
                    ch_j "Так и есть, но давай не здесь. . ."
                elif ApprovalCheck(JeanX, 2000, TabM=0):
                    ch_j "Возможно, но давай не здесь. . ."
                elif ApprovalCheck(JeanX, 1000, TabM=0):
                    $ JeanX.FaceChange("confused", 1,Mouth="smirk")
                    ch_j "Ага, но это не для твоих глаз."
                    $ JeanX.FaceChange("bemused", 0)
                else:
                    $ JeanX.FaceChange("angry", 1)
                    ch_j "Конечно, это так."
                    if not Player.Male:
                        ch_j "Небось, хотела поглазеть?"
                    else:
                        ch_j "Небось, хотел поглазеть?"

                call expression JeanX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in JeanX.History:
                        $ Line = 0
                if Line:
                    #If she got nude. . .
                    $ JeanX.OutfitChange("nude")
                    "Она сбрасывает одежду к своим ногам."
                    call Girl_First_Topless(JeanX)
                    call Girl_First_Bottomless(JeanX,1)
                    $ JeanX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется, что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in JeanX.Traits:
                                ch_j "Мммм. . ."
                                $ JeanX.Outfit = "nude"
                                $ JeanX.Statup("Lust", 50, 10)
                                $ JeanX.Statup("Lust", 70, 5)
                                $ JeanX.Shame = 50
                            elif "nowhammy" not in JeanX.Traits or ApprovalCheck(JeanX, 800, "I") or ApprovalCheck(JeanX, 2800, TabM=0):
                                ch_j "Конечно. . ."
                                $ JeanX.Outfit = "nude"
                                $ JeanX.Shame = 50
                            else:
                                $ JeanX.FaceChange("sexy", 1)
                                $ JeanX.Eyes = "surprised"
                                ch_j "Ага, эм. . . сейчас я таким не занимаюсь. . ."

                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in JeanX.Traits:
                                ch_j "Ох, ладно. . ."
                            elif "nowhammy" not in JeanX.Traits or ApprovalCheck(JeanX, 800, "I") or ApprovalCheck(JeanX, 2800, TabM=0):
                                $ JeanX.FaceChange("bemused", 1)
                                ch_j "На секунду я подумала, что ты хочешь, чтобы я расхаживала в таком виде. . ."
                                ch_j ". . ."
                            else:
                                $ JeanX.FaceChange("confused", 1)
                                ch_j "Ага, сейчас я подобным не увлекаюсь. . ."
                $ Line = 0

        "Неважно":
            return #jump Jean_Clothes

    return #jump Jean_Clothes
    #End of Jean Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jean_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять [get_clothing_name(JeanX.Over_key, vin)]?" if JeanX.Over:
                call Wardrobe_Remove(JeanX)

        "Примерь розовую рубашку." if JeanX.Over != "pink shirt":
                $ JeanX.FaceChange("bemused")
                ch_j "Конечно."
                $ JeanX.Over = "pink shirt"

        "Примерь зеленую футболку." if JeanX.Over != "green shirt":
                $ JeanX.FaceChange("bemused")
                ch_j "Конечно."
                $ JeanX.Over = "green shirt"

        "Примерь желтую майку." if JeanX.Over != "yellow shirt" and "halloween" in JeanX.History:
                $ JeanX.FaceChange("bemused")
                ch_j "Конечно."
                $ JeanX.Over = "yellow shirt"

        "Может, просто накинешь полотенце?" if JeanX.Over != "towel":
                $ JeanX.FaceChange("bemused", 1)
                if JeanX.Chest or JeanX.SeenChest:
                    ch_j "Эм, ладно. . ."
                elif ApprovalCheck(JeanX, 1000, TabM=0):
                    $ JeanX.FaceChange("perplexed", 1)
                    ch_j "Хм, ладно. . ."
                else:
                    call Display_DressScreen(JeanX)
                    if not _return:
                            ch_j "Я буду выглядеть нелепо."
                            return #jump Jean_Clothes
                $ JeanX.Over = "towel"

        "Неважно":
            pass
    return #jump Jean_Clothes
    #End of Jean Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Jean_NoBra:
        menu:
            ch_j "Сейчас на мне нет лифчика."
            "Тогда надень какой-нибудь. . .":
                        if ApprovalCheck(JeanX, 1200, TabM=4) or (JeanX.SeenChest and ApprovalCheck(JeanX, 1000, TabM=3)):
                                $ JeanX.Blush = 1
                                ch_j "Ну, не то, чтобы мне это сильно было нужно. . ."
                                $ JeanX.Blush = 0
                        elif ApprovalCheck(JeanX, 900, TabM=2) and "lace bra" in JeanX.Inventory:
                                ch_j "Думаю, я смогу что-нибудь подобрать."
                                $ JeanX.Chest  = "lace bra"
                                "Она достает свой кружевной лифчик и надевает его под [get_clothing_name(JeanX.Over_key, vin)]."
                        elif ApprovalCheck(JeanX, 700, TabM=2):
                                ch_j "Думаю, я смогу что-нибудь подобрать."
                                $ JeanX.Chest  = "green bra"
                                "Она достает свой зеленый лифчик и надевает его под [get_clothing_name(JeanX.Over_key, vin)]."
                        else:
                                ch_j "Ага, я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(JeanX, 1100, "LI", TabM=2) and JeanX.Love > JeanX.Inbt:
                                ch_j "Согласна. . ."
                        elif ApprovalCheck(JeanX, 700, "OI", TabM=2) and JeanX.Obed > JeanX.Inbt:
                                ch_j "Конечно. . ."
                        elif ApprovalCheck(JeanX, 600, "I", TabM=2):
                                ch_j "Ага. . ."
                        elif ApprovalCheck(JeanX, 1300, TabM=2):
                                ch_j "Ладно."
                        else:
                                $ JeanX.FaceChange("surprised")
                                $ JeanX.Brows = "angry"
                                if JeanX.Taboo > 20:
                                    ch_j ". . . Но не в данный момент. . ."
                                else:
                                    ch_j "Ха! Не для тебя, [JeanX.Petname]."
                                call expression JeanX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0
            "Неважно.":
                        ch_j "Ладно. . ."
                        return 0
        return 1
        #End of Jean bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jean_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(JeanX.Legs_key, vin)]?" if JeanX.Legs:
                call Wardrobe_Remove(JeanX,1)

        "Тебе отлично подходят брюки цвета хаки." if JeanX.Legs != "pants":
                ch_j "Ага, я знаю."
                $ JeanX.Legs = "pants"

        "Тебе отлично подходят штаны для йоги." if JeanX.Legs != "yoga pants":
                if ApprovalCheck(JeanX, 800, TabM=4):
                        ch_j "Ага, я знаю."
                        $ JeanX.Legs = "yoga pants"
                else:
                    call Display_DressScreen(JeanX)
                    if not _return:
                        ch_j "Они. . . неудобные."

        "Как насчет примерить зеленую юбочку?" if JeanX.Legs != "skirt":
                ch_j "Конечно, почему нет."
                $ JeanX.Legs = "skirt"

        "Ты отлично выглядишь в шортах." if JeanX.Legs != "shorts" and "halloween" in JeanX.History:
                ch_j "Ага, я знаю."
                $ JeanX.Legs = "shorts"

        "Сними обувь (locked)" if not JeanX.Boots:
                pass
        "Сними [get_clothing_name(JeanX.Boots_key, vin)]" if JeanX.Boots:
                ch_p "Может, снимешь [get_clothing_name(JeanX.Boots_key, vin)]?"
                ch_j "Конечно, почему нет."
                $ JeanX.Boots = 0
#        "Add Boots" if JeanX.Boots != "boots":
#                ch_p "Maybe put your boots on."
#                ch_j "Sure, why not."
#                $ JeanX.Boots = "boots"
        "Надень сандалии" if JeanX.Boots != "sandals":
                ch_p "Может, наденешь сандалии?"
                ch_j "Конечно, почему нет."
                $ JeanX.Boots = "sandals"

        "Неважно":
                pass
    return #jump Jean_Clothes
    #End of Jean Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Jean_NoPantiesOn:
        menu:
            ch_j "В данный момент на мне нет трусиков."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if ApprovalCheck(JeanX, 1500, TabM=4) or (JeanX.SeenPussy and ApprovalCheck(JeanX, 1100, TabM=4)):
                                $ JeanX.Blush = 1
                                ch_j "Нет, мне и без них хорошо. . ."
                                $ JeanX.Blush = 0
                        elif ApprovalCheck(JeanX, 700, TabM=4):
                                ch_j "Ага, наверное, так и сделаю."
                                if "lace panties" in JeanX.Inventory:
                                        $ JeanX.Panties  = "lace panties"
                                else:
                                        $ JeanX.Panties = "green panties"
                                if ApprovalCheck(JeanX, 1200, TabM=4):
                                    $ Line = get_clothing_name(JeanX.Legs_key, vin)
                                    $ JeanX.Legs = 0
                                    "Она снимает [Line] и натягивает [get_clothing_name(JeanX.Panties_key, vin)]."
                                elif JeanX.Legs == "skirt":
                                    "Она достает [get_clothing_name(JeanX.Panties_key, vin)] и натягивает их под юбку."
                                    $ JeanX.Legs = 0
                                    "Затем она скидывает юбку на пол."
                                else:
                                    $ Line = get_clothing_name(JeanX.Legs_key, vin)
                                    $ JeanX.Legs = 0
                                    "Она отходит на мгновение, а затем возвращается в [get_clothing_name(JeanX.Panties_key, pre)]."
                                return #jump Jean_Clothes
                        else:
                                ch_j "Не-а."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(JeanX, 1100, "LI", TabM=3) and JeanX.Love > JeanX.Inbt:
                                ch_j "Верно. . ."
                        elif ApprovalCheck(JeanX, 700, "OI", TabM=3) and JeanX.Obed > JeanX.Inbt:
                                ch_j "Да. . ."
                        elif ApprovalCheck(JeanX, 600, "I", TabM=3):
                                ch_j "Хммм. . ."
                        elif ApprovalCheck(JeanX, 1300, TabM=3):
                                ch_j "Ладно."
                        else:
                                $ JeanX.FaceChange("surprised")
                                $ JeanX.Brows = "angry"
                                if JeanX.Taboo > 20:
                                    ch_j ". . . Не сейчас. . ."
                                else:
                                    ch_j "Ха! Не для тебя, [JeanX.Petname]."
                                call expression JeanX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно.":
                ch_j "Ладно. . ."
                return 0
        return 1
        #End of Jean Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jean_Clothes_Under:
        "Верх":
            menu:
                "Может, снимешь [get_clothing_name(JeanX.Chest_key, vin)]?" if JeanX.Chest:
                        $ JeanX.FaceChange("bemused", 1)
                        if JeanX.SeenChest and ApprovalCheck(JeanX, 900, TabM=2.7):
                            ch_j "Ладно."
                        elif ApprovalCheck(JeanX, 1100, TabM=2):
                            if JeanX.Taboo:
                                ch_j "Я не уверена, не здесь. . ."
                            else:
                                ch_j "Может быть. . ."
                        elif JeanX.Over and ApprovalCheck(JeanX, 500, TabM=2):
                            ch_j "Думаю, можно. . ."
                        elif not JeanX.Over:
                            call Display_DressScreen(JeanX)
                            if not _return:
                                ch_j "Я не хочу показывать тебе сиськи."
                                return #jump Jean_Clothes
                        else:
                            call Display_DressScreen(JeanX)
                            if not _return:
                                ch_j "Не-а."
                                return #jump Jean_Clothes
                        $ Line = get_clothing_name(JeanX.Chest_key, vin)
                        $ JeanX.Chest = 0
                        if JeanX.Over:
                            "Она залазит под [get_clothing_name(JeanX.Over_key, vin)], хватает и снимает [Line], а затем кидает на пол."
                        else:
                            "Она снимает [Line] и кидает на пол."
                            if not renpy.showing('DressScreen'):
                                call Girl_First_Topless(JeanX)


                "Примерь зеленый лифчик." if JeanX.Chest != "green bra":
                        ch_j "Ладно."
                        $ JeanX.Chest = "green bra"

                "Примерь спортивный лифчик." if JeanX.Chest != "sports bra":
                        ch_j "Ладно."
                        $ JeanX.Chest = "sports bra"

                "Мне нравится твой кружевной лифчик." if JeanX.Chest != "lace bra" and "lace bra" in JeanX.Inventory :
                        if JeanX.SeenChest or ApprovalCheck(JeanX, 1300, TabM=2):
                            ch_j "Конечно."
                            $ JeanX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(JeanX)
                            if not _return:
                                ch_j "Он слегка просвечивает. . ."
                            else:
                                $ JeanX.Chest = "lace bra"

                "Мне нравится твой черный корсет." if JeanX.Chest != "corset" and "corset" in JeanX.Inventory :
                        if JeanX.SeenChest or ApprovalCheck(JeanX, 1000, TabM=1):
                            ch_j "Конечно."
                            $ JeanX.Chest = "corset"
                        else:
                            call Display_DressScreen(JeanX)
                            if not _return:
                                ch_j "Он слегка откровенный. . ."
                            else:
                                $ JeanX.Chest = "corset"

                "Мне нравится твой кружевной корсет." if JeanX.Chest != "lace corset" and "lace corset" in JeanX.Inventory :
                        if JeanX.SeenChest or ApprovalCheck(JeanX, 1300, TabM=2):
                            ch_j "Конечно."
                            $ JeanX.Chest = "lace corset"
                        else:
                            call Display_DressScreen(JeanX)
                            if not _return:
                                ch_j "Он слегка просвечивает. . ."
                            else:
                                $ JeanX.Chest = "lace corset"

                "Мне нравится твой лифчик бикини." if JeanX.Chest != "bikini top" and "bikini top" in JeanX.Inventory:
                        if bg_current == "bg pool":
                                ch_j "Конечно."
                                $ JeanX.Chest = "bikini top"
                        else:
                                if JeanX.SeenChest or ApprovalCheck(JeanX, 1000, TabM=2):
                                    ch_j "Конечно."
                                    $ JeanX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(JeanX)
                                    if not _return:
                                            ch_j "Здесь не место для \"бикини\". . ."
                                    else:
                                            $ JeanX.Chest = "bikini top"
                "Неважно":
                        pass
            return #jump Jean_Clothes_Under

        "Варианты колготок и чулок":
            menu:
                "Сними [get_clothing_name(JeanX.Hose_key, vin)]." if JeanX.Hose:# and JeanX.Hose != 'ripped tights' and JeanX.Hose != 'tights':
                                $ JeanX.Hose = 0
                "Чулки дополнили бы твой образ." if JeanX.Hose != "stockings":
                                $ JeanX.Hose = "stockings"
                "Колготки дополнили бы твой образ." if JeanX.Hose != "pantyhose" and "pantyhose" in JeanX.Inventory:
                                $ JeanX.Hose = "pantyhose"
                "Рваные колготки дополнили бы твой образ." if JeanX.Hose != "ripped pantyhose" and "ripped pantyhose" in JeanX.Inventory:
                                $ JeanX.Hose = "ripped pantyhose"
                "Чулки и пояс с подвязками дополнили бы твой образ." if JeanX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in JeanX.Inventory:
                                $ JeanX.Hose = "stockings and garterbelt"
                "Может, наденешь только пояс с подвязками?" if JeanX.Hose != "garterbelt" and "stockings and garterbelt" in JeanX.Inventory:
                                $ JeanX.Hose = "garterbelt"
                "Неважно":
                        pass
            return #jump Jean_Clothes_Under

        #Panties
        "Низ":
            menu:
                "Ты должна снять [get_clothing_name(JeanX.Panties_key, vin)]. . ." if JeanX.Panties:
                        $ JeanX.FaceChange("bemused", 1)
                        if ApprovalCheck(JeanX, 900) and (JeanX.Legs or (JeanX.SeenPussy and not JeanX.Taboo)):
                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                                if ApprovalCheck(JeanX, 850, "L"):
                                        ch_j "Верно. . ."
                                elif ApprovalCheck(JeanX, 500, "O"):
                                        ch_j "Согласна."
                                elif ApprovalCheck(JeanX, 350, "I"):
                                        ch_j "Хех."
                                else:
                                        ch_j "Конечно."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(JeanX, 1100, "LI", TabM=3) and JeanX.Love > JeanX.Inbt:
                                        ch_j "Слушай, дело не в тебе, но. . ."
                                elif ApprovalCheck(JeanX, 700, "OI", TabM=3) and JeanX.Obed > JeanX.Inbt:
                                        ch_j "Хорошо. . ."
                                elif ApprovalCheck(JeanX, 600, "I", TabM=3):
                                        ch_j "Хмммм. . ."
                                elif ApprovalCheck(JeanX, 1300, TabM=3):
                                        ch_j "Ладно-ладно."
                                else:
                                        call Display_DressScreen(JeanX)
                                        if not _return:
                                            $ JeanX.FaceChange("surprised")
                                            $ JeanX.Brows = "angry"
                                            if JeanX.Taboo > 20:
                                                ch_j ". . . Не сейчас. . ."
                                            else:
                                                ch_j "Ха! Нет, [JeanX.Petname]."
                                            return #jump Jean_Clothes
                        $ Line = get_clothing_name(JeanX.Panties_key, vin)
                        $ JeanX.Panties = 0
                        if not JeanX.Legs:
                            "Она стягивает свои [Line], затем бросает их на пол."
                            if not renpy.showing('DressScreen'):
                                    call Girl_First_Bottomless(JeanX)
                        elif ApprovalCheck(JeanX, 1200, TabM=4):
                            $ Trigger = JeanX.Legs
                            $ JeanX.Legs = 0
                            pause 0.5
                            $ JeanX.Legs = Trigger
                            "Она снимает [get_clothing_name(JeanX.Legs_key, vin)] и [Line], а затем снова надевает [get_clothing_name(JeanX.Legs_key, vin)]."
                            $ Trigger = 1
                            call Girl_First_Bottomless(JeanX,1)
                        elif JeanX.Legs == "skirt":
                            "Она залезает под юбку и стягивает [Line]."
                        else:
                            $ JeanX.Blush = 1
                            "Она на мгновение отходит, а затем возвращается."
                            $ JeanX.Blush = 0
                        $ Line = 0

                "Почему бы тебе вместо этих не надеть зеленые трусики?" if JeanX.Panties and JeanX.Panties != "green panties":
                        if ApprovalCheck(JeanX, 1100, TabM=3):
                                ch_j "Конечно."
                                $ JeanX.Panties = "green panties"
                        else:
                                call Display_DressScreen(JeanX)
                                if not _return:
                                        ch_j "Ты слишком много на себя берешь."
                                else:
                                        $ JeanX.Panties = "green panties"

                "Почему бы тебе вместо этих не надеть кружевные трусики?" if "lace panties" in JeanX.Inventory and JeanX.Panties and JeanX.Panties != "lace panties":
                        if ApprovalCheck(JeanX, 1300, TabM=3):
                                ch_j "Ладно."
                                $ JeanX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(JeanX)
                                if not _return:
                                        ch_j "Ты слишком много на себя берешь."
                                else:
                                        $ JeanX.Panties = "lace panties"

                "Мне нравятся твои трусики бикини." if "bikini bottoms" in JeanX.Inventory and JeanX.Panties != "bikini bottoms":
                        if bg_current == "bg pool":
                                ch_j "Конечно."
                                $ JeanX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(JeanX, 1000, TabM=2):
                                    ch_j "Конечно."
                                    $ JeanX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(JeanX)
                                    if not _return:
                                            ch_j "Здесь не место для \"бикини\". . ."
                                    else:
                                            $ JeanX.Panties = "bikini bottoms"

                "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not JeanX.Panties:
                        $ JeanX.FaceChange("bemused", 1)
                        if JeanX.Legs and (JeanX.Love+JeanX.Obed) <= (2 * JeanX.Inbt):
                            $ JeanX.Mouth = "smile"
                            ch_j "Я -могла- бы, но лучше не буду. . ."
                            menu:
                                "Ну ладно.":
                                    return #jump Jean_Clothes
                                "Я настаиваю, надевай.":
                                    if (JeanX.Love+JeanX.Obed) <= (1.5 * JeanX.Inbt):
                                        $ JeanX.FaceChange("angry", Eyes="side")
                                        ch_j "Ладно, мне все равно."
                                        return #jump Jean_Clothes
                                    else:
                                        $ JeanX.FaceChange("sadside")
                                        ch_j "Ох, ладно."
                        else:
                            ch_j "Думаю, можно. . ."
                        menu:
                            extend ""
                            "Как насчет зеленых?":
                                    ch_j "Конечно."
                                    $ JeanX.Panties = "green panties"
                            "Как насчет кружевных?" if "lace panties" in JeanX.Inventory:
                                    ch_j "Ладно."
                                    $ JeanX.Panties  = "lace panties"
                "Неважно":
                    pass
            return #jump Jean_Clothes_Under
        "Неважно":
            pass
    return #jump Jean_Clothes
    #End of Jean Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jean_Clothes_Misc:
        #Misc
        "Тебе идут сухие волосы." if JeanX.Hair == "wet":
                ch_p "Тебе идут сухие волосы."
                if ApprovalCheck(JeanX, 600):
                    ch_j "Ладно."
                    $ JeanX.Hair = "short"
                else:
                    ch_j "Не знаю, мне и так хорошо."

        "Тебе идут влажные волосы" if JeanX.Hair != "wet":
                ch_p "Тебе идут влажные волосы."
                if ApprovalCheck(JeanX, 800):
                    ch_j "Хмм?"
                    $ JeanX.Hair = "wet"
                    "Она отходит на минуту и вскоре возвращается."
                    ch_j "Типа так?"
                else:
                    ch_j "Уф, мне лень."

        "Мне нравится, когда твои волосы собраны в хвост" if JeanX.Hair != "pony" and "halloween" in JeanX.History:
                ch_p "Думаю, тебе стоит собрать свои волосы в хвост."
                if ApprovalCheck(JeanX, 600):
                    ch_j "Ладно."
                    $ JeanX.Hair = "pony"
                else:
                    ch_j "Не знаю, мне и так хорошо."
        "Распусти волосы." if JeanX.Hair == "pony":
                ch_p "Можешь распустить хвост."
                if ApprovalCheck(JeanX, 600):
                    ch_j "Ладно."
                    $ JeanX.Hair = "short"
                else:
                    ch_j "Не знаю, мне и так хорошо."

        "Отрасти волосы на лобке." if not JeanX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может, отрастишь?"
                call expression JeanX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in JeanX.Todo:
                        $ JeanX.FaceChange("bemused", 1)
                        ch_j "Дай мне время. . ."
                else:
                        $ JeanX.FaceChange("bemused", 1)
                        if ApprovalCheck(JeanX, 1000, TabM=0):
                            ch_j "Конечно. . ."
                        else:
                            $ JeanX.FaceChange("surprised")
                            $ JeanX.Brows = "angry"
                            ch_j "Тебя это не касается."
                            return #jump Jean_Clothes
                        $ JeanX.Todo.append("pubes")
                        $ JeanX.PubeC = 6
        "Побрей лобок." if JeanX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression JeanX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ JeanX.FaceChange("bemused", 1)
                if "shave" in JeanX.Todo:
                    ch_j "Ага, я знаю, скоро этим займусь."
                else:
                    if ApprovalCheck(JeanX, 1100, TabM=0):
                        ch_j "Неужели? Думаю, я могла бы побрить его. . ."
                    else:
                        $ JeanX.FaceChange("surprised")
                        $ JeanX.Brows = "angry"
                        ch_j "Тебя это не касается."
                        return #jump Jean_Clothes
                    $ JeanX.Todo.append("shave")

        "Пирсинг. [[Сначала посмотрите, как она выглядит без него] (locked)" if not JeanX.SeenPussy and not JeanX.SeenChest:
            pass

        "Надень пирсинг-кольца." if JeanX.Pierce != "ring" and (JeanX.SeenPussy or JeanX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-кольцами."
                if "ring" in JeanX.Todo:
                    ch_j "Ага, я знаю, скоро я этим займусь."
                else:
                    $ JeanX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(JeanX, 1150, TabM=0)
                    if ApprovalCheck(JeanX, 900, "L", TabM=0) or (Approval and JeanX.Love > 2* JeanX.Obed):
                        ch_j "Думаешь, он и правда меня скрасит?"
                    elif ApprovalCheck(JeanX, 600, "I", TabM=0) or (Approval and JeanX.Inbt > JeanX.Obed):
                        ch_j "Как-то я уже подумывала его сделать."
                    elif ApprovalCheck(JeanX, 500, "O", TabM=0) or Approval:
                        ch_j "Конечно, [JeanX.Petname]."
                    else:
                        $ JeanX.FaceChange("surprised")
                        $ JeanX.Brows = "angry"
                        ch_j "Меня это не интересует, [JeanX.Petname]."
                        return #jump Jean_Clothes
                    $ JeanX.Todo.append("ring")

        "Надень пирсинг-штанги" if JeanX.Pierce != "barbell" and (JeanX.SeenPussy or JeanX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in JeanX.Todo:
                    ch_j "Ага, я знаю, скоро этим займусь."
                else:
                    $ JeanX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(JeanX, 1150, TabM=0)
                    if ApprovalCheck(JeanX, 900, "L", TabM=0) or (Approval and JeanX.Love > 2 * JeanX.Obed):
                        ch_j "Думаешь, он и правда меня скрасит?"
                    elif ApprovalCheck(JeanX, 600, "I", TabM=0) or (Approval and JeanX.Inbt > JeanX.Obed):
                        ch_j "Как-то я уже подумывала его сделать."
                    elif ApprovalCheck(JeanX, 500, "O", TabM=0) or Approval:
                        ch_j "Конечно, [JeanX.Petname]."
                    else:
                        $ JeanX.FaceChange("surprised")
                        $ JeanX.Brows = "angry"
                        ch_j "Меня это не интересует, [JeanX.Petname]."
                        return #jump Jean_Clothes
                    $ JeanX.Todo.append("barbell")

        "Сними пирсинг" if JeanX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ JeanX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(JeanX, 1350, TabM=0)
                if ApprovalCheck(JeanX, 950, "L", TabM=0) or (Approval and JeanX.Love > JeanX.Obed):
                    ch_j "Определись уже. . ."
                elif ApprovalCheck(JeanX, 700, "I", TabM=0) or (Approval and JeanX.Inbt > JeanX.Obed):
                    ch_j "Что?"
                elif ApprovalCheck(JeanX, 600, "O", TabM=0) or Approval:
                    ch_j "Ладно."
                else:
                    $ JeanX.FaceChange("surprised")
                    $ JeanX.Brows = "angry"
                    ch_j "Не знаю, теперь он, вроде как, мне нравятся. . ."
                    return #jump Jean_Clothes
                $ JeanX.Pierce = 0

        "Надень подтяжки" if JeanX.Acc != "suspenders" and JeanX.Acc != "suspenders2" and "halloween" in JeanX.History:
                $ JeanX.Acc = "suspenders"
        "Сними подтяжки" if JeanX.Acc == "suspenders" or JeanX.Acc == "suspenders2":
                $ JeanX.Acc = 0

        "Сдвинь подтяжки" if JeanX.Acc == "suspenders" or JeanX.Acc == "suspenders2":
                $ JeanX.Acc = "suspenders" if JeanX.Acc == "suspenders2" else "suspenders2"

#        "Why don't you try on that medallion choker." if JeanX.Neck != "leash choker":
#                ch_j "Ok. . ."
#                $ JeanX.Neck = "leash choker"
#        "Maybe go without a necklace." if JeanX.Neck:
#                ch_j "Ok. . ."
#                $ JeanX.Neck = 0

#        "Why don't you put those wristbands on." if JeanX.Arms != "wrists":
#                ch_j "Ok. . ."
#                $ JeanX.Arms = "wrists"
#        "Maybe go without the wristbands." if JeanX.Arms:
#                ch_j "Ok. . ."
#                $ JeanX.Arms = 0

        "Неважно":
            pass
    return #jump Jean_Clothes
    #End of Jean Misc Wardrobe

return
#End Jean Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
