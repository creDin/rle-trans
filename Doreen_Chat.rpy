# star Doreen chat interface
#Doreen Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Doreen_Relationship: #rkeljsvgb
    while True:
        menu:
            ch_d "О чем ты хочешь поговорить?"
            "Хочешь стать моей девушкой?" if DoreenX not in Player.Harem and "ex" not in DoreenX.Traits:
                    $ DoreenX.DailyActions.append("relationship")
                    if "asked boyfriend" in DoreenX.DailyActions and "angry" in DoreenX.DailyActions:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Пожалуйста, перестань спрашивать."
                            return
                    elif "asked boyfriend" in DoreenX.DailyActions:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Я все еще не думаю, что это была бы хорошая идея."
                            return
                    elif DoreenX.Break[0]:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Нет, если ты все еще хочешь встречаться с другими девушками."
                            if Player.Harem:
                                    $ DoreenX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "Я уже ни с кем не встречаюсь."

                    $ DoreenX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "DoreenYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_d "Остальные не возражают, [DoreenX.Petname]?"
                        else:
                            ch_d "А [Player.Harem[0].Name] не возражает, [DoreenX.Petname]?"
                        return

                    if DoreenX.Event[5]:
                            $ DoreenX.FaceChange("bemused", 1)
                            if not Player.Male:
                                ch_d "Когда я предлагала, ты ответила мне \"нет\". . ."
                            else:
                                ch_d "Когда я предлагала, ты ответил мне \"нет\". . ."
                    else:
                            $ DoreenX.FaceChange("surprised", 2)
                            ch_d "Что? . ."
                            $ DoreenX.FaceChange("smile", 1)

                    call Doreen_OtherWoman

                    if DoreenX.Love >= 800:
                            $ DoreenX.FaceChange("surprised", 1)
                            $ DoreenX.Mouth = "smile"
                            if not DoreenX.Event[5]:
                                    $ DoreenX.Statup("Love", 200, 10)
                                    call Doreen_BF
                                    return
                            $ DoreenX.Statup("Love", 200, 40)
                            ch_d "Конечно!"
                            if "boyfriend" not in DoreenX.Petnames:
                                    $ DoreenX.Petnames.append("boyfriend")
                            if "DoreenYes" in Player.Traits:
                                    $ Player.Traits.remove("DoreenYes")
                            $ Player.Harem.append(DoreenX)
                            call Harem_Initiation
                            "[DoreenX.Name] обнимает вас и крепко целует."
                            $ DoreenX.FaceChange("kiss", 1)
                            $ DoreenX.Kissed += 1
                    elif DoreenX.Obed >= 500:
                            $ DoreenX.FaceChange("perplexed")
                            ch_d "Я не уверена, хочу ли я \"встречаться\". . ."
                    elif DoreenX.Inbt >= 500:
                            $ DoreenX.FaceChange("smile")
                            ch_d "Мне нравятся свободные отношения."
                    else:
                            $ DoreenX.FaceChange("perplexed", 1)
                            ch_d "Я. . . я не готова, [DoreenX.Petname]."

            "Может, начнем все сначала?" if "ex" in DoreenX.Traits:
                    $ DoreenX.DailyActions.append("relationship")
                    if "asked boyfriend" in DoreenX.DailyActions and "angry" in DoreenX.DailyActions:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Пожалуйста, перестань спрашивать."
                            return
                    elif "asked boyfriend" in DoreenX.DailyActions:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Извини, но нет."
                            return

                    $ DoreenX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "DoreenYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_d "Остальные не возражают против этого, [DoreenX.Petname]?"
                            else:
                                ch_d "А [Player.Harem[0].Name] не возражает, [DoreenX.Petname]?"
                            return

                    $ Cnt = 0
                    call Doreen_OtherWoman

                    if DoreenX.Love >= 800:
                            $ DoreenX.FaceChange("surprised", 1)
                            $ DoreenX.Mouth = "smile"
                            $ DoreenX.Statup("Love", 90, 5)
                            ch_d "Думаю, я могу дать тебе еще один шанс."
                            if "boyfriend" not in DoreenX.Petnames:
                                        $ DoreenX.Petnames.append("boyfriend")
                            $ DoreenX.Traits.remove("ex")
                            if "DoreenYes" in Player.Traits:
                                    $ Player.Traits.remove("DoreenYes")
                            $ Player.Harem.append(DoreenX)
                            call Harem_Initiation
                            "[DoreenX.Name] притягивает вас к себе и крепко целует."
                            $ DoreenX.FaceChange("kiss", 1)
                            $ DoreenX.Kissed += 1
                    elif DoreenX.Love >= 600 and ApprovalCheck(DoreenX, 1500):
                            $ DoreenX.FaceChange("smile", 1)
                            $ DoreenX.Statup("Love", 90, 5)
                            ch_d ". . . конечно."
                            if "boyfriend" not in DoreenX.Petnames:
                                    $ DoreenX.Petnames.append("boyfriend")
                            $ DoreenX.Traits.remove("ex")
                            if "DoreenYes" in Player.Traits:
                                    $ Player.Traits.remove("DoreenYes")
                            $ Player.Harem.append(DoreenX)
                            call Harem_Initiation
                            $ DoreenX.FaceChange("kiss", 1)
                            "[DoreenX.Name] дарит вам легкий поцелуй."
                            $ DoreenX.FaceChange("sly", 1)
                            $ DoreenX.Kissed += 1
                    elif DoreenX.Obed >= 500:
                            $ DoreenX.FaceChange("sad")
                            ch_d "Не думаю, что между нами была химия. . ."
                    elif DoreenX.Inbt >= 500:
                            $ DoreenX.FaceChange("perplexed")
                            ch_d "Теперь это в прошлом."
                    else:
                            $ DoreenX.FaceChange("sadside", 1)
                            ch_d "Не думаю, что готова пройти через все это снова. . ."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if DoreenX in Player.Harem:
                            call AskDateOther

            "Думаю, мы должны расстаться." if DoreenX in Player.Harem:
                            if "breakup talk" in DoreenX.RecentActions:
                                    ch_d "Пожалуйста, перестань спрашивать об этом."
                            elif "breakup talk" in DoreenX.DailyActions:
                                    ch_d "Снова?"
                                    ch_d "Хватит, [DoreenX.Petname]."
                            else:
                                    call Breakup(DoreenX)

            "О разговоре, который у нас был ранее. . .":
                menu:
                    "Помнишь, ты признавалась мне в любви. . ?" if "lover" not in DoreenX.Traits and DoreenX.Event[6] >= 20 and DoreenX.Event[6] != 23:
                            call Doreen_Love_Redux

                    "Помнишь, ты рассказывала мне о себе. . ?" if "lover" not in DoreenX.Traits and DoreenX.Event[6] == 23:
                            call Doreen_Love_Redux

                    "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировала?" if "sir" not in DoreenX.Petnames and "sir" in DoreenX.History and not Player.Male:
                            if "asked sub" in DoreenX.RecentActions:
                                    ch_d "Пожалуйста, перестань спрашивать об этом."
                            elif "asked sub" in DoreenX.DailyActions:
                                    ch_d "Хватит, [DoreenX.Petname]."
                            else:
                                    call Doreen_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировал?" if "sir" not in DoreenX.Petnames and "sir" in DoreenX.History and Player.Male:
                            if "asked sub" in DoreenX.RecentActions:
                                    ch_d "Пожалуйста, перестань спрашивать об этом."
                            elif "asked sub" in DoreenX.DailyActions:
                                    ch_d "Хватит, [DoreenX.Petname]."
                            else:
                                    call Doreen_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоей хозяйкой?" if "master" not in DoreenX.Petnames and "master" in DoreenX.History and not Player.Male:
                            if "asked sub" in DoreenX.RecentActions:
                                    ch_d "Пожалуйста, перестань спрашивать об этом."
                            elif "asked sub" in DoreenX.DailyActions:
                                    ch_d "Хватит, [DoreenX.Petname]."
                            else:
                                    call Doreen_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я стал твоим хозяином?" if "master" not in DoreenX.Petnames and "master" in DoreenX.History and Player.Male:
                            if "asked sub" in DoreenX.RecentActions:
                                    ch_d "Пожалуйста, перестань спрашивать об этом."
                            elif "asked sub" in DoreenX.DailyActions:
                                    ch_d "Хватит, [DoreenX.Petname]."
                            else:
                                    call Doreen_Sub_Asked
                    "Неважно":
                            pass

            "Неважно":
                return

    return

label Doreen_OtherWoman(Cnt = 0): #rkeljsvgb
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((DoreenX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ DoreenX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_d "Я заметила, что ты теперь с [Player.Harem[0].Name_tvo] и кучей других, да?"
    else:
        ch_d "Я заметила, что ты теперь с [Player.Harem[0].Name_tvo], да?"
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "DoreenYes" in Player.Traits:
                if ApprovalCheck(DoreenX, 1800, Bonus = Cnt):
                        $ DoreenX.FaceChange("smile", 1)
                        if DoreenX.Love >= DoreenX.Obed:
                                ch_d "Думаю, тогда мы можем перейти на новый уровень отношений."
                        elif DoreenX.Obed >= DoreenX.Inbt:
                                ch_d "Думаю, тогда мы можем перейти на новый уровень отношений."
                        else:
                                ch_d "Думаю, тогда мы можем перейти на новый уровень отношений."
                else:
                        $ DoreenX.FaceChange("sad", 1)
                        ch_d "Ну. . . даже если и так, я не могу."
                        $ renpy.pop_call()
                        #This causes it to jump past the previous menu on the return

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "DoreenYes" not in Player.Traits and not Player.Male:
                if ApprovalCheck(DoreenX, 1800, Bonus = Cnt):
                        $ DoreenX.FaceChange("smile", 1)
#                        if DoreenX.Love >= DoreenX.Obed:
#                            ch_d "Then I may consider it. . ."
#                        elif DoreenX.Obed >= DoreenX.Inbt:
#                            ch_d "Then I may consider it. . ."
#                        else:
#                            ch_d "Then sure, why not."
                        ch_d "Ну, тогда может быть. . ."
                        ch_d "Найди меня завтра, после того как поговоришь с ней."
                else:
                        $ DoreenX.FaceChange("sad", 1)
                        ch_d "Ну. . . даже если она будет не против, я не могу."
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "DoreenYes" not in Player.Traits and Player.Male:
                if ApprovalCheck(DoreenX, 1800, Bonus = Cnt):
                        $ DoreenX.FaceChange("smile", 1)
#                        if DoreenX.Love >= DoreenX.Obed:
#                            ch_d "Then I may consider it. . ."
#                        elif DoreenX.Obed >= DoreenX.Inbt:
#                            ch_d "Then I may consider it. . ."
#                        else:
#                            ch_d "Then sure, why not."
                        ch_d "Ну, тогда может быть. . ."
                        ch_d "Найди меня завтра, после того как поговоришь с ней."
                else:
                        $ DoreenX.FaceChange("sad", 1)
                        ch_d "Ну. . . даже если она будет не против, я не могу."
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
                if ApprovalCheck(DoreenX, 1800, Bonus = -Cnt): #checks if Doreen likes you more than the other girl
                        $ DoreenX.FaceChange("smile", 1)
                        if DoreenX.Love >= DoreenX.Obed:
                                ch_d "Наверное. . ."
                        elif DoreenX.Obed >= DoreenX.Inbt:
                                ch_d "Наверное. . ."
                        else:
                                ch_d "Ох, здорово. . . здорово. . ."
                        $ DoreenX.Traits.append("downlow")
                else:
                        $ DoreenX.FaceChange("angry", 1)
                        if ApprovalCheck(DoreenX, 1800):
                                ch_d "Да ладно, это лучшее, что ты можешь предложить?"
                        else:
                                ch_d "Звучит ужасно!"
                        $ renpy.pop_call()

        "Я могу порвать с ней.":
                    $ DoreenX.FaceChange("sad")
                    ch_d "Дай мне знать, когда закончишь."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ DoreenX.FaceChange("sad")
                    ch_d "Думаешь?"
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ DoreenX.FaceChange("sad")
                    ch_d "Думаешь?"
                    $ renpy.pop_call()

    return


label Doreen_About(Check=0): #rkeljsvgb
    if Check not in TotalGirls:
            ch_d "А это кто?"
            return
    ch_d "Что я думаю о ней? Ну. . ."
    if Check == RogueX:
            if "poly Rogue" in DoreenX.Traits:
                ch_d "У нас, эм. . . думаю, у нас много общего."
            elif DoreenX.LikeRogue >= 900:
                ch_d "С ней очень весело!"
            elif DoreenX.LikeRogue >= 800:
                ch_d "Она очень милая."
            elif DoreenX.LikeRogue >= 700:
                ch_d "Она очень красивая, правда?"
            elif DoreenX.LikeRogue >= 600:
                ch_d "Она хорошая подруга."
            elif DoreenX.LikeRogue >= 500:
                ch_d "Мы особо не общались."
            elif DoreenX.LikeRogue >= 400:
                ch_d "Думаю, мы не особо нравимся друг другу."
            elif DoreenX.LikeRogue >= 300:
                ch_d "Она довольно злая."
            else:
                ch_d "Эм. . . она мне не очень нравится."
    elif Check == KittyX:
            if "poly Kitty" in DoreenX.Traits:
                ch_d "У нас, эм. . . думаю, у нас много общего."
            elif DoreenX.LikeKitty >= 900:
                ch_d "Она очень приятно пахнет!"
            elif DoreenX.LikeKitty >= 800:
                ch_d "Она такая милая!"
            elif DoreenX.LikeKitty >= 700:
                ch_d "Она прекрасно разбирается в компьютерах."
            elif DoreenX.LikeKitty >= 600:
                ch_d "Она хорошая подруга."
            elif DoreenX.LikeKitty >= 500:
                ch_d "Мы особо не общались."
            elif DoreenX.LikeKitty >= 400:
                ch_d "Думаю, мы не особо нравимся друг другу."
            elif DoreenX.LikeKitty >= 300:
                ch_d "Она довольно злая."
            else:
                ch_d "Эм. . . она мне не очень нравится."
    elif Check == LauraX:
            if "poly Laura" in DoreenX.Traits:
                ch_d "У нас, эм. . . думаю, у нас много общего."
            elif DoreenX.LikeLaura >= 900:
                ch_d "Она очень. . . энергичная."
            elif DoreenX.LikeLaura >= 800:
                ch_d "У нее великолепное тело."
            elif DoreenX.LikeLaura >= 700:
                ch_d "Я не могу за ней угнаться. . ."
            elif DoreenX.LikeLaura >= 600:
                ch_d "Она очень спортивная."
            elif DoreenX.LikeLaura >= 500:
                ch_d "Мы особо не общались."
            elif DoreenX.LikeLaura >= 400:
                ch_d "Думаю, мы не особо нравимся друг другу."
            elif DoreenX.LikeLaura >= 300:
                ch_d "Она довольно злая."
            else:
                ch_d "Эм. . . она мне не очень нравится."
    elif Check == EmmaX:
            if "poly Emma" in DoreenX.Traits:
                ch_d "У нас, эм. . . думаю, у нас много общего."
            elif DoreenX.LikeEmma >= 900:
                ch_d "Она очень красивая."
            elif DoreenX.LikeEmma >= 800:
                ch_d "Она. . . очень привлекательная. . ."
            elif DoreenX.LikeEmma >= 700:
                ch_d "Она очень стильная!"
            elif DoreenX.LikeEmma >= 600:
                ch_d "Ее приятно слушать."
            elif DoreenX.LikeEmma >= 500:
                ch_d "Она хороший преподаватель."
            elif DoreenX.LikeEmma >= 400:
                ch_d "Думаю, мы не особо нравимся друг другу."
            elif DoreenX.LikeEmma >= 300:
                ch_d "Она довольно злая."
            else:
                ch_d "Эм. . . она мне не очень нравится."
    elif Check == JeanX:
            if "poly Jean" in DoreenX.Traits:
                ch_d "У нас, эм. . . думаю, у нас много общего."
            elif DoreenX.LikeJean >= 900:
                ch_d "Иногда она бывает злой, но от этого она еще сексуальнее."
            elif DoreenX.LikeJean >= 800:
                ch_d "Мне бы очень хотелось, чтобы она не была такой стервой. . ."
            elif DoreenX.LikeJean >= 700:
                ch_d "Иногда она. . . перегибает."
            elif DoreenX.LikeJean >= 600:
                ch_d "Думаю. . . я могу к ней привыкнуть."
            elif DoreenX.LikeJean >= 500:
                ch_d "Мы особо не общались."
            elif DoreenX.LikeJean >= 400:
                ch_d "Думаю, мы не особо нравимся друг другу."
            elif DoreenX.LikeJean >= 300:
                ch_d "Она довольно злая."
            else:
                ch_d "Эм. . . она мне не очень нравится."
    elif Check == StormX:
            if "poly Storm" in DoreenX.Traits:
                ch_d "У нас, эм. . . думаю, у нас много общего."
            elif DoreenX.LikeStorm >= 900:
                ch_d "Она такая красивая."
            elif DoreenX.LikeStorm >= 800:
                ch_d "Она очень. . . добрая. . ."
            elif DoreenX.LikeStorm >= 700:
                ch_d "Она очень радушно приняла меня в этом месте."
            elif DoreenX.LikeStorm >= 600:
                ch_d "Мне нравятся ее занятия."
            elif DoreenX.LikeStorm >= 500:
                ch_d "Она достойный преподаватель."
            elif DoreenX.LikeStorm >= 400:
                ch_d "Думаю, мы не особо нравимся друг другу."
            elif DoreenX.LikeStorm >= 300:
                ch_d "Она довольно злая."
            else:
                ch_d "Эм. . . она мне не очень нравится."
    elif Check == JubesX:
            if "poly Jubes" in DoreenX.Traits:
                ch_d "У нас, эм. . . думаю, у нас много общего."
            elif DoreenX.LikeJubes >= 900:
                ch_d "У нее отличные зубы."
            elif DoreenX.LikeJubes >= 800:
                ch_d "Она очаровательна. . ."
            elif DoreenX.LikeJubes >= 700:
                ch_d "С ней очень приятно ходить по магазинам."
            elif DoreenX.LikeJubes >= 600:
                ch_d "Она очень дружелюбная."
            elif DoreenX.LikeJubes >= 500:
                ch_d "Мы особо не общались."
            elif DoreenX.LikeJubes >= 400:
                ch_d "Думаю, мы не особо нравимся друг другу."
            elif DoreenX.LikeJubes >= 300:
                ch_d "Она довольно злая."
            else:
                ch_d "Эм. . . она мне не очень нравится."
    elif Check == GwenX:
            if "poly Gwen" in DoreenX.Traits:
                ch_d "У нас, эм. . . думаю, у нас много общего."
            elif DoreenX.LikeGwen >= 900:
                ch_d "Она полна энергии."
            elif DoreenX.LikeGwen >= 800:
                ch_d "Она очень симпатичная, не правда ли?"
            elif DoreenX.LikeGwen >= 700:
                ch_d "Она очень тепло меня встретила."
            elif DoreenX.LikeGwen >= 600:
                ch_d "Как бы это сказать. . . у нас. . . парасоциальные отношения?"
            elif DoreenX.LikeGwen >= 500:
                ch_d "Мы особо не общались."
            elif DoreenX.LikeGwen >= 400:
                ch_d "Думаю, мы не особо нравимся друг другу."
            elif DoreenX.LikeGwen >= 300:
                ch_d "Она довольно злая."
            else:
                ch_d "Эм. . . она мне не очень нравится."
    elif Check == BetsyX:
            if "poly Betsy" in DoreenX.Traits:
                ch_d "У нас, эм. . . думаю, у нас много общего."
            elif DoreenX.LikeBetsy >= 900:
                ch_d "Она очень сексуальная. . ."
            elif DoreenX.LikeBetsy >= 800:
                ch_d "Она такая утонченная."
            elif DoreenX.LikeBetsy >= 700:
                ch_d "У нее отличное чувство стиля."
            elif DoreenX.LikeBetsy >= 600:
                ch_d "У нее очень приятный акцент."
            elif DoreenX.LikeBetsy >= 500:
                ch_d "Мы особо не общались."
            elif DoreenX.LikeBetsy >= 400:
                ch_d "Думаю, мы не особо нравимся друг другу."
            elif DoreenX.LikeBetsy >= 300:
                ch_d "Она довольно злая."
            else:
                ch_d "Эм. . . она мне не очень нравится."
    elif Check == WandaX:
            if "poly Wanda" in DoreenX.Traits:
                ch_d "Мы, эм. . . она -очень- умелая!"
            elif DoreenX.LikeWanda >= 900:
                ch_d "С ней очень весело находиться рядом!"
            elif DoreenX.LikeWanda >= 800:
                ch_d "Она такая хорошенькая."
            elif DoreenX.LikeWanda >= 700:
                ch_d "Она очень хорошенькая, правда?"
            elif DoreenX.LikeWanda >= 600:
                ch_d "Она отличная подруга."
            elif DoreenX.LikeWanda >= 500:
                ch_d "Честно говоря, мы почти не общались."
            elif DoreenX.LikeWanda >= 400:
                ch_d "Думаю, мы не очень нравимся друг другу."
            elif DoreenX.LikeWanda >= 300:
                ch_d "Она довольно злая."
            else:
                ch_d "Эм. . . нет, она мне не очень нравится."
    else:
                ch_d "Эм, я потом расскажу тебе о ней."
    return
#End Doreen_AboutEmma

label Doreen_Monogamy: #rkeljsvgb
        #called from Doreen_Settings to ask her not to hook up with other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in DoreenX.Traits:
                    if DoreenX.Thirst >= 60 and not ApprovalCheck(DoreenX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ DoreenX.FaceChange("sly",1)
                            if "mono" not in DoreenX.DailyActions:
                                    $ DoreenX.Statup("Obed", 90, -2)
                            ch_d "У меня, эм. . . есть кое-какие потребности. . ."
                            return
                    elif ApprovalCheck(DoreenX, 1200, "LO", TabM=0) and DoreenX.Love >= DoreenX.Obed:
                            #she cares
                            $ DoreenX.FaceChange("sly",1)
                            if "mono" not in DoreenX.DailyActions:
                                    $ DoreenX.Statup("Love", 90, 1)
                            if not Player.Male:
                                ch_d "Конечно, до тех пор, пока ты доступна."
                            else:
                                ch_d "Конечно, до тех пор, пока ты доступен."
                    elif ApprovalCheck(DoreenX, 700, "O", TabM=0):
                            #she is obedient
                            $ DoreenX.FaceChange("sly",1,Eyes="side")
                            ch_d ". . . Наверное, я могу прекратить. . ."
                    else:
                            #she doesn't care
                            $ DoreenX.FaceChange("sly",1)
                            ch_d "У меня, эм. . . есть кое-какие потребности. . ."
                            return
                    if "mono" not in DoreenX.DailyActions:
                            $ DoreenX.Statup("Obed", 90, 3)
                    $ DoreenX.AddWord(1,0,"mono") #Daily
                    $ DoreenX.Traits.append("mono")
            "Не встречайся с другими девушками." if "mono" not in DoreenX.Traits:
                    if ApprovalCheck(DoreenX, 900, "O", TabM=0):
                            #she is obedient
                            $ DoreenX.FaceChange("sly",1,Eyes="side")
                            ch_d ". . . Наверное, я могу прекратить. . ."
                    elif DoreenX.Thirst >= 60 and not ApprovalCheck(DoreenX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ DoreenX.FaceChange("sly",1)
                            if "mono" not in DoreenX.DailyActions:
                                    $ DoreenX.Statup("Obed", 90, -2)
                            ch_d "У меня, эм. . . есть кое-какие потребности. . ."
                            return
                    elif ApprovalCheck(DoreenX, 600, "O", TabM=0):
                            #she is obedient
                            $ DoreenX.FaceChange("sly",1,Eyes="side")
                            ch_d ". . . Наверное, я могу прекратить. . ."
                    elif ApprovalCheck(DoreenX, 1400, "LO", TabM=0):
                            #she cares
                            $ DoreenX.FaceChange("sly",1)
                            if not Player.Male:
                                ch_d "Конечно, до тех пор, пока ты доступна."
                            else:
                                ch_d "Конечно, до тех пор, пока ты доступен."
                    else:
                            #she doesn't care
                            $ DoreenX.FaceChange("sly",1,Brows="confused")
                            ch_d "У меня, эм. . . есть кое-какие потребности. . ."
                            return
                    if "mono" not in DoreenX.DailyActions:
                            $ DoreenX.Statup("Obed", 90, 3)
                    $ DoreenX.AddWord(1,0,"mono") #Daily
                    $ DoreenX.Traits.append("mono")
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in DoreenX.Traits:
                    if ApprovalCheck(DoreenX, 700, "O", TabM=0):
                            $ DoreenX.FaceChange("sly",1,Eyes="side")
                            ch_d "Ох, здорово!"
                    elif ApprovalCheck(DoreenX, 800, "L", TabM=0):
                            $ DoreenX.FaceChange("sly",1)
                            ch_d "Эм. . . здорово. . ."
                    else:
                            $ DoreenX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in DoreenX.DailyActions:
                                    $ DoreenX.Statup("Love", 90, -2)
                            ch_d "Ох, здорово!"
                    if "mono" not in DoreenX.DailyActions:
                            $ DoreenX.Statup("Obed", 90, 3)
                    if "mono" in DoreenX.Traits:
                            $ DoreenX.Traits.remove("mono")
                    $ DoreenX.AddWord(1,0,"mono") #Daily
            "Неважно.":
                pass
        return

# end Doreen monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Doreen_Jumped: #rkeljsvgb
        #called from Doreen_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ DoreenX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_d "Я бы сказала немного по-другому. . ."
            "На будущее, можешь сначала спрашивать?" if "chill" not in DoreenX.Traits:
                    if DoreenX.Thirst >= 60 and not ApprovalCheck(DoreenX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ DoreenX.FaceChange("sly",1)
                            if "chill" not in DoreenX.DailyActions:
                                    $ DoreenX.Statup("Obed", 90, -2)
                            ch_d "Но иначе мне не получить твоего внимания. . ."
                            return
                    elif ApprovalCheck(DoreenX, 1000, "LO", TabM=0) and DoreenX.Love >= DoreenX.Obed:
                            #she cares
                            $ DoreenX.FaceChange("surprised",1)
                            if "chill" not in DoreenX.DailyActions:
                                    $ DoreenX.Statup("Love", 90, 1)
                            if not Player.Male:
                                ch_d "Ну, было бы здорово, если бы ты приходила ко мне почаще. . ."
                            else:
                                ch_d "Ну, было бы здорово, если бы ты приходил ко мне почаще. . ."
                            $ DoreenX.FaceChange("sly",1,Eyes="side")
                            ch_d "-но я попробую. . ."
                    elif ApprovalCheck(DoreenX, 500, "O", TabM=0):
                            #she is obedient
                            $ DoreenX.FaceChange("sly",1,Eyes="side")
                            ch_d ". . . если ты этого хочешь. . ."
                    else:
                            #she doesn't care
                            $ DoreenX.FaceChange("sly",1)
                            ch_d "Все зависит от тебя. . ."
                            return
                    if "chill" not in DoreenX.DailyActions:
                            $ DoreenX.Statup("Obed", 90, 3)
                    $ DoreenX.AddWord(1,0,"chill") #Daily
                    $ DoreenX.Traits.append("chill")
            "Больше так не делай." if "chill" not in DoreenX.Traits:
                    if ApprovalCheck(DoreenX, 800, "O", TabM=0):
                            #she is obedient
                            $ DoreenX.FaceChange("sly",1,Eyes="side")
                            ch_d ". . . если ты этого хочешь."
                    elif DoreenX.Thirst >= 60 and not ApprovalCheck(DoreenX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ DoreenX.FaceChange("sly",1)
                            if "chill" not in DoreenX.DailyActions:
                                    $ DoreenX.Statup("Obed", 90, -2)
                            ch_d "Но иначе мне не получить твоего внимания. . ."
                            return
                    elif ApprovalCheck(DoreenX, 400, "O", TabM=0):
                            #she is obedient
                            $ DoreenX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_d "Да, госпожа. . ."
                            else:
                                ch_d "Да, господин. . ."
                    elif ApprovalCheck(DoreenX, 500, "LO", TabM=0) and not ApprovalCheck(DoreenX, 500, "I", TabM=0):
                            #she cares
                            $ DoreenX.FaceChange("sly",1)
                            ch_d "Я вела себя немного грубо. . ."
                            ch_d "Извини."
                    else:
                            #she doesn't care
                            $ DoreenX.FaceChange("sly",1)
                            ch_d "Не волнуйся, тебе понравится."
                            return
                    if "chill" not in DoreenX.DailyActions:
                            $ DoreenX.Statup("Obed", 90, 3)
                    $ DoreenX.AddWord(1,0,"chill") #Daily
                    $ DoreenX.Traits.append("chill")
            "Делай, что хочешь.":
                    if ApprovalCheck(DoreenX, 800, "L", TabM=0):
                            $ DoreenX.FaceChange("sly",1)
                            ch_d "Я рада!"
                    elif ApprovalCheck(DoreenX, 700, "O", TabM=0):
                            $ DoreenX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_d "Ох, конечно, госпожа."
                            else:
                                ch_d "Ох, конечно, господин."
                    else:
                            $ DoreenX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in DoreenX.DailyActions:
                                    $ DoreenX.Statup("Love", 90, -2)
                            ch_d "Ладно. . ."
                    if "chill" not in DoreenX.DailyActions:
                            $ DoreenX.Statup("Obed", 90, 3)
                    if "chill" in DoreenX.Traits:
                            $ DoreenX.Traits.remove("chill")
                    $ DoreenX.AddWord(1,0,"chill") #Daily
            "Эм, неважно.":
                pass
        return

# end Doreen jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start Doreen hungry //////////////////////////////////////////////////////////
label Doreen_Hungry: #rkeljsvgb
    if DoreenX.Chat[3]:
        ch_d "Меня мучает дикая жажда. . ."
    elif DoreenX.Chat[2]:
        ch_d "Мне очень понравился вкус твоей сыворотки . ."
    else:
        ch_d "Меня мучает дикая жажда. . ."
        ch_d "Думаю, ты знаешь почему. . ."
    $ DoreenX.Traits.append("hungry")
return


# end Doreen hungry //////////////////////////////////////////////////////////

# Doreen Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Doreen_SexChat: #rkeljsvgb
    $ Line = "Что ты хочешь обсудить?" if not Line else Line
    while True:
            menu:
                ch_d "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in DoreenX.DailyActions:
                        ch_d "Ага, я знаю."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ DoreenX.FaceChange("sly")
                                        if DoreenX.PlayerFav == "sex":
                                            $ DoreenX.Statup("Lust", 80, 5)
                                            ch_d "Я знаю. . ."
                                        elif DoreenX.Favorite == "sex":
                                            $ DoreenX.Statup("Love", 90, 5)
                                            $ DoreenX.Statup("Lust", 80, 10)
                                            ch_b "Правда? Потрясающе!"
                                        elif DoreenX.Sex >= 5:
                                            ch_d "Ну, я не против."
                                        elif not DoreenX.Sex:
                                            $ DoreenX.FaceChange("perplexed")
                                            ch_d "С кем ты занимаешься сексом?"
                                        else:
                                            $ DoreenX.FaceChange("bemused")
                                            ch_d "Ох, ага. . ."
                                        $ DoreenX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ DoreenX.FaceChange("sly")
                                        if DoreenX.PlayerFav == "anal":
                                            $ DoreenX.Statup("Lust", 80, 5)
                                            ch_d "Я знаю. . ."
                                        elif DoreenX.Favorite == "anal":
                                            $ DoreenX.Statup("Love", 90, 5)
                                            $ DoreenX.Statup("Lust", 80, 10)
                                            ch_d "Мне тоже!"
                                        elif DoreenX.Anal >= 10:
                                            ch_d "Ага, это. . . здорово. . ."
                                        elif not DoreenX.Anal:
                                            $ DoreenX.FaceChange("perplexed")
                                            ch_d "С кем?"
                                        else:
                                            $ DoreenX.FaceChange("bemused",Eyes="side")
                                            ch_d "Ох, ого. . ."
                                        $ DoreenX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ DoreenX.FaceChange("sly")
                                        if DoreenX.PlayerFav == "blow":
                                            $ DoreenX.Statup("Lust", 80, 3)
                                            ch_d "Я знаю. . ."
                                        elif DoreenX.Favorite == "blow":
                                            $ DoreenX.Statup("Love", 90, 5)
                                            $ DoreenX.Statup("Lust", 80, 5)
                                            ch_d "Мне тоже!"
                                        elif DoreenX.Blow >= 10:
                                            ch_d "Ага, ты супер вкусный."
                                        elif not DoreenX.Blow:
                                            $ DoreenX.FaceChange("perplexed")
                                            ch_d "Кто тебе сосет?"
                                        else:
                                            $ DoreenX.FaceChange("bemused")
                                            ch_d "Это. . . очень весело. . ."
                                        $ DoreenX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ DoreenX.FaceChange("sly")
                                        if DoreenX.PlayerFav == "cun":
                                            $ DoreenX.Statup("Lust", 80, 3)
                                            ch_d "Я знаю. . ."
                                        elif DoreenX.Favorite == "cun":
                                            $ DoreenX.Statup("Love", 90, 5)
                                            $ DoreenX.Statup("Lust", 80, 5)
                                            ch_d "Мне тоже!"
                                        elif DoreenX.CUN >= 10:
                                            ch_d "Ага, ты супер вкусная."
                                        elif not DoreenX.CUN:
                                            $ DoreenX.FaceChange("perplexed")
                                            ch_d "Кто тебе лижет?"
                                        else:
                                            $ DoreenX.FaceChange("bemused")
                                            ch_d "Это. . . очень весело. . ."
                                        $ DoreenX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ DoreenX.FaceChange("sly")
                                        if DoreenX.PlayerFav == "titjob":
                                            $ DoreenX.Statup("Lust", 80, 5)
                                            ch_d "Я знаю. . ."
                                        elif DoreenX.Favorite == "titjob":
                                            $ DoreenX.Statup("Love", 90, 5)
                                            $ DoreenX.Statup("Lust", 80, 7)
                                            ch_d "Мне тоже!"
                                        elif DoreenX.Tit >= 10:
                                            ch_d "Это, безусловно, уникальный опыт. . ."
                                        elif not DoreenX.Tit:
                                            $ DoreenX.FaceChange("perplexed")
                                            ch_d "Кто занимается этим с тобой?"
                                        else:
                                            $ DoreenX.FaceChange("bemused")
                                            ch_d "И почему я не удивлена? . ."
                                            $ DoreenX.Statup("Love", 80, 5)
                                            $ DoreenX.Statup("Inbt", 50, 10)
                                        $ DoreenX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ DoreenX.FaceChange("sly")
                                        if DoreenX.PlayerFav == "foot":
                                            $ DoreenX.Statup("Lust", 80, 5)
                                            ch_d "Я знаю. . ."
                                        elif DoreenX.Favorite == "foot":
                                            $ DoreenX.Statup("Love", 90, 5)
                                            $ DoreenX.Statup("Lust", 80, 7)
                                            ch_d "Мне тоже!"
                                        elif DoreenX.Foot >= 10:
                                            ch_d "Мне тоже очень нравится. . ."
                                        elif not DoreenX.Foot:
                                            $ DoreenX.FaceChange("perplexed")
                                            ch_d "Кто занимается этим с тобой?"
                                        else:
                                            $ DoreenX.FaceChange("bemused")
                                            ch_d "Ага, это очень приятно. . ."
                                        $ DoreenX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ DoreenX.FaceChange("sly")
                                        if DoreenX.PlayerFav == "hand":
                                            $ DoreenX.Statup("Lust", 80, 5)
                                            ch_d "Я знаю. . ."
                                        elif DoreenX.Favorite == "hand":
                                            $ DoreenX.Statup("Love", 90, 5)
                                            $ DoreenX.Statup("Lust", 80, 7)
                                            ch_d "Мне тоже!"
                                        elif DoreenX.Hand >= 10:
                                            ch_d "Мне тоже очень нравится. . ."
                                        elif not DoreenX.Hand:
                                            $ DoreenX.FaceChange("perplexed")
                                            ch_d "Кто занимается этим с тобой?"
                                        else:
                                            $ DoreenX.FaceChange("bemused")
                                            ch_d "Ага, это очень приятно. . ."
                                        $ DoreenX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ DoreenX.FaceChange("sly")
                                        if DoreenX.PlayerFav == "finger":
                                            $ DoreenX.Statup("Lust", 80, 5)
                                            ch_d "Я знаю. . ."
                                        elif DoreenX.Favorite == "finger":
                                            $ DoreenX.Statup("Love", 90, 5)
                                            $ DoreenX.Statup("Lust", 80, 7)
                                            ch_d "Знаешь, мне тоже это нравится!"
                                        elif DoreenX.Finger >= 10:
                                            ch_d "Мне тоже очень нравится. . ."
                                        elif not DoreenX.Finger:
                                            $ DoreenX.FaceChange("perplexed")
                                            ch_d "Кто занимается этим с тобой?"
                                        else:
                                            $ DoreenX.FaceChange("bemused")
                                            ch_d "Ага, это очень приятно. . ."
                                        $ DoreenX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = DoreenX.FondleB + DoreenX.FondleT + DoreenX.SuckB + DoreenX.Hotdog
                                        $ DoreenX.FaceChange("sly")
                                        if DoreenX.PlayerFav == "fondle":
                                            $ DoreenX.Statup("Lust", 80, 3)
                                            ch_d "Я знаю. . ."
                                        elif DoreenX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ DoreenX.Statup("Love", 90, 5)
                                            $ DoreenX.Statup("Lust", 80, 5)
                                            ch_d "Знаешь, мне это нравится!"
                                        elif Cnt >= 10:
                                            ch_d "Мне тоже очень нравится. . ."
                                        elif not Cnt:
                                            $ DoreenX.FaceChange("perplexed")
                                            ch_d "Кого ты ласкаешь?"
                                        else:
                                            $ DoreenX.FaceChange("bemused")
                                            ch_d "У тебя очень ловкие руки. . ."
                                        $ DoreenX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ DoreenX.FaceChange("sly")
                                        if DoreenX.PlayerFav == "kiss you":
                                            $ DoreenX.Statup("Love", 90, 3)
                                            ch_d "Оу, это очень приятно. . ."
                                        elif DoreenX.Favorite == "kiss you":
                                            $ DoreenX.Statup("Love", 90, 5)
                                            $ DoreenX.Statup("Lust", 80, 5)
                                            ch_d "У тебя это очень хорошо получается."
                                        elif DoreenX.Kissed >= 10:
                                            ch_d "Мне тоже нравится тебя целовать . . ."
                                        elif not DoreenX.Kissed:
                                            $ DoreenX.FaceChange("perplexed")
                                            ch_d "С кем ты целуешься?"
                                        else:
                                            $ DoreenX.FaceChange("bemused")
                                            ch_d "Мне тоже очень нравится тебя целовать. . ."
                                        $ DoreenX.PlayerFav = "kiss you"

                        $ DoreenX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(DoreenX, 800):
                                        $ DoreenX.FaceChange("perplexed")
                                        ch_d ". . ."
                                else:
                                        if DoreenX.SEXP >= 50:
                                            $ DoreenX.FaceChange("sly")
                                            if not Player.Male:
                                                ch_d "Ты должна знать, что меня заводит. . ."
                                            else:
                                                ch_d "Ты должен знать, что меня заводит. . ."
                                        else:
                                            $ DoreenX.FaceChange("bemused")
                                            $ DoreenX.Eyes = "side"
                                            ch_d "Хмм. . ."


                                        if not DoreenX.Favorite or DoreenX.Favorite == "kiss":
                                                ch_d "Думаю, когда мы целуемся. . ."
                                        elif DoreenX.Favorite == "anal":
                                                ch_d "Думаю. . . анальный секс?"
                                        elif DoreenX.Favorite == "lick ass":
                                                ch_d "Думаю. . . когда ты вылизываешь мой анус?"
                                        elif DoreenX.Favorite == "insert ass":
                                                ch_d "Думаю, когда ты ласкаешь. . . мой. . . анус."
                                        elif DoreenX.Favorite == "sex":
                                                ch_d "Думаю, мне нравится, когда ты в моей киске."
                                        elif DoreenX.Favorite == "lick pussy":
                                                ch_d "Думаю. . . когда ты вылизываешь мою киску."
                                        elif DoreenX.Favorite == "fondle pussy":
                                                ch_d "Думаю, когда ты. . . ласкаешь мою киску."
                                        elif DoreenX.Favorite == "blow":
                                                ch_d "Думаю, когда я. . . сосу тебе?"
                                        elif DoreenX.Favorite == "cun":
                                                ch_d "Думаю, когда я. . .  лижу тебе?."
                                        elif DoreenX.Favorite == "tit":
                                                ch_d "Думаю, когда я мастурбирую тебя своими сиськами?"
                                        elif DoreenX.Favorite == "foot":
                                                ch_d ". . . работать ножками?"
                                        elif DoreenX.Favorite == "hand":
                                                ch_d "Мне нравится. . . мастурбировать тебе."
                                        elif DoreenX.Favorite == "finger":
                                                ch_d "Мне нравится. . . ласкать твою киску."
                                        elif DoreenX.Favorite == "hotdog":
                                                ch_d "Мне очень нравится, когда ты трешься о меня."
                                        elif DoreenX.Favorite == "suck breasts":
                                                ch_d "Мне нравится, когда ты трешься о меня."
                                        elif DoreenX.Favorite == "fondle breasts":
                                                ch_d "Мне нравится, когда ты. . . сосешь мою грудь."
                                        elif DoreenX.Favorite == "fondle thighs":
                                                ch_d "Мне нравится, когда ты массируешь мои ножки."
                                        else:
                                                ch_d "Чт-. . .эм. . . Я не знаю, а тебе что нравится? . ."

                                # End Doreen's favorite things.

                "Не болтай так много во время секса." if "vocal" in DoreenX.Traits:
                        if "setvocal" in DoreenX.DailyActions:
                                $ DoreenX.FaceChange("perplexed")
                                ch_d "Ох, тебе следует уже определиться."
                        else:
                            if ApprovalCheck(DoreenX, 1000) and DoreenX.Obed <= DoreenX.Love:
                                $ DoreenX.FaceChange("bemused")
                                $ DoreenX.Statup("Obed", 90, 1)
                                ch_d "Я постараюсь быть тихой."
                                $ DoreenX.Traits.remove("vocal")
                            elif ApprovalCheck(DoreenX, 700, "O"):
                                $ DoreenX.FaceChange("sadside")
                                $ DoreenX.Statup("Obed", 90, 1)
                                ch_d ". . ."
                                $ DoreenX.Traits.remove("vocal")
                            elif ApprovalCheck(DoreenX, 600):
                                $ DoreenX.FaceChange("sly")
                                $ DoreenX.Statup("Love", 90, -3)
                                $ DoreenX.Statup("Obed", 50, -1)
                                $ DoreenX.Statup("Inbt", 90, 5)
                                ch_d "Я предпочла бы высказать то, что думаю."
                            else:
                                $ DoreenX.FaceChange("angry")
                                $ DoreenX.Statup("Love", 90, -5)
                                $ DoreenX.Statup("Obed", 60, -3)
                                $ DoreenX.Statup("Inbt", 90, 10)
                                ch_d "Я не буду молчать, спасибо."

                            $ DoreenX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in DoreenX.Traits:
                        if "setvocal" in DoreenX.DailyActions:
                                $ DoreenX.FaceChange("perplexed")
                                ch_d "Ох, тебе следует уже определиться."
                        else:
                            if ApprovalCheck(DoreenX, 1000) and DoreenX.Obed <= DoreenX.Love:
                                $ DoreenX.FaceChange("sly")
                                $ DoreenX.Statup("Obed", 90, 2)
                                ch_d "Наверное, можно. . ."
                                $ DoreenX.Traits.append("vocal")
                            elif ApprovalCheck(DoreenX, 700, "O"):
                                $ DoreenX.FaceChange("sadside")
                                $ DoreenX.Statup("Obed", 90, 2)
                                ch_d "Я. . . попробую."
                                $ DoreenX.Traits.append("vocal")
                            elif ApprovalCheck(DoreenX, 600):
                                $ DoreenX.FaceChange("sly")
                                $ DoreenX.Statup("Obed", 90, 3)
                                ch_d "Ох. . . эм. . . ладно?"
                                $ DoreenX.Traits.append("vocal")
                            else:
                                $ DoreenX.FaceChange("angry")
                                $ DoreenX.Statup("Inbt", 90, 5)
                                ch_d ". . ."

                            $ DoreenX.DailyActions.append("setvocal")
                        # End Doreen Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in DoreenX.Traits:
                        if "initiative" in DoreenX.DailyActions:
                                $ DoreenX.FaceChange("perplexed")
                                ch_d "Ох, тебе следует уже определиться."
                        else:
                            if ApprovalCheck(DoreenX, 1200) and DoreenX.Obed <= DoreenX.Love:
                                $ DoreenX.FaceChange("bemused")
                                $ DoreenX.Statup("Obed", 90, 1)
                                ch_d "Ох. . . ладно."
                                $ DoreenX.Traits.append("passive")
                            elif ApprovalCheck(DoreenX, 700, "O"):
                                $ DoreenX.FaceChange("sadside")
                                $ DoreenX.Statup("Obed", 90, 1)
                                ch_d "Я. . . попробую?"
                                $ DoreenX.Traits.append("passive")
                            elif ApprovalCheck(DoreenX, 600):
                                $ DoreenX.FaceChange("sly")
                                $ DoreenX.Statup("Love", 90, -3)
                                $ DoreenX.Statup("Obed", 50, -1)
                                $ DoreenX.Statup("Inbt", 90, 5)
                                ch_d "Это вряд ли."
                            else:
                                $ DoreenX.FaceChange("angry")
                                $ DoreenX.Statup("Love", 90, -5)
                                $ DoreenX.Statup("Obed", 60, -3)
                                $ DoreenX.Statup("Inbt", 90, 10)
                                ch_d "Посмотрим."

                            $ DoreenX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in DoreenX.Traits:
                        if "initiative" in DoreenX.DailyActions:
                                $ DoreenX.FaceChange("perplexed")
                                ch_d "Ох, тебе следует уже определиться."
                        else:
                            if ApprovalCheck(DoreenX, 1000) and DoreenX.Obed <= DoreenX.Love:
                                $ DoreenX.FaceChange("bemused")
                                $ DoreenX.Statup("Obed", 90, 1)
                                ch_d "Ох, конечно."
                                $ DoreenX.Traits.remove("passive")
                            elif ApprovalCheck(DoreenX, 700, "O"):
                                $ DoreenX.FaceChange("sadside")
                                $ DoreenX.Statup("Obed", 90, 1)
                                ch_d "Думаю, можно. . ."
                                $ DoreenX.Traits.remove("passive")
                            elif ApprovalCheck(DoreenX, 600):
                                $ DoreenX.FaceChange("sly")
                                $ DoreenX.Statup("Obed", 90, 3)
                                ch_d "Посмотрим."
                                $ DoreenX.Traits.remove("passive")
                            else:
                                $ DoreenX.FaceChange("angry")
                                $ DoreenX.Statup("Inbt", 90, 5)
                                ch_d "Я не хочу."

                            $ DoreenX.DailyActions.append("initiative")

                "О том, как ты накидываешься" if "jumped" in DoreenX.History:
                        call Doreen_Jumped
                "О твоей мастурбации":
                        call NoFap(DoreenX)

                "Всегда носи вибратор" if "dailyvibe" not in DoreenX.Traits:
                        call Daily_Vibrator(DoreenX)
                "Перестань всегда носить вибратор" if "dailyvibe" in DoreenX.Traits:
                        ch_d "Ладно. . ."
                        $ DoreenX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи анальную пробку" if "dailyplug" not in DoreenX.Traits:
                        call Daily_Plug(DoreenX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in DoreenX.Traits:
                        ch_d "Ладно. . ."
                        $ DoreenX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Неважно" if Line == "Что ты хочешь обсудить?":
                        return
                "На этом все." if Line != "Что ты хочешь обсудить?":
                        return
            if Line == "Что ты хочешь обсудить?":
                $ Line = "Значит, на этом все?"
    return
# End Doreen Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Doreen Chitchat /////////////////// #Work in progress
label Doreen_Chitchat(O=0, Options = ["default","default","default"]): #rkeljsvg
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if DoreenX not in Digits:
                if ApprovalCheck(DoreenX, 500, "L") or ApprovalCheck(DoreenX, 250, "I"):
                    ch_d "Слушай, если тебе нужен мой номер телефона, вот."
                    $ Digits.append(DoreenX)
                    return
                elif ApprovalCheck(DoreenX, 250, "O"):
                    ch_d "Слушай, если тебе нужен мой номер телефона, вот."
                    $ Digits.append(DoreenX)
                    return

        if "hungry" not in DoreenX.Traits and (DoreenX.Swallow + DoreenX.Chat[2]) >= 10 and DoreenX.Loc == bg_current:  #She's swallowed a lot
                    call Doreen_Hungry
                    return

        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(DoreenX, 800, "I")):
                    if DoreenX.Loc == bg_current and DoreenX.Thirst >= 30 and "refused" not in DoreenX.DailyActions and "quicksex" not in DoreenX.DailyActions:
                            $ DoreenX.FaceChange("sly",1)
                            ch_d "Слушай. . . не хочешь пошалить?"
                            call Quick_Sex(DoreenX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in DoreenX.DailyActions:
#            $ Options.append("caught")
        if DoreenX.Event[0] and "key" not in DoreenX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in DoreenX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in DoreenX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in DoreenX.DailyActions:
            $ Options.append("corruption")

#        if "Doreen" not in DoreenX.Names:
#            $ Options.append("doreen")

        if DoreenX.Date >= 1 and bg_current != "bg restaurant":
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in DoreenX.DailyActions and "cheek" not in DoreenX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if DoreenX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in DoreenX.DailyActions and (Player.Male or "girltalk" in DoreenX.History):
            #If you've caught Doreen showering today
            $ Options.append("showercaught")
        if "fondle breasts" in DoreenX.DailyActions or "fondle pussy" in DoreenX.DailyActions or "fondle ass" in DoreenX.DailyActions:
            #If you've fondled Doreen today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in DoreenX.Inventory and "256 Shades of Grey" in DoreenX.Inventory and "Avengers Tower Penthouse" in DoreenX.Inventory:
            #If you've given Doreen the books
            if "book" not in DoreenX.Chat:
                $ Options.append("booked")
        if "lace bra" in DoreenX.Inventory or "lace panties" in DoreenX.Inventory:
            #If you've given Doreen the lingerie
            if "lingerie" not in DoreenX.Chat:
                $ Options.append("lingerie")
        if DoreenX.Hand and Player.Male:
            #If Doreen's given a handjob
            $ Options.append("handy")
        if DoreenX.Blow and Player.Male:
            #If Doreen's given a blowjob
            $ Options.append("blow")
        if DoreenX.Swallow:
            #If Doreen's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in DoreenX.DailyActions or "painted" in DoreenX.DailyActions:
            #If Doreen's been facialed
            $ Options.append("facial")
        if DoreenX.Sleep:
            #If Doreen's slept over
            $ Options.append("sleep")
        if (DoreenX.CreamP or DoreenX.CreamA) and Player.Male:
            #If Doreen's been creampied
            $ Options.append("creampie")
        if DoreenX.Sex or DoreenX.Anal:
            #If Doreen's been sexed
            $ Options.append("sexed")
        if DoreenX.Anal:
            #If Doreen's been analed
            $ Options.append("anal")

        if "seenpeen" in DoreenX.History and Player.Male:
            $ Options.append("seenpeen")
        if "topless" in DoreenX.History:
            $ Options.append("topless")
        if "bottomless" in DoreenX.History:
            $ Options.append("bottomless")
        if "master" in DoreenX.Petnames and "boyfriend" in DoreenX.Petnames and "tail" not in DoreenX.History:
            $ Options.append("tail")

#        if not DoreenX.Chat[0] and DoreenX.Sex:
#            $ Options.append("virgin")

#        if (bg_current == "bg doreen" or bg_current == "bg player") and "relationship" not in DoreenX.DailyActions:
#            if "lover" not in DoreenX.Petnames and ApprovalCheck(DoreenX, 900, "L"): # DoreenX.Event[6]
#                $ Options.append("lover?")
#            elif "sir" not in DoreenX.Petnames and ApprovalCheck(DoreenX, 500, "O"): # DoreenX.Event[7]
#                $ Options.append("sir?")
#            elif "daddy" not in DoreenX.Petnames and ApprovalCheck(DoreenX, 750, "L") and ApprovalCheck(DoreenX, 500, "O") and ApprovalCheck(DoreenX, 500, "I"): # DoreenX.Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in DoreenX.Petnames and ApprovalCheck(DoreenX, 900, "O"): # DoreenX.Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in DoreenX.Petnames and ApprovalCheck(DoreenX, 500, "I"): # DoreenX.Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in DoreenX.Petnames and ApprovalCheck(DoreenX, 900, "I"): # DoreenX.Event[10]
#                $ Options.append("fuckbuddy?")


        if not ApprovalCheck(DoreenX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ DoreenX.DailyActions.append("cologne chat")
        $ DoreenX.FaceChange("confused")
        ch_d "(нюх, нюх). . . от тебя пахнет каким-то. . . животным. . ."
        $ DoreenX.FaceChange("sexy", 2)
        ch_d ". . . я в деле. . ."
    elif Options[0] == "purple":
        $ DoreenX.DailyActions.append("cologne chat")
        $ DoreenX.FaceChange("sly",1)
        ch_d "(нюх, нюх). . . что это за аромат? . ."
        $ DoreenX.FaceChange("normal",0)
        ch_d ". . . что я могу для тебя сделать?"
    elif Options[0] == "corruption":
        $ DoreenX.DailyActions.append("cologne chat")
        $ DoreenX.FaceChange("confused")
        ch_d "(нюх, нюх). . . ого, какой мощный аромат. . ."
        $ DoreenX.FaceChange("angry")
        ch_d ". . . Меня начинают посещать. . . дурные мысли. . ."
        $ DoreenX.FaceChange("sly")

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in DoreenX.Chat:
                    ch_d "Эй! Из-за тебя меня чуть не исключили!"
                    if not ApprovalCheck(DoreenX, 500, "I"):
                         ch_d "Но это было довольно захватывающе. . ."
            else:
                    ch_d "[DoreenX.Petname], из-за тебя меня чуть не исключили!"
                    if not ApprovalCheck(DoreenX, 500, "I"):
                        ch_d "Наверное, в будущем нам не стоит выделяться. . ."
                    else:
                         ch_d "-но это было довольно весело. . ."
                    $ DoreenX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if DoreenX.SEXP <= 15:
                ch_d "Осторожно с ключом от моей комнаты. . ."
            else:
                ch_d "Слушай, помнишь, я дала тебе ключ от своей комнаты? Приходи ко мне почаще. . ."
            $ DoreenX.Chat.append("key")

    elif Options[0] == "dated":
            #Doreen's response to having gone on a date with the Player.
            ch_d "Тем вечером мне было очень весело, мы должна как-нибудь повторить."

    elif Options[0] == "kissed":
            #Doreen's response to having been kissed by the Player.
            $ DoreenX.FaceChange("normal",1)
            ch_d "[DoreenX.Petname], ты очень хорошо целуешься."
            menu:
                extend ""
                "Я стараюсь.":
                        $ DoreenX.FaceChange("smile",1)
                        ch_d "Ага. . ."
                "Ты правда так думаешь?":
                        $ DoreenX.FaceChange("smile",1)
                        ch_d "Да!"

    elif Options[0] == "dangerroom":
            #Doreen's response to Player working out in the Danger Room while Doreen is present
            $ DoreenX.FaceChange("sly",1)
            ch_d "Ох, [DoreenX.Petname]. Недавно я видела твою тренировку в Комнате Опасности."
            ch_d "У тебя очень хорошо получается!"

    elif Options[0] == "showercaught":
            #Doreen's response to being caught in the shower.
            if "shower" in DoreenX.Chat:
                if not Player.Male:
                    ch_d "Значит, ты снова видела меня в душе. . ."
                else:
                    ch_d "Значит, ты снова видел меня в душе. . ."
            else:
                ch_d "Я, эм. . . думаю, будет лучше, если ты не будешь заходить в душ, пока я им пользуюсь."
                ch_d "Ты всегда так делаешь?"
                $ DoreenX.Chat.append("shower")
                menu:
                    extend ""
                    "Это была чистая случайность! Клянусь!":
                            $ DoreenX.Statup("Love", 50, 5)
                            $ DoreenX.Statup("Love", 90, 2)
                            if ApprovalCheck(DoreenX, 1200):
                                $ DoreenX.FaceChange("sly",1)
                                ch_d "Ох, конечно. . ."
                                ch_d "Думаю, я не так уж и сильно против. . ."
                            else:
                                $ DoreenX.FaceChange("smile")
                                ch_d "Ох, конечно. . ."
                    "Только если там ты.":
                            $ DoreenX.Statup("Obed", 40, 5)
                            if ApprovalCheck(DoreenX, 1000) or ApprovalCheck(DoreenX, 700, "L"):
                                    $ DoreenX.Statup("Love", 90, 3)
                                    $ DoreenX.FaceChange("surprised",2,Mouth="normal")
                                    ch_d "Ох. . ."
                                    $ DoreenX.FaceChange("sly",1)
                                    ch_d "Ну. . . спасибо?"
                            else:
                                    $ DoreenX.Statup("Love", 70, -5)
                                    $ DoreenX.FaceChange("angry")
                                    if not Player.Male:
                                        ch_d "Не думаю, что ты меня поняла. . ."
                                    else:
                                        ch_d "Не думаю, что ты меня понял. . ."
                    "Я заглянула умышленно. Но я ни о чем не жалею." if not Player.Male:
                            if ApprovalCheck(DoreenX, 1200):
                                    $ DoreenX.Statup("Love", 90, 3)
                                    $ DoreenX.Statup("Obed", 70, 10)
                                    $ DoreenX.Statup("Inbt", 50, 5)
                                    $ DoreenX.FaceChange("sly",1)
                                    ch_d "Логично."
                            elif ApprovalCheck(DoreenX, 800):
                                    $ DoreenX.Statup("Obed", 60, 5)
                                    $ DoreenX.Statup("Inbt", 50, 5)
                                    $ DoreenX.FaceChange("perplexed",2)
                                    ch_d "Ну. . . ладно. . ."
                                    $ DoreenX.Blush = 1
                            else:
                                    $ DoreenX.Statup("Love", 50, -10)
                                    $ DoreenX.Statup("Love", 80, -10)
                                    $ DoreenX.Statup("Obed", 50, 10)
                                    $ DoreenX.FaceChange("angry")
                                    ch_d "От твоих слов мне не стало легче!"
                    "Я заглянул умышленно. Но я ни о чем не жалею." if Player.Male:
                            if ApprovalCheck(DoreenX, 1200):
                                    $ DoreenX.Statup("Love", 90, 3)
                                    $ DoreenX.Statup("Obed", 70, 10)
                                    $ DoreenX.Statup("Inbt", 50, 5)
                                    $ DoreenX.FaceChange("sly",1)
                                    ch_d "Логично."
                            elif ApprovalCheck(DoreenX, 800):
                                    $ DoreenX.Statup("Obed", 60, 5)
                                    $ DoreenX.Statup("Inbt", 50, 5)
                                    $ DoreenX.FaceChange("perplexed",2)
                                    ch_d "Ну. . . ладно. . ."
                                    $ DoreenX.Blush = 1
                            else:
                                    $ DoreenX.Statup("Love", 50, -10)
                                    $ DoreenX.Statup("Love", 80, -10)
                                    $ DoreenX.Statup("Obed", 50, 10)
                                    $ DoreenX.FaceChange("angry")
                                    ch_d "От твоих слов мне не стало легче!"

    elif Options[0] == "fondled":
            #Doreen's response to being felt up.
            if DoreenX.FondleB + DoreenX.FondleP + DoreenX.FondleA >= 15:
                ch_d "Знаешь, время от времени мне не помешал бы массаж. . ."
            else:
                ch_d "Если хочешь, можешь пощупать меня. . ."

    elif Options[0] == "booked":
            #Doreen's response after a Player gives her the books from the shop.
            if not Player.Male:
                ch_d "Я прочитала те книги, которые ты мне дала. . ."
            else:
                ch_d "Я прочитала те книги, которые ты мне дал. . ."
            menu:
                extend ""
                "Да? И как тебе?":
                        $ DoreenX.FaceChange("sly",2)
                        ch_d "Они очень. . . дикие. . ."
                "Хорошо. Пожалуй, ты могла бы чему-нибудь из них научиться.":
                        $ DoreenX.Statup("Obed", 70, 5)
                        $ DoreenX.Statup("Inbt", 50, 5)
                        $ DoreenX.FaceChange("surprised",2)
                        ch_d "Ага, видимо, даже очень многому."
            $ DoreenX.Blush = 1
            $ DoreenX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Doreen's response to being given lingerie.
            $ DoreenX.FaceChange("sly",2)
            if not Player.Male:
                ch_d "Мне нравится нижнее белье, которое ты мне подарила."
            else:
                ch_d "Мне нравится нижнее белье, которое ты мне подарил."
            ch_d "Оно очень красивое. . "
            $ DoreenX.Blush = 1
            $ DoreenX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Doreen's response after giving the Player a handjob.
            $ DoreenX.FaceChange("sly",1)
            ch_d "Надеюсь, моя, эм. . . мастурбация тебе. . ."
            ch_d "Понравилась. . ."

    elif Options[0] == "blow":
            if "blow" not in DoreenX.Chat:
                    #Doreen's response after giving the Player a blowjob.
                    $ DoreenX.FaceChange("sly",2)
                    ch_d "Слушай, эм, ты помнишь, когда я тебе отсосала. . ?"
                    ch_d "Все прошло. . . хорошо? . ."
                    menu:
                        extend ""
                        "Ты была великолепна.":
                                    $ DoreenX.Statup("Love", 90, 5)
                                    $ DoreenX.Statup("Inbt", 60, 10)
                                    $ DoreenX.FaceChange("surprised",2)
                                    ch_d "Ох!"
                                    $ DoreenX.FaceChange("sly",1,Eyes="side")
                                    ch_d "Ох, хорошо. . ."
                                    $ DoreenX.FaceChange("sexy",1)
                                    ch_d "Я, эм, я могла бы повторить. . ."
                        "Честно? Все было хорошо. . . но, думаю, тебе не помешает еще немного попрактиковаться.":
                                if ApprovalCheck(DoreenX, 300, "I") or not ApprovalCheck(DoreenX, 800):
                                    $ DoreenX.Statup("Love", 90, -5)
                                    $ DoreenX.Statup("Obed", 60, 10)
                                    $ DoreenX.Statup("Inbt", 50, 10)
                                    $ DoreenX.FaceChange("perplexed",1)
                                    ch_d "Наверное. . . наверное, ты прав. . ."
                                    ch_d "Ты найдешь для меня время?"
                                else:
                                    $ DoreenX.Statup("Obed", 70, 15)
                                    $ DoreenX.Statup("Inbt", 50, 5)
                                    $ DoreenX.FaceChange("sexy",1)
                                    ch_d "Хммм. . . ну, у меня было довольно мало практики. . ."
                        "Угу, если бы мне нравились стремные звуки и шкрябанье зубов по члену, но это далеко не так.":
                                    $ DoreenX.Statup("Love", 70, -5)
                                    $ DoreenX.Statup("Love", 90, -10)
                                    $ DoreenX.Statup("Obed", 60, 10)
                                    $ DoreenX.FaceChange("angry",2)
                                    ch_d "Я. . . ничего не могу с собой поделать. . ."
                    $ DoreenX.Blush = 1
                    $ DoreenX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["Должна сказать, твой член очень вкусный.",
                            "В прошлый раз я чуть не вывихнул себе челюсть!",
                            "Я могла бы как-нибудь еще раз отсосать тебе.",
                            "Хммм. . . [Стучит языком по внутренней стороне щеки.]"])
                    ch_d "[Line]"

    elif Options[0] == "swallowed":
            #Doreen's response after swallowing the Player's cum.
            if "swallow" in DoreenX.Chat:
                $ DoreenX.FaceChange("sly",1)
                if not Player.Male:
                    ch_d "Я хочу спросить, можно мне взять еще немного твоих соков?"
                else:
                    ch_d "Я хочу спросить, можно мне взять еще немного твоей спермы?"
            else:
                ch_d "Мне интересно. . ."
                $ DoreenX.FaceChange("confused",1,Mouth="normal")
                if not Player.Male:
                    ch_d "Ты знаешь, что у твоих соков безумный и. . ."
                else:
                    ch_d "Ты знаешь, что у твоей спермы безумный и. . ."
                $ DoreenX.FaceChange("normal",1)
                ch_d "необычный. . ."
                $ DoreenX.FaceChange("sly",1)
                ch_d ". . .вкус. . ?"
                $ DoreenX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Doreen's response after taking a facial from the Player.
            ch_d "Ладно, ты можешь подумать, что я странная, но. . ."
            $ DoreenX.FaceChange("sexy",2)
            if not Player.Male:
                ch_d "Но мне очень даже нравится ощущать твои соки на своем лице."
                ch_d ". . ."
                ch_d "Просто чтобы ты знала. . ."
            else:
                ch_d "Но мне очень даже нравится ощущать твою сперму на своем лице."
                ch_d ". . ."
                ch_d "Просто чтобы ты знал. . ."
            $ DoreenX.Blush = 1

    elif Options[0] == "sleepover":
            #Doreen's response after sleeping with the Player.
            ch_d "Мне очень понравилась та ночь."
            ch_d "Было так приятно ощущать твое теплое тело рядом. . ."

    elif Options[0] == "creampie":
            #Another of Doreen's responses after having sex with the Player.
            "[DoreenX.Name] подходит к вам вплотную и шепчет на ухо."
            if not Player.Male:
                ch_d "Я все еще чувствую, словно они. . . стекают по моим бедрам."
            else:
                ch_d "Я все еще чувствую, словно она. . . стекает по моим бедрам."

    elif Options[0] == "sexed":
            #A final response from Doreen after having sex with the Player.
            $ DoreenX.FaceChange("sexy",2,Eyes="side")
            if not Player.Male:
                ch_d "Просто чтобы ты знала. . ."
            else:
                ch_d "Просто чтобы ты знал. . ."
            $ DoreenX.FaceChange("sly",2,Eyes="side")
            ch_d ". . .в последнее время, когда я. . . доставляю себе удовольствие. . ."
            $ DoreenX.FaceChange("sexy",2)
            ch_d "Я думаю о тебе. . ."
            $ DoreenX.Blush = 1

    elif Options[0] == "anal":
            #Doreen's response after getting anal from the Player.
            $ DoreenX.FaceChange("sly")
            ch_d "Честно говоря, я не так часто занималась. . . анальным сексом. . ."
            $ DoreenX.FaceChange("sexy",1)
            ch_d ". . . но, думаю, что он мне очень нравится!"

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ DoreenX.FaceChange("sly",1, Eyes="down")
            ch_d "Ох, просто чтобы ты знал. . ."
            ch_d "Твой. . . член. . . я не могу выбросить это из головы. . ."
            ch_d "Он такой потрясающий!"
            $ DoreenX.FaceChange("bemused",1)
            $ DoreenX.Statup("Love", 50, 5)
            $ DoreenX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            if not Player.Male:
                ch_d "Итак, ты видела мою грудь, и. . ."
            else:
                ch_d "Итак, ты видел мою грудь, и. . ."
            ch_d "Мне интересно, как она тебе?"
            call Girl_First_TMenu
            $ DoreenX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            if not Player.Male:
                ch_d "Итак, ты видела мою. . . киску, и. . ."
            else:
                ch_d "Итак, ты видел мою. . . киску, и. . ."
            ch_d "Мне интересно, как она тебе?"
            call Girl_First_BMenu
            $ DoreenX.History.remove("bottomless")
    elif Options[0] == "tail": # tail removal scene
            ch_d "Я. . . всегда находила свой хвост немного неудобным. . ."
            call Doreen_Tail
            if not DoreenX.Tail:
                $ DoreenX.Statup("Love", 90, 1)
                $ DoreenX.Statup("Obed", 200, 1)
                $ DoreenX.FaceChange("smile",1)
                ch_d "Ох, прямо гора с плечь."
                ch_d "Тяжело постоянно таскать 3-4 кг меха."

#    elif Options[0] == "boyfriend?":
#        call Doreen_BF
#    elif Options[0] == "lover?":
#        call Doreen_Love
#    elif Options[0] == "sir?":
#        call Doreen_Sub
#    elif Options[0] == "master?":
#        call Doreen_Master
#    elif Options[0] == "sexfriend?":
#        call Doreen_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Doreen_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Doreen_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Отойди от меня.",
                "Я не хочу тебя видеть.",
                "Оставь меня в покое.",
                "Отойди.",
                "Прочь!"])
        ch_d "[Line]"

    else: #all else fell through. . .
            if DoreenX not in ActiveGirls:
                    $ D20 = 21
            else:
                    $ D20 = renpy.random.randint(1, 21)
            if D20 == 1:
                    $ DoreenX.FaceChange("smile")
                    ch_d "Мне кажется, я начинаю здесь приживаться."
            elif D20 == 2:
                    $ DoreenX.FaceChange("smile")
                    ch_d "Мне нравится, какими приветливыми были здешние преподаватели!"
            elif D20 == 3:
                    $ DoreenX.FaceChange("surprised")
                    ch_d "Хм? О, извини. Белки поспорили из-за каких-то орехов."
            elif D20 == 4:
                    $ DoreenX.FaceChange("normal")
                    ch_d "Ох, [DoreenX.Petname]. Я просто слушала спор двух моих маленьких друзей."
            elif D20 == 5:
                    $ DoreenX.FaceChange("smile")
                    if not Player.Male:
                        ch_d "В кафетерии очень вкусная еда, ты ее пробовала?"
                    else:
                        ch_d "В кафетерии очень вкусная еда, ты ее пробовал?"
            elif D20 == 6:
                    $ DoreenX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_d "Слушай, [DoreenX.Petname]. Ты не видела [JubesX.Name_vin]? Мы с ней хотели пройтись по магазинам."
                    else:
                        ch_d "Слушай, [DoreenX.Petname]. Ты не видел [JubesX.Name_vin]? Мы с ней хотели пройтись по магазинам."
            elif D20 == 7:
                    $ DoreenX.FaceChange("normal")
                    ch_d "Ранее я была в Комнате Опасности, я пыталась сделать сражение с Таносом более реалистичным."
            elif D20 == 8:
                    $ DoreenX.FaceChange("sad")
                    ch_d "Мне здесь нравится, но иногда мне нужно выбираться на природу. . ."
            elif D20 == 9:
                    $ DoreenX.FaceChange("smile",2)
                    ch_d "Кажется, я заметила, как Берто пялится на мою задницу!"
                    $ DoreenX.FaceChange("smile",1)
            elif D20 == 10:
                    $ DoreenX.FaceChange("smile")
                    ch_d "Мне нравится, что здесь я могу свободно пользоваться своими способностями."
                    ch_d "Очень удобно, если я что-нибудь забыла, я просто могу попросить белок принести мне это."
            elif D20 == 11:
                    $ DoreenX.FaceChange("smile")
                    ch_d "[LauraX.Name] замечательный спарринг-партнер."
                    ch_d "Она почти так же хороша, как и ее отец."
            elif D20 == 12:
                    $ DoreenX.FaceChange("sad")
                    ch_d "Не думаю, что я хорошо справилась с тем тестом, мне нужно больше заниматься. . ."
            elif D20 == 13:
                    $ DoreenX.FaceChange("smile")
                    ch_d "Китти и Лора сводили меня в торговый центр за мороженым!"
            elif D20 == 14:
                    $ DoreenX.FaceChange("sad")
                    ch_d "На миссии ходить очень интересно, но это может плохо сказаться на оценках!"
            elif D20 == 15:
                    $ DoreenX.FaceChange("perplexed")
                    ch_d "Ты знаешь Мстителей?"
                    ch_d "Однажды я чуть было не присоединилась к ним."
            elif D20 == 16:
                    $ DoreenX.FaceChange("perplexed")
                    ch_d "Тебе когда-нибудь приходилось бывать в Нью-Йорке? Центральный парк - это просто нечто удивительное."
            elif D20 == 17:
                    $ DoreenX.FaceChange("perplexed")
                    if DoreenX.Tail:
                        ch_d "Я чуть не снесла Профессора хвостом. . ."
                    else:
                        ch_d "Я чуть не снесла Профессора задницей. . ."
                    ch_d "Пожалуй, мне следует лучше смотреть, куда я иду. . ."
            elif D20 == 18:
                    $ DoreenX.FaceChange("smile")
                    ch_d "Никому об этом не говори, но Типпи То немного влюблена в доктора МакКоя."
            elif D20 == 19:
                    $ DoreenX.FaceChange("confused")
                    ch_d "Слушай, это пахнет. . . тортиком?!"
            elif D20 == 20:
                    $ DoreenX.FaceChange("smile")
                    ch_d "Я просто обожаю болтать без умолку. . ."
            else:
                    $ DoreenX.FaceChange("smile")
                    ch_d "Эй, рада тебя видеть. . ."

    $ Line = 0
    return

# start Doreen_Names//////////////////////////////////////////////////////////
label Doreen_Names:    #rkeljsvgb
    menu:
        ch_d "М? Как ты хочешь, чтобы я тебя звала?"
        "Зови по инициалам." if Player.Name in DoreenX.Petnames:
            $ DoreenX.Petname = Player.Name[:1]  #fix test this
            $ DoreenX.Petname_rod = Player.Name[:1]
            $ DoreenX.Petname_dat = Player.Name[:1]
            $ DoreenX.Petname_vin = Player.Name[:1]
            $ DoreenX.Petname_tvo = Player.Name[:1]
            $ DoreenX.Petname_pre = Player.Name[:1]
            ch_d "Конечно, [DoreenX.Petname]."
        "Зови меня по имени.":
            if Player.Name in DoreenX.Petnames:
                    $ DoreenX.Petname = Player.Name
                    $ DoreenX.Petname_rod = Player.Name_rod
                    $ DoreenX.Petname_dat = Player.Name_dat
                    $ DoreenX.Petname_vin = Player.Name_vin
                    $ DoreenX.Petname_tvo = Player.Name_tvo
                    $ DoreenX.Petname_pre = Player.Name_pre
            elif DoreenX.Petnames == ["Dude"]:
                    ch_d "Честно говоря, я не знаю, как тебя зовут. . ."
                    call DoreenPlayerName
            else:
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
            ch_d "Конечно, [DoreenX.Petname]."
        "Зови меня \"моя девушка\"." if "boyfriend" in DoreenX.Petnames and not Player.Male:
            $ DoreenX.Petname = "моя девушка"
            $ DoreenX.Petname_rod = "моей девушки"
            $ DoreenX.Petname_dat = "моей девушке"
            $ DoreenX.Petname_vin = "мою девушку"
            $ DoreenX.Petname_tvo = "моей девушкой"
            $ DoreenX.Petname_pre = "моей девушке"
            ch_d "Хорошо, [DoreenX.Petname]."
        "Зови меня \"мой парень\"." if "boyfriend" in DoreenX.Petnames and Player.Male:
            $ DoreenX.Petname = "мой парень"
            $ DoreenX.Petname_rod = "моего парня"
            $ DoreenX.Petname_dat = "моему парню"
            $ DoreenX.Petname_vin = "моего парня"
            $ DoreenX.Petname_tvo = "моим парнем"
            $ DoreenX.Petname_pre = "моем парне"
            ch_d "Хорошо, [DoreenX.Petname]."
        "Зови меня \"любимая\"." if "lover" in DoreenX.Petnames and not Player.Male:
            $ DoreenX.Petname = "любимая"
            $ DoreenX.Petname_rod = "любимой"
            $ DoreenX.Petname_dat = "любимой"
            $ DoreenX.Petname_vin = "любимую"
            $ DoreenX.Petname_tvo = "любимой"
            $ DoreenX.Petname_pre = "любимой"
            ch_d "Ооох, ладно, [DoreenX.Petname]."
        "Зови меня \"любимый\"." if "lover" in DoreenX.Petnames and Player.Male:
            $ DoreenX.Petname = "любимый"
            $ DoreenX.Petname_rod = "любимого"
            $ DoreenX.Petname_dat = "любимому"
            $ DoreenX.Petname_vin = "любимого"
            $ DoreenX.Petname_tvo = "любимым"
            $ DoreenX.Petname_pre = "любимом"
            ch_d "Ооох, ладно, [DoreenX.Petname]."
        "Зови меня \"госпожа\"." if "sir" in DoreenX.Petnames and not Player.Male:
            $ DoreenX.Petname = "госпожа"
            $ DoreenX.Petname_rod = "госпожи"
            $ DoreenX.Petname_dat = "госпоже"
            $ DoreenX.Petname_vin = "госпожу"
            $ DoreenX.Petname_tvo = "госпожой"
            $ DoreenX.Petname_pre = "госпоже"
            ch_d "Конечно, [DoreenX.Petname]."
        "Зови меня \"господин\"." if "sir" in DoreenX.Petnames and Player.Male:
            $ DoreenX.Petname = "господин"
            $ DoreenX.Petname_rod = "господина"
            $ DoreenX.Petname_dat = "господину"
            $ DoreenX.Petname_vin = "господина"
            $ DoreenX.Petname_tvo = "господином"
            $ DoreenX.Petname_pre = "господине"
            ch_d "Конечно, [DoreenX.Petname]."
        "Зови меня \"хозяйка\"." if "master" in DoreenX.Petnames and not Player.Male:
            $ DoreenX.Petname = "хозяйка"
            $ DoreenX.Petname_rod = "хозяйки"
            $ DoreenX.Petname_dat = "хозяйке"
            $ DoreenX.Petname_vin = "хозяйку"
            $ DoreenX.Petname_tvo = "хозяйкой"
            $ DoreenX.Petname_pre = "хозяйке"
            ch_d "Да, [DoreenX.Petname]."
        "Зови меня \"хозяин\"." if "master" in DoreenX.Petnames and Player.Male:
            $ DoreenX.Petname = "хозяин"
            $ DoreenX.Petname_rod = "хозяина"
            $ DoreenX.Petname_dat = "хозяину"
            $ DoreenX.Petname_vin = "хозяина"
            $ DoreenX.Petname_tvo = "хозяином"
            $ DoreenX.Petname_pre = "хозяине"
            ch_d "Да, [DoreenX.Petname]."
        "Зови меня \"любовница\"." if "sex friend" in DoreenX.Petnames and not Player.Male:
            $ DoreenX.Petname = "любовница"
            $ DoreenX.Petname_rod = "любовницы"
            $ DoreenX.Petname_dat = "любовнице"
            $ DoreenX.Petname_vin = "любовницу"
            $ DoreenX.Petname_tvo = "любовницей"
            $ DoreenX.Petname_pre = "любовнице"
            ch_d "Хех, ладно, [DoreenX.Petname]."
        "Зови меня \"любовник\"." if "sex friend" in DoreenX.Petnames and Player.Male:
            $ DoreenX.Petname = "любовник"
            $ DoreenX.Petname_rod = "любовника"
            $ DoreenX.Petname_dat = "любовнику"
            $ DoreenX.Petname_vin = "любовника"
            $ DoreenX.Petname_tvo = "любовником"
            $ DoreenX.Petname_pre = "любовнике"
            ch_d "Хех, ладно, [DoreenX.Petname]."
        "Зови меня \"секс-партнерша\"." if "fuck buddy" in DoreenX.Petnames and not Player.Male:
            $ DoreenX.Petname = "секс-партнерша"
            $ DoreenX.Petname_rod = "секс-партнерши"
            $ DoreenX.Petname_dat = "секс-партнерше"
            $ DoreenX.Petname_vin = "секс-партнершу"
            $ DoreenX.Petname_tvo = "секс-партнершей"
            $ DoreenX.Petname_pre = "секс-партнерше"
            ch_d "Ох, это немного. . . ладно. . . [DoreenX.Petname]."
        "Зови меня \"секс-партнер\"." if "fuck buddy" in DoreenX.Petnames and Player.Male:
            $ DoreenX.Petname = "секс-партнер"
            $ DoreenX.Petname_rod = "секс-партнера"
            $ DoreenX.Petname_dat = "секс-партнеру"
            $ DoreenX.Petname_vin = "секс-партнера"
            $ DoreenX.Petname_tvo = "секс-партнером"
            $ DoreenX.Petname_pre = "секс-партнере"
            ch_d "Ох, это немного. . . ладно. . . [DoreenX.Petname]."
        "Зови меня \"мамочка\"." if "daddy" in DoreenX.Petnames and not Player.Male:
            $ DoreenX.Petname = "мамочка"
            $ DoreenX.Petname_rod = "мамочки"
            $ DoreenX.Petname_dat = "мамочке"
            $ DoreenX.Petname_vin = "мамочку"
            $ DoreenX.Petname_tvo = "мамочкой"
            $ DoreenX.Petname_pre = "мамочке"
            ch_d "Ох! Конечно, [DoreenX.Petname]."
        "Зови меня \"папочка\"." if "daddy" in DoreenX.Petnames and Player.Male:
            $ DoreenX.Petname = "папочка"
            $ DoreenX.Petname_rod = "папочки"
            $ DoreenX.Petname_dat = "папочке"
            $ DoreenX.Petname_vin = "папочку"
            $ DoreenX.Petname_tvo = "папочкой"
            $ DoreenX.Petname_pre = "папочке"
            ch_d "Ох! Конечно, [DoreenX.Petname]."

        "Зови меня \"Главная Белка\"." if "sir" in DoreenX.Petnames:
            $ DoreenX.Petname = "Главная Белка"
            $ DoreenX.Petname_rod = "Главной Белки"
            $ DoreenX.Petname_dat = "Главной Белке"
            $ DoreenX.Petname_vin = "Главную Белку"
            $ DoreenX.Petname_tvo = "Главной Белкой"
            $ DoreenX.Petname_pre = "Главной Белке"
            ch_d "Конечно, [DoreenX.Petname]."
        "Зови меня \"Босс-Белка\"." if "master" in DoreenX.Petnames:
            $ DoreenX.Petname = "Босс-Белка"
            $ DoreenX.Petname_rod = "Босса-Белки"
            $ DoreenX.Petname_dat = "Боссу-Белке"
            $ DoreenX.Petname_vin = "Босса-Белку"
            $ DoreenX.Petname_tvo = "Боссом-Белкой"
            $ DoreenX.Petname_pre = "Боссе-Белке"
            ch_d "Да, [DoreenX.Petname]."
        "\"Чувиха\" в самый раз." if not Player.Male:
            $ DoreenX.Petname = "Чувиха"
            $ DoreenX.Petname_rod = "Чувихи"
            $ DoreenX.Petname_dat = "Чувихе"
            $ DoreenX.Petname_vin = "Чувиху"
            $ DoreenX.Petname_tvo = "Чувихой"
            $ DoreenX.Petname_pre = "Чувихе"
            ch_d "Ладно, чувиха."
        "\"Чувак\" в самый раз." if Player.Male:
            $ DoreenX.Petname = "Чувак"
            $ DoreenX.Petname_rod = "Чувака"
            $ DoreenX.Petname_dat = "Чуваку"
            $ DoreenX.Petname_vin = "Чувака"
            $ DoreenX.Petname_tvo = "Чуваком"
            $ DoreenX.Petname_pre = "Чуваке"
            ch_d "Ладно, чувак."
        "Неважно.":
            return
    return
# end Doreen_Names//////////////////////////////////////////////////////////

label Doreen_Pet: #rkeljsvgb
    while 1:
        menu:
            extend ""
            "Обходительно":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "Дорин.":
                        $ DoreenX.Pet = "Дорин"
                        $ DoreenX.Pet_rod = "Дорин"
                        $ DoreenX.Pet_dat = "Дорин"
                        $ DoreenX.Pet_vin = "Дорин"
                        $ DoreenX.Pet_tvo = "Дорин"
                        $ DoreenX.Pet_pre = "Дорин"
                        ch_d "Ладно."

                    "Девушка-Белка." if "Squirrel Girl" in DoreenX.Names:
                        if ApprovalCheck(DoreenX, 700, "L") and not ApprovalCheck(DoreenX, 500, "O"):
                                ch_d "Это довольно странное прозвище, [DoreenX.Petname]."
                        else:
                                $ DoreenX.Pet = "Девушка-Белка"
                                $ DoreenX.Pet_rod = "Девушки-Белки"
                                $ DoreenX.Pet_dat = "Девушке-Белке"
                                $ DoreenX.Pet_vin = "Девушку-Белку"
                                $ DoreenX.Pet_tvo = "Девушкой-Белкой"
                                $ DoreenX.Pet_pre = "Девушке-Белке"
                                ch_d "Ладно, наверное."


                    "\"моя девушка\".":
                        if "boyfriend" in DoreenX.Petnames:
                            $ DoreenX.FaceChange("sexy", 1)
                            $ DoreenX.Pet = "моя девушка"
                            $ DoreenX.Pet_rod = "моей девушки"
                            $ DoreenX.Pet_dat = "моей девушке"
                            $ DoreenX.Pet_vin = "мою девушку"
                            $ DoreenX.Pet_tvo = "моей девушкой"
                            $ DoreenX.Pet_pre = "моей девушке"
                            ch_d "Конечно, я же в самом деле твоя девушка, [DoreenX.Petname]."
                        else:
                            $ DoreenX.FaceChange("angry")
                            ch_d "Это слишком, [DoreenX.Petname]."

                    "\"детка\".":
                        if "boyfriend" in DoreenX.Petnames or ApprovalCheck(DoreenX, 700, "L"):
                            $ DoreenX.FaceChange("sexy", 1)
                            $ DoreenX.Pet = "детка"
                            $ DoreenX.Pet_rod = "детки"
                            $ DoreenX.Pet_dat = "детке"
                            $ DoreenX.Pet_vin = "детку"
                            $ DoreenX.Pet_tvo = "деткой"
                            $ DoreenX.Pet_pre = "детке"
                            ch_d "Я твоя \"детка,\" мне нравится."
                        else:
                            $ DoreenX.FaceChange("angry")
                            ch_d "Это слишком, [DoreenX.Petname]."

                    "\"крошка\".":
                        if "boyfriend" in DoreenX.Petnames or ApprovalCheck(DoreenX, 600, "L"):
                            $ DoreenX.FaceChange("sexy", 1)
                            $ DoreenX.Pet = "крошка"
                            $ DoreenX.Pet_rod = "крошки"
                            $ DoreenX.Pet_dat = "крошке"
                            $ DoreenX.Pet_vin = "крошку"
                            $ DoreenX.Pet_tvo = "крошкой"
                            $ DoreenX.Pet_pre = "крошке"
                            ch_d "Я твоя \"крошка,\" это так мило."
                        else:
                            $ DoreenX.FaceChange("angry")
                            ch_d "Это слишком, [DoreenX.Petname]."

                    "\"малышка\".":
                        if "boyfriend" in DoreenX.Petnames or ApprovalCheck(DoreenX, 500, "L"):
                            $ DoreenX.FaceChange("sexy", 1)
                            $ DoreenX.Pet = "малышка"
                            $ DoreenX.Pet_rod = "малышки"
                            $ DoreenX.Pet_dat = "малышке"
                            $ DoreenX.Pet_vin = "малышку"
                            $ DoreenX.Pet_tvo = "малышкой"
                            $ DoreenX.Pet_pre = "малышке"
                            ch_d "Я тебя обожаю, [DoreenX.Petname]."
                        else:
                            $ DoreenX.FaceChange("angry")
                            ch_d "Это слишком, [DoreenX.Petname]."


                    "\"дорогая\".":
                        if "boyfriend" in DoreenX.Petnames or ApprovalCheck(DoreenX, 600, "L"):
                            $ DoreenX.Pet = "дорогая"
                            $ DoreenX.Pet_rod = "дорогой"
                            $ DoreenX.Pet_dat = "дорогой"
                            $ DoreenX.Pet_vin = "дорогую"
                            $ DoreenX.Pet_tvo = "дорогой"
                            $ DoreenX.Pet_pre = "дорогой"
                            ch_d "Как это мило, [DoreenX.Petname]."
                        else:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Это слишком, [DoreenX.Petname]."

                    "\"секси\".":
                        if "lover" in DoreenX.Petnames or ApprovalCheck(DoreenX, 800):
                            $ DoreenX.Pet = "секси"
                            $ DoreenX.Pet_rod = "секси"
                            $ DoreenX.Pet_dat = "секси"
                            $ DoreenX.Pet_vin = "секси"
                            $ DoreenX.Pet_tvo = "секси"
                            $ DoreenX.Pet_pre = "секси"
                            $ DoreenX.FaceChange("sexy", 1)
                            ch_d "Хехе. . ."
                        else:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Это слишком, [DoreenX.Petname]."

                    "\"любимая\".":
                        if "lover" in DoreenX.Petnames or ApprovalCheck(DoreenX, 1200):
                            $ DoreenX.FaceChange("sexy", 1)
                            $ DoreenX.Pet = "любимая"
                            $ DoreenX.Pet_rod = "любимой"
                            $ DoreenX.Pet_dat = "любимой"
                            $ DoreenX.Pet_vin = "любимую"
                            $ DoreenX.Pet_tvo = "любимой"
                            $ DoreenX.Pet_pre = "любимой"
                            ch_d "Конечно."
                        else:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Я так не думаю, [DoreenX.Petname]."

                    "Назад":
                        pass

            "Грубо":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "\"рабыня\".":
                        if "master" in DoreenX.Petnames or ApprovalCheck(DoreenX, 800, "O"):
                            $ DoreenX.Pet = "рабыня"
                            $ DoreenX.Pet_rod = "рабыни"
                            $ DoreenX.Pet_dat = "рабыне"
                            $ DoreenX.Pet_vin = "рабыню"
                            $ DoreenX.Pet_tvo = "рабыней"
                            $ DoreenX.Pet_pre = "рабыне"
                            $ DoreenX.FaceChange("bemused", 1)
                            ch_d "Как пожелаешь, [DoreenX.Petname]."
                        else:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Я не рабыня, [DoreenX.Petname]."

                    "\"питомец\".":
                        if "master" in DoreenX.Petnames or ApprovalCheck(DoreenX, 650, "O"):
                            $ DoreenX.Pet = "питомец"
                            $ DoreenX.Pet_rod = "питомце"
                            $ DoreenX.Pet_dat = "питомцу"
                            $ DoreenX.Pet_vin = "питомца"
                            $ DoreenX.Pet_tvo = "питомцем"
                            $ DoreenX.Pet_pre = "питомце"
                            $ DoreenX.FaceChange("bemused", 1)
                            ch_d "Как хочешь, [DoreenX.Petname]."
                        else:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Я не питомец, [DoreenX.Petname]."

                    "\"шлюха\".":
                        if "sex friend" in DoreenX.Petnames or ApprovalCheck(DoreenX, 900, "OI"):
                            $ DoreenX.Pet = "шлюха"
                            $ DoreenX.Pet_rod = "шлюхи"
                            $ DoreenX.Pet_dat = "шлюхе"
                            $ DoreenX.Pet_vin = "шлюху"
                            $ DoreenX.Pet_tvo = "шлюхой"
                            $ DoreenX.Pet_pre = "шлюхе"
                            $ DoreenX.FaceChange("sexy")
                            ch_d "Это. . . точно. . ."
                        else:
                            $ DoreenX.FaceChange("angry", 1)
                            $ DoreenX.Mouth = "surprised"
                            ch_d "Это слишком, [DoreenX.Petname]."

                    "\"блядь\".":
                        if "fuckbuddy" in DoreenX.Petnames or ApprovalCheck(DoreenX, 1000, "OI"):
                            $ DoreenX.Pet = "блядь"
                            $ DoreenX.Pet_rod = "бляди"
                            $ DoreenX.Pet_dat = "бляде"
                            $ DoreenX.Pet_vin = "блядь"
                            $ DoreenX.Pet_tvo = "блядью"
                            $ DoreenX.Pet_pre = "бляде"
                            $ DoreenX.FaceChange("sly")
                            ch_d ". . . это довольно грубо, но ладно. . ."
                        else:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Это очень грубо, [DoreenX.Petname]."

                    "\"сладкогрудая\".":
                        if "sex friend" in DoreenX.Petnames or ApprovalCheck(DoreenX, 1400):
                            $ DoreenX.Pet = "сладкогрудая"
                            $ DoreenX.Pet_rod = "сладкогрудой"
                            $ DoreenX.Pet_dat = "сладкогрудой"
                            $ DoreenX.Pet_vin = "сладкогрудую"
                            $ DoreenX.Pet_tvo = "сладкогрудой"
                            $ DoreenX.Pet_pre = "сладкогрудой"
                            $ DoreenX.FaceChange("sly", 1)
                            ch_d "А? Ладно. . ."
                        else:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Это слишком, [DoreenX.Petname]."

                    "\"любовница\".":
                        if "sex friend" in DoreenX.Petnames or ApprovalCheck(DoreenX, 600, "I"):
                            $ DoreenX.Pet = "любовница"
                            $ DoreenX.Pet_rod = "любовницы"
                            $ DoreenX.Pet_dat = "любовнице"
                            $ DoreenX.Pet_vin = "любовницу"
                            $ DoreenX.Pet_tvo = "любовницей"
                            $ DoreenX.Pet_pre = "любовнице"
                            $ DoreenX.FaceChange("sly")
                            ch_d "Да?"
                        else:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Это слишком, [DoreenX.Petname]."

                    "\"секс-партнерша\".":
                        if "fuckbuddy" in DoreenX.Petnames or ApprovalCheck(DoreenX, 700, "I"):
                            $ DoreenX.Pet = "секс-партнерша"
                            $ DoreenX.Pet_rod = "секс-партнерши"
                            $ DoreenX.Pet_dat = "секс-партнерше"
                            $ DoreenX.Pet_vin = "секс-партнершу"
                            $ DoreenX.Pet_tvo = "секс-партнершей"
                            $ DoreenX.Pet_pre = "секс-партнерше"
                            $ DoreenX.FaceChange("sly")
                            ch_d "Да?"
                        else:
                            $ DoreenX.FaceChange("angry", 1)
                            $ DoreenX.Mouth = "surprised"
                            ch_d "Это слишком, [DoreenX.Petname]."

                    "\"доченька\".":
                        if "daddy" in DoreenX.Petnames or ApprovalCheck(DoreenX, 1200):
                            $ DoreenX.Pet = "доченька"
                            $ DoreenX.Pet_rod = "доченьки"
                            $ DoreenX.Pet_dat = "доченьке"
                            $ DoreenX.Pet_vin = "доченьку"
                            $ DoreenX.Pet_tvo = "доченькой"
                            $ DoreenX.Pet_pre = "доченьке"
                            $ DoreenX.FaceChange("smile", 1)
                            ch_d "Это просто очаровательно."
                        else:
                            $ DoreenX.FaceChange("angry", 1)
                            ch_d "Это очень странно."

                    "Назад":
                        pass

            "Неважно.":
                return
    return

#label Doreen_Namecheck(DoreenX.Pet = DoreenX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname


# start Doreen_Rename//////////////////////////////////////////////////////////
label Doreen_Rename:  #rkeljsvgb
        #Sets alternate names from Doreen
        $ DoreenX.Mouth = "smile"
        ch_d "Да?"
        menu:
            extend ""
            "Думаю, \"Дорин\" красивое имя." if DoreenX.Name != "Дорин" and "Doreen" in DoreenX.Names:
                    $ DoreenX.Name = "Дорин"
                    $ DoreenX.Name_rod = "Дорин"
                    $ DoreenX.Name_dat = "Дорин"
                    $ DoreenX.Name_vin = "Дорин"
                    $ DoreenX.Name_tvo = "Дорин"
                    $ DoreenX.Name_pre = "Дорин"
                    ch_d "Мне тоже нравится."
            "Думаю, \"Девушка-Белка\" звучит хорошо." if DoreenX.Name != "Девушка-Белка" and "Squirrel Girl" in DoreenX.Names:
                    if not ApprovalCheck(DoreenX, 500):
                            $ DoreenX.FaceChange("confused", 1)
                            ch_d "Мне [DoreenX.Name] больше нравится."
                    else:
                            if "namechange" not in DoreenX.DailyActions:
                                    $ DoreenX.Statup("Love", 70, 2)
                                    $ DoreenX.Statup("Obed", 70, 5)
                            $ DoreenX.Name_rod = "Девушки-Белки"
                            $ DoreenX.Name_dat = "Девушке-Белке"
                            $ DoreenX.Name_vin = "Девушку-Белку"
                            $ DoreenX.Name_tvo = "Девушкой-Белкой"
                            $ DoreenX.Name_pre = "Девушке-Белке"
                            $ DoreenX.Name = "Девушка-Белка"
                            $ DoreenX.FaceChange("sly", 1)
                            ch_d "Думаю, можно. . ."
            "Неважно.":
                    pass
        $ DoreenX.AddWord(1,0,"namechange")
        return
# end Doreen_Rename//////////////////////////////////////////////////////////


# start Doreen_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Doreen_Personality(Cnt = 0):   #rkeljsvgb
    if not DoreenX.Chat[4] or Cnt:
        "Поскольку у вас все хорошо получается в одной области, вы можете убедить Эмму сосредоточиться на любой другой."
        "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
        "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
    menu:
        ch_d "Да?"
        "Больше Послушания. [[Любовь в Послушание]" if DoreenX.Love > 900:
            ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
            ch_d "Ты хочешь, чтобы я была более послушной? Я попробую."
            $ DoreenX.Chat[4] = 1
        "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if DoreenX.Love > 900:
            ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
            ch_d "Ты хочешь, чтобы я была более послушной? Я попробую."
            $ DoreenX.Chat[4] = 2

        "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if DoreenX.Obed > 900:
            ch_p "Я хочу, чтобы ты была более раскрепощенной."
            ch_d "Ты хочешь, чтобы я была более раскрепощенной? Я попробую."
            $ DoreenX.Chat[4] = 3
        "Больше Любви. [[Повиновение в Любовь]" if DoreenX.Obed > 900:
            ch_p "Я хочу, чтобы ты училась любить меня."
            ch_d "Ты думаешь, что я не достаточно заботливая? Ладно, я попробую."
            $ DoreenX.Chat[4] = 4

        "Больше Повиновения. [[Раскрепощенность в Повиновение]" if DoreenX.Inbt > 900:
            ch_p "Я знаю, что нам и так весело, но разве ты не можешь иногда слушаться меня?"
            ch_d "Ты хочешь, чтобы я была более послушной? Это может быть весело."
            $ DoreenX.Chat[4] = 5

        "Больше Любви. [[Раскрепощенность в Любовь]" if DoreenX.Inbt > 900:
            ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
            ch_d "Ты думаешь, что я не достаточно заботливая? Ладно, я попробую."
            $ DoreenX.Chat[4] = 6

        "Просто делай то, что тебе нравится. . .[[Сбросить]" if DoreenX.Chat[4]:
            ch_p "Помнишь, что мы обсуждали? Забудь."
            ch_d "А. . . ладно?"
            $ DoreenX.Chat[4] = 0
        "Повторить правила":
            call Doreen_Personality(1)
            return
        "Неважно.":
            return
    return
# end Doreen_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Doreen_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Doreen_Summon(Tempmod=Tempmod): #rkeljsvgb
    $ DoreenX.OutfitChange()
    if "no summon" in DoreenX.RecentActions:
                if "no summon" in DoreenX.RecentActions:
                    ch_d "Перестань спрашивать!"
                    $ DoreenX.AddWord(1,"angry",0,0,0)
                elif Current_Time == "Night":
                    ch_d "Я же сказала тебе, уже поздно. Спокойной ночи."
                else:
                    ch_d "Я же сказала тебе, что занята."
                $ DoreenX.RecentActions.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if DoreenX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif DoreenX.Loc == "bg dangerroom":
        $ Tempmod = -10
    elif DoreenX.Loc == "bg showerroom":
        $ Tempmod = -30

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"
    if Time_Count >= 3: #night time
                if ApprovalCheck(DoreenX, 500, "L") or ApprovalCheck(DoreenX, 400, "O"):
                        #It's night time but she likes you.
                        ch_d "Думаю, я могу навестить тебя."
                        $ DoreenX.Loc = bg_current
                        call Taboo_Level
                        call Set_The_Scene
                else:
                        #It's night time and she isn't into you
                        ch_d "Извини, уже довольно поздно."
                        $ DoreenX.RecentActions.append("no summon")
                return
    elif "les" in DoreenX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(DoreenX, 2000):
                    if not Player.Male:
                        ch_d "Ко мне кое-кто заглянул, но мы были бы не против, если бы ты присоединилась к нам. . ."
                    else:
                        ch_d "Ко мне кое-кто заглянул, но мы были бы не против, если бы ты присоединился к нам. . ."
                    menu:
                        extend ""
                        "Конечно.":
                            $ Line = "go to"
                        "Нет, спасибо.":
                            ch_d "Shame you'll miss this. . ."
                            return
            else:
                    ch_d "Ох, эм, я тут немного занята."
                    ch_d "Увидимся в другой раз. . ."
                    $ DoreenX.RecentActions.append("no summon")
                    return
    elif not ApprovalCheck(DoreenX, 700, "L") or not ApprovalCheck(DoreenX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(DoreenX, 300):
                ch_d "Извини, я немного занята, [DoreenX.Petname]."
                $ DoreenX.RecentActions.append("no summon")
                return


        if "summoned" in DoreenX.RecentActions:
                pass
        elif "goto" in DoreenX.RecentActions:
                if not Player.Male:
                    ch_d "Но ты только что ушла. . ."
                else:
                    ch_d "Но ты только что ушел. . ."
        elif DoreenX.Loc == "bg classroom":
                ch_d "Я на занятиях, тоже хочешь пойти?"
        elif DoreenX.Loc == "bg dangerroom":
                ch_d "Я в Комнате Опасности, [DoreenX.Petname], хочешь присоединиться ко мне?"
        elif DoreenX.Loc == "bg campus":
                ch_d "Я отдыхаю во дворе, хочешь присоединиться ко мне?"
        elif DoreenX.Loc == "bg doreen":
                ch_d "Я в своей комнате, [DoreenX.Petname], хочешь присоединиться ко мне?"
        elif DoreenX.Loc == "bg player":
                ch_d "Я в твоей комнате, [DoreenX.Petname], хочешь присоединиться ко мне?"
        elif DoreenX.Loc == "bg showerroom":
            if ApprovalCheck(DoreenX, 1600):
                ch_d "Я сейчас в душе. Хочешь присоединиться ко мне?"
            else:
                ch_d "Я сейчас в душе, [DoreenX.Petname], увидимся позже."
                $ DoreenX.RecentActions.append("no summon")
                return
        elif DoreenX.Loc == "hold":
                ch_d "Извини, я сейчас немного занята."
                $ DoreenX.RecentActions.append("no summon")
                return
        else:
                ch_d "Ты всегда можешь прийти ко мне. . ."


        if "summoned" in DoreenX.RecentActions:
            ch_d "Снова? Ну ладно?"
            $ Line = "yes"
        elif "goto" in DoreenX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
#                                ch_d "Neat, see you then."
                                $ Line = "go to"
                "Нет.":
                                ch_d "Как хочешь."
                "Мне бы -очень- хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(DoreenX, 600, "L") or ApprovalCheck(DoreenX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(DoreenX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(DoreenX, 1400):
                                #she is generally favorable
                                ch_d "Ладно."
                                $ Line = "yes"
                        elif ApprovalCheck(DoreenX, 200, "O"):
                                #she is not obedient
                                ch_d "Оу."
                                ch_d "Ну, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(DoreenX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(DoreenX, 1400):
                                #she is generally favorable
                                ch_d "Ладно."
                                $ Line = "yes"
                        elif ApprovalCheck(DoreenX, 200, "O"):
                                #she is not obedient
                                ch_d "Оу."
                                ch_d "Ну, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Конечно, сейчас приду.":
                    $ DoreenX.Statup("Love", 55, 1)
                    $ DoreenX.Statup("Inbt", 30, 1)
#                    ch_d "Neat, see you then."
                    $ Line = "go to"

                "Нет, поговорим позже.":
                    $ DoreenX.Statup("Obed", 50, 1)
                    $ DoreenX.Statup("Obed", 30, 2)
                    ch_d "Ох, ну ладно."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                    if ApprovalCheck(DoreenX, 650, "L") or ApprovalCheck(DoreenX, 1500):
                        $ DoreenX.Statup("Love", 70, 1)
                        $ DoreenX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ DoreenX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                        ch_d "Оу, я не могу этого допустить!"

                "Приходи ко мне, будет весело.":
                    if ApprovalCheck(DoreenX, 400, "L") and ApprovalCheck(DoreenX, 800):
                        $ DoreenX.Statup("Love", 70, 1)
                        $ DoreenX.Statup("Obed", 50, 1)
                        $ Line = "fun"
                    else:
                        $ DoreenX.Statup("Inbt", 30, 1)
                        $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                    if ApprovalCheck(DoreenX, 600, "O"):
                        #she is obedient
                        $ DoreenX.Statup("Love", 50, 1, 1)
                        $ DoreenX.Statup("Love", 40, -1)
                        $ DoreenX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(DoreenX, 1500):
                        #she is generally favorable
                        $ DoreenX.Statup("Love", 70, -2)
                        $ DoreenX.Statup("Love", 90, -1)
                        $ DoreenX.Statup("Obed", 50, 2)
                        $ DoreenX.Statup("Obed", 90, 1)
                        ch_d "Ох, ладно."
                        $ Line = "yes"

                    elif ApprovalCheck(DoreenX, 200, "O"):
                        #she is not obedient
                        $ DoreenX.Statup("Love", 60, -4)
                        $ DoreenX.Statup("Love", 90, -3)
                        ch_d "Что?"
                        $ DoreenX.Statup("Inbt", 40, 2)
                        $ DoreenX.Statup("Inbt", 60, 1)
                        $ DoreenX.Statup("Obed", 70, -3)
                        ch_d "Я не подчиняюсь приказам."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ DoreenX.Statup("Inbt", 30, 1)
                        $ DoreenX.Statup("Inbt", 50, 1)
                        $ DoreenX.Statup("Love", 50, -1, 1)
                        $ DoreenX.Statup("Obed", 70, -1)
                        $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                    if ApprovalCheck(DoreenX, 600, "O"):
                        #she is obedient
                        $ DoreenX.Statup("Love", 50, 1, 1)
                        $ DoreenX.Statup("Love", 40, -1)
                        $ DoreenX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(DoreenX, 1500):
                        #she is generally favorable
                        $ DoreenX.Statup("Love", 70, -2)
                        $ DoreenX.Statup("Love", 90, -1)
                        $ DoreenX.Statup("Obed", 50, 2)
                        $ DoreenX.Statup("Obed", 90, 1)
                        ch_d "Ох, ладно."
                        $ Line = "yes"

                    elif ApprovalCheck(DoreenX, 200, "O"):
                        #she is not obedient
                        $ DoreenX.Statup("Love", 60, -4)
                        $ DoreenX.Statup("Love", 90, -3)
                        ch_d "Что?"
                        $ DoreenX.Statup("Inbt", 40, 2)
                        $ DoreenX.Statup("Inbt", 60, 1)
                        $ DoreenX.Statup("Obed", 70, -3)
                        ch_d "Я не подчиняюсь приказам."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ DoreenX.Statup("Inbt", 30, 1)
                        $ DoreenX.Statup("Inbt", 50, 1)
                        $ DoreenX.Statup("Love", 50, -1, 1)
                        $ DoreenX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if DoreenX.Love > DoreenX.Obed:
            ch_d "Конечно!"
        else:
            ch_d "Конечно, уже иду."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ DoreenX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            if DoreenX.Loc == "bg classroom":
                ch_d "Я никак не могу пропустить эту лекцию."
            elif DoreenX.Loc == "bg dangerroom":
                ch_d "Я только-только разогрелась!"
            else:
                ch_d "Извини, [DoreenX.Petname], я очень занята."
            $ DoreenX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ DoreenX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            $ Nearby = []
            $ Line = 0
            $ Party = [DoreenX]
            if DoreenX.Loc == "bg classroom":
                    ch_d "Здорово, найди меня, как придешь."
                    jump Class_Room
            elif DoreenX.Loc == "bg dangerroom":
                    ch_d "Здорово, я пока разогреюсь."
                    jump Danger_Room
            elif DoreenX.Loc == "bg doreen":
                    ch_d "Я. . . пока приберусь."
                    jump Doreen_Room
            elif DoreenX.Loc == "bg player":
                    ch_d "Увидимся, когда придешь."
                    jump Player_Room
            elif DoreenX.Loc == "bg showerroom":
                    ch_d "Я оставлю тебе немного горячей воды."
                    jump Shower_Room
            elif DoreenX.Loc == "bg campus":
                    ch_d "До встречи."
                    jump Campus
            elif DoreenX.Loc != "hold":
                    ch_d "Конечно, увидимся."
                    $ bg_current = DoreenX.Loc
                    jump Misplaced
            else:
                    ch_d "Возможно, я просто встречу тебя в своей комнате."
                    $ DoreenX.Loc = "bg doreen"
                    jump Doreen_Room

    #She's agreed to come over
    elif Line == "lonely":
            if not Player.Male:
                ch_d "Я никак не могу оставить тебя одну. . ."
            else:
                ch_d "Я никак не могу оставить тебя одного. . ."
    elif Line == "command":
            ch_d "Ладно, [DoreenX.Petname]."
    elif Line == "fun":
            ch_d "Конечно."

    $ DoreenX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(DoreenX)
            return
    $ DoreenX.Loc = bg_current
    call Taboo_Level(0)
    $ DoreenX.OutfitChange()
    call Set_The_Scene
    return

# End Doreen Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Doreen_Leave(Tempmod=Tempmod, GirlsNum = 0):    #rkeljsvgb
    if "leaving" in DoreenX.RecentActions:
        $ DoreenX.DrainWord("leaving")
    else:
        return

    if DoreenX.Loc == "hold":
            # Activates if she's being moved out of play
            ch_d "Мне нужно ненадолго отлучиться, увидимся позже."
            return

    if DoreenX in Party or "lockedtravels" in DoreenX.Traits:
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ DoreenX.Loc = bg_current
            return

    elif "freetravels" in DoreenX.Traits or not ApprovalCheck(DoreenX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.
            $ DoreenX.OutfitChange()
            if GirlsNum: #if someone left before her
                        ch_d "Ага, я тоже пошла."

            if DoreenX.Loc == "bg classroom":
                        ch_d "У меня занятия."
            elif DoreenX.Loc == "bg dangerroom":
                        ch_d "Я собираюсь позаниматься в Комнате Опасности."
            elif DoreenX.Loc == "bg campus":
                        ch_d "Отдохну во дворе."
            elif DoreenX.Loc == "bg doreen":
                        ch_d "Я возвращаюсь в свою комнату."
            elif DoreenX.Loc == "bg player":
                        ch_d "Я немного побуду в твоей комнате."
            elif DoreenX.Loc == "bg pool":
                        ch_d "Я собираюсь искупаться."
            elif DoreenX.Loc == "bg showerroom":
                if ApprovalCheck(DoreenX, 1400):
                        ch_d "Я собираюсь принять душ."
                else:
                        ch_d "Увидимся."
            else:
                        ch_d "До встречи."
            hide Doreen_Sprite
            hide Doreen_Seated
            return
            #End Free Travels

    if bg_current == "bg dangerroom":
            call Gym_Exit([DoreenX])

    $ DoreenX.OutfitChange()

    if "follow" not in DoreenX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ DoreenX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    # Sets her preferences
    if DoreenX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif DoreenX.Loc == "bg dangerroom":
        $ Tempmod = 20
    elif DoreenX.Loc == "bg showerroom":
        $ Tempmod = 40


    if GirlsNum: #if someone left before her
                ch_d "Ага, я тоже пойду."

    if DoreenX.Loc == "bg classroom":
            ch_d "Я на занятия, не хочешь со мной?"
    elif DoreenX.Loc == "bg dangerroom":
            ch_d "Я в Комнату Опасности, [DoreenX.Petname], не хочешь со мной?"
    elif DoreenX.Loc == "bg campus":
            ch_d "Я хочу отдохнуть во дворе, не хочешь со мной?"
    elif DoreenX.Loc == "bg doreen":
            ch_d "Я в свою комнату, [DoreenX.Petname], не хочешь со мной?"
    elif DoreenX.Loc == "bg player":
            ch_d "Я в твою комнату, [DoreenX.Petname], не хочешь со мной?"
    elif DoreenX.Loc == "bg mall":
            ch_d "Я в торговый центр, [DoreenX.Petname], не хочешь со мной?"
    elif DoreenX.Loc == "bg showerroom":
        if ApprovalCheck(DoreenX, 1600):
            ch_d "Я в душ. Не хочешь со мной?"
        else:
            ch_d "Я в душ, [DoreenX.Petname], увидимся позже."
            return
    elif DoreenX.Loc == "bg pool":
            ch_d "Я к бассейну. Не хочешь со мной?"
    else:
            ch_d "Не хочешь со мной?"


    menu:
        extend ""
        "Конечно, я сразу за тобой.":
                if "followed" not in DoreenX.RecentActions:
                    $ DoreenX.Statup("Love", 55, 1)
                    $ DoreenX.Statup("Inbt", 30, 1)
                $ Line = "go to"

        "Нет, поговорим позже.":
                if "followed" not in DoreenX.RecentActions:
                    $ DoreenX.Statup("Obed", 50, 1)
                    $ DoreenX.Statup("Obed", 30, 2)
                ch_d "Ох, ладно."

        "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                if ApprovalCheck(DoreenX, 650, "L") or ApprovalCheck(DoreenX, 1500):
                    if "followed" not in DoreenX.RecentActions:
                        $ DoreenX.Statup("Love", 70, 1)
                        $ DoreenX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else:
                    if "followed" not in DoreenX.RecentActions:
                        $ DoreenX.Statup("Inbt", 30, 1)
                    $ Line = "no"
                    ch_d "Оу, это так мило."

        "Останься, будет весело.":
                if ApprovalCheck(DoreenX, 400, "L") and ApprovalCheck(DoreenX, 800):
                    $ DoreenX.Statup("Love", 70, 1)
                    $ DoreenX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else:
                    $ DoreenX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Нет, останься здесь.":
                if ApprovalCheck(DoreenX, 600, "O"):
                    #she is obedient
                    if "followed" not in DoreenX.RecentActions:
                        $ DoreenX.Statup("Love", 40, -2)
                        $ DoreenX.Statup("Obed", 90, 1)
                    $ Line = "command"

                elif D20 >= 7 and ApprovalCheck(DoreenX, 1400):
                    #she is generally favorable
                    if "followed" not in DoreenX.RecentActions:
                        $ DoreenX.Statup("Love", 70, -2)
                        $ DoreenX.Statup("Love", 90, -1)
                        $ DoreenX.Statup("Obed", 50, 2)
                        $ DoreenX.Statup("Obed", 90, 1)
                    ch_d "Ладно, я могу немного задержаться."
                    $ Line = "yes"

                elif ApprovalCheck(DoreenX, 200, "O"):
                    #she is not obedient
                    if "followed" not in DoreenX.RecentActions:
                        $ DoreenX.Statup("Love", 70, -4)
                        $ DoreenX.Statup("Love", 90, -2)
                    ch_d "Что?"
                    if "followed" not in DoreenX.RecentActions:
                        $ DoreenX.Statup("Inbt", 40, 2)
                        $ DoreenX.Statup("Inbt", 60, 1)
                        $ DoreenX.Statup("Obed", 70, -2)
                    ch_d "Я не собираюсь здесь задерживаться."
                else:
                    #she is obedient, but you failed to meet the checks
                    if "followed" not in DoreenX.RecentActions:
                        $ DoreenX.Statup("Inbt", 30, 1)
                        $ DoreenX.Statup("Inbt", 50, 1)
                        $ DoreenX.Statup("Love", 50, -1, 1)
                        $ DoreenX.Statup("Love", 90, -2)
                        $ DoreenX.Statup("Obed", 70, -1)
                    $ Line = "no"
                #End ordered to stay

    call Taboo_Level(0)
    $ DoreenX.RecentActions.append("followed")
    if not Line:
            #You end the dialog neutrally
            hide Doreen_Sprite
            hide Doreen_Seated
            call Gym_Clothes_Off([DoreenX])
            return

    if Line == "no":
            # She's refused, context based dialog
            if DoreenX.Loc == "bg classroom":
                ch_d "Я никак не могу пропустить это занятие."
            elif DoreenX.Loc == "bg dangerroom":
                ch_d "Извини, [DoreenX.Petname], но мне очень нужно позаниматься."
            else:
                ch_d "Извини, но у меня еще много дел."
            hide Doreen_Sprite
            hide Doreen_Seated
            call Gym_Clothes_Off([DoreenX])
            return

    elif Line == "go to":
            #You agreed to go to her instead
            #$ Party.append(DoreenX)
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")
            $ DoreenX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            hide Doreen_Sprite
            hide Doreen_Seated
            $ Nearby = []
            $ Party = [DoreenX]
            call Gym_Clothes_Off([DoreenX])
            if DoreenX.Loc == "bg classroom":
                ch_d "Здорово, я займу тебе местечко."
                jump Class_Room_Entry
            elif DoreenX.Loc == "bg dangerroom":
                ch_d "Тогда я пока разомнусь."
                jump Danger_Room_Entry
            elif DoreenX.Loc == "bg doreen":
                ch_d "Здорово."
                jump Doreen_Room
            elif DoreenX.Loc == "bg player":
                ch_d "Здорово."
                jump Player_Room
            elif DoreenX.Loc == "bg showerroom":
                ch_d "Здорово."
                jump Shower_Room_Entry
            elif DoreenX.Loc == "bg campus":
                ch_d "Ох, здорово."
                jump Campus_Entry
            elif DoreenX.Loc == "bg pool":
                ch_d "Здорово."
                jump Pool_Entry
            elif DoreenX.Loc == "bg mall":
                ch_d "Здорово."
                jump Mall_Entry
            else:
                ch_d "Тогда я просто встречусь с тобой в твоей комнате."
                $ DoreenX.Loc = "bg player"
                jump Player_Room
            #End "goto" where she's at

    #She's agreed to come over
    elif Line == "lonely":
            if not Player.Male:
                ch_d "Я просто не могу оставить тебя одну. . ."
            else:
                ch_d "Я просто не могу оставить тебя одного. . ."
    elif Line == "command":
            ch_d "Ладно, [DoreenX.Petname]."
    elif Line:
            ch_d "Конечно."

    $ Line = 0
    ch_d "Я останусь здесь."
    $ DoreenX.Loc = bg_current
    call Taboo_Level(0)
    return

# End Doreen Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

### Doreen's Clothes  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Doreen_Clothes:   #rkeljsvgb
    if DoreenX.Taboo:
            if "exhibitionist" in DoreenX.Traits:
                ch_d "Да? . ."
            elif ApprovalCheck(DoreenX, 900, TabM=4) or ApprovalCheck(DoreenX, 400, "I", TabM=3):
                ch_d "Мы не в том месте, где я хотела бы переодеваться. . ."
            else:
                ch_d "Мы не в том месте, где я хотела бы переодеваться. . ."
                ch_d "Может, поговорим об этом в одной из наших комнат?"
                return
    elif ApprovalCheck(DoreenX, 900, TabM=4) or ApprovalCheck(DoreenX, 600, "L") or ApprovalCheck(DoreenX, 300, "O"):
                ch_d "Что ты хочешь обсудить?"
    else:
                ch_d "Почему тебя так беспокоит моя одежда?"
                return

    if Girl != DoreenX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = DoreenX
    call Shift_Focus(Girl)

label Doreen_Wardrobe_Menu:
    $ DoreenX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .
    while True:
        menu:
            ch_d "Что ты хочешь обсудить?"
            "Верх":
                        call Doreen_Clothes_Over
            "Низ":
                        call Doreen_Clothes_Legs
            "Нижнее белье":
                        call Doreen_Clothes_Under
            "Аксессуары":
                        call Doreen_Clothes_Misc
            "Управление нарядами":
                        call Doreen_Clothes_Outfits
            "Давай поговорим о том, что ты носишь.":
                        call Clothes_Schedule(DoreenX)

            "Могу я посмотреть?" if DoreenX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(DoreenX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_d "Ладно, как я выгляжу?"
                    hide PhoneSex
            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(DoreenX,0,2)
                    if _return:
                        hide DressScreen
            "Может, тебе будет комфортнее за ширмой? (locked)" if DoreenX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if DoreenX.Loc == bg_current and not DoreenX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if not Player.Male and "girltalk" not in DoreenX.History and "nogirls" not in DoreenX.History:
                            ch_d "Ох, зачем?"
                    elif ApprovalCheck(DoreenX, 1500) or (DoreenX.SeenChest and DoreenX.SeenPussy):
                            if not Player.Male:
                                ch_d "Я думаю, ты уже видела достаточно."
                            else:
                                ch_d "Я думаю, ты уже видел достаточно."
                    else:
                            show DressScreen zorder 150
                            ch_d "Эм, ага, спасибо."

            "У меня есть подарок для тебя (locked)" if DoreenX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if DoreenX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(DoreenX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ DoreenX.OutfitChange()
                    $ DoreenX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != DoreenX:
                            ch_p "Я хочу поговорить о твоей одежде."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = DoreenX
                    call Shift_Focus(Girl)

            "Сменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current:
                    pass
            "Сменить вид" if Girl.Loc == bg_current:
                    call WardrobeView(DoreenX)

            "Неважно, ты и так хорошо выглядишь":
                    call Girl_Pos_Reset(DoreenX)
                    if "wardrobe" not in DoreenX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if DoreenX.Chat[1] <= 1:
                                    $ DoreenX.Statup("Love", 70, 15)
                                    $ DoreenX.Statup("Obed", 40, 20)
                                    ch_d "Ох! Спасибо!"
                            elif DoreenX.Chat[1] <= 10:
                                    $ DoreenX.Statup("Love", 70, 5)
                                    $ DoreenX.Statup("Obed", 40, 7)
                                    ch_d "Да?"
                            elif DoreenX.Chat[1] <= 50:
                                    $ DoreenX.Statup("Love", 70, 1)
                                    $ DoreenX.Statup("Obed", 40, 1)
                                    ch_d "Да? Ладно."
                            else:
                                    ch_d "Конечно."
                            $ DoreenX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(DoreenX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ DoreenX.OutfitChange()
                    $ DoreenX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ DoreenX.Chat[1] += 1
                    $ Trigger = 0
                    if DoreenX.Panties and "pantyless" in DoreenX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ DoreenX.DailyActions.remove("pantyless")
                    return

        #Loops back up
        #return #jump Doreen_Clothes
        #End of Doreen Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Doreen_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(DoreenX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(DoreenX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(DoreenX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(DoreenX,4,1)
                    "Одежда для сна":
                                call OutfitShame(DoreenX,7,1)
                    "Купальник":
                                call OutfitShame(DoreenX,10,1)

                    "Повседневка 1" if ApprovalCheck(DoreenX, 2500):
                                call OutfitShame(DoreenX,11,1)
                    "Повседневка 2" if ApprovalCheck(DoreenX, 2500):
                                call OutfitShame(DoreenX,12,1)
                    #8 is Emma's teaching clothes,
                    "Неважно":
                                pass

        "Примерь пиджак и шорты.":
                $ DoreenX.OutfitChange("casual1")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                            $ DoreenX.Outfit = "casual1"
                            $ DoreenX.Shame = 0
                            ch_d "В этом я чувствую себя очень комфортно."
                    "Давай попробуем что-нибудь другое.":
                            ch_d "Ох."

        "Примерь футболку и юбку.":
                $ DoreenX.OutfitChange("casual2")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                            $ DoreenX.Outfit = "casual2"
                            $ DoreenX.Shame = 0
                            ch_d "В этом я выгляжу очень мило."
                    "Давай попробуем что-нибудь другое.":
                            ch_d "Ох."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not DoreenX.Custom1[0] and not DoreenX.Custom2[0] and not DoreenX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if DoreenX.Custom1[0] or DoreenX.Custom2[0] or DoreenX.Custom3[0]:
                $ Cnt = 0
                while 1:
                    menu:
                        "Надень Пользовательский 1 (locked)" if not DoreenX.Custom1[0]:
                                pass
                        "Надень Пользовательский 1" if DoreenX.Custom1[0]:
                                $ DoreenX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Надень Пользовательский 2 (locked)" if not DoreenX.Custom2[0]:
                                pass
                        "Надень Пользовательский 2" if DoreenX.Custom2[0]:
                                $ DoreenX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Надень Пользовательский 3 (locked)" if not DoreenX.Custom3[0]:
                                pass
                        "Надень Пользовательский 3" if DoreenX.Custom3[0]:
                                $ DoreenX.OutfitChange("custom3")
                                $ Cnt = 6

                        "Ты должна одеваться так, когда мы наедине (locked)" if not Cnt:
                                pass
                        "Ты должна одеваться так, когда мы наедине" if Cnt:
                                if Cnt == 5:
                                    $ DoreenX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ DoreenX.Clothing[9] = "custom3"
                                else:
                                    $ DoreenX.Clothing[9] = "custom1"
                                ch_d "Ох, конечно."

                        "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                menu:
                                    "Пользовательский 1 [[очистить слот 1]" if DoreenX.Custom1[0]:
                                        ch_d "Ох."
                                        $ DoreenX.Custom1[0] = 0
                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not DoreenX.Custom1[0]:
                                        pass
                                    "Пользовательский 2 [[очистить слот 2]" if DoreenX.Custom2[0]:
                                        ch_d "Ох."
                                        $ DoreenX.Custom2[0] = 0
                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not DoreenX.Custom2[0]:
                                        pass
                                    "Пользовательский 3 [[очистить слот 3]" if DoreenX.Custom3[0]:
                                        ch_d "Ох."
                                        $ DoreenX.Custom3[0] = 0
                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not DoreenX.Custom3[0]:
                                        pass
                                    "Неважно [[назад]":
                                        pass

                        "Тебе следует надеть его [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                pass
                        "Тебе следует надеть его" if Cnt:
                                call Custom_Out(DoreenX,Cnt)
                        "Ладно, вернемся к началу нашего разговора. . .":
                                $ Cnt = 0
                                return #jump Doreen_Clothes

        "Наденешь спортивную одежду?" if not DoreenX.Taboo or bg_current == "bg dangerroom":
                $ DoreenX.OutfitChange("gym")

        "Наденешь одежду для сна?" if not DoreenX.Taboo:
                if ApprovalCheck(DoreenX, 1200):
                        $ DoreenX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(DoreenX)
                        if _return:
                            $ DoreenX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (DoreenX.Taboo and bg_current != "bg pool" and not ApprovalCheck(DoreenX, 800, TabM=2)) or not DoreenX.Swim[0]:
                $ DoreenX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not DoreenX.Taboo or bg_current == "bg pool" or ApprovalCheck(DoreenX, 800, TabM=2)) and DoreenX.Swim[0]:
                $ DoreenX.OutfitChange("swimwear")

        "Наденешь хэллоуинский костюм?" if "halloween" in DoreenX.History:
                ch_d "Ладно."
                $ DoreenX.OutfitChange("costume")

        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ DoreenX.FaceChange("sexy", 1)
                $ Line = 0
                if not DoreenX.Chest and not DoreenX.Panties and not DoreenX.Over and not DoreenX.Legs and not DoreenX.Hose:
                    ch_d "Ох. . . подожди, откуда ты знаешь?!"
                elif DoreenX.SeenChest and DoreenX.SeenPussy and ApprovalCheck(DoreenX, 1200, TabM=4):
                    ch_d "Спасибо? . ."
                    $ Line = 1
                elif ApprovalCheck(DoreenX, 2000, TabM=4):
                    ch_d "Ладно. . ."
                    $ Line = 1
                elif DoreenX.SeenChest and DoreenX.SeenPussy and ApprovalCheck(DoreenX, 1200, TabM=0):
                    ch_d "Возможно, но я не хочу выставлять себя напоказ. . ."
                elif ApprovalCheck(DoreenX, 2000, TabM=0):
                    ch_d "Возможно, но я не хочу выставлять себя напоказ. . ."
                elif ApprovalCheck(DoreenX, 1000, TabM=0):
                    $ DoreenX.FaceChange("confused", 1,Mouth="smirk")
                    ch_d "Возможно, но я не хочу выставлять себя напоказ. . ."
                    $ DoreenX.FaceChange("bemused", 0)
                else:
                    $ DoreenX.FaceChange("angry", 1)
                    ch_d "Что?"

                call expression DoreenX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in DoreenX.History:
                        $ Line = 0
                if Line:
                    #If she got nude. . .
                    $ DoreenX.OutfitChange("nude")
                    "Она сбрасывает одежду к своим ногам."
                    call Girl_First_Topless(DoreenX)
                    call Girl_First_Bottomless(DoreenX,1)
                    $ DoreenX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется. что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in DoreenX.Traits:
                                ch_d "Ох, ого. . ."
                                $ DoreenX.Outfit = "nude"
                                $ DoreenX.Statup("Lust", 50, 10)
                                $ DoreenX.Statup("Lust", 70, 5)
                                $ DoreenX.Shame = 50
                            elif ApprovalCheck(DoreenX, 800, "I") or ApprovalCheck(DoreenX, 2800, TabM=0):
                                ch_d "Ооох, эм. . ."
                                $ DoreenX.Outfit = "nude"
                                $ DoreenX.Shame = 50
                            else:
                                $ DoreenX.FaceChange("sexy", 1)
                                $ DoreenX.Eyes = "surprised"
                                ch_d "Ни за что!"

                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in DoreenX.Traits:
                                ch_d "О, правда?"
                            elif ApprovalCheck(DoreenX, 800, "I") or ApprovalCheck(DoreenX, 2800, TabM=0):
                                $ DoreenX.FaceChange("bemused", 1)
                                ch_d "Ты не хочешь, чтобы я ходила так? . ."
                                ch_d ". . ."
                            else:
                                $ DoreenX.FaceChange("confused", 1)
                                ch_d "Я не против ходить голой только при тебе. . ."
                $ Line = 0

        "Неважно":
            return #jump Doreen_Clothes

    return #jump Doreen_Clothes
    #End of Doreen Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Doreen_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять [get_clothing_name(DoreenX.Over_key, vin)]?" if DoreenX.Over:
                call Wardrobe_Remove(DoreenX)

        "Примерь коричневую майку." if DoreenX.Over != "tube top":
                $ DoreenX.FaceChange("bemused")
                if not DoreenX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_d "Конечно."
                elif ApprovalCheck(DoreenX, 800, TabM=0):
                    ch_d "Конечно."
                else:
                    call Display_DressScreen(DoreenX)
                    if not _return:
                            $ DoreenX.FaceChange("bemused", 1)
                            ch_d "Я не хочу сейчас переодевать [get_clothing_name(DoreenX.Over_key, vin)]."
                            return #jump Doreen_Clothes
                $ DoreenX.Over = "tube top"

        "Примерь серую футболку." if DoreenX.Over != "tshirt":
                $ DoreenX.FaceChange("bemused")
                if not DoreenX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_d "Конечно."
                elif ApprovalCheck(DoreenX, 800, TabM=0):
                    ch_d "Конечно."
                else:
                    call Display_DressScreen(DoreenX)
                    if not _return:
                            $ DoreenX.FaceChange("bemused", 1)
                            ch_d "Я не хочу сейчас переодевать [get_clothing_name(DoreenX.Over_key, vin)]."
                            return #jump Doreen_Clothes
                $ DoreenX.Over = "tshirt"

        "Примерь желтый свитер." if DoreenX.Over != "sweater" and "halloween" in DoreenX.History:
                $ DoreenX.FaceChange("bemused")
                if not DoreenX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_d "Конечно."
                elif ApprovalCheck(DoreenX, 800, TabM=0):
                    ch_d "Конечно."
                else:
                    call Display_DressScreen(DoreenX)
                    if not _return:
                            $ DoreenX.FaceChange("bemused", 1)
                            ch_d "Я не хочу сейчас переодевать [get_clothing_name(DoreenX.Over_key, vin)]."
                            return #jump Doreen_Clothes
                $ DoreenX.Over = "sweater"

        "Может, просто накинешь полотенце?" if DoreenX.Over != "towel":
                $ DoreenX.FaceChange("bemused", 1)
                if DoreenX.Chest or DoreenX.SeenChest:
                    ch_d "Ты серьезно? . ."
                elif ApprovalCheck(DoreenX, 1000, TabM=0):
                    $ DoreenX.FaceChange("perplexed", 1)
                    ch_d "Ладно. . ."
                else:
                    call Display_DressScreen(DoreenX)
                    if not _return:
                            ch_d "Это. . . как-то странно."
                            return #jump Doreen_Clothes
                $ DoreenX.Over = "towel"

        "Примерь кожаную куртку." if DoreenX.Acc != "jacket":
                $ DoreenX.FaceChange("bemused")
                ch_d "Конечно."
                $ DoreenX.Acc = "jacket"
        "Примерь кожаную безрукавку." if DoreenX.Acc != "vest" and "vest" in DoreenX.Inventory:
                $ DoreenX.FaceChange("bemused")
                ch_d "Конечно."
                $ DoreenX.Acc = "vest"
        "Сними [get_clothing_name(DoreenX.Acc_key, vin)]." if DoreenX.Acc:
                $ DoreenX.FaceChange("bemused")
                ch_d "Конечно."
                $ DoreenX.Acc = 0

        "Неважно":
            pass
    return #jump Doreen_Clothes
    #End of Doreen Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Doreen_NoBra:
        menu:
            ch_d "У меня под [get_clothing_name(DoreenX.Over_key, tvo)] ничего нет. . ."
            "Тогда надень что-нибудь. . .":
                        if DoreenX.SeenChest and ApprovalCheck(DoreenX, 1000, TabM=3):
                                $ DoreenX.Blush = 1
                                ch_d "Ну, вообще-то, я не говорила, что меня это беспокоит. . ."
                                $ DoreenX.Blush = 0
                        elif ApprovalCheck(DoreenX, 1200, TabM=4):
                                $ DoreenX.Blush = 1
                                ch_d "Ну, вообще-то, я не говорила, что меня это беспокоит. . ."
                                $ DoreenX.Blush = 0
                        elif ApprovalCheck(DoreenX, 900, TabM=2) and "lace bra" in DoreenX.Inventory:
                                ch_d "Думаю, я могу что-нибудь подобрать."
                                $ DoreenX.Chest  = "lace bra"
                                "Она достает свой кружевной лифчик и надевает его под [get_clothing_name(DoreenX.Over_key, vin)]."
                        elif ApprovalCheck(DoreenX, 700, TabM=2):
                                ch_d "Думаю, я могу что-нибудь подобрать."
                                $ DoreenX.Chest = "bra"
                                "Она достает коричневый лифчик и надевает его под [get_clothing_name(DoreenX.Over_key, vin)]."
                        else:
                                ch_d "Я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(DoreenX, 1100, "LI", TabM=2) and DoreenX.Love > DoreenX.Inbt:
                                ch_d "Для тебя? Наверное. . ."
                        elif ApprovalCheck(DoreenX, 700, "OI", TabM=2) and DoreenX.Obed > DoreenX.Inbt:
                                ch_d "Конечно. . ."
                        elif ApprovalCheck(DoreenX, 600, "I", TabM=2):
                                ch_d "Ага. . ."
                        elif ApprovalCheck(DoreenX, 1300, TabM=2):
                                ch_d "Согласна."
                        else:
                                $ DoreenX.FaceChange("surprised")
                                $ DoreenX.Brows = "angry"
                                if DoreenX.Taboo > 20:
                                    ch_d "Но не на людях! Извини."
                                else:
                                    if not Player.Male:
                                        ch_d "Ты не настолько милая, [DoreenX.Petname]!"
                                    else:
                                        ch_d "Ты не настолько милый, [DoreenX.Petname]!"
                                call expression DoreenX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0
            "Неважно.":
                        ch_d "Ладно. . ."
                        return 0
        return 1
        #End of Doreen bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Doreen_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(DoreenX.Legs_key, vin)]?" if DoreenX.Legs:
                call Wardrobe_Remove(DoreenX,1)

        "Примерь коричневые шорты" if DoreenX.Legs != "shorts":
                ch_p "Ты великолепно выглядишь в коричневых шортах."
                ch_d "Да?"
                $ DoreenX.Legs = "shorts"

        "Примерь зеленую юбку" if DoreenX.Legs != "skirt":
                ch_p "Примеришь зеленую юбки?"
                ch_d "Да?"
                $ DoreenX.Legs = "skirt"
        "Примерь красную юбку" if DoreenX.Legs != "red skirt" and "halloween" in DoreenX.History:
                ch_p "Примеришь красную юбки?"
                ch_d "Да?"
                $ DoreenX.Legs = "red skirt"

        "Сними обувь (locked)" if not DoreenX.Boots:
                pass
        "Сними [get_clothing_name(DoreenX.Boots_key, vin)]" if DoreenX.Boots:
                ch_p "Может, снимешь [get_clothing_name(DoreenX.Boots_key, vin)]?"
                ch_d "Ладно."
                $ DoreenX.Boots = 0
        "Надень кеды" if DoreenX.Boots != "sneaks":
                ch_p "Может, наденешь кеды?"
                ch_d "Ладно."
                $ DoreenX.Boots = "sneaks"
        "Надень ботинки" if DoreenX.Boots != "boots":
                ch_p "Может, наденешь ботинки?"
                ch_d "Ладно."
                $ DoreenX.Boots = "boots"
#        "Add Sneakers" if DoreenX.Boots != "sneaks":
#                ch_p "Maybe put your sneakers on."
#                ch_d "'K."
#                $ DoreenX.Boots = "sneaks"

        "Неважно":
                pass
    return #jump Doreen_Clothes
    #End of Doreen Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Doreen_NoPantiesOn:
        menu:
            ch_d "На мне, эм. . . нет трусиков. . ."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if DoreenX.SeenPussy and ApprovalCheck(DoreenX, 1100, TabM=4):
                                $ DoreenX.Blush = 1
                                ch_d "Я не уверена, честно говоря, мне нравится без них. . ."
                                $ DoreenX.Blush = 0
                        elif ApprovalCheck(DoreenX, 1500, TabM=4):
                                $ DoreenX.Blush = 1
                                ch_d "Я не уверена, честно говоря, мне нравится без них. . ."
                                $ DoreenX.Blush = 0
                        elif ApprovalCheck(DoreenX, 700, TabM=4):
                                ch_d "Ох, наверное."
                                if "lace panties" in DoreenX.Inventory:
                                        ch_d "Мне нравится ход твоих мыслей."
                                        $ DoreenX.Panties  = "lace panties"
                                else:
                                        $ DoreenX.Panties = "tan panties"
                                if ApprovalCheck(DoreenX, 1200, TabM=4):
                                    $ Line = get_clothing_name(DoreenX.Legs_key, vin)
                                    $ DoreenX.Legs = 0
                                    "Она снимает [Line] и натягивает [get_clothing_name(DoreenX.Panties_key, vin)]."
                                elif DoreenX.Legs == "skirt":
                                    "Она достает [get_clothing_name(DoreenX.Panties_key, vin)] и натягивает их под юбку."
                                    $ DoreenX.Legs = 0
                                    "Затем она сбрасывает юбку на пол."
                                else:
                                    $ Line = get_clothing_name(DoreenX.Legs_key, vin)
                                    $ DoreenX.Legs = 0
                                    "Она отходит на мгновение, а затем возвращается в [get_clothing_name(DoreenX.Panties_key, pre)]."
                                return #jump Doreen_Clothes
                        else:
                                ch_d "Я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(DoreenX, 1100, "LI", TabM=3) and DoreenX.Love > DoreenX.Inbt:
                                ch_d "Ох, ого. . ."
                        elif ApprovalCheck(DoreenX, 700, "OI", TabM=3) and DoreenX.Obed > DoreenX.Inbt:
                                ch_d "Конечно. . ."
                        elif ApprovalCheck(DoreenX, 600, "I", TabM=3):
                                ch_d "Ооох. . ."
                        elif ApprovalCheck(DoreenX, 1300, TabM=3):
                                ch_d "Хм. . ."
                        else:
                                $ DoreenX.FaceChange("surprised")
                                $ DoreenX.Brows = "angry"
                                if DoreenX.Taboo > 20:
                                    ch_d "Но не на людях."
                                else:
                                    if not Player.Male:
                                        ch_d "Ты не настолько милая, [DoreenX.Petname]!"
                                    else:
                                        ch_d "Ты не настолько милый, [DoreenX.Petname]!"
                                call expression DoreenX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно.":
                ch_d "Ох. . ."
                return 0
        return 1
        #End of Doreen Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Doreen_Clothes_Under:
        "Верх":
            menu:
                "Может, снимешь [get_clothing_name(DoreenX.Chest_key, vin)]?" if DoreenX.Chest:
                        $ DoreenX.FaceChange("bemused", 1)
                        if DoreenX.SeenChest and ApprovalCheck(DoreenX, 900, TabM=2.7):
                                ch_d "Конечно."
                        elif ApprovalCheck(DoreenX, 1100, TabM=2):
                            if DoreenX.Taboo:
                                ch_d "Я не хочу делать это здесь. . ."
                            else:
                                ch_d "Наверное, можно. . ."
#                        elif DoreenX.Over == "jacket" and ApprovalCheck(DoreenX, 600, TabM=2):
#                            ch_d "This jacket is a bit revealing. . ."
                        elif DoreenX.Over and ApprovalCheck(DoreenX, 500, TabM=2):
                            ch_d "Думаю, можно. . ."
                        elif not DoreenX.Over:
                            call Display_DressScreen(DoreenX)
                            if not _return:
                                ch_d "Я не очень хочу это делать."
                                return #jump Doreen_Clothes
                        else:
                            call Display_DressScreen(DoreenX)
                            if not _return:
                                ch_d "Я так не думаю."
                                return #jump Doreen_Clothes
                        $ Line = get_clothing_name(DoreenX.Chest_key, vin)
                        $ DoreenX.Chest = 0
                        if DoreenX.Over:
                            "Она залезает под [get_clothing_name(DoreenX.Over_key, vin)], хватает и снимает [Line], а затем бросает на пол."
                        else:
                            "Она скидывает [Line] на пол."
                            if not renpy.showing('DressScreen'):
                                call Girl_First_Topless(DoreenX)

                "Примерь коричневый лифчик" if DoreenX.Chest != "tan bra":
                        ch_p "Мне нравится твой коричневый лифчик."
                        if DoreenX.SeenChest or ApprovalCheck(DoreenX, 1100, TabM=2):
                            ch_d "Да?"
                            $ DoreenX.Chest = "tan bra"
                        else:
                            call Display_DressScreen(DoreenX)
                            if not _return:
                                ch_d "Он довольно маленький. . ."
                            else:
                                $ DoreenX.Chest = "tan bra"


                "Примерь кружевной лифчик" if DoreenX.Chest != "lace bra" and "lace bra" in DoreenX.Inventory:
                        ch_p "Мне нравится твой кружевной лифчик."
                        if DoreenX.SeenChest or ApprovalCheck(DoreenX, 1300, TabM=2):
                            ch_d "Да?"
                            $ DoreenX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(DoreenX)
                            if not _return:
                                ch_d "Он довольно прозрачный. . ."
                            else:
                                $ DoreenX.Chest = "lace bra"

                "Примерь спортивный лифчик" if DoreenX.Chest != "sports bra":
                        ch_p "Мне нравится твой спортивный лифчик."
                        if DoreenX.SeenChest or ApprovalCheck(DoreenX, 1100, TabM=2):
                            ch_d "Да?"
                            $ DoreenX.Chest = "sports bra"
                        else:
                            call Display_DressScreen(DoreenX)
                            if not _return:
                                ch_d "Она довольно маленькая. . ."
                            else:
                                $ DoreenX.Chest = "sports bra"

                "Примерь лифчик бикини" if DoreenX.Chest != "bikini top" and "bikini top" in DoreenX.Inventory:
                        ch_p "Мне нравится твой лифчик бикини."
                        if bg_current == "bg pool":
                                ch_d "Хорошо."
                                $ DoreenX.Chest = "bikini top"
                        else:
                                if DoreenX.SeenChest or ApprovalCheck(DoreenX, 1000, TabM=2):
                                    ch_d "Хорошо."
                                    $ DoreenX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(DoreenX)
                                    if not _return:
                                            ch_d "Это место не совсем подходит для пляжной одежды. . ."
                                    else:
                                            $ DoreenX.Chest = "bikini top"
                "Неважно":
                        pass
            return #jump Doreen_Clothes_Under

        "Варианты колготок и чулок":
            menu:
                "Сними [get_clothing_name(DoreenX.Hose_key, vin)]." if DoreenX.Hose:
                                $ DoreenX.FaceChange("sexy", 1)
                                if DoreenX.SeenPanties and DoreenX.Panties and ApprovalCheck(DoreenX, 500, TabM=5):
                                    ch_d "Конечно."
                                elif DoreenX.SeenPussy and ApprovalCheck(DoreenX, 900, TabM=4):
                                    ch_d "Конечно."
                                elif ApprovalCheck(DoreenX, 1300, TabM=2) and DoreenX.Panties:
                                    ch_d "Ладно, ради тебя. . ."
                                elif ApprovalCheck(DoreenX, 700) and not DoreenX.Panties:
                                    call Doreen_NoPantiesOn
                                    if not _return and not DoreenX.Panties:
                                        if not ApprovalCheck(DoreenX, 1500):
                                            call Display_DressScreen(DoreenX)
                                            if not _return:
                                                return #jump Doreen_Clothes
                                        else:
                                                return #jump Doreen_Clothes
                                else:
                                    call Display_DressScreen(DoreenX)
                                    if not _return:
                                        ch_d "Я не хочу делать это, когда ты рядом."
                                        if not DoreenX.Panties:
                                                ch_d "На мне, эм. . . нет трусиков. . ."
                                        return #jump Doreen_Clothes
                                $ DoreenX.Hose = 0

                "Чулки дополнили бы твой образ." if DoreenX.Hose != "stockings":
                                $ DoreenX.Hose = "stockings"
                "Колготки дополнили бы твой образ." if DoreenX.Hose != "pantyhose" and "pantyhose" in DoreenX.Inventory:
                                $ DoreenX.Hose = "pantyhose"
                "Рваные колготки дополнили бы твой образ." if DoreenX.Hose != "ripped pantyhose" and "ripped pantyhose" in DoreenX.Inventory:
                                $ DoreenX.Hose = "ripped pantyhose"
                "Серые леггинсы дополнили бы твой образ." if DoreenX.Hose != "tights":
                                $ DoreenX.Hose = "tights"
#                "The ripped tights would look good with that." if DoreenX.Hose != "ripped tights" and "ripped tights" in DoreenX.Inventory:
#                                $ DoreenX.Hose = "ripped tights"
                "Чулки и пояс с подвязками дополнили бы твой образ." if DoreenX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in DoreenX.Inventory:
                                $ DoreenX.Hose = "stockings and garterbelt"
                "Может, наденешь только пояс с подвязками?" if DoreenX.Hose != "garterbelt" and "stockings and garterbelt" in DoreenX.Inventory:
                                $ DoreenX.Hose = "garterbelt"
#                "The blue socks would look good with that." if DoreenX.Hose != "socks":
#                                $ DoreenX.Hose = "socks"
                "Неважно":
                        pass
            return #jump Doreen_Clothes_Under

        #Panties
        "Низ":
            menu:
                "Ты должна снять [get_clothing_name(DoreenX.Panties_key, vin)]. . ." if DoreenX.Panties:
                        $ DoreenX.FaceChange("bemused", 1)
                        if ApprovalCheck(DoreenX, 900) and (DoreenX.Legs or (DoreenX.SeenPussy and not DoreenX.Taboo)):
                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                                if ApprovalCheck(DoreenX, 850, "L"):
                                        ch_d "Конечно. . ."
                                elif ApprovalCheck(DoreenX, 500, "O"):
                                        ch_d "Ладно."
                                elif ApprovalCheck(DoreenX, 350, "I"):
                                        ch_d "Ох."
                                else:
                                        ch_d "Пожалуй. . ."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(DoreenX, 1100, "LI", TabM=3) and DoreenX.Love > DoreenX.Inbt:
                                        ch_d "Я не могу сделать это на людях. . ."
                                elif ApprovalCheck(DoreenX, 700, "OI", TabM=3) and DoreenX.Obed > DoreenX.Inbt:
                                        ch_d "Хорошо. . ."
                                elif ApprovalCheck(DoreenX, 600, "I", TabM=3):
                                        ch_d "Хммм. . ."
                                elif ApprovalCheck(DoreenX, 1300, TabM=3):
                                        ch_d "Хм. . ."
                                else:
                                        call Display_DressScreen(DoreenX)
                                        if not _return:
                                            $ DoreenX.FaceChange("surprised")
                                            $ DoreenX.Brows = "angry"
                                            if DoreenX.Taboo > 20:
                                                ch_d "Здесь слишком людно."
                                            else:
                                                if not Player.Male:
                                                    ch_d "Ты не настолько милая, [DoreenX.Petname]!"
                                                else:
                                                    ch_d "Ты не настолько милый, [DoreenX.Petname]!"
                                            return #jump Doreen_Clothes
                        $ Line = get_clothing_name(DoreenX.Panties_key, vin)
                        $ DoreenX.Panties = 0
                        if not DoreenX.Legs:
                            "Она снимает [Line] и бросает их на пол."
                            if not renpy.showing('DressScreen'):
                                    call Girl_First_Bottomless(DoreenX)
                        elif ApprovalCheck(DoreenX, 1200, TabM=4):
                            $ Trigger = DoreenX.Legs
                            $ DoreenX.Legs = 0
                            pause 0.5
                            $ DoreenX.Legs = Trigger
                            "Она снимает [get_clothing_name(DoreenX.Legs_key, vin)] и [Line], а затем снова надевает [get_clothing_name(DoreenX.Legs_key, vin)]."
                            $ Trigger = 1
                            call Girl_First_Bottomless(DoreenX,1)
                        elif DoreenX.Legs == "skirt":
                            "Она залезает под юбку и стягивает [Line]."
                        else:
                            $ DoreenX.Blush = 1
                            "Она на мгновение отходит, а затем возвращается."
                            $ DoreenX.Blush = 0
                        $ Line = 0

                "Почему бы тебе вместо этих не надеть коричневые трусики?" if DoreenX.Panties and DoreenX.Panties != "tan panties":
                        if ApprovalCheck(DoreenX, 1100, TabM=3):
                                ch_d "Ох, конечно."
                                $ DoreenX.Panties = "tan panties"
                        else:
                                call Display_DressScreen(DoreenX)
                                if not _return:
                                        ch_d "Тебе не стоит беспокоиться о моем нижнем белье."
                                else:
                                        $ DoreenX.Panties = "tan panties"

                "Почему бы тебе вместо этих не надеть кружевные трусики?" if "lace panties" in DoreenX.Inventory and DoreenX.Panties and DoreenX.Panties != "lace panties":
                        if ApprovalCheck(DoreenX, 1300, TabM=3):
                                ch_d "Ох, конечно."
                                $ DoreenX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(DoreenX)
                                if not _return:
                                        ch_d "Тебе не стоит беспокоиться о моем нижнем белье."
                                else:
                                        $ DoreenX.Panties = "lace panties"

                "Примерь трусики бикини" if DoreenX.Panties != "bikini bottoms" and "bikini bottoms" in DoreenX.Inventory:
                        ch_p "Мне нравятся твои трусики бикини."
                        if bg_current == "bg pool":
                                ch_d "Хорошо."
                                $ DoreenX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(DoreenX, 800, TabM=2):
                                    ch_d "Хорошо."
                                    $ DoreenX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(DoreenX)
                                    if not _return:
                                            ch_d "Это место не совсем подходит для пляжной одежды. . ."
                                    else:
                                            $ DoreenX.Panties = "bikini bottoms"

                "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not DoreenX.Panties:
                        $ DoreenX.FaceChange("bemused", 1)
                        if DoreenX.Legs and (DoreenX.Love+DoreenX.Obed) <= (2 * DoreenX.Inbt):
                            $ DoreenX.Mouth = "smile"
                            ch_d "Но я не хочу. . ."
                            menu:
                                "Ну ладно.":
                                    return #jump Doreen_Clothes
                                "Я настаиваю, надевай.":
                                    if (DoreenX.Love+DoreenX.Obed) <= (1.5 * DoreenX.Inbt):
                                        $ DoreenX.FaceChange("angry", Eyes="side")
                                        ch_d "Нет, я против."
                                        return #jump Doreen_Clothes
                                    else:
                                        $ DoreenX.FaceChange("sadside")
                                        ch_d "Ох, ладно. . ."
                        else:
                            ch_d "Пожалуй. . ."
                        menu:
                            extend ""
                            "Как насчет коричневых?":
                                    ch_d "Ох, конечно."
                                    $ DoreenX.Panties = "tan panties"
                            "Как насчет трусиков бикини?" if "bikini bottoms" in DoreenX.Inventory:
                                    ch_d "Ох, конечно."
                                    $ DoreenX.Panties  = "bikini bottoms"
                            "Как насчет кружевных?" if "lace panties" in DoreenX.Inventory:
                                    ch_d "Ох, конечно."
                                    $ DoreenX.Panties  = "lace panties"
                "Неважно":
                    pass
            return #jump Doreen_Clothes_Under
        "Неважно":
            pass
    return #jump Doreen_Clothes
    #End of Doreen Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Doreen_Clothes_Misc:
        #Misc
        "Сухие волосы" if DoreenX.Hair == "wet" or DoreenX.Hair == "wetlong":
                ch_p "Тебе идут сухие волосы."
                if ApprovalCheck(DoreenX, 600):
                    ch_d "Ох, правда?"
                    if DoreenX.Hair == "wet":
                        $ DoreenX.Hair = "short"
                    else:
                        $ DoreenX.Hair = "long"
                else:
                    ch_d "Я даже не знаю, мне нравится моя текущая прическа."

        "Короткие волосы" if DoreenX.Hair == "long":
                ch_p "Мне кажется, тебе идет короткая стрижка."
                if ApprovalCheck(DoreenX, 600):
                    ch_d "Ох, ладно?"
                    show blackscreen onlayer black
                    "Она на минутку удаляется."
                    $ DoreenX.Hair = "short"
                    hide blackscreen onlayer black
                else:
                    ch_d "Мне больше нравится моя текущая прическа."
        "Длинные волосы" if DoreenX.Hair == "short":
                ch_p "Мне кажется, тебе идут длинные волосы."
                if ApprovalCheck(DoreenX, 600):
                    ch_d "Ох, ладно?"
                    show blackscreen onlayer black
                    "Она на минутку удаляется."
                    $ DoreenX.Hair = "long"
                    hide blackscreen onlayer black
                else:
                    ch_d "Мне нравится моя текущая прическа."

        "Влажные волосы" if DoreenX.Hair != "wet" and DoreenX.Hair != "wetlong":
                ch_p "Тебе стоит увлажнить волосы."
                if ApprovalCheck(DoreenX, 800):
                    ch_d "Ох, ладно?"
                    if DoreenX.Hair == "short":
                        $ DoreenX.Hair = "wet"
                    else:
                        $ DoreenX.Hair = "wetlong"
                    show blackscreen onlayer black
                    "Она отходит на минуту и вскоре возвращается."
                    hide blackscreen onlayer black
                    ch_d "Так?"
                else:
                    ch_d "Ох, это слишком хлопотно."

        "Отрасти волосы на лобке" if not DoreenX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может, отрастишь?"
                call expression DoreenX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in DoreenX.Todo:
                        $ DoreenX.FaceChange("bemused", 1)
                        ch_d "Да-да, я поняла."
                else:
                    $ DoreenX.FaceChange("bemused", 1)
                    if ApprovalCheck(DoreenX, 1000, TabM=0):
                            ch_d "Ладно, наверное, это можно устроить. . ."
                    else:
                            $ DoreenX.FaceChange("surprised")
                            $ DoreenX.Brows = "angry"
                            ch_d ". . . почему тебя интересует растительность на моем лобке?"
                            return #jump Doreen_Clothes
                    $ DoreenX.Todo.append("pubes")
                    $ DoreenX.PubeC = 6
        "Побрей лобок" if DoreenX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression DoreenX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ DoreenX.FaceChange("bemused", 1)
                if "shave" in DoreenX.Todo:
                        ch_d "Попозже я этим займусь."
                else:
                    if ApprovalCheck(DoreenX, 1100, TabM=0):
                            ch_d "Ох, так тебе не нравятся. . . заросли? . ."
                    else:
                            $ DoreenX.FaceChange("surprised")
                            $ DoreenX.Brows = "angry"
                            ch_d ". . . почему тебя интересует растительность на моем лобке?"
                            return #jump Doreen_Clothes
                    $ DoreenX.Todo.append("shave")

        "Пирсинг. [[Сначала посмотрите, как она выглядит без него] (locked)" if not DoreenX.SeenPussy and not DoreenX.SeenChest:
            pass

        "Надень пирсинг-кольца" if DoreenX.Pierce != "ring" and (DoreenX.SeenPussy or DoreenX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсингом-кольцами."
                if "ring" in DoreenX.Todo:
                    ch_d "Ага, я поняла."
                else:
                    $ DoreenX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(DoreenX, 1150, TabM=0)
                    if ApprovalCheck(DoreenX, 900, "L", TabM=0) or (Approval and DoreenX.Love > 2* DoreenX.Obed):
                        ch_d "Думаешь, он будет хорошо смотреться на мне?"
                    elif ApprovalCheck(DoreenX, 600, "I", TabM=0) or (Approval and DoreenX.Inbt > DoreenX.Obed):
                        ch_d "Я уже думала о нем. . ."
                    elif ApprovalCheck(DoreenX, 500, "O", TabM=0) or Approval:
                        ch_d "Если ты этого хочешь, [DoreenX.Petname]."
                    else:
                        $ DoreenX.FaceChange("surprised")
                        $ DoreenX.Brows = "angry"
                        ch_d "Мне не интересно, [DoreenX.Petname]."
                        return #jump Doreen_Clothes
                    $ DoreenX.Todo.append("ring")

        "Надень пирсинг-штанги" if DoreenX.Pierce != "barbell" and (DoreenX.SeenPussy or DoreenX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in DoreenX.Todo:
                    ch_d "Ага, я поняла."
                else:
                    $ DoreenX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(DoreenX, 1150, TabM=0)
                    if ApprovalCheck(DoreenX, 900, "L", TabM=0) or (Approval and DoreenX.Love > 2 * DoreenX.Obed):
                        ch_d "Думаешь, он будет хорошо смотреться на мне?"
                    elif ApprovalCheck(DoreenX, 600, "I", TabM=0) or (Approval and DoreenX.Inbt > DoreenX.Obed):
                        ch_d "Я уже думала о нем. . ."
                    elif ApprovalCheck(DoreenX, 500, "O", TabM=0) or Approval:
                        ch_d "Если ты этого хочешь, [DoreenX.Petname]."
                    else:
                        $ DoreenX.FaceChange("surprised")
                        $ DoreenX.Brows = "angry"
                        ch_d "Мне не интересно, [DoreenX.Petname]."
                        return #jump Doreen_Clothes
                    $ DoreenX.Todo.append("barbell")

        "Сними пирсинг" if DoreenX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ DoreenX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(DoreenX, 1350, TabM=0)
                if ApprovalCheck(DoreenX, 950, "L", TabM=0) or (Approval and DoreenX.Love > DoreenX.Obed):
                    ch_d "Ох, хорошо . ."
                elif ApprovalCheck(DoreenX, 700, "I", TabM=0) or (Approval and DoreenX.Inbt > DoreenX.Obed):
                    ch_d "Ну, а мне он нравится."
                    return
                elif ApprovalCheck(DoreenX, 600, "O", TabM=0) or Approval:
                    ch_d "Ладно. . ."
                else:
                    $ DoreenX.FaceChange("surprised")
                    $ DoreenX.Brows = "angry"
                    ch_d "Ну, а мне он нравится. . ."
                    return #jump Doreen_Clothes
                $ DoreenX.Pierce = 0

        "Надень ободок с ушками" if DoreenX.Hat != "headband":
                ch_p "Почему бы тебе не надеть ободок с ушками?"
                ch_d "Ох, ладно. . ."
                $ DoreenX.Hat = "headband"
        "Надень очки" if DoreenX.Hat != "glasses" and "halloween" in DoreenX.History:
                ch_p "Почему бы тебе не надеть очки?"
                ch_d "Ох, ладно. . ."
                $ DoreenX.Hat = "glasses"
        "Сними [get_clothing_name(DoreenX.Hat_key, vin)]" if DoreenX.Hat:
                ch_p "Думаю, тебе лучше снять [get_clothing_name(DoreenX.Hat_key, vin)]."
                ch_d "Ладно. . ."
                $ DoreenX.Hat = 0

        "Хвост вкл\выкл" if "tail" in DoreenX.History:
                if DoreenX.Tail:
                            ch_p "Мне кажется, тебе лучше без хвоста."
                else:
                            ch_p "Мне кажется, тебе лучше с хвостом."
                ch_d "Ладно. . ."
                show blackscreen onlayer black
                "Она на мгновение выходит из комнаты."
                $ DoreenX.Tail = 0 if DoreenX.Tail else 1
                hide blackscreen onlayer black

#        "Medallion choker" if DoreenX.Neck != "leash choker":
#                ch_p "Why don't you try on that medallion choker?"
#                ch_d "Ok. . ."
#                $ DoreenX.Neck = "leash choker"
#        "Remove Necklace" if DoreenX.Neck:
#                ch_p "Maybe go without a necklace."
#                ch_d "Ok. . ."
#                $ DoreenX.Neck = 0


#        "Toggle Gloves":
#                if not DoreenX.Arms:
#                        ch_p "Why don't you put those gloves back on."
#                else:
#                        ch_p "Maybe go without the gloves."
#                ch_d "Fine."
#                $ DoreenX.Arms = 0 if DoreenX.Arms else "gloves"

        "Неважно":
            pass
    return #jump Doreen_Clothes
    #End of Doreen Misc Wardrobe

return
#End Doreen Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
