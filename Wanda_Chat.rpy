# star Wanda chat interface
#Wanda Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Wanda_Relationship: #rkeljsvgbdw
    while True:
        menu:
            ch_w "Итак, о чем ты хочешь поговорить?"
            "Хочешь стать моей девушкой?" if WandaX not in Player.Harem and "ex" not in WandaX.Traits:
                    $ WandaX.DailyActions.append("relationship")
                    if "asked boyfriend" in WandaX.DailyActions and "angry" in WandaX.DailyActions:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Перестань спрашивать."
                            return
                    elif "asked boyfriend" in WandaX.DailyActions:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Все еще нет."
                            return
                    elif WandaX.Break[0]:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Нет, если ты все еще хочешь встречаться с другими девушками."
                            if Player.Harem:
                                    $ WandaX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "Я уже ни с кем не встречаюсь."

                    $ WandaX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "WandaYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_w "А остальные не против, [WandaX.Petname]?"
                        else:
                            ch_w "А [Player.Harem[0].Name] не против, [WandaX.Petname]?"
                        return

                    if WandaX.Event[5]:
                            $ WandaX.FaceChange("bemused", 1)
                            ch_w "Я думала, тебе это неинтересно."
                    else:
                            $ WandaX.FaceChange("surprised", 2)
                            ch_w "Что? . ."
                            $ WandaX.FaceChange("smile", 1)

                    call Wanda_OtherWoman

                    if WandaX.Love >= 800:
                            $ WandaX.FaceChange("surprised", 1)
                            $ WandaX.Mouth = "smile"
                            if not WandaX.Event[5]:
                                    $ WandaX.Statup("Love", 200, 10)
                                    call Wanda_BF
                                    return
                            $ WandaX.Statup("Love", 200, 40)
                            ch_w "Конечно."
                            if "boyfriend" not in WandaX.Petnames:
                                    $ WandaX.Petnames.append("boyfriend")
                            if "WandaYes" in Player.Traits:
                                    $ Player.Traits.remove("WandaYes")
                            $ Player.Harem.append(WandaX)
                            call Harem_Initiation
                            "[WandaX.Name] бросается к вам и страстно целует."
                            $ WandaX.FaceChange("kiss", 1)
                            $ WandaX.Kissed += 1
                    elif WandaX.Obed >= 500:
                            $ WandaX.FaceChange("perplexed")
                            ch_w "Я не уверена, думаю, мы уже нашли вариант получше. . ."
                    elif WandaX.Inbt >= 500:
                            $ WandaX.FaceChange("smile")
                            ch_w "Мне нравится свобода."
                    else:
                            $ WandaX.FaceChange("perplexed", 1)
                            ch_w "Мне больше это не интересно, [WandaX.Petname]."

            "Может, начнем все сначала?" if "ex" in WandaX.Traits:
                    $ WandaX.DailyActions.append("relationship")
                    if "asked boyfriend" in WandaX.DailyActions and "angry" in WandaX.DailyActions:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Перестань спрашивать."
                            return
                    elif "asked boyfriend" in WandaX.DailyActions:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Прости, но нет."
                            return

                    $ WandaX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "WandaYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_w "А остальные не против, [WandaX.Petname]?"
                            else:
                                ch_w "А [Player.Harem[0].Name] не против, [WandaX.Petname]?"
                            return

                    $ Cnt = 0
                    call Wanda_OtherWoman

                    if WandaX.Love >= 800:
                            $ WandaX.FaceChange("surprised", 1)
                            $ WandaX.Mouth = "smile"
                            $ WandaX.Statup("Love", 90, 5)
                            ch_w "Думаю, я могу дать тебе еще один шанс."
                            if "boyfriend" not in WandaX.Petnames:
                                        $ WandaX.Petnames.append("boyfriend")
                            $ WandaX.Traits.remove("ex")
                            if "WandaYes" in Player.Traits:
                                    $ Player.Traits.remove("WandaYes")
                            $ Player.Harem.append(WandaX)
                            call Harem_Initiation
                            "[WandaX.Name] притягивает вас к себе и страстно целует."
                            $ WandaX.FaceChange("kiss", 1)
                            $ WandaX.Kissed += 1
                    elif WandaX.Love >= 600 and ApprovalCheck(WandaX, 1500):
                            $ WandaX.FaceChange("smile", 1)
                            $ WandaX.Statup("Love", 90, 5)
                            ch_w ". . . конечно."
                            if "boyfriend" not in WandaX.Petnames:
                                    $ WandaX.Petnames.append("boyfriend")
                            $ WandaX.Traits.remove("ex")
                            if "WandaYes" in Player.Traits:
                                    $ Player.Traits.remove("WandaYes")
                            $ Player.Harem.append(WandaX)
                            call Harem_Initiation
                            $ WandaX.FaceChange("kiss", 1)
                            "[WandaX.Name] дарит вам легкий поцелуй."
                            $ WandaX.FaceChange("sly", 1)
                            $ WandaX.Kissed += 1
                    elif WandaX.Obed >= 500:
                            $ WandaX.FaceChange("sad")
                            ch_w "Не думаю, что у нас что-то получится. . ."
                    elif WandaX.Inbt >= 500:
                            $ WandaX.FaceChange("perplexed")
                            ch_w "Теперь это в прошлом."
                    else:
                            $ WandaX.FaceChange("sadside", 1)
                            ch_w "Я не уверена, что смогла бы пройти через это снова. . ."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if WandaX in Player.Harem:
                            call AskDateOther

            "Думаю, мы должны расстаться." if WandaX in Player.Harem:
                            if "breakup talk" in WandaX.RecentActions:
                                    ch_w "Прошу, перестань говорить об этом."
                            elif "breakup talk" in WandaX.DailyActions:
                                    ch_w "Снова?"
                                    ch_w "Перестань, [WandaX.Petname]."
                            else:
                                    call Breakup(WandaX)

            "О разговоре, который у нас был ранее. . .":
                menu:
                    "Помнишь, ты признавалась мне в любви. . ?" if "lover" not in WandaX.Traits and WandaX.Event[6] >= 20 and WandaX.Event[6] != 23:
                            call Wanda_Love_Redux

                    "Помнишь, ты рассказывала мне о себе. . ?" if "lover" not in WandaX.Traits and WandaX.Event[6] == 23:
                            call Wanda_Love_Redux

                    "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировала?" if "sir" not in WandaX.Petnames and "sir" in WandaX.History and not Player.Male:
                            if "asked sub" in WandaX.RecentActions:
                                    ch_w "Прошу, перестань спрашивать об этом."
                            elif "asked sub" in WandaX.DailyActions:
                                    ch_w "Перестань, [WandaX.Petname]."
                            else:
                                    call Wanda_Sub_Asked

                    "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировал?" if "sir" not in WandaX.Petnames and "sir" in WandaX.History and Player.Male:
                            if "asked sub" in WandaX.RecentActions:
                                    ch_w "Прошу, перестань спрашивать об этом."
                            elif "asked sub" in WandaX.DailyActions:
                                    ch_w "Перестань, [WandaX.Petname]."
                            else:
                                    call Wanda_Sub_Asked

                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоей хозяйкой?" if "master" not in WandaX.Petnames and "master" in WandaX.History and not Player.Male:
                            if "asked sub" in WandaX.RecentActions:
                                    ch_w "Прошу, перестань спрашивать об этом."
                            elif "asked sub" in WandaX.DailyActions:
                                    ch_w "Перестань, [WandaX.Petname]."
                            else:
                                    call Wanda_Sub_Asked

                    "Помнишь, ты говорила, что хочешь, чтобы я стал твоим хозяином?" if "master" not in WandaX.Petnames and "master" in WandaX.History and Player.Male:
                            if "asked sub" in WandaX.RecentActions:
                                    ch_w "Прошу, перестань спрашивать об этом."
                            elif "asked sub" in WandaX.DailyActions:
                                    ch_w "Перестань, [WandaX.Petname]."
                            else:
                                    call Wanda_Sub_Asked
                    "Неважно":
                            pass

            "Неважно":
                return

    return

label Wanda_OtherWoman(Cnt = 0): #rkeljsvgbdw
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((WandaX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ WandaX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_w "Я заметила, что ты теперь с [Player.Harem[0].Name_tvo] и другими, это правда так?"
    else:
        ch_w "Я заметила, что ты теперь с [Player.Harem[0].Name_tvo], это правда так?"
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "WandaYes" in Player.Traits:
                if ApprovalCheck(WandaX, 1800, Bonus = Cnt):
                        $ WandaX.FaceChange("smile", 1)
                        if WandaX.Love >= WandaX.Obed:
                                ch_w "Думаю, тогда мы можем попробовать."
                        elif WandaX.Obed >= WandaX.Inbt:
                                ch_w "Думаю, тогда мы можем попробовать."
                        else:
                                ch_w "Думаю, тогда мы можем попробовать."
                else:
                        $ WandaX.FaceChange("sad", 1)
                        ch_w "Даже если так, я не могу."
                        $ renpy.pop_call()
                        #This causes it to jump past the previous menu on the return

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "WandaYes" not in Player.Traits and not Player.Male:
                if ApprovalCheck(WandaX, 1800, Bonus = Cnt):
                        $ WandaX.FaceChange("smile", 1)
#                        if WandaX.Love >= WandaX.Obed:
#                            ch_w "Then I may consider it. . ."
#                        elif WandaX.Obed >= WandaX.Inbt:
#                            ch_w "Then I may consider it. . ."
#                        else:
#                            ch_w "Then sure, why not."
                        ch_w "Что ж. . ."
                        ch_w "Приходи ко мне, когда поговоришь с ней."
                else:
                        $ WandaX.FaceChange("sad", 1)
                        ch_w "Ну. . . даже если она будет не против, я не могу."
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "WandaYes" not in Player.Traits and Player.Male:
                if ApprovalCheck(WandaX, 1800, Bonus = Cnt):
                        $ WandaX.FaceChange("smile", 1)
#                        if WandaX.Love >= WandaX.Obed:
#                            ch_w "Then I may consider it. . ."
#                        elif WandaX.Obed >= WandaX.Inbt:
#                            ch_w "Then I may consider it. . ."
#                        else:
#                            ch_w "Then sure, why not."
                        ch_w "Что ж. . ."
                        ch_w "Приходи ко мне, когда поговоришь с ней."
                else:
                        $ WandaX.FaceChange("sad", 1)
                        ch_w "Ну. . . даже если она будет не против, я не могу."
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
                if ApprovalCheck(WandaX, 1800, Bonus = -Cnt): #checks if Wanda likes you more than the other girl
                        $ WandaX.FaceChange("smile", 1)
                        if WandaX.Love >= WandaX.Obed:
                                ch_w "Пожалуй. . ."
                        elif WandaX.Obed >= WandaX.Inbt:
                                ch_w "Ну, тогда, думаю, можно. . ."
                        else:
                                ch_w "О, клево. . ."
                        $ WandaX.Traits.append("downlow")
                else:
                        $ WandaX.FaceChange("angry", 1)
                        if ApprovalCheck(WandaX, 1800):
                                ch_w "Да ладно, это лучшее, что ты можешь предложить?"
                        else:
                                ch_w "Прозвучало просто ужасно!"
                        $ renpy.pop_call()

        "Я могу порвать с ней.":
                    $ WandaX.FaceChange("sad")
                    ch_w "Потом расскажи мне, как все прошло."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ WandaX.FaceChange("sad")
                    ch_w "Думаешь?"
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ WandaX.FaceChange("sad")
                    ch_w "Думаешь?"
                    $ renpy.pop_call()

    return


label Wanda_About(Check=0): #rkeljsvgbdw
    if Check not in TotalGirls:
            ch_w "Кто это?"
            return
    ch_w "Что я думаю о ней? Да?"
    if Check == RogueX:
            if "poly Rogue" in WandaX.Traits:
                if not Player.Male:
                    ch_w "Ну, ты и сама прекрасно знаешь. . ."
                else:
                    ch_w "Ну, ты и сам прекрасно знаешь. . ."
            elif WandaX.LikeRogue >= 900:
                ch_w "С ней очень приятно проводить время."
            elif WandaX.LikeRogue >= 800:
                ch_w "Она очень сексуальная."
            elif WandaX.LikeRogue >= 700:
                ch_w "Она довольно сексуальная, правда?"
            elif WandaX.LikeRogue >= 600:
                ch_w "Она довольно клевая."
            elif WandaX.LikeRogue >= 500:
                ch_w "Я не уверена, но, думаю, мы с ней поладим."
            elif WandaX.LikeRogue >= 400:
                ch_w "У нас с ней были не очень приятные моменты. . ."
            elif WandaX.LikeRogue >= 300:
                ch_w "Я ненавижу эту суку."
            else:
                ch_w "Она шлюха."
    elif Check == KittyX:
            if "poly Kitty" in WandaX.Traits:
                if not Player.Male:
                    ch_w "Ну, ты и сама прекрасно знаешь. . ."
                else:
                    ch_w "Ну, ты и сам прекрасно знаешь. . ."
            elif WandaX.LikeKitty >= 900:
                ch_w "Она хороша в постели. . ."
            elif WandaX.LikeKitty >= 800:
                ch_w "Она такая сексуальная."
            elif WandaX.LikeKitty >= 700:
                ch_w "Она довольно очаровательна, правда?"
            elif WandaX.LikeKitty >= 600:
                ch_w "Она довольно клевая."
            elif WandaX.LikeKitty >= 500:
                ch_w "Я не уверена, но, думаю, мы с ней поладим."
            elif WandaX.LikeKitty >= 400:
                ch_w "У нас с ней были не очень приятные моменты. . ."
            else:
                ch_w "Она шлюха."
    elif Check == LauraX:
            if "poly Laura" in WandaX.Traits:
                if not Player.Male:
                    ch_w "Ну, ты и сама прекрасно знаешь. . ."
                else:
                    ch_w "Ну, ты и сам прекрасно знаешь. . ."
            elif WandaX.LikeLaura >= 900:
                ch_w "Она подобна зверю. В хорошем смысле."
            elif WandaX.LikeLaura >= 800:
                ch_w "Она такая сексуальная."
            elif WandaX.LikeLaura >= 700:
                ch_w "Она довольно сексуальная, правда?"
            elif WandaX.LikeLaura >= 600:
                ch_w "У нее клевые волосы."
            elif WandaX.LikeLaura >= 500:
                ch_w "Мы с ней особо не общались."
            elif WandaX.LikeLaura >= 400:
                ch_w "У нас с ней были не очень приятные моменты. . ."
            elif WandaX.LikeLaura >= 300:
                ch_w "Я ненавижу эту суку."
            else:
                ch_w "Она шлюха."
    elif Check == EmmaX:
            if "poly Emma" in WandaX.Traits:
                if not Player.Male:
                    ch_w "Ну, ты и сама прекрасно знаешь. . ."
                else:
                    ch_w "Ну, ты и сам прекрасно знаешь. . ."
            elif WandaX.LikeEmma >= 900:
                ch_w "Она -такая- красивая."
            elif WandaX.LikeEmma >= 800:
                ch_w "У нее отличное тело. . ."
            elif WandaX.LikeEmma >= 700:
                ch_w "Из нее вышел клевый препод."
            elif WandaX.LikeEmma >= 600:
                ch_w "Она очень помогла мне обжиться здесь."
            elif WandaX.LikeEmma >= 500:
                ch_w "Думаю, она нормальный препод."
            elif WandaX.LikeEmma >= 400:
                ch_w "У нас с ней были не очень приятные моменты. . ."
            elif WandaX.LikeEmma >= 300:
                ch_w "Я ненавижу эту суку."
            else:
                ch_w "Она шлюха."
    elif Check == JeanX:
            if "poly Jean" in WandaX.Traits:
                if not Player.Male:
                    ch_w "Ну, ты и сама прекрасно знаешь. . ."
                else:
                    ch_w "Ну, ты и сам прекрасно знаешь. . ."
            elif WandaX.LikeJean >= 900:
                ch_w "Я готова сотворить с ее телом много ужасного. . ."
            elif WandaX.LikeJean >= 800:
                ch_w "Я бы очень хотела, чтобы она не была такой стервой. . ."
            elif WandaX.LikeJean >= 700:
                ch_w "Она не так плоха."
            elif WandaX.LikeJean >= 600:
                ch_w "Она довольно клевая. . . иногда."
            elif WandaX.LikeJean >= 500:
                ch_w "Я не уверена, но, думаю, мы с ней поладим."
            elif WandaX.LikeJean >= 400:
                ch_w "У нас с ней были не очень приятные моменты. . ."
            elif WandaX.LikeJean >= 300:
                ch_w "Я ненавижу эту суку."
            else:
                ch_w "Она шлюха."
    elif Check == StormX:
            if "poly Storm" in WandaX.Traits:
                if not Player.Male:
                    ch_w "Ну, ты и сама прекрасно знаешь. . ."
                else:
                    ch_w "Ну, ты и сам прекрасно знаешь. . ."
            elif WandaX.LikeStorm >= 900:
                ch_w "Я готова утонуть в ее сиськах. . ."
            elif WandaX.LikeStorm >= 800:
                ch_w "Она очень красивая. . ."
            elif WandaX.LikeStorm >= 700:
                ch_w "Из нее вышел клевый препод."
            elif WandaX.LikeStorm >= 600:
                ch_w "Она очень помогла мне обжиться здесь."
            elif WandaX.LikeStorm >= 500:
                ch_w "Думаю, она нормальный препод."
            elif WandaX.LikeStorm >= 400:
                ch_w "У нас с ней были не очень приятные моменты. . ."
            elif WandaX.LikeStorm >= 300:
                ch_w "Я ненавижу эту суку."
            else:
                ch_w "Она шлюха."
    elif Check == JubesX:
            if "poly Jubes" in WandaX.Traits:
                if not Player.Male:
                    ch_w "Ну, ты и сама прекрасно знаешь. . ."
                else:
                    ch_w "Ну, ты и сам прекрасно знаешь. . ."
            elif WandaX.LikeJubes >= 900:
                ch_w "У нее великолепное тело."
            elif WandaX.LikeJubes >= 800:
                ch_w "Она очень милая, правда?"
            elif WandaX.LikeJubes >= 700:
                ch_w "С ней весело проводить время."
            elif WandaX.LikeJubes >= 600:
                ch_w "Она довольно клевая."
            elif WandaX.LikeJubes >= 500:
                ch_w "Я не уверена, но, думаю, мы с ней поладим."
            elif WandaX.LikeJubes >= 400:
                ch_w "У нас с ней были не очень приятные моменты. . ."
            elif WandaX.LikeJubes >= 300:
                ch_w "Я ненавижу эту суку."
            else:
                ch_w "Она шлюха."
    elif Check == GwenX:
            if "poly Gwen" in WandaX.Traits:
                if not Player.Male:
                    ch_w "Ну, ты и сама прекрасно знаешь. . ."
                else:
                    ch_w "Ну, ты и сам прекрасно знаешь. . ."
            elif WandaX.LikeGwen >= 900:
                ch_w "Она -очень- энергичная."
            elif WandaX.LikeGwen >= 800:
                ch_w "Она очень милая, не так ли?"
            elif WandaX.LikeGwen >= 700:
                ch_w "Она очень позитивная. . ."
            elif WandaX.LikeGwen >= 600:
                ch_w "Она довольно клевая."
            elif WandaX.LikeGwen >= 500:
                ch_w "Я не уверена, но, думаю, мы с ней поладим."
            elif WandaX.LikeGwen >= 400:
                ch_w "У нас с ней были не очень приятные моменты. . ."
            elif WandaX.LikeGwen >= 300:
                ch_w "Я ненавижу эту суку."
            else:
                ch_w "Она шлюха."
    elif Check == BetsyX:
            if "poly Betsy" in WandaX.Traits:
                if not Player.Male:
                    ch_w "Ну, ты и сама прекрасно знаешь. . ."
                else:
                    ch_w "Ну, ты и сам прекрасно знаешь. . ."
            elif WandaX.LikeBetsy >= 900:
                ch_w "Она невероятно сексуальная. . ."
            elif WandaX.LikeBetsy >= 800:
                ch_w "Она такая. . . изящная."
            elif WandaX.LikeBetsy >= 700:
                ch_w "Она очень стильная."
            elif WandaX.LikeBetsy >= 600:
                ch_w "Она довольно клевая."
            elif WandaX.LikeBetsy >= 500:
                ch_w "Я не уверена, но, думаю, мы с ней поладим."
            elif WandaX.LikeBetsy >= 400:
                ch_w "У нас с ней были не очень приятные моменты. . ."
            elif WandaX.LikeBetsy >= 300:
                ch_w "Я ненавижу эту суку."
            else:
                ch_w "Она шлюха."
    elif Check == DoreenX:
            if "poly Doreen" in WandaX.Traits:
                if not Player.Male:
                    ch_w "Ну, ты и сама прекрасно знаешь. . ."
                else:
                    ch_w "Ну, ты и сам прекрасно знаешь. . ."
            elif WandaX.LikeDoreen >= 900:
                ch_w "У нее потрясающая задница."
            elif WandaX.LikeDoreen >= 800:
                ch_w "Мы. . . довольно близки."
            elif WandaX.LikeDoreen >= 700:
                ch_w "Она очень дружелюбная."
            elif WandaX.LikeDoreen >= 600:
                ch_w "Она довольно клевая."
            elif WandaX.LikeDoreen >= 500:
                ch_w "Я не уверена, но, думаю, мы с ней поладим."
            elif WandaX.LikeDoreen >= 400:
                ch_w "У нас с ней были не очень приятные моменты. . ."
            elif WandaX.LikeDoreen >= 300:
                ch_w "Я ненавижу ее. . . ладно, на самом деле я думаю, что она довольно милая."
            else:
                ch_w "Она шлюха."
    else:
                ch_w "Она. . . неважно."
    return
#End Wanda_AboutEmma

label Wanda_Monogamy: #rkeljsvgbdw
        #called from Wanda_Settings to ask her not to hook up with other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in WandaX.Traits:
                    if WandaX.Thirst >= 60 and not ApprovalCheck(WandaX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ WandaX.FaceChange("sly",1)
                            if "mono" not in WandaX.DailyActions:
                                    $ WandaX.Statup("Obed", 90, -2)
                            ch_w "Это невозможно."
                            return
                    elif ApprovalCheck(WandaX, 1200, "LO", TabM=0) and WandaX.Love >= WandaX.Obed:
                            #she cares
                            $ WandaX.FaceChange("sly",1)
                            if "mono" not in WandaX.DailyActions:
                                    $ WandaX.Statup("Love", 90, 1)
                            ch_w "Тогда тебе придется уделять мне больше внимания. . ."
                    elif ApprovalCheck(WandaX, 700, "O", TabM=0):
                            #she is obedient
                            $ WandaX.FaceChange("sly",1,Eyes="side")
                            ch_w ". . . я попробую. . ."
                    else:
                            #she doesn't care
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Нет."
                            return
                    if "mono" not in WandaX.DailyActions:
                            $ WandaX.Statup("Obed", 90, 3)
                    $ WandaX.AddWord(1,0,"mono") #Daily
                    $ WandaX.Traits.append("mono")
            "Не встречайся с другими девушками." if "mono" not in WandaX.Traits:
                    if ApprovalCheck(WandaX, 900, "O", TabM=0):
                            #she is obedient
                            $ WandaX.FaceChange("sly",1,Eyes="side")
                            ch_w ". . . я попробую. . ."
                    elif WandaX.Thirst >= 60 and not ApprovalCheck(WandaX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ WandaX.FaceChange("sly",1)
                            if "mono" not in WandaX.DailyActions:
                                    $ WandaX.Statup("Obed", 90, -2)
                            ch_w "Это невозможно."
                            return
                    elif ApprovalCheck(WandaX, 600, "O", TabM=0):
                            #she is obedient
                            $ WandaX.FaceChange("sly",1,Eyes="side")
                            ch_w ". . . я попробую. . ."
                    elif ApprovalCheck(WandaX, 1400, "LO", TabM=0):
                            #she cares
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Тогда тебе придется уделять мне больше внимания. . ."
                    else:
                            #she doesn't care
                            $ WandaX.FaceChange("sly",1,Brows="confused")
                            ch_w "Нет."
                            return
                    if "mono" not in WandaX.DailyActions:
                            $ WandaX.Statup("Obed", 90, 3)
                    $ WandaX.AddWord(1,0,"mono") #Daily
                    $ WandaX.Traits.append("mono")
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in WandaX.Traits:
                    if ApprovalCheck(WandaX, 700, "O", TabM=0):
                            $ WandaX.FaceChange("sly",1,Eyes="side")
                            ch_w "Ладно."
                    elif ApprovalCheck(WandaX, 800, "L", TabM=0):
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Конечно. . ."
                    else:
                            $ WandaX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in WandaX.DailyActions:
                                    $ WandaX.Statup("Love", 90, -2)
                            ch_w "Ладно."
                    if "mono" not in WandaX.DailyActions:
                            $ WandaX.Statup("Obed", 90, 3)
                    if "mono" in WandaX.Traits:
                            $ WandaX.Traits.remove("mono")
                    $ WandaX.AddWord(1,0,"mono") #Daily
            "Неважно.":
                pass
        return

# end Wanda monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Wanda_Jumped: #rkeljsvgbdw
        #called from Wanda_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ WandaX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_w "Что-то не так?"
            "На будущее, можешь сначала спрашивать?" if "chill" not in WandaX.Traits:
                    if WandaX.Thirst >= 60 and not ApprovalCheck(WandaX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ WandaX.FaceChange("sly",1)
                            if "chill" not in WandaX.DailyActions:
                                    $ WandaX.Statup("Obed", 90, -2)
                            ch_w "Когда ты рядом, я не могу держать себя в руках. . ."
                            return
                    elif ApprovalCheck(WandaX, 1000, "LO", TabM=0) and WandaX.Love >= WandaX.Obed:
                            #she cares
                            $ WandaX.FaceChange("surprised",1)
                            if "chill" not in WandaX.DailyActions:
                                    $ WandaX.Statup("Love", 90, 1)
                            ch_w "Мне очень нужно внимание. . ."
                            $ WandaX.FaceChange("sly",1,Eyes="side")
                            ch_w "-но я попробую. . ."
                    elif ApprovalCheck(WandaX, 500, "O", TabM=0):
                            #she is obedient
                            $ WandaX.FaceChange("sly",1,Eyes="side")
                            ch_w ". . . ладно. . ."
                    else:
                            #she doesn't care
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Посмотрим . ."
                            return
                    if "chill" not in WandaX.DailyActions:
                            $ WandaX.Statup("Obed", 90, 3)
                    $ WandaX.AddWord(1,0,"chill") #Daily
                    $ WandaX.Traits.append("chill")
            "Больше так не делай." if "chill" not in WandaX.Traits:
                    if ApprovalCheck(WandaX, 800, "O", TabM=0):
                            #she is obedient
                            $ WandaX.FaceChange("sly",1,Eyes="side")
                            ch_w ". . . ладно. . ."
                    elif WandaX.Thirst >= 60 and not ApprovalCheck(WandaX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ WandaX.FaceChange("sly",1)
                            if "chill" not in WandaX.DailyActions:
                                    $ WandaX.Statup("Obed", 90, -2)
                            ch_w "Когда ты рядом, я не могу держать себя в руках. . ."
                            return
                    elif ApprovalCheck(WandaX, 400, "O", TabM=0):
                            #she is obedient
                            $ WandaX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_w "Хорошо, госпожа. . ."
                            else:
                                ch_w "Хорошо, господин. . ."
                    elif ApprovalCheck(WandaX, 500, "LO", TabM=0) and not ApprovalCheck(WandaX, 500, "I", TabM=0):
                            #she cares
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Ладно. . ."
                            ch_w "Прости."
                    else:
                            #she doesn't care
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Не волнуйся, я сделаю так, чтобы тебе понравилось."
                            return
                    if "chill" not in WandaX.DailyActions:
                            $ WandaX.Statup("Obed", 90, 3)
                    $ WandaX.AddWord(1,0,"chill") #Daily
                    $ WandaX.Traits.append("chill")
            "Делай что хочешь.":
                    if ApprovalCheck(WandaX, 800, "L", TabM=0):
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Конечно!"
                    elif ApprovalCheck(WandaX, 700, "O", TabM=0):
                            $ WandaX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_w "Обязательно, госпожа."
                            else:
                                ch_w "Обязательно, господин."
                    else:
                            $ WandaX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in WandaX.DailyActions:
                                    $ WandaX.Statup("Love", 90, -2)
                            ch_w "Посмотрим. . ."
                    if "chill" not in WandaX.DailyActions:
                            $ WandaX.Statup("Obed", 90, 3)
                    if "chill" in WandaX.Traits:
                            $ WandaX.Traits.remove("chill")
                    $ WandaX.AddWord(1,0,"chill") #Daily
            "Эм, неважно.":
                pass
        return

# end Wanda jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start Wanda hungry //////////////////////////////////////////////////////////
label Wanda_Hungry: #rkeljsvgbdw
    if WandaX.Chat[3]:
        ch_w "Я невероятно хочу тебя. . ."
    elif WandaX.Chat[2]:
        if not Player.Male:
            ch_w "Сыворотка, которую ты мне дала, была очень хороша. . ."
        else:
            ch_w "Сыворотка, которую ты мне дал, была очень хороша. . ."
    else:
        ch_w "Я невероятно хочу тебя. . ."
        ch_w "И ты знаешь почему. . ."
    $ WandaX.Traits.append("hungry")
return


# end Wanda hungry //////////////////////////////////////////////////////////

# Wanda Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Wanda_SexChat: #rkeljsvgbdw
    $ Line = "Что ты хочешь обсудить?" if not Line else Line
    while True:
            menu:
                ch_w "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in WandaX.DailyActions:
                        ch_w "Конечно, я знаю."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ WandaX.FaceChange("sly")
                                        if WandaX.PlayerFav == "sex":
                                            $ WandaX.Statup("Lust", 80, 5)
                                            ch_w "Я знаю. . ."
                                        elif WandaX.Favorite == "sex":
                                            $ WandaX.Statup("Love", 90, 5)
                                            $ WandaX.Statup("Lust", 80, 10)
                                            ch_w "Понимаю."
                                        elif WandaX.Sex >= 5:
                                            ch_w "Ну, я не возражаю."
                                        elif not WandaX.Sex:
                                            $ WandaX.FaceChange("perplexed")
                                            ch_w "С кем ты занимаешься сексом?"
                                        else:
                                            $ WandaX.FaceChange("bemused")
                                            ch_w "О, ага. . ."
                                        $ WandaX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ WandaX.FaceChange("sly")
                                        if WandaX.PlayerFav == "anal":
                                            $ WandaX.Statup("Lust", 80, 5)
                                            ch_w "Я знаю. . ."
                                        elif WandaX.Favorite == "anal":
                                            $ WandaX.Statup("Love", 90, 5)
                                            $ WandaX.Statup("Lust", 80, 10)
                                            ch_w "У меня тоже!"
                                        elif WandaX.Anal >= 10:
                                            ch_w "Ага. . ."
                                        elif not WandaX.Anal:
                                            $ WandaX.FaceChange("perplexed")
                                            ch_w "С кем ты этим занимаешься?"
                                        else:
                                            $ WandaX.FaceChange("bemused",Eyes="side")
                                            ch_w "Ох, ого. . ."
                                        $ WandaX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ WandaX.FaceChange("sly")
                                        if WandaX.PlayerFav == "blow":
                                            $ WandaX.Statup("Lust", 80, 3)
                                            ch_w "Я знаю. . ."
                                        elif WandaX.Favorite == "blow":
                                            $ WandaX.Statup("Love", 90, 5)
                                            $ WandaX.Statup("Lust", 80, 5)
                                            ch_w "У меня тоже!"
                                        elif WandaX.Blow >= 10:
                                            ch_w "Ага, ты очень вкусный."
                                        elif not WandaX.Blow:
                                            $ WandaX.FaceChange("perplexed")
                                            ch_w "Кто тебе сосет?"
                                        else:
                                            $ WandaX.FaceChange("bemused")
                                            ch_w "Конечно. . ."
                                        $ WandaX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ WandaX.FaceChange("sly")
                                        if WandaX.PlayerFav == "cun":
                                            $ WandaX.Statup("Lust", 80, 3)
                                            ch_w "Я знаю. . ."
                                        elif WandaX.Favorite == "cun":
                                            $ WandaX.Statup("Love", 90, 5)
                                            $ WandaX.Statup("Lust", 80, 5)
                                            ch_w "У меня тоже!"
                                        elif WandaX.CUN >= 10:
                                            ch_w "Ага, ты очень вкусная."
                                        elif not WandaX.CUN:
                                            $ WandaX.FaceChange("perplexed")
                                            ch_w "Кто тебе отлизывает?"
                                        else:
                                            $ WandaX.FaceChange("bemused")
                                            ch_w "Конечно. . ."
                                        $ WandaX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ WandaX.FaceChange("sly")
                                        if WandaX.PlayerFav == "titjob":
                                            $ WandaX.Statup("Lust", 80, 5)
                                            ch_w "Я знаю. . ."
                                        elif WandaX.Favorite == "titjob":
                                            $ WandaX.Statup("Love", 90, 5)
                                            $ WandaX.Statup("Lust", 80, 7)
                                            ch_w "У меня тоже!"
                                        elif WandaX.Tit >= 10:
                                            ch_w "Это очень весело. . ."
                                        elif not WandaX.Tit:
                                            $ WandaX.FaceChange("perplexed")
                                            ch_w "С кем ты этим занимаешься?"
                                        else:
                                            $ WandaX.FaceChange("bemused")
                                            ch_w "И почему я не удивлена? . ."
                                            $ WandaX.Statup("Love", 80, 5)
                                            $ WandaX.Statup("Inbt", 50, 10)
                                        $ WandaX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ WandaX.FaceChange("sly")
                                        if WandaX.PlayerFav == "foot":
                                            $ WandaX.Statup("Lust", 80, 5)
                                            ch_w "Я знаю. . ."
                                        elif WandaX.Favorite == "foot":
                                            $ WandaX.Statup("Love", 90, 5)
                                            $ WandaX.Statup("Lust", 80, 7)
                                            ch_w "У меня тоже!"
                                        elif WandaX.Foot >= 10:
                                            ch_w "Мне это тоже очень нравится. . ."
                                        elif not WandaX.Foot:
                                            $ WandaX.FaceChange("perplexed")
                                            ch_w "С кем ты этим занимаешься?"
                                        else:
                                            $ WandaX.FaceChange("bemused")
                                            ch_w "Ага, это приятно. . ."
                                        $ WandaX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ WandaX.FaceChange("sly")
                                        if WandaX.PlayerFav == "hand":
                                            $ WandaX.Statup("Lust", 80, 5)
                                            ch_w "Я знаю. . ."
                                        elif WandaX.Favorite == "hand":
                                            $ WandaX.Statup("Love", 90, 5)
                                            $ WandaX.Statup("Lust", 80, 7)
                                            ch_w "Мне тоже нравится."
                                        elif WandaX.Hand >= 10:
                                            ch_w "Мне тоже это очень нравится. . ."
                                        elif not WandaX.Hand:
                                            $ WandaX.FaceChange("perplexed")
                                            ch_w "С кем ты этим занимаешься?"
                                        else:
                                            $ WandaX.FaceChange("bemused")
                                            ch_w "Ага, это приятно. . ."
                                        $ WandaX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ WandaX.FaceChange("sly")
                                        if WandaX.PlayerFav == "finger":
                                            $ WandaX.Statup("Lust", 80, 5)
                                            ch_w "Я знаю. . ."
                                        elif WandaX.Favorite == "finger":
                                            $ WandaX.Statup("Love", 90, 5)
                                            $ WandaX.Statup("Lust", 80, 7)
                                            ch_w "Знаешь, мне тоже это очень нравится!"
                                        elif WandaX.Finger >= 10:
                                            ch_w "Мне это тоже очень нравится. . ."
                                        elif not WandaX.Finger:
                                            $ WandaX.FaceChange("perplexed")
                                            ch_w "С кем ты этим занимаешься?"
                                        else:
                                            $ WandaX.FaceChange("bemused")
                                            ch_w "Ага, это довольно приятно. . ."
                                        $ WandaX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = WandaX.FondleB + WandaX.FondleT + WandaX.SuckB + WandaX.Hotdog
                                        $ WandaX.FaceChange("sly")
                                        if WandaX.PlayerFav == "fondle":
                                            $ WandaX.Statup("Lust", 80, 3)
                                            ch_w "Я знаю. . ."
                                        elif WandaX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ WandaX.Statup("Love", 90, 5)
                                            $ WandaX.Statup("Lust", 80, 5)
                                            ch_w "Знаешь, мне тоже это очень нравится!"
                                        elif Cnt >= 10:
                                            ch_w "Мне это тоже очень нравится. . ."
                                        elif not Cnt:
                                            $ WandaX.FaceChange("perplexed")
                                            ch_w "Кого ты лапаешь?"
                                        else:
                                            $ WandaX.FaceChange("bemused")
                                            ch_w "У тебя замечательные руки. . ."
                                        $ WandaX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ WandaX.FaceChange("sly")
                                        if WandaX.PlayerFav == "kiss you":
                                            $ WandaX.Statup("Love", 90, 3)
                                            ch_w "Это так мило. . ."
                                        elif WandaX.Favorite == "kiss you":
                                            $ WandaX.Statup("Love", 90, 5)
                                            $ WandaX.Statup("Lust", 80, 5)
                                            ch_w "У тебя это неплохо получается."
                                        elif WandaX.Kissed >= 10:
                                            ch_w "Мне тоже это очень нравится. . ."
                                        elif not WandaX.Kissed:
                                            $ WandaX.FaceChange("perplexed")
                                            ch_w "С кем ты целуешься?"
                                        else:
                                            $ WandaX.FaceChange("bemused")
                                            ch_w "Мне тоже это нравится. . ."
                                        $ WandaX.PlayerFav = "kiss you"

                        $ WandaX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(WandaX, 800):
                                            $ WandaX.FaceChange("perplexed")
                                            ch_w ". . ."
                                else:
                                        if WandaX.SEXP >= 50:
                                            $ WandaX.FaceChange("sly")
                                            if not Player.Male:
                                                ch_w "Ты должна знать, что меня заводит. . ."
                                            else:
                                                ch_w "Ты должен знать, что меня заводит. . ."
                                        else:
                                            $ WandaX.FaceChange("bemused")
                                            $ WandaX.Eyes = "side"
                                            ch_w "Хм. . ."


                                        if not WandaX.Favorite or WandaX.Favorite == "kiss":
                                                ch_w "Наверное, поцелуи. . ."
                                        elif WandaX.Favorite == "anal":
                                                ch_w "Возможно, анал?"
                                        elif WandaX.Favorite == "lick ass":
                                                ch_w "Возможно, когда ты. . . вылизываешь мою попку?"
                                        elif WandaX.Favorite == "insert ass":
                                                ch_w "Наверное, когда ты трахаешь мою попку пальцем. . ."
                                        elif WandaX.Favorite == "sex":
                                                ch_w "Все просто, я люблю хороший трах."
                                        elif WandaX.Favorite == "lick pussy":
                                                ch_w "Ты очень хорошо работаешь язычком."
                                        elif WandaX.Favorite == "fondle pussy":
                                                ch_w "У тебя волшебные пальцы."
                                        elif WandaX.Favorite == "blow":
                                                ch_w "Мне нравится вкус твоего члена."
                                        elif WandaX.Favorite == "cun":
                                                ch_w "Мне нравится вкус твоей киски."
                                        elif WandaX.Favorite == "tit":
                                                ch_w "Работать сиськами - это весело."
                                        elif WandaX.Favorite == "foot":
                                                ch_w "Думаю, мне нравится использовать свои ножки."
                                        elif WandaX.Favorite == "hand":
                                                ch_w "Мне нравится дрочить тебе."
                                        elif WandaX.Favorite == "finger":
                                                ch_w "Мне нравится ласкать твою киску."
                                        elif WandaX.Favorite == "hotdog":
                                                ch_w "Мне нравится, когда ты трешься о меня."
                                        elif WandaX.Favorite == "suck breasts":
                                                ch_w "Мне нравится, когда ты сосешь мою грудь."
                                        elif WandaX.Favorite == "fondle breasts":
                                                ch_w "Мне нравится, когда ты ласкаешь мою грудь."
                                        elif WandaX.Favorite == "fondle thighs":
                                                ch_w "Мне нравится, когда ты трогаешь мои бедра."
                                        else:
                                                ch_w "Что-. . .эм. . . я не знаю. . . наверное, то, что нравится тебе? . ."

                                # End Wanda's favorite things.

                "Не болтай так много во время секса." if "vocal" in WandaX.Traits:
                        if "setvocal" in WandaX.DailyActions:
                                $ WandaX.FaceChange("perplexed")
                                ch_w "Определись, чего ты хочешь."
                        else:
                            if ApprovalCheck(WandaX, 1000) and WandaX.Obed <= WandaX.Love:
                                $ WandaX.FaceChange("bemused")
                                $ WandaX.Statup("Obed", 90, 1)
                                ch_w "Ладно, я заткнусь."
                                $ WandaX.Traits.remove("vocal")
                            elif ApprovalCheck(WandaX, 700, "O"):
                                $ WandaX.FaceChange("sadside")
                                $ WandaX.Statup("Obed", 90, 1)
                                ch_w ". . ."
                                $ WandaX.Traits.remove("vocal")
                            elif ApprovalCheck(WandaX, 600):
                                $ WandaX.FaceChange("sly")
                                $ WandaX.Statup("Love", 90, -3)
                                $ WandaX.Statup("Obed", 50, -1)
                                $ WandaX.Statup("Inbt", 90, 5)
                                ch_w "Попробуй остановить меня."
                            else:
                                $ WandaX.FaceChange("angry")
                                $ WandaX.Statup("Love", 90, -5)
                                $ WandaX.Statup("Obed", 60, -3)
                                $ WandaX.Statup("Inbt", 90, 10)
                                ch_w "Попробуй остановить меня."

                            $ WandaX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in WandaX.Traits:
                        if "setvocal" in WandaX.DailyActions:
                                $ WandaX.FaceChange("perplexed")
                                ch_w "Определись, чего ты хочешь."
                        else:
                            if ApprovalCheck(WandaX, 1000) and WandaX.Obed <= WandaX.Love:
                                $ WandaX.FaceChange("sly")
                                $ WandaX.Statup("Obed", 90, 2)
                                ch_w "Осторожнее в своих желаниях."
                                $ WandaX.Traits.append("vocal")
                            elif ApprovalCheck(WandaX, 700, "O"):
                                $ WandaX.FaceChange("sadside")
                                $ WandaX.Statup("Obed", 90, 2)
                                ch_w "Я могу попробовать."
                                $ WandaX.Traits.append("vocal")
                            elif ApprovalCheck(WandaX, 600):
                                $ WandaX.FaceChange("sly")
                                $ WandaX.Statup("Obed", 90, 3)
                                ch_w "Ладно?"
                                $ WandaX.Traits.append("vocal")
                            else:
                                $ WandaX.FaceChange("angry")
                                $ WandaX.Statup("Inbt", 90, 5)
                                ch_w ". . ."

                            $ WandaX.DailyActions.append("setvocal")
                        # End Wanda Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in WandaX.Traits:
                        if "initiative" in WandaX.DailyActions:
                                $ WandaX.FaceChange("perplexed")
                                ch_w "Определись, чего ты хочешь."
                        else:
                            if ApprovalCheck(WandaX, 1200) and WandaX.Obed <= WandaX.Love:
                                $ WandaX.FaceChange("bemused")
                                $ WandaX.Statup("Obed", 90, 1)
                                ch_w "Тогда все на тебе."
                                $ WandaX.Traits.append("passive")
                            elif ApprovalCheck(WandaX, 700, "O"):
                                $ WandaX.FaceChange("sadside")
                                $ WandaX.Statup("Obed", 90, 1)
                                ch_w "Тогда я оставляю все на тебя."
                                $ WandaX.Traits.append("passive")
                            elif ApprovalCheck(WandaX, 600):
                                $ WandaX.FaceChange("sly")
                                $ WandaX.Statup("Love", 90, -3)
                                $ WandaX.Statup("Obed", 50, -1)
                                $ WandaX.Statup("Inbt", 90, 5)
                                ch_w "Посмотрим."
                            else:
                                $ WandaX.FaceChange("angry")
                                $ WandaX.Statup("Love", 90, -5)
                                $ WandaX.Statup("Obed", 60, -3)
                                $ WandaX.Statup("Inbt", 90, 10)
                                ch_w "Посмотрим."

                            $ WandaX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in WandaX.Traits:
                        if "initiative" in WandaX.DailyActions:
                                $ WandaX.FaceChange("perplexed")
                                ch_w "Ох, определись уже."
                        else:
                            if ApprovalCheck(WandaX, 1000) and WandaX.Obed <= WandaX.Love:
                                $ WandaX.FaceChange("bemused")
                                $ WandaX.Statup("Obed", 90, 1)
                                ch_w "О, конечно."
                                $ WandaX.Traits.remove("passive")
                            elif ApprovalCheck(WandaX, 700, "O"):
                                $ WandaX.FaceChange("sadside")
                                $ WandaX.Statup("Obed", 90, 1)
                                ch_w "Я могу попробовать."
                                $ WandaX.Traits.remove("passive")
                            elif ApprovalCheck(WandaX, 600):
                                $ WandaX.FaceChange("sly")
                                $ WandaX.Statup("Obed", 90, 3)
                                ch_w "Посмотрим."
                                $ WandaX.Traits.remove("passive")
                            else:
                                $ WandaX.FaceChange("angry")
                                $ WandaX.Statup("Inbt", 90, 5)
                                ch_w "Для этого у меня есть ты."

                            $ WandaX.DailyActions.append("initiative")

                "О том, как ты накидываешься" if "jumped" in WandaX.History:
                        call Wanda_Jumped
                "О твоей мастурбации":
                        call NoFap(WandaX)

                "Всегда носи вибратор" if "dailyvibe" not in WandaX.Traits:
                        call Daily_Vibrator(WandaX)
                "Перестань всегда носить вибратор" if "dailyvibe" in WandaX.Traits:
                        ch_w "Ладно. . ."
                        $ WandaX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи анальную пробку" if "dailyplug" not in WandaX.Traits:
                        call Daily_Plug(WandaX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in WandaX.Traits:
                        ch_w "Ладно. . ."
                        $ WandaX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Неважно" if Line == "Что ты хочешь обсудить?":
                        return
                "На этом все" if Line != "Что ты хочешь обсудить?":
                        return
            if Line == "Что ты хочешь обсудить?":
                $ Line = "Значит, на этом все?"
    return
# End Wanda Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Wanda Chitchat /////////////////// #Work in progress
label Wanda_Chitchat(O=0, Options = ["default","default","default"]): #rkeljsvg
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if WandaX not in Digits:
                if ApprovalCheck(WandaX, 500, "L") or ApprovalCheck(WandaX, 250, "I"):
                    ch_w "Послушай, если тебе нужен мой номер телефона, вот."
                    $ Digits.append(WandaX)
                    return
                elif ApprovalCheck(WandaX, 250, "O"):
                    ch_w "Послушай, если тебе нужен мой номер телефона, вот."
                    $ Digits.append(WandaX)
                    return

        if "hungry" not in WandaX.Traits and (WandaX.Swallow + WandaX.Chat[2]) >= 10 and WandaX.Loc == bg_current:  #She's swallowed a lot
                    call Wanda_Hungry
                    return

        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(WandaX, 700, "I")):
                    if WandaX.Loc == bg_current and WandaX.Thirst >= 30 and "refused" not in WandaX.DailyActions and "quicksex" not in WandaX.DailyActions:
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Слушай, не хочешь немного повеселиться?"
                            call Quick_Sex(WandaX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in WandaX.DailyActions:
#            $ Options.append("caught")
        if WandaX.Event[0] and "key" not in WandaX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in WandaX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in WandaX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in WandaX.DailyActions:
            $ Options.append("corruption")

#        if "Wanda" not in WandaX.Names:
#            $ Options.append("wanda")

        if WandaX.Date >= 1 and bg_current != "bg restaurant":
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in WandaX.DailyActions and "cheek" not in WandaX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if WandaX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in WandaX.DailyActions and (Player.Male or "girltalk" in WandaX.History):
            #If you've caught Wanda showering today
            $ Options.append("showercaught")
        if "fondle breasts" in WandaX.DailyActions or "fondle pussy" in WandaX.DailyActions or "fondle ass" in WandaX.DailyActions:
            #If you've fondled Wanda today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in WandaX.Inventory and "256 Shades of Grey" in WandaX.Inventory and "Avengers Tower Penthouse" in WandaX.Inventory:
            #If you've given Wanda the books
            if "book" not in WandaX.Chat:
                $ Options.append("booked")
        if "lace bra" in WandaX.Inventory or "lace panties" in WandaX.Inventory:
            #If you've given Wanda the lingerie
            if "lingerie" not in WandaX.Chat:
                $ Options.append("lingerie")
        if WandaX.Hand and Player.Male:
            #If Wanda's given a handjob
            $ Options.append("handy")
        if WandaX.Blow and Player.Male:
            #If Wanda's given a blowjob
            $ Options.append("blow")
        if WandaX.Swallow:
            #If Wanda's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in WandaX.DailyActions or "painted" in WandaX.DailyActions:
            #If Wanda's been facialed
            $ Options.append("facial")
        if WandaX.Sleep:
            #If Wanda's slept over
            $ Options.append("sleep")
        if (WandaX.CreamP or WandaX.CreamA) and Player.Male:
            #If Wanda's been creampied
            $ Options.append("creampie")
        if WandaX.Sex or WandaX.Anal:
            #If Wanda's been sexed
            $ Options.append("sexed")
        if WandaX.Anal:
            #If Wanda's been analed
            $ Options.append("anal")

        if "seenpeen" in WandaX.History and Player.Male:
            $ Options.append("seenpeen")
        if "topless" in WandaX.History:
            $ Options.append("topless")
        if "bottomless" in WandaX.History:
            $ Options.append("bottomless")

#        if not WandaX.Chat[0] and WandaX.Sex:
#            $ Options.append("virgin")

#        if (bg_current == "bg wanda" or bg_current == "bg player") and "relationship" not in WandaX.DailyActions:
#            if "lover" not in WandaX.Petnames and ApprovalCheck(WandaX, 900, "L"): # WandaX.Event[6]
#                $ Options.append("lover?")
#            elif "sir" not in WandaX.Petnames and ApprovalCheck(WandaX, 500, "O"): # WandaX.Event[7]
#                $ Options.append("sir?")
#            elif "daddy" not in WandaX.Petnames and ApprovalCheck(WandaX, 750, "L") and ApprovalCheck(WandaX, 500, "O") and ApprovalCheck(WandaX, 500, "I"): # WandaX.Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in WandaX.Petnames and ApprovalCheck(WandaX, 900, "O"): # WandaX.Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in WandaX.Petnames and ApprovalCheck(WandaX, 500, "I"): # WandaX.Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in WandaX.Petnames and ApprovalCheck(WandaX, 900, "I"): # WandaX.Event[10]
#                $ Options.append("fuckbuddy?")


        if not ApprovalCheck(WandaX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ WandaX.DailyActions.append("cologne chat")
        $ WandaX.FaceChange("confused")
        ch_w "(нюх, нюх). . . я чувствую. . . мускус. . ."
        $ WandaX.FaceChange("sexy", 2)
        ch_w ". . . мне. . . нравится? . ."
    elif Options[0] == "purple":
        $ WandaX.DailyActions.append("cologne chat")
        $ WandaX.FaceChange("sly",1)
        ch_w "(нюх, нюх). . . что это за запах? . ."
        $ WandaX.FaceChange("normal",0)
        ch_w ". . . тебе что-нибудь нужно?"
    elif Options[0] == "corruption":
        $ WandaX.DailyActions.append("cologne chat")
        $ WandaX.FaceChange("confused")
        ch_w "(нюх, нюх). . . ого, какой мощный аромат. . ."
        $ WandaX.FaceChange("angry",Eyes="psychic")
        ch_w ". . . у меня начинают появляться. . . мрачные мысли. . ."
        $ WandaX.FaceChange("sly")

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in WandaX.Chat:
                    ch_w "Эй! Из-за тебя меня могли снова упечь за решетку!"
                    if not ApprovalCheck(WandaX, 500, "I"):
                         ch_w "Но это было довольно захватывающе. . ."
            else:
                    ch_w "[WandaX.Petname], из-за тебя меня снова могли упечь за решетку!"
                    if not ApprovalCheck(WandaX, 500, "I"):
                        ch_w "Наверное, нам стоит быть не такими заметными. . ."
                    else:
                         ch_w "-но это было довольно весело. . ."
                    $ WandaX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if WandaX.SEXP <= 15:
                ch_w "Осторожнее с ключом от моей комнаты. . ."
            else:
                ch_w "Слушай, помнишь, я дала тебе ключ от своей комнаты? Возможно, тебе стоит пользоваться им почаще. . ."
            $ WandaX.Chat.append("key")

    elif Options[0] == "dated":
            #Wanda's response to having gone on a date with the Player.
            ch_w "Тем вечером я неплохо повеселилась. Мы должны как-нибудь повторить."

    elif Options[0] == "kissed":
            #Wanda's response to having been kissed by the Player.
            $ WandaX.FaceChange("normal",1)
            ch_w "Хочешь снова поцеловаться, [WandaX.Petname]?"
            menu:
                extend ""
                "Тебе понравилось?":
                        $ WandaX.FaceChange("smile",1)
                        ch_w "Хех, ага. . ."
                        call SexAct("kissing")
                "Конечно.":
                        $ WandaX.FaceChange("smile",1)
                        ch_w "Хех. . ."
                        call SexAct("kissing")
                "Не сейчас.":
                        $ WandaX.FaceChange("smile",1)
                        ch_w "Ладно, многое упускаешь."

    elif Options[0] == "dangerroom":
            #Wanda's response to Player working out in the Danger Room while Wanda is present
            $ WandaX.FaceChange("sly",1)
            ch_w "Я видела тебя в Комнате Опасности."
            ch_w "Впечатляет."

    elif Options[0] == "showercaught":
            #Wanda's response to being caught in the shower.
            if "shower" in WandaX.Chat:
                ch_w "Ты постоянно застаешь меня в душе. . ."
            else:
                ch_w "Ты постоянно застаешь меня в душе. . ."
                ch_w "Думаю, я уже привыкла к этому."
                $ WandaX.Chat.append("shower")
#                menu:
#                    extend ""
#                    "It was a total accident! I promise!":
#                            $ WandaX.Statup("Love", 50, 5)
#                            $ WandaX.Statup("Love", 90, 2)
#                            if ApprovalCheck(WandaX, 1200):
#                                $ WandaX.FaceChange("sly",1)
#                                ch_w "Oh, sure. . ."
#                                ch_w "I guess I don't mind -that- much. . ."
#                            else:
#                                $ WandaX.FaceChange("smile")
#                                ch_w "Oh, sure. . ."
#                    "Just with you.":
#                            $ WandaX.Statup("Obed", 40, 5)
#                            if ApprovalCheck(WandaX, 1000) or ApprovalCheck(WandaX, 700, "L"):
#                                    $ WandaX.Statup("Love", 90, 3)
#                                    $ WandaX.FaceChange("surprised",2,Mouth="normal")
#                                    ch_w "Oh. . ."
#                                    $ WandaX.FaceChange("sly",1)
#                                    ch_w "Well. . . thanks?"
#                            else:
#                                    $ WandaX.Statup("Love", 70, -5)
#                                    $ WandaX.FaceChange("angry")
#                                    ch_w "I don't think you got my point. . ."
#                    "Totally on purpose. I regret nothing.":
#                            if ApprovalCheck(WandaX, 1200):
#                                    $ WandaX.Statup("Love", 90, 3)
#                                    $ WandaX.Statup("Obed", 70, 10)
#                                    $ WandaX.Statup("Inbt", 50, 5)
#                                    $ WandaX.FaceChange("sly",1)
#                                    ch_w "Fair."
#                            elif ApprovalCheck(WandaX, 800):
#                                    $ WandaX.Statup("Obed", 60, 5)
#                                    $ WandaX.Statup("Inbt", 50, 5)
#                                    $ WandaX.FaceChange("perplexed",2)
#                                    ch_w "Well. . . ok then. . ."
#                                    $ WandaX.Blush = 1
#                            else:
#                                    $ WandaX.Statup("Love", 50, -10)
#                                    $ WandaX.Statup("Love", 80, -10)
#                                    $ WandaX.Statup("Obed", 50, 10)
#                                    $ WandaX.FaceChange("angry")
#                                    ch_w "That doesn't help at all!"

    elif Options[0] == "fondled":
            #Wanda's response to being felt up.
            if WandaX.FondleB + WandaX.FondleP + WandaX.FondleA >= 15:
                ch_w "Слушай, просто напоминаю, что иногда мне не помешал бы массаж. . ."
            else:
                ch_w "Слушай, какая часть моего тела тебе больше всего нравится? . ."
                ch_w "Я только за, если ты захочешь к ней прикоснуться. . ."

    elif Options[0] == "booked":
            #Wanda's response after a Player gives her the books from the shop.
            if not Player.Male:
                ch_w "Я прочитала те книги, которые ты мне дала. . ."
            else:
                ch_w "Я прочитала те книги, которые ты мне дал. . ."
            menu:
                extend ""
                "Да? И как тебе?":
                        $ WandaX.FaceChange("sly",2)
                        ch_w "Они довольно безумные. . ."
                "Хорошо. Пожалуй, ты могла бы чему-нибудь из них научиться.":
                        $ WandaX.Statup("Obed", 70, 5)
                        $ WandaX.Statup("Inbt", 50, 5)
                        $ WandaX.FaceChange("surprised",2)
                        ch_w "Ага, видимо, даже -очень- многому."
            $ WandaX.Blush = 1
            $ WandaX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Wanda's response to being given lingerie.
            $ WandaX.FaceChange("sly",2)
            if not Player.Male:
                ch_w "Мне нравится нижнее белье, которое ты мне подарила."
            else:
                ch_w "Мне нравится нижнее белье, которое ты мне подарил."
            ch_w "Оно очень сексуальное. . ."
            $ WandaX.Blush = 1
            $ WandaX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Wanda's response after giving the Player a handjob.
            $ WandaX.FaceChange("sly",1)
            ch_w "Слушай, если тебе когда-нибудь снова понадобится \"рука помощи\", просто дай мне знать. . ."

    elif Options[0] == "blow":
            if "blow" not in WandaX.Chat:
                    #Wanda's response after giving the Player a blowjob.
                    $ WandaX.FaceChange("sly",2)
                    ch_w "Я ведь неплохо делаю минет, правда?"
                    menu:
                        extend ""
                        "Ты была великолепна.":
                                    $ WandaX.Statup("Love", 90, 5)
                                    $ WandaX.Statup("Inbt", 60, 10)
                                    $ WandaX.FaceChange("sly",1,Eyes="side")
                                    ch_w "Вот и хорошо. . ."
                                    $ WandaX.FaceChange("sexy",1)
                                    ch_w "Дай мне знать, если захочешь повторить. . ."
                        "Честно? Все было хорошо. . . но, думаю, тебе не помешает еще немного попрактиковаться.":
                                if ApprovalCheck(WandaX, 300, "I") or not ApprovalCheck(WandaX, 800):
                                    $ WandaX.Statup("Love", 90, -5)
                                    $ WandaX.Statup("Obed", 60, 10)
                                    $ WandaX.Statup("Inbt", 50, 10)
                                    $ WandaX.FaceChange("perplexed",1)
                                    ch_w "Это непростая задача. . ."
                                else:
                                    $ WandaX.Statup("Obed", 70, 15)
                                    $ WandaX.Statup("Inbt", 50, 5)
                                    $ WandaX.FaceChange("sexy",1)
                                    ch_w "Хмммм. . . как скажешь. . ."
                        "Угу, если бы мне нравились стремные звуки и шкрябанье зубов по члену, но это далеко не так.":
                                    $ WandaX.Statup("Love", 70, -5)
                                    $ WandaX.Statup("Love", 90, -10)
                                    $ WandaX.Statup("Obed", 60, 10)
                                    $ WandaX.FaceChange("angry",2)
                                    ch_w ". . ."
                                    ch_w "Не такого ответа я ждала."
                    $ WandaX.Blush = 1
                    $ WandaX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["Мне нужно еще раз попробовать твой член.",
                            "У меня все еще сводит челюсь. . . с этим что-то нужно делать.",
                            "Хочешь как-нибудь еще один минет?",
                            "Хмммм. . . [Стучит языком по внутренней стороне щеки.]"])
                    ch_w "[Line]"

    elif Options[0] == "swallowed":
            #Wanda's response after swallowing the Player's cum.
            if "swallow" in WandaX.Chat:
                $ WandaX.FaceChange("sly",1)
                if not Player.Male:
                    ch_w "Слушай, можно мне еще немного твоих соков?"
                else:
                    ch_w "Слушай, можно мне еще немного твоей спермы?"
            else:
                $ WandaX.FaceChange("confused",1,Mouth="normal")
                if not Player.Male:
                    ch_w "Слушай, ты в курсе, что у твоих соков просто безумный вкус?"
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Они просто волшебные. . ."
                else:
                    ch_w "Слушай, ты в курсе, что у твоей спермы просто безумный вкус?"
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Она просто волшебная. . ."
                $ WandaX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Wanda's response after taking a facial from the Player.
            ch_w "Слушай, это прозвучит немного странно, но. . ."
            $ WandaX.FaceChange("sexy",2)
            if not Player.Male:
                ch_w "-Мне нравится чувствовать твои соки на своем лице."
            else:
                ch_w "-Мне нравится чувствовать твою сперму на своем лице."
            ch_w ". . ."
            ch_w "-просто захотелось сказать. . ."
            $ WandaX.Blush = 1

    elif Options[0] == "sleepover":
            #Wanda's response after sleeping with the Player.
            ch_w "Мне очень понравилась та ночь."
            ch_w "Приятно спать не одной. . ."

    elif Options[0] == "creampie":
            #Another of Wanda's responses after having sex with the Player.
            "[WandaX.Name] подходит к вам вплотную и шепчет на ухо:"
            if not Player.Male:
                ch_w "Иногда, когда я думаю о тебе, я чувствую. . . словно они опять стекают по моим бедрам."
            else:
                ch_w "Иногда, когда я думаю о тебе, я чувствую. . . словно она опять стекает по моим бедрам."

    elif Options[0] == "sexed":
            #A final response from Wanda after having sex with the Player.
            $ WandaX.FaceChange("sly",2,Eyes="side")
            ch_w ". . . слушай, когда я ласкаю себя. . ."
            $ WandaX.FaceChange("sexy",2)
            ch_w "-я всегда думаю о тебе. . ."
            $ WandaX.Blush = 1

    elif Options[0] == "anal":
            #Wanda's response after getting anal from the Player.
            $ WandaX.FaceChange("sly")
            ch_w "Честно говоря, я не так часто занималась. . . анальным сексом. . ."
            $ WandaX.FaceChange("sexy",1)
            ch_w ". . . но, думаю, что он мне очень нравится!"

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ WandaX.FaceChange("sly",1, Eyes="down")
            ch_w "Слушай, [WandaX.Petname]. . ."
            ch_w "Я весь день думала о твоем члене. . ."
            ch_w "О том, как он входит в меня. . ."
            $ WandaX.FaceChange("bemused",1)
            $ WandaX.Statup("Love", 50, 5)
            $ WandaX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            if not Player.Male:
                ch_w "Так вот, раз ты видела мои сиськи, мне интересно. . ."
                ch_w "Как они тебе?"
            else:
                ch_w "Так вот, раз ты видел мои сиськи, мне интересно. . ."
                ch_w "Как они тебе?"
            call Girl_First_TMenu
            $ WandaX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            if not Player.Male:
                ch_w "Так вот, раз ты видела мою киску, мне интересно. . ."
                ch_w "Как она тебе?"
            else:
                ch_w "Так вот, раз ты видел мою киску, мне интересно. . ."
                ch_w "Как она тебе?"
            call Girl_First_BMenu
            $ WandaX.History.remove("bottomless")

#    elif Options[0] == "boyfriend?":
#        call Wanda_BF
#    elif Options[0] == "lover?":
#        call Wanda_Love
#    elif Options[0] == "sir?":
#        call Wanda_Sub
#    elif Options[0] == "master?":
#        call Wanda_Master
#    elif Options[0] == "sexfriend?":
#        call Wanda_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Wanda_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Wanda_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Отойди от меня.",
                "Я не хочу тебя видеть.",
                "Убирайся.",
                "Отойди.",
                "Прочь!"])
        ch_w "[Line]"

    else: #all else fell through. . .
            if WandaX not in ActiveGirls:
                    $ D20 = 21
            else:
                    $ D20 = renpy.random.randint(1, 21)
            if D20 == 1:
                    $ WandaX.FaceChange("smile")
                    ch_w "Мне кажется, я начинаю привыкать к этому месту."
            elif D20 == 2:
                    $ WandaX.FaceChange("sly")
                    ch_w "Было немного сложно найти общий язык с преподами."
            elif D20 == 3:
                    $ WandaX.FaceChange("surprised")
                    ch_w "М? Прости, я отвлеклась. Задумалась о мультивселенной."
            elif D20 == 4:
                    $ WandaX.FaceChange("normal")
                    if not Player.Male:
                        ch_w "Слушай, [WandaX.Petname]. Ты встречалась с красным Халком в этой вселенной?"
                    else:
                        ch_w "Слушай, [WandaX.Petname]. Ты встречался с красным Халком в этой вселенной?"
            elif D20 == 5:
                    $ WandaX.FaceChange("smile")
                    ch_w "Здесь кормят намного лучше, чем в тюрьме."
            elif D20 == 6:
                    $ WandaX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_w "Слушай, [WandaX.Petname]. Ты не видела [JubesX.Name_vin]? Мы собирались по магазинам."
                    else:
                        ch_w "Слушай, [WandaX.Petname]. Ты не видел [JubesX.Name_vin]? Мы собирались по магазинам."
            elif D20 == 7:
                    $ WandaX.FaceChange("normal")
                    ch_w "Я недавно была в Комнате Опасности, пыталась сделать бой с Таносом более реалистичным."
            elif D20 == 8:
                    $ WandaX.FaceChange("sad")
                    ch_w "Трудно привыкнуть к тому, что я могу ходить куда хочу и когда захочу. . ."
            elif D20 == 9:
                    $ WandaX.FaceChange("smile",2)
                    ch_w "Нужно быть осторожнее, думаю, за мной следил Логан."
                    $ WandaX.FaceChange("smile",1)
            elif D20 == 10:
                    $ WandaX.FaceChange("smile")
                    ch_w "Мне нравится, что здесь я могу свободно пользоваться своими способностями."
                    ch_w "Каждый раз, когда я не могу что-то найти, \"вжух\" - и проблема решена."
            elif D20 == 11:
                    $ WandaX.FaceChange("smile")
                    ch_w "[JeanX.Name] иногда может по-настоящему вывести из себя."
                    ch_w "-но я могу ответить ей тем же."
            elif D20 == 12:
                    $ WandaX.FaceChange("sad")
                    ch_w "У меня проблемы с тестами. Я сильно отстаю. . ."
            elif D20 == 13:
                    $ WandaX.FaceChange("smile")
                    ch_w "Я как-то ходила в торговый центр вместе с [GwenX.Name_tvo], у нее. . . интересные вкусы."
            elif D20 == 14:
                    $ WandaX.FaceChange("sad")
                    ch_w "Мне нравятся учеба, но иногда приятно просто выйти на улицу и немного расслабиться."
            elif D20 == 15:
                    $ WandaX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_w "Ты ведь не смотрела репортажи со Мстителями, да?"
                    else:
                        ch_w "Ты ведь не смотрел репортажи со Мстителями, да?"
                    ch_w "Меня с ними-"
                    ch_w "-ничего не связывает."
            elif D20 == 16:
                    $ WandaX.FaceChange("sly")
                    if not Player.Male:
                        ch_w "Ты бывала в Нью Йорке? Однажды я устроила там погром."
                    else:
                        ch_w "Ты бывал в Нью Йорке? Однажды я устроила там погром."
            elif D20 == 17:
                    $ WandaX.FaceChange("perplexed")
                    ch_w "На днях я чуть не взорвала Профессора. . ."
                    ch_w "Мне нужно лучше контролировать себя. . ."
            elif D20 == 18:
                    $ WandaX.FaceChange("smile")
                    if not Player.Male:
                        ch_w "Ты видела, как мисс Фрост смотрит на тебя во время занятий?"
                    else:
                        ch_w "Ты видел, как мисс Фрост смотрит на тебя во время занятий?"
            elif D20 == 19:
                    $ WandaX.FaceChange("surprised")
                    ch_w "Берегись!"
                    $ WandaX.FaceChange("bemused",2)
                    ch_w "Я чуть не задела тебя, прости."
                    $ WandaX.FaceChange("sly,1")
            elif D20 == 20:
                    $ WandaX.FaceChange("smile")
                    ch_w "Здорово, когда есть кто-то, с кем я могу просто. . . поговорить, понимаешь?"
            else:
                    $ WandaX.FaceChange("smile")
                    ch_w "Привет, рада тебя видеть. . ."

    $ Line = 0
    return

# start Wanda_Names//////////////////////////////////////////////////////////
label Wanda_Names:    #rkeljsvgbdw
    menu:
        ch_w "Значит, ты хочешь, чтобы я звала тебя по-другому?"
        "Зови по инициалам." if Player.Name in WandaX.Petnames:
            $ WandaX.Petname = Player.Name[:1]  #fix test this
            $ WandaX.Petname_rod = Player.Name[:1]
            $ WandaX.Petname_dat = Player.Name[:1]
            $ WandaX.Petname_vin = Player.Name[:1]
            $ WandaX.Petname_tvo = Player.Name[:1]
            $ WandaX.Petname_pre = Player.Name[:1]
            ch_w "Конечно, [WandaX.Petname]."
        "Зови меня по имени.":
            $ WandaX.Petname = Player.Name
            $ WandaX.Petname_rod = Player.Name_rod
            $ WandaX.Petname_dat = Player.Name_dat
            $ WandaX.Petname_vin = Player.Name_vin
            $ WandaX.Petname_tvo = Player.Name_tvo
            $ WandaX.Petname_pre = Player.Name_pre
#            if Player.Name in WandaX.Petnames:
#                    $ WandaX.Petname = Player.Name
#            else:
#                    $ WandaX.Petname = WandaX.Petnames[0]
            ch_w "Конечно, [WandaX.Petname]."
        "Зови меня \"моя девушка\"." if "boyfriend" in WandaX.Petnames and not Player.Male:
            $ WandaX.Petname = "моя девушка"
            $ WandaX.Petname_rod = "моей девушки"
            $ WandaX.Petname_dat = "моей девушке"
            $ WandaX.Petname_vin = "мою девушку"
            $ WandaX.Petname_tvo = "моей девушкой"
            $ WandaX.Petname_pre = "моей девушке"
            ch_w "Хорошо, [WandaX.Petname]."
        "Зови меня \"мой парень\"." if "boyfriend" in WandaX.Petnames and Player.Male:
            $ WandaX.Petname = "мой парень"
            $ WandaX.Petname_rod = "моего парня"
            $ WandaX.Petname_dat = "моему парню"
            $ WandaX.Petname_vin = "моего парня"
            $ WandaX.Petname_tvo = "моим парнем"
            $ WandaX.Petname_pre = "моем парне"
            ch_w "Хорошо, [WandaX.Petname]."
        "Зови меня \"любимая\"." if "lover" in WandaX.Petnames and not Player.Male:
            $ WandaX.Petname = "любимая"
            $ WandaX.Petname_rod = "любимой"
            $ WandaX.Petname_dat = "любимой"
            $ WandaX.Petname_vin = "любимую"
            $ WandaX.Petname_tvo = "любимой"
            $ WandaX.Petname_pre = "любимой"
            ch_w "Ооох, ладно, [WandaX.Petname]."
        "Зови меня \"любимый\"." if "lover" in WandaX.Petnames and Player.Male:
            $ WandaX.Petname = "любимый"
            $ WandaX.Petname_rod = "любимого"
            $ WandaX.Petname_dat = "любимому"
            $ WandaX.Petname_vin = "любимого"
            $ WandaX.Petname_tvo = "любимым"
            $ WandaX.Petname_pre = "любимом"
            ch_w "Ооох, ладно, [WandaX.Petname]."
        "Зови меня \"госпожа\"." if "sir" in WandaX.Petnames and not Player.Male:
            $ WandaX.Petname = "госпожа"
            $ WandaX.Petname_rod = "госпожи"
            $ WandaX.Petname_dat = "госпоже"
            $ WandaX.Petname_vin = "госпожу"
            $ WandaX.Petname_tvo = "госпожой"
            $ WandaX.Petname_pre = "госпоже"
            ch_w "Конечно, [WandaX.Petname]."
        "Зови меня \"господин\"." if "sir" in WandaX.Petnames and Player.Male:
            $ WandaX.Petname = "господин"
            $ WandaX.Petname_rod = "господина"
            $ WandaX.Petname_dat = "господину"
            $ WandaX.Petname_vin = "господина"
            $ WandaX.Petname_tvo = "господином"
            $ WandaX.Petname_pre = "господине"
            ch_w "Конечно, [WandaX.Petname]."
        "Зови меня \"хозяйка\"." if "master" in WandaX.Petnames and not Player.Male:
            $ WandaX.Petname = "хозяйка"
            $ WandaX.Petname_rod = "хозяйки"
            $ WandaX.Petname_dat = "хозяйке"
            $ WandaX.Petname_vin = "хозяйку"
            $ WandaX.Petname_tvo = "хозяйкой"
            $ WandaX.Petname_pre = "хозяйке"
            ch_w "Хорошо, [WandaX.Petname]."
        "Зови меня \"хозяин\"." if "master" in WandaX.Petnames and Player.Male:
            $ WandaX.Petname = "хозяин"
            $ WandaX.Petname_rod = "хозяина"
            $ WandaX.Petname_dat = "хозяину"
            $ WandaX.Petname_vin = "хозяина"
            $ WandaX.Petname_tvo = "хозяином"
            $ WandaX.Petname_pre = "хозяине"
            ch_w "Хорошо, [WandaX.Petname]."
        "Зови меня \"любовница\"." if "sex friend" in WandaX.Petnames and not Player.Male:
            $ WandaX.Petname = "любовница"
            $ WandaX.Petname_rod = "любовницы"
            $ WandaX.Petname_dat = "любовнице"
            $ WandaX.Petname_vin = "любовницу"
            $ WandaX.Petname_tvo = "любовницей"
            $ WandaX.Petname_pre = "любовнице"
            ch_w "Хех, ладно, [WandaX.Petname]."
        "Зови меня \"любовник\"." if "sex friend" in WandaX.Petnames and Player.Male:
            $ WandaX.Petname = "любовник"
            $ WandaX.Petname_rod = "любовника"
            $ WandaX.Petname_dat = "любовнику"
            $ WandaX.Petname_vin = "любовника"
            $ WandaX.Petname_tvo = "любовником"
            $ WandaX.Petname_pre = "любовнике"
            ch_w "Хех, ладно, [WandaX.Petname]."
        "Зови меня \"секс-партнерша\"." if "fuck buddy" in WandaX.Petnames and not Player.Male:
            $ WandaX.Petname = "секс-партнерша"
            $ WandaX.Petname_rod = "секс-партнерши"
            $ WandaX.Petname_dat = "секс-партнерше"
            $ WandaX.Petname_vin = "секс-партнершу"
            $ WandaX.Petname_tvo = "секс-партнершей"
            $ WandaX.Petname_pre = "секс-партнерше"
            ch_w "Ох, это очень. . . ладно. . . [WandaX.Petname]."
        "Зови меня \"секс-партнер\"." if "fuck buddy" in WandaX.Petnames and Player.Male:
            $ WandaX.Petname = "секс-партнер"
            $ WandaX.Petname_rod = "секс-партнера"
            $ WandaX.Petname_dat = "секс-партнеру"
            $ WandaX.Petname_vin = "секс-партнера"
            $ WandaX.Petname_tvo = "секс-партнером"
            $ WandaX.Petname_pre = "секс-партнере"
            ch_w "Ох, это очень. . . ладно. . . [WandaX.Petname]."
        "Зови меня \"мамочка\"." if "daddy" in WandaX.Petnames and not Player.Male:
            $ WandaX.Petname = "мамочка"
            $ WandaX.Petname_rod = "мамочки"
            $ WandaX.Petname_dat = "мамочке"
            $ WandaX.Petname_vin = "мамочку"
            $ WandaX.Petname_tvo = "мамочкой"
            $ WandaX.Petname_pre = "мамочке"
            ch_w "О! Конечно, [WandaX.Petname]."
        "Зови меня \"папочка\"." if "daddy" in WandaX.Petnames and Player.Male:
            $ WandaX.Petname = "папочка"
            $ WandaX.Petname_rod = "папочки"
            $ WandaX.Petname_dat = "папочке"
            $ WandaX.Petname_vin = "папочку"
            $ WandaX.Petname_tvo = "папочкой"
            $ WandaX.Petname_pre = "папочке"
            ch_w "О! Конечно, [WandaX.Petname]."
        "Зови меня \"Вижн\"." if "Vision" in WandaX.Petnames:
            $ WandaX.Petname = "Вижн"
            $ WandaX.Petname_rod = "Вижн"
            $ WandaX.Petname_dat = "Вижн"
            $ WandaX.Petname_vin = "Вижн"
            $ WandaX.Petname_tvo = "Вижн"
            $ WandaX.Petname_pre = "Вижн"
            ch_w "Конечно, [WandaX.Petname]."
        "Зови меня \"сис\"." if not Player.Male:
            $ WandaX.Petname = "сис"
            $ WandaX.Petname_rod = "сис"
            $ WandaX.Petname_dat = "сис"
            $ WandaX.Petname_vin = "сис"
            $ WandaX.Petname_tvo = "сис"
            $ WandaX.Petname_pre = "сис"
            ch_w "Ладно, сис."
        "Зови меня \"бро\"." if Player.Male:
            $ WandaX.Petname = "бро"
            $ WandaX.Petname_rod = "бро"
            $ WandaX.Petname_dat = "бро"
            $ WandaX.Petname_vin = "бро"
            $ WandaX.Petname_tvo = "бро"
            $ WandaX.Petname_pre = "бро"
        "Неважно.":
            return
    return
# end Wanda_Names//////////////////////////////////////////////////////////

label Wanda_Pet: #rkeljsvgbdw
    while 1:
        menu:
            extend ""
            "Обходительно":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "Ванда.":
                        $ WandaX.Pet = "Ванда"
                        $ WandaX.Pet_rod = "Ванды"
                        $ WandaX.Pet_dat = "Ванде"
                        $ WandaX.Pet_vin = "Ванду"
                        $ WandaX.Pet_tvo = "Вандой"
                        $ WandaX.Pet_pre = "Ванде"
                        ch_w "Ладно."

                    "Алая Ведьма." if "Scarlet Witch" in WandaX.Names:
                        if ApprovalCheck(WandaX, 700, "L") and not ApprovalCheck(WandaX, 500, "O"):
                                $ WandaX.Pet = "Алая Ведьма"
                                $ WandaX.Pet_rod = "Алой Ведьмы"
                                $ WandaX.Pet_dat = "Алой Ведьме"
                                $ WandaX.Pet_vin = "Алую Ведьму"
                                $ WandaX.Pet_tvo = "Алой Ведьмой"
                                $ WandaX.Pet_pre = "Алой Ведьме"
                                ch_w "Ладно."
                        else:
                                ch_w "Звучит довольно странно, [WandaX.Petname]."

                    "\"моя девушка\".":
                        if "boyfriend" in WandaX.Petnames:
                            $ WandaX.Pet = "моя девушка"
                            $ WandaX.Pet_rod = "моей девушки"
                            $ WandaX.Pet_dat = "моей девушке"
                            $ WandaX.Pet_vin = "мою девушку"
                            $ WandaX.Pet_tvo = "моей девушкой"
                            $ WandaX.Pet_pre = "моей девушке"
                            $ WandaX.FaceChange("sexy", 1)
                            ch_w "Конечно, я же в самом деле твоя девушка [WandaX.Petname]."
                        else:
                            $ WandaX.FaceChange("angry")
                            ch_w "Мне не особо нравится, [WandaX.Petname]."

                    "\"детка\".":
                        if "boyfriend" in WandaX.Petnames or ApprovalCheck(WandaX, 700, "L"):
                            $ WandaX.Pet = "детка"
                            $ WandaX.Pet_rod = "детки"
                            $ WandaX.Pet_dat = "детке"
                            $ WandaX.Pet_vin = "детку"
                            $ WandaX.Pet_tvo = "деткой"
                            $ WandaX.Pet_pre = "детке"
                            $ WandaX.FaceChange("sexy", 1)
                            ch_w "\"Детка,\" прикольно!"
                        else:
                            $ WandaX.FaceChange("angry")
                            ch_w "Мне не особо нравится, [WandaX.Petname]."

                    "\"крошка\".":
                        if "boyfriend" in WandaX.Petnames or ApprovalCheck(WandaX, 600, "L"):
                            $ WandaX.Pet = "крошка"
                            $ WandaX.Pet_rod = "крошки"
                            $ WandaX.Pet_dat = "крошке"
                            $ WandaX.Pet_vin = "крошку"
                            $ WandaX.Pet_tvo = "крошкой"
                            $ WandaX.Pet_pre = "крошке"
                            $ WandaX.FaceChange("sexy", 1)
                            ch_w "\"Крошка,\" хех!"
                        else:
                            $ WandaX.FaceChange("angry")
                            ch_w "Мне не особо нравится, [WandaX.Petname]."

                    "\"малышка\".":
                        if "boyfriend" in WandaX.Petnames or ApprovalCheck(WandaX, 500, "L"):
                            $ WandaX.Pet = "малышка"
                            $ WandaX.Pet_rod = "малышки"
                            $ WandaX.Pet_dat = "малышке"
                            $ WandaX.Pet_vin = "малышку"
                            $ WandaX.Pet_tvo = "малышкой"
                            $ WandaX.Pet_pre = "малышке"
                            $ WandaX.FaceChange("sexy", 1)
                            ch_w "Я тебя обожаю, [WandaX.Petname]."
                        else:
                            $ WandaX.FaceChange("angry")
                            ch_w "Мне не особо нравится, [WandaX.Petname]."


                    "\"дорогая\".":
                        if "boyfriend" in WandaX.Petnames or ApprovalCheck(WandaX, 600, "L"):
                            $ WandaX.Pet = "дорогая"
                            $ WandaX.Pet_rod = "дорогой"
                            $ WandaX.Pet_dat = "дорогой"
                            $ WandaX.Pet_vin = "дорогую"
                            $ WandaX.Pet_tvo = "дорогой"
                            $ WandaX.Pet_pre = "дорогой"
                            ch_w "Мило, [WandaX.Petname]."
                        else:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Мне не особо нравится, [WandaX.Petname]."

                    "\"секси\".":
                        if "lover" in WandaX.Petnames or ApprovalCheck(WandaX, 800):
                            $ WandaX.Pet = "секси"
                            $ WandaX.Pet_rod = "секси"
                            $ WandaX.Pet_dat = "секси"
                            $ WandaX.Pet_vin = "секси"
                            $ WandaX.Pet_tvo = "секси"
                            $ WandaX.Pet_pre = "секси"
                            $ WandaX.FaceChange("sexy", 1)
                            ch_w "Хех. . ."
                        else:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Мне не особо нравится, [WandaX.Petname]."

                    "\"любимая\".":
                        if "lover" in WandaX.Petnames or ApprovalCheck(WandaX, 1200):
                            $ WandaX.Pet = "любимая"
                            $ WandaX.Pet_rod = "любимой"
                            $ WandaX.Pet_dat = "любимой"
                            $ WandaX.Pet_vin = "любимую"
                            $ WandaX.Pet_tvo = "любимой"
                            $ WandaX.Pet_pre = "любимой"
                            $ WandaX.FaceChange("sexy", 1)
                            ch_w "Конечно."
                        else:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Я так не думаю, [WandaX.Petname]."

                    "Назад":
                        pass

            "Грубо":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "\"рабыня\".":
                        if "master" in WandaX.Petnames or ApprovalCheck(WandaX, 800, "O"):
                            $ WandaX.Pet = "рабыня"
                            $ WandaX.Pet_rod = "рабыни"
                            $ WandaX.Pet_dat = "рабыне"
                            $ WandaX.Pet_vin = "рабыню"
                            $ WandaX.Pet_tvo = "рабыней"
                            $ WandaX.Pet_pre = "рабыне"
                            $ WandaX.FaceChange("bemused", 1)
                            ch_w "Хорошо, [WandaX.Petname]."
                        else:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Я не рабыня, [WandaX.Petname]."

                    "\"питомец\".":
                        if "master" in WandaX.Petnames or ApprovalCheck(WandaX, 650, "O"):
                            $ WandaX.Pet = "питомец"
                            $ WandaX.Pet_rod = "питомце"
                            $ WandaX.Pet_dat = "питомцу"
                            $ WandaX.Pet_vin = "питомца"
                            $ WandaX.Pet_tvo = "питомцем"
                            $ WandaX.Pet_pre = "питомце"
                            $ WandaX.FaceChange("bemused", 1)
                            ch_w "Как хочешь, [WandaX.Petname]."
                        else:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Я не питомец, [WandaX.Petname]."

                    "\"шлюха\".":
                        if "sex friend" in WandaX.Petnames or ApprovalCheck(WandaX, 900, "OI"):
                            $ WandaX.Pet = "шлюха"
                            $ WandaX.Pet_rod = "шлюхи"
                            $ WandaX.Pet_dat = "шлюхе"
                            $ WandaX.Pet_vin = "шлюху"
                            $ WandaX.Pet_tvo = "шлюхой"
                            $ WandaX.Pet_pre = "шлюхе"
                            $ WandaX.FaceChange("sexy")
                            ch_w "Пожалуй. . . это правда. . ."
                        else:
                            $ WandaX.FaceChange("angry", 1)
                            $ WandaX.Mouth = "surprised"
                            ch_w "Мне не нравится, [WandaX.Petname]."

                    "\"блядь\".":
                        if "fuckbuddy" in WandaX.Petnames or ApprovalCheck(WandaX, 1000, "OI"):
                            $ WandaX.Pet = "блядь"
                            $ WandaX.Pet_rod = "бляди"
                            $ WandaX.Pet_dat = "бляде"
                            $ WandaX.Pet_vin = "блядь"
                            $ WandaX.Pet_tvo = "блядью"
                            $ WandaX.Pet_pre = "бляде"
                            $ WandaX.FaceChange("sly")
                            ch_w ". . . это довольно грубо, но ладно. . ."
                        else:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Это -очень- грубо, [WandaX.Petname]."

                    "\"сладкогрудая\".":
                        if "sex friend" in WandaX.Petnames or ApprovalCheck(WandaX, 1400):
                            $ WandaX.Pet = "сладкогрудая"
                            $ WandaX.Pet_rod = "сладкогрудой"
                            $ WandaX.Pet_dat = "сладкогрудой"
                            $ WandaX.Pet_vin = "сладкогрудую"
                            $ WandaX.Pet_tvo = "сладкогрудой"
                            $ WandaX.Pet_pre = "сладкогрудой"
                            $ WandaX.FaceChange("sly", 1)
                            ch_w "М? Ладно. . ."
                        else:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Мне не нравится, [WandaX.Petname]."

                    "\"любовница\".":
                        if "sex friend" in WandaX.Petnames or ApprovalCheck(WandaX, 600, "I"):
                            $ WandaX.Pet = "любовница"
                            $ WandaX.Pet_rod = "любовницы"
                            $ WandaX.Pet_dat = "любовнице"
                            $ WandaX.Pet_vin = "любовницу"
                            $ WandaX.Pet_tvo = "любовницей"
                            $ WandaX.Pet_pre = "любовнице"
                            $ WandaX.FaceChange("sly")
                            ch_w "Да?"
                        else:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Мне не нравится, [WandaX.Petname]."

                    "\"секс-партнерша\".":
                        if "fuckbuddy" in WandaX.Petnames or ApprovalCheck(WandaX, 700, "I"):
                            $ WandaX.Pet = "секс-партнерша"
                            $ WandaX.Pet_rod = "секс-партнерши"
                            $ WandaX.Pet_dat = "секс-партнерше"
                            $ WandaX.Pet_vin = "секс-партнершу"
                            $ WandaX.Pet_tvo = "секс-партнершей"
                            $ WandaX.Pet_pre = "секс-партнерше"
                            $ WandaX.FaceChange("sly")
                            ch_w "Да?"
                        else:
                            $ WandaX.FaceChange("angry", 1)
                            $ WandaX.Mouth = "surprised"
                            ch_w "Мне не нравится, [WandaX.Petname]."

                    "\"доченька\".":
                        if "daddy" in WandaX.Petnames or ApprovalCheck(WandaX, 1200):
                            $ WandaX.Pet = "доченька"
                            $ WandaX.Pet_rod = "доченьки"
                            $ WandaX.Pet_dat = "доченьке"
                            $ WandaX.Pet_vin = "доченьку"
                            $ WandaX.Pet_tvo = "доченькой"
                            $ WandaX.Pet_pre = "доченьке"
                            $ WandaX.FaceChange("smile", 1)
                            ch_w "Это просто очаровательно."
                        else:
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Это очень странно."

                    "Назад":
                        pass

            "Неважно.":
                return
    return

#label Wanda_Namecheck(WandaX.Pet = WandaX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname


# start Wanda_Rename//////////////////////////////////////////////////////////
label Wanda_Rename:  #rkeljsvgbdw
        #Sets alternate names from Wanda
        $ WandaX.Mouth = "smile"
        ch_w "Да?"
        menu:
            extend ""
            "Думаю, \"Ванда\" красивое имя." if WandaX.Name != "Ванда":
                            $ WandaX.Name = "Ванда"
                            $ WandaX.Name_rod = "Ванды"
                            $ WandaX.Name_dat = "Ванде"
                            $ WandaX.Name_vin = "Ванду"
                            $ WandaX.Name_tvo = "Вандой"
                            $ WandaX.Name_pre = "Ванде"
                            ch_w "Спасибо."
            "Думаю, \"Алая Ведьма\" звучит круто." if WandaX.Name != "Алая Ведьма" and "Scarlet Witch" in WandaX.Names:
                    if not ApprovalCheck(WandaX, 500):
                            $ WandaX.FaceChange("confused", 1)
                            ch_w "Я предпочитаю, чтобы меня звали \"[WandaX.Name_tvo]\"."
                    else:
                            if "namechange" not in WandaX.DailyActions:
                                    $ WandaX.Statup("Love", 70, 2)
                                    $ WandaX.Statup("Obed", 70, 5)
                            $ WandaX.Name = "Алая Ведьма"
                            $ WandaX.Name_rod = "Алой Ведьмы"
                            $ WandaX.Name_dat = "Алой Ведьме"
                            $ WandaX.Name_vin = "Алую Ведьму"
                            $ WandaX.Name_tvo = "Алой Ведьмой"
                            $ WandaX.Name_pre = "Алой Ведьме"
                            $ WandaX.FaceChange("sly", 1)
                            ch_w "Ладно, если тебе так этого хочется. . ."
            "Неважно.":
                    pass
        $ WandaX.AddWord(1,0,"namechange")
        return
# end Wanda_Rename//////////////////////////////////////////////////////////


# start Wanda_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Wanda_Personality(Cnt = 0):   #rkeljsvgbdw
    if not WandaX.Chat[4] or Cnt:
        "Поскольку у вас все хорошо получается в одной области, вы можете убедить Эмму сосредоточиться на любой другой."
        "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
        "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
    menu:
        ch_w "Да?"
        "Больше Послушания. [[Любовь в Послушание]" if WandaX.Love > 900:
            ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
            ch_w "Ты хочешь, чтобы я была более послушной? Я попробую."
            $ WandaX.Chat[4] = 1
        "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if WandaX.Love > 900:
            ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
            ch_w "Ты хочешь, чтобы я была более послушной? Я попробую."
            $ WandaX.Chat[4] = 2

        "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if WandaX.Obed > 900:
            ch_p "Я хочу, чтобы ты была более раскрепощенной."
            ch_w "Ты хочешь, чтобы я была более раскрепощенной? Я попробую."
            $ WandaX.Chat[4] = 3
        "Больше Любви. [[Повиновение в Любовь]" if WandaX.Obed > 900:
            ch_p "Я хочу, чтобы ты училась любить меня."
            ch_w "Ты думаешь, что я не достаточно заботливая? Ладно, я попробую."
            $ WandaX.Chat[4] = 4

        "Больше Повиновения. [[Раскрепощенность в Повиновение]" if WandaX.Inbt > 900:
            ch_p "Я знаю, что нам и так весело, но разве ты не можешь иногда слушаться меня?"
            ch_w "Ты хочешь, чтобы я была более послушной? Это может быть весело."
            $ WandaX.Chat[4] = 5

        "Больше Любви. [[Раскрепощенность в Любовь]" if WandaX.Inbt > 900:
            ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
            ch_w "Ты думаешь, что я не достаточно заботливая? Ладно, я попробую."
            $ WandaX.Chat[4] = 6

        "Просто делай то, что тебе нравится. . .[[Сбросить]" if WandaX.Chat[4]:
            ch_p "Помнишь, что мы обсуждали? Забудь."
            ch_w "А. . . ладно?"
            $ WandaX.Chat[4] = 0
        "Повторить правила":
            call Wanda_Personality(1)
            return
        "Неважно.":
            return
    return
# end Wanda_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Wanda_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Wanda_Summon(Tempmod=Tempmod): #rkeljsvgbdw
    $ WandaX.OutfitChange()
    if "no summon" in WandaX.RecentActions:
                if "no summon" in WandaX.RecentActions:
                    ch_w "Перестань спрашивать!"
                    $ WandaX.AddWord(1,"angry",0,0,0)
                elif Current_Time == "Night":
                    ch_w "Я же сказала тебе, уже поздно."
                else:
                    ch_w "Я же сказала тебе, я занята."
                $ WandaX.RecentActions.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if WandaX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif WandaX.Loc == "bg dangerroom":
        $ Tempmod = -10
    elif WandaX.Loc == "bg showerroom":
        $ Tempmod = -30

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"
    if Time_Count >= 3: #night time
                if ApprovalCheck(WandaX, 500, "L") or ApprovalCheck(WandaX, 400, "O"):
                        #It's night time but she likes you.
                        ch_w "Конечно, я могу прийти к тебе."
                        $ WandaX.Loc = bg_current
                        call Taboo_Level
                        call Set_The_Scene
                else:
                        #It's night time and she isn't into you
                        ch_w "Прости, уже поздно."
                        $ WandaX.RecentActions.append("no summon")
                return
    elif "les" in WandaX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(WandaX, 2000):
                    ch_w "Я сейчас не одна, но ты можешь присоединиться к нам. . ."
                    menu:
                        extend ""
                        "Конечно":
                            $ Line = "go to"
                        "Нет, спасибо.":
                            ch_w "Как знаешь. . ."
                            return
            else:
                    ch_w "Ох, эм, я сейчас не одна."
                    ch_w "Возможно, если позже. . ."
                    $ WandaX.RecentActions.append("no summon")
                    return
    elif not ApprovalCheck(WandaX, 700, "L") or not ApprovalCheck(WandaX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(WandaX, 300):
                ch_w "Прости, я немного занята, [WandaX.Petname]."
                $ WandaX.RecentActions.append("no summon")
                return


        if "summoned" in WandaX.RecentActions:
                pass
        elif "goto" in WandaX.RecentActions:
                if not Player.Male:
                    ch_w "Но ты только что ушла. . ."
                else:
                    ch_w "Но ты только что ушел. . ."
        elif WandaX.Loc == "bg classroom":
                ch_w "Я в аудитории, хочешь прийти?"
        elif WandaX.Loc == "bg dangerroom":
                ch_w "Я в Комнате Опасности, [WandaX.Petname], хочешь присоединиться ко мне?"
        elif WandaX.Loc == "bg campus":
                ch_w "Я отдыхаю во дворе, хочешь присоединиться ко мне?"
        elif WandaX.Loc == "bg wanda":
                ch_w "Я в своей комнате, [WandaX.Petname], хочешь присоединиться ко мне?"
        elif WandaX.Loc == "bg player":
                ch_w "Я в твоей комнате, [WandaX.Petname], хочешь присоединиться ко мне?"
        elif WandaX.Loc == "bg showerroom":
            if ApprovalCheck(WandaX, 1600):
                ch_w "Я сейчас в душе. Хочешь присоединиться ко мне?"
            else:
                ch_w "Я сейчас в душе, [WandaX.Petname],  увидимся позже."
                $ WandaX.RecentActions.append("no summon")
                return
        elif WandaX.Loc == "hold":
                ch_w "Прости, я сейчас немного занята."
                $ WandaX.RecentActions.append("no summon")
                return
        else:
                ch_w "Ты всегда можешь прийти ко мне. . ."


        if "summoned" in WandaX.RecentActions:
            ch_w "Снова? Ну хорошо?"
            $ Line = "yes"
        elif "goto" in WandaX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
#                                ch_w "See you then."
                                $ Line = "go to"
                "Нет.":
                                ch_w "Как хочешь."
                "Мне бы -очень- хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(WandaX, 600, "L") or ApprovalCheck(WandaX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(WandaX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(WandaX, 1400):
                                #she is generally favorable
                                ch_w "Хорошо."
                                $ Line = "yes"
                        elif ApprovalCheck(WandaX, 200, "O"):
                                #she is not obedient
                                ch_w "Оу."
                                ch_w "Ну, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(WandaX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(WandaX, 1400):
                                #she is generally favorable
                                ch_w "Хорошо."
                                $ Line = "yes"
                        elif ApprovalCheck(WandaX, 200, "O"):
                                #she is not obedient
                                ch_w "Оу."
                                ch_w "Ну, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Конечно, сейчас приду.":
                    $ WandaX.Statup("Love", 55, 1)
                    $ WandaX.Statup("Inbt", 30, 1)
#                    ch_w "See you then."
                    $ Line = "go to"

                "Нет, поговорим позже.":
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.Statup("Obed", 30, 2)
                    ch_w "Oh, ok then."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                    if ApprovalCheck(WandaX, 650, "L") or ApprovalCheck(WandaX, 1500):
                        $ WandaX.Statup("Love", 70, 1)
                        $ WandaX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ WandaX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                        ch_w "Ого, ладно."

                "Приходи ко мне, будет весело.":
                    if ApprovalCheck(WandaX, 400, "L") and ApprovalCheck(WandaX, 800):
                        $ WandaX.Statup("Love", 70, 1)
                        $ WandaX.Statup("Obed", 50, 1)
                        $ Line = "fun"
                    else:
                        $ WandaX.Statup("Inbt", 30, 1)
                        $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                    if ApprovalCheck(WandaX, 600, "O"):
                        #she is obedient
                        $ WandaX.Statup("Love", 50, 1, 1)
                        $ WandaX.Statup("Love", 40, -1)
                        $ WandaX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(WandaX, 1500):
                        #she is generally favorable
                        $ WandaX.Statup("Love", 70, -2)
                        $ WandaX.Statup("Love", 90, -1)
                        $ WandaX.Statup("Obed", 50, 2)
                        $ WandaX.Statup("Obed", 90, 1)
                        ch_w "Ох, ладно."
                        $ Line = "yes"

                    elif ApprovalCheck(WandaX, 200, "O"):
                        #she is not obedient
                        $ WandaX.Statup("Love", 60, -4)
                        $ WandaX.Statup("Love", 90, -3)
                        ch_w "Что?"
                        $ WandaX.Statup("Inbt", 40, 2)
                        $ WandaX.Statup("Inbt", 60, 1)
                        $ WandaX.Statup("Obed", 70, -3)
                        ch_w "Я не собираюсь прислушиваться к этому бреду."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ WandaX.Statup("Inbt", 30, 1)
                        $ WandaX.Statup("Inbt", 50, 1)
                        $ WandaX.Statup("Love", 50, -1, 1)
                        $ WandaX.Statup("Obed", 70, -1)
                        $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                    if ApprovalCheck(WandaX, 600, "O"):
                        #she is obedient
                        $ WandaX.Statup("Love", 50, 1, 1)
                        $ WandaX.Statup("Love", 40, -1)
                        $ WandaX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(WandaX, 1500):
                        #she is generally favorable
                        $ WandaX.Statup("Love", 70, -2)
                        $ WandaX.Statup("Love", 90, -1)
                        $ WandaX.Statup("Obed", 50, 2)
                        $ WandaX.Statup("Obed", 90, 1)
                        ch_w "Ох, ладно."
                        $ Line = "yes"

                    elif ApprovalCheck(WandaX, 200, "O"):
                        #she is not obedient
                        $ WandaX.Statup("Love", 60, -4)
                        $ WandaX.Statup("Love", 90, -3)
                        ch_w "Что?"
                        $ WandaX.Statup("Inbt", 40, 2)
                        $ WandaX.Statup("Inbt", 60, 1)
                        $ WandaX.Statup("Obed", 70, -3)
                        ch_w "Я не собираюсь прислушиваться к этому бреду."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ WandaX.Statup("Inbt", 30, 1)
                        $ WandaX.Statup("Inbt", 50, 1)
                        $ WandaX.Statup("Love", 50, -1, 1)
                        $ WandaX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if WandaX.Love > WandaX.Obed:
            ch_w "Конечно."
        else:
            ch_w "Конечно, уже иду."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ WandaX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            if WandaX.Loc == "bg classroom":
                ch_w "Мне нужно наверстать упущенное."
            elif WandaX.Loc == "bg dangerroom":
                ch_w "Я только разогрелась!"
            else:
                ch_w "Прости, [WandaX.Petname], я очень занята."
            $ WandaX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ WandaX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            $ Nearby = []
            $ Line = 0
            $ Party = [WandaX]

            if WandaX.Loc == "bg classroom":
                    ch_w "Ладно, ты знаешь, где меня найти."
                    jump Class_Room
            elif WandaX.Loc == "bg dangerroom":
                    ch_w "Я пока немного разогреюсь."
                    jump Danger_Room
            elif WandaX.Loc == "bg wanda":
                    ch_w "Я. . . пока наведу чистоту."
                    jump Wanda_Room
            elif WandaX.Loc == "bg player":
                    ch_w "Увидимся, когда придешь."
                    jump Player_Room
            elif WandaX.Loc == "bg showerroom":
                    ch_w "Я пока намылюсь."
                    jump Shower_Room
            elif WandaX.Loc == "bg campus":
                    ch_w "Скоро увидимся."
                    jump Campus
            elif WandaX.Loc != "hold":
                    ch_w "Конечно, увидимся."
                    $ bg_current = WandaX.Loc
                    jump Misplaced
            else:
                    ch_w "Я просто встречу тебя в своей комнате."
                    $ WandaX.Loc = "bg wanda"
                    jump Wanda_Room

    #She's agreed to come over
    elif Line == "lonely":
            if not Player.Male:
                ch_w "Не могу оставить тебя одну ни на минуту. . ."
            else:
                ch_w "Не могу оставить тебя одного ни на минуту. . ."
    elif Line == "command":
            ch_w "Ладно, [WandaX.Petname]."
    elif Line == "fun":
            ch_w "Конечно."

    $ WandaX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(WandaX)
            return
    $ WandaX.Loc = bg_current
    call Taboo_Level(0)
    $ WandaX.OutfitChange()
    call Set_The_Scene
    return

# End Wanda Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Wanda_Leave(Tempmod=Tempmod, GirlsNum = 0):    #rkeljsvgbdw
    if "leaving" in WandaX.RecentActions:
        $ WandaX.DrainWord("leaving")
    else:
        return

    if WandaX.Loc == "hold":
            # Activates if she's being moved out of play
            ch_w "Мне нужно отлучиться, увидимся."
            return

    if WandaX in Party or "lockedtravels" in WandaX.Traits:
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ WandaX.Loc = bg_current
            return

    elif "freetravels" in WandaX.Traits or not ApprovalCheck(WandaX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.
            $ WandaX.OutfitChange()
            if GirlsNum: #if someone left before her
                        ch_w "Конечно, я тоже пойду."

            if WandaX.Loc == "bg classroom":
                        ch_w "У меня занятия."
            elif WandaX.Loc == "bg dangerroom":
                        ch_w "Я собираюсь насладиться Комнатой Опасности."
            elif WandaX.Loc == "bg campus":
                        ch_w "Я собираюсь погулять во дворе."
            elif WandaX.Loc == "bg wanda":
                        ch_w "Я возвращаюсь в свою комнату."
            elif WandaX.Loc == "bg player":
                        ch_w "Я немного побуду в твоей комнате."
            elif WandaX.Loc == "bg pool":
                        ch_w "Я иду к бассейну."
            elif WandaX.Loc == "bg showerroom":
                if ApprovalCheck(WandaX, 1400):
                        ch_w "Я собираюсь принять душ."
                else:
                        ch_w "Увидимся."
            else:
                        ch_w "До встречи."
            hide Wanda_Sprite
            hide Wanda_Seated
            return
            #End Free Travels

    if bg_current == "bg dangerroom":
            call Gym_Exit([WandaX])

    $ WandaX.OutfitChange()

    if "follow" not in WandaX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ WandaX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    # Sets her preferences
    if WandaX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif WandaX.Loc == "bg dangerroom":
        $ Tempmod = 20
    elif WandaX.Loc == "bg showerroom":
        $ Tempmod = 40


    if GirlsNum: #if someone left before her
            ch_w "Ага, я тоже пойду."

    if WandaX.Loc == "bg classroom":
            ch_w "Я иду на занятия, хочешь составить мне компанию?"
    elif WandaX.Loc == "bg dangerroom":
            ch_w "Я иду в Комнату Опасности, [WandaX.Petname], не хочешь присоединиться ко мне?"
    elif WandaX.Loc == "bg campus":
            ch_w "Я собираюсь погулять во дворе. Хочешь присоединиться ко мне?"
    elif WandaX.Loc == "bg wanda":
            ch_w "Я направляюсь в свою комнату, [WandaX.Petname], хочешь присоединиться ко мне?"
    elif WandaX.Loc == "bg player":
            ch_w "Я направляюсь в твою комнату, [WandaX.Petname], хочешь присоединиться ко мне?"
    elif WandaX.Loc == "bg showerroom":
        if ApprovalCheck(WandaX, 1600):
            ch_w "Я собираюсь принять душ. Хочешь присоединиться ко мне?"
        else:
            ch_w "Я собираюсь принять душ, [WandaX.Petname], увидимся позже."
            return
    elif WandaX.Loc == "bg pool":
            ch_w "Я направляюсь к бассейну. Хочешь присоединиться ко мне?"
    elif WandaX.Loc == "bg mall":
            ch_w "Я направляюсь в торговый центр. Хочешь присоединиться ко мне?"
    else:
            ch_w "Хочешь присоединиться ко мне?"


    menu:
        extend ""
        "Конечно, я сразу за тобой.":
                if "followed" not in WandaX.RecentActions:
                    $ WandaX.Statup("Love", 55, 1)
                    $ WandaX.Statup("Inbt", 30, 1)
                $ Line = "go to"

        "Нет, поговорим позже.":
                if "followed" not in WandaX.RecentActions:
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.Statup("Obed", 30, 2)
                ch_w "Ох, ладно."

        "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                if ApprovalCheck(WandaX, 650, "L") or ApprovalCheck(WandaX, 1500):
                    if "followed" not in WandaX.RecentActions:
                        $ WandaX.Statup("Love", 70, 1)
                        $ WandaX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else:
                    if "followed" not in WandaX.RecentActions:
                        $ WandaX.Statup("Inbt", 30, 1)
                    $ Line = "no"
                    ch_w "Ого."

        "Останься, будет весело.":
                if ApprovalCheck(WandaX, 400, "L") and ApprovalCheck(WandaX, 800):
                    $ WandaX.Statup("Love", 70, 1)
                    $ WandaX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else:
                    $ WandaX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Нет, останься здесь.":
                if ApprovalCheck(WandaX, 600, "O"):
                    #she is obedient
                    if "followed" not in WandaX.RecentActions:
                        $ WandaX.Statup("Love", 40, -2)
                        $ WandaX.Statup("Obed", 90, 1)
                    $ Line = "command"

                elif D20 >= 7 and ApprovalCheck(WandaX, 1400):
                    #she is generally favorable
                    if "followed" not in WandaX.RecentActions:
                        $ WandaX.Statup("Love", 70, -2)
                        $ WandaX.Statup("Love", 90, -1)
                        $ WandaX.Statup("Obed", 50, 2)
                        $ WandaX.Statup("Obed", 90, 1)
                    ch_w "Хорошо, я могу остаться ненадолго."
                    $ Line = "yes"

                elif ApprovalCheck(WandaX, 200, "O"):
                    #she is not obedient
                    if "followed" not in WandaX.RecentActions:
                        $ WandaX.Statup("Love", 70, -4)
                        $ WandaX.Statup("Love", 90, -2)
                    ch_w "Что?"
                    if "followed" not in WandaX.RecentActions:
                        $ WandaX.Statup("Inbt", 40, 2)
                        $ WandaX.Statup("Inbt", 60, 1)
                        $ WandaX.Statup("Obed", 70, -2)
                    ch_w "Я не останусь."
                else:
                    #she is obedient, but you failed to meet the checks
                    if "followed" not in WandaX.RecentActions:
                        $ WandaX.Statup("Inbt", 30, 1)
                        $ WandaX.Statup("Inbt", 50, 1)
                        $ WandaX.Statup("Love", 50, -1, 1)
                        $ WandaX.Statup("Love", 90, -2)
                        $ WandaX.Statup("Obed", 70, -1)
                    $ Line = "no"
                #End ordered to stay

    call Taboo_Level(0)
    $ WandaX.RecentActions.append("followed")
    if not Line:
            #You end the dialog neutrally
            hide Wanda_Sprite
            hide Wanda_Seated
            call Gym_Clothes_Off([WandaX])
            return

    if Line == "no":
            # She's refused, context based dialog
            if WandaX.Loc == "bg classroom":
                ch_w "Мне нужно многое здесь наверстать."
            elif WandaX.Loc == "bg dangerroom":
                ch_w "Прости, [WandaX.Petname], но мне очень нужно потренироваться."
            else:
                ch_w "Прости, но у меня много дел."
            hide Wanda_Sprite
            hide Wanda_Seated
            call Gym_Clothes_Off([WandaX])
            return

    elif Line == "go to":
            #You agreed to go to her instead
            #$ Party.append(WandaX)
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")
            $ WandaX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            hide Wanda_Sprite
            hide Wanda_Seated
            $ Nearby = []
            $ Party = [WandaX]
            call Gym_Clothes_Off([WandaX])
            if WandaX.Loc == "bg classroom":
                ch_w "Ладно, я займу тебе место."
                jump Class_Room_Entry
            elif WandaX.Loc == "bg dangerroom":
                ch_w "Тогда я пока разогреюсь."
                jump Danger_Room_Entry
            elif WandaX.Loc == "bg wanda":
                ch_w "Ладно."
                jump Wanda_Room
            elif WandaX.Loc == "bg player":
                ch_w "Ладно."
                jump Player_Room
            elif WandaX.Loc == "bg showerroom":
                ch_w "Ладно."
                jump Shower_Room_Entry
            elif WandaX.Loc == "bg campus":
                ch_w "Ладно."
                jump Campus_Entry
            elif WandaX.Loc == "bg pool":
                ch_w "Ладно."
                jump Pool_Entry
            elif WandaX.Loc == "bg mall":
                ch_w "Ладно."
                jump Mall_Entry
            else:
                ch_w "Тогда я просто встречусь с тобой в твоей комнате."
                $ WandaX.Loc = "bg player"
                jump Player_Room
            #End "goto" where she's at

    #She's agreed to come over
    elif Line == "lonely":
            if not Player.Male:
                ch_w "Не могу оставить тебя одну ни на минуту. . ."
            else:
                ch_w "Не могу оставить тебя одного ни на минуту. . ."
    elif Line == "command":
            ch_w "Ладно, [WandaX.Petname]."
    elif Line:
            ch_w "Конечно."

    $ Line = 0
    ch_w "Я останусь здесь."
    $ WandaX.Loc = bg_current
    return

# End Wanda Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

### Wanda's Clothes  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Wanda_Clothes:   #rkeljsvgbdw
    if WandaX.Taboo:
            if "exhibitionist" in WandaX.Traits:
                ch_w "Ооох . ."
            elif ApprovalCheck(WandaX, 900, TabM=4) or ApprovalCheck(WandaX, 400, "I", TabM=3):
                ch_w "Я бы предпочла не переодеваться здесь. . ."
            else:
                ch_w "Я бы предпочла не переодеваться здесь. . ."
                ch_w "Мы можем поговорить об этом в одной из наших комнат?"
                return
    elif ApprovalCheck(WandaX, 900, TabM=4) or ApprovalCheck(WandaX, 600, "L") or ApprovalCheck(WandaX, 300, "O"):
                ch_w "Что ты хочешь обсудить?"
    else:
                ch_w "Почему ты беспокоишься о моей одежде?"
                return

    if Girl != WandaX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = WandaX
    call Shift_Focus(Girl)

label Wanda_Wardrobe_Menu:
    $ WandaX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .
    while True:
        menu:
            ch_w "Что ты хочешь обсудить?"
            "Верх":
                        call Wanda_Clothes_Over
            "Низ":
                        call Wanda_Clothes_Legs
            "Нижнее белье":
                        call Wanda_Clothes_Under
            "Аксессуары":
                        call Wanda_Clothes_Misc
            "Управление нарядами":
                        call Wanda_Clothes_Outfits
            "Давай поговорим о том, что ты носишь.":
                        call Clothes_Schedule(WandaX)

            "Могу я посмотреть?" if WandaX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(WandaX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_w "Ладно, как я выгляжу?"
                    hide PhoneSex
            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(WandaX,0,2)
                    if _return:
                        hide DressScreen
            "Может, тебе будет комфортнее за ширмой? (locked)" if WandaX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if WandaX.Loc == bg_current and not WandaX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if not Player.Male and "girltalk" not in WandaX.History and "nogirls" not in WandaX.History:
                            ch_w "О, в ней нет нужды."
                    elif ApprovalCheck(WandaX, 1500) or (WandaX.SeenChest and WandaX.SeenPussy):
                            if not Player.Male:
                                ch_w "Я думаю, ты уже видела достаточно."
                            else:
                                ch_w "Я думаю, ты уже видела достаточно."
                    else:
                            show DressScreen zorder 150
                            ch_w "Эм, ага, спасибо."

            "У меня есть подарок для тебя (locked)" if WandaX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if WandaX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(WandaX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ WandaX.OutfitChange()
                    $ WandaX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != WandaX:
                            ch_p "Я хочу поговорить о твоей одежде."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = WandaX
                    call Shift_Focus(Girl)

            "Сменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current:
                    pass
            "Сменить вид" if Girl.Loc == bg_current:
                    call WardrobeView(WandaX)

            "Неважно, ты и так хорошо выглядишь.":
                    call Girl_Pos_Reset(WandaX)
                    if "wardrobe" not in WandaX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if WandaX.Chat[1] <= 1:
                                    $ WandaX.Statup("Love", 70, 15)
                                    $ WandaX.Statup("Obed", 40, 20)
                                    ch_w "Спасибо."
                            elif WandaX.Chat[1] <= 10:
                                    $ WandaX.Statup("Love", 70, 5)
                                    $ WandaX.Statup("Obed", 40, 7)
                                    ch_w "Да?"
                            elif WandaX.Chat[1] <= 50:
                                    $ WandaX.Statup("Love", 70, 1)
                                    $ WandaX.Statup("Obed", 40, 1)
                                    ch_w "Да? Ну ладно."
                            else:
                                    ch_w "Конечно."
                            $ WandaX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(WandaX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ WandaX.OutfitChange()
                    $ WandaX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ WandaX.Chat[1] += 1
                    $ Trigger = 0
                    if WandaX.Panties and "pantyless" in WandaX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ WandaX.DailyActions.remove("pantyless")
                    return

        #Loops back up
        #return #jump Wanda_Clothes
        #End of Wanda Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Wanda_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(WandaX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(WandaX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(WandaX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(WandaX,4,1)
                    "Одежда для сна":
                                call OutfitShame(WandaX,7,1)
                    "Купальник":
                                call OutfitShame(WandaX,10,1)

                    "Повседневка 1" if ApprovalCheck(WandaX, 2500):
                                call OutfitShame(WandaX,11,1)
                    "Повседневка 2" if ApprovalCheck(WandaX, 2500):
                                call OutfitShame(WandaX,12,1)
                    #8 is Emma's teaching clothes,
                    "Неважно":
                                pass

        "Надень красную рубашку с брюками.":
                $ WandaX.OutfitChange("casual1")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                            $ WandaX.Outfit = "casual1"
                            $ WandaX.Shame = 0
                            ch_w "Ага, мне они нравятся."
                    "Давай попробуем что-нибудь другое.":
                            ch_w "Ох."

        "Надень корсет и шорты.":
                $ WandaX.OutfitChange("casual2")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                            $ WandaX.Outfit = "casual2"
                            $ WandaX.Shame = 0
                            ch_w "Мне нравится."
                    "Давай попробуем что-нибудь другое.":
                            ch_w "Ох."

        "Надень наряд с черным платьем." if "witch" in WandaX.History:
                $ WandaX.OutfitChange("casual3")
                menu:
                    "Ты должна носить его. [[Выбрать текущий наряд]":
                            $ WandaX.Outfit = "casual3"
                            $ WandaX.Shame = 0
                            ch_w "Мне нравится."
                    "Давай попробуем что-нибудь другое.":
                            ch_w "Ох."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not WandaX.Custom1[0] and not WandaX.Custom2[0] and not WandaX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if WandaX.Custom1[0] or WandaX.Custom2[0] or WandaX.Custom3[0]:
                $ Cnt = 0
                while 1:
                    menu:
                        "Надень Пользовательский 1 (locked)" if not WandaX.Custom1[0]:
                                pass
                        "Надень Пользовательский 1" if WandaX.Custom1[0]:
                                $ WandaX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Надень Пользовательский 2 (locked)" if not WandaX.Custom2[0]:
                                pass
                        "Надень Пользовательский 2" if WandaX.Custom2[0]:
                                $ WandaX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Надень Пользовательский 3 (locked)" if not WandaX.Custom3[0]:
                                pass
                        "Надень Пользовательский 3" if WandaX.Custom3[0]:
                                $ WandaX.OutfitChange("custom3")
                                $ Cnt = 6

                        "Ты должна одеваться так, когда мы наедине (locked)" if not Cnt:
                                pass
                        "Ты должна одеваться так, когда мы наедине" if Cnt:
                                if Cnt == 5:
                                    $ WandaX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ WandaX.Clothing[9] = "custom3"
                                else:
                                    $ WandaX.Clothing[9] = "custom1"
                                ch_w "О, конечно."

                        "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                menu:
                                    "Пользовательский 1 [[очистить слот 1]" if WandaX.Custom1[0]:
                                        ch_w "Ох."
                                        $ WandaX.Custom1[0] = 0
                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not WandaX.Custom1[0]:
                                        pass
                                    "Пользовательский 2 [[очистить слот 2]" if WandaX.Custom2[0]:
                                        ch_w "Ох."
                                        $ WandaX.Custom2[0] = 0
                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not WandaX.Custom2[0]:
                                        pass
                                    "Пользовательский 3 [[очистить слот 3]" if WandaX.Custom3[0]:
                                        ch_w "Ох."
                                        $ WandaX.Custom3[0] = 0
                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not WandaX.Custom3[0]:
                                        pass
                                    "Неважно [[назад]":
                                        pass

                        "Тебе следует надеть его [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                pass
                        "Тебе следует надеть его" if Cnt:
                                call Custom_Out(WandaX,Cnt)
                        "Ладно, вернемся к началу нашего разговора. . .":
                                $ Cnt = 0
                                return #jump Wanda_Clothes

        "Наденешь спортивную одежду?" if not WandaX.Taboo or bg_current == "bg dangerroom":
                $ WandaX.OutfitChange("gym")

        "Наденешь одежду для сна?" if not WandaX.Taboo:
                if ApprovalCheck(WandaX, 1200):
                        $ WandaX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(WandaX)
                        if _return:
                            $ WandaX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (WandaX.Taboo and bg_current != "bg pool" and not ApprovalCheck(WandaX, 800, TabM=2)) or not WandaX.Swim[0]:
                $ WandaX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not WandaX.Taboo or bg_current == "bg pool" or ApprovalCheck(WandaX, 800, TabM=2)) and WandaX.Swim[0]:
                $ WandaX.OutfitChange("swimwear")

        "Наденешь хэллоуинский костюм?" if "halloween" in WandaX.History:
                ch_w "Ладно."
                $ WandaX.OutfitChange("costume")

        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ WandaX.FaceChange("sexy", 1)
                $ Line = 0
                if not WandaX.Chest and not WandaX.Panties and not WandaX.Over and not WandaX.Legs and not WandaX.Hose:
                    ch_w "Ага- подожди, тебе-то откуда знать?!"
                elif WandaX.SeenChest and WandaX.SeenPussy and ApprovalCheck(WandaX, 1200, TabM=4):
                    ch_w "Спасибо? . ."
                    $ Line = 1
                elif ApprovalCheck(WandaX, 2000, TabM=4):
                    if not Player.Male:
                        ch_w "Ладно, сис. . ."
                    else:
                        ch_w "Ладно, бро. . ."
                    $ Line = 1
                elif WandaX.SeenChest and WandaX.SeenPussy and ApprovalCheck(WandaX, 1200, TabM=0):
                    ch_w "Ага, но я не хочу хвастаться своим телом. . ."
                elif ApprovalCheck(WandaX, 2000, TabM=0):
                    ch_w "Ага, но я не хочу хвастаться своим телом. . ."
                elif ApprovalCheck(WandaX, 1000, TabM=0):
                    $ WandaX.FaceChange("confused", 1,Mouth="smirk")
                    ch_w "Ага, но я не хочу хвастаться своим телом. . ."
                    $ WandaX.FaceChange("bemused", 0)
                else:
                    $ WandaX.FaceChange("angry", 1)
                    ch_w "Что?"

                call expression WandaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in WandaX.History:
                        $ Line = 0
                if Line:
                    #If she got nude. . .
                    $ WandaX.OutfitChange("nude")
                    "Она сбрасывает одежду к своим ногам."
                    call Girl_First_Topless(WandaX)
                    call Girl_First_Bottomless(WandaX,1)
                    $ WandaX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется. что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in WandaX.Traits:
                                ch_w "Ох, ого. . ."
                                $ WandaX.Outfit = "nude"
                                $ WandaX.Statup("Lust", 50, 10)
                                $ WandaX.Statup("Lust", 70, 5)
                                $ WandaX.Shame = 50
                            elif ApprovalCheck(WandaX, 800, "I") or ApprovalCheck(WandaX, 2800, TabM=0):
                                ch_w "Оооох, эм. . ."
                                $ WandaX.Outfit = "nude"
                                $ WandaX.Shame = 50
                            else:
                                $ WandaX.FaceChange("sexy", 1)
                                $ WandaX.Eyes = "surprised"
                                ch_w "Ха!"

                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in WandaX.Traits:
                                ch_w "Оу."
                            elif ApprovalCheck(WandaX, 800, "I") or ApprovalCheck(WandaX, 2800, TabM=0):
                                $ WandaX.FaceChange("bemused", 1)
                                ch_w "Ты -не- хочешь, чтобы я ходила в таком виде? . ."
                                ch_w ". . ."
                            else:
                                $ WandaX.FaceChange("confused", 1)
                                ch_w "Честно говоря, я и не планировала выходить в люди в таком виде. . ."
                $ Line = 0

        "Неважно":
            return #jump Wanda_Clothes

    return #jump Wanda_Clothes
    #End of Wanda Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Wanda_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять [get_clothing_name(WandaX.Over_key, vin)]?" if WandaX.Over:
                call Wardrobe_Remove(WandaX)

        "Примерь красную рубашку" if WandaX.Over != "shirt":
                $ WandaX.FaceChange("bemused")
                if not WandaX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_w "Конечно."
                elif ApprovalCheck(WandaX, 800, TabM=0):
                    ch_w "Конечно."
                else:
                    call Display_DressScreen(WandaX)
                    if not _return:
                            $ WandaX.FaceChange("bemused", 1)
                            ch_w "Я не хочу сейчас переодевать [get_clothing_name(WandaX.Over_key, vin)]."
                            return #jump Wanda_Clothes
                $ WandaX.Over = "shirt"

        "Примерь корсет" if WandaX.Over != "corset":
                $ WandaX.FaceChange("bemused")
                if not WandaX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_w "Конечно."
                elif ApprovalCheck(WandaX, 800, TabM=0):
                    ch_w "Конечно."
                else:
                    call Display_DressScreen(WandaX)
                    if not _return:
                            $ WandaX.FaceChange("bemused", 1)
                            ch_w "Я не хочу сейчас переодевать [get_clothing_name(WandaX.Over_key, vin)]."
                            return #jump Wanda_Clothes
                $ WandaX.Over = "corset"

        "Надень фиолетовый топ" if WandaX.Over != "purple top" and "halloween" in WandaX.History:
                $ WandaX.FaceChange("bemused")
                if not WandaX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_w "Конечно."
                elif ApprovalCheck(WandaX, 800, TabM=0):
                    ch_w "Конечно."
                else:
                    call Display_DressScreen(WandaX)
                    if not _return:
                            $ WandaX.FaceChange("bemused", 1)
                            ch_w "Я не хочу сейчас переодевать [get_clothing_name(WandaX.Over_key, vin)]."
                            return #jump Wanda_Clothes
                $ WandaX.Over = "purple top"

        "Может, просто накинешь полотенце?" if WandaX.Over != "towel":
                $ WandaX.FaceChange("bemused", 1)
                if WandaX.Chest or WandaX.SeenChest:
                    ch_w "Ты сейчас серьезно? . ."
                elif ApprovalCheck(WandaX, 1000, TabM=0):
                    $ WandaX.FaceChange("perplexed", 1)
                    ch_w "Ладно. . ."
                else:
                    call Display_DressScreen(WandaX)
                    if not _return:
                            ch_w "Я не хочу укутываться в полотенце."
                            return #jump Wanda_Clothes
                $ WandaX.Over = "towel"

        "Примерь красную куртку" if WandaX.Acc != "jacket":
                $ WandaX.FaceChange("bemused")
                ch_w "Конечно."
                $ WandaX.Acc = "jacket"
        "Сними [get_clothing_name(WandaX.Acc_key, vin)]" if WandaX.Acc:
                $ WandaX.FaceChange("bemused")
                ch_w "Конечно."
                $ WandaX.Acc = 0

        "Неважно":
            pass
    return #jump Wanda_Clothes
    #End of Wanda Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Wanda_NoBra:
        menu:
            ch_w "У меня под [get_clothing_name(WandaX.Over_key, tvo)] ничего нет. . ."
            "Тогда надень что-нибудь. . .":
                        if WandaX.SeenChest and ApprovalCheck(WandaX, 1000, TabM=3):
                                $ WandaX.Blush = 1
                                ch_w "Я не сказала, что меня это беспокоит. . ."
                                $ WandaX.Blush = 0
                        elif ApprovalCheck(WandaX, 1200, TabM=4):
                                $ WandaX.Blush = 1
                                ch_w "Вообще-то, меня это не беспокоит. . ."
                                $ WandaX.Blush = 0
                        elif ApprovalCheck(WandaX, 900, TabM=2) and "lace bra" in WandaX.Inventory:
                                ch_w "Я могу что-нибудь подобрать."
                                $ WandaX.Chest  = "lace bra"
                                "Она достает свой кружевной лифчик и надевает его под [get_clothing_name(WandaX.Over_key, vin)]."
                        elif ApprovalCheck(WandaX, 700, TabM=2):
                                ch_w "Я могу что-нибудь подобрать."
                                $ WandaX.Chest = "red bra"
                                "Она достает красный лифчик и надевает его под [get_clothing_name(WandaX.Over_key, vin)]."
                        else:
                                ch_w "Ага, я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(WandaX, 1100, "LI", TabM=2) and WandaX.Love > WandaX.Inbt:
                                ch_w "Конечно. . ."
                        elif ApprovalCheck(WandaX, 700, "OI", TabM=2) and WandaX.Obed > WandaX.Inbt:
                                ch_w "Конечно. . ."
                        elif ApprovalCheck(WandaX, 600, "I", TabM=2):
                                ch_w "Ну. . . ага."
                        elif ApprovalCheck(WandaX, 1300, TabM=2):
                                ch_w "Ох, согласна."
                        else:
                                $ WandaX.FaceChange("surprised")
                                $ WandaX.Brows = "angry"
                                if WandaX.Taboo > 20:
                                    ch_w "Прости, но не на людях."
                                else:
                                    ch_w "Хех, не-а, [WandaX.Petname]!"
                                call expression WandaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0
            "Неважно.":
                        ch_w "Ладно. . ."
                        return 0
        return 1
        #End of Wanda bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Wanda_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(WandaX.Legs_key, vin)]?" if WandaX.Legs:
                call Wardrobe_Remove(WandaX,1)

        "Примерь кожаные брюки" if WandaX.Legs != "pants":
                ch_p "Как насчет кожаных брюк?"
                ch_w "Ладно?"
                $ WandaX.Legs = "pants"

        "Примерь черные шорты" if WandaX.Legs != "shorts":
                ch_p "Ты великолепно выглядишь в черных шортах."
                ch_w "Да?"
                $ WandaX.Legs = "shorts"

        "Примерь черное платье" if WandaX.Legs != "dress":
                ch_p "Почему бы тебе не примерить то черное платье?"
                ch_w "Хорошо?"
                $ WandaX.Legs = "dress"

        "Надень фиолетовую юбку" if WandaX.Legs != "skirt" and "halloween" in WandaX.History:
                ch_p "Почему бы тебе не надеть фиолетовую юбку?"
                ch_w "Хорошо?"
                $ WandaX.Legs = "skirt"

        "Сними обувь (locked)" if not WandaX.Boots:
                pass
        "Сними [get_clothing_name(WandaX.Boots_key, vin)]" if WandaX.Boots:
                ch_p "Может, снимешь [get_clothing_name(WandaX.Boots_key, vin)]?"
                ch_w "Ладно."
                $ WandaX.Boots = 0
#        "Add Sneakers" if WandaX.Boots != "sneaks":
#                ch_p "Maybe put your sneakers on."
#                ch_w "Ладно."
#                $ WandaX.Boots = "sneaks"
        "Надень обувь" if WandaX.Boots != "boots":
                ch_p "Может, наденешь ботинки?"
                ch_w "Ладно."
                $ WandaX.Boots = "boots"
#        "Add Sneakers" if WandaX.Boots != "sneaks":
#                ch_p "Maybe put your sneakers on."
#                ch_w "'K."
#                $ WandaX.Boots = "sneaks"

        "Неважно":
                pass
    return #jump Wanda_Clothes
    #End of Wanda Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Wanda_NoPantiesOn:
        menu:
            ch_w "На мне сейчас нет трусиков. . ."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if WandaX.SeenPussy and ApprovalCheck(WandaX, 1100, TabM=4):
                                $ WandaX.Blush = 2
                                ch_w "Честно говоря, меня это совсем не беспокоит. . ."
                                $ WandaX.Blush = 1
                        elif ApprovalCheck(WandaX, 1500, TabM=4):
                                $ WandaX.Blush = 2
                                ch_w "Честно говоря, меня это совсем не беспокоит. . ."
                                $ WandaX.Blush = 1
                        elif ApprovalCheck(WandaX, 700, TabM=4):
                                ch_w "О, конечно."
                                if "lace panties" in WandaX.Inventory:
                                        ch_w "Мне нравится ход твоих мыслей."
                                        $ WandaX.Panties  = "lace panties"
                                else:
                                        $ WandaX.Panties = "gray panties"
                                if ApprovalCheck(WandaX, 1200, TabM=4):
                                    $ Line = get_clothing_name(WandaX.Legs_key, vin)
                                    $ WandaX.Legs = 0
                                    "Она снимает [Line] и натягивает [get_clothing_name(WandaX.Panties_key, vin)]."
                                elif WandaX.Legs == "dress":
                                    "Она достает [get_clothing_name(WandaX.Panties_key, vin)] и натягивает их под платье."
                                    $ WandaX.Legs = 0
                                    "Затем она сбрасывает платье на пол."
                                else:
                                    $ Line = get_clothing_name(WandaX.Legs_key, vin)
                                    $ WandaX.Legs = 0
                                    "Она отходит на мгновение, а затем возвращается в [get_clothing_name(WandaX.Panties_key, pre)]."
                                return #jump Wanda_Clothes
                        else:
                                ch_w "Я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(WandaX, 1100, "LI", TabM=3) and WandaX.Love > WandaX.Inbt:
                                ch_w "Конечно. . ."
                        elif ApprovalCheck(WandaX, 700, "OI", TabM=3) and WandaX.Obed > WandaX.Inbt:
                                ch_w "Конечно. . ."
                        elif ApprovalCheck(WandaX, 600, "I", TabM=3):
                                ch_w "Ладно. . ."
                        elif ApprovalCheck(WandaX, 1300, TabM=2):
                                ch_w "Ох, наверное."
                        else:
                                $ WandaX.FaceChange("surprised")
                                $ WandaX.Brows = "angry"
                                if WandaX.Taboo > 20:
                                    ch_w "Прости, но не на людях."
                                else:
                                    ch_w "Хех, не-а, [WandaX.Petname]!"
                                call expression WandaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0
            "Неважно.":
                ch_w "Ладно. . ."
                return 0
        return 1
        #End of Wanda Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Wanda_Clothes_Under:
        "Верх":
            menu:
                "Может, снимешь [get_clothing_name(WandaX.Chest_key, vin)]?" if WandaX.Chest:
                        $ WandaX.FaceChange("bemused", 1)
                        if WandaX.SeenChest and ApprovalCheck(WandaX, 900, TabM=2.7):
                                ch_w "Конечно."
                        elif ApprovalCheck(WandaX, 1100, TabM=2):
                            if WandaX.Taboo:
                                ch_w "Я не хочу делать этого здесь. . ."
                            else:
                                ch_w "Пожалуй, можно. . ."
#                        elif WandaX.Over == "jacket" and ApprovalCheck(WandaX, 600, TabM=2):
#                            ch_w "This jacket is a bit revealing. . ."
                        elif WandaX.Over and ApprovalCheck(WandaX, 500, TabM=2):
                            ch_w "Наверное, можно. . ."
                        elif not WandaX.Over:
                            call Display_DressScreen(WandaX)
                            if not _return:
                                ch_w "Сперва мне нужно что-нибудь накинуть."
                                return #jump Wanda_Clothes
                        else:
                            call Display_DressScreen(WandaX)
                            if not _return:
                                ch_w "Я так не думаю."
                                return #jump Wanda_Clothes
                        $ Line = get_clothing_name(WandaX.Chest_key, vin)
                        $ WandaX.Chest = 0
                        if WandaX.Over:
                            "Она залезает под [get_clothing_name(WandaX.Over_key, vin)], хватает и снимает [Line], а затем бросает на пол."
                        else:
                            "Она скидывает [Line] на пол."
                            if not renpy.showing('DressScreen'):
                                call Girl_First_Topless(WandaX)

                "Примерь красный лифчик" if WandaX.Chest != "red bra":
                        ch_p "Мне нравится твой красный лифчик."
                        if WandaX.SeenChest or ApprovalCheck(WandaX, 1100, TabM=2):
                            ch_w "Да?"
                            $ WandaX.Chest = "red bra"
                        else:
                            call Display_DressScreen(WandaX)
                            if not _return:
                                ch_w "Он довольно маленький. . ."
                            else:
                                $ WandaX.Chest = "red bra"


                "Примерь кружевной лифчик" if WandaX.Chest != "lace bra" and "lace bra" in WandaX.Inventory:
                        ch_p "Мне нравится твой кружевной лифчик."
                        if WandaX.SeenChest or ApprovalCheck(WandaX, 1300, TabM=2):
                            ch_w "Конечно."
                            $ WandaX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(WandaX)
                            if not _return:
                                ch_w "Я не уверена на его счет. . ."
                            else:
                                $ WandaX.Chest = "lace bra"

                "Примерь сетчатый топ" if WandaX.Chest != "mesh top":
                        ch_p "Мне нравится твой сетчатый топ."
                        if WandaX.SeenChest or ApprovalCheck(WandaX, 1300, TabM=2) or WandaX.Over:
                            ch_w "Не сомневаюсь."
                            $ WandaX.Chest = "mesh top"
                        else:
                            call Display_DressScreen(WandaX)
                            if not _return:
                                ch_w "Он довольно прозрачный. . ."
                            else:
                                $ WandaX.Chest = "mesh top"

#                "Add sports bra" if WandaX.Chest != "sports bra":
#                        ch_p "I like that sports bra."
#                        if WandaX.SeenChest or ApprovalCheck(WandaX, 1100, TabM=2):
#                            ch_w "Yeah?"
#                            $ WandaX.Chest = "sports bra"
#                        else:
#                            call Display_DressScreen(WandaX)
#                            if not _return:
#                                ch_w "It's kinda small. . ."
#                            else:
#                                $ WandaX.Chest = "sports bra"

                "Примерь лифчик бикини" if WandaX.Chest != "bikini top" and "bikini top" in WandaX.Inventory:
                        ch_p "Мне нравится твой лифчик бикини."
                        if bg_current == "bg pool":
                                ch_w "Конечно."
                                $ WandaX.Chest = "bikini top"
                        else:
                                if WandaX.SeenChest or ApprovalCheck(WandaX, 1000, TabM=2):
                                    ch_w "Конечно."
                                    $ WandaX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(WandaX)
                                    if not _return:
                                            ch_w "Я не уверена, мы сейчас не на пляже. . ."
                                    else:
                                            $ WandaX.Chest = "bikini top"
                "Неважно":
                        pass
            return #jump Wanda_Clothes_Under

        "Варианты колготок и чулок":
            menu:
                "Сними [get_clothing_name(WandaX.Hose_key, vin)]." if WandaX.Hose:
                                $ WandaX.FaceChange("sexy", 1)
                                if WandaX.SeenPanties and WandaX.Panties and ApprovalCheck(WandaX, 500, TabM=5):
                                    ch_w "Конечно."
                                elif WandaX.SeenPussy and ApprovalCheck(WandaX, 900, TabM=4):
                                    ch_w "Конечно."
                                elif ApprovalCheck(WandaX, 1300, TabM=2) and WandaX.Panties:
                                    ch_w "Ладно, ради тебя. . ."
                                elif ApprovalCheck(WandaX, 700) and not WandaX.Panties:
                                    call Wanda_NoPantiesOn
                                    if not _return and not WandaX.Panties:
                                        if not ApprovalCheck(WandaX, 1500):
                                            call Display_DressScreen(WandaX)
                                            if not _return:
                                                return #jump Wanda_Clothes
                                        else:
                                                return #jump Wanda_Clothes
                                else:
                                    call Display_DressScreen(WandaX)
                                    if not _return:
                                        ch_w "Я так не думаю."
                                        if not WandaX.Panties:
                                                ch_w "На мне сейчас нет трусиков. . ."
                                        return #jump Wanda_Clothes
                                $ WandaX.Hose = 0

                "Чулки дополнили бы твой образ." if WandaX.Hose != "stockings":
                                $ WandaX.Hose = "stockings"
                "Колготки дополнили бы твой образ." if WandaX.Hose != "pantyhose" and "pantyhose" in WandaX.Inventory:
                                $ WandaX.Hose = "pantyhose"
                "Рваные колготки дополнили бы твой образ." if WandaX.Hose != "ripped pantyhose" and "ripped pantyhose" in WandaX.Inventory:
                                $ WandaX.Hose = "ripped pantyhose"
#                "The gray tights would look good with that." if WandaX.Hose != "tights":
#                                $ WandaX.Hose = "tights"
#                "The ripped tights would look good with that." if WandaX.Hose != "ripped tights" and "ripped tights" in WandaX.Inventory:
#                                $ WandaX.Hose = "ripped tights"
                "Чулки и пояс с подвязками дополнили бы твой образ." if WandaX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in WandaX.Inventory:
                                $ WandaX.Hose = "stockings and garterbelt"
                "Может, наденешь только пояс с подвязками?" if WandaX.Hose != "garterbelt" and "stockings and garterbelt" in WandaX.Inventory:
                                $ WandaX.Hose = "garterbelt"
                "Черные носки дополнили бы твой образ." if WandaX.Hose != "socks":
                                $ WandaX.Hose = "socks"
                "Неважно":
                        pass
            return #jump Wanda_Clothes_Under

        #Panties
        "Низ":
            menu:
                "Ты должна снять [get_clothing_name(WandaX.Panties_key, vin)]. . ." if WandaX.Panties:
                        $ WandaX.FaceChange("bemused", 1)
                        if ApprovalCheck(WandaX, 900) and (WandaX.Legs or (WandaX.SeenPussy and not WandaX.Taboo)):
                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                                if ApprovalCheck(WandaX, 850, "L"):
                                        ch_w "Конечно. . ."
                                elif ApprovalCheck(WandaX, 500, "O"):
                                        ch_w "Ладно."
                                elif ApprovalCheck(WandaX, 350, "I"):
                                        ch_w "Ох."
                                else:
                                        ch_w "Пожалуй. . ."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(WandaX, 1100, "LI", TabM=3) and WandaX.Love > WandaX.Inbt:
                                        ch_w "Не на людях. . ."
                                elif ApprovalCheck(WandaX, 700, "OI", TabM=3) and WandaX.Obed > WandaX.Inbt:
                                        ch_w "Что ж. . ."
                                elif ApprovalCheck(WandaX, 600, "I", TabM=3):
                                        ch_w "Хмммм. . ."
                                elif ApprovalCheck(WandaX, 1300, TabM=3):
                                        ch_w "Хм. . ."
                                else:
                                        call Display_DressScreen(WandaX)
                                        if not _return:
                                            $ WandaX.FaceChange("surprised")
                                            $ WandaX.Brows = "angry"
                                            if WandaX.Taboo > 20:
                                                ch_w "Прости, но на людях я не могу."
                                            else:
                                                ch_w "Хех, этому не бывать, [WandaX.Petname]!"
                                            return #jump Wanda_Clothes
                        $ Line = get_clothing_name(WandaX.Panties_key, vin)
                        $ WandaX.Panties = 0
                        if not WandaX.Legs:
                            "Она снимает [Line] и бросает их на пол."
                            if not renpy.showing('DressScreen'):
                                    call Girl_First_Bottomless(WandaX)
                        elif ApprovalCheck(WandaX, 1200, TabM=4):
                            $ Trigger = WandaX.Legs
                            $ WandaX.Legs = 0
                            pause 0.5
                            $ WandaX.Legs = Trigger
                            "Она снимает [get_clothing_name(WandaX.Legs_key, vin)] и [Line], затем снова надевает [get_clothing_name(WandaX.Legs_key, vin)]."
                            $ Trigger = 1
                            call Girl_First_Bottomless(WandaX,1)
                        elif WandaX.Legs == "dress":
                            "Она залезает под платье и стягивает [Line]."
                        else:
                            $ WandaX.Blush = 1
                            "Она на мгновение отходит, а затем возвращается."
                            $ WandaX.Blush = 0
                        $ Line = 0

                "Почему бы тебе вместо этих не надеть зеленые трусики?" if WandaX.Panties and WandaX.Panties != "gray panties":
                        if ApprovalCheck(WandaX, 1100, TabM=3):
                                ch_w "О, конечно."
                                $ WandaX.Panties = "gray panties"
                        else:
                                call Display_DressScreen(WandaX)
                                if not _return:
                                        ch_w "Тебе не следует думать, какие трусики на мне."
                                else:
                                        $ WandaX.Panties = "tan panties"

                "Почему бы тебе вместо этих не надеть кружевные трусики?" if "lace panties" in WandaX.Inventory and WandaX.Panties and WandaX.Panties != "lace panties":
                        if ApprovalCheck(WandaX, 1300, TabM=3):
                                ch_w "О, конечно."
                                $ WandaX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(WandaX)
                                if not _return:
                                        ch_w "Тебе не следует думать, какие трусики на мне."
                                else:
                                        $ WandaX.Panties = "lace panties"

                "Примерь трусики бикини" if WandaX.Panties != "bikini bottoms" and "bikini bottoms" in WandaX.Inventory:
                        ch_p "Мне нравятся твои трусики бикини."
                        if bg_current == "bg pool":
                                ch_w "Конечно."
                                $ WandaX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(WandaX, 800, TabM=2):
                                    ch_w "Конечно."
                                    $ WandaX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(WandaX)
                                    if not _return:
                                            ch_w "Я не уверена на их счет, мы сейчас не на пляже. . ."
                                    else:
                                            $ WandaX.Panties = "bikini bottoms"

                "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not WandaX.Panties:
                        $ WandaX.FaceChange("bemused", 1)
                        if WandaX.Legs and (WandaX.Love+WandaX.Obed) <= (2 * WandaX.Inbt):
                            $ WandaX.Mouth = "smile"
                            ch_w "А если я не хочу. . ?"
                            menu:
                                "Твое право":
                                    return #jump Wanda_Clothes
                                "Я настаиваю, надевай.":
                                    if (WandaX.Love+WandaX.Obed) <= (1.5 * WandaX.Inbt):
                                        $ WandaX.FaceChange("angry", Eyes="side")
                                        ch_w "Что ж, жаль."
                                        return #jump Wanda_Clothes
                                    else:
                                        $ WandaX.FaceChange("sadside")
                                        ch_w "Ох, ладно. . ."
                        else:
                            ch_w "Пожалуй. . ."
                        menu:
                            extend ""
                            "Как насчет зеленых?":
                                    ch_w "О, конечно."
                                    $ WandaX.Panties = "gray panties"
                            "Как насчет кружевных?" if "lace panties" in WandaX.Inventory:
                                    ch_w "О, конечно."
                                    $ WandaX.Panties  = "lace panties"
                            "Как насчет трусиков бикини?" if "bikini bottoms" in WandaX.Inventory:
                                    ch_w "О, конечно."
                                    $ WandaX.Panties = "bikini bottoms"
                "Неважно":
                    pass
            return #jump Wanda_Clothes_Under
        "Неважно":
            pass
    return #jump Wanda_Clothes
    #End of Wanda Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Wanda_Clothes_Misc:
        #Misc
        "Сухие волосы" if WandaX.Hair == "wet" or WandaX.Hair == "wetlong":
                ch_p "Тебе идут сухие волосы."
                if ApprovalCheck(WandaX, 600):
                    if not Player.Male:
                        ch_w "О, ты уверена?"
                    else:
                        ch_w "О, ты уверен?"
                    if WandaX.Hair == "wet":
                        $ WandaX.Hair = "short"
                    else:
                        $ WandaX.Hair = "long"
                else:
                    ch_w "Я не уверена, мне нравится моя нынешняя прическа."

        "Короткие волосы" if WandaX.Hair == "long":
                ch_p "Мне кажется, тебе идет короткая стрижка."
                if ApprovalCheck(WandaX, 600):
                    ch_w "О, правда?"
                    show blackscreen onlayer black
                    "Ее глаза на мгновение вспыхивают, а волосы укорачиваются."
                    $ WandaX.Hair = "short"
                    hide blackscreen onlayer black
                else:
                    ch_w "Мне больше нравится моя нынешняя прическа."
        "Длинные волосы" if WandaX.Hair == "short" and "witch" in WandaX.History:
                ch_p "Мне кажется, тебе идут длинные волосы."
                if ApprovalCheck(WandaX, 600):
                    ch_w "О, правда?"
                    show blackscreen onlayer black
                    "Ее глаза на мгновение вспыхивают, а волосы удлиняются."
                    $ WandaX.Hair = "long"
                    hide blackscreen onlayer black
                else:
                    ch_w "Мне больше нравится моя нынешняя прическа."

        "Влажные волосы" if WandaX.Hair != "wet" and WandaX.Hair != "wetlong":
                ch_p "Тебе стоит увлажнить волосы."
                if ApprovalCheck(WandaX, 800):
                    ch_w "О, правда?"
                    if WandaX.Hair == "short":
                        $ WandaX.Hair = "wet"
                    else:
                        $ WandaX.Hair = "wetlong"
                    show blackscreen onlayer black
                    "Она отходит на минуту и вскоре возвращается."
                    hide blackscreen onlayer black
                    ch_w "Так?"
                else:
                    ch_w "Уфф, это слишком хлопотно."

        "Отрасти волосы на лобке" if not WandaX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может, отрастишь?"
                call expression WandaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in WandaX.Todo:
                        $ WandaX.FaceChange("bemused", 1)
                        ch_w "Я работаю над этим."
                else:
                    $ WandaX.FaceChange("bemused", 1)
                    if ApprovalCheck(WandaX, 1000, TabM=0):
                            ch_w "Ладно, пожалуй, это можно устроить. . ."
                    else:
                            $ WandaX.FaceChange("surprised")
                            $ WandaX.Brows = "angry"
                            ch_w ". . . почему тебя интересуют волосы на моем лобке?"
                            return #jump Wanda_Clothes
                    $ WandaX.Todo.append("pubes")
                    $ WandaX.PubeC = 6
        "Побрей лобок" if WandaX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression WandaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ WandaX.FaceChange("bemused", 1)
                if "shave" in WandaX.Todo:
                        ch_w "Позже я этим займусь."
                else:
                    if ApprovalCheck(WandaX, 1100, TabM=0):
                        ch_w "О, значит, тебе не нравятся заросли?"
                    else:
                        $ WandaX.FaceChange("surprised")
                        $ WandaX.Brows = "angry"
                        ch_w ". . . почему тебя интересуют волосы на моем лобке?"
                        return #jump Wanda_Clothes
                    $ WandaX.Todo.append("shave")

        "Пирсинг [[Сначала посмотрите, как она выглядит без него] (locked)" if not WandaX.SeenPussy and not WandaX.SeenChest:
            pass

        "Надень пирсинг-кольца" if WandaX.Pierce != "ring" and (WandaX.SeenPussy or WandaX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсингом-кольцами."
                if "ring" in WandaX.Todo:
                    ch_w "Я работаю над этим."
                else:
                    $ WandaX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(WandaX, 1150, TabM=0)
                    if ApprovalCheck(WandaX, 900, "L", TabM=0) or (Approval and WandaX.Love > 2* WandaX.Obed):
                        ch_w "Думаешь, он дополнит мой образ?"
                    elif ApprovalCheck(WandaX, 600, "I", TabM=0) or (Approval and WandaX.Inbt > WandaX.Obed):
                        ch_w "Я думала о нем. . ."
                    elif ApprovalCheck(WandaX, 500, "O", TabM=0) or Approval:
                        ch_w "Если тебе он нравится, [WandaX.Petname]."
                    else:
                        $ WandaX.FaceChange("surprised")
                        $ WandaX.Brows = "angry"
                        ch_w "Мне не интересно, [WandaX.Petname]."
                        return #jump Wanda_Clothes
                    $ WandaX.Todo.append("ring")

        "Надень пирсинг-штанги" if WandaX.Pierce != "barbell" and (WandaX.SeenPussy or WandaX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in WandaX.Todo:
                    ch_w "Я работаю над этим."
                else:
                    $ WandaX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(WandaX, 1150, TabM=0)
                    if ApprovalCheck(WandaX, 900, "L", TabM=0) or (Approval and WandaX.Love > 2 * WandaX.Obed):
                        ch_w "Думаешь, он дополнит мой образ?"
                    elif ApprovalCheck(WandaX, 600, "I", TabM=0) or (Approval and WandaX.Inbt > WandaX.Obed):
                        ch_w "Я думала о нем. . ."
                    elif ApprovalCheck(WandaX, 500, "O", TabM=0) or Approval:
                        ch_w "Если тебе он нравится, [WandaX.Petname]."
                    else:
                        $ WandaX.FaceChange("surprised")
                        $ WandaX.Brows = "angry"
                        ch_w "Мне не интересно, [WandaX.Petname]."
                        return #jump Wanda_Clothes
                    $ WandaX.Todo.append("barbell")

        "Сними пирсинг" if WandaX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ WandaX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(WandaX, 1350, TabM=0)
                if ApprovalCheck(WandaX, 950, "L", TabM=0) or (Approval and WandaX.Love > WandaX.Obed):
                    ch_w "Да ладно, его было так сложно сделать. . ."
                elif ApprovalCheck(WandaX, 700, "I", TabM=0) or (Approval and WandaX.Inbt > WandaX.Obed):
                    ch_w "Что ж, а мне он нравится."
                    return
                elif ApprovalCheck(WandaX, 600, "O", TabM=0) or Approval:
                    ch_w "Ладно. . ."
                else:
                    $ WandaX.FaceChange("surprised")
                    $ WandaX.Brows = "angry"
                    ch_w "Что ж, а мне он нравится. . ."
                    return #jump Wanda_Clothes
                $ WandaX.Pierce = 0

        "Надень повязку на голову" if WandaX.Hat != "headband" and "halloween" in WandaX.History:
                ch_p "Почему бы тебе не надеть повязку на голову?"
                ch_w "О, хорошо. . ."
                $ WandaX.Hat = "headband"
#        "Glasses" if WandaX.Hat != "glasses" and "halloween" in WandaX.History:
#                ch_p "Why don't you wear those glasses?"
#                ch_w "Oh, ok. . ."
#                $ WandaX.Hat = "glasses"
        "Сними [get_clothing_name(WandaX.Hat_key, vin)]" if WandaX.Hat:
                ch_p "Думаю, тебе лучше [get_clothing_name(WandaX.Hat_key, vin)]."
                ch_w "Ладно. . ."
                $ WandaX.Hat = 0

        "Надень черный чокер" if WandaX.Neck != "choker":
                ch_p "Почему бы тебе не надеть чокер?"
                ch_w "Ладно. . ."
                $ WandaX.Neck = "choker"
        "Надень зеленый шарф" if WandaX.Neck != "scarf" and "halloween" in WandaX.History:
                ch_p "Почему бы тебе не надеть зеленый шарф?"
                ch_w "Ладно. . ."
                $ WandaX.Neck = "scarf"
        "Сними украшения с шеи" if WandaX.Neck:
                ch_p "Думаю, тебе стоит снять [get_clothing_name(WandaX.Neck_key, vin)]."
                ch_w "Ладно. . ."
                $ WandaX.Neck = 0


        "Вкл\выкл напульсники":
                if not WandaX.Arms:
                        ch_p "Почему бы тебе не надеть напульсники?"
                else:
                        ch_p "Думаю, тебе стоит снять напульсники."
                ch_w "Хорошо."
                $ WandaX.Arms = 0 if WandaX.Arms else "armlets"

        "Неважно":
            pass
    return #jump Wanda_Clothes
    #End of Wanda Misc Wardrobe

return
#End Wanda Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
