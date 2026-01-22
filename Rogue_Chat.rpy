##Rogue Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Rogue_Relationship: #rkelj
    while True:
        menu:
            ch_r "О чем ты хочешь поговорить?"
            "Хочешь стать моей девушкой?" if RogueX not in Player.Harem and "ex" not in RogueX.Traits:
                    $ RogueX.DailyActions.append("relationship")
                    if "asked boyfriend" in RogueX.DailyActions and "angry" in RogueX.DailyActions:
                            $ RogueX.FaceChange("angry", 1)
                            ch_r "Перестань меня доставать, я серьезно."
                            return
                    elif "asked boyfriend" in RogueX.DailyActions:
                            $ RogueX.FaceChange("angry", 1)
                            if not Player.Male:
                                ch_r "Ты уже спрашивала об этом, мой ответ все равно \"нет\"."
                            else:
                                ch_r "Ты уже спрашивал об этом, мой ответ все равно \"нет\"."
                            return
                    elif RogueX.Break[0]:
                            $ RogueX.FaceChange("angry", 1)
                            ch_r "Я уже говорила тебе, не когда ты с ней."
                            if Player.Harem:
                                    $ RogueX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "Я больше не с ней."

                    $ RogueX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "RogueYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_r "Это было бы нечестно по отношению к остальным, [RogueX.Petname]."
                        else:
                            ch_r "Между нами стоит [Player.Harem[0].Name], это было бы нечестно по отношению к ней, [RogueX.Petname]."
                        return

                    if RogueX.Event[5]:
                            $ RogueX.FaceChange("bemused", 1)
                            ch_r "Как-то я уже заводила такой разговор. . ."
                    else:
                            $ RogueX.FaceChange("surprised", 2)
                            ch_r "Вау, как неожиданно, [RogueX.Petname]. . ."
                            $ RogueX.FaceChange("smile", 1)

                    call Rogue_OtherWoman

                    if RogueX.Love >= 800:
                            $ RogueX.FaceChange("surprised", 1)
                            $ RogueX.Mouth = "grimace"
                            if not RogueX.Event[5]:
                                    $ RogueX.Statup("Love", 200, 10)
                                    call Rogue_BF
                                    return
                            $ RogueX.Statup("Love", 200, 40)
                            ch_r "С удовольствием!"
                            if "boyfriend" not in RogueX.Petnames:
                                        $ RogueX.Petnames.append("boyfriend")
                            if "RogueYes" in Player.Traits:
                                    $ Player.Traits.remove("RogueYes")
                            $ Player.Harem.append(RogueX)
                            call Harem_Initiation
                            "[RogueX.Name] подпрыгивает и страстно целует вас."
                            $ RogueX.FaceChange("kiss", 1)
                            $ RogueX.Kissed += 1
                    elif RogueX.Obed >= 500:
                            $ RogueX.FaceChange("perplexed")
                            ch_r "Не уверена, что при наших отношениях мы сможем \"встречаться.\""
                    elif RogueX.Inbt >= 500:
                            $ RogueX.FaceChange("smile")
                            ch_r "Если честно, я не хочу быть связана обязательствами."
                    else:
                            $ RogueX.FaceChange("perplexed", 1)
                            ch_r "Сейчас я не испытываю к тебе особых чувств, [RogueX.Petname]."

            "Может, начнем все сначала?" if "ex" in RogueX.Traits:
                    $ RogueX.DailyActions.append("relationship")
                    if "asked boyfriend" in RogueX.DailyActions and "angry" in RogueX.DailyActions:
                            $ RogueX.FaceChange("angry", 1)
                            ch_r "Перестань меня доставать, я серьезно."
                            return
                    elif "asked boyfriend" in RogueX.DailyActions:
                            $ RogueX.FaceChange("angry", 1)
                            if not Player.Male:
                                ch_r "Ты уже спрашивала об этом, мой ответ все равно \"нет\"."
                            else:
                                ch_r "Ты уже спрашивал об этом, мой ответ все равно \"нет\"."
                            return

                    $ RogueX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "RogueYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_r "Это было бы нечестно по отношению к остальным, [RogueX.Petname]."
                            else:
                                ch_r "Между нами стоит [Player.Harem[0].Name], это было бы нечестно по отношению к ней, [RogueX.Petname]."
                            return

                    $ Cnt = 0
                    call Rogue_OtherWoman

                    if RogueX.Love >= 800:
                            $ RogueX.FaceChange("surprised", 1)
                            $ RogueX.Mouth = "grimace"
                            $ RogueX.Statup("Love", 90, 5)
                            if not Player.Male:
                                ch_r "Если ты готова, то я тоже!"
                            else:
                                ch_r "Если ты готов, то я тоже!"
                            if "boyfriend" not in RogueX.Petnames:
                                        $ RogueX.Petnames.append("boyfriend")
                            $ RogueX.Traits.remove("ex")
                            if "RogueYes" in Player.Traits:
                                    $ Player.Traits.remove("RogueYes")
                            $ Player.Harem.append(RogueX)
                            call Harem_Initiation
                            "[RogueX.Name] подпрыгивает и страстно целует вас."
                            $ RogueX.FaceChange("kiss", 1)
                            $ RogueX.Kissed += 1
                    elif RogueX.Love >= 600 and ApprovalCheck(RogueX, 1500):
                            $ RogueX.FaceChange("smile", 1)
                            $ RogueX.Mouth = "grimace"
                            $ RogueX.Statup("Love", 90, 5)
                            ch_r "Мы можем попробовать еще раз."
                            if "boyfriend" not in RogueX.Petnames:
                                        $ RogueX.Petnames.append("boyfriend")
                            $ RogueX.Traits.remove("ex")
                            if "RogueYes" in Player.Traits:
                                    $ Player.Traits.remove("RogueYes")
                            $ Player.Harem.append(RogueX)
                            call Harem_Initiation
                            "[RogueX.Name] одаривает вас быстрым поцелуем."
                            $ RogueX.FaceChange("kiss", 1)
                            $ RogueX.Kissed += 1
                    elif RogueX.Obed >= 500:
                            $ RogueX.FaceChange("sad")
                            ch_r "Хоть что-то подобное и было между нами раньше, теперь все по-другому."
                    elif RogueX.Inbt >= 500:
                            $ RogueX.FaceChange("perplexed")
                            ch_r "Мы уже пытались, но ничего не вышло."
                    else:
                            $ RogueX.FaceChange("perplexed", 1)
                            if not Player.Male:
                                ch_r "Я не хочу, чтобы ты снова разбила мне сердце, [RogueX.Petname]."
                            else:
                                ch_r "Я не хочу, чтобы ты снова разбил мне сердце, [RogueX.Petname]."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if RogueX in Player.Harem:
                        call AskDateOther

            "Думаю, мы должны расстаться." if RogueX in Player.Harem:
                        if "breakup talk" in RogueX.RecentActions:
                                ch_r "Не смешно, [RogueX.Petname], совсем. Мы {i}недавно{/i} проходили через это."
                        elif "breakup talk" in RogueX.DailyActions:
                                if not Player.Male:
                                    ch_r "Так быстро снова устала от меня?"
                                else:
                                    ch_r "Так быстро снова устал от меня?"
                                ch_r "Сегодня мы не будем об этом говорить, [RogueX.Petname]."
                        else:
                                call Breakup(RogueX)

            "О разговоре, который у нас был ранее. . .":
                menu:
                    "Ты была не девственницей?" if RogueX.Sex and not RogueX.Chat[0]:
                        call Rogue_Not_Virgin

                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоей хозяйкой?" if RogueX.Event[8] and "master" not in RogueX.Petnames and not Player.Male:
                        menu:
                            ch_r "Да?"
                            "Теперь я готова.":
                                        if ApprovalCheck(RogueX, 800, "O"):
                                            $ RogueX.FaceChange("sexy", 1)
                                            ch_r "Надеюсь, я буду хорошо служить тебе, хозяйка."
                                            $ RogueX.Statup("Obed", 200, 100)
                                            $ RogueX.Petnames.append("master")
                                            $ RogueX.Event[8] = 2
                                        else:
                                            ch_r "Ну, мне эта затея больше не кажется такой заманчивой."
                                            ch_r "Ну, может быть, потом я передумаю."
                            "Неважно.":
                                        $ RogueX.FaceChange("sad")
                                        ch_r "Ох."
                                        $ RogueX.Statup("Obed", 200, -5)
                                        $ RogueX.Statup("Love", 90, -5)

                    "Помнишь, ты говорила, что хочешь, чтобы я стал твоим хозяином?" if RogueX.Event[8] and "master" not in RogueX.Petnames and Player.Male:
                        menu:
                            ch_r "Да?"
                            "Теперь я готов.":
                                        if ApprovalCheck(RogueX, 800, "O"):
                                            $ RogueX.FaceChange("sexy", 1)
                                            ch_r "Надеюсь, я буду хорошо служить тебе, хозяин."
                                            $ RogueX.Statup("Obed", 200, 100)
                                            $ RogueX.Petnames.append("master")
                                            $ RogueX.Event[8] = 2
                                        else:
                                            ch_r "Ну, мне эта затея больше не кажется такой заманчивой."
                                            ch_r "Ну, может быть, потом я передумаю."
                            "Неважно.":
                                        $ RogueX.FaceChange("sad")
                                        ch_r "Ох."
                                        $ RogueX.Statup("Obed", 200, -5)
                                        $ RogueX.Statup("Love", 90, -5)
                    "Неважно.":
                        pass
            "Неважно.":
                return
        return


label Rogue_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((RogueX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ RogueX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_r "А как же [Player.Harem[0].Name] и другие девушки?!"
    else:
        ch_r "А как же [Player.Harem[0].Name]?!"
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "RogueYes" in Player.Traits:
                if ApprovalCheck(RogueX, 1800, Bonus = Cnt):
                    $ RogueX.FaceChange("smile", 1)
                    if RogueX.Love >= RogueX.Obed:
                            ch_r "Пожалуй, пока мы можем быть вместе, я могу поделиться."
                    elif RogueX.Obed >= RogueX.Inbt:
                            ch_r "Ну, тогда я нискажу ни слова против."
                    else:
                            ch_r "Хорошо, конечно."
                else:
                    $ RogueX.FaceChange("angry", 1)
                    ch_r "Ну она и шлюха!"
                    $ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "RogueYes" not in Player.Traits and not Player.Male:
                if ApprovalCheck(RogueX, 1800, Bonus = Cnt):
                        $ RogueX.FaceChange("smile", 1)
                        if RogueX.Love >= RogueX.Obed:
                            ch_r "Пожалуй, пока мы можем быть вместе, я могу поделиться."
                        elif RogueX.Obed >= RogueX.Inbt:
                            ch_r "Ну, такой вариант меня бы устроил."
                        else:
                            ch_r "Хорошо, конечно."
                        ch_r "Сходи и узнай ее ответ, а завтра расскажешь мне о ее решение."
                else:
                        $ RogueX.FaceChange("angry", 1)
                        ch_r "Ну она и шлюха!"
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "RogueYes" not in Player.Traits and Player.Male:
                if ApprovalCheck(RogueX, 1800, Bonus = Cnt):
                        $ RogueX.FaceChange("smile", 1)
                        if RogueX.Love >= RogueX.Obed:
                            ch_r "Пожалуй, пока мы можем быть вместе, я могу поделиться."
                        elif RogueX.Obed >= RogueX.Inbt:
                            ch_r "Ну, такой вариант меня бы устроил."
                        else:
                            ch_r "Хорошо, конечно."
                        ch_r "Сходи и узнай ее ответ, а завтра расскажешь мне о ее решение."
                else:
                        $ RogueX.FaceChange("angry", 1)
                        ch_r "Ну она и шлюха!"
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
                if not ApprovalCheck(RogueX, 1800, Bonus = -Cnt): #checks if She likes you more than the other girl
                        $ RogueX.FaceChange("angry", 1)
                        if not ApprovalCheck(RogueX, 1800):
                                ch_r "Мне не нравится такое решение."
                        else:
                                ch_r "Я не разделяю твой настрой."
                        $ renpy.pop_call()
                else:
                        $ RogueX.FaceChange("smile", 1)
                        if RogueX.Love >= RogueX.Obed:
                                ch_r "Думаю, это неплохой вариант. . ."
                        elif RogueX.Obed >= RogueX.Inbt:
                                ch_r "Если ты настаиваешь."
                        else:
                                ch_r "Почему бы и нет."
                        $ RogueX.AddWord(1,0,0,"downlow")

        "Я могу порвать с ней.":
                    $ RogueX.FaceChange("sad")
                    ch_r "Ну, тогда найди меня после того как закончишь."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ RogueX.FaceChange("sad")
                    ch_r "Ага. . ."
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ RogueX.FaceChange("sad")
                    ch_r "Ага. . ."
                    $ renpy.pop_call()

    return


label Rogue_About(Check=0): #rkeljsvg
    if Check not in TotalGirls:
            ch_r "Кто это?"
            return
    ch_r "Что я думаю о ней? Ну. . ."
    if Check == KittyX:
            if "poly Kitty" in RogueX.Traits:
                ch_r "Думаю, ты и так это знаешь. . ."
            elif RogueX.LikeKitty >= 900:
                ch_r "Думаю, она очень . . . горяча?"
            elif RogueX.LikeKitty >= 800:
                ch_r "Я очень близка с ней, мы лучшие подруги и, возможно, даже больше."
            elif RogueX.LikeKitty >= 700:
                ch_r "Она одна из моих лучших подруг."
            elif RogueX.LikeKitty >= 600:
                ch_r "Мы хорошие подруги."
            elif RogueX.LikeKitty >= 500:
                ch_r "Не знаю. Ну, она нормальная."
            elif RogueX.LikeKitty >= 400:
                ch_r "Мы. . . вроде как, не очень нравимся друг другу."
            elif RogueX.LikeKitty >= 300:
                ch_r "Я не хочу о ней говорить."
            else:
                ch_r "Ты про эту шалаву?"
    elif Check == EmmaX:
            if "poly Emma" in RogueX.Traits:
                ch_r "Ну, я уж точно не выгоню ее из своей постели. . ."
            elif RogueX.LikeEmma >= 900:
                ch_r "Она вполне горяча. . . для преподавателя."
            elif RogueX.LikeEmma >= 800:
                ch_r "Она очень классная, правда? Иногда я даже удивляюсь насколько. . ."
            elif RogueX.LikeEmma >= 700:
                ch_r "Мы иногда проводим время вместе после занятий, с ней интересно поговорить."
            elif RogueX.LikeEmma >= 600:
                ch_r "Она просто отличный преподаватель, мне нравятся ее лекции."
            elif RogueX.LikeEmma >= 500:
                ch_r "Не знаю. Ну, она нормальная."
            elif RogueX.LikeEmma >= 400:
                ch_r "Мне не очень нравится, как она смотрит на тебя во время занятий."
            elif RogueX.LikeEmma >= 300:
                ch_r "Я ненавижу ее занятия."
            else:
                ch_r "Она самая настоящая ВЕДЬМА!"
    elif Check == LauraX:
            if "poly Laura" in RogueX.Traits:
                ch_r "Мы время от времени спим вместе. . ."
            elif RogueX.LikeLaura >= 900:
                ch_r "В ней есть животный магнетизм. . ."
            elif RogueX.LikeLaura >= 800:
                ch_r "Кажется, мы хорошо ладим. . ."
            elif RogueX.LikeLaura >= 700:
                ch_r "Она хорошая подруга."
            elif RogueX.LikeLaura >= 600:
                ch_r "Она хороший товарищ."
            elif RogueX.LikeLaura >= 500:
                ch_r "Не знаю. Ну, она хороша в бою."
            elif RogueX.LikeLaura >= 400:
                ch_r "Мы. . . не особо ладим."
            elif RogueX.LikeLaura >= 300:
                ch_r "Я не хочу о ней говорить."
            else:
                ch_r "Ты про эту шалаву?"
    elif Check == JeanX:
            if "poly Jean" in RogueX.Traits:
                ch_r "Мы время от времени спим вместе. . ."
            elif RogueX.LikeJean >= 900:
                ch_r "Она очень привлекательная. . ."
            elif RogueX.LikeJean >= 800:
                ch_r "Кажется, мы хорошо ладим. . ."
            elif RogueX.LikeJean >= 700:
                ch_r "Она. . . моя подруга."
            elif RogueX.LikeJean >= 600:
                ch_r "Она хороший товарищ."
            elif RogueX.LikeJean >= 500:
                ch_r "Не знаю. Ну, она нормальная."
            elif RogueX.LikeJean >= 400:
                ch_r "Мы. . . не особо ладим."
            elif RogueX.LikeJean >= 300:
                ch_r "Она. . . моя подруга."
            else:
                ch_r "Ты про эту шлюховатую ведьму?!"
    elif Check == StormX:
            if "poly Storm" in RogueX.Traits:
                ch_r "Ну, с ней приятно обниматься. . ."
            elif RogueX.LikeStorm >= 900:
                ch_r "Она мне нравится."
            elif RogueX.LikeStorm >= 800:
                ch_r "Она классная, правда? Я даже удивляюсь насколько. . ."
            elif RogueX.LikeStorm >= 700:
                ch_r "Мы иногда разговариваем после занятий, она хороший слушатель."
            elif RogueX.LikeStorm >= 600:
                ch_r "Она просто отличный преподаватель, мне нравятся ее лекции."
            elif RogueX.LikeStorm >= 500:
                ch_r "Не знаю. Ну, она нормальная."
            elif RogueX.LikeStorm >= 400:
                ch_r "Мне не очень нравится, как она смотрит на тебя во время занятий."
            elif RogueX.LikeStorm >= 300:
                ch_r "Я ненавижу ее занятия."
            else:
                ch_r "Она самая настоящая ВЕДЬМА!"
    elif Check == JubesX:
            if "poly Jubes" in RogueX.Traits:
                ch_r "Думаю, ты и так это знаешь. . ."
            elif RogueX.LikeJubes >= 900:
                ch_r "Думаю, она очень . . . горяча?"
            elif RogueX.LikeJubes >= 800:
                ch_r "Думаю, мы очень хорошо сработались. . ."
            elif RogueX.LikeJubes >= 700:
                ch_r "Она очень хорошая подруга."
            elif RogueX.LikeJubes >= 600:
                ch_r "Мы подруги."
            elif RogueX.LikeJubes >= 500:
                ch_r "Не знаю. Ну, она нормальная."
            elif RogueX.LikeJubes >= 400:
                ch_r "Мы. . . вроде как, не очень нравимся друг другу."
            elif RogueX.LikeJubes >= 300:
                ch_r "Я не хочу о ней говорить."
            else:
                ch_r "Ты про эту шалаву?"
    elif Check == GwenX:
            if "poly Gwen" in RogueX.Traits:
                ch_r "Думаю, ты и так это знаешь. . ."
            elif RogueX.LikeGwen >= 900:
                ch_r "Я думаю, она очень. . . веселая?"
            elif RogueX.LikeGwen >= 800:
                ch_r "Я думаю, она очень сексуальная. . ."
            elif RogueX.LikeGwen >= 700:
                ch_r "Она очень хорошая подруга."
            elif RogueX.LikeGwen >= 600:
                ch_r "Мы подруги."
            elif RogueX.LikeGwen >= 500:
                ch_r "Не знаю. Ну, она нормальная."
            elif RogueX.LikeGwen >= 400:
                ch_r "Мы. . . вроде как, не очень нравимся друг другу."
            elif RogueX.LikeGwen >= 300:
                ch_r "Я не хочу о ней говорить."
            else:
                ch_r "Ты про эту шалаву?"
    elif Check == BetsyX:
            if "poly Betsy" in RogueX.Traits:
                ch_r "Думаю, ты и так это знаешь. . ."
            elif RogueX.LikeBetsy >= 900:
                ch_r "Я думаю, она очень. . .  горячая?"
            elif RogueX.LikeBetsy >= 800:
                ch_r "Думаю, мы отлично с ней поладили. . ."
            elif RogueX.LikeBetsy >= 700:
                ch_r "Она очень хорошая подруга."
            elif RogueX.LikeBetsy >= 600:
                ch_r "Мы подруги."
            elif RogueX.LikeBetsy >= 500:
                ch_r "Я не знаю, но у нее очень необычный акцент."
            elif RogueX.LikeBetsy >= 400:
                ch_r "Мы. . . особо-то не и не общались."
            elif RogueX.LikeBetsy >= 300:
                ch_r "Я не хочу о ней говорить."
            else:
                ch_r "Ты про эту шалаву?"
    elif Check == DoreenX:
            if "poly Doreen" in RogueX.Traits:
                ch_r "Думаю, ты и так это знаешь. . ."
            elif RogueX.LikeDoreen >= 900:
                ch_r "У нее отличная задница, правда? . ."
            elif RogueX.LikeDoreen >= 800:
                ch_r "Думаю, она очень. . . веселая?"
            elif RogueX.LikeDoreen >= 700:
                ch_r "Она очень хорошая подруга."
            elif RogueX.LikeDoreen >= 600:
                ch_r "Мы подруги."
            elif RogueX.LikeDoreen >= 500:
                ch_r "Мы плохо знакомы, но она кажется очень милой."
            elif RogueX.LikeDoreen >= 400:
                ch_r "Мы. . . особо-то не и не общались."
            elif RogueX.LikeDoreen >= 300:
                ch_r "Я не хочу о ней говорить."
            else:
                ch_r "Ты про ту шалаву?"
    elif Check == WandaX:
            if "poly Wanda" in RogueX.Traits:
                ch_r "Думаю, ты знаешь, как я к ней отношусь. . ."
            elif RogueX.LikeWanda >= 900:
                ch_r "Думаю, она очень . . . сексуальная?"
            elif RogueX.LikeWanda >= 800:
                ch_r "Мне кажется, мы отлично сработались. . ."
            elif RogueX.LikeWanda >= 700:
                ch_r "Она очень хорошая подруга."
            elif RogueX.LikeWanda >= 600:
                ch_r "Мы подруги."
            elif RogueX.LikeWanda >= 500:
                ch_r "Даже не знаю, она нормальная."
            elif RogueX.LikeWanda >= 400:
                ch_r "Мы. . . особо-то не и не общались."
            elif RogueX.LikeWanda >= 300:
                cch_r "Я не хочу о ней говорить."
            else:
                ch_r "Ты про ту шлюху?"
    else:
            ch_r "Я оставлю свое мнение при себе."
    return
# End Rogue Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Rogue_Monogamy:
        #called from Rogue_Settings to ask her not to hook up with other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in RogueX.Traits:
                    if RogueX.Thirst >= 60 and not ApprovalCheck(RogueX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ RogueX.FaceChange("sly",1)
                            if "mono" not in RogueX.DailyActions:
                                    $ RogueX.Statup("Obed", 90, -2)
                            if not Player.Male:
                                ch_r "Как ты можешь указывать мне что делать, когда сама такая недоступная. . ."
                            else:
                                ch_r "Как ты можешь указывать мне что делать, когда сам такой недоступный. . ."
                            return
                    elif ApprovalCheck(RogueX, 1200, "LO", TabM=0) and RogueX.Love >= RogueX.Obed:
                            #she cares
                            $ RogueX.FaceChange("sly",1)
                            if "mono" not in RogueX.DailyActions:
                                    $ RogueX.Statup("Love", 90, 1)
                            ch_r "Ах, значит, ты ревнуешь?"
                            ch_r "Пожалуй, тогда мне лучше воздержаться от этого. . ."
                    elif ApprovalCheck(RogueX, 700, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side")
                            ch_r "Если ты действительно этого хочешь. . ."
                    else:
                            #she doesn't care
                            $ RogueX.FaceChange("sly",1,Brows="confused")
                            ch_r "С кем я \"встречаюсь\" - это мое личное дело."
                            return
                    if "mono" not in RogueX.DailyActions:
                            $ RogueX.Statup("Obed", 90, 3)
                    $ RogueX.AddWord(1,0,"mono","mono") #Daily
            "Не встречайся с другими девушками." if "mono" not in RogueX.Traits:
                    if ApprovalCheck(RogueX, 900, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side")
                            ch_r "Ладно."
                    elif RogueX.Thirst >= 60 and not ApprovalCheck(RogueX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ RogueX.FaceChange("sly",1)
                            if "mono" not in RogueX.DailyActions:
                                    $ RogueX.Statup("Obed", 90, -2)
                            if not Player.Male:
                                ch_r "Как ты можешь указывать мне что делать, когда сама такая недоступная. . ."
                            else:
                                ch_r "Как ты можешь указывать мне что делать, когда сам такой недоступный. . ."
                            return
                    elif ApprovalCheck(RogueX, 550, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side")
                            ch_r "Если ты действительно этого хочешь. . ."
                    elif ApprovalCheck(RogueX, 1400, "LO", TabM=0):
                            #she cares
                            $ RogueX.FaceChange("sly",1)
                            ch_r "Разве о таком можно разговаривать с девушкой?"
                            ch_r "Но ладно, ради тебя я пойду на это. . ."
                    else:
                            #she doesn't care
                            $ RogueX.FaceChange("sly",1,Brows="confused")
                            ch_r "С кем я \"встречаюсь\" - это мое личное дело."
                            return
                    if "mono" not in RogueX.DailyActions:
                            $ RogueX.Statup("Obed", 90, 3)
                    $ RogueX.AddWord(1,0,"mono","mono") #Daily
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in RogueX.Traits:
                    if ApprovalCheck(RogueX, 700, "O", TabM=0):
                            $ RogueX.FaceChange("sly",1,Eyes="side")
                            ch_r "Как скажешь."
                    elif ApprovalCheck(RogueX, 800, "L", TabM=0):
                            $ RogueX.FaceChange("sly",1)
                            ch_r "Надеюсь, ты не дашь мне никакого повода для этого. . ."
                    else:
                            $ RogueX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in RogueX.DailyActions:
                                    $ RogueX.Statup("Love", 90, -2)
                            ch_r "Да? Что ж, я рада, что получила твое разрешение."
                    if "mono" not in RogueX.DailyActions:
                            $ RogueX.Statup("Obed", 90, 3)
                    if "mono" in RogueX.Traits:
                            $ RogueX.Traits.remove("mono")
                    $ RogueX.AddWord(1,0,"mono") #Daily
            "Неважно.":
                pass
        return

# end Rogue monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


label Rogue_Jumped:
        #called from Rogue_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ RogueX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_r "Да?"
            "На будущее, можешь сначала спрашивать?" if "chill" not in RogueX.Traits:
                    if RogueX.Thirst >= 60 and not ApprovalCheck(RogueX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ RogueX.FaceChange("sly",1)
                            if "chill" not in RogueX.DailyActions:
                                    $ RogueX.Statup("Obed", 90, -2)
                            ch_r "Тогда тебе стоит уделять мне больше внимания. . ."
                            return
                    elif ApprovalCheck(RogueX, 1000, "LO", TabM=0) and RogueX.Love >= RogueX.Obed:
                            #she cares
                            $ RogueX.FaceChange("sly",1)
                            if "chill" not in RogueX.DailyActions:
                                    $ RogueX.Statup("Love", 90, 1)
                            ch_r "Извини, [RogueX.Petname], мне просто бывает иногда одиноко. . ."
                            ch_r "Я исправлюсь. . ."
                    elif ApprovalCheck(RogueX, 500, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side")
                            ch_r "Если ты действительно этого хочешь. . ."
                    else:
                            #she doesn't care
                            $ RogueX.FaceChange("sly",1,Brows="confused")
                            ch_r "Я не могу ничего обещать."
                            return
                    if "chill" not in RogueX.DailyActions:
                            $ RogueX.Statup("Obed", 90, 3)
                    $ RogueX.AddWord(1,0,"chill","chill") #Daily
            "Больше так не делай." if "chill" not in RogueX.Traits:
                    if ApprovalCheck(RogueX, 900, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side")
                            ch_r "Ладно."
                    elif RogueX.Thirst >= 60 and not ApprovalCheck(RogueX, 600, "O", TabM=0):
                            #she's too thirsty
                            $ RogueX.FaceChange("sly",1)
                            if "chill" not in RogueX.DailyActions:
                                    $ RogueX.Statup("Obed", 90, -2)
                            ch_r "Тогда тебе стоит уделять мне больше внимания. . ."
                            return
                    elif ApprovalCheck(RogueX, 450, "O", TabM=0):
                            #she is obedient
                            $ RogueX.FaceChange("sly",1,Eyes="side")
                            ch_r "Если ты действительно этого хочешь. . ."
                    elif ApprovalCheck(RogueX, 500, "LO", TabM=0) and not ApprovalCheck(RogueX, 500, "I", TabM=0):
                            #she cares
                            $ RogueX.FaceChange("sly",1)
                            ch_r "Думаю, тебе стоит следить за своим языком."
                            ch_r "Но ладно, я постараюсь держать себя в руках. . ."
                    else:
                            #she doesn't care
                            $ RogueX.FaceChange("sly",1,Brows="confused")
                            ch_r "Ничего не обещаю."
                            return
                    if "chill" not in RogueX.DailyActions:
                            $ RogueX.Statup("Obed", 90, 3)
                    $ RogueX.AddWord(1,0,"chill","chill") #Daily
            "Делай что хочешь.":
                    if ApprovalCheck(RogueX, 800, "L", TabM=0):
                            $ RogueX.FaceChange("sly",1)
                            ch_r "Хорошо. . ."
                    elif ApprovalCheck(RogueX, 700, "O", TabM=0):
                            $ RogueX.FaceChange("sly",1,Eyes="side")
                            ch_r "Как скажешь."
                    else:
                            $ RogueX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in RogueX.DailyActions:
                                    $ RogueX.Statup("Love", 90, -2)
                            ch_r "Если мне будет скучно."
                    if "chill" not in RogueX.DailyActions:
                            $ RogueX.Statup("Obed", 90, 3)
                    if "chill" in RogueX.Traits:
                            $ RogueX.Traits.remove("chill")
                    $ RogueX.AddWord(1,0,"chill") #Daily
            "Эм, неважно.":
                pass
        return

# end Rogue jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# start Rogue not a virgin
label Rogue_Not_Virgin:
    if not Player.Male:
        "Я заметила, что, когда мы занимались сексом, крови не было."
    else:
        "Я заметил, что, когда мы занимались сексом, крови не было."
    menu:
        "Разве я не была твоей первой?" if not Player.Male:
            $ RogueX.FaceChange("bemused", 1)
            $ RogueX.Statup("Love", 60, 5)
            $ RogueX.Statup("Obed", 20, 15)
            ch_r "Ох! До тебя у меня никого не было, просто. . .  понимаешь,"
            ch_r "Я веду очень активный образ жизни, это принесло свои плоды, я порвала. . . плеву."
        "Разве я не был твоим первым?" if Player.Male:
            $ RogueX.FaceChange("bemused", 1)
            $ RogueX.Statup("Love", 60, 5)
            $ RogueX.Statup("Obed", 20, 15)
            ch_r "Ох! До тебя у меня никого не было, просто. . .  понимаешь,"
            ch_r "Я веду очень активный образ жизни, это принесло свои плоды, я порвала. . . плеву."
        "Ты разве можешь касаться других?":
            $ RogueX.FaceChange("sexy", 1)
            $ RogueX.Brows = "angry"
            $ RogueX.Statup("Obed", 30, 15)
            $ RogueX.Statup("Obed", 60, 5)
            $ RogueX.Statup("Inbt", 30, 15)
            $ RogueX.Statup("Inbt", 60, 5)
            ch_r "Все не так. Я порвал ее много лет назад во время тренировки."
        "Ты шлюха?":
            $ RogueX.FaceChange("angry", 1)
            $ RogueX.Statup("Love", 30, -20, 1)
            $ RogueX.Statup("Love", 60, -40, 1)
            $ RogueX.Statup("Obed", 30, 30)
            $ RogueX.Statup("Obed", 60, 20)
            ch_r "[RogueX.Petname], если хочешь, чтобы я тебе все объяснила, смени тон."
    $ RogueX.Chat[0] = 1
    return

# end rogue not a virgin //////////////////////////////////////////////////////////

# start rogue hungry //////////////////////////////////////////////////////////
label Rogue_Hungry:
    if RogueX.Chat[3]:
        if not Player.Male:
            ch_r "Знаешь, я пришла, чтобы насладиться вкусом твоих. . . соков. Думаю, мне нужна добавка."
        else:
            ch_r "Знаешь, я пришла, чтобы насладиться вкусом твоей. . . спермы. Думаю, мне нужна добавка."
    elif RogueX.Chat[2]:
        ch_r "Знаешь, я пришла насладиться вкусом твоей сыворотки. Это, похоже, мой любимый напиток!"
    else:
        if not Player.Male:
            ch_r "Знаешь, я пришла, чтобы насладиться вкусом твоих. . . соков. Думаю, мне нужна добавка."
        else:
            ch_r "Знаешь, я пришла, чтобы насладиться вкусом твоей. . . спермы. Думаю, мне нужна добавка."
    $ RogueX.Traits.append("hungry")
return


# end rogue hungry //////////////////////////////////////////////////////////

# Rogue Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Rogue_SexChat:
    $ Line = "Ага, о чем хочешь поговорить?" if not Line else Line
    while True:
            menu:
                ch_r "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in RogueX.DailyActions:
                        if not Player.Male:
                            ch_r "Да, я знаю. Ты уже говорила мне об этом."
                        else:
                            ch_r "Да, я знаю. Ты уже говорил мне об этом."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "sex":
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Ага, знаю. . ."
                                        elif RogueX.Favorite == "sex":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 10)
                                            ch_r "Ооох, я тоже люблю хорошую прочистку труб. . ."
                                        elif RogueX.Sex >= 5:
                                            ch_r "Я не пртив хорошого перепихона."
                                        elif not RogueX.Sex:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "С кем {i}конкретно{/i} ты занимаешься сексом?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Хах, [RogueX.Petname], скажешь тоже. . ."
                                        $ RogueX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "anal":
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Я уже слышала. . ."
                                        elif RogueX.Favorite == "anal":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 10)
                                            ch_r "Не могу сказать, что я против. . ."
                                        elif RogueX.Anal >= 10:
                                            ch_r "Неплохой способ провести время вместе. . ."
                                        elif not RogueX.Anal:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "С кем {i}конкретно{/i} ты занимаешься сексом?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Хах, я . . . Я не {i}против{/i} этого. . ."
                                        $ RogueX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "blow":
                                            $ RogueX.Statup("Lust", 80, 3)
                                            ch_r "Я не удивлена. . ."
                                        elif RogueX.Favorite == "blow":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Похоже, благодаря мне ты распробовал это дело. . ."
                                        elif RogueX.Blow >= 10:
                                            ch_r "Мне, вообщем-то, тоже нравится. . ."
                                        elif not RogueX.Blow:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "Кто -именно- сосет тебе?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Я. . . начинаю привыкать к его вкусу. . ."
                                        $ RogueX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "cun":
                                            $ RogueX.Statup("Lust", 80, 3)
                                            ch_r "Я не удивлена. . ."
                                        elif RogueX.Favorite == "cun":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Похоже, благодаря мне ты распробовала это дело. . ."
                                        elif RogueX.CUN >= 10:
                                            ch_r "Мне, вообщем-то, тоже нравится. . ."
                                        elif not RogueX.CUN:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "Кто -именно- лижет тебе?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Я. . . начинаю привыкать к ее вкусу. . ."
                                        $ RogueX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "titjob":
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Я уже слышала. . ."
                                        elif RogueX.Favorite == "titjob":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 7)
                                            ch_r "Мне тоже очень нравится. . ."
                                        elif RogueX.Tit >= 10:
                                            ch_r "Это, безусловно, интересный опыт. . ."
                                        elif not RogueX.Tit:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "Кто -именно- трахает тебя своими сиськами?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Не могу сказать, что виню тебя за это. . ."
                                        $ RogueX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "foot":
                                            $ RogueX.Statup("Lust", 80, 5)
                                            if not Player.Male:
                                                ch_r "Ага, ты уже говорила это ранее. . ."
                                            else:
                                                ch_r "Ага, ты уже говорил это ранее. . ."
                                        elif RogueX.Favorite == "foot":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 7)
                                            ch_r "Мне очень нравятся эти ощущения. . ."
                                        elif RogueX.Foot >= 10:
                                            ch_r "Приятно ласкать тебя ножками. . ."
                                        elif not RogueX.Foot:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "И -кто- же тебе так дрочит?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Мне нравятся эти ощущения. . ."
                                        $ RogueX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "hand":
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Ага, ты уже говорил это ранее. . ."
                                        elif RogueX.Favorite == "hand":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 7)
                                            ch_r "Мне нравится, как он ощущается в моей руке. . ."
                                        elif RogueX.Hand >= 10:
                                            ch_r "Приятно ласкать его так . . ."
                                        elif not RogueX.Hand:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "И -кто- же тебе дрочит?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Мне нравятся эти ощущения. . ."
                                        $ RogueX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "finger":
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Ага, ты уже говорила это ранее. . ."
                                        elif RogueX.Favorite == "finger":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 7)
                                            ch_r "Мне нравится чувствовать тебя под своей рукой. . ."
                                        elif RogueX.Finger >= 10:
                                            ch_r "Приятно ласкать ее так . . ."
                                        elif not RogueX.Finger:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "И -кто- же тебе дрочит?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Мне нравятся эти ощущения. . ."
                                        $ RogueX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = RogueX.FondleB + RogueX.FondleT + RogueX.SuckB + RogueX.Hotdog
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "fondle":
                                            $ RogueX.Statup("Lust", 80, 3)
                                            ch_r "Да, думаю, мы уже это обсудили. . ."
                                        elif RogueX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Мне нравится, как ты прикасаешься ко мне. . ."
                                        elif Cnt >= 10:
                                            ch_r "Приятно осозновать, что есть кто-то, кто может касаться меня. . ."
                                        elif not Cnt:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "-Кого- это ты лапаешь?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Мне нравятся эти ощущения. . ."
                                        $ RogueX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ RogueX.FaceChange("sly")
                                        if RogueX.PlayerFav == "kiss you":
                                            $ RogueX.Statup("Love", 90, 3)
                                            ch_r "Хоть я это и слышала ранее, но мне нравится, когда ты об этом напоминаешь. . ."
                                        elif RogueX.Favorite == "kiss you":
                                            $ RogueX.Statup("Love", 90, 5)
                                            $ RogueX.Statup("Lust", 80, 5)
                                            ch_r "Я тоже не могу оторваться от твоих губ. . ."
                                        elif RogueX.Kissed >= 10:
                                            ch_r "Я тоже люблю тебя целовать . . ."
                                        elif not RogueX.Kissed:
                                            $ RogueX.FaceChange("perplexed")
                                            ch_r "И с -кем же- ты сосешься?"
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            ch_r "Приятно целовать кого-то, не причиняя ему боли. . ."
                                        $ RogueX.PlayerFav = "kiss you"

                        $ RogueX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(RogueX, 800):
                                        $ RogueX.FaceChange("perplexed")
                                        ch_r "Не думаю, что тебя это касается. . ."
                                else:
                                        if RogueX.SEXP >= 50:
                                            $ RogueX.FaceChange("sly")
                                            ch_r "Думаю, тебе пора бы это знать. . ."
                                        else:
                                            $ RogueX.FaceChange("bemused")
                                            $ RogueX.Eyes = "side"
                                            ch_r "Я не уверена. . ."


                                        if not RogueX.Favorite or RogueX.Favorite == "kiss you":
                                            ch_r "Наверное, мне нравится, когда мы целуемся. . ."
                                        elif RogueX.Favorite == "anal":
                                            if RogueX.Anal >= 10:
                                                ch_r "Мне нравится, когда ты трахаешь меня в попку."
                                            else:
                                                ch_r "Мне нравится, когда ты засовываешь его мне в. . . попку."
                                        elif RogueX.Favorite == "lick ass":
                                                ch_r "Мне нравится, когда ты вылизываешь мою. . . попку."
                                        elif RogueX.Favorite == "insert ass":
                                                ch_r "Мне нравится, когда ты играешься пальцем. . . с моей попкой."
                                        elif RogueX.Favorite == "sex":
                                                ch_r "Мне нравится, когда ты жестко трахаешь меня."
                                        elif RogueX.Favorite == "lick pussy":
                                                ch_r "Мне нравится когда ты вылизываешь мою киску."
                                        elif RogueX.Favorite == "fondle pussy":
                                                ch_r "Мне нравится, когда ты ласкаешь мою киску."
                                        elif RogueX.Favorite == "blow":
                                                ch_r "Мне, вроде как, нравится сосать твой член."
                                        elif RogueX.Favorite == "cun":
                                                ch_r "Мне, вроде как, нравится вылизывать твою киску."
                                        elif RogueX.Favorite == "tit":
                                                ch_r "Мне нравится надрачивать твой член моими сиськами."
                                        elif RogueX.Favorite == "hand":
                                                ch_r "Мне нравится чувствовать твой член в своей руке."
                                        elif RogueX.Favorite == "finger":
                                                ch_r "Мне нравится ощущать твою щелочку под своими пальцами."
                                        elif RogueX.Favorite == "foot":
                                                ch_r "Я, вроде как, люблю использовать свои ножки."
                                        elif RogueX.Favorite == "hotdog":
                                                ch_r "Мне нравится, когда ты трешься о меня."
                                        elif RogueX.Favorite == "suck breasts":
                                                ch_r "Мне нравится, когда ты сосешь мои сиськи."
                                        elif RogueX.Favorite == "fondle breasts":
                                                ch_r "Мне нравится, когда ты ласкаешь мои сиськи."
                                        elif RogueX.Favorite == "fondle thighs":
                                                ch_r "Мне нравится, когда ты массируешь мои ножки."
                                        else:
                                                ch_r "Я даже не знаю. . ."

                                # End Rogue's favorite things.

                "Не болтай так много во время секса." if "vocal" in RogueX.Traits:
                        if "setvocal" in RogueX.DailyActions:
                            $ RogueX.FaceChange("perplexed")
                            ch_r "Мы уже говорили об этом."
                        else:
                            if ApprovalCheck(RogueX, 1000) and RogueX.Obed <= RogueX.Love:
                                $ RogueX.FaceChange("bemused")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "Хех, ладно, если ты этого хочешь. . ."
                                $ RogueX.Traits.remove("vocal")
                            elif ApprovalCheck(RogueX, 700, "O"):
                                $ RogueX.FaceChange("sadside")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "Если ты этого хочешь, [RogueX.Petname]."
                                $ RogueX.Traits.remove("vocal")
                            elif ApprovalCheck(RogueX, 600):
                                $ RogueX.FaceChange("sly")
                                $ RogueX.Statup("Love", 90, -3)
                                $ RogueX.Statup("Obed", 50, -1)
                                $ RogueX.Statup("Inbt", 90, 5)
                                ch_r "Я буду говорить то, что хочу, тебе понравится, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry")
                                $ RogueX.Statup("Love", 90, -5)
                                $ RogueX.Statup("Obed", 60, -3)
                                $ RogueX.Statup("Inbt", 90, 10)
                                ch_r "Да ну тебя, я буду говорить сколько захочу."

                            $ RogueX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in RogueX.Traits:
                        if "setvocal" in RogueX.DailyActions:
                            $ RogueX.FaceChange("perplexed")
                            ch_r "Мы уже говорили об этом."
                        else:
                            if ApprovalCheck(RogueX, 1000) and RogueX.Obed <= RogueX.Love:
                                $ RogueX.FaceChange("sly")
                                $ RogueX.Statup("Obed", 90, 2)
                                ch_r "Хех, ладно, если ты этого хочешь. . ."
                                $ RogueX.Traits.append("vocal")
                            elif ApprovalCheck(RogueX, 700, "O"):
                                $ RogueX.FaceChange("sadside")
                                $ RogueX.Statup("Obed", 90, 2)
                                ch_r "Если ты этого хочешь, [RogueX.Petname]."
                                $ RogueX.Traits.append("vocal")
                            elif ApprovalCheck(RogueX, 600):
                                $ RogueX.FaceChange("sly")
                                $ RogueX.Statup("Obed", 90, 3)
                                ch_r "Я могу попробовать, [RogueX.Petname]."
                                $ RogueX.Traits.append("vocal")
                            else:
                                $ RogueX.FaceChange("angry")
                                $ RogueX.Statup("Inbt", 90, 5)
                                ch_r "Я буду говорить, что хочу, когда захочу."

                            $ RogueX.DailyActions.append("setvocal")
                        # End Rogue Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in RogueX.Traits:
                        if "initiative" in RogueX.DailyActions:
                                $ RogueX.FaceChange("perplexed")
                                ch_r "Мы уже говорили об этом."
                        else:
                            if ApprovalCheck(RogueX, 1000) and RogueX.Obed <= RogueX.Love:
                                $ RogueX.FaceChange("bemused")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "Хех, ладно, тогда веди ты. . ."
                                $ RogueX.Traits.append("passive")
                            elif ApprovalCheck(RogueX, 700, "O"):
                                $ RogueX.FaceChange("sadside")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "Ладно, я буду держать себя в руках, [RogueX.Petname]."
                                $ RogueX.Traits.append("passive")
                            elif ApprovalCheck(RogueX, 600):
                                $ RogueX.FaceChange("sly")
                                $ RogueX.Statup("Love", 90, -3)
                                $ RogueX.Statup("Obed", 50, -1)
                                $ RogueX.Statup("Inbt", 90, 5)
                                ch_r "Тебе это вряд ли понравится, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry")
                                $ RogueX.Statup("Love", 90, -5)
                                $ RogueX.Statup("Obed", 60, -3)
                                $ RogueX.Statup("Inbt", 90, 10)
                                ch_r "Я буду делать то, что хочу."

                            $ RogueX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in RogueX.Traits:
                        if "initiative" in RogueX.DailyActions:
                                $ RogueX.FaceChange("perplexed")
                                ch_r "Мы уже говорили об этом."
                        else:
                            if ApprovalCheck(RogueX, 1000) and RogueX.Obed <= RogueX.Love:
                                $ RogueX.FaceChange("bemused")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "Хех, думаю, я справлюсь. . ."
                                $ RogueX.Traits.remove("passive")
                            elif ApprovalCheck(RogueX, 700, "O"):
                                $ RogueX.FaceChange("sadside")
                                $ RogueX.Statup("Obed", 90, 1)
                                ch_r "Это я могу, [RogueX.Petname]."
                                $ RogueX.Traits.remove("passive")
                            elif ApprovalCheck(RogueX, 600):
                                $ RogueX.FaceChange("sly")
                                $ RogueX.Statup("Obed", 90, 3)
                                ch_r "Я попробую, [RogueX.Petname]."
                                $ RogueX.Traits.remove("passive")
                            else:
                                $ RogueX.FaceChange("angry")
                                $ RogueX.Statup("Inbt", 90, 5)
                                ch_r "Если захочу, то буду, но это не из-за твоей просьбы."

                            $ RogueX.DailyActions.append("initiative")

                "О том, как ты накидываешься" if "jumped" in RogueX.History:
                        call Rogue_Jumped
                "О твоей мастурбации":
                        call NoFap(RogueX)

                "Всегда носи вибратор" if "dailyvibe" not in RogueX.Traits:
                        call Daily_Vibrator(RogueX)
                "Перестань всегда носить вибратор" if "dailyvibe" in RogueX.Traits:
                        ch_r "Ладно. . ."
                        $ RogueX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи анальную пробку" if "dailyplug" not in RogueX.Traits:
                        call Daily_Plug(RogueX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in RogueX.Traits:
                        ch_r "Ладно. . ."
                        $ RogueX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Неважно" if Line == "Ага, о чем хочешь поговорить?":
                        return
                "На этом все." if Line != "Ага, о чем хочешь поговорить?":
                        return
            if Line == "Ага, о чем хочешь поговорить?":
                $ Line = "Что-то еще?"
    return
# End Rogue Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# Rogue Chitchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Rogue_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:
        if RogueX not in Digits:
            if ApprovalCheck(RogueX, 500, "L") or ApprovalCheck(RogueX, 250, "I"):
                    ch_r "Знаешь, я заметила, что у тебя нет моего номера телефона - вот, держи."
                    $ Digits.append(RogueX)
                    return
            elif ApprovalCheck(RogueX, 250, "O"):
                    ch_r "Знаешь, тебе стоит знать мой номер - вот, держи."
                    $ Digits.append(RogueX)
                    return
        if "hungry" not in RogueX.Traits and (RogueX.Swallow + RogueX.Chat[2]) >= 10 and RogueX.Loc == bg_current:  #She's swallowed a lot
                    call Rogue_Hungry
                    return
        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(RogueX, 800, "I")):
                    if RogueX.Loc == bg_current and RogueX.Thirst >= 30 and "refused" not in RogueX.DailyActions and "quicksex" not in RogueX.DailyActions:
                            $ RogueX.FaceChange("sly",1)
                            ch_r "Слушай, не хочешь немного пошалить?"
                            call Quick_Sex(RogueX)
                            return

        #adds options based on accomplishments
        if ApprovalCheck(RogueX, 1200) and bg_current == RogueX.Loc and bg_current != "bg restaurant":
            $ Options.append("dance")
        if ApprovalCheck(RogueX, 800, "L") and "nametag chat" not in RogueX.DailyActions:
            $ Options.append("close")
        if RogueX.Blow >= 2 and Player.Male:
            $ Options.append("blow")
        if "steal" in RogueX.Traits:
            $ Options.append("steal")
        if PunishmentX and "caught chat" not in RogueX.DailyActions:
            $ Options.append("caught")
        if RogueX.Event[0] and "key chat" not in RogueX.DailyActions:
            $ Options.append("key")
        if "luv" not in RogueX.History and "lover" in RogueX.Petnames and ApprovalCheck(RogueX, 900, "L"): # luvy dovey
            $ Options.append("luv")

        if "mandrill" in Player.Traits and "cologne chat" not in RogueX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in RogueX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in RogueX.DailyActions:
            $ Options.append("corruption")

        if not RogueX.Chat[0] and RogueX.Sex:
            $ Options.append("virgin")

        if "seenpeen" in RogueX.History and Player.Male:
            $ Options.append("seenpeen")
        if "topless" in RogueX.History:
            $ Options.append("topless")
        if "bottomless" in RogueX.History:
            $ Options.append("bottomless")

        if "lover" in RogueX.Petnames and "Anna" not in RogueX.Names:
            #if you've done the love scene, but never got Rogue's other name, second chance
            $ Options.append("annamarie")

        if (bg_current == "bg rogue" or bg_current == "bg player") and "nametag chat" not in RogueX.DailyActions:
            if "lover" not in RogueX.Petnames and ApprovalCheck(RogueX, 900, "L"): # RogueX.Event[6]
                $ Options.append("lover?")
            elif "sir" not in RogueX.Petnames and ApprovalCheck(RogueX, 500, "O"): # RogueX.Event[7]
                $ Options.append("sir?")
            elif "daddy" not in RogueX.Petnames and ApprovalCheck(RogueX, 750, "L") and ApprovalCheck(RogueX, 500, "O") and ApprovalCheck(RogueX, 500, "I"): # RogueX.Event[5]
                $ Options.append("daddy?")
            elif "master" not in RogueX.Petnames and ApprovalCheck(RogueX, 900, "O"): # RogueX.Event[8]
                $ Options.append("master?")
            elif "sex friend" not in RogueX.Petnames and ApprovalCheck(RogueX, 500, "I"): # RogueX.Event[9]
                $ Options.append("sexfriend?")
            elif "fuck buddy" not in RogueX.Petnames and ApprovalCheck(RogueX, 900, "I"): # RogueX.Event[10]
                $ Options.append("fuckbuddy?")

        if not ApprovalCheck(RogueX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "virgin": # "virgin line" not yet triggered:
        call Rogue_Not_Virgin

    elif Options[0] == "mandrill":
        $ RogueX.DailyActions.append("cologne chat")
        $ RogueX.FaceChange("confused")
        ch_r "(Нюх-нюх). . . пахнет обезьяньей задницей. . ."
        $ RogueX.FaceChange("sly", 1)
        if not Player.Male:
            ch_r ". . . но сегодня ты такая красивая, [RogueX.Petname]."
        else:
            ch_r ". . . но сегодня ты такой красивый, [RogueX.Petname]."
    elif Options[0] == "purple":
        $ RogueX.DailyActions.append("cologne chat")
        $ RogueX.FaceChange("sly",1)
        ch_r "(Нюх-нюх). . . Хммм, ты сегодня хорошо пахнешь. . ."
        ch_r ". . . я могу тебя как-нибудь осчастливить?"
    elif Options[0] == "corruption":
        $ RogueX.DailyActions.append("cologne chat")
        $ RogueX.FaceChange("confused")
        ch_r "(Нюх-нюх). . . у тебя довольно сильный аромат. . ."
        $ RogueX.FaceChange("sly")
        ch_r ". . . У меня почему-то появились очень неприличные мысли, [RogueX.Petname]. . ."

    elif Options[0] == "blow":
        $ Line = renpy.random.choice(["Знаешь, ты вкуснее, чем я думала.",
                "Из-за тебя у меня немного болит челюсть.",
                "Дай мне знать, если захочешь легкого минета.",
                "Хмммм. . . [Стучит языком по внутренней части щеки.]"])
        ch_r "[Line]"

    elif Options[0] == "close": # RogueX.Love >= 800
        ch_r "Знаешь, мне всегда было сложно находить общий язык с людьми, поскольку я не могла. . ."
        ch_r "-сблизиться- с ними, понимаешь?"
        ch_r "Для меня невероятное счастье, что я смогла настолько сблизиться с тобой."
        $ RogueX.DailyActions.append("close chat")
    elif Options[0] == "caught": # Xavier's caught you
        ch_r "Было страшно, когда нас завели в кабинет профессора."
        if not ApprovalCheck(RogueX, 500, "I"):
            ch_r "Наверное, нам стоит быть более осторожными, когда мы. . . ну, ты понимаешь."
        else:
            ch_r "Наверное, нам стоит быть более осторожными, когда мы трахаемся."
        $ RogueX.DailyActions.append("caught chat")
    elif Options[0] == "key": # you have her key
        if RogueX.SEXP <= 15:
            ch_r "Я рада, что теперь у тебя есть мой ключ, только не используй его по пустякам. . ."
        else:
            ch_r "Я рада, что теперь у тебя есть мой ключ, можешь как-нибудь . . .  \"удивить\" меня. . ."
        $ RogueX.DailyActions.append("key chat")
    elif Options[0] == "touch": # "touch" in RogueX.Traits:
        ch_r "Благодаря тому, что я с тобой так много общаюсь, я смогла научиться контролировать свои способности."
        ch_r "Если бы не твоя помощь, то я бы до сих пор не могла ни к кому притронуться!"
    elif Options[0] == "steal": # "steal" in RogueX.Traits:
        ch_r "Благодаря тому, что я с тобой так много общаюсь, я смогла научиться навсегда копировать способности других мутантов."
    elif Options[0] == "dance": # dancing comes up
        ch_r "Не могу дождаться следующей большой вечеринки."
        ch_r "Я обожаю танцевать, и у меня как раз есть партнер, о которого я могу потереться-"
        $ RogueX.Pose = "doggy"
        call Rogue_Sex_Launch("massage")
        if RogueX.PantsNum() == 5:
            $ RogueX.Upskirt = 1
            if RogueX.Panties and RogueX.SeenPanties and ApprovalCheck(RogueX, 800, TabM = 3):
                pass
            elif RogueX.Panties and ApprovalCheck(RogueX, 800, TabM = 3):
                $ RogueX.SeenPanties = 1
            elif RogueX.Panties:
                $ RogueX.Upskirt = 0
            elif RogueX.SeenPussy and ApprovalCheck(RogueX, 1000, TabM = 4):
                pass
            elif ApprovalCheck(RogueX, 1400, TabM = 3):
                call Girl_First_Bottomless(RogueX,1)
            else:
                $ RogueX.Upskirt = 0
            pause 0.5
            $ RogueX.Upskirt = 0
        ch_r "Ты же понимаешь, о чем я, [RogueX.Petname]?"
        $ RogueX.Upskirt = 0
        call Rogue_Doggy_Reset
        call Set_The_Scene


    elif Options[0] == "seenpeen": # first seen peen skipped
            $ RogueX.FaceChange("sly",1)
            if not Player.Male:
                ch_r "Я очень удивилась, когда впервые увидела твой член."
                ch_r "Я и не знала, что он такой огромный."
            else:
                ch_r "Я очень удивилась, когда впервые увидела твою киску."
                ch_r "Я и не знала, что она такая милая."
            $ RogueX.FaceChange("bemused",1)
            $ RogueX.Statup("Love", 90, 5)
            $ RogueX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            if not Player.Male:
                ch_r "Эм. . . когда ты впервые увидела мои обнаженные сиськи, ты толком ничего не сказала. . ."
            else:
                ch_r "Эм. . . когда ты впервые увидел мои обнаженные сиськи, ты толком ничего не сказал. . ."
            ch_r "Они тебе понравились?"
            call Girl_First_TMenu
            $ RogueX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            if not Player.Male:
                ch_r "Когда ты впервые увидел меня без трусиков, ты ничего толком не сказала. . ."
            else:
                ch_r "Когда ты впервые увидел меня без трусиков, ты ничего толком не сказал. . ."
            call Girl_First_BMenu
            $ RogueX.History.remove("bottomless")

    elif Options[0] == "luv": # love maxed out
        $ RogueX.FaceChange("bemused", 1)
        ch_r ". . ."
        ch_r "Понимаешь, в моей жизни бывали моменты, когда я думала, что навсегда останусь одна и так никогда не смогу ни к кому прикоснуться. . ."
        $ RogueX.FaceChange("smile")
        ch_r "Я очень рада, что повстречалась с тобой."
        ch_r "Я люблю тебя, [RogueX.Petname]."
        menu:
            extend ""
            "Я тоже тебя люблю.":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Statup("Obed", 80, 4)
                $ RogueX.Statup("Inbt", 80, 4)
            "Я тоже тебя люблю, [RogueX.Pet].":
                $ RogueX.NameCheck()
                if _return:
                    $ RogueX.FaceChange("angry")
                    $ RogueX.Statup("Love", 90, -1)
                    $ RogueX.Statup("Obed", 80, 10)
                    $ RogueX.Statup("Inbt", 80, 4)
                else:
                    $ RogueX.Statup("Love", 200, 10)
                    $ RogueX.Statup("Obed", 80, 4)
                    $ RogueX.Statup("Inbt", 80, 4)
            "Ага, я тоже.":
                $ RogueX.FaceChange("perplexed")
                $ RogueX.Statup("Love", 90, -1)
                $ RogueX.Statup("Obed", 80, 10)
                $ RogueX.Statup("Inbt", 80, 4)
            "Как скажешь.":
                $ RogueX.FaceChange("angry")
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 80, 4)
                $ RogueX.Statup("Inbt", 80, 10)
        $ RogueX.AddWord(1,0,0,0,"luv") #adds "word" tag to Recent

    elif Options[0] == "boyfriend?":
        call Rogue_BF
        $ RogueX.DailyActions.append("nametag chat")
    elif Options[0] == "lover?":
        call Rogue_Love
        $ RogueX.DailyActions.append("nametag chat")
    elif Options[0] == "sir?":
        call Rogue_Sub
        $ RogueX.DailyActions.append("nametag chat")
    elif Options[0] == "master?":
        call Rogue_Master
        $ RogueX.DailyActions.append("nametag chat")
    elif Options[0] == "sexfriend?":
        call Rogue_Sexfriend
        $ RogueX.DailyActions.append("nametag chat")
    elif Options[0] == "fuckbuddy?":
        call Rogue_Fuckbuddy
        $ RogueX.DailyActions.append("nametag chat")
    elif Options[0] == "daddy?":
        call Rogue_Daddy
        $ RogueX.DailyActions.append("nametag chat")
    elif Options[0] == "annamarie":
        call Rogue_AnnaMarie #adds new names to list
    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Отойди от меня.",
                "Я не желаю видеть твое лицо.",
                "Отстань от меня.",
                "Оставь меня в покое."])
        ch_r "[Line]"

    else: #all else fell through. . .
        $ D20 = renpy.random.randint(1, 16)
        if D20 == 1:
                $ RogueX.FaceChange("confused")
                ch_r "Я так нервничаю из-за теста по генетике с профессором МакКоем. Я вообще не разбираюсь в этой теме."
        elif D20 == 2:
                $ RogueX.FaceChange("sad")
                ch_r "Сегодня чувствую себя немного подавленной, [RogueX.Petname]. Семейные проблемы. Сложно объяснить."
        elif D20 == 3:
                $ RogueX.FaceChange("sly")
                if not Player.Male:
                    ch_r "Может быть, ты слышала о моих старых друзьях? Не все они настолько плохи, какими кажутся. В основном."
                else:
                    ch_r "Может быть, ты слышал о моих старых друзьях? Не все они настолько плохи, какими кажутся. В основном."
        elif D20 == 4:
                $ RogueX.FaceChange("smile")
                ch_r "Сегодня я побила все свои личные рекорды в комнате Опасности! Жаль, что тебя не было рядом!"
        elif D20 == 5:
                $ RogueX.FaceChange("smile")
                if not Player.Male:
                    ch_r "Ты когда-нибудь задумывалась, каково это - уметь летать? Это, пожалуй, самая крутая способность, согласна?"
                else:
                    ch_r "Ты когда-нибудь задумывался, каково это - уметь летать? Это, пожалуй, самая крутая способность, согласен?"
        elif D20 == 6:
                $ RogueX.FaceChange("smile")
                if not Player.Male:
                    ch_r "Бывала на озере Брейкстоун, что за особняком? Там так хорошо и спокойно. Чем-то это место напоминает мне мой дом в Миссисипи, летом. Только немного прохладнее."
                else:
                    ch_r "Бывал на озере Брейкстоун, что за особняком? Там так хорошо и спокойно. Чем-то это место напоминает мне мой дом в Миссисипи, летом. Только немного прохладнее."
        elif D20 == 7:
                $ RogueX.FaceChange("smile")
                $ RogueX.Eyes = "surprised"
                ch_r "Я только что видела очень клевую вещь! Стадо оленей, в лесу, прямо у забора!"
                $ RogueX.Eyes = "side"
                ch_r "Они выглядели такими. . . -мягкими-. Интересно, какие они на самом деле на ощупь?"
        elif D20 == 8:
                $ RogueX.FaceChange("smile")
                if not Player.Male:
                    ch_r "Видела Мстителей в сегодняшних новостях? Посмотришь на этих ребят, и все кажется таким простым!"
                else:
                    ch_r "Видел Мстителей в сегодняшних новостях? Посмотришь на этих ребят, и все кажется таким простым!"
        elif D20 == 9:
                $ RogueX.FaceChange("smile")
                ch_r "Завтра мы собираемся на пробежку по одному из подземных уровней. Погнали с нами!"
        elif D20 == 10:
                $ RogueX.FaceChange("down")
                ch_r "Мне задали -так- много домашки на этой неделе! А я -так- не хочу ничего делать!"
        elif D20 == 11:
                $ RogueX.FaceChange("startled")
                ch_r "Знаешь, я очень сильно ненавижу свои силы. Но ты можешь себе представить, какого профессору Ксавье?"
                ch_r "Я не знаю, смогла бы я справиться с такой ответственностью."
                ch_r "Может быть, ему, по-своему, даже хуже, чем мне."
        elif D20 == 12:
                $ RogueX.FaceChange("sad")
                ch_r "В особнеке отлично живется. . . но порой мне становится не по себе, что на нас в любой момент может напасть какой-нибудь супер-маньяк."
        elif D20 == 13:
                $ RogueX.FaceChange("smile")
                ch_r "Обожаю хорошенько выспаться. Чувствую себя потом изумительно!"
        elif D20 == 14:
                $ RogueX.FaceChange("bemused")
                ch_r "Я слышала, что они собираются в этом году устроить бал. Возможно, это будет. . .  интересно."
        elif D20 == 15:
                $ RogueX.FaceChange("smile")
                if not Player.Male:
                    ch_r "Ты выходила сегодня на улицу? Сегодня великолепная погода!"
                else:
                    ch_r "Ты выходил сегодня на улицу? Сегодня великолепная погода!"
        elif D20 == 16:
                $ RogueX.FaceChange("smile")
                ch_r "Знаешь, однажды я наблюдала за Росомахой,"
                $ RogueX.FaceChange("sadside")
                $ RogueX.Brows = "confused"
                ch_r "Я до сих пор ловлю себя на том, что время от времени называю людей \"дружками\"."
        else:
                $ RogueX.FaceChange("smile")
                ch_r "Мне нравится проводить время с тобой!"
    $ Line = 0
    return

# start Rogue_Names//////////////////////////////////////////////////////////
label Rogue_Names:
        #Sets pet names from Rogue
        if ApprovalCheck(RogueX, 600, "L", TabM=0) or ApprovalCheck(RogueX, 300, "O", TabM=0):
            pass
        else:
            $ RogueX.Mouth = "smile"
            ch_r "Я буду звать тебя как захочу, [RogueX.Petname], тебе придется привыкнуть."
            return
        if not Player.Male:
            ch_r "А? Как бы ты хотела, чтобы я тебя звала?"
        else:
            ch_r "А? Как бы ты хотел, чтобы я тебя звала?"
        menu:
            extend ""
            "Сладенькая в самый раз." if not Player.Male:
                    $ RogueX.Petname = "сладенькая"
                    $ RogueX.Petname_rod = "сладенькой"
                    $ RogueX.Petname_dat = "сладенькой"
                    $ RogueX.Petname_vin = "сладенькую"
                    $ RogueX.Petname_tvo = "сладенькой"
                    $ RogueX.Petname_pre = "сладенькой"
                    ch_r "Поняла, сладенькая."
            "Сладенький в самый раз." if Player.Male:
                    $ RogueX.Petname = "сладенький"
                    $ RogueX.Petname_rod = "сладенького"
                    $ RogueX.Petname_dat = "сладенькому"
                    $ RogueX.Petname_vin = "сладенького"
                    $ RogueX.Petname_tvo = "сладеньким"
                    $ RogueX.Petname_pre = "сладеньком"
                    ch_r "Поняла, сладенький."
            "Зови меня по имени.":
                    $ RogueX.Petname = Player.Name
                    $ RogueX.Petname_rod = Player.Name_rod
                    $ RogueX.Petname_dat = Player.Name_dat
                    $ RogueX.Petname_vin = Player.Name_vin
                    $ RogueX.Petname_tvo = Player.Name_tvo
                    $ RogueX.Petname_pre = Player.Name_pre
                    ch_r "Если ты этого хочешь, [RogueX.Petname]."
            "Зови меня своей \"девушкой\"." if "boyfriend" in RogueX.Petnames and not Player.Male:
                    $ RogueX.Petname = "моя девушка"
                    $ RogueX.Petname_rod = "моей девушки"
                    $ RogueX.Petname_dat = "моей девушке"
                    $ RogueX.Petname_vin = "мою девушку"
                    $ RogueX.Petname_tvo = "моей девушкой"
                    $ RogueX.Petname_pre = "моей девушке"
                    ch_r "Конечно, [RogueX.Petname]."
            "Зови меня своим \"парнем\"." if "boyfriend" in RogueX.Petnames and Player.Male:
                    $ RogueX.Petname = "мой парень"
                    $ RogueX.Petname_rod = "моего парня"
                    $ RogueX.Petname_dat = "моему парню"
                    $ RogueX.Petname_vin = "моего парня"
                    $ RogueX.Petname_tvo = "моим парнем"
                    $ RogueX.Petname_pre = "моем парне"
                    ch_r "Конечно, [RogueX.Petname]."
            "Зови меня \"любимая\"." if "lover" in RogueX.Petnames and not Player.Male:
                    $ RogueX.Petname = "любимая"
                    $ RogueX.Petname_rod = "любимой"
                    $ RogueX.Petname_dat = "любимой"
                    $ RogueX.Petname_vin = "любимую"
                    $ RogueX.Petname_tvo = "любимой"
                    $ RogueX.Petname_pre = "любимой"
                    ch_r "Ооох, мне нравится, [RogueX.Petname]."
            "Зови меня \"любимый\"." if "lover" in RogueX.Petnames and Player.Male:
                    $ RogueX.Petname = "любимый"
                    $ RogueX.Petname_rod = "любимого"
                    $ RogueX.Petname_dat = "любимому"
                    $ RogueX.Petname_vin = "любимого"
                    $ RogueX.Petname_tvo = "любимым"
                    $ RogueX.Petname_pre = "любимом"
                    ch_r "Ооох, мне нравится, [RogueX.Petname]."
            "Зови меня \"госпожа\"." if "sir" in RogueX.Petnames and not Player.Male:
                    $ RogueX.Petname = "госпожа"
                    $ RogueX.Petname_rod = "госпожи"
                    $ RogueX.Petname_dat = "госпоже"
                    $ RogueX.Petname_vin = "госпожу"
                    $ RogueX.Petname_tvo = "госпожой"
                    $ RogueX.Petname_pre = "госпоже"
                    ch_r "Да, [RogueX.Petname]."
            "Зови меня \"господин\"." if "sir" in RogueX.Petnames and Player.Male:
                    $ RogueX.Petname = "господин"
                    $ RogueX.Petname_rod = "господина"
                    $ RogueX.Petname_dat = "господину"
                    $ RogueX.Petname_vin = "господина"
                    $ RogueX.Petname_tvo = "господином"
                    $ RogueX.Petname_pre = "господине"
                    ch_r "Да, [RogueX.Petname]."
            "Зови меня \"хозяйка\"." if "master" in RogueX.Petnames and not Player.Male:
                    $ RogueX.Petname = "хозяйка"
                    $ RogueX.Petname_rod = "хозяйки"
                    $ RogueX.Petname_dat = "хозяйке"
                    $ RogueX.Petname_vin = "хозяйку"
                    $ RogueX.Petname_tvo = "хозяйкой"
                    $ RogueX.Petname_pre = "хозяйке"
                    ch_r "Как пожелаешь, [RogueX.Petname]."
            "Зови меня \"хозяин\"." if "master" in RogueX.Petnames and Player.Male:
                    $ RogueX.Petname = "хозяин"
                    $ RogueX.Petname_rod = "хозяина"
                    $ RogueX.Petname_dat = "хозяину"
                    $ RogueX.Petname_vin = "хозяина"
                    $ RogueX.Petname_tvo = "хозяином"
                    $ RogueX.Petname_pre = "хозяине"
                    ch_r "Как пожелаешь, [RogueX.Petname]."
            "Зови меня \"любовница\"." if "sex friend" in RogueX.Petnames and not Player.Male:
                    $ RogueX.Petname = "любовница"
                    $ RogueX.Petname_rod = "любовницы"
                    $ RogueX.Petname_dat = "любовнице"
                    $ RogueX.Petname_vin = "любовницу"
                    $ RogueX.Petname_tvo = "любовницей"
                    $ RogueX.Petname_pre = "любовнице"
                    ch_r "Хех, очень дерзко, [RogueX.Petname]."
            "Зови меня \"любовник\"." if "sex friend" in RogueX.Petnames and Player.Male:
                    $ RogueX.Petname = "любовник"
                    $ RogueX.Petname_rod = "любовника"
                    $ RogueX.Petname_dat = "любовнику"
                    $ RogueX.Petname_vin = "любовника"
                    $ RogueX.Petname_tvo = "любовником"
                    $ RogueX.Petname_pre = "любовнике"
                    ch_r "Хех, очень дерзко, [RogueX.Petname]."
            "Зови меня \"секс-партнерша\"." if "fuck buddy" in RogueX.Petnames and not Player.Male:
                    $ RogueX.Petname = "секс-партнерша"
                    $ RogueX.Petname_rod = "секс-партнерши"
                    $ RogueX.Petname_dat = "секс-партнерше"
                    $ RogueX.Petname_vin = "секс-партнершу"
                    $ RogueX.Petname_tvo = "секс-партнершей"
                    $ RogueX.Petname_pre = "секс-партнерше"
                    ch_r "Я в деле, если ты готова, [RogueX.Petname]."
            "Зови меня \"секс-партнер\"." if "fuck buddy" in RogueX.Petnames and Player.Male:
                    $ RogueX.Petname = "секс-партнер"
                    $ RogueX.Petname_rod = "секс-партнера"
                    $ RogueX.Petname_dat = "секс-партнеру"
                    $ RogueX.Petname_vin = "секс-партнера"
                    $ RogueX.Petname_tvo = "секс-партнером"
                    $ RogueX.Petname_pre = "секс-партнере"
                    ch_r "Я в деле, если ты готов, [RogueX.Petname]."
            "Зови меня \"мамочка\"." if "daddy" in RogueX.Petnames and not Player.Male:
                    $ RogueX.Petname = "мамочка"
                    $ RogueX.Petname_rod = "мамочки"
                    $ RogueX.Petname_dat = "мамочке"
                    $ RogueX.Petname_vin = "мамочку"
                    $ RogueX.Petname_tvo = "мамочкой"
                    $ RogueX.Petname_pre = "мамочке"
                    ch_r "Ох! Буду, не сомневайся, [RogueX.Petname]."
            "Зови меня \"папочка\"." if "daddy" in RogueX.Petnames and Player.Male:
                    $ RogueX.Petname = "папочка"
                    $ RogueX.Petname_rod = "папочки"
                    $ RogueX.Petname_dat = "папочке"
                    $ RogueX.Petname_vin = "папочку"
                    $ RogueX.Petname_tvo = "папочкой"
                    $ RogueX.Petname_pre = "папочке"
                    ch_r "Ох! Буду, не сомневайся, [RogueX.Petname]."
            "Неважно.":
                return
        return
# end Rogue_Names//////////////////////////////////////////////////////////

label Rogue_Pet:
        #sets what you call Rogue
        if ApprovalCheck(RogueX, 600, "L", TabM=0):
            ch_r "Да? В чём дело?"
        elif ApprovalCheck(RogueX, 300, "O", TabM=0):
            if not Player.Male:
                ch_r "Как бы ты хотела меня звать?"
            else:
                ch_r "Как бы ты хотел меня звать?"
        else:
            ch_r "Ох, это должно быть здорово. . ."
        while 1:
            menu:
                extend ""
                "Обходительно":
                    menu:
                        extend ""
                        "Думаю, буду просто звать тебя Роуг.":
                            $ RogueX.Pet = "Роуг"
                            $ RogueX.Pet_rod = "Роуг"
                            $ RogueX.Pet_dat = "Роуг"
                            $ RogueX.Pet_vin = "Роуг"
                            $ RogueX.Pet_tvo = "Роуг"
                            $ RogueX.Pet_pre = "Роуг"
                            ch_r "Не вижу причин для отказа, [RogueX.Petname]."

                        "Думаю, буду звать тебя \"моя девушка\".":
                            if "boyfriend" in RogueX.Petnames:
                                $ RogueX.Pet = "моя девушка"
                                $ RogueX.Pet_rod = "моей девушки"
                                $ RogueX.Pet_dat = "моей девушке"
                                $ RogueX.Pet_vin = "мою девушку"
                                $ RogueX.Pet_tvo = "моей девушкой"
                                $ RogueX.Pet_pre = "моей девушке"
                                $ RogueX.FaceChange("sexy", 1)
                                ch_r "Да, мы же все-таки встречаемся, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry")
                                ch_r "Я не твоя девушка, [RogueX.Petname]."

                        "Думаю, буду звать тебя \"детка\".":
                            if "boyfriend" in RogueX.Petnames or ApprovalCheck(RogueX, 500, "L"):
                                $ RogueX.Pet = "детка"
                                $ RogueX.Pet_rod = "детки"
                                $ RogueX.Pet_dat = "детке"
                                $ RogueX.Pet_vin = "детку"
                                $ RogueX.Pet_tvo = "деткой"
                                $ RogueX.Pet_pre = "детке"
                                $ RogueX.FaceChange("sexy", 1)
                                ch_r "Оу, я твоя детка, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry")
                                ch_r "Я тебе не детка,  [RogueX.Petname]."

                        "Думаю, буду звать тебя \"крошка\".":
                            if "boyfriend" in RogueX.Petnames or ApprovalCheck(RogueX, 500, "L"):
                                $ RogueX.Pet = "крошка"
                                $ RogueX.Pet_rod = "крошки"
                                $ RogueX.Pet_dat = "крошке"
                                $ RogueX.Pet_vin = "крошку"
                                $ RogueX.Pet_tvo = "крошкой"
                                $ RogueX.Pet_pre = "крошке"
                                $ RogueX.FaceChange("sexy", 1)
                                ch_r "Оу, Я твоя крошка, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry")
                                ch_r "Я тебе не крошка,  [RogueX.Petname]."

                        "Думаю, буду звать тебя \"малышка\".":
                            if "boyfriend" in RogueX.Petnames or ApprovalCheck(RogueX, 500, "L"):
                                $ RogueX.Pet = "малышка"
                                $ RogueX.Pet_rod = "малышки"
                                $ RogueX.Pet_dat = "малышке"
                                $ RogueX.Pet_vin = "малышку"
                                $ RogueX.Pet_tvo = "малышкой"
                                $ RogueX.Pet_pre = "малышке"
                                $ RogueX.FaceChange("sexy", 1)
                                ch_r "Оу, как мило, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry")
                                ch_r "Я тебе не малышка, [RogueX.Petname]."

                        "Думаю, буду звать тебя \"дорогуша\".":
                            if "lover" in RogueX.Petnames or ApprovalCheck(RogueX, 600, "L"):
                                $ RogueX.Pet = "дорогуша"
                                $ RogueX.Pet_rod = "дорогуши"
                                $ RogueX.Pet_dat = "дорогуше"
                                $ RogueX.Pet_vin = "дорогушу"
                                $ RogueX.Pet_tvo = "дорогушей"
                                $ RogueX.Pet_pre = "дорогуше"
                                $ RogueX.FaceChange("sexy", 1)
                                ch_r "Ох, как романтично, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                $ RogueX.Eyes = "side"
                                ch_r "Навевает. . . плохие воспоминания, [RogueX.Petname]."

                        "Думаю, буду звать тебя \"милая\".":
                            if "boyfriend" in RogueX.Petnames or ApprovalCheck(RogueX, 500, "L"):
                                $ RogueX.Pet = "милая"
                                $ RogueX.Pet_rod = "милой"
                                $ RogueX.Pet_dat = "милой"
                                $ RogueX.Pet_vin = "милую"
                                $ RogueX.Pet_tvo = "милой"
                                $ RogueX.Pet_pre = "милой"
                                ch_r "Оу, как мило, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                ch_r "Это слегка чересчур, [RogueX.Petname]."

                        "Думаю, буду звать тебя \"секси\".":
                            if "lover" in RogueX.Petnames or ApprovalCheck(RogueX, 900):
                                $ RogueX.Pet = "секси"
                                $ RogueX.Pet_rod = "секси"
                                $ RogueX.Pet_dat = "секси"
                                $ RogueX.Pet_vin = "секси"
                                $ RogueX.Pet_tvo = "секси"
                                $ RogueX.Pet_pre = "секси"
                                $ RogueX.FaceChange("sexy", 1)
                                ch_r "Да ты и сам не так уж плох, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                ch_r "Это совсем не к месту, [RogueX.Petname]."

                        "Думаю, буду звать тебя \"любимая\".":
                            if "lover" in RogueX.Petnames or ApprovalCheck(RogueX, 900):
                                $ RogueX.Pet = "любимая"
                                $ RogueX.Pet_rod = "любимой"
                                $ RogueX.Pet_dat = "любимой"
                                $ RogueX.Pet_vin = "любимую"
                                $ RogueX.Pet_tvo = "любимой"
                                $ RogueX.Pet_pre = "любимой"
                                $ RogueX.FaceChange("sexy", 1)
                                ch_r "Ох, Я тоже тебя люблю, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                ch_r "Ты забегаешь далеко вперед, [RogueX.Petname]."

                        "Назад":
                            pass

                "Грубо":
                    menu:
                        "Думаю, буду звать тебя \"рабыня\".":
                            if "master" in RogueX.Petnames or ApprovalCheck(RogueX, 700, "O"):
                                $ RogueX.Pet = "рабыня"
                                $ RogueX.Pet_rod = "рабыни"
                                $ RogueX.Pet_dat = "рабыне"
                                $ RogueX.Pet_vin = "рабыню"
                                $ RogueX.Pet_tvo = "рабыней"
                                $ RogueX.Pet_pre = "рабыне"
                                $ RogueX.FaceChange("bemused", 1)
                                ch_r "Как пожелаешь, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                ch_r "Никто не смеет так ко мне обращаться, [RogueX.Petname]."

                        "Думаю, буду звать тебя \"питомец\".":
                            if "master" in RogueX.Petnames or ApprovalCheck(RogueX, 600, "O"):
                                $ RogueX.Pet = "питомец"
                                $ RogueX.Pet_rod = "питомце"
                                $ RogueX.Pet_dat = "питомцу"
                                $ RogueX.Pet_vin = "питомца"
                                $ RogueX.Pet_tvo = "питомцем"
                                $ RogueX.Pet_pre = "питомце"
                                $ RogueX.FaceChange("bemused", 1)
                                ch_r "Хммм. Не забудь погладить меня, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                ch_r "Я тебе не питомец, [RogueX.Petname]."

                        "Думаю, буду звать тебя \"шлюха\".":
                            if "sex friend" in RogueX.Petnames or ApprovalCheck(RogueX, 1000, "OI"):
                                $ RogueX.Pet = "шлюха"
                                $ RogueX.Pet_rod = "шлюхи"
                                $ RogueX.Pet_dat = "шлюхе"
                                $ RogueX.Pet_vin = "шлюху"
                                $ RogueX.Pet_tvo = "шлюхой"
                                $ RogueX.Pet_pre = "шлюхе"
                                $ RogueX.FaceChange("sexy")
                                ch_r "Ты слишком хорошо меня знаешь, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                $ RogueX.Mouth = "surprised"
                                ch_r "Никогда!"

                        "Думаю, буду звать тебя \"блядь\".":
                            if "fuckbuddy" in RogueX.Petnames or ApprovalCheck(RogueX, 1100, "OI"):
                                $ RogueX.Pet = "блядь"
                                $ RogueX.Pet_rod = "бляди"
                                $ RogueX.Pet_dat = "бляде"
                                $ RogueX.Pet_vin = "блядь"
                                $ RogueX.Pet_tvo = "блядью"
                                $ RogueX.Pet_pre = "бляде"
                                $ RogueX.FaceChange("sly")
                                ch_r "Наверное, так и есть. . ."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                ch_r "Только попробуй повторить, [RogueX.Petname]!"

                        "Думаю, буду звать тебя \"сладкогрудая\".":
                            if "sex friend" in RogueX.Petnames or ApprovalCheck(RogueX, 1500):
                                $ RogueX.Pet = "сладкогрудая"
                                $ RogueX.Pet_rod = "сладкогрудой"
                                $ RogueX.Pet_dat = "сладкогрудой"
                                $ RogueX.Pet_vin = "сладкогрудую"
                                $ RogueX.Pet_tvo = "сладкогрудой"
                                $ RogueX.Pet_pre = "сладкогрудой"
                                $ RogueX.FaceChange("sly", 1)
                                ch_r "Хех."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                ch_r "Тогда тебе лучше не показываться мне на глаза, [RogueX.Petname]."

                        "Думаю, буду звать тебя \"любовница\".":
                            if "sex friend" in RogueX.Petnames or ApprovalCheck(RogueX, 600, "I"):
                                $ RogueX.Pet = "любовница"
                                $ RogueX.Pet_rod = "любовницы"
                                $ RogueX.Pet_dat = "любовнице"
                                $ RogueX.Pet_vin = "любовницу"
                                $ RogueX.Pet_tvo = "любовницей"
                                $ RogueX.Pet_pre = "любовнице"
                                $ RogueX.FaceChange("sly")
                                ch_r "Мммм. . ."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                ch_r "Эй, нет, [RogueX.Petname]."

                        "Думаю, буду звать тебя \"секс-партнерша\".":
                            if "fuckbuddy" in RogueX.Petnames or ApprovalCheck(RogueX, 700, "I"):
                                $ RogueX.Pet = "секс-партнерша"
                                $ RogueX.Pet_rod = "секс-партнерши"
                                $ RogueX.Pet_dat = "секс-партнерше"
                                $ RogueX.Pet_vin = "секс-партнершу"
                                $ RogueX.Pet_tvo = "секс-партнершей"
                                $ RogueX.Pet_pre = "секс-партнерше"
                                $ RogueX.FaceChange("sly")
                                ch_r "Хорошо, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                $ RogueX.Mouth = "surprised"
                                ch_r "Совсем не к месту, [RogueX.Petname]."

                        "Думаю, буду звать тебя \"доченька\".":
                            if "daddy" in RogueX.Petnames or ApprovalCheck(RogueX, 1200):
                                $ RogueX.Pet = "доченька"
                                $ RogueX.Pet_rod = "доченьки"
                                $ RogueX.Pet_dat = "доченьке"
                                $ RogueX.Pet_vin = "доченьку"
                                $ RogueX.Pet_tvo = "доченькой"
                                $ RogueX.Pet_pre = "доченьке"
                                $ RogueX.FaceChange("smile", 1)
                                ch_r "Тебе виднее, [RogueX.Petname]."
                            else:
                                $ RogueX.FaceChange("angry", 1)
                                ch_r "Я тебе не дочь, [RogueX.Petname]."

                        "Назад":
                            pass

                "Неважно.":
                    return
        return

#label Rogue_Namecheck(Cnt = 0, Ugh = 0):#RogueX.Pet is the internal pet name, Cnt and Ugh are internal count variable defunct, remove, replaced with $ RogueX.NameCheck()

# start Rogue_Names//////////////////////////////////////////////////////////
label Rogue_Rename:
        #Sets alternate names from Rogue
        $ RogueX.Mouth = "smile"
        ch_r "Да?"
        menu:
            extend ""
            "Мне кажется, \"Роуг\" подходит тебе." if RogueX.Name != "Роуг":
                    $ RogueX.Name = "Роуг"
                    $ RogueX.Name_rod = "Роуг"
                    $ RogueX.Name_dat = "Роуг"
                    $ RogueX.Name_vin = "Роуг"
                    $ RogueX.Name_tvo = "Роуг"
                    $ RogueX.Name_pre = "Роуг"
                    ch_r "Хорошо."
            "Мне нравится как звучит имя \"Мария.\"" if RogueX.Name != "Мария" and "Marie" in RogueX.Names:
                    $ RogueX.Name = "Мария"
                    $ RogueX.Name_rod = "Марии"
                    $ RogueX.Name_dat = "Марии"
                    $ RogueX.Name_vin = "Марию"
                    $ RogueX.Name_tvo = "Марией"
                    $ RogueX.Name_pre = "Марии"
                    ch_r "Да. . ."
            "Мне нравится как звучит имя \"Анна.\"" if RogueX.Name != "Анна" and "Anna" in RogueX.Names:
                    $ RogueX.Name = "Анна"
                    $ RogueX.Name_rod = "Анны"
                    $ RogueX.Name_dat = "Анне"
                    $ RogueX.Name_vin = "Анну"
                    $ RogueX.Name_tvo = "Анной"
                    $ RogueX.Name_pre = "Анне"
                    ch_r "Хорошо. . ."
            "Мне нравится как звучит имя \"Анна-Мария.\"" if RogueX.Name != "Анна-Мария" and "Anna-Marie" in RogueX.Names:
                    $ RogueX.Name = "Анна-Мария"
                    $ RogueX.Name_rod = "Анны-Марии"
                    $ RogueX.Name_dat = "Анне-Марии"
                    $ RogueX.Name_vin = "Анну-Марию"
                    $ RogueX.Name_tvo = "Анной-Марией"
                    $ RogueX.Name_pre = "Анне-Марии"
                    ch_r "Ну, если тебе так нравится. . ."
            "Неважно.":
                return
        return
# end Rogue_Names//////////////////////////////////////////////////////////

# start Rogue_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Personality(Cnt = 0):
        if not RogueX.Chat[4] or Cnt:
            "Поскольку у вас все хорошо получается в одной области, вы можете убедить Эмму сосредоточиться на любой другой."
            "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
            "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
        menu:
            ch_r "Конечно, в чем дело?"
            "Больше Послушания. [[Любовь в Послушание]" if RogueX.Love > 900:
                ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
                ch_r "Ну, пожалуй, для тебя я могла бы стать немного более послушной."
                $ RogueX.Chat[4] = 1
            "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if RogueX.Love > 900:
                ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
                ch_r "Ну, пожалуй, для тебя я могла бы стать немного более раскрепощенной."
                $ RogueX.Chat[4] = 2

            "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if RogueX.Obed > 900:
                ch_p "Я хочу, чтобы ты была более раскрепощенной."
                ch_r "Хорошо, я постараюсь проявлять больше инициативы."
                $ RogueX.Chat[4] = 3
            "Больше Любви. [[Повиновение в Любовь]" if RogueX.Obed > 900:
                ch_p "Я хочу, чтобы ты училась любить меня."
                ch_r "Я постараюсь."
                $ RogueX.Chat[4] = 4

            "Больше Повиновения. [[Раскрепощенность в Повиновение]" if RogueX.Inbt > 900:
                ch_p "Я знаю, что нам итак весело, но разве ты не можешь иногда слушаться меня?"
                ch_r "Думаю, это может быть интересно. . ."
                $ RogueX.Chat[4] = 5

            "Больше Любви. [[Раскрепощенность в Любовь]" if RogueX.Inbt > 900:
                ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
                ch_r "Ну, пожалуй, я начала привыкать к тебе. . ."
                $ RogueX.Chat[4] = 6

            "Просто делай то, что тебе нравится. . .[[Сбросить]" if RogueX.Chat[4]:
                ch_p "Помнишь, что мы обсуждали? Забудь."
                ch_r "Эм, ладно."
                $ RogueX.Chat[4] = 0
            "Повторить правила":
                call Rogue_Personality(1)
                return
            "Неважно.":
                return
        return
# end Rogue_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Rogue_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Rogue_Summon(Tempmod = Tempmod):
    $ RogueX.OutfitChange()
    if "no summon" in RogueX.RecentActions:
            # If she's refused to follow you once recently
            if "angry" in RogueX.RecentActions:
                ch_r "Какая часть слова \"нет\" тебе не понятна?"
            elif RogueX.RecentActions.count("no summon") > 1:
                if not Player.Male:
                    ch_r "Я тебе уже сказала 'нет', если ты не поняла."
                else:
                    ch_r "Я тебе уже сказала 'нет', если ты не понял."
                $ RogueX.RecentActions.append("angry")
            elif Time_Count >= 3: #night time
                ch_r "Я сказала тебе, сегодня уже слишком поздно."
            else:
                ch_r "Я же сказала, что занята."
            $ RogueX.RecentActions.append("no summon")
            return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if RogueX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif RogueX.Loc == "bg dangerroom":
        $ Tempmod = -20
    elif RogueX.Loc == "bg showerroom":
        $ Tempmod = -40

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"
    elif "les" in RogueX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(RogueX, 2000):
                    ch_r "Я сейчас не одна, [RogueX.Petname], не хочешь присоединиться к нам?"
                    menu:
                        extend ""
                        "Хочу":
                            $ Line = "go to"
                        "Нет, спасибо":
                            ch_r "Как знаешь."
                            return
            else:
                    ch_r "Что? Эмм. . . нет, не сейчас"
                    ch_r "Давай как-нибудь в другой раз."
                    $ RogueX.RecentActions.append("no summon")
                    return
    elif Time_Count >= 3: #night time
            if ApprovalCheck(RogueX, 700, "L") or ApprovalCheck(RogueX, 300, "O"):
                    #It's night time but she likes you.
                    ch_r "Ладно, уже поздно, но, думаю, я могу еще немного побыть с тобой."
                    $ RogueX.Loc = bg_current
                    call Taboo_Level
                    call Set_The_Scene
            else:
                    #It's night time and she isn't into you
                    ch_r "Уже поздно, [RogueX.Petname], давай завтра."
                    $ RogueX.RecentActions.append("no summon")
            return
    elif not ApprovalCheck(RogueX, 700, "L") or not ApprovalCheck(RogueX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(RogueX, 300):
                ch_r "Мне не особо интересно, [RogueX.Petname]."
                $ RogueX.RecentActions.append("no summon")
                return


        if "summoned" in RogueX.RecentActions:
                pass
        elif "goto" in RogueX.RecentActions:
                ch_r "Ты был рядом, а потом сбежал. Почему бы тебе просто не вернуться назад?"
        elif RogueX.Loc == "bg classroom":
                ch_r "Я вообще-то на занятиях, [RogueX.Petname], можешь присоединиться ко мне."
        elif RogueX.Loc == "bg dangerroom":
                ch_r "Я сейчас на тренировке, [RogueX.Petname], не хочешь присоединиться?"
        elif RogueX.Loc == "bg campus":
                ch_r "Я гуляю по кампусу, [RogueX.Petname], хочешь составить мне компанию?"
        elif RogueX.Loc == "bg rogue":
                ch_r "Я в своей комнате, [RogueX.Petname], не хочешь заскочить?"
        elif RogueX.Loc == "bg player":
                ch_r "Я случайно оказалась в твоей комнате, [RogueX.Petname], приходи. . ."
        elif RogueX.Loc == "bg showerroom":
            if ApprovalCheck(RogueX, 1600):
                ch_r "Я сейчас в душе, [RogueX.Petname], хочешь присоединиться?"
            else:
                ch_r "Я сейчас в душе, [RogueX.Petname], давай увидимся потом."
                $ RogueX.RecentActions.append("no summon")
                return
        elif RogueX.Loc == "hold":
                ch_r "Я сейчас не на территории кампуса, давай увидимся в другой раз?"
                $ RogueX.RecentActions.append("no summon")
                return
        else:
                #Unknown location
                ch_r "Почему бы тебе не подойти сюда, [RogueX.Petname]?"

        if "summoned" in RogueX.RecentActions:
            ch_r "Ладно, но тебе не надоело гонять меня?"
            $ Line = "yes"

        elif "goto" in RogueX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
#                                ch_r "See you then!"
                                $ Line = "go to"
                "Нет.":
                                ch_r "Ну ладно."
                "Мне бы {i}очень{/i} хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(RogueX, 600, "L") or ApprovalCheck(RogueX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(RogueX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(RogueX, 1400):
                                #she is generally favorable
                                ch_r "Думаю, можно, [RogueX.Petname]."
                                $ Line = "yes"
                        elif ApprovalCheck(RogueX, 200, "O"):
                                #she is not obedient
                                ch_r "Я так не думаю."
                                ch_r "Если ты хочешь меня увидеть, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(RogueX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(RogueX, 1400):
                                #she is generally favorable
                                ch_r "Думаю, можно, [RogueX.Petname]."
                                $ Line = "yes"
                        elif ApprovalCheck(RogueX, 200, "O"):
                                #she is not obedient
                                ch_r "Я так не думаю."
                                ch_r "Если ты хочешь меня увидеть, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Конечно, сейчас приду.":
                        $ RogueX.Statup("Love", 55, 1)
                        $ RogueX.Statup("Inbt", 30, 1)
#                        ch_r "See you then!"
                        $ Line = "go to"

                "Нет, поговорим позже.":
                        $ RogueX.Statup("Obed", 50, 1)
                        $ RogueX.Statup("Obed", 30, 2)
                        ch_r "Ох, ну ладно."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                        if ApprovalCheck(RogueX, 600, "L") or ApprovalCheck(RogueX, 1400):
                            $ RogueX.Statup("Love", 70, 1)
                            $ RogueX.Statup("Obed", 50, 1)
                            $ Line = "lonely"
                        else:
                            $ RogueX.Statup("Inbt", 30, 1)
                            $ Line = "no"

                "Приходи ко мне, будет весело.":
                        if ApprovalCheck(RogueX, 400, "L") and ApprovalCheck(RogueX, 800):
                            $ RogueX.Statup("Love", 70, 1)
                            $ RogueX.Statup("Obed", 50, 1)
                            $ Line = "fun"
                        else:
                            $ RogueX.Statup("Inbt", 30, 1)
                            $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(RogueX, 600, "O"):
                            #she is obedient
                            $ RogueX.Statup("Love", 50, 1, 1)
                            $ RogueX.Statup("Love", 40, -1)
                            $ RogueX.Statup("Obed", 90, 1)
                            $ Line = "command"

                        elif D20 >= 7 and ApprovalCheck(RogueX, 1400):
                            #she is generally favorable
                            $ RogueX.Statup("Love", 70, -2)
                            $ RogueX.Statup("Love", 90, -1)
                            $ RogueX.Statup("Obed", 50, 2)
                            $ RogueX.Statup("Obed", 90, 1)
                            ch_r "Думаю, можно, [RogueX.Petname]."
                            $ Line = "yes"

                        elif ApprovalCheck(RogueX, 200, "O"):
                            #she is not obedient
                            $ RogueX.Statup("Love", 70, -4)
                            $ RogueX.Statup("Love", 90, -2)
                            ch_r "Я не знаю, кем ты себя возомнила, раз так со мной разговариваешь."
                            $ RogueX.Statup("Inbt", 40, 2)
                            $ RogueX.Statup("Inbt", 60, 1)
                            $ RogueX.Statup("Obed", 70, -2)
                            ch_r "Если ты хочешь меня увидеть, ты знаешь, где меня найти."
                        else:
                            #she is obedient, but you failed to meet the checks
                            $ RogueX.Statup("Inbt", 30, 1)
                            $ RogueX.Statup("Inbt", 50, 1)
                            $ RogueX.Statup("Love", 50, -1, 1)
                            $ RogueX.Statup("Obed", 70, -1)
                            $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(RogueX, 600, "O"):
                            #she is obedient
                            $ RogueX.Statup("Love", 50, 1, 1)
                            $ RogueX.Statup("Love", 40, -1)
                            $ RogueX.Statup("Obed", 90, 1)
                            $ Line = "command"

                        elif D20 >= 7 and ApprovalCheck(RogueX, 1400):
                            #she is generally favorable
                            $ RogueX.Statup("Love", 70, -2)
                            $ RogueX.Statup("Love", 90, -1)
                            $ RogueX.Statup("Obed", 50, 2)
                            $ RogueX.Statup("Obed", 90, 1)
                            ch_r "Думаю, можно, [RogueX.Petname]."
                            $ Line = "yes"

                        elif ApprovalCheck(RogueX, 200, "O"):
                            #she is not obedient
                            $ RogueX.Statup("Love", 70, -4)
                            $ RogueX.Statup("Love", 90, -2)
                            ch_r "Я не знаю, кем ты себя возомнил, раз так со мной разговариваешь."
                            $ RogueX.Statup("Inbt", 40, 2)
                            $ RogueX.Statup("Inbt", 60, 1)
                            $ RogueX.Statup("Obed", 70, -2)
                            ch_r "Если ты хочешь меня увидеть, ты знаешь, где меня найти."
                        else:
                            #she is obedient, but you failed to meet the checks
                            $ RogueX.Statup("Inbt", 30, 1)
                            $ RogueX.Statup("Inbt", 50, 1)
                            $ RogueX.Statup("Love", 50, -1, 1)
                            $ RogueX.Statup("Obed", 70, -1)
                            $ Line = "no"
                        #end "ordered"
    else:
        #automatic acceptance
        if RogueX.Love > RogueX.Obed:
                ch_r "С удовольствием, [RogueX.Petname]."
        else:
                ch_r "Хорошо, я сейчас подойду, [RogueX.Petname]."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ RogueX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            if RogueX.Loc == "bg classroom":
                ch_r "Я не могу, [RogueX.Petname], впереди важный тест."
            elif RogueX.Loc == "bg dangerroom":
                ch_r "Жаль, но я не могу, [RogueX.Petname], мне нужно заниматься."
            else:
                ch_r "Извини, [RogueX.Petname], но сейчас я немного занята."
            $ RogueX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ Tempmod = 0
            $ Line = 0
            $ Nearby = []
            $ Party = [RogueX]
            $ RogueX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            if RogueX.Loc == "bg classroom":
                    ch_r "Тогда скоро увидимся!"
                    jump Class_Room
            elif RogueX.Loc == "bg dangerroom":
                    ch_r "Я пока разомнусь!"
                    jump Danger_Room
            elif RogueX.Loc == "bg rogue":
                    ch_r "Я пока приведу себя в порядок."
                    jump Rogue_Room
            elif RogueX.Loc == "bg player":
                    ch_r "Я буду ждать."
                    jump Player_Room
            elif RogueX.Loc == "bg showerroom":
                    ch_r "Ладно, я жду."
                    jump Shower_Room
            elif RogueX.Loc == "bg campus":
                    ch_r "Буду тебя выглядывать."
                    jump Campus
            elif RogueX.Loc != "hold":
                    ch_r "Увидимся там."
                    $ bg_current = RogueX.Loc
                    jump Misplaced
            else:
                    ch_r "Слушай, встретимся у меня в комнате."
                    $ RogueX.Loc = "bg rogue"
                    jump Rogue_Room

    #She's agreed to come over
    elif Line == "lonely":
            ch_r "О, ну и как я могу ответить тебе \"нет\", [RogueX.Petname]?"
    elif Line == "command":
            ch_r "Хорошо, если ты настаиваешь, [RogueX.Petname]."
    elif Line == "fun":
            ch_r "Конечно."

    $ RogueX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(RogueX)
            return
    $ RogueX.Loc = bg_current
    call Taboo_Level(0)
    $ RogueX.OutfitChange()
    call Set_The_Scene
    return

# End Rogue Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Rogue Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Leave(Tempmod=Tempmod):
        if "leaving" in RogueX.RecentActions:
            $ RogueX.DrainWord("leaving")
        else:
            return

        if bg_current == "bg dangerroom":
                call Gym_Exit([RogueX])

        if RogueX.Loc == "hold":
                # Activates if she's being moved out of play
                ch_r "Я ненадолго отойду, увидимся позже."
                return

        if RogueX in Party or "lockedtravels" in RogueX.Traits:
                #If she's in your party or if you've told her not to leave you
                #It resets her to your location
                $ RogueX.Loc = bg_current
                return

        elif "freetravels" in RogueX.Traits or not ApprovalCheck(RogueX, 700):
                #If you've told her to go wherever, or she just doesn't care what you think.
                $ RogueX.OutfitChange()
                if not ApprovalCheck(RogueX, 600, "LO"):
                                ch_r "Я ухожу, увидимся позже."
                elif RogueX.Loc == "bg classroom":
                                ch_r "Я сейчас собираюсь на занятия, [RogueX.Petname]."
                elif RogueX.Loc == "bg dangerroom":
                                ch_r "Я иду в Комнату Опасности, [RogueX.Petname]."
                elif RogueX.Loc == "bg campus":
                                ch_r "Пойду прогуляюсь по кампусу, [RogueX.Petname]."
                elif RogueX.Loc == "bg rogue":
                                ch_r "Я иду в свою комнату, [RogueX.Petname]."
                elif RogueX.Loc == "bg player":
                                ch_r "Я иду в твою комнату, [RogueX.Petname]."
                elif RogueX.Loc == "bg pool":
                                ch_r "Я иду к бассейну."
                elif RogueX.Loc == "bg showerroom":
                            if ApprovalCheck(RogueX, 1400):
                                ch_r "Я иду в душ, увидимся."
                            else:
                                ch_r "Мне. . . мне кое-куда нужно, увидимся позже."
                else:
                                ch_r "Мне надо отойти, увидимся позже."
                hide Rogue_Sprite
                hide Rogue_Seated
                return
                #End Free Travels

        $ RogueX.OutfitChange()

        if "follow" not in RogueX.Traits:
                # Sets a key to show that she's asked you to follow her at least once
                $ RogueX.Traits.append("follow")

        $ D20 = renpy.random.randint(1, 20)
        $ Line = 0
        # Sets her preferences
        if RogueX.Loc == "bg classroom": #fix change these if changed function
            $ Tempmod = 10
        elif RogueX.Loc == "bg dangerroom":
            $ Tempmod = 20
        elif RogueX.Loc == "bg showerroom":
            $ Tempmod = 40


        if RogueX.Loc == "bg classroom":
                        ch_r "Я сейчас собираюсь на занятия, [RogueX.Petname], можешь пойти со мной."
        elif RogueX.Loc == "bg dangerroom":
                        ch_r "Я иду в Комнату Опасности, [RogueX.Petname], не хочешь со мной?"
        elif RogueX.Loc == "bg campus":
                        ch_r "Пойду прогуляюсь по кампусу, [RogueX.Petname], хочешь составить мне компанию?"
        elif RogueX.Loc == "bg rogue":
                        ch_r "Я иду в свою комнату, [RogueX.Petname], не хочешь заскочить?"
        elif RogueX.Loc == "bg player":
                        ch_r "Я иду в твою комнату, [RogueX.Petname]."
        elif RogueX.Loc == "bg mall":
                        ch_r "Я собираюсь погулять по торговому центру, [RogueX.Petname], хочешь со мной?"
        elif RogueX.Loc == "bg showerroom":
                    if ApprovalCheck(RogueX, 1600):
                        ch_r "Я собираюсь в душ, [RogueX.Petname], не хочешь со мной?"
                    else:
                        ch_r "Я собираюсь в душ, [RogueX.Petname], увидимся позже."
                        return
        elif RogueX.Loc == "bg pool":
                        ch_r "Я иду к бассейну. Хочешь со мной?"
        else:
                        ch_r "Почему бы тебе не пойти со мной, [RogueX.Petname]?"

        menu:
            extend ""
            "Конечно, я сразу за тобой.":
                    if "followed" not in RogueX.RecentActions:
                        $ RogueX.Statup("Love", 55, 1)
                        $ RogueX.Statup("Inbt", 30, 1)
                    $ Line = "go to"

            "Нет, поговорим позже.":
                    if "followed" not in RogueX.RecentActions:
                        $ RogueX.Statup("Obed", 50, 1)
                        $ RogueX.Statup("Obed", 30, 2)
                    ch_r "Ох, хорошо."

            "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                    if ApprovalCheck(RogueX, 600, "L") or ApprovalCheck(RogueX, 1400):
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Love", 70, 1)
                            $ RogueX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Inbt", 30, 1)
                        $ Line = "no"

            "Останься со мной, будет весело.":
                    if ApprovalCheck(RogueX, 400, "L") and ApprovalCheck(RogueX, 800):
                        $ RogueX.Statup("Love", 70, 1)
                        $ RogueX.Statup("Obed", 50, 1)
                        $ Line = "fun"
                    else:
                        $ RogueX.Statup("Inbt", 30, 1)
                        $ Line = "no"

            "Нет, останься здесь.":
                    if ApprovalCheck(RogueX, 600, "O"):
                        #she is obedient
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Love", 50, 1, 1)
                            $ RogueX.Statup("Love", 40, -1)
                            $ RogueX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(RogueX, 1400):
                        #she is generally favorable
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Love", 70, -2)
                            $ RogueX.Statup("Love", 90, -1)
                            $ RogueX.Statup("Obed", 50, 2)
                            $ RogueX.Statup("Obed", 90, 1)
                        ch_r "Думаю, можно."
                        $ Line = "yes"

                    elif ApprovalCheck(RogueX, 200, "O"):
                        #she is not obedient
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Love", 70, -4)
                            $ RogueX.Statup("Love", 90, -2)
                        if not Player.Male:
                            ch_r "Я не знаю, кем ты себя возомнила, раз так со мной разговариваешь."
                        else:
                            ch_r "Я не знаю, кем ты себя возомнил, раз так со мной разговариваешь."
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Inbt", 40, 2)
                            $ RogueX.Statup("Inbt", 60, 1)
                            $ RogueX.Statup("Obed", 70, -2)
                        ch_r "Если ты хочешь меня увидеть, ты знаешь, где меня найти."
                    else:
                        #she is obedient, but you failed to meet the checks
                        if "followed" not in RogueX.RecentActions:
                            $ RogueX.Statup("Inbt", 30, 1)
                            $ RogueX.Statup("Inbt", 50, 1)
                            $ RogueX.Statup("Love", 50, -1, 1)
                            $ RogueX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #End ordered to stay

        $ RogueX.RecentActions.append("followed")
        if not Line:
                #You end the dialog neutrally
                hide Rogue_Sprite
                hide Rogue_Seated
                call Gym_Clothes_Off([RogueX])
                return

        if Line == "no":
                # She's refused, context based dialog
                if RogueX.Loc == "bg classroom":
                    ch_r "Я не могу, [RogueX.Petname], впереди важный тест."
                elif RogueX.Loc == "bg dangerroom":
                    ch_r "Мне жаль, но я не могу, [RogueX.Petname], мне нужно заниматься."
                else:
                    ch_r "Извини, [RogueX.Petname], но сейчас я немного занята."
                hide Rogue_Sprite
                hide Rogue_Seated
                call Gym_Clothes_Off([RogueX])
                return

        elif Line == "go to":
                #You agreed to go to her instead
                #$ Party.append(RogueX)
                $ Tempmod = 0
                $ Line = 0
                call DrainAll("leaving")
                call DrainAll("arriving")
                $ RogueX.RecentActions.append("goto")
                $ Player.RecentActions.append("goto")
                $ Player.DrainWord("locked",0,0,1)
                hide Rogue_Sprite
                hide Rogue_Seated
                $ Nearby = []
                $ Party = [RogueX]
                call Gym_Clothes_Off([RogueX])
                if RogueX.Loc == "bg classroom":
                    ch_r "Тогда скоро увидимся!"
                    jump Class_Room_Entry
                elif RogueX.Loc == "bg dangerroom":
                    ch_r "Я пока разомнусь!"
                    jump Danger_Room_Entry
                elif RogueX.Loc == "bg rogue":
                    ch_r "Я буду ждать."
                    jump Rogue_Room
                elif RogueX.Loc == "bg player":
                    ch_r "Я буду ждать."
                    jump Player_Room
                elif RogueX.Loc == "bg showerroom":
                    ch_r "Думаю, увидимся там."
                    jump Shower_Room_Entry
                elif RogueX.Loc == "bg campus":
                    ch_r "Скоро увидимся."
                    jump Campus_Entry
                elif RogueX.Loc == "bg pool":
                    ch_r "Скоро увидимся."
                    jump Pool_Entry
                elif RogueX.Loc == "bg mall":
                    ch_r "Скоро увидимся."
                    jump Mall_Entry
                else:
                    ch_r "Слушай, встретимся у меня в комнате."
                    $ RogueX.Loc = "bg rogue"
                    jump Rogue_Room
                #End "goto" where she's at

        #She's agreed to come over
        elif Line == "lonely":
                ch_r "О, ну и как я могу ответить тебе \"нет\", [RogueX.Petname]?"
        elif Line == "command":
                ch_r "Хорошо, если ты настаиваешь, [RogueX.Petname]."
        elif Line:
                ch_r "Конечно."

        $ Line = 0
        ch_r "Я могу остаться ненадолго."
        $ RogueX.Loc = bg_current
        call Taboo_Level(0)
        return

# End Rogue Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Rogue's Clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Clothes:
    if RogueX.Taboo:
            if "exhibitionist" in RogueX.Traits:
                ch_r "Ооох, шалунишка. . ."
            elif ApprovalCheck(RogueX, 900, TabM=4) or ApprovalCheck(RogueX, 400, "I", TabM=3):
                ch_r "Ну, тут довольно людно, но, думаю, я могла бы. . ."
            else:
                ch_r "Тебе не кажется, что здесь слишком людно?"
                ch_r "Давай поговорим об этом наедине."
                return
    elif ApprovalCheck(RogueX, 900, TabM=4) or ApprovalCheck(RogueX, 600, "L") or ApprovalCheck(RogueX, 300, "O"):
                if not Player.Male:
                    ch_r "Ладно, чего ты хотела?"
                else:
                    ch_r "Ладно, чего ты хотел?"
    else:
                ch_r "Меня не интересует твое мнение по поводу одежды."
                return
    if Girl != RogueX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = RogueX
    call Shift_Focus(Girl)

label Rogue_Wardrobe_Menu:
    while True:
        $ Trigger = 1 # to prevent Focus swapping. . .
        $ RogueX.FaceChange()
        menu:
            ch_r "Что именно тебя интересует?"
            "Верх":
                    call Rogue_Clothes_Over
            "Низ":
                    call Rogue_Clothes_Legs
            "Нижнее белье":
                    call Rogue_Clothes_Under
            "Аксессуары":
                    call Rogue_Clothes_Misc
            "Управление нарядами":
                    call Rogue_Clothes_Outfits
            "Давай поговорим о том, что ты носишь.":
                    call Clothes_Schedule(RogueX)

            "Могу я посмотреть?" if RogueX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(RogueX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_r "Ну как? . ."
                    hide PhoneSex
            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(RogueX,0,2)
                    if _return:
                        hide DressScreen

            "Может, тебе будет комфортнее за ширмой? (locked)" if RogueX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if RogueX.Loc == bg_current and not RogueX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if not Player.Male and "girltalk" not in RogueX.History and "nogirls" not in RogueX.History:
                            ch_r "Мы девушки, мне стесняться нечего."
                    elif ApprovalCheck(RogueX, 1500) or (RogueX.SeenChest and RogueX.SeenPussy):
                            ch_r "Не нужно, спасибо."
                    else:
                            show DressScreen zorder 150
                            ch_r "Так будет лучше, спасибо."

            "У меня есть подарок для тебя (locked)" if RogueX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if RogueX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(RogueX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ RogueX.OutfitChange()
                    $ RogueX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != RogueX:
                            ch_p "Я хочу поговорить о твоей одежде."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = RogueX
                    call Shift_Focus(Girl)

            "Сменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current:
                    pass
            "Сменить вид" if Girl.Loc == bg_current:
                    call WardrobeView(RogueX)

            "Неважно, ты и так хорошо выглядишь [[назад]":
                    call Girl_Pos_Reset(RogueX)
                    if "wardrobe" not in RogueX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if RogueX.Chat[1] <= 1:
                                    $ RogueX.Statup("Love", 70, 10)
                                    $ RogueX.Statup("Obed", 20, 10)
                                    ch_r "Оу, как мило."
                            elif RogueX.Chat[1] <= 10:
                                    $ RogueX.Statup("Love", 70, 5)
                                    $ RogueX.Statup("Obed", 20, 5)
                                    ch_r "Спасибо."
                            elif RogueX.Chat[1] <= 50:
                                    $ RogueX.Statup("Love", 70, 1)
                                    $ RogueX.Statup("Obed", 20, 1)
                                    ch_r "Ладно."
                            else:
                                    ch_r "Ладно."
                            $ RogueX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(RogueX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ RogueX.OutfitChange()
                    #sets up a temporary outfit
                    $ RogueX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ RogueX.Chat[1] += 1
                    $ Trigger = 0
                    if RogueX.Panties and "pantyless" in RogueX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ RogueX.DailyActions.remove("pantyless")
                    return
        #Loops back up
#    jump Rogue_Wardrobe_Menu
    #End of Rogue Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Rogue_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(RogueX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(RogueX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(RogueX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(RogueX,4,1)
                    "Одежда для сна":
                                call OutfitShame(RogueX,7,1)
                    "Купальник":
                                call OutfitShame(RogueX,10,1)

                    "Повседневка 1" if ApprovalCheck(RogueX, 2500):
                                call OutfitShame(RogueX,11,1)
                    "Повседневка 2" if ApprovalCheck(RogueX, 2500):
                                call OutfitShame(RogueX,12,1)
                    "Неважно":
                                pass

        "Мне очень нравится как сочетается зеленый топ с юбкой.":
                #Green
                $ RogueX.OutfitChange("casual1")
                menu:
                    "Надень-ка их. [[сменить текущий наряд]":
                        $ RogueX.Outfit = "casual1"
                        $ RogueX.Shame = 0
                        ch_r "Хорошо, [RogueX.Petname], мне они тоже нравятся."
                    "Но давай попробуем что-нибудь другое.":
                        ch_r "Конечно."

        "Розовый топ с брюками отлично тебе подходят.":
                #Pink
                $ RogueX.OutfitChange("casual2")
                menu:
                    "Надень-ка их. [[сменить текущий наряд]":
                        $ RogueX.Outfit = "casual2"
                        $ RogueX.Shame = 0
                        ch_r "Конечно, [RogueX.Petname]."
                    "Но давай попробуем что-нибудь другое.":
                        ch_r "Ладно."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not RogueX.Custom1[0] and not RogueX.Custom2[0] and not RogueX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if RogueX.Custom1[0] or RogueX.Custom2[0] or RogueX.Custom3[0]:
                        $ Cnt = 0
                        while 1:
                            menu:
                                "Надень Пользовательский 1 (locked)" if not RogueX.Custom1[0]:
                                        pass
                                "Надень Пользовательский 1" if RogueX.Custom1[0]:
                                        $ RogueX.OutfitChange("custom1")
                                        $ Cnt = 3
                                "Надень Пользовательский 2 (locked)" if not RogueX.Custom2[0]:
                                        pass
                                "Надень Пользовательский 2" if RogueX.Custom2[0]:
                                        $ RogueX.OutfitChange("custom2")
                                        $ Cnt = 5
                                "Надень Пользовательский 3 (locked)" if not RogueX.Custom3[0]:
                                        pass
                                "Надень Пользовательский 3" if RogueX.Custom3[0]:
                                        $ RogueX.OutfitChange("custom3")
                                        $ Cnt = 6

                                "Ты должна одеваться так, когда мы наедине (locked)" if not Cnt:
                                        pass
                                "Ты должна одеваться так, когда мы наедине" if Cnt:
                                        if Cnt == 5:
                                            $ RogueX.Clothing[9] = "custom2"
                                        elif Cnt == 6:
                                            $ RogueX.Clothing[9] = "custom3"
                                        else:
                                            $ RogueX.Clothing[9] = "custom1"
                                        ch_r "Хорошо."

                                "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                                menu:
                                                    ch_r "Ты о каком конкретно?"
                                                    "Пользовательский 1 [[очистить слот 1]" if RogueX.Custom1[0]:
                                                        ch_r "Ладно, без проблем."
                                                        $ RogueX.Custom1[0] = 0
                                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not RogueX.Custom1[0]:
                                                        pass
                                                    "Пользовательский 2 [[очистить слот 2]" if RogueX.Custom2[0]:
                                                        ch_r "Ладно, без проблем."
                                                        $ RogueX.Custom2[0] = 0
                                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not RogueX.Custom2[0]:
                                                        pass
                                                    "Пользовательский 3 [[очистить слот 3]" if RogueX.Custom3[0]:
                                                        ch_r "Ладно, без проблем."
                                                        $ RogueX.Custom3[0] = 0
                                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not RogueX.Custom3[0]:
                                                        pass
                                                    "Неважно [[назад]":
                                                        pass

                                "Тебе следует надеть его [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                                pass
                                "Тебе следует надеть его" if Cnt:
                                                call Custom_Out(RogueX,Cnt)
                                "Ладно, вернемся к началу нашего разговора. . .":
                                                $ Cnt = 0
                                                return
                                                #jump Rogue_Clothes

        "Наденешь спортивную одежду?" if not RogueX.Taboo or bg_current == "bg dangerroom":
                $ RogueX.OutfitChange("gym")

        "Наденешь одежду для сна?" if not RogueX.Taboo:
                if ApprovalCheck(RogueX, 1200):
                        $ RogueX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(RogueX)
                        if _return:
                            $ RogueX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (RogueX.Taboo and bg_current != "bg pool" and not ApprovalCheck(RogueX, 800, TabM=2)) or not RogueX.Swim[0]:
                $ RogueX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not RogueX.Taboo or bg_current == "bg pool" or ApprovalCheck(RogueX, 800, TabM=2)) and RogueX.Swim[0]:
                $ RogueX.OutfitChange("swimwear")

        "Наденешь хэллоуинский костюм?" if "halloween" in RogueX.History:
                ch_r "Конечно."
                $ RogueX.OutfitChange("costume")

        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ RogueX.FaceChange("sexy", 1)
                $ Line = 0
                if not RogueX.Chest and not RogueX.Panties and not RogueX.Over and not RogueX.Legs and not RogueX.Hose:
                        ch_r "Пожалуй. . ."
                elif RogueX.SeenChest and RogueX.SeenPussy and ApprovalCheck(RogueX, 1000, TabM=5):
                        ch_r "Шалунишка. . ."
                        $ Line = 1
                elif ApprovalCheck(RogueX, 2000, TabM=5):
                        if not Player.Male:
                            ch_r "Хмм. . . ты далеко заходишь, но, думаю, ты это заслужила. . ."
                        else:
                            ch_r "Хмм. . . ты далеко заходишь, но, думаю, ты это заслужил. . ."
                        $ Line = 1
                elif RogueX.SeenChest and RogueX.SeenPussy and ApprovalCheck(RogueX, 1000, TabM=0):
                        ch_r "Ну. . . вот если бы тут не было так. . . многолюдно."
                elif ApprovalCheck(RogueX, 2000, TabM=0):
                        ch_r "Я об этом бы подумала, если бы мы были наедине. . ."
                elif ApprovalCheck(RogueX, 1000, TabM=0):
                        $ RogueX.FaceChange("surprised", 1)
                        ch_r "Хмм. . . по-моему, ты торопишь события, [RogueX.Petname]."
                else:
                        $ RogueX.FaceChange("angry", 1)
                        ch_r "Ты меня что, считаешь дворовой шлюхой?"

                call expression RogueX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in RogueX.History:
                        $ Line = 0
                if Line:                                                            #If she got nude. . .
                    $ RogueX.OutfitChange("nude")
                    "Она скидывает с себя всю одежду."
                    call Girl_First_Topless(RogueX)
                    call Girl_First_Bottomless(RogueX,1)
                    $ RogueX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется. что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in RogueX.Traits:
                                    ch_r "А ты знаешь, как завести меня. . ."
                                    $ RogueX.Outfit = "nude"
                                    $ RogueX.Shame = 50
                            elif ApprovalCheck(RogueX, 750, "I") or ApprovalCheck(RogueX, 2500, TabM=0):
                                    ch_r "Хех, ну ладно, [RogueX.Petname]."
                                    $ RogueX.Outfit = "nude"
                                    $ RogueX.Shame = 50
                            else:
                                    $ RogueX.FaceChange("sexy", 1)
                                    $ RogueX.Eyes = "surprised"
                                    ch_r "Боюсь, что нет, [RogueX.Petname], это только для нас с тобой."
                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in RogueX.Traits:
                                    ch_r "Жаль, что ты не хочешь, чтобы я ходила в таком виде. . ."
                            elif ApprovalCheck(RogueX, 750, "I") or ApprovalCheck(RogueX, 2500, TabM=0):
                                    $ RogueX.FaceChange("bemused", 1)
                                    ch_r "Знаешь, я на секунду подумала, что ты захочешь, чтобы я так вышла на улицу. . ."
                                    ch_r "Хех. . ."
                            else:
                                    $ RogueX.FaceChange("confused", 1)
                                    ch_r "Ну, очевидно, я бы никогда не вышла в таком виде из комнаты."
                $ Line = 0

        "Неважно.":
                        return
                        #jump Rogue_Clothes
    return
    #jump Rogue_Clothes
    #End of Rogue Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Rogue_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять [get_clothing_name(RogueX.Over_key, vin)]?" if RogueX.Over:
                call Wardrobe_Remove(RogueX)

        "Примерь сетчатый топ." if RogueX.Over != "mesh top":
                $ RogueX.FaceChange("bemused", 1)
                if RogueX.Chest or (RogueX.SeenChest and ApprovalCheck(RogueX, 500, TabM=2)):
                    ch_r "Конечно."
                elif ApprovalCheck(RogueX, 600, TabM=0):
                    call Rogue_NoBra
                    if not _return:
                        if not ApprovalCheck(RogueX, 1200):
                            call Display_DressScreen(RogueX)
                            if not _return:
                                return  #jump Rogue_Clothes
                        else:
                                return  #jump Rogue_Clothes
                else:
                    call Display_DressScreen(RogueX)
                    if not _return:
                            ch_r "Боюсь, он слишком прозрачный, чтобы носить его на голое тело."
                            if not RogueX.Chest:
                                ch_r "На мне ведь нет лифчика."
                            return  #jump Rogue_Clothes

                $ RogueX.Over = "mesh top"
                menu:
                    ch_r "С ошейником?"
                    "Да":
                        $ RogueX.Neck = "spiked collar"
                    "Нет":
                        $ RogueX.Neck = 0
#                if RogueX.Chest == "buttoned tank":
#                    $ RogueX.Chest = "tank"
                if not RogueX.Chest and not renpy.showing('DressScreen'):
                    call Girl_First_Topless(RogueX)

        "Может, примеришь розовый топ?" if RogueX.Over != "pink top":
                $ RogueX.Over = "pink top"
                $ RogueX.Neck = 0

        "Может, примеришь зеленую толстовку?" if RogueX.Over != "hoodie":
                $ RogueX.Over = "hoodie"

        "Может, просто накинешь полотенце?" if RogueX.Over != "towel":
                $ RogueX.FaceChange("bemused", 1)
                if RogueX.Chest or RogueX.SeenChest:
                    ch_r "Пошленько."
                elif ApprovalCheck(RogueX, 900, TabM=0):
                    $ RogueX.FaceChange("perplexed", 1)
                    ch_r "Ну ладно? . ."
                else:
                    call Display_DressScreen(RogueX)
                    if not _return:
                            ch_r "Так мы не оставим ничего для воображения. . ."
                            return  #jump Rogue_Clothes
                $ RogueX.Over = "towel"

        "Как насчет примерить подаренную мной зеленую ночнушку?" if RogueX.Over != "nighty" and "nighty" in RogueX.Inventory:
                if RogueX.Legs:
                        ch_r "Она не сочетается с [get_clothing_name(RogueX.Legs_key, tvo)]."
                elif not ApprovalCheck(RogueX, 1100, TabM=3):
                        call Display_DressScreen(RogueX)
                        if not _return:
                                ch_r "Она слишком. . . прозрачная."
                                return  #jump Rogue_Clothes
                else:
                        ch_r "Конечно. . ."
                if "lace bra" in RogueX.Inventory:
                    $ RogueX.Chest = "lace bra"
                else:
                    $ RogueX.Chest = "bra"
                if "lace panties" in RogueX.Inventory:
                    $ RogueX.Panties = "lace panties"
                else:
                    $ RogueX.Panties = "black panties"
                $ RogueX.Over = "nighty"
                menu:
                    extend ""
                    "Отлично смотрится.":
                        pass
                    "Я хотела, чтобы ты надела {i}только{/i} ночнушку." if not Player.Male:
                        if ApprovalCheck(RogueX, 1400, TabM=3):
                            "Она снимает лифчик и надевает ночнушку."
                            $ RogueX.Panties = 0
                            $ RogueX.Chest = 0
                            ch_r "Хммм, ну ладно. . ."
                        elif ApprovalCheck(RogueX, 1200, TabM=3):
                            $ RogueX.Chest = 0
                            ch_r "Я предпочту не снимать трусики."
                        else:
                            ch_r "Довольствуйся тем, что имеешь."
                    "Я хотел, чтобы ты надела {i}только{/i} ночнушку." if Player.Male:
                        if ApprovalCheck(RogueX, 1400, TabM=3):
                            "Она снимает лифчик и надевает ночнушку."
                            $ RogueX.Panties = 0
                            $ RogueX.Chest = 0
                            ch_r "Хммм, ну ладно. . ."
                        elif ApprovalCheck(RogueX, 1200, TabM=3):
                            $ RogueX.Chest = 0
                            ch_r "Я предпочту не снимать трусики."
                        else:
                            ch_r "Довольствуйся тем, что имеешь."
                if not RogueX.Chest and not renpy.showing('DressScreen'):
                    call Girl_First_Topless(RogueX)

        "Неважно.":
            pass
    return  #jump Rogue_Clothes
    #End of Rogue Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Rogue_NoBra:
        menu:
            ch_r "На мне нет лифчика. . ."
            "Тогда надень какой-нибудь. . .":
                        if RogueX.SeenChest and ApprovalCheck(RogueX, 1000, TabM=3) or ApprovalCheck(RogueX, 1200, TabM=4):
                                $ RogueX.Blush = 2
                                ch_r "Меня это совсем не беспокоит. . ."
                                $ RogueX.Blush = 1
                        elif ApprovalCheck(RogueX, 900, TabM=2) and "lace bra" in RogueX.Inventory:
                                if not Player.Male:
                                    ch_r "Думаю, тут ты права. . ."
                                else:
                                    ch_r "Думаю, тут ты прав. . ."
                                $ RogueX.Chest  = "lace bra"
                                "Она достает свой кружевной лифчик и надевает его под [get_clothing_name(RogueX.Over_key, vin)]."
                        elif ApprovalCheck(RogueX, 800, TabM=2):
                                if not Player.Male:
                                    ch_r "Да, наверное ты права."
                                else:
                                    ch_r "Да, наверное ты прав."
                                $ RogueX.Chest = "bra"
                                "Она достает свой лифчик и надевает его под [get_clothing_name(RogueX.Over_key, vin)]."
                        elif ApprovalCheck(RogueX, 600, TabM=2):
                                if not Player.Male:
                                    ch_r "Да, наверное ты права."
                                else:
                                    ch_r "Да, наверное ты прав."
                                $ RogueX.Chest = "tank"
                                "Она достает майку и надевает ее под [get_clothing_name(RogueX.Over_key, vin)]."
                        else:
                                ch_r "Ага, но мне не хочется."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(RogueX, 1100, "LI", TabM=2) and RogueX.Love > RogueX.Inbt:
                                if not Player.Male:
                                    ch_r "Да, наверное ты права."
                                else:
                                    ch_r "Да, наверное ты прав."
                        elif ApprovalCheck(RogueX, 700, "OI", TabM=2) and RogueX.Obed > RogueX.Inbt:
                                ch_r "Конечно. . ."
                        elif ApprovalCheck(RogueX, 600, "I", TabM=2):
                                ch_r "Ага. . ."
                        elif ApprovalCheck(RogueX, 1300, TabM=2):
                                ch_r "Хорошо."
                        else:
                                $ RogueX.FaceChange("surprised")
                                $ RogueX.Brows = "angry"
                                if RogueX.Taboo > 20:
                                    ch_r "Но не на людях, [RogueX.Petname]!"
                                else:
                                    ch_r "Не настаивай на этом, [RogueX.Petname]."
                                call expression RogueX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно.":
                        ch_d "Ладно. . ."
                        return 0
        return 1
        #End of Rogue bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Rogue_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(RogueX.Legs_key, vin)]?" if RogueX.Legs:
                call Wardrobe_Remove(RogueX,1)

        "Может, наденешь свою юбочку?" if RogueX.Legs != "skirt":
                $ RogueX.Legs = "skirt"
                $ RogueX.Upskirt = 0

        "Джинсы отлично подчеркивают твою попку." if RogueX.Legs != "pants":
                $ RogueX.Legs = "pants"
                $ RogueX.Hose = 0

        "Леггинсы отлично дополнили бы твой образ." if RogueX.Hose != 'tights' and RogueX.Legs != "pants":
                $ RogueX.Hose = "tights"
        "Рванные леггинсы отлично дополнили бы твой образ." if RogueX.Hose != 'ripped tights' and "ripped tights" in RogueX.Inventory and RogueX.Legs != "pants":
                $ RogueX.Hose = "ripped tights"
        "Ты должна снять леггинсы." if RogueX.Hose == 'ripped tights' or RogueX.Hose == 'tights':
                $ RogueX.Hose = 0

        "Может, наденешь шортики?" if RogueX.Panties != "shorts":
                ch_r "Ладно."
                $ RogueX.Panties = "shorts"
        "Почему бы тебе не снять шорты?" if RogueX.Panties == "shorts":
                $ RogueX.FaceChange("sexy", 1)
                if RogueX.SeenPanties and RogueX.Panties and ApprovalCheck(RogueX, 500, TabM=5):
                    ch_r "Конечно."
                elif RogueX.SeenPussy and ApprovalCheck(RogueX, 900, TabM=4):
                    ch_r "Конечно, почему бы и нет?"
                elif ApprovalCheck(RogueX, 1300, TabM=2) and RogueX.Panties:
                    ch_r "Ну, если тебе так хочется. . ."
                elif ApprovalCheck(RogueX, 700) and not RogueX.Panties:
                    call Rogue_NoPantiesOn
                    if not _return and not RogueX.Panties:
                        if not ApprovalCheck(RogueX, 1500):
                            call Display_DressScreen(RogueX)
                            if not _return:
                                return  #jump Rogue_Clothes
                        else:
                                return  #jump Rogue_Clothes
                else:
                    call Display_DressScreen(RogueX)
                    if not _return:
                        ch_r "Не когда ты рядом, [RogueX.Petname]."
                        if not RogueX.Panties:
                            ch_r "Может, если я сначала надену трусики. . ."
                        return  #jump Rogue_Clothes
                if RogueX.Panties == "shorts":
                        $ RogueX.Panties = 0
                "Она стягивает с себя шорты и бросает их на пол."
                if renpy.showing('DressScreen'):
                    pass
                elif RogueX.Panties:
                    $ RogueX.SeenPanties = 1
                else:
                    call Girl_First_Bottomless(RogueX)

        "Может, наденешь свитер?" if RogueX.Acc != "sweater" and "halloween" in RogueX.History:
                ch_p "Как насчет того свитера, который ты надевала на вечеринку?"
                $ RogueX.Acc = "sweater"
        "Снимешь свитер?" if RogueX.Acc == "sweater" and "halloween" in RogueX.History:
                ch_p "Можешь снять свитер."
                $ RogueX.Acc = 0

        "Сними обувь (locked)" if not RogueX.Boots:
                pass
        "Сними [get_clothing_name(RogueX.Boots_key, vin)]" if RogueX.Boots:
                ch_p "Может, снимешь [get_clothing_name(RogueX.Boots_key, vin)]?"
                ch_r "Ладно."
                $ RogueX.Boots = 0
        "Надень ботинки" if RogueX.Boots != "boots":
                ch_p "Может, наденешь ботинки?"
                ch_r "Ладно."
                $ RogueX.Boots = "boots"
        "Надень кеды" if RogueX.Boots != "sneaks":
                ch_p "Может, наденешь кеды?"
                ch_r "Ладно."
                $ RogueX.Boots = "sneaks"

        "Неважно.":
            pass
    return  #jump Rogue_Clothes
    #End of Rogue Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Rogue_NoPantiesOn:
        menu:
            ch_r "Знаешь, я не ношу трусики. . ."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if RogueX.SeenPussy and ApprovalCheck(RogueX, 1100, TabM=4):
                                $ RogueX.Blush = 1
                                ch_r "Ладно."
                                $ RogueX.Blush = 0
                        elif ApprovalCheck(RogueX, 1500, TabM=4):
                                $ RogueX.Blush = 1
                                ch_r "Ладно."
                                $ RogueX.Blush = 0
                        elif ApprovalCheck(RogueX, 700, TabM=4):
                                ch_r "Мне нравится ход твоих мыслей."
                                if "lace panties" in RogueX.Inventory:
                                        $ RogueX.Panties  = "lace panties"
                                else:
                                        $ RogueX.Panties = "black panties"
                                if ApprovalCheck(RogueX, 1200, TabM=4) and RogueX.Legs:
                                        $ Line = get_clothing_name(RogueX.Legs_key, vin)
                                        $ RogueX.Legs = 0
                                        "Она снимает [Line] и надевает [get_clothing_name(RogueX.Panties_key, vin)]."
                                elif RogueX.Legs == "skirt":
                                        "Она достает [get_clothing_name(RogueX.Panties_key, vin)] и надевает их под юбку."
                                        $ RogueX.Legs = 0
                                        "Затем она сбрасывает юбку на пол."
                                else:
                                        $ Line = get_clothing_name(RogueX.Legs_key, vin)
                                        $ RogueX.Legs = 0
                                        "Она на мгновение отходит, а затем возвращается в [get_clothing_name(RogueX.Panties_key, pre)]."
                                return  #jump Rogue_Clothes
                        else:
                                ch_r "Не-а."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(RogueX, 1100, "LI", TabM=3) and RogueX.Love > RogueX.Inbt:
                                if not Player.Male:
                                    ch_r "Какая же ты бесстыжая. . . думаю, я могла бы устроить тебе такое представление. . ."
                                else:
                                    ch_r "Какой же ты бесстыжий. . . думаю, я могла бы устроить тебе такое представление. . ."
                        elif ApprovalCheck(RogueX, 750, "OI", TabM=3) and RogueX.Obed > RogueX.Inbt:
                                ch_r "Если ты этого хочешь."
                        elif ApprovalCheck(RogueX, 500, "I", TabM=3):
                                ch_r "Ооох, шалунишка."
                        elif ApprovalCheck(RogueX, 1400, TabM=3):
                                if not Player.Male:
                                    h_r "Ох, хорошо. Ты была хорошей девочкой."
                                else:
                                    h_r "Ох, хорошо. Ты был примерным мальчиком."
                        else:
                                $ RogueX.FaceChange("surprised")
                                $ RogueX.Brows = "angry"
                                if RogueX.Taboo:
                                    ch_r "Не здесь,[RogueX.Petname]!"
                                else:
                                    ch_r "Не когда ты рядом, [RogueX.Petname]!"
                                call expression RogueX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно.":
                ch_r "Ладно. . ."
                return 0
        return 1
        #End of Rogue Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu Rogue_Clothes_Under:
            "Верх":
                menu:
                    "Может, снимешь [get_clothing_name(RogueX.Chest_key, vin)]?" if RogueX.Chest:
                            $ RogueX.FaceChange("bemused", 1)
                            if RogueX.SeenChest and ApprovalCheck(RogueX, 1100, TabM=2):
                                ch_r "Конечно."
                            elif ApprovalCheck(RogueX, 1100, TabM=2):
                                if not Player.Male:
                                    ch_r "Ну, думаю, я не против, чтобы ты их увидела. . ."
                                else:
                                    ch_r "Ну, думаю, я не против, чтобы ты их увидел. . ."
                            elif RogueX.Over == "hoodie" and ApprovalCheck(RogueX, 500, TabM=2):
                                ch_r "Ну, думаю, они достаточно прикрыты. . ."
                            elif not RogueX.SeenChest and not ApprovalCheck(RogueX, 1100):
                                    call Display_DressScreen(RogueX)
                                    if not _return:
                                        if RogueX.Over == "pink top" and ApprovalCheck(RogueX, 950, TabM=2):
                                                ch_r "Я буду выглядеть довольно неприлично. . ."
                                        elif RogueX.Over == "mesh top":
                                                ch_r "Этот топ ничего толком не прикрывает!"
                                        elif not RogueX.Over:
                                                ch_r "Нужно соблюдать хоть какое-то приличие."
                                        else:
                                                ch_r "Я так не думаю, [RogueX.Petname]."
                                        return  #jump Rogue_Clothes
                            $ Line = get_clothing_name(RogueX.Chest_key, vin)
                            $ RogueX.Chest = 0
                            if RogueX.Over:
                                "Она залезает под [get_clothing_name(RogueX.Over_key, vin)], хватает и снимает [Line], а затем снимает кидает на пол."
                            else:
                                "Она снимает [Line] и бросает на пол."
                            if (not RogueX.Over or RogueX.Over == "mesh top") and not renpy.showing('DressScreen'):
                                call Girl_First_Topless(RogueX)

                    "Примерь черную майку." if RogueX.Chest != "tank":
                            $ RogueX.Chest = "tank"
                    "Мне нравится твоя майка на пуговицах." if RogueX.Chest != "buttoned tank":# and RogueX.Over != "mesh top":
                            $ RogueX.Chest = "buttoned tank"

                    "Мне нравится твой спортивный лифчик." if RogueX.Chest != "sports bra":
                            if (RogueX.SeenChest and ApprovalCheck(RogueX, 600)) or ApprovalCheck(RogueX, 900, TabM=2):
                                ch_r "Конечно."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "В нем я буду чувствовать себя слишком голой. . ."
                                    return  #jump Rogue_Clothes
                            $ RogueX.Chest = "sports bra"

                    "Мне нравится твой черный лифчик." if RogueX.Chest != "bra":
                            if (RogueX.SeenChest and ApprovalCheck(RogueX, 600)) or ApprovalCheck(RogueX, 1100, TabM=2):
                                ch_r "Конечно."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "Он слишком откровенный. . ."
                                    return  #jump Rogue_Clothes
                            $ RogueX.Chest = "bra"

                    "Мне нравится твой голубой топик." if RogueX.Chest != "tube top" and "halloween" in RogueX.History:
                            if (RogueX.SeenChest and ApprovalCheck(RogueX, 600)) or ApprovalCheck(RogueX, 900, TabM=2):
                                ch_r "Конечно."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "В нем я буду чувствовать себя слишком голой. . ."
                                    return  #jump Rogue_Clothes
                            $ RogueX.Chest = "tube top"

                    "Мне нравится твой кружевной лифчик." if "lace bra" in RogueX.Inventory and RogueX.Chest != "lace bra":
                            if (RogueX.SeenChest and ApprovalCheck(RogueX, 800)) or ApprovalCheck(RogueX, 1100, TabM=2):
                                ch_r "Конечно."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "В нем я буду чувствовать себя слишком голой. . ."
                                    return  #jump Rogue_Clothes
                            $ RogueX.Chest = "lace bra"

                    "Мне нравится твой лифчик бикини." if RogueX.Chest != "bikini top" and "bikini top" in RogueX.Inventory:
                            if bg_current == "bg pool":
                                ch_r "Конечно."
                            else:
                                    if RogueX.SeenChest or ApprovalCheck(RogueX, 1000, TabM=2):
                                        ch_r "Конечно."
                                    else:
                                        call Display_DressScreen(RogueX)
                                        if not _return:
                                            ch_r "Чувствую, он сейчас не к месту. . ."
                                            return  #jump Rogue_Clothes
                            $ RogueX.Chest = "bikini top"

                    "Неважно.":
                                pass
                jump Rogue_Clothes_Under


            "Варианты колготок и чулок":
                menu:
                    "Сними [get_clothing_name(RogueX.Hose_key, vin)]." if RogueX.Hose and RogueX.Hose != 'ripped tights' and RogueX.Hose != 'tights':
                            $ RogueX.Hose = 0
                    "Чулки дополнили бы твой образ." if RogueX.Hose != "stockings" and RogueX.Legs != "pants":
                            $ RogueX.Hose = "stockings"
                    "Колготки дополнили бы твой образ." if RogueX.Hose != "pantyhose" and RogueX.Legs != "pants":
                            $ RogueX.Hose = "pantyhose"
                    "Рваные колготки дополнили бы твой образ." if RogueX.Hose != "ripped pantyhose" and "ripped pantyhose" in RogueX.Inventory and RogueX.Legs != "pants":
                            $ RogueX.Hose = "ripped pantyhose"
                    "Чулки и пояс с подвязками дополнили бы твой образ." if RogueX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in RogueX.Inventory and RogueX.Legs != "pants":
                            $ RogueX.Hose = "stockings and garterbelt"
                    "Может, наденешь только пояс с подвязками?" if RogueX.Hose != "garterbelt" and "stockings and garterbelt" in RogueX.Inventory and RogueX.Legs != "pants":
                            $ RogueX.Hose = "garterbelt"
                    "Неважно.":
                            pass
                jump Rogue_Clothes_Under

            "Низ":
                menu:

                    "Ты должна снять [get_clothing_name(RogueX.Panties_key, vin)]. . ." if RogueX.Panties and RogueX.Panties != "shorts":
                            $ RogueX.FaceChange("bemused", 1)
                            if (RogueX.SeenPussy and ApprovalCheck(RogueX, 900)) and not RogueX.Taboo: # You've seen her pussy
                                if ApprovalCheck(RogueX, 850, "L", TabM=2):
                                    if not Player.Male:
                                        ch_r "Какая же ты бесстыжая. . ."
                                    else:
                                        ch_r "Какой же ты бесстыжий. . ."
                                elif ApprovalCheck(RogueX, 500, "O", TabM=2):
                                    ch_r "Ну ладно."
                                elif ApprovalCheck(RogueX, 350, "I", TabM=2):
                                    ch_r "Ооох, шалунишка."
                                else:
                                    ch_r "Ох, думаю, можно."
                            else:                       #You've never seen it
                                if ApprovalCheck(RogueX, 1100, "LI", TabM=2):
                                    if not Player.Male:
                                        ch_r "Какая же ты бесстыжая. . . думаю, я могла бы устроить тебе такое представление. . ."
                                    else:
                                        ch_r "Какой же ты бесстыжий. . . думаю, я могла бы устроить тебе такое представление. . ."
                                elif ApprovalCheck(RogueX, 750, "OI", TabM=2):
                                    ch_r "Если ты этого хочешь."
                                elif ApprovalCheck(RogueX, 500, "I", TabM=2):
                                    ch_r "Ооох, шалунишка."
                                elif ApprovalCheck(RogueX, 1400, TabM=3):
                                    if not Player.Male:
                                        ch_r "Ох, хорошо. Ты была хорошей девочкой."
                                    else:
                                        ch_r "Ох, хорошо. Ты был примерным мальчиком."
                                else:
                                    call Display_DressScreen(RogueX)
                                    if not _return:
                                        $ RogueX.FaceChange("surprised")
                                        $ RogueX.Brows = "angry"
                                        if RogueX.Taboo > 20:
                                            ch_r "Не на людях, [RogueX.Petname]!"
                                        else:
                                            ch_r "Не когда ты рядом, [RogueX.Petname]!"
                                        jump Rogue_Clothes
                            $ Line = get_clothing_name(RogueX.Panties_key, vin)
                            $ RogueX.Panties = 0
                            if not RogueX.Legs:
                                "Она снимает [Line], а затем бросает их на пол."
                                if not renpy.showing('DressScreen'):
                                        call Girl_First_Bottomless(RogueX)
                            elif ApprovalCheck(RogueX, 1200, TabM=4):
                                $ Trigger = RogueX.Legs
                                $ RogueX.Legs = 0
                                pause 0.5
                                $ RogueX.Legs = Trigger
                                "Она снимает [get_clothing_name(RogueX.Legs_key, vin)] и [Line], затем снова надевает [get_clothing_name(RogueX.Legs_key, vin)]."
                                $ Trigger = 1
                                call Girl_First_Bottomless(RogueX,1)
                            elif RogueX.Legs == "skirt":
                                "Она залезает под юбку и снимает [Line]."
                            else:
                                $ RogueX.Blush = 1
                                "Она на мгновение отходит, а затем возвращается."
                                $ RogueX.Blush = 0
                            $ Line = 0

                    "Почему бы тебе вместо этого не надеть зеленые трусики?" if RogueX.Panties and RogueX.Panties != "green panties":
                            if ApprovalCheck(RogueX, 1000, TabM=3):
                                ch_r "Ладно, конечно."
                                $ RogueX.Panties = "green panties"
                            elif RogueX.Panties == "shorts":
                                ch_r "Хех, нет, я считаю, мне не стоит этого делать."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "Спасибо, но я сама решаю, какие трусики надеть."
                                else:
                                        $ RogueX.Panties = "green panties"

                    "Почему бы тебе вместо этого не надеть черные трусики?" if RogueX.Panties and RogueX.Panties != "black panties":
                            if ApprovalCheck(RogueX, 1100, TabM=3):
                                ch_r "Конечно."
                                $ RogueX.Panties = "black panties"
                            elif RogueX.Panties == "shorts":
                                ch_r "Хех, нет, я считаю, мне не стоит этого делать."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                        ch_r "Это тебя не касается, [RogueX.Petname]."
                                else:
                                        $ RogueX.Panties = "black panties"

                    "Почему бы тебе вместо этого не надеть кружевные трусики?" if "lace panties" in RogueX.Inventory and RogueX.Panties and RogueX.Panties != "lace panties":
                            if ApprovalCheck(RogueX, 1200, TabM=3):
                                ch_r "Конечно."
                                $ RogueX.Panties = "lace panties"
                            elif RogueX.Panties == "shorts":
                                ch_r "Хех, нет, я считаю, мне не стоит этого делать."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                        ch_r "Это тебя не касается, [RogueX.Petname]."
                                else:
                                        $ RogueX.Panties = "lace panties"

                    "Мне нравятся твои трусики бикини." if RogueX.Panties != "bikini bottoms" and "bikini bottoms" in RogueX.Inventory:
                            if bg_current == "bg pool":
                                ch_r "Конечно."
                                $ RogueX.Panties = "bikini bottoms"
                            else:
                                if ApprovalCheck(RogueX, 1000, TabM=2):
                                    ch_r "Конечно."
                                    $ RogueX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(RogueX)
                                    if not _return:
                                            ch_r "Чувствую, они сейчас не к месту. . ."
                                    else:
                                            $ RogueX.Panties = "bikini bottoms"
                    "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not RogueX.Panties:
                            $ RogueX.FaceChange("bemused", 1)
                            if RogueX.Legs and (RogueX.Love+RogueX.Obed) <= (1.5 * RogueX.Inbt):
                                $ RogueX.Mouth = "smile"
                                ch_r "Нет, спасибо, [RogueX.Petname]."
                                menu:
                                    "Ну ладно.":
                                        jump Rogue_Clothes
                                    "Я настаиваю, надевай.":
                                        if (RogueX.Love+RogueX.Obed) <= RogueX.Inbt:
                                            $ RogueX.FaceChange("angry")
                                            ch_r "Тем хуже для тебя."
                                            jump Rogue_Clothes
                                        else:
                                            $ RogueX.FaceChange("sadside")
                                            ch_r "ЛАДНО."
                            menu:
                                extend ""
                                "Как насчет зеленых?":
                                    ch_r "Хорошо."
                                    $ RogueX.Panties = "green panties"
                                "Как насчет черных?":
                                    ch_r "Ладно."
                                    $ RogueX.Panties  = "black panties"
                                "Как насчет кружевных?" if "lace panties" in RogueX.Inventory:
                                    ch_r "Ладно."
                                    $ RogueX.Panties  = "lace panties"

                    "Неважно.":
                            pass
                jump Rogue_Clothes_Under
            "Неважно.":
                            return
    return
    #end loop
    #jump Rogue_Clothes
    #End of Rogue Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Rogue_Clothes_Misc:
        #Misc
        "Сухие волосы" if RogueX.Hair == "wet":
                ch_p "Тебе идут сухие волосы."
                if ApprovalCheck(RogueX, 600):
                        ch_r "Ладно."
                        $ RogueX.Hair = "evo"
                else:
                        ch_r "Мне больше нравятся увлажненные волосы."

        "Мокрые волосы" if RogueX.Hair != "wet":
                ch_p "Тебе стоит увлажнить волосы."
                if ApprovalCheck(RogueX, 800):
                        ch_r "Хмм?"
                        $ RogueX.Hair = "wet"
                        "Она отходит, но вскоре возвращается."
                        ch_r "Типа так?"
                else:
                        ch_r "Уверена, это не так."

        "Прическа для вечеринки" if RogueX.Hair != "cosplay" and "halloween" in RogueX.History:
                ch_p "Мне понравилась твоя прическа с вечеринки."
                if ApprovalCheck(RogueX, 600):
                        ch_r "Ох, ладно."
                        $ RogueX.Hair = "cosplay"
                else:
                        ch_r "Я не хочу менять прическу."
        "Обычная прическа" if RogueX.Hair == "cosplay":
                ch_p "Мне нравится твоя обычная прическа."
                if ApprovalCheck(RogueX, 600):
                        ch_r "Ох, ладно."
                        $ RogueX.Hair = "evo"
                else:
                        ch_r "Я не хочу менять прическу."

        "Отрасти волосы на лобке" if not RogueX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может, отрастишь?"
                call expression RogueX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in RogueX.Todo:
                        $ RogueX.FaceChange("bemused", 1)
                        ch_r "Да, я знаю, [RogueX.Petname]. Но они же не могут вырасти за ночь!"
                else:
                        $ RogueX.FaceChange("bemused", 1)
                        $ Approval = ApprovalCheck(RogueX, 1150, TabM=0)

                        if ApprovalCheck(RogueX, 850, "L", TabM=0) or (Approval and RogueX.Love > RogueX.Obed):
                            ch_r "Ну. . . если тебе так больше нравится. . ."
                        elif ApprovalCheck(RogueX, 500, "O", TabM=0) or (Approval and RogueX.Obed > RogueX.Inbt):
                            ch_r "Если ты этого хочешь."
                        elif ApprovalCheck(RogueX, 500, "I", TabM=0) or Approval:
                            if not Player.Male:
                                ch_r "Хех, обожаю, когда женщина знает, чего хочет, [RogueX.Petname]."
                            else:
                                ch_r "Хех, обожаю, когда мужчина знает, чего хочет, [RogueX.Petname]."
                        else:
                            $ RogueX.FaceChange("surprised")
                            $ RogueX.Brows = "angry"
                            ch_r "Я не понимаю, какое тебе до этого дело, [RogueX.Petname]."
                            return  #jump Rogue_Clothes
                        $ RogueX.Todo.append("pubes")
                        $ RogueX.PubeC = 6

        "Побрей лобок" if RogueX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression RogueX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ RogueX.FaceChange("bemused", 1)
                if "shave" in RogueX.Todo:
                        ch_r "Я знаю и я этим займусь. Если ты не в курсе, на это нужно время."
                else:
                        $ Approval = ApprovalCheck(RogueX, 1150, TabM=0)
                        if ApprovalCheck(RogueX, 850, "L", TabM=0) or (Approval and RogueX.Love > RogueX.Obed):
                            ch_r "Я буду следить за ним, если ты хочешь. . ."
                        elif ApprovalCheck(RogueX, 500, "O", TabM=0) or (Approval and RogueX.Obed > RogueX.Inbt):
                            ch_r "Хорошо, я все сделаю."
                        elif ApprovalCheck(RogueX, 500, "I", TabM=0) or Approval:
                            ch_r "Надеюсь, ты это оценишь, [RogueX.Petname]."
                        else:
                            $ RogueX.FaceChange("surprised")
                            $ RogueX.Brows = "angry"
                            ch_r "Я не понимаю, какое тебе до этого дело, [RogueX.Petname]."
                            return  #jump Rogue_Clothes
                        $ RogueX.Todo.append("shave")
        "Пирсинг [[Сначала посмотрите, как она выглядит без него] (locked)" if not RogueX.SeenPussy and not RogueX.SeenChest:
                        pass

        "Надеть пирсинг-кольца" if RogueX.Pierce != "ring" and (RogueX.SeenPussy or RogueX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсингом-кольцами."
                if "ring" in RogueX.Todo:
                    ch_r "Ага, я помню."
                else:
                    $ RogueX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(RogueX, 1350, TabM=0)
                    if ApprovalCheck(RogueX, 950, "L", TabM=0) or (Approval and RogueX.Love > RogueX.Obed):
                        ch_r "Тебе он правда нравится? Ну ладно. . ."
                    elif ApprovalCheck(RogueX, 600, "O", TabM=0) or (Approval and RogueX.Obed > RogueX.Inbt):
                        ch_r "Ладно, тогда я позабочусь об этом."
                    elif ApprovalCheck(RogueX, 600, "I", TabM=0) or Approval:
                        ch_r "Мне тоже, вроде как, нравится, как он выглядит. . ."
                    else:
                        $ RogueX.FaceChange("surprised")
                        $ RogueX.Brows = "angry"
                        ch_r "Я не понимаю, какое тебе до этого дело, [RogueX.Petname]."
                        return  #jump Rogue_Clothes
                    $ RogueX.Todo.append("ring")

        "Надеть пирсинг-штанги" if RogueX.Pierce != "barbell" and (RogueX.SeenPussy or RogueX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in RogueX.Todo:
                    ch_r "Ага, я помню."
                else:
                    $ RogueX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(RogueX, 1350, TabM=0)
                    if ApprovalCheck(RogueX, 900, "L", TabM=0) or (Approval and RogueX.Love > RogueX.Obed):
                        ch_r "Тебе он правда нравится? Ну ладно. . ."
                    elif ApprovalCheck(RogueX, 600, "O", TabM=0) or (Approval and RogueX.Obed > RogueX.Inbt):
                        ch_r "Ладно, тогда я позабочусь об этом."
                    elif ApprovalCheck(RogueX, 600, "I", TabM=0) or Approval:
                        ch_r "Мне тоже, вроде как, нравится, как он выглядит. . ."
                    else:
                        $ RogueX.FaceChange("surprised")
                        $ RogueX.Brows = "angry"
                        ch_r "Я не понимаю, какое тебе до этого дело, [RogueX.Petname]."
                        return  #jump Rogue_Clothes
                    $ RogueX.Todo.append("barbell")

        "Сними пирсинг" if RogueX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ RogueX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(RogueX, 1350, TabM=0)
                if ApprovalCheck(RogueX, 950, "L", TabM=0) or (Approval and RogueX.Love > RogueX.Obed):
                    ch_r "Ты правда так думаешь? Тогда я могу его снять. . ."
                elif ApprovalCheck(RogueX, 600, "O", TabM=0) or (Approval and RogueX.Obed > RogueX.Inbt):
                    ch_r "Тогда я его сниму."
                elif ApprovalCheck(RogueX, 600, "I", TabM=0) or Approval:
                    ch_r "Ну, мне вообщем-то тоже больше нравилось ходить без пирсинга. . ."
                else:
                    $ RogueX.FaceChange("surprised")
                    $ RogueX.Brows = "angry"
                    ch_r "Если не возражаешь, то я бы предпочла его оставить."
                    return  #jump Rogue_Clothes
                $ RogueX.Pierce = 0

        "Надень шипованный ошейник" if RogueX.Neck != "spiked collar":
                        $ RogueX.Neck = "spiked collar"
        "Сними шипованный ошейник" if RogueX.Neck == "spiked collar":
                        $ RogueX.Neck = 0

        "Надень перчатки" if not RogueX.Arms:
                        $ RogueX.Arms = "gloves"
        "Сними перчатки" if RogueX.Arms:
                        $ RogueX.Arms = 0

        "Неважно.":
                pass
    return
    #jump Rogue_Clothes
    #End of Rogue Misc Wardrobe

return

#End Rogue Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
