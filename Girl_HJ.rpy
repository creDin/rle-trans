## Ch_Focus.Handjob //////////////////////////////////////////////////////////////////////
label Girl_Handjob:
    if not Player.Male:
            call Girl_Finger
            return
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)
    if Ch_Focus.Hand >= 7: # She loves it
        $ Tempmod += 10
    elif Ch_Focus.Hand >= 3: #You've done it before several times
        $ Tempmod += 7
    elif Ch_Focus.Hand: #You've done it before
        $ Tempmod += 3
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 2

    if Ch_Focus.Addict >= 75 and Ch_Focus.Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    if Ch_Focus.Addict >= 75:
        $ Tempmod += 5

    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (3*Ch_Focus.Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 40
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10

    if "no hand" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no hand" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not Ch_Focus.Hand and "no hand" not in Ch_Focus.RecentActions:
        $ Ch_Focus.FaceChange("confused", 2)
        if Ch_Focus is RogueX:
                ch_r "Ты хочешь, чтобы я поласкала твой член своей рукой?"
        elif Ch_Focus is KittyX:
                ch_k "Хочешь воспользоваться моей рукой?"
        elif Ch_Focus is EmmaX:
                ch_e "Ты хочешь, чтобы я сделала тебе приятно?"
        elif Ch_Focus is LauraX:
                ch_l "Хм, значит ты хочешь, чтобы я тебе подрочила. . ."
        elif Ch_Focus is JeanX:
                ch_j "Хмм, значит, хочешь чтобы тебе подрочили. . ."
        elif Ch_Focus is StormX:
                ch_s "Ты хочешь, чтобы я подрочила тебе?"
        elif Ch_Focus is JubesX:
                ch_v "О, ты хочешь, чтобы я тебе подрочила. . ."
        elif Ch_Focus is GwenX:
                ch_g "Ох, ты хочешь. . . чтобы я тебе подрочила. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Ох, ты хочешь. . . чтобы я тебе подрочила. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Ох, ты хочешь. . . чтобы я тебе подрочила. . ."
        elif Ch_Focus is WandaX:
                ch_w "Значит ты хочешь, чтобы я тебе подрочила. . ."
        $ Ch_Focus.Blush = 1

    if not Ch_Focus.Hand and Approval:
        #First time dialog
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad",1)
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
        elif Ch_Focus.Love >= (Ch_Focus.Obed + Ch_Focus.Inbt):
            #Love highest
            $ Ch_Focus.FaceChange("sexy",1)
            $ Ch_Focus.Brows = "sad"
            $ Ch_Focus.Mouth = "smile"
            if Ch_Focus is RogueX:
                    ch_r "Ну, я никогда по-настоящему не могла прикасаться к людям, не опустошая их, это могут быть интересные впечатления. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Думаю, это может быть интересно. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Полагаю, ты кое-что да заслужил. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Тебе понравится. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Ну, думаю, это может быть не так уж плохо. . ."
            elif Ch_Focus is StormX:
                    ch_s "Возможно, мне даже понравится. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Я могла бы сделать это для тебя. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Это может быть весело. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Это может быть довольно весело. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Это может быть довольно весело. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Это может быть забавно. . ."
        elif Ch_Focus.Obed >= Ch_Focus.Inbt:
            #obedience highest
            $ Ch_Focus.FaceChange("normal",1)
            if Ch_Focus in (EmmaX,StormX,BetsyX):
                    call AnyLine(Ch_Focus,"Если ты этого хочешь, "+Ch_Focus.Petname+". . .")
            else:
                    call AnyLine(Ch_Focus,"Если это то, чего ты хочешь, "+Ch_Focus.Petname+". . .")
        else: # Uninhibited
            #inhibition highest
            $ Ch_Focus.FaceChange("lipbite",1)
            $ Line = renpy.random.choice(["Хех. . ." ,
                "Хм, это может быть весело. . .",
                "Думаю, это я могу. . .",
                "Пожалуй, я могу это сделать. . .",
                "Хмм. . ."])
            call AnyLine(Ch_Focus,Line)

    elif Approval:
        #Second time+ dialog
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
            if Ch_Focus is RogueX:
                    ch_r "Это действительно то, чего ты хочешь?"
            elif Ch_Focus is KittyX:
                    ch_k "Это все, чего ты хочешь, да?"
            elif Ch_Focus is EmmaX:
                    ch_e "И не более?"
            elif Ch_Focus is LauraX:
                    ch_l "И ничего более?"
            elif Ch_Focus is JeanX:
                    ch_j "И это все, чего ты хочешь?"
            elif Ch_Focus is StormX:
                    ch_s "И ничего более?"
            elif Ch_Focus is JubesX:
                    ch_v "Тебе нужны только мои руки?"
            elif Ch_Focus is GwenX:
                    ch_g "И все?"
            elif Ch_Focus is BetsyX:
                    ch_b "И ничего более?"
            elif Ch_Focus is DoreenX:
                    ch_d "И на этом все закончится?"
            elif Ch_Focus is WandaX:
                    ch_w "-и все?"
        elif not Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabyes") #"This -would- be a better place for it. . ."
        elif "hand" in Ch_Focus.DailyActions:
            $ Ch_Focus.FaceChange("sexy", 1)
            if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Снова?",
                    "Я могу натереть себе мозоли.",
                    "Тебе все мало?",
                    "У меня сильно болит рука после прошлого раза.",
                    "Моя рука немного побаливает прошлого раза."])
            else:
                $ Line = renpy.random.choice(["Тебе хочется большего?",
                    "Значит, ты хочешь еще одну дрочку?",
                    "Тебе хочется. . . [трясет кулачком]?",
                    "Желаешь еще одной мастурбации?"])
            call AnyLine(Ch_Focus,Line)
            if "hand" in Ch_Focus.RecentActions:
                    jump Girl_HJ_Prep
        elif Ch_Focus.Hand < 3:
            $ Ch_Focus.FaceChange("sexy", 1)
            $ Ch_Focus.Brows = "confused"
            $ Ch_Focus.Mouth = "kiss"
            $ Line = renpy.random.choice(["Значит, желаешь, чтобы тебе снова подрочили?",
                    "Хммм, похоже, у меня волшебные пальчики. . .",
                    "Тебе так понравилось в прошлый раз?. . .",
                    "Кажется, тебе это нравится. . .",
                    "Думаю, ты начинаешь привыкать. . .",
                    "В прошлый раз тебе понравилось?. . .",
                    "Думаю, у меня это неплохо получается. . .",
                    "Кажется, тебе нравится. . .",
                    "Похоже, тебе это очень нравится. . .",
                    "Похоже, тебе это нравится. . .",
                    "По тебе видно, что тебе это нравится. . ."])
            call AnyLine(Ch_Focus,Line)
        else:
            $ Ch_Focus.FaceChange("sexy", 1)
            $ Ch_Focus.ArmPose = 2
            if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Хочешь еще?",
                    "Значит, ты хочешь еще?",
                    "Еще? [покачивает кулаком верх-вниз]",
                    "О, ты хочешь немного внимания?"])
            else:
                $ Line = renpy.random.choice(["Желаешь еще?",
                    "Значит, тебе настолько это нравится?",
                    "Хочешь. . . [потряхивает кулаком]?",
                    "Желаешь, чтобы я еще разок подрочила тебе?"])
            call AnyLine(Ch_Focus,Line)
        $ Line = 0

    if Ch_Focus is JeanX and ApprovalCheck(JeanX, 1000) and (Approval < 2 or "psysex" not in JeanX.History):
            #sees if you're up for psychic handy
            call Psychic_Sex(JeanX)

    if Approval >= 2:
        #She's into it. . .
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Inbt", 60, 1)
            if Ch_Focus in (EmmaX,StormX,BetsyX):
                    call AnyLine(Ch_Focus,"Хорошо.")
            else:
                    call AnyLine(Ch_Focus,"Ладно.")
        else:
            $ Ch_Focus.FaceChange("sexy", 1)
            $ Ch_Focus.Statup("Love", 90, 1)
            $ Ch_Focus.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Пожалуй, это я могу.",
                "Ох, ладно.",
                "Хорошо.",
                "Пожалуй, это я могу. . .",
                "Ох, ладно. . . [Подзывает вас жестом].",
                "Ох, хорошо."])
            call AnyLine(Ch_Focus,Line)
            $ Line = 0
        $ Ch_Focus.Statup("Obed", 20, 1)
        $ Ch_Focus.Statup("Obed", 60, 1)
        $ Ch_Focus.Statup("Inbt", 70, 2)
        jump Girl_HJ_Prep

    else:
        #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("angry")
        if "no hand" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"noday") #"I don't think I've been confusing on this one."
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday") #"Like I said, I don't do that sort of thing. . . -in public-."
        elif not Ch_Focus.Hand:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "Я совсем не хочу к нему прикасаться, [RogueX.Petname]. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Я не уверена, [KittyX.Petname]. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Ты в этом уверен, [EmmaX.Petname]?. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Ты серьезно, [LauraX.Petname]. . ?"
            elif Ch_Focus is JeanX:
                    ch_j "Серьезно, [JeanX.Petname]. . ?"
            elif Ch_Focus is StormX:
                    ch_s "Ты уверен, [StormX.Petname]? . ."
            elif Ch_Focus is JubesX:
                    ch_v "Я не уверена. . . [JubesX.Petname]? . ."
            elif Ch_Focus is GwenX:
                    ch_g "Серьезно, [GwenX.Petname]. . ?"
            elif Ch_Focus is BetsyX:
                    ch_b "Ох, будь серьезней, [BetsyX.Petname]. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Да ладно, ты серьезно. . . [Ch_Focus.Petname]? . ."
            elif Ch_Focus is WandaX:
                    ch_w "Не мог придумать ничего лучше, [WandaX.Petname]? . ."
        else:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "Нет, не сейчас, [RogueX.Petname]. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Не сейчас, ладно?"
            elif Ch_Focus is EmmaX:
                    ch_e "Сейчас я бы предпочла этого не делать."
            elif Ch_Focus is LauraX:
                    ch_l "Нет."
            elif Ch_Focus is JeanX:
                    ch_j "Не-а."
            elif Ch_Focus is StormX:
                    ch_s "Сейчас я бы предпочла этого не делать."
            elif Ch_Focus is JubesX:
                    ch_v "Я не уверена. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Не."
            elif Ch_Focus is BetsyX:
                    ch_b "Я бы предпочла этого не делать."
            elif Ch_Focus is DoreenX:
                    ch_d "Я. . . не хочу."
            elif Ch_Focus is WandaX:
                    ch_w "Хмм. . . я так не думаю."
        menu:
            extend ""
            "Извини, забудь." if "no hand" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"noproblem") #"Oh, thanks, I understand. . ."
                return
            "Может, в другой раз?" if "no hand" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"maybe") #". . . maybe."
                $ Ch_Focus.Statup("Love", 80, 2)
                $ Ch_Focus.Statup("Inbt", 70, 2)
                if Ch_Focus.Taboo:
                    $ Ch_Focus.RecentActions.append("tabno")
                    $ Ch_Focus.DailyActions.append("tabno")
                $ Ch_Focus.RecentActions.append("no hand")
                $ Ch_Focus.DailyActions.append("no hand")
                return
            "Я был бы тебе очень признателен. . .":
                if Approval:
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 90, 2)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                    $ Ch_Focus.Statup("Inbt", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 40, 2)
                    if Ch_Focus in (EmmaX,StormX,BetsyX):
                            $ Line = renpy.random.choice(["Пожалуй, я даже соглашусь.",
                                "Ох, хорошо.",
                                "Ладно.",
                                "Пожалуй, можно. . .",
                                "Ох, ясно. . . [Она жестом подзывает вас].",
                                "Конечно."])
                    else:
                            $ Line = renpy.random.choice(["Может, я все же могу это устроить.",
                                "Ох, хорошо.",
                                "Круто, дай-ка я взгляну на него.",
                                "Конечно, доставай.",
                                "Ладно.",
                                "Что ж, доставай.",
                                "Л-адно.",
                                "Хорошо.",
                                "Может, я все же могу это устроить. . .",
                                "Ох. . . [Она жестом подзывает вас].",
                                "Ладно, если так."])
                    call AnyLine(Ch_Focus,Line)
                    $ Line = 0
                    jump Girl_HJ_Prep
                else:
                    pass

            "Давай, приступай.":                                            # Pressured into it
                $ Approval = ApprovalCheck(Ch_Focus, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -5, 1)
                    $ Ch_Focus.Statup("Love", 200, -2)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #"Oh, fine."
                    $ Ch_Focus.Statup("Obed", 50, 4)
                    $ Ch_Focus.Statup("Inbt", 80, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    $ Ch_Focus.Forced = 1
                    jump Girl_HJ_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -15)
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    #She refused all offers.
    $ Ch_Focus.ArmPose = 1
    if "no hand" in Ch_Focus.DailyActions:
        $ Ch_Focus.FaceChange("angry", 1)
        call Sex_Basic_Dialog(Ch_Focus,"nothanks") #"Quit bugging me."
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("angry", 1)
        if Ch_Focus is RogueX:
                ch_r "Я не такая!"
        elif Ch_Focus is KittyX:
                ch_k "Даже если бы у тебя был полметровый ствол."
                $ KittyX.FaceChange("surprised", 2)
                h_k "Блин, я не это хотела сказать. . ."
                $ KittyX.FaceChange("angry", 1)
                ch_k "Да что я вообще оправдываюсь, ты все прекрасно понял!"
        elif Ch_Focus is EmmaX:
                ch_e "Ты хочешь слишком многого."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Меня это не устраивает."
        elif Ch_Focus is JubesX:
                ch_v "Неее-а."
        elif Ch_Focus is GwenX:
                ch_g "Эм. . . нет."
        elif Ch_Focus is BetsyX:
                ch_b ". . . Я бы предпочла этого не делать."
        elif Ch_Focus is DoreenX:
                ch_d ". . . Не думаю, что хочу этого. . ."
        elif Ch_Focus is WandaX:
                ch_w ". . . Мне такое не по вкусу."
        $ Ch_Focus.Statup("Lust", 200, 5)
        if Ch_Focus.Love > 300:
                $ Ch_Focus.Statup("Love", 70, -2)
        $ Ch_Focus.Statup("Obed", 50, -2)
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Taboo:                             # she refuses and this is too public a place for her
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.DailyActions.append("tabno")
        call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You can't do that here!"
        $ Ch_Focus.Statup("Lust", 200, 5)
        $ Ch_Focus.Statup("Obed", 50, -3)
    elif Ch_Focus.Hand:
        $ Ch_Focus.FaceChange("sad")
        if Ch_Focus is RogueX:
                ch_r "Думаю, на этот раз ты должен справиться сам. . ."
        elif Ch_Focus is KittyX:
                ch_k "Я не в настроение сегодня. . ."
        elif Ch_Focus is EmmaX:
                ch_e "Я бы не хотела подобного. . ."
        elif Ch_Focus is LauraX:
                ch_l "Мне сегодня не хочется. . ."
        elif Ch_Focus is JeanX:
                ch_j "Мне сегодня не хочется. . ."
        elif Ch_Focus is StormX:
                ch_s ". . . Я бы предпочла этого не делать."
        elif Ch_Focus is JubesX:
                ch_v "Не сейчас. . ."
        elif Ch_Focus is GwenX:
                ch_g "Эм, не сегодня. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Меня это не интересует. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Мне. . . сейчас не хочется. . ."
        elif Ch_Focus is WandaX:
                ch_w "Не сейчас, ладно?"
    else:
        $ Ch_Focus.FaceChange("normal", 1)
        if Ch_Focus is RogueX:
                ch_r "Я бы этого не хотела."
        elif Ch_Focus is KittyX:
                ch_k "Я не хочу прикасаться к нему."
        elif Ch_Focus is EmmaX:
                ch_e "Нет, я так не думаю, [EmmaX.Petname]."
        elif Ch_Focus is LauraX:
                ch_l "Я бы предпочла не прикасаться к нему."
        elif Ch_Focus is JeanX:
                ch_j "Я бы предпочла не трогать его."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю, [StormX.Petname]."
        elif Ch_Focus is JubesX:
                ch_v "Я не в настроении."
        elif Ch_Focus is GwenX:
                ch_g "Эм, нет, спасибо."
        elif Ch_Focus is BetsyX:
                ch_b "Я бы. . . предпочла этим не заниматься."
        elif Ch_Focus is DoreenX:
                ch_d ". . . Не думаю, что хочу этого. . ."
        elif Ch_Focus is WandaX:
                ch_w "У меня нет никакого желания делать это."
    $ Ch_Focus.RecentActions.append("no hand")
    $ Ch_Focus.DailyActions.append("no hand")
    $ Tempmod = 0
    return


label Girl_HJ_Prep:
    if not Player.Male:
            call Girl_Finger_Prep
            return
    if Trigger2 == "hand":
        return

    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)

    $ Ch_Focus.FaceChange("sexy")
    if Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("sad")
    elif not Ch_Focus.Hand:
        $ Ch_Focus.Brows = "confused"
        $ Ch_Focus.Eyes = "sexy"
        $ Ch_Focus.Mouth = "smile"

    call Seen_First_Peen(Ch_Focus,Partner,React=Situation)
    call expression Ch_Focus.Tag + "_HJ_Launch" pass ("L") #call Girl_HJ_Launch("L")

    if Situation == Ch_Focus:
            #Girl auto-starts
            $ Situation = 0
            if Trigger2 == "jackin":
                "[Ch_Focus.Name] откидывает вашу руку в сторону и начинает ласкать ваш член."
            else:
                "[Ch_Focus.Name] одаривает вас озорной улыбкой и начинает ласкать ваш член."
            menu:
                "Что будете делать?"
                "Ничего не делать.":
                    $ Ch_Focus.Statup("Inbt", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 30, 2)
                    "[Ch_Focus.Name] продолжает свои действия."
                "Похвалить ее.":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Inbt", 70, 3)
                    ch_p "Ооох, [Ch_Focus.Pet], это так приятно."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] продолжает свои действия."
                    $ Ch_Focus.Statup("Love", 80, 1)
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    $ Ch_Focus.FaceChange("surprised")
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    ch_p "[Ch_Focus.Name], давай не сейчас."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] отстраняется."
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 1)
                    $ Ch_Focus.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ Ch_Focus.AddWord(1,"refused","refused")
                    return

    if not Ch_Focus.Hand:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -20)
            $ Ch_Focus.Statup("Obed", 70, 25)
            $ Ch_Focus.Statup("Inbt", 80, 30)
        else:
            $ Ch_Focus.Statup("Love", 90, 5)
            $ Ch_Focus.Statup("Obed", 70, 20)
            $ Ch_Focus.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no hand")
    $ Ch_Focus.RecentActions.append("hand")
    $ Ch_Focus.DailyActions.append("hand")

label Girl_HJ_Cycle:
    while Round > 0:
#        call Shift_Focus(Girl)
        call expression Ch_Focus.Tag + "_HJ_Launch" pass ("L") #call Girl_HJ_Launch
        $ Ch_Focus.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . ." if Speed:
                                    pass

                        "Начать? . ." if not Speed:
                                    # Modification mode
                                    if is_playing_music(audio.girl_handjob):
                                        $ play_music(name=audio.girl_handjob, loop=True)
                                    # -----------------

                                    $ Speed = 1

                        "Быстрее. . ." if Speed < 2:
                                    $ Speed = 2
                                    "Вы просите ее немного ускориться."
                        "Быстрее. . . (locked)" if Speed >= 2:
                                    pass

                        "Помедленнее. . ." if Speed:
                                    $ Speed -= 1
                                    "Вы просите ее немного сбавить темп."
                        "Помедленнее. . . (locked)" if not Speed:
                                    pass
                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0

                        "Другие варианты":
                                menu:
                                    "Начать также ласкать ее грудь." if Trigger2 != "fondle breasts":
                                            if Ch_Focus.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "Вы начинаете ласкать ее грудь."
                                                $ Ch_Focus.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Сменить основное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                    menu:
                                                        "Может, отсосешь?":
                                                                    if Ch_Focus.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Girl_HJ_After
                                                                        call Girl_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")

                                                        "Может, подрочишь мне сиськами?":
                                                                    if Ch_Focus.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Girl_HJ_After
                                                                        call Girl_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        "Неважно":
                                                                jump Girl_HJ_Cycle
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

                                            "Не бросай свое текущее занятие. . .(locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_HJ_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_HJ_Cycle
                                            "Неважно":
                                                        jump Girl_HJ_Cycle

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife
                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_HJ_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_HJ_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_HJ_After
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
                                call expression Ch_Focus.Tag + "_HJ_Reset"
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2 and Ch_Focus.SEXP >= 20:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_HJ_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Girl can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_HJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in Ch_Focus.RecentActions:#And Ch_Focus is unsatisfied,
                                "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                menu:
                                    "Хотите завершить начатое?"
                                    "Продолжим еще немного.":
                                        $ Line = "Вы возвращаетесь к процессу"
                                    "С меня хватит.":
                                        "Вы заканчиваете веселье."
                                        jump Girl_HJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ Ch_Focus.Brows = "angry"
                    if Ch_Focus is RogueX:
                            ch_r "Я уже все себе натерла, [RogueX.Petname]. Давай займемся чем-нибудь другим?"
                    elif Ch_Focus is KittyX:
                            ch_k "Ай, у меня руку сводит, мы можем[KittyX.like]сделать перерыв?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Хм, похоже, у меня руку сводит."
                            ch_e "Не возражаешь, если мы сделаем перерыв?"
                    elif Ch_Focus is LauraX:
                            ch_l "Хммм, это скучно. Может, прервемся?"
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно, мне стало скучно. Мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is StormX:
                            ch_s "Хм, похоже, у меня руку сводит."
                            ch_s "Не возражаешь, если мы сделаем перерыв?"
                    elif Ch_Focus is JubesX:
                            ch_v "Моя рука подустала, может мы могли бы заняться чем-нибудь другим?"
                    elif Ch_Focus is GwenX:
                            ch_g "У меня болит рука."
                            ch_g ". . . мы можем сделать перерыв?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Боюсь, у меня уже немного сводит руку. . ."
                            ch_b ". . . не могли бы мы сделать перерыв?"
                    elif Ch_Focus is DoreenX:
                            ch_d "По-моему, у меня руку сводит. . ."
                            ch_d ". . . не могли бы мы сделать перерыв?"
                    elif Ch_Focus is WandaX:
                            ch_w "Ладно, по-моему, у меня руку сводит. . ."
                            ch_w ". . . давай сделаем перерыв?"
                    menu:
                        extend ""
                        "Как насчет отсоса?" if Ch_Focus.Action and MultiAction:
                                $ Situation = "shift"
                                call Girl_HJ_After
                                call Girl_Blowjob
                        "Закончить." if Player.FocusX:
                                "Вы расслабляетесь. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Girl_HJ_Cycle
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                call expression Ch_Focus.Tag + "_HJ_Reset"
                                $ Situation = "shift"
                                jump Girl_HJ_After
                        "Нет, давай за работу.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она ворчит, но возвращается к работе."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    "Она сердито смотрит на вас, отпускает ваш член и отстраняется."
                                    if Ch_Focus is RogueX:
                                            ch_r "Занимайся чем хочешь, но без меня."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Послушай, если ты будешь вести себя[KittyX.Like]как мудак, то у меня найдутся дела повожнее."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Ты знаешь, у меня есть дела поважнее."
                                    elif Ch_Focus is LauraX:
                                            ch_l "У меня есть дела поважнее."
                                    elif Ch_Focus is JeanX:
                                            ch_j "У меня есть дела поважнее."
                                    elif Ch_Focus is StormX:
                                            ch_s "Возможно, некоторое время в одиночестве поможет тебе переосмыслить свой выбор."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Ни за что, заканчивай сам."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Ну, если такова твоя реакция, я пошла. . ."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Боюсь, тогда тебе придется развлекаться без меня. . ."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Тогда я оставлю тебя. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Тогда справляйся сам."
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_HJ_After
        elif Cnt == 10 and Ch_Focus.SEXP <= 100 and not ApprovalCheck(Ch_Focus, 1200, "LO"):
                            $ Ch_Focus.Brows = "confused"
                            $ Line = renpy.random.choice(["Ты уже скоро? Мне становится немного больно.",
                                    "Мы можем уже закончить? У меня начинает болеть рука.",
                                    "Ты уверен, что не хочешь заняться чем-нибудь другим?",
                                    "Ты скоро?",
                                    "Приятно, правда?",
                                    "Ты уверен, что не хочешь заняться ничем другим?",
                                    "Тебе приятно?"])
                            call AnyLine(Ch_Focus,Line)
        #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10)  #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5)  #ch_d "Tic tock, [Ch_Focus.Petname]."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done")  # ch_d "Ok, [Ch_Focus.Petname], breaktime."

label Girl_HJ_After:
    # Modification mode
    $ play_music()
    $ play_sound()
    # -----------------

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.Hand += 1
    $ Ch_Focus.Action -=1
    $ Ch_Focus.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Ch_Focus.Addictionrate += 1
    $ Ch_Focus.Statup("Lust", 90, 5)

    call Partner_Like(Ch_Focus,1)

    if (Ch_Focus.Tag + " Handi-Queen") in Achievements: #test this
            pass
    elif Ch_Focus.Hand >= 10:
            $ Ch_Focus.FaceChange("smile", 1)
            if Ch_Focus is RogueX:
                    ch_r "Наверное, теперь ты можешь звать меня \"Королевой Дрочки.\""
            elif Ch_Focus is KittyX:
                    ch_k "Я вроде как стала[KittyX.like]\"Королевой Дрочки\" или типа того."
            elif Ch_Focus is EmmaX:
                    ch_e "Теперь меня, похоже, также можно звать \"королевой\" дрочки."
            elif Ch_Focus is LauraX:
                    ch_l "Мне кажется, я стала гораздо опытнее, [LauraX.Petname]."
            elif Ch_Focus is JeanX:
                    ch_j "Похоже, в последнее время мы только этим и занимаемся. . ."
            elif Ch_Focus is StormX:
                    ch_s "Кажется, я стала \"королевой\" хороших дрочек."
            elif Ch_Focus is JubesX:
                    ch_v "Ого, я так много дрочила. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Думаю, я достигла максимума в дереве навыков \"мастурбация\"."
            elif Ch_Focus is BetsyX:
                    ch_b "Думаю, я стала настоящим экспертом."
            elif Ch_Focus is DoreenX:
                    ch_d "Возможно, мне придется сменить имя на \"Девушка Золотые Ручки.\""
            elif Ch_Focus is WandaX:
                    ch_w "Кажется, я теперь отлично понимаю, как сделать тебе приятно."
            $ Achievements.append(Ch_Focus.Tag + " Handi-Queen")
            $Ch_Focus.SEXP += 5
    elif Ch_Focus.Hand == 1:
            $Ch_Focus.SEXP += 10
            if Ch_Focus.Love >= 500:
                $ Ch_Focus.Mouth = "smile"
                if Ch_Focus is RogueX:
                        ch_r "Ну, очень приятно иметь кого-то, кого можно всегда потрогать."
                elif Ch_Focus is KittyX:
                        ch_k "Он такой теплый на ощупь. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Какой прекрасный опыт. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Это было, вроде как. . . приятно. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Это было довольно весело. . ."
                elif Ch_Focus is StormX:
                        ch_s "Это было приятнее, чем я ожидала. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Это было. . . весело. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Это было очень весело, правда. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Честно говоря, это было очень весело. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Это было очень весело, правда. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Это было весело."
            elif Player.Focus <= 20:
                $ Ch_Focus.Mouth = "sad"
                if Ch_Focus is RogueX:
                        ch_r "Ну, я надеюсь, что ты получил хоть какое-то удовольствие."
                elif Ch_Focus is KittyX:
                        ch_k "Ты удовлетворен?"
                elif Ch_Focus is EmmaX:
                        ch_e "Ты удовлетворен?"
                elif Ch_Focus is LauraX:
                        ch_l "Тебе хоть немного понравилось?"
                elif Ch_Focus is JeanX:
                        ch_j "Очень приятно, да?"
                elif Ch_Focus is StormX:
                        ch_s "Ты удовлетворен?"
                elif Ch_Focus is JubesX:
                        ch_v "Твои потребности удовлетворены?"
                elif Ch_Focus is GwenX:
                        ch_g "Ты доволен?"
                elif Ch_Focus is BetsyX:
                        ch_b "Полагаю, ты удовлетворен?"
                elif Ch_Focus is DoreenX:
                        ch_d "Это было достаточно хорошо, правда?"
                elif Ch_Focus is WandaX:
                        if not Player.Male:
                            ch_w "Ты довольна?"
                        else:
                            ch_w "Ты доволен?"
    elif Ch_Focus.Hand == 5:
                if Ch_Focus is RogueX:
                        ch_r "Думаю, у меня теперь неплохо получается."
                elif Ch_Focus is KittyX:
                        ch_k "Дай мне знать, когда тебе понадобится \"рука помощи.\""
                elif Ch_Focus is EmmaX:
                        ch_e "Прошу, зови меня снова. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Думаю, что у меня неплохо получается."
                elif Ch_Focus is JeanX:
                        ch_j "У меня неплохо получается, ведь так?"
                elif Ch_Focus is StormX:
                        ch_s "Я уже привыкла. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Кажется, я поняла в чем суть."
                elif Ch_Focus is GwenX:
                        ch_g "Думаю, я начинаю понимать в чем суть."
                elif Ch_Focus is BetsyX:
                        ch_b "Думаю, я достаточно \"наловчилась.\""
                elif Ch_Focus is DoreenX:
                        ch_d "Думаю, я начала разбираться."
                elif Ch_Focus is WandaX:
                        ch_w "Думаю, я втянулась."
    $ Tempmod = 0
    if Situation == "shift":
        call Sex_Basic_Dialog(Ch_Focus,"shift") #"Ok, so what else did you want to do?"
    else:
        call expression Ch_Focus.Tag + "_HJ_Reset" #call Girl_HJ_Reset
    call Checkout
    return

## end Ch_Focus.Handjob //////////////////////////////////////////////////////////////////////


## Ch_Focus.Titjob //////////////////////////////////////////////////////////////////////              Not finished
label Girl_Titjob:
##    #fix remove
#    if Ch_Focus is WandaX:
#        "Not currently available."
#        return
##    #fix remove
    if not Player.Male:
            "Пока не реализовано, извините. . ."
            return
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)
    if Ch_Focus.Tit >= 7: # She loves it
        $ Tempmod += 10
    elif Ch_Focus.Tit >= 3: #You've done it before several times
        $ Tempmod += 7
    elif Ch_Focus.Tit: #You've done it before
        $ Tempmod += 5
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 3

    if Ch_Focus.Addict >= 75 and Ch_Focus.Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    elif Ch_Focus.Addict >= 75:
        $ Tempmod += 5

    if Ch_Focus.SeenChest and ApprovalCheck(Ch_Focus, 500): # You've seen her tits.
        $ Tempmod += 10
    if not Ch_Focus.Chest and not Ch_Focus.Over: #She's already topless
        $ Tempmod += 10
    if Ch_Focus.Lust > 75: #She's really horny
        $ Tempmod += 10
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (5*Ch_Focus.Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 30
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10

    if "no titjob" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no titjob" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 1200, TabM = 4) # 120, 135, 150, Taboo -200(320)

    if not Ch_Focus.Tit and "no titjob" not in Ch_Focus.RecentActions:
        $ Ch_Focus.FaceChange("surprised", 1)
        $ Ch_Focus.Mouth = "kiss"
        if Ch_Focus is RogueX:
                ch_r "Ты хочешь, чтобы я потерла твой член своей грудью?"
        elif Ch_Focus is KittyX:
                ch_k "Ты хочешь потереться своим членом о мою. . . грудь?"
        elif Ch_Focus is EmmaX:
                ch_e "Хмм, а ты уверен, что справишься, [EmmaX.Petname]?"
        elif Ch_Focus is LauraX:
                ch_l "Ты хочешь, чтобы я подрочила тебе своими сиськами, да?"
        elif Ch_Focus is JeanX:
                ch_j "Ох, так значит ты хочешь увидеть их в деле. . ."
                $ JeanX.FaceChange("sly", 1)
                ch_j "Я не могу винить тебя за это. . ."
        elif Ch_Focus is StormX:
                ch_s "Тебя очень привлекает моя грудь, [StormX.Petname]?"
        elif Ch_Focus is JubesX:
                ch_v "О! Ты, эм. . . хочешь трахнуть мои сиськи?"
        elif Ch_Focus is GwenX:
                ch_g "Ты, эм. . . хочешь дрочку грудью?"
        elif Ch_Focus is BetsyX:
                ch_b "Ты хочешь, чтобы я доставила тебе. . . удовольствие. . . своей. . . грудью?"
        elif Ch_Focus is DoreenX:
                ch_d "Ты. . . хочешь воспользоваться моей грудью?"
        elif Ch_Focus is WandaX:
                ch_w "Хм, значит, ты хочешь мои сиськи. . . "
        if Ch_Focus.Blow:
            $ Ch_Focus.Mouth = "smile"
            call AnyLine(Ch_Focus,"Моего ротика тебе уже мало?")
        elif Ch_Focus.Hand:
            $ Ch_Focus.Mouth = "smile"
            call AnyLine(Ch_Focus,"Моей руки тебе уже мало?")


    if not Ch_Focus.Tit and Approval:
        #First time dialog
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
        elif Ch_Focus.Love >= (Ch_Focus.Obed + Ch_Focus.Inbt):
            $ Ch_Focus.FaceChange("sexy")
            $ Ch_Focus.Brows = "sad"
            $ Ch_Focus.Mouth = "smile"
            if Ch_Focus is RogueX:
                    ch_r "Хм, если ты после этого отстанешь."
            elif Ch_Focus is KittyX:
                    ch_k "Приятно, что ты вообще об этом подумал."
            elif Ch_Focus is EmmaX:
                    ch_e "Полагаю, ты заслужил чего-то особенного. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Ну, возможно, ты этого заслуживаешь."
            elif Ch_Focus is JeanX:
                    ch_j "Я бы с удовольствием, но. . ."
            elif Ch_Focus is StormX:
                    ch_s "Пожалуй, ты заслужил что-то особенное. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Пожалуй, мы могли бы это сделать. . ."
            elif Ch_Focus is GwenX:
                    ch_g ". . . Я могла бы принять в этом участие."
            elif Ch_Focus is BetsyX:
                    ch_b ". . . Я приму твое предложение."
            elif Ch_Focus is DoreenX:
                    ch_d ". . . наверное, я могу на это пойти. . ."
            elif Ch_Focus is WandaX:
                    ch_w ". . . думаю, я не против. . ."
        elif Ch_Focus.Obed >= Ch_Focus.Inbt:
            $ Ch_Focus.FaceChange("normal")
            if Ch_Focus in (EmmaX,StormX,BetsyX):
                    call AnyLine(Ch_Focus,"Если ты этого хочешь, "+Ch_Focus.Petname+". . .")
            else:
                    call AnyLine(Ch_Focus,"Если это то, чего ты хочешь, "+Ch_Focus.Petname+". . .")
        else: # Uninhibited
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Mouth = "smile"
            if Ch_Focus is KittyX:
                    ch_k "Я никогда даже не задумывалась об этом."
            elif Ch_Focus is EmmaX:
                    ch_e "Хм, мне было интересно, когда ты спросишь. . ."
            elif Ch_Focus is StormX:
                    ch_s "Хмм, я ждала, что однажды ты этого попросишь. . ."
            else:
                    $ Line = renpy.random.choice(["Хех. . ." ,
                        "Хмм, это может быть весело. . .",
                        "Наверное, я согласна. . .",
                        "Пожалуй, можно. . .",
                        "Хмм. . ."])
                    call AnyLine(Ch_Focus,Line)
    elif Approval:
        #Second time+ dialog
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
            if Ch_Focus is RogueX:
                    ch_r "Это ведь не войдет у тебя в привычку, да?"
            elif Ch_Focus is KittyX:
                    ch_k "Это ведь не войдет у тебя в привычку, правда?"
            elif Ch_Focus is EmmaX:
                    ch_e "Надеюсь, подобное не войдет у тебя в привычку?"
            elif Ch_Focus is LauraX:
                    ch_l "Ты немного перегибаешь."
            elif Ch_Focus is JeanX:
                    ch_j "Ну, ты просишь о слишком многом. . ."
            elif Ch_Focus is StormX:
                    ch_s "Тебе так нравится использовать ее?"
            elif Ch_Focus is JubesX:
                    ch_v "Может, воспользуешься моими руками?"
            elif Ch_Focus is GwenX:
                    ch_g "Это как-то слишком. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Это немного черезчур. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Я не уверена. . ."
            elif Ch_Focus is WandaX:
                    ch_w "-это немного черезчур."
        elif not Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabyes") #"This -would- be a better place for it. . ."
        elif "titjob" in Ch_Focus.DailyActions:
            $ Ch_Focus.FaceChange("sexy", 1)
            if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Хочешь добавки?",
                    "Похоже, тебе нравятся мои девочки за работой.",
                    "Тебе все мало?",
                    "Похоже, тебе нравятся мои малышки за работой."])
            else:
                $ Line = renpy.random.choice(["Вернулся за добавкой?",
                    "Тебе правда они так нравятся?",
                    "Тебе все мало?",
                    "Ты действительно вернулся за добавкой?"])
            call AnyLine(Ch_Focus,Line)
            if "titjob" in Ch_Focus.RecentActions:
                    jump Girl_TJ_Prep
        elif Ch_Focus.Tit < 3:
            $ Ch_Focus.FaceChange("sexy", 1)
            $ Ch_Focus.Brows = "confused"
            $ Ch_Focus.Mouth = "kiss"
            if Ch_Focus is RogueX:
                    ch_r "Так что, ты хочешь, чтобы я снова подрочила тебе сиськами?"
            elif Ch_Focus is KittyX:
                    ch_k "Так что, ты хочешь, чтобы я снова подрочила тебе сиськами?"
            elif Ch_Focus is EmmaX:
                    ch_e "Хмм, еще одну дрочку грудью?"
            elif Ch_Focus is LauraX:
                    ch_l "Снова подрочить тебе сиськами?"
            elif Ch_Focus is JeanX:
                    ch_j "Что, опять?"
            elif Ch_Focus is StormX:
                    ch_s "Все не можешь насытиться?"
            elif Ch_Focus is JubesX:
                    ch_v "Ох, снова?"
            elif Ch_Focus is GwenX:
                    ch_g "А, опять?"
            elif Ch_Focus is BetsyX:
                    ch_b "Ох, дорогуша, снова?"
            elif Ch_Focus is DoreenX:
                    ch_d "Еще раз подрочить грудью?"
            elif Ch_Focus is WandaX:
                    ch_w "Снова хочешь, чтобы я поработала своими сиськами?"
        else:
            $ Ch_Focus.FaceChange("sexy", 1)
            $ Ch_Focus.ArmPose = 2
#            if Ch_Focus in (EmmaX,StormX,BetsyX):
#                    $ Line = renpy.random.choice(["Very well, place it here.",
#                        "Oh. . . very well then.",
#                        "Yum.",
#                        "Certainly, let's whip it out then.",
#                        "Oh, very well. . . [She drools a bit into her cleavage].",
#                        "Ha, very well then. . ."])
#            else:
            $ Line = renpy.random.choice(["Ты хочешь этого. . . [покачивает своими сиськами]?",
                "Так, ты хочешь, чтобы я снова подрочила тебе сиськами?",
                "Еще немного этих. . . упругих малышек?",
                "Значит, ты снова хочешь мою грудь?",
                "Снова, эм. . . \"подрочить грудью?\"",
                "Еще немножко. . . [указывает на свою грудь]?"])
            call AnyLine(Ch_Focus,Line)
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
            $ Ch_Focus.Statup("Obed", 90, 1)
            $ Ch_Focus.Statup("Inbt", 60, 1)
            if Ch_Focus in (EmmaX,StormX,BetsyX):
                    call AnyLine(Ch_Focus,"Хорошо.")
            else:
                    call AnyLine(Ch_Focus,"Ладно.")
        elif not Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabyes") #"This -would- be a better place for it. . ."
        else:
            $ Ch_Focus.FaceChange("sexy", 1)
            $ Ch_Focus.Statup("Love", 90, 1)
            $ Ch_Focus.Statup("Inbt", 50, 3)
            if Ch_Focus in (EmmaX,StormX,BetsyX):
                $ Line = renpy.random.choice(["Хорошо, давай его сюда.",
                    "Ох. . . хорошо.",
                    "Ням.",
                    "Конечно, давай его сюда.",
                    "Ох, хорошо. . . [Она размазывает немного слюны между своих грудей].",
                    "Хех, ну хорошо. . ."])
            else:
                $ Line = renpy.random.choice(["Конечно, давай его сюда.",
                    "Ну. . . ладно.",
                    "Ням.",
                    "Конечно, доставай его.",
                    "Ладно. . . [Она размазывает немного слюны между своих грудей].",
                    "Хех, ладно."])
            call AnyLine(Ch_Focus,Line)
            $ Line = 0
        $ Ch_Focus.Statup("Obed", 20, 1)
        $ Ch_Focus.Statup("Obed", 70, 1)
        $ Ch_Focus.Statup("Inbt", 80, 2)
        jump Girl_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("angry")
        if "no titjob" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"noday") #"I don't think I've been confusing on this one."
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday") #"Like I said, I don't do that sort of thing. . . -in public-."
        elif not Ch_Focus.Tit:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "Я пока еще к этому не готова, [RogueX.Petname]. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Я еще к этому не готова, [KittyX.Petname]. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Думаю, ты еще не готов, [EmmaX.Petname]. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Мне такое не особо нравится, [LauraX.Petname]. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Это не ко мне, [JeanX.Petname]. . ."
            elif Ch_Focus is StormX:
                    ch_s "Не думаю, что это возможно."
            elif Ch_Focus is JubesX:
                    ch_v "Я не уверена. . . [JubesX.Petname]? . ."
            elif Ch_Focus is GwenX:
                    ch_g "Серьезно, [GwenX.Petname]. . ?"
            elif Ch_Focus is BetsyX:
                    ch_b "Ты серьезно, [BetsyX.Petname]. . ?"
            elif Ch_Focus is DoreenX:
                    ch_d "Да ладно тебе, [Ch_Focus.Petname]. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Ты сейчас серьезно, [WandaX.Petname]. . ?"
        else:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "Нет, не сейчас, [RogueX.Petname]. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Не сейчас, ладно?"
            elif Ch_Focus is EmmaX:
                    ch_e "Сейчас я бы предпочла этого не делать."
            elif Ch_Focus is LauraX:
                    ch_l "Нет."
            elif Ch_Focus is JeanX:
                    ch_j "Не-а."
            elif Ch_Focus is StormX:
                    ch_s "Сейчас я бы предпочла этого не делать."
            elif Ch_Focus is JubesX:
                    ch_v "Я не уверена. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Не."
            elif Ch_Focus is BetsyX:
                    ch_b "Я бы предпочла этого не делать."
            elif Ch_Focus is DoreenX:
                    ch_d "Я. . . не хочу."
            elif Ch_Focus is WandaX:
                    ch_w "Хмм. . . я так не думаю."
        menu:
            extend ""
            "Извини, забудь." if "no titjob" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"noproblem") #"Oh, thanks, I understand. . ."
                return
            "Может, в другой раз?" if "no titjob" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy")
                call Sex_Basic_Dialog(Ch_Focus,"maybe") #". . . maybe."
                $ Ch_Focus.Statup("Love", 80, 2)
                $ Ch_Focus.Statup("Inbt", 70, 2)
                if Ch_Focus.Taboo:
                    $ Ch_Focus.RecentActions.append("tabno")
                    $ Ch_Focus.DailyActions.append("tabno")
                $ Ch_Focus.RecentActions.append("no titjob")
                $ Ch_Focus.DailyActions.append("no titjob")
                return
            "Я считаю, это понравится нам обоим. . .":
                if Approval:
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 80, 2)
                    $ Ch_Focus.Statup("Obed", 40, 2)
                    $ Ch_Focus.Statup("Inbt", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 40, 2)
                    if Ch_Focus in (EmmaX,StormX,BetsyX):
                        $ Line = renpy.random.choice(["Ну, хорошо, давай свой член сюда.",
                            "Ох. . . ну хорошо.",
                            "Ням.",
                            "Конечно, доставай его.",
                            "Ох, хорошо. . . [Она размазывает немного слюны между своих грудей].",
                            "Хех, хорошо. . ."])
                    else:
                        $ Line = renpy.random.choice(["Ну, ладно, давай свой член сюда.",
                            "Ну. . . ладно.",
                            "Ням.",
                            "Думаю, можешь доставать свой член.",
                            "Ладно. . . [Она размазывает немного слюны между своих грудей].",
                            "Хех, ну ладно."])
                    call AnyLine(Ch_Focus,Line)
                    $ Line = 0
                    jump Girl_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(Ch_Focus, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if (Approval >= 2 and Ch_Focus.Blow) or Ch_Focus is JubesX:
                        $ Ch_Focus.Statup("Inbt", 80, 1)
                        $ Ch_Focus.Statup("Inbt", 60, 3)
                        $ Ch_Focus.FaceChange("confused", 1)
                        if Ch_Focus is RogueX:
                                ch_r "Может вместо этого. . . я отсосу тебе?"
                        elif Ch_Focus is KittyX:
                                ch_k "Может, мне[KittyX.like]лучше. . . отсосать тебе?"
                        elif Ch_Focus is EmmaX:
                                ch_e "Тебе, по-видимому, нравятся минеты, может, не откажешься и в этот раз?"
                        elif Ch_Focus is LauraX:
                                ch_l "Может, я лучше отсосу тебе?"
                        elif Ch_Focus is JeanX:
                                ch_j "Может, тогда лучше минет?"
                        elif Ch_Focus is StormX:
                                ch_s "Тебе, видимому, нравятся минеты, может, не откажешься и в этот раз?"
                        elif Ch_Focus is JubesX:
                                ch_v "Что, если. . . вместо этого я отсосу тебе?"
                        elif Ch_Focus is GwenX:
                                ch_g "А может минет?"
                        elif Ch_Focus is BetsyX:
                                ch_b "Может, тебе будет достаточно минета?"
                        elif Ch_Focus is DoreenX:
                                ch_d "Может, я, эм. . . лучше его оближу?"
                        elif Ch_Focus is WandaX:
                                ch_w "Может, тебе хватит минета?"
                        menu:
                            extend ""
                            "Ладно, вставай на колени.":
                                $ Ch_Focus.Statup("Love", 80, 2)
                                $ Ch_Focus.Statup("Inbt", 60, 1)
                                $ Ch_Focus.Statup("Obed", 50, 1)
                                jump Girl_BJ_Prep
                            "Нет, вся прелесть именно в сиськах.":
                                $ Line = "no BJ"
                    if Approval and Ch_Focus.Hand:
                        $ Ch_Focus.Statup("Inbt", 80, 1)
                        $ Ch_Focus.Statup("Inbt", 60, 3)
                        $ Ch_Focus.FaceChange("confused", 1)
                        if Ch_Focus is RogueX:
                                ch_r "Может согласишься на подрочить?"
                        elif Ch_Focus is KittyX:
                                ch_k "Может я лучше[KittyX.like]подрочу тебе?"
                        elif Ch_Focus is EmmaX:
                                ch_e "Может, вместо этого я тебе подрочу?"
                        elif Ch_Focus is LauraX:
                                ch_l "Может я лучше подрочу тебе?"
                        elif Ch_Focus is JeanX:
                                ch_j "Может, тогда лучше согласишься на мою руку?"
                        elif Ch_Focus is StormX:
                                ch_s "Может, вместо этого я тебе подрочу?"
                        #elif Ch_Focus is JubesX:
                        elif Ch_Focus is GwenX:
                                ch_g "Может, я лучше подрочу?"
                        elif Ch_Focus is BetsyX:
                                ch_b "Может, я тебе лучше подрочу?"
                        elif Ch_Focus is DoreenX:
                                h_d "Эм, может я лучше тебе подрочу?"
                        elif Ch_Focus is WandaX:
                                ch_w "Что ж, может, выберешь дрочку?"
                        menu:
                            extend ""
                            "Конечно, я не против.":
                                $ Ch_Focus.Statup("Love", 80, 2)
                                $ Ch_Focus.Statup("Inbt", 60, 1)
                                $ Ch_Focus.Statup("Obed", 50, 1)
                                jump Girl_HJ_Prep
                            "Я хочу сиськи." if Line == "no BJ":
                                $ Line = 0
                            "Нет, вся прелесть именно в сиськах." if Line != "no BJ":
                                pass
                    $ Ch_Focus.Statup("Love", 200, -2)
                    $ Line = renpy.random.choice(["Что ж, жаль.",
                        "Ладно, как хочешь.",
                        "Жаль. . .",
                        "Тогда ничего не получишь.",
                        "Хм. . ."])
                    $ Ch_Focus.Statup("Obed", 70, 2)


            "Да брось, дай мне трахнуть свои сиськи, [Ch_Focus.Pet].":                                               # Pressured into it
                $ Ch_Focus.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(Ch_Focus, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -5, 1)
                    $ Ch_Focus.Statup("Love", 200, -2)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #"Oh, fine."
                    $ Ch_Focus.Statup("Obed", 50, 4)
                    $ Ch_Focus.Statup("Inbt", 80, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    $ Ch_Focus.Forced = 1
                    jump Girl_TJ_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -15)
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    #She refused all offers.
    if "no titjob" in Ch_Focus.DailyActions:
        $ Ch_Focus.FaceChange("angry", 1)
        call Sex_Basic_Dialog(Ch_Focus,"nothanks") #"Quit bugging me."
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("angry", 1)
        if Ch_Focus is RogueX:
                ch_r "Я не такая!"
        elif Ch_Focus is KittyX:
                ch_k "Нет, это даже звучит странно."
        elif Ch_Focus is EmmaX:
                ch_e "Осторожнее."
        elif Ch_Focus is LauraX:
                ch_l "Нет."
        elif Ch_Focus is JeanX:
                ch_j "Нет."
        elif Ch_Focus is StormX:
                ch_s "Меня это не устраивает."
        elif Ch_Focus is JubesX:
                ch_v "Неее-а."
        elif Ch_Focus is GwenX:
                ch_g "Эм. . . нет."
        elif Ch_Focus is BetsyX:
                ch_b ". . . Я бы предпочла этого не делать."
        elif Ch_Focus is DoreenX:
                ch_d ". . . Не думаю, что хочу этого. . ."
        elif Ch_Focus is WandaX:
                ch_w ". . . Мне такое не по вкусу."
        $ Ch_Focus.Statup("Lust", 200, 5)
        if Ch_Focus.Love > 300:
                $ Ch_Focus.Statup("Love", 70, -2)
        $ Ch_Focus.Statup("Obed", 50, -2)
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Taboo:                             # she refuses and this is too public a place for her
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.DailyActions.append("tabno")
        call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You can't do that here!"
        $ Ch_Focus.Statup("Lust", 200, 5)
        $ Ch_Focus.Statup("Obed", 50, -3)
    elif Ch_Focus.Tit:
        $ Ch_Focus.FaceChange("sad")
        if Ch_Focus is RogueX:
                ch_r "Думаю, на этот раз ты должен справиться сам. . ."
        elif Ch_Focus is KittyX:
                ch_k "Я не в настроение сегодня. . ."
        elif Ch_Focus is EmmaX:
                ch_e "Я бы не хотела подобного. . ."
        elif Ch_Focus is LauraX:
                ch_l "Мне сегодня не хочется. . ."
        elif Ch_Focus is JeanX:
                ch_j "Мне сегодня не хочется. . ."
        elif Ch_Focus is StormX:
                ch_s "Our time together was a memory."
        elif Ch_Focus is JubesX:
                ch_v "Не сейчас. . ."
        elif Ch_Focus is GwenX:
                ch_g "Эм, не сегодня. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Меня это не интересует. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Мне. . . сейчас не хочется. . ."
        elif Ch_Focus is WandaX:
                ch_w "Не сейчас, ладно?"
    else:
        $ Ch_Focus.FaceChange("normal", 1)
        if Ch_Focus is RogueX:
                ch_r "Давай не будем, [RogueX.Petname]."
        elif Ch_Focus is KittyX:
                ch_k "Я не хочу прикасаться к нему."
        elif Ch_Focus is EmmaX:
                ch_e "Нет, я так не думаю, [EmmaX.Petname]."
        elif Ch_Focus is LauraX:
                ch_l "Я бы предпочла не прикасаться к нему."
        elif Ch_Focus is JeanX:
                ch_j "Я бы предпочла не трогать его."
        elif Ch_Focus is StormX:
                ch_s "Нет, я так не думаю, [StormX.Petname]."
        elif Ch_Focus is JubesX:
                ch_v "Я не в настроении."
        elif Ch_Focus is GwenX:
                ch_g "Эм, нет, спасибо."
        elif Ch_Focus is BetsyX:
                ch_b "Определенно, нет."
        elif Ch_Focus is DoreenX:
                ch_d ". . . Не думаю, что хочу этого. . ."
        elif Ch_Focus is WandaX:
                ch_w "У меня нет никакого желания делать это."
    $ Ch_Focus.RecentActions.append("no titjob")
    $ Ch_Focus.DailyActions.append("no titjob")
    $ Tempmod = 0
    return

label Girl_TJ_Prep:
##    #fix remove
#    if Ch_Focus is WandaX:
#        "Not currently available."
#        return
##    #fix remove

    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)

    $ Ch_Focus.FaceChange("sexy")
    if Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("sad")
    elif not Ch_Focus.Tit:
        $ Ch_Focus.Brows = "confused"
        $ Ch_Focus.Eyes = "sexy"
        $ Ch_Focus.Mouth = "smile"

    call Seen_First_Peen(Ch_Focus,Partner,React=Situation)
    call expression Ch_Focus.Tag + "_TJ_Launch" pass ("L") #call Girl_TJ_Launch("L")

    if Situation == Ch_Focus:
            #Girl auto-starts
            $ Situation = 0
            "[Ch_Focus.Name] опускается вниз и вставляет ваш член между своих сисек."
            menu:
                "Что будете делать?"
                "Ничего не делать.":
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    $ Ch_Focus.Statup("Inbt", 40, 2)
                    "[Ch_Focus.Name] начинает двигать ими вверх-вниз."
                "Похвалить ее.":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    ch_p "Ох, [Ch_Focus.Pet] это хорошая идея."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] продолжает свои действия."
                    $ Ch_Focus.Statup("Love", 85, 1)
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    $ Ch_Focus.FaceChange("confused")
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    ch_p "[Ch_Focus.Name], давай не сейчас."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] выпускает член из объятий своих сисек."
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ Ch_Focus.AddWord(1,"refused","refused")
                    return

    if not Ch_Focus.Tit:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -25)
            $ Ch_Focus.Statup("Obed", 70, 30)
            $ Ch_Focus.Statup("Inbt", 80, 35)
        else:
            $ Ch_Focus.Statup("Love", 90, 5)
            $ Ch_Focus.Statup("Obed", 70, 25)
            $ Ch_Focus.Statup("Inbt", 80, 30)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no titjob")
    $ Ch_Focus.RecentActions.append("titjob")
    $ Ch_Focus.DailyActions.append("titjob")

label Girl_TJ_Cycle: #Repeating strokes
    while Round > 0:
#        call Shift_Focus(Girl)
        call expression Ch_Focus.Tag + "_TJ_Launch" pass ("L") #call Girl_TJ_Launch
        $ Ch_Focus.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . ." if Speed:
                                    pass
                        "Начать? . ." if Speed == 0:
                                    # Modification mode
                                    if is_playing_music(audio.girl_titjob):
                                        $ play_music(name=audio.girl_titjob, loop=True)
                                    # -----------------

                                    $ Speed = 1

                        "Быстрее. . ." if  Speed == 1:
                                    $ Speed = 2
                                    "Вы просите ее немного ускориться."
                        "Быстрее. . . (locked)" if Speed >= 2:
                                    pass

                        "Stop moving" if Speed == 1 or Speed == 3:
                                    $ Speed = 0
                        "Помедленнее. . ." if Speed == 2:
                                    $ Speed = 1
                                    "Вы просите ее немного сбавить темп."
                        "Помедленнее. . . (locked)" if not Speed:
                                    pass

                        "Оближи его" if Speed != 3:
                                    $ Speed = 3
                        "Оближи его (locked)" if Speed == 3:
                                    pass

                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0

                        "Другие варианты":
                                menu:
                                    "Начать также ласкать ее грудь." if Trigger2 != "fondle breasts":
                                            if Ch_Focus.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "Вы начинаете ласкать ее грудь."
                                                $ Ch_Focus.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Сменить основное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                    menu:
                                                        "Может, отсосешь?":
                                                                if Ch_Focus.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Girl_TJ_After
                                                                    call Girl_Blowjob
                                                                else:
                                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")

                                                        "Может, подрочишь мне рукой?":
                                                                if Ch_Focus.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Girl_TJ_After
                                                                    call Girl_Handjob
                                                                else:
                                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        "Неважно":
                                                                jump Girl_TJ_Cycle
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

                                            "Не бросай свое текущее занятие. . .(locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_TJ_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_TJ_Cycle
                                            "Неважно":
                                                        jump Girl_TJ_Cycle

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife
                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_TJ_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_TJ_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_TJ_After
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
                                call expression Ch_Focus.Tag + "_TJ_Reset"
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2 and Ch_Focus.SEXP >= 20:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_TJ_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Girl can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_TJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in Ch_Focus.RecentActions:#And Ch_Focus is unsatisfied,
                                "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                menu:
                                    "Хотите завершить начатое?"
                                    "Продолжим еще немного.":
                                        $ Line = "Вы возвращаетесь к процессу"
                                    "С меня хватит.":
                                        "Вы заканчиваете веселье."
                                        jump Girl_TJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        if Speed >= 4:
                call Speed_Shift(0) #resets speed after orgasm
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
                pass
        elif Cnt == (5 + Ch_Focus.Tit):
                $ Ch_Focus.Brows = "confused"
                if Ch_Focus is RogueX:
                        ch_r "Ты уже скоро? Мне становится немного больно."
                elif Ch_Focus is KittyX:
                        ch_k "Ты уже скоро? Мне немного больно."
                elif Ch_Focus is EmmaX:
                        ch_e "Ты уже скоро? Мне слегка больно."
                elif Ch_Focus is LauraX:
                        ch_l "Ты скоро? Мне уже скучно."
                elif Ch_Focus is JeanX:
                        ch_j "Эй, как там у тебя дела? Ты скоро?"
                elif Ch_Focus is StormX:
                        ch_s "Ты заканчиваешь? Меня это уже немного раздражает. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Ты уже скоро? Я немного устала."
                elif Ch_Focus is GwenX:
                        ch_g "Ну как тебе?"
                elif Ch_Focus is BetsyX:
                        ch_b "Тебя все устраивает?"
                elif Ch_Focus is DoreenX:
                        ch_d "Тебе. . . этого достаточно?"
                elif Ch_Focus is WandaX:
                        ch_w "Тебе нравится?"
        if Cnt == (10 + Ch_Focus.Tit):
                $ Ch_Focus.Brows = "angry"
                if Ch_Focus is RogueX:
                        ch_r "Я уже все себе натерла, [RogueX.Petname]. Давай займемся чем-нибудь другим?"
                elif Ch_Focus is KittyX:
                        ch_k "Похоже, у меня появились мозоли, [KittyX.Petname]. Может, займемся чем-нибудь другим?"
                elif Ch_Focus is EmmaX:
                        ch_e "Я немного устала, не могли бы мы заняться чем-нибудь другим?"
                elif Ch_Focus is LauraX:
                        ch_l "Серьезно, мы можем заняться чем-нибудь другим?"
                elif Ch_Focus is JeanX:
                        ch_j "Ладно, я серьезно, мы не можем заняться чем-нибудь другим?"
                elif Ch_Focus is StormX:
                        ch_s "Мне немного некофмортно, может придумаешь как закончить по-другому?"
                elif Ch_Focus is JubesX:
                        ch_v "Мы, типа, можем заняться чем-нибудь другим?"
                elif Ch_Focus is GwenX:
                        ch_g "У меня, эм. . . немного болит грудь."
                elif Ch_Focus is BetsyX:
                        ch_b "Ты не видишь, что мне немного больно?"
                elif Ch_Focus is DoreenX:
                        ch_d "Мне, эм. . . немного больно."
                elif Ch_Focus is WandaX:
                        ch_w "Слушай, мне. . . немного больно."
                menu:
                    extend ""
                    "Как насчет отсоса?" if Ch_Focus.Action and MultiAction:
                        $ Situation = "shift"
                        call Girl_TJ_After
                        call Girl_Blowjob
                        return
                    "Закончить." if Player.FocusX:
                        "Вы расслабляетесь. . ."
                        $ Player.FocusX = 0
                        $ Player.Focus += 15
                        jump Girl_TJ_Cycle
                    "Давай попробуем что-нибудь другое." if MultiAction:
                        $ Line = 0
                        call expression Ch_Focus.Tag + "_TJ_Reset"
                        $ Situation = "shift"
                        jump Girl_TJ_After
                    "Нет, давай за работу.":
                        if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                            $ Ch_Focus.Statup("Love", 200, -5)
                            $ Ch_Focus.Statup("Obed", 50, 3)
                            $ Ch_Focus.Statup("Obed", 80, 2)
                            "Она ворчит, но возвращается к работе."
                        else:
                            $ Ch_Focus.FaceChange("angry", 1)
                            "Она сердито смотрит на вас, отпускает ваш член и отстраняется."
                            if Ch_Focus is RogueX:
                                    ch_r "Занимайся чем хочешь, но без меня."
                            elif Ch_Focus is KittyX:
                                    ch_k "Послушай, если ты будешь вести себя[KittyX.Like]как мудак, то у меня найдутся дела повожнее."
                            elif Ch_Focus is EmmaX:
                                    ch_e "Ты знаешь, у меня есть дела поважнее."
                            elif Ch_Focus is LauraX:
                                    ch_l "У меня есть дела поважнее."
                            elif Ch_Focus is JeanX:
                                    ch_j "У меня есть дела поважнее."
                            elif Ch_Focus is StormX:
                                    ch_s "Возможно, некоторое время в одиночестве поможет тебе переосмыслить свой выбор."
                            elif Ch_Focus is JubesX:
                                    ch_v "Ни за что, заканчивай сам."
                            elif Ch_Focus is GwenX:
                                    ch_g "Ну, если такова твоя реакция, я пошла. . ."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Боюсь, тогда тебе придется развлекаться без меня. . ."
                            elif Ch_Focus is DoreenX:
                                    ch_d "Тогда я оставлю тебя. . ."
                            elif Ch_Focus is WandaX:
                                    ch_w "Тогда справляйся сам."
                            $ Ch_Focus.Statup("Love", 50, -3, 1)
                            $ Ch_Focus.Statup("Love", 80, -4, 1)
                            $ Ch_Focus.Statup("Obed", 30, -1, 1)
                            $ Ch_Focus.Statup("Obed", 50, -1, 1)
                            $ Ch_Focus.RecentActions.append("angry")
                            $ Ch_Focus.DailyActions.append("angry")
                            jump Girl_TJ_After
            #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10)  #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5)  #ch_d "Tic tock, [Ch_Focus.Petname]."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done")  # ch_d "Ok, [Ch_Focus.Petname], breaktime."

label Girl_TJ_After:
    # Modification mode
    $ play_music()
    $ play_sound()
    # -----------------

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.Tit += 1
    $ Ch_Focus.Action -=1
    $ Ch_Focus.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Ch_Focus.Addictionrate += 1

    call Partner_Like(Ch_Focus,4)

    if Ch_Focus.Tit > 5:
        pass
    elif Ch_Focus.Tit == 1:
        $ Ch_Focus.SEXP += 12
        if Ch_Focus.Love >= 500:
            $ Ch_Focus.Mouth = "smile"
            if Ch_Focus is RogueX:
                    ch_r "Ну, это было определенно интересно."
            elif Ch_Focus is KittyX:
                    ch_k "Это было довольно весело."
            elif Ch_Focus is EmmaX:
                    ch_e "Ммм, тебе было также хорошо, как и мне?"
            elif Ch_Focus is LauraX:
                    ch_l "Это было весело."
            elif Ch_Focus is JeanX:
                    ch_j "Ладно, это было весело."
            elif Ch_Focus is StormX:
                    ch_s "Ммм, мне очень понравилось!"
            elif Ch_Focus is JubesX:
                    ch_v "Это было очень весело. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Ладно, это было очень весело."
            elif Ch_Focus is BetsyX:
                    ch_b "Ох, это было довольно приятно."
            elif Ch_Focus is DoreenX:
                    ch_d "Слушай! Это было довольно весело."
            elif Ch_Focus is WandaX:
                    ch_w "Хех, нам стоит как-нибудь повторить."
        elif Player.Focus <= 20:
            $ Ch_Focus.Mouth = "sad"
            if Ch_Focus is RogueX:
                    ch_r "Ну, я надеюсь, что ты получил хоть какое-то удовольствие."
            elif Ch_Focus is KittyX:
                    ch_k "Ты удовлетворен?"
            elif Ch_Focus is EmmaX:
                    ch_e "Надеюсь, что оправдала твои ожидания."
            elif Ch_Focus is LauraX:
                    ch_l "Тебе хоть немного понравилось?"
            elif Ch_Focus is JeanX:
                    ch_j "Очень приятно, да?"
            elif Ch_Focus is StormX:
                    ch_s "Надеюсь, что соответствовала твоим стандартам."
            elif Ch_Focus is JubesX:
                    ch_v "Твои потребности удовлетворены?"
            elif Ch_Focus is GwenX:
                    ch_g "Ты доволен?"
            elif Ch_Focus is BetsyX:
                    ch_b "Полагаю, ты удовлетворен?"
            elif Ch_Focus is DoreenX:
                    ch_d "Эм, тебе этого достаточно?"
            elif Ch_Focus is WandaX:
                    ch_w "Ты доволен?"
    elif Ch_Focus.Tit == 5:
            if Ch_Focus is RogueX:
                    ch_r "Думаю, я кое-чему научилась."
            elif Ch_Focus is KittyX:
                    ch_k "Эм, хоть для чего то они пригодились."
            elif Ch_Focus is EmmaX:
                    ch_e "Вижу, тебе понравилось."
            elif Ch_Focus is LauraX:
                    ch_l "Похоже, тебе это нравится."
            elif Ch_Focus is JeanX:
                    ch_j "Неплохо, да?"
            elif Ch_Focus is StormX:
                    ch_s "Похоже, тебе это нравится."
            elif Ch_Focus is JubesX:
                    ch_v "Тебе, кажется, это нравится. . ."
                    if "titlick" in JubesX.RecentActions and not JubesX.Blow:
                            ch_v "Я могла бы, эм. . . пососать его еще немного. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Думаю, у меня стало получаться."
            elif Ch_Focus is BetsyX:
                    ch_b "Я думаю, у меня стало получаться лучше."
            elif Ch_Focus is DoreenX:
                    ch_d "Я вроде как начинаю к этому привыкать!"
            elif Ch_Focus is WandaX:
                    ch_w "Это довольно весело."
    $ Tempmod = 0

    if Situation == "shift":
            call Sex_Basic_Dialog(Ch_Focus,"shift") #"Ok, so what else did you want to do?"
    else:
            call expression Ch_Focus.Tag + "_TJ_Reset" #call Girl_TJ_Reset
    call Checkout
    return

## end Ch_Focus.Titjob //////////////////////////////////////////////////////////////////////



# Ch_Focus.Blowjob //////////////////////////////////////////////////////////////////////

label Girl_Blowjob:
##    #fix remove
#    if Ch_Focus is WandaX:
#        "Not currently available."
#        return
##    #fix remove
    if not Player.Male:
            call Girl_CUN
            return
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)
    if Ch_Focus.Blow >= 7: # She loves it
        $ Tempmod += 15
    elif Ch_Focus.Blow >= 3: #You've done it before several times
        $ Tempmod += 10
    elif Ch_Focus.Blow: #You've done it before
        $ Tempmod += 7
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 4

    if Ch_Focus.Addict >= 75 and Ch_Focus.Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 25
    elif Ch_Focus.Addict >= 75: #She's really strung out
        $ Tempmod += 15

    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (4*Ch_Focus.Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 40
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10

    if "no blow" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no blow" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not Ch_Focus.Blow and "no blow" not in Ch_Focus.RecentActions:
        $ Ch_Focus.FaceChange("surprised", 2)
        $ Ch_Focus.Mouth = "kiss"
        if Ch_Focus is RogueX:
                ch_r "Ты хочешь, чтобы я взяла твой член. . . себе в рот?"
        elif Ch_Focus is KittyX:
                ch_k "Ты хочешь, чтобы я отсосала тебе?"
        elif Ch_Focus is EmmaX:
                $ EmmaX.FaceChange("sly")
                ch_e "Так, ты хочешь, чтобы я отсосала тебе?"
        elif Ch_Focus is LauraX:
                ch_l "Ты хочешь, чтобы я отсосала тебе?"
        elif Ch_Focus is JeanX:
                ch_j "О! Ты хочешь, чтобы я отсосала тебе?"
        elif Ch_Focus is StormX:
                $ StormX.FaceChange("sly")
                ch_s "Ты хочешь, чтобы я пососала твой член?"
        elif Ch_Focus is JubesX:
                $ JubesX.FaceChange("surprised", 2)
                $ JubesX.Mouth = "kiss"
                ch_v "Ооо! Ты хочешь, чтобы я отсосала тебе?"
                $ JubesX.Mouth = "smile"
                ch_v "Уверен, что не боишься моих зубок?"
        elif Ch_Focus is GwenX:
                ch_g "Ох, ты, эм. . . хочешь, чтобы я. . ."
                ch_g "-отсосала твой член. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Ох, дорогуша ты хочешь, чтобы я. . ."
                ch_b "-отсосала твой член. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Ох. ты, эм. . . хочешь. . ."
                ch_d "-чтобы я облизала твой пенис? . ."
        elif Ch_Focus is WandaX:
                ch_w "Ты хочешь минет, да? . ."
        if Ch_Focus.Hand:
            $ Ch_Focus.Mouth = "smile"
            if Ch_Focus is RogueX:
                    ch_r "Моей руки теперь тебе мало?"
            elif Ch_Focus is KittyX:
                    ch_k "Моих ладоней тебе уже мало?"
            elif Ch_Focus is LauraX:
                    ch_l "Дрочки уже недостаточно?"
            elif Ch_Focus is GwenX:
                    ch_g "Уже устал от дрочки?"
            elif Ch_Focus is BetsyX:
                    ch_b "Уже устал от дрочки?"
            elif Ch_Focus is DoreenX:
                    ch_d "Тебе. . . недостаточно моей руки?"
            elif Ch_Focus is WandaX:
                    ch_w "Тебе уже мало дрочки?"
        $ Ch_Focus.Blush = 1

    if not Ch_Focus.Blow and Approval:
            #First time dialog
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Love", 70, -3, 1)
                $ Ch_Focus.Statup("Love", 20, -2, 1)
            elif Ch_Focus.Love >= (Ch_Focus.Obed + Ch_Focus.Inbt):
                $ Ch_Focus.FaceChange("sexy")
                $ Ch_Focus.Brows = "sad"
                $ Ch_Focus.Mouth = "smile"
                if Ch_Focus is RogueX:
                        ch_r "Я никогда не брала ничего подобного в рот. . . это может быть интересно."
                elif Ch_Focus is KittyX:
                        ch_k "Мне даже немного интересно, каков ты. . . на вкус."
                elif Ch_Focus is EmmaX:
                        ch_e "Мне любопытно, так ли он хорош на вкус, как выглядит. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Мне интересно, какой ты на вкус."
                elif Ch_Focus is JeanX:
                        ch_j "Ну, я вряд ли смогу отказаться от подобного предложения. . ."
                elif Ch_Focus is StormX:
                        ch_s "Мне любопытно, каково это. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Я даже слегка с нетерпением ждала этого. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Мне интересно, какой ты на вкус."
                elif Ch_Focus is BetsyX:
                        ch_b "Мне немного любопытно узнать твой -особый- вкус."
                elif Ch_Focus is DoreenX:
                        ch_d "Мне немного любопытно, каков ты на вкус."
                elif Ch_Focus is WandaX:
                        ch_w "Не могу сказать, что я не думала об этом."
            elif Ch_Focus.Obed >= Ch_Focus.Inbt:
                $ Ch_Focus.FaceChange("normal")
                if Ch_Focus in (EmmaX,StormX,BetsyX):
                        call AnyLine(Ch_Focus,"Если ты этого хочешь, "+Ch_Focus.Petname+". . .")
                else:
                        call AnyLine(Ch_Focus,"Если это то, чего ты хочешь, "+Ch_Focus.Petname+". . .")
            else: # Uninhibited
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Mouth = "smile"
                $ Line = renpy.random.choice(["Хех. . ." ,
                    "Хмм, это может быть весело. . .",
                    "Наверное, можно. . .",
                    "Пожалуй, это я могу. . .",
                    "Хмм. . ."])
                call AnyLine(Ch_Focus,Line)
            #end First time dialog
    elif Approval:
            #Second time+ dialog
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                if Ch_Focus is not JubesX:
                        $ Ch_Focus.Statup("Love", 70, -3, 1)
                        $ Ch_Focus.Statup("Love", 20, -2, 1)
                if Ch_Focus is RogueX:
                        ch_r "Ты хочешь, чтобы я сделала это снова?"
                elif Ch_Focus is KittyX:
                        ch_k "Ты хочешь, чтобы я сделала это снова?"
                elif Ch_Focus is EmmaX:
                        ch_e "Ах, снова?"
                elif Ch_Focus is LauraX:
                        ch_l "Снова?"
                elif Ch_Focus is JeanX:
                        ch_j "Снова?"
                elif Ch_Focus is StormX:
                        ch_s "Ц, снова?"
                elif Ch_Focus is JubesX:
                        $ JubesX.FaceChange("normal")
                        $ JubesX.Statup("Obed", 90, 1)
                        $ JubesX.Statup("Inbt", 60, 1)
                        ch_v "Снова?"
                elif Ch_Focus is GwenX:
                        ch_g "Снова?"
                elif Ch_Focus is BetsyX:
                        ch_b "Ох, дорогуша, снова?"
                elif Ch_Focus is DoreenX:
                        ch_d "Ох, снова?"
                elif Ch_Focus is WandaX:
                        ch_w "Хм. Снова?"
            elif not Taboo and "tabno" in Ch_Focus.DailyActions:
                call Sex_Basic_Dialog(Ch_Focus,"tabyes") #"This -would- be a better place for it. . ."
            elif "blow" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy", 1)
                if Ch_Focus is JubesX:
                    $ Line = renpy.random.choice(["Пришел за добавкой?",
                        "Даже у меня есть свои пределы. . .",
                        "Должно быть, я слишком хороша в этом.",
                        "Хмм. . .",
                        "Тебе все мало?"])
                else:
                    $ Line = renpy.random.choice(["Снова так скоро?",
                        "Дай мне набрать немного слюны.",
                        "Все еще недостаточно?",
                        "Моя челюсть все еще побаливает после прошлого раза.",
                        "Моя челюсть все еще побаливает от того, что было раньше."])
                call AnyLine(Ch_Focus,Line)
                if "blow" in Ch_Focus.RecentActions:
                        jump Girl_BJ_Prep
            elif Ch_Focus.Blow < 3:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Brows = "confused"
                $ Ch_Focus.Mouth = "kiss"
                if Ch_Focus is RogueX:
                        ch_r "Итак, хочешь еще один минет?"
                elif Ch_Focus is KittyX:
                        ch_k "Итак, хочешь еще один минет?"
                elif Ch_Focus is EmmaX:
                        ch_e "Еще один минет?"
                elif Ch_Focus is LauraX:
                        ch_l "Хочешь еще один отсос?"
                elif Ch_Focus is JeanX:
                        ch_j "Хочешь еще один отсос?"
                elif Ch_Focus is StormX:
                        ch_s "Еще один минет?"
                elif Ch_Focus is JubesX:
                        ch_v "Ооо, вернулся за добавкой?"
                elif Ch_Focus is GwenX:
                        ch_g "Ох, еще раз? . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Ох, желаешь еще раз? . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Ты хочешь, чтобы я полизал тебя еще немного?"
                elif Ch_Focus is WandaX:
                        ch_w "Желаешь еще один минет?"
            else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.ArmPose = 2
                if Ch_Focus is JubesX:
                    $ Line = renpy.random.choice(["Хочешь. . . [изображает отсос]?",
                        "Ооо, еще один минет?",
                        "Хочешь, чтобы я облизала тебя?",
                        "Хочешь, чтобы я немного пососала тебе?",
                        "Хочешь минет?"])
                elif Ch_Focus is BetsyX:
                    $ Line = renpy.random.choice(["Хочешь, чтобы я. . . [изображает отсос]?",
                        "Желаешь еще один минет?",
                        "Хочешь, чтобы я полизала твой член?",
                        "Хочешь, чтобы я отсосала твой член?",
                        "Небольшой минет?"])
                else:
                    $ Line = renpy.random.choice(["Хочешь. . . [изображает минет]?",
                        "Хочешь еще один минет?",
                        "Хочешь, чтобы я облизала его?",
                        "Хочешь, чтобы я отсосала тебе?",
                        "Немного минета?",
                        "Ты спрашиваешь, голодна ли я?",
                        "Отсосать?",
                        "Подойди поближе."])
                call AnyLine(Ch_Focus,Line)
            $ Line = 0
            #end Second time+ dialog

    if Approval >= 2:
            #She's into it. . .
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Obed", 90, 1)
                $ Ch_Focus.Statup("Inbt", 60, 1)
                if Ch_Focus is JubesX:
                        ch_v "Ладно, твоя взяла."
                elif Ch_Focus in (EmmaX,StormX,BetsyX):
                        call AnyLine(Ch_Focus,"Хорошо.")
                else:
                        call AnyLine(Ch_Focus,"Ладно.")
            elif "no blow" in Ch_Focus.DailyActions:
                $ Line = renpy.random.choice(["Пожалуй, это я могу.",
                    "Ох, хорошо.",
                    "Ладно.",
                    "Наверное, это я могу. . .",
                    "Ох, хорошо. . . [Она жестом подзывает вас к себе].",
                    "Ох, ладно."])
                call AnyLine(Ch_Focus,Line)
            else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Statup("Love", 90, 1)
                $ Ch_Focus.Statup("Inbt", 50, 3)
                if Ch_Focus in (EmmaX,StormX,BetsyX):
                    $ Line = renpy.random.choice(["Что ж, хорошо.",
                        "Что ж. . . ладно.",
                        "Мммм.",
                        "Конечно, дай мне свой член.",
                        "Хорошо. . . [Она облизывает свои губы].",
                        "Что ж, хорошо."])
                else:
                    $ Line = renpy.random.choice(["Ну, конечно. Аааах.",
                        "Ну. . . хорошо.",
                        "Ням.",
                        "Конечно, доставай свой член.",
                        "Хорошо. . . [Она облизывает свои губы].",
                        "Хех. Ладно, хорошо."])
                call AnyLine(Ch_Focus,Line)
                $ Line = 0
            $ Ch_Focus.Statup("Obed", 20, 1)
            $ Ch_Focus.Statup("Obed", 70, 1)
            $ Ch_Focus.Statup("Inbt", 80, 2)
            jump Girl_BJ_Prep
    elif Ch_Focus is JubesX and not Ch_Focus.Taboo:
            #if Jubilee's not in public, she's down.
            if JubesX.Blow > 3 and "angry" not in JubesX.RecentActions:
                $ JubesX.FaceChange("sexy", 1)
                $ JubesX.Statup("Love", 90, 2)
                $ JubesX.Statup("Love", 70, 1)
                $ JubesX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Конечно. Мммм. . .",
                    "Нууу. . . конечно!",
                    "Ням.",
                    "Конечно, дай мне посмотреть на него.",
                    "Ладно. . . [Она облизывает свои губы].",
                    "Ладно, клево."])
                ch_v "[Line]"
                $ Line = 0
                $ JubesX.Statup("Obed", 20, 1)
                $ JubesX.Statup("Obed", 70, 1)
                $ JubesX.Statup("Inbt", 80, 2)
                jump Girl_BJ_Prep
            ch_v "Ok, sure."
            menu:
                extend ""
                "Извини, заб- Что?" if "no blow" in JubesX.DailyActions:
                    $ JubesX.FaceChange("sad")
                    ch_v "Не давай заднюю. . ."
                    $ JubesX.FaceChange("sexy")
                "Может, в др- а?" if "no blow" not in JubesX.DailyActions:
                    $ JubesX.FaceChange("sexy")
                    ch_v "Я сказала. . . конечно."
                    $ JubesX.Statup("Love", 80, 2)
                    $ JubesX.Statup("Inbt", 70, 2)
                "Ну давай, пож- подожди, что?":
                    $ JubesX.FaceChange("sexy")
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Inbt", 70, 3)
                    $ JubesX.Statup("Inbt", 40, 2)
                    ch_v "Я сказала. . . конечно."
                "Соси, [JubesX.Pet].":                                                    # Pressured into it
                    $ JubesX.NameCheck() #checks reaction to petname
                    $ JubesX.FaceChange("confused")
                    $ Approval = ApprovalCheck(JubesX, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                    if Approval > 1 or (Approval and JubesX.Forced):
                        $ JubesX.Statup("Love", 70, -5, 1)
                        $ JubesX.Statup("Love", 200, -2)
                        ch_v "Ладно. . . расслабься. . ."
                        $ JubesX.FaceChange("sly")
                        ch_v "Я ведь сказала, что мне бы и самой этого хотелось. . ."
                        $ JubesX.Statup("Obed", 50, 4)
                        $ JubesX.Statup("Inbt", 80, 1)
                        $ JubesX.Statup("Inbt", 60, 3)
                        $ JubesX.Forced = 1
                    else:
                        $ JubesX.Statup("Love", 200, -5)
                        h_v "Ох, не порти момент. . ."
                "Клево.":
                        $ JubesX.FaceChange("sly")
                        $ JubesX.Statup("Love", 80, 2)
                        $ JubesX.Statup("Obed", 50, 2)
                        $ JubesX.Statup("Obed", 70, 1)
                        $ JubesX.Statup("Inbt", 70, 2)
            if not JubesX.Blow:
                    ch_v "Мне нужно попробовать. . ."
            else:
                    ch_v "Я просто не могу удержаться."
            jump Girl_BJ_Prep
            #end Jubilee's detour
    else:
        #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("angry")
        if "no blow" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"noday") #"I don't think I've been confusing on this one."
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"tabnoday") #"Like I said, I don't do that sort of thing. . . -in public-."
        elif not Ch_Focus.Blow:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "Не думаю, что мне понравится вкус, [RogueX.Petname]. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Я не уверена, что хочу его пробовать на вкус, [KittyX.Petname]. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Не уверена, что ты соответствуешь моим предпочтениям, [EmmaX.Petname]. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Я не уверена, будет ли твой вкус соответствовать твоему запаху, [LauraX.Petname]. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Мне интересно, каков ты на вкус, [JeanX.Petname], но. . ."
            elif Ch_Focus is StormX:
                    ch_s "Я не уверена, что мне это понравится, [StormX.Petname]. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Я не уверена. . . [JubesX.Petname]. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Серьезно, [GwenX.Petname]. . ?"
            elif Ch_Focus is BetsyX:
                    ch_b "Ты серьезно, [BetsyX.Petname]. . ?"
            elif Ch_Focus is DoreenX:
                    ch_d "Серьезно, [Ch_Focus.Petname]. . ?"
            elif Ch_Focus is WandaX:
                    ch_w "Ты сейчас серьезно, [WandaX.Petname]. . ?"
        else:
            $ Ch_Focus.FaceChange("bemused")
            if Ch_Focus is RogueX:
                    ch_r "Нет, не сейчас, [RogueX.Petname]. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Не сейчас, ладно?"
            elif Ch_Focus is EmmaX:
                    ch_e "Сейчас я бы предпочла этого не делать."
            elif Ch_Focus is LauraX:
                    ch_l "Нет."
            elif Ch_Focus is JeanX:
                    ch_j "Не-а."
            elif Ch_Focus is StormX:
                    ch_s "Сейчас я бы предпочла этого не делать."
            elif Ch_Focus is JubesX:
                    ch_v "Я не уверена. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Не."
            elif Ch_Focus is BetsyX:
                    ch_b "О боже, нет."
            elif Ch_Focus is DoreenX:
                    ch_d "Я. . . не хочу."
            elif Ch_Focus is WandaX:
                    ch_w "Хмм. . . я так не думаю."
        menu:
            extend ""
            "Извини, забудь." if "no blow" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("bemused")
                call Sex_Basic_Dialog(Ch_Focus,"noproblem") #"Oh, thanks, I understand. . ."
                return
            "Может, в другой раз?" if "no blow" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy")
                call Sex_Basic_Dialog(Ch_Focus,"maybe") #". . . maybe."
                $ Ch_Focus.Statup("Love", 80, 2)
                $ Ch_Focus.Statup("Inbt", 70, 2)
                if Ch_Focus.Taboo:
                    $ Ch_Focus.RecentActions.append("tabno")
                    $ Ch_Focus.DailyActions.append("tabno")
                $ Ch_Focus.RecentActions.append("no blow")
                $ Ch_Focus.DailyActions.append("no blow")
                return
            "Ну давай, пожалуйста?":
                if Approval or Ch_Focus is JubesX:
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 90, 2)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                    $ Ch_Focus.Statup("Inbt", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Конечно, ааааах.",
                        "Ну. . . ладно.",
                        "Думаю, попробовать не помешает.",
                        "Думаю, можно. . . доставай свой член.",
                        "Ладно. . . [Она облизывает свои губы].",
                        "Хм, ладно."])
                    call AnyLine(Ch_Focus,Line)
                    $ Line = 0
                    jump Girl_BJ_Prep
                else:
                    if ApprovalCheck(Ch_Focus, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ Ch_Focus.Statup("Inbt", 80, 1)
                        $ Ch_Focus.Statup("Inbt", 60, 3)
                        $ Ch_Focus.FaceChange("confused", 1)
                        $ Ch_Focus.ArmPose = 2
                        if Ch_Focus.Hand:
                            if Ch_Focus is RogueX:
                                    ch_r "Может согласишься на подрочить?"
                            elif Ch_Focus is KittyX:
                                    ch_k "Может я лучше[KittyX.like]подрочу тебе?"
                            elif Ch_Focus is EmmaX:
                                    ch_e "Может, вместо этого я тебе подрочу?"
                            elif Ch_Focus is LauraX:
                                    ch_l "Может я лучше подрочу тебе?"
                            elif Ch_Focus is JeanX:
                                    ch_j "Может, тогда лучше согласишься на мою руку?"
                            elif Ch_Focus is StormX:
                                    ch_s "Может, вместо этого я тебе подрочу?"
                            #elif Ch_Focus is JubesX:
                            elif Ch_Focus is GwenX:
                                    ch_g "Может, я лучше подрочу?"
                            elif Ch_Focus is BetsyX:
                                    ch_b "Может, я тебе лучше подрочу?"
                            elif Ch_Focus is DoreenX:
                                    h_d "Эм, может я лучше тебе подрочу?"
                            elif Ch_Focus is WandaX:
                                    ch_w "Что ж, может, выберешь дрочку?"
                        menu:
                            extend ""
                            "Конечно, я не против.":
                                $ Ch_Focus.Statup("Love", 80, 2)
                                $ Ch_Focus.Statup("Inbt", 60, 1)
                                $ Ch_Focus.Statup("Obed", 50, 1)
                                jump Girl_HJ_Prep
                            "Нет, я согласен только на минет.":
                                $ Ch_Focus.Statup("Love", 200, -2)
                                $ Ch_Focus.ArmPose = 1
                                $ Line = renpy.random.choice(["Ну, тебе же хуже.",
                                    "Ладно, как хочешь.",
                                    "Что ж, жаль. . .",
                                    "Ну нет, так нет.",
                                    "Хм. . ."])
                                call AnyLine(Ch_Focus,Line)
                                $ Ch_Focus.Statup("Obed", 70, 2)

            "Соси, [Ch_Focus.Pet].":                                               # Pressured into it
                $ Ch_Focus.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(Ch_Focus, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -5, 1)
                    $ Ch_Focus.Statup("Love", 200, -2)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #"Oh, fine."
                    $ Ch_Focus.Statup("Obed", 50, 4)
                    $ Ch_Focus.Statup("Inbt", 80, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    $ Ch_Focus.Forced = 1
                    jump Girl_BJ_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -15)
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    #She refused all offers.
    if "no blow" in Ch_Focus.DailyActions:
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.ArmPose = 2
        call Sex_Basic_Dialog(Ch_Focus,"nothanks") #"Quit bugging me."
        $ Ch_Focus.ArmPose = 1
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("angry", 1)
        if Ch_Focus is RogueX:
                ch_r "Это не то, чего бы я хотела!"
        elif Ch_Focus is KittyX:
                ch_k "Я не могу!"
        elif Ch_Focus is EmmaX:
                ch_e "Ты заходишь слишком далеко!"
        elif Ch_Focus is LauraX:
                $ LauraX.ArmPose = 2
                $ LauraX.Claws = 1
                ch_l "Выкуси."
                $ LauraX.ArmPose = 1
                $ LauraX.Claws = 0
        elif Ch_Focus is JeanX:
                $ JeanX.FaceChange("angry", 1)
                $ JeanX.ArmPose = 2
                ch_j "Ты хочешь, чтобы я заставила тебя сосать самому себе?"
                $ JeanX.ArmPose = 1
                $ JeanX.FaceChange("angry",1,Eyes="side")
                ch_j "Черт. . . я забыла, что не могу. . ."
        elif Ch_Focus is StormX:
                ch_s "Ты заходишь слишком далеко!"
        elif Ch_Focus is JubesX:
                ch_v "Хотела бы я это сделать, но. . ."
        elif Ch_Focus is GwenX:
                ch_g "Сам соси."
        elif Ch_Focus is BetsyX:
                ch_b ". . . Я бы предпочла этого не делать."
        elif Ch_Focus is DoreenX:
                ch_d "Я не могу, извини."
        elif Ch_Focus is WandaX:
                ch_w "Я не могу, прости."
        $ Ch_Focus.Statup("Lust", 200, 5)
        if Ch_Focus.Love > 300:
                $ Ch_Focus.Statup("Love", 70, -2)
        $ Ch_Focus.Statup("Obed", 50, -2)
        $ Ch_Focus.RecentActions.append("angry")
        $ Ch_Focus.DailyActions.append("angry")
        $ Ch_Focus.RecentActions.append("no blow")
        $ Ch_Focus.DailyActions.append("no blow")
        return
    elif Ch_Focus.Taboo:                             # she refuses and this is too public a place for her
        $ Ch_Focus.FaceChange("angry", 1)
        $ Ch_Focus.DailyActions.append("tabno")
        call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You can't do that here!"
        $ Ch_Focus.Statup("Lust", 200, 5)
        $ Ch_Focus.Statup("Obed", 50, -3)
        return
    elif Ch_Focus.Blow:
        $ Ch_Focus.FaceChange("sad")
        if Ch_Focus is RogueX:
                ch_r "Кажется, теперь у меня во рту появился неприятный привкус, спасибо."
        elif Ch_Focus is KittyX:
                ch_k "Я не в настроение сегодня. . ."
        elif Ch_Focus is EmmaX:
                ch_e "Я бы не хотела подобного. . ."
        elif Ch_Focus is LauraX:
                ch_l "Мне сегодня не хочется. . ."
        elif Ch_Focus is JeanX:
                ch_j "Мне сегодня не хочется. . ."
        elif Ch_Focus is StormX:
                ch_s "Я совсем не в настроении, [StormX.Petname]."
        elif Ch_Focus is JubesX:
                ch_v "Не сейчас. . ."
        elif Ch_Focus is GwenX:
                ch_g "Эм, не сегодня. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Меня это не интересует. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Эм, не сегодня. . ."
        elif Ch_Focus is WandaX:
                ch_w "Хм, не сегодня. . ."
    else:
        $ Ch_Focus.FaceChange("normal", 1)
        if Ch_Focus is RogueX:
                ch_r "Я бы этого не хотела."
        elif Ch_Focus is KittyX:
                ch_k "Я не хочу прикасаться к нему."
        elif Ch_Focus is EmmaX:
                ch_e "Нет, я так не думаю, [EmmaX.Petname]."
        elif Ch_Focus is LauraX:
                ch_l "Я бы предпочла не прикасаться к нему."
        elif Ch_Focus is JeanX:
                ch_j "Ха! Хорошая попытка."
        elif Ch_Focus is StormX:
                ch_s "Не думаю, что соглашусь."
        elif Ch_Focus is JubesX:
                ch_v "Я не в настроении."
        elif Ch_Focus is GwenX:
                ch_g "Эм, нет, спасибо."
        elif Ch_Focus is BetsyX:
                ch_b "Я бы. . . очень не хотела этого делать."
        elif Ch_Focus is DoreenX:
                ch_d "Эм, нет, спасибо."
        elif Ch_Focus is WandaX:
                ch_w "У меня нет никакого желания делать это."
    $ Ch_Focus.RecentActions.append("no blow")
    $ Ch_Focus.DailyActions.append("no blow")
    $ Tempmod = 0
    return


label Girl_BJ_Prep:
##    #fix remove
#    if Ch_Focus is WandaX:
#        "Not currently available."
#        return
##    #fix remove

    if Ch_Focus is DoreenX and not Ch_Focus.Blow and Situation != Ch_Focus:
            #teeth stuff
            ch_d "Ты не беспокоишься о- [[она показывает на свои зубы]?"
            menu:
                extend ""
                "Да не особо":
                        $ Ch_Focus.Statup("Love", 80, 3)
                        ch_d "Ох, ладно. . ."
                "Немного.":
                        $ Ch_Focus.Statup("Inbt", 80, 3)
                        ch_d "Ох. . . не надо."
                        ch_d "Наверное."
                "Я видал и похуже." if JubesX.Blow:
                        ch_d "А?"
                        $ Ch_Focus.Statup("Obed", 80, 3)
                        $ Ch_Focus.Statup("Lust", 70, 2)
                        ch_d "Ооооооо. . ."
                        ch_d "Ты про [JubesX.Name_vin], да?"
                ". . .":
                        ch_d "Лаааааадно. . ."
            ch_d "Думаю, я смогу сделать все аккуратно. . ."
    #end Girl stuff

    if not Player.Male:
            call Girl_CUN_Prep
            return
    if renpy.showing(Ch_Focus.Tag+"_HJ_Animation"):
            $ renpy.hide(Ch_Focus.Tag+"_HJ_Animation")
    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)

    $ Ch_Focus.FaceChange("sexy")
    if Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("sad")
    elif not Ch_Focus.Blow:
        $ Ch_Focus.Brows = "confused"
        $ Ch_Focus.Eyes = "sexy"
        $ Ch_Focus.Mouth = "smile"

    call Seen_First_Peen(Ch_Focus,Partner,React=Situation)
    if "69" in Ch_Focus.History and Ch_Focus.Pose != "69":
            menu:
                "Желаете перейти в позу 69?"
                "Да":
                        $ Ch_Focus.Pose = "69"
                "Нет":
                        $ Ch_Focus.Pose = 0
    call expression Ch_Focus.Tag + "_BJ_Launch" pass ("L") #call Girl_BJ_Launch("L")
    if Situation == Ch_Focus:
            #Girl auto-starts
            $ Situation = 0
            #"[Ch_Focus.Name] slides down and gives your cock a little lick."
            menu:
                "Что будете делать?"
                "Ничего не делать.":
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    $ Ch_Focus.Statup("Inbt", 40, 2)
                    "[Ch_Focus.Name] продолжает его лизать."
                "Похвалить ее.":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    ch_p "Хмммм, [DoreenX.Pet], продолжай."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] продолжает свои действия."
                    $ Ch_Focus.Statup("Love", 85, 1)
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    $ Ch_Focus.FaceChange("surprised")
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    ch_p "[Ch_Focus.Name], давай не сейчас."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] отстраняется."
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ Ch_Focus.AddWord(1,"refused","refused")
                    return
    if not Ch_Focus.Blow:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -70)
            $ Ch_Focus.Statup("Obed", 70, 45)
            $ Ch_Focus.Statup("Inbt", 80, 60)
        else:
            $ Ch_Focus.Statup("Love", 90, 5)
            $ Ch_Focus.Statup("Obed", 70, 35)
            $ Ch_Focus.Statup("Inbt", 80, 40)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no blow")
    $ Ch_Focus.RecentActions.append("blow")
    $ Ch_Focus.DailyActions.append("blow")

label Girl_BJ_Cycle: #Repeating strokes
    while Round > 0:
#        call Shift_Focus(Girl)
        $ Player.Sprite = 1
        call expression Ch_Focus.Tag + "_BJ_Launch" pass ("L") #call Girl_BJ_Launch
        $ Trigger = "blow"
        $ Ch_Focus.LustFace()

        if Player.Focus < 100:
                    if "setpace" in Ch_Focus.RecentActions:
                            $ D20 = renpy.random.randint(1, 20)
                            if Ch_Focus.Blow < 5:
                                $ D20 -= 10
                            elif Ch_Focus.Blow < 10:
                                $ D20 -= 5

                            if D20 > 17:
                                $ Speed = 4
                                # Modification mode
                                $ refresh_animations_girl(Ch_Focus.Tag,"BJ")
                                # -----------------
                            elif D20 > 13:
                                $ Speed = 3
                                # Modification mode
                                $ refresh_animations_girl(Ch_Focus.Tag,"BJ")
                                # -----------------
                            elif D20 > 9:
                                $ Speed = 2
                                # Modification mode
                                $ refresh_animations_girl(Ch_Focus.Tag,"BJ")
                                # -----------------
                            elif D20 > 5:
                                $ Speed = 1
                                # Modification mode
                                $ refresh_animations_girl(Ch_Focus.Tag,"BJ")
                                # -----------------
                    #Player Command menu
                    menu:
                        "Продолжать. . ." if Speed:
                                    pass

                        "Облизывай его. . ." if Speed != 1:
                                # Modification mode
                                $ play_music(name=audio.girl_blowjob)
                                # -----------------

                                $ Ch_Focus.DrainWord("setpace",1,0,0,0)
                                $ Speed = 1
                        "Облизывай его. . . (locked)" if Speed == 1:
                                pass

                        "Возьми в рот головку. . ." if Speed != 2:
                                # Modification mode
                                $ play_music(name=audio.girl_blowjob)
                                # -----------------

                                $ Ch_Focus.DrainWord("setpace",1,0,0,0)
                                $ Speed = 2
                        "Возьми в рот головку. . . (locked)" if Speed == 2:
                                pass

                        "Соси его." if Speed != 3:
                                # Modification mode
                                $ play_music(name=audio.girl_blowjob)
                                # -----------------

                                $ Ch_Focus.DrainWord("setpace",1,0,0,0)
                                $ Speed = 3
                                if Trigger2 == "jackin":
                                    "Она опускает голову чуть ниже и вы убираете свою руку."

                        "Соси его. (locked)" if Speed == 3:
                                pass

                        "Заглоти его." if Speed != 4:
                                # Modification mode
                                $ play_music(name=audio.girl_blowjob)
                                # -----------------

                                $ Ch_Focus.DrainWord("setpace",1,0,0,0)
                                if Trigger2 == "jackin" and Speed != 3:
                                    "Она заглатывает ваш член по самые яйца, а вы убираете свою руку."
                                $ Speed = 4
                        "Заглоти его. (locked)" if Speed == 4:
                                pass

                        "Делай, что тебе больше хочется. . .":
                                "[Ch_Focus.Name] издает звук согласия."
                                if "setpace" not in Ch_Focus.DailyActions:
                                    $ Ch_Focus.Statup("Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if Ch_Focus.Blow < 5:
                                    $ D20 -= 10
                                elif Ch_Focus.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    call Speed_Shift(4)
                                    if "setpace" not in Ch_Focus.DailyActions:
                                        $ Ch_Focus.Statup("Inbt", 80, 3)
                                elif D20 > 10:
                                    $ Speed = 3
                                elif D20 > 5:
                                    $ Speed = 2
                                else:
                                    $ Speed = 1
                                $ Ch_Focus.AddWord(1,"setpace","setpace")

                        "69 [[недоступно] (locked)" if "69" not in Ch_Focus.History:
                                    pass
                        "69" if Ch_Focus.Pose != "69" and ("69" in Ch_Focus.History and "69" in Player.History and Ch_Focus.SEXP >= 30):
                                    # Modification mode
                                    $ play_music(name=audio.girl_blowjob)
                                    # -----------------

                                    $ Ch_Focus.Pose = "69"
                                    call expression Ch_Focus.Tag + "_BJ_Launch" #call Girl_BJ_Launch
                                    jump Girl_BJ_Cycle
                        "Stand-Up" if Ch_Focus.Pose == "69":
                                    $ Ch_Focus.Pose = 0
                                    call expression Ch_Focus.Tag + "_BJ_Launch" #call Girl_BJ_Launch
                                    jump Girl_BJ_Cycle

                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0

                        "Другие варианты":
                                menu:
                                    "Начать также ласкать ее грудь." if Trigger2 != "fondle breasts":
                                            if Ch_Focus.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "Вы начинаете ласкать ее грудь."
                                                $ Ch_Focus.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Дополнительное действие" if Ch_Focus.Loc == bg_current and Ch_Focus.Pose == "69":
                                            if Ch_Focus.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                    $ Ch_Focus.Action -= 1
                                            else:
                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Сменить основное действие":
                                            if Ch_Focus.Action and MultiAction:
                                                    menu:
                                                        "Может, подрочишь мне рукой?":
                                                                if Ch_Focus.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Girl_BJ_After
                                                                    call Girl_Handjob
                                                                else:
                                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        "Может, подрочишь мне сиськами?":
                                                                if Ch_Focus.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Girl_BJ_After
                                                                    call Girl_Titjob
                                                                else:
                                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        "Неважно":
                                                                jump Girl_BJ_Cycle
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

                                            "Не бросай свое текущее занятие. . .(locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_BJ_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_BJ_Cycle
                                            "Неважно":
                                                        jump Girl_BJ_Cycle

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife
                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_BJ_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_BJ_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_BJ_After
        #End menu (if Line)

#        call Shift_Focus(Girl)
        call Sex_Dialog(Ch_Focus,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1
        if Speed:
            $ Player.Wet = 1 #wets penis
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Ch_Focus)
                            if "angry" in Ch_Focus.RecentActions:
                                call expression Ch_Focus.Tag + "_BJ_Reset" #call Girl_BJ_Reset
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2 and Ch_Focus.SEXP >= 20:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_BJ_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Girl can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_BJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."

                            if "unsatisfied" in Ch_Focus.RecentActions:#And Ch_Focus is unsatisfied,
                                "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                menu:
                                    "Хотите завершить начатое?"
                                    "Продолжим еще немного.":
                                        $ Line = "Вы возвращаетесь к процессу"
                                    "С меня хватит.":
                                        "Вы заканчиваете веселье."
                                        jump Girl_BJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Ch_Focus is JubesX and Cnt == (10 + Ch_Focus.Blow):
                        ch_v "Thanks, bee-tee-dubs."
        elif Cnt == (10 + Ch_Focus.Blow):
                $ Ch_Focus.Brows = "angry"
                if Ch_Focus is RogueX:
                        ch_r "Я немного устала, [RogueX.Petname]. Может займемся чем-нибудь другим?"
                elif Ch_Focus is KittyX:
                        ch_k "Мне[KittyX.like]надоело. Давай займемся чем-нибудь другим?"
                elif Ch_Focus is EmmaX:
                        ch_e "Я немного устала, не могли бы мы заняться чем-нибудь другим?"
                elif Ch_Focus is LauraX:
                        ch_l "Мне скучно. Может займемся чем-нибудь другим?"
                elif Ch_Focus is JeanX:
                        ch_j "Ладно, хватит. Может, займемся чем-нибудь другим?"
                elif Ch_Focus is StormX:
                        ch_s "У меня челюсь сводит, мы можем заняться чем-нибудь другим?"
                elif Ch_Focus is JubesX:
                        ch_v "Я устала."
                elif Ch_Focus is GwenX:
                        ch_g "Слушай, эм. . . ты уже скоро?"
                elif Ch_Focus is BetsyX:
                        ch_b "Спрашиваю из чистого любопытства, мы скоро закончим?"
                elif Ch_Focus is DoreenX:
                        ch_d "Мы. . . скоро. . . закончим?"
                elif Ch_Focus is WandaX:
                        ch_w "Ты. . . уже. . . скоро?"
                menu:
                    extend ""
                    "Может, подрочишь мне рукой?" if Ch_Focus.Action and MultiAction:
                            $ Situation = "shift"
                            call Girl_BJ_After
                            call Girl_Handjob
                            return
                    "Закончить." if Player.FocusX:
                            "Вы расслабляетесь. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                            jump Girl_BJ_Cycle
                    "Давай попробуем что-нибудь другое." if MultiAction:
                            $ Line = 0
                            call expression Ch_Focus.Tag + "_BJ_Reset" #call Girl_BJ_Reset
                            $ Situation = "shift"
                            jump Girl_BJ_After
                    "Нет, давай за работу.":
                            if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                $ Ch_Focus.Statup("Love", 200, -5)
                                $ Ch_Focus.Statup("Obed", 50, 3)
                                $ Ch_Focus.Statup("Obed", 80, 2)
                                "Она ворчит, но возвращается к работе."
                            else:
                                $ Ch_Focus.FaceChange("angry", 1)
                                "Она сердито смотрит на вас, отпускает ваш член и отстраняется."
                                if Ch_Focus is RogueX:
                                        ch_r "Занимайся чем хочешь, но без меня."
                                elif Ch_Focus is KittyX:
                                        ch_k "Послушай, если ты будешь вести себя[KittyX.Like]как мудак, то у меня найдутся дела повожнее."
                                elif Ch_Focus is EmmaX:
                                        ch_e "Ты знаешь, у меня есть дела поважнее."
                                elif Ch_Focus is LauraX:
                                        ch_l "У меня есть дела поважнее."
                                elif Ch_Focus is JeanX:
                                        ch_j "У меня есть дела поважнее."
                                elif Ch_Focus is StormX:
                                        ch_s "Возможно, некоторое время в одиночестве поможет тебе переосмыслить свой выбор."
                                elif Ch_Focus is JubesX:
                                        ch_v "Ни за что, заканчивай сам."
                                elif Ch_Focus is GwenX:
                                        ch_g "Ну, если такова твоя реакция, я пошла. . ."
                                elif Ch_Focus is BetsyX:
                                        ch_b "Боюсь, тогда тебе придется развлекаться без меня. . ."
                                elif Ch_Focus is DoreenX:
                                        ch_d "Тогда я оставлю тебя. . ."
                                elif Ch_Focus is WandaX:
                                        ch_w "Тогда справляйся сам."
                                $ Ch_Focus.Statup("Love", 50, -3, 1)
                                $ Ch_Focus.Statup("Love", 80, -4, 1)
                                $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                $ Ch_Focus.RecentActions.append("angry")
                                $ Ch_Focus.DailyActions.append("angry")
                                jump Girl_BJ_After
        elif Cnt == (5 + Ch_Focus.Blow) and Ch_Focus.SEXP <= 100 and not ApprovalCheck(Ch_Focus, 1200, "LO"):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Ты уже скоро? У меня сильно болит челюсть."
                    elif Ch_Focus is KittyX:
                            ch_k "Ты уже скоро? У меня челюсть сводит."
                    elif Ch_Focus is EmmaX:
                            ch_e "Ты уже скоро? Я немного устала."
                    elif Ch_Focus is LauraX:
                            ch_l "Ты скоро? Мне скучно."
                    elif Ch_Focus is JeanX:
                            ch_j "Эй, ты уже скоро?"
                    elif Ch_Focus is StormX:
                            ch_s "Ты уже скоро? Я начинаю уставать."
                    elif Ch_Focus is JubesX:
                            ch_v "Ого, это так здорово!"
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе. . . нравится?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Моей. . . техники достаточно?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Я. . . все правильно делаю?"
                    elif Ch_Focus is WandaX:
                            ch_w "Как у тебя дела?"
        #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10)  #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5)  #ch_d "Tic tock, [Ch_Focus.Petname]."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done")  # ch_d "Ok, [Ch_Focus.Petname], breaktime."

label Girl_BJ_After:
    # Modification mode
    $ play_music()
    $ play_sound()
    # -----------------

    $ Ch_Focus.FaceChange("sexy")
    $ Ch_Focus.DrainWord("setpace",1,0,0,0)

    $ Ch_Focus.Blow += 1
    $ Ch_Focus.Action -=1
    $ Ch_Focus.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Ch_Focus.Addictionrate += 1

    call Partner_Like(Ch_Focus,2)

    if Ch_Focus.Tag + " Jobber" in Achievements:
        pass
#    elif Situation == "shift":
#        pass
    elif Ch_Focus.Blow == 1:
            $Ch_Focus.SEXP += 15
            if Ch_Focus.Love >= 500:
                $ Ch_Focus.Mouth = "smile"
                if Ch_Focus is RogueX:
                        ch_r "Это было не так уж и плохо."
                elif Ch_Focus is KittyX:
                        ch_k "Хм, это было неплохо."
                elif Ch_Focus is EmmaX:
                        ch_e "Хм, лучше, чем я себе представляла. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Слушай, а знаешь, было вполне неплохо."
                elif Ch_Focus is JeanX:
                        ch_j "Ммм, да, как я и ожидала, это было очень хорошо. . ."
                elif Ch_Focus is StormX:
                        ch_s "Хм, это, безусловно, было приятно. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Ого. . . это было потрясающе. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Вау, это было очень здорово!"
                elif Ch_Focus is BetsyX:
                        ch_b "Это было весьма бодряще!"
                elif Ch_Focus is DoreenX:
                        ch_d "Это веселее, чем я думала!"
                elif Ch_Focus is WandaX:
                        ch_w "Это было очень вкусно."
            elif Player.Focus <= 20:
                $ Ch_Focus.Mouth = "sad"
                if Ch_Focus is RogueX:
                        ch_r "Ну, я надеюсь, что ты получил хоть какое-то удовольствие."
                elif Ch_Focus is KittyX:
                        ch_k "Надеюсь, тебе понравилось."
                elif Ch_Focus is EmmaX:
                        ch_e "Ты получил все, о чем мечтал?"
                elif Ch_Focus is LauraX:
                        ch_l "Надеюсь, тебе понравилось."
                elif Ch_Focus is JeanX:
                        ch_j "Ну, ты получил желаемое?"
                elif Ch_Focus is StormX:
                        ch_s "Я оправдала твои ожидания?"
                elif Ch_Focus is JubesX:
                        $ JubesX.FaceChange("sexy", 2,Eyes="side")
                        ch_v "Ого. . . "
                        $ JubesX.FaceChange("angry", 1)
                        ch_v "То есть, надеюсь, что тебе понравилось."
                        $ JubesX.FaceChange("bemused", 1)
                elif Ch_Focus is GwenX:
                        ch_g "Ну, могло быть и хуже. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Пожалуй, могло быть и хуже. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Нуу. . . это было интересно. . ."
                elif Ch_Focus is WandaX:
                        ch_w ". . . это было интересно. . ."
    elif Ch_Focus.Blow == 5:
        $ Ch_Focus.FaceChange("smile", 1)
        if Ch_Focus is RogueX:
                ch_r "Думаю, у меня стало неплохо получаться."
        elif Ch_Focus is KittyX:
                ch_k "С каждым разом у меня получается все лучше. . . верно?"
        elif Ch_Focus is EmmaX:
                ch_e "Уверена, это лучшее, что когда-либо с тобой происходило."
        elif Ch_Focus is LauraX:
                ch_l "У меня вель начинает получаться. . . правда?"
        elif Ch_Focus is JeanX:
                ch_j "Мне это нравится. Тебе ведь тоже, верно?"
        elif Ch_Focus is StormX:
                ch_s "Предполагаю, тебе понравилось."
        elif Ch_Focus is JubesX:
                ch_v "Это. . . очень здорово."
                ch_v "То есть, я знаю, что тебе это нравится и все такое, но. . ."
                ch_v "Ого."
        elif Ch_Focus is GwenX:
                ch_g "Я очень хороша."
                ch_g ". . . правда?"
        elif Ch_Focus is BetsyX:
                ch_b "Мне кажется, у меня неплохо получается."
                ch_b ". . . ты согласен?"
        elif Ch_Focus is DoreenX:
                ch_d "Я думаю, у меня теперь получается лучше!"
                $ Ch_Focus.FaceChange("confused", 1)
                ch_d ". . . правда?"
        elif Ch_Focus is WandaX:
                ch_w "У меня неплохо получается, верно?"
        menu:
            "[[кивнуть]":
                    $ Ch_Focus.FaceChange("smile", 1)
                    $ Ch_Focus.Statup("Love", 90, 15)
                    $ Ch_Focus.Statup("Obed", 80, 5)
                    $ Ch_Focus.Statup("Inbt", 90, 10)
            "[[покачать головой]":
                    if ApprovalCheck(Ch_Focus, 500, "O"):
                        $ Ch_Focus.FaceChange("sad", 2)
                        $ Ch_Focus.Statup("Love", 200, -5)
                    else:
                        $ Ch_Focus.FaceChange("angry", 2)
                        $ Ch_Focus.Statup("Love", 200, -25)
                    $ Ch_Focus.Statup("Obed", 80, 10)
                    if Ch_Focus is RogueX:
                            ch_r ". . ."
                    elif Ch_Focus is KittyX:
                            ch_k ". . ."
                    elif Ch_Focus is EmmaX:
                            ch_e ". . ."
                    elif Ch_Focus is LauraX:
                            ch_l ". . ."
                    elif Ch_Focus is JeanX:
                            ch_j ". . ."
                    elif Ch_Focus is StormX:
                            ch_s "Очень жаль."
                    elif Ch_Focus is JubesX:
                            ch_v "Тебе не понравилось?"
                            ch_v "Ладно, буду стараться лучше. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Оу. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Ужас. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Оу, жаль это слышать. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "В тебе столько дерьма. . ."
                    $ Ch_Focus.FaceChange("sad", 1)
            "Ха, шлюха. . ." if Ch_Focus is JubesX:
                    if ApprovalCheck(JubesX, 250, "I"):
                        $ JubesX.FaceChange("sly", 1)
                        ch_v ". . . агась. . ."
                    elif ApprovalCheck(JubesX, 250, "O"):
                        $ JubesX.FaceChange("sad", 1)
                        ch_v ". . . чистая правда."
                    else:
                        $ JubesX.FaceChange("angry", 2)
                        $ JubesX.Statup("Love", 200, -10)
                        ch_v ". . ."
                        $ JubesX.FaceChange("sad", 1)
                    $ JubesX.Statup("Obed", 80, 10)
                    $ JubesX.Statup("Inbt", 90, 10)
    #end elif Ch_Focus.Blow == 5:
    elif Ch_Focus.Blow >= 10:
            $ Ch_Focus.FaceChange("smile", 1)
            if Ch_Focus is RogueX:
                    ch_r "Признаюсь, я начинаю получать от этого удовольствие."
            elif Ch_Focus is KittyX:
                    ch_k "Я не могу[KittyX.like]выбросить вкус твоего члена из головы."
            elif Ch_Focus is EmmaX:
                    ch_e "Твой вкус меня опьяняет, [EmmaX.Petname]."
            elif Ch_Focus is LauraX:
                    ch_l "Твой вкус опьяняет."
            elif Ch_Focus is JeanX:
                    $ JeanX.FaceChange("confused", 1,Eyes="side")
                    ch_j "Вау, знаешь. . . мне никогда это особо не нравилось. . ."
                    $ JeanX.FaceChange("smile", 2)
                    ch_j "но, думаю, с тобой все по-другому. . ."
            elif Ch_Focus is StormX:
                    ch_s "Не представляю, почему я так долго обходилась без такого деликатеса, [StormX.Petname]."
            elif Ch_Focus is JubesX:
                    ch_v "Я все никак не могу насытиться. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Твой член не выходит у меня из головы. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Я потрясена тем, насколько это приятно. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "После такого я не могу вернуться к мороженому. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Я не могу от него оторваться. . ."
            $ Achievements.append(Ch_Focus.Tag + " Jobber")
            $ Ch_Focus.SEXP += 5
    $ Tempmod = 0
    if Situation != "shift":
        call expression Ch_Focus.Tag + "_BJ_Reset" #call Girl_BJ_Reset
    call Checkout
    return



# end Ch_Focus.Blowjob                                 //////////////////////////////////////////////////////////////////////////////


## Ch_Focus.Footjob //////////////////////////////////////////////////////////////////////
label Girl_Footjob:
##    #fix remove
#    if Ch_Focus is WandaX:
#        "Not currently available."
#        return
##    #fix remove
    if not Player.Male:
            "Пока не реализовано, извините. . ."
            return
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)
    if Ch_Focus.Foot >= 7: # She loves it
        $ Tempmod += 10
    elif Ch_Focus.Foot >= 3: #You've done it before several times
        $ Tempmod += 7
    elif Ch_Focus.Foot: #You've done it before
        $ Tempmod += 3
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 3

    if Ch_Focus.Addict >= 75 and Ch_Focus.Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 10
    if Ch_Focus.Addict >= 75:
        $ Tempmod += 5

    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (3*Ch_Focus.Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 40
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Ch_Focus.Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10

    if "no foot" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no foot" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if Situation == Ch_Focus:
        #Girl auto-starts
        if Approval > 2:
            if Ch_Focus is EmmaX:
                if Trigger2 == "jackin":
                    "[EmmaX.Name] садится поудобнее и начинает тереть ногой ваш член."
                else:
                    "[EmmaX.Name] одаривает вас хитрой улыбкой и начинает тереть ногой ваш член."
            else:
                    "[Ch_Focus.Name] откидывается назад и начинает тереть ваш член между своими ступнями."
            menu:
                "Что будете делать?"
                "Ничего не делать.":
                    $ Ch_Focus.Statup("Inbt", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 30, 2)
                    "[Ch_Focus.Name] продолжает свои действия."
                "Похвалить ее.":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Inbt", 70, 3)
                    ch_p "Ооох, [Ch_Focus.Pet], это так приятно."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] продолжает свои действия."
                    $ Ch_Focus.Statup("Love", 80, 1)
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    $ Ch_Focus.FaceChange("surprised")
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    ch_p "[Ch_Focus.Name], давай не сейчас."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] отстраняется."
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 1)
                    $ Ch_Focus.Statup("Obed", 30, 2)
                    return
            if Trigger:
                $ Ch_Focus.Offhand = "foot"
                return
            jump Girl_FJ_Prep
        else:
            $ Tempmod = 0
            $ Trigger2 = 0
            return

    if not Ch_Focus.Foot and "no foot" not in Ch_Focus.RecentActions:
        $ Ch_Focus.FaceChange("confused", 2)
        if Ch_Focus is RogueX:
                ch_r "Эм, я еще понимаю, что можно использовать руки, но. . . ножки?"
        elif Ch_Focus is KittyX:
                ch_k "Значит ты хочешь, чтобы я потрогала твой член ногами, да?"
        elif Ch_Focus is EmmaX:
                $ Ch_Focus.FaceChange("sly", 1)
                ch_e "Мммм, значит, тебя привлекают ножки, [EmmaX.Petname]?"
        elif Ch_Focus is LauraX:
                $ Ch_Focus.FaceChange("sly", 1)
                ch_l "Простая дрочка ногами?"
        elif Ch_Focus is JeanX:
                $ Ch_Focus.FaceChange("sly", 1)
                ch_j "Ох, любитель ножек, да?"
        elif Ch_Focus is StormX:
                ch_s "Ох, ты хочешь, чтобы я воспользовалась своими ножками, [StormX.Petname]?"
        elif Ch_Focus is JubesX:
                $ Ch_Focus.FaceChange("sly", 2)
                ch_v "О, так вот значит чего ты хочешь?"
        elif Ch_Focus is GwenX:
                ch_g "Ох! Ты, эм. . . хочешь мои. . . ножки. . ?"
        elif Ch_Focus is BetsyX:
                ch_b "О боже! Ты хочешь мои. . . ножки. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Ох! Ты, эм. . . желаешь мои. . . ножки. . ."
        elif Ch_Focus is WandaX:
                ch_w "Желаешь, чтобы я подрочила тебе ножками?"
        $ Ch_Focus.Blush = 1

    if not Ch_Focus.Foot and Approval:
        #First time dialog
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad",1)
            $ Ch_Focus.Statup("Love", 70, -3, 1)
            $ Ch_Focus.Statup("Love", 20, -2, 1)
        elif Ch_Focus.Love >= (Ch_Focus.Obed + Ch_Focus.Inbt):
            $ Ch_Focus.FaceChange("sexy",1)
            $ Ch_Focus.Brows = "sad"
            $ Ch_Focus.Mouth = "smile"
            if Ch_Focus is RogueX:
                    ch_r "Если тебе такое нравится. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Думаю, это может быть интересно. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Полагаю, ты заслужил что-то особенное. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Думаю, это не повредит. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Наверное, можно. . ."
            elif Ch_Focus is StormX:
                    ch_s "Мне может понравится. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Тебе нравятся мои маленькие пальчики? . ."
            elif Ch_Focus is GwenX:
                    ch_g "Это может быть весело. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Это может быть весело. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Это может быть весело. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Это может быть весело. . ."
        elif Ch_Focus.Obed >= Ch_Focus.Inbt:
            $ Ch_Focus.FaceChange("normal",1)
            if Ch_Focus in (EmmaX,StormX,BetsyX):
                    call AnyLine(Ch_Focus,"Если ты этого хочешь, "+Ch_Focus.Petname+". . .")
            else:
                    call AnyLine(Ch_Focus,"Если это то, чего ты хочешь, "+Ch_Focus.Petname+". . .")
        else: # Uninhibited
            $ Ch_Focus.FaceChange("lipbite",1)
            if Ch_Focus in (EmmaX,StormX):
                    call AnyLine(Ch_Focus,"Хорошо. . .")
            elif Ch_Focus is BetsyX:
                    ch_b "Конечно. . ."
            else:
                $ Line = renpy.random.choice(["Хех. . ." ,
                    "Хмм, это может быть весело. . .",
                    "Пожалуй, можно. . .",
                    "Конечно. . .",
                    "Наверное, можно. . .",
                    "Хмм. . ."])
                call AnyLine(Ch_Focus,Line)
        #end First time dialog

    elif Approval:
        #Second time+ dialog
        if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Love", 70, -3, 1)
                $ Ch_Focus.Statup("Love", 20, -2, 1)
                if Ch_Focus is RogueX:
                        ch_r "Это все, чего ты хочешь?"
                elif Ch_Focus is KittyX:
                        ch_k "И все?"
                elif Ch_Focus is EmmaX:
                        ch_e "Это все, чего ты хочешь?"
                elif Ch_Focus is LauraX:
                        ch_l "И все?"
                elif Ch_Focus is JeanX:
                        ch_j "Это все, чего ты хочешь?"
                elif Ch_Focus is StormX:
                        ch_s "Это все, чего ты хочешь?"
                elif Ch_Focus is JubesX:
                        ch_v "И все?"
                elif Ch_Focus is GwenX:
                        ch_g "О, хочешь только ножки?"
                elif Ch_Focus is BetsyX:
                        ch_b "Только ножки?"
                elif Ch_Focus is DoreenX:
                        ch_d "Ох, только ножки?"
                elif Ch_Focus is WandaX:
                        ch_w "Хочешь только ножки, да?"
        elif not Taboo and "tabno" in Ch_Focus.DailyActions:
                call Sex_Basic_Dialog(Ch_Focus,"tabyes") #"This -would- be a better place for it. . ."
        elif "foot" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Еще раз?",
                    "Тебе все мало?",
                    "Хочешь, чтобы я натерла себе мозоли?",
                    "Мои ножки немного побаливают после прошлого раза.",
                    "Мои ножки вроде как побаливают после прошлого раза."])
                call AnyLine(Ch_Focus,Line)
                if "foot" in Ch_Focus.RecentActions:
                        jump Girl_FJ_Prep
        elif Ch_Focus.Foot < 3:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Brows = "confused"
                $ Ch_Focus.Mouth = "kiss"
                if Ch_Focus is RogueX:
                        ch_r "Снова?"
                elif Ch_Focus is KittyX:
                        ch_k "Хмм, волшебные пальчики ножек. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Ох, хорошо. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Хмм, волшебные пальчики ножек. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Хм, это довольно весело. . ."
                elif Ch_Focus is StormX:
                        ch_s "Ох, хорошо. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Тебе, должно быть, понравилось в прошлый раз. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Мммм, ножки. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Ясно, желаешь ножек. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Мммм, ножки. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Ладно, ножки так ножки. . ."
        else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.ArmPose = 2
                if Ch_Focus in (EmmaX,StormX,BetsyX):
                    $ Line = renpy.random.choice(["Значит, ты предпочитаешь ножки?",
                        "Так, ты хочешь еще одну дрочку ножками?",
                        ". . . [она трется своей ногой о вашу ногу]?",
                        "Немного ласки от ножек?"])
                else:
                    $ Line = renpy.random.choice(["Ты хочешь, чтобы я воспользовалась своими ножками?",
                        "Так ты хочешь еще раз?",
                        "Так ты хочешь, чтобы я. . . [она трется своей ногой о вашу ногу]?",
                        "Так ты хочешь еще раз?"])
                call AnyLine(Ch_Focus,Line)
        $ Line = 0
        #end Second time+ dialog

    if Approval >= 2:
            #She's into it. . .
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Obed", 90, 1)
                $ Ch_Focus.Statup("Inbt", 60, 1)
                if Ch_Focus in (EmmaX,StormX,BetsyX):
                        call AnyLine(Ch_Focus,"Хорошо.")
                else:
                        call AnyLine(Ch_Focus,"Ладно.")
            else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Statup("Love", 90, 1)
                $ Ch_Focus.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Наверное, можно.",
                    "Ох, ладно.",
                    "Хорошо.",
                    "Пожалуй, это можно. . .",
                    "Ох, хорошо. . . [Она подзывает вас жестом].",
                    "Ладно."])
                call AnyLine(Ch_Focus,Line)
                $ Line = 0
            $ Ch_Focus.Statup("Obed", 20, 1)
            $ Ch_Focus.Statup("Obed", 60, 1)
            $ Ch_Focus.Statup("Inbt", 70, 2)
            jump Girl_FJ_Prep
            #End Approval 2

    else:
        #She's not into it, but maybe. . .
        $ Ch_Focus.FaceChange("angry")
        if "no foot" in Ch_Focus.DailyActions:
                call Sex_Basic_Dialog(Ch_Focus,"noday") #"I don't think I've been confusing on this one."
        elif Taboo and "tabno" in Ch_Focus.DailyActions:
                call Sex_Basic_Dialog(Ch_Focus,"tabnoday") #"Like I said, I don't do that sort of thing. . . -in public-."
        elif not Ch_Focus.Foot:
                $ Ch_Focus.FaceChange("bemused")
                if Ch_Focus is RogueX:
                        ch_r ". . . я не уверена, [RogueX.Petname]. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Я не уверена, [KittyX.Petname]. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Я не уверена, [EmmaX.Petname]. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Эм, [LauraX.Petname]. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Ну. . ."
                elif Ch_Focus is StormX:
                        ch_s "Я не уверена, [StormX.Petname]. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Эм, [JubesX.Petname]. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Эм, [GwenX.Petname]. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Эм, [BetsyX.Petname]. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Эм, [Ch_Focus.Petname]. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Хммм. . . я не уверена."
        else:
                $ Ch_Focus.FaceChange("bemused")
                if Ch_Focus is RogueX:
                        ch_r "Нет, не сейчас, [RogueX.Petname]. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Не сейчас, ладно?"
                elif Ch_Focus is EmmaX:
                        ch_e "Сейчас я бы предпочла этого не делать."
                elif Ch_Focus is LauraX:
                        ch_l "Нет."
                elif Ch_Focus is JeanX:
                        ch_j "Не-а."
                elif Ch_Focus is StormX:
                        ch_s "Сейчас я бы предпочла этого не делать."
                elif Ch_Focus is JubesX:
                        ch_v "Я не уверена. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Не."
                elif Ch_Focus is BetsyX:
                        ch_b "Я бы предпочла этого не делать."
                elif Ch_Focus is DoreenX:
                        ch_d "Я. . . не хочу."
                elif Ch_Focus is WandaX:
                        ch_w "Хмм. . . я так не думаю."
        menu:
            extend ""
            "Извини, забудь." if "no foot" in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("bemused")
                    call Sex_Basic_Dialog(Ch_Focus,"noproblem") #"Oh, thanks, I understand. . ."
                    return
            "Может, в другой раз?" if "no foot" not in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("sexy")
                    call AnyLine(Ch_Focus,". . .")
                    call Sex_Basic_Dialog(Ch_Focus,"maybe") #". . . maybe."
                    $ Ch_Focus.Statup("Love", 80, 2)
                    $ Ch_Focus.Statup("Inbt", 70, 2)
                    if Ch_Focus.Taboo:
                        $ Ch_Focus.RecentActions.append("tabno")
                        $ Ch_Focus.DailyActions.append("tabno")
                    $ Ch_Focus.RecentActions.append("no foot")
                    $ Ch_Focus.DailyActions.append("no foot")
                    return
            "Я был бы тебе очень признателен. . .":
                    if Approval:
                        $ Ch_Focus.FaceChange("sexy")
                        $ Ch_Focus.Statup("Obed", 90, 2)
                        $ Ch_Focus.Statup("Obed", 50, 2)
                        $ Ch_Focus.Statup("Inbt", 70, 3)
                        $ Ch_Focus.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Конечно, тогда, пожалуй, можно.",
                            "Хорошо.",
                            "Хорошо, доставай его.",
                            "Пожалуй, тогда я согласна. . .",
                            "Хорошо. . . [Она жестом подзывает вас].",
                            "Хммм, ладно."])
                        call AnyLine(Ch_Focus,Line)
                        $ Line = 0
                        jump Girl_FJ_Prep
#                    else:
#                        pass

            "Давай, приступай.":                                            # Pressured into it
                $ Approval = ApprovalCheck(Ch_Focus, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and Ch_Focus.Forced):
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -5, 1)
                    $ Ch_Focus.Statup("Love", 200, -2)
                    call Sex_Basic_Dialog(Ch_Focus,"forceit") #"Oh, fine."
                    $ Ch_Focus.Statup("Obed", 50, 4)
                    $ Ch_Focus.Statup("Inbt", 80, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 3)
                    $ Ch_Focus.Forced = 1
                    jump Girl_FJ_Prep
                else:
                    $ Ch_Focus.Statup("Love", 200, -15)
                    $ Ch_Focus.RecentActions.append("angry")
                    $ Ch_Focus.DailyActions.append("angry")

    #She refused all offers.
    $ Ch_Focus.ArmPose = 1
    if "no foot" in Ch_Focus.DailyActions:
            $ Ch_Focus.FaceChange("angry", 1)
            call Sex_Basic_Dialog(Ch_Focus,"nothanks") #"Quit bugging me."
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("angry", 1)
            if Ch_Focus is RogueX:
                    ch_r "Никаких ножек."
            elif Ch_Focus is KittyX:
                    ch_k "Я не хочу прикасаться к нему ногами."
            elif Ch_Focus is EmmaX:
                    ch_e "Ты правда хочешь, чтобы мои каблуки были рядом с твоим мужским достоинством?"
            elif Ch_Focus is LauraX:
                    ch_l "Ты же понимаешь, что у меня там тоже есть когти. . ?"
            elif Ch_Focus is JeanX:
                    ch_j "Нет."
            elif Ch_Focus is StormX:
                    ch_s "Не искушай меня показать, на что способны мои ноги."
            elif Ch_Focus is JubesX:
                    ch_v "Неее-а."
            elif Ch_Focus is GwenX:
                    ch_g "Эм. . . нет."
            elif Ch_Focus is BetsyX:
                    ch_b ". . . Я бы предпочла этого не делать."
            elif Ch_Focus is DoreenX:
                    ch_d "Я просто. . . не хочу."
            elif Ch_Focus is WandaX:
                    ch_w ". . . Мне такое не по вкусу."
            $ Ch_Focus.Statup("Lust", 200, 5)
            if Ch_Focus.Love > 300:
                    $ Ch_Focus.Statup("Love", 70, -2)
            $ Ch_Focus.Statup("Obed", 50, -2)
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Taboo:                             # she refuses and this is too public a place for her
            $ Ch_Focus.FaceChange("angry", 1)
            $ Ch_Focus.DailyActions.append("tabno")
            call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You can't do that here!"
            $ Ch_Focus.Statup("Lust", 200, 5)
            $ Ch_Focus.Statup("Obed", 50, -3)
    elif Ch_Focus.Foot:
            $ Ch_Focus.FaceChange("sad")
            if Ch_Focus is RogueX:
                    ch_r "Думаю, на этот раз ты должен справиться сам. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Я не в настроение сегодня. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Я бы не хотела подобного. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Мне сегодня не хочется. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Мне сегодня не хочется. . ."
            elif Ch_Focus is StormX:
                    ch_s ". . . Я бы предпочла этого не делать."
            elif Ch_Focus is JubesX:
                    ch_v "Не сейчас. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Эм, не сегодня. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Меня это не интересует. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Мне. . . сейчас не хочется. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Не сейчас, ладно?"
    else:
            $ Ch_Focus.FaceChange("normal", 1)
            if Ch_Focus is RogueX:
                    ch_r "Я бы этого не хотела."
            elif Ch_Focus is KittyX:
                    ch_k "Я не хочу прикасаться к нему."
            elif Ch_Focus is EmmaX:
                    ch_e "Нет, я так не думаю, [EmmaX.Petname]."
            elif Ch_Focus is LauraX:
                    ch_l "Я бы предпочла не прикасаться к нему."
            elif Ch_Focus is JeanX:
                    ch_j "Я бы предпочла не трогать его."
            elif Ch_Focus is StormX:
                    ch_s "Нет, я так не думаю, [StormX.Petname]."
            elif Ch_Focus is JubesX:
                    ch_v "Я не в настроении."
            elif Ch_Focus is GwenX:
                    ch_g "Эм, нет, спасибо."
            elif Ch_Focus is BetsyX:
                    ch_b "Я бы. . . предпочла этим не заниматься."
            elif Ch_Focus is DoreenX:
                    ch_d ". . . Не думаю, что хочу этого. . ."
            elif Ch_Focus is WandaX:
                    ch_w "У меня нет никакого желания делать это."
    $ Ch_Focus.RecentActions.append("no foot")
    $ Ch_Focus.DailyActions.append("no foot")
    $ Tempmod = 0
    return


label Girl_FJ_Prep:
##    #fix remove
#    if Ch_Focus is WandaX:
#        "Not currently available."
#        return
##    #fix remove
    if Trigger2 == "foot":
        return

    if Ch_Focus.Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)

    $ Ch_Focus.FaceChange("sexy")
    if Ch_Focus.Forced:
        $ Ch_Focus.FaceChange("sad")
    elif not Ch_Focus.Foot:
        $ Ch_Focus.Brows = "confused"
        $ Ch_Focus.Eyes = "sexy"
        $ Ch_Focus.Mouth = "smile"

    call Seen_First_Peen(Ch_Focus,Partner,React=Situation)

    if Situation == Ch_Focus:
        #Girl auto-starts
        $ Situation = 0
        if Ch_Focus is EmmaX:
            if Trigger2 == "jackin":
                "[EmmaX.Name] садится поудобнее и начинает тереть ногой ваш член."
            else:
                "[EmmaX.Name] одаривает вас хитрой улыбкой и начинает тереть ногой ваш член."
        else:
                "[Ch_Focus.Name] откидывается назад и начинает тереть ваш член своей ногой."
        menu:
            "Что будете делать?"
            "Ничего не делать.":
                $ Ch_Focus.Statup("Inbt", 70, 3)
                $ Ch_Focus.Statup("Inbt", 30, 2)
                "[Ch_Focus.Name] продолжает свои действия."
            "Похвалить ее.":
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Statup("Inbt", 70, 3)
                ch_p "Ооох, [Ch_Focus.Pet], это так приятно."
                $ Ch_Focus.NameCheck() #checks reaction to petname
                "[Ch_Focus.Name] продолжает свои действия."
                $ Ch_Focus.Statup("Love", 80, 1)
                $ Ch_Focus.Statup("Obed", 90, 1)
                $ Ch_Focus.Statup("Obed", 50, 2)
            "Сказать ей остановиться.":
                $ Ch_Focus.FaceChange("surprised")
                $ Ch_Focus.Statup("Inbt", 70, 1)
                ch_p "[Ch_Focus.Name], давай не сейчас."
                $ Ch_Focus.NameCheck() #checks reaction to petname
                "[Ch_Focus.Name] отстраняется."
                $ Ch_Focus.Statup("Obed", 90, 1)
                $ Ch_Focus.Statup("Obed", 50, 1)
                $ Ch_Focus.Statup("Obed", 30, 2)
                return

    if not Ch_Focus.Foot:
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -20)
            $ Ch_Focus.Statup("Obed", 70, 25)
            $ Ch_Focus.Statup("Inbt", 80, 30)
        else:
            $ Ch_Focus.Statup("Love", 90, 5)
            $ Ch_Focus.Statup("Obed", 70, 20)
            $ Ch_Focus.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Ch_Focus.Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no foot")
    $ Ch_Focus.RecentActions.append("foot")
    $ Ch_Focus.DailyActions.append("foot")
    if Ch_Focus.Pose != "doggy" and Ch_Focus.Pose != "sex":
        menu:
            "Лицом или спиной к вам?"
            "Лицом" if Ch_Focus is EmmaX:
                    $ Ch_Focus.Pose = "foot"
            "Лицом" if Ch_Focus is not EmmaX:
                    $ Ch_Focus.Pose = "sex"
            "Спиной":
                    $ Ch_Focus.Pose = "doggy"

label Girl_FJ_Cycle:
    while Round > 0:
#        call Shift_Focus(Girl)
        call expression Ch_Focus.Tag + "_Sex_Launch" pass ("foot") #call Girl_Sex_Launch("foot")
        $ Ch_Focus.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . ." if Speed:
                                    pass

                        "Начать? . ." if not Speed:
                                    # Modification mode
                                    if is_playing_music(audio.girl_feetjob):
                                        $ play_music(name=audio.girl_feetjob, loop=True)
                                    # -----------------

                                    $ Speed = 1

                        "Быстрее. . ." if Speed < 2:
                                    $ Speed += 1
                                    "Вы просите ее немного ускориться."
                        "Быстрее. . . (locked)" if Speed >= 2:
                                    pass

                        "Помедленнее. . ." if Speed:
                                    $ Speed -= 1
                                    "Вы просите ее немного сбавить темп."
                        "Помедленнее. . . (locked)" if not Speed:
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_FJ_Cycle

                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0

                        "Развернуть ее":
                                    $ Ch_Focus.Pose = "doggy" if Ch_Focus.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Girl_FJ_Cycle

                        "Повернуть ее голову" if Ch_Focus.Pose == "doggy":
                                    call View_Facing(Ch_Focus,1)
                                    jump Girl_FJ_Cycle

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
                                                        "Может, отсосешь?":
                                                                    if Ch_Focus.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Girl_FJ_After
                                                                        call Girl_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        "Может, подрочишь мне рукой?":
                                                                    if Ch_Focus.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Girl_FJ_After
                                                                        call Girl_Handjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")

                                                        "Может, подрочишь мне сиськами?":
                                                                    if Ch_Focus.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Girl_FJ_After
                                                                        call Girl_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")



                                                        "Неважно":
                                                                jump Girl_FJ_Cycle
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

                                            "Не бросай свое текущее занятие. . .(locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_FJ_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_FJ_Cycle
                                            "Неважно":
                                                        jump Girl_FJ_Cycle

                                    "Псионический нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife
                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_FJ_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_FJ_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_FJ_After
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
                                call expression Ch_Focus.Tag + "_Sex_Reset" #call Girl_Sex_Reset
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_FJ_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Girl can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_FJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in Ch_Focus.RecentActions:#And Ch_Focus is unsatisfied,
                                "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                menu:
                                    "Хотите завершить начатое?"
                                    "Продолжим еще немного.":
                                        $ Line = "Вы возвращаетесь к процессу"
                                    "С меня хватит.":
                                        "Вы заканчиваете веселье."
                                        jump Girl_FJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ Ch_Focus.Brows = "angry"
                    if Ch_Focus is RogueX:
                            ch_r "Ох, я все никак к этому не привыкну. Не возражаешь, если мы сделаем перерыв?"
                    elif Ch_Focus is KittyX:
                            ch_k "Ай, у меня ноги сводит, мы можем[KittyX.like]сделать перерыв?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Хмм, у меня ноги сводит, не могли бы мы сделать небольшой перерыв?"
                    elif Ch_Focus is LauraX:
                            ch_l "Хмм, становится слишком скучно."
                    elif Ch_Focus is JeanX:
                            ch_j "Хмм, у меня уже ноги сводит. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Хм, у меня ногу сводит. Не могли бы мы сделать небольшой перерыв?"
                    elif Ch_Focus is JubesX:
                            ch_v "У меня судороги в ногах. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "У меня, эм, ноги сводит."
                    elif Ch_Focus is BetsyX:
                            ch_b "Боюсь, если мы продолжим, у меня могут начаться судороги."
                    elif Ch_Focus is DoreenX:
                            ch_d "У меня, эм, похоже, сводит ногу."
                    elif Ch_Focus is WandaX:
                            ch_w "У меня уже ноги сводит."
                    menu:
                        extend ""
                        "Как насчет отсоса?" if Ch_Focus.Action and MultiAction:
                                $ Situation = "shift"
                                call Girl_FJ_After
                                call Girl_Blowjob
                        "Может, подрочишь мне рукой?" if Ch_Focus.Action and MultiAction:
                                $ Situation = "shift"
                                call Girl_FJ_After
                                call Girl_Handjob
                        "Закончить." if Player.FocusX:
                                "Вы расслабляетесь. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Girl_FJ_Cycle
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                call expression Ch_Focus.Tag + "_Sex_Reset" #call Girl_Sex_Reset
                                $ Situation = "shift"
                                jump Girl_FJ_After
                        "Нет, давай за работу.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она ворчит, но возвращается к работе."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    "Она кидает на вас сердитый взгляд и отстраняется."
                                    if Ch_Focus is RogueX:
                                            ch_r "Занимайся чем хочешь, но без меня."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Послушай, если ты будешь вести себя[KittyX.Like]как мудак, то у меня найдутся дела повожнее."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Ты знаешь, у меня есть дела поважнее."
                                    elif Ch_Focus is LauraX:
                                            ch_l "У меня есть дела поважнее."
                                    elif Ch_Focus is JeanX:
                                            ch_j "У меня есть дела поважнее."
                                    elif Ch_Focus is StormX:
                                            ch_s "Возможно, некоторое время в одиночестве поможет тебе переосмыслить свой выбор."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Ни за что, заканчивай сам."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Ну, если такова твоя реакция, я пошла. . ."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Боюсь, тогда тебе придется развлекаться без меня. . ."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Тогда я оставлю тебя. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Тогда справляйся сам."
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_FJ_After
        elif Cnt == 10 and Ch_Focus.SEXP <= 100 and not ApprovalCheck(Ch_Focus, 1200, "LO"):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Может уже закончим? Мне становится больно."
                    elif Ch_Focus is KittyX:
                            ch_k "Мы можем уже[KittyX.Like]закончить? Мне немного больно."
                    elif Ch_Focus is EmmaX:
                            ch_e "Давай закончим, мои ножки побаливают."
                    elif Ch_Focus is LauraX:
                            ch_l "Ладно, я серьезно, давай попробуем что-нибудь другое."
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно, я серьезно, давай попробуем что-нибудь другое."
                    elif Ch_Focus is StormX:
                            ch_s "Давай закончим, мои ножки побаливают."
                    elif Ch_Focus is JubesX:
                            ch_v "Давай займемся чем-нибудь другим."
                    elif Ch_Focus is GwenX:
                            ch_g "Ладно, я серьезно, давай попробуем что-нибудь другое."
                    elif Ch_Focus is BetsyX:
                            ch_b "Уверена, тебе этого достаточно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ладно, серьезно, давай попробуем что-нибудь другое."
                    elif Ch_Focus is WandaX:
                            ch_w "Все еще продолжаем?"
        #End Count check

        call Escalation(Ch_Focus) #sees if she wants to escalate things

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10)  #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5)  #ch_d "Tic tock, [Ch_Focus.Petname]."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done")  # ch_d "Ok, [Ch_Focus.Petname], breaktime."

label Girl_FJ_After:
    # Modification mode
    $ play_music()
    $ play_sound()
    # -----------------

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.Foot += 1
    $ Ch_Focus.Action -=1
    $ Ch_Focus.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ Ch_Focus.Addictionrate += 1
    $ Ch_Focus.Statup("Lust", 90, 5)

    call Partner_Like(Ch_Focus,1)

    if Ch_Focus.Tag+"pedi" in Achievements:
            pass
    elif Ch_Focus.Foot >= 10:
            $ Ch_Focus.FaceChange("smile", 1)
            if Ch_Focus is RogueX:
                    ch_r "Наверное, я уже привыкла к этим штучкам ногами."
            elif Ch_Focus is KittyX:
                    ch_k "Похоже, я теперь профи в работе ножками."
            elif Ch_Focus is EmmaX:
                    ch_e "Я рада, что тебе нравятся мои ножки."
                    ch_e "Я тренировалась много лет."
            elif Ch_Focus is LauraX:
                    ch_l "Наконец-то я вернулась к практике."
            elif Ch_Focus is JeanX:
                    ch_j "Хм, это довольно весело. . ."
            elif Ch_Focus is StormX:
                    ch_s "Я рада, что ты убедил меня попробовать."
                    ch_s "Это так. . . интимно."
            elif Ch_Focus is JubesX:
                    ch_v "Это вроде как нормально, если привыкнуть. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Ноги. . . на удивление очень чувствительные. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Ножки удивительно. . . чувствительные. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Удивительно, какие. . . чувствительные у нас ступни. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Я рада, что могу использовать свои ножки для этого."
            $ Achievements.append(Ch_Focus.Tag+"pedi")
            $ Ch_Focus.SEXP += 5
    elif Ch_Focus.Foot == 1:
            $ Ch_Focus.SEXP += 10
            if Ch_Focus.Love >= 500:
                $ Ch_Focus.Mouth = "smile"
                if Ch_Focus is RogueX:
                        ch_r "Это были очень интересные ощущения. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Приятно ощупывать тебя ножками. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Твой член был таким горячим. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Тебе понравилось? . ."
                elif Ch_Focus is JeanX:
                        ch_j "Тебе понравилось? . ."
                elif Ch_Focus is StormX:
                        ch_s "Это, безусловно, был интересный опыт. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Ну, что скажешь? . ."
                elif Ch_Focus is GwenX:
                        ch_g "Это было. . . весело!"
                elif Ch_Focus is BetsyX:
                        ch_b "Это было. . . довольно приятно."
                elif Ch_Focus is DoreenX:
                        ch_d "Это было. . . весело!"
                elif Ch_Focus is WandaX:
                        ch_w "Мне очень понравилось!"
            elif Player.Focus <= 20:
                $ Ch_Focus.Mouth = "sad"
                if Ch_Focus is RogueX:
                        ch_r "Ну, я надеюсь, что ты получил хоть какое-то удовольствие."
                elif Ch_Focus is KittyX:
                        ch_k "Ты удовлетворен?"
                elif Ch_Focus is EmmaX:
                        ch_e "Ты удовлетворен?"
                elif Ch_Focus is LauraX:
                        ch_l "Тебе хоть немного понравилось?"
                elif Ch_Focus is JeanX:
                        ch_j "Очень приятно, да?"
                elif Ch_Focus is StormX:
                        ch_s "Ты удовлетворен?"
                elif Ch_Focus is JubesX:
                        ch_v "Твои потребности удовлетворены?"
                elif Ch_Focus is GwenX:
                        ch_g "Ты доволен?"
                elif Ch_Focus is BetsyX:
                        ch_b "Полагаю, ты удовлетворен?"
                elif Ch_Focus is DoreenX:
                        ch_d "Ну? Тебе понравилось?"
                elif Ch_Focus is WandaX:
                        ch_w "Ты доволен?"
    elif Ch_Focus.Foot == 5:
                if Ch_Focus is RogueX:
                        ch_r "Похоже, мне нравятся эти ощущения."
                        ch_r "Никогда бы не подумала, что буду прикасаться к людям своими ножками."
                elif Ch_Focus is KittyX:
                        ch_k "Дай мне знать, когда тебе понадобится \"лишняя пара ног.\""
                elif Ch_Focus is EmmaX:
                        ch_e "Мне понравился этот опыт."
                elif Ch_Focus is LauraX:
                        ch_l "Я потихоньку привыкаю. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Я потихоньку привыкаю. . ."
                elif Ch_Focus is StormX:
                        ch_s "Мне понравился этот опыт."
                elif Ch_Focus is JubesX:
                        ch_v "Хорошо, я начинаю разбираться. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Это веселее, чем я думала. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Это гораздо веселее, чем я ожидала. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Это веселее, чем я думала. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Думаю, я начинаю во всем разбираться. . ."
    $ Tempmod = 0
    if Situation == "shift":
        call Sex_Basic_Dialog(Ch_Focus,"shift") #"Ok, so what else did you want to do?"
    else:
        call expression Ch_Focus.Tag + "_Sex_Reset" #call Girl_Sex_Reset
    call Checkout
    return

## end Ch_Focus.Footjob //////////////////////////////////////////////////////////////////////



label Psychic_Sex(Girl=0,Act=0):
    if Ch_Focus.Addict >= 50 and "ultimatum" in Ch_Focus.RecentActions:
            #skip this if she's addicted
            return
    elif "psysex" in Ch_Focus.History:
            #if you've done it before. . .
            ch_j "Ну что, хочешь еще одну телепатическую дрочку?"
    elif Ch_Focus.Taboo:
            ch_j "Я не хочу заниматься подобным здесь. . ."
            ch_j "А что, если вместо этого я воспользуюсь своими способностями?"
    else:
            ch_j "Я не уверена, хочу ли. . . касаться тебя. . ."
            ch_j "А что, если вместо этого я воспользуюсь своими способностями?"
    menu PS_Menu:
            extend ""
            "Конечно, это было бы здорово.":
                    $ Ch_Focus.Statup("Love", 80, 2)
                    $ Ch_Focus.Statup("Inbt", 70, 2)
                    ch_j "Чудесно. . ."
                    $ Situation = "psy"
                    jump Jean_PJ_Prep
            "Что ты имеешь в виду?" if "psysex" not in Ch_Focus.History and "ask" not in Player.RecentActions:
                    ch_j "Ну знаешь, я могу \"прикасаться\" к предметам используя силу своего разума. . ."
                    $ Ch_Focus.Statup("Inbt", 70, 2)
                    ch_j "К любым предметам. . ."
                    ch_j "Вот так я могу доставить тебе удовольствие. . ."
                    $ Player.RecentActions.append("ask")
                    jump PS_Menu
            "Нет, мне больше нравятся \"реальные\" руки.":
                    $ Ch_Focus.Statup("Obed", 90, 2)
                    if Approval < 2:
                            $ Ch_Focus.FaceChange("sad")
                            $ Ch_Focus.Statup("Love", 80, -2)
                            ch_j "Ну и ладно!"
                            ch_j ". . ."
                            $ Ch_Focus.FaceChange("normal")
                    #returns to previous menu.
                    return
    return

label Jean_PJ_Prep:
    if JeanX.Taboo:
        $ JeanX.Statup("Inbt", 90, int(Taboo/10))
        $ JeanX.Statup("Lust", 50, int(Taboo/5))

    $ JeanX.FaceChange("sexy")
    if JeanX.Forced:
        $ JeanX.FaceChange("sad")

    call Seen_First_Peen(JeanX,Partner,React=Situation)
    call Jean_PJ_Launch

    if Situation == JeanX:
            #Jean auto-starts
            $ Situation = 0
            if Trigger2 == "jackin":
                "Невидимая сила откидывает ваши руку в сторону и начинает ласкать ваш член."
            elif Trigger2 == "jilling":
                "Невидимая сила откидывает ваши руку в сторону и начинает ласкать вашу киску."
            else:
                if not Player.Male:
                    "[JeanX.Name] дарит вам озорную улыбку, и нежное \"нечто\" начинает ласкать вашу киску."
                else:
                    "[JeanX.Name] дарит вам озорную улыбку, и нежное \"нечто\" начинает ласкать ваш член."
            menu:
                "Что будете делать?"
                "Ничего не делать.":
                    $ JeanX.Statup("Inbt", 70, 3)
                    $ JeanX.Statup("Inbt", 30, 2)
                    "[JeanX.Name] продолжает свои действия."
                "Похвалить ее.":
                    $ JeanX.FaceChange("sexy", 1)
                    $ JeanX.Statup("Inbt", 70, 3)
                    ch_p "Ооох, как хорошо, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] продолжает свои действия."
                    $ JeanX.Statup("Love", 80, 1)
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    $ JeanX.FaceChange("surprised")
                    $ JeanX.Statup("Inbt", 70, 1)
                    ch_p "Давай сейчас не будем, [JeanX.Pet]."
                    $ JeanX.NameCheck() #checks reaction to petname
                    "[JeanX.Name] отстраняется."
                    $ JeanX.Statup("Obed", 90, 1)
                    $ JeanX.Statup("Obed", 50, 1)
                    $ JeanX.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ JeanX.AddWord(1,"refused","refused")
                    return

    if "psysex" not in JeanX.History:
        if JeanX.Forced:
            $ JeanX.Statup("Love", 90, -10)
            $ JeanX.Statup("Obed", 70, 15)
            $ JeanX.Statup("Inbt", 80, 20)
        else:
            $ JeanX.Statup("Love", 90, 5)
            $ JeanX.Statup("Obed", 70, 15)
            $ JeanX.Statup("Inbt", 80, 15)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ JeanX.RecentActions.append("psysex")
    $ JeanX.DailyActions.append("psysex")

label Jean_PJ_Cycle:
    $ Trigger = "psy"
    while Round > 0:
        call Shift_Focus(JeanX)
        call Jean_PJ_Launch
        $ JeanX.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . ." if Speed:
                                    pass

                        "Начать? . ." if not Speed:
                                    $ Speed = 1

                        "Быстрее. . ." if Speed < 2:
                                    $ Speed = 2
                                    "Вы просите ее немного ускориться."
                        "Быстрее. . . (locked)" if Speed >= 2:
                                    pass

                        "Помедленнее. . ." if Speed:
                                    $ Speed -= 1
                                    "Вы просите ее немного сбавить темп."
                        "Помедленнее. . . (locked)" if not Speed:
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(JeanX)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Jean_PJ_Cycle

                        "Концентрироваться на продолжительности [[не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                        "Сменить вид":
                                    call ViewShift(JeanX,"menu")
                                    jump Jean_PJ_Cycle
                        "Изменить структуру силы":
                                    menu:
                                        "Что вы хотите ощущать?"
                                        "Руку":
                                            if ApprovalCheck(JeanX, 1000):
                                                    $ Psychic = "hand"
                                            else:
                                                    ch_j "Я бы предпочла этого не делать."
                                        "Рот":
                                            if ApprovalCheck(JeanX, 1100):
                                                    $ Psychic = "mouth"
                                            else:
                                                    ch_j "Не-а."
                                        "Грудь" if Player.Male:
                                            if ApprovalCheck(JeanX, 1000):
                                                    $ Psychic = "tits"
                                            else:
                                                    ch_j "Я бы предпочла этого не делать."
                                        "Киску":
                                            if ApprovalCheck(JeanX, 1200):
                                                    $ Psychic = "pussy"
                                            else:
                                                    ch_j "Эм. . . нет."
                                        "Попку" if Player.Male:
                                            if ApprovalCheck(JeanX, 1300):
                                                    $ Psychic = "anal"
                                            else:
                                                    ch_j "Ну да, тебе бы этого хотелось."
                        "Другие варианты":
                                menu:
                                    "Начать также ласкать ее грудь." if Trigger2 != "fondle breasts":
                                            if JeanX.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "Вы начинаете ласкать ее грудь."
                                                $ JeanX.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(JeanX,"tired")

                                    "Сменить основное действие (locked)":
                                            pass

                                    "Тройничек (locked)" if not Partner:
                                        pass
                                    "Тройничек" if Partner:
                                        menu:
                                            "Пусть [JeanX.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе" if Trigger == "lesbian":
                                                        call Les_Change(JeanX)
                                            "Пусть [JeanX.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Пусть [Partner.Name] займется чем-нибудь другим":
                                                        call Three_Change(JeanX)

                                            "Не бросай свое текущее занятие. . . (locked)" if not ThreeCount or not Partner.Offhand:
                                                        $ ThreeCount = 0
                                            "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        $ ThreeCount = 0

                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(JeanX)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Jean_PJ_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Jean_PJ_Cycle
                                            "Неважно":
                                                        jump Jean_PJ_Cycle
                                    "Раздеть [JeanX.Name_tvo]":
                                            call Girl_Undress(JeanX)
                                    "Привести в порядок [JeanX.Name_tvo] (locked)" if not JeanX.Spunk:
                                            pass
                                    "Привести в порядок [JeanX.Name_tvo]" if JeanX.Spunk:
                                            call Girl_Cleanup(JeanX,"ask")
                                    "Неважно":
                                            jump Jean_PJ_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Jean_PJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Jean_PJ_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Jean_PJ_Reset
                                    $ Line = 0
                                    jump Jean_PJ_After
        #End menu (if Line)

        call Shift_Focus(JeanX)
        call Sex_Dialog(JeanX,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or JeanX.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(JeanX)
                            if "angry" in JeanX.RecentActions:
                                call Jean_PJ_Reset
                                return
                            $ JeanX.Statup("Lust", 200, 5)
                            if 100 > JeanX.Lust >= 70 and JeanX.OCount < 2 and JeanX.SEXP >= 20:
                                $ JeanX.RecentActions.append("unsatisfied")
                                $ JeanX.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jean_PJ_After
                            $ Line = "came"

                    if JeanX.Lust >= 100:
                            #If Jean can cum
                            call Girl_Cumming(JeanX)
                            if Situation == "shift" or "angry" in JeanX.RecentActions:
                                jump Jean_PJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "Вы истощены, вам, наверное, пора взять перерыв."


                            if "unsatisfied" in JeanX.RecentActions:#And Jean is unsatisfied,
                                "[JeanX.Name] все еще выглядит слегка неудовлетворенной."
                                menu:
                                    "Хотите завершить начатое?"
                                    "Продолжим еще немного.":
                                        $ Line = "Вы возвращаетесь к процессу"
                                    "С меня хватит.":
                                        "Вы заканчиваете веселье."
                                        jump Jean_PJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ JeanX.Brows = "angry"
                    menu:
                        ch_j "Ладно, мне стало скучно. Мы можем заняться чем-нибудь другим?"
#                        "Как насчет отсоса?" if JeanX.Action and MultiAction:
#                                $ Situation = "shift"
#                                call Jean_PJ_After
#                                call Jean_Blowjob
                        "Закончить." if Player.FocusX:
                                "Вы расслабляетесь. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Jean_PJ_Cycle
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                call Jean_PJ_Reset
                                $ Situation = "shift"
                                jump Jean_PJ_After
                        "Нет, давай за работу.":
                                if ApprovalCheck(JeanX, 1200) or ApprovalCheck(JeanX, 500, "O"):
                                    $ JeanX.Statup("Love", 200, -5)
                                    $ JeanX.Statup("Obed", 50, 3)
                                    $ JeanX.Statup("Obed", 80, 2)
                                    "Она ворчит, но возвращается к работе."
                                else:
                                    $ JeanX.FaceChange("angry", 1)
                                    "Она сердито смотрит на вас, отпускает ваш член и отстраняется."
                                    ch_j "У меня есть дела поважнее."
                                    $ JeanX.Statup("Love", 50, -3, 1)
                                    $ JeanX.Statup("Love", 80, -4, 1)
                                    $ JeanX.Statup("Obed", 30, -1, 1)
                                    $ JeanX.Statup("Obed", 50, -1, 1)
                                    $ JeanX.RecentActions.append("angry")
                                    $ JeanX.DailyActions.append("angry")
                                    jump Jean_PJ_After
        elif Cnt == 10 and JeanX.SEXP <= 100 and not ApprovalCheck(JeanX, 1200, "LO"):
                    $ JeanX.Brows = "confused"
                    ch_j "Приятно, да?"
        #End Count check

        call Escalation(JeanX) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(JeanX,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(JeanX,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ JeanX.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(JeanX,"done")   #"Ok, [Ch_Focus.Petname], that's enough of that for now."

label Jean_PJ_After:
    $ JeanX.FaceChange("sexy")

    $ JeanX.Action -=1

    $ JeanX.Statup("Lust", 90, 5)

    call Partner_Like(JeanX,1)

    if "psysex" not in JeanX.History:
            ch_j "Довольно неплохо, да?"
    $ JeanX.AddWord(1,0,0,0,"psysex")

    $ Tempmod = 0
    if Situation == "shift":
        ch_j "Хорошо, так что ты предлагаешь?"
    call Jean_PJ_Reset
    call Checkout
    return

## end JeanX.Psychic Handjob //////////////////////////////////////////////////////////////////////
