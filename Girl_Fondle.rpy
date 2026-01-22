# Ch_Focus.Fondle /////////////////////////////////////////////////////////////////////////////
label Girl_Fondle: #rkeljsvgb
    $ Ch_Focus.Mouth = "smile"
    if not Ch_Focus.Action:
        call Sex_Basic_Dialog(Ch_Focus,"tired")
        return
    if Ch_Focus is RogueX:
            ch_r "Что именно ты желаешь потрогать, [RogueX.Petname]?"
    elif Ch_Focus is KittyX:
            ch_k "Эм, что ты хочешь потрогать, [KittyX.Petname]?"
    elif Ch_Focus is EmmaX:
            ch_e "Ну? Что ты хочешь потрогать, [EmmaX.Petname]?"
    elif Ch_Focus is LauraX:
            ch_l "Ну? Что ты хочешь потрогать, [LauraX.Petname]?"
    elif Ch_Focus is JeanX:
            ch_j "Ну? К чему ты хочешь прикоснуться, [JeanX.Petname]?"
    elif Ch_Focus is StormX:
            ch_s "Что ты хочешь потрогать, [StormX.Petname]?"
    elif Ch_Focus is JubesX:
            ch_v "Ну? Что ты хочешь потрогать, [JubesX.Petname]?"
    elif Ch_Focus is GwenX:
            ch_g "К чему ты хочешь прикоснуться, [GwenX.Petname]?"
    elif Ch_Focus is BetsyX:
            ch_b "К чему ты надеешься прикоснуться, [BetsyX.Petname]?"
    elif Ch_Focus is DoreenX:
            ch_d "К чему ты хочешь прикоснуться, [DoreenX.Petname]?"
    elif Ch_Focus is WandaX:
            ch_w "К чему ты желаешь прикоснуться, [WandaX.Petname]?"
    menu:
        extend ""
        "К твоей груди." if Ch_Focus.Action:
                jump Girl_Fondle_Breasts
        "К твоим бедрам." if Ch_Focus.Action:
                jump Girl_Fondle_Thighs
        "К твоей киске." if Ch_Focus.Action:
                jump Girl_Fondle_Pussy
        "К твоей попке." if Ch_Focus.Action:
                jump Girl_Fondle_Ass
        "Неважно.":
                return
    return


# Ch_Focus.Fondle Breasts /////////////////////////////////////////////////////////////////////////////
label Girl_Fondle_Breasts: #rkeljsvgb
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)

    # Will she let you fondle? Modifiers
    if Ch_Focus.FondleB: #You've done it before
        $ Tempmod += 15
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 3
    if Ch_Focus.Lust > 75: #She's really horny
        $ Tempmod += 20
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (3*Ch_Focus.Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 20
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10
    if Ch_Focus.Taboo and "public" not in Ch_Focus.History:
        $ Tempmod -= 20

    if "no fondle breasts" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no fondle breasts" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 950, TabM = 3) # 95, 110, 125 -120(215)

    if Situation == "auto":
        if Approval:
            $ Ch_Focus.FaceChange("sexy")
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Obed", 70, 2)
            $ Ch_Focus.Statup("Inbt", 70, 3)
            $ Ch_Focus.Statup("Inbt", 30, 2)
            "Когда вы берете ее грудь в свои руки, [Ch_Focus.Name] мягко кивает."
            jump Girl_FB_Prep
        else:
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Brows = "confused"
            $ Ch_Focus.Statup("Obed", 50, -2)
            if Ch_Focus is RogueX:
                    if not Player.Male:
                        ch_r "Ах, просто продолжай то, что делала, [RogueX.Petname]."
                    else:
                        ch_r "Ах, просто продолжай то, что делал, [RogueX.Petname]."
            elif Ch_Focus is KittyX:
                    if not Player.Male:
                        ch_k "Не-а, [KittyX.Petname], вернись к тому, что делала ранее."
                    else:
                        ch_k "Не-а, [KittyX.Petname], вернись к тому, что делал ранее."
            elif Ch_Focus is EmmaX:
                    if not Player.Male:
                        ch_e "Полегче, ты так хорошо справлялась. . ."
                    else:
                        ch_e "Полегче, ты так хорошо справлялся. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Давай вернемся назад, [LauraX.Petname]. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Не так быстро, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Пожалуй, нет, не сейчас. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Сбавь обороты, [JubesX.Petname]. . ."
            elif Ch_Focus is GwenX:
                    if not Player.Male:
                        ch_g "Эм. . . не могла бы ты убрать руку, [GwenX.Petname]. . ?"
                    else:
                        ch_g "Эм. . . не мог бы ты убрать руку, [GwenX.Petname]. . ?"
            elif Ch_Focus is BetsyX:
                    ch_b "Мне кажется, твоя рука не на своем месте, [BetsyX.Petname]. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Не думаю, что тебе нужно было передвигать руку, [DoreenX.Petname]. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Эй-эй, верни руку обратно, [WandaX.Petname]. . ."
            $ Tempmod = 0
            $ Trigger2 = 0
            return

    # fondle yes:

    if Approval:                                                                       #Second time+ dialog
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
        elif not Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabyes") #"This does seem less. . . exposed."

    if "fondle breasts" in Ch_Focus.RecentActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                call AnyLine(Ch_Focus,"Мммм, опять? Что ж, пожалуй, я не против. . .")
        else:
                call AnyLine(Ch_Focus,"Снова? Ну ладно.")
        jump Girl_FB_Prep
    elif "fondle breasts" in Ch_Focus.DailyActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Ах, расслабься. . .",
                    "Нежнее. . . нежнее. . .",
                    "Давай нежно и осторожно. . .",
                    "Расслабься. . .",
                    "Ммм. . ."])
        else:
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Ах, расслабься. . .",
                    "Тебе все мало?",
                    "Осторожнее.",
                    "Оу, расслабься. . .",
                    "Расслабься. . .",
                    "Давай в этот раз полегче. . .",
                    "Расслабься. . .",
                    "Ммм. . ."])
        call AnyLine(Ch_Focus,Line)

    if Approval >= 2:
        $ Ch_Focus.FaceChange("bemused", 1)
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Inbt", 60, 1)
        if Ch_Focus is RogueX:
                ch_r "Ладно, [RogueX.Petname], подойди и возьми."
        elif Ch_Focus is KittyX:
                ch_k "Ладно, [KittyX.Petname], подойди и возьми."
        elif Ch_Focus is EmmaX:
                ch_e "Звучит прекрасно, сделай мне приятно."
        elif Ch_Focus is LauraX:
                ch_l "Конечно, звучит весело."
        elif Ch_Focus is JeanX:
                ch_j "Конечно, звучит весело."
        elif Ch_Focus is StormX:
                ch_s "С удовольствием. . ."
        elif Ch_Focus is JubesX:
                ch_v "Конечно, звучит весело."
        elif Ch_Focus is GwenX:
                ch_g "Конечно, звучит весело."
        elif Ch_Focus is BetsyX:
                ch_b "Понимаю."
        elif Ch_Focus is DoreenX:
                ch_d "Конечно."
        elif Ch_Focus is WandaX:
                ch_w "Конечно."
        $ Ch_Focus.Statup("Love", 90, 1)
        $ Ch_Focus.Statup("Inbt", 50, 3)
        jump Girl_FB_Prep

    else:
        $ Ch_Focus.FaceChange("angry", 1)
        if "no fondle breasts" in Ch_Focus.RecentActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions and "no fondle breasts" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif "no fondle breasts" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif not Ch_Focus.FondleB:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "[RogueX.Petname], я не уверена, что уже готова. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Я[KittyX.like]не готова к этому, [KittyX.Petname]. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Я очень сомневаюсь, что ты справишься, [EmmaX.Petname]. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Послушай, я не знаю, готовы ли мы к этому, [LauraX.Petname]. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Можешь смотреть, но не трогать, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Возможно, в другой раз, [StormX.Petname]. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Послушай, я не знаю, готовы ли мы к этому, [JubesX.Petname]. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Ох, эм. . . я не уверена, [GwenX.Petname]. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Ох, дорогуша, . . я не уверена, [BetsyX.Petname]. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Ох. . . я не уверена, [DoreenX.Petname]. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Я не уверена, готова ли я, [WandaX.Petname]. . ."
        else:
            $ Ch_Focus.FaceChange("bemused")
            call Sex_Basic_Dialog(Ch_Focus,"nothanks")
        menu:
            extend ""
            "Извини, забудь." if "no fondle breasts" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"noproblem")  # ch_r "Ok, no problem, [RogueX.Petname]."
                return
            "Может, в другой раз?" if "no fondle breasts" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy")
                if Ch_Focus in (EmmaX,StormX,DoreenX):
                        "Она поправляет декольте."
                call Sex_Basic_Dialog(Ch_Focus,"maybe")  # ch_d "I'll think about it, [Ch_Focus.Petname]."
                $ Ch_Focus.Statup("Love", 80, 1)
                $ Ch_Focus.Statup("Love", 50, 1)
                $ Ch_Focus.Statup("Inbt", 30, 2)
                if Taboo:
                    $ Ch_Focus.RecentActions.append("tabno")
                    $ Ch_Focus.DailyActions.append("tabno")
                $ Ch_Focus.RecentActions.append("no fondle breasts")
                $ Ch_Focus.DailyActions.append("no fondle breasts")
                return
            "Ну давай, пожалуйста?":
                if Approval:
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 50, 2)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    $ Ch_Focus.Statup("Inbt", 30, 2)
                    call Sex_Basic_Dialog(Ch_Focus,"pleaseyes")  # ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
                    jump Girl_FB_Prep
                else:
                    $ Ch_Focus.FaceChange("sexy")
                    call Sex_Basic_Dialog(Ch_Focus,"pleaseno") #ch_r "I'm afraid not this time, sorry [RogueX.Petname]."

            "[[Все равно схватить ее за грудь]":                                                       # Pressured into fondling.
                $ Approval = ApprovalCheck(Ch_Focus, 350, "OI", TabM = 3) # 35, 50, 65
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -5, 1)
                    $ Ch_Focus.Statup("Love", 20, -2, 1)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #ch_w "Whoa!" ch_w ". . ." ch_w "Ok, ok, just get to it. . ."
                    $ Ch_Focus.Statup("Obed", 90, 2)
                    $ Ch_Focus.Statup("Obed", 50, 4)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ Ch_Focus.Forced = 1
                    jump Girl_FB_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -10)
                    $ Ch_Focus.FaceChange("angry", 1)
                    $ Line = renpy.random.choice(["Что?",
                        "Эй!",
                        "М?",
                        "Воу!",
                        "Прошу прощения?",
                        "Не-а."])
                    call AnyLine(Ch_Focus,Line)
                    "Она шлепает вас по руке."
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    if "no fondle breasts" in Ch_Focus.DailyActions:
        call Sex_Basic_Dialog(Ch_Focus,"noday") #"Stop asking."
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("angry", 1)
        if Ch_Focus is RogueX:
                if not Player.Male:
                    ch_r "Я не хочу, чтобы ты касалась меня."
                else:
                    ch_r "Я не хочу, чтобы ты касался меня."
        elif Ch_Focus is KittyX:
                ch_k "Даже не думай."
        elif Ch_Focus is EmmaX:
                ch_e "Не искушай судьбу."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Ты заходишь слишком далеко."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Эм, нет, спасибо. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, я не могу. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Для меня это слишком. . ."
        elif Ch_Focus is WandaX:
                ch_w "Это не по мне."
        $ Ch_Focus.Statup("Lust", 60, 5)
        $ Ch_Focus.Statup("Obed", 50, -2)
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Taboo:
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.RecentActions.append("tabno")
        $ Ch_Focus.DailyActions.append("tabno")
        call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You picked a bad place for this. . ."
    elif Ch_Focus.FondleB:
        $ Ch_Focus.FaceChange("sad")
        if Ch_Focus is RogueX:
                ch_r "Извини, [RogueX.Petname], ты больше к ним не притронешься."
        elif Ch_Focus is KittyX:
                ch_k "У тебя был шанс."
        elif Ch_Focus is EmmaX:
                ch_e "Боюсь, ты не заслуживаешь моего расположения."
        elif Ch_Focus is LauraX:
                ch_l "Тебе придется снова заслужить это."
        elif Ch_Focus is JeanX:
                ch_j "С нас хватит этого."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Тебе придется это заслужить."
        elif Ch_Focus is GwenX:
                ch_g "Я, эм. . . больше не хочу."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, этого больше не повторится."
        elif Ch_Focus is DoreenX:
                ch_d "Нет, я не хочу."
        elif Ch_Focus is WandaX:
                ch_w "Не сейчас."
    else:
        $ Ch_Focus.FaceChange("sexy")
        $ Ch_Focus.Mouth = "sad"
        if Ch_Focus is RogueX:
                ch_r "Этого не произойдет."
        elif Ch_Focus is KittyX:
                ch_k "Ни за что."
        elif Ch_Focus is EmmaX:
                ch_e "Нет."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Не-а."
        elif Ch_Focus is BetsyX:
                ch_b "Благодарю, но нет."
        elif Ch_Focus is DoreenX:
                ch_d "Нет, спасибо."
        elif Ch_Focus is WandaX:
                ch_w "Нет, спасибо."
    $ Ch_Focus.RecentActions.append("no fondle breasts")
    $ Ch_Focus.DailyActions.append("no fondle breasts")
    $ Tempmod = 0
    return


label Girl_FB_Prep:  #rkeljsvgb
#    if Trigger == "kiss you":
#        $ Trigger = "fondle breasts"
#        return

    if Trigger2 == "fondle breasts":
        return

    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle breasts")
    else:
            call ViewShift(Ch_Focus,"breasts",0,"fondle breasts")

    if Situation == Ch_Focus:
            #Girl auto-starts
            $ Situation = 0
            if (Ch_Focus.Over or Ch_Focus.Chest) and not Ch_Focus.Uptop:
                #if she has some sort of top on. . .
                if ApprovalCheck(Ch_Focus, 1250, TabM = 1) or (Ch_Focus.SeenChest and ApprovalCheck(Ch_Focus, 500) and not Taboo):
                        $ Ch_Focus.Uptop = 1
                        $ Line = get_clothing_name(Ch_Focus.Over_key, vin) if Ch_Focus.Over else get_clothing_name(Ch_Focus.Chest_key, vin)
                        "С голодной ухмылкой, [Ch_Focus.Name] приподнимает [Line] над своей грудью."
                        call Girl_First_Topless(Ch_Focus,1)
                        $ Line = 0
                        "Затем она хватает вас за руку и прижимает ладонь к своей груди, явно желая, чтобы вы приступили к делу."
                else:
                        "[Ch_Focus.Name] хватает вас за руку и прижимает ладонь к своей прикрытой груди, явно желая, чтобы вы приступили к делу."
            else:
                        "[Ch_Focus.Name] хватает вас за руку и прижимает ладонь к своей груди, явно желая, чтобы вы приступили к делу."
            menu:
                "Что будете делать?"
                "Приступить.":
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 2)
                    "Вы начинаете ласкать ее грудь."
                "Похвалить ее.":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    ch_p "[Ch_Focus.Pet], мне нравится твоя инициатива."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "Вы начинаете ласкать ее грудь."
                    $ Ch_Focus.Statup("Love", 85, 1)
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    "Вы одергиваете руку."
                    $ Ch_Focus.FaceChange("surprised")
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    ch_p "[Ch_Focus.Pet], давай не будем."
                    if Ch_Focus is JeanX:
                            $ JeanX.Statup("Love", 70, -3)
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] отстраняется."
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 1)
                    $ Ch_Focus.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ Ch_Focus.AddWord(1,"refused","refused")
                    return
            #end auto

    if not Ch_Focus.Forced and Situation != "auto":
        $ Tempmod = 0
        call Top_Off(Ch_Focus)
        if "angry" in Ch_Focus.RecentActions:
            return

    $ Tempmod = 0
    if not Ch_Focus.FondleB:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -20)
            $ Ch_Focus.Statup("Obed", 70, 25)
            $ Ch_Focus.Statup("Inbt", 80, 15)
        else:
            $ Ch_Focus.Statup("Love", 90, 10)
            $ Ch_Focus.Statup("Obed", 70, 5)
            $ Ch_Focus.Statup("Inbt", 80, 15)

    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no fondle breasts")
    $ Ch_Focus.AddWord(0,"fondle breasts","fondle breasts")
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle breasts")
    else:
            call ViewShift(Ch_Focus,"breasts",0,"fondle breasts")

label Girl_FB_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle breasts")
#        call Shift_Focus(Girl)
        $ Ch_Focus.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . .":
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_FB_Cycle
                        "В стиле минета" if Ch_Focus.Pose == "69":
                                    call Girl_BJ_Menu
                                    jump Girl_FB_Cycle

                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                        "Сменить вид":
                                    call ViewShift(Ch_Focus,"menu")
                                    jump Girl_FB_Cycle

                        "Другие варианты":
                                menu:
                                    "Дополнительное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ Ch_Focus.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Сменить основное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                    menu:
                                                        "Попросить пососать их.":
                                                                if Ch_Focus.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Girl_FB_After
                                                                    call Girl_Suck_Breasts
                                                                else:
                                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        "Начать сосать их не спрашивая.":
                                                                if Ch_Focus.Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call Girl_FB_After
                                                                    call Girl_Suck_Breasts
                                                                else:
                                                                    "Когда вы наклоняетесь, чтобы пососать ее грудь, она хватает вас за голову и отталкивает назад."
                                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        "Неважно":
                                                                    jump Girl_FB_Cycle
                                            else:
                                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Тройничек (locked)" if not Partner:
                                        pass
                                    "Тройничек" if Partner:
                                        menu:
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе" if Trigger == "lesbian":
                                                        call Les_Change(Ch_Focus)
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Пусть [Partner.Name] займется чем-нибудь другим":
                                                        call Three_Change(Ch_Focus)

                                            "Не бросай свое текущее занятие. . . (locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_FB_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_FB_Cycle
                                            "Неважно":
                                                        jump Girl_FB_Cycle

                                    "Показывать ее ноги" if not ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Вставить анальную пробку" if not Ch_Focus.Plug and "plug" in Ch_Focus.Inventory:
                                            call Insert_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку" if Ch_Focus.Plug:
                                            call Remove_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку (locked)" if "plug" not in Ch_Focus.Inventory:
                                            pass

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_FB_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_FB_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_FB_After
        #End menu (if Line)

#        call Shift_Focus(Girl)
        call Sex_Dialog(Ch_Focus,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Ch_Focus)
                            if "angry" in Ch_Focus.RecentActions:
                                call Girl_Pos_Reset(Ch_Focus)
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_FB_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Doreen can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_FB_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in Ch_Focus.RecentActions and Ch_Focus.SEXP >= 20:#And Doreen is unsatisfied,
                                "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                menu:
                                    "Хотите завершить начатое?"
                                    "Продолжим еще немного.":
                                        $ Line = "Вы возвращаетесь к процессу"
                                    "С меня хватит.":
                                        "Вы заканчиваете веселье."
                                        jump Girl_FB_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.FondleB):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Ты просто не можешь оторваться, да?"
                    elif Ch_Focus is KittyX:
                            ch_k "Ты просто не можешь оторваться, да?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Они ведь великолепны, верно?"
                    elif Ch_Focus is LauraX:
                            ch_l "Тебе нравится?"
                    elif Ch_Focus is JeanX:
                            ch_j "Ну как, тебе весело?"
                    elif Ch_Focus is StormX:
                            ch_s "Похоже, тебе это очень нравится. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Веселишься?"
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе, эм. . . нравится?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Тебе. . . приятно?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Тебе. . . приятно?"
                    elif Ch_Focus is WandaX:
                            ch_w "Тебе нравится?"
        elif Ch_Focus.Lust >= 85:
                    pass
        elif Cnt == (15 + Ch_Focus.FondleB) and Ch_Focus.SEXP >= 15 and not ApprovalCheck(Ch_Focus, 1500):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Я знаю, что тебе весело, но, возможно, нам стоит попробовать что-нибудь другое, [RogueX.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Может быть, мы могли бы попробовать что-нибудь еще, [KittyX.Petname]?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Возможно, мы могли бы попробовать что-то другое, [EmmaX.Petname]?"
                    elif Ch_Focus is LauraX:
                            ch_l "Может, пришло время для чего-нибудь другого, [LauraX.Petname]?"
                    elif Ch_Focus is JeanX:
                            ch_j "Может, пришло время для чего-нибудь другого, [JeanX.Petname]?"
                    elif Ch_Focus is StormX:
                            ch_s "Уверена, тебе сейчас весело, но не могли бы мы попробовать что-нибудь другое?"
                    elif Ch_Focus is JubesX:
                            ch_v "Может, попробуем. . . что-нибудь другое?"
                    elif Ch_Focus is GwenX:
                            ch_g "Может, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Может быть, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Не могли бы мы заняться чем-нибудь другим?"
                    elif Ch_Focus is WandaX:
                            ch_w "Разве мы не можем заняться чем-нибудь другим?"

                    menu:
                        extend ""
                        "Закончить.":
                                "Вы заканчиваете веселье. . ."
                                jump Girl_FB_After
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Girl_FB_After
                        "Не-а, это так весело.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она возмущается, но позволяет вам продолжить."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call Girl_Pos_Reset(Ch_Focus)
                                    "Она кидает на вас сердитый взгляд и отстраняется."
                                    if Ch_Focus is RogueX:
                                            ch_r "Раз ты так ко мне относишься, я не нуждаюсь в твоей \"помощи\"."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Может тебе и весело, но я уже устала."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Возможно, тебе и нравится, но мне уже немного больно."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Раз так, то у меня найдутся дела поинтереснее."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Раз так, то у меня найдутся дела поинтереснее."
                                    elif Ch_Focus is StormX:
                                            ch_s "Что ж, как бы тебе не нравилось, мне нужно сделать перерыв."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Мне ужасно скучно. . ."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Эм. . . перестань."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Тогда, боюсь, мне придется тебя покинуть."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Облом тебе."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Что ж, а -мне- скучно."
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_FB_After
        #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10) #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5) #ch_d "Tic tock, [Ch_Focus.Petname]."

        if Ch_Focus.Lust >= 50 and not Ch_Focus.Uptop and (Ch_Focus.Chest or Ch_Focus.Over):
                $ Ch_Focus.Uptop = 1
                "[Ch_Focus.Name] ухмыляется и сдвигает одежду в сторону."
                call Girl_First_Topless(Ch_Focus)

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done") # "Ok, [Ch_Focus.Petname], breaktime."

label Girl_FB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Girl_Pos_Reset(Ch_Focus)

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.FondleB += 1
    $ Ch_Focus.Action -=1
    $ Ch_Focus.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Ch_Focus.Addictionrate += 1

    call Partner_Like(Ch_Focus,2)

    if Ch_Focus.FondleB == 1:
            $ Ch_Focus.SEXP += 4
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                        if Ch_Focus is RogueX:
                                ch_r "Это было. . . очень приятно, [RogueX.Petname]."
                        elif Ch_Focus is KittyX:
                                ch_k "Надеюсь, я[KittyX.like]тебе понравилось."
                        elif Ch_Focus is EmmaX:
                                ch_e "Уверена, это превзошло все твои ожидания. . ."
                        elif Ch_Focus is LauraX:
                                ch_l "Тебе понравилось?"
                        elif Ch_Focus is JeanX:
                                ch_j "Уверена, тебе понравилось."
                        elif Ch_Focus is StormX:
                                ch_s "Это было довольно весело. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Тебе понравилось?"
                        elif Ch_Focus is GwenX:
                                ch_g "Было. . . весело?"
                        elif Ch_Focus is BetsyX:
                                ch_b "Тебе понравилось?"
                        elif Ch_Focus is DoreenX:
                                ch_d "Тебе было весело?"
                        elif Ch_Focus is WandaX:
                                ch_w "Неплохо, да?"
                #end if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                        $ Ch_Focus.FaceChange("perplexed", 1)
                        if Ch_Focus is RogueX:
                                if not Player.Male:
                                    ch_r "Ты повеселилась?"
                                else:
                                    ch_r "Ты повеселился?"
                        elif Ch_Focus is KittyX:
                                if not Player.Male:
                                    ch_k "Ты ведь не разочарована?"
                                else:
                                    ch_k "Ты ведь не разочарован?"
                        elif Ch_Focus is EmmaX:
                                if not Player.Male:
                                    ch_e "Что ж, ты определенно сорвала джекпот."
                                else:
                                    ch_e "Что ж, ты определенно сорвал джекпот."
                        elif Ch_Focus is LauraX:
                                if not Player.Male:
                                    ch_l "Ты удовлетворена?"
                                else:
                                    ch_l "Ты удовлетворен?"
                        elif Ch_Focus is JeanX:
                                if not Player.Male:
                                    ch_j "Ты получила то, что хотела?"
                                else:
                                    ch_j "Ты получил то, что хотел?"
                        elif Ch_Focus is StormX:
                                ch_s "Полагаю, тебе понравилось. . ."
                        elif Ch_Focus is JubesX:
                                if not Player.Male:
                                    ch_v "Ты удовлетворена?"
                                else:
                                    ch_v "Ты удовлетворен?"
                        elif Ch_Focus is GwenX:
                                ch_g "Тебе понравилось?"
                        elif Ch_Focus is BetsyX:
                                if not Player.Male:
                                    ch_b "Ты удовлетворена?"
                                else:
                                    ch_b "Ты удовлетворен?"
                        elif Ch_Focus is DoreenX:
                                ch_d "Тебе этого достаточно?"
                        elif Ch_Focus is WandaX:
                                ch_w "Тебе этого достаточно?"
                #end elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
    $ Tempmod = 0
    call Checkout
    return

# End Girl Fondle Breasts


# R Suck Breasts /////////////////////////////////////////////////////////////////////////////

label Girl_Suck_Breasts: #rkeljsvgb
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)
                                                                                        # Will she let you suck? Modifiers
    if Ch_Focus.SuckB: #You've done it before
        $ Tempmod += 15
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 3
    if not Ch_Focus.Chest and not Ch_Focus.Over:
        $ Tempmod += 15
    if Ch_Focus.Lust > 75: #She's really horny
        $ Tempmod += 20
    if Ch_Focus.Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (4*Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 25
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10
    if Ch_Focus in (EmmaX,StormX) and Ch_Focus.Taboo and "public" not in Ch_Focus.History:
        $ Tempmod -= 20

    if "no suck breasts" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no suck breasts" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ Ch_Focus.FaceChange("sexy")
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Obed", 70, 2)
            $ Ch_Focus.Statup("Inbt", 70, 3)
            $ Ch_Focus.Statup("Inbt", 30, 2)
            "Когда вы припадаете к ее груди, [Ch_Focus.Name] слегка удивляется."
            jump Girl_SB_Prep
        else:
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Statup("Obed", 50, -2)
            if Ch_Focus is RogueX:
                    if not Player.Male:
                        ch_r "Слушай, просто продолжай то, что делала, [RogueX.Petname]."
                    else:
                        ch_r "Слушай, просто продолжай то, что делал, [RogueX.Petname]."
            elif Ch_Focus is KittyX:
                    if not Player.Male:
                        ch_k "Не-а, [KittyX.Petname], вернись к тому, что делала ранее."
                    else:
                        ch_k "Не-а, [KittyX.Petname], вернись к тому, что делал ранее."
            elif Ch_Focus is EmmaX:
                    if not Player.Male:
                        ch_e "Полегче, ты так хорошо справлялась. . ."
                    else:
                        ch_e "Полегче, ты так хорошо справлялся. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Давай вернемся назад, [LauraX.Petname]. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Не так быстро, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Прояви немного самообладания. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Сбавь обороты, [JubesX.Petname]. . ."
            elif Ch_Focus is GwenX:
                    if not Player.Male:
                        ch_g "Эм, не могла бы ты откатиться на секунду назад, [GwenX.Petname]. . ."
                    else:
                        ch_g "Эм, не мог бы ты откатиться на секунду назад, [GwenX.Petname]. . ."
            elif Ch_Focus is BetsyX:
                    ch_b ". . . тебе не стоит забегать вперед, [BetsyX.Petname]. . ."
            elif Ch_Focus is DoreenX:
                    ch_d ". . . мне кажется, ты спешишь, [DoreenX.Petname]. . ."
            elif Ch_Focus is WandaX:
                    ch_w ". . . послушай, ты слишком спешишь, [WandaX.Petname]. . ."
            $ Tempmod = 0
            $ Trigger2 = 0
            return

    if "suck breasts" in Ch_Focus.RecentActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                call AnyLine(Ch_Focus,"Мммм, опять? Что ж, пожалуй, я не против. . .")
        else:
                call AnyLine(Ch_Focus,"Снова? Ну ладно.")
        jump Girl_SB_Prep
    elif "suck breasts" in Ch_Focus.DailyActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Ах, расслабься. . .",
                    "Давай нежно и осторожно.",
                    "Нежнее. . . нежнее. . .",
                    "Осторожнее. . .",
                    "Ммм. . ."])
        else:
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Ах, нежнее. . .",
                    "Тебе все мало?",
                    "Осторожнее.",
                    "Ах, расслабься. . .",
                    "Расслабься. . .",
                    "Давай в этот раз полегче.",
                    "Расслабься. . .",
                    "Ммм. . ."])
        call AnyLine(Ch_Focus,Line)

    if Approval >= 2:                                                                   #She's into it. . .
        $ Ch_Focus.FaceChange("bemused", 1)
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Inbt", 60, 1)
        if Ch_Focus is RogueX:
                ch_r "Ладно, [RogueX.Petname], подойди и возьми."
        elif Ch_Focus is KittyX:
                ch_k "Ладно, лаааадно."
        elif Ch_Focus is EmmaX:
                ch_e "Звучит прекрасно, сделай мне приятно."
        elif Ch_Focus is LauraX:
                ch_l "Конечно, звучит весело."
        elif Ch_Focus is JeanX:
                ch_j "Конечно, звучит весело."
        elif Ch_Focus is StormX:
                ch_s "С удовольствием. . ."
        elif Ch_Focus is JubesX:
                ch_v "Конечно, звучит весело."
        elif Ch_Focus is GwenX:
                ch_g "Конечно, звучит весело."
        elif Ch_Focus is BetsyX:
                ch_b "Понимаю."
        elif Ch_Focus is DoreenX:
                ch_d "Конечно."
        elif Ch_Focus is WandaX:
                ch_w "Конечно."
        $ Ch_Focus.Statup("Love", 90, 1)
        $ Ch_Focus.Statup("Inbt", 50, 3)
        jump Girl_SB_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("angry", 1)
        if "no suck breasts" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions and "no suck breasts" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif "no suck breasts" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif not Ch_Focus.SuckB:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "[RogueX.Petname], я не уверена, что уже готова. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Я[KittyX.like]не готова к этому, [KittyX.Petname]. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Я очень сомневаюсь, что ты справишься, [EmmaX.Petname]. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Послушай, я не знаю, готовы ли мы к этому, [LauraX.Petname]. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Можешь смотреть, но не трогать, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Возможно, в другой раз, [StormX.Petname]. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Послушай, я не знаю, готовы ли мы к этому, [JubesX.Petname]. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Ох, эм. . . я не уверена, [GwenX.Petname]. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Ох, дорогуша, . . я не уверена, [BetsyX.Petname]. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Ох. . . я не уверена, [DoreenX.Petname]. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Я не уверена, готова ли я, [WandaX.Petname]. . ."
        elif not Ch_Focus.SuckB:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "[RogueX.Petname], я не уверена, что уже готова. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Не. . . сейчас. . . может быть, в другой раз."
            elif Ch_Focus is EmmaX:
                    ch_e "Я очень сомневаюсь, что ты справишься, [EmmaX.Petname]. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Думаю, мы можем над этим поработать. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Можешь смотреть, но не трогать, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Возможно, в другой раз, [StormX.Petname]. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Послушай, я не знаю, готовы ли мы к этому, [JubesX.Petname]. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Ох, эм. . . я не уверена, [GwenX.Petname]. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Ох, дорогуша, . . я не уверена, [BetsyX.Petname]. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Ох. . . я не уверена, [DoreenX.Petname]. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Я не уверена, готова ли я, [WandaX.Petname]. . ."
        else:
            $ Ch_Focus.FaceChange("bemused")
            call Sex_Basic_Dialog(Ch_Focus,"nothanks")
        menu:
            extend ""
            "Извини, забудь." if "no suck breasts" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"noproblem")  # ch_r "Ok, no problem, [RogueX.Petname]."
                return
            "Может, в другой раз?" if "no suck breasts" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy")
                call Sex_Basic_Dialog(Ch_Focus,"maybe")  # ch_d "I'll think about it, [Ch_Focus.Petname]."
                $ Ch_Focus.Statup("Love", 80, 1)
                $ Ch_Focus.Statup("Love", 50, 1)
                $ Ch_Focus.Statup("Inbt", 30, 2)
                if Taboo:
                    $ Ch_Focus.RecentActions.append("tabno")
                    $ Ch_Focus.DailyActions.append("tabno")
                $ Ch_Focus.RecentActions.append("no suck breasts")
                $ Ch_Focus.DailyActions.append("no suck breasts")
                return
            "Ну давай, пожалуйста?":
                if Approval:
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    $ Ch_Focus.Statup("Inbt", 30, 2)
                    call Sex_Basic_Dialog(Ch_Focus,"pleaseyes")  # ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
                    jump Girl_SB_Prep
                else:
                    $ Ch_Focus.FaceChange("angry")
                    call Sex_Basic_Dialog(Ch_Focus,"pleaseno") #ch_r "I'm afraid not this time, sorry [RogueX.Petname]."

            "[[Все равно начать сосать]":                                          # Pressured into licking.
                $ Approval = ApprovalCheck(Ch_Focus, 450, "OI", TabM = 3) # 45, 60, 75, -120(165)
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -5, 1)
                    $ Ch_Focus.Statup("Love", 20, -2, 1)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #ch_w "Whoa!" ch_w ". . ." ch_w "Ok, ok, just get to it. . ."
                    $ Ch_Focus.Statup("Obed", 90, 2)
                    $ Ch_Focus.Statup("Obed", 50, 4)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ Ch_Focus.Forced = 1
                    jump Girl_SB_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -10)
                    $ Ch_Focus.FaceChange("angry", 1)
                    $ Line = renpy.random.choice(["Что?",
                        "Эй!",
                        "М?",
                        "Воу!",
                        "Прошу прощения?",
                        "Хм."])
                    call AnyLine(Ch_Focus,Line)
                    "Она отталкивает вашу голову назад."
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    if "no suck breasts" in Ch_Focus.DailyActions:
        call Sex_Basic_Dialog(Ch_Focus,"noday") #"Stop asking."
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("angry", 1)
        if Ch_Focus is RogueX:
                ch_r "Я не хочу, чтобы твои губы касались меня."
        elif Ch_Focus is KittyX:
                ch_k "[KittyX.Like]убери свой рот от меня."
        elif Ch_Focus is EmmaX:
                ch_e "Не стоит."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Ты заходишь слишком далеко."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Эм, нет, спасибо. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, я не могу. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Это слишком для меня. . ."
        elif Ch_Focus is WandaX:
                ch_w "Это не по мне."
        $ Ch_Focus.Statup("Lust", 60, 5)
        $ Ch_Focus.Statup("Obed", 50, -2)
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Taboo:
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.RecentActions.append("tabno")
        $ Ch_Focus.DailyActions.append("tabno")
        call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You picked a bad place for this. . ."
    elif Ch_Focus.SuckB:
        $ Ch_Focus.FaceChange("sad")
        if Ch_Focus is RogueX:
                ch_r "Извини, [RogueX.Petname], ты больше к ним не притронешься."
        elif Ch_Focus is KittyX:
                ch_k "У тебя был шанс."
        elif Ch_Focus is EmmaX:
                ch_e "Я сожалею, но, может быть, в другой раз?"
        elif Ch_Focus is LauraX:
                ch_l "Тебе придется снова заслужить это."
        elif Ch_Focus is JeanX:
                ch_j "С нас хватит этого."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Тебе придется это заслужить."
        elif Ch_Focus is GwenX:
                ch_g "Я, эм. . . больше не хочу."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, этого больше не повторится."
        elif Ch_Focus is DoreenX:
                ch_d "Я должна тебя расстроить."
        elif Ch_Focus is WandaX:
                ch_w "Не сейчас."
    else:
        $ Ch_Focus.FaceChange("sexy")
        $ Ch_Focus.Mouth = "sad"
        if Ch_Focus is RogueX:
                ch_r "Этого не произойдет."
        elif Ch_Focus is KittyX:
                ch_k "Нееее-а."
        elif Ch_Focus is EmmaX:
                ch_e "Нет."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Не-а."
        elif Ch_Focus is BetsyX:
                ch_b "Давай не будем."
        elif Ch_Focus is DoreenX:
                ch_d "Это очень интимное занятие. . ."
        elif Ch_Focus is WandaX:
                ch_w "Нет, спасибо."
    $ Ch_Focus.RecentActions.append("no suck breasts")
    $ Ch_Focus.DailyActions.append("no suck breasts")
    $ Tempmod = 0
    return


label Girl_SB_Prep: #rkeljsvgb

    if Trigger2 == "suck breasts":
        return

    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"suck breasts")
    else:
            call ViewShift(Ch_Focus,"breasts",0,"suck breasts")

    if Situation == Ch_Focus:
            #Doreen auto-starts
            $ Situation = 0
            if (Ch_Focus.Over or Ch_Focus.Chest) and not Ch_Focus.Uptop:
                #if she has some sort of top on. . .
                if ApprovalCheck(Ch_Focus, 1250, TabM = 1) or (Ch_Focus.SeenChest and ApprovalCheck(Ch_Focus, 500) and not Ch_Focus.Taboo):
                        $ Ch_Focus.Uptop = 1
                        $ Line = get_clothing_name(Ch_Focus.Over_key, vin) if Ch_Focus.Over else get_clothing_name(Ch_Focus.Chest_key, vin)
                        "С голодной ухмылкой, [Ch_Focus.Name] приподнимает [Line] над своей грудью."
                        call Girl_First_Topless(Ch_Focus,1)
                        $ Line = 0
                        "Затем она берет вас за голову и вжимает ваше лицо в свою грудь, явно желая заставить вас приступить к делу."
                else:
                        "[Ch_Focus.Name] берет вас за голову и вжимает ваше лицо в свою грудь, явно желая заставить вас приступить к делу."
            else:
                        "[Ch_Focus.Name] берет вас за голову и вжимает ваше лицо в свою грудь, явно желая заставить вас приступить к делу."
            menu:
                "Что будете делать?"
                "Приступить.":
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 2)
                    "Вы начинаете водить языком по ее соску."
                "Похвалить ее.":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    ch_p "Ммм, [Ch_Focus.Pet], мне нравится."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "Вы начинаете ласкать ее грудь."
                    $ Ch_Focus.Statup("Love", 85, 1)
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    "Вы отводите голову назад."
                    $ Ch_Focus.FaceChange("surprised")
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    ch_p "[Ch_Focus.Pet], давай не будем."
                    if Ch_Focus is JeanX:
                            $ JeanX.Statup("Love", 70, -4)
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] отстраняется."
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 1)
                    $ Ch_Focus.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ Ch_Focus.AddWord(1,"refused","refused")
                    return
            #end auto

    if not Ch_Focus.Forced and Situation != "auto":
        $ Tempmod = 0
        call Top_Off(Ch_Focus)
        if "angry" in Ch_Focus.RecentActions:
            return

    $ Tempmod = 0
    if not Ch_Focus.SuckB:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -25)
            $ Ch_Focus.Statup("Obed", 70, 25)
            $ Ch_Focus.Statup("Inbt", 80, 17)
        else:
            $ Ch_Focus.Statup("Love", 90, 10)
            $ Ch_Focus.Statup("Obed", 70, 10)
            $ Ch_Focus.Statup("Inbt", 80, 15)

    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no suck breasts")
    $ Ch_Focus.AddWord(0,"suck breasts","suck breasts")
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"suck breasts")
    else:
            call ViewShift(Ch_Focus,"breasts",0,"suck breasts")

label Girl_SB_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"suck breasts")
#        call Shift_Focus(Girl)
        $ Ch_Focus.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . .":
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_SB_Cycle
                        "В стиле минета" if Ch_Focus.Pose == "69":
                                    call Girl_BJ_Menu
                                    jump Girl_SB_Cycle

                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                        "Сменить вид":
                                    call ViewShift(Ch_Focus,"menu")
                                    jump Girl_SB_Cycle

                        "Другие варианты":
                                menu:
                                    "Дополнительное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                                $ Ch_Focus.Action -= 1
                                            else:
                                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Сменить основное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                    menu:
                                                        "Вернуться к ласканию руками.":
                                                            if Ch_Focus.Action and MultiAction:
                                                                $ Situation = "pullback"
                                                                call Girl_SB_After
                                                                call Girl_Fondle_Breasts
                                                            else:
                                                                "Когда вы отстраняетесь, [Ch_Focus.Name] прижимает вас обратно."
                                                                call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        "Неважно":
                                                                jump Girl_SB_Cycle
                                            else:
                                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Тройничек (locked)" if not Partner:
                                        pass
                                    "Тройничек" if Partner:
                                        menu:
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе" if Trigger == "lesbian":
                                                        call Les_Change(Ch_Focus)
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Пусть [Partner.Name] займется чем-нибудь другим":
                                                        call Three_Change(Ch_Focus)

                                            "Не бросай свое текущее занятие. . . (locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_SB_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_SB_Cycle
                                            "Неважно":
                                                        jump Girl_SB_Cycle

                                    "Показывать ее ноги" if not ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Вставить анальную пробку" if not Ch_Focus.Plug and "plug" in Ch_Focus.Inventory:
                                            call Insert_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку" if Ch_Focus.Plug:
                                            call Remove_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку (locked)" if "plug" not in Ch_Focus.Inventory:
                                            pass

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_SB_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_SB_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_SB_After
        #End menu (if Line)

        call Shift_Focus(Ch_Focus)
        call Sex_Dialog(Ch_Focus,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Ch_Focus)
                            if "angry" in Ch_Focus.RecentActions:
                                call Girl_Pos_Reset(Ch_Focus)
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_SB_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Doreen can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_SB_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in Ch_Focus.RecentActions:#And Doreen is unsatisfied,
                                    "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                    menu:
                                        "Хотите завершить начатое?"
                                        "Продолжим еще немного.":
                                            $ Line = "Вы возвращаетесь к процессу"
                                        "С меня хватит.":
                                            "Вы заканчиваете веселье."
                                            jump Girl_SB_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.SuckB):
                    $ Ch_Focus.Brows = "sly"
                    if Ch_Focus is RogueX:
                            ch_r "Ты просто не можешь оторваться, да?"
                    elif Ch_Focus is KittyX:
                            if not Player.Male:
                                ch_k "Ты ими довольна?"
                            else:
                                ch_k "Ты ими доволен?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Они прекрасны, верно?"
                    elif Ch_Focus is LauraX:
                            ch_l "Это довольно приятно. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Это довольно приятно. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Похоже, тебе это очень нравится. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Веселишься?"
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе, эм. . . нравится?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Тебе. . . приятно?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Тебе нравится?"
                    elif Ch_Focus is WandaX:
                            ch_w "Ну как?"
        elif Ch_Focus.Lust >= 85:
                    pass
        elif Cnt == (15 + Ch_Focus.SuckB) and Ch_Focus.SEXP >= 15 and not ApprovalCheck(Ch_Focus, 1500):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Я знаю, что тебе весело, но, возможно, нам стоит попробовать что-нибудь другое, [RogueX.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Может быть, мы могли бы попробовать что-нибудь еще, [KittyX.Petname]?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Возможно, мы могли бы попробовать что-то другое, [EmmaX.Petname]?"
                    elif Ch_Focus is LauraX:
                            ch_l "Может, пришло время для чего-нибудь другого, [LauraX.Petname]?"
                    elif Ch_Focus is JeanX:
                            ch_j "Может, пришло время для чего-нибудь другого, [JeanX.Petname]?"
                    elif Ch_Focus is StormX:
                            ch_s "Уверена, тебе сейчас весело, но не могли бы мы попробовать что-нибудь другое?"
                    elif Ch_Focus is JubesX:
                            ch_v "Может, попробуем. . . что-нибудь другое?"
                    elif Ch_Focus is GwenX:
                            ch_g "Может, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Может быть, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Не могли бы мы заняться чем-нибудь другим?"
                    elif Ch_Focus is WandaX:
                            ch_w "Разве мы не можем заняться чем-нибудь другим?"
                    menu:
                        extend ""
                        "Закончить.":
                                "Вы заканчиваете веселье. . ."
                                jump Girl_SB_After
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Girl_SB_After
                        "Не-а, это так весело.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она возмущается, но позволяет вам продолжить."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call Girl_Pos_Reset(Ch_Focus)
                                    "Она кидает на вас сердитый взгляд и отстраняется."
                                    if Ch_Focus is RogueX:
                                            ch_r "Раз ты так ко мне относишься, я не нуждаюсь в твоей \"помощи\"."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Может тебе и весело, но я уже устала."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Возможно, тебе и нравится, но мне уже немного больно."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Раз так, то у меня найдутся дела поинтереснее."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Раз так, то у меня найдутся дела поинтереснее."
                                    elif Ch_Focus is StormX:
                                            ch_s "Что ж, как бы тебе не нравилось, мне нужно сделать перерыв."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Мне ужасно скучно. . ."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Эм. . . перестань."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Тогда, боюсь, мне придется тебя покинуть."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Облом тебе."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Что ж, а -мне- скучно."
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_SB_After
        #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10) #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5) #ch_d "Tic tock, [Ch_Focus.Petname]."

        if Ch_Focus.Lust >= 50 and not Ch_Focus.Uptop and (Ch_Focus.Chest or Ch_Focus.Over):
                $ Ch_Focus.Uptop = 1
                "[Ch_Focus.Name] ухмыляется и сдвигает одежду в сторону."
                call Girl_First_Topless(Ch_Focus)

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done") # "Ok, [Ch_Focus.Petname], breaktime."

label Girl_SB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Girl_Pos_Reset(Ch_Focus)

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.SuckB += 1
    $ Ch_Focus.Action -=1
    $ Ch_Focus.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Ch_Focus.Addictionrate += 1

    if Partner == "Kitty":
        call Partner_Like(Ch_Focus,2,2)
    else:
        call Partner_Like(Ch_Focus,2)

    if Ch_Focus.SuckB == 1:
            $ Ch_Focus.SEXP += 4
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                        if Ch_Focus is RogueX:
                                ch_r "Мне . . . очень понравилось, [RogueX.Petname]."
                        elif Ch_Focus is KittyX:
                                ch_k "Надеюсь, тебе этого было достаточно. . ."
                        elif Ch_Focus is EmmaX:
                                ch_e "Они восхитительны, не правда ли?"
                        elif Ch_Focus is LauraX:
                                ch_l "Это было довольно приятно."
                        elif Ch_Focus is JeanX:
                                ch_j "Ну, это было весело."
                        elif Ch_Focus is StormX:
                                ch_s "Это было очень приятно."
                        elif Ch_Focus is JubesX:
                                ch_v "Это было довольно приятно."
                        elif Ch_Focus is GwenX:
                                ch_g "Ох, это было. . . весело."
                        elif Ch_Focus is BetsyX:
                                ch_b "Это было просто чудесно, [BetsyX.Petname]."
                        elif Ch_Focus is DoreenX:
                                ch_d "Честно говоря, было довольно весело."
                        elif Ch_Focus is WandaX:
                                if not Player.Male:
                                    ch_w "Ты полна энтузиазма."
                                else:
                                    ch_w "Ты полон энтузиазма."
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                        $ Ch_Focus.FaceChange("perplexed", 1)
                        if Ch_Focus is RogueX:
                                ch_r "Тебе понравился их вкус?"
                        elif Ch_Focus is KittyX:
                                ch_k "Тебя все устроило?"
                        elif Ch_Focus is EmmaX:
                                if not Player.Male:
                                    ch_e "Ты достаточно удовлетворена?"
                                else:
                                    ch_e "Ты достаточно удовлетворен?"
                        elif Ch_Focus is LauraX:
                                ch_l "Понравилось?"
                        elif Ch_Focus is JeanX:
                                ch_j "Понравилось?"
                        elif Ch_Focus is StormX:
                                ch_s "Понравилось?"
                        elif Ch_Focus is JubesX:
                                ch_v "Понравилось?"
                        elif Ch_Focus is GwenX:
                                ch_g "Тебе понравилось?"
                        elif Ch_Focus is BetsyX:
                                ch_b "Тебе понравилось?"
                        elif Ch_Focus is DoreenX:
                                ch_d "Тебе было весело?"
                        elif Ch_Focus is WandaX:
                                ch_w "Тебе этого достаточно?"
    $ Tempmod = 0
#    if Situation == "shift":
#        ch_d "Oh? What did you have in mind?"
    call Checkout
    return

# End Suck breasts

# Fondle Thighs start //////////////////////////////////////////

label Girl_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)
                                                                                        # Will she let you fondle her thighs? Modifiers
    if Ch_Focus.FondleT: #You've done it before
        $ Tempmod += 10
    if Ch_Focus.PantsNum() >= 6 or Ch_Focus.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 5
    if Ch_Focus.Lust > 75: #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += Taboo
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 25
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10
    if Ch_Focus in (EmmaX,StormX) and Ch_Focus.Taboo and "public" not in Ch_Focus.History:
        $ Tempmod -= 20

    if "no fondle thighs" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no fondle thighs" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 750, TabM=1) # 75, 90, 105, Taboo -40(105)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ Ch_Focus.FaceChange("sexy")
            $ Ch_Focus.Statup("Obed", 50, 1)
            $ Ch_Focus.Statup("Inbt", 30, 2)
            "Когда вы начинаете ласкать ее бедра, [Ch_Focus.Name] смотрит на вас и улыбается."
            jump Girl_FT_Prep
        else:
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Statup("Obed", 50, -2)
            if Ch_Focus is RogueX:
                    ch_r "Руки прочь, [RogueX.Petname]."
            elif Ch_Focus is KittyX:
                    ch_k "Хихи, держи руки выше пояса, [KittyX.Petname]."
            elif Ch_Focus is EmmaX:
                    ch_e "Возможно, нам стоит держать руки выше, [EmmaX.Petname]."
            elif Ch_Focus is LauraX:
                    if not Player.Male:
                        ch_l "Наверное, нам нужно, чтобы ты держала руки выше талии, [LauraX.Petname]."
                    else:
                        ch_l "Наверное, нам нужно, чтобы ты держал руки выше талии, [LauraX.Petname]."
            elif Ch_Focus is JeanX:
                    ch_j "Держи руки выше талии, [JeanX.Petname]."
            elif Ch_Focus is StormX:
                    ch_s "Возможно, нам стоит держать руки выше, [StormX.Petname]."
            elif Ch_Focus is JubesX:
                    if not Player.Male:
                        ch_v "Наверное, нам нужно, чтобы ты держала руки выше талии, [JubesX.Petname]."
                    else:
                        ch_v "Наверное, нам нужно, чтобы ты держал руки выше талии, [JubesX.Petname]."
            elif Ch_Focus is GwenX:
                    if not Player.Male:
                        ch_g "Наверное, нам нужно, чтобы ты держала руки выше талии, [GwenX.Petname]."
                    else:
                        ch_g "Наверное, нам нужно, чтобы ты держал руки выше талии, [GwenX.Petname]."
            elif Ch_Focus is BetsyX:
                    ch_b "Держи руки -выше- талии, [BetsyX.Petname]."
            elif Ch_Focus is DoreenX:
                    ch_d "Не опускай руки, [DoreenX.Petname]."
            elif Ch_Focus is WandaX:
                    ch_w "Ммм, пока рано, [WandaX.Petname]."
            $ Tempmod = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ Ch_Focus.FaceChange("surprised")
        $ Ch_Focus.Brows = "sad"
        if Ch_Focus.Lust > 60:
            $ Ch_Focus.Statup("Love", 70, -3)
        $ Ch_Focus.Statup("Obed", 90, 1)
        $ Ch_Focus.Statup("Obed", 70, 2)
        "Когда вы отстраняетесь, [Ch_Focus.Name] становится немного грустной."
        jump Girl_FT_Prep
    elif "fondle thighs" in Ch_Focus.RecentActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                call AnyLine(Ch_Focus,"Мммм, опять? Что ж, пожалуй, я не против. . .")
        else:
                call AnyLine(Ch_Focus,"Ммм, снова? Ладно.")
        jump Girl_FT_Prep
    elif "fondle thighs" in Ch_Focus.DailyActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Ах, расслабься. . .",
                    "Нежнее.",
                    "Нежнее. . . нежнее. . .",
                    "Расслабься. . .",
                    "Ммм. . ."])
        else:
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Ах, расслабься. . .",
                    "Тебе все мало?",
                    "У тебя очень мягкие прикосновения.",
                    "Оу, расслабься. . .",
                    "Расслабься. . .",
                    "Давай в этот раз нежнее.",
                    "Расслабься. . .",
                    "Ммм. . ."])
        call AnyLine(Ch_Focus,Line)

    if Approval >= 2:                                                                   #She's into it. . .
        $ Ch_Focus.FaceChange("bemused", 1)
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Inbt", 60, 1)
        if Ch_Focus is RogueX:
                ch_r "Ладно, [RogueX.Petname], можешь начинать."
        elif Ch_Focus is KittyX:
                ch_k "Ладно, [KittyX.Petname], вперед."
        elif Ch_Focus is EmmaX:
                ch_e "Ладно, [EmmaX.Petname], приступай."
        elif Ch_Focus is LauraX:
                ch_l "Конечно, звучит весело."
        elif Ch_Focus is JeanX:
                ch_j "Конечно, звучит весело."
        elif Ch_Focus is StormX:
                ch_s "С удовольствием. . ."
        elif Ch_Focus is JubesX:
                ch_v "Конечно."
        elif Ch_Focus is GwenX:
                ch_g "Конечно."
        elif Ch_Focus is BetsyX:
                ch_b "Понимаю."
        elif Ch_Focus is DoreenX:
                ch_d "Конечно."
        elif Ch_Focus is WandaX:
                ch_w "Конечно."
        $ Ch_Focus.Statup("Love", 90, 1)
        $ Ch_Focus.Statup("Inbt", 50, 3)
        jump Girl_FT_Prep

    else:       #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("angry", 1)
        if "no fondle thighs" in Ch_Focus.RecentActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions and "no fondle thighs" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif "no fondle thighs" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif not Ch_Focus.FondleT:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "[RogueX.Petname], я не уверена, что уже готова. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Не. . . сейчас. . . может быть, в другой раз."
            elif Ch_Focus is EmmaX:
                    ch_e "Руки прочь."
            elif Ch_Focus is LauraX:
                    ch_l "Звучит слишком настойчиво, [LauraX.Petname]."
            elif Ch_Focus is JeanX:
                    ch_j "Можешь смотреть, но не трогать, [JeanX.Petname]."
            elif Ch_Focus is StormX:
                    if not Player.Male:
                        ch_s "Я бы предпочла, чтобы ты этого не делала, [StormX.Petname]."
                    else:
                        ch_s "Я бы предпочла, чтобы ты этого не делал, [StormX.Petname]."
            elif Ch_Focus is JubesX:
                    ch_v "Ты слишком спешишь, [JubesX.Petname]."
            elif Ch_Focus is GwenX:
                    ch_g "Что-, эм. . . нет, спасибо."
            elif Ch_Focus is BetsyX:
                    ch_b "Это меня не интересует."
            elif Ch_Focus is DoreenX:
                    ch_d "Это немного. . . странно."
            elif Ch_Focus is WandaX:
                    ch_w "Ты сейчас серьезно? Я как-то не уверена. . ."
        else:
            $ Ch_Focus.FaceChange("bemused")
            call Sex_Basic_Dialog(Ch_Focus,"nothanks")
        menu:
            extend ""
            "Извини, забудь." if "no fondle thighs" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"noproblem")  # ch_r "Ok, no problem, [RogueX.Petname]."
                return
            "Может, в другой раз?" if "no fondle thighs" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy")
                call Sex_Basic_Dialog(Ch_Focus,"maybe")  # ch_d "I'll think about it, [Ch_Focus.Petname]."
                $ Ch_Focus.Statup("Love", 80, 1)
                $ Ch_Focus.Statup("Inbt", 30, 2)
                if Taboo:
                    $ Ch_Focus.RecentActions.append("tabno")
                    $ Ch_Focus.DailyActions.append("tabno")
                $ Ch_Focus.RecentActions.append("no fondle thighs")
                $ Ch_Focus.DailyActions.append("no fondle thighs")
                return
            "Ну давай, пожалуйста?":
                if Approval:
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 60, 1)
                    $ Ch_Focus.Statup("Obed", 30, 2)
                    $ Ch_Focus.Statup("Inbt", 50, 1)
                    $ Ch_Focus.Statup("Inbt", 30, 2)
                    call Sex_Basic_Dialog(Ch_Focus,"pleaseyes")  # ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
                    jump Girl_FT_Prep
                else:
                    $ Ch_Focus.FaceChange("angry")
                    call Sex_Basic_Dialog(Ch_Focus,"pleaseno") #ch_r "I'm afraid not this time, sorry [RogueX.Petname]."

            "[[Все равно начать ласкать ее бедра]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(Ch_Focus, 350, "OI", TabM = 2) # 35, 50, 65, -80(105)
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -5, 1)
                    $ Ch_Focus.Statup("Love", 20, -2, 1)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #ch_w "Whoa!" ch_w ". . ." ch_w "Ok, ok, just get to it. . ."
                    $ Ch_Focus.Statup("Obed", 50, 3)
                    $ Ch_Focus.Statup("Inbt", 60, 2)
                    if Approval < 2:
                        $ Ch_Focus.Forced = 1
                    jump Girl_FT_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -8)
                    $ Ch_Focus.FaceChange("angry", 1)
                    $ Line = renpy.random.choice(["Что?",
                        "Эй!",
                        "М?",
                        "Воу!",
                        "Прошу прощения?",
                        "Хм."])
                    call AnyLine(Ch_Focus,Line)
                    "Она шлепает вас по руке."
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    if "no fondle thighs" in Ch_Focus.DailyActions:
        call Sex_Basic_Dialog(Ch_Focus,"noday") #"Stop asking."
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("sad", 1)
        if Ch_Focus is RogueX:
                ch_r "Не так быстро."
        elif Ch_Focus is KittyX:
                ch_k "Даже не думай."
        elif Ch_Focus is EmmaX:
                ch_e "Не искушай судьбу."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Ты заходишь слишком далеко."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Эм, нет, спасибо. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, я не могу. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Просто мне немного неудобно. . ."
        elif Ch_Focus is WandaX:
                ch_w "Мне не особо нравится подобное. . ."
        $ Ch_Focus.Statup("Lust", 50, 2)
        $ Ch_Focus.Statup("Obed", 50, -1)
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Taboo:
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.RecentActions.append("tabno")
        $ Ch_Focus.DailyActions.append("tabno")
        call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You picked a bad place for this. . ."
    elif Ch_Focus.FondleT:
        $ Ch_Focus.FaceChange("sad")
        if Ch_Focus is RogueX:
                if not Player.Male:
                    ch_r "Нахалка!"
                else:
                    ch_r "Наглец!"
        elif Ch_Focus is KittyX:
                ch_k "Даже не думай."
        elif Ch_Focus is EmmaX:
                ch_e "Руки прочь."
        elif Ch_Focus is LauraX:
                ch_l "Держи руки при себе."
        elif Ch_Focus is JeanX:
                ch_j "Держи руки при себе."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Держи руки при себе."
        elif Ch_Focus is GwenX:
                ch_g "Эм, нет. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, что нет. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Я так не думаю. . ."
        elif Ch_Focus is WandaX:
                ch_w "Я так не думаю. . ."
    else:
        $ Ch_Focus.FaceChange("sexy")
        $ Ch_Focus.Mouth = "sad"
        if Ch_Focus is RogueX:
                ch_r "Не судьба, [RogueX.Petname]."
        elif Ch_Focus is KittyX:
                ch_k "Нееее-а."
        elif Ch_Focus is EmmaX:
                ch_e "Нет."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Не-а."
        elif Ch_Focus is BetsyX:
                ch_b "Благодарю, но нет."
        elif Ch_Focus is DoreenX:
                ch_d "Ох, нет, спасибо."
        elif Ch_Focus is WandaX:
                ch_w "Нет."
    $ Ch_Focus.RecentActions.append("no fondle thighs")
    $ Ch_Focus.DailyActions.append("no fondle thighs")
    $ Tempmod = 0
    return

label Girl_FT_Prep:                                                                 #Animation set-up
    if Trigger == "kiss you":
        $ Trigger = "fondle thighs"
        return

    if Trigger2 == "fondle thighs":
        return

    if not Ch_Focus.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(Ch_Focus)
        if "angry" in Ch_Focus.RecentActions:
            return

    $ Tempmod = 0
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle thighs")
    else:
            call ViewShift(Ch_Focus,"mid",0,"fondle thighs")
    if not Ch_Focus.FondleT:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -10)
            $ Ch_Focus.Statup("Obed", 70, 15)
            $ Ch_Focus.Statup("Inbt", 80, 10)
        else:
            $ Ch_Focus.Statup("Love", 90, 5)
            $ Ch_Focus.Statup("Obed", 70, 10)
            $ Ch_Focus.Statup("Inbt", 80, 15)

    if Ch_Focus.Taboo:
        $ Ch_Focus.Statup("Lust", 200, (int(Taboo/5)))
        $ Ch_Focus.Statup("Inbt", 200, (2*(int(Taboo/5))))

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no fondle thighs")
    $ Ch_Focus.AddWord(0,"fondle thighs","fondle thighs")
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle thighs")
    else:
            call ViewShift(Ch_Focus,"mid",0,"fondle thighs")

label Girl_FT_Cycle:                                                                #Repeating strokes
    while Round > 0:
        call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle thighs")
#        call Shift_Focus(Girl)
        $ Ch_Focus.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . .":
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_FT_Cycle
                        "В стиле минета" if Ch_Focus.Pose == "69":
                                    call Girl_BJ_Menu
                                    jump Girl_FT_Cycle

                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                        "Сменить вид":
                                    call ViewShift(Ch_Focus,"menu")
                                    jump Girl_FT_Cycle

                        "Другие варианты":
                                menu:
                                    "Дополнительное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ Ch_Focus.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Сменить основное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                    menu:
                                                        "Могу я подняться выше?":
                                                                if Ch_Focus.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Girl_FT_After
                                                                    call Girl_Fondle_Pussy
                                                                else:
                                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        "Сдвинуть руки немного выше, не спрашивая":
                                                                if Ch_Focus.Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call Girl_FT_After
                                                                    call Girl_Fondle_Pussy
                                                                else:
                                                                    "Когда ваши руки начинают поднимаются вверх, она хватает вас за запястья."
                                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        "Неважно":
                                                                jump Girl_FT_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Переключить свое внимание" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Girl_FT_After
                                                call Offhand_Set
                                    "Переключить свое внимание (locked)" if not Trigger2:
                                                pass

                                    "Тройничек (locked)" if not Partner:
                                        pass
                                    "Тройничек" if Partner:
                                        menu:
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе" if Trigger == "lesbian":
                                                        call Les_Change(Ch_Focus)
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Пусть [Partner.Name] займется чем-нибудь другим":
                                                        call Three_Change(Ch_Focus)

                                            "Не бросай свое текущее занятие. . . (locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_FT_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_FT_Cycle
                                            "Неважно":
                                                        jump Girl_FT_Cycle

                                    "Показывать ее ноги" if not ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Вставить анальную пробку" if not Ch_Focus.Plug and "plug" in Ch_Focus.Inventory:
                                            call Insert_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку" if Ch_Focus.Plug:
                                            call Remove_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку (locked)" if "plug" not in Ch_Focus.Inventory:
                                            pass

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_FT_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_FT_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_FT_After
        #End menu (if Line)

#        call Shift_Focus(Girl)
        call Sex_Dialog(Ch_Focus,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Ch_Focus)
                            if "angry" in Ch_Focus.RecentActions:
                                call Girl_Pos_Reset(Ch_Focus)
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2 and Ch_Focus.SEXP >= 20:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_FT_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Doreen can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_FT_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in Ch_Focus.RecentActions and Ch_Focus.SEXP >= 20:#And Doreen is unsatisfied,
                                    "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                    menu:
                                        "Хотите завершить начатое?"
                                        "Продолжим еще немного.":
                                            $ Line = "Вы возвращаетесь к процессу"
                                        "С меня хватит.":
                                            "Вы заканчиваете веселье."
                                            jump Girl_FT_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.FondleT):
                    $ Ch_Focus.FaceChange("smile", 1)
                    if Ch_Focus is RogueX:
                            ch_r "Тебе нравится, да?"
                    elif Ch_Focus is KittyX:
                            ch_k "Тебе нравится, да?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Роскошные, да?"
                    elif Ch_Focus is LauraX:
                            ch_l "Довольно приятно, но. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Довольно приятно, но. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Твои руки такие теплые. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Ладно, но, эм. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Ох, эм. . . тебе весело?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Довольно упругие, не так ли?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Разве они не мягкие?"
                    elif Ch_Focus is WandaX:
                            ch_w "Тебе нравится?"
        elif Cnt == (15 + Ch_Focus.FondleT) and Ch_Focus.SEXP >= 15 and not ApprovalCheck(Ch_Focus, 1500):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Я знаю, что тебе весело, но, возможно, нам стоит попробовать что-нибудь другое, [RogueX.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Может быть, мы могли бы попробовать что-нибудь еще, [KittyX.Petname]?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Возможно, мы могли бы попробовать что-то другое, [EmmaX.Petname]?"
                    elif Ch_Focus is LauraX:
                            ch_l "Может, пришло время для чего-нибудь другого, [LauraX.Petname]?"
                    elif Ch_Focus is JeanX:
                            ch_j "Может, пришло время для чего-нибудь другого, [JeanX.Petname]?"
                    elif Ch_Focus is StormX:
                            ch_s "Уверена, тебе сейчас весело, но не могли бы мы попробовать что-нибудь другое?"
                    elif Ch_Focus is JubesX:
                            ch_v "Может, попробуем. . . что-нибудь другое?"
                    elif Ch_Focus is GwenX:
                            ch_g "Может, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Может быть, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Не могли бы мы заняться чем-нибудь другим?"
                    elif Ch_Focus is WandaX:
                            ch_w "Разве мы не можем заняться чем-нибудь другим?"
                    menu:
                        extend ""
                        "Закончить.":
                                "Вы заканчиваете веселье. . ."
                                jump Girl_FT_After
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Girl_FT_After
                        "Не-а, это так весело.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она возмущается, но позволяет вам продолжить."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call Girl_Pos_Reset(Ch_Focus)
                                    "Она кидает на вас сердитый взгляд и отстраняется."
                                    if Ch_Focus is DoreenX:
                                            ch_d "Тогда давай без меня."
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_FT_After
        #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10) #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5) #ch_d "Tic tock, [Ch_Focus.Petname]."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done") # "Ok, [Ch_Focus.Petname], breaktime."


label Girl_FT_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Girl_Pos_Reset(Ch_Focus)

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.FondleT += 1
    $ Ch_Focus.Action -=1
    if Ch_Focus.PantsNum() < 6 or Ch_Focus.Upskirt:
        $ Ch_Focus.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ Ch_Focus.Addictionrate += 1

    if Partner == "Kitty":
        call Partner_Like(Ch_Focus,2)
    else:
        call Partner_Like(Ch_Focus,1)

    if Ch_Focus.FondleT == 1:
            $ Ch_Focus.SEXP += 3
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                    if Ch_Focus is RogueX:
                            ch_r "Это было. . . приятно."
                    elif Ch_Focus is KittyX:
                            ch_k "Мне понравилось."
                    elif Ch_Focus is EmmaX:
                            ch_e "Это было. . . очень приятно."
                    elif Ch_Focus is LauraX:
                            ch_l "Это. . . было интересно."
                    elif Ch_Focus is JeanX:
                            ch_j "Ну, это было. . . удивительно."
                    elif Ch_Focus is StormX:
                            ch_s "Благодарю тебя за это."
                    elif Ch_Focus is JubesX:
                            ch_v "Это. . . было интересно."
                    elif Ch_Focus is GwenX:
                            ch_g "Ладно. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Это было прекрасно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Это было здорово. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Это было весело и все такое. . ."

                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                    $ Ch_Focus.FaceChange("perplexed", 1)
                    if Ch_Focus is RogueX:
                            ch_r "Этого тебе достаточно?"
                    elif Ch_Focus is KittyX:
                            ch_k "Этого достаточно?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Этого достаточно?"
                    elif Ch_Focus is LauraX:
                            ch_l "Этого достаточно?"
                    elif Ch_Focus is JeanX:
                            ch_j "Этого достаточно?"
                    elif Ch_Focus is StormX:
                            ch_s "Ладно, все было хорошо?"
                    elif Ch_Focus is JubesX:
                            ch_v "Этого достаточно?"
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе понравилось?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Тебе этого достаточно?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Тебе этого достаточно?"
                    elif Ch_Focus is WandaX:
                            ch_w "Тебе этого достаточно?"
    $ Tempmod = 0
#    if Situation == "shift":
#        ch_d "Oh? What did you have in mind?"
    call Checkout
    return

# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy
label Girl_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)
                                                                                        # Will she let you fondle? Modifiers
    if Ch_Focus.FondleP: #You've done it before
        $ Tempmod += 20
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 4
    if Ch_Focus.PantsNum() >= 6 or Ch_Focus.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 10
    if Ch_Focus.Lust > 75: #She's really horny
        $ Tempmod += 15
    if Ch_Focus.Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (2*Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 25
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10
    if Ch_Focus in (EmmaX,StormX) and Ch_Focus.Taboo and "public" not in Ch_Focus.History:
        $ Tempmod -= 20

    if "no fondle pussy" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no fondle pussy" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ Ch_Focus.FaceChange("sexy")
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Obed", 70, 2)
            $ Ch_Focus.Statup("Inbt", 70, 3)
            $ Ch_Focus.Statup("Inbt", 30, 2)
            "Когда ваша рука начинает подниматься по ее бедру, [Ch_Focus.Name] слегка удивляется, но затем кивает."
            jump Girl_FP_Prep
        else:
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Statup("Obed", 50, -2)
            if Ch_Focus is RogueX:
                    if not Player.Male:
                        ch_r "Слушай, просто продолжай то, что делала, [RogueX.Petname]."
                    else:
                        ch_r "Слушай, просто продолжай то, что делал, [RogueX.Petname]."
            elif Ch_Focus is KittyX:
                    if not Player.Male:
                        ch_k "Не-а, [KittyX.Petname], вернись к тому, что делала ранее."
                    else:
                        ch_k "Не-а, [KittyX.Petname], вернись к тому, что делал ранее."
            elif Ch_Focus is EmmaX:
                    if not Player.Male:
                        ch_e "Полегче, ты так хорошо справлялась. . ."
                    else:
                        ch_e "Полегче, ты так хорошо справлялся. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Давай вернемся назад, [LauraX.Petname]. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Не так быстро, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Возможно, тебе стоит проявить немного самоконтроля. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Сбавь обороты, [JubesX.Petname]. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Эм. . . тебе стоит убрать руку, [GwenX.Petname]. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Мне кажется, ты заходишь слишком далеко, [BetsyX.Petname]. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Воу, нет, спасибо. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Эй-эй, оставь это на потом, [WandaX.Petname]. . ."
            $ Tempmod = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ Ch_Focus.FaceChange("surprised")
        $ Ch_Focus.Brows = "sad"
        if Ch_Focus.Lust > 80:
            $ Ch_Focus.Statup("Love", 70, -4)
        $ Ch_Focus.Statup("Obed", 90, 1)
        $ Ch_Focus.Statup("Obed", 70, 2)
        "Когда вы отстраняетесь, [Ch_Focus.Name] растроенно вздыхает."
        jump Girl_FP_Prep
    elif "fondle pussy" in Ch_Focus.RecentActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                call AnyLine(Ch_Focus,"Мммм, опять? Что ж, пожалуй, я не против. . .")
        else:
                call AnyLine(Ch_Focus,"Снова? Ну ладно.")
        jump Girl_FP_Prep
    elif "fondle pussy" in Ch_Focus.DailyActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Тебе следует расслабиться. . .",
                    "Полегче.",
                    "Нежнее. . . нежнее. . .",
                    "Расслабься. . .",
                    "Ммм. . ."])
        else:
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Тебе следует расслабиться. . .",
                    "Тебе все мало?",
                    "Полегче.",
                    "Ах, расслабься. . .",
                    "Расслабься. . .",
                    "Не торопись, я еще не отошла от прошлого раза.",
                    "Расслабься. . .",
                    "Ммм. . ."])
        call AnyLine(Ch_Focus,Line)

    if Approval >= 2:                                                                   #She's into it. . .
        $ Ch_Focus.FaceChange("bemused", 2)
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Inbt", 60, 1)
        if Ch_Focus is RogueX:
                ch_r "Конечно, давай."
        elif Ch_Focus is KittyX:
                ch_k "Ладно, как скажешь."
        elif Ch_Focus is EmmaX:
                ch_e "Ммм, я не могу отказаться. . ."
        elif Ch_Focus is LauraX:
                ch_l "Конечно, звучит весело."
        elif Ch_Focus is JeanX:
                ch_j "Конечно, звучит весело."
        elif Ch_Focus is StormX:
                ch_s "С удовольствием. . ."
        elif Ch_Focus is JubesX:
                ch_v "Конечно, звучит весело."
        elif Ch_Focus is GwenX:
                ch_g "Конечно, звучит весело."
        elif Ch_Focus is BetsyX:
                ch_b "Мммм, я только за. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Конечно."
        elif Ch_Focus is WandaX:
                ch_w "Конечно."
        $ Ch_Focus.FaceChange("bemused", 1)
        $ Ch_Focus.Statup("Love", 90, 1)
        $ Ch_Focus.Statup("Inbt", 50, 3)
        jump Girl_FP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("angry", 1)
        if "no fondle pussy" in Ch_Focus.RecentActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions and "no fondle pussy" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif "no fondle pussy" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif not Ch_Focus.FondleP:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "Эм, только не там, [RogueX.Petname]. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Эм, только не там, [KittyX.Petname]. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Полагаю, ты немного спешишь, [EmmaX.Petname]. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Думаю, ты немного спешишь, [LauraX.Petname]. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Ты немного спешишь, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Не так быстро, [StormX.Petname]. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Думаю, ты немного спешишь, [JubesX.Petname]. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Ох, ты хочешь. . . нет, спасибо. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Ох, ты хочешь. . . благодарю, но нет. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Ох, ты хочешь. . . нет, спасибо. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Ты правла решился на это? . ."
        else:
            $ Ch_Focus.FaceChange("bemused")
            call Sex_Basic_Dialog(Ch_Focus,"nothanks")
        menu:
            extend ""
            "Извини, забудь." if "no fondle pussy" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"noproblem")  # ch_r "Ok, no problem, [RogueX.Petname]."
                return
            "Может, в другой раз?" if "no fondle pussy" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy")
                call Sex_Basic_Dialog(Ch_Focus,"maybe")  # ch_d "I'll think about it, [Ch_Focus.Petname]."
                $ Ch_Focus.Statup("Love", 80, 2)
                $ Ch_Focus.Statup("Inbt", 70, 2)
                if Taboo:
                    $ Ch_Focus.RecentActions.append("tabno")
                    $ Ch_Focus.DailyActions.append("tabno")
                $ Ch_Focus.RecentActions.append("no fondle pussy")
                $ Ch_Focus.DailyActions.append("no fondle pussy")
                return
            "Ну давай, пожалуйста?":
                if Approval:
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 90, 2)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                    $ Ch_Focus.Statup("Inbt", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 40, 2)
                    call Sex_Basic_Dialog(Ch_Focus,"pleaseyes")  # ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
                    jump Girl_FP_Prep
                else:
                    $ Ch_Focus.FaceChange("angry")
                    call Sex_Basic_Dialog(Ch_Focus,"pleaseno") #ch_r "I'm afraid not this time, sorry [RogueX.Petname]."

            "[[Все равно начать ласкать]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(Ch_Focus, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -5, 1)
                    $ Ch_Focus.Statup("Love", 200, -2)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #ch_w "Whoa!" ch_w ". . ." ch_w "Ok, ok, just get to it. . ."
                    $ Ch_Focus.Statup("Obed", 50, 4)
                    $ Ch_Focus.Statup("Inbt", 80, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ Ch_Focus.Forced = 1
                    jump Girl_FP_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -15)
                    $ Ch_Focus.FaceChange("angry", 1)
                    $ Line = renpy.random.choice(["Что?",
                        "Эй!",
                        "М?",
                        "Воу!",
                        "Прошу прощения?",
                        "Хм."])
                    call AnyLine(Ch_Focus,Line)
                    "Она шлепает вас по руке."
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    if "no fondle pussy" in Ch_Focus.DailyActions:
        call Sex_Basic_Dialog(Ch_Focus,"noday") #"Stop asking."
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("angry", 1)
        if Ch_Focus is RogueX:
                ch_r "Держись подальше от моих трусиков, [RogueX.Petname]."
        elif Ch_Focus is KittyX:
                ch_k "Держись подальше от моей \"китти\", [KittyX.Petname]."
        elif Ch_Focus is EmmaX:
                ch_e "Не искушай судьбу."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Ты заходишь слишком далеко."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Эм, нет, спасибо. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, я не могу. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Это слишком для меня. . ."
        elif Ch_Focus is WandaX:
                ch_w "Это не по мне."
        $ Ch_Focus.Statup("Lust", 70, 5)
        $ Ch_Focus.Statup("Obed", 50, -2)
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Taboo:
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.RecentActions.append("tabno")
        $ Ch_Focus.DailyActions.append("tabno")
        call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You picked a bad place for this. . ."
    elif Ch_Focus.FondleP:
        $ Ch_Focus.FaceChange("sad")
        if Ch_Focus is RogueX:
                ch_r "Прости, но держи свои руки подальше."
        elif Ch_Focus is KittyX:
                ch_k "Извини, но держи свои руки подальше."
        elif Ch_Focus is EmmaX:
                ch_e "Прости, но держи свои руки подальше."
        elif Ch_Focus is LauraX:
                ch_l "Извини, но держи пальцы снаружи."
        elif Ch_Focus is JeanX:
                ch_j "Тебе стоит держать руки при себе."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Извини, но держи пальцы снаружи."
        elif Ch_Focus is GwenX:
                ch_g "Я, эм. . . больше не хочу."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, корабль уже ушел."
        elif Ch_Focus is DoreenX:
                ch_d "Мне кажется, лучше рассмотреть другие варианты."
        elif Ch_Focus is WandaX:
                ch_w "Думаю, я прекрасно могу сама о себе позаботиться."
    else:
        $ Ch_Focus.FaceChange("sexy")
        $ Ch_Focus.Mouth = "sad"
        if Ch_Focus is RogueX:
                ch_r "Не судьба, [RogueX.Petname]."
        elif Ch_Focus is KittyX:
                ch_k "Не судьба [KittyX.Petname]."
        elif Ch_Focus is EmmaX:
                ch_e "Нет, благодарю, [EmmaX.Petname]."
        elif Ch_Focus is LauraX:
                ch_l "Нет, спасибо, [LauraX.Petname]."
        elif Ch_Focus is JeanX:
                ch_j "Нет, спасибо, [JeanX.Petname]."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Нет, спасибо, [JubesX.Petname]."
        elif Ch_Focus is GwenX:
                ch_g "Эм, нет, спасибо."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, я не могу."
        elif Ch_Focus is DoreenX:
                ch_d "Это слишком. . . интимно."
        elif Ch_Focus is WandaX:
                ch_w "Нет."
    $ Ch_Focus.RecentActions.append("no fondle pussy")
    $ Ch_Focus.DailyActions.append("no fondle pussy")
    $ Tempmod = 0
    return

label Girl_FP_Prep: #Animation set-up
    if Trigger2 == "fondle pussy":
        return

    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle pussy")
    else:
            call ViewShift(Ch_Focus,"pussy",0,"fondle pussy")

    if Situation == Ch_Focus:
            #Doreen auto-starts
            $ Situation = 0
            if (Ch_Focus.Legs and not Ch_Focus.Upskirt) or (Ch_Focus.Panties and not Ch_Focus.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(Ch_Focus, 1250, TabM = 1) or (Ch_Focus.SeenPussy and ApprovalCheck(Ch_Focus, 500) and not Taboo):
                        $ Ch_Focus.Upskirt = 1
                        $ Ch_Focus.PantiesDown = 1
                        $ Line = 0
                        if Ch_Focus.PantsNum() == 5:
                            $ Line = Ch_Focus.Name + " задирает свою юбку"
                        elif Ch_Focus.PantsNum() >= 6:
                            $ Line = Ch_Focus.Name + " стягивает с себя " + get_clothing_name(Ch_Focus.Legs_key, vin)
                        else:
                            $ Line = "Она наклоняется "
                        if Ch_Focus.Panties:
                            #wearing pants
                            "[Line] и сдвигает свои [get_clothing_name(Ch_Focus.Panties_key, vin)] в сторону."
                            "Она берет вас за руку и кладет вашу ладонь себе между ног, явно желая, чтобы вы взялись за дело."
                        else:
                            #pants but no panties
                            "[Line], а затем кладет вашу ладонь себе между ног."
                            "Она явно хочет, чтобы вы взялись за дело."
                        call Girl_First_Bottomless(Ch_Focus,1)
                else:
                        "[Ch_Focus.Name] берет вас за руку и кладет вашу ладонь себе между ног, явно желая, чтобы вы взялись за дело."
            else:
                        "[Ch_Focus.Name] берет вас за руку и кладет вашу ладонь себе между ног, явно желая, чтобы вы взялись за дело."
            menu:
                "Что будете делать?"
                "Приступить.":
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 2)
                    "Вы начинаете водить пальцами по ее киске."
                "Похвалить ее.":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    ch_p "[Ch_Focus.Pet], мне нравится твоя инициатива."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "Вы начинаете водить пальцами по ее киске."
                    $ Ch_Focus.Statup("Love", 85, 1)
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    "Вы одергиваете руку."
                    $ Ch_Focus.FaceChange("surprised")
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    ch_p "[Ch_Focus.Pet], давай не будем."
                    if Ch_Focus is JeanX:
                            $ JeanX.Statup("Love", 70, -4)
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] отстраняется."
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 1)
                    $ Ch_Focus.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ Ch_Focus.AddWord(1,"refused","refused")
                    return
            #end auto

    if not Ch_Focus.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(Ch_Focus)
        if "angry" in Ch_Focus.RecentActions:
            return
    $ Tempmod = 0

    if not Ch_Focus.FondleP:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -50)
            $ Ch_Focus.Statup("Obed", 70, 35)
            $ Ch_Focus.Statup("Inbt", 80, 25)
        else:
            $ Ch_Focus.Statup("Love", 90, 10)
            $ Ch_Focus.Statup("Obed", 70, 10)
            $ Ch_Focus.Statup("Inbt", 80, 15)
    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no fondle pussy")
    $ Ch_Focus.AddWord(0,"fondle pussy","fondle pussy")
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle pussy")
    else:
            call ViewShift(Ch_Focus,"pussy",0,"fondle pussy")
    $ Speed = 1

label Girl_FP_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle pussy")
#        call Shift_Focus(Girl)
        $ Ch_Focus.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . .":
                                    pass

                        "Я хочу вставить палец внутрь. . ." if Speed != 2:
                                if Ch_Focus.InsertP:
                                    $ Speed = 2
                                else:
                                    menu:
                                        "Сначала спросить":
                                            $ Situation = "shift"
                                        "Не спрашивать [[просто вставить]":
                                            $ Situation = "auto"
                                    call Girl_Insert_Pussy

                        "Немного притормозить. . ." if Speed == 2:
                                    $ Speed = 0

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_FP_Cycle
                        "В стиле минета" if Ch_Focus.Pose == "69":
                                    call Girl_BJ_Menu
                                    jump Girl_FP_Cycle

                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                        "Сменить вид":
                                    call ViewShift(Ch_Focus,"menu")
                                    jump Girl_FP_Cycle

                        "Другие варианты":
                                menu:
                                    "Дополнительное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ Ch_Focus.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Сменить основное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                    menu:
                                                        "Я хочу вылизать твою киску.":
                                                                $ Situation = "shift"
                                                                call Girl_FP_After
                                                                call Girl_Lick_Pussy
                                                        "Просто начать вылизывать":
                                                                $ Situation = "auto"
                                                                call Girl_FP_After
                                                                call Girl_Lick_Pussy
                                                        "Потянуться обратно к бедрам":
                                                                $ Situation = "pullback"
                                                                call Girl_FP_After
                                                                call Girl_Fondle_Thighs
                                                        "Я хочу вставить туда фаллоимитатор.":
                                                                $ Situation = "shift"
                                                                call Girl_FP_After
                                                                call Girl_Dildo("pussy") #call Girl_Dildo_Pussy
                                                                if "no dildo" not in Ch_Focus.RecentActions: #if she refuses, continue on, otherwise, skip back to previous label
                                                                        return
                                                        "Неважно":
                                                                jump Girl_FP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Переключить свое внимание" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Girl_FP_After
                                                call Offhand_Set
                                    "Переключить свое внимание (locked)" if not Trigger2:
                                                pass

                                    "Тройничек (locked)" if not Partner:
                                        pass
                                    "Тройничек" if Partner:
                                        menu:
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе" if Trigger == "lesbian":
                                                        call Les_Change(Ch_Focus)
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Пусть [Partner.Name] займется чем-нибудь другим":
                                                        call Three_Change(Ch_Focus)

                                            "Не бросай свое текущее занятие. . . (locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_FP_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_FP_Cycle
                                            "Неважно":
                                                        jump Girl_FP_Cycle

                                    "Показывать ее ноги" if not ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Вставить анальную пробку" if not Ch_Focus.Plug and "plug" in Ch_Focus.Inventory:
                                            call Insert_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку" if Ch_Focus.Plug:
                                            call Remove_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку (locked)" if "plug" not in Ch_Focus.Inventory:
                                            pass

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_FP_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_FP_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_FP_After
        #End menu (if Line)

#        call Shift_Focus(Girl)
        call Sex_Dialog(Ch_Focus,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Ch_Focus)
                            if "angry" in Ch_Focus.RecentActions:
                                call Girl_Pos_Reset(Ch_Focus)
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_FP_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Doreen can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_FP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in Ch_Focus.RecentActions:#And Doreen is unsatisfied,
                                    "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                    menu:
                                        "Хотите завершить начатое?"
                                        "Продолжим еще немного.":
                                            $ Line = "Вы возвращаетесь к процессу"
                                        "С меня хватит.":
                                            "Вы заканчиваете веселье."
                                            jump Girl_FP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.FondleP):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Как ощущения?"
                    elif Ch_Focus is KittyX:
                            ch_k "Как ощущения?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Как ощущения?"
                    elif Ch_Focus is LauraX:
                            ch_l "Мммм, тебе нравится, да?"
                    elif Ch_Focus is JeanX:
                            ch_j "Мммм, тебе нравится, да?"
                    elif Ch_Focus is StormX:
                            ch_s "Мммм, да. . . глубже. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Веселишься?"
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе, эм. . . нравится?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Тебе приятно?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Тебе, эм, похоже, очень нравится. . ."
                    elif Ch_Focus is WandaX:
                            if not Player.Male:
                                ch_w "Ты и правда решилась на это. . ."
                            else:
                                ch_w "Ты и правда решился на это. . ."
        elif Ch_Focus.Lust >= 80:
                    pass
        elif Cnt == (15 + Ch_Focus.FondleP) and Ch_Focus.SEXP >= 15 and not ApprovalCheck(Ch_Focus, 1500):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Я знаю, что тебе весело, но, возможно, нам стоит попробовать что-нибудь другое, [RogueX.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Может быть, мы могли бы попробовать что-нибудь еще, [KittyX.Petname]?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Возможно, мы могли бы попробовать что-то другое, [EmmaX.Petname]?"
                    elif Ch_Focus is LauraX:
                            ch_l "Может, пришло время для чего-нибудь другого, [LauraX.Petname]?"
                    elif Ch_Focus is JeanX:
                            ch_j "Может, пришло время для чего-нибудь другого, [JeanX.Petname]?"
                    elif Ch_Focus is StormX:
                            ch_s "Уверена, тебе сейчас весело, но не могли бы мы попробовать что-нибудь другое?"
                    elif Ch_Focus is JubesX:
                            ch_v "Может, попробуем. . . что-нибудь другое?"
                    elif Ch_Focus is GwenX:
                            ch_g "Может, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Может быть, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Не могли бы мы заняться чем-нибудь другим?"
                    elif Ch_Focus is WandaX:
                            ch_w "Разве мы не можем заняться чем-нибудь другим?"
                    menu:
                        extend ""
                        "Закончить.":
                                "Вы заканчиваете веселье. . ."
                                jump Girl_FP_After
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Girl_FP_After
                        "Не-а, это так весело.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она возмущается, но позволяет вам продолжить."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call Girl_Pos_Reset(Ch_Focus)
                                    "Она кидает на вас сердитый взгляд и отстраняется."
                                    if Ch_Focus is RogueX:
                                            ch_r "Раз ты так ко мне относишься, я не нуждаюсь в твоей \"помощи\"."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Может тебе и весело, но я уже устала."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Возможно, тебе и нравится, но мне уже немного больно."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Раз так, то у меня найдутся дела поинтереснее."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Раз так, то у меня найдутся дела поинтереснее."
                                    elif Ch_Focus is StormX:
                                            ch_s "Что ж, как бы тебе не нравилось, мне нужно сделать перерыв."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Мне ужасно скучно. . ."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Эм. . . перестань."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Тогда, боюсь, мне придется тебя покинуть."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Облом тебе."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Что ж, а -мне- скучно."
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_FP_After
        #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10) #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5) #ch_d "Tic tock, [Ch_Focus.Petname]."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done") # "Ok, [Ch_Focus.Petname], breaktime."


label Girl_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Girl_Pos_Reset(Ch_Focus)

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.FondleP += 1
    $ Ch_Focus.Action -=1
    if Ch_Focus.PantsNum() < 6 or Ch_Focus.Upskirt:
        $ Ch_Focus.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ Ch_Focus.Addictionrate += 1

    call Partner_Like(Ch_Focus,2)

    if Ch_Focus.FondleP == 1:
            $ Ch_Focus.SEXP += 7
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                        if Ch_Focus is RogueX:
                                ch_r "Когда ласкаю себя не я, совсем другие ощущения."
                        elif Ch_Focus is KittyX:
                                ch_k "Твоей рукой. . . лучше, чем моей."
                        elif Ch_Focus is EmmaX:
                                ch_e "Я ценю. . . твой напор."
                        elif Ch_Focus is LauraX:
                                ch_l "Твои руки в самом деле знают, что делать."
                        elif Ch_Focus is JeanX:
                                ch_j "Ну, это был приятный сюрприз. . ."
                        elif Ch_Focus is StormX:
                                if not Player.Male:
                                    ch_s "Ты определенно. . . достигла пары интересных мест. . ."
                                else:
                                    ch_s "Ты определенно. . . достиг пары интересных мест. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Ого. . . это было здорово. . ."
                        elif Ch_Focus is GwenX:
                                if not Player.Male:
                                    ch_g "Ты, эм. . . сделала все, как надо."
                                else:
                                    ch_g "Ты, эм. . . сделал все, как надо."
                        elif Ch_Focus is BetsyX:
                                ch_b "У тебя очень умелая рука. . ."
                        elif Ch_Focus is DoreenX:
                                if not Player.Male:
                                    ch_d "Ты, эм. . . -очень- хороша. . ."
                                else:
                                    ch_d "Ты, эм. . . -очень- хорош. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "У тебя настоящий талант. . ."
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                        if Ch_Focus is RogueX:
                                if not Player.Male:
                                    ch_k "Ты получила то, что хотела?"
                                else:
                                    ch_k "Ты получил то, что хотел?"
                        elif Ch_Focus is EmmaX:
                                if not Player.Male:
                                    ch_e "Ты удовлетворила свое любопытство?"
                                else:
                                    ch_e "Ты удовлетворил свое любопытство?"
                        elif Ch_Focus is LauraX:
                                if not Player.Male:
                                    ch_l "Ты удовлетворила свое любопытство?"
                                else:
                                    ch_l "Ты удовлетворил свое любопытство?"
                        elif Ch_Focus is JeanX:
                                if not Player.Male:
                                    ch_j "Ты удовлетворила свое любопытство?"
                                else:
                                    ch_j "Ты удовлетворил свое любопытство?"
                        elif Ch_Focus is StormX:
                                ch_s "Полагаю, тебе понравилось. . ."
                        elif Ch_Focus is JubesX:
                                if not Player.Male:
                                    ch_v "Ты нашла то, что искала?"
                                else:
                                    ch_v "Ты нашел то, что искал?"
                        elif Ch_Focus is GwenX:
                                ch_g "Тебе понравилось?"
                        elif Ch_Focus is BetsyX:
                                ch_b "Тебе этого достаточно?"
                        elif Ch_Focus is DoreenX:
                                ch_d "Тебе этого достаточно?"
                        elif Ch_Focus is WandaX:
                                ch_w "Тебе этого достаточно?"

    $ Tempmod = 0
#    if Situation == "shift":
#        ch_d "Oh? What did you have in mind?"
    call Checkout
    return

# end Ch_Focus.Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Girl_Insert_Pussy:
#    call Shift_Focus(Girl)
    if Situation == "auto":                                                                  #You auto-start
        if ApprovalCheck(Ch_Focus, 1100, TabM = 2):
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Obed", 70, 2)
            $ Ch_Focus.Statup("Inbt", 70, 3)
            $ Ch_Focus.Statup("Inbt", 30, 2)
            "Когда вы вводите палец внутрь, [Ch_Focus.Name] слегка удивляется, но вскоре расслабляется."
            jump Girl_IP_Prep
        else:
            $ Ch_Focus.FaceChange("surprised",2)
            $ Ch_Focus.Statup("Love", 80, -2)
            $ Ch_Focus.Statup("Obed", 50, -3)
            $ Line = renpy.random.choice(["Что?",
                "Эй!",
                "М?",
                "Ох!",
                "Воу!",
                "Прошу прощения?",
                "Хм."])
            call AnyLine(Ch_Focus,Line)
            "Она шлепает вас по руке."
            $ Ch_Focus.FaceChange("perplexed",1)
            if Ch_Focus is RogueX:
                    ch_r "Держи пальцы снаружи, [RogueX.Petname]."
            elif Ch_Focus is KittyX:
                    ch_k "Эм, не надо."
            elif Ch_Focus is EmmaX:
                    ch_e "Осторожней с тем, что суешь туда, однажды ты можешь этого лишиться."
            elif Ch_Focus is LauraX:
                    ch_l "Следи за руками, или потеряешь их."
            elif Ch_Focus is JeanX:
                    ch_j "Не так быстро, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Осторожней с тем, что суешь туда, однажды ты можешь этого лишиться."
            elif Ch_Focus is JubesX:
                    ch_v "Следи за своими руками, или их потеряешь."
            elif Ch_Focus is GwenX:
                    ch_g "Следи за своими руками, или их потеряешь."
            elif Ch_Focus is BetsyX:
                    ch_b "Не трогай там."
            elif Ch_Focus is DoreenX:
                    ch_d "Эм. . . пожалуйста, держи пальцы снаружи. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Эм. . . пожалуйста, держи пальцы снаружи. . ."
            return

    if ApprovalCheck(Ch_Focus, 1100, TabM = 2):                                                                   #She's into it. . .
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Inbt", 60, 1)
            call Sex_Basic_Dialog(Ch_Focus,"forceit") #"Stop asking."
        else:
            $ Ch_Focus.FaceChange("sexy", 1)
            $ Ch_Focus.Statup("Love", 90, 1)
            $ Ch_Focus.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Ах. . .",
                    "Как приятно. . .",
                    "Ооохх. . .",
                    "Ммммммм. . ."])
            call AnyLine(Ch_Focus,Line)
        $ Ch_Focus.Statup("Obed", 20, 1)
        $ Ch_Focus.Statup("Obed", 60, 1)
        $ Ch_Focus.Statup("Inbt", 70, 2)
        jump Girl_IP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("bemused", 1)
        if Ch_Focus is RogueX:
                ch_r "Этого не произойдет."
        elif Ch_Focus is KittyX:
                ch_k "Ни за что."
        elif Ch_Focus is EmmaX:
                ch_e "Нет."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Не-а."
        elif Ch_Focus is BetsyX:
                ch_b "Благодарю, но нет."
        elif Ch_Focus is DoreenX:
                ch_d "Ох. эм. . . нет, спасибо."
        elif Ch_Focus is WandaX:
                ch_w "Нет, спасибо."
        $ Ch_Focus.Blush = 0
    return


label Girl_IP_Prep: #Animation set-up
    if not Ch_Focus.InsertP:
        $ Ch_Focus.InsertP = 1
        $ Ch_Focus.SEXP += 10
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -60)
            $ Ch_Focus.Statup("Obed", 70, 55)
            $ Ch_Focus.Statup("Inbt", 80, 35)
        else:
            $ Ch_Focus.Statup("Love", 90, 10)
            $ Ch_Focus.Statup("Obed", 70, 20)
            $ Ch_Focus.Statup("Inbt", 80, 25)

    if not Ch_Focus.Forced and Situation != "auto":
        call Girl_Undress(Ch_Focus,"bottom")
        if "angry" in Ch_Focus.RecentActions:
            return

#    call Girl_Pussy_Launch("insert pussy")
    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)

    $ Line = 0
    $ Speed = 2
    return

# end Ch_Focus.Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Girl_Lick_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)
                                                                                  # Will she let you fondle? Modifiers
    if Ch_Focus.LickP: #You've done it before
        $ Tempmod += 15
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 3
    if Ch_Focus.PantsNum() >= 6 or Ch_Focus.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 15
    if Ch_Focus.Lust > 95:
        $ Tempmod += 20
    elif Ch_Focus.Lust > 85: #She's really horny
        $ Tempmod += 15
    if Situation == "shift":
        $ Tempmod += 10
    if Ch_Focus.Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (4*Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 25
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10
    if Ch_Focus in (EmmaX,StormX) and Ch_Focus.Taboo and "public" not in Ch_Focus.History:
        $ Tempmod -= 20

    if "no lick pussy" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no lick pussy" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Obed", 70, 2)
            $ Ch_Focus.Statup("Inbt", 70, 3)
            $ Ch_Focus.Statup("Inbt", 30, 2)
            "Когда вы присаживаетесь и начинаете лизать ее киску, [Ch_Focus.Name] пугается, но вскоре отдается новым ощущениям."
            $ Ch_Focus.FaceChange("sexy")
            jump Girl_LP_Prep
        else:
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Statup("Love", 80, -2)
            $ Ch_Focus.Statup("Obed", 50, -3)
            if Ch_Focus is RogueX:
                    ch_r "Ох! Нет, спасибо, [RogueX.Petname]."
            elif Ch_Focus is KittyX:
                    ch_k "Оооо! Эм, нет, спасибо. Нет. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Мне, так сказать, нравится, где находится твоя голова, но, возможно, стоит с этим повременить."
            elif Ch_Focus is LauraX:
                    ch_l "Эй, у тебя хорошее чутье, но, может быть, повременим?"
            elif Ch_Focus is JeanX:
                    ch_j "Хмммм, не сейчас, [JeanX.Petname]."
            elif Ch_Focus is StormX:
                    ch_s "Я ценю твои намерения, но сейчас не время для этого."
            elif Ch_Focus is JubesX:
                    ch_v "Эй, у тебя хорошее чутье, но, может быть, повременим?"
            elif Ch_Focus is GwenX:
                    ch_g "Эм. . . это не совсем то, что мне. . . необходимо."
            elif Ch_Focus is BetsyX:
                    ch_b "Ох, дорогуша . . в этом нет. . . необходимости."
            elif Ch_Focus is DoreenX:
                    ch_d "Ох, эм. . . в этом нет никакой. . . необходимости."
            elif Ch_Focus is WandaX:
                    ch_w "Воу! Не нужно этого делать."
            $ Ch_Focus.FaceChange("perplexed",1)
            "Она отталкивает вашу голову от себя."
            $ Tempmod = 0
            $ Trigger2 = 0
            return

    if "lick pussy" in Ch_Focus.RecentActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                call AnyLine(Ch_Focus,"Мммм, опять? Что ж, пожалуй, я не против. . .")
        else:
                call AnyLine(Ch_Focus,"Снова? Ну ладно.")
        jump Girl_LP_Prep
    elif "lick pussy" in Ch_Focus.DailyActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Тебе следует расслабиться. . .",
                    "Полегче.",
                    "Похоже, я сделала что-то правильно.",
                    "Мне это очень нравится. . .",
                    "Нежнее. . . нежнее. . .",
                    "Расслабься. . .",
                    "Ммм. . ."])
        else:
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Тебе следует расслабиться. . .",
                    "Тебе все мало?",
                    "Полегче.",
                    "Мне это очень нравится. . .",
                    "Похоже, я сделала что-то правильно.",
                    "Тебе следует расслабиться. . .",
                    "Расслабься. . .",
                    "Не торопись, я еще не отошла от прошлого раза.",
                    "Расслабься. . .",
                    "Ммм. . ."])
        call AnyLine(Ch_Focus,Line)

    if Approval >= 2:                                                                   #She's into it. . .
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Inbt", 60, 1)
        else:
            $ Ch_Focus.FaceChange("sexy", 1)
            $ Ch_Focus.Eyes = "closed"
            $ Ch_Focus.Statup("Love", 90, 1)
            $ Ch_Focus.Statup("Inbt", 50, 3)
            $ Ch_Focus.Statup("Lust", 200, 3)
        if Ch_Focus is RogueX:
                ch_r "Конечно, давай."
        elif Ch_Focus is KittyX:
                ch_k "Ладно, как скажешь."
        elif Ch_Focus is EmmaX:
                ch_e "Ммм, я не могу отказаться. . ."
        elif Ch_Focus is LauraX:
                ch_l "Конечно, звучит весело."
        elif Ch_Focus is JeanX:
                ch_j "Конечно, звучит весело."
        elif Ch_Focus is StormX:
                ch_s "С удовольствием. . ."
        elif Ch_Focus is JubesX:
                ch_v "Конечно, звучит весело."
        elif Ch_Focus is GwenX:
                ch_g "Конечно, звучит весело."
        elif Ch_Focus is BetsyX:
                ch_b "Мммм, я только за. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Конечно."
        elif Ch_Focus is WandaX:
                ch_w "Конечно."
        $ Ch_Focus.Statup("Obed", 20, 1)
        $ Ch_Focus.Statup("Obed", 60, 1)
        $ Ch_Focus.Statup("Inbt", 70, 2)
        jump Girl_LP_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("angry", 1)

        if "no lick pussy" in Ch_Focus.RecentActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions and "no lick pussy" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif "no lick pussy" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif not Ch_Focus.LickP:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "Это довольно интимно, [RogueX.Petname]. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Это довольно интимно, [KittyX.Petname]. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Я не уверена, что наши отношения на этом этапе, [EmmaX.Petname]. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Я не уверена, что мы уже в таких отношениях, [LauraX.Petname]. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Ммммм, давай в другой раз, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Ох, это было бы. . . хотя, нет, [StormX.Petname]. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Я не уверена, что мы уже в таких отношениях, [JubesX.Petname]. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Ох, тебе, эм, не нужно это предлагать. . ."
            elif Ch_Focus is BetsyX:
                    if not Player.Male:
                        ch_b "Ох, дорогуша, ты. . . не обязана. . ."
                    else:
                        ch_b "Ох, дорогуша, ты. . . не обязан. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Эм, тебе. . . не нужды это делать. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Тебе не стоит этого делать. . ."
        else:
            $ Ch_Focus.FaceChange("bemused")
            call Sex_Basic_Dialog(Ch_Focus,"nothanks")
        menu:
            extend ""
            "Извини, забудь." if "no lick pussy" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"noproblem")  # ch_r "Ok, no problem, [RogueX.Petname]."
                return
            "Мне кажется, в следующий раз я смогу тебя убедить. . ." if "no lick pussy" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy")
                call Sex_Basic_Dialog(Ch_Focus,"maybe")  # ch_d "I'll think about it, [Ch_Focus.Petname]."
                $ Ch_Focus.Statup("Love", 80, 2)
                $ Ch_Focus.Statup("Inbt", 70, 2)
                if Taboo:
                    $ Ch_Focus.RecentActions.append("tabno")
                    $ Ch_Focus.DailyActions.append("tabno")
                $ Ch_Focus.RecentActions.append("no lick pussy")
                $ Ch_Focus.DailyActions.append("no lick pussy")
                return
            "Думаю, тебе бы это очень понравилось. . .":
                if Approval:
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 90, 2)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                    call Sex_Basic_Dialog(Ch_Focus,"enjoyyes")  # ch_d "Maybe I will. . ."
                    $ Ch_Focus.Statup("Inbt", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 40, 2)
                    jump Girl_LP_Prep
                else:
                    $ Ch_Focus.FaceChange("sexy")
                    call Sex_Basic_Dialog(Ch_Focus,"enjoyno")  # ch_d "I don't know, but. . . no. Still \"no,\" [Ch_Focus.Petname]."

            "[[Все равно приступить]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(Ch_Focus, 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -5, 1)
                    $ Ch_Focus.Statup("Love", 200, -2)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #ch_w "Whoa!" ch_w ". . ." ch_w "Ok, ok, just get to it. . ."
                    $ Ch_Focus.Statup("Obed", 50, 4)
                    $ Ch_Focus.Statup("Inbt", 80, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ Ch_Focus.Forced = 1
                    jump Girl_LP_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -15)
                    $ Ch_Focus.FaceChange("angry", 1)
                    $ Line = renpy.random.choice(["Что?",
                        "Эй!",
                        "М?",
                        "Воу!",
                        "Прошу прощения?",
                        "Хм."])
                    call AnyLine(Ch_Focus,Line)
                    "Она отталкивает вашу голову назад."
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    if "no lick pussy" in Ch_Focus.DailyActions:
        call Sex_Basic_Dialog(Ch_Focus,"noday") #"Stop asking."
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("angry", 1)
        if Ch_Focus is RogueX:
                if not Player.Male:
                    ch_r "Я не хочу, чтобы ты касалась меня."
                else:
                    ch_r "Я не хочу, чтобы ты касался меня."
        elif Ch_Focus is KittyX:
                ch_k "Даже не думай."
        elif Ch_Focus is EmmaX:
                ch_e "Не искушай судьбу."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Ты заходишь слишком далеко."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Эм, нет, спасибо. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, я не могу. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Это слишком для меня. . ."
        elif Ch_Focus is WandaX:
                ch_w "Это не по мне."
        $ Ch_Focus.Statup("Lust", 80, 5)
        $ Ch_Focus.Statup("Obed", 50, -2)
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Taboo:
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.RecentActions.append("tabno")
        $ Ch_Focus.DailyActions.append("tabno")
        call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You picked a bad place for this. . ."
    elif Ch_Focus.LickP:
        $ Ch_Focus.FaceChange("sad")
        if Ch_Focus is RogueX:
                ch_r "Извини, но держи свой язык при себе."
        elif Ch_Focus is KittyX:
                ch_k "Держи свою голову подальше оттуда."
        elif Ch_Focus is EmmaX:
                ch_e "Держи свою голову подальше оттуда."
        elif Ch_Focus is LauraX:
                ch_l "Держи свою голову подальше оттуда."
        elif Ch_Focus is JeanX:
                ch_j "Держи свой язык подальше от меня."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Держи свою голову подальше оттуда."
        elif Ch_Focus is GwenX:
                ch_g "Я, эм. . . больше не хочу."
        elif Ch_Focus is BetsyX:
                ch_b "Думаю, мы не можем повторить."
        elif Ch_Focus is DoreenX:
                if not Player.Male:
                    ch_d "Не думаю, что хочу, чтобы ты снова прикасалась ко мне там."
                else:
                    ch_d "Не думаю, что хочу, чтобы ты снова прикасался ко мне там."
        elif Ch_Focus is WandaX:
                if not Player.Male:
                    ch_w "Ты потеряла эту привилегию."
                else:
                    ch_w "Ты потерял эту привилегию."

    else:
        $ Ch_Focus.FaceChange("surprised")
        if Ch_Focus is RogueX:
                ch_r "Фу!"
        elif Ch_Focus is KittyX:
                ch_k "Фи!"
        elif Ch_Focus is EmmaX:
                ch_e "Я знаю, я так же разочарована, как и ты."
        elif Ch_Focus is LauraX:
                ch_l "Мне жаль."
        elif Ch_Focus is JeanX:
                ch_j "Мне жаль."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Эм. . . нет, спасибо."
        elif Ch_Focus is BetsyX:
                ch_b "Ох. . . благодарю, но нет."
        elif Ch_Focus is DoreenX:
                ch_d "Ох. . . нет. . . но спасибо за предложение."
        elif Ch_Focus is WandaX:
                ch_w "Что ж, спасибо за предложение."
        $ Ch_Focus.FaceChange()
    $ Ch_Focus.RecentActions.append("no lick pussy")
    $ Ch_Focus.DailyActions.append("no lick pussy")
    $ Tempmod = 0
    return

label Girl_LP_Prep: #Animation set-up
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return

    $ Tempmod = 0
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"lick pussy")
    else:
            call ViewShift(Ch_Focus,"pussy",0,"lick pussy")

    if Situation == Ch_Focus:
            #Doreen auto-starts
            $ Situation = 0
            if (Ch_Focus.Legs and not Ch_Focus.Upskirt) or (Ch_Focus.Panties and not Ch_Focus.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(Ch_Focus, 1250, TabM = 1) or (Ch_Focus.SeenPussy and ApprovalCheck(Ch_Focus, 500) and not Taboo):
                        $ Ch_Focus.Upskirt = 1
                        $ Ch_Focus.PantiesDown = 1
                        $ Line = 0
                        if Ch_Focus.PantsNum() == 5:
                            $ Line = Ch_Focus.Name + "задирает свою юбку"
                        elif Ch_Focus.PantsNum() >= 6:
                            $ Line = Ch_Focus.Name + " стягивает с себя " + get_clothing_name(Ch_Focus.Legs_key, vin)
                        else:
                            $ Line = 0
                        if Ch_Focus.Panties:
                            if Line:
                                #wearing pants
                                "[Line] и сдвигает свои [get_clothing_name(Ch_Focus.Panties_key, vin)] в сторону."
                                "Затем она берет вас за голову и тянет ее к своей промежности, явно желая, чтобы вы взялись за дело."
                            else:
                                #no pants
                                "Она сдвигает свои [get_clothing_name(Ch_Focus.Panties_key, vin)] в сторону, а затем обхватывает своими бедрами вашу голову."
                                "Она явно хочет, чтобы вы взялись за дело."
                        else:
                            #pants but no panties
                            "[Line], а затем обхватывает своими бедрами вашу голову."
                            "Она явно хочет, чтобы вы взялись за дело."
                        call Girl_First_Bottomless(Ch_Focus,1)
                else:
                        "[Ch_Focus.Name] берет вас за голову и тянет ее к своей промежности, явно желая, чтобы вы взялись за дело."
            else:
                        "[Ch_Focus.Name] берет вас за голову и тянет ее к своей промежности, явно желая, чтобы вы взялись за дело."
            menu:
                "Что будете делать?"
                "Приступить.":
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 2)
                    "Вы начинаете работать языком."
                "Похвалить ее.":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    ch_p "Ммм, мне нравится твоя идея, [Ch_Focus.Pet]."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "Вы начинаете работать языком."
                    $ Ch_Focus.Statup("Love", 85, 1)
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    "Вы отводите свою голову."
                    $ Ch_Focus.FaceChange("surprised")
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    ch_p "[Ch_Focus.Pet], давай не будем."
                    if Ch_Focus is JeanX:
                            $ JeanX.Statup("Love", 70, -5)
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] отстраняется."
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 1)
                    $ Ch_Focus.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ Ch_Focus.AddWord(1,"refused","refused")
                    return
            #end auto

    if not Ch_Focus.Forced and Situation != "auto":
        $ Tempmod = 0
        if Ch_Focus.PantsNum() >= 6 and not Ch_Focus.Upskirt:
            $ Tempmod = 15
        call Bottoms_Off(Ch_Focus)
        if "angry" in Ch_Focus.RecentActions:
            return

    if not Ch_Focus.LickP:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -30)
            $ Ch_Focus.Statup("Obed", 70, 35)
            $ Ch_Focus.Statup("Inbt", 80, 75)
        else:
            $ Ch_Focus.Statup("Love", 90, 35)
            $ Ch_Focus.Statup("Obed", 70, 15)
            $ Ch_Focus.Statup("Inbt", 80, 35)
    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    if Ch_Focus.PantsNum() == 5:
        $ Ch_Focus.Upskirt = 1
        $ Ch_Focus.SeenPanties = 1
    call Girl_First_Bottomless(Ch_Focus,1)

    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no lick pussy")
    $ Ch_Focus.AddWord(0,"lick pussy","lick pussy")
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"lick pussy")
    else:
            call ViewShift(Ch_Focus,"pussy",0,"lick pussy")

label Girl_LP_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"lick pussy")
#        call Shift_Focus(Girl)
        $ Ch_Focus.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . .":
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_LP_Cycle
                        "В стиле минета" if Ch_Focus.Pose == "69":
                                    call Girl_BJ_Menu
                                    jump Girl_LP_Cycle
                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                        "Сменить вид":
                                    call ViewShift(Ch_Focus,"menu")
                                    jump Girl_LP_Cycle

                        "Другие варианты":
                                menu:
                                    "Дополнительное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ Ch_Focus.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Сменить основное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                    menu:
                                                        "Отпрянуть и снова начать ласкать.":
                                                                if Ch_Focus.Action and MultiAction:
                                                                    $ Situation = "pullback"
                                                                    call Girl_LP_After
                                                                    call Girl_Fondle_Pussy
                                                                else:
                                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        "Я хочу вставить туда фаллоимитатор.":
                                                                $ Situation = "shift"
                                                                call Girl_LP_After
                                                                call Girl_Dildo("pussy") #call Girl_Dildo_Pussy
                                                                if "no dildo" not in Ch_Focus.RecentActions: #if she refuses, continue on, otherwise, skip back to previous label
                                                                        return
                                                        "Неважно":
                                                                jump Girl_LP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Переключить свое внимание" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Girl_LP_After
                                                call Offhand_Set
                                    "Переключить свое внимание (locked)" if not Trigger2:
                                                pass

                                    "Тройничек (locked)" if not Partner:
                                        pass
                                    "Тройничек" if Partner:
                                        menu:
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе" if Trigger == "lesbian":
                                                        call Les_Change(Ch_Focus)
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Пусть [Partner.Name] займется чем-нибудь другим":
                                                        call Three_Change(Ch_Focus)

                                            "Не бросай свое текущее занятие. . . (locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_LP_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_LP_Cycle
                                            "Неважно":
                                                        jump Girl_LP_Cycle

                                    "Показывать ее ноги" if not ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Вставить анальную пробку" if not Ch_Focus.Plug and "plug" in Ch_Focus.Inventory:
                                            call Insert_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку" if Ch_Focus.Plug:
                                            call Remove_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку (locked)" if "plug" not in Ch_Focus.Inventory:
                                            pass

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_LP_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_LP_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_LP_After
        #End menu (if Line)

        if Ch_Focus.Panties or Ch_Focus.PantsNum() >= 6 or Ch_Focus.HoseNum() >= 5: #This checks if Doreen wants to strip down.
                call Girl_Undress(Ch_Focus,"auto")

#        call Shift_Focus(Girl)
        call Sex_Dialog(Ch_Focus,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Ch_Focus)
                            if "angry" in Ch_Focus.RecentActions:
                                call Girl_Pos_Reset(Ch_Focus)
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_LP_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Doreen can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_LP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in Ch_Focus.RecentActions:#And Doreen is unsatisfied,
                                    "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                    menu:
                                        "Хотите завершить начатое?"
                                        "Продолжим еще немного.":
                                            $ Line = "Вы возвращаетесь к процессу"
                                        "С меня хватит.":
                                            "Вы заканчиваете веселье."
                                            jump Girl_LP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.LickP):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Тебе нравится?"
                    elif Ch_Focus is KittyX:
                            ch_k "Тебе нравится?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Разве она не восхитительна?"
                    elif Ch_Focus is LauraX:
                            ch_l "Разве она не восхитительна?"
                    elif Ch_Focus is JeanX:
                            ch_j "Разве она не восхитительна?"
                    elif Ch_Focus is StormX:
                            ch_s "Ох, это восхитительно. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Ага, мне это тоже нравится. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Это. . . эм. . . приятно."
                    elif Ch_Focus is BetsyX:
                            ch_b "О боже. . . это. . . восхитительно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ох, ого. . . это . . -очень- приятно. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Послушай. . . у тебя прямо талант. . ."
        elif Ch_Focus.Lust >= 80:
                    pass
        elif Cnt == (15 + Ch_Focus.LickP) and Ch_Focus.SEXP >= 15 and not ApprovalCheck(Ch_Focus, 1500):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Я знаю, что тебе весело, но, возможно, нам стоит попробовать что-нибудь другое, [RogueX.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Может быть, мы могли бы попробовать что-нибудь еще, [KittyX.Petname]?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Возможно, мы могли бы попробовать что-то другое, [EmmaX.Petname]?"
                    elif Ch_Focus is LauraX:
                            ch_l "Может, пришло время для чего-нибудь другого, [LauraX.Petname]?"
                    elif Ch_Focus is JeanX:
                            ch_j "Может, пришло время для чего-нибудь другого, [JeanX.Petname]?"
                    elif Ch_Focus is StormX:
                            ch_s "Уверена, тебе сейчас весело, но не могли бы мы попробовать что-нибудь другое?"
                    elif Ch_Focus is JubesX:
                            ch_v "Может, попробуем. . . что-нибудь другое?"
                    elif Ch_Focus is GwenX:
                            ch_g "Может, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Может быть, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Не могли бы мы заняться чем-нибудь другим?"
                    elif Ch_Focus is WandaX:
                            ch_w "Разве мы не можем заняться чем-нибудь другим?"
                    menu:
                        extend ""
                        "Закончить.":
                                "Вы заканчиваете веселье. . ."
                                jump Girl_LP_After
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Girl_LP_After
                        "Не-а, это так весело.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она возмущается, но позволяет вам продолжить."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call Girl_Pos_Reset(Ch_Focus)
                                    "Она кидает на вас сердитый взгляд и отстраняется."
                                    if Ch_Focus is DoreenX:
                                            ch_d "Тогда, думаю, тебе придется вытереть рот."
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_LP_After
        #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10) #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5) #ch_d "Tic tock, [Ch_Focus.Petname]."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done") # "Ok, [Ch_Focus.Petname], breaktime."


label Girl_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Girl_Pos_Reset(Ch_Focus)

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.LickP += 1
    $ Ch_Focus.Action -=1
    if Ch_Focus.PantsNum() < 6 or Ch_Focus.Upskirt:
        $ Ch_Focus.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ Ch_Focus.Addictionrate += 1

    if Partner == "Rogue":
        call Partner_Like(Ch_Focus,3,2)
    else:
        call Partner_Like(Ch_Focus,2)

    if Ch_Focus.LickP == 1:
            $ Ch_Focus.SEXP += 10
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                    if Ch_Focus is RogueX:
                            ch_r "Ну и. . . как я на вкус?"
                    elif Ch_Focus is KittyX:
                            ch_k "Это было. . . приятно?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Я бы хотела чаще пользоваться твоими услугами. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Ты в самом деле хорошо умеешь пользоваться языком."
                    elif Ch_Focus is JeanX:
                            if not Player.Male:
                                ch_j "Хорошо поработала языком. . ."
                            else:
                                ch_j "Хорошо поработал языком. . ."
                    elif Ch_Focus is StormX:
                            ch_s "У тебя определенно талант. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Не зря я связалась с тобой. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Ты, эм. . . спасибо."
                    elif Ch_Focus is BetsyX:
                            ch_b "Ох, у тебя. . . настоящий. . . талант. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "У тебя потрясающий язычок. . ."
                    elif Ch_Focus is WandaX:
                            if not Player.Male:
                                ch_w "Ты совсем не плоха. . ."
                            else:
                                ch_w "Ты совсем не плох. . ."
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                    $ Ch_Focus.FaceChange("perplexed", 1)
                    if Ch_Focus is RogueX:
                            ch_r "Тебе понравилось?"
                    elif Ch_Focus is KittyX:
                            ch_k "Ну, тебе она понравилась?"
                    elif Ch_Focus is EmmaX:
                            if not Player.Male:
                                ch_e "Полагаю, это пошло на пользу нам обеим. . ."
                            else:
                                ch_e "Полагаю, это пошло на пользу нам обоим. . ."
                    elif Ch_Focus is LauraX:
                            if not Player.Male:
                                ch_l "Полагаю, мы обе что-то получили. . ."
                            else:
                                ch_l "Полагаю, мы оба что-то получили. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Думаю, это было не так уж и плохо. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Это было не так уж плохо. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Нууу, это было не так уж плохо. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе понравилось?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Тебе этого достаточно?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Тебе этого достаточно?"
                    elif Ch_Focus is WandaX:
                            ch_w "Тебе этого достаточно?"

    $ Tempmod = 0
#    if Situation == "shift":
#        ch_d "Oh? What did you have in mind?"
    call Checkout
    return


# end Ch_Focus.Lick Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Fondle Ass
label Girl_Fondle_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)
                                                                                     # Will she let you fondle? Modifiers
    if Ch_Focus.FondleA: #You've done it before
        $ Tempmod += 10
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 2
    if Ch_Focus.PantsNum() >= 6 or Ch_Focus.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 5
    if Ch_Focus.Lust > 75: #She's really horny
        $ Tempmod += 15
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += Taboo
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 25
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10
    if Ch_Focus in (EmmaX,StormX) and Ch_Focus.Taboo and "public" not in Ch_Focus.History:
        $ Tempmod -= 20

    if "no fondle ass" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no fondle ass" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 850, TabM=1) # 85, 100, 115, Taboo -40(125)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ Ch_Focus.FaceChange("surprised", 1)
            $ Ch_Focus.Statup("Obed", 70, 2)
            $ Ch_Focus.Statup("Inbt", 40, 2)
            "Когда ваша рука двигается вниз по ее попке, [Ch_Focus.Name] слегка удивляется, но затем кивает."
            $ Ch_Focus.FaceChange("sexy")
            jump Girl_FA_Prep
        else:
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Statup("Obed", 50, -3)
            if Ch_Focus is RogueX:
                    ch_r "Руки прочь, [RogueX.Petname]."
            elif Ch_Focus is KittyX:
                    ch_k "Руки прочь, [KittyX.Petname]."
            elif Ch_Focus is EmmaX:
                    ch_e "Руки прочь, [EmmaX.Petname]."
            elif Ch_Focus is LauraX:
                    ch_l "Руки прочь, [LauraX.Petname]."
            elif Ch_Focus is JeanX:
                    ch_j "Не так быстро, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Отпусти меня, [StormX.Petname]."
            elif Ch_Focus is JubesX:
                    ch_v "Руки прочь, [JubesX.Petname]."
            elif Ch_Focus is GwenX:
                    ch_g "Держи руки так, чтобы я их видела, [GwenX.Petname]."
            elif Ch_Focus is BetsyX:
                    ch_b "Не трогай там, [BetsyX.Petname]."
            elif Ch_Focus is DoreenX:
                    ch_d "Эй, руки прочь от моей попки, [DoreenX.Petname]."
            elif Ch_Focus is WandaX:
                    ch_w "Воу, убери руки оттуда, [WandaX.Petname]."
            $ Ch_Focus.FaceChange("bemused")
            $ Tempmod = 0
            $ Trigger2 = 0
            return

    if Situation == "pullback":
        $ Ch_Focus.FaceChange("surprised")
        $ Ch_Focus.Brows = "sad"
        if Ch_Focus.Lust > 80:
            $ Ch_Focus.Statup("Love", 70, -4)
        $ Ch_Focus.Statup("Obed", 90, 1)
        $ Ch_Focus.Statup("Obed", 70, 2)
        "Когда вы отстраняетесь, [Ch_Focus.Name] растроенно вздыхает."
        jump Girl_FA_Prep
    elif "fondle ass" in Ch_Focus.RecentActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                call AnyLine(Ch_Focus,"Мммм, опять? Что ж, пожалуй, я не против. . .")
        else:
                call AnyLine(Ch_Focus,"Снова? Ну ладно.")
        jump Girl_FA_Prep
    elif "fondle ass" in Ch_Focus.DailyActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Тебе следует расслабиться. . .",
                    "Полегче.",
                    "Нежнее. . . нежнее. . .",
                    "Расслабься. . .",
                    "Ммм. . ."])
        else:
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Тебе следует расслабиться. . .",
                    "Тебе все мало?",
                    "Полегче.",
                    "Тебе следует расслабиться. . .",
                    "Расслабься. . .",
                    "Не торопись, я еще не отошла от прошлого раза.",
                    "Расслабься. . .",
                    "Ммм. . ."])
        call AnyLine(Ch_Focus,Line)

    if Approval >= 2:                                                                   #She's into it. . .
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -2, 1)
            $ Ch_Focus.Statup("Obed", 90, 2)
            $ Ch_Focus.Statup("Inbt", 60, 2)
        else:
            $ Ch_Focus.FaceChange("bemused, 1")
        if Ch_Focus is RogueX:
                ch_r "Ладно, [RogueX.Petname], подойди и возьми."
        elif Ch_Focus is KittyX:
                ch_k "Ладно, [KittyX.Petname], подойди и возьми."
        elif Ch_Focus is EmmaX:
                ch_e "Звучит прекрасно, сделай мне приятно."
        elif Ch_Focus is LauraX:
                ch_l "Конечно, звучит весело."
        elif Ch_Focus is JeanX:
                ch_j "Конечно, звучит весело."
        elif Ch_Focus is StormX:
                ch_s "С удовольствием. . ."
        elif Ch_Focus is JubesX:
                ch_v "Конечно, звучит весело."
        elif Ch_Focus is GwenX:
                ch_g "Конечно, звучит весело."
        elif Ch_Focus is BetsyX:
                ch_b "Понимаю."
        elif Ch_Focus is DoreenX:
                ch_d "Конечно."
        elif Ch_Focus is WandaX:
                ch_w "Конечно."
        $ Ch_Focus.Statup("Lust", 200, 3)
        $ Ch_Focus.Statup("Obed", 60, 1)
        $ Ch_Focus.Statup("Inbt", 70, 1)
        jump Girl_FA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("angry", 1)
        if "no fondle ass" in Ch_Focus.RecentActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions and "no fondle ass" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif "no fondle ass" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif not Ch_Focus.FondleA:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "Не сейчас, [Ch_Focus.Petname]. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Не сейчас, [Ch_Focus.Petname]. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Не сейчас, [EmmaX.Petname]. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Не сейчас, [LauraX.Petname]. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Не сейчас, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Я бы предпочла этого не делать, [StormX.Petname]. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Не сейчас, [JubesX.Petname]. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Я даже не знаю, что ответить, [GwenX.Petname]. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Пожалуй, не сейчас, [BetsyX.Petname]. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Думаю, нам не стоит этого делать, [DoreenX.Petname]. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Думаю, нам не стоит этого делать, [WandaX.Petname]. . ."
        else:
            $ Ch_Focus.FaceChange("bemused")
            call Sex_Basic_Dialog(Ch_Focus,"nothanks")
        menu:
            extend ""
            "Извини, забудь." if "no fondle ass" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"noproblem")  # ch_r "Ok, no problem, [RogueX.Petname]."
                return
            "Может, в другой раз?" if "no fondle ass" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy")
                call Sex_Basic_Dialog(Ch_Focus,"maybe")  # ch_d "I'll think about it, [Ch_Focus.Petname]."
                $ Ch_Focus.Statup("Love", 80, 2)
                $ Ch_Focus.Statup("Inbt", 50, 2)
                if Taboo:
                    $ Ch_Focus.RecentActions.append("tabno")
                    $ Ch_Focus.DailyActions.append("tabno")
                $ Ch_Focus.RecentActions.append("no fondle ass")
                $ Ch_Focus.DailyActions.append("no fondle ass")
                return
            "Можно я только разок хорошо сожму?":
                if Approval:
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                    if Ch_Focus is RogueX:
                            ch_r "Хорошо, раз ты собираешься умолять. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Мне нравится, когда ты умоляешь. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Мне нравится слушать, как ты умоляешь. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Ооох, умоляй меня. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Ооох, умоляй меня. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Что ж, разок не повредит. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Ооох, умоляй меня. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Ну. . . разок возможно. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Ну. . . если только разок. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ну. . . если только разочек. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Если только один раз. . ."
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    $ Ch_Focus.Statup("Inbt", 40, 2)
                    jump Girl_FA_Prep
                else:
                    $ Ch_Focus.FaceChange("sexy")
                    call Sex_Basic_Dialog(Ch_Focus,"pleaseno") #ch_d "Not even one."

            "[[Все равно начать ласкать]":                                               # Pressured into fondling.
                $ Approval = ApprovalCheck(Ch_Focus, 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -3, 1)
                    $ Ch_Focus.Statup("Love", 200, -1)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #ch_w "Whoa!" ch_w ". . ." ch_w "Ok, ok, just get to it. . ."
                    $ Ch_Focus.Statup("Obed", 50, 3)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ Ch_Focus.Forced = 1
                    jump Girl_FA_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -10)
                    $ Ch_Focus.FaceChange("angry", 1)
                    $ Line = renpy.random.choice(["Что?",
                        "Эй!",
                        "М?",
                        "Воу!",
                        "Прошу прощения?",
                        "Хм."])
                    call AnyLine(Ch_Focus,Line)
                    "Она шлепает вас по руке."
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    if "no fondle ass" in Ch_Focus.DailyActions:
        call Sex_Basic_Dialog(Ch_Focus,"noday") #"Stop asking."
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("angry", 1)
        if Ch_Focus is RogueX:
                if not Player.Male:
                    ch_r "Я не хочу, чтобы ты касалась меня."
                else:
                    ch_r "Я не хочу, чтобы ты касался меня."
        elif Ch_Focus is KittyX:
                ch_k "Даже не думай."
        elif Ch_Focus is EmmaX:
                ch_e "Не искушай судьбу."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Ты заходишь слишком далеко."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Эм, нет, спасибо. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, я не могу. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Это слишком для меня. . ."
        elif Ch_Focus is WandaX:
                ch_w "Это не по мне."
        $ Ch_Focus.Statup("Lust", 60, 5)
        $ Ch_Focus.Statup("Obed", 50, -2)
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Taboo:
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.RecentActions.append("tabno")
        $ Ch_Focus.DailyActions.append("tabno")
        call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You picked a bad place for this. . ."
    elif Ch_Focus.FondleA:
        $ Ch_Focus.FaceChange("sad")
        if Ch_Focus is RogueX:
                ch_r "Извини, но убери руки от моей попки."
        elif Ch_Focus is KittyX:
                ch_k "У тебя был шанс."
        elif Ch_Focus is EmmaX:
                ch_e "Боюсь, ты не заслуживаешь моего расположения."
        elif Ch_Focus is LauraX:
                ch_l "Тебе придется снова заслужить это."
        elif Ch_Focus is JeanX:
                ch_j "С нас хватит этого."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Тебе придется это заслужить."
        elif Ch_Focus is GwenX:
                ch_g "Я, эм. . . больше не хочу."
        elif Ch_Focus is BetsyX:
                ch_b "Боюсь, этого больше не повторится."
        elif Ch_Focus is DoreenX:
                ch_d "Нет, я не хочу."
        elif Ch_Focus is WandaX:
                ch_w "Не сейчас."
    else:
        $ Ch_Focus.FaceChange("sexy")
        $ Ch_Focus.Mouth = "sad"
        if Ch_Focus is RogueX:
                ch_r "Этого не произойдет."
        elif Ch_Focus is KittyX:
                ch_k "Ни за что."
        elif Ch_Focus is EmmaX:
                ch_e "Нет."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Нет."
        elif Ch_Focus is GwenX:
                ch_g "Не-а."
        elif Ch_Focus is BetsyX:
                ch_b "Благодарю, но нет."
        elif Ch_Focus is DoreenX:
                ch_d "Нет, спасибо."
        elif Ch_Focus is WandaX:
                ch_w "Нет, спасибо."
    $ Ch_Focus.RecentActions.append("no fondle ass")
    $ Ch_Focus.DailyActions.append("no fondle ass")
    $ Tempmod = 0
    return

return

label Girl_FA_Prep: #Animation set-up
    if Trigger2 == "fondle ass":
        return
    if not Ch_Focus.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(Ch_Focus)
        if "angry" in Ch_Focus.RecentActions:
            return
    $ Tempmod = 0
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle ass")
    else:
            call ViewShift(Ch_Focus,"mid",0,"fondle ass")
    if not Ch_Focus.FondleA:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -20)
            $ Ch_Focus.Statup("Obed", 70, 20)
            $ Ch_Focus.Statup("Inbt", 80, 15)
        else:
            $ Ch_Focus.Statup("Love", 90, 10)
            $ Ch_Focus.Statup("Obed", 70, 12)
            $ Ch_Focus.Statup("Inbt", 80, 20)
    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no fondle ass")
    $ Ch_Focus.AddWord(0,"fondle ass","fondle ass")
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle ass")
    else:
            call ViewShift(Ch_Focus,"breasts",0,"fondle ass")

label Girl_FA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"fondle ass")
#        call Shift_Focus(Girl)
        $ Ch_Focus.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . .":
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_FA_Cycle
                        "В стиле минета" if Ch_Focus.Pose == "69":
                                    call Girl_BJ_Menu
                                    jump Girl_FA_Cycle

                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                        "Сменить вид":
                                    call ViewShift(Ch_Focus,"menu")
                                    jump Girl_FA_Cycle

                        "Другие варианты":
                                menu:
                                    "Дополнительное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ Ch_Focus.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Сменить основное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                    menu:
                                                        "Я хочу вставить палец внутрь.":
                                                                $ Situation = "shift"
                                                                call Girl_FA_After
                                                                call Girl_Insert_Ass
                                                        "Просто вставить палец, не спрашивая.":
                                                                $ Situation = "auto"
                                                                call Girl_FA_After
                                                                call Girl_Insert_Ass
                                                        "Я хочу вылизать твой анус.":
                                                                $ Situation = "shift"
                                                                call Girl_FA_After
                                                                call Girl_Lick_Ass
                                                        "Просто начать вылизывать.":
                                                                $ Situation = "auto"
                                                                call Girl_FA_After
                                                                call Girl_Lick_Ass
                                                        "Я хочу вставить туда фаллоимитатор.":
                                                                $ Situation = "shift"
                                                                call Girl_FA_After
                                                                call Girl_Dildo("anal") #call Girl_Dildo_Ass
                                                                if "no dildo" not in Ch_Focus.RecentActions: #if she refuses, continue on, otherwise, skip back to previous label
                                                                        return
                                                        "Неважно":
                                                                jump Girl_FA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Переключить свое внимание" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Girl_FA_After
                                                call Offhand_Set
                                    "Переключить свое внимание (locked)" if not Trigger2:
                                                pass

                                    "Тройничек (locked)" if not Partner:
                                        pass
                                    "Тройничек" if Partner:
                                        menu:
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе" if Trigger == "lesbian":
                                                        call Les_Change(Ch_Focus)
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Пусть [Partner.Name] займется чем-нибудь другим":
                                                        call Three_Change(Ch_Focus)

                                            "Не бросай свое текущее занятие. . . (locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_FA_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_FA_Cycle
                                            "Неважно":
                                                        jump Girl_FA_Cycle

                                    "Показывать ее ноги" if not ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Вставить анальную пробку" if not Ch_Focus.Plug and "plug" in Ch_Focus.Inventory:
                                            call Insert_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку" if Ch_Focus.Plug:
                                            call Remove_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку (locked)" if "plug" not in Ch_Focus.Inventory:
                                            pass

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_FA_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_FA_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_FA_After
        #End menu (if Line)

        if Ch_Focus.Panties or Ch_Focus.PantsNum() >= 6 or Ch_Focus.HoseNum() >= 5: #This checks if Doreen wants to strip down.
                call Girl_Undress(Ch_Focus,"auto")

#        call Shift_Focus(Girl)
        call Sex_Dialog(Ch_Focus,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Ch_Focus)
                            if "angry" in Ch_Focus.RecentActions:
                                call Girl_Pos_Reset(Ch_Focus)
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2 and Ch_Focus.SEXP >= 20:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_FA_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Doreen can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_FA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in Ch_Focus.RecentActions:#And Doreen is unsatisfied,
                                    "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                    menu:
                                        "Хотите завершить начатое?"
                                        "Продолжим еще немного.":
                                            $ Line = "Вы возвращаетесь к процессу"
                                        "С меня хватит.":
                                            "Вы заканчиваете веселье."
                                            jump Girl_FA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.FondleA):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Ух, это приятно, но. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Ох, это приятно, но. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Ммм, мне очень нравится. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Мммм. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Мммм. . ."
                    elif Ch_Focus is StormX:
                            ch_d "Мммм. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Мммм. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе, эм. . . нравится?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Тебе приятно?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Она, эм, не -слишком- большая, правда?"
                    elif Ch_Focus is WandaX:
                            ch_w "Очень упругая, правда?"
        elif Ch_Focus.Lust >= 80:
                    pass
        elif Cnt == (15 + Ch_Focus.FondleA) and Ch_Focus.SEXP >= 15 and not ApprovalCheck(Ch_Focus, 1500):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Я знаю, что тебе весело, но, возможно, нам стоит попробовать что-нибудь другое, [RogueX.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Может быть, мы могли бы попробовать что-нибудь еще, [KittyX.Petname]?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Возможно, мы могли бы попробовать что-то другое, [EmmaX.Petname]?"
                    elif Ch_Focus is LauraX:
                            ch_l "Может, пришло время для чего-нибудь другого, [LauraX.Petname]?"
                    elif Ch_Focus is JeanX:
                            ch_j "Может, пришло время для чего-нибудь другого, [JeanX.Petname]?"
                    elif Ch_Focus is StormX:
                            ch_s "Уверена, тебе сейчас весело, но не могли бы мы попробовать что-нибудь другое?"
                    elif Ch_Focus is JubesX:
                            ch_v "Может, попробуем. . . что-нибудь другое?"
                    elif Ch_Focus is GwenX:
                            ch_g "Может, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Может быть, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Не могли бы мы заняться чем-нибудь другим?"
                    elif Ch_Focus is WandaX:
                            ch_w "Разве мы не можем заняться чем-нибудь другим?"
                    menu:
                        extend ""
                        "Закончить.":
                                "Вы заканчиваете веселье. . ."
                                jump Girl_FA_After
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Girl_FA_After
                        "Не-а, это так весело.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она возмущается, но позволяет вам продолжить."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call Girl_Pos_Reset(Ch_Focus)
                                    "Она кидает на вас сердитый взгляд и отстраняется."
                                    if Ch_Focus is DoreenX:
                                            ch_d "Тогда убери руки от моей попки."
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_FA_After
        #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10) #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5) #ch_d "Tic tock, [Ch_Focus.Petname]."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done") # "Ok, [Ch_Focus.Petname], breaktime."


label Girl_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Girl_Pos_Reset(Ch_Focus)

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.FondleA += 1
    $ Ch_Focus.Action -=1
    if Ch_Focus.PantsNum() < 6 or Ch_Focus.Upskirt:
        $ Ch_Focus.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ Ch_Focus.Addictionrate += 1

        call Partner_Like(Ch_Focus,2)

    if Ch_Focus.FondleA == 1:
            $ Ch_Focus.SEXP += 4
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                    if Ch_Focus is RogueX:
                            ch_r "Это было. . . приятно. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Хм. . . эм. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Это было. . . приятно. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Это было. . . приятно. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Это было. . . приятно. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Это было. . . приятно. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Это было. . . приятно. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Это было. . . приятно. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Это было. . . замечательно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Это было. . . здорово. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Хорошо, с этим покончено. . ."
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                    $ Ch_Focus.FaceChange("perplexed", 1)
                    if Ch_Focus is RogueX:
                            if not Player.Male:
                                ch_r "Ты повеселилась?"
                            else:
                                ch_r "Ты повеселился?"
                    elif Ch_Focus is KittyX:
                            if not Player.Male:
                                ch_k "Ты ведь не разочарована?"
                            else:
                                ch_k "Ты ведь не разочарован?"
                    elif Ch_Focus is EmmaX:
                            if not Player.Male:
                                ch_e "Что ж, ты определенно сорвала джекпот."
                            else:
                                ch_e "Что ж, ты определенно сорвал джекпот."
                    elif Ch_Focus is LauraX:
                            if not Player.Male:
                                ch_l "Ты удовлетворена?"
                            else:
                                ch_l "Ты удовлетворен?"
                    elif Ch_Focus is JeanX:
                            if not Player.Male:
                                ch_j "Ты получила то, что хотела?"
                            else:
                                ch_j "Ты получил то, что хотел?"
                    elif Ch_Focus is StormX:
                            ch_s "Полагаю, тебе понравилось. . ."
                    elif Ch_Focus is JubesX:
                            if not Player.Male:
                                ch_v "Ты удовлетворена?"
                            else:
                                ch_v "Ты удовлетворен?"
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе понравилось?"
                    elif Ch_Focus is BetsyX:
                            if not Player.Male:
                                ch_b "Ты удовлетворена?"
                            else:
                                ch_b "Ты удовлетворен?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Тебе этого достаточно?"
                    elif Ch_Focus is WandaX:
                            ch_w "Тебе этого достаточно?"
    $ Tempmod = 0
#    if Situation == "shift":
#        ch_d "Oh? What did you have in mind?"
    call Checkout
    return


# end Ch_Focus.Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Girl_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)

    if Ch_Focus.InsertA: #You've done it before
        $ Tempmod += 25
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 10
    if Ch_Focus.PantsNum() >= 6 or Ch_Focus.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 15
    if Ch_Focus.Lust > 85: #She's really horny
        $ Tempmod += 15
    if Ch_Focus.Lust > 95:
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
    if Ch_Focus.Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (4*Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 25
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10
    if Ch_Focus in (EmmaX,StormX) and Ch_Focus.Taboo and "public" not in Ch_Focus.History:
        $ Tempmod -= 20

    if "no insert ass" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no insert ass" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Statup("Obed", 90, 2)
            $ Ch_Focus.Statup("Obed", 70, 2)
            $ Ch_Focus.Statup("Inbt", 80, 2)
            $ Ch_Focus.Statup("Inbt", 30, 2)
            "Когда вы вводите палец внутрь, [Ch_Focus.Name] неожиданно сжимает анус, но вскоре расслабляет его."
            $ Ch_Focus.FaceChange("sexy")
            jump Girl_IA_Prep
        else:
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Statup("Love", 80, -2)
            $ Ch_Focus.Statup("Obed", 50, -3)
            if Ch_Focus is RogueX:
                    ch_r "Держи свои пальцы подальше, [RogueX.Petname]."
            elif Ch_Focus is KittyX:
                    ch_k "Воу, отвали, [KittyX.Petname]."
            elif Ch_Focus is EmmaX:
                    ch_e "Воу, назад, [EmmaX.Petname]."
            elif Ch_Focus is LauraX:
                    ch_l "Эй, назад, [LauraX.Petname]."
            elif Ch_Focus is JeanX:
                    ch_j "Ooo! Давай в другой раз, [JeanX.Petname]."
            elif Ch_Focus is StormX:
                    ch_s "Ты заходишь слишком далекоr, [StormX.Petname]."
            elif Ch_Focus is JubesX:
                    ch_v "Воу, назад, [JubesX.Petname]."
            elif Ch_Focus is GwenX:
                    ch_g "Воу, назад, [GwenX.Petname]."
            elif Ch_Focus is BetsyX:
                    ch_b "Ооох! Не надо совать туда пальцы, [BetsyX.Petname]!"
            elif Ch_Focus is DoreenX:
                    ch_d "Ой! Воу, держись оттуда подальше, [Ch_Focus.Petname]!"
            elif Ch_Focus is WandaX:
                    ch_w "Воу, туда нельзя, [WandaX.Petname]!"
            $ Tempmod = 0
            $ Trigger2 = 0
            return

    if "insert ass" in Ch_Focus.DailyActions and not Ch_Focus.Loose:
        $ Ch_Focus.FaceChange("bemused", 1)
        call AnyLine(Ch_Focus,"У меня все еще немного побаливает после прошлого раза, "+Ch_Focus.Petname+".")
    elif "insert ass" in Ch_Focus.DailyActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Тебе следует расслабиться. . .",
                    "Полегче.",
                    "Нежнее. . . нежнее. . .",
                    "Расслабься. . .",
                    "Ммм. . ."])
        else:
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Тебе следует расслабиться. . .",
                    "Тебе все мало?",
                    "Полегче.",
                    "Тебе следует расслабиться. . .",
                    "Расслабься. . .",
                    "Не торопись, я еще не отошла от прошлого раза.",
                    "Расслабься. . .",
                    "Ммм. . ."])
        call AnyLine(Ch_Focus,Line)

    if Approval >= 2:                                                                   #She's into it. . .
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Inbt", 60, 1)
        else:
            $ Ch_Focus.FaceChange("sexy", 1)
            $ Ch_Focus.Eyes = "closed"
            $ Ch_Focus.Statup("Love", 90, 1)
            $ Ch_Focus.Statup("Inbt", 50, 3)
            $ Ch_Focus.Statup("Lust", 200, 3)
        if Ch_Focus is RogueX:
                ch_r "Конечно, давай."
        elif Ch_Focus is KittyX:
                ch_k "Ладно, как скажешь."
        elif Ch_Focus is EmmaX:
                ch_e "Если тебе это так необходимо. . ."
        elif Ch_Focus is LauraX:
                ch_l "Конечно, звучит весело."
        elif Ch_Focus is JeanX:
                ch_j "Конечно, звучит весело."
        elif Ch_Focus is StormX:
                ch_s "С удовольствием. . ."
        elif Ch_Focus is JubesX:
                ch_v "Конечно, звучит весело."
        elif Ch_Focus is GwenX:
                ch_g "Конечно, звучит весело."
        elif Ch_Focus is BetsyX:
                ch_b "Понимаю."
        elif Ch_Focus is DoreenX:
                ch_d "Конечно."
        elif Ch_Focus is WandaX:
                ch_w "Конечно."
        $ Ch_Focus.Statup("Obed", 20, 1)
        $ Ch_Focus.Statup("Obed", 60, 1)
        $ Ch_Focus.Statup("Inbt", 70, 2)
        jump Girl_IA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("angry", 1)

        if "no insert ass" in Ch_Focus.RecentActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions and "no insert ass" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif "no insert ass" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif not Ch_Focus.InsertA:
            $ Ch_Focus.FaceChange("perplexed")
            if Ch_Focus is RogueX:
                    ch_r "Я. . . не думаю, что стоит. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Я. . . не думаю, что стоит. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Такое не в моем стиле. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Такое совсем не в моем стиле. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Такое совсем не в моем стиле. . ."
            elif Ch_Focus is StormX:
                    ch_s "Я не уверена насчет этого. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Такое совсем не в моем стиле. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Мне не особо это интересно. . . так что нет, спасибо."
            elif Ch_Focus is BetsyX:
                    ch_b "Благодарю, но нет. . . меня такое не особенно интересует."
            elif Ch_Focus is DoreenX:
                    ch_d "Мне не очень нравится такое. . . спасибо."
            elif Ch_Focus is WandaX:
                    ch_w "Мне совсем не нравится такое."
        else:
            $ Ch_Focus.FaceChange("bemused")
            call Sex_Basic_Dialog(Ch_Focus,"nothanks")
        menu:
            extend ""
            "Извини, забудь." if "no insert ass" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"noproblem")  # ch_r "Ok, no problem, [RogueX.Petname]."
                return
            "Может, в другой раз?" if "no insert ass" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy")
                call Sex_Basic_Dialog(Ch_Focus,"maybe")  # ch_d "I'll think about it, [Ch_Focus.Petname]."
                $ Ch_Focus.Statup("Love", 80, 2)
                $ Ch_Focus.Statup("Inbt", 70, 2)
                if Taboo:
                    $ Ch_Focus.RecentActions.append("tabno")
                    $ Ch_Focus.DailyActions.append("tabno")
                $ Ch_Focus.RecentActions.append("no insert ass")
                $ Ch_Focus.DailyActions.append("no insert ass")
                return
            "Думаю, тебе бы это очень понравилось. . .":
                if Approval:
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 90, 2)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                    call Sex_Basic_Dialog(Ch_Focus,"enjoyyes") #ch_d "Well, -maybe-. . ."
                    $ Ch_Focus.Statup("Inbt", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 40, 2)
                    jump Girl_IA_Prep
                else:
                    $ Ch_Focus.FaceChange("bemused")
                    call Sex_Basic_Dialog(Ch_Focus,"enjoyno") #ch_d "Probably not."

            "[[Все равно вставить палец]":                                               # Pressured into being fingered.
                $ Approval = ApprovalCheck(Ch_Focus, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("surprised", 1)
                    $ Ch_Focus.Statup("Love", 70, -5, 1)
                    $ Ch_Focus.Statup("Love", 200, -2)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #ch_w "Whoa!" ch_w ". . ." ch_w "Ok, ok, just get to it. . ."
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Obed", 50, 4)
                    $ Ch_Focus.Statup("Inbt", 80, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ Ch_Focus.Forced = 1
                    jump Girl_IA_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -15)
                    $ Ch_Focus.FaceChange("angry", 1)
                    $ Line = renpy.random.choice(["Что?",
                        "Эй!",
                        "М?",
                        "Воу!",
                        "Прошу прощения?",
                        "Хм."])
                    call AnyLine(Ch_Focus,Line)
                    "Она шлепает вас по руке."
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    if "no insert ass" in Ch_Focus.DailyActions:
        call Sex_Basic_Dialog(Ch_Focus,"noday") #"Stop asking."
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("angry", 1)
        if Ch_Focus is RogueX:
                ch_r "Эм, ни за что."
        elif Ch_Focus is KittyX:
                ch_k "Эм, ни за что."
        elif Ch_Focus is EmmaX:
                ch_e "Сегодня я не собираюсь заходить так далеко."
        elif Ch_Focus is LauraX:
                ch_l "Сегодня я не готова."
        elif Ch_Focus is JeanX:
                ch_j "Сегодня я не готова."
        elif Ch_Focus is StormX:
                ch_s "Ты заходишь слишком далеко."
        elif Ch_Focus is JubesX:
                ch_v "Сегодня я не готова."
        elif Ch_Focus is GwenX:
                ch_g "Эм. . . нет. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Ох, дорогуша, это так. . . нет. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Воу, эм. . . нет. . ."
        elif Ch_Focus is WandaX:
                ch_w "Это не по мне."
        if ApprovalCheck(Ch_Focus, 500, "I"):
                $ Ch_Focus.Statup("Lust", 80, 10)
        else:
                $ Ch_Focus.Statup("Lust", 50, 3)
        $ Ch_Focus.Statup("Obed", 50, -2)
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Taboo:
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.RecentActions.append("tabno")
        $ Ch_Focus.DailyActions.append("tabno")
        call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You picked a bad place for this. . ."
    elif Ch_Focus.InsertA:
        $ Ch_Focus.FaceChange("sad")
        if Ch_Focus is RogueX:
                ch_r "Думаю, тебе следует держать свои пальцы при себе."
        elif Ch_Focus is KittyX:
                ch_k "Я. . . не думаю, что стоит. . ."
        elif Ch_Focus is EmmaX:
                ch_e "Я. . . не думаю, что стоит. . ."
        elif Ch_Focus is LauraX:
                ch_l "Я. . . не думаю, что стоит. . ."
        elif Ch_Focus is JeanX:
                ch_j "Я. . . не думаю, что стоит. . ."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Мне такое не нравится."
        elif Ch_Focus is GwenX:
                ch_g "Я, эм. . . больше не хочу."
        elif Ch_Focus is BetsyX:
                ch_b "Это теперь. . . неуместно. . . "
        elif Ch_Focus is DoreenX:
                ch_d "Это могло бы быть. . . нет, неважно."
        elif Ch_Focus is WandaX:
                ch_w "Хех, нет."
    else:
        $ Ch_Focus.FaceChange("surprised")
        if Ch_Focus is RogueX:
                ch_r "Я. . . Не сюда!"
        elif Ch_Focus is KittyX:
                ch_k "Это. . . не круто."
        elif Ch_Focus is EmmaX:
                ch_e "Не сегодня, [EmmaX.Petname]."
        elif Ch_Focus is LauraX:
                ch_l "Не сегодня, [LauraX.Petname]."
        elif Ch_Focus is JeanX:
                ch_j "Не сегодня, [JeanX.Petname]."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Сегодня я точно не готова."
        elif Ch_Focus is GwenX:
                ch_g "Ни за что!"
        elif Ch_Focus is BetsyX:
                ch_b "Конечно же я откажусь!"
        elif Ch_Focus is DoreenX:
                ch_d "Конечно же я отказываюсь!"
        elif Ch_Focus is WandaX:
                ch_w "Хех, нет, спасибо."
        $ Ch_Focus.FaceChange()
    $ Ch_Focus.RecentActions.append("no insert ass")
    $ Ch_Focus.DailyActions.append("no insert ass")
    $ Tempmod = 0
    return


label Girl_IA_Prep: #Animation set-up
    if Trigger2 == "insert ass":
        return

    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"insert ass")
    else:
            call ViewShift(Ch_Focus,"pussy",0,"insert ass")

    if Situation == Ch_Focus:
            #Doreen auto-starts
            $ Situation = 0
            if (Ch_Focus.Legs and not Ch_Focus.Upskirt) or (Ch_Focus.Panties and not Ch_Focus.PantiesDown):
                #if she has some sort of top on. . .
                if ApprovalCheck(Ch_Focus, 1250, TabM = 1) or (Ch_Focus.SeenPussy and ApprovalCheck(Ch_Focus, 500) and not Taboo):
                        $ Ch_Focus.Upskirt = 1
                        $ Ch_Focus.PantiesDown = 1
                        $ Line = 0
                        if Ch_Focus.PantsNum() == 5:
                            $ Line = Ch_Focus.Name + "задирает свою юбку"
                        elif Ch_Focus.PantsNum() >= 6:
                            $ Line = Ch_Focus.Name + " стягивает с себя " + get_clothing_name(Ch_Focus.Legs_key, vin)
                        else:
                            $ Line = 0
                        if Ch_Focus.Panties:
                            if Line:
                                #wearing pants
                                "[Line] и сдвигает свои [get_clothing_name(Ch_Focus.Panties_key, vin)] в сторону."
                                "Затем она хватает вас за руку и прижимает вашу ладонь к своей попке, явно желая, чтобы вы взялись за дело."
                            else:
                                #no pants
                                "Она сдвигает свои [get_clothing_name(Ch_Focus.Panties_key, vin)] в сторону, а затем прижимает вашу ладонь к своей попке."
                                "Она явно хочет, чтобы вы взялись за дело."
                        else:
                            #pants but no panties
                            "[Line], а затем прижимает вашу ладонь к своей попке."
                            "Она явно хочет, чтобы вы взялись за дело."
                        call Girl_First_Bottomless(Ch_Focus,1)
                else:
                        "[Ch_Focus.Name] хватает вас за руку и прижимает вашу ладонь к своей попке, явно желая, чтобы вы взялись за дело."
            else:
                        "[Ch_Focus.Name] хватает вас за руку и прижимает вашу ладонь к своей попке, явно желая, чтобы вы взялись за дело."
            menu:
                "Что будете делать?"
                "Приступить.":
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 2)
                    "Вы нажимаете на ее анус пальцем."
                "Похвалить ее.":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    ch_p "Какая же ты развратная девочка, [Ch_Focus.Pet]."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "Вы нажимаете на ее анус пальцем."
                    $ Ch_Focus.Statup("Love", 85, 1)
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    "Вы одергиваете руку."
                    $ Ch_Focus.FaceChange("surprised")
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    ch_p "[Ch_Focus.Pet], давай не будем."
                    if Ch_Focus is JeanX:
                            $ JeanX.Statup("Love", 70, -2)
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] отстраняется."
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 1)
                    $ Ch_Focus.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ Ch_Focus.AddWord(1,"refused","refused")
                    return
            #end auto

    if not Ch_Focus.Forced and Situation != "auto":
        $ Tempmod = 0
        call Bottoms_Off(Ch_Focus)
        if "angry" in Ch_Focus.RecentActions:
            return

    if Ch_Focus.Plug:
            "Сначала уберите анальную пробку. . ."
            call Remove_Anal_Plug(Ch_Focus)

    $ Tempmod = 0
    if not Ch_Focus.InsertA:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -50)
            $ Ch_Focus.Statup("Obed", 70, 60)
            $ Ch_Focus.Statup("Inbt", 80, 35)
        else:
            $ Ch_Focus.Statup("Love", 90, 10)
            $ Ch_Focus.Statup("Obed", 70, 20)
            $ Ch_Focus.Statup("Inbt", 80, 25)

    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no insert ass")
    $ Ch_Focus.AddWord(0,"insert ass","insert ass")
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"lick ass")
    else:
            call ViewShift(Ch_Focus,"pussy",0,"lick ass")

label Girl_IA_Cycle: #Repeating strokes
    while Round > 0:
        call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"insert ass")
#        call Shift_Focus(Girl)
        $ Ch_Focus.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . .":
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_IA_Cycle
                        "В стиле минета" if Ch_Focus.Pose == "69":
                                    call Girl_BJ_Menu
                                    jump Girl_IA_Cycle

                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                        "Сменить вид":
                                    call ViewShift(Ch_Focus,"menu")
                                    jump Girl_IA_Cycle

                        "Другие варианты":
                                menu:
                                    "Дополнительное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ Ch_Focus.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Сменить основное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                    menu:
                                                        "Отпрянуть и снова начать ласкать.":
                                                                $ Situation = "pullback"
                                                                call Girl_IA_After
                                                                call Girl_Fondle_Ass
                                                        "Я хочу вылизать твой анус.":
                                                                $ Situation = "shift"
                                                                call Girl_IA_After
                                                                call Girl_Lick_Ass
                                                        "Просто начать вылизывать.":
                                                                $ Situation = "auto"
                                                                call Girl_IA_After
                                                                call Girl_Lick_Ass
                                                        "Я хочу вставить туда фаллоимитатор.":
                                                                $ Situation = "shift"
                                                                call Girl_IA_After
                                                                call Girl_Dildo("anal") #call Girl_Dildo_Ass
                                                                if "no dildo" not in Ch_Focus.RecentActions: #if she refuses, continue on, otherwise, skip back to previous label
                                                                        return
                                                        "Неважно":
                                                                jump Girl_IA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Переключить свое внимание" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Girl_IA_After
                                                call Offhand_Set
                                    "Переключить свое внимание (locked)" if not Trigger2:
                                                pass

                                    "Тройничек (locked)" if not Partner:
                                        pass
                                    "Тройничек" if Partner:
                                        menu:
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе" if Trigger == "lesbian":
                                                        call Les_Change(Ch_Focus)
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Пусть [Partner.Name] займется чем-нибудь другим":
                                                        call Three_Change(Ch_Focus)

                                            "Не бросай свое текущее занятие. . . (locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_IA_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_IA_Cycle
                                            "Неважно":
                                                        jump Girl_IA_Cycle

                                    "Показывать ее ноги" if not ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_IA_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_IA_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_IA_After
        #End menu (if Line)

        if Ch_Focus.Panties or Ch_Focus.PantsNum() >= 6 or Ch_Focus.HoseNum() >= 5: #This checks if Doreen wants to strip down.
                call Girl_Undress(Ch_Focus,"auto")

#        call Shift_Focus(Girl)
        call Sex_Dialog(Ch_Focus,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Ch_Focus)
                            if "angry" in Ch_Focus.RecentActions:
                                call Girl_Pos_Reset(Ch_Focus)
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_IA_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Doreen can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_IA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in Ch_Focus.RecentActions:#And Doreen is unsatisfied,
                                    "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                    menu:
                                        "Хотите завершить начатое?"
                                        "Продолжим еще немного.":
                                            $ Line = "Вы возвращаетесь к процессу"
                                        "С меня хватит.":
                                            "Вы заканчиваете веселье."
                                            jump Girl_IA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.InsertA):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Что ты там возишься?"
                    elif Ch_Focus is KittyX:
                            ch_k "Ты собираешься заканчивать?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Хм, ты собираешься. . ."
                    elif Ch_Focus is LauraX:
                            if not Player.Male:
                                ch_l "Аргх, ты таки добилась желаемого. . ."
                            else:
                                ch_l "Аргх, ты таки добился желаемого. . ."
                    elif Ch_Focus is JeanX:
                            if not Player.Male:
                                ch_j "Аргх, ты таки добилась желаемого. . ."
                            else:
                                ch_j "Аргх, ты таки добился желаемого. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Охх, осторожнее, осторожнее. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Веселишься?"
                    elif Ch_Focus is GwenX:
                            ch_g "Ох, эм, тебе нравится, да?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Вполне. . . вполне. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Это просто. . . что-то с чем-то. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Хмммм, ну ладно. . ."
        elif Ch_Focus.Lust >= 80:
                    pass
        elif Cnt == (15 + Ch_Focus.InsertA) and Ch_Focus.SEXP >= 15 and not ApprovalCheck(Ch_Focus, 1500):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "[RogueX.Petname], мне немного неприятно, может быть, мы могли бы попробовать что-нибудь другое?"
                    elif Ch_Focus is KittyX:
                            ch_k "[KittyX.Petname], мне немного больно, мне кажется, нам стоит попробовать что-нибудь другое."
                    elif Ch_Focus is EmmaX:
                            ch_e "[EmmaX.Petname], мне надоело, может, попробуем что-нибудь другое?"
                    elif Ch_Focus is LauraX:
                            ch_l "Может, немного разнообразим наши занятия?"
                    elif Ch_Focus is JeanX:
                            ch_j "Может, попробуем что-нибудь другое?"
                    elif Ch_Focus is StormX:
                            ch_s "Уверена, тебе сейчас весело, но не могли бы мы попробовать что-нибудь другое?"
                    elif Ch_Focus is JubesX:
                            ch_v "Может, попробуем. . . что-нибудь другое?"
                    elif Ch_Focus is GwenX:
                            ch_g "Может, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Может быть, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Не могли бы мы заняться чем-нибудь другим?"
                    elif Ch_Focus is WandaX:
                            ch_w "Разве мы не можем заняться чем-нибудь другим?"
                    menu:
                        extend ""
                        "Закончить.":
                                "Вы заканчиваете веселье. . ."
                                jump Girl_IA_After
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Girl_IA_After
                        "Не-а, это так весело.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она возмущается, но позволяет вам продолжить."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call Girl_Pos_Reset(Ch_Focus)
                                    "Она кидает на вас сердитый взгляд и отстраняется."
                                    if Ch_Focus is DoreenX:
                                            ch_d "Ну, тогда, наверное, я придумаю, чем можно еще заняться."
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_IA_After
        #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10) #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5) #ch_d "Tic tock, [Ch_Focus.Petname]."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done") # "Ok, [Ch_Focus.Petname], breaktime."

label Girl_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Girl_Pos_Reset(Ch_Focus)

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.InsertA += 1
    $ Ch_Focus.Action -=1
    $ Ch_Focus.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Ch_Focus.Addictionrate += 1

    call Partner_Like(Ch_Focus,2)

    if Ch_Focus.InsertA == 1:
            $ Ch_Focus.SEXP += 12
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                        if Ch_Focus is RogueX:
                                ch_r "Интересные. . . ощущения. . ."
                        elif Ch_Focus is KittyX:
                                ch_k "Это было странно. . ."
                        elif Ch_Focus is EmmaX:
                                if not Player.Male:
                                    ch_e "Ты меня очень удивила. . ."
                                else:
                                    ch_e "Ты меня очень удивил. . ."
                        elif Ch_Focus is LauraX:
                                ch_l "Это было довольно дико. . ."
                        elif Ch_Focus is JeanX:
                                ch_j "Это. . . было интересно. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Такого я не ожидала. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Это было довольно странно. . ."
                        elif Ch_Focus is GwenX:
                                ch_g "Это было. . . эм. . . интересно. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Это было. . . довольно занимательно. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "Это было. . . намного веселее, чем я представляла. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Это было. . . великолепно. . ."
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                        $ Ch_Focus.FaceChange("perplexed", 1)
                        if Ch_Focus is RogueX:
                                ch_r "Тебе понравилось?"
                        elif Ch_Focus is KittyX:
                                if not Player.Male:
                                    ch_k "Ну? Довольна?"
                                else:
                                    ch_k "Ну? Доволен?"
                        elif Ch_Focus is EmmaX:
                                if not Player.Male:
                                    ch_e "Это все, о чем ты мечтала?"
                                else:
                                    ch_e "Это все, о чем ты мечтал?"
                        elif Ch_Focus is LauraX:
                                ch_l "Тебе понравилось?"
                        elif Ch_Focus is JeanX:
                                ch_j "Уверена, тебе понравилось."
                        elif Ch_Focus is StormX:
                                ch_s "Тебе понравилось?"
                        elif Ch_Focus is JubesX:
                                ch_v "Тебе понравилось?"
                        elif Ch_Focus is GwenX:
                                ch_g "Тебе понравилось?"
                        elif Ch_Focus is BetsyX:
                                ch_b "Тебе этого достаточно?"
                        elif Ch_Focus is DoreenX:
                                ch_d "Тебе этого достаточно?"
                        elif Ch_Focus is WandaX:
                                ch_w "Тебе этого достаточно?"
    $ Tempmod = 0
#    if Situation == "shift":
#        ch_d "Oh? What did you have in mind?"
    call Checkout
    return


# end Ch_Focus.Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass
label Girl_Lick_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)
                                                                             # Will she let you lick? Modifiers
    if Ch_Focus.LickA: #You've done it before
        $ Tempmod += 20
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 10
    if Ch_Focus.PantsNum() >= 6 or Ch_Focus.HoseNum() >= 5: # she's got pants on.
        $ Tempmod -= 25
    if Ch_Focus.Lust > 95:
        $ Tempmod += 20
    elif Ch_Focus.Lust > 85: #She's really horny
        $ Tempmod += 15
    if Ch_Focus.Lust > 85 and Situation == "auto": #auto
        $ Tempmod += 10
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (4*Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 25
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10
    if Ch_Focus in (EmmaX,StormX) and Ch_Focus.Taboo and "public" not in Ch_Focus.History:
        $ Tempmod -= 20

    if "no lick ass" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no lick ass" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)

    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Inbt", 80, 3)
            $ Ch_Focus.Statup("Inbt", 40, 2)
            "Когда вы приседаете и начнаете вылизывать ее анус, [Ch_Focus.Name] вздрагивает и напрягается, но вскоре приходит в себя."
            $ Ch_Focus.FaceChange("sexy")
            jump Girl_LA_Prep
        else:
            $ Ch_Focus.FaceChange("surprised")
            $ Ch_Focus.Statup("Love", 80, -2)
            $ Ch_Focus.Statup("Obed", 50, -3)
            if Ch_Focus is RogueX:
                    ch_r "Эм, нет, я не совсем. . . не надо."
            elif Ch_Focus is KittyX:
                    ch_k "Эм, не делай этого. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "[EmmaX.Petname]! Не сейчас. . ."
            elif Ch_Focus is LauraX:
                    ch_l "[LauraX.Petname]! Нет. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Эй, [JeanX.Petname]!"
            elif Ch_Focus is StormX:
                    ch_s "[StormX.Petname]! Не сейчас. . ."
            elif Ch_Focus is JubesX:
                    ch_v "[JubesX.Petname]! Нет. . ."
            elif Ch_Focus is GwenX:
                    ch_g "[GwenX.Petname]! Нет. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "[BetsyX.Petname]! Нет. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "[Ch_Focus.Petname]! Нет. . ."
            elif Ch_Focus is WandaX:
                    ch_w "[WandaX.Petname]! Воу. . ."
            $ Tempmod = 0
            $ Trigger2 = 0
            return

    if "lick ass" in Ch_Focus.RecentActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                call AnyLine(Ch_Focus,"Мммм, опять? Что ж, пожалуй, я не против. . .")
        else:
                call AnyLine(Ch_Focus,"Снова? Ну ладно.")
        jump Girl_LA_Prep
    elif "lick ass" in Ch_Focus.DailyActions:
        $ Ch_Focus.FaceChange("sexy", 1)
        if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Тебе следует расслабиться. . .",
                    "Полегче.",
                    "Нежнее. . . нежнее. . .",
                    "Расслабься. . .",
                    "Ммм. . ."])
        else:
                $ Line = renpy.random.choice(["Тебе все еще мало?",
                    "Тебе следует расслабиться. . .",
                    "Тебе все мало?",
                    "Полегче.",
                    "Тебе следует расслабиться. . .",
                    "Расслабься. . .",
                    "Не торопись, я еще не отошла от прошлого раза.",
                    "Расслабься. . .",
                    "Ммм. . ."])
        call AnyLine(Ch_Focus,Line)


    if Approval >= 2:                                                                   #She's into it. . .
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
            $ Ch_Focus.Statup("Obed", 90, 2)
            $ Ch_Focus.Statup("Inbt", 60, 2)
        else:
            $ Ch_Focus.FaceChange("sexy", 1)
            $ Ch_Focus.Eyes = "closed"
            $ Ch_Focus.Statup("Love", 90, 1)
            $ Ch_Focus.Statup("Inbt", 60, 2)
            $ Ch_Focus.Statup("Lust", 200, 3)
        if Ch_Focus is RogueX:
                ch_r "Ооооооох. . ."
        elif Ch_Focus is KittyX:
                ch_k "Что-. . ."
        elif Ch_Focus is EmmaX:
                ch_e "Ммм. . . как неприлично."
        elif Ch_Focus is LauraX:
                ch_l "Ммм. . . как неприлично."
        elif Ch_Focus is JeanX:
                ch_j "Ммм. . . как неприлично."
        elif Ch_Focus is StormX:
                ch_s "Ммм. . . как неприлично."
        elif Ch_Focus is JubesX:
                ch_v "Ммм. . . как неприлично."
        elif Ch_Focus is GwenX:
                ch_g "Ммм. . . как это ненормально."
        elif Ch_Focus is BetsyX:
                ch_b "Ммм. . . какое извращение."
        elif Ch_Focus is DoreenX:
                ch_d "Ммм. . . это так дико."
        elif Ch_Focus is WandaX:
                ch_w "Ммм. . . какая дикость. . ."
        $ Ch_Focus.Statup("Obed", 20, 1)
        $ Ch_Focus.Statup("Obed", 60, 1)
        $ Ch_Focus.Statup("Inbt", 80, 2)
        jump Girl_LA_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("angry", 1)

        if "no lick ass" in Ch_Focus.RecentActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions and "no lick ass" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif "no lick ass" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"norecent")
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
        elif not Ch_Focus.LickA:
            $ Ch_Focus.FaceChange("bemused",1)
            if Ch_Focus.Love >= Ch_Focus.Obed and Ch_Focus.Love >= Ch_Focus.Inbt:
                    if Ch_Focus is RogueX:
                            if not Player.Male:
                                ch_r "Я как-то не уверена, что хочу, чтобы ты лизала меня там. . ."
                            else:
                                ch_r "Я как-то не уверена, что хочу, чтобы ты лизал меня там. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Я. . . я не уверена. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Ох, неужели мы уже на таком этапе?"
                    elif Ch_Focus is LauraX:
                            ch_l "Ох, мы уже на таком этапе отношений?"
                    elif Ch_Focus is JeanX:
                            ch_j "Ох, мы уже на таком этапе отношений?"
                    elif Ch_Focus is StormX:
                            ch_s "Ох, ты немного спешишь!"
                    elif Ch_Focus is JubesX:
                            ch_v "Что? О чем ты говоришь?"
                    elif Ch_Focus is GwenX:
                            ch_g "Почему ты этого так хочешь. . ?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Ты что, правда так этого хочешь. . ?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Не сомневаюсь, что ты этого хочешь. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Ты хочешь вылизать мою попку? . ."
            elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                    if Ch_Focus is RogueX:
                            if not Player.Male:
                                ch_r "Ты не должна лизать меня там. . . если не хочешь."
                            else:
                                ch_r "Ты не должен лизать меня там. . . если не хочешь."
                    elif Ch_Focus is KittyX:
                            ch_k "Тебе не нужно этого делать."
                    elif Ch_Focus is EmmaX:
                            ch_e "Хм, я и не знала, что тебе нравится такое."
                    elif Ch_Focus is LauraX:
                            ch_l "Хм, я и не знала, что тебе нравится такое."
                    elif Ch_Focus is JeanX:
                            ch_j "Мммм, тебе нравится такое?"
                    elif Ch_Focus is StormX:
                            ch_s "Хммм, интересное предложение. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Хм, я никогда даже не думала об этом. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе нравится такое?"
                    elif Ch_Focus is BetsyX:
                            ch_b "В чем твой интерес?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Тебе правда нравится такое?"
                    elif Ch_Focus is WandaX:
                            ch_w "Тебе правда нравится такое?"
            else:
                    call AnyLine(Ch_Focus,". . .")
        else:
            $ Ch_Focus.FaceChange("bemused")
            call Sex_Basic_Dialog(Ch_Focus,"nothanks")
        menu:
            extend ""
            "Извини, забудь." if "no lick ass" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"noproblem")  # ch_r "Ok, no problem, [RogueX.Petname]."
                return
            "Мне кажется, в следующий раз я смогу тебя убедить. . ." if "no lick ass" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy")
                call Sex_Basic_Dialog(Ch_Focus,"maybe")  # ch_d "I'll think about it, [Ch_Focus.Petname]."
                $ Ch_Focus.Statup("Love", 80, 2)
                $ Ch_Focus.Statup("Inbt", 70, 2)
                if Taboo:
                    $ Ch_Focus.RecentActions.append("tabno")
                    $ Ch_Focus.DailyActions.append("tabno")
                $ Ch_Focus.RecentActions.append("no lick ass")
                $ Ch_Focus.DailyActions.append("no lick ass")
                return
            "Думаю, тебе бы это очень понравилось. . .":
                if Approval:
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 90, 2)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                    call Sex_Basic_Dialog(Ch_Focus,"enjoyyes")#ch_d "Maybe I would. . ."
                    $ Ch_Focus.Statup("Inbt", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 40, 2)
                    jump Girl_LA_Prep
                else:
                    $ Ch_Focus.FaceChange("sexy")
                    call Sex_Basic_Dialog(Ch_Focus,"enjoyno") #ch_d "Probably not."

            "[[Все равно начать вылизывать]":                                               # Pressured into being licked.
                $ Approval = ApprovalCheck(Ch_Focus, 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -5, 1)
                    $ Ch_Focus.Statup("Love", 200, -2)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #ch_w "Whoa!" ch_w ". . ." ch_w "Ok, ok, just get to it. . ."
                    $ Ch_Focus.Statup("Obed", 50, 4)
                    $ Ch_Focus.Statup("Inbt", 80, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    if Approval < 2:
                        $ Ch_Focus.Forced = 1
                    jump Girl_LA_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -15)
                    $ Ch_Focus.FaceChange("angry", 1)
                    $ Line = renpy.random.choice(["Что?",
                        "Эй!",
                        "М?",
                        "Воу!",
                        "Прошу прощения?",
                        "Хм."])
                    call AnyLine(Ch_Focus,Line)
                    "Она отталкивает вашу голову назад."
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    if "no lick ass" in Ch_Focus.DailyActions:
        call Sex_Basic_Dialog(Ch_Focus,"noday") #"Stop asking."
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("sadside", 1)
        if Ch_Focus is RogueX:
                ch_r "Фу, ни за что."
        elif Ch_Focus is KittyX:
                ch_k "Фи, ни за что."
        elif Ch_Focus is EmmaX:
                ch_e "Я так не думаю."
        elif Ch_Focus is LauraX:
                ch_l "Я так не думаю."
        elif Ch_Focus is JeanX:
                ch_j "Я так не думаю."
        elif Ch_Focus is StormX:
                ch_s "Ты заходишь слишком далеко."
        elif Ch_Focus is JubesX:
                ch_v "Я так не думаю."
        elif Ch_Focus is GwenX:
                ch_g "Эм, это. . . нет. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Хм, это. . . нет. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Хм, это. . . нет. . ."
        elif Ch_Focus is WandaX:
                ch_w "Это не по мне."
        if ApprovalCheck(Ch_Focus, 500, "I"):
                $ Ch_Focus.Statup("Lust", 80, 10)
        else:
                $ Ch_Focus.Statup("Lust", 50, 3)
        $ Ch_Focus.Statup("Obed", 50, -2)
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Taboo:
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.RecentActions.append("tabno")
        $ Ch_Focus.DailyActions.append("tabno")
        call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You picked a bad place for this. . ."
    elif Ch_Focus.LickA:
        $ Ch_Focus.FaceChange("sad")
        if Ch_Focus is RogueX:
                ch_r "Извини, но держи свой язык при себе."
        elif Ch_Focus is KittyX:
                ch_k "Прости, больше не надо."
        elif Ch_Focus is EmmaX:
                ch_e "Прости, больше не надо."
        elif Ch_Focus is LauraX:
                ch_l "Извини, больше не надо."
        elif Ch_Focus is JeanX:
                ch_j "С нас хватит этого."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "ПИзвини, больше не надо."
        elif Ch_Focus is GwenX:
                ch_g "Я, эм. . . больше не хочу."
        elif Ch_Focus is BetsyX:
                ch_b "Это уже как-то неуместно."
        elif Ch_Focus is DoreenX:
                ch_d "Я совсем не в настроении для этого."
        elif Ch_Focus is WandaX:
                ch_w "Я не в настроении для этого."
    else:
        $ Ch_Focus.FaceChange("surprised")
        if Ch_Focus is RogueX:
                ch_r "Что?! Какой ужас!"
        elif Ch_Focus is KittyX:
                ch_k "Фи."
        elif Ch_Focus is EmmaX:
                ch_e "Прошу прощения, не сейчас."
        elif Ch_Focus is LauraX:
                ch_l "Извини, не сейчас."
        elif Ch_Focus is JeanX:
                ch_j "Извини, не сейчас."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю."
        elif Ch_Focus is JubesX:
                ch_v "Извини, не сейчас."
        elif Ch_Focus is GwenX:
                ch_g "Ни за что!"
        elif Ch_Focus is BetsyX:
                ch_b "Конечно же я откажусь!"
        elif Ch_Focus is DoreenX:
                ch_d "Конечно же я отказываюсь!"
        elif Ch_Focus is WandaX:
                ch_w "Хех, нет!"
        $ Ch_Focus.FaceChange()
    $ Ch_Focus.RecentActions.append("no lick ass")
    $ Ch_Focus.DailyActions.append("no lick ass")
    $ Tempmod = 0
    return

label Girl_LA_Prep: #Animation set-up
    if Trigger2 == "lick ass":
        return
    if not Ch_Focus.Forced and Situation != "auto":
        $ Tempmod = 0
        if Ch_Focus.PantsNum() >= 6:
            $ Tempmod = 15
        call Bottoms_Off(Ch_Focus)
        if "angry" in Ch_Focus.RecentActions:
            return
    $ Tempmod = 0
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"lick ass")
    else:
            call ViewShift(Ch_Focus,"pussy",0,"lick ass")
    if not Ch_Focus.LickA:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -30)
            $ Ch_Focus.Statup("Obed", 70, 40)
            $ Ch_Focus.Statup("Inbt", 80, 80)
        else:
            $ Ch_Focus.Statup("Love", 90, 35)
            $ Ch_Focus.Statup("Obed", 70, 25)
            $ Ch_Focus.Statup("Inbt", 80, 55)
    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

    $ Ch_Focus.Upskirt = 1
    if Ch_Focus.PantsNum() == 5:
        $ Ch_Focus.SeenPanties = 1
    if not Ch_Focus.Panties:
        call Girl_First_Bottomless(Ch_Focus,1)
    if Ch_Focus.Plug:
            "Сначала уберите анальную пробку. . ."
            call Remove_Anal_Plug(Ch_Focus)
    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no lick ass")

    $ Ch_Focus.AddWord(1,"lick","lick")
    $ Ch_Focus.AddWord(1,"ass","ass")
    $ Ch_Focus.AddWord(0,"lick ass","lick ass")
    if Ch_Focus.Pose and Ch_Focus.Pose != "kiss":
            call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"lick ass")
    else:
            call ViewShift(Ch_Focus,"pussy",0,"lick ass")
label Girl_LA_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round > 0:
        call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"lick ass")
#        call Shift_Focus(Girl)
        $ Ch_Focus.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . .":
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_LA_Cycle
                        "В стиле минета" if Ch_Focus.Pose == "69":
                                    call Girl_BJ_Menu
                                    jump Girl_LA_Cycle

                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                        "Сменить вид":
                                    call ViewShift(Ch_Focus,"menu")
                                    jump Girl_LA_Cycle

                        "Другие варианты":
                                menu:
                                    "Дополнительное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ Ch_Focus.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Сменить основное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                    menu:
                                                        "Перейти к ласкам.":
                                                                $ Situation = "pullback"
                                                                call Girl_LA_After
                                                                call Girl_Fondle_Ass
                                                        "Я хочу вставить палец внутрь.":
                                                                $ Situation = "shift"
                                                                call Girl_LA_After
                                                                call Girl_Insert_Ass
                                                        "Просто вставить палец внутрь [[не спрашивая].":
                                                                $ Situation = "auto"
                                                                call Girl_LA_After
                                                                call Girl_Insert_Ass
                                                        "Я хочу вставить туда фаллоимитатор.":
                                                                $ Situation = "shift"
                                                                call Girl_LA_After
                                                                call Girl_Dildo("anal") #call Girl_Dildo_Ass
                                                                if "no dildo" not in Ch_Focus.RecentActions: #if she refuses, continue on, otherwise, skip back to previous label
                                                                        return
                                                        "Неважно":
                                                                jump Girl_LA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Переключить свое внимание" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Girl_LA_After
                                                call Offhand_Set
                                    "Переключить свое внимание (locked)" if not Trigger2:
                                                pass

                                    "Тройничек (locked)" if not Partner:
                                        pass
                                    "Тройничек" if Partner:
                                        menu:
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе" if Trigger == "lesbian":
                                                        call Les_Change(Ch_Focus)
                                            "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Пусть [Partner.Name] займется чем-нибудь другим":
                                                        call Three_Change(Ch_Focus)

                                            "Не бросай свое текущее занятие. . . (locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_LA_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_LA_Cycle
                                            "Неважно":
                                                        jump Girl_LA_Cycle

                                    "Показывать ее ноги" if not ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet and (Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex"):
                                            $ ShowFeet = 0

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_LA_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_LA_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_LA_After
        #End menu (if Line)

        if Ch_Focus.Panties or Ch_Focus.PantsNum() >= 6 or Ch_Focus.HoseNum() >= 5: #This checks if Doreen wants to strip down.
                call Girl_Undress(Ch_Focus,"auto")

#        call Shift_Focus(Girl)
        call Sex_Dialog(Ch_Focus,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Ch_Focus)
                            if "angry" in Ch_Focus.RecentActions:
                                call Girl_Pos_Reset(Ch_Focus)
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_LA_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Doreen can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_LA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in Ch_Focus.RecentActions:#And Doreen is unsatisfied,
                                    "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                    menu:
                                        "Хотите завершить начатое?"
                                        "Продолжим еще немного.":
                                            $ Line = "Вы возвращаетесь к процессу"
                                        "С меня хватит.":
                                            "Вы заканчиваете веселье."
                                            jump Girl_LA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.LickA):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Что ты там возишься?"
                    elif Ch_Focus is KittyX:
                            ch_k "Ты собираешься заканчивать?"
                    elif Ch_Focus is EmmaX:
                            ch_e "В тебе так много энергии. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Кажется, тебе нравится. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Похоже, тебе нравится. . ."
                    elif Ch_Focus is StormX:
                            ch_s "В тебе полно энтузиазма. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Веселишься?"
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе, эм. . . нравится?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Это. . . интересно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Это. . . эм. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Вау, ты действительно это делаешь. . ."
        elif Ch_Focus.Lust >= 80:
                    pass
        elif Cnt == (15 + Ch_Focus.LickA) and Ch_Focus.SEXP >= 15 and not ApprovalCheck(Ch_Focus, 1500):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Я знаю, что тебе весело, но, возможно, нам стоит попробовать что-нибудь другое, [RogueX.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Может быть, мы могли бы попробовать что-нибудь еще, [KittyX.Petname]?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Возможно, мы могли бы попробовать что-то другое, [EmmaX.Petname]?"
                    elif Ch_Focus is LauraX:
                            ch_l "Может, пришло время для чего-нибудь другого, [LauraX.Petname]?"
                    elif Ch_Focus is JeanX:
                            ch_j "Может, пришло время для чего-нибудь другого, [JeanX.Petname]?"
                    elif Ch_Focus is StormX:
                            ch_s "Уверена, тебе сейчас весело, но не могли бы мы попробовать что-нибудь другое?"
                    elif Ch_Focus is JubesX:
                            ch_v "Может, попробуем. . . что-нибудь другое?"
                    elif Ch_Focus is GwenX:
                            ch_g "Может, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Может быть, мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Не могли бы мы заняться чем-нибудь другим?"
                    elif Ch_Focus is WandaX:
                            ch_w "Разве мы не можем заняться чем-нибудь другим?"
                    menu:
                        extend ""
                        "Закончить.":
                                "Вы заканчиваете веселье. . ."
                                jump Girl_LA_After
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Girl_LA_After
                        "Не-а, это так весело.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она возмущается, но позволяет вам продолжить."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call Girl_Pos_Reset(Ch_Focus)
                                    "Она кидает на вас сердитый взгляд и отстраняется."
                                    if Ch_Focus is RogueX:
                                            ch_r "Раз ты так ко мне относишься, я не нуждаюсь в твоей \"помощи\"."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Может тебе и весело, но я уже устала."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Хоть тебе и нравится, но я уже устала."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Мне скучно."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Ну, а -мне- скучно."
                                    elif Ch_Focus is StormX:
                                            ch_s "Что ж, как бы тебе не нравилось, мне нужно сделать перерыв."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Мне ужасно скучно. . ."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Эм. . . перестань."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Тогда, боюсь, мне придется тебя покинуть."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Тогда я в этом не учавствую, лижи кого-нибудь другого!"
                                    elif Ch_Focus is WandaX:
                                            ch_w "Ну, а -я- уже устала."
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_LA_After
        #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10) #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5) #ch_d "Tic tock, [Ch_Focus.Petname]."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done") # "Ok, [Ch_Focus.Petname], breaktime."

label Girl_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Girl_Pos_Reset(Ch_Focus)

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.LickA += 1
    $ Ch_Focus.Action -=1
    if Ch_Focus.PantsNum() < 6 or Ch_Focus.Upskirt:
        $ Ch_Focus.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ Ch_Focus.Addictionrate += 1

    call Partner_Like(Ch_Focus,2)

    if Ch_Focus.LickA == 1:
            $ Ch_Focus.SEXP += 15
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                    if Ch_Focus is RogueX:
                            ch_r "Тебе. . . понравилось?"
                    elif Ch_Focus is KittyX:
                            ch_k "Тебе. . . понравилось?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Это было. . . бодряще."
                    elif Ch_Focus is LauraX:
                            ch_l "Это. . . было интересно."
                    elif Ch_Focus is JeanX:
                            ch_j "Это. . . было интересно."
                    elif Ch_Focus is StormX:
                            ch_s "Это было. . . безусловно, интересно. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Это. . . было интересно."
                    elif Ch_Focus is GwenX:
                            ch_g "Эм. . . что сейчас произошло. . ?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Хммм. . . это было довольно. . .  интересно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Хм. . . это было. . . интересно. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Хех. . . это было. . . интересно. . ."
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                    $ Ch_Focus.FaceChange("perplexed", 1)
                    if Ch_Focus is RogueX:
                            ch_r "Тебе понравилось?"
                    elif Ch_Focus is KittyX:
                            if not Player.Male:
                                ch_k "Ты удоовлетворена?"
                            else:
                                ch_k "Ты удоовлетворен?"
                    elif Ch_Focus is EmmaX:
                            if not Player.Male:
                                ch_e "Это все, о чем ты мечтала?"
                            else:
                                ch_e "Это все, о чем ты мечтал?"
                    elif Ch_Focus is LauraX:
                            ch_l "Тебе было хорошо?"
                    elif Ch_Focus is JeanX:
                            ch_j "Тебе было хорошо?"
                    elif Ch_Focus is StormX:
                            ch_s "Тебе понравилось?"
                    elif Ch_Focus is JubesX:
                            ch_v "Тебе было хорошо?"
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе понравилось?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Тебе этого достаточно?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Тебе этого достаточно?"
                    elif Ch_Focus is WandaX:
                            ch_w "Тебе этого достаточно?"
    $ Tempmod = 0
#    if Situation == "shift":
#        ch_d "Oh? What did you have in mind?"
    call Checkout
    return

# end Ch_Focus.Lick Ass /////////////////////////////////////////////////////////////////////////////
