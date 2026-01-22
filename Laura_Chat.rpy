# star Laura chat interface
#Laura Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Laura_Relationship: #rkelj
    while True:
        menu:
            ch_l "О чем ты хочешь поговорить?"
            "Хочешь стать моей девушкой?" if LauraX not in Player.Harem and "ex" not in LauraX.Traits:
                    $ LauraX.DailyActions.append("relationship")
                    if "asked boyfriend" in LauraX.DailyActions and "angry" in LauraX.DailyActions:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Как я уже сказала, мне это неинтересно."
                            return
                    elif "asked boyfriend" in LauraX.DailyActions:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Все еще нет."
                            return
                    elif LauraX.Break[0]:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Я не ищу себе стаю."
                            if Player.Harem:
                                    $ LauraX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "У меня теперь никого."

                    $ LauraX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "LauraYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_l "Сначала тебе нужно обсудить это с остальными, [LauraX.Petname]."
                        else:
                            ch_l "Сначала, [LauraX.Petname], тебе нужно обсудить это с [Player.Harem[0].Name_tvo]."
                        return

                    if LauraX.Event[5]:
                            $ LauraX.FaceChange("bemused", 1)
                            if not Player.Male:
                                ch_l "Я тебе сама это предлагала, но ты ответила \"нет\". . ."
                            else:
                                ch_l "Я тебе сама это предлагала, но ты ответил \"нет\". . ."
                    else:
                            $ LauraX.FaceChange("surprised", 2)
                            ch_l "А? . ."
                            $ LauraX.FaceChange("smile", 1)

                    call Laura_OtherWoman

                    if LauraX.Love >= 800:
                            $ LauraX.FaceChange("surprised", 1)
                            $ LauraX.Mouth = "smile"
                            if not LauraX.Event[5]:
                                    $ LauraX.Statup("Love", 200, 10)
                                    call Laura_BF
                                    return
                            $ LauraX.Statup("Love", 200, 40)
                            ch_l "Конечно!"
                            if "boyfriend" not in LauraX.Petnames:
                                    $ LauraX.Petnames.append("boyfriend")
                            if "LauraYes" in Player.Traits:
                                    $ Player.Traits.remove("LauraYes")
                            $ Player.Harem.append(LauraX)
                            call Harem_Initiation
                            "[LauraX.Name] хватает вас и крепко целует."
                            $ LauraX.FaceChange("kiss", 1)
                            $ LauraX.Kissed += 1
                    elif LauraX.Obed >= 500:
                            $ LauraX.FaceChange("perplexed")
                            ch_l "Я не уверена, что хочу \"встречаться\". . ."
                    elif LauraX.Inbt >= 500:
                            $ LauraX.FaceChange("smile")
                            ch_l "Нет, нам и без этого очень весело."
                    else:
                            $ LauraX.FaceChange("perplexed", 1)
                            ch_l "Эй, притормози, [LauraX.Petname]."

            "Может, начнем все сначала?" if "ex" in LauraX.Traits:
                    $ LauraX.DailyActions.append("relationship")
                    if "asked boyfriend" in LauraX.DailyActions and "angry" in LauraX.DailyActions:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Как я уже сказала, мне это неинтересно."
                            return
                    elif "asked boyfriend" in LauraX.DailyActions:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Все еще не хочу."
                            return

                    $ LauraX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "LauraYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_l "Сначала тебе нужно обсудить это с остальными, [LauraX.Petname]."
                            else:
                                ch_l "Сначала, [LauraX.Petname], тебе нужно обсудить это с [Player.Harem[0].Name_tvo]."
                            return

                    $ Cnt = 0
                    call Laura_OtherWoman

                    if LauraX.Love >= 800:
                            $ LauraX.FaceChange("surprised", 1)
                            $ LauraX.Mouth = "smile"
                            $ LauraX.Statup("Love", 90, 5)
                            if not Player.Male:
                                ch_l "Ладно, ты заслужила еще один шанс!"
                            else:
                                ch_l "Ладно, ты заслужил еще один шанс!"
                            if "boyfriend" not in LauraX.Petnames:
                                        $ LauraX.Petnames.append("boyfriend")
                            $ LauraX.Traits.remove("ex")
                            if "LauraYes" in Player.Traits:
                                    $ Player.Traits.remove("LauraYes")
                            $ Player.Harem.append(LauraX)
                            call Harem_Initiation
                            "[LauraX.Name] притягивает вас к себе и крепко целует."
                            $ LauraX.FaceChange("kiss", 1)
                            $ LauraX.Kissed += 1
                    elif LauraX.Love >= 600 and ApprovalCheck(LauraX, 1500):
                            $ LauraX.FaceChange("smile", 1)
                            $ LauraX.Statup("Love", 90, 5)
                            ch_l "Эм, ладно, наверное."
                            if "boyfriend" not in LauraX.Petnames:
                                $ LauraX.Petnames.append("boyfriend")
                            $ LauraX.Traits.remove("ex")
                            if "LauraYes" in Player.Traits:
                                    $ Player.Traits.remove("LauraYes")
                            $ Player.Harem.append(LauraX)
                            call Harem_Initiation
                            $ LauraX.FaceChange("kiss", 1)
                            "[LauraX.Name] дарит вам легкий поцелуй."
                            $ LauraX.FaceChange("sly", 1)
                            $ LauraX.Kissed += 1
                    elif LauraX.Obed >= 500:
                            $ LauraX.FaceChange("sad")
                            ch_l "Думаю, будет лучше, если мы не будем все усложнять."
                    elif LauraX.Inbt >= 500:
                            $ LauraX.FaceChange("perplexed")
                            ch_l "И испортить все веселье?"
                    else:
                            $ LauraX.FaceChange("perplexed", 1)
                            ch_l "Я тебе не настолько доверяю."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if LauraX in Player.Harem:
                            call AskDateOther

            "Думаю, мы должны расстаться." if LauraX in Player.Harem:
                            if "breakup talk" in LauraX.RecentActions:
                                    ch_l "Ты что, шутишь? Мы только что говорили об этом."
                            elif "breakup talk" in LauraX.DailyActions:
                                    if not Player.Male:
                                        ch_l "Ты мне уже надоела."
                                    else:
                                        ch_l "Ты мне уже надоел."
                                    ch_l "Не сегодня, [LauraX.Petname]."
                            else:
                                    call Breakup(LauraX)

            "О разговоре, который у нас был ранее. . .":
                menu:
                    "Помнишь, ты как-то призналась мне в любви. . ?" if "lover" not in LauraX.Traits and LauraX.Event[6] >= 20 and LauraX.Event[6] != 23:
                            call Laura_Love_Redux

                    "Помнишь, ты как-то рассказывала мне о себе. . ?" if "lover" not in LauraX.Traits and LauraX.Event[6] == 23:
                            call Laura_Love_Redux

                    "Помнишь, ты говорила, что хочешь, чтобы больше тебя контролировала?" if "sir" not in LauraX.Petnames and "sir" in LauraX.History and not Player.Male:
                            if "asked sub" in LauraX.RecentActions:
                                    ch_l "Мы только что это обсуждали."
                            elif "asked sub" in LauraX.DailyActions:
                                    ch_l "Хватит этих разговоров на сегодня. . ."
                            else:
                                    call Laura_Sub_Asked

                    "Помнишь, ты говорила, что хочешь, чтобы больше тебя контролировал?" if "sir" not in LauraX.Petnames and "sir" in LauraX.History and Player.Male:
                            if "asked sub" in LauraX.RecentActions:
                                    ch_l "Мы только что это обсуждали."
                            elif "asked sub" in LauraX.DailyActions:
                                    ch_l "Хватит этих разговоров на сегодня. . ."
                            else:
                                    call Laura_Sub_Asked

                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоей хозяйкой?" if "master" not in LauraX.Petnames and "master" in LauraX.History and not Player.Male:
                            if "asked sub" in LauraX.RecentActions:
                                    ch_l "Мы только что это обсуждали."
                            elif "asked sub" in LauraX.DailyActions:
                                    ch_l "Хватит этих разговоров на сегодня. . ."
                            else:
                                    call Laura_Sub_Asked

                    "Помнишь, ты говорила, что хочешь, чтобы я стал твоим хозяином?" if "master" not in LauraX.Petnames and "master" in LauraX.History and Player.Male:
                            if "asked sub" in LauraX.RecentActions:
                                    ch_l "Мы только что это обсуждали."
                            elif "asked sub" in LauraX.DailyActions:
                                    ch_l "Хватит этих разговоров на сегодня. . ."
                            else:
                                    call Laura_Sub_Asked
                    "Неважно":
                            pass

            "Неважно":
                return

    return

label Laura_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((LauraX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ LauraX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_l "Но ты же сейчас с [Player.Harem[0].Name_tvo] и у тебя уже целая стая."
    else:
        ch_l "Но ты же сейчас с [Player.Harem[0].Name_tvo], ведь так?"
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "LauraYes" in Player.Traits:
                if ApprovalCheck(LauraX, 1800, Bonus = Cnt):
                    $ LauraX.FaceChange("smile", 1)
                    if LauraX.Love >= LauraX.Obed:
                            ch_l "Наверное, я смогу с этим смириться."
                    elif LauraX.Obed >= LauraX.Inbt:
                            ch_l "Если ты этого хочешь."
                    else:
                            ch_l "Хорошо."
                else:
                    $ LauraX.FaceChange("angry", 1)
                    ch_l "Ага, думаю, это так похоже на нее, но я не собираюсь делиться."
                    $ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "LauraYes" not in Player.Traits and not Player.Male:
                if ApprovalCheck(LauraX, 1800, Bonus = Cnt):
                        $ LauraX.FaceChange("smile", 1)
                        if LauraX.Love >= LauraX.Obed:
                            ch_l "Наверное, я смогу с этим смириться."
                        elif LauraX.Obed >= LauraX.Inbt:
                            ch_l "Если ты этого хочешь."
                        else:
                            ch_l "Хорошо."
                        ch_l "Спроси ее и расскажи мне утром, что она ответила."
                else:
                        $ LauraX.FaceChange("angry", 1)
                        ch_l "Ага, думаю, это так похоже на нее, но я не собираюсь делиться."
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "LauraYes" not in Player.Traits and Player.Male:
                if ApprovalCheck(LauraX, 1800, Bonus = Cnt):
                        $ LauraX.FaceChange("smile", 1)
                        if LauraX.Love >= LauraX.Obed:
                            ch_l "Наверное, я смогу с этим смириться."
                        elif LauraX.Obed >= LauraX.Inbt:
                            ch_l "Если ты этого хочешь."
                        else:
                            ch_l "Хорошо."
                        ch_l "Спроси ее и расскажи мне утром, что она ответила."
                else:
                        $ LauraX.FaceChange("angry", 1)
                        ch_l "Ага, думаю, это так похоже на нее, но я не собираюсь делиться."
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
                if not ApprovalCheck(LauraX, 1800, Bonus = -Cnt): #checks if Laura likes you more than the other girl
                        $ LauraX.FaceChange("angry", 1)
                        if not ApprovalCheck(LauraX, 1800):
                                ch_l "На ее месте, мне было бы больно такое узнать."
                        else:
                                ch_l "Мне это не нравится."
                        $ renpy.pop_call()
                else:
                        $ LauraX.FaceChange("smile", 1)
                        if LauraX.Love >= LauraX.Obed:
                                ch_l "Думаю, можно. . ."
                        elif LauraX.Obed >= LauraX.Inbt:
                                ch_l "Если ты этого хочешь."
                        else:
                                ch_l "Хорошо."
                        $ LauraX.Traits.append("downlow")

        "Я могу порвать с ней.":
                    $ LauraX.FaceChange("sad")
                    ch_l "После этого возращайся ко мне."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ LauraX.FaceChange("sad")
                    ch_l "Ага."
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ LauraX.FaceChange("sad")
                    ch_l "Ага."
                    $ renpy.pop_call()

    return


label Laura_About(Check=0): #rkeljsvg
    if Check not in TotalGirls:
            ch_l "Кто это?"
            return
    ch_l "Что я думаю о ней? Ну. . ."
    if Check == RogueX:
            if "poly Rogue" in LauraX.Traits:
                ch_l "Ну, мы спим вместе, так что. . ."
            elif LauraX.LikeRogue >= 900:
                ch_l "У нее клевая задница. . ."
            elif LauraX.LikeRogue >= 800:
                ch_l "Она в хорошей форме. . ."
            elif LauraX.LikeRogue >= 700:
                ch_l "Она хорошо сражается."
            elif LauraX.LikeRogue >= 600:
                ch_l "Мы хорошо ладим."
            elif LauraX.LikeRogue >= 500:
                ch_l "Думаю, я пару раз ее где-то видела."
            elif LauraX.LikeRogue >= 400:
                ch_l "Я не хочу о ней говорить."
            elif LauraX.LikeRogue >= 300:
                ch_l "Ненавижу ее."
            else:
                ch_l "Она сука."
    elif Check == KittyX:
            if "poly Kitty" in LauraX.Traits:
                ch_l "Ну, мы спим вместе, так что. . ."
            elif LauraX.LikeKitty >= 900:
                ch_l "Мне очень нравятся ее маленькие сиськи. . ."
            elif LauraX.LikeKitty >= 800:
                ch_l "Она держит себя в форме. . ."
            elif LauraX.LikeKitty >= 700:
                ch_l "Ей не сидится на одном месте."
            elif LauraX.LikeKitty >= 600:
                ch_l "Она клевая."
            elif LauraX.LikeKitty >= 500:
                ch_l "Думаю, я пару раз ее где-то видела."
            elif LauraX.LikeKitty >= 400:
                ch_l "Я не хочу о ней говорить."
            elif LauraX.LikeKitty >= 300:
                ch_l "Ненавижу ее."
            else:
                ch_l "Она сука."
    elif Check == EmmaX:
            if "poly Emma" in LauraX.Traits:
                ch_l "Ну, мы спим вместе, так что. . ."
            elif LauraX.LikeEmma >= 900:
                ch_l "У нее классные буфера. . ."
            elif LauraX.LikeEmma >= 800:
                ch_l "Она очень хорошо пахнет. . ."
            elif LauraX.LikeEmma >= 700:
                ch_l "Она мила со мной после занятий."
            elif LauraX.LikeEmma >= 600:
                ch_l "Она хороший преподаватель."
            elif LauraX.LikeEmma >= 500:
                ch_l "Она нормальная."
            elif LauraX.LikeEmma >= 400:
                ch_l "Мне не нравится ее излишнее внимание ко мне."
            elif LauraX.LikeEmma >= 300:
                ch_l "Ей нужно держаться подальше от моей головы."
            else:
                ch_l "Грррр."
    elif Check == JeanX:
            if "poly Jean" in LauraX.Traits:
                ch_l "Ну, мы спим вместе, так что. . ."
            elif LauraX.LikeJean >= 900:
                ch_l "У нее клевая задница. . ."
            elif LauraX.LikeJean >= 800:
                ch_l "Она в хорошей форме. . ."
            elif LauraX.LikeJean >= 700:
                ch_l "Она. . . нормальная."
            elif LauraX.LikeJean >= 600:
                ch_l "Думаю, она нормальная?"
            elif LauraX.LikeJean >= 500:
                ch_l "Она в какой-то степени доставучая."
            elif LauraX.LikeJean >= 400:
                ch_l "Ей нужно держаться подальше от моей головы."
            elif LauraX.LikeJean >= 300:
                ch_l "Ненавижу ее."
            else:
                ch_l "Она сука."
    elif Check == StormX:
            if "poly Storm" in LauraX.Traits:
                ch_l "Ну, мы спим вместе, так что. . ."
            elif LauraX.LikeStorm >= 900:
                ch_l "У нее отличная задница. . ."
            elif LauraX.LikeStorm >= 800:
                ch_l "От нее пахнет садом. . ."
            elif LauraX.LikeStorm >= 700:
                ch_l "SОна мила со мной после занятий."
            elif LauraX.LikeStorm >= 600:
                ch_l "Она хороший преподаватель."
            elif LauraX.LikeStorm >= 500:
                ch_l "Она нормальная."
            elif LauraX.LikeStorm >= 400:
                ch_l "Она может быть злой."
            elif LauraX.LikeStorm >= 300:
                ch_l "Она должна держаться подальше от меня."
            else:
                ch_l "Грррр."
    elif Check == JubesX:
            if "poly Jubes" in LauraX.Traits:
                ch_l "Ну, мы спим вместе, так что. . ."
            elif LauraX.LikeJubes >= 900:
                ch_l "Мне нравится ее гладкая кожа. . ."
            elif LauraX.LikeJubes >= 800:
                ch_l "У нее хорошая фигура. . ."
            elif LauraX.LikeJubes >= 700:
                ch_l "Трудно сказать."
            elif LauraX.LikeJubes >= 600:
                ch_l "Она клевая."
            elif LauraX.LikeJubes >= 500:
                ch_l "Думаю, я пару раз ее где-то видела."
            elif LauraX.LikeJubes >= 400:
                ch_l "Она кусается."
            elif LauraX.LikeJubes >= 300:
                ch_l "Ненавижу ее."
            else:
                ch_l "Она сука."
    elif Check == GwenX:
            if "poly Gwen" in LauraX.Traits:
                ch_l "Ну, мы спим вместе, так что. . ."
            elif LauraX.LikeGwen >= 900:
                ch_l "Мне нравится ее упругая попка. . ."
            elif LauraX.LikeGwen >= 800:
                ch_l "Она держит себя в форме. . ."
            elif LauraX.LikeGwen >= 700:
                ch_l "Она хорошо дерется."
            elif LauraX.LikeGwen >= 600:
                ch_l "Она клевая."
            elif LauraX.LikeGwen >= 500:
                ch_l "Думаю, я пару раз ее где-то видела."
            elif LauraX.LikeGwen >= 400:
                ch_l "Я не хочу о ней говорить."
            elif LauraX.LikeGwen >= 300:
                ch_l "Ненавижу ее."
            else:
                ch_l "Она сука."
    elif Check == BetsyX:
            if "poly Betsy" in LauraX.Traits:
                ch_l "Ну, мы спим вместе, так что. . ."
            elif LauraX.LikeBetsy >= 900:
                ch_l "Мне очень нравится ее упругая задница. . ."
            elif LauraX.LikeBetsy >= 800:
                ch_l "Она держит себя в форме. . ."
            elif LauraX.LikeBetsy >= 700:
                ch_l "Она хорошо дерется."
            elif LauraX.LikeBetsy >= 600:
                ch_l "Она клевая."
            elif LauraX.LikeBetsy >= 500:
                ch_l "Думаю, я пару раз ее где-то видела."
            elif LauraX.LikeBetsy >= 400:
                ch_l "Я не хочу о ней говорить."
            elif LauraX.LikeBetsy >= 300:
                ch_l "Ненавижу ее."
            else:
                ch_l "Она сука."
    elif Check == DoreenX:
            if "poly Doreen" in LauraX.Traits:
                ch_l "Ну, мы спим вместе, так что. . ."
            elif LauraX.LikeDoreen >= 900:
                ch_l "Мне очень нравится ее пухлая задница. . ."
            elif LauraX.LikeDoreen >= 800:
                ch_l "Она держит себя в форме. . ."
            elif LauraX.LikeDoreen >= 700:
                ch_l "Она хороший боец."
            elif LauraX.LikeDoreen >= 600:
                ch_l "Она клевая."
            elif LauraX.LikeDoreen >= 500:
                ch_l "Думаю, я пару раз ее где-то видела."
            elif LauraX.LikeDoreen >= 400:
                ch_l "Я не хочу о ней говорить."
            elif LauraX.LikeDoreen >= 300:
                ch_l "Ненавижу ее."
            else:
                ch_l "Она сука."
    elif Check == WandaX:
            if "poly Wanda" in LauraX.Traits:
                ch_l "Мы спим вместе, так что. . ."
            elif LauraX.LikeWanda >= 900:
                ch_l "У нее сексуальные сиськи. . ."
            elif LauraX.LikeWanda >= 800:
                ch_l "У нее хорошая фигура. . ."
            elif LauraX.LikeWanda >= 700:
                ch_l "Она хороший боец."
            elif LauraX.LikeWanda >= 600:
                ch_l "Мы хорошо ладим."
            elif LauraX.LikeWanda >= 500:
                ch_l "Думаю, я пару раз ее где-то видела."
            elif LauraX.LikeWanda >= 400:
                ch_l "Я не хочу о ней говорить."
            elif LauraX.LikeWanda >= 300:
                ch_l "Ненавижу ее."
            else:
                ch_l "Она ведьма."
    else:
                ch_l "Эм. . ."
    return
#End Laura_AboutEmma

label Laura_Monogamy:
        #called from Laura_Settings to ask her not to hook up with other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in LauraX.Traits:
                    if LauraX.Thirst >= 60 and not ApprovalCheck(LauraX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ LauraX.FaceChange("sly",1)
                            if "mono" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Obed", 90, -2)
                            ch_l "Ты не в состояние влиять на меня. . ."
                            return
                    elif ApprovalCheck(LauraX, 1200, "LO", TabM=0) and LauraX.Love >= LauraX.Obed:
                            #she cares
                            $ LauraX.FaceChange("sly",1)
                            if "mono" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Love", 90, 1)
                            if not Player.Male:
                                ch_l "Не хочу, чтобы ты ревновала."
                            else:
                                ch_l "Не хочу, чтобы ты ревновал."
                            ch_l "Ладно, никаких левых кисок. . ."
                    elif ApprovalCheck(LauraX, 700, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Согласна."
                    else:
                            #she doesn't care
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Поверь, тебе не стоит меня видеть голодной."
                            return
                    if "mono" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    $ LauraX.AddWord(1,0,"mono") #Daily
                    $ LauraX.Traits.append("mono")
            "Не встречайся с другими девушками." if "mono" not in LauraX.Traits:
                    if ApprovalCheck(LauraX, 900, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Ладно."
                    elif LauraX.Thirst >= 60 and not ApprovalCheck(LauraX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ LauraX.FaceChange("sly",1)
                            if "mono" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Obed", 90, -2)
                            ch_l "Я бы с удовольствием, но ты так редко бываешь рядом. . ."
                            return
                    elif ApprovalCheck(LauraX, 600, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Ладно, как скажешь."
                    elif ApprovalCheck(LauraX, 1400, "LO", TabM=0):
                            #she cares
                            $ LauraX.FaceChange("sly",1)
                            ch_l "На твоем месте, я бы не стала так давить, но ладно, я согласна."
                    else:
                            #she doesn't care
                            $ LauraX.FaceChange("sly",1,Brows="confused")
                            ch_l "Поверь, тебе не стоит меня видеть, когда у меня голод."
                            return
                    if "mono" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    $ LauraX.AddWord(1,0,"mono") #Daily
                    $ LauraX.Traits.append("mono")
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in LauraX.Traits:
                    if ApprovalCheck(LauraX, 700, "O", TabM=0):
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Согласна."
                    elif ApprovalCheck(LauraX, 800, "L", TabM=0):
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Тебе лучше не оставлять меня без присмотра. . ."
                    else:
                            $ LauraX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Love", 90, -2)
                            ch_l "Зовите девушек, мне только что дали разрешение!"
                    if "mono" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    if "mono" in LauraX.Traits:
                            $ LauraX.Traits.remove("mono")
                    $ LauraX.AddWord(1,0,"mono") #Daily
            "Неважно":
                pass
        return

# end Laura monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Laura_Jumped:
        #called from Laura_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ LauraX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_l "Да?"
            "На будущее, можешь сначала спрашивать?" if "chill" not in LauraX.Traits:
                    if LauraX.Thirst >= 60 and not ApprovalCheck(LauraX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ LauraX.FaceChange("sly",1)
                            if "chill" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Obed", 90, -2)
                            ch_l "Нет, если ты и дальше собираешься избегать меня. . ."
                            return
                    elif ApprovalCheck(LauraX, 1000, "LO", TabM=0) and LauraX.Love >= LauraX.Obed:
                            #she cares
                            $ LauraX.FaceChange("surprised",1)
                            if "chill" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Love", 90, 1)
                            ch_l "Извини, я просто перевозбудилась. . ."
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Я постараюсь держать себя в руках. . ."
                    elif ApprovalCheck(LauraX, 500, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Извини. . ."
                    else:
                            #she doesn't care
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Только если я не смогу тебя найти."
                            return
                    if "chill" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    $ LauraX.AddWord(1,0,"chill") #Daily
                    $ LauraX.Traits.append("chill")
            "Больше так не делай." if "chill" not in LauraX.Traits:
                    if ApprovalCheck(LauraX, 800, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Ладно."
                    elif LauraX.Thirst >= 60 and not ApprovalCheck(LauraX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ LauraX.FaceChange("sly",1)
                            if "chill" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Obed", 90, -2)
                            ch_l "Тогда не избегай меня. . ."
                            return
                    elif ApprovalCheck(LauraX, 400, "O", TabM=0):
                            #she is obedient
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            ch_l "Согласна. . ."
                    elif ApprovalCheck(LauraX, 500, "LO", TabM=0) and not ApprovalCheck(LauraX, 500, "I", TabM=0):
                            #she cares
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Не указывай мне, что делать."
                            ch_l "Но ладно, я постараюсь себя контролировать. . ."
                    else:
                            #she doesn't care
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Только если я не смогу тебя найти."
                            return
                    if "chill" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    $ LauraX.AddWord(1,0,"chill") #Daily
                    $ LauraX.Traits.append("chill")
            "Делай что хочешь.":
                    if ApprovalCheck(LauraX, 800, "L", TabM=0):
                            $ LauraX.FaceChange("sly",1)
                            if not Player.Male:
                                ch_l "Ох, думаю, нам обоеим это понравится. . ."
                            else:
                                ch_l "Ох, думаю, нам обоим это понравится. . ."
                    elif ApprovalCheck(LauraX, 700, "O", TabM=0):
                            $ LauraX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_l "О, да, госпожа."
                            else:
                                ch_l "О, да, господин."
                    else:
                            $ LauraX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Love", 90, -2)
                            ch_l "Конечно, если я буду возбуждена."
                    if "chill" not in LauraX.DailyActions:
                            $ LauraX.Statup("Obed", 90, 3)
                    if "chill" in LauraX.Traits:
                            $ LauraX.Traits.remove("chill")
                    $ LauraX.AddWord(1,0,"chill") #Daily
            "Эм, неважно.":
                pass
        return

# end Laura jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start laura hungry //////////////////////////////////////////////////////////
label Laura_Hungry:
    if LauraX.Chat[3]:
        ch_l "[[облизывает свои губы] Я немного голодна. . ."
    elif LauraX.Chat[2]:
        if not Player.Male:
            ch_l "Мне очень нравится та сыворотка, которую ты приготовила."
        else:
            ch_l "Мне очень нравится та сыворотка, которую ты приготовил."
    else:
        ch_l "[[облизывает свои губы] Я немного голодна. . ."
    $ LauraX.Traits.append("hungry")
return


# end laura hungry //////////////////////////////////////////////////////////

# Laura Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Laura_SexChat:
    $ Line = "Ага, о чем ты хочешь поговорить?" if not Line else Line
    while True:
            menu:
                ch_l "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in LauraX.DailyActions:
                        ch_l "Я помню."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "sex":
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Ага, я знаю. . ."
                                        elif LauraX.Favorite == "sex":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 10)
                                            ch_l "Мне тоже очень нравится!"
                                        elif LauraX.Sex >= 5:
                                            ch_l "Ну, я не против."
                                        elif not LauraX.Sex:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Кто тебя трахает?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Хех, эм, ага, это приятно. . ."
                                        $ LauraX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "anal":
                                            $ LauraX.Statup("Lust", 80, 5)
                                            if not Player.Male:
                                                ch_l "Ты уже говорила. . ."
                                            else:
                                                ch_l "Ты уже говорил. . ."
                                        elif LauraX.Favorite == "anal":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 10)
                                            ch_l "Мне тоже нравится!"
                                        elif LauraX.Anal >= 10:
                                            ch_l "Ага, это. . . приятно. . ."
                                        elif not LauraX.Anal:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Кто тебя трахает?"
                                        else:
                                            $ LauraX.FaceChange("bemused",Eyes="side")
                                            ch_l "Хех, ага, эм, это нормально. . ."
                                        $ LauraX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "blow":
                                            $ LauraX.Statup("Lust", 80, 3)
                                            ch_l "Ага, я знаю."
                                        elif LauraX.Favorite == "blow":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Я люблю твой член!"
                                        elif LauraX.Blow >= 10:
                                            ch_l "Ага, ты довольно вкусный."
                                        elif not LauraX.Blow:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Кто сосет твой член?!"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Я. . . начинаю привыкать к его вкусу. . ."
                                        $ LauraX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "cun":
                                            $ LauraX.Statup("Lust", 80, 3)
                                            ch_l "Ага, я знаю."
                                        elif LauraX.Favorite == "cun":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Я люблю твою киску!"
                                        elif LauraX.CUN >= 10:
                                            ch_l "Ага, ты довольно вкусная."
                                        elif not LauraX.CUN:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Кто вылизывает твою киску?!"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Я. . . начинаю привыкать к ее вкусу. . ."
                                        $ LauraX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "titjob":
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Ага, ты уже говорил это ранее. . ."
                                        elif LauraX.Favorite == "titjob":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 7)
                                            ch_l "Ага, мне тоже нравится. . ."
                                        elif LauraX.Tit >= 10:
                                            ch_l "Это, безусловно, интересный опыт . . ."
                                        elif not LauraX.Tit:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Кто тебя трахает своими сиськами?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Мило с твоей стороны это упомянуть. . ."
                                            $ LauraX.Statup("Love", 80, 5)
                                            $ LauraX.Statup("Inbt", 50, 10)
                                        $ LauraX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "foot":
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Ага, ты уже говорил это. . ."
                                        elif LauraX.Favorite == "foot":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 7)
                                            ch_l "Мне очень нравится использовать свои ножки. . ."
                                        elif LauraX.Foot >= 10:
                                            ch_l "Мне тоже нравится . . ."
                                        elif not LauraX.Foot:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Кто играет с тобой своими ножками?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Ага, это приятно. . ."
                                        $ LauraX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "hand":
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Ага, ты уже говорил это. . ."
                                        elif LauraX.Favorite == "hand":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 7)
                                            ch_l "Он комфортно лежит в руке. . ."
                                        elif LauraX.Hand >= 10:
                                            ch_l "Мне тоже нравится . . ."
                                        elif not LauraX.Hand:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Кто тебе дрочит?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Ага, это приятно. . ."
                                        $ LauraX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "finger":
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Ага, ты уже говорила это. . ."
                                        elif LauraX.Favorite == "finger":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 7)
                                            ch_l "Она приятная на ощупь. . ."
                                        elif LauraX.Finger >= 10:
                                            ch_l "Мне тоже нравится . . ."
                                        elif not LauraX.Finger:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Кто это ласкает твою киску?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Ага, это приятно. . ."
                                        $ LauraX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = LauraX.FondleB + LauraX.FondleT + LauraX.SuckB + LauraX.Hotdog
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "fondle":
                                            $ LauraX.Statup("Lust", 80, 3)
                                            ch_l "Ага, думаю, все это уже поняли. . ."
                                        elif LauraX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Мне нравится, когда ты прикасаешься ко мне. . ."
                                        elif Cnt >= 10:
                                            ch_l "Ага, это очень приятно. . ."
                                        elif not Cnt:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Кто позволяет тебе лапать себя?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Мне нравятся эти ощущения. . ."
                                        $ LauraX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ LauraX.FaceChange("sly")
                                        if LauraX.PlayerFav == "kiss you":
                                            $ LauraX.Statup("Love", 90, 3)
                                            ch_l "Как романтично. . ."
                                        elif LauraX.Favorite == "kiss you":
                                            $ LauraX.Statup("Love", 90, 5)
                                            $ LauraX.Statup("Lust", 80, 5)
                                            ch_l "Ммм, твой вкус на моих губах. . ."
                                        elif LauraX.Kissed >= 10:
                                            ch_l "Я тоже люблю тебя целовать . . ."
                                        elif not LauraX.Kissed:
                                            $ LauraX.FaceChange("perplexed")
                                            ch_l "Кого это ты целуешь?"
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            ch_l "Мне тоже нравится целовать тебя. . ."
                                        $ LauraX.PlayerFav = "kiss you"

                        $ LauraX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(LauraX, 800):
                                        $ LauraX.FaceChange("perplexed")
                                        ch_l ". . ."
                                else:
                                        if LauraX.SEXP >= 50:
                                            $ LauraX.FaceChange("sly")
                                            if not Player.Male:
                                                ch_l "Ты должна знать. . ."
                                            else:
                                                ch_l "Ты должен знать. . ."
                                        else:
                                            $ LauraX.FaceChange("bemused")
                                            $ LauraX.Eyes = "side"
                                            ch_l "Хмм. . ."


                                        if not LauraX.Favorite or LauraX.Favorite == "kiss you":
                                            ch_l "Поцелуи?"
                                        elif LauraX.Favorite == "anal":
                                                ch_l "Пожалуй, анал."
                                        elif LauraX.Favorite == "lick ass":
                                                ch_l "Когда ты вылизываешь мою попку."
                                        elif LauraX.Favorite == "insert ass":
                                                ch_l "Наверное, когда ты трахаешь пальцем меня в попку."
                                        elif LauraX.Favorite == "sex":
                                                ch_l "Классический секс."
                                        elif LauraX.Favorite == "lick pussy":
                                                ch_l "Когда ты лижешь мою киску."
                                        elif LauraX.Favorite == "fondle pussy":
                                                ch_l "Когда ты теребишь мою киску пальцем."
                                        elif LauraX.Favorite == "blow":
                                                ch_l "Мне нравится вкус твоего члена."
                                        elif LauraX.Favorite == "cun":
                                                ch_l "Мне нравится вкус твоей киски."
                                        elif LauraX.Favorite == "tit":
                                                ch_l "Когда я использую свои сиськи."
                                        elif LauraX.Favorite == "foot":
                                                ch_l "Дрочка ногами - это довольно весело."
                                        elif LauraX.Favorite == "hand":
                                                ch_l "Мне нравится дрочить тебе."
                                        elif LauraX.Favorite == "finger":
                                                ch_l "Мне нравится ласкать твою киску."
                                        elif LauraX.Favorite == "hotdog":
                                                ch_l "Когда ты трешься о меня."
                                        elif LauraX.Favorite == "suck breasts":
                                                ch_l "Когда ты сосешь мои сиськи."
                                        elif LauraX.Favorite == "fondle breasts":
                                                ch_l "Когда ты мнешь мои сиськи."
                                        elif LauraX.Favorite == "fondle thighs":
                                                ch_l "Когда ты растираешь мои бедра."
                                        else:
                                                ch_l "Откуда мне знать?"

                                # End Laura's favorite things.

                "Не болтай так много во время секса." if "vocal" in LauraX.Traits:
                        if "setvocal" in LauraX.DailyActions:
                            $ LauraX.FaceChange("perplexed")
                            ch_l "Определись уже."
                        else:
                            if ApprovalCheck(LauraX, 1000) and LauraX.Obed <= LauraX.Love:
                                $ LauraX.FaceChange("bemused")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l "Вести себя тише, поняла."
                                $ LauraX.Traits.remove("vocal")
                            elif ApprovalCheck(LauraX, 700, "O"):
                                $ LauraX.FaceChange("sadside")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l ". . ."
                                $ LauraX.Traits.remove("vocal")
                            elif ApprovalCheck(LauraX, 600):
                                $ LauraX.FaceChange("sly")
                                $ LauraX.Statup("Love", 90, -3)
                                $ LauraX.Statup("Obed", 50, -1)
                                $ LauraX.Statup("Inbt", 90, 5)
                                ch_l "Не дави на меня, [LauraX.Petname]."
                            else:
                                $ LauraX.FaceChange("angry")
                                $ LauraX.Statup("Love", 90, -5)
                                $ LauraX.Statup("Obed", 60, -3)
                                $ LauraX.Statup("Inbt", 90, 10)
                                ch_l "Я не подчиняюсь твоим приказам, [LauraX.Petname]."

                            $ LauraX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in LauraX.Traits:
                        if "setvocal" in LauraX.DailyActions:
                            $ LauraX.FaceChange("perplexed")
                            ch_l "Я услышала тебя и в первый раз."
                        else:
                            if ApprovalCheck(LauraX, 1000) and LauraX.Obed <= LauraX.Love:
                                $ LauraX.FaceChange("sly")
                                $ LauraX.Statup("Obed", 90, 2)
                                ch_l "Ладно, буду шумнее. . ."
                                $ LauraX.Traits.append("vocal")
                            elif ApprovalCheck(LauraX, 700, "O"):
                                $ LauraX.FaceChange("sadside")
                                $ LauraX.Statup("Obed", 90, 2)
                                ch_l "Если ты этого хочешь, [LauraX.Petname]."
                                $ LauraX.Traits.append("vocal")
                            elif ApprovalCheck(LauraX, 600):
                                $ LauraX.FaceChange("sly")
                                $ LauraX.Statup("Obed", 90, 3)
                                ch_l "Ладно?"
                                $ LauraX.Traits.append("vocal")
                            else:
                                $ LauraX.FaceChange("angry")
                                $ LauraX.Statup("Inbt", 90, 5)
                                ch_l ". . ."

                            $ LauraX.DailyActions.append("setvocal")
                        # End Laura Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in LauraX.Traits:
                        if "initiative" in LauraX.DailyActions:
                            $ LauraX.FaceChange("perplexed")
                            ch_l "Я услышала тебя и в первый раз."
                        else:
                            if ApprovalCheck(LauraX, 1200) and LauraX.Obed <= LauraX.Love:
                                $ LauraX.FaceChange("bemused")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l "Стать пассивной? Ладно."
                                $ LauraX.Traits.append("passive")
                            elif ApprovalCheck(LauraX, 700, "O"):
                                $ LauraX.FaceChange("sadside")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l "Я постараюсь держать себя в руках."
                                $ LauraX.Traits.append("passive")
                            elif ApprovalCheck(LauraX, 600):
                                $ LauraX.FaceChange("sly")
                                $ LauraX.Statup("Love", 90, -3)
                                $ LauraX.Statup("Obed", 50, -1)
                                $ LauraX.Statup("Inbt", 90, 5)
                                ch_l "Хм, нет."
                            else:
                                $ LauraX.FaceChange("angry")
                                $ LauraX.Statup("Love", 90, -5)
                                $ LauraX.Statup("Obed", 60, -3)
                                $ LauraX.Statup("Inbt", 90, 10)
                                ch_l "Посмотрим."

                            $ LauraX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in LauraX.Traits:
                        if "initiative" in LauraX.DailyActions:
                                $ LauraX.FaceChange("perplexed")
                                ch_l "Я услышала тебя и в первый раз."
                        else:
                            if ApprovalCheck(LauraX, 1000) and LauraX.Obed <= LauraX.Love:
                                $ LauraX.FaceChange("bemused")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l "Стать более активной, поняла."
                                $ LauraX.Traits.remove("passive")
                            elif ApprovalCheck(LauraX, 700, "O"):
                                $ LauraX.FaceChange("sadside")
                                $ LauraX.Statup("Obed", 90, 1)
                                ch_l "Если ты настаиваешь."
                                $ LauraX.Traits.remove("passive")
                            elif ApprovalCheck(LauraX, 600):
                                $ LauraX.FaceChange("sly")
                                $ LauraX.Statup("Obed", 90, 3)
                                ch_l "Посмотрим."
                                $ LauraX.Traits.remove("passive")
                            else:
                                $ LauraX.FaceChange("angry")
                                $ LauraX.Statup("Inbt", 90, 5)
                                ch_l "Для этого требуется слишком много сил."

                            $ LauraX.DailyActions.append("initiative")

                "О том, как ты накидываешься" if "jumped" in LauraX.History:
                        call Laura_Jumped
                "О твоей мастурбации":
                    call NoFap(LauraX)

                "Всегда носи вибратор" if "dailyvibe" not in LauraX.Traits:
                        call Daily_Vibrator(LauraX)
                "Перестань всегда носить вибратор" if "dailyvibe" in LauraX.Traits:
                        ch_l "Ладно. . ."
                        $ LauraX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи анальную пробку" if "dailyplug" not in LauraX.Traits:
                        call Daily_Plug(LauraX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in LauraX.Traits:
                        ch_l "Ладно. . ."
                        $ LauraX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Неважно" if Line == "Ага, о чем ты хочешь поговорить?":
                        return
                "На этом все." if Line != "Ага, о чем ты хочешь поговорить?":
                        return
            if Line == "Ага, о чем ты хочешь поговорить?":
                $ Line = "Что-нибудь еще?"
    return
# End Laura Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Laura Chitchat /////////////////// #Work in progress
label Laura_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if LauraX not in Digits:
                if ApprovalCheck(LauraX, 500, "L") or ApprovalCheck(LauraX, 250, "I"):
                    ch_l "Ох, вот мой номер, на случай, если тебе понадобится помощь."
                    $ Digits.append(LauraX)
                    return
                elif ApprovalCheck(LauraX, 250, "O"):
                    ch_l "Вот мой номер, на случай, если тебе понадобиться связаться со мной."
                    $ Digits.append(LauraX)
                    return

        if "hungry" not in LauraX.Traits and (LauraX.Swallow + LauraX.Chat[2]) >= 10 and LauraX.Loc == bg_current:  #She's swallowed a lot
                    call Laura_Hungry
                    return

        if "partyfoul" in LauraX.History and "partyfix" not in LauraX.History:
                    call Laura_Foul
                    return

        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(LauraX, 800, "I")):
                    if LauraX.Loc == bg_current and LauraX.Thirst >= 30 and "refused" not in LauraX.DailyActions and "quicksex" not in LauraX.DailyActions:
                            $ LauraX.FaceChange("sly",1)
                            ch_l "Эй, хочешь перепихнуться?"
                            call Quick_Sex(LauraX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in LauraX.DailyActions:
#            $ Options.append("caught")
        if LauraX.Event[0] and "key" not in LauraX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in LauraX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in LauraX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in LauraX.DailyActions:
            $ Options.append("corruption")

        if "Laura" not in LauraX.Names:
            $ Options.append("laura")

        if LauraX.Date >= 1 and bg_current != "bg restaurant":
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in LauraX.DailyActions and "cheek" not in LauraX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if LauraX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in LauraX.DailyActions and (Player.Male or "girltalk" in LauraX.History):
            #If you've caught Laura showering today
            $ Options.append("showercaught")
        if "fondle breasts" in LauraX.DailyActions or "fondle pussy" in LauraX.DailyActions or "fondle ass" in LauraX.DailyActions:
            #If you've fondled Laura today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in LauraX.Inventory and "256 Shades of Grey" in LauraX.Inventory and "Avengers Tower Penthouse" in LauraX.Inventory:
            #If you've given Laura the books
            if "book" not in LauraX.Chat:
                $ Options.append("booked")
        if "lace bra" in LauraX.Inventory or "lace panties" in LauraX.Inventory:
            #If you've given Laura the lingerie
            if "lingerie" not in LauraX.Chat:
                $ Options.append("lingerie")
        if LauraX.Hand and Player.Male:
            #If Laura's given a handjob
            $ Options.append("handy")
        if LauraX.Blow and Player.Male:
            #If Laura's given a blowjob
            $ Options.append("blow")
        if LauraX.Swallow:
            #If Laura's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in LauraX.DailyActions or "painted" in LauraX.DailyActions:
            #If Laura's been facialed
            $ Options.append("facial")
        if LauraX.Sleep:
            #If Laura's slept over
            $ Options.append("sleep")
        if (LauraX.CreamP or LauraX.CreamA) and Player.Male:
            #If Laura's been creampied
            $ Options.append("creampie")
        if LauraX.Sex or LauraX.Anal:
            #If Laura's been sexed
            $ Options.append("sexed")
        if LauraX.Anal:
            #If Laura's been analed
            $ Options.append("anal")

        if "seenpeen" in LauraX.History and Player.Male:
            $ Options.append("seenpeen")
        if "topless" in LauraX.History:
            $ Options.append("topless")
        if "bottomless" in LauraX.History:
            $ Options.append("bottomless")

#        if not LauraX.Chat[0] and LauraX.Sex:
#            $ Options.append("virgin")

#        if (bg_current == "bg laura" or bg_current == "bg player") and "relationship" not in LauraX.DailyActions:
#            if "lover" not in LauraX.Petnames and ApprovalCheck(LauraX, 900, "L"): # LauraX.Event[6]
#                $ Options.append("lover?")
#            elif "sir" not in LauraX.Petnames and ApprovalCheck(LauraX, 500, "O"): # LauraX.Event[7]
#                $ Options.append("sir?")
#            elif "daddy" not in LauraX.Petnames and ApprovalCheck(LauraX, 750, "L") and ApprovalCheck(LauraX, 500, "O") and ApprovalCheck(LauraX, 500, "I"): # LauraX.Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in LauraX.Petnames and ApprovalCheck(LauraX, 900, "O"): # LauraX.Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in LauraX.Petnames and ApprovalCheck(LauraX, 500, "I"): # LauraX.Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in LauraX.Petnames and ApprovalCheck(LauraX, 900, "I"): # LauraX.Event[10]
#                $ Options.append("fuckbuddy?")


        if not ApprovalCheck(LauraX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ LauraX.DailyActions.append("cologne chat")
        $ LauraX.FaceChange("confused")
        ch_l "(нюх-нюх). . . пахнет. . . обезьяной . . ."
        $ LauraX.FaceChange("sexy", 2)
        ch_l ". . . хочешь заняться чем-нибудь попозже?"
    elif Options[0] == "purple":
        $ LauraX.DailyActions.append("cologne chat")
        $ LauraX.FaceChange("sly",1)
        ch_l "(нюх-нюх). . . что это? . ."
        $ LauraX.FaceChange("normal",0)
        ch_l ". . . ты что-нибудь хочешь?"
    elif Options[0] == "corruption":
        $ LauraX.DailyActions.append("cologne chat")
        $ LauraX.FaceChange("confused")
        ch_l "(нюх-нюх). . .  сильный запах. . ."
        $ LauraX.FaceChange("angry")
        ch_l ". . . опасный запах. . ."
        $ LauraX.FaceChange("sly")

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in LauraX.Chat:
                    ch_l "Мы должны быть осторожнее, чтобы не попасться."
                    if not ApprovalCheck(LauraX, 500, "I"):
                         ch_l "Пока что. . ."
            else:
                    ch_l "Извини, что нас потащили в кабинет профессора."
                    if not ApprovalCheck(LauraX, 500, "I"):
                        ch_l "Думаю, тебе больше не захочется заниматься подобным на людях."
                    else:
                        ch_l "Хотя мне это даже понравилось. . ."
                    $ LauraX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if LauraX.SEXP <= 15:
                ch_l "Я дала тебе ключ для удобства, не злоупотребляй его использованием. . ."
            else:
                ch_l "Я дала тебе ключ, но ты не приходишь. . ."
            $ LauraX.Chat.append("key")

#    elif Options[0] == "cheek":
#            #Laura's response to having her cheek touched.
#            ch_l "So,[LauraX.Petname]. . .y'know how you[LauraX.like]kinda just brushed my cheek before?"
#            ch_p "Yeah?  Was that okay?"
#            $ LauraX.FaceChange("smile",1)
#            ch_l "More than just {i}okay{/i}."
#            $ LauraX.Chat.append("cheek")


    elif Options[0] == "laura":
            #if she never told you her name. . .
            ch_l "О, да, кстати, меня также зовут \"Лора.\" Лора Кинни."
            $ LauraX.Names.append("Laura")
            menu:
                "О, красивое имя. Пожалуй, стоит звать тебя так.":
                        $ LauraX.Statup("Love", 70, 5) # Love
                        $ LauraX.Name = "Лора"
                        $ LauraX.Name_rod = "Лоры"
                        $ LauraX.Name_dat = "Лоре"
                        $ LauraX.Name_vin = "Лору"
                        $ LauraX.Name_tvo = "Лорой"
                        $ LauraX.Name_pre = "Лоре"
                "Ладно, но Икс-23 звучит круче.":
                        $ LauraX.Statup("Love", 70, -2) # Love
                        $ LauraX.Statup("Obed", 70, 5) # Obed
                        $ LauraX.Name = "Икс-23"
                        $ LauraX.Name_rod = "Икс-23"
                        $ LauraX.Name_dat = "Икс-23"
                        $ LauraX.Name_vin = "Икс-23"
                        $ LauraX.Name_tvo = "Икс-23"
                        $ LauraX.Name_pre = "Икс-23"

    elif Options[0] == "dated":
            #Laura's response to having gone on a date with the Player.
            ch_l "Вчера было весело, надо как-нибудь повторить."

    elif Options[0] == "kissed":
            #Laura's response to having been kissed by the Player.
            $ LauraX.FaceChange("normal",1)
            ch_l "Ты очень хорошо целуешься, [LauraX.Petname]."
            menu:
                extend ""
                "Эй. . . Да я лучшая." if not Player.Male:
                        $ LauraX.FaceChange("smile",1)
                        ch_l "Тебе придется это доказать."
                "Эй. . . Да я лучший." if Player.Male:
                        $ LauraX.FaceChange("smile",1)
                        ch_l "Тебе придется это доказать."
                "Ты правда так думаешь?":
                        ch_l "Разве я похожа на шута?"

    elif Options[0] == "dangerroom":
            #Laura's response to Player working out in the Danger Room while Laura is present
            $ LauraX.FaceChange("sly",1)
            ch_l "Слушай, [LauraX.Petname]. Я наблюдала за тобой в комнате Опасности."
            ch_l "Тебе стоит держать левую руку выше, ты пропускаешь слишком много ударов в голову."

    elif Options[0] == "showercaught":
            #Laura's response to being caught in the shower.
            if "shower" in LauraX.Chat:
                if not Player.Male:
                    ch_l "Ты снова видела, как я принимала душ. . ."
                else:
                    ch_l "Ты снова видел, как я принимала душ. . ."
            else:
                ch_l "У тебя что, привычка так нагло врываться в душ?"
                $ LauraX.Chat.append("shower")
                menu:
                    extend ""
                    "Это чистая случайность! Клянусь!":
                            $ LauraX.Statup("Love", 50, 5)
                            $ LauraX.Statup("Love", 90, 2)
                            if ApprovalCheck(LauraX, 1200):
                                $ LauraX.FaceChange("sly",1)
                                ch_l "Я не возражаю."
                            $ LauraX.FaceChange("smile")
                            ch_l "Мы все совершаем ошибки."
                    "Только если там ты.":
                            $ LauraX.Statup("Obed", 40, 5)
                            if ApprovalCheck(LauraX, 1000) or ApprovalCheck(LauraX, 700, "L"):
                                    $ LauraX.Statup("Love", 90, 3)
                                    $ LauraX.FaceChange("sly",1)
                                    ch_l "Хмм, приму за комплимент."
                            else:
                                    $ LauraX.Statup("Love", 70, -5)
                                    $ LauraX.FaceChange("angry")
                                    ch_l "Думаю, мне следует обидеться."
                    "Я заглянула умышленно. Но я ни о чем не жалею." if not Player.Male:
                            if ApprovalCheck(LauraX, 1200):
                                    $ LauraX.Statup("Love", 90, 3)
                                    $ LauraX.Statup("Obed", 70, 10)
                                    $ LauraX.Statup("Inbt", 50, 5)
                                    $ LauraX.FaceChange("sly",1)
                                    ch_l "Кажется, ты знаешь, чего хочешь."
                            elif ApprovalCheck(LauraX, 800):
                                    $ LauraX.Statup("Obed", 60, 5)
                                    $ LauraX.Statup("Inbt", 50, 5)
                                    $ LauraX.FaceChange("perplexed",2)
                                    ch_l "Я хочу, чтобы ты проявила инициативу."
                                    $ LauraX.Blush = 1
                            else:
                                    $ LauraX.Statup("Love", 50, -10)
                                    $ LauraX.Statup("Love", 80, -10)
                                    $ LauraX.Statup("Obed", 50, 10)
                                    $ LauraX.FaceChange("angry")
                                    ch_l "Ты меня пугаешь."
                    "Я заглянул умышленно. Но я ни о чем не жалею." if Player.Male:
                            if ApprovalCheck(LauraX, 1200):
                                    $ LauraX.Statup("Love", 90, 3)
                                    $ LauraX.Statup("Obed", 70, 10)
                                    $ LauraX.Statup("Inbt", 50, 5)
                                    $ LauraX.FaceChange("sly",1)
                                    ch_l "Кажется, ты знаешь, чего хочешь."
                            elif ApprovalCheck(LauraX, 800):
                                    $ LauraX.Statup("Obed", 60, 5)
                                    $ LauraX.Statup("Inbt", 50, 5)
                                    $ LauraX.FaceChange("perplexed",2)
                                    ch_l "Я хочу, чтобы ты проявил инициативу."
                                    $ LauraX.Blush = 1
                            else:
                                    $ LauraX.Statup("Love", 50, -10)
                                    $ LauraX.Statup("Love", 80, -10)
                                    $ LauraX.Statup("Obed", 50, 10)
                                    $ LauraX.FaceChange("angry")
                                    ch_l "Ты меня пугаешь."

    elif Options[0] == "fondled":
            #Laura's response to being felt up.
            if LauraX.FondleB + LauraX.FondleP + LauraX.FondleA >= 15:
                ch_l "Я хочу почувствовать твои прикосновения."
            else:
                ch_l "Ты можешь потрогать меня, если хочешь."

    elif Options[0] == "booked":
            #Laura's response after a Player gives her the books from the shop.
            if not Player.Male:
                ch_l "Слушай, я прочитала те книги, которые ты мне дал."
            else:
                ch_l "Слушай, я прочитала те книги, которые ты мне дал."
            menu:
                extend ""
                "Да?  И как тебе?":
                        $ LauraX.FaceChange("sly",2)
                        ch_l "Они. . .{i}интересные{/i}."
                "Хорошо. Пожалуй, ты могла бы чему-нибудь из них научиться.":
                        $ LauraX.Statup("Love", 90, -3)
                        $ LauraX.Statup("Obed", 70, 5)
                        $ LauraX.Statup("Inbt", 50, 5)
                        $ LauraX.FaceChange("angry")
                        ch_l "Не понимаю чему."
            $ LauraX.Blush = 1
            $ LauraX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Laura's response to being given lingerie.
            $ LauraX.FaceChange("sly",2)
            if not Player.Male:
                ch_l "Нижнее белье, которое ты мне подарила, немного неудобное, но зато красивое."
            else:
                ch_l "Нижнее белье, которое ты мне подарил, немного неудобное, но зато красивое."
            $ LauraX.Blush = 1
            $ LauraX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Laura's response after giving the Player a handjob.
            $ LauraX.FaceChange("sly",1)
            ch_l "На днях я думала о твоем члене в моей руке. . ."
            ch_l "Похоже, тебе понравилось."
            $ LauraX.Blush = 0

    elif Options[0] == "blow":
            if "blow" not in LauraX.Chat:
                    #Laura's response after giving the Player a blowjob.
                    $ LauraX.FaceChange("sly",2)
                    ch_l "Тебе понравился тот минет?"
                    menu:
                        extend ""
                        "Ты была великолепна.":
                                    $ LauraX.Statup("Love", 90, 5)
                                    $ LauraX.Statup("Inbt", 60, 10)
                                    $ LauraX.FaceChange("normal",1)
                                    ch_l "Хорошо. Это хорошо. . . "
                                    $ LauraX.FaceChange("sexy",1)
                                    ch_l "Я бы хотела как-нибудь повторить."
                        "Честно? Все было хорошо. . . но, думаю, тебе не помешает еще немного попрактиковаться.":
                                if ApprovalCheck(LauraX, 300, "I") or not ApprovalCheck(LauraX, 800):
                                    $ LauraX.Statup("Love", 90, -5)
                                    $ LauraX.Statup("Obed", 60, 10)
                                    $ LauraX.Statup("Inbt", 50, 10)
                                    $ LauraX.FaceChange("perplexed",1)
                                    ch_l "Да? Извини, что разочаровала."
                                else:
                                    $ LauraX.Statup("Obed", 70, 15)
                                    $ LauraX.Statup("Inbt", 50, 5)
                                    $ LauraX.FaceChange("sexy",1)
                                    ch_l "Да? Думаю, нам нужно продолжать, пока я не научусь делать все правильно."
                        "Угу, если бы мне нравились стремные звуки и шкрябанье зубов по члену, но это далеко не так.":
                                $ LauraX.Statup("Love", 90, -10)
                                $ LauraX.Statup("Obed", 60, 10)
                                $ LauraX.FaceChange("angry",2)
                                ch_l "Ну что ж, тогда удачи."
                    $ LauraX.Blush = 1
                    $ LauraX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["Я должна сказать тебе, твой член великолепен на вкус.",
                            "Кажется, в прошлый раз я чуть не вывихнула челюсть.",
                            "Дай мне знать, если когда-нибудь захочешь еще один минет.",
                            "Мммм. . . [Стучит языком по внутренней стороне щеки.]"])
                    ch_l "[Line]"

    elif Options[0] == "swallowed":
            #Laura's response after swallowing the Player's cum.
            if "swallow" in LauraX.Chat:
                ch_l "Слушай, я не против когда-нибудь снова попробовать тебя."
            else:
                ch_l "Так вот. . . в тот день. . ."
                if not Player.Male:
                    ch_l "Мне впервые понравились соки на вкус."
                else:
                    ch_l "Мне впервые понравилась сперма на вкус."
                $ LauraX.FaceChange("sly",1)
                ch_l "Хорошая работа!"
                $ LauraX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Laura's response after taking a facial from the Player.
            ch_l "Хм. . . Знаю, это прозвучит странно. . ."
            $ LauraX.FaceChange("sexy",2)
            if not Player.Male:
                ch_l "Я чувствую себя так {i}хорошо{/i} с твоими соками на своем лице."
            else:
                ch_l "Я чувствую себя так {i}хорошо{/i} с твоей спермой на своем лице."
            $ LauraX.Blush = 1

    elif Options[0] == "sleepover":
            #Laura's response after sleeping with the Player.
            ch_l "Мне очень понравилась та ночь."
            ch_l "Я чувствовала себя в такой безопастности, лежа в кровати с кем-то, помимо себя."

    elif Options[0] == "creampie":
            #Another of Laura's responses after having sex with the Player.
            "[LauraX.Name] сближается с вами, чтобы прошептать вам на ухо."
            if not Player.Male:
                ch_l "Я все еще чувствую, как твои. . . стекают по внутренней стороне моего бедра."
            else:
                ch_l "Я все еще чувствую, как твоя. . . стекает по внутренней стороне моего бедра."

    elif Options[0] == "sexed":
            #A final response from Laura after having sex with the Player.
            if not Player.Male:
                ch_l "Что ж. . . Ты должна знать. . ."
            else:
                ch_l "Что ж. . . Ты должен знать. . ."
            $ LauraX.FaceChange("sexy",2)
            ch_l ". . .в последнее время, когда я играюсь со своей фасолинкой. . ."
            ch_l "Я думаю о тебе. . . внутри себя."
            $ LauraX.Blush = 1

    elif Options[0] == "anal":
            #Laura's response after getting anal from the Player.
            $ LauraX.FaceChange("sly")
            ch_l "Мне не очень нравился анал."
            $ LauraX.FaceChange("sexy",1)
            ch_l "Ну, по крайней мере, до тебя."

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ LauraX.FaceChange("sly",1, Eyes="down")
            ch_l "Я забыла сказать, у тебя очень красивый член. . ."
            $ LauraX.FaceChange("bemused",1)
            $ LauraX.Statup("Love", 50, 5)
            $ LauraX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            ch_l "Слушай, что скажешь о моих сиськах?"
            ch_l "Они тебе понравились?"
            call Girl_First_TMenu
            $ LauraX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            if not Player.Male:
                ch_l "Слушай, что ты подумала, когда впервые увидела мою киску?"
            else:
                ch_l "Слушай, что ты подумал, когда впервые увидел мою киску?"
            call Girl_First_BMenu
            $ LauraX.History.remove("bottomless")

#    elif Options[0] == "boyfriend?":
#        call Laura_BF
#    elif Options[0] == "lover?":
#        call Laura_Love
#    elif Options[0] == "sir?":
#        call Laura_Sub
#    elif Options[0] == "master?":
#        call Laura_Master
#    elif Options[0] == "sexfriend?":
#        call Laura_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Laura_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Laura_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Отойди от меня.",
                "Я не хочу чувствовать тебя рядом с собой.",
                "Назад.",
                "Отвали."])
        ch_l "[Line]"

    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 21)
            if D20 == 1:
                    $ LauraX.FaceChange("smile")
                    ch_l "Я получила хорошую оценку за тот тест по биологии."
            elif D20 == 2:
                    $ LauraX.FaceChange("angry")
                    ch_l "Если я еще раз услышу от него \"я лучший\", клянусь, я уйду. . ."
            elif D20 == 3:
                    $ LauraX.FaceChange("surprised")
                    ch_l "А? Ох, извини. Я растерялась. Это так не похоже на меня."
            elif D20 == 4:
                    $ LauraX.FaceChange("sad")
                    ch_l "Ох, [LauraX.Petname]. Не беспокойся. Я просто кое-что вспомнила."
            elif D20 == 5:
                    $ LauraX.FaceChange("smile")
                    ch_l "Я так хорошо поспала. Приятно находиться в месте, где можно спать, не беспокоясь о своей безопасности."
            elif D20 == 6:
                    $ LauraX.FaceChange("perplexed")
                    ch_l "Ох, [LauraX.Petname]. Кажется, я только что видела, как Эмма Фрост пялится на Циклопа. Это было так. . . странно."
            elif D20 == 7:
                    $ LauraX.FaceChange("smile")
                    ch_l "Я только что побила свой рекорд в Комнате Опасности."
            elif D20 == 8:
                    $ LauraX.FaceChange("sad")
                    ch_l "Мне нравится находиться тут, но иногда здесь бывает так шумно. . ."
            elif D20 == 9:
                    $ LauraX.FaceChange("confused")
                    ch_l "Я все никак не пойму, что за странное мясо было сегодня в столовой."
                    ch_l "У меня отличное обоняние, но даже с ним я не могу понять!"
            elif D20 == 10:
                    $ LauraX.FaceChange("smile")
                    ch_l "Китти, Роуг и еще несколько ребят позвали меня поесть с ними мороженное."
            elif D20 == 11:
                    $ LauraX.FaceChange("smile")
                    ch_l "Я сходила на занятие по танцам, как мне сказала Китти. Похоже, у меня хорошо получается."
            elif D20 == 12:
                    $ LauraX.FaceChange("sad")
                    ch_l "Мне нравится общаться с Китти и другими. Это заставляет меня чувствовать себя, я не знаю. . ."
                    ch_l "{i}не{/i} очень опасным мутантом, который запросто может всех выпотрошить."
            elif D20 == 13:
                    $ LauraX.FaceChange("smile")
                    ch_l "Китти и Роуг посмели назвать Логана моим \"папой\". Я думаю, мы могли довести его до сердечного приступа."
            elif D20 == 14:
                    $ LauraX.FaceChange("sad")
                    ch_l "Я люблю ходить на задания, но узнавать, что произошло, пока меня не было, всегда больно."
            elif D20 == 15:
                    $ LauraX.FaceChange("perplexed")
                    ch_l "Их называют \"Мстителями\", но разве они когда-нибудь мстят?"
                    ch_l "Взять, например, Фантастическую четверку: они на самом деле делают странные и фантастические вещи."
            elif D20 == 16:
                    $ LauraX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_l "Ты когда-нибудь бывала в Нью-Йорке? Я удивляюсь, что кто-то все еще желает там жить."
                    else:
                        ch_l "Ты когда-нибудь бывал в Нью-Йорке? Я удивляюсь, что кто-то все еще желает там жить."
            elif D20 == 17:
                    $ LauraX.FaceChange("perplexed")
                    ch_l "Логан как-то подошел ко мне и сказал, что если я когда-нибудь встречу кого-то по имени. . ."
                    ch_l "\"Дед. . .пул?\". . . Я должна сразу же дать ему в морду."
                    ch_l "Кто это вообще такой?"
            elif D20 == 18:
                    $ LauraX.FaceChange("smile")
                    ch_l "Никому не говори об этом, но я думаю, что Циклоп слегка зажатый."
            elif D20 == 19:
                    $ LauraX.FaceChange("confused")
                    ch_l "Ты чувствуешь? Пахнет. . . начос и. . . шоколадным сиропом?!"
            elif D20 == 20:
                    $ LauraX.FaceChange("smile")
                    ch_l "Мне нравится просто болтать ни о чем. Это так. . . приятно."
            else:
                    $ LauraX.FaceChange("smile")
                    ch_l "С тобой весело проводить время."

    $ Line = 0
    return

# start Laura_Names//////////////////////////////////////////////////////////
label Laura_Names:
    menu:
        ch_l "А? Как тебе хочется, чтобы я тебя звала?"
        "Зови по инициалам.":
            $ LauraX.Petname = Player.Name[:1]  #fix test this
            $ LauraX.Petname_rod = Player.Name[:1]
            $ LauraX.Petname_dat = Player.Name[:1]
            $ LauraX.Petname_vin = Player.Name[:1]
            $ LauraX.Petname_tvo = Player.Name[:1]
            $ LauraX.Petname_pre = Player.Name[:1]
            ch_l "Поняла, [LauraX.Petname]."
        "Зови меня по имени.":
            $ LauraX.Petname = Player.Name
            $ LauraX.Petname_rod = Player.Name_rod
            $ LauraX.Petname_dat = Player.Name_dat
            $ LauraX.Petname_vin = Player.Name_vin
            $ LauraX.Petname_tvo = Player.Name_tvo
            $ LauraX.Petname_pre = Player.Name_pre
            ch_l "Если ты этого хочешь, [LauraX.Petname]."
        "Зови меня \"моя девушка\"." if "boyfriend" in LauraX.Petnames and not Player.Male:
            $ LauraX.Petname = "моя девушка"
            $ LauraX.Petname_rod = "моей девушки"
            $ LauraX.Petname_dat = "моей девушке"
            $ LauraX.Petname_vin = "мою девушку"
            $ LauraX.Petname_tvo = "моей девушкой"
            $ LauraX.Petname_pre = "моей девушке"
            ch_l "Конечно, [LauraX.Petname]."
        "Зови меня \"мой парень\"." if "boyfriend" in LauraX.Petnames and Player.Male:
            $ LauraX.Petname = "мой парень"
            $ LauraX.Petname_rod = "моего парня"
            $ LauraX.Petname_dat = "моему парню"
            $ LauraX.Petname_vin = "моего парня"
            $ LauraX.Petname_tvo = "моим парнем"
            $ LauraX.Petname_pre = "моем парне"
            ch_l "Конечно, [LauraX.Petname]."
        "Зови меня \"любимый\"." if "lover" in LauraX.Petnames and Player.Male:
            $ LauraX.Petname = "любимый"
            $ LauraX.Petname_rod = "любимого"
            $ LauraX.Petname_dat = "любимому"
            $ LauraX.Petname_vin = "любимого"
            $ LauraX.Petname_tvo = "любимым"
            $ LauraX.Petname_pre = "любимом"
            ch_l "Ооох, мне нравится, [LauraX.Petname]."
        "Зови меня \"любимая\"." if "lover" in LauraX.Petnames and not Player.Male:
            $ LauraX.Petname = "любимая"
            $ LauraX.Petname_rod = "любимой"
            $ LauraX.Petname_dat = "любимой"
            $ LauraX.Petname_vin = "любимую"
            $ LauraX.Petname_tvo = "любимой"
            $ LauraX.Petname_pre = "любимой"
            ch_l "Ооох, мне нравится, [LauraX.Petname]."
        "Зови меня \"господин\"." if "sir" in LauraX.Petnames and Player.Male:
            $ LauraX.Petname = "господин"
            $ LauraX.Petname_rod = "господина"
            $ LauraX.Petname_dat = "господину"
            $ LauraX.Petname_vin = "господина"
            $ LauraX.Petname_tvo = "господином"
            $ LauraX.Petname_pre = "господине"
            ch_l "Да, [LauraX.Petname]."
        "Зови меня \"госпожа\"." if "sir" in LauraX.Petnames and not Player.Male:
            $ LauraX.Petname = "госпожа"
            $ LauraX.Petname_rod = "госпожи"
            $ LauraX.Petname_dat = "госпоже"
            $ LauraX.Petname_vin = "госпожу"
            $ LauraX.Petname_tvo = "госпожой"
            $ LauraX.Petname_pre = "госпоже"
            ch_l "Да, [LauraX.Petname]."
        "Зови меня \"хозяйка\"." if "master" in LauraX.Petnames and not Player.Male:
            $ LauraX.Petname = "хозяйка"
            $ LauraX.Petname_rod = "хозяйки"
            $ LauraX.Petname_dat = "хозяйке"
            $ LauraX.Petname_vin = "хозяйку"
            $ LauraX.Petname_tvo = "хозяйкой"
            $ LauraX.Petname_pre = "хозяйке"
            ch_l "Как пожелаешь, [LauraX.Petname]."
        "Зови меня \"хозяин\"." if "master" in LauraX.Petnames and Player.Male:
            $ LauraX.Petname = "хозяин"
            $ LauraX.Petname_rod = "хозяина"
            $ LauraX.Petname_dat = "хозяину"
            $ LauraX.Petname_vin = "хозяина"
            $ LauraX.Petname_tvo = "хозяином"
            $ LauraX.Petname_pre = "хозяине"
            ch_l "Как пожелаешь, [LauraX.Petname]."
        "Зови меня \"любовница\"." if "sex friend" in LauraX.Petnames and not Player.Male:
            $ LauraX.Petname = "любовница"
            $ LauraX.Petname_rod = "любовницы"
            $ LauraX.Petname_dat = "любовнице"
            $ LauraX.Petname_vin = "любовницу"
            $ LauraX.Petname_tvo = "любовницей"
            $ LauraX.Petname_pre = "любовнице"
            ch_l "Хех, как скажешь, [LauraX.Petname]."
        "Зови меня \"любовник\"." if "sex friend" in LauraX.Petnames and Player.Male:
            $ LauraX.Petname = "любовник"
            $ LauraX.Petname_rod = "любовника"
            $ LauraX.Petname_dat = "любовнику"
            $ LauraX.Petname_vin = "любовника"
            $ LauraX.Petname_tvo = "любовником"
            $ LauraX.Petname_pre = "любовнике"
            ch_l "Хех, как скажешь, [LauraX.Petname]."
        "Зови меня \"секс-партнерша\"." if "fuck buddy" in LauraX.Petnames and not Player.Male:
            $ LauraX.Petname = "секс-партнерша"
            $ LauraX.Petname_rod = "секс-партнерши"
            $ LauraX.Petname_dat = "секс-партнерше"
            $ LauraX.Petname_vin = "секс-партнершу"
            $ LauraX.Petname_tvo = "секс-партнершей"
            $ LauraX.Petname_pre = "секс-партнерше"
            ch_l "Я в деле, если ты готов, [LauraX.Petname]."
        "Зови меня \"секс-партнер\"." if "fuck buddy" in LauraX.Petnames and Player.Male:
            $ LauraX.Petname = "секс-партнер"
            $ LauraX.Petname_rod = "секс-партнера"
            $ LauraX.Petname_dat = "секс-партнеру"
            $ LauraX.Petname_vin = "секс-партнера"
            $ LauraX.Petname_tvo = "секс-партнером"
            $ LauraX.Petname_pre = "секс-партнере"
            ch_l "Я в деле, если ты готова, [LauraX.Petname]."
        "Зови меня \"мамочка\"." if "daddy" in LauraX.Petnames and not Player.Male:
            $ LauraX.Petname = "мамочка"
            $ LauraX.Petname_rod = "мамочки"
            $ LauraX.Petname_dat = "мамочке"
            $ LauraX.Petname_vin = "мамочку"
            $ LauraX.Petname_tvo = "мамочкой"
            $ LauraX.Petname_pre = "мамочке"
            ch_l "Ох! Буду, можешь не сомневаться, [LauraX.Petname]."
        "Зови меня \"папочка\"." if "daddy" in LauraX.Petnames and Player.Male:
            $ LauraX.Petname = "папочка"
            $ LauraX.Petname_rod = "папочки"
            $ LauraX.Petname_dat = "папочке"
            $ LauraX.Petname_vin = "папочку"
            $ LauraX.Petname_tvo = "папочкой"
            $ LauraX.Petname_pre = "папочке"
            ch_l "Ох! Буду, можешь не сомневаться, [LauraX.Petname]."
        "\"Дружок\" в самый раз. [[\"bub\"]" if Player.Male:
            $ LauraX.Petname = "дружок"
            "CreDz" "В мульте Логан ака Росомаха кидает \"bub\" направо и налево. Хз как перевели в ру локализации."
            ch_l "Поняла, дружок."
        "Неважно.":
            return
    return
# end Laura_Names//////////////////////////////////////////////////////////

label Laura_Pet:
    while 1:
        menu:
            extend ""
            "Обходительно":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "Лора." if "Laura" in LauraX.Names:
                        $ LauraX.Pet_rod = "Лоры"
                        $ LauraX.Pet_dat = "Лоре"
                        $ LauraX.Pet_vin = "Лору"
                        $ LauraX.Pet_tvo = "Лорой"
                        $ LauraX.Pet_pre = "Лоре"
                        $ LauraX.Pet = "Лора"
                        ch_l "Без проблем, [LauraX.Petname]."

                    "Икс-23.":
                        $ LauraX.Pet = "Икс-23"
                        $ LauraX.Pet_rod = "Икс-23"
                        $ LauraX.Pet_dat = "Икс-23"
                        $ LauraX.Pet_vin = "Икс-23"
                        $ LauraX.Pet_tvo = "Икс-23"
                        $ LauraX.Pet_pre = "Икс-23"
                        if ApprovalCheck(LauraX, 700, "L") and not ApprovalCheck(LauraX, 500, "O"):
                                ch_l "Ох, как скажешь, [LauraX.Petname]."
                        else:
                                ch_l "Без проблем, [LauraX.Petname]."

                    "\"моя девушка\".":
                        if "boyfriend" in LauraX.Petnames:
                            $ LauraX.Pet = "моя девушка"
                            $ LauraX.Pet_rod = "моей девушки"
                            $ LauraX.Pet_dat = "моей девушке"
                            $ LauraX.Pet_vin = "мою девушку"
                            $ LauraX.Pet_tvo = "моей девушкой"
                            $ LauraX.Pet_pre = "моей девушке"
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "Я полностью твоя, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry")
                            ch_l "Я НЕ твоя девушка, [LauraX.Petname]."

                    "\"детка\".":
                        if "boyfriend" in LauraX.Petnames or ApprovalCheck(LauraX, 700, "L"):
                            $ LauraX.Pet = "детка"
                            $ LauraX.Pet_rod = "детки"
                            $ LauraX.Pet_dat = "детке"
                            $ LauraX.Pet_vin = "детку"
                            $ LauraX.Pet_tvo = "деткой"
                            $ LauraX.Pet_pre = "детке"
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "Я твоя детка, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry")
                            ch_l "Я тебе НЕ детка, [LauraX.Petname]."

                    "\"крошка\".":
                        if "boyfriend" in LauraX.Petnames or ApprovalCheck(LauraX, 600, "L"):
                            $ LauraX.Pet = "крошка"
                            $ LauraX.Pet_rod = "крошки"
                            $ LauraX.Pet_dat = "крошке"
                            $ LauraX.Pet_vin = "крошку"
                            $ LauraX.Pet_tvo = "крошкой"
                            $ LauraX.Pet_pre = "крошке"
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "Я твоя крошка, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry")
                            ch_l "Я тебе НЕ крошка, [LauraX.Petname]."

                    "\"малышка\".":
                        if "boyfriend" in LauraX.Petnames or ApprovalCheck(LauraX, 500, "L"):
                            $ LauraX.Pet = "малышка"
                            $ LauraX.Pet_rod = "малышки"
                            $ LauraX.Pet_dat = "малышке"
                            $ LauraX.Pet_vin = "малышку"
                            $ LauraX.Pet_tvo = "малышкой"
                            $ LauraX.Pet_pre = "малышке"
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "Мило, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry")
                            ch_l "Я тебе НЕ малышка."


                    "\"милая\".":
                        if "boyfriend" in LauraX.Petnames or ApprovalCheck(LauraX, 600, "L"):
                            $ LauraX.Pet = "милая"
                            $ LauraX.Pet_rod = "милой"
                            $ LauraX.Pet_dat = "милой"
                            $ LauraX.Pet_vin = "милую"
                            $ LauraX.Pet_tvo = "милой"
                            $ LauraX.Pet_pre = "милой"
                            ch_l "Оу, как мило, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Слишком приторно, [LauraX.Petname]."

                    "\"секси\".":
                        if "lover" in LauraX.Petnames or ApprovalCheck(LauraX, 800):
                            $ LauraX.Pet = "секси"
                            $ LauraX.Pet_rod = "секси"
                            $ LauraX.Pet_dat = "секси"
                            $ LauraX.Pet_vin = "секси"
                            $ LauraX.Pet_tvo = "секси"
                            $ LauraX.Pet_pre = "секси"
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "Тебе виднее, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Ты перегибаешь, [LauraX.Petname]."

                    "\"любимая\".":
                        if "lover" in LauraX.Petnames or ApprovalCheck(LauraX, 1200):
                            $ LauraX.Pet = "любимая"
                            $ LauraX.Pet_rod = "любимой"
                            $ LauraX.Pet_dat = "любимой"
                            $ LauraX.Pet_vin = "любимую"
                            $ LauraX.Pet_tvo = "любимой"
                            $ LauraX.Pet_pre = "любимой"
                            $ LauraX.FaceChange("sexy", 1)
                            ch_l "Я знаю."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Я так не думаю, [LauraX.Petname]."

                    "\"Роси\".":
                        if ApprovalCheck(LauraX, 500, "I"):
                            $ LauraX.FaceChange("sexy", 1)
                            $ LauraX.Pet = "Роси"
                            $ LauraX.Pet_rod = "Роси"
                            $ LauraX.Pet_dat = "Роси"
                            $ LauraX.Pet_vin = "Роси"
                            $ LauraX.Pet_tvo = "Роси"
                            $ LauraX.Pet_pre = "Роси"
                            ch_l "Хех, ладно, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry")
                            ch_l "Не так уж и мило, [LauraX.Petname]."

                    "Назад":
                        pass

            "Грубо":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "\"рабыня\".":
                        if "master" in LauraX.Petnames or ApprovalCheck(LauraX, 800, "O"):
                            $ LauraX.Pet = "рабыня"
                            $ LauraX.Pet_rod = "рабыни"
                            $ LauraX.Pet_dat = "рабыне"
                            $ LauraX.Pet_vin = "рабыню"
                            $ LauraX.Pet_tvo = "рабыней"
                            $ LauraX.Pet_pre = "рабыне"
                            $ LauraX.FaceChange("bemused", 1)
                            ch_l "Как пожелаешь, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Я не твоя рабыня, [LauraX.Petname]."

                    "\"питомец\".":
                        if "master" in LauraX.Petnames or ApprovalCheck(LauraX, 650, "O"):
                            $ LauraX.Pet = "питомец"
                            $ LauraX.Pet_rod = "питомце"
                            $ LauraX.Pet_dat = "питомцу"
                            $ LauraX.Pet_vin = "питомца"
                            $ LauraX.Pet_tvo = "питомцем"
                            $ LauraX.Pet_pre = "питомце"
                            $ LauraX.FaceChange("bemused", 1)
                            ch_l "Можешь погладить меня, если хочешь, [LauraX.Petname]."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Я не твой питомец, [LauraX.Petname]."

                    "\"шлюха\".":
                        if "sex friend" in LauraX.Petnames or ApprovalCheck(LauraX, 900, "OI"):
                            $ LauraX.Pet = "шлюха"
                            $ LauraX.Pet_rod = "шлюхи"
                            $ LauraX.Pet_dat = "шлюхе"
                            $ LauraX.Pet_vin = "шлюху"
                            $ LauraX.Pet_tvo = "шлюхой"
                            $ LauraX.Pet_pre = "шлюхе"
                            $ LauraX.FaceChange("sexy")
                            ch_l "Логично."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            $ LauraX.Mouth = "surprised"
                            ch_l "Я бы хотела посмотреть, как ты попробуешь произнести это со сломанной челюстью."

                    "\"блядь\".":
                        if "fuckbuddy" in LauraX.Petnames or ApprovalCheck(LauraX, 1000, "OI"):
                            $ LauraX.Pet = "блядь"
                            $ LauraX.Pet_rod = "бляди"
                            $ LauraX.Pet_dat = "бляде"
                            $ LauraX.Pet_vin = "блядь"
                            $ LauraX.Pet_tvo = "блядью"
                            $ LauraX.Pet_pre = "бляде"
                            $ LauraX.FaceChange("sly")
                            ch_l "Ладно. . ."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Осторожнее, не то. . ."

                    "\"сладкогрудая\".":
                        if "sex friend" in LauraX.Petnames or ApprovalCheck(LauraX, 1400):
                            $ LauraX.Pet = "сладкогрудая"
                            $ LauraX.Pet_rod = "сладкогрудой"
                            $ LauraX.Pet_dat = "сладкогрудой"
                            $ LauraX.Pet_vin = "сладкогрудую"
                            $ LauraX.Pet_tvo = "сладкогрудой"
                            $ LauraX.Pet_pre = "сладкогрудой"
                            $ LauraX.FaceChange("sly", 1)
                            ch_l "Было бы это еще правдой."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Это не прикольно."

                    "\"любовница\".":
                        if "sex friend" in LauraX.Petnames or ApprovalCheck(LauraX, 600, "I"):
                            $ LauraX.Pet = "любовница"
                            $ LauraX.Pet_rod = "любовницы"
                            $ LauraX.Pet_dat = "любовнице"
                            $ LauraX.Pet_vin = "любовницу"
                            $ LauraX.Pet_tvo = "любовницей"
                            $ LauraX.Pet_pre = "любовнице"
                            $ LauraX.FaceChange("sly")
                            ch_l "Ага. . ."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Осторожнее выбирай слова, [LauraX.Petname]."

                    "\"секс-партнерша\".":
                        if "fuckbuddy" in LauraX.Petnames or ApprovalCheck(LauraX, 700, "I"):
                            $ LauraX.Pet = "секс-партнерша"
                            $ LauraX.Pet_rod = "секс-партнерши"
                            $ LauraX.Pet_dat = "секс-партнерше"
                            $ LauraX.Pet_vin = "секс-партнершу"
                            $ LauraX.Pet_tvo = "секс-партнершей"
                            $ LauraX.Pet_pre = "секс-партнерше"
                            $ LauraX.FaceChange("sly")
                            ch_l "Агась."
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            $ LauraX.Mouth = "surprised"
                            ch_l "Не шути так, [LauraX.Petname]."

                    "\"доченька\".":
                        if "daddy" in LauraX.Petnames or ApprovalCheck(LauraX, 1200):
                            $ LauraX.Pet = "доченька"
                            $ LauraX.Pet_rod = "доченьки"
                            $ LauraX.Pet_dat = "доченьке"
                            $ LauraX.Pet_vin = "доченьку"
                            $ LauraX.Pet_tvo = "доченькой"
                            $ LauraX.Pet_pre = "доченьке"
                            $ LauraX.FaceChange("smile", 1)
                            ch_l "Ладно?"
                        else:
                            $ LauraX.FaceChange("angry", 1)
                            ch_l "Это очень странно."

                    "Назад":
                        pass

            "Неважно.":
                return
    return

#label Laura_Namecheck(LauraX.Pet = LauraX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname


# start Laura_Rename//////////////////////////////////////////////////////////
label Laura_Rename:
        #Sets alternate names from Laura
        $ LauraX.Mouth = "smile"
        ch_l "Да?"
        menu:
            extend ""
            "Я думаю, \"Лора\" прекрасное имя." if LauraX.Name != "Лора" and "Laura" in LauraX.Names:
                    $ LauraX.Name = "Лора"
                    $ LauraX.Name_rod = "Лоры"
                    $ LauraX.Name_dat = "Лоре"
                    $ LauraX.Name_vin = "Лору"
                    $ LauraX.Name_tvo = "Лорой"
                    $ LauraX.Name_pre = "Лоре"
                    ch_l "Да, звучит неплохо."
            "Мне кажется, \"Икс-23\" звучит круто." if LauraX.Name != "Икс-23":
                    if not ApprovalCheck(LauraX, 500, "O") and not ApprovalCheck(LauraX, 800, "L"):
                            ch_l "Это имя я давно оставила в прошлом, лучше не надо. . ."
                    else:
                            if not ApprovalCheck(LauraX, 500, "O"):
                                    $ LauraX.FaceChange("sadside", 0,Brows="normal")
                            if "namechange" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Love", 70, -2)
                                    $ LauraX.Statup("Obed", 70, 5)
                            $ LauraX.Name = "Икс-23"
                            $ LauraX.Name_rod = "Икс-23"
                            $ LauraX.Name_dat = "Икс-23"
                            $ LauraX.Name_vin = "Икс-23"
                            $ LauraX.Name_tvo = "Икс-23"
                            $ LauraX.Name_pre = "Икс-23"
                            ch_l "Ох, конечно. . . Думаю, я смогу снова пользоваться этим именем. . ."
            "Мне нравится имя \"Росомаха.\"" if LauraX.Name != "Росомаха" and "Wolverine" in LauraX.Names:
                    $ LauraX.FaceChange("confused", 1)
                    if ApprovalCheck(LauraX, 500, "O") or ApprovalCheck(LauraX, 500, "I"):
                            $ LauraX.Name = "Росомаха"
                            $ LauraX.Name_rod = "Росомахи"
                            $ LauraX.Name_dat = "Росомахе"
                            $ LauraX.Name_vin = "Росомаху"
                            $ LauraX.Name_tvo = "Росомахой"
                            $ LauraX.Name_pre = "Росомахе"
                            $ LauraX.FaceChange("confused", 1)
                            if "namechange" not in LauraX.DailyActions:
                                    $ LauraX.Statup("Obed", 70, 2)
                                    $ LauraX.Statup("Inbt", 50, 2)
                            ch_l "Думаю, можно попробовать. . ."
                    else:
                            $ LauraX.Blush = 2
                            ch_l "Я. . . если честно, я не думаю, что оно распространяется и на меня. . ."
                    $ LauraX.FaceChange()
            "Неважно.":
                    pass
        $ LauraX.AddWord(1,0,"namechange")
        return
# end Laura_Rename//////////////////////////////////////////////////////////


# start Laura_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Personality(Cnt = 0):
    if not LauraX.Chat[4] or Cnt:
        "Поскольку у вас все хорошо получается в одной области, вы можете убедить Лору сосредоточиться на любой другой."
        "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
        "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
    menu:
        ch_l "Да? Что такое?"
        "Больше Послушания. [[Любовь в Послушание]" if LauraX.Love > 900:
            ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
            ch_l "Конечно, если тебя это так волнует."
            $ LauraX.Chat[4] = 1
        "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if LauraX.Love > 900:
            ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
            ch_l "Я всегда могу быть немного более дикой, если ты этого хочешь."
            $ LauraX.Chat[4] = 2

        "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if LauraX.Obed > 900:
            ch_p "Я хочу, чтобы ты была более раскрепощенной."
            ch_l "Думаю, я могу пойти на все."
            $ LauraX.Chat[4] = 3
        "Больше Любви. [[Повиновение в Любовь]" if LauraX.Obed > 900:
            ch_p "Я хочу, чтобы ты училась любить меня."
            ch_l "Я могу попробовать."
            $ LauraX.Chat[4] = 4

        "Больше Повиновения. [[Раскрепощенность в Повиновение]" if LauraX.Inbt > 900:
            ch_p "Я знаю, что нам и так весело, но разве ты не можешь иногда слушаться меня?"
            ch_l "Я могу попробовать. . ."
            $ LauraX.Chat[4] = 5

        "Больше Любви. [[Раскрепощенность в Любовь]" if LauraX.Inbt > 900:
            ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
            ch_l "Если тебе это нужно. . ."
            $ LauraX.Chat[4] = 6

        "Просто делай то, что тебе нравится. . .[[Сбросить]" if LauraX.Chat[4]:
            ch_p "Помнишь, что мы обсуждали? Забудь."
            ch_l "Эм, ладно."
            $ LauraX.Chat[4] = 0
        "Повторить правила":
            call Laura_Personality(1)
            return
        "Неважно.":
            return
    return
# end Laura_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Laura_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_Summon(Tempmod=Tempmod):
    $ LauraX.OutfitChange()
    if "no summon" in LauraX.RecentActions:
                if "angry" in LauraX.RecentActions:
                    ch_l "Грррррррр."
                elif LauraX.RecentActions.count("no summon") > 1:
                    ch_l "Отвали!"
                    $ LauraX.RecentActions.append("angry")
#                elif Current_Time == "Night":
#                    ch_l "Like I said, it's too late for that."
                else:
                    ch_l "Как я уже сказала, я занята."
                $ LauraX.RecentActions.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if LauraX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif LauraX.Loc == "bg dangerroom":
        $ Tempmod = -10
    elif LauraX.Loc == "bg showerroom":
        $ Tempmod = -30

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"
    if Time_Count >= 3: #night time
                if ApprovalCheck(LauraX, 500, "L") or ApprovalCheck(LauraX, 400, "O"):
                        #It's night time but she likes you.
                        ch_l "Ты тоже не спишь? Конечно, мы можем пообщаться."
                        $ LauraX.Loc = bg_current
                        call Taboo_Level
                        call Set_The_Scene
                else:
                        #It's night time and she isn't into you
                        ch_l "Не-а."
                        $ LauraX.RecentActions.append("no summon")
                return
    elif "les" in LauraX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(LauraX, 2000):
                    ch_l "Я сейчас вроде как с девушкой. Хочешь заглянуть?"
                    menu:
                        extend ""
                        "Конечно.":
                            $ Line = "go to"
                        "Нет, спасибо.":
                            ch_l "Хах, как хочешь."
                            return
            else:
                    ch_l "О. . . Эм. . . Я тут немного занята."
                    ch_l "Увидимся позже, ладно?"
                    $ LauraX.RecentActions.append("no summon")
                    return
    elif not ApprovalCheck(LauraX, 700, "L") or not ApprovalCheck(LauraX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(LauraX, 300):
                ch_l "Я занята, [LauraX.Petname]."
                $ LauraX.RecentActions.append("no summon")
                return


        if "summoned" in LauraX.RecentActions:
                pass
        elif "goto" in LauraX.RecentActions:
                if not Player.Male:
                    ch_l "Ты только что была здесь."
                else:
                    ch_l "Ты только что был здесь."
        elif LauraX.Loc == "bg classroom":
                ch_l "Я на занятиях, ты тоже хочешь прийти?"
        elif LauraX.Loc == "bg dangerroom":
                ch_l "Я в Комнате Опасности, [LauraX.Petname], хочешь прийти?"
        elif LauraX.Loc == "bg campus":
                ch_l "Я отдыхаю под деревом на площади, хочешь прийти?"
        elif LauraX.Loc == "bg laura":
                ch_l "Я в своей комнате, [LauraX.Petname], хочешь составить компанию?"
        elif LauraX.Loc == "bg player":
                ch_l "Я в твоей комнате, [LauraX.Petname], почему тебя здесь нет?"
        elif LauraX.Loc == "bg showerroom":
            if ApprovalCheck(LauraX, 1600):
                ch_l "Я сейчас в душе. Присоединишься?"
            else:
                ch_l "Я сейчас в душе, [LauraX.Petname]. Встретимся позже."
                $ LauraX.RecentActions.append("no summon")
                return
        elif LauraX.Loc == "hold":
                ch_l "Я сейчас на задании. Извини?"
                $ LauraX.RecentActions.append("no summon")
                return
        else:
                ch_l "Почему бы тебе не прийти ко мне?"


        if "summoned" in LauraX.RecentActions:
            ch_l "Снова? Ну хорошо."
            $ Line = "yes"
        elif "goto" in LauraX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
#                                ch_l "See you when you get here."
                                $ Line = "go to"
                "Нет.":
                                ch_l "Как хочешь."
                "Мне бы {i}очень{/i} хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(LauraX, 600, "L") or ApprovalCheck(LauraX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(LauraX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(LauraX, 1400):
                                #she is generally favorable
                                ch_l "Пфф."
                                $ Line = "yes"
                        elif ApprovalCheck(LauraX, 200, "O"):
                                #she is not obedient
                                ch_l "Мне все равно."
                                ch_l "Я буду здесь, если ты передумаешь."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(LauraX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(LauraX, 1400):
                                #she is generally favorable
                                ch_l "Пфф."
                                $ Line = "yes"
                        elif ApprovalCheck(LauraX, 200, "O"):
                                #she is not obedient
                                ch_l "Мне все равно."
                                ch_l "Я буду здесь, если ты передумаешь."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Конечно, сейчас приду.":
                    $ LauraX.Statup("Love", 55, 1)
                    $ LauraX.Statup("Inbt", 30, 1)
#                    ch_l "See you when you get here."
                    $ Line = "go to"

                "Нет, поговорим позже.":
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Obed", 30, 2)
                    ch_l "Хорошо. Тогда увидимся позже."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                    if ApprovalCheck(LauraX, 650, "L") or ApprovalCheck(LauraX, 1500):
                        $ LauraX.Statup("Love", 70, 1)
                        $ LauraX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ LauraX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                        if not Player.Male:
                            ch_l "Блин, ты такая дурочка."
                        else:
                            ch_l "Блин, ты такой дурачок."

                "Давай, будет весело.":
                    if ApprovalCheck(LauraX, 400, "L") and ApprovalCheck(LauraX, 800):
                        $ LauraX.Statup("Love", 70, 1)
                        $ LauraX.Statup("Obed", 50, 1)
                        $ Line = "fun"
                    else:
                        $ LauraX.Statup("Inbt", 30, 1)
                        $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                    if ApprovalCheck(LauraX, 600, "O"):
                        #she is obedient
                        $ LauraX.Statup("Love", 50, 1, 1)
                        $ LauraX.Statup("Love", 40, -1)
                        $ LauraX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(LauraX, 1500):
                        #she is generally favorable
                        $ LauraX.Statup("Love", 70, -2)
                        $ LauraX.Statup("Love", 90, -1)
                        $ LauraX.Statup("Obed", 50, 2)
                        $ LauraX.Statup("Obed", 90, 1)
                        ch_l "Ладно, хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(LauraX, 200, "O"):
                        #she is not obedient
                        $ LauraX.Statup("Love", 60, -4)
                        $ LauraX.Statup("Love", 90, -3)
                        ch_l "Даже не пытайся."
                        $ LauraX.Statup("Inbt", 40, 2)
                        $ LauraX.Statup("Inbt", 60, 1)
                        $ LauraX.Statup("Obed", 70, -3)
                        ch_l "Я останусь здесь."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ LauraX.Statup("Inbt", 30, 1)
                        $ LauraX.Statup("Inbt", 50, 1)
                        $ LauraX.Statup("Love", 50, -1, 1)
                        $ LauraX.Statup("Obed", 70, -1)
                        $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                    if ApprovalCheck(LauraX, 600, "O"):
                        #she is obedient
                        $ LauraX.Statup("Love", 50, 1, 1)
                        $ LauraX.Statup("Love", 40, -1)
                        $ LauraX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(LauraX, 1500):
                        #she is generally favorable
                        $ LauraX.Statup("Love", 70, -2)
                        $ LauraX.Statup("Love", 90, -1)
                        $ LauraX.Statup("Obed", 50, 2)
                        $ LauraX.Statup("Obed", 90, 1)
                        ch_l "Ладно, хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(LauraX, 200, "O"):
                        #she is not obedient
                        $ LauraX.Statup("Love", 60, -4)
                        $ LauraX.Statup("Love", 90, -3)
                        ch_l "Даже не пытайся."
                        $ LauraX.Statup("Inbt", 40, 2)
                        $ LauraX.Statup("Inbt", 60, 1)
                        $ LauraX.Statup("Obed", 70, -3)
                        ch_l "Я останусь здесь."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ LauraX.Statup("Inbt", 30, 1)
                        $ LauraX.Statup("Inbt", 50, 1)
                        $ LauraX.Statup("Love", 50, -1, 1)
                        $ LauraX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if LauraX.Love > LauraX.Obed:
            ch_l "Конечно!"
        else:
            ch_l "Ладно, сейчас буду."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ LauraX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            if LauraX.Loc == "bg classroom":
                ch_l "Я не могу пропустить эту лекцию."
            elif LauraX.Loc == "bg dangerroom":
                ch_l "Я только разогрелась!"
            else:
                ch_l "Извини, [LauraX.Petname], я немного занята."
            $ LauraX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ LauraX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            $ Line = 0
            $ Nearby = []
            $ Party = [LauraX]
            if LauraX.Loc == "bg classroom":
                    ch_l "Ладно, рядом со мной есть место."
                    jump Class_Room
            elif LauraX.Loc == "bg dangerroom":
                    ch_l "Я постараюсь оставить для тебя несколько ботов."
                    jump Danger_Room
            elif LauraX.Loc == "bg laura":
                    ch_l "Я пока. . . освобожу немного места."
                    jump Laura_Room
            elif LauraX.Loc == "bg player":
                    ch_l "Я буду ждать."
                    jump Player_Room
            elif LauraX.Loc == "bg showerroom":
                    ch_l "Я оставлю тебе немного горячей воды."
                    jump Shower_Room
            elif LauraX.Loc == "bg campus":
                    ch_l "Ищи самое большое дерево."
                    jump Campus
            elif LauraX.Loc != "hold":
                    ch_l "Ага, увидимся."
                    $ bg_current = LauraX.Loc
                    jump Misplaced
            else:
                    ch_l "Эм, я просто встречусь с тобой в своей комнате."
                    $ LauraX.Loc = "bg laura"
                    jump Laura_Room

    #She's agreed to come over
    elif Line == "lonely":
            if not Player.Male:
                ch_l "Ты такая дурочка."
            else:
                ch_l "Ты такой дурачок."
    elif Line == "command":
            ch_l "Да, [LauraX.Petname]."
    elif Line == "fun":
            ch_l "Конечно."

    $ LauraX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(LauraX)
            return
    $ LauraX.Loc = bg_current
    call Taboo_Level(0)
    $ LauraX.OutfitChange()
    call Set_The_Scene
    return

# End Laura Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Laura_Leave(Tempmod=Tempmod, GirlsNum = 0):
    if "leaving" in LauraX.RecentActions:
        $ LauraX.DrainWord("leaving")
    else:
        return

    if LauraX.Loc == "hold":
            # Activates if she's being moved out of play
            ch_l "Я отлучусь ненадолго, увидимся позже."
            return

    if LauraX in Party or "lockedtravels" in LauraX.Traits:
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ LauraX.Loc = bg_current
            return

    elif "freetravels" in LauraX.Traits or not ApprovalCheck(LauraX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.
            $ LauraX.OutfitChange()
            if GirlsNum: #if someone left before her
                        ch_l "Ага, я тоже ухожу."

            if LauraX.Loc == "bg classroom":
                        ch_l "У меня занятия."
            elif LauraX.Loc == "bg dangerroom":
                        ch_l "Я иду в Комнату Опасности."
            elif LauraX.Loc == "bg campus":
                        ch_l "Я вздремну на площади."
            elif LauraX.Loc == "bg laura":
                        ch_l "Я возвращаюсь в свою комнату."
            elif LauraX.Loc == "bg player":
                        ch_l "Я собираюсь немного побыть в твоей комнате."
            elif LauraX.Loc == "bg pool":
                        ch_l "Я иду в бассейн."
            elif LauraX.Loc == "bg showerroom":
                if ApprovalCheck(LauraX, 1400):
                        ch_l "Я иду в душ, увидимся."
                else:
                        ch_l "Я ухожу."
            else:
                        ch_l "Я ухожу, увидимся."
            hide Laura_Sprite
            hide Laura_Seated
            return
            #End Free Travels

    if bg_current == "bg dangerroom":
            call Gym_Exit([LauraX])

    $ LauraX.OutfitChange()

    if "follow" not in LauraX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ LauraX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    # Sets her preferences
    if LauraX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif LauraX.Loc == "bg dangerroom":
        $ Tempmod = 20
    elif LauraX.Loc == "bg showerroom":
        $ Tempmod = 40


    if GirlsNum: #if someone left before her
                ch_l "Ага, я тоже ухожу."

    if LauraX.Loc == "bg classroom":
        ch_l "У меня занятия, хочешь со мной?"
    elif LauraX.Loc == "bg dangerroom":
        ch_l "У меня тренировка в Комнате Опасности, хочешь со мной?"
    elif LauraX.Loc == "bg campus":
        ch_l "Я пойду вздремну на площади, хочешь со мной?"
    elif LauraX.Loc == "bg laura":
        ch_l "Я возвращаюсь в свою комнату, хочешь со мной?"
    elif LauraX.Loc == "bg player":
        ch_l "Я собираюсь немного побыть в твоей комнате, хочешь со мной?"
    elif LauraX.Loc == "bg mall":
        ch_l "Я собираюсь немного погулять в торговом центре, ты придешь ко мне?"
    elif LauraX.Loc == "bg showerroom":
        if ApprovalCheck(LauraX, 1600):
            ch_l "Я в душ, тебе тоже не помешает."
        else:
            ch_l "Я в душ, увидимся позже."
            return
    elif LauraX.Loc == "bg pool":
            ch_l "Я иду в бассейн. Хочешь со мной?"
    else:
            ch_l "Хочешь присоединиться ко мне?"


    menu:
        extend ""
        "Конечно, я сразу за тобой.":
                if "followed" not in LauraX.RecentActions:
                    $ LauraX.Statup("Love", 55, 1)
                    $ LauraX.Statup("Inbt", 30, 1)
                $ Line = "go to"

        "Нет, поговорим позже.":
                if "followed" not in LauraX.RecentActions:
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Obed", 30, 2)
                ch_l "Конечно, как скажешь."

        "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                if ApprovalCheck(LauraX, 650, "L") or ApprovalCheck(LauraX, 1500):
                    if "followed" not in LauraX.RecentActions:
                        $ LauraX.Statup("Love", 70, 1)
                        $ LauraX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else:
                    if "followed" not in LauraX.RecentActions:
                        $ LauraX.Statup("Inbt", 30, 1)
                    $ Line = "no"
                    if not Player.Male:
                        ch_l "Блин, ты такая дурочка."
                    else:
                        ch_l "Блин, ты такой дурачок."

        "Давай, будет весело.":
                if ApprovalCheck(LauraX, 400, "L") and ApprovalCheck(LauraX, 800):
                    $ LauraX.Statup("Love", 70, 1)
                    $ LauraX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else:
                    $ LauraX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Нет, останься здесь.":
                if ApprovalCheck(LauraX, 600, "O"):
                    #she is obedient
                    if "followed" not in LauraX.RecentActions:
                        $ LauraX.Statup("Love", 40, -2)
                        $ LauraX.Statup("Obed", 90, 1)
                    $ Line = "command"

                elif D20 >= 7 and ApprovalCheck(LauraX, 1400):
                    #she is generally favorable
                    if "followed" not in LauraX.RecentActions:
                        $ LauraX.Statup("Love", 70, -2)
                        $ LauraX.Statup("Love", 90, -1)
                        $ LauraX.Statup("Obed", 50, 2)
                        $ LauraX.Statup("Obed", 90, 1)
                    ch_l "Ну, если я тебе нужна."
                    $ Line = "yes"

                elif ApprovalCheck(LauraX, 200, "O"):
                    #she is not obedient
                    if "followed" not in LauraX.RecentActions:
                        $ LauraX.Statup("Love", 70, -4)
                        $ LauraX.Statup("Love", 90, -2)
                    ch_l "Не указывай мне, что делать."
                    if "followed" not in LauraX.RecentActions:
                        $ LauraX.Statup("Inbt", 40, 2)
                        $ LauraX.Statup("Inbt", 60, 1)
                        $ LauraX.Statup("Obed", 70, -2)
                    ch_l "Я пошла."
                else:
                    #she is obedient, but you failed to meet the checks
                    if "followed" not in LauraX.RecentActions:
                        $ LauraX.Statup("Inbt", 30, 1)
                        $ LauraX.Statup("Inbt", 50, 1)
                        $ LauraX.Statup("Love", 50, -1, 1)
                        $ LauraX.Statup("Love", 90, -2)
                        $ LauraX.Statup("Obed", 70, -1)
                    $ Line = "no"
                #End ordered to stay

    call Taboo_Level(0)
    $ LauraX.RecentActions.append("followed")
    if not Line:
            #You end the dialog neutrally
            hide Laura_Sprite
            hide Laura_Seated
            call Gym_Clothes_Off([LauraX])
            return

    if Line == "no":
            # She's refused, context based dialog
            if LauraX.Loc == "bg classroom":
                ch_l "Я никак не могу это пропустить."
            elif LauraX.Loc == "bg dangerroom":
                ch_l "Извини, [LauraX.Petname], но мне нужно выпустить пар."
            else:
                ch_l "Извини, у меня дела."
            hide Laura_Sprite
            hide Laura_Seated
            call Gym_Clothes_Off([LauraX])
            return

    elif Line == "go to":
            #You agreed to go to her instead
            #$ Party.append(LauraX)
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")
            $ LauraX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            hide Laura_Sprite
            hide Laura_Seated
            $ Nearby = []
            $ Party = [LauraX]
            call Gym_Clothes_Off([LauraX])
            if LauraX.Loc == "bg classroom":
                ch_l "Ладно, тогда пошевеливайся."
                jump Class_Room_Entry
            elif LauraX.Loc == "bg dangerroom":
                ch_l "Я пока разогреюсь."
                jump Danger_Room_Entry
            elif LauraX.Loc == "bg laura":
                ch_l "Ладно."
                jump Laura_Room
            elif LauraX.Loc == "bg player":
                ch_l "Хорошо."
                jump Player_Room
            elif LauraX.Loc == "bg showerroom":
                ch_l "Ладно, хорошо."
                jump Shower_Room_Entry
            elif LauraX.Loc == "bg campus":
                ch_l "Ладно, хорошо."
                jump Campus_Entry
            elif LauraX.Loc == "bg pool":
                ch_l "Клево."
                jump Pool_Entry
            elif LauraX.Loc == "bg mall":
                ch_l "Клево."
                jump Mall_Entry
            else:
                ch_l "Я просто встречусь с тобой в твоей комнате."
                $ LauraX.Loc = "bg player"
                jump Player_Room
            #End "goto" where she's at

    #She's agreed to come over
    elif Line == "lonely":
            ch_l "Ну, наверное, тебе не стоит оставаться в одиночестве. . ."
    elif Line == "command":
            ch_l "Да, [LauraX.Petname]."
    elif Line:
            ch_l "Конечно."

    $ Line = 0
    ch_l "Я останусь здесь."
    $ LauraX.Loc = bg_current
    call Taboo_Level(0)
    return

# End Laura Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

### Laura's Clothes  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_Clothes:
    if LauraX.Taboo:
            if "exhibitionist" in LauraX.Traits:
                ch_l "Да? . ."
            elif ApprovalCheck(LauraX, 900, TabM=4) or ApprovalCheck(LauraX, 400, "I", TabM=3):
                ch_l "Не думаю, что мне стоит раздеваться здесь. . ."
            else:
                ch_l "Не думаю, что мне стоит раздеваться здесь. . ."
                ch_l "Мы можем поговорить в одной из наших комнатах?"
                return
    elif ApprovalCheck(LauraX, 900, TabM=4) or ApprovalCheck(LauraX, 600, "L") or ApprovalCheck(LauraX, 300, "O"):
                ch_l "А? Что не так с моей одеждой?"
    else:
                ch_l "Я особо не беспокоюсь о своей одежде."
                if not Player.Male:
                    ch_l "Ты тем более не должна."
                else:
                    ch_l "Ты тем более не должен."
                return

    if Girl != LauraX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = LauraX
    call Shift_Focus(Girl)

label Laura_Wardrobe_Menu:
    $ LauraX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .
    while True:
        menu:
            ch_l "Что насчет моей одежды?"
            "Верх":
                        call Laura_Clothes_Over
            "Низ":
                        call Laura_Clothes_Legs
            "Нижнее белье":
                        call Laura_Clothes_Under
            "Аксессуары":
                        call Laura_Clothes_Misc
            "Управление нарядами":
                        call Laura_Clothes_Outfits
            "Давай поговорим о том, что ты носишь.":
                        call Clothes_Schedule(LauraX)

            "Могу я посмотреть?" if LauraX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(LauraX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_l "Ладно, так хорошо?"
                    hide PhoneSex
            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(LauraX,0,2)
                    if _return:
                        hide DressScreen
            "Может, тебе будет комфортнее за ширмой? (locked)" if LauraX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if LauraX.Loc == bg_current and not LauraX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if not Player.Male and "girltalk" not in LauraX.History and "nogirls" not in LauraX.History:
                            ch_l "Что? Зачем?"
                    elif ApprovalCheck(LauraX, 1500) or (LauraX.SeenChest and LauraX.SeenPussy):
                            ch_l "Скорее всего она не понадобится, но спасибо."
                    else:
                            show DressScreen zorder 150
                            ch_l "Ага, так лучше, спасибо."

            "У меня есть подарок для тебя (locked)" if LauraX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if LauraX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(LauraX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ LauraX.OutfitChange()
                    $ LauraX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != LauraX:
                            ch_p "Я хочу поговорить о твоей одежде."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = LauraX
                    call Shift_Focus(Girl)

            "Сменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current:
                    pass
            "Сменить вид" if Girl.Loc == bg_current:
                    call WardrobeView(LauraX)

            "Неважно, ты и так хорошо выглядишь":
                    call Girl_Pos_Reset(LauraX)
                    if "wardrobe" not in LauraX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if LauraX.Chat[1] <= 1:
                                    $ LauraX.Statup("Love", 70, 15)
                                    $ LauraX.Statup("Obed", 40, 20)
                                    ch_l "О! Спасибо."
                            elif LauraX.Chat[1] <= 10:
                                    $ LauraX.Statup("Love", 70, 5)
                                    $ LauraX.Statup("Obed", 40, 7)
                                    ch_l "Правда?"
                            elif LauraX.Chat[1] <= 50:
                                    $ LauraX.Statup("Love", 70, 1)
                                    $ LauraX.Statup("Obed", 40, 1)
                                    ch_l "Угу."
                            else:
                                    ch_l "Конечно."
                            $ LauraX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(LauraX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ LauraX.OutfitChange()
                    $ LauraX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ LauraX.Chat[1] += 1
                    $ Trigger = 0
                    if LauraX.Panties and "pantyless" in LauraX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ LauraX.DailyActions.remove("pantyless")
                    return

        #Loops back up
        #return #jump Laura_Clothes
        #End of Laura Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Laura_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(LauraX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(LauraX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(LauraX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(LauraX,4,1)
                    "Одежда для сна":
                                call OutfitShame(LauraX,7,1)
                    "Купальник":
                                call OutfitShame(LauraX,10,1)

                    "Повседневка 1" if ApprovalCheck(LauraX, 2500):
                                call OutfitShame(LauraX,11,1)
                    "Повседневка 2" if ApprovalCheck(LauraX, 2500):
                                call OutfitShame(LauraX,12,1)
                    #8 is Emma's teaching clothes,
                    "Неважно":
                                pass

        "Примерь кожаный боевой костюм":
                $ LauraX.OutfitChange("casual1")
                menu:
                    "Ты должна носить его. [[Выбрать текущий наряд]":
                            $ LauraX.Outfit = "casual1"
                            $ LauraX.Shame = 0
                            ch_l "Ага, мне нравится надевать его на задания."
                    "Давай попробуем что-нибудь другое.":
                            ch_l "Ладно."

        "Примерь кожаный пиджак и юбку":
                $ LauraX.OutfitChange("casual2")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                            $ LauraX.Outfit = "casual2"
                            $ LauraX.Shame = 0
                            ch_l "Хорошо, мой двоюродный брат купил эти вещи для меня."
                    "Давай попробуем что-нибудь другое.":
                            ch_l "Ладно."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not LauraX.Custom1[0] and not LauraX.Custom2[0] and not LauraX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if LauraX.Custom1[0] or LauraX.Custom2[0] or LauraX.Custom3[0]:
                $ Cnt = 0
                while 1:
                    menu:
                        "Надень Пользовательский 1 (locked)" if not LauraX.Custom1[0]:
                                pass
                        "Надень Пользовательский 1" if LauraX.Custom1[0]:
                                $ LauraX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Надень Пользовательский 2 (locked)" if not LauraX.Custom2[0]:
                                pass
                        "Надень Пользовательский 2" if LauraX.Custom2[0]:
                                $ LauraX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Надень Пользовательский 3 (locked)" if not LauraX.Custom3[0]:
                                pass
                        "Надень Пользовательский 3" if LauraX.Custom3[0]:
                                $ LauraX.OutfitChange("custom3")
                                $ Cnt = 6

                        "Ты должна одеваться так, когда мы наедине (locked)" if not Cnt:
                                pass
                        "Ты должна одеваться так, когда мы наедине" if Cnt:
                                if Cnt == 5:
                                    $ LauraX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ LauraX.Clothing[9] = "custom3"
                                else:
                                    $ LauraX.Clothing[9] = "custom1"
                                ch_l "Конечно."

                        "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                menu:
                                    "Пользовательский 1 [[очистить слот 1]" if LauraX.Custom1[0]:
                                        ch_l "Ладно."
                                        $ LauraX.Custom1[0] = 0
                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not LauraX.Custom1[0]:
                                        pass
                                    "Пользовательский 2 [[очистить слот 2]" if LauraX.Custom2[0]:
                                        ch_l "Ладно."
                                        $ LauraX.Custom2[0] = 0
                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not LauraX.Custom2[0]:
                                        pass
                                    "Пользовательский 3 [[очистить слот 3]" if LauraX.Custom3[0]:
                                        ch_l "Ладно."
                                        $ LauraX.Custom3[0] = 0
                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not LauraX.Custom3[0]:
                                        pass
                                    "Неважно [[назад]":
                                        pass

                        "Тебе следует надеть его. [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                pass
                        "Тебе следует надеть его" if Cnt:
                                call Custom_Out(LauraX,Cnt)
                        "Ладно, вернемся к началу нашего разговора. . .":
                                $ Cnt = 0
                                return #jump Laura_Clothes

        "Наденешь спортивную одежду?" if not LauraX.Taboo or bg_current == "bg dangerroom":
                $ LauraX.OutfitChange("gym")

        "Наденешь одежду для сна?" if not LauraX.Taboo:
                if ApprovalCheck(LauraX, 1200):
                        $ LauraX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(LauraX)
                        if _return:
                            $ LauraX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (LauraX.Taboo and bg_current != "bg pool" and not ApprovalCheck(LauraX, 800, TabM=2)) or not LauraX.Swim[0]:
                $ LauraX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not LauraX.Taboo or bg_current == "bg pool" or ApprovalCheck(LauraX, 800, TabM=2)) and LauraX.Swim[0]:
                $ LauraX.OutfitChange("swimwear")

        "Наденешь хэллоуинский костюм?" if "halloween" in LauraX.History:
                ch_l "Ладно."
                $ LauraX.OutfitChange("costume")

        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ LauraX.FaceChange("sexy", 1)
                $ Line = 0
                if not LauraX.Chest and not LauraX.Panties and not LauraX.Over and not LauraX.Legs and not LauraX.Hose:
                    if not Player.Male:
                        ch_l "Ага. . . подожди, с чего ты взяла?"
                    else:
                        ch_l "Ага. . . подожди, с чего ты взял?"
                elif LauraX.SeenChest and LauraX.SeenPussy and ApprovalCheck(LauraX, 1200, TabM=4):
                    ch_l "Тебе виднее. . ."
                    $ Line = 1
                elif ApprovalCheck(LauraX, 2000, TabM=4):
                    ch_l "Перейдем сразу к раздеванию?"
                    $ Line = 1
                elif LauraX.SeenChest and LauraX.SeenPussy and ApprovalCheck(LauraX, 1200, TabM=0):
                    ch_l "Возможно, но не здесь . ."
                elif ApprovalCheck(LauraX, 2000, TabM=0):
                    ch_l "Возможно, но не здесь . ."
                elif ApprovalCheck(LauraX, 1000, TabM=0):
                    $ LauraX.FaceChange("confused", 1,Mouth="smirk")
                    ch_l "Ага, но я не хвастаюсь."
                    $ LauraX.FaceChange("bemused", 0)
                else:
                    $ LauraX.FaceChange("angry", 1)
                    ch_l "А тебе какое дело?"

                call expression LauraX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in LauraX.History:
                        $ Line = 0
                if Line:
                    #If she got nude. . .
                    $ LauraX.OutfitChange("nude")
                    "Она сбрасывает одежду к своим ногам."
                    call Girl_First_Topless(LauraX)
                    call Girl_First_Bottomless(LauraX,1)
                    $ LauraX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется. что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in LauraX.Traits:
                                ch_l "Ммммм. . ."
                                $ LauraX.Outfit = "nude"
                                $ LauraX.Statup("Lust", 50, 10)
                                $ LauraX.Statup("Lust", 70, 5)
                                $ LauraX.Shame = 50
                            elif ApprovalCheck(LauraX, 800, "I") or ApprovalCheck(LauraX, 2800, TabM=0):
                                ch_l "Я возбуждаюсь. . ."
                                $ LauraX.Outfit = "nude"
                                $ LauraX.Shame = 50
                            else:
                                $ LauraX.FaceChange("sexy", 1)
                                $ LauraX.Eyes = "surprised"
                                ch_l "Мне кажется, не стоит. Извини."

                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in LauraX.Traits:
                                if not Player.Male:
                                    ch_l "Ты уверена?"
                                else:
                                    ch_l "Ты уверен?"
                            elif ApprovalCheck(LauraX, 800, "I") or ApprovalCheck(LauraX, 2800, TabM=0):
                                $ LauraX.FaceChange("bemused", 1)
                                ch_l "Я боялась, ты захочешь, чтобы я ходила голой."
                                ch_l ". . ."
                            else:
                                $ LauraX.FaceChange("confused", 1)
                                if not Player.Male:
                                    ch_l "Я не против, чтобы ты смотрела на мое обнаженное тело, но. . ."
                                else:
                                    ch_l "Я не против, чтобы ты смотрел на мое обнаженное тело, но. . ."
                $ Line = 0

        "Неважно":
            return #jump Laura_Clothes

    return #jump Laura_Clothes
    #End of Laura Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Laura_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять [get_clothing_name(LauraX.Over_key, vin)]?" if LauraX.Over:
                call Wardrobe_Remove(LauraX)

        "Примерь кожаную куртку." if LauraX.Over != "jacket":
                $ LauraX.FaceChange("bemused")
                if not LauraX.Over or LauraX.Chest == "leather bra":
                    #if she's not already wearing a top, or has the leather bra on
                    ch_l "Конечно."
                elif ApprovalCheck(LauraX, 800, TabM=0):
                    ch_l "Ага, ладно."
                else:
                    call Display_DressScreen(LauraX)
                    if not _return:
                            $ LauraX.FaceChange("bemused", 1)
                            ch_l "Я сейчас совсем не хочу переодевать [get_clothing_name(LauraX.Over_key, vin)]."
                            return #jump Laura_Clothes
                $ LauraX.Over = "jacket"

        "Может, просто накинешь полотенце?" if LauraX.Over != "towel":
                $ LauraX.FaceChange("bemused", 1)
                if LauraX.Chest or LauraX.SeenChest:
                    ch_l "Странный выбор."
                elif ApprovalCheck(LauraX, 1000, TabM=0):
                    $ LauraX.FaceChange("perplexed", 1)
                    ch_l "Эм, ладно. . ."
                else:
                    call Display_DressScreen(LauraX)
                    if not _return:
                            ch_l "Думаю, мне не стоит это делать."
                            return #jump Laura_Clothes
                $ LauraX.Over = "towel"

        "Неважно":
            pass
    return #jump Laura_Clothes
    #End of Laura Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Laura_NoBra:
        menu:
            ch_l "У меня под [get_clothing_name(LauraX.Over_key, vin)] совсем ничего нет. . ."
            "Тогда надень что-нибудь. . .":
                        if LauraX.SeenChest and ApprovalCheck(LauraX, 1000, TabM=3):
                                $ LauraX.Blush = 1
                                ch_l "-Я не говорила, что меня это беспокоит. . ."
                                $ LauraX.Blush = 0
                        elif ApprovalCheck(LauraX, 1200, TabM=4):
                                $ LauraX.Blush = 1
                                ch_l "-Я не говорила, что меня это беспокоит. . ."
                                $ LauraX.Blush = 0
                        elif ApprovalCheck(LauraX, 900, TabM=2) and "lace corset" in LauraX.Inventory:
                                ch_l "Наверное, я смогу что-нибудь подобрать."
                                $ LauraX.Chest  = "lace corset"
                                "Она достает свой кружевной корсет и надевает его под [get_clothing_name(LauraX.Over_key, vin)]."
                        elif ApprovalCheck(LauraX, 700, TabM=2) and "corset" in LauraX.Inventory:
                                ch_l "Наверное, я смогу что-нибудь подобрать."
                                $ LauraX.Chest  = "corset"
                                "Она достает свой корсет и надевает его под [get_clothing_name(LauraX.Over_key, vin)]."
                        elif ApprovalCheck(LauraX, 600, TabM=2):
                                if not Player.Male:
                                    ch_l "Ага, наверное, ты права."
                                else:
                                    ch_l "Ага, наверное, ты прав."
                                $ LauraX.Chest = "leather bra"
                                "Она достает свой кожаный лифчик и надевает его под [get_clothing_name(LauraX.Over_key, vin)]."
                        else:
                                ch_l "Ага, но мне не хочется."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(LauraX, 1100, "LI", TabM=2) and LauraX.Love > LauraX.Inbt:
                                ch_l "Для тебя? Пожалуй. . ."
                        elif ApprovalCheck(LauraX, 700, "OI", TabM=2) and LauraX.Obed > LauraX.Inbt:
                                ch_l "Конечно. . ."
                        elif ApprovalCheck(LauraX, 600, "I", TabM=2):
                                ch_l "Ага. . ."
                        elif ApprovalCheck(LauraX, 1300, TabM=2):
                                ch_l "Согласна."
                        else:
                                $ LauraX.FaceChange("surprised")
                                $ LauraX.Brows = "angry"
                                if LauraX.Taboo > 20:
                                    ch_l "Но не на людях!"
                                else:
                                    if not Player.Male:
                                        ch_l "Ты не настолько милая, [LauraX.Petname]!"
                                    else:
                                        ch_l "Ты не настолько милый, [LauraX.Petname]!"
                                call expression LauraX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0
            "Неважно":
                        ch_l "Ладно. . ."
                        return 0
        return 1
        #End of Laura bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Laura_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(LauraX.Legs_key, vin)]?" if LauraX.Legs:
                call Wardrobe_Remove(LauraX,1)

        "Примерь кожанные штаны" if LauraX.Legs != "leather pants":
                ch_p "Тебе идут кожанные штаны."
                ch_l "Ага, ладно."
                $ LauraX.Legs = "leather pants"

        "Примерь ажурные брюки" if LauraX.Legs != "mesh pants" and "mesh pants" in LauraX.Inventory:
                ch_p "Ты отлично выглядишь в ажурных брюках."
                if ApprovalCheck(LauraX, 1000, TabM=4):
                        ch_l "Ага, ладно."
                        $ LauraX.Legs = "mesh pants"
                else:
                    call Display_DressScreen(LauraX)
                    if not _return:
                        ch_l "Извини, но в них. . . холодно."
                    else:
                        $ LauraX.Legs = "mesh pants"

        "Примерь кожаную юбку с ремнем" if LauraX.Legs != "skirt":
                ch_p "Как насчет того, чтобы надеть кожаную юбку? С ремнями?"
                ch_l "Конечно, почему бы и нет."
                $ LauraX.Legs = "skirt"

        "Примерь кожаную юбку" if LauraX.Legs != "other skirt" and "halloween" in LauraX.History:
                ch_p "Как насчет того, чтобы надеть свою кожаную юбку?"
                ch_l "Конечно, почему бы и нет."
                $ LauraX.Legs = "other skirt"

        "Сними обувь (locked)" if not LauraX.Boots:
                pass
        "Сними [get_clothing_name(LauraX.Boots_key, vin)]" if LauraX.Boots:
                ch_p "Может, снимешь [get_clothing_name(LauraX.Boots_key, vin)]?"
                ch_l "Конечно, почему бы и нет."
                $ LauraX.Boots = 0
        "Надень ботинки" if LauraX.Boots != "boots":
                ch_p "Может, наденешь ботинки?"
                ch_l "Конечно, почему бы и нет."
                $ LauraX.Boots = "boots"
#        "Add Sneakers" if LauraX.Boots != "sneaks":
#                ch_p "Maybe put your sneakers on."
#                ch_l "Sure, why not."
#                $ LauraX.Boots = "sneaks"

        "Неважно":
                pass
    return #jump Laura_Clothes
    #End of Laura Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Laura_NoPantiesOn:
        menu:
            ch_l "Я сегодня без трусиков."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if LauraX.SeenPussy and ApprovalCheck(LauraX, 1100, TabM=4):
                                $ LauraX.Blush = 1
                                ch_l "Нет, мне и без них хорошо. . ."
                                $ LauraX.Blush = 0
                        elif ApprovalCheck(LauraX, 1500, TabM=4):
                                $ LauraX.Blush = 1
                                ch_l "Нет, мне и без них хорошо. . ."
                                $ LauraX.Blush = 0
                        elif ApprovalCheck(LauraX, 700, TabM=4):
                                ch_l "Ага, наверное."
                                if "lace panties" in LauraX.Inventory:
                                        ch_l "Мне нравится ход твоих мыслей."
                                        $ LauraX.Panties  = "lace panties"
                                else:
                                        $ LauraX.Panties = "black panties"
                                if ApprovalCheck(LauraX, 1200, TabM=4):
                                    $ Line = get_clothing_name(LauraX.Legs_key, vin)
                                    $ LauraX.Legs = 0
                                    "Она снимает [Line] и надевает [get_clothing_name(LauraX.Panties_key, vin)]."
                                elif LauraX.Legs == "skirt":
                                    "Она достает [get_clothing_name(LauraX.Panties_key, vin)] и надевает их под юбку."
                                    $ LauraX.Legs = 0
                                    "Затем она сбрасывает юбку на пол."
                                else:
                                    $ Line = get_clothing_name(LauraX.Legs_key, vin)
                                    $ LauraX.Legs = 0
                                    "Она на мгновение отходит, а затем возвращается в [get_clothing_name(LauraX.Panties_key, pre)]."
                                return #jump Laura_Clothes
                        else:
                                ch_l "Не-а."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(LauraX, 1100, "LI", TabM=3) and LauraX.Love > LauraX.Inbt:
                                ch_l "Верно. . ."
                        elif ApprovalCheck(LauraX, 700, "OI", TabM=3) and LauraX.Obed > LauraX.Inbt:
                                ch_l "Да. . ."
                        elif ApprovalCheck(LauraX, 600, "I", TabM=3):
                                ch_l "Хммм. . ."
                        elif ApprovalCheck(LauraX, 1300, TabM=3):
                                ch_l "Согласна."
                        else:
                                $ LauraX.FaceChange("surprised")
                                $ LauraX.Brows = "angry"
                                if LauraX.Taboo > 20:
                                    ch_l "Да, но не на людях, [LauraX.Petname]!"
                                else:
                                    if not Player.Male:
                                        ch_l "Ты не настолько милая, [LauraX.Petname]!"
                                    else:
                                        ch_l "Ты не настолько милый, [LauraX.Petname]!"
                                call expression LauraX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно":
                ch_l "Ладно. . ."
                return 0
        return 1
        #End of Laura Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Laura_Clothes_Under:
        "Верх":
            menu:
                "Может, снимешь [get_clothing_name(LauraX.Chest_key, vin)]?" if LauraX.Chest:
                        $ LauraX.FaceChange("bemused", 1)
                        if LauraX.SeenChest and ApprovalCheck(LauraX, 900, TabM=2.7):
                            ch_l "Ладно."
                        elif ApprovalCheck(LauraX, 1100, TabM=2):
                            if LauraX.Taboo:
                                ch_l "Здесь как-то не хочется. . ."
                            else:
                                ch_l "Может быть. . ."
                        elif LauraX.Over == "jacket" and ApprovalCheck(LauraX, 600, TabM=2):
                            ch_l "Я буду выглядеть слишком непристойно. . ."
                        elif LauraX.Over and ApprovalCheck(LauraX, 500, TabM=2):
                            ch_l "Думаю, можно. . ."
                        elif not LauraX.Over:
                            call Display_DressScreen(LauraX)
                            if not _return:
                                ch_l "Я не могу."
                                return #jump Laura_Clothes
                        else:
                            call Display_DressScreen(LauraX)
                            if not _return:
                                ch_l "Не-а."
                                return #jump Laura_Clothes
                        $ Line = get_clothing_name(LauraX.Chest_key, vin)
                        $ LauraX.Chest = 0
                        if LauraX.Over:
                            "Она залезает под [get_clothing_name(LauraX.Over_key, vin)], хватает и снимает [Line], а затем бросает на пол."
                        else:
                            "Она снимает [Line] и кидает на пол."
                            if not renpy.showing('DressScreen'):
                                call Girl_First_Topless(LauraX)


                "Примерь кожаный лифчик" if LauraX.Chest != "leather bra":
                        ch_p "Примерь кожаный лифчик."
                        ch_l "Ладно."
                        $ LauraX.Chest = "leather bra"

                "Примерь белую майку" if LauraX.Chest != "white tank" and "halloween" in LauraX.History:
                        ch_p "Примерь белую майку."
                        ch_l "Ладно."
                        $ LauraX.Chest = "white tank"

                "Примерь красный корсет" if LauraX.Chest != "corset" and "corset" in LauraX.Inventory:
                        ch_p "Мне нравится твой красный корсет."
                        if LauraX.SeenChest or ApprovalCheck(LauraX, 1000, TabM=1):
                            ch_l "Ладно."
                            $ LauraX.Chest = "corset"
                        else:
                            call Display_DressScreen(LauraX)
                            if not _return:
                                ch_l "Он слегка откровенный. . ."
                            else:
                                $ LauraX.Chest = "corset"

                "Примерь кружевной корсет" if LauraX.Chest != "lace corset" and "lace corset" in LauraX.Inventory:
                        ch_p "Мне нравится твой кружевной корсет."
                        if LauraX.SeenChest or ApprovalCheck(LauraX, 1300, TabM=2):
                            ch_l "Ладно."
                            $ LauraX.Chest = "lace corset"
                        else:
                            call Display_DressScreen(LauraX)
                            if not _return:
                                ch_l "Он слишком прозрачный. . ."
                            else:
                                $ LauraX.Chest = "lace corset"

                "Примерь топ в расцветке Росомахи" if LauraX.Chest != "wolvie top" and "wolvie top" in LauraX.Inventory:
                        ch_p "Мне нравится твой топ в расцветке Росомахи."
                        if LauraX.SeenChest or ApprovalCheck(LauraX, 1000, TabM=2):
                            ch_l "Ладно."
                            $ LauraX.Chest = "wolvie top"
                        else:
                            call Display_DressScreen(LauraX)
                            if not _return:
                                ch_l "Мне {i}немного{/i} неловко надевать его. . ."
                            else:
                                $ LauraX.Chest = "wolvie top"

                "Примерь лифчик бикини" if LauraX.Chest != "bikini top" and "bikini top" in LauraX.Inventory:
                        ch_p "Мне нравится твой лифчик бикини."
                        if bg_current == "bg pool":
                                ch_l "Ладно."
                                $ LauraX.Chest = "bikini top"
                        else:
                                if LauraX.SeenChest or ApprovalCheck(LauraX, 1000, TabM=2):
                                    ch_l "Ладно."
                                    $ LauraX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(LauraX)
                                    if not _return:
                                            ch_l "Тут не место для \"бикини\". . ."
                                    else:
                                            $ LauraX.Chest = "bikini top"
                "Неважно":
                        pass
            return #jump Laura_Clothes_Under

        "Варианты колготок и чулок":
            menu:
                "Сними [get_clothing_name(LauraX.Hose_key, vin)]." if LauraX.Hose:
                                $ LauraX.Hose = 0
                "Чулки дополнили бы твой образ." if LauraX.Hose != "stockings":
                                $ LauraX.Hose = "stockings"
                "Черные чулки дополнили бы твой образ." if LauraX.Hose != "black stockings" and "halloween" in LauraX.History:
                                $ LauraX.Hose = "black stockings"
                "Колготки дополнили бы твой образ." if LauraX.Hose != "pantyhose" and "pantyhose" in LauraX.Inventory:
                                $ LauraX.Hose = "pantyhose"
                "Рваные колготки дополнили бы твой образ." if LauraX.Hose != "ripped pantyhose" and "ripped pantyhose" in LauraX.Inventory:
                                $ LauraX.Hose = "ripped pantyhose"
                "Чулки и пояс с подвязками дополнили бы твой образ." if LauraX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in LauraX.Inventory:
                                $ LauraX.Hose = "stockings and garterbelt"
                "Может, наденешь только пояс с подвязками?" if LauraX.Hose != "garterbelt" and "stockings and garterbelt" in LauraX.Inventory:
                                $ LauraX.Hose = "garterbelt"
                "Неважно":
                        pass
            return #jump Laura_Clothes_Under

        #Panties
        "Низ":
            menu:
                "Ты должна снять [get_clothing_name(LauraX.Panties_key, vin)]. . ." if LauraX.Panties:
                        $ LauraX.FaceChange("bemused", 1)
                        if ApprovalCheck(LauraX, 900) and (LauraX.Legs or (LauraX.SeenPussy and not LauraX.Taboo)):
                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                                if ApprovalCheck(LauraX, 850, "L"):
                                        ch_l "Верно. . ."
                                elif ApprovalCheck(LauraX, 500, "O"):
                                        ch_l "Согласна."
                                elif ApprovalCheck(LauraX, 350, "I"):
                                        ch_l "Хах."
                                else:
                                        ch_l "Конечно, наверное."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(LauraX, 1100, "LI", TabM=3) and LauraX.Love > LauraX.Inbt:
                                        ch_l "Слушай, дело не в тебе, но. . ."
                                elif ApprovalCheck(LauraX, 700, "OI", TabM=3) and LauraX.Obed > LauraX.Inbt:
                                        ch_l "Хорошо. . ."
                                elif ApprovalCheck(LauraX, 600, "I", TabM=3):
                                        ch_l "Хммм. . ."
                                elif ApprovalCheck(LauraX, 1300, TabM=3):
                                        ch_l "Ладно-ладно."
                                else:
                                        call Display_DressScreen(LauraX)
                                        if not _return:
                                            $ LauraX.FaceChange("surprised")
                                            $ LauraX.Brows = "angry"
                                            if LauraX.Taboo > 20:
                                                ch_l "Не на людях."
                                            else:
                                                if not Player.Male:
                                                    ch_l "Ты не настолько милая, [LauraX.Petname]!"
                                                else:
                                                    ch_l "Ты не настолько милый, [LauraX.Petname]!"
                                            return #jump Laura_Clothes
                        $ Line = get_clothing_name(LauraX.Panties_key, vin)
                        $ LauraX.Panties = 0
                        if not LauraX.Legs:
                            "Она снимает [Line], затем бросает их на пол."
                            if not renpy.showing('DressScreen'):
                                    call Girl_First_Bottomless(LauraX)
                        elif ApprovalCheck(LauraX, 1200, TabM=4):
                            $ Trigger = LauraX.Legs
                            $ LauraX.Legs = 0
                            pause 0.5
                            $ LauraX.Legs = Trigger
                            "Она снимает [get_clothing_name(LauraX.Legs_key, vin)] и [Line], затем снова надевает [get_clothing_name(LauraX.Legs_key, vin)]."
                            $ Trigger = 1
                            call Girl_First_Bottomless(LauraX,1)
                        elif LauraX.Legs == "skirt":
                            "Она залезает под юбку и снимает [Line]."
                        else:
                            $ LauraX.Blush = 1
                            "Она на мгновение отходит, а затем возвращается."
                            $ LauraX.Blush = 0
                        $ Line = 0

                "Почему бы тебе вместо этих не надеть черные трусики?" if LauraX.Panties and LauraX.Panties != "black panties" and LauraX.Panties != "leather panties":
                        if ApprovalCheck(LauraX, 1100, TabM=3):
                                ch_l "Наверное, можно."
                                $ LauraX.Panties = "black panties"
                        else:
                                call Display_DressScreen(LauraX)
                                if not _return:
                                        ch_l "Тебя это не касается."
                                else:
                                        $ LauraX.Panties = "black panties"

                "Почему бы тебе вместо этих не надеть трусики в расцветке Росомахи? (желто-синие трусики)" if "wolvie panties" in LauraX.Inventory and LauraX.Panties and LauraX.Panties != "wolvie panties":
                        if ApprovalCheck(LauraX, 1000, TabM=3):
                                ch_l "Наверное, можно."
                                $ LauraX.Panties = "wolvie panties"
                        else:
                                call Display_DressScreen(LauraX)
                                if not _return:
                                        ch_l "Тебя это не касается."
                                else:
                                        $ LauraX.Panties = "wolvie panties"

                "Почему бы тебе вместо этих не надеть кружевные трусики?" if "lace panties" in LauraX.Inventory and LauraX.Panties and LauraX.Panties != "lace panties":
                        if ApprovalCheck(LauraX, 1300, TabM=3):
                                ch_l "Наверное, можно."
                                $ LauraX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(LauraX)
                                if not _return:
                                        ch_l "Тебя это не касается."
                                else:
                                        $ LauraX.Panties = "lace panties"

                "Мне нравятся твои трусики бикини." if "bikini bottoms" in LauraX.Inventory and LauraX.Panties != "bikini bottoms":
                        if bg_current == "bg pool":
                                ch_l "Ладно."
                                $ LauraX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(LauraX, 1000, TabM=2):
                                    ch_l "Ладно."
                                    $ LauraX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(LauraX)
                                    if not _return:
                                            ch_l "Тут не место для \"бикини\". . ."
                                    else:
                                            $ LauraX.Panties = "bikini bottoms"

                "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not LauraX.Panties:
                        $ LauraX.FaceChange("bemused", 1)
                        if LauraX.Legs and (LauraX.Love+LauraX.Obed) <= (2 * LauraX.Inbt):
                            $ LauraX.Mouth = "smile"
                            ch_l "Я не уверена, насчет этого."
                            menu:
                                "Ну ладно.":
                                    return #jump Laura_Clothes
                                "Я настаиваю, надевай.":
                                    if (LauraX.Love+LauraX.Obed) <= (1.5 * LauraX.Inbt):
                                        $ LauraX.FaceChange("angry", Eyes="side")
                                        ch_l "А я настаиваю на обратном."
                                        return #jump Laura_Clothes
                                    else:
                                        $ LauraX.FaceChange("sadside")
                                        ch_l "Ох, ладно."
                        else:
                            ch_l "Ну ладно. . ."
                        menu:
                            extend ""
                            "Как насчет черных?":
                                    ch_l "Ладно, конечно."
                                    $ LauraX.Panties = "black panties"
                            "Как насчет трусиков в расцветке Росомахи?" if "wolvie panties" in LauraX.Inventory:
                                    ch_l "Конечно."
                                    $ LauraX.Panties  = "wolvie panties"
                            "Как насчет кружевных?" if "lace panties" in LauraX.Inventory:
                                    ch_l "Хорошо."
                                    $ LauraX.Panties  = "lace panties"
                "Неважно":
                    pass
            return #jump Laura_Clothes_Under
        "Неважно":
            pass
    return #jump Laura_Clothes
    #End of Laura Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Laura_Clothes_Misc:
        #Misc
        "Сухие волосы" if LauraX.Hair == "wet":
                ch_p "Тебе идут сухие волосы."
                if ApprovalCheck(LauraX, 600):
                    ch_l "Ладно."
                    $ LauraX.Hair = "long"
                else:
                    ch_l "Я не уверена, все хорошо и так."

        "Влажные волосы" if LauraX.Hair != "wet":
                ch_p "Тебе стоит увлажнить волосы."
                if ApprovalCheck(LauraX, 800):
                    ch_l "Хмм?"
                    $ LauraX.Hair = "wet"
                    "Она отходит на минуту и вскоре возвращается."
                    ch_l "Типа так?"
                else:
                    ch_l "Пфф, слишком сложно."

        "Отрасти волосы на лобке" if not LauraX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может, отрастишь?"
                call expression LauraX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in LauraX.Todo:
                        $ LauraX.FaceChange("bemused", 1)
                        ch_l "Даже я не могу отрастить их мгновенно."
                else:
                        $ LauraX.FaceChange("bemused", 1)
                        if ApprovalCheck(LauraX, 1000, TabM=0):
                            ch_l "Конечно, так будет проще. . ."
                        else:
                            $ LauraX.FaceChange("surprised")
                            $ LauraX.Brows = "angry"
                            ch_l "Это тебя никак не касается."
                            return #jump Laura_Clothes
                        $ LauraX.Todo.append("pubes")
                        $ LauraX.PubeC = 6
        "Побрей лобок" if LauraX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression LauraX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ LauraX.FaceChange("bemused", 1)
                if "shave" in LauraX.Todo:
                    ch_l "Ага, я помню."
                else:
                    if ApprovalCheck(LauraX, 1100, TabM=0):
                        ch_l "Правда? Пожалуй, я могла бы побрить его. . ."
                    else:
                        $ LauraX.FaceChange("surprised")
                        $ LauraX.Brows = "angry"
                        ch_l "Это тебя никак не касается."
                        return #jump Laura_Clothes
                    $ LauraX.Todo.append("shave")

        "Пирсинг [[Сначала посмотрите, как она выглядит без него] (locked)" if not LauraX.SeenPussy and not LauraX.SeenChest:
            pass

        "Надень пирсинг-кольца" if LauraX.Pierce != "ring" and (LauraX.SeenPussy or LauraX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсингом-кольцами."
                if "ring" in LauraX.Todo:
                    ch_l "Ага, я помню."
                else:
                    $ LauraX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(LauraX, 1150, TabM=0)
                    if ApprovalCheck(LauraX, 900, "L", TabM=0) or (Approval and LauraX.Love > 2* LauraX.Obed):
                        ch_l "Ты думаешь он правда мне подойдет?"
                    elif ApprovalCheck(LauraX, 600, "I", TabM=0) or (Approval and LauraX.Inbt > LauraX.Obed):
                        ch_l "Я уже давненько думаю об этом."
                    elif ApprovalCheck(LauraX, 500, "O", TabM=0) or Approval:
                        ch_l "Да, [LauraX.Petname]."
                    else:
                        $ LauraX.FaceChange("surprised")
                        $ LauraX.Brows = "angry"
                        ch_l "Мне это совсем не интересно, [LauraX.Petname]."
                        return #jump Laura_Clothes
                    $ LauraX.Todo.append("ring")

        "Надень пирсинг-штанги" if LauraX.Pierce != "barbell" and (LauraX.SeenPussy or LauraX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in LauraX.Todo:
                    ch_l "Ага, я помню."
                else:
                    $ LauraX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(LauraX, 1150, TabM=0)
                    if ApprovalCheck(LauraX, 900, "L", TabM=0) or (Approval and LauraX.Love > 2 * LauraX.Obed):
                        ch_l "Ты думаешь он правда мне подойдет?"
                    elif ApprovalCheck(LauraX, 600, "I", TabM=0) or (Approval and LauraX.Inbt > LauraX.Obed):
                        ch_l "Я уже давненько думаю об этом."
                    elif ApprovalCheck(LauraX, 500, "O", TabM=0) or Approval:
                        ch_l "Да, [LauraX.Petname]."
                    else:
                        $ LauraX.FaceChange("surprised")
                        $ LauraX.Brows = "angry"
                        ch_l "Мне это совсем не интересно, [LauraX.Petname]."
                        return #jump Laura_Clothes
                    $ LauraX.Todo.append("barbell")

        "Сними пирсинг" if LauraX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ LauraX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(LauraX, 1350, TabM=0)
                if ApprovalCheck(LauraX, 950, "L", TabM=0) or (Approval and LauraX.Love > LauraX.Obed):
                    ch_l "Определись уже. . ."
                elif ApprovalCheck(LauraX, 700, "I", TabM=0) or (Approval and LauraX.Inbt > LauraX.Obed):
                    ch_l "Наконец-то, он мне уже надоел."
                elif ApprovalCheck(LauraX, 600, "O", TabM=0) or Approval:
                    ch_l "Ладно."
                else:
                    $ LauraX.FaceChange("surprised")
                    $ LauraX.Brows = "angry"
                    ch_l "Я вроде как уже привязалась к нему."
                    return #jump Laura_Clothes
                $ LauraX.Pierce = 0

        "Чокер с медальоном" if LauraX.Neck != "leash choker":
                ch_p "Почему бы тебе не примерить чокер с медальоном?"
                ch_l "Ладно. . ."
                $ LauraX.Neck = "leash choker"
        "Сними чокер" if LauraX.Neck:
                ch_p "Может, снимешь чокер?"
                ch_l "Ладно. . ."
                $ LauraX.Neck = 0

        "Надень подтяжки" if LauraX.Acc != "suspenders" and LauraX.Acc != "suspenders2" and "halloween" in LauraX.History:
                $ LauraX.Acc = "suspenders"
        "Сними подтяжки" if LauraX.Acc == "suspenders" or LauraX.Acc == "suspenders2":
                $ LauraX.Acc = 0

        "Сдвинь подтяжки" if LauraX.Acc == "suspenders" or LauraX.Acc == "suspenders2":
                $ LauraX.Acc = "suspenders" if LauraX.Acc == "suspenders2" else "suspenders2"

        "Вкл\Выкл Браслеты":
                if LauraX.Arms != "wrists":
                        ch_p "Почему бы тебе не надеть браслеты?"
                else:
                        ch_p "Давай обойдемся без браслетов."
                ch_l "Ладно. . ."
                $ LauraX.Arms = "wrists" if LauraX.Arms != "wrists" else 0
        "Вкл\Выкл перчатки" if "halloween" in LauraX.History:
                if LauraX.Arms != "gloves":
                        ch_p "Почему бы тебе не надеть длинные перчатки?"
                else:
                        ch_p "Давай обойдемся без перчаток."
                ch_l "Ладно. . ."
                $ LauraX.Arms = "gloves" if LauraX.Arms != "gloves" else 0

        "Неважно":
            pass
    return #jump Laura_Clothes
    #End of Laura Misc Wardrobe

return
#End Laura Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
