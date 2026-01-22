# star Emma chat interface

label Emma_Chat_Minimal:
    $ EmmaX.FaceChange()
    call Shift_Focus(EmmaX)
    if EmmaX.Loc != bg_current:
                show Cellphone at SpriteLoc(EmmaX.SpriteLoc)
    else:
                hide Cellphone
    if "caught" in EmmaX.RecentActions:
                ch_e "Я думаю, нас не должны видеть вместе."
                return
    if "angry" in EmmaX.RecentActions:
                ch_e "Осторожней, не искушай судьбу."
                return

    if Girl == EmmaX and "noise" in Player.History:
            #asks her about noise in the attic, launching Storm meet
            call StormMeetAsk
    menu:
        ch_e "Что ты хочешь обсудить, [EmmaX.Petname]?"
        "Приходи ко мне." if EmmaX.Loc != bg_current:
                    ch_e "Не думаю, что я должна навещать студентов по их прихоти."
                    ch_e "Мои рабочии часы ты знаешь."
        "Попросить [EmmaX.Name_vin] уйти" if EmmaX.Loc == bg_current:
                    ch_e "I'll come and go as I see fit, thank you."
        "Ухаживать":
                menu:
                    "Флиртовать (locked)" if EmmaX.Chat[5]:
                                pass
                    "Флиртовать" if not EmmaX.Chat[5]:
                                call Emma_Flirt_Minimal
                    "Секс меню" if EmmaX.Loc == bg_current:
                                ch_p "Хочешь пошалить?"
                                if not Player.Male:
                                    ch_e "Со своей студенткой? Полагаю, тебе хорошо известен мой ответ, [EmmaX.Petname]."
                                else:
                                    ch_e "Со своим студентом? Полагаю, тебе хорошо известен мой ответ, [EmmaX.Petname]."
                    "Грязный разговор (locked)" if True:
                                    pass
                    "Свидание":
                                ch_p "Хочешь сходить на свидание сегодня вечером?"
                                ch_e "Твое предложение неуместно."
                    "Подарок" if EmmaX.Loc == bg_current:
                                if not Player.Male:
                                    ch_p "Я бы хотела тебе кое-что подарить."
                                else:
                                    ch_p "Я бы хотел тебе кое-что подарить."
                                ch_e "Я не уверена, что сейчас подходящий момент."
                    "Назад":
                                pass
        "Поговорить":
                menu:
                    "Я просто хочу поболтать. . .":
                                call Emma_Chitchat
                    "Об отношениях":
                                ch_p "Мы можем поговорить о нас?"
                                ch_e "Не уверена, что сейчас подходящий момент для этого разговора."
                    "Могу я узнать твой номер телефона?" if EmmaX not in Digits:
                                if ApprovalCheck(EmmaX, 800, "LI"):
                                    ch_e "Не вижу причин отказать."
                                    $ Digits.append(EmmaX)
                                elif ApprovalCheck(EmmaX, 500, "OI"):
                                    ch_e "Хмм. . . хорошо, дай мне свой телефон."
                                    $ Digits.append(EmmaX)
                                else:
                                    ch_e "Не думаю, что студентам стоит знать мой номер."
                    "Назад":
                                pass
        "Изменить что-нибудь в [EmmaX.Name_pre]":
                    ch_p "Давай поговорим о тебе."
                    ch_e "Сомневаюсь, что тебя это касается."
        "Собрать группу" if EmmaX not in Party and EmmaX.Loc == bg_current:
                    ch_p "Не могла бы ты пойти со мной?"
                    ch_e "Не думаю, что мне следует это делать."
        "Распустить группу" if EmmaX in Party:
                    ch_p "Ладно, если хочешь, можешь идти."
                    $ Party.remove(EmmaX)
        "Неважно.":
                    if Time_Count == 2: #evening time
                            ch_e "Если это все, пожалуйста, уходи."
                            $ EmmaX.FaceChange("bemused",2)
                            ch_e "У меня остались еще. . . кое-какие дела."
                    else:
                            "Она ведет себя холодо с вами. Возможно, вам нужно что-то сделать, чтобы растопить лед."
                            "Возможно, вам стоит навестить ее в аудитории после занятий, когда студенты уйдут."
                    return
    jump Emma_Chat_Minimal

label Emma_Flirt_Minimal:
        menu:
            "Сделать комплимент":
                        call Compliment(Girl)
            "Прищнаться в любви":
                        if EmmaX.Love >= 500:
                                $ EmmaX.Statup("Love", 90, 2)
                        $ EmmaX.Statup("Obed", 40, 1)
                        ch_e "Не шути так, [EmmaX.Petname]."
            "Коснуться ее щеки":
                        "Вы начинаете приближаться к ней, но она отталкивает вас твердой рукой."
                        ch_e "Не подходи ко мне слишком близко, [EmmaX.Petname]."
            "Взять ее за руки":
                        "Вы начинаете приближаться к ней, но она отталкивает вас твердой рукой."
                        ch_e "Не подходи ко мне слишком близко, [EmmaX.Petname]."
            "Погладить ее по голове":
                        "Вы начинаете приближаться к ней, но она отталкивает вас твердой рукой."
                        ch_e "Не подходи ко мне слишком близко, [EmmaX.Petname]."
            "Поцеловать ее в щечку":
                        "Вы начинаете приближаться к ней, но она отталкивает вас твердой рукой."
                        ch_e "Не подходи ко мне слишком близко, [EmmaX.Petname]."
            "Обнять":
                        "Вы начинаете приближаться к ней, но она отталкивает вас твердой рукой."
                        ch_e "Не подходи ко мне слишком близко, [EmmaX.Petname]."
            "Шлепнуть ее по заднице":
                        "Вы начинаете приближаться к ней, но она отталкивает вас твердой рукой."
                        ch_e "Не подходи ко мне слишком близко, [EmmaX.Petname]."
            "Ущипнуть ее за задницу":
                        "Вы начинаете приближаться к ней, но она отталкивает вас твердой рукой."
                        ch_e "Не подходи ко мне слишком близко, [EmmaX.Petname]."
            "Схватить ее за грудь":
                        "Вы начинаете приближаться к ней, но она отталкивает вас твердой рукой."
                        ch_e "Не подходи ко мне слишком близко, [EmmaX.Petname]."
            "Потереть ее плечи":
                        "Вы начинаете приближаться к ней, но она отталкивает вас твердой рукой."
                        ch_e "Не подходи ко мне слишком близко, [EmmaX.Petname]."
            "Неважно":
                return
        $ EmmaX.Chat[5] = 1
        return
#Emma Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Emma_Relationship: #rkelj
    while True:
        menu:
            ch_e "О чем ты желаешь поговорить?"
            "Хочешь стать моей девушкой?" if EmmaX not in Player.Harem and "ex" not in EmmaX.Traits:
                    $ EmmaX.DailyActions.append("relationship")
                    if "asked boyfriend" in EmmaX.DailyActions and "angry" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("angry", 1)
                            if not Player.Male:
                                ch_e "Какая ты надоедливая."
                            else:
                                ch_e "Какой ты надоедливый."
                            return
                    elif "asked boyfriend" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Не сегодня, а теперь исчезни."
                            return
                    elif EmmaX.Break[0]:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Я не желаю ни с кем делиться."
                            if Player.Harem:
                                    $ EmmaX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "Я уже ни с кем не встречаюсь."

                    $ EmmaX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "EmmaYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_e "Я сомневаюсь, что они поймут, [EmmaX.Petname]."
                        else:
                            ch_e "Я сомневаюсь, что [Player.Harem[0].Name] поймет, [EmmaX.Petname]."
                        return

                    if EmmaX.Event[5]:
                            $ EmmaX.FaceChange("bemused", 1)
                            ch_e "Кажется, я уже когда-то тебя спрашивала, ты помнишь свой ответ?"
                    else:
                            $ EmmaX.FaceChange("surprised", 2)
                            ch_e "Мне кажется, это не уместно, [EmmaX.Petname]. . ."
                            $ EmmaX.FaceChange("smile", 1)

                    call Emma_OtherWoman

                    if EmmaX.Love >= 800:
                            $ EmmaX.FaceChange("surprised", 1)
                            $ EmmaX.Mouth = "smile"
                            if not EmmaX.Event[5]:
                                    $ EmmaX.Statup("Love", 200, 10)
                                    call Emma_BF
                                    return
                            $ EmmaX.Statup("Love", 200, 40)
                            ch_e "Полагаю, я уже привыкла к тебе. . ."
                            if "boyfriend" not in EmmaX.Petnames:
                                    $ EmmaX.Petnames.append("boyfriend")
                            if "EmmaYes" in Player.Traits:
                                    $ Player.Traits.remove("EmmaYes")
                            $ Player.Harem.append(EmmaX)
                            call Harem_Initiation
                            "[EmmaX.Name] прижимается к вам и страстно целует."
                            $ EmmaX.FaceChange("kiss", 1)
                            $ EmmaX.Kissed += 1
                    elif EmmaX.Obed >= 500:
                            $ EmmaX.FaceChange("perplexed")
                            ch_e "Мы не можем \"встречаться\" при текущих наших отношениях."
                    elif EmmaX.Inbt >= 500:
                            $ EmmaX.FaceChange("smile")
                            ch_e "Не думаю, что мы должны довольствоваться лишь друг другом."
                    else:
                            $ EmmaX.FaceChange("perplexed", 1)
                            ch_e "По правде говоря, я не могу серьезно относиться к студентам, [EmmaX.Petname]."

            "Может, начнем все сначала?" if "ex" in EmmaX.Traits:
                    $ EmmaX.DailyActions.append("relationship")
                    if "asked boyfriend" in EmmaX.DailyActions and "angry" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Стоит ли мне объяснять, насколько это маловероятно?"
                            return
                    elif "asked boyfriend" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Сейчас ты ставишь себя в неловкое положение."
                            return

                    $ EmmaX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "EmmaYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_e "Я сомневаюсь, что они поймут, [EmmaX.Petname]."
                            else:
                                ch_e "Я сомневаюсь, что [Player.Harem[0].Name] поймет, [EmmaX.Petname]."
                            return

                    $ Cnt = 0
                    call Emma_OtherWoman

                    if EmmaX.Love >= 800:
                            $ EmmaX.FaceChange("sly", 1)
                            $ EmmaX.Statup("Love", 90, 5)
                            ch_e "Даже при всем желании, я не могу злиться на тебя."
                            if "boyfriend" not in EmmaX.Petnames:
                                    $ EmmaX.Petnames.append("boyfriend")
                            $ EmmaX.Traits.remove("ex")
                            if "EmmaYes" in Player.Traits:
                                    $ Player.Traits.remove("EmmaYes")
                            $ Player.Harem.append(EmmaX)
                            call Harem_Initiation
                            "[EmmaX.Name] наклоняется и страстно целует вас."
                            $ EmmaX.FaceChange("kiss", 1)
                            $ EmmaX.Kissed += 1
                    elif EmmaX.Love >= 600 and ApprovalCheck(EmmaX, 1500):
                            $ EmmaX.FaceChange("smile", 1)
                            $ EmmaX.Statup("Love", 90, 5)
                            ch_e "Хм, ну хорошо."
                            if "boyfriend" not in EmmaX.Petnames:
                                    $ EmmaX.Petnames.append("boyfriend")
                            $ EmmaX.Traits.remove("ex")
                            if "EmmaYes" in Player.Traits:
                                    $ Player.Traits.remove("EmmaYes")
                            $ Player.Harem.append(EmmaX)
                            call Harem_Initiation
                            $ EmmaX.FaceChange("kiss", 1)
                            "[EmmaX.Name] дарит вам легкий поцелуй."
                            $ EmmaX.FaceChange("sly", 1)
                            $ EmmaX.Kissed += 1
                    elif EmmaX.Obed >= 500:
                            $ EmmaX.FaceChange("sad")
                            ch_e "Давай пока сохраним все как есть."
                    elif EmmaX.Inbt >= 500:
                            $ EmmaX.FaceChange("perplexed")
                            ch_e "Нет, \"не постоянные\" отношения мне нравятся больше."
                    else:
                            $ EmmaX.FaceChange("perplexed", 1)
                            ch_e "Я не признаю никаких \"вторых шансов\"."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if EmmaX in Player.Harem:
                            call AskDateOther

            "Думаю, мы должны расстаться." if EmmaX in Player.Harem:
                        if "breakup talk" in EmmaX.DailyActions:
                                ch_e "Да ты, наверное, шутишь. Снова?"
                        else:
                                call Breakup(EmmaX)

            "О разговоре, который у нас был ранее. . .":
                menu:
                    "Помнишь, ты признавалась мне в любви. . ?" if "lover" not in EmmaX.Traits and EmmaX.Event[6] >= 20:
                            call Emma_Love_Redux
                    "Помнишь, ты говорила, что хочешь, чтобы я была более властной?" if "sir" not in EmmaX.Petnames and "sir" in EmmaX.History and not Player.Male:
                            if "asked sub" in EmmaX.DailyActions:
                                    if not Player.Male:
                                        ch_e "Говорила, но ты не согласилась."
                                    else:
                                        ch_e "Говорила, но ты не согласился."
                            else:
                                    call Emma_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я был более властным?" if "sir" not in EmmaX.Petnames and "sir" in EmmaX.History and Player.Male:
                            if "asked sub" in EmmaX.DailyActions:
                                    if not Player.Male:
                                        ch_e "Говорила, но ты не согласилась."
                                    else:
                                        ch_e "Говорила, но ты не согласился."
                            else:
                                    call Emma_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоей хозяйкой?" if "master" not in EmmaX.Petnames and "master" in EmmaX.History not Player.Male:
                            if "asked sub" in EmmaX.DailyActions:
                                    ch_e "Кажется, я что-то такое припоминаю. . ."
                            else:
                                    call Emma_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я стал твоим хозяином?" if "master" not in EmmaX.Petnames and "master" in EmmaX.History not Player.Male:
                            if "asked sub" in EmmaX.DailyActions:
                                    ch_e "Кажется, я что-то такое припоминаю. . ."
                            else:
                                    call Emma_Sub_Asked
                    "Неважно":
                            pass
            "Неважно":
                return

    return

label Emma_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((EmmaX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ EmmaX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_e "Но ты же сейчас с [Player.Harem[0].Name_tvo], если не считать других."
    else:
        ch_e "Но ты же сейчас с [Player.Harem[0].Name_tvo]."
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "EmmaYes" in Player.Traits:
                if ApprovalCheck(EmmaX, 1800, Bonus = Cnt):
                    $ EmmaX.FaceChange("smile", 1)
                    if EmmaX.Love >= EmmaX.Obed:
                            ch_e "Полагаю, ты того стоишь, я готова разделить тебя с другими."
                    elif EmmaX.Obed >= EmmaX.Inbt:
                            ch_e "Если она готова делить тебя с другими, то и я тоже."
                    else:
                            ch_e "Конечно, почему нет."
                else:
                    $ EmmaX.FaceChange("angry", 1)
                    ch_e "Мне абсолютно все равно, что сказала эта маленькая потаскушка."
                    $ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "EmmaYes" not in Player.Traits  not Player.Male:
                if ApprovalCheck(EmmaX, 1800, Bonus = Cnt):
                        $ EmmaX.FaceChange("smile", 1)
                        if EmmaX.Love >= EmmaX.Obed:
                            ch_e "Полагаю, ты того стоишь, я готова разделить тебя с другими."
                        elif EmmaX.Obed >= EmmaX.Inbt:
                            ch_e "Если она будет готова разделить тебя с другими, то и я тоже."
                        else:
                            ch_e "Конечно, почему нет."
                        ch_e "Пока спроси ее, а я подумаю. Завтра возвращайся с ее ответом."
                else:
                        $ EmmaX.FaceChange("angry", 1)
                        ch_e "Мне абсолютно все равно, что скажет эта маленькая потаскушка."
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "EmmaYes" not in Player.Traits  Player.Male:
                if ApprovalCheck(EmmaX, 1800, Bonus = Cnt):
                        $ EmmaX.FaceChange("smile", 1)
                        if EmmaX.Love >= EmmaX.Obed:
                            ch_e "Полагаю, ты того стоишь, я готова разделить тебя с другими."
                        elif EmmaX.Obed >= EmmaX.Inbt:
                            ch_e "Если она будет готова разделить тебя с другими, то и я тоже."
                        else:
                            ch_e "Конечно, почему нет."
                        ch_e "Пока спроси ее, а я подумаю. Завтра возвращайся с ее ответом."
                else:
                        $ EmmaX.FaceChange("angry", 1)
                        ch_e "Мне абсолютно все равно, что скажет эта маленькая потаскушка."
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
                if not ApprovalCheck(EmmaX, 1800, Bonus = -Cnt): #checks if Emma likes you more than Rogue
                        $ EmmaX.FaceChange("angry", 1)
                        if not ApprovalCheck(EmmaX, 1800):
                                ch_e "Я не хочу этого."
                        else:
                                ch_e "Я не хочу делить тебя ни с кем."
                        $ renpy.pop_call()
                else:
                        $ EmmaX.FaceChange("smile", 1)
                        if EmmaX.Love >= EmmaX.Obed:
                                ch_e "Полагаю, мы могли бы что-нибудь придумать."
                        elif EmmaX.Obed >= EmmaX.Inbt:
                                ch_e "Если ты настаиваешь."
                        else:
                                ch_e "Не вижу причин отказываться."
                        $ EmmaX.Traits.append("downlow")

        "Я могу порвать с ней.":
                    $ EmmaX.FaceChange("sad")
                    ch_e "Давай, после поговорим."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ EmmaX.FaceChange("sad")
                    ch_e "Разумеется. . ."
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ EmmaX.FaceChange("sad")
                    ch_e "Разумеется. . ."
                    $ renpy.pop_call()
    return


label Emma_About(Check=0): #rkeljsvg
    if Check not in TotalGirls:
            ch_e "Это вообще кто?"
            return
    ch_e "Что я о ней думаю? Что ж. . ."
    if Check == RogueX:
            if "poly Rogue" in EmmaX.Traits:
                ch_e "Как ты, наверное, знаешь, у нас много общего. . ."
            elif EmmaX.LikeRogue >= 900:
                ch_e "Я нахожу ее довольно завораживающей. . ."
            elif EmmaX.LikeRogue >= 800:
                ch_e "Я имею влияние на нее. . ."
            elif EmmaX.LikeRogue >= 700:
                ch_e "Мы стали довольно близки."
            elif EmmaX.LikeRogue >= 600:
                ch_e "Она мне очень нравится."
            elif EmmaX.LikeRogue >= 500:
                ch_e "Она достойная студентка."
            elif EmmaX.LikeRogue >= 400:
                ch_e "С ней бывают проблемы."
            elif EmmaX.LikeRogue >= 300:
                ch_e "Я едва терплю ее неуважительный характер."
            else:
                ch_e "Что я вообще должна думать об этой болотной крысе?"
    elif Check == KittyX:
            if "poly Kitty" in EmmaX.Traits:
                ch_e "Как ты знаешь, мы хорошо ладим. . ."
            elif EmmaX.LikeKitty >= 900:
                ch_e "Она довольно. . . своевольная. . ."
            elif EmmaX.LikeKitty >= 800:
                ch_e "Она довольно очаровательна. . ."
            elif EmmaX.LikeKitty >= 700:
                ch_e "Она мне кто-то вроде подруги."
            elif EmmaX.LikeKitty >= 600:
                ch_e "Как только я узнала ее получше, она не так уж и плоха."
            elif EmmaX.LikeKitty >= 500:
                ch_e "Она достойная студентка."
            elif EmmaX.LikeKitty >= 400:
                ch_e "Она немного зазнайка."
            elif EmmaX.LikeKitty >= 300:
                ch_e "Я терпеть не могу ее постоянных вопросов."
            else:
                if not Player.Male:
                    ch_e "Ты уверена, что хочешь знать, что я думаю об этой маленькой сучке?"
                else:
                    ch_e "Ты уверен, что хочешь знать, что я думаю об этой маленькой сучке?"
    elif Check == LauraX:
            if "poly Laura" in EmmaX.Traits:
                ch_e "Она очень даже. . . энергичная. . ."
            elif EmmaX.LikeLaura >= 900:
                ch_e "Она очень стойкая. . ."
            elif EmmaX.LikeLaura >= 800:
                ch_e "В ней есть некая грубость, меня это возбуждает. . ."
            elif EmmaX.LikeLaura >= 700:
                ch_e "Она мне кто-то вроде подруги."
            elif EmmaX.LikeLaura >= 600:
                ch_e "Как только я узнала ее получше, она не так уж и плоха."
            elif EmmaX.LikeLaura >= 500:
                ch_e "Она достойная студентка."
            elif EmmaX.LikeLaura >= 400:
                ch_e "Она слегка грубовата."
            elif EmmaX.LikeLaura >= 300:
                ch_e "Она дикая."
            else:
                ch_e "Будь моя воля, я бы ее поставила на место."
    elif Check == JeanX:
            if "poly Jean" in EmmaX.Traits:
                ch_e "Как ты, наверное, знаешь, у нас много общего. . ."
            elif EmmaX.LikeJean >= 900:
                ch_e "Я нахожу ее довольно завораживающей. . ."
            elif EmmaX.LikeJean >= 800:
                ch_e "Если дать ей возможность, она показывает себя с прекрасной стороны. . ."
            elif EmmaX.LikeJean >= 700:
                ch_e "Мне нравятся такие как она. . ."
            elif EmmaX.LikeJean >= 600:
                ch_e "Она мне очень нравится."
            elif EmmaX.LikeJean >= 500:
                ch_e "Она достойная студентка."
            elif EmmaX.LikeJean >= 400:
                ch_e "Она немного странная."
            elif EmmaX.LikeJean >= 300:
                ch_e "Я едва терплю ее высокомерие."
            else:
                ch_e "Что я вообще могу думать об этой суке?"
    elif Check == StormX:
            if "poly Storm" in EmmaX.Traits:
                ch_e "Она удивительно опытна. . ."
            elif EmmaX.LikeStorm >= 900:
                ch_e "Она хорошо дополняет меня. . ."
            elif EmmaX.LikeStorm >= 800:
                ch_e "У нее прекрасная фигура. . ."
            elif EmmaX.LikeStorm >= 700:
                ch_e "Она в некотором роде моя подруга."
            elif EmmaX.LikeStorm >= 600:
                ch_e "Она отличная коллега."
            elif EmmaX.LikeStorm >= 500:
                ch_e "Она достойная коллега."
            elif EmmaX.LikeStorm >= 400:
                ch_e "Она слегка грубовата"
            elif EmmaX.LikeStorm >= 300:
                if not Player.Male:
                    ch_e "У нее волосы на лобке и голове одинакового цвета. Но ты это и сама, конечно, знаешь."
                else:
                    ch_e "У нее волосы на лобке и голове одинакового цвета. Но ты это и сам, конечно, знаешь."
            else:
                ch_e "Хотела бы я убедить Чарльза уволить ее."
    elif Check == JubesX:
            if "poly Jubes" in EmmaX.Traits:
                ch_e "Как ты знаешь, мы хорошо ладим. . ."
            elif EmmaX.LikeJubes >= 900:
                ch_e "Она довольно. . . своевольная. . ."
            elif EmmaX.LikeJubes >= 800:
                ch_e "Она очень милая. . ."
            elif EmmaX.LikeJubes >= 700:
                ch_e "Она мне кто-то вроде подруги."
            elif EmmaX.LikeJubes >= 600:
                ch_e "Как только я узнала ее получше, она не так уж и плоха."
            elif EmmaX.LikeJubes >= 500:
                ch_e "Она достойная студентка."
            elif EmmaX.LikeJubes >= 400:
                ch_e "У нее острые зубки"
            elif EmmaX.LikeJubes >= 300:
                ch_e "От нее много проблем."
            else:
                if not Player.Male:
                    ch_e "Ты уверена, что хочешь знать, что я думаю об этой маленькой сучке?"
                else:
                    ch_e "Ты уверен, что хочешь знать, что я думаю об этой маленькой сучке?"
    elif Check == GwenX:
            if "poly Gwen" in EmmaX.Traits:
                ch_e "Как ты знаешь, мы довольно хорошо ладим. . ."
            elif EmmaX.LikeGwen >= 900:
                ch_e "Она очень даже. . . активная. . ."
            elif EmmaX.LikeGwen >= 800:
                ch_e "Она довольно очаровательна. . ."
            elif EmmaX.LikeGwen >= 700:
                ch_e "Мне нравится ее внимательность."
            elif EmmaX.LikeGwen >= 600:
                ch_e "Как только я узнала ее получше, она не так уж и плоха."
            elif EmmaX.LikeGwen >= 500:
                ch_e "У нее неплохой вкус."
            elif EmmaX.LikeGwen >= 400:
                ch_e "Она бывает немного. . . агрессивной."
            elif EmmaX.LikeGwen >= 300:
                ch_e "Терпеть не могу ее постоянные приставания."
            else:
                if not Player.Male:
                    ch_e "Ты уверена, что хочешь знать, что я думаю об этой маленькой сучке?"
                else:
                    ch_e "Ты уверен, что хочешь знать, что я думаю об этой маленькой сучке?"
    elif Check == BetsyX:
            if "poly Betsy" in EmmaX.Traits:
                ch_e "Как ты знаешь, мы довольно хорошо ладим. . ."
            elif EmmaX.LikeBetsy >= 900:
                ch_e "Она владеет несколькими очень интересными техниками. . ."
            elif EmmaX.LikeBetsy >= 800:
                ch_e "Она довольно элегантна. . ."
            elif EmmaX.LikeBetsy >= 700:
                ch_e "Она мне кто-то вроде подруги."
            elif EmmaX.LikeBetsy >= 600:
                ch_e "Как только узнаешь ее поближе, понимаешь, что она не так уж и плоха."
            elif EmmaX.LikeBetsy >= 500:
                ch_e "Она прилежная студентка."
            elif EmmaX.LikeBetsy >= 400:
                ch_e "Она может быть довольно заносчивой."
            elif EmmaX.LikeBetsy >= 300:
                ch_e "Я не думаю, что ей место у нас в институте."
            else:
                if not Player.Male:
                    ch_e "Ты уверена, что хочешь знать, что я думаю об этой маленькой сучке?"
                else:
                    ch_e "Ты уверен, что хочешь знать, что я думаю об этой маленькой сучке?"
    elif Check == DoreenX:
            if "poly Doreen" in EmmaX.Traits:
                ch_e "Как ты знаешь, мы довольно хорошо ладим. . ."
            elif EmmaX.LikeDoreen >= 900:
                ch_e "Она. . . полна энтузиазма. . ."
            elif EmmaX.LikeDoreen >= 800:
                ch_e "Она довольно очаровательна. . ."
            elif EmmaX.LikeDoreen >= 700:
                ch_e "Мне стало нравиться ее внимание."
            elif EmmaX.LikeDoreen >= 600:
                ch_e "Как только узнаешь ее поближе, понимаешь, что она не так уж и плоха."
            elif EmmaX.LikeDoreen >= 500:
                ch_e "Она на любителя."
            elif EmmaX.LikeDoreen >= 400:
                ch_e "Она может быть немного. . . агрессивной."
            elif EmmaX.LikeDoreen >= 300:
                ch_e "Я терпеть не могу ее постоянных приставаний."
            else:
                if not Player.Male:
                    ch_e "Ты уверена, что хочешь знать, что я думаю об этой маленькой сучке?"
                else:
                    ch_e "Ты уверен, что хочешь знать, что я думаю об этой маленькой сучке?"
    elif Check == WandaX:
            if "poly Wanda" in EmmaX.Traits:
                ch_e "Как ты знаешь, у нас много общего. . ."
            elif EmmaX.LikeWanda >= 900:
                ch_e "Я нахожу ее довольно привлекательной. . ."
            elif EmmaX.LikeWanda >= 800:
                ch_e "Ее энтузиазм, безусловно, пришелся мне по душе. . ."
            elif EmmaX.LikeWanda >= 700:
                ch_e "Мы с ней очень сблизились."
            elif EmmaX.LikeWanda >= 600:
                ch_e "Она мне очень нравится."
            elif EmmaX.LikeWanda >= 500:
                ch_e "Она адекватная студентка."
            elif EmmaX.LikeWanda >= 400:
                ch_e "Она может быть не в меру вспыльчивой."
            elif EmmaX.LikeWanda >= 300:
                ch_e "Я с трудом выношу ее трудный характер."
            else:
                ch_e "Ты про ту хулиганку? Что с ней?"
    else:
                ch_e "Я не хочу разговаривать о ней."
    return
#End Emma_AboutRogue

label Emma_Monogamy:
        #called from Emma_Settings to ask her not to hook up with other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in EmmaX.Traits:
                    if EmmaX.Thirst >= 50 and not ApprovalCheck(EmmaX, 1800, "LO", TabM=0):
                            #she's too thirsty
                            $ EmmaX.FaceChange("sly",1)
                            if "mono" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Obed", 90, -2)
                            ch_e "Знаешь, ты же не оставляешь мне иного выбора. . ."
                            return
                    elif ApprovalCheck(EmmaX, 1300, "LO", TabM=0) and EmmaX.Love >= EmmaX.Obed:
                            #she cares
                            $ EmmaX.FaceChange("sly",1)
                            if "mono" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Love", 90, 1)
                            ch_e "Ревность тебе очень к лицу. . ."
                            ch_e "Полагаю, я смогу удержаться от соблазна. . ."
                    elif ApprovalCheck(EmmaX, 750, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side")
                            ch_e "Если ты настаиваешь. . ."
                    else:
                            #she doesn't care
                            $ EmmaX.FaceChange("sly",1,Brows="confused")
                            ch_e "Боюсь, мои дела- это только МОИ дела."
                            ch_e "Не заставляй меня. . ."
                            return
                    if "mono" not in EmmaX.DailyActions:
                            $ EmmaX.Statup("Obed", 90, 3)
                    $ EmmaX.AddWord(1,0,"mono") #Daily
                    $ EmmaX.Traits.append("mono")
            "Не встречайся с другими девушками." if "mono" not in EmmaX.Traits:
                    if ApprovalCheck(EmmaX, 900, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side")
                            ch_e "Ох, хорошо."
                    elif EmmaX.Thirst >= 60 and not ApprovalCheck(EmmaX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ EmmaX.FaceChange("sly",1)
                            if "mono" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Obed", 90, -2)
                            ch_e "Знаешь, ты же не оставляешь мне иного выбора. . ."
                            return
                    elif ApprovalCheck(EmmaX, 600, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side")
                            ch_e "Если так надо. . ."
                    elif ApprovalCheck(EmmaX, 1500, "LO", TabM=0):
                            #she cares
                            $ EmmaX.FaceChange("sly",1)
                            ch_e "Тебе не стоит разговаривать со мной в таком ключе."
                            ch_e "Но, пожалуй, в этот раз я тебя прощаю. . ."
                    else:
                            #she doesn't care
                            $ EmmaX.FaceChange("sly",1,Brows="confused")
                            ch_e "Мои дела касаются только меня."
                            return
                    if "mono" not in EmmaX.DailyActions:
                            $ EmmaX.Statup("Obed", 90, 3)
                    $ EmmaX.AddWord(1,0,"mono") #Daily
                    $ EmmaX.Traits.append("mono")
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in EmmaX.Traits:
                    if ApprovalCheck(EmmaX, 700, "O", TabM=0):
                            $ EmmaX.FaceChange("sly",1,Eyes="side")
                            ch_e "Конечно."
                    elif ApprovalCheck(EmmaX, 800, "L", TabM=0):
                            $ EmmaX.FaceChange("sly",1)
                            ch_e "Только если я встречу такую, с которой хотела бы. . ."
                    else:
                            $ EmmaX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Love", 90, -2)
                            ch_e "Я не знала, что мне нужно твое разрешение."
                    if "mono" not in EmmaX.DailyActions:
                            $ EmmaX.Statup("Obed", 90, 3)
                    if "mono" in EmmaX.Traits:
                            $ EmmaX.Traits.remove("mono")
                    $ EmmaX.AddWord(1,0,"mono") #Daily
            "Неважно.":
                pass
        return

# end Emma monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_Jumped:
        #called from Emma_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ EmmaX.FaceChange("sly",1,Brows="confused")
        ch_e "Кажется, я припоминаю что-то подобное."
        menu:
            ch_e "К чему ты ведешь?"
            "На будущее, можешь сначала спрашивать?" if "chill" not in EmmaX.Traits:
                    if EmmaX.Thirst >= 60 and not ApprovalCheck(EmmaX, 1600, "LO", TabM=0):
                            #she's too thirsty
                            $ EmmaX.FaceChange("sly",1)
                            if "chill" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Obed", 90, -2)
                            ch_e "У меня есть потребности, которые должны быть удовлетворены."
                            ch_e "Держи ухо востро."
                            return
                    elif ApprovalCheck(EmmaX, 1100, "LO", TabM=0) and EmmaX.Love >= EmmaX.Obed:
                            #she cares
                            $ EmmaX.FaceChange("sly",1)
                            if "chill" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Love", 90, 1)
                            ch_e "Я не хотела тебя расстраивать, [EmmaX.Petname]. . ."
                            ch_e "Постараюсь держать себя в руках. . ."
                    elif ApprovalCheck(EmmaX, 600, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side")
                            ch_e "Если тебе от этого станет спокойнее. . ."
                    else:
                            #she doesn't care
                            $ EmmaX.FaceChange("sly",1,Brows="confused")
                            ch_e "Посмотрим, как я смогу с этим справиться."
                            ch_e "Будь на чеку."
                            return
                    if "chill" not in EmmaX.DailyActions:
                            $ EmmaX.Statup("Obed", 90, 3)
                    $ EmmaX.AddWord(1,0,"chill") #Daily
                    $ EmmaX.Traits.append("chill")
            "Больше так не делай." if "chill" not in EmmaX.Traits:
                    if ApprovalCheck(EmmaX, 900, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side")
                            ch_e "Ох, хорошо."
                    elif EmmaX.Thirst >= 60 and not ApprovalCheck(EmmaX, 600, "O", TabM=0):
                            #she's too thirsty
                            $ EmmaX.FaceChange("sly",1)
                            if "chill" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Obed", 90, -2)
                            ch_e "У меня есть потребности, которые должны быть удовлетворены."
                            ch_e "Держи ухо востро."
                            return
                    elif ApprovalCheck(EmmaX, 450, "O", TabM=0):
                            #she is obedient
                            $ EmmaX.FaceChange("sly",1,Eyes="side")
                            ch_e "Что ж, я не хотела \"приставать\". . ."
                    elif ApprovalCheck(EmmaX, 500, "LO", TabM=0) and not ApprovalCheck(EmmaX, 500, "I", TabM=0):
                            #she cares
                            $ EmmaX.FaceChange("sly",1)
                            ch_e "Не искушай судьбу, [EmmaX.Petname]."
                            ch_e "Но, я постараюсь дать тебе немного личного пространства. . ."
                    else:
                            #she doesn't care
                            $ EmmaX.FaceChange("sly",1,Brows="confused")
                            ch_e "Посмотрим, как я смогу с этим справиться."
                            ch_e "Будь на чеку."
                            return
                    if "chill" not in EmmaX.DailyActions:
                            $ EmmaX.Statup("Obed", 90, 3)
                    $ EmmaX.AddWord(1,0,"chill") #Daily
                    $ EmmaX.Traits.append("chill")
            "Делай что хочешь.":
                    if ApprovalCheck(EmmaX, 800, "L", TabM=0):
                            $ EmmaX.FaceChange("sly",1)
                            ch_e "Буду, не сомневайся. . ."
                    elif ApprovalCheck(EmmaX, 700, "O", TabM=0):
                            $ EmmaX.FaceChange("sly",1,Eyes="side")
                            ch_e "Хорошо."
                    else:
                            $ EmmaX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Love", 90, -2)
                            ch_e "Посмотрим. . ."
                    if "chill" not in EmmaX.DailyActions:
                            $ EmmaX.Statup("Obed", 90, 3)
                    if "chill" in EmmaX.Traits:
                            $ EmmaX.Traits.remove("chill")
                    $ EmmaX.AddWord(1,0,"chill") #Daily
            "Um, never mind.":
                pass
        return

# end Emma jumped  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# start emma hungry  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Hungry:
    if EmmaX.Chat[3]:
        ch_e "Мне нравится твой вкус. . ."
    elif EmmaX.Chat[2]:
        ch_e "Знаешь, эта твоя сыворотка имеет довольно. . . знакомый вкус."
    else:
        ch_e "Мне нравится твой вкус. . ."
    $ EmmaX.Traits.append("hungry")
return


# end emma hungry / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Emma Sexchat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_SexChat:
    $ Line = "Ммм? О чем ты хочешь поговорить?" if not Line else Line
    while True:
            menu:
                ch_e "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in EmmaX.DailyActions:
                        if not Player.Male:
                            ch_e "Я в курсе. Ты уже говорила это мне."
                        else:
                            ch_e "Я в курсе. Ты уже говорил это мне."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "sex":
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Я в курсе. . ."
                                        elif EmmaX.Favorite == "sex":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 10)
                                            ch_e "Ох. . . так и должно быть. . ."
                                        elif EmmaX.Sex:
                                            ch_e "И я знаю почему."
                                        else:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "И -кого- ты трахаешь?"
                                        $ EmmaX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "anal":
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Я уже знаю. . ."
                                        elif EmmaX.Favorite == "anal":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 10)
                                            ch_e "-У меня тоже-. . ."
                                        elif EmmaX.Anal >= 10:
                                            ch_e "Это хорошая тренировка. . ."
                                        elif not EmmaX.Anal:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "Чтю это попку ты трахаешь?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            if not Player.Male:
                                                ch_e "Да, ты была полна восторга. . ."
                                            else:
                                                ch_e "Да, ты был полон восторга. . ."
                                        $ EmmaX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "blow":
                                            $ EmmaX.Statup("Lust", 80, 3)
                                            ch_e "Да, ты говорил. . ."
                                        elif EmmaX.Favorite == "blow":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Ммм. Ты такой вкусный. . ."
                                        elif EmmaX.Blow >= 10:
                                            ch_e "Я не могу жаловаться на это . . ."
                                        elif not EmmaX.Blow:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "О? Какая-то шлюха отсасывает тебе?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "Да, мне он тоже нравится. . . ."
                                        $ EmmaX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "cun":
                                            $ EmmaX.Statup("Lust", 80, 3)
                                            ch_e "Да, ты говорила. . ."
                                        elif EmmaX.Favorite == "cun":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Ммм. Ты такая вкусныая. . ."
                                        elif EmmaX.CUN >= 10:
                                            ch_e "Я не могу жаловаться на это . . ."
                                        elif not EmmaX.CUN:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "О? Какая-то шлюха отлизывает тебе?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "Да, мне он тоже нравится. . . ."
                                        $ EmmaX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "titjob":
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Ты уже говорил. . ."
                                        elif EmmaX.Favorite == "titjob":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 7)
                                            ch_e "Мне тоже очень нравится. . ."
                                        elif EmmaX.Tit >= 10:
                                            ch_e "Не представляю почему. . ."
                                        elif not EmmaX.Tit:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "Ох, кто-то оказывает тебе эту услугу?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "Я могу понять почему. . ."
                                        $ EmmaX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "foot":
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Да, ты говорил. . ."
                                        elif EmmaX.Favorite == "foot":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 7)
                                            ch_e "Мне тоже. . ."
                                        elif EmmaX.Foot >= 10:
                                            ch_e "Да, это хорошая тренировка . . ."
                                        elif not EmmaX.Foot:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "Ох, какая-то маленькая шлюшка предлагает тебе свои ножки?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "Я заметила. . ."
                                        $ EmmaX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "hand":
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Да, ты говорил. . ."
                                        if EmmaX.Favorite == "hand":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 7)
                                            ch_e "Мне тоже. . ."
                                        elif EmmaX.Hand >= 10:
                                            ch_e "Ага, это хорошая тренировка . . ."
                                        elif not EmmaX.Hand:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "Ох, неужели какая-то маленькая шлюшка использует свои ручки?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "Я заметила. . ."
                                        $ EmmaX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "finger":
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Да, ты говорила. . ."
                                        if EmmaX.Favorite == "finger":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 7)
                                            ch_e "А мне нравится это делать. . ."
                                        elif EmmaX.Finger >= 10:
                                            ch_e "Ага, это хорошая тренировка . . ."
                                        elif not EmmaX.Finger:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "Ох, неужели какая-то маленькая шлюшка использует свои пальцы?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "Я заметила. . ."
                                        $ EmmaX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = EmmaX.FondleB + EmmaX.FondleT + EmmaX.SuckB + EmmaX.Hotdog
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "fondle":
                                            $ EmmaX.Statup("Lust", 80, 3)
                                            ch_e "Я уже это слышала. . ."
                                        elif EmmaX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Ты умеешь обращаться с моим телом . ."
                                        elif not Cnt:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "Я не могу себе это представить. Пока."
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "У тебя очень ловкие пальцы . . ."
                                        $ EmmaX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ EmmaX.FaceChange("sly")
                                        if EmmaX.PlayerFav == "kiss you":
                                            $ EmmaX.Statup("Love", 90, 3)
                                            ch_e "Я в курсе. . ."
                                        elif EmmaX.Favorite == "kiss you":
                                            $ EmmaX.Statup("Love", 90, 5)
                                            $ EmmaX.Statup("Lust", 80, 5)
                                            ch_e "Моя романтическая сторона этому рада. . ."
                                        elif EmmaX.Kissed >= 10:
                                            ch_e "Я тоже люблю целовать тебя . . ."
                                        elif not EmmaX.Kissed:
                                            $ EmmaX.FaceChange("perplexed")
                                            ch_e "И с {i}кем{/i} это ты целуешься, [EmmaX.Petname]?"
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            ch_e "Как романтично."
                                        $ EmmaX.PlayerFav = "kiss you"

                        $ EmmaX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(EmmaX, 800):
                                        $ EmmaX.FaceChange("perplexed")
                                        ch_e "Не думаю, что это уместный вопрос. . ."
                                else:
                                        if EmmaX.SEXP >= 50:
                                            $ EmmaX.FaceChange("sly")
                                            if not Player.Male:
                                                ch_e "Ты уже должна знать. . ."
                                            else:
                                                ch_e "Ты уже должен знать. . ."
                                        else:
                                            $ EmmaX.FaceChange("bemused")
                                            $ EmmaX.Eyes = "side"
                                            ch_e "Полагаю, я могу рассказать тебе. . ."


                                        if not EmmaX.Favorite or EmmaX.Favorite == "kiss you":
                                            ch_e "Можешь звать меня романтиком, но мне нравится целовать тебя. . ."
                                        elif EmmaX.Favorite == "anal":
                                                ch_e "Мне очень нравится анал."
                                        elif EmmaX.Favorite == "lick ass":
                                                ch_e "Мне нравится, когда ты вылизаешь мой анус."
                                        elif EmmaX.Favorite == "insert ass":
                                                ch_e "Мне нравится, когда ты вставляешь палец мне в попку."
                                        elif EmmaX.Favorite == "sex":
                                                ch_e "Мне нравится, когда ты жестко меня трахаешь."
                                        elif EmmaX.Favorite == "lick pussy":
                                                ch_e "Мне нравится, когда ты вылизываешь мою киску."
                                        elif EmmaX.Favorite == "fondle pussy":
                                                ch_e "Мне нравится, когда ты трахаешь меня пальцем."
                                        elif EmmaX.Favorite == "blow":
                                                ch_e "Мне очень нравится сосать тебе, это ведь не проблема?"
                                        elif EmmaX.Favorite == "cun":
                                                ch_e "Мне очень нравится лизать тебе, это ведь не проблема?"
                                        elif EmmaX.Favorite == "tit":
                                                ch_e "Мне нравится использовать свои сиськи."
                                        elif EmmaX.Favorite == "foot":
                                                ch_e "Мне нравится использовать ножки."
                                        elif EmmaX.Favorite == "hand":
                                                ch_e "Мне нравиться дрочить тебе руками."
                                        elif EmmaX.Favorite == "finger":
                                                ch_e "Мне нравится ласкать твою киску."
                                        elif EmmaX.Favorite == "hotdog":
                                                ch_e "Мне нравится, когда ты трешься о меня."
                                        elif EmmaX.Favorite == "suck breasts":
                                                ch_e "Ты хорошо сосешь мою грудь."
                                        elif EmmaX.Favorite == "fondle breasts":
                                                ch_e "Ты хорошо ласкаешь мои сиськи."
                                        elif EmmaX.Favorite == "fondle thighs":
                                                ch_e "Мне нравится, когда ты массируешь мои ножки."
                                        else:
                                                ch_e "Я не уверена. . ."

                                # End Emma's favorite things.

                "Не болтай так много во время секса." if "vocal" in EmmaX.Traits:
                        if "setvocal" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("perplexed")
                            if not Player.Male:
                                ch_e "Ты уже выразилась предельно ясно."
                            else:
                                ch_e "Ты уже выразился предельно ясно."
                        else:
                            if ApprovalCheck(EmmaX, 1000) and EmmaX.Obed <= EmmaX.Love:
                                $ EmmaX.FaceChange("bemused")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "Ох, хорошо. . ."
                                $ EmmaX.Traits.remove("vocal")
                            elif ApprovalCheck(EmmaX, 700, "O"):
                                $ EmmaX.FaceChange("sadside")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "Ладно, [EmmaX.Petname]."
                                $ EmmaX.Traits.remove("vocal")
                            elif ApprovalCheck(EmmaX, 600):
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Love", 90, -3)
                                $ EmmaX.Statup("Obed", 50, -1)
                                $ EmmaX.Statup("Inbt", 90, 5)
                                ch_e "Не смей указывать мне, что и сколько говорить, [EmmaX.Petname]."
                            else:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Love", 90, -5)
                                $ EmmaX.Statup("Obed", 60, -3)
                                $ EmmaX.Statup("Inbt", 90, 10)
                                ch_e "Я буду говорить все, что захочу, тебе придется наслаждаться этим."

                            $ EmmaX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in EmmaX.Traits:
                        if "setvocal" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("perplexed")
                            ch_e "Мы это уже обсуждали."
                        else:
                            if ApprovalCheck(EmmaX, 1000) and EmmaX.Obed <= EmmaX.Love:
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Obed", 90, 2)
                                ch_e "Мммм, полагаю, с этим я справлюсь. . ."
                                $ EmmaX.Traits.append("vocal")
                            elif ApprovalCheck(EmmaX, 700, "O"):
                                $ EmmaX.FaceChange("sadside")
                                $ EmmaX.Statup("Obed", 90, 2)
                                ch_e "Если ты этого хочешь, [EmmaX.Petname]."
                                $ EmmaX.Traits.append("vocal")
                            elif ApprovalCheck(EmmaX, 600):
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Obed", 90, 3)
                                ch_e "Ладно, [EmmaX.Petname]."
                                $ EmmaX.Traits.append("vocal")
                            else:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Inbt", 90, 5)
                                ch_e "Если мне захочется."

                            $ EmmaX.DailyActions.append("setvocal")
                        # End Emma Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in EmmaX.Traits:
                        if "initiative" in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("perplexed")
                            ch_e "Мы это уже обсуждали."
                        else:
                            if ApprovalCheck(EmmaX, 1000) and EmmaX.Obed <= EmmaX.Love:
                                $ EmmaX.FaceChange("bemused")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "О, значит ты все берешь на себя? . ."
                                $ EmmaX.Traits.append("passive")
                            elif ApprovalCheck(EmmaX, 700, "O"):
                                $ EmmaX.FaceChange("sadside")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "Буду ждать твоих указаний, [EmmaX.Petname]."
                                $ EmmaX.Traits.append("passive")
                            elif ApprovalCheck(EmmaX, 600):
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Love", 90, -3)
                                $ EmmaX.Statup("Obed", 50, -1)
                                $ EmmaX.Statup("Inbt", 90, 5)
                                ch_e "Полагаю, ты это не всерьез, [EmmaX.Petname]."
                            else:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Love", 90, -5)
                                $ EmmaX.Statup("Obed", 60, -3)
                                $ EmmaX.Statup("Inbt", 90, 10)
                                ch_e "Этого хочешь ты, а не я."

                            $ EmmaX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in EmmaX.Traits:
                        if "initiative" in EmmaX.DailyActions:
                                $ EmmaX.FaceChange("perplexed")
                                ch_e "Мы это уже обсуждали."
                        else:
                            if ApprovalCheck(EmmaX, 1000) and EmmaX.Obed <= EmmaX.Love:
                                $ EmmaX.FaceChange("bemused")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "Ох, как скажешь. . ."
                                $ EmmaX.Traits.remove("passive")
                            elif ApprovalCheck(EmmaX, 700, "O"):
                                $ EmmaX.FaceChange("sadside")
                                $ EmmaX.Statup("Obed", 90, 1)
                                ch_e "Это я могу, [EmmaX.Petname]."
                                $ EmmaX.Traits.remove("passive")
                            elif ApprovalCheck(EmmaX, 600):
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Obed", 90, 3)
                                ch_e "Пожалуй, я согласна, [EmmaX.Petname]."
                                $ EmmaX.Traits.remove("passive")
                            else:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Inbt", 90, 5)
                                ch_e "Посмотрим."

                            $ EmmaX.DailyActions.append("initiative")


                "О том, как ты накидываешься" if "jumped" in EmmaX.History:
                        call Emma_Jumped

                "О \"изоляции разума\"" if "screen" in EmmaX.Traits or "noscreen" in EmmaX.Traits:
                        ch_e "Ты про то, что я могу иногда изолировать нас от Чарльза?"
                        menu:
                            extend ""
                            "Да, начни это делать." if "noscreen" in EmmaX.Traits:
                                ch_e "Замечательно. . ."
                                $ EmmaX.Traits.append("screen")
                            "Не делай этого больше, я хочу, чтобы он знал" if "screen" in EmmaX.Traits:
                                ch_e "Ну ты и шалунишка."
                                if ApprovalCheck(EmmaX, 900, "OI"):
                                        $ EmmaX.FaceChange("sad")
                                        ch_e "Хорошо, я больше не буду нас скрывать."
                                        $ EmmaX.FaceChange("bemused")
                                        $ EmmaX.Traits.append("noscreen")
                                else:
                                        ch_e "Мне очень не нравится его вмешательство."
                                        ch_e "Я все равно буду экранировать нас."
                            "Неважно.":
                                pass

                "О твоей мастурбации":
                        call NoFap(EmmaX)

                "Всегда носи вибратор" if "dailyvibe" not in EmmaX.Traits:
                        call Daily_Vibrator(EmmaX)
                "Перестань всегда носить вибратор" if "dailyvibe" in EmmaX.Traits:
                        ch_e "Ладно. . ."
                        $ EmmaX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи анальную пробку" if "dailyplug" not in EmmaX.Traits:
                        call Daily_Plug(EmmaX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in EmmaX.Traits:
                        ch_e "Ладно. . ."
                        $ EmmaX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Ты не думала о том, чтобы развлекаться на людях?" if "taboocheck" not in EmmaX.History and "taboo" not in EmmaX.History:
                        call Emma_Taboo_Talk
                "Помнишь, мы говорили о том, чтобы развлекаться на людях?" if "taboocheck" in EmmaX.History and "taboo" not in EmmaX.History:
                        call Emma_Taboo_Talk

                "Ты не думала о сексе втроем?" if "threecheck" not in EmmaX.History and "three" not in EmmaX.History:
                        call Emma_ThreeCheck
                "Помнишь, мы говорили о сексе втроем?" if "threecheck" in EmmaX.History and "three" not in EmmaX.History:
                        call Emma_ThreeCheck

                "Неважно" if Line == "Ммм? О чем ты хочешь поговорить?":
                        return
                "На этом все." if Line != "Ммм? О чем ты хочешь поговорить?":
                        return
            if Line == "Ммм? О чем ты хочешь поговорить?":
                $ Line = "Что-нибудь еще?"
    return
# End Emma Sexchat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Emma Chitchat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:
        if EmmaX not in Digits:
                if ApprovalCheck(EmmaX, 850, "LI"):
                    ch_e "Если ты захочешь связаться со мной в нерабочее время. . . вот мой номер телефона."
                    $ Digits.append(EmmaX)
                    return
                elif ApprovalCheck(EmmaX, 500, "OI"):
                    h_e "Мне нужно оставить тебе свои контакты."
                    $ Digits.append(EmmaX)
                    return

        if "hungry" not in EmmaX.Traits and (EmmaX.Swallow + EmmaX.Chat[2]) >= 10 and EmmaX.Loc == bg_current:  #She's swallowed a lot
                    call Emma_Hungry
                    return
        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(EmmaX, 800, "I")):
                    if EmmaX.Loc == bg_current and EmmaX.Thirst >= 30 and "refused" not in EmmaX.DailyActions and "quicksex" not in EmmaX.DailyActions:
                            $ EmmaX.FaceChange("sly",1,Eyes="down")
                            ch_e "Сейчас я испытываю ужасно желание. . . "
                            "[EmmaX.Name] опускает руку вниз и касается своей киски."
                            $ EmmaX.FaceChange("sly",1)
                            ch_e ". . может, ты поможешь мне?"
                            call Quick_Sex(EmmaX)
                            return
        if "loser" in EmmaX.History and ApprovalCheck(EmmaX, 2800) and len(Player.Harem) >= 1 and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Loser
        if "idiot" in EmmaX.History and ApprovalCheck(EmmaX, 2800) and Player.Lvl >= 7 and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Idiot

#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
        if "classcaught" in EmmaX.History:
            if "caught" in EmmaX.DailyActions and "caught chat" not in EmmaX.DailyActions:
                $ Options.append("caught")
            if "screen" not in EmmaX.Traits and "noscreen" not in EmmaX.Traits and "screen" in JeanX.Traits:
                $ Options.append("screen")
            if EmmaX.Event[0] and "key" not in EmmaX.Chat:
                $ Options.append("key")
            if "lover" in EmmaX.Petnames and ApprovalCheck(EmmaX, 900, "L"): # luvy dovey
                $ Options.append("luv")

            if "mandrill" in Player.Traits and "cologne chat" not in EmmaX.DailyActions:
                $ Options.append("mandrill")
            if "purple" in Player.Traits and "cologne chat" not in EmmaX.DailyActions:
                $ Options.append("purple")
            if "corruption" in Player.Traits and "cologne chat" not in EmmaX.DailyActions:
                $ Options.append("corruption")

            if EmmaX.Date >= 1 and bg_current != "bg restaurant":
                #if you've dated before
                $ Options.append("dated")
            if "cheek" in EmmaX.DailyActions and "cheek" not in EmmaX.Chat:
                #If you've touched her cheek today
                $ Options.append("cheek")
            if EmmaX.Kissed >= 5:
                #if you've kissed a few times
                $ Options.append("kissed")
            if "dangerroom" in Player.DailyActions:
                #If you've been in the danger room today
                $ Options.append("dangerroom")
            if "showered" in EmmaX.DailyActions and (Player.Male or "girltalk" in EmmaX.History):
                #If you've caught Emma showering today
                $ Options.append("showercaught")
            if "fondle breasts" in EmmaX.DailyActions or "fondle pussy" in EmmaX.DailyActions or "fondle ass" in EmmaX.DailyActions:
                #If you've fondled Emma today
                $ Options.append("fondled")
            if "Dazzler and Longshot" in EmmaX.Inventory and "256 Shades of Grey" in EmmaX.Inventory and "Avengers Tower Penthouse" in EmmaX.Inventory:
                #If you've given Emma the books
                if "book" not in EmmaX.Chat:
                    $ Options.append("booked")
            if "lace bra" in EmmaX.Inventory or "lace panties" in EmmaX.Inventory:
                #If you've given Emma the lingerie
                if "lingerie" not in EmmaX.Chat:
                    $ Options.append("lingerie")

            if "seenpeen" in EmmaX.History and Player.Male:
                $ Options.append("seenpeen")
            if "topless" in EmmaX.History:
                $ Options.append("topless")
            if "bottomless" in EmmaX.History:
                $ Options.append("bottomless")

            if EmmaX.Hand and Player.Male:
                #If Emma's given a handjob
                $ Options.append("handy")
            if EmmaX.Blow and Player.Male:
                #If Emma's given a blowjob
                $ Options.append("blow")
            if EmmaX.Swallow:
                #If Emma's swallowed before
                $ Options.append("swallowed")
            if "cleaned" in EmmaX.DailyActions or "painted" in EmmaX.DailyActions:
                #If Emma's been facialed
                $ Options.append("facial")
            if EmmaX.Sleep:
                #If Emma's slept over
                $ Options.append("sleep")
            if (EmmaX.CreamP or EmmaX.CreamA) and Player.Male:
                #If Emma's been creampied
                $ Options.append("creampie")
            if EmmaX.Sex or EmmaX.Anal:
                #If Emma's been sexed
                $ Options.append("sexed")
            if EmmaX.Anal:
                #If Emma's been analed
                $ Options.append("anal")
            if "public" in EmmaX.History and "public" not in EmmaX.Chat:
                $ Options.append("public")

            if (bg_current == "bg emma" or bg_current == "bg player") and "relationship" not in EmmaX.DailyActions:
                if "lover" not in EmmaX.Petnames and EmmaX.Love >= 950 and EmmaX.Event[6] != 20: # EmmaX.Event[6]
                    $ Options.append("lover?")
                elif "sir" not in EmmaX.History and EmmaX.Obed >= 500: # EmmaX.Event[7]
                    $ Options.append("sir?")
                elif "daddy" not in EmmaX.Petnames and ApprovalCheck(EmmaX, 750, "L") and ApprovalCheck(EmmaX, 500, "O") and ApprovalCheck(EmmaX, 500, "I"): # EmmaX.Event[5]
                    $ Options.append("daddy?")
                elif "master" not in EmmaX.History and EmmaX.Obed >= 800 and "sir" in EmmaX.Petnames: # EmmaX.Event[8]
                    $ Options.append("master?")
                elif "sex friend" not in EmmaX.Petnames and EmmaX.Inbt >= 500 and bg_current == "bg classroom" and Time_Count == 2: # EmmaX.Event[9]
                    $ Options.append("sexfriend?")
                elif "fuck buddy" not in EmmaX.Petnames and EmmaX.Inbt >= 800 and bg_current != EmmaX.Loc: # EmmaX.Event[10]
                    $ Options.append("fuckbuddy?")


        if not ApprovalCheck(EmmaX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ EmmaX.DailyActions.append("cologne chat")
        $ EmmaX.FaceChange("confused")
        ch_e "(нюх, нюх). . . Ты ведь не используешь дешевый мускус бабуина? . ."
        $ EmmaX.FaceChange("perplexed", 1)
        ch_e ". . . хотя, полагаю. . . он не так уж и плох. . ."
    elif Options[0] == "purple":
        $ EmmaX.DailyActions.append("cologne chat")
        $ EmmaX.FaceChange("sly",1)
        ch_e "(нюх, нюх). . . хм, что это за запах? . ."
        ch_e ". . . могу я что-нибудь для тебя сделать?"
    elif Options[0] == "corruption":
        $ EmmaX.DailyActions.append("cologne chat")
        $ EmmaX.FaceChange("confused")
        ch_e "(нюх, нюх). . . этот. . . запах. . ."
        $ EmmaX.FaceChange("sly")
        ch_e ". . . У меня, возможно. . . позже будет для тебя одно задание. . ."

    elif Options[0] == "caught": # Xavier's caught you
            $ EmmaX.FaceChange("angry", Eyes="side")
            if "caught chat" in EmmaX.Chat:
                    ch_e "Мне уже порядком надоело, что меня вызывают в кабинет Чарльза."
                    ch_e "Возможно, нам следует быть более . . . сдержанными."
                    if not ApprovalCheck(EmmaX, 500, "I"):
                        $ EmmaX.FaceChange("sly", Eyes="side")
                        ch_e "Иногда. . ."
            else:
                    ch_e "Что ж, это было неприятно."
                    ch_e "Ксавье говорил не меньше часа."
                    ch_e "Нес какой-то бред про \"обязанности педагога.\""
                    ch_e "К твоему сведению, я отношусь к своим обязанностям перед студентами. . ."
                    $ EmmaX.FaceChange("sly")
                    ch_e "-очень- серьезно. . ."
                    if not ApprovalCheck(EmmaX, 500, "I"):
                        ch_e "Я не уверена, что мы можем продолжать развлекаться на людях."
                    else:
                        ch_e "Однако, мне понравилось видеть старого заунуду таким взволнованным. . ."
                    $ EmmaX.Chat.append("caught chat")

    elif Options[0] == "screen": # Xavier's caught you
            $ EmmaX.FaceChange("angry")
            ch_e "Чарльз!"
            ch_e "Я устала от его вмешательства в наши дела!"
            $ EmmaX.FaceChange("surprised")
            ch_e "О!"
            $ EmmaX.FaceChange("sly")
            ch_e "У меня появилась идея."
            ch_e "Я могла бы использовать свои способности, чтобы нейтрализовать его, сделать так, чтобы он нас \"не видел\"."
            menu:
                "Конечно, давай так и сделаем.":
                    ch_e "Замечательно. . ."
                    $ EmmaX.Traits.append("screen")
                "Нет, я хочу, чтобы он знал.":
                    ch_e "Ну ты и шалунишка."
                    if ApprovalCheck(EmmaX, 900, "OI"):
                            $ EmmaX.FaceChange("sad")
                            ch_e "Хорошо, тогда не будем скрываться."
                            $ EmmaX.FaceChange("bemused")
                            $ EmmaX.Traits.append("noscreen")
                    else:
                            ch_e "Даже если ты этого хочешь, мне все равно не нравится его вмешательство."
                            ch_e "Я буду экранировать нас."
                            $ EmmaX.Traits.append("screen")
    elif Options[0] == "key": # you have her key
            if EmmaX.SEXP <= 15:
                if not Player.Male:
                    ch_e "Если я дала тебе ключ от своей комнаты, это не значит, что ты не должна стучаться. . ."
                else:
                    ch_e "Если я дала тебе ключ от своей комнаты, это не значит, что ты не должен стучаться. . ."
            else:
                ch_e "Я дала тебе свой ключ не просто так, возможно, ты захочешь когда-нибудь им воспользоваться. . ."
            $ EmmaX.Chat.append("key")

    elif Options[0] == "cheek":
            #Emma's response to having her cheek touched.
            if not Player.Male:
                ch_e "Ты погладила меня по щеке. . ."
            else:
                ch_e "Ты погладил меня по щеке. . ."
            ch_p "Да? Тебе понравилось?"
            if ApprovalCheck(EmmaX, 600, "L"):
                    $ EmmaX.FaceChange("smile",1)
                    ch_e "Да. Это было так. . . интимно."
                    $ EmmaX.Chat.append("cheek")
            elif ApprovalCheck(EmmaX, 800):
                    $ EmmaX.FaceChange("normal",1,Eyes="side")
                    ch_e "Я. . . полагаю, это так, [EmmaX.Petname]."
            else:
                    $ EmmaX.FaceChange("confused",1,Eyes="side")
                    ch_e "Я думаю, что ты. . . забегаешь немного вперед."


    elif Options[0] == "dated":
            #Emma's response to having gone on a date with the Player.
            ch_e "Тебе стоит знать, мне понравилось наше последнее свидание. Мы должны как-нибудь повторить."

    elif Options[0] == "kissed":
            #Emma's response to having been kissed by the Player.
            $ EmmaX.FaceChange("sly",1)
            ch_e "У тебя удивительно умелые губы, [EmmaX.Petname]."
            menu:
                extend ""
                "Хех. . . когда все делаешь как надо, ты хорош." if Player.Male:
                        $ EmmaX.FaceChange("smile",1)
                        ch_e "О, не зазнавайся."
                        ch_e "-только если ты не собираешься заняться мной."
                "Хех. . . когда все делаешь как надо, ты хороша." if not Player.Male:
                        $ EmmaX.FaceChange("smile",1)
                        ch_e "О, не зазнавайся."
                        ch_e "-только если ты не собираешься заняться мной."
                "Ты правда так думаешь?":
                        ch_e "Ох, научись принимать комплименты, [EmmaX.Petname]."

    elif Options[0] == "dangerroom":
            #Emma's response to Player working out in the Danger Room while Emma is present
            $ EmmaX.FaceChange("sly",1)
            ch_e "Я видела твой последний сеанс в Комнате Опасности, [EmmaX.Petname]."
            ch_e "Твоя форма. . . тебе к лицу."

    elif Options[0] == "showercaught":
            #Emma's response to being caught in the shower.
            if "shower" in EmmaX.Chat:
                ch_e "Насладился зрелищем?"
            else:
                ch_e "Я надеюсь, что мое присутствие в душе не слишком тебя смутило."
                $ EmmaX.Chat.append("shower")
                menu:
                    extend ""
                    "Это была чистая случайность! Клянусь!":
                            $ EmmaX.Statup("Love", 50, 5)
                            $ EmmaX.Statup("Love", 90, 2)
                            if ApprovalCheck(EmmaX, 1000):
                                $ EmmaX.FaceChange("sly",1)
                                ch_e "М? Значит я могу не расчитывать на продолжение?"
                            else:
                                $ EmmaX.FaceChange("smile")
                                ch_e "Бывает, только не привыкай."
                    "Наглядеться на тебя не могу.":
                            $ EmmaX.Statup("Obed", 40, 5)
                            if ApprovalCheck(EmmaX, 1000) or ApprovalCheck(EmmaX, 700, "L"):
                                    $ EmmaX.Statup("Love", 90, 3)
                                    $ EmmaX.FaceChange("sly",1)
                                    ch_e "О, уверена, это правда. . ."
                                    ch_e "Приятно слышать."
                            else:
                                    $ EmmaX.Statup("Love", 70, -5)
                                    $ EmmaX.FaceChange("angry", Eyes="side")
                                    ch_e "Полагаю, лучше ты, чем Циклоп."
                    "Я заглянула умышленно. Но я ни о чем не жалею." if not Player.Male:
                            if ApprovalCheck(EmmaX, 1200):
                                    $ EmmaX.Statup("Love", 90, 3)
                                    $ EmmaX.Statup("Obed", 70, 10)
                                    $ EmmaX.Statup("Inbt", 50, 5)
                                    $ EmmaX.FaceChange("sly",1)
                                    ch_e "Что ж. . . Ценю твою честность."
                                    $ EmmaX.FaceChange("sly",1, Eyes="side")
                                    ch_e ". . .если бы ты еще довела дело до конца."
                            elif ApprovalCheck(EmmaX, 800):
                                    $ EmmaX.Statup("Obed", 60, 5)
                                    $ EmmaX.Statup("Inbt", 50, 5)
                                    $ EmmaX.FaceChange("perplexed",2)
                                    ch_e "Хм? Полагаю, я не могу винить тебя за это."
                            else:
                                    $ EmmaX.Statup("Love", 50, -10)
                                    $ EmmaX.Statup("Love", 80, -10)
                                    $ EmmaX.Statup("Obed", 50, 10)
                                    $ EmmaX.FaceChange("angry")
                                    ch_e "На удивление, ты честная, но наглая."
                    "Я заглянул умышленно. Но я ни о чем не жалею." if Player.Male:
                            if ApprovalCheck(EmmaX, 1200):
                                    $ EmmaX.Statup("Love", 90, 3)
                                    $ EmmaX.Statup("Obed", 70, 10)
                                    $ EmmaX.Statup("Inbt", 50, 5)
                                    $ EmmaX.FaceChange("sly",1)
                                    ch_e "Что ж. . . Ценю твою честность."
                                    $ EmmaX.FaceChange("sly",1, Eyes="side")
                                    ch_e ". . .если бы ты еще довел дело до конца."
                            elif ApprovalCheck(EmmaX, 800):
                                    $ EmmaX.Statup("Obed", 60, 5)
                                    $ EmmaX.Statup("Inbt", 50, 5)
                                    $ EmmaX.FaceChange("perplexed",2)
                                    ch_e "Хм? Полагаю, я не могу винить тебя за это."
                            else:
                                    $ EmmaX.Statup("Love", 50, -10)
                                    $ EmmaX.Statup("Love", 80, -10)
                                    $ EmmaX.Statup("Obed", 50, 10)
                                    $ EmmaX.FaceChange("angry")
                                    ch_e "На удивление, ты честный, но наглый."

    elif Options[0] == "fondled":
            #Emma's response to being felt up.
            if EmmaX.FondleB + EmmaX.FondleP + EmmaX.FondleA >= 10:
                ch_e "Позже мне понадобится помощь."
            else:
                ch_e "У тебя неплохие навыки в. . . массаже."
                ch_e "Полагаю, нам стоит изучить их подробнее. . ."

    elif Options[0] == "booked":
            #Emma's response after a Player gives her the books from the shop.
            if not Player.Male:
                ch_e "Я прочитала. . . книги, которые ты мне дала."
            else:
                ch_e "Я прочитала. . . книги, которые ты мне дал."
            menu:
                extend ""
                "Да? Они тебе понравились?":
                        $ EmmaX.FaceChange("sly",2)
                        ch_e "Они немного простоваты, но вдохновляют."
                "Хорошо. Пожалуй, ты могла бы чему-нибудь из них научиться.":
                        $ EmmaX.Statup("Love", 90, 3)
                        $ EmmaX.Statup("Inbt", 50, 10)
                        $ EmmaX.FaceChange("sly")
                        ch_e "Ох, [EmmaX.Petname], то, чему я смогла бы научить этих авторов, свело бы их с ума."
            $ EmmaX.Blush = 1
            $ EmmaX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Emma's response to being given lingerie.
            $ EmmaX.FaceChange("sly")
            if not Player.Male:
                ch_e "[EmmaX.Petname], я хочу еще раз поблагодарить тебя за. . .-одежду-, что ты купила мне."
            else:
                ch_e "[EmmaX.Petname], я хочу еще раз поблагодарить тебя за. . .-одежду-, что ты купил мне."
            ch_e "Она замечательная."
            $ EmmaX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Emma's response after giving the Player a handjob.
            $ EmmaX.FaceChange("sly", Eyes="side")
            ch_e "Знаешь, я думала о своей руке,"
            $ EmmaX.FaceChange("sly")
            ch_e "на твоем члене. . ."
            ch_e "Ох, выражение твоего лица в этот момент бесценно. . ."
            ch_e "Полагаю, нам нужно будет как-нибудь повторить. . ."

    elif Options[0] == "blow":
            if "blow" not in EmmaX.Chat:
                    #Emma's response after giving the Player a blowjob.
                    $ EmmaX.FaceChange("sly",2)
                    ch_e "Знаешь, [EmmaX.Petname], У тебя очень уникальный вкус."
                    ch_p "А?"
                    ch_e "То есть, вкус твоего члена."
                    ch_e "Очень. . . приятный."
                    menu:
                        extend ""
                        "Если хочешь, можешь взять добавку.":
                                    $ EmmaX.Statup("Love", 90, 5)
                                    $ EmmaX.Statup("Inbt", 60, 10)
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "Учту."
                        "Я рад, что ты сравниваешь меня с другими парнями.":
                                if ApprovalCheck(EmmaX, 300, "I") or not ApprovalCheck(EmmaX, 800):
                                    $ EmmaX.Statup("Obed", 60, 10)
                                    $ EmmaX.Statup("Inbt", 50, 10)
                                    $ EmmaX.FaceChange("smile",1)
                                    ch_e "Ох, ты определенно выделяешься."
                                else:
                                    $ EmmaX.Statup("Love", 80, -2)
                                    $ EmmaX.Statup("Obed", 70, 10)
                                    $ EmmaX.Statup("Inbt", 50, 5)
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "Ты что, намекаешь на мой. . . опыт?"
                    $ EmmaX.Blush = 1
                    $ EmmaX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["Мне нравится твой вкус.",
                            "Моя челюсть в последнее время немного побаливает.",
                            "Если тебе понадобится немного. . . внимания, дай мне знать.",
                            "Ммм. . . [Стучит языком по внутренней стороне щеки.]"])
                    ch_e "[Line]"

    elif Options[0] == "swallowed":
            #Emma's response after swallowing the Player's cum.
            if "swallow" in EmmaX.Chat:
                ch_e "Пожалуй, я хочу еще раз попробовать твой. . . экстракт."
            else:
                if not Player.Male:
                    ch_e "У твоих соков и правда неповторимый вкус, [EmmaX.Petname]."
                else:
                    ch_e "У твоей спермы и правда неповторимый вкус, [EmmaX.Petname]."
                $ EmmaX.FaceChange("sly",1)
                ch_e "Очень. . . бодрящий. . ."
                $ EmmaX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Emma's response after taking a facial from the Player.
            $ EmmaX.FaceChange("sexy")
            ch_e "Может, в следующий раз ты постараешься кончить подальше от моих глаз?"

    elif Options[0] == "sleepover":
            #Emma's response after sleeping with the Player.
            ch_e "У тебя такой беспокойный сон, что это наводит меня на кое-какие. . . мысли."

    elif Options[0] == "creampie":
            #Another of Emma's responses after having sex with the Player.
            "[EmmaX.Name] подходит к вам вплотную и начинает шептать на ухо."
            if not Player.Male:
                ch_e "Я все еще чувствую, как они. . . стекают по моей ноге."
            else:
                ch_e "Я все еще чувствую, как она. . . стекает по моей ноге."

    elif Options[0] == "sexed":
            #A final response from Emma after having sex with the Player.
            $ EmmaX.FaceChange("sexy",2)
            ch_e "С тех пор, как я с тобой, мне есть чем заняться после занятий. . ."

    elif Options[0] == "anal":
            #Emma's response after getting anal from the Player.
            $ EmmaX.FaceChange("sly",1)
            ch_e "Давненько я никого не впускала в \"заднюю дверь\"."
            $ EmmaX.FaceChange("sexy")
            if not Player.Male:
                ch_e "Я рада, что ты \"вошла туда.\""
            else:
                ch_e "Я рада, что ты \"вошел туда.\""

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ EmmaX.FaceChange("sly",1)
            ch_e "Возможно, мне нужно было сказать раньше,"
            $ EmmaX.FaceChange("sly",1, Eyes="down")
            if not Player.Male:
                ch_e "Твоя киска очень интересная."
            else:
                ch_e "Твой член - очень интересный образец."
            $ EmmaX.FaceChange("bemused",1)
            $ EmmaX.Statup("Love", 50, 5)
            $ EmmaX.Statup("Love", 90, 10)
            $ EmmaX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            $ EmmaX.FaceChange("sly",1)
            if not Player.Male:
                ch_e "Интересно, когда ты увидела мою грудь впервые. . ."
                ch_e "Ты именно такой ее себе представляла?"
            else:
                ch_e "Интересно, когда ты увидел мою грудь впервые. . ."
                ch_e "Ты именно такой ее себе представлял?"
            call Girl_First_TMenu
            $ EmmaX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            $ EmmaX.FaceChange("sly",1)
            if not Player.Male:
                ch_e "Интересно, когда ты увидела мою киску впервые. . ."
                ch_e "Что ты о ней подумала?"
            else:
                ch_e "Интересно, когда ты увидел мою киску впервые. . ."
                ch_e "Что ты о ней подумал?"
            call Girl_First_BMenu
            $ EmmaX.History.remove("bottomless")

    elif Options[0] == "boyfriend?":
        call Emma_BF
    elif Options[0] == "lover?":
        call Emma_Love
    elif Options[0] == "sir?":
        call Emma_Sub
    elif Options[0] == "master?":
        call Emma_Master
    elif Options[0] == "sexfriend?":
        call Emma_Sexfriend
    elif Options[0] == "fuckbuddy?":
        call Emma_Fuckbuddy
    elif Options[0] == "daddy?":
        call Emma_Daddy

    elif Options[0] == "public": # You had sex in public
                $ EmmaX.FaceChange("sly")
                ch_e "Хм, полагаю, тайное рано или поздно становиться явным."
                $ EmmaX.FaceChange("sly", Eyes="side",Brows="angry")
                if "spotted" in EmmaX.DailyActions:
                    ch_e "Сейчас поползут слухи из-за представления, что мы устроили ранее."
                else:
                    ch_e "Думаю, скоро поползут слухи из-за представления, что мы устроили несколько дней назад."
                ch_e ". . ."
                $ EmmaX.FaceChange("sly")
                $ EmmaX.Statup("Obed", 70, 10)
                $ EmmaX.Statup("Inbt", 60, 10)
                $ EmmaX.Statup("Inbt", 90, 10)
                ch_e "Полагаю, мы должны дать еще немного поводов для слухов. . ."
                $ EmmaX.Chat.append("public")

    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Я бы предпочла, чтобы наши отношения оставались чисто деловыми.",
                "Если хочешь что-то сказать, напиши на бумаге.",
                "Отвали.",
                "Оставь меня в покое."])
        ch_e "[Line]"

    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)
            if D20 == 1:
                    $ EmmaX.FaceChange("smile")
                    if not Player.Male:
                        ch_e "Ты отлично справилась с тестом на днях."
                    else:
                        ch_e "Ты отлично справился с тестом на днях."
            elif D20 == 2:
                    $ EmmaX.FaceChange("sad")
                    ch_e "В последнее время у меня ужасно много бумажной работы."
                    $ EmmaX.FaceChange("bemused")
                    ch_e "Может быть, зайдешь после занятий и поможешь?"
            elif D20 == 3:
                    $ EmmaX.FaceChange("surprised")
                    if not Player.Male:
                        ch_e "Ты бы видела, что раньше надевала мисс Прайд!"
                    else:
                        ch_e "Ты бы видел, что раньше надевала мисс Прайд!"
            elif D20 == 4:
                    $ EmmaX.FaceChange("sad")
                    ch_e "Подготовка к тесту на следующею неделю утомительна!"
            elif D20 == 5:
                    $ EmmaX.FaceChange("smile")
                    ch_e "Сегодня очень замечательный день для прогулки. . ."
            elif D20 == 6:
                    $ EmmaX.FaceChange("startled")
                    ch_e "В последнее время было много серьезных проблем от атак Стражей."
            elif D20 == 7:
                    $ EmmaX.FaceChange("smile")
                    ch_e "Я только что получила положительный отчет о проделанной работе."
            elif D20 == 8:
                    $ EmmaX.FaceChange("sad")
                    ch_e "Это прекрасное учебное заведение, но я скучаю по удобствам большого города."
            elif D20 == 9:
                    $ EmmaX.FaceChange("confused")
                    ch_e "У тебя тоже этот странный гул от Ксавье в голове или только у меня?"
            elif D20 == 10:
                    $ EmmaX.FaceChange("smile")
                    ch_e "Думаю, учебные занятия подходят к концу."
            elif D20 == 11:
                    $ EmmaX.FaceChange("smile")
                    ch_e "Я с нетерпением жду следующей тренировки."
            elif D20 == 12:
                    $ EmmaX.FaceChange("sad")
                    ch_e "Не знаю, что делать с оценками Роуг, они начинают падать."
            elif D20 == 13:
                    $ EmmaX.FaceChange("smile")
                    ch_e "Не подумай, я не пьянчуга, но я хочу выпить."
            elif D20 == 14:
                    $ EmmaX.FaceChange("sad")
                    ch_e "В новостях я услышала о еще одной атаке. Все печально."
            elif D20 == 15:
                    $ EmmaX.FaceChange("sadside")
                    ch_e "Кажется, я что-то потянула во время вчерашней тренировки."
                    $ EmmaX.FaceChange("sly",Mouth="normal")
                    if not Player.Male:
                        ch_e "Возможно, ты могла бы помочь мне?"
                    else:
                        ch_e "Возможно, ты мог бы помочь мне?"
            else:
                    $ EmmaX.FaceChange("startled")
                    ch_e "С каждым годом, студенты все более невыносимые."

    $ Line = 0
    return

# start Emma_Names / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Names(TempName=0):
    call LastNamer
    $ TempName = _return
    menu:
        ch_e "Ох? Как ты хочешь, чтобы я звала тебя?"
        "Зовт меня мистером [Player.Name_tvo].":
            # ie "Mr. Zero"
            $ EmmaX.Petname = "мистер [Player.Name]"
            $ EmmaX.Petname_rod = "мистера [Player.Name_rod]"
            $ EmmaX.Petname_dat = "мистеру [Player.Name_dat]"
            $ EmmaX.Petname_vin = "мистера [Player.Name_vin]"
            $ EmmaX.Petname_tvo = "мистером [Player.Name_tvo]"
            $ EmmaX.Petname_pre = "мистере [Player.Name_pre]"
            ch_e "Я так и думала, [EmmaX.Petname]."
        "Зови меня по имени.":
            $ EmmaX.Petname = Player.Name
            $ EmmaX.Petname_rod = Player.Name_rod
            $ EmmaX.Petname_dat = Player.Name_dat
            $ EmmaX.Petname_vin = Player.Name_vin
            $ EmmaX.Petname_tvo = Player.Name_tvo
            $ EmmaX.Petname_pre = Player.Name_pre
            ch_e "Если ты этого хочешь, [EmmaX.Petname]."
        "Зови меня \"дорогая\"." if "dear" in EmmaX.Petnames and not Player.Male:
            $ EmmaX.Petname = "дорогая"
            $ EmmaX.Petname_rod = "дорогой"
            $ EmmaX.Petname_dat = "дорогой"
            $ EmmaX.Petname_vin = "дорогую"
            $ EmmaX.Petname_tvo = "дорогой"
            $ EmmaX.Petname_pre = "дорогой"
            ch_e "Конечно, [EmmaX.Petname]."
        "Зови меня \"дорогой\"." if "dear" in EmmaX.Petnames and Player.Male:
            $ EmmaX.Petname = "дорогой"
            $ EmmaX.Petname_rod = "дорогого"
            $ EmmaX.Petname_dat = "дорогому"
            $ EmmaX.Petname_vin = "дорогого"
            $ EmmaX.Petname_tvo = "дорогим"
            $ EmmaX.Petname_pre = "дорогом"
            ch_e "Конечно, [EmmaX.Petname]."
        "Зови меня \"милая\"." if "darling" in EmmaX.Petnames and not Player.Male:
            $ EmmaX.Petname = "милая"
            $ EmmaX.Petname_rod = "милой"
            $ EmmaX.Petname_dat = "милой"
            $ EmmaX.Petname_vin = "милую"
            $ EmmaX.Petname_tvo = "милой"
            $ EmmaX.Petname_pre = "милой"
            ch_e "Конечно, [EmmaX.Petname]."
        "Зови меня \"милый\"." if "darling" in EmmaX.Petnames and Player.Male:
            $ EmmaX.Petname = "милый"
            $ EmmaX.Petname_rod = "милого"
            $ EmmaX.Petname_dat = "милому"
            $ EmmaX.Petname_vin = "милого"
            $ EmmaX.Petname_tvo = "милым"
            $ EmmaX.Petname_pre = "милом"
            ch_e "Конечно, [EmmaX.Petname]."
        "Зови меня своей \"девушкой\"." if "boyfriend" in EmmaX.Petnames and not Player.Male:
            $ EmmaX.Petname = "моя девушка"
            $ EmmaX.Petname_rod = "моей девушки"
            $ EmmaX.Petname_dat = "моей девушке"
            $ EmmaX.Petname_vin = "мою девушку"
            $ EmmaX.Petname_tvo = "моей девушкой"
            $ EmmaX.Petname_pre = "моей девушке"
            ch_e "Как банально, но ладно, [EmmaX.Petname]."
        "Зови меня своим \"парнем\"." if "boyfriend" in EmmaX.Petnames and Player.Male:
            $ EmmaX.Petname = "мой парень"
            $ EmmaX.Petname_rod = "моего парня"
            $ EmmaX.Petname_dat = "моему парню"
            $ EmmaX.Petname_vin = "моего парня"
            $ EmmaX.Petname_tvo = "моим парнем"
            $ EmmaX.Petname_pre = "моем парне"
            ch_e "Как банально, но ладно, [EmmaX.Petname]."
        "Зови меня \"любимая\"." if "lover" in EmmaX.Petnames and not Player.Male:
            $ EmmaX.Petname = "любимая"
            $ EmmaX.Petname_rod = "любимой"
            $ EmmaX.Petname_dat = "любимой"
            $ EmmaX.Petname_vin = "любимую"
            $ EmmaX.Petname_tvo = "любимой"
            $ EmmaX.Petname_pre = "любимой"
            ch_e "Конечно, [EmmaX.Petname]."
        "Зови меня \"любимый\"." if "lover" in EmmaX.Petnames and Player.Male:
            $ EmmaX.Petname = "любимый"
            $ EmmaX.Petname_rod = "любимого"
            $ EmmaX.Petname_dat = "любимому"
            $ EmmaX.Petname_vin = "любимого"
            $ EmmaX.Petname_tvo = "любимым"
            $ EmmaX.Petname_pre = "любимом"
            ch_e "Конечно, [EmmaX.Petname]."
        "Зови меня \"госпожа\"." if "sir" in EmmaX.Petnames and not Player.Male:
            $ EmmaX.Petname = "госпожа"
            $ EmmaX.Petname_rod = "госпожи"
            $ EmmaX.Petname_dat = "госпоже"
            $ EmmaX.Petname_vin = "госпожу"
            $ EmmaX.Petname_tvo = "госпожой"
            $ EmmaX.Petname_pre = "госпоже"
            ch_e "Ладно, [EmmaX.Petname]."
        "Зови меня \"господин\"." if "sir" in EmmaX.Petnames and Player.Male:
            $ EmmaX.Petname = "господин"
            $ EmmaX.Petname_rod = "господина"
            $ EmmaX.Petname_dat = "господину"
            $ EmmaX.Petname_vin = "господина"
            $ EmmaX.Petname_tvo = "господином"
            $ EmmaX.Petname_pre = "господине"
            ch_e "Ладно, [EmmaX.Petname]."
        "Зови меня \"хозяйка\"." if "master" in EmmaX.Petnames and not Player.Male:
            $ EmmaX.Petname = "хозяйка"
            $ EmmaX.Petname_rod = "хозяйки"
            $ EmmaX.Petname_dat = "хозяйке"
            $ EmmaX.Petname_vin = "хозяйку"
            $ EmmaX.Petname_tvo = "хозяйкой"
            $ EmmaX.Petname_pre = "хозяйке"
            ch_e "Как пожелаешь, [EmmaX.Petname]."
        "Зови меня \"хозяин\"." if "master" in EmmaX.Petnames and Player.Male:
            $ EmmaX.Petname = "хозяин"
            $ EmmaX.Petname = "хозяин"
            $ EmmaX.Petname_rod = "хозяина"
            $ EmmaX.Petname_dat = "хозяину"
            $ EmmaX.Petname_vin = "хозяина"
            $ EmmaX.Petname_tvo = "хозяином"
            $ EmmaX.Petname_pre = "хозяине"
            ch_e "Как пожелаешь, [EmmaX.Petname]."
        "Зови меня \"любовница\"." if "sex friend" in EmmaX.Petnames and not Player.Male:
            $ EmmaX.Petname = "любовница"
            $ EmmaX.Petname_rod = "любовницы"
            $ EmmaX.Petname_dat = "любовнице"
            $ EmmaX.Petname_vin = "любовницу"
            $ EmmaX.Petname_tvo = "любовницей"
            $ EmmaX.Petname_pre = "любовнице"
            ch_e "Шалунишка. Отлично, [EmmaX.Petname]."
        "Зови меня \"любовник\"." if "sex friend" in EmmaX.Petnames and Player.Male:
            $ EmmaX.Petname = "любовник"
            $ EmmaX.Petname_rod = "любовника"
            $ EmmaX.Petname_dat = "любовнику"
            $ EmmaX.Petname_vin = "любовника"
            $ EmmaX.Petname_tvo = "любовником"
            $ EmmaX.Petname_pre = "любовнике"
            ch_e "Шалунишка. Отлично, [EmmaX.Petname]."
        "Зови меня \"секс-партнерша\"." if "fuck buddy" in EmmaX.Petnames and not Player.Male:
            $ EmmaX.Petname = "секс-партнерша"
            $ EmmaX.Petname_rod = "секс-партнерши"
            $ EmmaX.Petname_dat = "секс-партнерше"
            $ EmmaX.Petname_vin = "секс-партнершу"
            $ EmmaX.Petname_tvo = "секс-партнершей"
            $ EmmaX.Petname_pre = "секс-партнерше"
            ch_e "Как неприятно, но ладно, \"[EmmaX.Petname]\"."
        "Зови меня \"секс-партнер\"." if "fuck buddy" in EmmaX.Petnames and Player.Male:
            $ EmmaX.Petname = "секс-партнер"
            $ EmmaX.Petname_rod = "секс-партнера"
            $ EmmaX.Petname_dat = "секс-партнеру"
            $ EmmaX.Petname_vin = "секс-партнера"
            $ EmmaX.Petname_tvo = "секс-партнером"
            $ EmmaX.Petname_pre = "секс-партнере"
            ch_e "Как неприятно, но ладно, \"[EmmaX.Petname]\"."
        "Зови меня \"мамочка\"." if "daddy" in EmmaX.Petnames and not Player.Male:
            $ EmmaX.Petname = "мамочка"
            $ EmmaX.Petname_rod = "мамочки"
            $ EmmaX.Petname_dat = "мамочке"
            $ EmmaX.Petname_vin = "мамочку"
            $ EmmaX.Petname_tvo = "мамочкой"
            $ EmmaX.Petname_pre = "мамочке"
            ch_e "Ммм, ладно, [EmmaX.Petname]."
        "Зови меня \"папочка\"." if "daddy" in EmmaX.Petnames and Player.Male:
            $ EmmaX.Petname = "папочка"
            $ EmmaX.Petname_rod = "папочки"
            $ EmmaX.Petname_dat = "папочке"
            $ EmmaX.Petname_vin = "папочку"
            $ EmmaX.Petname_tvo = "папочкой"
            $ EmmaX.Petname_pre = "папочке"
            ch_e "Ммм, ладно, [EmmaX.Petname]."
        "Зови меня \"малышка\"." if "daddy" in EmmaX.Petnames and not Player.Male:
            $ EmmaX.Petname = "малышка"
            $ EmmaX.Petname_rod = "малышки"
            $ EmmaX.Petname_dat = "малышке"
            $ EmmaX.Petname_vin = "малышку"
            $ EmmaX.Petname_tvo = "малышкой"
            $ EmmaX.Petname_pre = "малышке"
            ch_e "О, ты хочешь быть моей малышкой?"
        "Зови меня \"малыш\"." if "daddy" in EmmaX.Petnames and Player.Male:
            $ EmmaX.Petname = "малыш"
            $ EmmaX.Petname_rod = "малыша"
            $ EmmaX.Petname_dat = "малышу"
            $ EmmaX.Petname_vin = "малыша"
            $ EmmaX.Petname_tvo = "малышом"
            $ EmmaX.Petname_pre = "малыше"
            ch_e "О, ты хочешь быть моим малышом?"
        "Неважно.":
            return
    return
# end Emma_Names//////////////////////////////////////////////////////////

label Emma_Pet:
    while 1:
        menu:
            extend ""
            "Обходительно":
                menu:
                    extend ""
                    "Думаю, буду просто звать тебя мисс Фрост.":
                        $ EmmaX.Pet = "Эмма Фрост"
                        $ EmmaX.Pet_rod = "Эммы Фрост"
                        $ EmmaX.Pet_dat = "Эмме Фрост"
                        $ EmmaX.Pet_vin = "Эмму Фрост"
                        $ EmmaX.Pet_tvo = "Эммой Фрост"
                        $ EmmaX.Pet_pre = "Эмме Фрост"
                        $ EmmaX.Name = "Эмма Фрост"
                        $ EmmaX.Name_rod = "Эммы Фрост"
                        $ EmmaX.Name_dat = "Эмме Фрост"
                        $ EmmaX.Name_vin = "Эмму Фрост"
                        $ EmmaX.Name_tvo = "Эммой Фрост"
                        $ EmmaX.Name_pre = "Эмме Фрост"
                        ch_e "Почему бы и нет, [EmmaX.Petname]."

                    "Думаю, я буду звать тебя просто Эммой.":
                        if ApprovalCheck(EmmaX, 700) or "classcaught" in EmmaX.History:
                            ch_e "Почему бы и нет, [EmmaX.Petname]."
                            $ EmmaX.Pet = "Эмма"
                            $ EmmaX.Pet_rod = "Эммы"
                            $ EmmaX.Pet_dat = "Эмме"
                            $ EmmaX.Pet_vin = "Эмму"
                            $ EmmaX.Pet_tvo = "Эммой"
                            $ EmmaX.Pet_pre = "Эмме"
                            $ EmmaX.Name = "Эмма"
                            $ EmmaX.Name_rod = "Эммы"
                            $ EmmaX.Name_dat = "Эмме"
                            $ EmmaX.Name_vin = "Эмму"
                            $ EmmaX.Name_tvo = "Эммой"
                            $ EmmaX.Name_pre = "Эмме"
                        else:
                            ch_e "Я бы этого не хотела, [EmmaX.Petname]."

                    "Думаю, буду звать тебя \"моя девушка\".":
                        if "boyfriend" in EmmaX.Petnames:
                            $ EmmaX.FaceChange("sexy", 1)
                            $ EmmaX.Pet = "моя девушка"
                            $ EmmaX.Pet_rod = "моей девушки"
                            $ EmmaX.Pet_dat = "моей девушке"
                            $ EmmaX.Pet_vin = "мою девушку"
                            $ EmmaX.Pet_tvo = "моей девушкой"
                            $ EmmaX.Pet_pre = "моей девушке"
                            ch_e "Забавно, [EmmaX.Petname]."
                        else:
                            $ EmmaX.FaceChange("angry")
                            ch_e "Не надо, [EmmaX.Petname]."

                    "Думаю, буду звать тебя \"детка\".":
                        if "boyfriend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 800, "L"):
                            $ EmmaX.FaceChange("bemused", 1)
                            $ EmmaX.Pet = "детка"
                            $ EmmaX.Pet_rod = "детки"
                            $ EmmaX.Pet_dat = "детке"
                            $ EmmaX.Pet_vin = "детку"
                            $ EmmaX.Pet_tvo = "деткой"
                            $ EmmaX.Pet_pre = "детке"
                            ch_e "Как мило, [EmmaX.Petname]."
                        else:
                            $ EmmaX.FaceChange("angry")
                            ch_e "Я не такая, [EmmaX.Petname]."

                    "Думаю, буду звать тебя \"крошка\".":
                        if "boyfriend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 800, "L"):
                            $ EmmaX.FaceChange("sexy", 1)
                            $ EmmaX.Pet = "крошка"
                            $ EmmaX.Pet_rod = "крошки"
                            $ EmmaX.Pet_dat = "крошке"
                            $ EmmaX.Pet_vin = "крошку"
                            $ EmmaX.Pet_tvo = "крошкой"
                            $ EmmaX.Pet_pre = "крошке"
                            ch_e "Полагаю, я и есть твоя. . . \"крошка?\""
                        else:
                            $ EmmaX.FaceChange("angry")
                            ch_e "Что это хотя бы значит?."

                    "Думаю, буду звать тебя \"малышка\"":
                        if "boyfriend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 500, "L"):
                            $ EmmaX.Pet = "малышка"
                            $ EmmaX.Pet_rod = "малышки"
                            $ EmmaX.Pet_dat = "малышке"
                            $ EmmaX.Pet_vin = "малышку"
                            $ EmmaX.Pet_tvo = "малышкой"
                            $ EmmaX.Pet_pre = "малышке"
                            $ EmmaX.FaceChange("sexy", 1)
                            ch_e "Как здорово."
                        else:
                            $ EmmaX.FaceChange("angry")
                            ch_e "Думаю, я слишком зрелая для этого."

                    "Думаю, буду звать тебя \"дорогая\".":
                        if "boyfriend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 600, "L"):
                            $ EmmaX.Pet = "дорогая"
                            $ EmmaX.Pet_rod = "дорогой"
                            $ EmmaX.Pet_dat = "дорогой"
                            $ EmmaX.Pet_vin = "дорогую"
                            $ EmmaX.Pet_tvo = "дорогой"
                            $ EmmaX.Pet_pre = "дорогой"
                            ch_e "Я тебя обожаю, [EmmaX.Petname]."
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Немного преждевременно, [EmmaX.Petname]."

                    "Думаю, буду звать тебя \"милая\".":
                        if "boyfriend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 500, "L"):
                            $ EmmaX.Pet = "милая"
                            $ EmmaX.Pet_rod = "милой"
                            $ EmmaX.Pet_dat = "милой"
                            $ EmmaX.Pet_vin = "милую"
                            $ EmmaX.Pet_tvo = "милой"
                            $ EmmaX.Pet_pre = "милой"
                            ch_e "Правда, [EmmaX.Petname]?"
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Слишком слащаво, [EmmaX.Petname]."

                    "Думаю, буду звать тебя \"секси\".":
                        if "lover" in EmmaX.Petnames or ApprovalCheck(EmmaX, 900):
                            $ EmmaX.Pet = "секси"
                            $ EmmaX.Pet_rod = "секси"
                            $ EmmaX.Pet_dat = "секси"
                            $ EmmaX.Pet_vin = "секси"
                            $ EmmaX.Pet_tvo = "секси"
                            $ EmmaX.Pet_pre = "секси"
                            $ EmmaX.FaceChange("sexy", 1)
                            ch_e "Не буду спорить, [EmmaX.Petname]."
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Немного черезчур, [EmmaX.Petname]."

                    "Думаю, буду звать тебя \"любимая\".":
                        if "lover" in EmmaX.Petnames or ApprovalCheck(EmmaX, 900, "L"):
                            $ EmmaX.Pet = "любимая"
                            $ EmmaX.Pet_rod = "любимой"
                            $ EmmaX.Pet_dat = "любимой"
                            $ EmmaX.Pet_vin = "любимую"
                            $ EmmaX.Pet_tvo = "любимой"
                            $ EmmaX.Pet_pre = "любимой"
                            $ EmmaX.FaceChange("sexy", 1)
                            ch_e "Я люблю тебя, [EmmaX.Petname]!"
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Не в этой жизни, [EmmaX.Petname]."

                    "Назад":
                        pass

            "Грубо":
                menu:
                    "Думаю, буду звать тебя \"рабыня\".":
                        if "master" in EmmaX.Petnames or ApprovalCheck(EmmaX, 900, "O"):
                            $ EmmaX.Pet = "рабыня"
                            $ EmmaX.Pet_rod = "рабыни"
                            $ EmmaX.Pet_dat = "рабыне"
                            $ EmmaX.Pet_vin = "рабыню"
                            $ EmmaX.Pet_tvo = "рабыней"
                            $ EmmaX.Pet_pre = "рабыне"
                            $ EmmaX.FaceChange("bemused", 1)
                            ch_e "Как пожелаешь, [EmmaX.Petname]."
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Ни один человек не сделает меня рабыней, [EmmaX.Petname]."

                    "Думаю, буду звать тебя \"питомец\".":
                        if "master" in EmmaX.Petnames or ApprovalCheck(EmmaX, 600, "O"):
                            $ EmmaX.Pet = "питомец"
                            $ EmmaX.Pet_rod = "питомце"
                            $ EmmaX.Pet_dat = "питомцу"
                            $ EmmaX.Pet_vin = "питомца"
                            $ EmmaX.Pet_tvo = "питомцем"
                            $ EmmaX.Pet_pre = "питомце"
                            $ EmmaX.FaceChange("bemused", 1)
                            ch_e "Пока ты меня гладишь, [EmmaX.Petname]."
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Сомневаюсь, что тебе понравится, если я стану твоим питомцем, [EmmaX.Petname]."

                    "Думаю, буду звать тебя \"шлюха\".":
                        if "sex friend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 1000, "OI"):
                            $ EmmaX.Pet = "шлюха"
                            $ EmmaX.Pet_rod = "шлюхи"
                            $ EmmaX.Pet_dat = "шлюхе"
                            $ EmmaX.Pet_vin = "шлюху"
                            $ EmmaX.Pet_tvo = "шлюхой"
                            $ EmmaX.Pet_pre = "шлюхе"
                            $ EmmaX.FaceChange("sexy")
                            ch_e "Я не могу не согласиться, [EmmaX.Petname]."
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            $ EmmaX.Mouth = "surprised"
                            ch_e "На твоем месте, я бы пересмотрела свое решение."

                    "Думаю, буду звать тебя \"блядь\".":
                        if "fuckbuddy" in EmmaX.Petnames or ApprovalCheck(EmmaX, 1100, "OI"):
                            $ EmmaX.Pet = "блядь"
                            $ EmmaX.Pet_rod = "бляди"
                            $ EmmaX.Pet_dat = "бляде"
                            $ EmmaX.Pet_vin = "блядь"
                            $ EmmaX.Pet_tvo = "блядью"
                            $ EmmaX.Pet_pre = "бляде"
                            $ EmmaX.FaceChange("sly")
                            ch_e "Но только для тебя. . ."
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Последний человек, который так назвал меня, даже не помнит своего имени."

                    "Думаю, буду звать тебя \"сладкогрудая\".":
                        if "sex friend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 1400):
                            $ EmmaX.Pet = "сладкогрудая"
                            $ EmmaX.Pet_rod = "сладкогрудой"
                            $ EmmaX.Pet_dat = "сладкогрудой"
                            $ EmmaX.Pet_vin = "сладкогрудую"
                            $ EmmaX.Pet_tvo = "сладкогрудой"
                            $ EmmaX.Pet_pre = "сладкогрудой"
                            $ EmmaX.FaceChange("sly", 1)
                            ch_e "Конечно, они у меня очень сладкие. . ."
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Я ожидала от тебе большего, [EmmaX.Petname]."

                    "Думаю, буду звать тебя \"любовница\".":
                        if "sex friend" in EmmaX.Petnames or ApprovalCheck(EmmaX, 600, "I"):
                            $ EmmaX.Pet = "любовница"
                            $ EmmaX.Pet_rod = "любовницы"
                            $ EmmaX.Pet_dat = "любовнице"
                            $ EmmaX.Pet_vin = "любовницу"
                            $ EmmaX.Pet_tvo = "любовницей"
                            $ EmmaX.Pet_pre = "любовнице"
                            $ EmmaX.FaceChange("sly")
                            ch_e "Ммм?"
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Очень надеюсь, на людях ты меня так не будешь звать, [EmmaX.Petname]."

                    "Думаю, буду звать тебя \"секс-партнерша\".":
                        if "fuckbuddy" in EmmaX.Petnames or ApprovalCheck(EmmaX, 700, "I"):
                            $ EmmaX.Pet = "секс-партнерша"
                            $ EmmaX.Pet_rod = "секс-партнерши"
                            $ EmmaX.Pet_dat = "секс-партнерше"
                            $ EmmaX.Pet_vin = "секс-партнершу"
                            $ EmmaX.Pet_tvo = "секс-партнершей"
                            $ EmmaX.Pet_pre = "секс-партнерше"
                            $ EmmaX.FaceChange("bemused")
                            ch_e "Что ж. . . хорошо."
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            $ EmmaX.Mouth = "surprised"
                            ch_e "Как глупо."

                    "Думаю, буду звать тебя \"доченька\".":
                        if "daddy" in EmmaX.Petnames or ApprovalCheck(EmmaX, 1200):
                            $ EmmaX.Pet = "доченька"
                            $ EmmaX.Pet_rod = "доченьки"
                            $ EmmaX.Pet_dat = "доченьке"
                            $ EmmaX.Pet_vin = "доченьку"
                            $ EmmaX.Pet_tvo = "доченькой"
                            $ EmmaX.Pet_pre = "доченьке"
                            $ EmmaX.FaceChange("smile", 1)
                            ch_e "Очаровательно."
                        else:
                            $ EmmaX.FaceChange("angry", 1)
                            ch_e "Совсем не к месту."

                    "Думаю, буду звать тебя \"мамочка\".":
                        if "mommy" in EmmaX.Pets or ApprovalCheck(EmmaX, 1500):
                            $ EmmaX.FaceChange("sly", 1, Mouth="kiss")
                            $ EmmaX.Pet = "мамочка"
                            $ EmmaX.Pet_rod = "мамочки"
                            $ EmmaX.Pet_dat = "мамочке"
                            $ EmmaX.Pet_vin = "мамочку"
                            $ EmmaX.Pet_tvo = "мамочкой"
                            $ EmmaX.Pet_pre = "мамочке"
                            ch_e "Ооох, [EmmaX.Petname]."
                        else:
                            $ EmmaX.FaceChange("angry")
                            ch_e "Это слишком, [EmmaX.Petname]"

                    "Думаю, буду звать тебя \"Белая Королева\"." if "White Queen" in EmmaX.Pets or "Белая Королева" in EmmaX.Pets:
                        $ EmmaX.Pet = "Белая Королева"
                        $ EmmaX.Pet_rod = "Белой Королевы"
                        $ EmmaX.Pet_dat = "Белой Королеве"
                        $ EmmaX.Pet_vin = "Белую Королеву"
                        $ EmmaX.Pet_tvo = "Белой Королевой"
                        $ EmmaX.Pet_pre = "Белой Королеве"
                        $ EmmaX.FaceChange("sly", 1, Mouth="kiss")
                        ch_e "Ооох, [EmmaX.Petname]."

                    "Назад":
                        pass

            "Неважно.":
                return
    return

#label Emma_Namecheck(EmmaX.Pet = EmmaX.Pet, Cnt = 0, Ugh = 0):#$ Girl.NameCheck() #checks reaction to petname

# start Emma_Rename//////////////////////////////////////////////////////////
label Emma_Rename:
        #Sets alternate names from Emma
        $ EmmaX.Mouth = "smile"
        ch_e "Да, и?"
        menu:
            extend ""
            "Думаю, \"Эмма\" красивое имя." if EmmaX.Name != "Emma" and "Emma" in EmmaX.Names:
                    $ EmmaX.Name = "Эмма"
                    $ EmmaX.Name_rod = "Эммы"
                    $ EmmaX.Name_dat = "Эмме"
                    $ EmmaX.Name_vin = "Эмму"
                    $ EmmaX.Name_tvo = "Эммой"
                    $ EmmaX.Name_pre = "Эмме"
                    ch_e "Мне всегда оно нравилось. . ."
            "Думаю, \"Мисс Фрост\" звучит круто." if EmmaX.Name != "Ms. Frost" and "Ms. Frost" in EmmaX.Names:
                    $ EmmaX.Name = "Эмма Фрост"
                    $ EmmaX.Name_rod = "Эммы Фрост"
                    $ EmmaX.Name_dat = "Эмме Фрост"
                    $ EmmaX.Name_vin = "Эмму Фрост"
                    $ EmmaX.Name_tvo = "Эммой Фрост"
                    $ EmmaX.Name_pre = "Эмме Фрост"
                    if ApprovalCheck(EmmaX, 1000, "LI"):
                            $ EmmaX.FaceChange("sly", 1)
                            if "namechange" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Obed", 70, 2)
                                    $ EmmaX.Statup("Inbt", 70, 3)
                            ch_e "Шалунишка. . ."
                    else:
                            ch_e "Полагаю, нам стоит придерживаться формального общения. . ."
            "Мне нравится прозвище \"Белая Королева.\"" if EmmaX.Name != "White Queen" and "White Queen" in EmmaX.Names:
                    $ EmmaX.Name = "Белая Королева"
                    $ EmmaX.Name_rod = "Белой Королевы"
                    $ EmmaX.Name_dat = "Белой Королеве"
                    $ EmmaX.Name_vin = "Белую Королеву"
                    $ EmmaX.Name_tvo = "Белой Королевой"
                    $ EmmaX.Name_pre = "Белой Королеве"
                    if not ApprovalCheck(EmmaX, 500, "I"):
                            $ EmmaX.FaceChange("confused")
                            if not Player.Male:
                                ch_e "Где ты это услышала-"
                            else:
                                ch_e "Где ты это услышал-"
                            $ EmmaX.FaceChange("sly", 2)
                            if "namechange" not in EmmaX.DailyActions:
                                    $ EmmaX.Statup("Love", 80, 2)
                                    $ EmmaX.Statup("Obed", 70, 2)
                                    $ EmmaX.Statup("Inbt", 80, 3)
                            if not Player.Male:
                                ch_e "Ах ты маленькая негодница. . ."
                            else:
                                ch_e "Ах ты негодник. . ."
                    else:
                            $ EmmaX.FaceChange("confused")
                            ch_e "Что ж, полагаю, я не против, если ты будешь звать меня так. . ."
                    $ EmmaX.FaceChange()
            "Неважно.":
                    pass
        $ EmmaX.AddWord(1,0,"namechange")
        return
# end Emma_Rename//////////////////////////////////////////////////////////

# start Emma_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Personality(Cnt = 0):
    if not EmmaX.Chat[4] or Cnt:
        "Поскольку у вас все хорошо получается в одной области, вы можете убедить Эмму сосредоточиться на любой другой."
        "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
        "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
    menu:
        ch_e "Конечно, в чем дело?"
        "Больше Послушания. [[Любовь в Послушание]" if EmmaX.Love > 900:
            ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
            ch_e "Для тебя все, что угодно, [EmmaX.Petname]."
            $ EmmaX.Chat[4] = 1
        "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if EmmaX.Love > 900:
            ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
            ch_e "Не думаю, что смогу стать еще более раскрепощенной, но я попробую."
            $ EmmaX.Chat[4] = 2

        "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if EmmaX.Obed > 900:
            ch_p "Я хочу, чтобы ты была более раскрепощенной."
            ch_e "Если ты так говоришь. . ."
            $ EmmaX.Chat[4] = 3
        "Больше Любви. [[Повиновение в Любовь]" if EmmaX.Obed > 900:
            ch_p "Я хочу, чтобы ты училась любить меня."
            ch_e "Я попробую."
            $ EmmaX.Chat[4] = 4

        "Больше Повиновения. [[Раскрепощенность в Повиновение]" if EmmaX.Inbt > 900:
            ch_p "Я знаю, что нам и так весело, но разве ты не можешь иногда слушаться меня?"
            ch_e "Это тебя раздражает?"
            $ EmmaX.Chat[4] = 5

        "Больше Любви. [[Раскрепощенность в Любовь]" if EmmaX.Inbt > 900:
            ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
            ch_e "Ладно. . ."
            $ EmmaX.Chat[4] = 6

        "Просто делай то, что тебе нравится. . .[[Сбросить]" if EmmaX.Chat[4]:
            ch_p "Помнишь, что мы обсуждали? Забудь."
            ch_e "Хорошо?"
            $ EmmaX.Chat[4] = 0
        "Повторить правила":
            call Emma_Personality(1)
            return
        "Неважно.":
            return
    return
# end Emma_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Emma_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_Summon(Tempmod=Tempmod):
    $ EmmaX.OutfitChange()
    if "no summon" in EmmaX.RecentActions:
                if "angry" in EmmaX.RecentActions:
                    ch_e "Я не в настроении, [EmmaX.Petname]."
                elif EmmaX.RecentActions.count("no summon") > 1:
                    if not Player.Male:
                        ch_e "Ты уже меня слышала."
                    else:
                        ch_e "Ты уже меня слышал."
                    $ EmmaX.RecentActions.append("angry")
                elif Time_Count >= 3: #night time
                    ch_e "Тебе уже давно пора спать."
                else:
                    ch_e "Как я уже сказала, у меня есть дела."
                $ EmmaX.RecentActions.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if EmmaX.Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = -30
    elif EmmaX.Loc == "bg classroom":
        $ Tempmod = -10
    elif EmmaX.Loc == "bg dangerroom":
        $ Tempmod = -10
    elif EmmaX.Loc == "bg showerroom":
        $ Tempmod = -30

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"
    if Time_Count >= 3: #night time
                if ApprovalCheck(EmmaX, 700, "L") or ApprovalCheck(EmmaX, 300, "O"):
                        #It's night time but she likes you.
                        if not Player.Male:
                            ch_e "Уже поздно, но ладно, что ты хотела?"
                        else:
                            ch_e "Уже поздно, но ладно, что ты хотел?"
                        $ EmmaX.Loc = bg_current
                        call Taboo_Level
                        call Set_The_Scene
                else:
                        #It's night time and she isn't into you
                        ch_e "Уже поздно, [EmmaX.Petname], поговорим завтра."
                        $ EmmaX.RecentActions.append("no summon")
                return
    elif "les" in EmmaX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(EmmaX, 2000):
                    ch_e "Я. . . сейчас развлекаюсь, [EmmaX.Petname], не хочешь присоедениться к нам?"
                    menu:
                        extend ""
                        "Конечно.":
                            $ Line = "go to"
                        "Нет, спасибо.":
                            ch_e "Многое теряешь."
                            return
            else:
                    ch_e "Ох. . . Это может быть проблемой, нам - мне. . ."
                    ch_e "нездоровится. . ."
                    ch_e "Возможно, мы могли бы встретиться позже."
                    $ EmmaX.RecentActions.append("no summon")
                    return
    elif not ApprovalCheck(EmmaX, 700, "L") or not ApprovalCheck(EmmaX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(EmmaX, 300):
                ch_e "Мне сейчас не до этого, [EmmaX.Petname]."
                $ EmmaX.RecentActions.append("no summon")
                return


        if "summoned" in EmmaX.RecentActions:
                pass
        elif "goto" in EmmaX.RecentActions:
                if not Player.Male:
                    ch_e "Ты только что ушла, почему бы тебе не вернуться?"
                else:
                    ch_e "Ты только что ушел, почему бы тебе не вернуться?"
        elif EmmaX.Loc == "bg classroom" or EmmaX.Loc == "bg teacher":
                ch_e "Ты можешь найти меня в аудитории, [EmmaX.Petname]."
        elif EmmaX.Loc == "bg dangerroom":
                ch_e "Я тренируюсь, [EmmaX.Petname], не хочешь присоединиться ко мне?"
        elif EmmaX.Loc == "bg campus":
                ch_e "Я отдыхаю на площади, можешь присоедениться ко мне."
        elif EmmaX.Loc == "bg emma":
                ch_e "Я в своей комнате, [EmmaX.Petname]."
        elif EmmaX.Loc == "bg player":
                ch_e "Я жду в твоей комнате, [EmmaX.Petname]. . ."
        elif EmmaX.Loc == "bg showerroom":
            if ApprovalCheck(EmmaX, 1600):
                ch_e "Я сейчас в душе, [EmmaX.Petname], тебе нужно особое приглашение?"
            else:
                ch_e "Я сейчас в душе, [EmmaX.Petname], возможно, увидимся позже."
                $ EmmaX.RecentActions.append("no summon")
                return
        elif EmmaX.Loc == "hold":
                ch_e "Я ненадолго уехала из кампуса, вернусь позже."
                $ EmmaX.RecentActions.append("no summon")
                return
        else:
                ch_e "Ты всегда можешь прийти ко мне, [EmmaX.Petname]."


        if "summoned" in EmmaX.RecentActions:
            ch_e "Снова? Что ж, хорошо."
            $ Line = "yes"
        elif "goto" in EmmaX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
#                                ch_e "I'll be waiting."
                                $ Line = "go to"
                "Нет.":
                                ch_e "Хорошо."
                "Мне бы -очень- хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(EmmaX, 600, "L") or ApprovalCheck(EmmaX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(EmmaX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(EmmaX, 1400):
                                #she is generally favorable
                                ch_e "Хмм, хорошо."
                                $ Line = "yes"
                        elif ApprovalCheck(EmmaX, 200, "O"):
                                #she is not obedient
                                ch_e "Если тебе повезет, ты сможешь найти меня там же."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(EmmaX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(EmmaX, 1400):
                                #she is generally favorable
                                ch_e "Хмм, хорошо."
                                $ Line = "yes"
                        elif ApprovalCheck(EmmaX, 200, "O"):
                                #she is not obedient
                                ch_e "Если тебе повезет, ты сможешь найти меня там же."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Конечно, сейчас приду.":
                    $ EmmaX.Statup("Love", 55, 1)
                    $ EmmaX.Statup("Inbt", 30, 1)
#                    ch_e "I'll be waiting."
                    $ Line = "go to"

                "Нет, поговорим позже.":
                    $ EmmaX.Statup("Obed", 50, 1)
                    $ EmmaX.Statup("Obed", 30, 2)
                    ch_e "Very well."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                    if ApprovalCheck(EmmaX, 600, "L") or ApprovalCheck(EmmaX, 1400):
                        $ EmmaX.Statup("Love", 70, 1)
                        $ EmmaX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ EmmaX.Statup("Inbt", 30, 1)
                        $ Line = "no"

                "Приходи ко мне, будет весело.":
                        if ApprovalCheck(GwenX, 400, "L") and ApprovalCheck(EmmaX, 800):
                            $ EmmaX.Statup("Love", 70, 1)
                            $ EmmaX.Statup("Obed", 50, 1)
                            $ Line = "fun"
                        else:
                            $ EmmaX.Statup("Inbt", 30, 1)
                            $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                    if ApprovalCheck(EmmaX, 600, "O"):
                        #she is obedient
                        $ EmmaX.Statup("Love", 50, 1, 1)
                        $ EmmaX.Statup("Love", 40, -1)
                        $ EmmaX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(EmmaX, 1400):
                        #she is generally favorable
                        $ EmmaX.Statup("Love", 70, -2)
                        $ EmmaX.Statup("Love", 90, -1)
                        $ EmmaX.Statup("Obed", 50, 2)
                        $ EmmaX.Statup("Obed", 90, 1)
                        ch_e "Ладно, хорошо, [EmmaX.Petname]."
                        $ Line = "yes"

                    elif ApprovalCheck(EmmaX, 200, "O"):
                        #she is not obedient
                        $ EmmaX.Statup("Love", 70, -4)
                        $ EmmaX.Statup("Love", 90, -2)
                        ch_e "Как думаешь, кто здесь главный?!"
                        $ EmmaX.Statup("Inbt", 40, 2)
                        $ EmmaX.Statup("Inbt", 60, 1)
                        $ EmmaX.Statup("Obed", 70, -2)
                        ch_e "Лучше тебе не попадаться мне на глаза."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ EmmaX.Statup("Inbt", 30, 1)
                        $ EmmaX.Statup("Inbt", 50, 1)
                        $ EmmaX.Statup("Love", 50, -1, 1)
                        $ EmmaX.Statup("Obed", 70, -1)
                        $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                    if ApprovalCheck(EmmaX, 600, "O"):
                        #she is obedient
                        $ EmmaX.Statup("Love", 50, 1, 1)
                        $ EmmaX.Statup("Love", 40, -1)
                        $ EmmaX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(EmmaX, 1400):
                        #she is generally favorable
                        $ EmmaX.Statup("Love", 70, -2)
                        $ EmmaX.Statup("Love", 90, -1)
                        $ EmmaX.Statup("Obed", 50, 2)
                        $ EmmaX.Statup("Obed", 90, 1)
                        ch_e "Ладно, хорошо, [EmmaX.Petname]."
                        $ Line = "yes"

                    elif ApprovalCheck(EmmaX, 200, "O"):
                        #she is not obedient
                        $ EmmaX.Statup("Love", 70, -4)
                        $ EmmaX.Statup("Love", 90, -2)
                        ch_e "Как думаешь, кто здесь главный?!"
                        $ EmmaX.Statup("Inbt", 40, 2)
                        $ EmmaX.Statup("Inbt", 60, 1)
                        $ EmmaX.Statup("Obed", 70, -2)
                        ch_e "Лучше тебе не попадаться мне на глаза."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ EmmaX.Statup("Inbt", 30, 1)
                        $ EmmaX.Statup("Inbt", 50, 1)
                        $ EmmaX.Statup("Love", 50, -1, 1)
                        $ EmmaX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if EmmaX.Love > EmmaX.Obed:
            ch_e "С удовольствием."
        else:
            ch_e "Сейчас приду, [EmmaX.Petname]."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ EmmaX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            if EmmaX.Loc == "bg teacher":
                ch_e "Я не могу покинуть аудиторию, [EmmaX.Petname]."
            elif EmmaX.Loc == "bg classroom":
                ch_e "У меня много работы, [EmmaX.Petname]."
            elif EmmaX.Loc == "bg dangerroom":
                ch_e "Я только разогрелась."
            else:
                ch_e "Мне сперва многое нужно закончить."
            $ EmmaX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ Tempmod = 0
            $ Line = 0
            $ Party = [EmmaX]
            $ Nearby = []
            $ EmmaX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            if EmmaX.Loc == "bg classroom" or EmmaX.Loc == "bg teacher":
                    ch_e "Давай быстрее, а то многое пропустишь."
                    jump Class_Room
            elif EmmaX.Loc == "bg dangerroom":
                    ch_e "Я постараюсь оставить немного для тебя."
                    jump Danger_Room
            elif EmmaX.Loc == "bg emma":
                    ch_e "Пока немного приберусь."
                    jump Emma_Room
            elif EmmaX.Loc == "bg player":
                    ch_e "Я буду ждать тебя."
                    jump Player_Room
            elif EmmaX.Loc == "bg showerroom":
                    ch_e "Не заставляй меня ждать . ."
                    jump Shower_Room
            elif EmmaX.Loc == "bg campus":
                    ch_e "Я выбрала хорошее местечко."
                    jump Campus
            elif EmmaX.Loc != "hold":
                    ch_e "Постараюсь пока чем-нибудь занять себя."
                    $ bg_current = EmmaX.Loc
                    jump Misplaced
            else:
                    ch_e "Давай просто встретимся у меня в комнате."
                    $ EmmaX.Loc = "bg emma"
                    jump Emma_Room

    #She's agreed to come over
    elif Line == "lonely":
            ch_e "Хорошо, нам не стоит этого допускать."
    elif Line == "command":
            ch_e "Если так надо. . ."
    elif Line == "fun":
            ch_e "Конечно."

    $ EmmaX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(EmmaX)
            return
    $ EmmaX.Loc = bg_current
    call Taboo_Level(0)
    $ EmmaX.OutfitChange()
    call Set_The_Scene
    return

# End Emma Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Emma_Leave(Tempmod=Tempmod, GirlsNum = 0):
    if "leaving" in EmmaX.RecentActions:
        $ EmmaX.DrainWord("leaving")
    else:
        return

    if EmmaX.Loc == "hold":
            # Activates if she's being moved out of play
            ch_e "Извини, у меня есть кое-какие дела."
            return

    if EmmaX in Party or "lockedtravels" in EmmaX.Traits:
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ EmmaX.Loc = bg_current
            return

    elif "freetravels" in EmmaX.Traits or not ApprovalCheck(EmmaX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.
            $ EmmaX.OutfitChange()
            if GirlsNum: #if someone left before her
                        ch_e "Мне тоже пора идти."

            if EmmaX.Loc == "bg teacher":
                        ch_e "У меня занятия."
            elif EmmaX.Loc == "bg classroom":
                        ch_e "Мне нужно разобраться с бумагами."
            elif EmmaX.Loc == "bg dangerroom":
                        ch_e "У меня запланирована тренировка."
            elif EmmaX.Loc == "bg campus":
                        ch_e "Я собираюсь немного позагорать."
            elif EmmaX.Loc == "bg emma":
                        ch_e "Я возвращаюсь в свою комнату."
            elif EmmaX.Loc == "bg player":
                        ch_e "Я пойду в твою комнату."
            elif EmmaX.Loc == "bg showerroom" and ApprovalCheck(EmmaX, 1400):
                        ch_e "Я быстренько приму душ."
            elif EmmaX.Loc == "bg pool":
                        ch_e "Я собираюсь поплавать."
            else:
                        ch_e "Увидимся позже."
            hide Emma_Sprite
            return
            #End Free Travels

    if bg_current == "bg dangerroom":
            call Gym_Exit([EmmaX])

    $ EmmaX.OutfitChange()

    if "follow" not in EmmaX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ EmmaX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    # Sets her preferences
    if EmmaX.Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = -40
    elif EmmaX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif EmmaX.Loc == "bg dangerroom":
        $ Tempmod = 20
    elif EmmaX.Loc == "bg showerroom":
        $ Tempmod = 20


    if GirlsNum: #if someone left before her
                ch_e "Я тоже пойду."

    if EmmaX.Loc == "bg teacher":
        if not Player.Male:
            ch_e "У меня занятие, ты могла бы что-нибудь подчерпнуть на нем."
        else:
            ch_e "У меня занятие, ты мог бы что-нибудь подчерпнуть на нем."
    elif EmmaX.Loc == "bg classroom":
        ch_e "Мне нужно разобраться с бумагами, но ты можешь составить мне компанию."
    elif EmmaX.Loc == "bg dangerroom":
        ch_e "У меня запланирована тренировка, но я могу позаниматься и с тобой."
    elif EmmaX.Loc == "bg campus":
        ch_e "Я планирую немного позагорать, присоединишься ко мне?"
    elif EmmaX.Loc == "bg emma":
        ch_e "Я возвращаюсь в свою комнату, но ты можешь проводить меня."
    elif EmmaX.Loc == "bg player":
        ch_e "Вообще-то я направляюсь в твою комнату, [EmmaX.Petname]."
    elif EmmaX.Loc == "bg mall":
        ch_e "У меня впланах кое-что прикупить, не хочешь присоединиться ко мне?"
    elif EmmaX.Loc == "bg showerroom":
        if ApprovalCheck(EmmaX, 1600):
            ch_e "Я быстренько приму душ, присоединишься ко мне?"
        else:
            ch_e "Я иду в душ, держись подальше."
            return
    elif EmmaX.Loc == "bg pool":
            ch_e "Я собираюсь поплавать. Присоединишься ко мне?"
    else:
            ch_e "Не хочешь пойти со мной?"


    menu:
        extend ""
        "Конечно, я сразу за тобой.":
                if "followed" not in EmmaX.RecentActions:
                    $ EmmaX.Statup("Love", 55, 1)
                    $ EmmaX.Statup("Inbt", 30, 1)
                $ Line = "go to"

        "Нет, поговорим позже.":
                if "followed" not in EmmaX.RecentActions:
                    $ EmmaX.Statup("Obed", 50, 1)
                    $ EmmaX.Statup("Obed", 30, 2)
                ch_e "Что ж, хорошо."

        "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                if ApprovalCheck(EmmaX, 600, "L") or ApprovalCheck(EmmaX, 1400):
                    if "followed" not in EmmaX.RecentActions:
                        $ EmmaX.Statup("Love", 70, 1)
                        $ EmmaX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else:
                    if "followed" not in EmmaX.RecentActions:
                        $ EmmaX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Останься со мной, будет весело.":
                if ApprovalCheck(GwenX, 400, "L") and ApprovalCheck(EmmaX, 800):
                    $ EmmaX.Statup("Love", 70, 1)
                    $ EmmaX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else:
                    $ EmmaX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Нет, останься здесь.":
                if ApprovalCheck(EmmaX, 600, "O"):
                    #she is obedient
                    if "followed" not in EmmaX.RecentActions:
                        if EmmaX.Love >= 50:
                            $ EmmaX.Statup("Love", 90, 1)
                        $ EmmaX.Statup("Love", 40, -1)
                        $ EmmaX.Statup("Obed", 90, 1)
                    $ Line = "command"

                elif D20 >= 7 and ApprovalCheck(EmmaX, 1400):
                    #she is generally favorable
                    if "followed" not in EmmaX.RecentActions:
                        $ EmmaX.Statup("Love", 70, -2)
                        $ EmmaX.Statup("Love", 90, -1)
                        $ EmmaX.Statup("Obed", 50, 2)
                        $ EmmaX.Statup("Obed", 90, 1)
                    ch_e "Думаю, дела могут и подождать. . ."
                    $ Line = "yes"

                elif ApprovalCheck(EmmaX, 200, "O"):
                    #she is not obedient
                    if "followed" not in EmmaX.RecentActions:
                        $ EmmaX.Statup("Love", 70, -4)
                        $ EmmaX.Statup("Love", 90, -2)
                    ch_e "Это работает с твоими шлюшками?"
                    if "followed" not in EmmaX.RecentActions:
                        $ EmmaX.Statup("Inbt", 40, 2)
                        $ EmmaX.Statup("Inbt", 60, 1)
                        $ EmmaX.Statup("Obed", 70, -2)
                else:
                    #she is obedient, but you failed to meet the checks
                    if "followed" not in EmmaX.RecentActions:
                        $ EmmaX.Statup("Inbt", 30, 1)
                        $ EmmaX.Statup("Inbt", 50, 1)
                        $ EmmaX.Statup("Love", 50, -1, 1)
                        $ EmmaX.Statup("Obed", 70, -1)
                    $ Line = "no"
                #End ordered to stay

    call Taboo_Level(0)
    $ EmmaX.RecentActions.append("followed")
    if not Line:
            #You end the dialog neutrally
            hide Emma_Sprite
            call Gym_Clothes_Off([EmmaX])
            return

    if Line == "no":
            # She's refused, context based dialog
            if EmmaX.Loc == "bg teacher":
                ch_e "Я не собираюсь \"прогуливать занятия,\" [EmmaX.Petname]."
            elif EmmaX.Loc == "bg classroom":
                ch_e "Боюсь, что не могу, [EmmaX.Petname], Мне нужно закончить работу."
            elif EmmaX.Loc == "bg dangerroom":
                ch_e "Мне очень жаль, но как по-твоемо мне поддерживать себя в форме?"
            else:
                ch_e "Извини, но я сейчас слишком занята."
            hide Emma_Sprite
            call Gym_Clothes_Off([EmmaX])
            return

    elif Line == "go to":
            #You agreed to go to her instead
            #$ Party.append(EmmaX)
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")
            $ EmmaX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            hide Emma_Sprite
            $ Nearby = []
            $ Party = [EmmaX]
            call Gym_Clothes_Off([EmmaX])
            if EmmaX.Loc == "bg teacher":
                ch_e "Увидимся там."
                jump Class_Room_Entry
            elif EmmaX.Loc == "bg classroom":
                ch_e "Отлично, скрасишь мое время."
                jump Class_Room_Entry
            elif EmmaX.Loc == "bg dangerroom":
                ch_e "Я постараюсь оставить немного для тебя."
                jump Danger_Room_Entry
            elif EmmaX.Loc == "bg emma":
                ch_e "Я буду ждать."
                jump Emma_Room
            elif EmmaX.Loc == "bg player":
                ch_e "Я буду ждать."
                jump Player_Room
            elif EmmaX.Loc == "bg showerroom":
                ch_e "Я пока начну."
                jump Shower_Room_Entry
            elif EmmaX.Loc == "bg campus":
                ch_e "Хорошо."
                jump Campus_Entry
            elif EmmaX.Loc == "bg pool":
                ch_e "Хорошо."
                jump Pool_Entry
            elif EmmaX.Loc == "bg mall":
                ch_e "Хорошо, я дождусь тебя."
                jump Mall_Entry
            else:
                ch_e "Знаешь, я просто встречусь с тобой в своей комнате."
                $ EmmaX.Loc = "bg emma"
                jump Emma_Room
            #End "goto" where she's at

    #She's agreed to come over
    elif Line == "lonely":
            ch_e "Что ж, мне бы этого не хотелось. . ."
    elif Line == "command":
            ch_e "Если ты настаиваешь."
    elif Line:
            ch_e "Конечно."

    $ Line = 0
    ch_e "Полагаю, я могу остаться ненадолго."
    $ EmmaX.Loc = bg_current
    call Taboo_Level(0)
    return

# End Emma Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


## Emma's Clothes // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
label Emma_Clothes(Public=0,Bonus=0):
    if EmmaX.Taboo:
            if "exhibitionist" in EmmaX.Traits:
                ch_e "Ммммм. . ."
            elif ApprovalCheck(EmmaX, 900, TabM=4) or ApprovalCheck(EmmaX, 400, "I", TabM=3):
                ch_e "Мы сейчас не совсем в подходящем месте для этого. . ."
                return #alter to be conditional
            else:
                ch_e "Я бы предпочла обсудить это наедине."
                return
    elif ApprovalCheck(EmmaX, 900, TabM=4) or ApprovalCheck(EmmaX, 600, "L") or ApprovalCheck(EmmaX, 300, "O"):
        ch_e "Что не так с моим стилем?"
    else:
        ch_e "Я сообщу тебе, когда мне будет не наплевать на твое мнение."
        return

    if Girl != EmmaX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = EmmaX
    call Shift_Focus(Girl)

    $ Public = 0
    if "exhibitionist" in EmmaX.Traits:
            $ Public += 1
    if EmmaX.Rep <= 200:
            $ Public += 2
    elif EmmaX.Rep <= 400:
            $ Public += 1
    if "public" in EmmaX.History:
            $ Public += 2
    #This is a trait for if she's open to being sexy in public

label Emma_Wardrobe_Menu:
    $ Trigger = 1 # to prevent Focus swapping. . .
    $ EmmaX.FaceChange()
    while True:
        menu:
            ch_e "Значит, желаешь обсудить мой выбор одежды?"
            "Верх":
                        call Emma_Clothes_Over
            "Низ":
                        call Emma_Clothes_Legs
            "Нижнее белье":
                        call Emma_Clothes_Under
            "Аксессуары":
                        call Emma_Clothes_Misc
            "Управление нарядами":
                        call Emma_Clothes_Outfits
            "Давай поговорим о том, что ты носишь.":
                        call Clothes_Schedule(EmmaX)

            "Могу я посмотреть?" if EmmaX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(EmmaX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_e "Ладно, только по-быстрому. . ."
                    hide PhoneSex

            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(EmmaX,0,2)
                    if _return:
                        hide DressScreen
            "Может, тебе будет комфортнее за ширмой? (locked)" if EmmaX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if EmmaX.Loc == bg_current and not EmmaX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if not Player.Male and "girltalk" not in EmmaX.History and "nogirls" not in EmmaX.History:
                            ch_e "Я не думаю, что это будет проблемой, дорогая."
                    elif ApprovalCheck(EmmaX, 1500) or (EmmaX.SeenChest and EmmaX.SeenPussy):
                            ch_e "Ох, пожалуй, мы справимся и без нее."
                    else:
                            show DressScreen zorder 150
                            ch_e "Да, так будет лучше."

            "У меня есть подарок для тебя (locked)" if EmmaX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if EmmaX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(EmmaX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ EmmaX.OutfitChange()
                    $ EmmaX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != EmmaX:
                            ch_p "Я хочу поговорить о твоей одежде."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = EmmaX
                    call Shift_Focus(Girl)

            "Сменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current:
                    pass
            "Сменить вид" if Girl.Loc == bg_current:
                    call WardrobeView(EmmaX)
            "Неважно, ты и так хорошо выглядишь":
                    call Girl_Pos_Reset(EmmaX)
                    if "wardrobe" not in EmmaX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if EmmaX.Chat[1] <= 1:
                                    $ EmmaX.Statup("Love", 70, 15)
                                    $ EmmaX.Statup("Obed", 40, 20)
                                    ch_e "Я тоже так думаю."
                            elif EmmaX.Chat[1] <= 10:
                                    $ EmmaX.Statup("Love", 70, 5)
                                    $ EmmaX.Statup("Obed", 40, 7)
                                    ch_e "Правда?"
                            elif EmmaX.Chat[1] <= 50:
                                    $ EmmaX.Statup("Love", 70, 1)
                                    $ EmmaX.Statup("Obed", 40, 1)
                            $ EmmaX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(EmmaX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ EmmaX.OutfitChange()
                    $ EmmaX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ EmmaX.Chat[1] += 1
                    $ Trigger = 0
                    if EmmaX.Panties and "pantyless" in EmmaX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ EmmaX.DailyActions.remove("pantyless")
                    return

        #Loops back up
        #return #jump Emma_Clothes
        #End of Emma Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Emma_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(EmmaX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(EmmaX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(EmmaX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(EmmaX,4,1)
                    "Одежда для сна":
                                call OutfitShame(EmmaX,7,1)
                    "Купальник":
                                call OutfitShame(EmmaX,10,1)

                    "Повседневка 1" if ApprovalCheck(EmmaX, 2500):
                                call OutfitShame(EmmaX,11,1)
                    "Повседневка 2" if ApprovalCheck(EmmaX, 2500):
                                call OutfitShame(EmmaX,12,1)
                    "Неважно":
                                pass
        "Мне очень нравится твой костюм преподавателя.":
                $ EmmaX.OutfitChange("casual1")
                menu:
                    "Ты должна носить его. [[Выбрать текущий наряд]":
                        $ EmmaX.Outfit = "casual1"
                        $ EmmaX.Shame = 0
                        ch_e "Да, хороший выбор."
                    "Но давай попробуем что-нибудь другое.":
                        ch_e "Хорошо."

        "Эта боевая униформа очень хорошо подчеркивает твои формы.":
                $ EmmaX.OutfitChange("casual2")
                menu:
                    "Ты должна носить ее. [[Выбрать текущий наряд]":
                        $ EmmaX.Outfit = "casual2"
                        $ EmmaX.Shame = 0
                        ch_e "Буду носить ее с удовольствием."
                    "Но давай попробуем что-нибудь другое.":
                        ch_e "Хорошо."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not EmmaX.Custom1[0] and not EmmaX.Custom2[0] and not EmmaX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if EmmaX.Custom1[0] or EmmaX.Custom2[0] or EmmaX.Custom3[0]:
                $ Cnt = 0
                while 1:
                    menu:
                        "Надень Пользовательский 1 (locked)" if not EmmaX.Custom1[0]:
                                pass
                        "Надень Пользовательский 1" if EmmaX.Custom1[0]:
                                $ EmmaX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Надень Пользовательский 2 (locked)" if not EmmaX.Custom2[0]:
                                pass
                        "Надень Пользовательский 2" if EmmaX.Custom2[0]:
                                $ EmmaX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Надень Пользовательский 3 (locked)" if not EmmaX.Custom3[0]:
                                pass
                        "Надень Пользовательский 3" if EmmaX.Custom3[0]:
                                $ EmmaX.OutfitChange("custom3")
                                $ Cnt = 6

                        "Ты должна одеваться так, когда мы наедине (locked)" if not Cnt:
                                pass
                        "Ты должна одеваться так, когда мы наедине" if Cnt:
                                if Cnt == 5:
                                    $ EmmaX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ EmmaX.Clothing[9] = "custom3"
                                else:
                                    $ EmmaX.Clothing[9] = "custom1"
                                ch_e "Конечно."

                        "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                menu:
                                    "Пользовательский 1 [[очистить слот 1]" if EmmaX.Custom1[0]:
                                        ch_e "Хорошо."
                                        $ EmmaX.Custom1[0] = 0
                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not EmmaX.Custom1[0]:
                                        pass
                                    "Пользовательский 2 [[очистить слот 2]" if EmmaX.Custom2[0]:
                                        ch_e "Хорошо."
                                        $ EmmaX.Custom2[0] = 0
                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not EmmaX.Custom2[0]:
                                        pass
                                    "Пользовательский 3 [[очистить слот 3]" if EmmaX.Custom3[0]:
                                        ch_e "Хорошо."
                                        $ EmmaX.Custom3[0] = 0
                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not EmmaX.Custom3[0]:
                                        pass
                                    "Неважно [[назад]":
                                        pass

                        "Тебе следует надеть его. [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                pass
                        "Тебе следует надеть его." if Cnt:
                                call Custom_Out(EmmaX,Cnt)
                        "Ладно, вернемся к началу нашего разговора. . .":
                                $ Cnt = 0
                                return #jump Emma_Clothes

        "Наденешь спортивную одежду?" if not EmmaX.Taboo or bg_current == "bg dangerroom":
                $ EmmaX.OutfitChange("gym")


        "Наденешь одежду для сна?" if not EmmaX.Taboo:
                if ApprovalCheck(EmmaX, 1200):
                        $ EmmaX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(EmmaX)
                        if _return:
                            $ EmmaX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (EmmaX.Taboo and bg_current != "bg pool" and not ApprovalCheck(EmmaX, 800, TabM=2)) or not EmmaX.Swim[0]:
                $ EmmaX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not EmmaX.Taboo or bg_current == "bg pool" or ApprovalCheck(EmmaX, 800, TabM=2)) and EmmaX.Swim[0]:
                $ EmmaX.OutfitChange("swimwear")

        "Наденешь хэллоуинский костюм?" if "halloween" in EmmaX.History:
                ch_e "Хорошо. . ."
                $ EmmaX.OutfitChange("costume")

        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ EmmaX.FaceChange("sly", 1)
                $ Line = 0
                if not EmmaX.Chest and not EmmaX.Panties and not EmmaX.Over and not EmmaX.Legs and not EmmaX.Hose:
                    # if already naked (yes)
                    ch_e "Пожалуй. . ."
                elif EmmaX.SeenChest and EmmaX.SeenPussy and ApprovalCheck(EmmaX, 1200, TabM=(5-Public)):
                    #if you've seen it all and she likes you well enough (yes)
                    ch_e "Приму это за приглашение. . ."
                    $ Line = 1
                elif ApprovalCheck(EmmaX, 2000, TabM=(5-Public)):
                    #if you haven't seen everything but she really likes you (yes)
                    if not Player.Male:
                        ch_e "Полагаю, ты это заслужила. . ."
                    else:
                        ch_e "Полагаю, ты это заслужил. . ."
                    $ Line = 1
                elif EmmaX.SeenChest and EmmaX.SeenPussy and ApprovalCheck(EmmaX, 1200, TabM=0):
                    # if you've seen it but it's in public (no)
                    ch_e "Мы сейчас не в подходящем месте. . ."
                elif ApprovalCheck(EmmaX, 2000, TabM=0):
                    #if you haven't seen everything but she really likes you and it's public (no)
                    ch_e "Так оно и есть, но мы сейчас не в подходящем месте. . ."
                elif ApprovalCheck(EmmaX, 1000, TabM=0):
                    #if you haven't seen everything and she kinda likes you but it's public (no)
                    $ EmmaX.FaceChange("surprised", 1)
                    ch_e "Так оно и есть, но мне не нравится к чему ты клонишь."
                    $ EmmaX.Blush = 0
                else:
                    # if she refuses. (no)
                    $ EmmaX.FaceChange("angry", 1)
                    ch_e "Не самое худшее предложение, которое я слышала."
                    ch_e ". . . но очень близкое к нему."

                call expression EmmaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in EmmaX.History:
                        $ Line = 0
                if Line:                                                            #If she got nude. . .
                    $ EmmaX.OutfitChange("nude")
                    "Она раздевается."
                    call Girl_First_Topless(EmmaX)
                    call Girl_First_Bottomless(EmmaX,1)
                    $ EmmaX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется, что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in EmmaX.Traits:
                                $ EmmaX.FaceChange("sexy",2,Eyes="down")
                                ch_e "Ммммм. . ."
                                $ EmmaX.Outfit = "nude"
                                $ EmmaX.Statup("Lust", 50, 10)
                                $ EmmaX.Statup("Lust", 70, 5)
                                $ EmmaX.Shame = 50
                                $ EmmaX.FaceChange("sexy",1)
                            elif ApprovalCheck(EmmaX, 800, "I") or ApprovalCheck(EmmaX, 2800, TabM=0):
                                ch_e "Ооох, это вызовет настоящий переполох. . ."
                                $ EmmaX.Outfit = "nude"
                                $ EmmaX.Shame = 50
                            elif ApprovalCheck(EmmaX, 400, "I") and ApprovalCheck(EmmaX, 1200, TabM=0):
                                $ EmmaX.FaceChange("bemused", 1,Eyes="side")
                                ch_e "Тебе не стоит предлагать такое. . ."
                            else:
                                $ EmmaX.FaceChange("sexy", 1,Eyes="surprised")
                                ch_e "Это невозможно."

                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in EmmaX.Traits:
                                ch_e "Для тебя это слишком?"
                            elif ApprovalCheck(EmmaX, 800, "I") or ApprovalCheck(EmmaX, 2800, TabM=0):
                                $ EmmaX.FaceChange("bemused", 1)
                                ch_e "Конечно, ведь очевидно, я не могу расхаживать в таком виде. . ."
                            else:
                                $ EmmaX.FaceChange("confused", 1)
                                ch_e "Пока мы только вдвоем, я не возражаю."
                $ Line = 0

        "Неважно":
            return #jump Emma_Clothes

    return #jump Emma_Clothes
    #End of Emma Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Emma_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять [get_clothing_name(EmmaX.Over_key, vin)]?" if EmmaX.Over:
                call Wardrobe_Remove(EmmaX)

        "Примерь свой белый пиджак." if EmmaX.Over != "jacket":
                $ EmmaX.FaceChange("bemused")
                if EmmaX.Chest or EmmaX.SeenChest or ApprovalCheck(EmmaX, 500, TabM=(3-Public)):
                    ch_e "Ладно."
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            $ EmmaX.FaceChange("bemused", 1)
                            ch_e "Не думаю, что его стоит надевать без лифчика."
                            return #jump Emma_Clothes
                $ EmmaX.Over = "jacket"

        "Примерь белое платье." if EmmaX.Over != "dress" and "halloween" in EmmaX.History:
                $ EmmaX.FaceChange("bemused")
                if EmmaX.Chest or EmmaX.SeenChest or ApprovalCheck(EmmaX, 500, TabM=(3-Public)):
                    ch_e "Ладно."
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            $ EmmaX.FaceChange("bemused", 1)
                            ch_e "Не думаю, что его стоит надевать без лифчика."
                            return #jump Emma_Clothes
                menu:
                    ch_e "Полностью или только верхнюю часть?"
                    "Полностью.":
                            $ EmmaX.Legs = "dress"
                    "Только верхнюю часть.":
                            pass
                $ EmmaX.Over = "dress"

        "Примерь кружевную ночнушку." if EmmaX.Over != "nighty":
                $ EmmaX.FaceChange("bemused")
                if EmmaX.Chest or EmmaX.SeenChest or ApprovalCheck(EmmaX, 500, TabM=(3-Public)):
                    ch_e "Ладно."
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            $ EmmaX.FaceChange("bemused", 1)
                            ch_e "Она слишком прозрачная."
                            return #jump Emma_Clothes
                $ EmmaX.Over = "nighty"

        "Может, просто накинешь полотенце?" if EmmaX.Over != "towel":
                $ EmmaX.FaceChange("bemused", 1)
                $ Bonus = 5 if bg_current == "bg showerroom" else 0
                if EmmaX.Chest or (EmmaX.SeenChest and ApprovalCheck(EmmaX, 500, TabM=(3-Public-Bonus))):
                    ch_e "Ох, значит, тебе такое нравится?"
                elif ApprovalCheck(EmmaX, 1000, TabM=(3-Public-Bonus)):
                    $ EmmaX.FaceChange("perplexed", 1)
                    ch_e "Хорошо."
                else:
                    call Display_DressScreen(EmmaX)
                    if not _return:
                            $ EmmaX.FaceChange("bemused", 1)
                            ch_e "С ним не остается места для воображения."
                            return #jump Emma_Clothes
                call Emma_NoBra
                if not _return:
                    return #jump Emma_Clothes
                $ EmmaX.Over = "towel"

        "Неважно":
                pass
    return #jump Emma_Clothes
    #End of Emma Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Emma_NoBra: #fix test this
        menu:
            ch_e "На мне нет лифчика. . ."
            "Тогда надень какой-нибудь. . .":
                        if (EmmaX.SeenChest and ApprovalCheck(EmmaX, 1000, TabM=(4-Public))) or ApprovalCheck(EmmaX, 1200, TabM=(5-Public)):
                                ch_e "-не то, чтобы меня это сильно волновало. . ."
                        elif ApprovalCheck(EmmaX, 900, TabM=(3-Public)) and "lace bra" in EmmaX.Inventory:
                                ch_e "Пожалуй, можно."
                                $ EmmaX.Chest  = "lace bra"
                                "Она достает свой кружевной лифчик и надевает его под [get_clothing_name(EmmaX.Over_key, vin)]."
#                        elif ApprovalCheck(EmmaX, 800, TabM=(3-Public)):
#                                ch_e "I suppose I could."
#                                $ EmmaX.Chest = "bra"
#                                "She pulls out her bra and slips it on under her [EmmaX.Over]."
                        elif ApprovalCheck(EmmaX, 700, TabM=(3-Public)):
                                ch_e "Пожалуй, можно."
                                $ EmmaX.Chest = "corset"
                                "Она достает свой корсет и надевает его под [get_clothing_name(EmmaX.Over_key, vin)]."
                        elif ApprovalCheck(EmmaX, 600, TabM=(3-Public)):
                                ch_e "I suppose I could."
                                $ EmmaX.Chest = "sports bra"
                                "Она достает свой спортивный лифчик и надевает его под [get_clothing_name(EmmaX.Over_key, vin)]."
                        else:
                                ch_e "Да, но я бы предпочла этого не делать."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(EmmaX, 1100, "LI", TabM=(3-Public)) and EmmaX.Love > EmmaX.Inbt:
                                ch_e "Для тебя все что угодно. . ."
                        elif ApprovalCheck(EmmaX, 700, "OI", TabM=(3-Public)) and EmmaX.Obed > EmmaX.Inbt:
                                ch_e "Если ты настаиваешь. . ."
                        elif ApprovalCheck(EmmaX, 600, "I", TabM=(3-Public)):
                                ch_e "Пожалуй, можно. . ."
                        elif ApprovalCheck(EmmaX, 1300, TabM=(3-Public)):
                                ch_e "Хорошо."
                        else:
                                $ EmmaX.FaceChange("surprised")
                                $ EmmaX.Brows = "angry"
                                if EmmaX.Taboo > 20:
                                    ch_e "Боюсь, я не смогу сделать это на людях."
                                else:
                                    ch_e "Я бы могла, но не стану."
                                call expression EmmaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0


            "Неважно.":
                        return 0
        return 1
        #End of Emma bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Emma_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(EmmaX.Legs_key, vin)]?" if EmmaX.Legs:
                call Wardrobe_Remove(EmmaX,1)

        "Тебе идут твои белые брюки." if EmmaX.Legs != "pants":
                ch_e "Я знаю."
                $ EmmaX.Legs = "pants"

        "Тебе идет твоя юбочка." if EmmaX.Legs != "skirt":
                ch_e "Согласна."
                $ EmmaX.Legs = "skirt"

        "Примерь свое белое платье." if EmmaX.Legs != "dress" and "halloween" in EmmaX.History:
                $ EmmaX.FaceChange("bemused")
                menu:
                    ch_e "Полностью или только юбку?"
                    "Полностью.":
                            $ EmmaX.Over = "dress"
                    "Только юбку.":
                            pass
                $ EmmaX.Legs = "dress"

        "Тебе очень идут эти штанах для йоги." if EmmaX.Legs != "yoga pants":
                ch_e "Ладно."
                $ EmmaX.Legs = "yoga pants"

        "Сними обувь (locked)" if not EmmaX.Boots:
                pass
        "Сними [get_clothing_name(EmmaX.Boots_key, vin)]" if EmmaX.Boots:
                ch_p "Может, снимешь [get_clothing_name(EmmaX.Boots_key, vin)]?"
                ch_e "Пожалуй, можно."
                $ EmmaX.Boots = 0
        "Ты отлично выглядишь в сапожках." if EmmaX.Boots != "thigh boots":
                ch_e "Согласна, они мне очень идут."
                $ EmmaX.Boots = "thigh boots"
        "Ты отлично выглядишь в туфлях." if EmmaX.Boots != "shoes":
                ch_e "Согласна, они мне очень идут."
                $ EmmaX.Boots = "shoes"

        "Неважно":
                pass
    return #jump Emma_Clothes
    #End of Emma Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Emma_NoPantiesOn: #fix test this
        $ EmmaX.FaceChange("sexy",Eyes="side")
        ch_e "Ты следует знать. . ."
        $ EmmaX.FaceChange("sly")
        menu:
            ch_e "Сейчас на мне нет трусиков. . ."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if (EmmaX.SeenPussy and ApprovalCheck(EmmaX, 1100, TabM=(5-Public))) or ApprovalCheck(EmmaX, 1500, TabM=(5-Public)):
                                $ EmmaX.Blush = 1
                                ch_e "Я не говорила, что меня это беспокоит. . ."
                                $ EmmaX.Blush = 0
                        elif ApprovalCheck(EmmaX, 700, TabM=5):
                                ch_e "Полагаю, можно. . ."
                                if "lace panties" in EmmaX.Inventory:
                                        $ EmmaX.Panties  = "lace panties"
                                else:
                                        $ EmmaX.Panties = "white panties"
                                if ApprovalCheck(EmmaX, 1200, TabM=4):
                                    $ Line = get_clothing_name(EmmaX.Legs_key, vin)
                                    $ EmmaX.Legs = 0
                                    "Она снимает [Line] и натягивает [get_clothing_name(EmmaX.Panties_key, vin)]."
                                elif EmmaX.Legs == "skirt":
                                    "Она достает свои [get_clothing_name(EmmaX.Panties_key, vin)] и натягивает их под юбку."
                                    $ EmmaX.Legs = 0
                                    "Затем она сбрасывает юбку на пол."
                                else:
                                    $ Line = EmmaX.Legs
                                    $ EmmaX.Legs = 0
                                    "Она отходит на мгновение, а затем возвращается в [get_clothing_name(EmmaX.Panties_key, pre)]."
                                return #jump Emma_Clothes
                        elif EmmaX.Taboo and ApprovalCheck(EmmaX, 800, TabM=0):
                                ch_e "Мне нравится ход твоих мыслей, но давай не на людях."
                                return 0
                        else:
                                ch_e "Я бы предпочла этого не делать."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(EmmaX, 1100, "LI", TabM=(5-Public)) and EmmaX.Love > EmmaX.Inbt:
                                ch_e "Пожалуй, соглашусь. . ."
                        elif ApprovalCheck(EmmaX, 700, "OI", TabM=(5-Public)) and EmmaX.Obed > EmmaX.Inbt:
                                ch_e "Если тебя это устраивает. . ."
                        elif ApprovalCheck(EmmaX, 600, "I", TabM=(5-Public)):
                                ch_e "Возможно. . ."
                        elif ApprovalCheck(EmmaX, 1300, TabM=(5-Public)):
                                ch_e "Я тебя поняла."
                        else:
                                $ EmmaX.FaceChange("surprised")
                                $ EmmaX.Brows = "angry"
                                if EmmaX.Taboo > 20:
                                    ch_e "Возможно, но точно не здесь, [EmmaX.Petname]!"
                                else:
                                    ch_e "Не сомневаюсь, что тебя это устраивает, [EmmaX.Petname]!"
                                call expression EmmaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно.":
                ch_e "Ладно. . ."
                return 0
        return 1
        #End of Emma Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Emma_Clothes_Under:
        "Верх":
            menu:
                "Может, снимешь [get_clothing_name(EmmaX.Chest_key, vin)]?" if EmmaX.Chest:
                    $ EmmaX.FaceChange("bemused", 1)
                    if EmmaX.SeenChest and ApprovalCheck(EmmaX, 900, TabM=(4-Public)):
                        ch_e "Конечно."
                    elif ApprovalCheck(EmmaX, 1100, TabM=2):
                        if EmmaX.Taboo:
                            ch_e "Не здесь. . ."
                        else:
                            ch_e "Только для тебя. . ."
                    elif EmmaX.Over == "jacket" and ApprovalCheck(EmmaX, 700, TabM=(3-Public)):
                        ch_e "Это немного дерзко, пиджак да на голое тело. . ."
                    elif not EmmaX.Over:
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "Не думаю, что это уместно."
                            return #jump Emma_Clothes
                    else:
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "Боюсь, что не могу, [EmmaX.Petname]."
                            return #jump Emma_Clothes
                    $ Line = get_clothing_name(EmmaX.Chest_key, vin)
                    $ EmmaX.Chest = 0
                    if EmmaX.Over:
                        "Она залезает под [get_clothing_name(EmmaX.Over_key, vin)], хватает [Line] и вытаскивает, роняя на пол."
                    else:
                        "Она скидывает [Line] на пол."
                        if not renpy.showing('DressScreen'):
                            call Girl_First_Topless(EmmaX)

                "Мне нравится твой корсет." if EmmaX.Chest != "corset":
                    if EmmaX.SeenChest or ApprovalCheck(EmmaX, 1000, TabM=(3-Public)):
                        ch_e "Мне тоже."
                        $ EmmaX.Chest = "corset"
                        $ EmmaX.TitsUp = 1
                    else:
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "Не думаю, что уместно сейчас его надевать. . ."
                        else:
                            $ EmmaX.Chest = "corset"

                "Мне нравится твой кружевной лифчик." if "lace bra" in EmmaX.Inventory and EmmaX.Chest != "lace bra":
                    if EmmaX.SeenChest or ApprovalCheck(EmmaX, 1300, TabM=(3-Public)):
                        ch_e "Хорошо."
                        $ EmmaX.Chest = "lace bra"
                    else:
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "Он слегка откровенный. . ."
                        else:
                            $ EmmaX.Chest = "lace bra"

                "Мне нравится этот спортивный лифчик." if EmmaX.Chest != "sports bra":
                    if EmmaX.SeenChest or ApprovalCheck(EmmaX, 1000, TabM=(3-Public)):
                        ch_e "Хорошо."
                        $ EmmaX.Chest = "sports bra"
                    else:
                        call Display_DressScreen(EmmaX)
                        if not _return:
                            ch_e "Я не уверена на его счет. . ."
                        else:
                            $ EmmaX.Chest = "sports bra"

                "Мне нравится твой лифчик бикини." if EmmaX.Chest != "bikini top" and "bikini top" in EmmaX.Inventory:
                    if bg_current == "bg pool":
                            ch_e "Хорошо."
                            $ EmmaX.Chest = "bikini top"
                    else:
                            if EmmaX.SeenChest or ApprovalCheck(EmmaX, 800, TabM=2):
                                ch_e "Хорошо."
                                $ EmmaX.Chest = "bikini top"
                            else:
                                call Display_DressScreen(EmmaX)
                                if not _return:
                                    ch_e "Я не уверена, стоит ли надевать его здесь. . ."
                                else:
                                    $ EmmaX.Chest = "bikini top"
                "Неважно":
                    pass
            return #jump Emma_Clothes_Under


        "Варианты колготок и чулок":
            menu:
                "Сними [get_clothing_name(EmmaX.Hose_key, vin)]." if EmmaX.Hose:
                                $ EmmaX.Hose = 0
                "Чулки дополнили бы твой образ." if EmmaX.Hose != "stockings" and "stockings and garterbelt" in EmmaX.Inventory:
                                $ EmmaX.Hose = "stockings"
                "Колготки дополнили бы твой образ." if EmmaX.Hose != "pantyhose" and "pantyhose" in EmmaX.Inventory:
                                $ EmmaX.Hose = "pantyhose"
                "Рваные колготки дополнили бы твой образ." if EmmaX.Hose != "ripped pantyhose" and "ripped pantyhose" in EmmaX.Inventory:
                                $ EmmaX.Hose = "ripped pantyhose"
                "Чулки и пояс с подвязками дополнили бы твой образ." if EmmaX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in EmmaX.Inventory:
                                $ EmmaX.Hose = "stockings and garterbelt"
                "Может, наденешь только пояс с подвязками?" if EmmaX.Hose != "garterbelt" and "stockings and garterbelt" in EmmaX.Inventory:
                                $ EmmaX.Hose = "garterbelt"
                "Неважно":
                        pass
            return #jump Emma_Clothes_Under

        #Panties
        "Низ":
            menu:
                "Ты должна снять [get_clothing_name(EmmaX.Panties_key, vin)]. . ." if EmmaX.Panties:
                        $ EmmaX.FaceChange("bemused", 1)
                        if (ApprovalCheck(EmmaX, 900) or EmmaX.SeenPussy) and not EmmaX.Taboo:
                            #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public

                            if ApprovalCheck(EmmaX, 850, "L"):
                                    ch_e "Нравится вид?"
                            elif ApprovalCheck(EmmaX, 500, "O"):
                                    ch_e "Если ты этого хочешь."
                            elif ApprovalCheck(EmmaX, 350, "I"):
                                    ch_e "По правде говоря, мне нравится ходить без них. . ."
                            else:
                                    ch_e "Хорошо."
                        else:
                            #low approval or not wearing pants or in public
                            if ApprovalCheck(EmmaX, 1100, "LI", TabM=(4-Public)) and EmmaX.Love > EmmaX.Inbt:
                                    ch_e "Я не возражаю, если ты посмотришь. . ."
                            elif ApprovalCheck(EmmaX, 700, "OI", TabM=(4-Public)) and EmmaX.Obed > EmmaX.Inbt:
                                    ch_e "Пожалуй, можно. . ."
                            elif ApprovalCheck(EmmaX, 600, "I", TabM=(4-Public)):
                                    ch_e "Почему нет."
                            elif ApprovalCheck(EmmaX, 1300, TabM=(4-Public)):
                                    ch_e "Хорошо."
                            else:
                                call Display_DressScreen(EmmaX)
                                if not _return:
                                    $ EmmaX.FaceChange("surprised")
                                    $ EmmaX.Brows = "angry"
                                    if EmmaX.Taboo > 20:
                                        ch_e "Я не уверена, что смогу снять их здесь, [EmmaX.Petname]!"
                                    else:
                                        ch_e "Я могла бы, но не буду, [EmmaX.Petname]!"
                                    return #jump Emma_Clothes
                        $ Line = get_clothing_name(EmmaX.Panties_key, vin)
                        $ EmmaX.Panties = 0
                        if not EmmaX.Legs:
                            "Она снимает [Line] и бросает их на пол."
                            if not renpy.showing('DressScreen'):
                                    call Girl_First_Bottomless(EmmaX)
                        elif ApprovalCheck(EmmaX, 1200, TabM=4):
                            $ Trigger = EmmaX.Legs
                            $ EmmaX.Legs = 0
                            pause 0.5
                            $ EmmaX.Legs = Trigger
                            "Она снимает [get_clothing_name(EmmaX.Legs_key, vin)] и [Line], затем снова надевает [get_clothing_name(EmmaX.Legs_key, vin)]."
                            $ Trigger = 1
                            call Girl_First_Bottomless(EmmaX,1)
                        elif EmmaX.Legs == "skirt":
                            "Она залезает под юбку и стягивает [Line]."
                        else:
                            $ EmmaX.Blush = 1
                            "Она отходит на мгновение, а затем возвращается обратно."
                            $ EmmaX.Blush = 0
                        $ Line = 0

                "Почему бы тебе вместо этих не надеть белые трусики?" if EmmaX.Panties and EmmaX.Panties != "white panties":
                        if ApprovalCheck(EmmaX, 1100, TabM=(4-Public)):
                                ch_e "Ладно."
                                $ EmmaX.Panties = "white panties"
                        else:
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                ch_e "Я не совсем понимаю, каким боком тебя это вообще касается."
                            else:
                                $ EmmaX.Panties = "white panties"

                "Почему бы тебе вместо этих не надеть спортивные трусики?" if EmmaX.Panties and EmmaX.Panties != "sports panties":
                        if ApprovalCheck(EmmaX, 1200, TabM=(4-Public)):
                                ch_e "Хорошо."
                                $ EmmaX.Panties = "sports panties"
                        else:
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                ch_e "Я не совсем понимаю, каким боком тебя это вообще касается."
                            else:
                                $ EmmaX.Panties = "sports panties"

                "Почему бы тебе вместо этих не надеть кружевные трусики?" if "lace panties" in EmmaX.Inventory and EmmaX.Panties and EmmaX.Panties != "lace panties":
                        if ApprovalCheck(EmmaX, 1300, TabM=(4-Public)):
                                ch_e "Хорошо."
                                $ EmmaX.Panties = "lace panties"
                        else:
                            call Display_DressScreen(EmmaX)
                            if not _return:
                                ch_e "Я не совсем понимаю, каким боком тебя это вообще касается."
                            else:
                                $ EmmaX.Panties = "lace panties"

                "Мне нравятся твои трусики бикини." if EmmaX.Panties != "bikini bottoms" and "bikini bottoms" in EmmaX.Inventory:
                        if bg_current == "bg pool":
                                ch_e "Хорошо."
                                $ EmmaX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(EmmaX, 800, TabM=2):
                                    ch_e "Хорошо."
                                    $ EmmaX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(EmmaX)
                                    if not _return:
                                        ch_e "Я не уверена, стоит ли надевать их здесь. . ."
                                    else:
                                        $ EmmaX.Panties = "bikini bottoms"

                "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not EmmaX.Panties:
                        $ EmmaX.FaceChange("bemused", 1)
                        if EmmaX.Legs and (EmmaX.Love+EmmaX.Obed) <= (2* EmmaX.Inbt):
                            $ EmmaX.Mouth = "smile"
                            ch_e "Я -могла- бы, но не буду."
                            menu:
                                "Ну ладно.":
                                    return #jump Emma_Clothes
                                "Я настаиваю, надевай.":
                                    if (EmmaX.Love+EmmaX.Obed) <= EmmaX.Inbt:
                                        $ EmmaX.FaceChange("angry", Eyes="side")
                                        ch_e "Я же сказала, что не надену, уймись."
                                        return #jump Emma_Clothes
                                    else:
                                        $ EmmaX.FaceChange("sadside")
                                        ch_e "Если ты настаиваешь."
                        menu:
                            ch_e "Если ты настаиваешь. . ."
                            "Как насчет белых?":
                                ch_e "Хорошо."
                                $ EmmaX.Panties = "white panties"
                            "Как насчет спортивных?":
                                ch_e "Хорошо."
                                $ EmmaX.Panties = "sports panties"
                            "Как насчет кружевных?" if "lace panties" in EmmaX.Inventory:
                                ch_e "Хорошо."
                                $ EmmaX.Panties  = "lace panties"
                "Неважно":
                    pass
            return #jump Emma_Clothes_Under
        "Неважно":
            pass
    return #jump Emma_Clothes
    #End of Emma Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Emma_Clothes_Misc:
        #Misc
        "Тебе идет пышная прическа." if EmmaX.Hair != "long":
                if ApprovalCheck(EmmaX, 600):
                    $ EmmaX.Hair = "long"
                    ch_e "Так?"
                else:
                    ch_e "Да, это так."

        "Думаю, тебе стоит ходить с прямыми волосам." if EmmaX.Hair != "wet":
                if ApprovalCheck(EmmaX, 600):
                    $ EmmaX.Hair = "wet"
                    ch_e "Думаешь?"
                else:
                    ch_e "Я предпочитаю, чтобы они были слегка распущены."

        "Тебе идет короткая стрижка." if EmmaX.Hair != "short":
                if ApprovalCheck(EmmaX, 600):
                    $ EmmaX.Hair = "short"
                    ch_e "Так?"
                else:
                    ch_e "Да, это так."

        "Надень шляпу" if not EmmaX.Hat and "halloween" in EmmaX.History:
                ch_p "Шляпа, которую ты надевала на вечеринку, была милой."
                $ EmmaX.Hat = "sun hat"
        "Сними шляпу" if EmmaX.Hat:
                ch_p "Думаю, тебе следует снять шляпу."
                $ EmmaX.Hat = 0

        "Отрасти волосы на лобке." if not EmmaX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может отрастишь?"
                call expression EmmaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in EmmaX.Todo:
                    $ EmmaX.FaceChange("bemused", 1)
                    ch_e "Что ж, построили Рим не за один день. . ."
                else:
                    $ EmmaX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(EmmaX, 1150, TabM=0)
                    if ApprovalCheck(EmmaX, 850, "L", TabM=0) or (Approval and EmmaX.Love > 2 * EmmaX.Obed):
                        ch_e "Ну, если тебе такое нравится. . ."
                    elif ApprovalCheck(EmmaX, 500, "I", TabM=0) or (Approval and EmmaX.Inbt > EmmaX.Obed):
                        ch_e "Я могу стать немного более. . . неопрятной."
                    elif ApprovalCheck(EmmaX, 400, "O", TabM=0) or Approval:
                        ch_e "Если ты настаиваешь. . ."
                    else:
                        $ EmmaX.FaceChange("surprised")
                        $ EmmaX.Brows = "angry"
                        ch_e "Полагаю, тебя это не касается, [EmmaX.Petname]."
                        return #jump Emma_Clothes
                    $ EmmaX.Todo.append("pubes")
                    $ EmmaX.PubeC = 6

        "Побрей лобок" if EmmaX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression EmmaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ EmmaX.FaceChange("bemused", 1)
                if "shave" in EmmaX.Todo:
                    ch_e "Да, да, это уже в моих планах."
                else:
                    $ Approval = ApprovalCheck(EmmaX, 1150, TabM=0)

                    if ApprovalCheck(EmmaX, 850, "L", TabM=0) or (Approval and EmmaX.Love > 2 * EmmaX.Obed):
                        ch_e "Я знаю, что тебе это нравится."
                    elif ApprovalCheck(EmmaX, 500, "I", TabM=0) or (Approval and EmmaX.Inbt > EmmaX.Obed):
                        ch_e "Мне нравится, когда все аккуратно."
                    elif ApprovalCheck(EmmaX, 400, "O", TabM=0) or Approval:
                        ch_e "Если ты настаиваешь."
                    else:
                        $ EmmaX.FaceChange("surprised")
                        $ EmmaX.Brows = "angry"
                        ch_e "Полагаю, тебя это не касается, [EmmaX.Petname]."
                        return #jump Emma_Clothes
                    $ EmmaX.Todo.append("shave")
        "Пирсинг. [[Сначала посмотрите, как она выглядит без него] (locked)" if not EmmaX.SeenPussy and not EmmaX.SeenChest:
                pass

        "Надень пирсинг-кольца" if EmmaX.Pierce != "ring" and (EmmaX.SeenPussy or EmmaX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсингом-кольцами."
                if "ring" in EmmaX.Todo:
                        ch_e "Да, да, это уже в моих планах."
                else:
                        $ EmmaX.FaceChange("bemused", 1)
                        $ Approval = ApprovalCheck(EmmaX, 1350, TabM=0)
                        if ApprovalCheck(EmmaX, 900, "L", TabM=0) or (Approval and EmmaX.Love > 2* EmmaX.Obed):
                                ch_e "Полагаю, чтобы было за что ухватиться?"
                        elif ApprovalCheck(EmmaX, 600, "I", TabM=0) or (Approval and EmmaX.Inbt > EmmaX.Obed):
                                ch_e "Мне нравятся красивые колечки. . ."
                        elif ApprovalCheck(EmmaX, 500, "O", TabM=0) or Approval:
                                ch_e "Я не знала, что тебе нравится такое."
                        else:
                                $ EmmaX.FaceChange("surprised")
                                $ EmmaX.Brows = "angry"
                                ch_e "К такому я не готова, [EmmaX.Petname]."
                                return #jump Emma_Clothes
                        $ EmmaX.Todo.append("ring")

        "Надень пирсинг-штанги." if EmmaX.Pierce != "barbell" and (EmmaX.SeenPussy or EmmaX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in EmmaX.Todo:
                        ch_e "Да, да, это уже в моих планах."
                else:
                        $ EmmaX.FaceChange("bemused", 1)
                        $ Approval = ApprovalCheck(EmmaX, 1350, TabM=0)
                        if ApprovalCheck(EmmaX, 900, "L", TabM=0) or (Approval and EmmaX.Love > 2 * EmmaX.Obed):
                            ch_e "Полагаю, чтобы было за что ухватиться?"
                        elif ApprovalCheck(EmmaX, 600, "I", TabM=0) or (Approval and EmmaX.Inbt > EmmaX.Obed):
                            ch_e "Они будут хорошо смотреться на этих малышках. . ."
                        elif ApprovalCheck(EmmaX, 500, "O", TabM=0) or Approval:
                            ch_e "Я не знала, что тебе нравится такое."
                        else:
                            $ EmmaX.FaceChange("surprised")
                            $ EmmaX.Brows = "angry"
                            ch_e "К такому я не готова, [EmmaX.Petname]."
                            return #jump Emma_Clothes
                        $ EmmaX.Todo.append("barbell")

        "Сними пирсинг" if EmmaX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ EmmaX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(EmmaX, 1350, TabM=0)
                if ApprovalCheck(EmmaX, 950, "L", TabM=0) or (Approval and EmmaX.Love > EmmaX.Obed):
                    ch_e "Что ж, если тебе не нравится. . ."
                elif ApprovalCheck(EmmaX, 700, "I", TabM=0) or (Approval and EmmaX.Inbt > EmmaX.Obed):
                    ch_e "Он мне никогда не нравился."
                elif ApprovalCheck(EmmaX, 600, "O", TabM=0) or Approval:
                    ch_e "Тогда я сниму его."
                else:
                    $ EmmaX.FaceChange("surprised")
                    $ EmmaX.Brows = "angry"
                    ch_e "Что ж, а {i}мне{/i} он нравятся."
                    return #jump Emma_Clothes
                $ EmmaX.Pierce = 0

        "Надень чокер" if EmmaX.Neck != "choker":
                ch_p "Почему бы тебе не примерить свой белый чокер?"
                ch_e "Ладно. . ."
                $ EmmaX.Neck = "choker"
        "Сними чокер" if EmmaX.Neck:
                ch_p "Давай без чокера."
                ch_e "Ладно. . ."
                $ EmmaX.Neck = 0

        "Может, снимешь перчатки?" if EmmaX.Arms:
                $ EmmaX.Arms = 0
                ch_e "Ладно."
        "Надень перчатки." if not EmmaX.Arms:
                $ EmmaX.Arms = "gloves"
                ch_e "Ладно."
        "Неважно":
                pass
    return #jump Emma_Clothes
    #End of Emma Misc Wardrobe

return
#End Emma Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
