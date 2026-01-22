# star Storm chat interface
#Storm Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Storm_Relationship: #rkeljs
    while True:
        menu:
            ch_s "О чем ты хочешь поговорить?"
            "Хочешь стать моей девушкой?" if StormX not in Player.Harem and "ex" not in StormX.Traits and "story" not in Player.History:
                    $ StormX.DailyActions.append("relationship")
                    if "asked boyfriend" in StormX.DailyActions and "angry" in StormX.DailyActions:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Прошу, хватит."
                            return
                    elif "asked boyfriend" in StormX.DailyActions:
                            $ StormX.FaceChange("sad", 1)
                            ch_s "Ох, [Girl.Petname], нет."
                            return
                    elif StormX.Break[0]:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Я. . . не делюсь."
                            if Player.Harem:
                                    $ StormX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_s "Мне это. . . не подходит."

                    $ StormX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "StormYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_s "Сначала тебе нужно обсудить это с остальными, [StormX.Petname]."
                        else:
                            ch_s "Сначала, [StormX.Petname], тебе нужно обсудить это с [Player.Harem[0].Name_tvo]."
                        return

                    if StormX.Event[5]:
                            $ StormX.FaceChange("bemused", 1)
                            if not Player.Male:
                                ch_s "Когда я сама тебе это предлагала, ты ответила \"нет\". . ."
                            else:
                                ch_s "Когда я сама тебе это предлагала, ты ответил \"нет\". . ."
                    else:
                            $ StormX.FaceChange("surprised", 2)
                            ch_s "Что? . ."
                            $ StormX.FaceChange("smile", 1)

                    call Storm_OtherWoman

                    if StormX.Love >= 800:
                            $ StormX.FaceChange("surprised", 1)
                            $ StormX.Mouth = "smile"
                            if StormX.Event[5]:
                                    $ StormX.Statup("Love", 200, 10)
                                    call Storm_BF
                                    return
                            $ StormX.Statup("Love", 200, 40)
                            ch_s "С удовольствием!"
                            if "boyfriend" not in StormX.Petnames:
                                    $ StormX.Petnames.append("boyfriend")
                            if "StormYes" in Player.Traits:
                                    $ Player.Traits.remove("StormYes")
                            $ Player.Harem.append(StormX)
                            call Harem_Initiation
                            "[StormX.Name] подходит и страстно целует вас."
                            $ StormX.FaceChange("kiss", 1)
                            $ StormX.Kissed += 1
                    elif StormX.Obed >= 500:
                            $ StormX.FaceChange("perplexed")
                            ch_s "Я не уверена, что хочу именно \"встречаться\". . ."
                    elif StormX.Inbt >= 500:
                            $ StormX.FaceChange("smile")
                            ch_s "Разве мы не можем просто оставить все как есть?"
                    else:
                            $ StormX.FaceChange("perplexed", 1)
                            ch_s "Я не уверена, насчет этого, [StormX.Petname]."

            "Может, начнем все сначала?" if "ex" in StormX.Traits:
                    $ StormX.DailyActions.append("relationship")
                    if "asked boyfriend" in StormX.DailyActions and "angry" in StormX.DailyActions:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Прошу, хватит."
                            return
                    elif "asked boyfriend" in StormX.DailyActions:
                            $ StormX.FaceChange("sad", 1)
                            ch_s "Ох, [Girl.Petname], нет."
                            return

                    $ StormX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "StormYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_s "Сначала тебе нужно обсудить это с остальными, [StormX.Petname]."
                            else:
                                ch_s "Сначала, [StormX.Petname], тебе нужно обсудить это с [Player.Harem[0].Name_tvo]."
                            return

                    $ Cnt = 0
                    call Storm_OtherWoman

                    if StormX.Love >= 800:
                            $ StormX.FaceChange("surprised", 1)
                            $ StormX.Mouth = "smile"
                            $ StormX.Statup("Love", 90, 5)
                            ch_s "Пожалуй, я могу дать тебе еще один шанс."
                            if "boyfriend" not in StormX.Petnames:
                                    $ StormX.Petnames.append("boyfriend")
                            $ StormX.Traits.remove("ex")
                            if "StormYes" in Player.Traits:
                                    $ Player.Traits.remove("StormYes")
                            $ Player.Harem.append(StormX)
                            call Harem_Initiation
                            "[StormX.Name] притягивает вас к себе и крепко целует."
                            $ StormX.FaceChange("kiss", 1)
                            $ StormX.Kissed += 1
                    elif StormX.Love >= 600 and ApprovalCheck(StormX, 1500):
                            $ StormX.FaceChange("smile", 1)
                            $ StormX.Statup("Love", 90, 5)
                            ch_s "Пожалуй, я могу дать нашим отношениям еще один шанс."
                            if "boyfriend" not in StormX.Petnames:
                                $ StormX.Petnames.append("boyfriend")
                            $ StormX.Traits.remove("ex")
                            if "StormYes" in Player.Traits:
                                    $ Player.Traits.remove("StormYes")
                            $ Player.Harem.append(StormX)
                            call Harem_Initiation
                            $ StormX.FaceChange("kiss", 1)
                            "[StormX.Name] дарит вам легкий поцелуй."
                            $ StormX.FaceChange("sly", 1)
                            $ StormX.Kissed += 1
                    elif StormX.Obed >= 500:
                            $ StormX.FaceChange("sad")
                            ch_s "Пожалуй, наши \"отношения\" выходят за рамки общепринятых норм."
                    elif StormX.Inbt >= 500:
                            $ StormX.FaceChange("perplexed")
                            ch_s "Давай оставим все как есть."
                    else:
                            $ StormX.FaceChange("perplexed", 1)
                            if not Player.Male:
                                ch_s "Ты потеряла мое доверие."
                            else:
                                ch_s "Ты потерял мое доверие."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if StormX in Player.Harem:
                            call AskDateOther

            "Думаю, мы должны расстаться." if StormX in Player.Harem:
                            if "breakup talk" in StormX.RecentActions:
                                    ch_s "Зачем ты мучаешь меня?"
                            elif "breakup talk" in StormX.DailyActions:
                                    ch_s "Давай не сегодня, [StormX.Petname]."
                            else:
                                    call Breakup(StormX)

            "О разговоре, который у нас был ранее. . .":
                menu:
                    "Ты хотела рассказать мне какую-то историю. . ." if "story" in Player.History and StormX.Event[5] == 20:
                            $ Player.History.remove("story")
                            ch_s "Ах, да, тогда я начну. . ."
                            call Storm_BF_Story
                    "Чувствую, ранее ты что-то хотела мне сказать. . ." if "lover" not in StormX.Traits and StormX.Event[6] >= 5:
                            if ApprovalCheck(StormX, 900, "L"):
                                    $ StormX.Event[6] = 3
                                    ch_s "Да, чувства тебя не подводят. . ."
                                    $ StormX.DailyActions.append("relationship")
                                    call Storm_Love_Redux
                            else:
                                    if not Player.Male:
                                        ch_s "Не думаю, что ты сейчас готова. . ."
                                    else:
                                        ch_s "Не думаю, что ты сейчас готов. . ."


                    "Ты говорила, что хочешь, чтобы я была более напористой?" if "sir" not in StormX.Petnames and "sir" in StormX.History and not Player.Male:
                            if "asked sub" in StormX.RecentActions:
                                    ch_s "Мы уже говорили об этом несколько минут назад."
                            elif "asked sub" in StormX.DailyActions:
                                    ch_s "Мы уже обсуждали это ранее. . ."
                            else:
                                    call Storm_Sub_Asked

                    "Ты говорила, что хочешь, чтобы я был более напористым?" if "sir" not in StormX.Petnames and "sir" in StormX.History and Player.Male:
                            if "asked sub" in StormX.RecentActions:
                                    ch_s "Мы уже говорили об этом несколько минут назад."
                            elif "asked sub" in StormX.DailyActions:
                                    ch_s "Мы уже обсуждали это ранее. . ."
                            else:
                                    call Storm_Sub_Asked

                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоей хозяйкой?" if "master" not in StormX.Petnames and "master" in StormX.History and not Player.Male:
                            if "asked sub" in StormX.RecentActions:
                                    ch_s "Мы уже говорили об этом несколько минут назад."
                            elif "asked sub" in StormX.DailyActions:
                                    ch_s "Мы уже обсуждали это ранее. . ."
                            else:
                                    call Storm_Sub_Asked

                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоим хозяином?" if "master" not in StormX.Petnames and "master" in StormX.History and Player.Male:
                            if "asked sub" in StormX.RecentActions:
                                    ch_s "Мы уже говорили об этом несколько минут назад."
                            elif "asked sub" in StormX.DailyActions:
                                    ch_s "Мы уже обсуждали это ранее. . ."
                            else:
                                    call Storm_Sub_Asked
                    "Неважно":
                            pass

            "Неважно":
                return

    return

label Storm_OtherWoman(Cnt = 0): #rkeljs
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((StormX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ StormX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_s "Но ты сейчас с [Player.Harem[0].Name_tvo] и другими."
    else:
        ch_s "Но ты сейчас с [Player.Harem[0].Name_tvo], разве нет?"
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "StormYes" in Player.Traits:
                if ApprovalCheck(StormX, 1800, Bonus = Cnt):
                    $ StormX.FaceChange("smile", 1)
                    if StormX.Love >= StormX.Obed:
                            ch_s "Пожалуй, я могу с ней поделиться."
                    elif StormX.Obed >= StormX.Inbt:
                            ch_s "Если ты этого хочешь."
                    else:
                            ch_s "Хорошо."
                else:
                    $ StormX.FaceChange("angry", 1)
                    ch_s "Да, пожалуй, это на нее похоже, но я не хочу делиться."
                    $ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "StormYes" not in Player.Traits and not Player.Male:
                if ApprovalCheck(StormX, 1800, Bonus = Cnt):
                        $ StormX.FaceChange("smile", 1)
                        if StormX.Love >= StormX.Obed:
                            ch_s "Наверное, я смогу с этим смириться."
                        elif StormX.Obed >= StormX.Inbt:
                            ch_s "Если ты этого хочешь."
                        else:
                            ch_s "Хорошо."
                        ch_s "Спроси ее и расскажи мне утром, что она ответила."
                else:
                        $ StormX.FaceChange("angry", 1)
                        ch_s "Да, пожалуй, это так похоже на нее, но я не собираюсь делиться."
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "StormYes" not in Player.Traits and Player.Male:
                if ApprovalCheck(StormX, 1800, Bonus = Cnt):
                        $ StormX.FaceChange("smile", 1)
                        if StormX.Love >= StormX.Obed:
                            ch_s "Наверное, я смогу с этим смириться."
                        elif StormX.Obed >= StormX.Inbt:
                            ch_s "Если ты этого хочешь."
                        else:
                            ch_s "Хорошо."
                        ch_s "Спроси ее и расскажи мне утром, что она ответила."
                else:
                        $ StormX.FaceChange("angry", 1)
                        ch_s "Да, пожалуй, это так похоже на нее, но я не собираюсь делиться."
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
                if not ApprovalCheck(StormX, 1800, Bonus = -Cnt): #checks if Storm likes you more than the other girl
                        $ StormX.FaceChange("angry", 1)
                        if not ApprovalCheck(StormX, 1800):
                                ch_s "Это причинит боль нам обеим."
                        else:
                                ch_s "Не стоит, это ниже твоего достоинства."
                        $ renpy.pop_call()
                else:
                        $ StormX.FaceChange("smile", 1)
                        if StormX.Love >= StormX.Obed:
                                ch_s "Пожалуй, я смогу с этим жить. . ."
                        elif StormX.Obed >= StormX.Inbt:
                                ch_s "Если ты этого хочешь."
                        else:
                                ch_s "Хорошо."
                        $ StormX.Traits.append("downlow")

        "Я могу порвать с ней.":
                    $ StormX.FaceChange("sad")
                    ch_s "Тогда отложим наш разговор на потом."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ StormX.FaceChange("sad")
                    ch_s "Очень зря."
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ StormX.FaceChange("sad")
                    ch_s "Очень зря."
                    $ renpy.pop_call()

    return


label Storm_About(Check=0): #rkeljsvg
    if Check not in TotalGirls:
            ch_s "Это кто?"
            return
    ch_s "Что я о ней думаю? Что ж. . ."
    if Check == RogueX:
            if "poly Rogue" in StormX.Traits:
                ch_s "Мы наслаждаемся обществом друг друга. . ."
            elif StormX.LikeRogue >= 900:
                ch_s "У нее прекрасная фигура . ."
            elif StormX.LikeRogue >= 800:
                ch_s "Она замечательный человек. . ."
            elif StormX.LikeRogue >= 700:
                ch_s "Она довольно трудолюбива."
            elif StormX.LikeRogue >= 600:
                ch_s "Она милая."
            elif StormX.LikeRogue >= 500:
                ch_s "Я часто пересекаюсь с ней."
            elif StormX.LikeRogue >= 400:
                ch_s "Я бы предпочла не говорить о ней."
            elif StormX.LikeRogue >= 300:
                ch_s "Я ненавижу ее."
            else:
                ch_s "Она сучка."
    elif Check == KittyX:
            if "poly Kitty" in StormX.Traits:
                ch_s "Мы наслаждаемся обществом друг друга. . ."
            elif StormX.LikeKitty >= 900:
                ch_s "У нее такая миниатюрная фигурка. . ."
            elif StormX.LikeKitty >= 800:
                ch_s "Она замечательный человек. . ."
            elif StormX.LikeKitty >= 700:
                ch_s "Она очень внимательна на занятиях."
            elif StormX.LikeKitty >= 600:
                ch_s "Она трудолюбива."
            elif StormX.LikeKitty >= 500:
                ch_s "Она наша студентка, верно?"
            elif StormX.LikeKitty >= 400:
                ch_s "Я бы предпочла не говорить о ней."
            elif StormX.LikeKitty >= 300:
                ch_s "Мне она ужасно не нравится."
            else:
                ch_s "Она сучка."
    elif Check == EmmaX:
            if "poly Emma" in StormX.Traits:
                ch_s "Мы наслаждаемся обществом друг друга. . ."
            elif StormX.LikeEmma >= 900:
                ch_s "Она очень фигуристая . ."
            elif StormX.LikeEmma >= 800:
                ch_s "Я полюбила ее компанию. . ."
            elif StormX.LikeEmma >= 700:
                ch_s "Она прекрасный педагог."
            elif StormX.LikeEmma >= 600:
                ch_s "Я не против разделить с ней занятия."
            elif StormX.LikeEmma >= 500:
                ch_s "Она нормальная."
            elif StormX.LikeEmma >= 400:
                ch_s "Я бы хотела видеться с ней поменьше."
            elif StormX.LikeEmma >= 300:
                ch_s "Ей нужно держаться подальше от моей головы."
            else:
                ch_s "Она сучка."
    elif Check == LauraX:
            if "poly Laura" in StormX.Traits:
                ch_s "Мы наслаждаемся обществом друг друга. . ."
            elif StormX.LikeLaura >= 900:
                ch_s "У нее прекрасная фигура . ."
            elif StormX.LikeLaura >= 800:
                ch_s "Она замечательный человек. . . как выяснилось."
            elif StormX.LikeLaura >= 700:
                ch_s "Из нее довольно сильный боец."
            elif StormX.LikeLaura >= 600:
                ch_s "Она агрессивна."
            elif StormX.LikeLaura >= 500:
                ch_s "Я часто пересекаюсь с ней."
            elif StormX.LikeLaura >= 400:
                ch_s "Я бы предпочла не говорить о ней."
            elif StormX.LikeLaura >= 300:
                ch_s "Я ненавижу ее."
            else:
                ch_s "Она сучка."
    elif Check == JeanX:
            if "poly Jean" in StormX.Traits:
                ch_s "Мы наслаждаемся обществом друг друга. . ."
            elif StormX.LikeJean >= 900:
                ch_s "У нее прекрасная фигура . ."
            elif StormX.LikeJean >= 800:
                ch_s "Она специфичный человек. . ."
            elif StormX.LikeJean >= 700:
                ch_s "Она. . . старается."
            elif StormX.LikeJean >= 600:
                ch_s "Я привыкла к ней."
            elif StormX.LikeJean >= 500:
                ch_s "Она может быть трудной."
            elif StormX.LikeJean >= 400:
                ch_s "От нее много хлопот."
            elif StormX.LikeJean >= 300:
                ch_s "Она мне очень не нравится."
            else:
                ch_s "Она сучка."
    elif Check == JubesX:
            if "poly Jubes" in StormX.Traits:
                ch_s "Мы наслаждаемся обществом друг друга. . ."
            elif StormX.LikeJubes >= 900:
                ch_s "У нее прекрасная фигура . ."
            elif StormX.LikeJubes >= 800:
                ch_s "Она замечательный человек. . ."
            elif StormX.LikeJubes >= 700:
                ch_s "Она очень внимательна на занятиях."
            elif StormX.LikeJubes >= 600:
                ch_s "Она трудолюбива."
            elif StormX.LikeJubes >= 500:
                ch_s "Она наша студентка, верно?"
            elif StormX.LikeJubes >= 400:
                ch_s "Она немного кусачая."
            elif StormX.LikeJubes >= 300:
                ch_s "Мне она ужасно не нравится."
            else:
                ch_s "Она сучка."
    elif Check == GwenX:
            if "poly Gwen" in StormX.Traits:
                ch_s "Мы наслаждаемся обществом друг друга. . ."
            elif StormX.LikeGwen >= 900:
                ch_s "Она очень. . . увлеченная. . ."
            elif StormX.LikeGwen >= 800:
                ch_s "Она замечательный человек. . ."
            elif StormX.LikeGwen >= 700:
                ch_s "Она очень внимательна на занятиях."
            elif StormX.LikeGwen >= 600:
                ch_s "Она трудолюбива."
            elif StormX.LikeGwen >= 500:
                ch_s "Я часто пересекаюсь с ней. . ."
            elif StormX.LikeGwen >= 400:
                ch_s "Я считаю, что она слишком часто смотрит на меня. . ."
            elif StormX.LikeGwen >= 300:
                ch_s "Я не хочу плохо о ней говорить."
            else:
                ch_s "Она сучка."
    elif Check == BetsyX:
            if "poly Betsy" in StormX.Traits:
                ch_s "Мы наслаждаемся обществом друг друга. . ."
            elif StormX.LikeBetsy >= 900:
                ch_s "У нее прекрасная фигура . ."
            elif StormX.LikeBetsy >= 800:
                ch_s "Она замечательный человек. . ."
            elif StormX.LikeBetsy >= 700:
                ch_s "Она очень внимательна на занятиях."
            elif StormX.LikeBetsy >= 600:
                ch_s "Она трудолюбива."
            elif StormX.LikeBetsy >= 500:
                ch_s "Она учится у нас, верно?"
            elif StormX.LikeBetsy >= 400:
                ch_s "Я бы предпочла не говорить о ней."
            elif StormX.LikeBetsy >= 300:
                ch_s "Она мне сильно не нравится."
            else:
                ch_s "Она сучка."
    elif Check == DoreenX:
            if "poly Doreen" in StormX.Traits:
                ch_s "Мы наслаждаемся обществом друг друга. . ."
            elif StormX.LikeDoreen >= 900:
                ch_s "Она очень. . . энергичная. . ."
            elif StormX.LikeDoreen >= 800:
                ch_s "Она замечательный человек. . ."
            elif StormX.LikeDoreen >= 700:
                ch_s "Она -очень- внимательна на занятиях."
            elif StormX.LikeDoreen >= 600:
                ch_s "Она трудолюбива."
            elif StormX.LikeDoreen >= 500:
                ch_s "Я рада, что мы нашли для нее место. . ."
            elif StormX.LikeDoreen >= 400:
                ch_s "Я редко с ней. . . встречаюсь. . ."
            elif StormX.LikeDoreen >= 300:
                ch_s "Я не хочу говорить о ней плохо."
            else:
                ch_s "Она сучка."
    elif Check == WandaX:
            if "poly Wanda" in StormX.Traits:
                ch_s "Мы наслаждались обществом друг друга. . ."
            elif StormX.LikeWanda >= 900:
                ch_s "У нее прекрасная фигура. . ."
            elif StormX.LikeWanda >= 800:
                ch_s "Она прекрасный человек. . ."
            elif StormX.LikeWanda >= 700:
                ch_s "Она очень трудолюбива."
            elif StormX.LikeWanda >= 600:
                ch_s "Она милая."
            elif StormX.LikeWanda >= 500:
                ch_s "Я пару раз ее видела."
            elif StormX.LikeWanda >= 400:
                ch_s "Я бы предпочла не говорить о ней."
            elif StormX.LikeWanda >= 300:
                ch_s "Я ненавижу ее."
            else:
                ch_s "Она ведьма."
    else:
                ch_s "Я бы предпочла не говорить на эту тему."
    return
#End Storm_AboutEmma

label Storm_Monogamy: #rkeljs
        #called from Storm_Settings to ask her not to hook up with other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in StormX.Traits:
                    if StormX.Thirst >= 60 and not ApprovalCheck(StormX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ StormX.FaceChange("sly",1)
                            if "mono" not in StormX.DailyActions:
                                    $ StormX.Statup("Obed", 90, -2)
                            ch_s "У меня есть потребности, которые должны быть удовлетворены. . ."
                            return
                    elif ApprovalCheck(StormX, 1200, "LO", TabM=0) and StormX.Love >= StormX.Obed:
                            #she cares
                            $ StormX.FaceChange("sly",1)
                            if "mono" not in StormX.DailyActions:
                                    $ StormX.Statup("Love", 90, 1)
                            ch_s "Не думала, что ты ревнивый человек."
                            ch_s "Хорошо, я удовлетворю твою просьбу. . . пока."
                    elif ApprovalCheck(StormX, 700, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Хорошо."
                    else:
                            #she doesn't care
                            $ StormX.FaceChange("sly",1)
                            ch_s "Нет, у меня есть потребности."
                            return
                    if "mono" not in StormX.DailyActions:
                            $ StormX.Statup("Obed", 90, 3)
                    $ StormX.AddWord(1,0,"mono") #Daily
                    $ StormX.Traits.append("mono")
            "Не встречайся с другими девушками." if "mono" not in StormX.Traits:
                    if ApprovalCheck(StormX, 900, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Если ты так этого хочешь."
                    elif StormX.Thirst >= 60 and not ApprovalCheck(StormX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ StormX.FaceChange("sly",1)
                            if "mono" not in StormX.DailyActions:
                                    $ StormX.Statup("Obed", 90, -2)
                            ch_s "У меня есть потребности, которые должны быть удовлетворены. . ."
                            return
                    elif ApprovalCheck(StormX, 600, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Хорошо."
                    elif ApprovalCheck(StormX, 1400, "LO", TabM=0):
                            #she cares
                            $ StormX.FaceChange("sly",1)
                            ch_s "Осторожней подбирай слова, но я обдумаю твою просьбу."
                    else:
                            #she doesn't care
                            $ StormX.FaceChange("sly",1,Brows="confused")
                            ch_s "Тебе стоит следить за своим тоном."
                            return
                    if "mono" not in StormX.DailyActions:
                            $ StormX.Statup("Obed", 90, 3)
                    $ StormX.AddWord(1,0,"mono") #Daily
                    $ StormX.Traits.append("mono")
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in StormX.Traits:
                    if ApprovalCheck(StormX, 700, "O", TabM=0):
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s ". . . тогда ладно."
                    elif ApprovalCheck(StormX, 800, "L", TabM=0):
                            $ StormX.FaceChange("sly",1)
                            ch_s "Хорошо. . ."
                    else:
                            $ StormX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in StormX.DailyActions:
                                    $ StormX.Statup("Love", 90, -2)
                            ch_s "Похоже, у меня появились кое-какие планы на выходные."
                    if "mono" not in StormX.DailyActions:
                            $ StormX.Statup("Obed", 90, 3)
                    if "mono" in StormX.Traits:
                            $ StormX.Traits.remove("mono")
                    $ StormX.AddWord(1,0,"mono") #Daily
            "Неважно.":
                pass
        return

# end Storm monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Storm_Jumped: #rkeljs
        #called from Storm_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ StormX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_s "Да?"
            "На будущее, можешь сначала спрашивать?" if "chill" not in StormX.Traits:
                    if StormX.Thirst >= 60 and not ApprovalCheck(StormX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ StormX.FaceChange("sly",1)
                            if "chill" not in StormX.DailyActions:
                                    $ StormX.Statup("Obed", 90, -2)
                            if not Player.Male:
                                ch_s "Я бы так и сделала, если бы ты приходила ко мне почаще. . ."
                            else:
                                ch_s "Я бы так и сделала, если бы ты приходил ко мне почаще. . ."
                            return
                    elif ApprovalCheck(StormX, 1000, "LO", TabM=0) and StormX.Love >= StormX.Obed:
                            #she cares
                            $ StormX.FaceChange("surprised",1)
                            if "chill" not in StormX.DailyActions:
                                    $ StormX.Statup("Love", 90, 1)
                            ch_s "Прости, но у меня есть потребности. . ."
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Однако я постораюсь исправиться. . ."
                    elif ApprovalCheck(StormX, 500, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Я сожалею об этом. . ."
                    else:
                            #she doesn't care
                            $ StormX.FaceChange("sly",1)
                            ch_s "Я буду брать то, что мне нужно."
                            return
                    if "chill" not in StormX.DailyActions:
                            $ StormX.Statup("Obed", 90, 3)
                    $ StormX.AddWord(1,0,"chill") #Daily
                    $ StormX.Traits.append("chill")
            "Больше так не делай." if "chill" not in StormX.Traits:
                    if ApprovalCheck(StormX, 800, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Хорошо."
                    elif StormX.Thirst >= 60 and not ApprovalCheck(StormX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ StormX.FaceChange("sly",1)
                            if "chill" not in StormX.DailyActions:
                                    $ StormX.Statup("Obed", 90, -2)
                            if not Player.Male:
                                ch_s "Я бы к тебе не приставала, если бы ты приходила ко мне почаще. . ."
                            else:
                                ch_s "Я бы к тебе не приставала, если бы ты приходил ко мне почаще. . ."
                            return
                    elif ApprovalCheck(StormX, 400, "O", TabM=0):
                            #she is obedient
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Хорошо. . ."
                    elif ApprovalCheck(StormX, 500, "LO", TabM=0) and not ApprovalCheck(StormX, 500, "I", TabM=0):
                            #she cares
                            $ StormX.FaceChange("sly",1)
                            ch_s "Следи за своим языком."
                            ch_s "Но ладно, я постараюсь держать свои потребности под контролем. . ."
                    else:
                            #she doesn't care
                            $ StormX.FaceChange("sly",1)
                            ch_s "Я буду брать то, что мне нужно."
                            return
                    if "chill" not in StormX.DailyActions:
                            $ StormX.Statup("Obed", 90, 3)
                    $ StormX.AddWord(1,0,"chill") #Daily
                    $ StormX.Traits.append("chill")
            "Делай что хочешь.":
                    if ApprovalCheck(StormX, 800, "L", TabM=0):
                            $ StormX.FaceChange("sly",1)
                            ch_s "Приму к сведению. . ."
                    elif ApprovalCheck(StormX, 700, "O", TabM=0):
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            ch_s "Хорошо. . ."
                    else:
                            $ StormX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in StormX.DailyActions:
                                    $ StormX.Statup("Love", 90, -2)
                            ch_s "Конечно, если это потребуется."
                    if "chill" not in StormX.DailyActions:
                            $ StormX.Statup("Obed", 90, 3)
                    if "chill" in StormX.Traits:
                            $ StormX.Traits.remove("chill")
                    $ StormX.AddWord(1,0,"chill") #Daily
            "Эм, неважно.":
                pass
        return

# end Storm jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start Storm hungry //////////////////////////////////////////////////////////
label Storm_Hungry:#rkeljs
    if StormX.Chat[3]:
        ch_s "[[облизывает губы] я бы хотела попробовать еще раз. . ."
    elif StormX.Chat[2]:
        ch_s "Мне очень понравилась твоя сыворотка."
    else:
        ch_s "[[облизывает губы] Мне очень нравится твой вкус. . ."
    $ StormX.Traits.append("hungry")
return


# end Storm hungry //////////////////////////////////////////////////////////

# Storm Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Storm_SexChat:#rkeljs
    $ Line = "Да? Что ты хочешь обсудить?" if not Line else Line
    while True:
            menu:
                ch_s "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in StormX.DailyActions:
                        ch_s "Мы уже говорили об этом."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "sex":
                                            $ StormX.Statup("Lust", 80, 5)
                                            if not Player.Male:
                                                ch_s "Да, ты уже говорила."
                                            else:
                                                ch_s "Да, ты уже говорил."
                                        elif StormX.Favorite == "sex":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 10)
                                            ch_s "Мне тоже нравится. . ."
                                        elif StormX.Sex >= 5:
                                            ch_s "Несомненно, это приятно. . ."
                                        elif not StormX.Sex:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "И кто тебя трахает?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Да. . . эм. . . это неплохо. . ."
                                        $ StormX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "anal":
                                            $ StormX.Statup("Lust", 80, 5)
                                            if not Player.Male:
                                                ch_s "Да, ты уже говорила."
                                            else:
                                                ch_s "Да, ты уже говорил."
                                        elif StormX.Favorite == "anal":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 10)
                                            ch_s "Мне тоже нравится. . ."
                                        elif StormX.Anal >= 10:
                                            ch_s "Несомненно, это приятно. . ."
                                        elif not StormX.Anal:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "И кто тебя трахает?"
                                        else:
                                            $ StormX.FaceChange("bemused",Eyes="side")
                                            ch_s "Да. . . эм. . . это неплохо. . ."
                                        $ StormX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "blow":
                                            $ StormX.Statup("Lust", 80, 3)
                                            ch_s "Да, ты уже говорил."
                                        elif StormX.Favorite == "blow":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Не могу не согласиться. . ."
                                        elif StormX.Blow >= 10:
                                            ch_s "Ты очень вкусный. . ."
                                        elif not StormX.Blow:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "Кто сосет твой пенис?!"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Я. . . немного привыкаю к вкусу. . ."
                                        $ StormX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "cun":
                                            $ StormX.Statup("Lust", 80, 3)
                                            ch_s "Да, ты уже говорила."
                                        elif StormX.Favorite == "cun":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Не могу не согласиться. . ."
                                        elif StormX.CUN >= 10:
                                            ch_s "Ты очень вкусная. . ."
                                        elif not StormX.CUN:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "Кто вылизывает твою киску?!"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Я. . . понемногу привыкаю к ее вкусу. . ."
                                        $ StormX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "titjob":
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Да, ты уже говорил."
                                        elif StormX.Favorite == "titjob":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 7)
                                            ch_s "Мне тоже нравится. . ."
                                        elif StormX.Tit >= 10:
                                            ch_s "Несомненно, это приятно. . ."
                                        elif not StormX.Tit:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "И кто же дрочит тебе сиськами?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Да. . . эм. . . это неплохо. . ."
                                            $ StormX.Statup("Love", 80, 5)
                                            $ StormX.Statup("Inbt", 50, 10)
                                        $ StormX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "foot":
                                            $ StormX.Statup("Lust", 80, 5)
                                            if not Player.Male:
                                                ch_s "Да, ты уже говорила."
                                            else:
                                                ch_s "Да, ты уже говорил."
                                        elif StormX.Favorite == "foot":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 7)
                                            ch_s "Мне тоже нравится. . ."
                                        elif StormX.Foot >= 10:
                                            ch_s "Мне это тоже нравится . . ."
                                        elif not StormX.Foot:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "И кто же играется ножками с тобой?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Да. . . эм. . . это неплохо. . ."
                                        $ StormX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "hand":
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Да, ты уже говорил."
                                        elif StormX.Favorite == "hand":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 7)
                                            ch_s "Мне тоже нравится. . ."
                                        elif StormX.Hand >= 10:
                                            ch_s "Мне это тоже нравится . . ."
                                        elif not StormX.Hand:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "И кто же передергивает тебе?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Да. . . эм. . . это неплохо. . ."
                                        $ StormX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "finger":
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Да, ты уже говорила."
                                        elif StormX.Favorite == "finger":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 7)
                                            ch_s "Мне тоже нравится. . ."
                                        elif StormX.Finger >= 10:
                                            ch_s "Мне это тоже нравится . . ."
                                        elif not StormX.Finger:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "И кто же ласкает твою киску?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Да. . . эм. . . это неплохо. . ."
                                        $ StormX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = StormX.FondleB + StormX.FondleT + StormX.SuckB + StormX.Hotdog
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "fondle":
                                            $ StormX.Statup("Lust", 80, 3)
                                            if not Player.Male:
                                                ch_s "Да, ты уже говорила."
                                            else:
                                                ch_s "Да, ты уже говорил."
                                        elif StormX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Я и сама не против. . ."
                                        elif Cnt >= 10:
                                            ch_s "Несомненно, это приятно. . ."
                                        elif not Cnt:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "И кто же позволяет тебе себя лапать?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Мне очень нравятся эти ощущения. . ."
                                        $ StormX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ StormX.FaceChange("sly")
                                        if StormX.PlayerFav == "kiss you":
                                            $ StormX.Statup("Love", 90, 3)
                                            if not Player.Male:
                                                ch_s "Да, ты уже говорила."
                                            else:
                                                ch_s "Да, ты уже говорил."
                                        elif StormX.Favorite == "kiss you":
                                            $ StormX.Statup("Love", 90, 5)
                                            $ StormX.Statup("Lust", 80, 5)
                                            ch_s "Мне тоже нравится. . ."
                                        elif StormX.Kissed >= 10:
                                            ch_s "Несомненно, это приятно. . ."
                                        elif not StormX.Kissed:
                                            $ StormX.FaceChange("perplexed")
                                            ch_s "И кого это ты целуешь?"
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            ch_s "Мне тоже нравится целовать тебя. . ."
                                        $ StormX.PlayerFav = "kiss you"

                        $ StormX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(StormX, 800):
                                        $ StormX.FaceChange("perplexed")
                                        ch_s ". . . Я бы предпочла не говорить."
                                else:
                                        if StormX.SEXP >= 50:
                                            $ StormX.FaceChange("sly")
                                            if not Player.Male:
                                                ch_s "Ты должна быть в курсе. . ."
                                            else:
                                                ch_s "Ты должен быть в курсе. . ."
                                        else:
                                            $ StormX.FaceChange("bemused")
                                            $ StormX.Eyes = "side"
                                            ch_s "Что ж. . ."


                                        if not StormX.Favorite or StormX.Favorite == "kiss you":
                                                ch_s "Поцелуи?"
                                        elif StormX.Favorite == "anal":
                                                ch_s "Пожалуй, анал."
                                        elif StormX.Favorite == "lick ass":
                                                ch_s "Когда ты вылизываешь мою попку."
                                        elif StormX.Favorite == "insert ass":
                                                ch_s "Наверное, когда ты трахаешь пальцем меня в попку."
                                        elif StormX.Favorite == "sex":
                                                ch_s "Больше всего мне нравится обычный секс."
                                        elif StormX.Favorite == "lick pussy":
                                                ch_s "Когда ты лижешь мою киску."
                                        elif StormX.Favorite == "fondle pussy":
                                                ch_s "Когда ты теребишь мою киску пальцем."
                                        elif StormX.Favorite == "blow":
                                                ch_s "Я обожаю вкус твоего члена."
                                        elif StormX.Favorite == "cun":
                                                ch_s "Я обожаю вкус твоей киски."
                                        elif StormX.Favorite == "tit":
                                                ch_s "Когда я использую свою грудь."
                                        elif StormX.Favorite == "foot":
                                                ch_s "Забавно ласкать тебя ножками."
                                        elif StormX.Favorite == "hand":
                                                ch_s "Мне нравится дрочить тебе."
                                        elif StormX.Favorite == "finger":
                                                ch_s "Мне нравится ласкать твою киску."
                                        elif StormX.Favorite == "hotdog":
                                                ch_s "Когда ты трешься о меня."
                                        elif StormX.Favorite == "suck breasts":
                                                ch_s "Когда ты сосешь мою грудь."
                                        elif StormX.Favorite == "fondle breasts":
                                                ch_s "Когда ты мнешь мою грудь."
                                        elif StormX.Favorite == "fondle thighs":
                                                ch_s "Когда ты растираешь мои бедра."
                                        else:
                                                ch_s "По правде говоря, я не уверена."

                                # End Storm's favorite things.

                "Не болтай так много во время секса." if "vocal" in StormX.Traits:
                        if "setvocal" in StormX.DailyActions:
                                $ StormX.FaceChange("perplexed")
                                if not Player.Male:
                                    ch_s "Я бы хотела, чтобы ты уже определилась."
                                else:
                                    ch_s "Я бы хотела, чтобы ты уже определился."
                        else:
                            if ApprovalCheck(StormX, 1000) and StormX.Obed <= StormX.Love:
                                $ StormX.FaceChange("bemused")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s "Я могу молчать, если ты хочешь."
                                $ StormX.Traits.remove("vocal")
                            elif ApprovalCheck(StormX, 700, "O"):
                                $ StormX.FaceChange("sadside")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s ". . ."
                                $ StormX.Traits.remove("vocal")
                            elif ApprovalCheck(StormX, 600):
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Love", 90, -3)
                                $ StormX.Statup("Obed", 50, -1)
                                $ StormX.Statup("Inbt", 90, 5)
                                ch_s "Даже не думай контролировать меня, [StormX.Petname]."
                            else:
                                $ StormX.FaceChange("angry")
                                $ StormX.Statup("Love", 90, -5)
                                $ StormX.Statup("Obed", 60, -3)
                                $ StormX.Statup("Inbt", 90, 10)
                                ch_s "Я не подчиняюсь твоим приказам, [StormX.Petname]."

                            $ StormX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in StormX.Traits:
                        if "setvocal" in StormX.DailyActions:
                                $ StormX.FaceChange("perplexed")
                                if not Player.Male:
                                    ch_s "Я бы хотела, чтобы ты уже определилась."
                                else:
                                    ch_s "Я бы хотела, чтобы ты уже определился."
                        else:
                            if ApprovalCheck(StormX, 1000) and StormX.Obed <= StormX.Love:
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Obed", 90, 2)
                                ch_s "Уверена, с этим я справлюсь. . ."
                                $ StormX.Traits.append("vocal")
                            elif ApprovalCheck(StormX, 700, "O"):
                                $ StormX.FaceChange("sadside")
                                $ StormX.Statup("Obed", 90, 2)
                                ch_s "Если ты так этого хочешь, [StormX.Petname]."
                                $ StormX.Traits.append("vocal")
                            elif ApprovalCheck(StormX, 600):
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Obed", 90, 3)
                                ch_s "Пожалуй, можно. . ."
                                $ StormX.Traits.append("vocal")
                            else:
                                $ StormX.FaceChange("angry")
                                $ StormX.Statup("Inbt", 90, 5)
                                ch_s ". . . Я бы предпочла этого не делать."

                            $ StormX.DailyActions.append("setvocal")
                        # End Storm Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in StormX.Traits:
                        if "initiative" in StormX.DailyActions:
                                $ StormX.FaceChange("perplexed")
                                if not Player.Male:
                                    ch_s "Я бы хотела, чтобы ты уже определилась."
                                else:
                                    ch_s "Я бы хотела, чтобы ты уже определился."
                        else:
                            if ApprovalCheck(StormX, 1200) and StormX.Obed <= StormX.Love:
                                $ StormX.FaceChange("bemused")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s "Позволить тебе взять на себя инициативу? Хорошо."
                                $ StormX.Traits.append("passive")
                            elif ApprovalCheck(StormX, 700, "O"):
                                $ StormX.FaceChange("sadside")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s "Я постараюсь сдержаться."
                                $ StormX.Traits.append("passive")
                            elif ApprovalCheck(StormX, 600):
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Love", 90, -3)
                                $ StormX.Statup("Obed", 50, -1)
                                $ StormX.Statup("Inbt", 90, 5)
                                ch_s "Посмотрим."
                            else:
                                $ StormX.FaceChange("angry")
                                $ StormX.Statup("Love", 90, -5)
                                $ StormX.Statup("Obed", 60, -3)
                                $ StormX.Statup("Inbt", 90, 10)
                                ch_s "Я не думаю, что должна это делать."

                            $ StormX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in StormX.Traits:
                        if "initiative" in StormX.DailyActions:
                                $ StormX.FaceChange("perplexed")
                                if not Player.Male:
                                    ch_s "Я бы хотела, чтобы ты уже определилась."
                                else:
                                    ch_s "Я бы хотела, чтобы ты уже определился."
                        else:
                            if ApprovalCheck(StormX, 1000) and StormX.Obed <= StormX.Love:
                                $ StormX.FaceChange("bemused")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s "Предпочитаешь, чтобы выбор был за мной? Хорошо."
                                $ StormX.Traits.remove("passive")
                            elif ApprovalCheck(StormX, 700, "O"):
                                $ StormX.FaceChange("sadside")
                                $ StormX.Statup("Obed", 90, 1)
                                ch_s "Если ты настаиваешь."
                                $ StormX.Traits.remove("passive")
                            elif ApprovalCheck(StormX, 600):
                                $ StormX.FaceChange("sly")
                                $ StormX.Statup("Obed", 90, 3)
                                ch_s "Посмотрим."
                                $ StormX.Traits.remove("passive")
                            else:
                                $ StormX.FaceChange("angry")
                                $ StormX.Statup("Inbt", 90, 5)
                                ch_s "Я бы предпочла этого не делать."

                            $ StormX.DailyActions.append("initiative")

                "О том, как ты накидываешься" if "jumped" in StormX.History:
                            call Storm_Jumped
                "О твоей мастурбации":
                            call NoFap(StormX)

                "Всегда носи вибратор" if "dailyvibe" not in StormX.Traits:
                        call Daily_Vibrator(StormX)
                "Перестань всегда носить вибратор" if "dailyvibe" in StormX.Traits:
                        ch_s "Хорошо. . ."
                        $ StormX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи анальную пробку" if "dailyplug" not in StormX.Traits:
                        call Daily_Plug(StormX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in StormX.Traits:
                        ch_s "Хорошо. . ."
                        $ StormX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Неважно" if Line == "Да? Что ты хочешь обсудить?":
                        return
                "На этом все" if Line != "Да? Что ты хочешь обсудить?":
                        return
            if Line == "Да? Что ты хочешь обсудить?":
                $ Line = "Что-нибудь еще?"
    return
# End Storm Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Storm Chitchat /////////////////// #Work in progress
label Storm_Chitchat(O=0, Options = ["default","default","default"]): #rkeljs
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if StormX not in Digits:
                if ApprovalCheck(StormX, 500, "L") or ApprovalCheck(StormX, 250, "I"):
                    ch_s "Ох, вот мой номер, на случай, если тебе понадобится помощь."
                    $ Digits.append(StormX)
                    return
                elif ApprovalCheck(StormX, 250, "O"):
                    ch_s "Вот мой номер, на случай, если тебе понадобиться связаться со мной."
                    $ Digits.append(StormX)
                    return

        if "hungry" not in StormX.Traits and (StormX.Swallow + StormX.Chat[2]) >= 10 and StormX.Loc == bg_current:  #She's swallowed a lot
                    call Storm_Hungry
                    return

        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(StormX, 800, "I")):
                    if StormX.Loc == bg_current and StormX.Thirst >= 30 and "refused" not in StormX.DailyActions and "quicksex" not in StormX.DailyActions:
                            $ StormX.FaceChange("sly",1)
                            ch_s "Я хочу спросить, не желаешь ли ты. . ."
                            ch_s "\"уединиться\" со мной?"
                            call Quick_Sex(StormX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in StormX.DailyActions:
#            $ Options.append("caught")
        if StormX.Event[0] and "key" not in StormX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in StormX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in StormX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in StormX.DailyActions:
            $ Options.append("corruption")

        if StormX.Date >= 1 and bg_current != "bg restaurant" :
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in StormX.DailyActions and "cheek" not in StormX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if StormX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
#        if "showered" in StormX.DailyActions:
#            #If you've caught Storm showering today
            $ Options.append("showercaught")
        if "fondle breasts" in StormX.DailyActions or "fondle pussy" in StormX.DailyActions or "fondle ass" in StormX.DailyActions:
            #If you've fondled Storm today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in StormX.Inventory and "256 Shades of Grey" in StormX.Inventory and "Avengers Tower Penthouse" in StormX.Inventory:
            #If you've given Storm the books
            if "book" not in StormX.Chat:
                $ Options.append("booked")
        if "lace bra" in StormX.Inventory or "lace panties" in StormX.Inventory:
            #If you've given Storm the lingerie
            if "lingerie" not in StormX.Chat:
                $ Options.append("lingerie")
        if StormX.Hand and Player.Male:
            #If Storm's given a handjob
            $ Options.append("handy")
        if StormX.Blow and Player.Male:
            #If Storm's given a blowjob
            $ Options.append("blow")
        if StormX.Swallow:
            #If Storm's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in StormX.DailyActions or "painted" in StormX.DailyActions:
            #If Storm's been facialed
            $ Options.append("facial")
        if StormX.Sleep:
            #If Storm's slept over
            $ Options.append("sleep")
        if (StormX.CreamP or StormX.CreamA) and Player.Male:
            #If Storm's been creampied
            $ Options.append("creampie")
        if StormX.Sex or StormX.Anal:
            #If Storm's been sexed
            $ Options.append("sexed")
        if StormX.Anal:
            #If Storm's been analed
            $ Options.append("anal")

        if "seenpeen" in StormX.History and Player.Male:
            $ Options.append("seenpeen")
        if "nudity" not in StormX.History:
            $ Options.append("nudity")
#        if "topless" in StormX.History:
#            $ Options.append("topless")
#        if "bottomless" in StormX.History:
#            $ Options.append("bottomless")

#        if not StormX.Chat[0] and StormX.Sex:
#            $ Options.append("virgin")

#        if (bg_current == "bg storm" or bg_current == "bg player") and "relationship" not in StormX.DailyActions:
#            if "lover" not in StormX.Petnames and ApprovalCheck(StormX, 900, "L"): # StormX.Event[6]
#                $ Options.append("lover?")
#            elif "sir" not in StormX.Petnames and ApprovalCheck(StormX, 500, "O"): # StormX.Event[7]
#                $ Options.append("sir?")
#            elif "daddy" not in StormX.Petnames and ApprovalCheck(StormX, 750, "L") and ApprovalCheck(StormX, 500, "O") and ApprovalCheck(StormX, 500, "I"): # StormX.Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in StormX.Petnames and ApprovalCheck(StormX, 900, "O"): # StormX.Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in StormX.Petnames and ApprovalCheck(StormX, 500, "I"): # StormX.Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in StormX.Petnames and ApprovalCheck(StormX, 900, "I"): # StormX.Event[10]
#                $ Options.append("fuckbuddy?")


        if not ApprovalCheck(StormX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ StormX.DailyActions.append("cologne chat")
        $ StormX.FaceChange("confused")
        ch_s "(нюх, нюх). . . Я чувствую запах. . . какой-то обезьяны . . ."
        $ StormX.FaceChange("sexy", 2)
        ch_s ". . . кстати, ты выглядишь очень привлекательно. . ."
    elif Options[0] == "purple":
        $ StormX.DailyActions.append("cologne chat")
        $ StormX.FaceChange("sly",1)
        ch_s "(нюх, нюх). . . что это за запах? . ."
        $ StormX.FaceChange("normal",0)
        ch_s ". . . Ты что-нибудь хочешь?"
    elif Options[0] == "corruption":
        $ StormX.DailyActions.append("cologne chat")
        $ StormX.FaceChange("confused")
        ch_s "(нюх, нюх). . . какой сильный запах. . ."
        $ StormX.FaceChange("angry")
        ch_s ". . . чувствую, я в большой опасности. . ."
        $ StormX.FaceChange("sly")

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in StormX.Chat:
                    ch_s "Нам следует быть осторожнее, когда мы вместе. . ."
                    if not ApprovalCheck(StormX, 500, "I"):
                        ch_s "Не то, чтобы это должно нас остановить. . ."
            else:
                    ch_s "Я сожалею о том неприятном инциденте с участием Чарльза."
                    if not ApprovalCheck(StormX, 500, "I"):
                        ch_s "Пожалуй, нам следует избегать публичных действий."
                    else:
                        ch_s "Хотя мне понравились сопутствующие острые ощущения. . ."
                    $ StormX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if StormX.SEXP <= 15:
                ch_s "Я дала тебе этот ключ для удобства, не злоупотребляй его использованием . ."
            else:
                ch_s "Я дала тебе ключ, но ты никогда не заходишь ко мне в гости. . ."
            $ StormX.Chat.append("key")

#    elif Options[0] == "cheek":
#            #Storm's response to having her cheek touched.
#            ch_s "So,[StormX.Petname]. . .y'know how you[StormX.like]kinda just brushed my cheek before?"
#            ch_p "Yeah?  Was that okay?"
#            $ StormX.FaceChange("smile",1)
#            ch_s "More than just {i}okay{/i}."
#            $ StormX.Chat.append("cheek")


    elif Options[0] == "dated":
            #Storm's response to having gone on a date with the Player.
            ch_s "Мне понравилось наше свидание, мы обязательно должны когда-нибудь повторить."

    elif Options[0] == "kissed":
            #Storm's response to having been kissed by the Player.
            $ StormX.FaceChange("normal",1)
            ch_s "Знаешь, [StormX.Petname], а ты очень хорошо целуешься."
            menu:
                extend ""
                "Эй. . . Да я лучшая." if not Player.Male:
                        $ StormX.FaceChange("bemused",1,Eyes="leftside")
                        ch_s "Что ж, вполне возможно, что ты одна из лучших."
                        $ StormX.FaceChange("smile",1)
                        ch_s "Но мы сделаем из тебя самую лучшую. . ."
                "Эй. . . Да я лучший." if Player.Male:
                        $ StormX.FaceChange("bemused",1,Eyes="leftside")
                        ch_s "Что ж, вполне возможно, что ты один из лучших."
                        $ StormX.FaceChange("smile",1)
                        ch_s "Но мы сделаем из тебя самого лучшего. . ."
                "Ты правда так думаешь?":
                        ch_s "Я уверена. . ."
                        ch_s "Но мы могли бы еще поэкспериментировать. . ."

    elif Options[0] == "dangerroom":
            #Storm's response to Player working out in the Danger Room while Storm is present
            $ StormX.FaceChange("sly",1)
            if not Player.Male:
                ch_s "Послушай, [StormX.Petname]. Я видела, как ты занималась в комнате Опасности."
            else:
                ch_s "Послушай, [StormX.Petname]. Я видела, как ты занимался в комнате Опасности."
            ch_s "Тебе лучше держаться поближе к \"танку\", во избежание ранений. . ."
    elif Options[0] == "nudity":
            #Storm's response to Player asking about nudity.
            if not Player.Male:
                ch_p "Я заметила, что ты ходишь голой намного чаще, чем другие."
            else:
                ch_p "Я заметил, что ты ходишь голой намного чаще, чем другие."
            call Storm_Nudity

#    elif Options[0] == "showercaught":
#            #Storm's response to being caught in the shower.
#            if "shower" in StormX.Chat:
#                ch_s "You saw me taking a shower again. . ."
#            else:
#                ch_s "Do you make a habit of bursting into the showers?"
#                $ StormX.Chat.append("shower")
#                menu:
#                    extend ""
#                    "It was a total accident!  I promise!":
#                            $ StormX.Statup("Love", 50, 5)
#                            $ StormX.Statup("Love", 90, 2)
#                            if ApprovalCheck(StormX, 1200):
#                                $ StormX.FaceChange("sly",1)
#                                ch_s "I didn't mind."
#                            $ StormX.FaceChange("smile")
#                            ch_s "We all make mistakes."
#                    "Just with you.":
#                            $ StormX.Statup("Obed", 40, 5)
#                            if ApprovalCheck(StormX, 1000) or ApprovalCheck(StormX, 700, "L"):
#                                    $ StormX.Statup("Love", 90, 3)
#                                    $ StormX.FaceChange("sly",1)
#                                    ch_s "Hmm, I guess that's a compliment."
#                            else:
#                                    $ StormX.Statup("Love", 70, -5)
#                                    $ StormX.FaceChange("angry")
#                                    ch_s "I think I should be insulted."
#                    "Totally on purpose. I regret nothing.":
#                            if ApprovalCheck(StormX, 1200):
#                                    $ StormX.Statup("Love", 90, 3)
#                                    $ StormX.Statup("Obed", 70, 10)
#                                    $ StormX.Statup("Inbt", 50, 5)
#                                    $ StormX.FaceChange("sly",1)
#                                    ch_s "You seem to know what you want."
#                            elif ApprovalCheck(StormX, 800):
#                                    $ StormX.Statup("Obed", 60, 5)
#                                    $ StormX.Statup("Inbt", 50, 5)
#                                    $ StormX.FaceChange("perplexed",2)
#                                    ch_s "I guess you show initiative."
#                                    $ StormX.Blush = 1
#                            else:
#                                    $ StormX.Statup("Love", 50, -10)
#                                    $ StormX.Statup("Love", 80, -10)
#                                    $ StormX.Statup("Obed", 50, 10)
#                                    $ StormX.FaceChange("angry")
#                                    ch_s "That's a bit disturbing."

    elif Options[0] == "fondled":
            #Storm's response to being felt up.
            if StormX.FondleB + StormX.FondleP + StormX.FondleA >= 15:
                ch_s "Пожалуйста, прикасайся ко мне. . . иногда. . ."
            else:
                ch_s "Знаешь, ты можешь прикоснуться ко мне. . . если захочешь."

    elif Options[0] == "booked":
            #Storm's response after a Player gives her the books from the shop.
            if not Player.Male:
                ch_s "Я прочитала те книги, которые ты мне дала."
            else:
                ch_s "Я прочитала те книги, которые ты мне дал."
            menu:
                extend ""
                "Да? И как тебе?":
                        $ StormX.FaceChange("sly",2)
                        ch_s "Они. . .{i}интересные{/i}."
                "Хорошо. Пожалуй, ты могла бы чему-нибудь из них научиться.":
                        $ StormX.Statup("Love", 90, -3)
                        $ StormX.Statup("Obed", 70, 5)
                        $ StormX.Statup("Inbt", 50, 5)
                        $ StormX.FaceChange("angry")
                        ch_s "Что ж, не могу сказать, что не научилась кое-чему."
            $ StormX.Blush = 1
            $ StormX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Storm's response to being given lingerie.
            $ StormX.FaceChange("sly",2)
            if not Player.Male:
                ch_s "Мне понравилось то нижнее белье, которое ты купила для меня."
            else:
                ch_s "Мне понравилось то нижнее белье, которое ты купил для меня."
            $ StormX.Blush = 1
            $ StormX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Storm's response after giving the Player a handjob.
            $ StormX.FaceChange("sly",1)
            ch_s "На днях я думала о твоем члене в своей руке. . ."
            ch_s "Тебе понравилось?"
            $ StormX.Blush = 0

    elif Options[0] == "blow":
            if "blow" not in StormX.Chat:
                    #Storm's response after giving the Player a blowjob.
                    $ StormX.FaceChange("sly",2)
                    ch_s "Мне любопытно, понравился ли тебе минет от меня?"
                    menu:
                        extend ""
                        "Ты была великолепна.":
                                    $ StormX.Statup("Love", 90, 5)
                                    $ StormX.Statup("Inbt", 60, 10)
                                    $ StormX.FaceChange("normal",1)
                                    ch_s ". . . "
                                    $ StormX.FaceChange("sexy",1)
                                    ch_s "На что я и надеялась. . ."
                                    ch_s "Дай мне знать, если захочешь повторить. . ."
                        "Честно? Все было хорошо. . . но, думаю, тебе не помешает еще немного попрактиковаться.":
                                if ApprovalCheck(StormX, 300, "I") or not ApprovalCheck(StormX, 800):
                                    $ StormX.Statup("Love", 90, -5)
                                    $ StormX.Statup("Obed", 60, 10)
                                    $ StormX.Statup("Inbt", 50, 10)
                                    $ StormX.FaceChange("perplexed",1)
                                    ch_s "Ох? Что ж, мне жаль, что я не соответствовала твоим стандартам. . ."
                                else:
                                    $ StormX.Statup("Obed", 70, 15)
                                    $ StormX.Statup("Inbt", 50, 5)
                                    $ StormX.FaceChange("sexy",1)
                                    ch_s "Ох? Что ж, уверена, я смогу улучшить свои навыки. . ."
                        "Угу, если бы мне нравились стремные звуки и шкрябанье зубов по члену, но это далеко не так.":
                                    $ StormX.Statup("Love", 90, -10)
                                    $ StormX.Statup("Obed", 60, 10)
                                    $ StormX.FaceChange("angry",2)
                                    ch_s "Ох, тогда, полагаю, ты не будешь по этому скучать."
                    $ StormX.Blush = 1
                    $ StormX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["Знаешь, мне очень нравится вкус твоего члена.",
                            "Кажется, в прошлый раз я чуть не вывихнула челюсть.",
                            "Дай мне знать, если захочешь насладиться еще одним минетом.",
                            "Мммм. . . [Стучит языком по внутренней стороне щеки.]"])
                    ch_s "[Line]"

    elif Options[0] == "swallowed":
            #Storm's response after swallowing the Player's cum.
            if "swallow" in StormX.Chat:
                ch_s "Я бы хотела когда-нибудь попробовать тебя снова."
            else:
                ch_s "Так вот. . . в тот день. . ."
                if not Player.Male:
                    ch_s "Мне очень понравился вкус твоих соков."
                else:
                    ch_s "Мне очень понравился вкус твоей спермы."
                $ StormX.FaceChange("sly",1)
                ch_s "Это довольно удивительно, учитывая все обстоятельства."
                $ StormX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Storm's response after taking a facial from the Player.
            ch_s ". . .Я знаю, что это немного необычно, но. . ."
            $ StormX.FaceChange("sexy",2)
            ch_s "Мне так нравится, когда ты кончаешь мне на лицо. . ."
            $ StormX.Blush = 1

    elif Options[0] == "sleepover":
            #Storm's response after sleeping with the Player.
            ch_s "Мне очень понравилась та ночь."
            ch_s "Не часто удается поспать с кем-то рядом. . ."

    elif Options[0] == "creampie":
            #Another of Storm's responses after having sex with the Player.
            "[StormX.Name] подходит к вам вплотную и начинает шептать на ухо:"
            if not Player.Male:
                ch_s "Я все еще чувствую, как они. . . стекают по внутренней стороне моего бедра."
            else:
                ch_s "Я все еще чувствую, как она. . . стекает по внутренней стороне моего бедра."

    elif Options[0] == "sexed":
            #A final response from Storm after having sex with the Player.
            if not Player.Male:
                ch_s "Что ж. . . Ты должна знать. . ."
            else:
                ch_s "Что ж. . . Ты должен знать. . ."
            $ StormX.FaceChange("sexy",2)
            ch_s ". . .когда я. . . удовлетворяю свои потребности. . ."
            ch_s "Я представляю, что ты со мной. . ."
            $ StormX.Blush = 1

    elif Options[0] == "anal":
            #Storm's response after getting anal from the Player.
            $ StormX.FaceChange("sly")
            ch_s "Меня никогда не интересовал анальный секс."
            $ StormX.FaceChange("sexy",1)
            if not Player.Male:
                ch_s ". . . но ты заставила меня передумать."
            else:
                ch_s ". . . но ты заставил меня передумать."

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ StormX.FaceChange("sly",1, Eyes="leftside")
            ch_s "Ох, просто чтобы ты знал, меня очень впечатлил твое. . ."
            $ StormX.FaceChange("sly",2, Eyes="down")
            ch_s ". . . мужское достоинство. . ."
            $ StormX.FaceChange("bemused",1)
            $ StormX.Statup("Love", 50, 5)
            $ StormX.History.remove("seenpeen")
#    elif Options[0] == "topless": # first seen breasts skipped
#            ch_s "Hey, what'd you think of my tits?"
#            ch_s "Did you like what you saw?"
#            call Girl_First_TMenu
#            $ StormX.History.remove("topless")
#    elif Options[0] == "bottomless": # first seen pussy skipped
#            ch_s "Hey, what'd you think when you saw my pussy earlier?"
#            call Girl_First_BMenu
#            $ StormX.History.remove("bottomless")

#    elif Options[0] == "boyfriend?":
#        call Storm_BF
#    elif Options[0] == "lover?":
#        call Storm_Love
#    elif Options[0] == "sir?":
#        call Storm_Sub
#    elif Options[0] == "master?":
#        call Storm_Master
#    elif Options[0] == "sexfriend?":
#        call Storm_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Storm_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Storm_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Отойди от меня.",
                "Я не хочу тебя видеть.",
                "Держись подальше.",
                "Оставь меня."])
        ch_s "[Line]"

    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)
            if D20 == 1:
                    $ StormX.FaceChange("smile")
                    ch_s "Представь, что ты просыпаешься под яркий восход солнца, чувствуешь прохладный ветерок на своем лице и используешь силу молнии, чтобы зарядить себя на весь день."
                    ch_s "Вот так началось мое утро!"
            elif D20 == 2:
                    ch_s "На занятиях я призываю вас изучать различные точки зрения, точно так же, как я приспосабливаюсь к изменчивым ветрам и принимаю разнообразие погодных явлений во всем мире."
            elif D20 == 3:
                    ch_s "Будь то гроза, снегопад или слабый дождь, каждое погодное явление имеет свою собственную историю. Аналогичным образом, каждое занятие, которое мы рассматриваем, имеет свою уникальную историю."
            elif D20 == 4:
                    ch_s "Помни, что на погоду влияют различные факторы, подобно взаимодействию культур, идеологий и верований, которые формируют наше общество. Понимание этих связей имеет решающее значение."
            elif D20 == 5:
                    ch_s "В течение дня я постоянно отслеживаю погодные условия, точно так же, как вы должны анализировать различные источники, точки зрения и ссылки, чтобы сформировать всестороннее понимание любого предмета."
            elif D20 == 6:
                    $ StormX.FaceChange("smile")
                    ch_s "Сегодняшний день был весьма насыщен событиями. Когда я шла через кампус, я чувствовала электричество в воздухе, словно атмосфера готовилась к буре."
            elif D20 == 7:
                    ch_s "Лорна подошла ко мне после занятий, борясь с неуверенностью в себе. Я подбодрила ее, напомнив, что истинная сила заключается в принятии своих уникальных способностей."
            elif D20 == 8:
                    $ StormX.FaceChange("bemused")
                    ch_s "В перерывах между занятиями я нахожу тихое место для медитации и общения с природой. Очень важно поддерживать баланс внутри себя, особенно когда сталкиваешься с хаосом повседневной жизни."
            elif D20 == 9:
                    $ StormX.FaceChange("smile")
                    ch_s "Когда я покидала кампус, солнце пробилось сквозь облака, рассыпав по небу яркую радугу. Это напомнило мне о том, что, несмотря на трудности, с которыми мы сталкиваемся, всегда есть надежда. [[Джейсон Стетхем]"
            elif D20 == 10:
                    ch_s "Сегодня мы изучим захватывающую динамику атмосферного давления и его влияние на погодные условия."
            elif D20 == 11:
                    $ StormX.FaceChange("smile")
                    ch_s "Представь, что ты просыпаешься и чувствуешь, как легкий ветерок ласкает твое лицо, сопровождаемый бодрящим ароматом дождя."
                    ch_s "Это напоминает о тонком балансе между красотой природы и ее огромной силой."
            elif D20 == 12:
                    ch_s "Одним из самых ярких моментов моего дня было проведение эксперимента по изучению влияния скорости ветра на траекторию полета снарядов."
                    ch_s "Я вызвала порыв ветра и наблюдала, как он отклоняет предметы, демонстрируя концепцию аэродинамики."
            elif D20 == 13:
                    $ StormX.FaceChange("smile")
                    ch_s "Во время обеденного перерыва я нашла успокоение в своем мансардном саду, чувствуя ритм растений, реагирующих на мое присутствие."
                    ch_s "Это напомнило мне о сложной связи между природой и всеми живыми существами."
            elif D20 == 14:
                    $ StormX.FaceChange("smile")
                    ch_s "[KittyX.Name] подошла ко мне сегодня и засыпала меня вопросами. Видя ее энтузиазм и стремление учиться, я прониклась надеждой на будущее."
            elif D20 == 15:
                    ch_s "Я всегда призываю своих студентов проявлять любопытство и исследовать чудеса природы. Мы можем многому научиться, наблюдая и понимая сложный танец между стихиями."
            elif D20 == 16:
                    $ StormX.FaceChange("smile")
                    ch_s "Во время занятий на свежем воздухе мы наблюдали захватывающий закат, и я не могла не объяснить науку, стоящую за яркими цветами, и то, как на них влияют частицы в атмосфере."
                    ch_s "Красота природы и наука идут рука об руку."
            elif D20 == 17:
                    ch_s "Когда я шла по кампусу, ветер хлестал по деревьям, нашептывая древние сказания и тайны мира. Это напомнило мне о взаимосвязи всех живых существ.. . ."
            elif D20 == 18:
                    ch_s "Ранее я провела увлекательную дискуссию о символизме штормов в литературе и о том, как они отражают внутренние потрясения и конфликты персонажей."
                    ch_s "Удивительно, как погодные явления могут служить мощными метафорами."
            elif D20 == 19:
                    ch_s "Когда день подходил к концу, я стояла на улице и чувствовала на своей коже легкий дождь. Это напомнило мне о том, как важно найти мир внутри себя и соединиться с природой."
            elif D20 == 20:
                    $ StormX.FaceChange("smile")
                    ch_s "Я всегда с нетерпением жду встречи с тобой на занятиях. . ."
            else:
                    $ StormX.FaceChange("smile")
                    ch_s "Мне нравится общаться с тобой. . ."

    $ Line = 0
    return

# start Storm_Names//////////////////////////////////////////////////////////
label Storm_Names:     #rkeljs
    menu:
        ch_s "Ох? Как ты предпочитаешь, чтобы я тебя звала?"
        "Зови по инициалам.":
            $ StormX.Petname = Player.Name[:1]  #fix test this
            $ StormX.Petname_rod = Player.Name[:1]
            $ StormX.Petname_dat = Player.Name[:1]
            $ StormX.Petname_vin = Player.Name[:1]
            $ StormX.Petname_tvo = Player.Name[:1]
            $ StormX.Petname_pre = Player.Name[:1]
            ch_s "Поняла, [StormX.Petname]."
        "Зови меня по имени.":
            $ StormX.Petname = Player.Name
            $ StormX.Petname_rod = Player.Name_rod
            $ StormX.Petname_dat = Player.Name_dat
            $ StormX.Petname_vin = Player.Name_vin
            $ StormX.Petname_tvo = Player.Name_tvo
            $ StormX.Petname_pre = Player.Name_pre
            ch_s "Если ты этого хочешь, [StormX.Petname]."
        "Зови меня \"моя девушка\"." if "boyfriend" in StormX.Petnames and not Player.Male:
            $ StormX.Petname = "моя девушка"
            $ StormX.Petname_rod = "моей девушки"
            $ StormX.Petname_dat = "моей девушке"
            $ StormX.Petname_vin = "мою девушку"
            $ StormX.Petname_tvo = "моей девушкой"
            $ StormX.Petname_pre = "моей девушке"
            ch_s "Хорошо, [StormX.Petname]."
        "Зови меня \"мой парень\"." if "boyfriend" in StormX.Petnames and Player.Male:
            $ StormX.Petname = "мой парень"
            $ StormX.Petname_rod = "моего парня"
            $ StormX.Petname_dat = "моему парню"
            $ StormX.Petname_vin = "моего парня"
            $ StormX.Petname_tvo = "моим парнем"
            $ StormX.Petname_pre = "моем парне"
            ch_s "Хорошо, [StormX.Petname]."
        "Зови меня \"любимая\"." if "lover" in StormX.Petnames and not Player.Male:
            $ StormX.Petname = "любимая"
            $ StormX.Petname_rod = "любимой"
            $ StormX.Petname_dat = "любимой"
            $ StormX.Petname_vin = "любимую"
            $ StormX.Petname_tvo = "любимой"
            $ StormX.Petname_pre = "любимой"
            ch_s "С удовольствием, [StormX.Petname]."
        "Зови меня \"любимый\"." if "lover" in StormX.Petnames and Player.Male:
            $ StormX.Petname = "любимый"
            $ StormX.Petname_rod = "любимого"
            $ StormX.Petname_dat = "любимому"
            $ StormX.Petname_vin = "любимого"
            $ StormX.Petname_tvo = "любимым"
            $ StormX.Petname_pre = "любимом"
            ch_s "С удовольствием, [StormX.Petname]."
        "Зови меня \"возлюбленная\"." if "lover" in StormX.Petnames and not Player.Male:
            $ StormX.Petname = "возлюбленная"
            $ StormX.Petname_rod = "возлюбленной"
            $ StormX.Petname_dat = "возлюбленной"
            $ StormX.Petname_vin = "возлюбленную"
            $ StormX.Petname_tvo = "возлюбленной"
            $ StormX.Petname_pre = "возлюбленной"
            ch_s "С удовольствием, [StormX.Petname]."
        "Зови меня \"возлюбленный\"." if "lover" in StormX.Petnames and Player.Male:
            $ StormX.Petname = "возлюбленный"
            $ StormX.Petname_rod = "возлюбленного"
            $ StormX.Petname_dat = "возлюбленному"
            $ StormX.Petname_vin = "возлюбленного"
            $ StormX.Petname_tvo = "возлюбленным"
            $ StormX.Petname_pre = "возлюбленном"
            ch_s "С удовольствием, [StormX.Petname]."
        "Зови меня \"госпожа\"." if "sir" in StormX.Petnames and not Player.Male:
            $ StormX.Petname = "госпожа"
            $ StormX.Petname_rod = "госпожи"
            $ StormX.Petname_dat = "госпоже"
            $ StormX.Petname_vin = "госпожу"
            $ StormX.Petname_tvo = "госпожой"
            $ StormX.Petname_pre = "госпоже"
            ch_s "Да, [StormX.Petname]."
        "Зови меня \"господин\"." if "sir" in StormX.Petnames and Player.Male:
            $ StormX.Petname = "господин"
            $ StormX.Petname_rod = "господина"
            $ StormX.Petname_dat = "господину"
            $ StormX.Petname_vin = "господина"
            $ StormX.Petname_tvo = "господином"
            $ StormX.Petname_pre = "господине"
            ch_s "Да, [StormX.Petname]."
        "Зови меня \"хозяйка\"." if "master" in StormX.Petnames and not Player.Male:
            $ StormX.Petname = "хозяйка"
            $ StormX.Petname_rod = "хозяйки"
            $ StormX.Petname_dat = "хозяйке"
            $ StormX.Petname_vin = "хозяйку"
            $ StormX.Petname_tvo = "хозяйкой"
            $ StormX.Petname_pre = "хозяйке"
            ch_s "Как пожелаешь, [StormX.Petname]."
        "Зови меня \"хозяин\"." if "master" in StormX.Petnames and Player.Male:
            $ StormX.Petname = "хозяин"
            $ StormX.Petname_rod = "хозяина"
            $ StormX.Petname_dat = "хозяину"
            $ StormX.Petname_vin = "хозяина"
            $ StormX.Petname_tvo = "хозяином"
            $ StormX.Petname_pre = "хозяине"
            ch_s "Как пожелаешь, [StormX.Petname]."
        "Зови меня \"любовница\"." if "sex friend" in StormX.Petnames and not Player.Male:
            $ StormX.Petname = "любовница"
            $ StormX.Petname_rod = "любовницы"
            $ StormX.Petname_dat = "любовнице"
            $ StormX.Petname_vin = "любовницу"
            $ StormX.Petname_tvo = "любовницей"
            $ StormX.Petname_pre = "любовнице"
            ch_s "Довольно дерзко, [StormX.Petname]."
        "Зови меня \"любовник\"." if "sex friend" in StormX.Petnames and Player.Male:
            $ StormX.Petname = "любовник"
            $ StormX.Petname_rod = "любовника"
            $ StormX.Petname_dat = "любовнику"
            $ StormX.Petname_vin = "любовника"
            $ StormX.Petname_tvo = "любовником"
            $ StormX.Petname_pre = "любовнике"
            ch_s "Довольно дерзко, [StormX.Petname]."
        "Зови меня \"секс-партнерша\"." if "fuck buddy" in StormX.Petnames and not Player.Male:
            $ StormX.Petname = "секс-партнерша"
            $ StormX.Petname_rod = "секс-партнерши"
            $ StormX.Petname_dat = "секс-партнерше"
            $ StormX.Petname_vin = "секс-партнершу"
            $ StormX.Petname_tvo = "секс-партнершей"
            $ StormX.Petname_pre = "секс-партнерше"
            ch_s "Хорошо, [StormX.Petname]."
        "Зови меня \"секс-партнер\"." if "fuck buddy" in StormX.Petnames and Player.Male:
            $ StormX.Petname = "секс-партнер"
            $ StormX.Petname_rod = "секс-партнера"
            $ StormX.Petname_dat = "секс-партнеру"
            $ StormX.Petname_vin = "секс-партнера"
            $ StormX.Petname_tvo = "секс-партнером"
            $ StormX.Petname_pre = "секс-партнере"
            ch_s "Хорошо, [StormX.Petname]."
        "Зови меня \"мамочка\"." if "daddy" in StormX.Petnames and not Player.Male:
            $ StormX.Petname = "мамочка"
            $ StormX.Petname_rod = "мамочки"
            $ StormX.Petname_dat = "мамочке"
            $ StormX.Petname_vin = "мамочку"
            $ StormX.Petname_tvo = "мамочкой"
            $ StormX.Petname_pre = "мамочке"
            ch_s "Ладно, [StormX.Petname]."
        "Зови меня \"папочка\"." if "daddy" in StormX.Petnames and Player.Male:
            $ StormX.Petname = "папочка"
            $ StormX.Petname_rod = "папочки"
            $ StormX.Petname_dat = "папочке"
            $ StormX.Petname_vin = "папочку"
            $ StormX.Petname_tvo = "папочкой"
            $ StormX.Petname_pre = "папочке"
            ch_s "Ладно, [StormX.Petname]."
        "Неважно.":
            return
    return
# end Storm_Names//////////////////////////////////////////////////////////

label Storm_Pet: #rkeljs
    while True:
        menu:
            extend ""
            "Обходительно":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "Ороро.":
                        $ StormX.Pet = "Ороро"
                        $ StormX.Pet_rod = "Ороро"
                        $ StormX.Pet_dat = "Ороро"
                        $ StormX.Pet_vin = "Ороро"
                        $ StormX.Pet_tvo = "Ороро"
                        $ StormX.Pet_pre = "Ороро"
                        ch_s "Не вижу причин отказывать, [StormX.Petname]."
                    "Шторм.":
                        $ StormX.Pet = "Шторм"
                        $ StormX.Pet_rod = "Шторм"
                        $ StormX.Pet_dat = "Шторм"
                        $ StormX.Pet_vin = "Шторм"
                        $ StormX.Pet_tvo = "Шторм"
                        $ StormX.Pet_pre = "Шторм"
                        ch_s "Не вижу причин отказывать, [StormX.Petname]."
                    "Штормик.":
                        if ApprovalCheck(StormX, 600):
                            $ StormX.FaceChange("smile", 1)
                            $ StormX.Pet = "Штормик"
                            $ StormX.Pet_rod = "Штормик"
                            $ StormX.Pet_dat = "Штормик"
                            $ StormX.Pet_vin = "Штормик"
                            $ StormX.Pet_tvo = "Штормик"
                            $ StormX.Pet_pre = "Штормик"
                            ch_s "Не вижу причин отказывать, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("normal", 1)
                            ch_s "Пожалуй, мы не настолько близки, [StormX.Petname]."
                    "'Ро.":
                        if ApprovalCheck(StormX, 700):
                            $ StormX.FaceChange("smile", 1)
                            $ StormX.Pet = "'Ро"
                            $ StormX.Pet_rod = "'Ро"
                            $ StormX.Pet_dat = "'Ро"
                            $ StormX.Pet_vin = "'Ро"
                            $ StormX.Pet_tvo = "'Ро"
                            $ StormX.Pet_pre = "'Ро"
                            ch_s "Не вижу причин отказаться, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("normal", 1)
                            ch_s "Пожалуй, мы не настолько близки, [StormX.Petname]."

                    "Мисс Манро." if "Ms. Munroe" in StormX.Names:
                        if ApprovalCheck(StormX, 700):
                            $ StormX.FaceChange("bemused", 1)
                            $ StormX.Pet = "Мисс Манро"
                            $ StormX.Pet_rod = "Мисс Манро"
                            $ StormX.Pet_dat = "Мисс Манро"
                            $ StormX.Pet_vin = "Мисс Манро"
                            $ StormX.Pet_tvo = "Мисс Манро"
                            $ StormX.Pet_pre = "Мисс Манро"
                            ch_s "Не вижу причин отказаться, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("normal", 1)
                            ch_s "Это слишком, [StormX.Petname]."


                    "\"моя девушка\".":
                        if "boyfriend" in StormX.Petnames:
                            $ StormX.Pet = "моя девушка"
                            $ StormX.Pet_rod = "моей девушки"
                            $ StormX.Pet_dat = "моей девушке"
                            $ StormX.Pet_vin = "мою девушку"
                            $ StormX.Pet_tvo = "моей девушкой"
                            $ StormX.Pet_pre = "моей девушке"
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "И это будет правдой, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry")
                            ch_s "Я НЕ твоя девушка, [StormX.Petname]."

                    "\"детка\".":
                        if "boyfriend" in StormX.Petnames or ApprovalCheck(StormX, 700, "L"):
                            $ StormX.Pet = "детка"
                            $ StormX.Pet_rod = "детки"
                            $ StormX.Pet_dat = "детке"
                            $ StormX.Pet_vin = "детку"
                            $ StormX.Pet_tvo = "деткой"
                            $ StormX.Pet_pre = "детке"
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "Я могу быть твоей деткой, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry")
                            ch_s "Я НЕ твоя детка, [StormX.Petname]."

                    "\"крошка\".":
                        if "boyfriend" in StormX.Petnames or ApprovalCheck(StormX, 600, "L"):
                            $ StormX.Pet = "крошка"
                            $ StormX.Pet_rod = "крошки"
                            $ StormX.Pet_dat = "крошке"
                            $ StormX.Pet_vin = "крошку"
                            $ StormX.Pet_tvo = "крошкой"
                            $ StormX.Pet_pre = "крошке"
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "Я могу быть твоей крошкой, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry")
                            ch_s "Я НЕ твоя крошка, [StormX.Petname]."

                    "\"малышка\".":
                        if "boyfriend" in StormX.Petnames or ApprovalCheck(StormX, 500, "L"):
                            $ StormX.Pet = "малышка"
                            $ StormX.Pet_rod = "малышки"
                            $ StormX.Pet_dat = "малышке"
                            $ StormX.Pet_vin = "малышку"
                            $ StormX.Pet_tvo = "малышкой"
                            $ StormX.Pet_pre = "малышке"
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "Мило, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry")
                            ch_s "Я не твоя малышка."


                    "\"милая\".":
                        if "boyfriend" in StormX.Petnames or ApprovalCheck(StormX, 600, "L"):
                            $ StormX.Pet = "милая"
                            $ StormX.Pet_rod = "милой"
                            $ StormX.Pet_dat = "милой"
                            $ StormX.Pet_vin = "милую"
                            $ StormX.Pet_tvo = "милой"
                            $ StormX.Pet_pre = "милой"
                            ch_s "Это так мило, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Полагаю, это перебор, [StormX.Petname]."

                    "\"секси\".":
                        if "lover" in StormX.Petnames or ApprovalCheck(StormX, 800):
                            $ StormX.Pet = "секси"
                            $ StormX.Pet_rod = "секси"
                            $ StormX.Pet_dat = "секси"
                            $ StormX.Pet_vin = "секси"
                            $ StormX.Pet_tvo = "секси"
                            $ StormX.Pet_pre = "секси"
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "Пожалуй, так оно и есть, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Ты переходишь черту, [StormX.Petname]."

                    "\"любимая\".":
                        if "lover" in StormX.Petnames or ApprovalCheck(StormX, 1200):
                            $ StormX.Pet = "любимая"
                            $ StormX.Pet_rod = "любимой"
                            $ StormX.Pet_dat = "любимой"
                            $ StormX.Pet_vin = "любимую"
                            $ StormX.Pet_tvo = "любимой"
                            $ StormX.Pet_pre = "любимой"
                            $ StormX.FaceChange("sexy", 1)
                            ch_s "Пожалуй, так оно и есть."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Я так не думаю, [StormX.Petname]."

                    "Назад":
                        pass

            "Грубо":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "\"рабыня\".":
                        if "master" in StormX.Petnames or ApprovalCheck(StormX, 850, "O"):
                            $ StormX.Pet = "рабыня"
                            $ StormX.Pet_rod = "рабыни"
                            $ StormX.Pet_dat = "рабыне"
                            $ StormX.Pet_vin = "рабыню"
                            $ StormX.Pet_tvo = "рабыней"
                            $ StormX.Pet_pre = "рабыне"
                            $ StormX.FaceChange("bemused", 1)
                            ch_s "Как пожелаешь, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Я никому не рабыня, [StormX.Petname]."

                    "\"питомец\".":
                        if "master" in StormX.Petnames or ApprovalCheck(StormX, 700, "O"):
                            $ StormX.Pet = "питомец"
                            $ StormX.Pet_rod = "питомце"
                            $ StormX.Pet_dat = "питомцу"
                            $ StormX.Pet_vin = "питомца"
                            $ StormX.Pet_tvo = "питомцем"
                            $ StormX.Pet_pre = "питомце"
                            $ StormX.FaceChange("bemused", 1)
                            ch_s "Можешь погладить меня, если хочешь, [StormX.Petname]."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Я не твой питомец, [StormX.Petname]."

                    "\"шлюха\".":
                        if "sex friend" in StormX.Petnames or ApprovalCheck(StormX, 900, "OI"):
                            $ StormX.Pet = "шлюха"
                            $ StormX.Pet_rod = "шлюхи"
                            $ StormX.Pet_dat = "шлюхе"
                            $ StormX.Pet_vin = "шлюху"
                            $ StormX.Pet_tvo = "шлюхой"
                            $ StormX.Pet_pre = "шлюхе"
                            $ StormX.FaceChange("sexy")
                            ch_s "Логично."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            $ StormX.Mouth = "surprised"
                            ch_s "Следи за языком."

                    "\"блядь\".":
                        if "fuckbuddy" in StormX.Petnames or ApprovalCheck(StormX, 1000, "OI"):
                            $ StormX.Pet = "блядь"
                            $ StormX.Pet_rod = "бляди"
                            $ StormX.Pet_dat = "бляде"
                            $ StormX.Pet_vin = "блядь"
                            $ StormX.Pet_tvo = "блядью"
                            $ StormX.Pet_pre = "бляде"
                            $ StormX.FaceChange("sly")
                            ch_s ". . ."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Лучше тебе меня не провоцировать. . ."

                    "\"сладкогрудая\".":
                        if "sex friend" in StormX.Petnames or ApprovalCheck(StormX, 1400):
                            $ StormX.Pet = "сладкогрудая"
                            $ StormX.Pet_rod = "сладкогрудой"
                            $ StormX.Pet_dat = "сладкогрудой"
                            $ StormX.Pet_vin = "сладкогрудую"
                            $ StormX.Pet_tvo = "сладкогрудой"
                            $ StormX.Pet_pre = "сладкогрудой"
                            $ StormX.FaceChange("sly", 1)
                            ch_s "Полагаю, это правда. . ."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "С чего ты вообще-."

                    "\"любовница\".":
                        if "sex friend" in StormX.Petnames or ApprovalCheck(StormX, 600, "I"):
                            $ StormX.Pet = "любовница"
                            $ StormX.Pet_rod = "любовницы"
                            $ StormX.Pet_dat = "любовнице"
                            $ StormX.Pet_vin = "любовницу"
                            $ StormX.Pet_tvo = "любовницей"
                            $ StormX.Pet_pre = "любовнице"
                            $ StormX.FaceChange("sly")
                            ch_s "Да. . ."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Не говори так, [StormX.Petname]."

                    "\"секс-партнерша\".":
                        if "fuckbuddy" in StormX.Petnames or ApprovalCheck(StormX, 700, "I"):
                            $ StormX.Pet = "секс-партнерша"
                            $ StormX.Pet_rod = "секс-партнерши"
                            $ StormX.Pet_dat = "секс-партнерше"
                            $ StormX.Pet_vin = "секс-партнершу"
                            $ StormX.Pet_tvo = "секс-партнершей"
                            $ StormX.Pet_pre = "секс-партнерше"
                            $ StormX.FaceChange("sly")
                            ch_s "Конечно."
                        else:
                            $ StormX.FaceChange("angry", 1)
                            $ StormX.Mouth = "surprised"
                            ch_s "Это совсем не смешно, [StormX.Petname]."

                    "\"доченька\".":
                        if "daddy" in StormX.Petnames or ApprovalCheck(StormX, 1200):
                            $ StormX.Pet = "доченька"
                            $ StormX.Pet_rod = "доченьки"
                            $ StormX.Pet_dat = "доченьке"
                            $ StormX.Pet_vin = "доченьку"
                            $ StormX.Pet_tvo = "доченькой"
                            $ StormX.Pet_pre = "доченьке"
                            $ StormX.FaceChange("smile", 1)
                            ch_s "Пожалуй?"
                        else:
                            $ StormX.FaceChange("angry", 1)
                            ch_s "Это очень странно. . ."

                    "Назад":
                        pass

            "Неважно.":
                return
    return

#label Storm_Namecheck(StormX.Pet = StormX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname


# start Storm_Rename//////////////////////////////////////////////////////////
label Storm_Rename:   #rkeljs
        #Sets alternate names from Storm
        $ StormX.Mouth = "smile"
        ch_s "Да?"
        menu:
            extend ""
            "Я думаю, \"Шторм\" классное имя." if StormX.Name != "Шторм" and "Storm" in StormX.Names:
                    $ StormX.Name = "Шторм"
                    $ StormX.Name_rod = "Шторм"
                    $ StormX.Name_dat = "Шторм"
                    $ StormX.Name_vin = "Шторм"
                    $ StormX.Name_tvo = "Шторм"
                    $ StormX.Name_pre = "Шторм"
                    ch_s "Звучит неплохо."
            "Я думаю, \"Ороро\" красивое имя." if StormX.Name != "Ороро" and "Ororo" in StormX.Names:
                    $ StormX.Name = "Ороро"
                    $ StormX.Name_rod = "Ороро"
                    $ StormX.Name_dat = "Ороро"
                    $ StormX.Name_vin = "Ороро"
                    $ StormX.Name_tvo = "Ороро"
                    $ StormX.Name_pre = "Ороро"
                    ch_s "Звучит неплохо."
            "Я думаю, \"Мисс Манро\" красивое имя." if StormX.Name != "Мисс Манро" and "Ms. Munroe" in StormX.Names:
                    $ StormX.Name = "Мисс Манро"
                    $ StormX.Name_rod = "Мисс Манро"
                    $ StormX.Name_dat = "Мисс Манро"
                    $ StormX.Name_vin = "Мисс Манро"
                    $ StormX.Name_tvo = "Мисс Манро"
                    $ StormX.Name_pre = "Мисс Манро"
                    ch_s "Звучит неплохо."
            "Неважно.":
                    pass
        $ StormX.AddWord(1,0,"namechange")
        return
# end Storm_Rename//////////////////////////////////////////////////////////


# start Storm_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Storm_Personality(Cnt = 0):    #rkeljs
    if not StormX.Chat[4] or Cnt:
        "Поскольку у вас все хорошо получается в одной области, вы можете убедить Шторм сосредоточиться на любой другой."
        "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
        "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
    menu:
        ch_s "Да? Ты что-то хочешь?"
        "Больше Послушания. [[Любовь в Послушание]" if StormX.Love > 900:
            ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
            ch_s "Пожалуй, я могу попробовать."
            $ StormX.Chat[4] = 1
        "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if StormX.Love > 900:
            ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
            ch_s "Я могу попытаться стать более открытой."
            $ StormX.Chat[4] = 2

        "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if StormX.Obed > 900:
            ch_p "Я хочу, чтобы ты была более раскрепощенной."
            ch_s "Я могу попытаться стать более открытой."
            $ StormX.Chat[4] = 3
        "Больше Любви. [[Повиновение в Любовь]" if StormX.Obed > 900:
            ch_p "Я хочу, чтобы ты училась любить меня."
            ch_s "Я могу попробовать."
            $ StormX.Chat[4] = 4

        "Больше Повиновения. [[Раскрепощенность в Повиновение]" if StormX.Inbt > 900:
            ch_p "Я знаю, что нам и так весело, но разве ты не можешь иногда слушаться меня?"
            ch_s "Пожалуй, я могу попробовать."
            $ StormX.Chat[4] = 5

        "Больше Любви. [[Раскрепощенность в Любовь]" if StormX.Inbt > 900:
            ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
            ch_s "Я могу попробовать."
            $ StormX.Chat[4] = 6

        "Просто делай то, что тебе нравится. . .[[Сбросить]" if StormX.Chat[4]:
            ch_p "Помнишь, что мы обсуждали? Забудь."
            ch_s ". . . хорошо."
            $ StormX.Chat[4] = 0
        "Повторить правила":
            call Storm_Personality(1)
            return
        "Неважно.":
            return
    return
# end Storm_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Storm_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Storm_Summon(Tempmod=Tempmod): #rkeljs
    $ StormX.OutfitChange()
    if "no summon" in StormX.RecentActions:
                if "angry" in StormX.RecentActions:
                    ch_s "Я слишком раздражена для этого."
                elif StormX.RecentActions.count("no summon") > 1:
                    ch_s "Хватит меня доставать!"
                    $ StormX.RecentActions.append("angry")
#                elif Current_Time == "Night":
#                    ch_s "Like I said, it's too late for that."
                else:
                    ch_s "Как я уже сказала, я занята."
                $ StormX.RecentActions.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if StormX.Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = -30
    elif StormX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -30
    elif StormX.Loc == "bg dangerroom":
        $ Tempmod = -10
    elif StormX.Loc == "bg showerroom":
        $ Tempmod = -30

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"
    if Time_Count >= 3: #night time
                if ApprovalCheck(StormX, 500, "L") or ApprovalCheck(StormX, 400, "O"):
                        #It's night time but she likes you.
                        ch_s "Ты не спишь? Я могу составить тебе компанию."
                        $ StormX.Loc = bg_current
                        call Taboo_Level
                        call Set_The_Scene
                else:
                        #It's night time and she isn't into you
                        ch_s "Уже слишком поздно, мне нужно поспать."
                        $ StormX.RecentActions.append("no summon")
                return
    elif "les" in StormX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(StormX, 2000):
                    ch_s "Я сейчас с одной девушкой. Присоединишься к нам?"
                    menu:
                        extend ""
                        "Конечно.":
                            $ Line = "go to"
                        "Нет, спасибо.":
                            ch_s "Тогда до свидания."
                            return
            else:
                    ch_s "Я сейчас по уши в делах"
                    ch_s "Возможно, мы могли бы поговорить позже?"
                    $ StormX.RecentActions.append("no summon")
                    return
    elif not ApprovalCheck(StormX, 700, "L") or not ApprovalCheck(StormX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(StormX, 300):
                ch_s "Я занята, [StormX.Petname]."
                $ StormX.RecentActions.append("no summon")
                return


        if "summoned" in StormX.RecentActions:
                pass
        elif "goto" in StormX.RecentActions:
                if not Player.Male:
                    ch_s "Ты только что была здесь."
                else:
                    ch_s "Ты только что был здесь."
        elif StormX.Loc == "bg classroom"or StormX.Loc == "bg teacher":
                ch_s "Ты можешь найти меня в аудитории."
        elif StormX.Loc == "bg dangerroom":
                ch_s "Я в комнате Опасности, [StormX.Petname], не хочешь со мной?"
        elif StormX.Loc == "bg campus":
                ch_s "Я отдыхаю во дворе, не хочешь со мной?"
        elif StormX.Loc == "bg storm":
                ch_s "Я в своей комнате, [StormX.Petname], не хочешь со мной?"
        elif StormX.Loc == "bg player":
                ch_s "Я в твоей комнате, [StormX.Petname], ты скоро вернешься?"
        elif StormX.Loc == "bg showerroom":
            if ApprovalCheck(StormX, 1600):
                ch_s "Я сейчас в душе. Не хочешь ко мне?"
            else:
                ch_s "Я сейчас в душе, [StormX.Petname]. Встретимся позже."
                $ StormX.RecentActions.append("no summon")
                return
        elif StormX.Loc == "hold":
                ch_s "Прошу прощения. Я сейчас занята."
                $ StormX.RecentActions.append("no summon")
                return
        else:
                if not Player.Male:
                    ch_s "Возможно, ты могла бы зайти ко мне?"
                else:
                    ch_s "Возможно, ты мог бы зайти ко мне?"


        if "summoned" in StormX.RecentActions:
            ch_s "Снова? Что ж, хорошо. . ."
            $ Line = "yes"
        elif "goto" in StormX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
#                                ch_s "I will see you soon then."
                                $ Line = "go to"
                "Нет.":
                                ch_s "Как пожелаешь."
                "Мне бы {i}очень{/i} хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(StormX, 600, "L") or ApprovalCheck(StormX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(StormX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(StormX, 1400):
                                #she is generally favorable
                                ch_s ". . ."
                                $ Line = "yes"
                        elif ApprovalCheck(StormX, 200, "O"):
                                #she is not obedient
                                ch_s "Ты знаешь, где меня найти, если вдруг передумаешь."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(StormX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(StormX, 1400):
                                #she is generally favorable
                                ch_s ". . ."
                                $ Line = "yes"
                        elif ApprovalCheck(StormX, 200, "O"):
                                #she is not obedient
                                ch_s "Ты знаешь, где меня найти, если вдруг передумаешь."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Конечно, сейчас приду.":
                    $ StormX.Statup("Love", 55, 1)
                    $ StormX.Statup("Inbt", 30, 1)
#                    ch_s "I will see you soon then."
                    $ Line = "go to"

                "Нет, поговорим позже.":
                    $ StormX.Statup("Obed", 50, 1)
                    $ StormX.Statup("Obed", 30, 2)
                    ch_s "Хорошо. Увидимся позже."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                    if ApprovalCheck(StormX, 650, "L") or ApprovalCheck(StormX, 1500):
                        $ StormX.Statup("Love", 70, 1)
                        $ StormX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ StormX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                        ch_s "Что ж, мы не можем этого допустить. . ."

                "Давай, будет весело.":
                    if ApprovalCheck(StormX, 400, "L") and ApprovalCheck(StormX, 800):
                        $ StormX.Statup("Love", 70, 1)
                        $ StormX.Statup("Obed", 50, 1)
                        $ Line = "fun"
                    else:
                        $ StormX.Statup("Inbt", 30, 1)
                        $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                    if ApprovalCheck(StormX, 600, "O"):
                        #she is obedient
                        $ StormX.Statup("Love", 50, 1, 1)
                        $ StormX.Statup("Love", 40, -1)
                        $ StormX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(StormX, 1500):
                        #she is generally favorable
                        $ StormX.Statup("Love", 70, -2)
                        $ StormX.Statup("Love", 90, -1)
                        $ StormX.Statup("Obed", 50, 2)
                        $ StormX.Statup("Obed", 90, 1)
                        ch_s "Хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(StormX, 200, "O"):
                        #she is not obedient
                        $ StormX.Statup("Love", 60, -4)
                        $ StormX.Statup("Love", 90, -3)
                        ch_s "Отказываюсь."
                        $ StormX.Statup("Inbt", 40, 2)
                        $ StormX.Statup("Inbt", 60, 1)
                        $ StormX.Statup("Obed", 70, -3)
                        ch_s "Я предпочитаю остаться."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ StormX.Statup("Inbt", 30, 1)
                        $ StormX.Statup("Inbt", 50, 1)
                        $ StormX.Statup("Love", 50, -1, 1)
                        $ StormX.Statup("Obed", 70, -1)
                        $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                    if ApprovalCheck(StormX, 600, "O"):
                        #she is obedient
                        $ StormX.Statup("Love", 50, 1, 1)
                        $ StormX.Statup("Love", 40, -1)
                        $ StormX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(StormX, 1500):
                        #she is generally favorable
                        $ StormX.Statup("Love", 70, -2)
                        $ StormX.Statup("Love", 90, -1)
                        $ StormX.Statup("Obed", 50, 2)
                        $ StormX.Statup("Obed", 90, 1)
                        ch_s "Хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(StormX, 200, "O"):
                        #she is not obedient
                        $ StormX.Statup("Love", 60, -4)
                        $ StormX.Statup("Love", 90, -3)
                        ch_s "Отказываюсь."
                        $ StormX.Statup("Inbt", 40, 2)
                        $ StormX.Statup("Inbt", 60, 1)
                        $ StormX.Statup("Obed", 70, -3)
                        ch_s "Я предпочитаю остаться."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ StormX.Statup("Inbt", 30, 1)
                        $ StormX.Statup("Inbt", 50, 1)
                        $ StormX.Statup("Love", 50, -1, 1)
                        $ StormX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if StormX.Love > StormX.Obed:
            ch_s "Уже иду."
        else:
            ch_s "Хорошо."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ StormX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            if StormX.Loc == "bg classroom" or StormX.Loc == "bg teacher":
                ch_s "Я не могу так просто уйти с занятий."
            elif StormX.Loc == "bg dangerroom":
                ch_s "У меня впереди тяжелая тренировка."
            else:
                ch_s "Мне жаль, [StormX.Petname], я занята."
            $ StormX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ StormX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            $ Line = 0
            $ Nearby = []
            $ Party = [StormX]
            if StormX.Loc == "bg classroom" or StormX.Loc == "bg teacher":
                    ch_s "Тогда скоро увидимся."
                    jump Class_Room
            elif StormX.Loc == "bg dangerroom":
                    ch_s "Тогда скоро увидимся."
                    jump Danger_Room
            elif StormX.Loc == "bg storm":
                    ch_s "Тогда скоро увидимся."
                    jump Storm_Room
            elif StormX.Loc == "bg player":
                    ch_s "Я буду ждать."
                    jump Player_Room
            elif StormX.Loc == "bg showerroom":
                    ch_s "Я оставлю тебе немного горячей воды."
                    jump Shower_Room
            elif StormX.Loc == "bg campus":
                    ch_s "Буду выглядывать тебя."
                    jump Campus
            elif StormX.Loc != "hold":
                    ch_s "Тогда увидимся."
                    $ bg_current = StormX.Loc
                    jump Misplaced
            else:
                    ch_s "Я просто встречу тебя в своей комнате."
                    $ StormX.Loc = "bg storm"
                    jump Storm_Room

    #She's agreed to come over
    elif Line == "lonely":
            if not Player.Male:
                ch_s "И почему ты такая очаровательная?"
            else:
                ch_s "И почему ты такой очаровательный?"
    elif Line == "command":
            ch_s "Да, [StormX.Petname]."
    elif Line == "fun":
            ch_s "Конечно."

    $ StormX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(StormX)
            return
    $ StormX.Loc = bg_current
    call Taboo_Level(0)
    $ StormX.OutfitChange()
    call Set_The_Scene
    return

# End Storm Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Storm_Leave(Tempmod=Tempmod, GirlsNum = 0):   #rkeljs
    if "leaving" in StormX.RecentActions:
        $ StormX.DrainWord("leaving")
    else:
        return

    if StormX.Loc == "hold":
            # Activates if she's being moved out of play
            ch_s "У меня есть кое-какие дела."
            return

    if StormX in Party or "lockedtravels" in StormX.Traits:
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ StormX.Loc = bg_current
            return

    elif "freetravels" in StormX.Traits or not ApprovalCheck(StormX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.
            $ StormX.OutfitChange()
            if GirlsNum: #if someone left before her
                        ch_s "Да, я тоже пошла."

            if StormX.Loc == "bg classroom" or StormX.Loc == "bg teacher":
                        ch_s "Мне нужно вести занятия."
            elif StormX.Loc == "bg dangerroom":
                        ch_s "Я в комнату Опасности."
            elif StormX.Loc == "bg campus":
                        ch_s "Я собираюсь отдохнуть во дворе."
            elif StormX.Loc == "bg storm":
                        ch_s "Я возвращаюсь в свою комнату."
            elif StormX.Loc == "bg player":
                        ch_s "Я планирую отдохнуть в твоей комнате."
            elif StormX.Loc == "bg pool":
                        ch_s "Я собираюсь искупаться."
            elif StormX.Loc == "bg showerroom":
                if ApprovalCheck(StormX, 1400):
                        ch_s "Я в душ, увидимся позже."
                else:
                        ch_s "Увидимся позже."
            else:
                        ch_s "Увидимся позже."
            hide Storm_Sprite
            return
            #End Free Travels

    if bg_current == "bg dangerroom":
            call Gym_Exit([StormX])

    $ StormX.OutfitChange()

    if "follow" not in StormX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ StormX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    # Sets her preferences
    if StormX.Loc == "bg classroom" or StormX.Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = 30
    elif StormX.Loc == "bg dangerroom":
        $ Tempmod = 20
    elif StormX.Loc == "bg showerroom":
        $ Tempmod = 40


    if GirlsNum: #if someone left before her
                ch_s "Ага, я тоже пошла."


    if StormX.Loc == "bg classroom" or StormX.Loc == "bg teacher":
                ch_s "Мне нужно вести занятия, ты придешь?"
    elif StormX.Loc == "bg dangerroom":
                ch_s "Я в комнату Опасности, не хочешь со мной?"
    elif StormX.Loc == "bg campus":
                ch_s "Я собираюсь отдохнуть во дворе, не хочешь со мной?"
    elif StormX.Loc == "bg storm":
                ch_s "Я возвращаюсь в свою комнату, не хочешь со мной?"
    elif StormX.Loc == "bg player":
                ch_s "Я планирую отдохнуть в твоей комнате, не хочешь со мной?"
    elif StormX.Loc == "bg pool":
                ch_s "Я собираюсь искупаться, не хочешь со мной?"
    elif StormX.Loc == "bg mall":
                ch_s "Я планирую посетить торговый центр, не хочешь со мной?"
    elif StormX.Loc == "bg showerroom":
        if ApprovalCheck(StormX, 1400):
                ch_s "Я в душ, не хочешь со мной?"
        else:
                ch_s "Увидимся позже."
    else:
                ch_s "Не хочешь со мной?"


    menu:
        extend ""
        "Конечно, я сразу за тобой.":
                if "followed" not in StormX.RecentActions:
                    $ StormX.Statup("Love", 55, 1)
                    $ StormX.Statup("Inbt", 30, 1)
                $ Line = "go to"

        "Нет, поговорим позже.":
                if "followed" not in StormX.RecentActions:
                    $ StormX.Statup("Obed", 50, 1)
                    $ StormX.Statup("Obed", 30, 2)
                ch_s "Хорошо."

        "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                if ApprovalCheck(StormX, 650, "L") or ApprovalCheck(StormX, 1500):
                    if "followed" not in StormX.RecentActions:
                        $ StormX.Statup("Love", 70, 1)
                        $ StormX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else:
                    if "followed" not in StormX.RecentActions:
                        $ StormX.Statup("Inbt", 30, 1)
                    $ Line = "no"
                    ch_s "Мы не можем этого допустить. . ."

        "Давай, будет весело.":
                if ApprovalCheck(StormX, 400, "L") and ApprovalCheck(StormX, 800):
                    $ StormX.Statup("Love", 70, 1)
                    $ StormX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else:
                    $ StormX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Нет, останься здесь.":
                if ApprovalCheck(StormX, 600, "O"):
                    #she is obedient
                    if "followed" not in StormX.RecentActions:
                        $ StormX.Statup("Love", 40, -2)
                        $ StormX.Statup("Obed", 90, 1)
                    $ Line = "command"

                elif D20 >= 7 and ApprovalCheck(StormX, 1400):
                    #she is generally favorable
                    if "followed" not in StormX.RecentActions:
                        $ StormX.Statup("Love", 70, -2)
                        $ StormX.Statup("Love", 90, -1)
                        $ StormX.Statup("Obed", 50, 2)
                        $ StormX.Statup("Obed", 90, 1)
                        ch_s "Хорошо."
                    $ Line = "yes"

                elif ApprovalCheck(StormX, 200, "O"):
                    #she is not obedient
                    if "followed" not in StormX.RecentActions:
                        $ StormX.Statup("Love", 70, -4)
                        $ StormX.Statup("Love", 90, -2)
                    ch_s "Отказываюсь."
                    if "followed" not in StormX.RecentActions:
                        $ StormX.Statup("Inbt", 40, 2)
                        $ StormX.Statup("Inbt", 60, 1)
                        $ StormX.Statup("Obed", 70, -2)
                    ch_s "Я предпочитаю уйти."
                else:
                    #she is obedient, but you failed to meet the checks
                    if "followed" not in StormX.RecentActions:
                        $ StormX.Statup("Inbt", 30, 1)
                        $ StormX.Statup("Inbt", 50, 1)
                        $ StormX.Statup("Love", 50, -1, 1)
                        $ StormX.Statup("Love", 90, -2)
                        $ StormX.Statup("Obed", 70, -1)
                    $ Line = "no"
                #End ordered to stay


    call Taboo_Level(0)
    $ StormX.RecentActions.append("followed")
    if not Line:
            #You end the dialog neutrally
            hide Storm_Sprite
            call Gym_Clothes_Off([StormX])
            return

    if Line == "no":
            # She's refused, context based dialog
            if StormX.Loc == "bg classroom" or StormX.Loc == "bg teacher":
                ch_s "Я не могу так просто пропускать занятия."
            elif StormX.Loc == "bg dangerroom":
                ch_s "У меня впереди тяжелая тренировка."
            else:
                ch_s "Мне жаль, [StormX.Petname], я занята."

            hide Storm_Sprite
            call Gym_Clothes_Off([StormX])
            return

    elif Line == "go to":
            #You agreed to go to her instead
            #$ Party.append(StormX)
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")
            $ StormX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            hide Storm_Sprite
            call Gym_Clothes_Off([StormX])
            $ Nearby = []
            $ Party = [StormX]
            if StormX.Loc == "bg classroom" or StormX.Loc == "bg teacher":
                    ch_s "Тогда скоро увидимся."
                    jump Class_Room
            elif StormX.Loc == "bg dangerroom":
                    ch_s "Тогда скоро увидимся."
                    jump Danger_Room
            elif StormX.Loc == "bg storm":
                    ch_s "Тогда скоро увидимся."
                    jump Storm_Room
            elif StormX.Loc == "bg player":
                    ch_s "Я буду ждать."
                    jump Player_Room
            elif StormX.Loc == "bg showerroom":
                    ch_s "Я оставлю тебе немного горячей воды."
                    jump Shower_Room
            elif StormX.Loc == "bg campus":
                    ch_s "Буду выглядывать тебя."
                    jump Campus
            elif StormX.Loc == "bg pool":
                    ch_s "Замечательно."
                    jump Pool_Entry
            elif StormX.Loc == "bg mall":
                    ch_s "Замечательно."
                    jump Mall_Entry
            else:
                    ch_s "Я просто встречу тебя в твоей комнате."
                    $ StormX.Loc = "bg player"
                    jump Player_Room
            #End "goto" where she's at


    #She's agreed to come over
    elif Line == "lonely":
        if not Player.Male:
            ch_s "И почему ты такая очаровательная?"
        else:
            ch_s "И почему ты такой очаровательный?"
    elif Line == "command":
            ch_s "Да, [StormX.Petname]."
    elif Line:
            ch_s "Конечно."

    $ Line = 0
    ch_s "Я останусь здесь."
    $ StormX.Loc = bg_current
    return

# End Storm Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

### Storm's Clothes  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Storm_Clothes:  #rkeljs
    if StormX.Taboo and StormX not in Rules:
            if "exhibitionist" in StormX.Traits:
                ch_s "О, здесь? . ."
            elif ApprovalCheck(StormX, 900, TabM=4) or ApprovalCheck(StormX, 400, "I", TabM=3):
                ch_s "Я не должна здесь раздеваться. . ."
            else:
                ch_s "Я не должна здесь раздеваться. . ."
                ch_s "Мы можем поговорить в одной из наших комнатах?"
                return
    elif ApprovalCheck(StormX, 900, TabM=4) or ApprovalCheck(StormX, 600, "L") or ApprovalCheck(StormX, 300, "O"):
                ch_s "Ох? Что не так с моей одеждой?"
    else:
                ch_s "Если честно, мне не нужны советы по моде, благодарю."
                return

    if Girl != StormX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = StormX
    call Shift_Focus(Girl)

label Storm_Wardrobe_Menu:
    $ StormX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .
    while True:
        menu:
            ch_s "Что насчет моего гардероба?"
            "Верх":
                        call Storm_Clothes_Over
            "Низ":
                        call Storm_Clothes_Legs
            "Нижнее белье":
                        call Storm_Clothes_Under
            "Аксессуары":
                        call Storm_Clothes_Misc
            "Управление нарядами":
                        call Storm_Clothes_Outfits
            "Давай поговорим о том, что ты носишь.":
                        call Clothes_Schedule(StormX)

            "Могу я посмотреть?" if StormX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(StormX,0,2)
                    if _return:
                            show PhoneSex zorder 150
                            ch_s "Что думаешь?"
                    hide PhoneSex
            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(StormX,0,2)
                    if _return:
                        hide DressScreen
            "Может, тебе будет комфортнее за ширмой? (locked)" if StormX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if StormX.Loc == bg_current and not StormX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    #if ApprovalCheck(StormX, 1500) or (StormX.SeenChest and StormX.SeenPussy):
                            ch_s "Мне она не понадобится, но благодарю за предложение."
                    #else:
#                            show DressScreen zorder 150
#                            ch_s "Yeah, this is better."

            "У меня есть подарок для тебя (locked)" if StormX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if StormX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(StormX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ StormX.OutfitChange()
                    $ StormX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != StormX:
                            ch_p "Я хочу поговорить о твоей одежде."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = StormX
                    call Shift_Focus(Girl)

            "Cменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current:
                    pass
            "Cменить вид" if Girl.Loc == bg_current:
                    call WardrobeView(StormX)

            "Неважно, ты и так хорошо выглядишь":
                    call Girl_Pos_Reset(StormX)
                    if "wardrobe" not in StormX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if (StormX.OverNum()+StormX.ChestNum()<4) or (StormX.PantiesNum()+StormX.PantsNum() < 5):
                                    #if she's half-naked
                                    $ StormX.FaceChange("sly",Eyes="down")
                                    ch_s "Я понимаю, почему -ты- так думаешь. . ."
                                    $ StormX.FaceChange("sly")
                            elif StormX.Chat[1] <= 1:
                                    $ StormX.Statup("Love", 70, 15)
                                    $ StormX.Statup("Obed", 40, 20)
                                    ch_s "Ох, как приятно, что ты так говоришь."
                            elif StormX.Chat[1] <= 10:
                                    $ StormX.Statup("Love", 70, 5)
                                    $ StormX.Statup("Obed", 40, 7)
                                    ch_s "Мне нравится этот образ."
                            elif StormX.Chat[1] <= 50:
                                    $ StormX.Statup("Love", 70, 1)
                                    $ StormX.Statup("Obed", 40, 1)
                                    ch_s "Благодарю. . ."
                            else:
                                    ch_s "Безусловно."
                            $ StormX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(StormX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ StormX.OutfitChange()
                    $ StormX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ StormX.Chat[1] += 1
                    $ Trigger = 0
                    if StormX.Panties and "pantyless" in StormX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ StormX.DailyActions.remove("pantyless")
                    return

        #Loops back up
        #return #jump Storm_Clothes
        #End of Storm Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Storm_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(StormX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(StormX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(StormX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(StormX,4,1)
                    "Одежда для сна":
                                call OutfitShame(StormX,7,1)
                    "Купальник":
                                call OutfitShame(StormX,10,1)

                    "Повседневка 1" if ApprovalCheck(StormX, 2500):
                                call OutfitShame(StormX,11,1)
                    "Повседневка 2" if ApprovalCheck(StormX, 2500):
                                call OutfitShame(StormX,12,1)
                    #8 is Emma's teaching clothes,
                    "Неважно":
                                pass

        "Надень комплект с юбкой":
                $ StormX.OutfitChange("casual1")
                menu:
                    "Ты должна носить его. [[Выбрать текущий наряд]":
                            $ StormX.Outfit = "casual1"
                            $ StormX.Shame = 0
                            ch_s "Да, это мой любимый повседневный наряд."
                    "Давай попробуем что-нибудь другое.":
                            ch_s "Ладно."

        "Надень комплект с кожаной курткой и брюками":
                $ StormX.OutfitChange("casual2")
                menu:
                    "Ты должна носить его. [[Выбрать текущий наряд]":
                            $ StormX.Outfit = "casual2"
                            $ StormX.Shame = 0
                            ch_s "Да, я нахожу этот вариант очень стильным."
                    "Давай попробуем что-нибудь другое.":
                            ch_s "Ладно."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not StormX.Custom1[0] and not StormX.Custom2[0] and not StormX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if StormX.Custom1[0] or StormX.Custom2[0] or StormX.Custom3[0]:
                $ Cnt = 0
                while True:
                    menu:
                        "Надень Пользовательский 1 (locked)" if not StormX.Custom1[0]:
                                pass
                        "Надень Пользовательский 1" if StormX.Custom1[0]:
                                $ StormX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Надень Пользовательский 2 (locked)" if not StormX.Custom2[0]:
                                pass
                        "Надень Пользовательский 2" if StormX.Custom2[0]:
                                $ StormX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Надень Пользовательский 3 (locked)" if not StormX.Custom3[0]:
                                pass
                        "Надень Пользовательский 3" if StormX.Custom3[0]:
                                $ StormX.OutfitChange("custom3")
                                $ Cnt = 6

                        "Ты должна одеваться так, когда мы наедине (locked)" if not Cnt:
                                pass
                        "Ты должна одеваться так, когда мы наедине" if Cnt:
                                if Cnt == 5:
                                        $ StormX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                        $ StormX.Clothing[9] = "custom3"
                                else:
                                        $ StormX.Clothing[9] = "custom1"
                                ch_s "Это было бы замечательно."

                        "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                menu:
                                    "Пользовательский 1 [[очистить слот 1]" if StormX.Custom1[0]:
                                            ch_s "Хорошо."
                                            $ StormX.Custom1[0] = 0
                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not StormX.Custom1[0]:
                                            pass
                                    "Пользовательский 2 [[очистить слот 2]" if StormX.Custom2[0]:
                                            ch_s "Хорошо."
                                            $ StormX.Custom2[0] = 0
                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not StormX.Custom2[0]:
                                            pass
                                    "Пользовательский 3 [[очистить слот 3]" if StormX.Custom3[0]:
                                            ch_s "Хорошо."
                                            $ StormX.Custom3[0] = 0
                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not StormX.Custom3[0]:
                                            pass
                                    "Неважно [[назад]":
                                            pass

                        "Тебе следует надеть его [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                pass
                        "Тебе следует надеть его" if Cnt:
                                call Custom_Out(StormX,Cnt)
                        "Ладно, вернемся к началу нашего разговора. . .":
                                $ Cnt = 0
                                return #jump Storm_Clothes

        "Наденешь спортивную одежду?" if not StormX.Taboo or bg_current == "bg dangerroom":
                $ StormX.OutfitChange("gym")

        "Наденешь одежду для сна?" if not StormX.Taboo:
                if ApprovalCheck(StormX, 1200):
                        $ StormX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(StormX)
                        if _return:
                                $ StormX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (StormX.Taboo and bg_current != "bg pool" and not ApprovalCheck(StormX, 800, TabM=2)) or not StormX.Swim[0]:
                $ StormX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not StormX.Taboo or bg_current == "bg pool" or ApprovalCheck(StormX, 800, TabM=2)) and StormX.Swim[0]:
                $ StormX.OutfitChange("swimwear")


        "Наденешь хэллоуинский костюм?" if "halloween" in StormX.History:
                if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                        ch_s "Хорошо."
                        $ StormX.OutfitChange("costume")
                elif ApprovalCheck(StormX, 1100, TabM=3):
                        ch_s "Ладно."
                        $ StormX.OutfitChange("costume")
                else:
                        call Display_DressScreen(StormX)
                        if not _return:
                                ch_s "Я бы очень этого не хотела. . ."
                        else:
                                $ StormX.OutfitChange("costume")


        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ StormX.FaceChange("sexy", 1)
                $ Line = 0
                if not StormX.Chest and not StormX.Panties and not StormX.Over and not StormX.Legs and not StormX.Hose:
                        ch_s "Благодарю."
                elif ApprovalCheck(StormX, 1200, TabM=4): #and StormX.SeenChest and StormX.SeenPussy
                        ch_s "Безусловно. . ."
                        $ Line = 1
                elif ApprovalCheck(StormX, 2000, TabM=4):
                        ch_s "Так просто, без прелюдий?"
                        $ Line = 1
                elif not ApprovalCheck(StormX, 500, TabM=0):
                        $ StormX.FaceChange("confused", 1,Mouth="smirk")
                        ch_s "Знаешь, я не раздеваюсь по команде. . ."
                        $ StormX.FaceChange("bemused", 0)
                elif StormX.Taboo and StormX not in Rules: #StormX.SeenChest and StormX.SeenPussy and ApprovalCheck(StormX, 1200, TabM=0)
                        ch_s "Возможно, но не здесь. . ."
                elif ApprovalCheck(StormX, 1000, TabM=0):
                        $ StormX.FaceChange("confused", 1,Mouth="smirk")
                        ch_s "Ага, но я не хвастаюсь."
                        $ StormX.FaceChange("bemused", 0)
                else:
                        $ StormX.FaceChange("angry", 1)
                        ch_s "Я бы предпочла не раздеваться."

                call expression StormX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in StormX.History:
                        $ Line = 0
                if Line:
                    #If she got nude. . .
                    $ StormX.OutfitChange("nude")
                    "Она сбрасывает одежду к своим ногам."
                    call Girl_First_Topless(StormX)
                    call Girl_First_Bottomless(StormX,1)
                    $ StormX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется, что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in StormX.Traits:
                                    ch_s "Мммм. . ."
                                    $ StormX.Outfit = "nude"
                                    $ StormX.Statup("Lust", 50, 10)
                                    $ StormX.Statup("Lust", 70, 5)
                                    $ StormX.Shame = 50
                            elif ApprovalCheck(StormX, 800, "I") or ApprovalCheck(StormX, 2800, TabM=0) or StormX in Rules:
                                    ch_s "Можно. . ."
                                    $ StormX.Outfit = "nude"
                                    $ StormX.Shame = 50
                            else:
                                    $ StormX.FaceChange("sexy", 1)
                                    $ StormX.Eyes = "surprised"
                                    ch_s "Наверное, не стоит. Мне жаль."

                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in StormX.Traits:
                                    if not Player.Male:
                                        ch_s "Ты уверена?"
                                    else:
                                        ch_s "Ты уверен?"
                            elif ApprovalCheck(StormX, 800, "I") or ApprovalCheck(StormX, 2800, TabM=0) or StormX in Rules:
                                    $ StormX.FaceChange("bemused", 1)
                                    ch_s "Я ждала, что ты захочешь, чтобы я ходила в таком виде."
                                    ch_s ". . ."
                            else:
                                    $ StormX.FaceChange("confused", 1)
                                    if not Player.Male:
                                        ch_s "Я не возражаю, чтобы ты видела мое тело, но у Чарльза свои правила. . ."
                                    else:
                                        ch_s "Я не возражаю, чтобы ты видел мое тело, но у Чарльза свои правила. . ."
                $ Line = 0

        "Неважно":
            return #jump Storm_Clothes

    return #jump Storm_Clothes
    #End of Storm Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Storm_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять [get_clothing_name(StormX.Over_key, vin)]?" if StormX.Over:
                call Wardrobe_Remove(StormX)

        "Примерь белую майку." if StormX.Over != "white shirt":
                $ StormX.FaceChange("bemused")
                if not StormX.Over or StormX.ChestNum() >= 5:
                    #if she's not already wearing a top, or has fair clothes on under
                    ch_s "Хорошо."
                elif ApprovalCheck(StormX, 800, TabM=3):
                    ch_s "Хорошо."
                else:
                    call Display_DressScreen(StormX)
                    if not _return:
                            $ StormX.FaceChange("bemused", 1)
                            ch_s "Я не хочу сейчас переодевать [get_clothing_name(StormX.Over_key, vin)]."
                            return #jump Storm_Clothes
                $ StormX.Over = "white shirt"

        "Примерь кожаную куртку." if StormX.Over != "jacket":
                $ StormX.FaceChange("bemused")
                if not StormX.Over or StormX.ChestNum() >= 5:
                    #if she's not already wearing a top, or has fair clothes on under
                    ch_s "Хорошо."
                elif ApprovalCheck(StormX, 800, TabM=3):
                    ch_s "Хорошо."
                else:
                    call Display_DressScreen(StormX)
                    if not _return:
                            $ StormX.FaceChange("bemused", 1)
                            ch_s "Я не хочу сейчас переодевать [get_clothing_name(StormX.Over_key, vin)]."
                            return #jump Storm_Clothes
                $ StormX.Over = "jacket"

        "Может, просто накинешь полотенце?" if StormX.Over != "towel":
                $ StormX.FaceChange("bemused", 1)
                if StormX.ChestNum() >= 5: #or StormX.SeenChest
                    ch_s "Если ты этого хочешь. . ."
                elif ApprovalCheck(StormX, 1000, TabM=3):
                    $ StormX.FaceChange("perplexed", 1)
                    ch_s "Если ты этого хочешь. . ."
                else:
                    call Display_DressScreen(StormX)
                    if not _return:
                            ch_s "Боюсь, я не могу."
                            return #jump Storm_Clothes
                $ StormX.Over = "towel"

        "Неважно":
            pass
    return #jump Storm_Clothes
    #End of Storm Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Storm_NoBra:
        menu:
            ch_s "Под [get_clothing_name(StormX.Over_key, tvo)] у меня ничего нет. . ."
            "Тогда надень что-нибудь. . .":
                        if StormX in Rules or StormX.Taboo < 20 :
                                ch_s "Нет, пожалуй, меня все устраивает, во всяком случае, сейчас."
                        elif StormX.SeenChest and ApprovalCheck(StormX, 1000, TabM=3):
                                $ StormX.Blush = 2
                                ch_s "Я совсем не против. . ."
                                $ StormX.Blush = 0
#                        elif ApprovalCheck(StormX, 1200, TabM=4):
#                                $ StormX.Blush = 1
#                                ch_s "-I didn't say that I minded. . ."
#                                $ StormX.Blush = 0
                        elif ApprovalCheck(StormX, 900, TabM=2) and "lace bra" in StormX.Inventory:
                                ch_s "Хорошо."
                                $ StormX.Chest  = "lace bra"
                                "Она достает кружевной лифчик и надевает его под [get_clothing_name(StormX.Over_key, vin)]."
                        elif ApprovalCheck(StormX, 700, TabM=2) and "corset" in StormX.Inventory:
                                ch_s "Хорошо."
                                $ StormX.Chest  = "black bra"
                                "Она достает свой черный лифчик и надевает его под [get_clothing_name(StormX.Over_key, vin)]."
                        elif ApprovalCheck(StormX, 600, TabM=2):
                                ch_s "Хорошо."
                                $ StormX.Chest = "tube top"
                                "Она достает майку и надевает ее под [get_clothing_name(StormX.Over_key, vin)]."
                        else:
                                ch_s "Не думаю, что это было бы уместно."
                                return 0

            "Так даже лучше. . .":
                        if StormX in Rules or not StormX.Taboo:
                                ch_s "Пожалуй, меня все устраивает, во всяком случае, сейчас."
                        elif ApprovalCheck(StormX, 1100, "LI", TabM=2) and StormX.Love > StormX.Inbt:
                                ch_s "Для тебя? Конечно. . ."
                        elif ApprovalCheck(StormX, 700, "OI", TabM=2) and StormX.Obed > StormX.Inbt:
                                ch_s "Хорошо. . ."
                        elif ApprovalCheck(StormX, 600, "I", TabM=2):
                                ch_s "Да. . ."
                        elif ApprovalCheck(StormX, 1300, TabM=2):
                                ch_s "Согласна."
                        else:
                                $ StormX.FaceChange("sadside")
                                if StormX.Taboo > 20:
                                    ch_s "Боюсь, не на людях."
                                else:
                                    ch_s "Боюсь, что нет, [StormX.Petname]!"
                                call expression StormX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0
            "Неважно.":
                        ch_s "Ладно. . ."
                        return 0
        return 1
        #End of Storm bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Storm_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(StormX.Legs_key, vin)]?" if StormX.Legs:
                call Wardrobe_Remove(StormX,1)

        "Ты отлично выглядишь в черных брюках." if StormX.Legs != "pants":
                ch_s "Хорошо, один момент. . ."
                $ StormX.Legs = "pants"

        "Тебе отлично подходят штаны для йоги." if StormX.Legs != "yoga pants":
                ch_s "Хорошо, один момент. . ."
                $ StormX.Legs = "yoga pants"

        "Как насчет того, чтобы надеть свою фиолетовую юбку?" if StormX.Legs != "skirt":
                ch_s "Хорошо, один момент. . ."
                $ StormX.Legs = "skirt"

        "Сними обувь (locked)" if not StormX.Boots:
                pass
        "Сними [get_clothing_name(StormX.Boots_key, vin)]" if StormX.Boots:
                ch_p "Может, снимешь [get_clothing_name(StormX.Boots_key, vin)]?"
                ch_s "Хорошо, один момент. . ."
                $ StormX.Boots = 0
        "Надень ботинки" if StormX.Boots != "boots":
                ch_p "Может, наденешь ботинки?"
                ch_s "Хорошо, один момент. . ."
                $ StormX.Boots = "boots"
        "Надень сандалии" if StormX.Boots != "sandals":
                ch_p "Может, наденешь сандалии?"
                ch_s "Хорошо, один момент. . ."
                $ StormX.Boots = "sandals"
        "Надень кольца" if StormX.Boots != "rings" and "halloween" in StormX.History:
                ch_p "Может, наденешь кольца на ладышки?"
                ch_s "Хорошо, один момент. . ."
                $ StormX.Boots = "rings"

        "Неважно":
                pass
    return #jump Storm_Clothes
    #End of Storm Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Storm_NoPantiesOn:
        menu:
            ch_s "Сегодня на мне нет трусиков."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if StormX.Taboo <= 20 or StormX.HoseNum() >= 5 or StormX in Rules:
                                ch_s "Нет, меня все устраивает."
                        elif StormX.SeenPussy and ApprovalCheck(StormX, 1100, TabM=4):
                                $ StormX.Blush = 1
                                ch_s "Нет, мне и без них хорошо. . ."
                                $ StormX.Blush = 0
#                        elif ApprovalCheck(StormX, 1500, TabM=4):
#                                $ StormX.Blush = 1
#                                ch_s "No, commando's fine. . ."
#                                $ StormX.Blush = 0
                        elif ApprovalCheck(StormX, 700, TabM=4):
                                ch_s "Хорошо."
                                if "lace panties" in StormX.Inventory:
                                        $ StormX.Panties  = "lace panties"
                                else:
                                        $ StormX.Panties = "black panties"
                                if ApprovalCheck(StormX, 1200, TabM=4):
                                    $ Line = get_clothing_name(StormX.Legs_key, vin)
                                    $ StormX.Legs = 0
                                    "Она снимает [Line] и надевает [get_clothing_name(StormX.Panties_key, vin)]."
                                elif StormX.Legs == "skirt":
                                    "Она достает [get_clothing_name(StormX.Panties_key, vin)] и надевает их под юбку."
                                    $ StormX.Legs = 0
                                    "Затем она сбрасывает юбку на пол."
                                else:
                                    $ Line = get_clothing_name(StormX.Legs_key, vin)
                                    $ StormX.Legs = 0
                                    "Она на мгновение отходит, а затем возвращается в [get_clothing_name(StormX.Panties_key, pre)]."
                                return #jump Storm_Clothes
                        else:
                                ch_s "Нет, благодарю."
                                return 0

            "Так даже лучше. . .":
                        if StormX.Taboo <= 20 or StormX.HoseNum() >= 5 or StormX in Rules:
                                ch_s "Верно."
                        elif ApprovalCheck(StormX, 1100, "LI", TabM=3) and StormX.Love > StormX.Inbt:
                                ch_s "Верно."
                        elif ApprovalCheck(StormX, 700, "OI", TabM=3) and StormX.Obed > StormX.Inbt:
                                ch_s "Да. . ."
                        elif ApprovalCheck(StormX, 600, "I", TabM=3):
                                ch_s "Хммм. . ."
                        elif ApprovalCheck(StormX, 1300, TabM=3):
                                ch_s "Согласна."
                        else:
                                $ StormX.FaceChange("bemused")
                                if StormX.Taboo > 20:
                                    ch_s "Естественно, но не на людях, [StormX.Petname]."
                                else:
                                    ch_s "Боюсь, что нет, [StormX.Petname]!"
                                call expression StormX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно.":
                ch_s "Ладно. . ."
                return 0
        return 1
        #End of Storm Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Storm_Clothes_Under:
        "Верх":
            menu:
                "Может, снимешь [get_clothing_name(StormX.Chest_key, vin)]?" if StormX.Chest:
                        $ StormX.FaceChange("bemused", 1)

                        if StormX.Taboo <= 20 or StormX in Rules or StormX.OverNum() >= 5:
                            ch_s "Хорошо."
                        elif StormX.SeenChest and ApprovalCheck(StormX, 900, TabM=2.7):
                            ch_s "Хорошо."
#                        elif ApprovalCheck(StormX, 1100, TabM=2):
#                            if StormX.Taboo:
#                                ch_s "I don't know, here. . ."
#                            else:
#                                ch_s "Maybe. . ."
                        elif StormX.Over == "jacket" and ApprovalCheck(StormX, 600, TabM=2):
                            ch_s "Я буду выглядеть слишком откровенно. . ."
#                        elif StormX.Over and ApprovalCheck(StormX, 500, TabM=2):
#                            ch_s "I guess I could. . ."
                        elif not StormX.Over:
                            call Display_DressScreen(StormX)
                            if not _return:
                                ch_s "Сначала мне нужно накинуть что-нибудь поверх."
                                return #jump Storm_Clothes
                        else:
                            call Display_DressScreen(StormX)
                            if not _return:
                                ch_s "Боюсь, что нет."
                                return #jump Storm_Clothes
                        $ Line = get_clothing_name(StormX.Chest_key, vin)
                        $ StormX.Chest = 0
                        if StormX.Over:
                            "Она залезает под [StormX.Over], хватает и снимает [Line], а затем бросает на пол."
                        else:
                            "Она снимает [Line] и кидает на пол."
                            if not renpy.showing('DressScreen'):
                                call Girl_First_Topless(StormX)


                "Примерь майку." if StormX.Chest != "tube top":
                        ch_s "Хорошо."
                        $ StormX.Chest = "tube top"

                "Примерь спортивный лифчик." if StormX.Chest != "sports bra":
                        ch_s "Хорошо."
                        $ StormX.Chest = "sports bra"

                "Мне нравится твой черный лифчик." if StormX.Chest != "black bra":
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.OverNum() >= 5:
                            ch_s "Хорошо."
                            $ StormX.Chest = "black bra"
                        elif StormX.SeenChest or ApprovalCheck(StormX, 1100, TabM=2):
                            ch_s "Хорошо."
                            $ StormX.Chest = "black bra"
                        else:
                            call Display_DressScreen(StormX)
                            if not _return:
                                ch_s "Он почти ничего не прикрывает. . ."
                            else:
                                $ StormX.Chest = "black bra"

                "Мне нравится твой кружевной лифчик." if StormX.Chest != "lace bra" and "lace bra" in StormX.Inventory:
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.OverNum() >= 5:
                            ch_s "Хорошо."
                            $ StormX.Chest = "lace bra"
                        elif StormX.SeenChest or ApprovalCheck(StormX, 1300, TabM=2):
                            ch_s "Хорошо."
                            $ StormX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(StormX)
                            if not _return:
                                ch_s "Он слегка прозрачный. . ."
                            else:
                                $ StormX.Chest = "lace bra"

                "Мне нравится твой лифчик бикини." if StormX.Chest != "bikini top" and "bikini top" in StormX.Inventory:
                        if bg_current == "bg pool":
                                ch_s "Хорошо."
                                $ StormX.Chest = "bikini top"
                        else:
                                if StormX.Taboo <= 20 or StormX in Rules or StormX.OverNum() >= 5:
                                    ch_s "Хорошо."
                                    $ StormX.Chest = "bikini top"
                                elif StormX.SeenChest or ApprovalCheck(StormX, 1000, TabM=2):
                                    ch_s "Хорошо."
                                    $ StormX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(StormX)
                                    if not _return:
                                            ch_s "Тут не место для \"бикини\". . ."
                                    else:
                                            $ StormX.Chest = "bikini top"

                "Мне нравится тот лифчик, который был на тебе во время вечеринки." if StormX.Chest != "cos bra" and "halloween" in StormX.History:
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.OverNum() >= 5:
                            ch_s "Хорошо."
                            $ StormX.Chest = "cos bra"
                        elif StormX.SeenChest or ApprovalCheck(StormX, 1100, TabM=2):
                            ch_s "Хорошо."
                            $ StormX.Chest = "cos bra"
                        else:
                            call Display_DressScreen(StormX)
                            if not _return:
                                ch_s "Он почти ничего не прикрывает. . ."
                            else:
                                $ StormX.Chest = "cos bra"

                "Неважно":
                        pass
            return #jump Storm_Clothes_Under

        "Варианты колготок и чулок":
            menu:
                "Сними [get_clothing_name(StormX.Hose_key, vin)]." if StormX.Hose:
                                $ StormX.Hose = 0
                "Чулки дополнили бы твой образ." if StormX.Hose != "stockings":
                                $ StormX.Hose = "stockings"
                "Колготки дополнили бы твой образ." if StormX.Hose != "pantyhose":
                                $ StormX.Hose = "pantyhose"
                "Рваные колготки дополнили бы твой образ." if StormX.Hose != "ripped pantyhose" and "ripped pantyhose" in StormX.Inventory:
                                $ StormX.Hose = "ripped pantyhose"
                "Чулки и пояс с подвязками дополнили бы твой образ." if StormX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in StormX.Inventory:
                                $ StormX.Hose = "stockings and garterbelt"
                "Может, наденешь только пояс с подвязками?" if StormX.Hose != "garterbelt" and "stockings and garterbelt" in StormX.Inventory:
                                $ StormX.Hose = "garterbelt"
                "Неважно":
                        pass
            return #jump Storm_Clothes_Under

        #Panties
        "Низ":
            menu:
                "Ты должна снять [get_clothing_name(StormX.Panties_key, vin)]. . ." if StormX.Panties:
                        $ StormX.FaceChange("bemused", 1)
                        if StormX.Taboo <= 20 or StormX.HoseNum() >= 5 or StormX.PantsNum() >= 5 or StormX in Rules:
                                ch_s "Конечно."
#                        elif ApprovalCheck(StormX, 900) and (StormX.Legs or (StormX.SeenPussy and not StormX.Taboo)):
#                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
#                                if ApprovalCheck(StormX, 850, "L"):
#                                        ch_s "True. . ."
#                                elif ApprovalCheck(StormX, 500, "O"):
#                                        ch_s "Agreed."
#                                elif ApprovalCheck(StormX, 350, "I"):
#                                        ch_s "Heh."
#                                else:
#                                        ch_s "Sure, I guess."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(StormX, 1100, "LI", TabM=3) and StormX.Love > StormX.Inbt:
                                        ch_s "Пожалуй, я могла бы, но. . ."
                                elif ApprovalCheck(StormX, 700, "OI", TabM=3) and StormX.Obed > StormX.Inbt:
                                        ch_s "Хорошо. . ."
                                elif ApprovalCheck(StormX, 600, "I", TabM=3):
                                        ch_s "Хммм. . ."
                                elif ApprovalCheck(StormX, 1300, TabM=3):
                                        ch_s "Ладно-ладно."
                                else:
                                        call Display_DressScreen(StormX)
                                        if not _return:
                                            $ StormX.FaceChange("bemused")
                                            if StormX.Taboo >= 20:
                                                ch_s "Естественно, но не на людях, [StormX.Petname]."
                                            else:
                                                ch_s "Боюсь, что нет, [StormX.Petname]!"
                                            return #jump Storm_Clothes
                        $ Line = get_clothing_name(StormX.Panties_key, vin)
                        $ StormX.Panties = 0
                        if not StormX.Legs:
                            "Она снимает [Line], а затем бросает их на пол."
                            if not renpy.showing('DressScreen'):
                                    call Girl_First_Bottomless(StormX)
                        elif ApprovalCheck(StormX, 1200, TabM=4):
                            $ Trigger = StormX.Legs
                            $ StormX.Legs = 0
                            pause 0.5
                            $ StormX.Legs = Trigger
                            "Она снимает [get_clothing_name(StormX.Legs_key, vin)] и [Line], затем снова надевает [get_clothing_name(StormX.Legs_key, vin)]."
                            $ Trigger = 1
                            call Girl_First_Bottomless(StormX,1)
                        elif StormX.Legs == "skirt":
                            "Она залезает под юбку и снимает [Line]."
                        else:
                            $ StormX.Blush = 1
                            "Она на мгновение отходит, а затем возвращается."
                            $ StormX.Blush = 0
                        $ Line = 0

                "Почему бы тебе вместо этих не надеть белые трусики?" if StormX.Panties and StormX.Panties != "white panties":
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                                ch_s "Хорошо."
                                $ StormX.Panties = "white panties"
                        elif ApprovalCheck(StormX, 1100, TabM=3):
                                ch_s "Ладно."
                                $ StormX.Panties = "white panties"
                        else:
                                call Display_DressScreen(StormX)
                                if not _return:
                                        ch_s "Это совершенно тебя не касается."
                                else:
                                    $ StormX.Panties = "white panties"

                "Почему бы тебе вместо этих не надеть черные трусики?" if StormX.Panties and StormX.Panties != "black panties":
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                                ch_s "Хорошо."
                                $ StormX.Panties = "black panties"
                        elif ApprovalCheck(StormX, 1100, TabM=3):
                                ch_s "Ладно."
                                $ StormX.Panties = "black panties"
                        else:
                                call Display_DressScreen(StormX)
                                if not _return:
                                        ch_s "Это совершенно тебя не касается."
                                else:
                                    $ StormX.Panties = "black panties"

                "Почему бы тебе вместо этих не надеть кружевные трусики?" if "lace panties" in StormX.Inventory and StormX.Panties and StormX.Panties != "lace panties":
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                                ch_s "Хорошо."
                                $ StormX.Panties = "lace panties"
                        elif ApprovalCheck(StormX, 1300, TabM=3):
                                ch_s "Пожалуй, можно."
                                $ StormX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(StormX)
                                if not _return:
                                        ch_s "Это совершенно тебя не касается."
                                else:
                                    $ StormX.Panties = "lace panties"

                "Мне нравятся твои трусики бикини." if "bikini bottoms" in StormX.Inventory and StormX.Panties != "bikini bottoms":
                        if bg_current == "bg pool":
                                ch_s "Хорошо."
                                $ StormX.Panties = "bikini bottoms"
                        else:
                                if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                                    ch_s "Хорошо."
                                    $ StormX.Panties = "bikini bottoms"
                                elif ApprovalCheck(StormX, 1000, TabM=2):
                                    ch_s "Хорошо."
                                    $ StormX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(StormX)
                                    if not _return:
                                            ch_s "Тут не место для \"бикини\". . ."
                                    else:
                                            $ StormX.Panties = "bikini bottoms"

                "Почему бы тебе не надеть те трусики с вечеринки?" if StormX.Panties and "halloween" in StormX.History and StormX.Panties != "cos panties":
                        if StormX.Taboo <= 20 or StormX in Rules or StormX.PantsNum() >= 5:
                                ch_s "Хорошо."
                                $ StormX.Panties = "cos panties"
                        elif ApprovalCheck(StormX, 1100, TabM=3):
                                ch_s "Ладно."
                                $ StormX.Panties = "cos panties"
                        else:
                                call Display_DressScreen(StormX)
                                if not _return:
                                        ch_s "Это совершенно тебя не касается."
                                else:
                                    $ StormX.Panties = "cos panties"

                "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not StormX.Panties:
                        $ StormX.FaceChange("bemused", 1)
                        if StormX.Legs and (StormX.Love+StormX.Obed) <= (2 * StormX.Inbt):
                            $ StormX.Mouth = "smile"
                            ch_s "Я не уверена насчет этого."
                            menu:
                                "Ну ладно.":
                                    return #jump Storm_Clothes
                                "Я настаиваю, надевай.":
                                    if (StormX.Love+StormX.Obed) <= (1.5 * StormX.Inbt):
                                        $ StormX.FaceChange("angry", Eyes="side")
                                        ch_s "Я же настаиваю на обратном."
                                        return #jump Storm_Clothes
                                    else:
                                        $ StormX.FaceChange("sadside")
                                        ch_s "Ох, ладно. . ."
                        else:
                            ch_s "Которые?"
                        menu:
                            extend ""
                            "Как насчет белых?":
                                    ch_s "Хорошо."
                                    $ StormX.Panties = "white panties"
                            "Как насчет черных?":
                                    ch_s "Хорошо."
                                    $ StormX.Panties = "black panties"
                            "Как насчет кружевных?" if "lace panties" in StormX.Inventory:
                                    ch_s "Хорошо."
                                    $ StormX.Panties  = "lace panties"
                            "Как насчет трусиков бикини?" if "bikini bottoms" in StormX.Inventory:
                                    ch_s "Хорошо."
                                    $ StormX.Panties = "bikini bottoms"
                            "Как насчет трусиков с вечеринки?" if "halloween" in StormX.History:
                                    ch_s "Хорошо."
                                    $ StormX.Panties = "cos panties"
                "Неважно":
                    pass
            return #jump Storm_Clothes_Under
        "Неважно":
            pass
    return #jump Storm_Clothes
    #End of Storm Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Storm_Clothes_Misc:
        #Misc
        "Длинные волосы" if StormX.Hair != "long" and StormX.Hair != "wet":
                ch_p "Ты хорошо выглядишь с длинными волосами."
                if "hair" in StormX.RecentActions:
                    ch_s "Я уже слишком долго возилась с прической сегодня."
                elif ApprovalCheck(StormX, 900):
                    ch_s "Ох, ты так думаешь?"
                    ch_s "Пожалуй, я могу поговорить об этом с Хэнком. . ."
                    show blackscreen onlayer black
                    $ Round -5 if Round >= 10 else 0
                    "Она отходит на несколько минут."
                    hide blackscreen onlayer black
                    if StormX.Hair == "wethawk":
                            $ StormX.Hair = "wet"
                    else:
                            $ StormX.Hair = "long"
                    $ StormX.AddWord(1,"hair","hair",0,0)
                    ch_s "Так?"
                else:
                    ch_s "Благодарю, но сейчас меня такой стиль не интересует."

        "Могавк" if "mohawk" in StormX.History and (StormX.Hair != "mohawk" and StormX.Hair != "wethawk"):
                ch_p "Ты хорошо выглядишь с могавком."
                if "hair" in StormX.RecentActions:
                    ch_s "Я уже слишком долго возилась с прической сегодня."
                elif ApprovalCheck(StormX, 900):
                    ch_s "Тебе он понравился?"
                    show blackscreen onlayer black
                    $ Round -5 if Round >= 10 else 0
                    "Она отходит на несколько минут."
                    hide blackscreen onlayer black
                    if StormX.Hair == "wet":
                            $ StormX.Hair = "wethawk"
                    else:
                            $ StormX.Hair = "mohawk"
                    $ StormX.AddWord(1,"hair","hair",0,0)
                    ch_s "Так?"
                else:
                    ch_s "Благодарю, но сейчас меня такой стиль не интересует."

        "Короткие волосы" if StormX.Hair != "short" and "halloween" in StormX.History:
                ch_p "Ты хорошо выглядишь с короткими волосами."
                if "hair" in StormX.RecentActions:
                    ch_s "Я уже слишком долго возилась с прической сегодня."
                elif ApprovalCheck(StormX, 900):
                    ch_s "Ох, ты так думаешь?"
                    ch_s "Пожалуй, я могу поговорить об этом с Хэнком. . ."
                    show blackscreen onlayer black
                    $ Round -5 if Round >= 10 else 0
                    "Она отходит на несколько минут."
                    hide blackscreen onlayer black
                    $ StormX.Hair = "short"
                    $ StormX.AddWord(1,"hair","hair",0,0)
                    ch_s "Так?"
                else:
                    ch_s "Благодарю, но сейчас меня такой стиль не интересует."

        "Влажные волосы" if StormX.Hair != "wet" and StormX.Hair != "wethawk":
                ch_p "Тебе стоит увлажнить волосы."
                if ApprovalCheck(StormX, 800):
                    ch_s "Правда?"
                    if StormX.Hair == "mohawk":
                            $ StormX.Hair = "wethawk"
                    else:
                            $ StormX.Hair = "wet"
                    "Концентрированный ураган пару мгновений кружит вокруг ее головы, приводя ее волосы в нужное состояние."
                    ch_s "Так?"
                else:
                    ch_s "Я бы этого не хотела."

        "Сухие волосы" if StormX.Hair == "wet" or StormX.Hair == "wethawk":
                ch_p "Тебе идут сухие волосы."
                if ApprovalCheck(StormX, 600):
                    ch_s "Хорошо."
                    "Возникают порывы ветра, которые обсушивают ее волосы."
                    if StormX.Hair == "wethawk":
                            $ StormX.Hair = "mohawk"
                    else:
                            $ StormX.Hair = "long"
                else:
                    ch_s "Я не уверена, думаю, и так нормально."

        "Отрасти волосы на лобке" if not StormX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может, отрастишь?"
                call expression StormX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in StormX.Todo:
                        $ StormX.FaceChange("bemused", 1)
                        ch_s "Они не могут отрасти мгновенно!"
                else:
                        $ StormX.FaceChange("bemused", 1)
                        if ApprovalCheck(StormX, 500, TabM=0):
                            ch_s "Мне тоже так больше нравится. . ."
                        else:
                            $ StormX.FaceChange("surprised")
                            $ StormX.Brows = "angry"
                            ch_s "Я не нуждаюсь в твоих советах."
                            return #jump Storm_Clothes
                        $ StormX.Todo.append("pubes")
                        $ StormX.PubeC = 6
        "Побрей лобок" if StormX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression StormX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ StormX.FaceChange("bemused", 1)
                if "shave" in StormX.Todo:
                    ch_s "Да, я займусь этим."
                else:
                    if ApprovalCheck(StormX, 1100, TabM=0):
                        ch_s "Да? Пожалуй, я могу побрить. . ."
                    else:
                        $ StormX.FaceChange("surprised")
                        $ StormX.Brows = "angry"
                        ch_s "Это тебя не касается."
                        return #jump Storm_Clothes
                    $ StormX.Todo.append("shave")

#        "Пирсинг. [[Сначала посмотрите, как она выглядит без него] (locked)" if not StormX.SeenPussy and not StormX.SeenChest:
#            pass

        "Надень пирсинг-кольца" if StormX.Pierce != "ring": #and (StormX.SeenPussy or StormX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсингом-кольцами."
                if "ring" in StormX.Todo:
                    ch_s "Знаю, скоро я все сделаю."
                else:
                    $ StormX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(StormX, 1150, TabM=0)
                    if ApprovalCheck(StormX, 900, "L", TabM=0) or (Approval and StormX.Love > 2* StormX.Obed):
                        ch_s "Тебе нравится представлять, как он будет смотреться на мне?"
                    elif ApprovalCheck(StormX, 600, "I", TabM=0) or (Approval and StormX.Inbt > StormX.Obed):
                        ch_s "Я уже как-то подумывала его сделать."
                    elif ApprovalCheck(StormX, 500, "O", TabM=0) or Approval:
                        ch_s "Да, [StormX.Petname]."
                    else:
                        $ StormX.FaceChange("bemused")
                        ch_s "Я бы предпочла этого не делать, [StormX.Petname]."
                        return #jump Storm_Clothes
                    $ StormX.Todo.append("ring")

        "Надень пирсинг-штанги" if StormX.Pierce != "barbell":# and (StormX.SeenPussy or StormX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in StormX.Todo:
                    ch_s "Знаю, скоро я все сделаю."
                else:
                    $ StormX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(StormX, 1150, TabM=0)
                    if ApprovalCheck(StormX, 900, "L", TabM=0) or (Approval and StormX.Love > 2 * StormX.Obed):
                        ch_s "Тебе нравится представлять, как он будет смотреться на мне?"
                    elif ApprovalCheck(StormX, 600, "I", TabM=0) or (Approval and StormX.Inbt > StormX.Obed):
                        ch_s "Я уже как-то подумывала его сделать."
                    elif ApprovalCheck(StormX, 500, "O", TabM=0) or Approval:
                        ch_s "Да, [StormX.Petname]."
                    else:
                        $ StormX.FaceChange("bemused")
                        ch_s "Я бы предпочла этого не делать, [StormX.Petname]."
                        return #jump Storm_Clothes
                    $ StormX.Todo.append("barbell")

        "Сними пирсинг" if StormX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ StormX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(StormX, 1350, TabM=0)
                if ApprovalCheck(StormX, 950, "L", TabM=0) or (Approval and StormX.Love > StormX.Obed):
                    ch_s "Серьезно? Что ж, хорошо. . ."
                elif ApprovalCheck(StormX, 700, "I", TabM=0) or (Approval and StormX.Inbt > StormX.Obed):
                    ch_s "Ох, я уже привязалась к нему. . ."
                elif ApprovalCheck(StormX, 600, "O", TabM=0) or Approval:
                    ch_s "Хорошо."
                else:
                    $ StormX.FaceChange("surprised")
                    $ StormX.Brows = "angry"
                    ch_s "Я уже очень привязалась к нему."
                    return #jump Storm_Clothes
                $ StormX.Pierce = 0

        "Надень золотое ожерелье" if StormX.Neck != "gold necklace":
                ch_p "Почему бы тебе не надеть золотое ожерелье?"
                ch_s "Ладно. . ."
                $ StormX.Neck = "gold necklace"
        "Надень ожерелье-кольцо" if StormX.Neck != "rings" and "halloween" in StormX.History:
                ch_p "Почему бы тебе не надеть ожерелье-кольцо?"
                ch_s "Ладно. . ."
                $ StormX.Neck = "rings"
        "Сними ожерелье" if StormX.Neck:
                ch_p "Может, снимешь украшения с шеи?"
                ch_s "Ладно. . ."
                $ StormX.Neck = 0

        "Надень обручи для рук и ног" if StormX.Acc != "rings" and "halloween" in StormX.History:
                ch_p "Почему бы тебе не надеть обручи для тела?"
                ch_s "Ладно. . ."
                $ StormX.Acc = "rings"
        "Сними обручи для рук и ног" if StormX.Acc == "rings":
                ch_p "Почему бы тебе не снять обручи для тела?"
                ch_s "Ладно. . ."
                $ StormX.Acc = 0

#        "Why don't you put those wristbands on." if StormX.Arms != "wrists":
#                ch_s "Ok. . ."
#                $ StormX.Arms = "wrists"
#        "Maybe go without the wristbands." if StormX.Arms:
#                ch_s "Ok. . ."
#                $ StormX.Arms = 0

        "Неважно":
            pass
    return #jump Storm_Clothes
    #End of Storm Misc Wardrobe

return
#End Storm Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
