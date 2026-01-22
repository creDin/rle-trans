
# Start Main Phase / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Group_Strip_Study(BO=[],QuizOrder=[]):
    $ Count = 0
    $ Count2 = 1
    $ Cnt = 0
    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # The entire list of objects. . .
    $ renpy.random.shuffle(QuizOrder)  # . . .shuffled randomly. . .
    if EmmaX in Party and Party[0] != EmmaX:
            # Forces Emma into the lead
            $ Party.reverse()
            call Shift_Focus(Party[0])
            if len(Party) >= 2 and Second == Party[0]:
                    $ Second = Party[1]

    # intros
    if Party[0] is RogueX:
            if not RogueX.Over and not RogueX.Legs and RogueX.PantiesNum <= 5:
                    #if she's mostly naked, cheat
                    $ RogueX.FaceChange("sly")
                    ch_r "Ну, я тут подумала и решила предложить тебе \"стрип-обучение,\". . ."
                    $ RogueX.Eyes = "down"
                    ch_r "но, похоже, придется отложить его на другой раз. . ."
                    $ RogueX.Eyes = "squint"
                    ch_r "У тебя есть что-нибудь еще на примете?"
                    call SexMenu
                    return
            "[RogueX.Name] подходит немного ближе к вам, а затем предлагает заняться \"стрип-обучением.\""
            ch_r "Хорошо, [RogueX.Petname], все просто. Я буду задавать тебе вопросы, если ты отвечаешь верно, я что-нибудь с себя снимаю. . ."
            ch_r "Сделаешь три ошибки и ты в пролете. Удачи."
    elif Party[0] is KittyX:
            "[KittyX.Name] забирает книгу из ваших рук и откладывает в сторону."
            if not KittyX.Over and not KittyX.Legs:
                    #if she's mostly naked, cheat
                    $ KittyX.FaceChange("sly")
                    ch_k "Я тут[KittyX.like]подумывала о \"стрип-обучение,\". . ."
                    $ KittyX.Eyes = "down"
                    ch_k "но это будет довольно короткая игра. . ."
                    $ KittyX.Eyes = "squint"
                    ch_k "У тебя есть какие-нибудь другие идейки?"
                    call SexMenu
                    return
            "Затем она спрашивает, не хотите ли вы поучавствовать в \"стрип-обучении?\""
            $ KittyX.FaceChange("perplexed", 2)
            ch_k "Ладно, итак[KittyX.like]если ты даешь правильный ответ. . . Я снимаю с себя часть одежды. . ."
            ch_k "Но у тебя всего только три попытки."
            $ KittyX.FaceChange("sly", 1)
    elif Party[0] is EmmaX:
            call Emma_StripStudy_Intro #special intro for Emma. . .
            if not _return:
                    #if you aren't on board, it reverts to the previous scene
                    return
            ch_e "Я очень серьезно отношусь к процессу обучения."
            $ EmmaX.FaceChange("bemused", Eyes="side")
            ch_e "Итак, если правильно ответишь на заданный вопрос. . . "
            ch_e ". . ."
            $ EmmaX.FaceChange("sly")
            ch_e "Я сниму с себя часть одежды. . ."
            ch_e "Но у тебя всего только три попытки."
    elif Party[0] is LauraX:
            #Laura does not do Strip Study solo, she's not interested.
            $ LauraX.FaceChange("sly", 1)
            "[LauraX.Name] забирает книгу из ваших рук и откладывает в сторону."
            ch_l "Мне малость надоело, может хочешь потрогать меня или что-нибудь типа того?"
            menu:
                "Sure?":
                        ch_l "Хорошо."
                        "[LauraX.Name] хватает вашу руку и прижимает ее к своей груди."
                        call Date_Sex_Break(LauraX,Second)
                        if _return == 4:
                                "[LauraX.Name] прекращает свое действие."
                                ch_l "На этом все."
                                return
                        if _return == 3:
                                #if the other girl took off. . .
                                menu:
                                    ch_l "Продолжим?"
                                    "Давай.":
                                            ch_l "Угу-м."
                                    "Мы должны остановиться.":
                                            ch_l "Гррр."
                                            return
                        call Girl_FB_Prep
                        if Situation:
                                #if she quits back having wanted to try something else. . .
                                jump SexMenu
                "Честно говоря, я думаю, мы должны заниматься.":
                        $ LauraX.FaceChange("perplexed", 1)
                        ch_l "?"
                        $ LauraX.Statup("Love", 80, -5)
                        $ LauraX.Statup("Obed", 70, 10)
                        $ LauraX.Statup("Inbt", 70, -5)
                        if ApprovalCheck(LauraX,600,"L"):
                                $ LauraX.FaceChange("sadside", 1)
                        else:
                                $ LauraX.FaceChange("angry", 1)
                        ch_l "А? Ну, ладно. Будь по твоему."
            return
    elif Party[0] is JeanX:
            #Jean does not do Strip Study solo, she's not interested.
            "[JeanX.Name] забирает книгу из ваших рук и откладывает в сторону."
            ch_j "Это так -скучно!-"
            $ JeanX.FaceChange("sly", 1)
            ch_j "Может, немного пошалим?"
            menu:
                "Конечно?":
                        ch_j "Хорошо."
                        "[JeanX.Name] хватает вашу руку и прижимает ее к своей груди."
                        call Date_Sex_Break(JeanX,Second)
                        if _return == 4:
                                "[JeanX.Name] прекращает свое действие."
                                ch_j "Ладно, все, руки прочь. . ."
                                return
                        if _return == 3:
                                #if the other girl took off. . .
                                menu:
                                    ch_j "Продолжим?"
                                    "Давай.":
                                            ch_j "Классно."
                                    "Мы должны остановиться.":
                                            ch_j "Ладно."
                                            return
                        call Girl_FB_Prep
                        if Situation:
                                #if she quits back having wanted to try something else. . .
                                jump SexMenu
                "Честно говоря, я думаю, мы должны заниматься.":
                        $ JeanX.FaceChange("perplexed", 1)
                        ch_j "Ты сейчас серьезно?"
                        $ JeanX.Statup("Love", 80, -5)
                        $ JeanX.Statup("Obed", 70, 10)
                        $ JeanX.Statup("Inbt", 70, -5)
                        if ApprovalCheck(JeanX,600,"L"):
                                $ JeanX.FaceChange("sadside", 1)
                        else:
                                $ JeanX.FaceChange("angry", 1)
                        ch_j "Хм. Ну хорошо."
                        "Это было не хорошо. . ."
            return
    elif Party[0] is StormX:
            ch_s "Думаю, тебя бы не помешало немного поощрить. . ."
            $ StormX.FaceChange("bemused", Eyes="side")
            ch_s "Если ты правильно ответишь на вопрос. . . "
            ch_s ". . ."
            $ StormX.FaceChange("sly")
            ch_s "Я сниму что-нибудь из одежды. . ."
            ch_s "Ты можешь ошибиться всего три раза, имей это ввиду."
    elif Party[0] is JubesX:
            "[JubesX.Name] забирает книгу из ваших рук и откладывает в сторону."
            if not JubesX.Over and not JubesX.Legs:
                    #if she's mostly naked, cheat
                    $ JubesX.FaceChange("sly")
                    ch_v "Я было подумала предложить тебе заняться \"стрип-обучением,\". . ."
                    $ JubesX.Eyes = "down"
                    ch_v "но что в этом веселого? . ."
                    $ JubesX.Eyes = "squint"
                    ch_v "Может, ты сможешь предложить что-нибудь более интересное?"
                    call SexMenu
                    return
            ch_v "Слушай, может быть, тебя заинтересует \"стрип-обучение?\""
            $ JubesX.FaceChange("perplexed", 2)
            ch_v "Надеюсь, ты понимаешь правила?"
            ch_v "Я задаю вопрос, ты отвечаешь. . ."
            ch_v "-но стоит тебе всего три раза ошибиться, и ты выбываешь."
            ch_v "Ответишь на вопрос -правильно,- и, возможно, я немного оголюсь. . ."
            $ JubesX.FaceChange("sly", 1)
    elif Party[0] is GwenX:
            "[GwenX.Name] наклоняется немного ближе к вам. . . некомфортно близко. . ."
            if not GwenX.Over and not GwenX.Legs:
                    #if she's mostly naked, cheat
                    $ GwenX.FaceChange("sly")
                    ch_g "Разве мы уже не достаточно \"позанимались\"?"
                    $ GwenX.Eyes = "down"
                    ch_g "Так воооот. . ."
                    $ GwenX.Eyes = "squint"
                    ch_g "Может, займемся чем-нибудь более интересным?"
                    call SexMenu
                    return
            ch_g "Разве мы уже не достаточно \"позанимались\"?"
            $ GwenX.FaceChange("perplexed", 2)
            ch_g "Как насчет того, чтобы вместо обычных занятий устроить \"стрип-обучение?\"?"
            ch_g "Я задаю вопрос, а ты отвечаешь. . ."
            ch_g "-но стоит только сделать три ошибки, и ты выбываешь из игры."
            ch_g "Отвечаешь правильно - и, возможно, я скидываю часть своей одежды. . ."
            $ GwenX.FaceChange("sly", 1)
    elif Party[0] is BetsyX:
            "[BetsyX.Name] придвигается ближе к вам и кладет руку вам на плечо. . ."
            if not BetsyX.Over and not GwenX.Legs:
                    #if she's mostly naked, cheat
                    $ BetsyX.FaceChange("sly")
                    ch_b "Пожалуй, основную программу мы уже освоили. . ."
                    $ BetsyX.Eyes = "down"
                    ch_b "В таком случае. . ."
                    $ BetsyX.Eyes = "squint"
                    ch_b "У тебя есть идеи, чем еще можно заняться?"
                    call SexMenu
                    return
            ch_b "Пожалуй, основную программу мы уже освоили. . ."
            $ BetsyX.FaceChange("bemused", 2)
            ch_b "Может. займемся. . . \"стрип-обучением?\""
            if not Player.Male:
                ch_b "Я задаю вопрос, а ты должна ответить на него правильно. . ."
            else:
                ch_b "Я задаю вопрос, а ты должен ответить на него правильно. . ."
            ch_b "И тогда я, возможно, снимаю часть своей одежды. . ."
            ch_b "-однако, у тебя только три права на ошибку."
            $ BetsyX.FaceChange("sly", 1)
    elif Party[0] is DoreenX:
            "[DoreenX.Name] берет книгу из ваших рук и откладывает ее в сторону."
            if not DoreenX.Over and not DoreenX.Legs:
                    #if she's mostly naked, cheat
                    $ DoreenX.FaceChange("sly")
                    ch_d "Я было подумала, что мы можем заняться \"стрип-обучением,\". . ."
                    $ DoreenX.Eyes = "down"
                    ch_d "но это довольно короткая игра. . ."
                    $ DoreenX.Eyes = "squint"
                    ch_d "Может, займемся чем-то другим?"
                    call SexMenu
                    return
            "Затем она спрашивает, не хотите ли вы заняться \"стрип-обучением?\""
            $ DoreenX.FaceChange("perplexed", 2)
            ch_d "Итак. . . если ты правильно отвечаешь. . . я снимаю что-нибудь из одежды.. . ."
            ch_d "Ты можешь ошибиться всего три раза."
            $ DoreenX.FaceChange("sly", 1)
    elif Party[0] is WandaX:
            "[WandaX.Name] берет книгу из ваших рук и откладывает ее в сторону."
            if not WandaX.Over and not WandaX.Legs:
                    #if she's mostly naked, cheat
                    $ WandaX.FaceChange("sly")
                    ch_w "Ладно, на сегодня хватит учебы."
                    $ WandaX.Eyes = "down"
                    ch_w "Есть идеи, чем мы можем заняться?"
                    $ WandaX.Eyes = "squint"
                    call SexMenu
                    return
            $ WandaX.FaceChange("sly", 1)
            ch_w "Слушай, когда я была за решеткой, мы порой играли в стрип-покер."
            ch_w "Не хочешь попробовать, но вместо покера я буду задавать вопросы?"
            ch_w "Отвечаешь правильно. . . я снимаю какую-нибудь часть одежды. . ."
            ch_w "Я дам тебе три попытки."
    # end Intro

    $ BO = Party[:]
    while BO:
            $ BO[0].AddWord(1,0,"stripstudy",0,"stripstudy") #adds to Daily and History
            $ BO.remove(BO[0])

    if len(Party) >= 2:
            if Cnt == 3:
                    #if from the Emma menu she didn't agree to participate. . .
                    pass
            elif ApprovalCheck(Party[1], 1300) or ApprovalCheck(Party[1], 500,"I") or Party[1] is WandaX:
                    if Party[1] is RogueX:
                            ch_r "Я думаю, будем по очереди."
                    elif Party[1] is KittyX:
                            ch_k "Итак[KittyX.like]наверное, будем по очереди?"
                    elif Party[1] is EmmaX:
                            ch_e "Полагаю, мы будем задавать вопросы по очереди."
                    elif Party[1] is LauraX:
                            ch_l "Займу свою очередь."
                    elif Party[1] is JeanX:
                            ch_j "Хорошо, дайте мне попробовать."
                    elif Party[1] is StormX:
                            ch_s "Пожалуй, я тоже могла бы присоединиться. . ."
                    elif Party[1] is JubesX:
                            ch_v "Значит, будем по очереди, да?"
                    elif Party[1] is GwenX:
                            ch_g "Звучит весело!"
                    elif Party[1] is BetsyX:
                            ch_b "Это звучит довольно весело!"
                    elif Party[1] is DoreenX:
                            ch_d "Звучит весело!"
                    elif Party[1] is WandaX:
                            ch_w "Ладно."
            else:
                    #she refuses
                    if Party[1] == JeanX:
                            ch_j "Не, это глупо."
                            "Она просто сидит и наблюдает."
                            $ Party.remove(JeanX)
                    else:
                            if Party[1] is RogueX:
                                    ch_r "Меня это не устраивает."
                            elif Party[1] is KittyX:
                                    ch_k "Эм, мне это не особо нравится."
                            elif Party[1] is EmmaX:
                                    ch_e "Это возмутительно."
                            elif Party[1] is LauraX:
                                    ch_l "Я так не думаю."
                            elif Party[1] is StormX:
                                    ch_s "Я не хочу принимать в этом участие. . ."
                            elif Party[1] is JubesX:
                                    ch_v "Извините, ребята, у -вас- тут своя атмосфера. . ."
                            elif Party[1] is GwenX:
                                    ch_g "Эм. . . я должна просто. . . уйти. . ."
                            elif Party[1] is BetsyX:
                                    ch_b "Возможно, мне следует оставить вас наедине. . ."
                            elif Party[1] is DoreenX:
                                    ch_d "Ох. . . эм. . . ладно, ребята, веселитесь!"
                            elif Party[1] is WandaX:
                                    ch_w "Хех, развлекайтесь."
                            "[Party[1].Name] выходит из комнаты."
                            call Remove_Girl(Party[1])

    #Primary loop
    while Count2:
            #"Question [Count2]. . ."
            call expression Party[0].Tag + "_Quiz_Question"

            $ Count2 += 1

            if _return:
                    call Strip_Study_Right
            else:
                    $ Count += 1
                    call Strip_Study_Wrong
                    if Count2 == 0 and len(Party) >= 2 and not Party[1].ClothingCheck:
                            #if you failed out, but the other girl is nude. . .
                            menu:
                                "[Party[1].Name], мы с тобой все еще могли бы развлечься. . .":
                                        $ Tempmod = 50
                                        call SexMenu # call expression Party[0].Tag + "_SexMenu"
                                "Тогда облом":
                                        pass

            if len(Party) >= 2 and Cnt != 3 and Party[1].ClothingCheck:
                    #if there are multiple girls, and the other girl is not nude, alternate
                    $ Party.reverse()
                    call Shift_Focus(Party[0])
                    if len(Party) >= 2 and Second == Party[0]:
                            $ Second = Party[1]
    #Loop ends when Count2 is 0 due to failures, returns to sender

    return

# End Main Phase / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start "Question right" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Strip_Study_Right:
        if Party[0].Hose:
                # Will she lose the hose?
                $ Line = get_clothing_name(Party[0].Hose_key, vin)
                $ Party[0].Hose = 0
                "Она медленно снимает с себя [Line]. . ."
                $ Party[0].Statup("Lust", 50, 3)
                return

        if Party[0] in (JubesX,DoreenX) and Party[0].Acc:
                # Will she lose the jacket?
                $ Line = get_clothing_name(Party[0].Acc_key, vin)
                $ Party[0].Acc = 0
                "Она снимает с себя [Line]. . ."
                call AnyLine(Party[0],"Знаешь что? Держи небольшой бонус. . .")

        if Party[0].Over:
            #will she lose the top?
            if Party[0] is StormX or Party[0].SeenChest or (Party[0].Chest and ApprovalCheck(Party[0], 300)) or ApprovalCheck(Party[0], 850):
                    $ Party[0].Statup("Inbt", 25, 1)
                    $ Party[0].Statup("Inbt", 50, 1)
                    $ Line = get_clothing_name(Party[0].Over_key, vin)
                    $ Party[0].Over = 0
                    "Она стягивает с себя [Line] и отбрасывает в сторону."
                    if not Party[0].Chest:
                        call Girl_First_Topless(Party[0])
            else:
                    if Party[0] is RogueX:
                            ch_r "Знаешь, думаю, я еще не готова, извини, [Party[0].Petname]. Я не должна была так себя вести."
                    elif Party[0] is KittyX:
                            ch_k "Извини, я не хотела тебя дразнить, я просто еще не готова."
                    elif Party[0] is EmmaX:
                            ch_e "Извини, я не хотела тебя дразнить, но я сомневаюсь, что ты справишься."
                    elif Party[0] is LauraX:
                            $ LauraX.FaceChange("sly", 2)
                            if not Player.Male:
                                ch_l "Хех, ты хорошо подготовлена, да?"
                            else:
                                ch_l "Хех, ты хорошо подготовлен, да?"
                            $ LauraX.FaceChange("bemused", 1)
                    elif Party[0] is JeanX:
                            ch_j "Ребячество."
    #                elif Party[0] is StormX:    #should be unnecessary, she should never refuse
    #                        ch_s "I suppose I could join in as well. . ."
                    elif elif Party[0] is JubesX:
                            ch_v "Я, эм. . . Пока я, вроде как, все. . ."
                    elif Party[0] is GwenX:
                            ch_g "Ха, ладно, все как-то серьезно. . ."
                    elif Party[0] is BetsyX:
                            ch_b "Ох, дорогуша, возможно, я недооценила тебя."
                    elif Party[0] is DoreenX:
                            ch_d "Ладно. . . ох. . . не ладно. . . Я не могу, извини."
                    elif Party[0] is WandaX:
                            ch_w "Воу, все становится слишком реальным. . ."
                    $ Count2 = 0
            return

        if Party[0].Legs:
            #will she lose the pants/skirt?
            if Party[0] == StormX or (Party[0].SeenPanties and Party[0].SeenPussy) or (Party[0].Panties and (ApprovalCheck(Party[0], 700) or Party[0].SeenPanties)) or ApprovalCheck(Party[0], 950):
                    $ Party[0].Statup("Lust", 50, 5)
                    $ Party[0].Statup("Inbt", 30, 1)
                    $ Party[0].Statup("Inbt", 50, 1)
                    $ Line = get_clothing_name(Party[0].Legs_key, vin)
                    $ Party[0].Legs = 0
                    "Она расстегивает [Line] и стягивает вниз."
                    if Party[0].Panties:
                        if not Party[0].SeenPanties:
                                $ Party[0].Statup("Inbt", 200, 2)
                                $ Party[0].Statup("Inbt", 50, 3)
                                $ Party[0].SeenPanties = 1
                    else:
                        #R seen pussy
                        $ Party[0].Blush = 1
                        "Вы видите, что на ней, очевидно, нет трусиков. Она слегка краснеет."
                        call Girl_First_Bottomless(Party[0])
            else:
                    if Party[0] is RogueX:
                            ch_r "Знаешь, думаю, я еще не готова, извини, [Party[0].Petname]. Я не должна была так себя вести."
                    elif Party[0] is KittyX:
                            ch_k "Извини, я не хотела тебя дразнить, я просто еще не готова."
                    elif Party[0] is EmmaX:
                            ch_e "Извини, я не хотела тебя дразнить, но я сомневаюсь, что ты справишься."
                    elif Party[0] is LauraX:
                            ch_l "Неет, пока на этом все."
                    elif Party[0] is JeanX:
                            ch_j "Ребячество."
                    elif elif Party[0] is JubesX:
                            ch_v "Ага, извини, не думаю, что хочу продолжать. . ."
                    elif Party[0] is GwenX:
                            ch_g "Ха, ладно, это немного серьезно. . ."
                    elif Party[0] is BetsyX:
                            ch_b "Ох, дорогуша, возможно, я недооценила тебя."
                    elif Party[0] is DoreenX:
                            ch_d "Ладно. . . ох. . . не ладно. . . Я не могу, извини."
                    elif Party[0] is WandaX:
                            ch_w "Воу, все становится слишком реальным. . ."
                    $ Count2 = 0
            return

        if Party[0].Chest: # Will she go topless?
            if Party[0] == StormX or ApprovalCheck(Party[0], 900) or (Party[0].SeenChest and ApprovalCheck(Party[0], 600)):
                    $ Party[0].Statup("Lust", 60, 5)
                    $ Party[0].Statup("Inbt", 50, 2)
                    $ Party[0].Statup("Inbt", 200, 1)
                    $ Line = get_clothing_name(Party[0].Chest_key, vin)
                    $ Party[0].Chest = 0
                    "Она снимает [Line] и отбрасывает в сторону."
                    if not Party[0].SeenChest:
                            $ Party[0].Statup("Inbt", 200, 3)
                            $ Party[0].Statup("Inbt", 50, 1)
                            call Girl_First_Topless(Party[0])
                    $ Player.Statup("Focus", 80, 15)
            else:
                    if Party[0] is RogueX:
                            ch_r "Я знаю, сделка есть сделка, но я не хотела бы оголять грудь. Извини, [Party[0].Petname]."
                    elif Party[0] is KittyX:
                            ch_k "Так. . . Я знаю, что уже поздно говорить об этом, но я не хотела бы оголять грудь."
                    elif Party[0] is EmmaX:
                            $ EmmaX.FaceChange("perplexed", 1)
                            ch_e "Хмм. . . ты лучше, чем я думала."
                            $ EmmaX.FaceChange("sly", 1)
                            if not Player.Male:
                                ch_e "Но я сомневаюсь, что ты к этому уже готов."
                            else:
                                ch_e "Но я сомневаюсь, что ты к этому уже готов."
                    elif Party[0] is LauraX:
                            ch_l "Да, пока хватит."
                    elif Party[0] is JeanX:
                            ch_j "Ребячество."
                    elif elif Party[0] is JubesX:
                            ch_v "Эм, извини, я не думаю, что хочу продолжать. . ."
                    elif Party[0] is GwenX:
                            ch_g "О, эм. . . все становится слишком \"реальным.\" . ."
                    elif Party[0] is BetsyX:
                            ch_b "Ох, дорогуша, это, пожалуй, уже чересчур."
                    elif Party[0] is DoreenX:
                            ch_d "Ладно. . . ох. . . не ладно. . . Я не могу, извини."
                    elif Party[0] is WandaX:
                            ch_w "Воу, все становится слишком реальным. . ."
                    $ Count2 = 0
            return

        if Party[0].Panties: # Will she go bottomless?
            if Party[0] is StormX or ApprovalCheck(Party[0], 950) or (Party[0].SeenPussy and ApprovalCheck(Party[0], 600)):
                    $ Party[0].Statup("Lust", 70, 10)
                    $ Party[0].Statup("Inbt", 70, 2)
                    $ Party[0].Statup("Inbt", 200, 2)
                    $ Line = get_clothing_name(Party[0].Panties_key, vin)
                    $ Party[0].Panties = 0
                    "Она спускает [Line], оставляя свою киску обнаженной."
                    if not Party[0].SeenPussy:
                            $ Party[0].Statup("Inbt", 50, 4)
                            $ Party[0].Statup("Inbt", 200, 4)
                            call Girl_First_Bottomless(Party[0])
                    $ Player.Statup("Focus", 75, 20)
            else:
                    if Party[0] is RogueX:
                            ch_r "Послушай, все зашло слишком далеко, [Party[0].Petname]. Я бы хотела закончить на сегодня."
                    elif Party[0] is KittyX:
                            ch_k "Оу, Я. . . Я не совсем готова к такому, прости!"
                    elif Party[0] is EmmaX:
                            $ EmmaX.FaceChange("perplexed", 1)
                            ch_e "Хмм. . . лучше, чем я думала."
                            $ EmmaX.FaceChange("sly", 1)
                            if not Player.Male:
                                ch_e "Но я сомневаюсь, что ты к этому уже готов."
                            else:
                                ch_e "Но я сомневаюсь, что ты к этому уже готов."
                    elif Party[0] is LauraX:
                            $ LauraX.FaceChange("perplexed", 2)
                            ch_l "Думаю, с тебя хватит."
                            $ LauraX.FaceChange("perplexed", 1)
                    elif Party[0] is JeanX:
                            ch_j "Ребячество."
                    elif elif Party[0] is JubesX:
                            ch_v "Ага, извини, не думаю, что хочу продолжать. . ."
                    elif Party[0] is GwenX:
                            ch_g "О, эм. . . все становится слишком \"реальным.\" . ."
                    elif Party[0] is BetsyX:
                            ch_b "Ох, дорогуша, это, пожалуй, уже чересчур."
                    elif Party[0] is DoreenX:
                            ch_d "Ладно. . . ох. . . не ладно. . . Я не могу, извини."
                    elif Party[0] is WandaX:
                            ch_w "Воу, все становится слишком реальным. . ."
                    $ Count2 = 0
            return

        if Party[0] is RogueX:
                $ KittyX.FaceChange("sly", 1)
                ch_r "Хорошо, еще один правильный ответ, но на мне больше ничего не осталось. . ."
        elif Party[0] is KittyX:
                ch_k "Итак. . . снова верно. . ."
                $ KittyX.Eyes = "down"
                ch_k ". . . но на мне[KittyX.like]больше ничего нет. . ."
                $ KittyX.FaceChange("sly", 1)
        elif Party[0] is EmmaX:
                $ EmmaX.FaceChange("sly", 1)
                ch_e "Хмм. . . снова верный ответ. . ."
                $ EmmaX.Eyes = "down"
                ch_e ". . . но мне больше нечего снимать. . ."
                $ EmmaX.FaceChange("sly", 1)
        elif Party[0] is LauraX:
                $ LauraX.FaceChange("sly", 1)
                ch_l "Итак. . . снова верно. . ."
                $ LauraX.Eyes = "down"
                ch_l ". . . но, похоже, мне больше нечего снять. . ."
                $ LauraX.FaceChange("sly", 1)
        elif Party[0] is JeanX:
                $ JeanX.FaceChange("sly", 1, Eyes="down")
                if not Player.Male:
                    ch_j "Что ж, похоже, ты уже сняла с меня все."
                else:
                    ch_j "Что ж, похоже, ты уже снял с меня все."
                $ JeanX.FaceChange("sly", 1)
                ch_j "Что ты теперь собираешься со мной делать? . . "
        elif Party[0] is StormX:
                $ StormX.FaceChange("sly", 1)
                ch_s "Хмм. . . правильный ответ. . ."
                $ StormX.Eyes = "down"
                ch_s ". . . но, как видишь, я уже голая. . ."
                $ StormX.FaceChange("sly", 1)
        elif elif Party[0] is JubesX:
                ch_v "Так, что у нас тут. . ."
                $ JubesX.FaceChange("sly", 1, Eyes="down")
                ch_v "Похоже, у меня закончились \"жетоны.\" . ."
                $ JubesX.FaceChange("sly", 1)
                ch_v "Есть идеи, чем мы могли бы заняться дальше?"
        elif Party[0] is GwenX:
                $ GwenX.FaceChange("sly")
                ch_g "Хм. . ."
                $ GwenX.Eyes = "down"
                ch_g "Похоже, у меня закончилась одежда. . ."
                $ GwenX.Eyes = "squint"
                ch_g "Есть идеи, чем можно еще заняться?"
        elif Party[0] is BetsyX:
                $ BetsyX.FaceChange("sly")
                ch_b "Ну что ж. . ."
                $ BetsyX.Eyes = "down"
                ch_b "Похоже, на мне закончилась одежда. . ."
                $ BetsyX.Eyes = "side"
                ch_b "Чем же нам теперь заняться. . ."
                $ BetsyX.Eyes = "squint"
                ch_b "Может быть, у тебя есть идеи?"
        elif Party[0] is DoreenX:
                $ DoreenX.FaceChange("sly")
                ch_d "Ладно. . . ох. . ."
                $ DoreenX.Eyes = "down"
                ch_d "Похоже, мне больше нечего снимать. . ."
                $ DoreenX.FaceChange("sly")
                ch_d "Можешь придумать, чем нам еще можно заняться?"
        elif Party[0] is WandaX:
                $ WandaX.FaceChange("sly")
                ch_w "Так. . ."
                $ WandaX.Eyes = "down"
                ch_w "Похоже, на этом игра заканчивается. . ."
                $ WandaX.Eyes = "side"
                ch_w "BНо у нас еще -осталось- время. . ."
                $ WandaX.Eyes = "squint"
                ch_w "Есть идеи?"

        if len(Party) >= 2:
                menu:
                    "Я могу придумать для тебя что-нибудь еще. . .":
                            pass
                    "Похоже, у [Party[1].Name_rod] есть вопросы ко мне. . ." if Party[1].ClothingCheck:
                            #if the other girl has anything on. . .
                            return
        $ Count2 = 0
        $ Tempmod = 50
        call SexMenu # call expression Party[0].Tag + "_SexMenu"
        if not Party:
                pass
        elif Party[0] is RogueX:
                ch_r "Мне очень понравилось."
        elif Party[0] is KittyX:
                ch_k "Думаю, я кое-чему научилась. . ."
        elif Party[0] is EmmaX:
                if not Player.Male:
                    ch_e "Надеюсь, ты чему-нибудь научилась. . ."
                else:
                    ch_e "Надеюсь, ты чему-нибудь научился. . ."
        elif Party[0] is LauraX:
                ch_l "Ну, это лучше, чем просто учиться. . ."
        elif Party[0] is JeanX:
                ch_j "Хорошо скоротали время."
        elif Party[0] is StormX:
                ch_s "Это было занимательное отступление. . ."
        elif elif Party[0] is JubesX:
                ch_v "Вот так мне нравится заканчивать обучение. . ."
        elif Party[0] is GwenX:
                ch_g "Ха, вот так я люблю учиться. . ."
        elif Party[0] is BetsyX:
                ch_b "Это было довольно продуктивное занятие."
        elif Party[0] is DoreenX:
                ch_d "Ну, это было довольно информативно. . ."
        elif Party[0] is WandaX:
                if not Player.Male:
                    ch_w "Уверена, ты что-то точно усвоила. . ."
                else:
                    ch_w "Уверена, ты что-то точно усвоил. . ."
        $ Count2 = 0
        return
# End "Question right" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start "Question wrong" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Strip_Study_Wrong:
        $ Party[0].FaceChange("sly", 1)
        if Count == 1:
                if Party[0] is RogueX:
                        ch_r "Тц, очень плохо, [RogueX.Petname]."
                elif Party[0] is KittyX:
                        ch_k "Не-а."
                elif Party[0] is EmmaX:
                        ch_e "К сожалению. . . нет."
                elif Party[0] is LauraX:
                        ch_l "Что?"
                elif Party[0] is JeanX:
                        ch_j "Не-а."
                elif Party[0] is StormX:
                        ch_s "Хмм. . . Боюсь, что нет."
                elif elif Party[0] is JubesX:
                        ch_v "Оооп, ошибка номер -раз-. . ."
                elif Party[0] is GwenX:
                        ch_g "Не-а. . . тебе нужно больше заниматься. . ."
                elif Party[0] is BetsyX:
                        ch_b "Ох, не повезло."
                elif Party[0] is DoreenX:
                        ch_d "Ох. . . нет. . ."
                elif Party[0] is WandaX:
                        ch_w "Хех, нет. . ."
        elif Count == 2:
                if Party[0] is RogueX:
                        ch_r "Ох, у тебя, похоже, не очень хорошо получается. Ну же, у тебя остался последний шанс."
                elif Party[0] is KittyX:
                        if not Player.Male:
                            ch_k "-Почти- проиграла. Последняя попытка."
                        else:
                            ch_k "-Почти- проиграл. Последняя попытка."
                elif Party[0] is EmmaX:
                        ch_e "Боюсь, что нет, последний шанс."
                elif Party[0] is LauraX:
                        if not Player.Male:
                            ch_l ". . . как ты вообще смогла снова ошибиться. . ."
                        else:
                            ch_l ". . . как ты вообще смог снова ошибиться. . ."
                elif Party[0] is JeanX:
                        ch_j "Далеко тебе до победы."
                elif Party[0] is StormX:
                        ch_s "Я разочарована. . ."
                elif elif Party[0] is JubesX:
                        ch_v "Ай, ошибка номер -два-, [JubesX.Petname]. . ."
                elif Party[0] is GwenX:
                        ch_g "Не-а. У тебя еще остался шанс на победу. . ."
                elif Party[0] is BetsyX:
                        ch_b "Боюсь, что сейчас тоже мимо."
                elif Party[0] is DoreenX:
                        ch_d "Даже не близко. . ."
                elif Party[0] is WandaX:
                        ch_w "Нет!"
        elif Count > 2:
                if Party[0] is RogueX:
                        ch_r "И ты выбываешь! Извини, [RogueX.Petname], спасибо за игру, на этом все."
                elif Party[0] is KittyX:
                        ch_k "Ой, как жалко. Возможно, повезет в другой раз."
                elif Party[0] is EmmaX:
                        ch_e "Жаль, я ожидала от тебя большего."
                elif Party[0] is LauraX:
                        ch_l "Что? К черту."
                elif Party[0] is JeanX:
                        if not Player.Male:
                            ch_j "Ты вообще заглядывала в конспекты?"
                        else:
                            ch_j "Ты вообще заглядывал в конспекты?"
                elif Party[0] is StormX:
                        ch_s "Ох, как прискорбно. . ."
                elif elif Party[0] is JubesX:
                        ch_v "О -нет!- И это ошибка номер -три!-"
                        if not Player.Male:
                            ch_v "Ты всех нас разочаровала. . ."
                        else:
                            ch_v "Ты всех нас разочаровал. . ."
                elif Party[0] is GwenX:
                        if not Player.Male:
                            ch_g "Оу, как жаль, ты не добралась до финального босса. . ."
                        else:
                            ch_g "Оу, как жаль, ты не добрался до финального босса. . ."
                elif Party[0] is BetsyX:
                        ch_b "Боюсь, тебе ужасно не повезло. В следующий раз, возможно, повезет больше."
                elif Party[0] is DoreenX:
                        ch_d "Ох. . . видимо, тебе сильно не везет. . ."
                elif Party[0] is WandaX:
                        if not Player.Male:
                            ch_w "Ты -безнадежна-!"
                        else:
                            ch_w "Ты -безнадежен-!"
                $ Count2 = 0
        return

# End "Question wrong" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Rogue Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Quiz_Question:
    if QuizOrder[Count2] == 1:
        menu:
            ch_r "Кто был первым, на ком я использовала свои способности?"
            "A. Колби":
                return 0
            "B. Ренли":
                return 0
            "C. Реми":
                return 0
            "D. Коди":
                return 1
    if QuizOrder[Count2] == 2:
        menu:
            ch_r "Где я жила до переезда к Ксавье?"
            "A. Луизиана":
                return 0
            "B. Миссисипи":
                return 1
            "C. Коннектикут":
                return 0
            "D. Теннесси":
                return 0
    if QuizOrder[Count2] == 3:
        menu:
            ch_r "Какой была первая способность, которую я. . . позаимствовала?"
            "A. Изменение внешности Мистик":
                return 0
            "B. Прохождение сквозь предметы Призрачной Кошки":
                return 0
            "C. Телепортация Ночного Змея":
                return 1
            "D. Лазер Циклопа":
                return 0
    if QuizOrder[Count2] == 4:
        menu:
            ch_r "Кто из мутантов удочерил меня до того, как проявились мои силы?"
            "A. Магнето":
                return 0
            "B. Мистик":
                return 1
            "C. Ксавье":
                return 0
            "D. Беласко":
                return 0
    if QuizOrder[Count2] == 5:
        menu:
            ch_r "В конце концов, я присоединилась к Людям Икс после того, как Мистик напала на меня. Где она напала на меня?"
            "A. В школе":
                return 0
            "B. На пляже":
                return 0
            "C. В горах":
                return 1
            "D. На берегу реки":
                return 0
    if QuizOrder[Count2] == 6:
        menu:
            ch_r "Когда Магнето отбирал самых подходящих мутантов для Астероида M, я была схвачен после того, как победила кое-кого из Братства. Кто это был?"
            "A. Пузырь":
                return 0
            "B. Лавина":
                return 0
            "C. Жаба":
                ch_r "Верно, [RogueX.Petname], Я засунула его лягушачий язык в дверцу машины."
                ch_r "Лучше не серди меня."
                return 1
            "D. Ртуть":
                return 0

    #remove this once I have enough questions
    "Она задает вопрос и вы правильно на него отвечаете."
    return 1


# Kitty Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Kitty_Quiz_Question:
    if QuizOrder[Count2] == 1:
        menu:
            ch_k "Ладно, знаешь[KittyX.like]откуда я родом? Какой мой родной город?"
            "A. Чикаго, Иллинойс":
                return 0
            "B. Дирфилд, Иллинойс":
                return 1
            "C. Город Нью-Йорк, штат Нью-Йорк":
                return 0
            "D. Сент-Луис, Миссури":
                return 0
    if QuizOrder[Count2] == 2:
        menu:
            ch_k "Как называется моя способность?"
            "A. Исчезнование":
                return 0
            "B. Призрачность":
                return 0
            "C. Нематериальность":
                return 1
            "D. Перемещение":
                return 0
    if QuizOrder[Count2] == 3:
        ch_k "Так вот. . . только не смейся, но у меня есть мягкая игрушка, с которой я сплю[KittyX.like]каждую ночь."
        menu:
            ch_k "Знаешь ее имя?"
            "A. Драко":
                return 0
            "B. Флиппер":
                return 0
            "C. Локхид":
                return 1
            "D. Н'гари":
                return 0

    if QuizOrder[Count2] == 4:
        if not Player.Male:
            ch_k "Ладно. Ты знала, что порой Доктор Маккой берет группу студентов, которые отстают в Естественных науках, на учебную экскурсию?"
        else:
            ch_k "Ладно. Ты знал, что порой Доктор Маккой берет группу студентов, которые отстают в Естественных науках, на учебную экскурсию?"
        menu:
            ch_k "Куда он с ними ходит?"
            "A. Великий Редвудский Лес, Калифорния":
                return 1
            "B. Гора Маккинли, Аляска":
                return 0
            "C. Гора Рашмор, Южная Дакота":
                return 0
            "D. Йеллоустонский Национальный Парк, Вайоминг":
                return 0
    if QuizOrder[Count2] == 5:
        ch_k "Одной из самых опасных угроз, о которой стоит волноваться всем мутантам, являются гигантские роботы под названием Стражи."
        menu:
            ch_k "Знаешь, кто их спроектировал?"
            "A. Аркада":
                return 0
            "B. Боливар Траск":
                return 1
            "C. Магнето":
                return 0
            "D. Унус Неприкасаемый":
                return 0
    if QuizOrder[Count2] == 6:
        ch_k "Знаешь, мы не всегда учились здесь, в Институте."
        ch_k "Какое-то время мы ходили в местную школу."
        menu:
            ch_k "В какую именно?"
            "A. Старшая Школа Бэйвилля":
                return 1
            "B. Королевская Мемориальная Старшая Школа":
                return 0
            "C. Старшая Школа Риверсайда":
                return 0
            "D. Старшая Школа Сета Пейна":
                return 0
    if QuizOrder[Count2] == 7:
        menu:
            ch_k "Это было давно, но ты знаешь, кем был первый встреченный мною мутант?"
            "A. Джин Грей":
                return 0
            "B. Ланс Алверс":
                return 1
            "C. Мистик":
                return 0
            "D. Профессор Ксавье":
                return 0
    if QuizOrder[Count2] == 8:
        ch_k "Роуг, Бум-Бум, Магма, Джин и я как-то создали команду по борьбе с преступностью и занялись делом, связанным с мошенничеством."
        ch_k "Хоть это было весело, но мы в конечном итоге распустили эту команду."
        menu:
            ch_k "В общем, как называлась наша команда?"
            "A. Мстители Бейвилла":
                return 0
            "B. Забияки Бейвилла":
                return 0
            "C. Гарпии Бейвилла":
                return 0
            "D. Сирены Бейвилла":
                return 1
    if QuizOrder[Count2] == 9:
        menu:
            ch_k "Ладно[KittyX.like]не то, чтобы я не знала, но ты знаешь средство против бомб-вонючек?"
            "A. Горячий душ":
                return 0
            "B. Метилэтилкетон":
                return 0
            "C. Изоляция":
                return 1
            "D. Томатный сок":
                return 0
    if QuizOrder[Count2] == 10:
        ch_k "Когда я использую свои силы, я не[KittyX.like]{i}совсем{/i} неуязвима."
        menu:
            ch_k "У кого есть способности, которые могут навредить мне?"
            "A. Пузырь":
                return 0
            "B. Магнето":
                return 0
            "C. Ртуть":
                return 0
            "D. Алая ведьма":
                return 1

 #remove this once I have enough questions
    "Она задает вопрос и вы правильно на него отвечаете."
    return 1

# Emma Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Quiz_Question:
    ch_e "Вопрос [Count2]. . ."
    if QuizOrder[Count2] == 1:
        menu:
            ch_e "Ты знаешь, где я жила в детстве?"
            "A. Манчестер, Англия":
                return 0
            "B. Город Нью-Йорк, штат Нью-Йорк":
                return 0
            "C. Бостон, Массачусетс":
                return 1
            "D. Лондон, Англия":
                return 0
    if QuizOrder[Count2] == 2:
        menu:
            ch_e "Какая у меня способность?"
            "A. Телекинез":
                return 0
            "B. Ледяные Силы":
                return 0
            "C. Телепатия":
                return 1
            "D. Выпекание":
                return 0
    if QuizOrder[Count2] == 3:
        ch_e "Когда-то я была лидером в одном. . . общественном клубе."
        menu:
            ch_e "Как назывался тот клуб?"
            "A. Акацуки":
                return 0
            "B. Гордость":
                return 0
            "C. Клуб Адского Пламени":
                return 1
            "D. Зловещая Шестерка":
                return 0

    if QuizOrder[Count2] == 4:
        menu:
            ch_e "Ты знаешь, как меня называют?"
            "A. Черная Королева":
                return 0
            "B. Белая Королева":
                return 1
            "C. Красная Королева":
                return 0
            "D. Могущественная Принцесса":
                return 0
    if QuizOrder[Count2] == 5:
        ch_e "У меня есть несколько близнецов, бродящих где-то. . . неподалеку."
        menu:
            ch_e "Как их называют?"
            "A. Кагебуншин":
                return 0
            "B. Степфордские Кукушки":
                return 1
            "C. Джейми Мэддрокс":
                return 0
            "D. Спайс Герлз":
                return 0
    if QuizOrder[Count2] == 6:
        menu:
            ch_e "Как называется, когда мутант развивает новую способность, не связанную с их первоначальной?"
            "A. Вторичная Мутация":
                return 1
            "B. Повышение Уровня":
                return 0
            "C. Дигивация":
                return 0
            "D. Супер-Мутация":
                return 0
    if QuizOrder[Count2] == 7:
        ch_e "Раньше я преподавала в островном государстве мутантов."
        menu:
            ch_e "Как оно называлось?"
            "A. Австралия":
                return 0
            "B. Геноша":
                return 1
            "C. Мартиника":
                return 0
            "D. Пирожный остров":
                return 0
    if QuizOrder[Count2] == 8:
        menu:
            ch_e "Когда мы впервые встретились, как я подстригала свои лобковые волосы?"
            "A. Никак":
                return 0
            "B. В форме \"X\"":
                return 0
            "C. Я не знаю":
                $ EmmaX.FaceChange("sadside", 1)
                if not EmmaX.SeenPussy:
                    ch_e "Нуу, думала, ты хотя бы предположишь. . ."
                else:
                    if not Player.Male:
                        ch_e "Очевидно, ты не уделяла этому достаточно внимания."
                    else:
                        ch_e "Очевидно, ты не уделял этому достаточно внимания."
                $ EmmaX.FaceChange("normal")
                return 0
            "D. Все идеально выбривала":
                $ EmmaX.FaceChange("sly", 1)
                ch_e "Хоть кто-то обратил на это внимание. . ."
                return 1
    if QuizOrder[Count2] == 9:
        menu:
            ch_e "Назови одну из моих ужасных сестер."
            "A. Друсилла":
                return 0
            "B. Эльза":
                return 0
            "C. Адриенна":
                return 1
            "D. Корделия":
                return 1
    if QuizOrder[Count2] == 10:
        menu:
            ch_e "В какой школе Лиги Плюща я раньше преподавала?"
            "A. Общественный Колледж Дирфилда":
                return 0
            "B. Принстон":
                return 0
            "C. Университет Эмпайр Стейт":
                return 0
            "D. Массачусетская Академия":
                return 1

 #remove this once I have enough questions
    "Она задает вопрос и вы правильно на него отвечаете."
    return 1

# Laura Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_Quiz_Question:
    if QuizOrder[Count2] == 1:
        menu:
            ch_l "Я не знаю. . . какого цвета у меня глаза?"
            "A. Голубые":
                return 0
            "B. Зеленые":
                return 1
            "C. Карие":
                return 0
            "D. Красные":
                return 0
    if QuizOrder[Count2] == 2:
        $ LauraX.FaceChange("perplexed",1,Eyes="side")
        ch_l "Эм. . ."
        $ LauraX.FaceChange("sly")
        menu:
            ch_l "Назови мое имя."
            "A. [LauraX.Pet]":
                ch_l "Довольно близко."
                return 1
            "B. Эсме":
                return 0
            "C. Лора":
                return 1
            "D. . . .":
                return 0
    if QuizOrder[Count2] == 3:
        menu:
            ch_l "Что ты думаешь о моей попе?"
            "A. Плоская?":
                return 0
            "B. Упругая?":
                return 1
            "C. Знойная?":
                return 1
            "D. Я не знаю?":
                return 0

    if QuizOrder[Count2] == 4:
        menu:
            ch_l "О каком номере я думаю?"
            "A. 23?":
                $ LauraX.FaceChange("surprised")
                if not Player.Male:
                    ch_l "Как ты догадалась?"
                else:
                    ch_l "Как ты догадался?"
                $ LauraX.FaceChange("sly")
                return 1
            "B. 2?":
                $ LauraX.FaceChange("sly")
                ch_l "Мммм, ты и я?"
                return 1
            "C. 8?":
                $ LauraX.FaceChange("perplexed")
                if not Player.Male:
                    ch_l ". . . Что? Откуда вообще ты его взяла?"
                else:
                    ch_l ". . . Что? Откуда вообще ты его взял?"
                $ LauraX.FaceChange("bemused")
                return 0
            "D. О зеленом?":
                ch_l ". . ."
                return 0
#    if QuizOrder[Count2] == 5:
#        menu:
#            ch_l "Do you know who built them?"
#            "A. Arcade":
#                return 0
#            "B. Bolivar Trask":
#                return 1
#            "C. Magneto":
#                return 0
#            "D. Unus the Untouchable":
#                return 0
#    if QuizOrder[Count2] == 6:
#        ch_l "Y'know, we didn't always have classes here at the Institute."
#        ch_l "For a while, all the students here went to a local public school."
#        menu:
#            ch_l "Know which one?"
#            "A. Bayville High School":
#                return 1
#            "B. King Memorial High School":
#                return 0
#            "C. Riverside High School":
#                return 0
#            "D. Seth Paine High School":
#                return 0
#    if QuizOrder[Count2] == 7:
#        menu:
#            ch_l "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
#            "A. Jean Grey":
#                return 0
#            "B. Lance Alvers":
#                return 1
#            "C. Mystique":
#                return 0
#            "D. Professor Xavier":
#                return 0
#    if QuizOrder[Count2] == 8:
#        ch_l "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation."
#        ch_l "Even though it was a lot of fun, we ended up disbanding after that."
#        menu:
#            ch_l "Anyway, know what the name we chose for the group was?"
#            "A. The Bayville Avengers":
#                return 0
#            "B. The Bayville Brawlers":
#                return 0
#            "C. The Bayville Harpies":
#                return 0
#            "D. The Bayville Sirens":
#                return 1
#    if QuizOrder[Count2] == 9:
#        menu:
#            ch_l "Okay[LauraX.like]..not that I'd know, but do you know the remedy for stink bomb aroma?"
#            "A. A hot shower":
#                return 0
#            "B. Methyl Ethyl Ketone":
#                return 0
#            "C. Isolation":
#                return 1
#            "D. Tomato Juice":
#                return 0
#    if QuizOrder[Count2] == 10:
#        ch_l "When I'm using my powers, I'm not[LauraX.like]{i}totally{/i} invulnerable."
#        menu:
#            ch_l "Who has powers that can still affect me?"
#            "A. Blob":
#                return 0
#            "B. Magneto":
#                return 0
#            "C. Quicksilver":
#                return 0
#            "D. Scarlet Witch":
#                return 1

 #remove this once I have enough questions
    ch_l ". . . Я ничего не могу придумать."
    return 1



# Jean Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jean_Quiz_Question:
    if QuizOrder[Count2] == 1:
        menu:
            ch_j "Я не знаю. . . какого цвета у меня глаза?"
            "A. Голубые":
                return 0
            "B. Зеленые":
                return 1
            "C. Карие":
                return 0
            "D. Красные":
                return 0
    if QuizOrder[Count2] == 2:
        $ JeanX.FaceChange("perplexed",1,Eyes="side")
        ch_j "Эм. . ."
        $ JeanX.FaceChange("sly")
        menu:
            ch_j "Назови мое имя."
            "A. [JeanX.Pet]":
                ch_j "Довольно близко."
                return 1
            "B. Эсме":
                return 0
            "C. Джин":
                return 1
            "D. . . .":
                return 0
    if QuizOrder[Count2] == 3:
        menu:
            ch_j "Что ты думаешь о моей попе?"
            "A. Плоская?":
                return 0
            "B. Упругая?":
                return 1
            "C. Знойная?":
                return 1
            "D. Я не знаю?":
                return 0

    if QuizOrder[Count2] == 4:
        menu:
            ch_j "О каком номере я думаю?"
            "A. 3?":
                $ JeanX.FaceChange("surprised")
                ch_j "Нет?"
                $ JeanX.FaceChange("sly")
                return 0
            "B. 2?":
                $ JeanX.FaceChange("sly")
                ch_j "Мммм, ты и я?"
                return 1
            "C. 8?":
                $ JeanX.FaceChange("perplexed")
                if not Player.Male:
                    ch_j ". . . Что? Откуда вообще ты его взяла?"
                else:
                    ch_j ". . . Что? Откуда вообще ты его взял?"
                $ JeanX.FaceChange("bemused")
                return 0
            "D. О зеленом?":
                ch_j ". . ."
                return 0
#    if QuizOrder[Count2] == 5:
#        menu:
#            ch_j "Do you know who built them?"
#            "A. Arcade":
#                return 0
#            "B. Bolivar Trask":
#                return 1
#            "C. Magneto":
#                return 0
#            "D. Unus the Untouchable":
#                return 0
#    if QuizOrder[Count2] == 6:
#        ch_j "Y'know, we didn't always have classes here at the Institute."
#        ch_j "For a while, all the students here went to a local public school."
#        menu:
#            ch_j "Know which one?"
#            "A. Bayville High School":
#                return 1
#            "B. King Memorial High School":
#                return 0
#            "C. Riverside High School":
#                return 0
#            "D. Seth Paine High School":
#                return 0
#    if QuizOrder[Count2] == 7:
#        menu:
#            ch_j "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
#            "A. Jean Grey":
#                return 0
#            "B. Lance Alvers":
#                return 1
#            "C. Mystique":
#                return 0
#            "D. Professor Xavier":
#                return 0
#    if QuizOrder[Count2] == 8:
#        ch_j "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation."
#        ch_j "Even though it was a lot of fun, we ended up disbanding after that."
#        menu:
#            ch_j "Anyway, know what the name we chose for the group was?"
#            "A. The Bayville Avengers":
#                return 0
#            "B. The Bayville Brawlers":
#                return 0
#            "C. The Bayville Harpies":
#                return 0
#            "D. The Bayville Sirens":
#                return 1
#    if QuizOrder[Count2] == 9:
#        menu:
#            ch_j "Okay[JeanX.like]..not that I'd know, but do you know the remedy for stink bomb aroma?"
#            "A. A hot shower":
#                return 0
#            "B. Methyl Ethyl Ketone":
#                return 0
#            "C. Isolation":
#                return 1
#            "D. Tomato Juice":
#                return 0
#    if QuizOrder[Count2] == 10:
#        ch_j "When I'm using my powers, I'm not[JeanX.like]{i}totally{/i} invulnerable."
#        menu:
#            ch_j "Who has powers that can still affect me?"
#            "A. Blob":
#                return 0
#            "B. Magneto":
#                return 0
#            "C. Quicksilver":
#                return 0
#            "D. Scarlet Witch":
#                return 1

 #remove this once I have enough questions
    ch_j ". . . Я ничего не могу придумать."
    return 1

label Storm_Quiz_Question:
    if QuizOrder[Count2] == 1:
        menu:
            ch_s "Итак, какого цвета мои глаза?"
            "A. Голубые":
                return 1
            "B. Зеленые":
                return 0
            "C. Карие":
                return 0
            "D. Белые?":
                ch_s ". . . иногда."
                return 1
    if QuizOrder[Count2] == 2:
        menu:
            ch_s "Где я родилась?"
            "A. Кения":
                return 0
            "B. Нью-Йорк":
                return 1
            "C. Египет":
                return 0
            "D. Гонолулу":
                return 0
    if QuizOrder[Count2] == 3:
        menu:
            ch_s "Что ты думаешь о моем теле?"
            "A. Ты плоская?":
                $ StormX.FaceChange("confused")
                return 0
            "B. Ты плотная?":
                $ Party[0].Statup("Love", 80, 2)
                $ Party[0].Statup("Inbt", 80, 2)
                return 1
            "C. Ты знойная?":
                return 1
            "D. Я не знаю?":
                ch_s "Ожидаемая реакция."
                return 1

    if QuizOrder[Count2] == 4:
        menu:
            ch_j "В каком городе я была воровкой?"
            "A. Детройт?":
                return 0
            "B. Рим?":
                return 0
            "C. Нью-Йорк?":
                return 0
            "D. Каир?":
                return 1
#    if QuizOrder[Count2] == 5:
#        menu:
#            ch_j "Do you know who built them?"
#            "A. Arcade":
#                return 0
#            "B. Bolivar Trask":
#                return 1
#            "C. Magneto":
#                return 0
#            "D. Unus the Untouchable":
#                return 0
#    if QuizOrder[Count2] == 6:
#        ch_j "Y'know, we didn't always have classes here at the Institute."
#        ch_j "For a while, all the students here went to a local public school."
#        menu:
#            ch_j "Know which one?"
#            "A. Bayville High School":
#                return 1
#            "B. King Memorial High School":
#                return 0
#            "C. Riverside High School":
#                return 0
#            "D. Seth Paine High School":
#                return 0
#    if QuizOrder[Count2] == 7:
#        menu:
#            ch_j "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
#            "A. Jean Grey":
#                return 0
#            "B. Lance Alvers":
#                return 1
#            "C. Mystique":
#                return 0
#            "D. Professor Xavier":
#                return 0
#    if QuizOrder[Count2] == 8:
#        ch_j "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation."
#        ch_j "Even though it was a lot of fun, we ended up disbanding after that."
#        menu:
#            ch_j "Anyway, know what the name we chose for the group was?"
#            "A. The Bayville Avengers":
#                return 0
#            "B. The Bayville Brawlers":
#                return 0
#            "C. The Bayville Harpies":
#                return 0
#            "D. The Bayville Sirens":
#                return 1
#    if QuizOrder[Count2] == 9:
#        menu:
#            ch_j "Okay[JeanX.like]..not that I'd know, but do you know the remedy for stink bomb aroma?"
#            "A. A hot shower":
#                return 0
#            "B. Methyl Ethyl Ketone":
#                return 0
#            "C. Isolation":
#                return 1
#            "D. Tomato Juice":
#                return 0
#    if QuizOrder[Count2] == 10:
#        ch_j "When I'm using my powers, I'm not[JeanX.like]{i}totally{/i} invulnerable."
#        menu:
#            ch_j "Who has powers that can still affect me?"
#            "A. Blob":
#                return 0
#            "B. Magneto":
#                return 0
#            "C. Quicksilver":
#                return 0
#            "D. Scarlet Witch":
#                return 1

 #remove this once I have enough questions
    "Она задает вопрос и вы правильно на него отвечаете."
    return 1


# Jubes Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_Quiz_Question:
    if QuizOrder[Count2] == 1:
        menu:
            ch_v "Где я выросла?"
            "A. Гонконг":
                ch_v "Мои -родители,- возможно. . ."
                return 0
            "B. Беверли-Хиллз":
                return 1
            "C. Шэньчжэнь":
                return 0
            "D. Бел Эйр":
                ch_v "Близко. . ."
                return 0
    if QuizOrder[Count2] == 2:
        menu:
            ch_v "Какое мое полное имя?"
            "A. Джубилейшен":
                if JubesX.Name == "Джубилейшен":
                        ch_v "Ладно, это было слишком просто."
                return 1
            "B. Джубал":
                return 0
            "C. Джубилант":
                return 0
            "D. Джаброни":
                ch_v ". . . нет."
                return 0
    if QuizOrder[Count2] == 3:
        menu:
            ch_v "Где я жила после потери родителей?"
            "A. С твоим дядей Брюсом":
                return 0
            "B. В заброшенном здании":
                return 0
            "C. В пещере":
                ch_v "No, the vampire thing came later."
                return 0
            "D. В торговом центре":
                return 1

    if QuizOrder[Count2] == 4:
        menu:
            ch_v "Каким видом спорта я занималась в детстве?"
            "A. Бейсболом":
                $ JubesX.FaceChange("surprised")
                ch_v "Ладно, возможно, я дала несколько неверных подсказок?"
                $ JubesX.FaceChange("sly")
                return 0
            "B. Фигурным катанием":
                return 0
            "C. Гимнастикой":
                ch_v "Да, все так. . ."
                ch_v "Я до сих пор достаточно гибка. . ."
                return 1
            "D. Метанием ядра":
                ch_v ". . ."
                return 0

 #remove this once I have enough questions
    "Она задает вам еще несколько каверзных вопросов, но вам удается ответить на них правильно."
    return 1


label Gwen_Quiz_Question:
    if QuizOrder[Count2] == 1:
        menu:
            ch_g "Откуда я родом?"
            "A. Из \"реального мира?\"":
                $ GwenX.Statup("Love", 90, 2)
                ch_g "Ага!"
                return 1
            "B. Квинс, Нью Йорк?":
                ch_g "Не правильно, \"Гвен\". . ."
                return 0
            "C. Из какого-то другого измерения?":
                ch_g "Ну, довольно близко. . ."
                return 1
            "D. Канада?":
                ch_g "Неправильно, \"Пул\"."
                return 0
    if QuizOrder[Count2] == 2:
        menu:
            ch_g "Какое мое полное имя?"
            "A. Гвенгвин":
                if "Gwenguin" not in GwenX.Names:
                        ch_g "Что?"
                        ch_g ". . ."
                        $ GwenX.Statup("Love", 90, 5)
                        ch_g "А вообще довольно круто звучит. . ."
                        $ GwenX.Names.append("Gwenguin")
                else:
                        ch_g "Ха, нет, это скорее прозвище."
                return 0
            "B. Гвенивер":
                return 0
            "C. Гвендолин":
                if GwenX.Name == "Гвендолин":
                        ch_g "Ладно, это было слишком просто."
                return 1
            "D. Гвеннифер":
                ch_g ". . . нет."
                return 0
    if QuizOrder[Count2] == 3:
        menu:
            ch_g "Какая у меня фамилия?"
            "A. Пул [[Pool]":
                return 0
            "B. Стейси":
                $ GwenX.Statup("Love", 80, -2)
                ch_g "Почему люди продолжают ошибаться в этом вопросе?!"
                return 0
            "C. Пэлтроу":
                ch_g "Что? Даже не близко!"
                return 0
            "D. Пул [[Poole]":
                return 1

    if QuizOrder[Count2] == 4:
        menu:
            ch_g "Какой была моя первая работа, когда я оказалась в 616?"
            "A. Спорт!":
                return 0
            "B. Кондитер":
                return 0
            "C. Наемник":
                if not Player.Male:
                    ch_g "Агась! +1 очко этой госпоже."
                else:
                    ch_g "Агась! +1 очко этому господину."
                return 1
            "D. Супергерой":
                ch_g ". . ."
                ch_g "Ну. . . я пыталась. . ."
                return 0

    if QuizOrder[Count2] == 5:
        menu:
            ch_g "Кто был моим наставником по боевому искусству?"
            "A. Мистер Мияги":
                return 0
            "B. Дэдпул":
                ch_g "Нет!"
                return 0
            "C. Шан-Чи":
                return 0
            "D. Батрок":
                ch_g "Агась, он научил меня всему, что я знаю о бое!"
                return 1

 #remove this once I have enough questions
    "Она задает вам еще несколько каверзных вопросов, но вам удается ответить на них правильно."
    return 1


label Betsy_Quiz_Question:
#    if QuizOrder[Count2] == 1:
#        menu:
#            ch_b "Where did I originaly come from?"
#            "A. The \"real world?\"":
#                $ GwenX.Statup("Love", 90, 2)
#                ch_b "Yeah!"
#                return 1
#            "B. Queens, NY?":
#                ch_b "Wrong \"Gwen\". . ."
#                return 0
#            "C. Some other dimension?":
#                ch_b "Eh, close enough. . ."
#                return 1
#            "D. Canada?":
#                ch_b "Wrong 'pool."
#                return 0
#    if QuizOrder[Count2] == 2:
#        menu:
#            ch_b "What is my full first name?"
#            "A. Gwenguin":
#                if "Gwenguin" not in GwenX.Names:
#                        ch_b "What?"
#                        ch_b ". . ."
#                        $ GwenX.Statup("Love", 90, 5)
#                        ch_b "That's actually kinda cool. . ."
#                        $ GwenX.Names.append("Gwenguin")
#                else:
#                        ch_b "Heh, no, that's more of a nickname."
#                return 0
#            "B. Guinevere":
#                return 0
#            "C. Gwendolyne":
#                if GwenX.Name == "Gwendolyne":
#                        ch_b "Ok, that one was too easy."
#                return 1
#            "D. Gwennefer":
#                ch_b ". . . no."
#                return 0
#    if QuizOrder[Count2] == 3:
#        menu:
#            ch_b "What's my -last- name?"
#            "A. Pool":
#                return 0
#            "B. Stacy":
#                $ GwenX.Statup("Love", 80, -2)
#                ch_b "Why do people keep getting that one wrong?!"
#                return 0
#            "C. Paltrow":
#                ch_b "What? Not even close!"
#                return 0
#            "D. Poole":
#                return 1

#    if QuizOrder[Count2] == 4:
#        menu:
#            ch_b "What was my first job when I found myself in the 616?"
#            "A. Sports!":
#                return 0
#            "B. Patissier":
#                return 0
#            "C. Mercenary":
#                ch_b "Yup! Gotta make that bank!"
#                return 1
#            "D. Superhero":
#                ch_b ". . ."
#                ch_b "I mean. . . I tried. . ."
#                return 0

#    if QuizOrder[Count2] == 5:
#        menu:
#            ch_b "Who was my mentor in combat?"
#            "A. Mr. Miyagi":
#                return 0
#            "B. Deadpool":
#                ch_b "No!"
#                return 0
#            "C. Shang-Chi":
#                return 0
#            "D. Batroc":
#                ch_b "Yup, taught me everything I know about fighting!"
#                return 1

 #remove this once I have enough questions
    "Она задает вам еще несколько каверзных вопросов, но вам удается ответить на них правильно."
    return 1
# End of  Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Doreen_Quiz_Question:
#    if QuizOrder[Count2] == 1:
#        menu:
#            ch_b "Where did I originaly come from?"
#            "A. The \"real world?\"":
#                $ GwenX.Statup("Love", 90, 2)
#                ch_b "Yeah!"
#                return 1
#            "B. Queens, NY?":
#                ch_b "Wrong \"Gwen\". . ."
#                return 0
#            "C. Some other dimension?":
#                ch_b "Eh, close enough. . ."
#                return 1
#            "D. Canada?":
#                ch_b "Wrong 'pool."
#                return 0
#    if QuizOrder[Count2] == 2:
#        menu:
#            ch_b "What is my full first name?"
#            "A. Gwenguin":
#                if "Gwenguin" not in GwenX.Names:
#                        ch_b "What?"
#                        ch_b ". . ."
#                        $ GwenX.Statup("Love", 90, 5)
#                        ch_b "That's actually kinda cool. . ."
#                        $ GwenX.Names.append("Gwenguin")
#                else:
#                        ch_b "Heh, no, that's more of a nickname."
#                return 0
#            "B. Guinevere":
#                return 0
#            "C. Gwendolyne":
#                if GwenX.Name == "Gwendolyne":
#                        ch_b "Ok, that one was too easy."
#                return 1
#            "D. Gwennefer":
#                ch_b ". . . no."
#                return 0
#    if QuizOrder[Count2] == 3:
#        menu:
#            ch_b "What's my -last- name?"
#            "A. Pool":
#                return 0
#            "B. Stacy":
#                $ GwenX.Statup("Love", 80, -2)
#                ch_b "Why do people keep getting that one wrong?!"
#                return 0
#            "C. Paltrow":
#                ch_b "What? Not even close!"
#                return 0
#            "D. Poole":
#                return 1

#    if QuizOrder[Count2] == 4:
#        menu:
#            ch_b "What was my first job when I found myself in the 616?"
#            "A. Sports!":
#                return 0
#            "B. Patissier":
#                return 0
#            "C. Mercenary":
#                ch_b "Yup! Gotta make that bank!"
#                return 1
#            "D. Superhero":
#                ch_b ". . ."
#                ch_b "I mean. . . I tried. . ."
#                return 0

#    if QuizOrder[Count2] == 5:
#        menu:
#            ch_b "Who was my mentor in combat?"
#            "A. Mr. Miyagi":
#                return 0
#            "B. Deadpool":
#                ch_b "No!"
#                return 0
#            "C. Shang-Chi":
#                return 0
#            "D. Batroc":
#                ch_b "Yup, taught me everything I know about fighting!"
#                return 1

label Wanda_Quiz_Question:

 #remove this once I have enough questions
    "Она задает вам еще несколько каверзных вопросов, но вам удается ответить на них правильно."
    return 1
# End of  Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Emma Intro / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_StripStudy_Intro:
    if Party[0] != EmmaX:
            $ Party.reverse()
    call Shift_Focus(Party[0])
    if len(Party) >= 2 and Second == Party[0]:
            $ Second = Party[1]
    if not EmmaX.Over and not EmmaX.Legs:
            #if she's mostly naked, cheat
            $ EmmaX.FaceChange("sly")
            ch_e "Я рассматривала возможность. . . как-нибудь промотивировать тебя. . ."
            $ EmmaX.Eyes = "down"
            ch_e "но, я полагаю, мы уже прошли через это. . ."
            $ EmmaX.Eyes = "squint"
            ch_e "У тебя есть какие-нибудь предложения?"
            call SexMenu # Emma_SexMenu
    else:
            "[EmmaX.Name] придвигается немного ближе к вам. . ."
            ch_e "Мне любопытно, [EmmaX.Petname]. . ."
            ch_e "Как думаешь, небольшая \"мотивация\" может увеличить твою тягу к знаниям?"
            if "stripstudy" not in EmmaX.History:
                menu:
                    extend ""
                    "Какого рода мотивация?":
                        if "frisky" not in EmmaX.History:
                            $ EmmaX.FaceChange("sly")
                            $ Line = "ask"
                        else:
                            $ EmmaX.Statup("Obed", 80, 3)
                            $ EmmaX.FaceChange("confused",1)
                            "Она теребит края своей одежды."
                            ch_e "Ты ведь не заставишь меня это сказать, правда. . .?"
                            menu:
                                extend ""
                                "Эм. . . ох, ОГО! Да, звучит неплохо. [[Стрип-обучение]":
                                            $ Line = "strip"
                                "Похоже, у меня нет другого выбора. . .":
                                    if ApprovalCheck(EmmaX, 500, "O"):
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            $ EmmaX.Statup("Inbt", 50, 5)
                                            $ EmmaX.FaceChange("sly", 2)
                                            $ Line = "ask"
                                    elif ApprovalCheck(EmmaX, 500, "LO"):
                                            $ EmmaX.FaceChange("confused", 2)
                                            $ EmmaX.Statup("Love", 70, -5)
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            ch_e "Очень хорошо. . ."
                                            $ Line = "ask"
                                    else:
                                            $ EmmaX.Statup("Love", 200, -5)
                                            $ EmmaX.Statup("Inbt", 50, -5)
                                            $ EmmaX.FaceChange("angry", 1)
                                            ch_e "Ох, тогда не бери в голову."
                                ". . .":
                                    if ApprovalCheck(EmmaX, 400, "O"):
                                            $ EmmaX.FaceChange("confused", 2)
                                            $ EmmaX.Statup("Inbt", 50, 5)
                                            $ Line = "ask"
                                    elif ApprovalCheck(EmmaX, 500, "LO"):
                                            $ EmmaX.FaceChange("confused", 1, Brows="angry")
                                            $ EmmaX.Statup("Obed", 50, 5)
                                            $ EmmaX.Statup("Inbt", 50, 5)
                                            $ Line = "ask"
                                    else:
                                            $ EmmaX.Statup("Love", 200, -5)
                                            $ EmmaX.Statup("Inbt", 50, -5)
                                            $ EmmaX.FaceChange("angry", 1)
                                            ch_e "Oh, never mind then."

                    "Думаю, может и помочь." if "frisky" in EmmaX.History:
                            $ EmmaX.FaceChange("sly")
                            $ EmmaX.Statup("Love", 80, 5)
                            $ EmmaX.Statup("Obed", 80, 3)
                            $ EmmaX.Statup("Inbt", 50, 5)
                            ch_e "Я надеялась, что ты ответишь именно так. . ."
                            $ Line = "strip"
                    "Нет, я и так справлюсь.":
                            $ EmmaX.FaceChange("confused", Eyes="side")
                            if "frisky" in EmmaX.History:
                                    $ EmmaX.Statup("Love", 200, -10)
                                    $ EmmaX.Statup("Obed", 80, 5)
                                    $ EmmaX.Statup("Inbt", 50, -5)
                            else:
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Inbt", 50, -5)
                            ch_e "Ох. . . ну тогда я рада за тебя."
                            $ EmmaX.FaceChange("confused")
                if Line == "ask":
                    ch_e "Что ж, я могла бы поспрашивать тебя по психологии мутантов. . ."
                    $ EmmaX.Eyes = "side"
                    ch_e "и, возможно, если ты будешь правильно отвечать. . ."
                    $ EmmaX.Eyes = "squint"
                    ch_e "Я буду. . ."
                    menu:
                        extend ""
                        ". . . снимать одежду?":
                                $ EmmaX.Statup("Inbt", 50, 5)
                                ch_e "Да."
                                $ Line = "strip"
                        "Да? . .":
                                if ApprovalCheck(EmmaX, 500, "O"):
                                    $ EmmaX.FaceChange("confused", 2)
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.Statup("Love", 200, -5)
                                            $ EmmaX.Statup("Obed", 80, 10)
                                    else:
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)
                                    $ Line = "ask"
                                elif ApprovalCheck(EmmaX, 500, "LO"):
                                    $ EmmaX.FaceChange("confused", 1, Brows="angry")
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.Statup("Love", 200, -5)
                                            $ EmmaX.Statup("Obed", 80, 5)
                                    else:
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)
                                    $ Line = "ask"
                        ". . .":
                                if ApprovalCheck(EmmaX, 500, "O"):
                                    $ EmmaX.FaceChange("confused", 2)
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.Statup("Obed", 50, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)
                                    else:
                                            $ EmmaX.Statup("Obed", 50, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)
                                    $ Line = "ask"
                                elif ApprovalCheck(EmmaX, 500, "LO"):
                                    $ EmmaX.FaceChange("confused", 1, Brows="angry")
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.Statup("Love", 200, -5)
                                            $ EmmaX.Statup("Obed", 50, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)
                                    else:
                                            $ EmmaX.Statup("Obed", 50, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)
                                    $ Line = "ask"
                    if Line == "ask":
                                    $ EmmaX.FaceChange("bemused", Eyes="side")
                                    ch_e "Снимать что-нибудь из одежды. . ."
                                    $ Line = "strip"
                    $ EmmaX.FaceChange("sly", Brows="confused")
                    menu:
                        ch_e "Такое тебя заинтересует?"
                        "Определенно!":
                            $ EmmaX.FaceChange("sly",Mouth="smile")
                            $ EmmaX.Statup("Love", 50, 5)
                            $ EmmaX.Statup("Love", 80, 5)
                            $ EmmaX.Statup("Inbt", 50, 5)
                        "Ага.":
                            $ EmmaX.FaceChange("sly")
                            $ EmmaX.Statup("Love", 80, 3)
                            $ EmmaX.Statup("Obed", 50, 3)
                            $ EmmaX.Statup("Inbt", 50, 3)
                        "Нет, спасибо.":
                            if "frisky" in EmmaX.History:
                                    $ EmmaX.Statup("Love", 200, -10)
                                    $ EmmaX.Statup("Obed", 80, 10)
                                    $ EmmaX.Statup("Inbt", 50, -5)
                            else:
                                    $ EmmaX.Statup("Love", 200, -5)
                                    $ EmmaX.Statup("Obed", 80, 5)
                                    $ EmmaX.Statup("Inbt", 50, -5)
                            $ EmmaX.FaceChange("angry")
                            ch_e "Хмм."
                            $ Line = "no"

            if Line == "strip":
                    $ EmmaX.FaceChange("sly", 0)
                    if len(Party) >= 2:
                        ch_e "А ты, [Party[1].Name]? Хочешь поучаствовать?"
                        call Date_Sex_Break(EmmaX,Party[1])
                        if _return == 4:
                                #you stop it because of the other girl
                                ch_e "Что ж, полагаю, мы можем. . . это отложить."
                                return
                        elif _return == 3:
                                #the other girl is mad
                                ch_e "Ну, думаю это можно принять за ответ."
                                $ Cnt = 3
                        elif _return == 2:
                                #the other girl will watch
                                ch_e "Полагаю, тогда ты можешь просто наблюдать. . ."
                                $ Cnt = 3
                        elif _return == 1 and len(Party) >= 2:
                                if Party[1] == RogueX:
                                    ch_r "Думаю, я могла бы присоединиться."
                                elif Party[1] == KittyX:
                                    ch_k "Это может быть весело. . ."
                                elif Party[1] == LauraX:
                                    ch_l "Ага, ладно. . ."
                    return 1
            else:
                    return 0
    return 0
# End Emma_Strip_Study Intro / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
