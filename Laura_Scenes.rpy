
# start LauraMeet//////////////////////////////////////////////////////////

label LauraMeet(Topics=[],Loop=1):
    $ ActiveGirls.append(LauraX) if LauraX not in ActiveGirls else ActiveGirls
    $ LauraX.Name = "???"
    $ LauraX.Name_rod = "???"
    $ LauraX.Name_dat = "???"
    $ LauraX.Name_vin = "???"
    $ LauraX.Name_tvo = "???"
    $ LauraX.Name_pre = "???"
    $ LauraX.Names.remove("Laura")
    $ LauraX.Names.append("X-23")
    $ bg_current = "bg dangerroom"
    call CleartheRoom("All",0,1)
    $ LauraX.Loc = "bg dangerroom"
    $ LauraX.Love = 400
    $ LauraX.Obed = 0
    $ LauraX.Inbt = 200
    $ LauraX.Lust = 10
    call Shift_Focus(LauraX)
    $ LauraX.SpriteLoc = StageCenter
    call Set_The_Scene(0)
    $ LauraX.Petname = Player.Name
    $ LauraX.Petname_rod = Player.Name_rod
    $ LauraX.Petname_dat = Player.Name_dat
    $ LauraX.Petname_vin = Player.Name_vin
    $ LauraX.Petname_tvo = Player.Name_tvo
    $ LauraX.Petname_pre = Player.Name_pre
    $ LauraX.OutfitDay = "casual1"
    $ LauraX.Outfit = "casual1"
    $ LauraX.OutfitChange("casual1")
    $ Player.AddWord(1,0,"Intro",0,0) #adds tag to Daily

    "Вы подходите к комнате Опасности и слышите свирепый лязг металла."
    "Как только вы проходите через дверь, роборука бьет вас по лицу."
    ". . ."
    $ LauraX.FaceChange("normal", 0)
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc)
    "Когда вы приходите в себя, вы видите, что какая-то девушка держит вас за руку."
    $ LauraX.FaceChange("surprised", 0, Eyes="squint",Brows="sad")
    if not Player.Male:
        ch_u "О, хорошо, похоже, ты не сильно пострадала."
    else:
        ch_u "О, хорошо, похоже, ты не сильно пострадал."
    $ LauraX.FaceChange("smile", 0, Brows="sad")
    ch_u "Извини, я тренировалась и, видимо, забыла запереть дверь."
    $ LauraX.FaceChange("smile", 0)
    while Loop:
        menu:
            extend ""
            "Кто ты?" if LauraX.Name == "???":
                    $ LauraX.FaceChange("normal", 0)
                    ch_l "Можешь звать меня \"Икс-23\"."
                    $ LauraX.Name = "Икс-23"
                    $ LauraX.Name_rod = "Икс-23"
                    $ LauraX.Name_dat = "Икс-23"
                    $ LauraX.Name_vin = "Икс-23"
                    $ LauraX.Name_tvo = "Икс-23"
                    $ LauraX.Name_pre = "Икс-23"
            "Икс-23? Это твое настоящее имя?" if LauraX.Name == "Икс-23" and "X23" not in Topics:
                    $ LauraX.FaceChange("confused", 0)
                    ch_l "Так меня назвали при рождении."
                    $ Topics.append("X23")
            "Я могу еще как-нибудь звать тебя?" if "X23" in Topics and LauraX not in Topics:
                    $ LauraX.Statup("Love", 70, 5) # Love
                    $ LauraX.FaceChange("normal", 0)
                    ch_l "Меня также зовут Лора. Лора Кинни."
                    $ LauraX.FaceChange("confused", 0, Mouth="normal")
                    $ LauraX.Name = "Лора"
                    $ LauraX.Name_rod = "Лоры"
                    $ LauraX.Name_dat = "Лоре"
                    $ LauraX.Name_vin = "Лору"
                    $ LauraX.Name_tvo = "Лорой"
                    $ LauraX.Name_pre = "Лоре"
                    $ LauraX.Names.append("Laura")
                    $ Topics.append(LauraX)
                    menu:
                        extend ""
                        "Приятно познакомиться, Лора.":
                            $ LauraX.Statup("Love", 70, 5) # Love
                            $ LauraX.FaceChange("normal", 0)
                            ch_l "Ага."
                        "Приятно познакомиться, Лора Лора Кинни.":
                            $ LauraX.FaceChange("confused", 0,Mouth="sucking")
                            ch_l "Это просто-"
                            $ LauraX.FaceChange("smile", 0,Brows="surprised")
                            $ LauraX.Statup("Love", 70, 3) # Love
                            $ LauraX.Statup("Inbt", 70, 2) # Inbt
                            ch_l "О, я поняла."
                        "Ладно, откуда у тебя это имя?":
                            $ LauraX.FaceChange("angry", 1,Eyes="side")
                            $ LauraX.Statup("Love", 70, -2) # Love
                            $ LauraX.Statup("Obed", 70, 2) # Obed
                            ch_l "Это слишком личное."
            "Пожалуй, я лучше буду звать тебя Икс-23." if LauraX.Name == "Лора" and LauraX in Topics:
                            $ LauraX.Statup("Love", 70, -2) # Love
                            $ LauraX.Statup("Obed", 70, 5) # Obed
                            $ LauraX.FaceChange("sadside", 0,Brows="normal")
                            ch_l "Как хочешь."
                            $ LauraX.Name = "Икс-23"
                            $ LauraX.Name_rod = "Икс-23"
                            $ LauraX.Name_dat = "Икс-23"
                            $ LauraX.Name_vin = "Икс-23"
                            $ LauraX.Name_tvo = "Икс-23"
                            $ LauraX.Name_pre = "Икс-23"
            "Меня зовут [Player.Name]" if LauraX.Name != "???" and "player" not in Topics:
                    $ LauraX.FaceChange("normal", 0)
                    ch_l "Ладно."
                    $ Topics.append("player")
                    menu:
                        extend ""
                        ". . .и приятно познакомиться.":
                            $ LauraX.Statup("Love", 70, 1) # Love
                            $ LauraX.FaceChange("confused", 0,Mouth="normal")
                            ch_l "Да, мне тоже."
                        "Так вот. . . [[двигаться дальше]":
                            $ LauraX.Statup("Love", 70, 3) # Love
                            $ LauraX.Statup("Obed", 70, 1) # Obed
                            $ LauraX.Statup("Inbt", 70, 1) # Inbt

            "Что ты здесь делаешь?" if "Training" not in Topics:
                    $ LauraX.Statup("Obed", 70, -2) # Obed
                    $ LauraX.FaceChange("confused", 0)
                    ch_l "Тренируюсь. Для этого и предназначено это место."
                    $ Topics.append("Training")
                    menu:
                        extend ""
                        "То есть в институте, я тебя раньше здесь не видела." if not Player.Male:
                                $ LauraX.Statup("Obed", 70, 2) # Obed
                        "То есть в институте, я тебя раньше здесь не видел." if Player.Male:
                                $ LauraX.Statup("Obed", 70, 2) # Obed
                        "Логично.":
                                $ LauraX.FaceChange("normal", 0)
                                ch_p "Но ты новенькая?"
                                $ LauraX.Statup("Love", 70, 3) # Love
                                $ LauraX.Statup("Obed", 70, 4) # Obed
                    ch_l "Я здесь дольше тебя."
                    ch_l "Хотя в основном и на заданиях."
            "Значит, ты здесь ненадолго?" if "Training" in Topics and "Stay" not in Topics:
                    $ LauraX.Statup("Love", 70, 2) # Love
                    $ LauraX.FaceChange("normal", 0,Eyes="side")
                    ch_l "Скоро у меня новая миссия."
                    $ LauraX.FaceChange("normal", 0)
                    ch_l "Но после я планирую остаться на более долгий срок."
                    $ Topics.append("Stay")


            "Что это была за хрень?" if len(Topics) <= 1 and "WTF" not in Topics:
                    $ LauraX.Statup("Love", 70, -2) # Love
                    $ LauraX.Statup("Obed", 70, 8) # Obed
                    $ LauraX.FaceChange("confused", 0)
                    ch_l "Это была роборука."
                    $ LauraX.FaceChange("sad", 1,Eyes="leftside")
                    ch_l "Как я уже сказала, извини."
                    $ LauraX.Statup("Obed", 70, -3) # Obed
                    $ LauraX.Statup("Inbt", 70, 3) # Inbt
                    $ LauraX.FaceChange("smile", 0,Brows="confused")
                    ch_l "Хотя тебе, наверное, стоило увернуться."
                    $ Topics.append("WTF")

            "Мне интересно, какие у тебя способности?" if LauraX.Name != "???" and "claws" not in Topics:
                    $ LauraX.Statup("Love", 70, 1) # Love
                    $ LauraX.Statup("Obed", 70, 1) # Obed
                    $ LauraX.FaceChange("normal", 0)
                    ch_l "У меня быстрая регенерация."
                    $ LauraX.ArmPose = 2
                    ch_l "И когти."
                    $ LauraX.Claws = 1
                    $ LauraX.FaceChange("smile", 0,Brows="confused")
                    "*чик*"
                    $ Topics.append("claws")
                    menu:
                        "Похоже, острые коготки.":
                                $ LauraX.Statup("Inbt", 70, 3) # Inbt
                                ch_l "Ага, а еще их невозможно сломать."
                        "Клево.":
                                $ LauraX.Statup("Love", 70, 3) # Love
                                $ LauraX.Statup("Obed", 70, 2) # Obed
                                $ LauraX.Statup("Inbt", 70, 1) # Inbt
                                $ LauraX.FaceChange("smile", 0,Brows="surprised")
                                ch_l "Ага, а еще их невозможно сломать."
                        "Ауч.":
                                $ LauraX.Claws = 0
                                $ LauraX.FaceChange("confused", 0)
                                $ LauraX.Statup("Love", 70, -2) # Love
                                $ LauraX.Statup("Obed", 70, -5) # Obed
                                ch_l "Не волнуйся, я тебя не пораню."
                                $ LauraX.FaceChange("confused", 0,Mouth="normal")
                                $ LauraX.Statup("Inbt", 70, 7) # Inbt
                                ch_l "Наверное."
                    $ LauraX.Claws = 0
                    $ LauraX.ArmPose = 1

            "Разве ты не хочешь узнать про мою способность?" if "claws" in Topics and "powers" not in Topics:
                    if LauraX.Love >= 405:
                            $ LauraX.FaceChange("smile", 0,Brows="confused")
                            ch_l "Хочу, наверное."
                    else:
                            $ LauraX.FaceChange("normal", 0)
                            ch_l "Не особо."
                    $ LauraX.Statup("Inbt", 70, 3) # Inbt
                    $ Topics.append("powers")
                    if not Player.Male:
                        ch_p "Я невосприимчива к способностям других мутантов и могу их отключать."
                    else:
                        ch_p "Я невосприимчив к способностям других мутантов и могу их отключать."
                    $ LauraX.FaceChange("smile", 0,Brows="confused")
                    $ LauraX.Statup("Love", 70, 3) # Love
                    $ LauraX.Statup("Obed", 70, 3) # Obed
                    ch_l "Да? Интересно. Значит, ты можешь остановить мою регенерацию?"
                    ch_p "Ага. Временно, если я прикоснусь к тебе."
                    $ LauraX.Statup("Obed", 70, 2) # Obed
                    $ LauraX.Statup("Lust", 70, 3) # Lust
                    ch_l "Давай попробуем."
                    "Она протягивает руку, и вы прикасаетесь к ней."
                    $ LauraX.Statup("Love", 70, 1) # Love
                    $ LauraX.Statup("Obed", 70, 2) # Obed
                    $ LauraX.Statup("Lust", 70, 5) # Lust
                    $ LauraX.FaceChange("confused", 0)
                    ch_l "Хм."
                    $ LauraX.FaceChange("sexy", 1,Eyes="closed")
                    $ LauraX.Addictionrate += 1
                    "Вы чувствуете, как по ней проходит легкая дрожь."
                    $ LauraX.FaceChange("sexy", 1)
                    $ LauraX.Statup("Love", 70, 1) # Love
                    $ LauraX.Statup("Obed", 70, 3) # Obed
                    $ LauraX.Statup("Lust", 70, 5) # Lust
                    $ LauraX.Addictionrate += 1
                    ch_l "Странные ощущения."
                    $ LauraX.FaceChange("sexy", 1,Eyes="leftside")
                    $ LauraX.Statup("Obed", 70, 1) # Obed
                    $ LauraX.Statup("Lust", 70, 3) # Lust
                    $ LauraX.Addictionrate += 1
                    ch_l "-чувствую себя более \"живой\", чем обычно."
                    $ LauraX.Statup("Inbt", 70, 5) # Inbt
                    $ LauraX.Statup("Lust", 70, 5) # Lust
                    $ LauraX.FaceChange("sexy", 1,Brows="confused")
                    $ LauraX.Addictionrate += 1
                    ch_l "Это может быть. . . опасно."

            "Неважно. . . [[двигаться дальше]" if LauraX.Name != "???":
                    $ Loop = 0

        if len(Topics) >= 3 and LauraX.Name == "???":
                $ LauraX.Statup("Love", 70, -2) # Love
                $ LauraX.Statup("Obed", 70, 5) # Obed
                $ LauraX.Statup("Inbt", 70, 5) # Inbt
                ch_l "Да, кстати, ты можешь звать меня \"Икс-23\"."
                $ LauraX.Name = "Икс-23"
                $ LauraX.Name_rod = "Икс-23"
                $ LauraX.Name_dat = "Икс-23"
                $ LauraX.Name_vin = "Икс-23"
                $ LauraX.Name_tvo = "Икс-23"
                $ LauraX.Name_pre = "Икс-23"
        if len(Topics) >= 8:
                $ Loop = 0


    #close while loop
    ch_l "Ладно, мне еще нужно успеть на самолет."
    if "player" in Topics:
            $ LauraX.Statup("Love", 70, 2) # Love
            $ LauraX.Statup("Lust", 70, 1) # Lust
            $ LauraX.FaceChange("smile",0)
            ch_l "Может быть, мы увидимся снова, когда я вернусь, [Player.Name]."
    else:
            $ LauraX.FaceChange("normal", 0)
            if not Player.Male:
                ch_l "Может быть, мы увидимся снова, когда я вернусь, незнакомка."
            else:
                ch_l "Может быть, мы увидимся снова, когда я вернусь, незнакомец."
    if "powers" in Topics:
            $ LauraX.Statup("Obed", 70, 2) # Obed
            $ LauraX.Statup("Inbt", 70, 2) # Inbt
            $ LauraX.Statup("Lust", 70, 3) # Lust
            $ LauraX.FaceChange("smile", 1, Brows="confused")
            ch_l "Нам нужно будет. . . провести спарринг."

    $ LauraX.Loc = "hold"
    call Set_The_Scene

    "Она выбегает из комнаты, прямиком к ангару."

    $ LauraX.PubeC = 3
    $ LauraX.Todo.append("mission")

    $ bg_current = "bg dangerroom"
    $ Round -= 10
    call Shift_Focus(RogueX)
    $ ActiveGirls.remove(LauraX) if LauraX in ActiveGirls else ActiveGirls

    return

# end LauraMeet//////////////////////////////////////////////////////////


label Laura_Key:
        call Shift_Focus(LauraX)
        $ LauraX.Loc = bg_current
        call Set_The_Scene
        $ LauraX.FaceChange("bemused")
        $ Event_Queue = [0,0]
        ch_l "Слушай, эм. . . это не похоже на меня, но. . ."
        ch_l "Ты довольно часто ночуешь у меня, и я подумала. . ."
        ch_l "В общем, просто возьми."
        "Она берет вас за руку и практически насильно вкладывает ключ в вашу ладонь."
        $ Keys.append(LauraX) if LauraX not in Keys else Keys
        $ LauraX.Event[0] = 1
        ch_p "Спасибо."
        return



# Event Laura_Caught_Masturbating  /////////////////////////////////////////////////////


label Laura_BF(BO=[]):
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(LauraX,"bemused","краснеет. . .")
                return
        call Shift_Focus(LauraX)
        if LauraX.Loc != bg_current:
            $ LauraX.Loc = bg_current
            if LauraX not in Party:
                "[LauraX.Name] подходит к вам и показывает жестами, что хочет поговорить с вами наедине."
            else:
                "[LauraX.Name] поворачивается к вам и показывает жестами, что хочет поговорить с вами наедине."
        $ LauraX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ Event_Queue = [0,0]
        call Set_The_Scene(0)
        call Display_Girl(LauraX)
        $ LauraX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in LauraX.History:
                call expression LauraX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        "Она выглядит немного обеспокоенной, вы можете с уверенностью сказать, что ее тревожит тема предстоящего разговора."
        call Taboo_Level
        call CleartheRoom(LauraX)
        $ LauraX.FaceChange("angry",1,Eyes="side")
        $ Line = 0
        if "asked boyfriend" not in LauraX.DailyActions:
                ch_l "Значит так, [LauraX.Petname]. . ."
        $ LauraX.FaceChange("confused",1,Mouth="lipbite")
        ch_l "Я не знаю с чего мне начать- . . . Ты ведь знаешь, что мне приятно проводить с тобой время?"
        menu:
            extend ""
            "Я тоже очень люблю проводить время с тобой!":
                $ LauraX.FaceChange("surprised",2)
                ch_l "Хорошо, но-"
                $ LauraX.Statup("Obed", 50, -3)
                $ LauraX.Statup("Inbt", 80, 1)
                ch_l ". . ."
                $ LauraX.Statup("Love", 200, 5)
                $ LauraX.FaceChange("bemused",1,Eyes="side")
                ch_l "\"люблю\" - слишком сильно сказано, [LauraX.Petname]."
            "Да, конечно, это очень весело.":
                $ LauraX.Statup("Love", 200, 10)
                $ LauraX.Statup("Inbt", 80, 2)
                $ LauraX.FaceChange("smile",0)
                ch_l "Правда?"
            "Думаю, лучше с тобой, чем на занятиях по математике. . .":
                $ LauraX.Statup("Love", 200, 3)
                $ LauraX.Statup("Obed", 80, 3)
                $ LauraX.Statup("Inbt", 80, -3)
                $ LauraX.FaceChange("angry",1)
                ch_l "Эм, я хотела услышать немного другое. . ."
            "Ну, если ты так говоришь.":
                $ LauraX.Statup("Obed", 80, 6)
                $ LauraX.Statup("Inbt", 80, -8)
                $ LauraX.FaceChange("confused",1)
                ch_l ". . ."

        ch_l "Так вот, как я уже говорила, у меня не так много друзей."
        $ LauraX.FaceChange("sadside",1)
        ch_l "Я вроде как выросла в ужасном месте, а потом много времени провела в странствиях."
        ch_l "У меня была совсем другая жизнь до приезда сюда."
        menu:
            extend ""
            "Каково это было?":
                $ LauraX.Statup("Love", 200, 7)
                $ LauraX.Statup("Obed", 80, 2)
                $ LauraX.Statup("Inbt", 80, 3)
                $ LauraX.FaceChange("sad",1,Mouth="lipbite")
            "Да? Я знала." if not Player.Male:
                $ LauraX.Statup("Love", 200, 3)
                $ LauraX.Statup("Obed", 80, 4)
                $ LauraX.Statup("Inbt", 80, 1)
                $ LauraX.FaceChange("confused",1,Mouth="lipbite")
            "Да? Я знал." if Player.Male:
                $ LauraX.Statup("Love", 200, 3)
                $ LauraX.Statup("Obed", 80, 4)
                $ LauraX.Statup("Inbt", 80, 1)
                $ LauraX.FaceChange("confused",1,Mouth="lipbite")
            "Не нужно так драматизировать.":
                $ LauraX.Statup("Love", 200, -5)
                $ LauraX.Statup("Obed", 80, 10)
                $ LauraX.Statup("Inbt", 80, -5)
                $ LauraX.FaceChange("angry",1)
                $ Line = "bad"
                ch_l "Ладно!"
                ch_l "Тогда скажу \"проще\"."
                ch_l "Я не ненавижу проводить время с тобой."
        if Line != "bad":
                $ LauraX.FaceChange("normal",1,Eyes="side")
                if not Player.Male:
                    ch_l "Ну, ты, наверное, уже догадалась, что я связана с Росомахой."
                else:
                    ch_l "Ну, ты, наверное, уже догадался, что я связана с Росомахой."
                menu:
                    extend ""
                    "Да, это довольно очевидно.":
                            $ LauraX.Statup("Love", 200, 4)
                    "Я не знала!" if not Player.Male:
                            $ LauraX.Statup("Love", 200, 3)
                            $ LauraX.Statup("Inbt", 80, 1)
                            $ LauraX.FaceChange("confused",1)
                    "Я не знал!" if Player.Male:
                            $ LauraX.Statup("Love", 200, 3)
                            $ LauraX.Statup("Inbt", 80, 1)
                            $ LauraX.FaceChange("confused",1)
                    "А то.":
                            $ LauraX.Statup("Love", 200, 1)
                            $ LauraX.Statup("Obed", 80, 2)
                            $ LauraX.FaceChange("angry",1)
                ch_l "Если точнее, я в какой-то степени его клон."
                $ LauraX.FaceChange("angry",1,Eyes="side")
                ch_l "Я была создана, чтобы стать чем-то вроде биологического оружия, убийцей."
                ch_l "В детстве я много работала на них, пока в конце концов не сбежала."
                $ LauraX.FaceChange("sadside",1)
                ch_l "После этого мне приходилось делать разное. . . чтобы выжить."
                ch_l "Такое, чем я совсем не горжусь."
                $ LauraX.FaceChange("sad",1)
                ch_l "Но. . . не знаю. . . проводить время с тобой, думаю, помогает."
                $ LauraX.FaceChange("sad",1,Mouth="smile")
                ch_l "Мне вроде как становится. . . лучше."
        if LauraX.SEXP >= 20:
                $ LauraX.Statup("Obed", 80, 3)
                $ LauraX.Statup("Inbt", 80, 2)
                $ LauraX.Statup("Lust", 80, 5)
                $ LauraX.FaceChange("sly",1)
                if not Player.Male:
                    ch_l "В конце концов, ты очень хороша в постели."
                else:
                    ch_l "В конце концов, ты очень хорош в постели."
        if len(Player.Harem) >= 2:
                ch_l "Я знаю, что у тебя есть и другие девушки. . ."
                ch_l ". . . но я все равно хотела бы стать частью твоей жизни."
        elif Player.Harem:
                ch_l "Я знаю, что у тебя кто-то есть. . ."
                ch_l ". . . но я все равно хотела бы стать частью твоей жизни."
        else:
                ch_l "Я просто хотела бы стать частью твоей жизни."
        $ LauraX.FaceChange("sad",1,Mouth="smile")
        ch_l "Вот и все."

        $ LauraX.Event[5] += 1

        if LauraX in Player.Harem:
                #if she somehow already ended up in the harem
                if "LauraYes" in Player.Traits:
                        $ Player.Traits.remove("LauraYes")
                if "boyfriend" not in LauraX.Petnames:
                        $ LauraX.Petnames.append("boyfriend")
                return
        menu:
            extend ""
            "Ага! Я очень тебя люблю.":
                    $ LauraX.Statup("Love", 200, -3)
                    $ LauraX.Statup("Obed", 80, -3)
                    $ LauraX.Statup("Inbt", 80, 3)
                    $ LauraX.FaceChange("surprised",1)
                    ch_l "Ого!"
                    $ LauraX.FaceChange("perplexed")
                    ch_l "Тебе стоит притормозить, [LauraX.Petname]."
                    $ LauraX.FaceChange("smile",Eyes="side")
                    ch_l "Я не. . ."
                    ch_l "Я не думаю, что наши отношения доросли до такого. . ."
                    $ LauraX.FaceChange("perplexed",1)
                    if not Player.Male:
                        ch_l "Согласна?"
                    else:
                        ch_l "Согласен?"
                    menu:
                        extend ""
                        "Я считаю иначе.":
                                $ LauraX.Statup("Love", 200, 10)
                                $ LauraX.Statup("Obed", 80, 5)
                                $ LauraX.Statup("Inbt", 80, 5)
                                $ LauraX.Statup("Lust", 80, 2)
                                $ LauraX.FaceChange("smile",1,Eyes="side")
                                ch_l "Хах."
                        "Возможно, ты и права.":
                                $ LauraX.Statup("Love", 200, 6)
                                $ LauraX.Statup("Obed", 80, 3)
                                $ LauraX.Statup("Inbt", 80, 2)
                                $ LauraX.FaceChange("angry",1,Eyes="side",Mouth="lipbite")
                                ch_l "Ага. . ."
                    #end "I love you"
            "Ага, думаю, это было бы отлично.":
                    $ LauraX.Statup("Love", 200, 6)
                    $ LauraX.Statup("Obed", 80, 2)
                    $ LauraX.Statup("Inbt", 80, 3)
                    $ LauraX.FaceChange("smile",1,Eyes="side")
                    ch_l "Клево."
            "Хмм? Ладно.":
                    $ LauraX.Statup("Love", 80, 3)
                    $ LauraX.Statup("Obed", 80, 5)
                    $ LauraX.Statup("Inbt", 80, 3)
                    $ LauraX.FaceChange("confused",1,Eyes="side")
                    ch_l "Ага. . . клево."
            "Мне этого не очень хочется.":
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 80, 5)
                    $ LauraX.Statup("Inbt", 80, -5)
                    $ LauraX.FaceChange("sad",1)
                    if len(Player.Harem) >= 2:
                            ch_l "Это из-за [Player.Harem[0].Name_rod] и остальных?"
                    elif Player.Harem:
                            ch_l "Это из-за [Player.Harem[0].Name_rod]?"
                    else:
                            ch_l "Почему нет? В чем дело?"
                    menu:
                        extend ""
                        "Ага, не думаю, что она меня поймет." if len(Player.Harem) == 1:
                                $ LauraX.Statup("Love", 200, -5)
                                $ LauraX.Statup("Obed", 80, 7)
                                $ LauraX.FaceChange("angry",1,Eyes="side")
                                $ LauraX.GLG(Player.Harem[0],800,-20,1)
                                ch_l "Вот ведь сучка."
                        "Они этого не пойму." if len(Player.Harem) > 1:
                                $ LauraX.Statup("Love", 200, -5)
                                $ LauraX.Statup("Obed", 80, 7)
                                $ LauraX.FaceChange("angry",1,Eyes="side")
                                call HaremStatup(LauraX,700,-20) #lowers like of all Harem girls by 10
                                ch_l "Вот ведь сучки."
                        "Все. . . сложно.":
                                $ LauraX.Statup("Love", 200, -20)
                                $ LauraX.Statup("Obed", 80, 8)
                                $ LauraX.Statup("Inbt", 80, -5)
                                $ LauraX.FaceChange("angry",1)
                                ch_l "Сложно. Ага, конечно."
                                $ LauraX.FaceChange("angry",1,Eyes="side")
                                if len(Player.Harem) >= 2:
                                    ch_l "Наверное, это все из-за этих сучек."
                                    call HaremStatup(LauraX,700,-10) #lowers like of all Harem girls by 10
                                elif Player.Harem:
                                    ch_l "Наверное, это все из-за нее."
                                    $ LauraX.GLG(Player.Harem[0],800,-20,1)
                                $ Line = "no"
                        "Просто ты мне не настолько нравишься.":
                                $ LauraX.Statup("Love", 200, -10)
                                $ LauraX.FaceChange("surprised",1)
                                ch_l "Ох."
                                $ LauraX.Statup("Obed", 80, 10)
                                $ LauraX.Statup("Inbt", 80, 5)
                                $ LauraX.FaceChange("sadside",1)
                                ch_l "Ладно, думаю, я понимаю."
                    #end "why not?"

                    $ LauraX.FaceChange("sad",1)
                    if Line != "no":
                            ch_l "Твои слова не повлияют на мое отношение к тебе."
                    ch_l "Мне нужно. . . идти."
                    "Ошеломленная [LauraX.Name] уходит."
                    $ LauraX.Event[5] = 20
                    call Remove_Girl(LauraX)
                    $ Line = 0
                    return

        if Player.Harem:
                if not ApprovalCheck(LauraX, 1400):
                        if len(Player.Harem) >= 2:
                            ch_l "Так ты порвешь с остальными?"
                        else:
                            ch_l "Так ты порвешь с [Player.Harem[0].Name_tvo]?"
                        menu:
                            extend ""
                            "Ага, ради тебя.":
                                        $ LauraX.Statup("Love", 200, 20)
                                        $ LauraX.Statup("Obed", 80, 5)
                                        $ LauraX.Statup("Inbt", 80, 5)
                                        $ LauraX.FaceChange("surprised",2,Mouth="smile")
                                        ch_l ". . ."
                                        $ LauraX.FaceChange("smile",1)
                                        # fix, I need to add code here to initiate breakups with the rest. . .
                                        $ LauraX.Event[5] = 10
                            "Мне бы хотелось, чтобы ты присоединилась к нам.":
                                    $ Line = 0
                                    if ApprovalCheck(LauraX, 1200):
                                            #if she likes you well enough. . .
                                            $ BO = Player.Harem[:]
                                            while BO and Line != "no":
                                                # Spits out a "no" if she doesn't like another girl
                                                if LauraX.GirlLikeCheck(BO[0]) <= 500:
                                                        $ Line = "no"
                                                $ BO.remove(BO[0])
                                    else:
                                            $ Line = "no"
                                    if Line == "no":
                                            $ LauraX.Statup("Love", 200, -10)
                                            $ LauraX.Statup("Obed", 80, 10)
                                            $ LauraX.FaceChange("angry",1)
                                            call HaremStatup(LauraX,700,-10) #lowers like of all Harem girls by 10
                                            ch_l "Эм, я пас."
                                    else:
                                            $ LauraX.Statup("Love", 200,5)
                                            $ LauraX.Statup("Obed", 80, 15)
                                            $ LauraX.Statup("Inbt", 80, 10)
                                            $ LauraX.FaceChange("bemused",1)
                                            ch_l "Ну, пожалуй, в этом нет ничего страшного."
                            "Что? Конечно нет.":
                                            $ LauraX.Statup("Love", 200, -25)
                                            $ LauraX.Statup("Obed", 80, 5)
                                            call HaremStatup(LauraX,700,-20) #lowers like of all Harem girls by 20
                                            $ LauraX.FaceChange("angry",1)
                                            ch_l "Ну и ладно."
                                            $ Line = "no"
                        if Line == "no":
                                $ LauraX.Event[5] = 20
                                call Remove_Girl(LauraX)
                                $ Line = 0
                                return
                #end "she tries to get you to break up with the rest. . .

                #if you agreed, but have other girls. . .
                if len(Player.Harem) >= 2:
                    ch_l "А ты не думаешь, что остальные будут возражать?"
                else:
                    ch_l "А ты не думаешь, что [Player.Harem[0].Name] будет возражать?"
                menu:
                    extend ""
                    "Все хорошо, всех все устраивает." if "LauraYes" in Player.Traits:
                            $ LauraX.Statup("Love", 200, 5)
                            $ LauraX.Statup("Obed", 80, 10)
                            $ LauraX.Statup("Inbt", 80, 5)
                            $ LauraX.FaceChange("surprised",1)
                            ch_l "О, клево."
                    "Нууу. . . это сперва еще нужно выяснить." if "LauraYes" not in Player.Traits:
                            $ LauraX.Statup("Love", 200, 3)
                            $ LauraX.Statup("Obed", 80, 3)
                            $ LauraX.Statup("Inbt", 80, 1)
                            $ LauraX.Statup("Lust", 80, 1)
                            $ LauraX.FaceChange("confused",1)
                            ch_l "Хм, надеюсь, ты вернешься ко мне с ответом?"
                            $ LauraX.Event[5] = 20
                            call Remove_Girl(LauraX)
                            $ Line = 0
                            return
                call HaremStatup(LauraX,900,20) #raises like of all Harem girls by 20
        # end harem stuff

        if "Historia" not in Player.Traits:
            $ Player.Harem.append(LauraX)
            if "LauraYes" in Player.Traits:
                    $ Player.Traits.remove("LauraYes")
            $ LauraX.Petnames.append("boyfriend")
            call Harem_Initiation
        $ LauraX.Statup("Love", 200, 3)
        $ LauraX.Statup("Obed", 80, 3)
        $ LauraX.Statup("Inbt", 80, 1)
        $ LauraX.Statup("Lust", 80, 1)
        $ LauraX.FaceChange("sly",1)
        ch_l "Ты как, можешь уделить мне несколько минут? . ."
        if "Historia" in Player.Traits:
                return 1
        $ Tempmod = 10
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        $ Tempmod = 0

        return

label Laura_Cleanhouse:
        # this is triggered if you agree to break up the other girls, but then fail to within the time limit
        $ LauraX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        if "cleanhouse" in LauraX.Todo:
                        $ LauraX.Todo.remove("cleanhouse")
        if not Player.Harem or LauraX in Player.Harem:
                        $ LauraX.Event[5] = 2
                        return

        if LauraX.Loc == bg_current or LauraX in Party:
                "[LauraX.Name] бросает на вас хмурый взгляд."
        else:
                "[LauraX.Name] выходит из-за угла и натыкается на вас."
        if bg_current != "bg laura" and bg_current != "bg player":
                "Не говоря ни слова, она пристраивается за вами и подталкивает вас к ее комнате."
                $ bg_current = "bg laura"
        $ LauraX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(LauraX)
        call Set_The_Scene
        call Taboo_Level
        $ LauraX.DailyActions.append("relationship")
        $ LauraX.Statup("Love", 200, -20)
        $ LauraX.FaceChange("angry",1)
        ch_l "В чем дело, [Player.Petname]?"
        ch_l "Прошла уже неделя, а ты все еще встречаешься с [Player.Harem[0].Name_tvo]!"
        if len(Player.Harem) >= 2:
                ch_l "Не говоря уже об остальных!"
        menu:
            extend ""
            "Извини, но я не хочу ничего менять":
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 80, 5)
                    $ LauraX.Statup("Inbt", 80, 5)
                    $ LauraX.FaceChange("angry",2)
                    ch_l "Сволочь."
                    $ LauraX.FaceChange("sadside",1)
                    if not Player.Male:
                        ch_l "Ну, хотя бы не соврала."
                    else:
                        ch_l "Ну, хотя бы не соврал."
            "Должно быть, вылетело из головы":
                    $ LauraX.Statup("Love", 200, -10)
                    $ LauraX.Statup("Obed", 80, 10)
                    ch_l "!"
                    if not Player.Male:
                        ch_l "Ты серьезно? И это все, что ты смогла придумать?"
                    else:
                        ch_l "Ты серьезно? И это все, что ты смог придумать?"
            "[[пожать плечами]":
                    $ LauraX.Statup("Love", 200, -20)
                    $ LauraX.Statup("Obed", 80, 10)
                    $ LauraX.Statup("Inbt", 80, 10)
                    $ LauraX.Blush = 2
                    show Laura_Sprite with vpunch
                    "Она бьет вас."
                    "Заслуженно."
                    $ LauraX.Blush = 1

        ch_l "Не могу поверить, что ты заставляешь меня пройти через это."
        ch_l "Вынуждаешь меня выбирать между тобой и этим соглашением."
        $ Line = 0
        if ApprovalCheck(LauraX, 1400) and ApprovalCheck(LauraX, 600,"O"):
                #if she's very obedient. . .
                pass
        elif ApprovalCheck(LauraX, 1200) and ApprovalCheck(LauraX, 500,"O"):
                #second chance on if she likes you well enough. . .
                $ BO = Player.Harem[:]
                while BO and Line != "no":
                    # Spits out a "no" if she doesn't like another girl
                    if LauraX.GirlLikeCheck(BO[0]) <= 400:
                            $ Line = "no"
                    $ BO.remove(BO[0])
        else:
                $ Line = "no"
        if Line == "no":
                $ LauraX.Statup("Love", 200, -10)
                $ LauraX.Statup("Obed", 80, 10)
                $ LauraX.FaceChange("angry",1)
                call HaremStatup(LauraX,700,-15) #lowers like of all Harem girls by 15
                ch_l "Нет, это все бред, забудь."
        else:
                $ LauraX.Statup("Love", 200, 5)
                $ LauraX.Statup("Obed", 80, 20)
                $ LauraX.Statup("Inbt", 80, 10)
                $ LauraX.FaceChange("angry",1,Eyes="side")
                ch_l "Ладно, ладно, неважно. Я с вами."
                if "Historia" not in Player.Traits:
                        $ Player.Harem.append(LauraX)
                        if "LauraYes" in Player.Traits:
                                $ Player.Traits.remove("LauraYes")
                        $ LauraX.Petnames.append("boyfriend")
                        call Harem_Initiation
                        call HaremStatup(LauraX,900,20) #raises like of all Harem girls by 20
                        $ LauraX.Event[5] = 20
        return

## start Laura_Love//////////////////////////////////////////////////////////
label Laura_Love(Shipping=[],Shipshape=0,Topics=[],BO=[]):
        # SHipping is used to track who else you're involved with
        # if LauraX.Event[6] = 5, then it cleared
        # if LauraX.Event[6] = 20, then it broke because you didn't love her
        # if LauraX.Event[6] = 23, then it broke because you pissed her off
        # if LauraX.Event[6] = 25, then it broke and you already went through the redux

        $ LauraX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ BO = TotalGirls[:]
        $ BO.remove(LauraX)
        while BO:
            if ApprovalCheck(BO[0], 1200, "LO"):
                    $ Shipping.append(BO[0])
            $ BO.remove(BO[0])
        $ Shipshape = len(Shipping)

        if LauraX.Loc == bg_current or LauraX in Party:
                "[LauraX.Name] смотрит на вас с озабоченным видом."
        else:
                "[LauraX.Name] выходит из-за угла и натыкается на вас."
        if bg_current != "bg laura" and bg_current != "bg player":
                "Не говоря ни слова, она пристраивается за вами и подталкивает вас к ее комнате."
                $ bg_current = "bg laura"
        $ LauraX.Loc = bg_current
        $ Event_Queue = [0,0]
        call Set_The_Scene
        call CleartheRoom(LauraX)
        call Set_The_Scene
        call Taboo_Level
        call Shift_Focus(LauraX)
        $ LauraX.DailyActions.append("relationship")
        $ LauraX.FaceChange("sad",1)
        ch_l "Итак, начну. . . мне нравится то, что происходит. . ."
        ch_l "-между нами. . ."
        $ LauraX.FaceChange("sadside",1)
        ch_l "Мне довольно трудно открыться людям. . ."
        ch_l "Меня так много раз предавали."
        menu:
            extend ""
            "Я никогда тебя не предам.":
                    $ LauraX.FaceChange("bemused",1)
                    $ LauraX.Statup("Love", 200, 10)
                    $ LauraX.Statup("Obed", 70, 5)
                    $ LauraX.Statup("Inbt", 60, 5)
                    ch_l "Я. . . теперь я знаю."
            "Мне грустно это слышать.":
                    $ LauraX.FaceChange("sadside",1,Mouth="smile")
                    $ LauraX.Statup("Love", 200, 5)
                    $ LauraX.Statup("Obed", 90, -5)
                    $ LauraX.Statup("Inbt", 60, 10)
                    ch_l ". . ."
                    $ LauraX.FaceChange("smile",1)
                    ch_l "Спасибо. . ."
            "Это, должно быть, тяжело.":
                    $ LauraX.FaceChange("sadside",1,Mouth="normal")
                    $ LauraX.Statup("Love", 200, 5)
                    ch_l ". . ."
                    $ LauraX.FaceChange("smile",1)
                    ch_l "Да, тяжело. . ."
            "Оу, хреново.":
                    $ LauraX.FaceChange("confused",1)
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 90, 10)
                    $ LauraX.Statup("Inbt", 90, -5)
                    ch_l ". . ."
                    $ LauraX.FaceChange("angry",1,Eyes="side")
                    ch_l "Ага. . ."
        ch_l "Мне никогда не было так легко, как здесь, с тобой."
        $ LauraX.Eyes = "normal"
        ch_l "Я подумала, что пришло время открыться и рассказать тебе больше."
        $ Line = 0
        while len(Topics) < 9 and "exit" not in Topics:
                #Lines are topics of current discussion. "Topics" catalogues things alrewady discussed

                if Line == "facility":
                        menu:
                            extend ""
                            "Как много человек ты убила?" if "kills" not in Topics:
                                    $ LauraX.FaceChange("angry",0,Eyes="side")
                                    ch_l "Несколько десятков. Как минимум 13 главных целей."
                                    ch_l "А \"сошек\" еще больше"
                                    $ Topics.append("kills")
                            "Ты когда-нибудь проваливала задание?" if "fail" not in Topics:
                                    $ LauraX.FaceChange("angry",0,Eyes="side",Brows="normal")
                                    ch_l "Один раз или два."
                                    ch_l "Иногда целям удавалось уйти."
                                    ch_l "Я не горжусь тем, кем я тогда была, но даже в те времена. . ."
                                    $ LauraX.Mouth = "smile"
                                    ch_l ". . . часть меня радовалась, когда они сбегали."
                                    $ Topics.append("fail")
                            "Кто нибудь заботился о тебе?" if "mother" not in Topics:
                                    $ LauraX.FaceChange("smile",0)
                                    ch_l "Моя мама, Сара Кинни."
                                    ch_l "Именно она родила меня, а также она была одной из ученых, которые создали меня."
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "Она пыталась мне помочь, пока я ее не убила."
                                    $ Topics.append("mother")
                                    $ Line = "mother"
                            "Как тебе удалось сбежать?" if "escape" not in Topics:
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "Мне помогла мама."
                                    ch_l "Она вытащила меня, нашла путь к побегу."
                                    ch_l "Это было последнее, что она сделала."
                                    $ Topics.append("escape")
                                    $ Line = "mother"
                            "Мне бы хотелось узнать больше о том, что произошло после.":
                                    $ Line = "NYX"
                            "Хватит об этом. . .":
                                    $ Line = 0

                # end facility questions

                if Line == "mother":
                        menu:
                            extend ""
                            "Кем была твоя мама?" if "mother" not in Topics:
                                    $ LauraX.FaceChange("smile",0)
                                    ch_l "Ее звали Сара Кинни."
                                    ch_l "Именно она родила меня, а также она была одной из ученых, которые создали меня."
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "Она пыталась мне помочь, пока я ее не убила."
                                    $ Topics.append("mother")
                                    $ Line = "mother"
                            "Почему ты убила ее?" if "killed" not in Topics and "mother" in Topics:
                                    $ LauraX.FaceChange("sad",0,Eyes="surprised")
                                    ch_l "Я не хотела, но Триггер вынудил меня. . ."
                                    $ LauraX.FaceChange("sadside",0)
                                    if "trigger" in LauraX.History:
                                            ch_l "Я уже говорила тебе об этом ранее. . ."
                                    else:
                                            $ LauraX.History.append("trigger")
                                    ch_l ". . . это вещество, которое заставляло меня убивать, даже если я не хотела."
                                    $ Topics.append("killed")
                            "Это была не твоя вина." if "killed" in Topics:
                                    $ LauraX.Statup("Love", 200, 5)
                                    $ LauraX.Statup("Obed", 70, 5)
                                    $ LauraX.Statup("Inbt", 70, 5)
                                    $ LauraX.FaceChange("sad",0)
                                    ch_l "Нет, конечно нет."
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "Но ее кровь на моих руках."
                                    $ Line = "facility"
                            "Это, наверное, было ужасно." if "killed" in Topics:
                                    $ LauraX.FaceChange("sadside",0)
                                    $ LauraX.Statup("Love", 200, 5)
                                    $ LauraX.Statup("Obed", 90, 5)
                                    ch_l "Мне потребовалось некоторое время, чтобы прийти в себя. . ."
                                    $ LauraX.FaceChange("normal",0)
                                    ch_l "но думаю, теперь я в порядке."
                                    $ Line = "facility"
                            "Ну что сказать, облом." if "killed" in Topics:
                                    $ LauraX.FaceChange("angry",1)
                                    $ LauraX.Statup("Love", 200, -10)
                                    $ LauraX.Statup("Obed", 90, 5)
                                    ch_l "Ты серьезно? Смеешься над смертью моей мамы?!"
                                    $ Topics.append("exit")
                                    $ Line = "angry"
                # end questions about mother

                if Line == "NYX":
                        menu:
                            extend ""
                            "Как ты выживала?" if "living" not in Topics:
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "В то время я мало что могла сделать, в основном просто искала еду где придется."
                                    ch_l "Ты можешь пережить много ужасных вещей, если у тебя есть быстрая регенерация."
                                    $ LauraX.FaceChange("bemused",1,Brows="sad")
                                    ch_l "Также мне приходилось заниматься. . . сомнительными вещами."
                                    $ Topics.append("living")

                            "Сексуального плана?" if "work" not in Topics and "living" in Topics:
                                    $ LauraX.FaceChange("sadside",2)
                                    $ LauraX.Statup("Obed", 90, 5)
                                    $ LauraX.Statup("Inbt", 90, 10)
                                    ch_l ". . ."
                                    $ LauraX.Blush = 1
                                    ch_l "В какой-то степени."
                                    $ Line = "work"
                                    $ Topics.append("work")

                            "Ты причиняла людям боль?" if "work" not in Topics and "living" in Topics:
                                    $ LauraX.FaceChange("surprised",0,Eyes="normal")
                                    ch_l "Нет, конечно нет."
                                    ch_l "После учреждения я просто не могла больше заниматься таким."
                                    $ LauraX.FaceChange("bemused",0)
                                    ch_l "Я никому не причиняла вреда."
                                    $ LauraX.FaceChange("sadside",2)
                                    ch_l "Скорее, я оказывала что-то вроде услуг. . . сексуального плана."
                                    $ Line = "work"
                                    $ Topics.append("work")

                            "А потом ты, в конце концов, добралась сюда? [[выход]" if "xaviers" not in Topics:
                                    $ LauraX.FaceChange("bemused",0)
                                    ch_l "Да, в конце концов."
                                    ch_l "Я увидела Росомаху в новостях и подумала, возможно, он сможет дать ответы."
                                    ch_l "Хотя он редко бывает здесь."
                                    $ Topics.append("xaviers")
                                    $ Line = 0
                            "Хорошо, что в итоге ты оказалась здесь. [[выход]" if "xaviers" in Topics:
                                    $ LauraX.FaceChange("smile",0)
                                    ch_l "Ага."
                                    $ Line = 0

                if Line == "work":
                        $ LauraX.FaceChange("sadside",0,Mouth="normal")
                        ch_l "В основном у меня были очень грубые клиенты."
                        ch_l "Те, кто не мог контролировать себя."
                        $ LauraX.FaceChange("angry",0,Mouth="smile")
                        ch_l "Самое то для девушки, которая может исцеляться, верно?"
                        menu:
                                extend ""
                                "Это ужасно. Хотела бы я защитить тебя." if not Player.Male:
                                        $ LauraX.FaceChange("smile",1)
                                        $ LauraX.Statup("Love", 200, 5)
                                        $ LauraX.Statup("Obed", 90, 5)
                                        $ LauraX.Statup("Inbt", 90, -5)
                                        ch_l "Спасибо, но со мной все было в порядке."
                                        $ LauraX.FaceChange("sadside",0)
                                        ch_l "Я не заслуживала такой жизни, но тогда я чувствовала, что не достойна лучшего."
                                "Это ужасно. Хотел бы я защитить тебя." if Player.Male:
                                        $ LauraX.FaceChange("smile",1)
                                        $ LauraX.Statup("Love", 200, 5)
                                        $ LauraX.Statup("Obed", 90, 5)
                                        $ LauraX.Statup("Inbt", 90, -5)
                                        ch_l "Спасибо, но со мной все было в порядке."
                                        $ LauraX.FaceChange("sadside",0)
                                        ch_l "Я не заслуживала такой жизни, но тогда я чувствовала, что не достойна лучшего."
                                "Ты сильная, смогла выбраться оттуда.":
                                        $ LauraX.FaceChange("smile",0)
                                        $ LauraX.Statup("Love", 200, 5)
                                        $ LauraX.Statup("Obed", 90, 10)
                                        $ LauraX.Statup("Inbt", 90, 5)
                                        ch_l "Спасибо."
                                        ch_l "Тогда я не думала об этом так. . ."
                                        $ LauraX.FaceChange("sadside",0)
                                        ch_l "Я просто чувствовала, что такова моя участь."
                                        ch_l "Но теперь я понимаю, насколько это было неправильно."
                                "Да, в этом есть смысл.":
                                        $ LauraX.FaceChange("confused",1)
                                        $ LauraX.Statup("Love", 200, -5)
                                        $ LauraX.Statup("Obed", 90, 15)
                                        $ LauraX.Statup("Inbt", 90, -5)
                                        ch_l "Не думаешь, прежде чем говорить, да?"
                                        $ LauraX.FaceChange("sadside",0)
                                        ch_l "Это было неправильно, просто тогда я этого не понимала."
                        ch_l "В конце концов, я все преодолела и решила уйти оттуда."
                        ch_l "Я совру, если скажу, что они не пытались остановить меня."
                        $ Line = "NYX"

                if not Line:
                        # Primary menu, falls through to this
                        menu:
                            extend ""
                            "Чем ты занималась в том учреждение?" if "facility" not in Topics:
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "После того, как они проверили мои способности, они заставили меня работать."
                                    ch_l "В основном я убивала людей за них."
                                    $ Topics.append("facility")
                                    $ Line = "facility"
                            "Раскажи подробнее о том учреждение. . ." if "facility" in Topics:
                                    $ Line = "facility"

                            "Куда ты пошла, после того как сбежала?" if "NYX" not in Topics:
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "Я несколько недель бродила по дикой местности."
                                    ch_l "И в конце концов я нашла дорогу в Нью-Йорк."
                                    ch_l "Несколько лет я жила на улице."
                                    $ Topics.append("NYX")
                                    $ Line = "NYX"
                            "Подробнее о временах после побега. . ." if "NYX" in Topics:
                                    $ Line = "NYX"

                            "Я рада, что ты открылась мне. [[выход]" if len(Topics) >= 5 and not Player.Male:
                                    $ LauraX.FaceChange("smile",0)
                                    $ LauraX.Statup("Love", 200, 10)
                                    $ LauraX.Statup("Obed", 90, 3)
                                    $ LauraX.Statup("Inbt", 90, 3)
                                    ch_l "Спасибо, что выслушала мою болтовню."
                                    $ Topics.append("exit")
                            "Я рад, что ты открылась мне. [[выход]" if len(Topics) >= 5 and Player.Male:
                                    $ LauraX.FaceChange("smile",0)
                                    $ LauraX.Statup("Love", 200, 10)
                                    $ LauraX.Statup("Obed", 90, 3)
                                    $ LauraX.Statup("Inbt", 90, 3)
                                    ch_l "Спасибо, что выслушала мою болтовню."
                                    $ Topics.append("exit")
                            "Думаю, этого достаточно. [[выход]" if "facility" in Topics and "NYX" in Topics:
                                    $ LauraX.FaceChange("sadside",0, Mouth="smile")
                                    $ LauraX.Statup("Obed", 90, 10)
                                    ch_l "Ага, теперь ты знаешь, через что я прошла."
                                    $ Topics.append("exit")
                            "Честно говоря, мне все равно. [[выход]":
                                    $ LauraX.FaceChange("angry",0)
                                    $ LauraX.Statup("Love", 200, -15)
                                    $ LauraX.Statup("Obed", 50, 5)
                                    $ LauraX.Statup("Obed", 90, 10)
                                    $ LauraX.Statup("Inbt", 90, -5)
                                    ch_l "Ох, извини, если я утомила тебя своей болтовней."
                                    $ Line = "angry"
                                    $ Topics.append("exit")

        #end while loop

        if Line == "angry":
                $ LauraX.FaceChange("angry",0)
                ch_l "А я-то думала, что что-то да значу для тебя."
                ch_l "Ладно, забудь!"
                $ Line = 0
                $ LauraX.Event[6] = 23
                $ LauraX.RecentActions.append("angry")
                $ LauraX.DailyActions.append("angry")
                hide Laura_Sprite with easeoutright
                call Remove_Girl(LauraX)
                $ LauraX.Loc = "hold" #puts her off the board for the day
                jump Misplaced
                return

        $ LauraX.FaceChange("bemused",0,Eyes="down")
        if not Player.Male:
            ch_l "Я подумала и решила, что ты должна знать. . ."
        else:
            ch_l "Я подумала и решила, что ты должен знать. . ."
        $ LauraX.FaceChange("smile",2)
        ch_l "Я люблю тебя."
        menu:
                extend ""
                "Я тоже тебя люблю!":
                    $ LauraX.FaceChange("smile",1)
                    $ LauraX.Statup("Love", 200, 20)
                    $ LauraX.Statup("Inbt", 90, 5)
                    ch_l "На секунду я даже заволновалась."
                    $ LauraX.Petnames.append("lover")
                    jump Laura_Love_End
                "Я знаю.":
                    $ LauraX.FaceChange("smile",1)
                    $ LauraX.Statup("Love", 200, 10)
                    $ LauraX.Statup("Obed", 90, 5)
                    $ LauraX.Statup("Inbt", 90, 10)
                    $ LauraX.Statup("Lust", 90, 5)
                    ch_l "Ну и скользкая же ты персона. А если серьезно, то что насчет тебя?"
                "Эм. . . это здорово?":
                    $ LauraX.FaceChange("confused",1)
                    $ LauraX.Statup("Obed", 90, 5)
                    ch_l "Я ждала чего-то большего, [LauraX.Petname]."
                "Хм.":
                    $ LauraX.FaceChange("confused",1)
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 90, 10)
                    ch_l "Не знаю, как это понимать."


        menu:
                extend ""
                "Ох, я тоже тебя люблю!":
                    $ LauraX.FaceChange("smile",1)
                    $ LauraX.Statup("Love", 200, 15)
                    $ LauraX.Statup("Obed", 90, 5)
                    $ LauraX.Statup("Inbt", 90, 5)
                    ch_l "На секунду я даже заволновалась."
                    $ LauraX.Petnames.append("lover")
                    jump Laura_Love_End
                "Я. . . тоже тебя люблю?":
                    $ LauraX.FaceChange("confused",1)
                    $ LauraX.Statup("Love", 200, 5)
                    $ LauraX.Statup("Obed", 90, 10)
                    ch_l "Ладно, сойдет."
                    $ LauraX.Petnames.append("lover")
                    jump Laura_Love_End
                "Это, конечно, круто и все такое. . .":
                    $ LauraX.FaceChange("sadside",1)
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 90, 10)
                    $ LauraX.Statup("Inbt", 90, -5)
                    ch_l ". . . но ты не можешь ответить мне взаимностью. Понятно."
                "Мне. . . не по себе от твоих слов.":
                    $ LauraX.FaceChange("angry",1)
                    $ LauraX.Statup("Love", 200, -10)
                    $ LauraX.Statup("Obed", 90, 15)
                    $ LauraX.Statup("Inbt", 90, -5)
                    ch_l "Мне не нравится, к чему все идет."

        ch_l "В чем проблема?"
        ch_l "Это из-за другой?"
        $ Line = 0
        menu:
                extend ""
                "Да, из-за другой." if Shipping and Shipshape < 3:
                    menu:       #rkeljsvgb
                        "Из-за [RogueX.Name_rod]." if RogueX in Shipping:
                                $ Line = RogueX
                        "Из-за [KittyX.Name_rod]." if KittyX in Shipping:
                                $ Line = KittyX
                        "Из-за [EmmaX.Name_rod]." if EmmaX in Shipping:
                                $ Line = EmmaX
                        "Из-за [JeanX.Name_rod]." if JeanX in Shipping:
                                $ Line = JeanX
                        "Из-за [StormX.Name_rod]." if StormX in Shipping:
                                $ Line = StormX
                        "Из-за [JubesX.Name_rod]." if JubesX in Shipping:
                                $ Line = JubesX
                        "Из-за [GwenX.Name_rod]." if GwenX in Shipping:
                                $ Line = GwenX
                        "Из-за [BetsyX.Name_rod]." if BetsyX in Shipping:
                                $ Line = BetsyX
                        "Из-за [DoreenX.Name_rod]." if DoreenX in Shipping:
                                $ Line = DoreenX
                        "Из-за [WandaX.Name_rod]." if WandaX in Shipping:
                                $ Line = WandaX
                        "Мне бы не хотелось произносить ее имя.":
                                $ LauraX.Statup("Obed", 90, 15)
                                $ LauraX.Statup("Inbt", 90, 5)
                                $ LauraX.Statup("Lust", 90, 5)
                                $ LauraX.FaceChange("sadside",1)
                                ch_l "Ну, у тебя всегда есть выбор."

                "Да, из-за других" if Shipshape > 1:
                        $ LauraX.Statup("Obed", 90, 15)
                        $ LauraX.Statup("Inbt", 90, 5)
                        $ LauraX.Statup("Lust", 90, 5)
                        $ LauraX.FaceChange("sadside",1)
                        ch_l "Ну, у тебя всегда есть выбор."
                "У меня никого нет.":
                        $ LauraX.Statup("Love", 200, -15)
                        $ LauraX.Statup("Obed", 90, 15)
                        $ LauraX.Statup("Inbt", 90, 5)
                        $ LauraX.FaceChange("sad",1)
                        if ApprovalCheck(LauraX, 1000, "OI"):
                            ch_l "Хоть что-то."
                        else:
                            ch_l ". . ."
                "Дело в \"тебе\".":
                        $ LauraX.FaceChange("angry")
                        $ LauraX.Statup("Love", 200, -25)
                        $ LauraX.Statup("Obed", 90, 15)
                        ch_l "Серьезно? Ты надо мной издеваешься?"
                        $ LauraX.Statup("Love", 200, -10)
                        ch_l "Поверь, тебе не понравится, если ты увидишь меня в гневе."
                        $ LauraX.RecentActions.append("angry")
                        $ LauraX.DailyActions.append("angry")


        if Line:
                #If you called out a girl,
                if LauraX.GirlLikeCheck(Line) >= 800:
                        $ LauraX.Statup("Love", 200, 5)
                        $ LauraX.Statup("Obed", 90, 20)
                        $ LauraX.Statup("Inbt", 90, 5)
                        $ LauraX.Statup("Lust", 90, 5)
                        $ LauraX.FaceChange("sadside",1)
                        ch_l "Ага, я думаю, она классная."
                else:
                        $ LauraX.FaceChange("angry",Eyes="side")
                        $ LauraX.Statup("Love", 200, -5)
                        $ LauraX.Statup("Obed", 90, 20)
                        ch_l "Вот сучка."
                        $ LauraX.RecentActions.append("angry")
                        $ LauraX.GLG(Line,800,-50,1)
        ch_l "Ну, если ты так к этому относишься. . ."
        ch_l "Я. . . увидимся позже."
        ch_l "Это. . . больно."

label Laura_Love_End:
        if "lover" not in LauraX.Petnames:
                $ LauraX.Event[6] = 20
                hide Laura_Sprite with easeoutright
                call Remove_Girl(LauraX)
                $ LauraX.Loc = "hold" #puts her off the board for the day
                jump Misplaced
                return

        $ LauraX.Event[6] = 5
        "[LauraX.Name] крепко обнимает вас."
        $ LauraX.Statup("Love", 200, 25)
        $ LauraX.Statup("Lust", 90, 5)
        $ LauraX.FaceChange("sly",1)
        ch_l "Итак. . . у нас есть немного времени. . ."
        $ LauraX.Statup("Lust", 90, 10)

        if not LauraX.Sex:
            $ LauraX.FaceChange("bemused",2)
            ch_l "Думаю, я готова. . ."
        else:
            ch_l "Не хочешь немного развлечься?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Да, давай cделаем это! [[секс]":
                    $ LauraX.Statup("Inbt", 30, 20)
                    $ LauraX.Statup("Obed", 70, 10)
                    ch_l "Ммм. . ."
                    if Player.Male:
                            call SexAct("sex") # call Laura_SexAct("sex")
                    else:
                            call SexAct("blow") # call Laura_SexAct("blow")
                "У меня есть другая идея. . .[[выбрать другое занятие]":
                    $ LauraX.Brows = "confused"
                    $ LauraX.Statup("Obed", 70, 25)
                    ch_l "Например? . ."
                    $ Tempmod = 20
                    call SexMenu
        jump Misplaced
        return

label Laura_Love_Redux:
         #this is for if you rejected her but want a second chance
        $ Line = 0
        $ LauraX.DailyActions.append("relationship")
        call Shift_Focus(LauraX)

        if LauraX.Event[6] >= 25:
                #if this is the second time through
                ch_p "Надеюсь, ты меня простила, я все еще люблю тебя."
                $ LauraX.Statup("Love", 95, 10)
                if ApprovalCheck(LauraX, 950, "L"):
                    $ Line = "love"
                else:
                    $ LauraX.FaceChange("angry")
                    ch_l "Смотрю, ты все еще на что-то надеешься, [LauraX.Petname]."
                    $ LauraX.Eyes="side"
                    ch_l ". . ."
                    $ LauraX.FaceChange("angry",Mouth="lipbite")
                    ch_l "Хочу услышать твои оправдания."
        elif LauraX.Event[6] >= 23:
                #if you pissed her off the first time
                if not Player.Male:
                    ch_p "Ранее я была груба, когда ты решилась открыться мне."
                else:
                    ch_p "Ранее я был груб, когда ты решилась открыться мне."
                $ LauraX.Statup("Love", 95, 10)
                if ApprovalCheck(LauraX, 950, "L"):
                    ch_l "И. . ."
                else:
                    $ LauraX.FaceChange("angry")
                    ch_l "Смотрю, ты все еще на что-то надеешься, [LauraX.Petname]."
                    $ LauraX.Eyes="side"
                    ch_l ". . ."
                    $ LauraX.FaceChange("angry",Mouth="lipbite")
                    ch_l "Хочу услышать твои оправдания."
        else:
                    if not Player.Male:
                        ch_p "Помнишь момент, когда я сказала тебе, что не люблю тебя?"
                    else:
                        ch_p "Помнишь момент, когда я сказал тебе, что не люблю тебя?"
                    $ LauraX.FaceChange("perplexed",1)
                    ch_l ". . ."
                    $ LauraX.FaceChange("angry", Eyes="side")
                    ch_l "Как я могла забыть?"

        if Line != "love":
                menu:
                    extend ""
                    "Прости, я не хотела так говорить." if not Player.Male:
                        $ LauraX.Eyes = "surprised"
                        ch_l "О, серьезно?"
                        ch_l "Как удобно."
                        ch_p "Я люблю тебя, [LauraX.Name]."
                        $ LauraX.Statup("Love", 200, 10)
                        if ApprovalCheck(LauraX, 950, "L"):
                            $ Line = "love"
                        else:
                            $ LauraX.FaceChange("sadside")
                            ch_l "Ну а я больше в этом не уверена. . ."
                    "Прости, я не хотел так говорить." if Player.Male:
                        $ LauraX.Eyes = "surprised"
                        ch_l "О, серьезно?"
                        ch_l "Как удобно."
                        ch_p "Я люблю тебя, [LauraX.Name]."
                        $ LauraX.Statup("Love", 200, 10)
                        if ApprovalCheck(LauraX, 950, "L"):
                            $ Line = "love"
                        else:
                            $ LauraX.FaceChange("sadside")
                            ch_l "Ну а я больше в этом не уверена. . ."
                    "Я передумала, я люблю тебя, так что. . ." if not Player.Male:
                        if ApprovalCheck(LauraX, 950, "L"):
                            $ Line = "love"
                            ch_l "Ну вот и отлично."
                        else:
                            $ LauraX.Mouth = "sad"
                            ch_l "Рада за тебя."
                            $ LauraX.Statup("Inbt", 90, 10)
                            $ LauraX.FaceChange("sadside")
                            ch_l "Жаль, не могу ответить тем же. . ."
                    "Я передумал, я люблю тебя, так что. . ." if Player.Male:
                        if ApprovalCheck(LauraX, 950, "L"):
                            $ Line = "love"
                            ch_l "Ну вот и отлично."
                        else:
                            $ LauraX.Mouth = "sad"
                            ch_l "Рада за тебя."
                            $ LauraX.Statup("Inbt", 90, 10)
                            $ LauraX.FaceChange("sadside")
                            ch_l "Жаль, не могу ответить тем же. . ."
                    "Эм, неважно.":
                            $ LauraX.Statup("Love", 200, -30)
                            $ LauraX.Statup("Obed", 50, 10)
                            $ LauraX.FaceChange("angry")
                            ch_l "Ох, да иди ты нахуй."
                            $ LauraX.RecentActions.append("angry")
                            $ LauraX.DailyActions.append("angry")
        if Line == "love":
                $ LauraX.Statup("Love", 200, 40)
                $ LauraX.Statup("Obed", 90, 10)
                $ LauraX.Statup("Inbt", 90, 10)
                $ LauraX.FaceChange("smile")
                if not Player.Male:
                    ch_l "Я рада, что ты пришла в себя."
                else:
                    ch_l "Я рада, что ты пришел в себя."
                ch_l "Я тоже тебя люблю, [LauraX.Petname]!"
                if LauraX.Event[6] < 25:
                        $ LauraX.FaceChange("sly")
                        "Она берет вас за затылок и притягивает к себе."
                        ch_l "В следующий раз не заставляй меня ждать."
                $ LauraX.Petnames.append("lover")
        $ LauraX.Event[6] = 25
        return

# end Laura_Love//////////////////////////////////////////////////////////


# start Laura_Sub//////////////////////////////////////////////////////////

label Laura_Sub:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(LauraX,"bemused","выглядит тихой. . .")
            return
    $ LauraX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    call Shift_Focus(LauraX)
    if LauraX.Loc != bg_current and LauraX not in Party:
        "Вдруг [LauraX.Name] подходит к вам с явным желанием поговорить."

    $ Event_Queue = [0,0]
    $ LauraX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(LauraX)
    call CleartheRoom(LauraX)
    call Set_The_Scene
    call Taboo_Level
    $ LauraX.DailyActions.append("relationship")
    $ LauraX.FaceChange("bemused", 1)
    if not Player.Male and "girltalk" not in LauraX.History:
            call expression LauraX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
            return

    $ Line = 0
    ch_l "Я тут кое-что заметила."
    ch_l "В последнее время ты пытаешься мной командовать."
    menu:
        ch_l "В последнее время ты пытаешься мной командовать.{w=2.8}{nw}"
        "Верно. Для меня это естественно.":
                pass
        "Извини, не думала, что веду себя так." if not Player.Male:
                pass
        "Извини, не думал, что веду себя так." if Player.Male:
                pass
        "Ага. Смирись.":
                pass
    "Прежде, чем вы успеваете заговорить, она закрывает вам рот рукой."
    $ LauraX.FaceChange("sly", 1,Eyes="side")
    ch_l "Не знаю, как к этому относиться."
    if LauraX.Event[6]: #if you've done the Love route
            $ LauraX.FaceChange("sadside", 1)
            ch_l "Ты знаешь, какое у меня было прошлое, с этим учреждением, с. . . "
            ch_l ". . . работой, которую я выполняла для них."
            $ LauraX.FaceChange("sad", 1)
            ch_l "Я не уверена, хочу ли я, чтобы кто-нибудь снова указывал мне, что делать."
    menu Laura_Sub_Question:
        extend ""
        "Я хочу продолжать вести себя так.":
                $ LauraX.FaceChange("sly", 1)
                $ LauraX.Statup("Obed", 200, 10)
                $ LauraX.Statup("Inbt", 50, 5)
        "Я не хочу больше вести себя так.":
                $ LauraX.FaceChange("sly", 1)
                $ LauraX.Statup("Love", 80, 5)
                $ LauraX.Statup("Obed", 200, -5)
                $ LauraX.Statup("Inbt", 50, -5)
                if not Player.Male:
                    ch_l "Я понимаю, ты просто была слишком настойчивой. . ."
                else:
                    ch_l "Я понимаю, ты просто был слишком настойчивым. . ."
        "Напомнишь мне о учереждение?" if LauraX.Event[6] and Line != "facility":
                $ LauraX.FaceChange("sadside", 1)
                $ LauraX.Statup("Love", 99, -10)
                $ LauraX.Statup("Inbt", 50, -5)
                ch_l "Как я уже говорила, я выросла в подпольной правительственной лаборатории."
                ch_l "Они приказывали мне убивать людей для них."
                $ LauraX.FaceChange("sly", 0, Brows= "angry")
                ch_l ". . . пока мне не надоело подчиняться приказам."
                $ Line = "facility"
                jump Laura_Sub_Question
        "Что такого в том, что тебе велят что-либо делать?" if not LauraX.Event[6] and Line != "facility":
                $ LauraX.FaceChange("sadside", 1)
                $ LauraX.Statup("Love", 80, 5)
                ch_l "У меня просто уже был неприятный опыт."
                ch_l "Тебе не нужно о нем знать."
                ch_l ". . ."
                $ LauraX.FaceChange("sad", 0)
                ch_l "Скажем так, мне приказывали делать то, о чем я сожалею."
                $ Line = "facility"
                jump Laura_Sub_Question
        "А теперь, перейдем к нашей программе.":
                if ApprovalCheck(LauraX, 1000, "LO"):
                        $ LauraX.FaceChange("sly", 1)
                        $ LauraX.Statup("Obed", 200, 20)
                        $ LauraX.Statup("Inbt", 50, 10)
                        ch_l "Хмммм. . ."
                else:
                        $ LauraX.Statup("Love", 200, -10)
                        $ LauraX.Statup("Inbt", 50, -5)
                        $ LauraX.FaceChange("angry",0)
                        ch_l "Не очень хорошее начало. Тебе стоит пересмотреть свое отношение."
                        menu:
                            extend ""
                            "Извини, мне показалось, что тебе понравится.":
                                    $ LauraX.FaceChange("perplexed", 1,Eyes="side")
                                    $ LauraX.Eyes = "side"
                                    $ LauraX.Statup("Love", 75, 10)
                                    $ LauraX.Statup("Obed", 200, 5)
                                    $ LauraX.Statup("Inbt", 50, 5)
                                    ch_l ". . . после того, что я сказала. . ."
                                    $ LauraX.FaceChange("sly", 1)
                                    ch_l "Ладно, неважно."
                            "Мне все равно на твое мнение.":
                                    $ LauraX.Statup("Love", 95, -10)
                                    ch_l "По тебе видно."
                                    $ Line = "rude"
    if Line == "facility":
            $ Line = 0

    if not Line:
            # She's advancing to the next stage
            $ LauraX.FaceChange("sly", 1)
            ch_l "Послушай. . ."
            $ LauraX.FaceChange("sly", 2)
            ch_l ". . . не то чтобы я совсем это ненавидела."
            $ LauraX.FaceChange("smile", 1, Eyes="side")
            ch_l ". . . честно говоря, думаю, подобное вызывает у меня. . ."
            menu:
                extend ""
                "-возбуждение?":
                    $ LauraX.Statup("Obed", 200, 5)
                    $ LauraX.Statup("Inbt", 50, 5)
                    ch_l ". . ."
                    $ LauraX.FaceChange("sly", 1)
                    $ LauraX.Statup("Lust", 50, 10)
                    ch_l "ага, немного."
                "-отвращение?":
                    $ LauraX.Statup("Love", 75, -5)
                    $ LauraX.Statup("Obed", 200, -5)
                    $ LauraX.FaceChange("sadside", 1)
                    ch_l ". . . типа того,"
                    $ LauraX.FaceChange("sly", 1)
                    $ LauraX.Statup("Inbt", 70, 5)
                    $ LauraX.Statup("Lust", 50, 5)
                    ch_l "но отчасти и возбуждение."
                "-голод?":
                    $ LauraX.FaceChange("confused", 1,Eyes="surprised",Mouth="smile")
                    $ LauraX.Statup("Obed", 200, -5)
                    $ LauraX.Statup("Inbt", 50, -5)
                    ch_l "?!"
                    $ LauraX.FaceChange("confused", 1,Eyes="normal",Mouth="smile")
                    ch_l "Эм. . . что?. . . Я бы скорее сказала-"
                    $ LauraX.FaceChange("sly", 1)
                    $ LauraX.Statup("Lust", 50, 5)
                    ch_l ". . .возбуждение."
                "-похоть?":
                    $ LauraX.Statup("Obed", 200, 10)
                    $ LauraX.Statup("Inbt", 50, 5)
                    $ LauraX.FaceChange("startled", 2,Mouth="lipbite")
                    ch_l "!"
                    $ LauraX.FaceChange("sly", 1, Eyes="side")
                    $ LauraX.Statup("Inbt", 50, 5)
                    $ LauraX.Statup("Lust", 50, 10)
                    $ LauraX.Statup("Lust", 70, 5)
                    ch_l "Да."
            menu:
                extend ""
                "Хорошо. Если ты хочешь быть со мной, то выполняй мои приказы.":
                        if ApprovalCheck(LauraX, 1000, "LO"):
                            $ LauraX.FaceChange("sly", 1)
                            $ LauraX.Statup("Obed", 200, 15)
                            $ LauraX.Statup("Inbt", 50, 10)
                            ch_l "Хммм. . ."
                        else:
                            $ LauraX.FaceChange("sadside", 1,Mouth="normal")
                            $ LauraX.Statup("Love", 200, -5)
                            $ LauraX.Statup("Obed", 200, 10)
                            ch_l "Думаю, тебе стоит умерить свой пыл, [LauraX.Petname]."
                            menu:
                                extend ""
                                "Плевать. Все так, как есть. Смирись или проваливай.":
                                        $ LauraX.FaceChange("angry")
                                        $ LauraX.Statup("Love", 200, -10)
                                        $ LauraX.Statup("Obed", 200, 5)
                                        ch_l "Мне кажется, ты заходишь слишком далеко, [LauraX.Petname]."
                                        $ Line = "rude"
                                "Ладно, это можно устроить.":
                                        $ LauraX.FaceChange("bemused", 1)
                                        $ LauraX.Statup("Love", 95, 5)
                                        $ LauraX.Statup("Inbt", 50, 5)
                                        ch_l "-но слишком не увлекайся."

                "М? Ты находишь это сексуальным?":
                                        $ LauraX.FaceChange("bemused", 2,Eyes="side")
                                        $ LauraX.Statup("Obed", 200, 5)
                                        $ LauraX.Statup("Inbt", 50, 10)
                                        ch_l ". . ."
                                        $ LauraX.Statup("Lust", 50, 5)
                                        ch_l "Ага."

                "Ты уверена, что не хочешь, чтобы я немного сбавила обороты?" if not Player.Male:
                        $ LauraX.FaceChange("startled", 1,Eyes="squint")
                        $ LauraX.Statup("Obed", 200, -5)
                        menu:
                            ch_l "Уверена. . ."
                            "Ладно, раз ты не против.":
                                $ LauraX.FaceChange("bemused", 1)
                                $ LauraX.Statup("Love", 95, 10)
                                $ LauraX.Statup("Inbt", 50, 10)
                                $ Line = 0
                            "Эм. . . Я думаю это слишком странно. Извини.":
                                $ LauraX.FaceChange("sad", 1, Eyes="surprised")
                                $ LauraX.Statup("Love", 200, -15)
                                $ LauraX.Statup("Obed", 200, -5)
                                $ LauraX.Statup("Inbt", 50, -10)
                                $ Line = "embarrassed"

                "Ты уверена, что не хочешь, чтобы я немного сбавил обороты?" if Player.Male:
                        $ LauraX.FaceChange("startled", 1,Eyes="squint")
                        $ LauraX.Statup("Obed", 200, -5)
                        menu:
                            ch_l "Уверена. . ."
                            "Ладно, раз ты не против.":
                                $ LauraX.FaceChange("bemused", 1)
                                $ LauraX.Statup("Love", 95, 10)
                                $ LauraX.Statup("Inbt", 50, 10)
                                $ Line = 0
                            "Эм. . . Я думаю это слишком странно. Извини.":
                                $ LauraX.FaceChange("sad", 1, Eyes="surprised")
                                $ LauraX.Statup("Love", 200, -15)
                                $ LauraX.Statup("Obed", 200, -5)
                                $ LauraX.Statup("Inbt", 50, -10)
                                $ Line = "embarrassed"

                "Меня не волнует, что тебе хочется. Я делаю то, что хочу.":
                                $ LauraX.Statup("Love", 200, -10)
                                $ LauraX.Statup("Obed", 200, 15)
                                $ LauraX.FaceChange("angry")
                                ch_l "Мне кажется, ты заходишь слишком далеко, [LauraX.Petname]."
                                $ Line = "rude"

    if not Line:
        $ LauraX.FaceChange("bemused", 1,Eyes = "down")
        ch_l "Так вот, я готова попробовать."
        ch_l "Просто пробный период, посмотрим, как пойдет."
        ch_l "Говори мне, что ты хочешь, и. . . я попробую об этом позаботиться."
        menu Laura_Sub_Choice:
            extend ""
            "Думаю, я смогу привыкнуть к таким отношениям.":
                    $ LauraX.Statup("Obed", 200, 5)
                    $ LauraX.Statup("Inbt", 50, 5)
                    $ LauraX.FaceChange("sly", 1)
                    $ Line = 0
            "Ты не считаешь такие отношения несколько. . . ненормальными?":
                    $ LauraX.FaceChange("sad", 1, Eyes="surprised")
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Inbt", 50, -15)
                    $ Line = "embarrassed"

    if not Line:
        $ LauraX.FaceChange("smile", 1)
        if not Player.Male:
            ch_l "Клево. Итак, тебе что-нибудь нужно. . . госпожа?"
        else:
            ch_l "Клево. Итак, тебе что-нибудь нужно. . . господин?"
        menu:
            extend ""
            "А мне нравится, как ты меня зовешь.":
                    $ LauraX.Statup("Love", 95, 5)
                    $ LauraX.Statup("Obed", 200, 15)
                    $ LauraX.Statup("Inbt", 50, 5)
                    if not Player.Male:
                        ch_l "Поняла, госпожа."
                    else:
                        ch_l "Поняла, господин."
                    if not Player.Male:
                        $ LauraX.Petname = "госпожа"
                        $ LauraX.Petname_rod = "госпожи"
                        $ LauraX.Petname_dat = "госпоже"
                        $ LauraX.Petname_vin = "госпожу"
                        $ LauraX.Petname_tvo = "госпожой"
                        $ LauraX.Petname_pre = "госпоже"
                    else:
                        $ LauraX.Petname = "господин"
                        $ LauraX.Petname_rod = "господина"
                        $ LauraX.Petname_dat = "господину"
                        $ LauraX.Petname_vin = "господина"
                        $ LauraX.Petname_tvo = "господином"
                        $ LauraX.Petname_pre = "господине"
            "Не надо меня так звать, ладно?":
                $ LauraX.FaceChange("perplexed", 1)
                ch_l "Хм. Ладно."
                $ LauraX.Statup("Inbt", 50, -5)
                $ LauraX.FaceChange("sly", 1,Eyes="side")
                menu:
                    ch_l "Но ты же будешь отдавать мне приказы, да?"
                    "Да, без проблем.":
                            $ LauraX.Statup("Obed", 200, 10)
                            $ LauraX.FaceChange("smile", 1)
                            ch_l "Хорошо."
                    "От этого мне становится как-то не по себе. . .":
                            $ LauraX.FaceChange("sad", 1, Eyes="side")
                            $ LauraX.Statup("Love", 200, -10)
                            $ LauraX.Statup("Obed", 200, -30)
                            $ LauraX.Statup("Inbt", 50, -15)
                            $Line = "embarrassed"

#Laura_Sub_Bad_End:
    $ LauraX.History.append("sir")
    if not Line:
            $ LauraX.Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif Line == "rude":
            call Remove_Girl(LauraX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[LauraX.Name] проходит мимо вас и уходит прочь."
    elif Line == "embarrassed":
            $ LauraX.FaceChange("sadside", 2)
            ch_l "Ну ладно, раз тебе не интересно. . ."
            hide Laura_Sprite with easeoutright
            call Remove_Girl(LauraX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[LauraX.Name] выходит из комнаты."
    return

label Laura_Sub_Asked:
    $ Line = 0
    call Shift_Focus(LauraX)
    $ LauraX.FaceChange("sadside", 1)
    ch_l "Ага. И, похоже, тебе не понравилась эта идея."
    menu:
        extend ""
        "Я хочу извиниться. Надеюсь, мы можем попробовать еще раз.":
                if "sir" in LauraX.Petnames and ApprovalCheck(LauraX, 850, "O"):
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck(LauraX, 550, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        pass
                else: #if it failed both those things,
                        $ LauraX.FaceChange("angry", 1)
                        ch_l "Не беспокойся, это была плохая идея." #Failed again. :(
                        $ Line = "rude"

                if Line != "rude":
                        $ LauraX.Statup("Love", 90, 10)
                        $ LauraX.FaceChange("sly", 1)
                        if not Player.Male:
                            ch_l "Ну, хоть ты все равно не переставала мной командовать."
                        else:
                            ch_l "Ну, хоть ты все равно не переставал мной командовать."
                        ch_l "Я готова попробовать еще раз."

        "Я знаю, что ты этого хочешь. Попробуем еще раз или нет?":
                $ LauraX.FaceChange("bemused", 1)
                if "sir" in LauraX.Petnames:
                    if ApprovalCheck(LauraX, 850, "O"):
                        ch_l "Ладно, хорошо."
                    else:
                        ch_l "Нет, мне и так хорошо."
                        $ Line = "rude"
                elif ApprovalCheck(LauraX, 600, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        $ LauraX.FaceChange("confused", 1)
                        ch_l "Хоть мне это не совсем нравится."
                        $ LauraX.FaceChange("sly", 1)
                        if not Player.Male:
                            ch_l "Но, может, ты и права."
                            ch_l "Ты точно уверена, что готова?"
                        else:
                            ch_l "Но, может, ты и прав."
                            ch_l "Ты точно уверен, что готов?"
                        menu:
                            extend ""
                            "Да, извини, что я была довольно груба." if not Player.Male:
                                            $ LauraX.Statup("Love", 90, 15)
                                            $ LauraX.Statup("Inbt", 50, 10)
                                            $ LauraX.FaceChange("bemused", 1)
                                            $ LauraX.Eyes = "side"
                                            ch_l "Ну, тогда ладно."
                            "Да, извини, что я был довольно груб." if Player.Male:
                                            $ LauraX.Statup("Love", 90, 15)
                                            $ LauraX.Statup("Inbt", 50, 10)
                                            $ LauraX.FaceChange("bemused", 1)
                                            $ LauraX.Eyes = "side"
                                            ch_l "Ну, тогда ладно."
                            "Ты охуеть как права, сучка.":
                                    if "sir" in LauraX.Petnames and ApprovalCheck(LauraX, 900, "O"):
                                            $ LauraX.Statup("Love", 200, -5)
                                            $ LauraX.Statup("Obed", 200, 10)
                                            ch_l ". . ."
                                    elif ApprovalCheck(LauraX,700, "O"):
                                            $ LauraX.Statup("Love", 200, -5)
                                            $ LauraX.Statup("Obed", 200, 10)
                                            ch_l "Хмммм. . ."
                                    else: #if it failed both those things,
                                            $ LauraX.Statup("Love", 200, -10)
                                            $ LauraX.Statup("Obed", 90, -10)
                                            $ LauraX.Statup("Obed", 200, -10)
                                            $ LauraX.Statup("Inbt", 50, -15)
                                            $ LauraX.FaceChange("angry", 1)
                                            ch_l "Ого, это уже слишком."
                                            $ Line = "rude"
                            "Ладно, тогда не бери в голову.":
                                            $ LauraX.FaceChange("angry", 1)
                                            $ LauraX.Statup("Love", 200, -10)
                                            $ LauraX.Statup("Obed", 90, -10)
                                            $ LauraX.Statup("Obed", 200, -10)
                                            $ LauraX.Statup("Inbt", 50, -15)
                                            ch_l "Я думала, что буду выполнять твои команды, а не играть в эти игры."
                                            ch_l "Я должна была догадаться, что все будет именно так."
                                            $ Line = "rude"

    $ LauraX.RecentActions.append("asked sub")
    $ LauraX.DailyActions.append("asked sub")
    if Line == "rude":
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Laura_Sprite with easeoutright
            call Remove_Girl(LauraX)
            $ LauraX.RecentActions.append("angry")
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[LauraX.Name], не отводя от вас взгляда, выходит из комнаты."
    elif "sir" in LauraX.Petnames:
            #it didn't fail and "sir" was covered
            $ LauraX.Statup("Obed", 200, 50)
            $ LauraX.Petnames.append("master")
            if not Player.Male:
                $ LauraX.Petname = "хозяйка"
                $ LauraX.Petname_rod = "хозяйки"
                $ LauraX.Petname_dat = "хозяйке"
                $ LauraX.Petname_vin = "хозяйку"
                $ LauraX.Petname_tvo = "хозяйкой"
                $ LauraX.Petname_pre = "хозяйке"
            else:
                $ LauraX.Petname = "хозяин"
                $ LauraX.Petname_rod = "хозяина"
                $ LauraX.Petname_dat = "хозяину"
                $ LauraX.Petname_vin = "хозяина"
                $ LauraX.Petname_tvo = "хозяином"
                $ LauraX.Petname_pre = "хозяине"
            $ LauraX.Eyes = "sly"
            if not Player.Male:
                ch_l ". . . хозяйка. . ."
            else:
                ch_l ". . . хозяин. . ."
    else:
            #it didn't fail
            $ LauraX.Statup("Obed", 200, 30)
            $ LauraX.Petnames.append("sir")
            if not Player.Male:
                $ LauraX.Petname = "госпожа"
                $ LauraX.Petname_rod = "госпожи"
                $ LauraX.Petname_dat = "госпоже"
                $ LauraX.Petname_vin = "госпожу"
                $ LauraX.Petname_tvo = "госпожой"
                $ LauraX.Petname_pre = "госпоже"
            else:
                $ LauraX.Petname = "господин"
                $ LauraX.Petname_rod = "господина"
                $ LauraX.Petname_dat = "господину"
                $ LauraX.Petname_vin = "господина"
                $ LauraX.Petname_tvo = "господином"
                $ LauraX.Petname_pre = "господине"
            $ LauraX.FaceChange("sly", 1)
            if not Player.Male:
                ch_l ". . . госпожа."
            else:
                ch_l ". . . господин."
    return

# end Laura_Sub//////////////////////////////////////////////////////////


# start Laura_Master//////////////////////////////////////////////////////////

label Laura_Master:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(LauraX,"bemused","выглядит необычайно покорной. . .")
            return
    $ LauraX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    call Shift_Focus(LauraX)
    if LauraX.Loc != bg_current and LauraX not in Party:
        "Вдруг [LauraX.Name] подходит к вам с явным желанием поговорить."

    $ Event_Queue = [0,0]
    $ LauraX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(LauraX)
    call CleartheRoom(LauraX)
    call Set_The_Scene
    $ LauraX.DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ LauraX.FaceChange("sly", 1)
    ch_l "[LauraX.Petname]. . ."
    ch_l ". . . я хочу откровенно поговорить. . ."
    menu:
        extend ""
        "Хорошо.":
            $ LauraX.Statup("Obed", 200, 5)
            $ LauraX.Statup("Inbt", 50, 5)
        "О чем?":
            ch_l "Кое о чем. . ."
            $ LauraX.Eyes = "side"
            ch_l ". . . личном."
            $ LauraX.Eyes = "squint"
            menu:
                extend ""
                "Ох, ладно, начинай.":
                    $ LauraX.Statup("Love", 80, 5)
                    $ LauraX.Statup("Obed", 200, 5)
                    ch_l "Хорошо. . ."
                "Ох, тогда нет.":
                    $ LauraX.FaceChange("sad", 1)
                    $ LauraX.Statup("Love", 80, -5)
                    $ LauraX.Statup("Obed", 200, -10)
                    $ Line = "embarrassed"
        "Нет.":
            $ LauraX.FaceChange("perplexed", 1,Brows="confused")
            $ LauraX.Statup("Love", 80, -5)
            $ LauraX.Statup("Obed", 200, -5)
            $ LauraX.Statup("Inbt", 50, -5)
            if not Player.Male:
                ch_l "-ты уверена?"
            else:
                ch_l "-ты уверен?"
            menu:
                extend ""
                "Ох, ладно, начинай.":
                    $ LauraX.FaceChange("confused", 1)
                    $ LauraX.Statup("Obed", 200, 10)
                    $ LauraX.Statup("Inbt", 60, 10)
                    ch_l "Хорошо. . ."
                "Да, мне это не интересно.":
                    $ LauraX.FaceChange("sad", 1)
                    $ LauraX.Statup("Love", 80, -5)
                    $ LauraX.Statup("Inbt", 50, -10)
                    $ Line = "embarrassed"


    if not Line:
        $ LauraX.FaceChange("sly", 1)
        if not Player.Male:
            ch_l "Думаю, мне нравится, когда ты за главную."
        else:
            ch_l "Думаю, мне нравится, когда ты за главного."
        ch_l "Это придает мне. . . целостность. . ."
        menu:
            extend ""
            "Мне тоже нравится.":
                    $ LauraX.FaceChange("sly", 1)
                    $ LauraX.Statup("Obed", 200, 5)
                    ch_l "Хорошо. Тогда, может, мы могли бы относиться к этому чуть более серьезно?"
                    menu:
                        extend ""
                        "Нет. Все и так идеально.":
                                $ LauraX.FaceChange("sad", 1)
                                $ LauraX.Statup("Obed", 200, -15)
                                $ LauraX.Statup("Love", 80, 10)
                                $ Line = "fail"
                        "Что ты имеешь в виду?":
                                $ LauraX.Eyes = "side"
                                if not Player.Male:
                                    ch_l "Я подумала и решила, что готова звать тебя. . . {i}хозяйкой{/i}?"
                                else:
                                    ch_l "Я подумала и решила, что готова звать тебя. . . {i}хозяином{/i}?"
                                $ LauraX.Eyes = "squint"
                                menu:
                                    extend ""
                                    "О да. Мне нравится.":
                                            $ LauraX.Statup("Obed", 200, 5)
                                            ch_l "Хорошо. . ."
                                    "Эм. . . нет.  Это слишком.":
                                            $ LauraX.FaceChange("sadside", 1)
                                            $ LauraX.Statup("Obed", 200, -15)
                                            $ LauraX.Statup("Inbt", 50, 5)
                                            $ Line = "fail"

                        "Честно говоря, мне бы хотелось перестать держать все под контролем.":
                                $ LauraX.FaceChange("sad", 1)
                                $ LauraX.Statup("Love", 200, -5)
                                $ LauraX.Statup("Obed", 200, -10)
                                $ LauraX.Statup("Inbt", 50, 15)
                                $ Line = "fail"

                        "Знаешь, давай все прекратим. Меня это начинает пугать.":
                                $ LauraX.FaceChange("angry", 2, Eyes="surprised")
                                $ LauraX.Statup("Love", 200, -10)
                                $ LauraX.Statup("Obed", 200, -50)
                                $ LauraX.Statup("Inbt", 50, -15)
                                ch_l "Ни слова больше, я не хочу ПУГАТЬ ТЕБЯ."
                                $ Line = "embarrassed"

            "Как будто меня волнует твое мнение, шлюха.":
                    $ LauraX.FaceChange("angry", 1, Mouth="smile")
                    $ LauraX.Statup("Love", 90, -20)
                    $ LauraX.Statup("Obed", 200, 10)
                    $ LauraX.Statup("Inbt", 50, -10)
                    ch_l ". . ."
                    menu:
                        ch_l "Эм. . . что это сейчас было?"
                        "Извиняюсь. Мне просто все равно, чего ты хочешь.":
                                if ApprovalCheck(LauraX, 1400, "LO"):
                                        $ LauraX.Statup("Obed", 200, 10)
                                        ch_l ". . ."
                                        $ LauraX.FaceChange("sly", 1)
                                        $ LauraX.Statup("Love", 200, 20)
                                        $ LauraX.Statup("Inbt", 50, 15)
                                        ch_l ". . .-продолжай-. . ."
                                else:
                                        $ LauraX.Statup("Love", 200, -15)
                                        $ LauraX.Statup("Obed", 200, -10)
                                        $ LauraX.Statup("Inbt", 50, 5)
                                        $ LauraX.FaceChange("angry", 1)
                                        ch_l "!!!"
                                        $ Line = "rude"

                        "Извини. Я просто пытаюсь быть более -властной-. Я думала тебе понравится. Это перебор?" if not Player.Male:
                                $ LauraX.Statup("Love", 200, 10)
                                $ LauraX.Statup("Obed", 200, 10)
                                $ LauraX.Statup("Inbt", 50, 5)
                                if ApprovalCheck(LauraX, 1400, "LO"):
                                        $ LauraX.Statup("Obed", 200, 10)
                                        ch_l ". . ."
                                        $ LauraX.FaceChange("sly", 1)
                                        $ LauraX.Statup("Love", 200, 20)
                                        $ LauraX.Statup("Inbt", 50, 15)
                                        ch_l ". . .-нет, примерно так и должно быть-. . ."
                                else:
                                        $ LauraX.Statup("Love", 200, 5)
                                        $ LauraX.Statup("Obed", 200, -5)
                                        $ LauraX.Statup("Inbt", 50, 5)
                                        $ LauraX.FaceChange("angry", 1, Eyes="side")
                                        ch_l ". . ."
                                        ch_l "Мы еще поработаем над этим. . ."

                        "Извини. Я просто пытаюсь быть более -властным-. Я думал тебе понравится. Это перебор?" if Player.Male:
                                $ LauraX.Statup("Love", 200, 10)
                                $ LauraX.Statup("Obed", 200, 10)
                                $ LauraX.Statup("Inbt", 50, 5)
                                if ApprovalCheck(LauraX, 1400, "LO"):
                                        $ LauraX.Statup("Obed", 200, 10)
                                        ch_l ". . ."
                                        $ LauraX.FaceChange("sly", 1)
                                        $ LauraX.Statup("Love", 200, 20)
                                        $ LauraX.Statup("Inbt", 50, 15)
                                        ch_l ". . .-нет, примерно так и должно быть-. . ."
                                else:
                                        $ LauraX.Statup("Love", 200, 5)
                                        $ LauraX.Statup("Obed", 200, -5)
                                        $ LauraX.Statup("Inbt", 50, 5)
                                        $ LauraX.FaceChange("angry", 1, Eyes="side")
                                        ch_l ". . ."
                                        ch_l "Мы еще поработаем над этим. . ."

            "Это до жути странно.":
                                $ LauraX.FaceChange("sad", 2)
                                $ LauraX.Statup("Love", 200, -20)
                                $ LauraX.Statup("Obed", 200, -20)
                                $ LauraX.Statup("Inbt", 50, -10)
                                $ Line = "embarrassed"

    $ LauraX.History.append("master")
    if Line == "rude":
            $ LauraX.RecentActions.append("angry")
            hide Laura_Sprite with easeoutright
            call Remove_Girl(LauraX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[LauraX.Name] выбегает из комнаты."
    elif Line == "embarrassed":
            ch_l "Тогда ладно."
            ch_l "А я уже собиралась поднять твой \"уровень допуска.\""
            hide Laura_Sprite with easeoutright
            call Remove_Girl(LauraX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[LauraX.Name] проходит мимо вас и уходит."
    elif Line == "fail":
            ch_l "Ох. . ."
            ch_l "Думаю, это нормально."
    else:
            $ LauraX.Statup("Obed", 200, 50)
            $ LauraX.Petnames.append("master")
            if not Player.Male:
                $ LauraX.Petname = "хозяйка"
                $ LauraX.Petname_rod = "хозяйки"
                $ LauraX.Petname_dat = "хозяйке"
                $ LauraX.Petname_vin = "хозяйку"
                $ LauraX.Petname_tvo = "хозяйкой"
                $ LauraX.Petname_pre = "хозяйке"
            else:
                $ LauraX.Petname = "хозяин"
                $ LauraX.Petname_rod = "хозяина"
                $ LauraX.Petname_dat = "хозяину"
                $ LauraX.Petname_vin = "хозяина"
                $ LauraX.Petname_tvo = "хозяином"
                $ LauraX.Petname_pre = "хозяине"
            if not Player.Male:
                ch_l ". . .хозяйка."
            else:
                ch_l ". . .хозяин."
    return

# end Laura_Master//////////////////////////////////////////////////////////



# start Laura_Sexfriend//////////////////////////////////////////////////////////

label Laura_Sexfriend:   #Laura_Update
        #set this to occur after class
        $ LauraX.Lust = 70
        if LauraX.Loc != bg_current:
                "[LauraX.Name] подходит к вам и отводит в сторону. Кажется, ее слегка трясет."
        else:
                "[LauraX.Name] поворачивается к вам."
        $ LauraX.Loc = bg_current
        $ LauraX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ Event_Queue = [0,0]
        call Shift_Focus(LauraX)
        call Set_The_Scene
        $ LauraX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in LauraX.History:
                call expression LauraX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        $ Line = 0
        $ LauraX.FaceChange("sly",2,Eyes="side")
        "Она мнется и потирает одной ногой о другую."
        $ LauraX.Petnames.append("sex friend")
        $ LauraX.FaceChange("sly",2)
        if LauraX in Player.Harem:
                ch_l "Слушай."
                ch_l "Мне нужно поговорить с тобой наедине."
        elif "lover" in LauraX.Petnames or "master" in LauraX.Petnames or "sir" in LauraX.Petnames:
                #if you have done the lover thing
                ch_l "Слушай."
                ch_l "Мне нужно поговорить с тобой наедине."
        else:
                #if you've done no relationship stuff yet. . .
                ch_l "Слушай. . . так вот. . . "
                if LauraX.SEXP >= 50:
                    ch_l "Я знаю, что у нас свободные отношения и все такое. . ."
                else:
                    ch_l "Может быть, это покажется немного странным, но. . ."
                ch_l "Я бы очень хотела просто заниматься сексом."
                ch_l "С тобой."
                menu:
                    extend ""
                    "Я только за":
                        $ LauraX.FaceChange("sly",2,Mouth="smile")
                        $Line = "yes"
                    "Нет, спасибо":
                        $ LauraX.FaceChange("confused",2)
                        $Line = "no"
                    ". . .":
                        $ LauraX.Statup("Obed", 90, 5)
                        $ LauraX.FaceChange("confused",2)

                if not Line:
                        ch_l "Если это, конечно, возможно. . ."
                        menu:
                            extend ""
                            "Конечно":
                                $ LauraX.FaceChange("sly",2,Mouth="smile")
                                $Line = "yes"
                            "Нет, спасибо":
                                $ LauraX.FaceChange("confused",2)
                                $Line = "no"

                if Line == "no":
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 80, 5)
                    ch_l "Что? Почему?"
                    menu:
                        extend ""
                        "Ладно, уговорила":
                            $ LauraX.FaceChange("confused",2,Mouth="smile")
                            ch_l "Обожаю тебя."
                            $Line = "yes"
                        "Мне это не интересно":
                            $ LauraX.FaceChange("confused",2)

                        "У меня уже кое-кто есть":
                            $ LauraX.Statup("Love", 95, -5)
                            $ LauraX.Statup("Obed", 90, 5)
                            if Player.Harem:
                                    $ LauraX.FaceChange("surprised",2)
                                    ch_l "Это [Player.Harem[0].Name]?"
                                    $ LauraX.GLG(Player.Harem[0],600,-25,1)
                            $ LauraX.FaceChange("sly",2)
                            ch_l "Ей не нужно об этом знать. . ."
                            menu:
                                extend ""
                                "Ладно, уговорила":
                                        ch_l "Обожаю тебя."
                                        $ Line = "yes"
                                "Я все равно не согласна" if not Player.Male:
                                        pass
                                "Я все равно не согласен" if Player.Male:
                                        pass

        if Line == "no":
                    $ LauraX.Statup("Love", 200, -10)
                    $ LauraX.Statup("Obed", 90, 15)
                    $ LauraX.Statup("Inbt", 90, 10)
                    $ LauraX.FaceChange("sad",2)
                    ch_l "Серьезно?"
                    ch_l "Облом."
                    ch_l "Дай мне знать если передумаешь."
                    $ LauraX.FaceChange("sadside",2,Mouth="lipbite",Brows="angry")
                    if Player.Harem:
                            ch_l "Интересно, занята ли сейчас [Player.Harem[0].Name]. . ."
                            $ LauraX.GLG(Player.Harem[0],500,25,1)
                    else:
                            ch_l "Интересно, занята ли сейчас Китти. . ."
                            $ LauraX.GLG("Kitty",500,25,1)
        else:
                $ LauraX.Statup("Love", 90, 10)
                $ LauraX.Statup("Obed", 90, 5)
                $ LauraX.Statup("Inbt", 90, 15)
                $ LauraX.FaceChange("sly",1,Mouth="smile")
                if Taboo:
                    ch_l "Может, пройдем в другое место?"
                    menu:
                        extend ""
                        "Ага":
                                ch_l "Тогда пошли."
                                if bg_current == "bg player":
                                        $ bg_current = "bg laura"
                                else:
                                        $ bg_current = "bg player"
                                $ LauraX.Loc = bg_current
                                $ Party = []
                                call Set_The_Scene
                                call CleartheRoom(LauraX)
                                call Set_The_Scene
                                $ Taboo = 0
                                $ LauraX.Taboo = 0

                        "Нет, давай сделаем это здесь.":
                                $ LauraX.Statup("Obed", 80, 5)
                                $ LauraX.Statup("Inbt", 90, 15)
                                if not Player.Male:
                                    ch_l "Извращенка."
                                else:
                                    ch_l "Извращенец."

                $ Situation = LauraX
                $ Player.AddWord(1,"interruption") #adds to Recent
                call Girl_SexPrep              #she offers sex
                call SexMenu
                jump Misplaced

                #end "if no relationship"
        return

# end Laura_Sexfriend//////////////////////////////////////////////////////////


# start Laura_Fuckbuddy//////////////////////////////////////////////////////////

label Laura_Fuckbuddy:
        $ LauraX.DailyActions.append("relationship")
        $ LauraX.Lust = 80
        $ LauraX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        # Conditions, in your room, laura not there.
        "Вы слышите стук в дверь и идете ее открывать."
        #change laura's outfit to default
        $ Event_Queue = [0,0]
        $ LauraX.Loc = bg_current
        call Shift_Focus(LauraX)
        call Set_The_Scene(0)
        $ LauraX.Outfit = "casual1"
        $ LauraX.OutfitDay = "casual1"
        $ LauraX.OutfitChange("casual1")
        call Display_Girl(LauraX)
        call Taboo_Level
        $ Trigger = "masturbation"
#        $ Trigger3 = "fondle pussy"
        $ LauraX.Offhand = "fondle pussy"
        $ LauraX.FaceChange("sly",2,Mouth="lipbite")
        "[LauraX.Name] стоит в дверях с рукой в штанах."
        "Вы можете с уверенностью сказать, что она мастурбировала."
        $ Trigger = 0
#        $ Trigger3 = 0
        $ LauraX.Offhand = 0
        $ LauraX.ArmPose = 1
        "Она жадно оглядывает вас с головы до ног и вытаскивает руку из брюк."
        "Она протягивает руку и гладит ваше лицо, размазывая по нему свои соки."
        if not Player.Male:
            ch_l "Ты моя."
        else:
            ch_l "Ты мой."
        $ LauraX.Petnames.append("fuck buddy")
        $ LauraX.Event[10] += 1

        $ Situation = LauraX
        $ Player.AddWord(1,"interruption") #adds to Recent
        call Girl_SexPrep              #she offers sex
        call SexMenu
        return
# end Laura_Fuckbuddy//////////////////////////////////////////////////////////

# start Laura_Daddy//////////////////////////////////////////////////////////

#Not updated

label Laura_Daddy:       #Laura_Update
        $ LauraX.DailyActions.append("relationship")
        $ LauraX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(LauraX)
        if LauraX.Loc != bg_current:
                $ LauraX.Loc = bg_current
                "[LauraX.Name] подходит к вам."
        $ Event_Queue = [0,0]
        call Set_The_Scene
        ch_l ". . ."
        if LauraX in Player.Harem:
            ch_l "Итак, мы ведь уже встречаемся довольно давно?"
        else:
            ch_l "Нам вместе было достаточно весело, верно?"
        if LauraX.Love > LauraX.Obed and LauraX.Love > LauraX.Inbt:
            if not Player.Male:
                ch_l "И ты была очень добра ко мне. . ."
            else:
                ch_l "И ты был очень добр ко мне. . ."
        elif LauraX.Obed > LauraX.Inbt:
            if not Player.Male:
                ch_l "И ты хорошо повлияла на меня. . ."
            else:
                ch_l "И ты хорошо повлиял на меня. . ."
        elif LauraX in Player.Harem:
            ch_l "И нам было очень-очень весело. . ."
        else:
            ch_l "Я бы даже сказала, нам было очень-очень весело. . ."
        ch_l "Так вот, я тут подумала и. . . Ты, случайно, не хочешь, чтобы я звала тебя. . ."
        if not Player.Male:
            ch_l "\"мамочкой?\""
        else:
            ch_l "\"папочкой?\""
        menu:
            extend ""
            "Я не против?":
                $ LauraX.FaceChange("smile")
                $ LauraX.Statup("Love", 90, 20)
                $ LauraX.Statup("Obed", 60, 10)
                $ LauraX.Statup("Inbt", 80, 30)
                ch_l "Клево."
            "Зачем?":
                $ LauraX.FaceChange("bemused")
                if Player.Male:
                        ch_l "Я не знаю, хреновые люди заменяли мне отца. . ."
                else:
                        ch_l "Я не знаю, у меня было. . . тяжелое прошлое, связанное с моей мамой. . ."
                ch_l "Я просто. . ."
                if LauraX.Love > LauraX.Obed and LauraX.Love > LauraX.Inbt:
                    if Player.Male:
                        ch_l "Думаю, ты был бы куда лучше. . ."
                    else:
                        ch_l "Думаю, ты могла бы заполнить эту пустоту. . ."
                elif LauraX.Obed > LauraX.Inbt:
                        if not Player.Male:
                            ch_l "Ты всегда была такой решительной. . ."
                        else:
                            ch_l "Ты всегда был таким решительным. . ."
                else:
                        ch_l "Думаешь, это странно?"

                menu:
                    extend ""
                    "Звучит интересно, мне нравится.":
                            $ LauraX.FaceChange("smile")
                            $ LauraX.Statup("Love", 90, 15)
                            $ LauraX.Statup("Obed", 60, 20)
                            $ LauraX.Statup("Inbt", 80, 25)
                            ch_l "Отлично!"
                            $ LauraX.FaceChange("sly",2)
                            if not Player.Male:
                                ch_l " . . . мамочка."
                            else:
                                ch_l " . . . папочка."
                            $ LauraX.FaceChange("sly",1)
                            if not Player.Male:
                                $ LauraX.Petname = "мамочка"
                                $ LauraX.Petname_rod = "мамочки"
                                $ LauraX.Petname_dat = "мамочке"
                                $ LauraX.Petname_vin = "мамочку"
                                $ LauraX.Petname_tvo = "мамочкой"
                                $ LauraX.Petname_pre = "мамочке"
                            else:
                                $ LauraX.Petname = "папочка"
                                $ LauraX.Petname_rod = "папочки"
                                $ LauraX.Petname_dat = "папочке"
                                $ LauraX.Petname_vin = "папочку"
                                $ LauraX.Petname_tvo = "папочкой"
                                $ LauraX.Petname_pre = "папочке"
                    "Прошу, не надо.":
                            $ LauraX.Statup("Love", 90, 5)
                            $ LauraX.Statup("Obed", 80, 40)
                            $ LauraX.Statup("Inbt", 80, 20)
                            $ LauraX.FaceChange("sad")
                            ch_l "   . . .   "
                            ch_l "Ну, ладно."
                    "У тебя были непростые отношения с матерью, да?" if not Player.Male:
                            $ LauraX.Statup("Love", 90, -15)
                            $ LauraX.Statup("Obed", 80, 45)
                            $ LauraX.Statup("Inbt", 70, 5)
                            $ LauraX.FaceChange("angry")
                            ch_l "Да. . . я так и сказала."
                    "У тебя были непростые отношения с отцом, да?" if Player.Male:
                            $ LauraX.Statup("Love", 90, -15)
                            $ LauraX.Statup("Obed", 80, 45)
                            $ LauraX.Statup("Inbt", 70, 5)
                            $ LauraX.FaceChange("angry")
                            ch_l "Да. . . я так и сказала."
                    "Думаю, ты понимаешь как я могу \"заполнить эту пустоту.\"" if not Player.Male and LauraX.Love > LauraX.Obed and LauraX.Love > LauraX.Inbt:
                            $ LauraX.Statup("Love", 90, -15)
                            $ LauraX.Statup("Obed", 80, 45)
                            $ LauraX.Statup("Inbt", 70, 5)
                            $ LauraX.FaceChange("angry")
                            ch_l "Класс. . ."

            "У тебя были непростые отношения с матерью, да?" if not Player.Male:
                    $ LauraX.Statup("Love", 90, -15)
                    $ LauraX.Statup("Obed", 80, 45)
                    $ LauraX.Statup("Inbt", 70, 5)
                    $ LauraX.FaceChange("angry")
                    ch_l ". . . Возможно."
                    ch_l "Забудь."
            "У тебя были непростые отношения с отцом, да?" if Player.Male:
                    $ LauraX.Statup("Love", 90, -15)
                    $ LauraX.Statup("Obed", 80, 45)
                    $ LauraX.Statup("Inbt", 70, 5)
                    $ LauraX.FaceChange("angry")
                    ch_l ". . . Возможно."
                    ch_l "Забудь."
        $ LauraX.Petnames.append("daddy")
        return

# end Laura_Daddy//////////////////////////////////////////////////////////




label Gwentro:
        $ Player.AddWord(1,"interruption") #adds to Recent
        if Taboo <= 5 and AloneCheck(LauraX):
            #returns if other girls are present, this is a one on one thing.
            return
        $ LauraX.History.append("Gwentro")
        $ GwenX.Name = "? ? ?"
        ch_g "Где тут выход?!"
        $ GwenX.FaceChange("angry")
        show Gwen_Sprite at SpriteLoc(1500) zorder 25:
                xzoom -1
        show Gwen_Sprite at SpriteLoc(100) zorder 25 with easeinright #call Display_Gwen
        pause .1
        $ GwenX.FaceChange("surprised")
        $ Speed = 0
        $ LauraX.FaceChange("surprised",2,Eyes="side")
        show Gwen_Sprite at SpriteLoc(200) zorder 25 with vpunch #call Display_Gwen
        ch_g "Ай!"
        $ GwenX.FaceChange("angry")
        ch_g "Хорошо, видимо. . . это стена."
        $ GwenX.FaceChange("surprised")
        ch_g "О, эй вы-"
        ch_g "Эм. . ."
        $ GwenX.FaceChange("surprised",2,Mouth="open")
        $ GwenX.Statup("Love", 200, 5)
        $ GwenX.Statup("Obed", 200, 5)
        $ GwenX.Statup("Lust", 80, 5)
        ch_g "Простите! Виновата, я просто. . ."
        $ LauraX.FaceChange("confused",2,Eyes="side")
        $ GwenX.FaceChange("surprised")
        extend "\n искала выход. . ."
        $ GwenX.FaceChange("smile")
        extend "\n но вы. . . кажется, кое-чем заняты. . ."
        $ GwenX.FaceChange("sad")
        extend "\n и теперь я ничего не вижу из-за этого дурацкого шара. . ."
        show Gwen_Sprite:
            ease 1 ypos 150
        $ GwenX.FaceChange("smile")
        extend ""
        ch_g "Вот, так лучше. . ."
        show Gwen_Sprite:
            ease 1 ypos 50
        ch_g "Так, ладно, как тебя зовут?"
        $ LauraX.FaceChange("angry",1,Eyes="side")
        show Gwen_Sprite:
            ypos 50
        ch_g "Так, ладно, как тебя зовут?{w=0.2}{nw}"
        $ GwenX.FaceChange("surprised",Mouth="open")
        menu:
            ch_g "Так, ладно, как тебя зовут?{nw}"
            "[Player.Name]":
                pass
            "Зеро":
                pass
            "Не твое дело":
                pass
            "Кто ты такая?":
                pass
        ch_g "Воу!" with vpunch
        menu:
            ch_g "Воу!"
            "Что?":
                pass
        $ GwenX.FaceChange("surprised")
        ch_g "Извини, просто выскочившее меню застало меня врасплох."
        $ GwenX.FaceChange("smile")
        ch_g "Значит, так вы здесь общаетесь? Через диалоговые окна?"
        menu:
            extend ""
            "Да?":
                    ch_g "Все в порядке, я не осуждаю. . ."
                    ch_g "Я думаю, сейчас это не самое важное. . ."
            "Ты вообще о чем?":
                    ch_g "О всплывающие блоках? Думаю, ты не видишь их. . ."
                    ch_g "Если только ты сейчас не прикидываешься."
        ch_g "Ладно, вернемся к тебе, как тебя зовут?"
        menu:
            extend ""
            "[Player.Name]":
                $ GwenX.Statup("Love", 200, 5)
                ch_p "Я [Player.Name]."
                ch_g "Привет, [Player.Name], а я Гвен!"
                $ GwenX.Name = "Гвен"
                $ GwenX.Name_rod = "Гвен"
                $ GwenX.Name_dat = "Гвен"
                $ GwenX.Name_vin = "Гвен"
                $ GwenX.Name_tvo = "Гвен"
                $ GwenX.Name_pre = "Гвен"
            "Не твое дело":
                $ GwenX.Statup("Love", 200, -5)
                $ GwenX.Statup("Obed", 200, 3)
                ch_p "Это не твое дело."
                ch_g "Ну, похоже тебя зовут [Player.Name]."
                ch_g "Я поняла по диалоговому окну."
                ch_g "А я Гвен, между прочим."
            "Кто ты такая?":
                ch_p "Не важно кто я, куда важнее кто ты?!"
                ch_g "Ох! Справедливое замечание, я здесь новенькая. Меня зовут Гвен!"
                ch_g "А тебя, похоже, зовут [Player.Name]."
                ch_g "Я поняла по диалоговому окну."
        if GwenX.Name != "Гвен":
            $ GwenX.Name = "Гвен"
            $ GwenX.Name_rod = "Гвен"
            $ GwenX.Name_dat = "Гвен"
            $ GwenX.Name_vin = "Гвен"
            $ GwenX.Name_tvo = "Гвен"
            $ GwenX.Name_pre = "Гвен"
            menu:
                extend ""
                "По какому, нахер, окну?!":
                    ch_g "Не бери в голову."
                "Лаааадно. . .":
                    pass
        ch_g "Хоть здесь и довольно людно, если ты не возражаешь. . ."
        show Gwen_Sprite:
            easeout 1 xpos 300
            xzoom 1
            easein .5 xpos 900
        ch_g "Ах, приятно вдохнуть полной грудью!"
        $ LauraX.FaceChange("angry",Eyes="leftside")
        ch_g "Прости, я должна была поздороваться раньше, привет Лора!"
        $ LauraX.FaceChange("confused",Eyes="leftside")
        ch_l "Откуда ты знаешь мое имя?!"
        ch_g "Я все прочитала о тебе! Или ты предпочитаешь \"Икс-23?\""
        ch_g "Или \"Росомаха?\""
        $ GwenX.FaceChange("surprised")
        ch_g "Боже, ну не \"Коготь\" же?"
        $ GwenX.FaceChange("smile")
        ch_l "[LauraX.Name] - в самый раз."
        $ GwenX.FaceChange("smile",Mouth="kiss")
        ch_g "Отлично, итак. . ."
        menu:
            "Что ты здесь делаешь?":
                ch_p "Что ты здесь делаешь?"
                ch_g "Я чувствовала, что ты спросишь об этом."
            "-Какой-то вариант ответа-":
                ch_p "Что ты здесь делаешь?"
                ch_g "Тебе знакомо понятие детерминизма?"
        $ LauraX.FaceChange("confused",Eyes="leftside")
        ch_g "Почему вообще кто-то из нас здесь?"
        if not Player.Male:
            ch_g "А! Ты имела в виду \"почему я именно {i}здесь{/i}\", в этой игре?"
        else:
            ch_g "А! Ты имел в виду \"почему я именно {i}здесь{/i}\", в этой игре?"
        $ GwenX.FaceChange("sad")
        ch_g "Честно? Без понятия."
        $ GwenX.FaceChange("smile")
        ch_g "Может, меня добавил какой-то фанат?"
        $ GwenX.FaceChange("smile",2)
        ch_g "Судя по тому, чем вы двое занимались, я, похоже в какой-то хентай-игре."
        ch_g "Ну, как говорится \"В чужой монастырь. . .\""
        show Gwen_Sprite:
            easeout .2 xpos 890
            easeout .2 xpos 900
            pause .5
            easeout .15 xpos 880
            easeout .15 xpos 910
            easeout .15 xpos 880
            easeout .15 xpos 900
        ch_g "Ну, как говорится \"В чужой монастырь. . .\"{w=1.8}{nw}"
        $ GwenX.FaceChange("angry",2)
        ch_g "Хм."
        ch_g "Видимо, я не могу здесь раздеться."
        $ GwenX.FaceChange("sad,1")
        ch_g "Жаль."
        $ GwenX.FaceChange("angry",Mouth="smile")
        ch_g "Но я могла бы остаться и немного понаблюдать. . ."
        $ LauraX.FaceChange("angry",Eyes="leftside")
        $ GwenX.FaceChange("surprised",Mouth="open")
        ch_l "НЕТ!"
        ch_g "Хорошо, хорошо. Никому нельзя трогать Росомаху. . ."
        $ GwenX.FaceChange("smile")
        ch_g "Кроме тебя, конечно *подмигивает*."
        $ GwenX.FaceChange("sad",0)
        show Gwen_Sprite:
            ease .5 xpos 950
        ch_g "Тогда мне, наверное, пора идти. . ."
        show Gwen_Sprite:
            ease .5 xpos 1050
        ch_g "Не знаю, когда я вернусь. . ."
        show Gwen_Sprite:
            ease .5 xpos 1200
        ch_g "Если вообще вернусь. . ."
        show Gwen_Sprite:
            ease .5 xpos 1000
        $ GwenX.FaceChange("sad",Eyes="surprised")
        ch_g "Мы, возможно, никогда больше не встретимся."
        show Gwen_Sprite:
            ease .2 xpos 1500
        $ GwenX.FaceChange("surprised")
        ch_l "Убирайся!"
        ch_g "Ладно! Ну, я пошла, еще раз извините!"
        hide Gwen_Sprite
        $ GwenX.FaceChange("normal")
        $ LauraX.FaceChange("bemused",Eyes="sexy")
        $ GwenX.PubeC = 3
        $ GwenX.Todo.append("Gwentro")
        ch_l "А теперь, на чем мы там остановились. . ?"

        return

#Start Laura new clothes content/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Dressup:
        #(Condition: X23 has returned to school)
        #(location: campus square)
        $ ActiveGirls.append(LauraX) if LauraX not in ActiveGirls else ActiveGirls
        call Shift_Focus(LauraX)
        $ bg_current = "bg campus"
        call Remove_Girl("All")
        $ LauraX.Loc = bg_current
        call Set_The_Scene(0)

        $ LauraX.Outfit = "casual1"
        $ LauraX.OutfitChange("casual1")
        show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) with vpunch
        $ Round -= 10 if Round >= 11 else Round
        $ LauraX.History.remove("dress0")
        $ LauraX.History.append("dress1")
        $ LauraX.History.append("met")
        "Когда вы пересекаете площадь, вы натыкаетесь на [LauraX.Name_vin]."
        $ LauraX.FaceChange("normal")
        ch_l "О, привет."
        menu:
            extend ""
            "О, [LauraX.Name]. Ты вернулась!":
                    $ LauraX.Statup("Love", 50, 3)
                    $ LauraX.Statup("Obed", 50, 1)
                    ch_l "Ага, только что."
            "Привет.":
                    ch_l "Ага, я только что вернулась."
            "Напомни, кто ты?":
                    $ LauraX.Statup("Love", 70, -3)
                    $ LauraX.Statup("Obed", 80, 5)
                    $ LauraX.FaceChange("confused")
                    ch_l "Лора."
                    ch_l "Мы не так давно познакомились."

        "Она потягивается и разминает шею."
        ch_l "В этот раз я задержусь здесь надолго."
        ch_l "Еще увидимся, мне надо бы принять горячий душ."

        menu:
            extend ""
            "Конечно. До встречи!":
                    pass
            "Ладно, увидимся.":
                    pass
            "Составить компанию?":
                    $ LauraX.Statup("Love", 70, -1)
                    $ LauraX.Statup("Obed", 80, 5)
                    $ LauraX.Statup("Inbt", 80, 5)
                    $ LauraX.FaceChange("bemused")
                    ch_l "И не надейся."

        hide Laura_Sprite with easeoutright
        call Remove_Girl(LauraX)
        "ока вы смотрите, как [LauraX.Name] уходит, кто-то хлопает вас по плечу."

        call Shift_Focus(KittyX)
        $ KittyX.Loc = bg_current
        call Set_The_Scene(0)
        $ KittyX.Outfit = KittyX.OutfitDay
        $ KittyX.OutfitChange()
        call Display_Girl(KittyX)

        $ KittyX.FaceChange("smile")
        if not Player.Male:
            ch_k "Привет, [KittyX.Petname], на что уставилась?"
        else:
            ch_k "Привет, [KittyX.Petname], на что уставился?"
        #add Kitty arrving here

        menu:
            extend ""
            "Привет, [KittyX.Name]. Я только что разговаривала с [LauraX.Name_tvo]." if not Player.Male:
                    ch_k "О, она вернулась?"
            "Привет, [KittyX.Name]. Я только что разговаривал с [LauraX.Name_tvo]." if Player.Male:
                    ch_k "О, она вернулась?"
            "Ни на что.":
                    ch_k "А, ясно, на [LauraX.Name_vin], значит."
                    ch_k "Она вернулась?"
            "Я рассматривала вон ту красивую цыпочку." if not Player.Male:
                if ApprovalCheck(KittyX,1200,"LO") or KittyX.Les >= 10:
                        $ KittyX.Statup("Obed", 80, 5)
                        $ KittyX.Statup("Inbt", 80, 5)
                        $ KittyX.FaceChange("bemused",1)
                        ch_k "Думаю, не могу винить тебя за это. . ."
                else:
                        $ KittyX.Statup("Love", 70, -5)
                        $ KittyX.Statup("Obed", 80, 10)
                        $ KittyX.Statup("Inbt", 80, 5)
                        $ KittyX.FaceChange("angry")
                        ch_k "Не слишком ли пошло?"
            "Я рассматривал вон ту красивую цыпочку." if Player.Male:
                if ApprovalCheck(KittyX,1200,"LO") or KittyX.Les >= 10:
                        $ KittyX.Statup("Obed", 80, 5)
                        $ KittyX.Statup("Inbt", 80, 5)
                        $ KittyX.FaceChange("bemused",1)
                        ch_k "Думаю, не могу винить тебя за это. . ."
                else:
                        $ KittyX.Statup("Love", 70, -5)
                        $ KittyX.Statup("Obed", 80, 10)
                        $ KittyX.Statup("Inbt", 80, 5)
                        $ KittyX.FaceChange("angry")
                        ch_k "Не слишком ли пошло?"

        $ KittyX.FaceChange("smile",Eyes="side")
        ch_k "Знаешь, она редко бывает здесь."
        ch_k "Должно быть, из-за Логана."

        menu:
            extend ""
            "Они как-то связаны?":
                    ch_k "Да, она его дочь или типа того? Я не уверена."
            "Она ведь его клон, да?":
                    ch_k "Наверное? Я не уверена."
        "Она пожимает плечами, но затем хитро улыбается."

        $ KittyX.FaceChange("sly")
        ch_k "Мы думали сделать ей подарок по -возращению домой-."
        ch_k "Скинешься?"

        menu:
            extend ""
            "Конечно, почему нет?":
                    $ KittyX.Statup("Love", 50, 5)
                    $ KittyX.Statup("Obed", 40, 5)
                    ch_p "Хорошо. Что вы хотите ей подарить?"
            "Нет, я ее толком то и не знаю.":
                    if not Player.Male:
                        ch_k "Да, наверное, ты права. Иногда она такая колючая."
                    else:
                        ch_k "Да, наверное, ты прав. Иногда она такая колючая."
                    return
            "Странное предложение.":
                    if not Player.Male:
                        ch_k "Да, наверное, ты права. Иногда она такая колючая."
                    else:
                        ch_k "Да, наверное, ты прав. Иногда она такая колючая."
                    return

        #"Kitty grins."
        ch_k "Ну, честно говоря, у нее не так много вещей, поэтому мы собирались подарить ей что-нибудь из одежды."

        menu:
            extend ""
            "Ты очень стильная, так что, наверное, ты подберешь что-нибудь классное.":
                    $ KittyX.Statup("Love", 80, 5)
                    $ KittyX.Statup("Inbt", 40, 3)
                    $ KittyX.FaceChange("smile",1)
                    if not Player.Male:
                        ch_k "Подхалимка."
                    else:
                        ch_k "Льстец."
            "Звучит неплохо.":
                    $ KittyX.Statup("Love", 60, 2)
            "С твоим чувством стиля? Это не закончится ничем хорошим.":
                    $ KittyX.Statup("Love", 70, -5)
                    $ KittyX.Statup("Obed", 80, 5)
                    $ KittyX.Statup("Inbt", 80, -3)
                    $ KittyX.FaceChange("angry")
        ch_k "В общем, мы думали скинуться по $10 с каждого."

        menu:
            extend ""
            "Вот." if Player.Cash >= 10:
                    $ KittyX.Statup("Love", 70, 1)
                    $ KittyX.Statup("Obed", 40, 2)
                    ch_k "Отоично."
                    $ Player.Cash -= 10
                    $ LauraX.History.append("dress2")
            "У меня столько нет. . ." if Player.Cash < 10:
                    $ KittyX.Statup("Love", 70, 1)
                    $ KittyX.Statup("Obed", 40, 2)
                    $ KittyX.FaceChange("normal",1,Brows="surprised",Mouth="sad")
                    ch_k "Ох."
                    ch_k "Пока не к спеху, если вдруг захочешь, просто найди меня."
            "Знаешь, мне это не интересно.":
                    $ KittyX.Statup("Love", 70, -2)
                    $ KittyX.Statup("Obed", 40, -1)
                    $ KittyX.FaceChange("normal",1,Brows="surprised",Mouth="sad")
                    ch_k "Ох, ладно."
        return

label Laura_Dressup2:
        #plays if you blew Kitty off earlier. State should be "dress1"
        ch_p "Помнишь, мы говорили о подарке для [LauraX.Name_rod]?"
        $ KittyX.FaceChange("smile")
        ch_k "Да?"
        menu:
            extend ""
            "Вот, $10.":
                    $ KittyX.Statup("Love", 70, 1)
                    $ KittyX.Statup("Obed", 40, 2)
                    ch_k "Круто."
                    $ LauraX.History.append("dress2")
            "Забудь.":
                    ch_k "Ох, ладно."
        return


label Laura_Dressup3:
        #(Condition: Laura_Dressup has already played), State should be "dress2"
        #(location: Kitty's room door)
        $ LauraX.History.remove("dress1")
        $ LauraX.History.remove("dress2")
        $ LauraX.History.append("dress3")
        $ LauraX.Inventory.append("wolvie top")
        $ LauraX.Inventory.append("wolvie panties")

        "Когда вы проходите мимо двери [KittyX.Name_rod], вы слышите, как она над чем-то смеется."
        "Вы также слышите другой голос, с ней в комнате явно кто-то еще."

        ch_l "[KittyX.Name], не стоит."
        ch_l "Нет, серьезно. . ."
        ch_l "тебе не следовало этого делать."
        ch_k "Да ладно тебе, Ты выглядишь великолепно."

        "Вы вспоминаете разговор с [KittyX.Name_tvo] о подарке для [LauraX.Name_rod]. Похоже, [LauraX.Name] его получила."
        "Вам становится любопытно. . ."

        $ KittyX.Outfit = KittyX.OutfitDay
        $ KittyX.OutfitChange()
        $ LauraX.OutfitChange("nude")
        $ LauraX.Chest = "wolvie top"
        $ LauraX.Panties = "wolvie panties"
        menu:
            extend ""
#            "Sneak a peek [[no key] (locked)" if KittyX not in Keys:
#                    pass
            "Заглянуть украдкой":
                    "Вы толкаете дверь и обнаруживаете, что она незаперта. Вы открываете ее и заглядываете внуть."
                    ch_p "Привет, [KittyX.Name], в чем дело?"
                    if KittyX in Keys:
                            ch_k "Привет, [KittyX.Petname]! Заходи!"
                    else:
                            ch_k "Привет, [KittyX.Petname]! Подожди, что ты здесь делаешь?!"

                    call CleartheRoom("All",0,1)
                    call Shift_Focus(LauraX)
                    $ KittyX.Loc = "bg kitty"
                    $ LauraX.Loc = "bg kitty"
                    call Set_The_Scene(Dress=0)

                    $ LauraX.FaceChange("sad",2,Eyes="squint",Brows="confused")
                    "[LauraX.Name] смотрит на вас, прищурившись. Она явно на взводе."
                    $ LauraX.FaceChange("sad",2,Brows="confused",Eyes="leftside")
                    ch_l "Разве ты не заперла дверь?"
                    if KittyX.Event[0] == 1:
                            $ KittyX.FaceChange("smile",Eyes="side")
                            if not Player.Male:
                                ch_k ". . . Думаю, заперла, но. . . Я все равно дала ей ключ."
                                $ LauraX.FaceChange("sad",1,Brows="confused",Eyes="leftside")
                                ch_l "Ты. . . дала ей ключ?"
                            else:
                                ch_k ". . . Думаю, нет, но. . . Я все равно дала ему ключ."
                                $ LauraX.FaceChange("sad",1,Brows="confused",Eyes="leftside")
                                ch_l "Ты. . . дала ему ключ?"
                    else:
                            # you probably stole it from Xavier
                            $ KittyX.FaceChange("confused",Eyes="side")
                            ch_k ". . . Думаю, заперла. . ."
                            if not ApprovalCheck(KittyX,1200):
                                    #if she doesn't like you a lot yet. . .
                                    $ KittyX.FaceChange("angry",1)
                                    ch_k "Ладно, довольно, на выход!"
                                    "Вы выходите."
                                    return
                            $ KittyX.FaceChange("smile")
                            ch_k "Хотя, думаю, все нормально. . ."
                            $ LauraX.FaceChange("sad",1,Brows="confused",Eyes="leftside")
                            if not Player.Male:
                                ch_l "Нормально, что у нее есть загадочный ключ?"
                            else:
                                ch_l "Нормально, что у него есть загадочный ключ?"
                    $ KittyX.FaceChange("smile",1)
                    if not Player.Male:
                        ch_k "Угу. Ну, она моя [KittyX.Petname]."
                        ch_l "Твоя. . . [KittyX.Petname]. . ?"
                    else:
                        ch_k "Угу. Ну, он мой [KittyX.Petname]."
                        ch_l "Твой. . . [KittyX.Petname]. . ?"
            "Постучаться":
                    "Вы стучитесь в дверь."
                    ch_k "Кто там?"
                    ch_p "[Player.Name], не возражаешь, если я войду?"
                    if not ApprovalCheck(KittyX, 1000):
                            ch_k "Эм, извини, [KittyX.Petname], мы тут немного заняты."
                            ch_k "[KittyX.Like]может, заглянешь позже?"
                            ch_p "Конечно, без проблем."
                            "Вы уходите."
                            return
                    ch_k "Конечно, [KittyX.Petname]! Секунду!"
                    "[KittyX.Name] распахивает дверь."

                    call CleartheRoom("All",0,1)
                    call Shift_Focus(LauraX)
                    $ KittyX.Loc = "bg kitty"
                    $ LauraX.Loc = "bg kitty"
                    call Set_The_Scene(Dress=0)

                    $ LauraX.FaceChange("sad",2,Brows="surprised")
                    if not Player.Male:
                        ch_l "Ты впускаешь ее всякий раз, как ей вздумается?"
                        $ KittyX.FaceChange("smile",1)
                        ch_k "Угу. Она же моя [KittyX.Petname]."
                        ch_l "Твоя. . . [KittyX.Petname]. . ?"
                    else:
                        ch_l "Ты впускаешь его всякий раз, как ему вздумается?"
                        $ KittyX.FaceChange("smile",1)
                        ch_k "Угу. Он же мой [KittyX.Petname]."
                        ch_l "Твой. . . [KittyX.Petname]. . ?"

            "Уйти":
                    "Нет, пусть побудут наедине."
                    return
        $ LauraX.SeenPanties = 1
        $ LauraX.FaceChange("angry",1,Eyes="closed")
        "Она качает головой, пытаясь переварить всю эту новую информацию."
        "Она бормочет что-то себе под нос."
        ch_l "Меня не было дольше, чем я думала. . ."
        $ LauraX.FaceChange("sad",1,Brows="confused",Eyes="leftside")

        call Laura_Girltalk(1) # "Hey, are you inta me?"
        if not Player.Male:
            ch_l "Так почему она здесь?"
            $ KittyX.FaceChange("smile",Eyes="side")
            ch_k "Ну, она вроде как тоже учавствовала в покупке, так почему бы не узнать, что она думает?"
        else:
            ch_l "Так почему он здесь?"
            $ KittyX.FaceChange("smile",Eyes="side")
            ch_k "Ну, он вроде как тоже учавствовал в покупке, так почему бы не узнать, что он думает?"
        "[KittyX.Name] подходит и встает в позу, словно она представляет [LauraX.Name] в качестве модели."
        $ KittyX.ArmPose = 2
        $ KittyX.FaceChange("smile")
        ch_k "Ну, что думаешь?"

        menu:
            extend ""
            "Ее наряд выглядит знако. . .":
                    ch_k "Я дала ему название - образ Логана."
                    $ LauraX.FaceChange("sad",2,Eyes="stunned")
                    $ LauraX.Statup("Inbt", 40, -2)
                    ch_l "Прошу, не называй его так."
            "Хорошо выглядишь, [LauraX.Name]!":
                    $ LauraX.Statup("Love", 70, 5)
                    $ LauraX.Statup("Obed", 40, 3)
                    $ LauraX.Statup("Inbt", 40, 5)
                    $ LauraX.GLG(KittyX,700,5,1)
                    $ LauraX.FaceChange("sadside",1)
                    ch_l "Ага, ну. . . [KittyX.Name] свое дело знает."
                    $ KittyX.Statup("Love", 70, 1)
                    $ KittyX.Statup("Obed", 40, 3)
                    $ KittyX.GLG(LauraX,700,3,1)
                    ch_k "Хихи, спасибо."
            "Отличный наряд, [KittyX.Name]! Он замечательно ей подходит!":
                    $ KittyX.Statup("Love", 70, 5)
                    $ KittyX.Statup("Obed", 40, 3)
                    ch_k "Еще бы, свое дело я знаю."
                    $ LauraX.Statup("Love", 70, 3)
                    $ LauraX.Statup("Obed", 40, 2)
                    $ LauraX.Statup("Inbt", 40, 5)
                    $ LauraX.FaceChange("bemused",1)
                    $ LauraX.GLG(KittyX,700,3,1)
                    ch_l "Ага, наверное, так оно и есть. . ."
            "Могу я получить возврат?":
                    $ KittyX.Statup("Love", 70, -5)
                    $ KittyX.Statup("Obed", 40, -3)
                    $ KittyX.FaceChange("angry")
                    if not Player.Male:
                        ch_k "Нашла, как испортить настроение."
                    else:
                        ch_k "Нашел, как испортить настроение."
                    $ LauraX.Statup("Love", 70, -5)
                    $ LauraX.Statup("Obed", 40, 5)
                    $ LauraX.Statup("Inbt", 40, -5)
                    $ LauraX.FaceChange("angry")
                    ch_l "Точно."

        $ LauraX.FaceChange("smile",0,Eyes="leftside")
        $ LauraX.GLG(KittyX,700,5,1)
        $ KittyX.GLG(LauraX,700,5,1)
        ch_l "Но серьезно, [KittyX.Name], спасибо за подарок."
        $ KittyX.FaceChange("smile",Eyes="side")
        ch_k "Пожалуйста! Для чего еще нужны друзья?"
        ch_l "Уверена, друзья обычно не используют друг друга в качестве кукол для переодеваний."
        ch_k "Ох, [LauraX.Name], тебе оооочень многому предстоит научиться."
        $ LauraX.FaceChange("smile",Eyes="down")
        "[LauraX.Name] слегка улыбается и осматривает себя."
        ch_l "Я думаю, носить весь комплект - это слишком."
        $ LauraX.FaceChange("smile",Eyes="leftside")
        ch_l "Ты же знаешь, что Логан бросит в мой адрес пару колкостей, если увидит меня в таком виде."
        $ KittyX.FaceChange("smile",Eyes="side")
        ch_k "Эй, теперь это твой наряд. Меняй и сочетай, как тебе захочется, подруга!"
        ch_l "Да. Пожалуй, так и сделаю."
        $ LauraX.Names.append("Wolverine")

        $ KittyX.FaceChange("smile")
        $ LauraX.FaceChange("sly",1)
        "[LauraX.Name] пристально смотрит на вас."

        ch_l "Я бы хотела переодеться."

        menu:
            extend ""
            "Давай, переодевайся!":
                    $ LauraX.Statup("Obed", 40, 3)
                    $ LauraX.Statup("Inbt", 40, 3)
                    if not Player.Male and "girltalk" not in LauraX.History and "nogirls" not in LauraX.History:
                            #if she hasn't clocked you,
                            pass
                    elif (not LauraX.SeenChest or not LauraX.SeenPussy) and not ApprovalCheck(LauraX,1400):
                            $ LauraX.Statup("Love", 70, -5)
                            $ LauraX.FaceChange("angry",1)
                            ch_l "Так не пойдет."
                            ch_k "Ага, думаю, тебе лучше уйти, [KittyX.Petname]. . ."
                            ch_k ". . . Прежде чем она сделает с тобой то же, что Логан делает с теми, кто его злит."
                            "[KittyX.Name] уверенно провожает вас до двери."
                            $ Round -= 20 if Round >= 21 else Round
                            return
                    if (LauraX.SeenChest and LauraX.SeenPussy) or not Player.Male:
                            ch_l "Справедливое замечание. . ."
                    elif ApprovalCheck(LauraX,1400):
                            if not Player.Male:
                                ch_l "А ты смелая. . ."
                            else:
                                ch_l "А ты смелый. . ."
                    $ KittyX.FaceChange("surprised",2,Eyes="side")
                    $ LauraX.Chest = 0
                    "[LauraX.Name] начинает снимать новый наряд. . ."
                    if ApprovalCheck(KittyX,1200):
                            $ KittyX.FaceChange("sly",1)
                    else:
                            $ KittyX.FaceChange("angry",1,Eyes="side")

                    $ LauraX.Panties = 0
                    call Girl_First_Topless(LauraX)
                    call Girl_First_Bottomless(LauraX,1)
                    pause 1
                    $ LauraX.OutfitChange(LauraX.OutfitDay,Changed=1)
                    "А затем надевает свою обычный одежду."

                    if ApprovalCheck(KittyX,1200):
                            $ KittyX.FaceChange("sly",1)
                    else:
                            $ KittyX.FaceChange("angry",1)
                    if Player.Male or ("girltalk" in KittyX.History or "nogirls" in KittyX.History):
                            ch_k "Ну, думаю, на сегодня тебе хватит."
                    ch_k "А теперь дай девочкам уединиться."
                    "[KittyX.Name] выгоняет вас из комнаты, и вы направляетесь на площадь кампуса."

            "Намек понят. Пока, девочки!":
                        ch_k "До встречи, [KittyX.Petname]!"
                        ch_l "Увидимся."

        $ Round -= 20 if Round >= 21 else Round
        return
        #End scene
#End Laura new clothes content/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



label Laura_Foul:
        $ LauraX.History.remove("partyfoul")
        if "partysolved" in LauraX.History:
                $ LauraX.History.remove("partysolved")
        $ LauraX.AddWord(1,0,0,0,"partyfix") #adds "partysolved" to History
        $ LauraX.FaceChange("sad",1)
        if LauraX.Loc == bg_current or LauraX in Party:
                "[LauraX.Name] смотрит на вас с огорченным видом."
        else:
                "[LauraX.Name] выходит из-за угла и натыкается на вас."
        if bg_current != "bg laura" and bg_current != "bg player":
                "Не говоря ни слова, она пристраивается за вами и подталкивает вас к ее комнате."
                $ bg_current = "bg laura"
        $ LauraX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(LauraX)
        call Set_The_Scene
        call Taboo_Level
        ch_l "Слушай. . ."
        ch_l "[LauraX.Petname]. . ."
        ch_l "Насчет того случая на вечеринке. . ."
        menu:
            extend ""
            "Какой случай? На какой вечеринке?":
                    $ LauraX.Statup("Love", 90, -2)
                    $ LauraX.Statup("Obed", 80, 2)
                    $ LauraX.Statup("Inbt", 60, 1)
                    $ LauraX.FaceChange("confused",2)
            "А, да. Извини.":
                    $ LauraX.Statup("Love", 80, 5)
                    $ LauraX.Statup("Love", 200, 5)
                    $ LauraX.FaceChange("surprised",2)
                    $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                    $ LauraX.FaceChange("smile",1)
            "Да?":
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Inbt", 60, 1)
                    $ LauraX.FaceChange("sad",1)
            ". . .":
                    $ LauraX.Statup("Love", 80, -1)
                    $ LauraX.Statup("Obed", 50, 2)
                    $ LauraX.FaceChange("sad",1)

        if "sorry" not in LauraX.RecentActions:
                    #if you didn't apologize in first response
                    $ LauraX.FaceChange("sadside",1)
                    ch_l "Мы были на вечеринке в честь Хэллоуина. . ."
                    $ LauraX.FaceChange("sad",1)
                    if not Player.Male:
                        ch_l "И ты кое-что сказала о моем костюме. . ."
                    else:
                        ch_l "И ты кое-что сказал о моем костюме. . ."
                    menu:
                        extend ""
                        "Не помню, что я сказала?" if not Player.Male:
                                $ LauraX.Statup("Love", 99, -3)
                                $ LauraX.FaceChange("surprised",1)
                        "Не помню, что я сказал?" if Player.Male:
                                $ LauraX.Statup("Love", 99, -3)
                                $ LauraX.FaceChange("surprised",1)
                        "А, да. Извини.":
                                $ LauraX.FaceChange("smile",1)
                                $ LauraX.Statup("Love", 80, 5)
                                $ LauraX.Statup("Love", 200, 5)
                                $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                        "Разве?":
                                $ LauraX.FaceChange("surprised",1)
                                ch_l ". . ."
                                $ LauraX.Statup("Love", 99, -5)
                                $ LauraX.Statup("Obed", 70, 3)
                                $ LauraX.Statup("Obed", 90, 2)
                                $ LauraX.FaceChange("angry",1)
                        ". . .":
                                $ LauraX.Statup("Love", 99, -1)
                                $ LauraX.FaceChange("angry",1)

        if "sorry" not in LauraX.RecentActions:
                    #if you didn't apologize in second response
                    if not Player.Male:
                        ch_l "Ты сказала, что я была похожа на. . ."
                    else:
                        ch_l "Ты сказал, что я была похожа на. . ."
                    ch_l "Проститутку."
                    menu:
                        extend ""
                        "Ооох. Блин. Да.":
                                $ LauraX.FaceChange("sly",1)
                                $ LauraX.Statup("Love", 80, 2)
                                $ LauraX.Statup("Love", 200, 2)
                                $ LauraX.Statup("Inbt", 60, 2)
                        "А, да. Извини.":
                                $ LauraX.FaceChange("smile",1)
                                $ LauraX.Statup("Love", 80, 2)
                                $ LauraX.Statup("Love", 200, 5)
                                $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                        "Это проблема?":
                                $ LauraX.FaceChange("surprised",1)
                                pause 0.5
                                $ LauraX.FaceChange("angry",1)
                                $ LauraX.Statup("Love", 80, -5)
                                $ LauraX.Statup("Love", 200, -5)
                                $ LauraX.Statup("Obed", 70, 5)
                                ch_l "-Конечно- это -проблема-. . ."
                        "Хм.":
                                $ LauraX.Statup("Love", 99, -3)
                                $ LauraX.Statup("Obed", 70, 5)
                                $ LauraX.FaceChange("surprised",1)
                        ". . .":
                                $ LauraX.Statup("Love", 80, -2)
                                $ LauraX.Statup("Love", 200, -2)
                                $ LauraX.FaceChange("angry",1)

        if "lover" in LauraX.Petnames:
                ch_l "Ты понимаешь почему это. . . беспокоит меня. . ?"
                menu:
                    extend ""
                    "Ох. . . да.":
                            $ LauraX.FaceChange("normal",1,Eyes="side")
                            $ LauraX.Statup("Love", 90, 1)
                            $ LauraX.Statup("Inbt", 60, 2)
                            $ LauraX.AddWord(1,"nyx",0,0,0) #adds "nyx" to Recent
                    "Извини, видимо, я что-то упустила." if not Player.Male:
                            $ LauraX.FaceChange("confused",2)
                            $ LauraX.Statup("Love", 200, -3)
                            ch_l "Ты серьезно?"
                            $ LauraX.FaceChange("angry",1)
                    "Извини, видимо, я что-то упустил." if Player.Male:
                            $ LauraX.FaceChange("confused",2)
                            $ LauraX.Statup("Love", 200, -3)
                            ch_l "Ты серьезно?"
                            $ LauraX.FaceChange("angry",1)
                    "Что? Почему?":
                            $ LauraX.FaceChange("confused",2)
                            $ LauraX.Statup("Love", 200, -5)
                            ch_l "Ты серьезно?"
                            $ LauraX.FaceChange("angry",1)

        if "nyx" not in LauraX.RecentActions:
                ch_l "Может быть, ты не понимаешь, почему меня это так глубоко задело. . ."
                ch_l ". . ."
                $ LauraX.FaceChange("sadside",1)
                ch_l "Когда я была моложе, сама по себе. . ."
                $ LauraX.Statup("Inbt", 60, 1)
                ch_l "Мне приходилось заниматься разными вещами. . ."
                $ LauraX.Blush = 2
                $ LauraX.Statup("Inbt", 60, 1)
                ch_l "На улицах."
                $ LauraX.FaceChange("sad",1)
                ch_l "Поэтому я не хочу, чтобы меня называли. . . так."

        menu:
            extend ""
            "Ох, мне так стыдно.":
                    $ LauraX.Statup("Love", 200, 5)
                    $ LauraX.FaceChange("smile",1,Eyes="side")
                    ch_l "Спасибо. . ."
                    $ LauraX.FaceChange("smile",1)
                    $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
            "Да, я понимаю.":
                    $ LauraX.Statup("Love", 80, 2)
                    $ LauraX.Statup("Love", 200, 3)
                    $ LauraX.Statup("Obed", 80, 1)
                    $ LauraX.Statup("Inbt", 60, 1)
                    $ LauraX.FaceChange("smile",1)
                    ch_l "Спасибо."
                    $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
            "Ох, ладно.":
                    if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 400, "O"):
                        $ LauraX.Statup("Obed", 60, 3)
                        $ LauraX.Statup("Obed", 90, 2)
                        $ LauraX.Statup("Inbt", 60, 3)
                        $ LauraX.FaceChange("sly",1)
                    else:
                        $ LauraX.Statup("Love", 200, -5)
                        $ LauraX.Statup("Obed", 90, 5)
                        $ LauraX.FaceChange("angry",1)
                    ch_l ". . ."
            "Ха! Переживешь.":
                    $ LauraX.FaceChange("angry",1)
                    $ LauraX.Statup("Love", 80, -5)
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 80, 5)
                    $ LauraX.Statup("Inbt", 60, 5)
                    ch_l "Сволочь."
                    $ LauraX.DrainWord("sorry",1,0,0)
        menu:
            extend ""
            "Этого больше не повторится.":
                    if "sorry" not in LauraX.RecentActions:
                            $ LauraX.FaceChange("confused",1)
                            ch_l "Значит, ты сожалеешь?"
                            menu:
                                "Да, конечно!":
                                        $ LauraX.FaceChange("smile",1)
                                        $ LauraX.Statup("Love", 200, 3)
                                        ch_l "Хорошо."
                                        $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                                "Эм, наверное?":
                                        ch_l ". . ."
                                        if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 400, "O"):
                                                $ LauraX.FaceChange("normal",1)
                                                $ LauraX.Statup("Love", 80, 2)
                                                $ LauraX.Statup("Love", 200, 2)
                                                $ LauraX.Statup("Obed", 90, 2)
                                                $ LauraX.Statup("Inbt", 60, 1)
                                                ch_l "Сойдет."
                                                $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                                        else:
                                                $ LauraX.Statup("Love", 90, -5)
                                                $ LauraX.Statup("Obed", 90, 3)
                                                $ LauraX.Statup("Inbt", 60, 1)
                                                $ LauraX.FaceChange("angry",1)
                                                ch_l "Такой ответ меня не устраивает."
                                "О чем?":
                                        $ LauraX.FaceChange("angry",1)
                                        $ LauraX.Statup("Love", 80, -5)
                                        $ LauraX.Statup("Love", 99, -5)
                                        $ LauraX.Statup("Obed", 90, 5)
                                        $ LauraX.Statup("Inbt", 50, 5)
                                        $ LauraX.Statup("Inbt", 70, 5)
                                        ch_l "Гррррр."
                    else:
                            $ LauraX.FaceChange("angry",1,Mouth="smile")
                            $ LauraX.Statup("Obed", 80, 2)
                            $ LauraX.Statup("Inbt", 60, 3)
                            ch_l "Лучше бы этого никогда не происходило."

            "Это все?":
                    $ LauraX.FaceChange("angry",1)
                    $ LauraX.Statup("Love", 80, -5)
                    $ LauraX.Statup("Love", 99, -5)
                    $ LauraX.Statup("Inbt", 60, 10)
                    ch_l "Ты серьезно?!"

        if "sorry" in LauraX.RecentActions:
                $ LauraX.FaceChange("smile",1)
                ch_l "Я рада, что тебе по крайней мере не все равно."
        else:
                $ LauraX.FaceChange("angry",1)
                $ LauraX.AddWord(1,"angry","angry",0,0) #adds "angry" to Recent/Daily
                if not Player.Male:
                    ch_l "Пошла на хуй и мнение свое с собой прихвати!"
                else:
                    ch_l "Пошел на хуй и мнение свое с собой прихвати!"
        return


# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        if "switched" in LauraX.History:
                jump Laura_Switch2
        $ LauraX.FaceChange("smile", 1)
        ch_l "Мы знакомы?"
        ch_l "[[нюх, нюх]"
        ch_l "О, привет, [Player.XName]."
        menu:
            extend ""
            "Это я, [Player.XName].":
                    $ LauraX.FaceChange("confused", 1)
                    ch_l "Ага."
                    $ LauraX.FaceChange("smile", 1)
                    if Player.Male:
                            ch_l "Ты, эм, выглядишь больше?"
                    else:
                            ch_l "Ты, эм, выглядишь меньше?"
                    $ LauraX.AddWord(1,"switch") #recent

            "Нет.":
                    ch_l "Хм."
                    if Player.Male:
                            ch_l "Значит, ты ее брат? Запах почти такой же."
                    else:
                            ch_l "Значит, ты его сестра? Запах почти такой же."
                    ch_l "Кстати, я [LauraX.Name]."
            "Возможно?":
                    ch_l "Мне кажется, у тебя серьезная травма головы. . ."

        if "switch" not in LauraX.RecentActions:
                    $ LauraX.FaceChange("confused", 1)
                    ch_l "[[нюх, нюх]"
                    ch_l "Нет, ты точно [Player.XName]!"
                    $ LauraX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Ага, это я, [Player.XName].":
                                $ LauraX.Statup("Love", 90, 1)
                                $ LauraX.Statup("Obed", 70, 1)
                                ch_l "Я так и поняла."
                                $ LauraX.FaceChange("smile", 1)
                                if Player.Male:
                                        ch_l "Ты, эм, выглядишь больше?"
                                else:
                                        ch_l "Ты, эм, выглядишь меньше?"
                        "Нет.":
                                $ LauraX.FaceChange("angry", 1)
                                $ LauraX.Statup("Obed", 60, 1)
                                $ LauraX.Statup("Obed", 70, 1)
                                ch_l "Чушь."
                        "Возможно?":
                                $ LauraX.FaceChange("sly", 1)
                                $ LauraX.Statup("Love", 80, 1)
                                $ LauraX.Statup("Obed", 70, 1)
                                $ LauraX.Statup("Inbt", 60, 1)
                                ch_l "Может, нам стоит сдать тебя в лабораторию. . ?"
                    ch_l "Почему сразу нельзя было сказать?"
                    menu:
                        extend ""
                        "Извини, хотелось пошутить.":
                                $ LauraX.FaceChange("sly", 1)
                                $ LauraX.Statup("Love", 70, 1)
                        "Молодец, ты все поняла.":
                                $ LauraX.FaceChange("sly", 1)
                                $ LauraX.Statup("Obed", 70, 1)
                                $ LauraX.Statup("Inbt", 80, 1)
                                ch_l "Еще бы. . ."
                        "Хех.":
                                $ LauraX.FaceChange("sly", 1,Eyes="side")
                                $ LauraX.Statup("Love", 70, 1)
                                $ LauraX.Statup("Love", 90, 1)
                                $ LauraX.Statup("Inbt", 70, 1)
                                ch_l "Хах. . ."
                                call Punch
                                "Она крепко сжимает ваше плечо."
                    ch_l "Не пытайся повторить подобное с теми, у кого превосходный нюх. . ."
        #end "tried to lie"
        $ LauraX.FaceChange("smile", 1)
        ch_l "К чему такие изменения?"
        menu:
            extend ""
            "Да так, по приколу.":
                    $ LauraX.Statup("Inbt", 70, 1)
                    $ LauraX.FaceChange("sly", 1)
            "Я так себя сейчас ощущаю.":
                    pass
            "У меня не было каких-то особых причин.":
                    pass

        ch_l "Ага, понимаю."

        if [Player.Name] != [Player.XName]:
                ch_p "А еще теперь меня зовут [Player.Name]."
                ch_l "Ясно."

        if LauraX.SEXP >= 15:
                $ LauraX.FaceChange("sad", 1,Mouth="smile")
                ch_l "Я тебе еще нравлюсь?"
                menu:
                    extend ""
                    "Конечно!":
                            $ LauraX.FaceChange("smile", 1)
                            $ LauraX.Statup("Love", 70, 2)
                            $ LauraX.Statup("Love", 90, 1)
                            ch_l "Клево. . ."
                    "Да не особо.":
                            $ LauraX.FaceChange("sad", 1)
                            $ LauraX.Statup("Love", 80, -2)
                            $ LauraX.Statup("Obed", 60, 2)
                            $ LauraX.Statup("Obed", 80, 2)
                            ch_l "Ладно, поняла."
                    "А ты как думаешь?":
                            $ LauraX.FaceChange("sly", 1)
                            $ LauraX.Statup("Obed", 70, 1)
                            $ LauraX.Statup("Inbt", 70, 1)
                            ch_l "Думаю. я тебя \"возбуждаю\". . ."

        if not Player.Male and LauraX.Les > 5:
                $ LauraX.FaceChange("sly", 1)
                ch_l "Я и по мальчикам, и по девочкам. . ."
        if ApprovalCheck(LauraX, 1200):
                ch_l "Это может быть весело."
                $ LauraX.AddWord(1,0,0,0,"girltalk") #history
        else:
                $ LauraX.FaceChange("normal", 1,Eyes="side")
                ch_l "Думаю, как-нибудь свидимся. . ."
        $ LauraX.Traits.remove("switchcheck")
        $ LauraX.AddWord(1,0,0,0,"switched") #history
        return

label Laura_Switch2:
        #when you switch for a 2+ time
        $ LauraX.FaceChange("smile", 1)
        ch_l "Хм, ты выглядишь как раньше."
        $ LauraX.Traits.remove("switchcheck")
        $ LauraX.History.remove("switched")
        $ LauraX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_Girltalk(Auto=0,Other=0):
        # if Auto Laura starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in LauraX.History:
                return
        if "nogirls" in LauraX.History:
                jump Laura_Girltalk_Redux
        $ LauraX.FaceChange("smile", 1)
        if Auto:
                ch_l "Слушай, [Player.Name]. . ."
        ch_l "Я тебе нравлюсь?"
        menu:
            extend ""
            "Да?":
                    $ LauraX.FaceChange("sly", 1)
                    $ LauraX.Statup("Love", 70, 2)
                    $ LauraX.Statup("Love", 90, 2)
                    $ LauraX.Statup("Obed", 70, 1)
                    ch_l "Понятно."
            "Возможно?":
                    $ LauraX.FaceChange("confused", 1)
                    $ LauraX.Statup("Love", 70, 1)
                    $ LauraX.Statup("Obed", 80, 2)
                    $ LauraX.Statup("Inbt", 80, 2)
                    ch_l "Правда? . ."
            "Не особо.":
                    $ LauraX.FaceChange("sly", 1)
                    $ LauraX.Statup("Love", 90, -1)
                    $ LauraX.Statup("Obed", 60, 2)
                    $ LauraX.Statup("Obed", 80, 2)
                    ch_l "Угу-м. . ."
        $ LauraX.FaceChange("sly", 1)
        if not ApprovalCheck(LauraX, 1000) and not LauraX.Les:
                ch_l "Эм. . . не сейчас."
                $ LauraX.AddWord(1,0,0,0,"nogirls") #history
                call Girltalk_Check(LauraX)
                return
        ch_l "Я даже отсюда чувствую, что от тебя исходит."
        ch_l "Думаю, я тоже испытываю к тебе подобное влечение. . ."
        ch_l "Вкус мне не особо важен, если ты понимаешь о чем я. . ."
        $ LauraX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(LauraX)
        return

label Laura_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing
        if ApprovalCheck(LauraX, 1000):
                $ LauraX.FaceChange("sly", 1)
                if Other in TotalGirls and "nogirls" in Other.History:
                        ch_l "Я не уверена. . ."
                ch_l ". . . хорошо."
                ch_l "Думаю, я тоже испытываю к тебе подобное влечение. . ."
                ch_l "Вкус мне не особо важен, если ты понимаешь о чем я. . ."
                $ LauraX.DrainWord("nogirls",0,0,0,1) #history
                $ LauraX.AddWord(1,0,0,0,"girltalk") #history
        elif "nogirls" not in LauraX.History:
                $ LauraX.AddWord(1,0,0,0,"nogirls") #history
                ch_l "Эм. . . не сейчас."
        elif "nogirls" in LauraX.DailyActions:
                $ LauraX.FaceChange("angry", 1)
                if LauraX.Forced:
                        #if Forced, she will just go with it anyway
                        if "nogirls" not in LauraX.RecentActions:
                                $ LauraX.Statup("Love", 80, -2)
                                $ LauraX.Statup("Obed", 80, 2)
                                $ LauraX.AddWord(1,"nogirls",0,0,0) #recent
                        return
                ch_l "Back off."
        else:
                $ LauraX.Statup("Inbt", 50, 2)
                ch_l "Сейчас мне это неинтересно."
                $ LauraX.AddWord(1,0,"nogirls",0,0) #daily
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_69_Intro:
        if "69" in LauraX.History:
                return
        if Trigger == "lick pussy" and LauraX.LickP:
                if LauraX.Blow or LauraX.CUN or (ApprovalCheck(LauraX, 1300) and LauraX.SeenPeen):
                        #if licking pussy but have gotten blowjob
                        $ LauraX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_l "Слушай, у меня появилась идея. . ."
                        "Она прижимает вас к полу и забирается на вас сверху."
                        if "cockout" not in Player.RecentActions:
                                $ Player.RecentActions.append("cockout")
                                if Player.Male:
                                        "Она вытаскивает ваш член и начинает его сосать."
                                else:
                                        "Она обнажает вашу киску и начинает лизать ее."
                        else:
                                if Player.Male:
                                        "Она берет в руки ваш член и располагается над ним."
                                else:
                                        "Она начинает лизать вашу киску."
                        $ LauraX.Pose = "69"
                        call Laura_BJ_Launch
                        ch_l "Ладно, [LauraX.Petname], приступай. . ."
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ LauraX.Statup("Love", 95, 3)
                                    $ LauraX.Statup("Inbt", 70, 2)
                                    $ LauraX.Statup("Inbt", 90, 1)
                                    ch_l "Хорошо."
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ LauraX.Statup("Love", 80, -8)
                                    $ LauraX.Statup("Obed", 80, 3)
                                    $ LauraX.Statup("Obed", 90, 1)
                                    $ LauraX.Statup("Inbt", 70, -1)
                                    if not Player.Male:
                                        ch_l "Овца."
                                    else:
                                        ch_l "Козел."
                        $ Situation = "69"
                        call SexAct("blow") # call Laura_SexAct("blow")
                        $ renpy.pop_call() #causes it to skip past the Escalation
                        $ renpy.pop_call() #causes it to skip past the last activity
        elif (Trigger == "blow" or Trigger == "cun") and (LauraX.Blow or LauraX.CUN):
                        #if licked pussy
                        $ LauraX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_l "Слушай, пока я занята. . ."
                        "Она прижимает вас к полу и забирается на вас сверху."
                        $ LauraX.Pose = "69"
                        call Laura_BJ_Launch
                        if not Player.Male:
                            ch_l ". . .не могла бы и ты сделать мне приятно? . ."
                        else:
                            ch_l ". . .не мог бы и ты сделать мне приятно? . ."
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ LauraX.Statup("Love", 95, 3)
                                    $ LauraX.Statup("Inbt", 70, 2)
                                    $ LauraX.Statup("Inbt", 90, 1)
                                    ch_l "Хорошо."
                                    if not LauraX.LickP:
                                        $ LauraX.LickP += 1
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ LauraX.Statup("Love", 80, -5)
                                    $ LauraX.Statup("Obed", 80, 3)
                                    $ LauraX.Statup("Obed", 90, 1)
                                    $ LauraX.Statup("Inbt", 70, -1)
                                    if not Player.Male:
                                        ch_l "Овца."
                                    else:
                                        ch_l "Козел."
                        #returns to BJ already in progress
        return
