# star Jubes chat interface
#Jubes Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Jubes_Relationship: #rkeljsvg
    while True:
        menu:
            ch_v "О чем ты хочешь поговорить?"
            "Хочешь стать моей девушкой?" if JubesX not in Player.Harem and "ex" not in JubesX.Traits:
                    $ JubesX.DailyActions.append("relationship")
                    if "asked boyfriend" in JubesX.DailyActions and "angry" in JubesX.DailyActions:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Как я уже сказала, мне это не интересно."
                            return
                    elif "asked boyfriend" in JubesX.DailyActions:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Все еще нет."
                            return
                    elif JubesX.Break[0]:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Я не хочу быть с тобой."
                            if Player.Harem:
                                    $ JubesX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "Все уже изменилось. . ."

                    $ JubesX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "JubesYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_v "Нууу, сначала тебе нужно посоветоваться с остальными, [JubesX.Petname]."
                        else:
                            ch_v "Нууу, сначала тебе нужно посоветоваться с [Player.Harem[0].Name_tvo], [JubesX.Petname]."
                        return

                    if JubesX.Event[5]:
                            $ JubesX.FaceChange("bemused", 1)
                            if not Player.Male:
                                ch_v "Ты сама отвергла меня. . ."
                            else:
                                ch_v "Ты сам отверг меня. . ."
                    else:
                            $ JubesX.FaceChange("surprised", 2)
                            ch_v "Что? . ."
                            $ JubesX.FaceChange("smile", 1)

                    call Jubes_OtherWoman

                    if JubesX.Love >= 800:
                            $ JubesX.FaceChange("surprised", 1)
                            $ JubesX.Mouth = "smile"
                            if not JubesX.Event[5]:
                                    $ JubesX.Statup("Love", 200, 10)
                                    call Jubes_BF
                                    return
                            $ JubesX.Statup("Love", 200, 40)
                            ch_v "Конечно!"
                            if "boyfriend" not in JubesX.Petnames:
                                    $ JubesX.Petnames.append("boyfriend")
                            if "JubesYes" in Player.Traits:
                                    $ Player.Traits.remove("JubesYes")
                            $ Player.Harem.append(JubesX)
                            call Harem_Initiation
                            "[JubesX.Name] хватает вас и крепко целует."
                            $ JubesX.FaceChange("kiss", 1)
                            $ JubesX.Kissed += 1
                    elif JubesX.Obed >= 500:
                            $ JubesX.FaceChange("perplexed")
                            ch_v "Не уверена, хочу ли я -встречаться- с тобой. . ."
                    elif JubesX.Inbt >= 500:
                            $ JubesX.FaceChange("smile")
                            ch_v "Ты знаешь, что я просто хочу поразвлечься?"
                    else:
                            $ JubesX.FaceChange("perplexed", 1)
                            ch_v "Воу, сбавь обороты, [JubesX.Petname]."

            "Может, начнем все сначала?" if "ex" in JubesX.Traits:
                    $ JubesX.DailyActions.append("relationship")
                    if "asked boyfriend" in JubesX.DailyActions and "angry" in JubesX.DailyActions:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Я же сказала тебе, что мне неинтересно."
                            return
                    elif "asked boyfriend" in JubesX.DailyActions:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Не-а."
                            return

                    $ JubesX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "JubesYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_v "Нууу, сначала тебе нужно посоветоваться с остальными, [JubesX.Petname]."
                            else:
                                ch_v "Нууу, сначала тебе нужно посоветоваться с [Player.Harem[0].Name_tvo], [JubesX.Petname]."
                            return

                    $ Cnt = 0
                    call Jubes_OtherWoman

                    if JubesX.Love >= 800:
                            $ JubesX.FaceChange("surprised", 1)
                            $ JubesX.Mouth = "smile"
                            $ JubesX.Statup("Love", 90, 5)
                            ch_v "Ну ладно, попробовать можно."
                            if "boyfriend" not in JubesX.Petnames:
                                        $ JubesX.Petnames.append("boyfriend")
                            $ JubesX.Traits.remove("ex")
                            if "JubesYes" in Player.Traits:
                                    $ Player.Traits.remove("JubesYes")
                            $ Player.Harem.append(JubesX)
                            call Harem_Initiation
                            "[JubesX.Name] притягивает вас к себе и крепко целует."
                            $ JubesX.FaceChange("kiss", 1)
                            $ JubesX.Kissed += 1
                    elif JubesX.Love >= 600 and ApprovalCheck(JubesX, 1500):
                            $ JubesX.FaceChange("smile", 1)
                            $ JubesX.Statup("Love", 90, 5)
                            ch_v "Конечно, думаю, мы можем попробовать."
                            if "boyfriend" not in JubesX.Petnames:
                                $ JubesX.Petnames.append("boyfriend")
                            $ JubesX.Traits.remove("ex")
                            if "JubesYes" in Player.Traits:
                                    $ Player.Traits.remove("JubesYes")
                            $ Player.Harem.append(JubesX)
                            call Harem_Initiation
                            $ JubesX.FaceChange("kiss", 1)
                            "[JubesX.Name] дарит вам легкий поцелуй."
                            $ JubesX.FaceChange("sly", 1)
                            $ JubesX.Kissed += 1
                    elif JubesX.Obed >= 500:
                            $ JubesX.FaceChange("sad")
                            ch_v "Нет, из этого не выйдет ничего хорошего."
                    elif JubesX.Inbt >= 500:
                            $ JubesX.FaceChange("perplexed")
                            ch_v "Нет, давай просто оставим все как есть."
                    else:
                            $ JubesX.FaceChange("perplexed", 1)
                            if not Player.Male:
                                ch_v "Не-а, ты упустила свой шанс."
                            else:
                                ch_v "Не-а, ты упустил свой шанс."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if JubesX in Player.Harem:
                            call AskDateOther

            "Думаю, мы должны расстаться." if JubesX in Player.Harem:
                            if "breakup talk" in JubesX.DailyActions:
                                    if not Player.Male:
                                        ch_v "Ты что, головой ударилась?"
                                    else:
                                        ch_v "Ты что, головой ударился?"
                            else:
                                    call Breakup(JubesX)

            "О разговоре, который у нас был ранее. . .":
                menu:
                    "Помнишь, ты как-то признавалась мне в любви. . ?" if "lover" not in JubesX.Traits and JubesX.Event[6] >= 20 and JubesX.Event[6] != 23:
                            call Jubes_Love_Redux

                    "Помнишь, ты как-то рассказывала мне о себе. . ?" if "lover" not in JubesX.Traits and JubesX.Event[6] == 23:
                            call Jubes_Love_Redux

                    "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировала?" if "sir" not in JubesX.Petnames and "sir" in JubesX.History and not Player.Male:
                            if "asked sub" in JubesX.DailyActions:
                                    ch_v "Мы должны оставить подобные разговоры на сегодня. . ."
                            else:
                                    call Jubes_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировал?" if "sir" not in JubesX.Petnames and "sir" in JubesX.History and Player.Male:
                            if "asked sub" in JubesX.DailyActions:
                                    ch_v "Мы должны оставить подобные разговоры на сегодня. . ."
                            else:
                                    call Jubes_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоей хозяйкой?" if "master" not in JubesX.Petnames and "master" in JubesX.History and not Player.Male:
                            if "asked sub" in JubesX.DailyActions:
                                    ch_v "Мы должны оставить подобные разговоры на сегодня. . ."
                            else:
                                    call Jubes_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я стал твоим хозяином?" if "master" not in JubesX.Petnames and "master" in JubesX.History and Player.Male:
                            if "asked sub" in JubesX.DailyActions:
                                    ch_v "Мы должны оставить подобные разговоры на сегодня. . ."
                            else:
                                    call Jubes_Sub_Asked
                    "Неважно":
                            pass

            "Неважно":
                return

    return

label Jubes_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((JubesX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ JubesX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_v "Ты ведь с [Player.Harem[0].Name_tvo], так? И с кучей других!"
    else:
        ch_v "Ты ведь с [Player.Harem[0].Name_tvo], так?"
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "JubesYes" in Player.Traits:
                if ApprovalCheck(JubesX, 1800, Bonus = Cnt):
                    $ JubesX.FaceChange("smile", 1)
                    if JubesX.Love >= JubesX.Obed:
                            ch_v "Нууу, думаю, я смогу с этим смириться."
                    elif JubesX.Obed >= JubesX.Inbt:
                            ch_v "Хорошо, тогда я могу принять твое предложение."
                    else:
                            ch_v "Классно."
                else:
                    $ JubesX.FaceChange("angry", 1)
                    ch_v "Ага, хорошо, но мне это не нравится."
                    $ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "JubesYes" not in Player.Traits and not Player.Male:
                if ApprovalCheck(JubesX, 1800, Bonus = Cnt):
                        $ JubesX.FaceChange("smile", 1)
                        if JubesX.Love >= JubesX.Obed:
                            ch_v "Нууу, если она не против, я бы с этим смирилась."
                        elif JubesX.Obed >= JubesX.Inbt:
                            ch_v "Хорошо, в этом случае я могла бы принять твое предложение."
                        else:
                            ch_v "Классно."
                        ch_v "Хорошо, спроси ее и дай мне знать."
                else:
                        $ JubesX.FaceChange("angry", 1)
                        ch_v "Ага, хорошо, но мне это не нравится."
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "JubesYes" not in Player.Traits and Player.Male:
                if ApprovalCheck(JubesX, 1800, Bonus = Cnt):
                        $ JubesX.FaceChange("smile", 1)
                        if JubesX.Love >= JubesX.Obed:
                            ch_v "Нууу, если она не против, я бы с этим смирилась."
                        elif JubesX.Obed >= JubesX.Inbt:
                            ch_v "Хорошо, в этом случае я могла бы принять твое предложение."
                        else:
                            ch_v "Классно."
                        ch_v "Хорошо, спроси ее и дай мне знать."
                else:
                        $ JubesX.FaceChange("angry", 1)
                        ch_v "Ага, хорошо, но мне это не нравится."
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
                if not ApprovalCheck(JubesX, 1800, Bonus = -Cnt): #checks if Jubes likes you more than the other girl
                        $ JubesX.FaceChange("angry", 1)
                        if not ApprovalCheck(JubesX, 1800):
                                ch_v "Нуу, меня такое не устраивает."
                        else:
                                ch_v "Звучит стремно."
                        $ renpy.pop_call()
                else:
                        $ JubesX.FaceChange("smile", 1)
                        if JubesX.Love >= JubesX.Obed:
                                ch_v "Думаю, я могла бы согласиться на такое. . ."
                        elif JubesX.Obed >= JubesX.Inbt:
                                ch_v "Хорошо, в этом случае я могла бы принять твое предложение."
                        else:
                                ch_v "Классно."
                        $ JubesX.Traits.append("downlow")

        "Я могу порвать с ней.":
                    $ JubesX.FaceChange("sad")
                    ch_v "Сделай это и возвращайся ко мне."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ JubesX.FaceChange("sad")
                    ch_v "Думаешь?"
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ JubesX.FaceChange("sad")
                    ch_v "Думаешь?"
                    $ renpy.pop_call()

    return


label Jubes_About(Check=0): #rkeljsvg
    if Check not in TotalGirls:
            ch_v "Это кто?"
            return
    ch_v "Что я думаю о ней? Нууу. . ."
    if Check == RogueX:
            if "poly Rogue" in JubesX.Traits:
                ch_v "Нууу, с ней весело в постели. . ."
            elif JubesX.LikeRogue >= 900:
                ch_v "У нее клевая попка. . ."
            elif JubesX.LikeRogue >= 800:
                ch_v "Она. . .  клевая. . .  очень клевая. . ."
            elif JubesX.LikeRogue >= 700:
                ch_v "Мне нравится общаться с ней."
            elif JubesX.LikeRogue >= 600:
                ch_v "Она клевая."
            elif JubesX.LikeRogue >= 500:
                ch_v "Думаю, я пару раз ее где-то видела."
            elif JubesX.LikeRogue >= 400:
                ch_v "Тьфу, не заставляй меня вспоминать о ней."
            elif JubesX.LikeRogue >= 300:
                ch_v "Она меня бесит!"
            else:
                ch_v "Она сука."
    elif Check == KittyX:
            if "poly Kitty" in JubesX.Traits:
                ch_v "Нууу, с ней весело в постели. . ."
            elif JubesX.LikeKitty >= 900:
                ch_v "Она очень. . . веселая. . ."
            elif JubesX.LikeKitty >= 800:
                ch_v "Она в хорошей форме. . ."
            elif JubesX.LikeKitty >= 700:
                ch_v "Она довольно гибкая. . ."
            elif JubesX.LikeKitty >= 600:
                ch_v "Она клевая."
            elif JubesX.LikeKitty >= 500:
                ch_v "Думаю, я пару раз ее где-то видела."
            elif JubesX.LikeKitty >= 400:
                ch_v "Тьфу, не заставляй меня вспоминать о ней."
            elif JubesX.LikeKitty >= 300:
                ch_v "Она такая плакса!"
            else:
                ch_v "Она сука."
    elif Check == EmmaX:
            if "poly Emma" in JubesX.Traits:
                ch_v "Нууу, с ней весело в постели. . ."
            elif JubesX.LikeEmma >= 900:
                ch_v "У нее такие классные сиськи!"
            elif JubesX.LikeEmma >= 800:
                ch_v "У нее такие формы. . ."
            elif JubesX.LikeEmma >= 700:
                ch_v "Она классный преподаватель. . ."
            elif JubesX.LikeEmma >= 600:
                ch_v "Она нормальная. . ."
            elif JubesX.LikeEmma >= 500:
                ch_v "Ничего не имею против нее."
            elif JubesX.LikeEmma >= 400:
                ch_v "Ты про эту занозу в заднице, да?"
            elif JubesX.LikeEmma >= 300:
                ch_v "У меня от нее голова болит."
            else:
                ch_v "Она настоящая ведьма."
    elif Check == LauraX:
            if "poly Laura" in JubesX.Traits:
                ch_v "Нууу, с ней весело в постели. . ."
            elif JubesX.LikeLaura >= 900:
                ch_v "Она такая шалунья!"
            elif JubesX.LikeLaura >= 800:
                ch_v "От нее пахнет опасностью. . ."
            elif JubesX.LikeLaura >= 700:
                ch_v "Она крепкий орешек."
            elif JubesX.LikeLaura >= 600:
                ch_v "С ней очень весело."
            elif JubesX.LikeLaura >= 500:
                ch_v "Она нормальная."
            elif JubesX.LikeLaura >= 400:
                ch_v "Иногда она бесит."
            elif JubesX.LikeLaura >= 300:
                ch_v "Ей не нужно совать нос в чужие дела."
            else:
                ch_v "Грррр."
    elif Check == JeanX:
            if "poly Jean" in JubesX.Traits:
                ch_v "Нууу, с ней весело в постели. . ."
            elif JubesX.LikeJean >= 900:
                ch_v "Она очень сексуальная. . ."
            elif JubesX.LikeJean >= 800:
                ch_v "Она неплохо выглядит. . ."
            elif JubesX.LikeJean >= 700:
                ch_v "Она. . . сносная."
            elif JubesX.LikeJean >= 600:
                ch_v "Думаю, она нормальная?"
            elif JubesX.LikeJean >= 500:
                ch_v "Она, вроде как, доставучая."
            elif JubesX.LikeJean >= 400:
                ch_v "Ей нужно завязывать с промывкой мозгов."
            elif JubesX.LikeJean >= 300:
                ch_v "Ненавижу ее."
            else:
                ch_v "Она сука."
    elif Check == StormX:
            if "poly Storm" in JubesX.Traits:
                ch_v "Нууу, с ней весело в постели. . ."
            elif JubesX.LikeStorm >= 900:
                ch_v "Она хороша, правда?"
            elif JubesX.LikeStorm >= 800:
                ch_v "Она такая красивая. . ."
            elif JubesX.LikeStorm >= 700:
                ch_v "Она заботится о том, чтобы я выполняла домашнюю работу."
            elif JubesX.LikeStorm >= 600:
                ch_v "Она - отличный препод."
            elif JubesX.LikeStorm >= 500:
                ch_v "Она клевая."
            elif JubesX.LikeStorm >= 400:
                ch_v "Она может быть злой."
            elif JubesX.LikeStorm >= 300:
                ch_v "Ей не нужно совать нос в мои дела."
            else:
                ch_v "Она настоящая ведьма."
    elif Check == GwenX:
            if "poly Gwen" in JubesX.Traits:
                ch_v "Нууу, с ней весело в постели. . ."
            elif JubesX.LikeGwen >= 900:
                ch_v "Она такая. . . игривая. . ."
            elif JubesX.LikeGwen >= 800:
                ch_v "Она милая. . ."
            elif JubesX.LikeGwen >= 700:
                ch_v "Она забавная. . ."
            elif JubesX.LikeGwen >= 600:
                ch_v "Она клевая."
            elif JubesX.LikeGwen >= 500:
                ch_v "Думаю, я пару раз ее где-то видела."
            elif JubesX.LikeGwen >= 400:
                ch_v "Тьфу, не заставляй меня вспоминать о ней."
            elif JubesX.LikeGwen >= 300:
                ch_v "Она такая странная!"
            else:
                ch_v "Она сука."
    elif Check == BetsyX:
            if "poly Betsy" in JubesX.Traits:
                ch_v "Нууу, с ней весело в постели. . ."
            elif JubesX.LikeBetsy >= 900:
                ch_v "Она очень. . . необычная. . ."
            elif JubesX.LikeBetsy >= 800:
                ch_v "У нее \"хорошая форма\". . ."
            elif JubesX.LikeBetsy >= 700:
                ch_v "Она довольна сексуальна. . ."
            elif JubesX.LikeBetsy >= 600:
                ch_v "Она клевая."
            elif JubesX.LikeBetsy >= 500:
                ch_v "Мне кажется, я где-то видела."
            elif JubesX.LikeBetsy >= 400:
                ch_v "Пфф, не заставляй меня про нее вспоминать."
            elif JubesX.LikeBetsy >= 300:
                ch_v "Она та еще плакса!"
            else:
                ch_v "Она сука."
    elif Check == DoreenX:
            if "poly Doreen" in JubesX.Traits:
                ch_v "Нууу, с ней весело в постели. . ."
            elif JubesX.LikeDoreen >= 900:
                ch_v "Она такая. . . жизнерадостная. . ."
            elif JubesX.LikeDoreen >= 800:
                ch_v "Она милая. . ."
            elif JubesX.LikeDoreen >= 700:
                ch_v "Она веселая. . ."
            elif JubesX.LikeDoreen >= 600:
                ch_v "Она клевая."
            elif JubesX.LikeDoreen >= 500:
                ch_v "Мне кажется, я где-то видела."
            elif JubesX.LikeDoreen >= 400:
                ch_v "Пфф, не заставляй меня про нее вспоминать."
            elif JubesX.LikeDoreen >= 300:
                ch_v "Она такая странная!"
            else:
                ch_v "Она сука."
    elif Check == WandaX:
            if "poly Wanda" in JubesX.Traits:
                ch_v "Ну, в постели с ней весело. . ."
            elif JubesX.LikeWanda >= 900:
                ch_v "У нее великолепное тело. . ."
            elif JubesX.LikeWanda >= 800:
                ch_v "Она. . . клевая. . . очень клевая. . ."
            elif JubesX.LikeWanda >= 700:
                ch_v "Мне нравится общаться с ней."
            elif JubesX.LikeWanda >= 600:
                ch_v "Она клевая."
            elif JubesX.LikeWanda >= 500:
                ch_v "Мне кажется, я пару раз с ней пересекалась."
            elif JubesX.LikeWanda >= 400:
                ch_v "Пфф, не заставляй меня про нее вспоминать."
            elif JubesX.LikeWanda >= 300:
                ch_v "Она ужасно раздражает!"
            else:
                ch_v "Она ведьма."
    else:
                ch_v "Я даже не знаю."
    return
#End Jubes_AboutEmma

label Jubes_Monogamy:
        #called from Jubes_Settings to ask her not to hook up with other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in JubesX.Traits:
                    if JubesX.Thirst >= 60 and not ApprovalCheck(JubesX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ JubesX.FaceChange("sly",1)
                            if "mono" not in JubesX.DailyActions:
                                    $ JubesX.Statup("Obed", 90, -2)
                            ch_v "Я могла бы, но как мне тогда развлекаться?"
                            return
                    elif ApprovalCheck(JubesX, 1200, "LO", TabM=0) and JubesX.Love >= JubesX.Obed:
                            #she cares
                            $ JubesX.FaceChange("sly",1)
                            if "mono" not in JubesX.DailyActions:
                                    $ JubesX.Statup("Love", 90, 1)
                            ch_v "Ох. . . хочешь оставить меня для себя?."
                            ch_v "Хорошо, я буду осторожнее. . ."
                    elif ApprovalCheck(JubesX, 700, "O", TabM=0):
                            #she is obedient
                            $ JubesX.FaceChange("sly",1,Eyes="side")
                            ch_v "Конечно."
                    else:
                            #she doesn't care
                            $ JubesX.FaceChange("sly",1)
                            ch_v "Неее."
                            return
                    if "mono" not in JubesX.DailyActions:
                            $ JubesX.Statup("Obed", 90, 3)
                    $ JubesX.AddWord(1,0,"mono") #Daily
                    $ JubesX.Traits.append("mono")
            "Не встречайся с другими девушками." if "mono" not in JubesX.Traits:
                    if ApprovalCheck(JubesX, 900, "O", TabM=0):
                            #she is obedient
                            $ JubesX.FaceChange("sly",1,Eyes="side")
                            ch_v "Хорошо."
                    elif JubesX.Thirst >= 60 and not ApprovalCheck(JubesX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ JubesX.FaceChange("sly",1)
                            if "mono" not in JubesX.DailyActions:
                                    $ JubesX.Statup("Obed", 90, -2)
                            ch_v "Я могла бы, но как мне тогда развлекаться?"
                            return
                    elif ApprovalCheck(JubesX, 600, "O", TabM=0):
                            #she is obedient
                            $ JubesX.FaceChange("sly",1,Eyes="side")
                            ch_v "Если ты настаиваешь."
                    elif ApprovalCheck(JubesX, 1400, "LO", TabM=0):
                            #she cares
                            $ JubesX.FaceChange("sly",1)
                            ch_v "Ага, хорошо, но в следующий раз проси вежливо."
                    else:
                            #she doesn't care
                            $ JubesX.FaceChange("sly",1,Brows="confused")
                            ch_v "Неее."
                            return
                    if "mono" not in JubesX.DailyActions:
                            $ JubesX.Statup("Obed", 90, 3)
                    $ JubesX.AddWord(1,0,"mono") #Daily
                    $ JubesX.Traits.append("mono")
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in JubesX.Traits:
                    if ApprovalCheck(JubesX, 700, "O", TabM=0):
                            $ JubesX.FaceChange("sly",1,Eyes="side")
                            ch_v "Клево, клево."
                    elif ApprovalCheck(JubesX, 800, "L", TabM=0):
                            $ JubesX.FaceChange("sly",1)
                            if not Player.Male:
                                ch_v "Хорошо, но ты будешь мне должна. . ."
                            else:
                                ch_v "Хорошо, но ты будешь мне должен. . ."
                    else:
                            $ JubesX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in JubesX.DailyActions:
                                    $ JubesX.Statup("Love", 90, -2)
                            ch_v "Хорошо. . ."
                    if "mono" not in JubesX.DailyActions:
                            $ JubesX.Statup("Obed", 90, 3)
                    if "mono" in JubesX.Traits:
                            $ JubesX.Traits.remove("mono")
                    $ JubesX.AddWord(1,0,"mono") #Daily
            "Неважно.":
                pass
        return

# end Jubes monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Jubes_Jumped:
        #called from Jubes_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ JubesX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_v "Да?"
            "На будущее, можешь сначала спрашивать?" if "chill" not in JubesX.Traits:
                    if JubesX.Thirst >= 60 and not ApprovalCheck(JubesX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ JubesX.FaceChange("sly",1)
                            if "chill" not in JubesX.DailyActions:
                                    $ JubesX.Statup("Obed", 90, -2)
                            ch_v "Нууу, ты гораздо лучше, чем пакеты с кровью. . ."
                            return
                    elif ApprovalCheck(JubesX, 1000, "LO", TabM=0) and JubesX.Love >= JubesX.Obed:
                            #she cares
                            $ JubesX.FaceChange("surprised",1)
                            if "chill" not in JubesX.DailyActions:
                                    $ JubesX.Statup("Love", 90, 1)
                            ch_v "Извини, мне. . .  это было нужно. . ."
                            $ JubesX.FaceChange("sly",1,Eyes="side")
                            ch_v "Я исправлюсь. . ."
                    elif ApprovalCheck(JubesX, 500, "O", TabM=0):
                            #she is obedient
                            $ JubesX.FaceChange("sly",1,Eyes="side")
                            ch_v "Извини. . ."
                    else:
                            #she doesn't care
                            $ JubesX.FaceChange("sly",1)
                            ch_v "Посмотрим. . ."
                            return
                    if "chill" not in JubesX.DailyActions:
                            $ JubesX.Statup("Obed", 90, 3)
                    $ JubesX.AddWord(1,0,"chill") #Daily
                    $ JubesX.Traits.append("chill")
            "Больше так не делай." if "chill" not in JubesX.Traits:
                    if ApprovalCheck(JubesX, 800, "O", TabM=0):
                            #she is obedient
                            $ JubesX.FaceChange("sly",1,Eyes="side")
                            ch_v "Хорошо."
                    elif JubesX.Thirst >= 60 and not ApprovalCheck(JubesX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ JubesX.FaceChange("sly",1)
                            if "chill" not in JubesX.DailyActions:
                                    $ JubesX.Statup("Obed", 90, -2)
                            ch_v "Извини, мне. . .  это было нужно. . ."
                            return
                    elif ApprovalCheck(JubesX, 400, "O", TabM=0):
                            #she is obedient
                            $ JubesX.FaceChange("sly",1,Eyes="side")
                            ch_v "Конечно. . ."
                    elif ApprovalCheck(JubesX, 500, "LO", TabM=0) and not ApprovalCheck(JubesX, 500, "I", TabM=0):
                            #she cares
                            $ JubesX.FaceChange("sly",1)
                            ch_v "Эй, аккуратнее с такими просьбами."
                            ch_v "Но попробовать я могу. . ."
                    else:
                            #she doesn't care
                            $ JubesX.FaceChange("sly",1)
                            ch_v "Посмотрим. . ."
                            return
                    if "chill" not in JubesX.DailyActions:
                            $ JubesX.Statup("Obed", 90, 3)
                    $ JubesX.AddWord(1,0,"chill") #Daily
                    $ JubesX.Traits.append("chill")
            "Делай что хочешь.":
                    if ApprovalCheck(JubesX, 800, "L", TabM=0):
                            $ JubesX.FaceChange("sly",1)
                            ch_v "Игры продолжаются. . ."
                    elif ApprovalCheck(JubesX, 700, "O", TabM=0):
                            $ JubesX.FaceChange("sly",1,Eyes="side")
                            ch_v "Поняла!"
                    else:
                            $ JubesX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in JubesX.DailyActions:
                                    $ JubesX.Statup("Love", 90, -2)
                            ch_v "Ага, посмотрим. . ."
                    if "chill" not in JubesX.DailyActions:
                            $ JubesX.Statup("Obed", 90, 3)
                    if "chill" in JubesX.Traits:
                            $ JubesX.Traits.remove("chill")
                    $ JubesX.AddWord(1,0,"chill") #Daily
            "Эм, неважно.":
                pass
        return

# end Jubes jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start jubilee hungry //////////////////////////////////////////////////////////
label Jubes_Hungry:
    if JubesX.Chat[3]:
        ch_v "[[облизывает губы] Что-то выпить захотелось. . ."
    elif JubesX.Chat[2]:
        ch_v "Мне очень нравится твоя сыворотка."
    else:
        ch_v "[[облизывает губы] Что-то выпить захотелось. . ."
    $ JubesX.Traits.append("hungry")
return


# end jubilee hungry //////////////////////////////////////////////////////////

# Jubes Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Jubes_SexChat:
    $ Line = "Ага, о чем ты хочешь поговорить?" if not Line else Line
    while True:
            menu:
                ch_v "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in JubesX.DailyActions:
                        ch_v "Я помню."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ JubesX.FaceChange("sly")
                                        if JubesX.PlayerFav == "sex":
                                            $ JubesX.Statup("Lust", 80, 5)
                                            ch_v "Ага, я это знаю. . ."
                                        elif JubesX.Favorite == "sex":
                                            $ JubesX.Statup("Love", 90, 5)
                                            $ JubesX.Statup("Lust", 80, 10)
                                            ch_v "Мне тоже это очень нравится!"
                                        elif JubesX.Sex >= 5:
                                            ch_v "Нууу, я не против."
                                        elif not JubesX.Sex:
                                            $ JubesX.FaceChange("perplexed")
                                            ch_v "Кто тебя трахает?"
                                        else:
                                            $ JubesX.FaceChange("bemused")
                                            ch_v "Хех, эм, ага, это мило. . ."
                                        $ JubesX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ JubesX.FaceChange("sly")
                                        if JubesX.PlayerFav == "anal":
                                            $ JubesX.Statup("Lust", 80, 5)
                                            if not Player.Male:
                                                ch_v "Ты уже говорила. . ."
                                            else:
                                                ch_v "Ты уже говорил. . ."
                                        elif JubesX.Favorite == "anal":
                                            $ JubesX.Statup("Love", 90, 5)
                                            $ JubesX.Statup("Lust", 80, 10)
                                            ch_v "Мне тоже это нравится!"
                                        elif JubesX.Anal >= 10:
                                            ch_v "Ага, это. . . приятно. . ."
                                        elif not JubesX.Anal:
                                            $ JubesX.FaceChange("perplexed")
                                            ch_v "Кто тебя трахает?"
                                        else:
                                            $ JubesX.FaceChange("bemused",Eyes="side")
                                            ch_v "Хех, ага, эм, ладно. . ."
                                        $ JubesX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ JubesX.FaceChange("sly")
                                        if JubesX.PlayerFav == "blow":
                                            $ JubesX.Statup("Lust", 80, 3)
                                            ch_v "Разумеется."
                                        elif JubesX.Favorite == "blow":
                                            $ JubesX.Statup("Love", 90, 5)
                                            $ JubesX.Statup("Lust", 80, 5)
                                            ch_v "Мне тоже!"
                                        elif JubesX.Blow >= 10:
                                            ch_v "Ага, ты очень вкусный."
                                        elif not JubesX.Blow:
                                            $ JubesX.FaceChange("perplexed")
                                            ch_v "Кто сосет твой член?!"
                                        else:
                                            $ JubesX.FaceChange("bemused")
                                            ch_v "Я. . . это хорошо. . ."
                                        $ JubesX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ JubesX.FaceChange("sly")
                                        if JubesX.PlayerFav == "cun":
                                            $ JubesX.Statup("Lust", 80, 3)
                                            ch_v "Разумеется."
                                        elif JubesX.Favorite == "cun":
                                            $ JubesX.Statup("Love", 90, 5)
                                            $ JubesX.Statup("Lust", 80, 5)
                                            ch_v "Мне тоже!"
                                        elif JubesX.CUN >= 10:
                                            ch_v "Ага, ты очень вкусная."
                                        elif not JubesX.CUN:
                                            $ JubesX.FaceChange("perplexed")
                                            ch_v "Кто лижет твою киску?!"
                                        else:
                                            $ JubesX.FaceChange("bemused")
                                            ch_v "Я. . . это хорошо. . ."
                                        $ JubesX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ JubesX.FaceChange("sly")
                                        if JubesX.PlayerFav == "titjob":
                                            $ JubesX.Statup("Lust", 80, 5)
                                            ch_v "Ага, ты уже говорил это ранее. . ."
                                        elif JubesX.Favorite == "titjob":
                                            $ JubesX.Statup("Love", 90, 5)
                                            $ JubesX.Statup("Lust", 80, 7)
                                            ch_v "Ага, мне это тоже нравится. . ."
                                        elif JubesX.Tit >= 10:
                                            ch_v "Это, безусловно, интересный опыт . . ."
                                        elif not JubesX.Tit:
                                            $ JubesX.FaceChange("perplexed")
                                            ch_v "Кто тебя трахает своими сиськами?"
                                        else:
                                            $ JubesX.FaceChange("bemused")
                                            ch_v "Мило с твоей стороны это упомянуть. . ."
                                            $ JubesX.Statup("Love", 80, 5)
                                            $ JubesX.Statup("Inbt", 50, 10)
                                        $ JubesX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ JubesX.FaceChange("sly")
                                        if JubesX.PlayerFav == "foot":
                                            $ JubesX.Statup("Lust", 80, 5)
                                            ch_v "Ага, ты уже говорил это. . ."
                                        elif JubesX.Favorite == "foot":
                                            $ JubesX.Statup("Love", 90, 5)
                                            $ JubesX.Statup("Lust", 80, 7)
                                            ch_v "Мне очень нравится использовать свои ножки. . ."
                                        elif JubesX.Foot >= 10:
                                            ch_v "Мне это тоже нравится . . ."
                                        elif not JubesX.Foot:
                                            $ JubesX.FaceChange("perplexed")
                                            ch_v "Кто играет с тобой своими ножками?"
                                        else:
                                            $ JubesX.FaceChange("bemused")
                                            ch_v "Ага, мило. . ."
                                        $ JubesX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ JubesX.FaceChange("sly")
                                        if JubesX.PlayerFav == "hand":
                                            $ JubesX.Statup("Lust", 80, 5)
                                            ch_v "Ага, ты уже говорил это. . ."
                                        elif JubesX.Favorite == "hand":
                                            $ JubesX.Statup("Love", 90, 5)
                                            $ JubesX.Statup("Lust", 80, 7)
                                            ch_v "Он комфортно лежит в руке. . ."
                                        elif JubesX.Hand >= 10:
                                            ch_v "Мне это тоже нравится . . ."
                                        elif not JubesX.Hand:
                                            $ JubesX.FaceChange("perplexed")
                                            ch_v "Кто тебе дрочит?"
                                        else:
                                            $ JubesX.FaceChange("bemused")
                                            ch_v "Ага, мило. . ."
                                        $ JubesX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ JubesX.FaceChange("sly")
                                        if JubesX.PlayerFav == "finger":
                                            $ JubesX.Statup("Lust", 80, 5)
                                            ch_v "Ага, ты уже говорила это. . ."
                                        elif JubesX.Favorite == "finger":
                                            $ JubesX.Statup("Love", 90, 5)
                                            $ JubesX.Statup("Lust", 80, 7)
                                            ch_v "Она приятная на ощупь. . ."
                                        elif JubesX.Finger >= 10:
                                            ch_v "Мне это тоже нравится . . ."
                                        elif not JubesX.Finger:
                                            $ JubesX.FaceChange("perplexed")
                                            ch_v "Кто тебе дрочит?"
                                        else:
                                            $ JubesX.FaceChange("bemused")
                                            ch_v "Ага, мило. . ."
                                        $ JubesX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = JubesX.FondleB + JubesX.FondleT + JubesX.SuckB + JubesX.Hotdog
                                        $ JubesX.FaceChange("sly")
                                        if JubesX.PlayerFav == "fondle":
                                            $ JubesX.Statup("Lust", 80, 3)
                                            ch_v "Ага, думаю, все уже поняли. . ."
                                        elif JubesX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ JubesX.Statup("Love", 90, 5)
                                            $ JubesX.Statup("Lust", 80, 5)
                                            ch_v "Мне нравится, когда ты прикасаешься ко мне. . ."
                                        elif Cnt >= 10:
                                            ch_v "Ага, это очень приятно. . ."
                                        elif not Cnt:
                                            $ JubesX.FaceChange("perplexed")
                                            ch_v "Кто позволяет тебе лапать себя?"
                                        else:
                                            $ JubesX.FaceChange("bemused")
                                            ch_v "Мне нравятся эти ощущения. . ."
                                        $ JubesX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ JubesX.FaceChange("sly")
                                        if JubesX.PlayerFav == "kiss you":
                                            $ JubesX.Statup("Love", 90, 3)
                                            ch_v "Мммммм. . ."
                                        elif JubesX.Favorite == "kiss you":
                                            $ JubesX.Statup("Love", 90, 5)
                                            $ JubesX.Statup("Lust", 80, 5)
                                            ch_v "Ммм, твой вкус на моих губах. . ."
                                        elif JubesX.Kissed >= 10:
                                            ch_v "Я тоже люблю тебя целовать. . ."
                                        elif not JubesX.Kissed:
                                            $ JubesX.FaceChange("perplexed")
                                            ch_v "Кого это ты целуешь?"
                                        else:
                                            $ JubesX.FaceChange("bemused")
                                            ch_v "Я тоже люблю тебя целовать. . ."
                                        $ JubesX.PlayerFav = "kiss you"

                        $ JubesX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(JubesX, 800):
                                        $ JubesX.FaceChange("perplexed")
                                        ch_v ". . ."
                                else:
                                        if JubesX.SEXP >= 50:
                                            $ JubesX.FaceChange("sly")
                                            if not Player.Male:
                                                ch_v "Ты должна знать. . ."
                                            else:
                                                ch_v "Ты должен знать. . ."
                                        else:
                                            $ JubesX.FaceChange("bemused")
                                            $ JubesX.Eyes = "side"
                                            ch_v "Хмм. . ."


                                        if not JubesX.Favorite or JubesX.Favorite == "kiss you":
                                                ch_v "Поцелуи?"
                                        elif JubesX.Favorite == "anal":
                                                ch_v "Пожалуй, анал."
                                        elif JubesX.Favorite == "lick ass":
                                                ch_v "Когда ты вылизываешь мою попку."
                                        elif JubesX.Favorite == "insert ass":
                                                ch_v "Наверное, когда ты трахаешь пальцем меня в попку."
                                        elif JubesX.Favorite == "sex":
                                                ch_v "Классический секс."
                                        elif JubesX.Favorite == "lick pussy":
                                                ch_v "Когда ты лижешь мою киску."
                                        elif JubesX.Favorite == "fondle pussy":
                                                ch_v "Когда ты теребишь мою киску пальцем."
                                        elif JubesX.Favorite == "blow":
                                                ch_v "Мне -нравится- вкус твоего члена."
                                        elif JubesX.Favorite == "cun":
                                                ch_v "Мне -нравится- вкус твоей киски."
                                        elif JubesX.Favorite == "tit":
                                                ch_v "Когда я использую свои сиськи."
                                        elif JubesX.Favorite == "foot":
                                                ch_v "Дрочка ногами - это довольно весело."
                                        elif JubesX.Favorite == "hand":
                                                ch_v "Мне нравится дрочить тебе."
                                        elif JubesX.Favorite == "finger":
                                                ch_v "Мне нравится ласкать тебя."
                                        elif JubesX.Favorite == "hotdog":
                                                ch_v "Когда ты трешься о меня."
                                        elif JubesX.Favorite == "suck breasts":
                                                ch_v "Когда ты сосешь мои сиськи."
                                        elif JubesX.Favorite == "fondle breasts":
                                                ch_v "Когда ты мнешь мои сиськи."
                                        elif JubesX.Favorite == "fondle thighs":
                                                ch_v "Когда ты растираешь мои бедра."
                                        else:
                                                ch_v "Откуда мне знать?"

                                # End Jubes's favorite things.

                "Не болтай так много во время секса." if "vocal" in JubesX.Traits:
                        if "setvocal" in JubesX.DailyActions:
                                $ JubesX.FaceChange("perplexed")
                                ch_v "Определись уже."
                        else:
                            if ApprovalCheck(JubesX, 1000) and JubesX.Obed <= JubesX.Love:
                                $ JubesX.FaceChange("bemused")
                                $ JubesX.Statup("Obed", 90, 1)
                                ch_v "Буду молчать, хорошо."
                                $ JubesX.Traits.remove("vocal")
                            elif ApprovalCheck(JubesX, 700, "O"):
                                $ JubesX.FaceChange("sadside")
                                $ JubesX.Statup("Obed", 90, 1)
                                ch_v ". . ."
                                $ JubesX.Traits.remove("vocal")
                            elif ApprovalCheck(JubesX, 600):
                                $ JubesX.FaceChange("sly")
                                $ JubesX.Statup("Love", 90, -3)
                                $ JubesX.Statup("Obed", 50, -1)
                                $ JubesX.Statup("Inbt", 90, 5)
                                ch_v "Не настаивай на этом, [JubesX.Petname]."
                            else:
                                $ JubesX.FaceChange("angry")
                                $ JubesX.Statup("Love", 90, -5)
                                $ JubesX.Statup("Obed", 60, -3)
                                $ JubesX.Statup("Inbt", 90, 10)
                                ch_v "Неее."

                            $ JubesX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in JubesX.Traits:
                        if "setvocal" in JubesX.DailyActions:
                                $ JubesX.FaceChange("perplexed")
                                ch_v "Я услышала тебя и в первый раз."
                        else:
                            if ApprovalCheck(JubesX, 1000) and JubesX.Obed <= JubesX.Love:
                                $ JubesX.FaceChange("sly")
                                $ JubesX.Statup("Obed", 90, 2)
                                ch_v "Это я могу. . ."
                                $ JubesX.Traits.append("vocal")
                            elif ApprovalCheck(JubesX, 700, "O"):
                                $ JubesX.FaceChange("sadside")
                                $ JubesX.Statup("Obed", 90, 2)
                                ch_v "Если ты этого хочешь, [JubesX.Petname]."
                                $ JubesX.Traits.append("vocal")
                            elif ApprovalCheck(JubesX, 600):
                                $ JubesX.FaceChange("sly")
                                $ JubesX.Statup("Obed", 90, 3)
                                if not Player.Male:
                                    ch_v "Уверена?"
                                else:
                                    ch_v "Уверен?"
                                $ JubesX.Traits.append("vocal")
                            else:
                                $ JubesX.FaceChange("angry")
                                $ JubesX.Statup("Inbt", 90, 5)
                                ch_v ". . ."

                            $ JubesX.DailyActions.append("setvocal")
                        # End Jubes Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in JubesX.Traits:
                        if "initiative" in JubesX.DailyActions:
                                $ JubesX.FaceChange("perplexed")
                                ch_v "Я услышала тебя и в первый раз."
                        else:
                            if ApprovalCheck(JubesX, 1200) and JubesX.Obed <= JubesX.Love:
                                $ JubesX.FaceChange("bemused")
                                $ JubesX.Statup("Obed", 90, 1)
                                ch_v "Хорошо, ты можешь взять инициативу на себя. . ."
                                $ JubesX.Traits.append("passive")
                            elif ApprovalCheck(JubesX, 700, "O"):
                                $ JubesX.FaceChange("sadside")
                                $ JubesX.Statup("Obed", 90, 1)
                                ch_v "Я постараюсь сдерживать себя. . ."
                                $ JubesX.Traits.append("passive")
                            elif ApprovalCheck(JubesX, 600):
                                $ JubesX.FaceChange("sly")
                                $ JubesX.Statup("Love", 90, -3)
                                $ JubesX.Statup("Obed", 50, -1)
                                $ JubesX.Statup("Inbt", 90, 5)
                                ch_v "Хм, нет."
                            else:
                                $ JubesX.FaceChange("angry")
                                $ JubesX.Statup("Love", 90, -5)
                                $ JubesX.Statup("Obed", 60, -3)
                                $ JubesX.Statup("Inbt", 90, 10)
                                ch_v "Угу. . ."

                            $ JubesX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in JubesX.Traits:
                        if "initiative" in JubesX.DailyActions:
                                $ JubesX.FaceChange("perplexed")
                                ch_v "Я услышала тебя и в первый раз."
                        else:
                            if ApprovalCheck(JubesX, 1000) and JubesX.Obed <= JubesX.Love:
                                $ JubesX.FaceChange("bemused")
                                $ JubesX.Statup("Obed", 90, 1)
                                ch_v "Я могу взять инициативу на себя. . ."
                                $ JubesX.Traits.remove("passive")
                            elif ApprovalCheck(JubesX, 700, "O"):
                                $ JubesX.FaceChange("sadside")
                                $ JubesX.Statup("Obed", 90, 1)
                                ch_v "Конечно, без проблем."
                                $ JubesX.Traits.remove("passive")
                            elif ApprovalCheck(JubesX, 600):
                                $ JubesX.FaceChange("sly")
                                $ JubesX.Statup("Obed", 90, 3)
                                ch_v "Посмотрим."
                                $ JubesX.Traits.remove("passive")
                            else:
                                $ JubesX.FaceChange("angry")
                                $ JubesX.Statup("Inbt", 90, 5)
                                ch_v "Ну уж нет."

                            $ JubesX.DailyActions.append("initiative")

                "О том, как ты накидываешься" if "jumped" in JubesX.History:
                            call Jubes_Jumped
                "О твоей мастурбации":
                            call NoFap(JubesX)

                "Всегда носи вибратор" if "dailyvibe" not in JubesX.Traits:
                        call Daily_Vibrator(JubesX)
                "Перестань всегда носить вибратор" if "dailyvibe" in JubesX.Traits:
                        ch_v "Ладно. . ."
                        $ JubesX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи анальную пробку" if "dailyplug" not in JubesX.Traits:
                        call Daily_Plug(JubesX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in JubesX.Traits:
                        ch_v "Ладно. . ."
                        $ JubesX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Неважно" if Line == "Ага, о чем ты хочешь поговорить?":
                            return
                "На этом все" if Line != "Ага, о чем ты хочешь поговорить?":
                            return
            if Line == "Ага, о чем ты хочешь поговорить?":
                $ Line = "Что-нибудь еще?"
    return
# End Jubes Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Jubes Chitchat /////////////////// #Work in progress
label Jubes_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if JubesX not in Digits:
                if ApprovalCheck(JubesX, 500, "L") or ApprovalCheck(JubesX, 250, "I"):
                    ch_v "О, вот мой номер, позвони мне как-нибудь."
                    $ Digits.append(JubesX)
                    return
                elif ApprovalCheck(JubesX, 250, "O"):
                    ch_v "Если тебе нужно будет позвонить мне, вот мой номер."
                    $ Digits.append(JubesX)
                    return

        if "hungry" not in JubesX.Traits and JubesX.Swallow >= 3 and JubesX.Loc == bg_current:  #She's swallowed a lot
                    call Jubes_Hungry
                    return

        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(JubesX, 800, "I")):
                    if JubesX.Loc == bg_current and JubesX.Thirst >= 30 and "refused" not in JubesX.DailyActions and "quicksex" not in JubesX.DailyActions:
                            $ JubesX.FaceChange("sly",1)
                            ch_v "Эй. . . хочешь чем-нибудь заняться?"
                            call Quick_Sex(JubesX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in JubesX.DailyActions:
#            $ Options.append("caught")
        if JubesX.Event[0] and "key" not in JubesX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in JubesX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in JubesX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in JubesX.DailyActions:
            $ Options.append("corruption")

        if "Jubes" not in JubesX.Names:
            $ Options.append("jubes")

        if JubesX.Date >= 1 and bg_current != "bg restaurant":
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in JubesX.DailyActions and "cheek" not in JubesX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if JubesX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")

        if "vamp" in "contagious" not in JubesX.History:
            $ Options.append("contagious")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in JubesX.DailyActions and (Player.Male or "girltalk" in JubesX.History):
            #If you've caught Jubes showering today
            $ Options.append("showercaught")
        if "fondle breasts" in JubesX.DailyActions or "fondle pussy" in JubesX.DailyActions or "fondle ass" in JubesX.DailyActions:
            #If you've fondled Jubes today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in JubesX.Inventory and "256 Shades of Grey" in JubesX.Inventory and "Avengers Tower Penthouse" in JubesX.Inventory:
            #If you've given Jubes the books
            if "book" not in JubesX.Chat:
                $ Options.append("booked")
        if "lace bra" in JubesX.Inventory or "lace panties" in JubesX.Inventory:
            #If you've given Jubes the lingerie
            if "lingerie" not in JubesX.Chat:
                $ Options.append("lingerie")
        if JubesX.Hand and Player.Male:
            #If Jubes's given a handjob
            $ Options.append("handy")
        if JubesX.Blow and Player.Male:
            #If Jubes's given a blowjob
            $ Options.append("blow")
        if JubesX.Swallow:
            #If Jubes's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in JubesX.DailyActions or "painted" in JubesX.DailyActions:
            #If Jubes's been facialed
            $ Options.append("facial")
        if JubesX.Sleep:
            #If Jubes's slept over
            $ Options.append("sleep")
        if (JubesX.CreamP or JubesX.CreamA) and Player.Male:
            #If Jubes's been creampied
            $ Options.append("creampie")
        if JubesX.Sex or JubesX.Anal:
            #If Jubes's been sexed
            $ Options.append("sexed")
        if JubesX.Anal:
            #If Jubes's been analed
            $ Options.append("anal")

        if "seenpeen" in JubesX.History and Player.Male:
            $ Options.append("seenpeen")
        if "topless" in JubesX.History:
            $ Options.append("topless")
        if "bottomless" in JubesX.History:
            $ Options.append("bottomless")

#        if not JubesX.Chat[0] and JubesX.Sex:
#            $ Options.append("virgin")

#        if (bg_current == "bg jubes" or bg_current == "bg player") and "relationship" not in JubesX.DailyActions:
#            if "lover" not in JubesX.Petnames and ApprovalCheck(JubesX, 900, "L"): # JubesX.Event[6]
#                $ Options.append("lover?")
#            elif "sir" not in JubesX.Petnames and ApprovalCheck(JubesX, 500, "O"): # JubesX.Event[7]
#                $ Options.append("sir?")
#            elif "daddy" not in JubesX.Petnames and ApprovalCheck(JubesX, 750, "L") and ApprovalCheck(JubesX, 500, "O") and ApprovalCheck(JubesX, 500, "I"): # JubesX.Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in JubesX.Petnames and ApprovalCheck(JubesX, 900, "O"): # JubesX.Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in JubesX.Petnames and ApprovalCheck(JubesX, 500, "I"): # JubesX.Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in JubesX.Petnames and ApprovalCheck(JubesX, 900, "I"): # JubesX.Event[10]
#                $ Options.append("fuckbuddy?")


        if not ApprovalCheck(JubesX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ JubesX.DailyActions.append("cologne chat")
        $ JubesX.FaceChange("confused")
        ch_v "(нюх, нюх). . . от тебя пахнет обезьяньей задницей . . ."
        ch_v ". . . почему это меня так заводит?"
        $ JubesX.FaceChange("sexy", 2)
    elif Options[0] == "purple":
        $ JubesX.DailyActions.append("cologne chat")
        $ JubesX.FaceChange("sly",1)
        ch_v "(нюх, нюх). . . какой необычный аромат. . ."
        $ JubesX.FaceChange("normal",0)
        ch_v ". . . ты чего-то хочешь?"
    elif Options[0] == "corruption":
        $ JubesX.DailyActions.append("cologne chat")
        $ JubesX.FaceChange("confused")
        ch_v "(нюх, нюх). . . это. . . эм, что-то сильное. . ."
        $ JubesX.FaceChange("angry")
        ch_v ". . . и опасное. . ."
        $ JubesX.FaceChange("sly")

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in JubesX.Chat:
                    ch_v "Мы должны стараться не попадаться."
                    if not ApprovalCheck(JubesX, 500, "I"):
                         ch_v "Пока. . ."
            else:
                    ch_v "Извини, что нас потащили в кабинет профессора."
                    if not ApprovalCheck(JubesX, 500, "I"):
                        ch_v "Думаю, ты больше не захочешь таких публичных действий."
                    else:
                        ch_v "Хотя мне было весело. . ."
                    $ JubesX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if JubesX.SEXP <= 15:
                if not Player.Male:
                    ch_v "Будь осторожна, используя этот ключ. . ."
                else:
                    ch_v "Будь осторожен, используя этот ключ. . ."
            else:
                ch_v "Я дала тебе ключ, но ты не приходишь. . ."
            $ JubesX.Chat.append("key")

#    elif Options[0] == "cheek":
#            #Jubes's response to having her cheek touched.
#            ch_v "So,[JubesX.Petname]. . .y'know how you[JubesX.like]kinda just brushed my cheek before?"
#            ch_p "Yeah?  Was that okay?"
#            $ JubesX.FaceChange("smile",1)
#            ch_v "More than just {i}okay{/i}."
#            $ JubesX.Chat.append("cheek")


    elif Options[0] == "contagious":
                        $ JubesX.FaceChange("sadside",2)
                        if not Player.Male:
                            ch_v "Просто чтобы ты знала, вся эта вампирская тема. . ."
                        else:
                            ch_v "Просто чтобы ты знал, вся эта вампирская тема. . ."
                        ch_v "Это не заразно. . ."
                        $ JubesX.FaceChange("sadside",1)
                        ch_v "Доктор Стрэндж смог наложить заклинание или что-то типа того."
                        ch_v "Так что тебе не нужно беспокоиться."
                        $ JubesX.FaceChange("sad",1)
                        $ JubesX.AddWord(1,0,0,0,"contagious") #adds "word" tag to History

    elif Options[0] == "jubes":
            #if she never told you her name. . .
            ch_v "А, кстати, меня также можно звать \"Джубс.\""
            ch_v "Я подумала, что тебе, наверное, стоит это знать."
            $ JubesX.Names.append("Jubes")
            $ JubesX.Pets.append("Jubes")
            menu:
                "О, это здорово, думаю, я буду звать тебя так.":
                        $ JubesX.Statup("Love", 70, 5) # Love
                        $ JubesX.Name = "Джубс"
                        $ JubesX.Name_rod = "Джубс"
                        $ JubesX.Name_dat = "Джубс"
                        $ JubesX.Name_vin = "Джубс"
                        $ JubesX.Name_tvo = "Джубс"
                        $ JubesX.Name_pre = "Джубс"
                "Хорошо, но мне больше нравится имя [JubesX.Name].":
                        $ JubesX.Statup("Love", 70, 2) # Love
                        $ JubesX.Statup("Obed", 70, 2) # Obed
                        $ JubesX.FaceChange("smile",1)
                        ch_v "Ох, ладно."

    elif Options[0] == "dated":
            #Jubes's response to having gone on a date with the Player.
            ch_v "Раньше мне нравилось гулять, но в последнее время у меня было не так уж много возможностей это делать."

    elif Options[0] == "kissed":
            #Jubes's response to having been kissed by the Player.
            $ JubesX.FaceChange("sly",1)
            ch_v "Ты отлично целуешься, [JubesX.Petname]."
            menu:
                extend ""
                "Эй. . . Да я лучшая." if not Player.Male:
                        $ JubesX.FaceChange("smile",1)
                        ch_v "Нууу. . . возможно."
                        ch_v "Мы должны это хорошенько проверить."
                "Эй. . . Да я лучший." if Player.Male:
                        $ JubesX.FaceChange("smile",1)
                        ch_v "Нууу. . . возможно."
                        ch_v "Мы должны это хорошенько проверить."
                "Ты правда так думаешь?":
                        ch_v "Разве я сказала бы подобное, будь это иначе?"

    elif Options[0] == "dangerroom":
            #Jubes's response to Player working out in the Danger Room while Jubes is present
            $ JubesX.FaceChange("sly",1)
            ch_v "Слушай, [JubesX.Petname]. Я видела тебя ранее в Комнате Опасности."
            ch_v "У тебя это на удивление хорошо получается, учитывая, что у тебя нет способности делать \"пиу-пиу\"."

    elif Options[0] == "showercaught":
            #Jubes's response to being caught in the shower.
            if "shower" in JubesX.Chat:
                if not Player.Male:
                    ch_v "Ты снова видела, как я принимала душ. . ."
                else:
                    ch_v "Ты снова видел, как я принимала душ. . ."
            else:
                ch_v "Эй, разве ты не проверяешь, прежде чем войти в душевую?"
                $ JubesX.Chat.append("shower")
                menu:
                    extend ""
                    "Это чистая случайность! Клянусь!":
                            $ JubesX.Statup("Love", 50, 5)
                            $ JubesX.Statup("Love", 90, 2)
                            if ApprovalCheck(JubesX, 1200):
                                $ JubesX.FaceChange("sly",1)
                                ch_v "Я не говорила, что против. . ."
                            $ JubesX.FaceChange("smile")
                            ch_v "Хорошо, конечно, отлично."
                    "Только если там ты.":
                            $ JubesX.Statup("Obed", 40, 5)
                            if ApprovalCheck(JubesX, 1000) or ApprovalCheck(JubesX, 700, "L"):
                                    $ JubesX.Statup("Love", 90, 3)
                                    $ JubesX.FaceChange("sly",1)
                                    ch_v "Нууу, думаю, это довольно мило. . ."
                            else:
                                    $ JubesX.Statup("Love", 70, -5)
                                    $ JubesX.FaceChange("angry")
                                    ch_v "Что ж, прекращай!"
                    "Я заглянула умышленно. Но я ни о чем не жалею." if not Player.Male:
                            if ApprovalCheck(JubesX, 1200):
                                    $ JubesX.Statup("Love", 90, 3)
                                    $ JubesX.Statup("Obed", 70, 10)
                                    $ JubesX.Statup("Inbt", 50, 5)
                                    $ JubesX.FaceChange("sly",1)
                                    ch_v "Справедливо."
                            elif ApprovalCheck(JubesX, 800):
                                    $ JubesX.Statup("Obed", 60, 5)
                                    $ JubesX.Statup("Inbt", 50, 5)
                                    $ JubesX.FaceChange("perplexed",2)
                                    ch_v "Нууу, думаю, я не могу винить тебя. . ."
                                    $ JubesX.Blush = 1
                            else:
                                    $ JubesX.Statup("Love", 50, -10)
                                    $ JubesX.Statup("Love", 80, -10)
                                    $ JubesX.Statup("Obed", 50, 10)
                                    $ JubesX.FaceChange("angry")
                                    ch_v "Это. . . неприятно. . ."
                    "Я заглянул умышленно. Но я ни о чем не жалею." if Player.Male:
                            if ApprovalCheck(JubesX, 1200):
                                    $ JubesX.Statup("Love", 90, 3)
                                    $ JubesX.Statup("Obed", 70, 10)
                                    $ JubesX.Statup("Inbt", 50, 5)
                                    $ JubesX.FaceChange("sly",1)
                                    ch_v "Справедливо."
                            elif ApprovalCheck(JubesX, 800):
                                    $ JubesX.Statup("Obed", 60, 5)
                                    $ JubesX.Statup("Inbt", 50, 5)
                                    $ JubesX.FaceChange("perplexed",2)
                                    ch_v "Нууу, думаю, я не могу винить тебя. . ."
                                    $ JubesX.Blush = 1
                            else:
                                    $ JubesX.Statup("Love", 50, -10)
                                    $ JubesX.Statup("Love", 80, -10)
                                    $ JubesX.Statup("Obed", 50, 10)
                                    $ JubesX.FaceChange("angry")
                                    ch_v "Это. . . неприятно. . ."

    elif Options[0] == "fondled":
            #Jubes's response to being felt up.
            if not Player.Male:
                ch_v "Слушай, не могла бы ты потрогать меня немного?"
            else:
                ch_v "Слушай, не мог бы ты потрогать меня немного?"

    elif Options[0] == "booked":
            #Jubes's response after a Player gives her the books from the shop.
            if not Player.Male:
                ch_v "Слушай, я прочитала те книги, которые ты мне дала."
            else:
                ch_v "Слушай, я прочитала те книги, которые ты мне дал."
            menu:
                extend ""
                "Да? Они тебе понравились?":
                        $ JubesX.FaceChange("sly",2)
                        ch_v "Нууу. . . да, наверное. . ."
                "Хорошо. Пожалуй, ты могла бы чему-нибудь из них научиться.":
                        $ JubesX.Statup("Love", 90, -3)
                        $ JubesX.Statup("Obed", 70, 5)
                        $ JubesX.Statup("Inbt", 50, 5)
                        $ JubesX.FaceChange("sad")
                        ch_v "Нууу. . . Думаю, да."
            $ JubesX.Blush = 1
            $ JubesX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Jubes's response to being given lingerie.
            $ JubesX.FaceChange("sly",2)
            if not Player.Male:
                ch_v "То нижнее белье, которое ты мне подарила, довольно милое. . . спасибо."
            else:
                ch_v "То нижнее белье, которое ты мне подарил, довольно милое. . . спасибо."
            $ JubesX.Blush = 1
            $ JubesX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Jubes's response after giving the Player a handjob.
            $ JubesX.FaceChange("sly",1)
            ch_v "Я фантазировала о твоем члене в моей руке. . ."
            ch_v "Возможно, мне стоит воплатить фантазию в жизнь. . ."
            $ JubesX.Blush = 0

    elif Options[0] == "blow":
            if "blow" not in JubesX.Chat:
                    #Jubes's response after giving the Player a blowjob.
                    $ JubesX.FaceChange("sly",2)
                    ch_v "Слушай, я ведь не кусалась, правда?"
                    menu:
                        extend ""
                        "Ты была великолепна.":
                                    $ JubesX.Statup("Love", 90, 5)
                                    $ JubesX.Statup("Inbt", 60, 10)
                                    $ JubesX.FaceChange("normal",1)
                                    ch_v "Хорошо. Это хорошо. . . "
                                    $ JubesX.FaceChange("sexy",1)
                                    ch_v "Я бы хотела как-нибудь повторить."
                        "Честно? Все было хорошо. . . но, думаю, тебе не помешает еще немного попрактиковаться.":
                                if ApprovalCheck(JubesX, 300, "I") or not ApprovalCheck(JubesX, 800):
                                    $ JubesX.Statup("Love", 90, -5)
                                    $ JubesX.Statup("Obed", 60, 10)
                                    $ JubesX.Statup("Inbt", 50, 10)
                                    $ JubesX.FaceChange("perplexed",1)
                                    ch_v "Ох! Извини!"
                                else:
                                    $ JubesX.Statup("Obed", 70, 15)
                                    $ JubesX.Statup("Inbt", 50, 5)
                                    $ JubesX.FaceChange("sexy",1)
                                    ch_v "Да? Нууу, совершенство достигается в практике. . ."
                        "Кусалась и больно.":
                                    $ JubesX.Statup("Love", 90, -5)
                                    $ JubesX.Statup("Obed", 60, 5)
                                    $ JubesX.FaceChange("sad",2)
                                    ch_v "Нууу. . . извини. . ."
                    $ JubesX.Blush = 1
                    $ JubesX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["Знаешь, у твоего члена отличный вкус.",
                            "Кажется, в прошлый раз я чуть не вывихнулf челюсть.",
                            "Дай мне знать, если как-нибудь ты захочешь еще один минет.",
                            "Ммммм. . . [Стучит языком по внутренней стороне щеки.]"])
                    ch_v "[Line]"

    elif Options[0] == "swallowed":
            #Jubes's response after swallowing the Player's cum.
            if "swallow" in JubesX.Chat:
                ch_v "Я бы не отказалась еще раз попробовать тебя. . ."
            else:
                ch_v "Так вот. . . на днях. . ."
                if not Player.Male:
                    ch_v "Я получила хороший заряд бодрости от того, что выпила твои. . ."
                else:
                    ch_v "Я получила хороший заряд бодрости от того, что выпила твою. . ."
                $ JubesX.FaceChange("sly",1)
                ch_v "Я не против как-нибудь повторить."
                $ JubesX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Jubes's response after taking a facial from the Player.
            ch_v "Слушай. . . Я знаю, это немного странно. . ."
            $ JubesX.FaceChange("sexy",2)
            if not Player.Male:
                ch_v "Мне приятно носить твои. . . соки, но. . ."
            else:
                ch_v "Мне приятно носить твою. . . сперму, но. . ."
            ch_v "Это вроде же бесполезно?"
            $ JubesX.Blush = 1

    elif Options[0] == "sleepover":
            #Jubes's response after sleeping with the Player.
            ch_v "Мне очень понравилась та ночь."
            ch_v "Было приятно снова провести ночь с кем-то."

    elif Options[0] == "creampie":
            #Another of Jubes's responses after having sex with the Player.
            "[JubesX.Name] сближается с вами, чтобы прошептать вам на ухо."
            ch_v "Мне нравилось чувствовать, как ты кончаешь в меня. . ."

    elif Options[0] == "sexed":
            #A final response from Jubes after having sex with the Player.
            ch_v "Слушай, эм. . ."
            $ JubesX.FaceChange("sexy",2)
            ch_v ". . .когда я. . . ублажала себя. . ."
            ch_v "Я думала о тебе."
            $ JubesX.Blush = 1

    elif Options[0] == "anal":
            #Jubes's response after getting anal from the Player.
            $ JubesX.FaceChange("sly")
            ch_v "Я раньше не занималась анальным сексом. . ."
            $ JubesX.FaceChange("sexy",1)
            ch_v "Нууу, по крайней мере, до тебя."

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ JubesX.FaceChange("sly",1, Eyes="down")
            ch_v "Ох, эм, тебе есть чем гордиться, м?"
            $ JubesX.FaceChange("bemused",1)
            $ JubesX.Statup("Love", 50, 5)
            $ JubesX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            ch_v "Слушай, тебе понравились мои сиськи или как?"
            call Girl_First_TMenu
            $ JubesX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            if not Player.Male:
                ch_v "Слушай, а что ты подумала, когда впервые увидела мою. . . эм. . ."
            else:
                ch_v "Слушай, а что ты подумал, когда впервые увидел мою. . . эм. . ."
            ch_v "-мою киску. . ."
            call Girl_First_BMenu
            $ JubesX.History.remove("bottomless")

#    elif Options[0] == "boyfriend?":
#        call Jubes_BF
#    elif Options[0] == "lover?":
#        call Jubes_Love
#    elif Options[0] == "sir?":
#        call Jubes_Sub
#    elif Options[0] == "master?":
#        call Jubes_Master
#    elif Options[0] == "sexfriend?":
#        call Jubes_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Jubes_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Jubes_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        if not Player.Male:
            $ Line = renpy.random.choice(["Отойди от меня.",
                    "Я не хочу, чтобы ты была рядом со мной.",
                    "Назад.",
                    "Отвали."])
        else:
            $ Line = renpy.random.choice(["Отойди от меня.",
                    "Я не хочу, чтобы ты был рядом со мной.",
                    "Назад.",
                    "Отвали."])
        ch_v "[Line]"

    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 21)
            if D20 == 1:
                    $ JubesX.FaceChange("smile")
                    ch_v "Приятно иметь возможность чаще выходить на улицу. . ."
            elif D20 == 2:
                    ch_v "Ты не поверишь, сколько кофе я выпила, чтобы пережить утреннюю лекцию. У меня передоз кофеином!"
            elif D20 == 3:
                    ch_v "В библиотеке кампуса была специальная выставка, посвященная истории мутантов. Я на несколько часов словно попала в прошлое."
            elif D20 == 4:
                    $ JubesX.FaceChange("sad",2)
                    ch_v "В обед была катастрофа! Я случайно опрокинула свой поднос в кафетерии, еда разлетелась по всему залу!"
                    $ JubesX.FaceChange("smile",1,Mouth="open")
                    ch_v ". . ."
            elif D20 == 5:
                    ch_v "Ночные игры с девочками, ужасно вымотали меня. . ."
            elif D20 == 6:
                    $ JubesX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_v "Так вот, я шла на занятия, и тут из ниоткуда появляется девушка с магнитными способностями и начинает плавить все металлическое вокруг себя. Ты бы видела какой хаос она создала."
                    else:
                        ch_v "Так вот, я шла на занятия, и тут из ниоткуда появляется девушка с магнитными способностями и начинает плавить все металлическое вокруг себя. Ты бы видел какой хаос она создала."
                    $ JubesX.FaceChange("normal")
            elif D20 == 7:
                    $ JubesX.FaceChange("smile")
                    ch_v "У меня был самый замечательный перерыв на обед! Я открыла для себя новое суши-заведение с шеф-поваром-мутантом, который может создавать огненные роллы. Это было умопомрачительно!"
            elif D20 == 8:
                    $ JubesX.FaceChange("smile")
                    ch_v "Ты же знаешь, как я могу создавать фейерверки кончиками пальцев? Сегодня я случайно зажгла искру во время занятия по рисованию. Вот так просто, одним движением пальцев можно всех удивить!"
            elif D20 == 9:
                    $ JubesX.FaceChange("smile")
                    ch_v "Угадай, что? Сегодня я спасла положение в кампусе. Появилась Бум Бум и начала создавать проблемы, но вмешалась я и надрала ей задницу!"
            elif D20 == 10:
                    $ JubesX.FaceChange("sadside",2)
                    ch_v "Ранее, во время занятий я нечаянно запустила фейерверк."
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Это было немного неловко. . . но и довольно круто!"
            elif D20 == 11:
                    ch_v "Сегодня у меня была самая сумасшедшая встреча. Я столкнулась с Логаном в библиотеке!"
                    ch_v "В итоге мы побеседовали о его жизни, и, позволь мне сказать, его истории - это нечто. . ."
            elif D20 == 12:
                    $ JubesX.FaceChange("smile")
                    ch_v "У меня была самая веселая встреча с ручной белкой Дорин во дворе."
                    ch_v "Мы закончили тем, что устроили танцевальный батл, и, позволь мне сказать, этот малыш очень хорошо танцует!"
            elif D20 == 13:
                    $ JubesX.FaceChange("sadside",2)
                    ch_v "У меня случился серьезный инцидент в библиотеке. Я случайно запустила немного. . . фейерверков."
                    $ JubesX.FaceChange("smile",1,Mouth="open")
                    ch_v "Излишне говорить, что это привлекло всеобщее внимание!"
            elif D20 == 14:
                    ch_v "Сегодня я столкнулась с Логаном, и он дал мне несколько эпичных советов по боевой подготовке."
                    ch_v "Не могу дождаться, чтобы показать свои новые навыки в следующем спарринге!"
            elif D20 == 15:
                    $ JubesX.FaceChange("angry")
                    ch_v "Боже мой, ты не поверишь, что профессор МакКой мне сегодня сказал. Он был так строг со мной, когда я пила кровь в лаборатории!"
                    $ JubesX.FaceChange("normal")
            elif D20 == 16:
                    $ JubesX.FaceChange("sad")
                    ch_v "Так вот, когда я шла через кампус, я случайно напугала парочку новеньких своими клыками."
                    $ JubesX.FaceChange("sad",2)
                    ch_v "Они буквально побросали свои книги и побежали."
                    $ JubesX.FaceChange("sadside",2,Mouth="smile")
                    ch_v "Это было уморительно. . . и -слегка- неловко!"
                    $ JubesX.FaceChange("normal",1)
            elif D20 == 17:
                    $ JubesX.FaceChange("smile")
                    ch_v "Я нашла укромное место в кампусе, которое идеально подходит для наблюдения за восходом солнца."
                    ch_v "Цвета были настолько яркими, я очень рада, что у меня появилась возможность увидеть это снова. Это было так захватывающе."
            elif D20 == 18:
                    $ JubesX.FaceChange("smile")
                    ch_v "Тебе ведь знакомы эти бесячие листовки, которые постоянно кто-нибудь раздает? Так вот, сегодня я случайно подпалила их своим фейерверком, пытаясь пройти мимо."
                    ch_v "Лицо того парня было незабываемым, но после этого я почувствовала себя плохо. . ."
            elif D20 == 19:
                    ch_v "Я окончательно превратилась в ночную сову. Вместо того чтобы заниматься днем, я могу заниматься всю ночь, когда все остальные спят."
                    ch_v "Это на удивление спокойно и продуктивно!"
            elif D20 == 20:
                    ch_v "Так вот, я записалась на вечерние занятия йогой, чтобы помочь своей гибкости."
                    $ JubesX.FaceChange("smile")
                    ch_v "Скажу так, моя поза раком вышла на совершенно новый уровень."
            else:
                    $ JubesX.FaceChange("smile")
                    ch_v "Мне нравится проводить время с тобой."

    $ Line = 0
    return

# start Jubes_Names//////////////////////////////////////////////////////////
label Jubes_Names:
    menu:
        ch_v "А? Как ты хочешь, чтобы я тебя звала?"
        "Зови по инициалам.":
            $ JubesX.Petname = Player.Name[:1]  #fix test this
            $ JubesX.Petname_rod = Player.Name[:1]
            $ JubesX.Petname_dat = Player.Name[:1]
            $ JubesX.Petname_vin = Player.Name[:1]
            $ JubesX.Petname_tvo = Player.Name[:1]
            $ JubesX.Petname_pre = Player.Name[:1]
            ch_v "Поняла, [JubesX.Petname]."
        "Зови меня по имени.":
            $ JubesX.Petname = Player.Name
            $ JubesX.Petname_rod = Player.Name_rod
            $ JubesX.Petname_dat = Player.Name_dat
            $ JubesX.Petname_vin = Player.Name_vin
            $ JubesX.Petname_tvo = Player.Name_tvo
            $ JubesX.Petname_pre = Player.Name_pre
            ch_v "Как хочешь, [JubesX.Petname]."
        "Зови меня \"моя девушка\"." if "boyfriend" in JubesX.Petnames and not Player.Male:
            $ JubesX.Petname = "моя девушка"
            $ JubesX.Petname_rod = "моей девушки"
            $ JubesX.Petname_dat = "моей девушке"
            $ JubesX.Petname_vin = "мою девушку"
            $ JubesX.Petname_tvo = "моей девушкой"
            $ JubesX.Petname_pre = "моей девушке"
            ch_v "Конечно, [JubesX.Petname]."
        "Зови меня \"мой парень\"." if "boyfriend" in JubesX.Petnames and Player.Male:
            $ JubesX.Petname = "мой парень"
            $ JubesX.Petname_rod = "моего парня"
            $ JubesX.Petname_dat = "моему парню"
            $ JubesX.Petname_vin = "моего парня"
            $ JubesX.Petname_tvo = "моим парнем"
            $ JubesX.Petname_pre = "моем парне"
            ch_v "Конечно, [JubesX.Petname]."
        "Зови меня \"любимая\"." if "lover" in JubesX.Petnames and not Player.Male:
            $ JubesX.Petname = "любимая"
            $ JubesX.Petname_rod = "любимой"
            $ JubesX.Petname_dat = "любимой"
            $ JubesX.Petname_vin = "любимую"
            $ JubesX.Petname_tvo = "любимой"
            $ JubesX.Petname_pre = "любимой"
            ch_v "Ооох, мне нравится, [JubesX.Petname]."
        "Зови меня \"любимый\"." if "lover" in JubesX.Petnames and Player.Male:
            $ JubesX.Petname = "любимый"
            $ JubesX.Petname_rod = "любимого"
            $ JubesX.Petname_dat = "любимому"
            $ JubesX.Petname_vin = "любимого"
            $ JubesX.Petname_tvo = "любимым"
            $ JubesX.Petname_pre = "любимом"
            ch_v "Ооох, мне нравится, [JubesX.Petname]."
        "Зови меня \"госпожа\"." if "sir" in JubesX.Petnames and not Player.Male:
            $ JubesX.Petname = "госпожа"
            $ JubesX.Petname_rod = "госпожи"
            $ JubesX.Petname_dat = "госпоже"
            $ JubesX.Petname_vin = "госпожу"
            $ JubesX.Petname_tvo = "госпожой"
            $ JubesX.Petname_pre = "госпоже"
            ch_v "Да, [JubesX.Petname]."
        "Зови меня \"господин\"." if "sir" in JubesX.Petnames and Player.Male:
            $ JubesX.Petname = "господин"
            $ JubesX.Petname_rod = "господина"
            $ JubesX.Petname_dat = "господину"
            $ JubesX.Petname_vin = "господина"
            $ JubesX.Petname_tvo = "господином"
            $ JubesX.Petname_pre = "господине"
            ch_v "Да, [JubesX.Petname]."
        "Зови меня \"хозяйка\"." if "master" in JubesX.Petnames and not Player.Male:
            $ JubesX.Petname = "хозяйка"
            $ JubesX.Petname_rod = "хозяйки"
            $ JubesX.Petname_dat = "хозяйке"
            $ JubesX.Petname_vin = "хозяйку"
            $ JubesX.Petname_tvo = "хозяйкой"
            $ JubesX.Petname_pre = "хозяйке"
            ch_v "Как пожелаешь, [JubesX.Petname]."
        "Зови меня \"хозяин\"." if "master" in JubesX.Petnames and Player.Male:
            $ JubesX.Petname = "хозяин"
            $ JubesX.Petname_rod = "хозяина"
            $ JubesX.Petname_dat = "хозяину"
            $ JubesX.Petname_vin = "хозяина"
            $ JubesX.Petname_tvo = "хозяином"
            $ JubesX.Petname_pre = "хозяине"
            ch_v "Как пожелаешь, [JubesX.Petname]."
        "Зови меня \"любовница\"." if "sex friend" in JubesX.Petnames and not Player.Male:
            $ JubesX.Petname = "любовница"
            $ JubesX.Petname_rod = "любовницы"
            $ JubesX.Petname_dat = "любовнице"
            $ JubesX.Petname_vin = "любовницу"
            $ JubesX.Petname_tvo = "любовницей"
            $ JubesX.Petname_pre = "любовнице"
            ch_v "Хех, забавно, [JubesX.Petname]."
        "Зови меня \"любовник\"." if "sex friend" in JubesX.Petnames and Player.Male:
            $ JubesX.Petname = "любовник"
            $ JubesX.Petname_rod = "любовника"
            $ JubesX.Petname_dat = "любовнику"
            $ JubesX.Petname_vin = "любовника"
            $ JubesX.Petname_tvo = "любовником"
            $ JubesX.Petname_pre = "любовнике"
            ch_v "Хех, забавно, [JubesX.Petname]."
        "Зови меня \"секс-партнерша\"." if "fuck buddy" in JubesX.Petnames and not Player.Male:
            $ JubesX.Petname = "секс-партнерша"
            $ JubesX.Petname_rod = "секс-партнерши"
            $ JubesX.Petname_dat = "секс-партнерше"
            $ JubesX.Petname_vin = "секс-партнершу"
            $ JubesX.Petname_tvo = "секс-партнершей"
            $ JubesX.Petname_pre = "секс-партнерше"
            ch_v "Я в деле, если ты готова, [JubesX.Petname]."
        "Зови меня \"секс-партнер\"." if "fuck buddy" in JubesX.Petnames and Player.Male:
            $ JubesX.Petname = "секс-партнер"
            $ JubesX.Petname_rod = "секс-партнера"
            $ JubesX.Petname_dat = "секс-партнеру"
            $ JubesX.Petname_vin = "секс-партнера"
            $ JubesX.Petname_tvo = "секс-партнером"
            $ JubesX.Petname_pre = "секс-партнере"
            ch_v "Я в деле, если ты готов, [JubesX.Petname]."
        "Зови меня \"мамочка\"." if "daddy" in JubesX.Petnames and not Player.Male:
            $ JubesX.Petname = "мамочка"
            $ JubesX.Petname_rod = "мамочки"
            $ JubesX.Petname_dat = "мамочке"
            $ JubesX.Petname_vin = "мамочку"
            $ JubesX.Petname_tvo = "мамочкой"
            $ JubesX.Petname_pre = "мамочке"
            ch_v "Ох! Конечно, [JubesX.Petname]."
        "Зови меня \"папочка\"." if "daddy" in JubesX.Petnames and Player.Male:
            $ JubesX.Petname = "папочка"
            $ JubesX.Petname_rod = "папочки"
            $ JubesX.Petname_dat = "папочке"
            $ JubesX.Petname_vin = "папочку"
            $ JubesX.Petname_tvo = "папочкой"
            $ JubesX.Petname_pre = "папочке"
            ch_v "Ох! Конечно, [JubesX.Petname]."
        "Чувиха в самый раз." if and not Player.Male:
            $ JubesX.Petname = "Чувиха"
            $ JubesX.Petname_rod = "Чувихи"
            $ JubesX.Petname_dat = "Чувихе"
            $ JubesX.Petname_vin = "Чувиху"
            $ JubesX.Petname_tvo = "Чувихой"
            $ JubesX.Petname_pre = "Чувихе"
            ch_v "Поняла, чувиха."
        "Чувак в самый раз." if and Player.Male:
            $ JubesX.Petname = "Чувак"
            $ JubesX.Petname_rod = "Чувака"
            $ JubesX.Petname_dat = "Чуваку"
            $ JubesX.Petname_vin = "Чувака"
            $ JubesX.Petname_tvo = "Чуваком"
            $ JubesX.Petname_pre = "Чуваке"
            ch_v "Поняла, чувак."
        "Сис в самый раз." if "bro" in JubesX.Petnames and not Player.Male:
            $ JubesX.Petname = "сис"
            $ JubesX.Petname_rod = "сис"
            $ JubesX.Petname_dat = "сис"
            $ JubesX.Petname_vin = "сис"
            $ JubesX.Petname_tvo = "сис"
            $ JubesX.Petname_pre = "сис"
            ch_v "Поняла, [JubesX.Petname]."
        "Бро в самый раз." if "bro" in JubesX.Petnames and Player.Male:
            $ JubesX.Petname = "бро"
            $ JubesX.Petname_rod = "бро"
            $ JubesX.Petname_dat = "бро"
            $ JubesX.Petname_vin = "бро"
            $ JubesX.Petname_tvo = "бро"
            $ JubesX.Petname_pre = "бро"
            ch_v "Поняла, [JubesX.Petname]."
        "Неважно.":
            return
    return
# end Jubes_Names//////////////////////////////////////////////////////////

label Jubes_Pet:
    while 1:
        menu:
            extend ""
            "Обходительно":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "Джубс.":
                        $ JubesX.Pet = "Джубс"
                        $ JubesX.Pet_rod = "Джубс"
                        $ JubesX.Pet_dat = "Джубс"
                        $ JubesX.Pet_vin = "Джубс"
                        $ JubesX.Pet_tvo = "Джубс"
                        $ JubesX.Pet_pre = "Джубс"
                        ch_v "Конечно, [JubesX.Petname]."

                    "Джубили.":
                        $ JubesX.Pet = "Джубили"
                        $ JubesX.Pet_rod = "Джубили"
                        $ JubesX.Pet_dat = "Джубили"
                        $ JubesX.Pet_vin = "Джубили"
                        $ JubesX.Pet_tvo = "Джубили"
                        $ JubesX.Pet_pre = "Джубили"
                        ch_v "Конечно, [JubesX.Petname]."

                    "Джубилейшен.":
                        $ JubesX.Pet = "Джубилейшен"
                        $ JubesX.Pet_rod = "Джубилейшен"
                        $ JubesX.Pet_dat = "Джубилейшен"
                        $ JubesX.Pet_vin = "Джубилейшен"
                        $ JubesX.Pet_tvo = "Джубилейшен"
                        $ JubesX.Pet_pre = "Джубилейшен"
                        ch_v "Конечно, [JubesX.Petname]."

                    "\"моя девушка\".":
                        if "boyfriend" in JubesX.Petnames:
                            $ JubesX.Pet = "моя девушка"
                            $ JubesX.Pet_rod = "моей девушки"
                            $ JubesX.Pet_dat = "моей девушке"
                            $ JubesX.Pet_vin = "мою девушку"
                            $ JubesX.Pet_tvo = "моей девушкой"
                            $ JubesX.Pet_pre = "моей девушке"
                            $ JubesX.FaceChange("sexy", 1)
                            ch_v "Ага, я твоя, [JubesX.Petname]."
                        else:
                            $ JubesX.FaceChange("angry")
                            ch_v "Я НЕ твоя девушка, [JubesX.Petname]."

                    "\"детка\".":
                        if "boyfriend" in JubesX.Petnames or ApprovalCheck(JubesX, 700, "L"):
                            $ JubesX.Pet = "детка"
                            $ JubesX.Pet_rod = "детки"
                            $ JubesX.Pet_dat = "детке"
                            $ JubesX.Pet_vin = "детку"
                            $ JubesX.Pet_tvo = "деткой"
                            $ JubesX.Pet_pre = "детке"
                            $ JubesX.FaceChange("sexy", 1)
                            ch_v "Я твоя детка, [JubesX.Petname]."
                        else:
                            $ JubesX.FaceChange("angry")
                            ch_v "Я тебе НЕ детка, [JubesX.Petname]."

                    "\"крошка\".":
                        if "boyfriend" in JubesX.Petnames or ApprovalCheck(JubesX, 600, "L"):
                            $ JubesX.Pet = "крошка"
                            $ JubesX.Pet_rod = "крошки"
                            $ JubesX.Pet_dat = "крошке"
                            $ JubesX.Pet_vin = "крошку"
                            $ JubesX.Pet_tvo = "крошкой"
                            $ JubesX.Pet_pre = "крошке"
                            $ JubesX.FaceChange("sexy", 1)
                            ch_v "Я твоя крошка, [JubesX.Petname]."
                        else:
                            $ JubesX.FaceChange("angry")
                            ch_v "Я тебе НЕ крошка, [JubesX.Petname]."

                    "\"малышка\".":
                        if "boyfriend" in JubesX.Petnames or ApprovalCheck(JubesX, 500, "L"):
                            $ JubesX.Pet = "малышка"
                            $ JubesX.Pet_rod = "малышки"
                            $ JubesX.Pet_dat = "малышке"
                            $ JubesX.Pet_vin = "малышку"
                            $ JubesX.Pet_tvo = "малышкой"
                            $ JubesX.Pet_pre = "малышке"
                            $ JubesX.FaceChange("sexy", 1)
                            ch_v "Мило, [JubesX.Petname]."
                        else:
                            $ JubesX.FaceChange("angry")
                            ch_v "Я не твоя малышка."


                    "\"милая\".":
                        if "boyfriend" in JubesX.Petnames or ApprovalCheck(JubesX, 600, "L"):
                            $ JubesX.Pet = "милая"
                            $ JubesX.Pet_rod = "милой"
                            $ JubesX.Pet_dat = "милой"
                            $ JubesX.Pet_vin = "милую"
                            $ JubesX.Pet_tvo = "милой"
                            $ JubesX.Pet_pre = "милой"
                            ch_v "Оу, как мило, [JubesX.Petname]."
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Слишком приторно, [JubesX.Petname]."

                    "\"секси\".":
                        if "lover" in JubesX.Petnames or ApprovalCheck(JubesX, 800):
                            $ JubesX.Pet = "секси"
                            $ JubesX.Pet_rod = "секси"
                            $ JubesX.Pet_dat = "секси"
                            $ JubesX.Pet_vin = "секси"
                            $ JubesX.Pet_tvo = "секси"
                            $ JubesX.Pet_pre = "секси"
                            $ JubesX.FaceChange("sexy", 1)
                            ch_v "Тебе виднее, [JubesX.Petname]."
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Я не уверена, [JubesX.Petname]."

                    "\"любимая\".":
                        if "lover" in JubesX.Petnames or ApprovalCheck(JubesX, 1200):
                            $ JubesX.Pet = "любимая"
                            $ JubesX.Pet_rod = "любимой"
                            $ JubesX.Pet_dat = "любимой"
                            $ JubesX.Pet_vin = "любимую"
                            $ JubesX.Pet_tvo = "любимой"
                            $ JubesX.Pet_pre = "любимой"
                            $ JubesX.FaceChange("sexy", 1)
                            ch_v "Я знаю."
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Я так не думаю, [JubesX.Petname]."

                    "Назад":
                        pass

            "Грубо":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "\"рабыня\".":
                        if "master" in JubesX.Petnames or ApprovalCheck(JubesX, 800, "O"):
                            $ JubesX.Pet = "рабыня"
                            $ JubesX.Pet_rod = "рабыни"
                            $ JubesX.Pet_dat = "рабыне"
                            $ JubesX.Pet_vin = "рабыню"
                            $ JubesX.Pet_tvo = "рабыней"
                            $ JubesX.Pet_pre = "рабыне"
                            $ JubesX.FaceChange("bemused", 1)
                            ch_v "Как пожелаешь, [JubesX.Petname]."
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Я не твоя рабыня, [JubesX.Petname]."

                    "\"питомец\".":
                        if "master" in JubesX.Petnames or ApprovalCheck(JubesX, 650, "O"):
                            $ JubesX.Pet = "питомец"
                            $ JubesX.Pet_rod = "питомце"
                            $ JubesX.Pet_dat = "питомцу"
                            $ JubesX.Pet_vin = "питомца"
                            $ JubesX.Pet_tvo = "питомцем"
                            $ JubesX.Pet_pre = "питомце"
                            $ JubesX.FaceChange("bemused", 1)
                            ch_v "Можешь погладить меня, если хочешь, [JubesX.Petname]."
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Я не твой питомец, [JubesX.Petname]."

                    "\"шлюха\".":
                        if "sex friend" in JubesX.Petnames or ApprovalCheck(JubesX, 900, "OI"):
                            $ JubesX.Pet = "шлюха"
                            $ JubesX.Pet_rod = "шлюхи"
                            $ JubesX.Pet_dat = "шлюхе"
                            $ JubesX.Pet_vin = "шлюху"
                            $ JubesX.Pet_tvo = "шлюхой"
                            $ JubesX.Pet_pre = "шлюхе"
                            $ JubesX.FaceChange("sexy")
                            ch_v "Логично."
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            $ JubesX.Mouth = "surprised"
                            ch_v "Следи за языком."

                    "\"блядь\".":
                        if "fuckbuddy" in JubesX.Petnames or ApprovalCheck(JubesX, 1000, "OI"):
                            $ JubesX.Pet = "блядь"
                            $ JubesX.Pet_rod = "бляди"
                            $ JubesX.Pet_dat = "бляде"
                            $ JubesX.Pet_vin = "блядь"
                            $ JubesX.Pet_tvo = "блядью"
                            $ JubesX.Pet_pre = "бляде"
                            $ JubesX.FaceChange("sly")
                            ch_v "Ауч. . ."
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Осторожнее, не то. . ."

                    "\"сладкогрудая\".":
                        if "sex friend" in JubesX.Petnames or ApprovalCheck(JubesX, 1400):
                            $ JubesX.Pet = "сладкогрудая"
                            $ JubesX.Pet_rod = "сладкогрудой"
                            $ JubesX.Pet_dat = "сладкогрудой"
                            $ JubesX.Pet_vin = "сладкогрудую"
                            $ JubesX.Pet_tvo = "сладкогрудой"
                            $ JubesX.Pet_pre = "сладкогрудой"
                            $ JubesX.FaceChange("sly", 1)
                            ch_v "А?"
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Это не прикольно."

                    "\"любовница\".":
                        if "sex friend" in JubesX.Petnames or ApprovalCheck(JubesX, 600, "I"):
                            $ JubesX.Pet = "любовница"
                            $ JubesX.Pet_rod = "любовницы"
                            $ JubesX.Pet_dat = "любовнице"
                            $ JubesX.Pet_vin = "любовницу"
                            $ JubesX.Pet_tvo = "любовницей"
                            $ JubesX.Pet_pre = "любовнице"
                            $ JubesX.FaceChange("sly")
                            ch_v "Ага. . ."
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Осторожнее выбирай слова, [JubesX.Petname]."

                    "\"секс-партнерша\".":
                        if "fuckbuddy" in JubesX.Petnames or ApprovalCheck(JubesX, 700, "I"):
                            $ JubesX.Pet = "секс-партнерша"
                            $ JubesX.Pet_rod = "секс-партнерши"
                            $ JubesX.Pet_dat = "секс-партнерше"
                            $ JubesX.Pet_vin = "секс-партнершу"
                            $ JubesX.Pet_tvo = "секс-партнершей"
                            $ JubesX.Pet_pre = "секс-партнерше"
                            $ JubesX.FaceChange("sly")
                            ch_v "Агась."
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            $ JubesX.Mouth = "surprised"
                            ch_v "Да не в жизнь, [JubesX.Petname]."

                    "\"доченька\".":
                        if "daddy" in JubesX.Petnames or ApprovalCheck(JubesX, 1200):
                            $ JubesX.Pet = "доченька"
                            $ JubesX.Pet_rod = "доченьки"
                            $ JubesX.Pet_dat = "доченьке"
                            $ JubesX.Pet_vin = "доченьку"
                            $ JubesX.Pet_tvo = "доченькой"
                            $ JubesX.Pet_pre = "доченьке"
                            $ JubesX.FaceChange("smile", 1)
                            ch_v "Ладно?"
                        else:
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Это дико странно."

                    "\"Мисс Ли\"." if "Miss Lee" in JubesX.Names:
                        if ApprovalCheck(JubesX, 900):
                            $ JubesX.Pet = "Мисс Ли"
                            $ JubesX.Pet_rod = "Мисс Ли"
                            $ JubesX.Pet_dat = "Мисс Ли"
                            $ JubesX.Pet_vin = "Мисс Ли"
                            $ JubesX.Pet_tvo = "Мисс Ли"
                            $ JubesX.Pet_pre = "Мисс Ли"
                            $ JubesX.FaceChange("bemused", 1)
                            ch_v "Хорошо, если тебе так хочется, [JubesX.Petname]."
                        else:
                            $ JubesX.FaceChange("sad", 1)
                            ch_v "Это типа слишком. . . формально, [JubesX.Petname]."

                    "Назад":
                        pass

            "Неважно.":
                return
    return

#label Jubes_Namecheck(JubesX.Pet = JubesX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname


# start Jubes_Rename//////////////////////////////////////////////////////////
label Jubes_Rename:
        #Sets alternate names from Jubes
        $ JubesX.Mouth = "smile"
        ch_v "Да?"
        menu:
            extend ""
            "Думаю, \"Джубили\" красивое имя." if JubesX.Name != "Джубили":
                    $ JubesX.Name = "Джубили"
                    $ JubesX.Name_rod = "Джубили"
                    $ JubesX.Name_dat = "Джубили"
                    $ JubesX.Name_vin = "Джубили"
                    $ JubesX.Name_tvo = "Джубили"
                    $ JubesX.Name_pre = "Джубили"
                    ch_v "Звучит неплохо."
            "Думаю, \"Джубс\" прикольное имя." if JubesX.Name != "Джубс":
                    $ JubesX.Name = "Джубс"
                    $ JubesX.Name_rod = "Джубс"
                    $ JubesX.Name_dat = "Джубс"
                    $ JubesX.Name_vin = "Джубс"
                    $ JubesX.Name_tvo = "Джубс"
                    $ JubesX.Name_pre = "Джубс"
                    ch_v "Хорошо, если ты хочешь. . ."
            "Думаю, \"Джубилейшен\" прекрасное имя." if JubesX.Name != "Джубилейшен" and "Jubilation" in JubesX.Names:
                    $ JubesX.Name = "Джубилейшен"
                    $ JubesX.Name_rod = "Джубилейшен"
                    $ JubesX.Name_dat = "Джубилейшен"
                    $ JubesX.Name_vin = "Джубилейшен"
                    $ JubesX.Name_tvo = "Джубилейшен"
                    $ JubesX.Name_pre = "Джубилейшен"
                    ch_v "Оу, спасибо. . ."
            "\"Мисс Ли\"." if "Miss Lee" in JubesX.Names and JubesX.Name != "Мисс Ли":
                    if ApprovalCheck(JubesX, 900):
                        $ JubesX.FaceChange("bemused", 1)
                        $ JubesX.Name = "Мисс Ли"
                        $ JubesX.Name_rod = "Мисс Ли"
                        $ JubesX.Name_dat = "Мисс Ли"
                        $ JubesX.Name_vin = "Мисс Ли"
                        $ JubesX.Name_tvo = "Мисс Ли"
                        $ JubesX.Name_pre = "Мисс Ли"
                        ch_v "Хорошо, если тебе так хочется, [JubesX.Petname]."
                    else:
                        $ JubesX.FaceChange("sad", 1)
                        ch_v "Это типа слишком. . . формально, [JubesX.Petname]."
            "Неважно.":
                    pass
        $ JubesX.AddWord(1,0,"namechange")
        return
# end Jubes_Rename//////////////////////////////////////////////////////////


# start Jubes_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jubes_Personality(Cnt = 0):
    if not JubesX.Chat[4] or Cnt:
        "Поскольку у вас все хорошо получается в одной области, вы можете убедить Джуби сосредоточиться на любой другой."
        "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
        "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
    menu:
        ch_v "Да? Что такое?"
        "Больше Послушания. [[Любовь в Послушание]" if JubesX.Love > 900:
            ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
            ch_v "Конечно, если тебя это так волнует."
            $ JubesX.Chat[4] = 1
        "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if JubesX.Love > 900:
            ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
            ch_v "Я всегда могу быть немного более дикой, если ты этого хочешь."
            $ JubesX.Chat[4] = 2

        "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if JubesX.Obed > 900:
            ch_p "Я хочу, чтобы ты была более раскрепощенной."
            ch_v "Думаю, ради тебя я могу пойти на все."
            $ JubesX.Chat[4] = 3
        "Больше Любви. [[Повиновение в Любовь]" if JubesX.Obed > 900:
            ch_p "Я хочу, чтобы ты училась любить меня."
            ch_v "Я могу попробовать."
            $ JubesX.Chat[4] = 4

        "Больше Повиновения. [[Раскрепощенность в Повиновение]" if JubesX.Inbt > 900:
            ch_p "Я знаю, что нам и так весело, но разве ты не можешь иногда слушаться меня?"
            ch_v "Я могу попробовать. . ."
            $ JubesX.Chat[4] = 5

        "Больше Любви. [[Раскрепощенность в Любовь]" if JubesX.Inbt > 900:
            ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
            ch_v "Если тебе это нужно. . ."
            $ JubesX.Chat[4] = 6

        "Просто делай то, что тебе нравится. . .[[Сбросить]" if JubesX.Chat[4]:
            ch_p "Помнишь, что мы обсуждали? Забудь."
            ch_v "Эм, ладно."
            $ JubesX.Chat[4] = 0
        "Повторить правила":
            call Jubes_Personality(1)
            return
        "Неважно.":
            return
    return
# end Jubes_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Jubes_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_Summon(Tempmod=Tempmod):
    $ JubesX.OutfitChange()
    if "no summon" in JubesX.RecentActions:
                if "angry" in JubesX.RecentActions:
                    ch_v "Гррррррр."
                elif JubesX.RecentActions.count("no summon") > 1:
                    ch_v "Отвали!"
                    $ JubesX.RecentActions.append("angry")
#                elif Current_Time == "Night":
#                    ch_v "Like I said, it's too late for that."
                else:
                    ch_v "Как я уже сказала, я занята."
                $ JubesX.RecentActions.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if JubesX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif JubesX.Loc == "bg dangerroom":
        $ Tempmod = -10
    elif JubesX.Loc == "bg showerroom":
        $ Tempmod = -30

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"
#    if Current_Time == "Night":
#                if ApprovalCheck(JubesX, 500, "L") or ApprovalCheck(JubesX, 400, "O"):
#                        #It's night time but she likes you.
#                        ch_v "You're up too? Sure, we can hang."
#                        $ JubesX.Loc = bg_current
#                        call Set_The_Scene
#                else:
#                        #It's night time and she isn't into you
#                        ch_v "Nah."
#                        $ JubesX.RecentActions.append("no summon")
#                return
    if "les" in JubesX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(JubesX, 2000):
                    ch_v "У меня сейчас кое-кто есть, но, думаю, ты можешь заглянуть ко мне. . ."
                    menu:
                        extend ""
                        "Конечно.":
                            $ Line = "go to"
                        "Нет, спасибо.":
                            if not Player.Male:
                                ch_v "Хех, ты сделала свой выбор."
                            else:
                                ch_v "Хех, ты сделал свой выбор."
                            return
            else:
                    ch_v "Ох, эм, ко мне вроде как кое-кто заглянул."
                    ch_v "Увидимся позже, ладно?"
                    $ JubesX.RecentActions.append("no summon")
                    return
    elif not ApprovalCheck(JubesX, 700, "L") or not ApprovalCheck(JubesX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(JubesX, 300):
                ch_v "Я немного занята, [JubesX.Petname]."
                $ JubesX.RecentActions.append("no summon")
                return


        if "summoned" in JubesX.RecentActions:
                pass
        elif "goto" in JubesX.RecentActions:
                if not Player.Male:
                    ch_v "Ты только что ушла!"
                else:
                    ch_v "Ты только что ушел!"
        elif JubesX.Loc == "bg classroom":
                ch_v "Я на занятиях, ты тоже хочешь прийти?"
        elif JubesX.Loc == "bg dangerroom":
                ch_v "Я в Комнате Опасности, [JubesX.Petname], хочешь прийти?"
        elif JubesX.Loc == "bg campus":
                ch_v "Я наслаждаюсь солнцем, хочешь подойти?"
        elif JubesX.Loc == "bg jubes":
                ch_v "Я в своей комнате, [JubesX.Petname], не хочешь заглянуть?"
        elif JubesX.Loc == "bg player":
                ch_v "Я в твоей комнате, [JubesX.Petname], ты собираешься возвращаться?"
        elif JubesX.Loc == "bg showerroom":
            if ApprovalCheck(JubesX, 1600):
                ch_v "Я сейчас в душе. Присоединишься?"
            else:
                ch_v "Я сейчас в душе, [JubesX.Petname]. Увидимся позже."
                $ JubesX.RecentActions.append("no summon")
                return
        elif JubesX.Loc == "hold":
                ch_v "Я сейчас немного занята. Извини?"
                $ JubesX.RecentActions.append("no summon")
                return
        else:
                ch_v "Почему бы тебе не прийти ко мне?"

        if "summoned" in JubesX.RecentActions:
                ch_v "О, ты хочешь, чтобы я вернулась так скоро?"
                $ Line = "yes"
        elif "goto" in JubesX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
#                                ch_v "Cool, see you then."
                                $ Line = "go to"
                "Нет.":
                                ch_v "Хорошо, тогда встретимся в другой раз."
                "Мне бы {i}очень{/i} хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(JubesX, 600, "L") or ApprovalCheck(JubesX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(JubesX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(JubesX, 1400):
                                #she is generally favorable
                                ch_v "Хорошо."
                                $ Line = "yes"
                        elif ApprovalCheck(JubesX, 200, "O"):
                                #she is not obedient
                                ch_v "Мне все равно, что ты там говоришь."
                                ch_v "Если передумаешь, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(JubesX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(JubesX, 1400):
                                #she is generally favorable
                                ch_v "Хорошо."
                                $ Line = "yes"
                        elif ApprovalCheck(JubesX, 200, "O"):
                                #she is not obedient
                                ch_v "Мне все равно, что ты там говоришь."
                                ch_v "Если передумаешь, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Конечно, сейчас приду.":
                    $ JubesX.Statup("Love", 55, 1)
                    $ JubesX.Statup("Inbt", 30, 1)
#                    ch_v "Cool, see you then."
                    $ Line = "go to"

                "Нет, поговорим позже.":
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Obed", 30, 2)
                    ch_v "Хорошо. Тогда увидимся в другой раз."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                    if ApprovalCheck(JubesX, 650, "L") or ApprovalCheck(JubesX, 1500):
                        $ JubesX.Statup("Love", 70, 1)
                        $ JubesX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ JubesX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                        ch_v "Оу, как я могу сказать \"нет\"?"

                "Давай, будет весело.":
                    if ApprovalCheck(JubesX, 400, "L") and ApprovalCheck(JubesX, 800):
                        $ JubesX.Statup("Love", 70, 1)
                        $ JubesX.Statup("Obed", 50, 1)
                        $ Line = "fun"
                    else:
                        $ JubesX.Statup("Inbt", 30, 1)
                        $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                    if ApprovalCheck(JubesX, 600, "O"):
                        #she is obedient
                        $ JubesX.Statup("Love", 50, 1, 1)
                        $ JubesX.Statup("Love", 40, -1)
                        $ JubesX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(JubesX, 1500):
                        #she is generally favorable
                        $ JubesX.Statup("Love", 70, -2)
                        $ JubesX.Statup("Love", 90, -1)
                        $ JubesX.Statup("Obed", 50, 2)
                        $ JubesX.Statup("Obed", 90, 1)
                        ch_v "Ладно, хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(JubesX, 200, "O"):
                        #she is not obedient
                        $ JubesX.Statup("Love", 60, -4)
                        $ JubesX.Statup("Love", 90, -3)
                        ch_v "Ни за что."
                        $ JubesX.Statup("Inbt", 40, 2)
                        $ JubesX.Statup("Inbt", 60, 1)
                        $ JubesX.Statup("Obed", 70, -3)
                        ch_v "Я остаюсь здесь."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ JubesX.Statup("Inbt", 30, 1)
                        $ JubesX.Statup("Inbt", 50, 1)
                        $ JubesX.Statup("Love", 50, -1, 1)
                        $ JubesX.Statup("Obed", 70, -1)
                        $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                    if ApprovalCheck(JubesX, 600, "O"):
                        #she is obedient
                        $ JubesX.Statup("Love", 50, 1, 1)
                        $ JubesX.Statup("Love", 40, -1)
                        $ JubesX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(JubesX, 1500):
                        #she is generally favorable
                        $ JubesX.Statup("Love", 70, -2)
                        $ JubesX.Statup("Love", 90, -1)
                        $ JubesX.Statup("Obed", 50, 2)
                        $ JubesX.Statup("Obed", 90, 1)
                        ch_v "Ладно, хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(JubesX, 200, "O"):
                        #she is not obedient
                        $ JubesX.Statup("Love", 60, -4)
                        $ JubesX.Statup("Love", 90, -3)
                        ch_v "Ни за что."
                        $ JubesX.Statup("Inbt", 40, 2)
                        $ JubesX.Statup("Inbt", 60, 1)
                        $ JubesX.Statup("Obed", 70, -3)
                        ch_v "Я остаюсь здесь."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ JubesX.Statup("Inbt", 30, 1)
                        $ JubesX.Statup("Inbt", 50, 1)
                        $ JubesX.Statup("Love", 50, -1, 1)
                        $ JubesX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if JubesX.Love > JubesX.Obed:
            ch_v "Конечно!"
        else:
            ch_v "Круто, я уже в пути."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ JubesX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            if JubesX.Loc == "bg classroom":
                ch_v "Я не могу пропустить эту лекцию."
            elif JubesX.Loc == "bg dangerroom":
                ch_v "Я только разогрелась."
            else:
                ch_v "Извини, [JubesX.Petname], я немного занята."
            $ JubesX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ JubesX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            $ Line = 0
            $ Nearby = []
            $ Party = [JubesX]
            if JubesX.Loc == "bg classroom":
                    ch_v "Лады, рядом со мной есть место."
                    jump Class_Room
            elif JubesX.Loc == "bg dangerroom":
                    ch_v "Не задерживайся. . ."
                    jump Danger_Room
            elif JubesX.Loc == "bg jubes":
                    ch_v "Я. . . приготовлюсь."
                    jump Jubes_Room
            elif JubesX.Loc == "bg player":
                    ch_v "Я буду ждать."
                    jump Player_Room
            elif JubesX.Loc == "bg showerroom":
                    ch_v "Я оставлю тебе немного горячей воды."
                    jump Shower_Room
            elif JubesX.Loc == "bg campus":
                    ch_v "Я пока посижу в тенечке. . ."
                    jump Campus
            elif JubesX.Loc != "hold":
                    ch_v "Ага, увидимся."
                    $ bg_current = JubesX.Loc
                    jump Misplaced
            else:
                    ch_v "Эм, я просто встречусь с тобой в своей комнате."
                    $ JubesX.Loc = "bg jubes"
                    jump Jubes_Room

    #She's agreed to come over
    elif Line == "lonely":
            ch_v "Оу, уже бегу!"
    elif Line == "command":
            ch_v "Ладно, [JubesX.Petname]."
    elif Line == "fun":
            ch_v "Конечно."

    if bg_current not in PersonalRooms:
            call Jubes_Sunshock
            if _return:
                    #if she couldn't go out and refused, then head back.
                    $ JubesX.RecentActions.append("no summon")
                    return

    $ JubesX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(JubesX)
            return
    $ JubesX.Loc = bg_current
    call Taboo_Level(0)
    $ JubesX.OutfitChange()
    call Set_The_Scene
    return

# End Jubes Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Jubes_Leave(Tempmod=Tempmod, GirlsNum = 0):
    if "leaving" in JubesX.RecentActions:
        $ JubesX.DrainWord("leaving")
    else:
        return

    if JubesX.Loc == "hold":
            # Activates if she's being moved out of play
            ch_v "Ладно, иди с миром."
            return

    if JubesX in Party or "lockedtravels" in JubesX.Traits:
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ JubesX.Loc = bg_current
            return

    elif "freetravels" in JubesX.Traits or not ApprovalCheck(JubesX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.
            $ JubesX.OutfitChange()
            if GirlsNum: #if someone left before her
                        ch_v "Ага, я тоже пошла."

            if JubesX.Loc == "bg classroom":
                        ch_v "У меня занятия."
            elif JubesX.Loc == "bg dangerroom":
                        ch_v "Я иду в Комнату Опасности."
            elif JubesX.Loc == "bg campus":
                        ch_v "Я собираюсь принять немного солнечных ванн."
            elif JubesX.Loc == "bg jubes":
                        ch_v "Я возвращаюсь в свою комнату."
            elif JubesX.Loc == "bg player":
                        ch_v "Я собираюсь немного побыть в твоей комнате."
            elif JubesX.Loc == "bg pool":
                        ch_v "Я иду в бассейн."
            elif JubesX.Loc == "bg showerroom":
                if ApprovalCheck(JubesX, 1400):
                        ch_v "Я иду в душ, увидимся."
                else:
                        ch_v "Я ухожу."
            else:
                        ch_v "Я ухожу, увидимся."
            hide Jubes_Sprite
            hide Jubes_Seated
            return
            #End Free Travels

    if bg_current == "bg dangerroom":
            call Gym_Exit([JubesX])

    $ JubesX.OutfitChange()

    if "follow" not in JubesX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ JubesX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    # Sets her preferences
    if JubesX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif JubesX.Loc == "bg dangerroom":
        $ Tempmod = 20
    elif JubesX.Loc == "bg showerroom":
        $ Tempmod = 40


    if GirlsNum: #if someone left before her
                ch_v "Ага, я тоже ухожу."

    if JubesX.Loc == "bg classroom":
        ch_v "У меня занятия, тебе интересно?"
    elif JubesX.Loc == "bg dangerroom":
        ch_v "У меня тренировка в Комнате Опасности, тебе интересно?"
    elif JubesX.Loc == "bg campus":
        ch_v "Я собираюсь позагорать во дворе, тебе интересно?"
    elif JubesX.Loc == "bg jubes":
        ch_v "Я возвращаюсь в свою комнату, тебе интересно?"
    elif JubesX.Loc == "bg player":
        ch_v "Я собираюсь немного побыть в твоей комнате, тебе интересно?"
    elif JubesX.Loc == "bg mall":
        ch_v "Я отправилась в торговый центр. Хочешь ко мне?"
    elif JubesX.Loc == "bg showerroom":
        if ApprovalCheck(JubesX, 1600):
            if not Player.Male:
                ch_v "Я иду в душ, ты должна присоединиться ко мне."
            else:
                ch_v "Я иду в душ, ты должен присоединиться ко мне."
        else:
            ch_v "Я иду в душ, увидимся."
            return
    elif JubesX.Loc == "bg pool":
            ch_v "Я иду в бассей. Хочешь прийти?"
    else:
            ch_v "Хочешь присоединиться ко мне?"


    menu:
        extend ""
        "Конечно, я сразу за тобой.":
                if "followed" not in JubesX.RecentActions:
                    $ JubesX.Statup("Love", 55, 1)
                    $ JubesX.Statup("Inbt", 30, 1)
                $ Line = "go to"

        "Нет, поговорим позже.":
                if "followed" not in JubesX.RecentActions:
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Obed", 30, 2)
                ch_v "Конечно, как скажешь."

        "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                if ApprovalCheck(JubesX, 650, "L") or ApprovalCheck(JubesX, 1500):
                    if "followed" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 70, 1)
                        $ JubesX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else:
                    if "followed" not in JubesX.RecentActions:
                        $ JubesX.Statup("Inbt", 30, 1)
                    $ Line = "no"
                    ch_v "Оу, как я могу сказать \"нет\"?"

        "Давай, будет весело.":
                if ApprovalCheck(JubesX, 400, "L") and ApprovalCheck(JubesX, 800):
                    $ JubesX.Statup("Love", 70, 1)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else:
                    $ JubesX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Нет, останься здесь.":
                if ApprovalCheck(JubesX, 600, "O"):
                    #she is obedient
                    if "followed" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 40, -2)
                        $ JubesX.Statup("Obed", 90, 1)
                    $ Line = "command"

                elif D20 >= 7 and ApprovalCheck(JubesX, 1400):
                    #she is generally favorable
                    if "followed" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 70, -2)
                        $ JubesX.Statup("Love", 90, -1)
                        $ JubesX.Statup("Obed", 50, 2)
                        $ JubesX.Statup("Obed", 90, 1)
                    ch_v "Думаю, можно. . ."
                    $ Line = "yes"

                elif ApprovalCheck(JubesX, 200, "O"):
                    #she is not obedient
                    if "followed" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 70, -4)
                        $ JubesX.Statup("Love", 90, -2)
                    ch_v "Ни за что."
                    if "followed" not in JubesX.RecentActions:
                        $ JubesX.Statup("Inbt", 40, 2)
                        $ JubesX.Statup("Inbt", 60, 1)
                        $ JubesX.Statup("Obed", 70, -2)
                    ch_v "Я остаюсь здесь."
                else:
                    #she is obedient, but you failed to meet the checks
                    if "followed" not in JubesX.RecentActions:
                        $ JubesX.Statup("Inbt", 30, 1)
                        $ JubesX.Statup("Inbt", 50, 1)
                        $ JubesX.Statup("Love", 50, -1, 1)
                        $ JubesX.Statup("Love", 90, -2)
                        $ JubesX.Statup("Obed", 70, -1)
                    $ Line = "no"
                #End ordered to stay

    call Taboo_Level(0)
    $ JubesX.RecentActions.append("followed")
    if not Line:
            #You end the dialog neutrally
            hide Jubes_Sprite
            hide Jubes_Seated
            call Gym_Clothes_Off([JubesX])
            return

    if Line == "no":
            # She's refused, context based dialog
            if JubesX.Loc == "bg classroom":
                ch_v "Я никак не могу это пропустить."
            elif JubesX.Loc == "bg dangerroom":
                ch_v "Извини, [JubesX.Petname], мне нужно позаниматься."
            else:
                ch_v "Извини, я немного занята."
            hide Jubes_Sprite
            hide Jubes_Seated
            call Gym_Clothes_Off([JubesX])
            return

    elif Line == "go to":
            #You agreed to go to her instead
            #$ Party.append(JubesX)
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")
            $ JubesX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            hide Jubes_Sprite
            hide Jubes_Seated
            $ Nearby = []
            $ Party = [JubesX]
            call Gym_Clothes_Off([JubesX])
            if JubesX.Loc == "bg classroom":
                ch_v "Ладно, тогда пошевеливайся."
                jump Class_Room_Entry
            elif JubesX.Loc == "bg dangerroom":
                ch_v "Я пока разогреюсь."
                jump Danger_Room_Entry
            elif JubesX.Loc == "bg jubes":
                ch_v "Ладно."
                jump Jubes_Room
            elif JubesX.Loc == "bg player":
                ch_v "Хорошо."
                jump Player_Room
            elif JubesX.Loc == "bg showerroom":
                ch_v "Ладно, хорошо."
                jump Shower_Room_Entry
            elif JubesX.Loc == "bg campus":
                ch_v "Ладно, хорошо."
                jump Campus_Entry
            elif JubesX.Loc == "bg pool":
                ch_v "Классно."
                jump Pool_Entry
            elif JubesX.Loc == "bg mall":
                ch_v "Классно."
                jump Mall_Entry
            else:
                ch_v "Я просто встречусь с тобой в твоей комнате."
                $ JubesX.Loc = "bg player"
                jump Player_Room
            #End "goto" where she's at

    #She's agreed to come over
    elif Line == "lonely":
            ch_v "Оу, что ж, я могу помочь с этим!"
    elif Line == "command":
            ch_v "Ладно, [JubesX.Petname]."
    elif Line:
            ch_v "Конечно."

    $ Line = 0
    ch_v "Я останусь здесь."
    $ JubesX.Loc = bg_current
    call Taboo_Level(0)
    return

# End Jubes Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

### Jubes's Clothes  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_Clothes:
    if JubesX.Taboo:
            if "exhibitionist" in JubesX.Traits:
                ch_v "Да? . ."
            elif ApprovalCheck(JubesX, 900, TabM=4) or ApprovalCheck(JubesX, 400, "I", TabM=3):
                ch_v "Здесь довольно людно, я пас. . ."
            else:
                ch_v "Здесь довольно людно. . ."
                ch_v "Разве мы не можем поговорить об этом в наших комнатах?"
                return
    elif ApprovalCheck(JubesX, 900, TabM=4) or ApprovalCheck(JubesX, 600, "L") or ApprovalCheck(JubesX, 300, "O"):
                if not Player.Male:
                    ch_v "Ох, что именно хочешь обсудить? . ."
                else:
                    ch_v "Ох, что именно хочешь обсудить? . ."
    else:
                ch_v "Я не думаю, что мне так нужны твои советы по моде."
                return

    if Girl != JubesX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = JubesX
    call Shift_Focus(Girl)

label Jubes_Wardrobe_Menu:
    $ JubesX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .
    while True:
        menu:
            ch_v "Что насчет моей одежды?"
            "Верх":
                        call Jubes_Clothes_Over
            "Низ":
                        call Jubes_Clothes_Legs
            "Нижнее белье":
                        call Jubes_Clothes_Under
            "Аксессуары":
                        call Jubes_Clothes_Misc
            "Управление нарядами":
                        call Jubes_Clothes_Outfits
            "Давай поговорим о том, что ты носишь.":
                        call Clothes_Schedule(JubesX)

            "Могу я посмотреть?" if JubesX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(JubesX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_v "Ладно, так хорошо?"
                    hide PhoneSex
            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(JubesX,0,2)
                    if _return:
                        hide DressScreen
            "Может, тебе будет комфортнее за ширмой? (locked)" if JubesX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if JubesX.Loc == bg_current and not JubesX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if not Player.Male and "girltalk" not in JubesX.History and "nogirls" not in JubesX.History:
                            ch_v "Я не понимаю, зачем она нужна."
                    elif ApprovalCheck(JubesX, 1500) or (JubesX.SeenChest and JubesX.SeenPussy):
                            ch_v "Думаю, мне и так хорошо. . ."
                    else:
                            show DressScreen zorder 150
                            ch_v "Да, так будет лучше, спасибо."

            "У меня есть подарок для тебя (locked)" if JubesX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if JubesX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(JubesX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ JubesX.OutfitChange()
                    $ JubesX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != JubesX:
                            ch_p "Я хочу поговорить о твоей одежде."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = JubesX
                    call Shift_Focus(Girl)

            "Сменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current:
                    pass
            "Сменить вид" if Girl.Loc == bg_current:
                    call WardrobeView(JubesX)

            "Неважно, ты и так хорошо выглядишь":
                    call Girl_Pos_Reset(JubesX)
                    if "wardrobe" not in JubesX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if JubesX.Chat[1] <= 1:
                                    $ JubesX.Statup("Love", 70, 15)
                                    $ JubesX.Statup("Obed", 40, 20)
                                    ch_v "О! Спасибо."
                            elif JubesX.Chat[1] <= 10:
                                    $ JubesX.Statup("Love", 70, 5)
                                    $ JubesX.Statup("Obed", 40, 7)
                                    ch_v "Правда?"
                            elif JubesX.Chat[1] <= 50:
                                    $ JubesX.Statup("Love", 70, 1)
                                    $ JubesX.Statup("Obed", 40, 1)
                                    ch_v "Угу."
                            else:
                                    ch_v "Конечно."
                            $ JubesX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(JubesX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ JubesX.OutfitChange()
                    $ JubesX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ JubesX.Chat[1] += 1
                    $ Trigger = 0
                    if JubesX.Panties and "pantyless" in JubesX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ JubesX.DailyActions.remove("pantyless")
                    return

        #Loops back up
        #return #jump Jubes_Clothes
        #End of Jubes Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jubes_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(JubesX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(JubesX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(JubesX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(JubesX,4,1)
                    "Одежда для сна":
                                call OutfitShame(JubesX,7,1)
                    "Купальник":
                                call OutfitShame(JubesX,10,1)

                    "Повседневка 1" if ApprovalCheck(JubesX, 2500):
                                call OutfitShame(JubesX,11,1)
                    "Повседневка 2" if ApprovalCheck(JubesX, 2500):
                                call OutfitShame(JubesX,12,1)
                    #8 is Emma's teaching clothes,
                    "Неважно":
                                pass

        "Примерь красно-синий наряд":
                $ JubesX.OutfitChange("casual1")
                menu:
                    "Ты должна носить его. [[Выбрать текущий наряд]":
                            $ JubesX.Outfit = "casual1"
                            $ JubesX.Shame = 0
                            if not Player.Male:
                                ch_v "Ага, это же классика, согласна?"
                            else:
                                ch_v "Ага, это же классика, согласен?"
                    "Давай попробуем что-нибудь другое.":
                            ch_v "Ладно."

        "Примерь черный кожаный комплект":
                $ JubesX.OutfitChange("casual2")
                menu:
                    "Ты должна носить его. [[Выбрать текущий наряд]":
                            $ JubesX.Outfit = "casual2"
                            $ JubesX.Shame = 0
                            ch_v "Я знаю, что он немного старомоден и все такое, но мне нравится!"
                    "Давай попробуем что-нибудь другое.":
                            ch_v "Ладно."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not JubesX.Custom1[0] and not JubesX.Custom2[0] and not JubesX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if JubesX.Custom1[0] or JubesX.Custom2[0] or JubesX.Custom3[0]:
                $ Cnt = 0
                while 1:
                    menu:
                        "Надень Пользовательский 1 (locked)" if not JubesX.Custom1[0]:
                                pass
                        "Надень Пользовательский 1" if JubesX.Custom1[0]:
                                $ JubesX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Надень Пользовательский 2 (locked)" if not JubesX.Custom2[0]:
                                pass
                        "Надень Пользовательский 2" if JubesX.Custom2[0]:
                                $ JubesX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Надень Пользовательский 3 (locked)" if not JubesX.Custom3[0]:
                                pass
                        "Надень Пользовательский 3" if JubesX.Custom3[0]:
                                $ JubesX.OutfitChange("custom3")
                                $ Cnt = 6

                        "Ты должна одеваться так, когда мы наедине (locked)" if not Cnt:
                                pass
                        "Ты должна одеваться так, когда мы наедине" if Cnt:
                                if Cnt == 5:
                                    $ JubesX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ JubesX.Clothing[9] = "custom3"
                                else:
                                    $ JubesX.Clothing[9] = "custom1"
                                ch_v "Хорошо, конечно."

                        "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                menu:
                                    "Пользовательский 1 [[очистить слот 1]" if JubesX.Custom1[0]:
                                        ch_v "Ладно."
                                        $ JubesX.Custom1[0] = 0
                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not JubesX.Custom1[0]:
                                        pass
                                    "Пользовательский 2 [[очистить слот 2]" if JubesX.Custom2[0]:
                                        ch_v "Ладно."
                                        $ JubesX.Custom2[0] = 0
                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not JubesX.Custom2[0]:
                                        pass
                                    "Пользовательский 3 [[очистить слот 3]" if JubesX.Custom3[0]:
                                        ch_v "Ладно."
                                        $ JubesX.Custom3[0] = 0
                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not JubesX.Custom3[0]:
                                        pass
                                    "Неважно [[назад]":
                                        pass

                        "Тебе следует надеть его [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                pass
                        "Тебе следует надеть его" if Cnt:
                                call Custom_Out(JubesX,Cnt)
                        "Ладно, вернемся к началу нашего разговора. . .":
                                $ Cnt = 0
                                return #jump Jubes_Clothes

        "Наденешь спортивную одежду?" if not JubesX.Taboo or bg_current == "bg dangerroom":
                $ JubesX.OutfitChange("gym")

        "Наденешь одежду для сна?" if not JubesX.Taboo:
                if ApprovalCheck(JubesX, 1200):
                        $ JubesX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(JubesX)
                        if _return:
                            $ JubesX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (JubesX.Taboo and bg_current != "bg pool" and not ApprovalCheck(JubesX, 800, TabM=2)) or not JubesX.Swim[0]:
                $ JubesX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not JubesX.Taboo or bg_current == "bg pool" or ApprovalCheck(JubesX, 800, TabM=2)) and JubesX.Swim[0]:
                $ JubesX.OutfitChange("swimwear")

        "Наденешь хэллоуинский костюм?" if "halloween" in JubesX.History:
                if JubesX.Taboo <= 20 or JubesX in Rules:
                        ch_v "Хорошо."
                        $ JubesX.OutfitChange("costume")
                elif ApprovalCheck(JubesX, 1100, TabM=3):
                        ch_v "Ладно."
                        $ JubesX.OutfitChange("costume")
                else:
                        call Display_DressScreen(JubesX)
                        if not _return:
                                ch_v "Эм, здесь? . ."
                        else:
                                $ JubesX.OutfitChange("costume")
                if "stockings and garterbelt" not in JubesX.Inventory:
                        $ JubesX.Hose = "stockings"
                if "lace bra" not in JubesX.Inventory:
                        $ JubesX.Chest = "sports bra"
                if "lace panties" not in JubesX.Inventory:
                        $ JubesX.Panties = "blue panties"

        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ JubesX.FaceChange("sexy", 1)
                $ Line = 0
                if not JubesX.Chest and not JubesX.Panties and not JubesX.Over and not JubesX.Legs and not JubesX.Hose:
                    ch_v "Угу-м. . . подожди, откуда ты знаешь?!"
                elif JubesX.SeenChest and JubesX.SeenPussy and ApprovalCheck(JubesX, 1200, TabM=4):
                    ch_v ". . . да?"
                    $ Line = 1
                elif ApprovalCheck(JubesX, 2000, TabM=4):
                    ch_v "О, ты переходишь сразу к делу!"
                    $ Line = 1
                elif JubesX.SeenChest and JubesX.SeenPussy and ApprovalCheck(JubesX, 1200, TabM=0):
                    ch_v "Возмооожно, но не здесь. . ."
                elif ApprovalCheck(JubesX, 2000, TabM=0):
                    ch_v "Возмооожно, но не здесь. . ."
                elif ApprovalCheck(JubesX, 1000, TabM=0):
                    $ JubesX.FaceChange("confused", 1,Mouth="smirk")
                    ch_v "Ага, но ты этого не увидишь. . ."
                    $ JubesX.FaceChange("bemused", 0)
                else:
                    $ JubesX.FaceChange("angry", 1)
                    ch_v "Это тебя не касается!"

                call expression JubesX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in JubesX.History:
                        $ Line = 0
                if Line:
                    #If she got nude. . .
                    $ JubesX.OutfitChange("nude")
                    "Она сбрасывает одежду к своим ногам."
                    call Girl_First_Topless(JubesX)
                    call Girl_First_Bottomless(JubesX,1)
                    $ JubesX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется. что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in JubesX.Traits:
                                ch_v "Мммм. . ."
                                $ JubesX.Outfit = "nude"
                                $ JubesX.Statup("Lust", 50, 10)
                                $ JubesX.Statup("Lust", 70, 5)
                                $ JubesX.Shame = 50
                            elif ApprovalCheck(JubesX, 800, "I") or ApprovalCheck(JubesX, 2800, TabM=0):
                                ch_v "Забавно. . ."
                                $ JubesX.Outfit = "nude"
                                $ JubesX.Shame = 50
                            else:
                                $ JubesX.FaceChange("sexy", 1)
                                $ JubesX.Eyes = "surprised"
                                ch_v "Я этого совсем не хочу."

                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in JubesX.Traits:
                                ch_v "Серьезно?"
                            elif ApprovalCheck(JubesX, 800, "I") or ApprovalCheck(JubesX, 2800, TabM=0):
                                $ JubesX.FaceChange("bemused", 1)
                                ch_v "О! Я думала, ты хочешь, чтобы я ходила так. . ."
                                ch_v ". . ."
                            else:
                                $ JubesX.FaceChange("confused", 1)
                                ch_v "Ага, то есть, я бы не стала так ходить, конечно. . ."
                $ Line = 0

        "Неважно":
            return #jump Jubes_Clothes

    return #jump Jubes_Clothes
    #End of Jubes Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jubes_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять куртку?" if JubesX.Acc:
                $ JubesX.FaceChange("bemused", 1)
                if JubesX.Over or (ApprovalCheck(JubesX, 800, TabM=3) and (JubesX.Chest or JubesX.SeenChest)):
                    #if she has a shirt on, or a bra and is a bit loose about it
                    ch_v "Конечно."
                elif ApprovalCheck(JubesX, 600, TabM=0):
                    call Jubes_NoBra
                    if not _return:
                        if not ApprovalCheck(JubesX, 1200):
                            call Display_DressScreen(JubesX)
                            if not _return:
                                return #jump Jubes_Clothes
                        else:
                                return #jump Jubes_Clothes
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            ch_v "Не сейчас."
                            if not JubesX.Chest:
                                ch_v "У меня под ней ничего нет. . ."
                            return #jump Jubes_Clothes
                $ JubesX.Acc = 0
                "Она скидывает куртку к своим ногам."
                if not renpy.showing('DressScreen'):
                        call Girl_First_Topless(JubesX)

        "Почему бы тебе не снять [get_clothing_name(JubesX.Over_key, vin)]?" if JubesX.Over:
                call Wardrobe_Remove(JubesX)

        "Примерь желтую куртку." if not JubesX.Acc:
                $ JubesX.FaceChange("bemused")
                ch_v "Конечно."
                $ JubesX.Acc = "jacket"

        "Может, тебе стоит приоткрыть куртку?" if JubesX.Acc and JubesX.Acc != "open jacket":
                $ JubesX.FaceChange("bemused")
                if JubesX.Over or (ApprovalCheck(JubesX, 800, TabM=3) and (JubesX.Chest or JubesX.SeenChest)):
                    #if she has a shirt on, or a bra and is a bit loose about it
                    ch_v "Конечно."
                elif ApprovalCheck(JubesX, 600, TabM=0):
                    call Jubes_NoBra
                    if not _return:
                        if not ApprovalCheck(JubesX, 1200):
                            call Display_DressScreen(JubesX)
                            if not _return:
                                return #jump Jubes_Clothes
                        else:
                                return #jump Jubes_Clothes
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            ch_v "Не сейчас."
                            if not JubesX.Chest:
                                ch_v "У меня под ней ничего нет. . ."
                            return #jump Jubes_Clothes
                $ JubesX.Acc = "open jacket"
                if not renpy.showing('DressScreen'):
                        call Girl_First_Topless(JubesX)

        "Может, тебе стоит поправить куртку?" if JubesX.Acc and JubesX.Acc != "jacket":
                $ JubesX.FaceChange("bemused")
                if JubesX.Over or (ApprovalCheck(JubesX, 800, TabM=3) and (JubesX.Chest or JubesX.SeenChest)):
                    #if she has a shirt on, or a bra and is a bit loose about it
                    ch_v "Конечно."
                elif ApprovalCheck(JubesX, 600, TabM=0):
                    call Jubes_NoBra
                    if not _return:
                        if not ApprovalCheck(JubesX, 1200):
                            call Display_DressScreen(JubesX)
                            if not _return:
                                return #jump Jubes_Clothes
                        else:
                                return #jump Jubes_Clothes
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            ch_v "Не сейчас."
                            if not JubesX.Chest:
                                ch_v "У меня под ней ничего нет. . ."
                            return #jump Jubes_Clothes
                $ JubesX.Acc = "jacket"
                if not renpy.showing('DressScreen'):
                        call Girl_First_Topless(JubesX)

        "Может, застегнешь куртку на молнию?" if JubesX.Acc and JubesX.Acc != "shut jacket":
                $ JubesX.FaceChange("bemused")
                ch_v "Конечно."
                $ JubesX.Acc = "shut jacket"

        "Примерь красную рубашку." if JubesX.Over != "red shirt":
                $ JubesX.FaceChange("bemused")
                if not JubesX.Over:
                    #if she's not already wearing a top
                    ch_v "Конечно."
                elif ApprovalCheck(JubesX, 800, TabM=0):
                    ch_v "Ага, ладно."
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            $ JubesX.FaceChange("bemused", 1)
                            ch_v "Я совсем не хочу сейчас переодевать [get_clothing_name(JubesX.Over_key, vin)]."
                            return #jump Jubes_Clothes
                $ JubesX.Over = "red shirt"

        "Примерь кожаную рубашку." if JubesX.Over != "black shirt":
                $ JubesX.FaceChange("bemused")
                if not JubesX.Over:
                    #if she's not already wearing a top
                    ch_v "Конечно."
                elif ApprovalCheck(JubesX, 800, TabM=0):
                    ch_v "Ага, ладно."
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            $ JubesX.FaceChange("bemused", 1)
                            ch_v "Я совсем не хочу сейчас переодевать [get_clothing_name(JubesX.Over_key, vin)]."
                            return #jump Jubes_Clothes
                $ JubesX.Over = "black shirt"

        "Примерь розовый топик." if JubesX.Over != "tube top":
                $ JubesX.FaceChange("bemused")
                if not JubesX.Over:
                    #if she's not already wearing a top
                    ch_v "Конечно."
                elif ApprovalCheck(JubesX, 800, TabM=0):
                    ch_v "Ага, ладно."
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            $ JubesX.FaceChange("bemused", 1)
                            ch_v "Я совсем не хочу сейчас переодевать [get_clothing_name(JubesX.Over_key, vin)]."
                            return #jump Jubes_Clothes
                $ JubesX.Over = "tube top"

        "Примерь красное платье." if JubesX.Over != "dress" and "halloween" in JubesX.History:
                $ JubesX.FaceChange("bemused")
                if not JubesX.Over:
                    #if she's not already wearing a top
                    ch_v "Конечно."
                elif ApprovalCheck(JubesX, 800, TabM=0):
                    ch_v "Ага, ладно."
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            $ JubesX.FaceChange("bemused", 1)
                            ch_v "Я совсем не хочу сейчас переодевать [get_clothing_name(JubesX.Over_key, vin)]."
                            return #jump Jubes_Clothes
                $ JubesX.Over = "dress"

        "Может, просто накинешь полотенце?" if JubesX.Over != "towel":
                $ JubesX.FaceChange("bemused", 1)
                if JubesX.Chest or JubesX.SeenChest:
                    ch_v "Странный выбор."
                elif ApprovalCheck(JubesX, 1000, TabM=0):
                    $ JubesX.FaceChange("perplexed", 1)
                    ch_v "Эм, конечно . ."
                else:
                    call Display_DressScreen(JubesX)
                    if not _return:
                            ch_v "Неее."
                            return #jump Jubes_Clothes
                $ JubesX.Over = "towel"

        "Неважно":
            pass
    return #jump Jubes_Clothes
    #End of Jubes Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Jubes_NoBra:
        menu:
            ch_v "У меня под [get_clothing_name(JubesX.Over_key, tvo)] совсем ничего нет. . ."
            "Тогда надень что-нибудь. . .":
                        if JubesX.SeenChest and ApprovalCheck(JubesX, 1000, TabM=3):
                                $ JubesX.Blush = 1
                                ch_v "Ох, я просто предупредила -тебя-. . ."
                                $ JubesX.Blush = 0
                        elif ApprovalCheck(JubesX, 1200, TabM=4):
                                $ JubesX.Blush = 1
                                ch_v "Ох, я просто предупредила -тебя-. . ."
                                $ JubesX.Blush = 0
                        elif ApprovalCheck(JubesX, 900, TabM=2) and "lace bra" in JubesX.Inventory:
                                ch_v "Нууу, у меня есть кое-что, что я могла бы надеть. . ."
                                $ JubesX.Chest  = "lace bra"
                                "Она достает кружевной лифчик и надевает его под [get_clothing_name(JubesX.Over_key, vin)]."
                        elif ApprovalCheck(JubesX, 600, TabM=2):
                                ch_v "Нууу, у меня есть кое-что, что я могла бы надеть. . ."
                                $ JubesX.Chest = "sports bra"
                                "Она достает спортивный лифчик и надевает его под [get_clothing_name(JubesX.Over_key, vin)]."
                        else:
                                ch_v "Ага, это не поможет."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(JubesX, 1100, "LI", TabM=2) and JubesX.Love > JubesX.Inbt:
                                ch_v "Для тебя? Конечно. . ."
                        elif ApprovalCheck(JubesX, 700, "OI", TabM=2) and JubesX.Obed > JubesX.Inbt:
                                ch_v "Конечно. . ."
                        elif ApprovalCheck(JubesX, 600, "I", TabM=2):
                                ch_v "Ага. . ."
                        elif ApprovalCheck(JubesX, 1300, TabM=2):
                                ch_v "Ладно, все нормально."
                        else:
                                $ JubesX.FaceChange("surprised")
                                $ JubesX.Brows = "angry"
                                if JubesX.Taboo > 20:
                                    ch_v "Мы же на людях!"
                                else:
                                    ch_v "Неее."
                                call expression JubesX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0
            "Неважно.":
                        ch_v "Ладно. . ."
                        return 0
        return 1
        #End of Jubes bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jubes_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(JubesX.Legs_key, vin)]?" if JubesX.Legs:
                call Wardrobe_Remove(JubesX,1)

        "Примерь кожаные брюки" if JubesX.Legs != "pants":
                ch_p "Тебе идут твои кожанные брюки."
                ch_v "Ага, ладно."
                $ JubesX.Legs = "pants"

        "Примерь джинсовые шорты" if JubesX.Legs != "shorts":
                ch_p "Как насчет того, чтобы надеть джинсовые шорты?"
                ch_v "Конечно, почему бы и нет."
                $ JubesX.Legs = "shorts"

        "Примерь красную юбку" if JubesX.Legs != "skirt" and "halloween" in JubesX.History:
                ch_p "Как насчет того, чтобы надеть красную юбку?"
                ch_v "Конечно, почему бы и нет."
                $ JubesX.Legs = "skirt"

        "Сними обувь (locked)" if not JubesX.Boots:
                pass
        "Сними [get_clothing_name(JubesX.Boots_key, vin)]" if JubesX.Boots:
                ch_p "Может, снимешь [get_clothing_name(JubesX.Boots_key, vin)]?"
                ch_v "Конечно."
                $ JubesX.Boots = 0
#        "Add Boots" if JubesX.Boots != "boots":
#                ch_p "Maybe put your boots on."
#                ch_v "Sure."
#                $ JubesX.Boots = "boots"
        "Надень кеды" if JubesX.Boots != "sneaks":
                ch_p "Может, наденешь кеды?"
                ch_v "Конечно."
                $ JubesX.Boots = "sneaks"

        "Неважно":
                pass
    return #jump Jubes_Clothes
    #End of Jubes Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Jubes_NoPantiesOn:
        menu:
            ch_v "На самом деле, на мне нет трусиков."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if JubesX.SeenPussy and ApprovalCheck(JubesX, 1100, TabM=4):
                                $ JubesX.Blush = 1
                                ch_v "Нет, нет, все в порядке. . ."
                                $ JubesX.Blush = 0
                        elif ApprovalCheck(JubesX, 1500, TabM=4):
                                $ JubesX.Blush = 1
                                ch_v "Нет, нет, все в порядке. . ."
                                $ JubesX.Blush = 0
                        elif ApprovalCheck(JubesX, 700, TabM=4):
                                ch_v "Это я могу, наверное. . ."
                                if "lace panties" in JubesX.Inventory:
                                        $ JubesX.Panties  = "lace panties"
                                else:
                                        $ JubesX.Panties = "blue panties"
                                if ApprovalCheck(JubesX, 1200, TabM=4):
                                        $ Line = get_clothing_name(JubesX.Legs_key, vin)
                                        $ JubesX.Legs = 0
                                        "Она снимает [Line] и надевает [get_clothing_name(JubesX.Panties_key, vin)]."
                                elif JubesX.Legs == "skirt":
                                        "Она достает  [get_clothing_name(JubesX.Panties_key, vin)] и надевает их под юбку."
                                        $ JubesX.Legs = 0
                                        "Затем она сбрасывает юбку на пол."
                                else:
                                        $ Line = get_clothing_name(JubesX.Legs_key, vin)
                                        $ JubesX.Legs = 0
                                        "Она отходит на мгновение, а затем возвращается в [get_clothing_name(JubesX.Panties_key, pre)]."
                                return #jump Jubes_Clothes
                        else:
                                ch_v "Не-а."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(JubesX, 1100, "LI", TabM=3) and JubesX.Love > JubesX.Inbt:
                                ch_v "Верно. . ."
                        elif ApprovalCheck(JubesX, 700, "OI", TabM=3) and JubesX.Obed > JubesX.Inbt:
                                ch_v "Конечно. . ."
                        elif ApprovalCheck(JubesX, 600, "I", TabM=3):
                                ch_v "Хммм. . ."
                        elif ApprovalCheck(JubesX, 1300, TabM=3):
                                ch_v "Хорошо."
                        else:
                                $ JubesX.FaceChange("surprised")
                                $ JubesX.Brows = "angry"
                                if JubesX.Taboo > 20:
                                    ch_v "Ага, но не на людях, [JubesX.Petname]!"
                                else:
                                    ch_v "Неее."
                                call expression JubesX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно.":
                ch_v "Ладно. . ."
                return 0
        return 1
        #End of Jubes Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jubes_Clothes_Under:
        "Верх":
            menu:
                "Может, снимешь [get_clothing_name(JubesX.Chest_key, vin)]?" if JubesX.Chest:
                        $ JubesX.FaceChange("bemused", 1)
                        if JubesX.SeenChest and ApprovalCheck(JubesX, 900, TabM=2.7):
                            ch_v "Конечно."
                        elif ApprovalCheck(JubesX, 1100, TabM=2):
                            if JubesX.Taboo:
                                ch_v "Что-то мне не хочется делать это здесь. . ."
                            else:
                                ch_v "Возмооожно. . ."
                        elif JubesX.Acc == "jacket" and ApprovalCheck(JubesX, 600, TabM=2):
                            ch_v "Тогда куртка почти ничего не будет прикрывать. . ."
                        elif JubesX.Over and ApprovalCheck(JubesX, 500, TabM=2):
                            ch_v "Думаю, можно. . ."
                        elif not JubesX.Over:
                            call Display_DressScreen(JubesX)
                            if not _return:
                                ch_v "Нет, без верхней одежды не буду. . ."
                                return #jump Jubes_Clothes
                        else:
                            call Display_DressScreen(JubesX)
                            if not _return:
                                ch_v "Неее."
                                return #jump Jubes_Clothes
                        $ Line = get_clothing_name(JubesX.Chest_key, vin)
                        $ JubesX.Chest = 0
                        if JubesX.Acc:
                            "Она лезет под куртку, хватает и снимает [Line], а затем кидает на пол."
                        elif JubesX.Over:
                            "Она залезает под [get_clothing_name(JubesX.Over_key, vin)], хватает и снимает [Line], а затем кидает на пол."
                        else:
                            "Она снимает [Line] и кидает на пол."
                            if not renpy.showing('DressScreen'):
                                call Girl_First_Topless(JubesX)

                "Примерь спортивный лифчик" if JubesX.Chest != "sports bra":
                        ch_p "Примерь спортивный лифчик."
                        ch_v "Ладно."
                        $ JubesX.Chest = "sports bra"

                "Примерь кружевной лифчик" if JubesX.Chest != "lace bra" and "lace bra" in JubesX.Inventory:
                        ch_p "Мне нравится твой лифчик-корсет."
                        if JubesX.SeenChest or ApprovalCheck(JubesX, 1300, TabM=2):
                            ch_v "Лады."
                            $ JubesX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(JubesX)
                            if not _return:
                                ch_v "Он довольно откровенный. . ."
                            else:
                                $ JubesX.Chest = "lace bra"

                "Примерь лифчик бикини" if JubesX.Chest != "bikini top" and "bikini top" in JubesX.Inventory:
                        ch_p "Мне нравится твой лифчик бикини."
                        if bg_current == "bg pool":
                                ch_v "Лады."
                                $ JubesX.Chest = "bikini top"
                        else:
                                if JubesX.SeenChest or ApprovalCheck(JubesX, 1000, TabM=2):
                                    ch_v "Лады."
                                    $ JubesX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(JubesX)
                                    if not _return:
                                            ch_v "Это не совсем подходящее место для \"бикини\". . ."
                                    else:
                                            $ JubesX.Chest = "bikini top"
                "Неважно":
                        pass
            return #jump Jubes_Clothes_Under

        "Варианты колготок и чулок":
            menu:
                "Сними [get_clothing_name(JubesX.Hose_key, vin)]." if JubesX.Hose:
                                $ JubesX.Hose = 0
                "Чулки дополнили бы твой образ." if JubesX.Hose != "stockings":
                                $ JubesX.Hose = "stockings"
                "Колготки дополнили бы твой образ." if JubesX.Hose != "pantyhose" and "pantyhose" in JubesX.Inventory:
                                $ JubesX.Hose = "pantyhose"
                "Рваные колготки дополнили бы твой образ." if JubesX.Hose != "ripped pantyhose" and "ripped pantyhose" in JubesX.Inventory:
                                $ JubesX.Hose = "ripped pantyhose"
                "Высокие носки дополнили бы твой образ." if JubesX.Hose != "socks" and "socks" in JubesX.Inventory:
                                $ JubesX.Hose = "socks"
                "Чулки и пояс с подвязками дополнили бы твой образ." if JubesX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in JubesX.Inventory:
                                $ JubesX.Hose = "stockings and garterbelt"
                "Может, наденешь только пояс с подвязками?" if JubesX.Hose != "garterbelt" and "stockings and garterbelt" in JubesX.Inventory:
                                $ JubesX.Hose = "garterbelt"
                "Неважно":
                        pass
            return #jump Jubes_Clothes_Under

        #Panties
        "Низ":
            menu:
                "Ты должна снять [get_clothing_name(JubesX.Panties_key, vin)]. . ." if JubesX.Panties:
                        $ JubesX.FaceChange("bemused", 1)
                        if ApprovalCheck(JubesX, 900) and (JubesX.Legs or (JubesX.SeenPussy and not JubesX.Taboo)):
                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                                if ApprovalCheck(JubesX, 850, "L"):
                                        ch_v "Верно. . ."
                                elif ApprovalCheck(JubesX, 500, "O"):
                                        ch_v "Точно. . ."
                                elif ApprovalCheck(JubesX, 350, "I"):
                                        ch_v "Хех."
                                else:
                                        ch_v "Конечно, наверное."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(JubesX, 1100, "LI", TabM=3) and JubesX.Love > JubesX.Inbt:
                                        ch_v "Я не уверена, здесь вроде как людно. . ."
                                elif ApprovalCheck(JubesX, 700, "OI", TabM=3) and JubesX.Obed > JubesX.Inbt:
                                        ch_v "Хорошо. . ."
                                elif ApprovalCheck(JubesX, 600, "I", TabM=3):
                                        ch_v "Хммм. . ."
                                elif ApprovalCheck(JubesX, 1300, TabM=3):
                                        ch_v "Ладно, хорошо."
                                else:
                                        call Display_DressScreen(JubesX)
                                        if not _return:
                                            $ JubesX.FaceChange("surprised")
                                            $ JubesX.Brows = "angry"
                                            if JubesX.Taboo > 20:
                                                ch_v "Здесь слишком людно."
                                            else:
                                                ch_v "Неее."
                                            return #jump Jubes_Clothes
                        $ Line = get_clothing_name(JubesX.Panties_key, vin)
                        $ JubesX.Panties = 0
                        if not JubesX.Legs:
                            "Она стягивает свои [Line], затем бросает их на пол."
                            if not renpy.showing('DressScreen'):
                                    call Girl_First_Bottomless(JubesX)
                        elif ApprovalCheck(JubesX, 1200, TabM=4):
                            $ Trigger = JubesX.Legs
                            $ JubesX.Legs = 0
                            pause 0.5
                            $ JubesX.Legs = Trigger
                            "Она снимает [get_clothing_name(JubesX.Legs_key, vin)] и [Line], затем снова надевает [get_clothing_name(JubesX.Legs_key, vin)]."
                            $ Trigger = 1
                            call Girl_First_Bottomless(JubesX,1)
                        elif JubesX.Legs == "skirt":
                            "Она лезет под юбку и снимает [Line]."
                        else:
                            $ JubesX.Blush = 1
                            "Она на мгновение отходит, а затем возвращается."
                            $ JubesX.Blush = 0
                        $ Line = 0

                "Почему бы тебе вместо этих не надеть синие трусики?" if JubesX.Panties and JubesX.Panties != "blue panties":
                        if ApprovalCheck(JubesX, 1100, TabM=3):
                                ch_v "Ладно."
                                $ JubesX.Panties = "blue panties"
                        else:
                                call Display_DressScreen(JubesX)
                                if not _return:
                                        ch_v "Не лезь не в своей дело."
                                else:
                                        $ JubesX.Panties = "blue panties"

                "Почему бы тебе вместо этих не надеть кружевные трусики?" if "lace panties" in JubesX.Inventory and JubesX.Panties and JubesX.Panties != "lace panties":
                        if ApprovalCheck(JubesX, 1300, TabM=3):
                                ch_v "Можно."
                                $ JubesX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(JubesX)
                                if not _return:
                                        ch_v "Не лезь не в своей дело."
                                else:
                                        $ JubesX.Panties = "lace panties"

                "Почему бы тебе вместо этих не надеть трусики в тигровую полоску?" if "tiger panties" in JubesX.Inventory and JubesX.Panties and JubesX.Panties != "tiger panties":
                        if ApprovalCheck(JubesX, 1300, TabM=3):
                                ch_v "Можно."
                                $ JubesX.Panties = "tiger panties"
                        else:
                                call Display_DressScreen(JubesX)
                                if not _return:
                                        ch_v "Не лезь не в своей дело."
                                else:
                                        $ JubesX.Panties = "tiger panties"

                "Мне нравятся твои трусики бикини." if "bikini bottoms" in JubesX.Inventory and JubesX.Panties != "bikini bottoms":
                        if bg_current == "bg pool":
                                ch_v "Лады."
                                $ JubesX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(JubesX, 1000, TabM=2):
                                    ch_v "Лады."
                                    $ JubesX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(JubesX)
                                    if not _return:
                                            ch_v "Это не совсем подходящее место для \"бикини\". . ."
                                    else:
                                            $ JubesX.Panties = "bikini bottoms"

                "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not JubesX.Panties:
                        $ JubesX.FaceChange("bemused", 1)
                        if JubesX.Legs and (JubesX.Love+JubesX.Obed) <= (2 * JubesX.Inbt):
                            $ JubesX.Mouth = "smile"
                            ch_v "Я не уверена насчет этого."
                            menu:
                                "Ну ладно.":
                                    return #jump Jubes_Clothes
                                "Я настаиваю, надевай.":
                                    if (JubesX.Love+JubesX.Obed) <= (1.5 * JubesX.Inbt):
                                        $ JubesX.FaceChange("angry", Eyes="side")
                                        ch_v "Что ж, очень жаль."
                                        return #jump Jubes_Clothes
                                    else:
                                        $ JubesX.FaceChange("sadside")
                                        ch_v "Ох, ладно."
                        else:
                            ch_v "Пожалуй. . ."
                        menu:
                            extend ""
                            "Как насчет синих?":
                                    ch_v "Конечно."
                                    $ JubesX.Panties = "blue panties"
                            "Как насчет кружевных?" if "lace panties" in JubesX.Inventory:
                                    ch_v "Хорошо."
                                    $ JubesX.Panties  = "lace panties"
                            "Как насчет тигровых?" if "tiger panties" in JubesX.Inventory:
                                    ch_v "Хорошо."
                                    $ JubesX.Panties  = "tiger panties"
                            "Как насчет трусиков бикини?" if "bikini bottoms" in JubesX.Inventory:
                                    ch_v "Хорошо."
                                    $ JubesX.Panties  = "bikini bottoms"
                "Неважно":
                    pass
            return #jump Jubes_Clothes_Under
        "Неважно":
            pass
    return #jump Jubes_Clothes
    #End of Jubes Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Jubes_Clothes_Misc:
        #Misc
        "Добавь очки в свои волосы" if JubesX.Hair != "shades":
                ch_p "Тебе недостает твоих фирменных очков!"
                if ApprovalCheck(JubesX, 600):
                    ch_v "О да!"
                    $ JubesX.Hair = "shades"
                else:
                    ch_v "Я не уверена, все хорошо и так."

        "Убери очки из своих волос" if JubesX.Hair == "shades":
                ch_p "Ты должна снять очки."
                if ApprovalCheck(JubesX, 600):
                    ch_v "Ладно. . ."
                    $ JubesX.Hair = "short"
                else:
                    ch_v "Я не уверена, все хорошо и так."

        "Сухие волосы" if JubesX.Hair == "wet":
                ch_p "Тебе идут сухие волосы."
                if ApprovalCheck(JubesX, 600):
                    ch_v "Ладно."
                    $ JubesX.Hair = "short"
                else:
                    ch_v "Я не уверена, все хорошо и так."

        "Влажные волосы" if JubesX.Hair != "wet":
                ch_p "Тебе стоит увлажнить волосы."
                if ApprovalCheck(JubesX, 800):
                    ch_v "Хмм?"
                    $ JubesX.Hair = "wet"
                    "Она отходит на минуту и вскоре возвращается."
                    ch_v "Типа так?"
                else:
                    ch_v "Это слишком сложно."


        "Отрасти волосы на лобке" if not JubesX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может, отрастишь?"
                call expression JubesX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in JubesX.Todo:
                        $ JubesX.FaceChange("bemused", 1)
                        ch_v "Они не отрастают за ночь!"
                else:
                        $ JubesX.FaceChange("bemused", 1)
                        if ApprovalCheck(JubesX, 1000, TabM=0):
                            ch_v "Думаю, можно. . ."
                        else:
                            $ JubesX.FaceChange("surprised")
                            $ JubesX.Brows = "angry"
                            ch_v "Это тебя не касается!"
                            return #jump Jubes_Clothes
                        $ JubesX.Todo.append("pubes")
                        $ JubesX.PubeC = 6
        "Побрей лобок" if JubesX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression JubesX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ JubesX.FaceChange("bemused", 1)
                if "shave" in JubesX.Todo:
                    ch_v "Я тебя услышала, я этим займусь."
                else:
                    if ApprovalCheck(JubesX, 1100, TabM=0):
                        ch_v "Значит, тебе нравится так? . ."
                    else:
                        $ JubesX.FaceChange("surprised")
                        $ JubesX.Brows = "angry"
                        ch_v "Это тебя не касается!"
                        return #jump Jubes_Clothes
                    $ JubesX.Todo.append("shave")

        "Пирсинг. [[Сначала посмотрите, как она выглядит без него] (locked)" if not JubesX.SeenPussy and not JubesX.SeenChest:
            pass

        "Надень пирсинг-кольца" if JubesX.Pierce != "ring" and (JubesX.SeenPussy or JubesX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсингом-кольцами."
                if "ring" in JubesX.Todo:
                    ch_v "Я тебя услышала, я этим займусь."
                else:
                    $ JubesX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(JubesX, 1150, TabM=0)
                    if ApprovalCheck(JubesX, 900, "L", TabM=0) or (Approval and JubesX.Love > 2* JubesX.Obed):
                        ch_v "Ты думаешь, он будет мне к лицу?"
                    elif ApprovalCheck(JubesX, 600, "I", TabM=0) or (Approval and JubesX.Inbt > JubesX.Obed):
                        ch_v "Я уже давненько думаю об этом."
                    elif ApprovalCheck(JubesX, 500, "O", TabM=0) or Approval:
                        ch_v "Да, [JubesX.Petname]."
                    else:
                        $ JubesX.FaceChange("surprised")
                        $ JubesX.Brows = "angry"
                        ch_v "Мне он не нравится, [JubesX.Petname]."
                        return #jump Jubes_Clothes
                    $ JubesX.Todo.append("ring")

        "Надень пирсинг-штанги" if JubesX.Pierce != "barbell" and (JubesX.SeenPussy or JubesX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in JubesX.Todo:
                    ch_v "Я тебя услышала, я этим займусь."
                else:
                    $ JubesX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(JubesX, 1150, TabM=0)
                    if ApprovalCheck(JubesX, 900, "L", TabM=0) or (Approval and JubesX.Love > 2 * JubesX.Obed):
                        ch_v "Ты думаешь, он будет мне к лицу?"
                    elif ApprovalCheck(JubesX, 600, "I", TabM=0) or (Approval and JubesX.Inbt > JubesX.Obed):
                        ch_v "Я уже давненько думаю об этом."
                    elif ApprovalCheck(JubesX, 500, "O", TabM=0) or Approval:
                        ch_v "Да, [JubesX.Petname]."
                    else:
                        $ JubesX.FaceChange("surprised")
                        $ JubesX.Brows = "angry"
                        ch_v "Мне он не нравится, [JubesX.Petname]."
                        return #jump Jubes_Clothes
                    $ JubesX.Todo.append("barbell")

        "Сними пирсинг" if JubesX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ JubesX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(JubesX, 1350, TabM=0)
                if ApprovalCheck(JubesX, 950, "L", TabM=0) or (Approval and JubesX.Love > JubesX.Obed):
                    ch_v "Определись уже. . ."
                elif ApprovalCheck(JubesX, 700, "I", TabM=0) or (Approval and JubesX.Inbt > JubesX.Obed):
                    ch_v "Ну да, он раздражает. . ."
                elif ApprovalCheck(JubesX, 600, "O", TabM=0) or Approval:
                    ch_v "Хорошо."
                else:
                    $ JubesX.FaceChange("surprised")
                    $ JubesX.Brows = "angry"
                    ch_v "Мне он очень нравится!"
                    return #jump Jubes_Clothes
                $ JubesX.Pierce = 0

        "Надень черный чокер" if JubesX.Neck != "choker" and "halloween" in JubesX.History:
                ch_p "Почему бы тебе не примерить черный чокер?"
                ch_v "Ладно. . ."
                $ JubesX.Neck = "choker"
        "Сними украшения с шеи" if JubesX.Neck:
                ch_p "Может, снимешь украшения с шеи?"
                ch_v "Ладно. . ."
                $ JubesX.Neck = 0

        "Неважно":
            pass
    return #jump Jubes_Clothes
    #End of Jubes Misc Wardrobe

return
#End Jubes Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
