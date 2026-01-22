# star Gwen chat interface
#Gwen Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Gwen_Relationship: #rkeljsvg
    while True:
        menu:
            ch_g "О чем ты хочешь поговорить?"
            "Хочешь стать моей девушкой?" if GwenX not in Player.Harem and "ex" not in GwenX.Traits:
                    $ GwenX.DailyActions.append("relationship")
                    if "asked boyfriend" in GwenX.DailyActions and "angry" in GwenX.DailyActions:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Перестань спрашивать."
                            return
                    elif "asked boyfriend" in GwenX.DailyActions:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Все еще нет."
                            return
                    elif GwenX.Break[0]:
                            $ GwenX.FaceChange("angry", 1)
                            if not Player.Male:
                                ch_g "Нет, если ты не решила остепениться."
                            else:
                                ch_g "Нет, если ты не решил остепениться."
                            if Player.Harem:
                                    $ GwenX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "Это уже в прошлом."

                    $ GwenX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "GwenYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_g "Как другие относятся к этому, [GwenX.Petname]?"
                        else:
                            ch_g "Как [Player.Harem[0].Name] относится к этому, [GwenX.Petname]?"
                        return

                    if GwenX.Event[5]:
                            $ GwenX.FaceChange("bemused", 1)
                            if not Player.Male:
                                ch_g "Когда я спрашивала, ты ответила \"нет\". . ."
                            else:
                                ch_g "Когда я спрашивала, ты ответил \"нет\". . ."
                    else:
                            $ GwenX.FaceChange("surprised", 2)
                            ch_g "А? . ."
                            $ GwenX.FaceChange("smile", 1)

                    call Gwen_OtherWoman

                    if GwenX.Love >= 800:
                            $ GwenX.FaceChange("surprised", 1)
                            $ GwenX.Mouth = "smile"
                            if not GwenX.Event[5]:
                                    $ GwenX.Statup("Love", 200, 10)
                                    call Gwen_BF
                                    return
                            $ GwenX.Statup("Love", 200, 40)
                            ch_g "Конечно!"
                            if "boyfriend" not in GwenX.Petnames:
                                    $ GwenX.Petnames.append("boyfriend")
                            if "GwenYes" in Player.Traits:
                                    $ Player.Traits.remove("GwenYes")
                            $ Player.Harem.append(GwenX)
                            call Harem_Initiation
                            "[GwenX.Name] хватает вас и крепко целует."
                            $ GwenX.FaceChange("kiss", 1)
                            $ GwenX.Kissed += 1
                    elif GwenX.Obed >= 500:
                            $ GwenX.FaceChange("perplexed")
                            ch_g "Я не уверена, что хочу \"встречаться\". . ."
                    elif GwenX.Inbt >= 500:
                            $ GwenX.FaceChange("smile")
                            ch_g "Нет, нам и без этого очень весело."
                    else:
                            $ GwenX.FaceChange("perplexed", 1)
                            ch_g "Воу, притормози, [GwenX.Petname]."

            "Может, начнем все сначала?" if "ex" in GwenX.Traits:
                    $ GwenX.DailyActions.append("relationship")
                    if "asked boyfriend" in GwenX.DailyActions and "angry" in GwenX.DailyActions:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Перестань спрашивать."
                            return
                    elif "asked boyfriend" in GwenX.DailyActions:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Все еще не хочу."
                            return

                    $ GwenX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "GwenYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_g "Как другие относятся к этому, [GwenX.Petname]?"
                            else:
                                ch_g "Как [Player.Harem[0].Name] относится к этому, [GwenX.Petname]?"
                            return

                    $ Cnt = 0
                    call Gwen_OtherWoman

                    if GwenX.Love >= 800:
                            $ GwenX.FaceChange("surprised", 1)
                            $ GwenX.Mouth = "smile"
                            $ GwenX.Statup("Love", 90, 5)
                            ch_g "Ну. . . хорошо, мы можем попробовать."
                            if "boyfriend" not in GwenX.Petnames:
                                        $ GwenX.Petnames.append("boyfriend")
                            $ GwenX.Traits.remove("ex")
                            if "GwenYes" in Player.Traits:
                                    $ Player.Traits.remove("GwenYes")
                            $ Player.Harem.append(GwenX)
                            call Harem_Initiation
                            "[GwenX.Name] притягивает вас к себе и крепко целует."
                            $ GwenX.FaceChange("kiss", 1)
                            $ GwenX.Kissed += 1
                    elif GwenX.Love >= 600 and ApprovalCheck(GwenX, 1500):
                            $ GwenX.FaceChange("smile", 1)
                            $ GwenX.Statup("Love", 90, 5)
                            ch_g "Эм, ладно, наверное."
                            if "boyfriend" not in GwenX.Petnames:
                                    $ GwenX.Petnames.append("boyfriend")
                            $ GwenX.Traits.remove("ex")
                            if "GwenYes" in Player.Traits:
                                    $ Player.Traits.remove("GwenYes")
                            $ Player.Harem.append(GwenX)
                            call Harem_Initiation
                            $ GwenX.FaceChange("kiss", 1)
                            "[GwenX.Name] дарит вам легкий поцелуй."
                            $ GwenX.FaceChange("sly", 1)
                            $ GwenX.Kissed += 1
                    elif GwenX.Obed >= 500:
                            $ GwenX.FaceChange("sad")
                            ch_g "Эх, у нас ничего не сложилось. . ."
                    elif GwenX.Inbt >= 500:
                            $ GwenX.FaceChange("perplexed")
                            ch_g "Это испортит всё веселье."
                    else:
                            $ GwenX.FaceChange("sadside", 1)
                            if not Player.Male:
                                ch_g "Я не уверена, ты разбила мне сердце. . ."
                            else:
                                ch_g "Я не уверена, ты разбил мне сердце. . ."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if GwenX in Player.Harem:
                            call AskDateOther

            "Думаю, мы должны расстаться." if GwenX in Player.Harem:
                            if "breakup talk" in GwenX.RecentActions:
                                    ch_g "Хватит спрашивать меня об этом."
                            elif "breakup talk" in GwenX.DailyActions:
                                    ch_g "Опять несешь этот бред?"
                                    ch_g "Угомонись уже, [GwenX.Petname]."
                            else:
                                    call Breakup(GwenX)

            "О разговоре, который у нас был ранее. . .":
                menu:
                    "Помнишь, ты признавалась мне в любви. . ." if "lover" not in GwenX.Traits and GwenX.Event[6] >= 20 and GwenX.Event[6] != 23:
                            call Gwen_Love_Redux

                    "Помнишь, ты рассказывала мне о себе. . ." if "lover" not in GwenX.Traits and GwenX.Event[6] == 23:
                            call Gwen_Love_Redux

#                    "You said you wanted me to be more in control?" if "sir" not in GwenX.Petnames and "sir" in GwenX.History:
#                            if "asked sub" in GwenX.RecentActions:
#                                    ch_g "Stop asking about this."
#                            elif "asked sub" in GwenX.DailyActions:
#                                    ch_g "Give it a rest, [GwenX.Petname]."
#                            else:
#                                    call Gwen_Sub_Asked
#                    "You said you wanted me to be your [Terms['master']]?" if "master" not in GwenX.Petnames and "master" in GwenX.History:
#                            if "asked sub" in GwenX.RecentActions:
#                                    ch_g "Stop asking about this."
#                            elif "asked sub" in GwenX.DailyActions:
#                                    ch_g "Give it a rest, [GwenX.Petname]."
#                            else:
#                                    call Gwen_Sub_Asked
                    "Неважно":
                            pass

            "Неважно":
                return

    return

label Gwen_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((GwenX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ GwenX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_g "Но я слышала, что ты сейчас с [Player.Harem[0].Name_tvo], и у тебя, вроде как, целый гарем?"
    else:
        ch_g "Но я слышала, что ты сейчас с [Player.Harem[0].Name_tvo], так?"
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "GwenYes" in Player.Traits:
                if ApprovalCheck(GwenX, 1800, Bonus = Cnt):
                        $ GwenX.FaceChange("smile", 1)
                        if GwenX.Love >= GwenX.Obed:
                                ch_g "Ну, думаю, я могу вступить в ваш клуб."
                        elif GwenX.Obed >= GwenX.Inbt:
                                ch_g "Ладно, думаю, мне лучше вступить в ваш клуб."
                        else:
                                ch_g "Эм, почему бы и нет."
                else:
                        $ GwenX.FaceChange("angry", 1)
                        ch_g "Ха, я совсем не удивлена, но это не значит, что я согласна."
                        $ renpy.pop_call()
                        #This causes it to jump past the previous menu on the return

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "GwenYes" not in Player.Traits and not Player.Male:
                if ApprovalCheck(GwenX, 1800, Bonus = Cnt):
                        $ GwenX.FaceChange("smile", 1)
                        if GwenX.Love >= GwenX.Obed:
                            ch_g "Тогда я могла бы присоединиться к вам. . ."
                        elif GwenX.Obed >= GwenX.Inbt:
                            ch_g "Ну, тогда я, может быть, соглашусь."
                        else:
                            ch_g "Ну конечно, почему бы и нет."
                        ch_g "Сходи и спроси, расскажешь потом мне, как все прошло."
                else:
                        $ GwenX.FaceChange("angry", 1)
                        ch_g "Ха, я совсем не удивлена, но это не значит, что я согласна."
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "GwenYes" not in Player.Traits and Player.Male:
                if ApprovalCheck(GwenX, 1800, Bonus = Cnt):
                        $ GwenX.FaceChange("smile", 1)
                        if GwenX.Love >= GwenX.Obed:
                            ch_g "Тогда я могла бы присоединиться к вам. . ."
                        elif GwenX.Obed >= GwenX.Inbt:
                            ch_g "Ну, тогда я, может быть, соглашусь."
                        else:
                            ch_g "Ну конечно, почему бы и нет."
                        ch_g "Сходи и спроси, расскажешь потом мне, как все прошло."
                else:
                        $ GwenX.FaceChange("angry", 1)
                        ch_g "Ха, я совсем не удивлена, но это не значит, что я согласна."
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
                if not ApprovalCheck(GwenX, 1800, Bonus = -Cnt): #checks if Gwen likes you more than the other girl
                        $ GwenX.FaceChange("angry", 1)
                        if not ApprovalCheck(GwenX, 1800):
                                ch_g "Мне на ее месте было бы больно."
                        else:
                                ch_g "Остынь."
                        $ renpy.pop_call()
                else:
                        $ GwenX.FaceChange("smile", 1)
                        if GwenX.Love >= GwenX.Obed:
                                ch_g "Ну, тогда я буду держать все в секрете. . ."
                        elif GwenX.Obed >= GwenX.Inbt:
                                ch_g "Ну, если ты этого так хочешь. . ."
                        else:
                                ch_g "Эм, почему бы и нет."
                        $ GwenX.Traits.append("downlow")

        "Я могу порвать с ней.":
                    $ GwenX.FaceChange("sad")
                    ch_g "Хорошо, расскажи потом, как все прошло."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ GwenX.FaceChange("sad")
                    ch_g "Ага."
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ GwenX.FaceChange("sad")
                    ch_g "Ага."
                    $ renpy.pop_call()

    return


label Gwen_About(Check=0): #rkeljsvg
    if Check not in TotalGirls:
            ch_g "Кто это?"
            return
    ch_g "Что я думаю о ней? Ну. . ."
    if Check == RogueX:
            if "poly Rogue" in GwenX.Traits:
                ch_g "Мы сейчас встречаемся! Разве это не удивительно?!"
            elif GwenX.LikeRogue >= 900:
                ch_g "У нее разноцветные волосы. . . даже внизу!"
            elif GwenX.LikeRogue >= 800:
                ch_g "Она очень сексуальная, правда?"
            elif GwenX.LikeRogue >= 700:
                ch_g "Она очень хорошо двигается."
            elif GwenX.LikeRogue >= 600:
                ch_g "Мне нравится проводить время с -Роуг-."
            elif GwenX.LikeRogue >= 500:
                ch_g "Мы мало общаемся."
            elif GwenX.LikeRogue >= 400:
                ch_g "Не думаю, что мы ладим."
            elif GwenX.LikeRogue >= 300:
                ch_g "Она меня бесит."
            else:
                ch_g "Фу."
    elif Check == KittyX:
            if "poly Kitty" in GwenX.Traits:
                ch_g "Мы сейчас встречаемся! Разве это не удивительно?!"
            elif GwenX.LikeKitty >= 900:
                ch_g "Она очень приятно пахнет!"
            elif GwenX.LikeKitty >= 800:
                ch_g "Она такая милая!"
            elif GwenX.LikeKitty >= 700:
                ch_g "Она отлично танцует."
            elif GwenX.LikeKitty >= 600:
                ch_g "Она -такая- крутая."
            elif GwenX.LikeKitty >= 500:
                ch_g "Мы не так много общались."
            elif GwenX.LikeKitty >= 400:
                ch_g "Не думаю, что мы ладим."
            elif GwenX.LikeKitty >= 300:
                ch_g "Меня бесит ее слово паразит бесит!"
            else:
                ch_g "Фу."
    elif Check == LauraX:
            if "poly Laura" in GwenX.Traits:
                ch_g "Мы сейчас встречаемся! Разве это не удивительно?!"
            elif GwenX.LikeLaura >= 900:
                ch_g "Она удивительная."
            elif GwenX.LikeLaura >= 800:
                ch_g "Она в отличной форме, как Джейн Фостер, а ее я видела в живую!"
            elif GwenX.LikeLaura >= 700:
                ch_g "Она изматывает меня на тренировках. . . но мне нравится. . ."
            elif GwenX.LikeLaura >= 600:
                ch_g "Она такая классная."
            elif GwenX.LikeLaura >= 500:
                ch_g "Мы не часто общались."
            elif GwenX.LikeLaura >= 400:
                ch_g "Не думаю, что мы ладим."
            elif GwenX.LikeLaura >= 300:
                ch_g "Она меня бесит."
            else:
                ch_g "Фу."
    elif Check == EmmaX:
            if "poly Emma" in GwenX.Traits:
                ch_g "Мы сейчас встречаемся! Разве это не удивительно?!"
            elif GwenX.LikeEmma >= 900:
                ch_g "Она словно перьевая подушка. . ."
                ch_g ". . ."
                ch_g "Подожди, а какой был вопрос?"
            elif GwenX.LikeEmma >= 800:
                ch_g "Она очень здорово выглядит. . ."
            elif GwenX.LikeEmma >= 700:
                ch_g "Она не такая стерва, как может показаться на первый взгляд."
                ch_g "Она гораздо лучше."
            elif GwenX.LikeEmma >= 600:
                ch_g "Она помогла мне наверстать упущенное."
            elif GwenX.LikeEmma >= 500:
                ch_g "Она классная."
                ch_g "И не такая стерва, как может показаться на первый взгляд."
            elif GwenX.LikeEmma >= 400:
                ch_g "Не думаю, что мы ладим."
            elif GwenX.LikeEmma >= 300:
                ch_g "Она меня бесит."
            else:
                ch_g "Фу."
    elif Check == JeanX:
            if "poly Jean" in GwenX.Traits:
                ch_g "Думаю, мы теперь встречаемся."
            elif GwenX.LikeJean >= 900:
                ch_g "\"Джин практически совершенна во всех отношениях\". . ."
            elif GwenX.LikeJean >= 800:
                ch_g "Она первоклассная стерва, но у нее есть все, что для этого нужно. . ."
            elif GwenX.LikeJean >= 700:
                ch_g "Она. . . лучше, чем кажется."
            elif GwenX.LikeJean >= 600:
                ch_g "Я начинаю привыкать к ее взгляду?"
            elif GwenX.LikeJean >= 500:
                ch_g "Она, вроде как, лучше, чем кажется."
            elif GwenX.LikeJean >= 400:
                ch_g "Не думаю, что мы ладим."
            elif GwenX.LikeJean >= 300:
                ch_g "Думаю, она здесь, чтобы издеваться надо мной."
            else:
                ch_g "Она сучка."
                if not Player.Male:
                    ch_g "Ну, ты и сама знаешь."
                else:
                    ch_g "Ну, ты и сам знаешь."
    elif Check == StormX:
            if "poly Storm" in GwenX.Traits:
                ch_g "Мы сейчас встречаемся! Разве это не удивительно?!"
            elif GwenX.LikeStorm >= 900:
                if not Player.Male:
                    ch_g "Ты и сама прекрасно ее знаешь. . ."
                else:
                    ch_g "Ты и сам прекрасно ее знаешь. . ."
            elif GwenX.LikeStorm >= 800:
                ch_g "Она. . . впечатляет. . ."
            elif GwenX.LikeStorm >= 700:
                ch_g "Я не могу поверить, что могу смотреть на Шторм весь день."
            elif GwenX.LikeStorm >= 600:
                ch_g "Она очень приветливая!"
            elif GwenX.LikeStorm >= 500:
                ch_g "Не думаю, что мы ладим."
            elif GwenX.LikeStorm >= 400:
                ch_g "Она может быть злой."
            elif GwenX.LikeStorm >= 300:
                ch_g "Она меня бесит."
            else:
                ch_g "Фу."
    elif Check == JubesX:
            if "poly Jubes" in GwenX.Traits:
                ch_g "Мы сейчас встречаемся! Разве это не удивительно?!"
            elif GwenX.LikeJubes >= 900:
                ch_g "Она кусается. . ."
            elif GwenX.LikeJubes >= 800:
                ch_g "Она такая милая с этими своими малюсенькими клыками. . ."
            elif GwenX.LikeJubes >= 700:
                ch_g "Мы много раз ходили в торговый центр."
            elif GwenX.LikeJubes >= 600:
                ch_g "Она такая классная."
            elif GwenX.LikeJubes >= 500:
                ch_g "Мы не часто общались."
            elif GwenX.LikeJubes >= 400:
                ch_g "Не думаю, что мы ладим."
            elif GwenX.LikeJubes >= 300:
                ch_g "Она меня бесит."
            else:
                ch_g "Фу."
    elif Check == BetsyX:
            if "poly Betsy" in GwenX.Traits:
                ch_g "Мы сейчас встречаемся! Разве это не удивительно?!"
            elif GwenX.LikeBetsy >= 900:
                ch_g "Она в ужасно хорошей форме!"
            elif GwenX.LikeBetsy >= 800:
                ch_g "Она очень сексуальная!"
            elif GwenX.LikeBetsy >= 700:
                ch_g "Она очень стильная."
            elif GwenX.LikeBetsy >= 600:
                ch_g "Ее не всегда получается понять из-за акцента!"
            elif GwenX.LikeBetsy >= 500:
                ch_g "Нам толком не удалось пообщаться."
            elif GwenX.LikeBetsy >= 400:
                ch_g "Не думаю, что мы ладим."
            elif GwenX.LikeBetsy >= 300:
                ch_g "Она меня бесит."
            else:
                ch_g "Фу."
    elif Check == DoreenX:
            if "poly Doreen" in GwenX.Traits:
                ch_g "Мы сейчас встречаемся! Разве это не удивительно?!"
            elif GwenX.LikeDoreen >= 900:
                ch_g "Она очень мягкая. . ."
            elif GwenX.LikeDoreen >= 800:
                ch_g "Она очень милая из-за этого неправильного прикуса. . ."
            elif GwenX.LikeDoreen >= 700:
                ch_g "Мы сошлись во вкусах."
            elif GwenX.LikeDoreen >= 600:
                ch_g "Она -такая- милая."
            elif GwenX.LikeDoreen >= 500:
                ch_g "Мы почти не общались."
            elif GwenX.LikeDoreen >= 400:
                ch_g "Не думаю, что мы ладим."
            elif GwenX.LikeDoreen >= 300:
                ch_g "Она меня бесит."
            else:
                ch_g "Фу."
    elif Check == WandaX:
            if "poly Wanda" in GwenX.Traits:
                ch_g "Мы теперь вместе! Разве это не удивительно?!"
            elif GwenX.LikeWanda >= 900:
                ch_g "Она от природы рыжая!"
                ch_g "Теперь. . . по-видимому."
            elif GwenX.LikeWanda >= 800:
                ch_g "Она очень привлекательная, правда?"
            elif GwenX.LikeWanda >= 700:
                ch_g "Она очень хорошо двигается."
            elif GwenX.LikeWanda >= 600:
                ch_g "Так круто проводить время с -Вандой-."
            elif GwenX.LikeWanda >= 500:
                ch_g "Мы почти не общались."
            elif GwenX.LikeWanda >= 400:
                ch_g "Я не думаю, что мы поладим."
            elif GwenX.LikeWanda >= 300:
                ch_g "Она раздражает."
            else:
                ch_g "Фу."
    else:
                ch_g "Спойлеры!"
    return
#End Gwen_AboutEmma

label Gwen_Monogamy:
        #called from Gwen_Settings to ask her not to hook up with other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in GwenX.Traits:
                    if GwenX.Thirst >= 60 and not ApprovalCheck(GwenX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ GwenX.FaceChange("sly",1)
                            if "mono" not in GwenX.DailyActions:
                                    $ GwenX.Statup("Obed", 90, -2)
                            if not Player.Male:
                                ch_g "Я тебя услышала, но где была ты?"
                            else:
                                ch_g "Я тебя услышала, но где был ты?"
                            ch_g "Точно далеко от меня."
                            return
                    elif ApprovalCheck(GwenX, 1200, "LO", TabM=0) and GwenX.Love >= GwenX.Obed:
                            #she cares
                            $ GwenX.FaceChange("sly",1)
                            if "mono" not in GwenX.DailyActions:
                                    $ GwenX.Statup("Love", 90, 1)
                            ch_g "Ооох, ревнуешь?"
                            ch_g "Хорошо, я буду держаться подальше от других девушек. . ."
                            ch_g "С тебя должок."
                    elif ApprovalCheck(GwenX, 700, "O", TabM=0):
                            #she is obedient
                            $ GwenX.FaceChange("sly",1,Eyes="side")
                            ch_g "Что?"
                            ch_g "Ну ладно. . ."
                    else:
                            #she doesn't care
                            $ GwenX.FaceChange("sly",1)
                            ch_g "Ты шутишь? У меня тут свой фанфик, а ты не хочешь, чтобы я наслаждалась?"
                            return
                    if "mono" not in GwenX.DailyActions:
                            $ GwenX.Statup("Obed", 90, 3)
                    $ GwenX.AddWord(1,0,"mono") #Daily
                    $ GwenX.Traits.append("mono")
            "Не встречайся с другими девушками." if "mono" not in GwenX.Traits:
                    if ApprovalCheck(GwenX, 900, "O", TabM=0):
                            #she is obedient
                            $ GwenX.FaceChange("sly",1,Eyes="side")
                            ch_g "Хорошо."
                    elif GwenX.Thirst >= 60 and not ApprovalCheck(GwenX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ GwenX.FaceChange("sly",1)
                            if "mono" not in GwenX.DailyActions:
                                    $ GwenX.Statup("Obed", 90, -2)
                            if not Player.Male:
                                ch_g "Я тебя услышала, но где была ты?"
                            else:
                                ch_g "Я тебя услышала, но где был ты?"
                            ch_g "Точно далеко от меня."
                            return
                    elif ApprovalCheck(GwenX, 600, "O", TabM=0):
                            #she is obedient
                            $ GwenX.FaceChange("sly",1,Eyes="side")
                            ch_g "Хорошо, я буду держаться подальше от других девушек. . ."
                    elif ApprovalCheck(GwenX, 1400, "LO", TabM=0):
                            #she cares
                            $ GwenX.FaceChange("sly",1)
                            ch_g "Ооох, ревнуешь?"
                            ch_g "Хорошо, я буду держаться подальше от других девушек. . ."
                            ch_g "С тебя должок."
                    else:
                            #she doesn't care
                            $ GwenX.FaceChange("sly",1,Brows="confused")
                            ch_g "Ты шутишь? У меня тут свой фанфик, а ты не хочешь, чтобы я наслаждалась?"
                            return
                    if "mono" not in GwenX.DailyActions:
                            $ GwenX.Statup("Obed", 90, 3)
                    $ GwenX.AddWord(1,0,"mono") #Daily
                    $ GwenX.Traits.append("mono")
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in GwenX.Traits:
                    if ApprovalCheck(GwenX, 700, "O", TabM=0):
                            $ GwenX.FaceChange("sly",1,Eyes="side")
                            ch_g "Клево."
                    elif ApprovalCheck(GwenX, 800, "L", TabM=0):
                            $ GwenX.FaceChange("sly",1)
                            if not Player.Male:
                                ch_g "Хорошо, но. . . ты должна уделять мне немного внимания. . ."
                            else:
                                ch_g "Хорошо, но. . . ты должен уделять мне немного внимания. . ."
                    else:
                            $ GwenX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in GwenX.DailyActions:
                                    $ GwenX.Statup("Love", 90, -2)
                            ch_g "Ох, опять придется крутиться!"
                    if "mono" not in GwenX.DailyActions:
                            $ GwenX.Statup("Obed", 90, 3)
                    if "mono" in GwenX.Traits:
                            $ GwenX.Traits.remove("mono")
                    $ GwenX.AddWord(1,0,"mono") #Daily
            "Неважно.":
                pass
        return

# end Gwen monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Gwen_Jumped:
        #called from Gwen_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ GwenX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_g "Угу."
            "На будущее, можешь сначала спрашивать?" if "chill" not in GwenX.Traits:
                    if GwenX.Thirst >= 60 and not ApprovalCheck(GwenX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ GwenX.FaceChange("sly",1)
                            if "chill" not in GwenX.DailyActions:
                                    $ GwenX.Statup("Obed", 90, -2)
                            ch_g "Нет, если ты собираешься продолжать игнорировать меня. . ."
                            return
                    elif ApprovalCheck(GwenX, 1000, "LO", TabM=0) and GwenX.Love >= GwenX.Obed:
                            #she cares
                            $ GwenX.FaceChange("surprised",1)
                            if "chill" not in GwenX.DailyActions:
                                    $ GwenX.Statup("Love", 90, 1)
                            ch_g "Прости, это не хорошо, я знаю. . ."
                            $ GwenX.FaceChange("sly",1,Eyes="side")
                            ch_g "Я попробую. . ."
                    elif ApprovalCheck(GwenX, 500, "O", TabM=0):
                            #she is obedient
                            $ GwenX.FaceChange("sly",1,Eyes="side")
                            ch_g "Извини. . ."
                    else:
                            #she doesn't care
                            $ GwenX.FaceChange("sly",1)
                            ch_g "Ну, это зависит от того, насколько хорошо меня удовлетворяют. . ."
                            return
                    if "chill" not in GwenX.DailyActions:
                            $ GwenX.Statup("Obed", 90, 3)
                    $ GwenX.AddWord(1,0,"chill") #Daily
                    $ GwenX.Traits.append("chill")
            "Больше так не делай." if "chill" not in GwenX.Traits:
                    if ApprovalCheck(GwenX, 800, "O", TabM=0):
                            #she is obedient
                            $ GwenX.FaceChange("sly",1,Eyes="side")
                            ch_g "Ладно."
                    elif GwenX.Thirst >= 60 and not ApprovalCheck(GwenX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ GwenX.FaceChange("sly",1)
                            if "chill" not in GwenX.DailyActions:
                                    $ GwenX.Statup("Obed", 90, -2)
                            ch_g "Нет, если ты собираешься продолжать игнорировать меня. . ."
                            return
                    elif ApprovalCheck(GwenX, 400, "O", TabM=0):
                            #she is obedient
                            $ GwenX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_g "Да, госпожа. . ."
                            else:
                                ch_g "Да, господин. . ."
                    elif ApprovalCheck(GwenX, 500, "LO", TabM=0) and not ApprovalCheck(GwenX, 500, "I", TabM=0):
                            #she cares
                            $ GwenX.FaceChange("sly",1)
                            ch_g "Ты мне не указ!"
                            ch_g "Но я, все равно, попробую. . ."
                    else:
                            #she doesn't care
                            $ GwenX.FaceChange("sly",1)
                            ch_g "Я буду \"приставать\" к тебе как захочу и когда захочу."
                            return
                    if "chill" not in GwenX.DailyActions:
                            $ GwenX.Statup("Obed", 90, 3)
                    $ GwenX.AddWord(1,0,"chill") #Daily
                    $ GwenX.Traits.append("chill")
            "Делай что хочешь.":
                    if ApprovalCheck(GwenX, 800, "L", TabM=0):
                            $ GwenX.FaceChange("sly",1)
                            ch_g "Ох, думаю, нам обоим это понравится. . ."
                    elif ApprovalCheck(GwenX, 700, "O", TabM=0):
                            $ GwenX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_g "О, да, госпожа."
                            else:
                                ch_g "О, да, господин."
                    else:
                            $ GwenX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in GwenX.DailyActions:
                                    $ GwenX.Statup("Love", 90, -2)
                            ch_g "Конечно, если я буду возбуждена."
                    if "chill" not in GwenX.DailyActions:
                            $ GwenX.Statup("Obed", 90, 3)
                    if "chill" in GwenX.Traits:
                            $ GwenX.Traits.remove("chill")
                    $ GwenX.AddWord(1,0,"chill") #Daily
            "Эм, неважно.":
                pass
        return

# end Gwen jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start Gwen hungry //////////////////////////////////////////////////////////
label Gwen_Hungry:
    if GwenX.Chat[3]:
        ch_g "[[облизывает губы] У меня жажда. . ."
    elif GwenX.Chat[2]:
        ch_g "Слушай, эта твоя сыворотка просто супер. . ."
    else:
        ch_g "[[облизывает губы] У меня жажда. . ."
        ch_g "И единственное решение. . ."
        ch_g "Воспользоваться больше твоим предложением. . ."
    $ GwenX.Traits.append("hungry")
return


# end Gwen hungry //////////////////////////////////////////////////////////

# Gwen Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Gwen_SexChat:
    $ Line = "Ага, о чем ты хочешь поговорить?" if not Line else Line
    while True:
            menu:
                ch_g "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in GwenX.DailyActions:
                        ch_g "Ага, я слышала."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ GwenX.FaceChange("sly")
                                        if GwenX.PlayerFav == "sex":
                                            $ GwenX.Statup("Lust", 80, 5)
                                            ch_g "Ага, я знаю. . ."
                                        elif GwenX.Favorite == "sex":
                                            $ GwenX.Statup("Love", 90, 5)
                                            $ GwenX.Statup("Lust", 80, 10)
                                            ch_g "О, правда? Как удивлительно!"
                                        elif GwenX.Sex >= 5:
                                            ch_g "Ну, я не против."
                                        elif not GwenX.Sex:
                                            $ GwenX.FaceChange("perplexed")
                                            ch_g "Кто тебя трахает?"
                                        else:
                                            $ GwenX.FaceChange("bemused")
                                            ch_g "Ха, эм, да, это нормально. . ."
                                        $ GwenX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ GwenX.FaceChange("sly")
                                        if GwenX.PlayerFav == "anal":
                                            $ GwenX.Statup("Lust", 80, 5)
                                            ch_g "Я услышала тебя и в первый раз. . ."
                                        elif GwenX.Favorite == "anal":
                                            $ GwenX.Statup("Love", 90, 5)
                                            $ GwenX.Statup("Lust", 80, 10)
                                            ch_g "Мне он тоже нравится!"
                                        elif GwenX.Anal >= 10:
                                            ch_g "Ага, это. . . приятно. . ."
                                        elif not GwenX.Anal:
                                            $ GwenX.FaceChange("perplexed")
                                            ch_g "Кто тебя трахает?"
                                        else:
                                            $ GwenX.FaceChange("bemused",Eyes="side")
                                            ch_g "Ха, ага, эм, ладно. . ."
                                        $ GwenX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ GwenX.FaceChange("sly")
                                        if GwenX.PlayerFav == "blow":
                                            $ GwenX.Statup("Lust", 80, 3)
                                            ch_g "Ага, я знаю. . ."
                                        elif GwenX.Favorite == "blow":
                                            $ GwenX.Statup("Love", 90, 5)
                                            $ GwenX.Statup("Lust", 80, 5)
                                            ch_g "Мне тоже нравится!"
                                        elif GwenX.Blow >= 10:
                                            ch_g "Ну, ты довольно вкусный."
                                        elif not GwenX.Blow:
                                            $ GwenX.FaceChange("perplexed")
                                            ch_g "Кто сосет твой член?!"
                                        else:
                                            $ GwenX.FaceChange("bemused")
                                            ch_g "Я. . . тихонько к этому привыкаю. . ."
                                        $ GwenX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ GwenX.FaceChange("sly")
                                        if GwenX.PlayerFav == "cun":
                                            $ GwenX.Statup("Lust", 80, 3)
                                            ch_g "Ага, я знаю. . ."
                                        elif GwenX.Favorite == "cun":
                                            $ GwenX.Statup("Love", 90, 5)
                                            $ GwenX.Statup("Lust", 80, 5)
                                            ch_g "Мне нравится твоя киска!"
                                        elif GwenX.CUN >= 10:
                                            ch_g "Ну, ты довольно вкусная."
                                        elif not GwenX.CUN:
                                            $ GwenX.FaceChange("perplexed")
                                            ch_g "Кто сосет твой клитор?!"
                                        else:
                                            $ GwenX.FaceChange("bemused")
                                            ch_g "Я. . . тихонько к этому привыкаю. . ."
                                        $ GwenX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ GwenX.FaceChange("sly")
                                        if GwenX.PlayerFav == "titjob":
                                            $ GwenX.Statup("Lust", 80, 5)
                                            ch_g "Ага, я знаю. . ."
                                        elif GwenX.Favorite == "titjob":
                                            $ GwenX.Statup("Love", 90, 5)
                                            $ GwenX.Statup("Lust", 80, 7)
                                            ch_g "Ага, мне тоже нравится. . ."
                                        elif GwenX.Tit >= 10:
                                            ch_g "Это, безусловно, интересный опыт . . ."
                                        elif not GwenX.Tit:
                                            $ GwenX.FaceChange("perplexed")
                                            ch_g "Кто тебя трахает своими сиськами?"
                                        else:
                                            $ GwenX.FaceChange("bemused")
                                            ch_g "И не говори. . ."
                                            $ GwenX.Statup("Love", 80, 5)
                                            $ GwenX.Statup("Inbt", 50, 10)
                                        $ GwenX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ GwenX.FaceChange("sly")
                                        if GwenX.PlayerFav == "foot":
                                            $ GwenX.Statup("Lust", 80, 5)
                                            ch_g "Ага, я знаю. . ."
                                        elif GwenX.Favorite == "foot":
                                            $ GwenX.Statup("Love", 90, 5)
                                            $ GwenX.Statup("Lust", 80, 7)
                                            ch_g "Это даже забавно, использовать так свои ноги. . ."
                                        elif GwenX.Foot >= 10:
                                            ch_g "Мне тоже нравится . . ."
                                        elif not GwenX.Foot:
                                            $ GwenX.FaceChange("perplexed")
                                            ch_g "Кто играет с тобой своими ножками?"
                                        else:
                                            $ GwenX.FaceChange("bemused")
                                            ch_g "Ага, мило. . ."
                                        $ GwenX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ GwenX.FaceChange("sly")
                                        if GwenX.PlayerFav == "hand":
                                            $ GwenX.Statup("Lust", 80, 5)
                                            ch_g "Ага, я знаю. . ."
                                        elif GwenX.Favorite == "hand":
                                            $ GwenX.Statup("Love", 90, 5)
                                            $ GwenX.Statup("Lust", 80, 7)
                                            ch_g "Он комфортно лежит в руке. . ."
                                        elif GwenX.Hand >= 10:
                                            ch_g "Мне тоже нравится . . ."
                                        elif not GwenX.Hand:
                                            $ GwenX.FaceChange("perplexed")
                                            ch_g "Кто тебе дрочит?"
                                        else:
                                            $ GwenX.FaceChange("bemused")
                                            ch_g "Ага, мило. . ."
                                        $ GwenX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ GwenX.FaceChange("sly")
                                        if GwenX.PlayerFav == "finger":
                                            $ GwenX.Statup("Lust", 80, 5)
                                            ch_g "Ага, я знаю. . ."
                                        elif GwenX.Favorite == "finger":
                                            $ GwenX.Statup("Love", 90, 5)
                                            $ GwenX.Statup("Lust", 80, 7)
                                            ch_g "Она приятная на ощупь. . ."
                                        elif GwenX.Finger >= 10:
                                            ch_g "Мне тоже нравится . . ."
                                        elif not GwenX.Finger:
                                            $ GwenX.FaceChange("perplexed")
                                            ch_g "Кто тебя ласкает?"
                                        else:
                                            $ GwenX.FaceChange("bemused")
                                            ch_g "Ага, мило. . ."
                                        $ GwenX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = GwenX.FondleB + GwenX.FondleT + GwenX.SuckB + GwenX.Hotdog
                                        $ GwenX.FaceChange("sly")
                                        if GwenX.PlayerFav == "fondle":
                                            $ GwenX.Statup("Lust", 80, 3)
                                            ch_g "Да, я заметила. . ."
                                        elif GwenX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ GwenX.Statup("Love", 90, 5)
                                            $ GwenX.Statup("Lust", 80, 5)
                                            ch_g "Мне нравится, когда ты прикасаешься ко мне. . ."
                                        elif Cnt >= 10:
                                            ch_g "Ага, это очень приятно. . ."
                                        elif not Cnt:
                                            $ GwenX.FaceChange("perplexed")
                                            ch_g "И кого это ты ласкаешь?"
                                        else:
                                            $ GwenX.FaceChange("bemused")
                                            ch_g "Мне нравятся эти ощущения. . ."
                                        $ GwenX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ GwenX.FaceChange("sly")
                                        if GwenX.PlayerFav == "kiss you":
                                            $ GwenX.Statup("Love", 90, 3)
                                            ch_g "Оу, это так мило. . ."
                                        elif GwenX.Favorite == "kiss you":
                                            $ GwenX.Statup("Love", 90, 5)
                                            $ GwenX.Statup("Lust", 80, 5)
                                            ch_g "Хмм, ты отлично целуешься. . ."
                                        elif GwenX.Kissed >= 10:
                                            ch_g "Я тоже люблю тебя целовать. . ."
                                        elif not GwenX.Kissed:
                                            $ GwenX.FaceChange("perplexed")
                                            ch_g "Кого это ты целуешь?"
                                        else:
                                            $ GwenX.FaceChange("bemused")
                                            ch_g "Мне тоже нравится целовать тебя. . ."
                                        $ GwenX.PlayerFav = "kiss you"

                        $ GwenX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(GwenX, 800):
                                        $ GwenX.FaceChange("perplexed")
                                        ch_g ". . ."
                                else:
                                        if GwenX.SEXP >= 50:
                                            $ GwenX.FaceChange("sly")
                                            ch_g "Если ты до сих пор не знаешь. . ."
                                        else:
                                            $ GwenX.FaceChange("bemused")
                                            $ GwenX.Eyes = "side"
                                            ch_g "Хмм. . ."


                                        if not GwenX.Favorite or GwenX.Favorite == "kiss":
                                                ch_g "Думаю, когда меня целуют?"
                                        elif GwenX.Favorite == "anal":
                                                ch_g "Наверное. . . анал?"
                                        elif GwenX.Favorite == "lick ass":
                                                ch_g "Когда ты. . . вылизываешь мою попку?"
                                        elif GwenX.Favorite == "insert ass":
                                                ch_g "Наверное. . . когда ты. . . трахаешь мою попку пальцем."
                                        elif GwenX.Favorite == "sex":
                                                ch_g "Просто эм. . . классический секс."
                                        elif GwenX.Favorite == "lick pussy":
                                                ch_g "Когда ты. . . вылизываешь мою киску."
                                        elif GwenX.Favorite == "fondle pussy":
                                                ch_g "Когда ты. . . трахаешь меня пальцем."
                                        elif GwenX.Favorite == "blow":
                                                ch_g "Мне нравится. . . эм. . . сосать тебе?"
                                        elif GwenX.Favorite == "cun":
                                                ch_g "Мне нравится. . . эм. . . лизать тебе?"
                                        elif GwenX.Favorite == "tit":
                                                ch_g "Когда я. . . эм. . . трахаю тебя сиськами?"
                                        elif GwenX.Favorite == "foot":
                                                ch_g ". . . ножки?"
                                        elif GwenX.Favorite == "hand":
                                                ch_g "Мне нравится. . . эм. . . дрочить тебе."
                                        elif GwenX.Favorite == "finger":
                                                ch_g "Мне нравится. . . эм. . . ласкать твою киску."
                                        elif GwenX.Favorite == "hotdog":
                                                ch_g "Когда ты трешься о меня."
                                        elif GwenX.Favorite == "suck breasts":
                                                ch_g "Когда ты. . . сосешь мои сиськи."
                                        elif GwenX.Favorite == "fondle breasts":
                                                ch_g "Когда ты. . . мнешь мои сиськи."
                                        elif GwenX.Favorite == "fondle thighs":
                                                ch_g "Когда ты растираешь мои бедра."
                                        else:
                                                ch_g "Эм. . . я не знаю?"

                                # End Gwen's favorite things.

                "Не болтай так много во время секса." if "vocal" in GwenX.Traits:
                        if "setvocal" in GwenX.DailyActions:
                                $ GwenX.FaceChange("perplexed")
                                ch_g "Мы -уже- об этом разговаривали! . ."
                        else:
                            if ApprovalCheck(GwenX, 1000) and GwenX.Obed <= GwenX.Love:
                                $ GwenX.FaceChange("bemused")
                                $ GwenX.Statup("Obed", 90, 1)
                                ch_g "Больше ни слова."
                                $ GwenX.Traits.remove("vocal")
                            elif ApprovalCheck(GwenX, 700, "O"):
                                $ GwenX.FaceChange("sadside")
                                $ GwenX.Statup("Obed", 90, 1)
                                ch_g ". . ."
                                $ GwenX.Traits.remove("vocal")
                            elif ApprovalCheck(GwenX, 600):
                                $ GwenX.FaceChange("sly")
                                $ GwenX.Statup("Love", 90, -3)
                                $ GwenX.Statup("Obed", 50, -1)
                                $ GwenX.Statup("Inbt", 90, 5)
                                ch_g "Не лишай меня радости!"
                            else:
                                $ GwenX.FaceChange("angry")
                                $ GwenX.Statup("Love", 90, -5)
                                $ GwenX.Statup("Obed", 60, -3)
                                $ GwenX.Statup("Inbt", 90, 10)
                                ch_g "Нет."

                            $ GwenX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in GwenX.Traits:
                        if "setvocal" in GwenX.DailyActions:
                                $ GwenX.FaceChange("perplexed")
                                ch_g "Мы -уже- об этом разговаривали! . ."
                        else:
                            if ApprovalCheck(GwenX, 1000) and GwenX.Obed <= GwenX.Love:
                                $ GwenX.FaceChange("sly")
                                $ GwenX.Statup("Obed", 90, 2)
                                ch_g "Думаю, я справлюсь. . ."
                                $ GwenX.Traits.append("vocal")
                            elif ApprovalCheck(GwenX, 700, "O"):
                                $ GwenX.FaceChange("sadside")
                                $ GwenX.Statup("Obed", 90, 2)
                                ch_g "Посмотрим, что я смогу сделать."
                                $ GwenX.Traits.append("vocal")
                            elif ApprovalCheck(GwenX, 600):
                                $ GwenX.FaceChange("sly")
                                $ GwenX.Statup("Obed", 90, 3)
                                ch_g "Ох. . . ладно?"
                                $ GwenX.Traits.append("vocal")
                            else:
                                $ GwenX.FaceChange("angry")
                                $ GwenX.Statup("Inbt", 90, 5)
                                ch_g ". . ."

                            $ GwenX.DailyActions.append("setvocal")
                        # End Gwen Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in GwenX.Traits:
                        if "initiative" in GwenX.DailyActions:
                                $ GwenX.FaceChange("perplexed")
                                ch_g "Мы -уже- об этом разговаривали! . ."
                        else:
                            if ApprovalCheck(GwenX, 1200) and GwenX.Obed <= GwenX.Love:
                                $ GwenX.FaceChange("bemused")
                                $ GwenX.Statup("Obed", 90, 1)
                                ch_g "Ох. . . ладно."
                                $ GwenX.Traits.append("passive")
                            elif ApprovalCheck(GwenX, 700, "O"):
                                $ GwenX.FaceChange("sadside")
                                $ GwenX.Statup("Obed", 90, 1)
                                ch_g "Я, эм. . . попробую?"
                                $ GwenX.Traits.append("passive")
                            elif ApprovalCheck(GwenX, 600):
                                $ GwenX.FaceChange("sly")
                                $ GwenX.Statup("Love", 90, -3)
                                $ GwenX.Statup("Obed", 50, -1)
                                $ GwenX.Statup("Inbt", 90, 5)
                                ch_g "Ха, нет."
                            else:
                                $ GwenX.FaceChange("angry")
                                $ GwenX.Statup("Love", 90, -5)
                                $ GwenX.Statup("Obed", 60, -3)
                                $ GwenX.Statup("Inbt", 90, 10)
                                ch_g "Ох, посмотрим."

                            $ GwenX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in GwenX.Traits:
                        if "initiative" in GwenX.DailyActions:
                                $ GwenX.FaceChange("perplexed")
                                ch_g "Мы -уже- об этом разговаривали! . ."
                        else:
                            if ApprovalCheck(GwenX, 1000) and GwenX.Obed <= GwenX.Love:
                                $ GwenX.FaceChange("bemused")
                                $ GwenX.Statup("Obed", 90, 1)
                                ch_g "Ох, ладно."
                                $ GwenX.Traits.remove("passive")
                            elif ApprovalCheck(GwenX, 700, "O"):
                                $ GwenX.FaceChange("sadside")
                                $ GwenX.Statup("Obed", 90, 1)
                                ch_g "Это я могу."
                                $ GwenX.Traits.remove("passive")
                            elif ApprovalCheck(GwenX, 600):
                                $ GwenX.FaceChange("sly")
                                $ GwenX.Statup("Obed", 90, 3)
                                ch_g "Ох, посмотрим."
                                $ GwenX.Traits.remove("passive")
                            else:
                                $ GwenX.FaceChange("angry")
                                $ GwenX.Statup("Inbt", 90, 5)
                                ch_g "Выполняй свою часть дела."

                            $ GwenX.DailyActions.append("initiative")

                "О том, как ты накидываешься" if "jumped" in GwenX.History:
                        call Gwen_Jumped
                "О твоей мастурбации":
                        call NoFap(GwenX)

                "Всегда носи вибратор" if "dailyvibe" not in GwenX.Traits:
                        call Daily_Vibrator(GwenX)
                "Перестань всегда носить вибратор" if "dailyvibe" in GwenX.Traits:
                        ch_g "Ладно. . ."
                        $ GwenX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи анальную пробку" if "dailyplug" not in GwenX.Traits:
                        call Daily_Plug(GwenX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in GwenX.Traits:
                        ch_g "Ладно. . ."
                        $ GwenX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Неважно" if Line == "Ага, о чем ты хочешь поговорить?":
                        return
                "На этом все." if Line != "Ага, о чем ты хочешь поговорить?":
                        return
            if Line == "Ага, о чем ты хочешь поговорить?":
                $ Line = "Что-нибудь еще?"
    return
# End Gwen Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Gwen Chitchat /////////////////// #Work in progress
label Gwen_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if GwenX not in Digits:
                if ApprovalCheck(GwenX, 500, "L") or ApprovalCheck(GwenX, 250, "I"):
                    ch_g "Ох, вот мой номер, на случай, если тебе понадобится помощь."
                    $ Digits.append(GwenX)
                    return
                elif ApprovalCheck(GwenX, 250, "O"):
                    ch_g "Вот мой номер, на случай, если тебе понадобиться связаться со мной."
                    $ Digits.append(GwenX)
                    return

        if "hungry" not in GwenX.Traits and (GwenX.Swallow + GwenX.Chat[2]) >= 10 and GwenX.Loc == bg_current:  #She's swallowed a lot
                    call Gwen_Hungry
                    return

        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(GwenX, 800, "I")):
                    if GwenX.Loc == bg_current and GwenX.Thirst >= 30 and "refused" not in GwenX.DailyActions and "quicksex" not in GwenX.DailyActions:
                            $ GwenX.FaceChange("sly",1)
                            ch_g "Так вот, эм. . . хочешь трахнуться?"
                            call Quick_Sex(GwenX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in GwenX.DailyActions:
#            $ Options.append("caught")
        if GwenX.Event[0] and "key" not in GwenX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in GwenX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in GwenX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in GwenX.DailyActions:
            $ Options.append("corruption")

#        if "Gwen" not in GwenX.Names:
#            $ Options.append("gwen")

        if GwenX.Date >= 1 and bg_current != "bg restaurant":
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in GwenX.DailyActions and "cheek" not in GwenX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if GwenX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in GwenX.DailyActions and (Player.Male or "girltalk" in GwenX.History):
            #If you've caught Gwen showering today
            $ Options.append("showercaught")
        if "fondle breasts" in GwenX.DailyActions or "fondle pussy" in GwenX.DailyActions or "fondle ass" in GwenX.DailyActions:
            #If you've fondled Gwen today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in GwenX.Inventory and "256 Shades of Grey" in GwenX.Inventory and "Avengers Tower Penthouse" in GwenX.Inventory:
            #If you've given Gwen the books
            if "book" not in GwenX.Chat:
                $ Options.append("booked")
        if "lace bra" in GwenX.Inventory or "lace panties" in GwenX.Inventory:
            #If you've given Gwen the lingerie
            if "lingerie" not in GwenX.Chat:
                $ Options.append("lingerie")
        if GwenX.Hand and Player.Male:
            #If Gwen's given a handjob
            $ Options.append("handy")
        if GwenX.Blow and Player.Male:
            #If Gwen's given a blowjob
            $ Options.append("blow")
        if GwenX.Swallow:
            #If Gwen's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in GwenX.DailyActions or "painted" in GwenX.DailyActions:
            #If Gwen's been facialed
            $ Options.append("facial")
        if GwenX.Sleep:
            #If Gwen's slept over
            $ Options.append("sleep")
        if (GwenX.CreamP or GwenX.CreamA) and Player.Male:
            #If Gwen's been creampied
            $ Options.append("creampie")
        if GwenX.Sex or GwenX.Anal:
            #If Gwen's been sexed
            $ Options.append("sexed")
        if GwenX.Anal:
            #If Gwen's been analed
            $ Options.append("anal")

        if "seenpeen" in GwenX.History and Player.Male:
            $ Options.append("seenpeen")
        if "topless" in GwenX.History:
            $ Options.append("topless")
        if "bottomless" in GwenX.History:
            $ Options.append("bottomless")

#        if not GwenX.Chat[0] and GwenX.Sex:
#            $ Options.append("virgin")

#        if (bg_current == "bg gwen" or bg_current == "bg player") and "relationship" not in GwenX.DailyActions:
#            if "lover" not in GwenX.Petnames and ApprovalCheck(GwenX, 900, "L"): # GwenX.Event[6]
#                $ Options.append("lover?")
#            elif "sir" not in GwenX.Petnames and ApprovalCheck(GwenX, 500, "O"): # GwenX.Event[7]
#                $ Options.append("sir?")
#            elif "daddy" not in GwenX.Petnames and ApprovalCheck(GwenX, 750, "L") and ApprovalCheck(GwenX, 500, "O") and ApprovalCheck(GwenX, 500, "I"): # GwenX.Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in GwenX.Petnames and ApprovalCheck(GwenX, 900, "O"): # GwenX.Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in GwenX.Petnames and ApprovalCheck(GwenX, 500, "I"): # GwenX.Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in GwenX.Petnames and ApprovalCheck(GwenX, 900, "I"): # GwenX.Event[10]
#                $ Options.append("fuckbuddy?")


        if not ApprovalCheck(GwenX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ GwenX.DailyActions.append("cologne chat")
        $ GwenX.FaceChange("confused")
        ch_g "(нюх-нюх). . . пахнет. . . обезьяной. . ."
        $ GwenX.FaceChange("sexy", 2)
        ch_g ". . . хочешь заняться чем-нибудь попозже?"
    elif Options[0] == "purple":
        $ GwenX.DailyActions.append("cologne chat")
        $ GwenX.FaceChange("sly",1)
        ch_g "(нюх-нюх). . . что это? . ."
        $ GwenX.FaceChange("normal",0)
        ch_g ". . . ты что-нибудь хочешь?"
    elif Options[0] == "corruption":
        $ GwenX.DailyActions.append("cologne chat")
        $ GwenX.FaceChange("confused")
        ch_g "(нюх-нюх). . .  сильный запах. . ."
        $ GwenX.FaceChange("angry")
        ch_g ". . . Я чувствую себя злой Гвен. . ."
        $ GwenX.FaceChange("sly")

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in GwenX.Chat:
                    ch_g "Эй! Из-за тебя я чуть не влетела!"
                    if not ApprovalCheck(GwenX, 500, "I"):
                         ch_g "Но это было довольно увлекательно. . ."
            else:
                    ch_g "Эй! Из-за тебя я чуть не влетела!"
                    if not ApprovalCheck(GwenX, 500, "I"):
                        ch_g "Так что, думаю, больше никаких \"публичных непристойностей.\" . ."
                    else:
                        ch_g "Но это было довольно увлекательно. . ."
                    $ GwenX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if GwenX.SEXP <= 15:
                ch_g "Я дала тебе ключ от комнаты, но будь с ним осторожнее. . ."
            else:
                ch_g "Я дала тебе ключ, но ты не приходишь. . ."
            $ GwenX.Chat.append("key")

    elif Options[0] == "dated":
            #Gwen's response to having gone on a date with the Player.
            ch_g "Мне было весело прошлой ночью, мы должны повторить."

    elif Options[0] == "kissed":
            #Gwen's response to having been kissed by the Player.
            $ GwenX.FaceChange("normal",1)
            ch_g "Ты хорошо целуешься, [GwenX.Petname]."
            menu:
                extend ""
                "Я стараюсь.":
                        $ GwenX.FaceChange("smile",1)
                        ch_g "Ага, заметно."
                "Ты так думаешь?":
                        ch_g "Ну, да."

    elif Options[0] == "dangerroom":
            #Gwen's response to Player working out in the Danger Room while Gwen is present
            $ GwenX.FaceChange("sly",1)
            ch_g "Слушай, [GwenX.Petname]. Я наблюдала за тобой в комнате Опасности."
            if not Player.Male:
                ch_g "Ты выглядела так глупо! Пиу-пиу, \"аххх, перестаньте в меня стрелять!\""
            else:
                ch_g "Ты выглядел так глупо! Пиу-пиу, \"аххх, перестаньте в меня стрелять!\""

    elif Options[0] == "showercaught":
            #Gwen's response to being caught in the shower.
            if "shower" in GwenX.Chat:
                if not Player.Male:
                    ch_g "Хм, ты снова видела, как я принимала душ. . ."
                else:
                    ch_g "Хм, ты снова видел, как я принимала душ. . ."
            else:
                ch_g "Ты всегда. . . так делаешь?"
                ch_g "Сразу врываешься в душ?"
                $ GwenX.Chat.append("shower")
                menu:
                    extend ""
                    "Это чистая случайность! Клянусь!":
                            $ GwenX.Statup("Love", 50, 5)
                            $ GwenX.Statup("Love", 90, 2)
                            if ApprovalCheck(GwenX, 1200):
                                $ GwenX.FaceChange("sly",1)
                                ch_g "Ну-ну. . ."
                                ch_g "Не позволяй этому повториться. . ."
                            else:
                                $ GwenX.FaceChange("smile")
                                ch_g "Хорошо, я тебе верю. . ."
                    "Только если там ты.":
                            $ GwenX.Statup("Obed", 40, 5)
                            if ApprovalCheck(GwenX, 1000) or ApprovalCheck(GwenX, 700, "L"):
                                    $ GwenX.Statup("Love", 90, 3)
                                    $ GwenX.FaceChange("surprised",2,Mouth="normal")
                                    ch_g "Ох, эм. . ."
                                    $ GwenX.FaceChange("sly",1)
                                    ch_g "Спасибо?"
                            else:
                                    $ GwenX.Statup("Love", 70, -5)
                                    $ GwenX.FaceChange("angry")
                                    ch_g "Угу, и это совсем не жутко. . ."
                    "Я заглянула умышленно. Но я ни о чем не жалею." if not Player.Male:
                            if ApprovalCheck(GwenX, 1200):
                                    $ GwenX.Statup("Love", 90, 3)
                                    $ GwenX.Statup("Obed", 70, 10)
                                    $ GwenX.Statup("Inbt", 50, 5)
                                    $ GwenX.FaceChange("sly",1)
                                    ch_g "Думаю, я могу забыть об этом инциденте."
                            elif ApprovalCheck(GwenX, 800):
                                    $ GwenX.Statup("Obed", 60, 5)
                                    $ GwenX.Statup("Inbt", 50, 5)
                                    $ GwenX.FaceChange("perplexed",2)
                                    ch_g "Ну. . . тогда ладно. . ."
                                    $ GwenX.Blush = 1
                            else:
                                    $ GwenX.Statup("Love", 50, -10)
                                    $ GwenX.Statup("Love", 80, -10)
                                    $ GwenX.Statup("Obed", 50, 10)
                                    $ GwenX.FaceChange("angry")
                                    ch_g "Угу, и это совсем не жутко. . ."
                    "Я заглянул умышленно. Но я ни о чем не жалею." if Player.Male:
                            if ApprovalCheck(GwenX, 1200):
                                    $ GwenX.Statup("Love", 90, 3)
                                    $ GwenX.Statup("Obed", 70, 10)
                                    $ GwenX.Statup("Inbt", 50, 5)
                                    $ GwenX.FaceChange("sly",1)
                                    ch_g "Думаю, я могу забыть об этом инциденте."
                            elif ApprovalCheck(GwenX, 800):
                                    $ GwenX.Statup("Obed", 60, 5)
                                    $ GwenX.Statup("Inbt", 50, 5)
                                    $ GwenX.FaceChange("perplexed",2)
                                    ch_g "Ну. . . тогда ладно. . ."
                                    $ GwenX.Blush = 1
                            else:
                                    $ GwenX.Statup("Love", 50, -10)
                                    $ GwenX.Statup("Love", 80, -10)
                                    $ GwenX.Statup("Obed", 50, 10)
                                    $ GwenX.FaceChange("angry")
                                    ch_g "Угу, и это совсем не жутко. . ."

    elif Options[0] == "fondled":
            #Gwen's response to being felt up.
            if GwenX.FondleB + GwenX.FondleP + GwenX.FondleA >= 15:
                if not Player.Male:
                    ch_g "Не могла бы ты провести мне еще один осмотр?"
                else:
                    ch_g "Не мог бы ты провести мне еще один осмотр?"
            else:
                if not Player.Male:
                    ch_g "Я была бы не против, если бы ты меня как-нибудь потрогала."
                else:
                    ch_g "Я была бы не против, если бы ты меня как-нибудь потрогал."

    elif Options[0] == "booked":
            #Gwen's response after a Player gives her the books from the shop.
            if not Player.Male:
                ch_g "Слушай, я прочитала те книги, которые ты мне дала."
            else:
                ch_g "Слушай, я прочитала те книги, которые ты мне дал."
            menu:
                extend ""
                "Да? И как тебе?":
                        $ GwenX.FaceChange("sly",2)
                        ch_g "Они. . . далеки от канона. . ."
                "Хорошо. Пожалуй, ты могла бы чему-нибудь из них научиться.":
                        $ GwenX.Statup("Love", 90, -3)
                        $ GwenX.Statup("Obed", 70, 5)
                        $ GwenX.Statup("Inbt", 50, 5)
                        $ GwenX.FaceChange("angry")
                        ch_g "Неприлично говорить такое!"
            $ GwenX.Blush = 1
            $ GwenX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Gwen's response to being given lingerie.
            $ GwenX.FaceChange("sly",2)
            if not Player.Male:
                ch_g "Мне, эм. . . очень нравится белье, которое ты мне подарила."
            else:
                ch_g "Мне, эм. . . очень нравится белье, которое ты мне подарил."
            ch_g "Оно классное. . . "
            $ GwenX.Blush = 1
            $ GwenX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Gwen's response after giving the Player a handjob.
            $ GwenX.FaceChange("sly",1)
            ch_g "Похоже, тебе очень понравилась дрочка, которую я тебе сделала. . ."
            ch_g "Приятно, что я выбрала правильный подход. . ."

    elif Options[0] == "blow":
            if "blow" not in GwenX.Chat:
                    #Gwen's response after giving the Player a blowjob.
                    $ GwenX.FaceChange("sly",2)
                    ch_g "Так вот, эт. . . помнишь, я тебе отсосала? . ."
                    ch_g "Было ведь не совсем ужасно, правда?"
                    menu:
                        extend ""
                        "Ты была великолепна.":
                                    $ GwenX.Statup("Love", 90, 5)
                                    $ GwenX.Statup("Inbt", 60, 10)
                                    $ GwenX.FaceChange("surprised",2)
                                    ch_g "Ох!"
                                    $ GwenX.FaceChange("sly",1,Eyes="side")
                                    ch_g "Ох, хорошо. . ."
                                    $ GwenX.FaceChange("sexy",1)
                                    ch_g "Я бы, эм. . . не отказалась попробовать как-нибудь еще раз. . ."
                        "Честно? Все было хорошо. . . но, думаю, тебе не помешает еще немного попрактиковаться.":
                                if ApprovalCheck(GwenX, 300, "I") or not ApprovalCheck(GwenX, 800):
                                    $ GwenX.Statup("Love", 90, -5)
                                    $ GwenX.Statup("Obed", 60, 10)
                                    $ GwenX.Statup("Inbt", 50, 10)
                                    $ GwenX.FaceChange("perplexed",1)
                                    ch_g "Ну. . . ладно."
                                else:
                                    $ GwenX.Statup("Obed", 70, 15)
                                    $ GwenX.Statup("Inbt", 50, 5)
                                    $ GwenX.FaceChange("sexy",1)
                                    ch_g "Хмммм. . . Я буду тренироваться. . ."
                        "Угу, если бы мне нравились стремные звуки и шкрябанье зубов по члену, но это далеко не так.":
                                $ GwenX.Statup("Love", 90, -10)
                                $ GwenX.Statup("Obed", 60, 10)
                                $ GwenX.FaceChange("angry",2)
                                ch_g "Ну. . . таков -Мой- стиль!"
                    $ GwenX.Blush = 1
                    $ GwenX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["Знаешь, для кучки пикселей у твоего члена прекрасный вкус.",
                            "Кажется, в прошлый раз я чуть не вывихнула себе челюсть.",
                            "Я могла бы когда-нибудь сделать тебе еще один минет.",
                            "Хммм. . . [Стучит языком по внутренней стороне щеки.]"])
                    ch_g "[Line]"

    elif Options[0] == "swallowed":
            #Gwen's response after swallowing the Player's cum.
            if "swallow" in GwenX.Chat:
                $ GwenX.FaceChange("sly",1)
                if not Player.Male:
                    ch_g "Так вот. . . могу я как-нибудь снова попробовать твои соки?"
                else:
                    ch_g "Так вот. . . могу я как-нибудь снова попробовать твою сперму?"
            else:
                ch_g "Слушай, эм. . . в тот день. . ."
                $ GwenX.FaceChange("confused",1,Mouth="normal")
                if not Player.Male:
                    ch_g "Ты знаешь, что твои соки странные на вкус?"
                else:
                    ch_g "Ты знаешь, что твоя сперма странная на вкус?"
                $ GwenX.FaceChange("normal",1)
                ch_g "Так не должно быть. . ."
                $ GwenX.FaceChange("sly",1)
                if not Player.Male:
                    ch_g "Они не очень. . . вкусные. . ."
                else:
                    ch_g "Она не очень. . . вкусная. . ."
                $ GwenX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Gwen's response after taking a facial from the Player.
            ch_g "Ладно, послушай меня. . ."
            $ GwenX.FaceChange("sexy",2)
            if not Player.Male:
                ch_g "Мне очень приятно, когда у меня на лице твои соки."
                ch_g ". . ."
                ch_g "Просто хочу, чтобы ты знала. . ."
            else:
                ch_g "Мне очень приятно, когда у меня на лице твоя сперма."
                ch_g ". . ."
                ch_g "Просто хочу, чтобы ты знал. . ."
            $ GwenX.Blush = 1

    elif Options[0] == "sleepover":
            #Gwen's response after sleeping with the Player.
            ch_g "Мне очень понравилась та ночь."
            ch_g "Приятно спать не одной. . ."

    elif Options[0] == "creampie":
            #Another of Gwen's responses after having sex with the Player.
            "[GwenX.Name] сближается с вами, чтобы прошептать вам на ухо."
            ch_g "Частичка тебя. . . все еще стекает по моему бедру."

    elif Options[0] == "sexed":
            #A final response from Gwen after having sex with the Player.
            if not Player.Male:
                ch_g "Я, эм. . . хочу, чтобы ты знала. . . эм. . ."
            else:
                ch_g "Я, эм. . . хочу, чтобы ты знал. . . эм. . ."
            $ GwenX.FaceChange("sly",2,Eyes="side")
            if not Player.Male:
                ch_g ". . .С того времени, когда мы. . . ну, ты поняла. . ."
            else:
                ch_g ". . .С того времени, когда мы. . . ну, ты понял. . ."
            $ GwenX.FaceChange("sexy",2)
            ch_g "Я, эм. . . постоянно думаю о тебе."
            $ GwenX.Blush = 1

    elif Options[0] == "anal":
            #Gwen's response after getting anal from the Player.
            $ GwenX.FaceChange("sly")
            ch_g "Мне не особо нравился анал. . ."
            $ GwenX.FaceChange("sexy",1)
            ch_g "Пока я не повстречала тебя."

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ GwenX.FaceChange("sly",1, Eyes="down")
            ch_g "Ох, эм. . . Кажется, я никогда не упоминала. . ."
            ch_g "У тебя очень хороший, эм. . ."
            if not Player.Male:
                ch_g "-экземпляр?"
            else:
                ch_g "-прибор?"
            $ GwenX.FaceChange("bemused",1)
            $ GwenX.Statup("Love", 50, 5)
            $ GwenX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            if not Player.Male:
                ch_g "Итак, эм, ты видела мои сиськи, верно?"
            else:
                ch_g "Итак, эм, ты видел мои сиськи, верно?"
            ch_g "Что ты о них думаешь?"
            call Girl_First_TMenu
            $ GwenX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            if not Player.Male:
                ch_g "Слушай, эм, ты видела мою киску. . ."
            else:
                ch_g "Слушай, эм, ты видел мою киску. . ."
            ch_g "Что ты о ней думаешь?"
            call Girl_First_BMenu
            $ GwenX.History.remove("bottomless")

#    elif Options[0] == "boyfriend?":
#        call Gwen_BF
#    elif Options[0] == "lover?":
#        call Gwen_Love
#    elif Options[0] == "sir?":
#        call Gwen_Sub
#    elif Options[0] == "master?":
#        call Gwen_Master
#    elif Options[0] == "sexfriend?":
#        call Gwen_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Gwen_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Gwen_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        if not Player.Male:
            $ Line = renpy.random.choice(["Отойди от меня.",
                    "Я не хочу, чтобы ты была рядом со мной.",
                    "Я пытаюсь уйти отсюда.",
                    "Отвали.",
                    "Убирайся."])
        else:
            $ Line = renpy.random.choice(["Отойди от меня.",
                    "Я не хочу, чтобы ты был рядом со мной.",
                    "Я пытаюсь уйти отсюда.",
                    "Отвали.",
                    "Убирайся."])
        ch_g "[Line]"

    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 21)
            if D20 == 1:
                    $ GwenX.FaceChange("smile")
                    ch_g "Пока что я получаю неплохие оценки. \"Биология Мутантов\" гораздо интереснее \"математики.\""
            elif D20 == 2:
                    $ GwenX.FaceChange("angry")
                    ch_g "Почему многие вообще думают, что я Дэдпул?"
                    ch_g "Ну, если не брать в расчет, что у нас похожие маски."
            elif D20 == 3:
                    $ GwenX.FaceChange("surprised")
                    ch_g "А? О, извини. Я отвлеклась. Это так похоже на меня."
            elif D20 == 4:
                    $ GwenX.FaceChange("sad")
                    ch_g "Ох, [GwenX.Petname]. Извини, я думаю о пироге."
            elif D20 == 5:
                    $ GwenX.FaceChange("smile")
                    ch_g "Весело иногда просто расслабиться и позволить маленькому таймеру крутиться."
            elif D20 == 6:
                    $ GwenX.FaceChange("perplexed")
                    ch_g "Ох, [GwenX.Petname]. Я вижу всех НИПов, которых ты не видишь. Вон Санспот, прямо над твоим плечом."
            elif D20 == 7:
                    $ GwenX.FaceChange("smile")
                    ch_g "Слушай, кажется, я поняла, как заставить комнату Опасности создавать истории \"Диксон Хилл\"."
                    "CreDz" "\"Диксон Хилл\" - типа  метавымышленный детектив, который был в сериале \"Звездный Путь\"... "
                    "CreDz" "Где одного из героев играл актер, который снимался в трилогии \"Люди Икс\" в роли профессора Ксавье."
                    "CreDz" "Сам я не ебу, что да как, но для чего еще нужен интернет?"
                    ch_g "Ксавьер будет в восторге!"
            elif D20 == 8:
                    $ GwenX.FaceChange("sad")
                    ch_g "Мне нравится быть здесь, но во вселенной комиксов тоже было весело. . ."
            elif D20 == 9:
                    $ GwenX.FaceChange("confused")
                    ch_g "Не знаю, знаешь ли ты, но здешняя еда на вкус странная."
            elif D20 == 10:
                    $ GwenX.FaceChange("smile")
                    ch_g "Так здорово общаться со всеми местными персонажами!"
            elif D20 == 11:
                    $ GwenX.FaceChange("smile")
                    ch_g "Я танцевала с Китти Прайд!"
            elif D20 == 12:
                    $ GwenX.FaceChange("sad")
                    ch_g "Мне нравится разговаривать с Роуг и другими. От этого я чувствую, даже не знаю. . ."
                    ch_g "Чувствую, что мое место здесь. . ."
            elif D20 == 13:
                    $ GwenX.FaceChange("smile")
                    ch_g "Китти и Лора взяли меня с собой в торговый центр за мороженым!"
            elif D20 == 14:
                    $ GwenX.FaceChange("sad")
                    ch_g "Мне нравится ходить на миссии, но потом приходится наверстывать упущенное."
            elif D20 == 15:
                    $ GwenX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_g "Ты замечала здесь какие-нибудь моменты не из Людей Икс?"
                    else:
                        ch_g "Ты замечал здесь какие-нибудь моменты не из Людей Икс?"
                    ch_g "Что-нибудь из \"Новых Воинов\" или еще откуда-нибудь?"
                    ch_g "Из \"Защитников\"?"
            elif D20 == 16:
                    $ GwenX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_g "Ты когда-нибудь была в Нью-Йорке? Он огромен."
                    else:
                        ch_g "Ты когда-нибудь был в Нью-Йорке? Он огромен."
            elif D20 == 17:
                    $ GwenX.FaceChange("perplexed")
                    ch_g "Логан просто подошел и сказал, что я похожа на. . ."
                    ch_g "\"Того-кого-не-следует-называть\". . ."
                    ch_g "Я чуть не ударила его ножом в лицо, но что толку?"
            elif D20 == 18:
                    $ GwenX.FaceChange("smile")
                    ch_g "Никому не говори, но я думаю, что Зверь из правила 63 довольно сексуальный."
            elif D20 == 19:
                    $ GwenX.FaceChange("confused")
                    ch_g "Эй, это. . . торт?!"
            elif D20 == 20:
                    $ GwenX.FaceChange("smile")
                    ch_g "Просто болтать - весело. . . и фразы совсем не повторяются. . ."
            else:
                    $ GwenX.FaceChange("smile")
                    ch_g "С тобой весело проводить время."

    $ Line = 0
    return

# start Gwen_Names//////////////////////////////////////////////////////////
label Gwen_Names:
    menu:
        ch_g "А? Как тебе хочется, чтобы я тебя звала?"
        "Зови по инициалам.":
            $ GwenX.Petname = Player.Name[:1]  #fix test this
            $ GwenX.Petname_rod = Player.Name[:1]
            $ GwenX.Petname_dat = Player.Name[:1]
            $ GwenX.Petname_vin = Player.Name[:1]
            $ GwenX.Petname_tvo = Player.Name[:1]
            $ GwenX.Petname_pre = Player.Name[:1]
            ch_g "Поняла, [GwenX.Petname]."
        "Зови меня по имени.":
            $ GwenX.Petname = Player.Name
            $ GwenX.Petname_rod = Player.Name_rod
            $ GwenX.Petname_dat = Player.Name_dat
            $ GwenX.Petname_vin = Player.Name_vin
            $ GwenX.Petname_tvo = Player.Name_tvo
            $ GwenX.Petname_pre = Player.Name_pre
            ch_g "Ладно, [GwenX.Petname]."
        "Зови меня своей \"девушкой\"." if "boyfriend" in GwenX.Petnames and not Player.Male:
            $ GwenX.Petname = "моя девушка"
            $ GwenX.Petname_rod = "моей девушки"
            $ GwenX.Petname_dat = "моей девушке"
            $ GwenX.Petname_vin = "мою девушку"
            $ GwenX.Petname_tvo = "моей девушкой"
            $ GwenX.Petname_pre = "моей девушке"
            ch_g "Конечно, [GwenX.Petname]."
        "Зови меня своим \"парнем\"." if "boyfriend" in GwenX.Petnames and Player.Male:
            $ GwenX.Petname = "мой парень"
            $ GwenX.Petname_rod = "моего парня"
            $ GwenX.Petname_dat = "моему парню"
            $ GwenX.Petname_vin = "моего парня"
            $ GwenX.Petname_tvo = "моим парнем"
            $ GwenX.Petname_pre = "моем парне"
            ch_g "Конечно, [GwenX.Petname]."
        "Зови меня \"любимая\"." if "lover" in GwenX.Petnames and not Player.Male:
            $ GwenX.Petname = "любимая"
            $ GwenX.Petname_rod = "любимой"
            $ GwenX.Petname_dat = "любимой"
            $ GwenX.Petname_vin = "любимую"
            $ GwenX.Petname_tvo = "любимой"
            $ GwenX.Petname_pre = "любимой"
            ch_g "Ооох, мне нравится, [GwenX.Petname]."
        "Зови меня \"любимый\"." if "lover" in GwenX.Petnames and Player.Male:
            $ GwenX.Petname = "любимый"
            $ GwenX.Petname_rod = "любимого"
            $ GwenX.Petname_dat = "любимому"
            $ GwenX.Petname_vin = "любимого"
            $ GwenX.Petname_tvo = "любимым"
            $ GwenX.Petname_pre = "любимом"
            ch_g "Ооох, мне нравится, [GwenX.Petname]."
        "Зови меня \"госпожа\"." if "sir" in GwenX.Petnames and not Player.Male:
            $ GwenX.Petname = "госпожа"
            $ GwenX.Petname_rod = "госпожи"
            $ GwenX.Petname_dat = "госпоже"
            $ GwenX.Petname_vin = "госпожу"
            $ GwenX.Petname_tvo = "госпожой"
            $ GwenX.Petname_pre = "госпоже"
            ch_g "Да, [GwenX.Petname]."
        "Зови меня \"господин\"." if "sir" in GwenX.Petnames and Player.Male:
            $ GwenX.Petname = "господин"
            $ GwenX.Petname_rod = "господина"
            $ GwenX.Petname_dat = "господину"
            $ GwenX.Petname_vin = "господина"
            $ GwenX.Petname_tvo = "господином"
            $ GwenX.Petname_pre = "господине"
            ch_g "Да, [GwenX.Petname]."
        "Зови меня \"хозяйка\"." if "master" in GwenX.Petnames and not Player.Male:
            $ GwenX.Petname = "хозяйка"
            $ GwenX.Petname_rod = "хозяйки"
            $ GwenX.Petname_dat = "хозяйке"
            $ GwenX.Petname_vin = "хозяйку"
            $ GwenX.Petname_tvo = "хозяйкой"
            $ GwenX.Petname_pre = "хозяйке"
            ch_g "Как пожелаешь, [GwenX.Petname]."
        "Зови меня \"хозяин\"." if "master" in GwenX.Petnames and Player.Male:
            $ GwenX.Petname = "хозяин"
            $ GwenX.Petname_rod = "хозяина"
            $ GwenX.Petname_dat = "хозяину"
            $ GwenX.Petname_vin = "хозяина"
            $ GwenX.Petname_tvo = "хозяином"
            $ GwenX.Petname_pre = "хозяине"
            ch_g "Как пожелаешь, [GwenX.Petname]."
        "Зови меня \"любовница\"." if "sex friend" in GwenX.Petnames and not Player.Male:
            $ GwenX.Petname = "любовница"
            $ GwenX.Petname_rod = "любовницы"
            $ GwenX.Petname_dat = "любовнице"
            $ GwenX.Petname_vin = "любовницу"
            $ GwenX.Petname_tvo = "любовницей"
            $ GwenX.Petname_pre = "любовнице"
            ch_g "Ха, ладно, [GwenX.Petname]."
        "Зови меня \"любовник\"." if "sex friend" in GwenX.Petnames and Player.Male:
            $ GwenX.Petname = "любовник"
            $ GwenX.Petname_rod = "любовника"
            $ GwenX.Petname_dat = "любовнику"
            $ GwenX.Petname_vin = "любовника"
            $ GwenX.Petname_tvo = "любовником"
            $ GwenX.Petname_pre = "любовнике"
            ch_g "Ха, ладно, [GwenX.Petname]."
        "Зови меня \"секс-партнерша\"." if "fuck buddy" in GwenX.Petnames and not Player.Male:
            $ GwenX.Petname = "секс-партнерша"
            $ GwenX.Petname_rod = "секс-партнерши"
            $ GwenX.Petname_dat = "секс-партнерше"
            $ GwenX.Petname_vin = "секс-партнершу"
            $ GwenX.Petname_tvo = "секс-партнершей"
            $ GwenX.Petname_pre = "секс-партнерше"
            ch_g "Ого. . . [GwenX.Petname]."
        "Зови меня \"секс-партнер\"." if "fuck buddy" in GwenX.Petnames and Player.Male:
            $ GwenX.Petname = "секс-партнер"
            $ GwenX.Petname_rod = "секс-партнера"
            $ GwenX.Petname_dat = "секс-партнеру"
            $ GwenX.Petname_vin = "секс-партнера"
            $ GwenX.Petname_tvo = "секс-партнером"
            $ GwenX.Petname_pre = "секс-партнере"
            ch_g "Ого. . . [GwenX.Petname]."
        "Зови меня \"мамочка\"." if "daddy" in GwenX.Petnames and not Player.Male:
            $ GwenX.Petname = "мамочка"
            $ GwenX.Petname_rod = "мамочки"
            $ GwenX.Petname_dat = "мамочке"
            $ GwenX.Petname_vin = "мамочку"
            $ GwenX.Petname_tvo = "мамочкой"
            $ GwenX.Petname_pre = "мамочке"
            ch_g "Ох! Конечно, [GwenX.Petname]."
        "Зови меня \"папочка\"." if "daddy" in GwenX.Petnames and Player.Male:
            $ GwenX.Petname = "папочка"
            $ GwenX.Petname_rod = "папочки"
            $ GwenX.Petname_dat = "папочке"
            $ GwenX.Petname_vin = "папочку"
            $ GwenX.Petname_tvo = "папочкой"
            $ GwenX.Petname_pre = "папочке"
            ch_g "Ох! Конечно, [GwenX.Petname]."
        "\"Чувиха\" в самый раз." if not Player.Male:
            $ GwenX.Petname = "Чувиха"
            $ GwenX.Petname_rod = "Чувихи"
            $ GwenX.Petname_dat = "Чувихе"
            $ GwenX.Petname_vin = "Чувиху"
            $ GwenX.Petname_tvo = "Чувихой"
            $ GwenX.Petname_pre = "Чувихе"
            ch_g "Поняла, чувиха."
        "\"Чувак\" в самый раз." if Player.Male:
            $ GwenX.Petname = "Чувак"
            $ GwenX.Petname_rod = "Чувака"
            $ GwenX.Petname_dat = "Чуваку"
            $ GwenX.Petname_vin = "Чувака"
            $ GwenX.Petname_tvo = "Чуваком"
            $ GwenX.Petname_pre = "Чуваке"
            ch_g "Поняла, чувак."
        "Неважно.":
            return
    return
# end Gwen_Names//////////////////////////////////////////////////////////

label Gwen_Pet:
    while 1:
        menu:
            extend ""
            "Обходительно":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "Гвен.":
                        $ GwenX.Pet = "Гвен"
                        $ GwenX.Pet_rod = "Гвен"
                        $ GwenX.Pet_dat = "Гвен"
                        $ GwenX.Pet_vin = "Гвен"
                        $ GwenX.Pet_tvo = "Гвен"
                        $ GwenX.Pet_pre = "Гвен"
                        ch_g "Не вижу причин отказывать, [GwenX.Petname]."

                    "Гвенпул.":
                        $ GwenX.Pet = "Гвенпул"
                        $ GwenX.Pet_rod = "Гвенпул"
                        $ GwenX.Pet_dat = "Гвенпул"
                        $ GwenX.Pet_vin = "Гвенпул"
                        $ GwenX.Pet_tvo = "Гвенпул"
                        $ GwenX.Pet_pre = "Гвенпул"
                        if ApprovalCheck(GwenX, 700, "L") and not ApprovalCheck(GwenX, 500, "O"):
                                ch_g "Ох, как скажешь, [GwenX.Petname]."
                        else:
                                ch_g "Не вижу причин отказывать, [GwenX.Petname]."

                    "\"моя девушка\".":
                        if "boyfriend" in GwenX.Petnames:
                            $ GwenX.FaceChange("sexy", 1)
                            $ GwenX.Pet = "моя девушка"
                            $ GwenX.Pet_rod = "моей девушки"
                            $ GwenX.Pet_dat = "моей девушке"
                            $ GwenX.Pet_vin = "мою девушку"
                            $ GwenX.Pet_tvo = "моей девушкой"
                            $ GwenX.Pet_pre = "моей девушке"
                            ch_g "Я полностью твоя, [GwenX.Petname]."
                        else:
                            $ GwenX.FaceChange("angry")
                            ch_g "Я НЕ твоя девушка, [GwenX.Petname]."

                    "\"детка\".":
                        if "boyfriend" in GwenX.Petnames or ApprovalCheck(GwenX, 700, "L"):
                            $ GwenX.Pet = "детка"
                            $ GwenX.Pet_rod = "детки"
                            $ GwenX.Pet_dat = "детке"
                            $ GwenX.Pet_vin = "детку"
                            $ GwenX.Pet_tvo = "деткой"
                            $ GwenX.Pet_pre = "детке"
                            $ GwenX.FaceChange("sexy", 1)
                            ch_g "Я твоя детка, [GwenX.Petname]."
                        else:
                            $ GwenX.FaceChange("angry")
                            ch_g "Я тебе НЕ детка, [GwenX.Petname]."

                    "\"крошка\".":
                        if "boyfriend" in GwenX.Petnames or ApprovalCheck(GwenX, 600, "L"):
                            $ GwenX.FaceChange("sexy", 1)
                            $ GwenX.Pet = "крошка"
                            $ GwenX.Pet_rod = "крошки"
                            $ GwenX.Pet_dat = "крошке"
                            $ GwenX.Pet_vin = "крошку"
                            $ GwenX.Pet_tvo = "крошкой"
                            $ GwenX.Pet_pre = "крошке"
                            ch_g "Я твоя крошка, [GwenX.Petname]."
                        else:
                            $ GwenX.FaceChange("angry")
                            ch_g "Я тебе НЕ крошка, [GwenX.Petname]."

                    "\"малышка\".":
                        if "boyfriend" in GwenX.Petnames or ApprovalCheck(GwenX, 500, "L"):
                            $ GwenX.FaceChange("sexy", 1)
                            $ GwenX.Pet = "малышка"
                            $ GwenX.Pet_rod = "малышки"
                            $ GwenX.Pet_dat = "малышке"
                            $ GwenX.Pet_vin = "малышку"
                            $ GwenX.Pet_tvo = "малышкой"
                            $ GwenX.Pet_pre = "малышке"
                            ch_g "Мило, [GwenX.Petname]."
                        else:
                            $ GwenX.FaceChange("angry")
                            ch_g "Я тебе НЕ малышка."


                    "\"милая\".":
                        if "boyfriend" in GwenX.Petnames or ApprovalCheck(GwenX, 600, "L"):
                            $ GwenX.Pet = "милая"
                            $ GwenX.Pet_rod = "милой"
                            $ GwenX.Pet_dat = "милой"
                            $ GwenX.Pet_vin = "милую"
                            $ GwenX.Pet_tvo = "милой"
                            $ GwenX.Pet_pre = "милой"
                            ch_g "Оу, как мило, [GwenX.Petname]."
                        else:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Слишком приторно, [GwenX.Petname]."

                    "\"секси\".":
                        if "lover" in GwenX.Petnames or ApprovalCheck(GwenX, 800):
                            $ GwenX.FaceChange("sexy", 1)
                            $ GwenX.Pet = "секси"
                            $ GwenX.Pet_rod = "секси"
                            $ GwenX.Pet_dat = "секси"
                            $ GwenX.Pet_vin = "секси"
                            $ GwenX.Pet_tvo = "секси"
                            $ GwenX.Pet_pre = "секси"
                            ch_g "Тебе виднее, [GwenX.Petname]."
                        else:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Ты перегибаешь, [GwenX.Petname]."

                    "\"любимая\".":
                        if "lover" in GwenX.Petnames or ApprovalCheck(GwenX, 1200):
                            $ GwenX.Pet = "любимая"
                            $ GwenX.Pet_rod = "любимой"
                            $ GwenX.Pet_dat = "любимой"
                            $ GwenX.Pet_vin = "любимую"
                            $ GwenX.Pet_tvo = "любимой"
                            $ GwenX.Pet_pre = "любимой"
                            $ GwenX.FaceChange("sexy", 1)
                            ch_g "Я знаю."
                        else:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Я так не думаю, [GwenX.Petname]."

                    "Гвенгвин." if "Gwenguin" in GwenX.Names:
                        if ApprovalCheck(GwenX, 700, "L") and not ApprovalCheck(GwenX, 500, "O"):
                                $ GwenX.Pet = "Гвенгвин"
                                $ GwenX.Pet_rod = "Гвенгвин"
                                $ GwenX.Pet_dat = "Гвенгвин"
                                $ GwenX.Pet_vin = "Гвенгвин"
                                $ GwenX.Pet_tvo = "Гвенгвин"
                                $ GwenX.Pet_pre = "Гвенгвин"
                                ch_g "Странный выбор, но ладно!"
                        else:
                                ch_g "Ни за что."

                    "Назад":
                        pass

            "Грубо":
                menu:
                    "Пожалуй, я буду звать тебя. . ."
                    "\"рабыня\".":
                        if "master" in GwenX.Petnames or ApprovalCheck(GwenX, 800, "O"):
                            $ GwenX.Pet = "рабыня"
                            $ GwenX.Pet_rod = "рабыни"
                            $ GwenX.Pet_dat = "рабыне"
                            $ GwenX.Pet_vin = "рабыню"
                            $ GwenX.Pet_tvo = "рабыней"
                            $ GwenX.Pet_pre = "рабыне"
                            $ GwenX.FaceChange("bemused", 1)
                            ch_g "Как пожелаешь, [GwenX.Petname]."
                        else:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Я тебе не рабыня, [GwenX.Petname]."

                    "\"питомец\".":
                        if "master" in GwenX.Petnames or ApprovalCheck(GwenX, 650, "O"):
                            $ GwenX.Pet = "питомец"
                            $ GwenX.Pet_rod = "питомце"
                            $ GwenX.Pet_dat = "питомцу"
                            $ GwenX.Pet_vin = "питомца"
                            $ GwenX.Pet_tvo = "питомцем"
                            $ GwenX.Pet_pre = "питомце"
                            $ GwenX.FaceChange("bemused", 1)
                            ch_g "Можешь погладить меня, если хочешь, [GwenX.Petname]."
                        else:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Я не твой питомец, [GwenX.Petname]."

                    "\"шлюха\".":
                        if "sex friend" in GwenX.Petnames or ApprovalCheck(GwenX, 900, "OI"):
                            $ GwenX.Pet = "шлюха"
                            $ GwenX.Pet_rod = "шлюхи"
                            $ GwenX.Pet_dat = "шлюхе"
                            $ GwenX.Pet_vin = "шлюху"
                            $ GwenX.Pet_tvo = "шлюхой"
                            $ GwenX.Pet_pre = "шлюхе"
                            $ GwenX.FaceChange("sexy")
                            ch_g "Конечно."
                        else:
                            $ GwenX.FaceChange("angry", 1)
                            $ GwenX.Mouth = "surprised"
                            ch_g "Не для тебя."

                    "\"блядь\".":
                        if "fuckbuddy" in GwenX.Petnames or ApprovalCheck(GwenX, 1000, "OI"):
                            $ GwenX.Pet = "блядь"
                            $ GwenX.Pet_rod = "бляди"
                            $ GwenX.Pet_dat = "бляде"
                            $ GwenX.Pet_vin = "блядь"
                            $ GwenX.Pet_tvo = "блядью"
                            $ GwenX.Pet_pre = "бляде"
                            $ GwenX.FaceChange("sly")
                            ch_g "Ладно. . ."
                        else:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Запомни, я б-о-е-ц. . ."

                    "\"сладкогрудая\".":
                        if "sex friend" in GwenX.Petnames or ApprovalCheck(GwenX, 1400):
                            $ GwenX.Pet = "сладкогрудая"
                            $ GwenX.Pet_rod = "сладкогрудой"
                            $ GwenX.Pet_dat = "сладкогрудой"
                            $ GwenX.Pet_vin = "сладкогрудую"
                            $ GwenX.Pet_tvo = "сладкогрудой"
                            $ GwenX.Pet_pre = "сладкогрудой"
                            $ GwenX.FaceChange("sly", 1)
                            ch_g "Было бы это еще правдой."
                        else:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Это не прикольно."

                    "\"любовница\".":
                        if "sex friend" in GwenX.Petnames or ApprovalCheck(GwenX, 600, "I"):
                            $ GwenX.Pet = "любовница"
                            $ GwenX.Pet_rod = "любовницы"
                            $ GwenX.Pet_dat = "любовнице"
                            $ GwenX.Pet_vin = "любовницу"
                            $ GwenX.Pet_tvo = "любовницей"
                            $ GwenX.Pet_pre = "любовнице"
                            $ GwenX.FaceChange("sly")
                            ch_g "Ага. . ."
                        else:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Эй, не так громко, [GwenX.Petname]."

                    "\"секс-партнерша\".":
                        if "fuckbuddy" in GwenX.Petnames or ApprovalCheck(GwenX, 700, "I"):
                            $ GwenX.Pet = "секс-партнерша"
                            $ GwenX.Pet_rod = "секс-партнерши"
                            $ GwenX.Pet_dat = "секс-партнерше"
                            $ GwenX.Pet_vin = "секс-партнершу"
                            $ GwenX.Pet_tvo = "секс-партнершей"
                            $ GwenX.Pet_pre = "секс-партнерше"
                            $ GwenX.FaceChange("sly")
                            ch_g "Агась."
                        else:
                            $ GwenX.FaceChange("angry", 1)
                            $ GwenX.Mouth = "surprised"
                            if not Player.Male:
                                ch_g "Овца."
                            else:
                                ch_g "Урод."

                    "\"доченька\".":
                        if "daddy" in GwenX.Petnames or ApprovalCheck(GwenX, 1200):
                            $ GwenX.Pet = "доченька"
                            $ GwenX.Pet_rod = "доченьки"
                            $ GwenX.Pet_dat = "доченьке"
                            $ GwenX.Pet_vin = "доченьку"
                            $ GwenX.Pet_tvo = "доченькой"
                            $ GwenX.Pet_pre = "доченьке"
                            $ GwenX.FaceChange("smile", 1)
                            ch_g "Ладно?"
                        else:
                            $ GwenX.FaceChange("angry", 1)
                            ch_g "Это очень странно."

                    "\"Дэдпул\".":
                        if ApprovalCheck(GwenX, 500, "O"):
                            $ GwenX.FaceChange("sexy", 1)
                            $ GwenX.Pet = "Дэдпул"
                            $ GwenX.Pet_rod = "Дэдпула"
                            $ GwenX.Pet_dat = "Дэдпулу"
                            $ GwenX.Pet_vin = "Дэдпула"
                            $ GwenX.Pet_tvo = "Дэдпулом"
                            $ GwenX.Pet_pre = "Дэдпуле"
                            ch_g "Ха, ладно, [GwenX.Petname]."
                        else:
                            $ GwenX.FaceChange("angry")
                            ch_g "Да ни в жизнь!"

                    "\"Гвен Стейси\".":
                        if ApprovalCheck(GwenX, 500, "O"):
                            $ GwenX.Pet = "Гвен Стейси"
                            $ GwenX.Pet_rod = "Гвен Стейси"
                            $ GwenX.Pet_dat = "Гвен Стейси"
                            $ GwenX.Pet_vin = "Гвен Стейси"
                            $ GwenX.Pet_tvo = "Гвен Стейси"
                            $ GwenX.Pet_pre = "Гвен Стейси"
                            $ GwenX.FaceChange("sexy", 1)
                            ch_g "Ха, ладно, [GwenX.Petname]."
                        else:
                            $ GwenX.FaceChange("angry")
                            ch_g "Ты ходишь по тонкому льду, [GwenX.Petname]."
                    "Назад":
                        pass

            "Неважно.":
                return
    return

#label Gwen_Namecheck(GwenX.Pet = GwenX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname


# start Gwen_Rename//////////////////////////////////////////////////////////
label Gwen_Rename:
        #Sets alternate names from Gwen
        $ GwenX.Mouth = "smile"
        ch_g "Да?"
        menu:
            extend ""
            "Я думаю, \"Гвен\" прекрасное имя." if GwenX.Name != "Гвен" and "Gwen" in GwenX.Names:
                    $ GwenX.Name = "Гвен"
                    $ GwenX.Name_rod = "Гвен"
                    $ GwenX.Name_dat = "Гвен"
                    $ GwenX.Name_vin = "Гвен"
                    $ GwenX.Name_tvo = "Гвен"
                    $ GwenX.Name_pre = "Гвен"
                    ch_g "Ага!"
            "Думаю, \"Гвенпул\" звучит круто." if GwenX.Name != "Гвенпул" and "Gwenpool" in GwenX.Names:
                    if not ApprovalCheck(GwenX, 500) and not ApprovalCheck(GwenX, 300, "I"):
                            $ GwenX.FaceChange("confused", 1)
                            ch_g "Странное заявление. . ."
                    else:
                            if "namechange" not in GwenX.DailyActions:
                                    $ GwenX.Statup("Love", 70, 2)
                                    $ GwenX.Statup("Obed", 70, 5)
                            $ GwenX.Name = "Гвенпул"
                            $ GwenX.Name_rod = "Гвенпул"
                            $ GwenX.Name_dat = "Гвенпул"
                            $ GwenX.Name_vin = "Гвенпул"
                            $ GwenX.Name_tvo = "Гвенпул"
                            $ GwenX.Name_pre = "Гвенпул"
                            $ GwenX.FaceChange("sly", 1)
                            ch_g "Ооо, это из-за маски?"
            "Думаю, \"Гвендолин\" звучит круто." if GwenX.Name != "Гвендолин" and "Gwendolyn" in GwenX.Names:
                    if not ApprovalCheck(GwenX, 500):
                            $ GwenX.FaceChange("confused", 1)
                            ch_g "Лаааадно? . ."
                    else:
                            if "namechange" not in GwenX.DailyActions:
                                    $ GwenX.Statup("Love", 70, 2)
                                    $ GwenX.Statup("Obed", 70, 5)
                            $ GwenX.Name = "Гвендолин"
                            $ GwenX.Name_rod = "Гвендолин"
                            $ GwenX.Name_dat = "Гвендолин"
                            $ GwenX.Name_vin = "Гвендолин"
                            $ GwenX.Name_tvo = "Гвендолин"
                            $ GwenX.Name_pre = "Гвендолин"
                            $ GwenX.FaceChange("sly", 1)
                            ch_g "Немного формально, но пойдет."
            "Неважно.":
                    pass
        $ GwenX.AddWord(1,0,"namechange")
        return
# end Gwen_Rename//////////////////////////////////////////////////////////


# start Gwen_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Personality(Cnt = 0):
    if not GwenX.Chat[4] or Cnt:
        "Поскольку у вас все хорошо получается в одной области, вы можете убедить Гвен сосредоточиться на любой другой."
        "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
        "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
    menu:
        ch_g "Да? Что такое?"
        "Больше Послушания. [[Любовь в Послушание]" if GwenX.Love > 900:
            ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
            ch_g "Стать более послушной? С радостью."
            $ GwenX.Chat[4] = 1
        "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if GwenX.Love > 900:
            ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
            ch_g "С радостью."
            $ GwenX.Chat[4] = 2

        "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if GwenX.Obed > 900:
            ch_p "Я хочу, чтобы ты была более раскрепощенной."
            ch_g "Поняла."
            $ GwenX.Chat[4] = 3
        "Больше Любви. [[Повиновение в Любовь]" if GwenX.Obed > 900:
            ch_p "Я хочу, чтобы ты училась любить меня."
            ch_g "Поняла."
            $ GwenX.Chat[4] = 4

        "Больше Повиновения. [[Раскрепощенность в Повиновение]" if GwenX.Inbt > 900:
            ch_p "Я знаю, что нам и так весело, но разве ты не можешь иногда слушаться меня?"
            ch_g "Звучит соблазнительно."
            $ GwenX.Chat[4] = 5

        "Больше Любви. [[Раскрепощенность в Любовь]" if GwenX.Inbt > 900:
            ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
            ch_g "Звучит весело."
            $ GwenX.Chat[4] = 6

        "Просто делай то, что тебе нравится. . .[[Сбросить]" if GwenX.Chat[4]:
            ch_p "Помнишь, что мы обсуждали? Забудь."
            ch_g "Эм. . . ладно?"
            $ GwenX.Chat[4] = 0
        "Повторить правила":
            call Gwen_Personality(1)
            return
        "Неважно.":
            return
    return
# end Gwen_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Gwen_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Gwen_Summon(Tempmod=Tempmod):
    $ GwenX.OutfitChange()
    if "no summon" in GwenX.RecentActions:
                if "no summon" in GwenX.RecentActions:
                    ch_g "Хватит спрашивать!"
                    $ GwenX.AddWord(1,"angry",0,0,0)
                elif Current_Time == "Night":
                    ch_g "Я же сказала, уже поздно. Спокойной ночи."
                else:
                    ch_g "Я же сказала, что я занята."
                $ GwenX.RecentActions.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if GwenX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif GwenX.Loc == "bg dangerroom":
        $ Tempmod = -10
    elif GwenX.Loc == "bg showerroom":
        $ Tempmod = -30

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"
    if Time_Count >= 3: #night time
                if ApprovalCheck(GwenX, 500, "L") or ApprovalCheck(GwenX, 400, "O"):
                        #It's night time but she likes you.
                        ch_g "Ну, я думаю, ты можешь зайти ненадолго."
                        $ GwenX.Loc = bg_current
                        call Taboo_Level
                        call Set_The_Scene
                else:
                        #It's night time and she isn't into you
                        ch_g "Нет, уже довольно поздно."
                        $ GwenX.RecentActions.append("no summon")
                return
    elif "les" in GwenX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(GwenX, 2000):
                    ch_g "Ну, у меня вроде как гости, но ты можешь прийти. . ."
                    menu:
                        extend ""
                        "Конечно.":
                            $ Line = "go to"
                        "Нет, спасибо.":
                            ch_g "Потом будешь жалеть. . ."
                            return
            else:
                    ch_g "О. . . Эм. . . Я тут немного занята."
                    ch_g "Может быть, зайду позже. . ."
                    $ GwenX.RecentActions.append("no summon")
                    return
    elif not ApprovalCheck(GwenX, 700, "L") or not ApprovalCheck(GwenX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(GwenX, 300):
                ch_g "Я занята, [GwenX.Petname]."
                $ GwenX.RecentActions.append("no summon")
                return


        if "summoned" in GwenX.RecentActions:
                pass
        elif "goto" in GwenX.RecentActions:
                if not Player.Male:
                    ch_g "Ты только что ушла. . ."
                else:
                    ch_g "Ты только что ушел. . ."
        elif GwenX.Loc == "bg classroom":
                ch_g "Я на занятиях, не хочешь тоже прийти?"
        elif GwenX.Loc == "bg dangerroom":
                ch_g "Я в Комнате Опасности, [GwenX.Petname], хочешь зайти?"
        elif GwenX.Loc == "bg campus":
                ch_g "Я сейчас во дворе, хочешь присоединиться ко мне?"
        elif GwenX.Loc == "bg gwen":
                ch_g "Я в своей комнате, [GwenX.Petname], хочешь присоединиться ко мне?"
        elif GwenX.Loc == "bg player":
                ch_g "Я в твоей комнате, [GwenX.Petname], где ты?"
        elif GwenX.Loc == "bg showerroom":
            if ApprovalCheck(GwenX, 1600):
                ch_g "Я сейчас в душе. хочешь присоединиться ко мне?"
            else:
                ch_g "Я сейчас в душе, [GwenX.Petname]. Увидимся позже."
                $ GwenX.RecentActions.append("no summon")
                return
        elif GwenX.Loc == "hold":
                ch_g "Извини, я немного сейчас занята."
                $ GwenX.RecentActions.append("no summon")
                return
        else:
                ch_g "Ты всегда можешь прийти ко мне. . ."


        if "summoned" in GwenX.RecentActions:
            ch_g "Снова? Ну хорошо."
            $ Line = "yes"
        elif "goto" in GwenX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
#                                ch_g "See you when you get here."
                                $ Line = "go to"
                "Нет.":
                                ch_g "Как хочешь."
                "Мне бы {i}очень{/i} хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(GwenX, 600, "L") or ApprovalCheck(GwenX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(GwenX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(GwenX, 1400):
                                #she is generally favorable
                                ch_g "Хорошо."
                                $ Line = "yes"
                        elif ApprovalCheck(GwenX, 200, "O"):
                                #she is not obedient
                                ch_g "Мне все равно."
                                ch_g "Если что, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(GwenX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(GwenX, 1400):
                                #she is generally favorable
                                ch_g "Хорошо."
                                $ Line = "yes"
                        elif ApprovalCheck(GwenX, 200, "O"):
                                #she is not obedient
                                ch_g "Мне все равно."
                                ch_g "Если что, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Конечно, сейчас приду.":
                    $ GwenX.Statup("Love", 55, 1)
                    $ GwenX.Statup("Inbt", 30, 1)
#                    ch_g "See you when you get here."
                    $ Line = "go to"

                "Нет, поговорим позже.":
                    $ GwenX.Statup("Obed", 50, 1)
                    $ GwenX.Statup("Obed", 30, 2)
                    ch_g "Хорошо. Тогда увидимся в другой раз."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                    if ApprovalCheck(GwenX, 650, "L") or ApprovalCheck(GwenX, 1500):
                        $ GwenX.Statup("Love", 70, 1)
                        $ GwenX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ GwenX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                        ch_g "Оу, это так мило!"

                "Давай, будет весело.":
                    if ApprovalCheck(GwenX, 400, "L") and ApprovalCheck(GwenX, 800):
                        $ GwenX.Statup("Love", 70, 1)
                        $ GwenX.Statup("Obed", 50, 1)
                        $ Line = "fun"
                    else:
                        $ GwenX.Statup("Inbt", 30, 1)
                        $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                    if ApprovalCheck(GwenX, 600, "O"):
                        #she is obedient
                        $ GwenX.Statup("Love", 50, 1, 1)
                        $ GwenX.Statup("Love", 40, -1)
                        $ GwenX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(GwenX, 1500):
                        #she is generally favorable
                        $ GwenX.Statup("Love", 70, -2)
                        $ GwenX.Statup("Love", 90, -1)
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 90, 1)
                        ch_g "Ладно, хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(GwenX, 200, "O"):
                        #she is not obedient
                        $ GwenX.Statup("Love", 60, -4)
                        $ GwenX.Statup("Love", 90, -3)
                        ch_g "Даже не пытайся."
                        $ GwenX.Statup("Inbt", 40, 2)
                        $ GwenX.Statup("Inbt", 60, 1)
                        $ GwenX.Statup("Obed", 70, -3)
                        ch_g "Я не приду."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ GwenX.Statup("Inbt", 30, 1)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Love", 50, -1, 1)
                        $ GwenX.Statup("Obed", 70, -1)
                        $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                    if ApprovalCheck(GwenX, 600, "O"):
                        #she is obedient
                        $ GwenX.Statup("Love", 50, 1, 1)
                        $ GwenX.Statup("Love", 40, -1)
                        $ GwenX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(GwenX, 1500):
                        #she is generally favorable
                        $ GwenX.Statup("Love", 70, -2)
                        $ GwenX.Statup("Love", 90, -1)
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 90, 1)
                        ch_g "Ладно, хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(GwenX, 200, "O"):
                        #she is not obedient
                        $ GwenX.Statup("Love", 60, -4)
                        $ GwenX.Statup("Love", 90, -3)
                        ch_g "Даже не пытайся."
                        $ GwenX.Statup("Inbt", 40, 2)
                        $ GwenX.Statup("Inbt", 60, 1)
                        $ GwenX.Statup("Obed", 70, -3)
                        ch_g "Я не приду."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ GwenX.Statup("Inbt", 30, 1)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Love", 50, -1, 1)
                        $ GwenX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if GwenX.Love > GwenX.Obed:
            ch_g "Конечно!"
        else:
            ch_g "Ладно, уже иду."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ GwenX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            if GwenX.Loc == "bg classroom":
                ch_g "Я никак не могу пропустить эту лекцию."
            elif GwenX.Loc == "bg dangerroom":
                ch_g "Я только разогрелась!"
            else:
                ch_g "Извини, [GwenX.Petname], я немного занята."
            $ GwenX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ GwenX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            $ Nearby = []
            $ Line = 0
            $ Party = [GwenX]
            if GwenX.Loc == "bg classroom":
                    ch_g "Хорошо, найди меня, когда придешь."
                    jump Class_Room
            elif GwenX.Loc == "bg dangerroom":
                    ch_g "Ладно, я пока разогреюсь."
                    jump Danger_Room
            elif GwenX.Loc == "bg gwen":
                    ch_g "Я. . . немного приберусь."
                    jump Gwen_Room
            elif GwenX.Loc == "bg player":
                    ch_g "Я буду ждать."
                    jump Player_Room
            elif GwenX.Loc == "bg showerroom":
                    ch_g "Я оставлю тебе немного горячей воды."
                    jump Shower_Room
            elif GwenX.Loc == "bg campus":
                    ch_g "Увидимся."
                    jump Campus
            elif GwenX.Loc != "hold":
                    ch_g "Ага, увидимся."
                    $ bg_current = GwenX.Loc
                    jump Misplaced
            else:
                    ch_g "Эм, я просто встречусь с тобой в своей комнате."
                    $ GwenX.Loc = "bg gwen"
                    jump Gwen_Room

    #She's agreed to come over
    elif Line == "lonely":
            if not Player.Male:
                ch_g "Я не могу оставить тебя одну ни на секунду."
            else:
                ch_g "Я не могу оставить тебя одного ни на секунду."
    elif Line == "command":
            ch_g "Ладно, [GwenX.Petname]."
    elif Line == "fun":
            ch_g "Конечно."

    $ GwenX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(GwenX)
            return
    $ GwenX.Loc = bg_current
    call Taboo_Level(0)
    $ GwenX.OutfitChange()
    call Set_The_Scene
    return

# End Gwen Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Gwen_Leave(Tempmod=Tempmod, GirlsNum = 0):
    if "leaving" in GwenX.RecentActions:
        $ GwenX.DrainWord("leaving")
    else:
        return

    if GwenX.Loc == "hold":
            # Activates if she's being moved out of play
            ch_g "Мне нужно отлучиться ненадолго, увидимся позже."
            return

    if GwenX in Party or "lockedtravels" in GwenX.Traits:
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ GwenX.Loc = bg_current
            return

    elif "freetravels" in GwenX.Traits or not ApprovalCheck(GwenX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.
            $ GwenX.OutfitChange()
            if GirlsNum: #if someone left before her
                        ch_g "Ага, я тоже ухожу."

            if GwenX.Loc == "bg classroom":
                        ch_g "У меня занятия."
            elif GwenX.Loc == "bg dangerroom":
                        ch_g "Я иду в Комнату Опасности."
            elif GwenX.Loc == "bg campus":
                        ch_g "Я иду во двор."
            elif GwenX.Loc == "bg gwen":
                        ch_g "Я возвращаюсь в свою комнату."
            elif GwenX.Loc == "bg player":
                        ch_g "Я немного посижу в твоей комнате."
            elif GwenX.Loc == "bg pool":
                        ch_g "Я иду в бассейн."
            elif GwenX.Loc == "bg showerroom":
                if ApprovalCheck(GwenX, 1400):
                        ch_g "Я собираюсь принять душ."
                else:
                        ch_g "Увидимся."
            else:
                        ch_g "Увидимся позже."
            hide Gwen_Sprite
            hide Gwen_Seated
            return
            #End Free Travels

    if bg_current == "bg dangerroom":
            call Gym_Exit([GwenX])

    $ GwenX.OutfitChange()

    if "follow" not in GwenX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ GwenX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    # Sets her preferences
    if GwenX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif GwenX.Loc == "bg dangerroom":
        $ Tempmod = 20
    elif GwenX.Loc == "bg showerroom":
        $ Tempmod = 40


    if GirlsNum: #if someone left before her
                ch_g "Ага, я тоже ухожу."

    if GwenX.Loc == "bg classroom":
        ch_g "У меня занятия, хочешь присоединиться ко мне?"
    elif GwenX.Loc == "bg dangerroom":
        ch_g "У меня тренировка в Комнате Опасности, хочешь присоединиться ко мне?"
    elif GwenX.Loc == "bg campus":
        ch_g "Я пойду вздремну на площади, ты хочешь присоединиться ко мне?"
    elif GwenX.Loc == "bg gwen":
        ch_g "Я возвращаюсь в свою комнату, ты хочешь присоединиться ко мне?"
    elif GwenX.Loc == "bg player":
        ch_g "Я собираюсь немного посидеть в твоей комнате, ты присоединишься ко мне?"
    elif GwenX.Loc == "bg mall":
        ch_g "Я направляюсь в торговый центр, хочешь присоединиться ко мне?"
    elif GwenX.Loc == "bg showerroom":
        if ApprovalCheck(GwenX, 1600):
            ch_g "Я собираюсь в душ, ты хочешь присоединиться ко мне?"
        else:
            ch_g "Я собираюсь в душ, до встречи."
            return
    elif GwenX.Loc == "bg pool":
            ch_g "Я иду в бассейн. Хочешь присоединиться ко мне?"
    else:
            ch_g "Хочешь присоединиться ко мне?"


    menu:
        extend ""
        "Конечно, я сразу за тобой.":
                if "followed" not in GwenX.RecentActions:
                    $ GwenX.Statup("Love", 55, 1)
                    $ GwenX.Statup("Inbt", 30, 1)
                $ Line = "go to"

        "Нет, поговорим позже.":
                if "followed" not in GwenX.RecentActions:
                    $ GwenX.Statup("Obed", 50, 1)
                    $ GwenX.Statup("Obed", 30, 2)
                ch_g "Хорошо, здорово."

        "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                if ApprovalCheck(GwenX, 650, "L") or ApprovalCheck(GwenX, 1500):
                    if "followed" not in GwenX.RecentActions:
                        $ GwenX.Statup("Love", 70, 1)
                        $ GwenX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else:
                    if "followed" not in GwenX.RecentActions:
                        $ GwenX.Statup("Inbt", 30, 1)
                    $ Line = "no"
                    ch_g "Оу, это так мило!"

        "Давай, будет весело.":
                if ApprovalCheck(GwenX, 400, "L") and ApprovalCheck(GwenX, 800):
                    $ GwenX.Statup("Love", 70, 1)
                    $ GwenX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else:
                    $ GwenX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Нет, останься здесь.":
                if ApprovalCheck(GwenX, 600, "O"):
                    #she is obedient
                    if "followed" not in GwenX.RecentActions:
                        $ GwenX.Statup("Love", 40, -2)
                        $ GwenX.Statup("Obed", 90, 1)
                    $ Line = "command"

                elif D20 >= 7 and ApprovalCheck(GwenX, 1400):
                    #she is generally favorable
                    if "followed" not in GwenX.RecentActions:
                        $ GwenX.Statup("Love", 70, -2)
                        $ GwenX.Statup("Love", 90, -1)
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 90, 1)
                    ch_g "Хорошо, я могу немного задержаться."
                    $ Line = "yes"

                elif ApprovalCheck(GwenX, 200, "O"):
                    #she is not obedient
                    if "followed" not in GwenX.RecentActions:
                        $ GwenX.Statup("Love", 70, -4)
                        $ GwenX.Statup("Love", 90, -2)
                    ch_g "Не командуй мной."
                    if "followed" not in GwenX.RecentActions:
                        $ GwenX.Statup("Inbt", 40, 2)
                        $ GwenX.Statup("Inbt", 60, 1)
                        $ GwenX.Statup("Obed", 70, -2)
                    ch_g "Не-а, я пошла."
                else:
                    #she is obedient, but you failed to meet the checks
                    if "followed" not in GwenX.RecentActions:
                        $ GwenX.Statup("Inbt", 30, 1)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Love", 50, -1, 1)
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Obed", 70, -1)
                    $ Line = "no"
                #End ordered to stay

    call Taboo_Level(0)
    $ GwenX.RecentActions.append("followed")
    if not Line:
            #You end the dialog neutrally
            hide Gwen_Sprite
            hide Gwen_Seated
            call Gym_Clothes_Off([GwenX])
            return

    if Line == "no":
            # She's refused, context based dialog
            if GwenX.Loc == "bg classroom":
                ch_g "Я никак не могу пропустить это занятие."
            elif GwenX.Loc == "bg dangerroom":
                ch_g "Извини, [GwenX.Petname], но мне очень нужно потренироваться."
            else:
                ch_g "Извини, у меня дела."
            hide Gwen_Sprite
            hide Gwen_Seated
            call Gym_Clothes_Off([GwenX])
            return

    elif Line == "go to":
            #You agreed to go to her instead
            #$ Party.append(GwenX)
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")
            $ GwenX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            hide Gwen_Sprite
            hide Gwen_Seated
            $ Nearby = []
            $ Party = [GwenX]
            call Gym_Clothes_Off([GwenX])
            if GwenX.Loc == "bg classroom":
                ch_g "Хорошо, я займу тебе место."
                jump Class_Room_Entry
            elif GwenX.Loc == "bg dangerroom":
                ch_g "Я пока разогреюсь."
                jump Danger_Room_Entry
            elif GwenX.Loc == "bg gwen":
                ch_g "Ладно."
                jump Gwen_Room
            elif GwenX.Loc == "bg player":
                ch_g "Хорошо."
                jump Player_Room
            elif GwenX.Loc == "bg showerroom":
                ch_g "Ладно, хорошо."
                jump Shower_Room_Entry
            elif GwenX.Loc == "bg campus":
                ch_g "Ладно, хорошо."
                jump Campus_Entry
            elif GwenX.Loc == "bg pool":
                ch_g "Клево."
                jump Pool_Entry
            elif GwenX.Loc == "bg mall":
                ch_g "Клево."
                jump Mall_Entry
            else:
                ch_g "Я просто встречусь с тобой в твоей комнате."
                $ GwenX.Loc = "bg player"
                jump Player_Room
            #End "goto" where she's at

    #She's agreed to come over
    elif Line == "lonely":
            if not Player.Male:
                ch_g "Оу, ну как я могу оставить тебя одну. . ."
            else:
                ch_g "Оу, ну как я могу оставить тебя одного. . ."
    elif Line == "command":
            ch_g "Ладно, [GwenX.Petname]."
    elif Line:
            ch_g "Конечно."

    $ Line = 0
    ch_g "Я останусь здесь."
    $ GwenX.Loc = bg_current
    call Taboo_Level(0)
    return

# End Gwen Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

### Gwen's Clothes  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Gwen_Clothes:
    if GwenX.Taboo:
            if "exhibitionist" in GwenX.Traits:
                ch_g "Да? . ."
            elif ApprovalCheck(GwenX, 900, TabM=4) or ApprovalCheck(GwenX, 400, "I", TabM=3):
                ch_g "Мне не стоит раздеваться здесь. . ."
            else:
                ch_g "Мне не стоит раздеваться здесь. . ."
                ch_g "Разве мы не могли поговорить об этом в наших комнатах?"
                return
    elif ApprovalCheck(GwenX, 900, TabM=4) or ApprovalCheck(GwenX, 600, "L") or ApprovalCheck(GwenX, 300, "O"):
                ch_g "Что ты хочешь?"
    else:
                ch_g "Почему ты беспокоишься о том, что на мне надето?"
                return

    if Girl != GwenX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = GwenX
    call Shift_Focus(Girl)

label Gwen_Wardrobe_Menu:
    $ GwenX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .
    while True:
        menu:
            ch_g "Что ты хочешь обсудить?"
            "Верх":
                        call Gwen_Clothes_Over
            "Низ":
                        call Gwen_Clothes_Legs
            "Нижнее белье":
                        call Gwen_Clothes_Under
            "Аксессуары":
                        call Gwen_Clothes_Misc
            "Управление нарядами":
                        call Gwen_Clothes_Outfits
            "Давай поговорим о том, что ты носишь.":
                        call Clothes_Schedule(GwenX)

            "Могу я посмотреть?" if GwenX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(GwenX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_g "Хорошо, как я выгляжу?"
                    hide PhoneSex
            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(GwenX,0,2)
                    if _return:
                        hide DressScreen
            "Может, тебе будет комфортнее за ширмой? (locked)" if GwenX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if GwenX.Loc == bg_current and not GwenX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if not Player.Male and "girltalk" not in GwenX.History and "nogirls" not in GwenX.History:
                            ch_g "Разве она необходима?"
                    elif ApprovalCheck(GwenX, 1500) or (GwenX.SeenChest and GwenX.SeenPussy):
                            ch_g "Не думаю, что она мне пригодится."
                    else:
                            show DressScreen zorder 150
                            ch_g "Ага, так лучше, спасибо."

            "У меня есть подарок для тебя (locked)" if GwenX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if GwenX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(GwenX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ GwenX.OutfitChange()
                    $ GwenX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != GwenX:
                            ch_p "Я хочу поговорить о твоей одежде."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = GwenX
                    call Shift_Focus(Girl)

            "Сменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current:
                    pass
            "Сменить вид" if Girl.Loc == bg_current:
                    call WardrobeView(GwenX)

            "Неважно, ты и так хорошо выглядишь":
                    call Girl_Pos_Reset(GwenX)
                    if "wardrobe" not in GwenX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if GwenX.Chat[1] <= 1:
                                    $ GwenX.Statup("Love", 70, 15)
                                    $ GwenX.Statup("Obed", 40, 20)
                                    ch_g "О! Спасибо!"
                            elif GwenX.Chat[1] <= 10:
                                    $ GwenX.Statup("Love", 70, 5)
                                    $ GwenX.Statup("Obed", 40, 7)
                                    ch_g "Правда?"
                            elif GwenX.Chat[1] <= 50:
                                    $ GwenX.Statup("Love", 70, 1)
                                    $ GwenX.Statup("Obed", 40, 1)
                                    ch_g "Угу."
                            else:
                                    ch_g "Конечно."
                            $ GwenX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(GwenX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ GwenX.OutfitChange()
                    $ GwenX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ GwenX.Chat[1] += 1
                    $ Trigger = 0
                    if GwenX.Panties and "pantyless" in GwenX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ GwenX.DailyActions.remove("pantyless")
                    return

        #Loops back up
        #return #jump Gwen_Clothes
        #End of Gwen Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Gwen_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(GwenX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(GwenX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(GwenX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(GwenX,4,1)
                    "Одежда для сна":
                                call OutfitShame(GwenX,7,1)
                    "Купальник":
                                call OutfitShame(GwenX,10,1)

                    "Повседневка 1" if ApprovalCheck(GwenX, 2500):
                                call OutfitShame(GwenX,11,1)
                    "Повседневка 2" if ApprovalCheck(GwenX, 2500):
                                call OutfitShame(GwenX,12,1)
                    #8 is Emma's teaching clothes,
                    "Неважно":
                                pass

        "Примерь супергеройский костюм":
                $ GwenX.OutfitChange("casual1")
                menu:
                    "Ты должна носить его. [[Выбрать текущий наряд]":
                            $ GwenX.Outfit = "casual1"
                            $ GwenX.Shame = 0
                            ch_g "Ага, эх, даже на ностальгию пробило."
                    "Давай попробуем что-нибудь другое.":
                            ch_g "Ладно."

        "Не носи маску" if GwenX.Casual1[12] == "mask":
                ch_p "Не носи маску, когда на тебе костюм."
                ch_g "Ох. . . Ладно."
                $ GwenX.Casual1[12] = 0
        "Носи маску" if GwenX.Casual1[12] != "mask":
                ch_p "Ты должна носить маску, когда на тебе костюм."
                ch_g "Ох. . . Ладно."
                $ GwenX.Casual1[12] = "mask"

        "Примерь футболку и шорты":
                $ GwenX.OutfitChange("casual2")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                            $ GwenX.Outfit = "casual2"
                            $ GwenX.Shame = 0
                            ch_g "Ага, это мой основной образ."
                    "Давай попробуем что-нибудь другое.":
                            ch_g "Ладно."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not GwenX.Custom1[0] and not GwenX.Custom2[0] and not GwenX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if GwenX.Custom1[0] or GwenX.Custom2[0] or GwenX.Custom3[0]:
                $ Cnt = 0
                while 1:
                    menu:
                        "Надень Пользовательский 1 (locked)" if not GwenX.Custom1[0]:
                                pass
                        "Надень Пользовательский 1" if GwenX.Custom1[0]:
                                $ GwenX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Надень Пользовательский 2 (locked)" if not GwenX.Custom2[0]:
                                pass
                        "Надень Пользовательский 2" if GwenX.Custom2[0]:
                                $ GwenX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Надень Пользовательский 3 (locked)" if not GwenX.Custom3[0]:
                                pass
                        "Надень Пользовательский 3" if GwenX.Custom3[0]:
                                $ GwenX.OutfitChange("custom3")
                                $ Cnt = 6

                        "Ты должна одеваться так, когда мы наедине. (locked)" if not Cnt:
                                pass
                        "Ты должна одеваться так, когда мы наедине." if Cnt:
                                if Cnt == 5:
                                    $ GwenX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ GwenX.Clothing[9] = "custom3"
                                else:
                                    $ GwenX.Clothing[9] = "custom1"
                                ch_g "Хорошо, конечно."

                        "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                menu:
                                    "Пользовательский 1 [[очистить слот 1]" if GwenX.Custom1[0]:
                                        ch_g "Ладно."
                                        $ GwenX.Custom1[0] = 0
                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not GwenX.Custom1[0]:
                                        pass
                                    "Пользовательский 2 [[очистить слот 2]" if GwenX.Custom2[0]:
                                        ch_g "Ладно."
                                        $ GwenX.Custom2[0] = 0
                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not GwenX.Custom2[0]:
                                        pass
                                    "Пользовательский 3 [[очистить слот 3]" if GwenX.Custom3[0]:
                                        ch_g "Ладно."
                                        $ GwenX.Custom3[0] = 0
                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not GwenX.Custom3[0]:
                                        pass
                                    "Неважно [[назад]":
                                        pass

                        "Тебе следует надеть его. [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                pass
                        "Тебе следует надеть его." if Cnt:
                                call Custom_Out(GwenX,Cnt)
                        "Ладно, вернемся к началу нашего разговора. . .":
                                $ Cnt = 0
                                return #jump Gwen_Clothes

        "Наденешь спортивную одежду?" if not GwenX.Taboo or bg_current == "bg dangerroom":
                $ GwenX.OutfitChange("gym")

        "Наденешь одежду для сна?" if not GwenX.Taboo:
                if ApprovalCheck(GwenX, 1200):
                        $ GwenX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(GwenX)
                        if _return:
                            $ GwenX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (GwenX.Taboo and bg_current != "bg pool" and not ApprovalCheck(GwenX, 800, TabM=2)) or not GwenX.Swim[0]:
                $ GwenX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not GwenX.Taboo or bg_current == "bg pool" or ApprovalCheck(GwenX, 800, TabM=2)) and GwenX.Swim[0]:
                $ GwenX.OutfitChange("swimwear")

        "Наденешь хэллоуинский костюм?" if "halloween" in GwenX.History:
                ch_g "Ладно."
                $ GwenX.OutfitChange("costume")

        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ GwenX.FaceChange("sexy", 1)
                $ Line = 0
                if not GwenX.Chest and not GwenX.Panties and not GwenX.Over and not GwenX.Legs and not GwenX.Hose:
                    if not Player.Male:
                        ch_g "Ага. . . подожди, с чего ты взяла?"
                    else:
                        ch_g "Ага. . . подожди, с чего ты взял?"
                elif GwenX.SeenChest and GwenX.SeenPussy and ApprovalCheck(GwenX, 1200, TabM=4):
                    ch_g "Ну, ага. . ."
                    $ Line = 1
                elif ApprovalCheck(GwenX, 2000, TabM=4):
                    ch_g "Ого, это очень возбуждает. . ."
                    $ Line = 1
                elif GwenX.SeenChest and GwenX.SeenPussy and ApprovalCheck(GwenX, 1200, TabM=0):
                    ch_g "Возможно, но не здесь . ."
                elif ApprovalCheck(GwenX, 2000, TabM=0):
                    ch_g "Возможно, но не здесь . ."
                elif ApprovalCheck(GwenX, 1000, TabM=0):
                    $ GwenX.FaceChange("confused", 1,Mouth="smirk")
                    ch_g "Ага, но я не хвастаюсь своим телом."
                    $ GwenX.FaceChange("bemused", 0)
                else:
                    $ GwenX.FaceChange("angry", 1)
                    ch_g "Зачем ты об этом говоришь?"

                call expression GwenX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in GwenX.History:
                        $ Line = 0
                if Line:
                    #If she got nude. . .
                    $ GwenX.OutfitChange("nude")
                    "Она сбрасывает одежду к своим ногам."
                    call Girl_First_Topless(GwenX)
                    call Girl_First_Bottomless(GwenX,1)
                    $ GwenX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется. что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in GwenX.Traits:
                                ch_g "Мммм. . ."
                                $ GwenX.Outfit = "nude"
                                $ GwenX.Statup("Lust", 50, 10)
                                $ GwenX.Statup("Lust", 70, 5)
                                $ GwenX.Shame = 50
                            elif ApprovalCheck(GwenX, 800, "I") or ApprovalCheck(GwenX, 2800, TabM=0):
                                ch_g "Мне стало так жарко. . ."
                                $ GwenX.Outfit = "nude"
                                $ GwenX.Shame = 50
                            else:
                                $ GwenX.FaceChange("sexy", 1)
                                $ GwenX.Eyes = "surprised"
                                ch_g "Ни за что."

                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in GwenX.Traits:
                                if not Player.Male:
                                    ch_g "Уверена?"
                                else:
                                    ch_g "Уверен?"
                            elif ApprovalCheck(GwenX, 800, "I") or ApprovalCheck(GwenX, 2800, TabM=0):
                                $ GwenX.FaceChange("bemused", 1)
                                if not Player.Male:
                                    ch_g "Хм, значит, ты не пыталась вытащить меня в таком виде на люди. . ."
                                else:
                                    ch_g "Хм, значит, ты не пытался вытащить меня в таком виде на люди. . ."
                                ch_g ". . ."
                            else:
                                $ GwenX.FaceChange("confused", 1)
                                if not Player.Male:
                                    ch_g "Ага, я не против, чтобы ты смотрела на мое обнаженное тело, но. . ."
                                else:
                                    ch_g "Ага, я не против, чтобы ты смотрел на мое обнаженное тело, но. . ."
                $ Line = 0

        "Неважно":
            return #jump Gwen_Clothes

    if GwenX.Panties and "pantyless" in GwenX.DailyActions:  #resets pantyless state if you had her put a pair on
            $ GwenX.DailyActions.remove("pantyless")
    return #jump Gwen_Clothes
    #End of Gwen Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Gwen_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять [get_clothing_name(GwenX.Over_key, vin)]?" if GwenX.Over:
                call Wardrobe_Remove(GwenX)

        "Примерь верх супергеройского костюма." if GwenX.Over != "suit":
                $ GwenX.FaceChange("bemused")
                if not GwenX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_g "Конечно."
                elif ApprovalCheck(GwenX, 800, TabM=0):
                    ch_g "Ага, ладно."
                else:
                    call Display_DressScreen(GwenX)
                    if not _return:
                            $ GwenX.FaceChange("bemused", 1)
                            ch_g "Я не хочу сейчас переодевать [get_clothing_name(GwenX.Over_key, vin)]."
                            return #jump Gwen_Clothes
                $ GwenX.Over = "suit"

        "Давай попробуем расстегнутый верх костюма." if GwenX.Over != "open suit" and GwenX.Over == "suit":
                $ GwenX.FaceChange("bemused")
                if not GwenX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_g "Конечно."
                elif  ApprovalCheck(GwenX, 800, TabM=3) and (GwenX.Chest or GwenX.SeenChest):
                    ch_g "Ага, ладно."
                else:
                    call Display_DressScreen(GwenX)
                    if not _return:
                            $ GwenX.FaceChange("bemused", 1)
                            ch_g "Я сейчас не хочу его расстегивать."
                            return #jump Gwen_Clothes
                $ GwenX.Over = "open suit"

        "Примерь свою футболку." if GwenX.Over != "tshirt":
                $ GwenX.FaceChange("bemused")
                if not GwenX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_g "Конечно."
                elif ApprovalCheck(GwenX, 800, TabM=0):
                    ch_g "Ага, ладно."
                else:
                    call Display_DressScreen(GwenX)
                    if not _return:
                            $ GwenX.FaceChange("bemused", 1)
                            ch_g "Я не хочу сейчас переодевать [get_clothing_name(GwenX.Over_key, vin)]."
                            return #jump Gwen_Clothes
                $ GwenX.Over = "tshirt"

        "Может, наденешь топик чирлидерши?" if GwenX.Over != "cheer top" and "halloween" in GwenX.History:
                $ GwenX.FaceChange("bemused")
                if not GwenX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_g "Конечно."
                elif ApprovalCheck(GwenX, 800, TabM=0):
                    ch_g "Ага, ладно."
                else:
                    call Display_DressScreen(GwenX)
                    if not _return:
                            $ GwenX.FaceChange("bemused", 1)
                            ch_g "Я не хочу сейчас переодевать [get_clothing_name(GwenX.Over_key, vin)]."
                            return #jump Gwen_Clothes
                $ GwenX.Over = "cheer top"

        "Может, просто накинешь полотенце?" if GwenX.Over != "towel":
                $ GwenX.FaceChange("bemused", 1)
                if GwenX.Chest or GwenX.SeenChest:
                    ch_g "Странный выбор."
                elif ApprovalCheck(GwenX, 1000, TabM=0):
                    $ GwenX.FaceChange("perplexed", 1)
                    ch_g "Хм, ладно. . ."
                else:
                    call Display_DressScreen(GwenX)
                    if not _return:
                            ch_g "Мне не стоит это делать."
                            return #jump Gwen_Clothes
                $ GwenX.Over = "towel"

        "Неважно":
            pass
    return #jump Gwen_Clothes
    #End of Gwen Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Gwen_NoBra:
        menu:
            ch_g "Под [get_clothing_name(GwenX.Over_key, tvo)] у меня совсем ничего нет. . ."
            "Тогда надень что-нибудь. . .":
                        if GwenX.SeenChest and ApprovalCheck(GwenX, 1000, TabM=3):
                                $ GwenX.Blush = 1
                                ch_g "-Я не сказала, что меня это беспокоит. . ."
                                $ GwenX.Blush = 0
                        elif ApprovalCheck(GwenX, 1200, TabM=4):
                                $ GwenX.Blush = 1
                                ch_g "-Я не сказала, что меня это беспокоит. . ."
                                $ GwenX.Blush = 0
                        elif ApprovalCheck(GwenX, 900, TabM=2) and "lace bra" in GwenX.Inventory:
                                ch_g "Наверное, я смогу что-нибудь подобрать."
                                $ GwenX.Chest  = "lace bra"
                                "Она достает кружевной лифчик и надевает его под [get_clothing_name(GwenX.Over_key, vin)]."
                        elif ApprovalCheck(GwenX, 600, TabM=2):
                                ch_g "Ага, наверное, так и сделаю."
                                $ GwenX.Chest = "tank"
                                "Она достает белую майку и надевает ее под [get_clothing_name(GwenX.Over_key, vin)]."
                        else:
                                ch_g "Ага, но мне не хочется."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(GwenX, 1100, "LI", TabM=2) and GwenX.Love > GwenX.Inbt:
                                ch_g "Для тебя? Наверное. . ."
                        elif ApprovalCheck(GwenX, 700, "OI", TabM=2) and GwenX.Obed > GwenX.Inbt:
                                ch_g "Конечно. . ."
                        elif ApprovalCheck(GwenX, 600, "I", TabM=2):
                                ch_g "Ага. . ."
                        elif ApprovalCheck(GwenX, 1300, TabM=2):
                                ch_g "Ну, наверное."
                        else:
                                $ GwenX.FaceChange("surprised")
                                $ GwenX.Brows = "angry"
                                if GwenX.Taboo > 20:
                                    ch_g "Только не на людях!"
                                else:
                                    if not Player.Male:
                                        ch_g "Ты не настолько милая, [GwenX.Petname]!"
                                    else:
                                        ch_g "Ты не настолько милый, [GwenX.Petname]!"
                                call expression GwenX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0
            "Неважно.":
                        ch_g "Ладно. . ."
                        return 0
        return 1
        #End of Gwen bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Gwen_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(GwenX.Legs_key, vin)]." if GwenX.Legs:
                call Wardrobe_Remove(GwenX,1)

        "Надень супергеройские шорты" if GwenX.Legs != "suit":
                ch_p "Ты отлично выглядишь в шортах от супергеройского костюма."
                ch_g "Ага, ладно."
                $ GwenX.Legs = "suit"

        "Надень розовые шорты" if GwenX.Legs != "shorts":
                ch_p "Ты отлично выглядишь в розовых шортах."
                ch_g "Ага, ладно."
                $ GwenX.Legs = "shorts"

        "Надень розовую юбку" if GwenX.Legs != "skirt":
                ch_p "Как насчет того, чтобы надеть свою розовую юбку?"
                ch_g "Ага, ладно."
                $ GwenX.Legs = "skirt"

        "Надень юбку чирлидерши" if GwenX.Legs != "cheer skirt" and "halloween" in GwenX.History:
                ch_p "Как насчет того, чтобы надеть юбку чирлидерши?"
                ch_g "Ага, ладно."
                $ GwenX.Legs = "cheer skirt"

        "Сними обувь (locked)" if not GwenX.Boots:
                pass
        "Сними [get_clothing_name(GwenX.Boots_key, vin)]" if GwenX.Boots:
                ch_p "Может, снимешь [get_clothing_name(GwenX.Boots_key, vin)]?"
                ch_g "Ладно."
                $ GwenX.Boots = 0
        "Надень ботинки" if GwenX.Boots != "boots":
                ch_p "Может, наденешь ботинки?"
                ch_g "Ладно."
                $ GwenX.Boots = "boots"
        "Надень кеды" if GwenX.Boots != "sneaks":
                ch_p "Может, наденешь кеды?"
                ch_g "Ладно."
                $ GwenX.Boots = "sneaks"

        "Неважно":
                pass
    return #jump Gwen_Clothes
    #End of Gwen Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Gwen_NoPantiesOn:
        menu:
            ch_g "На мне нет трусиков. . ."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if GwenX.SeenPussy and ApprovalCheck(GwenX, 1100, TabM=4):
                                $ GwenX.Blush = 1
                                ch_g "Нет, мне нравится ветерок. . ."
                                $ GwenX.Blush = 0
                        elif ApprovalCheck(GwenX, 1500, TabM=4):
                                $ GwenX.Blush = 1
                                ch_g "Нет, мне нравится ветерок. . ."
                                $ GwenX.Blush = 0
                        elif ApprovalCheck(GwenX, 700, TabM=4):
                                ch_g "Ага, наверное, так и сделаю."
                                if "lace panties" in GwenX.Inventory:
                                        ch_g "Мне нравится ход твоих мыслей."
                                        $ GwenX.Panties  = "lace panties"
                                else:
                                        $ GwenX.Panties = "white panties"
                                if ApprovalCheck(GwenX, 1200, TabM=4):
                                    $ Line = get_clothing_name(GwenX.Legs_key, vin)
                                    $ GwenX.Legs = 0
                                    "Она снимает [Line] и надевает [get_clothing_name(GwenX.Panties_key, vin)]."
                                elif GwenX.Legs == "skirt":
                                    "Она достает [get_clothing_name(GwenX.Panties_key, vin)] и надевает их под юбку."
                                    $ GwenX.Legs = 0
                                    "Затем она сбрасывает юбку на пол."
                                else:
                                    $ Line = GwenX.Legs
                                    $ GwenX.Legs = 0
                                    "Она на мгновение отходит, а затем возвращается в [get_clothing_name(GwenX.Panties_key, pre)]."
                                #return #jump Gwen_Clothes
                        else:
                                ch_g "Не-а."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(GwenX, 1100, "LI", TabM=3) and GwenX.Love > GwenX.Inbt:
                                ch_g "Ага. . ."
                        elif ApprovalCheck(GwenX, 700, "OI", TabM=3) and GwenX.Obed > GwenX.Inbt:
                                ch_g "Да. . ."
                        elif ApprovalCheck(GwenX, 600, "I", TabM=3):
                                ch_g "Хммм. . ."
                        elif ApprovalCheck(GwenX, 1300, TabM=3):
                                ch_g "Согласна."
                        else:
                                $ GwenX.FaceChange("surprised")
                                $ GwenX.Brows = "angry"
                                if GwenX.Taboo > 20:
                                    ch_g "Ага, но не на людях, [GwenX.Petname]!"
                                else:
                                    if not Player.Male:
                                        ch_g "Ты не настолько милая, [GwenX.Petname]!"
                                    else:
                                        ch_g "Ты не настолько милый, [GwenX.Petname]!"
                                call expression GwenX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно.":
                ch_g "Ладно. . ."
                return 0
        if GwenX.Panties and "pantyless" in GwenX.DailyActions:  #resets pantyless state if you had her put a pair on
                $ GwenX.DailyActions.remove("pantyless")
        return 1
        #End of Gwen Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Gwen_Clothes_Under:
        "Верх":
            menu:
                "Может, снимешь [get_clothing_name(GwenX.Chest_key, vin)]?" if GwenX.Chest:
                        $ GwenX.FaceChange("bemused", 1)
                        if GwenX.SeenChest and ApprovalCheck(GwenX, 900, TabM=2.7):
                            ch_g "Ладно."
                        elif ApprovalCheck(GwenX, 1100, TabM=2):
                            if GwenX.Taboo:
                                ch_g "Что-то мне не очень хочется делать это здесь. . ."
                            else:
                                ch_g "Может быть. . ."
#                        elif GwenX.Over == "jacket" and ApprovalCheck(GwenX, 600, TabM=2):
#                            ch_g "This jacket is a bit revealing. . ."
                        elif GwenX.Over and ApprovalCheck(GwenX, 500, TabM=2):
                            ch_g "Думаю, можно. . ."
                        elif not GwenX.Over:
                            call Display_DressScreen(GwenX)
                            if not _return:
                                ch_g "Нет, я не хочу светить грудью."
                                return #jump Gwen_Clothes
                        else:
                            call Display_DressScreen(GwenX)
                            if not _return:
                                ch_g "Не-а."
                                return #jump Gwen_Clothes
                        $ Line = get_clothing_name(GwenX.Chest_key, vin)
                        $ GwenX.Chest = 0
                        if GwenX.Over:
                            "Она залезает под [get_clothing_name(GwenX.Over_key, vin)], хватает и снимает [Line], а затем бросает на пол."
                        else:
                            "Она снимает [Line] и кидает на пол."
                            if not renpy.showing('DressScreen'):
                                call Girl_First_Topless(GwenX)


                "Надень белую майку" if GwenX.Chest != "tank":
                        ch_p "Примерь белую майку."
                        ch_g "Ладно."
                        $ GwenX.Chest = "tank"

                "Надень белый лифчик" if GwenX.Chest != "bra":
                        ch_p "Мне нравится твой белый лифчик."
                        if GwenX.SeenChest or ApprovalCheck(GwenX, 1100, TabM=2):
                            ch_g "Ладно."
                            $ GwenX.Chest = "bra"
                        else:
                            call Display_DressScreen(GwenX)
                            if not _return:
                                ch_g "Он немного откровенный. . ."
                            else:
                                $ GwenX.Chest = "bra"


                "Надень кружевной лифчик" if GwenX.Chest != "lace bra" and "lace bra" in GwenX.Inventory:
                        ch_p "Мне нравится твой кружевной лифчик."
                        if GwenX.SeenChest or ApprovalCheck(GwenX, 1300, TabM=2):
                            ch_g "Ладно."
                            $ GwenX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(GwenX)
                            if not _return:
                                ch_g "Он слегка прозрачный. . ."
                            else:
                                $ GwenX.Chest = "lace bra"

                "Надень лифчик бикини" if GwenX.Chest != "bikini top" and "bikini top" in GwenX.Inventory:
                        ch_p "Мне нравится твой лифчик бикини."
                        if bg_current == "bg pool":
                                ch_g "Ладно."
                                $ GwenX.Chest = "bikini top"
                        else:
                                if GwenX.SeenChest or ApprovalCheck(GwenX, 1000, TabM=2):
                                    ch_g "Ладно."
                                    $ GwenX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(GwenX)
                                    if not _return:
                                            ch_g "Тут не место для \"бикини\". . ."
                                    else:
                                            $ GwenX.Chest = "bikini top"
                "Неважно":
                        pass
            return #jump Gwen_Clothes_Under

        "Варианты колготок и чулок":
            menu:
                "Сними [get_clothing_name(GwenX.Hose_key, vin)]." if GwenX.Hose:
                                $ GwenX.FaceChange("sexy", 1)
                                if GwenX.SeenPanties and GwenX.Panties and ApprovalCheck(GwenX, 500, TabM=5):
                                    ch_g "Хорошо, конечно."
                                elif GwenX.SeenPussy and ApprovalCheck(GwenX, 900, TabM=4):
                                    ch_g "Ага, ладно."
                                elif ApprovalCheck(GwenX, 1300, TabM=2) and GwenX.Panties:
                                    ch_g "Хорошо, ради тебя. . ."
                                elif ApprovalCheck(GwenX, 700) and not GwenX.Panties:
                                    call Gwen_NoPantiesOn
                                    if not _return and not GwenX.Panties:
                                        if not ApprovalCheck(GwenX, 1500):
                                            call Display_DressScreen(GwenX)
                                            if not _return:
                                                return #jump Gwen_Clothes
                                        else:
                                                return #jump Gwen_Clothes
                                else:
                                    call Display_DressScreen(GwenX)
                                    if not _return:
                                        ch_g "Эм, не когда ты рядом."
                                        if not GwenX.Panties:
                                                ch_g "На мне нет трусиков. . ."
                                        return #jump Gwen_Clothes
                                $ GwenX.Hose = 0

                "Чулки дополнили бы твой образ." if GwenX.Hose != "stockings":
                                $ GwenX.Hose = "stockings"
                "Колготки дополнили бы твой образ." if GwenX.Hose != "pantyhose" and "pantyhose" in GwenX.Inventory:
                                $ GwenX.Hose = "pantyhose"
                "Рваные колготки дополнили бы твой образ." if GwenX.Hose != "ripped pantyhose" and "ripped pantyhose" in GwenX.Inventory:
                                $ GwenX.Hose = "ripped pantyhose"
                "Черные леггинсы дополнили бы твой образ." if GwenX.Hose != "tights":
                                $ GwenX.Hose = "tights"
                "Порванные леггинсы дополнили бы твой образ." if GwenX.Hose != "ripped tights" and "ripped tights" in GwenX.Inventory:
                                $ GwenX.Hose = "ripped tights"
                "Чулки и пояс с подвязками дополнили бы твой образ." if GwenX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in GwenX.Inventory:
                                $ GwenX.Hose = "stockings and garterbelt"
                "Может, наденешь только пояс с подвязками?" if GwenX.Hose != "garterbelt" and "stockings and garterbelt" in GwenX.Inventory:
                                $ GwenX.Hose = "garterbelt"
                "Высокие носки дополнили бы твой образ." if GwenX.Hose != "socks" and "halloween" in GwenX.History:
                                $ GwenX.Hose = "socks"
                "Неважно":
                        pass
            return #jump Gwen_Clothes_Under

        #Panties
        "Низ":
            menu:
                "Ты должна снять трусики. . ." if GwenX.Panties:
                        $ GwenX.FaceChange("bemused", 1)
                        if ApprovalCheck(GwenX, 900) and (GwenX.Legs or (GwenX.SeenPussy and not GwenX.Taboo)):
                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                                if ApprovalCheck(GwenX, 850, "L"):
                                        ch_g "Верно. . ."
                                elif ApprovalCheck(GwenX, 500, "O"):
                                        ch_g "Согласна."
                                elif ApprovalCheck(GwenX, 350, "I"):
                                        ch_g "Ха."
                                else:
                                        ch_g "Конечно, наверное."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(GwenX, 1100, "LI", TabM=3) and GwenX.Love > GwenX.Inbt:
                                        ch_g "Слушай, дело не в тебе, но. . ."
                                elif ApprovalCheck(GwenX, 700, "OI", TabM=3) and GwenX.Obed > GwenX.Inbt:
                                        ch_g "Хорошо. . ."
                                elif ApprovalCheck(GwenX, 600, "I", TabM=3):
                                        ch_g "Хммм. . ."
                                elif ApprovalCheck(GwenX, 1300, TabM=3):
                                        ch_g "Ладно-ладно."
                                else:
                                        call Display_DressScreen(GwenX)
                                        if not _return:
                                            $ GwenX.FaceChange("surprised")
                                            $ GwenX.Brows = "angry"
                                            if GwenX.Taboo > 20:
                                                ch_g "Не на людях."
                                            else:
                                                if not Player.Male:
                                                    ch_g "Ты не настолько милая, [GwenX.Petname]!"
                                                else:
                                                    ch_g "Ты не настолько милый, [GwenX.Petname]!"
                                            return #jump Gwen_Clothes
                        $ Line = get_clothing_name(GwenX.Panties_key, vin)
                        $ GwenX.Panties = 0
                        if not GwenX.Legs:
                            "Она снимает [Line], затем бросает их на пол."
                            if not renpy.showing('DressScreen'):
                                    call Gwen_First_Bottomless
                        elif ApprovalCheck(GwenX, 1200, TabM=4):
                            $ Trigger = GwenX.Legs
                            $ GwenX.Legs = 0
                            pause 0.5
                            $ GwenX.Legs = Trigger
                            "Она снимает [get_clothing_name(GwenX.Legs_key, vin)] и [Line], затем снова надевает [get_clothing_name(GwenX.Legs_key, vin)]."
                            $ Trigger = 1
                            call Girl_First_Bottomless(GwenX,1)
                        elif GwenX.Legs == "skirt":
                            "Она залезает под юбку и снимает [Line]."
                        else:
                            $ GwenX.Blush = 1
                            "Она на мгновение отходит, а затем возвращается."
                            $ GwenX.Blush = 0
                        $ Line = 0

                "Почему бы тебе вместо этих не надеть белые трусики?" if GwenX.Panties and GwenX.Panties != "white panties":
                        if ApprovalCheck(GwenX, 1100, TabM=3):
                                ch_g "Ладно."
                                $ GwenX.Panties = "white panties"
                        else:
                                call Display_DressScreen(GwenX)
                                if not _return:
                                        ch_g "Мои трусики - мой выбор."
                                else:
                                        $ GwenX.Panties = "white panties"

                "Почему бы тебе вместо этих не надеть кружевные трусики?" if "lace panties" in GwenX.Inventory and GwenX.Panties and GwenX.Panties != "lace panties":
                        if ApprovalCheck(GwenX, 1300, TabM=3):
                                ch_g "Ладно."
                                $ GwenX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(GwenX)
                                if not _return:
                                        ch_g "Мои трусики - мой выбор."
                                else:
                                        $ GwenX.Panties = "lace panties"

                "Мне нравятся твои трусики бикини." if "bikini bottoms" in GwenX.Inventory and GwenX.Panties != "bikini bottoms":
                        if bg_current == "bg pool":
                                ch_g "Ладно."
                                $ GwenX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(GwenX, 1000, TabM=2):
                                    ch_g "Ладно."
                                    $ GwenX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(GwenX)
                                    if not _return:
                                            ch_g "Тут не место для \"бикини\". . ."
                                    else:
                                            $ GwenX.Panties = "bikini bottoms"

                "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not GwenX.Panties:
                        $ GwenX.FaceChange("bemused", 1)
                        if GwenX.Legs and (GwenX.Love+GwenX.Obed) <= (2 * GwenX.Inbt):
                            $ GwenX.Mouth = "smile"
                            ch_g "Ну, я, может быть, я не хочу. . ."
                            menu:
                                "Ну ладно.":
                                    return #jump Gwen_Clothes
                                "Я настаиваю, надевай.":
                                    if (GwenX.Love+GwenX.Obed) <= (1.5 * GwenX.Inbt):
                                        $ GwenX.FaceChange("angry", Eyes="side")
                                        ch_g "Решать не тебе."
                                        return #jump Gwen_Clothes
                                    else:
                                        $ GwenX.FaceChange("sadside")
                                        ch_g "Ох, ладно."
                        else:
                            if not Player.Male:
                                ch_g "Пожалуй, ты права. . ."
                            else:
                                ch_g "Пожалуй, ты прав. . ."
                        menu:
                            extend ""
                            "Как насчет белых?":
                                    ch_g "Ладно, конечно."
                                    $ GwenX.Panties = "white panties"
                            "Как насчет трусиков бикини?" if "bikini bottoms" in GwenX.Inventory:
                                    ch_g "Конечно."
                                    $ GwenX.Panties  = "bikini bottoms"
                            "Как насчет кружевных?" if "lace panties" in GwenX.Inventory:
                                    ch_g "Ладно."
                                    $ GwenX.Panties  = "lace panties"
                "Неважно":
                    pass
            if GwenX.Panties and "pantyless" in GwenX.DailyActions:  #resets pantyless state if you had her put a pair on
                    $ GwenX.DailyActions.remove("pantyless")
            return #jump Gwen_Clothes_Under
        "Неважно":
            pass
    return #jump Gwen_Clothes
    #End of Gwen Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Gwen_Clothes_Misc:
        #Misc
        "Сухие волосы" if GwenX.Hair == "wet":
                ch_p "Тебе идут сухие волосы."
                if ApprovalCheck(GwenX, 600):
                    ch_g "Ладно."
                    $ GwenX.Hair = "short"
                else:
                    ch_g "Я не уверена, все и так хорошо."
        "Короткие волосы" if GwenX.Hair == "pony":
                ch_p "Думаю, тебе стоит сделать короткую стрижку."
                if ApprovalCheck(GwenX, 600):
                    ch_g "Ладно."
                    $ GwenX.Hair = "short"
                else:
                    ch_g "Я не уверена, все и так хорошо."

        "Влажные волосы" if GwenX.Hair != "wet":
                ch_p "Тебе стоит увлажнить волосы."
                if ApprovalCheck(GwenX, 800):
                    ch_g "Хмм?"
                    $ GwenX.Hair = "wet"
                    "Она отходит на минуту и вскоре возвращается."
                    ch_g "Типа так?"
                else:
                    ch_g "Это слишком сложно."

        "Два хвостика" if GwenX.Hair != "pony" and "halloween" in GwenX.History:
                ch_p "С двумя хвостиками ты выглядела очень мило."
                if ApprovalCheck(GwenX, 600):
                    ch_g "Ладно."
                    $ GwenX.Hair = "pony"
                else:
                    ch_g "Я не уверена, все и так хорошо."

        "Вкл\выкл Маску" if GwenX.Hat:
                if not GwenX.Hat:
                        ch_p "Почему бы тебе не надеть маску?"
                else:
                        ch_p "Давай снимем маску."
                ch_g "Ладно."
                $ GwenX.Hat = 0 if GwenX.Hat else "hat"
                menu:
                    ch_g "Как думаешь, мне стоит носить маску с костюмом?"
                    "Не носи маску":
                            ch_g "Ладно."
                            $ GwenX.Casual1[12] = 0
                    "Носи маску":
                            ch_g "Ладно."
                            $ GwenX.Casual1[12] = "mask"

        "Отрасти волосы на лобке" if not GwenX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может, отрастишь?"
                call expression GwenX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in GwenX.Todo:
                        $ GwenX.FaceChange("bemused", 1)
                        ch_g "Как быстро по-твоему они растут?"
                else:
                    $ GwenX.FaceChange("bemused", 1)
                    if ApprovalCheck(GwenX, 1000, TabM=0):
                            ch_g "Ладно. . ."
                    else:
                            $ GwenX.FaceChange("surprised")
                            $ GwenX.Brows = "angry"
                            ch_g ". . . Почему ты просишь меня об этом?"
                            return #jump Gwen_Clothes
                    $ GwenX.Todo.append("pubes")
                    $ GwenX.PubeC = 6
        "Побрей лобок" if GwenX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression GwenX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ GwenX.FaceChange("bemused", 1)
                if "shave" in GwenX.Todo:
                        ch_g "Попозже я займусь этим."
                else:
                    if ApprovalCheck(GwenX, 1100, TabM=0):
                        ch_g "Правда? Я даже не знаю, наверное, это можно устроить. . ."
                    else:
                        $ GwenX.FaceChange("surprised")
                        $ GwenX.Brows = "angry"
                        ch_g ". . . Почему ты просишь меня об этом?"
                        return #jump Gwen_Clothes
                    $ GwenX.Todo.append("shave")

        "Пирсинг. [[Сначала посмотрите, как она выглядит без него] (locked)" if not GwenX.SeenPussy and not GwenX.SeenChest:
            pass

        "Надень пирсинг-кольца" if GwenX.Pierce != "ring" and (GwenX.SeenPussy or GwenX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсингом-кольцами."
                if "ring" in GwenX.Todo:
                    ch_g "Ага, я в деле."
                else:
                    $ GwenX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(GwenX, 1150, TabM=0)
                    if ApprovalCheck(GwenX, 900, "L", TabM=0) or (Approval and GwenX.Love > 2* GwenX.Obed):
                        ch_g "Ты думаешь он правда мне подойдет?"
                    elif ApprovalCheck(GwenX, 600, "I", TabM=0) or (Approval and GwenX.Inbt > GwenX.Obed):
                        ch_g "Я уже давненько думаю об этом."
                    elif ApprovalCheck(GwenX, 500, "O", TabM=0) or Approval:
                        ch_g "Ладно, [GwenX.Petname]."
                    else:
                        $ GwenX.FaceChange("surprised")
                        $ GwenX.Brows = "angry"
                        ch_g "Мне это совсем не интересно, [GwenX.Petname]."
                        return #jump Gwen_Clothes
                    $ GwenX.Todo.append("ring")

        "Надень пирсинг-штанги" if GwenX.Pierce != "barbell" and (GwenX.SeenPussy or GwenX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in GwenX.Todo:
                    ch_g "Ага, я в деле."
                else:
                    $ GwenX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(GwenX, 1150, TabM=0)
                    if ApprovalCheck(GwenX, 900, "L", TabM=0) or (Approval and GwenX.Love > 2 * GwenX.Obed):
                        ch_g "Ты думаешь, он правда мне подойдет?"
                    elif ApprovalCheck(GwenX, 600, "I", TabM=0) or (Approval and GwenX.Inbt > GwenX.Obed):
                        ch_g "Я уже давненько думаю об этом."
                    elif ApprovalCheck(GwenX, 500, "O", TabM=0) or Approval:
                        ch_g "Ладно, [GwenX.Petname]."
                    else:
                        $ GwenX.FaceChange("surprised")
                        $ GwenX.Brows = "angry"
                        ch_g "Мне это совсем не интересно, [GwenX.Petname]."
                        return #jump Gwen_Clothes
                    $ GwenX.Todo.append("barbell")

        "Сними пирсинг" if GwenX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ GwenX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(GwenX, 1350, TabM=0)
                if ApprovalCheck(GwenX, 950, "L", TabM=0) or (Approval and GwenX.Love > GwenX.Obed):
                    ch_g "Определись уже. . ."
                elif ApprovalCheck(GwenX, 700, "I", TabM=0) or (Approval and GwenX.Inbt > GwenX.Obed):
                    ch_g "Все будет."
                elif ApprovalCheck(GwenX, 600, "O", TabM=0) or Approval:
                    ch_g "Хорошо."
                else:
                    $ GwenX.FaceChange("surprised")
                    $ GwenX.Brows = "angry"
                    ch_g "Мне он очень нравится. . ."
                    return #jump Gwen_Clothes
                $ GwenX.Pierce = 0

#        "Medallion choker" if GwenX.Neck != "leash choker":
#                ch_p "Why don't you try on that medallion choker?"
#                ch_g "Ok. . ."
#                $ GwenX.Neck = "leash choker"
#        "Remove Necklace" if GwenX.Neck:
#                ch_p "Maybe go without a necklace."
#                ch_g "Ok. . ."
#                $ GwenX.Neck = 0

#        "Add Suspenders" if GwenX.Acc != "suspenders" and GwenX.Acc != "suspenders2" and "halloween" in GwenX.History:
#                $ GwenX.Acc = "suspenders"
#        "Remove Suspenders" if GwenX.Acc == "suspenders" or GwenX.Acc == "suspenders2":
#                $ GwenX.Acc = 0

#        "Shift Suspenders" if GwenX.Acc == "suspenders" or GwenX.Acc == "suspenders2":
#                $ GwenX.Acc = "suspenders" if GwenX.Acc == "suspenders2" else "suspenders2"

        "Вкл\Выкл Перчатки" if GwenX.Over == "suit":
                if not GwenX.Arms:
                        ch_p "Почему бы тебе не надеть перчатки обратно?"
                else:
                        ch_p "Давай обойдемся без перчаток."
                ch_g "Ладно."
                $ GwenX.Arms = 0 if GwenX.Arms else "gloves"

        "Неважно":
            pass
    return #jump Gwen_Clothes
    #End of Gwen Misc Wardrobe

return
#End Gwen Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
