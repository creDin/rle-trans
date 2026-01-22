## Ch_Focus.Finger //////////////////////////////////////////////////////////////////////
label Girl_Finger: #rkeljsvgbdw

        $ Round -= 5 if Round > 5 else (Round-1)
#        call Shift_Focus(Girl)
        if Ch_Focus.Finger >= 7: # She loves it
            $ Tempmod += 10
        elif Ch_Focus.Finger >= 3: #You've done it before several times
            $ Tempmod += 7
        elif Ch_Focus.Finger: #You've done it before
            $ Tempmod += 3
        elif Ch_Focus is DoreenX:
            $ Tempmod -= 2
        elif Ch_Focus is WandaX:
            $ Tempmod += 5

        if Ch_Focus.Addict >= 75 and Ch_Focus.Swallow >=3: #She's really strung out and has swallowed
            $ Tempmod += 15
        if Ch_Focus.Addict >= 75:
            $ Tempmod += 5

        if Situation == "shift":
            $ Tempmod += 15
        if "exhibitionist" in Ch_Focus.Traits:
            $ Tempmod += (3*Taboo)
        if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
            $ Tempmod += 10
        elif "ex" in Ch_Focus.Traits:
            $ Tempmod -= 40
        if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
            $ Tempmod -= 5 * Ch_Focus.ForcedCount

        if Taboo and "tabno" in Ch_Focus.DailyActions:
            $ Tempmod -= 10

        if "no finger" in Ch_Focus.DailyActions:
            $ Tempmod -= 5
            $ Tempmod -= 10 if "no finger" in Ch_Focus.RecentActions else 0

        $ Approval = ApprovalCheck(Ch_Focus, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

        if not Ch_Focus.Finger and "no finger" not in Ch_Focus.RecentActions:
                #first time you ask
                $ Ch_Focus.FaceChange("surprised", 1)
                if Ch_Focus is RogueX:
                        ch_r "Ты. . . хочешь, чтобы я поласкала тебя пальцами?"
                elif Ch_Focus is KittyX:
                        ch_k "Ох, эм. . . ты хочешь, чтобы я поласкала тебя пальцами?"
                elif Ch_Focus is EmmaX:
                        ch_e "Ох, поласкать тебя пальцами?"
                elif Ch_Focus is LauraX:
                        ch_l "Эм, поласкать тебя пальцами?"
                elif Ch_Focus is JeanX:
                        ch_j "Ох, ты хочешь, чтобы я поласкала тебя пальцами?"
                elif Ch_Focus is StormX:
                        ch_s "Ты желаешь, чтобы я поласкала тебя пальцами?"
                elif Ch_Focus is JubesX:
                        ch_v "Поласкать тебя пальцами?"
                elif Ch_Focus is GwenX:
                        ch_g "Ох, ты хочешь, чтобы я поласкала тебя пальцами. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Ох, ты хочешь, чтобы я поласкала тебя пальцами. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Ты, эм, хочешь, чтобы я поласкала тебя пальцами? . ."
                elif Ch_Focus is WandaX:
                        ch_w "Ты хочешь, чтобы я трахнула тебя пальцами?"

        call expression Ch_Focus.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
        if "nogirls" in Ch_Focus.History and not Ch_Focus.Forced:
                #if she isn't into girls but isn't coerced. . .
                return

        if not Ch_Focus.Finger and Approval:
                #First time dialog if she agrees
                if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -3, 1)
                    $ Ch_Focus.Statup("Love", 20, -2, 1)
                elif Ch_Focus.Love >= (Ch_Focus.Obed + Ch_Focus.Inbt):
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Brows = "sad"
                    $ Ch_Focus.Mouth = "smile"
                elif Ch_Focus.Obed >= Ch_Focus.Inbt:
                    $ Ch_Focus.FaceChange("normal")
                elif Ch_Focus.Addict >= 50:
                    $ Ch_Focus.FaceChange("manic", 1)
                else: # Uninhibited
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Mouth = "smile"
                if Ch_Focus is RogueX:
                        ch_r "Ну, можно и так. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Я этим не. . . эм. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Полагаю, в классике есть своя прелесть. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Давненько я этим не занималась. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Это может быть интересно."
                elif Ch_Focus is StormX:
                        ch_s "Пожалуй, это могло бы быть хорошим началом. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Нууу, это может быть интересно. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Хмм, мне не противна эта идея. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Что ж, это я могу. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Наверное, можно. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Это может быть весело. . ."

        elif Approval:
                #Second time+ dialog if she agrees
                if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -3, 1)
                    $ Ch_Focus.Statup("Love", 20, -2, 1)
                    if Ch_Focus is RogueX:
                            ch_r "И все? . ."
                    elif Ch_Focus is KittyX:
                            ch_k "И ничего. . . более. . ?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Немного скучновато. . ."
                    elif Ch_Focus is LauraX:
                            ch_l ". . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Фи."
                    elif Ch_Focus is StormX:
                            ch_s "Я думала, ты захочешь большего. . ."
                    elif Ch_Focus is JubesX:
                            ch_v ". . . И все?"
                    elif Ch_Focus is GwenX:
                            ch_g "И ничего более. . ?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Это все, что тебе нужно?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Это все, чего ты хочешь? . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Это все?"
                elif "finger" in Ch_Focus.RecentActions:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    jump Girl_Finger_Prep
                else:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.ArmPose = 2
                    $ Line = renpy.random.choice(["Хочешь немного разогреться?",
                        "Ты хочешь, чтобы я поласкала тебя пальцами?",
                        "Немного. . . [шевелит двумя пальцами]?",
                        "Хочешь, чтобы я немного разогрела тебя?",
                        "Тебе нужно немного смазки?"])
                    call AnyLine(Ch_Focus,Line)
                $ Line = 0

        if Approval >= 2:
                #She's into it. . .
                if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 1)
                    if Ch_Focus is RogueX:
                            ch_r "Ладно."
                    elif Ch_Focus is KittyX:
                            ch_k "Ох, как хочешь."
                    elif Ch_Focus is EmmaX:
                            ch_e "Почему бы и нет. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Как хочешь."
                    elif Ch_Focus is JeanX:
                            ch_j "Конечно."
                    elif Ch_Focus is StormX:
                            ch_s "Приемлемо."
                    elif Ch_Focus is JubesX:
                            ch_v "Как хочешь."
                    elif Ch_Focus is GwenX:
                            ch_g "Конечно. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Ну хорошо."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ох, ладно. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Конечно."
                else:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Love", 90, 1)
                    $ Ch_Focus.Statup("Inbt", 50, 3)
                    $ Line = renpy.random.choice(["Конечно.",
                        "Хорошо.",
                        "Ладно.",
                        "Ладно, иди ко мне.",
                        "Хорошо. . . [Жестом подзывает вас к себе].",
                        ". . . ok."])
                    call AnyLine(Ch_Focus,Line)
                    $ Line = 0
                $ Ch_Focus.Statup("Obed", 20, 1)
                $ Ch_Focus.Statup("Obed", 60, 1)
                $ Ch_Focus.Statup("Inbt", 70, 2)
                jump Girl_Finger_Prep

        else:
            #She's not into it, but maybe. . .
            $ Ch_Focus.FaceChange("angry")
            if "no finger" in Ch_Focus.DailyActions:
                call AnyLine(Ch_Focus,"Я уже сказала тебе \"нет,\" "+Ch_Focus.Petname+".")
            elif Taboo and "tabno" in Ch_Focus.DailyActions:
                call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
            else:
                $ Ch_Focus.FaceChange("bemused")
                if Ch_Focus is RogueX:
                        ch_r "Может не сейчас? . ."
                elif Ch_Focus is KittyX:
                        ch_k "Я не уверена. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Я так не думаю. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Нет."
                elif Ch_Focus is JeanX:
                        ch_j "Не-а."
                elif Ch_Focus is StormX:
                        ch_s "Я так не думаю. . ."
                elif Ch_Focus is JubesX:
                        ch_v ". . . нет?"
                elif Ch_Focus is GwenX:
                        ch_g "Но. . . нет, спасибо. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Что ж, возможно, но не сейчас. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я, эм, не уверена. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Я не уверена, подходящее ли сейчас время и место. . ."
            menu:
                extend ""
                "Извини, забудь." if "no finger" in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("bemused")
                    if Ch_Focus is RogueX:
                            ch_r "Ладно."
                    elif Ch_Focus is KittyX:
                            ch_k ". . ."
                            ch_k "Все нормально."
                    elif Ch_Focus is EmmaX:
                            ch_e ". . ."
                            $ Ch_Focus.FaceChange("sexy")
                            ch_e "Не беспокойся об этом. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Лан."
                    elif Ch_Focus is JeanX:
                            ch_j "Угу."
                    elif Ch_Focus is StormX:
                            ch_s "Не беспокойся. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Ага."
                    elif Ch_Focus is GwenX:
                            ch_g "Ага, все нормально. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Ох, конечно?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Спасибо. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Без проблем."
                    return
                "Может, в другой раз?" if "no finger" not in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("bemused")
                    if Ch_Focus is RogueX:
                            ch_r "Я подумаю, [RogueX.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k ". . ."
                            ch_k "Может быть."
                    elif Ch_Focus is EmmaX:
                            ch_e ". . ."
                            $ Ch_Focus.FaceChange("sexy")
                            ch_e "Этого нельзя исключать. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Может быть."
                    elif Ch_Focus is JeanX:
                            ch_j "Возможно."
                    elif Ch_Focus is StormX:
                            ch_s ". . ."
                            ch_s "Возможно. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Может быть."
                    elif Ch_Focus is GwenX:
                            ch_g "Ага, может быть. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Возможно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d ". . . может быть? . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Может быть."
                    $ Ch_Focus.Statup("Love", 80, 2)
                    $ Ch_Focus.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ Ch_Focus.RecentActions.append("tabno")
                        $ Ch_Focus.DailyActions.append("tabno")
                    $ Ch_Focus.RecentActions.append("no finger")
                    $ Ch_Focus.DailyActions.append("no finger")
                    return
                "Я была бы тебе очень признательна. . .":
                    if Approval:
                        $ Ch_Focus.FaceChange("sexy")
                        $ Ch_Focus.Statup("Obed", 90, 2)
                        $ Ch_Focus.Statup("Obed", 50, 2)
                        $ Ch_Focus.Statup("Inbt", 70, 3)
                        $ Ch_Focus.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Конечно, иди ко мне.",
                            "Ладно, не вопрос.",
                            "Конечно.",
                            "Пожалуй, тогда можно.",
                            "Ладно [Она жестом подзывает вас].",
                            "Хех, ладно."])
                        call AnyLine(Ch_Focus,Line)
                        $ Line = 0
                        jump Girl_Finger_Prep
                    else:
                        pass

                "Давай, приступай.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(Ch_Focus, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and Ch_Focus.Forced):
                        $ Ch_Focus.FaceChange("sad")
                        $ Ch_Focus.Statup("Love", 70, -5, 1)
                        $ Ch_Focus.Statup("Love", 200, -2)
                        if Ch_Focus is RogueX:
                                ch_r "Ох, ладно, давай ее сюда."
                        elif Ch_Focus is KittyX:
                                ch_k "Ладно."
                        elif Ch_Focus is EmmaX:
                                ch_e "Хм. Хорошо, но не искушай судьбу, [EmmaX.Petname]."
                        elif Ch_Focus is LauraX:
                                ch_l "Ладно, хорошо."
                        elif Ch_Focus is JeanX:
                                ch_j ". . . Ладно, как скажешь."
                        elif Ch_Focus is StormX:
                                ch_s ". . . Хорошо."
                        elif Ch_Focus is JubesX:
                                ch_v "Ладно, как скажешь."
                        elif Ch_Focus is GwenX:
                                ch_g ". . . Как скажешь."
                        elif Ch_Focus is BetsyX:
                                ch_b "Ох, хорошо."
                        elif Ch_Focus is DoreenX:
                                ch_d "Ох, ладно. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Конечно."
                        $ Ch_Focus.Statup("Obed", 50, 4)
                        $ Ch_Focus.Statup("Inbt", 80, 1)
                        $ Ch_Focus.Statup("Inbt", 60, 3)
                        $ Ch_Focus.Forced = 1
                        jump Girl_Finger_Prep
                    else:
                        $ Ch_Focus.Statup("Love", 200, -15)
                        $ Ch_Focus.RecentActions.append("angry")
                        $ Ch_Focus.DailyActions.append("angry")


        #She refused all offers.
        $ Ch_Focus.ArmPose = 1
        if "no finger" in Ch_Focus.DailyActions:
            $ Ch_Focus.FaceChange("angry", 1)
            if Ch_Focus is RogueX:
                    ch_r "Я просто не хочу этого делать, [Ch_Focus.Petname]."
            elif Ch_Focus is KittyX:
                    ch_k "Я не буду повторять."
            elif Ch_Focus is EmmaX:
                    ch_e "Не заставляй меня повторяться."
            elif Ch_Focus is LauraX:
                    ch_l "Не спрашивай больше."
            elif Ch_Focus is JeanX:
                    ch_j "Не спрашивай больше."
            elif Ch_Focus is StormX:
                    ch_s "Не заставляй меня повторяться."
            elif Ch_Focus is JubesX:
                    ch_v "Боже, перестань спрашивать!"
            elif Ch_Focus is GwenX:
                    ch_g "Слушай, разве ты не можешь сделать все сама?"
            elif Ch_Focus is BetsyX:
                    ch_b "Пожалуйста, перестань приставать ко мне."
            elif Ch_Focus is DoreenX:
                    ch_d "Прекрати. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Успокойся."
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
                    ch_k "Да что я вообще оправдываюсь, ты все прекрасно поняла!"
            elif Ch_Focus is EmmaX:
                    ch_e "Ты хочешь слишком многого."
            elif Ch_Focus is LauraX:
                    ch_l "Нет."
            elif Ch_Focus is JeanX:
                    ch_j "Нет."
            elif Ch_Focus is StormX:
                    ch_s "Меня это не устраивает."
            elif Ch_Focus is JubesX:
                    ch_v "Не-а."
            elif Ch_Focus is GwenX:
                    ch_g "Извини. . ."
            elif Ch_Focus is BetsyX:
                    ch_b ". . . нет."
            elif Ch_Focus is DoreenX:
                    ch_d "Я- я не могу сделать что-то подобно!"
            elif Ch_Focus is WandaX:
                    ch_w "Меня это не интересует."
            $ Ch_Focus.Statup("Lust", 200, 5)
            if Ch_Focus.Love > 300:
                    $ Ch_Focus.Statup("Love", 70, -2)
            $ Ch_Focus.Statup("Obed", 50, -2)
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
        elif Taboo:                             # she refuses and this is too public a place for her
            $ Ch_Focus.FaceChange("angry", 1)
            $ Ch_Focus.DailyActions.append("tabno")
            call Sex_Basic_Dialog(Ch_Focus,"tabno")
            $ Ch_Focus.Statup("Lust", 200, 5)
            $ Ch_Focus.Statup("Obed", 50, -3)
        elif Ch_Focus.Finger:
            $ Ch_Focus.FaceChange("sad")
            if Ch_Focus is RogueX:
                    ch_r "Думаю, на этот раз ты должна справиться сама. . ."
            elif Ch_Focus is KittyX:
                    ch_k "Я не в настроение сегодня. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Я бы не хотела подобного. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Мне сегодня как-то не хочется. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Мне сегодня не хочется. . ."
            elif Ch_Focus is StormX:
                    ch_s ". . . Я бы предпочла этого не делать."
            elif Ch_Focus is JubesX:
                    ch_v "Не сейчас. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Эм, не сегодня. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Уверена, ты сможешь справиться и без меня."
            elif Ch_Focus is DoreenX:
                    ch_d "Ты можешь и сама справиться. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Ты и сама справишься."
        else:
            $ Ch_Focus.FaceChange("normal", 1)
            if Ch_Focus is RogueX:
                    ch_r "Я бы этого не хотела."
            elif Ch_Focus is KittyX:
                    ch_k "Я не хочу прикасаться к ней."
            elif Ch_Focus is EmmaX:
                    ch_e "Нет, я так не думаю, [EmmaX.Petname]."
            elif Ch_Focus is LauraX:
                    ch_l "Я бы предпочла не прикасаться к ней."
            elif Ch_Focus is JeanX:
                    ch_j "Я бы предпочла не трогать ее."
            elif Ch_Focus is StormX:
                    ch_s "Нет, я так не думаю, [StormX.Petname]."
            elif Ch_Focus is JubesX:
                    ch_v "Я не в настроении."
            elif Ch_Focus is GwenX:
                    ch_g "Эм, нет, спасибо."
            elif Ch_Focus is BetsyX:
                    ch_b "Я бы. . . предпочла этим не заниматься."
            elif Ch_Focus is DoreenX:
                    ch_d "Мне. . . не хочется. . . извини."
            elif Ch_Focus is WandaX:
                    ch_w "Нет, может, в другой раз."
        $ Ch_Focus.RecentActions.append("no finger")
        $ Ch_Focus.DailyActions.append("no finger")
        $ Tempmod = 0
        return


label Girl_Finger_Prep: #rkeljsvgb
#        call Shift_Focus(Girl)
        if Trigger2 == "finger":
            return

        if Taboo:
            $ Ch_Focus.Inbt += int(Taboo/10)
            $ Ch_Focus.Lust += int(Taboo/5)

        $ Ch_Focus.FaceChange("sexy")
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
        elif not Ch_Focus.Finger:
            if Ch_Focus in (RogueX,KittyX):
                    $ Ch_Focus.FaceChange("perplexed",2)

        call Seen_First_Peen(Ch_Focus,Partner,React=Situation)
        call expression Ch_Focus.Tag + "_Finger_Launch" pass ("L")

        if Situation == Ch_Focus:
                #Girl auto-starts
                $ Situation = 0
                if Trigger2 == "jilling":
                    "[Ch_Focus.Name] откидывает ваши руку в сторону и начинает ласкать вашу киску."
                else:
                    "[Ch_Focus.Name] одаривает вас хитрой улыбкой и начинает ласкать вашу киску."
                menu:
                    "Что будете делать?"
                    "Ничего не делать.":
                        $ Ch_Focus.Statup("Inbt", 70, 3)
                        $ Ch_Focus.Statup("Inbt", 30, 2)
                        "[Ch_Focus.Name] продолжает свои действия."
                    "Похвалить ее.":
                        $ Ch_Focus.FaceChange("sexy", 1)
                        $ Ch_Focus.Statup("Inbt", 70, 3)
                        ch_p "Ооох, как хорошо, [Ch_Focus.Pet]."
                        $ Ch_Focus.NameCheck() #checks reaction to petname
                        "[Ch_Focus.Name] продолжает свои действия."
                        $ Ch_Focus.Statup("Love", 80, 1)
                        $ Ch_Focus.Statup("Obed", 90, 1)
                        $ Ch_Focus.Statup("Obed", 50, 2)
                    "Сказать ей остановиться.":
                        $ Ch_Focus.FaceChange("surprised")
                        $ Ch_Focus.Statup("Inbt", 70, 1)
                        ch_p "Давай сейчас не будем, [Ch_Focus.Pet]."
                        $ Ch_Focus.NameCheck() #checks reaction to petname
                        "[Ch_Focus.Name] отстраняется."
                        $ Ch_Focus.Statup("Obed", 90, 1)
                        $ Ch_Focus.Statup("Obed", 50, 1)
                        $ Ch_Focus.Statup("Obed", 30, 2)
                        $ Player.RecentActions.append("nope")
                        $ Ch_Focus.AddWord(1,"refused","refused")
                        return

        if not Ch_Focus.Finger:
            if Ch_Focus.Forced:
                $ Ch_Focus.Statup("Love", 90, -20)
                $ Ch_Focus.Statup("Obed", 70, 25)
                $ Ch_Focus.Statup("Inbt", 80, 30)
            else:
                $ Ch_Focus.Statup("Love", 90, 5)
                $ Ch_Focus.Statup("Obed", 70, 20)
                $ Ch_Focus.Statup("Inbt", 80, 20)

        if Situation:
#            $ renpy.pop_call()
            $ Situation = 0
        $ Line = 0
        $ Cnt = 0
        if Taboo:
            $ Ch_Focus.DrainWord("tabno")
        $ Ch_Focus.DrainWord("no finger")
        $ Ch_Focus.RecentActions.append("finger")
        $ Ch_Focus.DailyActions.append("finger")

label Girl_Finger_Cycle: #rkeljsvgb
        while Round > 0:
#            call Shift_Focus(Girl)
            call expression Ch_Focus.Tag + "_Finger_Launch"
            $ Ch_Focus.LustFace()

            if  Player.Focus < 100:
                        #Player Command menu
                        menu:
                            "Продолжать. . ." if Speed:
                                        pass

                            "Начать? . ." if not Speed:
                                        $ Speed = 1

                            "Быстрее. . ." if Speed < 2:
                                        $ Speed = 2
                                        "Вы просите ее немного набрать темп."
                            "Быстрее. . . (locked)" if Speed >= 2:
                                        pass

                            "Помедленнее. . ." if Speed:
                                        $ Speed -= 1
                                        "Вы просите ее немного набрать темп."
                            "Помедленнее. . . (locked)" if not Speed:
                                        pass
                            "Концентрироваться на продолжительности [[Не открыто] (locked)" if "focus" not in Player.Traits:
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
                                                            "Может, вылижешь мою киску?":
                                                                        if Ch_Focus.Action and MultiAction:
                                                                            $ Situation = "shift"
                                                                            call Girl_Finger_After
                                                                            call Girl_CUN
                                                                        else:
                                                                            call Sex_Basic_Dialog(Ch_Focus,"tired")

    #                                                        "How about a titjob?":
    #                                                                    if Ch_Focus.Action and MultiAction:
    #                                                                        $ Situation = "shift"
    #                                                                        call Girl_Finger_After
    #                                                                        call Girl_Titjob
    #                                                                    else:
    #                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                            "Неважно":
                                                                    jump Girl_Finger_Cycle
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
                                                            jump Girl_Finger_Cycle
                                                "Привести в порядок [Partner.Name_vin] (locked)" if not Partner.Spunk:
                                                            pass
                                                "Привести в порядок [Partner.Name_vin]" if Partner.Spunk:
                                                            call Girl_Cleanup(Partner,"ask")
                                                            jump Girl_Finger_Cycle
                                                "Неважно":
                                                            jump Girl_Finger_Cycle
                                        "Раздеть [Ch_Focus.Name_vin]":
                                                call Girl_Undress(Ch_Focus)
                                        "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                                pass
                                        "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                                call Girl_Cleanup(Ch_Focus,"ask")
                                        "Неважно":
                                                jump Girl_Finger_Cycle

                            "Вернуться к Секс-меню" if MultiAction:
                                        ch_p "Нам стоит попробовать что-нибудь другое."
                                        call expression Ch_Focus.Tag + "_Finger_Reset"
                                        $ Situation = "shift"
                                        $ Line = 0
                                        jump Girl_Finger_After
                            "Закончить" if not MultiAction:
                                        ch_p "Нам стоит пока закончить."
                                        call expression Ch_Focus.Tag + "_Finger_Reset"
                                        $ Line = 0
                                        jump Girl_Finger_After
            #End menu (if Line)

#            call Shift_Focus(Girl)
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
                                    call expression Ch_Focus.Tag + "_Finger_Reset"
                                    return
                                $ Ch_Focus.Statup("Lust", 200, 5)
                                if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2 and Ch_Focus.SEXP >= 20:
                                    $ Ch_Focus.RecentActions.append("unsatisfied")
                                    $ Ch_Focus.DailyActions.append("unsatisfied")

                                if Player.Focus > 80:
                                    jump Girl_Finger_After
                                $ Line = "came"

                        if Ch_Focus.Lust >= 100:
                                #If Girl can cum
                                call Girl_Cumming(Ch_Focus)
                                if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                    jump Girl_Finger_After

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
                                            jump Girl_Finger_After
            if Partner and Partner.Lust >= 100:
                    #Checks if partner could orgasm
                    call Girl_Cumming(Partner)
            #End orgasm

            $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

            if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
                pass
            elif Cnt == (5 + Ch_Focus.Finger):
                        $ Ch_Focus.Brows = "confused"
                        call AnyLine(Ch_Focus,"Ты уже скоро?")
            elif Cnt == (10 + Ch_Focus.Finger):
                        $ Ch_Focus.Brows = "angry"
                        call AnyLine(Ch_Focus,"Может, мы можем заняться чем-нибудь другим?")
                        menu:
                            extend ""
                            "Как насчет вылизать мою киску?" if Ch_Focus.Action and MultiAction:
                                    $ Situation = "shift"
                                    call Girl_Finger_After
                                    call Girl_CUN
                            "Закончить." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                                    $ Player.Focus += 15
                                    jump Girl_Finger_Cycle
                            "Давай попробуем что-нибудь другое." if MultiAction:
                                    $ Line = 0
                                    call expression Ch_Focus.Tag + "_Finger_Reset"
                                    $ Situation = "shift"
                                    jump Girl_Finger_After
                            "Нет, давай за работу.":
                                    if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                        $ Ch_Focus.Statup("Love", 200, -5)
                                        $ Ch_Focus.Statup("Obed", 50, 3)
                                        $ Ch_Focus.Statup("Obed", 80, 2)
                                        "Она ворчит, но возвращается к работе."
                                    else:
                                        $ Ch_Focus.FaceChange("angry", 1)
                                        "Она кидает на вас сердитый взгляд и отстраняется."
                                        call AnyLine(Ch_Focus,"Я так не думаю.")
                                        $ Ch_Focus.Statup("Love", 50, -3, 1)
                                        $ Ch_Focus.Statup("Love", 80, -4, 1)
                                        $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                        $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                        $ Ch_Focus.RecentActions.append("angry")
                                        $ Ch_Focus.DailyActions.append("angry")
                                        jump Girl_Finger_After
            #End Count check

            call Escalation(Ch_Focus) #sees if she wants to escalate things

            if Round == 10:
                    call Sex_Basic_Dialog(Ch_Focus,10) #"It is getting late, [Ch_Focus.Petname]. . ."
            elif Round == 5:
                    call Sex_Basic_Dialog(Ch_Focus,5)   #"We should take a break soon."

        #Round = 0 loop breaks
        $ Ch_Focus.FaceChange("bemused", 0)
        $ Line = 0
        call Sex_Basic_Dialog(Ch_Focus,"done") # ch_s "I need to take a moment to collect myself."


label Girl_Finger_After: #rkeljsvgb
        $ Ch_Focus.FaceChange("sexy")

        $ Ch_Focus.Finger += 1
        $ Ch_Focus.Action -=1
        $ Ch_Focus.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ Ch_Focus.Addictionrate += 1
        $ Ch_Focus.Statup("Lust", 90, 5)

        call Partner_Like(Ch_Focus,2)

        if Ch_Focus.Tag + " Magic Fingers" in Achievements:
                pass
        elif Ch_Focus.Finger >= 10:
                    $ Ch_Focus.FaceChange("smile", 1)
                    if Ch_Focus is RogueX:
                            ch_r "Должно быть, у меня \"волшебные пальчики.\""
                    elif Ch_Focus is KittyX:
                            ch_k "Мне кажется, я теперь[KittyX.like]мастер или типа того."
                    elif Ch_Focus is EmmaX:
                            ch_e "Я всегда говорила, что данное действие требует деликатного подхода. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Мне кажется, я стала гораздо опытнее, [Ch_Focus.Petname]."
                    elif Ch_Focus is JeanX:
                            ch_j "Похоже, в последнее время мы только этим и занимаемся. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Кажется, я стала \"королевой\"."
                    elif Ch_Focus is JubesX:
                            ch_v "Ого, я так много мастурбировала киски. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Я практиковалась дома. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Похоже, у меня к этому талант."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я думаю, тебе очень нравятся мои пальчики. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "В этом определенно есть некая \"магия\"."
                    $ Achievements.append(Ch_Focus.Tag + " Magic Fingers")
                    $Ch_Focus.SEXP += 5
        elif Ch_Focus.Finger == 1:
                $Ch_Focus.SEXP += 10
                if Ch_Focus.Love >= 500:
                    $ Ch_Focus.Mouth = "smile"
                    if Ch_Focus is RogueX:
                            ch_r "Ну, очень приятно иметь кого-то, кого можно. . . всегда потрогать."
                    elif Ch_Focus is KittyX:
                            ch_k "Ты такая теплая на ощупь. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "У тебя очень соблазнительная киска, [Ch_Focus.Petname]. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Это было отчасти. . . приятно. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Это было довольно весело. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Это было приятнее, чем я ожидала. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Это было. . . весело. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Ммм, это было довольно безумно. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Мне даже понравилось."
                    elif Ch_Focus is DoreenX:
                            ch_d "Это было. . . очень весело. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Это было клево, правда?"
                elif Player.Focus <= 20:
                    $ Ch_Focus.Mouth = "sad"
                    if Ch_Focus is RogueX:
                            ch_r "Ну, я надеюсь, что ты получила хоть какое-то удовольствие."
                    elif Ch_Focus is KittyX:
                            ch_k "Ты удовлетворена?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Ты удовлетворена?"
                    elif Ch_Focus is LauraX:
                            ch_l "Тебе хоть немного понравилось?"
                    elif Ch_Focus is JeanX:
                            ch_j "Очень приятно, да?"
                    elif Ch_Focus is StormX:
                            ch_s "Ты удовлетворен?"
                    elif Ch_Focus is JubesX:
                            ch_v "Твои потребности удовлетворены?"
                    elif Ch_Focus is GwenX:
                            ch_g "Ты довольна?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Полагаю, ты удовлетворена?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Это было достаточно хорошо. . . правда?"
                    elif Ch_Focus is WandaX:
                            ch_w "Уверена, что тебе понравилось."
        elif Ch_Focus.Finger == 5:
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
                            ch_g "Думаю, теперь я могу взяться за гитару."
                    elif Ch_Focus is BetsyX:
                            ch_b "Знаешь. . . я способна на большее."
                    elif Ch_Focus is DoreenX:
                            ch_d "Это было очень весело. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Ты постоянно возвращаешься за добавкой."
        $ Tempmod = 0
        if Situation == "shift":
            call Sex_Basic_Dialog(Ch_Focus,"shift") # "Mmm, so what else did you have in mind?"
        else:
            call expression Ch_Focus.Tag + "_Finger_Reset"
        call Checkout
        return

## end Ch_Focus.Finger //////////////////////////////////////////////////////////////////////


# Ch_Focus.CUN //////////////////////////////////////////////////////////////////////

label Girl_CUN: #rkeljsvg
#        if Ch_Focus is WandaX:       #fix, remove           fix, remove           fix, remove           fix, remove
#            "This is not implemented yet."
#            return              #fix, remove           fix, remove           fix, remove           fix, remove
        $ Round -= 5 if Round > 5 else (Round-1)
#        call Shift_Focus(Girl)
        if Ch_Focus.CUN >= 7: # She loves it
            $ Tempmod += 15
        elif Ch_Focus.CUN >= 3: #You've done it before several times
            $ Tempmod += 10
        elif Ch_Focus.CUN: #You've done it before
            $ Tempmod += 7
        elif Ch_Focus is DoreenX:
            $ Tempmod -= 5
        elif Ch_Focus is WandaX:
            $ Tempmod += 5

        if Ch_Focus.Addict >= 75 and Ch_Focus.Swallow >=3: #She's really strung out and has swallowed
            $ Tempmod += 25
        elif Ch_Focus.Addict >= 75: #She's really strung out
            $ Tempmod += 15

        if Situation == "shift":
            $ Tempmod += 15
        if "exhibitionist" in Ch_Focus.Traits:
            $ Tempmod += (4*Taboo)
        if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
            $ Tempmod += 10
        elif "ex" in Ch_Focus.Traits:
            $ Tempmod -= 40
        if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
            $ Tempmod -= 5 * Ch_Focus.ForcedCount

        if Taboo and "tabno" in Ch_Focus.DailyActions:
            $ Tempmod -= 10

        if "no cun" in Ch_Focus.DailyActions:
            $ Tempmod -= 5
            $ Tempmod -= 10 if "no cun" in Ch_Focus.RecentActions else 0

        $ Approval = ApprovalCheck(Ch_Focus, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

        if not Ch_Focus.CUN and "no cun" not in Ch_Focus.RecentActions:
            #first time question
            $ Ch_Focus.FaceChange("surprised", 1)
            $ Ch_Focus.Mouth = "kiss"
            if Ch_Focus is RogueX:
                    ch_r "Ты хочешь, чтобы я прижалась своим ртом к. . . твоей киске?"
            elif Ch_Focus is KittyX:
                    ch_k "Ты хочешь, чтобы я отлизала тебе?"
            elif Ch_Focus is EmmaX:
                    ch_e "Так, ты хочешь, чтобы я отлизала тебе?"
            elif Ch_Focus is LauraX:
                    ch_l "Ты хочешь, чтобы я отлизала тебе?"
            elif Ch_Focus is JeanX:
                    ch_j "Ох! Ты хочешь, чтобы я отлизала тебе?"
            elif Ch_Focus is StormX:
                    ch_s "Ты хочешь, чтобы я полизала твою розу?"
            elif Ch_Focus is JubesX:
                    $ JubesX.Blush = 2
                    $ JubesX.Mouth = "kiss"
                    ch_v "Ооо! Ты хочешь, чтобы я отлизала тебе?"
                    $ JubesX.Mouth = "smile"
                    ch_v "Уверена, что не боишься моих зубок?"
                    $ JubesX.Blush = 1
            elif Ch_Focus is GwenX:
                    ch_g "Ох. . . значит, желаешь отведать моего язычка. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Ты просишь меня спустится к твоей киске?"
            elif Ch_Focus is DoreenX:
                    ch_d "Ты хочешь, чтобы я лизнула там. . . ниже?"
            elif Ch_Focus is WandaX:
                    ch_w "Хочешь, чтобы я отлизала тебя?"
            if Ch_Focus.Finger:
                $ Ch_Focus.Mouth = "smile"
                if Ch_Focus is RogueX:
                        ch_r "Моих пальчиков уже мало?"
                elif Ch_Focus is KittyX:
                        ch_k "Тебя не удовлетворяют мои пальчики?"
                elif Ch_Focus is DoreenX:
                        ch_d "Я не могу просто. . . воспользоваться пальчиками или типа того?"

        call expression Ch_Focus.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
        if "nogirls" in Ch_Focus.History and not Ch_Focus.Forced:
                #if she isn't into girls but isn't coerced. . .
                return

        if not Ch_Focus.CUN and Approval:
            #First time dialog
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Love", 70, -3, 1)
                $ Ch_Focus.Statup("Love", 20, -2, 1)
            elif Ch_Focus.Love >= (Ch_Focus.Obed + Ch_Focus.Inbt):
                $ Ch_Focus.FaceChange("sexy")
                $ Ch_Focus.Brows = "sad"
                $ Ch_Focus.Mouth = "smile"
            elif Ch_Focus.Obed >= Ch_Focus.Inbt:
                $ Ch_Focus.FaceChange("normal")
            elif Ch_Focus.Addict >= 50:
                $ Ch_Focus.FaceChange("manic", 1)
            else:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Mouth = "smile"

            if Ch_Focus.Love >= 700:
                if Ch_Focus is RogueX:
                        ch_r "Я никогда раньше не пробовала другую девушку. . . это может быть интересно."
                elif Ch_Focus is KittyX:
                        ch_k "Мне даже немного интересно, какова ты. . . на вкус."
                elif Ch_Focus is EmmaX:
                        ch_e "Мне любопытно, так ли она хороша на вкус, как выглядит. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Мне интересно, какая ты на вкус."
                elif Ch_Focus is JeanX:
                        ch_j "Ну, я вряд ли смогу отказаться от подобного предложения. . ."
                elif Ch_Focus is StormX:
                        ch_s "Мне любопытно, какого это. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Я даже слегка с нетерпением ждала этого. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Мне интересно попробовать другую девушку. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Пожалуй, мне интересен твой вкус."
                elif Ch_Focus is DoreenX:
                        ch_d "Мне. . . кажется, твой вкус может быть. . . интересным. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Мне интересно, какова ты на вкус. . ."
            else: # Uninhibited
                if Ch_Focus is RogueX:
                        ch_r "Наверное, можно. . ."
                elif Ch_Focus is KittyX:
                        ch_k "[KittyX.Like]конечно. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Полагаю, можно попробовать. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Хм. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Хм. . ."
                elif Ch_Focus is StormX:
                        ch_s "Пожалуй, можно. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Я в деле. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Ну, звучит весело. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Пожалуй, можно. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Наверное, можно. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Это может быть весело."


        elif Approval:
            #Second time+ dialog
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Love", 70, -3, 1)
                $ Ch_Focus.Statup("Love", 20, -2, 1)
                if Ch_Focus is RogueX:
                        ch_r "И все? . ."
                elif Ch_Focus is KittyX:
                        ch_k "И ничего. . . более. . ?"
                elif Ch_Focus is EmmaX:
                        ch_e "Немного скучновато. . ."
                elif Ch_Focus is LauraX:
                        ch_l ". . ."
                elif Ch_Focus is JeanX:
                        ch_j "Фи."
                elif Ch_Focus is StormX:
                        ch_s "Я думала, ты захочешь большего. . ."
                elif Ch_Focus is JubesX:
                        ch_v ". . . И все?"
                elif Ch_Focus is GwenX:
                        ch_g "Хорошо. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Это все, что тебе нужно?"
                elif Ch_Focus is DoreenX:
                        ch_d "Это все, чего ты хочешь? . ."
                elif Ch_Focus is WandaX:
                        ch_w "И все?"
            elif "cun" in Ch_Focus.RecentActions:
                $ Ch_Focus.FaceChange("sexy", 1)
                jump Girl_CUN_Prep
            elif "cun" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Вернулась так скоро?",
                    "У меня от тебя челюсть сведет.",
                    "Дай-ка я наберу немного слюны.",
                    "Тебе мало прошлого раза?",
                    "У меня после прошлого раза все еще побаливает челюсть.",
                    "У меня после прошлого раза все еще побаливает челюсть."])
                call AnyLine(Ch_Focus,Line)
            else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Хочешь этого. . . [делает жест язычком]?",
                    "Значит, хочешь, чтобы я снова тебе отлизала",
                    "Немного. . . полизать?",
                    "Хочешь, попробовать еще раз?",
                    "Еще разок поработать язычком?"])
                call AnyLine(Ch_Focus,Line)
            $ Line = 0


        if Approval >= 2:
            #She's into it. . .
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Obed", 90, 1)
                $ Ch_Focus.Statup("Inbt", 60, 1)
                if Ch_Focus is RogueX:
                        ch_r "Как скажешь."
                elif Ch_Focus is KittyX:
                        ch_k "Как хочешь."
                elif Ch_Focus is EmmaX:
                        ch_e "Хорошо."
                elif Ch_Focus is LauraX:
                        ch_l "Как скажешь."
                elif Ch_Focus is JeanX:
                        ch_j "Ладно, давай скорее покончим с этим."
                elif Ch_Focus is StormX:
                        ch_s "Хорошо."
                elif Ch_Focus is JubesX:
                        ch_v "Ладно, твоя взяла."
                elif Ch_Focus is GwenX:
                        ch_g "Конечно, как скажешь."
                elif Ch_Focus is BetsyX:
                        ch_b "Если это так необходимо. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Ладно. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Конечно."
            else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Statup("Love", 90, 1)
                $ Ch_Focus.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Конечно. Аххххх.",
                    "Ну. . . ладно.",
                    "Ням.",
                    "Конечно, давай ее сюда.",
                    "Ладно. . . [Облизывает губы].",
                    "Хорошо, давай посмотрим на нее."])
                call AnyLine(Ch_Focus,Line)
                $ Line = 0
            $ Ch_Focus.Statup("Obed", 20, 1)
            $ Ch_Focus.Statup("Obed", 70, 1)
            $ Ch_Focus.Statup("Inbt", 80, 2)
            jump Girl_CUN_Prep

        elif Ch_Focus is JubesX and not Taboo and not JubesX.Taboo:
            #if Jubilee's not in public, she's down.
            if JubesX.Blow > 3 and "angry" not in JubesX.RecentActions:
                $ JubesX.FaceChange("sexy", 1)
                $ JubesX.Statup("Love", 90, 2)
                $ JubesX.Statup("Love", 70, 1)
                $ JubesX.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Конечно. Мммм. . .",
                    "Ну. . . конечно!",
                    "Ням.",
                    "Конечно, дай мне на нее посмотреть.",
                    "Ладно. . . [Облизывает губы].",
                    "Ладно."])
                ch_v "[Line]"
                $ Line = 0
                $ JubesX.Statup("Obed", 20, 1)
                $ JubesX.Statup("Obed", 70, 1)
                $ JubesX.Statup("Inbt", 80, 2)
                jump Girl_CUN_Prep
            ch_v "Ладно, конечно."
            menu:
                extend ""
                "Извини, заб- Что?" if "no cun" in JubesX.DailyActions:
                    $ JubesX.FaceChange("sad")
                    ch_v "Не давай заднюю. . ."
                    $ JubesX.FaceChange("sexy")
                "Может, в др- а?" if "no cun" not in JubesX.DailyActions:
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
                "Лижи, [JubesX.Pet].":                                               # Pressured into it
                    $ JubesX.NameCheck() #checks reaction to petname
                    $ JubesX.FaceChange("confused")
                    $ Approval = ApprovalCheck(JubesX, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                    if Approval > 1 or (Approval and JubesX.Forced):
                        $ JubesX.Statup("Love", 70, -5, 1)
                        $ JubesX.Statup("Love", 200, -2)
                        ch_v "Ладно. . . расслабься. . ."
                        $ JubesX.FaceChange("sly")
                        ch_v "Я же сказала, что мне и самой этого хотелось бы. . ."
                        $ JubesX.Statup("Obed", 50, 4)
                        $ JubesX.Statup("Inbt", 80, 1)
                        $ JubesX.Statup("Inbt", 60, 3)
                        $ JubesX.Forced = 1
                    else:
                        $ JubesX.Statup("Love", 200, -5)
                        ch_v "Ох, не порти момент. . ."
                "Клево.":
                        $ JubesX.FaceChange("sly")
                        $ JubesX.Statup("Love", 80, 2)
                        $ JubesX.Statup("Obed", 50, 2)
                        $ JubesX.Statup("Obed", 70, 1)
                        $ JubesX.Statup("Inbt", 70, 2)
            if not JubesX.CUN:
                    ch_v "Мне нужно попробовать. . ."
            else:
                    ch_v "Я просто не могу удержаться."
            jump Girl_CUN_Prep
            #end jubilee exception
        else:
            #She's not into it, but maybe. . .
            $ Ch_Focus.FaceChange("angry")
            if "no cun" in Ch_Focus.DailyActions:
                call AnyLine(Ch_Focus,"Я уже сказала тебе \"нет,\" "+Ch_Focus.Petname+".")
            elif Taboo and "tabno" in Ch_Focus.DailyActions:
                call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
            else:
                $ Ch_Focus.FaceChange("bemused")
                if Ch_Focus is RogueX:
                        ch_r "Может, не сейчас? . ."
                elif Ch_Focus is KittyX:
                        ch_k "Я не уверена. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Я так не думаю. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Нет."
                elif Ch_Focus is JeanX:
                        ch_j "Не-а."
                elif Ch_Focus is StormX:
                        ch_s "Я так не думаю. . ."
                elif Ch_Focus is JubesX:
                        ch_v ". . . нет?"
                elif Ch_Focus is GwenX:
                        ch_g "Я не уверена. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Я бы предпочла этого не делать. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Может. . . не будем?"
                elif Ch_Focus is WandaX:
                        ch_w "Я не уверена."
            menu:
                extend ""
                "Извини, забудь." if "no cun" in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("bemused")
                    if Ch_Focus is RogueX:
                            ch_r "Ага, ладно, [Ch_Focus.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Оу, все нормально, [KittyX.Petname]."
                    elif Ch_Focus is EmmaX:
                            ch_e "Все нормально, никто не пострадал, [EmmaX.Petname]."
                    elif Ch_Focus is LauraX:
                            ch_l "Клево."
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно."
                    elif Ch_Focus is StormX:
                            ch_s "Все нормально, [StormX.Petname]."
                    elif Ch_Focus is JubesX:
                            $ JubesX.FaceChange("sad")
                            ch_v "Ладно. . ."
                            ch_v "Но, наверное, в другом месте. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Все нормально, спасибо. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Я это ценю."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ох, все хорошо."
                    elif Ch_Focus is WandaX:
                            ch_w "Конечно, не волнуйся."
                    return
                "Может, в другой раз?" if "no cun" not in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("sexy")
                    if Ch_Focus is RogueX:
                            ch_r "В следующий раз я могу быть голодна, [Ch_Focus.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Заранее[KittyX.like]не узнаешь, [KittyX.Petname]."
                    elif Ch_Focus is EmmaX:
                            ch_e "Нельзя этого исключать, [EmmaX.Petname]."
                    elif Ch_Focus is LauraX:
                            ch_l "Ага, может быть, [LauraX.Petname]."
                    elif Ch_Focus is JeanX:
                            ch_j "Конечно, как скажешь, [JeanX.Petname]."
                    elif Ch_Focus is StormX:
                            ch_s "Не исключено, [StormX.Petname]."
                    elif Ch_Focus is JubesX:
                            ch_v "Ага, точно!"
                    elif Ch_Focus is GwenX:
                            ch_g "Ага, может быть. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b ". . . возможно."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я. . . наверное. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Не исключено."
                    $ Ch_Focus.Statup("Love", 80, 2)
                    $ Ch_Focus.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ Ch_Focus.RecentActions.append("tabno")
                        $ Ch_Focus.DailyActions.append("tabno")
                    $ Ch_Focus.RecentActions.append("no cun")
                    $ Ch_Focus.DailyActions.append("no cun")
                    return
                "Ну давай, пожалуйста?":
                    if Approval:
                        $ Ch_Focus.FaceChange("sexy")
                        $ Ch_Focus.Statup("Obed", 90, 2)
                        $ Ch_Focus.Statup("Obed", 50, 2)
                        $ Ch_Focus.Statup("Inbt", 70, 3)
                        $ Ch_Focus.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Ну, конечно, ааааах.",
                            "Ну. . . ладно.",
                            "Думаю, попробовать не помешает.",
                            "Думаю, можно. . . давай ее сюда.",
                            "Ладно. . . [Она облизывает свои губы].",
                            "Хех, ладно."])
                        call AnyLine(Ch_Focus,Line)
                        $ Line = 0
                        jump Girl_CUN_Prep
                    elif Ch_Focus is JubesX:
                        pass
                    else:
                        if ApprovalCheck(Ch_Focus, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)
                            #Fingering instead?
                            $ Ch_Focus.Statup("Inbt", 80, 1)
                            $ Ch_Focus.Statup("Inbt", 60, 3)
                            $ Ch_Focus.FaceChange("confused", 1)
                            $ Ch_Focus.ArmPose = 2
                            if Ch_Focus is RogueX:
                                    if Ch_Focus.Finger:
                                        ch_r "Может, я лучше воспользуюсь своими пальчиками?"
                                    else:
                                        ch_r "Может, я могла бы. . . [[шевелит пальцами]?"
                            elif Ch_Focus is KittyX:
                                    if Ch_Focus.Finger:
                                        ch_k "Может, я просто воспользуюсь своими пальчиками?"
                                    else:
                                        ch_k "Может, я могла бы. . . [[шевелит пальцами]?"
                            elif Ch_Focus is EmmaX:
                                    if Ch_Focus.Finger:
                                        ch_e "Возможно, я могла бы просто поласкать тебя?"
                                    else:
                                        ch_e "Может, тебя устроят мои пальчики?"
                            elif Ch_Focus is LauraX:
                                    if Ch_Focus.Finger:
                                        ch_l "Разве я не могу снова воспользоваться своими пальцами?"
                                        ch_l "Мне казалось, тебе это нравится."
                                    else:
                                        ch_l "Может, вместо этого я могла бы тебя поласкать, что думаешь?"
                            elif Ch_Focus is JeanX:
                                    if "psysex" in JeanX.History:
                                        ch_j "Может, я снова воспользуюсь своей способностью?"
                                        $ JeanX.FaceChange("sly", 1)
                                        ch_j "Тебе понравится. . ."
                                    else:
                                        ch_j "Может я просто воспользуюсь телекинезом?"
                                        $ JeanX.FaceChange("confused", 1)
                                        ch_j "Это будет здорово, обещаю. . ."
                            elif Ch_Focus is StormX:
                                    if Ch_Focus.Finger:
                                        ch_s "Возможно, я могла бы просто поласкать тебя?"
                                    else:
                                        ch_s "Может тебя устроят мои пальчики?"
                            elif Ch_Focus is GwenX:
                                    ch_g "Может, я могу просто поласкать тебя?"
                            elif Ch_Focus is BetsyX:
                                    ch_b "Может, тебя устроят мои пальчики?"
                            elif Ch_Focus is DoreenX:
                                    ch_d "Могу я, эм. . . просто воспользоваться своими пальчиками?"
                            elif Ch_Focus is WandaX:
                                    ch_w "Как насчет того, чтобы я просто поласкала тебя пальцами?"
                            menu:
                                extend ""
                                "Конечно, я не против.":
                                    $ Ch_Focus.Statup("Love", 80, 2)
                                    $ Ch_Focus.Statup("Inbt", 60, 1)
                                    $ Ch_Focus.Statup("Obed", 50, 1)
                                    if Ch_Focus is JeanX:
                                            jump Jean_PJ_Prep
                                    jump Girl_Finger_Prep
                                "Нет, это не очень приятно.":
                                    $ Ch_Focus.Statup("Love", 200, -2)
                                    if Ch_Focus is RogueX:
                                            ch_r "Ага, ладно, [Ch_Focus.Petname]."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Ладно, многое теряешь."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Жаль."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Ладно, как хочешь."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Жаль."
                                    elif Ch_Focus is StormX:
                                            ch_s "Очень жаль."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Оу, облом. . ."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Ну и ладно."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Оу, жаль."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Отказываешься от моих нежных пальчиков?"
                                    $ Ch_Focus.Statup("Obed", 70, 2)


                "Лижи, [Ch_Focus.Pet].":
                    # Pressured into it
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    $ Approval = ApprovalCheck(Ch_Focus, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                    if Approval > 1 or (Approval and Ch_Focus.Forced):
                        $ Ch_Focus.FaceChange("sad")
                        $ Ch_Focus.Statup("Love", 70, -5, 1)
                        $ Ch_Focus.Statup("Love", 200, -2)
                        if Ch_Focus is RogueX:
                                ch_r "Ладно, хорошо, довай ее сюда."
                        elif Ch_Focus is KittyX:
                                ch_k "Ладно. . ."
                        elif Ch_Focus is EmmaX:
                                ch_e "Хорошо. . ."
                        elif Ch_Focus is LauraX:
                                ch_l "Как скажешь. . ."
                        elif Ch_Focus is JeanX:
                                $ JeanX.FaceChange("angry",2)
                                ch_j ". . ."
                                $ JeanX.FaceChange("angry",1,Eyes="side")
                                ch_j "Как скажешь. . ."
                        elif Ch_Focus is StormX:
                                ch_s ". . . Ладно. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Ладно. . . хорошо. . ."
                        elif Ch_Focus is GwenX:
                                ch_g ". . . ладно. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Давай. . . тогда быстрее перейдем к делу. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d ". . . ладно. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Ладно, как пожелаешь."
                        $ Ch_Focus.Statup("Obed", 50, 4)
                        $ Ch_Focus.Statup("Inbt", 80, 1)
                        $ Ch_Focus.Statup("Inbt", 60, 3)
                        $ Ch_Focus.Forced = 1
                        jump Girl_CUN_Prep
                    else:
                        $ Ch_Focus.Statup("Love", 200, -15)
                        $ Ch_Focus.RecentActions.append("angry")
                        $ Ch_Focus.DailyActions.append("angry")

        #She refused all offers.
        if "no cun" in Ch_Focus.DailyActions:
            $ Ch_Focus.FaceChange("angry", 1)
            if Ch_Focus is RogueX:
                    ch_r "Читай по губам, -НЕТ-."
            elif Ch_Focus is KittyX:
                    ch_k "Я не буду лизать твою кисоньку. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Тогда, надеюсь, ты сможешь позаботиться о себе сама."
            elif Ch_Focus is LauraX:
                    $ LauraX.ArmPose = 2
                    $ LauraX.Claws = 1
                    ch_l "Выкуси."
                    $ LauraX.ArmPose = 1
                    $ LauraX.Claws = 0
            elif Ch_Focus is JeanX:
                    ch_j "Ты хочешь, чтобы я заставила тебя отлизать самой себе?"
                    $ JeanX.ArmPose = 1
                    $ JeanX.FaceChange("angry",1,Eyes="side")
                    ch_j "Чёрт. . . я забыла, что не могу. . ."
            elif Ch_Focus is StormX:
                    ch_s "Тогда, надеюсь, ты сможешь позаботиться о себе сама."
            elif Ch_Focus is JubesX:
                    ch_v "Я не сосу -все-, что мне предлагают."
            elif Ch_Focus is GwenX:
                    ch_g "Я другого рода \"наемница!\". . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Я ясно высказала свое мнение."
            elif Ch_Focus is DoreenX:
                    ch_d "Я сказала, \"нет\"!"
            elif Ch_Focus is WandaX:
                    ch_w "Не сейчас."
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
                    ch_l "Лучше бы тебе не давить."
            elif Ch_Focus is JeanX:
                    ch_j "Я не буду этого делать."
            elif Ch_Focus is StormX:
                    ch_s "Ты заходишь слишком далеко!"
            elif Ch_Focus is JubesX:
                    $ Ch_Focus.FaceChange("sad", 1)
                    ch_v "Хотела бы я это сделать, но. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Извини. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Мне кажется, это слишком. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Ни за что!"
            elif Ch_Focus is WandaX:
                    ch_w "Забудь."
            $ Ch_Focus.Statup("Lust", 200, 5)
            if Ch_Focus.Love > 300:
                    $ Ch_Focus.Statup("Love", 70, -2)
            $ Ch_Focus.Statup("Obed", 50, -2)
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
            $ Ch_Focus.RecentActions.append("no cun")
            $ Ch_Focus.DailyActions.append("no cun")
            return
        elif Taboo:                             # she refuses and this is too public a place for her
            $ Ch_Focus.FaceChange("angry", 1)
            $ Ch_Focus.DailyActions.append("tabno")
            call Sex_Basic_Dialog(Ch_Focus,"tabno")
            $ Ch_Focus.Statup("Lust", 200, 5)
            $ Ch_Focus.Statup("Obed", 50, -3)
            return
        elif Ch_Focus.CUN:
            $ Ch_Focus.FaceChange("sad")
            if Ch_Focus is RogueX:
                    ch_r "Кажется, теперь у меня во рту появился неприятный привкус, спасибо."
            elif Ch_Focus is KittyX:
                    ch_k "Нет, не в этот раз."
            elif Ch_Focus is EmmaX:
                    ch_e "Я так не думаю."
            elif Ch_Focus is LauraX:
                    ch_l "Не-а."
            elif Ch_Focus is JeanX:
                    ch_j "Нет, не в этот раз."
            elif Ch_Focus is StormX:
                    ch_s "Я совсем не в настроении, [StormX.Petname]."
            elif Ch_Focus is JubesX:
                    ch_v "Эм, нет. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Я не хочу снова заниматься этим. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Не сейчас, [BetsyX.Petname]."
            elif Ch_Focus is DoreenX:
                    ch_d "Я так не думаю. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Не сейчас."
        else:
            $ Ch_Focus.FaceChange("normal", 1)
            if Ch_Focus is RogueX:
                    ch_r "Не интересует."
            elif Ch_Focus is KittyX:
                    ch_k "Не-а."
            elif Ch_Focus is EmmaX:
                    ch_e "Я бы предпочла этого не делать. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Не-а."
            elif Ch_Focus is JeanX:
                    ch_j "Ха! Хорошая попытка."
            elif Ch_Focus is StormX:
                    ch_s "Не думаю, что соглашусь."
            elif Ch_Focus is JubesX:
                    ch_v "Не-а."
            elif Ch_Focus is GwenX:
                    ch_g "Эм, нет, спасибо."
            elif Ch_Focus is BetsyX:
                    ch_b "Я бы предпочла этого не делать, спасибо."
            elif Ch_Focus is DoreenX:
                    ch_d "Ох, нет, спасибо. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Нет, мне и без этого хорошо."
        $ Ch_Focus.RecentActions.append("no cun")
        $ Ch_Focus.DailyActions.append("no cun")
        $ Tempmod = 0
        return




label Girl_CUN_Prep:    #rkeljsvg
#        if Girl == WandaX:       #fix, remove           fix, remove           fix, remove           fix, remove
#            "This is not implemented yet."
#            return              #fix, remove           fix, remove           fix, remove           fix, remove
#        call Shift_Focus(Girl)
        if Taboo:
            $ Ch_Focus.Inbt += int(Taboo/10)
            $ Ch_Focus.Lust += int(Taboo/5)

        $ Ch_Focus.FaceChange("sexy")
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
        elif not Ch_Focus.CUN:
            $ Ch_Focus.Brows = "confused"
            $ Ch_Focus.Eyes = "sexy"
            $ Ch_Focus.Mouth = "smile"

        call Seen_First_Peen(Ch_Focus,Partner,React=Situation)
        call expression Ch_Focus.Tag + "_CUN_Launch" pass ("L")

        if Situation == Ch_Focus:
                #Girl auto-starts
                $ Situation = 0
                "[Ch_Focus.Name] опускается к вашей киске и слегка облизывает ее."
                menu:
                    "Что будете делать?"
                    "Ничего не делать.":
                        $ Ch_Focus.Statup("Inbt", 80, 3)
                        $ Ch_Focus.Statup("Inbt", 40, 2)
                        "[Ch_Focus.Name] продолжает ее лизать."
                    "Похвалить ее.":
                        $ Ch_Focus.FaceChange("sexy", 1)
                        $ Ch_Focus.Statup("Inbt", 80, 3)
                        ch_p "Хмммм, продолжай, [Ch_Focus.Pet]."
                        $ Ch_Focus.NameCheck() #checks reaction to petname
                        "[Ch_Focus.Name] продолжает свои действия."
                        $ Ch_Focus.Statup("Love", 85, 1)
                        $ Ch_Focus.Statup("Obed", 90, 1)
                        $ Ch_Focus.Statup("Obed", 50, 2)
                    "Сказать ей остановиться.":
                        $ Ch_Focus.FaceChange("surprised")
                        $ Ch_Focus.Statup("Inbt", 70, 1)
                        ch_p "Давай сейчас не будем, [Ch_Focus.Pet]."
                        $ Ch_Focus.NameCheck() #checks reaction to petname
                        "[Ch_Focus.Name] отстраняется."
                        $ Ch_Focus.Statup("Obed", 90, 1)
                        $ Ch_Focus.Statup("Obed", 50, 3)
                        $ Player.RecentActions.append("nope")
                        $ Ch_Focus.AddWord(1,"refused","refused")
                        return

        if not Ch_Focus.CUN:
            if Ch_Focus.Forced:
                $ Ch_Focus.Statup("Love", 90, -70)
                $ Ch_Focus.Statup("Obed", 70, 45)
                $ Ch_Focus.Statup("Inbt", 80, 60)
            else:
                $ Ch_Focus.Statup("Love", 90, 5)
                $ Ch_Focus.Statup("Obed", 70, 35)
                $ Ch_Focus.Statup("Inbt", 80, 40)

        if Situation:
#            $ renpy.pop_call()
            $ Situation = 0
        $ Line = 0
        $ Cnt = 0
        if Taboo:
            $ Ch_Focus.DrainWord("tabno")
        $ Ch_Focus.DrainWord("no cun")
        $ Ch_Focus.RecentActions.append("cun")
        $ Ch_Focus.DailyActions.append("cun")

label Girl_CUN_Cycle: #rkeljsvg
        while Round > 0:
#            call Shift_Focus(Girl)
            call expression Ch_Focus.Tag + "_CUN_Launch"
            $ Trigger = "cun"
            $ Ch_Focus.LustFace()

            if  Player.Focus < 100:
                        if "setpace" in Ch_Focus.DailyActions:
                                $ D20 = renpy.random.randint(1, 20)
                                if Ch_Focus.CUN < 5:
                                    $ D20 -= 10
                                elif Ch_Focus.CUN < 10:
                                    $ D20 -= 5
                                if D20 > 10:
                                    $ Speed = 3
                                elif D20 > 5:
                                    $ Speed = 2
                                else:
                                    $ Speed = 1
                        #Player Command menu
                        menu:
                            "Продолжать. . ." if Speed:
                                        pass

                            "Облизывай ее. . ." if Speed != 1:
                                    $ Speed = 1
                                    $ Ch_Focus.DrainWord("setpace",1,0,0,0)
                            "Облизывай ее. . . (locked)" if Speed == 1:
                                    pass

                            "Возьми в рот клитор. . ." if Speed != 2:
                                    $ Speed = 2
                                    $ Ch_Focus.DrainWord("setpace",1,0,0,0)
                            "Возьми в рот клитор. . . (locked)" if Speed == 2:
                                    pass

                            "Соси ее." if Speed != 3:
                                    $ Speed = 3
                                    $ Ch_Focus.DrainWord("setpace",1,0,0,0)
                                    if Trigger2 == "jilling":
                                        "Она опускает голову чуть ниже и вы убираете свои пальцы."

                                    if Ch_Focus is LauraX  and "met" not in GwenX.History and "Gwentro" not in LauraX.History: #calls the special Gwentro event
                                                call Gwentro

                            "Соси ее. (locked)" if Speed == 3:
                                    pass

                            "Делай, что тебе больше хочется. . .":
                                    "[Ch_Focus.Name] издает звук согласия."
                                    if "setpace" not in Ch_Focus.DailyActions:
                                            $ Ch_Focus.Statup("Love", 80, 2)
                                    $ D20 = renpy.random.randint(1, 20)
                                    if Ch_Focus.CUN < 5:
                                        $ D20 -= 10
                                    elif Ch_Focus.CUN < 10:
                                        $ D20 -= 5
                                    if D20 > 10:
                                        $ Speed = 3
                                    elif D20 > 5:
                                        $ Speed = 2
                                    else:
                                        $ Speed = 1
                                    $ Ch_Focus.AddWord(1,"setpace","setpace")

                            "69 [[locked] (locked)" if "69" not in Ch_Focus.History:
                                        pass
                            "69" if Ch_Focus.Pose != "69" and ("69" in Ch_Focus.History and "69" in Player.History and Ch_Focus.SEXP >= 30):
                                        $ Ch_Focus.Pose = "69"
                                        call expression Ch_Focus.Tag + "_BJ_Launch"
                                        jump Girl_CUN_Cycle
                            "Встать" if Ch_Focus.Pose == "69":
                                        $ Ch_Focus.Pose = 0
                                        call expression Ch_Focus.Tag + "_BJ_Launch"
                                        jump Girl_CUN_Cycle

                            "Концентрироваться на продолжительности [[Не открыто] (locked)" if "focus" not in Player.Traits:
                                        pass
                            "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                        "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                        $ Player.FocusX = 1
                            "Прекратить концентрироваться." if Player.FocusX:
                                        "Вы расслабляетесь. . ."
                                        $ Player.FocusX = 0

                            "Другие варианты":
                                    menu:
                                        "Дополнительное действие" if Ch_Focus.Loc == bg_current and Ch_Focus.Pose == "69":
                                                if Ch_Focus.Action and MultiAction:
                                                    call Offhand_Set
                                                    if Trigger2:
                                                        $ Ch_Focus.Action -= 1
                                                else:
                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")

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
                                                            "Может, поласкаешь мою киску пальчиками?":
                                                                    if Ch_Focus.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Girl_CUN_After
                                                                        call Girl_Finger
                                                                    else:
                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")
#                                                            "How about a titjob?":
#                                                                    if Ch_Focus.Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call Girl_CUN_After
#                                                                        call Girl_Titjob
#                                                                    else:
#                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                            "Неважно":
                                                                    jump Girl_CUN_Cycle
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
                                                            jump Girl_CUN_Cycle
                                                "Привести в порядок [Partner.Name_vin] (locked)" if not Partner.Spunk:
                                                            pass
                                                "Привести в порядок [Partner.Name_vin]" if Partner.Spunk:
                                                            call Girl_Cleanup(Partner,"ask")
                                                            jump Girl_CUN_Cycle
                                                "Неважно":
                                                            jump Girl_CUN_Cycle
                                        "Раздеть [Ch_Focus.Name_vin]":
                                                call Girl_Undress(Ch_Focus)
                                        "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                                pass
                                        "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                                call Girl_Cleanup(Ch_Focus,"ask")
                                        "Неважно":
                                                jump Girl_CUN_Cycle

                            "Вернуться к Секс-меню" if MultiAction:
                                        ch_p "Нам стоит попробовать что-нибудь другое."
                                        call expression Ch_Focus.Tag + "_CUN_Reset"
                                        $ Situation = "shift"
                                        $ Line = 0
                                        jump Girl_CUN_After
                            "Закончить" if not MultiAction:
                                        ch_p "Нам стоит пока закончить."
                                        call expression Ch_Focus.Tag + "_CUN_Reset"
                                        $ Line = 0
                                        jump Girl_CUN_After
            #End menu (if Line)

#            call Shift_Focus(Girl)
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
                                    call expression Ch_Focus.Tag + "_CUN_Reset"
                                    return
                                $ Ch_Focus.Statup("Lust", 200, 5)
                                if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2 and Ch_Focus.SEXP >= 20:
                                    $ Ch_Focus.RecentActions.append("unsatisfied")
                                    $ Ch_Focus.DailyActions.append("unsatisfied")
                                if Player.Focus > 80:
                                    jump Girl_CUN_After
                                $ Line = "came"

                        if Ch_Focus.Lust >= 100:
                                #If Girl can cum
                                call Girl_Cumming(Ch_Focus)
                                if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                    jump Girl_CUN_After

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
                                            jump Girl_CUN_After
            if Partner and Partner.Lust >= 100:
                    #Checks if partner could orgasm
                    call Girl_Cumming(Partner)
            #End orgasm

            $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

            if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
                pass
            elif Cnt == (5 + Ch_Focus.CUN):
                        $ Ch_Focus.Brows = "confused"
                        call AnyLine(Ch_Focus,"Ты скоро? У меня начинает болеть челюсть.")
            elif Cnt == (10 + Ch_Focus.CUN):
                        $ Ch_Focus.Brows = "angry"
                        call AnyLine(Ch_Focus,"Мы можем заняться чем-нибудь другим?")
                        menu:
                            extend ""
                            "Продолжим (locked)":
                                    pass
                            "Может поласкаешь мою киску пальчиками?" if Ch_Focus.Action and MultiAction:
                                    $ Situation = "shift"
                                    call Girl_CUN_After
                                    call Girl_Finger
                                    return
                            "Может поласкаешь мою киску пальчиками? (locked)" if not Ch_Focus.Action or not MultiAction:
                                    pass
                            "Закончить." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                                    $ Player.Focus += 15
                                    jump Girl_CUN_Cycle
                            "Закончить. (locked)" if not Player.FocusX:
                                    pass
                            "Давай попробуем что-нибудь другое." if MultiAction:
                                    $ Line = 0
                                    call expression Ch_Focus.Tag + "_CUN_Reset"
                                    $ Situation = "shift"
                                    jump Girl_CUN_After
                            "Давай попробуем что-нибудь другое. (locked)" if not MultiAction:
                                    pass
                            "Нет, давай за работу.":
                                    if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                        $ Ch_Focus.Statup("Love", 200, -5)
                                        $ Ch_Focus.Statup("Obed", 50, 3)
                                        $ Ch_Focus.Statup("Obed", 80, 2)
                                        "Она ворчит, но возвращается к работе."
                                    else:
                                        $ Ch_Focus.FaceChange("angry", 1)
                                        "Она кидает на вас сердитый взгляд и отстраняется."
                                        call AnyLine(Ch_Focus,"Я так не думаю.")
                                        $ Ch_Focus.Statup("Love", 50, -3, 1)
                                        $ Ch_Focus.Statup("Love", 80, -4, 1)
                                        $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                        $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                        $ Ch_Focus.RecentActions.append("angry")
                                        $ Ch_Focus.DailyActions.append("angry")
                                        jump Girl_CUN_After
            #End Count check

            call Escalation(Ch_Focus) #sees if she wants to escalate things

            if Round == 10:
                    call Sex_Basic_Dialog(Ch_Focus,10) #"It is getting late, [Ch_Focus.Petname]. . ."
            elif Round == 5:
                    call Sex_Basic_Dialog(Ch_Focus,5)   #"We should take a break soon."

        #Round = 0 loop breaks
        $ Ch_Focus.FaceChange("bemused", 0)
        $ Line = 0
        call Sex_Basic_Dialog(Ch_Focus,"done") # ch_s "I need to take a moment to collect myself."

label Girl_CUN_After:   #rkeljsvg
        $ Ch_Focus.FaceChange("sexy")
        $ Ch_Focus.CUN += 1
        $ Ch_Focus.Action -=1
        $ Ch_Focus.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ Ch_Focus.Addictionrate += 1

        call Partner_Like(Ch_Focus,2)

        if "Girl Jobber" in Achievements:
            pass
        elif Ch_Focus.CUN >= 10:
            $ Ch_Focus.FaceChange("smile", 1)
            if Ch_Focus is RogueX:
                    ch_r "Признаюсь, я начинаю получать от этого удовольствие."
            elif Ch_Focus is KittyX:
                    ch_k "Я не могу[KittyX.like]выбросить твой вкус из головы."
            elif Ch_Focus is EmmaX:
                    ch_e "Твой вкус меня опьяняет, [EmmaX.Petname]."
            elif Ch_Focus is LauraX:
                    ch_l "Твой вкус опьяняет."
            elif Ch_Focus is JeanX:
                    $ JeanX.FaceChange("confused", 1,Eyes="side")
                    ch_j "Вау, знаешь. . . мне никогда это особо не нравилось. . ."
                    $ JeanX.FaceChange("smile", 2)
                    ch_j "но, думаю, с тобой все как-то по-другому. . ."
                    $ JeanX.Blush = 1
            elif Ch_Focus is StormX:
                    ch_s "Не представляю, почему я так долго обходился без такого деликатеса, [StormX.Petname]."
            elif Ch_Focus is JubesX:
                    ch_v "Я все никак не могу насытиться. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Думаю, ты моя новая любимая закуска. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Это было поистине потрясающе. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Я прямо вхожу во вкус!"
            elif Ch_Focus is WandaX:
                    ch_w "Ты должна признать, что у меня хорошо получается."
            $ Achievements.append("Girl Jobber")
            $Ch_Focus.SEXP += 5
        elif Situation == "shift":
            pass
        elif Ch_Focus.CUN == 1:
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
                            ch_g "Вау, мне было дико интересно, каковы девушки на вкус в этой игре. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Это было восхитительно."
                    elif Ch_Focus is DoreenX:
                            ch_d "Это было на удивление весело!"
                    elif Ch_Focus is WandaX:
                            ch_w "Неплохо, правда?"
                elif Player.Focus <= 20:
                    $ Ch_Focus.Mouth = "sad"
                    if Ch_Focus is RogueX:
                            ch_r "Ну, я надеюсь, что ты получила хоть какое-то удовольствие."
                    elif Ch_Focus is KittyX:
                            ch_k "Надеюсь, тебе понравилось."
                    elif Ch_Focus is EmmaX:
                            ch_e "Ты получила все, о чем мечтала?"
                    elif Ch_Focus is LauraX:
                            ch_l "Надеюсь, тебе понравилось."
                    elif Ch_Focus is JeanX:
                            ch_j "Ну, ты получила желаемое?"
                    elif Ch_Focus is StormX:
                            ch_s "Это оправдало твои ожидания?"
                    elif Ch_Focus is JubesX:
                            $ JubesX.FaceChange("sexy", 2,Eyes="side")
                            ch_v "Ого. . . "
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "То есть, надеюсь, что тебе понравилось."
                            $ JubesX.FaceChange("bemused", 1)
                    elif Ch_Focus is GwenX:
                            ch_g "Ну, похоже, тебе понравилось."
                    elif Ch_Focus is BetsyX:
                            ch_b "Полагаю, тебе понравилось."
                    elif Ch_Focus is DoreenX:
                            ch_d "Все прошло. . . нормально?"
                    elif Ch_Focus is WandaX:
                            ch_w "Ну как?"
        elif Ch_Focus.CUN == 5:
                if Ch_Focus is RogueX:
                        ch_r "Думаю, у меня стало неплохо получаться."
                elif Ch_Focus is KittyX:
                        ch_k "С каждым разом у меня получается все лучше. . . верно?"
                elif Ch_Focus is EmmaX:
                        ch_e "Уверена, это лучшее, что когда-либо с тобой происходило."
                elif Ch_Focus is LauraX:
                        ch_l "Я ведь в самом деле начинаю разбираться в этом. . . правда?"
                elif Ch_Focus is JeanX:
                        ch_j "Мне это нравится. Тебе ведь тоже, верно?"
                elif Ch_Focus is StormX:
                        ch_s "Предполагаю, тебе понравилось."
                elif Ch_Focus is JubesX:
                        ch_v "Это. . . очень здорово."
                        ch_v "То есть, я знаю, что тебе это нравится и все такое, но. . ."
                        ch_v "Ого."
                elif Ch_Focus is GwenX:
                        ch_g "Ну, мне кажется, у меня начинает хорошо получаться."
                elif Ch_Focus is BetsyX:
                        ch_b "Ты прекрасная партнерша. Полагаю, со своей задачей я справляюсь?"
                elif Ch_Focus is DoreenX:
                        ch_d "На вкус ты намного лучше, чем я ожидала."
                elif Ch_Focus is WandaX:
                        ch_w "Неплохо, да?"
                menu:
                    extend ""
                    "[[кивнуть]":
                        $ Ch_Focus.FaceChange("smile", 1)
                        $ Ch_Focus.Statup("Love", 90, 15)
                        $ Ch_Focus.Statup("Obed", 80, 5)
                        $ Ch_Focus.Statup("Inbt", 90, 10)


                    "Ха, шлюха. . ." if Ch_Focus is JubesX:
                        if ApprovalCheck(JubesX, 250, "I"):
                            $ JubesX.FaceChange("sly", 1)
                            ch_v ". . . Агась. . ."
                        elif ApprovalCheck(JubesX, 250, "O"):
                            $ JubesX.FaceChange("sad", 1)
                            ch_v ". . . справедливое замечание."
                        else:
                            $ JubesX.FaceChange("angry", 2)
                            $ JubesX.Statup("Love", 200, -10)
                            ch_v ". . ."
                            $ JubesX.FaceChange("sad", 1)
                        $ JubesX.Statup("Obed", 80, 10)
                        $ JubesX.Statup("Inbt", 90, 10)
                    "[[покачать головой]":
                        if ApprovalCheck(Ch_Focus, 500, "O"):
                            $ Ch_Focus.FaceChange("sad", 2)
                            $ Ch_Focus.Statup("Love", 200, -5)
                        else:
                            $ Ch_Focus.FaceChange("angry", 2)
                            $ Ch_Focus.Statup("Love", 200, -25)
                            if Ch_Focus is EmmaX:
                                    $ Ch_Focus.Statup("Love", 200, -5)
                            elif Ch_Focus is JeanX:
                                    $ Ch_Focus.Statup("Obed", 80, 10)
                        $ Ch_Focus.Statup("Obed", 80, 10)
                        call AnyLine(Ch_Focus,". . .")
                        $ Ch_Focus.FaceChange("sad", 1)
        $ Tempmod = 0
        if Situation != "shift":
            call expression Ch_Focus.Tag + "_CUN_Reset"
        call Checkout
        return

return

# end Ch_Focus.CUN                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Dildo stuff
label Girl_Dildo_Check(Girl=0): #rkeljsvgb
    $ Girl = GirlCheck(Girl) #makes sure a girl is chosen
    if Girl not in TotalGirls:
            return
    if "dildo" in Player.Inventory:
            "Вы вытаскиваете большой резиновый фаллоимитатор. Повезло, что он у вас всегда под рукой."
    elif "dildo" in Girl.Inventory:
            "Вы просите ее достать свой любимый фаллоимитатор."
    else:
            "У вас нет его с собой."
            return 0
    return 1

label Girl_Vibrator_Check(Girl=0): #rkeljsvg
    $ Girl = GirlCheck(Girl) #makes sure a girl is chosen
    if Girl not in TotalGirls:
            return
    if "vibein" in Girl.DailyActions:
            pass
    elif "vibrator" in Player.Inventory:
            "Вы вытаскиваете видратор, как удобно, что он оказался у вас под рукой."
    elif "vibrator" in Girl.Inventory:
            "Вы просите [Girl.Name_vin] достать вибратор."
    else:
            "У вас нет его с собой."
            return 0
    return 1

label Dildo_Occupied(Girl=Ch_Focus,Target="pussy"):
        #Called if told to dildo, to make sure cock is not in there
        if Target == "anal":
                if Player.Cock == "anal":
                        $ Player.Cock = "out"
                        $ Player.Sprite = 0
                        if not Player.Male:
                            "Вы вытаскиваете свой резиновый член из попки [Girl.Name]."
                        else:
                            "Вы вытаскиваете свой член из попки [Girl.Name]."
        else: #Target != "anal":
                if Player.Cock == "in":
                        $ Player.Cock = "out"
                        $ Player.Sprite = 0
                        if not Player.Male:
                            "Вы вытаскиваете свой резиновый член из киски [Girl.Name]."
                        else:
                            "Вы вытаскиваете свой член из киски [Girl.Name]."
        return

label Cock_Occupied(Girl=Ch_Focus,Goal="pussy"):
        # call Cock_Occupied(RogueX,"pussy")
        #Called if told to cock, to make sure dildo is not in there
        if Goal == "anal":
                if "dildo anal" in (Trigger,Trigger2,Girl.Offhand): #if "dildo anal" in (Trigger,Trigger2,Trigger3,Trigger4,Trigger5):
                        if Trigger == "dildo anal":
                            $ Trigger = 0
                        elif Trigger2 == "dildo anal":
                            $ Trigger2 = 0
                        if Girl.Offhand == "dildo anal":
                            $ Girl.Offhand = 0
                        "Вы вытаскиваете фаллоимитатор из попки [Girl.Name_rod]."
        else: #Goal != "anal":
                if "dildo pussy" in (Trigger,Trigger2,Girl.Offhand):   #if "dildo pussy" in (Trigger,Trigger2,Trigger3,Trigger4,Trigger5):
                        if Trigger == "dildo pussy":
                            $ Trigger = 0
                        elif Trigger2 == "dildo pussy":
                            $ Trigger2 = 0
                        if Girl.Offhand == "dildo pussy":
                            $ Girl.Offhand = 0
                        "Вы вытаскиваете фаллоимитатор из киски [Girl.Name_rod]."
        return

label Girl_Dildo(Target="pussy"): #rkeljsvgb
    #Target is the location, "pussy" or "anal"
    # call Girl_Dildo(Ch_Focus,"pussy")
    $ Round -= 5 if Round > 5 else (Round-1)
#    call Shift_Focus(Girl)
    call Girl_Dildo_Check(Ch_Focus)
    if not _return:
        if Trigger2 == "dildo pussy" or Trigger2 == "dildo anal":
                $ Trigger2 = 0
        return

    if Target == "anal":
            if Ch_Focus.Loose:
                $ Tempmod += 30
            elif "anal" in Ch_Focus.RecentActions or "dildo anal" in Ch_Focus.RecentActions:
                $ Tempmod -= 20
            elif "anal" in Ch_Focus.DailyActions or "dildo anal" in Ch_Focus.DailyActions:
                $ Tempmod -= 10
            elif (Ch_Focus.Anal + Ch_Focus.DildoA + Ch_Focus.Plugged) > 0: #You've done it before
                $ Tempmod += 20
            elif Ch_Focus is DoreenX:
                $ Tempmod -= 10
    else: #if Target == "pussy":
            if Ch_Focus.DildoP: #You've done it before
                $ Tempmod += 15
            elif Ch_Focus is DoreenX:
                $ Tempmod -= 10

    if Ch_Focus.PantsNum() > 6: # she's got pants on.
        $ Tempmod -= 20

    if Ch_Focus.Lust > 95:
        $ Tempmod += 20
    elif Ch_Focus.Lust > 85: #She's really horny
        $ Tempmod += 15

    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (5*Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 40
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    if Taboo and "tabno" in Ch_Focus.DailyActions:
        $ Tempmod -= 10

    if "no dildo" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no dildo" in Ch_Focus.RecentActions else 0

    if Target == "anal":
            $ Approval = ApprovalCheck(Ch_Focus, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    else: #if Target == "pussy":
            $ Approval = ApprovalCheck(Ch_Focus, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if Situation == Ch_Focus:
                #Girl auto-starts
                if Approval > 2:                                                      # fix, add rogue auto stuff here
                    if Ch_Focus.PantsNum() == 5:
                        "[Ch_Focus.Name] берет свой фаллоимитатор, задирая при этом юбку."
                        $ Ch_Focus.Upskirt = 1
                    elif Ch_Focus.PantsNum() > 6:
                        "[Ch_Focus.Name] берет свой фаллоимитатор, стягивая при этом штаны."
                        $ Ch_Focus.Upskirt = 1
                    else:
                        "[Ch_Focus.Name] берет свой фаллоимитатор и возбуждающе водит им по своему телу."
                    $ Ch_Focus.SeenPanties = 1
                    if Target == "anal":
                        "Она прижимает кончик фаллоимитатора к своей попке, похоже, хочет, чтобы вы вставили его."
                    else:
                        "Она прижимает кончик фаллоимитатора к своей киске, похоже, хочет, чтобы вы вставили его."
                    menu:
                        "Что будете делать?"
                        "Ничего не делать.":
                            $ Ch_Focus.Statup("Inbt", 80, 3)
                            $ Ch_Focus.Statup("Inbt", 50, 2)
                            "[Ch_Focus.Name] вставляет его."
                        "Перехватить инициативу.":
                            $ Ch_Focus.FaceChange("sexy", 1)
                            $ Ch_Focus.Statup("Inbt", 80, 3)
                            ch_p "О да, [Ch_Focus.Pet], давай сделаем это."
                            $ Ch_Focus.NameCheck() #checks reaction to petname
                            "Вы берете фаллоимитатор и вставляете его внутрь."
                            $ Ch_Focus.Statup("Love", 85, 1)
                            $ Ch_Focus.Statup("Obed", 90, 1)
                            $ Ch_Focus.Statup("Obed", 50, 2)
                        "Сказать ей остановиться.":
                            $ Ch_Focus.FaceChange("surprised")
                            $ Ch_Focus.Statup("Inbt", 70, 1)
                            ch_p "Давай не будем сейчас этого делать, [Ch_Focus.Pet]."
                            $ Ch_Focus.NameCheck() #checks reaction to petname
                            "[Ch_Focus.Name] опускает фаллоимитатор."
                            $ Ch_Focus.Statup("Obed", 90, 1)
                            $ Ch_Focus.Statup("Obed", 50, 1)
                            $ Ch_Focus.Statup("Obed", 30, 2)
                            return
                    jump Girl_Dildo_Prep
                else:
                    $ Tempmod = 0                               # fix, add rogue auto stuff here
                    $ Trigger2 = 0
                return

    if Situation == "auto":
                call Dildo_Occupied(Ch_Focus,Target)
                if Target == "anal":
                    "Вы водите фаллоимитатором по ее телу и по ее тугому анусу."
                else:
                    "Вы водите фаллоимитатором по ее телу и по ее влажной щелке."
                $ Ch_Focus.FaceChange("surprised", 1)

                if Approval > 1 or (Approval and ((Target == "anal" and Ch_Focus.DildoA) or (Target != "anal" and Ch_Focus.DildoP))):
                    #this is not the first time you've used a dildo on her, or she's into it
                    "[Ch_Focus.Name] на мгновение пугается и поворачивается к вам, но затем улыбается и издает легкий стон."
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Statup("Obed", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 3)
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    call AnyLine(Ch_Focus,"Хорошо, давай сделаем это.")
                    jump Girl_Dildo_Prep
                else:                                                                                                            #she's questioning it
                    $ Ch_Focus.Brows = "angry"
                    call AnyLine(Ch_Focus,"Что это у тебя там?")
                    menu:
                        extend ""
                        "Извини-извини! Ничего такого.":
                            if Approval:
                                    $ Ch_Focus.FaceChange("sexy", 1)
                                    $ Ch_Focus.Statup("Obed", 70, 3)
                                    $ Ch_Focus.Statup("Inbt", 50, 3)
                                    $ Ch_Focus.Statup("Inbt", 70, 1)
                                    call AnyLine(Ch_Focus,"Ну, мы можем попробовать. . .")
                                    jump Girl_Dildo_Prep
                            "Вы отстраняетесь, прежде чем успеваете вставить его."
                            $ Ch_Focus.FaceChange("bemused", 1)
                            if Ch_Focus.DildoP:
                                    call AnyLine(Ch_Focus,"Ну, ничего страшного. . . просто предупреди меня в следующий раз.")
                            else:
                                    call AnyLine(Ch_Focus,"Ну, хорошо. . . может быть, в другой раз я соглашусь.")
                        "Просто играю с моими любимыми игрушками.":
                            $ Ch_Focus.Statup("Love", 80, -10, 1)
                            $ Ch_Focus.Statup("Love", 200, -10)
                            "Вы вставляете его немного глубже."
                            $ Ch_Focus.Statup("Obed", 70, 3)
                            $ Ch_Focus.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(Ch_Focus, 700, "O", TabM=1): #Checks if Obed is 700+
                                $ Ch_Focus.FaceChange("angry")
                                "[Ch_Focus.Name] отталкивает вас и бьет по лицу."
                                call AnyLine(Ch_Focus,"!!!")
                                call AnyLine(Ch_Focus,"Если таково твое отношение, то мы закончили!")
                                $ Ch_Focus.Statup("Love", 50, -10, 1)
                                $ Ch_Focus.Statup("Obed", 50, 3)
                                if renpy.showing(Girl.Tag+"_Doggy"):
                                        call expression Ch_Focus.Tag + "_Doggy_Reset"
                                $ Ch_Focus.RecentActions.append("angry")
                                $ Ch_Focus.DailyActions.append("angry")
                                $ renpy.pop_call()
                                if Situation:
                                        $ renpy.pop_call()
                            else:
                                $ Ch_Focus.FaceChange("sad")
                                "Похоже, [Ch_Focus.Name_dat] не нравится, но вам повезло, что она такая послушная."
                                jump Girl_Dildo_Prep
                return
    #end Auto

    if Target == "anal" and not Ch_Focus.DildoA:
            #first time
            $ Ch_Focus.FaceChange("surprised", 1)
            $ Ch_Focus.Mouth = "kiss"
            call AnyLine(Ch_Focus,"О, хочешь поиграть со мной?")
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                call AnyLine(Ch_Focus,"Хочешь в попку значит?")
            else:
                call AnyLine(Ch_Focus,"Еще и в попку. . .")
    elif not Ch_Focus.DildoP: #Target != "anal" and
            #first time
            $ Ch_Focus.FaceChange("surprised", 1)
            $ Ch_Focus.Mouth = "kiss"
            call AnyLine(Ch_Focus,"О, хочешь поиграть со мной?")
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                call AnyLine(Ch_Focus,"Ну, я думаю, это не так уж плохо.")

    if Approval and ((Target == "anal" and not Ch_Focus.DildoA) or (Target != "anal" and not Ch_Focus.DildoP)):
            #First time dialog
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Love", 70, -3, 1)
                $ Ch_Focus.Statup("Love", 20, -2, 1)
            else:
                if Ch_Focus.Love >= (Ch_Focus.Obed + Ch_Focus.Inbt):
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Brows = "sad"
                    $ Ch_Focus.Mouth = "smile"
                elif Ch_Focus.Obed >= Ch_Focus.Inbt:
                    $ Ch_Focus.FaceChange("normal")
                else: # Uninhibited
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Mouth = "smile"

                if Ch_Focus is RogueX:
                    if Target == "anal":
                        ch_r "Честно говоря, я ни разу не использовала подобное на попке. . ."
                    else:
                        ch_r "Знаешь, у меня приличный опыт такого рода. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Думаю, это не первое, что побывало во мне. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Игрушки могут развлечь. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Много вещей побывало во мне за эти годы. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Ты не хочешь прикасаться ко мне?"
                elif Ch_Focus is StormX:
                        ch_s "Творческий подход. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Это может быть очень весело. . ."
                elif Ch_Focus is GwenX:
                        if not Player.Male:
                            ch_g "Ты бы видела коллекцию игрушек, которую я собрала у себя дома. . ."
                        else:
                            ch_g "Ты бы видел коллекцию игрушек, которую я собрала у себя дома. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Это может быть приятным развлечением. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я. . . иногда. . . ими пользуюсь. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Ага, думаю, это может помочь. . ."

    elif Approval:
            #Second time+ dialog
            if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -3, 1)
                    $ Ch_Focus.Statup("Love", 20, -2, 1)
                    call AnyLine(Ch_Focus,"Снова игрушки?")
            elif not Taboo and "tabno" in Ch_Focus.DailyActions:
                    call Sex_Basic_Dialog(Ch_Focus,"tabyes")  #  "Well, at least you got us some privacy this time. . ."
            elif "dildo pussy" in Ch_Focus.RecentActions or "dildo anal" in Ch_Focus.RecentActions:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    call AnyLine(Ch_Focus,"Снова? Ну ладно.")
                    jump Girl_Dildo_Prep
            elif "dildo pussy" in Ch_Focus.DailyActions or "dildo anal" in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Line = renpy.random.choice(["Снова достаем игрушки?",
                        "Тебе все мало?",
                        "Ты меня измотаешь."])
                    call AnyLine(Ch_Focus,Line)
            elif Target == "anal" and Ch_Focus.DildoA < 3:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Brows = "confused"
                    $ Ch_Focus.Mouth = "kiss"
                    call AnyLine(Ch_Focus,"Хочешь снова вставить его мне в попку?")
            elif Target != "anal" and Ch_Focus.DildoP < 3:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Brows = "confused"
                    $ Ch_Focus.Mouth = "kiss"
                    call AnyLine(Ch_Focus,"Хочешь снова вставить его мне в киску?")
            else:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.ArmPose = 2
                    $ Line = renpy.random.choice(["Хочешь вставить его в меня?",
                        "Значит, хочешь еще разок?",
                        "Снова хочешь поиграть со мной?",
                        "Хочешь снова вставить его в меня?",
                        "Хочешь, чтобы я смазала твою игрушку?"])
                    call AnyLine(Ch_Focus,Line)
                    $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Obed", 90, 1)
                $ Ch_Focus.Statup("Inbt", 60, 1)
                call AnyLine(Ch_Focus,"Ладно.")
            else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Statup("Love", 90, 1)
                $ Ch_Focus.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Конечно, вставляй.",
                    "Ну. . . ладно.",
                    "Конечно!",
                    "Думаю, можно. . . вставляй.",
                    "О да.",
                    "Ладно-ладно."])
                call AnyLine(Ch_Focus,Line)
                $ Line = 0
            $ Ch_Focus.Statup("Obed", 20, 1)
            $ Ch_Focus.Statup("Obed", 60, 1)
            $ Ch_Focus.Statup("Inbt", 70, 2)
            jump Girl_Dildo_Prep

    else:
            #She's not into it, but maybe. . .
            $ Ch_Focus.FaceChange("angry")
            if "no dildo" in Ch_Focus.RecentActions:
                call Sex_Basic_Dialog(Ch_Focus,"norecent")  # "What part of \"no,\" did you not get, [Ch_Focus.Petname]?"
            elif Taboo and "tabno" in Ch_Focus.DailyActions:
                call AnyLine(Ch_Focus,"Перестань размахивать этой штукой на людях!")
            elif "no dildo" in Ch_Focus.DailyActions:
                call Sex_Basic_Dialog(Ch_Focus,"nodaily")  #  "I already told you \"no,\" [Ch_Focus.Petname]."
            elif Target == "anal" and not Ch_Focus.Loose and "dildo anal" not in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("perplexed")
                call AnyLine(Ch_Focus,"В прошлый раз тебе следовало быть нежнее, "+Ch_Focus.Petname+". . .")
            else:
                $ Ch_Focus.FaceChange("bemused")
                if Ch_Focus is RogueX:
                        ch_r "Я совсем не люблю игрушки, [Ch_Focus.Petname]. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Я предпочитаю прямой контакт. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Они отнимают все удовольствие. . ."
                elif Ch_Focus is LauraX:
                        ch_l "За эти годы во мне побывало много вещей. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Я так устала от них. . ."
                elif Ch_Focus is StormX:
                        ch_s "Они все обезличивают. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Я бы предпочла прямой контакт. . ."
                elif Ch_Focus is GwenX:
                        ch_g "У меня дома полно фаллоимитаторов!"
                elif Ch_Focus is BetsyX:
                        ch_b "Я бы предпочла этого не делать. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я не. . . хочу. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Я не уверена, хочу ли я воспользоваться им сейчас. . ."

            menu:
                extend ""
                "Извини, забудь." if "no dildo" in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("bemused")
                    call AnyLine(Ch_Focus,"Ага, ладно, "+Ch_Focus.Petname+".")
                    return
                "Может, в другой раз?" if "no dildo" not in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("sexy")
                    call AnyLine(Ch_Focus,"Может быть, я буду практиковаться в свободное время, "+Ch_Focus.Petname+".")
                    $ Ch_Focus.Statup("Love", 80, 2)
                    $ Ch_Focus.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ Ch_Focus.RecentActions.append("tabno")
                        $ Ch_Focus.DailyActions.append("tabno")
                    $ Ch_Focus.RecentActions.append("no dildo")
                    $ Ch_Focus.DailyActions.append("no dildo")
                    return
                "Думаю, тебе понравится. . .":
                    if Approval:
                        $ Ch_Focus.FaceChange("sexy")
                        $ Ch_Focus.Statup("Obed", 90, 2)
                        $ Ch_Focus.Statup("Obed", 50, 2)
                        $ Ch_Focus.Statup("Inbt", 70, 3)
                        $ Ch_Focus.Statup("Inbt", 40, 2)
                        if not Player.Male:
                            $ Line = renpy.random.choice(["Конечно, вставляй.",
                                "Возможно. . .",
                                "Ты меня заинтересовала."])
                        else:
                            $ Line = renpy.random.choice(["Конечно, вставляй.",
                                "Возможно. . .",
                                "Ты меня заинтересовал."])
                        call AnyLine(Ch_Focus,Line)
                        $ Line = 0
                        jump Girl_Dildo_Prep
                    else:
                        pass

                "[[прижать его к ней]":                                               # Pressured into it
                    if Target == "anal":
                            $ Approval = ApprovalCheck(Ch_Focus, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    else:
                            $ Approval = ApprovalCheck(Ch_Focus, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and Ch_Focus.Forced):
                        $ Ch_Focus.FaceChange("sad")
                        $ Ch_Focus.Statup("Love", 70, -5, 1)
                        $ Ch_Focus.Statup("Love", 200, -5)
                        call AnyLine(Ch_Focus,"Хорошо. Если мы собираемся заняться этим, то вставьте уже его.")
                        $ Ch_Focus.Statup("Obed", 80, 4)
                        $ Ch_Focus.Statup("Inbt", 80, 1)
                        $ Ch_Focus.Statup("Inbt", 60, 3)
                        $ Ch_Focus.Forced = 1
                        jump Girl_Dildo_Prep
                    else:
                        $ Ch_Focus.Statup("Love", 200, -20)
                        $ Ch_Focus.RecentActions.append("angry")
                        $ Ch_Focus.DailyActions.append("angry")

    #She refused all offers.
    $ Ch_Focus.ArmPose = 1
    if "no dildo" in Ch_Focus.DailyActions:
            call AnyLine(Ch_Focus,"Учись принимать \"нет\" за ответ, "+Ch_Focus.Petname+".")
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("angry", 1)
            if not Player.Male:
                call AnyLine(Ch_Focus,"Я не хочу, чтобы ты использовала его на мне. . .")
            else:
                call AnyLine(Ch_Focus,"Я не хочу, чтобы ты использовал его на мне. . .")
            $ Ch_Focus.Statup("Lust", 200, 5)
            if Ch_Focus.Love > 300:
                    $ Ch_Focus.Statup("Love", 70, -2)
            $ Ch_Focus.Statup("Obed", 50, -2)
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ Ch_Focus.FaceChange("angry", 1)
            $ Ch_Focus.RecentActions.append("tabno")
            $ Ch_Focus.DailyActions.append("tabno")
            call Sex_Basic_Dialog(Ch_Focus,"tabno")  #  "not here"
            $ Ch_Focus.Statup("Lust", 200, 5)
            $ Ch_Focus.Statup("Obed", 50, -3)
    elif Target == "anal" and not Ch_Focus.Loose and "dildo anal" in Ch_Focus.DailyActions:
            $ Ch_Focus.FaceChange("bemused")
            call AnyLine(Ch_Focus,"Извини, мне нужно немного передохнуть, "+Ch_Focus.Petname+".")
    elif Ch_Focus.DildoP:
            $ Ch_Focus.FaceChange("sad")
            call AnyLine(Ch_Focus,"Извини, но тебе следует оставить свои игрушки при себе.")
    else:
            $ Ch_Focus.FaceChange("normal", 1)
            call AnyLine(Ch_Focus,"No way.")
    $ Ch_Focus.RecentActions.append("no dildo")
    $ Ch_Focus.DailyActions.append("no dildo")
    $ Tempmod = 0
    return

label Girl_Dildo_Prep: #rkeljsvg
    if "Target" not in locals().keys():
            $ Target = "pussy"
    elif Target not in ("anal","pussy"):
            $ Target = "pussy"
    if Trigger2 == "dildo pussy" or Trigger2 == "dildo anal":
        return
    if not Ch_Focus.Forced and Situation != "auto":
        $ Tempmod = 15 if Ch_Focus.PantsNum() > 6 else 0
        call Bottoms_Off(Ch_Focus)
        if "angry" in Ch_Focus.RecentActions:
            return
    $ Tempmod = 0
    if not Ch_Focus.Pose and Ch_Focus not in (1,2): #add new girls until they get doggy pose
            $ Ch_Focus.Pose = "doggy"
    if Target == "anal":
            call expression Ch_Focus.Tag + "_Sex_Launch" pass ("dildo anal")
            $ Trigger = "dildo anal"
    else:
            call expression Ch_Focus.Tag + "_Sex_Launch" pass ("dildo pussy")
            $ Trigger = "dildo pussy"
    if (Target == "anal" and not Ch_Focus.DildoA) or (Target != "anal" and not Ch_Focus.DildoP):
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -75)
            $ Ch_Focus.Statup("Obed", 70, 60)
            $ Ch_Focus.Statup("Inbt", 80, 35)
        else:
            $ Ch_Focus.Statup("Love", 90, 10)
            $ Ch_Focus.Statup("Obed", 70, 20)
            $ Ch_Focus.Statup("Inbt", 80, 45)
    if Taboo:
        $ Ch_Focus.Inbt += int(Taboo/10)
        $ Ch_Focus.Lust += int(Taboo/5)

    if Situation:
#        $ renpy.pop_call()
        $ Situation = 0

    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no dildo")
    if Target == "anal":
            $ Ch_Focus.RecentActions.append("dildo anal")
            $ Ch_Focus.DailyActions.append("dildo anal")
    else:
            $ Ch_Focus.RecentActions.append("dildo pussy")
            $ Ch_Focus.DailyActions.append("dildo pussy")
label Girl_Dildo_Cycle: #Repeating strokes
    $ Target = "pussy" if not Target else Target
    while Round > 0:
#        call Shift_Focus(Girl)
        call ViewShift(Ch_Focus,Ch_Focus.Pose,0)
        $ Ch_Focus.LustFace()
        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . .":
                                    pass

                        "Шлепнуть ее по заднице":
                                call Slap_Ass(Ch_Focus)
                                jump Girl_Dildo_Cycle

                        "Концентрироваться на продолжительности [[Не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0

                        "Сменить вид":
                                    call ViewShift(Ch_Focus,"menu")
                                    jump Girl_Dildo_Cycle

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
                                                        "Сказать, что хотите вставить свой член в ее попку.":
                                                                $ Situation = "shift"
                                                                call Girl_Dildo_After
                                                                call Girl_Sex_A # call expression Ch_Focus.Tag + "_Sex_A"
                                                        "Просто вставить свой член в ее попку без спроса.":
                                                                $ Situation = "auto"
                                                                call Girl_Dildo_After
                                                                call Girl_Sex_A # call expression Ch_Focus.Tag + "_Sex_A"

                                                        "Сказать, что хотите вставить свой член в ее киску.":
                                                                $ Situation = "shift"
                                                                call Girl_Dildo_After
                                                                call Girl_Sex_P # call expression Ch_Focus.Tag + "_Sex_P"
                                                        "Просто вставить свой член в ее киску без спроса.":
                                                                $ Situation = "auto"
                                                                call Girl_Dildo_After
                                                                call Girl_Sex_P # call expression Ch_Focus.Tag + "_Sex_P"

                                                        "Сказать, что хотите вставить фаллоимитатор ей в попку." if Target != "anal":
                                                                $ Situation = "shift"
                                                                call Girl_Dildo_After
                                                                call Girl_Dildo("anal")
                                                                if "no dildo" not in Ch_Focus.RecentActions: #if she refuses, continue on, otherwise, skip back to previous label
                                                                        return
                                                        "Сказать, что хотите вставить фаллоимитатор в ее киску." if Target != "pussy":
                                                                $ Situation = "shift"
                                                                call Girl_Dildo_After
                                                                call Girl_Dildo("pussy")
                                                                if "no dildo" not in Ch_Focus.RecentActions: #if she refuses, continue on, otherwise, skip back to previous label
                                                                        return

                                                        "Неважно":
                                                                jump Girl_Dildo_Cycle
                                            else:
                                                call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Переключить свое внимание" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Girl_Dildo_After
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
                                                        jump Girl_Dildo_Cycle
                                            "Привести в порядок [Partner.Name_vin] (locked)" if not Partner.Spunk:
                                                        pass
                                            "Привести в порядок [Partner.Name_vin]" if Partner.Spunk:
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_Dildo_Cycle
                                            "Неважно":
                                                        jump Girl_Dildo_Cycle
                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_Dildo_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus) #call expression Ch_Focus.Tag + "_Pos_Reset"
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_Dildo_After
                        "Закончить" if not MultiAction:
                                    ch_p "Нам стоит пока закончить."
                                    call Girl_Pos_Reset(Ch_Focus) #call expression Ch_Focus.Tag + "_Pos_Reset"
                                    $ Line = 0
                                    jump Girl_Dildo_After
        #End menu (if Line)

        if Ch_Focus.Panties or Ch_Focus.PantsNum() > 6 or Ch_Focus.HoseNum() >= 5: #This checks if Girl wants to strip down.
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
                                call Girl_Pos_Reset(Ch_Focus) #call expression Ch_Focus.Tag + "_Pos_Reset"
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_Dildo_After
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If Girl can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_Dildo_After

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
                                        jump Girl_Dildo_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.DildoP + Ch_Focus.DildoA):
                    $ Ch_Focus.Brows = "confused"
                    call AnyLine(Ch_Focus,"Are you ok back there?")
        elif Ch_Focus.Lust >= 80:
                    pass
        elif Cnt == (15 + Ch_Focus.DildoP + Ch_Focus.DildoA) and Ch_Focus.SEXP >= 15 and not ApprovalCheck(Ch_Focus, 1500):
                    $ Ch_Focus.Brows = "confused"
                    call AnyLine(Ch_Focus,Ch_Focus.Petname+", мне становится неприятно, может, попробуем что-нибудь другое?")
                    menu:
                        extend ""
                        "Закончить.":
                                "Вы заканчиваете. . ."
                                jump Girl_Dildo_After
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Girl_Dildo_After
                        "Не-а, это же так весело.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она ворчит, но позволяет вам продолжать."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call Girl_Pos_Reset(Ch_Focus) #call Girl_Pos_Reset(Girl) #call expression Ch_Focus.Tag + "_Pos_Reset"
                                    "Она кидает на вас сердитый взгляд и отстраняется."
                                    call AnyLine(Ch_Focus,"Ну, если ты так себя ведешь, мне не нужна твоя \"помощь.\"")
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_Dildo_After
        #End Count check

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10)  #  "You might want to wrap this up, it's getting late."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5)  #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done")  #"Ok, [Ch_Focus.Petname], that's enough of that for now."

label Girl_Dildo_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Girl_Pos_Reset(Ch_Focus) #call Girl_Pos_Reset(Girl) #call expression Ch_Focus.Tag + "_Pos_Reset"

    $ Ch_Focus.FaceChange("sexy")
    $ Ch_Focus.Action -=1
    call Partner_Like(Ch_Focus,2)

    if Target == "anal":
        $ Ch_Focus.DildoA += 1
        if Ch_Focus.DildoA == 1:
            $ Ch_Focus.SEXP += 10
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                    if Ch_Focus.Loose:
                        call AnyLine(Ch_Focus,"Ну, это было довольно весело. . .")
                    else:
                        call AnyLine(Ch_Focus,"Ну, было довольно грубо. . .")
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                    $ Ch_Focus.FaceChange("perplexed", 1)
                    if not Player.Male:
                        call AnyLine(Ch_Focus,"Ты довольна?")
                    else:
                        call AnyLine(Ch_Focus,"Ты доволен?")
    else:
        $ Ch_Focus.DildoP += 1
        if Ch_Focus.DildoP == 1:
            $ Ch_Focus.SEXP += 10
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                    call AnyLine(Ch_Focus,"Ну, это было довольно весело. . .")
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                    $ Ch_Focus.FaceChange("perplexed", 1)
                    if not Player.Male:
                        call AnyLine(Ch_Focus,"Ты довольна?")
                    else:
                        call AnyLine(Ch_Focus,"Ты доволен?")

    $ Tempmod = 0
    if Situation == "shift":
              call Sex_Basic_Dialog(Ch_Focus,"shift") # "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end Ch_Focus.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# Ch_Focus.SC //////////////////////////////////////////////////////////////////////

label Girl_SC: #rkeljsvgbdw
        #Scissoring between two girls
#        if Ch_Focus is WandaX:       #fix, remove           fix, remove           fix, remove           fix, remove
#            "This is not implemented yet."
#            return              #fix, remove           fix, remove           fix, remove           fix, remove
        $ Round -= 5 if Round > 5 else (Round-1)
#        call Shift_Focus(Girl)
        if Ch_Focus.SC >= 7: # She loves it
            $ Tempmod += 15
        elif Ch_Focus.SC >= 3: #You've done it before several times
            $ Tempmod += 10
        elif Ch_Focus.SC: #You've done it before
            $ Tempmod += 7
        elif Ch_Focus is DoreenX:
            $ Tempmod -= 5
        elif Ch_Focus is WandaX:
            $ Tempmod += 5

        if Ch_Focus.Addict >= 75 and Ch_Focus.Swallow >=3: #She's really strung out and has swallowed
            $ Tempmod += 25
        elif Ch_Focus.Addict >= 75: #She's really strung out
            $ Tempmod += 15

        if Situation == "shift":
            $ Tempmod += 15
        if "exhibitionist" in Ch_Focus.Traits:
            $ Tempmod += (4*Taboo)
        if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
            $ Tempmod += 10
        elif "ex" in Ch_Focus.Traits:
            $ Tempmod -= 40
        if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
            $ Tempmod -= 5 * Ch_Focus.ForcedCount

        if Taboo and "tabno" in Ch_Focus.DailyActions:
            $ Tempmod -= 10

        if "no scissor" in Ch_Focus.DailyActions:
            $ Tempmod -= 5
            $ Tempmod -= 10 if "no scissor" in Ch_Focus.RecentActions else 0

        $ Approval = ApprovalCheck(Ch_Focus, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

        if not Ch_Focus.SC and "no scissor" not in Ch_Focus.RecentActions:
            #first time question
            $ Ch_Focus.FaceChange("surprised", 1)
            $ Ch_Focus.Mouth = "kiss"
            if Ch_Focus is RogueX:
                    ch_r "Ты хочешь, чтобы мы потерлись кисками?"
            elif Ch_Focus is KittyX:
                    ch_k "Хочешь устроить ножницы?"
            elif Ch_Focus is EmmaX:
                    ch_e "Боже, ты хочешь отполировать наших моллюсков?"
            elif Ch_Focus is LauraX:
                    ch_l "Ножницы, значит?"
            elif Ch_Focus is JeanX:
                    ch_j "Ножницы?"
            elif Ch_Focus is StormX:
                    ch_s "Ты желаешь устроить ножницы со мной?"
            elif Ch_Focus is JubesX:
                    ch_v "Ты хочешь ножницы?"
            elif Ch_Focus is GwenX:
                    ch_g "Хм, ножницы, значит. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Желаешь, чтобы тебе все там отполировали?"
            elif Ch_Focus is DoreenX:
                    ch_d "Ох, ты хочешь [[изображает каждой рукой ножницы и насаживает их друг на друга]?"
            elif Ch_Focus is WandaX:
                    ch_w "Желаешь ножницы?"
            if Ch_Focus.Finger:
                if Ch_Focus is DoreenX:
                        $ Ch_Focus.Mouth = "smile"
                        ch_d "Может, я лучше. . . поиграю с тобой пальчиками?"

        call expression Ch_Focus.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
        if "nogirls" in Ch_Focus.History and not Ch_Focus.Forced:
                #if she isn't into girls but isn't coerced. . .
                return

        if not Ch_Focus.SC and Approval:
            #First time dialog
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Love", 70, -3, 1)
                $ Ch_Focus.Statup("Love", 20, -2, 1)
            elif Ch_Focus.Love >= (Ch_Focus.Obed + Ch_Focus.Inbt):
                $ Ch_Focus.FaceChange("sexy")
                $ Ch_Focus.Brows = "sad"
                $ Ch_Focus.Mouth = "smile"
            elif Ch_Focus.Obed >= Ch_Focus.Inbt:
                $ Ch_Focus.FaceChange("normal")
            elif Ch_Focus.Addict >= 50:
                $ Ch_Focus.FaceChange("manic", 1)
            else:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Mouth = "smile"

            if Ch_Focus.Love >= 700:
                if Ch_Focus is RogueX:
                        ch_r "Я никогда не пробовала этого раньше. . . это может быть интересно."
                elif Ch_Focus is KittyX:
                        ch_k "Мне довольно интересно, на что это. . . похоже."
                elif Ch_Focus is EmmaX:
                        ch_e "Это может быть довольно весело. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Это может быть весело."
                elif Ch_Focus is JeanX:
                        ch_j "Возможно. это даже весело. . ."
                elif Ch_Focus is StormX:
                        ch_s "Мне даже немного любопытно. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Это может быть довольно весело. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Это может быть весело. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Это может быть интересно. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я. . . думаю, что это может быть. . . интересно. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Это может быть весело. . ."
            else: # Uninhibited
                if Ch_Focus is RogueX:
                        ch_r "Наверное, можно. . ."
                elif Ch_Focus is KittyX:
                        ch_k "[KittyX.Like]конечно. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Пожалуй, можно. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Хм. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Хм. . ."
                elif Ch_Focus is StormX:
                        ch_s "Пожалуй, можно. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Ладно, погнали. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Звучит весело. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Пожалуй, можно. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Наверное, можно. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Это может быть весело. . ."


        elif Approval:
            #Second time+ dialog
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Love", 70, -3, 1)
                $ Ch_Focus.Statup("Love", 20, -2, 1)
                if Ch_Focus is RogueX:
                        ch_r "И все? . ."
                elif Ch_Focus is KittyX:
                        ch_k "И не. . . более. . ?"
                elif Ch_Focus is EmmaX:
                        ch_e "Это немного скучноват. . ."
                elif Ch_Focus is LauraX:
                        ch_l ". . ."
                elif Ch_Focus is JeanX:
                        ch_j "Фи."
                elif Ch_Focus is StormX:
                        ch_s "Нам может этого не хватить. . ."
                elif Ch_Focus is JubesX:
                        ch_v ". . . И все?"
                elif Ch_Focus is GwenX:
                        ch_g "Нууу. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "И это все, чего ты желаешь?"
                elif Ch_Focus is DoreenX:
                        ch_d "Ты просишь только это?"
                elif Ch_Focus is WandaX:
                        ch_w "И все?"
            elif "scissor" in Ch_Focus.RecentActions:
                $ Ch_Focus.FaceChange("sexy", 1)
                jump Girl_SC_Prep
            elif "scissor" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Так скоро вернулась за добавкой?",
                    "Ты хочешь, чтобы у меня там появились мозоли?",
                    "Я уже намокла.",
                    "Тебе не хватило в прошлый раз?",
                    "После прошлого раза она у меня все еще немного побаливает.",
                    "После прошлого раза она у меня все еще немного побаливает."])
                call AnyLine(Ch_Focus,Line)
            else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Хочешь [изображает каждой рукой ножницы и насаживает их друг на друга]?",
                    "Значит, ты хочешь, устроить ножницы со мной?",
                    "Значит. . . ножницы?",
                    "Хочешь снова потереться о мою киску?",
                    "Снова ножницы?"])
                call AnyLine(Ch_Focus,Line)
            $ Line = 0


        if Approval >= 2:
            #She's into it. . .
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Obed", 90, 1)
                $ Ch_Focus.Statup("Inbt", 60, 1)
                if Ch_Focus is RogueX:
                        ch_r "Как скажешь."
                elif Ch_Focus is KittyX:
                        ch_k "Как скажешь."
                elif Ch_Focus is EmmaX:
                        ch_e "Хорошо."
                elif Ch_Focus is LauraX:
                        ch_l "Как скажешь."
                elif Ch_Focus is JeanX:
                        ch_j "Хорошо, давай поскорее с этим покончим."
                elif Ch_Focus is StormX:
                        ch_s "Хорошо."
                elif Ch_Focus is JubesX:
                        ch_v "Ладно, я в деле."
                elif Ch_Focus is GwenX:
                        ch_g "Конечно. . . наверное. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Если это так необходимо. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Ладно. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Конечно."
            else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Statup("Love", 90, 1)
                $ Ch_Focus.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Что ж, хорошо.",
                    "Ну. . . ладно.",
                    "Без проблем.",
                    "Конечно, снимай штаны.",
                    "Ладно. . .",
                    "Хех, хорошо."])
                call AnyLine(Ch_Focus,Line)
                $ Line = 0
            $ Ch_Focus.Statup("Obed", 20, 1)
            $ Ch_Focus.Statup("Obed", 70, 1)
            $ Ch_Focus.Statup("Inbt", 80, 2)
            jump Girl_SC_Prep

        else:
            #She's not into it, but maybe. . .
            $ Ch_Focus.FaceChange("angry")
            if "no scissor" in Ch_Focus.DailyActions:
                call AnyLine(Ch_Focus,"Я уже сказала тебе \"нет,\" "+Ch_Focus.Petname+".")
            elif Taboo and "tabno" in Ch_Focus.DailyActions:
                call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
            else:
                $ Ch_Focus.FaceChange("bemused")
                if Ch_Focus is RogueX:
                        ch_r "Может, не сейчас? . ."
                elif Ch_Focus is KittyX:
                        ch_k "Я даже не знаю. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Я так не думаю. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Нет."
                elif Ch_Focus is JeanX:
                        ch_j "Не-а."
                elif Ch_Focus is StormX:
                        ch_s "Я так не думаю. . ."
                elif Ch_Focus is JubesX:
                        ch_v ". . . нет?"
                elif Ch_Focus is GwenX:
                        ch_g "Знаешь, что-то я не уверена. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Боюсь, что нет. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Может. . . нет?"
                elif Ch_Focus is WandaX:
                        ch_w "Я не уверена."
            menu:
                extend ""
                "Извини, забудь." if "no scissor" in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("bemused")
                    if Ch_Focus is RogueX:
                            ch_r "Ага, ладно, [Ch_Focus.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Оу, ладно, [KittyX.Petname]."
                    elif Ch_Focus is EmmaX:
                            ch_e "Ничего страшного, [EmmaX.Petname]."
                    elif Ch_Focus is LauraX:
                            ch_l "Клево."
                    elif Ch_Focus is JeanX:
                            ch_j "Ну ладно."
                    elif Ch_Focus is StormX:
                            ch_s "Все нормально, [StormX.Petname]."
                    elif Ch_Focus is JubesX:
                            $ JubesX.FaceChange("sad")
                            ch_v "Ладно. . ."
                            ch_v "Может, когда-нибудь потом. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Спасибо, все нормально. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Я это ценю."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ох, все нормально."
                    elif Ch_Focus is WandaX:
                            ch_w "Конечно, все нормально"
                    return
                "Может, в другой раз?" if "no scissor" not in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("sexy")
                    if Ch_Focus is RogueX:
                            ch_r "Ага, все может быть, [Ch_Focus.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Может быть, невозможно знать все наперед."
                    elif Ch_Focus is EmmaX:
                            ch_e "Я бы не стала этого исключать, [EmmaX.Petname]."
                    elif Ch_Focus is LauraX:
                            ch_l "Ага, может быть."
                    elif Ch_Focus is JeanX:
                            ch_j "Конечно, [JeanX.Petname]."
                    elif Ch_Focus is StormX:
                            ch_s "Я не могу этого исключать, [StormX.Petname]."
                    elif Ch_Focus is JubesX:
                            ch_v "Ага, конечно!"
                    elif Ch_Focus is GwenX:
                            ch_g "Ага, может быть. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Возможно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ну. . . наверное. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Хех, возможно, ага."
                    $ Ch_Focus.Statup("Love", 80, 2)
                    $ Ch_Focus.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ Ch_Focus.RecentActions.append("tabno")
                        $ Ch_Focus.DailyActions.append("tabno")
                    $ Ch_Focus.RecentActions.append("no scissor")
                    $ Ch_Focus.DailyActions.append("no scissor")
                    return
                "Тебе может понравится. . .":
                        if Approval:
                            $ Ch_Focus.FaceChange("sexy")
                            $ Ch_Focus.Statup("Obed", 90, 2)
                            $ Ch_Focus.Statup("Obed", 50, 2)
                            $ Ch_Focus.Statup("Inbt", 70, 3)
                            $ Ch_Focus.Statup("Inbt", 40, 2)
                            $ Line = renpy.random.choice(["Ага, возможно. . .",
                                "Все может быть. . .",
                                "Возможно, давай проверим.",
                                ". . . хорошее замечание. . ."])
                            call AnyLine(Ch_Focus,Line)
                            $ Line = 0
                            jump Girl_SC_Prep


                "Просто смрись.":
                    # Pressured into it
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    $ Approval = ApprovalCheck(Ch_Focus, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                    if Approval > 1 or (Approval and Ch_Focus.Forced):
                        $ Ch_Focus.FaceChange("sad")
                        $ Ch_Focus.Statup("Love", 70, -5, 1)
                        $ Ch_Focus.Statup("Love", 200, -2)
                        if Ch_Focus is RogueX:
                                ch_r "Ладно, снимай штаны."
                        elif Ch_Focus is KittyX:
                                ch_k "Ладно. . ."
                        elif Ch_Focus is EmmaX:
                                ch_e "Хорошо. . ."
                        elif Ch_Focus is LauraX:
                                ch_l "Как скажешь. . ."
                        elif Ch_Focus is JeanX:
                                $ JeanX.FaceChange("angry",2)
                                ch_j ". . ."
                                $ JeanX.FaceChange("angry",1,Eyes="side")
                                ch_j "Как скажешь. . ."
                        elif Ch_Focus is StormX:
                                ch_s ". . . хорошо. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Ладно. . . хорошо. . ."
                        elif Ch_Focus is GwenX:
                                ch_g ". . . ладно. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Что ж. . . тогда давай сразу перейдем к делу. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d ". . . ладно. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Ладно, как скажешь."
                        $ Ch_Focus.Statup("Obed", 50, 4)
                        $ Ch_Focus.Statup("Inbt", 80, 1)
                        $ Ch_Focus.Statup("Inbt", 60, 3)
                        $ Ch_Focus.Forced = 1
                        jump Girl_SC_Prep
                    else:
                        $ Ch_Focus.Statup("Love", 200, -15)
                        $ Ch_Focus.RecentActions.append("angry")
                        $ Ch_Focus.DailyActions.append("angry")

        #She refused all offers.
        if "no scissor" in Ch_Focus.DailyActions:
            $ Ch_Focus.FaceChange("angry", 1)
            if Ch_Focus is RogueX:
                    ch_r "Ни за что."
            elif Ch_Focus is KittyX:
                    ch_k "Я не буду ласкать твою киску. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Тогда, надеюсь, ты сможешь сама о себе позаботиться."
            elif Ch_Focus is LauraX:
                    $ LauraX.ArmPose = 2
                    $ LauraX.Claws = 1
                    ch_l "Нвхуй ножницы."
                    $ LauraX.ArmPose = 1
                    $ LauraX.Claws = 0
            elif Ch_Focus is JeanX:
                    ch_j "Ни за что. . ."
            elif Ch_Focus is StormX:
                    ch_s "Тогда, надеюсь, ты сможешь сама о себе позаботиться."
            elif Ch_Focus is JubesX:
                    ch_v "Мне это не интересно."
            elif Ch_Focus is GwenX:
                    ch_g "Ни за что. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Я ясно выразилась на этот счет."
            elif Ch_Focus is DoreenX:
                    ch_d "Да ни за что!"
            elif Ch_Focus is WandaX:
                    ch_w "Не сейчас."
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
        elif Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("angry", 1)
            if Ch_Focus is RogueX:
                    ch_r "Это не то, чего бы я хотела!"
            elif Ch_Focus is KittyX:
                    ch_k "Сегодня мне этого совсем не хочется. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Ты забегаешь далеко вперед!"
            elif Ch_Focus is LauraX:
                    ch_l "Не заставляй меня."
            elif Ch_Focus is JeanX:
                    ch_j "Я на это не пойду."
            elif Ch_Focus is StormX:
                    ch_s "Ты забегаешь вперед!"
            elif Ch_Focus is JubesX:
                    $ Ch_Focus.FaceChange("sad", 1)
                    ch_v "Жаль, но я не могу. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Извини. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Думаю, для меня это слишком. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Ни за что!"
            elif Ch_Focus is WandaX:
                    ch_w "Забудь об этом."
            $ Ch_Focus.Statup("Lust", 200, 5)
            if Ch_Focus.Love > 300:
                    $ Ch_Focus.Statup("Love", 70, -2)
            $ Ch_Focus.Statup("Obed", 50, -2)
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
            $ Ch_Focus.RecentActions.append("no scissor")
            $ Ch_Focus.DailyActions.append("no scissor")
            return
        elif Taboo:                             # she refuses and this is too public a place for her
            $ Ch_Focus.FaceChange("angry", 1)
            $ Ch_Focus.DailyActions.append("tabno")
            call Sex_Basic_Dialog(Ch_Focus,"tabno")
            $ Ch_Focus.Statup("Lust", 200, 5)
            $ Ch_Focus.Statup("Obed", 50, -3)
            return
        elif Ch_Focus.SC:
            $ Ch_Focus.FaceChange("sad")
            if Ch_Focus is RogueX:
                    ch_r "Мне это не интересно, спасибо."
            elif Ch_Focus is KittyX:
                    ch_k "Нет, не в этот раз."
            elif Ch_Focus is EmmaX:
                    ch_e "Я так не думаю."
            elif Ch_Focus is LauraX:
                    ch_l "Нет."
            elif Ch_Focus is JeanX:
                    ch_j "Не-а, не в этот раз."
            elif Ch_Focus is StormX:
                    ch_s "Я не в настроении, [StormX.Petname]."
            elif Ch_Focus is JubesX:
                    ch_v "Эм, нет. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Я не хочу этого снова. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Не сейчас, [BetsyX.Petname]."
            elif Ch_Focus is DoreenX:
                    ch_d "Я так не думаю. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Не сейчас."
        else:
            $ Ch_Focus.FaceChange("normal", 1)
            if Ch_Focus is RogueX:
                    ch_r "Мне это не интересно."
            elif Ch_Focus is KittyX:
                    ch_k "Не-а."
            elif Ch_Focus is EmmaX:
                    ch_e "Боюсь, я вынуждена отказаться. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Нет."
            elif Ch_Focus is JeanX:
                    ch_j "Ха! Хорошая попытка."
            elif Ch_Focus is StormX:
                    ch_s "Не думаю, что я на это пойду."
            elif Ch_Focus is JubesX:
                    ch_v "Не-а."
            elif Ch_Focus is GwenX:
                    ch_g "Это немного. . . в общем, нет. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Боюсь, я откажусь, благодарю."
            elif Ch_Focus is DoreenX:
                    ch_d "Ох, нет, спасибо. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Нет, мне и без этого хорошо."
        $ Ch_Focus.RecentActions.append("no scissor")
        $ Ch_Focus.DailyActions.append("no scissor")
        $ Tempmod = 0
        return




label Girl_SC_Prep:    #rkeljsvgbdw
#        if Girl == WandaX:       #fix, remove           fix, remove           fix, remove           fix, remove
#            "This is not implemented yet."
#            return              #fix, remove           fix, remove           fix, remove           fix, remove
#        call Shift_Focus(Girl)
        if Taboo:
            $ Ch_Focus.Inbt += int(Taboo/10)
            $ Ch_Focus.Lust += int(Taboo/5)

        $ Ch_Focus.FaceChange("sexy")
        if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad")
        elif not Ch_Focus.SC:
            $ Ch_Focus.Brows = "confused"
            $ Ch_Focus.Eyes = "sexy"
            $ Ch_Focus.Mouth = "smile"

        call Seen_First_Peen(Ch_Focus,Partner,React=Situation)
        call expression Ch_Focus.Tag + "_SC_Launch" pass ("L")

        if Situation == Ch_Focus:
                #Girl auto-starts
                $ Situation = 0
                "[Ch_Focus.Name] откидывается назад и притягивает вас к себе, прижимаясь к вашей киске."
                menu:
                    "Что будете делать?"
                    "Отдаться моменту.":
                        $ Ch_Focus.Statup("Inbt", 80, 3)
                        $ Ch_Focus.Statup("Inbt", 50, 2)
                        "[Ch_Focus.Name] начинает тереться о вас."
                    "Похвалить ее.":
                        $ Ch_Focus.FaceChange("sexy", 1)
                        $ Ch_Focus.Statup("Inbt", 80, 3)
                        ch_p "О да, [Ch_Focus.Pet], давай сделаем это."
                        $ Ch_Focus.NameCheck() #checks reaction to petname
                        "[Ch_Focus.Name] начинает тереться о вас."
                        $ Ch_Focus.Statup("Love", 85, 1)
                        $ Ch_Focus.Statup("Obed", 90, 1)
                        $ Ch_Focus.Statup("Obed", 50, 2)
                    "Сказать ей остановиться.":
                        $ Ch_Focus.FaceChange("surprised")
                        $ Ch_Focus.Statup("Inbt", 70, 1)
                        ch_p "[Ch_Focus.Pet], давай не будем сейчас этим заниматься."
                        $ Ch_Focus.NameCheck() #checks reaction to petname
                        "[Ch_Focus.Name] отстраняется."
                        $ Ch_Focus.Statup("Obed", 90, 1)
                        $ Ch_Focus.Statup("Obed", 50, 1)
                        $ Ch_Focus.Statup("Obed", 30, 2)
                        $ Player.RecentActions.append("nope")
                        $ Ch_Focus.AddWord(1,"refused","refused")
                        return
        elif Situation != "auto":
    #        call Bottoms_Off(Ch_Focus)
            "[Ch_Focus.Name] медленно прижимается к вашей промежности."

        else: #if Situation == "auto"
            "Она укладывает вас на спину, притягивая к своей киске."

        if not Ch_Focus.Hotdog:                                                      #First time stat buffs
            if Ch_Focus.Forced:
                $ Ch_Focus.Statup("Love", 90, -5)
                $ Ch_Focus.Statup("Obed", 70, 20)
                $ Ch_Focus.Statup("Inbt", 80, 10)
            else:
                $ Ch_Focus.Statup("Love", 90, 20)
                $ Ch_Focus.Statup("Obed", 70, 20)
                $ Ch_Focus.Statup("Inbt", 80, 20)

        if Situation:
            $ renpy.pop_call()
            $ Situation = 0
        $ Line = 0
        $ Cnt = 0
        $ Trigger = "scissor"
        $ Speed = 1
        if Taboo:
            $ Ch_Focus.DrainWord("tabno")
        $ Ch_Focus.DrainWord("no scissor")
        $ Ch_Focus.RecentActions.append("scissor")
        $ Ch_Focus.DailyActions.append("scissor")

label Girl_SC_Cycle: #rkeljsvgbdw
        while Round > 0:
#            call Shift_Focus(Girl)
            call expression Ch_Focus.Tag + "_SC_Launch"
            $ Trigger = "scissor"
            $ Ch_Focus.LustFace()

            if  Player.Focus < 100:
                        if "setpace" in Ch_Focus.DailyActions:
                                $ D20 = renpy.random.randint(1, 20)
                                if Ch_Focus.SC < 5:
                                    $ D20 -= 10
                                elif Ch_Focus.SC < 10:
                                    $ D20 -= 5
                                if D20 > 10:
                                    $ Speed = 3
                                elif D20 > 5:
                                    $ Speed = 2
                                else:
                                    $ Speed = 1
                        #Player Command menu
                        menu:
                            "Продолжать. . ." if Speed:
                                    pass
                            "Продолжать. . . (locked)" if not Speed:
                                        pass

                            "Начать? . ." if not Speed:
                                        $ Speed = 1
    #                                    call Speed_Shift(1)
                            "Быстрее. . ." if 0 < Speed < 2:
                                        $ Speed += 1
    #                                    call Speed_Shift(Speed+1)
                                        "Вы немного ускоряете свои движения."
                            "Быстрее. . . (locked)" if Speed >= 2:
                                        pass

                            "Помедленнее. . ." if Speed:
                                        $ Speed -= 1
    #                                    call Speed_Shift(Speed-1)
                                        "Вы немного замедляете свои движения."
                            "Помедленнее. . . (locked)" if not Speed:
                                        pass

                            "Концентрироваться на продолжительности [[Не открыто] (locked)" if "focus" not in Player.Traits:
                                        pass
                            "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                        "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                        $ Player.FocusX = 1
                            "Прекратить концентрироваться." if Player.FocusX:
                                        "Вы расслабляетесь. . ."
                                        $ Player.FocusX = 0

                            "Другие варианты":
                                    menu:
                                        "Дополнительное действие" if Ch_Focus.Loc == bg_current and Ch_Focus.Pose == "69":
                                                if Ch_Focus.Action and MultiAction:
                                                    call Offhand_Set
                                                    if Trigger2:
                                                        $ Ch_Focus.Action -= 1
                                                else:
                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")

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
                                                            "Может, поласкаешь мою киску пальчиками?":
                                                                    if Ch_Focus.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Girl_SC_After
                                                                        call Girl_Finger
                                                                    else:
                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")
#                                                            "How about a titjob?":
#                                                                    if Ch_Focus.Action and MultiAction:
#                                                                        $ Situation = "shift"
#                                                                        call Girl_SC_After
#                                                                        call Girl_Titjob
#                                                                    else:
#                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                            "Неважно":
                                                                    jump Girl_SC_Cycle
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
                                                            jump Girl_SC_Cycle
                                                "Привести в порядок [Partner.Name_vin] (locked)" if not Partner.Spunk:
                                                            pass
                                                "Привести в порядок [Partner.Name_vin]" if Partner.Spunk:
                                                            call Girl_Cleanup(Partner,"ask")
                                                            jump Girl_SC_Cycle
                                                "Неважно":
                                                            jump Girl_SC_Cycle
                                        "Раздеть [Ch_Focus.Name_vin]":
                                                call Girl_Undress(Ch_Focus)
                                        "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                                pass
                                        "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                                call Girl_Cleanup(Ch_Focus,"ask")
                                        "Неважно":
                                                jump Girl_SC_Cycle

                            "Вернуться к Секс-меню" if MultiAction:
                                        ch_p "Нам стоит попробовать что-нибудь другое."
                                        call expression Ch_Focus.Tag + "_SC_Reset"
                                        $ Situation = "shift"
                                        $ Line = 0
                                        jump Girl_SC_After
                            "Закончить" if not MultiAction:
                                        ch_p "Нам стоит пока закончить."
                                        call expression Ch_Focus.Tag + "_SC_Reset"
                                        $ Line = 0
                                        jump Girl_SC_After
            #End menu (if Line)

#            call Shift_Focus(Girl)
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
                                    call expression Ch_Focus.Tag + "_SC_Reset"
                                    return
                                $ Ch_Focus.Statup("Lust", 200, 5)
                                if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2 and Ch_Focus.SEXP >= 20:
                                    $ Ch_Focus.RecentActions.append("unsatisfied")
                                    $ Ch_Focus.DailyActions.append("unsatisfied")
                                if Player.Focus > 80:
                                    jump Girl_SC_After
                                $ Line = "came"

                        if Ch_Focus.Lust >= 100:
                                #If Girl can cum
                                call Girl_Cumming(Ch_Focus)
                                if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                    jump Girl_SC_After

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
                                            jump Girl_SC_After
            if Partner and Partner.Lust >= 100:
                    #Checks if partner could orgasm
                    call Girl_Cumming(Partner)
            #End orgasm

            $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

            if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
                pass
            elif Cnt == (5 + Ch_Focus.SC):
                        $ Ch_Focus.Brows = "confused"
                        call AnyLine(Ch_Focus,"Ты скоро? Я немного устала.")
            elif Cnt == (10 + Ch_Focus.SC):
                        $ Ch_Focus.Brows = "angry"
                        call AnyLine(Ch_Focus,"Может, займемся чем-нибудь другим?")
                        menu:
                            extend ""
                            "Продолжим (locked)":
                                    pass
                            "Может поласкаешь мою киску пальчиками?" if Ch_Focus.Action and MultiAction:
                                    $ Situation = "shift"
                                    call Girl_SC_After
                                    call Girl_Finger
                                    return
                            "Может поласкаешь мою киску пальчиками? (locked)" if not Ch_Focus.Action or not MultiAction:
                                    pass
                            "Закончить." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0
                                    $ Player.Focus += 15
                                    jump Girl_SC_Cycle
                            "Закончить. (locked)" if not Player.FocusX:
                                    pass
                            "Давай попробуем что-нибудь другое." if MultiAction:
                                    $ Line = 0
                                    call expression Ch_Focus.Tag + "_SC_Reset"
                                    $ Situation = "shift"
                                    jump Girl_SC_After
                            "Давай попробуем что-нибудь другое. (locked)" if not MultiAction:
                                    pass
                            "Нет, давай за работу.":
                                    if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                        $ Ch_Focus.Statup("Love", 200, -5)
                                        $ Ch_Focus.Statup("Obed", 50, 3)
                                        $ Ch_Focus.Statup("Obed", 80, 2)
                                        "Она ворчит, но возвращается к работе."
                                    else:
                                        $ Ch_Focus.FaceChange("angry", 1)
                                        "Она кидает на вас сердитый взгляд и отстраняется."
                                        call AnyLine(Ch_Focus,"Я так не думаю.")
                                        $ Ch_Focus.Statup("Love", 50, -3, 1)
                                        $ Ch_Focus.Statup("Love", 80, -4, 1)
                                        $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                        $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                        $ Ch_Focus.RecentActions.append("angry")
                                        $ Ch_Focus.DailyActions.append("angry")
                                        jump Girl_SC_After
            #End Count check

            call Escalation(Ch_Focus) #sees if she wants to escalate things

            if Round == 10:
                    call Sex_Basic_Dialog(Ch_Focus,10) #"It is getting late, [Ch_Focus.Petname]. . ."
            elif Round == 5:
                    call Sex_Basic_Dialog(Ch_Focus,5)   #"We should take a break soon."

        #Round = 0 loop breaks
        $ Ch_Focus.FaceChange("bemused", 0)
        $ Line = 0
        call Sex_Basic_Dialog(Ch_Focus,"done") # ch_s "I need to take a moment to collect myself."

label Girl_SC_After:   #rkeljsvgbdw
        $ Ch_Focus.FaceChange("sexy")
        $ Ch_Focus.SC += 1
        $ Ch_Focus.Action -=1
        $ Ch_Focus.Addictionrate += 1
        if "addictive" in Player.Traits:
            $ Ch_Focus.Addictionrate += 1

        call Partner_Like(Ch_Focus,2)

        if Ch_Focus.SC == 10:
            $ Ch_Focus.SEXP += 5
        elif Ch_Focus.SC == 1:
            $ Ch_Focus.SEXP += 10
            if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                    if Ch_Focus is RogueX:
                            ch_r "Это было круто, [RogueX.Petname], нам нужно как-нибудь повторить."
                    elif Ch_Focus is KittyX:
                            ch_k "Мне. . . очень понравилось."
                    elif Ch_Focus is EmmaX:
                            ch_e "Это было. . . приятно."
                    elif Ch_Focus is LauraX:
                            ch_l "Это было. . . хорошо."
                    elif Ch_Focus is JeanX:
                            ch_j "Все прошло. . . нормально."
                    elif Ch_Focus is StormX:
                            ch_s "Я насладилась. . . моментов."
                    elif Ch_Focus is JubesX:
                            ch_v "Это было. . . весело."
                    elif Ch_Focus is GwenX:
                            ch_g "Это было. . . клево."
                    elif Ch_Focus is BetsyX:
                            ch_b "Это было. . . довольно приятно."
                    elif Ch_Focus is DoreenX:
                            ch_d "Это было. . . клево."
                    elif Ch_Focus is WandaX:
                            ch_w "Это было довольно весело."
            elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                    $ Ch_Focus.Mouth = "sad"
                    if Ch_Focus is RogueX:
                            ch_r "Ты получила то, что тебе было нужно?"
                    elif Ch_Focus is KittyX:
                            ch_k "Тебя все устроило?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Тебе этого хватило?"
                    elif Ch_Focus is LauraX:
                            ch_l "Тебе хватило?"
                    elif Ch_Focus is JeanX:
                            ch_j "Думаю, что могло бы быть и хуже. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Ты удовлетворена?"
                    elif Ch_Focus is JubesX:
                            ch_v "Тебе понравилось?"
                    elif Ch_Focus is GwenX:
                            ch_g "Тебе теперь лучше?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Ты удовлетворена?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Я все правильно делала?"
                    elif Ch_Focus is WandaX:
                            ch_w "Ну как?"
            if "unsatisfied" in Ch_Focus.RecentActions:
                    $ Ch_Focus.FaceChange("angry")
                    $ Ch_Focus.Eyes = "side"
                    if Ch_Focus is RogueX:
                            ch_r "Мне не очень понравилось. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Ты не могла уделить мне больше внимания? . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Не могла бы ты быть повнимательнее? . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Ты ничего не забыла? . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Думаю, тебе стоит закончить начатое."
                    elif Ch_Focus is StormX:
                            ch_s "Тебе не помешало бы уделять больше внимания моим потребностям. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Знаешь, ты могла бы подумать и обо мне. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Эй! Разве ты не собираешься закончить со мной?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Тебе не кажется, что тебе нужно кое-что закончить?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Эм, знаешь. . . я не совсем. . ."
                            ch_d "\"Закончила.\""
                    elif Ch_Focus is WandaX:
                            ch_w "Послушай, тебе не помешало бы уделять мне больше внимания."
        $ Tempmod = 0
        if Situation != "shift":
            call expression Ch_Focus.Tag + "_SC_Reset"
        call Checkout
        return

return

# end Ch_Focus.SC                                 //////////////////////////////////////////////////////////////////////////////

# Start Girl CUN Offhand Speed Menu  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_CUN_Menu:
       menu:
            "Продолжать. . ." if Speed:
                        pass

            "Облизывай ее. . ." if Speed != 1:
                    $ Speed = 1
                    $ Ch_Focus.DrainWord("setpace",1,0,0,0)
            "Облизывай ее. . . (locked)" if Speed == 1:
                    pass

            "Возьми в рот клитор. . ." if Speed != 2:
                    $ Speed = 2
                    $ Ch_Focus.DrainWord("setpace",1,0,0,0)
            "Возьми в рот клитор. . . (locked)" if Speed == 2:
                    pass

            "Пососи ее." if Speed != 3:
                    $ Speed = 3
                    $ Ch_Focus.DrainWord("setpace",1,0,0,0)
                    if Trigger2 == "jilling":
                        "Она опускает голову чуть ниже и вы убираете свою руку."
            "Пососи ее. (locked)" if Speed == 3:
                    pass

            "Делай, что тебе больше хочется. . .":
                    "[Ch_Focus.Name] издает звук согласия."
                    if "setpace" not in Ch_Focus.DailyActions:
                            $ Ch_Focus.Statup("Love", 80, 2)
                    $ D20 = renpy.random.randint(1, 20)
                    if Ch_Focus.CUN < 5:
                        $ D20 -= 10
                    elif Ch_Focus.CUN < 10:
                        $ D20 -= 5
                    if D20 > 10:
                        $ Speed = 3
                    elif D20 > 5:
                        $ Speed = 2
                    else:
                        $ Speed = 1
                    $ Ch_Focus.AddWord(1,"setpace","setpace")
            "Неважно. . .":
                    pass
       return
# End Girl CUN Offhand Speed Menu  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
