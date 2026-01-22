label Sleepover(Line = 0,BO=[]): #rkeljsvgbdw
            # This event gets called from Round10
            # If there's a Lead, she's been sent to this from elsewhere
            # Sleep tracks number of previous sleepovers

            if bg_current not in PersonalRooms: #sends you home if you're in a public space
                    "Уже слишком поздно, пора спать."
                    $ bg_current = "bg player"
                    jump Misplaced

            $ Party = []

            $ BO = TotalGirls[:]
            while BO:
                    if BO[0].Loc == bg_current:
                            $ Party.append(BO[0])
                    $ BO.remove(BO[0])


            # Modification mode
            if bg_current == "bg player" and Day >=9 and "met" not in JubesX.History and not Party and JubesX.Delay == 0:
                call CleartheRoom ("All", 1, 0)
                menu:
                    "Хотите познакомиться с Джубили сегодня ночью?"
                    "Да":
                        call Jubes_Meet
                    "Возможно, завтра":
                        $ JubesX.Delay += 1
                        pass
                    "Возможно, на следующей неделе":
                        $ JubesX.Delay += 7
                        pass
                "Уже поздно, так что вы идете спать."
                call Wait
                return

            if not Party and bg_current == "bg player":
                    #if nobody is around.
                    call CleartheRoom("All",1)
                    #if nobody is here, you just go to sleep
                    "Уже поздно, так что вы идете спать."
                    if "met" not in JubesX.History and JubesX.Delay == 0 and Day >= 9:
                        menu:
                            "Хотите познакомиться с Джубили сегодня ночью?"
                            "Да":
                                call Jubes_Meet
                            "Возможно, завтра":
                                $ JubesX.Delay += 1
                                pass
                            "Возможно, на следующей неделе":
                                $ JubesX.Delay += 7
                                pass
                    call Wait
                    return
            # -----------------

            while len(Party) > 2:
                    #culls out extra members
                    $ Party.remove(Party[2])

            if Day <= 4: #was at 7
                    # prevents anyone agreeing before day 7.
                    $ Party = []
            elif Party and Party[0]:
                    call Shift_Focus(Party[0])

            if bg_current != "bg player":
                    #if this isn't your room, sets "room" to the name of the room's owner
                    $ BO = TotalGirls[:]
                    while BO:
                            if BO[0].Home == bg_current:
                                    if BO[0] not in Party:
                                            #either another girl is around
                                            "Наверное, [BO[0].Name] будет не в восторге, если вы останетесь здесь, вы возвращаетесь в свою комнату."
                                            call Remove_Girl("All")
                                            jump Return_Player
                                    if BO[0] is not Party[0]:
                                            $ Party.reverse() #makes sure the room's owner is first
                                    $ BO = [1]
                            $ BO.remove(BO[0])

            # the previous statement should cull out all situations where the owner isn't there
            if bg_current == "bg player":
                    if len(Party) == 2:
                        $ renpy.random.shuffle(Party)
                        if ApprovalCheck(Party[0],Check=1) <= ApprovalCheck(Party[1],Check=1):
                            # If second one likes you more, pick her
                            $ Party.reverse()
                    if not Party:
                        pass
                    elif Party[0].Sleep >= 3 and ApprovalCheck(Party[0], 800):
                        pass
                    elif Party[0] is RogueX:
                            ch_r "Уже поздно, я немного устала."
                    elif Party[0] is KittyX:
                            ch_k "Уже поздно, думаю, мне пора. . ."
                    elif Party[0] is EmmaX:
                            ch_e "Уже поздно, я устала. . ."
                    elif Party[0] is LauraX:
                            ch_l "Мне надо немного поспать. . ."
                    elif Party[0] is JeanX:
                            ch_j "Я спать. . ."
                    elif Party[0] is StormX:
                            ch_s "Уже поздно, мне пора. . ."
                    elif Party[0] is JubesX:
                            ch_v "Ну, уже довольно поздно, тебе нужно поспать. . ."
                    elif Party[0] is GwenX:
                            ch_g "*Зевает*. . . ну, пора на боковую. . ."
                    elif Party[0] is BetsyX:
                            ch_b "Боюсь, что уже довольно поздно. . ."
                    elif Party[0] is DoreenX:
                            ch_d "Уже довольно поздно. . ."
                    elif Party[0] is WandaX:
                            ch_w "Знаешь, уже довольно поздно. . ."
            elif Party and bg_current == Party[0].Home:
                    if Party[0] is RogueX:#Room == RogueX.Name:
                            ch_r "Уже поздно, я ложусь спать."
                    elif Party[0] is KittyX:
                            ch_k "Я немного устала. . ."
                    elif Party[0] is EmmaX:
                            ch_e "Уже поздно, [EmmaX.Petname]. . ."
                    elif Party[0] is LauraX:
                            ch_l "Я устала. . ."
                    elif Party[0] is JeanX:
                            ch_j "Я спать. . ."
                    elif Party[0] is StormX:
                            ch_s "Уже поздно, я бы хотела пойти лечь спать. . ."
                    elif Party[0] is JubesX:
                            ch_v "Ну, уже довольно поздно, тебе нужно поспать. . ."
                    elif Party[0] is GwenX:
                            ch_g "*Зевает*. . . ну, пора отправиться в царство морфея. . ."
                    elif Party[0] is BetsyX:
                            ch_b "*Зевает*. . . ну что ж, пора на сеновал. . ."
                    elif Party[0] is DoreenX:
                            ch_d "Уже довольно поздно, я бы хотела лечь спать. . ."
                    elif Party[0] is WandaX:
                            ch_w "Я уже собираюсь ложиться спать. . ."
            else:
                "Something went wrong."
                "Tell Oni \"[Party] - [bg_current]\""


            if Day <= 4: #was at 7
                    # If it's too early for sleepovers,
                    jump Return_Player

            if EmmaX in Party:
                    if "classcaught" not in EmmaX.History:
                            if bg_current == EmmaX.Home:
                                    ch_e "Тебе, пожалуй, пора идти, мы не должны давать поводов для сплетен."
                                    jump Return_Player
                            else:
                                    ch_e "Мне, пожалуй, пора идти, мы не должны давать поводов для сплетен."
                                    call Remove_Girl(EmmaX)
                    elif len(Party) >= 2 and "three" not in EmmaX.History:
                            #if Emma's around but can't do threesome stuff yet
                            if (bg_current == EmmaX.Home or bg_current == "bg player") and ApprovalCheck(EmmaX, 1100, "LI"):
                                if Party[0] is not EmmaX:
                                        $ Party.reverse()
                                ch_e "[Party[1].Name], дорогая, мне нужно немного побыть с [Player.Name_tvo] наедине, ты можешь идти."
                                $ Party[1].FaceChange("confused",1)
                                call AnyLine(Party[1],"Ох, ладно. . .")
                                call Remove_Girl(Party[1])
                                ch_e "Извини, но мне нужно кое-что обсудить с тобой наедине."
                            else:
                                #if it's not her room, or she doesn't like you enough to stay
                                ch_e "Да, мне, по правде говоря, пора уходить, ведите себя прилично."
                                call Remove_Girl(EmmaX)
                            if "sleeptime" not in EmmaX.History:
                                $ EmmaX.History.append("sleeptime")
                    if not Party or (EmmaX not in Party and bg_current == EmmaX.Home):
                                #if Emma leaves
                                jump Return_Player

            $ Party[0].FaceChange("sexy",1)

            $ Line = 0
            if Party[0].Sleep >= 3 and ApprovalCheck(Party[0], 800):
                    #You've slept over several times and she still likes you
                    if Party[0].Home == bg_current:
                            call AnyLine(Party[0],"Ты останешься на ночь?")
                    else:
                            call AnyLine(Party[0],"Я останусь на ночь, ты не против?")
                    $ Line = 1

            elif Party[0].Sleep < 3 and ApprovalCheck(Party[0], 1100, "LI",Bias=-200):
                    #You haven't slept over much, but she wants you to
                    $ Party[0].FaceChange("bemused",1)
                    if Party[0] is RogueX:
                            if bg_current == Party[0].Home:
                                ch_r "Я тут подумала. . . Может, ты хочешь остаться на ночь?"
                            else:
                                ch_r "Я тут подумала. . . могу я остаться на ночь?"
                    elif Party[0] is KittyX:
                            if bg_current == Party[0].Home:
                                ch_k "Так[KittyX.like]хочешь остаться на ночь?"
                            else:
                                ch_k "Так[KittyX.like]могу я остаться на ночь?"
                    elif Party[0] is EmmaX:
                            if bg_current == Party[0].Home:
                                ch_e "Мне интересно, может ты хочешь остаться на ночь?"
                            else:
                                ch_e "Мне интересно, могу ли я остаться на ночь?"
                    elif Party[0] is LauraX:
                            if bg_current == Party[0].Home:
                                ch_l "Ну как, ты останешься на ночь?"
                            else:
                                ch_l "Ну как, могу я остаться на ночь?"
                    elif Party[0] is JeanX:
                            if bg_current == Party[0].Home:
                                ch_j "Ты планируешь остаться на ночь?"
                            else:
                                ch_j "Я остаюсь, ладно?"
                    elif Party[0] is StormX:
                            if bg_current == Party[0].Home:
                                ch_s "Ты хочешь остаться на ночь?"
                            else:
                                ch_s "Ты не будешь возражать, если я переночую здесь?"
                    elif Party[0] is JubesX:
                            if bg_current == Party[0].Home:
                                ch_v "Может, ты хочешь поспать здесь?"
                            else:
                                ch_v "Может, ты хочешь, чтобы я переночевала здесь?"
                    elif Party[0] is GwenX:
                            if bg_current == Party[0].Home:
                                ch_g "Ты хочешь остаться на ночь?"
                            else:
                                ch_g "Не возражаешь, если я посплю у тебя?"
                    elif Party[0] is BetsyX:
                            if bg_current == Party[0].Home:
                                ch_b "Не желаешь остаться на ночь?"
                            else:
                                ch_b "Я тебя не побеспокою, если останусь у тебя?"
                    elif Party[0] is DoreenX:
                            if bg_current == Party[0].Home:
                                ch_d "Хочешь остаться на ночь?"
                            else:
                                ch_d "Не возражаешь, если я останусь на ночь?"
                    elif Party[0] is WandaX:
                            if bg_current == Party[0].Home:
                                ch_w "Останешься спать здесь?"
                            else:
                                ch_w "Не возражаешь, если я переночую здесь?"
                    $ Line = 1


            if Line:
                    #she offered to sleep over
                    menu:
                        extend ""
                        "Конечно.":
                                if Party[0].Sleep <= 5:
                                        $ Party[0].Statup("Love", 70, 10)
                                        $ Party[0].Statup("Obed", 80, 10)
                                        $ Party[0].Statup("Obed", 50, 20)
                                        $ Party[0].Statup("Inbt", 25, 20)
                                $ Party[0].Statup("Love", 70, 5)
                                $ Party[0].FaceChange("smile")
                                # Line = 1

                        "Извини, но нет.":
                                $ Party[0].Statup("Obed", 50, 2)
                                $ Party[0].Statup("Obed", 30, 5)
                                $ Party[0].Statup("Inbt", 40, 3)
                                $ Party[0].FaceChange("sad")
                                $ Line = 0
                                if Party[0] is RogueX:
                                        ch_r "Ладно, тогда до завтра. Спокойной."
                                elif Party[0] is KittyX:
                                        ch_k "Хорошо. . . тогда до завтра. . ."
                                elif Party[0] is EmmaX:
                                        ch_e "Ну, если ты настаиваешь. Тогда до завтра."
                                elif Party[0] is LauraX:
                                        ch_l "Ладно."
                                elif Party[0] is JeanX:
                                        ch_j "А? Ладно, как скажешь."
                                elif Party[0] is StormX:
                                        ch_s "Хорошо, тогда увидимся завтра."
                                elif Party[0] is JubesX:
                                        ch_v "Ну ладно, ладно. . . увидимся. . ."
                                elif Party[0] is GwenX:
                                        ch_g "Ох, ладно. . . Тогда увидимся завтра."
                                elif Party[0] is BetsyX:
                                        ch_b "Ох, ну хорошо. Увидимся завтра. . ."
                                elif Party[0] is DoreenX:
                                        ch_d "Оу, ну ладно. . ."
                                elif Party[0] is WandaX:
                                        ch_w "Ладно, до завтра. . ."
            else:
                    #if she didn't offer to sleep over
                    if Party[0] is RogueX:
                            if bg_current == Party[0].Home:
                                ch_r "Тебе пора идти."
                            else:
                                ch_r "Я ухожу, увидимся завтра."
                    elif Party[0] is KittyX:
                            if bg_current == Party[0].Home:
                                ch_k "Тебе следует[KittyX.like]уйти."
                            else:
                                ch_k "До завтра, [KittyX.Petname]."
                    elif Party[0] is EmmaX:
                            if bg_current == Party[0].Home:
                                if not Player.Male:
                                    ch_e "Не могла бы ты покинуть комнату?"
                                else:
                                    ch_e "Не мог бы ты покинуть комнату?"
                            else:
                                ch_e "Мне нужно идти."
                    elif Party[0] is LauraX:
                            if bg_current == Party[0].Home:
                                ch_l "Уходи."
                            else:
                                ch_l "Ну, увидимся."
                    elif Party[0] is JeanX:
                            if bg_current == Party[0].Home:
                                ch_l "Уходи."
                            #else:
                                #ch_j "I'm crashing here, ok?"
                    elif Party[0] is StormX:
                            if bg_current == Party[0].Home:
                                if not Player.Male:
                                    ch_s "Не могла бы ты оставить меня одну?"
                                else:
                                    ch_s "Не мог бы ты оставить меня одну?"
                            else:
                                ch_s "Увидимся завтра."
                    elif Party[0] is JubesX:
                            if bg_current == Party[0].Home:
                                ch_v "У меня есть кое-какие дела, так что, думаю, тебе пора идти."
                            else:
                                ch_v "У меня есть кое-какие дела, так что мне пора идти."
                    elif Party[0] is GwenX:
                            if bg_current == Party[0].Home:
                                if not Player.Male:
                                    ch_g "Ладно. . . не могла бы ты тогда уйти?"
                                else:
                                    ch_g "Ладно. . . не мог бы ты тогда уйти?"
                            else:
                                ch_g "Ну, я, пожалуй, пойду. . ."
                    elif Party[0] is BetsyX:
                            if bg_current == Party[0].Home:
                                if not Player.Male:
                                    ch_b "Не могла бы ты уйти?"
                                else:
                                    ch_b "Не мог бы ты уйти?"
                            else:
                                ch_b "Пожалуй, мне следует уйти."
                    elif Party[0] is DoreenX:
                            if bg_current == Party[0].Home:
                                ch_d "Эм, можешь покинуть комнату?"
                            else:
                                ch_d "Думаю, мне пора. . ."
                    elif Party[0] is WandaX:
                            if bg_current == Party[0].Home:
                                if not Player.Male:
                                    ch_w "Слушай. . . не могла бы ты уже уйти?"
                                else:
                                    ch_w "Слушай. . . не мог бы ты уже уйти?"
                            else:
                                ch_w "Слушай. . . мне пора идти."

                    menu:
                        extend ""
                        "Ладно, я пойду. Спокойной ночи." if Party[0].Home == bg_current:
                                #if she didn't agree and this is her room
                                $ Line = "leave"
                        "Ладно, увидимся. Спокойной ночи." if Party[0].Home != bg_current:
                                #if she didn't agree and this is not her room
                                $ Line = "leave"

                        "Уверена, что я не могу остаться на ночь? . ." if not Party[0].Sleep and Party[0].Home == bg_current:
                                $ Line = "please"
                        "Уверена, что не хочешь остаться на ночь? . ." if not Party[0].Sleep and Party[0].Home != bg_current:
                                $ Line = "please"

                        "Эх, а той ночью ты говорила иначе . ." if Party[0].Sleep:
                                #if she wants you gone
                                if ApprovalCheck(Party[0],900)or ApprovalCheck(Party[0],700,"L") or ApprovalCheck(Party[0],500,"O"):
                                    $ Party[0].FaceChange("bemused",1)
                                    $ Line = 1
                                    if Party[0] is RogueX:
                                            ch_r "Ну. . . Думаю, все обернулось не так уж плохо. . ."
                                    elif Party[0] is KittyX:
                                            ch_k "и все прошло довольно хорошо. . ."
                                    elif Party[0] is EmmaX:
                                            ch_e "Это был приятный вечер."
                                    elif Party[0] is LauraX:
                                            ch_l "Да, так и было."
                                    elif Party[0] is JeanX:
                                            ch_j "Наверное?"
                                    elif Party[0] is StormX:
                                            ch_s "Это было замечательно. . ."
                                    elif Party[0] is JubesX:
                                            ch_v "Да-да. . ."
                                    elif Party[0] is GwenX:
                                            ch_g "Верно. . ."
                                    elif Party[0] is BetsyX:
                                            ch_b "И мы ужасно приятно провели время. . ."
                                    elif Party[0] is DoreenX:
                                            ch_d "Ну, ага. . ."
                                    elif Party[0] is WandaX:
                                            ch_w "Конечно. . ."
                                else:
                                    $ Party[0].FaceChange("smile",Brows="confused")
                                    # Line = 0
                                    if Party[0] is RogueX:
                                            ch_r "Боюсь, что не в этот раз, [RogueX.Petname]. Увидимся."
                                    elif Party[0] is KittyX:
                                            ch_k "Хм, нет, боюсь, что не в этот раз. Увидимся завтра."
                                    elif Party[0] is EmmaX:
                                            ch_e "Что ж, не сегодня, [EmmaX.Petname]."
                                    elif Party[0] is LauraX:
                                            ch_l "Да, но не в этот раз."
                                    elif Party[0] is JeanX:
                                            ch_j "И что?"
                                    elif Party[0] is StormX:
                                            ch_s "Да, но, к сожалению, не сегодня. . ."
                                    elif Party[0] is JubesX:
                                            ch_v "Ага, я знаю, но сегодня вечером у меня дела. . ."
                                    elif Party[0] is GwenX:
                                            ch_g "Да, но у меня еще остались кое-какие дела. . ."
                                    elif Party[0] is BetsyX:
                                            ch_b "Боюсь, что сегодня все будет по-другому. . ."
                                    elif Party[0] is DoreenX:
                                            ch_d "Да, но сегодня мне нужно немного поспать. . ."
                                    elif Party[0] is WandaX:
                                            ch_w "Ага, но мне нужно немного побыть одной. . ."

                                    if bg_current != "bg player":
                                            #if it's a girl's room, you leave.
                                            ch_p "Хорошо, тогда я пойду."
                    #if she didn't offer to sleep over

            if Line == "leave":
                    # if you agreed to leave
                    $ Party[0].Statup("Love", 90, 3)
                    $ Party[0].Statup("Inbt", 25, 2)
                    $ Party[0].FaceChange("smile")
                    $ Line = 0
                    if Party[0] is RogueX:
                            ch_r "Ага, спокойной ночи, [RogueX.Petname]. . ."
                    elif Party[0] is KittyX:
                            ch_k "Ага, спокойной, [KittyX.Petname]. . ."
                    elif Party[0] is EmmaX:
                            ch_e "Да, спокойной ночи, [EmmaX.Petname]."
                    elif Party[0] is LauraX:
                            ch_l "Ладно, тогда спокойной ночи."
                    elif Party[0] is JeanX:
                            ch_j "Ладно, спокойной."
                    elif Party[0] is StormX:
                            ch_s "Да, спокойной ночи."
                    elif Party[0] is JubesX:
                            ch_v "Угум. . . увидимся. . ."
                    elif Party[0] is GwenX:
                            ch_g "Ладно, спокойной, [GwenX.Petname]. . ."
                    elif Party[0] is BetsyX:
                            ch_b "Тогда до завтра. . ."
                    elif Party[0] is DoreenX:
                            ch_d "Ладно, спокойной!"
                    elif Party[0] is WandaX:
                            ch_w "Спокойной."

            if Line == "please":
                    #if she said no but you asked nicely
                    if ApprovalCheck(Party[0],1000,Bias=-200) or ApprovalCheck(Party[0],700,"L") or ApprovalCheck(Party[0],500,"O"):
                        $ Party[0].FaceChange("bemused")
                        $ Line = 1
                        if Party[0] is RogueX:
                                ch_r "Ну. . . Думаю, ничего плохого не случится."
                        elif Party[0] is KittyX:
                                ch_k "Ну, мооожет быыыть. . ."
                        elif Party[0] is EmmaX:
                                ch_e "Полагаю, мы могли бы в этот раз сделать исключение. . ."
                        elif Party[0] is LauraX:
                                ch_l "Как хочешь."
                        elif Party[0] is JeanX:
                                ch_j "Блин, -ладно-."
                        elif Party[0] is StormX:
                                ch_s "Ох, пожалуй, можно. . ."
                        elif Party[0] is JubesX:
                                ch_v "Нууу. . . ладно. . ."
                        elif Party[0] is GwenX:
                                ch_g "Ох, как я могу отказать такой мордашке. . ."
                        elif Party[0] is BetsyX:
                                ch_b "Пожалуй, сегодня можно сделать исключение. . ."
                        elif Party[0] is DoreenX:
                                ch_d "Ну, наверное, можно. . ."
                        elif Party[0] is WandaX:
                                ch_w "Ладно, как скажешь. . ."
                    else:
                        $ Party[0].FaceChange("smile",Brows="confused")
                        $ Line = 0
                        if Party[0] is RogueX:
                                ch_r "Боюсь, что нет, [RogueX.Petname]. Иди к себе, увидимся позже."
                        elif Party[0] is KittyX:
                                ch_k "Ээээм. . . нет, не сегодня, [KittyX.Petname]. Извини."
                        elif Party[0] is EmmaX:
                                ch_e "Боюсь, что нет."
                        elif Party[0] is LauraX:
                                ch_l "Не дави."
                        elif Party[0] is JeanX:
                                ch_j "Ага, ну уж нет."
                        elif Party[0] is StormX:
                                ch_s "Нет, мы не можем."
                        elif Party[0] is JubesX:
                                ch_v "Неа."
                        elif Party[0] is GwenX:
                                ch_g "Извини, [GwenX.Petname]. . ."
                        elif Party[0] is BetsyX:
                                ch_b "Я не могу. . ."
                        elif Party[0] is DoreenX:
                                ch_d "Ага, но нет."
                        elif Party[0] is WandaX:
                                ch_w "Прости, [WandaX.Petname]."

            if not Line:
                    #if the primary girl refused to sleep over
                    if Party[0].Home == bg_current:
                            #if it's her room, removes any other girls around
                            call CleartheRoom(Party[0],1)
                            jump Return_Player
                    else:
                            #if it's not her room, remove her, and try again
                            call Remove_Girl(Party[0])
                            call Sleepover
                            return

            #If the primary girl agreed
            if len(Party) >= 2:
                #if there is another girl
                if Party[0].GirlLikeCheck(Party[1]) >= 700 and ApprovalCheck(Party[0], 1200,Bias=-300):
                        # If she likes the other girl quite a bit and likes you a decent amount
                        if Party[0] is RogueX:
                                ch_r "А ты, [Party[1].Name]?"
                        elif Party[0] is KittyX:
                                ch_k "А как насчет тебя, [Party[1].Name]?"
                        elif Party[0] is EmmaX:
                                ch_e "А что насчет тебя, [Party[1].Name]?"
                        elif Party[0] is LauraX:
                                ch_l "А ты, [Party[1].Name]?"
                        elif Party[0] is JeanX:
                                ch_j ". . ."
                                ch_j ". . . . . ."
                                ch_j "А ты, [Party[1].Name]?"
                        elif Party[0] is StormX:
                                ch_s "А ты тоже останешься, [Party[1].Name]?"
                        elif Party[0] is JubesX:
                                ch_v "А что насчет тебя, [Party[1].Name]?"
                        elif Party[0] is GwenX:
                                ch_g "Ты тоже, [Party[1].Name]. . .?"
                        elif Party[0] is BetsyX:
                                ch_b "Ты присоединишься к нам, [Party[1].Name]?"
                        elif Party[0] is DoreenX:
                                ch_d "А ты останешься, [Party[1].Name]?"
                        elif Party[0] is WandaX:
                                ch_w "А как насчет тебя, [Party[1].Name]?"

                else:
                        if Party[0] is RogueX:
                                ch_r "Ты уходишь, [Party[1].Name]?"
                        elif Party[0] is KittyX:
                                ch_k "Ты уйдешь, [Party[1].Name]?"
                        elif Party[0] is EmmaX:
                                ch_e "Полагаю, ты уходишь, [Party[1].Name]?"
                        elif Party[0] is LauraX:
                                ch_l "Увидимся позже, [Party[1].Name]."
                        elif Party[0] is JeanX:
                                ch_j ". . ."
                                ch_j ". . . . . ."
                                ch_j "А ты, [Party[1].Name]?"
                        elif Party[0] is StormX:
                                ch_s "Предположу, что ты уходишь, [Party[1].Name]?"
                        elif Party[0] is JubesX:
                                ch_v "Ты должна идти, -да-, [Party[1].Name]?"
                        elif Party[0] is GwenX:
                                ch_g "Значит увидимся позже, [Party[1].Name]? . ."
                        elif Party[0] is BetsyX:
                                ch_b "Тогда, пожалуй, тебе пора идти, [Party[1].Name]."
                        elif Party[0] is DoreenX:
                                ch_d "Думаю, тебе уже пора, [Party[1].Name]?"
                        elif Party[0] is WandaX:
                                ch_w "А как насчет тебя, [Party[1].Name]?"

                if Party[1].GirlLikeCheck(Party[0]) >= 500 and ApprovalCheck(Party[1], 1200,Bias=-200):
                        # If second girl likes the other girl a bit and likes you a decent amount
                        $ Party[1].FaceChange("smile")
                        if Party[1] is RogueX:
                                ch_r "Я бы тоже хотела остаться."
                        elif Party[1] is KittyX:
                                ch_k "Можно я тоже останусь?"
                        elif Party[1] is EmmaX:
                                ch_e "Я бы предпочла присоединиться к веселью."
                        elif Party[1] is LauraX:
                                ch_l "Я тоже, ладно?"
                        elif Party[1] is JeanX:
                                ch_j "Звучит весело, я в деле."
                        elif Party[1] is StormX:
                                ch_s "Я бы предпочла остаться."
                        elif Party[1] is JubesX:
                                ch_v "Я тоже могу остаться, да?"
                        elif Party[1] is GwenX:
                                ch_g "Я могу поучаствовать, правда?"
                        elif Party[1] is BetsyX:
                                ch_b "Я бы не хотела остаться в стороне. . ."
                        elif Party[1] is DoreenX:
                                ch_d "Оу, а мне обязательно уходить?"
                        elif Party[1] is WandaX:
                                ch_w "Я не могу остаться?"
                        $ Line = 1
                else:
                        $ Party[0].FaceChange("smile",1)
                        if Party[1] is RogueX:
                                ch_r "Думаю, мне пора идти."
                        elif Party[1] is KittyX:
                                ch_k "Я должна идти, ладно?"
                        elif Party[1] is EmmaX:
                                ch_e "Полагаю, трое - слишком много."
                        elif Party[1] is LauraX:
                                ch_l "Я должна уйти."
                        elif Party[1] is JeanX:
                                ch_j "Звучит \"очень\" весело"
                                ch_j "Увидимся позже ребята."
                        elif Party[1] is StormX:
                                ch_s "Ах, тогда мне пора идти."
                        elif Party[1] is JubesX:
                                ch_v "Эм, ага... у меня дела, так что. . ."
                        elif Party[1] is GwenX:
                                ch_g "Ох, ну. . . Мне пора идти. . ."
                        elif Party[1] is BetsyX:
                                ch_b "Пожалуй, мне лучше вам не мешать. . ."
                        elif Party[1] is DoreenX:
                                ch_d "Третий лишний. . ."
                        elif Party[1] is WandaX:
                                ch_w "Не хотелось бы злоупотреблять гостеприимством. . ."
                        $ Line = 0
                menu:
                    extend ""
                    "Ты должна остаться, [Party[1].Name].":
                            #this checks the second girl's response.
                            if Party[1].GirlLikeCheck(Party[0]) >= 500 and ApprovalCheck(Party[1], 1200,Bias=-200):
                                    # If second girl likes the first girl a bit and likes you a decent amount
                                    if Party[1] is RogueX:
                                            ch_r "Ох, С удовольствием."
                                    elif Party[1] is KittyX:
                                            ch_k "Теперь мы соседи по комнате!"
                                    elif Party[1] is EmmaX:
                                            ch_e "С удовольствием."
                                    elif Party[1] is LauraX:
                                            ch_l "Здорово."
                                    elif Party[1] is JeanX:
                                            ch_j "О, я так рада, что мне разрешили. . ."
                                    elif Party[1] is StormX:
                                            ch_s "Спасибо, с удовольствием останусь."
                                    elif Party[1] is JubesX:
                                            ch_v "О! Спасибо!"
                                    elif Party[1] is GwenX:
                                            ch_g "О! Круто!"
                                    elif Party[1] is BetsyX:
                                            ch_b "С удовольствием."
                                    elif Party[1] is DoreenX:
                                            ch_d "Ох, здорово!"
                                    elif Party[1] is WandaX:
                                            ch_w "Ты нехороший человек."
                                    $ Line = 1
                                    $ Party[0].GLG(Party[1],800,3,1)
                            else:
                                    $ Party[1].FaceChange("sadside",1,Mouth="smile")
                                    if Party[1] is RogueX:
                                            ch_r "Я не хочу мешать."
                                    elif Party[1] is KittyX:
                                            ch_k "Не получится."
                                    elif Party[1] is EmmaX:
                                            ch_e "Я не могу."
                                    elif Party[1] is LauraX:
                                            ch_l "Нет."
                                    elif Party[1] is JeanX:
                                            $ Party[1].FaceChange("angry",1,Mouth="smile")
                                            ch_j "О, я так рада, что мне разрешили. . ."
                                    elif Party[1] is StormX:
                                            ch_s "Я не хотела бы мешать."
                                    elif Party[1] is JubesX:
                                            ch_v ". . . нее, серьезно. . . у меня дела."
                                    elif Party[1] is GwenX:
                                            ch_g "Оу. . . неа, я бы не хотела мешать. . ."
                                    elif Party[1] is BetsyX:
                                            ch_b "Я не хочу мешать вам. . ."
                                    elif Party[1] is DoreenX:
                                            ch_d "Ох, может быть, когда-нибудь. . ."
                                    elif Party[1] is WandaX:
                                            ch_w "Нет, это не тебе решать."
                                    $ Line = 0
                                    $ Party[0].GLG(Party[1],700,-5,1)

                            #This checks the first girl's response
                            if Line:
                                if Party[0].GirlLikeCheck(Party[1]) >= 700 and ApprovalCheck(Party[0], 1200,Bias=-200):
                                    # If first girl likes the other girl quite a bit and likes you a decent amount
                                    if Party[0] is RogueX:
                                            ch_r "Отлично!"
                                    elif Party[0] is KittyX:
                                            ch_k "Теперь мы соседи по комнате!"
                                    elif Party[0] is EmmaX:
                                            ch_e "Прекрасно."
                                    elif Party[0] is LauraX:
                                            ch_l "Ладно."
                                    elif Party[0] is JeanX:
                                            ch_j "Как мило, тройничок."
                                    elif Party[0] is StormX:
                                            ch_s "Замечательно, я рада."
                                    elif Party[0] is JubesX:
                                            ch_v "О, круто!"
                                    elif Party[0] is GwenX:
                                            ch_g "Здорово!"
                                    elif Party[0] is BetsyX:
                                            ch_b "Рада, что ты с нами."
                                    elif Party[0] is DoreenX:
                                            ch_d "Ох, здорово!"
                                    elif Party[0] is WandaX:
                                            ch_w "Уже интересней."
                                    $ Party[1].GLG(Party[0],800,5,1)
                                elif Party[0].GirlLikeCheck(Party[1]) >= 400 and ApprovalCheck(Party[0], 1400,Bias=-200):
                                    # If she barely likes the other girl but likes you a a lot
                                    $ Party[0].FaceChange("sadside",1,Mouth="smile")
                                    if Party[0] is RogueX:
                                            ch_r "Конечно. . . наверное."
                                    elif Party[0] is KittyX:
                                            ch_k "Эм, ладно."
                                    elif Party[0] is EmmaX:
                                            ch_e "Думаю, здесь хватит места для еще одного."
                                    elif Party[0] is LauraX:
                                            ch_l "Как скажешь."
                                    elif Party[0] is JeanX:
                                            ch_j "Ага, ладно."
                                    elif Party[0] is StormX:
                                            ch_s "Хорошо, чувствуйте себя как дома. . ."
                                    elif Party[0] is JubesX:
                                            ch_v "О, круто! Обещаю не кусаться."
                                    elif Party[0] is GwenX:
                                            ch_g "Ладно, думаю, это нормально. . ."
                                    elif Party[0] is BetsyX:
                                            ch_b "Пожалуй, и для нее место найдется. . ."
                                    elif Party[0] is DoreenX:
                                            ch_d "Ну, если ты этого хочешь. . ."
                                    elif Party[0] is WandaX:
                                            ch_w "Конечно, как скажешь."
                                else:
                                    $ Party[0].FaceChange("angry",1)
                                    if Party[0] is RogueX:
                                            ch_r "Меня это не устраивает."
                                    elif Party[0] is KittyX:
                                            ch_k "Ни за что."
                                    elif Party[0] is EmmaX:
                                            ch_e "Я так не думаю."
                                    elif Party[0] is LauraX:
                                            ch_l "Эм, нет."
                                    elif Party[0] is JeanX:
                                            ch_j "Точно нет."
                                    elif Party[0] is StormX:
                                            ch_s "Нет, боюсь, что нет, [Party[1].Name]."
                                    elif Party[0] is JubesX:
                                            ch_v "О. . . круто. Обещаю не кусаться."
                                            ch_v "сильно. . ."
                                    elif Party[0] is GwenX:
                                            ch_g "Эм, нет. . ."
                                    elif Party[0] is BetsyX:
                                            ch_b "Мне. . . это не нравится."
                                    elif Party[0] is DoreenX:
                                            ch_d "Я. . . так не думаю. . ."
                                    elif Party[0] is WandaX:
                                            ch_w "Я так не думаю."
                                    $ Party[0].GLG(Party[1],700,-5,1)
                                    $ Party[1].GLG(Party[0],700,-5,1)
                                    $ Line = 0

                    "Тебе пора идти, [Party[1].Name].":
                            if Party[1] is RogueX:
                                    ch_r "Ох, ладно."
                            elif Party[1] is KittyX:
                                    ch_k "Ага."
                            elif Party[1] is EmmaX:
                                    ch_e "Я так и предполагала."
                            elif Party[1] is LauraX:
                                    ch_l "Ага."
                            elif Party[1] is JeanX:
                                    ch_j "Что? Это не ты выгоняешь меня, а я сама ухожу!"
                            elif Party[1] is StormX:
                                    ch_s "Ах, я понимаю."
                            elif Party[1] is JubesX:
                                    ch_v "О, ну, ладно. . ."
                            elif Party[1] is GwenX:
                                    ch_g "Что? Ох, ладно. . ."
                            elif Party[1] is BetsyX:
                                    ch_b "-вздох- Жаль. . ."
                            elif Party[1] is DoreenX:
                                    ch_d "Оу, облом."
                            elif Party[1] is WandaX:
                                    ch_w "Конечно."
                            $ Line = 0

            if Line == 0:
                    #if the second girl got the boot:
                    if len(Party) >= 2:
                        if Party[0] is RogueX:
                                ch_r "До встречи, [Party[1].Name]."
                        elif Party[0] is KittyX:
                                ch_k "Спокойной, [Party[1].Name]."
                        elif Party[0] is EmmaX:
                                ch_e "Доброй ночи, [Party[1].Name]."
                        elif Party[0] is LauraX:
                                ch_l "Спокойной."
                        elif Party[0] is JeanX:
                                ch_j "До встречи, [Party[1].Name]."
                        elif Party[0] is StormX:
                                ch_s "Спокойной ночи, [Party[1].Name]."
                        elif Party[0] is JubesX:
                                ch_v "Спокойной, [Party[1].Name]."
                        elif Party[0] is GwenX:
                                ch_g "Ладно, спокойной [Party[1].Name]. . ."
                        elif Party[0] is BetsyX:
                                ch_b "Увидимся, [Party[1].Name]."
                        elif Party[0] is DoreenX:
                                ch_d "До завтра, [Party[1].Name]."
                        elif Party[0] is WandaX:
                                ch_w "Спокойной, [Party[1].Name]."

                        if Party[1] is RogueX:
                                ch_r "До встречи, ребята."
                        elif Party[1] is KittyX:
                                ch_k "Спокойной."
                        elif Party[1] is EmmaX:
                                ch_e "Доброй ночи."
                        elif Party[1] is LauraX:
                                ch_l "Спокойной."
                        elif Party[1] is JeanX:
                                ch_j "Хорошо, до встречи."
                        elif Party[1] is StormX:
                                ch_s "Спокойной ночи."
                        elif Party[1] is JubesX:
                                ch_v "Спокойной!"
                        elif Party[1] is GwenX:
                                ch_g "Ладно, спокойной. . ."
                        elif Party[1] is BetsyX:
                                ch_b "Увидимся завтра."
                        elif Party[1] is DoreenX:
                                ch_d "Увидимся!"
                        elif Party[1] is WandaX:
                                ch_w "Спокойной."
                    if Party:
                        call CleartheRoom(Party[0],1,1) #removes any other girls around

            if not Party:
                    #if nobody is around.
                    if bg_current != "bg player":
                            jump Return_Player
                    call CleartheRoom("All",1)
                    #if nobody is here, you just go to sleep
                    "Уже поздно, так что вы идете спать."
                    call Wait
                    return

            if bg_current != "bg player" and bg_current != Party[0].Home:
                    #if the room's owner left you in her room. . .
                    "Вам, пожалуй, не стоит здесь спать, вы возвращаетесь в свою комнату."
                    call Remove_Girl("All")
                    $ renpy.pop_call()
                    jump Player_Room

            jump Sleepover_Morning


label Return_Player:
        # This label is jumped to by the Sleep labels if the player or girl leaves after a sleepover (fail state).
        $ del Party[:]
        $ BO = TotalGirls[:]
        $ renpy.random.shuffle(BO)
        while BO:
                if bg_current != BO[0].Home and BO[0].Loc == bg_current:
                        "[BO[0].Name] выходит."
                        $ BO[0].Loc = BO[0].Home
                $ BO.remove(BO[0])
        if bg_current != "bg player":
                "Вы возвращаетесь в свою комнату."
        $ bg_current = "bg player"
        jump Misplaced
#        call Set_The_Scene
#        $ renpy.pop_call()
#        jump Player_Room

label Sleepover_Morning: #rkeljsvgbdw
        #This label is jumped too from Sleepover if you successfully stay the night
        $ BO = TotalGirls[:]
        while BO:
                if BO[0].Loc == bg_current and BO[0] not in Party:
                        call Remove_Girl(BO[0])
                $ BO.remove(BO[0])

        call Shift_Focus(Party[0])

        if Party[0] is StormX and not StormX.Sleepwear[0] and StormX.Taboo < 20:
                #if it's Storm, you haven't set Sleepwear, and there's nobody else that would mind, go nude
                $ Party[0].OutfitChange("nude")
        else:
                $ Party[0].OutfitChange("sleep")
        $ Party[0].OutfitDay == Party[0].Outfit
        if len(Party) >= 2:
                #If there are two girls. . .
                if Party[1] is StormX and not StormX.Sleepwear[0] and StormX.Taboo < 20:
                        #if it's Storm, you haven't set Sleepwear, and there's nobody else that would mind, go nude
                        $ Party[1].OutfitChange("nude")
                else:
                        $ Party[1].OutfitChange("sleep")
                $ Party[1].OutfitDay == Party[1].Outfit
                "Девушки переодеваются в одежду для сна."
        else:
                "[Party[0].Name] переодевается в одежду для сна."

        if Party[0] is RogueX:
                ch_r "Ммм, так немного удобнее."
        elif Party[0] is KittyX:
                ch_k "Ах, так-то лучше."
        elif Party[0] is EmmaX:
                ch_e "Ммм, так-то лучше."
        elif Party[0] is LauraX:
                ch_l ". . ."
        elif Party[0] is JeanX:
                ch_j "Так сексуальнее, верно?"
        elif Party[0] is StormX:
                ch_s "Ах, намного лучше."
        elif Party[0] is JubesX:
                ch_v "Ах, так-то лучше."
        elif Party[0] is GwenX:
                ch_g "Симпатичный наряд, правда?"
        elif Party[0] is BetsyX:
                ch_b "Вот, так-то лучше. . ."
        elif Party[0] is DoreenX:
                ch_d "Ладно, так гораздо лучше."
        elif Party[0] is WandaX:
                ch_w "Ахххх."

        # should no longer be necessary
        #$ Party[0].Traits.append("sleepover") #this is temporary, removed in the morning

        if len(Party) >= 2:
                if Party[1] is RogueX:
                        ch_r "Давайте ложиться."
                elif Party[1] is KittyX:
                        ch_k "Спокойной, [KittyX.Petname]"
                elif Party[1] is EmmaX:
                        ch_e "Выключаем свет."
                elif Party[1] is LauraX:
                        ch_l "Спокойной."
                elif Party[1] is JeanX:
                        ch_j "Спокойной."
                elif Party[1] is StormX:
                        ch_s "Спокойной ночи."
                elif Party[1] is JubesX:
                        ch_v "Спокойной."
                elif Party[1] is GwenX:
                        ch_g "Ладно, тогда спокойной. . ."
                elif Party[1] is BetsyX:
                        ch_b "Спокойной ночи. . ."
                elif Party[1] is DoreenX:
                        ch_d "Ладно, спокойной!"
                elif Party[1] is WandaX:
                        ch_w "Спокойной."
                # should no longer be necessary
                #$ Party[1].Traits.append("sleepover") #this is temporary, removed in the morning
        else:
                if Party[0] is RogueX:
                        ch_r "Давай ложиться."
                elif Party[0] is KittyX:
                        ch_k "Спокойной, [KittyX.Petname]"
                elif Party[0] is EmmaX:
                        ch_e "Доброй ночи."
                elif Party[0] is LauraX:
                        ch_l "Спокойной."
                elif Party[0] is JeanX:
                        ch_j "Спокойной."
                elif Party[0] is StormX:
                        ch_s "Спокойной ночи."
                elif Party[0] is JubesX:
                        ch_v "Спокойной."
                elif Party[0] is GwenX:
                        ch_g "Ладно, спокойной тогда. . ."
                elif Party[0] is BetsyX:
                        ch_b "Спокойной ночи. . ."
                elif Party[0] is DoreenX:
                        ch_d "Ладно, спокойной!"
                elif Party[0] is WandaX:
                        ch_w "Спокойной."

        show blackscreen onlayer black
        pause 1


        #replace "Wait" content here. . .
        #call Wait(0,0) #shouldn't change outfit or lighting

        #fake "wait" period to make it temporarily morning. Is reversed later.
        $ Time_Count = 0
        $ Current_Time = Time_Options[(Time_Count)]
        $ Day += 1

        if Weekday < 6:
            $ Weekday += 1
        else:
            $ Weekday = 0



        $ DayofWeek = Week[Weekday]
        hide NightMask onlayer nightmask
        $ Player.Semen = Player.Semen_Max
        $ Player.Spunk = 0
        $ Round = 50

        $ BO = Party[:]
        while BO:
            $ BO[0].Action = BO[0].MaxAction
            $ BO.remove(BO[0])

        # should no longer be necessary
#        $ Party = []
#        $ BO = TotalGirls[:]
#        while BO:
#                if "sleepover" in BO[0].Traits:
#                        $ Party.append(BO[0])
#                        $ BO[0].Loc = bg_current
#                        $ BO[0].Outfit = "sleep"
#                        $ BO[0].OutfitChange()
#                elif BO[0].Loc == bg_current:
#                        call Remove_Girl(BO[0])
#                $ BO.remove(BO[0])

        call Morningwood_Check # / / / / / / / checks for morning wood event here / / / / / / / checks for morning wood event here / / / / / / / checks for morning wood event here

        $ Party[0].FaceChange("smile")
        if len(Party) >= 2:
                $ Party[1].FaceChange("smile")
        hide NightMask onlayer nightmask
        hide blackscreen onlayer black

        if "morningwood" in Player.DailyActions:
                #if you got some
                if Party[0] is RogueX:
                        ch_r "Ну так как, хорошо спалось?"
                elif Party[0] is KittyX:
                        ch_k "Ну. . . доброго утречка . . ."
                elif Party[0] is EmmaX:
                        ch_e "Раз уж мы решились на это. . ."
                        ch_e "Доброе утро, [Party[0].Petname]."
                elif Party[0] is LauraX:
                        ch_l "В общем, доброе утро."
                elif Party[0] is JeanX:
                        ch_j "Ну. . . Доброе утро."
                elif Party[0] is StormX:
                        ch_s "В общем,  доброе утро, [Party[0].Petname]."
                elif Party[0] is JubesX:
                        ch_v "В общем,  доброе утро, [Party[0].Petname]."
                elif Party[0] is GwenX:
                        ch_g "Утречка, [Party[0].Petname]. . ."
                elif Party[0] is BetsyX:
                        ch_b "Как спалось, [Party[0].Petname]?"
                elif Party[0] is DoreenX:
                        ch_d "Ну, как спалось?"
                elif Party[0] is WandaX:
                        ch_w "Утречка. . ."
        else:
                if Party[0] is RogueX:
                        ch_r "Утречка, [RogueX.Petname]. Хорошо спалось?"
                elif Party[0] is KittyX:
                        ch_k "Доброго утречка. . ."
                elif Party[0] is EmmaX:
                        ch_e "Хрммм. . ."
                        ch_e "О. Ты здесь."
                elif Party[0] is LauraX:
                        ch_l "Доброе утро."
                elif Party[0] is JeanX:
                        ch_j "-зевает-"
                elif Party[0] is StormX:
                        ch_s "Доброе утро, [StormX.Petname]."
                elif Party[0] is JubesX:
                        ch_v "Приветик. . . доброе утро, [Party[0].Petname]."
                elif Party[0] is GwenX:
                        ch_g "-зевает- доброе утро, [Party[0].Petname]. . ."
                elif Party[0] is BetsyX:
                        ch_b "Мммм, тебе хорошо спалось, [Party[0].Petname]?"
                elif Party[0] is DoreenX:
                        ch_d "Хорошо спалось?"
                elif Party[0] is WandaX:
                        ch_w "Утречка. . ."

        menu:
            extend ""
            "С тобой всегда приятно спать." if Party[0].Sleep:
                    if Party[0].Sleep < 5:
                            $ Party[0].Statup("Love", 90, 8)
                            $ Party[0].Statup("Obed", 50, 10)
                            $ Party[0].Statup("Inbt", 70, 8)
                    $ Party[0].Blush = 1

                    if Party[0] is RogueX:
                            if not Player.Male:
                                ch_r "Ах, ты такая милая, [RogueX.Petname]."
                                ch_r "Мы можем всегда спать вместе."
                            else:
                                ch_r "Ах, ты такой милый, [RogueX.Petname]."
                                ch_r "Мы можем всегда спать вместе."
                    elif Party[0] is KittyX:
                            ch_k "Такое всегда приятно слышать."
                            ch_k "Мы можем продолжать спать вместе."
                    elif Party[0] is EmmaX:
                            ch_e "Хорошо. . ."
                            ch_e "Тогда давай возьмем это в привычку."
                    elif Party[0] is LauraX:
                            ch_l "Ага. . ."
                            ch_l "С тобой тепло. . ."
                    elif Party[0] is JeanX:
                            ch_j "Ну конечно."
                            ch_j "Я же принцесса."
                    elif Party[0] is StormX:
                            ch_s "Мне тоже нравится, [StormX.Petname]."
                            ch_s "Ты согреваешь постель. . ."
                    elif Party[0] is JubesX:
                            ch_v "Ага. . . приятно, когда кто-то рядом. . ."
                            ch_v "С тобой так уютно. . ."
                    elif Party[0] is GwenX:
                            ch_g "Оу, ага. . . с тобой очень уютно. . ."
                    elif Party[0] is BetsyX:
                            ch_b "Восхитительно."
                    elif Party[0] is DoreenX:
                            ch_d "Оуууу. . ."
                    elif Party[0] is WandaX:
                            ch_w "Странный ты человек. . ."

            "Мне понравилось спать рядом с тобой." if not Party[0].Sleep:
                    $ Party[0].Statup("Love", 90, 15)
                    $ Party[0].Statup("Love", 70, 10)
                    $ Party[0].Statup("Obed", 50, 12)
                    $ Party[0].Statup("Inbt", 70, 12)
                    $ Line = "nice"

            "Это было забавно.":
                    if not Party[0].Sleep:
                            $ Party[0].Statup("Love", 90, 10)
                            $ Party[0].Statup("Love", 70, 8)
                            $ Party[0].Statup("Obed", 50, 15)
                            $ Party[0].Statup("Inbt", 70, 15)
                    elif Party[0].Sleep < 5:
                            $ Party[0].Statup("Love", 70, 8)
                            $ Party[0].Statup("Obed", 80, 10)
                            $ Party[0].Statup("Inbt", 35, 8)
                    $ Party[0].Statup("Obed", 50, 8)
                    if ApprovalCheck(Party[0], 800, "L"):
                            $ Party[0].FaceChange("bemused")
                    else:
                            $ Party[0].FaceChange("confused")

                    $ Line = "fun"
                    if Party[0] is RogueX:
                            ch_r "Ладно, надеюсь, я не {i}слишком{/i} тебе докучала."
                    elif Party[0] is KittyX:
                            ch_k "Ага, наверное. . ."
                    elif Party[0] is EmmaX:
                            ch_e "\"Забавно\" я сказала бы также."
                    elif Party[0] is LauraX:
                            ch_l "Да, наверное?"
                    elif Party[0] is JeanX:
                            ch_j "Эм, \"забавно?\" . . Ага."
                    elif Party[0] is StormX:
                            ch_s ". . . Да. . ."
                            ch_s ". . . забавно."
                    elif Party[0] is JubesX:
                            ch_v "Ага. . . приятно, когда кто-то рядом. . ."
                            $ Line = "nice"
                    elif Party[0] is GwenX:
                            ch_g "Рада это слышать. . ."
                            $ Line = "nice"
                    elif Party[0] is BetsyX:
                            ch_b "Ну и хорошо."
                    elif Party[0] is DoreenX:
                            ch_d "Эм, ага."
                    elif Party[0] is WandaX:
                            ch_w "Хех. . ."

            "Ты постоянно толкалась.":
                    $ Party[0].Blush = 1
                    if ApprovalCheck(Party[0], 800, "L") or ApprovalCheck(Party[0], 1200):
                            $ Party[0].FaceChange("bemused")
                            call AnyLine(Party[0],"Хмм?")
                    else:
                            $ Party[0].FaceChange("angry")
                            call AnyLine(Party[0],"!!!")
                    if Party[0].Sleep < 5:
                            if Party[0] is RogueX:
                                    ch_r "Ну, как будто ты не знаешь, что это мне в новинку. . ."
                            elif Party[0] is KittyX:
                                    ch_k "Я не специально. . ."
                            elif Party[0] is EmmaX:
                                    ch_e "Я давно не спала ни с кем рядом."
                            elif Party[0] is LauraX:
                                    ch_l "Смирись."
                            elif Party[0] is JeanX:
                                    ch_j "Это называется \"женская грация.\""
                            elif Party[0] is StormX:
                                    ch_s "Да. . . что ж. . ."
                                    ch_s "у меня много энергии. . ."
                            elif Party[0] is JubesX:
                                    ch_v "Я просто не привыкла спать по ночам. . ."
                            elif Party[0] is GwenX:
                                    ch_g "Ага, согласна. . ."
                            elif Party[0] is BetsyX:
                                    ch_b ". . . Я не. . . \"толкаюсь.\""
                            elif Party[0] is DoreenX:
                                    ch_d "Ну. . . во мне много энергии."
                            elif Party[0] is WandaX:
                                    ch_w "Да?"
                            $ Party[0].Statup("Love", 60, -8)
                            $ Party[0].Statup("Obed", 50, 22)
                            $ Party[0].Statup("Inbt", 50, 22)
                    else:
                            if Party[0] is RogueX:
                                    if not Player.Male:
                                        ch_r "Ну, ты, наверное, уже должна была привыкнуть"
                                    else:
                                        ch_r "Ну, ты, наверное, уже должен был привыкнуть"
                            elif Party[0] is KittyX:
                                    if not Player.Male:
                                        ch_k "Да, но. . . ты уже должна была привыкнуть!"
                                    else:
                                        ch_k "Да, но. . . ты уже должен был привыкнуть!"
                            elif Party[0] is EmmaX:
                                    ch_e "Сейчас у меня нет в планах менять свои привычки."
                            elif Party[0] is LauraX:
                                    ch_l "Да, и так будет всегда."
                            elif Party[0] is JeanX:
                                    ch_j "Смирись."
                            elif Party[0] is StormX:
                                    ch_s "Пожалуй, что так."
                            elif Party[0] is JubesX:
                                    ch_v "Тебе не нужно зацикливаться на этом. . ."
                            elif Party[0] is GwenX:
                                    ch_g "-Мы знаем.-"
                            elif Party[0] is BetsyX:
                                    ch_b "Да-да, мы это прекрасно знаем. . ."
                            elif Party[0] is DoreenX:
                                    ch_d "Угу-м. . ."
                            elif Party[0] is WandaX:
                                    ch_w "Конечно. . ."
                    $Line = "toss"

            "Тебе надо научиться спать на своей стороне.":
                    if Party[0].Sleep < 5:
                            $ Party[0].Statup("Love", 80, -8)
                            $ Party[0].Statup("Obed", 50, 40)
                    if ApprovalCheck(Party[0], 500, "O"):
                            $ Party[0].Statup("Love", 80, -2)
                            $ Party[0].Statup("Obed", 90, 5)
                            $ Party[0].FaceChange("normal")
                            if Party[0] is RogueX:
                                    ch_r "Ага, [RogueX.Petname], Я постараюсь."
                            elif Party[0] is KittyX:
                                    ch_k "Ладно, как скажешь."
                            elif Party[0] is EmmaX:
                                    ch_e "Я попробую."
                            elif Party[0] is LauraX:
                                    ch_l "Ладно."
                            elif Party[0] is JeanX:
                                    ch_j "Вся кровать моя сторона."
                            elif Party[0] is StormX:
                                    ch_s "Я. . . могу попробовать. . ."
                            elif Party[0] is JubesX:
                                    ch_v "Я думала, ты хочешь привлечь к себе внимание. . ."
                            elif Party[0] is GwenX:
                                    ch_g "И где тут веселье? . ."
                            elif Party[0] is BetsyX:
                                    ch_b "\"Моя сторона\" там, где я лежу."
                            elif Party[0] is DoreenX:
                                    ch_d "Оу, но мне нравится прижиматься!"
                            elif Party[0] is WandaX:
                                    ch_w "Не хочу."
                            if Party[0].Sleep < 5:
                                    $ Party[0].Statup("Obed", 80, 8)
                    else:
                            $ Party[0].FaceChange("angry")
                            $ Party[0].Statup("Obed", 90, 5)
                            if Party[0] is RogueX:
                                    if not Player.Male:
                                        ch_r "Пфффф, если продолжишь так говорить, будешь спать одна."
                                    else:
                                        ch_r "Пфффф, если продолжишь так говорить, будешь спать один."
                            elif Party[0] is KittyX:
                                    ch_k "Что-то у меня поубавилось желания спать рядом с тобой."
                            elif Party[0] is EmmaX:
                                    ch_e "Я буду спать как мне заблагорассудится."
                            elif Party[0] is LauraX:
                                    ch_l "Ну, удачи."
                            elif Party[0] is JeanX:
                                    ch_j "Вся кровать - моя сторона."
                            elif Party[0] is StormX:
                                    ch_s "Это маловероятно."
                            elif Party[0] is JubesX:
                                    ch_v "Я могла бы просто держаться подальше от кровати. . ."
                            elif Party[0] is GwenX:
                                    ch_g "Или я могла бы просто захватить всю кровать. . ."
                            elif Party[0] is BetsyX:
                                    ch_b "Я сама -решаю-, где \"моя сторона.\""
                            elif Party[0] is DoreenX:
                                    ch_d "Как грубо."
                            elif Party[0] is WandaX:
                                    ch_w "Я не привыкла делиться. . ."
                            if Party[0].Sleep < 5:
                                    $ Party[0].Statup("Inbt", 35, 20)
                    $ Line = "toss"

        if not Party[0].Sleep and Line == "nice":
                if Party[0] is RogueX:
                        $ Party[0].Blush = 1
                        if not Player.Male:
                            ch_r "Ах, ты такая милая, [RogueX.Petname]."
                        else:
                            ch_r "Ах, ты такой милый, [RogueX.Petname]."
                        ch_r "Хочу почаще спать рядом с тобой."
                elif Party[0] is KittyX:
                        $ Party[0].Blush = 2
                        ch_k "Ага, мне[KittyX.like]тоже понравилось."
                        $ Party[0].Blush = 1
                        ch_k "Я бы[KittyX.like]не прочь повторить."
                        $ Party[0].Blush = 2
                        ch_k "Ну знаешь, как - нибудь. . . "
                        $ Party[0].Blush = 1
                elif Party[0] is EmmaX:
                        $ Party[0].FaceChange("smile",1)
                        if Player.Male or "girltalk" in EmmaX.History:
                                ch_e "Ты безнадежный романтик, [EmmaX.Petname]."
                        else:
                                ch_e "Ты безнадежна, [EmmaX.Petname]."
                        $ Party[0].FaceChange("smile",2,Eyes="side")
                        ch_e "Полагаю, что тоже могу стать немного безнадежной. . ."
                elif Party[0] is LauraX:
                        $ Party[0].FaceChange("confused",1)
                        ch_l "Ох. . ."
                        $ Party[0].FaceChange("surprised",2,Brows="confused")
                        if not Player.Male:
                            ch_l "Да, и мне тоже, раз уж ты сама об этом заговорила. . ."
                        else:
                            ch_l "Да, и мне тоже, раз уж ты сам об этом заговорил. . ."
                        $ Party[0].FaceChange("confused",1)
                        ch_l "Да."
                elif Party[0] is JeanX:
                        $ Party[0].FaceChange("confused",1)
                        ch_j "А? . ."
                        ch_j "О, да. . . все было супер. . ."
                        $ Party[0].FaceChange("smile",1)
                elif Party[0] is StormX:
                        $ Party[0].FaceChange("smile",1)
                        ch_s "Что ж, да, было приятно спать рядом с тобой, [StormX.Petname]."
                        $ Party[0].FaceChange("smile",2,Eyes="leftside")
                        ch_s "Я думаю, мы должны взять это в привычку. . ."
                        $ Party[0].FaceChange("smile",1)
                elif Party[0] is JubesX:
                        $ Party[0].FaceChange("smile",1)
                        ch_v "Ага, мне тоже понравилось. . ."
                        $ Party[0].FaceChange("sad",1)
                        ch_v "Я не очень-то много сплю с тех пор, как. . ."
                        $ Party[0].FaceChange("sadside",1)
                        ch_v ". . . изменилась."
                        $ Party[0].FaceChange("smile",1)
                        ch_v "Приятно, когда кто-то остается со мной. . ."
                elif Party[0] is GwenX:
                        $ Party[0].FaceChange("sadside",1)
                        ch_g "Когда я только попала сюда, я не знала, как все обернется. . ."
                        $ Party[0].FaceChange("smile",1)
                        ch_g "Сейчас я чувствую себя намного комфортнее. . ."
                elif Party[0] is BetsyX:
                        $ Party[0].FaceChange("smile",1)
                        ch_b "Это было замечательно, [BetsyX.Petname]."
                        $ Party[0].FaceChange("sly",2,Eyes="leftside")
                        ch_b "Пожалуй, нам надо взять это в привычку. . ."
                        $ Party[0].FaceChange("smile",1)
                elif Party[0] is DoreenX:
                        $ Party[0].FaceChange("smile",1)
                        ch_d "Оу, это так мило."
                        $ Party[0].FaceChange("sly",2,Eyes="leftside")
                        ch_d "Надо будет как-нибудь снова повторить. . ."
                        $ Party[0].FaceChange("smile",1)
                elif Party[0] is WandaX:
                        $ Party[0].FaceChange("smile",1)
                        ch_w "Давненько я ни с кем не спала."
                        $ Party[0].FaceChange("sly",1,Eyes="leftside")
                        ch_w "Возможно, нам стоит делать это почаще. . ."
                        $ Party[0].FaceChange("smile",1)

        $ Party[0].Blush = 0

        if len(Party) >= 2:
            #second girl's lines
            if "morningwood" in Player.DailyActions:
                    if Party[1] is RogueX:
                            ch_r "А как насчет меня?"
                    elif Party[1] is KittyX:
                            ch_k "А мне?"
                    elif Party[1] is EmmaX:
                            ch_e "А мне?"
                    elif Party[1] is LauraX:
                            ch_l "Хм, доброе утро."
                    elif Party[1] is JeanX:
                            ch_j "Да, да, доброе утро."
                    elif Party[1] is StormX:
                            ch_s "Ах да, доброе утро."
                    elif Party[1] is JubesX:
                            ch_v "Ага. . . доброе утро."
                    elif Party[1] is GwenX:
                            ch_g "Доброе утро, [Party[1].Petname]. . ."
                    elif Party[1] is BetsyX:
                            ch_b "А мне ни слова?"
                    elif Party[1] is DoreenX:
                            ch_d "Ага, утречка!"
                    elif Party[1] is WandaX:
                            ch_w "Утречка. . ."
            else:
                    "[Party[1].Name] переворачивается в постели."
                    if Party[1] is RogueX:
                            ch_r "Ммм, да, утречка, [RogueX.Petname]."
                    elif Party[1] is KittyX:
                            ch_k "Ага, доброе утро . . ."
                    elif Party[1] is EmmaX:
                            ch_e "Хрммм. . ."
                            ch_e "Ох. Ребята, давайте не так громко."
                    elif Party[1] is JeanX:
                            ch_j "Да, да, доброе утро."
                    elif Party[1] is StormX:
                            ch_s "Ах да, доброе утро."
                    elif Party[1] is JubesX:
                            ch_v "Ох, эм, ага. . . доброе утро."
                    elif Party[1] is GwenX:
                            ch_g "-зевает- доброе утро, [Party[1].Petname]. . ."
                    elif Party[1] is BetsyX:
                            ch_b "А мне ни слова?"
                    elif Party[1] is DoreenX:
                            ch_d "Ага, утречка!"
                    elif Party[1] is WandaX:
                            ch_w "Утречка. . ."

            menu:
                extend ""
                "И с тобой тоже всегда приятно спать, [Party[1].Name]." if Party[1].Sleep:
                        if Party[1].Sleep < 5:
                            $ Party[1].Statup("Love", 90, 8)
                            $ Party[1].Statup("Obed", 50, 10)
                            $ Party[1].Statup("Inbt", 70, 8)
                        $ Party[1].Blush = 1

                        if Party[1] is RogueX:
                                ch_r "Приятно слышать такое от тебя, [RogueX.Petname]."
                        elif Party[1] is KittyX:
                                ch_k "Это так мило!"
                        elif Party[1] is EmmaX:
                                ch_e "Ммм. . . да, прелестно."
                        elif Party[1] is LauraX:
                                ch_l "Конечно. . ."
                        elif Party[1] is JeanX:
                                ch_j "Ауч, так приторно, что у меня заболели зубы."
                        elif Party[1] is StormX:
                                ch_s "И мне тоже нравится, [StormX.Petname]."
                        elif Party[1] is JubesX:
                                ch_v "Ага. . . приятно, когда кто-то рядом. . ."
                        elif Party[1] is GwenX:
                                ch_g "Оу, ага. . . Здесь очень уютно. . ."
                        elif Party[1] is BetsyX:
                                ch_b "Ты прелесть."
                        elif Party[1] is DoreenX:
                                ch_d "Оууу. . ."
                        elif Party[1] is WandaX:
                                ch_w "Странный ты человек. . ."

                "И с тобой тоже было очень приятно спать, [Party[1].Name]." if not Party[1].Sleep:
                        $ Party[1].Statup("Love", 90, 15)
                        $ Party[1].Statup("Love", 70, 10)
                        $ Party[1].Statup("Obed", 50, 12)
                        $ Party[1].Statup("Inbt", 70, 12)
                        $ Line = "nice"

                "И с тобой тоже мне было забавно спать, [Party[1].Name].":
                        if not Party[1].Sleep:
                                $ Party[1].Statup("Love", 90, 10)
                                $ Party[1].Statup("Love", 70, 8)
                                $ Party[1].Statup("Obed", 50, 15)
                                $ Party[1].Statup("Inbt", 70, 15)
                        elif Party[1].Sleep < 5:
                                $ Party[1].Statup("Love", 70, 8)
                                $ Party[1].Statup("Obed", 80, 10)
                                $ Party[1].Statup("Inbt", 35, 8)
                        $ Party[1].Statup("Obed", 50, 8)
                        if ApprovalCheck(Party[1], 800, "L"):
                                $ Party[1].FaceChange("bemused")
                        else:
                                $ Party[1].FaceChange("confused")

                        $ Line = "fun"
                        if Party[1] is RogueX:
                                ch_r "Ага, кхм, забавно."
                        elif Party[1] is KittyX:
                                ch_k "Да, наверное. . ."
                        elif Party[1] is EmmaX:
                                ch_e "\"Забавно\" я сказала бы также."
                        elif Party[1] is LauraX:
                                ch_l "Да, наверное?"
                        elif Party[1] is JeanX:
                                if not Player.Male:
                                    ch_j "Ага, все как ты и сказала."
                                else:
                                    ch_j "Ага, все как ты и сказал."
                        elif Party[1] is StormX:
                                ch_s ". . . Да. . ."
                                ch_s ". . . забавно."
                        elif Party[1] is JubesX:
                                ch_v "Ага. . . приятно, когда кто-то рядом. . ."
                                $ Line = "nice"
                        elif Party[1] is GwenX:
                                ch_g "Рада это слышать. . ."
                                $ Line = "nice"
                        elif Party[1] is BetsyX:
                                ch_b "Ну и славно."
                        elif Party[1] is DoreenX:
                                ch_d "Эм, ага."
                        elif Party[1] is WandaX:
                                ch_w "Конечно. . ."

                "[Party[1].Name], ты всю ночь толкалась." if Line == "toss":
                        $ Line = "toss"
                "[Party[1].Name], ты тоже всю ночь толкалась." if Line != "toss":
                        $ Line = "toss"

                "[Party[1].Name], тебе нужно научиться спать на своей стороне." if Line == "toss":
                        $ Line = "turn"
                "[Party[1].Name], тебе тоже нужно научиться спать на своей стороне." if Line != "toss":
                        $ Line = "turn"

            if not Party[1].Sleep and Line == "nice":
                    if Party[1] is RogueX:
                            $ Party[1].Blush = 1
                            if not Player.Male:
                                ch_r "Ах, ты такая милая, [RogueX.Petname]."
                            else:
                                ch_r "Ах, ты такой милый, [RogueX.Petname]."
                            ch_r "Я бы хотела повторить."
                            ch_r "И, эм, с тобой тоже, [Party[1].Name]."
                    elif Party[1] is KittyX:
                            $ Party[1].Blush = 2
                            ch_k "Ага, мне[KittyX.like]тоже понравилось."
                            $ Party[1].Blush = 1
                            ch_k "Я бы[KittyX.like]не прочь повторить."
                            $ Party[1].Blush = 2
                            ch_k "Ну знаешь, как - нибудь. . . "
                            $ Party[1].Blush = 1
                            ch_k "И[KittyX.like]с тобой тоже, [Party[1].Name]."
                    elif Party[1] is EmmaX:
                            $ Party[1].FaceChange("smile",1)
                            if Player.Male or "girltalk" in EmmaX.History:
                                    ch_e "Ты безнадежна, [EmmaX.Petname]."
                            else:
                                    ch_e "Ты безнадежный романтик, [EmmaX.Petname]."
                            $ Party[1].FaceChange("smile",2,Eyes="side")
                            ch_e "Полагаю, что тоже могу стать немного безнадежной. . ."
                            ch_e "Ты знаешь о чем я говорю, [Party[1].Name]."
                    elif Party[1] is LauraX:
                            $ LauraX.FaceChange("confused",1)
                            ch_l "Ох. . ."
                            $ Party[1].FaceChange("surprised",2,Brows="confused")
                            if not Player.Male:
                                ch_l "Да, и мне тоже, раз уж ты сама об этом заговорила. . ."
                            else:
                                ch_l "Да, и мне тоже, раз уж ты сам об этом заговорил. . ."
                            $ Party[1].FaceChange("confused",1)
                            ch_l "Да."
                            ch_l "Странно, правда, [Party[1].Name]?"
                    elif Party[1] is JeanX:
                            $ Party[1].FaceChange("confused",1)
                            ch_j "А? . ."
                            ch_j "О, да. . . все было супер. . ."
                            $ Party[1].FaceChange("smile",1)
                    elif Party[1] is StormX:
                            $ Party[1].FaceChange("smile",1)
                            ch_s "Что ж, да, было приятно спать рядом с тобой, [StormX.Petname]."
                            $ Party[1].FaceChange("smile",2,Eyes="leftside")
                            ch_s "Я думаю, мы должны взять это в привычку. . ."
                            $ Party[1].FaceChange("smile",1)
                    elif Party[1] is JubesX:
                            $ Party[1].FaceChange("smile",1)
                            ch_v "Ага, мне тоже понравилось. . ."
                            $ Party[1].FaceChange("sad",1)
                            ch_v "Я не очень-то много сплю с тех пор, как. . ."
                            $ Party[1].FaceChange("sadside",1)
                            ch_v ". . . изменилась."
                            $ Party[1].FaceChange("smile",1)
                            ch_v "Приятно, когда кто-то остается со мной. . ."
                    elif Party[1] is GwenX:
                            $ Party[1].FaceChange("sadside",1)
                            ch_g "Когда я только попала сюда, я не знала, как все обернется. . ."
                            $ Party[1].FaceChange("smile",1)
                            ch_g "Сейчас я чувствую себя намного комфортнее. . ."
                    elif Party[1] is BetsyX:
                            $ Party[1].FaceChange("smile",1)
                            ch_b "Это было замечательно, [BetsyX.Petname]."
                            $ Party[1].FaceChange("sly",2,Eyes="leftside")
                            ch_b "Мы должны взять это в привычку. . ."
                            $ Party[1].FaceChange("smile",1)
                    elif Party[1] is DoreenX:
                            $ Party[1].FaceChange("smile",1)
                            ch_d "Оу, это так мило."
                            $ Party[1].FaceChange("sly",2,Eyes="leftside")
                            ch_d "Надо будет как-нибудь снова повторить. . ."
                            $ Party[1].FaceChange("smile",1)
                    elif Party[1] is WandaX:
                            $ Party[1].FaceChange("smile",1)
                            ch_w "Давненько я ни с кем не спала."
                            $ Party[1].FaceChange("sly",1,Eyes="leftside")
                            ch_w "Возможно, нам стоит делать это почаще. . ."
                            $ Party[1].FaceChange("smile",1)


            elif Line == "toss":
                        $ Party[1].Blush = 1
                        if ApprovalCheck(Party[1], 800, "L") or ApprovalCheck(Party[1], 1200):
                                $ Party[1].FaceChange("bemused")
                                call AnyLine(Party[1],"Хмм?")
                        else:
                                $ Party[1].FaceChange("angry")
                                call AnyLine(Party[1],"!!!")
                        if Party[1].Sleep < 5:
                                if Party[1] is RogueX:
                                        ch_r "Ну, как будто ты не знаешь, что для меня это все в новинку. . ."
                                elif Party[1] is KittyX:
                                        ch_k "Я не специально. . ."
                                elif Party[1] is EmmaX:
                                        ch_e "Я давно не спала ни с кем рядом."
                                elif Party[1] is LauraX:
                                        ch_l "Смирись."
                                elif Party[1] is JeanX:
                                        ch_j "Это называется \"женская грация.\""
                                elif Party[1] is StormX:
                                        ch_s "Да. . . что ж. . ."
                                        ch_s "у меня много энергии. . ."
                                elif Party[1] is JubesX:
                                        ch_v "Я просто не привыкла спать по ночам. . ."
                                elif Party[1] is GwenX:
                                        ch_g "И где тут веселье? . ."
                                elif Party[1] is BetsyX:
                                        ch_b ". . . Я не. . . \"толкаюсь.\""
                                elif Party[1] is DoreenX:
                                        ch_d "Ну. . . во мне много энергии."
                                elif Party[1] is WandaX:
                                        ch_w "Да?"
                                $ Party[1].Statup("Love", 60, -8)
                                $ Party[1].Statup("Obed", 50, 22)
                                $ Party[1].Statup("Inbt", 50, 22)
                        else:
                                if Party[1] is RogueX:
                                        if not Player.Male:
                                            ch_r "Ну, ты, наверное, уже должна была привыкнуть."
                                        else:
                                            ch_r "Ну, ты, наверное, уже должен был привыкнуть."
                                elif Party[1] is KittyX:
                                        if not Player.Male:
                                            ch_k "Да, но. . . ты уже должна была привыкнуть!"
                                        else:
                                            ch_k "Да, но. . . ты уже должен был привыкнуть!"
                                elif Party[1] is EmmaX:
                                        ch_e "Сейчас у меня нет в планах менять свои привычки."
                                elif Party[1] is LauraX:
                                        ch_l "Да, и так будет всегда."
                                elif Party[1] is JeanX:
                                        ch_j "Смирись."
                                elif Party[1] is StormX:
                                        ch_s "Пожалуй, что так."
                                elif Party[1] is JubesX:
                                        ch_v "Я могла бы просто держаться подальше от кровати. . ."
                                elif Party[1] is GwenX:
                                        ch_g "Или я могла бы просто захватить всю кровать. . ."
                                elif Party[1] is BetsyX:
                                        ch_b "Да-да, мы прекрасно знаем. . ."
                                elif Party[1] is DoreenX:
                                        ch_d "Угум. . ."
                                elif Party[1] is WandaX:
                                        ch_w "Конечно. . ."
            elif Line == "turn":
                        if Party[1].Sleep < 5:
                                $ Party[1].Statup("Love", 80, -8)
                                $ Party[1].Statup("Obed", 50, 40)
                        if ApprovalCheck(Party[1], 500, "O"):
                                $ Party[1].Statup("Love", 80, -2)
                                $ Party[1].Statup("Obed", 90, 5)
                                $ Party[1].FaceChange("normal")
                                if Party[1] is RogueX:
                                        ch_r "Ага, [RogueX.Petname], Я постараюсь."
                                elif Party[1] is KittyX:
                                        ch_k "Ладно, как скажешь."
                                elif Party[1] is EmmaX:
                                        ch_e "Я попробую."
                                elif Party[1] is LauraX:
                                        ch_l "Ладно."
                                elif Party[1] is JeanX:
                                        ch_j "Вся кровать моя сторона."
                                elif Party[1] is StormX:
                                        ch_s "Я. . . могу попробовать. . ."
                                elif Party[1] is JubesX:
                                        ch_v "Я могла бы просто держаться подальше от кровати. . ."
                                elif Party[1] is GwenX:
                                        ch_g "Или я могла бы просто захватить всю кровать. . ."
                                elif Party[1] is BetsyX:
                                        ch_b "\"Моя сторона\" там, где лежу я."
                                elif Party[1] is DoreenX:
                                        ch_d "Оу, но мне нравится прижиматься!"
                                elif Party[1] is WandaX:
                                        ch_w "Не хочу. . ."
                                if Party[1].Sleep < 5:
                                        $ Party[1].Statup("Obed", 80, 8)
                        else:
                                $ Party[1].FaceChange("angry")
                                $ Party[1].Statup("Obed", 90, 5)
                                if Party[1] is RogueX:
                                        if not Player.Male:
                                            ch_r "Пфффф, если продолжишь так говорить, будешь спать одна."
                                        else:
                                            ch_r "Пфффф, если продолжишь так говорить, будешь спать один."
                                elif Party[1] is KittyX:
                                        ch_k "Что-то у меня поубавилось желания спать рядом с тобой."
                                elif Party[1] is EmmaX:
                                        ch_e "Я буду спать как мне заблагорассудится."
                                elif Party[1] is LauraX:
                                        ch_l "Ну, удачи."
                                elif Party[1] is JeanX:
                                        ch_j "Вся кровать моя сторона."
                                elif Party[1] is StormX:
                                        ch_s "Это маловероятно."
                                elif Party[1] is JubesX:
                                        ch_v "Я могла бы просто держаться подальше от кровати. . ."
                                elif Party[1] is GwenX:
                                        ch_g "Или я могла бы просто захватить всю кровать. . ."
                                elif Party[1] is BetsyX:
                                        ch_b "Я сама -решаю-, где \"моя сторона.\""
                                elif Party[1] is DoreenX:
                                        ch_d "Как грубо."
                                elif Party[1] is WandaX:
                                        ch_w "Я не привыкла делиться. . ."
                                if Party[1].Sleep < 5:
                                        $ Party[1].Statup("Inbt", 35, 20)

            $ Party[1].Blush = 0
        #end second girl's lines


        if len(Party) >= 2:
                $ Party[1].Sleep += 1
                #$ Party[1].DrainWord("sleepover",1,1,1)                                #no longer necessary?
                #call Girls_Schedule([Party[1]],2) #forces clothing pick                #no longer necessary?
        $ Party[0].Sleep += 1
        #$ Party[0].DrainWord("sleepover",1,1,1)                                        #no longer necessary?
        #call Girls_Schedule([Party[0]],2) #forces clothing pick                        #no longer necessary?

        # Removes faux "Wait" changes, resets timing to previous night
        $ Time_Count = 3
        $ Current_Time = Time_Options[(Time_Count)]
        $ Day -= 1

        if Weekday == 0:
            $ Weekday = 6
        else:
            $ Weekday -= 1

        $ DayofWeek = Week[Weekday]

        call Wait                                                                       #Wait added here?

        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                if "leaving" in BX.RecentActions or BX.Loc == bg_current:
                        #should add to the party any girls who are staying in the room for the morning
                        #or who were in the room but are leaving
                        Party.append(BX)
                        BX.Loc = bg_current
                        if "leaving" in BX.RecentActions:
                            BX.RecentActions.remove("leaving")
                if "morningwood" in BX.Traits:
                        #if a morning wood event happened, apply these traits to them
                        BX.RecentActions.append("blow")
                        BX.DailyActions.append("blow")
                        BX.DailyActions.append("morningwood")
                        BX.Traits.remove("morningwood")

        #fix add sex option here

        if Party:
            $ Party[0].FaceChange("normal")
            $ Party[0].OutfitChange(6,Changed = 1)

            if len(Party) >= 2:
                    $ Party[1].FaceChange("normal")
                    $ Party[1].OutfitChange(6,Changed = 1)
                    "Девушки переодеваются в повседневную одежду."
            else:
                    "[Party[0].Name] переодевается в повседневную одежду."
        $ Party = []

#        $ BO = Party[:]
#        while BO:
#                $ Party.remove(BO[0])
#                call Girls_Schedule([BO[0]])
#                $ BO.remove(BO[0])

        call Girls_Location
        return

# end Event Sleepover / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# start Event Morning Wood / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start Morning Wood Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Morningwood_Check(Girls=[0,-3],D20=0): #rkeljsvgbdw
        #This element sends player to the Morningwood event or returns them
        #it is called from Sleepover_Morning

        $ D20 = renpy.random.randint(0,3)
        $ Line = 0

        if len(Party) >= 2:
                #builds a modifier for how the girls like each other
                if Party[0].GirlLikeCheck(Party[1]) >= 900:
                        # If the first girl really likes the second
                        $ Girls[0] = 2
                elif Party[0].GirlLikeCheck(Party[1]) >= 750:
                        # If the first girl kinda likes the second
                        $ Girls[0] = 0
                elif Party[0].GirlLikeCheck(Party[1]) <= 400:
                        # If the first girl really hates the second
                        $ Girls[0] = 2
                else:
                        $ Girls[0] = 0

                if Party[1].GirlLikeCheck(Party[0]) >= 900:
                        # If the second girl really likes the first
                        $ Girls[1] = 2
                elif Party[1].GirlLikeCheck(Party[0]) >= 750:
                        # If the second girl kinda likes the first
                        $ Girls[1] = 0
                elif Party[1].GirlLikeCheck(Party[0]) <= 400:
                        # If the second girl really hates the first
                        $ Girls[1] = -5
                else:
                        $ Girls[1] = -3
        else:
                        $ Girls[0] -= 2

        #checks if Primary girl wants to do it
        if "chill" in Party[0].Traits:
                #if you've told her to chill, she stops here.
                $ Girls[0] = 0
        else:
                if Party[0].Blow >= 5 or ApprovalCheck(Party[0], 900, "I"):
                        $ Girls[0] += 3
                elif Party[0].Blow and ApprovalCheck(Party[0], 900):
                        $ Girls[0] += 2
                elif ApprovalCheck(Party[0], 1400):
                        $ Girls[0] += 2
                elif Party[0].Blow or ApprovalCheck(Party[0], 900):
                        $ Girls[0] += 1

                if "hungry" in Party[0].Traits and D20 >= 2:
                        #if she likes cum and gets a 50-70 result
                        $ Girls[0] += 2
                if Party[0].Thirst >= 60:
                        #if she's horny
                        $ Girls[0] += 2
                elif Party[0].Thirst >= 30:
                        #if she's horny
                        $ Girls[0] += 1
                if Party[0].Lust >= 50:
                        #if she's horny
                        $ Girls[0] += 1
                if Party[0].SEXP <= 15:
                        #if she's inexperienced
                        $ Girls[0] -= 1
                #end first girls

                if Girls[1] >= 0:
                        # if the other girl quite likes her
                        $ Girls[0] += 1

        #minimum: -1 likely: 3 maximum: 11
#        if WandaX in Party:
#                 #remove when new girl has a BJ animation                           #remove when new girl has a BJ animation
#                if len(Party) >= 2:
#                        $ Line = "no"
#                else:
#                        return
        if Girls[0] >= D20:
                $ Line = "yes"


        #end first girl check, Girls[0] maybe "yes," maybe 0

        if len(Party) >= 2:
                if Party[1].Blow >= 5 or ApprovalCheck(Party[1], 900, "I"):
                        $ Girls[1] += 3
                elif Party[1].Blow and ApprovalCheck(Party[1], 900):
                        $ Girls[1] += 2
                elif ApprovalCheck(Party[1], 1400):
                        $ Girls[1] += 2
                elif Party[1].Blow or ApprovalCheck(Party[1], 900):
                        $ Girls[1] += 1

                if "hungry" in Party[1].Traits and D20 >= 2:
                        #if she likes cum and gets a 50-70 result
                        $ Girls[1] += 2
                if Party[1].Thirst >= 60:
                        #if she's horny
                        $ Girls[1] += 2
                elif Party[1].Thirst >= 30:
                        #if she's horny
                        $ Girls[1] += 1
                if Party[1].Lust >= 50:
                        #if she's horny
                        $ Girls[1] += 1
                if Party[1].SEXP <= 15:
                        #if she's inexperienced
                        $ Girls[1] -= 1
                #end second girls

                if Girls[0] >= 0:
                        # if the other girl quite likes her
                        $ Girls[1] += 1

                #minimum: -6 likely: 2 maximum: 11
#                if Party[1] is JubesX:
#                        #remove when Jubes is into it
#                        if Girls[1] >= (D20 + 1):# 1-4
#                                $ Line = "other"
#                        elif Girls[1] <= -1:
#                                $ Line = "no"
                if Girls[1] >= (D20 + 1):# 1-4
                        if Line == "Да": #if the first girl agreed
                                $ Line = "double"
                        else:
                                $ Line = "other"
                elif Girls[1] <= -1:
                        $ Line = "no"
                #else: stays "yes"

                if Line == "other" and Party[0].GirlLikeCheck(Party[1]) >= 500 and "chill" not in Party[1].Traits:
                    # If Girl 1 wasn't into it, but liked girl 2 and girl 2 was, swap them
                    $ Party.reverse()
                    $ Girls[0] = "yes"
                    $ Girls[1] = 0

        #End second girl check, Girls[1] maybe "double," maybe "no", maybe 0


        if Line:
            # if Line has changed from 0


            if not Player.Male and "girltalk" not in Party[0].History:
                    #will not do this if player is female and hasn't "had the talk" yet
                    return
            if Line == "Нет":
                        # second girl ruins it
                        "Вы просыпаетесь под какой-то шум."
                        if Party[1] is RogueX:
                                ch_r "[Party[0].Name], убирайся!"
                        elif Party[1] is KittyX:
                                "Вы слышите тихую ругань и глухой стук, словно что-то тяжелое падает с кровати."
                                call AnyLine(Party[0],"Ай!")
                                ch_k "Так тебе и надо, [Party[0].Name]."
                        elif Party[1] is EmmaX:
                                ch_e "Отойди от [Player.Name_rod], [Party[0].Name]."
                        elif Party[1] is LauraX:
                                ch_l "Отвали, [Party[0].Name]."
                        elif Party[1] is JeanX:
                                ch_j "Отвали, [Party[0].Name]."
                        elif Party[1] is StormX:
                                ch_s "[Party[0].Name], кое-кто пытается поспать. . ."
                        elif Party[1] is JubesX:
                                if not Player.Male:
                                    ch_v "Эй, он пытается поспать, прекрати. . ."
                                else:
                                    ch_v "Эй, он пытается поспать, прекрати. . ."
                        elif Party[1] is GwenX:
                                ch_g "Эй. . . прекрати, я тут, как бы, сплю. . ."
                        elif Party[1] is BetsyX:
                                ch_b "Веди себя хорошо, [Party[0].Name]. . ."
                        elif Party[1] is DoreenX:
                                if not Player.Male:
                                    ch_d "Эй! Отойди от нее, [Party[0].Name]. . ."
                                else:
                                    ch_d "Эй! Отойди от него, [Party[0].Name]. . ."
                        elif Party[1] is WandaX:
                                ch_w "Эй, отойди. . ."

                        if Party[0] is RogueX:
                                ch_r "Я не хотела ничего плохого, [Party[1].Name]."
                        elif Party[0] is KittyX:
                                "Вы слышите тихую ругань и глухой стук, словно что-то тяжелое падает с кровати."
                                call AnyLine(Party[0],"Ай!")
                                ch_k "Все настроение испортила."
                        elif Party[0] is EmmaX:
                                ch_e "Не будь занудой, дорогая."
                        elif Party[0] is LauraX:
                                ch_l "Ладно, как скажешь."
                        elif Party[0] is JeanX:
                                ch_j "Отвали. . ."
                                "-Вшух-"
                        elif Party[0] is StormX:
                                ch_s "Я не собиралась тебя будить. . ."
                        elif Party[0] is JubesX:
                                ch_v "Ох, ладно. . ."
                        elif Party[0] is GwenX:
                                ch_g "Все настроение испортила. . ."
                        elif Party[0] is BetsyX:
                                ch_b "Черт. . ."
                        elif Party[0] is DoreenX:
                                ch_d "Упс."
                        elif Party[0] is WandaX:
                                ch_w "Сучка. . ."
                        if Party[0] is not JeanX:
                                return
            elif Line == "double":
                    # it's a threesome
#                    if not Player.Male and "girltalk" not in Party[1].History:
#                                #will not do this if player is female and hasn't "had the talk" yet
#                                pass
#                    else:
                        if Player.Male:
                                $ Party[1].Offhand = "blow"
                                $ Party[1].RecentActions.append("blow")
                                $ Party[1].DailyActions.append("blow")
                        else:
                                $ Party[1].Offhand = "cun"
                                $ Party[1].RecentActions.append("cun")
                                $ Party[1].DailyActions.append("cun")
                        $ Party[1].DailyActions.append("morningwood")
                        $ Party[1].Traits.append("morningwood")
            # it's a solo act with girl 1
            if Player.Male:
                    $ Trigger = "blow"
                    $ Party[0].RecentActions.append("blow")
                    $ Party[0].DailyActions.append("blow")
            else:
                    $ Trigger = "cun"
                    $ Party[0].RecentActions.append("cun")
                    $ Party[0].DailyActions.append("cun")
            $ Party[0].DailyActions.append("morningwood")
            $ Party[0].Traits.append("morningwood")
            call Sleepover_MorningWood
            #call expression Party[0].Tag + "_SexAct" pass ("morningwood")
            call Sex_Over(0)
            #end "yes"

        else: #Girls[0] = 0
            #neither girl was interested
            pass

        return


# end Morning Wood Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



label Sleepover_MorningWood: #rkeljsvgbdw
        # this label is called from Morningwood_Check, which was called from Sleepover_Morning
        $ Player.AddWord(1,"interruption") #prevents interruption
        call Shift_Focus(Party[0])
        $ Player.Focus = 30
        if Trigger == "blow":
                    ch_u "\"Чмок, чмок, чмок.\""
        else:
                    ch_u "\"Хлюп, хлюп, хлюп.\""

        $ Player.Statup("Focus", 80, 5)
        $ Party[0].Statup("Lust", 80, 5)
        $ Player.DailyActions.append("morningwood")

        $ Partner = Party[1] if len(Party) >= 2 else 0
        #display other girl here if necessary

        $ Player.RecentActions.append("cockout")

        if Partner in TotalGirls:
                $ renpy.show(Partner.Tag+"_Sprite",at_list=[Sprite_Set(900,250)],zorder=75)
#                if Partner is RogueX:
#                        show Rogue_Sprite:
#                            pos (900,250)
                $ Partner.RecentActions.append("threesome")

        $ Party[0].RecentActions.append("blanket")
        if Player.Male:
                call expression Party[0].Tag + "_BJ_Launch"
        else:
                call expression Party[0].Tag + "_CUN_Launch"

        $ Party[0].FaceChange("closed",1)
        if Partner:
                $ Partner.FaceChange("closed",1,Mouth="tongue")

        "Вы ощущаете нечто приятное. . ."
        if Trigger == "blow":
                if Partner:
                    ch_u "\"Чмок, чмок, чмок.\" \n \ \"Чмок, чмок, чмок.\""
                else:
                    ch_u "\"Чмок, чмок, чмок.\""
        else:
                if Partner:
                    ch_u "\"Хлюп, хлюп, хлюп.\" \n \ \"Чмок, чмок, чмок.\""
                else:
                    ch_u "\"Хлюп, хлюп, хлюп.\""
        $ Player.Statup("Focus", 80, 5)
        $ Party[0].Statup("Lust", 80, 5)

        "В области паха. . ."
        if Trigger == "blow":
                if Partner:
                    ch_u "\"Чмок, чмок, чмок.\" \n \ \"Чмок, чмок, чмок.\""
                else:
                    ch_u "\"Чмок, чмок, чмок.\""
        else:
                if Partner:
                    ch_u "\"Хлюп, хлюп, хлюп.\" \n \ \"Чмок, чмок, чмок.\""
                else:
                    ch_u "\"Хлюп, хлюп, хлюп.\""
        $ Player.Statup("Focus", 80, 10)
        $ Party[0].Statup("Lust", 80, 5)

        "Вы открываете глаза. . ."

        hide NightMask onlayer nightmask
        hide blackscreen onlayer black

        $ Speed = 3
        $ Count = 3
        $ Line = 0
        call Seen_First_Peen(Party[0],Partner,1,1,1)
        while Count > 0:
                #Looping portion
                $ Player.Statup("Focus", 80, 10)
                $ Party[0].Statup("Lust", 80, 5)
                if Partner:
                        $ Partner.Statup("Lust", 80, 5)
                menu:
                    "Лежать тихо":
                        if Count > 2:
                            if Partner:
                                "Вы решаете позволить им делать свое дело, вы притворяетесь, что вы все еще спите."
                            else:
                                "Вы решаете позволить ей делать свое дело, вы притворяетесь, что вы все еще спите."
                        elif Count > 1:
                                "It does feel nice. . ."
                        elif Count == 1:
                            if Partner:
                                "Вы не хотите их прерывать. . ."
                            else:
                                "Вы не хотите ее прерывать. . ."
                        else:
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 < 15:
                                        call Morning_Finish
                                        if "secretwood" in Player.DailyActions:
                                                #returns to previous state if finished to completion.
                                                return
                        if Trigger == "blow":
                                call AnyLine(Party[0],"\"Чмок, чмок, чмок.\"")
                        else:
                                call AnyLine(Party[0],"\"Хлюп, хлюп, хлюп.\"")
                        if Partner:
                                call AnyLine(Party[1],"\"Чмок, чмок, чмок.\"")
                        ". . ."
                    "Эм. . . [Party[0].Pet], что ты делаешь?":
                        $ Line = "question"
                        $ Count = 1
                    "Как же классно. . .":
                        $ Line = "praise"
                        $ Count = 1
                    "Эй, хватит!":
                        $ Line = "no"
                        $ Count = 1
                $ Count -= 1

        $ Speed = 1
        $ Party[0].Blush = 1
        if Player.Male:
            if Partner:
                "[Party[0].Name] отрывается от члена, [Party[1].Name] также отстраняется."
                $ Party[1].Offhand = 0
            else:
                "[Party[0].Name] отрывается от члена."
        else:
            if Partner:
                "[Party[0].Name] отстраняется, оставляя после себя немного слюны, [Party[1].Name] следует ее примеру."
                $ Party[1].Offhand = 0
            else:
                "[Party[0].Name] отстраняется, оставляя после себя немного слюны."
        if Line == "question":
                        $ Party[0].FaceChange("smile",1)
                        if Party[0] is RogueX:
                                ch_r "Уж точно не занимаюсь ерундой, [RogueX.Petname]."
                        elif Party[0] is KittyX:
                                ch_k "А разве[KittyX.like]не видно?"
                        elif Party[0] is EmmaX:
                                if not Player.Male:
                                    ch_e "Уверена, что ты сама в состояние догодаться, [EmmaX.Petname]."
                                else:
                                    ch_e "Уверена, что ты сам в состояние догодаться, [EmmaX.Petname]."
                        elif Party[0] is LauraX:
                                ch_l "Догадайся."
                        elif Party[0] is JeanX:
                                $ Party[0].FaceChange("confused",1)
                                $ Speed = 2
                                ch_j ". . ."
                                if Player.Male:
                                        ch_j "У меня туть щлен ва ртьу. . ."
                                else:
                                        ch_j "Я туть как бы щанятьа. . ."
                                ch_j "Можьет уще протрещь глазьа?"
                                $ Speed = 1
                                if Partner:
                                    $ Party[0].Eyes = "leftside"
                                    if not Player.Male:
                                        ch_j "Она умом тронулась?"
                                    else:
                                        ch_j "Он умом тронулся?"
                                $ Party[0].FaceChange("sly",1)
                        elif Party[0] is StormX:
                                ch_s "Я не собиралась тебя будить. . ."
                        elif Party[0] is JubesX:
                                ch_v "Извини, я. . . не завтракала. . ."
                        elif Party[0] is GwenX:
                                ch_g "Разве это не очевидно?"
                        elif Party[0] is BetsyX:
                                ch_b "Я не собиралась нарушать твой сон. . ."
                        elif Party[0] is DoreenX:
                                if not Player.Male:
                                    ch_d "Ну, я не собиралась прятать в тебя орешки. . ."
                                else:
                                    ch_d "Ну, я не собиралась забирать твои \"орешки\". . ."
                        elif Party[0] is WandaX:
                                ch_w "Неужели я настолько разучилась это делать? . ."
        elif Line == "praise":
                        $ Party[0].FaceChange("smile",1)
                        $ Party[0].Statup("Love", 90, 5)
                        $ Party[0].Statup("Obed", 50, 2)
                        $ Party[0].Statup("Inbt", 60, 2)
                        if Party[0] is RogueX:
                                ch_r "Ммм, с удовольствием, [RogueX.Petname]."
                        elif Party[0] is KittyX:
                                ch_k "Ммм, хихи."
                        elif Party[0] is EmmaX:
                                ch_e "Лишняя практика не помешает, [EmmaX.Petname]."
                        elif Party[0] is LauraX:
                                ch_l "Да, наверное?"
                        elif Party[0] is JeanX:
                                ch_j "Ха."
                        elif Party[0] is StormX:
                                ch_s "Конечно. . ."
                        elif Party[0] is JubesX:
                                ch_v "Мне это очень нравится. . ."
                        elif Party[0] is GwenX:
                                ch_g "Ха, спасибо . ."
                        elif Party[0] is BetsyX:
                                ch_b "Я уж думала, ты будешь жаловаться. . ."
                        elif Party[0] is DoreenX:
                                $DoreenX.Blush = 2
                                ch_d "Я. . . может быть. . ."
                                $DoreenX.Blush = 1
                        elif Party[0] is WandaX:
                                ch_w "Я подумала, что тебе это может понравиться. . ."
        elif Line == "Нет":
                        $ Party[0].Statup("Love", 90, -3)
                        $ Party[0].Statup("Obed", 50, 2)
                        $ Party[0].Statup("Inbt", 60, -2)
                        $ Speed = 0
                        $ Party[0].FaceChange("angry",1,Brows="confused")
                        if Party[0] is RogueX:
                                 ch_r "Ничего себе \"приветствие,\" когда тут девушка старается сделать тебе приятное!"
                        elif Party[0] is KittyX:
                                 ch_k "И вот {i}это{/i} твое спасибо?!"
                        elif Party[0] is EmmaX:
                                 if not Player.Male:
                                     ch_e "Могла бы хоть немного \"поблагодарить\". . ."
                                 else:
                                     ch_e "Мог бы хоть немного \"поблагодарить\". . ."
                        elif Party[0] is LauraX:
                                 ch_l "А?"
                        elif Party[0] is JeanX:
                                 ch_j "Серьезно? Даже никакого \"спасибо?\""
                        elif Party[0] is StormX:
                                 ch_s "Ох, прости меня за мою бесцеремонность. . ."
                        elif Party[0] is JubesX:
                                 $ Party[0].FaceChange("sad",1,Brows="confused")
                                 ch_v "Прости, прости! Я была немного голодна. . ."
                        elif Party[0] is GwenX:
                                 $ Party[0].FaceChange("confused")
                                 ch_g "Я думала, тебе понравится такое!"
                        elif Party[0] is BetsyX:
                                ch_b "Я ожидала немного больше благодарности. . ."
                        elif Party[0] is DoreenX:
                                ch_d "Ну, я просто подумала, что тебе понравится. . ."
                        elif Party[0] is WandaX:
                                ch_w "Ладно, урок усвоен. \"Никакого веселья.\""
        else: #if it fell through due to time
                        if Party[0] is RogueX:
                                if not Player.Male:
                                    ch_r "Хах, я вижу, ты уже проснулась, [RogueX.Petname]. . ."
                                    ch_r "Ты стала. . . более отзывчивой."
                                else:
                                    ch_r "Хах, я вижу, ты уже проснулся, [RogueX.Petname]. . ."
                                    ch_r "Ты стал. . . более отзывчивым."
                        elif Party[0] is KittyX:
                                ch_k "Ты уже можешь перестать притворяться, [KittyX.Petname]. . ."
                                if not Player.Male:
                                    ch_k "Твой подружка сдала тебя."
                                else:
                                    ch_k "Твой дружок сдал тебя."
                        elif Party[0] is EmmaX:
                                ch_e "Не знаю, кого ты пытаешься обмануть."
                                if not Player.Male:
                                    ch_e "Я знаю, что ты уже проснулась, [EmmaX.Petname]. . ."
                                else:
                                    ch_e "Я знаю, что ты уже проснулся, [EmmaX.Petname]. . ."
                        elif Party[0] is LauraX:
                                if not Player.Male:
                                    ch_l "Ты можешь перестать притворяться мертвой, [LauraX.Petname]. . ."
                                else:
                                    ch_l "Ты можешь перестать притворяться мертвым, [LauraX.Petname]. . ."
                                ch_l "Это самый известный трюк из учебника."
                        elif Party[0] is JeanX:
                                if not Player.Male:
                                    ch_j "Ты уже можешь перестать притворяться спящей. . ."
                                    ch_j "Я не могу прочитать твои мысли, но я могу прочитать твою киску. . ."
                                else:
                                    ch_j "Ты уже можешь перестать притворяться спящим. . ."
                                    ch_j "Я не могу прочитать твои мысли, но я могу прочитать твой член. . ."
                        elif Party[0] is StormX:
                                ch_s "Я не собиралась тебя будить, но, похоже, все-таки разбудила."
                        elif Party[0] is JubesX:
                                ch_v "О, доброе утро, соня. . ."
                        elif Party[0] is GwenX:
                                if not Player.Male:
                                    ch_g "Кхм. . . Ты проснулась, м?"
                                else:
                                    ch_g "Кхм. . . Ты проснулся, м?"
                        elif Party[0] is BetsyX:
                                ch_b "Ты же понимаешь, что тебе так никого не обмануть, [BetsyX.Petname]. . ?"
                        elif Party[0] is DoreenX:
                                ch_d "Я почувствовала движение. . ."
                        elif Party[0] is WandaX:
                                ch_w "Просыпайся, просыпайся. . ."
        #end first response phase

        if Partner:
                #second girl's lines
                if Line == "question":
                                $ Party[1].FaceChange("smile",1)
                elif Line == "praise":
                                $ Party[1].Statup("Love", 90, 3)
                                $ Party[1].Statup("Obed", 50, 2)
                                $ Party[1].Statup("Inbt", 60, -2)
                                $ Party[1].FaceChange("smile",1)
                elif Line == "Нет":
                                $ Party[1].Statup("Love", 90, -3)
                                $ Party[1].Statup("Obed", 50, 2)
                                $ Party[1].Statup("Inbt", 60, -2)
                                $ Party[1].FaceChange("angry",1,Brows="confused")

                if Partner is RogueX:
                        if "blow" in Partner.RecentActions or "cun" in Partner.RecentActions:
                            ch_r "Я ничего не знаю, [Partner.Petname]."
                        else:
                            "[Partner.Name] переворачивается в постели."
                            ch_r "Не останавливайтесь из-за меня, [RogueX.Petname]."
                elif Partner is KittyX:
                        if "blow" in Partner.RecentActions or "cun" in Partner.RecentActions:
                            ch_k "Хм. . ."
                        else:
                            "[Partner.Name] переворачивается в постели."
                            ch_k "Похоже, вам весело . . ."
                elif Partner is EmmaX:
                        if "blow" in Partner.RecentActions or "cun" in Partner.RecentActions:
                            ch_e "Что ж. . ."
                        else:
                            "[Partner.Name] переворачивается в постели."
                            ch_e "Ох, только не прерывайтесь из-за меня."
                elif Partner is LauraX:
                        if "blow" in Partner.RecentActions or "cun" in Partner.RecentActions:
                            ch_l "Хмм. . ."
                        else:
                            if not Player.Male:
                                "[Partner.Name] переворачивается в постели и начинает смотреть на вас обеих."
                            else:
                                "[Partner.Name] переворачивается в постели и начинает смотреть на вас обоих."
                elif Partner is JeanX:
                        if "blow" in Partner.RecentActions or "cun" in Partner.RecentActions:
                            ch_j "Хмм. . ."
                        else:
                            if not Player.Male:
                                "[JeanX.Name] переворачивается на другой бок и начинает смотреть на вас обеих."
                            else:
                                "[JeanX.Name] переворачивается на другой бок и начинает смотреть на вас обоих."
                elif Partner is StormX:
                        if "blow" in Partner.RecentActions or "cun" in Partner.RecentActions:
                            ch_s "Хм?"
                        else:
                            "[Partner.Name] поворачивается в постели."
                            ch_s "Ах."
                            ch_s "Продолжайте. . ."
                elif Partner is JubesX:
                        if "blow" in Partner.RecentActions or "cun" in Partner.RecentActions:
                            ch_v "Мммм. . ."
                        else:
                            "[Partner.Name] поворачивается в постели."
                            ch_v "Я просто подумала, что это выглядит забавно. . ."
                elif Partner is GwenX:
                        if "blow" in Partner.RecentActions or "cun" in Partner.RecentActions:
                            ch_g "Мммм. . ."
                        else:
                            "[Partner.Name] поворачивается в постели."
                            ch_g "Мне просто захотелось посмотреть. . ."
                elif Partner is BetsyX:
                        if "blow" in Partner.RecentActions or "cun" in Partner.RecentActions:
                            ch_b "Мммм. . ."
                        else:
                            "[Partner.Name] поворачивается в постели."
                            ch_b "Продолжайте. . ."
                elif Partner is DoreenX:
                        if "blow" in Partner.RecentActions or "cun" in Partner.RecentActions:
                            ch_d "Что ж. . ."
                        else:
                            "[Partner.Name] поворачивается в постели."
                            ch_d "Пожалуй. . . можете заниматься всем, чем хотите. . . я не против."
                elif Partner is WandaX:
                        if "blow" in Partner.RecentActions or "cun" in Partner.RecentActions:
                            ch_w "Хех. . ."
                        else:
                            "[Partner.Name] поворачивается в постели."
                            ch_w "Что ж. . . занимайтесь всем, чем хотите. . ."

        #start second question phase
        menu:
            "В общем, эм. . . может, продолжим?":
                    if Line != "Нет":
                            #assuming you weren't rude
                            $ Party[0].FaceChange("smile",1)
                            if Party[0] is RogueX:
                                    ch_r "С удовольствием."
                            elif Party[0] is KittyX:
                                    ch_k "Хихи, мммм. . ."
                            elif Party[0] is EmmaX:
                                    ch_e "Если ты настаиваешь. . ."
                            elif Party[0] is LauraX:
                                    ch_l "Неплохая идея. . ."
                            elif Party[0] is JeanX:
                                    ch_j "Конечно."
                            elif Party[0] is StormX:
                                    ch_s "С удовольствием. . ."
                            elif Party[0] is JubesX:
                                    ch_v "Конечно."
                            elif Party[0] is GwenX:
                                    ch_g "Ага!"
                            elif Party[0] is BetsyX:
                                    ch_b "Я думала, ты никогда не попросишь."
                            elif Party[0] is DoreenX:
                                    ch_d "Конечно, мы продолжим!"
                            elif Party[0] is WandaX:
                                    ch_w "Меня не нужно просить дважды."
                    elif Line == "no" and ApprovalCheck(Party[0], 1750):
                            #if you were a dick but she's ok
                            $ Party[0].Statup("Obed", 80, 3)
                            $ Party[0].Statup("Inbt", 60, 2)
                            $ Party[0].FaceChange("bemused")
                            if Party[0] is RogueX:
                                    ch_r "Тебе повезло, что ты мне очень нравишься. . ."
                            elif Party[0] is KittyX:
                                    ch_k "Чт-? Ну. . . наверное, можно. . ."
                            elif Party[0] is EmmaX:
                                    if not Player.Male:
                                        ch_e "Постарайся на этот раз не быть дурочкой. . ."
                                    else:
                                        ch_e "Постарайся на этот раз не быть придурком. . ."
                            elif Party[0] is LauraX:
                                    ch_l "Ладно. . ."
                            elif Party[0] is JeanX:
                                    $ Party[0].Statup("Obed", 90, 3)
                                    ch_j "Как скажешь."
                            elif Party[0] is StormX:
                                    ch_s ". . ."
                                    ch_s "Пожалуй, я должна закончить то, что начала."
                            elif Party[0] is JubesX:
                                    ch_v "Мне не нужно повторять дважды."
                            elif Party[0] is GwenX:
                                    ch_g ". . . конечно, наверное."
                            elif Party[0] is BetsyX:
                                    ch_b "Ладно, я попытаюсь успокоиться и продолжить. . ."
                            elif Party[0] is DoreenX:
                                    ch_d "Ну, ладно."
                            elif Party[0] is WandaX:
                                    ch_w "Конечно. . ."
                            $ Line = "maybe"
                    else:
                            #if you were a dick and she's not ok with that
                            $ Party[0].FaceChange("angry",1)
                            if Party[0] is RogueX:
                                    if not Player.Male:
                                        ch_r "Ну уж нет, ты была слишком груба со мной."
                                        ch_r "Ты и сама прекрасно справишься."
                                    else:
                                        ch_r "Ну уж нет, ты был слишком груб со мной."
                                        ch_r "Ты и сам прекрасно справишься."
                            elif Party[0] is KittyX:
                                    ch_k "Ну уж нет!"
                                    if not Player.Male:
                                        ch_k "Сама о себе позаботься."
                                    else:
                                        ch_k "Сам о себе позаботься."
                            elif Party[0] is EmmaX:
                                    ch_e "Я не потерплю к себе грубого отношения."
                                    ch_e "Думаю, ты и без меня прекрасно справишься."
                            elif Party[0] is LauraX:
                                    ch_l "Нет."
                            elif Party[0] is JeanX:
                                    ch_j "Ха! Нет."
                            elif Party[0] is StormX:
                                    ch_s "Теперь у меня пропала вся мотивация. . ."
                            elif Party[0] is JubesX:
                                    ch_v "Нет, думаю, я получила достаточно. . ."
                            elif Party[0] is GwenX:
                                    ch_g ". . . нет, я так не думаю."
                            elif Party[0] is BetsyX:
                                    ch_b "У меня есть дела поважнее."
                            elif Party[0] is DoreenX:
                                    ch_d "Я. . . не обязана!"
                            elif Party[0] is WandaX:
                                    ch_w "Нет, нет, я все понимаю. Больше не буду тебя беспокоить. . ."
            "Может, займемся чем-то более интересным?":
                    if Line != "Нет":
                            #assuming you weren't rude
                            $ Party[0].FaceChange("sexy",1)
                            if Party[0] is RogueX:
                                    ch_r "Оох, ты о чем?"
                            elif Party[0] is KittyX:
                                    ch_k "Возмооожноо. . . например, чем?"
                            elif Party[0] is EmmaX:
                                    ch_e "Возможно. . . что ты предлагаешь?"
                            elif Party[0] is LauraX:
                                    ch_l "Да, наверное?"
                            elif Party[0] is JeanX:
                                    ch_j "Ты прямо читаешь мои мысли. . ."
                            elif Party[0] is StormX:
                                    ch_s "С удовольствием. . ."
                            elif Party[0] is JubesX:
                                    ch_v "Конечно. . ."
                            elif Party[0] is GwenX:
                                    ch_g "Ооо, удиви меня!"
                            elif Party[0] is BetsyX:
                                    ch_b "Можешь попробовать заинтересовать меня. . ."
                            elif Party[0] is DoreenX:
                                    ch_d "Ооо, например?"
                            elif Party[0] is WandaX:
                                    ch_w "Например?"
                            $ Line = "sex"
                    elif Line == "no" and ApprovalCheck(Party[0], 1650):
                            #if you were a dick but she's ok
                            $ Party[0].Statup("Obed", 80, 3)
                            $ Party[0].Statup("Inbt", 60, 3)
                            $ Party[0].FaceChange("bemused",1)
                            if Party[0] is RogueX:
                                    if not Player.Male:
                                        ch_r "Хоть ты и дурочка, но ты милая."
                                    else:
                                        ch_r "Хоть ты и придурок, но милый придурок."
                                    ch_r "Что предлагаешь?"
                            elif Party[0] is KittyX:
                                    ch_k "Ох, так значит у тебя есть {i}какие-то{/i} идеи. . ."
                                    ch_k "Например?"
                            elif Party[0] is EmmaX:
                                    ch_e "Хмм, ладно, вот твой второй шанс, [EmmaX.Petname], что ты предлагаешь?"
                            elif Party[0] is LauraX:
                                    ch_l "Да, наверное?"
                            elif Party[0] is JeanX:
                                    ch_j "О? Пытаешься загладить свою вину?"
                            elif Party[0] is StormX:
                                    ch_s "Полжалуй, можно, если тебе так хочется. . ."
                            elif Party[0] is JubesX:
                                    ch_v "Наверное?"
                            elif Party[0] is GwenX:
                                    if not Player.Male:
                                        ch_g ". . . решила, значит, загладить свою вину. . ."
                                    else:
                                        ch_g ". . . решил, значит, загладить свою вину. . ."
                            elif Party[0] is BetsyX:
                                    ch_b "Возможно, я могу уступить."
                            elif Party[0] is DoreenX:
                                    ch_d "Я даже не знаю, может я и согласна?"
                            elif Party[0] is WandaX:
                                    ch_w "Я даже не знаю, какие у тебя есть предложения?"
                            $ Line = "sex"
                    else:
                            #if you were a dick and she's not ok with that
                            $ Party[0].FaceChange("angry",1)
                            if Party[0] is RogueX:
                                    if not Player.Male:
                                        ch_r "Ну уж нет, ты была слишком груба со мной."
                                        ch_r "Ты и сама прекрасно справишься."
                                    else:
                                        ch_r "Ну уж нет, ты был слишком груб со мной."
                                        ch_r "Ты и сам прекрасно справишься."
                            elif Party[0] is KittyX:
                                    ch_k "Ну уж нет!"
                                    if not Player.Male:
                                        ch_k "Сама о себе позаботься."
                                    else:
                                        ch_k "Сам о себе позаботься."
                            elif Party[0] is EmmaX:
                                    ch_e "Я не потерплю к себе грубого отношения."
                                    ch_e "Думаю, ты и без меня прекрасно справишься."
                            elif Party[0] is LauraX:
                                    ch_l "Нет."
                            elif Party[0] is JeanX:
                                    if not Player.Male:
                                        ch_j "Ну, я -предлагала,- но ты решила побыть сучкой."
                                    else:
                                        ch_j "Ну, я -предлагала,- но ты решил побыть мудаком."
                            elif Party[0] is StormX:
                                    ch_s "Я больше не в настроении."
                            elif Party[0] is JubesX:
                                    ch_v "Ахаха, нет. . ."
                            elif Party[0] is GwenX:
                                    ch_g "Точно не сейчас."
                            elif Party[0] is BetsyX:
                                    ch_b "Может я бы согласилась. . ."
                                    if not Player.Male:
                                        ch_b "Но ты, увы, испортила мне настроение."
                                    else:
                                        ch_b "Но ты, увы, испортил мне настроение."
                            elif Party[0] is DoreenX:
                                    ch_d "Нет!"
                            elif Party[0] is WandaX:
                                    ch_w "Нет, нет, я все понимаю. Больше не буду тебя беспокоить. . ."
            "Извини-извини, пожалуйста, продолжай." if Line == "Нет":
                    if ApprovalCheck(Party[0], 1450):
                            #if you were a dick but she's ok
                            $ Party[0].Statup("Love", 90, 3)
                            $ Party[0].Statup("Obed", 80, 2)
                            $ Party[0].Statup("Inbt", 60, 4)
                            $ Party[0].FaceChange("bemused",1)
                            if Party[0] is RogueX:
                                    ch_r "Хорошо, раз уж ты так мило просишь. . ."
                            elif Party[0] is KittyX:
                                    ch_k "Думаю, я могу простить тебя. . ."
                            elif Party[0] is EmmaX:
                                    ch_e "Хорошо, я дам тебе еще один шанс."
                            elif Party[0] is LauraX:
                                    ch_l "Да, наверное?"
                            elif Party[0] is JeanX:
                                    ch_j ". . . ладно."
                            elif Party[0] is StormX:
                                    ch_s "Хорошо."
                            elif Party[0] is JubesX:
                                    ch_v "Да, конечно."
                            elif Party[0] is GwenX:
                                    ch_g "Будет сделано!"
                            elif Party[0] is BetsyX:
                                    ch_b "Что ж, если ты так умоляешь. . ."
                            elif Party[0] is DoreenX:
                                    ch_d "Ну. . . наверное, можно. . ."
                            elif Party[0] is WandaX:
                                    ch_w "Пожалуй, можно. . ."
                            $ Line = "maybe"
                    else:
                            #if you were a dick and she's not ok with that
                            $ Party[0].Statup("Love", 90, 2)
                            $ Party[0].FaceChange("angry",1)
                            if Party[0] is RogueX:
                                    if not Player.Male:
                                        ch_r "Ну уж нет, ты была слишком груба со мной."
                                        ch_r "Ты и сама прекрасно справишься."
                                    else:
                                        ch_r "Ну уж нет, ты был слишком груб со мной."
                                        ch_r "Ты и сам прекрасно справишься."
                            elif Party[0] is KittyX:
                                    ch_k "Ну уж нет!"
                                    if not Player.Male:
                                        ch_k "Сама о себе позаботься."
                                    else:
                                        ch_k "Сам о себе позаботься."
                            elif Party[0] is EmmaX:
                                    ch_e "Я не потерплю к себе грубого отношения."
                                    ch_e "Думаю, ты и без меня прекрасно справишься."
                            elif Party[0] is LauraX:
                                    ch_l "Нет."
                            elif Party[0] is JeanX:
                                    ch_j "Хорошая попытка."
                            elif Party[0] is StormX:
                                    ch_s "Я больше не в настроении."
                            elif Party[0] is JubesX:
                                    ch_v "Нее, хватит. . ."
                            elif Party[0] is GwenX:
                                    ch_g "Нет-нет, я услышала тебя в первый раз. . ."
                            elif Party[0] is BetsyX:
                                    ch_b "По крайней мере, ты осознаешь свою ошибку."
                            elif Party[0] is DoreenX:
                                    if not Player.Male:
                                        ch_d "Ну, как ты и сказал, \"извини.\""
                                    else:
                                        ch_d "Ну, как ты и сказала, \"извини.\""
                            elif Party[0] is WandaX:
                                    ch_w "Нет, нет, я все понимаю. Больше не буду тебя беспокоить. . ."
            "Извини, мы могли бы заняться чем-то другим." if Line == "Нет":
                    if ApprovalCheck(Party[0], 1350):
                            #if you were a dick but she's ok
                            $ Party[0].Statup("Love", 90, 3)
                            $ Party[0].FaceChange("sexy",1)
                            if Party[0] is RogueX:
                                    ch_r "Хорошо, раз уж ты так мило просишь. . ."
                                    ch_r "Что предлагаешь?"
                            elif Party[0] is KittyX:
                                    ch_k "Думаю, можно. . ."
                                    ch_k "Чем займемся?"
                            elif Party[0] is EmmaX:
                                    ch_e "Ммм, я подумаю. . ."
                            elif Party[0] is LauraX:
                                    ch_l "Да, наверное?"
                            elif Party[0] is JeanX:
                                    ch_j ". . . ладно."
                            elif Party[0] is StormX:
                                    ch_s "Я. . . полагаю, что можно."
                            elif Party[0] is JubesX:
                                    ch_v "Конечно. . ."
                            elif Party[0] is GwenX:
                                    ch_g "Ладно, здорово."
                            elif Party[0] is BetsyX:
                                    ch_b "Смотря что предложишь. . ."
                            elif Party[0] is DoreenX:
                                    ch_d "Хорошо. . ."
                            elif Party[0] is WandaX:
                                    ch_w "Например? . ."
                            $ Line = "sex"
                    else:
                            #if you were a dick and she's not ok with that
                            $ Party[0].Statup("Love", 90, 2)
                            $ Party[0].FaceChange("angry",1)
                            if Party[0] is RogueX:
                                    if not Player.Male:
                                        ch_r "Ну уж нет, ты была слишком груба со мной."
                                        ch_r "Ты и сама прекрасно справишься."
                                    else:
                                        ch_r "Ну уж нет, ты был слишком груб со мной."
                                        ch_r "Ты и сам прекрасно справишься."
                            elif Party[0] is KittyX:
                                    ch_k "Ну уж нет!"
                                    if not Player.Male:
                                        ch_k "Сама о себе позаботься."
                                    else:
                                        ch_k "Сам о себе позаботься."
                            elif Party[0] is EmmaX:
                                    ch_e "Я не потерплю к себе грубого отношения."
                                    ch_e "Думаю, ты и без меня прекрасно справишься."
                            elif Party[0] is LauraX:
                                    ch_l "Нет."
                            elif Party[0] is JeanX:
                                    ch_j "Неа, уже слишком поздно."
                            elif Party[0] is StormX:
                                    ch_s "Нет, я больше не в настроении."
                            elif Party[0] is JubesX:
                                    ch_v "Неа. . ."
                            elif Party[0] is GwenX:
                                    ch_g "Ахаха, нет."
                            elif Party[0] is BetsyX:
                                    ch_b "Боюсь, что я вынуждена отказаться."
                            elif Party[0] is DoreenX:
                                    ch_d "Я так не думаю!"
                            elif Party[0] is WandaX:
                                    ch_w "Нет, нет, я все понимаю. Больше не буду тебя беспокоить. . ."
            "Я все не могу отойти ото сна.":
                            $ Party[0].FaceChange("angry",1)
                            if Party[0] is RogueX:
                                    ch_r "Ладно, как хочешь!"
                                    $RogueX.Eyes = "side"
                                    if not Player.Male:
                                        ch_r "[[ворчит себе под нос] Я пыталась сделать ей одолжение, а она. . ."
                                    else:
                                        ch_r "[[ворчит себе под нос] Девушка пытается сделать ему одолжение, а он. . ."
                            elif Party[0] is KittyX:
                                    ch_k "Оу. . ."
                                    $KittyX.Eyes = "side"
                                    ch_k "Я в последний раз делала тебе одолжение. . ."
                            elif Party[0] is EmmaX:
                                    ch_e "Хмм. . ."
                                    $EmmaX.Eyes = "side"
                                    ch_e "Хотела сделать тебе приятное, а ты. . ."
                            elif Party[0] is LauraX:
                                    ch_l "Тц. . ."
                                    $LauraX.Eyes = "side"
                                    if Player.Male:
                                            ch_l "Больше никаких \"бесплатных\" минетов, понял?. . ."
                                    else:
                                            ch_l "Больше не будет \"бесплатных\" куни, поняла?. . ."
                            elif Party[0] is JeanX:
                                    $ Party[0].Statup("Love", 90, -5)
                                    $ Party[0].Statup("Obed", 90, 2)
                                    ch_j "Серьезно? . ."
                                    $JeanX.Eyes = "side"
                                    ch_j "Почему все вокруг такие \"правильные\". . ?"
                            elif Party[0] is StormX:
                                    ch_s "Я могу тебя понять."
                            elif Party[0] is JubesX:
                                    ch_v "Ладно, ладно. . ."
                            elif Party[0] is GwenX:
                                    ch_g "Ясно. . ."
                            elif Party[0] is BetsyX:
                                    ch_b ". . . Что ж, я тебя поняла."
                            elif Party[0] is DoreenX:
                                    ch_d "Ну ладно. . ."
                            elif Party[0] is WandaX:
                                    ch_w "Понимаю, прости. . ."
                            $ Line = "no"
        #end second question phase


        if Line == "no" or Line == "sex":
                if Partner:
                        $ Partner.FaceChange("sexy")
                $ Party[0].RecentActions.remove("blanket")
                call expression Party[0].Tag + "_BJ_Reset"
                call expression Party[0].Tag + "_CUN_Reset"
                if len(Party) >= 2:
                        #Reset's Partner location
                        call QuickDisplay(Party[1],700,50)

                if Line == "Нет":
                        if bg_current == "bg player":
                            if Partner:
                                    call AnyLine(Partner,"Я ухожу.")
                            call AnyLine(Party[0],"Да, я тоже.")
                        else:
                            call AnyLine(Party[0],"Ох, убирайся уже отсюда.")

#                        $ Party[0].OutfitChange(6) #sets to OutfitDay
#                        if Partner:
#                                $ Partner.OutfitChange(6)
                        $ Party = []
                        $ Partner = 0

                        # Removes faux "Wait" changes, resets timing to previous night
                        $ Time_Count = 3
                        $ Current_Time = Time_Options[(Time_Count)]
                        $ Day -= 1

                        if Weekday == 0:
                            $ Weekday = 6
                        else:
                            $ Weekday -= 1

                        $ DayofWeek = Week[Weekday]
                        call Wait

                        jump Return_Player

                elif Line == "sex":
                        #shift to other sex stuff with her
                        $ Player.DrainWord("sexit",1,0)
                        call SexMenu # call expression Party[0].Tag + "_SexMenu"
        else:
                        #continue with the BJ
                        $ Line = 0
                        $ Speed = 1
                        $ Situation = 0

                        if Partner:
                            $ Partner.FaceChange("sexy")
                            #Reset's Partner location
                            call QuickDisplay(Partner,700,50)
                            if Player.Male:
                                    $ Party[1].Offhand = "blow"
                            else:
                                    $ Party[1].Offhand = "cun"
                        call SexAct("blow") #call expression Party[0].Tag + "_SexAct" pass ("blow")
        return

label Morning_Finish:
        #This is if you pretend to stay asleep
        while Player.Semen == Player.Semen_Max:
                #Loops until you cum, reducing semen amount to below maximum
                menu:
                    ". . .":
                            pass

                    "Концентрироваться на продолжительности [[Не открыто] (locked)" if "focus" not in Player.Traits:
                                pass
                    "Концентрироваться на продолжительности." if not Player.FocusX and "focus" in Player.Traits:
                                "Вы концентрируетесь на том, чтобы не кончить слишком быстро."
                                $ Player.FocusX = 1
                    "Прекратить концентрироваться." if Player.FocusX:
                                "Вы расслабляетесь. . ."
                                $ Player.FocusX = 0

                    "Эм. . . [Party[0].Pet], что ты делаешь?":
                        $ Line = "question"
                        return
                    "Как же классно. . .":
                        $ Line = "praise"
                        return
                    "Эй, хватит!":
                        $ Line = "no"
                        return
                $ Player.Statup("Focus", 80, 5)
                $ Player.Statup("Focus", 200, 10)
                $ Party[0].Statup("Lust", 80, 5)
                $ Party[0].Statup("Lust", 200, 10)
                if Partner:
                        $ Partner.Statup("Lust", 80, 5)
                        $ Partner.Statup("Lust", 200, 10)
                if Trigger == "blow":
                        call AnyLine(Party[0],"\"Чмок, чмок, чмок.\"")
                else:
                        call AnyLine(Party[0],"\"Хлюп, хлюп, хлюп.\"")
                if Partner:
                        call AnyLine(Party[1],"\"Чмок, чмок, чмок.\"")
                if Player.Focus >= 100:
                        #If you can cum:
                        "Вы чувствуете, что достигаете кульминации. . ."

                        #warn them?

                        "Вы кончаете ей в рот."
                        $ Player.Semen -= 1
                        $ Player.Focus = 0
                        $ Speed = 0
                        $ Girl.Thirst -= 10 if Girl.Thirst > 50 else 5

                        $ Girl.Statup("Lust", 200, 5)
                        if Partner:
                                $ Partner.Statup("Lust", 200, 5)
                        $ Girl.Statup("Inbt", 50, 3)
                        $ Girl.Addict -= 20
                        $ Girl.Addictionrate += 2
                        if "addictive" in Player.Traits:
                                $ Girl.Addictionrate += 2

                        if Girl.Swallow:
                                $ Girl.Swallow += 1
                                $ Girl.RecentActions.append("swallowed")
                                $ Girl.DailyActions.append("swallowed")
                                $ Player.Focus = 10
                                "Она продолжает и продолжает истощать вас, пока вы не кончаете."
                                if Partner:
                                        "Затем они вместе все начисто вылизывают."
                                else:
                                        "Затем она все начисто вылизывает."
                                $ Player.Focus = 15
                        else:
                                "Она слегка давится и все выплевывает."
                                $ Player.Focus = 5
                                if Partner:
                                    if Partner.Swallow:
                                        "Затем [Partner.Name] начисто вылизывает все."
                                    else:
                                        "Затем они все начисто вытирают."
                                else:
                                        "Затем она все начисто вытирает."
                                $ Player.Focus = 10

                if Girl.Lust >= 100:
                        #If the lead Girl can cum
                        $ Girl.Thirst = int(Girl.Thirst/2)
                        $ Girl.Thirst -= 5
                        $ Girl.Lust = 20
                        $ Girl.OCount += 1
                        $ Girl.Statup("Inbt", 50, 1)
                        $ Girl.Statup("Inbt", 70, 1)
                        "Вы слышите, как [Girl.Name] издает легкий писк, и слегка вздрагивает."
                        "Возможно, она была слишком возбуждена."
                        $ Player.Focus += 5

                if Partner and Partner.Lust >= 100:
                        #Checks if partner could orgasm
                        $ Partner.Thirst = int(Partner.Thirst/2)
                        $ Partner.Thirst -= 5
                        $ Partner.Lust = 20
                        $ Partner.OCount += 1
                        $ Partner.Statup("Inbt", 50, 1)
                        $ Partner.Statup("Inbt", 70, 1)
                        if Girl.OCount:
                                "[Partner.Name], кажется, тоже слегка вздрагивает. . ."
                        else:
                                "Вы слышите, как [Girl.Name] издает легкий писк, и слегка вздрагивает."
                                "Возможно, она была слишком возбуждена."
                        $ Player.Focus += 5

                $ Player.Focus -= 8 if Player.FocusX and Player.Focus > 50 else 0
        #out of loop, Focus under 25
        "С довольным вздохом, [Girl.Name] сворачивается калачиком рядом с вами и прижимается к вам."
        "Вы тоже ненадолго погружаетесь в сон. . ."
        $ Player.AddWord(1,0,"secretwood",0,"secretwood") #adds to daily and history
        $ Player.DrainWord("morningwood") #removes since you didn't acknowledge it happened. . .
        return
# end Event Morning Finish / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# end Event Morning Wood / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# end Sleepover content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /






## start Poly _Start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Poly_Start(Newbie=0,Round2=0,Asked=0): #rkeljsvgbdw
        # This is called prior to any new girls being added to your dating structure
        # If there are already two girls in there, it kicks up to the Harem version.
        # Newbie will be the new girl
        # Asked is passed if you request it from a chat menu
        $ Line = 0

        $ Event_Queue = [0,0]
        if Newbie in Player.Harem:
                "Tell Oni Poly was called with the newbie in the lead, [Newbie.Tag]."
                return

        if not Player.Harem:
                "Tell Oni Poly was called without a harem."
                return

        if Player.Harem[0] is WandaX:
            $ Tempmod += 10

        if Asked in TotalGirls:
                if Asked in Player.Harem and Player.Harem[0] is not Asked:
                        #moves character "Asked" to the head of the line.
                        $ Player.Harem.remove(Asked)
                        if Player.Harem:
                                $ Player.Harem.insert(0,Asked)
                        else:
                                $ Player.Harem.append(Asked)

        if "polystart" in Player.DailyActions:
                if Round2 and Asked:
                        "Вы ненадолго отводите [Player.Harem[0].Name] в сторону."
                        ch_p "Слушай, ты случайно не передумала насчет [Newbie.Name_rod]?"
                        if Player.Harem[0] is RogueX:
                                ch_r "Не слишком ли ты жадничаешь?"
                        elif Player.Harem[0] is KittyX:
                                ch_k "Воу, успокойся."
                        elif Player.Harem[0] is EmmaX:
                                ch_e "Ты слишком спешишь, [Player.Harem[0].Petname]."
                        elif Player.Harem[0] is LauraX:
                                ch_l "Охлади свое траханье."
                        elif Player.Harem[0] is JeanX:
                                ch_j "Нет, не совсем."
                        elif Player.Harem[0] is StormX:
                                ch_s "Дай мне время, я взвешиваю все варианты."
                        elif Player.Harem[0] is JubesX:
                                ch_v "Послушай. . . у меня есть чувства. . ."
                        elif Player.Harem[0] is GwenX:
                                ch_g "Не знаю, спроси меня попозже. . ."
                        elif Player.Harem[0] is BetsyX:
                                ch_b "Я все еще обдумываю. . ."
                        elif Player.Harem[0] is DoreenX:
                                ch_d "Я еще думаю. . ."
                        elif Player.Harem[0] is WandaX:
                                ch_w "Я дам тебе знать, если что-то изменится. . ."
                        call AnyLine(Asked,"Спроси меня об этом в другой раз.")
                $ Tempmod = 0
                return

        $ Player.DailyActions.append("polystart")

        if len(Player.Harem) >= 2:
                call Harem_Start(Newbie,Round2)
                $ Tempmod = 0
                return


        $ Party = [Player.Harem[0]]
        call Shift_Focus(Player.Harem[0])
        call Set_The_Scene
        call CleartheRoom(Player.Harem[0])


        if Round2:
                "Вы ненадолго отводите [Player.Harem[0].Name_vin] в сторону."
                ch_p "Слушай, ты случайно не передумала насчет [Newbie.Name_rod]?"
        else:
                $ Party[0].FaceChange("bemused")
                "[Party[0].Name] отводит вас в сторону и изъявляет желание о чем-то поговорить."

                #Line 1
                if Party[0] is RogueX:
                        ch_r "Вижу, вы с [Newbie.Name_tvo] неплохо устроились."
                elif Party[0] is KittyX:
                        if not Player.Male:
                            ch_k "Похоже, ты в последнее время неплохо сблизилась с [Newbie.Name_tvo]."
                        else:
                            ch_k "Похоже, ты в последнее время неплохо сблизился с [Newbie.Name_tvo]."
                elif Party[0] is EmmaX:
                        ch_e "Я заметила, что вы с [Newbie.Name_tvo] частенько проводите время вместе."
                elif Party[0] is LauraX:
                        ch_l "В последнее время я часто вижу тебя с [Newbie.Name_tvo]."
                elif Party[0] is JeanX:
                        ch_j "Я видела тебя вместе с [Newbie.Name_tvo]."
                elif Party[0] is StormX:
                        ch_s "Я видела, как ты проводишь время вместе с [Newbie.Name_tvo]."
                elif Party[0] is JubesX:
                        if not Player.Male:
                            ch_v "Я видела, как ты тусовалась с [Newbie.Name_tvo]."
                        else:
                            ch_v "Я видела, как ты тусовался с [Newbie.Name_tvo]."
                elif Party[0] is GwenX:
                        ch_g "Я видела тебя с [Newbie.Name_tvo]. . ."
                elif Party[0] is BetsyX:
                        if not Player.Male:
                            ch_b "Я заметила, что ты. . . увлеклась [Newbie.Name_tvo]."
                        else:
                            ch_b "Я заметила, что ты. . . увлекся [Newbie.Name_tvo]."
                elif Party[0] is DoreenX:
                        ch_d "Мне кажется, тебе довольно комфортно с [Newbie.Name_tvo]. . ."
                elif Party[0] is WandaX:
                        ch_w "В последнее время ты часто общаешься с [Newbie.Name_tvo]. . ."
                #end Line 1


        if Party[0].GirlLikeCheck(Newbie) >= 800:
                $ Party[0].FaceChange("sly")
        elif Party[0].GirlLikeCheck(Newbie) >= 600:
                pass
        else:
                # neither likes her much
                $ Party[0].FaceChange("angry",Mouth="normal")

        # We like her or not
        if Party[0] is RogueX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "Думаю, она очень сексуальная."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "Она мне очень нравится, просто мне было интересно, к чему все идет."
                else:
                        # neither likes her much
                        ch_r "Если честно, мне она не особо нравится."
        elif Party[0] is KittyX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "Я понимаю, она ведь такая сексуальная. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "Она нормальная, конечно, но я не очень уверена на ее счет. . ."
                else:
                        # neither likes her much
                        ch_k "Она мне не очень нравится."
        elif Party[0] is EmmaX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "Думаю, она настоящая находка."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "Она мне очень нравится, но у меня есть некоторые опасения на ее счет."
                else:
                        # neither likes her much
                        ch_e "Я не одобряю ее поведение."
        elif Party[0] is LauraX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "Я тебя понимаю, она такая горячая."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "Наверное, она нормальная."
                else:
                        # neither likes her much
                        ch_l "Мне она не нравится."
        elif Party[0] is JeanX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_j "Она довольно горячая."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_j "Она. . . нормальная."
                else:
                        # neither likes her much
                        ch_j "Тебе, наверное, лучше не стоит видеться с ней."
        elif Party[0] is StormX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_s "Она, конечно, очень красивая."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_s "Она, конечно, хорошая девочка. . ."
                else:
                        # neither likes her much
                        ch_s "Не думаю, что она мне сильно нравится."
        elif Party[0] is JubesX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_v "Ладно, она очень сексуальна, но. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_v "Она. . . нормальная, но. . ."
                else:
                        # neither likes her much
                        ch_v "Я здесь не для этого."
        elif Party[0] is GwenX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_g "Слушай, она настоящая находка, но. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_g "Мне она нравится, но. . ."
                else:
                        # neither likes her much
                        ch_g "Мне она не особо нравится."
        elif Party[0] is BetsyX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_b "Она довольно привлекательна, однако. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_b "Мы, пожалуй, ладим, однако. . ."
                else:
                        # neither likes her much
                        ch_b "Боюсь, мы с ней не в ладах."
        elif Party[0] is DoreenX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_d "Она, конечно, очень милая. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_d "Мы очень хорошие подруги, но. . ."
                else:
                        # neither likes her much
                        ch_d "Она мне не особо нравится. . ."
        elif Party[0] is WandaX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_w "Она горяча, но. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_w "Мы с ней ладим, но все равно. . ."
                else:
                        # neither likes her much
                        ch_w "Я терпеть ее не могу, но я понимаю твои вкусы. . ."
        #end line 2


        #Line 3
        if Party[0] is RogueX:
                ch_r "Я не знаю, как относиться к тому, чтобы делить тебя с какой-то другой девушкой."
                ch_r "Ты планируешь вступить с ней в серьезные отношения?"
        elif Party[0] is KittyX:
                if not Player.Male:
                    ch_k "Я не знаю какого это, делить свою девушку с кем-то еще."
                else:
                    ch_k "Я не знаю какого это, делить своего парня с кем-то еще."
                ch_k "Ну так что, ты[KittyX.like]хочешь встречаться с ней?"
        elif Party[0] is EmmaX:
                ch_e "У меня появилось небольшое чувство. . . собственничества к своему партнеру."
                ch_e "У тебя с ней все серьезно?"
        elif Party[0] is LauraX:
                ch_l "Я не очень хорошо лажу с другими."
                ch_l "У вас двоих все серьезно?"
        elif Party[0] is JeanX:
                ch_j "Если честно, я не заинтересована, чтобы делиться с ней."
                ch_j "Так что, у вас двоих все серьезно?"
        elif Party[0] is StormX:
                ch_s "Я не уверена, что я чувствую по этому поводу."
                ch_s "Каковы твои намерения на ее счет?"
        elif Party[0] is JubesX:
                ch_v "Я даже не знаю. . ."
                ch_v "Она правда тебе нравится?"
        elif Party[0] is GwenX:
                ch_g "Ты хочешь, чтобы она. . . присоединилась к нам?"
        elif Party[0] is BetsyX:
                ch_b "Я не знаю, насколько мне нравится, что у тебя есть любовница. . ."
                ch_b "У тебя серьезные намерения на ее счет?"
        elif Party[0] is DoreenX:
                ch_d "Я даже не знаю. . ."
                ch_d "Я совсем не хочу делить тебя с другими девушками. . ."
        elif Party[0] is WandaX:
                ch_w "Ты хочешь, чтобы она присоединилась к нам?"
        #end Line 3

        menu:
            extend ""
            "Я хочу встречаться и с ней.":
                $ Line = "y"
            "Возможно, мне стоит начать встречаться с ней, что думаешь?":
                $ Line = "m"
            "Я не хочу с ней встречаться.":
                $ Line = "n"

        if Line == "y":
            if Party[0].GirlLikeCheck(Newbie) >= 800:
                    # if they like her a lot
                    $ Line = "yy"
                    $ Party[0].Statup("Love", 90, 5)
                    $ Party[0].Statup("Obed", 50, 5)
                    $ Party[0].Statup("Inbt", 90, 10)
            elif ApprovalCheck(Party[0], 1800):
                    # if they really like you enough to put up with it
                    $ Line = "ym"
                    $ Party[0].Statup("Obed", 50, 5)
            elif ApprovalCheck(Party[0], 1500) and Party[0].GirlLikeCheck(Newbie) >= 500:
                    # if they like her well enough
                    $ Line = "ym"
            else:
                    # neither likes her much
                    $ Line = "yn"
                    $ Party[0].Statup("Love", 90, -10)
        #end Line = y
        if Line == "m":
            if Party[0].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "my"
                    $ Party[0].Statup("Inbt", 90, 5)
            elif ApprovalCheck(Party[0], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "mm"
            elif ApprovalCheck(Party[0], 1500) and Party[0].GirlLikeCheck(Newbie) >= 600:
                    # if they both like her well enough
                    $ Line = "mm"
            else:
                    # neither likes her much
                    $ Line = "mn"
        #end Line = m
        if Line == "n":
            if Party[0].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "ny"
                    $ Party[0].Statup("Inbt", 90, 10)
            elif ApprovalCheck(Party[0], 1700):
                    # if they both really like you enough to put up with it
                    $ Line = "nm"
                    $ Party[0].Statup("Inbt", 90, 5)
            elif ApprovalCheck(Party[0], 1300) and Party[0].GirlLikeCheck(Newbie) >= 500:
                    # if they both like her well enough
                    $ Line = "nm"
                    $ Party[0].Statup("Love", 90, 5)
            else:
                    # if they don't like her well enough
                    $ Line = "nn"
                    $ Party[0].Statup("Love", 90, 10)
        #end Line = n


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        if Line == "yn" or Line == "mn" or Line == "nn":
                $ Party[0].FaceChange("angry")
        elif Line == "yy" or Line == "ny" or Line == "my":
                $ Party[0].FaceChange("sexy")
        else:
                $ Party[0].FaceChange("bemused")

        #Line 5
        if Party[0] is RogueX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_r "Отлично, это может быть интересно."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_r "Ох, если ты захочешь, я поддержу тебя."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_r "Ох. Думаю, тебе это нужно!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_r "Да, думаю, я смогу с ней ужиться."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_r "Хмм, ну, я была бы непротив."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_r "Не думаю, что меня это устроит."
                elif Line == "nn":
                        # if you said no and agree
                        ch_r "Приятно слышать."

        elif Party[0] is KittyX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_k "Клево, звучит весело."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_k "Ох. Я не против, серьезно!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_k "Как ты можешь не хотеть ее, она такая сексуальная!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_k "Ага, я смогу[KittyX.like]смириться с этим."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_k "Ладно, хотя я бы не возражала."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "Мне это не нравится."
                elif Line == "nn":
                        # if you said no and agree
                        ch_k "Хорошо, а то мне не нравится эта идея."

        elif Party[0] is EmmaX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_e "Прекрасно. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_e "О, пожалуйста, поговори с ней, она милая."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_e "Жаль, она мне нравится."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_e "Полагаю, я могу смириться с этим."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        if not Player.Male:
                            ch_e "Ты могла бы сделать все гораздо хуже."
                        else:
                            ch_e "Ты мог бы сделать все гораздо хуже."

                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_e "Я не думаю, что это будет приемлемо."
                elif Line == "nn":
                        # if you said no and agree
                        ch_e "Полагаю, это к лучшему."

        elif Party[0] is LauraX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_l "Хорошо."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_l "Да ладно тебе, она клевая."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        if not Player.Male:
                            ch_l "Ты уверена? Она же такая сексуальная."
                        else:
                            ch_l "Ты уверен? Она же такая сексуальная."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_l "Хорошо."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_l "Ладно. Но я не против, если ты этого захочешь."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_l "Неа."
                elif Line == "nn":
                        # if you said no and agree
                        ch_l "Хорошо."

        elif Party[0] is JeanX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_j "Конечно, это хорошо."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_j "Ну. . . с ней может быть весело. . ."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_j "Ты серьезно? С ней ведь может быть весело."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_j "Я не против ее компании. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_j "Хорошо. Хотя, я была бы не против."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_j "Не хочу даже слышать об этом."
                elif Line == "nn":
                        # if you said no and agree
                        ch_j "Ага."

        elif Party[0] is StormX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_s "Ох, это будет здорово. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_s "Ох, тебе определенно стоит это сделать!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_s "Это очень плохо. Вам было бы хорошо вместе."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_s "Ну, это должно быть неплохо."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_s "Возможно, ты захочешь пересмотреть свое решение. . ."

                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_s "Не думаю, что смогу с ней ужиться."
                elif Line == "nn":
                        # if you said no and agree
                        ch_s "Да, я согласна с этим."

        elif Party[0] is JubesX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_v "Ладно, клево."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_v "Ага, конечно, я согласна."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_v "Ладно, но ты можешь многое упустить!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_v "Ладно, ага, я справлюсь."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_v "Ладно, думаю, тебе решать."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_v "Нууу. . . Знаешь, у меня другое мнение."
                elif Line == "nn":
                        # if you said no and agree
                        ch_v "Рада, что мы на одной волне."

        elif Party[0] is GwenX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_g "Хорошо."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_g "Ладно, просто знай, я не против."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_g "Оу!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_g "Ну, думаю, это будет не конец света. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_g "Ладно, думаю, это нормально."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_g "Мне это не нравится."
                elif Line == "nn":
                        # if you said no and agree
                        ch_g "Ага."

        elif Party[0] is BetsyX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_b "Восхитительно."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_b "Я за то, чтобы вы начали встречаться. . ."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_b "Жаль. . ."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_b "Пожалуй, я должна уступить. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_b "Возможно, это к лучшему."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_b "Что ж, я против этого."
                elif Line == "nn":
                        # if you said no and agree
                        ch_b "Я одобряю твое решение."

        elif Party[0] is DoreenX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_d "Ох, здорово!"
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_d "Ну, я только за. . ."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_d "Оу. . ."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_d "Ну ладно, наверное. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_d "Эм, ладно."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_d "Хм, ну, мне это не нравится. . ."
                elif Line == "nn":
                        # if you said no and agree
                        ch_d "Спасибо. . ."

        elif Party[0] is WandaX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_w "У тебя столько грязных мыслей!"
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_w "Ага, тогда ладно. . ."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_w "Жаль. . ."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_w "Ага, ладно. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_w "Эм, ладно."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_w "Мне придется отказаться. . ."
                elif Line == "nn":
                        # if you said no and agree
                        ch_w "Клево. . ."
        #end Line 5

        if Line != "yy" and Line != "nn":
            #if there was some doubt to it
            menu:
                extend ""
                "Хорошо, тогда я попрошу ее присоединиться к нам." if Line in ("my","ny","ym","mm","nm"):
                    #They were generally favorable, so you agreed
                    $ Line = "yy"
                    $ Party[0].FaceChange("smile")
                    $ Party[0].Statup("Love", 90, 10)
                    $ Party[0].Statup("Obed", 50, 10)
                    if Party[0] is RogueX:
                                    ch_r "Отлично, это может быть интересным."
                    elif Party[0] is KittyX:
                                    ch_k "Клево, звучит весело."
                    elif Party[0] is EmmaX:
                                    ch_e "Прекрасно. . ."
                    elif Party[0] is LauraX:
                                    ch_l "Хорошо."
                    elif Party[0] is JeanX:
                                    ch_j "Ладно."
                    elif Party[0] is StormX:
                                    ch_s "Звучит потрясающе."
                    elif Party[0] is JubesX:
                                    ch_v "Славно!"
                    elif Party[0] is GwenX:
                                    ch_g "Отлично!"
                    elif Party[0] is BetsyX:
                                    ch_b "Восхитительно. . ."
                    elif Party[0] is DoreenX:
                                    ch_d "Здорово!"
                    elif Party[0] is WandaX:
                                    ch_w "Ну и хорошо!"

                "Что ж, тогда, я пожалуй, не буду ей ничего предлагать." if Line in ("mn","yn","ym","mm","nm"):
                    #They were unfavorable, so you gave up on it.
                    $ Line = "nn"
                    $ Party[0].FaceChange("smile")
                    $ Party[0].Statup("Love", 90, 10)
                    if Party[0] is RogueX:
                                    ch_r "Приятно слышать."
                    elif Party[0] is KittyX:
                                    ch_k "Хорошо, а то мне не нравится эта идея."
                    elif Party[0] is EmmaX:
                                    ch_e "Полагаю, это к лучшему."
                    elif Party[0] is LauraX:
                                    ch_l "Хорошо."
                    elif Party[0] is JeanX:
                                    ch_j "Ладно."
                    elif Party[0] is StormX:
                                    ch_s "Это было бы неплохо."
                    elif Party[0] is JubesX:
                                    ch_v "Ладно, хорошо."
                    elif Party[0] is GwenX:
                                    ch_g "Ладно."
                    elif Party[0] is BetsyX:
                                    ch_b "Я ценю вашу сдержанность."
                    elif Party[0] is DoreenX:
                                    ch_d "Оу, спасибо."
                    elif Party[0] is WandaX:
                                    ch_w "Клево."

                "Я всё равно приглашу её присоединиться к нам." if Line in ("mn","yn"):
                    #if they were unfavorable, but you insist
                    pass

                "Что ж, я все равно не собираюсь ничего ей предлагать." if Line in ("nm","ny","mm"):
                    #if they give you permission, but you aren't into it.
                    $ Line = "nn"
                    $ Party[0].FaceChange("sad")
                    $ Party[0].Statup("Obed", 70, 5)
                    if Party[0] is RogueX:
                                    ch_r "Ох, ладно."
                    elif Party[0] is KittyX:
                                    ch_k "Ну ладно."
                    elif Party[0] is EmmaX:
                                    ch_e "Как хочешь."
                    elif Party[0] is LauraX:
                                    ch_l "Ладно."
                    elif Party[0] is JeanX:
                                    ch_j "Ладно. . ."
                    elif Party[0] is StormX:
                                    ch_s "Хорошо."
                    elif Party[0] is JubesX:
                                    ch_v "Ага, все в порядке."
                    elif Party[0] is GwenX:
                                    ch_g "Оу. Ладно."
                    elif Party[0] is BetsyX:
                                    ch_b "Это прискорбно. . ."
                    elif Party[0] is DoreenX:
                                    ch_d "Оу. . ."
                    elif Party[0] is WandaX:
                                    ch_w "Конечно."

        #end player response to their feedback

        if Line == "mn" or Line == "yn":
                # if you said yes/maybe and they said no, but you insisted anyway

                if ApprovalCheck(Party[0], 1600) and Party[0].GirlLikeCheck(Newbie) >= 500:
                            $ Party[0].FaceChange("sadside")
                            $ Party[0].Statup("Love", 90, -5)
                            $ Party[0].Statup("Obed", 50, 15)
                            if Party[0] is RogueX:
                                    ch_r "Ну ладно, пусть так."
                            elif Party[0] is KittyX:
                                    ch_k "Блин, ладно."
                            elif Party[0] is EmmaX:
                                    ch_e "Полагаю, мы сможем найти для нее местечко."
                            elif Party[0] is LauraX:
                                    ch_l "Как скажешь."
                            elif Party[0] is JeanX:
                                    ch_j "Ну. . . хорошо."
                                    ch_j "Но считай это твоим рождественским подарком."
                            elif Party[0] is StormX:
                                    ch_s ". . ."
                                    ch_s "Я смогу смириться с этим."
                            elif Party[0] is JubesX:
                                    ch_v "Хорошо. Как скажешь."
                            elif Party[0] is GwenX:
                                    ch_g "Думаю, я смогу с этим жить."
                            elif Party[0] is BetsyX:
                                    ch_b "Пожалуй, я смогу адаптироваться. . ."
                            elif Party[0] is DoreenX:
                                    ch_d "Ну, думаю, я смогу с этим свыкнуться. . ."
                            elif Party[0] is WandaX:
                                    ch_w ". . . Хорошо, я сделаю так, чтобы все было замечательно."
                            $ Line = "yy"
                else:
                            $ Party[0].FaceChange("angry",Eyes="side")
                            $ Party[0].Statup("Love", 90, -25)
                            $ Party[0].Statup("Inbt", 90, 10)
                            if Party[0] is RogueX:
                                    ch_r "Ты мне не настолько нравишься, [RogueX.Petname]."
                                    ch_r "Я в этом не участвую."
                            elif Party[0] is KittyX:
                                    if not Player.Male:
                                        ch_k "Ты не настолько милая, [KittyX.Petname]."
                                    else:
                                        ch_k "Ты не настолько милый, [KittyX.Petname]."
                                    ch_k "С меня хватит."
                            elif Party[0] is EmmaX:
                                    ch_e "Не переоценивай себя, [EmmaX.Petname]."
                                    ch_e "Мы закончили."
                            elif Party[0] is LauraX:
                                    ch_l "Ты заходишь слишком далеко, [LauraX.Petname]."
                                    ch_l "Я в этом не участвую."
                            elif Party[0] is JeanX:
                                    ch_j "Меня одной более чем достаточно."
                                    ch_j "Я в этом не участвую."
                            elif Party[0] is StormX:
                                    ch_s ". . ."
                                    ch_s "Я не могу стать частью подобного."
                            elif Party[0] is JubesX:
                                    ch_v "Нууу, тогда я пас."
                            elif Party[0] is GwenX:
                                    ch_g "Мне не стоит становиться частью этого бардака."
                            elif Party[0] is BetsyX:
                                    ch_b "Боюсь, я не могу это принять. . ."
                            elif Party[0] is DoreenX:
                                    ch_d "Ну, мне это как-то не нравится!"
                            elif Party[0] is WandaX:
                                    ch_w "Мне не хочется ввязываться вл весь этот бардак."
                            $ Party[0].Traits.append("ex")
                            $ Party[0].Break[0] = 5 + Party[0].Break[1] + Party[0].Cheated
                            $ Player.Harem.remove(Party[0])
                            call Remove_Girl(Party[0])
        #end "she said no but you insisted"

        $ Party = []
        if Line == "yy":
                if Newbie.Tag + "No" in Player.Traits:
                        $ Player.Traits.remove(Newbie.Tag + "No")
                $ Player.DrainWord(Newbie.Tag + "No",0,0,1)
                $ Player.Traits.append(Newbie.Tag + "Yes")
                "Вам нужно поговорить с [Newbie.Name_tvo]."
        else:
                $ Player.Traits.append(Newbie.Tag + "No")
        $ Tempmod = 0
        return

## end Poly _Start//////////////////////////////////////////////////////////



## start Harem _Start//////////////////////////////////////////////////////////
label Harem_Start(Newbie=0,Round2=0): #rkeljsvgbdw
        # This is called prior to any new girls being added to your dating structure
        # If there are aren't two girls in there, it kicks back.
        # Newbie will be the new girl

        $ Line = 0

        if len(Player.Harem) < 2:
                #if there aren't enough girls yet, forget about it.
                "Tell Oni Harem_Start called without enough people in it"
                return

        $ Party = [Player.Harem[0],Player.Harem[1]]
        # Adds first two harem members to party, removed everyone else from the room.
        call Present_Check
        $ Party = [Player.Harem[0],Player.Harem[1]]
        call Shift_Focus(Player.Harem[0])
        call Set_The_Scene

        if WandaX in Party and not Tempmod:
                $ Tempmod += 10

        $ Party[0].FaceChange("bemused")
        $ Party[1].FaceChange("bemused")
        if Round2:
                "Вы зовете [Party[0].Name_vin] и [Party[1].Name_vin]."
                ch_p "Мне интересно, не передумали ли вы насчет [Newbie.Name_rod]."
        else:
                "[Party[0].Name] отводит вас в сторону и изъявляет желание о чем-то поговорить."
                #Line 1

                if Party[0] is RogueX:
                        ch_r "Слушай, мы с [Party[1].Name_tvo] поговорили."
                elif Party[0] is KittyX:
                        ch_k "Ну[KittyX.like]мы с [Party[1].Name_tvo] немного поболтали."
                elif Party[0] is EmmaX:
                        ch_e "Мы с [Party[1].Name_tvo] кое-что обсудили."
                elif Party[0] is LauraX:
                        ch_l "Мы с [Party[1].Name_tvo] немного поболтали. . ."
                elif Party[0] is JeanX:
                        ch_j "Я тут поговорила. . . вот с ней. . ."
                elif Party[0] is StormX:
                        ch_s "На днях мы с [Party[1].Name_tvo] пообедали вместе, и во время нашего разговора кое-что всплыло."
                elif Party[0] is JubesX:
                        ch_v "Так вот, мы с [Party[1].Name_tvo] поговорили, и кое-что всплыло. . ."
                elif Party[0] is GwenX:
                        ch_g "Так вот, мы тут с [Party[1].Name_tvo] поговорили. . ."
                elif Party[0] is BetsyX:
                        ch_b "Мы с [Party[1].Name_tvo] мило поболтали, и всплыла одна интересная тема. . ."
                elif Party[0] is DoreenX:
                        ch_d "Слушай, мы тут с [Party[1].Name_tvo] недавно поговорили. . ."
                elif Party[0] is WandaX:
                        ch_w "Послушай, мы тут поговорили. . ."
                #end Line 1

                #Line 2
                if Party[1] is RogueX:
                        ch_r "Мы слышали, что вы с [Newbie.Name_tvo] довольно уютно устроились ."
                elif Party[1] is KittyX:
                        if not Player.Male:
                            ch_k "Мы слышали, что ты в последнее время сблизилась с [Newbie.Name_tvo]."
                        else:
                            ch_k "Мы слышали, что ты в последнее время сблизился с [Newbie.Name_tvo]."
                elif Party[1] is EmmaX:
                        ch_e "Мы слышали, что вы с [Newbie.Name_tvo] частенько проводите время вместе."
                elif Party[1] is LauraX:
                        ch_l "В последнее время мы слишком часто видели тебя вместе с [Newbie.Name_tvo]."
                elif Party[1] is JeanX:
                        if not Player.Male:
                            ch_j "Мы заметили, что в последнее время ты слишком часто была рядом с [Newbie.Name_tvo]."
                        else:
                            ch_j "Мы заметили, что в последнее время ты слишком часто был слишком с [Newbie.Name_tvo]."
                elif Party[1] is StormX:
                        ch_s "Мы обе заметили, что ты проводишь много время с [Newbie.Name_tvo]."
                elif Party[1] is JubesX:
                        if not Player.Male:
                            ch_v "Мы точно видели, как ты тусовалась с [Newbie.Name_tvo]."
                        else:
                            ch_v "Мы точно видели, как ты тусовался с [Newbie.Name_tvo]."
                elif Party[1] is GwenX:
                        ch_g "Ну, мы видели тебя вместе с [Newbie.Name_tvo]. . ."
                elif Party[1] is BetsyX:
                        ch_b "Мы пришли к выводу, что, возможно, между тобой и [Newbie.Name_tvo]. . ."
                        ch_b ". . . что-то есть?"
                elif Party[1] is DoreenX:
                        ch_d "Нам показалось, что вы с [Newbie.Name_tvo] очень близки. . ."
                elif Party[1] is WandaX:
                        ch_w "Мы пришли к выводу, что в последнее время ты часто общаешься с [Newbie.Name_tvo]. . ."
                #end Line 2

        # We like her or not Line 3

        if Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                pass
        elif Party[0].GirlLikeCheck(Newbie) >= 700:
                # only first girl likes her
                $ Party[1].FaceChange("angry",Mouth="normal")
        elif Party[1].GirlLikeCheck(Newbie) >= 700:
                # only second girl likes her
                $ Party[0].FaceChange("angry",Mouth="normal")
        else:
                # neither likes her much
                $ Party[0].FaceChange("angry",Mouth="normal")
                $ Party[1].FaceChange("angry",Mouth="normal")

        if Party[0] is RogueX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "Теперь она нам очень нравится и мы не против ее компании."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "Теперь она нам очень нравится, но мы не особо уверены на счет нее."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_r "Теперь она нам очень нравится, но [Party[1].Name] не особо уверена на счет нее."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_r "Теперь она очень нравится [Party[1].Name_dat], но я не особо уверена на счет нее."
                else:
                        # neither likes her much
                        ch_r "Мы обе не в восторге от нее."
        elif Party[0] is KittyX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "Она очень сексуальная, мы обе это понимаем. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "Она нормальная, конечно, но мы не особо уверены на ее счет. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_k "Мне она нравится, но [Party[1].Name] не уверена на ее счет."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_k "[Party[1].Name_dat] она нравится, но я не уверена на ее счет."
                else:
                        # neither likes her much
                        ch_k "Она нам не очень нравится."
        elif Party[0] is EmmaX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "Я думаю, мы обе согласны, что она настоящая находка."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "Она нам нравится, но у нас есть некоторые опасения на ее счет."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_e "[Party[1].Name_dat] она не нравится."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_e "[Party[1].Name_dat] она нравится."
                else:
                        # neither likes her much
                        ch_e "Нам она не нравится."
        elif Party[0] is LauraX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "Она очень сексуальная, мы обе это понимаем."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "Наверное, она нормальная."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_l "Она нормальная, но [Party[1].Name_dat] она не нравится."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_l "[Party[1].Name_dat] она нравится. Но не мне."
                else:
                        # neither likes her much
                        ch_l "Она нам не нравится."
        elif Party[0] is JeanX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_j "Она очень даже сексуальная."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_j "Она. . . нормальная."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_j "Думаю, она нормальная, но [Party[1].Name_dat] она не нравится."
                        ch_j "Но это лишь мое замечание. . ."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_j "[Party[1].Name_dat] она нравится. Но не мне."
                        ch_j "Поэтому я думаю, что ты сделаешь правильный выбор. . ."
                else:
                        # neither likes her much
                        ch_j "Тебе, наверное, лучше не стоит видеться с ней."
        elif Party[0] is StormX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_s "Мы согласны, что она великолепна. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_s "Она хорошая девочка, но у нас есть некоторые опасения на ее счет. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_s "Она мне нравится, но [Party[1].Name] ее не одобряет."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_s "Кажется, она нравится [Party[1].Name_dat], но я не уверена на ее счет."
                else:
                        # neither likes her much
                        ch_s "Она нам не очень нравится."
        elif Party[0] is JubesX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_v "Ладно, она очень сексуальна, но. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_v "Она. . . нормальная, но. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_v "Она. . . нормальная, но [Party[1].Name] так не думает. . ."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_v "[Party[1].Name_dat] она нравится, но я не уверена."
                else:
                        # neither likes her much
                        ch_v "Она нам не нравится."

        elif Party[0] is GwenX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_g "Слушай, она настоящая находка, но. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_g "Мне она нравится, но. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_g "Мне она нравится, но не [Party[1].Name_dat]. . ."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_g "[Party[1].Name_dat] она нравится, но мне не очень."
                else:
                        # neither likes her much
                        ch_g "Она нам не очень нравится."

        elif Party[0] is BetsyX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_b "Она довольно привлекательна, однако. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_b "Пожалуй, мы ладим, однако. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_b "У меня с ней нормальные отношения, но не могу сказать то же про [Party[1].Name_vin]. . ."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_b "[Party[1].Name_dat] она нравится, но боюсь, что мы с ней не поладим."
                else:
                        # neither likes her much
                        ch_b "Боюсь, мы не поладим."
        elif Party[0] is DoreenX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_d "Она очень милая. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_d "Мы очень хорошие подруги, но. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_d "Мы очень хорошие подруги, но. . . [Party[1].Name] против. . ."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_d "[Party[1].Name] думает, что она милая, но я не могу с ней согласиться."
                else:
                        # neither likes her much
                        ch_d "Она нам совсем не нравится. . ."
        elif Party[0] is WandaX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_w "Она горяча, но. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_w "Мы с ней ладим, но все равно. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_w "Я с ней лажу, но. . . не [Party[1].Name]. . ."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_w "[Party[1].Name_dat] она нравится, но не мне."
                else:
                        # neither likes her much
                        ch_w "Мы ее терпеть не можем, но я понимаю твои вкусы. . ."
        #end line 3

        #Line 4
        if Party[1] is RogueX:
                ch_r "Ты планируешь вступить с ней в серьезные отношения?"
        elif Party[1] is KittyX:
                ch_k "Ну так что, ты[KittyX.like]хочешь встречаться с ней?"
        elif Party[1] is EmmaX:
                ch_e "У тебя с ней все серьезно?"
        elif Party[1] is LauraX:
                ch_l "У вас двоих все серьезно?"
        elif Party[1] is JeanX:
                ch_j "Так что, вас двоих все серьезно?"
        elif Party[1] is StormX:
                ch_s "К чему у вас все идет?"
        elif Party[1] is JubesX:
                ch_v "Я даже не знаю. . ."
                ch_v "Она правда тебе нравится?"
        elif Party[1] is GwenX:
                ch_g "Ты хочешь, чтобы она. . . присоединилась к нам?"
        elif Party[1] is BetsyX:
                ch_b "У тебя серьезные намерения на ее счет?"
        elif Party[1] is DoreenX:
                ch_d "Ты. . . хочешь с ней встречаться?"
        elif Party[1] is WandaX:
                ch_w "Ты хочешь, чтобы она присоединилась к нам?"
        #end Line 4

        menu:
            extend ""
            "Я хочу встречаться и с ней.":
                $ Line = "y"
            "Возможно, мне стоит начать встречаться с ней, что думаешь?":
                $ Line = "m"
            "Я не хочу с ней встречаться.":
                $ Line = "n"

        if Line == "y":
            if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "yy"
                    $ Party[0].Statup("Love", 90, 5)
                    $ Party[0].Statup("Obed", 50, 5)
                    $ Party[0].Statup("Inbt", 90, 10)
                    $ Party[1].Statup("Love", 90, 5)
                    $ Party[1].Statup("Obed", 50, 5)
                    $ Party[1].Statup("Inbt", 90, 10)
            elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "ym"
                    $ Party[0].Statup("Obed", 50, 10)
                    $ Party[1].Statup("Obed", 50, 10)
            elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
                    if Party[0].GirlLikeCheck(Newbie) >= 500 and Party[1].GirlLikeCheck(Newbie) >= 500:
                            # if they both like her well enough
                            $ Line = "ym"
                            $ Party[0].Statup("Obed", 80, 15)
                            $ Party[1].Statup("Obed", 80, 15)
                    else:
                            # if they don't like her well enough
                            $ Line = "yn"
                            $ Party[0].Statup("Love", 90, -5)
                            $ Party[0].Statup("Obed", 50, -5)
                            $ Party[1].Statup("Love", 90, -5)
                            $ Party[1].Statup("Obed", 50, -5)
            else:
                            # neither likes her much
                            $ Line = "yn"
                            $ Party[0].Statup("Love", 90, -10)
                            $ Party[0].Statup("Obed", 50, -5)
                            $ Party[1].Statup("Love", 90, -10)
                            $ Party[1].Statup("Obed", 50, -5)
        #end Line = y
        if Line == "m":
            if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "my"
                    $ Party[0].Statup("Inbt", 90, 5)
                    $ Party[1].Statup("Inbt", 90, 5)
            elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "mm"
            elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
                    if Party[0].GirlLikeCheck(Newbie) >= 600 or Party[1].GirlLikeCheck(Newbie) >= 600:
                            # if they both like her well enough
                            $ Line = "mm"
                    else:
                            # if they don't like her well enough
                            $ Line = "mn"
            else:
                            # neither likes her much
                            $ Line = "mn"
        #end Line = m
        if Line == "n":
            if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "ny"
                    $ Party[0].Statup("Inbt", 90, 10)
                    $ Party[1].Statup("Inbt", 90, 10)
            elif ApprovalCheck(Party[0], 1700) and ApprovalCheck(Party[1], 1700):
                    # if they both really like you enough to put up with it
                    $ Line = "nm"
                    $ Party[0].Statup("Inbt", 90, 5)
            elif ApprovalCheck(Party[0], 1300) and ApprovalCheck(Party[1], 1300):
                    if Party[0].GirlLikeCheck(Newbie) >= 500 and Party[1].GirlLikeCheck(Newbie) >= 500:
                            # if they both like her well enough
                            $ Line = "nm"
                    else:
                            # if they don't like her well enough
                            $ Line = "nn"
                            $ Party[0].Statup("Love", 90, 5)
                            $ Party[0].Statup("Inbt", 90, 5)
                            $ Party[1].Statup("Love", 90, 5)
                            $ Party[1].Statup("Inbt", 90, 5)
            else:
                            # neither likes her much
                            $ Line = "nn"
                            $ Party[0].Statup("Love", 90, 5)
                            $ Party[0].Statup("Inbt", 90, 5)
                            $ Party[1].Statup("Love", 90, 5)
                            $ Party[1].Statup("Inbt", 90, 5)
        #end Line = n


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        if Line == "yn" or Line == "mn" or Line == "nn":
                $ Party[0].FaceChange("angry")
                $ Party[1].FaceChange("angry")
        elif Line == "yy" or Line == "ny" or Line == "my":
                $ Party[0].FaceChange("sexy")
                $ Party[1].FaceChange("sexy")
        else:
                $ Party[0].FaceChange("bemused")
                $ Party[1].FaceChange("bemused")

        #Line 5
        if Party[0] is RogueX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_r "Отлично, это может быть интересным."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_r "Ох, если ты захочешь, я поддержу тебя."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_r "Ох. Думаю, тебе это нужно!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_r "Да, думаю, мы сможем с ней ужиться."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_r "Хмм, ну, я была бы не против."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_r "Не думаю, что нас это устроит."
                elif Line == "nn":
                        # if you said no and agree
                        ch_r "Приятно слышать."

        elif Party[0] is KittyX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_k "Клево, звучит весело."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_k "Ох. Серьезно, мы не против!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_k "Как ты можешь не хотеть ее, она такая сексуальная!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_k "Да, мы сможем[KittyX.like]смириться с этим."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_k "Ладно, хотя мы бы не возражали."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "Нам это не нравится."
                elif Line == "nn":
                        # if you said no and agree
                        ch_k "Хорошо, а то мне не нравится эта идея."

        elif Party[0] is EmmaX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_e "Прекрасно. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_e "О, пожалуйста, поговори с ней, она замечательная."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_e "Жаль, она мне нравится."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_e "Полагаю, мы сможем смириться с этим."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        if not Player.Male:
                            ch_e "Ты могла бы сделать все гораздо хуже."
                        else:
                            ch_e "Ты мог бы сделать все гораздо хуже."

                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_e "Я не думаю, что это будет приемлемо."
                elif Line == "nn":
                        # if you said no and agree
                        ch_e "Полагаю, это к лучшему."

        elif Party[0] is LauraX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_l "Хорошо."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_l "Да ладно тебе, она клевая."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_l "Точно? Она же такая сексуальная."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_l "Хорошо."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_l "Хорошо. Мы не против, если ты этого хочешь."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_l "Неа."
                elif Line == "nn":
                        # if you said no and agree
                        ch_l "Хорошо."

        elif Party[0] is JeanX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_j "Конечно, это хорошо."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_j "Ну. . . с ней может быть весело. . ."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_j "Ты серьезно? С ней ведь может быть весело."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_j "Мы не против ее компании. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_j "Хорошо. Хотя, я была бы не против."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_j "Не хочу даже слышать об этом."
                elif Line == "nn":
                        # if you said no and agree
                        ch_j "Ага."

        elif Party[0] is StormX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_s "Ох, это будет здорово. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_s "Ох, тебе определенно стоит это сделать!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_s "Это очень плохо. Вам было бы хорошо вместе."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_s "Ну, это должно быть неплохо."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_s "Возможно, ты захочешь пересмотреть свое решение. . ."

                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_s "Не думаю, что мы сможем с ней ужиться."
                elif Line == "nn":
                        # if you said no and agree
                        ch_s "Да, мы с тобой согласны."

        elif Party[0] is JubesX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_v "Ладно, клево."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_v "Ага, конечно, думаю, мы согласны."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_v "Ладно, но ты можешь многое упустить!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_v "Ладно, ага, мы справимся."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_v "Ладно, думаю, тебе решать."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_v "Нууу. . . тебе стоило сперва подумать о нас."
                elif Line == "nn":
                        # if you said no and agree
                        ch_v "Рада, что мы на одной волне."

        elif Party[0] is GwenX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_g "Хорошо."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_g "Хорошо, просто знай, что мы только за."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_g "Оу!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_g "Ну, думаю, это будет не конец света. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_g "Ладно, думаю, это нормально."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_g "Нам это не нравится."
                elif Line == "nn":
                        # if you said no and agree
                        ch_g "Ага."

        elif Party[0] is BetsyX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_b "Восхитительно."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_b "Знай, что мы не против. . ."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_b "Как жаль. . ."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_b "Пожалуй, мы можем пойти на уступки. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_b "Пожалуй, это к лучшему."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_b "Что ж, мы против."
                elif Line == "nn":
                        # if you said no and agree
                        ch_b "Мы благодарны за такое решение."

        elif Party[0] is DoreenX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_d "Ох, здорово!"
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_d "Ну, мы только за. . ."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_d "Оу. . ."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_d "Ну, ладно. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_d "Эм, ладно."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_d "Хм, ну, нам это не нравится. . ."
                elif Line == "nn":
                        # if you said no and agree
                        ch_d "Спасибо. . ."

        elif Party[0] is WandaX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_w "У тебя столько грязных мыслей!"
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_w "Ага, тогда ладно. . ."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_w "Жаль. . ."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_w "Ага, ладно. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_w "Эм, ладно."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_w "Я вынуждена отказаться. . ."
                elif Line == "nn":
                        # if you said no and agree
                        ch_w "Клево. . ."
        #end Line 5

        if Line != "yy" and Line != "nn":
            #if there was some doubt to it
            menu:
                extend ""
                "Хорошо, тогда я попрошу ее присоединиться к нам." if Line in ("my","ny","ym","mm","nm"):
                        #They were generally favorable, so you agreed
                        $ Line = "yy"
                        $ Party[0].FaceChange("smile")
                        $ Party[1].FaceChange("smile")
                        $ Party[0].Statup("Obed", 80, 5)
                        $ Party[0].Statup("Inbt", 90, 10)
                        $ Party[1].Statup("Obed", 80, 5)
                        $ Party[1].Statup("Inbt", 90, 10)
                        if Party[0] is RogueX:
                                ch_r "Отлично, это может быть интересным."
                        elif Party[0] is KittyX:
                                ch_k "Клево, звучит весело."
                        elif Party[0] is EmmaX:
                                ch_e "Прекрасно. . ."
                        elif Party[0] is LauraX:
                                ch_l "Хорошо."
                        elif Party[0] is JeanX:
                                ch_j "Хорошо."
                        elif Party[0] is StormX:
                                ch_s "Хорошо."
                        elif Party[0] is JubesX:
                                ch_v "Славно!"
                        elif Party[0] is GwenX:
                                ch_g "Отлично!"
                        elif Party[0] is BetsyX:
                                ch_b "Восхитительно!"
                        elif Party[0] is DoreenX:
                                ch_d "Здорово!"
                        elif Party[0] is WandaX:
                                ch_w "Ну и замечательно!"
                "Что ж, тогда, я пожалуй, не буду ей ничего предлагать." if Line in ("mn","yn"):
                        #They were unfavorable, so you gave up on it.
                        $ Line = "nn"
                        $ Party[0].FaceChange("normal")
                        $ Party[1].FaceChange("normal")
                        $ Party[0].Statup("Love", 90, 5)
                        $ Party[0].Statup("Inbt", 90, 5)
                        $ Party[1].Statup("Love", 90, 5)
                        $ Party[1].Statup("Inbt", 90, 5)
                        if Party[0] is RogueX:
                                ch_r "Приятно слышать."
                        elif Party[0] is KittyX:
                                ch_k "Хорошо, а то мне не нравится эта идея."
                        elif Party[0] is EmmaX:
                                ch_e "Полагаю, это к лучшему."
                        elif Party[0] is LauraX:
                                ch_l "Хорошо."
                        elif Party[0] is JeanX:
                                ch_j "Good."
                        elif Party[0] is StormX:
                                ch_s "Good."
                        elif Party[0] is JubesX:
                                ch_v "Ладно, хорошо."
                        elif Party[0] is GwenX:
                                ch_g "Ладно."
                        elif Party[0] is BetsyX:
                                ch_b "Я ценю вашу сдержанность."
                        elif Party[0] is DoreenX:
                                ch_d "Оу, спасибо."
                        elif Party[0] is WandaX:
                                ch_w "Клево."
                "Я всё равно приглашу её присоединиться к нам." if Line in ("mn","yn"):
                        #if they were unfavorable, but you insist
                        pass

                "Что ж, я все равно не собираюсь ничего ей предлагать." if Line in ("ym","my","nm","ny","mm"):
                        #if they give you permission, but you aren't into it.
                        $ Line = "nn"
                        $ Party[0].FaceChange("sad")
                        $ Party[1].FaceChange("sad")
                        $ Party[0].Statup("Obed", 50, 5)
                        $ Party[1].Statup("Obed", 50, 5)
                        if Party[0] is RogueX:
                                ch_r "Ох, ладно."
                        elif Party[0] is KittyX:
                                ch_k "Ну ладно."
                        elif Party[0] is EmmaX:
                                ch_e "Как хочешь."
                        elif Party[0] is LauraX:
                                ch_l "Ладно."
                        elif Party[0] is JeanX:
                                ch_j "Ладно, наверное. . ."
                        elif Party[0] is StormX:
                                ch_s "Очень жаль. . ."
                        elif Party[0] is JubesX:
                                ch_v "Ага, все в порядке."
                        elif Party[0] is GwenX:
                                ch_g "Оу. Ладно."
                        elif Party[0] is BetsyX:
                                ch_b "Это прискорбно. . ."
                        elif Party[0] is DoreenX:
                                ch_d "Оу. . ."
                        elif Party[0] is WandaX:
                                ch_w "Конечно."
            #end player response to their feedback

            if Line == "yy" or Line == "nn":
                                pass
            elif len(Player.Harem) >= 3:
                                $ Party[0].FaceChange("smile",Eyes="side")
                                $ Party[1].FaceChange("smile",Eyes="side")
                                $ Party[0].Statup("Obed", 90, 5)
                                $ Party[0].Statup("Inbt", 90, 5)
                                if Party[0] is RogueX:
                                        ch_r "Ох, вот и еще одна."
                                elif Party[0] is KittyX:
                                        ch_k "Мы создаем настоящий \"прайд\"."
                                elif Party[0] is EmmaX:
                                        ch_e "Полагаю, еще одна не повредит."
                                elif Party[0] is LauraX:
                                        ch_l "Как скажешь."
                                elif Party[0] is JeanX:
                                        ch_j "Ох, ладно. . ."
                                        ch_j "Но не привязывайся к ней."
                                elif Party[0] is StormX:
                                        ch_s "Думаю, от еще одной много вреда не будет?"
                                elif Party[0] is JubesX:
                                        ch_v "Хорошо, я подвинусь."
                                elif Party[0] is GwenX:
                                        ch_g "Боже, куда же нам ее впихнуть. . ."
                                elif Party[0] is BetsyX:
                                        ch_b "Пожалуй, мы сможем найти место для еще одной. . ."
                                elif Party[0] is DoreenX:
                                        ch_d "Ну, думаю, я смогу это принять. . ."
                                elif Party[0] is WandaX:
                                        ch_w ". . . Хорошо, мы со всем справимся."
                                $ Line = "yy"
            elif Line == "mn" or Line == "yn":
                    # if you said yes/maybe and they said no, but you insisted anyway
                    $Count = 0
                    while Count < 2:
                        if ApprovalCheck(Party[Count], 1600) and Party[Count].GirlLikeCheck(Newbie) >= 500:
                                # She likes you enough to roll over
                                $ Party[Count].FaceChange("sadside")
                                $ Party[Count].Statup("Love", 90, -5)
                                $ Party[Count].Statup("Obed", 90, 10)
                                if Party[Count] is RogueX:
                                        ch_r "Ну ладно, пусть так."
                                elif Party[Count] is KittyX:
                                        ch_k "Блин, ладно."
                                elif Party[Count] is EmmaX:
                                        ch_e "Полагаю, мы сможем найти для нее местечко."
                                elif Party[Count] is LauraX:
                                        ch_l "Как скажешь."
                                elif Party[Count] is JeanX:
                                        ch_j "Ох, ладно. . ."
                                        ch_j "Но не привязывайся к ней."
                                elif Party[Count] is StormX:
                                        ch_s "Если ты настаиваешь, я найду для нее место. . ."
                                elif Party[Count] is JubesX:
                                        ch_v "Думаю, мы можем поделиться."
                                elif Party[Count] is GwenX:
                                        ch_g "Думаю, мы можем найти ей место. . ."
                                elif Party[Count] is BetsyX:
                                        ch_b "Пожалуй, мы можем найти место для еще одной. . ."
                                elif Party[Count] is DoreenX:
                                        ch_d "Ну, думаю, я смогу это принять. . ."
                                elif Party[Count] is WandaX:
                                        ch_w ". . . Хорошо, мы со всем справимся."
                                $ Line = "yy"
                        else:
                                # She doesn't like you enough to roll over
                                $ Party[Count].FaceChange("angry",Eyes="side")
                                $ Party[Count].Statup("Love", 90, -25)
                                $ Party[Count].Statup("Inbt", 90, 10)
                                if Party[Count] is RogueX:
                                        ch_r "Ты мне не настолько нравишься, [RogueX.Petname]."
                                        ch_r "Я в этом не участвую."
                                elif Party[Count] is KittyX:
                                        if not Player.Male:
                                            ch_k "Ты не настолько милая, [KittyX.Petname]."
                                        else:
                                            ch_k "Ты не настолько милый, [KittyX.Petname]."
                                        ch_k "С меня хватит."
                                elif Party[Count] is EmmaX:
                                        ch_e "Не переоценивай себя, [EmmaX.Petname]."
                                        ch_e "Мы закончили."
                                elif Party[Count] is LauraX:
                                        ch_l "Ты заходишь слишком далеко, [LauraX.Petname]."
                                        ch_l "Я в этом не участвую."
                                elif Party[Count] is JeanX:
                                        ch_j "Меня одной более чем достаточно. . ."
                                        ch_j "Я в этом не участвую."
                                elif Party[Count] is StormX:
                                        ch_s "Пожалуй, я не смогу в этом участвовать."
                                elif Party[Count] is JubesX:
                                        ch_v "Нууу, тогда я пас."
                                elif Party[Count] is GwenX:
                                        ch_g "Мне не стоит становиться частью этого бардака."
                                elif Party[Count] is BetsyX:
                                        ch_b "Боюсь, ситуация вышла из-под контроля. . ."
                                        ch_b "Я не должна в этом участвовать."
                                elif Party[Count] is DoreenX:
                                        ch_d "Ну, мне это как-то не нравится!"
                                elif Party[Count] is WandaX:
                                        ch_w "Я не желаю участвовать во всем этом бардаке."
                                $ Party[Count].Traits.append("ex")
                                $ Party[Count].Break[0] = 5 + Party[Count].Break[1] + Party[Count].Cheated

                                $ Player.Harem.remove(Party[Count])
                                call Remove_Girl(Party[Count])
                        $ Count += 1
            #end "she said no but you insisted"


        if Line == "yy":
                if Newbie.Tag + "No" in Player.Traits:
                        $ Player.Traits.remove(Newbie.Tag + "No")
                $ Player.DrainWord(Newbie.Tag + "No",0,0,1)
                $ Player.Traits.append(Newbie.Tag + "Yes")
                $ Count = len(Player.Harem)
                while Count:
                        $ Count -= 1
                        $ Player.Harem[Count].DrainWord("saw with "+Newbie.Tag,0,0,1)      #removes "saw with Kitty" from traits
                "Вам нужно поговорить с [Newbie.Name_tvo]."
        else:
                $ Player.Traits.append(Newbie.Tag + "No")

        $ Party = []
        $Count = 0
        return

label Harem_Initiation(BO=[],BO2=[]):
    # This is called when a new girl is added to the pack
    # it makes them more open to sexing each other.
    $ BO = Player.Harem[:]
    python:
        for BX in BO:
            BO2 = Player.Harem[:]
            for BY in BO2:
                if BX is not BY and "poly " + BY.Tag not in BX.Traits:
                            BX.Traits.append("poly " + BY.Tag)
                if BX is not BY and "saw with " + BY.Tag in BX.Traits:
                            BY.DrainWord("saw with " + BY.Tag,0,0,1)      #removes "saw with Kitty" from traits
    return
## end Harem _Start//////////////////////////////////////////////////////////


#start study session / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Study_Session(BO=[]): #rkeljsvgbdw
            #study events, girl is the lead girl in the scene
            $ Party = []

            $ BO = TotalGirls[:]
            python:
                for BX in BO:
                    if BX.Loc == bg_current:
                            Party.append(BX)

            if not Party:
                "Здесь некому составить вам компанию."
                menu:
                    "Все равно заниматься?"
                    "Да":
                        $ Player.XP += 5
                        $ Round -= 30 if Round >= 30 else Round
                    "Неважно.":
                        pass
                return

            $ renpy.random.shuffle(Party)

            if Time_Count >= 3: #night time
                if Party[0] is JubesX and len(Party) < 2:
                    #jubilee will do this at night, if she's the only one in.
                    pass
                else:
                    if EmmaX in Party:
                            ch_e "Уже как-то поздновато для занятий, возможно, завтра."
                    elif Party[0] is RogueX:
                            ch_r "Уже слегка поздновато для учебы, может быть, завтра."
                    elif Party[0] is KittyX:
                            ch_k "Уже слегка поздновато для учебы. . . Давай завтра?"
                    elif Party[0] is LauraX:
                            ch_l "Уже поздно. Может завтра."
                    elif Party[0] is JeanX:
                            ch_j "-Зевает- Может быть, завтра. . ."
                    elif Party[0] is StormX:
                            ch_s "Уже немного поздно для учебы."
                    elif Party[0] is JubesX:
                            ch_v "Нууу, уже довольно поздно. . ."
                            ch_v "Не думаю, что вам это будет полезно, ребята. . ."
                    elif Party[0] is GwenX:
                            ch_g "Не знаю, уже довольно поздно. . ."
                    elif Party[0] is BetsyX:
                            ch_b "Боюсь, уже слишком поздно для этого. . ."
                    elif Party[0] is DoreenX:
                            ch_d "Нам нужно хорошо выспаться. . ."
                    elif Party[0] is WandaX:
                            ch_w "Я не собираюсь заниматься так поздно."
                    $ Party = []
                    return

            if Round <= 30:
                    if EmmaX in Party:
                            ch_e "Боюсь, я как раз хотела отдохнуть, возможно, в другой раз. . ."
                    elif Party[0] is RogueX:
                            ch_r "Я не знаю, найду ли я на это время, может, если позже. . ."
                    elif Party[0] is KittyX:
                            ch_k "Я не знаю, найду ли я на это время, может, если позже. . ."
                    elif Party[0] is LauraX:
                            ch_l "Я собиралась отдохнуть, может позже."
                    elif Party[0] is JeanX:
                            ch_j "Мне нужно отдохнуть, дай мне минутку. . ."
                    elif Party[0] is StormX:
                            ch_s "Мне нужен небольшой отдых, возможно, через несколько минут."
                    elif Party[0] is JubesX:
                            ch_v "Мы могли бы сначала перекусить. . ."
                    elif Party[0] is GwenX:
                            ch_g "Давай сначала немного отдохнем, а затем приступим. . ."
                    elif Party[0] is BetsyX:
                            ch_b "Возможно, после того, как мы немного отдохнем. . ."
                    elif Party[0] is DoreenX:
                            ch_d "Может, нам сначала отдохнуть?"
                    elif Party[0] is WandaX:
                            ch_w "Сначала я хочу передохнуть."
                    $ Party = []
                    return

            elif EmmaX in Party and len(Party) >= 2:
                    ch_e "Пожалуй, вам не помешает немного позаниматься."
            else:
                    if EmmaX in Party:
                            ch_e "Отлично."
                    elif Party[0] is RogueX:
                            ch_r "Конечно."
                    elif Party[0] is KittyX:
                            ch_k "Конечно."
                    elif Party[0] is LauraX:
                            ch_l "Хорошо."
                    elif Party[0] is JeanX:
                            ch_j "Наверное."
                    elif Party[0] is StormX:
                            ch_s "Полагаю, мы могли бы пройтись по нескольким вопросам. . ."
                    elif Party[0] is JubesX:
                            ch_v "Думаю, мы могли бы позаниматься. . ."
                    elif Party[0] is GwenX:
                            ch_g "Конечно. . ."
                    elif Party[0] is BetsyX:
                            ch_b "Непременно. . ."
                    elif Party[0] is DoreenX:
                            ch_d "Конечно!"
                    elif Party[0] is WandaX:
                            ch_w "Конечно."


            $ Player.RecentActions.append("study")
            $ Player.XP += 5
            $ Trigger = 0
            $ Line = renpy.random.choice(["Вы пробегаетесь по основам, все проходит довольно гладко.",
                    "Вы готовитесь к тесту по биологии мутантов.",
                    "Вы готовитесь к тесту по математике.",
                    "Вам становится скучно и вместо этого вы обсуждаете различные сплетни.",
                    "Вы занимаетесь в течение нескольких часов, это было весело.",
                    "Вы проводите несколько часов, готовясь к тесту.",
                    "Вы изучаете курс геймдизайна."])
            "[Line]"
            $ Line = 0

            $ Party[0].Statup("Love", 80, 2)
            $ Party[0].XP += 5
            if len(Party) >= 2:
                    $ Party[1].Statup("Love", 80, 2)
                    $ Party[0].GLG(Party[1],700,5,1)
                    $ Party[1].GLG(Party[0],700,5,1)
                    $ Party[1].XP += 5
                    #raises both girl's likes of each other by 5 if they are under 70

            $ D20 = renpy.random.randint(1, 20)

            #There might be sexy time
            if len(Party) >= 2 and EmmaX in Party and "three" not in EmmaX.History:
                $ Line = "no"

            if Line != "no" and D20 >= 10:
                call Frisky_Study
            else:
                # if there is no frisky stuff
                if EmmaX in Party:
                        ch_e "Боюсь, уже слегка поздно, нам нужно закончить. . ."
                elif Party[0] is RogueX:
                        ch_r "Уже как-то поздно, нам пора закончить. . ."
                elif Party[0] is KittyX:
                        ch_k "Уже поздно, нам, наверное, пора остановиться. . ."
                elif Party[0] is LauraX:
                        ch_l "Я устала."
                elif Party[0] is JeanX:
                        ch_j "Ладно, хватит. . ."
                elif Party[0] is StormX:
                        ch_s "Думаю, пока этого будет достаточно."
                elif Party[0] is JubesX:
                        ch_v "Фух, голова болит!"
                elif Party[0] is GwenX:
                        ch_g "Ну ладно, хватит. . ."
                elif Party[0] is BetsyX:
                        ch_b "Это было довольно изнурительно. . ."
                elif Party[0] is DoreenX:
                        ch_d "Ладно, я думаю, этого достаточно. . ."
                elif Party[0] is WandaX:
                        ch_w "Ладно, на сегодня хватит учебы."
                $ Player.XP += 5
            $ Line = 0
            $ Party = []
            if Time_Count >= 3: #if it's night, Jubilee only
                    $ Round = 10
                    return
            call Wait
            call Girls_Location
            return
#End Study session  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Frisky study session / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Frisky_Study(Prime_Bonus=0,Second=0,Line=0,Second_Bonus=0): #rkeljsvgbdw
            # Second is a potential second girl, (make sure to set if no second girl)
            # Prime_Bonus,Second_Bonus=0 is needed by the Datebreak code but does nothing
            # Prime_Bonus is reappropriated to denote a second pass through

            call Shift_Focus(Party[0])

            if len(Party) >= 2:
                    $ Second = Party[1]

            if Party[0] is EmmaX and "classcaught" not in EmmaX.History:
                    #if you've never caught her having sex before.
                    "[EmmaX.Name] на мгновение прижимается к вам, но потом спохватывается и отстраняется."
            elif Party[0] is EmmaX and Second and ("three" not in EmmaX.History or "taboo" not in EmmaX.History):
                    #if there's a second girl and Emma doesn't do threesomes yet
                    "[EmmaX.Name] начинает наклоняться к вам, но потом замечает [Second.Name_vin]."
                    $ Party[0].FaceChange("sly",1,Eyes="side")
                    "Она тут же останавливается и слегка смущается."
            elif D20 > 17 and ApprovalCheck(Party[0], 1000) and (Party[0].Blow > 5 or Party[0].CUN > 5):
                    $ Line = "blow"
            elif D20 > 14 and Party[0] is JubesX and ApprovalCheck(Party[0], 1000) and (Party[0].Blow or Party[0].CUN):
                    $ Line = "blow"
            elif D20 > 14 and ApprovalCheck(Party[0], 1000) and (Party[0].Hand >= 5 or Party[0].Finger > 5):
                    $ Line = "hand"
            elif D20 > 10 and (ApprovalCheck(Party[0], 1300) or (Party[0].Mast and ApprovalCheck(Party[0], 1000))) and Party[0].Lust >= 70:
                    $ Line = "masturbate"
            elif D20 > 10 and ApprovalCheck(Party[0], 1200) and Party[0].Lust >= 30:
                    $ Line = "strip"
            elif ApprovalCheck(Party[0], 700) and Party[0].Kissed > 1:
                    $ Line = "kissing"
            elif ApprovalCheck(Party[0], 500):
                    $ Line = "snuggle"
                    if Party[0] is not JeanX or ApprovalCheck(Party[0], 700,"L"):
                            $ Line = "snuggle"
                    else:
                            "[Party[0].Name] ненадолго прижимается к вашему плечу, но потом спохватывается и отстраняется."
                            $ Line = 0
            # End first phase

            if RogueX in Party and KittyX in Party and "KittyPuss" not in RogueX.History:
                        #Plays Rogue X Kitty scene
                        if ApprovalCheck(KittyX, 400, "I") and ApprovalCheck(KittyX,1350):
                                #if she's ready to clear the pussy part
                                call Rogue_and_Kitty
                                return
                        elif "KittyTits" not in RogueX.History and ApprovalCheck(KittyX, 300, "I") and ApprovalCheck(KittyX,1050):
                                #if she's ready to clear the breast part
                                call Rogue_and_Kitty
                                return
                        elif "KittyKiss" not in RogueX.History and ApprovalCheck(KittyX, 200, "I") and ApprovalCheck(KittyX,850):
                                #if she's ready to clear the kiss part
                                call Rogue_and_Kitty
                                return

            if Line and not Player.Male and "girltalk" not in Party[0].History:
                        if ApprovalCheck(Party[0], 1100):
                                call expression Party[0].Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                        if "nogirls" in Party[0].History:
                                $ Line = "snuggle"

            if not Line and len(Party) >= 2 and not Prime_Bonus:
                        # this sends it back to the start if there is a second girl
                        # it swaps their order to give the second girl a chance
                        $ Party.reverse()
                        if Second == Party[0]:
                                $ Second = Party[1]
                        call Frisky_Study(1)
                        return
            elif not Line or Line == "strip":
                        pass
            elif Line == "blow":
                        $ Party[0].FaceChange("sly")
                        if Party[0] is KittyX:
                                "[KittyX.Name] проникает рукой сквозь ваш учебник и кладет ее на ваши колени."
                                if Player.Male:
                                        "Она расстегивает ваши штаны, вытаскивает член и начинает медленно поглаживать его."
                                else:
                                        "Она расстегивает ваши штаны, находит ваш клитор и начинает медленно поглаживать его."
                                "Затем она ныряет головой под книгу и начинает его облизывать."
                        else:
                                "[Party[0].Name] хищно улыбается и начинаю расстегивать ваши штаны."
                                if Player.Male:
                                        "Она вытаскивает ваш член и засовывает его себе в рот."
                                else:
                                        "Она находит ваш клитор и начинает его облизывать."
            elif Line == "hand":
                        $ Party[0].FaceChange("sly")
                        if Party[0] is KittyX:
                                "[KittyX.Name] проникает рукой сквозь ваш учебник и кладет ее на ваши колени."
                                if Player.Male:
                                        "Она проводит пальцем по вашему стояку, ее рука проходит сквозь штаны и касается напрямую вашего голого члена."
                                        "Она расстегивает ваши штаны, вытаскивает член и начинает медленно поглаживать его."
                                else:
                                        "Она проводит пальцем по вашей промежности, ее рука проходит сквозь штаны и касается вашей голой киски."
                                        "Она расстегивает ваши штаны, кладет палец на клитор и начинает медленно поглаживать его."
                        elif Party[0] is JeanX and D20 > 15:
                                if not Player.Male:
                                    "Во время занятия, вы вдруг почувствовали прикосновение к своей киске."
                                else:
                                    "Во время занятия, вы вдруг почувствовали прикосновение к своему члену."
                                menu:
                                    "Не сопротивляться":
                                            "Через мгновение вы ощущутили, как невидимая сила начала растегивать молнию на ваших штанах."
                                            if Player.Male:
                                                    "Ваш член выскакивает из ваших штанов, наполовину приподнятый его естественное реакцией, а наполовину - за счет невидимой силы. . ."
                                            $ Party[0].FaceChange("sly",Eyes="leftside")
                                            if not Player.Male:
                                                "Вы переводите взгляд на [JeanX.Name_vin], на ее лице появилась веселая улыбка, а давление на вашу киску усилилось."
                                                "Вы начали ощущать сильное поглаживание по всей ее площади."
                                            else:
                                                "Вы переводите взгляд на [JeanX.Name_vin], на ее лице появилась веселая улыбка, а давление на ваш член усилилось."
                                                "Вы начали ощущать сильное поглаживание по всей его длине."
                                            if Player.Male:
                                                    "Ощущения похожи на то, словно вам сосут или дрочат."
                                            else:
                                                    "Ощущения похожи на то, словно вам ее лижут. . ."
                                            if not Player.Male:
                                                "[JeanX.Name] приобнимает вас за плечи, пока невидимая сила занимается вашей киской. . ."
                                            else:
                                                "[JeanX.Name] приобнимает вас за плечи, пока невидимая сила занимается вашим членом. . ."
                                    "Применить свою способность, чтобы освободиться":
                                            $ Party[0].FaceChange("sad")
                                            $ Party[0].Statup("Love", 80, -2)
                                            $ Party[0].Statup("Obed", 50, 3)
                                            $ Party[0].Statup("Obed", 80, 5)
                                            $ Party[0].Statup("Inbt", 90, -2)
                                            ch_j "Aw. . ."
                                            $ Line = 0
                        else:
                                "[Party[0].Name] хищно улыбается и начинаю расстегивать ваши штаны."
                                if Player.Male:
                                        "Она вытаскивает ваш член и начинает медленно его ласкать."
                                else:
                                        "Она кладет пальцы на ваш клитор и начинает медленно его ласкать."
            elif Line == "masturbate":
                        $ Party[0].FaceChange("sly", Eyes="side")
                        "[Party[0].Name] откидывается немного назад и начинает поглаживать свою киску."
                        $ Trigger = "masturbation"
            elif Line == "kissing":
                        "[Party[0].Name] наклоняется поближе к вам, чтобы поцеловать."
            elif Line == "snuggle":
                        "[Party[0].Name] прижимется к вам, так вы и проводите остаток занятия."


            if Line == "strip":
                    if Party[0] is not EmmaX and EmmaX in Party and ApprovalCheck(EmmaX, 1200) and EmmaX.Lust >= 30:
                            $ Party.reverse()
                            if len(Party) >= 2 and Second == Party[0]:
                                    $ Second = Party[1]
                            # Emma always takes priority
                    if StormX in Party and renpy.random.randint(1,2) > 1:
                            $ Party.reverse()
                            if len(Party) >= 2 and Second == Party[0]:
                                    $ Second = Party[1]
                            # Storm sometimes takes priority

                    call Group_Strip_Study
            elif Line and Line != "snuggle" and len(Party) < 2:
                    #if sex stuff is happening but only one girl
                    call SexAct(Line) # call expression Party[0].Tag + "_SexAct" pass (Line)
            elif Line:
                    #if something sexual is happening, checks if other girl is cool
                    if Line == "snuggle":
                                call Date_Sex_Break(Party[0],Second,2)
                                if _return == 3:
                                        $ Second.FaceChange("angry")
                                        "[Second.Name] смотрит на вас с легким неодобрением."
                                        $ Party[0].GLG(Second,700,5,1)
                                        $ Second.GLG(Party[0],700,5,1)
                    else:
                                call Date_Sex_Break(Party[0],Second)

                    if _return == 4:
                            if Line == "blow":
                                    if Player.Male:
                                            "[Party[0].Name] выпускает ваш член из своего рта."
                                    else:
                                            "[Party[0].Name] делает последний лизь и отстраняется."
                                    "Вы застегиваете свои штаны."
                            elif Line == "hand":
                                    if Player.Male:
                                            "[Party[0].Name] отпускает ваш член."
                                    else:
                                            "[Party[0].Name] последний раз касается вашего клитора и отстраняется."
                                    "Вы застегиваете свои штаны."
                            else:
                                    "[Party[0].Name] прекращает свои действия."

                            $ Party[0].FaceChange("sad")
                            if Party[0] is RogueX:
                                    ch_r "Облом."
                            elif Party[0] is KittyX:
                                    ch_k "Бууу."
                            elif Party[0] is EmmaX:
                                    ch_e "Ох, ну хорошо."
                            elif Party[0] is LauraX:
                                    ch_l "Так тому и быть."
                            elif Party[0] is JeanX:
                                    ch_j "Оу. . ."
                            elif Party[0] is StormX:
                                    ch_s "Как жаль."
                            elif Party[0] is JubesX:
                                    ch_v "Черт!"
                            elif Party[0] is GwenX:
                                    ch_g "Оу!"
                            elif Party[0] is BetsyX:
                                    ch_b "Жаль. . ."
                            elif Party[0] is DoreenX:
                                    ch_d "Блин. . ."
                            elif Party[0] is WandaX:
                                    ch_w "Облом."
                    elif Line != "snuggle":
                        #Plays if you didn't refuse to stop
                        #either the other girl left, or it just continues with both
                        if _return == 3:
                                #if the other girl took off. . .
                                if Party[0] is RogueX:
                                        ch_r "Не против продолжить?"
                                elif Party[0] is KittyX:
                                        ch_k "Я могу продолжить?"
                                elif Party[0] is EmmaX:
                                        ch_e "Ты не против, если я продолжу?"
                                elif Party[0] is LauraX:
                                        ch_l "Мне продолжить?"
                                elif Party[0] is JeanX:
                                        ch_j "Ладно, вернемся к делу. . ."
                                elif Party[0] is StormX:
                                        ch_s "Что ж, ты хочешь, чтобы я продолжила?"
                                elif Party[0] is JubesX:
                                        ch_v "Не интересует?"
                                elif Party[0] is GwenX:
                                        ch_g "Что дальше. . ?"
                                elif Party[0] is BetsyX:
                                        ch_b "Могу я продолжить?"
                                elif Party[0] is DoreenX:
                                        ch_d "Оу, как жаль. Эм, что теперь. . ?"
                                elif Party[0] is WandaX:
                                        ch_w "Что дальше. . ?"
                                menu:
                                    extend ""
                                    "Что ж, продолжим.":
                                            $ Party[0].FaceChange("sly")
                                            if Party[0] is RogueX:
                                                    ch_r "Хорошо."
                                            elif Party[0] is KittyX:
                                                    ch_k "Здорово."
                                            elif Party[0] is EmmaX:
                                                    ch_e "Прекрасно."
                                            elif Party[0] is LauraX:
                                                    ch_l "Эм."
                                            elif Party[0] is JeanX:
                                                    ch_j "Ммм. . ."
                                            elif Party[0] is StormX:
                                                    ch_s "Именно на это я и надеялась. . ."
                                            elif Party[0] is JubesX:
                                                    ch_v "Славно!"
                                            elif Party[0] is GwenX:
                                                    ch_g "Круто."
                                            elif Party[0] is BetsyX:
                                                    ch_b "Восхитительно."
                                            elif Party[0] is DoreenX:
                                                    ch_d "Здорово!"
                                            elif Party[0] is WandaX:
                                                    ch_w "Клево."
                                    "Мы должны остановиться.":
                                            $ Party[0].FaceChange("sad")
                                            if Party[0] is RogueX:
                                                    ch_r "Пфф."
                                            elif Party[0] is KittyX:
                                                    ch_k "Отстой."
                                            elif Party[0] is EmmaX:
                                                    if not Player.Male:
                                                        ch_e "Взяла и все испортила."
                                                    else:
                                                        ch_e "Взял и все испортил."
                                            elif Party[0] is LauraX:
                                                    ch_l "Грр."
                                            elif Party[0] is JeanX:
                                                    ch_j "Оу. . ."
                                            elif Party[0] is StormX:
                                                    ch_s "Жаль."
                                            elif Party[0] is JubesX:
                                                    ch_v "Оу!"
                                            elif Party[0] is GwenX:
                                                    ch_g "Черт."
                                            elif Party[0] is BetsyX:
                                                    ch_b "Фи."
                                            elif Party[0] is DoreenX:
                                                    ch_d "Оу. . ."
                                            elif Party[0] is WandaX:
                                                    ch_w "Жаль."
                                            $ Party[0].FaceChange("normal")
                                            return
                        # end "if the other girl took off"
                        if not Player.Male:
                                $ Line = "cun" if Line == "blow" else Line
                                $ Line = "finger" if Line == "hand" else Line
                        call SexAct(Line) # call expression Party[0].Tag + "_SexAct" pass (Line)
                    if len(Party) >= 2:
                        $ Party[0].GLG(Party[1],900,10,1)
                        $ Party[1].GLG(Party[0],900,10,1)
                        #if still two girls, raise both likes by 10
            else:
                        #if nothing sexy happened. . .
                        return
            if Party:
                    $ Party[0].AddWord(1,0,0,0,"frisky")
            if len(Party) >= 2:
                    $ Party[1].AddWord(1,0,0,0,"frisky")

            "Что ж, вы, безусловно, неплохо провели время за учебой. . ."
            return

#end Frisky study session / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Girls_Caught(Girl=0,TotalCaught=0,Shame=0,Count=0,T_Pet=0,BO=[]): #rkeljsvgbdw
    call Shift_Focus(Girl)
    call Checkout
    call AnyLine(Girl,"!!!")
    $ Line = Trigger
    call Trig_Reset
    $ Girl.OutfitChange()
    $ BO = TotalGirls[:]
    while BO:
            if BO[0].Loc == bg_current:
                    $ BO[0].Loc = "bg study"
            $ TotalCaught += BO[0].Caught
            $ BO.remove(BO[0])
    $ bg_current = "bg study"
    call Set_The_Scene(0)
    show Professor at SpriteLoc(StageLeft)

    call QuickDisplay(Girl,StageRight,50)

    call OutfitShame(Girl,20)
    if Partner:
            call OutfitShame(Partner,20)

    $ Count = Girl.Caught

    call QuickDisplay(Partner,StageFarRight,50)

    call XavierFace("shocked")
    $ Girl.FaceChange("sad")
    if (Girl is EmmaX or Partner is EmmaX) and (Girl is StormX or Partner is StormX):
            ch_x "Я очень разочарован в вас!"
            ch_x "Вы ОБЕ должны это хорошо понимать!"
    elif Girl is StormX or Partner is StormX:
            ch_x "Я очень разочарован вашим поведением, и в особенности твоим, Ороро."
    elif Girl is EmmaX or Partner is EmmaX:
            ch_x "Я очень разочарован вашим поведением, и в особенности твоим, Эмма."
    else:
            ch_x "Я очень разочарован вашим поведением."

    if "EmmaStorm" in EmmaX.History:
        if ApprovalCheck(EmmaX, 1200) and ApprovalCheck(StormX, 1200): #and "EmmaStormQueue" not in EmmaX.Traits:
            $ EmmaX.AddWord(1,0,0,"EmmaStormQueue") #adds to Traits, queuing up a redo of event
    elif "classcaught" in EmmaX.History and "met" in StormX.History and (EmmaX.SEXP >= 15 or StormX.SEXP >= 15):
            $ EmmaX.AddWord(1,0,0,"EmmaStormQueue") #adds to Traits, queuing up a redo of event


    if Line == "fondle thighs" or Line == "fondle breasts" or Line == "fondle pussy" or Line == "hotdog" or Line == "hand":
        ch_x "Вы лапаете друг друга, словно животные!"
    elif Line == "dildo pussy" or Line == "dildo anal":
        ch_x "Используете эти. . . устройства друг на друге, как грязно!"
    elif Line == "lick pussy":
        ch_x "Занимаетесь. . . кунилингусом. . . вы все тут заляпали. . ."
    elif Line == "blow":
        if Player.Male:
                ch_x "Прямо тут, на людях, да с его {i}пенисом{/i} во рту. . ."
        else:
                ch_x "Прямо тут, на людях, с лицом у нее между ног. . ."
    else:
        ch_x "Сексуальные отношения в таком общественном месте выставляют вас в очень плохом свете!"

    if "switchxavier" in Player.History:
            call Xavier_Switch

    if Girl.Shame >= 40 or (Partner and Partner.Shame >= 40):
            if Girl.Shame >= 40:
                    ch_x "[Girl.Name], дорогая, ты практически голая! Хотя бы накинь полотенце!"
                    "Он бросает [Girl.Name_dat] полотенце."
            else:
                    ch_x "[Partner.Name], дорогая, ты практически голая! Хотя бы накинь полотенце!"
                    "Он бросает [Partner.Name_dat] полотенце."
            show blackscreen onlayer black
            $ BO = TotalGirls[:]
            while BO:
                    if BO[0].Loc == bg_current and (not BO[0].Over and not BO[0].Chest):
                            $ BO[0].Over = "towel"
                    $ BO.remove(BO[0])
            hide blackscreen onlayer black
            if (Girl is StormX or Partner is StormX) and StormX.Over == "towel":
                    ch_x ". . ."
                    ch_x "Ороро, ради Бога. . ."
                    ch_x "Надень какую-нибудь одежду!"
                    show blackscreen onlayer black
                    $ StormX.Over = "white shirt"
                    $ StormX.Legs = "skirt"
                    hide blackscreen onlayer black
                    ch_x ". . . хорошо."

    elif Girl.Shame >= 20:
            ch_x "[Girl.Name], дорогая моя, твой вид просто возмутителен."

    if Girl.Caught:
            #if Caught for Girl > 0
            ch_x "И это происходит уже не в первый раз!"

    if Partner:
            $ Partner.FaceChange("surprised",2)
            if Partner in Rules:
                    if Partner is KittyX:
                        "Ксавье бросает взгляд на [KittyX.Name_vin], которая в этот момент уставилась в телефон. . ."
                    elif Partner is LauraX:
                        $ Laura_Arms = 2
                        "Ксавье бросает взгляд на [LauraX.Name_vin], которая в этот момент рассматривает свой кулак. . ."
                        $ Laura_Arms = 1
                    ch_x "И. . . хм, я готов поклясться с вами был кто-то еще. . ."
            else:
                    ch_x "И, [Partner.Name], ты просто наблюдала за происходящим!"
            $ Partner.FaceChange("bemused",1, Eyes="side")

    if EmmaX.Loc == bg_current and EmmaX not in Rules:
        if not EmmaX.Caught:
                ch_x "Эмма, тебе доверили преподавать здесь, я не могу допустить, чтобы ты настолько сближалась со студентами."
                ch_x "И в особенности в общественных местах нашего учебного заведения!"
                ch_x "Что это все значит?"
                ch_x "Думаешь, будет уместно, если я вдруг начну кататься по кориторам с мисс Грей на коленях?"
                call XavierFace("hypno")
                ch_x "Просто представь. . . я вожу руками по ее упругому молодому телу, не заботясь ни о чем. . ."
                call XavierFace("happy")
                if JeanX.Loc == bg_current:
                        "Вы бросаете взгляд на [JeanX.Name_vin], она пожимает плечами."
                ch_x ". . ."
                call XavierFace("shocked")
                ch_x "Так, ладно, как я говорил. . ."
        else:
                ch_x "Эмма, не могу поверить, что этот разговор у нас уже не впервые."
                ch_x "Надеюсь, это в последний раз."
    if StormX.Loc == bg_current and StormX not in Rules:
        if not StormX.Caught:
                if EmmaX.Loc == bg_current and EmmaX not in Rules:
                        ch_x "И Ороро! Ты лучше всех знаешь, что лучше не сближаться со студентами!"
                else:
                        ch_x "Ороро, тебе доверили здесь преподавать, я не могу допустить, чтобы ты настолько сближалась со студентами."
                ch_x "Я хорошо осведомлен о твоих богемных наклонностях, но на людях ты должна вести себя прилично."
                ch_x "Какой пример ты подаешь студентам?"
                ch_x "А если бы я участвовал в подобных выходках?"
                call XavierFace("hypno")
                ch_x "Просто представь. . . я катаюсь по коридорам, а мои голые яйца обдуваются ветерком. . ."
                call XavierFace("happy")
                ch_x ". . ."
                call XavierFace("shocked")
                ch_x "Ладно, не будем отвлекаться! . ."
        else:
                if EmmaX.Loc == bg_current and EmmaX not in Rules:
                        ch_x "И Ороро! Мы уже говорили об этом раньше."
                else:
                        ch_x "Ороро, не могу поверить, что этот разговор у нас уже не впервые."
                ch_x "Надеюсь, что такого больше не повториться."

    $ Line = 0
    menu:
        ch_x "Итак, что вы можете сказать в свое оправдание?"
        "Извините, сэр, этого больше не повторится.":
                if RogueX.Loc == bg_current and RogueX.Caught < 3:
                            $ RogueX.Statup("Love", 70, 20)
                            $ RogueX.Statup("Inbt", 50, -15)
                            $ RogueX.Statup("Love", 90, 5)
                if KittyX.Loc == bg_current and KittyX.Caught < 3:
                            $ KittyX.Statup("Love", 70, 10)
                            $ KittyX.Statup("Inbt", 30, -25)
                            $ KittyX.Statup("Inbt", 50, -10)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:
                            $ EmmaX.Statup("Love", 70, 5)
                            $ EmmaX.Statup("Inbt", 30, -15)
                if LauraX.Loc == bg_current and LauraX.Caught < 3:
                            $ LauraX.Statup("Inbt", 30, -20)
                            $ LauraX.Statup("Inbt", 50, -10)
                if JeanX.Loc == bg_current and JeanX.Caught < 3:
                            $ JeanX.Statup("Obed", 30, -20)
                            $ JeanX.Statup("Obed", 50, -10)
                if StormX.Loc == bg_current and StormX.Caught < 3:
                            $ StormX.Statup("Love", 70, 5)
                            $ StormX.Statup("Inbt", 30, -5)
                if JubesX.Loc == bg_current and JubesX.Caught < 3:
                            $ JubesX.Statup("Love", 70, 10)
                            $ JubesX.Statup("Obed", 70, 5)
                            $ JubesX.Statup("Inbt", 30, -10)
                            $ JubesX.Statup("Inbt", 50, -5)
                if GwenX.Loc == bg_current and GwenX.Caught < 3:
                            $ GwenX.Statup("Love", 70, 10)
                            $ GwenX.Statup("Obed", 70, 5)
                            $ GwenX.Statup("Inbt", 30, -10)
                            $ GwenX.Statup("Inbt", 50, -5)
                if BetsyX.Loc == bg_current and BetsyX.Caught < 3:
                            $ BetsyX.Statup("Love", 70, 3)
                            $ BetsyX.Statup("Obed", 70, -2)
                            $ BetsyX.Statup("Inbt", 50, -2)
                if DoreenX.Loc == bg_current and DoreenX.Caught < 3:
                            $ DoreenX.Statup("Love", 50, 2)
                            $ DoreenX.Statup("Love", 70, 3)
                            $ DoreenX.Statup("Obed", 70, -2)
                            $ DoreenX.Statup("Inbt", 50, -2)
                if WandaX.Loc == bg_current and WandaX.Caught < 3:
                            $ WandaX.Statup("Love", 50, 2)
                            $ WandaX.Statup("Obed", 70, -5)
                            $ WandaX.Statup("Inbt", 50, -5)
                $ Girl.Statup("Obed", 50, -5)

                call XavierFace("happy")
                if Girl.Caught:
                    if not Player.Male:
                        ch_x "Ты ведь осознаешь, что занималась подобным уже. . . по крайней мере [Girl.Caught] раз. . ?"
                    else:
                        ch_x "Ты ведь осознаешь, что занимался подобным уже. . . по крайней мере [Girl.Caught] раз. . ?"
                elif Girl is EmmaX and TotalCaught:
                    if not Player.Male:
                        ch_x "Возможно, не с мисс Фрост, но ты ведь осознаешь, что занималась подобным уже. . ."
                    else:
                        ch_x "Возможно, не с мисс Фрост, но ты ведь осознаешь, что занимался подобным уже. . ."
                    ch_x "по крайней мере [TotalCaught] раз. . ?"
                    $ Girl.FaceChange("sexy",Brows="confused")
                elif Girl is StormX and TotalCaught:
                    if not Player.Male:
                        ch_x "Возможно, не с мисс Манро, но ты ведь осознаешь, что занималась подобным уже. . ."
                    else:
                        ch_x "Возможно, не с мисс Манро, но ты ведь осознаешь, что занимался подобным уже. . ."
                    ch_x "по крайней мере [TotalCaught] раз. . ?"
                    $ Girl.FaceChange("sexy",Brows="confused")
                elif TotalCaught:
                    if not Player.Male:
                        ch_x "Возможно, не с этой молодой леди, но ты ведь осознаешь, что занималась подобным уже. . ."
                    else:
                        ch_x "Возможно, не с этой молодой леди, но ты ведь осознаешь, что занимался подобным уже. . ."
                    ch_x "по крайней мере [TotalCaught] раз. . ?"
                else:
                    ch_x "Хорошо, только не позволяй этому повториться снова."
                $ Count += 5
                if PunishmentX:
                    ch_x "Я продлеваю твое наказание на [Count] дней."
                else:
                    ch_x "Я уменьшаю твою ежедневную стипендию вдвое на [Count] дней."
                ch_x "А теперь возвращайтесь в свои комнаты и подумайте о своем поведение."
        #End "sorry"

        "Мы просто немного повеселились, верно, [Girl.Pet]?":
                $ Girl.NameCheck() #checks reaction to petname
                $ Girl.FaceChange("bemused")
                $ Girl.Statup("Lust", 90, 5)
                if RogueX.Loc == bg_current and RogueX.Caught < 5:
                        $ RogueX.Statup("Love", 70, 20)
                        $ RogueX.Statup("Love", 90, 10)
                if KittyX.Loc == bg_current and KittyX.Caught < 5:
                        $ KittyX.Statup("Inbt", 90, 10)
                        $ KittyX.Statup("Love", 90, 10)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 5:
                        $ EmmaX.Statup("Inbt", 90, 10)
                        $ EmmaX.Statup("Love", 90, 10)
                if LauraX.Loc == bg_current and LauraX.Caught < 5:
                        $ LauraX.Statup("Inbt", 90, 10)
                        $ LauraX.Statup("Obed", 90, 5)
                        $ LauraX.Statup("Love", 90, 5)
                if JeanX.Loc == bg_current and JeanX.Caught < 5:
                        $ JeanX.Statup("Inbt", 200, 10)
                        $ JeanX.Statup("Obed", 50, 5)
                        $ JeanX.Statup("Obed", 90, 5)
                        $ JeanX.Statup("Love", 90, 5)
                if StormX.Loc == bg_current and StormX.Caught < 5:
                        $ StormX.Statup("Inbt", 90, 15)
                        $ StormX.Statup("Obed", 50, 5)
                        $ StormX.Statup("Love", 90, 5)
                if JubesX.Loc == bg_current and JubesX.Caught < 5:
                        $ JubesX.Statup("Inbt", 90, 5)
                        $ JubesX.Statup("Obed", 80, 5)
                        $ JubesX.Statup("Love", 90, 10)
                if GwenX.Loc == bg_current and GwenX.Caught < 5:
                        $ GwenX.Statup("Inbt", 90, 10)
                        $ GwenX.Statup("Obed", 80, 5)
                        $ GwenX.Statup("Love", 90, 5)
                if BetsyX.Loc == bg_current and BetsyX.Caught < 5:
                        $ BetsyX.Statup("Obed", 70, 5)
                        $ BetsyX.Statup("Inbt", 50, 10)
                if DoreenX.Loc == bg_current and DoreenX.Caught < 5:
                        $ DoreenX.Statup("Love", 80, -2)
                        $ DoreenX.Statup("Obed", 70, 3)
                        $ DoreenX.Statup("Inbt", 50, 2)
                if WandaX.Loc == bg_current and WandaX.Caught < 5:
                        $ WandaX.Statup("Love", 60, 3)
                        $ WandaX.Statup("Love", 80, 2)
                        $ WandaX.Statup("Obed", 70, 3)
                        $ WandaX.Statup("Inbt", 50, 2)
                        $ WandaX.Statup("Inbt", 70, 2)

                call XavierFace("angry")
                $ Count += 10
                ch_x "Если ты так к этому относишься, возможно, потребуются более жесткие меры."
                if PunishmentX:
                    ch_x "Я продлеваю твое наказание на [Count] дней."
                else:
                    ch_x "Я уменьшаю твою ежедневную стипендию вдвое на [Count] дней."

                if RogueX.Loc == bg_current and RogueX.Caught < 3:
                        $ RogueX.Statup("Obed", 50, 20)
                        $ RogueX.Statup("Obed", 90, 20)
                        $ RogueX.Statup("Inbt", 30, -20)
                        $ RogueX.Statup("Inbt", 50, -10)
                if KittyX.Loc == bg_current and KittyX.Caught < 3:
                        $ KittyX.Statup("Obed", 50, 20)
                        $ KittyX.Statup("Obed", 90, 20)
                        $ KittyX.Statup("Inbt", 30, -20)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:
                        $ EmmaX.Statup("Obed", 50, 20)
                        $ EmmaX.Statup("Obed", 90, 20)
                        $ EmmaX.Statup("Inbt", 30, -20)
                if LauraX.Loc == bg_current and LauraX.Caught < 3:
                        $ LauraX.Statup("Obed", 50, 20)
                        $ LauraX.Statup("Obed", 90, 20)
                        $ LauraX.Statup("Inbt", 30, -20)
                if JeanX.Loc == bg_current and JeanX.Caught < 3:
                        $ JeanX.Statup("Obed", 50, 20)
                        $ JeanX.Statup("Obed", 90, 20)
                if StormX.Loc == bg_current and StormX.Caught < 3:
                        $ StormX.Statup("Obed", 50, 20)
                        $ StormX.Statup("Inbt", 30, -10)
                if JubesX.Loc == bg_current and JubesX.Caught < 3:
                        $ JubesX.Statup("Obed", 70, 10)
                        $ JubesX.Statup("Inbt", 30, -5)
                if GwenX.Loc == bg_current and GwenX.Caught < 3:
                        $ GwenX.Statup("Obed", 80, 5)
                        $ GwenX.Statup("Inbt", 90, -5)
                if BetsyX.Loc == bg_current and BetsyX.Caught < 3:
                        $ BetsyX.Statup("Obed", 70, 5)
                        $ BetsyX.Statup("Inbt", 50, -2)
                if DoreenX.Loc == bg_current and DoreenX.Caught < 3:
                        $ DoreenX.Statup("Inbt", 50, -2)
                if WandaX.Loc == bg_current and WandaX.Caught < 5:
                        $ WandaX.Statup("Obed", 70, 2)
                        $ WandaX.Statup("Inbt", 70, -1)

                ch_x "Я сыт вами по горло, убирайтесь."
        #End "Little fun"

        "Скажу лишь. . . План Омега, [RogueX.Name]." if Girl is RogueX and Player.Lvl >= 5:
                call Xavier_Plan(RogueX)
        "Скажу лишь. . . План Каппа, [KittyX.Name]!" if Girl is KittyX and Player.Lvl >= 5:
                call Xavier_Plan(KittyX)
        "Скажу лишь. . . План Пси, [EmmaX.Name]!" if Girl is EmmaX and Player.Lvl >= 5:
                call Xavier_Plan(EmmaX)
        "Скажу лишь. . . План Ки, [LauraX.Name]!" if Girl is LauraX and Player.Lvl >= 5:
                call Xavier_Plan(LauraX)
        "Скажу лишь. . . План Альфа, [JeanX.Name]!" if Girl is JeanX and Player.Lvl >= 5:
                call Xavier_Plan(JeanX)
        "Скажу лишь. . . План Ро, [StormX.Name]!" if Girl is StormX and Player.Lvl >= 5:
                call Xavier_Plan(StormX)
        "Скажу лишь. . . План Зета, [JubesX.Name]!" if Girl is JubesX and Player.Lvl >= 5:
                call Xavier_Plan(JubesX)
        "Скажу лишь. . . План Гамма, [GwenX.Name]!" if Girl is GwenX and Player.Lvl >= 5:
                call Xavier_Plan(GwenX)
        "Скажу лишь. . . План Бета, [BetsyX.Name]!" if Girl is BetsyX and Player.Lvl >= 5:
                call Xavier_Plan(BetsyX)
        "Скажу лишь. . . План Дельта, [DoreenX.Name]!" if Girl is DoreenX and Player.Lvl >= 5:
                call Xavier_Plan(DoreenX)
        "Скажу лишь. . . План Эпсилон, [WandaX.Name]!" if Girl is WandaX and Player.Lvl >= 5:
                call Xavier_Plan(WandaX)
        #End "Plan X"


        "Отсоси, старпер.":
                $ Girl.FaceChange("surprised")
                $ Girl.Statup("Lust", 90, 10)
                if RogueX.Loc == bg_current and RogueX.Caught < 3:
                        $ RogueX.Statup("Obed", 50, 20)
                        $ RogueX.Statup("Obed", 90, 40)
                if KittyX.Loc == bg_current and KittyX.Caught < 3:
                        $ KittyX.Statup("Obed", 50, 25)
                        $ KittyX.Statup("Obed", 90, 40)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:
                        $ EmmaX.Statup("Love", 90, 5)
                        $ EmmaX.Statup("Obed", 50, 20)
                        $ EmmaX.Statup("Obed", 90, 30)
                if LauraX.Loc == bg_current and LauraX.Caught < 3:
                        $ LauraX.Statup("Love", 90, 5)
                        $ LauraX.Statup("Obed", 50, 25)
                        $ LauraX.Statup("Obed", 90, 30)
                if JeanX.Loc == bg_current and JeanX.Caught < 3:
                        $ JeanX.Statup("Love", 50, 5)
                        $ JeanX.Statup("Love", 90, 10)
                        $ JeanX.Statup("Obed", 50, 25)
                        $ JeanX.Statup("Obed", 90, 30)
                if StormX.Loc == bg_current and StormX.Caught < 3:
                        $ StormX.Statup("Love", 90, -5)
                        $ StormX.Statup("Obed", 50, 20)
                        $ StormX.Statup("Obed", 90, 30)
                if JubesX.Loc == bg_current and JubesX.Caught < 3:
                        $ JubesX.Statup("Love", 80, 10)
                        $ JubesX.Statup("Obed", 50, 25)
                        $ JubesX.Statup("Obed", 90, 30)
                if GwenX.Loc == bg_current and GwenX.Caught < 3:
                        $ GwenX.Statup("Love", 80, 10)
                        $ GwenX.Statup("Obed", 50, 25)
                        $ GwenX.Statup("Obed", 90, 30)
                if BetsyX.Loc == bg_current and BetsyX.Caught < 3:
                        $ BetsyX.Statup("Love", 80, 5)
                        $ BetsyX.Statup("Obed", 50, 25)
                        $ BetsyX.Statup("Obed", 90, 35)
                if DoreenX.Loc == bg_current and DoreenX.Caught < 3:
                        $ DoreenX.Statup("Love", 50, -2)
                        $ DoreenX.Statup("Love", 70, -3)
                        $ DoreenX.Statup("Obed", 70, 2)
                        $ DoreenX.Statup("Inbt", 50, 5)
                if WandaX.Loc == bg_current and WandaX.Caught < 3:
                        $ WandaX.Statup("Love", 70, 2)
                        $ WandaX.Statup("Obed", 70, 3)
                        $ WandaX.Statup("Inbt", 50, 4)

                call XavierFace("angry")
                $ Count += 20
                ch_x "Если ты так к этому относишься, возможно, потребуются более жесткие меры."
                if PunishmentX:
                    ch_x "Я продлеваю твое наказание на [Count] дней!"
                else:
                    ch_x "Я уменьшаю твою ежедневную стипендию вдвое на [Count] дней!"

                if RogueX.Loc == bg_current and RogueX.Caught < 3:
                        if RogueX.Inbt > 500:
                            $ RogueX.Statup("Inbt", 90, 15)
                        $ RogueX.Statup("Inbt", 30, -20)
                        $ RogueX.Statup("Inbt", 50, -10)
                if KittyX.Loc == bg_current and KittyX.Caught < 3:
                        if KittyX.Inbt > 500:
                            $ KittyX.Statup("Inbt", 90, 15)
                        $ KittyX.Statup("Inbt", 30, -20)
                        $ KittyX.Statup("Inbt", 50, -10)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:
                        if EmmaX.Inbt > 500:
                            $ EmmaX.Statup("Inbt", 90, 15)
                        $ EmmaX.Statup("Inbt", 30, -20)
                        $ EmmaX.Statup("Inbt", 50, -10)
                if LauraX.Loc == bg_current and LauraX.Caught < 3:
                        if LauraX.Inbt > 500:
                            $ LauraX.Statup("Inbt", 90, 15)
                        $ LauraX.Statup("Inbt", 30, -15)
                        $ LauraX.Statup("Inbt", 50, -10)
                if JeanX.Loc == bg_current and JeanX.Caught < 3:
                        $ JeanX.Statup("Inbt", 90, 15)
                if StormX.Loc == bg_current and StormX.Caught < 3:
                        if StormX.Inbt > 500:
                            $ StormX.Statup("Inbt", 90, 5)
                        $ StormX.Statup("Inbt", 30, -10)
                        $ StormX.Statup("Inbt", 50, -5)
                if JubesX.Loc == bg_current and JubesX.Caught < 3:
                        if JubesX.Inbt > 500:
                            $ JubesX.Statup("Inbt", 90, 15)
                        $ JubesX.Statup("Inbt", 30, -15)
                        $ JubesX.Statup("Inbt", 50, -10)
                if GwenX.Loc == bg_current and GwenX.Caught < 3:
                        if GwenX.Inbt > 500:
                            $ GwenX.Statup("Inbt", 90, 15)
                        $ GwenX.Statup("Inbt", 30, -10)
                        $ GwenX.Statup("Inbt", 50, -5)
                if BetsyX.Loc == bg_current and BetsyX.Caught < 3:
                        if BetsyX.Inbt > 500:
                            $ BetsyX.Statup("Inbt", 90, 15)
                        $ BetsyX.Statup("Inbt", 30, -10)
                        $ BetsyX.Statup("Inbt", 50, -5)
                if DoreenX.Loc == bg_current and DoreenX.Caught < 3:
                        if DoreenX.Inbt > 500:
                            $ DoreenX.Statup("Inbt", 90, 5)
                        $ DoreenX.Statup("Inbt", 50, -5)
                if WandaX.Loc == bg_current and WandaX.Caught < 3:
                        if WandaX.Inbt > 500:
                            $ WandaX.Statup("Inbt", 90, 2)
                        $ WandaX.Statup("Inbt", 50, -2)

                ch_x "А теперь убирайтесь с глаз моих."
        #End "suck it"
    #End menu

    if Line:
            # if the plan falls through. . .
            call XavierFace("angry")
            $ Count += 10
            if not Player.Male:
                ch_x "Я понятия не имею, что это было, но, похоже, ты ничего так и не усвоила."
            else:
                ch_x "Я понятия не имею, что это было, но, похоже, ты ничего так и не усвоил."
            if PunishmentX:
                ch_x "Я продлеваю твое наказание на [Count] дней."
            else:
                ch_x "Я уменьшаю твою ежедневную стипендию вдвое на [Count] дней."

                if RogueX.Loc == bg_current and RogueX.Caught < 3:
                        $ RogueX.Statup("Obed", 50, 10)
                        $ RogueX.Statup("Obed", 90, 10)
                        $ RogueX.Statup("Inbt", 30, -10)
                        $ RogueX.Statup("Inbt", 50, -5)
                if KittyX.Loc == bg_current and KittyX.Caught < 3:
                        $ KittyX.Statup("Obed", 50, 10)
                        $ KittyX.Statup("Obed", 90, 10)
                        $ KittyX.Statup("Inbt", 30, -10)
                        $ KittyX.Statup("Inbt", 50, -5)
                if EmmaX.Loc == bg_current and EmmaX.Caught < 3:
                        $ EmmaX.Statup("Obed", 50, 10)
                        $ EmmaX.Statup("Inbt", 50, -5)
                if LauraX.Loc == bg_current and LauraX.Caught < 3:
                        $ LauraX.Statup("Obed", 50, 10)
                        $ LauraX.Statup("Obed", 90, 10)
                        $ LauraX.Statup("Inbt", 30, -10)
                        $ LauraX.Statup("Inbt", 50, -5)
                if JeanX.Loc == bg_current and JeanX.Caught < 3:
                        $ JeanX.Statup("Obed", 50, -10)
                if StormX.Loc == bg_current and StormX.Caught < 3:
                        $ StormX.Statup("Obed", 50, 10)
                        $ StormX.Statup("Inbt", 50, -5)
                if JubesX.Loc == bg_current and JubesX.Caught < 3:
                        $ JubesX.Statup("Obed", 50, 5)
                        $ JubesX.Statup("Obed", 90, 5)
                        $ JubesX.Statup("Inbt", 30, -8)
                        $ JubesX.Statup("Inbt", 50, -2)
                if GwenX.Loc == bg_current and GwenX.Caught < 3:
                        $ GwenX.Statup("Obed", 50, 5)
                        $ GwenX.Statup("Obed", 90, 5)
                        $ GwenX.Statup("Inbt", 30, -8)
                        $ GwenX.Statup("Inbt", 50, -2)
                if BetsyX.Loc == bg_current and BetsyX.Caught < 3:
                        $ BetsyX.Statup("Obed", 50, 5)
                        $ BetsyX.Statup("Obed", 90, 5)
                        $ BetsyX.Statup("Inbt", 30, -5)
                        $ BetsyX.Statup("Inbt", 50, -2)
                if DoreenX.Loc == bg_current and DoreenX.Caught < 3:
                        $ DoreenX.Statup("Obed", 60, 5)
                        $ DoreenX.Statup("Obed", 90, 5)
                        $ DoreenX.Statup("Inbt", 50, -2)
                if WandaX.Loc == bg_current and WandaX.Caught < 3:
                        $ WandaX.Statup("Obed", 60, 5)
                        $ WandaX.Statup("Obed", 90, 5)
                        $ WandaX.Statup("Inbt", 50, -2)
            ch_x "Я сыт вами по горло, убирайтесь."
            $ Line  = 0
    #End "evil plans"
    $ PunishmentX += Count

    $ Girl.Caught += 1
    if Partner in TotalGirls:
            $ Partner.Caught += 1
    $ Girl.AddWord(0,"caught","caught") #recent and daily

    if Girl is KittyX and KittyX not in Rules and "Xavier's photo" not in Player.Inventory:
            "Наверное, было бы неплохо найти способ заставить Ксавье оставить вас в покое."
            if KittyX.Caught > 1:
                "Может быть, вам стоит попробовать обыскать офис, когда его там нет."
            if KittyX.Caught > 2:
                "Вероятно, [KittyX.Name] сможет вам помочь."
            if KittyX.Caught > 3:
                "В левом ящике, похоже, есть что-то важное. . ."
    elif Girl is JeanX and "nowhammy" not in JeanX.Traits and JeanX.Caught > 1 and "whammy" not in JeanX.Traits:
            ch_x "О, и, Джин, дорогая, я хотел бы поговорить с тобой."
            $ Girl.FaceChange("bemused")
            ch_j "В чем дело?"
            ch_x "Я понимаю, что ты использовала свои способности, чтобы. . ."
            ch_x "прикрыть несколько своих. . . проступков."
            $ Girl.FaceChange("bemused",Eyes="up")
            ch_j "Ох, ты имеешь в виду, что я подтираю мозги слишком любопытным \"НИПам\"?"
            call XavierFace("angry")
            ch_x "Если под \"НИПами\" ты подразумевала своих однокурсников. . ."
            ch_x ". . . а под \"слишком любопытным,\" ты имела в виду, что они \"заметили, как ты занималась сексом в общественном месте\". . ."
            ch_x ". . . то да, это именно это я и имел в виду."
            $ Girl.FaceChange("bemused",Eyes="side")
            ch_j "Ага."
            ch_x "Я бы хотел, чтобы ты немедленно прекратила так делать!"
            ch_x "Это абсолютное злоупотребление твоими способностями и нарушение свободы студентов!"
            $ Girl.FaceChange("angry",1)
            ch_j "Да кого это вообще волнует."
            call XavierFace("shocked")
            ch_x "!!!"
            ch_x "Меня!"
            call XavierFace("angry")
            ch_x "Именно так, юная леди. До дальнейших распоряжений тебе запрещено. . . воздействовать на своих однокурсников!"
            $ Girl.FaceChange("angry",1,Mouth="surprised")
            ch_j "Бред!"
            $ Girl.FaceChange("angry",0,Eyes="psychic")
            ch_x "Кхм. . ."
            call XavierFace("psychic")
            ch_x "[Player.Name]. . . это может занять какое-то время. . ."
            if not Player.Male:
                ch_x "Ты свободна. . ."
            else:
                ch_x "Ты свободен. . ."
            $ JeanX.Traits.append("nowhammy")
            $ Girl.FaceChange("normal")

    if EmmaX.Loc == bg_current and EmmaX not in Rules:
            ch_x "Эмма, я бы хотел, чтобы ты задержалась, мы должны вкратце обсудить \"границы дозволенного\". . ."
            if EmmaX.Caught:
                    $ EmmaX.Statup("Love", 90, -5)
                    $ Girl.FaceChange("angry",Eyes="closed")
                    ch_e "Только не снова. . ."
    if StormX.Loc == bg_current and StormX not in Rules:
            if EmmaX.Loc == bg_current and EmmaX not in Rules:
                    ch_x "И Ороро, боюсь, нам также придется поговорить. . ."
            else:
                    ch_x "Ороро, я бы хотел, чтобы ты задержалась, мы должны вкратце обсудить \"границы дозволенного\". . ."
            if StormX.Caught:
                    $ StormX.Statup("Love", 90, -5)
                    $ Girl.FaceChange("angry",Eyes="closed")
                    ch_s "Снова? . ."
            if StormX not in Rules and "Xavier's files" not in Player.Inventory:
                    "Наверное, было бы неплохо найти способ заставить Ксавье оставить вас в покое."
                    if StormX.Caught > 1:
                        "Может быть, вам стоит попробовать обыскать офис, когда его там нет."
                    if StormX.Caught > 2:
                        "Вероятно, [StormX.Name] сможет вам помочь."
                    if StormX.Caught > 3:
                        "Наверняка в правом ящике есть что-то важное. . ."

    call Remove_Girl("All")
    "Вы возвращаетесь в свою комнату."
    hide Professor
    $ bg_current = "bg player"
    jump Misplaced
#End Caught / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Xavier_Plan(GirlX=0): #rkeljsvgbdw
    $ Line = "plan" #if not wiped, will cause a fail when it goes back to Xavier's office
    if GirlX is RogueX:
            if ApprovalCheck(RogueX, 1500, TabM=1, Loc="No"):
                    pass
            elif ApprovalCheck(RogueX, 1000, TabM=1, Loc="No"):
                    $ RogueX.FaceChange("perplexed",Brows = "sad")
                    ch_r "Мне не нравится что-то настолько экстремальное, [RogueX.Petname]. . ."
                    menu:
                        "Черт, [RogueX.Name]. . .":
                                $ RogueX.FaceChange("angry")
                                $ RogueX.Statup("Obed", 50, 5)
                                $ RogueX.Statup("Love", 90, -5)
                        "Ага, пожалуй, ты права. . .":
                                $ RogueX.FaceChange("bemused")
                    return
            else:
                    $ RogueX.FaceChange("confused")
                    ch_r "Что за чушь ты несешь?"
                    ch_p "План {i}Омега!{/i} . . ну же, вспоминай. . ."
                    ch_r "Звучит как полный бред."
                    ch_p "Ах да, наверное, мы еще его не обсуждали. . ."
                    $ RogueX.FaceChange("bemused")
                    return
            #End "Plan Omega"
    elif GirlX is KittyX:
            if "Xavier's photo" in Player.Inventory and ApprovalCheck(KittyX, 1500, TabM=1, Loc="No"):
                    pass
            elif ApprovalCheck(KittyX, 1000, TabM=1, Loc="No"):
                    $ KittyX.FaceChange("perplexed",Brows = "sad")
                    if "Xavier's photo" in Player.Inventory:
                            ch_k "Знаешь. . . если честно, я не думаю, что это хорошая идея. . ."
                    elif "kappa" in Player.History:
                            ch_k "Может, если мы вернемся сюда позже, мы сможем что-нибудь найти. . ."
                    else:
                            ch_k "Сейчас у нас нет возможности осуществить это. . ."
                            $ Player.History.append("kappa")
                    menu:
                        "Черт, [KittyX.Name]. . .":
                                $ KittyX.FaceChange("angry")
                                $ KittyX.Statup("Obed", 50, 5)
                                $ KittyX.Statup("Love", 90, -5)
                        "Ага, пожалуй, ты права. . .":
                                $ KittyX.FaceChange("bemused")
                                $ KittyX.Statup("Love", 90, 5)
                    return
            else:
                    $ KittyX.FaceChange("confused")
                    ch_k "Подожди, что за план?"
                    ch_p "План {i}Каппа!{/i} . . ну же, вспоминай. . ."
                    ch_k "Я вообще {i}не понимаю{/i} о чем ты говоришь."
                    ch_p "Ах да, наверное, мы еще его не обсуждали. . ."
                    $ KittyX.FaceChange("bemused")
                    return
            #End "Plan Kappa"
    elif GirlX is EmmaX:
            if ApprovalCheck(EmmaX, 1500, TabM=1, Loc="No"):
                    pass
            elif ApprovalCheck(EmmaX, 1000, TabM=1, Loc="No"):
                    $ EmmaX.FaceChange("perplexed",Brows = "sad")
                    ch_e "Эм, я не думаю, что мы уже готовы, [EmmaX.Petname]. . ."
                    menu:
                        "Черт, [EmmaX.Name]. . .":
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Obed", 50, 5)
                                $ EmmaX.Statup("Love", 90, -5)
                        "Ага, пожалуй, ты права. . .":
                                $ EmmaX.FaceChange("bemused")
                    return
            else:
                    $ EmmaX.FaceChange("confused")
                    ch_e "Господи, какой же ты ребенок, о чем ты вообще сейчас говоришь?"
                    ch_p "План {i}Пси!{/i} . . ну же, вспоминай. . ."
                    ch_e "Увы, ничего такого не припоминаю."
                    ch_p "Ах да, наверное, мы еще его не обсуждали. . ."
                    $ EmmaX.FaceChange("bemused")
                    return
            #End "Plan Psi"
    elif GirlX is LauraX:
            if LauraX.Lvl >= 2 and ApprovalCheck(LauraX, 1500, TabM=1, Loc="No") and ApprovalCheck(LauraX, 750, "I"):
                    pass
            elif ApprovalCheck(LauraX, 1000, TabM=1, Loc="No"):
                    $ LauraX.FaceChange("angry",Eyes="side",Brows = "angry")
                    ch_l "Говорю тебе, это глупая идея. . ."
                    menu:
                        "Черт, [LauraX.Name]. . .":
                                $ LauraX.FaceChange("angry")
                                $ LauraX.Statup("Obed", 50, 5)
                                $ LauraX.Statup("Love", 90, -5)
                        "Ага, пожалуй, ты права. . .":
                                $ LauraX.FaceChange("bemused")
                                $ LauraX.Statup("Love", 90, 5)
                    return
            else:
                    $ LauraX.FaceChange("confused")
                    ch_l "Да!"
                    ch_l ". . ."
                    ch_l "Подожди, что за план \"хи\"?"
                    ch_p "План {i}Ки!{/i} . . ну же, вспоминай. . ."
                    ch_l "Эммм. Не могу?"
                    ch_p "Ах да, наверное, мы еще его не обсуждали. . ."
                    $ LauraX.FaceChange("bemused")
                    return
            #End "Plan Chi"
    elif GirlX is JeanX:
            if ApprovalCheck(JeanX, 1500, TabM=1, Loc="No"):
                    pass
            elif ApprovalCheck(JeanX, 1000, TabM=1, Loc="No"):
                    $ JeanX.FaceChange("perplexed",Brows = "sad")
                    ch_j "Слушай, я не собираюсь все делать за тебя, идея твоя, ты и разбирайся, [JeanX.Petname]. . ."
                    menu:
                        "Черт, [JeanX.Name]. . .":
                                $ JeanX.FaceChange("angry")
                                $ JeanX.Statup("Obed", 50, 5)
                                $ JeanX.Statup("Love", 90, -5)
                        "Ага, пожалуй, ты права. . .":
                                $ JeanX.FaceChange("bemused")
                    return
            else:
                    $ JeanX.FaceChange("confused")
                    ch_j "А? Ты вообще о чем?"
                    ch_p "План {i}Альфа!{/i} . . ну же, вспоминай. . ."
                    ch_j "Ничего такого не припомню. . ."
                    ch_p "Ах да, наверное, мы еще его не обсуждали. . ."
                    $ JeanX.FaceChange("bemused")
                    return
            #End "Plan Alpha"
    elif GirlX is StormX:
            if "Xavier's files" in Player.Inventory and ApprovalCheck(StormX, 1500, TabM=1, Loc="No"):
                    pass
            elif ApprovalCheck(StormX, 1000, TabM=1, Loc="No"):
                    $ StormX.FaceChange("perplexed",Brows = "sad")
                    if "Xavier's files" in Player.Inventory:
                            ch_s "Я очень сомневаюсь, что нам следует пытаться это сделать. . ."
                    elif "rho" in Player.History:
                            ch_s "Возможно, если бы у нас были какие-то рычаги воздействия. . ."
                    else:
                            ch_s "Я не уверена, что мы можем это провернуть. . ."
                            $ Player.History.append("rho")
                    menu:
                        "Черт, [StormX.Name]. . .":
                                $ StormX.FaceChange("angry")
                                $ StormX.Statup("Obed", 50, 5)
                                $ StormX.Statup("Love", 90, -5)
                        "Ага, пожалуй, ты права. . .":
                                $ StormX.FaceChange("bemused")
                    return
            else:
                    $ StormX.FaceChange("confused")
                    ch_s "'Ро? Ты это мне?"
                    ch_p "Да! План {i}Ро!{/i} . . ну же, вспоминай. . ."
                    ch_s "Да, я 'Ро. А что за план?"
                    ch_p "Я не знаю!"
                    $ StormX.FaceChange("smile")
                    ch_s "Ах!"
                    $ StormX.FaceChange("bemused")
                    return
            #End "Plan Rho"
    elif GirlX is JubesX:
            if ApprovalCheck(JubesX, 1500, TabM=1, Loc="No"):
                    pass
            elif ApprovalCheck(JubesX, 1000, TabM=1, Loc="No"):
                    $ JubesX.FaceChange("perplexed",Brows = "sad")
                    ch_v "Что?! Эм, нет. . . давай не будем."
                    menu:
                        "Черт, [JubesX.Name]. . .":
                                $ JubesX.FaceChange("angry")
                                $ JubesX.Statup("Obed", 50, 5)
                                $ JubesX.Statup("Love", 90, -5)
                        "Ага, пожалуй, ты права. . .":
                                $ JubesX.FaceChange("bemused")
                    return
            else:
                    $ JubesX.FaceChange("confused")
                    ch_v "А?"
                    ch_p "План {i}Зета{/i} . . ну же, вспоминай. . ."
                    ch_v "Это что-то из \"Гандама\", да?[[ПП. Анимеха такая]"
                    ch_p "Ах да, наверное, мы еще его не обсуждали. . ."
                    $ JubesX.FaceChange("bemused")
                    return
            #End "Plan Zeta"
    elif GirlX is GwenX:
            if ApprovalCheck(GwenX, 1500, TabM=1, Loc="No") and GwenX.Lvl >= 2:
                    pass
            elif ApprovalCheck(GwenX, 1500, TabM=1, Loc="No"):
                    $ GwenX.FaceChange("perplexed",Brows = "sad")
                    ch_g "Я не знаю, чего ты от меня хочешь."
                    ch_g "Может, если бы у меня было больше боевого опыта. . ."
                    menu:
                        "Черт, [GwenX.Name]. . .":
                                $ GwenX.FaceChange("angry")
                                $ GwenX.Statup("Obed", 50, 5)
                                $ GwenX.Statup("Love", 90, -5)
                        "Ага, пожалуй, ты права. . .":
                                $ GwenX.FaceChange("bemused")
                    return
            elif GwenX.Lvl >= 2:
                    $ GwenX.FaceChange("perplexed",Brows = "sad")
                    ch_g "Я не уверена, это похоже на читерство. . ."
                    return
            else:
                    $ GwenX.FaceChange("confused")
                    ch_g "А?"
                    ch_p "План{i}Гамма!{/i} . . ну же, вспоминай. . ."
                    ch_g "А, точно!"
                    ch_g ". . ."
                    $ GwenX.FaceChange("angry")
                    ch_g "-Грррррррррррр!-" with vpunch
                    ch_g "-Раааар! Гвен крушить!!!-" with vpunch
                    ch_g ". . ."
                    ch_p ". . ."
                    ch_x ". . ."
                    $ GwenX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_g "Ты это имела в виду под планом \"Гамма?\""
                    else:
                        ch_g "Ты это имел в виду под планом \"Гамма?\""
                    menu:
                        "Черт, [GwenX.Name]. . .":
                                $ GwenX.FaceChange("angry")
                                $ GwenX.Statup("Obed", 50, 5)
                                $ GwenX.Statup("Love", 90, -2)
                        ". . .":
                                pass
                    $ GwenX.FaceChange("bemused")
                    return
        #End "Plan Gamma"
    elif GirlX is BetsyX:
            if "beta" not in BetsyX.History:
                    $ BetsyX.AddWord(1,0,0,0,"beta")
                    $ BetsyX.FaceChange("angry",Eyes="surprised")
                    ch_b "Подожди, \"Бета?\" Почему именно \"Бета?\""
                    $ BetsyX.FaceChange("angry")
                    ch_b "Думаю, кодовое слово \"Пси\" больше подошло бы мне!"
                    if EmmaX in Rules:
                            menu:
                                extend ""
                                "Ну, \"Пси\" мы уже используем с Эммой.":
                                        $ BetsyX.Statup("Obed", 50, 5)
                                ". . .":
                                        ch_b "Эх, Эмма опередила меня. . ."
                    else:
                            menu:
                                extend ""
                                "Ну, \"Пси\" я уже запланировала под Эмму." if not Player.Male:
                                        $ BetsyX.Statup("Obed", 50, 5)
                                "Ну, \"Пси\" я уже запланировал под Эмму." if Player.Male:
                                        $ BetsyX.Statup("Obed", 50, 5)
                                ". . .":
                                        ch_b "Эх, Эмма опередила меня. . ."

                    $ BetsyX.FaceChange("sad")
                    $ BetsyX.Statup("Love", 70, -5)
                    menu:
                        extend ""
                        "\"Бета\" почти \"Бетси.\"":
                                $ BetsyX.Statup("Love", 70, 2)
                                $ BetsyX.Statup("Love", 80, 1)
                                ch_b "Да, похоже, я понимаю ход твоих мыслей. . ."
                        ". . .":
                                $ BetsyX.Statup("Obed", 50, 1)
                                ch_b "Пожалуй, я поняла, откуда взялось это кодовое слово. . ."
                    $ BetsyX.FaceChange("normal")
            if ApprovalCheck(BetsyX, 1500, TabM=1, Loc="No") and BetsyX.Lvl >= 2:
                    pass
            elif ApprovalCheck(BetsyX, 1500, TabM=1, Loc="No"):
                    $ BetsyX.FaceChange("perplexed",Brows = "sad")
                    ch_b "Мне не очень нравится этот твой план. . ."
                    menu:
                        "Черт, [BetsyX.Name]. . .":
                                $ BetsyX.FaceChange("angry")
                                $ BetsyX.Statup("Obed", 50, 5)
                                $ BetsyX.Statup("Love", 90, -5)
                        "Ага, пожалуй, ты права. . .":
                                $ BetsyX.FaceChange("bemused")
                                $ BetsyX.Statup("Love", 90, 2)
                    return
            elif BetsyX.Lvl >= 2:
                    $ BetsyX.FaceChange("perplexed",Brows = "sad")
                    ch_b "Я совсем не хочу в этом участвовать. . ."
                    return
            else:
                    $ BetsyX.FaceChange("confused")

                    menu:
                        "Черт, [BetsyX.Name]. . .":
                                $ BetsyX.FaceChange("angry")
                                $ BetsyX.Statup("Obed", 50, 5)
                                $ BetsyX.Statup("Love", 90, -2)
                        ". . .":
                                pass
                    $ BetsyX.FaceChange("bemused")
                    return
        #End "Plan Beta"
    elif GirlX is DoreenX:
            if DoreenX.Lvl >= 2 and ApprovalCheck(DoreenX, 1500, TabM=1, Loc="No") and ApprovalCheck(DoreenX, 900, "OI"):
                    pass
            elif ApprovalCheck(DoreenX, 1000, TabM=1, Loc="No"):
                    $ DoreenX.FaceChange("angry",Eyes="side",Brows = "angry")
                    ch_d "Я не собираюсь в этом участвовать. . ."
                    menu:
                        "Чертова Белка. . .":
                                $ DoreenX.FaceChange("angry")
                                $ DoreenX.Statup("Obed", 50, 5)
                                $ DoreenX.Statup("Love", 90, -5)
                        "Эх, ладно. . .":
                                $ DoreenX.FaceChange("bemused")
                                $ DoreenX.Statup("Love", 90, 5)
                    return
            else:
                    $ DoreenX.FaceChange("confused")
                    ch_d "А?"
                    ch_p "План -Дельта!- . . ну же, вспоминай. . ."
                    ch_d "Эм. Не могу?"
                    ch_p "Ах да, наверное, мы еще его не обсуждали. . ."
                    $ DoreenX.FaceChange("bemused")
                    return
            #End "Plan Delta"
    elif GirlX is WandaX:
            if WandaX.Lvl >= 2 and ApprovalCheck(WandaX, 1500, TabM=1, Loc="No") and ApprovalCheck(WandaX, 900, "OI"):
                    pass
            elif ApprovalCheck(WandaX, 1000, TabM=1, Loc="No"):
                    $ WandaX.FaceChange("sad",Eyes="side",Brows = "angry")
                    ch_w "Я. . . не могу себя нормально контролировать. . ."
                    menu:
                        "Ну и какая из тебя тогда \"Алая Ведьма\". . .":
                                $ WandaX.FaceChange("angry")
                                $ WandaX.Statup("Obed", 50, 5)
                                $ WandaX.Statup("Love", 90, -5)
                        "Поняла, извини. . ." if not Player.Male:
                                $ WandaX.FaceChange("bemused")
                                $ WandaX.Statup("Love", 90, 5)
                        "Понял, извини. . ." if Player.Male:
                                $ WandaX.FaceChange("bemused")
                                $ WandaX.Statup("Love", 90, 5)
                    return
            else:
                    $ WandaX.FaceChange("confused")
                    ch_w "Что?"
                    ch_p "План -Эпсилон!- . . ну же, вспоминай. . ."
                    ch_w "Эм, не могу?"
                    ch_p "Ах да, наверное, мы еще его не обсуждали. . ."
                    $ WandaX.FaceChange("bemused")
                    return
            #End "Plan Upsilon"
    else:
        "Error:Please tell Oni you got to a Xavier plan in a broken way, and what led to that."
        return


    if "Xavier" in Player.DailyActions:
            "Профессор, похоже, не в себе."
            "Вы не думаете, что сегодня сможешь вытянуть из него что-нибудь еще."
            "Вы оставляете его в покое."
            $ bg_current = "bg player"
            jump Misplaced

    #$ GirlX = GirlCheck(GirlX)
    call Shift_Focus(GirlX)
    $ GirlX.FaceChange("sly")
    "Когда вы это говорите, на лице [GirlX.Name_rod] появляется хитрая ухмылка."
    "Вы быстро подходите к Ксавье и кладете ему руки на голову."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Ксавье в шоке понимает, что с вашими способностями его телепатия бесполезна."

    if Partner:
            if Partner is RogueX and "Omega" not in Player.Traits:
                    $ Line = "first"
            elif Partner is KittyX and "Kappa" not in Player.Traits:
                    $ Line = "first"
            elif Partner is EmmaX and "Psi" not in Player.Traits:
                    $ Line = "first"
            elif Partner is LauraX and "Chi" not in Player.Traits:
                    $ Line = "first"
            elif Partner is JeanX and "Alpha" not in Player.Traits:
                    $ Line = "first"
            elif Partner is StormX and "Rho" not in Player.Traits:
                    $ Line = "first"
            elif Partner is JubesX and "Zeta" not in Player.Traits:
                    $ Line = "first"
            elif Partner is GwenX and "Gamma" not in Player.Traits:
                    $ Line = "first"
            elif Partner is BetsyX and "Beta" not in Player.Traits:
                    $ Line = "first"
            elif Partner is DoreenX and "Delta" not in Player.Traits:
                    $ Line = "first"
            elif Partner is WandaX and "Upsilon" not in Player.Traits:
                    $ Line = "first"

            if Line == "first":
                #if the Partner has never done this. . .
                if ApprovalCheck(Partner, 1000) or Partner is JeanX:
                        #if she's cool with it.
                        $ Partner.FaceChange("surprised")
                        "Похоже, [Partner.Name] была не готова, но все-таки она соглашается на вашу авантюру."
                        $ Partner.FaceChange("sly")
                else:
                        $ Partner.FaceChange("surprised")
                        "[Partner.Name], кажется, не в своей тарелке от вашей идеи, она убегает."
                        call Remove_Girl(Partner)
            else:
                        $ Partner.FaceChange("sly")
                        "[Partner.Name] понимает к чему вы ведете."
    #end partner response

    call XavierFace("angry")
    if GirlX is RogueX:
            $ RogueX.Arms = 0
            $ RogueX.ArmPose = 2
            show Rogue_Sprite at SpriteLoc(StageLeft+100,85) zorder 24 with ease
            "[RogueX.Name] подходит и тоже хватает его за голову, копируя его способности, пока он беспомощно наблюдает."
            "Теперь, когда она владеет его полными способностями, в то время как он сам их лишен, он абсолютно беззащитен."
            call XavierFace("hypno")
            if "Omega" in Player.Traits:
                    ch_x "Ох, только не снова."
                    ch_x "Чего вы хотите на этот раз?"
                    $ RogueX.Statup("Obed", 80, 3)
                    $ RogueX.Statup("Inbt", 70, 1)
            else:
                    $ RogueX.Statup("Obed", 50, 40)
                    $ RogueX.Statup("Inbt", 70, 20)
            ch_r "Ну, [RogueX.Petname], как ты хочешь воспользоваться этой возможностью?"
            ch_r "Думаю, у нас будет только три попытки. . ."
    elif GirlX is KittyX:
            $ KittyX.ArmPose = 2
            show Kitty_Sprite at SpriteLoc(StageLeft+100,150) with ease
            $ KittyX.SpriteLoc = StageCenter
            "[KittyX.Name] подходит, садится к нему на колени и кладет руки на спинку кресла."
            if "Kappa" in Player.Traits:
                    ch_x "Ох, только не снова."
                    ch_x "Чего вы хотите на этот раз?"
                    $ KittyX.Statup("Obed", 80, 3)
                    $ KittyX.Statup("Inbt", 70, 1)
            else:
                    ch_x "Что все это значит? Отпустите меня!"
                    "Вы достаете фотографию, которую нашли ранее в его кабинете."
                    $ KittyX.Statup("Obed", 50, 40)
                    $ KittyX.Statup("Inbt", 70, 30)
                    ch_p "У меня здесь довольно. . . компрометирующая фотография вас с Мистик."
                    if not Player.Male:
                        ch_p "Я подумала, может быть, вы могли бы быть менее строгими к нам."
                    else:
                        ch_p "Я подумал, может быть, вы могли бы быть менее строгими к нам."
                    ch_x "А если я откажусь?"
                    ch_p "[KittyX.Name] сделает так, что на каждом компьютере института будет всплывать эта фотография, каждый день."
                    ch_p "И только у меня будет пароль."
                    ch_x "Ну хорошо. . . я закрою глаза на ваше наказание."
                    ch_p "Ох, думаю, теперь мы будем заниматься более развратными вещами. . ."
                    $ KittyX.Statup("Obed", 200, 30)
                    $ KittyX.Statup("Inbt", 200, 10)
            ch_k "Ну, [KittyX.Petname], что мы должны потребовать?"
    elif GirlX is EmmaX or GirlX is JeanX:
            if GirlX is EmmaX:
                    show Emma_Sprite at SpriteLoc(StageLeft+100,85) zorder 24 with ease
            elif GirlX is JeanX:
                    show Jean_Sprite at SpriteLoc(StageLeft+100,85) zorder 24 with ease
            "[GirlX.Name] подходит к Ксавье сзади и активирует собственную телепатию."
            call XavierFace("angry")
            if (GirlX is EmmaX and "Psi" in Player.Traits) or (GirlX is JeanX and "Alpha" in Player.Traits):
                    ch_x "Ох, только не снова."
                    $ GirlX.Statup("Obed", 80, 3)
                    $ GirlX.Statup("Inbt", 80, 1)
            else:
                    $ GirlX.Statup("Obed", 50, 40)
                    $ GirlX.Statup("Inbt", 70, 30)
                    $ GirlX.Statup("Obed", 200, 30)
                    $ GirlX.Statup("Inbt", 200, 10)
            call AnyLine(GirlX,"Ну, "+GirlX.Petname+", что мы должны потребовать?")
    elif GirlX is LauraX:
            $ LauraX.ArmPose = 2
            if "Chi" in Player.Traits:
                    ch_x "Ох, только не снова."
                    $ LauraX.Claws = 1
                    ch_x "Чего вы хотите на этот раз?"
                    $ LauraX.Statup("Obed", 80, 3)
                    $ LauraX.Statup("Inbt", 80, 1)
            else:
                    ch_x "Что все это значит? Отпустите меня!"
                    ch_p "[LauraX.Name] и я поговорили, и похоже, что никому из нас не нравится, что вы нам мешаете."
                    ch_x "А если я продолжу?"
                    ch_p "Моя маленькая [LauraX.Pet] обладает особым набором навыков, вы и сами это знаете. . ."
                    $ GirlX.NameCheck() #checks reaction to petname
                    $ LauraX.Claws = 1
                    $ GirlX.FaceChange("sly")
                    ch_p "Она может причинить вам много неприятностей, если вы и дальше будут вызывать ее сюда. . ."
                    "[LauraX.Name] проводит когтями по подлокотнику профессорского кресла, оставляя тонкие линии на металле."
                    ch_x "Ну хорошо. . . я закрою глаза на ваше наказание."
                    ch_p "Ох, думаю, теперь мы будем заниматься более развратными вещами. . ."
                    $ LauraX.Statup("Obed", 50, 40)
                    $ LauraX.Statup("Inbt", 80, 30)
                    $ LauraX.Statup("Obed", 200, 30)
                    $ LauraX.Statup("Inbt", 200, 10)
            ch_l "Ну, [LauraX.Petname], что мы должны потребовать?"
    elif GirlX is StormX:
            $ StormX.ArmPose = 1
            show Storm_Sprite at SpriteLoc(StageLeft+100,150) with ease
            $ StormX.SpriteLoc = StageCenter
            "[StormX.Name] подходит, садится к нему на колени и кладет руки на спинку стула."
            if "Rho" in Player.Traits:
                    ch_x "Ох, только не снова."
                    ch_x "Чего вы хотите на этот раз?"
                    $ StormX.Statup("Obed", 80, 3)
                    $ StormX.Statup("Inbt", 70, 1)
            else:
                    ch_x "Что все это значит? Отпустите меня!"
                    "Вы достаете файлы, которые нашли ранее в его кабинете."
                    $ StormX.Statup("Obed", 50, 40)
                    $ StormX.Statup("Inbt", 70, 30)
                    ch_p "У меня тут есть несколько довольно. . . сомнительных \"медицинских\" файлов"
                    ch_p "Я подумал, может быть, вы могли бы быть менее строгими к нам."
                    ch_x "А если я откажусь?"
                    ch_p "Мы позаботимся о том, чтобы все девушки из этих файлах обо всем узнали."
                    ch_x "Ну хорошо. . . я закрою глаза на ваше наказание."
                    ch_p "Ох, думаю, теперь мы будем заниматься более развратными вещами. . ."
                    $ StormX.Statup("Obed", 200, 30)
                    $ StormX.Statup("Inbt", 200, 10)
            ch_s "Что ж, [StormX.Petname], что мы должны потребовать?"
    elif GirlX is JubesX:
            $ JubesX.ArmPose = 2
            show Jubes_Sprite at SpriteLoc(StageLeft+100,150) with ease
            $ JubesX.SpriteLoc = StageCenter
            "[JubesX.Name] подходит и садится к нему на колени, прижимая его руки к креслу."
            "Она поворачивается, чтобы посмотреть на него."
            if "Zeta" in Player.Traits:
                    ch_x "Ох, только не снова."
                    ch_x "Чего вы хотите на этот раз?"
                    $ JubesX.Statup("Obed", 80, 3)
                    $ JubesX.Statup("Inbt", 70, 1)
            else:
                    ch_x "Что все это значит? Отпустите меня!"
                    $ JubesX.Statup("Inbt", 70, 30)
                    ch_v "Посмотри мне в глаза. . ."
                    $ JubesX.Statup("Obed", 50, 40)
                    $ JubesX.Statup("Inbt", 200, 10)
                    ch_v "видишь в них искры? . . ."
                    $ JubesX.Statup("Obed", 200, 30)
                    "Она медленно вводит его в транс, используя комбинацию своих вампирских способностей и фейерверков. . ."
            ch_v "Ну, [JubesX.Petname], что мы должны потребовать?"
    elif GirlX is GwenX:
            $ GwenX.ArmPose = 1
            show Gwen_Sprite at SpriteLoc(StageLeft+100,150) with ease
            $ GwenX.SpriteLoc = StageCenter
            "[GwenX.Name] подходит и садится к нему на колени, прижимая его руки к креслу."
            "Она поворачивается, чтобы посмотреть на него."
            if "Gamma" in Player.Traits:
                    ch_x "Ох, только не снова."
                    ch_x "Чего вы хотите на этот раз?"
                    $ GwenX.Statup("Obed", 80, 3)
                    $ GwenX.Statup("Inbt", 70, 1)
            else:
                    ch_x "Что все это значит? Отпустите меня!"
                    $ GwenX.Statup("Inbt", 70, 30)
                    call Gwen_Code #does "code" animation
                    "[GwenX.Name] тянется куда-то вверх, хватает что-то невидимое и тянет это вниз."
                    ch_g "Хорошо!"
                    $ GwenX.Statup("Obed", 50, 40)
                    $ GwenX.Statup("Inbt", 200, 10)
                    ch_g "Консоль открыта!"
                    $ GwenX.Statup("Obed", 200, 30)
                    ch_g "Просто скажи, что ты хочешь и это будет исполненно."
            ch_g "Чего ты хочешь?"
    elif GirlX is BetsyX:
            $ BetsyX.ArmPose = 2
            if "Chi" in Player.Traits:
                    ch_x "Ох, только не снова."
                    $ BetsyX.Knife = 1
                    ch_x "Чего вы хотите на этот раз?"
                    $ BetsyX.Statup("Obed", 80, 3)
                    $ BetsyX.Statup("Inbt", 80, 1)
            else:
                    ch_x "Что все это значит? Отпустите меня!"
                    $ BetsyX.Knife = 1
                    $ GirlX.FaceChange("sly")
                    "[BetsyX.Name] заходит за спину Ксавье и активирует свой псионический нож."
                    "Она погружает его ему в голову."
                    $ BetsyX.Statup("Obed", 50, 40)
                    $ BetsyX.Statup("Inbt", 80, 30)
                    $ BetsyX.Statup("Obed", 200, 30)
                    $ BetsyX.Statup("Inbt", 200, 10)
            ch_b "Что ж, [BetsyX.Petname], что нам следует попросить?"
    elif GirlX is DoreenX:
            $ DoreenX.ArmPose = 2
            if "Delta" in Player.Traits:
                    ch_x "Ох, пожалуйста, только не снова."
                    ch_x "Чего вы хотите на этот раз?"
                    $ DoreenX.Statup("Obed", 80, 3)
                    $ DoreenX.Statup("Inbt", 80, 1)
            else:
                    ch_x "Что все это значит? Отпустите меня!"
                    ch_p "[DoreenX.Name] и я поговорили, и похоже, что никому из нас не нравится, что вы нам мешаете."
                    ch_x "А если я продолжу?"
                    ch_p "Моя маленькая [DoreenX.Pet] обладает особым набором навыков, вы и сами это знаете. . ."
                    $ GirlX.NameCheck() #checks reaction to petname
                    "В комнате гаснет свет, и глаза Дорин загораются красным."
                    "Через мгновение вы будто видите уже две пары глаз, затем шесть, двенадцать, сотню."
                    $ GirlX.FaceChange("sly")
                    ch_p "Подумайте хорошенько."
                    ch_p "Вы не в силах ее остановить."
                    ch_p "Она может доставить вам много неприятностей, если вы и дальше будете вызывать ее сюда. . ."
                    "Глаза начинают метаться по комнате. . ."
                    ch_x "Ну хорошо. . . я закрою глаза на ваше наказание."
                    ch_p "Ох, думаю, теперь мы будем заниматься более развратными вещами. . ."
                    $ DoreenX.Statup("Obed", 50, 40)
                    $ DoreenX.Statup("Inbt", 80, 30)
                    $ DoreenX.Statup("Obed", 200, 30)
                    $ DoreenX.Statup("Inbt", 200, 10)
            ch_d "Ну, [DoreenX.Petname], что нам следует попросить?"
    elif GirlX is WandaX:
            $ WandaX.ArmPose = 2
            if "Upsilon" in Player.Traits:
                    ch_x "Ох, пожалуйста, только не снова."
                    ch_x "Чего вы хотите на этот раз?"
                    $ WandaX.Statup("Obed", 80, 3)
                    $ WandaX.Statup("Inbt", 80, 1)
            else:
                    ch_x "Что все это значит? Отпустите меня!"
                    ch_p "Мы с [WandaX.Name_tvo] поговорили, и похоже, что никому из нас не нравится, что вы нам мешаете."
                    ch_x "А если я продолжу?"
                    ch_p "Тогда, думаю, [WandaX.Pet] может устроить для вас настоящий ад. . ."
                    $ GirlX.NameCheck() #checks reaction to petname
                    "[WandaX.Name] приближается — тонкая струя энергии вырывается из ее пальцев и пронзает его сознание."
                    $ GirlX.FaceChange("sly")
                    "Ксавьер корчится, словно в кошмаре, бессвязно бормоча что-то себе под нос."
                    "По вашемй команде [WandaX.Name] рассеивает поток энергии. После чего Ксавье, кажется, приходит в себя."
                    ch_p "Это лишь затравка."
                    ch_x "Ну хорошо. . . я закрою глаза на ваше наказание."
                    ch_p "Ох, думаю, теперь мы будем заниматься более развратными вещами. . ."
                    $ WandaX.Statup("Obed", 50, 40)
                    $ WandaX.Statup("Inbt", 80, 30)
                    $ WandaX.Statup("Obed", 200, 30)
                    $ WandaX.Statup("Inbt", 200, 10)
            ch_w "Ну, [WandaX.Petname], что мы должны попросить?"

    $ Count = 3
    $ PunishmentX = 0
    while Count > 0:
        $ Count -= 1
        menu:
            ch_x "Чего ты хочешь?"
            "Не беспокойте нас больше, когда мы развлекаемся." if GirlX not in Rules:
                    ch_x "Ну, хорошо. . . Я могу предложить немного. . . свободы. . ."
                    $ Rules.append(GirlX)
            "You know, it's kinda fun dodging you, catch us if you can." if GirlX in Rules:
                    ch_x "If you. . . want me to, I suppose. . ."
                    $ Rules.remove(GirlX)

            "Знаете, [JeanX.Name] хочет снова \"воздействовать\" на людей." if JeanX in TotalGirls and "nowhammy" in JeanX.Traits and "met" in JeanX.History:
                    ch_x "Я сниму с нее запрет на использование сил. . ."
                    $ JeanX.Traits.remove("nowhammy")
                    $ JeanX.Traits.append("whammy")
                    if JeanX.Loc == bg_current:
                            $ JeanX.Statup("Obed", 50, 5)
                            $ JeanX.Statup("Love", 50, 5)
                            $ JeanX.Statup("Love", 70, 5)
                            $ JeanX.Statup("Love", 90, 5)
                            $ GirlX.FaceChange("sly",1)
                            ch_j "Отлично. . ."
            "Знаете, мне понравилось, когда вы не позволяли [JeanX.Name_dat] \"воздействовать\" на людей" if JeanX in TotalGirls and "whammy" in JeanX.Traits and "met" in JeanX.History:
                    ch_x "Я могу запретить ей стирать память. . ."
                    $ JeanX.Traits.append("nowhammy")
                    $ JeanX.Traits.remove("whammy")
                    if JeanX.Loc == bg_current:
                            $ JeanX.Statup("Obed", 50, 5)
                            $ JeanX.Statup("Obed", 80, 5)
                            $ JeanX.Statup("Love", 70, -5)
                            $ JeanX.Statup("Love", 90, -5)
                            $ GirlX.FaceChange("angry",1,Mouth="surprised")
                            ch_j "Эй!"
                            $ GirlX.FaceChange("angry",1)

            "Повысьте мне стипендию." if Player.Income < 40:
                    if GirlX is RogueX and "Omega" not in Player.Traits:
                            ch_x "Ну, хорошо. . . я могу ее поднять, но только ненамного. . ."
                            $ Player.Income += 2
                    elif GirlX is KittyX and "Kappa" not in Player.Traits:
                            ch_x "Ну, хорошо. . . я могу ее поднять, но только ненамного. . ."
                            $ Player.Income += 2
                    elif GirlX is EmmaX and "Psi" not in Player.Traits:
                            ch_x "Ну, хорошо. . . я могу ее поднять, но только ненамного. . ."
                            $ Player.Income += 2
                    elif GirlX is LauraX and "Chi" not in Player.Traits:
                            ch_x "Ну, хорошо. . . я могу ее поднять, но только ненамного. . ."
                            $ Player.Income += 2
                    elif GirlX is JeanX and "Alpha" not in Player.Traits:
                            ch_x "Ну, хорошо. . . я могу ее поднять, но только ненамного. . ."
                            $ Player.Income += 2
                    elif GirlX is StormX and "Rho" not in Player.Traits:
                            ch_x "Ну, хорошо. . . я могу ее поднять, но только ненамного. . ."
                            $ Player.Income += 2
                    elif GirlX is JubesX and "Zeta" not in Player.Traits:
                            ch_x "Ну, хорошо. . . я могу ее поднять, но только ненамного. . ."
                            $ Player.Income += 2
                    elif GirlX is GwenX and "Gamma" not in Player.Traits:
                            ch_x "Ну, хорошо. . . я могу ее поднять, но только ненамного. . ."
                            $ Player.Income += 2
                    elif GirlX is BetsyX and "Beta" not in Player.Traits:
                            ch_x "Ну, хорошо. . . я могу ее поднять, но только ненамного. . ."
                            $ Player.Income += 2
                    elif GirlX is DoreenX and "Delta" not in Player.Traits:
                            ch_x "Ну, хорошо. . . я могу ее поднять, но только ненамного. . ."
                            $ Player.Income += 2
                    elif GirlX is WandaX and "Upsilon" not in Player.Traits:
                            ch_x "Ну, хорошо. . . я могу ее поднять, но только ненамного. . ."
                            $ Player.Income += 2
                    else:
                            ch_x "Боюсь, я не смогу поднять ее еще больше. . ."
                            $ Count += 1
            "Повысьте мне стипендию. [[Использовано] (locked)" if Player.Income >= 40:
                    pass

            "Есть одна девушка, которая беспокоит меня. . .":
                    "Этот выбор отправит девушку подальше от вас, временно удалив ее из игры."
                    "Вы всегда сможете попросить вернуть ее."
                    $ Line = 0
                    menu:
                        ch_p "Не могли бы вы избавиться от. . ."
                        "[RogueX.Name_rod]" if RogueX in ActiveGirls:
                                $ Line = RogueX
                        "[KittyX.Name_rod]" if KittyX in ActiveGirls and "met" in KittyX.History:
                                $ Line = KittyX
                        "[EmmaX.Name_rod]" if EmmaX in ActiveGirls and "met" in EmmaX.History:
                                $ Line = EmmaX
                        "[LauraX.Name_rod]" if LauraX in ActiveGirls and "met" in LauraX.History and "dress0" not in LauraX.History:
                                $ Line = LauraX
                        "[JeanX.Name_rod]" if JeanX in ActiveGirls and "met" in JeanX.History:
                                $ Line = JeanX
                        "[StormX.Name_rod]" if StormX in ActiveGirls and "met" in StormX.History:
                                $ Line = StormX
                        "[JubesX.Name_rod]" if JubesX in ActiveGirls and "met" in JubesX.History:
                                $ Line = JubesX
                        "[GwenX.Name_rod]" if GwenX in ActiveGirls and "met" in GwenX.History:
                                $ Line = GwenX
                        "[BetsyX.Name_rod]" if BetsyX in ActiveGirls and "met" in BetsyX.History:
                                $ Line = BetsyX
                        "[DoreenX.Name_rod]" if DoreenX in ActiveGirls and "met" in DoreenX.History:
                                $ Line = DoreenX
                                $ Player.History.remove("SGattic") if "SGattic" in Player.History else 0
                                $ Player.History.remove("stormreport") if "stormreport" in Player.History else 0
                                $ Player.History.remove("doreenafter") if "doreenafter" in Player.History else 0
                        "[WandaX.Name_rod]" if WandaX in ActiveGirls and "met" in WandaX.History:
                                $ Line = WandaX
                        "Неважно. . .":
                                $ Count += 1
                    if Line:
                            #if you picked someone. . .
                            if len(ActiveGirls) <= 1:
                                    #if this is the only girl left. . .
                                    ch_x "Честно говоря, у меня забот с другими дамами полно, так что я не уверен, что смогу справиться с еще одной. . ."
                                    ch_x "Боюсь, тебе придется с этим смириться."
                            else:
                                    ch_x "Ну, хорошо, думаю, что смогу занять ее различными делами в кампусе. . ."
                                    ch_x "Больше она тебя не побеспокоит."

                            if Line.Loc == bg_current:
                                    #if she's in the room
                                    $ Line.Statup("Love", 90, -10)
                                    $ Line.Statup("Obed", 50, 3)
                                    if Line == RogueX:
                                            ch_r "То есть, я тебе \"мешаю\"?"
                                    elif Line == KittyX:
                                            ch_k "Эй, зачем тебе это?!"
                                    elif Line == EmmaX:
                                            ch_e "Прошу прощения? Похоже я не расслышала."
                                    elif Line == LauraX:
                                            ch_l "Объяснись."
                                    elif Line == JeanX:
                                            ch_j "Ты издеваешься надо мной?!"
                                    elif Line == StormX:
                                            ch_s "Я не понимаю."
                                    elif Line == JubesX:
                                            ch_v "Серьезно?!"
                                    elif Line == GwenX:
                                            ch_g "Эй!"
                                    elif Line == BetsyX:
                                            ch_b "Что?"
                                    elif Line == DoreenX:
                                            ch_d "Чего-чего?"
                                    elif Line == WandaX:
                                            ch_w "Эй!"
                                    menu:
                                        extend ""
                                        "Ох, прошу прощения, профессор, это была ошибка.":
                                                if ApprovalCheck(Line, 2000):
                                                        #if she accepts it
                                                        $ Line.FaceChange("confused")
                                                        $ Line.Statup("Love", 90, 3)
                                                        $ Line.Statup("Obed", 50, 2)
                                                        if Line == RogueX:
                                                                ch_r "Вот и правильно. . ."
                                                        elif Line == KittyX:
                                                                ch_k "Угу?"
                                                        elif Line == EmmaX:
                                                                ch_e ". . . правильно. . ."
                                                        elif Line == LauraX:
                                                                ch_l "Как скажешь."
                                                        elif Line == JeanX:
                                                                ch_j "Тебе придется объясниться. . ."
                                                        elif Line == StormX:
                                                                ch_s "Я это запомню. . ."
                                                        elif Line == JubesX:
                                                                ch_v "Тоооочно."
                                                        elif Line == GwenX:
                                                                ch_g "Конечно, простая ошибка. . ."
                                                        elif Line == BetsyX:
                                                                ch_b "Конечно. . ."
                                                        elif Line == DoreenX:
                                                                ch_d "Угу, конечно. . ."
                                                        elif Line == WandaX:
                                                                ch_w "Ага, конечно. . ."
                                                else:
                                                        #if she's mad
                                                        $ Line.FaceChange("angry")
                                                        $ Line.Statup("Obed", 50, -2)
                                                        $ Line.Statup("Inbt", 60, 3)
                                                        if Line == RogueX:
                                                                ch_r "Угу-м."
                                                        elif Line == KittyX:
                                                                ch_k "Ага."
                                                        elif Line == EmmaX:
                                                                ch_e "Я не знаю, о чем ты вообще думал."
                                                        elif Line == LauraX:
                                                                ch_l "Угу-м."
                                                        elif Line == JeanX:
                                                                ch_j "Тебе придется объясниться. . ."
                                                        elif Line == StormX:
                                                                ch_s "Я это запомню. . ."
                                                        elif Line == JubesX:
                                                                ch_v "Тебе придется объясниться."
                                                        elif Line == GwenX:
                                                                ch_g "Ты ходишь по тонкому льду. . ."
                                                        elif Line == BetsyX:
                                                                ch_b "Ты пожалеешь об этом. . ."
                                                        elif Line == DoreenX:
                                                                ch_d "Знаешь, я могу и укусить."
                                                        elif Line == WandaX:
                                                                ch_w "Я еще могу устроить тебе маленький ад!"
                                                $ Line = 0
                                        "Извини, но мне просто нужно немного времени \"для себя\".":
                                                if len(ActiveGirls) > 1:
                                                            $ ActiveGirls.remove(Line)
                                                $ Line.Statup("Obed", 50, 5)
                                                $ Line.Statup("Obed", 90, 2)
                                                $ Line.Statup("Inbt", 60, 2)
                                                if ApprovalCheck(Line, 900, "L") or ApprovalCheck(Line, 2000):
                                                        #if she accepts it
                                                        $ Line.FaceChange("sadside")
                                                        if Line == RogueX:
                                                                ch_r "Пожалуй, если ты это сделаешь, я дам тебе немного свободы."
                                                        elif Line == KittyX:
                                                                ch_k "Ну, думаю, мы могли бы отдохнуть друг от друга. . ."
                                                        elif Line == EmmaX:
                                                                ch_e "Я бы не хотела быть для тебя помехой. . ."
                                                        elif Line == LauraX:
                                                                ch_l "Я могу стать незаметной. . ."
                                                        elif Line == JeanX:
                                                                ch_j "Что ж, думаю, я могу найти кого-нибудь другого, чтобы скрасить свое время. . ."
                                                        elif Line == StormX:
                                                                ch_s ". . . хорошо, я понимаю. . ."
                                                        elif Line == JubesX:
                                                                ch_v "Ладно, неважно, у меня дела."
                                                        elif Line == GwenX:
                                                                ch_g "Значит, ты не хочешь, чтобы я смотрела, как ты мастурбируешь?"
                                                        elif Line == BetsyX:
                                                                ch_b "Прости меня за заботу. . ."
                                                        elif Line == DoreenX:
                                                                ch_d "Ну. . . наверное, я понимаю. . ."
                                                        elif Line == WandaX:
                                                                ch_w ". . . ладно, ненадолго я могу оставить тебя. . ."
                                                else:
                                                        #if she's mad
                                                        $ Line.Statup("Love", 90, -5)
                                                        $ Line.FaceChange("angry")
                                                        $ Line.AddWord(1,"angry","angry")
                                                        if Line == RogueX:
                                                                ch_r "Ох, ты его получишь."
                                                        elif Line == KittyX:
                                                                ch_k "Ага, ну и мне тогда тоже!"
                                                        elif Line == EmmaX:
                                                                ch_e "У меня есть и другие дела."
                                                        elif Line == LauraX:
                                                                ch_l "Я тоже занята."
                                                        elif Line == StormX:
                                                                ch_s "Ох, ты получишь его. . ."
                                                        elif Line == JubesX:
                                                                ch_v "Тебе придется объясниться."
                                                        elif Line == GwenX:
                                                                ch_g "У тебя появится время \"для себя\", когда у меня будет своя спин-офф игра!"
                                                        elif Line == BetsyX:
                                                                ch_b "Это можно устроить."
                                                        elif Line == DoreenX:
                                                                ch_d "Ох, будет тебе личное время."
                                                        elif Line == WandaX:
                                                                ch_w "О да, думаю, я могу дать тебе его."
                                        "Ты меня слышала.":
                                                if len(ActiveGirls) > 1:
                                                            $ ActiveGirls.remove(Line)
                                                $ Line.Statup("Love", 80, -5)
                                                $ Line.Statup("Love", 90, -5)
                                                $ Line.Statup("Obed", 80, 5)
                                                if ApprovalCheck(Line, 850, "O") or ApprovalCheck(Line, 1500, "LO"):
                                                        #if she accepts it
                                                        $ Line.FaceChange("sadside")
                                                        $ Line.Statup("Obed", 200, 10)
                                                else:
                                                        #if she's mad
                                                        $ Line.FaceChange("angry")
                                                        $ Line.Statup("Love", 90, -5)
                                                        $ Line.Statup("Inbt", 60, 5)
                                                        $ Line.AddWord(1,"angry","angry")
                                                if Line == RogueX:
                                                        ch_r "Четко и ясно."
                                                elif Line == KittyX:
                                                        ch_k ". . ."
                                                elif Line == EmmaX:
                                                        ch_e "Полагаю, что да."
                                                elif Line == LauraX:
                                                        ch_l "Как скажешь."
                                                elif Line == JeanX:
                                                        ch_j "Отменно. . ."
                                                elif Line == StormX:
                                                        ch_s "Четко как гром. . ."
                                                elif Line == JubesX:
                                                        ch_v "Тебе придется объясниться."
                                                elif Line == GwenX:
                                                        ch_g "О, я прекрасно тебя услышала. . ."
                                                elif Line == BetsyX:
                                                        ch_b "Слишком отчетливо."
                                                elif Line == DoreenX:
                                                        ch_d "-О- да."
                                                elif Line == WandaX:
                                                        ch_w "Ага."
                                    #end "picked same girl
                            else:
                                    #if she is not in the room
                                    if len(ActiveGirls) > 1:
                                                $ ActiveGirls.remove(Line)
                                    if Line == GwenX:
                                        $ Player.AddWord(1,0,0,"gwengone",0) #adds to traits
                                        $ GwenX.Event[7] = 7
                    if Line == GirlX:
                        if not Player.Male:
                            call AnyLine(GirlX,"Ты забыла, что я - твой план спасения?")
                        else:
                            call AnyLine(GirlX,"Ты забыл, что я - твой план спасения?")
                        menu:
                            "Ох. . .":
                                    ch_x "Я забуду о твоей просьбе."
                                    $ Count = 0
                    $ Line = 0
            #end "remove girl"

            "Я хочу вернуть девушку. . ." if len(TotalGirls) > len (ActiveGirls):
                    "Этот вариант вернет девушку в активную игру."
                    "Вы всегда сможете попросить отослать ее снова."
                    $ Line = 0
                    menu:
                        ch_p "Не могли бы вы вернуть. . ."
                        "[RogueX.Name_vin]" if RogueX not in ActiveGirls:
                                $ Line = RogueX
                        "[KittyX.Name_vin]" if KittyX not in ActiveGirls and "met" in KittyX.History:
                                $ Line = KittyX
                        "[EmmaX.Name_vin]" if EmmaX not in ActiveGirls and "met" in EmmaX.History:
                                $ Line = EmmaX
                        "[LauraX.Name_vin]" if LauraX not in ActiveGirls and "met" in LauraX.History and "dress0" not in LauraX.History:
                                #Laura has a special condition because of her introduction story
                                $ Line = LauraX
                        "[JeanX.Name_vin]" if JeanX not in ActiveGirls and "met" in JeanX.History:
                                $ Line = JeanX
                        "[StormX.Name_vin]" if StormX not in ActiveGirls and "met" in StormX.History:
                                $ Line = StormX
                        "[JubesX.Name_vin]" if JubesX not in ActiveGirls and "met" in JubesX.History:
                                $ Line = JubesX
                        "[GwenX.Name_vin]" if GwenX not in ActiveGirls and "met" in GwenX.History:
                                $ Line = GwenX
                                $ GwenX.Event[7] = 0
                                $ Player.DrainWord("gwengone",0,0,1) #removes from traits
                                #$ GwenX.DrainWord("promised",0,0,1) #removes from traits
                                #$ GwenX.DrainWord("goodbye",0,0,1) #removes from traits
                        "[BetsyX.Name_vin]" if BetsyX not in ActiveGirls and "met" in BetsyX.History:
                                $ Line = BetsyX
                        "[DoreenX.Name_vin]" if DoreenX not in ActiveGirls and "met" in DoreenX.History:
                                $ Line = DoreenX
                        "[WandaX.Name_vin]" if WandaX not in ActiveGirls and "met" in WandaX.History:
                                $ Line = WandaX
                        "Неважно. . .":
                                $ Count += 1
                    if Line:
                            #if you picked someone. . .
                            ch_x "Конечно. Я занимал ее работой, но я могу освободить ее. . ."
                            ch_x "Теперь у нее будет больше свободного времени. . ."
                            $ ActiveGirls.append(Line)
                    $ Line = 0
            "Меня интересует ключ. . . ":
                menu:
                    "Дайте мне ключ от вашего кабинета." if "Xavier" not in Keys:
                            ch_x "Fine, take it. . ."
                            $ Keys.append("Xavier")
                    "Дайте мне ключ от вашего кабинета.[[Уже есть] (locked)" if "Xavier" in Keys:
                            pass

                    "Дайте мне ключ от комнаты [GirlX.Name_rod]." if GirlX not in Keys:
                            ch_x "I. . . suppose I could do that. . ."
                            $ Keys.append(GirlX)
                    "Дайте мне ключ от комнаты [GirlX.Name_rod] [[Уже есть] (locked)" if GirlX in Keys:
                            pass

                    "Неважно.":
                            $ Count += 1
            "Ладно, достаточно.":
                $ Count = 0

    ch_x "Хорошо, на этом и закончим. Пожалуйста, уходите."
    if GirlX is RogueX:
            if "Omega" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Love", 70, 30)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Omega")
            ch_p "Ладно, хватит. Пусть Ксавье забудет обо всем, что здесь произошло, а потом уходим."
            $ GirlX.Arms = "gloves"
            $ GirlX.ArmPose = 1
    elif GirlX is KittyX:
            if "Kappa" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Kappa")
            $ GirlX.ArmPose = 2
    elif GirlX is EmmaX:
            ch_p "Ладно, хватит. Пусть Ксавье забудет обо всем, что здесь произошло, а потом уходим."
            if "Psi" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Psi")
    elif GirlX is LauraX:
            if "Chi" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Chi")
            $ GirlX.ArmPose = 1
            $ GirlX.Claws = 0
    elif GirlX is JeanX:
            ch_p "Ладно, хватит. Пусть Ксавье забудет обо всем, что здесь произошло, а потом уходим."
            if "Alpha" not in Player.Traits:
                    $ GirlX.Statup("Lust", 70, 20)
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Obed", 70, 10)
                    $ GirlX.Statup("Obed", 200, 20)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Alpha")
    elif GirlX is StormX:
            if "Rho" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Rho")
    elif GirlX is JubesX:
            if "Zeta" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Zeta")
            $ GirlX.ArmPose = 2
    elif GirlX is GwenX:
            if "Gamma" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Gamma")
            $ GirlX.ArmPose = 2
            "[GwenX.Name] делает жест рукой вверх, как будто сворачивает окно."
            ch_g "Хорошо, консоль закрыта."
    elif GirlX is BetsyX:
            if "Beta" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Chi")
            $ GirlX.ArmPose = 1
            $ GirlX.Knife = 0
    elif GirlX is DoreenX:
            if "Delta" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Delta")
            $ GirlX.ArmPose = 1
    elif GirlX is WandaX:
            if "Upsilon" not in Player.Traits:
                    $ GirlX.Statup("Lust", 90, 10)
                    $ GirlX.Statup("Inbt", 80, 10)
                    $ GirlX.Statup("Love", 70, 10)
                    $ GirlX.Statup("Love", 200, 20)
                    $ Player.Traits.append("Upsilon")

    $ Line = 0
    $ Player.DailyActions.append("Xavier")
    call Remove_Girl("All")
    hide Professor
    $ bg_current = "bg player"
    call Set_The_Scene
    "Вы возвращаетесь в свою комнату."
    jump Misplaced

# end Caught / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Caught Changing/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Caught_Changing(Girl=0): #rkeljsvgbdw
        if Girl not in TotalGirls:
                return
        call Shift_Focus(Girl)
        $ D20 = renpy.random.randint(1, 20)

        $ Girl.FaceChange("surprised", 1,Mouth="kiss")
        call Remove_Girl("All")

        if D20 > 17:
                #She's naked
                $ Girl.OutfitChange("nude")
        else:
                #restore base outfit
                $ Girl.OutfitChange(6)
                if D20 >15:
                        #She's bottomless
                        $ Girl.Legs = 0 #Legs
                        $ Girl.Hose = 0 #Hose
                        $ Girl.Panties = 0 #Panties
                elif D20 >14:
                        #She's Topless
                        $ Girl.Chest = 0 #Over
                        $ Girl.Over = 0 #Chest
                elif D20 >10:
                        #She's in her underwear
                        $ Girl.Over = 0 #Over
                        $ Girl.Legs = 0 #Legs
                elif D20 >5:
                        #She's wearing pants/skirt but no shirt
                        $ Girl.Over = 0 #Over
                $ Girl.Boots = 0 #Boots
                $ Girl.Hat = 0 #Hat
        #else: #fully dressed
        $ Girl.Loc = bg_current
        call Set_The_Scene(Dress=0)
        call Show_In_Door(Girl)
        show bg_opendoor zorder 151 #shows the door open
        if D20 > 17:
                #She's naked
                "Когда вы входите в комнату, вы видите [Girl.Name_vin] голой, похоже, она одевается."
        elif D20 >14:
                #She's Topless
                "Когда вы входите в комнату, вы видите [Girl.Name_vin] практически голой, похоже, она одевается."
        elif D20 >10:
                #She's in her underwear
                "Когда вы входите в комнату, вы видите [Girl.Name_vin] в нижнем белье, похоже, она одевается."
        elif D20 >5:
                #She's wearing pants/skirt
                "Когда вы входите в комнату, вы видите [Girl.Name_vin] без верха, похоже, она одевается."
        else:
                #She's done
                "Когда вы входите в комнату, вы видите, как [Girl.Name_vin] натягивает верхнюю одежду, похоже, она закончила одеваться."

        if Girl is StormX:
                ch_s "Ох, здравствуй, [Girl.Petname]."
        elif ApprovalCheck(Girl, 1400):
                if Girl is RogueX:
                        ch_r "О, привет."
                elif Girl is KittyX:
                        ch_k "Привет, [Girl.Petname]."
                elif Girl is EmmaX:
                        if not Player.Male:
                            ch_e "Ох, пришла посмотреть?"
                        else:
                            ch_e "Ох, пришел посмотреть?"
                elif Girl is LauraX:
                        ch_l "Привет."
                elif Girl is JeanX:
                        ch_j "О, [Girl.Petname]?"
                elif Girl is JubesX:
                        ch_v "Йо."
                elif Girl is GwenX:
                        ch_g "Привет."
                elif Girl is BetsyX:
                        ch_b "Ох!"
                elif Girl is DoreenX:
                        ch_d "Хех. . . привет."
                elif Girl is WandaX:
                        ch_w "Привет."
        else:
                if D20 > 5:
                        #she's undressed

                        if not Player.Male and "girltalk" not in Girl.History and not ApprovalCheck(Girl, 1400):
                                if Girl is RogueX:
                                        ch_r "О, привет."
                                elif Girl is KittyX:
                                        ch_k "Привет, [Girl.Petname]."
                                elif Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Ох, пришла посмотреть?"
                                        else:
                                            ch_e "Ох, пришел посмотреть?"
                                elif Girl is LauraX:
                                        ch_l "Привет."
                                elif Girl is JeanX:
                                        ch_j "О, [Girl.Petname]?"
                                elif Girl is JubesX:
                                        ch_v "Йо."
                                elif Girl is GwenX:
                                        ch_g "Привет."
                                elif Girl is BetsyX:
                                        ch_b "Ох!"
                                elif Girl is DoreenX:
                                        ch_d "Хех. . . привет."
                                elif Girl is WandaX:
                                        ch_w "Привет."
                                call Girl_First_Bottomless(Girl,1)
                                call Girl_First_Topless(Girl,1)

                        elif not ApprovalCheck(Girl, (D20 *70)) and (not Girl.SeenPussy or not Girl.SeenChest):
                                # if D20*70 is less than her approval, and this is the first you've seen of her bits. . .
                                $ Girl.FaceChange("surprised",Brows="angry")
                                $ Girl.Statup("Love", 80, -50)

                                if (Girl.OverNum() + Girl.ChestNum() <5) or (Girl.PantsNum() < 5 and Girl.HoseNum() < 10):
                                    # if either she is mostly topless or mostly bottomless)

                                    call Girl_First_Bottomless(Girl,1)
                                    call Girl_First_Topless(Girl,1)
                                    $ Girl.Over = "towel"
                                    "Она хватает полотенце и прикрывается им."
                        else:
                                #She's cool with it, but confused.
                                $ Girl.FaceChange("surprised", 1,Brows = "confused")
                                if "exhibitionist" in Girl.Traits:
                                    $ Girl.Statup("Lust", 200, (2*D20))
                                else:
                                    $ Girl.Statup("Lust", 200, D20)
                                if D20 > 17:
                                        call Girl_First_Bottomless(Girl)
                                        call Girl_First_Topless(Girl,1)
                                elif D20 > 15:
                                        call Girl_First_Bottomless(Girl)
                                elif D20 > 14:
                                        call Girl_First_Topless(Girl)
                        $ Girl.Statup("Inbt", 70, 20)


                        if not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History and not ApprovalCheck(Girl, 1400):
                            pass
                        else:
                            if Girl is RogueX:
                                    ch_r "Эй! Может, научишься сначала стучать?!"
                            elif Girl is KittyX:
                                    if not Player.Male:
                                        ch_k "Почему ты не постучала?!"
                                    else:
                                        ch_k "Почему ты не постучал?!"
                            elif Girl is EmmaX:
                                    if not Player.Male:
                                        ch_e "Ты не думала сначала постучать?"
                                    else:
                                        ch_e "Ты не думал сначала постучать?"
                            elif Girl is LauraX:
                                    if not Player.Male:
                                        ch_l "Даже не подумала постучать?"
                                    else:
                                        ch_l "Даже не подумал постучать?"
                            elif Girl is JeanX:
                                    if not Player.Male:
                                        ch_j "Забыла постучать, [JeanX.Petname]?"
                                    else:
                                        ch_j "Забыл постучать, [JeanX.Petname]?"
                            elif Girl is JubesX:
                                    ch_v "Эй, может сначала стоило постучать?"
                            elif Girl is GwenX:
                                    ch_g "Разве люди в вашей вселенной не умеют стучать?"
                            elif Girl is BetsyX:
                                    ch_b "Разве в штатах не принято сперва стучаться?"
                            elif Girl is DoreenX:
                                    ch_d "Эй, стоит сперва стучаться!"
                            elif Girl is WandaX:
                                    ch_w "Эй, может, сперва стоило постучать?"
                            menu:
                                extend ""
                                "Извини, мне стоило сначала постучаться.":
                                        $ Girl.Statup("Love", 50, 2)
                                        $ Girl.Statup("Love", 80, 4)
                                "И пропустить все самое интересное?":
                                        $ Girl.Statup("Obed", 50, 2)
                                        $ Girl.Statup("Obed", 80, 2)
                                        $ Girl.Statup("Inbt", 60, 1)
                                        call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                        #end if she's partially nude
                else:
                        #She's fully dressed
                        if not ApprovalCheck(Girl, 800) and (not Girl.SeenPussy or not Girl.SeenChest):
                                $ Girl.FaceChange("angry",Brows="confused")
                                $ Girl.Statup("Love", 80, -5)
                        else:
                                $ Girl.FaceChange("sexy",Brows="confused")
                        $ Girl.Statup("Inbt", 50, 3)

                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Ну привет, [Girl.Petname]. Надеялась увидеть что-то еще?"
                                else:
                                    ch_r "Ну привет, [Girl.Petname]. Надеялся увидеть что-то еще?"
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Привет, [Girl.Petname]. . . {i}ты{/i} надеялась, что я буду гоооолой?"
                                else:
                                    ch_k "Привет, [Girl.Petname]. . . {i}ты{/i} надеялся, что я буду гоооолой?"
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Ты надеялась застать меня в компрометирующем положении?"
                                else:
                                    ch_e "Ты надеялся застать меня в компрометирующем положении?"
                        elif Girl is LauraX:
                                ch_l "Привет, [Girl.Petname]. Пытаешься подглядывать?"
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "О, [Girl.Petname]. Надеялась, что я переодеваюсь?"
                                else:
                                    ch_j "О, [Girl.Petname]. Надеялся, что я переодеваюсь?"
                        elif Girl is JubesX:
                                if not Player.Male:
                                    ch_v "Привет, [Girl.Petname]. Надеялась снова застать меня голой?"
                                else:
                                    ch_v "Привет, [Girl.Petname]. Надеялся снова застать меня голой?"
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "О, привет. Надеялась, что тебе снова повезет?"
                                else:
                                    ch_g "О, привет. Надеялся, что тебе снова повезет?"
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ох. . . здравствуй. Надеялась что-то увидеть?"
                                else:
                                    ch_b "Ох. . . здравствуй. Надеялся что-то увидеть?"
                        elif Girl is DoreenX:
                                ch_d "Тебе следовало сперва постучать, я могла быть голой!"
                        elif Girl is WandaX:
                                if not Player.Male:
                                    ch_w "Слушай, [Girl.Petname], уверена, ты расчитывала на большее. . ."
                                else:
                                    ch_w "Слушай, [Girl.Petname], уверена, ты расчитывал на большее. . ."

                        menu:
                            extend ""
                            "Извини, мне стоило сначала постучаться.":
                                    $ Girl.Statup("Love", 50, 2)
                                    $ Girl.Statup("Love", 80, 2)
                            "Ну, честно говоря, я. . .":
                                    $ Girl.Statup("Love", 50, -2)
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                $ Girl.FaceChange("sexy")
                if ApprovalCheck(Girl, 1000,Alt=[[DoreenX],1200]):
                        #she flashes you
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Ты могла бы просто попросить, [RogueX.Petname]."
                                else:
                                    ch_r "Ты мог бы просто попросить, [RogueX.Petname]."
                        elif Girl is KittyX:
                                ch_k "Я не сказала, что {i}против{/i}. . ."
                        elif Girl is EmmaX:
                                ch_e "Тогда я проявлю инициативу. . ."
                        elif Girl is LauraX:
                                ch_l "Я не против."
                        elif Girl is JeanX:
                                ch_j "Что ж, дам аудитории то, что она хочет. . ."
                        elif Girl is JubesX:
                                ch_v "Тебе просто нужно попросить. . ."
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Знаешь, ты могла просто попросить."
                                else:
                                    ch_g "Знаешь, ты мог просто попросить."
                        elif Girl is BetsyX:
                                ch_b "В следующий раз просто попроси. Я не так уж и застенчивая."
                        elif Girl is DoreenX:
                                ch_d "Думаю, если тебе так хочется что-то увидеть. . ."
                        elif Girl is WandaX:
                                ch_w "Что ж, если тебе так этого хочется. . ."

                        $ Girl.Uptop = 1 #Uptop up
                        $ Girl.Upskirt = 1 #Upskirt up
                        pause 1
                        call Girl_First_Topless(Girl,1)
                        call Girl_First_Bottomless(Girl,1)
                        $ Girl.Uptop = 0 #Uptop up
                        $ Girl.Upskirt = 0 #Upskirt up
                        "Она быстро показывает вам кое-что интересное."
                else:
                        #if she doesn't flash you
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Ну, бывает, просто в следующий раз будь осторожна."
                                else:
                                    ch_r "Ну, бывает, просто в следующий раз будь осторожен."
                        elif Girl is KittyX:
                                ch_k "Ага. . . нам не нужны неприятные случайности. . ."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Хм, в следующий раз будь более осторожна. . ."
                                else:
                                    ch_e "Хм, в следующий раз будь более осторожен. . ."
                        elif Girl is LauraX:
                                ch_l "Угу. . ."
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Конечно, извращенка."
                                else:
                                    ch_j "Конечно, извращенец."
                        elif Girl is JubesX:
                                ch_v "Не надо подкрадываться."
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Извращенка."
                                else:
                                    ch_g "Извращенец."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Идиотка."
                                else:
                                    ch_b "Идиот."
                        elif Girl is DoreenX:
                                if not Player.Male:
                                    ch_d "Не будь такой жуткой."
                                else:
                                    ch_d "Не будь таким жутким."
                        elif Girl is WandaX:
                                if not Player.Male:
                                    ch_w "Нет причин быть такой жуткой. . ."
                                else:
                                    ch_w "Нет причин быть таким жутким. . ."
                #end "if she isn't into you."
        if Girl is RogueX:
                ch_r "Ну, ты собираешься остаться здесь?"
        elif Girl is KittyX:
                ch_k "Итак, ты планируешь остаться?"
        elif Girl is EmmaX:
                ch_e "У тебя ко мне дело?"
        elif Girl is LauraX:
                ch_l "Так, ты планируешь остаться?"
        elif Girl is JeanX:
                if not Player.Male:
                    ch_j "Так, чего ты хотела?"
                else:
                    ch_j "Так, чего ты хотел?"
        elif Girl is StormX:
                ch_s "Могу ли я чем-нибудь тебе помочь?"
        elif Girl is JubesX:
                if not Player.Male:
                    ch_v "Ты чего-то хотела?"
                else:
                    ch_v "Ты чего-то хотел?"
        elif Girl is GwenX:
                ch_g "Тебе что-то нужно?"
        elif Girl is BetsyX:
                ch_b "Я могу тебе чем-нибудь помочь?"
        elif Girl is DoreenX:
                ch_d "Ты что-то хочешь?"
        elif Girl is WandaX:
                ch_w "Ну и? Тебе что-то нужно?"
        menu:
                extend ""
                "Может, проведем немного время вместе?":
                        pass

                "Если честно, мне пора идти. . .":
                        $ Girl.OutfitChange(6,Changed=0)
                        $ renpy.pop_call()
                        call Worldmap

        if (Girl is StormX or ApprovalCheck(Girl, 1400))and D20 > 5:
            #she's at least partly nude
            call AnyLine(Girl,"Ладно, тогда дай мне закончить одеваться. . .")
            menu:
                "Ладно.":
                                "Она заканчивает одеваться."
                                $ Girl.OutfitChange(6,Changed=0)
                "Кстати, ты могла бы оставить все как есть.":
                        if ApprovalCheck(Girl, 950+(40*D20),Alt=[[StormX],450+(10*D20)]): #950-1350
                                $ Girl.Statup("Love", 70, 3)
                                $ Girl.Statup("Obed", 50, 1)
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.Statup("Inbt", 60, 2)
                                $ Girl.FaceChange("sexy")
                                if Girl is StormX:
                                        ch_s "Пожалуй, я согласна. . ."
                                else:
                                        call AnyLine(Girl,"Думаю, можно. . .")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.Statup("Inbt", 60, 2)
                                $ Girl.FaceChange("smile")
                                if Girl is StormX:
                                        ch_s "Ха! Я бы не хотела слишком сильно отвлекать тебя."
                                else:
                                        call AnyLine(Girl,"Я так не думаю. . .")
                                $ Girl.OutfitChange(6,Changed=0)
                        call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                "Почему бы тебе не снять и все остальное?":
                        $ Girl.FaceChange("sexy")
                        if ApprovalCheck(Girl, 1400,Alt=[[StormX],700]):
                                $ Girl.Statup("Love", 50, 1)
                                $ Girl.Statup("Love", 70, 1)
                                $ Girl.Statup("Obed", 50, 1)
                                $ Girl.Statup("Obed", 80, 1)
                                $ Girl.Statup("Inbt", 70, 1)
                                if Girl is StormX:
                                        ch_s "О, шалунишка. . ."
                                else:
                                        call AnyLine(Girl,"Ну. . .")
                                $ Girl.OutfitChange("nude")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        elif ApprovalCheck(Girl, 850+(10*D20)): #400-550
                                $ Girl.Statup("Love", 80, 1)
                                $ Girl.Statup("Obed", 50, 1)
                                $ Girl.Statup("Obed", 80, 1)
                                $ Girl.Statup("Inbt", 70, 2)
                                if Girl is StormX:
                                        ch_s "Я могла бы, по крайней мере. . . ненадолго остановиться?"
                                else:
                                        call AnyLine(Girl,"Ну. . .")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.Statup("Love", 60, 1)
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Inbt", 70, 1)
                                if Girl is StormX:
                                        ch_s "Да ты шутишь, [Girl.Petname]."
                                else:
                                        call AnyLine(Girl,"Ты, должно быть, шутишь. . .")
                                $ Girl.OutfitChange(6,Changed=0)
                        call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                "Не надо, оставь все как есть.":
                        $ Girl.Statup("Obed", 80, 2)
                        if ApprovalCheck(Girl, 1300,Alt=[[StormX],1100]):
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Inbt", 60, 1)
                                $ Girl.FaceChange("sexy")
                                call AnyLine(Girl,"Если ты этого хочешь. . .")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.Statup("Obed", 50, -1)
                                $ Girl.FaceChange("angry")
                                if Girl is StormX:
                                        ch_s "[Girl.Petname], это не тебе решать."
                                else:
                                        call AnyLine(Girl,"Ни за что. . .")
                                $ Girl.OutfitChange(6,Changed=0)
                        call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                "Сними все остальное.":
                        $ Girl.Statup("Obed", 80, 2)
                        if ApprovalCheck(Girl,1300):
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Inbt", 60, 1)
                                $ Girl.FaceChange("sexy")
                                call AnyLine(Girl,". . . хорошо.")
                                $ Girl.OutfitChange("nude")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        elif ApprovalCheck(Girl,600) and ApprovalCheck(Girl, 500, "O"):
                                $ Girl.Statup("Love", 50, -2)
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 80, 1)
                                $ Girl.FaceChange("sexy",Eyes="side")
                                call AnyLine(Girl,". . . ладно.")
                                $ Girl.OutfitChange("nude")
                                $ Girl.Set_Temp_Outfit() #sets current outfit as temporary
                        else:
                                $ Girl.Statup("Love", 50, -2)
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.Statup("Obed", 50, -2)
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.FaceChange("angry")
                                if Girl is StormX:
                                        ch_s "Я так не думаю."
                                else:
                                        call AnyLine(Girl,"Ни за что!")
                                $ Girl.OutfitChange(6,Changed=0)
                        call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
        hide bg_opendoor
        call Display_Girl(Girl,0,1)
        "Вы входите в комнату."
        return
#End Girl Caught Changing


label Girl_Caught_Mastubating(Girl=0): #rkeljsvgbdw
        #called by room entry dialog if the girl was masturbating
        if Girl not in TotalGirls:
            return
        $ Girl.DrainWord("gonnafap")
        call Remove_Girl("All")
        $ Girl.Loc = bg_current
        "Когда вы приближаетесь к ее комнате, вы слышите тихие стоны изнутри и замечаете, что дверь слегка приоткрыта."
        menu:
            extend ""
            "Вежливо постучать":
                $ Line = "knock"
            "Заглянуть внутрь":
                call Shift_Focus(Girl)
                show blackscreen onlayer black
                $ Girl.Upskirt = 1
                $ Girl.PantiesDown = 1
                $ Girl.Loc = bg_current
                #call CleartheRoom(Girl,1,1)
                call Set_The_Scene
                $ Girl.FaceChange("sexy")
                $ Girl.Eyes = "closed"
                $ Girl.ArmPose = 2
                $ Count = 0
                $ Trigger = "masturbation"
                hide blackscreen onlayer black
                $ Girl.Offhand = "fondle pussy"
                "Вы видите [Girl.Name_vin], энергично ласкающую себя с закрытыми глазами."
                menu:
                    extend ""
                    "Тихонько войти":
                            $ Line = "enter"
                    "Отойти и постучаться":
                            $ Line = "knock"
                    "Тихонько уйти":
                            $ Line = "leave"
                $ Trigger = 0
            "Тихонько войти":
                    $ Line = "enter"
            "Тихонько уйти":
                    $ Line = "leave"

        if Line == "leave":
                $ Girl.Statup("Lust", 80, 20)
                "Вы оставляете [Girl.Name_vin] заниматься своими делами и уходите."
                $ renpy.pop_call()
                jump Campus_Map
        elif Line == "knock":
                "Вы слышите тихие стоны, за которыми следует какая-то суета. Что-то падает на пол."
                "Через несколько секунд ожидания и звуков надевающейся одежды, [Girl.Name] подходит к двери."
                $ Girl.FaceChange("confused",1,Eyes = "surprised",Mouth = "smile")
                $ Trigger = 0
#                $ Trigger3 = 0
                $ Girl.Offhand = 0
                call Set_The_Scene
                if Girl is RogueX:
                        ch_r "Извини за ожидание, [RogueX.Petname], Я. . . тренировалась."
                elif Girl is KittyX:
                        ch_k "О, привет, [KittyX.Petname], я. . . неважно."
                elif Girl is EmmaX:
                        ch_e "Ну, можно сказать, я была немного. . . занята."
                elif Girl is LauraX:
                        ch_l "Эм, привет, [LauraX.Petname], я просто справлялась со стресом."
                elif Girl is JeanX:
                        ch_j "О, [JeanX.Petname]. Я была. . . а, неважно."
                elif Girl is StormX:
                        ch_s "Ох, эм, [StormX.Petname]. Я просто. . . разминалась."
                elif Girl is JubesX:
                        ch_v "О, привет, [Girl.Petname]. . . Я. . ."
                elif Girl is GwenX:
                        ch_g "О, эм. . . привет. . ."
                        ch_g "Здесь не на что смотреть. . ."
                elif Girl is BetsyX:
                        ch_b "Извини, что так долго. . . я была. . . сильно занята."
                elif Girl is DoreenX:
                        ch_d "Ох. . . боже. . . я. . ."
                        ch_d "Знаешь, неважно, как твои дела?"
                elif Girl is WandaX:
                        ch_w "Привет, [Girl.Petname]. . ."
                        ch_w "Я была. . . кое-чем занята."
                $ Tempmod += 10
        elif Line == "enter":
                call Shift_Focus(Girl)
                show blackscreen onlayer black
                $ Girl.Upskirt = 1
                $ Girl.PantiesDown = 1
                $ Girl.Loc = bg_current
                #call CleartheRoom(Girl,1,1)
                call Set_The_Scene
                $ Girl.FaceChange("sexy")
                $ Girl.Eyes = "closed"
                $ Girl.ArmPose = 2
                $ Count = 0
                $ Trigger = "masturbation"
                hide blackscreen onlayer black
                $ Player.AddWord(1,"interruption") #prevents interruption
                $ Girl.DailyActions.append("unseen")
                $ Girl.RecentActions.append("unseen")
                call SexAct("masturbate") # call expression Girl.Tag + "_SexAct" pass ("masturbate")
                if "angry" in Girl.RecentActions:
                        return

                #After caught masturbating. . .
                $ Girl.FaceChange("sexy",Brows="confused")
                if Girl.Mast == 1:
                        if Girl is RogueX:
                                ch_r "Ну, это было немного неожиданно. . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_r "но я бы не сказала, что неприятно. . ."
                                $ Girl.FaceChange("sexy")
                                ch_r "Но, может быть, в следующий раз сначала предупредишь?"
                        elif Girl is KittyX:
                                ch_k "Так[KittyX.like]я не ждала гостей. . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_k "хотя я и не против. . ."
                                $ Girl.FaceChange("sexy")
                                ch_k "Но, может, в следующий раз сначала постучишься?"
                        elif Girl is EmmaX:
                                ch_e "Я не ждала гостей. . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_e "хотя для тебя я могу сделать исключение. . ."
                                $ Girl.FaceChange("sexy")
                                ch_e "Но, возможно, в следующий раз ты сначала постучишься?"
                        elif Girl is LauraX:
                                ch_l "Что ты здесь делаешь? . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_l "не то чтобы я против твоей компании. . ."
                                $ Girl.FaceChange("sexy")
                                ch_l "Но, знаешь, сначала предупреждай меня."
                        elif Girl is JeanX:
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_j "Ну это было забавно. . ."
                                $ Girl.FaceChange("sexy")
                                ch_j "Так что привело тебя сюда? . ."
                        elif Girl is StormX:
                                ch_s "Это был интересный опыт. . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_s "Хотя, я уж точно не ожидала такого внимания к себе. . ."
                                $ Girl.FaceChange("sexy")
                                ch_s "Однако в следующий раз тебе стоит постучаться."
                        elif Girl is JubesX:
                                ch_v "Обычно у меня не бывает неожиданных гостей . ."
                                $ Girl.FaceChange("bemused",Eyes="side")
                                ch_v "хотя я не возражаю против компании. . ."
                                $ Girl.FaceChange("sexy")
                                ch_v "Но, может, в следующий раз сначала постучишь?"
                        elif Girl is GwenX:
                                ch_g "Я, эм. . . Я не привыкла устраивать такие представления. . ."
                                ch_g "Тебе не нужно врываться без стука в следующий раз, когда ты захочешь посмотреть."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Боюсь, ты застала меня в несколько. . . деликатном положении."
                                else:
                                    ch_b "Боюсь, ты застал меня в несколько. . . деликатном положении."
                                ch_b "У меня все-таки есть. . . потребности."
                                ch_b "Однако не так часто доводится выставлять их напоказ. . ."
                        elif Girl is DoreenX:
                                $ Girl.FaceChange("bemused",2,Eyes="side")
                                ch_d "Обычно, эм. . .  у меня не бывает зрителей. . ."
                                ch_d "Но это было не так и. . . плохо."
                                $ Girl.FaceChange("smile",1)
                        elif Girl is WandaX:
                                $ Girl.FaceChange("bemused",2,Eyes="side")
                                ch_w "Обычно я. . ."
                                ch_w "-так себя не веду. . ."
                                $ Girl.FaceChange("sly",1)
                                ch_w "Это было. . . весело."
                else:
                        if Girl is RogueX:
                                ch_r "Приятно видеть тебя здесь снова, [Girl.Petname]. Похоже, это не случайность. . ."
                        elif Girl is KittyX:
                                ch_k "Похоже, у тебя появилась привычка так заходить."
                        elif Girl is EmmaX:
                                ch_e "Я заметила, что у тебя появилась привычка заглядывать ко мне."
                        elif Girl is LauraX:
                                ch_l "Ты часто бываешь рядом. . ."
                        elif Girl is JeanX:
                                ch_j "У тебя уже выработалась привычка заглядывать. . ."
                        elif Girl is StormX:
                                ch_s "Ты довольно часто сюда приходишь. . ."
                        elif Girl is JubesX:
                                ch_v "Ты часто заходишь. . ."
                        elif Girl is GwenX:
                                ch_g "Ты часто ко мне заходишь. . ."
                        elif Girl is BetsyX:
                                ch_b "Я заметила, что у тебя появилась привычка приходить без предупреждения."
                        elif Girl is DoreenX:
                                ch_d "Ты, эм. . . так и продолжаешь заходить без предупреждения. . ."
                        elif Girl is WandaX:
                                ch_w "Ты постоянно появляешься из ниоткуда. . ."

                $ Girl.ArmPose = 1
                $ Girl.OutfitChange(Changed=0)
                #end "if you entered"
        return

#end girls caught masturbating / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#start Call_For_Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Call_For_Les(Girl=0,Girl2=0,BO=[]): #rkeljsvgbdw
        #called by EventCalls if girls are lesing and Girl approves

#        if Girl not in ActiveGirls:
#                $ BO = ActiveGirls[:]
#                while BO and Girl not in ActiveGirls:
#                        if BO[0] not in Party and BO[0].Loc != bg_current and "les" in BO[0].RecentActions:
#                                # if this girl is not already the focal girl, is at the current location but not in a party,
#                                # and was queued for a les action, set her up as girl 1.
#                                $ Girl = BO[0]
#                                $ BO = [1]
#                        $ BO.remove(BO[0])
#        if Girl in ActiveGirls and not Girl2:
#                #if a Girl was either offered or produced by first loop. . .
#                $ BO = ActiveGirls[:]
#                $ BO.remove(Girl)
#                while BO:
#                        if BO[0] not in Party and BO[0].Loc != bg_current and "les" in BO[0].RecentActions:
#                                # if this girl is not already the focal girl, is at the current location but not in a party,
#                                # and was queued for a les action, set her up as girl 2.
#                                if ApprovalCheck(BO[0], 1600 - BO[0].SEXP, TabM=0):
#                                        $ Girl2 = BO[0]
#                                        $ BO = [1]
#                                else:
#                                        return 0
#                        $ BO.remove(BO[0])
#        if Girl not in ActiveGirls or Girl2 not in ActiveGirls:
#                #if either girl refuses, continue with Jumper check
#                return 0

        if not Girl2:
                return 0
        $ LesQueue = []
        show Cellphone at SpriteLoc(StageLeft)

        $ Line = 0
        "Вам звонит [Girl.Name]."
        if Girl is RogueX:
                ch_r "Привет, [Player.Name]. . . Я тут сейчас с [Girl2.Name_tvo] и. . ."
                ch_r "Ну, ты, наверное, понимаешь. . . знаешь, нам интересно,"
                if not Player.Male:
                    ch_r "Не хотела бы ты присоединиться к нам?"
                else:
                    ch_r "Не хотел бы ты присоединиться к нам?"
        elif Girl is KittyX:
                ch_k "Ох, привет, [Girl.Petname]. . . Я тут сейчас вместе с [Girl2.Name_tvo]. . ."
                ch_k "мы только что[Girl.like]вспоминали тебя."
                ch_k "Не хочешь прийти и присоединиться к нам?"
        elif Girl is EmmaX:
                ch_e "[Girl.Petname]. . . Я сейчас приятно провожу время с [Girl2.Name_tvo]. . ."
                ch_e "ну, ты, наверное, понимаешь. . . нам интересно,"
                ch_e "Не хочешь ли ты помочь нам?"
                ch_e "И не только. . ."
        elif Girl is LauraX:
                ch_l "Привет, [Player.Name]. . . Я сейчас с [Girl2.Name_tvo], и. . ."
                ch_l "Знаешь, мы сейчас ласкаем друг друга-"
                call AnyLine(Girl2,"Эй!{w=0.3}{nw}")
                ch_l ". . . так вот . . ."
                ch_l "Не хочешь тоже поучавствовать?"
        elif Girl is JeanX:
                ch_j "Ох, [Girl.Petname]. . . Я сейчас рядом с [Girl2.Name_tvo]. . ."
                ch_j "Хочешь заскочить и \"вдолбить\" в нее немного \"здравого смысла\"?"
                call AnyLine(Girl2,"Эй!{w=0.3}{nw}")
                ch_j ". . ."
        elif Girl is StormX:
                ch_s "Здравствуй, [Girl.Petname]? . . Я сейчас. . . разговаривала с [Girl2.Name_tvo]. . ."
                ch_s "Мы хорошо проводили время вдвоем, но мы поговорили и решили, что ты, возможно, захочешь присоединиться к нам?"
        elif Girl is JubesX:
                ch_v "О, привет, [Girl.Petname]. . . рядом со мной [Girl2.Name]. . ."
                ch_v "мы немного повеселились. . . слушай. . ."
                ch_v "Не хочешь присоединиться к нам?"
        elif Girl is GwenX:
                ch_g "Ох. . . [Girl.Petname]. . . так вот, эм. . ."
                ch_g "[Girl2.Name] сейчас рядом со мной. . ."
                ch_g "Мне кажется, она хочет тебя трахнуть или типа того."
                "[[неразборчивые голоса]"
                ch_g "Я сказала, как сказала, шлюшка, тактыпридешьиликак? Ладнопока!"
                hide Cellphone
                "Она сбрасывает."
                menu:
                    "Хотите сходить к ним?"
                    "Да":
                            $ Line = "yes"
                    "Нет":
                            $ Line = "no"
                            $ Player.RecentActions.append("no les")
                            jump Misplaced
                #should skip next sequence
        elif Girl is BetsyX:
                ch_b "Ох, здравствуй, [Girl.Petname]. . . тут [Girl2.Name]. . . заглянула ко мне. . ."
                ch_b "и мы неплохо проводим время вместе. . ."
                ch_b "Уверена, у нас найдется место и для тебя, придешь?"
        elif Girl is DoreenX:
                ch_d "Ох, привет. . . [Girl.Petname]. . ."
                ch_d "Я тут сейчас вместе с [Girl2.Name_tvo], и, ну. . ."
                ch_d "Мы подумали, что ты, возможно, захочешь зайти, и. . ."
                ch_d "Немного повеселиться?"
        elif Girl is WandaX:
                ch_w "Привет, [Girl.Petname], пожалуй, я должна тебя предупредить. . ."
                ch_w "[Girl2.Name] сейчас со мной, и нам. . ."
                ch_w "весело, но мы подумали, что ты, возможно, захочешь присоединиться к нам."

        while not Line and Line != "what":
                menu:
                    extend ""
                    "Конечно, сейчас подойду!":
                            $ Girl.Statup("Love", 95, 5)
                            $ Girl.Statup("Obed", 95, 3)
                            $ Girl.Statup("Inbt", 95, 2)
                            if Girl in (EmmaX,StormX):
                                call AnyLine(Girl,"Прекрасно, скоро увидимся.")
                            else:
                                call AnyLine(Girl,"Здорово. Скоро увидимся.")
                            $ Girl2.Statup("Love", 95, 5)
                            $ Girl2.Statup("Obed", 95, 3)
                            $ Girl2.Statup("Inbt", 95, 2)
                            $ Line = "yes"
                    "Нет, веселитесь.":
                            $ Girl.Statup("Love", 90, -4)
                            $ Girl.Statup("Obed", 95, 2)
                            $ Girl.Statup("Inbt", 90, -2)
                            if Girl is RogueX:
                                    ch_r "Ох. Ну, ладно. . ."
                            elif Girl is KittyX:
                                    ch_k "Оу, ну, ладно."
                            elif Girl is EmmaX:
                                    ch_e "Я восхищаюсь твоим самоконтролем. . ."
                                    $ Girl.Statup("Obed", 95, 2)
                                    ch_e "Но не здравым смыслом. . ."
                            elif Girl is LauraX:
                                    ch_l "Эм, ладно."
                            elif Girl is JeanX:
                                    ch_j "Ладно, я просто спросила."
                                    ch_j "Тогда, увидимся позже."
                            elif Girl is StormX:
                                    ch_s "Очень жаль. . ."
                            elif Girl is JubesX:
                                    ch_v "Ладно, но ты многое теряешь!"
                            elif Girl is BetsyX:
                                    ch_b "Ох, жаль."
                            elif Girl is DoreenX:
                                    ch_d "Хех, ты просто не знаешь, что мы занимаемся. . ."
                                    ch_d "Мы тут трахаемся."
                            elif Girl is WandaX:
                                    ch_w "Тебе же хуже. . ."
                            $ Girl2.Statup("Love", 90, -4)
                            $ Girl2.Statup("Obed", 95, 2)
                            $ Girl2.Statup("Inbt", 90, -2)
                            $ Player.RecentActions.append("no les")
                            "Она сбрасывает."
                            hide Cellphone
                            jump Misplaced
                    "Вы что, кино смотрите?" if Line != "what" and Girl is not JeanX:
                            $ Girl.Statup("Love", 80, 2)
                            $ Girl.Statup("Inbt", 80, 2)
                            if Girl is RogueX:
                                    ch_r "О, у нас тут настоящее представление и это не кино."
                            elif Girl is KittyX:
                                    $ Girl.Statup("Inbt", 80, 2)
                                    ch_k "Эм. . . нет. . . мы, эммм. . ."
                            elif Girl is EmmaX:
                                    $ Girl.Statup("Love", 80, 1)
                                    ch_e "О, это так мило. Но нет, конечно же, нет."
                            elif Girl is LauraX:
                                    ch_l "Ты ударился головой или что?"
                            elif Girl is StormX:
                                    ch_s "Кино? . . нет. Мы не смотрим кино."
                            elif Girl is JubesX:
                                    ch_v "Хех, нет! Мы занимаемся. . . кое-чем поинтереснее. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я думаю, ты нас недооцениваешь."
                            elif Girl is DoreenX:
                                    ch_d "Кое-чем более. . . интересным. . ."
                            elif Girl is WandaX:
                                    ch_w "Нет, мы занимаемся кое-чем более. . . эротичным. . ."

                            $ Girl2.Statup("Love", 80, 2)
                            $ Girl2.Statup("Inbt", 80, 2)
                            if Girl2 is RogueX:
                                    ch_r "Мы тут кувыркаемся, [Girl2.Petname]."
                                    ch_r "Подумала, что ты захочешь прийти."
                            elif Girl2 is KittyX:
                                    $ Girl2.Statup("Inbt", 80, 2)
                                    ch_k "Эм. . . секс."
                                    ch_k "Мы занимаемся сексом."
                                    ch_k "-я подумала, может, ты захочешь присоединиться к нам?"
                            elif Girl2 is EmmaX:
                                    ch_e "Мы занимаемся -сексом-, [Girl2.Petname]."
                                    ch_e "Ты - хочешь - присоединиться - к - нам?"
                            elif Girl2 is LauraX:
                                    ch_l "Она про секс, тупица."
                                    if Player.Male:
                                            ch_l "Мы тут \"едим\" молюсков, но хотим мяса."
                                            ch_l "Ты придешь или как?"
                                    else:
                                            ch_l "Мы тут \"едим\" молюсков."
                                            ch_l "Ты с нами или как?"
                            elif Girl2 is StormX:
                                    ch_s "Мы наслаждаемся телами друг друга."
                                    ch_s "В общем, у нас тут секс. Мы бы хотели, чтобы ты присоединился к нам."
                            elif Girl2 is JubesX:
                                    ch_v "В основном я наслаждалась ее киской."
                                    ch_v "Хочешь в этом поучавствовать?"
                            elif Girl2 is BetsyX:
                                    ch_b "Мы занимаемся -блудом,- [Girl2.Petname]."
                            elif Girl2 is DoreenX:
                                    ch_d "Мы, эм. . . трахаемся. . ."
                            elif Girl2 is WandaX:
                                    ch_w "Я вылизывала ее киску."
                            $ Line = "what"
                            #loops back through. . .

        hide Cellphone
        #if you decide to come over. . .
        if bg_current == Girl.Home:
                #swaps girls if for some reason you're in the other one's room
                $ Line = Girl
                $ Girl = Girl2
                $ Girl2 = Line
        $ Girl.Loc = Girl.Home
        $ Girl2.Loc = Girl.Home
        $ bg_current = Girl.Home
        $ Taboo= 0
        $ Girl.Taboo = 0
        $ Girl2.Taboo = 0
        $ Line = 0

        $ Girl.DrainWord("les",1,0) #removes general "les" tag from recent actions
        $ Girl2.DrainWord("les",1,0) #removes general "les" tag from recent actions

        $ Girl.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions
        $ Girl2.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions
        $ Girl.AddWord(1,0,0,0,"les "+Girl2.Tag)  #adds "les Rogue" tag to recent actions
        $ Girl2.AddWord(1,0,0,0,"les "+Girl.Tag)  #adds "les Kitty" tag to recent actions

        call Shift_Focus(Girl)
        call Set_The_Scene(0,1,0,0)
        "Когда вы приближаетесь к ее комнате, вы слышите тихие стоны изнутри и замечаете, что дверь слегка приоткрыта."
        while Line < 2:
            menu:
                extend ""
                "Вежливо постучать":
                        if Girl is RogueX:
                                ch_r "Заходи, [RogueX.Petname]!"
                        elif Girl is KittyX:
                                ch_k "О! Заходи!"
                        elif Girl is EmmaX:
                                ch_e "Не жди особого приглашения. . ."
                        elif Girl is LauraX:
                                ch_l "Входи!"
                        elif Girl is JeanX:
                                ch_j "Заходи скорее!"
                        elif Girl is StormX:
                                ch_s "Входи!"
                        elif Girl is JubesX:
                                ch_v "Ты можешь войти!"
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Заходи! [[Видишь, я же говорила, что она скоро будет!]"
                                else:
                                    ch_g "Заходи! [[Видишь, я же говорила, что он скоро будет!]"
                        elif Girl is BetsyX:
                                ch_b "Ты можешь войти!"
                                ch_b "[[она шепчет в сторону] и не только в дверь. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох, добро пожаловать!"
                        elif Girl is WandaX:
                                ch_w "Привет!"
                        $ Line = 2
                "Заглянуть внутрь" if Line != 1:
                        call Set_The_Scene
                        $ Girl.FaceChange("kiss",1,Eyes = "closed")
                        $ Girl2.FaceChange("kiss",1,Eyes = "closed")
                        $ Trigger = "lesbian"
#                        $ Trigger3 = "fondle pussy"
#                        $ Trigger4 = "fondle pussy"
                        $ Girl.Offhand = "fondle pussy"
                        $ Girl2.Offhand = "fondle pussy"
                        "Вы видите, как [Girl.Name] и [Girl2.Name], закрыв глаза, ласкают друг друга."
                        $ Line = 1
                "Тихонько войти":
                        $ Line = 2
                "Тихонько уйти":
                        "Вы оставляете девушек заниматься своими делами и уходите."
                        $ Girl.Thirst -= 30
                        $ Girl.Lust = 20
                        $ Girl2.Thirst -= 30
                        $ Girl2.Lust = 20
                        $ Girl.Statup("Love", 90, -3)
                        $ Girl2.Statup("Love", 90, -3)
                        $ renpy.pop_call()
                        $ bg_current = "bg campus"
                        $ Line = 0
                        jump Misplaced

        $ Line = 0
        $ Girl.FaceChange("sly",1)
        $ Girl2.FaceChange("sly",1)
        call Set_The_Scene(1,0,0,0)  #no clothes or trigger resets
        if Girl is RogueX:
                ch_r "Прости что мы начали без тебя."
        elif Girl is KittyX:
                ch_k "О, привет, [KittyX.Petname], нам. . . стало немного скучно."
        elif Girl is EmmaX:
                ch_e "Мы не знали, что ты придешь."
        elif Girl is LauraX:
                ch_l "Ты что, ждешь особого приглашения?"
        elif Girl is JeanX:
                ch_j "И долго ты будешь просто стоять?"
        elif Girl is StormX:
                ch_s "Так что? Ты присоединишься к нам?"
        elif Girl is JubesX:
                ch_v "Иди сюда."
        elif Girl is GwenX:
                ch_g "Чего ты ждешь?"
        elif Girl is BetsyX:
                ch_b "Боюсь, мы не дождались тебя. . ."
        elif Girl is DoreenX:
                ch_d "Мы тут, эм. . . уже немного разогрелись. . ."
        elif Girl is WandaX:
                ch_w "Быстро наверстывай упущенное. . ."

        $ Trigger = "lesbian"
#        $ Trigger3 = "fondle pussy"
#        $ Trigger4 = "fondle pussy"
        $ Girl.Offhand = "fondle pussy"
        $ Girl2.Offhand = "fondle pussy"
        $ Partner = Girl2
        call SexAct("lesbian") # call expression Girl.Tag + "_SexAct" pass ("lesbian") #call Rogue_SexAct("lesbian")
        jump Misplaced
        return

#end Call_For_Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#start girls caught lesing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Caught_Lesing(Girl=0,Girl2=0,BO=[]): #rkeljsvgbdw
        #called by room entry dialog if the girls were lesing

        $ BO = ActiveGirls[:]
        if Girl in ActiveGirls:
                $ BO.remove(Girl)
#        while BO and not Girl:
#                if BO[0] not in Party and BO[0].Loc == bg_current and "les" in BO[0].RecentActions:
#                        # if this girl is not already the focal girl, is at the current location but not in a party,
#                        # and was queued for a les action, set her up as girl 1.
#                        $ Girl = BO[0]
#                        $ BO = [1]
#                $ BO.remove(BO[0])
#        if Girl and not Girl2:
#                #if a Girl was either offered or produced by first loop. . .
#                $ BO = ActiveGirls[:]
#                $ BO.remove(Girl)
#                while BO:
#                        if BO[0] not in Party and BO[0].Loc == bg_current and "les" in BO[0].RecentActions:
#                                # if this girl is not already the focal girl, is at the current location but not in a party,
#                                # and was queued for a les action, set her up as girl 2.
#                                $ Girl2 = BO[0]
#                                $ BO = [1]
#                        $ BO.remove(BO[0])
        python:
            for BX in BO:
                #Fills Girl if needed, then girl2 if needed, then cancels out.
                if BX not in Party and BX.Loc == bg_current and "les" in BX.RecentActions:
                        # if this girl is not already the focal girl, is at the current location but not in a party,
                        # and was queued for a les action, set her up as girl 1.
                        if not Girl:
                                Girl = BX
                        elif not Girl2:
                                Girl2 = BX
                        else:
                                break
        if not Girl or not Girl2:
                return 1

        $ Girl.DrainWord("les",1,0) #removes general "les" tag from recent actions
        $ Girl2.DrainWord("les",1,0) #removes general "les" tag from recent actions

        $ Girl.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions
        $ Girl2.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions
        $ Girl.AddWord(1,0,0,0,"les "+Girl2.Tag)  #adds "les Rogue" tag to recent actions
        $ Girl2.AddWord(1,0,0,0,"les "+Girl.Tag)  #adds "les Kitty" tag to recent actions

        "Когда вы приближаетесь к ее комнате, вы слышите тихие стоны изнутри и замечаете, что дверь слегка приоткрыта."
        call Shift_Focus(Girl)
        $ Line = 0
        while not Line:
            menu:
                extend ""
                "Вежливо постучать":
                        "Вы слышите тихие стоны, за которыми следует какая-то суета. Что-то падает на пол."
                        "Через несколько секунд ожидания и звуков надевающейся одежды, [Girl.Name] подходит к двери."
                        $ Girl.FaceChange("confused",2,Eyes = "surprised",Mouth = "smile")
                        $ Girl2.FaceChange("confused",2,Eyes = "surprised",Mouth = "smile")
                        $ Trigger = 0
#                        $ Trigger3 = 0
#                        $ Trigger4 = 0
#                        $ Trigger5 = 0
                        $ Girl.Offhand = 0
                        $ Girl2.Offhand = 0
                        call Set_The_Scene
                        if Girl is RogueX:
                                ch_r "Извини за ожидание, [Girl.Petname], мы, эм. . . тренировались."
                        elif Girl is KittyX:
                                ch_k "О, [Girl.Petname], привет, мы тут. . . неважно."
                        elif Girl is EmmaX:
                                ch_e "Что ж, надеюсь, у тебя есть веская причина прерывать нас."
                                ch_e "Я учила ее. . . кое-каким вещам. . ."
                        elif Girl is LauraX:
                                ch_l "Эм, привет [LauraX.Petname], мы, вообще-то, были немного заняты."
                        elif Girl is JeanX:
                                ch_j "Привет, [Girl.Petname], [Girl2.Name] училась работать язычком."
                        elif Girl is StormX:
                                ch_s "Ах, здравствуй, [Girl.Petname]. . . мы. . . с [Girl2.Name_tvo] беседовали. . ."
                        elif Girl is JubesX:
                                ch_v "О, привет. . . Мы с [Girl2.Name_tvo] просто. . . немного развлекались."
                        elif Girl is GwenX:
                                ch_g "О, привет, этой шлюшке требовалась хорошая взбучка."
                                $ Girl.FaceChange("angry",1,Eyes = "closed",Mouth = "open")
                                ch_g "Ай!" with vpunch
                                $ Girl.FaceChange("angry",1,Eyes = "leftside",Mouth = "open")
                                ch_g "Что ты делаешь?!"
                                $ Girl.FaceChange("sly")
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Боюсь, ты застала нас в довольно деликатном положении. . ."
                                else:
                                    ch_b "Боюсь, ты застал нас в довольно деликатном положении. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох, привет. . . [Girl.Petname]. . ."
                                ch_d "Мы были немного. . . заняты. . ."
                        elif Girl is WandaX:
                                ch_w "Привет, [Girl.Petname], мы . . . занимались кое-какими делами вместе."
                        $ Girl.FaceChange("smile",1)
                        $ Girl2.FaceChange("smile",1)
                        $ Tempmod += 10
                        $ Line = 1
                "Заглянуть внутрь":
                        call Set_The_Scene
                        $ Girl.FaceChange("kiss",1,Eyes = "closed")
                        $ Girl2.FaceChange("kiss",1,Eyes = "closed")
                        $ Trigger = "lesbian"
#                        $ Trigger3 = "fondle pussy"
#                        $ Trigger4 = "fondle pussy"
                        $ Girl.Offhand = "fondle pussy"
                        $ Girl2.Offhand = "fondle pussy"
                        "Вы видите, как [Girl.Name] и [Girl2.Name], закрыв глаза, ласкают друг друга."
                "Тихонько войти":
                        call Set_The_Scene(Quiet=1)
                        $ Girl.FaceChange("kiss",1,Eyes = "closed")
                        $ Girl2.FaceChange("kiss",1,Eyes = "closed")
                        $ Trigger = "lesbian"
#                        $ Trigger3 = "fondle pussy"
#                        $ Trigger4 = "fondle pussy"
                        $ Girl.Offhand = "fondle pussy"
                        $ Girl2.Offhand = "fondle pussy"
                        $ Girl.AddWord(1,"unseen","unseen")
                        $ Girl2.AddWord(1,"unseen","unseen")
                        $ Partner = Girl2
                        $ Line = 0
                        call SexAct("lesbian") # call expression Girl.Tag + "_SexAct" pass ("lesbian") #call Rogue_SexAct("lesbian")
                        return
                "Тихонько уйти":
                        "Вы оставляете девушек заниматься своими делами и уходите."
                        $ Girl.Thirst -= 30
                        $ Girl.Lust = 20
                        $ Girl2.Thirst -= 30
                        $ Girl2.Lust = 20
                        $ renpy.pop_call()
                        jump Campus_Map
        $ Line = 0
        return

#end Girls caught lesing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start girls caught showering / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Caught_Shower(Girl=0): #rkeljsvgb
        # Modification mode
        $ play_music()
        # -----------------
        if Girl not in TotalGirls:
                return
        call Shift_Focus(Girl)

        $ Options = []
        $ Girl.AddWord(1,"showered","showered",0,0)
        call Remove_Girl("All")

        $ Girl.OutfitChange("nude")
        $ Girl.FaceChange("smile",1)

        $ Girl.Loc = "bg showerroom"
        $ Girl.Water = 1
        $ Girl.Wet = 2

        if "gonnafap" in Girl.DailyActions:
                "Когда вы подходите к душевой, вы слышите приглушенные стоны изнутри."
        else:
                "Когда вы подходите к душевой, вы слышите какие-то звуки изнутри."
        menu:
                "Что будете делать?"
                "Войти":
                    # Modification mode
                    $ sfx_door(action="open")
                    # -----------------
                    pass
                "Постучаться":
                    $ Line = "knock"
                    # Modification mode
                    $ sfx_door(action="knock")
                    # -----------------
                "Вернуться позже":
                    call Remove_Girl(Girl)
                    $ Girl.OutfitChange(6) #dresses her
                    $ Girl.DrainWord("gonnafap",0,1) #removes "gonnafap" tag from daily
                    $ Girl.Lust = 25
                    $ Girl.Thirst -= int(Girl.Thirst/2) if Girl.Thirst >= 50 else int(Girl.Thirst/4)
                    $ bg_current = "bg campus"
                    jump Misplaced

        if Line == "knock":
                #You knock
                "Вы стучите в дверь. Изнутри доносятся звуки какого-то копошения."
                if (Girl.OverNum()+Girl.ChestNum() <5) or (Girl.PantsNum() < 5 and Girl.HoseNum() < 10):
                        $ Girl.Over = "towel"
                if "gonnafap" in Girl.DailyActions:
                        #Girl caught fapping
                        "Вдруг звук воды резко прекращается."
                        "Через несколько секунд [Girl.Name] подходит к двери."
                        $ Girl.FaceChange("perplexed",2,Mouth="normal")
                        call Set_The_Scene(Dress=0)
                        # Modification mode
                        if is_playing_music(name=audio.shower_location):
                            $ play_music(name=audio.shower_location)
                        # -----------------
                        if Girl is RogueX:
                                ch_r "Извини за ожидание, [RogueX.Petname], Я. . . как раз заканчивала принимать душ."
                        elif Girl is KittyX:
                                ch_k "О, привет, [KittyX.Petname]. Я просто. . . принимала душ. Да."
                        elif Girl is EmmaX:
                                ch_e "О, здравствуй, [EmmaX.Petname]. Я. . . занималась кое-какими личными делами."
                        elif Girl is LauraX:
                                ch_l "О, привет, [LauraX.Petname]. Я просто. . . снимала стресс."
                        elif Girl is JeanX:
                                ch_j "О, [JeanX.Petname]. Я просто. . . а, неважно."
                        elif Girl is StormX:
                                ch_s "Ах, здравствуй, [Girl.Petname] . . Я. . . приводила себя в порядок."
                        elif Girl is JubesX:
                                if not Player.Male:
                                    ch_v "О, привет, [Girl.Petname]. . . Я. . . что ты слышала?"
                                else:
                                    ch_v "О, привет, [Girl.Petname]. . . Я. . . что ты слышал?"
                        elif Girl is GwenX:
                                ch_g "О, эм. . . привет. . ."
                                ch_g "Здесь не на что смотреть. . ."
                        elif Girl is BetsyX:
                                ch_b "Ох, здравствуй, [Girl.Petname], я. . . -почти- закончила. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох, привет. . . [Girl.Petname], я, эм. . . просто мылась. . ."
                        elif Girl is WandaX:
                                ch_w "Привет, [Girl.Petname], я просто. . . приводила себя в порядок. . ."
                        $ Girl.Statup("Lust", 90, 5)
                        $ Tempmod += 10
                else:
                        #girl caught showering
                        "Вы слышите шорох полотенца, через несколько секунд [Girl.Name] подходит к двери."
                        call Set_The_Scene(Dress=0)
                        # Modification mode
                        if is_playing_music(name=audio.shower_location):
                            $ play_music(name=audio.shower_location)
                        # -----------------
                        if Girl is RogueX:
                                ch_r "Извини за ожидание, [Girl.Petname], Я как раз заканчивала принимать душ."
                        elif Girl is KittyX:
                                ch_k "О, привет, [Girl.Petname]. Я[KittyX.like]принимала душ."
                        elif Girl is EmmaX:
                                ch_e "О, здравствуй, [Girl.Petname]. Я как раз закончила принимать душ."
                        elif Girl is LauraX:
                                ch_l "О, привет, [Girl.Petname]. Я как раз закончила с душем."
                        elif Girl is JeanX:
                                ch_j "О, [Girl.Petname]. Я как раз закончила с душем."
                        elif Girl is StormX:
                                ch_s "Ах, здравствуй, [Girl.Petname]. . . Я как раз закончила с душем. . ."
                        elif Girl is JubesX:
                                ch_v "О, привет, [Girl.Petname]. Я как раз закончила с душем. . ."
                        elif Girl is GwenX:
                                ch_g "О, [Girl.Petname], я вот только из душа. . ."
                        elif Girl is BetsyX:
                                ch_b "О, здравствуй, [Girl.Petname], я как раз закончила с душем. . ."
                        elif Girl is DoreenX:
                                ch_d "О, я вот только из душа, осталось еще много горячей воды!"
                        elif Girl is WandaX:
                                ch_w "Привет, [Girl.Petname], я как раз закончила с душем."
                #end "knocked"
        else:
            #You don't knock
            if "gonnafap" in Girl.DailyActions:
                    #Caught masturbating in the shower.
                    $ Girl.DrainWord("gonnafap",0,1) #removes "gonnafap" tag from daily
                    $ Girl.FaceChange("sexy",Eyes="closed")
                    $ Girl.AddWord(1,"unseen","unseen",0,0)
                    call Set_The_Scene(Dress=0)
                    # Modification mode
                    if is_playing_music(name=audio.shower_location):
                        $ play_music(name=audio.shower_location)
                    # -----------------
                    $ Count = 0
                    $ Trigger = "masturbation"
#                    $ Trigger3 = "fondle pussy"
                    $ Girl.Offhand = "fondle pussy"
                    "Вы видите, как [Girl.Name] под струями душа ласкает себя."
                    call SexAct("masturbate") # call expression Girl.Tag + "_SexAct" pass ("masturbate") #call Laura_SexAct("masturbate")
                    $ bg_current = "bg showerroom"
                    jump Misplaced

            elif D20 >= 15 and Girl is not StormX:
                    #She's just showering and naked
                    call Set_The_Scene(Dress=0)
                    # Modification mode
                    if is_playing_music(name=audio.shower_location):
                        $ play_music(name=audio.shower_location)
                    # -----------------
                    $ Girl.FaceChange("surprised", 1)
                    "Вы входите в душ и видите, как [Girl.Name] моется."
                    call Girl_First_Bottomless(Girl,1)
                    call Girl_First_Topless(Girl,1)

                    if not Player.Male and "girltalk" not in Girl.History and not ApprovalCheck(Girl, 1400):
                            pass #if you're a girl and she hasn't clocked you
                    elif not ApprovalCheck(Girl, 1200) or not Girl.SeenPussy or not Girl.SeenChest:
                            $ Girl.Brows="angry"
                            $ Girl.Over = "towel"
                            "Она хватает полотенце и прикрывается им."
                            $ Girl.FaceChange("angry", 1)
                            $ Girl.Statup("Love", 80, -5)
                    else:
                            if "exhibitionist" in Girl.Traits:
                                $ Girl.Statup("Lust", 90, 20)
                            else:
                                $ Girl.Statup("Lust", 80, 15)
                            $ Girl.Brows="confused"
                    $ Girl.Statup("Inbt", 70, 3)

                    if not Player.Male and "girltalk" not in Girl.History and not ApprovalCheck(Girl, 1400):
                            pass #if you're a girl and she hasn't clocked you
                    elif ApprovalCheck(Girl, 1400):
                            if Girl is RogueX:
                                    ch_r "О, привет."
                            elif Girl is KittyX:
                                    ch_k "Привет, [Girl.Petname]."
                            elif Girl is EmmaX:
                                    ch_e "Ох, пришел посмотреть?"
                            elif Girl is LauraX:
                                    ch_l "Привет."
                            elif Girl is JeanX:
                                    ch_j "О, [Girl.Petname]?"
                            elif Girl is JubesX:
                                    ch_v "Йо."
                            elif Girl is GwenX:
                                    ch_g "Привет, [Girl.Petname]. . ."
                            elif Girl is BetsyX:
                                    ch_b "О, здравствуй, [Girl.Petname]."
                            elif Girl is DoreenX:
                                    ch_d "О, привет!"
                            elif Girl is WandaX:
                                    ch_w "Привет, [Girl.Petname]."
                            call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                    else:
                            if Girl is RogueX:
                                    ch_r "Эй! Может, научишься сначала стучать?!"
                            elif Girl is KittyX:
                                    ch_k "Тебя[KittyX.like]не учили стучаться?"
                            elif Girl is EmmaX:
                                    ch_e "Здравствуй. Разве тебя не учили стучать перед тем, как войти?"
                            elif Girl is LauraX:
                                    ch_l "Эм, привет? Разве стучаться вредно?"
                            elif Girl is JeanX:
                                    if not Player.Male:
                                        ch_j "Забыла постучать, [JeanX.Petname]?"
                                    else:
                                        ch_j "Забыл постучать, [JeanX.Petname]?"
                            elif Girl is StormX:
                                    ch_s "Ох, здравствуй, [Girl.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Эй, может сначала стоило постучать?"
                            elif Girl is GwenX:
                                    ch_g "Разве люди в вашей вселенной не умеют стучать?"
                            elif Girl is BetsyX:
                                    ch_b "Прости, разве здесь не принято сперва стучаться. . ?"
                            elif Girl is DoreenX:
                                    ch_d "Эй! Сперва стоило постучаться!"
                            elif Girl is WandaX:
                                    ch_w "Слушай, может, сперва стоит стучаться?"
                            menu:
                                    extend ""
                                    "Извини, мне стоило сначала постучаться.":
                                            $ Girl.Statup("Love", 50, 2)
                                            if Girl is not StormX:
                                                    $ Girl.Statup("Love", 80, 4)
                                    "И пропустить все самое интересное?":
                                            $ Girl.Statup("Obed", 50, 2)
                                            if Girl is not StormX:
                                                    $ Girl.Statup("Obed", 80, 2)
                                                    $ Girl.Statup("Inbt", 60, 1)
                                    "И что бы это изменило?":
                                            if not ApprovalCheck(Girl, 500,"I"):
                                                    $ Girl.Statup("Love", 50, -3)
                                                    $ Girl.Statup("Obed", 50, 2)
                                            $ Girl.Statup("Obed", 80, 2)
                                            $ Girl.Statup("Inbt", 60, 2)
                                    "Не думаю, что тебя это особо заботит. . ." if Girl is EmmaX:
                                            $ EmmaX.Statup("Obed", 50, 2)
                                            $ EmmaX.Statup("Obed", 80, 2)
                                            $ EmmaX.Statup("Inbt", 60, 2)
                    #end caught showering naked

            else:
                    #She's done showering and in a towel
                    $ Girl.Over = "towel"
                    call Set_The_Scene(Dress=0)
                    # Modification mode
                    if is_playing_music(name=audio.shower_location):
                        $ play_music(name=audio.shower_location)
                    # -----------------
                    "Когда вы входите в душ, вы видите [Girl.Name], накидывающую на себя полотенце."
                    if not ApprovalCheck(Girl, 1100) and (not Girl.SeenPussy or not Girl.SeenChest):
                            $ Girl.FaceChange("angry",Brows="confused")
                            $ Girl.Statup("Love", 80, -5)
                    else:
                            $ Girl.FaceChange("sexy",Brows="confused")
                    $ Girl.Statup("Inbt", 50, 3)
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Ну привет, [RogueX.Petname]. Надеялась увидеть нечто большее?"
                            else:
                                ch_r "Ну привет, [RogueX.Petname]. Надеялся увидеть нечто большее?"
                    elif Girl is KittyX:
                            if not Player.Male:
                                ch_k "О, привет. Ты надеялась, что я буду гоооолой?"
                            else:
                                ch_k "О, привет. Ты надеялся, что я буду гоооолой?"
                    elif Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Ох, здравствуй, [EmmaX.Petname]. Жалеешь, что не пришла раньше?"
                            else:
                                ch_e "Ох, здравствуй, [EmmaX.Petname]. Жалеешь, что не пришел раньше?"
                    elif Girl is LauraX:
                            if not Player.Male:
                                ch_l "О, привет, [LauraX.Petname]. Пыталась зайти незамеченной?"
                            else:
                                ch_l "О, привет, [LauraX.Petname]. Пытался зайти незамеченным?"
                    elif Girl is JeanX:
                            if not Player.Male:
                                ch_j "О, [JeanX.Petname], хотела прокрасться?"
                            else:
                                ch_j "О, [JeanX.Petname], хотел прокрасться?"
                    elif Girl is StormX:
                            ch_s "Ох, здравствуй, [Girl.Petname]."
                    elif Girl is JubesX:
                            ch_v "Ты ведешь себя подозрительно. . ."
                    elif Girl is GwenX:
                            if not Player.Male:
                                ch_g "Ты появилась из ниоткуда!"
                            else:
                                ch_g "Ты появился из ниоткуда!"
                    elif Girl is BetsyX:
                            if not Player.Male:
                                ch_b "Ох! Здравствуй, [Girl.Petname], ты застала меня врасплох. . ."
                            else:
                                ch_b "Ох! Здравствуй, [Girl.Petname], ты застал меня врасплох. . ."
                    elif Girl is DoreenX:
                            ch_d "Ой! О, привет. . ."
                    elif Girl is WandaX:
                            ch_w "Привет, [Girl.Petname]."
                    menu:
                            extend ""
                            "Извини, мне стоило сначала постучаться.":
                                    $ Girl.Statup("Love", 50, 2)
                                    if Girl is not StormX:
                                            $ Girl.Statup("Love", 80, 2)
                            "Ну, честно говоря, я. . .":
                                    $ Girl.Statup("Love", 50, -2)
                                    $ Girl.Statup("Obed", 50, 2)
                                    if Girl is not StormX:
                                            $ Girl.Statup("Obed", 80, 2)
                                            $ Girl.Statup("Inbt", 60, 1)
                                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                            "Мне нравится и нынешний твой вид. . ." if Girl is not EmmaX:
                                if ApprovalCheck(Girl, 500,"I"):
                                    $ Girl.Statup("Love", 80, 1)
                                else:
                                    $ Girl.Statup("Love", 50, -1)
                                    $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.Statup("Inbt", 60, 3)
                                call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                            "Не думаю, что тебя это особо заботит. . ." if Girl is EmmaX:
                                $ EmmaX.Statup("Obed", 50, 2)
                                $ EmmaX.Statup("Obed", 80, 2)
                                $ EmmaX.Statup("Inbt", 60, 2)
                    #end caught in towel

            $ Girl.FaceChange("sexy")
            if not Player.Male and "girltalk" not in Girl.History and not ApprovalCheck(Girl, 1400):
                    pass
            elif Girl is StormX:
                            ch_s "Ох, ничего страшного, [Girl.Petname]."
                            ch_s "Но с другими девушками тебе лучше быть поосторожнее."
            elif not ApprovalCheck(Girl, 1000) or not Girl.SeenPussy or not Girl.SeenChest:
                    if Girl is RogueX:
                            ch_r "Ну, бывает, просто будь осторожнее в следующий раз."
                    elif Girl is KittyX:
                            ch_k "Ну, не то, чтобы я совсем против. . ."
                    elif Girl is EmmaX:
                            ch_e "Хммм, да, неплохое оправдание."
                    elif Girl is LauraX:
                            ch_l "Ну, просто следи за своими собственными частями тела."
                            ch_l "Я не хотела бы, чтобы они пропали."
                    elif Girl is JeanX:
                            ch_j "Ну, просто. .  . будь осторожнее."
                    elif Girl is JubesX:
                            ch_v "В следующий раз предупреждай."
                    elif Girl is GwenX:
                            ch_g "Ага, ладно. . ."
                    elif Girl is BetsyX:
                            ch_b "Прошу, в следующий раз предупреждай."
                    elif Girl is DoreenX:
                            ch_d "Ага, только. . . стучись в следующий раз."
                    elif Girl is WandaX:
                            ch_w "Ага, все нормально, но никогда не знаешь, что можешь встретить за дверью."
            elif not ApprovalCheck(Girl, 1300):
                    if Girl is RogueX:
                            ch_r "Ну, бывает, просто будь осторожнее в следующий раз."
                    elif Girl is KittyX:
                            ch_k "Очень жаль."
                    elif Girl is EmmaX:
                            ch_e "Хммм, да, неплохое оправдание."
                    elif Girl is LauraX:
                            ch_l "Угу."
                    elif Girl is JeanX:
                            ch_j "Конечно. . ."
                    elif Girl is JubesX:
                            ch_v "Угум. . ."
                    elif Girl is GwenX:
                            ch_g "Лааадно. . ."
                    elif Girl is BetsyX:
                            ch_b "Прошу, в следующий раз будь внимательней."
                    elif Girl is DoreenX:
                            ch_d "Ага, ладно. . ."
                    elif Girl is WandaX:
                            ch_w "Все нормально."
            else:
                    if Girl is RogueX:
                            ch_r "Можно было просто попросить, [Girl.Petname]."
                    elif Girl is KittyX:
                            ch_k "Ну, это не значит, что я совсем против. . ."
                    elif Girl is EmmaX:
                            ch_e "Ну, не то чтобы я возражала. . ."
                    elif Girl is LauraX:
                            ch_l "Нет, я не против. . ."
                    elif Girl is JeanX:
                            ch_j "Как я могу устоять перед публикой?"
                    elif Girl is JubesX:
                            ch_v "В следующий раз предупреждай."
                    elif Girl is JubesX:
                            ch_v "Тебе просто нужно попросить. . ."
                    elif Girl is GwenX:
                            ch_g "Ты всегда можешь просто вежливо попросить. . ."
                    elif Girl is BetsyX:
                            ch_b "Можно было просто попросить. . ."
                    elif Girl is DoreenX:
                            ch_d "Хехе."
                    elif Girl is WandaX:
                            ch_w "Конечно."

                    if Girl.Over == "towel":
                            #if she's wearing a towel. . .
                            $ Girl.Over = 0 #removes towel
                            pause 0.5
                            $ Girl.Over = "towel"
                            "Она быстро показывает вам кое-что интересное."
                            $ Girl.Over = "towel"
                            call Girl_First_Bottomless(Girl,1)
                            call Girl_First_Topless(Girl,1) #same as "call Girl_First_Topless(RogueX,1)"

                            if Girl is LauraX:
                                    ch_l "Heh!"

            #end didn't knock

        if Girl is RogueX:
                ch_r "Ну, мне, наверное, пора идти. . ."
        elif Girl is KittyX:
                ch_k "Я уже закончила, увидимся позже?"
        elif Girl is EmmaX:
                ch_e "Полагаю, мне пора уходить. . ."
        elif Girl is LauraX:
                ch_l "Мне пора идти. . ."
        elif Girl is JeanX:
                ch_j "Ладно, я пошла."
        elif Girl is StormX:
                ch_s "Ладно, я закончила, [Girl.Petname]."
        elif Girl is JubesX:
                ch_v "Нууу, я закончила. . ."
        elif Girl is GwenX:
                ch_g "В общем, я пошла."
        elif Girl is BetsyX:
                ch_b "Боюсь, мне пора идти. . ."
        elif Girl is DoreenX:
                ch_d "Мне пора идти."
        elif Girl is WandaX:
                ch_w "Ладно, мне пора."
        menu:
            extend ""
            "Конечно, увидимся.":
                    call Remove_Girl(Girl)
            "Подожди, не могла бы ты ненадолго задержаться?":
                if ApprovalCheck(Girl, 900) or Girl is StormX:
                    if Girl is RogueX:
                            ch_r "Конечно, что такое?"
                    elif Girl is KittyX:
                            ch_k "Да?"
                    elif Girl is EmmaX:
                            ch_e "Ну хорошо, чего ты хочешь?"
                    elif Girl is LauraX:
                            $ LauraX.Loc = "bg showerroom"
                            ch_l "А? Ладно, что случилось?"
                    elif Girl is JeanX:
                            ch_j "Что? Зачем?"
                    elif Girl is StormX:
                            ch_s "Пожалуй, что могу, тебе что-то нужно?"
                    elif Girl is JubesX:
                            ch_v "А? Зачем?"
                    elif Girl is GwenX:
                            ch_g "А? Для чего?"
                    elif Girl is BetsyX:
                            ch_b "Пожалуй, я могу выделить тебе немного времени."
                    elif Girl is DoreenX:
                            ch_d "Конечно, что-то хочешь мне сказать?"
                    elif Girl is WandaX:
                            ch_w "М? Что-то случилось?"
                else:

                    if Girl is RogueX:
                            ch_r "Эм, если честно, мне не комфортно стоять рядом с тобой в таком виде, я чувствую себя слишком. . . уязвимой?"
                            ch_r "В общем, увидимся позже."
                    elif Girl is KittyX:
                            ch_k "Когда я[KittyX.like]почти голая?"
                            ch_k "В общем, я ухожу."
                    elif Girl is EmmaX:
                            ch_e "Мне не стоит \"расхаживать\" в таком виде."
                            ch_e "Поговорим позже."
                    elif Girl is LauraX:
                            ch_l "Пожалуй, мне не стоит задерживаться нигде в таком виде."
                            ch_l "Поговорим позже."
                    elif Girl is JeanX:
                            ch_j "Я бы не хотела."
                    elif Girl is JubesX:
                            ch_v "Эм. . . нет. . ."
                    elif Girl is GwenX:
                            ch_g "Может быть, позже, когда на мне будет больше одежды?"
                    elif Girl is BetsyX:
                            ch_b "Возможно, позже, при. . . других обстоятельствах?"
                    elif Girl is DoreenX:
                            ch_d "Хм, может, как-нибудь в другой раз?"
                    elif Girl is WandaX:
                            ch_w "Эм, как-нибудь в другой раз, [Girl.Petname]."
                    call Remove_Girl(Girl)

        if Line == "leaving":
                $ Girl.OutfitChange(6)
        $ Line = 0
        return 0
# End Girl Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




#start girls sunbathing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Pool_Sunbathe(Girl=0,Type=0,Mod=0,Loop=0): #rkeljsvgbdw
    # This gets called with a character name, and checks
    # Line tends to carry the current agreement state, Type tends to carry the item being discussed
    # mod is a modifier, base 0, but +200 if asking for no bottoms

    menu:
        "С кем?"
        "С [RogueX.Name_tvo]" if bg_current == RogueX.Loc:
                $ Girl = RogueX
        "С [KittyX.Name_tvo]" if bg_current == KittyX.Loc:
                $ Girl = KittyX
        "С [EmmaX.Name_tvo]" if bg_current == EmmaX.Loc:
                $ Girl = EmmaX
        "С [LauraX.Name_tvo]" if bg_current == LauraX.Loc:
                $ Girl = LauraX
        "С [JeanX.Name_tvo]" if bg_current == JeanX.Loc:
                $ Girl = JeanX
        "С [StormX.Name_tvo]" if bg_current == StormX.Loc:
                $ Girl = StormX
        "С [JubesX.Name_tvo]" if bg_current == JubesX.Loc:
                $ Girl = JubesX
        "С [GwenX.Name_tvo]" if bg_current == GwenX.Loc:
                $ Girl = GwenX
        "С [BetsyX.Name_tvo]" if bg_current == BetsyX.Loc:
                $ Girl = BetsyX
        "С [DoreenX.Name_tvo]" if bg_current == DoreenX.Loc:
                $ Girl = DoreenX
        "С [WandaX.Name_tvo]" if bg_current == WandaX.Loc:
                $ Girl = WandaX
        "Неважно.":
                return

    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
            ch_p "Слушай, [Girl.Name], почему бы тебе просто немного не расслабиться?"
            ch_p "Думаю, ты не хочешь получить неравномерный загар, почему бы тебе. . ."
            ch_p ". . . не скинуть что-нибудь?"
    else:
            ch_p "Ты уверена, что не хочешь. . ?"

label Pool_Sunbathe2:
    if Time_Count >= 2: #night/evening time
            $ Girl.FaceChange("confused")
            call AnyLine(Girl,"Немного поздновато для этого. . .")
            $ Girl.FaceChange("normal")
            return
    if not Girl.ClothingCheck():
            #if she's already nude. . .
            $ Girl.FaceChange("sly")
            call AnyLine(Girl,"Немного поздно для этого.")
            return
    if "no tan" in Girl.RecentActions:
            $ Girl.FaceChange("angry")
            call AnyLine(Girl,"Я уже сказала тебе \"нет.\"")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return
    elif "no tan" in Girl.DailyActions :
            $ Girl.FaceChange("angry")
            call AnyLine(Girl,"Не сегодня.")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return

    if Girl is EmmaX:
            if "classcaught" not in EmmaX.History:
                        $ Girl.FaceChange("angry",2)
                        ch_e "Это было бы совершенно неуместно."
                        return
            if "taboo" not in EmmaX.History:
                        $ Girl.FaceChange("bemused",2)
                        ch_e "[EmmaX.Petname], нельзя, чтобы нас видели в таком виде на людях. . ."
                        return
            if "three" not in EmmaX.History:
                if not AloneCheck(EmmaX):
                        $ Girl.FaceChange("bemused",2)
                        ch_e "Уж точно не в такой компании. . ."
                        return

    if not Girl.Over and not Girl.Chest and not Girl.Legs and not Girl.Panties and (not Girl.Acc or Girl is not JubesX): #jubilee could have a coat without that last bit
            #if she's already nude. . .
            $ Girl.FaceChange("sly")
            if Girl is RogueX:
                    ch_r "Не думаю, что сейчас с ним будут проблемы, [RogueX.Petname]."
            elif Girl is KittyX:
                    ch_k "Я уже опередила тебя."
            elif Girl is EmmaX:
                    ch_e "Я подготовилась заранее."
            elif Girl is LauraX:
                    ch_l "Ага."
            elif Girl is JeanX:
                    ch_j "Видишь, я уже об этом позаботилась. . ."
            elif Girl is StormX:
                    ch_s "Я не могу раздеться еще больше. . ."
            elif Girl is JubesX:
                    ch_v "Я уже абсолютно голая. . ."
            elif Girl is GwenX:
                    ch_g "Ну и что, по-твоему, я уже сделала?"
            elif Girl is BetsyX:
                    ch_b "Ужас. . . не видишь, что я уже полностью обнажена?"
            elif Girl is DoreenX:
                    ch_d "Я не могу раздеться больше, чем сейчас."
                    if DoreenX.Tail:
                            ch_d "Понимаешь, хвост не открепить. . ."
            elif Girl is WandaX:
                    ch_w "Ты что, не видишь, в каком я сейчас виде?"
            $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions
            # Modification mode
            $ Girl.skin_image.change_skin(skin_name="tan")
            # -----------------
            return

    $ Line = 0
    while True:
            #loops until you return
            if not Line:
                #only asks questions if there's not a play on the table.
                menu:
                    extend ""
                    "снимешь все?" if (Girl.Over or Girl.Chest) and (Girl.Legs or Girl.Panties or Girl.Hose):
                            if Girl.Over == "towel" and not Girl.Legs and not Girl.Hose and not Girl.Panties:
                                $ Type = "no panties"
                            elif (Girl.Legs or Girl.Hose) and not Girl.Panties:
                                $ Type = "no panties"
                            elif Girl.Over and not Girl.Chest:
                                $ Type = "no bra"
                            else:
                                $ Type = "both"
                            $ Mod = 200

                    "оголишься по пояс?" if Girl.Chest and not Girl.Over:
                            $ Type = "bra"

                    "может, снимешь куртку?" if Girl.Acc and Girl is JubesX:
                            if Girl.Acc == "shut jacket" and not Girl.Legs and not Girl.Hose and not Girl.Panties:
                                $ Type = "no panties"
                            elif Girl.Acc == "shut jacket" and not Girl.Over and not Girl.Chest:
                                $ Type = "no bra"
                            else:
                                $ Type = "jacket"

                    "может, снимешь [get_clothing_name(Girl.Over_key, vin)]?" if Girl.Over:
                            if Girl.Over == "towel" and not Girl.Legs and not Girl.Hose and not Girl.Panties:
                                $ Type = "no panties"
                            elif not Girl.Chest:
                                $ Type = "no bra"
                            else:
                                $ Type = "over"

                    "может, снимешь [get_clothing_name(Girl.Legs_key, vin)]?" if Girl.Legs:
                            if not Girl.Panties:
                                $ Type = "no panties"
                            else:
                                $ Type = "legs"

                    "может, снимешь [get_clothing_name(Girl.Hose_key, vin)]?" if Girl.Hose and not Girl.Legs:
                            if not Girl.Panties:
                                $ Type = "no panties"
                            else:
                                $ Type = "legs"

                    "может, снимешь [get_clothing_name(Girl.Panties_key, vin)]?" if Girl.Panties:
                                $ Type = "panties"
                                $ Mod = 200

                    "Неважно.":
                            return
            # end menu

            if Type == "no panties":
                    $ Mod = 200
                    $ Girl.FaceChange("bemused",1)
                    call AnyLine(Girl,"На мне нет трусиков. . .")
            elif Type == "no bra":
                    $ Girl.FaceChange("bemused",1)
                    call AnyLine(Girl,"На мне нет лифчика. . .")

            if (Girl.SeenPussy and Girl.SeenChest) and AloneCheck():
                    $ Mod -= 100         #makes it easier if you've already seen her
            if not Player.Male and "girltalk" not in Girl.History and not ApprovalCheck(Girl, 1400) and AloneCheck():
                    $ Mod -= 100         #makes it easier if you're a girl and she hasn't clocked you.

            # This is the primary check to see whether she's into it.
            if "exhibitionist" in Girl.Traits:
                    #if she's an exhibitionist
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 700+Mod, "I"):
                    #if she's generally slutty
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 1400+Mod) or (Girl is StormX and StormX in Rules):
                    # if she really likes you.
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 900):
                    # if she is fairly casual, not not enough
                    $ Line = "sorry"
            else:
                    # if she refuses
                    $ Line = "no"

            if Type == "no bra" or Type == "no panties":
                    #checks to see if she'd lose her jacket/pants if nothing on under
                    menu:
                        extend ""
                        "И что?":
                            if Line == "sure":
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Inbt", 70, 1)

                                    $ Girl.FaceChange("sly",1)
                                    if Girl is RogueX:
                                            ch_r "Хмм, и правда. . ."
                                    elif Girl is KittyX:
                                            ch_k "\"И что\". . . Я не знаю. . ."
                                    elif Girl is EmmaX:
                                            if not Player.Male:
                                                ch_e "\"И что\". . . тебе повезло, что ты такая милая. . ."
                                            else:
                                                ch_e "\"И что\". . . тебе повезло, что ты такой милый. . ."
                                    elif Girl is LauraX:
                                            ch_l "Я не знаю. . ."
                                    elif Girl is JeanX:
                                            ch_j "И правда."
                                    elif Girl is StormX:
                                            ch_s "Просто предупреждаю. . ."
                                    elif Girl is JubesX:
                                            ch_v "Ну. . . ладно. . ."
                                    elif Girl is GwenX:
                                            ch_g ". . ."
                                            ch_g "Ага!"
                                    elif Girl is BetsyX:
                                            ch_b "Справедливое замечание. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ох, эм. . . ну ладно. . ."
                                    elif Girl is WandaX:
                                            ch_w "Да ничего."
                            else:
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Love", 70, -1)
                                        $ Girl.Statup("Obed", 80, 1)

                                    $ Girl.FaceChange("angry",2)
                                    if Girl is RogueX:
                                            ch_r "\"И что\". . . больше ты ничего не получишь. . . пока. . ."
                                    elif Girl is KittyX:
                                            ch_k "\"И что\". . . Вот что!"
                                    elif Girl is EmmaX:
                                            ch_e "\"И что\". . . не искушай судьбу. . ."
                                    elif Girl is LauraX:
                                            ch_l "\"И что\". . . больше ты ничего не получишь."
                                    elif Girl is JeanX:
                                            $ Girl.FaceChange("bemused",1)
                                            ch_j "\"И что\". . . я не хочу."
                                    elif Girl is StormX:
                                            ch_s "\"И что\". . . Я бы предпочла оставить это на себе."
                                    elif Girl is JubesX:
                                            ch_v "Нууу, я оставлю это на себе."
                                    elif Girl is GwenX:
                                            if not Player.Male:
                                                ch_g "Ха, извините, госпожа Извращенка."
                                            else:
                                                ch_g "Ха, извините, мистер Извращенец."
                                    elif Girl is BetsyX:
                                            if not Player.Male:
                                                ch_b "Ха, идиотка. . ."
                                            else:
                                                ch_b "Ха, идиот. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ну- Я еще не готова к этому!"
                                    elif Girl is WandaX:
                                            ch_w "Хех, хорошая попытка."
                        "Все равно снимай.":
                            if Line == "sure" or (Line == "sorry" and Girl is not StormX and ApprovalCheck(Girl, 600+Mod, "O")):
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Obed", 50, 1)
                                        $ Girl.Statup("Obed", 80, 2)
                                    if Line != "sure":
                                            $ Girl.FaceChange("sad",2)
                                    else:
                                            $ Girl.FaceChange("normal",1)
                                    if Girl is RogueX:
                                            ch_r "Ну, ладно. . ."
                                    elif Girl is KittyX:
                                            ch_k "Ага, ладно. . ."
                                    elif Girl is EmmaX:
                                            ch_e "Если ты настаиваешь. . ."
                                    elif Girl is LauraX:
                                            ch_l "Хорошо."
                                    elif Girl is JeanX:
                                            ch_j ". . . ладно."
                                    elif Girl is StormX:
                                            $ Girl.Statup("Love", 80, -2)
                                            ch_s ". . . хорошо. . ."
                                    elif Girl is JubesX:
                                            ch_v "Как скажешь. . ."
                                    elif Girl is GwenX:
                                            if not Player.Male:
                                                ch_g "Ооо, ты такая требовательная. . ."
                                            else:
                                                ch_g "Ооо, ты такой требовательный. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Конечно. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Эм. . . ладно."
                                    elif Girl is WandaX:
                                            ch_w "Конечно. . ."
                                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

                                    $ Line = "sure"
                            else:
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Love", 80, -2)
                                        $ Girl.Statup("Obed", 80, -1)
                                        $ Girl.Statup("Inbt", 60, 1)

                                    $ Girl.FaceChange("angry",1)
                                    if Girl is RogueX:
                                            ch_r "Мне не нравится твой тон. . ."
                                    elif Girl is KittyX:
                                            ch_k "Как насчёт \"нет\". . ?"
                                    elif Girl is EmmaX:
                                            ch_e "Не когда ты говоришь со мной в таком тоне. . ."
                                    elif Girl is LauraX:
                                            ch_l "Не дави на меня."
                                    elif Girl is JeanX:
                                            $ Girl.FaceChange("bemused",1)
                                            ch_j "Ха! Нет."
                                    elif Girl is StormX:
                                            $ Girl.Statup("Love", 80, -2)
                                            ch_s "Ты слишком много себе позволяешь."
                                    elif Girl is JubesX:
                                            ch_v "Неа."
                                    elif Girl is GwenX:
                                            ch_g "Ха, мечтай!"
                                    elif Girl is BetsyX:
                                            ch_b "Пожалуй, тебе лучше передумать. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ну уж нет!"
                                    elif Girl is WandaX:
                                            ch_w "Хех, хорошая попытка."
                                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

                                    $ Girl.AddWord(1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions
                                    return
                        "Ты очень сексуальная.":
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Love", 80, 1)
                                        $ Girl.Statup("Obed", 70, 2)
                                        $ Girl.Statup("Inbt", 60, 1)
                                        $ Girl.Statup("Inbt", 80, 1)

                                    $ Girl.FaceChange("sly",1)
                                    if Girl is RogueX:
                                            if not Player.Male:
                                                ch_r "Хах, ты такая милая. . ."
                                            else:
                                                ch_r "Хах, ты такой милый. . ."
                                    elif Girl is KittyX:
                                            ch_k "Хихи . ."
                                    elif Girl is EmmaX:
                                            ch_e "Как мило. . ."
                                    elif Girl is LauraX:
                                            ch_l "И правда."
                                    elif Girl is JeanX:
                                            ch_j "Хорошо, что ты это понимаешь."
                                    elif Girl is StormX:
                                            ch_s ". . . Пожалуй, это так."
                                    elif Girl is JubesX:
                                            ch_v "Хех. . ."
                                    elif Girl is GwenX:
                                            ch_g "Хорошо, что ты это понимаешь. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Конечно."
                                    elif Girl is DoreenX:
                                            ch_d "Хехе."
                                    elif Girl is WandaX:
                                            ch_w "Пускаешь мне дым в глаза?"
                                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

                        "Ладно, все хорошо.":
                            if Line == "sure":
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Love", 80, 2)
                                        $ Girl.Statup("Obed", 80, 1)
                                        $ Girl.Statup("Inbt", 60, 1)
                                        $ Girl.Statup("Inbt", 80, 1)

                                    $ Girl.FaceChange("sly",1)
                                    if Girl is RogueX:
                                            if not Player.Male:
                                                ch_r "Готова к приятному сюрпризу? . ."
                                            else:
                                                ch_r "Готов к приятному сюрпризу? . ."
                                    elif Girl is KittyX:
                                            ch_k "Ох, ты и не представляешь насколько. . ."
                                    elif Girl is EmmaX:
                                            ch_e "Больше, чем ты думаешь. . ."
                                    elif Girl is LauraX:
                                            ch_l "Но я могу быть щедрой. . ."
                                    elif Girl is JeanX:
                                            ch_j "Но. . . думаю, я могу сделать исключение. . ."
                                    elif Girl is StormX:
                                            if not Player.Male:
                                                ch_s "Но ты права насчет важности ровного загара. . ."
                                            else:
                                                ch_s "Но ты прав насчет важности ровного загара. . ."
                                    elif Girl is JubesX:
                                            ch_v "Ты даже не представляешь насколько. . ."
                                    elif Girl is GwenX:
                                            ch_g "Ха. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Пора получить хороший загар. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Может, я и не против получить. . . естественный загар. . ."
                                    elif Girl is WandaX:
                                            ch_w "Ох, да я и не возражаю."
                            else:
                                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                                        $ Girl.Statup("Love", 50, 1)
                                        $ Girl.Statup("Love", 80, 1)
                                        $ Girl.Statup("Inbt", 60, 1)

                                    $ Girl.FaceChange("smile")
                                    if Girl is RogueX:
                                            ch_r "Спасибо, [RogueX.Petname]. . ."
                                    elif Girl is KittyX:
                                            ch_k "Спасибо, [KittyX.Petname]."
                                    elif Girl is EmmaX:
                                            ch_e "Спасибо. . ."
                                    elif Girl is LauraX:
                                            ch_l "Верно."
                                    elif Girl is JeanX:
                                            ch_j "Спасибо. . ."
                                    elif Girl is StormX:
                                            ch_s "Мне жаль тебя разочаровывать."
                                    elif Girl is JubesX:
                                            ch_v "Спасибо, [JubesX.Petname]."
                                    elif Girl is GwenX:
                                            ch_g ". . ."
                                    elif Girl is BetsyX:
                                            ch_b "Благодарю. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Спасибо."
                                    elif Girl is WandaX:
                                            ch_w "Здорово."

                    if Line == "sure":
                            #she agrees
                            $ Girl.Over = 0 # removes Over
                            call Girl_First_Topless(Girl)
                            if Type == "no panties":
                                    $ Girl.Legs = 0 # removes Legs
                                    $ Girl.Hose = 0 # removes Hose
                                    call Girl_First_Bottomless(Girl)
                            $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions
                            # Modification mode
                            $ Girl.skin_image.change_skin(skin_name="tan")
                            # -----------------
                    else:
                            $ Girl.AddWord(1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions

                    $ Line = 0
            # end "nothing on under this. . ."

            if Line == "sure":
                    #She agrees. . .
                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 70, 2)
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Inbt", 70, 2)
                            $ Girl.Statup("Inbt", 90, 1)
                    $ Girl.FaceChange("sly",1)
                    if Girl is RogueX:
                            ch_r "Думаю, можно. . ."
                    elif Girl is KittyX:
                            ch_k "Наверное, можно. . ."
                    elif Girl is EmmaX:
                            ch_e "Хмммм. . ."
                    elif Girl is LauraX:
                            ch_l "Конечно."
                    elif Girl is JeanX:
                            ch_j "Ага, ладно."
                    elif Girl is StormX:
                            ch_s "Думаю, можно."
                    elif Girl is JubesX:
                            ch_v "Конечно. . ."
                    elif Girl is GwenX:
                            ch_g "Без б. . ."
                    elif Girl is BetsyX:
                            ch_b "Почему нет. . ."
                    elif Girl is DoreenX:
                            ch_d "Ну ладно."
                    elif Girl is WandaX:
                            ch_w "Конечно."

                    $ Girl.Boots = 0
                    if Type == "jacket" or Type == "both":
                        if Girl is JubesX:
                            $ Girl.Acc = 0
                    if Type == "over" or Type == "both":
                            $ Girl.Over = 0
                    if Type == "bra" or Type == "both":
                            $ Girl.Chest = 0
                    call Girl_First_Topless(Girl)

                    if Type == "legs" or Type == "both":
                            $ Girl.Legs = 0 # removes Legs
                            $ Girl.Hose = 0 # removes Hose
                    if Type == "panties" or Type == "both":
                            $ Girl.Panties = 0
                    call Girl_First_Bottomless(Girl)

                    $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions
                    # Modification mode
                    $ Girl.skin_image.change_skin(skin_name="tan")
                    # -----------------

            elif Line == "sorry" and (Type == "over" or Type == "legs" or Type == "jacket"):
                    #She agrees to just an over-layer. . .
                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Obed", 80, 1)
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.Statup("Inbt", 80, 1)
                    $ Girl.FaceChange("bemused",1)
                    if Girl is RogueX:
                            ch_r "Думаю, можно. . ."
                    elif Girl is KittyX:
                            ch_k "Наверное, можно. . ."
                    elif Girl is EmmaX:
                            ch_e "Хмммм. . ."
                    elif Girl is LauraX:
                            ch_l "Конечно."
                    elif Girl is JeanX:
                            ch_j "Конечно. . . наверное."
                    elif Girl is StormX:
                            ch_s "Думаю, можно."
                    elif Girl is JubesX:
                            ch_v "Конечно. . ."
                    elif Girl is GwenX:
                            ch_g "Конечно. . ."
                    elif Girl is BetsyX:
                            ch_b "Почему нет, что ж, начнем. . ."
                    elif Girl is DoreenX:
                            ch_d "Все хорошо."
                    elif Girl is WandaX:
                            ch_w "Конечно."

                    $ Girl.Boots = 0
                    if Type == "jacket":
                            $ Girl.Acc = 0
                    if Type == "over":
                            $ Girl.Over = 0
                    if Type == "legs":
                            $ Girl.Legs = 0
                            $ Girl.Hose = 0
                    $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions
                    # Modification mode
                    $ Girl.skin_image.change_skin(skin_name="tan")
                    # -----------------

            elif Line == "sorry":
                    #She refuses but is not offended. . .
                    if "tan" not in Girl.RecentActions and "no tan" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.Statup("Inbt", 90, 2)
                    $ Girl.FaceChange("sadside",1)
                    if Girl is RogueX:
                            ch_r "Извини, но думаю, я это переживу. . ."
                    elif Girl is KittyX:
                            ch_k "Я просто не могу. . ."
                    elif Girl is EmmaX:
                            ch_e "Это было бы совсем неуместно. . ."
                    elif Girl is LauraX:
                            ch_l "Неа. . ."
                    elif Girl is JeanX:
                            ch_j "Мне. . . и так комфортно. . ."
                    elif Girl is StormX:
                            ch_s "Мне жаль разочаровывать тебя."
                    elif Girl is JubesX:
                            ch_v "Извини. . ."
                    elif Girl is GwenX:
                            ch_g "Мне очень жаль. . ."
                    elif Girl is BetsyX:
                            ch_b "Боюсь, что нет. . ."
                    elif Girl is DoreenX:
                            ch_d "Извини."
                    elif Girl is WandaX:
                            ch_w "Хех, прости."
                    $ Girl.AddWord(1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions

            elif Line == "Нет":
                    #She is offended you even asked. . .
                    $ Girl.Statup("Love", 50, -5)
                    $ Girl.Statup("Obed", 50, 2)
                    $ Girl.Statup("Inbt", 60, 1)
                    $ Girl.FaceChange("angry",1)
                    if Girl is RogueX:
                            ch_r "Не интересует, [RogueX.Petname]. . ."
                    elif Girl is KittyX:
                            ch_k "Нет."
                    elif Girl is EmmaX:
                            ch_e "Мечтай. . ."
                    elif Girl is LauraX:
                            ch_l "Нет. . ."
                    elif Girl is JeanX:
                            ch_j "Ха!"
                    elif Girl is StormX:
                            ch_s "Боюсь, что нет, [Girl.Petname]."
                    elif Girl is JubesX:
                            ch_v "Конечно. . ."
                    elif Girl is GwenX:
                            if not Player.Male:
                                ch_g "Дура. . ."
                            else:
                                ch_g "Дурак. . ."
                    elif Girl is BetsyX:
                            if not Player.Male:
                                ch_b "Идиотка. . ."
                            else:
                                ch_b "Идиот. . ."
                    elif Girl is DoreenX:
                            ch_d "Это, эм, было довольно грубо!"
                    elif Girl is WandaX:
                            if not Player.Male:
                                ch_w "Да ладно тебе, подруга."
                            else:
                                ch_w "Да ладно тебе, друг."

                    $ Girl.AddWord(1,"no tan","no tan") #adds the "no tan" trait to recent and daily actions
                    return
            if not Girl.Chest and not Girl.Over and not Girl.Panties and not Girl.Legs and Girl.HoseNum() < 10:
                        $ Girl.OutfitChange("nude") #removes remaining clothing.
            $ Mod = 0
            $ Line = 0
            if Girl.ClothingCheck():
                "Anything else?" #loops back to menu
            else:
                if len(Present) > 1 and not Loop:
                    #swaps lead girl.
                    if Present[0] is Girl:
                        $ Girl = Present[1]
                    else:
                        $ Girl = Present[0]
                    menu:
                        "Вы хотите пригласить и [Girl.Name_vin]?"
                        "Да":
                                ch_p "А что насчет тебя, [Girl.Name]?"
                                $ Loop = 1
                                jump Pool_Sunbathe2
                        "Нет":
                                if Present[0] is Girl:
                                    $ Girl = Present[1]
                                else:
                                    $ Girl = Present[0]

                return
    return

#End girls sunbathing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#start girls skinnydip / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Pool_Skinnydip(Girl=0,Line=0,Type=0,Mod=0,Loop=0): #rkeljsvgbdw
    # This gets called with a character name, and checks
    # Line tends to carry the current agreement state, Type tends to carry the item being discussed
    # mod is a modifier, base 0, but +200 if asking for no bottoms

    menu:
        "С кем?"
        "С [RogueX.Name_tvo]" if bg_current == RogueX.Loc:
                $ Girl = RogueX
        "С [KittyX.Name_tvo]" if bg_current == KittyX.Loc:
                $ Girl = KittyX
        "С [EmmaX.Name_tvo]" if bg_current == EmmaX.Loc:
                $ Girl = EmmaX
        "С [LauraX.Name_tvo]" if bg_current == LauraX.Loc:
                $ Girl = LauraX
        "С [JeanX.Name_tvo]" if bg_current == JeanX.Loc:
                $ Girl = JeanX
        "С [StormX.Name_tvo]" if bg_current == StormX.Loc:
                $ Girl = StormX
        "С [JubesX.Name_tvo]" if bg_current == JubesX.Loc:
                $ Girl = JubesX
        "С [GwenX.Name_tvo]" if bg_current == GwenX.Loc:
                $ Girl = GwenX
        "С [BetsyX.Name_tvo]" if bg_current == BetsyX.Loc:
                $ Girl = BetsyX
        "С [DoreenX.Name_tvo]" if bg_current == DoreenX.Loc:
                $ Girl = DoreenX
        "С [WandaX.Name_tvo]" if bg_current == WandaX.Loc:
                $ Girl = WandaX
        "Неважно.":
                return

    ch_p "Слушай, [Girl.Name], почему бы нам не искупаться голышом?"
label Pool_Skinnydip2:
    if Round <= 10:
            $ Girl.FaceChange("sad")
            call AnyLine(Girl,"На это нет времени.")
            return
    elif "no dip" in Girl.RecentActions:
            $ Girl.FaceChange("angry")
            call AnyLine(Girl,"Я уже сказала тебе \"нет.\"")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return
    elif "no dip" in Girl.DailyActions:
            $ Girl.FaceChange("angry")
            call AnyLine(Girl,"Не сегодня.")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return
    elif "dip" in Girl.RecentActions:
            $ Girl.FaceChange("confused")
            call AnyLine(Girl,"Мы уже это сделали.")
            return

    if Girl is EmmaX:
            if "classcaught" not in EmmaX.History:
                    $ Girl.FaceChange("angry",2)
                    ch_e "Это было бы совершенно неуместно."
                    return
            if "taboo" not in EmmaX.History:
                    $ Girl.FaceChange("bemused",2)
                    ch_e "[EmmaX.Petname], я не хочу рисковать, нас же могут увидеть. . ."
                    return
            if "three" not in EmmaX.History:
                    if not AloneCheck(EmmaX):
                            $ Girl.FaceChange("bemused",2)
                            ch_e "Уж точно не в такой компании. . ."
                            return

    if not Girl.ClothingCheck():
            #if she's already nude. . .
            $ Girl.FaceChange("sly")
            if Girl is RogueX:
                    ch_r "Конечно, давай искупаемся."
            elif Girl is KittyX:
                    ch_k "Бомбочка!"
            elif Girl is EmmaX:
                    ch_e "Прекрасно."
            elif Girl is LauraX:
                    ch_l "Я за."
            elif Girl is JeanX:
                    ch_j "Ха, конечно."
            elif Girl is StormX:
                    ch_s "С удовольствием."
            elif Girl is JubesX:
                    ch_v "Конечно!"
            elif Girl is GwenX:
                    ch_g "Ладно!"
            elif Girl is BetsyX:
                    ch_b "Замечательно."
            elif Girl is DoreenX:
                    ch_d "Здорово!"
            elif Girl is WandaX:
                    ch_w "Конечно!"
            $ Girl.OutfitChange("nude") #removes remaining clothing.

            $ Girl.AddWord(1,"dip","dip") #adds the "dip" trait to recent and daily actions
    else:
            #if she's dressed. . .
            if Girl.SeenPussy and Girl.SeenChest:
                    $ Mod += 100
            if not Player.Male and "girltalk" not in Girl.History and AloneCheck():
                    $ Mod += 200         #makes it easier if you're a girl and she hasn't clocked you.

            if "exhibitionist" in Girl.Traits:
                    #if she's an exhibitionist
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 700-Mod, "I"):
                    #if she's generally slutty
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 1200-Mod) or (Girl is StormX and StormX in Rules):
                    # if she really likes you.
                    $ Line = "sure"
            elif ApprovalCheck(Girl, 800):
                    # if she is fairly casual, not not enough
                    $ Line = "sorry"
            else:
                    # if she refuses
                    $ Line = "no"

            if Line == "sure":
                    #She agrees. . .
                    if "dip" not in Girl.RecentActions and "no dip" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 70, 2)
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Inbt", 70, 2)
                            $ Girl.Statup("Inbt", 90, 1)
                    $ Girl.FaceChange("sly",1)
                    if Girl is RogueX:
                            ch_r "Звучит весело. . ."
                    elif Girl is KittyX:
                            ch_k "Ооох, как неприлично"
                    elif Girl is EmmaX:
                            ch_e "Как смело. . ."
                    elif Girl is LauraX:
                            ch_l "Конечно."
                    elif Girl is JeanX:
                            ch_j "Ага, ладно."
                    elif Girl is StormX:
                            ch_s "Я бы с удовольствием."
                    elif Girl is JubesX:
                            ch_v "Конечно!"
                    elif Girl is GwenX:
                            ch_g "Ладно!"
                    elif Girl is BetsyX:
                            ch_b "Замечательно."
                    elif Girl is DoreenX:
                            ch_d "Здорово!"
                    elif Girl is WandaX:
                            ch_w "Конечно!"


                    $ Girl.Acc = 0 # removes jacket or other accessories
                    $ Girl.Boots = 0 # Takes off boots
                    $ Girl.Over = 0 # removes Over
                    $ Girl.Chest = 0 # removes Bra
                    call Girl_First_Topless(Girl)

                    $ Girl.Legs = 0 # removes Legs
                    $ Girl.Hose = 0 # removes Hose
                    $ Girl.Panties = 0 # removes Panties
                    call Girl_First_Bottomless(Girl)
                    $ Girl.OutfitChange("nude") #removes remaining clothing.
                    $ Girl.AddWord(1,"dip","dip") #adds the "dip" trait to recent and daily actions

            elif Line == "sorry":
                    #She refuses but is not offended. . .
                    if "dip" not in Girl.RecentActions and "no dip" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.Statup("Inbt", 90, 2)
                    $ Girl.FaceChange("sadside",1)
                    if Girl is RogueX:
                            ch_r "Может, мы могли бы просто нормально поплавать?"
                    elif Girl is KittyX:
                            ch_k "Я так не думаю. . ."
                    elif Girl is EmmaX:
                            ch_e "Точно не здесь. . ."
                    elif Girl is LauraX:
                            ch_l "Нет. . ."
                    elif Girl is JeanX:
                            ch_j "Эм, нет, не сейчас."
                    elif Girl is StormX:
                            ch_s "Боюсь, что нет, [Girl.Petname]."
                    elif Girl is JubesX:
                            ch_v "Ага, но не прямо сейчас."
                    elif Girl is GwenX:
                            ch_g "Эм, я пас. . ."
                    elif Girl is BetsyX:
                            ch_b "Я бы предпочла не раздеваться полностью. . ."
                    elif Girl is DoreenX:
                            ch_d "Я, эм. . . Я бы хотела остаться в одежде. . ."
                    elif Girl is WandaX:
                            ch_w "Но я бы не хотела полностью раздеваться."
                    menu:
                        extend ""
                        "Ладно, тогда давай переоденемся для купания.":
                                if Girl.Swim[0]:
                                        #if she has a suit to put on. . .
                                        if "dip" not in Girl.RecentActions and "no dip" not in Girl.RecentActions:
                                                $ Girl.Statup("Love", 80, 2)
                                                $ Girl.Statup("Obed", 50, 1)
                                                $ Girl.Statup("Inbt", 60, 2)
                                        $ Girl.FaceChange("smile")
                                        if Girl is RogueX:
                                                ch_r "Спасибо, [RogueX.Petname]."
                                        elif Girl is KittyX:
                                                ch_k "Здорово."
                                        elif Girl is EmmaX:
                                                ch_e "Это было бы хорошо."
                                        elif Girl is LauraX:
                                                ch_l "Как скажешь."
                                        elif Girl is JeanX:
                                                ch_j "Ага, ладно."
                                        elif Girl is StormX:
                                                ch_s "Да, это было бы неплохо."
                                        elif Girl is JubesX:
                                                ch_v "Конечно!"
                                        elif Girl is GwenX:
                                                ch_g "Ладно!"
                                        elif Girl is BetsyX:
                                                ch_b "Замечательно."
                                        elif Girl is DoreenX:
                                                ch_d "Спасибо."
                                        elif Girl is WandaX:
                                                ch_w "Здорово."

                                        show blackscreen onlayer black
                                        "Она отходит переодеться в купальник. . ."
                                        $ Girl.OutfitChange("swimwear") # puts on her swimsuit
                                        hide blackscreen onlayer black
                                        $ Girl.AddWord(1,"no dip","no dip") #adds the "no tan" trait to recent and daily actions
                                        $ Count = 1
                                elif Girl is GwenX:
                                        ch_g "Ох, эм, а у меня нет купальника. . ."
                                        ch_g "Но мой супергеройский костюм сойдет за него!"
                                        show blackscreen onlayer black
                                        "Она отходит переодеться. . ."
                                        $ Girl.OutfitChange("casual1") # puts on her swimsuit
                                        $ Girl.Panties = 0
                                        $ Girl.Boots = 0
                                        $ Girl.Hat = 0
                                        hide blackscreen onlayer black
                                        $ Girl.AddWord(1,"no dip","no dip") #adds the "no tan" trait to recent and daily actions
                                        $ Count = 1
                                else:
                                        if not Girl.OutfitChange("swimwear"):
                                                $ Count = 0
                                if not Count:
                                    #If she has no suit. . .
                                    menu:
                                        extend ""
                                        "Тогда, может, в нижнем белье?":
                                                if Girl.ChestNum() > 2 and Girl.PantiesNum() > 2 and ApprovalCheck(Girl, 1000):
                                                        #if she mostly likes you, and is wearing decent undies. . .
                                                        pass
                                                elif Girl.ChestNum() > 1 and Girl.PantiesNum() > 1 and ApprovalCheck(Girl, 1200):
                                                        #if she mostly likes you, and is wearing scandalous undies. . .
                                                        pass
                                                else:
                                                        $ Girl.FaceChange("sly",1)
                                                        call AnyLine(Girl,"Это тоже не вариант.")
                                                        $ Girl.AddWord(1,"no dip","no dip")
                                                        return
                                                $ Girl.FaceChange("smile",1)
                                                if Girl is RogueX:
                                                        ch_r "Ладно. . ."
                                                elif Girl is KittyX:
                                                        ch_k "Блин, ладно."
                                                elif Girl is EmmaX:
                                                        ch_e "Наверное, можно. . ."
                                                elif Girl is LauraX:
                                                        ch_l "Конечно, как скажешь. . ."
                                                elif Girl is JeanX:
                                                        ch_j ". . . можно."
                                                elif Girl is StormX:
                                                        ch_s "Ох, пожалуй, можно. . ."
                                                elif Girl is JubesX:
                                                        ch_v "Думаю, да. . ."
                                                elif Girl is GwenX:
                                                        ch_g "Пойдет."
                                                elif Girl is BetsyX:
                                                        ch_b "Пожалуй, можно."
                                                elif Girl is DoreenX:
                                                        ch_d "Ну, наверное, можно."
                                                elif Girl is WandaX:
                                                        ch_w "Ага, это меня устроит."
                                        "А как насчет твоего супергеройского костюма?" if Girl is GwenX and (Girl.Over != "suit" or Girl.Legs != "suit"):
                                                ch_g "О да! Он водонепроницаемый!"
                                                show blackscreen onlayer black
                                                "Она убегает, чтобы переодеться."
                                                $ Girl.Over = "suit"
                                                $ Girl.Legs = "suit"
                                                hide blackscreen onlayer black
                                                ch_g "Ну вот и все!"
                                                return
                                        "Ладно, неважно.":
                                                call AnyLine(Girl,"Спасибо.")
                                                $ Girl.AddWord(1,"no dip","no dip")
                                                return
                                    $ Girl.Acc = 0 # removes jacket or other accessories
                                    $ Girl.Boots = 0 # Takes off boots
                                    $ Girl.Over = 0 # Takes off Over
                                    "She starts to strip down."
                                    $ Girl.Legs = 0 # Takes off Legs
                                    $ Girl.Hose = 0 # Takes off Hose
                                    "And ends up in her underwear."
                                    $ Girl.SeenPanties = 1


                        "Ладно, неважно.":
                                $ Girl.Statup("Love", 80, -1)
                                if "dip" not in Girl.RecentActions and "no dip" not in Girl.RecentActions:
                                        $ Girl.Statup("Obed", 50, 2)
                                        $ Girl.Statup("Inbt", 60, 1)
                                if Girl is RogueX:
                                        ch_r "Пфф."
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Обломщица."
                                        else:
                                            ch_k "Обломщик."
                                elif Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Ты меня разочаровала."
                                        else:
                                            ch_e "Ты меня разочаровал."
                                elif Girl is LauraX:
                                        ch_l "Ладно."
                                elif Girl is StormX:
                                        ch_s "Спасибо, [Girl.Petname]."
                                elif Girl is JubesX:
                                        ch_v "Ладно."
                                elif Girl is GwenX:
                                        ch_g "Оу, ладно."
                                elif Girl is BetsyX:
                                        ch_b "Жаль."
                                elif Girl is DoreenX:
                                        ch_d "Оу."
                                elif Girl is WandaX:
                                        ch_w "Ага."
                                $ Girl.AddWord(1,"no dip","no dip") #adds the "no tan" trait to recent and daily actions
                                return

            elif Line == "Нет":
                    #She is offended you even asked. . .
                    if Player.Male or "girltalk" in Girl.History:
                            $ Girl.Statup("Love", 50, -5)
                    if "dip" not in Girl.RecentActions and "no dip" not in Girl.RecentActions:
                        $ Girl.Statup("Obed", 50, 2)
                        $ Girl.Statup("Inbt", 60, 1)
                    $ Girl.FaceChange("angry",1)
                    if Girl is RogueX:
                            ch_r "Не интересует, [RogueX.Petname]. . ."
                    elif Girl is KittyX:
                            ch_k "Нет."
                    elif Girl is EmmaX:
                            ch_e "Мечтай. . ."
                    elif Girl is LauraX:
                            ch_l "Нет. . ."
                    elif Girl is JeanX:
                            $ Girl.FaceChange("bemused",1)
                            ch_j "Ха!"
                    elif Girl is StormX:
                            ch_s "Боюсь, что нет, [Girl.Petname]."
                    elif Girl is JubesX:
                            ch_v "Извини. . ."
                    elif Girl is GwenX:
                            if not Player.Male:
                                ch_g "Ну да, ты бы этого хотела."
                            else:
                                ch_g "Ну да, ты бы этого хотел."
                    elif Girl is BetsyX:
                            if not Player.Male:
                                ch_b "Идиотка."
                            else:
                                ch_b "Идиот."
                    elif Girl is DoreenX:
                            ch_d "Эй, ну нельзя же просить такое."
                    elif Girl is WandaX:
                            $ Girl.FaceChange("sly",1)
                            $ Girl.Statup("Love", 50, 5)
                            ch_w "Хех, хорошая попытка."
                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

                    $ Girl.AddWord(1,"no dip","no dip") #adds the "no tan" trait to recent and daily actions
                    return

    if len(Present) > 1:
        if Loop:
                #second time through,
                $ Loop = 2
                $ renpy.pop_call() #removes call to Pool_Skinnydip2
        else:
                #swaps lead girl.
                if Present[0] is Girl:
                    $ Girl = Present[1]
                else:
                    $ Girl = Present[0]
                menu:
                    "Вы хотите пригласить и [Girl.Name_tvo]?"
                    "Да":
                            ch_p "А что насчет тебя, [Girl.Name]?"
                            $ Loop = 1
                            call Pool_Skinnydip2
                            if Present[0] is Girl:
                                $ Girl = Present[1]
                            else:
                                $ Girl = Present[0]
                            #if they return, then they've refused, it continues with only the first girl
                    "Нет":
                            if Present[0] is Girl:
                                $ Girl = Present[1]
                            else:
                                $ Girl = Present[0]
    if Loop == 2 and len(Present) > 1:
            #if both girls joined in
            call ShowPool([Present[0],Present[1]]) #displays pool graphics
            $ Present[0].Water = 1
            $ Present[1].Water = 1
            $ Round -= 20 if Round >= 20 else Round
            "Вы все вместе немного поплавали."
    else:
            call ShowPool([Girl]) #displays pool graphics
            $ Girl.Water = 1
            $ Round -= 20 if Round >= 20 else Round
    "Вы немного поплавали вместе."
    hide FullPool
    call Set_The_Scene(1,0,0)

    return

#End girls skinnydip / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Pool Topless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Pool_Topless(Girl=Ch_Focus,BO=[]): #rkeljsvgbdw
        #the girl is swimming, but ends up topless temporarily
        if Girl.Loc != bg_current:
                    #if the lead girl isn't in the room for some reason. . .
                    $ BO = TotalGirls[:]
                    $ renpy.random.shuffle(BO)
                    while BO:
                            if BO[0].Loc == bg_current:
                                    call Shift_Focus(BO[0])
                                    $ BO = [1]
                            $ BO.remove(BO[0])

        $ Ch_Focus = Girl
        if (Girl.ChestNum() <= 1 and Girl.OverNum() <= 1) or Girl.Loc != bg_current:
                #if *no* girls are present, ditch or no point, already topless
                $ D20 = renpy.random.randint(1, 14)
                return
        $ Girl.Uptop = 1 #sets uptop
        "[Girl.Name] ныряет в бассейн."
        menu:
            "Похоже, с ней случился небольшой казус."
            "Эй, [Girl.Name]. . .":
                    ch_p "Похоже, у тебя верх задрался. . ."
                    $ Girl.FaceChange("confused")
                    if Girl is not StormX:
                            $ Girl.Statup("Obed", 60, 2)
                            $ Girl.Statup("Inbt", 50, -2)
                            call AnyLine(Girl,". . .")
                            $ Girl.FaceChange("surprised",2,Eyes="down")
                    $ Girl.Statup("Love", 80, 3)
                    $ Girl.Statup("Love", 90, 1)
                    $ Girl.Statup("Lust", 50, 2)
                    $ Count = 100
            "Промолчать":
                    $ Girl.FaceChange("surprised",2,Eyes="down")
                    "Через несколько секунд [Girl.Name], кажется, замечает, что ее верх задрался."
                    if ApprovalCheck(Girl, 1200):
                            $ Count = 0
                    else:
                            $ Count = -100

        if (ApprovalCheck(Girl, 800-Count,"I") or ApprovalCheck(Girl, 1600-Count) or (Girl is StormX and StormX in Rules)) and Girl is not BetsyX:
                $ Girl.FaceChange("sly")
                $ Girl.Chest = 0 #loses top
                $ Girl.Over = 0 #loses top
                $ Girl.Statup("Obed", 60, 2)
                $ Girl.Statup("Inbt", 50, 4)
                $ Girl.Statup("Inbt", 90, 2)
                $ Girl.Statup("Lust", 50, 5)
                "Она с улыбкой снимает верх через голову."
                call Girl_First_Topless(Girl)
        elif ApprovalCheck(Girl, 500-Count,"I") or ApprovalCheck(Girl, 1200-Count):
                $ Girl.FaceChange("sly",1)
                $ Girl.Statup("Obed", 60, 2)
                $ Girl.Statup("Inbt", 50, 3)
                $ Girl.Statup("Inbt", 80, 2)
                $ Girl.Statup("Lust", 50, 3)
                "Она улыбается и решает оставить все как есть."
                call Girl_First_Topless(Girl)
        else:
                if ApprovalCheck(Girl, 800-Count) or (Girl is StormX):
                        #she's ok with it
                        $ Girl.Statup("Obed", 60, 2)
                        $ Girl.Statup("Inbt", 70, 2)
                        $ Girl.Statup("Lust", 50, 1)
                        $ Girl.FaceChange("bemused",2)
                else:
                        #she's mad
                        $ Girl.Statup("Love", 70, -2)
                        $ Girl.Statup("Inbt", 50, 1)
                        $ Girl.FaceChange("angry",2)
                call Girl_First_Topless(Girl,1)
                $ Girl.Uptop = 0 #resets uptop
                "Она поправляет свой верх."
                if Count <= 0:
                        $ Girl.Statup("Love", 70, -5)
                        $ Girl.Statup("Obed", 60, -2)
                        $ Girl.Statup("Inbt", 60, 2)
                        if not Player.Male:
                            call AnyLine(Girl,"Могла бы и сказать.")
                        else:
                            call AnyLine(Girl,"Мог бы и сказать.")

        $ Count = 0
        return
# End Pool Topless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start break-up dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Breakup(Girl=0,Other=0,Anger = 0,BO=[]): #rkeljsvgbdw
        # call Breakup(RogueX) from Chat
        # Repeats is number of times you've broken up, Other is a potential other woman, Anger is a meter that ends things at 4+

        $ Girl.AddWord(1,"breakup talk","breakup talk",0,0)

        if Girl.Break[1] > 3:
                $ Girl.FaceChange("angry")
                $ Girl.Statup("Love", 50, -5, 1)
                $ Girl.Statup("Love", 80, -10, 1)
                $ Girl.Statup("Obed", 30, -5, 1)
                $ Girl.Statup("Obed", 50, -10, 1)
                $ Girl.Statup("Inbt", 50, 3)
                $ Girl.Statup("Inbt", 80, 1)
                call AnyLine(Girl,"Я уже устала от этого.")
                $ Anger -= 1
        elif Girl.Break[1]:
                $ Girl.FaceChange("surprised")
                $ Girl.Statup("Love", 50, -5, 1)
                $ Girl.Statup("Obed", 30, -5, 1)
                $ Girl.Statup("Inbt", 80, 1)
                call AnyLine(Girl,"Что, снова?")
                $ Girl.FaceChange("angry")
                $ Anger += 1
        else:
                $ Girl.FaceChange("surprised")
                call AnyLine(Girl,"Что?! Почему?")

        $ Line = 0
        menu:
            "Дело не в тебе, а во мне.":
                    $ Girl.Statup("Love", 200, -5)
                    $ Girl.Statup("Obed", 80, -5)
                    $ Girl.Statup("Inbt", 50, 3)
                    $ Girl.Statup("Inbt", 70, 1)
                    $ Girl.FaceChange("confused")

            "Я просто думаю, что нам нужно сделать перерыв.":
                    $ Girl.Statup("Love", 200, -5)
                    $ Girl.FaceChange("sad")

            "У меня появилась другая":
                    $ Anger += 1
                    $ Girl.Statup("Love", 200, -10)
                    $ Girl.Statup("Obed", 50, 3)
                    $ Girl.Statup("Obed", 80, 3)
                    $ Girl.Statup("Inbt", 50, -5)
                    $ Girl.FaceChange("angry")
                    call AnyLine(Girl,"Кто?")
                    menu:
                        extend ""
                        "[RogueX.Name]" if Girl is not RogueX:
                                $ Other = RogueX
                        "[KittyX.Name]" if Girl is not KittyX and "met" in KittyX.History:
                                $ Other = KittyX
                        "[EmmaX.Name]" if Girl is not EmmaX and "met" in EmmaX.History:
                                $ Other = EmmaX
                        "[LauraX.Name]" if Girl is not LauraX and "met" in LauraX.History:
                                $ Other = LauraX
                        "[JeanX.Name]" if Girl is not JeanX and "met" in JeanX.History:
                                $ Other = JeanX
                        "[StormX.Name]" if Girl is not StormX and "met" in StormX.History:
                                $ Other = StormX
                        "[JubesX.Name]" if Girl is not JubesX and "met" in JubesX.History:
                                $ Other = JubesX
                        "[GwenX.Name]" if Girl is not GwenX and "met" in GwenX.History:
                                $ Other = GwenX
                        "[BetsyX.Name]" if Girl is not BetsyX and "met" in BetsyX.History:
                                $ Other = BetsyX
                        "[DoreenX.Name]" if Girl is not BetsyX and "met" in DoreenX.History:
                                $ Other = DoreenX
                        "[WandaX.Name]" if Girl is not BetsyX and "met" in WandaX.History:
                                $ Other = WandaX
                        "Я не могу сказать.":
                                $ Girl.Statup("Love", 200, -5)
                                $ BO = ActiveGirls[:]
                                $ BO.remove(Girl)
                                $ Count = 0
                                while BO:
                                        if BO[0].SEXP > Count:
                                                # if you've boned this girl more than the last, she's the boss
                                                $ Other = BO[0]
                                                $ Count = BO[0].SEXP
                                        $ BO.remove(BO[0])
                                $ Count = 0
                                if not Other:
                                        call AnyLine(Girl,"Ну, у нее же должно быть имя. . .")
                                else:
                                        call AnyLine(Girl,"Это "+Other.Name+", не так ли?")
                        "Шучу.":
                                $ Girl.Statup("Love", 200, -5)
                                $ Girl.Statup("Obed", 50, 3)
                                $ Girl.FaceChange("angry")
                                if Girl is RogueX:
                                        ch_r "Слишком жестко."
                                elif Girl is KittyX:
                                        ch_k "Не смей[KittyX.like]так шутить!"
                                elif Girl is EmmaX:
                                        ch_e "Ох, не смей со мной так \"шутить\"."
                                elif Girl is LauraX:
                                        ch_l ". . ."
                                elif Girl is JeanX:
                                        ch_j "Последний раз я слышала подобную шутку от семилетки."
                                elif Girl is StormX:
                                        ch_s "Тебе не стоит \"шутить\" о таком, [Girl.Petname]."
                                elif Girl is JubesX:
                                        ch_v "Ага. . ."
                                elif Girl is GwenX:
                                        ch_g "Ну конечно. . ."
                                elif Girl is BetsyX:
                                        ch_b "Американский юмор несколько туповат. . ."
                                elif Girl is DoreenX:
                                        ch_d "Это не смешно!"
                                elif Girl is WandaX:
                                        ch_w "Ого, это -нехорошая- шутка."
                                $ Girl.FaceChange("normal")
                                $ Anger += 1

            "Я просто хочу порвать с тобой.":
                    $ Girl.FaceChange("angry")
                    $ Girl.Statup("Love", 50, 3)
                    $ Girl.Statup("Love", 200, -15)
                    $ Girl.Statup("Obed", 50, 5)
                    $ Girl.Statup("Obed", 80, 5)
                    $ Girl.Statup("Obed", 200,5)
                    $ Girl.Statup("Inbt", 50, -5)
                    $ Anger += 1
        #end first question

        if not Other:
                #"denial":
                $ Girl.FaceChange("sad")
                if ApprovalCheck(Girl, 900, "O") or Girl is GwenX:
                        #high obedience
                        call AnyLine(Girl,"Если ты действительно этого хочешь. . .")
                elif ApprovalCheck(Girl, 900, "L"):
                        #high love
                        call AnyLine(Girl,"Но я очень сильно тебя люблю!")
                elif ApprovalCheck(Girl, 900, "I") or Girl is JeanX:
                        #super casual
                        call AnyLine(Girl,"Если ты ко мне ничего не чувствуешь. . .")
                elif ApprovalCheck(Girl, 1500):
                        #general mix
                        call AnyLine(Girl,"Но мы так много значим друг для друга!")
                else:
                        #doesn't care too much
                        if not Player.Male:
                            call AnyLine(Girl,"Ты уверена, что точно этого хочешь?")
                        else:
                            call AnyLine(Girl,"Ты уверен, что точно этого хочешь?")
                $ Line = "bargaining"

        else:
            #if there's another girl. . .
            #GirlLikeCheck(RogueX,KittyX) if Rogue is the girl talking and Kitty is the "other girl"
            $ Cnt = (int(Girl.GirlLikeCheck(Other)/2))-250

            if Girl.GirlLikeCheck(Other) >= 800 or Girl is GwenX:
                    $ Girl.Statup("Lust", 70, 5)
                    $ Girl.Statup("Obed", 50, 5)
                    $ Girl.Statup("Obed", 200, 5)
                    $ Girl.Statup("Inbt", 50, 1)
                    $ Girl.Statup("Inbt", 200, 5)
                    $ Girl.FaceChange(5,2) #blush2
                    call AnyLine(Girl,"Ну, по крайней мере, у тебя хороший вкус.")
                    $ Girl.FaceChange(5,1) #blush1
            elif Girl.GirlLikeCheck(Other) >= 600:
                    $ Girl.Statup("Love", 50, -5, 1)
                    $ Girl.Statup("Love", 80, -10, 1)
                    $ Girl.Statup("Obed", 50, 5)
                    $ Girl.Statup("Obed", 200, 3)
                    if Other is EmmaX and Girl is not StormX:
                            call AnyLine(Girl,"С нашим преподавателем?!")
                    if Other is StormX and Girl is not EmmaX:
                            call AnyLine(Girl,"С нашим преподавателем?!")
                    elif Girl is EmmaX and Other is not StormX:
                            ch_e "А она мне всегда нравилась. . ."
                    elif Girl is StormX and Other is EmmaX:
                            ch_s "А она казалась такой приличной. . ."
                    elif Girl in (EmmaX,StormX) and Other in (EmmaX,StormX):
                            if not Player.Male:
                                call AnyLine(Girl,"Тебе так нравятся преподаватели?")
                            else:
                                call AnyLine(Girl,"Ты падок на преподавателей?")
                    elif Girl is LauraX:
                            ch_l "Она мне вроде как нравится."
                    elif Girl is JeanX:
                            ch_j "Ну, она не совсем стерва."
                    else:
                            call AnyLine(Girl,"С моей подругой?!")
                    $ Girl.FaceChange("normal")
                    $ Anger += 1
            elif Girl.GirlLikeCheck(Other) >= 400:
                    $ Girl.Statup("Love", 50, -3, 1)
                    $ Girl.Statup("Love", 80, -5, 1)
                    $ Girl.Statup("Obed", 80, 5)
                    $ Girl.Statup("Inbt", 50, 1)
                    $ Girl.Statup("Inbt", 80, 3)
                    call AnyLine(Girl,"Можно было выбрать кого-то получше.")
            else: #Girl.GirlLikeCheck(Other) < 400
                    $ Girl.Statup("Love", 50, -5, 1)
                    $ Girl.Statup("Obed", 80, 3)
                    $ Girl.Statup("Inbt", 50, 2)
                    $ Girl.Statup("Inbt", 80, 5)
                    $ Girl.FaceChange("angry")
                    call AnyLine(Girl,"С этой шлюхой?!")
                    $ Anger += 2

            if ApprovalCheck(Girl, 2000, Bonus = Cnt,Alt=[[WandaX],1500]):
                    $ Girl.Statup("Lust", 70, 5)
                    $ Girl.FaceChange("sexy")
                    call AnyLine(Girl,"Почему бы тебе не быть с нами обеими?")
                    $ Line = "threeway"
            else:
                    $ Girl.FaceChange("sad")
                    call AnyLine(Girl,"Ты предпочитаешь ее, а не меня?")
                    menu:
                        extend ""
                        "Именно так.":
                                $ Girl.Statup("Love", 50, -3, 1)
                                $ Girl.Statup("Love", 80, -5, 1)
                                $ Girl.Statup("Obed", 30, 1)
                                $ Girl.Statup("Obed", 50, 1)
                                $ Anger += 1
                                $ Line = "bargaining"
                                if Girl is RogueX:
                                        ch_r "Тогда не жди от меня никакой помощи."
                                elif Girl is KittyX:
                                        ch_k "!!!"
                                elif Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Полагаю, ты сделала свой выбор."
                                        else:
                                            ch_e "Полагаю, ты сделал свой выбор."
                                elif Girl is LauraX:
                                        ch_l "Многое теряешь."
                                elif Girl is JeanX:
                                        ch_j "Чушь."
                                elif Girl is StormX:
                                        ch_s "Хорошо, я понимаю."
                                        $ Line = "threeway"
                                elif Girl is JubesX:
                                        ch_v "Как грубо. . ."
                                elif Girl is GwenX:
                                        ch_g "Угу. . ."
                                        $ Line = "threeway"
                                elif Girl is BetsyX:
                                        ch_b "Мне довольно трудно в это поверить. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ну, я понимаю. . ."
                                        $ Line = "threeway"
                                elif Girl is WandaX:
                                        ch_w "Думаю, я тебя понимаю."
                                        $ Line = "threeway"

                        "Я хочу быть с вами обеими.":
                                $ Line = "threeway"

                        "Нет, извини, забудь.":
                                $ Girl.Statup("Love", 50, -3, 1)
                                $ Girl.Statup("Obed", 80, -5)
                                call AnyLine(Girl,"Ты не отвертишься. . .")
                                $ Line = "bargaining"
        #end "if there's another" or not

        if Line == "threeway" and Anger < 4:
                if Girl is StormX:
                        ch_s "Она не будет возражать, если ты будешь встречаться с нами обеими?"
                elif Girl is GwenX:
                        ch_g "Ну, ты всегда можешь встречаться с нами обеими, если она к этому готова. . ."
                elif Girl is DoreenX:
                        ch_d "Слушай, может быть, ты хочешь встречаться с нами обеими?"
                else:
                        call AnyLine(Girl,"А что насчет встречаться сразу с нами обеими? Что она об этом думает?")
                menu Breakup_Threeway_Offer:
                        extend ""
                        "Она сказала, что не против." if "poly "+ Girl.Tag in Other.Traits or Girl.Tag+"Yes" in Player.Traits:
                                #"poly Rogue" in KittyX.Traits, or "KittyYes" in Player.Traits
                                if ApprovalCheck(Girl, 1800, Bonus = Cnt):
                                        $ Girl.FaceChange("smile", 1)
                                        $ Girl.Statup("Lust", 70, 5)
                                        $ Girl.Statup("Obed", 50, 5)
                                        $ Girl.Statup("Obed", 80, 3)
                                        $ Girl.Statup("Inbt", 50, 3)
                                        $ Girl.Statup("Inbt", 80, 1)
                                        if Girl.GirlLikeCheck(Other) < 400:
                                                $ Girl.FaceChange("angry")
                                                if Girl is RogueX:
                                                        ch_r "Я терпеть не могу эту суку, но ради тебя готова."
                                                elif Girl is KittyX:
                                                        ch_k "Она сука! Хорошо, ради тебя я стерплю ее."
                                                elif Girl is EmmaX:
                                                        ch_e "Полагаю, из нас двоих, я буду лучшей женщиной. . ."
                                                        ch_e "Не то чтобы у меня была конкуренция."
                                                elif Girl is LauraX:
                                                        ch_l "Я не буду выпускать когти. . . ради тебя."
                                                elif Girl is JeanX:
                                                        ch_j "Хорошо. . . Думаю, я смогу найти ей какое-нибудь применение."
                                                elif Girl is StormX:
                                                        ch_s "Она мне не нравится, но я потерплю."
                                                elif Girl is JubesX:
                                                        ch_v "Нууу, это не круто. . . но я могу справиться. . ."
                                                elif Girl is GwenX:
                                                        ch_g "В последнее время мы немного ссоримся, но я могу с ней договориться. . ."
                                                elif Girl is BetsyX:
                                                        ch_b "Боюсь, в ближайшее время нам прилется как-то уживаться друг с другом. . ."
                                                elif Girl is DoreenX:
                                                        ch_d "Я думаю, у нас все получится."
                                                elif Girl is WandaX:
                                                        ch_w "Тогда и я не против."
                                        elif Girl is StormX:
                                                ch_s "Тогда это все, что мне нужно знать."
                                        elif Girl is WandaX:
                                                ch_w "Ну и отлично."
                                        elif Girl.GirlLikeCheck(Other) >= 700 or Girl is JeanX:
                                                $ Girl.FaceChange("sexy")
                                                call AnyLine(Girl,"Должна признаться, я и сама об этом думала.")
                                        elif Girl.Love >= Girl.Obed:
                                                $ Girl.FaceChange("sad")
                                                call AnyLine(Girl,"Пока мы можем быть вместе, я смогу смириться с другой.")
                                        else:
                                                #Inbt highest
                                                call AnyLine(Girl,"Если она будет с тобой, то и я тоже.")

                                        $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits
                                else:
                                        $ Anger += 2
                                        $ Girl.Statup("Love", 50, -10, 1)
                                        $ Girl.Statup("Love", 80, -15, 1)
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Obed", 80, 3)
                                        $ Girl.Statup("Inbt", 50, 5)
                                        $ Girl.Statup("Inbt", 80, 3)
                                        $ Girl.FaceChange("angry", 1)
                                        call AnyLine(Girl,"Ну, может и так, но я не хочу делить тебя с ней." )
                                        $ Line = "bargaining"
                                        if Girl is StormX:
                                                $ Line = "breakup"
                        #End "she said it'd be ok.

                        "Я понятия не имею.": #if not KittyX.Break[0]:
                                $ Line = "ask " + Other.Tag #"ask Kitty"

                        "Ей не нравится эта идея.": #if KittyX.Break[0]:
                                if Girl.GirlLikeCheck(Other) >= 700:
                                        $ Girl.Statup("Love", 200, -5)
                                elif Girl.GirlLikeCheck(Other) <= 400:
                                        $ Girl.Statup("Love", 90, 5)
                                call AnyLine(Girl,"Тогда зачем было поднимать эту тему?")


                        "Ну, даже если она не согласна. . .":
                                $ Line = "ask " + Other.Tag #"ask Kitty"
                                if Girl.GirlLikeCheck(Other) >= 700:
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 200, -5)
                                elif Girl.GirlLikeCheck(Other) <= 400:
                                        $ Girl.Statup("Love", 90, 5)

                if Line == "ask " + Other.Tag and Girl.GirlLikeCheck(Other) >= 700:
                                #if previous responses had her wanting to ask the other girl about it
                                call AnyLine(Girl,"Хочешь, я спрошу ее вместо тебя?")
                                menu:
                                    extend ""
                                    "Да, это было бы хорошо.":
                                            $ Girl.Statup("Love", 90, 5)
                                            $ Girl.Statup("Obed", 70, 1)
                                            $ Girl.Statup("Inbt", 80, 5)
                                            $ Girl.FaceChange("sexy")
                                            call AnyLine(Girl,"Думаю, я справлюсь.")
                                            $ Girl.AddWord(1,0,0,"ask "+Other.Tag,0) #adds "ask Other" to traits
                                            $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits
                                    "Нет, давай просто держать наши отношения в секрете.":
                                            $ Girl.Statup("Love", 50, -5, 1)
                                            $ Girl.Statup("Love", 80, -5, 1)
                                            $ Girl.Statup("Obed", 80, 5)
                                            $ Girl.Statup("Inbt", 50, 3)
                                            call AnyLine(Girl,"Я не уверена, что это хорошая идея. . .")

                if Line == "breakup":
                        pass
                elif Line != "bargaining" and "poly "+ Other.Tag not in Girl.Traits:
                        #if the answer is not "bargaining," but also the girl has not agreed yet. . .
                        #"poly Kitty" not in RogueX.Traits:
                        if "ask "+ Other.Tag not in Girl.Traits and not ApprovalCheck(Girl, 1800, Bonus = (int(Girl.GirlLikeCheck(Other)/2))-300):
                                #"ask Kitty" not in RogueX.Traits
                                #checks if Girl likes you more than Other
                                $ Girl.Statup("Love", 50, -5, 1)
                                $ Girl.Statup("Obed", 80, -10, 1)
                                $ Girl.Statup("Inbt", 50, 5)
                                $ Girl.FaceChange("angry", 1)
                                if not ApprovalCheck(Girl, 1800):
                                        call AnyLine(Girl,"Возможно, ты мне тоже не особо сильно нравишься.")
                                else:
                                        $ Girl.Statup("Love", 80, -10, 1)
                                        $ Girl.Statup("Obed", 50, -5, 1)
                                        if Girl is EmmaX and Other is not StormX:
                                                ch_e "Я бы предпочла не развлекаться с парнем другой преподавательницы. . ."
                                        elif Girl is EmmaX:
                                                ch_e "Я бы предпочла не развлекаться с парнем моей студентки. . ."
                                        elif Girl is StormX:
                                                ch_s "Я бы предпочла в это не влезать."
                                        elif Girl is JeanX:
                                                ch_j "Не знаю, она немного скучновата. . ."
                                        elif Girl is BetsyX:
                                                ch_b "Я бы не хотела быть чьей-то любовницей. . ."
                                        elif Other is EmmaX:
                                                if not Player.Male:
                                                    call AnyLine(Girl,"Я не хочу, чтобы меня застукали с девушкой преподавателя!")
                                                else:
                                                    call AnyLine(Girl,"Я не хочу, чтобы меня застукали с парнем преподавателя!")
                                        else:
                                                call AnyLine(Girl,"Мне это не очень нравится, "+Other.Name+", как-никак, моя подруга." )
                                $ Anger += 1
                                if Girl is not StormX:
                                        $ Line = "bargaining"
                        else:
                                #if she agrees to polygamy
                                $ Girl.Statup("Obed", 30, 5)
                                $ Girl.Statup("Obed", 50, 3)
                                $ Girl.Statup("Inbt", 50, 5)
                                $ Girl.Statup("Inbt", 80, 1)
                                $ Girl.FaceChange("sad")
                                if Girl.GirlLikeCheck(Other) < 400:
                                        $ Girl.FaceChange("angry")
                                        if Girl is RogueX:
                                                ch_r "Я терпеть не могу эту суку, но ради тебя готова."
                                        elif Girl is KittyX:
                                                ch_k "Она сука! Хорошо, ради тебя я стерплю ее."
                                        elif Girl is EmmaX:
                                                ch_e "Полагаю, из нас двоих, я буду лучшей женщиной. . ."
                                                ch_e "Не то чтобы у меня была конкуренция."
                                        elif Girl is LauraX:
                                                ch_l "Я не буду выпускать когти. . . ради тебя."
                                        elif Girl is JeanX:
                                                ch_j "Хорошо. . . Думаю, я смогу найти ей какое-нибудь применение."
                                        elif Girl is StormX:
                                                ch_s "Она мне не нравится, но я потерплю."
                                        elif Girl is JubesX:
                                                ch_v "Нууу, это не круто. . . но я могу справиться. . ."
                                        elif Girl is GwenX:
                                                ch_g "В последнее время мы немного ссоримся, но я могу с ней договориться. . ."
                                        elif Girl is BetsyX:
                                                ch_b "Делить тебя с другой женщиной. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Думаю, моногамия переоценена."
                                        elif Girl is WandaX:
                                                ch_w "Думаю, это нормально."
                                elif Girl.GirlLikeCheck(Other) >= 700:
                                        $ Girl.FaceChange("sexy")
                                        call AnyLine(Girl,"Должна признаться, я и сама об этом думала.")
                                elif Girl.Love >= Girl.Obed:
                                        #RogueX.Love >= RogueX.Obed:
                                        $ Girl.FaceChange("sad")
                                        call AnyLine(Girl,"Пока мы можем быть вместе, я смогу смириться с другой.")
                                else:
                                        #Inbt highest
                                        call AnyLine(Girl,"Если она будет с тобой, то и я тоже")
                                $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0) #adds "poly Other" to traits
                                if "ask "+ Other.Tag in Girl.Traits:
                                        #"ask Kitty" in RogueX.Traits:
                                        call AnyLine(Girl,"Я поговорю с "+Other.Name_tvo+" об этом.")
                                else:
                                        $ Girl.FaceChange("sad")
                                        $ Girl.AddWord(1,0,0,"downlow",0) #adds "downlow" to traits
                                        if Girl is RogueX:
                                                ch_r "Думаю, мы должны держать наши отношения в секрете, по крайней мере пока."
                                        elif Girl is KittyX:
                                                ch_k "Ооох, это будет наш маленький секрет. . ."
                                        elif Girl is EmmaX:
                                                ch_e "Полагаю, я смогу быть осторожной."
                                        elif Girl is LauraX:
                                                ch_l "Я умею хранить секреты."
                                        elif Girl is JeanX:
                                                ch_j "Конечно, давай так и сделаем."
                                        elif Girl is StormX:
                                                ch_s "Я умею хранить свои секреты."
                                        elif Girl is JubesX:
                                                ch_v "Я могу держать себя в руках. . ."
                                        elif Girl is GwenX:
                                                ch_g "Мы можем держать это только между нами. . ."
                                        elif Girl is BetsyX:
                                                ch_b "Пожалуй, я могу разделить тебя с кем-нибудь. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Я думаю, что моногамия переоценена."
                                        elif Girl is WandaX:
                                                ch_w "Конечно."

                                        if Girl.GirlLikeCheck(Other) >= 800 and Girl is not JeanX:
                                                call AnyLine(Girl, "Пожалуйста, поговори с "+Other.Name_tvo+", чтобы нам не пришлось встречаться тайком.")
                                        elif Girl.GirlLikeCheck(Other) >= 500 and Girl is not JeanX:
                                                call AnyLine(Girl,"Если честно, мне не хочется быть на втором плане.")
                                        else:
                                                call AnyLine(Girl,"Это может быть забавно, встречаться за ее спиной.")
                #End Threeway

        if Line == "bargaining" and Anger < 4:
                $ Girl.FaceChange("sad")
                if not Player.Male:
                    call AnyLine(Girl,"Ты уверена, что я никак не могу убедить тебя остаться со мной?")
                else:
                    call AnyLine(Girl,"Ты уверен, что я никак не могу убедить тебя остаться со мной?")
                menu Breakup_Bargaining:
                    extend ""
                    "Извини, мое мнение изменилось.":
                            $ Girl.Statup("Obed", 80, 5)
                            if ApprovalCheck(Girl, 1500):
                                    $ Line = "makeup"
                                    $ Girl.Statup("Love", 80, 5)
                                    if Girl is RogueX:
                                            ch_r "Это же замечательно!"
                                    elif Girl is KittyX:
                                            ch_k "Ладно!"
                                    elif Girl is EmmaX:
                                            ch_e "Приму твои слова за извинения. . ."
                                    elif Girl is LauraX:
                                            ch_l "А? Ладно. . ."
                                    elif Girl is JeanX:
                                            if not Player.Male:
                                                ch_j "Наконец-то, ты пришла в себя."
                                            else:
                                                ch_j "Наконец-то, ты пришел в себя."
                                    elif Girl is StormX:
                                            ch_s "Тогда ты можешь остаться."
                                    elif Girl is JubesX:
                                            ch_v "Клево. . ."
                                    elif Girl is GwenX:
                                            ch_g "Ох, это был настоящий эмоциональный удар!"
                                    elif Girl is BetsyX:
                                            ch_b "Прошу, научись контролировать себя. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Это же. . . хорошо?"
                                    elif Girl is WandaX:
                                            ch_w ". . . ладно?"
                            else:
                                    $ Line = "breakup"
                                    $ Girl.Statup("Love", 90, -5)
                                    $ Girl.Statup("Obed", 80, -5)
                                    $ Girl.Statup("Inbt", 80, 10)
                                    if Girl is RogueX:
                                            ch_r "Знаешь что? Забудь. Мы расстаемся."
                                    elif Girl is KittyX:
                                            ch_k "Уже слишком поздно. . ."
                                    elif Girl is EmmaX:
                                            ch_e "Боюсь, уже слишком поздно."
                                    elif Girl is LauraX:
                                            ch_l "Угу. Уже слишком поздно."
                                    elif Girl is JeanX:
                                            ch_j "Знаешь что? Уже слишком поздно."
                                    elif Girl is StormX:
                                            ch_s "Меня не интересуют эти твои игры."
                                    elif Girl is JubesX:
                                            ch_v "Слишком поздно. . ."
                                    elif Girl is GwenX:
                                            if not Player.Male:
                                                ch_g "Знаешь, я думаю, ты была права с самого начала. . ."
                                            else:
                                                ch_g "Знаешь, я думаю, ты был прав с самого начала. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Уже слишком поздно. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ну. . . я за тебя рада?"
                                    elif Girl is WandaX:
                                            ch_w "У меня нет времени на эту драму."
                    "Выбор сделан.":
                            $ Girl.Statup("Obed", 80, 5)
                            $ Line = "breakup"
                    "Знаешь, думаю, ты могла бы кое-что для меня сделать. . .[[секс-меню]":
                            $ Girl.AddWord(1,"bargainsex",0,0,0) #adds "bargainsex" to recent
                            $ Girl.Statup("Obed", 80, 3)
                            $ Tempmod = 50
                            $ MultiAction = 0
                            call SMenu # call expression Girl.Tag + "_SMenu" #call Rogue_SexMenu
                            $ MultiAction = 1
                            menu:
                                "Ладно, думаю, мы можем начать все сначала.":
                                        $ Girl.Statup("Love", 80, 3)
                                        $ Girl.Statup("Obed", 80, 5)
                                        $ Line = "makeup"
                                        $ Girl.FaceChange("smile")

                                "Все было неплохо, но мы все равно расстаемся.":
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 50, -5, 1)
                                        $ Girl.Statup("Love", 80, -10, 1)
                                        $ Girl.Statup("Obed", 50, 15)
                                        $ Girl.Statup("Obed", 80, 10)
                                        $ Line = "breakup"
                                        $ Anger += 4

                    "Может, мы могли бы принять в наши отношения еще одну?" if not Other and "bargainthreeway" not in Girl.RecentActions:
                            # if you haven't just tried this
                            $ Girl.AddWord(1,"bargainthreeway",0,0,0) #adds "bargainthreeway" to recent
                            call AnyLine(Girl,"Кого?")
                            menu:
                                extend ""
                                "[RogueX.Name_vin]?" if Girl is not RogueX:
                                        $ Other = RogueX
                                "[KittyX.Name_vin]?" if Girl is not KittyX and "met" in KittyX.History:
                                        $ Other = KittyX
                                "[EmmaX.Name_vin]?" if Girl is not EmmaX and "met" in EmmaX.History:
                                        $ Other = EmmaX
                                "[LauraX.Name_vin]?" if Girl is not LauraX and "met" in LauraX.History:
                                        $ Other = LauraX
                                "[JeanX.Name_vin]?" if Girl is not JeanX and "met" in JeanX.History:
                                        $ Other = JeanX
                                "[StormX.Name_vin]?" if Girl is not StormX and "met" in StormX.History:
                                        $ Other = StormX
                                "[JubesX.Name_vin]?" if Girl is not JubesX and "met" in JubesX.History:
                                        $ Other = JubesX
                                "[GwenX.Name_vin]?" if Girl is not GwenX and "met" in GwenX.History:
                                        $ Other = GwenX
                                "[BetsyX.Name_vin]?" if Girl is not BetsyX and "met" in BetsyX.History:
                                        $ Other = BetsyX
                                "[DoreenX.Name_vin]?" if Girl is not DoreenX and "met" in DoreenX.History:
                                        $ Other = DoreenX
                                "[WandaX.Name_vin]?" if Girl is not WandaX and "met" in WandaX.History:
                                        $ Other = WandaX

                                "Есть кто-то на примете?":
                                        $ Girl.FaceChange("confused")
                                        #picks her favorite girl. . .
                                        $ BO = ActiveGirls[:]
                                        $ BO.remove(Girl)
                                        $ Count = 0
                                        while BO:
                                                if Girl.GirlLikeCheck(BO[0]) > Count:
                                                        # if she likes this girl more than the last, she's the pick
                                                        $ Other = BO[0]
                                                        $ Count = Girl.GirlLikeCheck(BO[0])
                                                $ BO.remove(BO[0])
                                        $ Count = 0
                                        call AnyLine(Girl,Other.Name+"?")

                                "Не бери в голову, тупой вопрос.":
                                        $ Girl.Statup("Love", 200, -10)
                                        $ Girl.Statup("Obed", 50, -10, 1)
                                        $ Anger += 1
                                        $ Girl.FaceChange("angry")
                                        jump Breakup_Bargaining

                            if Other:
                                    $ Girl.FaceChange("confused")
                                    jump Breakup_Threeway_Offer

                if Anger < 3 and Line != "breakup" and Line != "makeup":
                        #if no decision and she's not pissed yet, loop
                        if Girl is StormX:
                                $ Line = "breakup"
                        else:
                                jump Breakup_Bargaining
        # End Bargaining



        if Line == "breakup" or Anger >= 4:
                if Anger >= 4:
                        #if she's pissed
                        $ Girl.FaceChange("angry")
                        $ Girl.Statup("Love", 60, -10, 1)
                        $ Girl.Statup("Obed", 50, -5)
                        $ Girl.Statup("Inbt", 70, 5)
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Ну и пошла ты!"
                                else:
                                    ch_r "Ну и пошел ты!"
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Ну ты и сука!"
                                else:
                                    ch_k "Ну ты и мудак!"
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Стерва."
                                else:
                                    ch_e "Подонок."
                        elif Girl is LauraX:
                                ch_l "Тебе лучше уйти."
                        elif Girl is JeanX:
                                ch_j "Ладно, все, я закончила с тобой!"
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "Боюсь, ты исчерпала все мое расположение."
                                else:
                                    ch_s "Боюсь, ты исчерпал все мое расположение."
                        elif Girl is JubesX:
                                ch_v "Тогда уебывай!"
                        elif Girl is GwenX:
                                ch_g "Слишком поздно, убирайся отсюда!"
                        elif Girl is BetsyX:
                                ch_b "Свали с глаз моих!"
                        elif Girl is DoreenX:
                                ch_d "Я сейчас ужасно зла!"
                        elif Girl is WandaX:
                                ch_w "У меня нет времени на эту драму."
                else:
                        #if she's just sad
                        $ Girl.Statup("Inbt", 70, 5)
                        $ Girl.FaceChange("sad")

                        if Girl.Love >= Girl.Obed:
                                #RogueX.Love >= RogueX.Obed:
                                if Girl is RogueX:
                                        ch_r "Я буду скучать по тебе."
                                elif Girl is KittyX:
                                        ch_k "Мне[KittyX.like]будет тебя нехватать!"
                                elif Girl is EmmaX:
                                        ch_e "Мне будет тебя нехватать."
                                        ch_e "По крайней мере пять минут."
                                elif Girl is LauraX:
                                        ch_l ". . ."
                                elif Girl is JeanX:
                                        ch_j "Знаешь. . . а, забудь."
                                elif Girl is StormX:
                                        ch_s "Я буду скучать по тебе."
                                elif Girl is JubesX:
                                        ch_v "Я буду скучать по тебе . ."
                                elif Girl is GwenX:
                                        ch_g "Я очень привязалась к тебе. . ."
                                elif Girl is BetsyX:
                                        ch_b "Мне будет тебя нехватать. . ."
                                elif Girl is DoreenX:
                                        ch_d "Я думала, между нами были настоящии чувства!"
                                elif Girl is WandaX:
                                        ch_w "Мне очень нравились наши отношения."
                                $ Girl.AddWord(1,0,0,"ex",0) #adds "ex" to traits
                        elif Girl.Obed >= Girl.Inbt:
                                #RogueX.Obed >= RogueX.Inbt:
                                $ Girl.Statup("Obed", 200, -10)
                                if Girl is RogueX:
                                        ch_r "И как мне теперь без тебя."
                                elif Girl is KittyX:
                                        ch_k "Я[KittyX.like]не знаю, как быть дальше."
                                elif Girl is EmmaX:
                                        ch_e "Мне придется как-то с этим жить."
                                elif Girl is LauraX:
                                        ch_l "Мне понадобятся новые варианты."
                                elif Girl is JeanX:
                                        ch_j "Ну и ладно."
                                elif Girl is StormX:
                                        ch_s "Мне жаль, что до этого дошло."
                                elif Girl is JubesX:
                                        ch_v "Мне это было нужно. . ."
                                elif Girl is GwenX:
                                        ch_g "Я ухожу, обреченная на мрак. . ."
                                elif Girl is BetsyX:
                                        if not Player.Male:
                                            ch_b "Ты казалась мне таким соблазнительным. . ."
                                        else:
                                            ch_b "Ты казался мне таким соблазнительным. . ."
                                elif Girl is DoreenX:
                                        ch_d "С тобой мне было так. . . комфортно."
                                elif Girl is WandaX:
                                        ch_w "Я ценила наши отношения."
                                $ Girl.AddWord(1,0,0,"ex",0) #adds "ex" to traits
                        else:
                                #inbt highest
                                if Girl is RogueX:
                                        ch_r "И кого мне теперь трахать?"
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Наверное[KittyX.like]мне теперь нужно найти другую киску?"
                                        else:
                                            ch_k "Наверное[KittyX.like]мне теперь нужно найти другой член?"
                                elif Girl is EmmaX:
                                        ch_e "Полагаю, мне надо будет найти другие варианты."
                                elif Girl is LauraX:
                                        ch_l "Ладно, как-нибудь еще увидимся."
                                elif Girl is JeanX:
                                        ch_j "Ладно, это здорово."
                                elif Girl is StormX:
                                        ch_s "Что ж, я смогу двигаться дальше."
                                elif Girl is JubesX:
                                        ch_v "Это было весело. . ."
                                elif Girl is GwenX:
                                        ch_g "Ну, мне было весело. . ."
                                elif Girl is BetsyX:
                                        if not Player.Male:
                                            ch_b "Эх, а ты мне нравилась. . ."
                                        else:
                                            ch_b "Эх, а ты мне нравился. . ."
                                elif Girl is DoreenX:
                                        ch_d "Эх, нам было так весело вместе!"
                                elif Girl is WandaX:
                                        ch_w "По крайней мере, нам было весело."
                                #does not add "ex" to traits because she doesn't care that much

                if Girl in Player.Harem:
                        $ Player.Harem.remove(Girl)

                $ Girl.Break[0] = 5 + Girl.Break[1] + Girl.Cheated
                $ Girl.Break[1] += 1
        #end "if you break up"


        else: #Stay together.
                $ Girl.FaceChange("smile")
                call AnyLine(Girl,"Я рада, что мы смогли все уладить. . .")
                if Girl.Love >= Girl.Obed:
                        #RogueX.Love >= RogueX.Obed:
                        $ Girl.Statup("Love", 200, 3)
                        if Girl is RogueX:
                                ch_r "Я очень по тебе скучала бы."
                        elif Girl is KittyX:
                                ch_k "Я[KittyX.like]скучала бы по тебе!"
                        elif Girl is EmmaX:
                                ch_e "Я слишком к тебе привязалась, [EmmaX.Petname]."
                        elif Girl is LauraX:
                                ch_l "Я. . . переживаю за тебя."
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Ты выросла в моих глазах."
                                else:
                                    ch_j "Ты вырос в моих глазах."
                                $ Girl.FaceChange("sly")
                                ch_j "Ты больше не как маленький поросенок. . ."
                        elif Girl is StormX:
                                ch_s "Я бы очень скучала по тебе."
                        elif Girl is JubesX:
                                ch_v "Я по тебе скучала бы. . ."
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Признай, ты скучала бы по мне. . ."
                                else:
                                    ch_g "Признай, ты бы скучал бы по мне. . ."
                        elif Girl is BetsyX:
                                ch_b "Да, я дорожу нашими отношениями."
                        elif Girl is DoreenX:
                                ch_d "Я так рада!"
                        elif Girl is WandaX:
                                ch_w "Я не хотела бы отказываться от тебя."
                elif Girl.Obed >= Girl.Inbt:
                        #RogueX.Obed >= RogueX.Inbt:
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Мне нужно, чтобы ты была со мной."
                                else:
                                    ch_r "Мне нужно, чтобы ты был со мной."
                        elif Girl is KittyX:
                                ch_k "Я[KittyX.like]не смогла бы без тебя."
                        elif Girl is EmmaX:
                                ch_e "Я не думаю, что смогу без тебя."
                        elif Girl is LauraX:
                                if not Player.Male:
                                    ch_l "Ты мне очень нужна."
                                else:
                                    ch_l "Ты мне очень нужен."
                        elif Girl is JeanX:
                                ch_j "Я, если честно, начинаю получать от наших отношений удовольствие. . ."
                        elif Girl is StormX:
                                ch_s "Я очень скучала бы по тебе."
                        elif Girl is JubesX:
                                ch_v "Мне это нужно. . ."
                        elif Girl is GwenX:
                                ch_g "Я бы не хотела снова быть никому не нужной. . ."
                        elif Girl is BetsyX:
                                ch_b "Да, мне было бы трудно без тебя. . ."
                        elif Girl is DoreenX:
                                ch_d "Я слишком дорожу нашими отношениями. . ."
                        elif Girl is WandaX:
                                ch_w "Наши отношения помогают мне."
                else:
                        #inbt highest, still a break-up, but friendly
                        if Girl is RogueX:
                                ch_r "Нам весело вместе. Давай продолжим в том же духе."
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Ты[KittyX.like]и впрямь смогла отвертеться на этот раз."
                                else:
                                    ch_k "Ты[KittyX.like]и впрямь смог отвертеться на этот раз."
                        elif Girl is EmmaX:
                                ch_e "Знаешь, очень трудно найти другую такую игрушку."
                        elif Girl is LauraX:
                                ch_l "Ладно."
                        elif Girl is JeanX:
                                ch_j "Ага. . . ладно."
                        elif Girl is StormX:
                                ch_s "Пожалуй, что так."
                        elif Girl is JubesX:
                                ch_v "Это весело, правда?"
                        elif Girl is GwenX:
                                ch_g "Без меня жизнь была бы не такой веселой!"
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Мы бы обе потеряли такой замечательный секс. . ."
                                else:
                                    ch_b "Мы бы оба потеряли такой замечательный секс. . ."
                        elif Girl is DoreenX:
                                ch_d "Без тебя было бы намного скучнее!"
                        elif Girl is WandaX:
                                ch_w "Мне слишком весело в наших отношениях, чтобы отказываться от них."
        $ Line = 0
        return
        #End Break-up


# End Break-up/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start checks for cheating and sharing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label CheatCheck(BO=[],BO2=[],TempOption=[]):
        # This checks whether any girl saw you with any other girl today.
        # Called by EventCalls
        # If you're in the room with that girl, it launches the cheated scene, otherwise, it has her ask you about it later.
        # Roster[Counter] is the first girl, Roster[Counter2] is the second girl
        # loops through girl 2 options until finished, then next girl 1 option, until done

        # add an aspect to account for hooking up with multiple girls that have not yet been accounted for. . .
        $ BO = TotalGirls[:]
        $ renpy.random.shuffle(BO)


        python:
            for BX in BO:
                if BX not in Player.Harem:
                    pass
                elif "locked" in Player.Traits and BX.Loc != bg_current:
                    #exits if the door is locked and she is not in the room with you
                    pass
                else:
                    BO2 = TotalGirls[:]
                    for BY in BO2:
                        #if "dating" in RogueX.Traits or RogueX in Player.Harem:
                        if "saw with " + BY.Tag in BX.Traits:
                            #if "saw with Kitty" in RogueX.Traits:
                            if BX in Player.Harem and BY in Player.Harem:
                                    #if both girls were in the harem, this shouldn't happen
                                    BX.DrainWord("saw with "+BY.Tag,0,0,1)      #removes "saw with Kitty" from traits
                            elif BX in Player.Harem and BY.Tag + "Yes" in Player.Traits:
                                    BX.DrainWord("saw with "+BY.Tag,0,0,1)      #removes "saw with Kitty" from traits
                            elif bg_current == "bg player" or bg_current == BX.Home:
                                    TempOption = [BX,BY]
                                    break
        if TempOption:
                #if caught out, call the event then cancel back to home
                call Cheated(TempOption[0],TempOption[1])
                jump Misplaced
        return
#label ShareCheck(BO=[]):
#        # This checks whether one of the girls is supposed to ask the other about joining the harem
#        # Called by Relationship_Select
#        # EGirls[Counter] is the first girl, BO[Counter2] is the second girl
#        # loops through girl 2 options until finished, then next girl 1 option, until done

#        #if "dating" in RogueX.Traits or RogueX in Player.Harem:
#        $ BO = TotalGirls[:]
#        while BO:
#                if "ask " + BO[0].Tag in EGirls[0].Traits:
#                        #if "ask Kitty" in RogueX.Traits:
#                        if EGirls[0] in Player.Harem and BO[0] in Player.Harem:
#                                #if both girls were in the harem, this shouldn't happen
#                                $ EGirls[0].DrainWord("ask "+BO[0].Tag,0,0,1)      #removes "askKitty" from traits
#                        else:
#                                call Share(EGirls[0],BO[0])
#                                return
#                $ BO.remove(BO[0])
#        return

#Start Relationship_Select / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Relationship_Select(EGirls=[],BO=[]):
    #this picks a relationship scene to play out this time block, and then places it in Event_Queue as [RogueX,"_Love"]
    # This is then called in Events by "call expression Event_Queue[0].Tag + Event_Queue[1] #calls an event, ala "Rogue_Love""

    $ EGirls = ActiveGirls[:]
    $ renpy.random.shuffle(EGirls)

    $ Event_Queue = [0,0]
    #fills list and then randomly shuffles it.
    python:
        for EGX in EGirls:
            BO = TotalGirls[:]
            for BX in BO:
                    #call ShareCheck #new method,
                    # This checks whether one of the girls is supposed to ask the other about joining the harem
                    # EGX is the first girl, BX is the second girl
                    # loops through girl 2 options until finished, then next girl 1 option, until done
                    if "ask " + BX.Tag in EGX.Traits:
                            #if "ask Kitty" in RogueX.Traits:
                            if EGX in Player.Harem and BX in Player.Harem:
                                    #if both girls were in the harem, this shouldn't happen
                                    EGX.DrainWord("ask "+BX.Tag,0,0,1)      #removes "askKitty" from traits
                            else:
                                    ShareQueue = [EGX,BX]       #if ShareQueue: call Share(ShareQueue[0],ShareQueue[1])
                                    #call Share(EGX,BX)
                                    break                       #cancels out after picking one
            #end ShareCheck loop

            if "relationship" in EGX.DailyActions:
                            #skip all this if had another scene with her earlier
                            pass
            elif "stoodup" in EGX.Traits: #you stood her up
                            Event_Queue = [EGX,"Stoodup"]
            elif EGX.Break[0] or "angry" in EGX.DailyActions:
                            #skip all this if you're broken up
                            pass
            elif "nogirls" in EGX.History and not Player.Male and not ApprovalCheck(EGX, 1100):
                            #if she's refused to date you as a girl, skip the rest until that is settled
                            pass
            elif not EGX.Event[0] and EGX.Sleep >= 5 and EGX.Loc == bg_current:
                            Event_Queue = [EGX,"_Key"]
            elif EGX is JeanX:
                if bg_current != "bg classroom":
                    if JeanX.Obed >= 500 and "sir" not in JeanX.History:
                            Event_Queue = [EGX,"_Sub"]
                    elif JeanX.Obed >= 800 and "master" not in JeanX.History:
                            Event_Queue = [EGX,"_Master"]
                    elif JeanX.Love >= 500 and "sexfriend" not in JeanX.History:
                            Event_Queue = [EGX,"_BF"]
                    elif JeanX.Love >= 800 and JeanX.Obed >= 600 and not JeanX.Event[5]:
                            Event_Queue = [EGX,"_Love"]
                    elif "daddy" not in JeanX.Petnames and ApprovalCheck(JeanX, 750, "L"):
                            Event_Queue = [EGX,"_Daddy"]

            elif "boyfriend" not in EGX.Petnames and EGX.Love >= 800 and EGX.Event[5] != 20 and EGX.Tag + "No" not in Player.Traits: # EGX.Event[5]
                    # EGX.Event[5] is 20 if you refused due to other girlfriend
                    # if "RogueNo" it means you can't date her.
                    if EGX is LauraX and LauraX.Event[5] == 3:
                                #This gets called when Laura asks you to break up with the other girls
                                Event_Queue = [EGX,"_Cleanhouse"]
                    elif Player.Harem and EGX not in Player.Harem and EGX.Tag + "Yes" not in Player.Traits:
#                    elif Player.Harem and EGX and EGX.Tag + "Yes" not in Player.Traits:
                                Event_Queue = [EGX,"poly"]
                    else:
                                Event_Queue = [EGX,"_BF"]

            elif "lover" not in EGX.Petnames and EGX.Love >= 950 and EGX.Event[6] < 15: # EGX.Event[6]
                                # <15 is also != 20, but double check that there isn't more to that. . .K_Event[6] != 20? and E_Event[6] != 20:
                                Event_Queue = [EGX,"_Love"]

            elif "sir" not in EGX.History and "sir" not in EGX.Petnames and EGX.Obed >= 500: # EGX.Event[7]
                                Event_Queue = [EGX,"_Sub"]

            elif "master" not in EGX.History and "master" not in EGX.Petnames and EGX.Obed >= 850 and EGX.Event[8] < 2:
                                #and EGX.Event[8] < 2, remove that bit when Rogue's scene is updated to not need it.
                                Event_Queue = [EGX,"_Master"]

            elif "daddy" not in EGX.Petnames and ApprovalCheck(EGX, 750, "L") and ApprovalCheck(EGX, 500, "O") and ApprovalCheck(EGX, 500, "I"): # EGX.Event[5]
                                Event_Queue = [EGX,"_Daddy"]

            elif "sex friend" not in EGX.Petnames and EGX.Inbt >= 500: # EGX.Event[9]  Fix this one
                    if EGX is EmmaX:
                        if bg_current == "bg classroom" and (EmmaX.Loc == "bg teacher" or EmmaX.Loc == "bg classroom") and Time_Count == 2:
                                Event_Queue = [EGX,"_Sexfriend"] #only works if after class, otherwise picks some other girl
                    elif EGX is StormX:
                        if StormX.Event[9]:
                                pass
                        else:
                                Event_Queue = [EGX,"_Sexfriend"]
                    else:
                                Event_Queue = [EGX,"_Sexfriend"]

            elif "fuck buddy" not in EGX.Petnames and EGX.Inbt >= 800: # EGX.Event[10]  Fix this one
                    if EGX is LauraX or EGX is JubesX:
                        if bg_current == "bg player" and EGX.Loc != bg_current:
                                Event_Queue = [EGX,"_Fuckbuddy"]
                    elif EGX is StormX:
                        if bg_current == "bg classroom" and Time_Count == 2 and Weekday in (1,3):
                                Event_Queue = [EGX,"_Fuckbuddy"]
                    else:
                                Event_Queue = [EGX,"_Fuckbuddy"]

            if Event_Queue[1]:
                #kicks out of the loop if an answer is chosen
                break
    return
#end Relationship_Select / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label AddictCheck(BO=[],Exit=0): #rkeljsvgbdw
        # Called at end of Wait cycle to see if the girl is in an addiction spiral
        # if a girl is given the "Addict_Queue" status, the addiction event will play whenever you are in a character room.
        $ BO = ActiveGirls[:]

        $ renpy.random.shuffle(BO)

        $ Addict_Queue = 0
        if JubesX in BO and JubesX.Addict >= 50:
                #Moves Jubilee to head of the line if she's eligible.
                $ BO.remove(JubesX)
                $ BO.insert(0, JubesX)
        python:
            for BX in BO:
                if "asked fix" in Player.DailyActions and "asked meet" not in BO[0].DailyActions:
                                #this skips any new girls if you've agreed to meet another one
                                pass
                elif BX.Event[3]:
                                #this skips if you've already dealt with her once recently
                                pass
                elif BX is JubesX and "sunshine" not in JubesX.History:
                                pass
                elif "angry" not in BX.RecentActions and "addiction" not in BX.DailyActions and BX.Action >= 1:
                        #Activates if she needs her fix
                        if BX.Addict >= 60 and BX.Resistance:
                                #if addict over 60, and she's completed the event chain
                                Addict_Queue = BX         #call Addiction_Fix(BX)
                                if bg_current == BX.Home or bg_current == "bg player":
                                            pass #$ Addict_Queue = [BX]         #call Addiction_Fix(BX)
                                else:
                                    if "asked meet" in BX.RecentActions:
                                            pass
                                    elif "asked meet" in BX.DailyActions and BX.Addict >= 80:
                                            Exit = BX
                                            break
#                                            return BX
#                                            "[BX.Name] texts you. . ."
#                                            call AnyLine(BX,"I know I asked to meet you in your room earlier, but I'm serious, this is important.")
#                                            $ Player.AddWord(1,"asked fix",0,0,0)
#                                            $ BX.AddWord(1,"asked meet","asked meet",0,0)
#                                            call ReturnToRoom
#                                            return
                                    elif "meet girl" in Player.DailyActions:
                                            pass
                                    else:
                                            Exit = BX
                                            break
#                                            return BX
#                                            "[BX.Name] texts and asks if you could meet her in your room later."
#                                            $ BX.AddWord(1,"asked meet","asked meet",0,0)
#                                            call ReturnToRoom
#                                            return
                        #Activates if you don't need a fix but already have resistance
                        elif BX.Resistance:
                                pass
                        #These are the "first time addict" event chains
                        elif BX.Addict >= 35 and not BX.Event[1]:
                                #"I'm addicted" event
                                Addict_Queue = BX         #call First_Addicted(BX)
                        elif BX.Addict >= 60 and BX.Event[1] <= 2:
                                #"I'm super-addicted" event
                                Addict_Queue = BX         #call First_Addicted(BX)
                        elif BX.Addict >= 90:
                                #"I'm crazy-addicted" event
                                Addict_Queue = BX         #call First_Addicted(BX)
        if Exit:
            if "asked meet" in Exit.DailyActions and Exit.Addict >= 80:
                    "[Exit.Name] отправляет вам сообщение. . ."
                    call AnyLine(Exit,"Я знаю, что уже просила о встрече в твоей комнате. . . но это важно.")
                    $ Player.AddWord(1,"asked fix",0,0,0)
                    $ Exit.AddWord(1,"asked meet","asked meet",0,0)
                    $ Exit = 0
                    call ReturnToRoom
            else:
                    "[Exit.Name] отправляет вам сообщение, в котором просит вас встретиться с ней позже в вашей комнате."
                    $ Exit.AddWord(1,"asked meet","asked meet",0,0)
                    $ Exit = 0
                    call ReturnToRoom
        return
# end AddictCheck / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Share(Girl=0,Other=0): #rkeljsvgbdw
        # This checks when one girl asks another to share you.
        # it is called by EventCalls if ShareQueue is full

        $ Girl.DrainWord("ask "+Other.Tag,0,0,1) #removes "ask Kitty" from RogueX.Traits
        $ ShareQueue = []

        if Girl.Break[0]:
                #if the girl was only recently broken up with. . .
                "[Girl.Name] присылает вам сообщение."
                $ Other.Statup("Love", 90, -10)
                $ Other.Statup("Obed", 80, 10)
                $ Other.Statup("Inbt", 80, 5)
                if Other is RogueX:
                        call AnyLine(Girl,"Она сказала: \"перестань меня беспокоить?\"")
                elif Other is KittyX:
                        call AnyLine(Girl,"Она сказала: \"оставьте меня в покое?\"")
                elif Other is EmmaX:
                        call AnyLine(Girl,"Она сказала: \"я соглашусь, когда рак на горе свистнет?\"")
                elif Other is LauraX:
                        call AnyLine(Girl,"Она сказала: \"иди нахуй?\"")
                elif Other is JeanX:
                        call AnyLine(Girl,"Похоже, она не знала, о ком я говорю.")
                elif Other is StormX:
                        call AnyLine(Girl,"Она сказала: \"Я бы предпочла этого не делать?\"")
                elif Other is JubesX:
                        call AnyLine(Girl,"Она сказала: \"Оставь меня в покое?\"")
                elif Other is GwenX:
                        call AnyLine(Girl,"Она сказала: \"я не интересуюсь симуляторами гарема?\"")
                        call AnyLine(Girl,". . . что это значит?")
                elif Other is BetsyX:
                        call AnyLine(Girl,"Она сказала: \"меня не интересует роль содержанки.\"")
                elif Other is DoreenX:
                        call AnyLine(Girl,"Она сказала: \"я не хочу быть третьей лишней.\"")
                elif Other is WandaX:
                        call AnyLine(Girl,"Она сказала: \"Ну, попробуй угадать мой ответ.\"")
                call AnyLine(Girl,"Думаю, мы узнаем, если она согласится с этой идеей.")
        else:
                if Other is JeanX or Other.GirlLikeCheck(Girl) >= 800 or ApprovalCheck(Other, 1800) or (ApprovalCheck(Other, 1500) and Other.GirlLikeCheck(Girl) >= 500):
                        # if she likes the other girl a lot, or likes you a lot, or sort of likes you both. . .
                        $ Other.AddWord(1,0,0,"poly "+Girl.Tag,0) #adds "poly Kitty" to RogueX.Traits
                        #$ Other.AddWord(1,0,0,"dating?",0) #adds "dating" to KittyX.Traits

                        $ Other.Statup("Obed", 80, 10)
                        $ Other.Statup("Inbt", 80, 15)

                        $ BO = Player.Harem[:]
                        python:
                            for BX in BO:
                                BX.DrainWord("saw with "+Other.Tag,0,0,1)
                        if Girl.Event[5]:
                                # if you've already done her BF event before. . .
                                $ Player.Harem.append(Other)
                                #$ Other.AddWord(1,0,0,"dating",0)     #adds "dating" to traits
                        elif bg_current in PersonalRooms:
                                #if you're in a character room, launch their boyfriend speech
                                if Other.Tag+"Yes" not in Player.Traits:
                                        $ Player.Traits.append(Other.Tag+"Yes")
                                call expression Other.Tag + "_BF" #call Rogue_BF
                                jump Misplaced
                        else:
                                # if not in a character room, ask later
                                if Other.Tag+"Yes" not in Player.Traits:
                                        $ Player.Traits.append(Other.Tag+"Yes")
                                call AskedMeet(Other,"bemused","говорит, что "+Girl.Name+" ответила, что все в порядке. . .")
                else:
                        #If Girl refuses to share you
                        "[Girl.Name] присылает вам сообщение."
                        call AnyLine(Girl,"Я поговорила с "+Other.Name_tvo+" насчет нас троих, она сказала, что ей не нравится эта идея,")
                        if not ApprovalCheck(Other, 2000):
                                $ Other.Statup("Love", 200, -15)
                                $ Other.Statup("Obed", 50, -5)
                                $ Other.Statup("Inbt", 50, 5)
                                call AnyLine(Girl,"Ты просто ей не нравишься.")
                        else:
                                $ Other.Statup("Love", 200, -5)
                                call AnyLine(Girl,"Похоже, я ей не особо нравлюсь. . .")

                        #means that she won't be available to ask again for another 7 days
                        $ Other.Break[0] = 7
        return

# Start Cheated on the girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Cheated(Girl=0,Other=0, Resolution = 0, B = 0): #rkeljsvgbdw
        # Called by EventCalls->CheatCheck if you got caught cheating
        #Resolution is Resolution count, you want this over 2 at least. B is the bonus modifier
        $ Girl.AddWord(1,0,"relationship",0,0)
        call Shift_Focus(Girl)

        $ Girl.FaceChange("angry")

        if "switchcheck" in Girl.Traits:
                #if you recently switched sexes. . .
                if Girl.Loc != bg_current and Girl not in Party:
                        "Вдруг [Girl.Name] подходит к вам,"
                $ Girl.Loc = bg_current
                call Set_The_Scene
                call CleartheRoom(Girl)
                $ Girl.FaceChange("confused")
                call AnyLine(Girl,"Нам нужно поговорить, "+Player.Name+"! . . "+Player.Name+"? . . ")
                call expression Girl.Tag + "_Switch" #call Rogue_Switch
                $ Girl.FaceChange("angry")
                call AnyLine(Girl,". . . Но это не так уж важно!")

        elif Girl.Loc != bg_current and Girl not in Party:
                "Вдруг [Girl.Name] подходит к вам с явным желанием поговорить."

        $ Girl.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(Girl)
        $ Girl.DrainWord("asked meet",0,1) #removes "asked meet" from daily
        if "meet girl" in Player.DailyActions:
                $ Player.DailyActions.remove("meet girl")

        call Taboo_Level(1)

        if Girl.GirlLikeCheck(Other) >= 900:
                $ Resolution += 2
        elif Girl.GirlLikeCheck(Other) >= 800:
                $ Resolution += 1
        elif Girl is WandaX:
                $ Resolution += 1
        $ B = (int(Girl.GirlLikeCheck(Other)/2))-250

        if len(Player.Harem) < 3:
                $ Resolution -= Girl.Cheated if Girl.Cheated <= 3 else 3 #Adds to Resolution 3 or less based on cheating

        if len(Player.Harem) >= 3:
                if not Player.Male:
                    call AnyLine(Girl,"Я заметила, что ты, кажется, нашла еще одну. . .")
                else:
                    call AnyLine(Girl,"Я заметила, что ты, кажется, нашел еще одну. . .")
        elif Girl.Cheated:
                $ Girl.Statup("Love", 200, -50)
                $ Girl.Statup("Obed", 80, -20)
                $ Girl.Statup("Inbt", 50, -50)
                if Girl is RogueX:
                        ch_r "Почему ты опять меня обманываешь?"
                elif Girl is KittyX:
                        if not Player.Male:
                            ch_k "Ты опять взялась мне изменять?!"
                        else:
                            ch_k "Ты опять взялся мне изменять?!"
                elif Girl is EmmaX:
                        ch_e "Я заметила, что ты снова напрыгиваешь на все, что движется. . ."
                elif Girl is LauraX:
                        if not Player.Male:
                            ch_l "Ты опять трахалась с другой."
                        else:
                            ch_l "Ты опять трахался с другой."
                elif Girl is JeanX:
                        if not Player.Male:
                            ch_j "Ты кувыркалась с кем-то. . . снова!"
                        else:
                            ch_j "Ты кувыркался с кем-то. . . снова!"
                elif Girl is StormX:
                        ch_s "Ты опять изменяешь. . ."
                elif Girl is JubesX:
                        ch_v "Ты снова спишь за моей спиной. . ."
                elif Girl is GwenX:
                        ch_g "Ты опять играешь со мной?"
                elif Girl is BetsyX:
                        ch_b "Я снова обнаружила, что ты мне изменяешь!"
                elif Girl is DoreenX:
                        ch_d "Ты снова мне изменяешь!"
                        $ Resolution -= 2 if DoreenX.Obed < 800 else 1
                elif Girl is WandaX:
                        if not Player.Male:
                            ch_w "Ты снова ходила по бабам. . ."
                        else:
                            ch_w "Ты снова ходил по бабам. . ."
        else:
                $ Girl.Statup("Love", 200, -100)
                $ Girl.Statup("Obed", 80, -30)
                $ Girl.Statup("Inbt", 50, -20)
                if Girl is RogueX:
                        ch_r "Какого черта это было?"
                elif Girl is KittyX:
                        ch_k "Эй?! Что это было?"
                elif Girl is EmmaX:
                        if not Player.Male:
                            ch_e "Не могла бы ты мне объяснить, что это я видела?"
                        else:
                            ch_e "Не мог бы ты мне объяснить, что это я видела?"
                elif Girl is LauraX:
                        ch_l "Я видела тебя с кем-то."
                elif Girl is JeanX:
                        ch_j "Эй! Я видела тебя с. . . "
                        ch_j ". . . Я не помню ее имени, но я видела тебя с ней!"
                elif Girl is StormX:
                        if not Player.Male:
                            ch_s "Как я погляжу, ты нашла себе другую. . ."
                        else:
                            ch_s "Как я погляжу, ты нашел себе другую. . ."
                elif Girl is JubesX:
                        if not Player.Male:
                            ch_v "Я думаю, что ты изменила мне. . ."
                        else:
                            ch_v "Я думаю, что ты изменил мне. . ."
                elif Girl is GwenX:
                        ch_g "Эй, ну и что это было. . ?"
                elif Girl is BetsyX:
                        if not Player.Male:
                            ch_b "Мне кажется, ты вела себя с ней нездержанно. . ."
                        else:
                            ch_b "Мне кажется, ты вел себя с ней нездержанно. . ."
                elif Girl is DoreenX:
                        ch_d "Я. . . видел вас вместе. . ."
                        $ Resolution -= 1 if DoreenX.Obed < 800 else 0
                elif Girl is WandaX:
                        if not Player.Male:
                            ch_w "Кажется, ты заигрывала с другой девушкой. . ."
                        else:
                            ch_w "Кажется, ты заигрывал с другой девушкой. . ."

        menu:
                extend ""
                "Извини.":
                        $ Girl.Statup("Love", 90, 30)
                        $ Girl.Statup("Obed", 80, -10)
                        $ Line = "sorry"
                        $ Resolution += 1

                "Что ты имеешь в виду?":
                        $ Girl.Statup("Love", 200, -10)
                        $ Girl.Statup("Obed", 80, 15)
                        $ Girl.Statup("Inbt", 80, 5)
                        if Girl is StormX:
                                ch_s "Я говорю о тебе и [Other.Name_pre]. . ."
                        elif Girl is DoreenX:
                                ch_d "Я видела тебя вместе с [Other.Name_tvo]. . ."
                        else:
                                call AnyLine(Girl,"То, что ты спутался с "+Other.Name_tvo+"!")
                        menu:
                                extend ""
                                "Ох! Извини!":
                                    $ Girl.Statup("Love", 90, 20)
                                    $ Girl.Statup("Obed", 80, -10)
                                    $ Line = "sorry"
                                "А, ты про это, ага.":
                                    $ Girl.Statup("Love", 200, -20)
                                    $ Girl.Statup("Obed", 80, 10)
                                    $ Line = "yeah"
                                    $ Resolution -= 1

                "Ты имеешь в виду [Other.Name_vin]?":
                        $ Girl.Statup("Love", 200, -15)
                        $ Girl.Statup("Obed", 80, 20)
                        $ Girl.Statup("Inbt", 80, 10)
                        call AnyLine(Girl,"Да, \"я имею в виду "+Other.Name_vin+".\"")

                        if Girl is RogueX:
                                $ Line = "Вы развлекаетесь у меня за спиной!"
                        elif Girl is KittyX:
                                if not Player.Male:
                                    $ Line = "Почему ты так набросилась на нее?!"
                                else:
                                    $ Line = "Почему ты так набросился на нее?!"
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    $ Line = "Или ты не заметила, кого трахала?"
                                else:
                                    $ Line = "Или ты не заметил, кого трахал?"
                        elif Girl is LauraX:
                                $ Line = "Я чувствую ее запах на тебе."
                        elif Girl is JeanX:
                                $ Line = "Я прочитала ее воспоминания об этом!"
                        elif Girl is StormX:
                                $ Line = "Я знаю, что вы были вместе."
                        elif Girl is JubesX:
                                $ Line = "У меня хороший нюх. . ."
                        elif Girl is GwenX:
                                $ Line = "Я видела вас вместе. . ."
                        elif Girl is BetsyX:
                                $ Line = "Я видела вас вместе."
                        elif Girl is DoreenX:
                                $ Line = "Я видела вас. . . вместе."
                        elif Girl is WandaX:
                                $ Line = "Ага, я видела вас вместе."

                        if Girl.Cheated:
                            $ Line = Line+" Снова!"
                        call AnyLine(Girl,Line)
                        menu:
                                extend ""
                                "Ох! Извини!":
                                    $ Girl.Statup("Love", 90, 15)
                                    $ Girl.Statup("Obed", 80, -10)
                                    $ Line = "sorry"
                                "Ну да.":
                                    $ Girl.Statup("Love", 200, -20)
                                    $ Girl.Statup("Obed", 80, 10)
                                    $ Line = "yeah"
                                    $ Resolution -= 2

        if Line == "sorry":
                    $ Girl.FaceChange("sadside")
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Ну, конечно, еще бы ты не извинилась, но это не правильно."
                            else:
                                ch_r "Ну, конечно, еще бы ты не извинился, но это не правильно."
                            ch_r "Заниматься подобным с кем-то вроде [Other.Name_rod]. . ."
                    elif Girl is KittyX:
                            ch_k "Только не говори мне, что тебе жаль!"
                    elif Girl is EmmaX:
                            ch_e "Действительно очень жаль. . ."
                    elif Girl is LauraX:
                            ch_l "И правда жаль."
                    elif Girl is JeanX:
                            if not Player.Male:
                                ch_j "Еще бы ты не извинилась!"
                            else:
                                ch_j "Еще бы ты не извинился!"
                    elif Girl is StormX:
                            ch_s "Уверена, тебе очень жаль."
                    elif Girl is JubesX:
                            ch_v "Ох, уверена, что так и есть."
                    elif Girl is GwenX:
                            ch_g "Я не знаю, достаточно ли тут простых извинений. . ."
                    elif Girl is BetsyX:
                            ch_b "Раскаяние - это только первый шаг. . ."
                    elif Girl is DoreenX:
                            ch_d "Ну. . . для начала неплохо. . ."
                    elif Girl is WandaX:
                            ch_w "Да? И?"
                    $ Girl.FaceChange("sad")
        else:
                    $ Girl.FaceChange("confused")
                    if Girl is RogueX:
                            ch_r "Да? И что же ты можешь сказать в свое оправдание?"
                    elif Girl is KittyX:
                            ch_k "Да? Да?! Что это вообще значит?!"
                    elif Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Не уверена, что ты понимаешь, во что ты ввязалась. . ."
                            else:
                                ch_e "Не уверена, что ты понимаешь, во что ты ввязался. . ."
                    elif Girl is LauraX:
                            ch_l "У тебя есть объяснения? Или же. . ."
                    elif Girl is JeanX:
                            ch_j "Ты хочешь мне что-нибудь объяснить?!"
                    elif Girl is StormX:
                            ch_s "У тебя есть какое-нибудь объяснение?"
                    elif Girl is JubesX:
                            ch_v "Нууу, у тебя есть какое-нибудь оправдание?"
                    elif Girl is GwenX:
                            ch_g "Тебе есть, что мне сказать, или как?"
                    elif Girl is BetsyX:
                            ch_b "Ну? Тебе есть что сказать в свое оправдание?"
                    elif Girl is DoreenX:
                            ch_d "Ты. . .  хочешь что-нибудь сказать в свое оправдание?"
                    elif Girl is WandaX:
                            $ Resolution += 1
                            ch_w "Да? И?"
                    $ Girl.FaceChange("angry")

        menu:
                extend ""
                "Я знаю, что причинила тебе боль, мне очень жаль." if not Player.Male:
                        $ Girl.Statup("Love", 90, 25)
                        if Girl is JeanX:
                                $ Girl.Statup("Obed", 80, 10)
                                $ Resolution += 1
                                ch_j "Ага, с этим мы уже разобрались, что-то еще?"
                        else:
                                $ Girl.Statup("Obed", 80, -5)
                                call AnyLine(Girl,"Ну, по крайней мере, ты понимаешь это.")
                        $ Resolution += 2

                "Я знаю, что причинил тебе боль, мне очень жаль." if Player.Male:
                        $ Girl.Statup("Love", 90, 25)
                        if Girl is JeanX:
                                $ Girl.Statup("Obed", 80, 10)
                                $ Resolution += 1
                                ch_j "Ага, с этим мы уже разобрались, что-то еще?"
                        else:
                                $ Girl.Statup("Obed", 80, -5)
                                call AnyLine(Girl,"Ну, по крайней мере, ты понимаешь это.")
                        $ Resolution += 2

                "Мы просто баловались, ничего серьезного.":
                        $ Girl.Statup("Obed", 80, 30)
                        $ Girl.Statup("Inbt", 80, 10)
                        if Girl is RogueX:
                                ch_r "\"Ничего серьезного?\" Скорее всего, тебе -просто плевать-."
                        elif Girl is KittyX:
                                ch_k "Я покажу тебе \"ничего серьезного\"!"
                        elif Girl is EmmaX:
                                ch_e "Это уже мне судить, что \"серьезно\", а что нет"
                        elif Girl is LauraX:
                                if ApprovalCheck(Girl, 1500):
                                        ch_l "Ладно, зато честно."
                                else:
                                        ch_l "Хочешь попробовать еще раз?"
                        elif Girl is JeanX:
                                $ Girl.Eyes = "side"
                                $ Girl.Statup("Love", 80, 10)
                                $ Resolution += 1
                                ch_j "Ох. . . хорошо. . ."
                                $ Girl.FaceChange("angry",2)
                                ch_j "Но не в этом дело!"
                                $ Girl.Blush = 1
                        elif Girl is StormX:
                                ch_s "Ничего серьезного для тебя, но как насчет меня?"
                        elif Girl is JubesX:
                                ch_v "Ох, это типа оправдание?"
                        elif Girl is GwenX:
                                $ Girl.FaceChange("smile",2)
                                ch_g "О, ты просто дурачился, ладно. . ."
                                $ Girl.FaceChange("angry")
                                ch_g "Эй, подожди-ка!"
                        elif Girl is BetsyX:
                                ch_b ". . ."
                                ch_b "Боюсь, это неприемлемый ответ."
                        elif Girl is DoreenX:
                                ch_d ". . . я не могу принять такой ответ. . ."
                        elif Girl is WandaX:
                                $ Girl.Statup("Love", 200, -10)
                                $ Resolution += 2
                                ch_w "Хм. . ."
                        else:
                                $ Girl.Statup("Love", 200, -25)

                        if not ApprovalCheck(Girl, 700, "O", Bonus = (B/3)):
                            $ Resolution -= 2

                "Я считаю, она невероятно горяча.":
                    if B >= 100 or ApprovalCheck(Girl, 500, "I", Bonus = (B/3)):
                            # if Like trait is 700 or more. . .
                            $ Girl.FaceChange("confused",Eyes="side")
                            if Girl is StormX:
                                    ch_s "Она, конечно, красивая, но я не понимаю, почему это может служить оправданием."
                            elif Girl is BetsyX:
                                    ch_b "Она очень привлекательна, но я не понимаю, почему это может служить оправданием."
                            elif Other is KittyX:
                                    call AnyLine(Girl,"Ну. . . да, она симпатичная, но и что с того?")
                            else:
                                    call AnyLine(Girl,"Ну. . . да, она горяча, но и что с того?")
                            $ Girl.Statup("Lust", 90, 5)
                            $ Line = "threeway"
                    else:
                            $ Girl.Statup("Love", 200, -20)
                            $ Girl.Statup("Obed", 80, 30)
                            if Girl is RogueX:
                                    ch_r "Но это ни хрена не значит, [Player.Name], ты встречаешься не с ней, а со мной!"
                            elif Girl is KittyX:
                                    ch_k "Да какая разница?!"
                            elif Girl is EmmaX:
                                    ch_e "Мда. Говоришь о ней, когда я тут."
                            elif Girl is LauraX:
                                    ch_l "Это не оправдывает тебя."
                            elif Girl is JeanX:
                                    ch_j "Это не значит, что ты можешь трахать ее!"
                            elif Girl is StormX:
                                    ch_s "Не думаю, что от этого ситуация становится лучше."
                            elif Girl is JubesX:
                                    ch_v "Мне все равно, насколько она сексуальна!"
                            elif Girl is GwenX:
                                    ch_g "Конечно, она \"горяча,\" ее такой нарисовали!"
                            elif Girl is BetsyX:
                                    ch_b "Восхваляешь другую, мне кажется, ты думаешь не о том. . ."
                            elif Girl is DoreenX:
                                    ch_d "Мне совсем не нужно это слышать. . ."
                            elif Girl is WandaX:
                                    $ Resolution += 1
                                    ch_w "Пожалуй. . ."
                            $ Resolution -= 2

                "Разве она тебе не нравится?":
                    $ Girl.Statup("Obed", 80, 30)
                    if B >= 100 or ApprovalCheck(Girl,500,"I",Alt=[[WandaX],300]):
                            # if Like trait is 700 or more. . .
                            $ Girl.FaceChange("confused",Eyes="side")
                            $ Girl.Statup("Inbt", 90, 25)
                            $ Girl.Statup("Lust", 90, 5)
                            if Girl is RogueX:
                                    ch_r "Может быть, самую малость. . ."
                            elif Girl is KittyX:
                                    ch_k "Что? Нравится. . . типа \"нравится\" нравится? Эм. . ."
                            elif Girl is EmmaX:
                                    ch_e "Она привлекательна, да, но я не думаю, что это имеет значение."
                            elif Girl is LauraX:
                                    ch_l "Да, но и ты мне тоже нравишься."
                            elif Girl is JeanX:
                                    ch_j "Ну. . . возможно. . ."
                            elif Girl is StormX:
                                    ch_s "Нравится, хотя, возможно, не так сильно, как ты. . ."
                            elif Girl is JubesX:
                                    ch_v "Нууу, ага, но. . . не отходи от темы!"
                            elif Girl is GwenX:
                                    ch_g "Конечно нравится, она же супер."
                            elif Girl is BetsyX:
                                    ch_b ". . . она очень привлекательна. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ну. . . она очень милая. . ."
                            elif Girl is WandaX:
                                    ch_w "Нравится, конечно. . ."
                            $ Line = "threeway"
                    elif B >= 50 and Girl is not JeanX:
                            # if Like trait is 600 or more. . .
                            $ Girl.FaceChange("confused")
                            $ Girl.Statup("Love", 200, -10)
                            if Girl is EmmaX and Other is not StormX:
                                    ch_e "Она хорошая студентка, но это не значит, что мне хочется делить тебя с ней."
                            elif Girl is StormX:
                                    ch_s "Она мне очень нравится, но какая разница?"
                            elif Girl is GwenX:
                                    ch_g "Нравится она мне или нет, это не дает тебе права спать с ней. . ."
                            else:
                                    call AnyLine(Girl,"Мы подруги, но что с того?")
                    else:
                            $ Girl.Statup("Love", 200, -20)
                            if Girl is RogueX:
                                    ch_r "Нравится она мне или нет, это не дает тебе права спать с ней."
                            elif Girl is KittyX:
                                    ch_k "Какое это имеет отношение к нашему разговору?!"
                            elif Girl is EmmaX:
                                    ch_e "Это совершенно не имеет значения!"
                            elif Girl is LauraX:
                                    ch_l "Недостаточно, чтобы делить тебя с ней."
                            elif Girl is JeanX:
                                    ch_j "Этого недостаточно."
                            elif Girl is StormX:
                                    ch_s "Боюсь, этого недостаточно."
                            elif Girl is JubesX:
                                    ch_v "Мне все равно, насколько она сексуальна!"
                            elif Girl is GwenX:
                                    ch_g "Какое это имеет отношение к нашему разговору?!"
                            elif Girl is BetsyX:
                                    ch_b "Я не вижу в твоих словах никакого смысла."
                            elif Girl is DoreenX:
                                    ch_d "Какая разница?"
                            elif Girl is WandaX:
                                    ch_w "Может и нравится нравится. . ."
                            $ Resolution -= 1

        menu:
                "Больше подобного не повторится.":
                    if Girl.Cheated:
                            $ Girl.Statup("Love", 90, 5)
                            call AnyLine(Girl,"Будет как в прошлый раз?")
                            $ Resolution -= 1
                    else:
                            $ Girl.Statup("Love", 90, 20)
                            $ Girl.FaceChange("angry")
                            $ Resolution += 2 if Resolution < 3 else 0
                            call AnyLine(Girl,"Ловлю на слове.")
                    $ Line = 0

                "Я не могу ничего обещать, она слишком горяча.":
                            $ Girl.FaceChange("angry")
                            $ Girl.Statup("Love", 200, -40)
                            $ Girl.Statup("Obed", 90, 40)
                            $ Girl.Statup("Inbt", 90, 10)
                            call AnyLine(Girl,"Тогда на этом и закончим.")
                            $ Resolution -= 2
                            $ Line = 0

                "Может, возьмем ее к нам?":
                        $ Girl.FaceChange("confused",Mouth="smile")
                        if ApprovalCheck(Girl, 2200, Bonus = B) or ApprovalCheck(Girl, 950, "L", Bonus = (B/3)):
                                $ Girl.Statup("Inbt", 90, 30)
                                $ Girl.Statup("Lust", 89, 10)
                                $ Resolution += 2
                        elif ApprovalCheck(Girl, 1500, Alt=[[DoreenX],1700], Bonus = B) or Girl.GirlLikeCheck(Other) >= 700:
                                $ Girl.Statup("Inbt", 90, 10)
                                $ Girl.Statup("Lust", 90, 5)
                        else:
                                $ Resolution -= 3
                                $ Girl.Statup("Love", 200, -25)
                                $ Girl.Statup("Inbt", 90, 10)

                        $ Girl.Statup("Obed", 90, 40)
                        if Girl is RogueX:
                                ch_r "Я не знаю, то есть, ты предлагаешь тройничек?"
                        elif Girl is KittyX:
                                ch_k "Что? Ты хочешь тройничек?"
                        elif Girl is EmmaX:
                                ch_e "Я не уверена, как реагировать на это."
                                ch_e "Ты предлагаешь тройничек?"
                        elif Girl is LauraX:
                                ch_l "Ты хочешь трахнуть нас обеих?"
                        elif Girl is JeanX:
                                ch_j "Да, возможно."
                        elif Girl is StormX:
                                ch_s "Интересное предложение. . ."
                        elif Girl is JubesX:
                                ch_v "Что? . .  В смысле. . . "
                                ch_v ". . . о чем это ты?"
                        elif Girl is GwenX:
                                ch_g "Оооох, ты думаешь, ей это понравится?"
                        elif Girl is BetsyX:
                                ch_b "Ты хочешь, чтобы я разделила тебя с ней?"
                        elif Girl is DoreenX:
                                ch_d "Ты. . . хочешь тройничек? . ."
                        elif Girl is WandaX:
                                ch_w "Значит, хочешь тройничек. . ."
                        $ Line = "threeway"

        if ApprovalCheck(Girl, 1100, "LO", Bonus = (B/2)) or Girl is GwenX:
                        $ Resolution += 1
        if len(Player.Harem) >= 3:
                        $ Resolution += 1

        if Resolution >= 5 and Line == "threeway": #she agrees to a threeway
                        if Girl.Cheated:
                                $ Girl.Statup("Love", 90, 25)
                                $ Girl.Statup("Obed", 90, 30)
                                $ Girl.Statup("Inbt", 90, 60)
                        else:
                                $ Girl.Statup("Love", 90, 50)
                                $ Girl.Statup("Obed", 90, 40)
                                $ Girl.Statup("Inbt", 90, 40)
                        if Girl is RogueX:
                                ch_r "То есть, я ловлю тебя на измене, а ты предлагаешь мне тройничек?"
                        elif Girl is KittyX:
                                ch_k "То есть, ты мне изменяешь, а потом предлагаешь тройничек?"
                        elif Girl is EmmaX:
                                ch_e "Смелый шаг. Смелость должна быть вознаграждена. . ."
                        elif Girl is LauraX:
                                ch_l "Изменяешь мне, а потом просишь тройничек?"
                                ch_l "Рискованный ход."
                        elif Girl is JeanX:
                                ch_j "Я думала, что именно -я- буду приводить других. . ."
                        elif Girl is StormX:
                                ch_s "Пожалуй, это может. . . понравится нам обоим."
                        elif Girl is JubesX:
                                ch_v "Ну, думаю, мы могли бы попробовать. . ."
                        elif Girl is GwenX:
                                ch_g "Это было бы не так уж и ужасно. . ."
                        elif Girl is BetsyX:
                                ch_b "Тебя поймали на измене, а ты просишь большего?"
                        elif Girl is DoreenX:
                                ch_d "Тебя поймали с поличным, и ты хочешь извлечь из этого выгоду для себя. . ?"
                        call AnyLine(Girl,"Может быть, я смогу с этим жить, я поговорю с "+Other.Name_tvo+".")

                        $ Line = "poly"

        elif Resolution >= 5: #she suggests a threeway
                        if Girl.Cheated:
                                $ Girl.Statup("Love", 90, 20)
                                $ Girl.Statup("Obed", 90, 10)
                                $ Girl.Statup("Inbt", 90, 100)
                        else:
                                $ Girl.Statup("Love", 90, 40)
                                $ Girl.Statup("Obed", 90, 10)
                                $ Girl.Statup("Inbt", 90, 60)
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Ты просто похотливая сучка. Похоже, я не смогу тебя приручить."
                                else:
                                    ch_r "Ты просто кобель. Похоже, я не смогу тебя приручить."
                                ch_r "Не в одиночку, по крайней мере."
                        elif Girl is KittyX:
                                ch_k "Что за бардак. Хотя, думаю, я могу поделиться тобой. . ."
                        elif Girl is EmmaX:
                                ch_e "Смелый шаг. Смелость должна быть вознаграждена. . ."
                        elif Girl is LauraX:
                                if not Player.Male:
                                    ch_l "Ты та еще штучка, но, может быть, я могла бы поделиться тобой. . ."
                                else:
                                    ch_l "Ты тот еще тип, но, может быть, я могла бы поделиться тобой. . ."
                        elif Girl is JeanX:
                                ch_j "Я думала, что именно -я- буду приводить других. . ."
                        elif Girl is StormX:
                                ch_s "Возможно, есть способ, который удовлетворит нас обоих."
                        elif Girl is JubesX:
                                ch_v "Возможно, мы могли бы сработаться. . ."
                        elif Girl is GwenX:
                                ch_g "Я не хочу потерять тебя, но, возможно, мы могли бы взять к себе? . ."
                        elif Girl is BetsyX:
                                ch_b ". . . Пожалуй, разделить тебя с кем-то может быть не такой уж и плохой идеей. . ."
                        elif Girl is DoreenX:
                                ch_d "Я думаю, может, мы могли бы обсудить это. . ."
                        elif Girl is WandaX:
                                ch_w "Ладно, твоя взяла. . ."

                        if Girl in (EmmaX,StormX):
                                call AnyLine(Girl,"Возможно, мы с "+Other.Name_tvo+" сможем что-нибудь придумать.")
                        else:
                                call AnyLine(Girl,"Может быть, мы с "+Other.Name_tvo+" что-нибудь придумаем.")
                        $ Line = "poly"

        elif Resolution >= 2: #she agrees to forgive you
                    if Line == "threeway":
                            #you've asked for a threeway, but she knocked it down
                            $ Girl.Statup("Obed", 80, 10)
                            if Girl is RogueX:
                                    ch_r "Не пытайся меня обхитрить."
                            elif Girl is KittyX:
                                    ch_k "Подумай головой. . ."
                            elif Girl is EmmaX:
                                    ch_e "Я ценю твою инициативу, но уж точно не здравый смысл. . ."
                            elif Girl is LauraX:
                                    ch_l "Как будто бы это случится. . ."
                            elif Girl is JeanX:
                                    if not Player.Male:
                                        ch_j "Нет, ты этого не заслужила."
                                    else:
                                        ch_j "Нет, ты этого не заслужил."
                            elif Girl is StormX:
                                    if not Player.Male:
                                        ch_s "Не думаю, что ты готова к таким отношениям."
                                    else:
                                        ch_s "Не думаю, что ты готов к таким отношениям."
                            elif Girl is JubesX:
                                    ch_v "Меня это сейчас не интересует!"
                            elif Girl is GwenX:
                                    ch_g "Эм, я совсем не хочу иметь с ней ничего общего. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я бы предпочла не иметь с ней таких отношений."
                            elif Girl is DoreenX:
                                    ch_d "Слушай, я вроде как однолюб. . ."
                            elif Girl is WandaX:
                                    ch_w "Я не уверена, мне вроде как начинают нравится нынешние отношения. . ."
                    $ Girl.FaceChange("sadside")
                    if Girl.Cheated:
                            $ Girl.Statup("Obed", 80, 15)
                            if Girl is RogueX:
                                    if not Player.Male:
                                        ch_r "Я дала тебе шанс поступить правильно, а ты снова все испортила."
                                    else:
                                        ch_r "Я дала тебе шанс поступить правильно, а ты снова все испортил."
                                    ch_r "Не знаю, сколько еще раз я смогу это вытерпеть."
                            elif Girl is KittyX:
                                    ch_k "Ты слишком часто все портишь, [KittyX.Petname]. . ."
                            elif Girl is EmmaX:
                                    ch_e "Почему я все еще терплю тебя. . ."
                            elif Girl is LauraX:
                                    ch_l "Мне уже это надоело. . ."
                            elif Girl is JeanX:
                                    ch_j "Я не дам тебе больше возможности все испортить."
                            elif Girl is StormX:
                                    if not Player.Male:
                                        ch_s "Ты слишком много раз предавала мое доверие."
                                    else:
                                        ch_s "Ты слишком много раз предавал мое доверие."
                            elif Girl is JubesX:
                                    if not Player.Male:
                                        ch_v "Ты слишком много играла с моими чувствами. . ."
                                    else:
                                        ch_v "Ты слишком много играл с моими чувствами. . ."
                            elif Girl is GwenX:
                                    if not Player.Male:
                                        ch_g "Ты слишком много раз делала это. . ."
                                    else:
                                        ch_g "Ты слишком много раз делал это. . ."
                            elif Girl is BetsyX:
                                    ch_b ". . . тебе не получится меня приручить. . ."
                            elif Girl is DoreenX:
                                    ch_d "Мне. . . пора перестать с этим мириться. . ."
                            elif Girl is WandaX:
                                    ch_w "Я чувствую, что скоро придет конец нашим отношениям. . ."
                    else:
                            $ Girl.Statup("Obed", 80, 30)
                            if Girl is RogueX:
                                    if not Player.Male:
                                        ch_r "Ты предала мое доверие, [RogueX.Petname]."
                                    else:
                                        ch_r "Ты предал мое доверие, [RogueX.Petname]."
                                    ch_r "Не дай этому повториться."
                            elif Girl is KittyX:
                                    if not Player.Male:
                                        ch_k "Ты ранила мои чувства, [KittyX.Petname]. . ."
                                    else:
                                        ch_k "Ты ранил мои чувства, [KittyX.Petname]. . ."
                                    ch_k "Прошу, больше не причиняй мне боль."
                            elif Girl is EmmaX:
                                    ch_e "Я предупреждаю тебя, не повторяй свои ошибки."
                            elif Girl is LauraX:
                                    if not Player.Male:
                                        ch_l "Ты ходишь по тонкому льду, пожружка."
                                    else:
                                        ch_l "Ты ходишь по тонкому льду, дружок."
                            elif Girl is JeanX:
                                    ch_j "На этот раз я прощаю тебя, но не привыкай."
                            elif Girl is StormX:
                                    if not Player.Male:
                                        ch_s "Ты предала мое доверие, [StormX.Petname]."
                                    else:
                                        ch_s "Ты предал мое доверие, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Мне не нравятся подобные игры. . ."
                            elif Girl is GwenX:
                                    ch_g "Вот почему я пыталась найти отомэ-игру!"
                            elif Girl is BetsyX:
                                    ch_b "Я проглочу свою гордость на этот раз, но не доводи до такого больше."
                            elif Girl is DoreenX:
                                    ch_d "Я могу. . . дать тебе еще один шанс. . ."
                            elif Girl is WandaX:
                                    ch_w "Мы можем попробовать еще раз. . ."

        else:
                    #she doesn't agree to forgive you
                    $ Girl.FaceChange("angry")
                    if Line == "threeway":
                        $ Girl.Statup("Obed", 80, 10)
                        if Girl is RogueX:
                                ch_r "Поверить не могу, что ты предлагаешь секс -втроём!-"
                        elif Girl is KittyX:
                                ch_k "Серьезно? Тройничек?!"
                        elif Girl is EmmaX:
                                ch_e "Смелый шаг. Иногда одной смелости мало. . ."
                        elif Girl is LauraX:
                                ch_l "Тройничек?"
                        elif Girl is JeanX:
                                ch_j "Ты серьезно надеешься на вознагождение?"
                        elif Girl is StormX:
                                ch_s "Не думаю, что ты готов к таким отношениям."
                        elif Girl is JubesX:
                                ch_v "Ты слишком давишь."
                        elif Girl is GwenX:
                                ch_g "Она мне очень не нравится. . ."
                        elif Girl is BetsyX:
                                ch_b "Это совершенно неприемлемо."
                        elif Girl is DoreenX:
                                ch_d "Ни за что."
                        elif Girl is WandaX:
                                ch_w "Не-а."
                    if Girl.Cheated:
                        $ Girl.Statup("Obed", 90, -50)
                        $ Girl.Statup("Inbt", 90, 20)
                        if Girl is RogueX:
                                ch_r "Я слишком много раз прощала тебя."
                                ch_r "Извини, [RogueX.Petname], но это конец."
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Ты уже не кажешься такой милой. . ."
                                else:
                                    ch_k "Ты уже не кажешься таким милым. . ."
                                ch_k "Все кончено."
                        elif Girl is EmmaX:
                                ch_e "Не думаю, что хочу продолжать эти игры."
                                ch_e "Все кончено."
                        elif Girl is LauraX:
                                if not Player.Male:
                                    ch_l "Я надеялась, что смогу верить тебе, но ты опять все испортила. . ."
                                else:
                                    ch_l "Я надеялась, что смогу верить тебе, но ты опять все испортил. . ."
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Я дала тебе шанс, но ты все испортила."
                                else:
                                    ch_j "Я дала тебе шанс, но ты все испортил."
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "Ты слишком много раз предавала мое доверие."
                                else:
                                    ch_s "Ты слишком много раз предавал мое доверие."
                        elif Girl is JubesX:
                                if not Player.Male:
                                    ch_v "Ты слишком много играла с моими чувствами!"
                                else:
                                    ch_v "Ты слишком много играл с моими чувствами!"
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Ты уже достаточно получала \"второй шанс\". . ."
                                else:
                                    ch_g "Ты уже достаточно получал \"второй шанс\". . ."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ты просто невыносима."
                                else:
                                    ch_b "Ты просто невыносим."
                        elif Girl is DoreenX:
                                ch_d "У тебя было слишком много \"второх шансов\"!"
                        elif Girl is WandaX:
                                ch_w "Мы уже слишком много раз пытались все изменить. . ."
                    else:
                        $ Girl.Statup("Obed", 90, -50)
                        $ Girl.Statup("Inbt", 90, 10)
                        if Girl is RogueX:
                                ch_r "Я больше не думаю, что могу тебе доверять, [RogueX.Petname]."
                                ch_r "Больше нет никаких \"нас\"."
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Ты сделала мне больно. Я больше так не могу."
                                else:
                                    ch_k "Ты сделал мне больно. Я больше так не могу."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Ты потеряла мое доверие. Все кончено."
                                else:
                                    ch_e "Ты потерял мое доверие. Все кончено."
                        elif Girl is LauraX:
                                ch_l "Я не могу тебе доверять. С меня хватит."
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Я дала тебе шанс, но ты его упустила."
                                else:
                                    ch_j "Я дала тебе шанс, но ты его упустил."
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "Ты предала мое доверие, [StormX.Petname]."
                                else:
                                    ch_s "Ты предал мое доверие, [StormX.Petname]."
                        elif Girl is JubesX:
                                ch_v "Мне не нравятся подобные игры!"
                        elif Girl is GwenX:
                                ch_g "Вот почему я искала отоме-игру!"
                        elif Girl is BetsyX:
                                ch_b "Это просто неприемлемо."
                        elif Girl is DoreenX:
                                ch_d "Я никак не могу простить такое!"
                        elif Girl is WandaX:
                                ch_w "После всего, что было, я не могу тебе доверять. . ."

                    $ Girl.AddWord(1,0,0,"ex",0) #adds "ex" to traits
                    if Girl in Player.Harem:
                            $ Player.Harem.remove(Girl)
                    $ Girl.AddWord(1,0,"angry",0,0)

#        $ Girl.DrainWord("saw with " + Other,0,0,1)      #removes "saw with Kitty" from traits

        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                #removes "saw with Rogue" from traits
                Girl.DrainWord("saw with "+BX.Tag,0,0,1)

        if Line == "poly":
                $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0)    #adds "poly Kitty" to traits
                $ Girl.AddWord(1,0,0,"ask "+Other.Tag,0)     #adds "ask Kitty" to traits
        else:
                $ Girl.GLG(Other,1000,-50,1)   #$ RogueX.LikeKitty -= 50

        if "ex" in Girl.Traits:
            $ Girl.Break[0] = 5 + Girl.Break[1] + Girl.Cheated
        $ Girl.Cheated += 1

        #aftermath
        menu:
                "Хорошо, что мы смогли все уладить." if Girl in Player.Harem:
                        $ Girl.FaceChange("sad")
                        if Resolution >= 3:
                                $ Girl.Statup("Love", 90, 10)
                                $ Girl.Statup("Obed", 90, 5)
                                if Girl is RogueX:
                                        ch_r "Согласна, [RogueX.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Ага, [KittyX.Petname]. . ."
                        else:
                                $ Girl.Statup("Love", 90, 5)
                                if Girl is RogueX:
                                        ch_r "Да, посмотрим, что из этого выйдет, [RogueX.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Конечно, [KittyX.Petname]. . ."
                        if Girl is EmmaX:
                                ch_e "Да, замечательно."
                        elif Girl is LauraX:
                                ch_l "Да, конечно."
                        elif Girl is JeanX:
                                ch_j "Верно."
                        elif Girl is StormX:
                                ch_s "Посмотрим, [StormX.Petname], правильное ли я приняла решение."
                        elif Girl is JubesX:
                                ch_v "Ага, возможно. . ."
                        elif Girl is GwenX:
                                $ Girl.FaceChange("smile")
                                ch_g "Ага!"
                        elif Girl is BetsyX:
                                ch_b "Пожалуй. . ."
                        elif Girl is DoreenX:
                                ch_d "Наверное. . ."
                        elif Girl is WandaX:
                                ch_w "Ага. . ."

                "Хочешь немного пошалить?" if Girl in Player.Harem and not Taboo:
                        if Girl.Obed + Girl.Inbt >= (1.5 * Girl.Love) or Girl.Lust >= 70:
                            #(Obed + Inbt) >= (1.5 * Love) or Lust >= 70
                            $ Girl.FaceChange("sly",Eyes="side")
                            $ Girl.Statup("Love", 90, 20)
                            $ Girl.Statup("Obed", 90, 10)
                            $ Girl.Statup("Inbt", 90, 10)
                            if Girl is StormX:
                                    if not Player.Male:
                                        ch_s "Ты неисправима, [StormX.Petname]."
                                    else:
                                        ch_s "Ты неисправим, [StormX.Petname]."
                            else:
                                    call AnyLine(Girl,"Конечно, как скажешь.")
                            call SMenu # call expression Girl.Tag + "_SMenu" #call Rogue_SexMenu
                        else:
                            $ Girl.FaceChange("sad")
                            $ Girl.Statup("Love", 90, -10)
                            $ Girl.Statup("Obed", 90, -10)
                            if Girl is RogueX:
                                    ch_r "Еще слишком рано, [RogueX.Petname]."
                            elif Girl is KittyX:
                                    ch_k "Ты слишком спешишь, [KittyX.Petname]. . ."
                            elif Girl is EmmaX:
                                    ch_e "Ох, ты хочешь слишком многого."
                            elif Girl is LauraX:
                                    ch_l "Ага, но не сейчас."
                            elif Girl is JeanX:
                                    ch_j "Может в другой раз."
                            elif Girl is StormX:
                                    ch_s "Посиди и обдумай свои действия, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Уж точно не сейчас. . ."
                            elif Girl is GwenX:
                                    ch_g "У меня болит голова."
                            elif Girl is BetsyX:
                                    ch_b "Боюсь, что нет."
                            elif Girl is DoreenX:
                                    ch_d "Я. . . пока не готова. . ."
                            elif Girl is WandaX:
                                    ch_w "Я так не думаю. . ."

                "Мне очень жаль, что ничего не вышло." if Girl not in Player.Harem:
                            $ Girl.FaceChange("sad")
                            $ Girl.Statup("Love", 90, 10)
                            if Girl is RogueX:
                                    ch_r "Мне тоже, [RogueX.Petname]."
                            elif Girl is KittyX:
                                    ch_k "Да, мне тоже, [KittyX.Petname]. . ."
                            elif Girl is EmmaX:
                                    ch_e "Да, в конце концов. . . ты это переживешь."
                            elif Girl is LauraX:
                                    ch_l "Ага."
                            elif Girl is JeanX:
                                    ch_j "Конечно, как скажешь."
                            elif Girl is StormX:
                                    ch_s "Да, жаль. . ."
                            elif Girl is JubesX:
                                    ch_v "Ага, возможно. . ."
                            elif Girl is GwenX:
                                    ch_g "Ага, -тебе- жаль. Это не тебе нужно придумывать, чем здесь заняться."
                            elif Girl is BetsyX:
                                    ch_b "Да, согласна."
                            elif Girl is DoreenX:
                                    ch_d "Ага. . . жаль. . ."
                            elif Girl is WandaX:
                                    ch_w "Ага, мне тоже. . ."

                "Может, потрахаемся напоследок?" if Girl not in Player.Harem and not Taboo:
                        if Girl.Obed + Girl.Inbt >= (1.5 * Girl.Love) or Girl.Lust >= 70 or Girl is WandaX:
                            #(Obed + Inbt) >= (1.5 * Love) or Lust >= 70
                            $ Girl.FaceChange("angry",Eyes="side")
                            $ Girl.Statup("Obed", 90, 10)
                            $ Girl.Statup("Inbt", 90, 10)
                            if Girl is StormX:
                                    if not Player.Male:
                                        ch_s "Ты неисправима, [StormX.Petname]."
                                    else:
                                        ch_s "Ты неисправим, [StormX.Petname]."
                            elif Girl is BetsyX:
                                    if not Player.Male:
                                        ch_b "Ох, ты неисправима."
                                    else:
                                        ch_b "Ох, ты неисправим."
                            elif Girl is WandaX:
                                    ch_w "А знаешь что? Давай."
                            else:
                                    call AnyLine(Girl,"Конечно, как скажешь.")
                            $ Girl.DrainWord("angry",0,1)
                            call SMenu # call expression Girl.Tag + "_SMenu" #call Rogue_SMenu
                            $ Girl.AddWord(1,0,"angry",0,0) #adds "angry" to daily
                        else:
                            $ Girl.FaceChange("angry")
                            $ Girl.Statup("Love", 90, -20)
                            $ Girl.Statup("Obed", 90, -10)
                            if Girl is RogueX:
                                    ch_r "Ты должно быть шутишь."
                            elif Girl is KittyX:
                                    ch_k "Мечтай, [KittyX.Petname]. . ."
                            elif Girl is EmmaX:
                                    ch_e "Ох, ты хочешь слишком многого."
                            elif Girl is LauraX:
                                    ch_l "Ага, но не сейчас."
                            elif Girl is JeanX:
                                    ch_j "Может в другой раз."
                            elif Girl is StormX:
                                    ch_s "Посиди и обдумай свои действия, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Уж точно не сейчас. . ."
                            elif Girl is GwenX:
                                    ch_g "У меня болит голова."
                            elif Girl is BetsyX:
                                    ch_b "Боюсь, что нет."
                            elif Girl is DoreenX:
                                    ch_d "Я. . . не готова. . ."

                "Дай мне знать, если передумаешь." if Girl not in Player.Harem:
                            $ Girl.FaceChange("angry",Eyes="side")
                            $ Girl.Statup("Love", 90, -5)
                            $ Girl.Statup("Obed", 90, 10)
                            if Girl is RogueX:
                                    ch_r "Ага, как только, так сразу."
                            elif Girl is KittyX:
                                    ch_k "Ох, конечно."
                            elif Girl is EmmaX:
                                    if not Player.Male:
                                        ch_e "Ох, я уверена, ты будешь первой, кто об этом узнает."
                                    else:
                                        ch_e "Ох, я уверена, ты будешь первым, кто об этом узнает."
                            elif Girl is LauraX:
                                    ch_l "Угу."
                            elif Girl is JeanX:
                                    ch_j "Ох, конечно."
                            elif Girl is StormX:
                                    ch_s "Уверена, я так и сделаю, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Конечно, как скажешь. . ."
                            elif Girl is GwenX:
                                    ch_g "Посмотрим, через неделю или две. . ."
                            elif Girl is BetsyX:
                                    ch_b "Время покажет. . ."
                            elif Girl is DoreenX:
                                    ch_d "Я. . .  хорошо все обдумаю. . ."
                            elif Girl is WandaX:
                                    ch_w "О, конечно."

                "Ладно, тогда как-нибудь увидимся.":
                            $ Girl.FaceChange("confused")

        if Girl is RogueX:
                ch_r "Мне нужно немного побыть одной, [RogueX.Petname]. Увидимся позже."
        elif Girl is KittyX:
                ch_k "Мне нужно побыть наедине с собой, Увидимся."
        elif Girl is EmmaX:
                ch_e "Теперь мне нужно немного побыть одной"
        elif Girl is LauraX:
                ch_l "Хорошо, пока."
        #no Jean
        elif Girl is StormX:
                ch_s "Уверена, наши пути еще пересекутся, [StormX.Petname]."
        elif Girl is JubesX:
                ch_v "Я собираюсь. . . свалить отсюда. . ."
        elif Girl is GwenX:
                ch_g "Я пойду. . ."
        elif Girl is BetsyX:
                ch_b "Если это все, то я, пожалуй, откланяюсь."
        elif Girl is DoreenX:
                ch_d "Сейчас мне нужно немного времени побыть одной. . ."
        elif Girl is WandaX:
                ch_w "Дай мне немного времени. Мне нужно кое-что обдумать."

        $ Round -= 10 if Round > 10 else Round

        if bg_current == Girl.Home:
                #remove Rogue from the scene (or the player)
                $ bg_current = "bg player"
                jump Misplaced
        else:
                call Remove_Girl(Girl)
        return

# end Cheated on the Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start No Fapping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label NoFap(Girl=0,TabStore=Taboo,Cnt=0): #rkeljsvgbdw
        # called when you ask them not to fap from the romance menu
        # call NoFap(Girl)

        $ Taboo = 0
        ch_p "О твоей мастурбации в свободное время. . ."

        if "askedfap" in Girl.DailyActions:
                #if it's not the first time you've asked today. . .
                if "nofap" in Girl.Traits:
                        call AnyLine(Girl,"Я уже поняла.")
                else:
                        call AnyLine(Girl,"Перестань донимать меня этим.")

        elif "askedfap" in Girl.History:
                #if it's not the first time you asked. . .
                if not ApprovalCheck(Girl, 800):
                        #rude response
                        $ Girl.FaceChange("angry",2,Eyes="surprised")
                        $ Girl.Statup("Love", 80, -1)
                        $ Girl.Statup("Obed", 50, 1)
                        $ Girl.Statup("Obed", 80, 1)
                        $ Girl.Statup("Inbt", 30, -1)
                        $ Girl.Statup("Inbt", 30, 3, 1)
                        if Girl is RogueX:
                                ch_r "Я совсем не хочу говорить об этом снова. . ."
                        elif Girl is KittyX:
                                ch_k "Это не совсем уместно. . . "
                        elif Girl is EmmaX:
                                ch_e "Я бы предпочла не обсуждать это снова. . ."
                        elif Girl is LauraX:
                                ch_l "Хмм, Я не хочу снова заводить этот разговор."
                        elif Girl is JeanX:
                                ch_j "Мы уже говорили об этом, ты с головой не дружишь."
                        elif Girl is StormX:
                                ch_s "Это, по правде говоря, не твое дело, [StormX.Petname]."
                        elif Girl is JubesX:
                                ch_v "Тебе, эм, нужно перестать спрашивать. . ."
                        elif Girl is GwenX:
                                ch_g "Тебе нужно найти новое хобби."
                        elif Girl is BetsyX:
                                ch_b "Это ужасно неуместная тема."
                        elif Girl is DoreenX:
                                ch_d "Мы можем. . . не говорить об этом?"
                        elif Girl is WandaX:
                                ch_w "Заткнись уже."
                        $ Girl.FaceChange("angry",1)
                else:
                        #neutral response
                        $ Girl.Statup("Obed", 60, 2)
                        $ Girl.Statup("Obed", 90, 1)
                        $ Girl.Statup("Inbt", 60, 1)
                        $ Girl.Statup("Lust", 50, 1)
                        $ Girl.FaceChange("confused",1)
                        if Girl is EmmaX:
                                ch_e "О? Снова?"
                        elif Girl is LauraX:
                                ch_l "Да?"
                        elif Girl is StormX:
                                ch_s "О, что такое, [StormX.Petname]?"
                        elif Girl is BetsyX:
                                ch_b "Снова поднимаешь эту тему?"
                        else: #Rogue, Kitty, Jean
                                $ Girl.FaceChange("confused",2)
                                call AnyLine(Girl,"Эм, да, что ты хочешь сказать?")

        else:
                #if this is the first time you've asked her. . .
                if not ApprovalCheck(Girl, 800):
                        #rude response
                        $ Girl.FaceChange("angry",2,Eyes="surprised")
                        $ Girl.Statup("Love", 90, -5)
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Obed", 80, 1)
                        $ Girl.Statup("Inbt", 30, -1)
                        $ Girl.Statup("Inbt", 30, 3, 1)
                        if Girl is RogueX:
                                ch_r "Тебе не стоит беспокоиться о личном времени девушки."
                        elif Girl is KittyX:
                                ch_k "Я, эм. . . "
                                extend "эй! Это не твое дело!"
                        elif Girl is EmmaX:
                                ch_e "Чем я занимаюсь наедине с собой-"
                                ch_e "Мое личное дело."
                        elif Girl is LauraX:
                                ch_l "Хм, я не хочу об этом говорить."
                        elif Girl is JeanX:
                                ch_j ". . ."
                                ch_j "Почему ты спрашиваешь о моих личных делах?"
                        elif Girl is StormX:
                                ch_s ". . ."
                                ch_s "Я не совсем понимаю, какое тебе до этого дело, [StormX.Petname]."
                        elif Girl is JubesX:
                                ch_v "Я. . ."
                                ch_v "Что? Какое тебе до этого дело?!"
                        elif Girl is GwenX:
                                ch_g "Эй! Я не буду это обсуждать с тобой!"
                        elif Girl is BetsyX:
                                ch_b ". . . это неподходящая тема для обсуждения!"
                        elif Girl is DoreenX:
                                $ Girl.FaceChange("surprised",2)
                                ch_d "Что?! Ты. . . правда хочешь поговорить о ТАКОМ? . ."
                        elif Girl is WandaX:
                                ch_w "Мы не настолько близки, чтобы это обсуждать. . ."
                        $ Girl.FaceChange("angry",1)
                elif not ApprovalCheck(Girl, 500, "I"): # or RogueX.SEXP <= 30?
                        #shy response
                        $ Girl.Statup("Love", 90, -5)
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Obed", 80, 1)
                        $ Girl.Statup("Inbt", 30, -1)
                        $ Girl.Statup("Inbt", 30, 3, 1)
                        $ Girl.Statup("Lust", 50, 3)
                        if Girl is RogueX:
                                $ Girl.FaceChange("surprised",2)
                                ch_r "Я. . эм. . Если честно, я таким не занимаюсь. . ."
                        elif Girl is KittyX:
                                $ Girl.FaceChange("surprised",2)
                                ch_k "О, эм, я подобным не занимаюсь. . ."
                        elif Girl is EmmaX:
                                $ Girl.FaceChange("confused",1)
                                ch_e "Я не думаю, что тебя это касается. . ."
                        elif Girl is LauraX:
                                $ Girl.FaceChange("surprised",2)
                                ch_l "Эм. . . да?"
                        elif Girl is JeanX:
                                ch_j "Ну, смотри.  .  . это не твое дело."
                        elif Girl is StormX:
                                ch_s ". . ."
                                ch_s "Я не совсем понимаю, какое тебе до этого дело, [StormX.Petname]."
                        elif Girl is JubesX:
                                ch_v "Я. . ."
                                ch_v "Что? Эм. . . Я не хочу об этом говорить."
                        elif Girl is GwenX:
                                ch_g "Я. . . эм. . таким не занимаюсь. . . а ты?"
                        elif Girl is BetsyX:
                                ch_b ". . . Я бы предпочла не обсуждать свои привычки."
                        elif Girl is DoreenX:
                                $ Girl.FaceChange("surprised",2)
                                ch_d "Я, эм. . . таким не занимаюсь, эм. . ."
                        elif Girl is WandaX:
                                ch_w "Послушай, это только мое дело."
                elif ApprovalCheck(Girl, 500, "O"):
                        #submissive response
                        $ Girl.Statup("Obed", 90, 5)
                        $ Girl.Statup("Inbt", 50, 2)
                        $ Girl.Statup("Inbt", 80, 1)
                        $ Girl.Statup("Lust", 50, 5)
                        $ Girl.FaceChange("confused",1)
                        if Girl in(EmmaX,StormX,BetsyX):
                                call AnyLine(Girl,"Что конкретно ты хочешь спросить?")
                        else: #Rogue, Kitty, Laura
                                call AnyLine(Girl,"И что ты хочешь спросить?")
                else:
                        #neutral response
                        $ Girl.Statup("Obed", 90, 4)
                        $ Girl.Statup("Inbt", 90, 3)
                        $ Girl.Statup("Lust", 50, 3)
                        $ Girl.FaceChange("confused",1)
                        if Girl is EmmaX:
                                ch_e "Ох? И что ты хочешь сказать?"
                        elif Girl in (LauraX,JeanX):
                                call AnyLine(Girl,"Да?")
                        elif Girl is StormX:
                                ch_s ". . ."
                                ch_s "Что ты хочешь узнать?"
                        elif Girl is BetsyX:
                                ch_b ". . . я выслушаю тебя. . ."
                        else: #Rogue, Kitty
                                $ Girl.FaceChange("confused",2)
                                call AnyLine(Girl,"Эм, да, что ты хочешь сказать?")
        #end intro check. . .

        menu:
            extend ""
            "Мне хотелось бы, чтобы ты этим не занималась." if "nofap" not in Girl.Traits:
                    if "askedfap" not in Girl.DailyActions:
                            $ Girl.Statup("Obed", 200, 2)
                            $ Girl.Statup("Inbt", 90, 1)
                    if ApprovalCheck(Girl, 1400, "LO"):
                            #loving response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 4)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 3)
                            $ Girl.FaceChange("bemused",2)
                            if Girl is RogueX:
                                    ch_r "Ну, если для тебя это так важно. . ."
                            elif Girl is KittyX:
                                    ch_k "Тебя действительно заботит что-то подобное?"
                                    ch_k "Ладно."
                            elif Girl is EmmaX:
                                    ch_e "[EmmaX.Petname], тебя это так беспокоит?"
                                    ch_e "Ладно, я могу обойтись и без этого. . ."
                            elif Girl is LauraX:
                                    ch_l "Тебя действительно это так беспокоит? . ."
                                    ch_l "Думаю, я могу остановиться. . ."
                            elif Girl is JeanX:
                                    ch_j "Хмм. . ."
                                    ch_j "Думаю, мы могли бы попробовать. . ."
                                    ch_j "Но тебе лучше бы загладить свою вину."
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Ладно, если ты действительно веришь, что сможешь удовлетворить мои потребности, [StormX.Petname]. . ."
                            elif Girl is JubesX:
                                    ch_v "Нууу. . ."
                                    ch_v "У меня есть потребности. . ."
                                    ch_v "Тебе придется их. . . удовлетворять."
                            elif Girl is GwenX:
                                    ch_g "О, хочешь, чтобы я была только для тебя, да?"
                                    if not Player.Male:
                                        ch_g "Тогда мне нужно, чтобы ты была всегда недалеко. . ."
                                    else:
                                        ch_g "Тогда мне нужно, чтобы ты был всегда недалеко. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я. . . пожалуй, могла бы воздержаться от этого. . ."
                                    ch_b "Однако мне может. . . понадобиться твоя помощь."
                            elif Girl is DoreenX:
                                    ch_d "Н-ну. . ."
                                    ch_d "Если это так важно для тебя. . ."
                                    ch_d "Я согласна, но, возможно, мне понадобится твоя помощь."
                            elif Girl is WandaX:
                                    ch_w "Странная просьба. . ."
                                    ch_w "Но ладно, давай попробуем."
                                    ch_w "Только постарайся всегда быть на связи."
                            $ Girl.FaceChange("bemused",1)
                    elif ApprovalCheck(Girl, 1600) and not ApprovalCheck(Girl, 500, "I") and Girl is not JeanX:
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("bemused",2,Eyes="side")
                            if Girl is RogueX:
                                    ch_r "Не то, чтобы я таким занималась, но. . . ладно."
                            elif Girl is KittyX:
                                    ch_k "Я не. . . ну ладно, не буду."
                            elif Girl is EmmaX:
                                    ch_e "Полагаю, если для тебя это так важно. . ."
                            elif Girl is LauraX:
                                    ch_l "Ладно, если для тебя это так важно. . ."
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Я не совсем понимаю, какое тебе до этого дело, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "На самом деле я. . ."
                                    ch_v "Ладно, посмотрим. . ."
                            elif Girl is GwenX:
                                    ch_g "Хорошо. . . не то чтобы я таким занималась, но если бы занималась. . . что?"
                            elif Girl is BetsyX:
                                    ch_b "Я . . . пожалуй, я могу держать себя в руках. . ."
                            elif Girl is DoreenX:
                                    ch_d "Н-ну, наверное, можно. . ."
                            elif Girl is WandaX:
                                    ch_w "Если бы я этим занималась, то я бы согласилась."
                                    ch_w "Но я не занимаюсь подобным."
                            $ Girl.FaceChange("bemused",1)
                    elif ApprovalCheck(Girl, 700, "O",Alt=[[JeanX],800]):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 70, 5)
                            $ Girl.FaceChange("sly",1)
                            call AnyLine(Girl,"Да, "+Girl.Petname+".")
                    elif not ApprovalCheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, -5)
                                    $ Girl.Statup("Obed", 90, -3)
                                    $ Girl.Statup("Inbt", 90, 3)
                            $ Girl.FaceChange("angry",2)
                            if Girl is KittyX:
                                    ch_k "Я- весь этот разговор неуместен!"
                            elif Girl in (EmmaX,JeanX):
                                    if not Player.Male:
                                        call AnyLine(Girl,"Если честно, мне все равно \"чего бы ты хотела.\"")
                                    else:
                                        call AnyLine(Girl,"Если честно, мне все равно \"чего бы ты хотел.\"")
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Меня не интересует твое мнение по этому поводу, [StormX.Petname]."
                            elif Girl is DoreenX:
                                    ch_d "Н-ну, я этим не занимаюсь, так что. . ."
                            else: #Rogue, Laura
                                    if not Player.Male:
                                        call AnyLine(Girl,"А я бы хотела, чтобы ты не лезла в мои дела.")
                                    else:
                                        call AnyLine(Girl,"А я бы хотела, чтобы ты не лез в мои дела.")
                            $ Girl.FaceChange("angry",1)
                            $ Cnt = 1
                    else:
                            #no
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, -1)
                                    $ Girl.Statup("Obed", 70, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.FaceChange("sly",1)
                            if Girl is RogueX:
                                    ch_r "Боюсь, что нет, [RogueX.Petname]."
                            elif Girl is KittyX:
                                    ch_k "Извини, но нет. Я хочу этим заниматься."
                            elif Girl is EmmaX:
                                    ch_e "Нет, думаю, я продолжу этим заниматься. . . и часто."
                            elif Girl is LauraX:
                                    ch_l "Извини, [LauraX.Petname], У меня, все таки, есть потребности."
                            elif Girl is JeanX:
                                    $ Girl.FaceChange("confused",1)
                                    ch_j "Эм. . . нет?"
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Я бы предпочла не обсуждать это, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Эм, это было бы очень неудобно для меня, так что. . ."
                                    ch_v "Нет."
                            elif Girl is GwenX:
                                    ch_g "Я. . . не хочу!"
                            elif Girl is BetsyX:
                                    ch_b "Занимаюсь я этим или нет, это мое личное дело."
                            elif Girl is DoreenX:
                                    ch_d "Эм, не лезь в мои дела. . ."
                            elif Girl is WandaX:
                                    ch_w "Заткнись."
                            $ Cnt = 1
                    if not Cnt:
                            $ Girl.AddWord(1,0,0,"nofap")  #adds "nofap" tag to traits
            # end "ask nicely"

            "Не мастурбируй без моего разрешения." if "nofap" not in Girl.Traits:
                    if "askedfap" not in Girl.DailyActions:
                            $ Girl.Statup("Obed", 200, 3)
                    if ApprovalCheck(Girl, 600, "O"):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 3)
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                                    $ Girl.Statup("Lust", 70, 5)
                            $ Girl.FaceChange("sly")
                            call AnyLine(Girl,"Да, "+Girl.Petname+".")
                    elif ApprovalCheck(Girl, 1200, "LO"):
                            #positive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 4)
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 3)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("bemused",1)
                            if Girl is RogueX:
                                    ch_r "Ну, если это так много значит для тебя. . ."
                            elif Girl is KittyX:
                                    ch_k "Думаю, я могла бы -\"не мастурбировать-\". . ."
                            elif Girl is EmmaX:
                                    if not Player.Male:
                                        ch_e "Хорошо, ты такая властная. . ."
                                    else:
                                        ch_e "Хорошо, ты такой властный. . ."
                                    ch_e "Думаю, я смогу вытерпеть. . ."
                            elif Girl is LauraX:
                                    ch_l "Думаю, я справлюсь."
                            elif Girl is JeanX:
                                    ch_j "Хмм. . ."
                                    ch_j "Думаю, мы могли бы попробовать. . ."
                                    ch_j "Но тебе лучше бы загладить свою вину."
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Что ж, я могу попробовать, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Нууу. . ."
                                    ch_v "У меня есть потребности. . ."
                                    ch_v "Тебе придется их. . . удовлетворять."
                            elif Girl is GwenX:
                                    ch_g "О, хочешь, чтобы я была только для тебя, да?"
                                    if not Player.Male:
                                        ch_g "Тогда мне нужно, чтобы ты была всегда недалеко. . ."
                                    else:
                                        ch_g "Тогда мне нужно, чтобы ты был всегда недалеко. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я. . . пожалуй, могу воздержаться от этого. . ."
                                    ch_b "Или воспользоваться твоей помощью. . ."
                            elif Girl is DoreenX:
                                    ch_d "Н-ну. . ."
                                    ch_d "Если это так важно для тебя. . ."
                                    ch_d "Я согласна, но мне может понадобиться твоя помощь."
                            elif Girl is WandaX:
                                    ch_w "Если бы я этим занималась, то я бы согласилась."
                                    ch_w "Но я не занимаюсь подобным."
                    elif not ApprovalCheck(Girl, 500, "I"):
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("bemused",2,Eyes="side")
                            if Girl is RogueX:
                                    ch_r "Я вообще этим не занимаюсь. . ."
                            elif Girl is KittyX:
                                    if not Player.Male:
                                        ch_k "Девочки этим не занимаются. Но даже если бы я таким занималась, ты слишком груба."
                                    else:
                                        ch_k "Девочки этим не занимаются. Но даже если бы я таким занималась, ты слишком груб."
                            elif Girl is EmmaX:
                                    ch_e "Я не думаю, что тебя это касается."
                            elif Girl is LauraX:
                                    ch_l "Не интересует."
                            elif Girl is JeanX:
                                    ch_j "Мне не нравится твой тон. . ."
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Не говори со мной в таком тоне, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Я, эм, в этом не уверена. . ."
                            elif Girl is GwenX:
                                    ch_g "Я. . . эй, не проси меня о таком!"
                            elif Girl is BetsyX:
                                    ch_b "Мне некомфортно об этом говорить."
                            elif Girl is DoreenX:
                                    ch_d "Н-ну, я подумаю. . ."
                            elif Girl is WandaX:
                                    ch_w "Ну не знаю, может, мне и правда стоило бы так делать."
                                    ch_w "Если бы я этим занималась."
                            $ Girl.FaceChange("normal",1)
                            $ Cnt = 1
                    elif not ApprovalCheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 70, -5)
                                    $ Girl.Statup("Love", 90, -5)
                                    $ Girl.Statup("Obed", 60, -3)
                                    $ Girl.Statup("Obed", 90, -3)
                                    $ Girl.Statup("Inbt", 90, 3)
                            $ Girl.FaceChange("angry",2)
                            if Girl is RogueX:
                                    if not Player.Male:
                                        ch_r "Пошла ты, я не буду спрашивать твоего разрешения."
                                    else:
                                        ch_r "Пошел ты, я не буду спрашивать твоего разрешения."
                            elif Girl is KittyX:
                                    ch_k "Я- весь этот разговор неуместен!"
                            elif Girl is EmmaX:
                                    ch_e "Я не думаю, что это твое дело."
                            elif Girl is LauraX:
                                    ch_l "Не указывай мне что делать."
                            elif Girl is JeanX:
                                    ch_j "Отвали."
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Я бы предпочла не обсуждать это, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Как грубо. . ."
                            elif Girl is GwenX:
                                    ch_g "Как ты смеешь!"
                            elif Girl is BetsyX:
                                    ch_b "Я буду делать все, что захочу."
                            elif Girl is DoreenX:
                                    ch_d "Н-ну, я таким не занимаюсь, так что. . ."
                            elif Girl is WandaX:
                                    ch_w "Заткнись."
                            $ Girl.FaceChange("angry",1)
                            $ Cnt = 1
                    else:
                            #no
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, -2)
                                    $ Girl.Statup("Obed", 70, -2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.FaceChange("bemused",2)
                            if Girl is RogueX:
                                    ch_r "Боюсь, что нет, [RogueX.Petname]."
                            elif Girl is KittyX:
                                    ch_k "Извини, но нет. Я хочу этим заниматься."
                            elif Girl is EmmaX:
                                    ch_e "Нет, думаю, я продолжу этим заниматься. . . и часто."
                            elif Girl is LauraX:
                                    ch_l "Извини, [LauraX.Petname], У меня, все таки, есть потребности."
                            elif Girl is JeanX:
                                    $ Girl.FaceChange("confused",1)
                                    ch_j "Эм. . . нет?"
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Я бы предпочла не обсуждать это, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Я собираюсь. . . об этом забыть."
                            elif Girl is GwenX:
                                    ch_g "Я. . . не хочу!"
                            elif Girl is BetsyX:
                                    ch_b "Это не твое дело."
                            elif Girl is DoreenX:
                                    ch_d "Эм, не лезь в мои дела. . ."
                            elif Girl is WandaX:
                                    ch_w "Заткнись."
                            $ Girl.FaceChange("bemused",1)
                            $ Cnt = 1
                    if not Cnt:
                            $ Girl.AddWord(1,0,0,"nofap")  #adds "nofap" tag to traits
            # end "obedience order"

            "Ты можешь мастурбировать, если тебе хочется." if "nofap" in Girl.Traits:
                    if "askedfap" not in Girl.DailyActions:
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Inbt", 90, 1)
                    if not ApprovalCheck(Girl, 500, "I"):
                            #shy response
                            if "okfap" not in Girl.History:
                                    $ Girl.Statup("Love", 60, 1)
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Inbt", 70, 5)
                                    $ Girl.Statup("Lust", 90, 10)
                            $ Girl.FaceChange("confused",2)
                            if Girl is RogueX:
                                    ch_r "Ну и хорошо! Не то чтобы я вообще этим занималась, конечно. . ."
                            elif Girl is KittyX:
                                    ch_k "Ох? Эм, спасибо?"
                            elif Girl is EmmaX:
                                    ch_e "Я рада, что ты мне разрешил. . ."
                            elif Girl is LauraX:
                                    ch_l "Хорошо."
                            elif Girl is JeanX:
                                    ch_j "Ну. . . хорошо?"
                            elif Girl is StormX:
                                    ch_s "Ох?"
                                    ch_s "Хорошо."
                            elif Girl is JubesX:
                                    ch_v "А? Тогда ладно. . ."
                            elif Girl is GwenX:
                                    ch_g "Ох. . . ну ладно."
                            elif Girl is BetsyX:
                                    ch_b "Ох. . . приятно слышать."
                            elif Girl is DoreenX:
                                    ch_d "Н-ну, ладно. . ."
                            elif Girl is WandaX:
                                    ch_w "Ладно, клево."
                            $ Girl.FaceChange("smile",1)
                    elif ApprovalCheck(Girl, 750, "O"):
                            #submissive response
                            if "okfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 20)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Obed", 90, 10)
                                    $ Girl.Statup("Inbt", 90, 10)
                                    $ Girl.Statup("Lust", 90, 10)
                            $ Girl.FaceChange("sly",1)
                            call AnyLine(Girl,"Да, "+Girl.Petname+".")
                    else:
                            #positive response
                            if "okfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Inbt", 70, 3)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("surprised",2)
                            if Girl is RogueX:
                                    ch_r "Отлично! Это здорово."
                            elif Girl is KittyX:
                                    ch_k "Хорошо! Эм, да."
                            elif Girl is EmmaX:
                                    ch_e "Ох, какое облегчение. . ."
                            elif Girl is LauraX:
                                    ch_l "Наконец-то."
                            elif Girl is JeanX:
                                    ch_j "Ох! Это здорово. . ."
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Это замечательно, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Ох. . . ох! Хорошо!"
                            elif Girl is GwenX:
                                    ch_g "Здорово!"
                            elif Girl is BetsyX:
                                    ch_b "Ох. . . приятно слышать."
                            elif Girl is DoreenX:
                                    ch_d "Ох. . . здорово."
                            elif Girl is WandaX:
                                    ch_w "Конечно."
                            $ Girl.FaceChange("smile",1)
                    $ Girl.DrainWord("nofap",0,0,1) #removes "nofap" tag from traits
                    $ Girl.AddWord(1,0,0,0,"okfap")  #adds "okfap" tag to History

                    #fix add a potential for the girl to run out now. . .
            #end "return permission"

            "Неважно":
                    if not ApprovalCheck(Girl, 500, "I"):
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 80, 10)
                                    $ Girl.Statup("Inbt", 50, 5)
                            $ Girl.FaceChange("bemused",1)
                            if Girl is EmmaX:
                                    ch_e "Надеюсь, теперь мы вернемся к более подходящим темам?"
                            elif Girl is LauraX:
                                    ch_l "Рада, что мы закончили с этим. . ."
                            elif Girl is JeanX:
                                    $ Girl.FaceChange("confused",1)
                                    ch_j "Эм. . . ладно?"
                            elif Girl is StormX:
                                    ch_s ". . . ладно."
                            elif Girl is BetsyX:
                                    ch_b "Действительно?"
                            elif Girl is WandaX:
                                    ch_w "Лаааадно."
                            else: #Rogue, Kitty
                                    $ Girl.FaceChange("surprised",2)
                                    call AnyLine(Girl,"Ну и правильно! Так о чем мы говорили до этого?")
                                    $ Girl.FaceChange("smile",1)
                    elif ApprovalCheck(Girl, 500, "O"):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 60, 5)
                                    $ Girl.Statup("Inbt", 80, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("sly",1)
                            if Girl in (EmmaX, StormX, BetsyX):
                                    call AnyLine(Girl,"Хорошо. . .")
                            else:#Rogue, Kitty, Laura, Jean, Jubilee
                                    call AnyLine(Girl,"Ладно.")
                    elif not ApprovalCheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 80, 5)
                                    $ Girl.Statup("Obed", 50, 5)
                            $ Girl.FaceChange("angry",2,Eyes="side")
                            if Girl is RogueX:
                                    ch_r "Чертовски верно"
                            elif Girl is EmmaX:
                                    ch_e "Я надеялась, что ты так скажешь . . ."
                            elif Girl is StormX:
                                    ch_s "Конечно."
                            elif Girl is BetsyX:
                                    ch_b "Конечно."
                            else: #Kitty, Laura, Jean
                                    call AnyLine(Girl,"Хорошо сказано.")
                            $ Girl.FaceChange("angry",1)
                    else:
                            #neutral response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.FaceChange("sly",1)
                            if Girl in (EmmaX,StormX,BetsyX):
                                    call AnyLine(Girl,"Хорошо. . .")
                            else:#Rogue, Kitty, Laura, Jean
                                    call AnyLine(Girl,"Ладно.")
            #end "nevermind"

        $ Girl.AddWord(1,0,"askedfap",0,"askedfap")  #adds "askedfap" tag to Daily and History
        $ Taboo = TabStore
        return

# End No Fapping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Call to Fap / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label CalltoFap(Girl=0,Fap=0): #rkeljsvgbdw
        #called from EventCalls
        #The girl calls you for permission to fap, 1 is "yes," 2 is "i'll watch," 3 is "i'll visit."

        if Girl:
            $ EGirls = [Girl]
            $ Girl = 0
        else:
            $ EGirls = ActiveGirls[:]
            $ renpy.random.shuffle(EGirls)
        python:
            for BX in EGirls:
                if "wannafap" in BX.DailyActions and BX.Loc != bg_current:
                    #if she's wants to fap and is not in the room with you
                    if "nofap" not in BX.Traits:
                            #if she's allowed to fap, she will
                            BX.DrainWord("wannafap",0,1) #removes "wannafap" tag from daily
                            BX.AddWord(1,0,"gonnafap",0,0)  #adds "gonnafap" tag to daily
                    elif BX.Loc == bg_current:
                            #if she's in the room with you, this won't come up.
                            pass
                    elif Girl:
                        if "wannafap" in BX.DailyActions and "nofap" not in BX.DailyActions:
                            #if she's wants to fap and is allowed to, she will
                            BX.AddWord(1,0,"gonnafap",0,0)  #adds "gonnafap" tag to daily
                            #clears out remaining options, if applicable
                            #any girls who are under "nofap" orders are out of luck this turn. . .
                    else:
                            Girl = BX #checks to see if she's allowed
        #end fap call check

        if not Girl:
                return
        $ Player.DailyActions.append("fapcall")

#        call Shift_Focus(Girl)                 #fix later
        show Cellphone at SpriteLoc(StageLeft)

        "[Girl.Name] звонит вам. . ."
        if Girl is RogueX:
                ch_r "Так вот . . Мне тут стало интересно. . ."
                if not Player.Male:
                    ch_r "Я знаю, ты не хотела, чтобы я. . . эм. . . "
                else:
                    ch_r "Я знаю, ты не хотел, чтобы я. . . эм. . . "
                ch_r "удовлетворяла свои потребности. . ."
                ch_r ". . ."
                ch_r ". . .но, надеюсь, ты не будешь против если я все таки это сделаю?"
                ch_r "Прямо сейчас?"
        elif Girl is KittyX:
                if not Player.Male:
                    ch_k "Привет, я[KittyX.like]знаю, что ты говорила что-то типа. . ."
                else:
                    ch_k "Привет, я[KittyX.like]знаю, что ты говорил что-то типа. . ."
                ch_k "\"не ласкай себя, Китти,\" и[KittyX.like]"
                ch_k "Я знаю, что, вроде как, согласилась, но. . ."
                ch_k "Ты не против[KittyX.like]если я все таки займусь этим?"
        elif Girl is EmmaX:
                ch_e "Я знаю, что у нас было что-то вроде соглашения. . ."
                ch_e "Которое касается моего. . . самоудовлетворения. . ."
                ch_e "или его отсутствие. . ."
                ch_e "И мне просто стало любопытно, ты не против, если мы приостановим это соглашение. . ."
                ch_e "Возможно, только на сегодняшний вечер?"
        elif Girl is LauraX:
                if not Player.Male:
                    ch_l "Привет, помнишь, ты сказала мне, чтобы я не игралась с собой?"
                else:
                    ch_l "Привет, помнишь, ты сказал мне, чтобы я не игралась с собой?"
                ch_l "Я хочу поиграться."
                ch_l ". . ."
                ch_l "Все будет нормально? или. . ."
        elif Girl is JeanX:
                ch_j "Привет, [JeanX.Petname]. . ."
                ch_j "Помнишь, как мы договорились, что я буду держать свои руки подальше от своей. . ."
                ch_j ". . . бусинки?"
                ch_j "В общем, я тут подумала. . ."
                ch_j "Может, мы ненадолго отменим наш договор?"
        elif Girl is StormX:
                ch_s "[StormX.Petname]. . ."
                ch_s "Я чувствую, что мне необходимо немного. . . расслабиться."
                ch_s "Ты не против, если я займусь самоудовлетворением?"
        elif Girl is JubesX:
                if not Player.Male:
                    ch_v "Слушай, помнишь, как ты сказала мне, что я не могу. . ."
                else:
                    ch_v "Слушай, помнишь, как ты сказал мне, что я не могу. . ."
                ch_v ". . . \"заботиться о своих потребностях?\""
                ch_v "Нуу. . . У меня появились потребности."
                ch_v "Огромная куча потребностей. . ."
                ch_v "Так что я надеюсь. . ."
        elif Girl is GwenX:
                ch_g "Я бы хотела. . ."
                if not Player.Male:
                    ch_g "Помнишь, как ты сказала. . ."
                else:
                    ch_g "Помнишь, как ты сказал. . ."
                ch_g "Что я не должна \"самоудовлетворяться?\""
                ch_g "У меня был очень тяжелый день, так что я надеялась, что мы сможем. . ."
                ch_g "Найти компромисс?"
        elif Girl is BetsyX:
                ch_b "Я столкнулась с небольшой проблемой. . ."
                if not Player.Male:
                    ch_b "Помнишь, ты просила меня. . . сдерживать свои желания?"
                else:
                    ch_b "Помнишь, ты просил меня. . . сдерживать свои желания?"
                ch_b "Надеюсь, ты можешь. . . "
                ch_b ". . .освободить меня от этого обязательства."
        elif Girl is DoreenX:
                ch_d "Привет, эм. . ."
                if not Player.Male:
                    ch_d "Помнишь, ты сказала, что я не должна. . . доставлять себе удовольствие?"
                else:
                    ch_d "Помнишь, ты сказал, что я не должна. . . доставлять себе удовольствие?"
                ch_d "И я сказала, что. . . не буду?"
                ch_d "Можно я это сделаю, хотя бы разок?"
        elif Girl is WandaX:
                if not Player.Male:
                    ch_w "Слушай, помнишь, ты сказала, что мне не стоит теребить свою фасолинку?"
                else:
                    ch_w "Слушай, помнишь, ты сказал, что мне не стоит теребить свою фасолинку?"
                ch_w "Сейчас она нуждается в моем внимании."
                ch_w "Ты не против, если я это сделаю?"

        menu:
            "Конечно, без проблем.":
                            $ Girl.Statup("Love", 90, 5)
                            $ Girl.Statup("Love", 80, 5)
                            $ Girl.Statup("Love", 200, 1)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 80, 3)
                            $ Girl.Statup("Lust", 50, 5)
                            if Girl is RogueX:
                                    ch_r "Спасибо, я очень ценю это."
                            elif Girl is KittyX:
                                    ch_k "Клево!"
                            elif Girl is EmmaX:
                                    ch_e "Ох, спасибо, [EmmaX.Petname]."
                            elif Girl is LauraX:
                                    ch_l "Хорошо."
                            elif Girl is JeanX:
                                    ch_j "Фух!"
                            elif Girl is StormX:
                                    ch_s ". . . Благодарю, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Отлично. . ."
                            elif Girl is GwenX:
                                    ch_g "Здорово."
                            elif Girl is BetsyX:
                                    ch_b "Я очень это ценю. . ."
                            elif Girl is DoreenX:
                                    ch_d "Эм, спасибо. . ."
                            elif Girl is WandaX:
                                    ch_w "Клево."
                            $ Fap = 1
            "Если тебе действительно настолько невтерпеж. . .":
                    if (Girl.Love + Girl.Obed) >= 2*Girl.Inbt:
                            #if she agrees to not do it (Love+Obed >= double Inbt)
                            $ Girl.Statup("Love", 80, 2)
                            $ Girl.Statup("Obed", 60, 3)
                            $ Girl.Statup("Obed", 80, 1)
                            $ Girl.Statup("Lust", 80, 5)
                            if Girl is RogueX:
                                    ch_r "Ох, ну. . ."
                                    ch_r "Думаю, я смогу еще потерпеть. . ."
                            elif Girl is KittyX:
                                    ch_k "Ладно, потерплю, если тебя это так волнует. . ."
                            elif Girl is EmmaX:
                                    ch_e "Полагаю, я смогу отвлечься, [EmmaX.Petname]."
                            elif Girl is LauraX:
                                    ch_l "Хмм. Ладно. Не бери в голову."
                            elif Girl is JeanX:
                                    ch_j "Ну, думаю, я могу повременить. . ."
                                    ch_j "У меня же -исключительный- самоконтроль. . ."
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Пожалуй, я смогу выдержать, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Нууу. . ."
                                    ch_v "Я не хочу тебя разочаровывать. . ."
                            elif Girl is GwenX:
                                    ch_g "Ну. . . Я могу немного продержаться. . ."
                            elif Girl is BetsyX:
                                    ch_b ". . . Возможно, я смогу продержаться еще немного. . ."
                            elif Girl is DoreenX:
                                    ch_d "Все не так уж и серьезно, я просто. . ."
                                    ch_d "-занималась и. . . вот. . ."
                            elif Girl is WandaX:
                                    ch_w "Не то чтобы мне прям -невтерпеж-, просто. . ."
                                    ch_w "Ладно, я постараюсь держать себя в руках."
                            $ Girl.Thirst += 10

                    else:
                            #if she insists on doing it
                            $ Girl.Statup("Love", 80, 3)
                            $ Girl.Statup("Love", 200, 1)
                            $ Girl.Statup("Obed", 50, -4)
                            $ Girl.Statup("Obed", 90, -1)
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.Statup("Inbt", 80, 5)
                            $ Girl.Statup("Lust", 50, 5)
                            if Girl is RogueX:
                                    ch_r "Я была бы тебе ОЧЕНЬ признательна."
                                    ch_r "Спасибо."
                            elif Girl is KittyX:
                                    ch_k "Ну, пожалуй. . . так и есть."
                            elif Girl is EmmaX:
                                    ch_e "Я просто хочу снять напряжение после тяжелого дня."
                            elif Girl is LauraX:
                                    ch_l "Да, Наверное, так и есть."
                            elif Girl is JeanX:
                                    ch_j "Хорошо, спасибо!"
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Я ценю это, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Отлично. . ."
                            elif Girl is GwenX:
                                    ch_g "Здорово!"
                            elif Girl is BetsyX:
                                    ch_b "Я очень это ценю. . ."
                            elif Girl is DoreenX:
                                    ch_d "Здорово! Спасибо. . ."
                            elif Girl is WandaX:
                                    ch_w "Отлично!"
                            $ Fap = 1
            "Нет, я запрещаю.":
                    if ApprovalCheck(Girl,600,"O") and (Girl.Obed >= Girl.Inbt):
                            #if she agrees to not do it (Obed >= Inbt)
                            $ Girl.Statup("Love", 50, -5)
                            $ Girl.Statup("Obed", 60, 5)
                            $ Girl.Statup("Obed", 200, 2)
                            $ Girl.Statup("Lust", 80, 5)
                            if ApprovalCheck(Girl,800,"O"):
                                    $ Girl.Statup("Lust", 200, 5)
                            if Girl is RogueX:
                                    ch_r "Ох, ну. . ."
                                    ch_r "Думаю, я смогу вытерпеть. . ."
                            elif Girl is KittyX:
                                    ch_k "Ладно, потерплю, если тебя это так волнует. . ."
                            elif Girl is EmmaX:
                                    ch_e "Полагаю, я смогу отвлечься, [EmmaX.Petname]."
                            elif Girl is LauraX:
                                    ch_l "Хмм. Ладно. Не бери в голову."
                            elif Girl is JeanX:
                                    ch_j ". . ."
                                    ch_j ". . . . . ."
                                    ch_j "Ладно."
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Хорошо."
                            elif Girl is JubesX:
                                    ch_v "Ну. . . Ладно. . ."
                            elif Girl is GwenX:
                                    ch_g "!!!"
                                    ch_g ". . ."
                                    ch_g "Хорошо."
                            elif Girl is BetsyX:
                                    ch_b ". . . Я это переживу."
                            elif Girl is DoreenX:
                                    ch_d "Ох, эм. . . ну ладно. . ."
                            elif Girl is WandaX:
                                    ch_w "Черт."
                            $ Girl.Thirst += 10
                    elif ApprovalCheck(Girl,1000,"LO"):
                            #she is apologetic about it
                            $ Girl.Statup("Love", 70, -5)
                            $ Girl.Statup("Obed", 50, -3)
                            $ Girl.Statup("Obed", 80, -2)
                            $ Girl.Statup("Inbt", 50, 3)
                            $ Girl.Statup("Inbt", 80, 2)
                            $ Girl.Statup("Lust", 80, 5)
                            if Girl is RogueX:
                                    ch_r "Ну, эм, я вроде как уже начала. . ."
                            elif Girl is KittyX:
                                    ch_k "Эм, извини, но я[KittyX.like]должна?"
                            elif Girl is EmmaX:
                                    ch_e "Полагаю, мне все равно придется это сделать. . ."
                            elif Girl is LauraX:
                                    ch_l "Эм, извини, но. . ."
                            elif Girl is JeanX:
                                    ch_j "Ну. . . так получилось, что. . ."
                                    ch_j "Мне нужно \"попросить у тебя прощения\"."
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Боюсь, я уже превысила свои пределы, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Я сейчас немного на взводе. . ."
                            elif Girl is GwenX:
                                    ch_g "Я. . . эм. . . Я -определенно- не буду этого делать. . ."
                                    ch_g "Точно-точно."
                            elif Girl is BetsyX:
                                    ch_b ". . . Конечно. . . Я сожалею, но. . ."
                            elif Girl is DoreenX:
                                    ch_d "Тогда забудь, что я спрашивала. . ."
                            elif Girl is WandaX:
                                    ch_w "Ладно, тогда представь, что у нас не было этого разговора."
                            $ Girl.Thirst += 10
                            $ Fap = 1
                    else:
                            #if she is mad at you
                            $ Girl.Statup("Love", 70, -5)
                            $ Girl.Statup("Love", 90, -5)
                            $ Girl.Statup("Obed", 80, -5)
                            $ Girl.Statup("Inbt", 50, 4)
                            $ Girl.Statup("Inbt", 80, 3)
                            if Girl is RogueX:
                                    ch_r "Знаешь, что? К черту тебя и к черту твои идеи!"
                            elif Girl is KittyX:
                                    ch_k "Ну. . . Я все равно это сделаю!"
                            elif Girl is EmmaX:
                                    ch_e "Думаю, я сама буду это решать."
                            elif Girl is LauraX:
                                    ch_l "Конечно, продолжай считать, что мне важно твое мнение."
                            elif Girl is JeanX:
                                    ch_j "Ладно!"
                                    ch_j "Можешь представить, что я сейчас этого *не* делаю."
                                    $ Girl.FaceChange("angry",Mouth="smirk")
                                    call PsychicFlash (0)
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Что ж, тогда я тебя разочарую, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Мне вроде как сейчас необходимо немного расслабиться. . ."
                            elif Girl is GwenX:
                                    ch_g "Хорошо! . . Но я этого хочу!"
                            elif Girl is BetsyX:
                                    ch_b ". . . Боюсь, я должна."
                            elif Girl is DoreenX:
                                    ch_d "Но. . . мне ОЧЕНЬ плохо!"
                            elif Girl is WandaX:
                                    ch_w "Пожалуй, мне не нужно твое разрешение."
                            $ Girl.Thirst += 10
                            $ Fap = 1
            "Я могу прийти и помочь тебе. . .":
                            $ Girl.Statup("Love", 80, 4)
                            $ Girl.Statup("Love", 200, 1)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 80, 2)
                            $ Girl.Statup("Lust", 80, 5)
                            if Girl is EmmaX:
                                    ch_e "Пожалуй, я приму твое предложение, [EmmaX.Petname]."
                            elif Girl is LauraX:
                                    ch_l "Клево."
                            elif Girl is StormX:
                                    ch_s "Было бы неплохо, я полагаю, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "Это было бы неплохо."
                            elif Girl is WandaX:
                                    ch_w "Конечно, отказываться я точно не буду."
                            else: #Rogue, Kitty, Jean
                                    call AnyLine(Girl,"Ох, это было бы очень кстати. . .")
                            $ Fap = 3
            "Только если я смогу понаблюдать." if AloneCheck(): #only works if you're alone
                    if ApprovalCheck(Girl, 1200):
                            #She agrees
                            $ Girl.Statup("Love", 80, 4)
                            $ Girl.Statup("Obed", 60, 2)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.Statup("Inbt", 80, 3)
                            $ Girl.Statup("Lust", 80, 5)
                            if Girl is RogueX: #R_Mast
                                    ch_r "Хмм. . . это может быть забавно. . ."
                            elif Girl is KittyX:
                                    ch_k "Хихи, хочешь представление? . ."
                            elif Girl is EmmaX:
                                    ch_e "Думаю, это можно устроить. . ."
                            elif Girl is LauraX:
                                    ch_l "Да, я могу это устроить, дай мне минутку. . ."
                            elif Girl is JeanX:
                                    ch_j "Ладно, справедливо. . ."
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Я не возражаю, [StormX.Petname]."
                            elif Girl is JubesX:
                                    ch_v "О, ну, я думаю, это было бы хорошо. . ."
                            elif Girl is GwenX:
                                    ch_g "Думаю, это можно устроить. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я не против. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ну, это может быть весело. . ."
                            elif Girl is WandaX:
                                    ch_w "Чем больше компания, тем веселее."
                            $ Fap = 2
                    else:
                            #she's not into it.
                            $ Girl.Statup("Love", 60, -3)
                            $ Girl.Statup("Obed", 60, -2)
                            $ Girl.Statup("Inbt", 80, 3)
                            $ Girl.Statup("Lust", 50, 5)
                            if Girl is RogueX: #R_Mast
                                    ch_r "Я, эм, в этом не уверена. . ."
                            elif Girl is KittyX:
                                    ch_k "Кхм-кхм, эм, не думаю, что смогу. . ."
                            elif Girl is EmmaX:
                                    ch_e "Я бы предпочла не устраивать для тебя такого представления. . ."
                            elif Girl is LauraX:
                                    ch_l "Нет, хватит с меня слежки . . ."
                            elif Girl is JeanX:
                                    ch_j "Эм, нет?"
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    ch_s "Мне не нравится эта идея, [StormX.Petname]."
                            elif Girl is JubesX:
                                    if not Player.Male:
                                        ch_v "Я бы предпочла, эм, чтобы ты этого не делала. . ."
                                    else:
                                        ch_v "Я бы предпочла, эм, чтобы ты этого не делал. . ."
                            elif Girl is GwenX:
                                    ch_g "Ох, эм. . . Я не уверена, что это хорошая идея. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я не уверена, что хотела бы этого. . ."
                            elif Girl is DoreenX:
                                    ch_d "Эм, нет, спасибо. . ."
                            elif Girl is WandaX:
                                    ch_w "Да. . . насчет этого. . ."
                            $ Girl.Thirst += 15

        $ Girl.DrainWord("wannafap",0,1) #removes "wannafap" tag from daily
        hide Cellphone

        if Fap == 3:
                #if you decide to come over. . .
                $ del EGirls[:]

                $ Girl.Loc = Girl.Home
                $ bg_current = Girl.Home
                call Clear_Nearby
                call Taboo_Level(1)

                jump Misplaced

        elif Fap == 2:
                #if you agree to watch her. . .
                $ del EGirls[:]
                if Girl in (EmmaX,StormX) and Girl.Loc == "bg classroom" and Time_Count >= 2:
                        pass             #if it's Emma and she's in class and it's a good time, stay
                else:
                        $ Girl.Loc = Girl.Home
                call Taboo_Level(0)
                call PhoneSex(Girl)
                $ renpy.pop_call() #skips past EventCall
        elif Fap:
                #if you agree at some point. . .
                $ Girl.AddWord(1,0,"gonnafap",0,0)  #adds "gonnafap" tag to daily

        $ EGirls = ["empty"] #sets token entry to prevent a removal failure. . .
        return

            #add history elements
            #add "if girl is watching, "join us." to basic sex menus
# End Call to Fap / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Phone Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label PhoneSex(Girl=0): #rkeljsvgbdw
        # called by Eventcalls->CalltoFap
        # make sure to adjust orgasm options to work when you aren't in the room.
        if bg_current != "bg player":
                "Вы спешите обратно в свою комнату."
                $ bg_current = "bg player"
                call Taboo_Level
                call Set_The_Scene
        if not AloneCheck():
                ch_p "Мне нужно уединиться. . ."
                call Remove_Girl("All")

        if Girl in (EmmaX,JeanX,BetsyX):
                #telepathic sex?
                call MindFuck

        $ Player.AddWord(1,"phonesex","phonesex",0,"phonesex") #Recent and History
        #display the phone sex graphics

        call Shift_Focus(Girl)
#        show PhoneSex zorder 150

        $ Girl.AddWord(1,"phonesex","phonesex",0,"phonesex")  #adds "phonesex" tag to recent and daily actions, and history
        $ Trigger = 1
        call Shift_Focus(Girl)
        show PhoneSex zorder 150
        if Girl is RogueX:
                ch_r "Ладно, меня видно?"
        elif Girl is KittyX:
                ch_k "Ладно, вот так."
                ch_k "[KittyX.Like]как я выгляжу?"
        elif Girl is EmmaX:
                ch_e "А теперь поставим его вот так. . ."
                if not Player.Male:
                    ch_e "Сейчас ты должна меня видеть."
                else:
                    ch_e "Сейчас ты должен меня видеть."
        elif Girl is LauraX:
                ch_l "Ладно, видеовызов пошел. . ."
        elif Girl is JeanX:
                ch_j "Лаааадно. . . Вот так,  видеовызов пошел. . ."
        elif Girl is StormX:
                ch_s ". . ."
                ch_s "Вроде бы, я настроила камеру, [StormX.Petname]. . ."
        elif Girl is JubesX:
                ch_v "Ладно, загрузка завершена. . ."
                ch_v "Как я выгляжу?"
        elif Girl is GwenX:
                ch_g "Хорошо, телефон поставлю здесь и. . ."
                ch_g "Как меня видно?"
        elif Girl is BetsyX:
                ch_b "Так, вроде бы все настроила. . ."
                ch_b "Как меня видно?"
        elif Girl is DoreenX:
                ch_d "Секунду, надо все настроить. . ."
                ch_d "Как видно?"
        elif Girl is WandaX:
                ch_w "Ладно, телефон готов. . ."
                ch_w "Меня хорошо видно?"

        call Girl_M_Prep

        if Ch_Focus is RogueX:
                ch_r "Хмм, приятно было \"пообщаться\". . ."
                ch_r "Мне пора."
        elif Ch_Focus is KittyX:
                ch_k "Мммм . . звони в любое время, [KittyX.Petname]."
                ch_k "[KittyX.Like]вообще в любое."
        elif Ch_Focus is EmmaX:
                ch_e "Мне нравятся такие небольшие \"созвоны\". . ."
                ch_e "А теперь мне нужно идти."
        elif Ch_Focus is LauraX:
                ch_l "Это было весело. Созвонимся попозже?"
        elif Ch_Focus is JeanX:
                ch_j "Ладно, увидимся."
        elif Ch_Focus is StormX:
                ch_s "Мне понравилось, спасибо. . ."
        elif Ch_Focus is JubesX:
                ch_v "Ммммм. . . позвони как-нибудь снова, [JubesX.Petname]."
                ch_v "Я буду ждать. . ."
        elif Ch_Focus is GwenX:
                ch_g "Это было очень весело."
                ch_g "Дай знать, когда в следующий раз тебе понадобится виртуальная подружка. . ."
        elif Ch_Focus is BetsyX:
                ch_b "Это было довольно весело."
                ch_b "Прошу, позвони мне как-нибудь снова. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Хехехе. . ."
                ch_d "Можешь позвонить мне как-нибудь снова. . ."
        elif Ch_Focus is WandaX:
                ch_w "Фух. . ."
                ch_w "Нам обязательно нужно как-нибудь еще созвониться."
        hide PhoneSex
        #hide the phone sex graphics

        call Get_Dressed
        $ Ch_Focus.OutfitChange(5) #resets her clothes
        $ Ch_Focus.Spunk = []
        call Checkout(1)
        $ Player.RecentActions.remove("phonesex")

        jump Misplaced
        return
#add option for girl to strip herself. . .
# End Phone Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label MindFuck_Screen: #rkeljsvgbdw
        #Displays the current background as a ghost
        if bg_current in PersonalRooms:
                call RoomMask #in Rogue Animations

        elif bg_current == "bg classroom":
                    show bg_classmask onlayer black:
                        alpha .2
        elif bg_current == "bg dangerroom":
                    show bg_danger onlayer black:
                        alpha .2
        elif bg_current == "bg showerroom":
                    show bg_shower onlayer black:
                        alpha .2
        elif bg_current == "bg study":
                    show bg_study onlayer black:
                        alpha .2
        elif bg_current == "bg movies":
                    show bg_movies onlayer black:
                        alpha .2
        elif bg_current == "bg restaurant":
                    show bg_rest onlayer black:
                        alpha .2
        elif bg_current == "bg pool":
                    show bg_pool onlayer black:
                        alpha .2
        elif bg_current == "bg mall":
                    show bg_mall onlayer black:
                        alpha .2
        elif bg_current == "bg shop":
                    show bg_shop onlayer black:
                        alpha .2
        elif bg_current == "bg dressing":
                    show bg_dressing onlayer black:
                        alpha .2
        else: # if 'bg campus' or anything else
                    show bg_campus onlayer black:
                        alpha .2
        return

label PsychicFlash(Face="sly",TempLoc=0): #rkeljsvgbdw
        call MindFuck_Screen
        $ Line = Girl.Loc
        $ Girl.Loc = bg_current
        call Set_The_Scene(1,0,0,0,1)
        if Face:
                $ Girl.FaceChange(Face)
        $ Girl.ArmPose = 2
        $ Girl.Uptop = 1
        $ Girl.Upskirt = 1
        $ Girl.PantiesDown = 1
        ". . . {w=0.3}{nw}"
        if Girl is EmmaX:
                hide Emma_Sprite with fade
        elif Girl is JeanX:
                hide Jean_Sprite with fade
        elif Girl is BetsyX:
                hide Betsy_Sprite with fade
        $ Girl.OutfitChange(6,Changed=1)
        scene onlayer black
        $ Girl.ArmPose = 1
        $ Line = 0
        call AnyLine(Girl,". . .")


label MindFuck(TempLoc=0): #rkeljsvgbdw
        #having sex with a girl in her head
        if Girl is EmmaX:
                ch_e "Может займемся телепатическим сексом?"
        elif Girl is JeanX:
                ch_j "Разве телепатический секс не был бы веселее?"
        elif Girl is BetsyX:
                ch_b "Может быть, ты предпочитаешь, чтобы мы сделали это. . . телепатически?"
        menu MindFuck_Menu:
            "Конечно":
                    if Girl is EmmaX:
                            ch_e "Прекрасно. . ."
                            ch_e "Только позволь мне все подготовить. . ."
                    elif Girl is JeanX:
                            ch_j "Отлично!"
                            ch_j "Ладно, сейчас все будет. . ."
                    elif Girl is BetsyX:
                            ch_b "Замечательно!"
                            ch_b "Позволь мне устроиться поудобнее. . ."

                    call MindFuck_Screen
                    $ TempLoc = Girl.Loc
                    $ Girl.Loc = bg_current
                    $ Girl.FaceChange("sly")
                    #call Display_Girl(EmmaX,0,0)
                    call Set_The_Scene(1,0,0,0,1)
                    call AnyLine(Girl,"Вот. . .")

                    $ Player.AddWord(1,"MindFuck","MindFuck",0,"MindFuck")
                    call SexMenu # call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu

                    $ Girl.Loc = TempLoc
                    if Girl is EmmaX:
                            ch_e "На этом пока все. . ."
                            ch_e "Увидимся во снах. . ."
                    elif Girl is JeanX:
                            ch_j "Ладно, этого хватит. . ."
                            ch_j "Думай обо мне. . ."
                    elif Girl is BetsyX:
                            ch_b "Хорошо, пока закончим."
                            ch_b "Увидимся. . ."

                    $ Girl.OutfitChange(6,Changed=1)
                    $ Girl.Spunk = []
                    if Girl is EmmaX:
                            hide Emma_Sprite with fade
                    elif Girl is JeanX:
                            hide Jean_Sprite with fade
                    elif Girl is BetsyX:
                            hide Betsy_Sprite with fade
                    scene onlayer black
                    jump Misplaced
            "Что это такое?" if "mfuck?" not in Player.RecentActions and "MindFuck" not in Player.History:
                    if Girl is EmmaX:
                            ch_e "Что ж, если ты откроешь свой разум, я смогу создать в нем проекцию."
                            ch_e "Мы повеселимся. . . прямо в твоей голове. . ."
                    elif Girl is JeanX:
                            ch_j "Ну, знаешь, как если бы ты немного ослабил свою защиту. . ."
                            ch_j "Я могла бы пробраться в твою голову и мы могли бы там немного повеселиться. . ."
                    elif Girl is BetsyX:
                            ch_b "Позволь мне сперва устроиться поудобнее. . ."
                            ch_b "Так. . . я могу спроецировать себя в твоем сознании, и мы сможем потрахаться там."
                    $ Player.AddWord(1,"mfuck?")
                    jump MindFuck_Menu
            "Нет, мне хочется по телефону.":
                    if Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Ладно, какая ты скучная. . ."
                            else:
                                ch_e "Ладно, какой ты скучный. . ."
                    elif Girl is JeanX:
                            if not Player.Male:
                                ch_j "Ну и дура. . ."
                            else:
                                ch_j "Ну и дурак. . ."
                    elif Girl is BetsyX:
                            ch_b "Хорошо."
                    return
        return


#Start Frisky class content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Frisky_Class(Girl=0,Teacher=0,LineB=0, BO = []): #rkeljsvgbdw
        if Girl not in TotalGirls:
                return
        $ Partner = 0
        $ Line = 0

#        if len(Present) >= 2:
#            $ Present[1].SpriteLoc = StageLeft
#            $ Present[1].Eyes = "side"
#        $ Present[0].SpriteLoc = StageRight

#        $ BO = ActiveGirls[:]

#        while BO:
#                #loops through and makes choices.
#                if renpy.showing(BO[0].Tag+"_Sprite"):
#                    if BO[0] is RogueX:
#                            show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc,50):
#                                    ease .5 ypos 250
#                    elif BO[0] is KittyX:
#                            show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc,50):
#                                    ease .5 ypos 250
#                    elif BO[0] is LauraX:
#                            show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc,50):
#                                    ease .5 ypos 250
#                    elif BO[0] is JeanX:
#                            show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc,50):
#                                    ease .5 ypos 250
#                    elif BO[0] is JubesX:
#                            show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc,50):
#                                    ease .5 ypos 250
#                    elif BO[0] is GwenX:
#                            show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc,50):
#                                    ease .5 ypos 250
#                $ BO.remove(BO[0])

        call Shift_Focus(Girl)
        if EmmaX.Loc == "bg teacher":
            "[EmmaX.Name] читает лекцию о взаимоотношениях мутантов. Вы замечаете, как [Girl.Name], сидя на своем месте, начинает неловко ерзать."
            $ Teacher = EmmaX
        elif StormX.Loc == "bg teacher":
            "[StormX.Name] читает лекцию по географии и политике. Вы замечаете, как [Girl.Name], сидя на своем месте, начинает неловко ерзать."
            $ Teacher = StormX
        else:
            "Профессор МакКой читает лекцию о гене Икс. Вы замечаете, как [Girl.Name], сидя на своем месте, начинает неловко ерзать."
        "Время от времени вы ловите ее взгляд, направленный в вашу сторону."

        "[Girl.Name] открывает блокнот и начинает строчить записку."
        "Она вынимает листок бумаги, аккуратно складывает его, затем кладет перед вами."
        $ Girl.Facing = 0 #turns to look at you
        "Она наблюдает, как вы разворачиваете записку."
        if "friskyclass" in Girl.History:
                "Там написано \"Не желаешь снова пошалить? Да[[] Нет[[]\""
                menu:
                    "Да":
                        $ Girl.FaceChange("sly",1)
                        $ Girl.Statup("Love", 80, 3)
                        $ Girl.Statup("Inbt", 60, 3)
                        "Она многозначительно улыбается вам."
                        $ D20 = renpy.random.randint(1, 15)
                        jump Frisky_Class_Loop
                    "Нет":
                        $ Girl.Statup("Love", 80, -10)
                        $ Girl.Statup("Love", 70, -5)
                        $ Girl.Statup("Obed", 70, 5)
                        $ Girl.Statup("Inbt", 60, -3)
                        $ Line = "rejected"
                        $ Girl.FaceChange("angry")
                        $ Girl.DailyActions.append("angry")
                        jump Frisky_Class_End
        if Girl is RogueX:
                "Петлеобразные буквы гласят: \"Тебе нравится биология?\""
        elif Girl is KittyX:
                "Изящным почерком написано: \"как насчет биологии?\""
        elif Girl is LauraX:
                "Грубым почерком написано: \"Скучно, правда?\""
        elif Girl is JeanX:
                "Небрежным почерком написано: \"скучновато\"."
        elif Girl is JubesX:
                "Разноцветные буквы гласят: \"Ужасно скучно, да?\""
        elif Girl is GwenX:
                "Жирным шрифтом написано: \"Ну и скучно же тут. Правда?\""
        elif Girl is BetsyX:
                "Изысканным шрифтом написано: \"Здесь довольно скучно, тебе так не кажется?\""
        elif Girl is DoreenX:
                "Аккуратным шрифтом написано: \"Ты любишь биологию?\""
        elif Girl is WandaX:
                "Жирным, но аккуратным почерком написано: \"Занятие отстой, согласись?\""
        if Girl in (RogueX,KittyX,DoreenX):
                $ Girl.FaceChange("smile",2)
                "Вы оглядываетесь на нее и видите, что она слегка краснеет."
                "Она пододвигает к вам ручку, чтобы вы смогли написать ответ."
                $ Girl.FaceChange("smile",1)
        else:
                $ Girl.FaceChange("sly",1)
                "Вы оглядываетесь на нее и видите, как многозначительно она смотрит на вас."
                "Она пододвигает к вам ручку, чтобы вы смогли написать ответ."

        menu:
                "Вы отвечаете. . ."
                "Ты вообще о чем?":
                            jump Frisky_Class_End

                "Нет. Не очень.":
                            $ Girl.Statup("Love", 80, -3)
                            $ Girl.Statup("Inbt", 60, -3)
                            $ Girl.FaceChange("confused")
                            jump Frisky_Class_End

                "Это мой любимый предмет." if Girl in (RogueX,KittyX,DoreenX):
                            $ Girl.Statup("Love", 80, 5)
                            $ Girl.FaceChange("smile")
                            "[Girl.Name] читает вашу записку и улыбается. Она быстро набрасывает еще одну записку и снова кладет ее перед вами."
                            "Вы разворачиваете записку, стараясь, чтобы преподаватель вас не увидел. \"Тогда, может, позанимаемся вместе сегодня вечером?\"."
                            $ Line = "continue"

                "Ага, занятие полный отстой." if Girl not in (RogueX,KittyX,DoreenX):
                            $ Girl.Statup("Love", 80, 5)
                            $ Girl.FaceChange("smile")
                            "[Girl.Name] читает вашу записку и улыбается. Она быстро набрасывает еще одну записку и снова кладет ее перед вами."
                            "Вы разворачиваете записку, стараясь, чтобы преподаватель вас не увидел. \"Тогда, может, вместе 'позанимаемся' сегодня вечером?\"."
                            $ Line = "continue"

                "Да, когда речь заходит о тебе." if Girl in (RogueX,KittyX,DoreenX):
                            $ Line = "her"

                "Я была слишком занята, думая о тебе." if Girl not in (RogueX,KittyX,DoreenX) and not Player.Male:
                            $ Line = "her"


        #at this step, Line will either "her" which means it is about her, "continue", which is "Did you want to study tonight?", or "flirt", which jumps to sexier content, or pass, which drops through.
        if Line == "her":
                    if ApprovalCheck(Girl, 500, "I") or Girl.SEXP >= 30:
                            $ Girl.FaceChange("sly")
                            "[Girl.Name] читает вашу записку и многозначительно улыбается вам."
                            $ Line = "flirt"
                    elif ApprovalCheck(Girl, 900):
                            if Girl in (RogueX,KittyX,DoreenX):
                                    $ Girl.FaceChange("confused",2)
                                    "[Girl.Name] читает вашу записку и сильно краснеет, уставившись в свой конспект."
                            else:
                                    $ Girl.FaceChange("sly",1)
                                    "[Girl.Name] читает вашу записку и хитро улыбается, уставившись в свой конспект."
                            $ Girl.FaceChange("bemused",1)
                            $ Line = "flirt"
                    else:

                            if Girl in (RogueX,KittyX,DoreenX):
                                    $ Girl.FaceChange("perplexed",2)
                                    "[Girl.Name] читает вашу записку и сильно краснеет. Она быстро набрасывает еще одну записку и снова кладет ее перед вами."
                            else:
                                    $ Girl.FaceChange("sly",1)
                                    "[Girl.Name] читает вашу записку и хитро улыбается. Она быстро набрасывает еще одну записку и снова кладет ее перед вами."
                            "Вы разворачиваете записку, стараясь, чтобы преподаватель вас не увидел. \"Я имела ввиду занятия! Может, 'позанимаемся' сегодня вечером?\"."
                            $ Girl.FaceChange("bemused",1)
                            $ Line = "continue"

        #at this step, Line will either "continue", which is "Did you want to study tonight?", or "flirt", which jumps to sexier content, or pass, which drops through.
        if Line == "continue":
                "Она пытается сделать вид, что внимательно слушает лекцию, но не может скрыть широкую улыбку на лице."
                menu:
                    "Вы отвечаете. . ."
                    "Может, в другой раз.":
                            $ Girl.Statup("Love", 80, -3)
                            $ Girl.Statup("Obed", 70, 5)
                            $ Girl.Statup("Inbt", 60, -3)
                            $ Girl.FaceChange("confused")
                            $ Line = 0
                            jump Frisky_Class_End
                    "Неа. У меня есть дела поважнее.":
                            $ Girl.Statup("Love", 80, -10)
                            $ Girl.Statup("Love", 70, -5)
                            $ Girl.Statup("Obed", 70, 5)
                            $ Girl.Statup("Inbt", 60, -3)
                            $ Line = "rejected"
                            $ Girl.FaceChange("angry")
                            $ Girl.DailyActions.append("angry")
                            jump Frisky_Class_End
                    "Это можно.":
                            $ Girl.FaceChange("smile")
                            "Она улыбается, прочитав ваш ответ, и подмигивает вам."
                            $ Girl.DailyActions.append("studydate")
                            "Остальная часть занятия проходит без происшествий."
                            return
                    "Мы можем \"позаниматься\" прямо сейчас.":
                            if ApprovalCheck(Girl, 1000):
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Inbt", 60, 3)
                                    "На лице [Girl.Name_rod] появляется озорная ухмылка и она наклоняется к вам."
                                    $ Line = "flirt"
                            elif ApprovalCheck(Girl, 700):
                                    $ Girl.FaceChange("smile",1)
                                    $ Girl.Statup("Inbt", 60, 2)
                                    if Girl in (RogueX,KittyX,DoreenX):
                                            "[Girl.Name] краснеет и одаривает вас улыбкой."
                                    else:
                                            "[Girl.Name] слегка пугается, а затем одаривает вас улыбкой."
                                    $ Line = "flirt"
                            else:
                                    $ Girl.FaceChange("confused",1)
                                    "[Girl.Name] слегка удивляется, а затем одаривает вас хмурым взглядом."
                                    jump Frisky_Class_End

        #End if Line == "continue"

        #at this step, Line will either be "flirt", which jumps to sexier content, or it will fall through to the ending.
        if Line == "flirt":
                $ Round -= 20
                $ D20 = renpy.random.randint(1, 15)
                $ Girl.FaceChange("sly")
                "Вы замечаете, что одна из туфель [Girl.Name_rod] соскальзывает с ее ноги под столом. Она хитро усмехается, смотря вам в глаза."
                if Girl.Hose and Girl.Hose != "garterbelt":
                        "Вы чувствуете, как ее гладкая ножка в ткани начинает медленно скользить вверх и вниз по всей длине вашей голени."
                else:
                        "Вы чувствуете, как ее гладкая голая ножка начинает медленно скользить вверх и вниз по всей длине вашей голени."

                while D20 <= 21 or "go on" in Player.RecentActions:
                    menu Frisky_Class_Loop:
                        "Отстраниться от нее.":
                                if Line == "fondle pussy":
                                        "Вы медленно убираете руку с ее колена и снова начинаете делать записи."
                                        $ Line = "tease"
                                elif Line == "fondle breast":
                                        "Последний раз сжав ее грудь, вы перемещаете руку обратно на стол."
                                        $ Line = "tease"
                                elif Girl.OCount and Girl.Lust < 90:
                                        "Пока достаточно. . ."
                                        $ Line = "tease"
                                else:
                                        $ Line = "rejected"
                                        $ Girl.Statup("Love", 200, -15)
                                        $ Girl.Statup("Obed", 70, 2)
                                        $ Girl.Statup("Inbt", 60, -2)
                                jump Frisky_Class_End

                        "Посмотреть ей в глаза и слегка улыбнуться." if Line == "flirt":
                                $ Girl.FaceChange("smile")
                                $ Girl.Statup("Love", 200, 5)
                                "[Girl.Name] улыбается в ответ."
                                "Она оглядывается на переднюю часть аудитории, а ее рука в это время копошится под столом, пока не находит вашу руку."
                                $ Line = "handholding"
                                jump Frisky_Class_Loop
                        "Нежно взять ее за руку и легонько начать поглаживать." if Line == "handholding":
                                $ Girl.Statup("Love", 200, 5)
                                $ Girl.Statup("Lust", 50, 5)
                                $ Girl.FaceChange("smile")
                                "[Girl.Name] удовлетворенно вздыхает и держит вас за руку до конца занятия."
                                jump Frisky_Class_End
                        #end end polite flirting

                        "Попробовать просунуть руку между ее коленей." if Line != "fondle pussy":
                                $ Line = "fondle pussy"
                                if ApprovalCheck(Girl, 1200) and Girl.FondleP and Girl.SEXP >= 40:
                                        $ Girl.FaceChange("sly")
                                        $ Girl.Statup("Love", 90, 5)
                                        $ Girl.Statup("Obed", 70, 5)
                                        $ Girl.Statup("Inbt", 60, 5)
                                        "С лукавой улыбкой, [Girl.Name] кладет свою руку на вашу."
                                elif ApprovalCheck(Girl, 1400) and Girl.FondleP:
                                        $ Girl.FaceChange("smile")
                                        $ Girl.Statup("Love", 80, 3)
                                        $ Girl.Statup("Obed", 70, 7)
                                        $ Girl.Statup("Inbt", 60, 3)
                                        "Сначала [Girl.Name] слегка вздрагивает, когда ваша рука начинает двигаться вверх по ее бедру, но вскоре на ее лице появляется легкая улыбка."
                                elif ApprovalCheck(Girl, 1500):
                                        $ Girl.FaceChange("perplexed",2)
                                        $ Girl.Statup("Obed", 70, 10)
                                        $ Girl.Statup("Inbt", 60, 3)
                                        "[Girl.Name] смотрит на вас с тревогой, но затем тихонько успокаивается."
                                        $ Girl.FaceChange("smile",1)
                                        $ D20 += 2
                                else:
                                        $ Line = "too far"

                                if Line == "fondle pussy":
                                        $ Girl.FaceChange("sly")
                                        $ Girl.Statup("Lust", 94, 5)
                                        if Girl.PantsNum() == 5: #skirt
                                            "Хитрая улыбка [Girl.Name_rod] становится страстной, когда она чувствует, как ваши пальцы пробираются под ее юбку, а затем медленно обводят мягкие контуры ее холмика."
                                        elif Girl.PantsNum() >= 7: #pants
                                            "Хитрая улыбка [Girl.Name_rod] становится страстной, когда она чувствует, как ваши пальцы скользят под ее брюки, а затем медленно обводят мягкие контуры ее холмика."
                                        else: #No pants
                                            "Хитрая улыбка [Girl.Name_rod] становится страстной, когда она чувствует, как ваши пальцы проскальзывают между ее бедер, а затем медленно обводят мягкие контуры ее холмика."

                                        $ Girl.Statup("Lust", 94, 5)
                                        if Girl.Panties == "shorts":
                                            "Вы чувствуете, что ее шорты становятся влажными от ваших прикосновений через тонкий материал. Ее щеки заливаются краской, а дыхание становится все более глубоким и быстрым."
                                        elif Girl.Panties:
                                            "Вы чувствуете, что ее трусики становятся влажными от ваших прикосновений через тонкий материал. Ее щеки заливаются краской, а дыхание становится все более глубоким и быстрым."
                                        elif Girl.Pubes:
                                            "Вы чувствуете, что ее мохнатая киска стала влажной от ваших прикосновений. Ее щеки заливаются краской, а дыхание становится все более глубоким и быстрым."
                                        else:
                                            "Вы чувствуете, что ее гладкая киска стала влажной от ваших прикосновений. Ее щеки заливаются краской, а дыхание становится все более глубоким и быстрым."
                                        $ Trigger = "fondle pussy"
                                        $ D20 += 5

                        "Продолжить ласкать ее киску." if Line == "fondle pussy":
                                $ Girl.Statup("Obed", 70, 5)
                                $ Girl.Statup("Inbt", 60, 3)
                                $ Girl.Statup("Lust", 89, 5)
                                $ Girl.Statup("Lust", 94, 5)
                                $ LineB = renpy.random.choice(["Пока идет занятие, вы продолжаете медленно массировать ее теплую промежность.",
                                        "Пока продолжается занятие, вы продолжаете медленно массировать ее влажную киску.",
                                        "Пока идет лекция, вы продолжаете медленно ласкать ее клитор.",
                                        "Пока продолжается занятие, вы продолжаете медленно ласкать ее половые губы."])
                                "[LineB]"

                                $ D20 += 5
                        #end fondling pussy

                        "Начать ласкать ее сиськи." if Line != "fondle breasts":
                                $ Line = "fondle breasts"
                                if ApprovalCheck(Girl, 1100) and Girl.FondleB and Girl.SEXP >= 40:
                                        $ Girl.Statup("Love", 80, 5)
                                        $ Girl.Statup("Obed", 70, 5)
                                        $ Girl.Statup("Inbt", 60, 3)
                                        $ Girl.FaceChange("sly")
                                        "[Girl.Name] закрывает глаза и начинает поглаживать вашу руку."
                                elif ApprovalCheck(Girl, 1300) and Girl.FondleB:
                                        $ Girl.Statup("Love", 80, 3)
                                        $ Girl.Statup("Obed", 70, 7)
                                        $ Girl.Statup("Inbt", 60, 3)
                                        $ Girl.FaceChange("smile",1)
                                        "[Girl.Name] вздрагивает, когда ваша рука проходит по ее грудной клетке. Улыбка затрагивает ее уста, когда вы дотрагиваетесь до ее груди."
                                elif ApprovalCheck(Girl, 1400):
                                        $ Girl.Statup("Obed", 70, 10)
                                        $ Girl.Statup("Inbt", 60, 3)
                                        $ Girl.FaceChange("perplexed",2)
                                        "[Girl.Name] смотрит на вас с тревогой, но затем тихонько успокаивается."
                                        $ Girl.FaceChange("smile",2)
                                        $ D20 += 5
                                else:
                                        $ Line = "too far"

                                if Line == "fondle breasts":
                                        $ Girl.FaceChange("sly")
                                        $ Girl.Statup("Lust", 94, 5)
                                        "Хитрые глаза [Girl.Name_rod] загораются, когда ваша рука обхватывает ее грудь, нежно лаская."
                                        "Ее соски начинают твердеть и она издает легкий стон удовольствия."
                                        $ D20 += 7
                                        $ Trigger = "fondle breasts"
                        "Продолжить ласкать ее сиськи." if Line == "fondle breasts":
                                $ Girl.Statup("Obed", 70, 5)
                                $ Girl.Statup("Inbt", 60, 2)
                                $ Girl.Statup("Lust", 95, 3)
                                "Едва обращая внимание на лекцию, вы продолжаешь ласкать ее грудь в своей ладони."
                                $ D20 += 7
                        #end fondling tits

                        "Попробовать положить ее руку к себе на колени." if not Trigger2 and Player.Semen:
                                if "hand" in Girl.RecentActions or "finger" in Girl.RecentActions:
                                        if not Player.Male:
                                            "[Girl.Name] ухмыляется, а ее рука снова ложится вам на киску."
                                        else:
                                            "[Girl.Name] ухмыляется, а ее рука снова хватает ваш член."
                                elif ApprovalCheck(Girl, 1200) and Girl.Hand and Girl.SEXP >= 40:
                                        $ Girl.FaceChange("sly")
                                        $ Girl.Statup("Love", 90, 5)
                                        $ Girl.Statup("Obed", 70, 5)
                                        $ Girl.Statup("Inbt", 60, 5)
                                        "[Girl.Name] хитро улыбвается и ее рука начинает ласкать вашу промежность."
                                elif ApprovalCheck(Girl, 1400) and Girl.FondleP:
                                        $ Girl.FaceChange("smile")
                                        $ Girl.Statup("Love", 80, 3)
                                        $ Girl.Statup("Obed", 70, 7)
                                        $ Girl.Statup("Inbt", 60, 3)
                                        "[Girl.Name] слегка вздрагивает, когда вы кладете ее рукой на свое бедро, но затем она расплывается в улыбке."
                                elif ApprovalCheck(Girl, 1500):
                                        $ Girl.FaceChange("perplexed",2)
                                        $ Girl.Statup("Obed", 70, 10)
                                        $ Girl.Statup("Inbt", 60, 3)
                                        "[Girl.Name] смотрит на вас с тревогой, но потом тихонько успокаивается."
                                        $ Girl.FaceChange("smile",1)
                                        $ D20 += 2
                                else:
                                        $ Line = "too far"

                                if Line != "too far":
                                        #if she agrees. . .
                                        $ Girl.FaceChange("sly")
                                        $ Girl.Statup("Lust", 94, 5)
                                        if "cockout" not in Player.RecentActions:
                                                if Player.Male:
                                                        "[Girl.Name] медленно расстегивает молнию на ваших штанах и вытаскивает ваш член на свободу."
                                                        $ Girl.RecentActions.append("hand")
                                                        $ Girl.DailyActions.append("hand")
                                                        if "hand" not in Girl.RecentActions:
                                                                $ Girl.Hand += 1
                                                else:
                                                        "[Girl.Name] медленно расстегивает молнию на ваших штанах и проводит рукой по вашей киске."
                                                        $ Girl.RecentActions.append("finger")
                                                        $ Girl.DailyActions.append("finger")
                                                        if "finger" not in Girl.RecentActions:
                                                                $ Girl.Finger += 1
                                                $ Player.AddWord(1,"cockout")
                                                call Seen_First_Peen(Girl,Partner)
                                                $ Girl.Statup("Lust", 94, 5)
                                        if Player.Male:
                                                $ Trigger2 = "hand"
                                        else:
                                                $ Trigger2 = "finger"
                                        if not Player.Male:
                                            "Она начинает нежно поглаживать ее. . ."
                                        else:
                                            "Она начинает нежно поглаживать его. . ."
                                        $ D20 += 5
                        #end Start handjob

                        "Остановить дрочку." if Trigger2 == "hand":
                                "Вы кладете руку на ее запястье и отталкиваете ее руку."
                                if ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 700, "O") or (Girl.Love+Girl.Obed) >= (2*Girl.Inbt):
                                        #if high obedience or Obedience and Love greater than double inbt
                                        $ Girl.FaceChange("sad")
                                        $ Girl.Statup("Love", 90, -1)
                                        $ Girl.Statup("Obed", 60, 2)
                                        $ Girl.Statup("Obed", 80, 3)
                                        "[Girl.Name] позволяет убрать свою руку и возвращается к тому, что она ей делала."
                                        $ Girl.FaceChange("sly")
                                        $ Trigger2 = 0
                                else:
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 80, -3)
                                        $ Girl.Statup("Love", 90, -1)
                                        $ Girl.Statup("Obed", 70, -2)
                                        $ Girl.Statup("Inbt", 60, 3)
                                        $ Girl.Statup("Inbt", 80, 2)
                                        "[Girl.Name] крепко сжимает ваш член, затем продолжает гладить его, когда вы отпускаете ее руку."
                                        $ Girl.FaceChange("sly")
                                        $ D20 += 2
                        #end Stop handjob
                        "Остановить мастурбацию вашей киски." if Trigger2 == "finger":
                                "Вы кладете руку на ее запястье и отталкиваете ее руку."
                                if ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 700, "O") or (Girl.Love+Girl.Obed) >= (2*Girl.Inbt):
                                        #if high obedience or Obedience and Love greater than double inbt
                                        $ Girl.FaceChange("sad")
                                        $ Girl.Statup("Love", 90, -1)
                                        $ Girl.Statup("Obed", 60, 2)
                                        $ Girl.Statup("Obed", 80, 3)
                                        "[Girl.Name] позволяет убрать свою руку и возвращается к тому, что она ей делала."
                                        $ Girl.FaceChange("sly")
                                        $ Trigger2 = 0
                                else:
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 80, -3)
                                        $ Girl.Statup("Love", 90, -1)
                                        $ Girl.Statup("Obed", 70, -2)
                                        $ Girl.Statup("Inbt", 60, 3)
                                        $ Girl.Statup("Inbt", 80, 2)
                                        "[Girl.Name] крепко прижимается к вашей киске, затем продолжает гладить ее, когда вы отпускаете ее руку."
                                        $ Girl.FaceChange("sly")
                                        $ D20 += 2
                        #end Stop handjob

                    #after menu, still inside loop

                    #she tries to give you a handy. . .
                    if not Trigger2 and Player.Semen and "stophand" not in Girl.RecentActions:
                            if ApprovalCheck(Girl, 1200) and ApprovalCheck(Girl, 400, "I") and Girl.Hand and Girl.SEXP >= 40:
                                    $ Girl.FaceChange("sly")
                                    "[Girl.Name] хитро улыбвается и ее рука начинает ласкать вашу промежность."
                                    menu:
                                        "Что будете делать?"
                                        "Позволить":
                                                "Вы улыбаетесь и слегка киваете."
                                                $ Girl.FaceChange("sly")
                                                $ Girl.Statup("Love", 80, 1)
                                                $ Girl.Statup("Inbt", 70, 3)
                                                $ Girl.Statup("Inbt", 90, 2)
                                                $ Girl.Statup("Lust", 94, 5)
                                                if "cockout" not in Player.RecentActions:
                                                        if Player.Male:
                                                                "[Girl.Name] медленно расстегивает молнию на ваших штанах и вытаскивает ваш член на свободу."
                                                                $ Girl.RecentActions.append("hand")
                                                                $ Girl.DailyActions.append("hand")
                                                                if "hand" not in Girl.RecentActions:
                                                                        $ Girl.Hand += 1
                                                        else:
                                                                "[Girl.Name] медленно расстегивает молнию на ваших штанах и проводит рукой по вашей киске."
                                                                $ Girl.RecentActions.append("finger")
                                                                $ Girl.DailyActions.append("finger")
                                                                if "finger" not in Girl.RecentActions:
                                                                        $ Girl.Finger += 1
                                                        $ Player.AddWord(1,"cockout")
                                                        call Seen_First_Peen(Girl,Partner)
                                                        $ Girl.Statup("Lust", 94, 5)
                                                if Player.Male:
                                                        $ Trigger2 = "hand"
                                                else:
                                                        $ Trigger2 = "finger"
                                                if not Player.Male:
                                                    "Она начинает нежно поглаживать ее. . ."
                                                else:
                                                    "Она начинает нежно поглаживать его. . ."
                                                $ D20 += 10
                                        "Остановить":
                                                "Вы кладете руку на ее запястье и отталкиваете ее руку."
                                                $ Girl.RecentActions.append("stophand")
                                                if ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 700, "O") or (Girl.Love+Girl.Obed) >= (2*Girl.Inbt):
                                                        #if high obedience or Obedience and Love greater than double inbt
                                                        $ Girl.FaceChange("sad")
                                                        $ Girl.Statup("Love", 90, -1)
                                                        $ Girl.Statup("Obed", 60, 2)
                                                        $ Girl.Statup("Obed", 80, 3)
                                                        "[Girl.Name] позволяет убрать свою руку и возвращается к тому, что она ей делала."
                                                        $ Girl.FaceChange("sly")
                                                        $ Trigger2 = 0
                                                else:
                                                        $ Girl.FaceChange("angry")
                                                        $ Girl.Statup("Love", 80, -3)
                                                        $ Girl.Statup("Love", 90, -1)
                                                        $ Girl.Statup("Obed", 70, -2)
                                                        $ Girl.Statup("Inbt", 60, 3)
                                                        $ Girl.Statup("Inbt", 80, 2)
                                                        "[Girl.Name] останавливается, но выглядит очень раздраженной."
                                                        $ D20 += 10
                    #end Start auto handjob

                    if Trigger2:
                            #if you're getting a handy:
                            if not Player.Male:
                                "[Girl.Name] продолжает ласкать рукой вашу киску. . ."
                            else:
                                "[Girl.Name] продолжает ласкать рукой ваш член. . ."
                            $ Player.Focus += 15 if Player.Focus < 60 else 10
                            if Player.Focus >= 100:
                                    #If you can cum:
                                    if not Player.Male:
                                        "Когда вы приближаетесь к кульминации, [Girl.Name] кладет руку на вашу киску."
                                        ". . . Вы брызгаете ей на руку."
                                    else:
                                        "Когда вы приближаетесь к кульминации, [Girl.Name] кладет руку на ваш член."
                                        ". . . Вы кончаете ей на руку."
                                    $ Player.Semen -= 1
                                    $ Player.Focus = 15
                                    if (Girl.Blow and ApprovalCheck(Girl, 1200)) or Girl is JubesX:
                                            "Она быстро все слизывает."
                                            $ Girl.Addict -= 20
                                            $ Girl.Swallow += 1
                                            $ Girl.RecentActions.append("swallow")
                                            $ Girl.DailyActions.append("swallow")
                                    else:
                                            "Она быстро вытирает руку под столом."
                                    $ Girl.Statup("Lust", 200, 5)
                                    $ D20 += 10
                                    if not Player.Semen:
                                            "Она продолжает легонько поглаживать вас, но сейчас вы, похоже, не готовы к этому. . ."
                                            $ Trigger2 = 0
                            $ D20 += 5
                    #end handy cycling. . .


                    if Girl.Lust >= 95:
                            $ LineB = Line
                            call Girl_Cumming(Girl,1)
                            $ Line = LineB
                            $ LineB = renpy.random.choice([Girl.Name+" разваливается на столе.",
                                    Girl.Name+" бормочет что-то неразборчивое.",
                                    Girl.Name+", закусив губу, изо всех сил пытается удержаться в вертикальном положении.",
                                    Girl.Name+", кажется, слегка краснеет."])
                            "[LineB]"
                            $ D20 += 15
                    #end orgasms


                    $ Round -= 7
                    if Round <= 15:
                            "К сожалению, похоже, занятие подходит к концу. Вам придется отложить все на потом. . ."
                            $ Line = "tease"
                            jump Frisky_Class_End
                    if Line == "too far":
                            #You've pushed things with the lead girl too far
                            $ Girl.FaceChange("surprised",2)
                            $ Girl.Statup("Love", 80, -5)
                            $ Girl.Statup("Obed", 70, 7)
                            $ Girl.Statup("Inbt", 50, -3)
                            "[Girl.Name] начинает полушепотом ворчать на вас."
                            $ Girl.FaceChange("angry",1)
                            "Ее ледяного взгляда, направленного на вас, достаточно, чтобы привлечь внимание ваших однокурсников."
                            $ D20 += 20
                            if "go on" in Player.RecentActions:
                                    jump Frisky_Class_End
                                    $ Line = "caught"
                    else:
                        if len(Present) >= 2 and D20 >= 15:
                            #if there is another girl, see what she thinks.
                            if Partner:
                                    #If the girl has already joined in. . .
                                    $ Partner.GirlLikeUp(Girl,2)
                                    $ Girl.GirlLikeUp(Partner,2)
                                    $ Partner.Statup("Lust", 95, 3)
                                    $ LineB = renpy.random.choice([0,
                                            0,
                                            0,
                                            Partner.Name+", похоже, увлечена процессом. . .",
                                            Partner.Name+" ускоряет движения рукой.",
                                            Partner.Name+" прикусывает губу, не прекращая движения рукой.",
                                            Partner.Name+" немного замедляет движения рукой."])
                                    if LineB:
                                            "[LineB]"
                                    if Partner.Lust >= 95:
                                            $ LineB = Line
                                            call Girl_Cumming(Partner,1)
                                            $ Line = LineB
                                            $ LineB = renpy.random.choice([Partner.Name+" разваливается на столе.",
                                                    Partner.Name+" бормочет что-то неразборчивое.",
                                                    Partner.Name+", закусив губу, изо всех сил пытается удержаться в вертикальном положении.",
                                                    Partner.Name+", кажется, слегка краснеет."])
                                            "[LineB]"
                                            $ D20 += 15

                            elif "saw with "+ Girl.Tag in Present[1].Traits:
                                    call AnyLine(Present[1],"Ну и ну!")
                                    $ Present[1].GirlLikeUp(Girl,-4)
                                    $ Girl.GirlLikeUp(Present[1],-2)
                                    call Remove_Girl(Present[1])
                            elif ApprovalCheck(Present[1], 1500,Alt=[[WandaX],0]) and Present[1].GirlLikeCheck(Girl) >= 600:
                                    #If the other girl is into it, she lets it continue
                                    $ Present[1].Eyes = "leftside"
                                    "[Present[1].Name], похоже, замечает, чем заниматесь вы двое."
                                    $ Present[1].FaceChange("sly",1)
                                    "Похоже, ей это нравится. . ."
                                    if ApprovalCheck(Present[1], 800, "I") or "exhibitionist" in Present[1].Traits:
                                            $ Girl.Statup("Inbt", 90, 3)
                                            $ Present[1].GirlLikeUp(Girl,3)
                                            $ Girl.GirlLikeUp(Present[1],5)
                                            $ Present[1].Statup("Lust", 89, 7)
                                            "Вы замечаете, что и [Present[1].Name_dat] это начинает нравится."
                                            $ Present[1].AddWord(1,"frisky","frisky",0,0) #adds "word" to Recent/Daily
                                            $ Partner = Present[1]

                            else:
                                    #If she isn't into it.
#                                    $ Present[1].Eyes = "leftside"
                                    $ Present[1].Facing = 0 #turns to look at you
                                    "[Present[1].Name], похоже, замечает, чем заниматесь вы двое."
                                    $ Present[1].AddWord(1,0,0,"saw with " + Girl.Tag)
                                    $ Present[1].FaceChange("angry",1)
                                    if Present[1] is RogueX:
                                            ch_r "Как ты смеешь! Шлюха."
                                    elif Present[1] is KittyX:
                                            ch_k "Эй! . . . ЭЙ!"
                                    elif Present[1] is LauraX:
                                            ch_l "Хватит."
                                    elif Present[1] is JeanX:
                                            ch_j "Эй, прекрати."
                                    elif Present[1] is JubesX:
                                            ch_v "Воу, хватит!"
                                    elif Present[1] is GwenX:
                                            ch_g "Эй! Это, конечно, забавно и все такое, но кое-кто тут пытается учиться!"
                                    elif Present[1] is BetsyX:
                                            ch_b "Вам не кажется, что вы должны вести себя потише?"
                                    elif Present[1] is DoreenX:
                                            ch_d "Шшш, мы тут пытаемся заниматься!"
                                    elif Present[1] is WandaX:
                                            ch_w "Может, успокоитесь. . ?"
                                    $ Present[1].GirlLikeUp(Girl,-2)
                                    $ Girl.GirlLikeUp(Present[1],-3)
                                    $ D20 += 15
                                    if "go on" in Player.RecentActions:
                                        $ Line = "caught"
                                        jump Frisky_Class_End
                            #End "Partner" stuff.  ..

                        if Teacher and "frisky" in Teacher.RecentActions:
                            #if she is fapping. . .
                            $ Teacher.GirlLikeUp(Girl,2)
                            $ Girl.GirlLikeUp(Teacher,2)
                            $ Teacher.Statup("Lust", 95, 3)
                            $ LineB = renpy.random.choice([0,
                                    0,
                                    0,
                                    Teacher.Name+" немного заминается при чтении своей лекции.",
                                    Teacher.Name+" ускоряет движения рукой.",
                                    Teacher.Name+", прикусывает губу, не прекращая движения рукой.",
                                    Teacher.Name+" немного замедляет движения рукой."])
                            if LineB:
                                    "[LineB]"
                            if Teacher.Lust >= 95:
                                    $ LineB = Line
                                    call Girl_Cumming(Teacher,1)
                                    $ Line = LineB
                                    $ LineB = renpy.random.choice([Teacher.Name+" немного заминается при чтении своей лекции.",
                                            Teacher.Name+" бормочет что-то неразборчивое, но продолжает лекцию.",
                                            Teacher.Name+", закусив губу, изо всех сил пытается продолжить читать лекцию.",
                                            Teacher.Name+" выглядит немного неважно.",
                                            Teacher.Name+", кажется, слегка краснеет."])
                                    "[LineB]"
                                    $ D20 += 15
                        #end teacher content
                        if D20 > 30:
                            #if you've been making a spectacle. . .
                            if Nearby:
                                    $ BO = Nearby[:]
                                    while BO:
                                            $ BO[0].Facing = 0 #turns to look at you
                                            $ BO.remove(BO[0])
                            if D20 >= 50:
                                $ LineB = renpy.random.choice([0,
                                        0,
                                        0,
                                        "Все в аудитории больше не обращают внимания на лекцию.",
                                        "Всем в аудитории определенно нравится представление, которое она устроила.",
                                        "Все в аудитории обсуждают происходящее.",
                                        "Студенты, похоже, пристально наблюдают за вами."])
                            else:
                                $ LineB = renpy.random.choice([0,
                                        0,
                                        0,
                                        "Студенты, похоже, не совсем понимают, о чем она говорит.",
                                        "Студенты, кажется, немного смущены тем, чем она занимается.",
                                        "Студенты бросают странные взгляды в вашу сторону.",
                                        "Группа студентов, похоже, пристально наблюдает за вами."])
                            if LineB:
                                    "[LineB]"
                    #after menu, still inside loop

                #After D20:
                if "exhibitionist" not in Girl.Traits and not ApprovalCheck(Girl, 700,"I"):
                    #if it falls out and the girl is not prepared to continue, it goes "too far."
                    $ Line = "too far"
                if Line not in ("rejected", "handholding", "tease"):
                    $ Girl.FaceChange("surprised")
                    if Teacher:
                            $ Teacher.FaceChange("surprised",1)
                            "[Teacher.Name] прерывает свою лекцию на полуслове, когда замечает, чем вы двое заняты."
                            if "EmmaStorm" in EmmaX.History:
                                if ApprovalCheck(EmmaX, 1200) and ApprovalCheck(StormX, 1200): #and "EmmaStormQueue" not in EmmaX.Traits:
                                    $ EmmaX.AddWord(1,0,0,"EmmaStormQueue") #adds to Traits, queuing up a redo of event
                            elif len(Rules) >= 3 and "classcaught" in EmmaX.History and "met" in StormX.History and (EmmaX.SEXP >= 15 or StormX.SEXP >= 15):
                                    $ EmmaX.AddWord(1,0,0,"EmmaStormQueue") #adds to Traits, queuing up a redo of event
                            if ApprovalCheck(Teacher, 1500) and Teacher.GirlLikeCheck(Girl) >= 600:
                                    #If Teacher is into it, she lets it continue
                                    $ Teacher.FaceChange("sly",1)
                                    if Line == "too far":
                                            #if it was too much for the girl, it cancels out.
                                            $ Girl.Mouth = "sad"
                                            if Teacher == EmmaX:
                                                    "Она смотрит на вас и пожимает плечами, продолжая свою лекцию, но момент уже упущен."
                                            elif Teacher == StormX:
                                                    "Она смотрит на вас и улыбается, продолжая свою лекцию, но момент уже упущен."
                                            jump Frisky_Class_End
                                    "На ее лице появляется хитрая улыбка и она продолжает свою лекцию."
                                    $ Girl.FaceChange("sly",1)
                                    if ApprovalCheck(Teacher, 800, "I") or "exhibitionist" in Teacher.Traits:
                                            $ Teacher.Statup("Inbt", 90, 3)
                                            $ Teacher.GirlLikeUp(Girl,3)
                                            $ Girl.GirlLikeUp(Teacher,5)
                                            $ Teacher.Statup("Lust", 89, 7)
                                            "Вы замечаете, что рука [Teacher.Name_rod] устремляется вниз под трибуну и начинает двигаться."
                                            $ Teacher.AddWord(1,"frisky","frisky",0,0) #adds "word" to Recent/Daily
                                            $ Player.AddWord(1,"go on","go on",0,0) #adds "word" to Recent/Daily
                                    "[Girl.Name] оглядывается и пожимает плечами. . ."
                                    jump Frisky_Class_Loop
                            else:
                                    $ Teacher.FaceChange("angry",1)
                                    $ Girl.Mouth = "sad"
                                    if Teacher == EmmaX:
                                            ch_e "[EmmaX.Petname], [Girl.Name], вам не кажется, что вам лучше уделять такое внимание лекции, а не телам друг друга?"
                                            ch_e "Возможно, чтобы успокоиться, вам стоит посетить кабинет директора?"
                                    elif Teacher == StormX:
                                            ch_s "[StormX.Petname], [Girl.Name], я понимаю ваш задор, но могли бы вы заниматься подобным не при мне?"
                                            ch_s "Думаю, вам стоит успокоиться и посетить кабинет Чарльза."
                    else:
                            "Доктор МакКой останавливает лекцию, когда замечает, что все в аудитории смотрят на вас двоих."
                            ch_mc "Ох, пресвятые небеса!"
                            ch_mc "[Player.Name]!?! {b}ЧТО ВЫ ДЕЛАЕТЕ? ОБА, НЕМЕДЛЕННО В КАБИНЕТ ПРОФЕССОРА!{/b}"
                    $ Girl.AddWord(1,0,0,0,"friskyclass") #adds "word" to History
                    $ Line = 0
                    $ Girl.Statup("Love", 80, -10)
                    $ Girl.Statup("Obed", 70, -5)
                    $ Girl.Statup("Inbt", 50, -10)
                    $ Trigger = 0
                    if Girl not in Rules:
                            call Girls_Caught(Girl)
                    else:
                            "Поскольку Ксавье не заботят ваши дела, вы оба вместо этого отправляетесь по своим комнатам."
                            $ Girl.Loc = "bg player"
                            call CleartheRoom(Girl,0,1)
                            jump Player_Room
        # end if Line == "flirt"


label Frisky_Class_End:
        $ Trigger = 0
        $ Partner = 0
        if Teacher:
                $ Teacher.DrainWord("frisky",1,0)
        if not Line:
                #if no flirting happened
                $ Girl.FaceChange("confused")
                "Она разворачивает записку и быстро ее перечитывает."
                $ Girl.FaceChange("sad")
                "После этого, вы видите разочарование, отразившееся на ее лице."
                "Она пишет ответ и кладет записку перед вами."
                "Вы открываете ее и читаете: {i}Тогда забудь.{/i}"
        elif Line == "tease":
                #if you had been messing around, but pulled away
                if Girl.Lust >= 80:
                        $ Girl.FaceChange("surprised",2)
                        "[Girl.Name] поражается вами."
                        $ Girl.FaceChange("sad",2)
                        "[Girl.Name] смотрит на вас немного расстроенная тем, что вы так резко все оборвали."
                $ Girl.AddWord(1,0,0,0,"friskyclass") #adds "word" to History
                $ Girl.FaceChange("sly",1)
                "[Girl.Name] делает глубокий вдох, наклоняется к вам и шепчет с предыханием."
                if Girl is RogueX:
                        ch_r "Вечерние \"занятия\" будут гораздо интереснее."
                elif Girl is KittyX:
                        ch_k "Думаю, вечером нам[KittyX.like]будет -намного- веселее. . ."
                elif Girl is LauraX:
                        ch_l "Сегодня вечером мы можем. . . закончить с этим."
                elif Girl is JeanX:
                        ch_j "Думаю, мы можем с этим немного подождать. . ."
                elif Girl is JubesX:
                        ch_v "Я с нетерпением жду возможности заняться этим позже. . ."
                elif Girl is GwenX:
                        ch_g "Мы можем продолжить позже. . ."
                elif Girl is BetsyX:
                        ch_b "Уверена, мы сможем продолжить позже. . ."
                elif Girl is DoreenX:
                        ch_d "Увидимся позже, хорошо? . ."
                elif Girl is WandaX:
                        ch_w "Мы дожны позже закончить наш -диалог-."
        elif Line == "rejected":
                #if you shut her down har
                if Girl in (RogueX,KittyX):
                        $ Girl.FaceChange("sadside")
                        "[Girl.Name] выглядит удивленной и обиженной. До конца занятия она не произносит ни слова."
                else:
                        $ Girl.FaceChange("angry")
                        "[Girl.Name] выглядит удивленной и обиженной. До конца занятия она сверлит вас своим холодным взглядом."
                "Похоже ей трудно смотреть вам в глаза."
        elif Line == "caught":
                "Вы быстро отстраняетесь друг от друга и пытаетесь вернуться к занятию. . ."

        "В конце концов, [Girl.Name], кажется, успокаивается и переключает свое внимание на материалы занятия. Вы умудряетесь сделать то же самое, не заснув."
        $ Line = 0
        return

#End Frisky class content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Waiting for you content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Waiting(Girl=0,Knock=0,Buddy=0): #rkeljsvgbdw
        #if you try to enter a girl's room but she's waiting for you.
        if Girl not in TotalGirls or "switchcheck" in Girl.Traits:
                return

        $ Player.AddWord(1,"girlwaiting") #recent
        if ApprovalCheck(Girl, 1500,TabM=0) or Girl is StormX:
                #She's naked
                $ Girl.OutfitChange("nude")
        else:
                #restore base outfit
                $ Girl.OutfitChange(6)
                #She's in her underwear
                $ Girl.Over = 0
                $ Girl.Legs = 0
                $ Girl.Acc = 0
                $ Girl.Boots = 0
                $ Girl.Chest = "lace bra" if "lace bra" in Girl.Inventory else Girl.Chest
                $ Girl.Chest = "lace corset" if "lace corset" in Girl.Inventory else Girl.Chest
                $ Girl.Panties = "lace panties" if "lace panties" in Girl.Inventory else Girl.Panties
                $ Girl.Hose = "stockings and garterbelt" if "stockings and garterbelt" in Girl.Inventory else 0

        if Party and Girl is EmmaX and "taboo" not in EmmaX.History:
                #if Emma isn't down for public stuff, she waves off other girls,
                "Когда вы приближаетесь к двери, вы чувствуете легкое телепатическое давление."
                if len(Party) >=2:
                        ch_e "Дамы, пожалуйста, вернитесь в свои комнаты."
                        call Remove_Girl(Party[1])
                        "Они обе возвращаются в свои комнаты."
                else:
                        ch_e "[Party[0].Name], пожалуйста, вернись в свою комнату."
                        "[Party[0].Name] возвращается в свою комнату."
                call Remove_Girl(Party[0])
                ch_e "Извини, у меня были свои причины. . ."
                "На данный момент у вас нет причин стучаться. . ."
                $ Knock = 0

        if Knock:
                if Girl is RogueX:
                        ch_r "Заходи. . ."
                elif Girl is KittyX:
                        ch_k "О, заходи. . ."
                elif Girl is EmmaX:
                        ch_e "О, [Girl.Petname]. . . входи. . ."
                elif Girl is LauraX:
                        ch_l "Входи!"
                elif Girl is JeanX:
                        ch_j "Заходи."
                elif Girl is StormX:
                        ch_s "Можешь войти?"
                elif Girl is JubesX:
                        ch_v "Ладно, эм, заходи!"
                elif Girl is GwenX:
                        ch_g "Эм. . . заходи!"
                elif Girl is BetsyX:
                        ch_b "О, входи!"
                elif Girl is DoreenX:
                        ch_d "О, эм, заходи!"
                elif Girl is WandaX:
                        ch_w "Добро пожаловать, заходи. . ."
                "Вы открываете дверь и входите."
                $ Girl.FaceChange("sly",1)
        else:
                "Вы поворачиваете ключ и открываете дверь, входя в комнату."
                $ Girl.FaceChange("sly",1,Eyes="leftside")

        call Set_The_Scene(Chara=0,Dress=0)
        call Display_Girl(Girl,Dress=0)
        call Taboo_Level

        if ApprovalCheck(Girl, 1500,TabM=0):
                #she's nude
                "Перед вами стоит абсолютно обнаженная [Girl.Name]."
        else:
                #she's less nude
                "Перед вами стоит [Girl.Name] в нижнем белье."

        if not Knock:
                $ Girl.FaceChange("surprised",1)
                $ Girl.Statup("Obed", 50, 1)
                $ Girl.Statup("Obed", 80, 1)
                $ Girl.Statup("Inbt", 50, 1)
                if Girl is RogueX:
                        ch_r "Ох, ну, я думала, что ты постучишься. . ."
                elif Girl is KittyX:
                        ch_k "О, привет, [Girl.Petname], и почему я подумала, что ты[KittyX.like]постучишься?"
                elif Girl is EmmaX:
                        ch_e "Боюсь, я ожидала, что ты сначала постучишь. . ."
                elif Girl is LauraX:
                        ch_l "Я думала, ты постучишься или типа того."
                elif Girl is JeanX:
                    if Party:
                        $ Girl.FaceChange("sly",1)
                        ch_j "Знаешь, тебе, наверное, стоило сначала постучать, я могла быть чем-то занята."
                    else:
                        ch_j "Како-! Я не привыкла, что ко мне подкрадываются!"
                    menu:
                        extend ""
                        "Извини.":
                            $ Girl.FaceChange("smile",1)
                        ". . .":
                            $ Girl.FaceChange("sly",1)
                elif Girl is StormX:
                        ch_s "Здравствуй, [Girl.Petname]."
                elif Girl is JubesX:
                        ch_v "О, эм, [Girl.Petname]. Я думала, ты сначала постучишь. . ."
                elif Girl is GwenX:
                        if not Player.Male:
                            ch_g "О! Хорошо, ты просто взяла и вошла. . ."
                        else:
                            ch_g "О! Хорошо, ты просто взял и вошел. . ."
                elif Girl is BetsyX:
                        ch_b "Здравствуй."
                elif Girl is DoreenX:
                        ch_d ". . . Привет. . ."
                elif Girl is WandaX:
                        ch_w "О, привет."


        if Party:
                $ Girl.FaceChange("surprised",2)

                if Girl.GirlLikeCheck(Party[0]) <= 500:
                        #if the girl doesn't like your party member, she has statdowns
                        $ Girl.Statup("Love", 90, -2)
                        $ Girl.GirlLikeUp(Party[0],-5)

                $ Party[0].GirlLikeUp(Girl,5)
                if Girl is RogueX:
                        if not Player.Male:
                            ch_r "Ох, эм, ты взяла с собой [Party[0].Name_vin]. . ."
                        else:
                            ch_r "Ох, эм, ты взял с собой [Party[0].Name_vin]. . ."
                elif Girl is KittyX:
                        if not Player.Male:
                            ch_k "Ох, ты[KittyX.like]взяла с собой [Party[0].Name_vin]. . ."
                        else:
                            ch_k "Ох, ты[KittyX.like]взял с собой [Party[0].Name_vin]. . ."
                elif Girl is EmmaX:
                        ch_e "Ох, вижу, с тобой \"плюс один.\" . ."
                elif Girl is LauraX:
                        ch_l "О, смотри-ка, [Party[0].Name]."
                elif Girl is JeanX:
                        ch_j "Привет, [Party[0].Name]."
                elif Girl is StormX:
                        ch_s "Ох, здравствуй, [Party[0].Name]."
                elif Girl is JubesX:
                        ch_v "Ох, и. . . там [Party[0].Name] с тобой, да?"
                elif Girl is GwenX:
                        ch_g "[Party[0].Name]! Ты тоже здесь. . . кхм. . ."
                elif Girl is BetsyX:
                        ch_b "Ох! [Party[0].Name]. . . Я не знала, что у нас будут гости. . ."
                elif Girl is DoreenX:
                        ch_d "Ой! Я не думала, что ты приведешь компанию. . ."
                elif Girl is WandaX:
                        if not Player.Male:
                            ch_w "О, ты привела друзей!"
                        else:
                            ch_w "О, ты привел друзей!"
                if len(Party) >= 2:
                        #if there is a second girl in the party, she auto-leaves.
                        $ Party[1].Statup("Obed", 40, 1)
                        $ Party[1].Statup("Inbt", 40, 1)
                        $ Party[1].Statup("Inbt", 80, 1)
                        $ Party[1].GirlLikeUp(Girl,5)
                        call AnyLine(Party[1],"Вообще-то, мне, наверное, пора идти. . .")
                        "[Party[1].Name] выходит в коридор."
                        call Remove_Girl(Party[1])

                call Display_Girl(Party[0],Dress=0) #shows girl with you
                menu:
                    extend ""
                    "Это нормально?":
                            if (ApprovalCheck(Girl, 1500) and Girl.GirlLikeCheck(Party[0]) >= 600) or Girl in (JeanX,WandaX):
                                    #if she likes you 1500 and likes the other girl 600
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 60, 1)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 90, 1)
                                    if Girl is RogueX:
                                            ch_r "Ну, наверное."
                                    elif Girl is KittyX:
                                            ch_k "Эм, конечно, почему нет?"
                                    elif Girl is EmmaX:
                                            ch_e "Полагаю, это не будет проблемой. . ."
                                    elif Girl is LauraX:
                                            ch_l "Ага, наверное."
                                    elif Girl is JeanX:
                                            ch_j "Конечно."
                                    elif Girl is StormX:
                                            ch_s "Конечно."
                                    elif Girl is JubesX:
                                            ch_v "Ага, наверное."
                                    elif Girl is GwenX:
                                            ch_g "Конечно!"
                                    elif Girl is BetsyX:
                                            ch_b "Пожалуй, чем больше, тем лучше."
                                    elif Girl is DoreenX:
                                            ch_d "Ну. . . наверное. . ."
                                    elif Girl is WandaX:
                                            ch_w "Конечно, почему нет?"

                                    $ Girl.GirlLikeUp(Party[0],2)
                                    $ Buddy = 1
                            elif Girl is StormX:
                                            #Storm is fine with it, but stops the sex offer
                                            $ Girl.FaceChange("smile",1)
                                            ch_s "Конечно."
                            else:
                                    $ Girl.FaceChange("angry",1)
                                    $ Girl.Statup("Love", 80, -2)
                                    if Girl is RogueX:
                                            ch_r "Я так не думаю. . ."
                                    elif Girl is KittyX:
                                            ch_k "Нет, не нормально!"
                                    elif Girl is EmmaX:
                                            ch_e "Я так не думаю. . ."
                                    elif Girl is LauraX:
                                            ch_l "У меня были совсем другие планы, так что нет."
                                    elif Girl is JubesX:
                                            ch_v "Конечно нет!"
                                    elif Girl is GwenX:
                                            ch_g "Ну. . . Я ее не ждала!"
                                            $ Buddy = 1
                                    elif Girl is BetsyX:
                                            ch_b "Я не собиралась устраивать групповушку."
                                    elif Girl is DoreenX:
                                            ch_d "Я, эм. . . без обид, но я против ее компании. . ."
                                    $ Girl.GirlLikeUp(Party[0],-5)

                    "Это проблема?":
                            $ Girl.Statup("Obed", 80, 1)
                            if ApprovalCheck(Girl, 1500) or ApprovalCheck(Girl, 900, "OI") or Girl.GirlLikeCheck(Party[0]) >= 700 or Girl in (JeanX,WandaX):
                                    #if she likes you 1500 and likes the other girl 700
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 60, 2)
                                    $ Girl.Statup("Inbt", 90, 1)
                                    if Girl is RogueX:
                                            ch_r "Я так не думаю. . ."
                                    elif Girl is KittyX:
                                            ch_k "Наверное, нет. . ."
                                    elif Girl is EmmaX:
                                            ch_e "Я так не думаю."
                                    elif Girl is LauraX:
                                            ch_l "Наверное, нет."
                                    elif Girl is JeanX:
                                            $ Girl.FaceChange("confused",1)
                                            ch_j ". . . нет, почему это вообще должно быть проблемой?"
                                            $ Girl.FaceChange("sly",1)
                                    elif Girl is StormX:
                                            ch_s "Ох, вообще нет."
                                    elif Girl is JubesX:
                                            ch_v "Ох. . . .Наверное, нет."
                                    elif Girl is GwenX:
                                            ch_g "Ну. . . не особо."
                                    elif Girl is BetsyX:
                                            ch_b "Пожалуй, нет. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ну. . . наверное, нет. . ."
                                    elif Girl is WandaX:
                                            ch_w "Нет."
                                    $ Girl.GirlLikeUp(Party[0],5)
                                    $ Buddy = 1
                            elif Girl is StormX:
                                            #Storm is fine with it, but stops the sex offer
                                            $ Girl.FaceChange("smile",1)
                                            ch_s "Я не понимаю, почему ты вообще об этом спрашиваешь."
                            else:
                                    $ Girl.FaceChange("sad",1)
                                    $ Girl.Statup("Love", 60, -2)
                                    $ Girl.Statup("Love", 80, -5)
                                    $ Girl.Statup("Inbt", 60, 1)
                                    if Girl is RogueX:
                                            ch_r "Да, думаю. да. . ."
                                    elif Girl is KittyX:
                                            ch_k "Конечно, это проблема!"
                                    elif Girl is EmmaX:
                                            ch_e "Вполне возможно. . ."
                                    elif Girl is LauraX:
                                            $ Girl.FaceChange("angry",1)
                                            ch_l "Ага, и очень большая."
                                    elif Girl is JubesX:
                                            ch_v "Ага, и огромная!"
                                    elif Girl is GwenX:
                                            ch_g "Ну. . . Я ее не ждала!"
                                            $ Buddy = 1
                                    elif Girl is BetsyX:
                                            ch_b "Боюсь, что да."
                                    elif Girl is DoreenX:
                                            ch_d "Ну. . . наверное. . ."
                                    $ Girl.GirlLikeUp(Party[0],-8)

                    "Ага, она остается.":
                            $ Girl.Statup("Obed", 200, 2)
                            if ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 1200, "OI",Alt=[[WandaX],800]) or ApprovalCheck(Girl, 700, "O") or Girl.GirlLikeCheck(Party[0]) >= 800:
                                    #if she likes you 1800 or likes the other girl 800
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 90, 3)
                                    $ Girl.Statup("Inbt", 80, 1)
                                    if Girl is RogueX:
                                            ch_r "Ну, я не против. . ."
                                    elif Girl is KittyX:
                                            ch_k ". . . ладно."
                                    elif Girl is EmmaX:
                                            ch_e "Ладно, для нее найдется место. . ."
                                    elif Girl is LauraX:
                                            ch_l "Ладно. Чем больше - тем веселее."
                                    elif Girl is JeanX:
                                            ch_j "Хм. . . ладно."
                                    elif Girl is StormX:
                                            ch_s "Я бы и не хотела, чтобы было иначе."
                                    elif Girl is JubesX:
                                            ch_v "Эм, ладно. . . будет небольшой беспорядок, но ничего страшного. . ."
                                    elif Girl is GwenX:
                                            ch_g "Ну. . . Я ее не ждала!"
                                    elif Girl is BetsyX:
                                            ch_b "Если ты настаиваешь. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Эм. . . ладно. . ."
                                    elif Girl is WandaX:
                                            ch_w "Ну ладно."
                                    $ Girl.GirlLikeUp(Party[0],5)
                                    $ Buddy = 1
                            elif Girl is StormX:
                                            #Storm is fine with it, but stops the sex offer
                                            $ Girl.FaceChange("smile",1)
                                            ch_s "Конечно, будьте как дома."
                            else:
                                    $ Girl.FaceChange("angry",1)
                                    $ Girl.Statup("Love", 70, -5)
                                    $ Girl.Statup("Love", 200, -5)
                                    $ Girl.Statup("Inbt", 80, -1)
                                    if Girl is RogueX:
                                            ch_r "Ох, я так не думаю. . ."
                                    elif Girl is KittyX:
                                            ch_k "Нет!"
                                    elif Girl is EmmaX:
                                            ch_e "Мне так не кажется."
                                    elif Girl is LauraX:
                                            ch_l "Ни в коем случае."
                                    elif Girl is JeanX:
                                            ch_j "Не злоупотребляй моим гостеприимством."
                                            ch_j ". . . но какая разница."
                                            $ Buddy = 1
                                    elif Girl is JubesX:
                                            ch_v "Ни за что!"
                                    elif Girl is GwenX:
                                            ch_g "Ну. . . Я ее не ждала!"
                                    elif Girl is BetsyX:
                                            ch_b "Тогда, боюсь, тебе придется уйти."
                                    elif Girl is DoreenX:
                                            ch_d "Эм, нет. . . пусть она уйдет!"
                                    elif Girl is WandaX:
                                            ch_w "Нет, это для меня слишком."
                                    $ Girl.GirlLikeUp(Party[0],-12)

                #End menu

                if not Buddy and Party[0] is JeanX:
                        if "nowhammy" in JeanX.Traits or Girl in (EmmaX,JubesX,BetsyX):
                                ch_j "Ох, я. . . тогда пойду?"
                        else:
                                ch_j "Не волнуйся, у меня есть кое-что для нее."
                                $ Buddy = 1
                                call AnyLine(Girl,"Да, ты можешь остаться. . .")

                if not Buddy:
                        if Party[0] is RogueX:
                                ch_r "Ох. . . Пожалуй, мне пора идти. . ."
                        elif Party[0] is KittyX:
                                ch_k "Ох, эм, думаю, мне пора идти?"
                        elif Party[0] is EmmaX:
                                ch_e "Я вижу, что вы предпочли бы провести время с пользой и наедине. . ."
                        elif Party[0] is LauraX:
                                ch_l "Слушайте, я оставлю вас двоих наедине."
                        elif Party[0] is StormX:
                                ch_s "Я не хотела бы мешать. . ."
                        elif Party[0] is JubesX:
                                ch_v "Я, эм. . . не хочу мешать или типа того. . ."
                        elif Party[0] is GwenX:
                                ch_g "О, думаю, мне здесь не рады. . ."
                        elif Party[0] is BetsyX:
                                ch_b "Я бы не хотела навязываться. . ."
                        elif Party[0] is DoreenX:
                                ch_d "Наверное, мне пора. . ."
                        elif Party[0] is WandaX:
                                ch_w "Хорошо, тогда я пойду."
                        menu:
                            extend ""
                            "Ага, извини.":
                                    $ Girl.FaceChange("smile",1)
                                    $ Party[0].FaceChange("sadside",2,Mouth="smile")
                                    $ Party[0].Statup("Love", 70, -2)
                                    $ Party[0].Statup("Love", 80, -3)
                                    $ Party[0].Statup("Obed", 80, 3)
                                    $ Party[0].Statup("Inbt", 80, 1)
                                    $ Girl.Statup("Love", 70, 1)
                                    $ Girl.Statup("Love", 80, 1)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 80, 1)
                                    if Girl is RogueX:
                                            ch_r "До встречи, [Party[0].Name]."
                                    elif Girl is KittyX:
                                            ch_k "Ага, увидимся, [Party[0].Name]."
                                    elif Girl is EmmaX:
                                            ch_e "Конечно. До встречи, [Party[0].Name]."
                                    elif Girl is LauraX:
                                            ch_l "Без обид. . ."
                                    elif Girl is StormX:
                                            ch_s "Ах, [Party[0].Name], Тогда увидимся позже?"
                                    elif Girl is JubesX:
                                            ch_v "До встречи, [Party[0].Name]."
                                    elif Girl is GwenX:
                                            ch_g "Извини, [Party[0].Name]."
                                    elif Girl is BetsyX:
                                            ch_b "Мне жаль, [Party[0].Name]."
                                    elif Girl is DoreenX:
                                            ch_d "Извини за это, [Party[0].Name]. . ."
                                    elif Girl is WandaX:
                                            $ Party[0].GirlLikeUp(Girl,-5)
                                            ch_w "Ага, можешь идти, [Party[0].Name]."

                                    if Party[0] is JeanX:
                                            $ Party[0].Statup("Obed", 50, 2)
                                            $ Party[0].Statup("Obed", 80, 3)
                                    "[Party[0].Name] выходит в коридор."
                                    $ Girl.GirlLikeUp(Party[0],15)
                                    call Remove_Girl(Party[0])
                            "Нет, ты остаешься.":
                                    $ Party[0].Statup("Love", 70, 2)
                                    $ Party[0].Statup("Love", 90, 1)
                                    $ Party[0].Statup("Obed", 50, 1)
                                    $ Party[0].Statup("Obed", 90, 2)
                                    if ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 1200, "OI") or ApprovalCheck(Girl, 700, "O") or Girl.GirlLikeCheck(Party[0]) >= 800:
                                            $ Girl.FaceChange("sly",1,Brows="angry")
                                            $ Party[0].FaceChange("smile",1)
                                            $ Girl.Statup("Obed", 60, 1)
                                            $ Girl.Statup("Obed", 90, 2)
                                            $ Girl.Statup("Inbt", 80, 1)
                                            if Girl is RogueX:
                                                    ch_r "Хорошо, она может присоединиться к нам. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Ладно, как скажешь. . ."
                                            elif Girl is EmmaX:
                                                    ch_e "Полагаю, мы можем освободить место для нее. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Ладно."
                                            elif Girl is StormX:
                                                    ch_s "Пожалуй, я могу уступить. . ."
                                            elif Girl is JubesX:
                                                    ch_v "Ладно, думаю, она может остаться. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Ну. . . ладно."
                                            elif Girl is BetsyX:
                                                    ch_b "Если так нужно. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Ну. . . ладно. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Ооо, пикантненько. . ."
                                            $ Girl.GirlLikeUp(Party[0],5)
                                    elif Girl is StormX:
                                                    #Storm is fine with it, but stops the sex offer
                                                    $ Girl.FaceChange("smile",1)
                                                    $ Girl.Statup("Love", 80, -2)
                                                    $ Girl.Statup("Obed", 80, 2)
                                                    ch_s "Конечно."
                                                    return
                                    elif ApprovalCheck(Girl, 1300) and Girl.GirlLikeCheck(Party[0]) >= 500:
                                            $ Girl.FaceChange("angry",1)
                                            $ Party[0].FaceChange("sadside",2)
                                            $ Girl.Statup("Love", 70, -3)
                                            $ Girl.Statup("Love", 90, -5)
                                            $ Girl.Statup("Obed", 90, 3)
                                            $ Girl.Statup("Inbt", 50, -2)
                                            if Girl is RogueX:
                                                    ch_r "Вы испортили мне весь [Current_Time_Rus]. . ."
                                                    ch_r "Ладно, заходите, располагайтесь. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Хорошо, пусть будет так!"
                                                    ch_k "Присаживайтесь. . ."
                                            elif Girl is EmmaX:
                                                    ch_e "Что ж, все мои планы на [Current_Time_Rus] коту под хвост."
                                                    ch_e "Проходите, присаживайтесь."
                                            elif Girl is LauraX:
                                                    ch_l "У меня были планы, знаешь ли."
                                                    ch_l "Ну ладно, заходите, располагайтесь."
                                            elif Girl is JubesX:
                                                    ch_v "Нууу. . . у меня были кое - какие планы на [Current_Time_Rus]. . ."
                                                    ch_v "Но ладно, заходите, присаживайтесь. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Хорошо. . . Присаживайтесь. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Жаль."
                                                    ch_b "У меня были иные планы на [Current_Time_Rus]."
                                            elif Girl is DoreenX:
                                                    ch_d "У меня были кое-какие планы, но. . . ладно. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Ладно, думаю, мы можем поиграть в карты или еще во что-нибудь. . ."
                                            $ Girl.OutfitChange(6)
                                            "[Girl.Name] накидывает на себя одежду."
                                            $ Girl.GirlLikeUp(Party[0],-5)
                                            return
                                    else:
                                            $ Girl.FaceChange("angry",1)
                                            $ Girl.Statup("Love", 70, -3)
                                            $ Girl.Statup("Love", 90, -5)
                                            $ Girl.Statup("Inbt", 50, 1)
                                            if Girl is RogueX:
                                                    ch_r "Это неприемлемо. . ."
                                                    if not Player.Male:
                                                        ch_r "Убирайтесь, обе!"
                                                    else:
                                                        ch_r "Убирайтесь, оба!"
                                            elif Girl is KittyX:
                                                    ch_k "Ни за что!"
                                                    if not Player.Male:
                                                        ch_k "Убирайтесь отсюда, обе!"
                                                    else:
                                                        ch_k "Убирайтесь отсюда, оба!"
                                            elif Girl is EmmaX:
                                                    ch_e "Не думаю, что это решать тебе."
                                                    ch_e "Убирайтесь."
                                            elif Girl is LauraX:
                                                    ch_l "Ну уж нет."
                                                    ch_l "Убирайтесь отсюда!"
                                            elif Girl is JubesX:
                                                    ch_v "Я так не думаю!"
                                                    if not Player.Male:
                                                        ch_v "Уходите, обе!"
                                                    else:
                                                        ch_v "Уходите, оба!"
                                            elif Girl is GwenX:
                                                    ch_g "Убирайтесь!"
                                            elif Girl is BetsyX:
                                                    ch_b "Никто из вас здесь не останется."
                                            elif Girl is DoreenX:
                                                    ch_d "Нет, нет, нет. Уходите. . ."
                                            elif Girl is WandaX:
                                                    if not Player.Male:
                                                        ch_w "Нет, моя комната - мои правила, вон, обе!"
                                                    else:
                                                        ch_w "Нет, моя комната - мои правила, вон, оба!"
                                            $ Girl.GirlLikeUp(Party[0],-10)
                                            if not Player.Male:
                                                "Вы обе возвращайтесь во двор."
                                            else:
                                                "Вы оба возвращайтесь во двор."
                                            $ Girl.OutfitChange(6)
                                            $ bg_current = "bg campus"
                                            return

                            "Нет, я пойду с тобой.":
                                            $ Girl.FaceChange("angry",1,Mouth="sucking")
                                            $ Party[0].Statup("Love", 70, 2)
                                            $ Party[0].Statup("Love", 90, 1)
                                            $ Party[0].Statup("Obed", 50, 1)
                                            $ Party[0].Statup("Obed", 90, 2)
                                            $ Girl.Statup("Love", 70, -3)
                                            $ Girl.Statup("Love", 90, -5)
                                            $ Girl.Statup("Inbt", 50, 1)
                                            if not Player.Male:
                                                "Вы обе возвращайтесь во двор."
                                            else:
                                                "Вы оба возвращайтесь во двор."
                                            $ Girl.OutfitChange(6)
                                            $ Girl.GirlLikeUp(Party[0],-15)
                                            $ bg_current = "bg campus"
                                            return

                if not Party:
                    pass
                elif not ApprovalCheck(Party[0], 1000) or Party[0].SEXP <= 30 or (Girl is EmmaX and "three" not in EmmaX.History) or not Party[0].Les:
                    if Party[0] is JeanX:
                        pass
                    else:
                        #if she doesn't like you that much yet. . .
                        $ Party[0].FaceChange("sadside",2,Mouth="smile")
                        $ Girl.Statup("Obed", 80, 3)
                        $ Girl.Statup("Inbt", 80, 3)
                        if Party[0] is RogueX:
                                ch_r "Мне, наверное, пора идти. . ."
                        elif Party[0] is KittyX:
                                ch_k "Мне[KittyX.like]пора идти. . . наверное. . ."
                        elif Party[0] is EmmaX:
                                ch_e "Может, в другой раз, а пока мне пора идти. . ."
                        elif Party[0] is LauraX:
                                ch_l "Это не по мне, увидимся позже, ребята?"
                        elif Party[0] is StormX:
                                ch_s "Я не хотела бы мешать. . . Я должна уйти."
                        elif Party[0] is JubesX:
                                ch_v "Я бы не хотела вам мешать. . ."
                        elif Party[0] is GwenX:
                                ch_g "Я бы не хотел ничего прерывать. . ."
                        elif Party[0] is BetsyX:
                                ch_b "Я бы не хотела навязываться. . ."
                        elif Party[0] is DoreenX:
                                ch_d "Честно говоря, мне пора идти. . ."
                        elif Party[0] is WandaX:
                                ch_w "Мне пора идти. . ."
                        "[Party[0].Name] уходит."
                        $ Girl.GirlLikeUp(Party[0],5)
                        call Remove_Girl(Party[0])
        #end Party stuff

        call Set_The_Scene(Dress=0)
        $ Girl.FaceChange("sly",1)

        if Girl is RogueX:
                ch_r "А теперь. . . не хочешь заняться со мной чем-нибудь? . ."
        elif Girl is KittyX:
                ch_k "Ну. . . что будем делать дальше? . . ."
        elif Girl is EmmaX:
                ch_e "А теперь, думаю, ты понимаешь, чем мы займемся. . ."
        elif Girl is LauraX:
                ch_l "А теперь, что ты собираешься сделать со мной?"
        elif Girl is JeanX:
                ch_j "Ладно, тогда за работу."
        elif Girl is StormX:
                ch_s "А теперь, [Girl.Petname], я надеялась, что у тебя есть парочка похотливых идей. . ."
        elif Girl is JubesX:
                ch_v "Ну что. . . удовлетворишь парочку моих потребностей?"
        elif Girl is GwenX:
                ch_g "Ну, я думаю, ты знаешь, что делать. . ."
        elif Girl is BetsyX:
                ch_b "Ох, что ты теперь собираешься со мной делать? . ."
        elif Girl is DoreenX:
                ch_d "Ну так что. . . у тебя есть какие-нибудь интересные идеи? . ."
        elif Girl is WandaX:
                ch_w "Итак, пора перейти к делу. . ."
        call SexMenu # call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu

        return


#End Waiting for you content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Sex Change Intro Scene  //                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
#Start Intro to Rule 63 options / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rule63_Intro:
        #introduction to Rule 63 device, called on day 15
        "Вы получаете сообщение от профессора МакКоя, \"приходи в мою лабораторию, быстро.\""
        "Вы отправляетесь туда."
        ch_u "Эксперимент номер 63. . .  провал. . ."
        "В лаборатории находится шатенка в большом белом лабораторном халате."
        if not Player.Male:
            ch_u "[Player.Name], хорошо, ты пришла. . ."
        else:
            ch_u "[Player.Name], хорошо, ты пришел. . ."
        ch_u "Я работал над новым устройством, и, кажется, столкнулся с проблемой."
        menu:
            extend ""
            "Кто вы?":
                    ch_u "Это я, профессор МакКой."
            "Профессор?":
                    ch_u "О, да, это я."
        ch_mc "Я забыл, что меня трудно узнать в таком виде. . ."
        ch_mc "Я пытался создать устройство, которое бы удалило мою \"звериную\" натуру. . ."
        ch_mc "и, похоже, я превратился из \"чудовища\" в \"красотку\". . ."
        ch_mc "Я надеялся, что ты поможешь мне завершить работу над устройством, чтобы я мог вернуться в прежний облик. Ты ведь мне поможешь?"
        menu:
            extend ""
            "У меня есть срочные дела, мне нужно бежать. . .":
                    ch_mc "О, очень смешно."
            "Конечно.":
                    ch_mc "Спасибо."
            "Нет.":
                    ch_mc "Тогда мне придется настаивать."
        ch_mc "Это займет всего минуту."
        "Вы помогаете ему, пока он настраивает параметры устройства, а затем забирается внутрь."
        "После минуты или двух внутри устройства он выходит, выглядя как обычно."
        ch_mc "Это было. . . весьма познавательно."
        ch_mc "Но, очевидно, мои первоначальные исследования зашли в тупик."
        ch_mc "Я создал устройство, которое позволяет менять свой пол."
        ch_mc "Думаю, я просто оставлю его здесь, на случай, если оно кому-нибудь понадобится."
        ch_mc "В любом случае, спасибо помощь ."
        "Вы копаетесь в машине и находите загадочную записку."
        "Там написано: \"Нет, в игре не будет Зверя по правилу 63.\" [[Правило 63: у каждого персонажа непременно есть версия противоположного пола]"
        "Хм."
        "Вы возвращаетесь в свою комнату."
        $ Player.AddWord(1,0,0,0,"switcher") #adds to history
        return
#End Intro to Rule 63 options / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Xavier_Switch:
        # if "switchxavier" not in Player.History:
        #       call Xavier_Switch
        if not Player.Male:
            ch_x "А, [Player.Name], вижу, ты изменилась."
        else:
            ch_x "А, [Player.Name], вижу, ты изменился."
        $ Player.DrainWord("switchxavier",0,0,1) #removes from traits
        return

# End Sex Change Intro Scene  ////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

# Start Girltalk check  ////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
label Girltalk_Check(Girl=0,Girl2=0,BO=[]):
        #called when one girl notices you're lesbian, to see if other girls in the room have an opinion.
        #"Girl" is the girl who had the first encounter, call Girltalk_Check(RogueX)
        $ BO = TotalGirls[:]
        if Girl in BO:
                $ BO.remove(Girl)
        python:
            for BX in BO:
                if BX.Loc == bg_current:
                        Girl2 = BX
                        break

        if Girl2:
                call expression Girl2.Tag + "_Girltalk" pass (0,Girl)
        return
# End Girltalk check  ////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


## Start Sexy Photo Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Start Sexy Photo Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Sexy_Photo(Girl=0,Nudemod=0):
        #displays a sexy image of the girl, then hides it again. call Sexy_Photo(Girl)
        if Girl not in TotalGirls:
                return
        if Girl.Loc == bg_current or Girl in Nearby:
                return
        #have a check and some dialogue here
        ch_p "Слушай, не могла бы ты прислать мне фотографию?"
        if "selfie" not in Girl.History:
            if Girl is RogueX:
                    ch_r "Ты хочешь, чтобы я сделала селфи?"
            elif Girl is KittyX:
                    ch_k "О, хочешь селфи?"
            elif Girl is EmmaX:
                    ch_e "Ох, ты хочешь получить мою фотографию?"
            elif Girl is LauraX:
                    ch_l "Хочешь мое фото?"
            elif Girl is JeanX:
                    ch_j "Тебе, наверное, нужен материал для вдохновения."
            elif Girl is StormX:
                    ch_s "Желаешь получить мою фотографию?"
            elif Girl is JubesX:
                    ch_v "А, фото. . . "
            elif Girl is GwenX:
                    ch_g "Селфи?"
            elif Girl is BetsyX:
                    ch_b "О, ты хочешь мое селфи?"
            elif Girl is DoreenX:
                    ch_d "Селфи?"
            elif Girl is WandaX:
                    ch_w "Ты хочешь, чтобы я сделала селфи? . ."
        $ Girl.AddWord(1,0,"selfie",0,"selfie")  #adds tag to daily actions and history

        if Girl is EmmaX and EmmaX.Loc == "bg teacher":
            if not ApprovalCheck(Girl, 1100, TabM=2):
                ch_e "Боюсь, я сейчас веду занятие, может, попросишь позже?"
                return
            $ Tempmod -= 20
        if Girl is StormX and StormX.Loc == "bg teacher":
            if not ApprovalCheck(Girl, 1100, TabM=2):
                ch_s "В данный момент я преподаю, может, попросишь позже?"
                return
            $ Tempmod -= 20

        if Girl is RogueX:
                ch_r "Думаю, это я могу."
        elif Girl is KittyX:
                ch_k "Конечно, секундочку."
        elif Girl is EmmaX:
                ch_e "Полагаю, я могу отправить тебе ее. . ."
        elif Girl is LauraX:
                ch_l "Ага, ладно."
        elif Girl is JeanX:
                ch_j "Конечно."
        elif Girl is StormX:
                ch_s "Один момент, сейчас отправлю. . ."
        elif Girl is JubesX:
                ch_v "Конечно, без проблем."
        elif Girl is GwenX:
                ch_g "Ага, сейчас все будет."
        elif Girl is BetsyX:
                ch_b "Я могу его сделать."
        elif Girl is DoreenX:
                ch_d "Конечно. . . наверное. . ."
        elif Girl is WandaX:
                ch_w "Ладно, секунду. . ."
        $ Player.Sprite = 0     #hides player cock
        $ Trigger = 1
        $ Line = 0
        #set clothing here
        $ Girl.FaceChange("sly",1)
        menu:
            "Одежда"
            "Приподнять верхнюю часть одежды":
                $ Line = 1
                ch_p "Покажи мне свои сиськи."
                if ApprovalCheck(Girl, 1100, TabM=2) and Girl.SeenChest:
                        $ Girl.Uptop = 1
                        $ Girl.Statup("Inbt", 90, 2)
                        $ Line = 0
                elif ApprovalCheck(Girl, 500, "O", TabM=1) and Girl.SeenChest:
                        $ Girl.Uptop = 1
                        $ Girl.FaceChange("sadside",2)
                        $ Girl.Statup("Love", 80, -1)
                        $ Girl.Statup("Obed", 90, 2)
                        $ Girl.Statup("Inbt", 70, 1)
                elif Girl.Taboo:
                        call AnyLine(Girl,"Здесь не могу. . .")
                else:
                        call AnyLine(Girl,"Ни за что. . .")
            "Приспустить нижнюю часть одежды":
                $ Line = 1
                ch_p "Приспусти свои трусики."
                if ApprovalCheck(Girl, 1100, TabM=2) and Girl.SeenPussy:
                        $ Girl.Upskirt = 1
                        $ Girl.PantiesDown = 1
                        $ Line = 0
                        $ Girl.Statup("Inbt", 90, 3)
                elif ApprovalCheck(Girl, 600, "O", TabM=1) and Girl.SeenPussy:
                        $ Girl.Upskirt = 1
                        $ Girl.PantiesDown = 1
                        $ Girl.FaceChange("sadside",2)
                        $ Girl.Statup("Love", 80, -2)
                        $ Girl.Statup("Obed", 90, 3)
                        $ Girl.Statup("Inbt", 70, 1)
                elif Girl.Taboo:
                        call AnyLine(Girl,"Здесь не могу. . .")
                else:
                        call AnyLine(Girl,"Ни за что. . .")
            "Пусть покажет все":
                $ Line = 1
                ch_p "Покажи мне все."
                if ApprovalCheck(Girl, 1200, TabM=2) and Girl.SeenChest and Girl.SeenPussy:
                        $ Girl.Uptop = 1
                        $ Girl.Upskirt = 1
                        $ Girl.PantiesDown = 1
                        $ Line = 0
                        $ Girl.Statup("Inbt", 90, 4)
                elif ApprovalCheck(Girl, 600, "O", TabM=1) and Girl.SeenChest and Girl.SeenPussy:
                        $ Girl.Uptop = 1
                        $ Girl.Upskirt = 1
                        $ Girl.PantiesDown = 1
                        $ Girl.FaceChange("sadside",2)
                        $ Girl.Statup("Love", 80, -3)
                        $ Girl.Statup("Obed", 90, 4)
                        $ Girl.Statup("Inbt", 70, 2)
                else:
                        call AnyLine(Girl,"Ни за что. . .")
            "Пусть сама решает":
                $ Girl.Statup("Love", 80, 1)
                if ApprovalCheck(Girl, 1300, TabM=2) and Girl.SeenChest:
                        $ Girl.Uptop = 1
                        $ Girl.Statup("Inbt", 70, 1)
                        $ Girl.Statup("Inbt", 90, 2)
                if ApprovalCheck(Girl, 1300, TabM=2) and Girl.SeenPussy:
                        $ Girl.Upskirt = 1
                        $ Girl.PantiesDown = 1
                        $ Girl.Statup("Inbt", 70, 1)
                        $ Girl.Statup("Inbt", 90, 3)
        #set pose here
        $ Girl.Pose = 0
        if Girl.Loc != "bg teacher":
            menu:
                "Поза"
                "Стоя":
                            ch_p "Сфоткайся стоя."
                "Лежа" if Girl in (RogueX,KittyX,LauraX,JubesX,GwenX,BetsyX,DoreenX,WandaX):
                    ch_p "Почему бы тебе не прилечь. . ?"
                    if ApprovalCheck(Girl, 1000, TabM=2) or ApprovalCheck(Girl, 300, "O", TabM=1):
                            $ Girl.Pose = "sex"
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.Statup("Inbt", 70, 2)
                    elif Girl.Taboo:
                            call AnyLine(Girl,"Здесь не могу. . .")
                    else:
                            call AnyLine(Girl,"У меня никакого желания это делать. . .")
                "Лежа" if Girl in (EmmaX,JeanX,StormX):
                    ch_p "Почему бы тебе не прилечь. . ?"
                    if ApprovalCheck(Girl, 1000, TabM=2) or ApprovalCheck(Girl, 300, "O", TabM=1):
                            $ Girl.Pose = "sex"
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.Statup("Inbt", 70, 2)
                    elif Girl.Taboo:
                            call AnyLine(Girl,"Здесь не могу. . .")
                    else:
                            call AnyLine(Girl,"У меня никакого желания это делать. . .")
                "Вид сзади": #if Girl not in (DoreenX,1):
                    ch_p "Покажи мне себя сзади. . ."
                    if ApprovalCheck(Girl, 1000, TabM=2) or ApprovalCheck(Girl, 300, "O", TabM=1):
                            $ Girl.Pose = "doggy"
                            $ Girl.Statup("Inbt", 70, 1)
                            $ Girl.Statup("Inbt", 80, 3)
                    elif Girl.Taboo:
                            call AnyLine(Girl,"Здесь не могу. . .")
                    else:
                            call AnyLine(Girl,"У меня никакого желания это делать. . .")
                "Пусть сама решает":
                    if ApprovalCheck(Girl, 1000, TabM=3) or ApprovalCheck(Girl, 300, "O", TabM=1):
                            if Girl in (RogueX,KittyX,LauraX,JubesX,GwenX):
                                $ Girl.Pose = "sex"
                            else:
                                $ Girl.Pose = "doggy"
                            $ Girl.Statup("Love", 80, 1)
                            $ Girl.Statup("Inbt", 70, 2)
                            $ Girl.Statup("Inbt", 80, 3)
        #show picture here
        show PhoneSex zorder 120
        "Она присылает вам сексуальную фотку."
        #hide picture here
        hide PhoneSex

        #have some closing dialogue here
        if Girl.Upskirt or Girl.Upskirt or Girl.PantiesDown:
            $ Nudemod = 1
        menu:
            "Вау.":
                    $ Girl.Statup("Love", 80, 2+Nudemod)
                    $ Girl.Statup("Love", 90, 1)
                    $ Girl.Statup("Inbt", 60, 1+Nudemod)
                    $ Girl.Statup("Inbt", 80, 2)
            "Секси.":
                    $ Girl.Statup("Love", 80, 1)
                    $ Girl.Statup("Love", 90, 1)
                    $ Girl.Statup("Inbt", 60, 1+Nudemod)
                    $ Girl.Statup("Inbt", 80, 3)
            "Супер секси.":
                    $ Girl.Statup("Love", 80, 1+Nudemod)
                    $ Girl.Statup("Love", 90, 1)
                    $ Girl.Statup("Inbt", 60, 2)
                    $ Girl.Statup("Inbt", 80, 2+Nudemod)
            "Как скучно.":
                    $ Girl.Statup("Love", 60, -2)
                    $ Girl.Statup("Love", 80, -2-Nudemod)
                    $ Girl.Statup("Obed", 60, 2+Nudemod)
                    $ Girl.Statup("Obed", 90, 2)
                    $ Girl.Statup("Inbt", 70, -1-Nudemod)
                    $ Line = 1
            "Сойдет.":
                    $ Girl.Statup("Love", 60, -2-Nudemod)
                    $ Girl.Statup("Obed", 90, 2+Nudemod)
                    $ Girl.Statup("Inbt", 70, -1-Nudemod)
                    if not ApprovalCheck(Girl, 500, "O", TabM=1):
                            $ Line = 1
            ". . .":
                    $ Girl.Statup("Love", 80, -1)
                    $ Girl.Statup("Obed", 60, 2+Nudemod)
                    $ Girl.Statup("Obed", 90, 3)
                    $ Girl.Statup("Inbt", 50, -1-Nudemod)
                    if not ApprovalCheck(Girl, 400, "O", TabM=1):
                            $ Line = 1
        if Line:
                #you annoyed her with your response
                if Girl is RogueX:
                        ch_r "Большего ты не получишь."
                elif Girl is KittyX:
                        ch_k "Ну и ладно!"
                elif Girl is EmmaX:
                        ch_e "Следи за своим тоном."
                elif Girl is LauraX:
                        ch_l ". . ."
                elif Girl is JeanX:
                        ch_j "Что-то я не вижу благодарности."
                elif Girl is StormX:
                        ch_s "Это было не особо уважительно. . ."
                elif Girl is JubesX:
                        ch_v "Ох. . ."
                elif Girl is GwenX:
                        ch_g "Эй!"
                elif Girl is BetsyX:
                        ch_b "Как ты смеешь?"
                elif Girl is DoreenX:
                        ch_d "Ох. . ."
                elif Girl is WandaX:
                        ch_w "Как будто ты можешь сделать лучше!"
        else:
                #if things went well
                if Girl is RogueX:
                        ch_r "Оу. . ."
                elif Girl is KittyX:
                        ch_k "Хех. . ."
                elif Girl is EmmaX:
                        ch_e "Конечно. . ."
                elif Girl is LauraX:
                        ch_l "Ладно."
                elif Girl is JeanX:
                        if not Player.Male:
                            ch_j "Угу-м, значит, ты уже кончила?"
                        else:
                            ch_j "Угу-м, значит, ты уже кончил?"
                elif Girl is StormX:
                        ch_s "Я рада. . ."
                elif Girl is JubesX:
                        ch_v "Ну и славно."
                elif Girl is GwenX:
                        ch_g "Ну и здорово."
                elif Girl is BetsyX:
                        ch_b "Замечательно."
                elif Girl is DoreenX:
                        ch_d "Хех. . ."
                elif Girl is WandaX:
                        ch_w "Хех."
        $ Line = 0
        $ Trigger = 0
        $ Tempmod = 0
        $ Girl.FaceChange("normal",0)
        $ Girl.OutfitChange() #restores clothing
        return
## End Sexy Photo Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## End Sexy Photo Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Glossary
#Sleepover,Return_Player,Sleepover_Morning,Morningwood_Check,Sleepover_MorningWood,Morning_Finish

#Poly_Start,Harem_Start,Harem_Initiation

#Study_Session,Frisky_Study,

#Girls_Caught (by Xavier), Xavier_Plan

#Girl_Caught_Changing,Girl_Caught_Mastubating

#Call_For_Les, Girls_Caught_Lesing, Girl_Caught_Shower

#Pool_Sunbathe,Pool_Skinnydip,Pool_Topless

#Breakup,CheatCheck,ShareCheck,AddictCheck,Share,Cheated

#NoFap,CalltoFap,PhoneSex,MindFuck_Screen,PsychicFlash,Mindfuck

#Frisky_Class,Frisky_Class_End

#Girl_Waiting,Rule63_Intro,Xavier_Switch,Girltalk_Check, Sexy Photo
