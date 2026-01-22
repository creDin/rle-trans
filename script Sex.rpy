# Start Jackin it check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jackin(Girl=0,Cnt=0,BO=[]): #rkeljsvgbdw
        #Called when you try to jack it from inside a sex action
        #should include a girl's name, if not, one is randomly picked from the room.
        if not Player.Male:
                jump Jilling
        if not Girl or Girl not in TotalGirls:
            if Ch_Focus.Loc == bg_current:
                $ Girl = Ch_Focus
            else:
                $ BO = TotalGirls[:]
                python:
                    for BX in BO:
                        if BX.Loc == bg_current:
                                Girl = BX
                                break

        if not Girl or "unseen" in Girl.RecentActions:
                $ Player.RecentActions.append("cockout")
                $ Trigger2 = "jackin"
                "Вы достаете свой член и начинаете мастурбировать."
        else:
                if not Player.Semen:
                        "Вы не думаете, что это поможет, бедняжка спит."
                        return

                if "cockout" in Player.RecentActions:
                        "Вы начинаете мастурбировать."
                else:
                        "Вы достаете свой член и начинаете мастурбировать."
                        $ Player.RecentActions.append("cockout")
                        call Seen_First_Peen(Girl,Partner)

                $ Trigger2 = "jackin"
                if "jackin" in Girl.RecentActions:
                    return
                $ Girl.AddWord(0,"jackin","jackin",0,0)

                if Girl is EmmaX and "classcaught" not in Girl.History:
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Eyes = "down"
                        ch_e "Подожди. . ."
                        $ Girl.FaceChange("angry", 1)
                        ch_e "Это ужасно неуместно."
                        $ Girl.Statup("Lust", 50, 7)
                        if not ApprovalCheck(EmmaX, 1200, TabM = 3):
                                $ Girl.AddWord(0,"angry","angry",0,0)
                                $ renpy.pop_call()
                                return

                if Girl.SEXP < 10 and Girl not in (JeanX,StormX):
                        $ Girl.FaceChange("surprised", 2)
                        $ Girl.Eyes = "down"
                        if Girl == LauraX:
                                $ Girl.Brows = "confused"
                                "[Girl.Name], похоже, удивиляется, что вы сделали что-то подобное."
                        else:
                                "[Girl.Name] сильно краснеет, шокированная вашим поведением."
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Lust", 50, 5)
                        if not ApprovalCheck(Girl, 1200, TabM = 3):
                                $ Girl.AddWord(0,"angry","angry",0,0)
                                $ renpy.pop_call()
                                return
                elif Girl.SEXP <= 15:
                        $ Girl.FaceChange("surprised", 2)
                        $ Girl.Eyes = "down"
                        if Girl is EmmaX:
                                $ Girl.Blush = 1
                                "[Girl.Name] с некоторым удивлением смотрит вниз, на ваш член."
                                $ Girl.Statup("Lust", 60, 2)
                        else:
                                "[Girl.Name] с удивлением смотрит вниз, на ваш член."
                        $ Girl.FaceChange("perplexed", 1)
                        $ Girl.Statup("Lust", 60, 8)
                        if not ApprovalCheck(Girl, 1200, TabM = 3) and Girl is not JeanX:
                                return
                elif ApprovalCheck(Girl, 1100, TabM = 3):
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.Name] с улыбкой смотрит вниз на ваш член."
                        $ Girl.FaceChange("sly", 1)
                        $ Girl.Statup("Lust", 70, 8,Alt=[[EmmaX],60,12])
                elif ApprovalCheck(Girl, 500, "I", TabM=2):
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.Name] с веселой улыбкой смотрит на него."
                        $ Girl.FaceChange("sly", 1)
                        $ Girl.Statup("Lust", 70, 10,Alt=[[EmmaX],60,15])
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.Name] с хмурым видом смотрит вниз, на ваш член."
                        $ Girl.Eyes = "sexy"
                        $ Girl.AddWord(0,"angry","angry",0,0)
                        return

                if Girl.Action and Girl.Loc == bg_current and not Cnt:
                    $ BO = ["none"]

                    if Girl.Hand >= 5 and ApprovalCheck(Girl, 1100, TabM = 3):
                            $ Cnt = Girl.Hand - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            while Cnt:
                                $ BO.append("hand")
                                $ Cnt -= 1
                    if Girl.Blow >= 5 and ApprovalCheck(Girl, 1300, TabM = 3):
                            $ Cnt = Girl.Blow - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            $ Cnt += 5 if "hungry" in Girl.Traits else 0
                            while Cnt:
                                $ BO.append("blow")
                                $ Cnt -= 1
                    if Girl.Tit >= 5 and ApprovalCheck(Girl, 1200, TabM = 5):
                            $ Cnt = Girl.Tit - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            while Cnt:
                                $ BO.append("Tit")
                                $ Cnt -= 1
                    if Girl.Sex >= 5 and ApprovalCheck(Girl, 1400, TabM = 5):
                            $ Cnt = Girl.Sex - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            $ Cnt += 5 if Girl.Lust >= 70 else 0
                            while Cnt:
                                $ BO.append("sex")
                                $ Cnt -= 1
                    if Girl.Anal >= 5 and ApprovalCheck(Girl, 1550, TabM = 5):
                            $ Cnt = Girl.Anal - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            $ Cnt += 5 if Girl.Lust >= 70 and Girl.Loose else 0
                            while Cnt:
                                $ BO.append("anal")
                                $ Cnt -= 1

                    $ renpy.random.shuffle(BO)

                    if BO[0] == "hand":
                            if Girl is RogueX:
                                    ch_r "Уверен, что не хочешь, чтобы я занялась этим за тебя?"
                            elif Girl is KittyX:
                                    ch_k "Я могла бы. . . протянуть руку помощи. . ."
                            elif Girl is EmmaX:
                                    ch_e "Может, тебе нужна помощь?"
                            elif Girl is LauraX:
                                    ch_l "Может, тебе помочь?"
                            elif Girl is JeanX:
                                    ch_j "Помощь не нужна?"
                            elif Girl is StormX:
                                    ch_s "Тебе нужна моя помощь?"
                            elif Girl is JubesX:
                                    ch_v "Я могла бы, эм, помочь тебе с этим. . ."
                            elif Girl is GwenX:
                                    ch_g "Тебе не помешает еще одна рука?"
                            elif Girl is BetsyX:
                                    ch_b "Я могла бы помочь тебе. . ."
                            elif Girl is DoreenX:
                                    ch_d "Я, эм, могла бы помочь тебе. . ."
                            elif Girl is WandaX:
                                    ch_w "Слушай, тебе помочь? . ."
                    elif BO[0] == "blow" or (Girl is JubesX and JubesX.Blow):
                            if Girl is RogueX:
                                    ch_r "Уверен, что мой ротик не справится лучше?"
                            elif Girl is KittyX:
                                    ch_k "Я могла бы увлажнить тебя. . ."
                            elif Girl is EmmaX:
                                    ch_e "Я бы не отказалась попробовать его на вкус. . ."
                            elif Girl is LauraX:
                                    ch_l "Он выглядит приятным на вкус. . ."
                            elif Girl is JeanX:
                                    ch_j "Ну, выглядит приятно. . ."
                            elif Girl is StormX:
                                    ch_s "Я бы не отказалась попробовать его на вкус."
                            elif Girl is JubesX:
                                    $ Girl.FaceChange("sly", 1,Mouth="tongue")
                                    ch_v "Я, эм, была бы не против уделить ему все свое внимание. . ."
                                    $ Girl.Mouth="smile"
                                    $ BO[0] = "blow"
                            elif Girl is GwenX:
                                    ch_g "Знаешь, я бы не отказалась попробовать его на вкус. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я могла бы немного полизать его. . ."
                            elif Girl is DoreenX:
                                    ch_d "Я, эм, была бы не прочь лизнуть его. . ."
                            elif Girl is WandaX:
                                    ch_w "Я могу отсосать тебе, если хочешь."
                    elif BO[0] == "tit":
                            if Girl is RogueX:
                                    ch_r "Уверен, что не предпочтешь использовать моих малышек?"
                            elif Girl is KittyX:
                                    ch_k "Моя грудь могла бы согреться. . ."
                            elif Girl is EmmaX:
                                    ch_e "Если хочешь, я могла бы использовать свою грудь. . ."
                            elif Girl is LauraX:
                                    ch_l "Я могла бы использовать свои сиськи. . ."
                            elif Girl is JeanX:
                                    ch_j "Хочешь воспользоваться моими сиськами?"
                            elif Girl is StormX:
                                    ch_s "Ты бы предпочел мои груди?"
                            elif Girl is JubesX:
                                    ch_v "Я могла бы воспользоваться ими. . ."
                            elif Girl is GwenX:
                                    ch_g "Я могла бы подрочить тебе сиськами. . ."
                            elif Girl is BetsyX:
                                    ch_b "Может, ты желаешь воспользоваться моей грудью?"
                            elif Girl is DoreenX:
                                    ch_d "Может ты. . . хочешь воспользоваться моей грудью?"
                            elif Girl is WandaX:
                                    ch_w "Как насчет того, чтобы я воспользовалась своими сиськи?"
                    elif BO[0] == "sex":
                            if Girl is RogueX:
                                    ch_r "Ох, из-за тебя я намокла. . ."
                            elif Girl is KittyX:
                                    ch_k "Я слегка намокла. . ."
                            elif Girl is EmmaX:
                                    ch_e "Знаешь, я просто теку. . ."
                            elif Girl is LauraX:
                                    ch_l "Ну вот я и вся мокрая. . ."
                            elif Girl is JeanX:
                                    ch_j "Это один из способов сделать меня мокрой. . ."
                            elif Girl is StormX:
                                    ch_s "Что ж, это один из способов сделать меня мокрой. . ."
                            elif Girl is JubesX:
                                    ch_v "Я не прочь вставить его. . ."
                            elif Girl is GwenX:
                                    ch_g "Я уже вся мокрая. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я просто -должна- ощутить его внутри себя. . ."
                            elif Girl is DoreenX:
                                    ch_d "Мне, эм, очень хочется ощутить его внутри себя. . ."
                            elif Girl is WandaX:
                                    ch_w "Мне бы сейчас не помешал секс."
                    elif BO[0] == "anal":
                            if Girl is RogueX:
                                    ch_r "Моя попка вся трепещет из-за тебя. . ."
                            elif Girl is KittyX:
                                    ch_k "Почему бы тебе не вставить его сзади. . ."
                            elif Girl is EmmaX:
                                    ch_e "Я не против, если ты воспользуешься моей попкой. . ."
                            elif Girl is LauraX:
                                    ch_l "Почему бы тебе не вставить его в меня. . ."
                            elif Girl is JeanX:
                                    ch_j "Моей попке не помешало бы немного внимания. . ."
                            elif Girl is StormX:
                                    ch_s "Моей попке бы не помешала помощь. . ."
                            elif Girl is JubesX:
                                    ch_v "Я бы не отказалась в попку. . ."
                            elif Girl is GwenX:
                                    ch_g "Я, эм. . . не хочешь вставить его в меня?"
                            elif Girl is BetsyX:
                                    ch_b "Мне нужно ощутить его внутри себя. . ."
                            elif Girl is DoreenX:
                                    ch_d "Мне, эм, очень хочется ощутить его внутри себя. . ."
                            elif Girl is WandaX:
                                    ch_w "Слушай, эм, хочешь трахнуть меня в попку?"
                    else:
                            if Girl is RogueX:
                                    ch_r "Мне нравится вид. . ."
                            elif Girl is KittyX:
                                    ch_k "Прррр. . ."
                            elif Girl is EmmaX:
                                    ch_e "Ммммм. . ."
                            elif Girl is LauraX:
                                    ch_l "Прррр. . ."
                            elif Girl is JeanX:
                                    ch_j "Ооох. . ."
                            elif Girl is StormX:
                                    ch_s "Хмммм. . ."
                            elif Girl is JubesX:
                                    ch_v "Ооох. . ."
                            elif Girl is GwenX:
                                    ch_g "Ну здравствуй. . ."
                            elif Girl is BetsyX:
                                    ch_b "Ох, что такое? . ."
                            elif Girl is DoreenX:
                                    ch_d "Эм. . ."
                            elif Girl is WandaX:
                                    ch_w "Ну привет. . ."
                            return

                    menu:
                        extend ""
                        "Нет, спасибо, у меня все под контролем.":
                                if Girl is RogueX:
                                        ch_r "Многое теряешь, [Girl.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Как хочешь, [Girl.Petname]."
                                elif Girl is EmmaX:
                                        $ Girl.FaceChange("perplexed", 1)
                                        ch_e "Ох. . ."
                                        ch_e "Тогда продолжай, [Girl.Petname]."
                                        $ Girl.FaceChange("sly", 0,Eyes="down")
                                elif Girl is LauraX:
                                        ch_l "Не говори потом, что я не предлагала."
                                elif Girl is JeanX:
                                        ch_j "[[пожимает плечами]"
                                elif Girl is StormX:
                                        ch_s "Ты свой выбор сделал."
                                elif Girl is JubesX:
                                        ch_v "Таков твой выбор. . ."
                                elif Girl is GwenX:
                                        ch_g "Оу."
                                elif Girl is BetsyX:
                                        ch_b "Как хочешь. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ну ладно. . ."
                                elif Girl is WandaX:
                                        ch_w "Ох. . . ну ладно. . ."
                                return
                        "Хмм, звучит как план.":
                                $ Situation = Girl

                    $ Trigger2 = 0
                    #Close out what you were doing
                    if Trigger == "strip":
                            call Group_Strip_End
                    elif Trigger == "masturbation":
                            $ Girl.Action -= 1
                            $ Girl.Mast += 1
                            call Checkout
                    elif Trigger:
                            call CloseOut(Girl)

                    show blackscreen onlayer black
                    hide blackscreen onlayer black
                    $ Situation = Girl #should prevent return issues by adding a pop call
                    if BO[0] == "hand":
                            call Girl_HJ_Prep #jump expression Girl.Tag + "_HJ_Prep"
                    elif BO[0] == "blow":
                            call Girl_BJ_Prep #jump expression Girl.Tag + "_BJ_Prep"
                    elif BO[0] == "tit":
                            call Girl_TJ_Prep #jump expression Girl.Tag + "_TJ_Prep"
                    elif BO[0] == "sex":
                            call Girl_SexPrep #jump expression Girl.Tag + "_SexPrep"
                    elif BO[0] == "anal":
                            call Girl_AnalPrep #jump expression Girl.Tag + "_AnalPrep"
                    $ renpy.pop_call()
                    jump SexMenu
        return
# end Jackin it check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jilling it check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jilling(Girl=0,Cnt=0,BO=[]): #rkeljsvgbdw
        #Called when you try to jack it from inside a sex action
        #should include a girl's name, if not, one is randomly picked from the room.
        if not Girl or Girl not in TotalGirls:
            if Ch_Focus.Loc == bg_current:
                $ Girl = Ch_Focus
            else:
                $ BO = TotalGirls[:]
                python:
                    for BX in BO:
                        if BX.Loc == bg_current:
                                Girl = BX
                                break

        if not Girl or "unseen" in Girl.RecentActions:
                $ Player.RecentActions.append("cockout")
                $ Trigger2 = "jilling"
                "Вы опускаете руку и начинаете поглаживать свою киску."
        else:
                if not Player.Semen:
                        "Сейчас вы чувствуете себя немного разбитой, возможно, вам нужен перерыв."
                        return

                if "cockout" in Player.RecentActions:
                        "Вы начинаете ласкать свою киску."
                else:
                        "Вы опускаете руку и начинаете поглаживать свою киску."
                        $ Player.RecentActions.append("cockout")
                        call Seen_First_Peen(Girl,Partner)

                $ Trigger2 = "jilling"
                if "jilling" in Girl.RecentActions:
                        return
                $ Girl.AddWord(0,"jilling","jilling",0,0)

                if Girl == EmmaX and "classcaught" not in Girl.History:
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Eyes = "down"
                        ch_e "Подожди. . ."
                        $ Girl.FaceChange("angry", 1)
                        ch_e "Это ужасно неуместно."
                        $ Girl.Statup("Lust", 50, 7)
                        if not ApprovalCheck(EmmaX, 1200, TabM = 3):
                                $ Girl.AddWord(0,"angry","angry",0,0)
                                $ renpy.pop_call()
                                return

                if Girl.SEXP < 10 and Girl not in (JeanX,StormX):
                        $ Girl.FaceChange("surprised", 2)
                        $ Girl.Eyes = "down"
                        if Girl == LauraX:
                                $ Girl.Brows = "confused"
                                "[Girl.Name], похоже, удивиляется, что вы сделали что-то подобное."
                        else:
                                "[Girl.Name] сильно краснеет, шокированная вашим поведением."
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Lust", 50, 5)
                        if not ApprovalCheck(Girl, 1200, TabM = 3):
                                $ Girl.AddWord(0,"angry","angry",0,0)
                                $ renpy.pop_call()
                                return
                elif Girl.SEXP <= 15:
                        $ Girl.FaceChange("surprised", 2)
                        $ Girl.Eyes = "down"
                        if Girl == EmmaX:
                                $ Girl.Blush = 1
                                "[Girl.Name] с некоторым удивлением смотрит вниз, на вашу промежность."
                                $ Girl.Statup("Lust", 60, 2)
                        else:
                                "[Girl.Name] с удивлением смотрит вниз, на вашу промежность."
                        $ Girl.FaceChange("perplexed", 1)
                        $ Girl.Statup("Lust", 60, 8)
                        if not ApprovalCheck(Girl, 1200, TabM = 3) and Girl is not JeanX:
                                return
                elif ApprovalCheck(Girl, 1100, TabM = 3):
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.Name] с улыбкой смотрит вниз, на вашу промежность."
                        $ Girl.FaceChange("sly", 1)
                        $ Girl.Statup("Lust", 70, 8,Alt=[[EmmaX],60,12])
                elif ApprovalCheck(Girl, 500, "I", TabM=2):
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.Name] с веселой улыбкой смотрит на нее."
                        $ Girl.FaceChange("sly", 1)
                        $ Girl.Statup("Lust", 70, 10,Alt=[[EmmaX],60,15])
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Eyes = "down"
                        "[Girl.Name] с хмурым видом смотрит вниз,на вашу промежность."
                        $ Girl.Eyes = "sexy"
                        $ Girl.AddWord(0,"angry","angry",0,0)
                        return

                if Girl.Action and Girl.Loc == bg_current and not Cnt:
                    $ BO = ["none"]

                    if Girl.Finger >= 5 and ApprovalCheck(Girl, 1100, TabM = 3):
                            $ Cnt = Girl.Finger - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            while Cnt:
                                $ BO.append("finger")
                                $ Cnt -= 1
                    if Girl.CUN >= 5 and ApprovalCheck(Girl, 1300, TabM = 3):
                            $ Cnt = Girl.CUN - 4
                            $ Cnt = 10 if Cnt > 10 else Cnt
                            $ Cnt += 5 if "hungry" in Girl.Traits else 0
                            while Cnt:
                                $ BO.append("cun")
                                $ Cnt -= 1
#                    if Girl.Tit >= 5 and ApprovalCheck(Girl, 1200, TabM = 5):
#                            $ Cnt = Girl.Tit - 4
#                            $ Cnt = 10 if Cnt > 10 else Cnt
#                            while Cnt:
#                                $ BO.append("Tit")
#                                $ Cnt -= 1
#                    if Girl.Sex >= 5 and ApprovalCheck(Girl, 1400, TabM = 5):
#                            $ Cnt = Girl.Sex - 4
#                            $ Cnt = 10 if Cnt > 10 else Cnt
#                            $ Cnt += 5 if Girl.Lust >= 70 else 0
#                            while Cnt:
#                                $ BO.append("sex")
#                                $ Cnt -= 1
#                    if Girl.Anal >= 5 and ApprovalCheck(Girl, 1550, TabM = 5):
#                            $ Cnt = Girl.Anal - 4
#                            $ Cnt = 10 if Cnt > 10 else Cnt
#                            $ Cnt += 5 if Girl.Lust >= 70 and Girl.Loose else 0
#                            while Cnt:
#                                $ BO.append("anal")
#                                $ Cnt -= 1

                    $ renpy.random.shuffle(BO)

                    if BO[0] == "finger":
                            if Girl is RogueX:
                                    ch_r "Уверена, что не хочешь, чтобы я занялась этим за тебя?"
                            elif Girl is KittyX:
                                    ch_k "Я могла бы. . . протянуть руку помощи. . ."
                            elif Girl is EmmaX:
                                    ch_e "Может, тебе нужна помощь?"
                            elif Girl is LauraX:
                                    ch_l "Может, тебе помочь?"
                            elif Girl is JeanX:
                                    ch_j "Помощь не нужна?"
                            elif Girl is StormX:
                                    ch_s "Тебе нужна моя помощь?"
                            elif Girl is JubesX:
                                    ch_v "Я могла бы, эм, помочь тебе с этим. . ."
                            elif Girl is GwenX:
                                    ch_g "Тебе не помешает еще одна рука?"
                            elif Girl is BetsyX:
                                    ch_b "Я могла бы помочь тебе. . ."
                            elif Girl is DoreenX:
                                    ch_d "Я, эм, могла бы помочь тебе. . ."
                            elif Girl is WandaX:
                                    ch_w "Я могла бы помочь тебе. . ."
                    elif BO[0] == "cun" or (Girl is JubesX and JubesX.CUN):
                            if Girl is RogueX:
                                    ch_r "Уверена, что мой ротик не справится лучше?"
                            elif Girl is KittyX:
                                    ch_k "Я могла бы увлажнить тебя. . ."
                            elif Girl is EmmaX:
                                    ch_e "Я бы не отказалась попробовать ее на вкус. . ."
                            elif Girl is LauraX:
                                    ch_l "Она выглядит приятной на вкус. . ."
                            elif Girl is JeanX:
                                    ch_j "Ну, выглядит приятно. . ."
                            elif Girl is StormX:
                                    ch_s "Я бы не отказалась попробовать ее на вкус."
                            elif Girl is JubesX:
                                    $ Girl.FaceChange("sly", 1,Mouth="tongue")
                                    ch_v "Я, эм, была бы не против уделить ей все свое внимание. . ."
                                    $ Girl.Mouth="smile"
                                    $ BO[0] = "blow"
                            elif Girl is GwenX:
                                    ch_g "Знаешь, я бы не отказалась попробовать еге на вкус. . ."
                            elif Girl is BetsyX:
                                    ch_b "Не возражаешь, если я лизну? . ."
                            elif Girl is DoreenX:
                                    ch_d "Я, эм, хочу попробовать ее. . ."
                            elif Girl is WandaX:
                                    ch_w "Слушай, можно мне попробовать ее?"
#                    elif BO[0] == "tit":
#                            if Girl is RogueX:
#                                    ch_r "Sure you wouldn't prefer using these?"
#                            elif Girl is KittyX:
#                                    ch_k "My chest might keep that warm. . ."
#                            elif Girl is EmmaX:
#                                    ch_e "If you like, I could use my chest. . ."
#                            elif Girl is LauraX:
#                                    ch_l "I could use my tits. . ."
#                            elif Girl is JeanX:
#                                    ch_j "Did you want to use my tits with that?"
#                            elif Girl is StormX:
#                                    ch_s "Would you prefer these?"
#                            elif Girl is JubesX:
#                                    ch_v "I could use these. . ."
#                    elif BO[0] == "sex":
#                            if Girl is RogueX:
#                                    ch_r "Oh, you're making me pretty wet here. . ."
#                            elif Girl is KittyX:
#                                    ch_k "I'm getting a little wet. . ."
#                            elif Girl is EmmaX:
#                                    ch_e "I'm positively dripping, you know. . ."
#                            elif Girl is LauraX:
#                                    ch_l "Well that's getting me wet. . ."
#                            elif Girl is JeanX:
#                                    ch_j "That's one way to get me wet. . ."
#                            elif Girl is StormX:
#                                    ch_s "Well that is one way to get me wet. . ."
#                            elif Girl is JubesX:
#                                    ch_v "I wouldn't mind sticking that in. . ."
#                    elif BO[0] == "anal":
#                            if Girl is RogueX:
#                                    ch_r "You've really got my ass tingling. . ."
#                            elif Girl is KittyX:
#                                    ch_k "Why don't you bring that in through the back. . ."
#                            elif Girl is EmmaX:
#                                    ch_e "I wouldn't mind you using the back door. . ."
#                            elif Girl is LauraX:
#                                    ch_l "Why don't you stick that in me. . ."
#                            elif Girl is JeanX:
#                                    ch_j "I could use some attention around back. . ."
#                            elif Girl is StormX:
#                                    ch_s "I could use some help in back. . ."
#                            elif Girl is JubesX:
#                                    ch_v "I wouldn't mind taking that in the back. . ."
                    else:
                            if Girl is RogueX:
                                    ch_r "Мне нравится вид. . ."
                            elif Girl is KittyX:
                                    ch_k "Прррр. . ."
                            elif Girl is EmmaX:
                                    ch_e "Ммммм. . ."
                            elif Girl is LauraX:
                                    ch_l "Прррр. . ."
                            elif Girl is JeanX:
                                    ch_j "Ооох. . ."
                            elif Girl is StormX:
                                    ch_s "Хмммм. . ."
                            elif Girl is JubesX:
                                    ch_v "Ооох. . ."
                            elif Girl is GwenX:
                                    ch_g "Ну здравствуй. . ."
                            elif Girl is BetsyX:
                                    ch_b "Ох? Что такое? . ."
                            elif Girl is DoreenX:
                                    ch_d "Эм?"
                            elif Girl is WandaX:
                                    ch_w "Ох, миленько. . ."
                            return

                    menu:
                        extend ""
                        "Нет, спасибо, у меня все под контролем.":
                                if Girl is RogueX:
                                        ch_r "Многое теряешь, [Girl.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Как хочешь, [Girl.Petname]."
                                elif Girl is EmmaX:
                                        $ Girl.FaceChange("perplexed", 1)
                                        ch_e "Ох. . ."
                                        ch_e "Тогда продолжай, [Girl.Petname]."
                                        $ Girl.FaceChange("sly", 0,Eyes="down")
                                elif Girl is LauraX:
                                        ch_l "Не говори потом, что я не предлагала."
                                elif Girl is JeanX:
                                        ch_j "[[пожимает плечами]"
                                elif Girl is StormX:
                                        ch_s "Ты свой выбор сделала."
                                elif Girl is JubesX:
                                        ch_v "Таков твой выбор. . ."
                                elif Girl is GwenX:
                                        ch_g "Оу."
                                elif Girl is BetsyX:
                                        ch_b "Как хочешь. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ну ладно. . ."
                                elif Girl is WandaX:
                                        ch_w "Ох. . . ну ладно. . ."
                                return
                        "Хмм, звучит как план.":
                                $ Situation = Girl

                    $ Trigger2 = 0
                    #Close out what you were doing
                    if Trigger == "strip":
                            call Group_Strip_End
                    elif Trigger == "masturbation":
                            $ Girl.Action -= 1
                            $ Girl.Mast += 1
                            call Checkout
                    elif Trigger:
                            call CloseOut(Girl)

                    show blackscreen onlayer black
                    hide blackscreen onlayer black
                    if BO[0] == "finger":
                            call Girl_Finger_Prep
                            return
                    elif BO[0] == "cun":
                            call Girl_CUN_Prep
                            return
#                    elif BO[0] == "tit":
#                            jump expression Girl.Tag + "_TJ_Prep"
#                    elif BO[0] == "sex":
#                            jump expression Girl.Tag + "_SexPrep"
#                    elif BO[0] == "anal":
#                            jump expression Girl.Tag + "_AnalPrep"
                    $ renpy.pop_call()
                    jump SexMenu
        return
# end Jilling it check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# For when she tags you to drain you start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Tag(Girl=0,Forced = 0,Gloves=0): #rkeljsvgbdw
        #Called mostly by Addiction
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)
        $ Gloves = Girl.Arms
        $ Girl.ArmPose = 2
        if not Forced:
                $ Girl.Eyes = "closed"
                $ Girl.Brows = "sad"

        if Forced and Player.Lvl >= 5:
            if Gloves == "gloves":
                    $ Girl.Arms = 0
                    "Она стягивает перчатки и тянется к вашему лицу."
            else:
                    "Она тянется к вашему лицу."
            menu:
                extend ""
                "Поймать ее руку [[отказаться].":
                        $ Girl.FaceChange("surprised", 1)
                        "Вы перехватываете ее руку. Краткого контакта для нее недостаточно."
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Love", 80, -10)
                        if Girl.Addict >= 80 and not ApprovalCheck(Girl, 400, "O",Alt=[[RogueX],600]):
                                #if she's strung out and not obedient
                                $ Girl.Eyes = "manic"
                                "Она набрасывается на вас и хватает за подбородок."
                                $ Girl.Eyes = "sly"
                                if "no tag" not in Girl.RecentActions:
                                        $ Girl.Statup("Obed", 50, -5)
                                        $ Girl.Statup("Inbt", 30, 5)
                                        $ Girl.Statup("Inbt", 90, 1)
                                $ Forced = 1
                        else:
                                if Girl is RogueX:
                                        ch_r "Это не круто, [Girl.Petname]."
                                elif Girl is KittyX:
                                        ch_k "[Girl.Like]так не круто, [Girl.Petname]."
                                elif Girl is EmmaX:
                                        ch_e "Ты не захочешь увидеть во мне врага, [Player.Name]."
                                elif Girl is LauraX:
                                        ch_l "Не дави на меня, [Girl.Petname]."
                                elif Girl is JeanX:
                                        ch_j "Я тебе не понравлюсь, когда разозлюсь, [Girl.Petname]."
                                elif Girl is StormX:
                                        ch_s "Не играй со мной, [Girl.Petname]."
                                elif Girl is JubesX:
                                        ch_v "Пожалуйста. . ."
                                elif Girl is GwenX:
                                        if not Player.Male:
                                            ch_g "Эй, это ты втянула меня в это. . ."
                                        else:
                                            ch_g "Эй, это ты втянул меня в это. . ."
                                elif Girl is BetsyX:
                                        ch_b "Меня все это очень раздражает. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ты не даешь мне другого выбора. . ."
                                elif Girl is WandaX:
                                        ch_w "Жаль, что у меня нет иного выбора."
                                if "no tag" not in Girl.RecentActions:
                                        $ Girl.Statup("Obed", 50, 5)
                                        $ Girl.Statup("Obed", 80, 5)
                                $ Girl.RecentActions.append("no tag")
                                $ Girl.DailyActions.append("no tag")
                                $ Girl.Arms = Gloves
                                $ Girl.ArmPose = 1
                                return
                "Позволить.":
                        "Она касается вашего лица."
        else:
                $ Girl.Addict -= 10
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0
                $ Girl.Statup("Lust", 90, 5)
                if Gloves == "gloves":
                        $ Girl.Arms = 0
                        $ Line = "Она стягивает перчатки и"
                else:
                        $ Line = "Она протягивает руку и"
                if Girl is RogueX:
                            "[Line] ненадолго касается вашего лица."
                elif Girl is KittyX:
                            "[Line] хватает вас за обе щеки, пристально глядя в глаза."
                elif Girl is EmmaX:
                            "[Line] гладит тыльной стороной ладони вас по щеке."
                elif Girl is LauraX:
                            "[Line] хватает вас за лицо одной рукой и крепко тискает за щеку."
                elif Girl is JeanX:
                            "[Line] обхватывает рукой вашу шею сзади."
                elif Girl is StormX:
                            "[Line] проводит рукой по вашей щеке."
                elif Girl is JubesX:
                            "[Line] гладит вас по шее и кладет ладонь вам под подбородок."
                elif Girl is GwenX:
                            "[Line] тискает вас за щеки обеими руками."
                elif Girl is BetsyX:
                            "[Line] хватает вас за подбородок одной рукой и сжимает его."
                elif Girl is DoreenX:
                            "[Line] щипает вас за щеку, больно."
                elif Girl is WandaX:
                            "[Line] прикасается кончиками пальцев к вашему лбу."
        $ Girl.Blush = 2

        if Round <= 15:
                $ Girl.Addict -= 15 if Girl.Addict > 15 else Girl.Addict
        while Girl.Addict > 20 and Round > 15:
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0
                $ Girl.Addict -= 15
                $ Round -= 5
                $ Girl.Statup("Lust", 90, 5)
                if Girl == RogueX:
                        $ Girl.Statup("Lust", 90, 5)
                elif Forced:
                        $ Girl.Statup("Obed", 50, 1)
                "Она продолжает прикасаться к вам, легкая дрожь проходит по всему ее телу."
        if Round <= 15:
                call AnyLine(Girl,"Похоже, у нас нет времени на большее.")
        if Gloves and not Girl.Arms:
                "Удовлетворив свое желание, она снова надевает перчатки."
        $ Girl.Blush = 1
        $ Girl.Arms = Gloves
        $ Girl.ArmPose = 1
        $ Girl.FaceChange()
        if Forced:
                $ Girl.RecentActions.append("forced tag")
                $ Girl.DailyActions.append("forced tag")
        $ Girl.RecentActions.append("tag")
        $ Girl.DailyActions.append("tag")
        return
# End "tag" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Slap Ass / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Slap_Ass(Girl=0):  #rkeljsvgbdw
        if Girl not in TotalGirls:
                return
        call Shift_Focus(Girl)
        # Modification mode
        $ play_sound(name=audio.slap, multi=True, loop=False)
        # -----------------
        if renpy.showing(Girl.Tag+"_Doggy_Animation"):
                call Slap_Anim(Girl)
        else:
                call Punch

        $ Girl.Slap += 1 #add in slap-base obedience

        $ Girl.Blush = 2 if Taboo else 1
        if ApprovalCheck(Girl, 200, "O", TabM=1):
                $ Girl.FaceChange("sexy", 1)
                $ Girl.Mouth = "surprised"
                $ Girl.Statup("Lust", 51, 3, 1)
                $ Girl.Statup("Lust", 80, 1)
                if Girl.RecentActions.count("slap") < 4:
                        $ Girl.Statup("Lust", 200, 1)
                        if Girl.Slap <= 5:
                                $ Girl.Statup("Obed", 50, 2)
                        if Girl.Slap <= 10:
                                $ Girl.Statup("Obed", 80, 1)
                else:
                        $ Girl.Red = 1
                "Вы шлепаете ее по заднице, и она подпрыгивает от удовольствия."
        else:
                $ Girl.FaceChange("surprised", 1)
                if Girl.RecentActions.count("slap") < 4:
                        $ Girl.Statup("Obed", 70, 2)
                        $ Girl.Statup("Love", 50, -1)
                else:
                        $ Girl.Red = 1
                "Вы шлепаете ее по заднице, и она кидает на вас немного испуганный взгляд."

        if Trigger and Girl.Lust >= 100:
                #If you're still going at it and Rogue can cum
                call Girl_Cumming(Girl)

        if Taboo:
                if not ApprovalCheck(Girl, 800, TabM=2):
                        if Girl.Slap <= 5:
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.Statup("Obed", 50, 2)
                        $ Girl.Statup("Love", 70, -2)
                        $ Girl.Statup("Love", 50, -1)
                        "Похоже, она немного рассердилась."
                elif not ApprovalCheck(Girl, 1500, TabM=2):
                        if Girl.Slap <= 5:
                                $ Girl.Statup("Obed", 80, 2)
                        $ Girl.Statup("Love", 70, -1)
                        "Похоже, она немного засмущалась."
                else:                         #Over 1500
                        $ Girl.FaceChange("sexy")
                        $ Girl.Mouth = "smile"
                        if Girl.Slap <= 5:
                                $ Girl.Statup("Obed", 80, 1)
                        "Она одаривает вас озорной ухмылкой."
                $ Girl.Blush = 1
        if Girl.PantsNum() < 5 and Girl.PantiesNum() < 5:
                if ApprovalCheck(Girl, 500, "O") and Girl.RecentActions.count("slap") < 4:
                        $ Girl.Statup("Obed", 90, 1)
                        $ Girl.Statup("Lust", 200, 3)
                else:
                        $ Girl.Statup("Lust", 80, 1)
                $ Girl.Addict -= 1
        $ Girl.RecentActions.append("slap") if Girl.RecentActions.count("slap") < 4 else Girl.RecentActions
        $ Girl.DailyActions.append("slap") if Girl.DailyActions.count("slap") < 10 else Girl.DailyActions
        return

# End Slap Ass / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Makeout / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Makeout(Girl=0): #rkeljsvgbdw
        if Girl:
                call Shift_Focus(Girl)
        $ Round -= 5 if Round > 5 else (Round-1)

        call expression Ch_Focus.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
        if not Player.Male and "girltalk" not in Ch_Focus.History:
                return

        $ Approval = ApprovalCheck(Ch_Focus, 700, TabM=1,Alt=[[RogueX,JeanX],500]) #reduced check for Rogue

        if Ch_Focus is EmmaX and not ApprovalCheck(Ch_Focus, 1000):
                #if it's Emma, and she doesn't like you all that much. . .
                $ Ch_Focus.FaceChange("sadside")
                ch_e "Мы же едва знаем друг друга. . ."
                $ Ch_Focus.RecentActions.append("no kissing")
                $ Ch_Focus.DailyActions.append("no kissing")
                return
        if Approval > 1 and not Ch_Focus.Kissed and not Ch_Focus.Forced:
                #first time and she's into it
                $ Ch_Focus.FaceChange("sexy")
                $ Ch_Focus.Eyes = "side"
                if Ch_Focus is RogueX:
                        ch_r "Раньше я ни с кем не могла этого сделать, я немного взволнована. . ."
                elif Ch_Focus is KittyX:
                        if not Player.Male:
                            ch_k "Ты довольно милая. . ."
                        else:
                            ch_k "Ты довольно милый. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Ну, полагаю, это не повредит. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Стоит попробовать. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Почему нет?"
                elif Ch_Focus is StormX:
                        ch_s "Мне бы этого хотелось."
                elif Ch_Focus is JubesX:
                        ch_v "Я думаю, мы очень плохо начали. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Поцелуи? Конечно, почему бы и нет. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Я прямо очарована тобой. . ."
                elif Ch_Focus is DoreenX:
                        if not Player.Male:
                            ch_d "Ты такая обояшка. . ."
                        else:
                            ch_d "Ты такой обояшка. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Я думала, ты никогда не спросишь. . ."
        elif Approval and not Ch_Focus.Kissed:
                #first time, lower enthusiasm
                $ Ch_Focus.FaceChange("sexy")
                $ Ch_Focus.Eyes = "side"
                if Ch_Focus is RogueX:
                        ch_r "Думаю, стоит попробовать. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Я попробую. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Мы могли бы. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Если ты настаиваешь. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Думаю, можно. . ."
                elif Ch_Focus is StormX:
                        ch_s "Пожалуй, можно."
                elif Ch_Focus is JubesX:
                        ch_v "Пожалуй, мы могли бы. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Наверное, мы могли бы. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Пожалуй, можно. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Ну, я думаю, это мне не помешает. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Думаю, я бы не отказалась от легкого поцелуя. . ."
        elif Approval and "kissing" in Ch_Focus.RecentActions:
                # you were just kissing earlier
                $ Ch_Focus.FaceChange("sexy", 1)
                if Ch_Focus is KittyX:
                        ch_k "Мррр. . ."
                else:
                        call AnyLine(Ch_Focus,"Мммм. . .")
                jump KissPrep
        elif Approval and "kissing" in Ch_Focus.DailyActions:
                #you'd been kissing earlier in the day
                $ Ch_Focus.FaceChange("sexy", 1)

                $ Line = renpy.random.choice(["A","B","C"])
                if Line == "A":
                    call AnyLine(Ch_Focus,"Тебе все мало?")
                elif Ch_Focus is RogueX:
                    if Line == "B":
                            ch_r "-Я- привыкла, что мои прикосновения вытягивают из людей жизнь. . ."
                    else:
                            if not Player.Male:
                                ch_r "Дай мне немного сладенького, сладенькая."
                            else:
                                ch_r "Дай мне немного сладенького, сладенький."
                elif Ch_Focus is KittyX:
                    if Line == "B":
                            ch_k "Мяу."
                    else:
                            ch_k "Иди сюда, вкусняшка."
                elif Ch_Focus is EmmaX:
                    if Line == "B":
                            ch_e "Мммм. . ."
                    else:
                            ch_e "Иди ко мне."
                elif Ch_Focus is LauraX:
                    if Line == "B":
                            ch_l "Ммммм."
                    else:
                            ch_l "Иди сюда."
                elif Ch_Focus is JeanX:
                    if Line == "B":
                            ch_j "Мммммм. . ."
                    else:
                            ch_j "Ох, иди сюда."
                elif Ch_Focus is StormX:
                    if Line == "B":
                            ch_s "Мммм. . ."
                    else:
                            ch_s "Да, давай."
                elif Ch_Focus is JubesX:
                    if Line == "B":
                            ch_v "Мммм. . ."
                    else:
                            ch_v "Конечно, иди ко мне."
                elif Ch_Focus is GwenX:
                    if Line == "B":
                            ch_g "Мммм. . ."
                    else:
                            ch_g "Иди сюда. . . [[В оригинале кидает фразу скорпиона из мортал комбат \"get over here\"]"
                elif Ch_Focus is BetsyX:
                    if Line == "B":
                            ch_b "Ммм. . ."
                    else:
                            ch_b "Иди ко мне. . ."
                elif Ch_Focus is DoreenX:
                    if Line == "B":
                            ch_d "Мм-мм. . ."
                    else:
                            ch_d "Иди сюда. . ."
                elif Ch_Focus is WandaX:
                    if Line == "B":
                            ch_w "Мммммм. . ."
                    else:
                            ch_w "Подойди. . ."
                $ Line = 0
        elif Approval > 1 and Ch_Focus.Love > Ch_Focus.Obed:
                # love is higher than obedience
                $ Ch_Focus.FaceChange("sexy")
                if Ch_Focus is RogueX:
                        ch_r "Конечно, почему нет?"
                elif Ch_Focus is KittyX:
                        ch_k "Поцелуйчики!"
                elif Ch_Focus is EmmaX:
                        ch_e "Муа."
                elif Ch_Focus is LauraX:
                        ch_l "Ммммм. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Мммммм. . ."
                elif Ch_Focus is StormX:
                        ch_s "Хмм. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Мммм. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Хех. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Мммм. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Мм-мм. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Мммммм. . ."
        elif ApprovalCheck(Ch_Focus, 500, "O") and Ch_Focus.Obed > Ch_Focus.Love:
                # if Obedience is higher
                $ Ch_Focus.FaceChange("normal")
                if Ch_Focus is RogueX:
                        ch_r "Если хочешь."
                elif Ch_Focus is KittyX:
                        ch_k "Конечно."
                elif Ch_Focus is EmmaX:
                        ch_e "Конечно."
                elif Ch_Focus is LauraX:
                        ch_l "Если хочешь."
                elif Ch_Focus is JeanX:
                        ch_j "Ладно. . ."
                elif Ch_Focus is StormX:
                        ch_s "Хорошо. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Конечно. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Ладно. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Конечно. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Конечно. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Ладно. . ."
                $ Ch_Focus.Statup("Obed", 60, 1)
        elif ApprovalCheck(Ch_Focus, 250, "O",Alt=[[KittyX,LauraX],300]) and ApprovalCheck(Ch_Focus, 250, "L",Alt=[[KittyX,LauraX],200]):
                #if not that into it
                $ Ch_Focus.FaceChange("bemused")
                call AnyLine(Ch_Focus,"Ладно.")
                $ Ch_Focus.Statup("Obed", 50, 3)
        elif Ch_Focus.Addict >= 50:
                #high addiction
                $ Ch_Focus.FaceChange("sexy")
                $ Ch_Focus.Eyes = "manic"
                if Ch_Focus is RogueX:
                        ch_r "Хм. . . хорошо давай сделаем это."
                elif Ch_Focus is KittyX:
                        ch_k "Думаю, мне придется."
                elif Ch_Focus is EmmaX:
                        ch_e ". . . да."
                elif Ch_Focus is LauraX:
                        ch_l "Мне придется."
                elif Ch_Focus is JeanX:
                        ch_j "Эм. . . да. . ."
                elif Ch_Focus is StormX:
                        ch_s ". . . да. . ."
                elif Ch_Focus is JubesX:
                        ch_v "О, да. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Ах, да!"
                elif Ch_Focus is BetsyX:
                        ch_b ". . . неплохо."
                elif Ch_Focus is DoreenX:
                        ch_d "Ох, ага, ладно. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Ага. . ."
        elif Approval:
                #she's barely into it
                $ Ch_Focus.FaceChange("bemused")
                if Ch_Focus is RogueX:
                        ch_r "Хмм, ладно."
                elif Ch_Focus is KittyX:
                        ch_k "Ага, как скажешь."
                elif Ch_Focus is EmmaX:
                        ch_e "Отлично."
                elif Ch_Focus is LauraX:
                        ch_l "Конечно."
                elif Ch_Focus is JeanX:
                        ch_j "Как скажешь. . ."
                elif Ch_Focus is StormX:
                        ch_s "Хорошо."
                elif Ch_Focus is JubesX:
                        ch_v "Ладно, конечно. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Как скажешь. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Думаю, я не против. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Ага. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Ладно. . ."
        else:
                #she's out
                $ Ch_Focus.FaceChange("normal") # Else
                $ Ch_Focus.Mouth = "sad"
                if Ch_Focus is RogueX:
                        ch_r "Нет, не думаю, что мне это интересно."
                elif Ch_Focus is KittyX:
                        ch_k "Не-а."
                elif Ch_Focus is EmmaX:
                        ch_e "Хмм, нет."
                elif Ch_Focus is LauraX:
                        ch_l "Нет."
                elif Ch_Focus is JeanX:
                        ch_j "Ну да, ты бы хотел. . ."
                elif Ch_Focus is StormX:
                        ch_s "Я так не думаю."
                elif Ch_Focus is JubesX:
                        ch_v "Нет, спасибо. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Эм. . . мне это не интересно?"
                elif Ch_Focus is BetsyX:
                        ch_b "Честно говоря, я не в настроении целоваться. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я бы, эм, этого не хотела. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Я. . . так не думаю. . ."
                $ Ch_Focus.RecentActions.append("no kissing")
                $ Ch_Focus.DailyActions.append("no kissing")
                return

label KissPrep:
        # Modification mode
        if is_playing_music(audio.girl_kiss):
                $ play_music(name=audio.girl_kiss, loop=True)
        # -----------------

#        call Shift_Focus(Girl)
        $ Ch_Focus.Statup("Inbt", 10, 1)
        $ Ch_Focus.Statup("Inbt", 20, 1)

        call Girl_Kissing_Launch(Ch_Focus,"kiss you") #call expression Ch_Focus.Tag + "_Kissing_Launch" pass ("kiss you")

        if Ch_Focus.Kissed >= 10 and Ch_Focus.Inbt >= 300:
                $ Ch_Focus.FaceChange("sucking")
        elif Ch_Focus.Kissed > 1 and Ch_Focus.Addict >= 50:
                $ Ch_Focus.FaceChange("sucking")
        else:
                $ Ch_Focus.FaceChange("kiss",2)
        if Taboo:
                $ Ch_Focus.DrainWord("tabno")
        $ Ch_Focus.DrainWord("no kissing")

        if Ch_Focus is RogueX and not Ch_Focus.Kissed:
                #If it's Rogue's first time, it's only a simple kiss and then ends
                "Вы наклоняетесь и ваши губы встречаются с губами [Ch_Focus.Name_rod]."
                $ Ch_Focus.Eyes = "surprised"
                $ Ch_Focus.Statup("Love", 90, 15)
                $ Ch_Focus.Statup("Love", 60, 30)
                "Между вами проходит легкая искра, а ее глаза расширяются от удивления."
                $ Ch_Focus.Statup("Lust", 70, 5)
                ch_r "Вау, [Ch_Focus.Petname], это что-то с чем-то. . ."
                $ Ch_Focus.FaceChange("bemused",1)
                ch_r "Непривычные ощущения."
                $ Ch_Focus.Addict -= 5
                $ Ch_Focus.Statup("Obed", 30, 20)
                $ Ch_Focus.Statup("Inbt", 30, 30)
                jump Kiss_After

        if Situation == Ch_Focus:
                #Girl auto-starts
                $ Situation = 0
                "[Ch_Focus.Name] прижимается всем телом к вам и страстно вас целует."
                menu:
                    "Что будете делать?"
                    "Не сопротивляться.":
                            $ Ch_Focus.Statup("Inbt", 80, 3)
                            $ Ch_Focus.Statup("Inbt", 50, 2)
                            "Вы отдаетесь поцелую."
                    "Похвалить ее.":
                            $ Ch_Focus.FaceChange("sexy", 1)
                            $ Ch_Focus.Statup("Inbt", 80, 3)
                            ch_p "Ммм, какой приятный сюрприз, [Ch_Focus.Pet]."
                            $ Ch_Focus.NameCheck() #checks reaction to petname
                            "Вы отдаетесь поцелую."
                            $ Ch_Focus.Statup("Love", 85, 1)
                            $ Ch_Focus.Statup("Obed", 90, 1)
                            $ Ch_Focus.Statup("Obed", 50, 2)
                    "Сказать ей остановиться.":
                            "Вы отстраняетесь."
                            $ Ch_Focus.FaceChange("surprised")
                            $ Ch_Focus.Statup("Inbt", 70, 1)
                            ch_p "[Ch_Focus.Pet], давай не будем этого делать."
                            $ Ch_Focus.NameCheck() #checks reaction to petname
                            $ Ch_Focus.Statup("Obed", 90, 1)
                            $ Ch_Focus.Statup("Obed", 50, 1)
                            $ Ch_Focus.Statup("Obed", 30, 2)
                            $ Player.RecentActions.append("nope")
                            $ Ch_Focus.AddWord(1,"refused","refused")
                            return
                #end auto

        if Ch_Focus.Kissed >= 10 and Ch_Focus.Lust >= 80:
                $ Line = renpy.random.choice(["Она набрасывается на вас и начинает водить руками по вашему телу.",
                        "Она набрасывается на вас и начинает облизываеть все ваше лицо и шею.",
                        "Она набрасывается на вас и начинает покрывать все ваше лицо поцелуями, сильно к вам прижимаясь."])
        elif Ch_Focus.Kissed > 7:
                $ Line = renpy.random.choice(["Она интенсивно обсасывает ваше лицо.",
                        "Вы очень страстно целуетесь.",
                        "Вы очень страстно целуетесь.",
                        "Вы очень страстно целуетесь."])
        elif Ch_Focus.Kissed > 3:
                $ Line = renpy.random.choice(["Она сильно увлекается процессом.",
                        "Она сильно увлекается процессом, ее язык уже вовсю в работе.",
                        "Она сильно увлекается процессом, ее язык вытворяет страшные вещи."])
        else:
                $ Line = "Вы с ней целуетесь какое-то время."
        "[Line]"
        $ Cnt = 0
        $ Trigger = "kiss you"
        $ Line = 0
        if Situation:
            $ renpy.pop_call()
            $ Situation = 0

label KissCycle:
        while Round > 0:
#            call Shift_Focus(Girl)
            call Girl_Kissing_Launch(Ch_Focus,"kiss you") #call expression Ch_Focus.Tag + "_Kissing_Launch" pass ("kiss you")
            $ Ch_Focus.LustFace()
            $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
            if  Player.Focus < 100:
                        #Player Command menu
                        menu:
                            "Продолжать. . .":
                                        pass

                            "Шлепнуть ее по заднице":
                                        call Slap_Ass(Ch_Focus)
                                        $ Cnt += 1
                                        $ Round -= 1
                                        jump KissCycle

                            "Концентрироваться на продолжительности [[Не открыто]. (locked)" if "focus" not in Player.Traits:
                                        pass
                            "Концентрироваться на продолжительности." if not Player.FocusX and "focus" in Player.Traits:
                                        "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                        $ Player.FocusX = 1
                            "Прекратить концентрироваться." if Player.FocusX:
                                        "Вы расслабляетесь. . ."
                                        $ Player.FocusX = 0

                            "Начать дрочить." if MultiAction and Trigger2 != "jackin" and Player.Male:
                                        call Jackin
                            "Перестать дрочить." if MultiAction and Trigger2 == "jackin":
                                        "Вы перестаете дрочить."
                                        $ Trigger2 = 0
                            "Начать мастурбировать." if Trigger2 != "jilling" and not Player.Male:
                                        call Jilling
                            "Перестать мастурбировать." if Trigger2 == "jilling":
                                        $ Trigger2 = 0

                            "Другие варианты":
                                    menu:
                                        "Дополнительное действие":
                                                if Ch_Focus.Action and MultiAction:
                                                        call Offhand_Set
                                                        if Trigger2:
                                                             $ Ch_Focus.Action -= 1
                                                else:
                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                        #"I'm actually getting a little tired, so maybe we could wrap this up?"

                                        "Сменить основное действие":
                                                if Ch_Focus.Action and MultiAction:
                                                        menu:
                                                            "Переместить руку к ее груди. . ." if Ch_Focus.Kissed >= 1 and MultiAction:
                                                                    if Ch_Focus.Action and MultiAction:
                                                                        $ Situation = "auto"
                                                                        call Kiss_After
                                                                        call Girl_Fondle_Breasts #call expression Ch_Focus.Tag + "_Fondle_Breasts"
                                                                        if Trigger == "fondle breasts":
                                                                            $ Trigger2 = "kiss you"
                                                                            call Girl_FB_Prep #call expression Ch_Focus.Tag + "_FB_Prep"
                                                                        else:
                                                                            $ Trigger = "kiss you"
                                                                    else:
                                                                        "Когда ваши руки начинает двигаться вверх, она хватает их за запястья."
                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                                        #"I'm actually getting a little tired, so maybe we could wrap this up?"
                                                            "Переместить руку к ее бедрам. . ." if Ch_Focus.Kissed >= 1 and MultiAction:
                                                                    if Ch_Focus.Action and MultiAction:
                                                                        $ Situation = "auto"
                                                                        call Kiss_After
                                                                        call Girl_Fondle_Thighs #call expression Ch_Focus.Tag + "_Fondle_Thighs"
                                                                        if Trigger == "fondle thighs":
                                                                                $ Trigger2 = "kiss you"
                                                                                call Girl_FT_Prep #call expression Ch_Focus.Tag + "_FT_Prep"
                                                                        else:
                                                                                $ Trigger = "kiss you"
                                                                    else:
                                                                        "Когда ваши руки начинает двигаться вниз, она хватает их за запястья."
                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                                        #"I'm actually getting a little tired, so maybe we could wrap this up?"
                                                            "Неважно":
                                                                        jump KissCycle
                                                else:
                                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")
                                                                        #"I'm actually getting a little tired, so maybe we could wrap this up?"
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
                                                            jump KissCycle
                                                "Привести в порядок [Partner.Name_vin]":
                                                            call Girl_Cleanup(Partner,"ask")
                                                            #call Shift_Focus(Partner)
                                                            jump KissCycle
                                                "Неважно":
                                                            jump KissCycle
                                        "Раздеть [Ch_Focus.Name_vin]":
                                                call Girl_Undress(Ch_Focus)
                                        "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                                pass
                                        "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                                call Girl_Cleanup(Ch_Focus,"ask")
                                        "Неважно":
                                                jump KissCycle

                            "Вернуться к Секс-меню" if MultiAction and Ch_Focus.Kissed >= 5:
                                    ch_p "Давай попробуем что-нибудь другое."
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Kiss_After
                            "Закончить":
                                    ch_p "Давай пока остановимся."
                                    $ Line = 0
                                    jump Kiss_After
            #End menu (if Line)

#            call Shift_Focus(Girl)
            call Sex_Dialog(Ch_Focus,Partner)

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
                                if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2 and Ch_Focus.SEXP >= 20:
                                        $ Ch_Focus.RecentActions.append("unsatisfied")
                                        $ Ch_Focus.DailyActions.append("unsatisfied")
                                if Player.Focus > 80:
                                        jump Kiss_After
                                $ Line = "came"

                        if Ch_Focus.Lust >= 100:
                                #If you're still going at it and Rogue can cum
                                call Girl_Cumming(Ch_Focus)
                                if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                        jump Kiss_After

                        #If you came
                        if Line == "came": #ex Player.Focus <= 20:
                                #If you've just cum,
                                $ Line = 0
                                if not Player.Semen:
                                                    "Вы выдохлись, лучше пока остановиться."

                                if "unsatisfied" in Ch_Focus.RecentActions:#And Ch_Focus is unsatisfied,
                                    "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                                    menu:
                                        "Хотите завершить начатое?"
                                        "Продолжим еще немного.":
                                            $ Line = "Вы возвращаетесь к процессу"
                                        "С меня хватит.":
                                            "Вы отстраняетесь."
                                            jump Kiss_After

            if Partner and Partner.Lust >= 100:
                    #Checks if partner could orgasm
                    call Girl_Cumming(Partner)
            #End orgasm

            call Escalation(Ch_Focus) #sees if she wants to escalate things

            if Round == 10:
                    call Sex_Basic_Dialog(Ch_Focus,10) #"You might want to wrap this up, it's getting late."
            elif Round == 5:
                    call Sex_Basic_Dialog(Ch_Focus,5)   #"Seriously, it'll be time to stop soon."

        #Round = 0 loop breaks
        $ Ch_Focus.FaceChange("bemused", 0)
        $ Line = 0
        call Sex_Basic_Dialog(Ch_Focus,"done") #"Ok, [Ch_Focus.Petname], that's enough of that for now."

label Kiss_After: #rkeljsvgbdw
        # Modification mode
        $ play_music()
        $ play_sound()
        # -----------------

        $ Ch_Focus.FaceChange("sexy")

        $ Ch_Focus.Kissed += 1
        $ Ch_Focus.Action -=1
        $ Ch_Focus.Addictionrate += 2 if Ch_Focus.Addictionrate < 5 else 1
        $ Ch_Focus.Addictionrate += 1 if "addictive" in Player.Traits else 0

        call Partner_Like(Ch_Focus,1) #raises other girl's like levels if watching

        if "kissing" not in Ch_Focus.RecentActions:
                if Ch_Focus.Love > 300:
                        $ Ch_Focus.Statup("Love", 60, 4)
                $ Ch_Focus.Statup("Love", 70, 1)
                $ Ch_Focus.RecentActions.append("kissing")
                $ Ch_Focus.DailyActions.append("kissing")

        if Ch_Focus.Kissed > 10:
                pass
        elif Ch_Focus.Kissed == 10:
                $ Ch_Focus.FaceChange("smile", 1)
                if Ch_Focus is RogueX:
                        ch_r "Тебе, наверное, очень нравятся мои губки, да?"
                elif Ch_Focus is KittyX:
                        ch_k "Я могу тебя съесть."
                elif Ch_Focus is EmmaX:
                        ch_e "Это был приятный сюрприз."
                elif Ch_Focus is LauraX:
                        ch_l "Я могла бы делать это каждый день."
                elif Ch_Focus is JeanX:
                        if not Player.Male:
                            ch_j "Ты добилась серьезных успехов. . ."
                        else:
                            ch_j "Ты добился серьезных успехов. . ."
                        ch_j "Похоже, я хорошо на тебя влияю. . ."
                elif Ch_Focus is StormX:
                        ch_s "Мне очень нравится целовать тебя."
                elif Ch_Focus is JubesX:
                        ch_v "Мне нравится вкус твоих губ. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Я могу и привыкнуть к этому. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Это был лучший поцелуй в моей жизни. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Ты, эм, очень хорошо целуешься. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Знаешь, ты очень классно целуешься."
        elif Ch_Focus.Kissed == 5:
                if Ch_Focus is RogueX:
                        ch_r "Похоже, поцелуи входят у нас в привычку."
                elif Ch_Focus is KittyX:
                        ch_k "У тебя хорошо получается. . ."
                elif Ch_Focus is EmmaX:
                        if not Player.Male:
                            ch_e "Ты на удивление талантлива. . ."
                        else:
                            ch_e "Ты на удивление талантлив. . ."
                elif Ch_Focus is LauraX:
                        if not Player.Male:
                            ch_l "Ты очень талантлива. . ."
                        else:
                            ch_l "Ты очень талантлив. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Мммммм, все было хорошо. . ."
                elif Ch_Focus is StormX:
                        ch_s "Мммм, кто-нибудь говорил тебе, что ты довольно хорошо целуешься?"
                elif Ch_Focus is JubesX:
                        ch_v "Целовать тебя очень здорово!"
                elif Ch_Focus is GwenX:
                        ch_g "Мне всегда было интересно, на что похожи поцелуи в таких играх. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Знаешь, у тебя неплохо получается. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Мммм. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Я начинаю привыкать к этим ощущениям. . ."
        elif Ch_Focus.Kissed == 1:
            if Ch_Focus is JubesX:
                    "[Ch_Focus.Name] прикусывает слегка вашу губу, отстраняясь, и слизывает немного крови со своих губ."
                    ch_v "Извини. . ."
                    ch_v "Этого больше не повторится."
            elif Ch_Focus is GwenX:
                    ch_g "Ого, это было совсем уж реально. . ."
            $ Ch_Focus.SEXP += 1

        if not Situation and Ch_Focus.Kissed > 5 and Ch_Focus.Lust > 50 and ApprovalCheck(Ch_Focus, 950):
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Brows = "sad"
                if Ch_Focus is RogueX:
                        ch_r "Возможно, ты хочешь попробовать что-нибудь еще?"
                elif Ch_Focus is KittyX:
                        ch_k "И это все?"
                elif Ch_Focus is EmmaX:
                        ch_e "Может перейдем к чему-то большему? . ."
                elif Ch_Focus is LauraX:
                        ch_l "Хм, и это все чего ты хочешь?"
                elif Ch_Focus is JeanX:
                        ch_j "Это было приятно. . ."
                elif Ch_Focus is StormX:
                        ch_s "Ох. . . все прошло прекрасно."
                elif Ch_Focus is JubesX:
                        ch_v "Ты хочешь. . . большего?"
                elif Ch_Focus is GwenX:
                        ch_g "У тебя есть что-нибудь еще в планах? . ."
                elif Ch_Focus is BetsyX:
                        ch_b ". . . у тебя есть еще какие-нибудь идеи?"
                elif Ch_Focus is DoreenX:
                        ch_d "Это все, чего ты хочешь? . ."
                elif Ch_Focus is WandaX:
                        ch_w "Ты не хочешь чего-то большего? . ."
        $ Tempmod = 0
        if Situation:
                call Sex_Basic_Dialog(Ch_Focus,"shift") #"Mmm, so what else did you have in mind?"
        else:
                call Girl_Pos_Reset(Ch_Focus) #call expression Ch_Focus.Tag + "_Pos_Reset"
        call Checkout
        return
# End Makeout / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Massage / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Massage(Girl=0,Current=0,Past=0,MCount=0): #rkeljsvgbdw
#        $ Girl = GirlCheck(Girl)
#        call Shift_Focus(Girl)
        $ Tempmod = 0
        if "angry" in Ch_Focus.RecentActions:
                return

        $ Approval = ApprovalCheck(Ch_Focus, 500, TabM = 1) # 95, 110, 125 -120(215)

        if Ch_Focus is JeanX and not JeanX.Taboo:
                    $ Approval = 2
        if Approval >= 2:
                    $ Ch_Focus.FaceChange("bemused", 1)
                    if Ch_Focus.Forced:
                            $ Ch_Focus.FaceChange("sad")
                            $ Ch_Focus.Statup("Love", 20, -2, 1)
                            $ Ch_Focus.Statup("Obed", 90, 1)
                            $ Ch_Focus.Statup("Inbt", 60, 1)
                    if Ch_Focus is RogueX:
                            ch_r "Ладно, [Ch_Focus.Petname], конечно."
                    elif Ch_Focus is KittyX:
                            ch_k "Конечно, почему бы и нет."
                    elif Ch_Focus is EmmaX:
                            ch_e "Мне бы это не помешало, [Ch_Focus.Petname]."
                    elif Ch_Focus is LauraX:
                            ch_l "Думаю, мне не помешает массаж."
                    elif Ch_Focus is JeanX:
                            ch_j "Ох, Конечно, приступай."
                    elif Ch_Focus is StormX:
                            ch_s "Мне бы это не помешало."
                    elif Ch_Focus is JubesX:
                            ch_v "О, да, конечно."
                    elif Ch_Focus is GwenX:
                            ch_g "Лан. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Это было бы очень мило с твоей стороны."
                    elif Ch_Focus is DoreenX:
                            ch_d "Здорово!"
                    elif Ch_Focus is WandaX:
                            ch_w "Ох, ого, это было бы здорово. . ."
                    $ Ch_Focus.Statup("Love", 90, 1)
                    $ Ch_Focus.Statup("Inbt", 50, 3)
                    jump Massage_Prep

        else:
            $ Ch_Focus.FaceChange("angry", 1)
            if "no massage" in Ch_Focus.RecentActions:
                    if Ch_Focus is RogueX:
                            ch_r "Хех, я {i}только что{/i} сказала тебе \"нет,\" [Ch_Focus.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Да ладно, я {i}только что{/i} сказала тебе \"нет,\" [Ch_Focus.Petname]."
                    elif Ch_Focus is EmmaX:
                            ch_e "Я {i}только что{/i} отказала тебе, [Ch_Focus.Petname]."
                    elif Ch_Focus is LauraX:
                            ch_l "Я {i}только что{/i} отказала тебе, [Ch_Focus.Petname]."
                    elif Ch_Focus is JeanX:
                            ch_j "Я {i}только что{/i} сказала тебе \"нет,\"[Ch_Focus.Petname]."
                    elif Ch_Focus is StormX:
                            ch_s "Я ясно высказалась по этому вопросу."
                    elif Ch_Focus is JubesX:
                            ch_v "Ладно, ты можешь перестать спрашивать."
                    elif Ch_Focus is GwenX:
                            ch_g "Перестань спрашивать. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Я уже достаточно ясно выразилась."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я -только что- сказала тебе, что он мне не нужен."
                    elif Ch_Focus is WandaX:
                            ch_w "Я сказала, что он мне не нужен. . ."
            elif "no massage" in Ch_Focus.DailyActions:
                    if Ch_Focus is RogueX:
                            ch_r "Я уже сказала тебе \"нет\" ранее, [Ch_Focus.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Я уже сказала \"нет.\""
                    elif Ch_Focus is EmmaX:
                            ch_e "Я уже сказала тебе \"нет\" ранее, [Ch_Focus.Petname]."
                    elif Ch_Focus is LauraX:
                            ch_l "Я уже сказала тебе \"нет\" ранее, [Ch_Focus.Petname]."
                    elif Ch_Focus is JeanX:
                            ch_j "Я уже сказала тебе \"нет\" ранее, [Ch_Focus.Petname]."
                    elif Ch_Focus is StormX:
                            ch_s "Я уже отказалась ранее. И я не передумала."
                    elif Ch_Focus is JubesX:
                            ch_v "Серьезно, перестань спрашивать."
                    elif Ch_Focus is GwenX:
                            ch_g "Не сегодня. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Я уже достаточно ясно выразилась."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я же сказала тебе, что он мне не нужен."
                    elif Ch_Focus is WandaX:
                            ch_w "Я сказал, что он мне не нужен. . ."
            else:
                    $ Ch_Focus.FaceChange("bemused")
                    if Ch_Focus is RogueX:
                            ch_r "Я не знаю, не сейчас."
                    elif Ch_Focus is KittyX:
                            ch_k "Я не знаю, не сейчас."
                    elif Ch_Focus is EmmaX:
                            ch_e "Сейчас мне это не интересно, [Ch_Focus.Petname]."
                    elif Ch_Focus is LauraX:
                            ch_l "Сейчас мне это не интересно, [Ch_Focus.Petname]."
                    elif Ch_Focus is JeanX:
                            ch_j "Не сейчас."
                    elif Ch_Focus is StormX:
                            ch_s "Я, пожалуй, откажусь."
                    elif Ch_Focus is JubesX:
                            ch_v "Нее, мне и так хорошо."
                    elif Ch_Focus is GwenX:
                            ch_g "Нет, спасибо. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "В данный момент я не желаю массаж."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я не уверена, скорее нет. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Пожалуй, откажусь от этого предложения. . ."
            menu:
                extend ""
                "Извини, забудь." if "no massage" in Ch_Focus.DailyActions:
                        $ Ch_Focus.FaceChange("bemused")
                        if Ch_Focus is RogueX:
                                ch_r "Ладно, ничего страшного, [Ch_Focus.Petname]."
                        elif Ch_Focus is KittyX:
                                ch_k "Хорошо, [Ch_Focus.Petname]."
                        elif Ch_Focus is EmmaX:
                                ch_e "Не беспокойся, [Ch_Focus.Petname]."
                        elif Ch_Focus is LauraX:
                                ch_l "Не волнуйся."
                        elif Ch_Focus is JeanX:
                                ch_j "Все в порядке, может позже."
                        elif Ch_Focus is StormX:
                                ch_s "Ничего страшного не случилось."
                        elif Ch_Focus is JubesX:
                                ch_v "Не парься."
                        elif Ch_Focus is GwenX:
                                ch_g "Все нормально. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Ничего страшного."
                        elif Ch_Focus is DoreenX:
                                ch_d "Все хорошо. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Да все нормально. . ."
                        return
                "Может, в другой раз?" if "no massage" not in Ch_Focus.DailyActions:
                        $ Ch_Focus.FaceChange("sexy")
                        $ Ch_Focus.Statup("Love", 80, 1)
                        $ Ch_Focus.Statup("Inbt", 20, 1)
                        $ Ch_Focus.Statup("Obed", 20, 1)
                        if Ch_Focus is RogueX:
                                ch_r "Конечно, может быть."
                        elif Ch_Focus is KittyX:
                                ch_k "Ага, может быть."
                        elif Ch_Focus is EmmaX:
                                ch_e "Возможно."
                        elif Ch_Focus is LauraX:
                                ch_l "Может быть?"
                        elif Ch_Focus is JeanX:
                                ch_j "Возможно, ага."
                        elif Ch_Focus is StormX:
                                ch_s "Конечно, все возможно."
                        elif Ch_Focus is JubesX:
                                ch_v "Возможно, наверное."
                        elif Ch_Focus is GwenX:
                                ch_g "Не знаю, может быть. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Посмотрим."
                        elif Ch_Focus is DoreenX:
                                ch_d "Ну, может быть. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Посмотрим. . ."
                        $ Ch_Focus.RecentActions.append("no massage")
                        $ Ch_Focus.DailyActions.append("no massage")
                        return
                "Ну давай, пожалуйста?":
                    if Approval:
                        $ Ch_Focus.FaceChange("sexy")
                        $ Ch_Focus.Statup("Obed", 90, 1)
                        $ Ch_Focus.Statup("Obed", 40, 2)
                        $ Ch_Focus.Statup("Inbt", 30, 2)
                        if Ch_Focus is RogueX:
                                ch_r "Ну, если ты в таком отчаянии. . ."
                        elif Ch_Focus is KittyX:
                                ch_k "Думаю, мне не помешает немного расслабиться. . ."
                        elif Ch_Focus is EmmaX:
                                ch_e "У меня в самом деле накопилось напряжение. . ."
                        elif Ch_Focus is LauraX:
                                ch_l "Ладно, ладно. . ."
                        elif Ch_Focus is JeanX:
                                ch_j "Ох, хорошо."
                        elif Ch_Focus is StormX:
                                ch_s "Если ты настаиваешь. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Хорошо."
                        elif Ch_Focus is GwenX:
                                ch_g "Ох, как скажешь. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Ох, если так этого хочешь. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "Ну. . . ладно. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Ничего себе. . . ну ладно. . ."
                        jump Massage_Prep
                    else:
                        $ Ch_Focus.FaceChange("sexy")
                        if Ch_Focus is RogueX:
                                ch_r "Хех, нет спасибо, [Ch_Focus.Petname]."
                        elif Ch_Focus is KittyX:
                                ch_k "Хихи, извини, [Ch_Focus.Petname]."
                        else:
                                $ Ch_Focus.FaceChange("sly", Brows="confused")
                                call AnyLine(Ch_Focus,"Нет.")

        if "no massage" in Ch_Focus.DailyActions:
                if Ch_Focus is RogueX:
                        ch_r "Ты начинаешь меня раздражать, [Ch_Focus.Petname]."
                elif Ch_Focus is KittyX:
                        ch_k "Угадай мой ответ, [Ch_Focus.Petname]."
                elif Ch_Focus is EmmaX:
                        ch_e "Я уже дала тебе ясный ответ, [Ch_Focus.Petname]."
                elif Ch_Focus is LauraX:
                        ch_l "Я уже дала тебе ясный ответ, [Ch_Focus.Petname]."
                elif Ch_Focus is JeanX:
                        ch_j "Перестань спрашивать, это не весело."
                elif Ch_Focus is StormX:
                        ch_s "Я вряд ли когда-нибудь соглашусь."
                elif Ch_Focus is JubesX:
                        ch_v "Это становится очень странным."
                elif Ch_Focus is GwenX:
                        if not Player.Male:
                            ch_g "Ты странно настойчивая. . ."
                        else:
                            ch_g "Ты странно настойчивый. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Ты следует держать себя в руках."
                elif Ch_Focus is DoreenX:
                        ch_d "Послушай, я уже сказала тебе \"нет\". . ."
                elif Ch_Focus is WandaX:
                        ch_w "Мне сегодня не до этого. . ."
                $ Ch_Focus.RecentActions.append("angry")
                $ Ch_Focus.DailyActions.append("angry")
        elif Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("angry", 1)
                $ Ch_Focus.Statup("Lust", 60, 5)
                $ Ch_Focus.Statup("Obed", 50, -2)
                if Ch_Focus is RogueX:
                        if not Player.Male:
                            ch_r "Я не хочу, чтобы ты прикасалась ко мне."
                        else:
                            ch_r "Я не хочу, чтобы ты прикасался ко мне."
                elif Ch_Focus is KittyX:
                        ch_k "Это уже слишком."
                elif Ch_Focus is EmmaX:
                        ch_e "Держи руки при себе."
                elif Ch_Focus is LauraX:
                        ch_l "Держи руки при себе."
                elif Ch_Focus is JeanX:
                        ch_j "Даже не проси."
                elif Ch_Focus is StormX:
                        ch_s "Мне это не интересно."
                elif Ch_Focus is JubesX:
                        ch_v "Естественно нет."
                elif Ch_Focus is GwenX:
                        if not Player.Male:
                            ch_g "Я не хочу, чтобы ты касалась меня. . ."
                        else:
                            ch_g "Я не хочу, чтобы ты касался меня. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Мне не по себе от одной мысли об этом."
                elif Ch_Focus is DoreenX:
                        ch_d "Это, эм, немного жутко. . ."
                elif Ch_Focus is WandaX:
                        if not Player.Male:
                            ch_w "Я не желаю, чтобы ты прикасалась ко мне. . ."
                        else:
                            ch_w "Я не желаю, чтобы ты прикасался ко мне. . ."
                $ Ch_Focus.RecentActions.append("angry")
                $ Ch_Focus.DailyActions.append("angry")
        elif Ch_Focus.Taboo:
                $ Ch_Focus.FaceChange("angry", 1)
                if Ch_Focus is RogueX:
                        if not Player.Male:
                            ch_r "Я не хочу, чтобы ты прикасалась ко мне на людях."
                        else:
                            ch_r "Я не хочу, чтобы ты прикасался ко мне на людях."
                elif Ch_Focus is KittyX:
                        ch_k "Не[Ch_Focus.like]на людях."
                elif Ch_Focus is EmmaX:
                        ch_e "Меня не должны увидеть, занимающейся подобным."
                elif Ch_Focus is LauraX:
                        ch_l "Я стараюсь не привлекать внимания."
                elif Ch_Focus is JeanX:
                        ch_j "Я не хочу, чтобы меня видели во время массажа. . ."
                elif Ch_Focus is StormX:
                        ch_s "Люди неправильно все поймут."
                elif Ch_Focus is JubesX:
                        ch_v "Здесь слишком людно. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Я не хочу создавать проблем. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Это совершенно неуместно."
                elif Ch_Focus is DoreenX:
                        ch_d "Я бы не хотела делать этого здесь. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Здесь не место для этого. . ."
        else:
                $ Ch_Focus.FaceChange("sexy")
                $ Ch_Focus.Mouth = "sad"
                if Ch_Focus is RogueX:
                        ch_r "Серьезно, я не могу, [Ch_Focus.Petname]."
                elif Ch_Focus is KittyX:
                        ch_k "Серьезно, я не могу!"
                elif Ch_Focus is EmmaX:
                        ch_e "Я правда не могу."
                elif Ch_Focus is LauraX:
                        ch_l "Мне это не по душе."
                elif Ch_Focus is JeanX:
                        ch_j "Отойди."
                elif Ch_Focus is StormX:
                        ch_s "Остановись."
                elif Ch_Focus is JubesX:
                        ch_v "Ни за что."
                elif Ch_Focus is GwenX:
                        ch_g "Неа. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Я вынуждена отказаться."
                elif Ch_Focus is DoreenX:
                        ch_d "Извини. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Прости. . ."
        $ Ch_Focus.RecentActions.append("no massage")
        $ Ch_Focus.DailyActions.append("no massage")
        $ Tempmod = 0
        return

label Massage_Prep(Current=0,Past=0,MCount=0): #rkeljsvgbdw label Massage_Prep(Girl=Ch_Focus,Current=0,Past=0,MCount=0):
        call Top_Off(Ch_Focus,"massage")
        if not Ch_Focus.Over and "no topless" not in Ch_Focus.RecentActions:
                        $ Ch_Focus.Statup("Obed", 50, 3)
                        $ Ch_Focus.Statup("Inbt", 50, 3)
        elif Ch_Focus.Forced and "drugfree" not in Ch_Focus.RecentActions:
                #if it was during an addiction session or something. . .
                if "no topless" in Ch_Focus.RecentActions:
                        if Ch_Focus is RogueX:
                                ch_r "Послушай, одежда нам никак не помешает."
                        elif Ch_Focus is KittyX:
                                ch_k "Мы можем заняться этим даже с одеждой. . ."
                        elif Ch_Focus is EmmaX:
                                ch_e "Я думаю, мы справимся и с надетой одеждой. . ."
                        elif Ch_Focus is LauraX:
                                ch_l "Мы справимся и так. . ."
                        elif Ch_Focus is JeanX:
                                ch_j "Чего ты ждешь? Можешь приступать."
                        elif Ch_Focus is StormX:
                                ch_s "Обсудим прямой контакт в другой раз."
                        elif Ch_Focus is JubesX:
                                ch_v "Я бы предпочла оставить верх надетым."
                        elif Ch_Focus is GwenX:
                                ch_g "Но, эм, Я бы хотела остаться в верхней одежде. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Можешь приступать, но одежда останется на мне."
                        elif Ch_Focus is DoreenX:
                                ch_d "Я не буду ничего снимать, ладно?"
                        elif Ch_Focus is WandaX:
                                ch_w "Можешь приступать. . ."
                        menu:
                            extend ""
                            "Ладно.":
                                    $ Ch_Focus.Statup("Obed", 50, 5)
                                    $ Ch_Focus.Statup("Inbt", 50, 5)
                            "Нет, оно того не стоит.":
                                    if Ch_Focus is RogueX:
                                            ch_r "Ну хорошо! Что-нибудь еще?"
                                    elif Ch_Focus is KittyX:
                                            ch_k "Прекрасно!"
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Какая жалость. Еще есть идеи?"
                                    elif Ch_Focus is LauraX:
                                            ch_l "Ладно."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Справедливо."
                                    elif Ch_Focus is StormX:
                                            ch_s "Отлично."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Нуу, ладно, пусть будет так."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Оу. . ."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Ну хорошо."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Ох. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Ладно. . ."
                                    return
                else:
                        $ Ch_Focus.Statup("Obed", 50, 5)
                        $ Ch_Focus.Statup("Inbt", 50, 5)
                        if Ch_Focus is RogueX:
                                ch_r "Хорошо, но после того, как мы закончим, я тоже немного потрогаю тебя."
                        elif Ch_Focus is KittyX:
                                ch_k "Конечно, но после мне все равно нужно будет прикоснуться к тебе."
                        elif Ch_Focus is EmmaX:
                                ch_e "Хорошо, но мне все равно понадобится потрогать тебя."
                        elif Ch_Focus is LauraX:
                                ch_l "Да, но потом мне нужно будет прикоснуться к тебе тоже."
                        elif Ch_Focus is StormX:
                                ch_s "Я согласна, пока я могу прикоснуться к тебе. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Но знаешь, после мне нужен будет какой-нибудь контакт."
                                if Ch_Focus.Acc and Ch_Focus.Over:
                                        $ Ch_Focus.Acc = 0
                                        "Однако она все же снимает куртку."
                        elif Ch_Focus is GwenX:
                                ch_g "Но потом мне понадобится прикоснуться к тебе. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Однако после мне понадобится прикоснуться к тебе."
                        elif Ch_Focus is DoreenX:
                                ch_d "Но после мне понадобится быстренько прикоснуться к тебе. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Ага, но мне тоже надо будет потом прикоснуться к тебе. . ."
        if Ch_Focus not in (1,2):   #removes girls without a doggy pose
                call AnyLine(Ch_Focus,"Мне развернуться?")
                menu:
                    extend ""
                    "Да":
                            $ Ch_Focus.Pose = "doggy"
                    "Нет":
                            pass

                call AnyLine(Ch_Focus,"Ладно.")
        if "angry" in Ch_Focus.RecentActions:
                return

label Massage_Cycle: #rkeljsvgbdw
        #Current is the current action, past is the previous action, MCount is progress along the character track

        $ Ch_Focus.AddWord(1,"massage","massage",0,0) #adds "word" to Recent, Daily

        if Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex":
                call expression Ch_Focus.Tag + "_Sex_Launch" pass ("massage")

        $ Trigger = "massage"

        while Round >= 10 and MCount < 10:
#                call Shift_Focus(Girl)
                $ Ch_Focus.LustFace()

                call ViewShift(Ch_Focus,Ch_Focus.Pose,0)

                # Modification mode
                $ MassageBestChoice = Ch_Focus.MassageChart[MCount]
                menu Massage_Choices:
                    "К чему будете прикасаться?"
                    "{color=#FAAFBE}([MassageBestChoice])"
                # -----------------
                    "Верхняя часть тела":
                        menu:
                            "Шея":
                                    $ Past = Current
                                    $ Current = "neck"
                            "Плечи":
                                    $ Past = Current
                                    $ Current = "shoulders"
                            "Спина":
                                    $ Past = Current
                                    $ Current = "back"
                            "Грудь":
                                    $ Past = Current
                                    $ Current = "breasts"
                            "Локти":
                                    $ Past = Current
                                    $ Current = "arms"
                            "Ладони":
                                    $ Past = Current
                                    $ Current = "hands"
                            "Назад":
                                    jump Massage_Choices
                    "Нижняя часть тела":
                        menu:
                            "Внешняя часть бедер":
                                    $ Past = Current
                                    $ Current = "hips"
                            "Попа":
                                    $ Past = Current
                                    $ Current = "ass"
                            "Киска":
                                    $ Past = Current
                                    $ Current = "pussy"
                            "Внутренняя часть бедер":
                                    $ Past = Current
                                    $ Current = "thighs"
                            "Икры":
                                    $ Past = Current
                                    $ Current = "calves"
                            "Стопы":
                                    $ Past = Current
                                    $ Current = "feet"
                            "Назад":
                                    jump Massage_Choices
                    "Шея" if Current in ("neck","shoulders","back"):
                            $ Past = Current
                            $ Current = "neck"
                    "Плечи" if Current in ("neck","shoulders","back","arms"):
                            $ Past = Current
                            $ Current = "shoulders"
                    "Спина" if Current in ("neck","shoulders","back","breasts","hips"):
                            $ Past = Current
                            $ Current = "back"
                    "Грудь" if Current in ("breasts","back"):
                            $ Past = Current
                            $ Current = "breasts"
                    "Локти" if Current in ("shoulders","arms","hands"):
                            $ Past = Current
                            $ Current = "arms"
                    "Ладони" if Current in ("arms","hands"):
                            $ Past = Current
                            $ Current = "hands"
                    "Внешняя часть бедер" if Current in ("back","hips","ass","pussy","thighs"):
                            $ Past = Current
                            $ Current = "hips"
                    "Попа" if Current in ("back","hips","ass","pussy","thighs"):
                            $ Past = Current
                            $ Current = "ass"
                    "Киска" if Current in ("hips","ass","pussy","thighs"):
                            $ Past = Current
                            $ Current = "pussy"
                    "Внутренняя часть бедер" if Current in ("hips","ass","pussy","thighs","calves"):
                            $ Past = Current
                            $ Current = "thighs"
                    "Икры" if Current in ("thighs","calves","feet"):
                            $ Past = Current
                            $ Current = "calves"
                    "Стопы" if Current in ("calves","feet"):
                            $ Past = Current
                            $ Current = "feet"
                    "Одежда":
                            call Girl_Undress(Ch_Focus)
                            jump Massage_Choices
                    "У меня нет на это времени. [[Автоматически]":
                            menu:
                                "Просто сделать небольшой массаж и закончить?"
                                "Ага [[Авто завершение]":
                                        "Ладно."
                                        "Вы просто делаете быстрый массаж, затрагивая все основные области и прорабатывая ее мышцы."
                                        $ D20 = renpy.random.randint(2,5)
                                        $ Ch_Focus.Addict -= (10 + (4*D20)) #18-30
                                        $ MCount = D20 # 2-5
                                        $ Ch_Focus.Lust += (5 * D20) # 10-25
                                        $ Round -= 30
                                        $ Round = 5 if Round < 5 else Round
                                        jump Massage_After
                                "Нет [[Все сделать самостоятельно]":
                                        jump Massage_Cycle


                    "Сменить вид":
                            call ViewShift(Ch_Focus,"menu")
                            jump Massage_Cycle
                    "Остановиться":
                        jump Massage_After
                #end menu

                if Ch_Focus.Pose == "doggy" or Ch_Focus.Pose == "sex":
                        if Current in ("calves","feet"):
                                $ ShowFeet = 1
                        else:
                                $ ShowFeet = 0
                        #add feet display to this if Current == "feet"
                elif Current in ("neck","shoulders","back","breasts","arms","hands"):
                        $ Ch_Focus.Pose = "breasts"
                elif Current in ("hips","ass","pussy","thighs"):
                        $ Ch_Focus.Pose = "pussy"

                call ViewShift(Ch_Focus,Ch_Focus.Pose,0)

                if Current == "neck":
                        if Past in ("shoulders","back"):
                                $ Line = "Вы скользите своими руками к шее " +Ch_Focus.Name_rod
                                $ Check = 400
                        else:
                                $ Line = "Вы начинаете массировать шею " +Ch_Focus.Name_rod
                                $ Check = 500

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 60, 2)
                                $ Ch_Focus.Statup("Lust", 90, 1)
                                if Past == Current:
                                        $ Ch_Focus.Statup("Lust", 90, 2)
                                        "Вы впиваетесь руками в мышцы ее шеи, от чего она издает долгий стон удовольствия."
                                else:
                                        "[Line]. Она вытягивается от явного удовольствия."
                        #end neck
                        $ Ch_Focus.Addict -= 2
                elif Current == "shoulders":
                        if Past in ("back","neck","arms"):
                                $ Line = "Вы скользите своими руками к плечам " +Ch_Focus.Name_rod
                                $ Check = 400
                        else:
                                $ Line = "Вы начинаете массировать ее плечи " +Ch_Focus.Name_rod
                                $ Check = 500

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 60, 2)
                                $ Ch_Focus.Statup("Lust", 90, 2)
                                if Past == Current:
                                        $ Ch_Focus.Statup("Lust", 90, 2)
                                        "Вы впиваетесь в ее плечи, от чего она начинает извиваться и постанывать."
                                else:
                                        "[Line]. Она вытягивается от явного удовольствия."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "Вы продолжаете массировать плечи " +Ch_Focus.Name_rod
                        #end shoulders
                        if not Ch_Focus.Over:
                                $ Ch_Focus.Addict -= 3
                elif Current == "back":
                        if Past in ("neck","shoulders","breasts","hips"):
                                $ Line = "Вы скользите своими руками к спине " +Ch_Focus.Name_rod
                                $ Check = 400
                        else:
                                $ Line = "Вы начинаете массировать спину " +Ch_Focus.Name_rod
                                $ Check = 500

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 60, 2)
                                $ Ch_Focus.Statup("Lust", 90, 2)
                                if Past == Current:
                                        $ Ch_Focus.Statup("Lust", 90, 2)
                                        "Вы впиваетесь в мышцы ее спины, из-за чего она издает долгий стон удовольствия."
                                else:
                                        "[Line]. Она стонет и вытягивается от удовольствия."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "Вы продолжаете массировать спину " +Ch_Focus.Name_rod
                        #end back
                        if not Ch_Focus.Over:
                                $ Ch_Focus.Addict -= 2
                        if not Ch_Focus.Chest:
                                $ Ch_Focus.Addict -= 2
                elif Current == "breasts":
                        if Past == "back":
                                $ Line = "Вы ведете свои руки к грудям " +Ch_Focus.Name_rod+ ", а затем хватаете их"
                                $ Check = 1000
                        else:
                                $ Line = "Вы берете груди " +Ch_Focus.Name_rod+ " в свои ладони"
                                $ Check = 1050

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 60, 1)
                                $ Ch_Focus.Statup("Lust", 90, 2)
                                $ Ch_Focus.Statup("Lust", 200, 3)
                                if Past == Current:
                                        $ Ch_Focus.Statup("Lust", 200, 2)
                                        "Вы уверенно разминаете ее груди, она тихонько стонет."
                                else:
                                        "[Line]. Ее соски твердеют в ваших ладонях."
                        elif Past == Current:
                                $ Check = 1050
                                $ Ch_Focus.Statup("Lust", 200, 2)
                                $ Line = "Вы продолжаете массировать грудь " +Ch_Focus.Name_rod
                        #end breasts
                        if not Ch_Focus.Over and not Ch_Focus.Chest:
                                $ Ch_Focus.Addict -= 5
                elif Current == "arms":
                        if Past == "shoulders":
                                $ Line = "Вы скользите руками вниз к локтям " +Ch_Focus.Name_rod
                                $ Check = 400
                        elif Past == "hands":
                                $ Line = "Вы скользите руками вверх к локтям " +Ch_Focus.Name_rod
                                $ Check = 400
                        else:
                                $ Line = "Вы начинаете массировать руки " +Ch_Focus.Name_rod
                                $ Check = 500

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 60, 2)
                                $ Ch_Focus.Statup("Lust", 90, 1)
                                if Past == Current:
                                        $ Ch_Focus.Statup("Lust", 90, 2)
                                        "Вы с усилием массируете ее руки."
                                else:
                                        "[Line]. Ее руки непроизвольно сгибаются, от удовольствия у нее вырывается стон."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "Вы продолжаете массировать руки " +Ch_Focus.Name_rod
                        #end arms
                        if Ch_Focus.Over not in ("mesh top","pink top","jacket"):
                                $ Ch_Focus.Addict -= 3
                elif Current == "hands":
                        if Past == "arms":
                                $ Line = "Вы скользите руками вниз к ладоням " +Ch_Focus.Name_rod
                                $ Check = 400
                        else:
                                $ Line = "Вы берете ладони " +Ch_Focus.Name_rod+ " в свои и начинаете их массировать"
                                $ Check = 500

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 70, 2)
                                if Past == Current:
                                        $ Ch_Focus.Statup("Lust", 70, 2)
                                        "Вы растягиваете каждый палец и растираете суставы. Она слегка вздыхает."
                                else:
                                        "[Line]. Ее пальцы сгибаются от удовольствия."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "Вы продолжаете массировать ладони " +Ch_Focus.Name_rod
                        #end hands
                        $ Ch_Focus.Addict -= 3
                elif Current == "hips":
                        if Past == "Назад":
                                $ Line = "Вы скользите руками вниз к внешней части бедер " +Ch_Focus.Name_rod
                                $ Check = 400
                        elif Past in ("ass","pussy","thighs"):
                                $ Line = "Вы скользите руками вверх к внешней части бедер " +Ch_Focus.Name_rod
                                $ Check = 400
                        else:
                                $ Line = "Вы начинаете массировать бедра " +Ch_Focus.Name_rod
                                $ Check = 500

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 60, 2)
                                $ Ch_Focus.Statup("Lust", 90, 1)
                                if Past == Current:
                                        "Вы впиваетесь руками в ее бедра и она издает долгий стон удовольствия."
                                else:
                                        "[Line]. Ее спина выгибается от явного удовольствия."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "Вы продолжаете массировать бедра " +Ch_Focus.Name_rod
                        #end hips
                        if not Ch_Focus.Legs and Ch_Focus.HoseNum() < 10:
                                $ Ch_Focus.Addict -= 1
                elif Current == "ass":
                        if Past in ("back","hips"):
                                $ Line = "Вы скользите руками вниз к попке " +Ch_Focus.Name_rod
                                $ Check = 900
                        elif Past in ("pussy","thighs"):
                                $ Line = "Вы скользите руками вверх к попке " +Ch_Focus.Name_rod
                                $ Check = 900
                        else:
                                $ Line = "Вы начинаете массировать попку " +Ch_Focus.Name_rod
                                $ Check = 950

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 60, 2)
                                $ Ch_Focus.Statup("Lust", 90, 1)
                                $ Ch_Focus.Statup("Lust", 200, 3)
                                if Past == Current:
                                        $ Ch_Focus.Statup("Lust", 200, 2)
                                        "Вы массируете ее попку волнообразными движениями, ее спина выгибаться от удовольствия."
                                else:
                                        "[Line]. Ее мышцы напрягаются и расслабляются, пока вы массируете их."
                        elif Past == Current:
                                $ Check = 950
                                $ Ch_Focus.Statup("Lust", 90, 2)
                                $ Line = "Вы продолжаете массировать попку " +Ch_Focus.Name_rod
                        #end ass
                        if not Ch_Focus.Legs and not Ch_Focus.Panties and Ch_Focus.HoseNum() < 10:
                                $ Ch_Focus.Addict -= 3
                elif Current == "pussy":
                        if Past in ("hips","ass"):
                                $ Line = "Вы скользите своими руками к киске " +Ch_Focus.Name_rod
                                $ Check = 1200
                        elif Past == "thighs":
                                $ Line = "Вы скользите руками вверх к киске " +Ch_Focus.Name_rod
                                $ Check = 1100
                        else:
                                $ Line = "Вы начинаете массировать киску " +Ch_Focus.Name_rod
                                $ Check = 1200

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 60, 2)
                                $ Ch_Focus.Statup("Lust", 90, 2)
                                $ Ch_Focus.Statup("Lust", 200, 3)
                                if Past == Current:
                                        $ Ch_Focus.Statup("Lust", 200, 5)
                                        "Вы проводите большими пальцами по ее клитору, она вздрагивает от удовольствия."
                                else:
                                        "[Line]. Она с тихим стоном выгибает спину от удовольствия."
                        elif Past == Current:
                                $ Check = 1200
                                $ Ch_Focus.Statup("Lust", 200, 3)
                                $ Line = "Вы продолжаете массировать киску " +Ch_Focus.Name_rod
                        #end pussy
                        if not Ch_Focus.Legs and not Ch_Focus.Panties and Ch_Focus.HoseNum() < 10:
                                $ Ch_Focus.Addict -= 5
                elif Current == "thighs":
                        if Past == "calves":
                                $ Line = "ы скользите руками вверх к внутренней части бедер " +Ch_Focus.Name_rod
                                $ Check = 500
                        elif Past in ("hips","ass","pussy"):
                                $ Line = "Вы скользите руками вниз к внутренней части бедер " +Ch_Focus.Name_rod
                                $ Check = 400
                        else:
                                $ Line = "Вы начинаете массировать внутреннюю часть бедер " +Ch_Focus.Name_rod
                                $ Check = 600

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 60, 2)
                                $ Ch_Focus.Statup("Lust", 90, 1)
                                if Past == Current:
                                        $ Ch_Focus.Statup("Lust", 60, 1)
                                        "Вы с нажимом массируете ее бедро, она начинает стонать от удовольствия."
                                else:
                                        "[Line]. Ее ноги вытягиваются от явного удовольствия."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "Вы продолжаете массировать внутреннюю часть бедер " +Ch_Focus.Name_rod
                        #end thighs
                        if Ch_Focus.PantsNum() <= 6 and Ch_Focus.HoseNum() < 10:
                                $ Ch_Focus.Addict -= 3
                elif Current == "calves":
                        if Past == "feet":
                                $ Line = "Вы скользите руками вверх и начинаете гладить икры " +Ch_Focus.Name_rod
                                $ Check = 400
                        elif Past == "thighs":
                                $ Line = "Вы скользите руками к икрам " +Ch_Focus.Name_rod
                                $ Check = 400
                        else:
                                $ Line = "Вы начинаете массировать икры " +Ch_Focus.Name_rod
                                $ Check = 500

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 60, 2)
                                $ Ch_Focus.Statup("Lust", 90, 1)
                                if Past == Current:
                                        $ Ch_Focus.Statup("Lust", 60, 1)
                                        "Вы растираете ее лодыжки вперед и назад, расслабляя напряженные икры."
                                else:
                                        "[Line]. Она удовлетворенно сгибает пальцы ног."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "Вы продолжаете массаж икр " +Ch_Focus.Name_rod
                        #end calves
                        if Ch_Focus.PantsNum() <= 6 and Ch_Focus.HoseNum() < 10:
                                $ Ch_Focus.Addict -= 2
                elif Current == "feet":
                        if Past == "calves":
                                $ Line = "Вы скользите руками вниз к стопам " +Ch_Focus.Name_rod
                                $ Check = 400
                        else:
                                $ Line = "Вы начинаете массировать ее стопы " +Ch_Focus.Name_rod
                                $ Check = 600

                        if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                                # really likes it
                                $ Ch_Focus.Statup("Lust", 60, 2)
                                $ Ch_Focus.Statup("Lust", 90, 1)
                                if Past == Current:
                                        $ Ch_Focus.Statup("Lust", 90, 2)
                                        "Вы глубоко вдавливаете большие пальцы во внутреннюю часть ее стоп, ее пальцы ног вытягиваются от удовольствия."
                                else:
                                        "[Line]. Она вытягивает пальцы ног, тихонько постанывая."
                        elif Past == Current:
                                $ Check = 600
                                $ Line = "Вы продолжаете массировать стопы " +Ch_Focus.Name_rod
                        #end feet
                        if not Ch_Focus.Boots and Ch_Focus.HoseNum() < 10:
                                $ Ch_Focus.Addict -= 3
                # end primary checks

                # reaction checks
                if Ch_Focus.MassageChart[MCount] == Current and ApprovalCheck(Ch_Focus, Check):
                        # really likes it, we've covered this above
                        if Ch_Focus is JeanX:
                                $ Ch_Focus.Statup("Love", 60, 1)
                                $ Ch_Focus.Statup("Obed", 30, 1)
                elif ApprovalCheck(Ch_Focus, Check):
                        #kinda likes it
                        $ Line = Line + renpy.random.choice([". Она слегка извивается от удовольствия.",
                                ". Она начинает тихонько мурлыкать.",
                                ". Похоже, ей это очень нравится.",
                                ". Кажется, ей это нравится.",
                                ". Она начинает тихонько мурлыкать от удовольствия."])
                        $ Ch_Focus.Statup("Lust", 60, 2)
                        $ Ch_Focus.Statup("Lust", 90, 1)
                        "[Line]"
                        if Current == Past and Current in ("breasts","ass","pussy"):
                                #want to get a better grip on that?
                                #jump to the fondling activity
                                call Massage_After
                                $ Ch_Focus.Action += 1
                                if Current == "breasts":
                                        call Girl_FB_Prep #call expression Ch_Focus.Tag + "_FB_Prep"
                                elif Current == "ass":
                                        call Girl_FA_Prep #call expression Ch_Focus.Tag + "_FA_Prep"
                                elif Current == "pussy":
                                        call Girl_FP_Prep #call expression Ch_Focus.Tag + "_FP_Prep"
                                return
                elif ApprovalCheck(Ch_Focus, Check-200) or "massagefail" in Ch_Focus.RecentActions:
                        # dislikes it
                        $ Line = Line + renpy.random.choice([". Она слегка напряжена.",
                                ". Похоже, ей это не особо нравится.",
                                ". Ей это не нравится.",
                                ". Она цокает языком от раздражения."])
                        $ Ch_Focus.Statup("Lust", 60, -1)
                        $ Ch_Focus.Statup("Lust", 90, -2)
                        "[Line]"
                        if Current == Past and Current in ("breasts","ass","pussy"):
                                #could you cut that out?
                                call Massage_BadEnd
                                menu:
                                    extend ""
                                    "Ага, извини":
                                            "Вы одергиваете руки."
                                            $ Past = Current
                                            $ Current = 0
                                    "Мне все нравится":
                                            $ Ch_Focus.AddWord(1,"massagefail")
                                            jump Massage_BadEnd
                        $ Ch_Focus.AddWord(1,"massagefail")
                else:
                        # hates it
                        "[Line]. Она напрягается и садится."
                        $ Ch_Focus.AddWord(1,"massagefail")
                        jump Massage_BadEnd

                $ Round -= 6
                if Ch_Focus.MassageChart[MCount] == Current:
                        # advances progress along the track so long as you've hit the target
                        if MCount == 2:
                                "Вы чувствуете, что у вас все получается, что бы вы ни делали, это работает."
                        elif MCount == 7:
                                "Кажется, ее все устраивает, она чуть ли не мурлыкает."
                        $ MCount += 1

                #decides whether she wants to do a self-action. . .

                if not Ch_Focus.Taboo :
                        #if not in public. . .
                        $ Trigger = "massage"
                        $ Line = 0
                        call Girl_Self_Lines(Ch_Focus,Ch_Focus.Offhand)
                        if Line:
#                                $ Line3 = Line + "."
                                "[Line]."

                $ Player.Focus = 50 if (not Player.Semen and Player.Focus >= 50) else Player.Focus #Resets Player.Focus if can't get it up
                $ Player.Focus = 80 if (Player.Focus >= 80 and Ch_Focus.Offhand != "hand") else Player.Focus #Resets Player.Focus if higher than 80

                if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                            #If either of you can cum:
                            if Player.Focus >= 100:
                                    #If you can cum:
                                    call Player_Cumming(Ch_Focus)
                                    if "angry" in Ch_Focus.RecentActions:
                                            call Girl_Pos_Reset(Ch_Focus,0) #call expression Ch_Focus.Tag + "_Pos_Reset" pass (0)
                                            call Girl_Pos_Reset(Partner,0) #call expression Partner.Tag + "_Pos_Reset" pass (0)
                                            return
                                    $ Ch_Focus.Statup("Lust", 200, 5)
                                    if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                            $ Ch_Focus.RecentActions.append("unsatisfied")
                                            $ Ch_Focus.DailyActions.append("unsatisfied")
                                    $ Line = "came"

                            if Ch_Focus.Lust >= 100:
                                    #If the lead Girl can cum
                                    if ApprovalCheck(Ch_Focus, 1000, TabM = 1):
                                            call Girl_Cumming(Ch_Focus)
                                    else:
                                            call Girl_Cumming(Ch_Focus,1) #quick version
                                            $ Ch_Focus.FaceChange("bemused",2,Eyes="side")
                                            if Ch_Focus is RogueX:
                                                    ch_r "Ох. . . вау. . . эм. . ."
                                                    ch_r "Это было приятно. . ."
                                            elif Ch_Focus is KittyX:
                                                    ch_k ". . ."
                                                    ch_k "Это было. . . просто. . ."
                                                    ch_k "Вообщем, тут не к чему придраться. . ."
                                            elif Ch_Focus is EmmaX:
                                                    ch_e ". . ."
                                                    ch_e "Я не уверена, что ты думаешь по этому поводу, но не зазнавайся."
                                            elif Ch_Focus is LauraX:
                                                    ch_l "Хм. . ."
                                                    $ Ch_Focus.FaceChange("sexy",1)
                                                    ch_l "Хорошая работа."
                                            elif Ch_Focus is JeanX:
                                                    ch_j "Вау, ты прямо знаешь, что делаешь. . ."
                                                    if Ch_Focus.Org < 2:
                                                        $ Ch_Focus.Statup("Love", 80, 2)
                                                        $ Ch_Focus.Statup("Obed", 50, 2)
                                            elif Ch_Focus is StormX:
                                                    ch_s ". . ."
                                                    ch_s "Что ж, я удивлена. . ."
                                                    ch_s "Ты делаешь очень хороший массаж."
                                            elif Ch_Focus is JubesX:
                                                    ch_v "Ох!"
                                                    ch_v "Эм. . ."
                                                    ch_v "Ага, это было великолепно."
                                            elif Ch_Focus is GwenX:
                                                    ch_g "Воу. . ."
                                                    ch_g ". . ."
                                                    if not Player.Male:
                                                        ch_g "Эм. . . хорошая работа. . . мэм."
                                                    else:
                                                        ch_g "Эм. . . хорошая работа. . . сэр."
                                            elif Ch_Focus is BetsyX:
                                                    ch_b "Ох. . . боже."
                                                    ch_b "Это было. . . довольно впечатляюще. . ."
                                            elif Ch_Focus is DoreenX:
                                                    ch_d "Ох- оооооххххх. . ."
                                                    ch_d "Это просто. . . вау, у тебя очень умелые руки."
                                            elif Ch_Focus is WandaX:
                                                    ch_w "Ооох. . ."
                                                    ch_w "Ого. . ."
                                                    ch_w "Мне, эм. . . Мне понравилось."
                                            $ Ch_Focus.FaceChange("sexy",1)

                                    jump Massage_After

                            if Line == "came":
                                    $ Line = 0
                                    if not Player.Semen:
                                            "Вы опустошены, вам, вероятно, следует сделать перерыв."
                if Partner and Partner.Lust >= 100:
                        #Checks if partner could orgasm
                        call Girl_Cumming(Partner)
                #End orgasm

                if Check >= 1000:
                            #if you touched a no-no area
                            call expression Ch_Focus.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

                #End loop
label Massage_After: #rkeljsvgbdw
        call Girl_Pos_Reset(Ch_Focus,0) #call expression Ch_Focus.Tag + "_Pos_Reset" pass (0)
        if MCount >= 3:
                $ Ch_Focus.Statup("Love", 90, 1)
                $ Ch_Focus.Statup("Love", 50, 2)
                $ Ch_Focus.Statup("Obed", 30, 2)

        $ Ch_Focus.Massage += 1
        $ Ch_Focus.Action -= 1
        $ Ch_Focus.Addictionrate += 2 if Ch_Focus.Addictionrate < 5 else Ch_Focus.Addictionrate
        if "addictive" in Player.Traits:
                $ Ch_Focus.Addictionrate += 1

        $ Ch_Focus.FaceChange("smile",1)
        if MCount == 10 and not Ch_Focus.Forced:
                #you bowled her over
                if Ch_Focus is RogueX:
                        ch_r "Мммм, это так замечааааательно, [Ch_Focus.Petname]!"
                        ch_r "У тебя есть еще что-нибудь в планах?"
                elif Ch_Focus is KittyX:
                        ch_k "Ваааау, [Ch_Focus.Petname], это было потрясающе!"
                        ch_k "Что у тебя еще в планах?"
                elif Ch_Focus is EmmaX:
                        ch_e ". . ."
                        ch_e "Невероятно, [Ch_Focus.Petname]."
                        ch_e "Ты хочешь. . . продолжить?"
                elif Ch_Focus is LauraX:
                        ch_l "Мммм, [Ch_Focus.Petname], это было здорово!"
                        ch_l "Все было потрясающе, чем - нибудь еще займемся?"
                elif Ch_Focus is JeanX:
                        ch_j "Ммм. . . это было потрясающе!"
                        $ Ch_Focus.Statup("Love", 80, 2)
                        $ Ch_Focus.Statup("Love", 50, 2)
                        $ Ch_Focus.Statup("Obed", 50, 2)
                        ch_j "У тебя есть другие планы?"
                elif Ch_Focus is StormX:
                        ch_s "Это был поистине исключительный массаж, [Ch_Focus.Petname]."
                        ch_s "Нужно как-нибудь повторить."
                elif Ch_Focus is JubesX:
                        ch_v "Это на самом деле помогло. . ."
                        ch_v "Голова, плечи, колени, пальцы ног. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Это было очень. . . эффективно. . ."
                        ch_g "Я теперь такая. . . гибкая. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Ох. . . дорогуша."
                        ch_b "Это было. . . невероятно. . ."
                        ch_b "С такими руками у тебя большое будущее."
                elif Ch_Focus is DoreenX:
                        if not Player.Male:
                            ch_d "Ты -невероятно- хороша!"
                        else:
                            ch_d "Ты -невероятно- хорош!"
                        ch_d "Мне, эм. . . очень понравилось. Очень."
                elif Ch_Focus is WandaX:
                        ch_w "Вау. . . ничего себе. . ."
                        ch_w "У тебя. . .  волшебные прикосновения. . ."
        elif Ch_Focus.Massage == 1:
                #first time
                if Ch_Focus is RogueX:
                        ch_r "Это было очень расслабляюще, [Ch_Focus.Petname]."
                elif Ch_Focus is KittyX:
                        ch_k "Это было так прияяятно, [Ch_Focus.Petname]."
                elif Ch_Focus is EmmaX:
                        ch_e "Это было очень. . . приятно, [Ch_Focus.Petname]."
                elif Ch_Focus is LauraX:
                        ch_l "Это было. . . неплохо, [Ch_Focus.Petname]."
                elif Ch_Focus is JeanX:
                        if not Player.Male:
                            ch_j "Ты все сделала как надо, [Ch_Focus.Petname]."
                        else:
                            ch_j "Ты все сделал как надо, [Ch_Focus.Petname]."
                elif Ch_Focus is StormX:
                        ch_s "Это был отличный массаж, [Ch_Focus.Petname]."
                elif Ch_Focus is JubesX:
                        if not Player.Male:
                            ch_v "Слушай, ты очень хороша, [Ch_Focus.Petname]."
                        else:
                            ch_v "Слушай, ты очень хорош, [Ch_Focus.Petname]."
                elif Ch_Focus is GwenX:
                        ch_g "Слушай, у тебя неплохо получается!"
                elif Ch_Focus is BetsyX:
                        ch_b "Это было очень приятно."
                elif Ch_Focus is DoreenX:
                        ch_d "Это было очень здорово! У тебя хорошо получается!"
                elif Ch_Focus is WandaX:
                        ch_w "Это было. . . очень клево!"
        else:
                #any other time
                if Ch_Focus is RogueX:
                        ch_r "Я насладилась хорошим массажем, [Ch_Focus.Petname]."
                elif Ch_Focus is KittyX:
                        ch_k "Хм, мне понравилось, [Ch_Focus.Petname]."
                elif Ch_Focus is EmmaX:
                        ch_e "Это было очень. . . приятно, [Ch_Focus.Petname]."
                elif Ch_Focus is LauraX:
                        ch_l "Спасибо за массаж, [Ch_Focus.Petname]."
                elif Ch_Focus is JeanX:
                        ch_j "Это было очень приятно, [Ch_Focus.Petname]. Отличная работа."
                elif Ch_Focus is StormX:
                        ch_s "Благодарю, [Ch_Focus.Petname]."
                elif Ch_Focus is JubesX:
                        ch_v "Слушай, хорошая работа."
                elif Ch_Focus is GwenX:
                        ch_g "Ах, теперь мне лучше. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Очень хорошо, [Ch_Focus.Petname]."
                elif Ch_Focus is DoreenX:
                        ch_d "Это было очень приятно!"
                elif Ch_Focus is WandaX:
                        ch_w "Спасибо, мне это было нужно. . ."
        $ Ch_Focus.Statup("Love", 90, int(MCount/2)) #raises love by half your track progress
        $ Tempmod = 0
        call Checkout
        return

label Massage_BadEnd: #rkeljsvgbdw
        #if you fucked up. . .
        $ Ch_Focus.FaceChange("angry",1)
        if "massagefail" in Ch_Focus.RecentActions:
                #bad finale
                $ Ch_Focus.Massage += 1
                $ Ch_Focus.Action -=1
                $ Ch_Focus.Addictionrate += 2 if Ch_Focus.Addictionrate < 5 else Ch_Focus.Addictionrate
                if "addictive" in Player.Traits:
                        $ Ch_Focus.Addictionrate += 1
                if Ch_Focus is RogueX:
                        ch_r "Ладно, с тебя хватит, [Ch_Focus.Petname]."
                elif Ch_Focus is KittyX:
                        ch_k "Твои касания плохи!"
                elif Ch_Focus is EmmaX:
                        ch_e "С тебя хватит."
                elif Ch_Focus is LauraX:
                        ch_l "Ладно, я отстраняю тебя."
                elif Ch_Focus is JeanX:
                        ch_j "Ладно, с тебя хватит. . ."
                elif Ch_Focus is StormX:
                        ch_s "Благодарю, [Ch_Focus.Petname], думаю, этого вполне достаточно."
                elif Ch_Focus is JubesX:
                        ch_v "Ладно, прекращай, [Ch_Focus.Petname]."
                elif Ch_Focus is GwenX:
                        ch_g "Воу, ладно, хватит. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Этого будет -вполне- достаточно!"
                elif Ch_Focus is DoreenX:
                        ch_d "Ладно, все, хватит."
                elif Ch_Focus is WandaX:
                        ch_w "Ладно, достаточно."
                $ Tempmod = 0
                call Checkout
        elif Current == "breasts":
                if Ch_Focus is RogueX:
                        ch_r "Думаю, тебе стоит лучше следить за своими руками, [Ch_Focus.Petname]."
                elif Ch_Focus is KittyX:
                        ch_k "Эй! Эм, держись подальше от моей. . . груди."
                elif Ch_Focus is EmmaX:
                        ch_e "[Ch_Focus.Petname]! Держи себя в руках!"
                elif Ch_Focus is LauraX:
                        ch_l "Эй. Я думала, ты хочешь позаботиться обо мне, а не о себе."
                elif Ch_Focus is JeanX:
                        ch_j "Чуть меньше лапанья и чуть больше массажа. . ."
                elif Ch_Focus is StormX:
                        ch_s "Думаю, ты позволяешь своему желанию взять верх над собой, [Ch_Focus.Petname]."
                elif Ch_Focus is JubesX:
                        ch_v "Эй, не так быстро. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Воу, эй, придержи коней. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Я не уверена, что они есть в меню. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Воу! Руки прочь от девочек!"
                elif Ch_Focus is WandaX:
                        ch_w "Воу, следи за руками. . ."
        elif Current == "ass":
                if Ch_Focus is RogueX:
                        ch_r "Думаю, тебе не стоит так низко опускать свои руки, [Ch_Focus.Petname]."
                elif Ch_Focus is KittyX:
                        ch_k "Эй[Ch_Focus.like]держи руки подальше от моей задницы!"
                elif Ch_Focus is EmmaX:
                        if not Player.Male:
                            ch_e "[Ch_Focus.Petname]! Я была бы признательна, если бы ты не лапала мою попку!"
                        else:
                            ch_e "[Ch_Focus.Petname]! Я была бы признательна, если бы ты не лапал мою попку!"
                elif Ch_Focus is LauraX:
                        ch_l "Сейчас мне не нужен массаж моей задницы."
                elif Ch_Focus is JeanX:
                        ch_j "Не беспокойся о моей попке. . ."
                elif Ch_Focus is StormX:
                        ch_s "Лучше не прикасайся к ней, [Ch_Focus.Petname]."
                elif Ch_Focus is JubesX:
                        ch_v "Воу, не трогай ее."
                elif Ch_Focus is GwenX:
                        ch_g "Воу, на нее можно только смотреть. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Прошу, держись подальше от нее. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Ой! Руки!"
                elif Ch_Focus is WandaX:
                        ch_w "Хех, убери руки от моей попки. . ."
        elif Current == "pussy":
                if Ch_Focus is RogueX:
                        ch_r "Эй, [Ch_Focus.Petname]! Держи свои руки подальше от нее!"
                elif Ch_Focus is KittyX:
                        ch_r "Воу! Да, я знаю, меня зовут \"Китти\", но это не приглашение! (прим. Китти = киска)!"
                elif Ch_Focus is EmmaX:
                        if not Player.Male:
                            ch_e "[Ch_Focus.Petname]! Ты слишком наглая."
                        else:
                            ch_e "[Ch_Focus.Petname]! Ты слишком наглый."
                elif Ch_Focus is LauraX:
                        ch_l "Я дам тебе знать, когда мне понадобится -такой- массаж."
                elif Ch_Focus is JeanX:
                        ch_j "Да, это одна из частей моего тела, но, вероятно, не та, которая нуждается во внимании. . ."
                elif Ch_Focus is StormX:
                        if not Player.Male:
                            ch_s "Похоже, ты неправильно поняла мои потребности, [Ch_Focus.Petname]."
                        else:
                            ch_s "Похоже, ты неправильно понял мои потребности, [Ch_Focus.Petname]."
                elif Ch_Focus is JubesX:
                        ch_v "Массаж становится слишком интимным, не находишь?"
                elif Ch_Focus is GwenX:
                        ch_g "Слушай, эм, не заходи так. . . далеко. . ."
                elif Ch_Focus is BetsyX:
                        if not Player.Male:
                            ch_b "Боюсь, ты заблудилась. . ."
                        else:
                            ch_b "Боюсь, ты заблудился. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Ой! Не заходи так далеко!"
                elif Ch_Focus is WandaX:
                        ch_w "Прошу прощения? Тебе не следует заходить так далеко. . ."
        else:
                if Ch_Focus is RogueX:
                        ch_r "Думаю, тебе стоит лучше следить за своими руками, [Ch_Focus.Petname]."
                elif Ch_Focus is KittyX:
                        ch_k "Ох, только не там."
                elif Ch_Focus is EmmaX:
                        ch_e "[Ch_Focus.Petname]! Я ожидала от тебя большего профессионализма."
                elif Ch_Focus is LauraX:
                        ch_l "Вероятно, тебе следует избегать этой области."
                elif Ch_Focus is JeanX:
                        ch_j "Может, постараешься избегать этой области? . ."
                elif Ch_Focus is StormX:
                        ch_s "Не мог бы ты помассажировать другое место, [Ch_Focus.Petname]?"
                elif Ch_Focus is JubesX:
                        ch_v "Может, попробуешь что-то другое, [Ch_Focus.Petname]?"
                elif Ch_Focus is GwenX:
                        ch_g "Здесь не надо. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Пожалуй, тебе следует быть осторожнее."
                elif Ch_Focus is DoreenX:
                        ch_d "Воу! Полегче!"
                elif Ch_Focus is WandaX:
                        ch_w "Эй!"
        return


# end Massage / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# start Strip Tease / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#start Dancing/Stripping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Group_Strip(Girl=0,Tempmod = Tempmod,TempmodP=[0,0],BO=[]): #rkeljsvgbdw
        #Note, this event would break during a date, since it manipulates Adjacent. Perhaps use unique list?
        $ Present = []
        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                if BX.Loc == bg_current:
                        Present.append(BX)

        if not Present:
                "Здесь никого нет."
                "Вы танцуете в одиночестве."
                return

        while len(Present) > 2:
                #culls out extra members
                call Remove_Girl(Present[2])
    #            $ Present.remove(Present[2])

        if len(Present) == 2:
            $ renpy.random.shuffle(Present)
            if Girl and Present[0] != Girl:
                    $ Party.reverse()
            elif ApprovalCheck(Present[0],Check=1) <= ApprovalCheck(Present[1],Check=1):
                    # If second one likes you more, pick her
                    $ Present.reverse()

        call Shift_Focus(Present[0])

        $ Round -= 5 if Round > 5 else (Round-1)
        call Set_The_Scene(1,0,0,0)

        $ Present[0].FaceChange("sexy",1)
        if len(Present) >= 2:
                if Present[1] in TotalGirls:
                        $ Present[1].FaceChange("sexy",1)
                else:
                        $ Present.remove(Present[1])

        $ Cnt = len(Present) #max 2
        while Cnt:
            $ Cnt -= 1 #max 1
            if Girl == EmmaX and "classcaught" in EmmaX.RecentActions and AloneCheck(EmmaX):
                        #skip this step if during classcaught sequence
                        pass
            elif not ApprovalCheck(Present[Cnt], 600, TabM = 1,Alt=[[EmmaX],(650+Taboo*10)]) or (Present[Cnt] is EmmaX and Taboo and "taboo" not in EmmaX.History):
                    if not ApprovalCheck(Present[Cnt], 400):
                        #she does not like you at all
                        if Present[Cnt] is RogueX:
                                ch_r "Я что, похожа на танцовщицу Гоу - Гоу?"
                        elif Present[Cnt] is KittyX:
                                ch_k "Думаешь, я просто станцую для тебя?"
                        elif Present[Cnt] is EmmaX:
                                ch_e "О, ты думаешь, я буду танцевать под твою дудку?"
                        elif Present[Cnt] is LauraX:
                                ch_l "Я не танцую."
                        elif Present[Cnt] is JeanX:
                                ch_j "Я не в настроении."
                        elif Present[Cnt] is StormX:
                                ch_s "Я не танцую."
                        elif Present[Cnt] is JubesX:
                                ch_v "Я не хочу танцевать, чудила. . ."
                        elif Present[Cnt] is GwenX:
                                ch_g "Почему это я должна хотеть сейчас танцевать?"
                        elif Present[Cnt] is BetsyX:
                                ch_b "Я не заинтересована в таком фарсе."
                        elif Present[Cnt] is DoreenX:
                                ch_d "Я не буду танцевать лишь по одной твоей просьбе."
                        elif Present[Cnt] is WandaX:
                                ch_w "Я совсем не хочу устраивать представлений. . ."
                    elif Present[Cnt].Taboo:
                        #it's too public
                        if Present[Cnt] is RogueX:
                                ch_r "Я не думаю, что это лучшее место для танцев."
                        elif Present[Cnt] is KittyX:
                                ch_k "Я не уверна, наверное, это не подходящее место?"
                        elif Present[Cnt] is EmmaX:
                                ch_e "Ты, должно быть, шутишь. Здесь?"
                        elif Present[Cnt] is LauraX:
                                if ApprovalCheck(LauraX, 600, TabM = 0):    #should add a second Laura, then the first gets removed.
                                        $ Present.append(LauraX)            #This restores the "taboo is irrelevant to her" state
                                else:
                                        ch_l "Мне что-то не хочется."
                        elif Present[Cnt] is JeanX:
                                ch_j "Я не хочу просто спонтанно танцевать на людях."
                        elif Present[Cnt] is StormX:
                                ch_s "Я бы не хотела устраивать никаких представлений."
                        elif Present[Cnt] is JubesX:
                                ch_v "Если честно, здесь не самое подходящее место для этого. . ."
                        elif Present[Cnt] is GwenX:
                                ch_g "Это мне немного неловко танцевать."
                        elif Present[Cnt] is BetsyX:
                                ch_b "Это -совершенно- неподходящее место."
                        elif Present[Cnt] is DoreenX:
                                ch_d "Здесь? Я даже не знаю. . ."
                        elif Present[Cnt] is WandaX:
                                ch_w "Не. . . здесь. . ."
                    else:
                        #just not into it
                        if Present[Cnt] is RogueX:
                                ch_r "Думаю, я пока не готова."
                        elif Present[Cnt] is KittyX:
                                ch_k "Я не уверена, мне сейчас совсем не хочется танцевать."
                        elif Present[Cnt] is EmmaX:
                                ch_e "Я совсем сейчас не хочу танцевать."
                        elif Present[Cnt] is LauraX:
                                ch_l "Мне что-то не хочется."
                        elif Present[Cnt] is JeanX:
                                ch_j "Я не в настроении."
                        elif Present[Cnt] is StormX:
                                ch_s "Я не хочу сейчас танцевать."
                        elif Present[Cnt] is JubesX:
                                ch_v "Ага, мне сейчас не хочется танцевать. . ."
                        elif Present[Cnt] is GwenX:
                                ch_g "Эм, мне сейчас не до танцев."
                        elif Present[Cnt] is BetsyX:
                                ch_b "У меня сейчас нет настроения танцевать."
                        elif Present[Cnt] is DoreenX:
                                ch_d "Я не уверена, что сейчас хочу танцевать."
                        elif Present[Cnt] is WandaX:
                                ch_w "Я не в \"танцевальном\" настроении. . ."
                    $ Present.remove(Present[Cnt])

        if not Present:
                return

        if EmmaX.Loc == bg_current and EmmaX not in Present:
                #If Emma is here, but does not agree to this,
                if "classcaught" not in EmmaX.History:
                        if EmmaX.Loc == EmmaX.Home:
                                #if it's her room. . .
                                ch_e "Если вы хотите потанцевать, идите в другом месте."
                                $ Present = []
                                return
                        else:
                                ch_e "По правде говоря, мне пора идти."
                                call Remove_Girl(EmmaX)

        if "stripping" in Present[0].DailyActions and ApprovalCheck(Present[0], 500, TabM = 3):
                $ Line = renpy.random.choice(["Тебе понравилось предыдущее представление?",
                    "Тебе не хватило прошлого раза?",
                    "Ты меня загоняешь."])
        else:
                $ Line = renpy.random.choice(["Хорошо, звучит весело.",
                    "Думаю, можно.",
                    "Ага, ладно."])

        call AnyLine(Present[0],Line)
        $ Line = 0

        call AllReset("All")


        $ Cnt = len(Present) #max 2
        while Cnt:
                $ Cnt -= 1 #max 1

                #starts dance animation
                $ renpy.show(Present[Cnt].Tag+"_Sprite",at_list=[Girl_Dance1(Present[Cnt])],zorder=Present[Cnt].Layer)  #if Present[Cnt] is RogueX:  #show Rogue_Sprite at Girl_Dance1(RogueX)

                $ Present[Cnt].RecentActions.append("stripping")
                $ Present[Cnt].DailyActions.append("stripping")
                $ Present[Cnt].Strip += 1
                $ Present[Cnt].Action -= 1
                $ TempmodP[Cnt] = Tempmod
                if Present[Cnt].SeenChest or Present[Cnt].SeenPussy:
                        #You've seen her tits.
                        $ TempmodP[Cnt] += 20
                if Present[Cnt].SeenPanties:
                        #You've seen her panties.
                        $ TempmodP[Cnt] += 5
                if "exhibitionist" in Present[Cnt].Traits:
                        $ TempmodP[Cnt] += (4*Taboo)
                if ("sex friend" in Present[Cnt].Petnames or Present[Cnt] in Player.Harem) and not Taboo:
                        $ TempmodP[Cnt] += 15
                elif "ex" in Present[Cnt].Traits:
                        $ TempmodP[Cnt] -= 40
                elif Present[Cnt].ForcedCount and not Present[Cnt].Forced:
                        $ TempmodP[Cnt] -= 5 * Present[Cnt].ForcedCount

        if len(Present) >= 2:
                "Они начинают танцевать."
                $ Partner = Present[1]
                $ Count2 = 1
        else:
                "Она начинает танцевать."
                $ Count2 = 0
                $ Partner = 0


        if Girl == EmmaX and "classcaught" in EmmaX.RecentActions and AloneCheck(EmmaX):
                #skip this step if during classcaught sequence
                $ Count = 0
                jump Group_Stripping

        #this portion adds back in girls who dropped out, but sets their "stop" flag.
        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                if BX.Loc == bg_current and BX not in Present:
                        Present.append(BX)
                        if "stopdancing" not in BX.RecentActions:
                                BX.RecentActions.append("stopdancing")
        $ Tempmod = TempmodP[0]
        $ Trigger = "strip"
        $ Count = 1

        while Count and Round >=10:
                #Loops endlessly until you do something.
                $ Round -= 2 if Round > 2 else Round
                if len(Present) >= 2:
                    $ Present[0].GLG(Present[1],600,1,1)
                    $ Present[1].GLG(Present[0],600,1,1)
                menu:
                    "Продолжать":
                            #add auto-start here
                            if ApprovalCheck(Present[0], 1300, TabM = 3) or ApprovalCheck(Present[0], 500, "I", TabM = 2):
                                    $ D20 = renpy.random.randint(1, 20)
                                    if D20 >= 15 and Present[0] != EmmaX:
                                            $ Count = 0
                                            $ Girl.RecentActions.append("autostrip")

                    "Не могла бы ты снять одежду?":
                            #add checks here
                            call AnyLine(Present[0],"М?")
                            $ Count = 0
                    "Остановиться":
                            jump Group_Strip_End


        if EmmaX.Loc == bg_current and len(Present) >= 2:
                #If Emma is here, but does not agree to this,
                if "classcaught" not in EmmaX.History or "three" not in EmmaX.History or (Taboo and "taboo" not in EmmaX.History):
                    if EmmaX.Loc == "bg emma":
                            #if it's her room. . .
                            ch_e "Если вы хотите пошалить, пожалуйста, сделайте это в другом месте."
                            $ Present = []
                            return
                    else:
                            ch_e "По правде говоря, мне пора идти."
                            call Remove_Girl(EmmaX)

label Group_Stripping:
        while Round >= 10 and Present:
            $ Round -= 2 if Round > 2 else Round

            if Present[Count] != Ch_Focus:
                    call Shift_Focus(Present[Count])

            call Girl_Stripping(Present[Count])

            if len(Present) < 2 and Count != 0:
                    $ Count = 0
            if not Present or not Present[Count]: #threw "list index" errors?
                    jump Group_Strip_End
            if "stopdancing" in Present[Count].RecentActions:
                    #if she's just standing around, cut back to the other girl
                    if len(Present) >= 2 and "stopdancing" in Present[0].RecentActions and "stopdancing" in Present[1].RecentActions:
                            jump Group_Strip_End

            $ Trigger = "strip"

            if not Present:
                    #If everyone leaves, quit out
                    jump Group_Strip_End

            if len(Present) >= 2 and Count != Count2:
                $ Present[Count].GLG(Present[Count2],800,2,1)
                $ Present[Count2].GLG(Present[Count],800,2,1)

            if len(Present) >= 2:
                    # Flips the numbers if in a group
                    # Count starts at 0
                    if Count == 0 and "stopdancing" not in Present[1].RecentActions:
                            $ Count = 1
                            $ Count2 = 0
                            $ TempmodP[1] = Tempmod
                            $ Tempmod = TempmodP[0]
                    elif Count == 1 and "stopdancing" not in Present[0].RecentActions:
                            $ Count = 0
                            $ Count2 = 1
                            $ TempmodP[0] = Tempmod
                            $ Tempmod = TempmodP[1]
                    call Shift_Focus(Present[Count])
    #                $ Partner = Present[Count2]

                    call Activity_Check(Ch_Focus,Partner)

            if len(Present) < 2 or "stopdancing" in Present[1].RecentActions:
                    #Plays if only one girl is dancing
                    $ Tempmod = TempmodP[Count]
                    $ Count = 0
                    $ Count2 = 0
                    $ Partner = 0

                    call Activity_Check(Ch_Focus,Partner)

                    if not Present or "stopdancing" in Present[0].RecentActions:
                            jump Group_Strip_End
            #ends loop
        if Present and Round <=15:
                call AnyLine(Present[0],"Уже поздно, нам, наверное, стоит сделать перерыв.")

label Group_Strip_End:
        #add like-ups here. . .
        if Present:
                $ Present[0].DrainWord("stopdancing",1,0,0)
                $ Present[0].DrainWord("keepdancing",1,0,0)
        if len(Present) >= 2:
                $ Present[1].DrainWord("stopdancing",1,0,0)
                $ Present[1].DrainWord("keepdancing",1,0,0)

        call Set_The_Scene(1,0,0,0)
        $ Count = 0
        $ Count2 = 0
    #    $ renpy.pop_call()
        return

#end Dancing/Stripping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Girl_Stripping(Girl=0,Nudist=0): #rkeljsvgbdw
        #This gets called by Group_Stripping, and returns there at the end.
        if "stopdancing" in Girl.RecentActions:
                #if she's just standing around, cut back to the other girl
                return

        $ Girl.ArmPose = 2
        $ Girl.LustFace(1) #sets her lusty face

        if Girl == StormX and (StormX in Rules or Girl.Taboo <= 20):
                #if it's Storm and either you're in private or have broken Xavier, she doesn't fight you
                if Girl.Forced:
                        $ Nudist = -40
                else:
                        $ Nudist = Girl.Taboo
        if "keepdancing" not in Girl.RecentActions and "stopdancing" not in Girl.RecentActions:
                # if Count isn't 2, it loops.
                if Girl.Hat and Girl in (GwenX,EmmaX) and not ApprovalCheck(Girl, 1300):
                            #if she's wearing a hat and not slutty. . .
                            $ Line = get_clothing_name(Girl.Hat_key, vin)
                            $ Girl.Hat = 0
                            "[Girl.Name] снимает [Line] и отбрасывает в сторону."
                elif Girl is JubesX and Girl.Acc and (Girl.Over or Girl.Chest) and (Girl.Panties or Girl.PantsNum() >= 5 or Girl.HoseNum() >= 10):
                    #will she lose the jacket when she's dressed under?
                    if ApprovalCheck(Girl, 750, TabM = 3):
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Inbt", 25, 1)
                            $ Player.Statup("Focus", 60, 3)
                            $ Line = get_clothing_name(Girl.Acc_key, vin)
                            $ Girl.Acc = 0
                            "[Girl.Name] снимает [Line] и отбрасывает в сторону."
                    else:
                            jump Strip_Ultimatum
                elif Girl in (DoreenX,WandaX) and Girl.Acc:
                    #will she lose the jacket when she's dressed under?
                            $ Line = get_clothing_name(Girl.Acc_key, vin)
                            $ Girl.Acc = 0
                            "[Girl.Name] снимает [Line] и отбрасывает в сторону."
                elif Girl.Over and Girl.Chest and (Girl.Panties or Girl.PantsNum() >= 5 or Girl.HoseNum() >= 10):
                    #will she lose the overshirt when she's dressed under?
                    if ApprovalCheck(Girl, 750, TabM = 3,Alt=[[StormX],(300-Nudist*3)]):
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Inbt", 25, 1)
                            $ Player.Statup("Focus", 60, 3)
                            if Girl is KittyX:
                                    $ Line = Girl.Over_display
                                    $ Girl.Over = 0
                                    "[Girl.Name] опускает плечи и ее [Line] падает на пол."
                            else:
                                    $ Line = get_clothing_name(Girl.Over_key, vin)
                                    $ Girl.Over = 0
                                    "[Girl.Name] снимает [Line] через голову и бросает за себя."
                    else:
                            jump Strip_Ultimatum

                elif Girl.Legs and (Girl.Panties or Girl.HoseNum() >= 10):
                    #will she lose the pants/skirt if she has panties on?
                    if ApprovalCheck(Girl, 1200, TabM = 3,Alt=[[StormX],(600-Nudist*3)]) or (Girl.SeenPanties and ApprovalCheck(Girl, 900, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 50, 5)
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Inbt", 30, 1)
                            $ Player.Statup("Focus", 60, 5)
                            if Girl is KittyX:
                                    $ Line = Girl.Legs_display
                                    $ Girl.Legs = 0
                                    "Одно мгновение, и ее [Line] [Girl.Name_rod] уже на полу."
                            else:
                                    $ Line = get_clothing_name(Girl.Legs_key, vin)
                                    $ Girl.Legs = 0
                                    "[Girl.Name] расстегивает и стягивает вниз [Line], затем бросает на пол."
                            if not Girl.SeenPanties:
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Obed", 200, 3)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 2)
                                    $ Girl.SeenPanties = 1
                    else:
                            jump Strip_Ultimatum

                elif Girl.Hose:
                    # Will she lose the hose?
                    if Girl.HoseNum() >= 10:
                            if ApprovalCheck(Girl, 1200, TabM = 3):
                                    $ Girl.Statup("Lust", 50, 6)
                                    $ Player.Statup("Focus", 60, 6)
                            else:
                                    jump Strip_Ultimatum

                    elif Girl.HoseNum() >= 6 and ApprovalCheck(Girl, 1200, TabM = 3):
                            if ApprovalCheck(Girl, 1200, TabM = 3,Alt=[[StormX],(600-Nudist*3)]):
                                $ Girl.Statup("Lust", 50, 4)
                                $ Player.Statup("Focus", 60, 4)
                            else:
                                jump Strip_Ultimatum
                    else:
                            $ Player.Statup("Focus", 60, 3)
                    if Girl is KittyX:
                            $ Line = Girl.Hose_display
                            $ Girl.Hose = 0
                            "[Line.capitalize()] [Girl.Name_rod] скользят с ее ног и остаются на полу небольшой кучкой."
                    else:
                            $ Line = get_clothing_name(Girl.Hose_key, vin)
                            $ Girl.Hose = 0
                            "[Girl.Name] стягивает [Line] вниз, оставляя их на полу небольшой кучкой."
                    call Girl_First_Bottomless(Girl,1)

                elif Girl is JubesX and Girl.Acc and (Girl.Panties or Girl.Legs or Girl.HoseNum() >= 10):
                    #will she lose the jacket when she's topless under?
                    if ApprovalCheck(Girl, 1250, TabM = 3) or (Girl.SeenChest and ApprovalCheck(Girl, 1000, TabM = 3) and not Girl.Taboo):
                            if Girl.SeenChest:
                                    $ Girl.Statup("Lust", 60, 5)
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Inbt", 50, 10)
                                    $ Player.Statup("Focus", 80, 15)
                                    $ Line = get_clothing_name(Girl.Acc_key, vin)
                                    $ Girl.Acc = 0
                                    "[Girl.Name] снимает [Line] и бросает за спину."
                            elif not Girl.SeenChest:
                                    $ Girl.FaceChange("bemused", 1)
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 3)
                                    $ Line = get_clothing_name(Girl.Acc_key, vin)
                                    $ Girl.Acc = 0
                                    "[Girl.Name] нерешительно смотрит в вашу сторону, а потом, пожав плечами, снимает [Line] через голову и кидает на пол."
                                    call Girl_First_Topless(Girl,1)
                    else:
                            jump Strip_Ultimatum
                elif Girl.Over and not Girl.Chest and (Girl.Panties or Girl.HoseNum() >= 10):
                    #will she lose the top when she's topless with panties?
                    if ApprovalCheck(Girl, 1250, TabM = 3,Alt=[[StormX],(650-Nudist*3)]) or (Girl.SeenChest and ApprovalCheck(Girl, 1000, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 60, 5)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Inbt", 50, 10)
                            $ Player.Statup("Focus", 80, 15)
                            if not Girl.SeenChest:
                                    $ Girl.FaceChange("bemused", 1)
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 3)
                                    if Girl is KittyX:
                                            $ Line = get_clothing_name(Girl.Over_key, vin)
                                            $ Girl.Over = 0
                                            "[Girl.Name] нерешительно смотрит в вашу сторону, а затем сдергивает [Line] через тело и кидает на пол."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            $ Line = get_clothing_name(Girl.Over_key, vin)
                                            $ Girl.Over = 0
                                            "[Girl.Name] нерешительно смотрит в вашу сторону, а потом, пожав плечами, снимает [Line] через голову и кидает на пол."
                                    else:
                                            $ Line = get_clothing_name(Girl.Over_key, vin)
                                            $ Girl.Over = 0
                                            "[Girl.Name] нерешительно смотрит в вашу сторону, а потом, пожав плечами, снимает [Line] через голову и кидает на пол."
                                    call Girl_First_Topless(Girl,1)
                            else:
                                if Girl is KittyX:
                                        $ Line = Girl.Over_display
                                        $ Girl.Over = 0
                                        "[Girl.Name] пожимает плечами и [Line] падает к ее ногам."
                                else:
                                        $ Line = get_clothing_name(Girl.Over_key, vin)
                                        $ Girl.Over = 0
                                        "[Girl.Name] снимает [Line] через голову и кидает на пол."
                    else:
                            jump Strip_Ultimatum

                elif Girl.Chest and not Girl.Over:
                    # Will she lose the bra?
                    if ApprovalCheck(Girl, 1250, TabM = 3,Alt=[[StormX],(650-Nudist*3)]) or (Girl.SeenChest and ApprovalCheck(Girl, 1000, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 60, 5)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Inbt", 50, 1)
                            $ Player.Statup("Focus", 80, 15)
                            $ Line = get_clothing_name(Girl.Chest_key, vin)
                            $ Girl.Chest = 0
                            if not Girl.SeenChest:
                                    $ Girl.FaceChange("bemused", 1)
                                    if Line == "swimsuit":
                                            "[Girl.Name] нерешительно смотрит в вашу сторону, а затем, пожав плечами, оголяет грудь."
                                    elif Girl is KittyX:
                                            "[Girl.Name] нерешительно смотрит в вашу сторону, а потом, пожав плечами, сдергивает [Line] через тело и кидает на пол."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            "[Girl.Name] смотрит в вашу сторону, а потом, пожав плечами, снимает [Line] через голову и кидает на пол."
                                    else:
                                            "[Girl.Name] нерешительно смотрит в вашу сторону, а потом, пожав плечами, снимает [Line] через голову и кидает на пол."
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 3)
                                    call Girl_First_Topless(Girl,1)
                            else:
                                    $ Girl.FaceChange("sexy")
                                    if Line == "swimsuit":
                                            "[Girl.Name] оголяет грудь."
                                    elif Girl is KittyX:
                                            "[Girl.Name] сдергивает [Line] через тело и кидает на пол."
                                    else:
                                            "[Girl.Name] снимает [Line] и кидает на пол."
                    else:
                            jump Strip_Ultimatum

                elif Girl.Legs:
                    #will she lose the pants/skirt if she has no panties on?
                    if ApprovalCheck(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 75, 10)
                            $ Line = get_clothing_name(Girl.Legs_key, vin)
                            $ Girl.Legs = 0
                            if not Girl.SeenPussy:
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 50, 4)
                                    $ Girl.Statup("Inbt", 200, 4)
                                    if Girl is KittyX:
                                            "[Girl.Name] застенчиво смотрит на вас, а потом, пожав плечами, сдергивает [Line] через ноги и кидает на пол."
                                    elif Girl in (EmmaX,LauraX,JeanX):
                                            "[Girl.Name] смотрит на вас, затем медленно расстегивает молнию, снимает [Line] и бросает на пол."
                                    else:
                                            "[Girl.Name] застенчиво смотрит на вас, затем медленно расстегивает молнию, снимает [Line] и бросает на пол."
                                    call Girl_First_Bottomless(Girl,1)
                            else:
                                    $ Girl.Statup("Obed", 50, 1)
                                    $ Girl.Statup("Obed", 75, 1)
                                    if Girl is KittyX:
                                            "[Girl.Name] сдергивает [Line] через ноги и кидает на пол."
                                    else:
                                            "[Girl.Name] расстегивает молнию, снимает [Line] и бросает на пол."
                                    $ Girl.Statup("Inbt", 70, 2)
                            $ Player.Statup("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum

                elif Girl is JubesX and Girl.Acc:
                    #will she lose the jacket when she's naked under?
                    if ApprovalCheck(Girl, 1350, TabM = 3) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Line = get_clothing_name(Girl.Acc_key, vin)
                            $ Girl.Acc = 0
                            if not Girl.SeenPussy:
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 50, 4)
                                    $ Girl.Statup("Inbt", 200, 4)
                                    "[Girl.Name] нерешительно смотрит в вашу сторону, а потом, пожав плечами, снимает [Line] и бросает на пол."
                                    call Girl_First_Bottomless(Girl,1)
                            else:
                                    "[Girl.Name] снимает [Line] и бросает на пол."

                            if not Girl.Chest or Girl.Uptop:
                                if not Girl.SeenChest:
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Inbt", 50, 3)
                                        call Girl_First_Topless(Girl,1)
                                else:
                                        $ Girl.Statup("Lust", 60, 15)
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Obed", 75, 1)
                                        $ Girl.Statup("Inbt", 50, 3)
                            else:
                                    $ Girl.Statup("Lust", 75, 10)
                                    $ Girl.Statup("Obed", 50, 1)
                                    $ Girl.Statup("Obed", 75, 1)
                                    $ Girl.Statup("Inbt", 70, 2)
                            $ Player.Statup("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum
                elif Girl.Over and not Girl.Panties:
                    #will she lose the overshirt when she's bottomless under?
                    if ApprovalCheck(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Line = get_clothing_name(Girl.Over_key, vin)
                            $ Girl.Over = 0
                            if not Girl.SeenPussy:
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 50, 4)
                                    $ Girl.Statup("Inbt", 200, 4)
                                    if Girl is KittyX:
                                            "[Girl.Name] нерешительно смотрит в вашу сторону, а потом, пожав плечами, сдергивает [Line] через тело и кидает на пол."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            "[Girl.Name] смотрит в вашу сторону, а потом, пожав плечами, снимает [Line] через голову и кидает на пол."
                                    else:
                                            "[Girl.Name] нерешительно смотрит в вашу сторону, а потом, пожав плечами, снимает [Line] через голову и кидает на пол."
                                    call Girl_First_Bottomless(Girl,1)
                            else:
                                if Girl is KittyX:
                                        "[Girl.Name] сдергивает [Line] через тело и кидает на пол."
                                else:
                                        "[Girl.Name] снимает [Line] через голову и кидает на пол."

                            if not Girl.Chest or Girl.Uptop:
                                if not Girl.SeenChest:
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Inbt", 50, 3)
                                        call Girl_First_Topless(Girl,1)
                                else:
                                        $ Girl.Statup("Lust", 60, 15)
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Obed", 75, 1)
                                        $ Girl.Statup("Inbt", 50, 3)
                            else:
                                        $ Girl.Statup("Lust", 75, 10)
                                        $ Girl.Statup("Obed", 50, 1)
                                        $ Girl.Statup("Obed", 75, 1)
                                        $ Girl.Statup("Inbt", 70, 2)
                            $ Player.Statup("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum

                elif Girl.Chest:
                    # Will she go topless?
                    if ApprovalCheck(Girl, 1250, TabM = 3,Alt=[[StormX],(750-Nudist*3)]) or (Girl.SeenChest and ApprovalCheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 60, 5)
                            $ Line = Girl.Chest
                            $ Girl.Chest = 0
                            if not Girl.SeenChest:
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 50, 3)
                                    $ Girl.Statup("Inbt", 200, 3)
                                    if Line == "swimsuit":
                                            "[Girl.Name] нерешительно смотрит в вашу сторону, а затем, пожав плечами, оголяет грудь."
                                    elif Girl is KittyX:
                                            "[Girl.Name] нерешительно смотрит в вашу сторону, а потом, пожав плечами, сдергивает [Line] через тело и кидает на пол."
                                    elif Girl in (EmmaX,LauraX,StormX):
                                            "[Girl.Name] смотрит в вашу сторону, а потом, пожав плечами, снимает [Line] через голову и кидает на пол."
                                    else:
                                            "[Girl.Name] нерешительно смотрит в вашу сторону, а потом, пожав плечами, снимает [Line] через голову и кидает на пол."
                                    call Girl_First_Topless(Girl,1)
                            else:
                                    $ Girl.Statup("Obed", 50, 2)
                                    if Line == "swimsuit":
                                            "[Girl.Name] оголяет грудь."
                                    elif Girl is KittyX:
                                            "[Girl.Name] сдергивает [Line] через тело и кидает на пол."
                                    else:
                                            "[Girl.Name] снимает [Line] через голову и кидает на пол."
                                    $ Girl.Statup("Inbt", 50, 1)
                            $ Player.Statup("Focus", 80, 15)
                    else:
                            jump Strip_Ultimatum

                elif Girl.Panties:
                    # Will she go bottomless?
                    if ApprovalCheck(Girl, 1350, TabM = 3,Alt=[[StormX],(800-Nudist*3)]) or (Girl.SeenPussy and ApprovalCheck(Girl, 1100, TabM = 3) and not Girl.Taboo):
                            $ Girl.Statup("Lust", 75, 10)
                            $ Line = get_clothing_name(Girl.Panties_key, vin)
                            $ Girl.Panties = 0
                            if not Girl.SeenPussy:
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 50, 4)
                                    $ Girl.Statup("Inbt", 200, 4)
                                    if Girl is KittyX:
                                            "[Girl.Name] застенчиво смотрит на вас, а затем медленно вытягивает [Line] сквозь свое тело и отбрасывает в сторону."
                                    elif Girl in (EmmaX,LauraX):
                                            "[Girl.Name] смотрит на вас, а затем стягивает [Line] вниз и отбрасывает в сторону."
                                    else:
                                            "[Girl.Name] застенчиво смотрит на вас, а затем медленно стягивает [Line] вниз и отбрасывает в сторону."
                                    call Girl_First_Bottomless(Girl,1)
                            else:
                                    $ Girl.Statup("Obed", 50, 1)
                                    $ Girl.Statup("Obed", 75, 1)
                                    if Girl is KittyX:
                                            "[Girl.Name] смотрит на вас, а затем осторожно вытягивает [Line] сквозь свое тело и отбрасывает в сторону."
                                    else:
                                            "[Girl.Name] смотрит на вас, а затем осторожно стягивает [Line] вниз и отбрасывает в сторону."
                                    $ Girl.Statup("Inbt", 70, 2)
                            $ Player.Statup("Focus", 85, 15)
                    else:
                            jump Strip_Ultimatum
                elif Girl.Hat and Girl in (GwenX,EmmaX):
                            #if she's wearing a hat and not slutty. . .
                            $ Line = get_clothing_name(Girl.Hat_key, vin)
                            $ Girl.Hat = 0
                            "[Girl.Name] снимает [Line] и отбрасывает в сторону."
                elif "autostrip" in Girl.RecentActions:
                    #if she runs out of clothes while auto-strippping, she just keeps dancing
                    $ Girl.RecentActions.remove("autostrip")
                    $ Girl.RecentActions.append("keepdancing")
                else:
                    $ Girl.FaceChange("sexy")
                    if Girl is RogueX:
                            ch_r "Боюсь, это все, что на мне было, [Girl.Petname]. . ."
                    elif Girl is KittyX:
                            ch_k "Похоже, на мне закончилась одежда. . ."
                    elif Girl is EmmaX:
                            ch_e "Что ж, похоже, на мне закончилась одежда, [Girl.Petname]. . ."
                    elif Girl is LauraX:
                            ch_l "Ну, это все, что на мне было, [Girl.Petname]. . ."
                    elif Girl is JeanX:
                            ch_j "Я совсем без одежды. . ."
                    elif Girl is StormX:
                            ch_s "Кажется, я лишилась всей своей одежды. . ."
                    elif Girl is JubesX:
                            ch_v "Нууу, похоже, я закончила. . ."
                    elif Girl is GwenX:
                            ch_g "Упс, на мне закончилась одежда. . ."
                    elif Girl is BetsyX:
                            ch_b "Ох, дорогуша, боюсь, на мне закончилась одежда. . ."
                    elif Girl is DoreenX:
                            ch_d "А теперь. . . ох, думаю, на этом все. . ."
                    elif Girl is WandaX:
                            ch_w "Мне больше нечего показать. . ."
                    menu:
                            extend ""
                            "Хорошо, можешь остановиться":
                                    $ Girl.RecentActions.append("stopdancing")
                                    call Girl_Pos_Reset(Girl) #call expression Girl.Tag + "_Pos_Reset"
                            "Продолжай танцевать":
                                    $ Girl.RecentActions.append("keepdancing")
        # end "nude" not in Girl.RecentActions loop

        $ Girl.Statup("Lust", 70, 2)               #lust/Focus
        if "exhibitionist" in Girl.Traits:
                $ Girl.Statup("Lust", 200, 2)
        $ Player.Statup("Focus", 60, 3)
        if Trigger2 == "jackin" or Trigger2 == "jilling":
                $ Girl.Statup("Lust", 200, 2)
                $ Player.Statup("Focus", 200, 5)

        if not Player.Semen and Player.Focus >= 50:
                $ Player.Focus = 50

        if Player.Focus >= 100 or Girl.Lust >= 100:
                #If either of you could cum

                if Player.Focus >= 100:
                    #You cum
                    call Player_Cumming(Girl)
                    if "angry" in Girl.RecentActions:
                            return
                    $ Girl.Statup("Lust", 200, 5)
                    if not Player.Semen and (Trigger2 == "jackin" or Trigger2 == "jilling"):
                            "У вас во рту пересохло, пожалуй, вам остается лишь наблюдать."
                            $ Trigger2 = 0
                            if Player.Focus > 80:
                                    jump Group_Strip_End

                if Girl.Lust >= 100:
                    #and girl cums
                    call Girl_Cumming(Girl)
                    if Situation == "shift" or "angry" in Girl.RecentActions:
                            $ Count = 0
                            jump Group_Strip_End

                #Resets dance
                call Girl_Hide(Girl)    #call AllReset(Girl)
                $ renpy.show(Girl.Tag+"_Sprite",at_list=[Girl_Dance1(Girl)],zorder=Girl.Layer)  #        if Girl is RogueX: #show Rogue_Sprite at Girl_Dance1(Girl)

                $ Trigger = "strip"
                "[Girl.Name] снова начинает танцевать."

        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)

        menu:
            "Что дальше?"
            "Продолжай. . ." if "keepdancing" not in Girl.RecentActions:
                    $ Girl.Eyes = "sexy"
                    if Girl.Love >= 700 or Girl.Obed >= 500:
                        if not Tempmod:
                            $ Tempmod = 10
                        elif Tempmod <= 20:
                            $ Tempmod += 1
                    if Taboo and Girl.Strip <= 10:
                        $ Girl.Statup("Obed", 50, 7)
                    elif Taboo or Girl.Strip <= 10:
                        $ Girl.Statup("Obed", 50, 5)
                    elif Girl.Strip <= 50:
                        $ Girl.Statup("Obed", 50, 3)
            "Продолжай танец. . ." if "keepdancing" in Girl.RecentActions:
                    $ Girl.Eyes = "sexy"

            "Прекрати раздеваться, продолжай танцевать" if "keepdancing" not in Girl.RecentActions:
                    if "autostrip" in Girl.RecentActions:
                            #if she runs out of clothes while auto-strippping, she just keeps dancing
                            $ Girl.FaceChange("sad",1)
                            $ Girl.RecentActions.remove("autostrip")
                    if Girl is RogueX:
                            ch_r "Ладно. . ."
                    elif Girl is KittyX:
                            ch_k "Лады. . ."
                    elif Girl is EmmaX:
                            ch_e "Ох? Отлично."
                    elif Girl is LauraX:
                            if not Player.Male:
                                ch_l "А? Наверное, ты права. . ."
                            else:
                                ch_l "А? Наверное, ты прав. . ."
                    elif Girl is JeanX:
                            ch_j "Конечно."
                    elif Girl is StormX:
                            ch_s "Хорошо. . ."
                    elif Girl is JubesX:
                            ch_v "Ох, ну ладно. . ."
                    elif Girl is GwenX:
                            ch_g "Ох, ладно. . ."
                    elif Girl is BetsyX:
                            ch_b "Ну хорошо. . ."
                    elif Girl is DoreenX:
                            ch_d "Эм, ладно. . ."
                    elif Girl is WandaX:
                            ch_w "Ладно. . ."
                    $ Girl.RecentActions.append("keepdancing")

            "Снова начни раздеваться" if "keepdancing" in Girl.RecentActions:
                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                    if not Player.Male and "girltalk" not in Girl.History:
                            pass
                    else:
                            $ Girl.RecentActions.remove("keepdancing")

                    if "stripforced" in Girl.RecentActions:
                            call AnyLine(Girl,". . .")
                    else:
                            if Girl == RogueX:
                                    ch_r "Хмм. . ."
                            elif Girl == KittyX:
                                    ch_k "А?"
                            else:
                                    call AnyLine(Girl,"Хмм. . .")

            "(Просто молча смотреть)":
                if "watching" not in Girl.RecentActions:
                    if "keepdancing" not in Girl.RecentActions:
                        if Taboo and Girl.Strip <= 10:
                            $ Girl.Statup("Inbt", 50, 3)
                        elif Taboo or Girl.Strip <= 10:
                            $ Girl.Statup("Inbt", 50, 1)
                    elif Girl.Strip <= 50:
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.Statup("Lust", 70, 2)
                    $ Girl.RecentActions.append("watching")

            "Начать дрочить." if Trigger2 != "jackin" and Player.Male:
                    call Jackin(Girl)
            "Перестать дрочить." if Trigger2 == "jackin":
                    $ Trigger2 = 0
            "Начать мастурбировать." if Trigger2 != "jilling" and not Player.Male:
                    call Jackin(Girl)
            "Перестать мастурбировать." if Trigger2 == "jilling":
                    $ Trigger2 = 0

            "Сними [get_clothing_name(Girl.Arms_key, vin)]. . ." if Girl.Arms:
                    $ Girl.FaceChange("surprised")
                    $ Girl.Mouth = "kiss"
                    call AnyLine(Girl,"Ладно, "+Girl.Petname+".")
                    $ Girl.FaceChange("sexy")
                    $ Girl.Arms = 0

            "Сними [get_clothing_name(Girl.Hat_key, vin)]" if Girl.Hat:
                    #if she's wearing a hat and not slutty. . .
                    $ Line = get_clothing_name(Girl.Hat_key, vin)
                    $ Girl.Hat = 0
                    "Она снимает [Line] и откидывает в сторону."

            "Ладно, хватит.":
                    if Girl == RogueX:
                            ch_r "Хорошо, [Girl.Petname]. . . "
                    elif Girl == KittyX:
                            ch_k "Хорошо. . ."
                    else:
                            call AnyLine(Girl,"Хорошо, "+Girl.Petname+".")
                    $ renpy.pop_call()
                    jump Group_Strip_End

        return


label Strip_Ultimatum: #rkeljsvgbdw
        if "keepdancing" in Girl.RecentActions:
            return
        elif "autostrip" in Girl.RecentActions:
            #if she runs out of clothes while auto-strippping, she just keeps dancing
            $ Girl.RecentActions.remove("autostrip")
            $ Girl.RecentActions.append("keepdancing")
            return

        call Girl_Pos_Reset(Girl) #call expression Girl.Tag + "_Pos_Reset"

        $ Girl.FaceChange("bemused", 1)
        if "stripforced" in Girl.RecentActions:
                    $ Girl.FaceChange("sad", 1)
                    if Girl is RogueX:
                            ch_r "Это все, на что я готова, [Girl.Petname]."
                    elif Girl is KittyX:
                            ch_k "Это все, что ты получишь."
                    elif Girl is EmmaX:
                            ch_e "Думаю, этого достаточно, [Girl.Petname]."
                    elif Girl is LauraX:
                            ch_l "Это все, [Girl.Petname]."
                    elif Girl is JeanX:
                            ch_j "Ладно, это мой предел."
                    elif Girl is StormX:
                            ch_s "Я не буду продолжать. . ."
                    elif Girl is JubesX:
                            ch_v "Ладно, это все, что ты получишь. . ."
                    elif Girl is GwenX:
                            ch_g "Эм. . . Я бы хотела остановиться на этом. . ."
                    elif Girl is BetsyX:
                            ch_b "Я вынуждена отметить, что на этом все. . ."
                    elif Girl is DoreenX:
                            ch_d "Ладно, это мой предел. . ."
                    elif Girl is WandaX:
                            ch_w "Ладно, давай на этом остановимся. . ."
        else:
                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                    if Girl is RogueX:
                            ch_r "Извини, [Girl.Petname], Я не готова на большее. . . пока."
                    elif Girl is KittyX:
                            ch_k "Я не уверена, [Girl.Petname], пожалуй, это все, на что я готова сейчас."
                    elif Girl is EmmaX:
                            ch_e "Боюсь, это все, что я могу сделать, [Girl.Petname]. . . сейчас."
                    elif Girl is LauraX:
                            ch_l "Ладно, этого достаточно, [Girl.Petname]. . . на этот раз."
                    elif Girl is JeanX:
                            if not Player.Male:
                                ch_j "Ладно, думаю, ты уже достаточно насмотрелась. . ."
                            else:
                                ch_j "Ладно, думаю, ты уже достаточно насмотрелся. . ."
                    elif Girl is StormX:
                            ch_s "Пока этого достаточно. . ."
                    elif Girl is JubesX:
                            ch_v "Я вроде как закончила. . ."
                    elif Girl is GwenX:
                            ch_g "Эм, этого достаточно, ведь так?"
                    elif Girl is BetsyX:
                            ch_b "Я бы предпочла на этом закончить. . ."
                    elif Girl is DoreenX:
                            ch_d "Ладно, этого ведь. . . достаточно, правда?"
                    elif Girl is WandaX:
                            ch_w "Это все, чем я могу сейчас похвастаться. . ."
        menu:
            extend ""
            "Все в порядке, можешь остановиться.":
                    if "ultimatum" not in Girl.DailyActions:
                            $ Girl.Statup("Love", 50, 2)
                            $ Girl.Statup("Love", 90, 2)
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.DailyActions.append("ultimatum")
                    $ Girl.RecentActions.append("stopdancing")
                    return
            "Все в порядке, но потанцуй еще немного. . .":
                    if "ultimatum" not in Girl.DailyActions:
                            $ Girl.Statup("Love", 50, 2)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.DailyActions.append("ultimatum")
                    $ Girl.RecentActions.append("keepdancing")
                    if "stripforced" in Girl.RecentActions:
                            call AnyLine(Girl,". . .")
                    else:
                            if Girl is RogueX:
                                    ch_r "Хех, ладно, [Girl.Petname]."
                            elif Girl is KittyX:
                                    ch_k "Хихи, хорошо."
                            elif Girl is EmmaX:
                                    ch_e "Ох, если я должна, [Girl.Petname]."
                            elif Girl is LauraX:
                                    ch_l "Эм? Ладно."
                            elif Girl is JeanX:
                                    ch_j "Конечно."
                            elif Girl is StormX:
                                    ch_s "Хорошо. . ."
                            elif Girl is JubesX:
                                    ch_v "Конечно. . ."
                            elif Girl is GwenX:
                                    ch_g "Ха, ладно. . ."
                            elif Girl is BetsyX:
                                    ch_b "Это можно. . ."
                            elif Girl is DoreenX:
                                    ch_d "Эм, ладно. . ."
                            elif Girl is WandaX:
                                    ch_w "Конечно. . ."
            "Продолжай раздеваться." if Girl.Forced:
                    if not ApprovalCheck(Girl, 500, "O", TabM=5) and not ApprovalCheck(Girl, 800, "L", TabM=5):
                            $ Girl.FaceChange("angry")
                            if Girl is RogueX:
                                    if not Player.Male:
                                        ch_r "Я не знаю, за кого ты меня принимаешь, но я не собираюсь делать что-либо, только потому, что ты так сказала."
                                    else:
                                        ch_r "Я не знаю, за кого ты меня принимаешь, но я не собираюсь делать что-либо, только потому, что ты так сказал."
                                    ch_r "Думаю, на сегодня мы закончили."
                            elif Girl is KittyX:
                                    ch_k "Я не собираюсь выполнять все, что ты говоришь!"
                                    ch_k "Я закончила."
                            elif Girl is EmmaX:
                                    if not Player.Male:
                                        ch_e "Думаю, ты переступила все границы, [Girl.Petname]."
                                    else:
                                        ch_e "Думаю, ты переступил все границы, [Girl.Petname]."
                                    ch_e "Помни свое место."
                            elif Girl is LauraX:
                                    ch_l "Мне не нравится твой тон, [Girl.Petname]."
                            elif Girl is JeanX:
                                    ch_j "Не смей так со мной разговаривать."
                            elif Girl is StormX:
                                    ch_s "Мне не нравится твой тон."
                            elif Girl is JubesX:
                                    ch_v "Будет лучше, если мне не придется разбивать твое лицо. . ."
                            elif Girl is GwenX:
                                    ch_g "Я не люблю, когда мне приказывают. . ."
                            elif Girl is BetsyX:
                                    ch_b "Думай, с кем говоришь. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ну, с таким отношением ты ничего не добьешься. . ."
                            elif Girl is WandaX:
                                    ch_w "Тебе лучше меня не злить. . ."
                            $ Girl.RecentActions.append("angry")
                            $ Girl.DailyActions.append("angry")
                            call Remove_Girl(Girl)
                            return
                    $ Tempmod += 20
                    $ Girl.Forced += 1
                    $ Girl.FaceChange("sad")
                    if "stripforced" in Girl.RecentActions:
                            $ Girl.FaceChange("angry")
                            call AnyLine(Girl,". . .")
                    else:
                            if Girl is RogueX:
                                    ch_r "Я. . . думаю, я смогу. . ."
                            elif Girl is KittyX:
                                    ch_k "Я. . . могу показать немного больше. . ."
                            elif Girl is EmmaX:
                                    ch_e "Хмм, как властно. . ."
                            elif Girl is LauraX:
                                    ch_l "Грррр. . ."
                            elif Girl is JeanX:
                                    ch_j ". . . ладно."
                            elif Girl is StormX:
                                    ch_s ". . ."
                            elif Girl is JubesX:
                                    ch_v "Нууу. . . ладно. . ."
                            elif Girl is GwenX:
                                    ch_g "Ну, может быть, немного. . ."
                            elif Girl is BetsyX:
                                    ch_b "Если это нужно. . ."
                            elif Girl is DoreenX:
                                    ch_d "Эм, ладно. . ."
                            elif Girl is WandaX:
                                    ch_w "Конечно. . ."
                            $ Girl.RecentActions.append("stripforced")
                    $ Girl.Statup("Love", 200, -40)
            "Я знаю, ты можешь лучше. Продолжай." if not Girl.Forced:
                    if not ApprovalCheck(Girl, 300, "O", TabM=5) and not ApprovalCheck(Girl, 700, "L", TabM=5):
                            $ Girl.FaceChange("angry")
                            if Girl is RogueX:
                                    if not Player.Male:
                                        ch_r "Я не знаю, за кого ты меня принимаешь, но я не собираюсь делать что-либо, только потому, что ты так сказала."
                                    else:
                                        ch_r "Я не знаю, за кого ты меня принимаешь, но я не собираюсь делать что-либо, только потому, что ты так сказал."
                                    ch_r "Думаю, на сегодня мы закончили."
                            elif Girl is KittyX:
                                    ch_k "Я не собираюсь выполнять все, что ты говоришь!"
                                    ch_k "Я закончила."
                            elif Girl is EmmaX:
                                    if not Player.Male:
                                        ch_e "Думаю, ты переступила все границы, [Girl.Petname]."
                                    else:
                                        ch_e "Думаю, ты переступил все границы, [Girl.Petname]."
                                    ch_e "Помни свое место."
                            elif Girl is LauraX:
                                    ch_l "Мне не нравится твой тон, [Girl.Petname]."
                            elif Girl is JeanX:
                                    ch_j "Не смей так со мной разговаривать."
                            elif Girl is StormX:
                                    ch_s "Нет, я так не думаю."
                            elif Girl is JubesX:
                                    ch_v "Ох, могу, но ты этого не увидишь. . ."
                            elif Girl is GwenX:
                                    ch_g "Могу, но не буду. . ."
                            elif Girl is BetsyX:
                                    ch_b "Может, я и могу, но не буду. . ."
                            elif Girl is DoreenX:
                                    ch_d "Я не хочу!"
                            elif Girl is WandaX:
                                    ch_w "Тебе лучше меня не злить. . ."
                            $ Girl.RecentActions.append("angry")
                            $ Girl.DailyActions.append("angry")
                            call Remove_Girl(Girl)
                            return
                    $ Girl.Statup("Love", 200, -10)
                    $ Girl.Statup("Obed", 50, 3)
                    $ Girl.Statup("Obed", 75, 5)
                    $ Tempmod += 20
                    $ Girl.Forced += 1
                    $ Girl.FaceChange("sad")
                    if Girl is RogueX:
                            ch_r "Ну, если ты настаиваешь. . ."
                    elif Girl is KittyX:
                            ch_k "Может быть. . ."
                    elif Girl is EmmaX:
                            ch_e "Не знаю, что может быть лучше \"совершенства\". . ."
                    elif Girl is LauraX:
                            ch_l ". . . Верно. . ."
                    elif Girl is JeanX:
                            ch_j "Я не понимаю, как это возможно. . ."
                    elif Girl is StormX:
                            ch_s "Посмотрим. . ."
                    elif Girl is JubesX:
                            ch_v "Хорошо, как насчет этого. . ."
                    elif Girl is GwenX:
                            ch_g "Ну, может немного. . ."
                    elif Girl is BetsyX:
                            ch_b "Если это нужно. . ."
                    elif Girl is DoreenX:
                            ch_d "Эм. . . ладно. . ."
                    elif Girl is WandaX:
                            ch_w "Пожалуй, это я могу. . ."
        if "ultimatum" not in Girl.DailyActions:
                    $ Girl.DailyActions.append("ultimatum")

        #restarts dance animation
        $ renpy.show(Girl.Tag+"_Sprite",at_list=[Girl_Dance1(Girl)],zorder=Girl.Layer)  #        if Girl is RogueX: #show Rogue_Sprite at Girl_Dance1(Girl)
        "[Girl.Name] снова начинает танцевать."
        return

transform Girl_Dance1(Chr=Ch_Focus):
        subpixel True
        pos (Chr.SpriteLoc, 50)
        offset (0,0)
        anchor (0.5,0.0)
        zoom 1
        choice:
            parallel:
                ease 2.5 xoffset -40
                ease 2.5 xoffset 0
            parallel:
                easeout 1.0 yoffset 30 # 70 and 80
                linear 0.5 yoffset 40
                easein 1.0 yoffset 0
                easeout 1.0 yoffset 40
                linear 0.5 yoffset 50 #1.35
                easein 1.0 yoffset 0
        choice:
            parallel:
                ease 2.5 xoffset 40
                ease 2.5 xoffset 0
            parallel:
                easeout 1.0 yoffset 30 #1.3
                linear 0.5 yoffset 40
                easein 1.0 yoffset 0
                easeout 1.0 yoffset 40
                linear 0.5 yoffset 50 #1.35
                easein 1.0 yoffset 0
        choice(0.3):
            parallel:
                ease 2.5 xoffset -30
                ease 2.5 xoffset 0
            parallel:
                ease 1.5 yoffset 150
                ease 3.5 yoffset 0
        repeat
# End Strip Dancing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Girl_Lesbian / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Les_Interupted: #rkeljsvgbdw
#        $ Girl = GirlCheck(Girl)
#        call Shift_Focus(Girl)
        # Called if you catch them fucking
        if "unseen" not in Ch_Focus.RecentActions:
                if Ch_Focus.OCount < 3 and Ch_Focus.Action:
                    menu:
                        "Вы хотите остановить их?"
                        "Да.":
                            pass
                        "Нет, пусть продолжают.":
                            $ Ch_Focus.Action -= 1 if Ch_Focus.Action > 0 else 0
                            jump Les_Cycle
                else:
                    if Ch_Focus is LauraX:
                            ch_l "Ааах, то что надо. . ."
                    else:
                            call AnyLine(Ch_Focus,"Ладно, пожалуй, этого достаточно. . .")
                jump Les_After
        $ Ch_Focus.DrainWord("unseen",1,0) #She sees you, so remove unseens
        $ Partner.DrainWord("unseen",1,0) #She sees you, so remove unseens

        $ Ch_Focus.FaceChange("surprised", 1)
        $ Partner.FaceChange("surprised",2)

        "Вдруг [Ch_Focus.Name] резко отрывается от своего занятия, и толкает [Partner.Name_vin]."
        $ Ch_Focus.FaceChange("bemused", 0)
        $ Partner.FaceChange("perplexed",1)

        if Ch_Focus is RogueX:
                ch_r "Эм, [Player.Name], как долго ты смотришь?"
        elif Ch_Focus is KittyX:
                ch_k "Ой! [Player.Name], как давно ты здесь?!"
        elif Ch_Focus is EmmaX:
                ch_e "Хмм? [Ch_Focus.Petname], наслаждаешься представлением?"
        elif Ch_Focus is LauraX:
                ch_l "Ох! Эй, [Player.Name], как давно ты здесь?"
        elif Ch_Focus is JeanX:
                ch_j "Ох, эй, [Player.Name], хорошо видно?"
        elif Ch_Focus is StormX:
                ch_s "Ох? Здравствуй, [Ch_Focus.Petname]. Ты давно здесь?"
        elif Ch_Focus is JubesX:
                if not Player.Male:
                    ch_v "А? Слушай, [Ch_Focus.Petname]. Что ты видела?"
                else:
                    ch_v "А? Слушай, [Ch_Focus.Petname]. Что ты видел?"
        elif Ch_Focus is GwenX:
                ch_g "Ох, привет, [Ch_Focus.Petname]. . . почему-то я не удивлена, увидев тебя."
        elif Ch_Focus is BetsyX:
                ch_b "Ох, кажется, у нас тут зрители. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Ой! [Ch_Focus.Petname]!"
        elif Ch_Focus is WandaX:
                ch_w "Ох! Привет, [Ch_Focus.Petname]. . . что такое. . ?"
        $ Ch_Focus.Action -= 1 if Ch_Focus.Action > 0 else 0
        call Checkout#(1)
        $ Line = 0

        #If you've been jacking it
        if Trigger2 == "jackin" or Trigger2 == "jilling":
                $ Ch_Focus.Eyes = "down"
                if Ch_Focus is RogueX:
                        if Trigger2 == "jackin":
                                ch_r "И почему твой член так торчит?!"
                        else:
                                ch_r "И почему ты так ласкаешь свою киску?!"
                elif Ch_Focus is KittyX:
                        ch_k "и почему ты ласкаешь себя?!"
                elif Ch_Focus is EmmaX:
                        ch_e "и ты думаешь. . . это. . . подходящая реакция?"
                elif Ch_Focus is LauraX:
                        if not Player.Male:
                            ch_l "Похоже, ты решила позаботиться о себе."
                        else:
                            ch_l "Похоже, ты решил позаботиться о себе."
                elif Ch_Focus is JeanX:
                        ch_j "Похоже, ты наслаждаешься. . ."
                elif Ch_Focus is StormX:
                        if not Player.Male:
                            ch_s "Похоже, ты была занята."
                        else:
                            ch_s "Похоже, ты был занят."
                elif Ch_Focus is JubesX:
                        ch_v "Похоже, это привлекло твое внимание."
                elif Ch_Focus is GwenX:
                        ch_g "О, похоже, ты словно у себя дома. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Вижу, ты в восторге. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я думаю, тебе. . . понравилось. . ?"
                elif Ch_Focus is WandaX:
                        ch_w "Вижу. . . тебе понравилось. . ."

                if not Player.Male and "girltalk" not in Ch_Focus.History:
                        if not ApprovalCheck(Ch_Focus, 1100):
                                $ Ch_Focus.DrainWord("nogirls",0,0,0,1) #history
                                $ Ch_Focus.AddWord(1,0,0,0,"girltalk") #history
                        else:
                                $ Ch_Focus.AddWord(1,0,0,0,"nogirls") #history
                if not Player.Male and "girltalk" not in Partner.History:
                        if not ApprovalCheck(Partner, 1100):
                                $ Partner.DrainWord("nogirls",0,0,0,1) #history
                                $ Partner.AddWord(1,0,0,0,"girltalk") #history
                        else:
                                $ Partner.AddWord(1,0,0,0,"nogirls") #history
                menu:
                    extend ""
                    "Да, это было отличное представление.":
                            $ Ch_Focus.FaceChange("sexy")
                            $ Ch_Focus.Statup("Obed", 50, 3)
                            $ Ch_Focus.Statup("Obed", 70, 2)
                            "[Ch_Focus.Name] glances over at [Partner.Name]."
                            if Ch_Focus is RogueX:
                                    ch_r "Ну, думаю, так оно. . ."
                            elif Ch_Focus is KittyX:
                                    ch_k "Думаю, так. . ."
                            elif Ch_Focus is EmmaX:
                                    ch_e "Полагаю, так и есть. . ."
                            elif Ch_Focus is LauraX:
                                    ch_l "Ясно. . ."
                            elif Ch_Focus is JeanX:
                                    ch_j "Да, неплохое. . ."
                            elif Ch_Focus is StormX:
                                    ch_s "Да, полагаю, так."
                            elif Ch_Focus is JubesX:
                                    ch_v "Ты слышала? Мы с тобой теперь звезды."
                            elif Ch_Focus is GwenX:
                                    ch_g "Пожалуйста, не надо оваций."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Наверняка. . ."
                            elif Ch_Focus is DoreenX:
                                    ch_d "Хех. . . ладно. . ."
                            elif Ch_Focus is WandaX:
                                    ch_w "Конечно, конечно. . ."
                            if Ch_Focus.Love >= 800 or Ch_Focus.Obed >= 500 or Ch_Focus.Inbt >= 500:
                                    $ Tempmod += 10
                                    $ Ch_Focus.Statup("Lust", 90, 5)
                                    if Ch_Focus is RogueX:
                                            ch_r "Прятно смотреть на тебя под моим углом. . ."
                                    elif Ch_Focus is KittyX:
                                            if not Player.Male:
                                                ch_k "И[Ch_Focus.like]ты сама не так уж и плоха. . ."
                                            else:
                                                ch_k "И[Ch_Focus.like]ты сам не так уж и плох. . ."
                                    elif Ch_Focus is EmmaX:
                                            if not Player.Male:
                                                ch_e "Да ты и сама радуешь глаза. . ."
                                            else:
                                                ch_e "Да ты и сам радуешь глаза. . ."
                                    elif Ch_Focus is LauraX:
                                            if not Player.Male:
                                                ch_l "Ты тоже неплоха. . ."
                                            else:
                                                ch_l "Ты тоже неплох. . ."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Ты тоже хорошо выглядишь. . . "
                                    elif Ch_Focus is StormX:
                                            if not Player.Male:
                                                ch_s "А ты могла бы стать прекрасным дополнением. . ."
                                            else:
                                                ch_s "А ты мог бы стать прекрасным дополнением. . ."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Не хочешь присоединиться к нам?"
                                    elif Ch_Focus is GwenX:
                                            ch_g "Не хочешь поучавствовать?"
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Хочешь присоедениться?"
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Хочешь к нам? . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Так ты присоединяешься к нам, или. . ."
                    #end "Yeah, it was an excellent show."

                    "Я. . . здесь недавно?":
                            $ Ch_Focus.FaceChange("angry")
                            $ Ch_Focus.Statup("Love", 70, 2)
                            $ Ch_Focus.Statup("Love", 90, 1)
                            $ Ch_Focus.Statup("Obed", 50, 2)
                            $ Ch_Focus.Statup("Obed", 70, 2)
                            if Player.Male:
                                "Она многозначительно смотрит на ваш член,"
                            else:
                                "Она многозначительно смотрит на вашу влажную киску,"
                            if Ch_Focus is RogueX:
                                    ch_r "Конееечно . . ."
                            elif Ch_Focus is KittyX:
                                    ch_k "Агаа. . ."
                            elif Ch_Focus is EmmaX:
                                    ch_e "Ага, конечно. . ."
                            elif Ch_Focus is LauraX:
                                    ch_l "Эм, угу. . ."
                            elif Ch_Focus is JeanX:
                                    ch_j "Конечно. . ."
                            elif Ch_Focus is StormX:
                                    ch_s "Так я тебе и поверила."
                            elif Ch_Focus is JubesX:
                                    ch_v "Ну конечно."
                            elif Ch_Focus is GwenX:
                                    ch_g "Конечно. . ."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Конечно. . ."
                            elif Ch_Focus is DoreenX:
                                    ch_d "Угум. . ."
                            elif Ch_Focus is WandaX:
                                    ch_w "Конечно, конечно. . ."
                            if Ch_Focus.Love >= 800 or Ch_Focus.Obed >= 500 or Ch_Focus.Inbt >= 500:
                                    $ Tempmod += 10
                                    $ Ch_Focus.Statup("Lust", 90, 5)
                                    $ Ch_Focus.FaceChange("bemused", 1)
                                    if Ch_Focus is RogueX:
                                            ch_r "-считаю, мы были очень соблазнительны. . ."
                                    elif Ch_Focus is KittyX:
                                            ch_k "-не могу винить тебя за это. . ."
                                    elif Ch_Focus is EmmaX:
                                            if not Player.Male:
                                                ch_e "вижу, ты заинтересована. . ."
                                            else:
                                                ch_e "вижу, ты заинтересован. . ."
                                    elif Ch_Focus is LauraX:
                                            ch_l "-Я не могу тебя винить."
                                    elif Ch_Focus is JeanX:
                                            if not Player.Male:
                                                ch_j "Ты пропустила кое-что интересное. . ."
                                            else:
                                                ch_j "Ты пропустил кое-что интересное. . ."
                                    elif Ch_Focus is StormX:
                                            if not Player.Male:
                                                ch_s ". . . но очень жаль, что ты пропустила самое интересное."
                                            else:
                                                ch_s ". . . но очень жаль, что ты пропустил самое интересное."
                                    elif Ch_Focus is JubesX:
                                            if not Player.Male:
                                                ch_v "Жаль, что ты пропустила самое интересное. . ."
                                            else:
                                                ch_v "Жаль, что ты пропустил самое интересное. . ."
                                    elif Ch_Focus is GwenX:
                                            if not Player.Male:
                                                ch_g "Жаль, что ты пропустила кое-что интересное.. . ."
                                            else:
                                                ch_g "Жаль, что ты пропустил кое-что интересное.. . ."
                                    elif Ch_Focus is BetsyX:
                                            if not Player.Male:
                                                ch_b "Что ж, тогда жаль, что ты пропустила кое-что интенресное. . ."
                                            else:
                                                ch_b "Что ж, тогда жаль, что ты пропустил кое-что интенресное. . ."
                                    elif Ch_Focus is DoreenX:
                                            if not Player.Male:
                                                ch_d "Ох, жаль, что ты пропустила кое-что интересное. . ."
                                            else:
                                                ch_d "Ох, жаль, что ты пропустил кое-что интересное. . ."
                                    elif Ch_Focus is WandaX:
                                            if not Player.Male:
                                                ch_w "Очень жаль, что ты пропустила момент, когда она. . ."
                                            else:
                                                ch_w "Очень жаль, что ты пропустил момент, когда она. . ."
                            else:
                                    $ Tempmod -= 10
                                    $ Ch_Focus.Statup("Lust", 200, -5)
                    #end "I. . . just got here?"
                call Seen_First_Peen(Ch_Focus,Partner)
        #end "noticed you were jackin"
        else:
                #you haven't been jacking it
                menu:
                    extend ""
                    "Я здесь достаточно долго.":
                            $ Ch_Focus.FaceChange("sexy", 1)
                            $ Ch_Focus.Statup("Obed", 50, 3)
                            $ Ch_Focus.Statup("Obed", 70, 2)
                            if Ch_Focus is RogueX:
                                    if not Player.Male:
                                        ch_r "Ну, я надеюсь, ты насмотрелась вдоволь. . ."
                                    else:
                                        ch_r "Ну, я надеюсь, ты насмотрелся вдоволь. . ."
                            elif Ch_Focus is KittyX:
                                    ch_k "Думаю, мы[Ch_Focus.like]устроили хорошое представление. . ."
                            elif Ch_Focus is EmmaX:
                                    ch_e "Полагаю, мы показали себя с соблазнительной стороны. . ."
                            elif Ch_Focus is LauraX:
                                    ch_l "Я не собиралась заниматься таким. . ."
                            elif Ch_Focus is JeanX:
                                    ch_j "Уверена, так и есть. . ."
                            elif Ch_Focus is StormX:
                                    ch_s "Да, пожалуй, так."
                            elif Ch_Focus is JubesX:
                                    if not Player.Male:
                                        ch_v "Было бы неприятно, если бы ты пропустила все самое интересное. . ."
                                    else:
                                        ch_v "Было бы неприятно, если бы ты пропустил все самое интересное. . ."
                            elif Ch_Focus is GwenX:
                                    $ Ch_Focus.FaceChange("angry", 1,Eyes="leftside")
                                    $ Partner.FaceChange("angry", 1,Eyes="side")
                                    if not Player.Male:
                                        ch_g "Так значит ты видела, когда я-" with vpunch
                                    else:
                                        ch_g "Так значит ты видел, когда я-" with vpunch
                                    ch_g "[[[Partner.Name] щипает ее за руку]. . ."
                                    $ Ch_Focus.FaceChange("sexy", 1)
                                    $ Partner.FaceChange("sexy")
                            elif Ch_Focus is BetsyX:
                                    ch_b "Конечно. . ."
                            elif Ch_Focus is DoreenX:
                                    ch_d "Ох, хехе. . ."
                            elif Ch_Focus is WandaX:
                                    ch_w "Надеюсь. . ."
                    "Я здесь не так давно.":
                            $ Ch_Focus.FaceChange("bemused", 1)
                            $ Ch_Focus.Statup("Love", 70, 2)
                            $ Ch_Focus.Statup("Love", 90, 1)
                            if Ch_Focus is RogueX:
                                    ch_r "Ага, ага. . ."
                            elif Ch_Focus is KittyX:
                                    ch_k "Хм, угу. . ."
                            elif Ch_Focus is EmmaX:
                                    ch_e "Не сомневаюсь. . ."
                            elif Ch_Focus is LauraX:
                                    ch_l "Хм, угу. . ."
                            elif Ch_Focus is JeanX:
                                    ch_j "Конечно. . ."
                            elif Ch_Focus is StormX:
                                    ch_s "Поверю тебе."
                            elif Ch_Focus is JubesX:
                                    ch_v "Ну конечно."
                            elif Ch_Focus is GwenX:
                                    ch_g "Угу-м. . ."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Конечно. . ."
                            elif Ch_Focus is DoreenX:
                                    ch_d "Ох. . ."
                            elif Ch_Focus is WandaX:
                                    ch_w "Конечно, конечно. . ."
                            $ Ch_Focus.Statup("Obed", 50, 2)
                            $ Ch_Focus.Statup("Obed", 70, 2)

        if not ApprovalCheck(Ch_Focus, 1350,Alt=[[WandaX],1200]):
                #If she doesn't like you enough to have you around. . .
                $ Ch_Focus.Statup("Love", 200, -5)
                $ Ch_Focus.FaceChange("angry")
                $ Ch_Focus.RecentActions.append("angry")
                $ Ch_Focus.DailyActions.append("angry")
                if Ch_Focus is RogueX:
                        if not Player.Male:
                            ch_r "Ты должна срочно уйти. Думаю, тебе стоит научиться стучать."
                        else:
                            ch_r "Ты должен срочно уйти. Думаю, тебе стоит научиться стучать."
                elif Ch_Focus is KittyX:
                        ch_k "Так. . . может[Ch_Focus.like]оставишь нас в покое?"
                elif Ch_Focus is EmmaX:
                        ch_e "Может все-таки оставишь нас в покое?"
                elif Ch_Focus is LauraX:
                        ch_l "Может, просто оставишь нас в покое?"
                elif Ch_Focus is JeanX:
                        ch_j "Так вот. . . мы бы хотели остаться наедине. . ."
                elif Ch_Focus is StormX:
                        if not Player.Male:
                            ch_s "Если это все, я бы хотела, чтобы ты ушла."
                        else:
                            ch_s "Если это все, я бы хотела, чтобы ты ушел."
                elif Ch_Focus is JubesX:
                        ch_v "Ладно, но, эм, тебе пора уходить."
                elif Ch_Focus is GwenX:
                        if not Player.Male:
                            ch_g "Эм. . . не могла бы ты оставить нас наедине?"
                        else:
                            ch_g "Эм. . . не мог бы ты оставить нас наедине?"
                elif Ch_Focus is BetsyX:
                        ch_b "Теперь можешь нас оставить? . ."
                elif Ch_Focus is DoreenX:
                        if not Player.Male:
                            ch_d "Не могла бы ты, пожалуйста, уйти? . ."
                        else:
                            ch_d "Не мог бы ты, пожалуйста, уйти? . ."
                elif Ch_Focus is WandaX:
                        ch_w "Слушай, закрой дверь, когда будешь уходить. . ."
                $ renpy.pop_call()
                $ renpy.pop_call()
                if bg_current == "bg player":
                        jump Campus_Map
                else:
                        jump Player_Room

        if Round <= 10:
                #if there's no time, return
                if Ch_Focus is RogueX:
                        ch_r "Уже слишком поздно, пора сделать перерыв."
                elif Ch_Focus is KittyX:
                        ch_k "Мы как раз собирались сделать перерыв."
                elif Ch_Focus is EmmaX:
                        ch_e "Полагаю, пришло время сделать перерыв. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Я думаю, мы могли бы сделать перерыв."
                elif Ch_Focus is JeanX:
                        ch_j "Нам бы не помешал перерыв. . ."
                elif Ch_Focus is StormX:
                        ch_s "Пожалуй, мы как раз собирались сделать перерыв. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Однако, нам нужно отвлечься. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Но тебе уже поздновато присоединяться к нам. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Жаль, что уже так поздно. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Мы все равно собирались остановиться. . ."
                elif Ch_Focus is WandaX:
                        ch_w "В любом случае, мы вроде как хотели сделать перерыв. . ."
                return
        $ Situation = "interrupted"

label LesScene(Bonus = 0,BO=[]): #rkeljsvgbdw
#        $ Girl = GirlCheck(Girl)
#        call Shift_Focus(Girl)

        if not Ch_Focus.Action:
                #this is often called by the sex menu, and reverts if she's worn out.
                call Sex_Basic_Dialog(Ch_Focus,"tired")
                return

        if Partner not in TotalGirls:
                $ Partner = 0
                python:
                    for BX in TotalGirls:
                        if BX.Loc == bg_current and BX is not Ch_Focus:
                                Partner = BX
                                break
        if Ch_Focus.LesWatch:
                $ Tempmod += 10
        elif Ch_Focus.Les:
                $ Tempmod += 5
        if Ch_Focus.SEXP >= 50:
                $ Tempmod += 25
        elif Ch_Focus.SEXP >= 30:
                $ Tempmod += 15
        elif Ch_Focus.SEXP >= 15:
                $ Tempmod += 5

        if Ch_Focus.Lust >= 90:
                $ Tempmod += 5
        elif Ch_Focus.Lust >= 75:
                $ Tempmod += 5

        elif Ch_Focus.Inbt >= 750:
                $ Tempmod += 5

        if Ch_Focus is WandaX or Partner is WandaX:
                $ Tempmod += 20

        if "exhibitionist" in Ch_Focus.Traits:
                $ Tempmod += (3*Taboo)

        if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
                $ Tempmod += 10
        elif "ex" in Ch_Focus.Traits:
                $ Tempmod -= 40

        if Ch_Focus is JeanX:
                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                call Girl_Whammy(Partner)
        elif Partner is JeanX:
                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                call Girl_Whammy(Ch_Focus)

        $ Line = Ch_Focus.GirlLikeCheck(Partner)
        if Line >= 900:
                $ Bonus += 150
        elif Line >= 800 or "poly "+Partner.Tag in Ch_Focus.Traits:
                $ Bonus += 100
        elif Line >= 700:
                $ Bonus += 50
        elif Line <= 200:
                $ Bonus -= 200
        elif Line <= 500:
                $ Bonus -= 100
        $ Partner.DrainWord("unseen",1,0) #She sees you, so remove unseens
        $ Line = 0

        $ Ch_Focus.AddWord(1,"noticed "+Partner.Tag,"noticed "+Partner.Tag) #ie $ Ch_Focus.RecentActions.append("noticed Partner")
        $ Partner.AddWord(1,"noticed "+Ch_Focus.Tag,"noticed "+Ch_Focus.Tag) #ie $ Partner.RecentActions.append("noticed Ch_Focus")

        if bg_current in PersonalRooms:
                $ Taboo = 0
                $ Ch_Focus.Taboo = 0
                $ Partner.Taboo = 0
        if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
                $ Tempmod -= 5 * Ch_Focus.ForcedCount

        if RogueX.Loc == bg_current and KittyX.Loc == bg_current:
                    #if both Rogue and Kitty are involved. . .
                    if Ch_Focus in (RogueX,KittyX) and "KittyPuss" in RogueX.History:
                        menu:
                            "Переиграть сцену их совместной учебы?"
                            "Да":
                                    call Rogue_and_Kitty_Redux
                                    return
                            "Нет":
                                    pass
        # end Rogue_and_Kitty_Redux

        $ Approval = ApprovalCheck(Ch_Focus, 1350, TabM = 2, Bonus = Bonus) # 1350, 1500, 1650, Taboo -800

        $ Ch_Focus.DrainWord("unseen",1,0) #She sees you, so remove unseens

        if Situation == "interrupted":
            menu:
                extend ""
                "Пожалуй, мне пора идти. . .":
                        $ Ch_Focus.Statup("Love", 80, 3)
                        if Approval >= 2:
                                # if lead girl is very much in
                                if Ch_Focus is RogueX:
                                        ch_r "Я не говорила, что тебя обязательно уходить. . ."
                                elif Ch_Focus is KittyX:
                                        ch_k "Хммм, не знаю, стоит ли. . ."
                                elif Ch_Focus is EmmaX:
                                        ch_e "Думаю, тебе стоит задержаться. . ."
                                elif Ch_Focus is LauraX:
                                        ch_l "Хммм, не знаю, стоит ли. . ."
                                elif Ch_Focus is JeanX:
                                        ch_j "Тебе не нужно. . ."
                                elif Ch_Focus is StormX:
                                        ch_s "В этом нет необходимости."
                                elif Ch_Focus is JubesX:
                                        if not Player.Male:
                                            ch_v "Илииии. . . ты могла бы присоединиться к нам?"
                                        else:
                                            ch_v "Илииии. . . ты мог бы присоединиться к нам?"
                                elif Ch_Focus is GwenX:
                                        if not Player.Male:
                                            ch_g "Возможно, у нас найдется место для еще одной. . ."
                                        else:
                                            ch_g "Возможно, у нас найдется место для еще одного. . ."
                                elif Ch_Focus is BetsyX:
                                        ch_b "Мы -могли бы- найти место и для тебя. . ."
                                elif Ch_Focus is DoreenX:
                                        ch_d "Ну. . . я не уверена, но мне кажется, тебе стоит остаться. . ."
                                elif Ch_Focus is WandaX:
                                        ch_w "Ты можешь не уходить. . ."
                                call Les_Response(Partner,Ch_Focus,3,B2=Bonus)
                                if not _return:
                                        return
                        else:
                                # If lead girl is only so/so, but Partner is on board, she tries to convince lead girl
                                call Les_Response(Partner,Ch_Focus,1,B2=Bonus)
                                if not _return:
                                        #this is the default reaction if Partner is not into it either
                                        if Approval:
                                                if Ch_Focus is RogueX:
                                                        ch_r "Пожалуй, ты можешь присоединиться. . ."
                                                elif Ch_Focus is KittyX:
                                                        if not Player.Male:
                                                            ch_k "Ты могла бы остаться. . ."
                                                        else:
                                                            ch_k "Ты мог бы остаться. . ."
                                                elif Ch_Focus is EmmaX:
                                                        if not Player.Male:
                                                            ch_e "Ты могла бы остаться хотя бы ненадолго. . ."
                                                        else:
                                                            ch_e "Ты мог бы остаться хотя бы ненадолго. . ."
                                                elif Ch_Focus is LauraX:
                                                        ch_l "Ты можешь расслабиться с нами."
                                                elif Ch_Focus is JeanX:
                                                        ch_j "Ты еще можешь остаться. . ."
                                                elif Ch_Focus is StormX:
                                                        if not Player.Male:
                                                            ch_s "Тогда ты могла бы остаться и немного побеседовать с нами."
                                                        else:
                                                            ch_s "Тогда ты мог бы остаться и немного побеседовать с нами."
                                                elif Ch_Focus is JubesX:
                                                        ch_v "Ну, тогда просто проведи с нами немного времени."
                                                elif Ch_Focus is GwenX:
                                                        if not Player.Male:
                                                            ch_g "Наверное, ты могла бы провести немного времени с нами?"
                                                        else:
                                                            ch_g "Наверное, ты мог бы провести немного времени с нами?"
                                                elif Ch_Focus is BetsyX:
                                                        if not Player.Male:
                                                            ch_b "Ты могла бы остаться с нами ненадолго. . ."
                                                        else:
                                                            ch_b "Ты мог бы остаться с нами ненадолго. . ."
                                                elif Ch_Focus is DoreenX:
                                                        if not Player.Male:
                                                            ch_d "Думаю, ты могла бы посидеть немного с нами. . ."
                                                        else:
                                                            ch_d "Думаю, ты мог бы посидеть немного с нами. . ."
                                                elif Ch_Focus is WandaX:
                                                        ch_w "Думаю, мы могли бы провести время все вместе. . ."
                                                return
                                        else:
                                                if Ch_Focus is RogueX:
                                                        ch_r "Да, наверное, это хорошая идея. . ."
                                                elif Ch_Focus is KittyX:
                                                        ch_k "Пожалуй, что так. . ."
                                                elif Ch_Focus is EmmaX:
                                                        ch_e "Полагаю, что так. . ."
                                                elif Ch_Focus is LauraX:
                                                        ch_l "Ага. . ."
                                                elif Ch_Focus is JeanX:
                                                        ch_j "Ох, хорошо. . ."
                                                elif Ch_Focus is StormX:
                                                        ch_s "Извини, [Ch_Focus.Petname]. Возможно, в другой раз."
                                                elif Ch_Focus is JubesX:
                                                        ch_v "О, облом, ну тогда до встречи."
                                                elif Ch_Focus is GwenX:
                                                        ch_g "Оу, ну, тогда до встречи?"
                                                elif Ch_Focus is BetsyX:
                                                        ch_b "Что ж, до встречи, [Ch_Focus.Petname]. . ."
                                                elif Ch_Focus is DoreenX:
                                                        ch_d "Ладно, увидимся, [Ch_Focus.Petname]. . ."
                                                elif Ch_Focus is WandaX:
                                                        ch_w "Слушай, закрой дверь, когда будешь уходить. . ."
                                                $ renpy.pop_call()
                                                $ renpy.pop_call()
                                                if bg_current == "bg player":
                                                        jump Campus_Map
                                                else:
                                                        jump Player_Room
                                elif not Approval:
                                        #if Partner is in, but not lead girl
                                        if Ch_Focus is RogueX:
                                                ch_r "Извини, [Ch_Focus.Petname], я не хочу устраивать -Шоу-."
                                        elif Ch_Focus is KittyX:
                                                ch_k "Извини, [Ch_Focus.Petname], думаю, мы хотим сохранить все в тайне."
                                        elif Ch_Focus is EmmaX:
                                                ch_e "Мне жаль, [Ch_Focus.Petname], полагаю, мы хотели бы сохранить все в тайне."
                                        elif Ch_Focus is LauraX:
                                                ch_l "Извини, [Ch_Focus.Petname], может, в другой раз."
                                        elif Ch_Focus is JeanX:
                                                ch_j "Надеюсь, тебе понравилось увиденное, но сейчас мы немного заняты. . ."
                                        elif Ch_Focus is StormX:
                                                if not Player.Male:
                                                    ch_s "Боюсь, я бы предпочла, чтобы ты ушла."
                                                else:
                                                    ch_s "Боюсь, я бы предпочла, чтобы ты ушел."
                                        elif Ch_Focus is JubesX:
                                                ch_v "Извини, не интересно."
                                        elif Ch_Focus is GwenX:
                                                ch_g "Не хочу быть занудой, но я не могу. . ."
                                        elif Ch_Focus is BetsyX:
                                                ch_b "Боюсь, тебе стоит уйти, [Ch_Focus.Petname]. . ."
                                        elif Ch_Focus is DoreenX:
                                                ch_d "Хехе, извини, но я не могу при тебе, [Ch_Focus.Petname]. . ."
                                        elif Ch_Focus is WandaX:
                                                ch_w "Мне кажется, это плохая идея. . ."
                                        return
                                elif not Ch_Focus.Action:
                                        #if she's tired out. . .
                                        if Ch_Focus is RogueX:
                                                ch_r "Извини, [Ch_Focus.Petname], Я слишком устала. . ."
                                        elif Ch_Focus is KittyX:
                                                ch_k "Извини, [Ch_Focus.Petname], Я уже устала. . ."
                                        elif Ch_Focus is EmmaX:
                                                ch_e "Мне жаль, [Ch_Focus.Petname], но мне нужен перерыв. . ."
                                        elif Ch_Focus is LauraX:
                                                ch_l "Извини, [Ch_Focus.Petname], похоже, нам нужен перерыв. . ."
                                        elif Ch_Focus is JeanX:
                                                ch_j "Мне бы не помешал перерыв. . ."
                                        elif Ch_Focus is StormX:
                                                ch_s "Все-таки, мне нужно немного передохнуть."
                                        elif Ch_Focus is JubesX:
                                                ch_v "Я немного устала."
                                        elif Ch_Focus is GwenX:
                                                ch_g "Может быть, сначала немного передохнем?"
                                        elif Ch_Focus is BetsyX:
                                                ch_b "Возможно, после небольшого отдыха. . ."
                                        elif Ch_Focus is DoreenX:
                                                ch_d "Извини, я немного устала. . ."
                                        elif Ch_Focus is WandaX:
                                                ch_w "Прости, я немного переутомилась. . ."
                                        return
                                else:
                                        #if it all worked out. . .
                                        if Ch_Focus is RogueX:
                                                ch_r "Хорошо."
                                        elif Ch_Focus is KittyX:
                                                ch_k "Конечно."
                                        elif Ch_Focus is EmmaX:
                                                ch_e "Отлично."
                                        elif Ch_Focus is LauraX:
                                                ch_l "Конечно."
                                        elif Ch_Focus is JeanX:
                                                ch_j "Хорошо."
                                        elif Ch_Focus is StormX:
                                                ch_s "Ох, превосходно."
                                        elif Ch_Focus is JubesX:
                                                ch_v "Хорошо."
                                        elif Ch_Focus is GwenX:
                                                ch_g "Здорово."
                                        elif Ch_Focus is BetsyX:
                                                ch_b "Ох, хорошо!"
                                        elif Ch_Focus is DoreenX:
                                                ch_d "Здорово!"
                                        elif Ch_Focus is WandaX:
                                                if not Player.Male:
                                                    ch_w "Распутница. . ."
                                                else:
                                                    ch_w "Распутник. . ."
                        #if it passed the hurdles. . .
                        jump Les_Prep

                "Так, может мне присоедениться к вам, девочки?" if Player.Semen and Ch_Focus.Action:
                        $ Ch_Focus.FaceChange("sexy")
                        if Ch_Focus is RogueX:
                                ch_r "Ты хочешь нам что-то предложить?"
                        elif Ch_Focus is KittyX:
                                if not Player.Male:
                                    ch_k "Мммм, чего бы ты хотела?"
                                else:
                                    ch_k "Мммм, чего бы ты хотел?"
                        elif Ch_Focus is EmmaX:
                                ch_e "Ох? Есть предложения?"
                        elif Ch_Focus is LauraX:
                                ch_l "Ох, есть идеи?"
                        elif Ch_Focus is JeanX:
                                ch_j "Ох? Говори. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Думаю, это можно устроить. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Нууу, я думаю, мы могли бы что-нибудь придумать. . ."
                        elif Ch_Focus is GwenX:
                                ch_g "Не думаю, что я буду против. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Ох, это может быть просто потрясающе. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "Мне нравится ход твоих мыслей. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Конечно, почему нет?"
                        $ Situation = "join"
                        return                      #returns to sexmenu=
                "Могу я посмотреть еще немного?":
                        $ Ch_Focus.FaceChange("bemused", 1)
            #End "Interrupted" content.

        #first time
        if not Ch_Focus.LesWatch:
                $ Ch_Focus.FaceChange("surprised", 1,Mouth="kiss")
                if Ch_Focus is RogueX:
                        ch_r "Ты хочешь смотреть на нас, пока мы развлекаемся?"
                elif Ch_Focus is KittyX:
                        ch_k "Ты хочешь наблюдать за нашими играми?"
                elif Ch_Focus is EmmaX:
                        ch_e "Ты хочешь смотреть, как мы ублажаем друг друга?"
                elif Ch_Focus is LauraX:
                        ch_l "Ты хочешь наблюдать за нашими играми?"
                elif Ch_Focus is JeanX:
                        ch_j "Ох, так значит ты хочешь наблюдать за нами?. . ."
                elif Ch_Focus is StormX:
                        ch_s "Ох, так ты хочешь понаблюдать пока мы вместе?"
                elif Ch_Focus is JubesX:
                        ch_v "О, я и она? Вместе?"
                elif Ch_Focus is GwenX:
                        ch_g "Хочешь собственный фанфик?"
                        ch_g "Гвенпул и [Partner.Tag]!"
                elif Ch_Focus is BetsyX:
                        ch_b "Ох, ты хочешь посмотреть, как [Partner.Name]. . . сплетется со мной?"
                elif Ch_Focus is DoreenX:
                        ch_d "Ох. . . ты хочешь посмотреть, как [Partner.Name]. . . займется со мной любовью?"
                elif Ch_Focus is WandaX:
                        ch_w "Хех, хочешь посмотреть, как мы с [Partner.Name] ублажаем друг друга?"
                if Ch_Focus.Forced:
                        $ Ch_Focus.FaceChange("sad")
                        if Ch_Focus is RogueX:
                                ch_r "И -только- наблюдать?"
                        elif Ch_Focus is KittyX:
                                ch_k "И -только- наблюдать, да?"
                        elif Ch_Focus is EmmaX:
                                ch_e "Но не более того?"
                        elif Ch_Focus is LauraX:
                                ch_l "-Только- ведь наблюдать, верно?"
                        elif Ch_Focus is JeanX:
                                ch_j "-Только- наблюдать. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Только смотреть?"
                        elif Ch_Focus is JubesX:
                                ch_v "Только наблюдать?"
                        elif Ch_Focus is GwenX:
                                ch_g "Хочешь -только- наблюдать?"
                        elif Ch_Focus is BetsyX:
                                ch_b "-Только- смотреть?"
                        elif Ch_Focus is DoreenX:
                                ch_d "И -просто- смотреть?"
                        elif Ch_Focus is WandaX:
                                ch_w "И -только- смотреть?"
        #end if first time. . .

        call expression Ch_Focus.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
        if not Player.Male and "girltalk" not in Ch_Focus.History:
                return

        if Approval and (Partner is RogueX or Ch_Focus is RogueX) and "touch" not in RogueX.Traits:
                if Ch_Focus is RogueX:
                        ch_r "Я не знаю, разве мое прикосновение. . . не опасно?"
                        ch_p "Не волнуйся, я могу обезвредить его."
                        ch_r "Пожалуй, твоя правда. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Я не знаю, разве. . . прикосновения Роуг не опасны?"
                        ch_p "Не волнуйся, я могу обезвредить ее способности."
                        ch_k "Ну, пожалуй, твоя правда. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Я не уверена, прикосновения Роуг могут быть. . . разрушительными?"
                        ch_p "Не волнуйся, я могу обезвредить ее способности."
                        if not Player.Male:
                            ch_e "Ох, полагаю, ты способна на это. . ."
                        else:
                            ch_e "Ох, полагаю, ты способен на это. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Не знаю, прикосновение Роуг могут быть. . . жгучими. . ."
                        ch_p "Не волнуйся, я могу обезвредить ее способности."
                        if not Player.Male:
                            ch_l "Ну, думаю, ты права. . ."
                        else:
                            ch_l "Ну, думаю, ты прав. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Думаю, я могу использовать свой ТК, чтобы избежать прямого контакта. . ."
                elif Ch_Focus is StormX:
                        ch_s "Я не уверена, прикосновения Роуг могут быть проблемными."
                        ch_p "Не волнуйся, я могу обезвредить ее способности."
                        ch_s "Это верно. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Я бы не хотела проблем с. . . Роуг."
                        ch_p "Не волнуйся, я могу обезвредить ее способности."
                        ch_v "О, это подойдет."
                elif Ch_Focus is GwenX:
                        ch_g "Я немного знаю о. . . проблеме Роуг."
                        ch_g "Она не помешает?"
                        ch_p "Не волнуйся, я могу обезвредить ее способности."
                        ch_g "А, да, я забыла. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Но как быть с. . . деликатным состоянием Роуг?"
                        ch_p "Не волнуйся, я могу обезвредить ее способности."
                        ch_b "Ох, замечательно. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Не хочу портить настроение, но как быть с [RogueX.Name]?"
                        ch_d "Мы же не можем прикасаться друг к другу, да? Это ведь еще проблема?"
                        ch_p "Не волнуйся, я могу обезвредить ее способности."
                        ch_b "О, здорово!"
                elif Ch_Focus is WandaX:
                        ch_w "Хочу уточнить, к [RogueX.Name] ведь все еще нельзя прикасаться?"
                        ch_p "Не волнуйся, я могу обезвредить ее способности."
                        ch_b "О, клево!"
        #end "can Rogue touch" check

        if not Ch_Focus.LesWatch and Approval:
                #First time dialog
                if Ch_Focus.Forced:
                        $ Ch_Focus.FaceChange("sad")
                        $ Ch_Focus.Statup("Love", 70, -3, 1)
                        $ Ch_Focus.Statup("Love", 20, -2, 1)
                elif Bonus >= 100:
                        $ Ch_Focus.FaceChange("sly", Eyes="side")
                        if Ch_Focus is RogueX:
                                ch_r "Хм, вообще-то мне это может понравиться больше, чем ты думаешь. . ."
                        elif Ch_Focus is KittyX:
                                ch_k "Хихи, ты не знаешь, о чем просишь. . ."
                        elif Ch_Focus is EmmaX:
                                ch_e "Это будет не в первый раз. . ."
                        elif Ch_Focus is LauraX:
                                ch_l "Ну, ты будешь в восторге. . ."
                        elif Ch_Focus is JeanX:
                                ch_j "Я не откажусь от возможности. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Я, безусловно, более чем открыта для этого замысла."
                        elif Ch_Focus is JubesX:
                                ch_v "О, ага, без б."
                        elif Ch_Focus is GwenX:
                                $ Ch_Focus.FaceChange("surprised")
                                if not Player.Male:
                                    ch_g "Ты явно не заглядывала мою папку с порно."
                                    $ Ch_Focus.FaceChange("sly")
                                    ch_g "А может и заглядывала."
                                else:
                                    ch_g "Ты явно не заглядывал мою папку с порно."
                                    $ Ch_Focus.FaceChange("sly")
                                    ch_g "А может и заглядывал."
                        elif Ch_Focus is BetsyX:
                                ch_b "Ты можешь удивиться тому, чему я научилась в государственных школах."
                        elif Ch_Focus is DoreenX:
                                ch_d "Я, эм. . . не против. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Это вообще не проблема."
                elif Ch_Focus.Love >= (Ch_Focus.Obed + Ch_Focus.Inbt):
                        $ Ch_Focus.FaceChange("sexy")
                        $ Ch_Focus.Brows = "sad"
                        $ Ch_Focus.Mouth = "smile"
                        if Ch_Focus is RogueX:
                                ch_r "В последнее время, я не особо задумывалась о том, чтобы быть с другими людьми. . ."
                        elif Ch_Focus is KittyX:
                                ch_k "Если честно, я и не думала устраивать такое. . ."
                        elif Ch_Focus is EmmaX:
                                if not Player.Male:
                                    ch_e "Я не думала, что ты способна предложить подобное. . ."
                                else:
                                    ch_e "Я не думала, что ты способен предложить подобное. . ."
                        elif Ch_Focus is LauraX:
                                ch_l "Честно говоря, я и не думала устраивать такое. . ."
                        elif Ch_Focus is JeanX:
                                ch_j "Я таким не увлекаюсь. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Я могла бы это сделать, если тебя интересует подобное . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Думаю, я могла бы."
                        elif Ch_Focus is GwenX:
                                ch_g "Звучит довольно весело."
                        elif Ch_Focus is BetsyX:
                                ch_b "Обычно у меня нет зрителей. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "Я не уверена, стоит ли заниматься подобных перед зрителями. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Хотя я не уверена, хочу ли видеть тебя в этой комнате. . ."
                elif Ch_Focus.Obed >= Ch_Focus.Inbt:
                        $ Ch_Focus.FaceChange("normal")
                        if Ch_Focus is RogueX:
                                ch_r "Если ты этого хочешь, [Ch_Focus.Petname]. . ."
                        elif Ch_Focus is KittyX:
                                ch_k "Если ты этого хочешь, [Ch_Focus.Petname]. . ."
                        elif Ch_Focus is EmmaX:
                                ch_e "Если это порадует тебя, [Ch_Focus.Petname]. . ."
                        elif Ch_Focus is LauraX:
                                ch_l "Я не против, [Ch_Focus.Petname]. . ."
                        elif Ch_Focus is JeanX:
                                ch_j "Конечно. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Убедил. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Если тебе такое нравится. . ."
                        elif Ch_Focus is GwenX:
                                ch_g "Я согласна."
                        elif Ch_Focus is BetsyX:
                                ch_b "Если нужно. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "Эм. . . Ладно. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Что ж, ладно."
                else: # Uninhibited
                        $ Ch_Focus.FaceChange("sad")
                        $ Ch_Focus.Mouth = "smile"
                        if Ch_Focus is RogueX:
                                ch_r "Думаю, может быть весело, когда ты смотришь. . ."
                        elif Ch_Focus is KittyX:
                                ch_k "Думаю, может быть весело, когда ты смотришь. . ."
                        elif Ch_Focus is EmmaX:
                                ch_e "Мне нравится при зрителях. . ."
                        elif Ch_Focus is LauraX:
                                ch_l "Я не против. . ."
                        elif Ch_Focus is JeanX:
                                ch_j "Я не против зрителей. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Я открыта для этого предложения."
                        elif Ch_Focus is JubesX:
                                ch_v "Конечно, наверное. . ."
                        elif Ch_Focus is GwenX:
                                ch_g "Звучит довольно весело."
                        elif Ch_Focus is BetsyX:
                                ch_b "Пожалуй, при зрителях может быть интересно."
                        elif Ch_Focus is DoreenX:
                                ch_d "Звучит довольно. . . весело. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Не угрожай мне хорошим времяпрепровождением. . ."
                #End first time with approval dialogs

        elif Approval:
                    #Second time+ initial dialog
                    if Ch_Focus.Forced:
                            $ Ch_Focus.FaceChange("sad")
                            $ Ch_Focus.Statup("Love", 70, -3, 1)
                            $ Ch_Focus.Statup("Love", 20, -2, 1)
                            if Ch_Focus is RogueX:
                                    ch_r "Так ты хочешь снова понаблюдать за мной с девушкой?"
                            elif Ch_Focus is KittyX:
                                if Player.Male:
                                    ch_k "Тебе походу очень нравятся наши девичьи забавы, да?"
                                else:
                                    ch_k "Тебе просто нравится смотреть, да?"
                            elif Ch_Focus is EmmaX:
                                    ch_e "Тебе понравилось последнее представление?"
                            elif Ch_Focus is LauraX:
                                    ch_l "Тебя это так волнует?"
                            elif Ch_Focus is JeanX:
                                    ch_j "Нравятся наши -шоу-, а? . ."
                            elif Ch_Focus is StormX:
                                    ch_s "Тебе нравятся наши маленькие игры?"
                            elif Ch_Focus is JubesX:
                                    ch_v "Тебе такое нравится?"
                            elif Ch_Focus is GwenX:
                                    ch_g "О, я понимаю, как это бывает. . ."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Ты хочешь снова посмотреть нас?"
                            elif Ch_Focus is DoreenX:
                                    ch_d "Значит, хочешь снова посмотреть на нас. . ."
                            elif Ch_Focus is WandaX:
                                    ch_w "Хочешь снова понаблюдать за нами?"
                    elif Approval and "lesbian" in Ch_Focus.RecentActions:
                            $ Ch_Focus.FaceChange("sexy", 1)
                            if Ch_Focus is RogueX:
                                    ch_r "Думаю, мы могли бы повторить. . ."
                            elif Ch_Focus is KittyX:
                                    ch_k "Еще немного не повредит. . ."
                            elif Ch_Focus is EmmaX:
                                    if not Player.Male:
                                        ch_e "Хм, вернулась за добавкой?"
                                    else:
                                        ch_e "Хм, вернулся за добавкой?"
                            elif Ch_Focus is LauraX:
                                    ch_l "Я не против еще немного. . ."
                            elif Ch_Focus is JeanX:
                                    ch_j "Хорошо, тогда продолжим. . ."
                            elif Ch_Focus is StormX:
                                    ch_s "Хорошо. . ."
                            elif Ch_Focus is JubesX:
                                    ch_v "Думаю, мы можем пойти на это ради тебя. . ."
                            elif Ch_Focus is GwenX:
                                    ch_g "Лан."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Конечно."
                            elif Ch_Focus is DoreenX:
                                    ch_d "Я не против. . ."
                            elif Ch_Focus is WandaX:
                                    ch_w "Не думаю, что это может быть проблемой."
                            jump Les_Prep
                    elif Approval and "lesbian" in Ch_Focus.DailyActions:
                            $ Ch_Focus.FaceChange("sexy", 1)
                            $ Line = renpy.random.choice(["Так понравилось представление?",
                                    "Тебе все мало?",
                                    "Я не против зрителей. . ."])
                            call AnyLine(Ch_Focus,Line)
                    elif Ch_Focus.Les < 3:
                            $ Ch_Focus.FaceChange("sexy", 1)
                            $ Ch_Focus.Brows = "confused"
                            if Ch_Focus is RogueX:
                                    ch_r "Любишь наблюдать, да?"
                            elif Ch_Focus is KittyX:
                                    ch_k "Походу, тебе очень нравится наблюдать."
                            elif Ch_Focus is EmmaX:
                                    ch_e "А ты любитель наблюдать."
                            elif Ch_Focus is LauraX:
                                    ch_l "Любитель понаблюдать."
                            elif Ch_Focus is JeanX:
                                    ch_j "Не можешь насытиться мной. . ."
                            elif Ch_Focus is StormX:
                                    ch_s "Тебе нравятся наши маленькие игры?"
                            elif Ch_Focus is JubesX:
                                    ch_v "Я не знаю. . ."
                            elif Ch_Focus is GwenX:
                                    ch_g "Это становится регулярным."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Кажется, тебе понравилось представление."
                            elif Ch_Focus is DoreenX:
                                    ch_d "Думаю, тебе понравилось в прошлый раз. . ."
                            elif Ch_Focus is WandaX:
                                    ch_w "Хм, тебе, похоже, это нравится. . ."
                    else:
                            $ Ch_Focus.FaceChange("sexy", 1)
                            $ Ch_Focus.ArmPose = 2
                            $ Line = renpy.random.choice(["Похоже, тебе нравится наблюдать.",
                                    "Значит, ты хочешь, чтобы мы снова пошалили?",
                                    "Хочешь посмотреть еще немного?",
                                    "Хочешь, чтобы я занялась ей?"])
                            call AnyLine(Ch_Focus,Line)
                    $ Line = 0
                    #End second time+ initial dialog

        if Approval >= 2:
                    #If she's into it. . .
                    if Ch_Focus.Forced:
                            $ Ch_Focus.FaceChange("sad")
                            $ Ch_Focus.Statup("Obed", 90, 1)
                            $ Ch_Focus.Statup("Inbt", 60, 1)
                            if Ch_Focus is RogueX:
                                    ch_r "Ладно, я не против, если она согласна. . ."
                            elif Ch_Focus is KittyX:
                                    ch_k "Ну, думаю, если она согласна с этим. . ."
                            elif Ch_Focus is EmmaX:
                                    ch_e "Пока это устраивает нас обеих. . ."
                            elif Ch_Focus is LauraX:
                                    ch_l "Не самый плохой способ провести время. . ."
                            elif Ch_Focus is JeanX:
                                    ch_j "Ну, могло быть и хуже. . ."
                            elif Ch_Focus is StormX:
                                    ch_s "Пожалуй, ничего плохого от этого не случится."
                            elif Ch_Focus is JubesX:
                                    ch_v "Могло быть и хуже. . ."
                            elif Ch_Focus is GwenX:
                                    ch_g "Думаю, мы хотя бы нашли мне хорошего партнера. . ."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Пожалуй, это не худшее времяпрепровождение."
                            elif Ch_Focus is DoreenX:
                                    ch_d "Ладно, думаю, можно, если она не против. . ."
                            elif Ch_Focus is WandaX:
                                    ch_w "Я думаю, можно, если она к этому готова. . ."
                    else:
                            $ Ch_Focus.FaceChange("sexy", 1)
                            $ Ch_Focus.Statup("Love", 90, 1)
                            $ Ch_Focus.Statup("Inbt", 50, 3)
                            if Situation == "interrupted":
                                    if Ch_Focus is RogueX:
                                            ch_r "Я могла бы больше. . ."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Ну, я думаю, мы могли бы продолжить. . ."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Что ж, я полагаю, мы могли бы продолжить. . ."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Хорошо, я могла бы продолжить. . ."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Я хотела бы попробовать еще несколько вещей. . ."
                                    elif Ch_Focus is StormX:
                                            ch_s "Тогда иди сюда, [Partner.Name]."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Тогда продолжим?"
                                    elif Ch_Focus is GwenX:
                                            ch_g "Все так плохо, [Partner.Name]?"
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Пожалуй, мы могли бы продолжить. . ."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Думаю, мы могли бы продолжить. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Ладно, продолжим. . ."
                            else:
                                    $ Line = renpy.random.choice(["Ну. . . ладно.",
                                        "Я ничего не имею против того, чтобы быть с ней.. . .",
                                        "A",
                                        "Конечно.",
                                        "Пожалуй. . .",
                                        "Хех, хорошо."])
                                    if Line == "A":
                                            if Ch_Focus is RogueX:
                                                    ch_r "Возможно, мне это все равно было нужно. . ."
                                            elif Ch_Focus is KittyX:
                                                    ch_k "В любом случае мне это было нужно. . ."
                                            elif Ch_Focus is EmmaX:
                                                    ch_e "Я не против близости с ней. . ."
                                            elif Ch_Focus is LauraX:
                                                    ch_l "Мне вроде как нужно было выпустить пар. . ."
                                            elif Ch_Focus is JeanX:
                                                    ch_j "Ты еще не видел, что она вытворяет. . ."
                                            elif Ch_Focus is StormX:
                                                    ch_s "Тебе понравится."
                                            elif Ch_Focus is JubesX:
                                                    ch_v "Мне все равно нужно было немного внимания."
                                            elif Ch_Focus is GwenX:
                                                    ch_g "Ладно, смотри, тебе понравится. . ."
                                            elif Ch_Focus is BetsyX:
                                                    ch_b "Смотри не пропусти ни одного момента."
                                            elif Ch_Focus is DoreenX:
                                                    ch_d "Вперед!"
                                            elif Ch_Focus is WandaX:
                                                    ch_w "Ладно, начнем!"
                                    else:
                                            call AnyLine(Ch_Focus,Line)
                                    $ Line = 0
                    $ Ch_Focus.Statup("Obed", 20, 1)
                    $ Ch_Focus.Statup("Obed", 60, 1)
                    $ Ch_Focus.Statup("Inbt", 70, 2)
                    jump Les_Partner
                    #end instant approval
        else:
            #If she's not into it, but maybe. . .
            if Ch_Focus is RogueX:
                    ch_r "Хотя я в этом не уверена, [Ch_Focus.Petname]."
            elif Ch_Focus is KittyX:
                    ch_k "Я не знаю, [Ch_Focus.Petname]."
            elif Ch_Focus is EmmaX:
                    ch_e "Я не уверена в этом, [Ch_Focus.Petname]."
            elif Ch_Focus is LauraX:
                    ch_l "Я не знаю, [Ch_Focus.Petname]."
            elif Ch_Focus is JeanX:
                    ch_j "Хмм. . . Я не знаю. . ."
            elif Ch_Focus is StormX:
                    ch_s "Я не уверена. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Но. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Я не уверена, мне как-то неловко. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Мне не совсем нравится эта идея. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Я, эм. . . не уверена. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Я не уверена, нравится ли нам эта идея. . ."
            menu:
                "Может, в другой раз?":
                        $ Ch_Focus.FaceChange("sexy", 1)
                        if Bonus >= 100:
                                $ Ch_Focus.Statup("Inbt", 90, 5)
                                if Ch_Focus is RogueX:
                                        ch_r "Ну. . . возможно, когда-нибудь. . ."
                                elif Ch_Focus is KittyX:
                                        ch_k "Когда-нибудь. . ."
                                elif Ch_Focus is EmmaX:
                                        ch_e "Все может быть. . ."
                                elif Ch_Focus is LauraX:
                                        ch_l "Возможно. . ."
                                elif Ch_Focus is JeanX:
                                        ch_j "Конечно, может быть. . ."
                                elif Ch_Focus is StormX:
                                        ch_s "Да, возможно, в другой раз."
                                elif Ch_Focus is JubesX:
                                        ch_v "Конечно, может быть."
                                elif Ch_Focus is GwenX:
                                        ch_g "О, это -определенно- когда-нибудь произойдет, правда, [Partner.Name]?"
                                        ch_g "Ага, ей нравится эта мысль."
                                elif Ch_Focus is BetsyX:
                                        ch_b "Все может быть."
                                elif Ch_Focus is DoreenX:
                                        ch_d "Ох. . . эм, конечно. . ."
                                elif Ch_Focus is WandaX:
                                        ch_w "Ох, конечно."
                        elif Bonus >= 0:
                                $ Ch_Focus.GLG(Partner,800,3,1)
                                if Ch_Focus is RogueX:
                                        ch_r "Эм, я не знаю. . . может быть?"
                                elif Ch_Focus is KittyX:
                                        ch_k "Эм, я не знаю. . . может быть?"
                                elif Ch_Focus is EmmaX:
                                        ch_e "Никогда не знаешь наверняка. . ."
                                elif Ch_Focus is LauraX:
                                        ch_l "Эм, я не знаю. . ."
                                elif Ch_Focus is JeanX:
                                        ch_j "Хммм. . . может быть. . ."
                                elif Ch_Focus is StormX:
                                        ch_s "Хмм. . . возможно."
                                elif Ch_Focus is JubesX:
                                        ch_v "Конечно, может быть."
                                elif Ch_Focus is GwenX:
                                        ch_g "О, это -определенно- когда-нибудь произойдет, правда, [Partner.Name]?"
                                        ch_g "Ага, ей нравится эта мысль."
                                elif Ch_Focus is BetsyX:
                                        ch_b "Я подумаю над этим."
                                elif Ch_Focus is DoreenX:
                                        ch_d "Ох. . . эм, конечно. . ."
                                elif Ch_Focus is WandaX:
                                        ch_w "Возможно. . ."
                        else:
                                $ Ch_Focus.FaceChange("angry", 1, Eyes="side")
                                if Ch_Focus is RogueX:
                                        ch_r "Не думаю, что это когда-нибудь произойдет. . ."
                                elif Ch_Focus is KittyX:
                                        ch_k "Скорее всего, нет."
                                elif Ch_Focus is EmmaX:
                                        ch_e "Вряд ли."
                                elif Ch_Focus is LauraX:
                                        ch_l "Скорее всего, нет."
                                elif Ch_Focus is JeanX:
                                        ch_j "Вряд ли. . ."
                                elif Ch_Focus is StormX:
                                        ch_s "Очень сомневаюсь."
                                elif Ch_Focus is JubesX:
                                        ch_v "Очень сомневаюсь."
                                elif Ch_Focus is GwenX:
                                        ch_g "Ты про то, что мы с ней покувыркаемся, или про то, что ты будешь наблюдаешь?"
                                        ch_g "Первое - возможно, второе - вряд ли."
                                elif Ch_Focus is BetsyX:
                                        ch_b "Я в этом сомневаюсь."
                                elif Ch_Focus is DoreenX:
                                        ch_d "Я так -не думаю-?"
                                elif Ch_Focus is WandaX:
                                        ch_w "Сомневаюсь. . ."
                        if Ch_Focus is RogueX:
                                ch_r "Но спасибо, что не настаиваешь."
                        elif Ch_Focus is KittyX:
                                if not Player.Male:
                                    ch_k "Спасибо, что отнеслась спокойно. . ."
                                else:
                                    ch_k "Спасибо, что отнесся спокойно. . ."
                        elif Ch_Focus is EmmaX:
                                ch_e "Я ценю твое самообладание."
                        elif Ch_Focus is StormX:
                                ch_s "Я сожалею об этом."
                        elif Ch_Focus is JubesX:
                                ch_v "Извини."
                        elif Ch_Focus is GwenX:
                                ch_g "Извини."
                        elif Ch_Focus is BetsyX:
                                ch_b "Мне жаль, что ничего не вышло."
                        elif Ch_Focus is DoreenX:
                                ch_d "Извини."
                        elif Ch_Focus is WandaX:
                                ch_w "Прости."
                        $ Ch_Focus.FaceChange("smile", 1)
                        $ Ch_Focus.Statup("Love", 80, 2)
                        $ Ch_Focus.Statup("Inbt", 70, 5)
                        call Taboo_Level
                        return
                        # end "Maybe later?"

                "Похоже, что тебе это нравится. . .":
                        if Approval:
                                $ Ch_Focus.FaceChange("sexy")
                                $ Ch_Focus.Statup("Obed", 90, 4)
                                $ Ch_Focus.Statup("Obed", 50, 5)
                                $ Ch_Focus.Statup("Inbt", 70, 4)
                                $ Ch_Focus.Statup("Inbt", 40, 4)
                                $ Line = renpy.random.choice(["Ну. . . возможно.",
                                        "Я не против пообщаться с ней. . .",
                                        "A",
                                        "Конечно.",
                                        "Пожалуй. . .",
                                        "Хех, возможно."])
                                if Line == "A":
                                        if Ch_Focus is RogueX:
                                                ch_r "Возможно, мне это все равно было нужно. . ."
                                        elif Ch_Focus is KittyX:
                                                ch_k "В любом случае мне это было нужно. . ."
                                        elif Ch_Focus is EmmaX:
                                                ch_e "Я не против близости с ней. . ."
                                        elif Ch_Focus is LauraX:
                                                ch_l "Мне вроде как нужно было выпустить пар. . ."
                                        elif Ch_Focus is JeanX:
                                                if not Player.Male:
                                                    ch_j "Ты еще не видела, что она вытворяет. . ."
                                                else:
                                                    ch_j "Ты еще не видел, что она вытворяет. . ."
                                        elif Ch_Focus is StormX:
                                                ch_s "Как и тебе."
                                        elif Ch_Focus is JubesX:
                                                ch_v "Нууу, возможно."
                                        elif Ch_Focus is GwenX:
                                                ch_g "Все может быть. . ."
                                        elif Ch_Focus is BetsyX:
                                                ch_b "Возможно."
                                        elif Ch_Focus is DoreenX:
                                                ch_d "Ох, эм. . . ага. . ."
                                        elif Ch_Focus is WandaX:
                                                ch_w "Ага, еще как. . ."
                                else:
                                        call AnyLine(Ch_Focus,Line)
                                call AnyLine(Ch_Focus,Line)
                                $ Line = 0
                                jump Les_Partner

                "Просто приступай.":
                        # Pressured into it
                        $ Approval = ApprovalCheck(Ch_Focus, 550, "OI", TabM = 2) # 55, 70, 85
                        if Approval > 1 or (Approval and Ch_Focus.Forced):
                                $ Ch_Focus.FaceChange("sad")
                                $ Ch_Focus.Statup("Love", 70, -5, 1)
                                $ Ch_Focus.Statup("Love", 200, -5)
                                if Ch_Focus is RogueX:
                                        ch_r "Хорошо. Я попробую."
                                elif Ch_Focus is KittyX:
                                        ch_k "Ладно, как скажешь."
                                elif Ch_Focus is EmmaX:
                                        ch_e "Ох, хорошо."
                                elif Ch_Focus is LauraX:
                                        ch_l "Хорошо, если ты настаиваешь."
                                elif Ch_Focus is JeanX:
                                        ch_j "Ох, хорошо. . ."
                                elif Ch_Focus is StormX:
                                        ch_s ". . ."
                                elif Ch_Focus is JubesX:
                                        ch_v "Хорошо."
                                elif Ch_Focus is GwenX:
                                        ch_g "Ладно, ладно, только придержи коней. . ."
                                elif Ch_Focus is BetsyX:
                                        ch_b "Ох, хорошо."
                                elif Ch_Focus is DoreenX:
                                        ch_d "Ох. . . ну ладно."
                                elif Ch_Focus is WandaX:
                                        ch_w "Конечно. . ."
                                $ Ch_Focus.Statup("Obed", 80, 4)
                                $ Ch_Focus.Statup("Inbt", 80, 1)
                                $ Ch_Focus.Statup("Inbt", 60, 3)
                                $ Ch_Focus.Forced = 1
                                jump Les_Partner
                        else:
                                $ Ch_Focus.Statup("Love", 200, -20)
                                $ Ch_Focus.RecentActions.append("angry")
                                $ Ch_Focus.DailyActions.append("angry")
        # end of asking her to do it

        call Les_Response(Partner,Ch_Focus,1,B2=Bonus)
        if _return:
                #if the other girl convinces her
                $ Ch_Focus.FaceChange("smile", 1)
                if Ch_Focus is RogueX:
                        ch_r "Ладно! Ты меня уговорила."
                        ch_r "Иди сюда. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Ладно, если -ты- хочешь."
                        ch_k "Иди сюда. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Ну, если ты настаиваешь, дорогая."
                        $ Ch_Focus.FaceChange("sly", 1)
                        ch_e "Иди сюда. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Ладно, если -тебе- это нравится."
                        ch_l "Иди сюда. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Ты, конечно же, будешь в восторге. . ."
                        ch_j "Иди ко мне."
                elif Ch_Focus is StormX:
                        ch_s "Как я могу отказать тебе, [Partner.Name]?"
                        ch_s "Хорошо, иди сюда. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Ладно, хорошо, если тебе такое нравится."
                        ch_v "Иди сюда."
                elif Ch_Focus is GwenX:
                        ch_g "Ну, если этого хочет [Partner.Name], как я могу отказаться?"
                        ch_g "Я в деле!"
                elif Ch_Focus is BetsyX:
                        ch_b "Пожалуй, если ты настаиваешь, [Partner.Name]. . ."
                        ch_b "Подойди ближе, ты получишь невероятное удовольствие."
                elif Ch_Focus is DoreenX:
                        ch_d "Ого, ну, если тебе это интересно. . ."
                        ch_d "Конечно!"
                elif Ch_Focus is WandaX:
                        ch_w "Ох, тебе, похоже, уже не терпится. . ."
                        ch_w "Конечно, иди сюда!"
                jump Les_Prep


        #She refused all offers.
        $ Ch_Focus.ArmPose = 1
        if not Partner:
                if Ch_Focus is RogueX:
                        ch_r "Для танго, нужны двое, так что. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Похоже, ей это не понравилось. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Что ж, в одиночку я точно не справлюсь. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Не знаю, должна ли я чувствовать себя оскорбленной. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Мы с ней -поговорим- позже. . ."
                elif Ch_Focus is StormX:
                        ch_s "Боюсь, это все меняет."
                elif Ch_Focus is JubesX:
                        ch_v "Нууу, не похоже, что это произойдет. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Ох, беда. У тебя что-то еще есть на уме?"
                elif Ch_Focus is BetsyX:
                        ch_b "Что ж, жаль. У тебя есть еще какие-нибудь идеи?"
                elif Ch_Focus is DoreenX:
                        ch_d "Ну, думаю, тут и так все понятно. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Прости. . ."
        elif Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("angry", 1)
                if Ch_Focus is RogueX:
                        ch_r "Послушай, это даже не обсуждается."
                elif Ch_Focus is KittyX:
                        ch_k "Мне это не нравится."
                elif Ch_Focus is EmmaX:
                        ch_e "Мне это не нравится."
                elif Ch_Focus is LauraX:
                        ch_l "Я на такое не подписывалась."
                elif Ch_Focus is JeanX:
                        ch_j "Звучит как-то несерьезно. . ."
                elif Ch_Focus is StormX:
                        ch_s "Я бы предпочла что-нибудь другое."
                elif Ch_Focus is JubesX:
                        ch_v "Я не увлекаюсь подобным."
                elif Ch_Focus is GwenX:
                        ch_g "Этого не произойдет."
                elif Ch_Focus is BetsyX:
                        ch_b "Боюсь, я не должна этого делать."
                elif Ch_Focus is DoreenX:
                        ch_d "Я не могу, ну никак."
                elif Ch_Focus is WandaX:
                        ch_w "Ага, прости. . ."
                $ Ch_Focus.Statup("Lust", 90, 5)
                if Ch_Focus.Love > 300:
                        $ Ch_Focus.Statup("Love", 70, -2)
                $ Ch_Focus.Statup("Obed", 50, -2)
                $ Ch_Focus.RecentActions.append("angry")
                $ Ch_Focus.DailyActions.append("angry")
        elif Ch_Focus.Taboo > 20:
                # she refuses and this is too public a place for her
                $ Ch_Focus.FaceChange("angry", 1)
                $ Ch_Focus.DailyActions.append("tabno")
                if Ch_Focus is RogueX:
                        ch_r "Уж точно не здесь."
                elif Ch_Focus is KittyX:
                        ch_k "Точно не здесь."
                elif Ch_Focus is EmmaX:
                        ch_e "Точно не здесь."
                elif Ch_Focus is LauraX:
                        ch_l "Не в таком людном месте."
                elif Ch_Focus is JeanX:
                        ch_j "Не думаю, что это подходящее место."
                elif Ch_Focus is StormX:
                        ch_s "Это место слишком людное."
                elif Ch_Focus is JubesX:
                        ch_v "Здесь слишком людно."
                elif Ch_Focus is GwenX:
                        if not Player.Male:
                            ch_g "Ты выбрала неудачное место для этого. . ."
                        else:
                            ch_g "Ты выбрал неудачное место для этого. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Это место совершенно не подходит."
                elif Ch_Focus is DoreenX:
                        ch_d "Я не могу заняться чем-то подобным здесь!"
                elif Ch_Focus is WandaX:
                        ch_w "Мы никак не можем заняться этим здесь. . ."
                $ Ch_Focus.Statup("Lust", 90, 5)
                $ Ch_Focus.Statup("Obed", 50, -3)
        elif Ch_Focus.Les:
                $ Ch_Focus.FaceChange("sad")
                if Ch_Focus is RogueX:
                        if Bonus >= 100:
                            ch_r "Просто я не думаю, что готова к такому."
                        else:
                            ch_r "Просто я не думаю, что мне нравятся такое."
                elif Ch_Focus is KittyX:
                        if Bonus >= 100:
                            ch_k "Мне это не очень нравится."
                        else:
                            ch_k "Не думаю, что я готова к зрителям."
                elif Ch_Focus is EmmaX:
                        if Bonus >= 100:
                            ch_e "Мне это не очень нравится."
                        else:
                            ch_e "Не думаю, что я готова к зрителям."
                elif Ch_Focus is LauraX:
                        if Bonus >= 100:
                            ch_l "Я не готова к этому."
                        else:
                            ch_l "Не со зрителями же."
                elif Ch_Focus is JeanX:
                        if Bonus >= 100:
                            ch_j "Меня это не устраивает."
                        else:
                            if not Player.Male:
                                ch_j "Я бы предпочла, чтобы ты не смотрела."
                            else:
                                ch_j "Я бы предпочла, чтобы ты не смотрел."
                elif Ch_Focus is StormX:
                        if Bonus >= 100:
                            ch_s "Это не совсем то, чем я хотела бы заняться."
                        else:
                            ch_s "Не думаю, что зрители были бы тут уместны."
                elif Ch_Focus is JubesX:
                        if Bonus >= 100:
                            ch_v "Я не увлекаюсь подобным."
                        else:
                            ch_v "Я бы предпочла без наблюдателей."
                elif Ch_Focus is GwenX:
                            ch_g "Я не уверена, мне не нравится, когда кто-то смотрит. . ."
                elif Ch_Focus is BetsyX:
                            ch_b "Я вынуждена отказаться."
                elif Ch_Focus is DoreenX:
                            ch_d "Я не уверена, меня смущают зрители. . ."
                elif Ch_Focus is WandaX:
                            ch_w "Я не думаю, что заниматься этим при зрителях - хорошая идея. . ."
        else:
                $ Ch_Focus.FaceChange("normal", 1)
                if Ch_Focus is RogueX:
                        ch_r "Хех, ни за что, я {i}не{/i} буду этого делать."
                elif Ch_Focus is KittyX:
                        ch_k "Ни за что."
                elif Ch_Focus is EmmaX:
                        ch_e "Ни за что."
                elif Ch_Focus is LauraX:
                        ch_l "Не-а."
                elif Ch_Focus is JeanX:
                        ch_j "Ни за что. . ."
                elif Ch_Focus is StormX:
                        ch_s "Боюсь, что нет."
                elif Ch_Focus is JubesX:
                        ch_v "Не-а."
                elif Ch_Focus is GwenX:
                        ch_g "Неее."
                elif Ch_Focus is BetsyX:
                        ch_b "Боюсь, что нет."
                elif Ch_Focus is DoreenX:
                        ch_d "Нет!"
                elif Ch_Focus is WandaX:
                        ch_w "Нет. . ."
        $ Ch_Focus.RecentActions.append("no lesbian")
        $ Ch_Focus.DailyActions.append("no lesbian")
        $ Tempmod = 0
        call Taboo_Level
        return


label Les_Partner:
        # This checks to see if the other girl is into it.
        # Girl and BO are passed from previous label
        $ Line = 0
        python:
            for BX in TotalGirls:
                if BX.Loc == bg_current and BX is not Ch_Focus:
                        #Picks the other girl in the area and spits her out
                        Line = BX
                        break
#        $ BO = TotalGirls[:]
#        $ BO.remove(Ch_Focus)
#        $ Line = 0
#        python:
#            for BX in BO:
#                if BX.Loc == bg_current:
#                        #Picks the other girl in the area and spits her out
#                        Line = BX
#                        break
        if Line:
                #when a girl's picked, check if she's into it
                call Les_Response(Line,Ch_Focus,2)
                if not _return:
                        # If she refused
                        return
        else:
                        return
        #if nobody refuses, it passes through to the next label

label Les_Prep:
        #sets the scene up
        $ Line = 0
        if Ch_Focus == Partner:
                    $ Partner = 0
                    $ Line = 1

#        call Shift_Focus(Girl)
        if Partner not in TotalGirls:
                $ Partner = 0
                python:
                    for BX in TotalGirls:
                        if BX.Loc == bg_current and BX is not Ch_Focus:
                                Partner = BX
                                break

#        if Line:
#                #if for some reason the Partner and lead were jumbled, swap them.
#                call Shift_Focus(Partner)

#        $ Line = 0

        $ Ch_Focus.AddWord(1,"noticed "+Partner.Tag,"noticed "+Partner.Tag) #ie $ Ch_Focus.RecentActions.append("noticed Partner")
        $ Partner.AddWord(1,"noticed "+Ch_Focus.Tag,"noticed "+Ch_Focus.Tag) #ie $ Partner.RecentActions.append("noticed Ch_Focus")

        if "unseen" not in Ch_Focus.RecentActions:
                #if she knows you're there. . .
                $ Ch_Focus.FaceChange("sexy")
                $ Ch_Focus.ArmPose = 2
                "[Ch_Focus.Name] подходит к [Partner.Name_dat] и обнимает ее за шею."
                if not Ch_Focus.LesWatch:
                        #First time
                        if Ch_Focus.Forced:
                            $ Ch_Focus.Statup("Love", 90, -20)
                            $ Ch_Focus.Statup("Obed", 70, 55)
                            $ Ch_Focus.Statup("Inbt", 80, 55)
                        else:
                            $ Ch_Focus.Statup("Love", 90, 5)
                            $ Ch_Focus.Statup("Obed", 70, 20)
                            $ Ch_Focus.Statup("Inbt", 80, 60)
                call Les_FirstKiss
#                $ Trigger3 == "kiss girl"
#                $ Trigger4 == "kiss girl"
                $ Ch_Focus.Offhand = "kiss girl"
                $ Partner.Offhand = "kiss girl"

        if not Player.Male and "girltalk" not in Ch_Focus.History:
                if not ApprovalCheck(Ch_Focus, 1100):
                        $ Ch_Focus.DrainWord("nogirls",0,0,0,1) #history
                        $ Ch_Focus.AddWord(1,0,0,0,"girltalk") #history
                else:
                        $ Ch_Focus.AddWord(1,0,0,0,"nogirls") #history
        if not Player.Male and "girltalk" not in Partner.History:
                if not ApprovalCheck(Partner, 1100):
                        $ Partner.DrainWord("nogirls",0,0,0,1) #history
                        $ Partner.AddWord(1,0,0,0,"girltalk") #history
                else:
                        $ Partner.AddWord(1,0,0,0,"nogirls") #history
        $ Trigger = "lesbian"
        if Situation:
            $ renpy.pop_call()
            $ Situation = 0
        $ Line = 0
        if Ch_Focus.Taboo:
            $ Ch_Focus.DrainWord("tabno")
        $ Ch_Focus.DrainWord("no lesbian")
        $ Ch_Focus.AddWord(0,"lesbian","lesbian") #adds "lesbian" to daily and recent
        $ Partner.AddWord(0,"lesbian","lesbian") #adds "lesbian" to daily and recent

label Les_Cycle:
        while Round > 0:
            call Les_Launch(Ch_Focus)
            $ Ch_Focus.LustFace()

            if  Player.Focus < 100:
                        #Player Command menu
                        menu:
                            "Продолжать смотреть. . .":
                                        pass

                            "\"Кхм-кхм. . .\"" if "unseen" in Ch_Focus.RecentActions:
                                        jump Les_Interupted

                            "Начать дрочить." if Trigger2 != "jackin" and Player.Male:
                                        call Jackin(Ch_Focus)
                            "Перестать дрочить." if Trigger2 == "jackin":
                                        $ Trigger2 = 0
                            "Начать мастурбировать." if Trigger2 != "jilling" and not Player.Male:
                                        call Jilling(Ch_Focus)
                            "Перестать мастурбировать." if Trigger2 == "jilling":
                                        $ Trigger2 = 0

                            "Концентрироваться на продолжительности [[Не открыто]. (locked)" if "focus" not in Player.Traits:
                                        pass
                            "Концентрироваться на продолжительности." if not Player.FocusX and "focus" in Player.Traits:
                                        "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                        $ Player.FocusX = 1
                            "Прекратить концентрироваться." if Player.FocusX:
                                        "Вы расслабляетесь. . ."
                                        $ Player.FocusX = 0

                            "Другие варианты":
                                    menu:
                                        "Дополнительное действие":
                                                if Ch_Focus.Action and MultiAction:
                                                        call Offhand_Set
                                                        if Trigger2:
                                                             $ Ch_Focus.Action -= 1
                                                else:
                                                        call Sex_Basic_Dialog(Ch_Focus,"tired")  # "I'm actually getting a little tired,"

                                        "Тройничек":
                                            menu:
                                                "Пусть [Ch_Focus.Name] с [Partner.Name_tvo] займутся чем-нибудь вместе":
                                                        if "unseen" in Ch_Focus.RecentActions:
                                                                ch_p "О да, почему бы тебе не. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                call Les_Change(Ch_Focus)
                                                "Пусть [Partner.Name] займется чем-нибудь другим":
                                                        if "unseen" in Ch_Focus.RecentActions:
                                                                ch_p "О да, почему бы тебе не. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                call Three_Change(Ch_Focus)

                                                "Не бросай свое текущее занятие. . . (locked)" if not ThreeCount or not Partner.Offhand:
                                                            $ ThreeCount = 0
                                                "Не бросай свое текущее занятие. . ." if ThreeCount and Partner.Offhand:
                                                        if "unseen" in Ch_Focus.RecentActions:
                                                                ch_p "Ох, это хорошо. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                $ ThreeCount = 0

                                                #"Swap to [Partner.Name]":
                                                            #call Trigger_Swap(Ch_Focus)
                                                "Раздеть [Partner.Name_vin]":
                                                        if "unseen" in Ch_Focus.RecentActions:
                                                                ch_p "О да, раздевайся. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                call Girl_Undress(Partner)
                                                                call Shift_Focus(Partner)
                                                                jump Les_Cycle
                                                "Привести в порядок [Partner.Name_vin]":
                                                        if "unseen" in Ch_Focus.RecentActions:
                                                                ch_p "На тебе что-то есть. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                call Girl_Cleanup(Partner,"ask")
                                                                #call Shift_Focus(Partner)
                                                                jump Les_Cycle
                                                "Неважно":
                                                                jump Les_Cycle
                                        "Раздеть [Ch_Focus.Name_vin]":
                                                        if "unseen" in Ch_Focus.RecentActions:
                                                                ch_p "О да, почему бы тебе не. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                call Girl_Undress(Ch_Focus)
                                        "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                                                pass
                                        "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                                if "unseen" in Ch_Focus.RecentActions:
                                                                ch_p "На тебе что-то есть. . ."
                                                                jump Les_Interupted
                                                else:
                                                                call Girl_Cleanup(Ch_Focus,"ask")
                                        "Неважно":
                                                                jump Les_Cycle

                            "Вернуться к Секс-меню" if MultiAction:
                                        ch_p "Давай попробуем что-нибудь другое."
                                        $ Situation = "shift"
                                        $ Line = 0
                                        jump Les_After
                            "Закончить" if not MultiAction:
                                        ch_p "Давай пока остановимся."
                                        $ Line = 0
                                        jump Les_After
            #End menu (if Line)

            call Sex_Dialog(Ch_Focus,Partner)

            $ Cnt += 1
            $ Round -= 1

            $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

            if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                        #If either of you can cum:
                        if Player.Focus >= 100:
                                #If you can cum:
                                if "unseen" not in Ch_Focus.RecentActions: #if she knows you're there
                                        call Player_Cumming(Ch_Focus)
                                        if "angry" in Ch_Focus.RecentActions:
                                                call Girl_Pos_Reset(Ch_Focus) #call expression Ch_Focus.Tag + "_Pos_Reset"
                                                call Girl_Pos_Reset(Partner) #call expression Partner.Tag + "_Pos_Reset"
                                                return
                                        $ Ch_Focus.Statup("Lust", 200, 5)
                                        if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                                $ Ch_Focus.DailyActions.append("unsatisfied")
                                        $ Line = "came"
                                else: #If she wasn't aware you were there
                                        "Вы с ворчанием пытаетесь сдержаться."
                                        $ Player.Focus = 95
                                        jump Les_Interupted

                        if Ch_Focus.Lust >= 100:
                                        #If the lead Girl can cum
                                        call Girl_Cumming(Ch_Focus)
                                        jump Les_Interupted

                        if Line == "came":
                                        $ Line = 0
                                        if not Player.Semen:
                                                "Вы опустошены, вам, вероятно, следует сделать перерыв."
            if Partner and Partner.Lust >= 100:
                    #Checks if partner could orgasm
                    call Girl_Cumming(Partner)

            #End orgasm

            $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

            if "unseen" in Ch_Focus.RecentActions:
                    if Round == 10:
                            "Уже довольно поздно, [Ch_Focus.Name] с [Partner.Name_tvo], вероятно, скоро закончат."
                    elif Round == 5:
                            "Они точно скоро остановятся."
            else:
                    if Round == 10:
                            call Sex_Basic_Dialog(Ch_Focus,10) #"You might want to wrap this up, it's getting late."
                    elif Round == 5:
                            call Sex_Basic_Dialog(Ch_Focus,5)   #"Seriously, it'll be time to stop soon."
        #Round = 0 loop breaks
        $ Ch_Focus.FaceChange("bemused", 0)
        $ Line = 0
        if "unseen" not in Ch_Focus.RecentActions:
                call Sex_Basic_Dialog(Ch_Focus,"done")   #"Ok, [Ch_Focus.Petname], that's enough of that for now."


label Les_After: #rkeljsvgbdw
        call Girl_Hide(Ch_Focus)
        call Girl_Pos_Reset(Ch_Focus) #call expression Ch_Focus.Tag + "_Pos_Reset"
        if not Partner:
                $ Tempmod = 0
                call Checkout
                return
        call Girl_Hide(Partner)
        call Girl_Pos_Reset(Partner) #call expression Partner.Tag + "_Pos_Reset"
        $ Ch_Focus.FaceChange("sexy")
        if Partner is EmmaX:
                call Partner_Like(Ch_Focus,4)
        else:
                call Partner_Like(Ch_Focus,3)

        $ Ch_Focus.LesWatch += 1
        $ Partner.LesWatch += 1
        if Ch_Focus.LesWatch == 1:
                $ Ch_Focus.SEXP += 15
                if Ch_Focus.Love >= 500 and Ch_Focus.OCount:
                        if Ch_Focus is RogueX:
                                ch_r "Должна сказать, мне очень понравилось. . ."
                        elif Ch_Focus is KittyX:
                                ch_k "Хм, довольно забавно со зрителями. . ."
                        elif Ch_Focus is EmmaX:
                                ch_e "Мне нравится при зрителях. . ."
                                $ Ch_Focus.FaceChange("sly",1)
                                ch_e "как-нибудь повторим?"
                        elif Ch_Focus is LauraX:
                                ch_l "Мне понравилось со зрителями. . ."
                        elif Ch_Focus is JeanX:
                                ch_j "Приятно иметь зрителей. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Мне понравилось, когда за мной наблюдают. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Было здорово иметь наблюдателей. . ."
                        elif Ch_Focus is GwenX:
                                ch_g "Фанаты того стоят, верно, [Partner.Name]?"
                        elif Ch_Focus is BetsyX:
                                ch_b "Должна отметить, это было гораздо интереснее, чем я ожидала."
                        elif Ch_Focus is DoreenX:
                                ch_d "Ох. . . это было очень приятно. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Это было просто замечательно. . ."
        if Partner.LesWatch == 1:
                $ Partner.SEXP += 15
                if Partner.Love >= 500 and Partner.OCount:
                        if Partner is RogueX:
                                ch_r "Должна сказать, мне очень понравилось. . ."
                        elif Partner is KittyX:
                                ch_k "Хм, довольно забавно со зрителями. . ."
                        elif Partner is EmmaX:
                                ch_e "Мне нравится при зрителях. . ."
                                $ Partner.FaceChange("sly",1)
                                ch_e "как-нибудь повторим?"
                        elif Partner is LauraX:
                                ch_l "Мне понравилось со зрителями. . ."
                        elif Partner is JeanX:
                                ch_j "Приятно иметь зрителей. . ."
                        elif Partner is StormX:
                                ch_s "Мне понравилось, когда за мной наблюдают. . ."
                        elif Partner is JubesX:
                                ch_v "Было здорово иметь наблюдателей. . ."
                        elif Partner is GwenX:
                                ch_g "Фанаты того стоят, верно, [Partner.Name]?"
                        elif Partner is BetsyX:
                                ch_b "Должна отметить, это было гораздо интереснее, чем я ожидала."
                        elif Partner is DoreenX:
                                ch_d "Ох. . . было очень жарко. . ."
                        elif Partner is WandaX:
                                ch_w "Это было просто замечательно. . ."
        if not Situation:
                call Post_Les_Dialog
        $ Ch_Focus.AddWord(1,0,0,0,"les "+Partner.Tag) #ie $ Ch_Focus.RecentActions.append("noticed Partner")
        $ Partner.AddWord(1,0,0,0,"les "+Ch_Focus.Tag) #ie $ Partner.RecentActions.append("noticed Ch_Focus")
        $ Tempmod = 0
        call Checkout
        return
    # End LesScene


label Post_Les_Dialog: #rkeljsvgbdw
        # called from Les_After if they have dialog for each other.
        if Ch_Focus is RogueX:
                ch_r "Это было приятно. . ."
        elif Ch_Focus is KittyX:
                ch_k "Это было весело. . ."
        elif Ch_Focus is EmmaX:
                ch_e "Это было приятно. . ."
        elif Ch_Focus is LauraX:
                ch_l "Это было весело. . ."
        elif Ch_Focus is JeanX:
                ch_j "Эй, а это было весело. . ."
        elif Ch_Focus is StormX:
                ch_s "Это было. . . очень приятно."
        elif Ch_Focus is JubesX:
                ch_v "Это было просто супер. . ."
        elif Ch_Focus is GwenX:
                ch_g "Это было У-Див-Ительно. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Это было просто чудесно. . ."
        elif Ch_Focus is DoreenX:
                ch_d " . . спасибо, [Partner.Name]"
        elif Ch_Focus is WandaX:
                ch_w "Это было клево!"

        if "les "+Partner.Tag in Ch_Focus.History:
                #if this wasn't the first time. . .
                if Partner is RogueX:
                        ch_r "Мммм, да. . ."
                elif Partner is KittyX:
                        ch_k "Мммм, да, все было хорошо. . ."
                elif Partner is EmmaX:
                        ch_e "Безусловно. . ."
                elif Partner is LauraX:
                        ch_l "Агась. . ."
                elif Partner is JeanX:
                        ch_j "Да, наверное, так оно и было. . ."
                elif Partner is StormX:
                        ch_s "Конечно. . ."
                elif Partner is JubesX:
                        ch_v "Точно. . ."
                elif Partner is GwenX:
                        ch_g "Это было так весело!"
                elif Partner is BetsyX:
                        ch_b "Это было действительно очень приятно. . ."
                elif Partner is DoreenX:
                        ch_d "Ага. . . это было очень приятно. . ."
                elif Partner is WandaX:
                        ch_w "Ага, это было клево. . ."
        else:
                # If this is the first time they've done this. . .
                # "les Kitty" not in RogueX.History. . .
                if Ch_Focus.GirlLikeCheck(Partner) >= 600:
                        #if the Lead girl likes the Partner. . .
                        if Ch_Focus is RogueX:
                                ch_r "Ты. . . прямо знаешь, что нужно делать. . ."
                        elif Ch_Focus is KittyX:
                                ch_k "Ты так хороша!"
                        elif Ch_Focus is EmmaX:
                                ch_e "Ты прекрасна, дорогая!"
                        elif Ch_Focus is LauraX:
                                ch_l "Мне понравился этот трюк ртом."
                        elif Ch_Focus is JeanX:
                                ch_j "А ты оказывается. . . опытная. . ."
                        elif Ch_Focus is StormX:
                                ch_s "У тебя определенно есть талант. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "У тебя очень здорово получается. . ."
                        elif Ch_Focus is GwenX:
                                ch_g "Ты невероятно опытна!"
                        elif Ch_Focus is BetsyX:
                                ch_b "Нам определенно -нужно- проводить больше времени вместе. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "Мы должны как-нибудь повторить."
                        elif Ch_Focus is WandaX:
                                ch_w "Ты хорошо знаешь свое дело. . ."
                else:
                        #if the Lead girl doesn't like the Partner. . .
                        if Ch_Focus is RogueX:
                                ch_r "Это. . . было не совсем ужасно. . ."
                        elif Ch_Focus is KittyX:
                                ch_k "Это был. . . интересный опыт. . ."
                        elif Ch_Focus is EmmaX:
                                ch_e "По крайней мере, ты не отставала от меня. . ."
                        elif Ch_Focus is LauraX:
                                ch_l "Сойдет. . ."
                        elif Ch_Focus is JeanX:
                                ch_j "Ладно, сойдет. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Это было. . . не так уж и плохо."
                        elif Ch_Focus is JubesX:
                                ch_v "Ты. . . старалась. . ."
                        elif Ch_Focus is GwenX:
                                ch_g "Ты удивительно хороша. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "У тебя определенно есть какой-никакой опыт. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "Ох. . . похоже, ты знала, что делаешь."
                        elif Ch_Focus is WandaX:
                                ch_w "Ты неплохо знаешь свое дело. . ."

                #second girl response. . .
                if Partner.GirlLikeCheck(Ch_Focus) >= 600:
                        #if the Partner girl likes the Lead. . .
                        if Partner is RogueX:
                                ch_r "Эм, ага, ты тоже. . ."
                        elif Partner is KittyX:
                                ch_k "Ага, все было очень круто. . ."
                        elif Partner is EmmaX:
                                ch_e "Все дело в практике, дорогая. . ."
                        elif Partner is LauraX:
                                ch_l "Я -читала- твое тело."
                        elif Partner is JeanX:
                                ch_j "Ну, я -могу- читать мысли. . ."
                        elif Partner is StormX:
                                ch_s "Да, и ты тоже."
                        elif Partner is JubesX:
                                ch_v "Ага, ты был великолепна. . ."
                        elif Partner is GwenX:
                                ch_g "Ты была великолепна!"
                        elif Partner is BetsyX:
                                ch_b "Твоя техника была безупречна. . ."
                        elif Partner is DoreenX:
                                ch_d "Ты очень хороша!"
                        elif Partner is WandaX:
                                ch_w "Ты хорошо знаешь свое дело. . ."
                else:
                        #if the Partner girl doesn't like the Lead. . .
                        if Partner is RogueX:
                                ch_r "Похоже на то. . ."
                        elif Partner is KittyX:
                                ch_k "Наверное. . ."
                        elif Partner is EmmaX:
                                ch_e "Тебе определенно не помешало бы больше практики. . ."
                        elif Partner is LauraX:
                                ch_l "Угу."
                        elif Partner is JeanX:
                                ch_j "Конечно, как скажешь. . ."
                        elif Partner is StormX:
                                ch_s "Да. . ."
                        elif Partner is JubesX:
                                ch_v "Думаю, ты старалась. . ."
                        elif Partner is GwenX:
                                ch_g "Ага, ты тоже была довольно хороша. . ."
                        elif Partner is BetsyX:
                                ch_b "Твоя техника была безупречна. . . но тебе немного не хватает практики."
                        elif Partner is DoreenX:
                                ch_d "Это было не так уж и ужасно. . ."
                        elif Partner is WandaX:
                                ch_w "Ты неплохо знаешь свое дело. . ."
        return


#Start Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >
label Les_Response(Speaker=0,Subject=0, Step=1, B=0, B2=0, Tempmod=0, Result=0, Approval = 0): #rkeljsvgbdw
        #Dialog for responses to Lesbian scenes, Subject is the lead, Speaker is typically Partner to the lead girl. Step is the phase of the conversation
        # B is the bonus of how much Speaker is into this, B2 is a bonus for how much Subject is into it
        # call Les_Response(RogueX,1)
        # call Les_Response(KittyX,RogueX,1)
        if Speaker not in TotalGirls:
                $ Speaker = Partner
        if Subject not in TotalGirls:
                $ Subject = Ch_Focus
        if Speaker is EmmaX:
                #if Emma's not open to public sex yet, bailout
                if "three" not in EmmaX.History or "classcaught" not in EmmaX.History or (Taboo > 20 and "taboo" not in EmmaX.History):
                    $ EmmaX.RecentActions.append("no lesbian")
                    $ EmmaX.DailyActions.append("no lesbian")
                    $ EmmaX.Statup("Obed", 70, 5)
                    $ EmmaX.Statup("Inbt", 80, 5)
                    $ EmmaX.Statup("Lust", 50, 10)
                    $ Speaker.FaceChange("sadside", 1)
                    "[EmmaX.Name] украдкой оглядывается по сторонам."
                    if Subject is StormX:
                            ch_e "Для ясности, Ороро, я -не- вступаю в сексуальные отношения с такими студентами, как [Player.Name]."
                            ch_e "Полагаю, мне следует извиниться."
                            $ Subject.FaceChange("bemused", 1)
                            ch_s "О, да, мисс Фрост. Это лишь недопонимание."
                    else:
                            ch_e "Даже не представляю, почему ты думаешь, что я буду заниматься чем-то подобным со студенткой!"
                    call Remove_Girl(EmmaX)
                    "Она быстро выходит из комнаты."
                    return 0

        if not Speaker.Action:
                #this is often called by the sex menu, and reverts if she's worn out.
                if Speaker is RogueX:
                        ch_r "Прости, я просто устала"
                elif Speaker is KittyX:
                        ch_k "Я слишком устала для этого. . ."
                elif Speaker is EmmaX:
                        ch_e "Я устала, давай не сейчас. . ."
                elif Speaker is LauraX:
                        ch_l "У меня есть другие дела. . ."
                elif Speaker is JeanX:
                        ch_j "Я устала. . ."
                elif Speaker is StormX:
                        ch_s "Я сейчас не могу, прости."
                elif Speaker is JubesX:
                        ch_v "Прости, я просто устала. . ."
                elif Speaker is GwenX:
                        ch_g "Я. . . очень устала. . ."
                elif Speaker is BetsyX:
                        ch_b "Сейчас у меня нет сил. . ."
                elif Speaker is DoreenX:
                        ch_d "Извини, но я очень устала. . ."
                elif Speaker is WandaX:
                        ch_w "Прости, сейчас я совершенно обессилена. . ."
                return 0

        if Speaker.Les:
                $ Tempmod += 10
        if Speaker.SEXP >= 50:
                $ Tempmod += 25
        elif Speaker.SEXP >= 30:
                $ Tempmod += 15
        elif Speaker.SEXP >= 15:
                $ Tempmod += 5

        elif Speaker.Inbt >= 750:
                $ Tempmod += 5

        if "exhibitionist" in Speaker.Traits:
                $ Tempmod += (3*Taboo)

        if Speaker in Player.Harem or "sex friend" in Speaker.Petnames:
                $ Tempmod += 10
        elif "ex" in Speaker.Traits:
                $ Tempmod -= 40

        # Provides a bonus based on how much the speaker likes the subject girl
        if Speaker.GirlLikeCheck(Subject) >= 900:
                $ B += 150
        elif Speaker.GirlLikeCheck(Subject) >= 800 or "poly " + Subject.Tag in Speaker.Traits:
                $ B += 100
        elif Speaker.GirlLikeCheck(Subject) >= 700:
                $ B += 50
        elif Speaker.GirlLikeCheck(Subject) <= 200:
                $ B -= 200
        elif Speaker.GirlLikeCheck(Subject) <= 500:
                $ B -= 100

        if Speaker is JeanX:
                $ B += 100

        $ Approval = ApprovalCheck(Speaker, 1300, TabM = 2, Bonus = B) # 1300, 1450, 1600, Taboo -800

        if not Approval:
                #if there's no chance, skip to the end
                pass
        elif Step == 1:
                #this is if the first girl's check failed, but the speaking girl likes her.
                if Approval >= 2 or B >= 150:
                        $ Speaker.FaceChange("sexy", 1)
                        if Speaker is RogueX:
                                ch_r "Ты уверена, [Subject.Tag]? Это может быть очень весело?"
                        elif Speaker is KittyX:
                                ch_k "Давай, [Subject.Tag], это может быть весело."
                        elif Speaker is EmmaX:
                                ch_e "Ох, соглашайся, [Subject.Tag], Я могу тебя кое-чему научить."
                        elif Speaker is LauraX:
                                ch_l "Это и правда не так уж плохо, попробуй."
                        elif Speaker is JeanX:
                                ch_j "Давай. . . [Subject.Tag], это может быть весело."
                                $ B2 += 50
                        elif Speaker is StormX:
                                ch_s "[Subject.Tag], это было бы не так уж плохо, ты так не думаешь?"
                        elif Speaker is JubesX:
                                ch_v "Решай, ты в деле, [Subject.Tag]? . ."
                        elif Speaker is GwenX:
                                ch_g "Ну, разве ты не думаешь, что это может быть очень весело?"
                        elif Speaker is BetsyX:
                                ch_b "Ты уверена? Это может быть очень весело. . ."
                        elif Speaker is DoreenX:
                                ch_d "Ты уверена? . . . это может быть весело. . ."
                        elif Speaker is WandaX:
                                ch_w "Серьезно? Я сделаю так, что ты не пожалеешь. . ."
                        if B2 >= 100:
                                $ Result = 1
                                $ Speaker.GirlLikeUp(Subject,(int(B/10)))
                                $ Subject.GirlLikeUp(Speaker,(int(B2/10))) #B2 sent by the call. . .
                else:
                        return Result

        elif Step == 2:
            #this is the second step, usually in the Prep phase
            if Approval >= 2:
                    $ Speaker.FaceChange("smile", 1)
                    if Speaker is RogueX:
                            ch_r "Конечно!"
                    elif Speaker is KittyX:
                            ch_k "Конечно!"
                    elif Speaker is EmmaX:
                            ch_e "Конечно, [Speaker.Petname]."
                    elif Speaker is LauraX:
                            ch_l "Я в деле."
                    elif Speaker is JeanX:
                            ch_j "Конечно, почему бы и нет."
                    elif Speaker is StormX:
                            ch_s "Звучит весело."
                    elif Speaker is JubesX:
                            ch_v "Конечно, звучит весело."
                    elif Speaker is GwenX:
                            ch_g "Да!"
                    elif Speaker is BetsyX:
                            ch_b "Конечно!"
                    elif Speaker is DoreenX:
                            ch_d "Вперед!"
                    elif Speaker is WandaX:
                            ch_w "Конечно!"
                    $ Result = 1
                    return Result
            #if Approval, but not 2
            $ Speaker.FaceChange("sly", 2)
            if Speaker is RogueX:
                    if B >= 100:
                            ch_r "Не знаю, может и так. . ."
                    if B <= 0:
                            ch_r "Хотя я не уверена насчет нее. . ."
            elif Speaker is KittyX:
                    if B >= 100:
                            ch_k "Да, наверное. . ."
                    if B <= 0:
                            ch_k "Без обид, [Subject.Tag], но. . ."
            elif Speaker is EmmaX:
                    if B >= 100:
                            ch_e "Мммм, конечно. . ."
                    if B <= 0:
                            ch_e "[Subject.Tag], дорогая, честно говоря, я так не думаю. . ."
            elif Speaker is LauraX:
                    if B >= 100:
                            ch_l "Ты милая и все такое. . ."
                    if B <= 0:
                            ch_l "Я не знаю, [Subject.Tag]. . ."
            elif Speaker is JeanX:
                    if B >= 100:
                            ch_j "Она не так уж плоха. . ."
                    if B <= 0:
                            ch_j "С ней? . ."
            elif Speaker is StormX:
                    if B >= 100:
                            ch_s "О, да. . ."
                    if B <= 0:
                            ch_s "Я не уверена. . ."
            elif Speaker is JubesX:
                    if B >= 100:
                            ch_v "Конечно. . ."
                    if B <= 0:
                            ch_v "Я не уверена. . ."
            elif Speaker is GwenX:
                    if B >= 100:
                            ch_g "О, да!"
                    if B <= 0:
                            ch_g "Хмм. . . ну, я не уверена. . ."
            elif Speaker is BetsyX:
                    if B >= 100:
                            ch_b "Конечно!"
                    if B <= 0:
                            ch_b "Хмм. . . мы не очень-то с ней и ладим. . ."
            elif Speaker is DoreenX:
                    if B >= 100:
                            ch_d "Ох, ого, это может быть весело. . ."
                    if B <= 0:
                            ch_d "Мы с ней точно не лучшие подруги. . ."
            elif Speaker is WandaX:
                    if B >= 100:
                            ch_w "Это может быть очень весело. . ."
                    if B <= 0:
                            ch_w "Я не уверена, мы с ней не очень хорошо ладим. . ."
            $ Speaker.Blush = 1
            menu:
                extend ""
                "Ладно, все в порядке. . .":
                        if B >= 100:
                                if Speaker is RogueX:
                                        ch_r "Забудь, я в деле."
                                elif Speaker is KittyX:
                                        ch_k "Нет, нет, давай сделаем это."
                                elif Speaker is EmmaX:
                                        ch_e "Ох, не давай заднюю. . ."
                                elif Speaker is LauraX:
                                        ch_l "О, нет, я в деле."
                                elif Speaker is JeanX:
                                        ch_j "Ох, не пойми меня неправильно, я в деле."
                                elif Speaker is StormX:
                                        ch_s "Нет, нет, я заинтересована. . ."
                                elif Speaker is JubesX:
                                        ch_v "О, подождите, я в деле!"
                                elif Speaker is GwenX:
                                        ch_g "Ох, ну, один раз живем!"
                                elif Speaker is BetsyX:
                                        ch_b "Ну хорошо, я заинтересована!"
                                elif Speaker is DoreenX:
                                        ch_d "Подожди, я в деле!"
                                elif Speaker is WandaX:
                                        ch_w "О, нет, я -согласна-!"
                                $ Result = 1
                        else:
                                $ Speaker.FaceChange("smile")
                                if Speaker is RogueX:
                                        ch_r "Спасибо, я очень ценю это."
                                elif Speaker is KittyX:
                                        ch_k "Спасибо, я очень ценю это."
                                elif Speaker is EmmaX:
                                        ch_e "Я ценю твое самообладание."
                                elif Speaker is LauraX:
                                        ch_l "Ага. . ."
                                elif Speaker is JeanX:
                                        ch_j "Ага. . ."
                                elif Speaker is StormX:
                                        ch_s "Я ценю твой жест, благодарю."
                                elif Speaker is JubesX:
                                        ch_v "Ага, спасибо."
                                elif Speaker is GwenX:
                                        ch_g "Ага. . ."
                                elif Speaker is BetsyX:
                                        ch_b "Я очень это ценю."
                                elif Speaker is DoreenX:
                                        ch_d "Спасибо. . ."
                                elif Speaker is WandaX:
                                        ch_w "Спасибо. . ."
                "Давай, тебе должно понравиться. . .":
                        if B >= 50:
                                if Speaker is RogueX:
                                        ch_r "Ну, пожалуй, можно."
                                elif Speaker is KittyX:
                                        ch_k "Может быть?"
                                elif Speaker is EmmaX:
                                        ch_e "Уверена, так и будет. . ."
                                elif Speaker is LauraX:
                                        ch_l "Может быть. . . "
                                elif Speaker is JeanX:
                                        ch_j "Ага, может быть. . ."
                                elif Speaker is StormX:
                                        if not Player.Male:
                                            ch_s "Пожалуй, может ты и права. . ."
                                        else:
                                            ch_s "Пожалуй, может ты и прав. . ."
                                elif Speaker is JubesX:
                                        ch_v "Все может быть. . ."
                                elif Speaker is GwenX:
                                        ch_g "Я не подумала об этом. . ."
                                elif Speaker is BetsyX:
                                        ch_b "Возможно. . ."
                                elif Speaker is DoreenX:
                                        ch_d "Веееерно. . ."
                                elif Speaker is WandaX:
                                        ch_w "Может быть. . ."
                                $ Result = 1
                        else:
                                $ Speaker.FaceChange("sad", 2)
                                if Speaker is RogueX:
                                        ch_r "Я так не думаю."
                                elif Speaker is KittyX:
                                        ch_k "Скорее всего нет."
                                elif Speaker is EmmaX:
                                        ch_e "Скорее всего нет."
                                elif Speaker is LauraX:
                                        ch_l "Я в этом сомневаюсь."
                                elif Speaker is JeanX:
                                        ch_j "Сомневаюсь."
                                elif Speaker is StormX:
                                        ch_s "Точно не в данный момент."
                                elif Speaker is JubesX:
                                        ch_v "Не знаю, я так не думаю. . ."
                                elif Speaker is GwenX:
                                        ch_g "Есть много вещей, которые мне -может быть- понравятся. . ."
                                elif Speaker is BetsyX:
                                        ch_b "Мне так не кажется. . ."
                                elif Speaker is DoreenX:
                                        ch_d "Я в этом сомневаюсь. . ."
                                elif Speaker is WandaX:
                                        ch_w "Это вряд ли. . ."
                "Приступай, немедленно.":
                        if ApprovalCheck(Speaker, 550, "OI", TabM = 2):
                                $ Speaker.FaceChange("sadside", 1)
                                if Speaker is RogueX:
                                        ch_r "Ладно, как скажешь."
                                elif Speaker is KittyX:
                                        ch_k "Лаааадно."
                                elif Speaker is EmmaX:
                                        ch_e "Ох, хорошо."
                                elif Speaker is LauraX:
                                        ch_l "Хорошо."
                                elif Speaker is JeanX:
                                        ch_j "Ох, как скажешь."
                                elif Speaker is StormX:
                                        ch_s "Хорошо."
                                elif Speaker is JubesX:
                                        ch_v "Ох, как скажешь."
                                elif Speaker is GwenX:
                                        ch_g "Хорошо."
                                elif Speaker is BetsyX:
                                        ch_b "Если это так необходимо. . ."
                                elif Speaker is DoreenX:
                                        ch_d "Ох, ладно. . ."
                                elif Speaker is WandaX:
                                        ch_w "Конечно. . ."
                                $ Result = 1
                        else:
                                $ Speaker.FaceChange("angry")
                                if Speaker is RogueX:
                                        ch_r "С кем, по-твоему, ты разговариваешь?"
                                elif Speaker is KittyX:
                                        if not Player.Male:
                                            ch_k "Ты мне не хозяйка!"
                                        else:
                                            ch_k "Ты мне не хозяин!"
                                elif Speaker is EmmaX:
                                        ch_e "Не забывай, кто здесь главный, [Speaker.Petname]."
                                elif Speaker is LauraX:
                                        ch_l "Не дави на меня."
                                elif Speaker is JeanX:
                                        ch_j "Не указывай мне, во что ввязываться."
                                elif Speaker is StormX:
                                        ch_s "Так не просят об одолжении."
                                elif Speaker is JubesX:
                                        ch_v "Ни за что!"
                                elif Speaker is GwenX:
                                        ch_g "Неее-а!"
                                elif Speaker is BetsyX:
                                        ch_b "Конечно же я не соглашусь!"
                                elif Speaker is DoreenX:
                                        ch_d "Ни за что!"
                                elif Speaker is WandaX:
                                        ch_w "Хех, нет. . ."
                                $ Speaker.AddWord(1,"angry","angry") # adds to daily and recent
                "[Subject.Name], что ты думаешь?":
                        $ Subject.FaceChange("sexy", 1)
                        $ Speaker.GirlLikeUp(Subject,(int(B/10)))
                        if B >= 50:
                                $ Subject.GirlLikeUp(Speaker,5)
                        if Subject is RogueX:
                                if Speaker is KittyX:
                                    if Subject.Les and Speaker.Les:
                                            ch_r "Знаешь, мы можем хорошо провести время."
                                    else:
                                            ch_r "Это может быть очень весело."
                                elif Speaker is EmmaX:
                                    if Subject.Les and Speaker.Les:
                                            ch_r "Ты могла бы сделать то же самое, что и в прошлый раз. . ."
                                    else:
                                            ch_r "Я надеялась, что ты сможешь преподать мне пару уроков после занятий. . ."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_r "Ох, все пройдет не так уж плохо."
                                    else:
                                            ch_r "Это может быть очень весело."
                        elif Subject is KittyX:
                                if Speaker is RogueX:
                                    if Subject.Les and Speaker.Les:
                                            ch_k "Давай, [Speaker.Tag], ты же знаешь что мы повеселимся."
                                    else:
                                            ch_k "Давай, [Speaker.Tag], это будет весело."
                                elif Speaker in (EmmaX,StormX):
                                    if Subject.Les and Speaker.Les:
                                            ch_k "Думаю, будет неплохо показать [Subject.Petname_dat], чему ты меня научила. . ."
                                    else:
                                            ch_k "Я заметила, как ты смотрела на меня во время занятий. . ."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_k "Но нам так весело вместе."
                                    else:
                                            ch_k "Это может быть весело!"
                        elif Subject is EmmaX:
                                if Speaker is StormX:
                                    ch_e "Я уверена, мы бы многому могли научить [EmmaX.Petname_vin]. . ."
                                elif Subject.Les and Speaker.Les:
                                    ch_e "В чем дело [Speaker.Name]? Стесняешься перед [Player.Name_tvo]?"
                                else:
                                    ch_e "В чем дело, [Speaker.Name], Я видела, как ты смотришь на меня. . ."
                        elif Subject is LauraX:
                                if Speaker is EmmaX:
                                    if Subject.Les and Speaker.Les:
                                            ch_l "Ты не такая стеснительная, когда [Subject.Petname_rod] нет поблизости."
                                    else:
                                            ch_l "Давай, ты выглядишь такой грустной."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_l "Что, не хочешь трахаться, когда [Player.Name] рядом?"
                                    else:
                                            ch_l "Давай, я вижу, ты тоже этого хочешь."
                        elif Subject is JeanX:
                                if Speaker is EmmaX:
                                    ch_j "Да ладно тебе, мы обе знаем, что тебе нравится это."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_j "Что, теперь ты вдруг начала стесняться?"
                                    else:
                                            ch_j "Да ладно, хватит -сиськи мять-."
                        elif Subject is StormX:
                                if Speaker is KittyX:
                                    if Subject.Les and Speaker.Les:
                                            ch_s "Итак, [Speaker.Tag], это, конечно же, не будет твоим первым уроком. . ."
                                    else:
                                            ch_s "Итак, [Speaker.Tag], неужели ты не проявляешь ко мне. . . никакого интереса?"
                                elif Speaker is EmmaX:
                                    if Subject.Les and Speaker.Les:
                                            ch_s "Итак, [Subject.Petname], до этого ты говорила иначе. . ."
                                    else:
                                            ch_s "Что? Ты хочешь упустить возможность чему-нибудь научить [StormX.Petname_vin]. . ?"
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_s "Тебе не понравилось наше совместное времяпрепровождение?"
                                    else:
                                            ch_s "Обещаю, тебе понравится. . ."
                        elif Subject is JubesX:
                                    if Subject.Les and Speaker.Les:
                                            ch_v "Нууу, не скажу, что это наш -первый раз- или типа того. . ."
                                    else:
                                            ch_v "Думаю, я смогу перенести свой вес сюда. . ."
                        elif Subject is GwenX:
                                    if Subject.Les and Speaker.Les:
                                            if not Player.Male:
                                                ch_g "Разве ты не хочешь показать ей, что мы. . ."
                                            else:
                                                ch_g "Разве ты не хочешь показать ему, что мы. . ."
                                            ch_g "Ну, ты поняла. . ."
                                    elif Speaker is RogueX:
                                            ch_g "Знаешь, тебе не помешает -помощь-. . ."
                                    elif Speaker in (KittyX,StormX):
                                            ch_g "Знаешь, ты отлично управляешься с дамами. . ."
                                    elif Speaker is EmmaX:
                                            ch_g "Знаешь, ты могла бы научить меня паре вещей. . ."
                                    elif Speaker in (LauraX,JubesX):
                                            ch_g "Знаешь, в постели ты такая распутная. . ."
                                    elif Speaker is JeanX:
                                            ch_g "Знаешь, ты можешь поразить меня своей техникой. . ."
                                    else:
                                            ch_g "Обещаю, тебе понравится. . ."
                                    $ B += 50
                        elif Subject is BetsyX:
                                    if Subject.Les and Speaker.Les:
                                            ch_b "Разве ты не хочешь еще раз попробовать тот. . ?"
                                            ch_b "Ну, ты поняла. . ."
                                    else:
                                            ch_b "У меня довольно много талантов. . ."
                        elif Subject is DoreenX:
                                    if Subject.Les and Speaker.Les:
                                            ch_d "Думаю, мы могли бы попробовать то самое. . ."
                                            ch_d "Ну, ты поняла. . ."
                                    else:
                                            ch_d "Думаю, нам стоит попробовать. . ."
                        elif Subject is WandaX:
                                    if Subject.Les and Speaker.Les:
                                            ch_w "Знаешь, я могу кое-что сделать. . ."
                                            ch_w "Своим языком. . ."
                                    else:
                                            ch_w "Я могу показать несколько трюков. . ."
                        #end dialogs from if you asked the other girl what she thought. . .
                        #then the speaker responds. . .
                        if B >= 50:
                                #Yes
                                $ Speaker.FaceChange("smile", 1)
                                if Speaker is RogueX:
                                        ch_r "А знаешь, я не могу с этим поспорить, [Subject.Tag]."
                                elif Speaker is KittyX:
                                        ch_k "Хихи, наверное, так, [Subject.Tag]."
                                elif Speaker is EmmaX:
                                        ch_e "Если мы должны, [Subject.Tag]."
                                elif Speaker is LauraX:
                                        ch_l "Наверное, так."
                                elif Speaker is JeanX:
                                        ch_j "Справедливое замечание. . ."
                                elif Speaker is StormX:
                                        ch_s "Что ж, ты привела убедительные доводы. . ."
                                elif Speaker is JubesX:
                                        ch_v "Нууу, это правда. . ."
                                elif Speaker is GwenX:
                                        ch_g "Ну, если тебе этого хочется, [Subject.Tag]."
                                elif Speaker is BetsyX:
                                        ch_b "Если ты настаиваешь, [Subject.Tag]. . ."
                                elif Speaker is DoreenX:
                                        ch_d "Ну, если тебе так этого хочется, [Subject.Tag]."
                                elif Speaker is WandaX:
                                        ch_w "Что ж, раз тебе так хочется, [Subject.Tag]. . ."
                                $ Result = 1
                        else:
                                #No
                                $ Speaker.FaceChange("angry", 1, Eyes="side")
                                if Speaker is RogueX:
                                        ch_r "Извини, [Subject.Tag], ничего личного."
                                elif Speaker is KittyX:
                                        ch_k "Извини, [Subject.Tag], дело не в моем личном отношении к тебе."
                                elif Speaker is EmmaX:
                                        ch_e "Я извиняюсь, [Subject.Tag], дело не в тебе."
                                elif Speaker is LauraX:
                                        ch_l "Извини, [Subject.Tag], дело не в тебе."
                                elif Speaker is JeanX:
                                        ch_j "Ага, мне это совсем не интересно."
                                elif Speaker is StormX:
                                        ch_s "Боюсь, что мне ппридется отказаться, [Subject.Tag]."
                                elif Speaker is JubesX:
                                        ch_v "Ни за что, ничего личного, [Subject.Tag]."
                                elif Speaker is GwenX:
                                        ch_g "Извини, дело не в тебе, [Subject.Tag]."
                                elif Speaker is BetsyX:
                                        ch_b "Прошу прощения, [Subject.Tag]. Ничего личного. . ."
                                elif Speaker is DoreenX:
                                        ch_d "Я не могу, извини, [Subject.Tag]."
                                elif Speaker is WandaX:
                                        ch_w "Прости, [Subject.Tag]. . ."
                #end dialogs from if you asked the other girl what she thought. . .
        if Step == 3:
                #This is a check if you interrupted them and Primary wants to do it, does Secondary?
                if Approval:
                        $ Speaker.FaceChange("smile", 1)
                        if Speaker is RogueX:
                                ch_r "Пожалуй, я согласна. . ."
                        elif Speaker is KittyX:
                                ch_k "Наверное, я согласна. . ."
                        elif Speaker is EmmaX:
                                ch_e "Как я могу теперь отступить?"
                        elif Speaker is LauraX:
                                ch_l "Ага. . ."
                        elif Speaker is JeanX:
                                ch_j "Ну, думаю да."
                        elif Speaker is StormX:
                                ch_s "Пожалуй, мы могли бы продолжить. . ."
                        elif Speaker is JubesX:
                                ch_v "Нууу, пожалуй, если тебе такое нравится. . ."
                        elif Speaker is GwenX:
                                ch_g "Конечно!"
                        elif Speaker is BetsyX:
                                ch_b "Конечно."
                        elif Speaker is DoreenX:
                                ch_d "Ладно!"
                        elif Speaker is WandaX:
                                ch_w "Конечно!"
                        $ Result = 1
                else:
                        $ Speaker.FaceChange("sadside", 1)
                        if Speaker is RogueX:
                                ch_r "Мне сейчас совсем не до этого. . ."
                        elif Speaker is KittyX:
                                ch_k "Я не в восторге от этого. . ."
                        elif Speaker is EmmaX:
                                ch_e "Боюсь, что нет. . ."
                        elif Speaker is LauraX:
                                ch_l "Не сейчас. . ."
                        elif Speaker is JeanX:
                                ch_j "Мне неинтересно."
                        elif Speaker is StormX:
                                ch_s "Я, пожалуй, откажусь."
                        elif Speaker is JubesX:
                                ch_v "Нее, мне не нравится подобное."
                        elif Speaker is GwenX:
                                ch_g "Я так не думаю. . ."
                        elif Speaker is BetsyX:
                                ch_b "Боюсь, что нет. . ."
                        elif Speaker is DoreenX:
                                ch_d "Я, эм. . . не могу. Извини."
                        elif Speaker is WandaX:
                                ch_w "Не думаю, что я смогу. . ."
        if not Result:
                #response if all falls through and it fails. . .
                $ Speaker.RecentActions.append("no lesbian")
                $ Speaker.DailyActions.append("no lesbian")
                $ Speaker.FaceChange("sadside", 1)
                $ Partner = 0
                if Speaker is RogueX:
                        if B <= 0:
                                ch_r "Извини, [Speaker.Petname], просто с ней что-то не так."
                        if Speaker.Taboo > 20:
                                ch_r "Извини, [Speaker.Petname], это не самое подходящее место для этого."
                        if B >= 100:
                                ch_r "Извини, [Speaker.Petname], может быть, если бы тебя не было рядом. . ."
                        else:
                                ch_r "Извини, [Speaker.Petname], Мне просто неинтересно."
                elif Speaker is KittyX:
                        if B <= 0:
                                ch_k "Извини, [Speaker.Petname], Просто она мне не нравится."
                        if Speaker.Taboo > 20:
                                ch_k "Извини, [Speaker.Petname], это не совсем подходящее место для подобного."
                        if B >= 100:
                                ch_k "Извини, [Speaker.Petname], только не когда ты смотришь. . ."
                        else:
                                ch_k "Извини, [Speaker.Petname], Просто мне это не нравится."
                elif Speaker is EmmaX:
                        if B <= 0:
                                ch_e "Мне жаль, [Speaker.Petname], она просто не в моем вкусе."
                        if Speaker.Taboo > 20:
                                ch_e "Мне жаль, [Speaker.Petname], это может вызвать скандал."
                        if B >= 100:
                                ch_e "Мне жаль, [Speaker.Petname], только не со зрителями. . ."
                        else:
                                ch_e "Мне жаль, [Speaker.Petname], Меня это совсем не интересует."
                elif Speaker is LauraX:
                        if B <= 0:
                                ch_l "Извини, [Speaker.Petname], она не в моем вкусе."
                        if Speaker.Taboo > 20:
                                ch_l "Извини, [Speaker.Petname], это место немного людное."
                        if B >= 100:
                                ch_l "Извини, [Speaker.Petname], Мне не нужны зрители. . ."
                        else:
                                ch_l "Извини, [Speaker.Petname], Просто мне такое не нравится."
                elif Speaker is JeanX:
                        if B <= 0:
                                ch_j "Извини, [Speaker.Petname], я все могу сделать лучше, чем она."
                        if Speaker.Taboo > 20:
                                ch_j "Извини, [Speaker.Petname]. . . не на людях."
                        if B >= 100:
                                if not Player.Male:
                                    ch_j "Извини, [Speaker.Petname], ты этого не заслужила. . ."
                                else:
                                    ch_j "Извини, [Speaker.Petname], ты этого не заслужил. . ."
                        else:
                                ch_j "Извини, [Speaker.Petname], не сейчас."
                elif Speaker is StormX:
                        if B <= 0:
                                ch_s "Я извиняюсь, [Speaker.Petname], я не могу заняться подобным с ней."
                        if Speaker.Taboo > 20:
                                ch_s "Я извиняюсь, [Speaker.Petname], здесь не подходящее место для этого."
                        if B >= 100:
                                ch_s "Я извиняюсь, [Speaker.Petname], подобным стоит заниматься лишь в приватной обстановке. . ."
                        else:
                                ch_s "Я извиняюсь, [Speaker.Petname], мне просто не интересно."
                elif Speaker is JubesX:
                        if B <= 0:
                                ch_v "Извини, [Speaker.Petname], она не в моем вкусе."
                        if Speaker.Taboo > 20:
                                ch_v "Извини, [Speaker.Petname], по крайней мере, не здесь."
                        if B >= 100:
                                ch_v "Извини, [Speaker.Petname], мне не нужны зрители. . ."
                        else:
                                ch_v "Извини, [Speaker.Petname], мне такое не нравится."
                elif Speaker is GwenX:
                        if B <= 0:
                                ch_g "Извини, [Speaker.Petname], дело не во мне, а в тебе, [Subject.Tag]."
                        if Speaker.Taboo > 20:
                                if not Player.Male:
                                    ch_g "Извини, [Speaker.Petname], ты выбрала неудачное место."
                                else:
                                    ch_g "Извини, [Speaker.Petname], ты выбрал неудачное место."
                        if B >= 100:
                                ch_g "Извини, [Speaker.Petname], но это интимное дело. . ."
                        else:
                                ch_g "Извини, [Speaker.Petname], это перебор."
                elif Speaker is BetsyX:
                        if B <= 0:
                                ch_b "Прошу прощения, [Speaker.Petname], [Subject.Tag] и я не особо ладим."
                        if Speaker.Taboo > 20:
                                ch_b "Прошу прощения, [Speaker.Petname], мы сейчас в неудачном месте."
                        if B >= 100:
                                ch_b "Прошу прощения, [Speaker.Petname], меня не интересуют зрители. . ."
                        else:
                                ch_b "Прошу прощения, [Speaker.Petname], я просто не могу."
                elif Speaker is DoreenX:
                        if B <= 0:
                                ch_d "Извини, [Speaker.Petname], мне просто. . . она не нравится (извини!)."
                        if Speaker.Taboo > 20:
                                ch_d "Извини, [Speaker.Petname], я просто. . . не могу заняться чем-то подобным в таком месте."
                        if B >= 100:
                                ch_d "Извини, [Speaker.Petname], я просто. . . не могу, когда на меня смотрят."
                        else:
                                ch_d "Извини, [Speaker.Petname], я просто. . . не могу."
                elif Speaker is WandaX:
                        if B <= 0:
                                ch_w "Прости, [Speaker.Petname], она мне не очень нравится."
                        if Speaker.Taboo > 20:
                                ch_w "Прости, [Speaker.Petname], здесь слишком людно."
                        if B >= 100:
                                if not Player.Male:
                                    ch_w "Прости, [Speaker.Petname], я не хочу, чтобы ты наблюдала за нами."
                                else:
                                    ch_w "Прости, [Speaker.Petname], я не хочу, чтобы ты наблюдал за нами."
                        else:
                                ch_w "Прости, [Speaker.Petname], мне это неинтересно."
        # end failure text

        return Result

#End Ch_Focus.Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >

label Les_FirstKiss:
        # called when there is a first kiss situation between two girls
        if "les " + Partner.Tag in Ch_Focus.History:
                #if they've been together before
                $ Line = "experienced"
        elif Ch_Focus.Les and Partner.Les:
                #if both have kissed girls before
                $ Line = "first both"
        elif Ch_Focus.Les:
                # Girl's had experience
                $ Line = "first girl"
        elif Partner.Les:
                #Partner's had experience
                $ Line = "first partner"

        if Line == "experienced":
                "[Ch_Focus.Name] и [Partner.Name] сливаются в страстном поцелуе."
                "[Ch_Focus.Name] крепко прижимает к себе [Partner.Name_vin] за шею."
        else:
                if Line in ("first both", "first girl"):
                        # Girl's first time
                        "[Ch_Focus.Name] медленно подходит к [Partner.Name_dat] и нежно целует."
                else:
                        #not Girl's first time
                        "[Ch_Focus.Name] небрежно кладет руку на спину [Partner.Name_rod] и целует."
                if Line == "first partner":
                        #other girl's first time
                        "[Partner.Name] немного отстраняется, но затем берет себя в руки."
                else:
                        #not other girl's first time
                        "[Partner.Name] расплывается в улыбке и притягивает [Ch_Focus.Name_vin] еще ближе."
                "С каждой секундой между ними все больше и больше страсти."
        return
#End Ch_Focus.Les_Response / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Girl Whammy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Girl_Whammy(Other=0):
    #called when Jean is involved in a threesome, makes her whammy the other girl
#    if Other not in TotalGirls:
#            return
    if "nowhammy" not in JeanX.Traits and Other.LikeJean < 800:
            #this raises a girl's like-Jean stat if Jean wants to sleep with her
            $ Player.AddWord(1,0,0,0,"whammied") #adds a whammied marker to the player's history for chat options
            if Other == EmmaX and EmmaX.Lvl >= JeanX.Lvl:
                    ch_e "Ох, со мной это не сработает, Мисс Грей."
                    return
            if Other == JubesX and JubesX.Lvl >= JeanX.Lvl:
                    ch_v "Вампирская порча бьет мутанскую!"
                    return
            if "Jeaned" not in Other.Traits:
                    $ Other.Traits.append("Jeaned") #got whammied tag
                    $ setattr(JeanX,"LikeS"+Other.Tag,Other.LikeJean)     #$ JeanX.LikeSRogue = RogueX.LikeJean
            $ Other.LikeJean += 500 if Other.LikeJean <= 900 else Other.LikeJean
            $ Other.LikeJean = 900 if Other.LikeJean >= 900 else Other.LikeJean
    return
# End Girl Whammy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Les activity change  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Les_Change(Primary = 0, Secondary=Partner, D20S=0, PrimaryLust=0, SecondaryLust=0): #nee (D20S=0, Secondary=Partner, Primary = "Rogue", PrimaryLust=0, SecondaryLust=0):
        # for Lesbian primary activity: Threeway_Set(Primary,"preset", "lesbian", Girl.Offhand, ActiveGirl)
        #this is called when the player wants to change over a lesbian T3 behavior.
        # call Les_Change(RogueX)
        if Partner not in TotalGirls or Partner == Ch_Focus:
                return
        $ Line = 0
        menu:
            "Слушай, [Ch_Focus.Name]. . ."
            "почему бы тебе не поцеловать ее?" if Ch_Focus.Offhand != "kiss girl" and Ch_Focus.Offhand != "kiss both":
                        call Threeway_Set(Ch_Focus,Partner,"kiss girl",Ch_Focus.Offhand,"lesbian")
            "почему бы тебе не схватить ее за сиськи?" if Ch_Focus.Offhand != "fondle girl breasts":
                        call Threeway_Set(Ch_Focus,Partner,"fondle girl breasts",Ch_Focus.Offhand,"lesbian")
            "почему бы тебе не пососать ее сиськи?" if Ch_Focus.Offhand != "suck girl breasts":
                        call Threeway_Set(Ch_Focus,Partner,"suck girl breasts",Ch_Focus.Offhand,"lesbian")
            "почему бы тебе не поласкать ее пальцем?" if Ch_Focus.Offhand != "fondle girl pussy":
                        call Threeway_Set(Ch_Focus,Partner,"fondle girl pussy",Ch_Focus.Offhand,"lesbian")
            "почему бы тебе не спуститься к ее киске?" if Ch_Focus.Offhand != "lick girl pussy":
                        call Threeway_Set(Ch_Focus,Partner,"lick girl pussy",Ch_Focus.Offhand,"lesbian")
            "почему бы тебе не схватить ее за попку?" if Ch_Focus.Offhand != "fondle girl ass":
                        call Threeway_Set(Ch_Focus,Partner,"fondle girl ass",Ch_Focus.Offhand,"lesbian")
            "почему бы тебе не вылизать ее попку?" if Ch_Focus.Offhand != "lick girl ass": #if Trigger3 != "lick ass":
                        call Threeway_Set(Ch_Focus,Partner,"lick girl ass",Ch_Focus.Offhand,"lesbian") #call Threeway_Set(Ch_Focus,"lick ass", "lesbian", Trigger3,Partner)
            "Неважно.":
                pass
        if not Line:
            $ Line = "Вы возвращаетесь к тому, чем занимались ранее."
        else:
            $ Situation = "skip"
        "[Line]"
        return
# End Les activity change  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Girl BJ Offhand Speed Menu  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_BJ_Menu(Girl=Ch_Focus):
        call Seen_First_Peen(Ch_Focus,Partner,React="bj")
        if not Player.Male:
            jump Girl_CUN_Menu
        menu:
            "Облизывай его. . ." if Speed != 1:
                    $ Girl.DrainWord("setpace",1,0,0,0)
                    $ Speed = 1
            "Облизывай его. . . (locked)" if Speed == 1:
                    pass

            "Возьми в рот головку. . ." if Speed != 2:
                    $ Girl.DrainWord("setpace",1,0,0,0)
                    $ Speed = 2
            "Возьми в рот головку. . . (locked)" if Speed == 2:
                    pass

            "Соси его." if Speed != 3:
                    $ Girl.DrainWord("setpace",1,0,0,0)
                    $ Speed = 3
                    if Trigger2 == "jackin":
                        "Она опускает голову чуть ниже и вы убираете свою руку."

            "Соси его. (locked)" if Speed == 3:
                    pass

            "Заглоти его." if Speed != 4:
                    $ Girl.DrainWord("setpace",1,0,0,0)
                    if Trigger2 == "jackin" and Speed != 3:
                        "Она заглатывает ваш член по самые яйца, а вы убираете свою руку."
                    $ Speed = 4
            "Заглоти его. (locked)" if Speed == 4:
                    pass

            "Делай, что тебе больше хочется. . .":
                    "[Girl.Name] издает звук согласия."
                    if "setpace" not in Girl.DailyActions:
                        $ Girl.Statup("Love", 80, 2)
                    $ D20 = renpy.random.randint(1, 20)
                    if Girl.Blow < 5:
                        $ D20 -= 10
                    elif Girl.Blow < 10:
                        $ D20 -= 5

                    if D20 > 15:
                        call Speed_Shift(4)
                        if "setpace" not in Girl.DailyActions:
                            $ Girl.Statup("Inbt", 80, 3)
                    elif D20 > 10:
                        $ Speed = 3
                    elif D20 > 5:
                        $ Speed = 2
                    else:
                        $ Speed = 1
                    $ Girl.AddWord(1,"setpace","setpace")
            "Неважно. . .":
                    pass
        return
# End Girl BJ Offhand Speed Menu  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label JackCheck(Special=0):
    # called when seeing if the player wants to jack it, 1 reports back that you tried, 2 actually starts it
    # call JackCheck
    if not Trigger2:
        menu:
            "Начать дрочить?" if Trigger2 != "jackin" and Player.Male:
                    if Special:
                        if Special == 2:
                            $ Trigger2 = "jackin"
                            "Пока они отвлечены, вы начинаете дрочить."
                        return 1
                    else:
                        call Jackin(Ch_Focus,1)
            "Начать мастурбировать?" if Trigger2 != "jilling" and Player.Male != 1:
                    if Special:
                        if Special == 2:
                            $ Trigger2 = "jilling"
                            "Пока они отвлечены, вы начинаете играть со своей киской."
                        return 2
                    else:
                        call Jilling(Ch_Focus,1)
            "Посмотрим, чем это закончится.":
                        pass
    return 0
