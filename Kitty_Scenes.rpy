# start KittyMeet //////////////////////////////////////////////////////////


label KittyMeet:
        $ bg_current = "bg campus"
        $ KittyX.OutfitDay = "casual1"
        $ KittyX.Outfit = "casual1"
        $ KittyX.OutfitChange("casual1")
        call CleartheRoom("All",0,1)
        $ KittyX.Loc = "bg kitty"
        $ KittyX.Love = 400
        $ KittyX.Obed = 100
        $ KittyX.Inbt = 0
        call Shift_Focus(KittyX)
        call Set_The_Scene(0)
        $ KittyX.SpriteLoc = StageCenter
        $ KittyX.Petname = Player.Name[:1]  #fix test this
        $ KittyX.Petname_rod = Player.Name[:1]
        $ KittyX.Petname_dat = Player.Name[:1]
        $ KittyX.Petname_vin = Player.Name[:1]
        $ KittyX.Petname_tvo = Player.Name[:1]
        $ KittyX.Petname_pre = Player.Name[:1]
        $ KittyX.Name = "Китти"
        $ KittyX.Name_rod = "Китти"
        $ KittyX.Name_dat = "Китти"
        $ KittyX.Name_vin = "Китти"
        $ KittyX.Name_tvo = "Китти"
        $ KittyX.Name_pre = "Китти"

        "Спеша на занятия, вы замечаете одну студентку, бегущую прямо на вас."
        "Вы пытаетесь уступить дорогу, но вам не достает скорости, чтобы уйти с ее пути,"
        "Она врезается в вас на полном ходу и вы вместе падаете на землю."
        "Поднявшись на ноги, вы протягиваете девушке свою руку."
        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) with vpunch
        $ KittyX.Loc = "bg campus"
        $ KittyX.Statup("Love", 90, -25)
        $ KittyX.FaceChange("surprised")
        $ KittyX.ArmPose = 1
        ch_u "Эй!"
        $ KittyX.Brows = "angry"
        ch_u "Какого черта?"
        $ Player.AddWord(1,0,"Intro",0,0) #adds tag to Daily
        $ Cnt = 1

        menu:
            extend ""
            "Это ты в меня врезалась!":
                    $ KittyX.FaceChange("confused", 2)
                    $ KittyX.Statup("Love", 90, 5)
                    $ KittyX.Statup("Obed", 80, 20)
                    ch_u "Что-! А, ну, да. . ."
                    $ KittyX.Blush = 1
                    $ Cnt = 0
            "Извини.":
                    $ KittyX.FaceChange("bemused", 1)
                    $ KittyX.Eyes = "side"
                    $ KittyX.Statup("Love", 90, 25)
                    ch_u "Ну, пожалуй, это[KittyX.like]не совсем твоя вина. . ."
            "Счастливая случайность?":
                    $ KittyX.FaceChange("surprised", 2)
                    ch_u "  !  "
                    if Player.Male:
                            $ KittyX.FaceChange("bemused", 1)
                            $ KittyX.Statup("Love", 90, 15)
                            $ KittyX.Statup("Inbt", 70, 10)
                            ch_u "Хм. . . возможно. . ."
                    else:
                            $ KittyX.FaceChange("confused", 2)
                            $ KittyX.Statup("Love", 90, 5)
                            ch_u "Что? . ."
                            $ KittyX.FaceChange("bemused", 1)
                            $ KittyX.Statup("Love", 90, 10)
                            $ KittyX.Statup("Inbt", 70, 10)

        ch_p "Кстати, я [Player.Name]."
        if Cnt:
                $ KittyX.FaceChange("smile", 1)
                ch_k "А я Китти! Китти Прайд. Приятно познакомиться!"
        else:
                $ KittyX.FaceChange("sadside", 1)
                ch_k "Эм, а я Китти."
        $ KittyX.FaceChange("normal", 1)
        $ KittyX.Mouth = "sad"
        ch_k "Я просто[KittyX.like]не думала, что врежусь в тебя. Обычно я через все прохожу."

        menu:                                                               # + 5-10
            extend ""
            "Теряешь сноровку?":
                    $ KittyX.FaceChange("confused", 0)
                    $ KittyX.Statup("Obed", 80, 5)
                    ch_k "Не {i}думаю{/i}, что в этом дело. . ."
                    ch_p "Я просто шучу. . ."
                    $ KittyX.Statup("Love", 90, 5)
            "Засмотрелась на меня?":
                    $ KittyX.FaceChange("angry", 1, Brows = "normal")
                    $ KittyX.Statup("Love", 90, -2)
                    $ KittyX.Statup("Obed", 80, 8)
                    $ KittyX.Statup("Inbt", 70, 4)
                    ch_k "Еще чего."
                    ch_p "Ха, ну нет, так нет."
            "Все из-за моей способности.":
                    $ KittyX.FaceChange("confused", 0)
                    $ KittyX.Statup("Love", 90, 5)
                    ch_k "А?"

        ch_p "Я могу отключать силы других мутантов, поэтому ты не можешь пройти через меня."
        $ KittyX.FaceChange("perplexed", 0)
        ch_k "О! Вау, как интересно. То есть, если ты схватишь меня, то я не смогу вырваться?"

        menu:                                                               # +10
            extend ""
            "Хочешь попробовать?":
                    $ KittyX.FaceChange("perplexed", 0)
                    $ KittyX.Statup("Love", 90, 5)
                    $ KittyX.Statup("Inbt", 70, 5)
                    ch_k "Конечно, мне очень любопытно."
            "Наверное.":
                    $ KittyX.FaceChange("sadside", 0, Mouth = "lipbite")
                    $ KittyX.Statup("Obed", 80, 3)
                    $ KittyX.Statup("Inbt", 70, 7)
                    ch_k "Я бы хотела попробовать."
            "Тебя это заводит?":
                    $ KittyX.FaceChange("surprised", 2)
                    $ KittyX.Statup("Obed", 80, 5)
                    ch_k "Что?! Нет! . ."
                    $ KittyX.FaceChange("bemused", 1)
                    $ KittyX.Statup("Inbt", 70, 5)
                    $ KittyX.Eyes = "side"
                    ch_k ". . . нет."
                    $ KittyX.Eyes = "sexy"
                    ch_k "Но твою способность[KittyX.like]стоит испытать."

        ch_p "Хорошо, давай попробуем."
        "Вы протягиваете руку и берете ее за запястье."
        $ KittyX.FaceChange("angry", 1, Eyes = "down")
        $ KittyX.Addictionrate += 2
        "Она некоторое время пытается вырваться, но вы держите ее крепко."
        $ Cnt = 0
        while Cnt < 3:
            menu:
                extend ""
                "Отпустить ее.":
                        if not Cnt:                                     #you let go instantly
                                $ KittyX.Statup("Love", 90, 7)
                                $ KittyX.Statup("Inbt", 70, -2)
                        elif Cnt == 1:                                  #she just asked you to let go
                                $ KittyX.Statup("Love", 90, 10)
                        else:                                           #you let go after a pause
                                $ KittyX.Statup("Love", 90, 5)
                        "Вы отпускаете ее руку и отступаете на шаг назад."
                        $ Cnt = 4
                "Продолжать держать.":
                        "Вы продолжаете держать ее руку, она начинает слегка нервничать."
                        if not Cnt:
                                $ KittyX.Eyes = "sexy"
                                ch_k "Ты скоро[KittyX.like]отпустишь?"
                        elif Cnt == 2:
                                ch_k "Ладно, хватит!"
                                $ KittyX.Eyes = "sexy"
                                $ KittyX.Statup("Love", 90, -10)
                                $ KittyX.Statup("Obed", 80, -5)
                                $ KittyX.Statup("Inbt", 70, 10)
                                "Она хватает вашу руку и разжимает ладонь."
                                $ Cnt = 4
                        else:
                                $ KittyX.Statup("Love", 90, -1)
                                $ KittyX.Statup("Obed", 80, 2)
                                "Эм. . ."
                        $ Cnt += 1
                        $ KittyX.Addictionrate += 1

                "Притянуть ее и обнять.":
                        $ KittyX.Statup("Love", 90, -5)
                        $ KittyX.FaceChange("surprised", 2)
                        ch_k "Эй! Это, как бы, не круто!"
                        $ KittyX.FaceChange("angry", 1)
                        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) with vpunch
                        "Она бьет вас локтем под ребра и отталкивает на несколько шагов назад."
                        $ KittyX.Statup("Inbt", 70, 10)
                        ch_k "Мои способности могут и не действовать на тебя, но у меня, в отличии от тебя[KittyX.like]несколько лет боевого опыта за плечами."
                        ch_k "Не забывай!"
                        $ Cnt = 10

        if Cnt > 3:
            $ KittyX.Eyes = "side"
            ch_k "Ну, это был интересный опыт. . ."
        else:
            $ KittyX.FaceChange("bemused", 1, Eyes = "side")
            ch_k "Это был интересный опыт. . ."
        $ KittyX.Eyes = "sexy"
        $ KittyX.Mouth = "lipbite"
        ch_k "Мне было немного щекотно. . ."

        $ Cnt = 0
        $ KittyX.FaceChange("surprised", Mouth = "kiss")
        ch_k "Ох! Я[KittyX.like]совсем забыла, мне нужно бежать на брифинг!"
        if Cnt < 5:
                $ KittyX.FaceChange("smile")
                ch_k "Увидимся! Пока!"
        else:
                $ KittyX.FaceChange("normal")
                ch_k "Ну, наверное, как-нибудь свидимся! Пока!"

        $ KittyX.Loc = "bg kitty"
        call Set_The_Scene

        "Она убегает, а вы продолжаете свой путь до аудитории."
        $ KittyX.History.append("met")
        $ ActiveGirls.append(KittyX) if KittyX not in ActiveGirls else ActiveGirls
        $ bg_current = "bg classroom"
        $ Round -= 10
        call Shift_Focus(RogueX)
        return

# end KittyMeet //////////////////////////////////////////////////////////

# Event Kitty_Key /////////////////////////////////////////////////////

#Not updated

label Kitty_Key:
            call Shift_Focus(KittyX)
            $ KittyX.Loc = bg_current
            call Set_The_Scene
            $ KittyX.FaceChange("bemused")
            $ KittyX.ArmPose = 2
            $ Event_Queue = [0,0]
            ch_k "Итак, ты[KittyX.like]в последнее время, частенько заглядываешь ко мне, поэтому я подумала, что тебе может пригодиться ключ. . ."
            ch_p "Спасибо."
            "Она вручает вам ключ от своей комнаты."
            $ KittyX.ArmPose = 1
            $ Keys.append(KittyX) if KittyX not in Keys else Keys
            $ KittyX.Event[0] = 1
            return
# end Event Kitty_Key /////////////////////////////////////////////////////

# start Kitty_BF//////////////////////////////////////////////////////////

#Not updated
label Kitty_BF:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(KittyX,"bemused","краснеет. . .")
            return
    call Shift_Focus(KittyX)
    $ KittyX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    if KittyX.Loc != bg_current:
            $ KittyX.Loc = bg_current
            if KittyX not in Party:
                    "[KittyX.Name] подходит к вам и спрашивает, можете ли вы поговорить."
            else:
                    "[KittyX.Name] поворачивается к вам и спрашивает, можете ли вы поговорить."

    $ Event_Queue = [0,0]
    call Set_The_Scene(0)
    call Display_Girl(KittyX)
    $ KittyX.DailyActions.append("relationship")
    if not Player.Male and "girltalk" not in KittyX.History:
            call expression KittyX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
            return
    "Легкий румянец на щеках выдает ее волнение о предстоящем разговоре."
    call Taboo_Level
    call CleartheRoom(KittyX)
    $ KittyX.FaceChange("bemused", 1)

    if not Player.Male:
        ch_k "Так вот, [KittyX.Petname], мы[KittyX.like]частенько проводим время вместе, согласна?"
    else:
        ch_k "Так вот, [KittyX.Petname], мы[KittyX.like]частенько проводим время вместе, согласен?"
    ch_k ". . ."
    $ KittyX.Eyes = "sexy"
    menu:
        "Ага. И это потрясающе.":
                $ KittyX.Statup("Love", 200, 20)
        "Ага, наверное.":
                $ KittyX.Statup("Love", 200, 10)
        "Эм. . . возможно?":
                $ KittyX.Statup("Love", 200, -10)
                $ KittyX.Statup("Obed", 200, 30)
    if KittyX.SEXP >= 10:
            ch_k "Я хочу сказать, что я зашла с тобой дальше, чем с кем-либо прежде. . ."
    if KittyX.SEXP >= 15:
            ch_k "Ну, ты понимаешь[KittyX.like]в. . . {i}спальне{/i}. . ."
    if len(Player.Harem) >= 2:
            ch_k "Знаю[KittyX.like]что ты обхаживаешь всех и вся. . ."
    elif RogueX in Player.Harem:
        if "dating?" in KittyX.Traits:
                if not Player.Male:
                    ch_k "Я знаю, что ты[KittyX.like]девушка [RogueX.Name] и все такое. . . но мы[KittyX.like]разговорились и. . ."
                else:
                    ch_k "Я знаю, что ты[KittyX.like]парень [RogueX.Name] и все такое. . . но мы[KittyX.like]разговорились и. . ."
        else:
                if not Player.Male:
                    ch_k "Я знаю, что ты[KittyX.like]девушка [RogueX.Name] и все такое. . ."
                else:
                    ch_k "Я знаю, что ты[KittyX.like]парень [RogueX.Name] и все такое. . ."
    elif Player.Harem:
                ch_k "Я знаю, что ты[KittyX.like]встречаешься с [Player.Harem[0].Name_tvo] и все такое. . ."

    if KittyX in Player.Harem:
            #if she somehow already ended up in the harem
            ch_k "-но я рада, что тоже могу быть с тобой. . ."
            if "KittyYes" in Player.Traits:
                    $ Player.Traits.remove("KittyYes")
            if "boyfriend" not in KittyX.Petnames:
                    $ KittyX.Petnames.append("boyfriend")
            return

    if not KittyX.Event[5]:
            ch_k "Так что, эм. . ."
            ch_k "Не то чтобы я[KittyX.like]раньше ни с кем не встречалась. . ."
            ch_k "Просто. . . фух, мне[KittyX.like]так неловко. Ты мне действительно очень нравишься и. . ."
            if not Player.Male:
                ch_k "Я хочу спросить. . . ты станешь[KittyX.like]моей девушкой?"
            else:
                ch_k "Я хочу спросить. . . ты станешь[KittyX.like]моим парнем?"
            ch_k "[KittyX.Like]официально?"
    elif "dating?" in KittyX.Traits:
            ch_k "[RogueX.Name] сказала, что было бы здорово, если бы мы[KittyX.like]тоже начали встречаться."
    elif Player.Harem:
            ch_k "Если ты не против. . . я бы тоже хотела стать твоей девушкой."
    else:
            if not Player.Male:
                ch_k "Хотела бы я, чтобы ты[KittyX.like]поменьше вела себя как стерва, но все равно. . . Я абсолютно серьезна."
            else:
                ch_k "Хотела бы я, чтобы ты[KittyX.like]поменьше вел себя как козел, но все равно. . . Я абсолютно серьезна."
            ch_k "Я хочу стать твоей девушкой[KittyX.like]официально."
    $ KittyX.Event[5] += 1
    menu:
        extend ""
        "Ты шутишь? Мне бы тоже этого хотелось!":
                $ KittyX.Statup("Love", 200, 30)
                "[KittyX.Name] обнимает вас и страстно целует."
                $ KittyX.FaceChange("kiss")
                call Girl_Kissing_Launch(KittyX,"kiss you")
                $ KittyX.Kissed += 1
        "Эм[KittyX.like]ладно.":
                $ KittyX.Brows = "confused"
                "Кажется, [KittyX.Name] немного растроена от того, насколько небрежно вы к ней отнеслись."
                "Но все равно, она, наверное, решает, что это хороший первый шаг в ваших отношениях, поскольку она подходит к вам и нежно обнимает."
        "У меня сейчас кое-кто есть." if Player.Harem:
            $ KittyX.FaceChange("sad",1)
            ch_k "Знаю. Я просто. . . Я просто подумала, может ты[KittyX.like]сможешь встречаться и со мной тоже?"
            menu:
                extend ""
                "Да. Конечно." if "KittyYes" in Player.Traits:
                        $ KittyX.Statup("Love", 200, 30)
                        "[KittyX.Name] обнимает вас и страстно целует."
                        $ KittyX.FaceChange("kiss")
                        call Girl_Kissing_Launch(KittyX,"kiss you")
                        $ KittyX.Kissed += 1
                "Она этого не поймет." if len(Player.Harem) == 1:
                        $ Line = "no"
                "Они этого не поймут." if len(Player.Harem) > 1:
                        $ Line = "no"
                "Извини, но. . . нет." if KittyX.Event[5] != 20:
                        $ Line = "no"
                "Ни за что.":
                        jump Kitty_BF_Jerk
            if Line == "no":
                        $ KittyX.Statup("Love", 200, -10)
                        ch_k "Ну. . . ладно. Я все понимаю."
                        $ KittyX.Event[5] = 20
                        call Remove_Girl(KittyX)
                        $ Line = 0
                        return
        "Мне как-то этого не хочется.":
                        jump Kitty_BF_Jerk

    if "Historia" not in Player.Traits:
            $ Player.Harem.append(KittyX)
            if "KittyYes" in Player.Traits:
                    $ Player.Traits.remove("KittyYes")
    $ KittyX.Petnames.append("boyfriend")
    $ KittyX.FaceChange("sexy")
    if not Player.Male:
        ch_k "А теперь. . . моя девушка. . . как насчет вместе это[KittyX.like]отпраздновать, м?"
    else:
        ch_k "А теперь. . . мой парень. . . как насчет вместе это[KittyX.like]отпраздновать, м?"
    if "Historia" in Player.Traits:
            return 1
    $ Tempmod = 10
    $ Player.AddWord(1,"interruption") #adds to Recent
    call SexMenu
    $ Tempmod = 0
    return

label Kitty_BF_Jerk:
    $ KittyX.FaceChange("angry", 1)
    ch_k "Ладно![KittyX.Like]пусть будет по-твоему!"
    $ KittyX.Statup("Obed", 50, 40)
    if KittyX.Event[5] != 20:
            $ KittyX.Statup("Obed", 200, (20* KittyX.Event[5]))
    if 20 > KittyX.Event[5] >= 3:
            $ KittyX.FaceChange("sad")
            ch_k "Ах так?  Ну. . . мне[KittyX.like]все равно, чего ты хочешь! Мы встречаемся! И точка."
            ch_k "Я. . . эмм. . . думаю, что мне нужно[KittyX.like]побыть одной."
            if "Historia" in Player.Traits:
                    return 1
            $ KittyX.Petnames.append("boyfriend")
            $ Achievements.append("I am not your Boyfriend!")
            $ bg_current = "bg player"
            call Remove_Girl(KittyX)
            call Set_The_Scene
            $ renpy.pop_call()
            jump Player_Room
    if KittyX.Event[5] > 1:
            if not Player.Male:
                ch_k "Зря я решила тебя снова об этом спросить. Ты[KittyX.like]все такая же дура!"
            else:
                ch_k "Зря я решила тебя снова об этом спросить. Ты[KittyX.like]все такой же придурок!"
    if KittyX.Event[5] != 20:
            $ KittyX.Statup("Love", 200, -(50* KittyX.Event[5]))
    else:
            $ KittyX.Statup("Love", 200, -50)
    ch_k "Убирайся, ничтожество!"
    if "Historia" in Player.Traits:
            return
    $ bg_current = "bg player"
    call Remove_Girl(KittyX)
    $ renpy.pop_call()
    jump Player_Room

## end Kitty_BF//////////////////////////////////////////////////////////

## start Kitty_Love//////////////////////////////////////////////////////////
label Kitty_Love:
    #First time through, KittyX.Event[6] is 0, each time adds 1, automatically ends at 5,
    # it gets set at 20 if you refuse her advances, if it's 25 it means you've asked for a second chance and been refused
    call Shift_Focus(KittyX)
    $ KittyX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    if KittyX.Event[6]:
            #on repeat attempts
            "[KittyX.Name], выглядя немного смущенной, подходит к вам, набравшись смелости."
    if bg_current != "bg kitty" and bg_current != "bg player":
        if KittyX.Loc == bg_current or KittyX in Party:
            "Вдруг [KittyX.Name] изъявляет желание поговорить с вами в своей комнате и ведет вас туда."
        else:
            "Вдруг [KittyX.Name] появляется рядом и изъявляет желание поговорить с вами в своей комнате, затем сразу же ведет вас туда."
        $ bg_current = "bg kitty"
    else:
            "Вдруг [KittyX.Name] пристально начинает на вас пялиться."

    $ Event_Queue = [0,0]
    $ KittyX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(KittyX)
    call CleartheRoom(KittyX)
    call Taboo_Level
    $ KittyX.DailyActions.append("relationship")
    $ KittyX.FaceChange("bemused", 1)
    $ KittyX.Eyes = "side"
    $ Line = 0
    $ KittyX.Event[6] += 1
    if KittyX.Event[6] == 1:
            if KittyX in Player.Harem:
                ch_k "Мы[KittyX.like]частенько проводим время вместе, поэтому я подумала. . ."
            else:
                ch_k "Мы[KittyX.like]уже давно знакомы, поэтому я подумала. . ."
            ch_k "Знаешь, я очень тяжело[KittyX.like]схожусь с людьми. . ."
            $ KittyX.Eyes = "down"
            ch_k ". . . мне не часто[KittyX.like]бывает с ними комфортно, я редко могу быть с ними самой собой. . ."
            $ KittyX.Eyes = "sly"
            ch_k "Иногда я чувствую, что между тобой. . ."
            $ KittyX.Eyes = "side"
            ch_k "и[KittyX.like]мной . ."
            $ KittyX.FaceChange("perplexed", 2)
            $ KittyX.Eyes = "surprised"
            ch_k "Забудь!"
            "Китти убегает сквозь ближайшую стену."
            hide Kitty_Sprite with easeoutright
            call Remove_Girl(KittyX)
            jump Misplaced
            return
    if KittyX.Event[6] == 2:
        ch_k "Извини за случившееся, думаю, я тогда была не готова. . ."
        ch_k ". . . но я все обдумала и-"
    elif KittyX.Event[6] >= 5:
        ch_k "Эм. . ."
        $ KittyX.Eyes = "sly"
        ch_k "Ладно, пора перестать все время убегать. Я думаю, что люблю тебя."
        $ KittyX.Eyes = "side"
        ch_k "Тебе не обязательно отвечать, но знай, что это так."
        $ KittyX.Petnames.append("lover")
        ch_k "Эм, вот и все."
    else:
        ch_k "Эм. . ."
    if "lover" not in KittyX.Petnames:
            menu:
                "Она поворачивается с намерением пройти через ближайшую стену."
                "Поймать ее":
                    $ KittyX.FaceChange("perplexed", 2)
                    $ KittyX.Eyes = "surprised"
                    $ KittyX.Statup("Love", 95, 10)
                    $ KittyX.Statup("Obed", 95, 15)
                    "Когда она поворачивается, вы хватаете ее за руку. Не ожидая этого, она даже слегка вскрикивает."
                "Пусть уходит":
                    "Добежав до ближайшей стены, она скрывается за ней."
                    jump Kitty_Love_End
            $ KittyX.Blush = 1
            menu:
                extend ""
                "Притянуть ее к себе":
                    $ KittyX.FaceChange("smile", 1)
                    $ KittyX.Statup("Love", 95, 20)
                    "Вы притягиваете ее и обнимаете, крепко обхватив за талию."
                    $ Line = "hug"
                "Ничего не делать":
                    $ KittyX.Eyes = "down"
                    $ KittyX.Statup("Obed", 95, 10)
                    "Вы продолжаете держать ее за запястье."
                    $ Line = "wrist"
                "Отпустить ее":
                    if 1 < KittyX.Event[6] < 4:
                        "Вы немедленно отпускаете ее запястье."
                        $ KittyX.Eyes = "down"
                        "Она просачивается сквозь ближайшую стену и исчезает за ней."
                        jump Kitty_Love_End
                    else:
                        $ KittyX.Statup("Love", 95, 10)
                        $ KittyX.Statup("Obed", 95, 20)
                        $ KittyX.Statup("Inbt", 80, 20)
                        "Вы отпускаете ее запястье, и она отходит на шаг назад."

            ch_k "Я. . . прости, я просто немного запаниковала."
    if "lover" not in KittyX.Petnames:
            # If she hasn't confessed yet
            ch_k "Я подумала, что если позволю себе сблизиться с кем-то. . ."
            ch_k "Я оступлюсь. . ."
            menu:
                extend ""
                "Я тебя никогда не отпущу." if Line:
                        $ KittyX.Statup("Love", 95, 20)
                        $ KittyX.Statup("Inbt", 80, 10)
                        "Она отдается вашим объятиям."
                "Я никогда не позволю этому случиться.":
                        $ KittyX.FaceChange("smile")
                        $ KittyX.Statup("Love", 95, 20)
                        $ KittyX.Statup("Obed", 80, 15)
                        "Она улыбается вам, слегка смущаясь."
                "Ага, тебе стоит этого остерегаться.":
                        $ KittyX.FaceChange("angry", 1)
                        $ KittyX.RecentActions.append("angry")
                        $ KittyX.Statup("Love", 200, -20)
                        $ KittyX.Statup("Obed", 80, 10)
                        $ KittyX.Statup("Inbt", 80, 10)
                        "Она отталкивает вас, а затем со злостью на лице проходит через ближайшую стену."
                        jump Kitty_Love_End

                "Ладно, можешь идти. [[Подтолкнуть ее]":
                        $ KittyX.FaceChange("surprised", 1)
                        $ KittyX.Statup("Love", 200, -50)
                        $ KittyX.Statup("Obed", 80, 10)
                        $ KittyX.Statup("Inbt", 80, 10)
                        "Вы подталкиваете ее к ближайшей стене и отправляетесь дальше по своим делам."
                        $ KittyX.RecentActions.append("angry")
                        hide Kitty_Sprite with easeoutbottom
                        jump Kitty_Love_End

    if "lover" in KittyX.Petnames:
        #if she made the first move
        menu:
            extend "" #"I love you."
            "Я тоже тебя люблю.":
                            $ KittyX.Statup("Love", 200, 40)
                            $ KittyX.Statup("Inbt", 200, 50)
                            $ KittyX.FaceChange("smile")
            "Ты любишь меня?":
                $ KittyX.FaceChange("confused", 2)
                menu:
                    ch_k "А ты разве меня не любишь?"
                    "Конечно люблю!":
                            $ KittyX.Statup("Love", 200, 30)
                            $ KittyX.Statup("Inbt", 200, 60)
                            $ KittyX.FaceChange("smile")
                    "Может быть, немного?":
                            $ KittyX.Statup("Obed", 80, 20)
                            $ KittyX.Statup("Inbt", 80, -10)
                            ch_k "Значит, \"нет\". . ."
                            $ Line = "awkward"
                    "Не особо.":
                            $ KittyX.Statup("Love", 200, -30)
                            $ KittyX.Statup("Obed", 80, 30)
                            $ KittyX.Statup("Inbt", 80, -30)
                            $ KittyX.FaceChange("angry", 2)
                            ch_k "А?!"
                            $ Line = "awkward"
            "Хм.":
                $ KittyX.Statup("Love", 200, -10)
                $ KittyX.Statup("Obed", 80, 10)
                $ KittyX.Statup("Inbt", 80, -20)
                menu:
                    ch_k "Хм?!"
                    "Я хотела сказать, я тоже тебя люблю!" if not Player.Male:
                            $ KittyX.Statup("Love", 200, 30)
                            $ KittyX.Statup("Inbt", 80, 10)
                            $ KittyX.FaceChange("smile")
                            ch_k "Ну и зачем было тянуть до последнего. . ?"
                    "Я хотел сказать, я тоже тебя люблю!" if Player.Male:
                            $ KittyX.Statup("Love", 200, 30)
                            $ KittyX.Statup("Inbt", 80, 10)
                            $ KittyX.FaceChange("smile")
                            ch_k "Ну и зачем было тянуть до последнего. . ?"
                    "В странную ситуацию я угодила." if not Player.Male:
                            $ KittyX.Statup("Love", 200, -20)
                            $ KittyX.Statup("Obed", 80, 30)
                            $ KittyX.Statup("Inbt", 80, -20)
                            $ KittyX.FaceChange("angry", 2)
                            $ Line = "awkward"
                    "В странную ситуацию я угодил." if Player.Male:
                            $ KittyX.Statup("Love", 200, -20)
                            $ KittyX.Statup("Obed", 80, 30)
                            $ KittyX.Statup("Inbt", 80, -20)
                            $ KittyX.FaceChange("angry", 2)
                            $ Line = "awkward"
            "В странную ситуацию я угодила." if not Player.Male:
                            $ KittyX.Statup("Love", 200, -30)
                            $ KittyX.Statup("Obed", 80, 40)
                            $ KittyX.Statup("Inbt", 80, -20)
                            $ KittyX.FaceChange("perplexed", 2)
                            $ Line = "awkward"
            "В странную ситуацию я угодил." if Player.Male:
                            $ KittyX.Statup("Love", 200, -30)
                            $ KittyX.Statup("Obed", 80, 40)
                            $ KittyX.Statup("Inbt", 80, -20)
                            $ KittyX.FaceChange("perplexed", 2)
                            $ Line = "awkward"
    else:
        menu:
            extend ""
            "Я люблю тебя, [KittyX.Name].":
                        $ KittyX.Statup("Love", 200, 50)
                        $ KittyX.Statup("Inbt", 80, 30)
                        $ KittyX.FaceChange("smile")
                        $ Line = "love"
            "Я считаю, что ты прекрасна.":
                $ KittyX.FaceChange("confused")
                menu:
                    ch_k "Но разве меня не любишь?"
                    "Конечно люблю!":
                                $ KittyX.Statup("Love", 200, 30)
                                $ KittyX.Statup("Obed", 50, 10)
                                $ KittyX.Statup("Inbt", 80, 20)
                                $ KittyX.FaceChange("smile")
                    "Может быть, немного?":
                        if ApprovalCheck(KittyX, 1200, "OI"):
                                $ KittyX.FaceChange("sad")
                                $ KittyX.Statup("Love", 200, -30)
                                $ KittyX.Statup("Obed", 90, 20)
                                $ KittyX.Statup("Inbt", 80, 10)
                                ch_k "Ну[KittyX.like]хотя бы так. . ."
                        else:
                                $ Line = "awkward"
                    "Не особо.":
                        $ KittyX.FaceChange("sad")
                        if ApprovalCheck(KittyX, 1500, "OI"):
                                $ KittyX.Statup("Love", 200, -30)
                                $ KittyX.Statup("Obed", 50, 30)
                                ch_k "Ауч. . ."
                        else:
                                $ Line = "awkward"
            "Я не придаю особого значения нашим отношениям. . .":
                        $ KittyX.FaceChange("sad")
                        if ApprovalCheck(KittyX, 1200, "OI") or ApprovalCheck(KittyX, 700, "I"):
                                $ KittyX.Statup("Love", 200, -30)
                                $ KittyX.Statup("Obed", 90, 20)
                                $ KittyX.Statup("Inbt", 90, 30)
                                ch_k "Эм. . ."
                        else:
                                $ Line = "awkward"

    if Line == "awkward":
        if ApprovalCheck(KittyX, 700, "O"):
                ch_k "Ладно, между нами не обязательно должна быть любовь."
        elif ApprovalCheck(KittyX, 700, "I"):
                ch_k "Ладно, пусть между нами будет только секс."
        elif ApprovalCheck(KittyX, 1200, "OI"):
                ch_k "Ладно, пока мне и этого хватит."
        else:
                $ KittyX.Statup("Love", 200, -50)
                $ KittyX.Statup("Obed", 95, 50)
                $ KittyX.Statup("Inbt", 80, -50)
                ch_k "Ох, ну, если ты меня не любишь-"
                if not Player.Male:
                    ch_k "Ты не обязана любить меня, все нормально."
                else:
                    ch_k "Ты не обязан любить меня, все нормально."
                ch_k "Я просто, эм. . . забудь."
                if "Historia" not in Player.Traits:
                        $ KittyX.RecentActions.append("angry")
        $ KittyX.Event[6] = 20 #this means it shuts down future attempts
    else:
        if Line:
                # If you're holding her
                "Она сжимает вас еще крепче, тихонько ахая."
        else:
                "Она ныряет в ваши объятия, тихонько визгнув."
        if "lover" not in KittyX.Petnames:
                ch_k "Я тоже тебя люблю. . ."
                ch_k "И думаю, что уже давно."
                $ KittyX.Petnames.append("lover")

label Kitty_Love_End:
    if Line == "awkward" or "lover" not in KittyX.Petnames:
            hide Kitty_Sprite with easeoutright
            call Remove_Girl(KittyX)
            jump Misplaced
            return
    if not Player.Male:
        ch_k "Знаешь, я тут подумала. . . может, ты бы хотела. . ."
    else:
        ch_k "Знаешь, я тут подумала. . . может, ты бы хотел. . ."
    if bg_current != "bg player" and bg_current != "bg kitty":
            ch_k "Подожди, давай перенесем наш разговор  в более укромное местечко. . ."
            $ bg_current = "bg kitty"
            $ KittyX.Loc = bg_current
            call Set_The_Scene
            call CleartheRoom(KittyX)
            call Taboo_Level
            ch_k "Хорошо, как я говорила. . ."
    $ KittyX.Statup("Obed", 70, 10)
    $ Player.AddWord(1,"interruption") #adds to Recent
    menu:
        extend ""
        "Да, давай сделаем это. . . [[заняться сексом]":
                $ KittyX.Statup("Inbt", 30, 30)
                ch_k "Ммм. . ."
                if "Historia" in Player.Traits:
                        return 1
                call SexAct("sex") # call Kitty_SexAct("sex")
        "У меня есть другая идея. . .[[выбрать другое занятие]":
                $ KittyX.Brows = "confused"
                $ KittyX.Statup("Obed", 70, 20)
                ch_k "Например. . ?"
                if "Historia" in Player.Traits:
                        return 1
                $ Tempmod = 20
                call SexMenu
    jump Misplaced

label Kitty_Love_Redux:
    #this is for if you rejected her but want a second chance
    $ Line = 0
    call Shift_Focus(KittyX)
    $ KittyX.DailyActions.append("relationship")
    if KittyX.Event[6] >= 25:
            #if this is the second time through
            ch_p "Надеюсь, ты меня простила, я все еще люблю тебя."
            $ KittyX.Statup("Love", 95, 10)
            if ApprovalCheck(KittyX, 950, "L"):
                    $ Line = "love"
            else:
                    $ KittyX.FaceChange("sad")
                    if not Player.Male:
                        ch_k "Ты сама загнала себя в очень глубокую яму, [KittyX.Petname]."
                    else:
                        ch_k "Ты сам загнал себя в очень глубокую яму, [KittyX.Petname]."
                    ch_k "Но можешь попытаться выбраться."
    else:
            if not Player.Male:
                ch_p "Помнишь, я сказала тебе, что не люблю тебя?"
            else:
                ch_p "Помнишь, я сказал тебе, что не люблю тебя?"
            $ KittyX.FaceChange("perplexed",1)
            ch_k "Эм, ДА?!"
            menu:
                "Прости, я не хотела так говорить." if not Player.Male:
                        $ KittyX.Eyes = "surprised"
                        ch_k "Ну, если ты. . . так, погоди, то есть, ты любишь меня?"
                        ch_p "Да. . . Да, я люблю тебя, [KittyX.Name]."
                        $ KittyX.Statup("Love", 200, 10)
                        if ApprovalCheck(KittyX, 950, "L"):
                                $ Line = "love"
                        else:
                                $ KittyX.FaceChange("sadside")
                                ch_k "Ну а теперь я уже не уверена. . ."
                "Прости, я не хотел так говорить." if Player.Male:
                        $ KittyX.Eyes = "surprised"
                        ch_k "Ну, если ты. . . так, погоди, то есть, ты любишь меня?"
                        ch_p "Да. . . Да, я люблю тебя, [KittyX.Name]."
                        $ KittyX.Statup("Love", 200, 10)
                        if ApprovalCheck(KittyX, 950, "L"):
                                $ Line = "love"
                        else:
                                $ KittyX.FaceChange("sadside")
                                ch_k "Ну а теперь я уже не уверена. . ."
                "Я передумала, я люблю тебя, так что. . ." if not Player.Male:
                    if ApprovalCheck(KittyX, 950, "L"):
                            $ Line = "love"
                            $ KittyX.Eyes = "surprised"
                            ch_k "Правда?!"
                    else:
                            $ KittyX.Mouth = "sad"
                            ch_k "О, так ты передумала. Замечательно."
                            $ KittyX.Statup("Inbt", 90, 10)
                            $ KittyX.FaceChange("sadside")
                            ch_k "Я, наверное, тоже. . ."
                "Я передумал, я люблю тебя, так что. . ." if Player.Male:
                    if ApprovalCheck(KittyX, 950, "L"):
                            $ Line = "love"
                            $ KittyX.Eyes = "surprised"
                            ch_k "Правда?!"
                    else:
                            $ KittyX.Mouth = "sad"
                            ch_k "О, так ты передумал. Замечательно."
                            $ KittyX.Statup("Inbt", 90, 10)
                            $ KittyX.FaceChange("sadside")
                            ch_k "Я, наверное, тоже. . ."
                "Эм, неважно.":
                            $ KittyX.Statup("Love", 200, -30)
                            $ KittyX.Statup("Obed", 50, 10)
                            $ KittyX.FaceChange("angry")
                            ch_k "Ты серьезно?"
                            $ KittyX.RecentActions.append("angry")
    if Line == "love":
            $ KittyX.Statup("Love", 200, 40)
            $ KittyX.Statup("Obed", 90, 10)
            $ KittyX.Statup("Inbt", 90, 10)
            $ KittyX.FaceChange("smile")
            ch_k "Я[KittyX.like]тоже люблю тебя!"
            if KittyX.Event[6] < 25:
                    $ KittyX.FaceChange("sly")
                    "Она бьет вас своим кулачком по плечу."
                    if not Player.Male:
                        ch_k "Долго же ты думала."
                    else:
                        ch_k "Долго же ты думал."
            $ KittyX.Petnames.append("lover")
    $ KittyX.Event[6] = 25
    return
## end Kitty_Love//////////////////////////////////////////////////////////


# start Kitty_Sub//////////////////////////////////////////////////////////

label Kitty_Sub:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(KittyX,"bemused","выглядит тихой. . .")
            return
    call Shift_Focus(KittyX)
    $ KittyX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    if KittyX.Loc != bg_current and KittyX not in Party:
            "Внезапно [KittyX.Name] появляется перед вами с явным желанием поговорить."

    $ Event_Queue = [0,0]
    $ KittyX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(KittyX)
    call CleartheRoom(KittyX)
    call Taboo_Level
    $ KittyX.DailyActions.append("relationship")
    if not Player.Male and "girltalk" not in KittyX.History:
            call expression KittyX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
            return
    $ KittyX.FaceChange("bemused", 1)

    $ Line = 0
    if not Player.Male:
        ch_k "Так вот, эм. . . в последнее время ты вроде как взяла полный контроль над нашими[KittyX.like]отношениями."
    else:
        ch_k "Так вот, эм. . . в последнее время ты вроде как взял полный контроль над нашими[KittyX.like]отношениями."
    menu:
        extend ""
        "Верно. Для меня это естественно.":
                $ KittyX.Statup("Obed", 200, 10)
                $ KittyX.Statup("Inbt", 50, 5)
        "Извини, мне не хотелось вести себя так.":
                $ KittyX.FaceChange("startled", 2)
                $ KittyX.Statup("Love", 80, 5)
                $ KittyX.Statup("Obed", 200, -5)
                $ KittyX.Statup("Inbt", 50, -5)
                if not Player.Male:
                    ch_k "Нет-нет! Ты не так меня поняла! Я просто. . ."
                else:
                    ch_k "Нет-нет! Ты не так меня понял! Я просто. . ."
        "Ага. Смирись.":
                if ApprovalCheck(KittyX, 1000, "LO"):
                        $ KittyX.Statup("Obed", 200, 20)
                        $ KittyX.Statup("Inbt", 50, 10)
                        ch_k "Эм, ага. . ."
                else:
                        $ KittyX.Statup("Love", 200, -10)
                        $ KittyX.Statup("Obed", 200, 10)
                        $ KittyX.Statup("Inbt", 50, 5)
                        $ KittyX.FaceChange("angry")
                        if not Player.Male:
                            ch_k "Я {i}хотела{/i} тебе сказать, что мне это как бы нравится.  Но я и подумать не могла, что ты станешь вести себя, как еще большая мразь!"
                        else:
                            ch_k "Я {i}хотела{/i} тебе сказать, что мне это как бы нравится.  Но я и подумать не могла, что ты станешь вести себя, как еще больший гондон!"
                        menu:
                            extend ""
                            "Похоже, ты меня не так хорошо знаешь, а?":
                                    ch_k "Похоже, что так."
                                    $ Line = "rude"
                            "Извини. Я думала, что ты хочешь, чтобы я была такой." if not Player.Male:
                                    $ KittyX.FaceChange("sexy", 2)
                                    $ KittyX.Eyes = "side"
                                    $ KittyX.Statup("Love", 95, 5)
                                    $ KittyX.Statup("Obed", 200, 5)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    ch_k ". . ."
                            "Извини. Я думал, что ты хочешь, чтобы я был таким." if Player.Male:
                                    $ KittyX.FaceChange("sexy", 2)
                                    $ KittyX.Eyes = "side"
                                    $ KittyX.Statup("Love", 95, 5)
                                    $ KittyX.Statup("Obed", 200, 5)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    ch_k ". . ."

    $ KittyX.Blush = 1
    if not Line:
            # She's advancing to the next stage
            if not Player.Male:
                ch_k "Ну, у меня, эм. . . до этого никогда не было девушки, которая бы так ко мне относилась. . ."
            else:
                ch_k "Ну, у меня, эм. . . до этого никогда не было парня, который бы так ко мне относился. . ."
            $ KittyX.FaceChange("sly", 2)
            ch_k "Мне это вроде как понравилось."
            $ KittyX.FaceChange("smile", 1)
            menu:
                extend ""
                "Хорошо. Если ты хочешь быть со мной, то выполняй мои приказы.":
                        if ApprovalCheck(KittyX, 1000, "LO"):
                            $ KittyX.Statup("Obed", 200, 15)
                            $ KittyX.Statup("Inbt", 50, 10)
                            ch_k "Ну, я вообщем-то и не против. . ."
                        else:
                            $ KittyX.FaceChange("sadside", 1)
                            $ KittyX.Statup("Love", 200, -5)
                            $ KittyX.Statup("Obed", 200, 10)
                            if not Player.Male:
                                ch_k "Тебе не надо быть такой[KittyX.like]{i}все{/i} время. Тебе стоит быть милой хоть иногда."
                            else:
                                ch_k "Тебе не надо быть таким[KittyX.like]{i}все{/i} время. Тебе стоит быть милым хоть иногда."
                            menu:
                                extend ""
                                "Плевать. Все так, как есть. Смирись или уходи.":
                                        $ KittyX.FaceChange("angry")
                                        $ KittyX.Statup("Love", 200, -10)
                                        $ KittyX.Statup("Obed", 200, 5)
                                        ch_k "Какое же ты ничтожество, [Player.Name]!"
                                        $ Line = "rude"
                                "Думаю, это я могу." :
                                        $ KittyX.FaceChange("bemused", 2)
                                        $ KittyX.Eyes = "side"
                                        $ KittyX.Statup("Love", 95, 5)
                                        $ KittyX.Statup("Obed", 200, 3)
                                        $ KittyX.Statup("Inbt", 50, 5)
                                        ch_k "Эмм. . . ага. Это[KittyX.like]даже. . . немного заводит."

                "Да? Так тебя это возбуждает?":
                                        $ KittyX.FaceChange("bemused", 2)
                                        $ KittyX.Eyes = "side"
                                        $ KittyX.Statup("Obed", 200, 5)
                                        $ KittyX.Statup("Inbt", 50, 10)
                                        ch_k "Эмм. . . ага. Это[KittyX.like]немного заводит."

                "Ты не находишь такие отношения странными?":
                        $ KittyX.FaceChange("startled", 1)
                        $ KittyX.Statup("Obed", 200, -5)
                        if not Player.Male:
                            ch_k "Только, если ты сама считаешь, что они[KittyX.like]странные. Мне же такое поведение кажется привлекательным."
                        else:
                            ch_k "Только, если ты сам считаешь, что они[KittyX.like]странные. Мне же такое поведение кажется привлекательным."
                        menu:
                            "Ну, если ты не против, то и я тоже.":
                                    $ KittyX.FaceChange("bemused", 2)
                                    $ KittyX.Statup("Love", 95, 10)
                                    $ KittyX.Statup("Inbt", 50, 10)
                                    $ Line = 0
                            "Эм. . . Для меня это слишком. Извини.":
                                    $ KittyX.Statup("Love", 200, -15)
                                    $ KittyX.Statup("Obed", 200, -5)
                                    $ KittyX.Statup("Inbt", 50, -10)
                                    $ Line = "embarrassed"

                "Меня не волнует, что тебе хочется. Я делаю то, что хочу.":
                            $ KittyX.Statup("Love", 200, -10)
                            $ KittyX.Statup("Obed", 200, 15)
                            $ KittyX.FaceChange("angry")
                            ch_k "Какое же ты ничтожество, [Player.Name]!"
                            $ Line = "rude"

    if not Line:
        $ KittyX.FaceChange("bemused", 1)
        $ KittyX.Eyes = "down"
        if not Player.Male:
            ch_k "Круто.  Так. . . чтобы ты знала. . . я не против, чтобы ты[KittyX.like]брала на себя контроль."
        else:
            ch_k "Круто.  Так. . . чтобы ты знал. . . я не против, чтобы ты[KittyX.like]брал на себя контроль."
        if "256 Shades of Grey" in KittyX.Inventory:
                    ch_k "Как в книге '256 оттенков серого'."
        menu Kitty_Sub_Choice:
            extend ""
            "Ты не считаешь такие отношения несколько. . . ненормальными?":
                    $ KittyX.Statup("Love", 200, -5)
                    $ KittyX.Statup("Inbt", 50, -15)
                    $ Line = "embarrassed"
            "Думаю, я смогу привыкнуть к таким отношениям.":
                    $ KittyX.Statup("Obed", 200, 5)
                    $ KittyX.Statup("Inbt", 50, 5)
                    $ KittyX.FaceChange("smile", 1)
                    $ Line = 0
            "Ты что, {i}прочитала{/i} ее?" if "256 Shades of Grey" in KittyX.Inventory and Line != "grey":
                    $ KittyX.Statup("Love", 95, 5)
                    $ KittyX.FaceChange("sly", 1)
                    if not Player.Male:
                        ch_k "А ты думала, что я не буду читать то, что ты сама же мне и подарила? {i}Наверное{/i}, ты не совсем понимаешь, насколько ты мне нравишься."
                    else:
                        ch_k "А ты думал, что я не буду читать то, что ты сам мне подарил? {i}Наверное{/i}, ты не совсем понимаешь, насколько ты мне нравишься."
                    $ KittyX.Statup("Inbt", 50, 5)
                    ch_k "Конечно я прочитала ее. И. . . как оказалось, она. . . {i}очень{/i} заводит."
                    ch_k "Ну. . . что думаешь? Ты не против таких[KittyX.like]отношений?"
                    $ Line = "grey"
                    jump Kitty_Sub_Choice

    if not Line:
        $ KittyX.FaceChange("smile", 1)
        if not Player.Male:
            ch_k "Круто. И. . . если хочешь, я могу[KittyX.like]звать тебя {i}госпожой{/i} или как-то так."
        else:
            ch_k "Круто. И. . . если хочешь, я могу[KittyX.like]звать тебя {i}господином{/i} или как-то так."
        $ KittyX.FaceChange("sly", 2)
        ch_k "Что скажешь?"
        $ KittyX.Blush = 1
        menu:
            extend ""
            "Мне нравится.":
                    $ KittyX.Statup("Love", 95, 5)
                    $ KittyX.Statup("Obed", 200, 15)
                    $ KittyX.Statup("Inbt", 50, 5)
                    if not Player.Male:
                        ch_k "Хорошо. . .{i}госпожа{/i}."
                    else:
                        ch_k "Хорошо. . .{i}господин{/i}."
                    if not Player.Male:
                        $ KittyX.Petname = "госпожа"
                        $ KittyX.Petname_rod = "госпожи"
                        $ KittyX.Petname_dat = "госпоже"
                        $ KittyX.Petname_vin = "госпожу"
                        $ KittyX.Petname_tvo = "госпожой"
                        $ KittyX.Petname_pre = "госпоже"
                    else:
                        $ KittyX.Petname = "господин"
                        $ KittyX.Petname_rod = "господина"
                        $ KittyX.Petname_dat = "господину"
                        $ KittyX.Petname_vin = "господина"
                        $ KittyX.Petname_tvo = "господином"
                        $ KittyX.Petname_pre = "господине"
            "Не надо меня так звать, ладно?":
                $ KittyX.FaceChange("startled", 2)
                ch_k "Ох!"
                $ KittyX.Statup("Inbt", 50, -5)
                $ KittyX.FaceChange("sadside", 1)
                if not Player.Male:
                    menu:
                        ch_k ". . . Но. . . но ты же все равно будешь[KittyX.like]главной в наших отношениях?"
                        "Конечно.":
                                $ KittyX.Statup("Obed", 200, 10)
                                $ KittyX.FaceChange("smile", 1)
                                ch_k "Ты такая классная, [KittyX.Petname]."
                        "От этого мне становится как-то не по себе.":
                                $ KittyX.Statup("Love", 200, -10)
                                $ KittyX.Statup("Obed", 200, -50)
                                $ KittyX.Statup("Inbt", 50, -15)
                                $ Line = "embarrassed"
                else:
                    menu:
                        ch_k ". . . Но. . . но ты же все равно будешь[KittyX.like]главным в наших отношениях?"
                        "Конечно.":
                                $ KittyX.Statup("Obed", 200, 10)
                                $ KittyX.FaceChange("smile", 1)
                                ch_k "Ты такой классный, [KittyX.Petname]."
                        "От этого мне становится как-то не по себе.":
                                $ KittyX.Statup("Love", 200, -10)
                                $ KittyX.Statup("Obed", 200, -50)
                                $ KittyX.Statup("Inbt", 50, -15)
                                $ Line = "embarrassed"

#Kitty_Sub_Bad_End:
    $ KittyX.History.append("sir")
    if not Line:
            $ KittyX.Blush = 1
            $ KittyX.Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif Line == "rude":
            hide Kitty_Sprite with easeoutbottom
            call Remove_Girl(KittyX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[KittyX.Name] в гневе проваливается сквозь пол, оставляя вас в одиночестве."
    elif Line == "embarrassed":
            $ KittyX.FaceChange("sadside", 2)
            ch_k "О! Эм, да! [KittyX.Like]то есть. . ."
            $ KittyX.Mouth = "smile"
            ch_k "Я просто пошутила. Я. . . да.  Это слишком[KittyX.like]странно."
            ch_k "Мне надо идти. Кажется, я слышу, как профессор Ксавье зовет меня."
            $ KittyX.Blush = 1
            hide Kitty_Sprite with easeoutbottom
            call Remove_Girl(KittyX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[KittyX.Name] проваливается сквозь пол, оставляя вас в одиночестве."
    return

label Kitty_Sub_Asked:
    $ Line = 0
    call Shift_Focus(KittyX)
    $ KittyX.FaceChange("sadside", 1)
    if not Player.Male:
        ch_k "Ага, а также я[KittyX.like]помню, что из-за этого ты вела себя как {i}ничтожество{i}."
    else:
        ch_k "Ага, а также я[KittyX.like]помню, что из-за этого ты вел себя как {i}мудак{i}."
    menu:
        extend ""
        "Ну, я хочу извиниться. Надеюсь, ты дашь мне второй шанс.":
                if "sir" in KittyX.Petnames and ApprovalCheck(KittyX, 850, "O"):
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck(KittyX, 550, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        pass
                else: #if it failed both those things,
                        "Ну, возможно, {i}я{/i} над этим[KittyX.like]подумаю." #Failed again. :(
                        $ Line = "rude"

                if Line != "rude":
                        $ KittyX.Statup("Love", 90, 10)
                        $ KittyX.FaceChange("sly", 1)
                        if not Player.Male:
                            ch_k "Ну. . . Ладно. Думаю, меня это заводит. Кроме того, ты такая милая, когда извиняешься."
                        else:
                            ch_k "Ну. . . Ладно. Думаю, меня это заводит. Кроме того, ты такой милый, когда извиняешься."
                        call Girl_Smooch_Launch(KittyX)
                        ch_k "Ладно. Попробуем[KittyX.like]еще раз."

        "Послушай. . . я знаю, что ты этого хочешь. Ты согласна попробовать еще раз, или нет?":
                $ KittyX.FaceChange("bemused", 1)
                if "sir" in KittyX.Petnames:
                    if ApprovalCheck(KittyX, 850, "O"):
                        ch_k "Ладно."
                    else:
                        ch_k "Эм, да мне как-то не особо хочется."
                        $ Line = "rude"
                elif ApprovalCheck(KittyX, 600, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        $ KittyX.FaceChange("sadside", 1)
                        if not Player.Male:
                            ch_k "Ты[KittyX.like]абсолютно невыносима."
                            $ KittyX.Eyes = "squint"
                            ch_k "Хотя, возможно, ты права."
                            ch_k "Но я все еще думаю, что тебе стоит[KittyX.like]извиниться за то, каким ничтожеством ты была."
                        else:
                            ch_k "Ты[KittyX.like]абсолютно невыносим."
                            $ KittyX.Eyes = "squint"
                            ch_k "Хотя, возможно, ты прав."
                            ch_k "Но я все еще думаю, что тебе стоит[KittyX.like]извиниться за то, каким мудаком ты был."
                        menu:
                            extend ""
                            "Хорошо, извини, что я была довольно груба." if not Player.Male:
                                            $ KittyX.Statup("Love", 90, 15)
                                            $ KittyX.Statup("Inbt", 50, 10)
                                            $ KittyX.FaceChange("bemused", 1)
                                            $ KittyX.Eyes = "side"
                                            ch_k "Вот видишь, ничего сложного."
                            "Хорошо, извини, что я был довольно груб." if Player.Male:
                                            $ KittyX.Statup("Love", 90, 15)
                                            $ KittyX.Statup("Inbt", 50, 10)
                                            $ KittyX.FaceChange("bemused", 1)
                                            $ KittyX.Eyes = "side"
                                            ch_k "Вот видишь, ничего сложного."
                            "Не дождешься.":
                                    if "sir" in KittyX.Petnames and ApprovalCheck(KittyX, 900, "O"):
                                            $ KittyX.Statup("Love", 200, -5)
                                            $ KittyX.Statup("Obed", 200, 10)
                                            ch_k ". . ."
                                    elif ApprovalCheck(KittyX,650, "O"):
                                            $ KittyX.Statup("Love", 200, -5)
                                            $ KittyX.Statup("Obed", 200, 10)
                                            ch_k "Я, эм. . ."
                                    else: #if it failed both those things,
                                            $ KittyX.Statup("Love", 200, -10)
                                            $ KittyX.Statup("Obed", 90, -10)
                                            $ KittyX.Statup("Obed", 200, -10)
                                            $ KittyX.Statup("Inbt", 50, -15)
                                            "Китти вздыхает и закатывает глаза."
                                            $ KittyX.FaceChange("angry", 1)
                                            $ KittyX.Eyes = "side"
                                            if not Player.Male:
                                                ch_k "Ты так ничему и не научилась, да?"
                                            else:
                                                ch_k "Ты так ничему и не научился, да?"
                                            $ Line = "rude"
                            "Ладно, тогда не бери в голову.":
                                            $ KittyX.FaceChange("angry", 1)
                                            $ KittyX.Statup("Love", 200, -10)
                                            $ KittyX.Statup("Obed", 90, -10)
                                            $ KittyX.Statup("Obed", 200, -10)
                                            $ KittyX.Statup("Inbt", 50, -15)
                                            if not Player.Male:
                                                ch_k "Ты не изменилась."
                                            else:
                                                ch_k "Ты не изменился."
                                            ch_k "Я должна была[KittyX.like]догадаться, что так оно и будет."
                                            $ Line = "rude"

    $ KittyX.RecentActions.append("asked sub")
    $ KittyX.DailyActions.append("asked sub")
    if Line == "rude":
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Kitty_Sprite with easeoutbottom
            call Remove_Girl(KittyX)
            $ KittyX.RecentActions.append("angry")
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[KittyX.Name] проваливается сквозь пол, оставляя вас в одиночестве. Она выглядела очень расстроенной."
    elif "sir" in KittyX.Petnames:
            #it didn't fail and "sir" was covered
            $ KittyX.Statup("Obed", 200, 50)
            $ KittyX.Petnames.append("master")
            if not Player.Male:
                $ KittyX.Petname = "хозяйка"
                $ KittyX.Petname_rod = "хозяйки"
                $ KittyX.Petname_dat = "хозяйке"
                $ KittyX.Petname_vin = "хозяйку"
                $ KittyX.Petname_tvo = "хозяйкой"
                $ KittyX.Petname_pre = "хозяйке"
            else:
                $ KittyX.Petname = "хозяин"
                $ KittyX.Petname_rod = "хозяина"
                $ KittyX.Petname_dat = "хозяину"
                $ KittyX.Petname_vin = "хозяина"
                $ KittyX.Petname_tvo = "хозяином"
                $ KittyX.Petname_pre = "хозяине"
            $ KittyX.Eyes = "sly"
            if not Player.Male:
                ch_k ". . .хозяйка. . ."
            else:
                ch_k ". . .хозяин. . ."
    else:
            #it didn't fail
            $ KittyX.Statup("Obed", 200, 30)
            $ KittyX.Petnames.append("sir")
            if not Player.Male:
                $ KittyX.Petname = "госпожа"
                $ KittyX.Petname_rod = "госпожи"
                $ KittyX.Petname_dat = "госпоже"
                $ KittyX.Petname_vin = "госпожу"
                $ KittyX.Petname_tvo = "госпожой"
                $ KittyX.Petname_pre = "госпоже"
            else:
                $ KittyX.Petname = "господин"
                $ KittyX.Petname_rod = "господина"
                $ KittyX.Petname_dat = "господину"
                $ KittyX.Petname_vin = "господина"
                $ KittyX.Petname_tvo = "господином"
                $ KittyX.Petname_pre = "господине"
            $ KittyX.Eyes = "sly"
            if not Player.Male:
                ch_k ". . . госпожа."
            else:
                ch_k ". . . господин."
    return

# end Kitty_Sub//////////////////////////////////////////////////////////


# start Kitty_Master//////////////////////////////////////////////////////////

label Kitty_Master:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(KittyX,"bemused","выглядит необычайно покорной. . .")
            return
    call Shift_Focus(KittyX)
    $ KittyX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    if KittyX.Loc != bg_current and KittyX not in Party:
        "Внезапно [KittyX.Name] появляется перед вами с явным желанием поговорить."

    $ Event_Queue = [0,0]
    $ KittyX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(KittyX)
    call CleartheRoom(KittyX)
    $ KittyX.DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ KittyX.FaceChange("bemused", 1)
    ch_k "[KittyX.Petname], если ты не против. . ."
    ch_k "Я бы хотела сказать, что твой[KittyX.like]контроль наших отношений, дал очень даже неплохой результат."
    menu:
        extend ""
        "Мне тоже все нравится.":
                $ KittyX.FaceChange("sly", 1)
                ch_k "Круто. Может мы[KittyX.like]могли бы перейти на следующий этап?"
                menu:
                    extend ""
                    "Нет. Все и так идеально.":
                            $ KittyX.FaceChange("sad", 1)
                            $ KittyX.Statup("Obed", 200, -15)
                            $ KittyX.Statup("Inbt", 50, 10)
                            ch_k "Ох. Ну ладно. Может и так."
                            $ Line = "fail"
                    "Что ты имеешь в виду?":
                            $ KittyX.Eyes = "side"
                            if not Player.Male:
                                ch_k "Ну я не знаю. Я подумала, что я[KittyX.like]могла бы начать звать тебя. . . {i}хозяйкой{/i}?"
                            else:
                                ch_k "Ну я не знаю. Я подумала, что я[KittyX.like]могла бы начать звать тебя. . . {i}хозяином{/i}?"
                            $ KittyX.Eyes = "squint"
                            ch_k "Что думаешь? Мне кажется, звучит довольно[KittyX.like]сексуально."
                            menu:
                                extend ""
                                "О да. Мне нравится.":
                                        ch_k "Круто. . ."
                                "Эм. . .нет.  Это слишком.":
                                        $ KittyX.FaceChange("sad", 1)
                                        $ KittyX.Statup("Obed", 200, -15)
                                        $ KittyX.Statup("Inbt", 50, 5)
                                        ch_k "Oх. Ну ладно, может и так."
                                        $ Line = "fail"

                    "Честно говоря, я бы предпочла перестать держать все под контролем." if not Player.Male:
                            $ KittyX.FaceChange("sly", 1)
                            $ KittyX.Statup("Love", 200, 15)
                            $ KittyX.Statup("Obed", 200, -10)
                            $ KittyX.Statup("Inbt", 50, 10)
                            ch_k "Ах, думаю, я не стану из-за этого на тебя злиться. . ."
                            $ Line = "fail"

                    "Честно говоря, я бы предпочел перестать держать все под контролем." if Player.Male:
                            $ KittyX.FaceChange("sly", 1)
                            $ KittyX.Statup("Love", 200, 15)
                            $ KittyX.Statup("Obed", 200, -10)
                            $ KittyX.Statup("Inbt", 50, 10)
                            ch_k "Ах, думаю, я не стану из-за этого на тебя злиться. . ."
                            $ Line = "fail"

                    "Знаешь, давай все прекратим. Меня это начинает пугать.":
                            $ KittyX.FaceChange("perplexed", 2)
                            $ KittyX.Statup("Love", 200, -10)
                            $ KittyX.Statup("Obed", 200, -50)
                            $ KittyX.Statup("Inbt", 50, -15)
                            ch_k "Ох. Извини. Наверное, меня правда[KittyX.like]понесло немного не туда."
                            $ KittyX.Blush = 1
                            $ Line = "embarrassed"

        "Как будто меня волнует твое мнение, шлюха.":
                $ KittyX.FaceChange("sad", 1)
                $ KittyX.Statup("Love", 200, -20)
                $ KittyX.Statup("Obed", 200, 10)
                $ KittyX.Statup("Inbt", 50, -10)
                menu:
                    ch_k "Что?"
                    "Извиняюсь. Мне просто все равно, чего ты хочешь.":
                            if ApprovalCheck(KittyX, 1400, "LO"):
                                    $ KittyX.Statup("Obed", 200, 10)
                                    ch_k "Это было так. . ."
                                    $ KittyX.FaceChange("sly", 1)
                                    $ KittyX.Statup("Love", 200, 20)
                                    $ KittyX.Statup("Inbt", 50, 15)
                                    ch_k ". . .{i}грубо!{/i}"
                            else:
                                    $ KittyX.Statup("Love", 200, -15)
                                    $ KittyX.Statup("Obed", 200, -10)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    $ KittyX.FaceChange("angry", 1)
                                    ch_k "!!!"
                                    $ Line = "rude"

                    "Извини. Я просто пытаюсь быть более -властной-. Я думала, тебе понравится. Это перебор?" if not Player.Male:
                                    $ KittyX.Statup("Love", 200, 10)
                                    $ KittyX.Statup("Obed", 200, 10)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    ch_k "O, ну ладно.  Просто. . . в следующий раз попытайся[KittyX.like]быть чуточку помягче, ладно?"

                    "Извини. Я просто пытаюсь быть более -властным-. Я думал, тебе понравится. Это перебор?" if Player.Male:
                                    $ KittyX.Statup("Love", 200, 10)
                                    $ KittyX.Statup("Obed", 200, 10)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    ch_k "O, ну ладно.  Просто. . . в следующий раз попытайся[KittyX.like]быть чуточку помягче, ладно?"

        "Я так не считаю. Такие отношения до жути странные.":
                                    $ KittyX.FaceChange("sad", 2)
                                    $ KittyX.Statup("Love", 200, -10)
                                    $ KittyX.Statup("Obed", 200, -20)
                                    $ KittyX.Statup("Inbt", 50, -25)
                                    ch_k "Oх. Эмм. . . тогда забудь."
                                    $ Line = "embarrassed"

    $ KittyX.History.append("master")
    if Line == "rude":
            $ KittyX.RecentActions.append("angry")
            hide Kitty_Sprite with easeoutbottom
            call Remove_Girl(KittyX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[KittyX.Name] в гневе проваливается сквозь пол. Кажется, она плакала."
    elif Line == "embarrassed":
            hide Kitty_Sprite with easeoutbottom
            call Remove_Girl(KittyX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[KittyX.Name] проваливается сквозь пол, пыхтя от злости. Вы остаетесь в одиночестве."
    elif Line != "fail":
            $ KittyX.Statup("Obed", 200, 50)
            $ KittyX.Petnames.append("master")
            if not Player.Male:
                $ KittyX.Petname = "хозяйка"
                $ KittyX.Petname_rod = "хозяйки"
                $ KittyX.Petname_dat = "хозяйке"
                $ KittyX.Petname_vin = "хозяйку"
                $ KittyX.Petname_tvo = "хозяйкой"
                $ KittyX.Petname_pre = "хозяйке"
            else:
                $ KittyX.Petname = "хозяин"
                $ KittyX.Petname_rod = "хозяина"
                $ KittyX.Petname_dat = "хозяину"
                $ KittyX.Petname_vin = "хозяина"
                $ KittyX.Petname_tvo = "хозяином"
                $ KittyX.Petname_pre = "хозяине"
            if not Player.Male:
                ch_k ". . .хозяйка."
            else:
                ch_k ". . .хозяин."
    return

# end Kitty_Master//////////////////////////////////////////////////////////


# start Kitty_Sexfriend//////////////////////////////////////////////////////////

label Kitty_Sexfriend:
    if KittyX.Loc != bg_current:
            "[KittyX.Name] появляется, словно из ниоткуда."
    $ KittyX.Loc = bg_current
    $ Event_Queue = [0,0]
    call Set_The_Scene(0)
    call Shift_Focus(KittyX)
    call Display_Girl(KittyX)
    call CleartheRoom(KittyX)
    $ KittyX.DailyActions.append("relationship")
    if not Player.Male and "girltalk" not in KittyX.History:
            call expression KittyX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
            return
    call Taboo_Level
    $ Line = 0
    $ KittyX.FaceChange("bemused", 1)
    ch_k "Слушай, [KittyX.Petname]. . . у тебя[KittyX.like]есть минутка?" #blushing expression
    menu:
            extend ""
            "Я спешу.":
                $ KittyX.FaceChange("angry", 1)
                if not Player.Male:
                    ch_k "Ну ты и сучка, [Player.Name]!" #Angry expression.  Loss of points
                else:
                    ch_k "Ну ты и говнюк, [Player.Name]!" #Angry expression.  Loss of points
                $ KittyX.Statup("Love", 200, -20)
                $ KittyX.Statup("Obed", 50, 3)
                $ Line = "rude"

            "Мне уже не нравится этот разговор.":
                $ KittyX.FaceChange("perplexed", 1)
                ch_k "Обещаю. Ничего[KittyX.like]плохого я не скажу."

            "Да. Что случилось?":
                pass

    if not Line: #all this gets skipped if the "rude" response was procced above
            if ApprovalCheck(KittyX, 850, "L"):
                    $ KittyX.FaceChange("bemused", 1)
                    ch_k "Ну. . . Ты мне очень нравишься. Ты же это знаешь, да?" #Sexy expression.  This is Kitty's "High Like" response
                    menu:
                        extend ""
                        "Я на это надеялась." if not Player.Male:
                            $ KittyX.FaceChange("sexy", 1)
                            $ KittyX.Statup("Love", 90, 10)
                            $ KittyX.Statup("Inbt", 80, 5)
                            ch_k "Я {i}очень{/i} рада, что ты это сказала, [KittyX.Petname]." #Blushing expression

                        "Я на это надеялся." if Player.Male:
                            $ KittyX.FaceChange("sexy", 1)
                            $ KittyX.Statup("Love", 90, 10)
                            $ KittyX.Statup("Inbt", 80, 5)
                            ch_k "Я {i}очень{/i} рада, что ты это сказал, [KittyX.Petname]." #Blushing expression

                        "Правда?":
                            ch_k "Эмм[KittyX.Like]ну да." #Blushing expression

                        "О боже.":
                            $ KittyX.FaceChange("angry", 1)
                            $ KittyX.Statup("Love", 200, -10)
                            $ KittyX.Statup("Obed", 50, 5)
                            $ KittyX.Statup("Inbt", 80, -5)
                            if not Player.Male:
                                ch_k "Какой же ты овца, [Player.Name]!" #Angry expression.  Big loss of points
                            else:
                                ch_k "Какой же ты козел, [Player.Name]!" #Angry expression.  Big loss of points
                            $ Line = "rude"

            elif ApprovalCheck(KittyX, 1000, "LI"):
                    $ KittyX.FaceChange("sexy", 1)
                    if not Player.Male:
                        ch_k "Я просто хотела сказать. . . Я думаю, что ты[KittyX.like]довольно милая."
                    else:
                        ch_k "Я просто хотела сказать. . . Я думаю, что ты[KittyX.like]довольно милый."
                    menu:
                        extend ""
                        "Мне очень приятно.":
                            $ KittyX.Statup("Love", 80, 5)
                            $ KittyX.Statup("Inbt", 80, 5)
                            ch_k "Ну, я сказала от чистого сердца." #Blushing expression

                        "Я? Ты правда так думаешь?":
                            ch_k "Ага. Я {i}правда{/i} так считаю."

                        "Ты к чему то клонишь?":
                            $ KittyX.FaceChange("angry")
                            ch_k "Уже ни к чему!" #Angry expression.  Loss of points
                            $ Line = "rude"

            else: #if it reaches this block, it's because it failed the "like" check above.
                    $ KittyX.Mouth = "smile"
                    $ KittyX.Brows = "sad"
                    $ KittyX.Eyes = "side"
                    ch_k "Это может прозвучать[KittyX.like]очень странно."
                    menu:
                        extend ""
                        "Что ж, ты меня заинтриговала. Теперь ты просто обязана мне все рассказать.":
                            ch_k "Можешь пообещать, что не подумаешь обо мне[KittyX.like]{i}плохо{/i}?"  #Nervous expression
                            menu:
                                extend ""
                                "[KittyX.Name]. . . Ты мне очень нравишься. Обещаю.":
                                    $ KittyX.FaceChange("smile")
                                    $ KittyX.Statup("Love", 80, 10)
                                    $ KittyX.Statup("Inbt", 80, 5)
                                    ch_k "Нуууу. . . ладно."  #Blushing expression.  Gain of points.

                                "Эм. . . ладно?":
                                    ch_k "Нууу. .  ." #Nervous expression

                                "Ничего не обещаю.":
                                    $ KittyX.FaceChange("perplexed",2)
                                    $ KittyX.Statup("Inbt", 80, -5)
                                    ch_k "Эммм. . . тогда забудь."  #Embarrassed expression.  Minor loss of points
                                    $ Line = "embarrassed"

                        "Эм, думаю, я сыта по горло всякими {i}странностями{/i}, спасибо" if not Player.Male:
                            $ KittyX.FaceChange("angry",1)
                            ch_k "Ну и ладно. Тогда[KittyX.Like]забудь."
                            $ Line = "rude"

                        "Эм, думаю, я сыт по горло всякими {i}странностями{/i}, спасибо" if Player.Male:
                            $ KittyX.FaceChange("angry",1)
                            ch_k "Ну и ладно. Тогда[KittyX.Like]забудь."
                            $ Line = "rude"
    if KittyX in Player.Harem:
            $ Line = "harem"
    if not Line: #again, if the Line has been changed to "rude" or "embarrassed" then it skips past here.
            ch_k "В общем. . . Я тут[KittyX.like]подумала. . . мы ведь неплохо ладим, ведь так?"
            menu:
                extend ""
                "Ага. . . ":
                        pass
                "Все, перестать. Ты меня пугаешь.":
                        $ KittyX.FaceChange("perplexed",2)
                        $ KittyX.Statup("Love", 200, -10)
                        $ KittyX.Statup("Inbt", 80, -10)
                        ch_k "Извини. Я знала, что это было ошибкой." #Embarrassed expression.  Minor loss of points
                        $ Line = "embarrassed"

    if not Line:
            ch_k "И мы[KittyX.like]уже знакомы достаточно долго, верно?"
            menu:
                extend ""
                "Ага. . . ":
                        pass
                "Все, перестать. Ты меня пугаешь.":
                        $ KittyX.FaceChange("perplexed",2)
                        $ KittyX.Statup("Love", 200, -10)
                        $ KittyX.Statup("Inbt", 80, -10)
                        ch_k "Извини. Я знала, что это было ошибкой."
                        $ Line = "embarrassed"
    if not Line:
            ch_k "Так вот. . . "
            ch_k "Мы[KittyX.like]могли бы перейти на следующий уровень наших отношений, если хочешь."
            menu:
                extend ""
                "Ты намекаешь на. . . {i}секс без обязательств{/i}?":
                        ch_k "Нууу. . . да. Что скажешь?" #Blushing expression
                        menu:
                            extend ""
                            "Звучит потрясающе! Я за.":
                                    $ KittyX.FaceChange("smile",1)
                                    $ KittyX.Statup("Love", 80, 10)
                                    $ KittyX.Statup("Obed", 50, 10)
                                    $ KittyX.Statup("Inbt", 200, 50)
                                    $ KittyX.Statup("Lust", 200, 5)
                                    "Китти наклоняется и нежно целует вас в щечку."
                                    ch_k "Жду не дождусь, когда мы начнем, [KittyX.Petname]."

                            "Только шлюха могла предложить такое.":
                                    $ KittyX.FaceChange("angry",1)
                                    $ KittyX.Statup("Love", 200, -30)
                                    $ KittyX.Statup("Obed", 50, 10)
                                    $ KittyX.Statup("Inbt", 80, -40)
                                    if not Player.Male:
                                        ch_k "Какая же ты[KittyX.like]манда, [KittyX.Petname]!" #Angry expression.  HUGE loss of points
                                    else:
                                        ch_k "Какой же ты[KittyX.like]гондон, [KittyX.Petname]!" #Angry expression.  HUGE loss of points
                                    $ Line = "rude"

                "Если честно, мне бы этого не хотелось.":
                        $ KittyX.FaceChange("sadside",2)
                        $ KittyX.Statup("Obed", 50, 15)
                        $ KittyX.Statup("Inbt", 80, -15)
                        ch_k "Oх. Ну ладно."  #Sad expression
                        ch_k "Я[KittyX.like]думаю, что тебе стоит уйти. У меня еще[KittyX.like]остались кое-какие дела."
                        $ Line = "sad"
    if Line == "harem":
            if Player.Male:
                    ch_k "Я -полностью- зависима от твоего члена. . ."
            else:
                    ch_k "Я -полностью- зависима от твоей киски. . ."
            $ Line = 0
    if Line == "rude":
            $ KittyX.FaceChange("angry",1)
            $ KittyX.RecentActions.append("angry")
            $ KittyX.Statup("Love", 200, -20)
            $ KittyX.Statup("Obed", 50, 5)
            $ KittyX.Statup("Inbt", 80, -10)
            hide Kitty_Sprite with easeoutleft
            $ KittyX.RecentActions.append("angry")
            "[KittyX.Name] в бешенстве уходит. Она, судя по всему, очень зла на вас."
    elif Line == "embarrassed":
            $ KittyX.FaceChange("perplexed",1)
            $ KittyX.Statup("Love", 200, -10)
            $ KittyX.Statup("Obed", 50, 5)
            $ KittyX.Statup("Inbt", 80, -20)
            hide Kitty_Sprite with easeoutbottom
            "[KittyX.Name] проваливается сквозь пол, оставляя вас в одиночестве. Это было очень странно."
    elif Line == "sad":
            hide Kitty_Sprite with easeoutbottom
            "[KittyX.Name] проваливается сквозь пол, оставляя вас в одиночестве. Кажется, вы задели ее чувства."
    else: #if you kept Line unused throughout, then you passed all the checks, so. . .
            $ KittyX.Petnames.append("sex friend")
            $ KittyX.FaceChange("sly",2)
            $ KittyX.Statup("Inbt", 80, 10)
            $ KittyX.Statup("Lust", 80, 10)
            "[KittyX.Name] наклоняется и проводит рукой по вашему телу."
            "В этот момент ее рука проходит сквозь ваши джинсы, давая ей возможность прикоснуться к вам напрямую."
            $ KittyX.Blush = 1
            ch_k "Позже обязательно увидимся, [KittyX.Petname]."
            hide Kitty_Sprite with easeoutright
            "После этого она уходит сквозь ближайшую стену. "
    call Remove_Girl(KittyX)
    return

# end Kitty_Sexfriend//////////////////////////////////////////////////////////


# start Kitty_Fuckbuddy//////////////////////////////////////////////////////////

#Not updated

label Kitty_Fuckbuddy:
    $ KittyX.DailyActions.append("relationship")
    $ KittyX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    $ Event_Queue = [0,0]
    if Player.Male:
            "Неожиданно вы чувствуете, как чья-то рука начинает ласкать ваш член."
    else:
            "Неожиданно вы чувствуете, как чья-то рука начинает ласкать вашу киску."
    "Даже учитывая то, что вы полностью одеты, чувства не обманешь, кто-то с очень мягкой кожей прикасается к вам."
    "Вы оглядываетесь и видите тонкую руку, выходящую откуда-то из-за вашей спины и исчезающую в штанах."
    if Player.Male:
            "Пока вы пытаетесь контролировать нарастающую эрекцию, вы слышите шепот вам на ушко,"
    else:
            "Пока вы пытаетесь контролировать нарастающее возбуждение, вы слышите шепот вам на ушко,"
    ch_k "В любое время, только попроси. . ."
    "-и так же неожиданно все прекращается."
    "Вы оглядываетесь по сторонам, но не замечаете никого рядом с собой, и, судя по всему, никто больше ничего не заметил."
    "Наверное, потом вам стоит навестить [KittyX.Name_vin]. . ."
    $ KittyX.Petnames.append("fuck buddy")
    $ KittyX.Event[10] += 1
    return
# end Kitty_Fuckbuddy//////////////////////////////////////////////////////////

# start Kitty_Daddy//////////////////////////////////////////////////////////

#Not updated

label Kitty_Daddy:
    $ KittyX.DailyActions.append("relationship")
    $ KittyX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    $ Event_Queue = [0,0]
    if KittyX.Loc != bg_current:
            $ KittyX.Loc = bg_current
            "[KittyX.Name] подходит к вам."
    call Shift_Focus(KittyX)
    call Set_The_Scene
    ch_k ". . ."
    if KittyX in Player.Harem:
        ch_k "Привет, учитывая[KittyX.like]что мы встречаемся,"
    else:
        ch_k "Привет, учитывая[KittyX.like]как часто мы проводим время вместе,"
    if KittyX.Love > KittyX.Obed and KittyX.Love > KittyX.Inbt:
        if not Player.Male:
            ch_k "и то, что ты очень мила со мной. . ."
        else:
            ch_k "и то, что ты очень мил со мной. . ."
    elif KittyX.Obed > KittyX.Inbt:
        ch_k "и то, что ты знаешь, что мне нужно. . ."
    else:
        ch_k "и то, что с тобой я испытала много нового. . ."
    if not Player.Male:
        ch_k "Я[KittyX.like]решила, что хочу звать тебя. . . \"мамочкой?\""
    else:
        ch_k "Я[KittyX.like]решила, что хочу звать тебя. . . \"папочкой?\""
    menu:
        extend ""
        "Ладно, давай.":
                $ KittyX.FaceChange("smile")
                $ KittyX.Statup("Love", 90, 25)
                $ KittyX.Statup("Obed", 60, 10)
                $ KittyX.Statup("Inbt", 80, 30)
                ch_k "Отлично!"
        "Зачем тебе это?":
            $ KittyX.FaceChange("bemused")
            ch_k "Знаешь, я просто дико возбуждаюсь, когда представляю себя твоей дочерью. . ."
            ch_k "Позволишь мне так к тебе обращаться?"
            menu:
                extend ""
                "Звучит интересно, мне нравится.":
                        $ KittyX.FaceChange("smile")
                        $ KittyX.Statup("Love", 90, 17)
                        $ KittyX.Statup("Obed", 60, 20)
                        $ KittyX.Statup("Inbt", 80, 25)
                        if not Player.Male:
                            ch_k "Замечательно! . . папочка."
                        else:
                            ch_k "Замечательно! . . папочка."
                        if not Player.Male:
                            $ KittyX.Petname = "мамочка"
                            $ KittyX.Petname_rod = "мамочки"
                            $ KittyX.Petname_dat = "мамочке"
                            $ KittyX.Petname_vin = "мамочку"
                            $ KittyX.Petname_tvo = "мамочкой"
                            $ KittyX.Petname_pre = "мамочке"
                        else:
                            $ KittyX.Petname = "папочка"
                            $ KittyX.Petname_rod = "папочки"
                            $ KittyX.Petname_dat = "папочке"
                            $ KittyX.Petname_vin = "папочку"
                            $ KittyX.Petname_tvo = "папочкой"
                            $ KittyX.Petname_pre = "папочке"
                "Прошу, не надо.":
                        $ KittyX.Statup("Obed", 80, 40)
                        $ KittyX.Statup("Inbt", 80, 20)
                        $ KittyX.FaceChange("sad")
                        ch_k "   . . .   "
                        ch_k "Пфф. Ладно."
                "Нет, меня пугает такое.":
                        $ KittyX.Statup("Love", 90, -15)
                        $ KittyX.Statup("Obed", 80, 45)
                        $ KittyX.Statup("Inbt", 70, 5)
                        $ KittyX.FaceChange("angry")
                        ch_k "Бууу."
        "Нет, меня пугает такое.":
                        $ KittyX.Statup("Love", 90, -10)
                        $ KittyX.Statup("Obed", 80, 40)
                        $ KittyX.Statup("Inbt", 70, 10)
                        $ KittyX.FaceChange("angry")
                        ch_k "Пфффф."
    $ KittyX.Petnames.append("daddy")
    return

# end Kitty_Daddy//////////////////////////////////////////////////////////



label Kitty_Yoink(Girl=0,BO=[],TempBonus=0,Shy=0):  #rkeljsvgb
    #this is for if Kitty is asked to steal clothing from another girl in the scene.
    # Girl is the target, most of the variables are her starting outfit
    # Temp Bonus is 0 if Kitty thinks she'd be ok with it, high if Kitty hates her, low if Kitty doesn't hate her
    # Shy is the Taboo modifier, how embarssaing the trick will be.
    # it can be 2.5 for nudity, 2 for underwear, 1 for no exposure

    if "yoink" in KittyX.DailyActions:
            ch_k "Мы уже достаточно повеселились."
            return
    $ Options = []
    $ BO = ActiveGirls[:]
    python:
        for BX in BO:
            if BX.Loc == bg_current or BX.Loc == "nearby":
                    Options.append(BX)
            elif BX.Loc == "bg teacher" and bg_current == "bg classroom":
                    Options.append(BX)

#    if RogueX.Loc == bg_current:
#            $ Girl = RogueX

#    if (EmmaX.Loc == "bg teacher" or StormX.Loc == "bg teacher") and bg_current == "bg classroom":
            #if Emma is teaching. . .
    if Options:
            #if girls have been picked above. . .
            menu:
                "Кого выберете?"
#                "[Girl.Name]?" if Girl:
#                        pass
                "[RogueX.Name_vin]?" if RogueX in Options:
                        $ Girl = RogueX
#                "[KittyX.Name]?" if KittyX in Options:
#                        $ Girl = KittyX
                "[EmmaX.Name_vin]?" if EmmaX in Options:
                        $ Girl = EmmaX
                "[LauraX.Name_vin]?" if LauraX in Options:
                        $ Girl = LauraX
                "[JeanX.Name_vin]?" if JeanX in Options:
                        $ Girl = JeanX
                "[StormX.Name_vin]?" if StormX in Options:
                        $ Girl = StormX
                "[JubesX.Name_vin]?" if JubesX in Options:
                        $ Girl = JubesX
                "[GwenX.Name]_vin?" if GwenX in Options:
                        $ Girl = GwenX
                "[BetsyX.Name_vin]?" if BetsyX in Options:
                        $ Girl = BetsyX
                "[DoreenX.Name_vin]?" if DoreenX in Options:
                        $ Girl = DoreenX
                "[WandaX.Name_vin]?" if WandaX in Options:
                        $ Girl = WandaX
                "Никого":
                        $ Options = []
                        return
    else:
            $ Options = []
            "Я не знаю, у кого можно было бы что-нибудь спереть."
            return
    #end if Emma is teaching

    $ Options = []
    if KittyX.GirlLikeCheck(Girl) <= 200:
            $ TempBonus = 400
    elif KittyX.GirlLikeCheck(Girl) <= 400:
            $ TempBonus = 200
    elif KittyX.GirlLikeCheck(Girl) >= 800 or ApprovalCheck(Girl, 500, "I", TabM=3):
            #if she think's the girl's hot and the girl is pretty open minded. . .
            $ TempBonus = 0
    else:
            #if she's fairly average on the girl and the girl isn't uninhibited. . .
            $ TempBonus = -400

    menu:
        "Смотри, [KittyX.Name], тут [Girl.Name], почему бы тебе не стащить у нее. . ."
        ". . . [get_clothing_name(Girl.Over_key, vin)]?" if Girl.Over:
                if Girl.Chest:
                        #if she has a bra on under it
                        $ Shy = 2
                        if ApprovalCheck(KittyX, 800, TabM=2, Bonus=TempBonus):
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "over"
                        elif ApprovalCheck(KittyX, 600, TabM=2, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                else:
                        #if she has no bra on under it
                        $ Shy = 3
                        if ApprovalCheck(KittyX, 800, TabM=2.5, Bonus=(TempBonus*1.5)):
                            $ Line = "over"
                        elif ApprovalCheck(KittyX, 600, TabM=1.5, Bonus=TempBonus):
                            $ Line = "no"
                        else:
                            $ Line = "noway"

        ". . . [get_clothing_name(Girl.Chest_key, vin)]?" if Girl.Chest:
                if Girl.Over:
                        #if she has a shirt on over it
                        $ Shy = 1
                        if ApprovalCheck(KittyX, 1200, TabM=1, Bonus=TempBonus):
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "chest"
                        elif ApprovalCheck(KittyX, 600, TabM=0.5, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                else:
                        #if she has no shirt on over it
                        $ Shy = 3
                        if ApprovalCheck(KittyX, 800, TabM=2.5, Bonus=(TempBonus*1.5)):
                            $ Line = "chest"
                        elif ApprovalCheck(KittyX, 600, TabM=1.5, Bonus=TempBonus):
                            $ Line = "no"
                        else:
                            $ Line = "noway"

        ". . . [get_clothing_name(Girl.Legs_key, vin)]?" if Girl.Legs:
                if Girl.Panties or Girl.HoseNum() >= 10:
                        #if she has panties or tights on under it
                        $ Shy = 2
                        if ApprovalCheck(KittyX, 1000, TabM=2, Bonus=TempBonus):
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "legs"
                        elif ApprovalCheck(KittyX, 800, TabM=2, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                else:
                        #if she has no panties or tights on under it
                        $ Shy = 3
                        if ApprovalCheck(KittyX, 1000, TabM=2.5, Bonus=(TempBonus*1.5)):
                            $ Line = "legs"
                        elif ApprovalCheck(KittyX, 800, TabM=1.5, Bonus=TempBonus):
                            $ Line = "no"
                        else:
                            $ Line = "noway"

        ". . . [get_clothing_name(Girl.Panties_key, vin)]?" if Girl.Panties:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        #if she has legs or tights on over it
                        $ Shy = 1
                        if ApprovalCheck(KittyX, 1000, TabM=1, Bonus=TempBonus):
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "panties"
                        elif ApprovalCheck(KittyX, 800, TabM=0.5, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                else:
                        #if she has no legs or tights on over it
                        $ Shy = 3
                        if ApprovalCheck(KittyX, 1000, TabM=2.5, Bonus=(TempBonus*1.5)):
                            $ Line = "panties"
                        elif ApprovalCheck(KittyX, 800, TabM=1.5, Bonus=TempBonus):
                            $ Line = "no"
                        else:
                            $ Line = "noway"

        ". . . [get_clothing_name(Girl.Hose_key, vin)]?" if Girl.Hose:
                if Girl.Legs:
                        #if she has legs on over it
                        $ Shy = 1
                        if ApprovalCheck(KittyX, 800, TabM=1, Bonus=TempBonus):
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "hose"
                        elif ApprovalCheck(KittyX, 800, TabM=0.5, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                elif Girl.Panties or Girl.HoseNum() < 10:
                        #if she has panties on under it
                        $ Shy = 2
                        if ApprovalCheck(KittyX, 1000, TabM=2, Bonus=TempBonus):
                            #+800 check in standard taboo
                            #she's in
                            $ Line = "hose"
                        elif ApprovalCheck(KittyX, 800, TabM=2, Bonus=TempBonus):
                            #she says no, but not mad
                            $ Line = "no"
                        else:
                            #she's mad
                            $ Line = "noway"
                else:
                        #if she has no legs or panties on over it
                        $ Shy = 3
                        if ApprovalCheck(KittyX, 1000, TabM=2.5, Bonus=(TempBonus*1.5)):
                            $ Line = "hose"
                        elif ApprovalCheck(KittyX, 800, TabM=1.5, Bonus=TempBonus):
                            $ Line = "no"
                        else:
                            $ Line = "noway"

        "Неважно.":
                return

    if Line == "no":
            $ KittyX.FaceChange("sadside",1)
            $ KittyX.Statup("Love", 90, -(Shy))
            ch_k "Я не могу так с ней поступить."
            return
    if Line == "noway":
            $ KittyX.FaceChange("angry",1)
            $ KittyX.Statup("Love", 90, -(2*Shy))
            $ KittyX.Statup("Obed", 60, -(Shy))
            if not Player.Male:
                ch_k "Как ты могла даже[KittyX.like]{i}подумать{/i} о чем-то таком?"
            else:
                ch_k "Как ты мог даже[KittyX.like]{i}подумать{/i} о чем-то таком?"
            return
    #else, she agrees. . .

    $ KittyX.Statup("Obed", 70, Shy)
    $ KittyX.Statup("Inbt", 80, Shy)
    "[KittyX.Name] подкрадывается к [Girl.Name_dat] сзади. . ."

    $ Girl.FaceChange("surprised",2)
    if Line == "over":
                $ Line = get_clothing_name(Girl.Over_key, vin)
                $ Girl.Over = 0
                call Girl_First_Topless(Girl,1)
                "Она протягивает руку и снимает [Line] [Girl.Name_rod], потянув сквозь ее тело."

    elif Line == "chest":
                $ Line = get_clothing_name(Girl.Chest_key, vin)
                $ Girl.Chest = 0
                call Girl_First_Topless(Girl,1)
                if Girl.Over:
                    "Она протягивает руку и снимает [Line] [Girl.Name_rod] сквозь ее [get_clothing_name(Girl.Over_key, vin)] ."
                else:
                    "Она протягивает руку и снимает [Line] [Girl.Name_rod] одним рывком сквозь тело."

    elif Line == "legs":
                $ Line = get_clothing_name(Girl.Legs_key, vin)
                $ Girl.Legs = 0
                call Girl_First_Bottomless(Girl,1)
                "Она протягивает руку и снимает [Line] [Girl.Name_rod], потянув сквозь ее тело."

    elif Line == "panties":
                $ Line = get_clothing_name(Girl.Panties_key, vin)
                $ Girl.Panties = 0
                call Girl_First_Bottomless(Girl,1)
                if Girl.Legs:
                    "Она протягивает руку и снимает [Line] [Girl.Name_rod] сквозь ее [get_clothing_name(Girl.Legs_key, vin)]."
                elif Girl.Hose:
                    "Она протягивает руку и снимает [Line] [Girl.Name_rod] сквозь ее [get_clothing_name(Girl.Hose_key, vin)]."
                else:
                    "Она протягивает руку и снимает [Line] [Girl.Name_rod] одним рывком сквозь тело."
    elif Line == "hose":
                $ Line = get_clothing_name(Girl.Hose_key, vin)
                $ Girl.Hose = 0
                call Girl_First_Bottomless(Girl,1)
                if Girl.Legs:
                    "Она протягивает руку и снимает [Line] [Girl.Name_rod] сквозь [get_clothing_name(Girl.Legs_key, vin)]."
                else:
                    "Она протягивает руку и снимает [Line] [Girl.Name_rod] одним рывком сквозь тело."

    $ Girl.Facing = 0
    "Затем она отступает на несколько шагов назад, пряча [Line] за спиной."

    call Activity_Check(Girl,KittyX,1,0,2) #Girl=Girl,Girl2=KittyX,Silent=1,Removal=0,ClothesCheck=2)
    $ Approval = _return

    $ KittyX.DailyActions.append("yoink")
    if "yoink" not in KittyX.History:
            $ KittyX.History.append("yoink")

    if "exhibitionist" in Girl.Traits:
            $ Approval = 2
    $ Girl.DailyActions.append("yoink")

    if Shy <= 1:
            #if you remove a bra, hose, or panties without exposing anything
            if Approval >= 2:
                    #this girl's amused by this
                    $ Girl.FaceChange("sly")
                    $ Girl.Statup("Inbt", 80, Shy)
                    $ Girl.Statup("Lust", 80, 2)
                    "[Girl.Name] оглядывается назад с удивлением, но вскоре начинает улыбаться."
            elif Approval:
                    #this girl's annoyed
                    $ Girl.FaceChange("angry",1)
                    $ Girl.Statup("Love", 90, -(Shy))
                    "[Girl.Name] оглядывается назад с удивлением, но вскоре бросает на вас свирепый взгляд."
            else:
                    $ Girl.FaceChange("angry",2)
                    $ Girl.Statup("Love", 90, -(Shy))
                    "[Girl.Name] оглядывается назад с удивлением, но вскоре бросает на вас свирепый взгляд."
                    "Она с отвращением убегает."

    elif Shy <= 2:
            #if you expose bra or panties, but no nudity
            if Approval >= 2:
                    #this girl's amused by this
                    $ Girl.FaceChange("sly")
                    $ Girl.Statup("Inbt", 80, Shy)
                    $ Girl.Statup("Lust", 80, Shy)
                    "[Girl.Name] оглядывается назад с удивлением, но вскоре начинает улыбаться."
                    "Затем она начинает вести себя так, словно ничего не произошло."
            elif Approval or Girl == JeanX:
                    #this girl's annoyed
                    $ Girl.FaceChange("angry",1)
                    $ Girl.Statup("Love", 90, -(Shy))
                    $ Girl.Statup("Inbt", 80, -(Shy))
                    $ Girl.Statup("Lust", 80, Shy)
                    "[Girl.Name] оглядывается назад с удивлением, но вскоре бросает на вас свирепый взгляд."
                    if Girl != JeanX:
                            $ Girl.FaceChange("sadside",2)
                            "Вскоре она успокаивается и начинает слегка смущаться."
            else:
                    $ Girl.FaceChange("angry",2)
                    $ Girl.Statup("Love", 90, -(Shy))
                    $ Girl.Statup("Inbt", 80, -(Shy))
                    "[Girl.Name] оглядывается назад с удивлением, но вскоре бросает на вас свирепый взгляд."
                    "Она в смущении убегает."
    else:
            #if you strip part of her nude
            if Approval >= 2:
                    #this girl's amused by this
                    $ Girl.FaceChange("sly")
                    $ Girl.Statup("Love", 90, 1)
                    $ Girl.Statup("Inbt", 80, Shy)
                    $ Girl.Statup("Lust", 80, 2*Shy)
                    "[Girl.Name] оглядывается назад с удивлением, но вскоре начинает улыбаться."
                    "Она оглядывается по сторонам, чтобы оценить реакцию окружающих."
            elif Approval or Girl == JeanX:
                    #this girl's annoyed
                    $ Girl.FaceChange("angry",2)
                    $ Girl.Statup("Love", 90, -(Shy))
                    $ Girl.Statup("Inbt", 80, -(Shy))
                    "[Girl.Name] оглядывается назад с удивлением, но вскоре бросает на вас свирепый взгляд."
                    if Girl != JeanX:
                            "Она выглядит очень расстроенной, но старается не показывать вида."
            else:
                    $ Girl.FaceChange("angry",2)
                    $ Girl.Statup("Love", 90, -(Shy))
                    $ Girl.Statup("Inbt", 80, -(Shy))
                    "[Girl.Name] оглядывается назад с удивлением, но вскоре бросает на вас свирепый взгляд."
                    "Она в смущении убегает."


    #if the girl is embarassed
    if Approval:
            $ Girl.GLG(KittyX,900,(2*Shy),1)
            $ KittyX.GLG(Girl,900,(2*Shy),1)
            $ Girl.AddWord(1,"yoinked")  #sets a flag that this has happened before
    else:
            call Remove_Girl(Girl)
            $ Girl.GLG(KittyX,900,-(2*Shy),1)

    if Girl == JeanX and Approval < 2:
                "Быстро кивнув, она возвращает свою одежду обратно."
                $ Girl.DrainWord("yoinked")
                $ Girl.OutfitChange()
                "[KittyX.Name] немного этому удивляется."
    elif Girl == GwenX and Approval < 2:
                "[GwenX.Name] подбегает к вам и ее одежда сразу возвращается на нее."
                $ Girl.DrainWord("yoinked")
                $ Girl.OutfitChange()
                "[KittyX.Name] немного этому удивляется."
    elif TempBonus > 0:
            if Approval < 2:
                #she didn't like the girl, and drove her off.
                $ KittyX.FaceChange("sly")
                $ KittyX.Statup("Love", 80, 1)
                "[KittyX.Name] триумфально улыбается."
            else:
                #she didn't like the girl, but the girl was fine
                $ KittyX.FaceChange("angry",Eyes="side")
                "Похоже, [KittyX.Name] немного раздражена отношением [Girl.Name_rod]."

    elif not Approval:
                #she liked the girl well enough, but drove her off
                $ KittyX.FaceChange("sly")
                $ KittyX.Statup("Lust", 80, Shy)
                "[KittyX.Name] выглядит немного неуверенной от всего происходящего."
    else:
                #she liked the girl well enough, and the girl was fine
                $ KittyX.FaceChange("sly")
                $ KittyX.Statup("Love", 80, 1)
                $ KittyX.Statup("Lust", 80, Shy)
                "[KittyX.Name] смеется и крутит в руках [Line]."
    return


# start Kitty_Sexfriend//////////////////////////////////////////////////////////

label Kitty_Kate:
        $ KittyX.Loc = bg_current
        call Set_The_Scene(0)
        call Display_Girl(KittyX)
        call Taboo_Level
        $ Line = 0
        $ KittyX.FaceChange("bemused", 1)
        ch_k "Привет, [KittyX.Petname]. . . у тебя[KittyX.like]есть минутка?"
        menu:
                extend ""
                "Мне некогда.":
                    $ KittyX.FaceChange("angry", 1)
                    if not Player.Male:
                        ch_k "Ну ты и овца, [Player.Name]!"
                    else:
                        ch_k "Ну ты и говнюк, [Player.Name]!"
                    $ KittyX.Statup("Love", 200, -10)
                    $ KittyX.Statup("Obed", 50, 3)

                "Да, что случилось?":
                    pass
        $ KittyX.Names.append("Kate")
        ch_k "Я хотела предупредить тебя, что теперь меня зовут \"Кейт\"!"
        $ KittyX.Name = "Кейт"
        $ KittyX.Name_rod = "Кейт"
        $ KittyX.Name_dat = "Кейт"
        $ KittyX.Name_vin = "Кейт"
        $ KittyX.Name_tvo = "Кейт"
        $ KittyX.Name_pre = "Кейт"
        menu:
            extend ""
            "Нет, не зовут.":
                    $ KittyX.Statup("Love", 90, -10)
                    $ KittyX.Statup("Obed", 50, 10)
                    $ KittyX.Statup("Inbt", 80, -10)
                    $ KittyX.FaceChange("angry", 2)
                    ch_k "!!!"
                    if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "O"):
                            $ KittyX.Name = "Китти"
                            $ KittyX.Name_rod = "Китти"
                            $ KittyX.Name_dat = "Китти"
                            $ KittyX.Name_vin = "Китти"
                            $ KittyX.Name_tvo = "Китти"
                            $ KittyX.Name_pre = "Китти"
                            $ KittyX.FaceChange("sadside", 1)
                            $ KittyX.Statup("Obed", 90, 10)
                            $ KittyX.Statup("Inbt", 80, -5)
                            ch_k "Нууу. . .  ладно. . ."
                    else:
                            ch_k "Ты мне не указ!"
            "Тебе подходит это имя.":
                    $ KittyX.FaceChange("smile", 1)
                    $ KittyX.Statup("Love", 60, 5)
                    $ KittyX.Statup("Love", 90, 5)
                    $ KittyX.Statup("Inbt", 60, 5)
                    ch_k "Спасибо!"
            "Я всегда считала, что \"Китти\" очень красивое имя." if not Player.Male:
                    $ KittyX.Name = "Китти"
                    $ KittyX.Name_rod = "Китти"
                    $ KittyX.Name_dat = "Китти"
                    $ KittyX.Name_vin = "Китти"
                    $ KittyX.Name_tvo = "Китти"
                    $ KittyX.Name_pre = "Китти"
                    $ KittyX.Statup("Love", 90, 5)
                    $ KittyX.Statup("Obed", 70, 5)
                    $ KittyX.Statup("Inbt", 50, 5)
                    ch_k "Ну, если тебе и правда нравится \"Китти,\" я не буду менять имя. . ."
            "Я всегда считал, что \"Китти\" очень красивое имя." if Player.Male:
                    $ KittyX.Name = "Китти"
                    $ KittyX.Name_rod = "Китти"
                    $ KittyX.Name_dat = "Китти"
                    $ KittyX.Name_vin = "Китти"
                    $ KittyX.Name_tvo = "Китти"
                    $ KittyX.Name_pre = "Китти"
                    $ KittyX.Statup("Love", 90, 5)
                    $ KittyX.Statup("Obed", 70, 5)
                    $ KittyX.Statup("Inbt", 50, 5)
                    ch_k "Ну, если тебе и правда нравится \"Китти,\" я не буду менять имя. . ."
            "Почему?":
                    $ KittyX.Names.append("Katherine")
                    ch_k "Ну, мое полное имя \"Кэтрин Прайд\", я подумала, что \"Кейт\" звучит более по-взрослому."
                    menu:
                        extend ""
                        "Ну ладно, понимаю.":
                                $ KittyX.FaceChange("smile", 1)
                                $ KittyX.Statup("Love", 60, 5)
                                $ KittyX.Statup("Love", 90, 5)
                                $ KittyX.Statup("Inbt", 60, 5)
                                ch_k ". . ."
                        "Нет, скорее звучит по-глупому.":
                                $ KittyX.Statup("Love", 90, -10)
                                $ KittyX.Statup("Obed", 50, 10)
                                $ KittyX.Statup("Inbt", 80, -10)
                                $ KittyX.FaceChange("angry", 2)
                                ch_k "!!!"
                                if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "O"):
                                        $ KittyX.Name = "Китти"
                                        $ KittyX.Name_rod = "Китти"
                                        $ KittyX.Name_dat = "Китти"
                                        $ KittyX.Name_vin = "Китти"
                                        $ KittyX.Name_tvo = "Китти"
                                        $ KittyX.Name_pre = "Китти"
                                        $ KittyX.FaceChange("sadside", 1)
                                        $ KittyX.Statup("Obed", 90, 10)
                                        $ KittyX.Statup("Inbt", 80, -5)
                                        ch_k "Нууу. . .  ладно. . ."
                                else:
                                        ch_k "Ты слова для меня ничего не значат!"
                        "Может и так, но \"Китти\" очень красивое имя.":
                                $ KittyX.Statup("Love", 90, 5)
                                $ KittyX.Statup("Inbt", 50, 5)
                                if ApprovalCheck(KittyX, 800, "LO"):
                                        $ KittyX.Name = "Китти"
                                        $ KittyX.Name_rod = "Китти"
                                        $ KittyX.Name_dat = "Китти"
                                        $ KittyX.Name_vin = "Китти"
                                        $ KittyX.Name_tvo = "Китти"
                                        $ KittyX.Name_pre = "Китти"
                                        $ KittyX.Statup("Obed", 70, 5)
                                        ch_k "Ну, если тебе так больше нравится. . ."
                                else:
                                        ch_k "Что ж. . . Жаль, что ты считаешь по-другому."
                        "Почему тогда не \"Кэтрин\"?":
                                $ KittyX.Statup("Obed", 70, 5)
                                if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "0"):
                                        $ KittyX.Name = "Кэтрин"
                                        $ KittyX.Name_rod = "Кэтрин"
                                        $ KittyX.Name_dat = "Кэтрин"
                                        $ KittyX.Name_vin = "Кэтрин"
                                        $ KittyX.Name_tvo = "Кэтрин"
                                        $ KittyX.Name_pre = "Кэтрин"
                                        $ KittyX.Statup("Obed", 90, 5)
                                        ch_k "Пожалуй, звучит и правда неплохо. . ."
                                else:
                                        ch_k "Мне это имя не особо нравится. . ."
                                        menu:
                                            extend ""
                                            "Ладно, \"Кейт\" так \"Кейт\".":
                                                    $ KittyX.Name = "Кейт"
                                                    $ KittyX.Name_rod = "Кейт"
                                                    $ KittyX.Name_dat = "Кейт"
                                                    $ KittyX.Name_vin = "Кейт"
                                                    $ KittyX.Name_tvo = "Кейт"
                                                    $ KittyX.Name_pre = "Кейт"
                                                    $ KittyX.FaceChange("smile", 1)
                                                    $ KittyX.Statup("Love", 60, 5)
                                                    $ KittyX.Statup("Love", 90, 5)
                                                    $ KittyX.Statup("Inbt", 60, 5)
                                                    ch_k ". . ."
                                            "Ладно, тогда вернемся к \"Китти?\"":
                                                    $ KittyX.Statup("Love", 90, 5)
                                                    $ KittyX.Statup("Inbt", 50, 5)
                                                    if ApprovalCheck(KittyX, 800, "LO"):
                                                            $ KittyX.Name = "Китти"
                                                            $ KittyX.Name_rod = "Китти"
                                                            $ KittyX.Name_dat = "Китти"
                                                            $ KittyX.Name_vin = "Китти"
                                                            $ KittyX.Name_tvo = "Китти"
                                                            $ KittyX.Name_pre = "Китти"
                                                            $ KittyX.Statup("Obed", 70, 5)
                                                            ch_k "Ну, если тебе так больше нравится. . ."
                                                    else:
                                                            ch_k "Пожалуй, откажусь. Жаль, что тебе не понравился мой выбор."
                                #end "why not Katherine"
                    #end "why?"
        #end menu
        return

# end Kate//////////////////////////////////////////////////////////

# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Kitty_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        if "switched" in KittyX.History:
                jump Kitty_Switch2
        $ KittyX.FaceChange("smile", 1)
        ch_k "Привет?"
        ch_k ". . ."
        ch_k "Я тебя знаю?"
        menu:
            extend ""
            "Это я, [Player.XName].":
                    $ KittyX.FaceChange("confused", 1)
                    ch_k "А?"
                    $ KittyX.FaceChange("surprised", 1)
                    ch_k "О!"
                    $ KittyX.FaceChange("smile", 1)
                    ch_k "Ого, эм. . . тебя тяжело узнать. . ."
                    $ KittyX.AddWord(1,"switch") #recent

            "Нет.":
                    ch_k "Понятно."
                    ch_k "Я [KittyX.Name]!"
            "Возможно?":
                    ch_k "Хммм. . . ты выглядишь немного знакомо. . ."

        if "switch" not in KittyX.RecentActions:
                    $ KittyX.FaceChange("confused", 1)
                    ch_k ". . ."
                    ch_k "Мы -точно- никогда не встречались? . ."
                    $ KittyX.FaceChange("surprised", 1)
                    ch_k "Подожди-ка. . ."
                    ch_k "Ты [Player.XName]!"
                    $ KittyX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Ага, я [Player.XName].":
                                $ KittyX.Statup("Love", 90, 1)
                                $ KittyX.Statup("Obed", 70, 1)
                                ch_k "Ох!"
                                $ KittyX.FaceChange("smile", 1)
                                ch_k "Ого, эм. . . тебя тяжело узнать. . ."
                        "Нет.":
                                $ KittyX.FaceChange("angry", 1)
                                $ KittyX.Statup("Obed", 60, 1)
                                $ KittyX.Statup("Obed", 70, 1)
                                ch_k "[Player.XName], это ты!"
                        "Возможно?":
                                $ KittyX.FaceChange("sly", 1)
                                $ KittyX.Statup("Love", 80, 1)
                                $ KittyX.Statup("Obed", 70, 1)
                                $ KittyX.Statup("Inbt", 60, 1)
                                ch_k "[Player.XName], это ты!"
                    ch_k "К чему это все?"
                    ch_k "Почему сразу нельзя было сказать?"
                    menu:
                        extend ""
                        "Извини, хотелось пошутить.":
                                $ KittyX.FaceChange("angry", 1)
                                $ KittyX.Statup("Love", 70, 1)
                                ch_k "Угу-м. . ."
                        "Молодец, ты все поняла.":
                                $ KittyX.FaceChange("angry", 1)
                                $ KittyX.Statup("Obed", 70, 1)
                                $ KittyX.Statup("Inbt", 80, 1)
                                ch_k "Это было трудно!"
                        "Хех.":
                                $ KittyX.FaceChange("sly", 1,Eyes="side")
                                $ KittyX.Statup("Love", 70, 1)
                                $ KittyX.Statup("Love", 90, 1)
                                $ KittyX.Statup("Inbt", 70, 1)
                                ch_k "Ага. . ."
                    ch_k "Но в конце концов я тебя раскусила."
        #end "tried to lie"
        $ KittyX.FaceChange("smile", 1)
        ch_k "Скажи, к чему все эти перемены?"
        menu:
            extend ""
            "Да так, по приколу.":
                    $ KittyX.Statup("Inbt", 70, 1)
                    $ KittyX.FaceChange("surprised", 2)
                    ch_k "Нууу. . . эм. . . наверное, в этом есть смысл. . ."
                    $ KittyX.FaceChange("sly", 1)
            "Я так себя сейчас ощущаю.":
                    ch_k "Ох. . . понятно."
            "У меня не было каких-то особых причин.":
                    ch_k "Хм. . . ладно."

        if [Player.Name] != [Player.XName]:
                ch_p "А еще теперь меня зовут [Player.Name]."
                ch_k "Ладно. . . [Player.Name] так [Player.Name]."

        if KittyX.SEXP >= 15:
                $ KittyX.FaceChange("sad", 1,Mouth="smile")
                ch_k "Я, эм. . . все еще тебя привлекаю, правда?"
                menu:
                    extend ""
                    "Конечно!":
                            $ KittyX.FaceChange("smile", 1)
                            $ KittyX.Statup("Love", 70, 2)
                            $ KittyX.Statup("Love", 90, 1)
                            ch_k "Хорошо."
                    "Да не особо.":
                            $ KittyX.FaceChange("sad", 1)
                            $ KittyX.Statup("Love", 80, -2)
                            $ KittyX.Statup("Obed", 60, 2)
                            $ KittyX.Statup("Obed", 80, 2)
                            ch_k "Ох. . ."
                            $ KittyX.FaceChange("sadside", 1)
                            ch_k "Ладно. . ."
                            if ApprovalCheck(KittyX, 1500):
                                    $ KittyX.FaceChange("sadside", 1,Mouth="smirk")
                                    if not Player.Male:
                                        ch_k "Но я всё равно думаю, что ты милая. . ."
                                    else:
                                        ch_k "Но я всё равно думаю, что ты милый. . ."
                    "А ты как думаешь?":
                            $ KittyX.FaceChange("sly", 1)
                            $ KittyX.Statup("Obed", 70, 1)
                            $ KittyX.Statup("Inbt", 70, 1)
                            ch_k "Что я. . . возбуждаю тебя?"

        if not Player.Male and KittyX.Les > 5:
                $ KittyX.FaceChange("sly", 1)
                ch_k "Пожалуй, ранее у меня уже был опыт с девушками. . ."
        if ApprovalCheck(KittyX, 1500):
                ch_k "Мы что-нибудь придумаем."
                $ KittyX.AddWord(1,0,0,0,"girltalk") #history
        else:
                $ KittyX.FaceChange("normal", 1,Eyes="side")
                ch_k "Наверное, мне нужно немного времени, чтобы все обдумать. . ."
        $ KittyX.Traits.remove("switchcheck")
        $ KittyX.AddWord(1,0,0,0,"switched") #history
        return

label Kitty_Switch2:
        #when you switch for a 2+ time
        $ KittyX.FaceChange("surprised", 1)
        ch_k "О!"
        $ KittyX.FaceChange("confused", 1)
        ch_k "Ты, эм. . . ты снова ты."
        $ KittyX.FaceChange("smile", 1)
        if not Player.Male:
            ch_k "Прежняя \"ты\"."
        else:
            ch_k "Прежний \"ты\"."
        ch_k "Здорово!"
        $ KittyX.Traits.remove("switchcheck")
        $ KittyX.History.remove("switched")
        $ KittyX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Kitty_Girltalk(Auto=0,Other=0):
        # if Auto Kitty starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in KittyX.History:
                return
        if "nogirls" in KittyX.History:
                jump Kitty_Girltalk_Redux
        if Auto:
                $ KittyX.FaceChange("angry", 1,Mouth="smile")
                ch_k "Так вот, мне просто интересно. . ."
                ch_k "Ты[KittyX.like]присматриваешься ко мне?"
        else:
                $ KittyX.FaceChange("confused", 1)
                ch_k "А? Я тебе нравлюсь?"
        menu:
            extend ""
            "Да?":
                    $ KittyX.FaceChange("surprised", 2)
                    $ KittyX.Statup("Love", 70, 2)
                    $ KittyX.Statup("Love", 90, 2)
                    $ KittyX.Statup("Obed", 70, 1)
                    ch_k "Хм. . ."
                    $ KittyX.FaceChange("smile", 1, Eyes="side")
            "Наверное?":
                    $ KittyX.FaceChange("confused", 2)
                    $ KittyX.Statup("Obed", 80, 2)
                    $ KittyX.Statup("Inbt", 80, 2)
                    ch_k "Хм. . ."
                    $ KittyX.FaceChange("sly", 1)
            "Не особо.":
                    $ KittyX.FaceChange("sadside", 2)
                    $ KittyX.Statup("Love", 50, -2)
                    $ KittyX.Statup("Love", 90, -2)
                    $ KittyX.Statup("Obed", 60, 2)
                    $ KittyX.Statup("Obed", 80, 2)
                    ch_k "Ох. . ."
        ch_k "А ты[KittyX.like]думаешь, что я сексуальная? . ."
        menu:
            extend ""
            "Да?":
                    $ KittyX.FaceChange("smile", 2)
                    $ KittyX.Statup("Love", 90, 2)
                    $ KittyX.Statup("Obed", 70, 1)
                    ch_k "Хм. . ."
                    $ KittyX.FaceChange("smile", 1, Eyes="side")
                    $ Auto = 0
            "Скорее \"милая.\"":
                    $ KittyX.FaceChange("angry", 1)
                    $ KittyX.Statup("Love", 80, -1)
                    $ KittyX.Statup("Obed", 60, 2)
                    $ KittyX.Statup("Obed", 80, 2)
                    ch_k ". . ."
                    $ KittyX.FaceChange("sadside", 1)
            "Наверное?":
                    $ KittyX.FaceChange("confused", 2)
                    $ KittyX.Statup("Obed", 80, 1)
                    $ KittyX.Statup("Inbt", 80, 1)
                    ch_k "Это довольно грубо. . ."
                    $ KittyX.FaceChange("sly", 1)
            "Не особо.":
                    $ KittyX.FaceChange("angry", 2)
                    $ KittyX.Statup("Love", 80, -2)
                    $ KittyX.Statup("Obed", 80, 1)
                    ch_k "Как грубо!"
                    $ KittyX.FaceChange("angry", 1,Eyes="side")

        if not KittyX.Les:
                ch_k "Честно говоря, я еще не. . ."
                $ KittyX.FaceChange("sadside", 2)
                ch_k "не занималась \"этим\". . ."
                ch_k "-с девушкой. . ."
        if not ApprovalCheck(KittyX, 1000) and not KittyX.Les:
                $ KittyX.FaceChange("sadside", 1)
                ch_k "Это как-то. . . нет, пожалуй, нет. . ."
                $ KittyX.AddWord(1,0,0,0,"nogirls") #history
                call Girltalk_Check(KittyX)
                return
        $ KittyX.FaceChange("sly", 1)
        ch_k "Но, думаю, для тебя я могла бы сделать исключение. . ."
        $ KittyX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(KittyX)
        return

label Kitty_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing
        if ApprovalCheck(KittyX, 1000):
                if not KittyX.Les and "nogirls" not in KittyX.History:
                        ch_k "Честно говоря, я еще не. . ."
                        $ KittyX.FaceChange("sadside", 2)
                        ch_k "не занималась \"этим\". . ."
                        ch_k "-с девушкой. . ."
                $ KittyX.FaceChange("sly", 1)
                ch_k "Меня немного смущает вся эта ситуация. . ."
                ch_k "Но, думаю, для тебя я могла бы сделать исключение. . ."
                $ KittyX.DrainWord("nogirls",0,0,0,1) #history
                $ KittyX.AddWord(1,0,0,0,"girltalk") #history
        elif "nogirls" not in KittyX.History:
                if not KittyX.Les:
                        ch_k "Честно говоря, я еще не. . ."
                        $ KittyX.FaceChange("sadside", 2)
                        ch_k "не занималась \"этим\". . ."
                        ch_k "-с девушкой. . ."
                $ KittyX.FaceChange("sadside", 1)
                ch_k "Это как-то. . . нет, пожалуй, нет. . ."
                $ KittyX.AddWord(1,0,0,0,"nogirls") #history
        elif "nogirls" in KittyX.DailyActions:
                $ KittyX.FaceChange("angry", 1)
                if KittyX.Forced:
                        #if Forced, she will just go with it anyway
                        if "nogirls" not in KittyX.RecentActions:
                                $ KittyX.Statup("Love", 80, -1)
                                $ KittyX.Statup("Obed", 80, 2)
                                $ KittyX.AddWord(1,"nogirls",0,0,0) #recent
                        return
                ch_k "[KittyX.Like]отстань!"
        else:
                $ KittyX.Statup("Inbt", 50, 2)
                ch_k "Как я уже сказала, я не уверена, что хочу таких отношений. . ."
                $ KittyX.AddWord(1,0,"nogirls",0,0) #daily
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Kitty_69_Intro:
        if "69" in KittyX.History:
                return
        if Trigger == "lick pussy" and KittyX.LickP:
                if KittyX.Blow or KittyX.CUN or (ApprovalCheck(KittyX, 1300) and KittyX.SeenPeen):
                        #if licking pussy but have gotten blowjob
                        $ KittyX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_k "[KittyX.Like]раз ты желаешь сделать мне приятно. . ."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        if "cockout" not in Player.RecentActions:
                                $ Player.RecentActions.append("cockout")
                                if Player.Male:
                                        "Она вытаскивает ваш член и начинает его сосать."
                                else:
                                        "Она обнажает вашу киску и начинает ее лизать."
                        else:
                                if Player.Male:
                                        "Она хватает ваш член и располагается над ним."
                                else:
                                        "Она начинает лизать вашу киску."
                        $ KittyX.Pose = "69"
                        call Kitty_BJ_Launch
                        if Player.Male:
                                ch_k "Не мог бы ты начать? . ."
                        else:
                                ch_k "Не могла бы ты начать? . ."
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ KittyX.Statup("Love", 95, 3)
                                    $ KittyX.Statup("Inbt", 70, 2)
                                    $ KittyX.Statup("Inbt", 90, 1)
                                    ch_k "Замечательно."
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ KittyX.Statup("Love", 80, -8)
                                    $ KittyX.Statup("Obed", 80, 3)
                                    $ KittyX.Statup("Obed", 90, 1)
                                    $ KittyX.Statup("Inbt", 70, -1)
                                    ch_k "Буууу."
                        $ Situation = "69"
                        call SexAct("blow") # call Kitty_SexAct("blow")
                        $ renpy.pop_call() #causes it to skip past the Escalation
                        $ renpy.pop_call() #causes it to skip past the last activity
        elif (Trigger == "blow" or Trigger == "cun") and (KittyX.Blow or KittyX.CUN):
                        #if licked pussy
                        $ KittyX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_k "Раз я тебе помогаю. . ."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        $ KittyX.Pose = "69"
                        call Kitty_BJ_Launch
                        if Player.Male:
                                ch_k ". . .не мог бы ты[KittyX.like]и мне помочь? . ."
                        else:
                                ch_k ". . .не могла бы ты[KittyX.like]и мне помочь? . ."
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ KittyX.Statup("Love", 95, 3)
                                    $ KittyX.Statup("Inbt", 70, 2)
                                    $ KittyX.Statup("Inbt", 90, 1)
                                    ch_k "Замечательно."
                                    if not KittyX.LickP:
                                        $ KittyX.LickP += 1
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ KittyX.Statup("Love", 80, -5)
                                    $ KittyX.Statup("Obed", 80, 3)
                                    $ KittyX.Statup("Obed", 90, 1)
                                    $ KittyX.Statup("Inbt", 70, -1)
                                    ch_k "Буууу."
                        #returns to BJ already in progress
        return
