# star Betsy chat interface
#Betsy Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Betsy_Relationship: #rkeljsvgb
    while True:
        menu:
            ch_b "Что ты желаешь обсудить?"
            "Хочешь стать моей девушкой?" if BetsyX not in Player.Harem and "ex" not in BetsyX.Traits:
                    $ BetsyX.DailyActions.append("relationship")
                    if "asked boyfriend" in BetsyX.DailyActions and "angry" in BetsyX.DailyActions:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Перестань спрашивать."
                            return
                    elif "asked boyfriend" in BetsyX.DailyActions:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Мой ответ остается неизменным - \"нет.\""
                            return
                    elif BetsyX.Break[0]:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Нет, если ты продолжишь играть со мной."
                            if Player.Harem:
                                    $ BetsyX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "Я уже ни с кем не встречаюсь."

                    $ BetsyX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "BetsyYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_b "А остальные с этим согласны, [BetsyX.Petname]?"
                        else:
                            ch_b "А [Player.Harem[0].Name] с этим согласна, [BetsyX.Petname]?"
                        return

                    if BetsyX.Event[5]:
                            $ BetsyX.FaceChange("bemused", 1)
                            if not Player.Male:
                                ch_b "В прошлом ты мне отказала. . ."
                            else:
                                ch_b "В прошлом ты мне отказал. . ."
                    else:
                            $ BetsyX.FaceChange("surprised", 2)
                            ch_b "Что? . ."
                            $ BetsyX.FaceChange("smile", 1)

                    call Betsy_OtherWoman

                    if BetsyX.Love >= 800:
                            $ BetsyX.FaceChange("surprised", 1)
                            $ BetsyX.Mouth = "smile"
                            if not BetsyX.Event[5]:
                                    $ BetsyX.Statup("Love", 200, 10)
                                    call Betsy_BF
                                    return
                            $ BetsyX.Statup("Love", 200, 40)
                            ch_b "Конечно!"
                            if "boyfriend" not in BetsyX.Petnames:
                                    $ BetsyX.Petnames.append("boyfriend")
                            if "BetsyYes" in Player.Traits:
                                    $ Player.Traits.remove("BetsyYes")
                            $ Player.Harem.append(BetsyX)
                            call Harem_Initiation
                            "[BetsyX.Name] обнимает вас и крепко целует."
                            $ BetsyX.FaceChange("kiss", 1)
                            $ BetsyX.Kissed += 1
                    elif BetsyX.Obed >= 500:
                            $ BetsyX.FaceChange("perplexed")
                            ch_b "Я не уверена, что желаю \"встречаться\". . ."
                    elif BetsyX.Inbt >= 500:
                            $ BetsyX.FaceChange("smile")
                            ch_b "Я бы предпочла, чтобы все осталось как прежде."
                    else:
                            $ BetsyX.FaceChange("perplexed", 1)
                            ch_b "Притормози, [BetsyX.Petname]."

            "Может, начнем все сначала?" if "ex" in BetsyX.Traits:
                    $ BetsyX.DailyActions.append("relationship")
                    if "asked boyfriend" in BetsyX.DailyActions and "angry" in BetsyX.DailyActions:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Перестань спрашивать."
                            return
                    elif "asked boyfriend" in BetsyX.DailyActions:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Я останусь при своем мнении."
                            return

                    $ BetsyX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "BetsyYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_b "А остальные это примут, [BetsyX.Petname]?"
                            else:
                                ch_b "А [Player.Harem[0].Name] это примет, [BetsyX.Petname]?"
                            return

                    $ Cnt = 0
                    call Betsy_OtherWoman

                    if BetsyX.Love >= 800:
                            $ BetsyX.FaceChange("surprised", 1)
                            $ BetsyX.Mouth = "smile"
                            $ BetsyX.Statup("Love", 90, 5)
                            ch_b "Пожалуй, я могу дать тебе еще один шанс."
                            if "boyfriend" not in BetsyX.Petnames:
                                        $ BetsyX.Petnames.append("boyfriend")
                            $ BetsyX.Traits.remove("ex")
                            if "BetsyYes" in Player.Traits:
                                    $ Player.Traits.remove("BetsyYes")
                            $ Player.Harem.append(BetsyX)
                            call Harem_Initiation
                            "[BetsyX.Name] притягивает вас к себе и крепко целует."
                            $ BetsyX.FaceChange("kiss", 1)
                            $ BetsyX.Kissed += 1
                    elif BetsyX.Love >= 600 and ApprovalCheck(BetsyX, 1500):
                            $ BetsyX.FaceChange("smile", 1)
                            $ BetsyX.Statup("Love", 90, 5)
                            ch_b "Пожалуй, я согласна. . ."
                            if "boyfriend" not in BetsyX.Petnames:
                                    $ BetsyX.Petnames.append("boyfriend")
                            $ BetsyX.Traits.remove("ex")
                            if "BetsyYes" in Player.Traits:
                                    $ Player.Traits.remove("BetsyYes")
                            $ Player.Harem.append(BetsyX)
                            call Harem_Initiation
                            $ BetsyX.FaceChange("kiss", 1)
                            "[BetsyX.Name] дарит вам легкий поцелуй."
                            $ BetsyX.FaceChange("sly", 1)
                            $ BetsyX.Kissed += 1
                    elif BetsyX.Obed >= 500:
                            $ BetsyX.FaceChange("sad")
                            ch_b "Я не думаю, что у нас что-то получится. . ."
                    elif BetsyX.Inbt >= 500:
                            $ BetsyX.FaceChange("perplexed")
                            ch_b "Наши отношения теперь в прошлом."
                    else:
                            $ BetsyX.FaceChange("sadside", 1)
                            ch_b "Я не думаю, что смогу вынести это снова. . ."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if BetsyX in Player.Harem:
                            call AskDateOther

            "Думаю, мы должны расстаться." if BetsyX in Player.Harem:
                            if "breakup talk" in BetsyX.RecentActions:
                                    ch_b "Перестань об этом спрашивать."
                            elif "breakup talk" in BetsyX.DailyActions:
                                    ch_b "Опять эта чушь?"
                                    ch_b "Хватит, [BetsyX.Petname]."
                            else:
                                    call Breakup(BetsyX)

            "О разговоре, который у нас был ранее. . .":
                menu:
                    "Помнишь, ты признавалась мне в любви. . ?" if "lover" not in BetsyX.Traits and BetsyX.Event[6] >= 20 and BetsyX.Event[6] != 23:
                            call Betsy_Love_Redux

                    "Помнишь, ты рассказывала мне о себе. . ?" if "lover" not in BetsyX.Traits and BetsyX.Event[6] == 23:
                            call Betsy_Love_Redux

                    "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировал?" if "sir" not in BetsyX.Petnames and "sir" in BetsyX.History and Player.Male:
                            if "asked sub" in BetsyX.RecentActions:
                                    ch_b "Перестань об этом спрашивать."
                            elif "asked sub" in BetsyX.DailyActions:
                                    ch_b "Хватит, [BetsyX.Petname]."
                            else:
                                    call Betsy_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировала?" if "sir" not in BetsyX.Petnames and "sir" in BetsyX.History and not Player.Male:
                            if "asked sub" in BetsyX.RecentActions:
                                    ch_b "Перестань об этом спрашивать."
                            elif "asked sub" in BetsyX.DailyActions:
                                    ch_b "Хватит, [BetsyX.Petname]."
                            else:
                                    call Betsy_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоим хозяйкой?" if "master" not in BetsyX.Petnames and "master" in BetsyX.History and not Player.Male:
                            if "asked sub" in BetsyX.RecentActions:
                                    ch_b "Перестань об этом спрашивать."
                            elif "asked sub" in BetsyX.DailyActions:
                                    ch_b "Хватит, [BetsyX.Petname]."
                            else:
                                    call Betsy_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоим хозяином?" if "master" not in BetsyX.Petnames and "master" in BetsyX.History and Player.Male:
                            if "asked sub" in BetsyX.RecentActions:
                                    ch_b "Перестань об этом спрашивать."
                            elif "asked sub" in BetsyX.DailyActions:
                                    ch_b "Хватит, [BetsyX.Petname]."
                            else:
                                    call Betsy_Sub_Asked
                    "Неважно":
                            pass

            "Неважно":
                return

    return

label Betsy_OtherWoman(Cnt = 0): #rkeljsvgb
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((BetsyX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ BetsyX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_b "Я слышала, что ты сейчас с [Player.Harem[0].Name_tvo] и другими?"
    else:
        ch_b "Я слышала, что ты сейчас с [Player.Harem[0].Name_tvo]?"
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "BetsyYes" in Player.Traits:
                if ApprovalCheck(BetsyX, 1800, Bonus = Cnt):
                        $ BetsyX.FaceChange("smile", 1)
                        if BetsyX.Love >= BetsyX.Obed:
                                ch_b "Тогда, пожалуй, мы можем перейти на следующий уровень."
                        elif BetsyX.Obed >= BetsyX.Inbt:
                                ch_b "Тогда, пожалуй, мы можем перейти на следующий уровень."
                        else:
                                ch_b "Ох, хорошо. . ."
                else:
                        $ BetsyX.FaceChange("angry", 1)
                        ch_b "Но я все равно не могу согласиться на такое."
                        $ renpy.pop_call()
                        #This causes it to jump past the previous menu on the return

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "BetsyYes" not in Player.Traits and not Player.Male:
                if ApprovalCheck(BetsyX, 1800, Bonus = Cnt):
                        $ BetsyX.FaceChange("smile", 1)
#                        if BetsyX.Love >= BetsyX.Obed:
#                            ch_b "Then I may consider it. . ."
#                        elif BetsyX.Obed >= BetsyX.Inbt:
#                            ch_b "Then I may consider it. . ."
#                        else:
#                            ch_b "Then sure, why not."
                        ch_b "Тогда я могу рассмотреть твое предложение. . ."
                        ch_b "Давай завтра снова все обсудим."
                else:
                        $ BetsyX.FaceChange("angry", 1)
                        ch_b "Но я все равно не могу согласиться на такое."
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "BetsyYes" not in Player.Traits and Player.Male:
                if ApprovalCheck(BetsyX, 1800, Bonus = Cnt):
                        $ BetsyX.FaceChange("smile", 1)
#                        if BetsyX.Love >= BetsyX.Obed:
#                            ch_b "Then I may consider it. . ."
#                        elif BetsyX.Obed >= BetsyX.Inbt:
#                            ch_b "Then I may consider it. . ."
#                        else:
#                            ch_b "Then sure, why not."
                        ch_b "Тогда я могу рассмотреть твое предложение. . ."
                        ch_b "Давай завтра снова все обсудим."
                else:
                        $ BetsyX.FaceChange("angry", 1)
                        ch_b "Но я все равно не могу согласиться на такое."
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
                if not ApprovalCheck(BetsyX, 1800, Bonus = -Cnt): #checks if Betsy likes you more than the other girl
                        $ BetsyX.FaceChange("angry", 1)
                        if not ApprovalCheck(BetsyX, 1800):
                                ch_b "Представляю, насколько ей может быть больно, боюсь, я не могу на это пойти."
                        else:
                                ch_b "Тебе следует быть выше этого."
                        $ renpy.pop_call()
                else:
                        $ BetsyX.FaceChange("smile", 1)
                        if BetsyX.Love >= BetsyX.Obed:
                                ch_b "Пожалуй, это правда. . ."
                        elif BetsyX.Obed >= BetsyX.Inbt:
                                ch_b "Если ты этого хочешь. . ."
                        else:
                                ch_b "Что ж, хорошо."
                        $ BetsyX.Traits.append("downlow")

        "Я могу порвать с ней.":
                    $ BetsyX.FaceChange("sad")
                    ch_b "Тогда после и поговорим."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ BetsyX.FaceChange("sad")
                    ch_b "Согласна."
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ BetsyX.FaceChange("sad")
                    ch_b "Согласна."
                    $ renpy.pop_call()

    return


label Betsy_About(Check=0): #rkeljsvgb
    if Check not in TotalGirls:
            ch_b "Это кто?"
            return
    ch_b "Что я думаю о ней? Что ж. . ."
    if Check == RogueX:
            if "poly Rogue" in BetsyX.Traits:
                ch_b "Мы довольно. . . близки."
            elif BetsyX.LikeRogue >= 900:
                ch_b "Она полна. . . энергии."
            elif BetsyX.LikeRogue >= 800:
                ch_b "Она довольно милая, правда?"
            elif BetsyX.LikeRogue >= 700:
                ch_b "Она довольно милая."
            elif BetsyX.LikeRogue >= 600:
                ch_b "Мы хорошие подруги."
            elif BetsyX.LikeRogue >= 500:
                ch_b "Мы не так уж и часто общались друг с другом."
            elif BetsyX.LikeRogue >= 400:
                ch_b "Не думаю, что мы можем с ней поладить."
            elif BetsyX.LikeRogue >= 300:
                ch_b "Она меня очень раздражает."
            else:
                ch_b "Боже, я вообще не хочу ее обсуждать."
    elif Check == KittyX:
            if "poly Kitty" in BetsyX.Traits:
                ch_b "Мы довольно. . . близки."
            elif BetsyX.LikeKitty >= 900:
                ch_b "Она очень нежная."
            elif BetsyX.LikeKitty >= 800:
                ch_b "Она такая маленькая!"
            elif BetsyX.LikeKitty >= 700:
                ch_b "Она замечательно танцует."
            elif BetsyX.LikeKitty >= 600:
                ch_b "Мы хорошие подруги."
            elif BetsyX.LikeKitty >= 500:
                ch_b "Нам нечасто удавалось пообщаться."
            elif BetsyX.LikeKitty >= 400:
                ch_b "Не думаю, что мы можем с ней поладить."
            elif BetsyX.LikeKitty >= 300:
                ch_b "Она меня очень раздражает."
            else:
                ch_b "Боже, я вообще не хочу ее обсуждать."
    elif Check == LauraX:
            if "poly Laura" in BetsyX.Traits:
                ch_b "Мы довольно. . . близки."
            elif BetsyX.LikeLaura >= 900:
                ch_b "Она довольно. . . активная."
            elif BetsyX.LikeLaura >= 800:
                ch_b "Она в хорошей форме."
            elif BetsyX.LikeLaura >= 700:
                ch_b "Я не могу за ней угнаться. . ."
            elif BetsyX.LikeLaura >= 600:
                ch_b "Она довольно спортивная."
            elif BetsyX.LikeLaura >= 500:
                ch_b "Мы не так уж и часто общались друг с другом."
            elif BetsyX.LikeLaura >= 400:
                ch_b "Не думаю, что мы можем с ней поладить."
            elif BetsyX.LikeLaura >= 300:
                ch_b "Она меня очень раздражает."
            else:
                ch_b "Боже, я вообще не хочу ее обсуждать."
    elif Check == EmmaX:
            if "poly Emma" in BetsyX.Traits:
                ch_b "Мы довольно. . . близки."
            elif BetsyX.LikeEmma >= 900:
                ch_b "Она . . . впечатляет."
            elif BetsyX.LikeEmma >= 800:
                ch_b "Она очень красивая. . ."
            elif BetsyX.LikeEmma >= 700:
                ch_b "У нее довольно утонченные вкусы."
            elif BetsyX.LikeEmma >= 600:
                ch_b "С ее помощью я замечательно ознакомилась с учебной программой."
            elif BetsyX.LikeEmma >= 500:
                ch_b "Она уважаемый преподаватель."
            elif BetsyX.LikeEmma >= 400:
                ch_b "Не думаю, что мы можем с ней поладить."
            elif BetsyX.LikeEmma >= 300:
                ch_b "Она меня очень раздражает."
            else:
                ch_b "Боже, я вообще не хочу ее обсуждать."
    elif Check == JeanX:
            if "poly Jean" in BetsyX.Traits:
                ch_b "Мы. . . время от времени общаемся друг с другом."
            elif BetsyX.LikeJean >= 900:
                ch_b "Я думаю, что у нее более плохая репутация, чем она того заслуживает. . ."
            elif BetsyX.LikeJean >= 800:
                ch_b "Она может быть довольно ужасной, но она в хорошей форме. . ."
            elif BetsyX.LikeJean >= 700:
                ch_b "У нее. . . большой опыт."
            elif BetsyX.LikeJean >= 600:
                ch_b "Пожалуй, она вполне сносная."
            elif BetsyX.LikeJean >= 500:
                ch_b "Она немного доставучая."
            elif BetsyX.LikeJean >= 400:
                ch_b "Не думаю, что мы можем с ней поладить."
            elif BetsyX.LikeJean >= 300:
                ch_b "Она меня очень раздражает."
            else:
                ch_b "Она та еще сука."
                if not Player.Male:
                    ch_b "Ну, думаю, ты и сама это прекрасно знаешь."
                else:
                    ch_b "Ну, думаю, ты и сам это прекрасно знаешь."
    elif Check == StormX:
            if "poly Storm" in BetsyX.Traits:
                ch_b "Мы довольно. . . близки."
            elif BetsyX.LikeStorm >= 900:
                ch_b "Она подобна статуе из Британского музея."
            elif BetsyX.LikeStorm >= 800:
                ch_b "Она. . . эффектная. . ."
            elif BetsyX.LikeStorm >= 700:
                ch_b "Мне нравятся ее занятия."
            elif BetsyX.LikeStorm >= 600:
                ch_b "Она встретила меня довольно тепло."
            elif BetsyX.LikeStorm >= 500:
                ch_b "Не думаю, что мы можем с ней поладить."
            elif BetsyX.LikeStorm >= 400:
                ch_b "Она может быть довольно злой."
            elif BetsyX.LikeStorm >= 300:
                ch_b "Она меня очень раздражает."
            else:
                ch_b "Боже, я вообще не хочу ее обсуждать."
    elif Check == JubesX:
            if "poly Jubes" in BetsyX.Traits:
                ch_b "Мы довольно. . . близки."
            elif BetsyX.LikeJubes >= 900:
                ch_b "Она любит пускать в ход свой рот. . ."
            elif BetsyX.LikeJubes >= 800:
                ch_b "Она очаровательна. . ."
            elif BetsyX.LikeJubes >= 700:
                ch_b "Мы довольно часто ходим по магазинам."
            elif BetsyX.LikeJubes >= 600:
                ch_b "Она очень дружелюбная."
            elif BetsyX.LikeJubes >= 500:
                ch_b "Мы не так уж и часто общались друг с другом."
            elif BetsyX.LikeJubes >= 400:
                ch_b "Не думаю, что мы можем с ней поладить."
            elif BetsyX.LikeJubes >= 300:
                ch_b "Она меня очень раздражает."
            else:
                ch_b "Боже, я вообще не хочу ее обсуждать."
    elif Check == GwenX:
            if "poly Gwen" in BetsyX.Traits:
                ch_b "Мы довольно. . . близки."
            elif BetsyX.LikeGwen >= 900:
                ch_b "У нее очень насыщенное прошлое."
            elif BetsyX.LikeGwen >= 800:
                ch_b "Она очень милая, не так ли?"
            elif BetsyX.LikeGwen >= 700:
                ch_b "Кажется, она везде, куда бы я ни пошла."
            elif BetsyX.LikeGwen >= 600:
                ch_b "Она довольно напористая."
            elif BetsyX.LikeGwen >= 500:
                ch_b "Мы не так уж и часто общались друг с другом."
            elif BetsyX.LikeGwen >= 400:
                ch_b "Не думаю, что мы можем с ней поладить."
            elif BetsyX.LikeGwen >= 300:
                ch_b "Она меня очень раздражает."
            else:
                ch_b "Боже, я вообще не хочу ее обсуждать."
    elif Check == DoreenX:
            if "poly Doreen" in BetsyX.Traits:
                ch_b "Мы довольно. . . близки."
            elif BetsyX.LikeDoreen >= 900:
                ch_b "Она многое пережила."
            elif BetsyX.LikeDoreen >= 800:
                ch_b "Она очень милая, не так ли?"
            elif BetsyX.LikeDoreen >= 700:
                ch_b "Кажется, она везде, куда бы я ни пошла."
            elif BetsyX.LikeDoreen >= 600:
                ch_b "Она довольно дружелюбная."
            elif BetsyX.LikeDoreen >= 500:
                ch_b "Мы не так уж и часто общались друг с другом."
            elif BetsyX.LikeDoreen >= 400:
                ch_b "Не думаю, что мы можем с ней поладить."
            elif BetsyX.LikeDoreen >= 300:
                ch_b "Она меня очень раздражает."
            else:
                ch_b "Боже, я вообще не хочу ее обсуждать."
    elif Check == WandaX:
            if "poly Wanda" in BetsyX.Traits:
                ch_b "Мы довольно. . . близки, не так ли?"
            elif BetsyX.LikeWanda >= 900:
                ch_b "Она довольно. . . энергичная."
            elif BetsyX.LikeWanda >= 800:
                ch_b "Она довольно милая, правда?"
            elif BetsyX.LikeWanda >= 700:
                ch_b "Она весьма очаровательна."
            elif BetsyX.LikeWanda >= 600:
                ch_b "Она прекрасная подруга."
            elif BetsyX.LikeWanda >= 500:
                ch_b "Мы не так уж много времени провели вместе."
            elif BetsyX.LikeWanda >= 400:
                ch_b "Думаю, мы не особо ладим."
            elif BetsyX.LikeWanda >= 300:
                ch_b "Она меня довольно сильно раздражает."
            else:
                ch_b "Боже, не хочу ее обсуждать."
    else:
                ch_b "Я бы не хотела этого обсуждать."
    return
#End Betsy_AboutEmma

label Betsy_Monogamy: #rkeljsvgb
        #called from Betsy_Settings to ask her not to hook up with other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in BetsyX.Traits:
                    if BetsyX.Thirst >= 60 and not ApprovalCheck(BetsyX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ BetsyX.FaceChange("sly",1)
                            if "mono" not in BetsyX.DailyActions:
                                    $ BetsyX.Statup("Obed", 90, -2)
                            if not Player.Male:
                                ch_b "Я бы была менее распутной, если бы ты предложила альтернативу. . ."
                            else:
                                ch_b "Я бы была менее распутной, если бы ты предложил альтернативу. . ."
                            return
                    elif ApprovalCheck(BetsyX, 1200, "LO", TabM=0) and BetsyX.Love >= BetsyX.Obed:
                            #she cares
                            $ BetsyX.FaceChange("sly",1)
                            if "mono" not in BetsyX.DailyActions:
                                    $ BetsyX.Statup("Love", 90, 1)
                            ch_b "Это можно устроить, если ты выдержишь последствия."
                    elif ApprovalCheck(BetsyX, 700, "O", TabM=0):
                            #she is obedient
                            $ BetsyX.FaceChange("sly",1,Eyes="side")
                            ch_b "Ох, это можно."
                    else:
                            #she doesn't care
                            $ BetsyX.FaceChange("sly",1)
                            ch_b "Боюсь, у меня есть некие потребности, которые необходимо удовлетворять."
                            return
                    if "mono" not in BetsyX.DailyActions:
                            $ BetsyX.Statup("Obed", 90, 3)
                    $ BetsyX.AddWord(1,0,"mono") #Daily
                    $ BetsyX.Traits.append("mono")
            "Не встречайся с другими девушками." if "mono" not in BetsyX.Traits:
                    if ApprovalCheck(BetsyX, 900, "O", TabM=0):
                            #she is obedient
                            $ BetsyX.FaceChange("sly",1,Eyes="side")
                            ch_b "Если это так необходимо."
                    elif BetsyX.Thirst >= 60 and not ApprovalCheck(BetsyX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ BetsyX.FaceChange("sly",1)
                            if "mono" not in BetsyX.DailyActions:
                                    $ BetsyX.Statup("Obed", 90, -2)
                            if not Player.Male:
                                ch_b "Я бы была менее распутной, если бы ты предложила альтернативу. . ."
                            else:
                                ch_b "Я бы была менее распутной, если бы ты предложил альтернативу. . ."
                            return
                    elif ApprovalCheck(BetsyX, 600, "O", TabM=0):
                            #she is obedient
                            $ BetsyX.FaceChange("sly",1,Eyes="side")
                            ch_b "Если это так необходимо."
                    elif ApprovalCheck(BetsyX, 1400, "LO", TabM=0):
                            #she cares
                            $ BetsyX.FaceChange("sly",1)
                            ch_b "Это можно устроить, если ты выдержишь последствия."
                    else:
                            #she doesn't care
                            $ BetsyX.FaceChange("sly",1,Brows="confused")
                            ch_b "Боюсь, у меня есть некие потребности, которые необходимо удовлетворять."
                            return
                    if "mono" not in BetsyX.DailyActions:
                            $ BetsyX.Statup("Obed", 90, 3)
                    $ BetsyX.AddWord(1,0,"mono") #Daily
                    $ BetsyX.Traits.append("mono")
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in BetsyX.Traits:
                    if ApprovalCheck(BetsyX, 700, "O", TabM=0):
                            $ BetsyX.FaceChange("sly",1,Eyes="side")
                            ch_b "Замечательно!"
                    elif ApprovalCheck(BetsyX, 800, "L", TabM=0):
                            $ BetsyX.FaceChange("sly",1)
                            ch_b "Замечательно. . ."
                    else:
                            $ BetsyX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in BetsyX.DailyActions:
                                    $ BetsyX.Statup("Love", 90, -2)
                            ch_b "О, чудесно!"
                    if "mono" not in BetsyX.DailyActions:
                            $ BetsyX.Statup("Obed", 90, 3)
                    if "mono" in BetsyX.Traits:
                            $ BetsyX.Traits.remove("mono")
                    $ BetsyX.AddWord(1,0,"mono") #Daily
            "Неважно.":
                pass
        return

# end Betsy monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Betsy_Jumped: #rkeljsvgb
        #called from Betsy_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ BetsyX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_b "Я бы назвала это по-другому. . ."
            "На будущее, можешь сначала спрашивать?" if "chill" not in BetsyX.Traits:
                    if BetsyX.Thirst >= 60 and not ApprovalCheck(BetsyX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ BetsyX.FaceChange("sly",1)
                            if "chill" not in BetsyX.DailyActions:
                                    $ BetsyX.Statup("Obed", 90, -2)
                            ch_b "Боюсь, это единственный способ получить твое внимание. . ."
                            return
                    elif ApprovalCheck(BetsyX, 1000, "LO", TabM=0) and BetsyX.Love >= BetsyX.Obed:
                            #she cares
                            $ BetsyX.FaceChange("surprised",1)
                            if "chill" not in BetsyX.DailyActions:
                                    $ BetsyX.Statup("Love", 90, 1)
                            ch_b "Я -сожалею- об этом. . ."
                            $ BetsyX.FaceChange("sly",1,Eyes="side")
                            ch_b "Я попробую. . ."
                    elif ApprovalCheck(BetsyX, 500, "O", TabM=0):
                            #she is obedient
                            $ BetsyX.FaceChange("sly",1,Eyes="side")
                            ch_b "Я -сожалею- об этом. . ."
                    else:
                            #she doesn't care
                            $ BetsyX.FaceChange("sly",1)
                            ch_b "Все зависит только от тебя. . ."
                            return
                    if "chill" not in BetsyX.DailyActions:
                            $ BetsyX.Statup("Obed", 90, 3)
                    $ BetsyX.AddWord(1,0,"chill") #Daily
                    $ BetsyX.Traits.append("chill")
            "Больше так не делай." if "chill" not in BetsyX.Traits:
                    if ApprovalCheck(BetsyX, 800, "O", TabM=0):
                            #she is obedient
                            $ BetsyX.FaceChange("sly",1,Eyes="side")
                            ch_b "Если это так необходимо."
                    elif BetsyX.Thirst >= 60 and not ApprovalCheck(BetsyX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ BetsyX.FaceChange("sly",1)
                            if "chill" not in BetsyX.DailyActions:
                                    $ BetsyX.Statup("Obed", 90, -2)
                            ch_b "Боюсь, это единственный способ получить твое внимание. . ."
                            return
                    elif ApprovalCheck(BetsyX, 400, "O", TabM=0):
                            #she is obedient
                            $ BetsyX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_b "Да, госпожа. . ."
                            else:
                                ch_b "Да, господин. . ."
                    elif ApprovalCheck(BetsyX, 500, "LO", TabM=0) and not ApprovalCheck(BetsyX, 500, "I", TabM=0):
                            #she cares
                            $ BetsyX.FaceChange("sly",1)
                            ch_b "Мне не нравится твой тон, но я попробую."
                    else:
                            #she doesn't care
                            $ BetsyX.FaceChange("sly",1)
                            ch_b "Не волнуйся, я позабочусь о том, чтобы тебе понравилось."
                            return
                    if "chill" not in BetsyX.DailyActions:
                            $ BetsyX.Statup("Obed", 90, 3)
                    $ BetsyX.AddWord(1,0,"chill") #Daily
                    $ BetsyX.Traits.append("chill")
            "Делай что хочешь.":
                    if ApprovalCheck(BetsyX, 800, "L", TabM=0):
                            $ BetsyX.FaceChange("sly",1)
                            ch_b "Ох, восхитительно. . ."
                    elif ApprovalCheck(BetsyX, 700, "O", TabM=0):
                            $ BetsyX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_b "Ох, поняла, госпожа."
                            else:
                                ch_b "Ох, поняла, господин."
                    else:
                            $ BetsyX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in BetsyX.DailyActions:
                                    $ BetsyX.Statup("Love", 90, -2)
                            ch_b "Если это будет необходимо. . ."
                    if "chill" not in BetsyX.DailyActions:
                            $ BetsyX.Statup("Obed", 90, 3)
                    if "chill" in BetsyX.Traits:
                            $ BetsyX.Traits.remove("chill")
                    $ BetsyX.AddWord(1,0,"chill") #Daily
            "Эм, неважно.":
                pass
        return

# end Betsy jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start Betsy hungry //////////////////////////////////////////////////////////
label Betsy_Hungry: #rkeljsvgb
    if BetsyX.Chat[3]:
        ch_b "Знаешь, меня мучает жажда. . ."
    elif BetsyX.Chat[2]:
        ch_b "Мне очень понравилась твоя сыворотка. . ."
    else:
        ch_b "Знаешь, меня мучает жажда. . ."
        ch_b "Уверена, ты понимаешь, к чему я веду. . ."
    $ BetsyX.Traits.append("hungry")
return


# end Betsy hungry //////////////////////////////////////////////////////////

# Betsy Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Betsy_SexChat: #rkeljsvgb
    $ Line = "Что ты желаешь обсудить?" if not Line else Line
    while True:
            menu:
                ch_b "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in BetsyX.DailyActions:
                        ch_b "Я в курсе."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ BetsyX.FaceChange("sly")
                                        if BetsyX.PlayerFav == "sex":
                                            $ BetsyX.Statup("Lust", 80, 5)
                                            ch_b "Я прекрасно об этом знаю. . ."
                                        elif BetsyX.Favorite == "sex":
                                            $ BetsyX.Statup("Love", 90, 5)
                                            $ BetsyX.Statup("Lust", 80, 10)
                                            ch_b "Серьезно? Потрясающе!"
                                        elif BetsyX.Sex >= 5:
                                            ch_b "Что ж, я не против."
                                        elif not BetsyX.Sex:
                                            $ BetsyX.FaceChange("perplexed")
                                            ch_b "Воу, могу я узнать, с кем ты трахаешься?"
                                        else:
                                            $ BetsyX.FaceChange("bemused")
                                            ch_b "Ох, конечно. . ."
                                        $ BetsyX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ BetsyX.FaceChange("sly")
                                        if BetsyX.PlayerFav == "anal":
                                            $ BetsyX.Statup("Lust", 80, 5)
                                            ch_b "Я прекрасно об этом знаю. . ."
                                        elif BetsyX.Favorite == "anal":
                                            $ BetsyX.Statup("Love", 90, 5)
                                            $ BetsyX.Statup("Lust", 80, 10)
                                            ch_b "Мне тоже это нравится!"
                                        elif BetsyX.Anal >= 10:
                                            ch_b "Ага, это. . . чудесно. . ."
                                        elif not BetsyX.Anal:
                                            $ BetsyX.FaceChange("perplexed")
                                            ch_b "Воу, могу я узнать, с кем ты трахаешься?"
                                        else:
                                            $ BetsyX.FaceChange("bemused",Eyes="side")
                                            ch_b "Ох, ясно. . ."
                                        $ BetsyX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ BetsyX.FaceChange("sly")
                                        if BetsyX.PlayerFav == "blow":
                                            $ BetsyX.Statup("Lust", 80, 3)
                                            ch_b "Я прекрасно об этом знаю. . ."
                                        elif BetsyX.Favorite == "blow":
                                            $ BetsyX.Statup("Love", 90, 5)
                                            $ BetsyX.Statup("Lust", 80, 5)
                                            ch_b "Мне тоже это нравится!"
                                        elif BetsyX.Blow >= 10:
                                            ch_b "Что ж, ты очень даже вкусный."
                                        elif not BetsyX.Blow:
                                            $ BetsyX.FaceChange("perplexed")
                                            ch_b "Воу, могу я узнать, кто сосет тебе?"
                                        else:
                                            $ BetsyX.FaceChange("bemused")
                                            ch_b "Это. . . довольно увлекательно. . ."
                                        $ BetsyX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ BetsyX.FaceChange("sly")
                                        if BetsyX.PlayerFav == "cun":
                                            $ BetsyX.Statup("Lust", 80, 3)
                                            ch_b "Я прекрасно об этом знаю. . ."
                                        elif BetsyX.Favorite == "cun":
                                            $ BetsyX.Statup("Love", 90, 5)
                                            $ BetsyX.Statup("Lust", 80, 5)
                                            ch_b "Мне очень нравится твоя киска!"
                                        elif BetsyX.CUN >= 10:
                                            ch_b "Конечно, ты очень вкусная."
                                        elif not BetsyX.CUN:
                                            $ BetsyX.FaceChange("perplexed")
                                            ch_b "Воу, могу я узнать, кто лижет тебе?"
                                        else:
                                            $ BetsyX.FaceChange("bemused")
                                            ch_b "Это. . . довольно приятно. . ."
                                        $ BetsyX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ BetsyX.FaceChange("sly")
                                        if BetsyX.PlayerFav == "titjob":
                                            $ BetsyX.Statup("Lust", 80, 5)
                                            ch_b "Я прекрасно об этом знаю. . ."
                                        elif BetsyX.Favorite == "titjob":
                                            $ BetsyX.Statup("Love", 90, 5)
                                            $ BetsyX.Statup("Lust", 80, 7)
                                            ch_b "Мне тоже это нравится!"
                                        elif BetsyX.Tit >= 10:
                                            ch_b "Это, безусловно, интересный опыт . . ."
                                        elif not BetsyX.Tit:
                                            $ BetsyX.FaceChange("perplexed")
                                            ch_b "Воу, могу я узнать, кто трахает тебя грудью?"
                                        else:
                                            $ BetsyX.FaceChange("bemused")
                                            ch_b "И почему я не удивлена? . ."
                                            $ BetsyX.Statup("Love", 80, 5)
                                            $ BetsyX.Statup("Inbt", 50, 10)
                                        $ BetsyX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ BetsyX.FaceChange("sly")
                                        if BetsyX.PlayerFav == "foot":
                                            $ BetsyX.Statup("Lust", 80, 5)
                                            ch_b "Я прекрасно об этом знаю. . ."
                                        elif BetsyX.Favorite == "foot":
                                            $ BetsyX.Statup("Love", 90, 5)
                                            $ BetsyX.Statup("Lust", 80, 7)
                                            ch_b "Это, безусловно, увлекательно. . ."
                                        elif BetsyX.Foot >= 10:
                                            ch_b "Мне это тоже очень нравится. . ."
                                        elif not BetsyX.Foot:
                                            $ BetsyX.FaceChange("perplexed")
                                            ch_b "Воу, могу я узнать, кто играется с тобой ножками?"
                                        else:
                                            $ BetsyX.FaceChange("bemused")
                                            ch_b "Конечно, это довольно приятно. . ."
                                        $ BetsyX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ BetsyX.FaceChange("sly")
                                        if BetsyX.PlayerFav == "hand":
                                            $ BetsyX.Statup("Lust", 80, 5)
                                            ch_b "Я прекрасно об этом знаю. . ."
                                        elif BetsyX.Favorite == "hand":
                                            $ BetsyX.Statup("Love", 90, 5)
                                            $ BetsyX.Statup("Lust", 80, 7)
                                            ch_b "Мне очень нравится держать его в руках. . ."
                                        elif BetsyX.Hand >= 10:
                                            ch_b "Мне это тоже очень нравится. . ."
                                        elif not BetsyX.Hand:
                                            $ BetsyX.FaceChange("perplexed")
                                            ch_b "Воу, могу я узнать, кто мастурбирует тебе?"
                                        else:
                                            $ BetsyX.FaceChange("bemused")
                                            ch_b "Конечно, это довольно приятно. . ."
                                        $ BetsyX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ BetsyX.FaceChange("sly")
                                        if BetsyX.PlayerFav == "finger":
                                            $ BetsyX.Statup("Lust", 80, 5)
                                            ch_b "Я прекрасно об этом знаю. . ."
                                        elif BetsyX.Favorite == "finger":
                                            $ BetsyX.Statup("Love", 90, 5)
                                            $ BetsyX.Statup("Lust", 80, 7)
                                            ch_b "Мне тоже это нравится!"
                                        elif BetsyX.Finger >= 10:
                                            ch_b "Мне тоже очень нравится. . ."
                                        elif not BetsyX.Finger:
                                            $ BetsyX.FaceChange("perplexed")
                                            ch_b "Воу, могу я узнать, кто ласкает твою киску?"
                                        else:
                                            $ BetsyX.FaceChange("bemused")
                                            ch_b "Конечно, это довольно приятно. . ."
                                        $ BetsyX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = BetsyX.FondleB + BetsyX.FondleT + BetsyX.SuckB + BetsyX.Hotdog
                                        $ BetsyX.FaceChange("sly")
                                        if BetsyX.PlayerFav == "fondle":
                                            $ BetsyX.Statup("Lust", 80, 3)
                                            ch_b "Я прекрасно об этом знаю. . ."
                                        elif BetsyX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ BetsyX.Statup("Love", 90, 5)
                                            $ BetsyX.Statup("Lust", 80, 5)
                                            ch_b "Мне очень нравится, когда ты прикасаешься ко мне. . ."
                                        elif Cnt >= 10:
                                            ch_b "Мне тоже это очень нравится. . ."
                                        elif not Cnt:
                                            $ BetsyX.FaceChange("perplexed")
                                            ch_b "Воу, могу я узнать, кого ты лапаешь?"
                                        else:
                                            $ BetsyX.FaceChange("bemused")
                                            ch_b "У тебя очень умелые руки. . ."
                                        $ BetsyX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ BetsyX.FaceChange("sly")
                                        if BetsyX.PlayerFav == "kiss you":
                                            $ BetsyX.Statup("Love", 90, 3)
                                            ch_b "Оу, это очень приятно. . ."
                                        elif BetsyX.Favorite == "kiss you":
                                            $ BetsyX.Statup("Love", 90, 5)
                                            $ BetsyX.Statup("Lust", 80, 5)
                                            ch_b "Хм, ты чудесно целуешься. . ."
                                        elif BetsyX.Kissed >= 10:
                                            ch_b "Мне тоже нравится тебя целовать . . ."
                                        elif not BetsyX.Kissed:
                                            $ BetsyX.FaceChange("perplexed")
                                            ch_b "Воу, могу я узнать, с кем ты целуешься?"
                                        else:
                                            $ BetsyX.FaceChange("bemused")
                                            ch_b "Мне тоже очень нравится тебя целовать. . ."
                                        $ BetsyX.PlayerFav = "kiss you"

                        $ BetsyX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(BetsyX, 800):
                                        $ BetsyX.FaceChange("perplexed")
                                        ch_b ". . ."
                                else:
                                        if BetsyX.SEXP >= 50:
                                            $ BetsyX.FaceChange("sly")
                                            if not Player.Male:
                                                ch_b "Ты должна быть хорошо осведомлена о моих пристрастиях. . ."
                                            else:
                                                ch_b "Ты должен быть хорошо осведомлен о моих пристрастиях. . ."
                                        else:
                                            $ BetsyX.FaceChange("bemused")
                                            $ BetsyX.Eyes = "side"
                                            ch_b "Хмм. . ."


                                        if not BetsyX.Favorite or BetsyX.Favorite == "kiss":
                                                ch_b "Пожалуй, поцелуи. . ."
                                        elif BetsyX.Favorite == "anal":
                                                ch_b "Наверное. . . анальный секс?"
                                        elif BetsyX.Favorite == "lick ass":
                                                ch_b "Наверное. . . когда ты вылизываешь мой анус?"
                                        elif BetsyX.Favorite == "insert ass":
                                                ch_b "Наверное, когда ты ласкаешь. . . мой. . . анус."
                                        elif BetsyX.Favorite == "sex":
                                                ch_b "Пожалуй, мне нравится, когда ты в моей киске."
                                        elif BetsyX.Favorite == "lick pussy":
                                                ch_b "Наверное. . . когда ты вылизываешь мою киску."
                                        elif BetsyX.Favorite == "fondle pussy":
                                                ch_b "Наверное, когда ты. . . ласкаешь мою киску."
                                        elif BetsyX.Favorite == "blow":
                                                ch_b "Наверное, когда я. . . сосу тебе?"
                                        elif BetsyX.Favorite == "cun":
                                                ch_b "Наверное, когда я. . .  лижу тебе?."
                                        elif BetsyX.Favorite == "tit":
                                                ch_b "Возможно, когда я мастурбирую тебя своими сиськами?"
                                        elif BetsyX.Favorite == "foot":
                                                ch_b ". . . работать ножками?"
                                        elif BetsyX.Favorite == "hand":
                                                ch_b "Мне нравится. . . мастурбировать тебе."
                                        elif BetsyX.Favorite == "finger":
                                                ch_b "Мне нравится. . . ласкать твою киску."
                                        elif BetsyX.Favorite == "hotdog":
                                                ch_b "Мне нравится, когда ты трешься о меня."
                                        elif BetsyX.Favorite == "suck breasts":
                                                ch_b "Мне нравится, когда ты. . . сосешь мою грудь."
                                        elif BetsyX.Favorite == "fondle breasts":
                                                ch_b "Мне нравится, когда ты. . . ласкаешь мою грудь."
                                        elif BetsyX.Favorite == "fondle thighs":
                                                ch_b "Мне нравится, когда ты массируешь мои ножки."
                                        else:
                                                ch_b "Дорогуша. . . Я не могу сказать. . ."

                                # End Betsy's favorite things.

                "Не болтай так много во время секса." if "vocal" in BetsyX.Traits:
                        if "setvocal" in BetsyX.DailyActions:
                                $ BetsyX.FaceChange("perplexed")
                                ch_b "Прошу, определись."
                        else:
                            if ApprovalCheck(BetsyX, 1000) and BetsyX.Obed <= BetsyX.Love:
                                $ BetsyX.FaceChange("bemused")
                                $ BetsyX.Statup("Obed", 90, 1)
                                ch_b "Я постараюсь вести себя тихо."
                                $ BetsyX.Traits.remove("vocal")
                            elif ApprovalCheck(BetsyX, 700, "O"):
                                $ BetsyX.FaceChange("sadside")
                                $ BetsyX.Statup("Obed", 90, 1)
                                ch_b ". . ."
                                $ BetsyX.Traits.remove("vocal")
                            elif ApprovalCheck(BetsyX, 600):
                                $ BetsyX.FaceChange("sly")
                                $ BetsyX.Statup("Love", 90, -3)
                                $ BetsyX.Statup("Obed", 50, -1)
                                $ BetsyX.Statup("Inbt", 90, 5)
                                ch_b "Я предпочитаю высказывать то, что думаю."
                            else:
                                $ BetsyX.FaceChange("angry")
                                $ BetsyX.Statup("Love", 90, -5)
                                $ BetsyX.Statup("Obed", 60, -3)
                                $ BetsyX.Statup("Inbt", 90, 10)
                                ch_b "Я бы предпочла не молчать, спасибо."

                            $ BetsyX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in BetsyX.Traits:
                        if "setvocal" in BetsyX.DailyActions:
                                $ BetsyX.FaceChange("perplexed")
                                ch_b "Прошу, определись."
                        else:
                            if ApprovalCheck(BetsyX, 1000) and BetsyX.Obed <= BetsyX.Love:
                                $ BetsyX.FaceChange("sly")
                                $ BetsyX.Statup("Obed", 90, 2)
                                ch_b "Думаю, с этим я смогу справиться. . ."
                                $ BetsyX.Traits.append("vocal")
                            elif ApprovalCheck(BetsyX, 700, "O"):
                                $ BetsyX.FaceChange("sadside")
                                $ BetsyX.Statup("Obed", 90, 2)
                                ch_b "Я постараюсь."
                                $ BetsyX.Traits.append("vocal")
                            elif ApprovalCheck(BetsyX, 600):
                                $ BetsyX.FaceChange("sly")
                                $ BetsyX.Statup("Obed", 90, 3)
                                ch_b "Ох. . . ладно?"
                                $ BetsyX.Traits.append("vocal")
                            else:
                                $ BetsyX.FaceChange("angry")
                                $ BetsyX.Statup("Inbt", 90, 5)
                                ch_b ". . ."

                            $ BetsyX.DailyActions.append("setvocal")
                        # End Betsy Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in BetsyX.Traits:
                        if "initiative" in BetsyX.DailyActions:
                                $ BetsyX.FaceChange("perplexed")
                                ch_b "Прошу, определись."
                        else:
                            if ApprovalCheck(BetsyX, 1200) and BetsyX.Obed <= BetsyX.Love:
                                $ BetsyX.FaceChange("bemused")
                                $ BetsyX.Statup("Obed", 90, 1)
                                ch_b "Ох. . . конечно."
                                $ BetsyX.Traits.append("passive")
                            elif ApprovalCheck(BetsyX, 700, "O"):
                                $ BetsyX.FaceChange("sadside")
                                $ BetsyX.Statup("Obed", 90, 1)
                                ch_b "Я могу. . . попробовать?"
                                $ BetsyX.Traits.append("passive")
                            elif ApprovalCheck(BetsyX, 600):
                                $ BetsyX.FaceChange("sly")
                                $ BetsyX.Statup("Love", 90, -3)
                                $ BetsyX.Statup("Obed", 50, -1)
                                $ BetsyX.Statup("Inbt", 90, 5)
                                ch_b "Боюсь, на это я не могу пойти."
                            else:
                                $ BetsyX.FaceChange("angry")
                                $ BetsyX.Statup("Love", 90, -5)
                                $ BetsyX.Statup("Obed", 60, -3)
                                $ BetsyX.Statup("Inbt", 90, 10)
                                ch_b "Посмотрим."

                            $ BetsyX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in BetsyX.Traits:
                        if "initiative" in BetsyX.DailyActions:
                                $ BetsyX.FaceChange("perplexed")
                                ch_b "Прошу, определись."
                        else:
                            if ApprovalCheck(BetsyX, 1000) and BetsyX.Obed <= BetsyX.Love:
                                $ BetsyX.FaceChange("bemused")
                                $ BetsyX.Statup("Obed", 90, 1)
                                ch_b "Ох, конечно."
                                $ BetsyX.Traits.remove("passive")
                            elif ApprovalCheck(BetsyX, 700, "O"):
                                $ BetsyX.FaceChange("sadside")
                                $ BetsyX.Statup("Obed", 90, 1)
                                ch_b "Это я могу."
                                $ BetsyX.Traits.remove("passive")
                            elif ApprovalCheck(BetsyX, 600):
                                $ BetsyX.FaceChange("sly")
                                $ BetsyX.Statup("Obed", 90, 3)
                                ch_b "Я согдасна."
                                $ BetsyX.Traits.remove("passive")
                            else:
                                $ BetsyX.FaceChange("angry")
                                $ BetsyX.Statup("Inbt", 90, 5)
                                ch_b "Посмотрим."

                            $ BetsyX.DailyActions.append("initiative")

                "О том, как ты накидываешься" if "jumped" in BetsyX.History:
                        call Betsy_Jumped
                "О твоей мастурбации":
                        call NoFap(BetsyX)

                "Всегда вибратор" if "dailyvibe" not in BetsyX.Traits:
                        call Daily_Vibrator(BetsyX)
                "Перестань всегда носить вибратор" if "dailyvibe" in BetsyX.Traits:
                        ch_b "Ладно. . ."
                        $ BetsyX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи анальную пробку" if "dailyplug" not in BetsyX.Traits:
                        call Daily_Plug(BetsyX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in BetsyX.Traits:
                        ch_b "Ладно. . ."
                        $ BetsyX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Неважно" if Line == "Что ты желаешь обсудить?":
                        return
                "На этом все" if Line != "Что ты желаешь обсудить?":
                        return
            if Line == "Что ты желаешь обсудить?":
                $ Line = "Значит, на этом все?"
    return
# End Betsy Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Betsy Chitchat /////////////////// #Work in progress
label Betsy_Chitchat(O=0, Options = ["default","default","default"]): #rkeljsvg
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if BetsyX not in Digits:
                if ApprovalCheck(BetsyX, 500, "L") or ApprovalCheck(BetsyX, 250, "I"):
                    ch_b "Вот мой номер, возможно, он тебе пригодится."
                    $ Digits.append(BetsyX)
                    return
                elif ApprovalCheck(BetsyX, 250, "O"):
                    ch_b "Вот мой номер, возможно, он тебе пригодится."
                    $ Digits.append(BetsyX)
                    return

        if "hungry" not in BetsyX.Traits and (BetsyX.Swallow + BetsyX.Chat[2]) >= 10 and BetsyX.Loc == bg_current:  #She's swallowed a lot
                    call Betsy_Hungry
                    return

        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(BetsyX, 800, "I")):
                    if BetsyX.Loc == bg_current and BetsyX.Thirst >= 30 and "refused" not in BetsyX.DailyActions and "quicksex" not in BetsyX.DailyActions:
                            $ BetsyX.FaceChange("sly",1)
                            ch_b "Итак. . . не хочешь потрахаться?"
                            call Quick_Sex(BetsyX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in BetsyX.DailyActions:
#            $ Options.append("caught")
        if BetsyX.Event[0] and "key" not in BetsyX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in BetsyX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in BetsyX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in BetsyX.DailyActions:
            $ Options.append("corruption")

#        if "Betsy" not in BetsyX.Names:
#            $ Options.append("betsy")

        if BetsyX.Date >= 1 and bg_current != "bg restaurant":
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in BetsyX.DailyActions and "cheek" not in BetsyX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if BetsyX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in BetsyX.DailyActions and (Player.Male or "girltalk" in BetsyX.History):
            #If you've caught Betsy showering today
            $ Options.append("showercaught")
        if "fondle breasts" in BetsyX.DailyActions or "fondle pussy" in BetsyX.DailyActions or "fondle ass" in BetsyX.DailyActions:
            #If you've fondled Betsy today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in BetsyX.Inventory and "256 Shades of Grey" in BetsyX.Inventory and "Avengers Tower Penthouse" in BetsyX.Inventory:
            #If you've given Betsy the books
            if "book" not in BetsyX.Chat:
                $ Options.append("booked")
        if "lace bra" in BetsyX.Inventory or "lace panties" in BetsyX.Inventory:
            #If you've given Betsy the lingerie
            if "lingerie" not in BetsyX.Chat:
                $ Options.append("lingerie")
        if BetsyX.Hand and Player.Male:
            #If Betsy's given a handjob
            $ Options.append("handy")
        if BetsyX.Blow and Player.Male:
            #If Betsy's given a blowjob
            $ Options.append("blow")
        if BetsyX.Swallow:
            #If Betsy's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in BetsyX.DailyActions or "painted" in BetsyX.DailyActions:
            #If Betsy's been facialed
            $ Options.append("facial")
        if BetsyX.Sleep:
            #If Betsy's slept over
            $ Options.append("sleep")
        if (BetsyX.CreamP or BetsyX.CreamA) and Player.Male:
            #If Betsy's been creampied
            $ Options.append("creampie")
        if BetsyX.Sex or BetsyX.Anal:
            #If Betsy's been sexed
            $ Options.append("sexed")
        if BetsyX.Anal:
            #If Betsy's been analed
            $ Options.append("anal")

        if "seenpeen" in BetsyX.History and Player.Male:
            $ Options.append("seenpeen")
        if "topless" in BetsyX.History:
            $ Options.append("topless")
        if "bottomless" in BetsyX.History:
            $ Options.append("bottomless")

#        if not BetsyX.Chat[0] and BetsyX.Sex:
#            $ Options.append("virgin")

#        if (bg_current == "bg betsy" or bg_current == "bg player") and "relationship" not in BetsyX.DailyActions:
#            if "lover" not in BetsyX.Petnames and ApprovalCheck(BetsyX, 900, "L"): # BetsyX.Event[6]
#                $ Options.append("lover?")
#            elif "sir" not in BetsyX.Petnames and ApprovalCheck(BetsyX, 500, "O"): # BetsyX.Event[7]
#                $ Options.append("sir?")
#            elif "daddy" not in BetsyX.Petnames and ApprovalCheck(BetsyX, 750, "L") and ApprovalCheck(BetsyX, 500, "O") and ApprovalCheck(BetsyX, 500, "I"): # BetsyX.Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in BetsyX.Petnames and ApprovalCheck(BetsyX, 900, "O"): # BetsyX.Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in BetsyX.Petnames and ApprovalCheck(BetsyX, 500, "I"): # BetsyX.Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in BetsyX.Petnames and ApprovalCheck(BetsyX, 900, "I"): # BetsyX.Event[10]
#                $ Options.append("fuckbuddy?")


        if not ApprovalCheck(BetsyX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ BetsyX.DailyActions.append("cologne chat")
        $ BetsyX.FaceChange("confused")
        ch_b "(нюх, нюх). . . пахнешь. . . обезьяной. . ."
        $ BetsyX.FaceChange("sexy", 2)
        ch_b ". . . довольно насыщенный мускусный аромат. . ."
    elif Options[0] == "purple":
        $ BetsyX.DailyActions.append("cologne chat")
        $ BetsyX.FaceChange("sly",1)
        ch_b "(нюх, нюх). . . что это за аромат? . ."
        $ BetsyX.FaceChange("normal",0)
        ch_b ". . . я могу тебе как-нибудь помочь?"
    elif Options[0] == "corruption":
        $ BetsyX.DailyActions.append("cologne chat")
        $ BetsyX.FaceChange("confused")
        ch_b "(нюх, нюх). . . боже, какой сильный аромат. . ."
        $ BetsyX.FaceChange("angry")
        ch_b ". . . что ж, у меня вдруг появились довольно мрачные мысли. . ."
        $ BetsyX.FaceChange("sly")

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in BetsyX.Chat:
                    ch_b "Эй! Из-за тебя я чуть не влетела!"
                    if not ApprovalCheck(BetsyX, 500, "I"):
                         ch_b "Но это было довольно возбуждающе. . ."
            else:
                    ch_b "[BetsyX.Petname], у меня чуть не появились проблемы из-за тебя!"
                    if not ApprovalCheck(BetsyX, 500, "I"):
                        ch_b "Полагаю, это означает, что больше не будет никаких \"публичных непристойностей.\" . ."
                    else:
                         ch_b "-Хотя это было довольно возбуждающе. . ."
                    $ BetsyX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if BetsyX.SEXP <= 15:
                if not Player.Male:
                    ch_b "Я дала тебе ключ от комнаты, будь с ним осторожна. . ."
                else:
                    ch_b "Я дала тебе ключ от комнаты, будь с ним осторожен. . ."
            else:
                ch_b "Я дала тебе ключ, но ты не часто заходишь. . ."
            $ BetsyX.Chat.append("key")

    elif Options[0] == "dated":
            #Betsy's response to having gone on a date with the Player.
            ch_b "Мне очень понравился тот вечер, мы должна обязательно повторить."

    elif Options[0] == "kissed":
            #Betsy's response to having been kissed by the Player.
            $ BetsyX.FaceChange("normal",1)
            ch_b "Ты довольно хорошо целуешься, [BetsyX.Petname]."
            menu:
                extend ""
                "Я стараюсь.":
                        $ BetsyX.FaceChange("smile",1)
                        ch_b "Это видно."
                "Ты правда так думаешь?":
                        if not Player.Male:
                            ch_b "Ты точно соответствовала моим стандартам."
                        else:
                            ch_b "Ты точно соответствовал моим стандартам."

    elif Options[0] == "dangerroom":
            #Betsy's response to Player working out in the Danger Room while Betsy is present
            $ BetsyX.FaceChange("sly",1)
            ch_b "Ох, [BetsyX.Petname]. Я видела, как ты тренируешься в Комнате Опасности."
            if not Player.Male:
                ch_b "Мне показалось, что ты наслаждалась тренировкой."
            else:
                ch_b "Мне показалось, что ты наслаждался тренировкой."

    elif Options[0] == "showercaught":
            #Betsy's response to being caught in the shower.
            if "shower" in BetsyX.Chat:
                if not Player.Male:
                    ch_b "Итак, ты снова видела меня в душе. . ."
                else:
                    ch_b "Итак, ты снова видел меня в душе. . ."
            else:
                ch_b "Возможно, я не понимаю ваших обычаев. . ."
                ch_b "Скажи, у вас что, принято просто так заходить к женщинам, когда они моются?"
                $ BetsyX.Chat.append("shower")
                menu:
                    extend ""
                    "Это была чистая случайность! Клянусь!":
                            $ BetsyX.Statup("Love", 50, 5)
                            $ BetsyX.Statup("Love", 90, 2)
                            if ApprovalCheck(BetsyX, 1200):
                                $ BetsyX.FaceChange("sly",1)
                                ch_b "Ох, конечно. . ."
                                ch_b "Но пусть это тебя не останавливает. . ."
                            else:
                                $ BetsyX.FaceChange("smile")
                                ch_b "Ох, конечно. . ."
                    "Только если там ты.":
                            $ BetsyX.Statup("Obed", 40, 5)
                            if ApprovalCheck(BetsyX, 1000) or ApprovalCheck(BetsyX, 700, "L"):
                                    $ BetsyX.Statup("Love", 90, 3)
                                    $ BetsyX.FaceChange("surprised",2,Mouth="normal")
                                    ch_b "Ох, дорогуша. . ."
                                    $ BetsyX.FaceChange("sly",1)
                                    ch_b "Благодарю?"
                            else:
                                    $ BetsyX.Statup("Love", 70, -5)
                                    $ BetsyX.FaceChange("angry")
                                    ch_b "Мне стало тревожнее от твоих слов. . ."
                    "Я заглянула умышленно. Но я ни о чем не жалею." if not Player.Male:
                            if ApprovalCheck(BetsyX, 1200):
                                    $ BetsyX.Statup("Love", 90, 3)
                                    $ BetsyX.Statup("Obed", 70, 10)
                                    $ BetsyX.Statup("Inbt", 50, 5)
                                    $ BetsyX.FaceChange("sly",1)
                                    ch_b "Пожалуй, я могу с этим смириться."
                            elif ApprovalCheck(BetsyX, 800):
                                    $ BetsyX.Statup("Obed", 60, 5)
                                    $ BetsyX.Statup("Inbt", 50, 5)
                                    $ BetsyX.FaceChange("perplexed",2)
                                    ch_b "Что ж. . . хорошо. . ."
                                    $ BetsyX.Blush = 1
                            else:
                                    $ BetsyX.Statup("Love", 50, -10)
                                    $ BetsyX.Statup("Love", 80, -10)
                                    $ BetsyX.Statup("Obed", 50, 10)
                                    $ BetsyX.FaceChange("angry")
                                    ch_b "Мне не нравится твой ответ. . ."
                    "Я заглянул умышленно. Но я ни о чем не жалею." if Player.Male:
                            if ApprovalCheck(BetsyX, 1200):
                                    $ BetsyX.Statup("Love", 90, 3)
                                    $ BetsyX.Statup("Obed", 70, 10)
                                    $ BetsyX.Statup("Inbt", 50, 5)
                                    $ BetsyX.FaceChange("sly",1)
                                    ch_b "Пожалуй, я могу с этим смириться."
                            elif ApprovalCheck(BetsyX, 800):
                                    $ BetsyX.Statup("Obed", 60, 5)
                                    $ BetsyX.Statup("Inbt", 50, 5)
                                    $ BetsyX.FaceChange("perplexed",2)
                                    ch_b "Что ж. . . хорошо. . ."
                                    $ BetsyX.Blush = 1
                            else:
                                    $ BetsyX.Statup("Love", 50, -10)
                                    $ BetsyX.Statup("Love", 80, -10)
                                    $ BetsyX.Statup("Obed", 50, 10)
                                    $ BetsyX.FaceChange("angry")
                                    ch_b "Мне не нравится твой ответ. . ."

    elif Options[0] == "fondled":
            #Betsy's response to being felt up.
            if BetsyX.FondleB + BetsyX.FondleP + BetsyX.FondleA >= 15:
                ch_b "Время от времени мне не помешал бы дружеский массаж. . ."
            else:
                ch_b "Я была бы благодарна, если бы тебе снова захотелось меня потрогать."

    elif Options[0] == "booked":
            #Betsy's response after a Player gives her the books from the shop.
            if not Player.Male:
                ch_b "Я прочитала те книги, которые ты мне предложила. . ."
            else:
                ch_b "Я прочитала те книги, которые ты мне предложил. . ."
            menu:
                extend ""
                "Да? И как тебе?":
                        $ BetsyX.FaceChange("sly",2)
                        ch_b "Они, безусловно, очень интересные. . ."
                "Хорошо. Пожалуй, ты могла бы чему-нибудь из них научиться.":
                        $ BetsyX.Statup("Love", 90, -3)
                        $ BetsyX.Statup("Obed", 70, 5)
                        $ BetsyX.Statup("Inbt", 50, 5)
                        $ BetsyX.FaceChange("angry")
                        ch_b "Ты, видимо, меня недооцениваешь."
            $ BetsyX.Blush = 1
            $ BetsyX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Betsy's response to being given lingerie.
            $ BetsyX.FaceChange("sly",2)
            if not Player.Male:
                ch_b "Мне очень нравится нижнее белье, которое ты мне купила."
            else:
                ch_b "Мне очень нравится нижнее белье, которое ты мне купил."
            ch_b "Оно очень милое. . ."
            $ BetsyX.Blush = 1
            $ BetsyX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Betsy's response after giving the Player a handjob.
            $ BetsyX.FaceChange("sly",1)
            ch_b "Как я понимаю, тебе очень понравилась мастурбация в моем исполнении. . ."
            ch_b "Очень надеюсь, что ты ты будешь просить ее почаще. . ."

    elif Options[0] == "blow":
            if "blow" not in BetsyX.Chat:
                    #Betsy's response after giving the Player a blowjob.
                    $ BetsyX.FaceChange("sly",2)
                    ch_b "Помнишь, как-то я сделала тебе минет? . ."
                    ch_b "Надеюсь, он соответствовал твоим стандартам. . ."
                    menu:
                        extend ""
                        "Ты была великолепна.":
                                    $ BetsyX.Statup("Love", 90, 5)
                                    $ BetsyX.Statup("Inbt", 60, 10)
                                    $ BetsyX.FaceChange("surprised",2)
                                    ch_b "Ох!"
                                    $ BetsyX.FaceChange("sly",1,Eyes="side")
                                    ch_b "Ох, замечательно. . ."
                                    $ BetsyX.FaceChange("sexy",1)
                                    ch_b "Если хочешь, можем повторить. . ."
                        "Честно? Все было хорошо. . . но, думаю, тебе не помешает еще немного попрактиковаться.":
                                if ApprovalCheck(BetsyX, 300, "I") or not ApprovalCheck(BetsyX, 800):
                                    $ BetsyX.Statup("Love", 90, -5)
                                    $ BetsyX.Statup("Obed", 60, 10)
                                    $ BetsyX.Statup("Inbt", 50, 10)
                                    $ BetsyX.FaceChange("perplexed",1)
                                    ch_b "Я. . . буду больше практиковаться. . ."
                                else:
                                    $ BetsyX.Statup("Obed", 70, 15)
                                    $ BetsyX.Statup("Inbt", 50, 5)
                                    $ BetsyX.FaceChange("sexy",1)
                                    ch_b "Хмммм. . . что ж, возможно, у меня нет такого опыта, как у некоторых дамочек. . ."
                        "Угу, если бы мне нравились стремные звуки и шкрябанье зубов по члену, но это далеко не так.":
                                    $ BetsyX.Statup("Love", 90, -10)
                                    $ BetsyX.Statup("Obed", 60, 10)
                                    $ BetsyX.FaceChange("angry",2)
                                    ch_b "Я. . . постараюсь исправиться. . ."
                    $ BetsyX.Blush = 1
                    $ BetsyX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["Должна отметить, у твоего члена очень приятный вкус.",
                            "В прошлый раз я чуть не вывихнула челюсть.",
                            "Как-нибудь я могла бы сделать тебе еще минет.",
                            "Хммм. . . [Стучит языком по внутренней стороне щеки.]"])
                    ch_b "[Line]"

    elif Options[0] == "swallowed":
            #Betsy's response after swallowing the Player's cum.
            if "swallow" in BetsyX.Chat:
                $ BetsyX.FaceChange("sly",1)
                if not Player.Male:
                    ch_b "Мне интересно, могу я еще получить твоих соков?"
                else:
                    ch_b "Мне интересно, могу я еще получить твоей спермы?"
            else:
                if not Player.Male:
                    ch_b "Ты знаешь, что твои соки имеют необычный вкус?"
                    $ BetsyX.FaceChange("normal",1)
                    ch_b "Обычно они бывают не такие. . ."
                    $ BetsyX.FaceChange("sly",1)
                    ch_b ". . .вкусные. . ."
                else:
                    ch_b "Ты знаешь, что твоя сперма имеет необычный вкус?"
                    $ BetsyX.FaceChange("normal",1)
                    ch_b "Обычно она бывает не такая. . ."
                    $ BetsyX.FaceChange("sly",1)
                    ch_b ". . .вкусная. . ."
                $ BetsyX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Betsy's response after taking a facial from the Player.
            ch_b "Я понимаю, что это довольно необычная позиция. . ."
            $ BetsyX.FaceChange("sexy",2)
            if not Player.Male:
                ch_b "Но я нахожу, что мне очень нравится ощущать твои соки на своем лице."
            else:
                ch_b "Но я нахожу, что мне очень нравится ощущать твою сперму на своем лице."
            ch_b ". . ."
            ch_b "Я подумала, что тебе, возможно, будет интересно это узнать. . ."
            $ BetsyX.Blush = 1

    elif Options[0] == "sleepover":
            #Betsy's response after sleeping with the Player.
            ch_b "Мне очень понравилась та ночь."
            ch_b "Приятно, когда кто-то теплый делит с тобой постель. . ."

    elif Options[0] == "creampie":
            #Another of Betsy's responses after having sex with the Player.
            "[BetsyX.Name] подходит к вам вплотную и начинает шептать на ухо."
            if not Player.Male:
                ch_b "Я все еще чувствую, словно они. . . стикают по моим бедрам."
            else:
                ch_b "Я все еще чувствую, словно она. . . стикает по моим бедрам."

    elif Options[0] == "sexed":
            #A final response from Betsy after having sex with the Player.
            $ BetsyX.FaceChange("sexy",2,Eyes="side")
            ch_b "Я подумала, что тебе, возможно, будет интересно узнать. . ."
            $ BetsyX.FaceChange("sly",2,Eyes="side")
            ch_b ". . .недавно, когда я. . . доставляла себе удовольствие. . ."
            $ BetsyX.FaceChange("sexy",2)
            ch_b "Я не могла выбросить тебя из головы. . ."
            $ BetsyX.Blush = 1

    elif Options[0] == "anal":
            #Betsy's response after getting anal from the Player.
            $ BetsyX.FaceChange("sly")
            ch_b "У меня не было большого опыта анального секса. . ."
            $ BetsyX.FaceChange("sexy",1)
            ch_b "Теперь я понимаю, чего мне не хватало."

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ BetsyX.FaceChange("sly",1, Eyes="down")
            ch_b "Ох, пожалуй, у меня так и не нашлось времени упомянуть об этом. . ."
            ch_b "У тебя. . . просто. . . чудесный член. . ."
            $ BetsyX.FaceChange("bemused",1)
            $ BetsyX.Statup("Love", 50, 5)
            $ BetsyX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            if not Player.Male:
                ch_b "Мне интересно, ты видела мою грудь."
            else:
                ch_b "Мне интересно, ты видел мою грудь."
            ch_b "И как она тебе?"
            call Girl_First_TMenu
            $ BetsyX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            if not Player.Male:
                ch_b "Мне интересно, когда ты увидела мою. . . киску. . ."
            else:
                ch_b "Мне интересно, когда ты увидел мою. . . киску. . ."
            ch_b "Тебе она понравилась?"
            call Girl_First_BMenu
            $ BetsyX.History.remove("bottomless")

#    elif Options[0] == "boyfriend?":
#        call Betsy_BF
#    elif Options[0] == "lover?":
#        call Betsy_Love
#    elif Options[0] == "sir?":
#        call Betsy_Sub
#    elif Options[0] == "master?":
#        call Betsy_Master
#    elif Options[0] == "sexfriend?":
#        call Betsy_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Betsy_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Betsy_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        if not Player.Male:
            $ Line = renpy.random.choice(["Отойди от меня.",
                    "Я не хочу, чтобы ты была рядом.",
                    "Я хочу уйти побыстрее отсюда.",
                    "Уйди.",
                    "Прочь."])
        else:
            $ Line = renpy.random.choice(["Отойди от меня.",
                    "Я не хочу, чтобы ты был рядом.",
                    "Я хочу уйти побыстрее отсюда.",
                    "Уйди.",
                    "Прочь."])
        ch_b "[Line]"

    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 21)
            if D20 == 1:
                    ch_b "Сегодня просто восхитительная погода, я в восторге."
            elif D20 == 2:
                    $ BetsyX.FaceChange("smile")
                    ch_b "Я заметила, что [StormX.Name] и [EmmaX.Name] с удовольствием пьют чай после обеда, когда они не на занятиях."
            elif D20 == 3:
                    $ BetsyX.FaceChange("surprised")
                    ch_b "Что? Ох, извини. Я подслушивала другой разговор."
            elif D20 == 4:
                    $ BetsyX.FaceChange("normal")
                    ch_b "О, [BetsyX.Petname]. Должно быть, я отвлеклась на мимолетную мысль."
            elif D20 == 5:
                    $ BetsyX.FaceChange("smile")
                    ch_b "Мне очень нравится местная кухня."
            elif D20 == 6:
                    $ BetsyX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_b "О, [BetsyX.Petname]. Ты не видела [JubesX.Name_vin]? Мы с ней хотели пройтись по магазинам."
                    else:
                        ch_b "О, [BetsyX.Petname]. Ты не видел [JubesX.Name_vin]? Мы с ней хотели пройтись по магазинам."
            elif D20 == 7:
                    $ BetsyX.FaceChange("normal")
                    ch_b "Я работала над Комнатой Опасности, чтобы сделать голограммы ниндзя более точным."
            elif D20 == 8:
                    $ BetsyX.FaceChange("sad")
                    ch_b "Мне нравится быть здесь, но иногда я скучаю по родному поместью. . ."
            elif D20 == 9:
                    $ BetsyX.FaceChange("smile",2)
                    ch_b "Не знаю, известно ли тебе, но, по-моему, Чарльзу нравится наша мисс Грей!"
                    $ BetsyX.FaceChange("smile",1)
            elif D20 == 10:
                    $ BetsyX.FaceChange("smile")
                    ch_b "Меня воодушевляет мысль, что здесь я могу свободно тренировать свои способности."
            elif D20 == 11:
                    $ BetsyX.FaceChange("smile")
                    ch_b "[LauraX.Name] замечательный спарринг-партнер."
                    ch_b "Она в прекрасной физической форме."
            elif D20 == 12:
                    $ BetsyX.FaceChange("sad")
                    ch_b "Ты, случайно, не можешь подсказать, где можно достать резинку?"
                    menu:
                        extend ""
                        "Нет, извини.":
                                $ BetsyX.FaceChange("sad")
                                ch_b "Ох, жаль."
                                $ BetsyX.FaceChange("surprised",2,Mouth="open")
                                ch_b "Ох, эм. . . я имела в виду стирательную резинку!"
                        "Мы не пользуемся ими здесь.":
                                $ BetsyX.FaceChange("confused")
                                ch_b "Как странно. . ."
                                $ BetsyX.FaceChange("surprised",2,Mouth="open")
                                ch_b "Ох, эм. . . я имела в виду стирательную резинку!"
                        "Стирательную?":
                                $ BetsyX.FaceChange("smile")
                                ch_b "Конечно."
                        ". . .":
                                $ BetsyX.FaceChange("surprised",2,Mouth="open")
                                ch_b "Ох, эм. . . я имела в виду стирательную резинку!"
                    $ BetsyX.FaceChange("smile")
            elif D20 == 13:
                    $ BetsyX.FaceChange("smile")
                    ch_b "Мы с дамами недавно ходили в торговый центр за мороженым!"
            elif D20 == 14:
                    $ BetsyX.FaceChange("sad")
                    ch_b "Мне нравится ходить на миссии, но это ужасно влияет на успеваемость."
            elif D20 == 15:
                    $ BetsyX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_b "Ты когда-нибудь общалась с британской командой?"
                        ch_b "Если ты не знала, ими управляет мой брат."
                    else:
                        ch_b "Ты когда-нибудь общался с британской командой?"
                        ch_b "Если ты не знал, ими управляет мой брат."
            elif D20 == 16:
                    $ BetsyX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_b "Ты когда-нибудь бывала в Лондоне? Там гораздо спокойнее, чем здесь, в Штатах."
                    else:
                        ch_b "Ты когда-нибудь бывал в Лондоне? Там гораздо спокойнее, чем здесь, в Штатах."
            elif D20 == 17:
                    $ BetsyX.FaceChange("perplexed")
                    ch_b "Боюсь, у меня только что возникли разногласия с Логаном по поводу природы кинематографа о ниндзя."
            elif D20 == 18:
                    $ BetsyX.FaceChange("smile")
                    ch_b "Никому не рассказывай, но я звидела, как Логан обнюхивал шкафчик мисс Грей. . ."
            elif D20 == 19:
                    $ BetsyX.FaceChange("confused")
                    ch_b "О боже, пахнет. . . тортом?!"
            elif D20 == 20:
                    $ BetsyX.FaceChange("smile")
                    ch_b "Мне очень нравятся приятные беседы. . ."
            else:
                    $ BetsyX.FaceChange("smile")
                    ch_b "Я рада видеть тебя в таком хорошем настроении."

    $ Line = 0
    return

# start Betsy_Names//////////////////////////////////////////////////////////
label Betsy_Names:    #rkeljsvgb
    menu:
        ch_b "Ох? Как бы тебе хотелось, чтобы я тебя звала?"
        "Зови по инициалам.":
            $ BetsyX.Petname = Player.Name[:1]  #fix test this
            $ BetsyX.Petname_rod = Player.Name[:1]
            $ BetsyX.Petname_dat = Player.Name[:1]
            $ BetsyX.Petname_vin = Player.Name[:1]
            $ BetsyX.Petname_tvo = Player.Name[:1]
            $ BetsyX.Petname_pre = Player.Name[:1]
            ch_b "Конечно, [BetsyX.Petname]."
        "Зови меня по имени.":
            $ BetsyX.Petname = Player.Name
            $ BetsyX.Petname_rod = Player.Name_rod
            $ BetsyX.Petname_dat = Player.Name_dat
            $ BetsyX.Petname_vin = Player.Name_vin
            $ BetsyX.Petname_tvo = Player.Name_tvo
            $ BetsyX.Petname_pre = Player.Name_pre
            ch_b "Конечно, [BetsyX.Petname]."
        "Зови меня \"моя девушка\"." if "boyfriend" in BetsyX.Petnames and not Player.Male:
            $ BetsyX.Petname = "моя девушка"
            $ BetsyX.Petname_rod = "моей девушки"
            $ BetsyX.Petname_dat = "моей девушке"
            $ BetsyX.Petname_vin = "мою девушку"
            $ BetsyX.Petname_tvo = "моей девушкой"
            $ BetsyX.Petname_pre = "моей девушке"
            ch_b "Чудесно, [BetsyX.Petname]."
        "Зови меня \"мой парень\"." if "boyfriend" in BetsyX.Petnames and Player.Male:
            $ BetsyX.Petname = "мой парень"
            $ BetsyX.Petname_rod = "моего парня"
            $ BetsyX.Petname_dat = "моему парню"
            $ BetsyX.Petname_vin = "моего парня"
            $ BetsyX.Petname_tvo = "моим парнем"
            $ BetsyX.Petname_pre = "моем парне"
            ch_b "Чудесно, [BetsyX.Petname]."
        "Зови меня \"любимая\"." if "lover" in BetsyX.Petnames and not Player.Male:
            $ BetsyX.Petname = "любимая"
            $ BetsyX.Petname_rod = "любимой"
            $ BetsyX.Petname_dat = "любимой"
            $ BetsyX.Petname_vin = "любимую"
            $ BetsyX.Petname_tvo = "любимой"
            $ BetsyX.Petname_pre = "любимой"
            ch_b "Ооох, конечно, [BetsyX.Petname]."
        "Зови меня \"любимый\"." if "lover" in BetsyX.Petnames and Player.Male:
            $ BetsyX.Petname = "любимый"
            $ BetsyX.Petname_rod = "любимого"
            $ BetsyX.Petname_dat = "любимому"
            $ BetsyX.Petname_vin = "любимого"
            $ BetsyX.Petname_tvo = "любимым"
            $ BetsyX.Petname_pre = "любимом"
            ch_b "Ооох, конечно, [BetsyX.Petname]."
        "Зови меня \"госпожа\"." if "sir" in BetsyX.Petnames and not Player.Male:
            $ BetsyX.Petname = "госпожа"
            $ BetsyX.Petname_rod = "госпожи"
            $ BetsyX.Petname_dat = "госпоже"
            $ BetsyX.Petname_vin = "госпожу"
            $ BetsyX.Petname_tvo = "госпожой"
            $ BetsyX.Petname_pre = "госпоже"
            ch_b "Конечно, [BetsyX.Petname]."
        "Зови меня \"господин\"." if "sir" in BetsyX.Petnames and Player.Male:
            $ BetsyX.Petname = "господин"
            $ BetsyX.Petname_rod = "господина"
            $ BetsyX.Petname_dat = "господину"
            $ BetsyX.Petname_vin = "господина"
            $ BetsyX.Petname_tvo = "господином"
            $ BetsyX.Petname_pre = "господине"
            ch_b "Конечно, [BetsyX.Petname]."
        "Зови меня \"хозяйка\"." if "master" in BetsyX.Petnames and not Player.Male:
            $ BetsyX.Petname = "хозяйка"
            $ BetsyX.Petname_rod = "хозяйки"
            $ BetsyX.Petname_dat = "хозяйке"
            $ BetsyX.Petname_vin = "хозяйку"
            $ BetsyX.Petname_tvo = "хозяйкой"
            $ BetsyX.Petname_pre = "хозяйке"
            ch_b "Как пожелаешь, [BetsyX.Petname]."
        "Зови меня \"хозяин\"." if "master" in BetsyX.Petnames and Player.Male:
            $ BetsyX.Petname = "хозяин"
            $ BetsyX.Petname_rod = "хозяина"
            $ BetsyX.Petname_dat = "хозяину"
            $ BetsyX.Petname_vin = "хозяина"
            $ BetsyX.Petname_tvo = "хозяином"
            $ BetsyX.Petname_pre = "хозяине"
            ch_b "Как пожелаешь, [BetsyX.Petname]."
        "Зови меня \"любовница\"." if "sex friend" in BetsyX.Petnames and not Player.Male:
            $ BetsyX.Petname = "любовница"
            $ BetsyX.Petname_rod = "любовницы"
            $ BetsyX.Petname_dat = "любовнице"
            $ BetsyX.Petname_vin = "любовницу"
            $ BetsyX.Petname_tvo = "любовницей"
            $ BetsyX.Petname_pre = "любовнице"
            ch_b "Хах, ладно, [BetsyX.Petname]."
        "Зови меня \"любовник\"." if "sex friend" in BetsyX.Petnames and Player.Male:
            $ BetsyX.Petname = "любовник"
            $ BetsyX.Petname_rod = "любовника"
            $ BetsyX.Petname_dat = "любовнику"
            $ BetsyX.Petname_vin = "любовника"
            $ BetsyX.Petname_tvo = "любовником"
            $ BetsyX.Petname_pre = "любовнике"
            ch_b "Хах, ладно, [BetsyX.Petname]."
        "Зови меня \"секс-партнерша\"." if "fuck buddy" in BetsyX.Petnames and not Player.Male:
            $ BetsyX.Petname = "секс-партнерша"
            $ BetsyX.Petname_rod = "секс-партнерши"
            $ BetsyX.Petname_dat = "секс-партнерше"
            $ BetsyX.Petname_vin = "секс-партнершу"
            $ BetsyX.Petname_tvo = "секс-партнершей"
            $ BetsyX.Petname_pre = "секс-партнерше"
            ch_b "О, довольно непристойно. . . [BetsyX.Petname]."
        "Зови меня \"секс-партнер\"." if "fuck buddy" in BetsyX.Petnames and Player.Male:
            $ BetsyX.Petname = "секс-партнер"
            $ BetsyX.Petname_rod = "секс-партнера"
            $ BetsyX.Petname_dat = "секс-партнеру"
            $ BetsyX.Petname_vin = "секс-партнера"
            $ BetsyX.Petname_tvo = "секс-партнером"
            $ BetsyX.Petname_pre = "секс-партнере"
            ch_b "О, довольно непристойно. . . [BetsyX.Petname]."
        "Зови меня \"мамочка\"." if "daddy" in BetsyX.Petnames and not Player.Male:
            $ BetsyX.Petname = "мамочка"
            $ BetsyX.Petname_rod = "мамочки"
            $ BetsyX.Petname_dat = "мамочке"
            $ BetsyX.Petname_vin = "мамочку"
            $ BetsyX.Petname_tvo = "мамочкой"
            $ BetsyX.Petname_pre = "мамочке"
            ch_b "Ох! Конечно, [BetsyX.Petname]."
        "Зови меня \"папочка\"." if "daddy" in BetsyX.Petnames and Player.Male:
            $ BetsyX.Petname = "папочка"
            $ BetsyX.Petname_rod = "папочки"
            $ BetsyX.Petname_dat = "папочке"
            $ BetsyX.Petname_vin = "папочку"
            $ BetsyX.Petname_tvo = "папочкой"
            $ BetsyX.Petname_pre = "папочке"
            ch_b "Ох! Конечно, [BetsyX.Petname]."
        "\"Товарищ\" в самый раз.":
            $ BetsyX.Petname = "товарищ"
            $ BetsyX.Petname_rod = "товарища"
            $ BetsyX.Petname_dat = "товарищу"
            $ BetsyX.Petname_vin = "товарища"
            $ BetsyX.Petname_tvo = "товарищем"
            $ BetsyX.Petname_pre = "товарище"
            if not Player.Male:
                ch_b "Ты права, товарищ."
            else:
                ch_b "Ты прав, товарищ."
        "\"Любовь моя\" в самый раз.":
            $ BetsyX.Petname = "любовь моя"
            $ BetsyX.Petname_rod = "любви моей"
            $ BetsyX.Petname_dat = "любви моей"
            $ BetsyX.Petname_vin = "любовь мою"
            $ BetsyX.Petname_tvo = "любовью моей"
            $ BetsyX.Petname_pre = "любви моей"
            ch_b "Очень мило, любовь моя."
        "\"Кореш\" в самый раз." if not Player.Male:
            $ BetsyX.Petname = "кореш"
            $ BetsyX.Petname_rod = "кореша"
            $ BetsyX.Petname_dat = "корешу"
            $ BetsyX.Petname_vin = "кореша"
            $ BetsyX.Petname_tvo = "корешем"
            $ BetsyX.Petname_pre = "кореше"
            ch_b "Верно, кореш."
        "\"Подруга\" в самый раз." if Player.Male:
            $ BetsyX.Petname = "подруга"
            $ BetsyX.Petname_rod = "подруги"
            $ BetsyX.Petname_dat = "подруге"
            $ BetsyX.Petname_vin = "подругу"
            $ BetsyX.Petname_tvo = "подругой"
            $ BetsyX.Petname_pre = "подруге"
            ch_b "Верно, подруга."
        "\"Дорогуша\" в самый раз.":
            $ BetsyX.Petname = "дорогуша"
            $ BetsyX.Petname_rod = "дорогуши"
            $ BetsyX.Petname_dat = "дорогуше"
            $ BetsyX.Petname_vin = "дорогушу"
            $ BetsyX.Petname_tvo = "дорогушей"
            $ BetsyX.Petname_pre = "дорогуше"
            ch_b "Конечно, дорогуша."
        "\"Милочка\" в самый раз." if not Player.Male:
            $ BetsyX.Petname = "милочка"
            $ BetsyX.Petname_rod = "милочки"
            $ BetsyX.Petname_dat = "милочке"
            $ BetsyX.Petname_vin = "милочку"
            $ BetsyX.Petname_tvo = "милочкой"
            $ BetsyX.Petname_pre = "милочке"
            ch_b "Конечно, милочка."
        "\"Милок\" в самый раз." if Player.Male:
            $ BetsyX.Petname = "милок"
            $ BetsyX.Petname_rod = "милка"
            $ BetsyX.Petname_dat = "милку"
            $ BetsyX.Petname_vin = "милка"
            $ BetsyX.Petname_tvo = "милком"
            $ BetsyX.Petname_pre = "милке"
            ch_b "Конечно, милок."
        "Неважно.":
            return
    return
# end Betsy_Names//////////////////////////////////////////////////////////

label Betsy_Pet: #rkeljsvgb
    while 1:
        menu:
            extend ""
            "Обходительно":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "Бетси.":
                        $ BetsyX.Pet = "Бетси"
                        $ BetsyX.Pet_rod = "Бетси"
                        $ BetsyX.Pet_dat = "Бетси"
                        $ BetsyX.Pet_vin = "Бетси"
                        $ BetsyX.Pet_tvo = "Бетси"
                        $ BetsyX.Pet_pre = "Бетси"
                        ch_b "Не вижу причин отказываться, [BetsyX.Petname]."

                    "Псайлок.":
                        $ BetsyX.Pet = "Псайлок"
                        $ BetsyX.Pet_rod = "Псайлок"
                        $ BetsyX.Pet_dat = "Псайлок"
                        $ BetsyX.Pet_vin = "Псайлок"
                        $ BetsyX.Pet_tvo = "Псайлок"
                        $ BetsyX.Pet_pre = "Псайлок"
                        if ApprovalCheck(BetsyX, 700, "L") and not ApprovalCheck(BetsyX, 500, "O"):
                                ch_b "Это довольно необычное прозвище, [BetsyX.Petname]."
                        else:
                                ch_b "Не вижу причин отказываться, [BetsyX.Petname]."

                    "\"моя девушка\".":
                        if "boyfriend" in BetsyX.Petnames:
                            $ BetsyX.Pet = "моя девушка"
                            $ BetsyX.Pet_rod = "моей девушки"
                            $ BetsyX.Pet_dat = "моей девушке"
                            $ BetsyX.Pet_vin = "мою девушку"
                            $ BetsyX.Pet_tvo = "моей девушкой"
                            $ BetsyX.Pet_pre = "моей девушке"
                            $ BetsyX.FaceChange("sexy", 1)
                            ch_b "Конечно, я же в самом деле твоя девушка, [BetsyX.Petname]."
                        else:
                            $ BetsyX.FaceChange("angry")
                            ch_b "Это слишком, [BetsyX.Petname]."

                    "\"детка\".":
                        if "boyfriend" in BetsyX.Petnames or ApprovalCheck(BetsyX, 700, "L"):
                            $ BetsyX.Pet = "детка"
                            $ BetsyX.Pet_rod = "детки"
                            $ BetsyX.Pet_dat = "детке"
                            $ BetsyX.Pet_vin = "детку"
                            $ BetsyX.Pet_tvo = "деткой"
                            $ BetsyX.Pet_pre = "детке"
                            $ BetsyX.FaceChange("sexy", 1)
                            ch_b "Я твоя \"детка,\" как восхитительно."
                        else:
                            $ BetsyX.FaceChange("angry")
                            ch_b "Мне кажется, это слишком, [BetsyX.Petname]."

                    "\"крошка\".":
                        if "boyfriend" in BetsyX.Petnames or ApprovalCheck(BetsyX, 600, "L"):
                            $ BetsyX.Pet = "крошка"
                            $ BetsyX.Pet_rod = "крошки"
                            $ BetsyX.Pet_dat = "крошке"
                            $ BetsyX.Pet_vin = "крошку"
                            $ BetsyX.Pet_tvo = "крошкой"
                            $ BetsyX.Pet_pre = "крошке"
                            $ BetsyX.FaceChange("sexy", 1)
                            ch_b "Я твоя \"крошка,\" как восхитительно."
                        else:
                            $ BetsyX.FaceChange("angry")
                            ch_b "Мне кажется, это слишком, [BetsyX.Petname]."

                    "\"малышка\".":
                        if "boyfriend" in BetsyX.Petnames or ApprovalCheck(BetsyX, 500, "L"):
                            $ BetsyX.Pet = "малышка"
                            $ BetsyX.Pet_rod = "малышки"
                            $ BetsyX.Pet_dat = "малышке"
                            $ BetsyX.Pet_vin = "малышку"
                            $ BetsyX.Pet_tvo = "малышкой"
                            $ BetsyX.Pet_pre = "малышке"
                            $ BetsyX.FaceChange("sexy", 1)
                            ch_b "Восхитительно, [BetsyX.Petname]."
                        else:
                            $ BetsyX.FaceChange("angry")
                            ch_b "Мне кажется, это слишком, [BetsyX.Petname]."


                    "\"дорогая\".":
                        if "boyfriend" in BetsyX.Petnames or ApprovalCheck(BetsyX, 600, "L"):
                            $ BetsyX.Pet = "дорогая"
                            $ BetsyX.Pet_rod = "дорогой"
                            $ BetsyX.Pet_dat = "дорогой"
                            $ BetsyX.Pet_vin = "дорогую"
                            $ BetsyX.Pet_tvo = "дорогой"
                            $ BetsyX.Pet_pre = "дорогой"
                            ch_b "Как мило, [BetsyX.Petname]."
                        else:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Мне кажется, это слишком, [BetsyX.Petname]."

                    "\"секси\".":
                        if "lover" in BetsyX.Petnames or ApprovalCheck(BetsyX, 800):
                            $ BetsyX.Pet = "секси"
                            $ BetsyX.Pet_rod = "секси"
                            $ BetsyX.Pet_dat = "секси"
                            $ BetsyX.Pet_vin = "секси"
                            $ BetsyX.Pet_tvo = "секси"
                            $ BetsyX.Pet_pre = "секси"
                            $ BetsyX.FaceChange("sexy", 1)
                            ch_b "Это так."
                        else:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Мне кажется, это слишком, [BetsyX.Petname]."

                    "\"любимая\".":
                        if "lover" in BetsyX.Petnames or ApprovalCheck(BetsyX, 1200):
                            $ BetsyX.Pet = "любимая"
                            $ BetsyX.Pet_rod = "любимой"
                            $ BetsyX.Pet_dat = "любимой"
                            $ BetsyX.Pet_vin = "любимую"
                            $ BetsyX.Pet_tvo = "любимой"
                            $ BetsyX.Pet_pre = "любимой"
                            $ BetsyX.FaceChange("sexy", 1)
                            ch_b "Конечно."
                        else:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Я так не думаю, [BetsyX.Petname]."

                    "Назад":
                        pass

            "Грубо":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "\"рабыня\".":
                        if "master" in BetsyX.Petnames or ApprovalCheck(BetsyX, 800, "O"):
                            $ BetsyX.Pet = "рабыня"
                            $ BetsyX.Pet_rod = "рабыни"
                            $ BetsyX.Pet_dat = "рабыне"
                            $ BetsyX.Pet_vin = "рабыню"
                            $ BetsyX.Pet_tvo = "рабыней"
                            $ BetsyX.Pet_pre = "рабыне"
                            $ BetsyX.FaceChange("bemused", 1)
                            ch_b "Как пожелаешь, [BetsyX.Petname]."
                        else:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Я не рабыня, [BetsyX.Petname]."

                    "\"питомец\".":
                        if "master" in BetsyX.Petnames or ApprovalCheck(BetsyX, 650, "O"):
                            $ BetsyX.Pet = "питомец"
                            $ BetsyX.Pet_rod = "питомце"
                            $ BetsyX.Pet_dat = "питомцу"
                            $ BetsyX.Pet_vin = "питомца"
                            $ BetsyX.Pet_tvo = "питомцем"
                            $ BetsyX.Pet_pre = "питомце"
                            $ BetsyX.FaceChange("bemused", 1)
                            ch_b "Пожалуй, [BetsyX.Petname]."
                        else:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Я не питомец, [BetsyX.Petname]."

                    "\"шлюха\".":
                        if "sex friend" in BetsyX.Petnames or ApprovalCheck(BetsyX, 900, "OI"):
                            $ BetsyX.Pet = "шлюха"
                            $ BetsyX.Pet_rod = "шлюхи"
                            $ BetsyX.Pet_dat = "шлюхе"
                            $ BetsyX.Pet_vin = "шлюху"
                            $ BetsyX.Pet_tvo = "шлюхой"
                            $ BetsyX.Pet_pre = "шлюхе"
                            $ BetsyX.FaceChange("sexy")
                            ch_b "Возможно. . ."
                        else:
                            $ BetsyX.FaceChange("angry", 1)
                            $ BetsyX.Mouth = "surprised"
                            ch_b "Это было довольно грубо, [BetsyX.Petname]."

                    "\"блядь\".":
                        if "fuckbuddy" in BetsyX.Petnames or ApprovalCheck(BetsyX, 1000, "OI"):
                            $ BetsyX.Pet = "блядь"
                            $ BetsyX.Pet_rod = "бляди"
                            $ BetsyX.Pet_dat = "бляде"
                            $ BetsyX.Pet_vin = "блядь"
                            $ BetsyX.Pet_tvo = "блядью"
                            $ BetsyX.Pet_pre = "бляде"
                            $ BetsyX.FaceChange("sly")
                            ch_b ". . . как любопытно, думаю, мне нравится."
                        else:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Это было очень грубо, [BetsyX.Petname]."

                    "\"сладкогрудая\".":
                        if "sex friend" in BetsyX.Petnames or ApprovalCheck(BetsyX, 1400):
                            $ BetsyX.Pet = "сладкогрудая"
                            $ BetsyX.Pet_rod = "сладкогрудой"
                            $ BetsyX.Pet_dat = "сладкогрудой"
                            $ BetsyX.Pet_vin = "сладкогрудую"
                            $ BetsyX.Pet_tvo = "сладкогрудой"
                            $ BetsyX.Pet_pre = "сладкогрудой"
                            $ BetsyX.FaceChange("sly", 1)
                            ch_b "Хорошо?"
                        else:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Это было довольно грубо, [BetsyX.Petname]."

                    "\"любовница\".":
                        if "sex friend" in BetsyX.Petnames or ApprovalCheck(BetsyX, 600, "I"):
                            $ BetsyX.Pet = "любовница"
                            $ BetsyX.Pet_rod = "любовницы"
                            $ BetsyX.Pet_dat = "любовнице"
                            $ BetsyX.Pet_vin = "любовницу"
                            $ BetsyX.Pet_tvo = "любовницей"
                            $ BetsyX.Pet_pre = "любовнице"
                            $ BetsyX.FaceChange("sly")
                            ch_b "Да?"
                        else:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Это было довольно грубо, [BetsyX.Petname]."

                    "\"секс-партнерша\".":
                        if "fuckbuddy" in BetsyX.Petnames or ApprovalCheck(BetsyX, 700, "I"):
                            $ BetsyX.Pet = "секс-партнерша"
                            $ BetsyX.Pet_rod = "секс-партнерши"
                            $ BetsyX.Pet_dat = "секс-партнерше"
                            $ BetsyX.Pet_vin = "секс-партнершу"
                            $ BetsyX.Pet_tvo = "секс-партнершей"
                            $ BetsyX.Pet_pre = "секс-партнерше"
                            $ BetsyX.FaceChange("sly")
                            ch_b "Хорошо?"
                        else:
                            $ BetsyX.FaceChange("angry", 1)
                            $ BetsyX.Mouth = "surprised"
                            ch_b "Это было довольно грубо, [BetsyX.Petname]."

                    "\"доченька\".":
                        if "daddy" in BetsyX.Petnames or ApprovalCheck(BetsyX, 1200):
                            $ BetsyX.Pet = "доченька"
                            $ BetsyX.Pet_rod = "доченьки"
                            $ BetsyX.Pet_dat = "доченьке"
                            $ BetsyX.Pet_vin = "доченьку"
                            $ BetsyX.Pet_tvo = "доченькой"
                            $ BetsyX.Pet_pre = "доченьке"
                            $ BetsyX.FaceChange("smile", 1)
                            ch_b "Очаровательно."
                        else:
                            $ BetsyX.FaceChange("angry", 1)
                            ch_b "Это очень странно."

                    "Назад":
                        pass

            "Неважно.":
                return
    return

#label Betsy_Namecheck(BetsyX.Pet = BetsyX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname


# start Betsy_Rename//////////////////////////////////////////////////////////
label Betsy_Rename:  #rkeljsvgb
        #Sets alternate names from Betsy
        $ BetsyX.Mouth = "smile"
        ch_b "Да?"
        menu:
            extend ""
            "Думаю, \"Бетси\" красивое имя." if BetsyX.Name != "Бетси" and "Betsy" in BetsyX.Names:
                    $ BetsyX.Name = "Бетси"
                    $ BetsyX.Name_rod = "Бетси"
                    $ BetsyX.Name_dat = "Бетси"
                    $ BetsyX.Name_vin = "Бетси"
                    $ BetsyX.Name_tvo = "Бетси"
                    $ BetsyX.Name_pre = "Бетси"
                    ch_b "Мне оно тоже нравится."
            "Думаю, \"Элизабет\" звучит хорошо." if BetsyX.Name != "Элизабет" and "Elizabeth" in BetsyX.Names:
                    if not ApprovalCheck(BetsyX, 500):
                            $ BetsyX.FaceChange("confused", 1)
                            ch_b "Мне больше нравится, когда меня зовут [BetsyX.Name]."
                    else:
                            if "namechange" not in BetsyX.DailyActions:
                                    $ BetsyX.Statup("Love", 70, 2)
                                    $ BetsyX.Statup("Obed", 70, 5)
                            $ BetsyX.Name_rod = "Элизабет"
                            $ BetsyX.Name_dat = "Элизабет"
                            $ BetsyX.Name_vin = "Элизабет"
                            $ BetsyX.Name_tvo = "Элизабет"
                            $ BetsyX.Name_pre = "Элизабет"
                            $ BetsyX.Name = "Элизабет"
                            $ BetsyX.FaceChange("sly", 1)
                            ch_b "Пожалуй, соглашусь. . ."
            "Неважно.":
                    pass
        $ BetsyX.AddWord(1,0,"namechange")
        return
# end Betsy_Rename//////////////////////////////////////////////////////////


# start Betsy_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Betsy_Personality(Cnt = 0):   #rkeljsvgb
    if not BetsyX.Chat[4] or Cnt:
        "Поскольку у вас все хорошо получается в одной области, вы можете убедить Эмму сосредоточиться на любой другой."
        "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
        "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
    menu:
        ch_b "Да?"
        "Больше Послушания. [[Любовь в Послушание]" if BetsyX.Love > 900:
            ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
            ch_b "Ты хочешь, чтобы я была более послушной? Я попробую."
            $ BetsyX.Chat[4] = 1
        "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if BetsyX.Love > 900:
            ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
            ch_b "Ты хочешь, чтобы я была более раскрепощенной? Я попробую."
            $ BetsyX.Chat[4] = 2

        "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if BetsyX.Obed > 900:
            ch_p "Я хочу, чтобы ты была более раскрепощенной."
            ch_b "Ты хочешь, чтобы я была более раскрепощенной? Я попробую."
            $ BetsyX.Chat[4] = 3
        "Больше Любви. [[Повиновение в Любовь]" if BetsyX.Obed > 900:
            ch_p "Я хочу, чтобы ты училась любить меня."
            ch_b "Ты не находишь меня достаточно заботливой? Я попробую."
            $ BetsyX.Chat[4] = 4

        "Больше Повиновения. [[Раскрепощенность в Повиновение]" if BetsyX.Inbt > 900:
            ch_p "Я знаю, что нам и так весело, но разве ты не можешь иногда слушаться меня?"
            ch_b "Ты хочешь, чтобы я была более послушной? Звучит весело."
            $ BetsyX.Chat[4] = 5

        "Больше Любви. [[Раскрепощенность в Любовь]" if BetsyX.Inbt > 900:
            ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
            ch_b "Ты не находишь меня достаточно заботливой? Надеюсь, я смогу стать лучше."
            $ BetsyX.Chat[4] = 6

        "Просто делай то, что тебе нравится. . .[[Сбросить]" if BetsyX.Chat[4]:
            ch_p "Помнишь, что мы обсуждали? Забудь."
            ch_b "Ох. . . хорошо."
            $ BetsyX.Chat[4] = 0
        "Повторить правила":
            call Betsy_Personality(1)
            return
        "Неважно.":
            return
    return
# end Betsy_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Betsy_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Betsy_Summon(Tempmod=Tempmod): #rkeljsvgb
    $ BetsyX.OutfitChange()
    if "no summon" in BetsyX.RecentActions:
                if "no summon" in BetsyX.RecentActions:
                    ch_b "Перестань спрашивать!"
                    $ BetsyX.AddWord(1,"angry",0,0,0)
                elif Current_Time == "Night":
                    ch_b "Я же сказала тебе, уже поздно. Спокойной ночи."
                else:
                    ch_b "Я же сказала тебе, я занята."
                $ BetsyX.RecentActions.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if BetsyX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif BetsyX.Loc == "bg dangerroom":
        $ Tempmod = -10
    elif BetsyX.Loc == "bg showerroom":
        $ Tempmod = -30

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"
    if Time_Count >= 3: #night time
                if ApprovalCheck(BetsyX, 500, "L") or ApprovalCheck(BetsyX, 400, "O"):
                        #It's night time but she likes you.
                        ch_b "Пожалуй, ты можешь навестить меня."
                        $ BetsyX.Loc = bg_current
                        call Taboo_Level
                        call Set_The_Scene
                else:
                        #It's night time and she isn't into you
                        ch_b "Боюсь, это довольно поздно."
                        $ BetsyX.RecentActions.append("no summon")
                return
    elif "les" in BetsyX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(BetsyX, 2000):
                    if not Player.Male:
                        ch_b "Ко мне тут кое-кто зашел, но мы были бы не против, если бы ты присоединилась к нам. . ."
                    else:
                        ch_b "Ко мне тут кое-кто зашел, но мы были бы не против, если бы ты присоединился к нам. . ."
                    menu:
                        extend ""
                        "Конечно.":
                            $ Line = "go to"
                        "Нет, спасибо.":
                            ch_b "Жаль, что ты все пропустишь. . ."
                            return
            else:
                    ch_b "Ох, эм, я тут немного занята."
                    ch_b "Встретимся в другой раз. . ."
                    $ BetsyX.RecentActions.append("no summon")
                    return
    elif not ApprovalCheck(BetsyX, 700, "L") or not ApprovalCheck(BetsyX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(BetsyX, 300):
                ch_b "Боюсь, я занята, [BetsyX.Petname]."
                $ BetsyX.RecentActions.append("no summon")
                return


        if "summoned" in BetsyX.RecentActions:
                pass
        elif "goto" in BetsyX.RecentActions:
                if not Player.Male:
                    ch_b "Ты только что ушла. . ."
                else:
                    ch_b "Ты только что ушел. . ."
        elif BetsyX.Loc == "bg classroom":
                ch_b "Я на занятиях, тоже хочешь пойти?"
        elif BetsyX.Loc == "bg dangerroom":
                ch_b "Я в Комнате Опасности, [BetsyX.Petname], желаешь присоедениться?"
        elif BetsyX.Loc == "bg campus":
                ch_b "Я отдыхаю во дворе, не хочешь присоединиться ко мне?"
        elif BetsyX.Loc == "bg betsy":
                ch_b "Я в своей комнате, [BetsyX.Petname], не хочешь присоединиться ко мне?"
        elif BetsyX.Loc == "bg player":
                ch_b "Я в твоей комнате, [BetsyX.Petname], не хочешь присоединиться ко мне?"
        elif BetsyX.Loc == "bg showerroom":
            if ApprovalCheck(BetsyX, 1600):
                ch_b "Я сейчас в душе. Не желаешь присоедениться?"
            else:
                ch_b "Я сейчас в душе, [BetsyX.Petname], увидимся в другой раз."
                $ BetsyX.RecentActions.append("no summon")
                return
        elif BetsyX.Loc == "hold":
                ch_b "Пардон, в данный момент я очень занята."
                $ BetsyX.RecentActions.append("no summon")
                return
        else:
                ch_b "Ты всегда можешь прийти ко мне. . ."


        if "summoned" in BetsyX.RecentActions:
            ch_b "Снова? Ну, если это так необходимо."
            $ Line = "yes"
        elif "goto" in BetsyX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
                                ch_b "Хорошо. тогда скоро увидимся."
                                $ Line = "go to"
                "Нет.":
                                ch_b "Как хочешь."
                "Мне бы {i}очень{/i} хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(BetsyX, 600, "L") or ApprovalCheck(BetsyX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(BetsyX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(BetsyX, 1400):
                                #she is generally favorable
                                ch_b "Ладно."
                                $ Line = "yes"
                        elif ApprovalCheck(BetsyX, 200, "O"):
                                #she is not obedient
                                ch_b "Какое несчастье."
                                ch_b "Если что, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(BetsyX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(BetsyX, 1400):
                                #she is generally favorable
                                ch_b "Ладно."
                                $ Line = "yes"
                        elif ApprovalCheck(BetsyX, 200, "O"):
                                #she is not obedient
                                ch_b "Какое несчастье."
                                ch_b "Если что, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Конечно, сейчас приду.":
                    $ BetsyX.Statup("Love", 55, 1)
                    $ BetsyX.Statup("Inbt", 30, 1)
#                    ch_b "Jolly good, see you then."
                    $ Line = "go to"

                "Нет, поговорим позже.":
                    $ BetsyX.Statup("Obed", 50, 1)
                    $ BetsyX.Statup("Obed", 30, 2)
                    ch_b "Ох, ну хорошо."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                    if ApprovalCheck(BetsyX, 650, "L") or ApprovalCheck(BetsyX, 1500):
                        $ BetsyX.Statup("Love", 70, 1)
                        $ BetsyX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ BetsyX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                        ch_b "Как очаровательно."

                "Давай, будет весело.":
                    if ApprovalCheck(BetsyX, 400, "L") and ApprovalCheck(BetsyX, 800):
                        $ BetsyX.Statup("Love", 70, 1)
                        $ BetsyX.Statup("Obed", 50, 1)
                        $ Line = "fun"
                    else:
                        $ BetsyX.Statup("Inbt", 30, 1)
                        $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                    if ApprovalCheck(BetsyX, 600, "O"):
                        #she is obedient
                        $ BetsyX.Statup("Love", 50, 1, 1)
                        $ BetsyX.Statup("Love", 40, -1)
                        $ BetsyX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(BetsyX, 1500):
                        #she is generally favorable
                        $ BetsyX.Statup("Love", 70, -2)
                        $ BetsyX.Statup("Love", 90, -1)
                        $ BetsyX.Statup("Obed", 50, 2)
                        $ BetsyX.Statup("Obed", 90, 1)
                        ch_b "Ох, хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(BetsyX, 200, "O"):
                        #she is not obedient
                        $ BetsyX.Statup("Love", 60, -4)
                        $ BetsyX.Statup("Love", 90, -3)
                        ch_b "Что?"
                        $ BetsyX.Statup("Inbt", 40, 2)
                        $ BetsyX.Statup("Inbt", 60, 1)
                        $ BetsyX.Statup("Obed", 70, -3)
                        ch_b "Меня не интересуют твои приказы."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ BetsyX.Statup("Inbt", 30, 1)
                        $ BetsyX.Statup("Inbt", 50, 1)
                        $ BetsyX.Statup("Love", 50, -1, 1)
                        $ BetsyX.Statup("Obed", 70, -1)
                        $ Line = "no"

                "Я сказал, давай ко мне." if Player.Male:
                    if ApprovalCheck(BetsyX, 600, "O"):
                        #she is obedient
                        $ BetsyX.Statup("Love", 50, 1, 1)
                        $ BetsyX.Statup("Love", 40, -1)
                        $ BetsyX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(BetsyX, 1500):
                        #she is generally favorable
                        $ BetsyX.Statup("Love", 70, -2)
                        $ BetsyX.Statup("Love", 90, -1)
                        $ BetsyX.Statup("Obed", 50, 2)
                        $ BetsyX.Statup("Obed", 90, 1)
                        ch_b "Ох, хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(BetsyX, 200, "O"):
                        #she is not obedient
                        $ BetsyX.Statup("Love", 60, -4)
                        $ BetsyX.Statup("Love", 90, -3)
                        ch_b "Что?"
                        $ BetsyX.Statup("Inbt", 40, 2)
                        $ BetsyX.Statup("Inbt", 60, 1)
                        $ BetsyX.Statup("Obed", 70, -3)
                        ch_b "Меня не интересуют твои приказы."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ BetsyX.Statup("Inbt", 30, 1)
                        $ BetsyX.Statup("Inbt", 50, 1)
                        $ BetsyX.Statup("Love", 50, -1, 1)
                        $ BetsyX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if BetsyX.Love > BetsyX.Obed:
            ch_b "Хорошо!"
        else:
            ch_b "Конечно. Я уже в пути."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ BetsyX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            if BetsyX.Loc == "bg classroom":
                ch_b "Я никак не могу пропустить эту лекцию."
            elif BetsyX.Loc == "bg dangerroom":
                ch_b "Я только разогрелась!"
            else:
                ch_b "Пардон, [BetsyX.Petname], я очень занята."
            $ BetsyX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ BetsyX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            $ Nearby = []
            $ Line = 0
            $ Party = [BetsyX]
            if BetsyX.Loc == "bg classroom":
                    ch_b "Отлично, найди меня, когда придешь."
                    jump Class_Room
            elif BetsyX.Loc == "bg dangerroom":
                    ch_b "Хорошо, я пока разомнусь."
                    jump Danger_Room
            elif BetsyX.Loc == "bg betsy":
                    ch_b "Я пока. . . немного приберусь."
                    jump Betsy_Room
            elif BetsyX.Loc == "bg player":
                    ch_b "Увидимся, когда придешь."
                    jump Player_Room
            elif BetsyX.Loc == "bg showerroom":
                    ch_b "Я оставлю тебе немного горячей воды."
                    jump Shower_Room
            elif BetsyX.Loc == "bg campus":
                    ch_b "До встречи."
                    jump Campus
            elif BetsyX.Loc != "hold":
                    ch_b "Увидимся."
                    $ bg_current = BetsyX.Loc
                    jump Misplaced
            else:
                    ch_b "Возможно, я просто встречу тебя в своей комнате."
                    $ BetsyX.Loc = "bg betsy"
                    jump Betsy_Room

    #She's agreed to come over
    elif Line == "lonely":
            if not Player.Male:
                ch_b "Боже, я просто не могу оставить тебя одну. . ."
            else:
                ch_b "Боже, я просто не могу оставить тебя одного. . ."
    elif Line == "command":
            ch_b "Ладно, [BetsyX.Petname]."
    elif Line == "fun":
            ch_b "Конечно."

    $ BetsyX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(BetsyX)
            return
    $ BetsyX.Loc = bg_current
    call Taboo_Level(0)
    $ BetsyX.OutfitChange()
    call Set_The_Scene
    return

# End Betsy Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Betsy_Leave(Tempmod=Tempmod, GirlsNum = 0):    #rkeljsvgb
    if "leaving" in BetsyX.RecentActions:
        $ BetsyX.DrainWord("leaving")
    else:
        return

    if BetsyX.Loc == "hold":
            # Activates if she's being moved out of play
            ch_b "Мне нужно ненадолго отлучиться, увидимся позже."
            return

    if BetsyX in Party or "lockedtravels" in BetsyX.Traits:
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ BetsyX.Loc = bg_current
            return

    elif "freetravels" in BetsyX.Traits or not ApprovalCheck(BetsyX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.
            $ BetsyX.OutfitChange()
            if GirlsNum: #if someone left before her
                        ch_b "Конечно, я тоже пойду."

            if BetsyX.Loc == "bg classroom":
                        ch_b "У меня занятия."
            elif BetsyX.Loc == "bg dangerroom":
                        ch_b "Я собираюсь насладиться Комнатой Опасности."
            elif BetsyX.Loc == "bg campus":
                        ch_b "Отдохну во дворе."
            elif BetsyX.Loc == "bg betsy":
                        ch_b "Я возвращаюсь в свою комнату."
            elif BetsyX.Loc == "bg player":
                        ch_b "Я немного отдохну в твоей комнате."
            elif BetsyX.Loc == "bg pool":
                        ch_b "Я собираюсь насладиться бассейном."
            elif BetsyX.Loc == "bg showerroom":
                if ApprovalCheck(BetsyX, 1400):
                        ch_b "Я собираюсь принять душ."
                else:
                        ch_b "До свидания."
            else:
                        ch_b "До скорого."
            hide Betsy_Sprite
            hide Betsy_Seated
            return
            #End Free Travels

    if bg_current == "bg dangerroom":
            call Gym_Exit([BetsyX])

    $ BetsyX.OutfitChange()

    if "follow" not in BetsyX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ BetsyX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    # Sets her preferences
    if BetsyX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif BetsyX.Loc == "bg dangerroom":
        $ Tempmod = 20
    elif BetsyX.Loc == "bg showerroom":
        $ Tempmod = 40


    if GirlsNum: #if someone left before her
                ch_b "Да, я тоже пойду."

    if BetsyX.Loc == "bg classroom":
            ch_b "Я на занятия, хочешь тоже пойти?"
    elif BetsyX.Loc == "bg dangerroom":
            ch_b "Я в Комнату Опасности, [BetsyX.Petname], не хочешь присоединиться ко мне?"
    elif BetsyX.Loc == "bg campus":
            ch_b "Я хочу отдохнуть во дворе, не хочешь присоединиться ко мне?"
    elif BetsyX.Loc == "bg betsy":
            ch_b "Я в свою комнату, [BetsyX.Petname], не хочешь присоединиться ко мне?"
    elif BetsyX.Loc == "bg player":
            ch_b "Я в твою комнату, [BetsyX.Petname], не хочешь присоединиться ко мне?"
    elif BetsyX.Loc == "bg mall":
            ch_b "Я собираюсь по магазинам, [BetsyX.Petname], не хочешь присоединиться ко мне?"
    elif BetsyX.Loc == "bg showerroom":
        if ApprovalCheck(BetsyX, 1600):
            ch_b "Я в душ. Не хочешь присоединиться ко мне?"
        else:
            ch_b "Я в душ, [BetsyX.Petname], увидимся позже."
            return
    elif BetsyX.Loc == "bg pool":
                ch_b "Я к бассейну. Не хочешь присоединиться ко мне?"
    else:
                ch_b "Не хочешь присоединиться ко мне?"


    menu:
        extend ""
        "Конечно, я сразу за тобой.":
                if "followed" not in BetsyX.RecentActions:
                    $ BetsyX.Statup("Love", 55, 1)
                    $ BetsyX.Statup("Inbt", 30, 1)
                $ Line = "go to"

        "Нет, поговорим позже.":
                if "followed" not in BetsyX.RecentActions:
                    $ BetsyX.Statup("Obed", 50, 1)
                    $ BetsyX.Statup("Obed", 30, 2)
                ch_b "Ох, конечно."

        "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                if ApprovalCheck(BetsyX, 650, "L") or ApprovalCheck(BetsyX, 1500):
                    if "followed" not in BetsyX.RecentActions:
                        $ BetsyX.Statup("Love", 70, 1)
                        $ BetsyX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else:
                    if "followed" not in BetsyX.RecentActions:
                        $ BetsyX.Statup("Inbt", 30, 1)
                    $ Line = "no"
                    ch_b "Как очаровательно."

        "Давай, будет весело.":
                if ApprovalCheck(BetsyX, 400, "L") and ApprovalCheck(BetsyX, 800):
                    $ BetsyX.Statup("Love", 70, 1)
                    $ BetsyX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else:
                    $ BetsyX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Нет, останься здесь.":
                if ApprovalCheck(BetsyX, 600, "O"):
                    #she is obedient
                    if "followed" not in BetsyX.RecentActions:
                        $ BetsyX.Statup("Love", 40, -2)
                        $ BetsyX.Statup("Obed", 90, 1)
                    $ Line = "command"

                elif D20 >= 7 and ApprovalCheck(BetsyX, 1400):
                    #she is generally favorable
                    if "followed" not in BetsyX.RecentActions:
                        $ BetsyX.Statup("Love", 70, -2)
                        $ BetsyX.Statup("Love", 90, -1)
                        $ BetsyX.Statup("Obed", 50, 2)
                        $ BetsyX.Statup("Obed", 90, 1)
                    ch_b "Ладно, я могу немного задержаться."
                    $ Line = "yes"

                elif ApprovalCheck(BetsyX, 200, "O"):
                    #she is not obedient
                    if "followed" not in BetsyX.RecentActions:
                        $ BetsyX.Statup("Love", 70, -4)
                        $ BetsyX.Statup("Love", 90, -2)
                    ch_b "Что?"
                    if "followed" not in BetsyX.RecentActions:
                        $ BetsyX.Statup("Inbt", 40, 2)
                        $ BetsyX.Statup("Inbt", 60, 1)
                        $ BetsyX.Statup("Obed", 70, -2)
                    ch_b "Я не останусь из-за одной твоей прихоти."
                else:
                    #she is obedient, but you failed to meet the checks
                    if "followed" not in BetsyX.RecentActions:
                        $ BetsyX.Statup("Inbt", 30, 1)
                        $ BetsyX.Statup("Inbt", 50, 1)
                        $ BetsyX.Statup("Love", 50, -1, 1)
                        $ BetsyX.Statup("Love", 90, -2)
                        $ BetsyX.Statup("Obed", 70, -1)
                    $ Line = "no"
                #End ordered to stay

    call Taboo_Level(0)
    $ BetsyX.RecentActions.append("followed")
    if not Line:
            #You end the dialog neutrally
            hide Betsy_Sprite
            hide Betsy_Seated
            call Gym_Clothes_Off([BetsyX])
            return

    if Line == "no":
            # She's refused, context based dialog
            if BetsyX.Loc == "bg classroom":
                ch_b "Я никак не могу пропустить это занятие."
            elif BetsyX.Loc == "bg dangerroom":
                ch_b "Пардон, [BetsyX.Petname], но мне очень нужно позаниматься."
            else:
                ch_b "Пардон, но у меня много дел."
            hide Betsy_Sprite
            hide Betsy_Seated
            call Gym_Clothes_Off([BetsyX])
            return

    elif Line == "go to":
            #You agreed to go to her instead
            #$ Party.append(BetsyX)
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")
            $ BetsyX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            hide Betsy_Sprite
            hide Betsy_Seated
            $ Nearby = []
            $ Party = [BetsyX]
            call Gym_Clothes_Off([BetsyX])
            if BetsyX.Loc == "bg classroom":
                ch_b "Замечательно, я займу тебе место."
                jump Class_Room_Entry
            elif BetsyX.Loc == "bg dangerroom":
                ch_b "Я пока разогреюсь."
                jump Danger_Room_Entry
            elif BetsyX.Loc == "bg betsy":
                ch_b "Конечно."
                jump Betsy_Room
            elif BetsyX.Loc == "bg player":
                ch_b "Замечательно."
                jump Player_Room
            elif BetsyX.Loc == "bg showerroom":
                ch_b "Замечательно."
                jump Shower_Room_Entry
            elif BetsyX.Loc == "bg campus":
                ch_b "Замечательно."
                jump Campus_Entry
            elif BetsyX.Loc == "bg pool":
                ch_b "Замечательно."
                jump Pool_Entry
            elif BetsyX.Loc == "bg mall":
                ch_b "Замечательно."
                jump Mall_Entry
            else:
                ch_b "Тогда я просто встречусь с тобой в твоей комнате."
                $ BetsyX.Loc = "bg player"
                jump Player_Room
            #End "goto" where she's at

    #She's agreed to come over
    elif Line == "lonely":
            if not Player.Male:
                ch_b "Боже, я просто не могу оставить тебя одну. . ."
            else:
                ch_b "Боже, я просто не могу оставить тебя одного. . ."
    elif Line == "command":
            ch_b "Ладно, [BetsyX.Petname]."
    elif Line:
            ch_b "Конечно."

    $ Line = 0
    ch_b "I could stay here."
    $ BetsyX.Loc = bg_current
    call Taboo_Level(0)
    return

# End Betsy Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

### Betsy's Clothes  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Betsy_Clothes:   #rkeljsvgb
    if BetsyX.Taboo:
            if "exhibitionist" in BetsyX.Traits:
                ch_b "Да? . ."
            elif ApprovalCheck(BetsyX, 900, TabM=4) or ApprovalCheck(BetsyX, 400, "I", TabM=3):
                ch_b "Мне не стоит здесь раздеваться. . ."
            else:
                ch_b "Мне не стоит здесь раздеваться. . ."
                ch_b "Не могли бы мы все обсудить в одной из наших комнат?"
                return
    elif ApprovalCheck(BetsyX, 900, TabM=4) or ApprovalCheck(BetsyX, 600, "L") or ApprovalCheck(BetsyX, 300, "O"):
                ch_b "Что ты желаешь обсудить?"
    else:
                ch_b "Почему тебя так заботит моя одежда?"
                return

    if Girl != BetsyX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = BetsyX
    call Shift_Focus(Girl)

label Betsy_Wardrobe_Menu:
    $ BetsyX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .
    while True:
        menu:
            ch_b "Что ты желаешь обсудить?"
            "Верх":
                        call Betsy_Clothes_Over
            "Низ":
                        call Betsy_Clothes_Legs
            "Нижнее белье":
                        call Betsy_Clothes_Under
            "Аксессуары":
                        call Betsy_Clothes_Misc
            "Управление нарядами":
                        call Betsy_Clothes_Outfits
            "Давай поговорим о том, что ты носишь.":
                        call Clothes_Schedule(BetsyX)

            "Могу я посмотреть?" if BetsyX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(BetsyX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_b "Конечно, что думаешь?"
                    hide PhoneSex
            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(BetsyX,0,2)
                    if _return:
                        hide DressScreen
            "Может, тебе будет комфортнее за ширмой? (locked)" if BetsyX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if BetsyX.Loc == bg_current and not BetsyX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if not Player.Male and "girltalk" not in BetsyX.History and "nogirls" not in BetsyX.History:
                            ch_b "Это так необходимо?"
                    elif ApprovalCheck(BetsyX, 1500) or (BetsyX.SeenChest and BetsyX.SeenPussy):
                            ch_b "Пожалуй, в этом нет такой уж необходимости."
                    else:
                            show DressScreen zorder 150
                            ch_b "Так будет лучше, благодарю."

            "У меня есть подарок для тебя (locked)" if BetsyX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if BetsyX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(BetsyX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ BetsyX.OutfitChange()
                    $ BetsyX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != BetsyX:
                            ch_p "Я хочу поговорить о твоей одежде."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = BetsyX
                    call Shift_Focus(Girl)

            "Сменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current:
                    pass
            "Сменить вид" if Girl.Loc == bg_current:
                    call WardrobeView(BetsyX)

            "Неважно, ты и так хорошо выглядишь":
                    call Girl_Pos_Reset(BetsyX)
                    if "wardrobe" not in BetsyX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if BetsyX.Chat[1] <= 1:
                                    $ BetsyX.Statup("Love", 70, 15)
                                    $ BetsyX.Statup("Obed", 40, 20)
                                    ch_b "Ох! Благодарю."
                            elif BetsyX.Chat[1] <= 10:
                                    $ BetsyX.Statup("Love", 70, 5)
                                    $ BetsyX.Statup("Obed", 40, 7)
                                    ch_b "Правда?"
                            elif BetsyX.Chat[1] <= 50:
                                    $ BetsyX.Statup("Love", 70, 1)
                                    $ BetsyX.Statup("Obed", 40, 1)
                                    ch_b "Да?"
                            else:
                                    ch_b "Конечно."
                            $ BetsyX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(BetsyX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ BetsyX.OutfitChange()
                    $ BetsyX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ BetsyX.Chat[1] += 1
                    $ Trigger = 0
                    if BetsyX.Panties and "pantyless" in BetsyX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ BetsyX.DailyActions.remove("pantyless")
                    return

        #Loops back up
        #return #jump Betsy_Clothes
        #End of Betsy Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Betsy_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(BetsyX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(BetsyX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(BetsyX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(BetsyX,4,1)
                    "Одежда для сна":
                                call OutfitShame(BetsyX,7,1)
                    "Купальник":
                                call OutfitShame(BetsyX,10,1)
                    #8 is Emma's teaching clothes,

                    "Повседневка 1" if ApprovalCheck(BetsyX, 2500):
                                call OutfitShame(BetsyX,11,1)
                    "Повседневка 2" if ApprovalCheck(BetsyX, 2500):
                                call OutfitShame(BetsyX,12,1)

                    "Неважно":
                                pass

        "Надень майку и шорты.":
                $ BetsyX.OutfitChange("casual1")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                            $ BetsyX.Outfit = "casual1"
                            $ BetsyX.Shame = 0
                            ch_b "Мне очень нравится их стиль."
                    "Давай попробуем что-нибудь другое.":
                            ch_b "Ох."

        "Надень розовый топик и юбку.":
                $ BetsyX.OutfitChange("casual2")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                            $ BetsyX.Outfit = "casual2"
                            $ BetsyX.Shame = 0
                            ch_b "Конечно, они стильные."
                    "Давай попробуем что-нибудь другое.":
                            ch_b "Ох."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not BetsyX.Custom1[0] and not BetsyX.Custom2[0] and not BetsyX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if BetsyX.Custom1[0] or BetsyX.Custom2[0] or BetsyX.Custom3[0]:
                $ Cnt = 0
                while 1:
                    menu:
                        "Надень Пользовательский 1 (locked)" if not BetsyX.Custom1[0]:
                                pass
                        "Надень Пользовательский 1" if BetsyX.Custom1[0]:
                                $ BetsyX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Надень Пользовательский 2 (locked)" if not BetsyX.Custom2[0]:
                                pass
                        "Надень Пользовательский 2" if BetsyX.Custom2[0]:
                                $ BetsyX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Надень Пользовательский 3 (locked)" if not BetsyX.Custom3[0]:
                                pass
                        "Надень Пользовательский 3" if BetsyX.Custom3[0]:
                                $ BetsyX.OutfitChange("custom3")
                                $ Cnt = 6

                        "Ты должна одеваться так, когда мы наедине (locked)" if not Cnt:
                                pass
                        "Ты должна одеваться так, когда мы наедине" if Cnt:
                                if Cnt == 5:
                                    $ BetsyX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ BetsyX.Clothing[9] = "custom3"
                                else:
                                    $ BetsyX.Clothing[9] = "custom1"
                                ch_b "Ох, хорошо."

                        "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                menu:
                                    "Пользовательский 1 [[очистить слот 1]" if BetsyX.Custom1[0]:
                                        ch_b "Ох."
                                        $ BetsyX.Custom1[0] = 0
                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not BetsyX.Custom1[0]:
                                        pass
                                    "Пользовательский 2 [[очистить слот 2]" if BetsyX.Custom2[0]:
                                        ch_b "Ох."
                                        $ BetsyX.Custom2[0] = 0
                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not BetsyX.Custom2[0]:
                                        pass
                                    "Пользовательский 3 [[очистить слот 3]" if BetsyX.Custom3[0]:
                                        ch_b "Ох."
                                        $ BetsyX.Custom3[0] = 0
                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not BetsyX.Custom3[0]:
                                        pass
                                    "Неважно [[назад]":
                                        pass

                        "Тебе следует надеть его [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                pass
                        "Тебе следует надеть его" if Cnt:
                                call Custom_Out(BetsyX,Cnt)
                        "Ладно, вернемся к началу нашего разговора. . .":
                                $ Cnt = 0
                                return #jump Betsy_Clothes

        "Наденешь спортивную одежду?" if not BetsyX.Taboo or bg_current == "bg dangerroom":
                $ BetsyX.OutfitChange("gym")

        "Наденешь одежду для сна?" if not BetsyX.Taboo:
                if ApprovalCheck(BetsyX, 1200):
                        $ BetsyX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(BetsyX)
                        if _return:
                            $ BetsyX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (BetsyX.Taboo and bg_current != "bg pool" and not ApprovalCheck(BetsyX, 800, TabM=2)) or not BetsyX.Swim[0]:
                $ BetsyX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not BetsyX.Taboo or bg_current == "bg pool" or ApprovalCheck(BetsyX, 800, TabM=2)) and BetsyX.Swim[0]:
                $ BetsyX.OutfitChange("swimwear")

        "Наденешь хэллоуинский костюм?" if "halloween" in BetsyX.History:
                ch_b "Ох."
                $ BetsyX.OutfitChange("costume")

        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ BetsyX.FaceChange("sexy", 1)
                $ Line = 0
                if not BetsyX.Chest and not BetsyX.Panties and not BetsyX.Over and not BetsyX.Legs and not BetsyX.Hose:
                    ch_b "Ох. . . что?"
                elif BetsyX.SeenChest and BetsyX.SeenPussy and ApprovalCheck(BetsyX, 1200, TabM=4):
                    ch_b "Благодарю? . ."
                    $ Line = 1
                elif ApprovalCheck(BetsyX, 2000, TabM=4):
                    if not Player.Male:
                        ch_b "А ты смелая. . ."
                    else:
                        ch_b "А ты смелый. . ."
                    $ Line = 1
                elif BetsyX.SeenChest and BetsyX.SeenPussy and ApprovalCheck(BetsyX, 1200, TabM=0):
                    ch_b "Возможно, но мне не интересно делать из себя посмешище. . ."
                elif ApprovalCheck(BetsyX, 2000, TabM=0):
                    ch_b "Возможно, но мне не интересно делать из себя посмешище. . ."
                elif ApprovalCheck(BetsyX, 1000, TabM=0):
                    $ BetsyX.FaceChange("confused", 1,Mouth="smirk")
                    ch_b "Возможно, но мне не интересно делать из себя посмешище. . ."
                    $ BetsyX.FaceChange("bemused", 0)
                else:
                    $ BetsyX.FaceChange("angry", 1)
                    ch_b "Зачем было говорить об этом?"

                call expression BetsyX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in BetsyX.History:
                        $ Line = 0
                if Line:
                    #If she got nude. . .
                    $ BetsyX.OutfitChange("nude")
                    "Она сбрасывает одежду к своим ногам."
                    call Girl_First_Topless(BetsyX)
                    call Girl_First_Bottomless(BetsyX,1)
                    $ BetsyX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется, что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in BetsyX.Traits:
                                ch_b "Возможно. . ."
                                $ BetsyX.Outfit = "nude"
                                $ BetsyX.Statup("Lust", 50, 10)
                                $ BetsyX.Statup("Lust", 70, 5)
                                $ BetsyX.Shame = 50
                            elif ApprovalCheck(BetsyX, 800, "I") or ApprovalCheck(BetsyX, 2800, TabM=0):
                                ch_b "Оооох, конечно. . ."
                                $ BetsyX.Outfit = "nude"
                                $ BetsyX.Shame = 50
                            else:
                                $ BetsyX.FaceChange("sexy", 1)
                                $ BetsyX.Eyes = "surprised"
                                ch_b "Точно нет."

                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in BetsyX.Traits:
                                ch_b "Ох, серьезно?"
                            elif ApprovalCheck(BetsyX, 800, "I") or ApprovalCheck(BetsyX, 2800, TabM=0):
                                $ BetsyX.FaceChange("bemused", 1)
                                ch_b "Тебе неинтересно видеть, как я разгуливаю в таком виде? . ."
                                ch_b ". . ."
                            else:
                                $ BetsyX.FaceChange("confused", 1)
                                ch_b "Не то чтобы я против того, чтобы меня видели без одежды, но я бы предпочла не разгуливать в таком виде на людях. . ."
                $ Line = 0

        "Неважно":
            return #jump Betsy_Clothes

    return #jump Betsy_Clothes
    #End of Betsy Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Betsy_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять [get_clothing_name(BetsyX.Over_key, vin)]?" if BetsyX.Over:
                call Wardrobe_Remove(BetsyX)

        "Примерь синюю майку." if BetsyX.Over != "tank":
                $ BetsyX.FaceChange("bemused")
                if not BetsyX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_b "Хорошо."
                elif ApprovalCheck(BetsyX, 800, TabM=0):
                    ch_b "Хорошо."
                else:
                    call Display_DressScreen(BetsyX)
                    if not _return:
                            $ BetsyX.FaceChange("bemused", 1)
                            ch_b "Я бы предпочла сейчас не переодевать [get_clothing_name(BetsyX.Over_key, vin)]."
                            return #jump Betsy_Clothes
                $ BetsyX.Over = "tank"

        "Примерь розовый топик." if BetsyX.Over != "pink top":
                $ BetsyX.FaceChange("bemused")
                if not BetsyX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_b "Хорошо."
                elif ApprovalCheck(BetsyX, 800, TabM=0):
                    ch_b "Хорошо."
                else:
                    call Display_DressScreen(BetsyX)
                    if not _return:
                            $ BetsyX.FaceChange("bemused", 1)
                            ch_b "Я бы предпочла сейчас не переодевать [get_clothing_name(BetsyX.Over_key, vin)]."
                            return #jump Betsy_Clothes
                $ BetsyX.Over = "pink top"

        "Примерь куртку." if BetsyX.Over != "jacket" and "halloween" in BetsyX.History:
                $ BetsyX.FaceChange("bemused")
                if not BetsyX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_b "Хорошо."
                elif ApprovalCheck(BetsyX, 800, TabM=0):
                    ch_b "Хорошо."
                else:
                    call Display_DressScreen(BetsyX)
                    if not _return:
                            $ BetsyX.FaceChange("bemused", 1)
                            ch_b "Я бы предпочла сейчас не переодевать [get_clothing_name(BetsyX.Over_key, vin)]."
                            return #jump Betsy_Clothes
                $ BetsyX.Over = "jacket"

        "Может, просто накинешь полотенце?" if BetsyX.Over != "towel":
                $ BetsyX.FaceChange("bemused", 1)
                if BetsyX.Chest or BetsyX.SeenChest:
                    ch_b "Необычный выбор. . ."
                elif ApprovalCheck(BetsyX, 1000, TabM=0):
                    $ BetsyX.FaceChange("perplexed", 1)
                    ch_b "Ох. . ."
                else:
                    call Display_DressScreen(BetsyX)
                    if not _return:
                            ch_b "Не уверена, что оно сейчас к месту."
                            return #jump Betsy_Clothes
                $ BetsyX.Over = "towel"

        "Неважно":
            pass
    return #jump Betsy_Clothes
    #End of Betsy Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Betsy_NoBra:
        menu:
            ch_b "Боюсь, на мне сейчас нет лифчика. . ."
            "Тогда надень какой-нибудь. . .":
                        if BetsyX.SeenChest and ApprovalCheck(BetsyX, 1000, TabM=3):
                                $ BetsyX.Blush = 1
                                ch_b "Я не говорила, что меня это беспокоит. . ."
                                $ BetsyX.Blush = 0
                        elif ApprovalCheck(BetsyX, 1200, TabM=4):
                                $ BetsyX.Blush = 1
                                ch_b "Я не говорила, что меня это беспокоит. . ."
                                $ BetsyX.Blush = 0
                        elif ApprovalCheck(BetsyX, 900, TabM=2) and "lace bra" in BetsyX.Inventory:
                                ch_b "Пожалуй, я могу что-нибудь подобрать."
                                $ BetsyX.Chest  = "lace bra"
                                "Она достает свой кружевной лифчик и надевает его под [get_clothing_name(BetsyX.Over_key, vin)]."
                        elif ApprovalCheck(BetsyX, 700, TabM=2):
                                ch_b "I suppose I could find something."
                                $ BetsyX.Chest = "bra"
                                "Она достает синий лифчик и надевает его под [get_clothing_name(BetsyX.Over_key, vin)]."
                        else:
                                ch_b "Я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(BetsyX, 1100, "LI", TabM=2) and BetsyX.Love > BetsyX.Inbt:
                                ch_b "Для тебя? Пожалуй. . ."
                        elif ApprovalCheck(BetsyX, 700, "OI", TabM=2) and BetsyX.Obed > BetsyX.Inbt:
                                ch_b "Конечно. . ."
                        elif ApprovalCheck(BetsyX, 600, "I", TabM=2):
                                ch_b "Согласна. . ."
                        elif ApprovalCheck(BetsyX, 1300, TabM=2):
                                ch_b "Ох. . ."
                        else:
                                $ BetsyX.FaceChange("surprised")
                                $ BetsyX.Brows = "angry"
                                if BetsyX.Taboo > 20:
                                    ch_b "Боюсь, не на людях!"
                                else:
                                    if not Player.Male:
                                        ch_b "Ты далеко не такая милая, как ты думаешь, [BetsyX.Petname]!"
                                    else:
                                        ch_b "Ты далеко не такой милый, как ты думаешь, [BetsyX.Petname]!"
                                call expression BetsyX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0
            "Неважно.":
                        ch_b "Ох. . ."
                        return 0
        return 1
        #End of Betsy bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Betsy_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(BetsyX.Legs_key, vin)]?" if BetsyX.Legs:
                call Wardrobe_Remove(BetsyX,1)

        "Примерь синие шорты" if BetsyX.Legs != "shorts":
                ch_p "Ты великолепно выглядишь в своих синих шортах."
                ch_b "Правда?"
                $ BetsyX.Legs = "shorts"

        "Примерь синюю юбку" if BetsyX.Legs != "skirt":
                ch_p "Как насчет того, чтобы надеть синюю юбку?"
                ch_b "Ладно?"
                $ BetsyX.Legs = "skirt"

        "Примерь штаны для йоги" if BetsyX.Legs != "yoga pants":
                ch_p "Ты великолепно выглядишь в штанах для йоги."
                ch_b "Ладно?"
                $ BetsyX.Legs = "yoga pants"

        "Сними обувь (locked)" if not BetsyX.Boots:
                pass
        "Сними [get_clothing_name(BetsyX.Boots_key, vin)]" if BetsyX.Boots:
                ch_p "Может, снимешь [get_clothing_name(BetsyX.Boots_key, vin)]?"
                ch_b "Ох."
                $ BetsyX.Boots = 0
        "Надень сандалии" if BetsyX.Boots != "shoes":
                ch_p "Может, наденешь сандалии?"
                ch_b "Ох."
                $ BetsyX.Boots = "shoes"
        "Надень кеды" if BetsyX.Boots != "sneaks":
                ch_p "Может, наденешь кеды?"
                ch_b "Ох, тренировочные?"
                $ BetsyX.Boots = "sneaks"
#        "Add Sneakers" if BetsyX.Boots != "sneaks":
#                ch_p "Maybe put your sneakers on."
#                ch_b "'K."
#                $ BetsyX.Boots = "sneaks"

        "Неважно":
                pass
    return #jump Betsy_Clothes
    #End of Betsy Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Betsy_NoPantiesOn:
        menu:
            ch_b "Боюсь, на мне нет трусиков. . ."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if BetsyX.SeenPussy and ApprovalCheck(BetsyX, 1100, TabM=4):
                                $ BetsyX.Blush = 1
                                ch_b "Мне нравится, когда там все дышит. . ."
                                $ BetsyX.Blush = 0
                        elif ApprovalCheck(BetsyX, 1500, TabM=4):
                                $ BetsyX.Blush = 1
                                ch_b "Мне нравится, когда там все дышит. . ."
                                $ BetsyX.Blush = 0
                        elif ApprovalCheck(BetsyX, 700, TabM=4):
                                ch_b "Ох, пожалуй."
                                if "lace panties" in BetsyX.Inventory:
                                        ch_b "Мне нравится ход твоих мыслей."
                                        $ BetsyX.Panties  = "lace panties"
                                else:
                                        $ BetsyX.Panties = "blue panties"
                                if ApprovalCheck(BetsyX, 1200, TabM=4):
                                    $ Line = get_clothing_name(BetsyX.Legs_key, vin)
                                    $ BetsyX.Legs = 0
                                    "Она снимает [Line] и натягивает [get_clothing_name(BetsyX.Panties_key, vin)]."
                                elif BetsyX.Legs == "skirt":
                                    "Она достает [get_clothing_name(BetsyX.Panties_key, vin)] и натягивает их под юбку."
                                    $ BetsyX.Legs = 0
                                    "Затем она сбрасывает юбку на пол."
                                else:
                                    $ Line = get_clothing_name(BetsyX.Legs_key, vin)
                                    $ BetsyX.Legs = 0
                                    "Она отходит на мгновение, а затем возвращается в [get_clothing_name(BetsyX.Panties_key, pre)]."
                                return #jump Betsy_Clothes
                        else:
                                ch_b "Боюсь, я вынуждена отказаться."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(BetsyX, 1100, "LI", TabM=3) and BetsyX.Love > BetsyX.Inbt:
                                ch_b "Пожалуй. . ."
                        elif ApprovalCheck(BetsyX, 700, "OI", TabM=3) and BetsyX.Obed > BetsyX.Inbt:
                                ch_b "Конечно. . ."
                        elif ApprovalCheck(BetsyX, 600, "I", TabM=3):
                                ch_b "Наверное. . ."
                        elif ApprovalCheck(BetsyX, 1300, TabM=3):
                                ch_b "Согласна. . ."
                        else:
                                $ BetsyX.FaceChange("surprised")
                                $ BetsyX.Brows = "angry"
                                if BetsyX.Taboo > 20:
                                    ch_b "Но не на людях."
                                else:
                                    if not Player.Male:
                                        ch_b "Ты далеко не такая милая, как ты думаешь, [BetsyX.Petname]!"
                                    else:
                                        ch_b "Ты далеко не такой милый, как ты думаешь, [BetsyX.Petname]!"
                                call expression BetsyX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно.":
                ch_b "Ох. . ."
                return 0
        return 1
        #End of Betsy Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Betsy_Clothes_Under:
        "Верх":
            menu:
                "Может, снимешь [get_clothing_name(BetsyX.Chest_key, vin)]?" if BetsyX.Chest:
                        $ BetsyX.FaceChange("bemused", 1)
                        if BetsyX.SeenChest and ApprovalCheck(BetsyX, 900, TabM=2.7):
                            ch_b "Конечно."
                        elif ApprovalCheck(BetsyX, 1100, TabM=2):
                            if BetsyX.Taboo:
                                ch_b "Я бы предпочла не делать этого здесь. . ."
                            else:
                                ch_b "Ладно. . ."
#                        elif BetsyX.Over == "jacket" and ApprovalCheck(BetsyX, 600, TabM=2):
#                            ch_b "This jacket is a bit revealing. . ."
                        elif BetsyX.Over and ApprovalCheck(BetsyX, 500, TabM=2):
                            ch_b "Пожалуй, это я могу. . ."
                        elif not BetsyX.Over:
                            call Display_DressScreen(BetsyX)
                            if not _return:
                                ch_b "Боюсь, это неуместно."
                                return #jump Betsy_Clothes
                        else:
                            call Display_DressScreen(BetsyX)
                            if not _return:
                                ch_b "Боюсь, что не могу."
                                return #jump Betsy_Clothes
                        $ Line = get_clothing_name(BetsyX.Chest_key, vin)
                        $ BetsyX.Chest = 0
                        if Line == "swimsuit":
                            if BetsyX.Over:
                                "Сначала она просовывает руку под [get_clothing_name(BetsyX.Over_key, vin)] и снимает верх купальника."
                            else:
                                "Сначала она снимает верх купальника."
                        elif BetsyX.Over:
                            "Она залезает под [get_clothing_name(BetsyX.Over_key, vin)], хватает [Line] и вытаскивает, роняя на пол."
                        else:
                            "Она скидывает [Line] на пол."
                        if Line == "swimsuit":
                                "Затем она снимает его полностью."
                                if not renpy.showing('DressScreen'):
                                    call Girl_First_Bottomless(BetsyX,1)
                        if not renpy.showing('DressScreen'):
                            call Girl_First_Topless(BetsyX)

                "Примерь синий лифчик" if BetsyX.Chest != "bra":
                        ch_p "Мне нравится твой синий лифчик."
                        if BetsyX.SeenChest or ApprovalCheck(BetsyX, 1100, TabM=2):
                            ch_b "Хорошо."
                            $ BetsyX.Chest = "bra"
                        else:
                            call Display_DressScreen(BetsyX)
                            if not _return:
                                ch_b "Он довольно маленький. . ."
                            else:
                                $ BetsyX.Chest = "bra"

                "Примерь спортивный лифчик" if BetsyX.Chest != "sports bra" and "halloween" in BetsyX.History:
                        ch_p "Мне нравится твой спортивный лифчик."
                        if BetsyX.SeenChest or ApprovalCheck(BetsyX, 1100, TabM=2):
                            ch_b "Поняла."
                            $ BetsyX.Chest = "sports bra"
                        else:
                            call Display_DressScreen(BetsyX)
                            if not _return:
                                ch_b "Он немного жмет. . ."
                            else:
                                $ BetsyX.Chest = "sports bra"

                "Примерь кружевной лифчик" if BetsyX.Chest != "lace bra" and "lace bra" in BetsyX.Inventory:
                        ch_p "Мне нравится твой кружевной лифчик."
                        if BetsyX.SeenChest or ApprovalCheck(BetsyX, 1300, TabM=2):
                            ch_b "Хорошо."
                            $ BetsyX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(BetsyX)
                            if not _return:
                                ch_b "Он довольно прозрачный. . ."
                            else:
                                $ BetsyX.Chest = "lace bra"

                "Примерь купальник" if (BetsyX.Chest != "swimsuit" or BetsyX.Panties != "swimsuit") and "swimsuit" in BetsyX.Inventory:
                        ch_p "Мне нравится твой купальник."
                        $ BetsyX.Swim[0] = 1
                        if bg_current == "bg pool":
                                ch_b "Хорошо."
                                $ BetsyX.Chest = "swimsuit"
                                $ BetsyX.Panties = "swimsuit"
                        else:
                                if BetsyX.SeenChest or ApprovalCheck(BetsyX, 1000, TabM=2):
                                    ch_b "Хорошо."
                                    $ BetsyX.Chest = "swimsuit"
                                    $ BetsyX.Panties = "swimsuit"
                                else:
                                    call Display_DressScreen(BetsyX)
                                    if not _return:
                                            ch_b "Боюсь, что такой наряд не подходит для данного места. . ."
                                    else:
                                            $ BetsyX.Chest = "swimsuit"
                                            $ BetsyX.Panties = "swimsuit"
                "Неважно":
                        pass
            return #jump Betsy_Clothes_Under

        "Варианты колготок и чулок":
            menu:
                "Сними [get_clothing_name(BetsyX.Hose_key, vin)]." if BetsyX.Hose:
                                $ BetsyX.FaceChange("sexy", 1)
                                if BetsyX.SeenPanties and BetsyX.Panties and ApprovalCheck(BetsyX, 500, TabM=5):
                                    ch_b "Хорошо."
                                elif BetsyX.SeenPussy and ApprovalCheck(BetsyX, 900, TabM=4):
                                    ch_b "Хорошо."
                                elif ApprovalCheck(BetsyX, 1300, TabM=2) and BetsyX.Panties:
                                    ch_b "Ладно, ради тебя. . ."
                                elif ApprovalCheck(BetsyX, 700) and not BetsyX.Panties:
                                    call Betsy_NoPantiesOn
                                    if not _return and not BetsyX.Panties:
                                        if not ApprovalCheck(BetsyX, 1500):
                                            call Display_DressScreen(BetsyX)
                                            if not _return:
                                                return #jump Betsy_Clothes
                                        else:
                                                return #jump Betsy_Clothes
                                else:
                                    call Display_DressScreen(BetsyX)
                                    if not _return:
                                        ch_b "Я бы предпочла этого не делать при тебе."
                                        if not BetsyX.Panties:
                                                ch_b "Боюсь, на мне нет трусиков. . ."
                                        return #jump Betsy_Clothes
                                $ BetsyX.Hose = 0

                "Чулки дополнили бы твой образ." if BetsyX.Hose != "stockings":
                                $ BetsyX.Hose = "stockings"
                "Колготки дополнили бы твой образ." if BetsyX.Hose != "pantyhose" and "pantyhose" in BetsyX.Inventory:
                                $ BetsyX.Hose = "pantyhose"
                "Рваные колготки дополнили бы твой образ." if BetsyX.Hose != "ripped pantyhose" and "ripped pantyhose" in BetsyX.Inventory:
                                $ BetsyX.Hose = "ripped pantyhose"
#                "The black tights would look good with that." if BetsyX.Hose != "tights":
#                                $ BetsyX.Hose = "tights"
#                "The ripped tights would look good with that." if BetsyX.Hose != "ripped tights" and "ripped tights" in BetsyX.Inventory:
#                                $ BetsyX.Hose = "ripped tights"
                "Чулки и пояс с подвязками дополнили бы твой образ." if BetsyX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in BetsyX.Inventory:
                                $ BetsyX.Hose = "stockings and garterbelt"
                "Может, наденешь только пояс с подвязками?" if BetsyX.Hose != "garterbelt" and "stockings and garterbelt" in BetsyX.Inventory:
                                $ BetsyX.Hose = "garterbelt"
                "Синие носки дополнили бы твой образ." if BetsyX.Hose != "socks":
                                $ BetsyX.Hose = "socks"
                "Неважно":
                        pass
            return #jump Betsy_Clothes_Under

        #Panties
        "Низ":
            menu:
                "Ты должна снять [get_clothing_name(BetsyX.Panties_key, vin)]. . ." if BetsyX.Panties:
                        $ BetsyX.FaceChange("bemused", 1)
                        if ApprovalCheck(BetsyX, 900) and (BetsyX.Legs or (BetsyX.SeenPussy and not BetsyX.Taboo)):
                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                                if ApprovalCheck(BetsyX, 850, "L"):
                                        ch_b "Хорошо. . ."
                                elif ApprovalCheck(BetsyX, 500, "O"):
                                        ch_b "Конечно."
                                elif ApprovalCheck(BetsyX, 350, "I"):
                                        ch_b "Боже. . ."
                                else:
                                        ch_b "Пожалуй."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(BetsyX, 1100, "LI", TabM=3) and BetsyX.Love > BetsyX.Inbt:
                                        ch_b "Боюсь, я не хочу делать из себя посмешище. . ."
                                elif ApprovalCheck(BetsyX, 700, "OI", TabM=3) and BetsyX.Obed > BetsyX.Inbt:
                                        ch_b "Хорошо. . ."
                                elif ApprovalCheck(BetsyX, 600, "I", TabM=3):
                                        ch_b "Хммм. . ."
                                elif ApprovalCheck(BetsyX, 1300, TabM=3):
                                        ch_b "Ладно. . ."
                                else:
                                        call Display_DressScreen(BetsyX)
                                        if not _return:
                                            $ BetsyX.FaceChange("surprised")
                                            $ BetsyX.Brows = "angry"
                                            if BetsyX.Taboo > 20:
                                                ch_b "Здесь слишком людно."
                                            else:
                                                if not Player.Male:
                                                    ch_b "Ты далеко не такая милая, как ты думаешь, [BetsyX.Petname]!"
                                                else:
                                                    ch_b "Ты далеко не такой милый, как ты думаешь, [BetsyX.Petname]!"
                                            return #jump Betsy_Clothes
                        $ Line = get_clothing_name(BetsyX.Panties_key, vin)
                        $ BetsyX.Panties = 0
                        if Line == "swimsuit":
                                "Сначала она снимает верх купальника."
                                if not renpy.showing('DressScreen'):
                                    call Girl_First_Topless(BetsyX)
                                "Затем она снимает его полностью."
                                if not renpy.showing('DressScreen'):
                                    call Girl_First_Bottomless(BetsyX,1)
                        if not BetsyX.Legs:
                            "Она снимает [Line] и бросает их на пол."
                            if not renpy.showing('DressScreen'):
                                    call Girl_First_Bottomless(BetsyX)
                        elif ApprovalCheck(BetsyX, 1200, TabM=4):
                            $ Trigger = BetsyX.Legs
                            $ BetsyX.Legs = 0
                            pause 0.5
                            $ BetsyX.Legs = Trigger
                            "Она снимает [get_clothing_name(BetsyX.Legs_key, vin)] и [Line], затем снова надевает [get_clothing_name(BetsyX.Legs_key, vin)]."
                            $ Trigger = 1
                            call Girl_First_Bottomless(BetsyX,1)
                        elif BetsyX.Legs == "skirt":
                            "Она залезает под юбку и стягивает [Line]."
                        else:
                            $ BetsyX.Blush = 1
                            "Она на мгновение отходит, а затем возвращается."
                            $ BetsyX.Blush = 0
                        $ Line = 0

                "Почему бы тебе вместо этих не надеть синие трусики?" if BetsyX.Panties and BetsyX.Panties != "blue panties":
                        if ApprovalCheck(BetsyX, 1100, TabM=3):
                                ch_b "Ох, хорошо."
                                $ BetsyX.Panties = "blue panties"
                        else:
                                call Display_DressScreen(BetsyX)
                                if not _return:
                                        ch_b "Прошу, не думай о моих трусиках."
                                else:
                                        $ BetsyX.Panties = "blue panties"

                "Почему бы тебе вместо этих не надеть кружевные трусики?" if "lace panties" in BetsyX.Inventory and BetsyX.Panties and BetsyX.Panties != "lace panties":
                        if ApprovalCheck(BetsyX, 1300, TabM=3):
                                ch_b "Ох, хорошо."
                                $ BetsyX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(BetsyX)
                                if not _return:
                                        ch_b "Прошу, не думай о моих трусиках."
                                else:
                                        $ BetsyX.Panties = "lace panties"

                "Примерь купальник" if (BetsyX.Chest != "swimsuit" or BetsyX.Panties != "swimsuit") and "swimsuit" in BetsyX.Inventory:
                        ch_p "Мне нравится твой купальник."
                        $ BetsyX.Swim[0] = 1
                        if bg_current == "bg pool":
                                ch_b "Хорошо."
                                $ BetsyX.Chest = "swimsuit"
                                $ BetsyX.Panties = "swimsuit"
                        else:
                                if BetsyX.SeenChest or ApprovalCheck(BetsyX, 1000, TabM=2):
                                    ch_b "Хорошо."
                                    $ BetsyX.Chest = "swimsuit"
                                    $ BetsyX.Panties = "swimsuit"
                                else:
                                    call Display_DressScreen(BetsyX)
                                    if not _return:
                                            ch_b "Боюсь, что такой наряд не подходит для данного места. . ."
                                    else:
                                            $ BetsyX.Chest = "swimsuit"
                                            $ BetsyX.Panties = "swimsuit"

                "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not BetsyX.Panties:
                        $ BetsyX.FaceChange("bemused", 1)
                        if BetsyX.Legs and (BetsyX.Love+BetsyX.Obed) <= (2 * BetsyX.Inbt):
                            $ BetsyX.Mouth = "smile"
                            ch_b "Мне бы не хотелось этого делать. . ."
                            menu:
                                "Ну ладно.":
                                    return #jump Betsy_Clothes
                                "Я настаиваю, надевай.":
                                    if (BetsyX.Love+BetsyX.Obed) <= (1.5 * BetsyX.Inbt):
                                        $ BetsyX.FaceChange("angry", Eyes="side")
                                        ch_b "Я сама решу, что мне следует делать, а что нет."
                                        return #jump Betsy_Clothes
                                    else:
                                        $ BetsyX.FaceChange("sadside")
                                        ch_b "Ох, хорошо."
                        else:
                            ch_b "Пожалуй. . ."
                        menu:
                            extend ""
                            "Как насчет синих?":
                                    ch_b "Ох, хорошо."
                                    $ BetsyX.Panties = "blue panties"
                            "Как насчет купальника?" if "swimsuit" in BetsyX.Inventory:
                                    ch_b "Ох, хорошо."
                                    $ BetsyX.Swim[0] = 1
                                    $ BetsyX.Chest  = "swimsuit"
                                    $ BetsyX.Panties  = "swimsuit"
                            "Как насчет кружевных?" if "lace panties" in BetsyX.Inventory:
                                    ch_b "Ох, хорошо."
                                    $ BetsyX.Panties  = "lace panties"
                "Неважно":
                    pass
            return #jump Betsy_Clothes_Under
        "Неважно":
            pass
    return #jump Betsy_Clothes
    #End of Betsy Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Betsy_Clothes_Misc:
        #Misc
        "Сухие волосы" if BetsyX.Hair == "wet" or BetsyX.Hair == "wetlong":
                ch_p "Тебе идут сухие волосы."
                if ApprovalCheck(BetsyX, 600):
                    ch_b "Ох, правда?"
                    if BetsyX.Hair == "wet":
                        $ BetsyX.Hair = "short"
                    else:
                        $ BetsyX.Hair = "long"
                else:
                    ch_b "Я не уверена, думаю, меня и так все устраивает."

        "Короткие волосы" if BetsyX.Hair != "short" and BetsyX.Hair != "wet":
                ch_p "Мне кажется, тебе идет короткая стрижка."
                if ApprovalCheck(BetsyX, 600):
                    ch_b "Ох, правда?"
                    "Она на минутку удаляется."
                    $ BetsyX.Hair = "short"
                else:
                    ch_b "Мне больше нравится моя нынешняя прическа."
        "Длинные волосы" if BetsyX.Hair != "long" and BetsyX.Hair != "wetlong":
                ch_p "Мне кажется, тебе идут длинные волосы."
                if ApprovalCheck(BetsyX, 600):
                    ch_b "Ох, правда?"
                    "Она на минутку удаляется."
                    $ BetsyX.Hair = "long"
                else:
                    ch_b "Мне больше нравится моя нынешняя прическа."

        "Влажные волосы" if BetsyX.Hair != "wet" and BetsyX.Hair != "wetlong":
                ch_p "Тебе стоит увлажнить волосы."
                if ApprovalCheck(BetsyX, 800):
                    ch_b "Ох, правда?"
                    if BetsyX.Hair == "long":
                        $ BetsyX.Hair = "wetlong"
                    else:
                        $ BetsyX.Hair = "wet"
                    "Она отходит на минуту и вскоре возвращается."
                    ch_b "Так?"
                else:
                    ch_b "Ох, это требует слишком больших усилий."

        "Светлые волосы" if BetsyX.Hair != "blonde" and "halloween" in BetsyX.History:
                ch_p "Мне кажется, тебе снова стоит стать блондинкой."
                if ApprovalCheck(BetsyX, 600):
                    ch_b "О, правда?"
                    "Она отходит на минутку."
                    $ BetsyX.Hair = "blonde"
                else:
                    ch_b "Мне больше нравится моя нынешний цвет."

        "Отрасти волосы на лобке" if not BetsyX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может, отрастишь?"
                call expression BetsyX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in BetsyX.Todo:
                        $ BetsyX.FaceChange("bemused", 1)
                        ch_b "Боюсь, за день это невозможно осуществить."
                else:
                    $ BetsyX.FaceChange("bemused", 1)
                    if ApprovalCheck(BetsyX, 1000, TabM=0):
                            ch_b "Ладно, пожалуй, можно. . ."
                    else:
                            $ BetsyX.FaceChange("surprised")
                            $ BetsyX.Brows = "angry"
                            ch_b ". . . какое тебе дело до этого?"
                            return #jump Betsy_Clothes
                    $ BetsyX.Todo.append("pubes")
                    $ BetsyX.PubeC = 6
        "Побрей лобок" if BetsyX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression BetsyX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ BetsyX.FaceChange("bemused", 1)
                if "shave" in BetsyX.Todo:
                        ch_b "Я займусь этим попозже."
                else:
                    if ApprovalCheck(BetsyX, 1100, TabM=0):
                        ch_b "Ладно, пожалуй, можно. . ."
                    else:
                        $ BetsyX.FaceChange("surprised")
                        $ BetsyX.Brows = "angry"
                        ch_b ". . . какое тебе дело до этого?"
                        return #jump Betsy_Clothes
                    $ BetsyX.Todo.append("shave")

        "Пирсинг. [[Сначала посмотрите, как она выглядит без него] (locked)" if not BetsyX.SeenPussy and not BetsyX.SeenChest:
            pass

        "Надень пирсинг-кольца" if BetsyX.Pierce != "ring" and (BetsyX.SeenPussy or BetsyX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсингом-кольцами."
                if "ring" in BetsyX.Todo:
                    ch_b "Я займусь этим попозже."
                else:
                    $ BetsyX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(BetsyX, 1150, TabM=0)
                    if ApprovalCheck(BetsyX, 900, "L", TabM=0) or (Approval and BetsyX.Love > 2* BetsyX.Obed):
                        ch_b "Ты думаешь, он мне подойдет?"
                    elif ApprovalCheck(BetsyX, 600, "I", TabM=0) or (Approval and BetsyX.Inbt > BetsyX.Obed):
                        ch_b "Я уже какое-то время подумывала о нем."
                    elif ApprovalCheck(BetsyX, 500, "O", TabM=0) or Approval:
                        ch_b "Если тебе так этого хочется, [BetsyX.Petname]."
                    else:
                        $ BetsyX.FaceChange("surprised")
                        $ BetsyX.Brows = "angry"
                        ch_b "Меня это не интересует, [BetsyX.Petname]."
                        return #jump Betsy_Clothes
                    $ BetsyX.Todo.append("ring")

        "Надень пирсинг-штанги" if BetsyX.Pierce != "barbell" and (BetsyX.SeenPussy or BetsyX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in BetsyX.Todo:
                    ch_b "Я займусь этим попозже."
                else:
                    $ BetsyX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(BetsyX, 1150, TabM=0)
                    if ApprovalCheck(BetsyX, 900, "L", TabM=0) or (Approval and BetsyX.Love > 2 * BetsyX.Obed):
                        ch_b "Ты думаешь, он мне подойдет?"
                    elif ApprovalCheck(BetsyX, 600, "I", TabM=0) or (Approval and BetsyX.Inbt > BetsyX.Obed):
                        ch_b "Я уже какое-то время подумывала о нем."
                    elif ApprovalCheck(BetsyX, 500, "O", TabM=0) or Approval:
                        ch_b "Если тебе так этого хочется, [BetsyX.Petname]."
                    else:
                        $ BetsyX.FaceChange("surprised")
                        $ BetsyX.Brows = "angry"
                        ch_b "Меня это не интересует, [BetsyX.Petname]."
                        return #jump Betsy_Clothes
                    $ BetsyX.Todo.append("barbell")

        "Сними пирсинг" if BetsyX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ BetsyX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(BetsyX, 1350, TabM=0)
                if ApprovalCheck(BetsyX, 950, "L", TabM=0) or (Approval and BetsyX.Love > BetsyX.Obed):
                    ch_e "Что ж, если тебе не нравится. . ."
                elif ApprovalCheck(BetsyX, 700, "I", TabM=0) or (Approval and BetsyX.Inbt > BetsyX.Obed):
                    ch_b "Мне он тоже не особо нравился."
                elif ApprovalCheck(BetsyX, 600, "O", TabM=0) or Approval:
                    ch_b "Хорошо."
                else:
                    $ BetsyX.FaceChange("surprised")
                    $ BetsyX.Brows = "angry"
                    ch_b "Нет, мне он нравится. . ."
                    return #jump Betsy_Clothes
                $ BetsyX.Pierce = 0

#        "Medallion choker" if BetsyX.Neck != "leash choker":
#                ch_p "Why don't you try on that medallion choker?"
#                ch_b "Ok. . ."
#                $ BetsyX.Neck = "leash choker"
#        "Remove Necklace" if BetsyX.Neck:
#                ch_p "Maybe go without a necklace."
#                ch_b "Ok. . ."
#                $ BetsyX.Neck = 0

#        "Add Suspenders" if BetsyX.Acc != "suspenders" and BetsyX.Acc != "suspenders2" and "halloween" in BetsyX.History:
#                $ BetsyX.Acc = "suspenders"
#        "Remove Suspenders" if BetsyX.Acc == "suspenders" or BetsyX.Acc == "suspenders2":
#                $ BetsyX.Acc = 0

#        "Shift Suspenders" if BetsyX.Acc == "suspenders" or BetsyX.Acc == "suspenders2":
#                $ BetsyX.Acc = "suspenders" if BetsyX.Acc == "suspenders2" else "suspenders2"

        "Перчатки вкл\выкл":
                if not BetsyX.Arms:
                        ch_p "Почему бы тебе не надеть перчатки обратно?"
                else:
                        ch_p "Давай обойдемся без перчаток."
                ch_b "Ладно."
                $ BetsyX.Arms = 0 if BetsyX.Arms else "gloves"

        "Шарф вкл\выкл":
                if BetsyX.Acc != "scarf":
                        ch_p "Почему бы тебе не надеть шарф обратно?"
                else:
                        ch_p "Может, снимешь шарф?"
                ch_b "Ладно."
                $ BetsyX.Acc = 0 if BetsyX.Acc else "scarf"
        "Неважно":
            pass
    return #jump Betsy_Clothes
    #End of Betsy Misc Wardrobe

return
#End Betsy Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
