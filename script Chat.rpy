# Start Chat menus / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Chat(Girl=0):  #rkeljsvgbdw
        if not Girl:
                menu:
                    "Поговорить с [RogueX.Name_tvo]" if RogueX.Loc == bg_current:
                            $ Girl = RogueX

                    "Поговорить с [KittyX.Name_tvo]" if KittyX.Loc == bg_current:
                            $ Girl = KittyX

                    "Поговорить с [EmmaX.Name_tvo]" if EmmaX.Loc == bg_current:
                            $ Girl = EmmaX

                    "Поговорить с [LauraX.Name_tvo]" if LauraX.Loc == bg_current:
                            $ Girl = LauraX

                    "Поговорить с [JeanX.Name_tvo]" if JeanX.Loc == bg_current:
                            $ Girl = JeanX

                    "Поговорить с [StormX.Name_tvo]" if StormX.Loc == bg_current:
                            $ Girl = StormX

                    "Поговорить с [JubesX.Name_tvo]" if JubesX.Loc == bg_current:
                            $ Girl = JubesX

                    "Поговорить с [GwenX.Name_tvo]" if GwenX.Loc == bg_current:
                            $ Girl = GwenX

                    "Поговорить с [BetsyX.Name_tvo]" if BetsyX.Loc == bg_current:
                            $ Girl = BetsyX

                    "Поговорить с [DoreenX.Name_tvo]" if DoreenX.Loc == bg_current:
                            $ Girl = DoreenX

                    "Поговорить с [WandaX.Name_tvo]" if WandaX.Loc == bg_current:
                            $ Girl = WandaX

                    "Позвонить кому-нибудь":
                        menu:
                            "Позвонить [RogueX.Name_tvo]" if RogueX.Loc != bg_current:
                                    $ Girl = RogueX

                            "Позвонить [KittyX.Name_tvo]" if KittyX.Loc != bg_current and "met" in KittyX.History:
                                    $ Girl = KittyX

                            "Позвонить [EmmaX.Name_tvo]" if EmmaX.Loc != bg_current and "met" in EmmaX.History:
                                    $ Girl = EmmaX

                            "Позвонить [LauraX.Name_tvo]" if LauraX.Loc != bg_current and "met" in LauraX.History:
                                    $ Girl = LauraX

                            "Позвонить [JeanX.Name_tvo]" if JeanX.Loc != bg_current and "met" in JeanX.History:
                                    $ Girl = JeanX

                            "Позвонить [StormX.Name_tvo]" if StormX.Loc != bg_current and "met" in StormX.History:
                                    $ Girl = StormX

                            "Позвонить [JubesX.Name_tvo]" if JubesX.Loc != bg_current and "met" in JubesX.History:
                                    $ Girl = JubesX

                            "Позвонить [GwenX.Name_tvo]" if GwenX.Loc != bg_current and "met" in GwenX.History:
                                    $ Girl = GwenX

                            "Позвонить [BetsyX.Name_tvo]" if BetsyX.Loc != bg_current and "met" in BetsyX.History:
                                    $ Girl = BetsyX

                            "Позвонить [DoreenX.Name_tvo]" if DoreenX.Loc != bg_current and "met" in DoreenX.History:
                                    $ Girl = DoreenX

                            "Позвонить [WandaX.Name_tvo]" if WandaX.Loc != bg_current and "met" in WandaX.History:
                                    $ Girl = WandaX

                            "Неважно":
                                return

                    "Неважно":
                        return
        if Girl:
                if Girl.Loc == bg_current:
                        call Taboo_Level
                        if "switchcheck" in Girl.Traits:
                                #if you recently switched sexes. . .
                                call expression Girl.Tag + "_Switch" #call Rogue_Switch
                        if "intome" in Girl.Traits or (not Player.Male and "girltalk" not in Girl.History and ApprovalCheck(Girl, 1400)):
                                #if she thinks you might be into her as a girl
                                $ Girl.DrainWord("intome",0,0,1)
                                call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

                        if Girl is EmmaX and "classcaught" not in EmmaX.History:
                                        jump Emma_Chat_Minimal

                        if "caught" in Girl.DailyActions:
                                if Girl is RogueX:
                                        ch_r "Нам, наверное, пока стоит держаться подальше друг от друга."
                                elif Girl is KittyX:
                                        ch_k "Я[Girl.like]буду держаться от тебя подальше, пока все не утихнет."
                                elif Girl is EmmaX:
                                        ch_e "Я не думаю, что нас сейчас должны видеть вместе."
                                elif Girl is LauraX:
                                        ch_l "Я думаю, нам нужно немного переждать."
                                elif Girl is JeanX:
                                        if not Player.Male:
                                            ch_j "Ты втянула меня в неприятности."
                                        else:
                                            ch_j "Ты втянул меня в неприятности."
                                elif Girl is StormX:
                                        ch_s "Вероятно, нам пока следует держаться на расстоянии друг от друга. . ."
                                elif Girl is JubesX:
                                        ch_v "Я пока хочу держаться подальше от тебя. . ."
                                elif Girl is GwenX:
                                        ch_g "Я не хочу проблем. . ."
                                elif Girl is BetsyX:
                                        ch_b "Я бы предпочла избежать дальнейшей драмы. . ."
                                elif Girl is DoreenX:
                                        ch_d "Извини, но нам пока лучше держаться подальше друг от друга. . ."
                                elif Girl is WandaX:
                                        ch_w "Я не хочу устраивать бессмысленную драму."
                                return
                        #end if "caught" in Girl.DailyActions:

                        if Girl is LauraX and Girl.Loc == bg_current and "scent" in Player.DailyActions:
                                #if you've fucked another girl, and not showered, Laura will know.
                                if not ApprovalCheck(Girl, 1700) and not ApprovalCheck(Girl, 600,"O"):
                                        $ Options = TotalGirls[:]
                                        $ Options.remove(LauraX)
                                        python:
                                            for BX in Options:
                                                if BX.Tag in Player.DailyActions and "saw with " + BX.Tag not in Girl.Traits and Girl.GirlLikeCheck(BX) <= 700:
                                                        Girl.Traits.append("saw with " + BX.Tag)
                                $ Player.DailyActions.remove("scent")


                        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(Girl, 700, "I")):
                                    if Girl.Thirst >= 30 and "refused" not in Girl.DailyActions and "quicksex" not in Girl.DailyActions:
                                            $ Girl.FaceChange("sly",1)
                                            if Girl is RogueX:
                                                    ch_r "Слушай, не хочешь немного порезвиться?"
                                            elif Girl is KittyX:
                                                    ch_k "Слушай, эм . . . не хочешь. . ."
                                                    ch_k ". . . заняться сексом?"
                                            elif Girl is EmmaX:
                                                    ch_e ". . ты не против, если мы займемся быстрым сексом?"
                                            elif Girl is LauraX:
                                                    ch_l "Слушай, не хочешь потрахаться?"
                                            elif Girl is JeanX:
                                                    ch_j "Мне бы не помешало немного снять стресс, ты не против?"
                                            elif Girl is StormX:
                                                    ch_s "Я хочу спросить, не хочешь ли ты. . ."
                                                    ch_s "\"вступить в интимную связь\" со мной?"
                                            elif Girl is JubesX:
                                                    ch_v "Слушай, ты. . . не хочешь чем-нибудь заняться?"
                                            elif Girl is GwenX:
                                                    ch_g "Итак, эм. . . потрахаемся?"
                                            elif Girl is BetsyX:
                                                    ch_b "Так вот. . . не хочешь заняться сексом?"
                                            elif Girl is DoreenX:
                                                    ch_d "Слушай. . . не хочешь пошалить?"
                                            elif Girl is WandaX:
                                                    ch_w "Не хочешь повеселиться?"
                                            call Quick_Sex(Girl)
                                            return
                        # end call Quick_Sex(Girl)

                        if "angry" not in Girl.RecentActions:
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Так о чем ты хотела поговорить, [Girl.Petname]?"
                                        else:
                                            ch_r "Так о чем ты хотел поговорить, [Girl.Petname]?"
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Так[Girl.like]о чем ты хотела поговорить, [Girl.Petname]?"
                                        else:
                                            ch_k "Так[Girl.like]о чем ты хотел поговорить, [Girl.Petname]?"
                                elif Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Что ты хотела обсудить, [Girl.Petname]?"
                                        else:
                                            ch_e "Что ты хотел обсудить, [Girl.Petname]?"
                                elif Girl is LauraX:
                                        ch_l "Да?"
                                elif Girl is JeanX:
                                        ch_j "В чем дело?"
                                elif Girl is StormX:
                                        ch_s "Что я могу для тебя сделать, [Girl.Petname]?"
                                elif Girl is JubesX:
                                        ch_v "Эй, что я могу для тебя сделать, [Girl.Petname]?"
                                elif Girl is GwenX:
                                        ch_g "Так в чем дело?"
                                elif Girl is BetsyX:
                                        ch_b "Могу я тебе чем-нибудь помочь?"
                                elif Girl is DoreenX:
                                        ch_d "Эй, что случилось?"
                                elif Girl is WandaX:
                                        ch_w "Да, в чем дело?"
                        # end if "angry" not in Girl.RecentActions:
                        call Chat_Menu
                        #call expression Girl.Tag + "_Chat_Set" pass ("chat")
                elif Girl in Digits:
                    if Girl.Loc == "hold" or "switchcheck" in Girl.Traits:
                        "Похоже, она не собирается брать трубку."
                    else:
                        if Girl is EmmaX:
                                    if EmmaX.Loc == "bg teacher" and bg_current == "bg classroom":
                                            "В ответ она отправляет вам сообщение: \"Поговорим после занятий.\""
                                            return
                                    elif "classcaught" not in EmmaX.History:
                                            call Emma_Chat_Minimal
                                            return
                        if Girl is StormX:
                                    if StormX.Loc == "bg teacher" and bg_current == "bg classroom":
                                            "В ответ она отправляет вам сообщение: \"Подожди до окончания занятий.\""
                                            return

                        if Girl is DoreenX and "doreenafter" in Player.History:
                                    "Она не берет трубку."

                        if Girl.Loc != bg_current:
                                    show Cellphone at SpriteLoc(StageLeft)
                        else:
                                    hide Cellphone
                        "Вы звоните [Girl.Name_dat]."
                        #intro dialog

                        if "les" in Girl.RecentActions:
                                #if she's with a girl. . .
                                if Girl is RogueX:
                                        ch_r "Уууф. . . подожди минутку. . ."
                                        "Вы слышите на заднем плане какую-то движуху. . ."
                                        ch_r "Эм, не обращай внимание. . ."
                                        ". . . также до вас доносятся чьи-то смешки."
                                elif Girl is KittyX:
                                        ch_k "Ах! Одну минутку. . ."
                                        "Вы слышите на заднем плане какую-то движуху. . ."
                                        ch_k "Ладно. . . (\"прекрати!\")"
                                        ". . . также до вас доносятся чьи-то смешки."
                                        ch_k "Я слушаю. . ."
                                elif Girl is EmmaX:
                                        ch_e "Секунду, [Girl.Petname]. . ."
                                        "Вы слышите на заднем плане какую-то движуху. . ."
                                        ch_e "Ладно, я вся внимание. . ."
                                        ". . . также до вас доносятся чьи-то смешки."
                                elif Girl is LauraX:
                                        ch_l "Минутку. . ."
                                        "Вы слышите на заднем плане какую-то движуху. . ."
                                        if not Player.Male:
                                            ch_l "Да, эм. . . что ты хотела?"
                                        else:
                                            ch_l "Да, эм. . . что ты хотел?"
                                        ". . . также до вас доносятся чьи-то смешки."
                                elif Girl is JeanX:
                                        ch_j "Дай мне минутку. . ."
                                        "Вы слышите на заднем плане какую-то движуху. . ."
                                        ch_j "Хорошо. . . В чём дело?"
                                        ". . . также до вас доносятся чьи-то смешки."
                                elif Girl is StormX:
                                        ch_s "Секунду, [Girl.Petname]. . ."
                                        "Вы слышите на заднем плане какую-то движуху. . ."
                                        if not Player.Male:
                                            ch_s "Что ты хотела?"
                                        else:
                                            ch_s "Что ты хотел?"
                                        ". . . также до вас доносятся чьи-то смешки."
                                elif Girl is JubesX:
                                        ch_v "О, привет! Секундочку. . ."
                                        "Вы слышите на заднем плане какую-то движуху. . ."
                                        if not Player.Male:
                                            ch_v "Эй, эй, (прекрати!) Что ты хотела? . ."
                                        else:
                                            ch_v "Эй, эй, (прекрати!) Что ты хотел? . ."
                                        ". . . также до вас доносятся чьи-то смешки."
                                        ch_v "Эм. . . не обращай внимание."
                                elif Girl is GwenX:
                                        ch_g "Да?. . . секундочку. . ."
                                        "Вы слышите на заднем плане какую-то движуху. . ."
                                        if not Player.Male:
                                            ch_g "[[перестань!] Эм, что ты хотела?"
                                        else:
                                            ch_g "[[перестань!] Эм, что ты хотел?"
                                        ". . . также до вас доносятся чьи-то смешки."
                                elif Girl is BetsyX:
                                        ch_b ". . . Да?. . . прошу, подожди секунду. . ."
                                        "Вы слышите на заднем плане какую-то движуху. . ."
                                        ch_b "[[Пожалуйста, прекрати!] Боже. . . я могу тебе чем-нибудь помочь?"
                                        ". . . также до вас доносятся чьи-то смешки."
                                elif Girl is DoreenX:
                                        ch_d ". . . эм, да? . ."
                                        "Вы слышите на заднем плане какую-то движуху. . ."
                                        ch_d "[[Прекрати! Я разговариваю по телефону!] Фух. . . тебе что-то надо?"
                                        ". . . также до вас доносятся чьи-то смешки."
                                elif Girl is WandaX:
                                        ch_w ". . . здравствуй? . ."
                                        if ApprovalCheck(Girl, 1200):
                                                ch_w "Секундочку, я тут кое-кого ласкала пальцами."
                                        else:
                                                ch_w "Эм, дай мне секунду."
                                        ch_w ". . ."
                                        if not Player.Male:
                                            ch_w "Ладно, у нас есть минутка поговорить, чего ты хотела?"
                                        else:
                                            ch_w "Ладно, у нас есть минутка поговорить, чего ты хотел?"
                        #end les call, if "les" in Girl.RecentActions:

                        if "angry" not in Girl.RecentActions:
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Так о чем ты хотела поговорить, [Girl.Petname]?"
                                        else:
                                            ch_r "Так о чем ты хотел поговорить, [Girl.Petname]?"
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Так[Girl.like]о чем ты хотела поговорить, [Girl.Petname]?"
                                        else:
                                            ch_k "Так[Girl.like]о чем ты хотел поговорить, [Girl.Petname]?"
                                elif Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Что ты хотела обсудить, [Girl.Petname]?"
                                        else:
                                            ch_e "Что ты хотел обсудить, [Girl.Petname]?"
                                elif Girl is LauraX:
                                        ch_l "Да?"
                                elif Girl is JeanX:
                                        ch_j "В чем дело?"
                                elif Girl is StormX:
                                        ch_s "Что я могу для тебя сделать, [Girl.Petname]?"
                                elif Girl is JubesX:
                                        ch_v "Эй, что я могу для тебя сделать, [Girl.Petname]?"
                                elif Girl is GwenX:
                                        ch_g "Так в чем дело?"
                                elif Girl is BetsyX:
                                        ch_b "Могу я тебе чем-нибудь помочь?"
                                elif Girl is DoreenX:
                                        ch_d "Эй, что случилось?"
                                elif Girl is WandaX:
                                        ch_w "Да, в чем дело?"
                        call Chat_Menu
                # end elif Girl in Digits:

                else:
                        "Вы не знаете ее номера, вам придется лично встретиться с ней."
        return

# Start Main Chat menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Chat_Menu: #rkeljsvgbdw
        #Primary chat menu, called by "Chat", carries over "Girl"
        $ Round -= 3 if Round >= 3 else Round
        if Round <= 10:
                if Girl in (EmmaX,StormX,BetsyX): #if it times out, drop to Wait
                        call AnyLine(Ch_Focus,"Один момент. . .")
                else:
                        call AnyLine(Ch_Focus,"Секундочку. . .")
                return
        $ Girl = GirlCheck(Girl)
        $ Girl.FaceChange()
        call Shift_Focus(Girl)
        $ Player.DrainWord("sexit")
        if Girl.Loc != bg_current:
                    show Cellphone at SpriteLoc(StageLeft)
        else:
                    hide Cellphone

        if "angry" in Girl.RecentActions:
                    if Girl is RogueX:
                            ch_r "Я совсем не хочу сейчас с тобой разговаривать."
                    elif Girl is KittyX:
                            ch_k "Я[Girl.like]сейчас очень зла на тебя!"
                    elif Girl is EmmaX:
                            ch_e "Не искушай судьбу."
                    elif Girl is LauraX:
                            ch_l "Нам не стоит сейчас видеться."
                    elif Girl is JeanX:
                            ch_j "Отвали от меня."
                    elif Girl is StormX:
                            ch_s "Тебе лучше сейчас не связываться со мной."
                    elif Girl is JubesX:
                            ch_v "Я не в настроение, [Girl.Petname]."
                    elif Girl is GwenX:
                            ch_g "Я не хочу проблем. . ."
                    elif Girl is BetsyX:
                            ch_b "Я бы предпочла не усугублять драму. . ."
                    elif Girl is DoreenX:
                            ch_d "Мы пока не можем общаться."
                    elif Girl is WandaX:
                            ch_w "Не сейчас."
                    return

        if bg_current == "bg classroom":
                    $ Girl.Facing = 0 #turns to look at you

        if Time_Count == 2 and "yesdate" in Player.DailyActions:
                #checks to see if you want to go on a date
                call Readytogo(Girl)

        if Girl is EmmaX and "noise" in Player.History:
                #asks her about noise in the attic, launching Storm meet
                call StormMeetAsk

        #intro dialog
#        if Girl is RogueX:
#                ch_r "So what did you want to talk about, [Girl.Petname]?"
#        elif Girl is KittyX:
#                ch_k "So[Girl.like]what did you want to talk about, [Girl.Petname]?"
#        elif Girl is EmmaX:
#                ch_e "What was it you wanted to discuss, [Girl.Petname]?"
#        elif Girl is LauraX:
#                ch_l "Yeah?"
        menu:
            "Приходи ко мне." if Girl.Loc != bg_current:
                        if Girl in Nearby and bg_current != "bg showerrroom":
                                call Swap_Nearby(Girl)
                        elif Room_Full():
                                "Здесь уже и так полно людей."
                                call Dismissed
                        else:
                                call expression Girl.Tag + "_Summon" #call Rogue_Summon
            "Попросить [Girl.Name_vin] уйти" if Girl.Loc == bg_current:
                                call Girl_Dismissed(Girl)
                                return

            "Ухаживать":
                    menu:
                        "Флиртовать (locked)" if Girl.Chat[5]:
                                    pass
                        "Флиртовать" if not Girl.Chat[5]:
                                    call Flirt(Girl)

                        # Modification mode
                        "Попросить показать анальную пробку." if "plug" in Girl.Inventory:
                                    call Show_Plug(Girl)
                        # -----------------

                        "Секс-меню (locked)" if Girl.Loc != bg_current:
                                    pass
                        "Секс-меню" if Girl.Loc == bg_current:
                                    if Girl.Love >= Girl.Obed:
                                            ch_p "Хочешь пошалить?"
                                    else:
                                            if not Player.Male:
                                                ch_p "Я бы хотела немного пошалить."
                                            else:
                                                ch_p "Я бы хотел немного пошалить."

                                    if not Player.Male and "girltalk" not in Girl.History:
                                            call expression Girl.Tag + "_Girltalk" #call Rogue_Girltalk
                                    if "girltalk" in Girl.History:
                                            $ Girl.DrainWord("nogirls",0,0,0,1) #history
                                    if not Player.Male and "nogirls" in Girl.History and not Girl.Forced:
                                            pass #if you cleared it on the first pass, then this will skip, otherwise, it locks out sexy mode

                                    elif "angry" in Girl.RecentActions:
                                            if Girl is RogueX:
                                                    ch_r "Я сейчас не хочу с тобой связываться."
                                            elif Girl is KittyX:
                                                    ch_k "Нет!"
                                            elif Girl is EmmaX:
                                                    ch_e "Ты прекрасно знаешь мой ответ."
                                            elif Girl is LauraX:
                                                    ch_l "Плохая идея."
                                            elif Girl is JeanX:
                                                    ch_j "Мне это совсем не интересно."
                                            elif Girl is StormX:
                                                    ch_s "Мне это не интересно."
                                            elif Girl is JubesX:
                                                    ch_v "Я не в настроение, [Girl.Petname]?"
                                            elif Girl is GwenX:
                                                    ch_g "Это вряд ли. . ."
                                            elif Girl is BetsyX:
                                                    if not Player.Male:
                                                        ch_b "Не представляю, с чего ты подумала, что я соглашусь. . ."
                                                    else:
                                                        ch_b "Не представляю, с чего ты подумал, что я соглашусь. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Я сейчас немного зла на тебя. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Не сейчас."
                                    elif "caught" in Ch_Focus.RecentActions:
                                            call Sex_Menu_Dialog(Ch_Focus,"caught") #ch_d "I'm just happy to be here, I don't want to get in trouble."
                                    elif ApprovalCheck(Girl, 600, "LI"):
                                            $ Girl.FaceChange("sexy")
                                            if Girl is RogueX:
                                                    ch_r "Хах, ладно, [Girl.Petname]."
                                            elif Girl is KittyX:
                                                    ch_k "Мммм, ладно, [Girl.Petname]."
                                            elif Girl is EmmaX:
                                                    ch_e "Возможно я не против. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Клево."
                                            elif Girl is JeanX:
                                                    ch_j "Да?"
                                            elif Girl is StormX:
                                                    ch_s "Ох?"
                                            elif Girl is JubesX:
                                                    ch_v "Да?"
                                            elif Girl is GwenX:
                                                    ch_g "Ох? . ."
                                            elif Girl is BetsyX:
                                                    ch_b "О?"
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. Да?"
                                            elif Girl is WandaX:
                                                    ch_w "Конечно."
                                            call SexMenu # call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu
                                            $ Player.DrainWord("sexit")
                                            return
                                    elif ApprovalCheck(Girl, 400, "OI"):
                                            if Girl is RogueX:
                                                    ch_r "Если ты этого хочешь, [Girl.Petname]."
                                            elif Girl is KittyX:
                                                    ch_k "Да, [Girl.Petname]."
                                            elif Girl is EmmaX:
                                                    ch_e "Если ты этого хочешь, [Girl.Petname]."
                                            elif Girl is LauraX:
                                                    ch_l "Да, [Girl.Petname]."
                                            elif Girl is JeanX:
                                                    ch_j "Если ты хочешь. . ."
                                            elif Girl is StormX:
                                                    ch_s "Хорошо."
                                            elif Girl is JubesX:
                                                    if not Player.Male:
                                                        ch_v "Что бы ты хотела, [Girl.Petname]?"
                                                    else:
                                                        ch_v "Что бы ты хотел, [Girl.Petname]?"
                                            elif Girl is GwenX:
                                                    ch_g "Что ты хочешь мне предложить? . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Да?"
                                            elif Girl is DoreenX:
                                                    ch_d "Ладно."
                                            elif Girl is WandaX:
                                                    ch_w "Конечно."
                                            call SexMenu # call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu
                                            $ Player.DrainWord("sexit")
                                            return
                                    else:
                                            if Girl is RogueX:
                                                    ch_r "Мне это совсем не интересно, [Girl.Petname]."
                                            elif Girl is KittyX:
                                                    ch_k "Нет, спасибо, [Girl.Petname]."
                                            elif Girl is EmmaX:
                                                    ch_e "Нет, благодарю, [Girl.Petname]."
                                            elif Girl is LauraX:
                                                    ch_l "Нет, спасибо, [Girl.Petname]."
                                            elif Girl is JeanX:
                                                    ch_j "Не интересует."
                                            elif Girl is StormX:
                                                    ch_s "Мне это неинтересно."
                                            elif Girl is JubesX:
                                                    ch_v "Неее, я не увлекаюсь подобным."
                                            elif Girl is GwenX:
                                                    ch_g "Неа. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Я не в настроении, [Girl.Petname]. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох, эм. . . нет. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Хех, нет."

                        "Грязный разговор (locked)" if Girl.SEXP < 10:
                                        pass
                        "Грязный разговор" if Girl.SEXP >= 10:
                                        ch_p "О том, когда мы наедине. . ."
                                        $ Line = 0
                                        call expression Girl.Tag + "_SexChat" #call Rogu_SexChat

                        "Свидание (locked)" if Time_Count > 2:
                                        pass
                        "Свидание"  if Time_Count <= 2:
                                        ch_p "Не хочешь сходить сегодня вечером на свидание?"
                                        call Date_Ask(Girl)

                        "Подарок (locked)" if Girl.Loc != bg_current:
                                        pass
                        "Подарок" if Girl.Loc == bg_current:
                                        ch_p "У меня кое-что есть для тебя."
                                        call Gifts #(Girl)
                        "Назад":
                                        pass

            "Поговорить":
                    menu:
                        "Я просто хотела поговорить. . ." if not Player.Male:
                                    call expression Girl.Tag + "_Chitchat" #call Rogue_Chitchat
                        "Я просто хотел поговорить. . ." if Player.Male:
                                    call expression Girl.Tag + "_Chitchat" #call Rogue_Chitchat
                        "Об отношениях":
                                    ch_p "Мы можем поговорить о нас?"
                                    call Shift_Focus(Girl)
                                    if Girl.Loc == bg_current:
                                        call expression Girl.Tag + "_Relationship" #call Rogue_Relationship
                                    else:
                                        if Girl is RogueX:
                                                ch_r "Похоже, будет сложно поговорить о таком по телефону."
                                                ch_r "Давай при встрече?"
                                        elif Girl is KittyX:
                                                ch_k "Лучше нам поговорить об этом при встрече."
                                                ch_k "Может, отложим этот разговор до личной встречи?"
                                        elif Girl is EmmaX:
                                                ch_e "Это не телефонный разговор."
                                                ch_e "Возможно, поговорим при встрече."
                                        elif Girl is LauraX:
                                                ch_l "Похоже, будет тяжелый разговор."
                                                ch_l "Может позже, когда мы встретимся лицом к лицу?"
                                        elif Girl is JeanX:
                                                ch_j "Лучше ведь поговорить при встрече, хорошо?"
                                        elif Girl is StormX:
                                                ch_s "Такие разговоры ведутся с глазу на глаз."
                                                ch_s "Возможно, будет лучше поговорить об этом при встрече."
                                        elif Girl is JubesX:
                                                ch_v "Нуу, звучит как-то зловеще."
                                                ch_v "Может быть поговорим, когда увидимся лично?"
                                        elif Girl is GwenX:
                                                ch_g "Ого, звучит серьезно. . ."
                                                ch_g "Может при личной встрече?"
                                        elif Girl is BetsyX:
                                                ch_b "Мне кажется, это не телефонный разговор."
                                                ch_b "Давай поговорим об этом при встречи."
                                        elif Girl is DoreenX:
                                                ch_d "Ох. . . звучит довольно серьезно. . ."
                                                ch_d "Мне кажется, нам стоит поговорить об этом лицом к лицу. . ."
                                        elif Girl is WandaX:
                                                ch_w "Мне кажется, нам следует обсудить лицом к лицу."

                        "О других девушках":
                                    menu:
                                        "Что ты думаешь о. . ."
                                        "[RogueX.Name_pre]?" if Girl is not RogueX:
                                                call expression Girl.Tag + "_About" pass (RogueX)
                                        "[KittyX.Name_pre]?" if Girl is not KittyX and "met" in KittyX.History:
                                                call expression Girl.Tag + "_About" pass (KittyX)
                                        "[EmmaX.Name_pre]?" if Girl is not EmmaX and "met" in EmmaX.History:
                                                call expression Girl.Tag + "_About" pass (EmmaX)
                                        "[LauraX.Name_pre]?" if Girl is not LauraX and "met" in LauraX.History:
                                                call expression Girl.Tag + "_About" pass (LauraX)
                                        "[JeanX.Name_pre]?" if Girl is not JeanX and "met" in JeanX.History:
                                                call expression Girl.Tag + "_About" pass (JeanX)
                                        "[StormX.Name_pre]?" if Girl is not StormX and "met" in StormX.History:
                                                call expression Girl.Tag + "_About" pass (StormX)
                                        "[JubesX.Name_pre]?" if Girl is not JubesX and "met" in JubesX.History:
                                                call expression Girl.Tag + "_About" pass (JubesX)
                                        "[GwenX.Name_pre]?" if Girl is not GwenX and "met" in GwenX.History:
                                                call expression Girl.Tag + "_About" pass (GwenX)
                                        "[BetsyX.Name_pre]?" if Girl is not BetsyX and "met" in BetsyX.History:
                                                call expression Girl.Tag + "_About" pass (BetsyX)
                                        "[DoreenX.Name_pre]?" if Girl is not DoreenX and "met" in DoreenX.History:
                                                call expression Girl.Tag + "_About" pass (DoreenX)
                                        "[WandaX.Name_pre]?" if Girl is not WandaX and "met" in WandaX.History:
                                                call expression Girl.Tag + "_About" pass (WandaX)
                                        ". . . своих отношениях с другими девушками. . ?":
                                                call expression Girl.Tag + "_Monogamy" #call Rogue_Monogamy
                                        "Неважно.":
                                                pass

                        "Могу я узнать твой номер телефона?" if Girl not in Digits:
                                    if Girl is EmmaX and ApprovalCheck(Girl, 800, "LI"):
                                            ch_e "Почему бы и нет."
                                            $ Digits.append(Girl)
                                    elif Girl is not EmmaX and (ApprovalCheck(Girl, 400, "L") or ApprovalCheck(Girl, 200, "I")):
                                            if Girl is RogueX:
                                                    ch_r "Конечно, думаю ничего страшного не случится."
                                            elif Girl is KittyX:
                                                    ch_k "Боже[Girl.like]конечно."
                                            elif Girl is LauraX:
                                                    ch_l "Ох, конечно."
                                            elif Girl is JeanX:
                                                    ch_j "А? Ладно."
                                            elif Girl is StormX:
                                                    ch_s "Ох? Конечно."
                                            elif Girl is JubesX:
                                                    ch_v "Да, конечно."
                                            elif Girl is GwenX:
                                                    ch_g "Конечно!"
                                            elif Girl is BetsyX:
                                                    ch_b "Безусловно."
                                            elif Girl is DoreenX:
                                                    ch_d "О. . . конечно!"
                                            elif Girl is WandaX:
                                                    ch_w "Конечно."
                                            $ Digits.append(Girl)
                                    elif ApprovalCheck(Girl, 200, "O",Alt=[[EmmaX],500-EmmaX.Inbt]):
                                            if Girl is RogueX:
                                                    ch_r "Ладно, если ты так этого хочешь."
                                            elif Girl is KittyX:
                                                    ch_k "[Girl.Like]ладно."
                                            elif Girl is EmmaX:
                                                    ch_e "Хмм. . . хорошо, дай мне свой телефон."
                                            elif Girl is LauraX:
                                                    ch_l "Думаю, можешь."
                                            elif Girl is JeanX:
                                                    ch_j "А? Ладно."
                                            elif Girl is StormX:
                                                    ch_s "Почему бы и нет."
                                            elif Girl is JubesX:
                                                    ch_v "Наверное?"
                                            elif Girl is GwenX:
                                                    ch_g "Ох, конечно. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Конечно."
                                            elif Girl is DoreenX:
                                                    ch_d "Конечно. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Конечно."
                                            $ Digits.append(Girl)
                                    else:
                                            if Girl is RogueX:
                                                    if not Player.Male:
                                                        ch_r "Если честно, я не хочу, чтобы ты звонила мне."
                                                    else:
                                                        ch_r "Если честно, я не хочу, чтобы ты звонил мне."
                                            elif Girl is KittyX:
                                                    ch_k "[Girl.Like]лучше не надо."
                                            elif Girl is EmmaX:
                                                    ch_e "Не думаю, что студентам стоит знать мой номер."
                                            elif Girl is LauraX:
                                                    ch_l "Эм, наверное, нет."
                                            elif Girl is JeanX:
                                                    ch_j "Будет лучше, если ты не сможешь мне позвонить."
                                            elif Girl is StormX:
                                                    ch_s "Я предпочла бы не давать тебе свой номер."
                                            elif Girl is JubesX:
                                                    ch_v "Нее, будет лучше, если меня не будет в твоих контактах."
                                            elif Girl is GwenX:
                                                    if not Player.Male:
                                                        ch_g "Ты не думала, что у меня вообще может не быть телефона? . ."
                                                    else:
                                                        ch_g "Ты не думал, что у меня вообще может не быть телефона? . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Боюсь, что у меня не местный номер."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. . . я так не думаю. . ."
                                            elif Girl is WandaX:
                                                    ch_w "У меня нет телефона."

                        "Рассказать ей о [DoreenX.Name_pre]" if Girl is StormX and "SGattic" in Player.History:
                                    call DoreenStormReport(1)
                        "Назад":
                                    pass

            "Изменить что-нибудь в ней":
                        call Girl_Settings

            "Добавить ее в группу" if Girl not in Party and Girl.Loc == bg_current:
                        ch_p "Можешь немного походить со мной?"
                        if Girl is EmmaX and ApprovalCheck(Girl, 1250):
                                $ Party.append(Girl)
                                ch_e "Веди."
                                return
                        if ApprovalCheck(Girl, 600,Alt=[[EmmaX,JeanX],900]):
                                $ Party.append(Girl)
                                if Girl is RogueX:
                                        ch_r "Ладно, куда идем?"
                                elif Girl is KittyX:
                                        ch_k "[Girl.Like]куда пойдем?"
                                elif Girl is EmmaX:
                                        ch_e "Лучше бы тебе не надоедать мне."
                                elif Girl is LauraX:
                                        ch_l "Куда мы направляемся?"
                                elif Girl is JeanX:
                                        ch_j "Эм, конечно."
                                elif Girl is StormX:
                                        ch_s "Ох, конечно."
                                elif Girl is JubesX:
                                        ch_v "Конечно, куда идем?"
                                elif Girl is GwenX:
                                        ch_g "Ладно, куда пойдем?"
                                elif Girl is BetsyX:
                                        if not Player.Male:
                                            ch_b "Куда бы ты хотела отправиться?"
                                        else:
                                            ch_b "Куда бы ты хотел отправиться?"
                                elif Girl is DoreenX:
                                        ch_d "Ох. . . ладно, куда пойдем?"
                                elif Girl is WandaX:
                                        ch_w "Конечно. Куда пойдем?"
                                return
                        elif not ApprovalCheck(Girl, 400):
                                if Girl is RogueX:
                                        ch_r "Эм, нет, спасибо."
                                elif Girl is KittyX:
                                        ch_k "Фи, нет."
                                elif Girl is EmmaX:
                                        ch_e "Я не могу представить, зачем мне это."
                                elif Girl is LauraX:
                                        ch_l "Нет."
                                elif Girl is JeanX:
                                        ch_j "Что? Нет."
                                elif Girl is StormX:
                                        ch_s "Хм, нет, благодарю."
                                elif Girl is JubesX:
                                        ch_v "Неее, я не увлекаюсь подобным."
                                elif Girl is GwenX:
                                        ch_g "Я. . . так не думаю. . ."
                                elif Girl is BetsyX:
                                        ch_b "Я бы предпочла остаться здесь."
                                elif Girl is DoreenX:
                                        ch_d "Я лучше останусь здесь. . ."
                                elif Girl is WandaX:
                                        ch_w "Я пока останусь здесь."
                        else:
                                if Girl is RogueX:
                                        ch_r "Мне и здесь хорошо, спасибо."
                                elif Girl is KittyX:
                                        ch_k "Думаю, я лучше останусь здесь."
                                elif Girl is EmmaX:
                                        ch_e "Лучше откажусь."
                                elif Girl is LauraX:
                                        ch_l "Я не хочу."
                                elif Girl is JeanX:
                                        ch_j "Что? Нет."
                                elif Girl is StormX:
                                        ch_s "Мне и здесь комфортно."
                                elif Girl is JubesX:
                                        ch_v "Неа."
                                elif Girl is GwenX:
                                        ch_g "Я за тобой не пойду."
                                elif Girl is BetsyX:
                                        ch_b "Я считаю, что это довольно неуместно."
                                elif Girl is DoreenX:
                                        ch_d "Эм, нет, спасибо. . ."
                                elif Girl is WandaX:
                                        ch_w "Эм, нет."

            "Распустить группу" if Girl in Party:
                        ch_p "Ладно, можешь идти, если хочешь."
                        $ Options = Party[:]
                        while Options:
                                $ Party.remove(Options[0])
                                call Girls_Schedule([Options[0]],0)
                                if "leaving" in Options[0].RecentActions:
                                        $ Options[0].DrainWord("leaving")
                                if Options[0] is RogueX:
                                        if Options[0].Loc == bg_current:
                                                ch_r "Ладно, я, наверное, останусь еще ненадолго."
                                        else:
                                                ch_r "Ладно, увидимся позже."
                                elif Options[0] is KittyX:
                                        if Options[0].Loc == bg_current:
                                                ch_k "Буду знать, но мне[Options[0].like]и здесь хорошо."
                                        else:
                                                ch_k "Отлично, до встречи."
                                elif Options[0] is EmmaX:
                                        if Options[0].Loc == bg_current:
                                                if not Player.Male:
                                                    ch_e "Я рада, что ты мне \"разрешила\" уйти, но я бы предпочла остаться."
                                                else:
                                                    ch_e "Я рада, что ты мне \"разрешил\" уйти, но я бы предпочла остаться."
                                        elif Options[0].Loc == "bg teacher" and bg_current == "bg classroom":
                                                if not Player.Male:
                                                    ch_e "Я рада, что ты мне \"разрешила\" уйти, но мне {i}нужно{/i} преподавать."
                                                else:
                                                    ch_e "Я рада, что ты мне \"разрешил\" уйти, но мне {i}нужно{/i} преподавать."
                                        else:
                                                ch_e "Если это все, то увидимся позже."
                                elif Options[0] is LauraX:
                                        if Options[0].Loc == bg_current:
                                                ch_l "Думаю, мне и здесь хорошо."
                                        else:
                                                ch_l "Ладно, тогда увидимся."
                                elif Options[0] is JeanX:
                                        #if Options[0].Loc == bg_current:
                                                #ch_j "Ok."
                                        #else:
                                                ch_j "Ладно."
                                elif Options[0] is StormX:
                                        if Options[0].Loc == bg_current:
                                                ch_s "Я бы предпочла остаться, спасибо."
                                        elif Options[0].Loc == "bg teacher" and bg_current == "bg classroom":
                                                ch_s "Мне нужно вести занятия. Я остаюсь."
                                        else:
                                                ch_s "Ах, хорошо, увидимся позже."
                                elif Options[0] is JubesX:
                                        if Options[0].Loc == bg_current:
                                                ch_v "Хорошо, но я останусь здесь."
                                        else:
                                                ch_v "Ладно-ладно. Увидимся."
                                elif Options[0] is GwenX:
                                        if Options[0].Loc == bg_current:
                                                ch_g "Ладно."
                                                "[[Она остается.]"
                                        else:
                                                ch_g "Ладно, увидимся!"
                                elif Options[0] is BetsyX:
                                        if Options[0].Loc == bg_current:
                                                ch_b "Я бы предпочла остаться, если ты не возражаешь."
                                        else:
                                                ch_b "Пожалуй, я пойду."
                                elif Options[0] is DoreenX:
                                        if Options[0].Loc == bg_current:
                                                ch_d "Я бы. . . хотела остаться."
                                        else:
                                                ch_d ". . . Пожалуй, я пойду. . ."
                                elif Options[0] is WandaX:
                                        if Options[0].Loc == bg_current:
                                                ch_w "Пока что я останусь здесь."
                                        else:
                                                ch_w "Конечно."
                                if Options[0].Loc != bg_current:
                                        call Set_The_Scene
                                $ Options.remove(Options[0])
                        return

            "Переключиться на. . .":
                    call Switch_Chat

            # Modification mode
            # -----------------
            "{color=#FDCA6E}Меню Характеристик{/color}":
                call info_stats_menu
            # -----------------

            "Неважно.":
                        if Girl is RogueX:
                                ch_r "Ладно, тогда в другой раз."
                        elif Girl is KittyX:
                                ch_k "Ладно, пока."
                        elif Girl is EmmaX:
                                ch_e "Тогда поговорим в другой раз."
                        elif Girl is LauraX:
                                ch_l "Ладно."
                        elif Girl is JeanX:
                                ch_j "Ладно?"
                        elif Girl is StormX:
                                ch_s "Хорошо."
                        elif Girl is JubesX:
                                ch_v "Лады. . ."
                        elif Girl is GwenX:
                                ch_g "Ладно. . ."
                        elif Girl is BetsyX:
                                ch_b "До свидания."
                        elif Girl is DoreenX:
                                ch_d "Ладно, пока. . ."
                        elif Girl is WandaX:
                                ch_w "Хорошо, увидимся."
                        if bg_current == "bg classroom":
                                    $ Girl.Facing = 1 #turns to look at you
                        return
        jump Chat_Menu
# End Main Chat menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Switch_Chat(Gift=0): #rkeljsvgbdw
    #called from Main Chat, Settings, or Wardrobe
    # if Gift, only allows people who are local
    if bg_current == "HW Party":
            "Вам придется пойти к остальным девушкам, если вы хотите с ними поговорить."
            return
    $ Line = Girl
    menu:
        "[RogueX.Name]" if Girl is not RogueX and (not Gift or RogueX.Loc == bg_current):
                $ Girl = RogueX
        "[KittyX.Name]" if Girl is not KittyX and "met" in KittyX.History and (not Gift or KittyX.Loc == bg_current):
                $ Girl = KittyX
        "[EmmaX.Name]" if Girl is not EmmaX and "met" in EmmaX.History and (not Gift or EmmaX.Loc == bg_current):
                $ Girl = EmmaX
        "[LauraX.Name]" if Girl is not LauraX and "met" in LauraX.History and (not Gift or LauraX.Loc == bg_current):
                $ Girl = LauraX
        "[JeanX.Name]" if Girl is not JeanX and "met" in JeanX.History and (not Gift or JeanX.Loc == bg_current):
                $ Girl = JeanX
        "[StormX.Name]" if Girl is not StormX and "met" in StormX.History and (not Gift or StormX.Loc == bg_current):
                $ Girl = StormX
        "[JubesX.Name]" if Girl is not JubesX and "met" in JubesX.History and (not Gift or JubesX.Loc == bg_current):
                $ Girl = JubesX
        "[GwenX.Name]" if Girl is not GwenX and "met" in GwenX.History and (not Gift or GwenX.Loc == bg_current):
                $ Girl = GwenX
        "[BetsyX.Name]" if Girl is not BetsyX and "met" in BetsyX.History and (not Gift or BetsyX.Loc == bg_current):
                $ Girl = BetsyX
        "[DoreenX.Name]" if Girl is not DoreenX and "met" in DoreenX.History and (not Gift or DoreenX.Loc == bg_current):
                $ Girl = DoreenX
        "[WandaX.Name]" if Girl is not WandaX and "met" in WandaX.History and (not Gift or WandaX.Loc == bg_current):
                $ Girl = WandaX
        "Неважно":
                $ Line = 0
                return

    if bg_current != "bg classroom":
            call Girl_Pos_Reset(Line)
    if Girl.Loc != bg_current:
        if Girl in Digits:
                "Вы звоните [Girl.Name_dat]."
                if Girl is EmmaX and "classcaught" not in EmmaX.History:
                    ch_e "У меня сейчас нет времени на разговоры со студентами."
                    $ Girl = Line
        else:
                    "У вас нет ее номера телефона."
                    $ Girl = Line
    if Girl is EmmaX and "classcaught" not in EmmaX.History:
            ch_e "Конечно, обсудить это позже. . . наедине."
            $ Girl = Line
            $ Line = 0
            return
    call Shift_Focus(Girl)

    call Set_The_Scene
    if bg_current == "bg classroom":
            call Class_Setting
    if "angry" not in Girl.RecentActions and Girl != Line:
            if Girl is RogueX:
                    if not Player.Male:
                        ch_r "Так о чем ты хотела поговорить, [Girl.Petname]?"
                    else:
                        ch_r "Так о чем ты хотел поговорить, [Girl.Petname]?"
            elif Girl is KittyX:
                    if not Player.Male:
                        ch_k "Так[Girl.like]о чем ты хотела поговорить, [Girl.Petname]?"
                    else:
                        ch_k "Так[Girl.like]о чем ты хотел поговорить, [Girl.Petname]?"
            elif Girl is EmmaX:
                    if not Player.Male:
                        ch_e "Что ты хотела обсудить, [Girl.Petname]?"
                    else:
                        ch_e "Что ты хотел обсудить, [Girl.Petname]?"
            elif Girl is LauraX:
                    ch_l "Да?"
            elif Girl is JeanX:
                    ch_j "В чем дело?"
            elif Girl is StormX:
                    ch_s "Что я могу для тебя сделать, [Girl.Petname]?"
            elif Girl is JubesX:
                    ch_v "Эй, что я могу для тебя сделать, [Girl.Petname]?"
            elif Girl is GwenX:
                    ch_g "В чем дело?"
            elif Girl is BetsyX:
                    ch_b "Могу я тебе чем-нибудь помочь?"
            elif Girl is DoreenX:
                    ch_d "Эй! Что случилось?"
            elif Girl is WandaX:
                    ch_w "Да, в чем дело?"
    $ Line = 0
    return

# Start Girl_Dismissed / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Dismissed(Girl=0,Leaving = 0): #rkeljsvgbdw
    $ Girl = GirlCheck(Girl)
    if Girl in Party:
            $ Party.remove(Girl)
    call Girls_Schedule([Girl],0)
    #if Girl.Loc == bg_current then it means she wants to stay here
    if "leaving" in Girl.RecentActions:
                $ Girl.DrainWord("leaving")
    menu:
        "Ты можешь уйти, если хочешь.":
                if Girl.Loc == bg_current and not ApprovalCheck(Girl, 700, "O"):
                        if Girl is RogueX:
                                ch_r "Спасибо, но я лучше останусь."
                        elif Girl is KittyX:
                                ch_k "Ну, думаю, я останусь."
                        elif Girl is EmmaX:
                                ch_e "Я все равно останусь здесь ненадолго."
                        elif Girl is LauraX:
                                ch_l "Ладно. [[Кажется, она не собирается уходить. . .]"
                        elif Girl is JeanX:
                                ch_j "Ладно. [[Кажется, она не собирается уходить. . .]"
                        elif Girl is StormX:
                                ch_s "Я тебя услышала. [[Кажется, она не собирается уходить. . .]"
                        elif Girl is JubesX:
                                ch_v "Лады. . . [[Кажется, она не собирается уходить. . .]"
                        elif Girl is GwenX:
                                ch_g "Ладно. [[Кажется, она не собирается уходить. . .]"
                        elif Girl is BetsyX:
                                ch_b "Как скажешь. . . [[Кажется, она не собирается уходить. . .]"
                        elif Girl is DoreenX:
                                ch_d "Думаю, я останусь. . . [[Кажется, она не собирается уходить. . .]"
                        elif Girl is WandaX:
                                ch_w "О, я пока останусь. . . [[Кажется, она не собирается уходить. . .]"
                else:
                        if Girl is RogueX:
                                ch_r "Хорошо. Увидимся позже."
                        elif Girl is KittyX:
                                ch_k "Ладно, до встречи!"
                        elif Girl is EmmaX:
                                ch_e "Хорошо, [Girl.Petname]"
                        elif Girl is LauraX:
                                ch_l "Ладно."
                        elif Girl is JeanX:
                                ch_j "Ладно."
                        elif Girl is StormX:
                                ch_s "Ладно тогда."
                        elif Girl is JubesX:
                                ch_v "Лады. . ."
                        elif Girl is GwenX:
                                ch_g "Ладно!"
                        elif Girl is BetsyX:
                                ch_b "Конечно."
                        elif Girl is DoreenX:
                                ch_d "Ладно, пока. . ."
                        elif Girl is WandaX:
                                ch_w "Хорошо, увидимся."
                        $ Leaving = 1
                # End "You can leave if you like."
        "Не могла бы ты уйти?":
                if Girl.Loc == bg_current and not ApprovalCheck(Girl, 800, "LO"):
                        if Girl is RogueX:
                                ch_r "Я лучше останусь."
                        elif Girl is KittyX:
                                ch_k "Мне сейчас некуда уходить."
                        elif Girl is EmmaX:
                                ch_e "Так уж получилось, что других планов сейчас у меня нет."
                        elif Girl is LauraX:
                                ch_l "Никто меня не выгонит [[Она остается на месте]."
                        elif Girl is JeanX:
                                ch_j "Что? Нет."
                        elif Girl is StormX:
                                ch_s "Я лучше останусь."
                        elif Girl is JubesX:
                                ch_v "Неа, мне и здесь хорошо."
                        elif Girl is GwenX:
                                ch_g "А? Нет, я бы хотела остаться здесь."
                        elif Girl is BetsyX:
                                ch_b "Боюсь, что я вынуждена отказаться."
                        elif Girl is DoreenX:
                                ch_d "Эм. . . нет."
                        elif Girl is WandaX:
                                ch_w "Хех, нет."
                elif not ApprovalCheck(Girl, 500, "LO"):
                        if Girl is RogueX:
                                ch_r "Думаю, я лучше останусь."
                        elif Girl is KittyX:
                                ch_k "Ага. . . нет."
                        elif Girl is EmmaX:
                                ch_e "Не думаю, что смогу."
                        elif Girl is LauraX:
                                ch_l "Неа."
                        elif Girl is JeanX:
                                ch_j "Что? Нет."
                        elif Girl is StormX:
                                ch_s "Нет, благодарю."
                        elif Girl is JubesX:
                                ch_v "Нее, мне и здесь хорошо."
                        elif Girl is GwenX:
                                ch_g "Я хочу остаться."
                        elif Girl is BetsyX:
                                ch_b "Я бы предпочла посмотреть, чем все обернется."
                        elif Girl is DoreenX:
                                ch_d "Я вроде как хочу посмотреть, чем все обернется. . ."
                        elif Girl is WandaX:
                                ch_w "Здесь весело."
                else:
                        if "dismissed" not in Girl.DailyActions:
                                $ Girl.Statup("Obed", 30, 5)
                                $ Girl.Statup("Obed", 50, 5)
                        if Girl is RogueX:
                                ch_r "Без проблем, увидимся позже."
                        elif Girl is KittyX:
                                ch_k "Конечно."
                        elif Girl is EmmaX:
                                ch_e "Хорошо. . ."
                        elif Girl is LauraX:
                                ch_l "Ладно."
                        elif Girl is JeanX:
                                ch_j "Как скажешь."
                        elif Girl is StormX:
                                ch_s "Ладно."
                        elif Girl is JubesX:
                                ch_v "Хорошо. . ."
                        elif Girl is GwenX:
                                ch_g "Ладно. . ."
                        elif Girl is BetsyX:
                                ch_b "Отлично."
                        elif Girl is DoreenX:
                                ch_d "Ладно, пока. . ."
                        elif Girl is WandaX:
                                ch_w "Хорошо, увидимся."
                        $ Leaving = 1
                #end "Could you give me the room please?"
        "Теперь ты можешь идти.":
                if Girl.Loc == bg_current and not ApprovalCheck(Girl, 500, "O"):
                        if Girl is RogueX:
                                ch_r "Думаю, я останусь."
                        elif Girl is KittyX:
                                ch_k "Эм, нет."
                        elif Girl is EmmaX:
                                ch_e "Нет, не думаю, что смогу."
                        elif Girl is LauraX:
                                ch_l "Нет, я не хочу."
                        elif Girl is JeanX:
                                ch_j "Ладно. [[Похоже, она не собирается уходить]"
                        elif Girl is StormX:
                                ch_s "Но я лучше останусь."
                        elif Girl is JubesX:
                                ch_v "Ага, но я не уйду."
                        elif Girl is GwenX:
                                ch_g "Ага, ладно. [[Похоже, она не собирается уходить]"
                        elif Girl is BetsyX:
                                ch_b "Конечно. [[Похоже, она не собирается уходить]"
                        elif Girl is DoreenX:
                                ch_d "Ладно. . . [[Похоже, она не собирается уходить]"
                        elif Girl is WandaX:
                                ch_w "Конечно, конечно. [[Она не собирается уходить]"
                elif not ApprovalCheck(Girl, 300, "O"):
                        $ Girl.FaceChange("confused")
                        if Girl is RogueX:
                                ch_r "Ну, если ты хочешь, чтобы я ушла, тогда, видимо, мне стоит остаться."
                        elif Girl is KittyX:
                                ch_k "Не тогда, когда мне любопытно."
                        elif Girl is EmmaX:
                                ch_e "Теперь я заинтригована."
                        elif Girl is LauraX:
                                ch_l "Зачем?"
                        elif Girl is JeanX:
                                ch_j "Угу. [[Похоже, она не собирается уходить]"
                        elif Girl is StormX:
                                ch_s "А?"
                        elif Girl is JubesX:
                                ch_v "Почему это?"
                        elif Girl is GwenX:
                                ch_g "А? Зачем? Чем ты собираешься заняться?"
                        elif Girl is BetsyX:
                                ch_b "Теперь я заинтересована. . ."
                        elif Girl is DoreenX:
                                ch_d "Я хочу посмотреть. . ."
                        elif Girl is WandaX:
                                ch_w "Здесь весело."
                else:
                        if "dismissed" not in Girl.DailyActions:
                                $ Girl.Statup("Obed", 40, 10)
                                $ Girl.Statup("Obed", 60, 5)
                        if Girl is RogueX:
                                ch_r "Если ты этого хочешь."
                        elif Girl is KittyX:
                                ch_k "Эм, ладно."
                        elif Girl is EmmaX:
                                ch_e "Хорошо. . ."
                        elif Girl is LauraX:
                                ch_l "Ладно."
                        elif Girl is JeanX:
                                ch_j "Как скажешь."
                        elif Girl is StormX:
                                ch_s "Ладно."
                        elif Girl is JubesX:
                                ch_v "Ох, ладно. . ."
                        elif Girl is GwenX:
                                ch_g "Ох. . ."
                        elif Girl is BetsyX:
                                ch_b "Конечно."
                        elif Girl is DoreenX:
                                ch_d "Ладно, пока. . ."
                        elif Girl is WandaX:
                                ch_w "Ладно, увидимся."
                        $ Leaving = 1
                #end "You can go now."
        "Неважно.":
                        return

    if not Leaving and bg_current in ("bg campus","bg classroom","bg dangerroom"):
            #if there is space nearby. . .
            call Remove_Girl(Girl,1,1)
    elif not Leaving:
            #if she's refused to leave yet. . .
            menu:
                extend ""
                "Я настаиваю, уходи.":
                        if Girl.Loc != bg_current and (ApprovalCheck(Girl, 1200, "LO") or ApprovalCheck(Girl, 500, "O")):
                                #If she has someplace to be and is obedient
                                if "dismissed" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 70, -5, 1)
                                        $ Girl.Statup("Obed", 50, 10)
                                        $ Girl.Statup("Obed", 80, 5)
                                if Girl is RogueX:
                                        ch_r "Хорошо, раз ты настаиваешь, я уйду."
                                elif Girl is KittyX:
                                        ch_k "Эм, ладно."
                                elif Girl is EmmaX:
                                        ch_e "Хорошо. . ."
                                elif Girl is LauraX:
                                        ch_l "Ладно, хорошо."
                                elif Girl is JeanX:
                                        ch_j ". . ."
                                        ch_j "Ладно."
                                elif Girl is StormX:
                                        ch_s ". . . Ладно."
                                elif Girl is JubesX:
                                        ch_v "Ладно, хорошо. . ."
                                elif Girl is GwenX:
                                        ch_g "Ох. . ."
                                elif Girl is BetsyX:
                                        ch_b "Конечно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох, ладно. . ."
                                elif Girl is WandaX:
                                        ch_w "Уф, ладно."
                                $ Leaving = 1
                        elif Girl.Loc != bg_current and (ApprovalCheck(Girl, 1000, "LO") or ApprovalCheck(Girl, 300, "O")):
                                #If she has someplace to be and is less obedient
                                if "dismissed" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 50, -5, 1)
                                        $ Girl.Statup("Love", 70, -5, 1)
                                        $ Girl.Statup("Obed", 50, 10)
                                        $ Girl.Statup("Obed", 80, 5)
                                $ Girl.FaceChange("angry")
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Ладно, если ты собираешься вести себя как стерва."
                                        else:
                                            ch_r "Ладно, если ты собираешься вести себя как мудак."
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Ладно, дура!"
                                        else:
                                            ch_k "Ладно, придурок!"
                                elif Girl is EmmaX:
                                        ch_e "Я уйду, но больше испытывай мое терпение, [Girl.Petname]"
                                elif Girl is LauraX:
                                        ch_l "У меня все равно остались незаконченные дела."
                                elif Girl is JeanX:
                                        ch_j ". . ."
                                        ch_j "Ох, я совсем забыла, мне нужно еще сделать... кое-что."
                                elif Girl is StormX:
                                        ch_s "Что ж, у меня как раз оставались кое-какие незаконченные дела."
                                elif Girl is JubesX:
                                        ch_v "Как скажешь. . ."
                                elif Girl is GwenX:
                                        ch_g "Ну. . . ладно. . ."
                                elif Girl is BetsyX:
                                        ch_b "Ладно, как пожелаешь. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ладно. . . Думаю, я могу найти себе другое занятие. . ."
                                elif Girl is WandaX:
                                        ch_w "Ладно, потом я выясню, к чему все это было."
                                $ Leaving = 1
                        elif Girl.Loc != bg_current:
                                #If she has someplace to be but is not obedient
                                if "dismissed" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 50, -5, 1)
                                        $ Girl.Statup("Love", 70, -10, 1)
                                        $ Girl.Statup("Obed", 50, -5)
                                        $ Girl.Statup("Inbt", 50, 5)
                                        $ Girl.Statup("Inbt", 80, 3)
                                $ Girl.FaceChange("angry")
                                if Girl is RogueX:
                                        ch_r "Чёрта с два."
                                elif Girl is KittyX:
                                        ch_k "Неееа."
                                elif Girl is EmmaX:
                                        ch_e "Теперь точно нет."
                                elif Girl is LauraX:
                                        if not Player.Male:
                                            ch_l "Нет, пока я не увижу, что ты задумала."
                                        else:
                                            ch_l "Нет, пока я не увижу, что ты задумал."
                                elif Girl is JeanX:
                                        ch_j "Прозвучало как-то не весело."
                                elif Girl is StormX:
                                        ch_s "Теперь мне определенно стоит остаться."
                                elif Girl is JubesX:
                                        ch_v "Нуу, теперь я -точно- останусь здесь. . ."
                                elif Girl is GwenX:
                                        ch_g "Ох, это прозвучало -так- хорошо. . ."
                                elif Girl is BetsyX:
                                        ch_b "Я так не думаю."
                                elif Girl is DoreenX:
                                        ch_d "Теперь мне -ужасно- любопытно. . ."
                                elif Girl is WandaX:
                                        ch_w "Теперь мне еще интереснее."
                        elif ApprovalCheck(Girl, 1400, "LO") or ApprovalCheck(Girl, 400, "O"):
                                #If she has nowhere to be to be but is obedient
                                if "dismissed" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 50, -5, 1)
                                        $ Girl.Statup("Obed", 50, 10)
                                        $ Girl.Statup("Obed", 80, 5)
                                $ Girl.FaceChange("sad")
                                if Girl is RogueX:
                                        ch_r "Ладно, если ты этого хочешь."
                                elif Girl is KittyX:
                                        ch_k "Эм, конечно."
                                elif Girl is EmmaX:
                                        ch_e "Ладно, не буду тебе мешать."
                                elif Girl is LauraX:
                                        ch_l "Ладно."
                                elif Girl is JeanX:
                                        ch_j "Как скажешь."
                                elif Girl is StormX:
                                        ch_s "Ладно."
                                elif Girl is JubesX:
                                        ch_v "Ладно, хорошо. . ."
                                elif Girl is GwenX:
                                        ch_g "Ох. . . ладно."
                                elif Girl is BetsyX:
                                        ch_b "Ну хорошо."
                                elif Girl is DoreenX:
                                        ch_d "Ох, ладно. . ."
                                elif Girl is WandaX:
                                        ch_w "Ладно."
                                $ Leaving = 1
                        else:
                                #If she has nowhere to be to be and is not obedient
                                if "dismissed" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 50, -5, 1)
                                        $ Girl.Statup("Love", 70, -10, 1)
                                        $ Girl.Statup("Obed", 50, -5)
                                        $ Girl.Statup("Inbt", 50, 3)
                                        $ Girl.Statup("Inbt", 80, 2)
                                $ Girl.FaceChange("sad")
                                if Girl is RogueX:
                                        ch_r "Этого хочешь ты, а не я."
                                elif Girl is KittyX:
                                        ch_k "Ну, нет."
                                elif Girl is EmmaX:
                                        ch_e "Не думаю, что это произойдет."
                                elif Girl is LauraX:
                                        ch_l "Неа."
                                elif Girl is JeanX:
                                        ch_j "Что? Нет."
                                elif Girl is StormX:
                                        ch_s "Ох, конечно же нет."
                                elif Girl is JubesX:
                                        ch_v "Неа. . ."
                                elif Girl is GwenX:
                                        ch_g "Ха!"
                                elif Girl is BetsyX:
                                        ch_b "Могу притвориться, что мне не все равно."
                                elif Girl is DoreenX:
                                        ch_d "Я тебя услышала."
                                elif Girl is WandaX:
                                        ch_w "Хех, нет."
                        #end "I insist, get going."
                "Ладно, неважно.":
                                pass

    if "dismissed" not in Girl.DailyActions:
            $ Girl.DailyActions.append("dismissed")
    if Girl in Nearby:
            "Вы немного отходите от [Girl.Name_rod]."
    elif Leaving == 0:
            # Stay
            $ Girl.Loc = bg_current
    else:
            # Go
            if Girl.Loc != bg_current: #it stays the same
                pass
            elif bg_current == Girl.Home:
                $ Girl.Loc = "bg campus"
            else:
                $ Girl.Loc = Girl.Home

            if Girl in Present:
                    $ Present.remove(Girl)
            call AllReset(Girl)
            "[Girl.Name] уходит."
    return
    #end "you can leave"
# End Girl_Dismissed / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Flirt menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Flirt(Girl =0): #rkeljsvgbdw
    # call Flirt(RogueX)
    $ Girl = GirlCheck(Girl)
    call Shift_Focus(Girl)

    if Girl.Chat[5]:
            "Она уже слишком поражена вашим обаянием, возможно, вам стоит попробовать позже."
            return
    if Girl.Loc != bg_current:
        while not Girl.Chat[5]:
            #menu for if over the phone
            menu:
                "Сделать комплимент":
                        $ Girl.Chat[5] = 1 #can only flirt once per cycle.
                        call Compliment(Girl)
#                "Say you love her":
#                            call Love_You(Girl)
                "Попросить сделать сексуальное селфи":
                        if Girl in Nearby:
                                "Она сейчас рядом."
                        else:
                                $ Girl.Chat[5] = 1 #can only flirt once per cycle.
                                call Sexy_Photo(Girl)
                "Секс по телефону" if bg_current == "bg player":
                        ch_p "Хочешь заняться сексом по телефону?"
                        call Taboo_Level(0)
#                        if not ApprovalCheck(Girl, 900) or Girl.SEXP < 15:
#                                #she hates the idea
#                                $ Girl.Statup("Love", 70, -2)
#                                $ Girl.Statup("Love", 90, -2)
#                                $ Girl.Statup("Obed", 60, 2)
#                                $ Girl.Statup("Inbt", 40, 2)
#                                if Girl is RogueX: #R_Mast
#                                        ch_r "You have -got- to be kidding me. . ."
#                                elif Girl is KittyX:
#                                        ch_k "Are you[Girl.like]serious?!"
#                                elif Girl is EmmaX:
#                                        ch_e "That would be extremely inappropriate."
#                                elif Girl is LauraX:
#                                        ch_l "What? No."
#                                elif Girl is JeanX:
#                                        ch_j "Pretty sketch."
#                                elif Girl is StormX:
#                                        ch_s "Definitely not."
#                                elif Girl is JubesX:
#                                        ch_v "Def not. . ."
#                                elif Girl is GwenX:
#                                        ch_g "Heheh. . . oh, no!"
#                                elif Girl is BetsyX:
#                                        ch_b "How ghastly."
#                                elif Girl is DoreenX:
#                                        ch_d "Whoa! What?"
#                                elif Girl is WandaX:
#                                        ch_w "Heh, no."
#                                return
                        if Girl.Taboo and ApprovalCheck(Girl, 1400):
                                #she agrees to move
                                if Girl is RogueX: #R_Mast
                                        ch_r "Хмм. . . а это может быть весело. . ."
                                        ch_r "Мне нужно поскорее вернуться в свою комнату. . ."
                                elif Girl is KittyX:
                                        ch_k "Хихи, хочешь представления? . ."
                                        ch_k "Позволь мне сначала вернуться в свою комнату. . ."
                                elif Girl is EmmaX:
                                        ch_e "Я думаю, мы могли этим заняться. . ."
                                        ch_e "Дай мне минутку. . ."
                                elif Girl is LauraX:
                                        ch_l "Ага, можно, подожди минутку. . ."
                                        ch_l "Мне сначала нужно дойти до комнаты. . ."
                                elif Girl is JeanX:
                                        ch_j "А, наверное?"
                                        ch_j "Дай мне минуту на подготовку. . ."
                                elif Girl is StormX:
                                        ch_s "Это может быть забавно, дай мне одну минуту. . ."
                                elif Girl is JubesX:
                                        ch_v "О. . . это может быть весело. . ."
                                        ch_v "Позволь мне только найти место. . ."
                                elif Girl is GwenX:
                                        ch_g "Оооо. . ."
                                        ch_g "Эм, давай я сначала найду местечко. . ."
                                elif Girl is BetsyX:
                                        ch_b "Я согласна, но не здесь. . ."
                                        ch_b "Подожди немного."
                                elif Girl is DoreenX:
                                        ch_d "Ну. . ."
                                        ch_d "Не здесь. . . сейчас вернусь в комнату. . ."
                                elif Girl is WandaX:
                                        ch_w "Хорошо, я в деле, но сначала мне нужно вернуться в свою комнату."
                                if Girl in (EmmaX,StormX) and Girl.Loc == "bg classroom" and Time_Count >= 2:
                                        pass             #if it's Emma and she's in class and it's a good time, stay
                                else:
                                        $ Girl.Loc = Girl.Home
                        elif ApprovalCheck(Girl, 1200):
                                #she agrees
                                if Girl is RogueX: #R_Mast
                                        ch_r "Хмм. . . а это может быть весело. . ."
                                elif Girl is KittyX:
                                        ch_k "Хихи, хочешь представления? . ."
                                elif Girl is EmmaX:
                                        ch_e "Я думаю, мы могли этим заняться. . ."
                                elif Girl is LauraX:
                                        ch_l "Ага, можно, подожди минутку. . ."
                                elif Girl is JeanX:
                                        ch_j "Да, конечно. . ."
                                elif Girl is StormX:
                                        ch_s "Конечно, один момент. . ."
                                elif Girl is JubesX:
                                        ch_v "Ох, как эротично. . . конечно, секундочку. . ."
                                elif Girl is GwenX:
                                        ch_g "Оооо. . . ладно."
                                elif Girl is BetsyX:
                                        ch_b "Я согласна. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох, эм . . . звучит весело! Секундочку. . ."
                                elif Girl is WandaX:
                                        ch_w "Звучит весело."
                        elif Girl.Taboo:
                                #she doesn't agree because public
                                if Girl is RogueX:
                                        ch_r "Я сейчас не у себя, так что не могу."
                                elif Girl is KittyX:
                                        ch_k "Хихи, извини, я сейчас на улице."
                                elif Girl is EmmaX:
                                        ch_e "Боюсь, я сейчас немного занята. . ."
                                elif Girl is LauraX:
                                        ch_l "Я сейчас не в безопасном месте, может, в другой раз. . ."
                                elif Girl is JeanX:
                                        ch_j "Здесь, знаешь ли, довольно людно. . ."
                                elif Girl is StormX:
                                        ch_s "Боюсь, здесь слишком людно. . ."
                                elif Girl is JubesX:
                                        ch_v "Я, вроде как, сейчас занята. . ."
                                elif Girl is GwenX:
                                        ch_g "Я немного занята. . ."
                                elif Girl is BetsyX:
                                        ch_b "Боюсь, я сейчас не могу."
                                elif Girl is DoreenX:
                                        ch_d "Сейчас я ну никак не могу. . ."
                                elif Girl is WandaX:
                                        ch_w "Я сейчас не у себя."
                                return
                        else:
                                #she doesn't agree
                                if Girl is RogueX: #R_Mast
                                        ch_r "Я. . . эм. . . я не знаю. . ."
                                elif Girl is KittyX:
                                        ch_k "Хихи. . . эм, думаю, я не смогу. . ."
                                elif Girl is EmmaX:
                                        ch_e "Я бы предпочла таким не заниматься. . ."
                                elif Girl is LauraX:
                                        ch_l "Нет, не хочу, чтобы за мной снова наблюдали. . ."
                                elif Girl is JeanX:
                                        ch_j "Лучше не стоит."
                                elif Girl is StormX:
                                        ch_s "Я так не думаю."
                                elif Girl is JubesX:
                                        ch_v "Неее, я не увлекаюсь подобным. . ."
                                elif Girl is GwenX:
                                        ch_g "Ха, нет. . ."
                                elif Girl is BetsyX:
                                        ch_b "Боже, нет."
                                elif Girl is DoreenX:
                                        ch_d "Ох, нет, спасибо. . ."
                                elif Girl is WandaX:
                                        ch_w "Хех, нет."
                                return
                        $ Girl.Statup("Obed", 70, 2)
                        $ Girl.Statup("Inbt", 80, 2)
                        call Taboo_Level(0)
                        $ Girl.Chat[5] = 1 #can only flirt once per cycle.
                        call PhoneSex(Girl)
                        call Taboo_Level(0)
                        $ renpy.pop_call() #skips past ChatMenu, returns to room
                        return
                "Секс по телефону [[не здесь] (locked)" if bg_current != "bg player":
                        pass
                "Неважно [[выход]":
                        pass
    else:
        while not Girl.Chat[5]:
            #Menu for if local.
            $ Girl.Chat[5] = 1 #can only flirt once per cycle.
            menu:
                "Милый флирт":
                    menu:
                        "Сделать комплимент":
                                call Compliment(Girl)

                        "Признаться в любви":
                                call Love_You(Girl)

                        "Коснуться ее щеки":
                                call TouchCheek(Girl)

                        "Взять ее за руки":
                                call Hold_Hands(Girl)

                        "Погладить ее по голове":
                                call Girl_Headpat(Girl)

                        "Поцеловать ее в щечку":
                                call Kiss_Cheek

                        "Поцеловать ее в губы":
                                call Kiss_Lips

                        "Обнять":
                                call Hug

                        "Погладить ее по плечам":
                                call Rub_Shoulders

                        "Назад":
                                $ Girl.Chat[5] = 0

                "Сексуальный флирт":
                    menu:
                        "Шлепнуть ее по заднице":
                                call Slap_Ass(Girl)

                        "Ущипнуть ее за задницу":
                                call Pinch_Ass

                        "Задрать ее юбку" if Girl.PantsNum() == 5 and not Girl.Upskirt:
                                call Flip_Skirt

                        "Схватить ее за грудь":
                                call Grab_Tit

                        "Попросить у нее трусики":
                                call AskPanties(Girl)

                        "Попросить вставить вибратор" if "vibein" not in Girl.DailyActions:
                                call Ask_Vibrator(Girl)
                        "Попросить вытащить вибратор" if "vibein" in Girl.DailyActions:
                                call Ask_Vibrator(Girl)

                        "Попросить незаметно стащить чью-нибудь одежду" if Girl is KittyX:
                                call Kitty_Yoink

                        "Назад":
                                $ Girl.Chat[5] = 0

                "Неважно [[выход]":
                        $ Girl.Chat[5] = 0
                        return
    return

#End flirt core menu. / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Compliments / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Compliment(Girl=0,Line0=0,Line1=0,Line2=0,Options=[],CountList=[],Line=0,D20=0): #rkeljsvgbdw
    #called from the flirt menu, picked three random options from the Options list
    #player picks one, then that outcome is evaluated to determine stat outcomes.
    #call Compliment(Girl)

    $ Options = ["Ты отлично потренировалась в комнате Опасности", #0
                "Хорошо поработала на занятиях",             #1
                "Сегодня ты выглядишь особенно привлекательно",         #2
                "Знаешь, ты красавица",                          #3
                "Прости, я теряюсь в твоих глазах",           #4
                "В последнее время ты выглядишь очень подтянутой",           #5
                "У тебя очень красивая грудь",               #6
                "Твоя попка выглядит просто великолепно",                  #7
                "О, что это за аромат? Он тебе очень подходит",      #8
                "Ты мне очень нравишься"]

    $ CountList = [0,1,2,3,4,5,6,7,8,9]
    $ renpy.random.shuffle(CountList)

    $ Line0 = Options[CountList[0]] #let's say, this is 7
    $ Line1 = Options[CountList[1]]
    $ Line2 = Options[CountList[2]]
    menu:
            "[Line0]":
                $ Line = CountList[0] # Line would now = 7, corresponding to the 7th entry in Options
            "[Line1]":
                $ Line = CountList[1]
            "[Line2]":
                $ Line = CountList[2]
            "(Надо придумать варианты получше. . .)":
                ch_p "Эм. . ."
                $ Girl.Statup("Love", 50, -1)
                $ Girl.Statup("Obed", 40, -1)
                call Compliment(Girl)
                return
            "Неважно":
                $ Girl.Chat[5] = 0 #can only flirt once per cycle.
                return

    $ D20 = renpy.random.randint(5, 20)
    if Girl is JubesX:
            $ D20 += 3

    #responses based on compliment <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <>
    if Line == 0:
            #"You really nailed that Danger Room exercise",  #0
            if ApprovalCheck(Girl, 1000):
                    $ D20 += 5

            $ Girl.Statup("Love", 60, 3)
            if Girl is LauraX:
                    $ Girl.Statup("Love", 40, 3)
                    if D20 >= 10:
                            $ Girl.FaceChange("smile")
                            $ Girl.Statup("Love", 80, 2)
                            $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.Statup("Lust", 50, 2)
                            ch_l "Думаешь, я не знаю?"
                            ch_l "У этих жестянок не было ни единого шанса!"
                    else:
                            $ Girl.FaceChange("angry",1,Eyes="side")
                            $ Girl.Statup("Inbt", 50, 1)
                            ch_l "Спасибо. . ."
                            ch_l "Не знаю, похоже, я пропустила одного Стража."
                            ch_l "Я должна стать еще лучше."
                            $ Girl.FaceChange("normal",0)
            elif Girl is JeanX:
                    $ Girl.Statup("Love", 40, 3)
                    $ Girl.Statup("Love", 80, 2)
                    $ D20 -= 5
                    if D20 >= 10:
                            $ Girl.FaceChange("smile")
                            $ Girl.Statup("Obed", 60, 2)
                            ch_j "Да, так и есть."
                    else:
                            $ Girl.FaceChange("angry",1,Eyes="side")
                            $ Girl.Statup("Inbt", 80, 2)
                            if D20 >= 9:
                                    ch_j "Ага, я знаю, но, я считаю, [EmmaX.Name] справилась очень плохо."
                                    ch_j "Уверена, она бы тоже хотела иметь телекинез. . ."
                            elif D20 >= 8:
                                    ch_j "Ага, я знаю, Но, я считаю, [KittyX.Name] облажалась."
                                    ch_j "Да, она может становиться бесплотной, но все же. . ."
                            elif D20 >= 7:
                                    ch_j "Ага, я знаю, но [RogueX.Name] врезалась в меня и чуть не высосала все мои силы."
                                    ch_j "Обычно она полный отстой. . ."
                            elif D20 >= 6:
                                    ch_j "Ага, я знаю, но [LauraX.Name] чуть не отрубила мне голову."
                                    ch_j "А это одна из лучших моих частей!"
                            else:
                                    $ Girl.Statup("Inbt", 90, 2)
                                    if not Player.Male:
                                        ch_j "Ага, я знаю, но ты была очень плоха."
                                    else:
                                        ch_j "Ага, я знаю, но ты был очень плох."
                                    ch_j "Похоже, твоя сила бесполезна против роботов. . ."
                            $ Girl.FaceChange("normal",0)
            if Girl is GwenX:
                    $ Girl.Statup("Love", 40, 3)
                    $ Girl.FaceChange("smile")
                    if D20 >= 15:
                            $ Girl.Statup("Love", 80, 2)
                            $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.Statup("Lust", 50, 2)
                            ch_g "Верно! Это было так весело!"
                            ch_g "Почему они не откроют это место для всех?!"
                            ch_g "Можно срубить легкие деньги!"
                    else:
                            $ Girl.Statup("Inbt", 50, 1)
                            ch_g "Да, думаю, я тихонько совершенствуюсь. . ."
                            ch_g "Как говорит Батрок: \"всегда прыгай.\""
            else:
                    $ Girl.Statup("Obed", 60, 2)
                    if D20 >= 15:
                            $ Girl.FaceChange("smile")
                            $ Girl.Statup("Love", 60, 1)
                            $ Girl.Statup("Obed", 60, 2)
                            $ Girl.Statup("Inbt", 60, 1)
                            if Girl is StormX:
                                    ch_s "Да, думаю, что у меня хорошо получилось."
                            elif Girl is BetsyX:
                                    ch_b "Я верю, что становлюсь лучше. . ."
                            else:
                                    call AnyLine(Girl,"Да, думаю, я действительно отлично справилась.")
                    elif D20 >= 10:
                            $ Girl.FaceChange("bemused",2)
                            $ Girl.Statup("Love", 60, 1)
                            $ Girl.Statup("Obed", 60, 1)
                            call AnyLine(Girl,"И все же я думаю, что нет предела совершенству.")
                    else:
                            $ Girl.FaceChange("bemused",1,Eyes="side")
                            $ Girl.Statup("Love", 80, 1)
                            call AnyLine(Girl,"Я ценю твою поддержку, но мы оба знаем, что я могла бы и лучше.")
                            $ Girl.FaceChange("smile")
            #"You really nailed that Danger Room exercise",  #0
    elif Line == 1:
            #"Great job in class the other day",             #1
            if not ApprovalCheck(Girl, 700):
                    $ D20 -= 5

            if D20 >= 10:
                    $ Girl.Statup("Love", 70, 2)
                    $ Girl.Statup("Obed", 60, 1)
                    if Girl is KittyX:
                            $ Girl.FaceChange("smile")
                            $ Girl.Statup("Love", 80, 2)
                            $ Girl.Statup("Inbt", 50, 1)
                            ch_k "Спасибо, [KittyX.Petname]!"
                            ch_k "Числа словно говорили со мной."
                    elif Girl is EmmaX or Girl is StormX:
                            $ Girl.FaceChange("bemused")
                            $ Girl.Statup("Love", 80, 2)
                            if not Player.Male:
                                call AnyLine(Girl,"Я рада, что ты обратила на это внимание, "+Girl.Petname+".")
                            else:
                                call AnyLine(Girl,"Я рада, что ты обратил на это внимание, "+Girl.Petname+".")
                    elif Girl is JeanX:
                            $ Girl.Statup("Love", 80, 2)
                            ch_j "Спасибо, это было не трудно."
                    elif Girl is BetsyX:
                            ch_b "Я очень старалась."
                    else:
                            $ Girl.FaceChange("confused")
                            call AnyLine(Girl,"Спасибо?")
            else:
                    $ Girl.FaceChange("bemused")
                    $ Girl.Statup("Love", 60, 1)
                    $ Girl.Statup("Inbt",50, 1)
                    if Girl is KittyX:
                            ch_k "Да, я несомненно выложилась на все сто."
                            $ D20 += 5
                    elif Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Я удивлена, что ты обратила на это внимание."
                            else:
                                ch_e "Я удивлена, что ты обратил на это внимание."
                    elif Girl is JeanX:
                            $ Girl.Statup("Love", 80, 2)
                            ch_j "Спасибо, это было не трудно."
                            $ Girl.Statup("Love", 80, -1)
                            $ Girl.Statup("Obed", 60, 2)
                            $ Girl.FaceChange("confused",1)
                            ch_j "Подожди-ка. . ."
                    elif Girl is StormX:
                            if not Player.Male:
                                ch_s "Значит ты не спала. Теперь я должна Эмме выпивку."
                            else:
                                ch_s "Значит ты не спал. Теперь я должна Эмме выпивку."
                    elif Girl is BetsyX:
                            ch_b "Я на это надеюсь."
                    elif Girl is DoreenX:
                            ch_d "Ага, это было так интересно!"
                    else:
                            call AnyLine(Girl,"Да, все прошло неплохо. Хотя и немного скучно.")
            #"Great job in class the other day",             #1
    elif Line == 2:
            #"You're looking extra beautiful today",         #2
            if not ApprovalCheck(Girl, 900):
                    $ D20 -= 10
            if Girl in (RogueX, KittyX, JeanX, JubesX,BetsyX):
                    $ D20 += 5

            $ Girl.Statup("Inbt", 50, 2)
            if Girl is LauraX:
                    $ Girl.FaceChange("confused",1)
                    $ Girl.Statup("Love", 80, 1, 1)
                    $ Girl.Statup("Obed", 60, 2)
                    ch_l ". . ."
                    ch_l "Ладно?"
            elif D20 >= 10:
                    $ Girl.FaceChange("bemused",2)
                    $ Girl.Statup("Love", 70, 2)
                    $ Girl.Statup("Love", 90, 2)
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Ну разве ты не милая."
                            else:
                                ch_r "Ну разве ты не милый."
                    elif Girl is KittyX:
                            if not Player.Male:
                                ch_k "Ах, ты такая милая."
                            else:
                                ch_k "Ах, ты такой милый."
                    elif Girl is EmmaX:
                            ch_e "Ну, я стараюсь. . ."
                    elif Girl is JeanX:
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 90, 2)
                            ch_j "Поздравляю, у тебя есть глаза."
                    elif Girl is StormX:
                            ch_s "Я стремлюсь к \"большему.\""
                    elif Girl is JubesX:
                            ch_v "Оу, спасибо!"
                    elif Girl is GwenX:
                            ch_g "Хехехе. . ."
                    elif Girl is BetsyX:
                            ch_b "Утонченность требует усилий."
                    elif Girl is DoreenX:
                            $ Girl.FaceChange("surprised",2)
                            ch_d "Кто? Я? Ты правда так думаешь?"
                    elif Girl is WandaX:
                            ch_w "Хмм. . . спасибо. . ."
                    $ Girl.FaceChange("bemused",1)
            else:
                    $ Girl.FaceChange("bemused",1)
                    $ Girl.Statup("Love", 50, -1)
                    $ Girl.Statup("Love", 70, -1)
                    $ Girl.Statup("Obed", 50, 2)
                    if Girl is RogueX:
                            ch_r "Знаешь, прозвучало как-то не очень. . ."
                    elif Girl is KittyX:
                            ch_k "Эм, ладно. . ."
                    elif Girl is EmmaX:
                            ch_e "То есть, -только- сегодня? . ."
                    elif Girl is JeanX:
                            $ Girl.FaceChange("confused",1)
                            $ Girl.Statup("Inbt", 90, 2)
                            ch_j "Значит ты не думаешь, что я -всегда- красивая?"
                    elif Girl is StormX:
                            ch_s "Я не думаю, что моя внешность должна тебя беспокоить."
                    elif Girl is JubesX:
                            ch_v "Нууу, не пялься ты так пристально."
                    elif Girl is GwenX:
                            ch_g "Эм. . . спасибо?"
                    elif Girl is BetsyX:
                            ch_b "О, меня оценили."
                    elif Girl is DoreenX:
                            $ Girl.FaceChange("confused",1)
                            ch_d "Конечно. . . как скажешь. . ."
                    elif Girl is WandaX:
                            ch_w "Хмм. . . спасибо. . ."
            #"You're looking extra beautiful today",         #2
    elif Line == 3:
            #"Hey there, gorgeous",                          #3
            if not ApprovalCheck(Girl, 900):
                    $ D20 -= 10
            if Girl in (KittyX, EmmaX, JeanX, JubesX):
                    $ D20 += 5

            if Girl is LauraX:
                    $ Girl.FaceChange("confused",1)
                    $ Girl.Statup("Love", 70, 2, 1)
                    $ Girl.Statup("Inbt", 50, 1)
                    ch_l "Эм. . . привет?"
            elif D20 >= 10:
                    $ Girl.FaceChange("smile",2)
                    $ Girl.Statup("Love", 60, 2)
                    if D20 >= 15:
                            $ Girl.Statup("Love", 200, 1)
                            $ Girl.Statup("Obed", 60, 1)
                            $ Girl.Statup("Inbt", 80, 1)
                    if Girl is RogueX:
                            ch_r "И тебе \"привет\"."
                    elif Girl is KittyX:
                            ch_k "Ох. . . хихи, это так мило. . ."
                    elif Girl is EmmaX:
                            ch_e "Да. . . и тебе привет."
                    elif Girl is JeanX:
                            $ Girl.Statup("Obed", 60, 3)
                            ch_j "Ох, привет."
                    elif Girl is StormX:
                            ch_s "И тебе \"привет, красавчик\"."
                    elif Girl is JubesX:
                            ch_v "Это так мило. . ."
                    elif Girl is GwenX:
                            ch_g "И тебе!"
                    elif Girl is BetsyX:
                            ch_b "Хаха."
                    elif Girl is DoreenX:
                            $ Girl.FaceChange("confused",1)
                            ch_d "Привет. . . что?"
                    elif Girl is WandaX:
                            ch_w "Хмм. . . спасибо. . ."
                    $ Girl.FaceChange("smile",1)
            else:
                    $ Girl.FaceChange("bemused",1)
                    $ Girl.Statup("Love", 60, -1)
                    $ Girl.Statup("Obed", 60, 2)
                    $ Girl.Statup("Inbt", 50, 1)
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Ты сама \"красотка\"."
                            else:
                                ch_r "Ты сам \"красавчик\"."
                    elif Girl is KittyX:
                            ch_k "Вееерно. . ."
                    elif Girl is EmmaX:
                            ch_e "Ох уж эта молодежь. . ."
                    elif Girl is JeanX:
                            $ Girl.Statup("Love", 80, 1)
                            ch_j "Как скажешь."
                    elif Girl is StormX:
                            ch_s "Ох, здравствуй."
                    elif Girl is JubesX:
                            ch_v "Привет."
                    elif Girl is GwenX:
                            ch_g "Угум. . ."
                    elif Girl is BetsyX:
                            ch_b "Да, конечно."
                    elif Girl is DoreenX:
                            $ Girl.FaceChange("confused",1)
                            ch_d "Конечно. . . как скажешь. . ."
                    elif Girl is WandaX:
                            ch_w "Хмм. . . спасибо. . ."
            #"Hey there, gorgeous",                          #3
    elif Line == 4:
            #"I'm sorry, I got lost in your eyes",           #4
            if ApprovalCheck(Girl, 900, "L") and Girl is not EmmaX:
                    pass
            elif not ApprovalCheck(Girl, 1000):
                    $ D20 -= 10
            if Girl in (RogueX,KittyX,BetsyX,DoreenX,WandaX):
                    $ D20 += 10

            if Girl is LauraX:
                            $ Girl.FaceChange("confused")
                            ch_l "Что?"
            elif D20 >= 10:
                    $ Girl.FaceChange("bemused",2)
                    $ Girl.Statup("Love", 90, 2)
                    $ Girl.Statup("Obed", 50, 2)
                    $ Girl.Statup("Inbt", 30, 1)
                    if Girl is RogueX:
                            ch_r "Ты прелесть."
                    elif Girl is KittyX:
                            $ Girl.FaceChange("bemused",2,Mouth="smile")
                            $ Girl.Statup("Love", 200, 1)
                            $ Girl.Statup("Lust", 50, 2)
                            ch_k "Хихи. . . и не говори. . ."
                    elif Girl is EmmaX:
                            $ Girl.FaceChange("bemused",1)
                            ch_e "Хорошая попытка. . ."
                    elif Girl is JeanX:
                            ch_j "Ну. . . ладно."
                    elif Girl is StormX:
                            ch_s "Я к этому привыкла."
                    elif Girl is JubesX:
                            ch_v "Такое я оказываю влияние на людей."
                    elif Girl is GwenX:
                        if GwenX.Hat:
                            $ Girl.FaceChange("confused")
                            $ Girl.Statup("Love", 70, -1)
                            ch_g "Ха, ты серьезно?"
                        else:
                            ch_g "Ха, так банально!"
                    elif Girl is BetsyX:
                            ch_b "Боже. . ."
                    elif Girl is DoreenX:
                            ch_d "Это очень мило. . ."
                    elif Girl is WandaX:
                            ch_w "А я-то думала, что это -Я- тут колдунья. . ."
                    $ Girl.FaceChange("bemused",1)
            else:
                    $ Girl.FaceChange("angry",1,Eyes="up")
                    $ Girl.Statup("Love", 60, 1)
                    $ Girl.Statup("Obed", 50, 1)
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Может, тебе и стоит оставаться потерянной."
                            else:
                                ch_r "Может, тебе и стоит оставаться потерянным."
                    elif Girl is KittyX:
                            ch_k "Угум. . ."
                    elif Girl is EmmaX:
                            ch_e "Полагаю, ты преувеличиваешь. . ."
                    elif Girl is JeanX:
                            $ Girl.FaceChange("bemused",1,Eyes="up")
                            $ Girl.Statup("Love", 60, 1)
                            $ Girl.Statup("Obed", 80, 1)
                            $ Girl.Statup("Inbt", 80, 1)
                            if not Player.Male:
                                ch_j "Не будь таким простым."
                            else:
                                ch_j "Не будь такой простой."
                    elif Girl is StormX:
                            $ Girl.Eyes = "white"
                            ch_s "Тебе уже лучше?"
                    elif Girl is JubesX:
                            ch_v "Извини, иногда я оказываю такое влияние на людей. . ."
                    elif Girl is GwenX:
                        if GwenX.Hat:
                            $ Girl.FaceChange("confused")
                            $ Girl.Statup("Love", 70, -2)
                            ch_g ". . . Как?"
                        else:
                            ch_g "Уфф."
                    elif Girl is BetsyX:
                            ch_b "Конечно. . ."
                    elif Girl is DoreenX:
                            ch_d "Ох. . . ладно?"
                    elif Girl is WandaX:
                            ch_w "Ох, блин. . ."
                    $ Girl.FaceChange("normal")
            #"I'm sorry, I got lost in your eyes",           #4
    elif Line == 5:
            #"You're looking really toned lately",           #5
            if not ApprovalCheck(Girl, 600):
                    $ D20 -= 12
            elif not ApprovalCheck(Girl, 1200) or Girl is DoreenX:
                    $ D20 -= 8

            if Girl in (LauraX,StormX):
                    $ D20 += 8

            if Girl is LauraX:
                            $ Girl.FaceChange("bemused")
                            $ Girl.Statup("Love", 80, 2)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Inbt", 50, 2)
                            ch_l "Спасибо? Я попробовала кое-что новое."
            elif D20 >= 10:
                    $ Girl.FaceChange("bemused",1)
                    $ Girl.Statup("Love", 60, 2)
                    $ Girl.Statup("Obed", 60, 2)
                    $ Girl.Statup("Inbt", 60, 2)
                    if Girl is RogueX:
                            ch_r "Ну. . . очень мило с твоей стороны. . ."
                    elif Girl is KittyX:
                            ch_k "Ох. . . ладно, эм, спасибо?"
                    elif Girl is EmmaX:
                            ch_e "Хмм, может я немного похудела."
                    elif Girl is JeanX:
                            if not Player.Male:
                                ch_j "Думаю, ты хотела сказать \"всегда.\""
                            else:
                                ch_j "Думаю, ты хотел сказать \"всегда.\""
                    elif Girl is StormX:
                            ch_s "Я попробовала кое-что новое."
                    elif Girl is JubesX:
                            ch_v "Я тренировалась. . ."
                    elif Girl is GwenX:
                            ch_g "Нужно держать себя в форме, иначе для тебя не выделят ни одной страницы."
                    elif Girl is BetsyX:
                            if not Player.Male:
                                ch_b "Ты и сама в хорошей форме."
                            else:
                                ch_b "Ты и сам в хорошей форме."
                    elif Girl is DoreenX:
                            ch_d "Спасибо, я стараюсь. . ."
                    elif Girl is WandaX:
                            ch_w "Ох, спасибо. . ."
            else:
                    $ Girl.FaceChange("angry",2)
                    $ Girl.Statup("Love", 50, -1)
                    $ Girl.Statup("Love", 70, -1)
                    $ Girl.Statup("Obed", 50, 2)
                    $ Girl.Statup("Inbt", 50, 1)
                    if Girl is RogueX:
                            ch_r "Тебе не стоит обращать внимание на мою \"подтянутость.\""
                    elif Girl is KittyX:
                            ch_k "Это сарказм?"
                    elif Girl is EmmaX:
                            ch_e "Думаю, нам не стоит обсуждать мое тело."
                    elif Girl is JeanX:
                            if not Player.Male:
                                ch_j "Ты явно хотела сказать, что я -всегда- подтянута."
                            else:
                                ch_j "Ты явно хотел сказать, что я -всегда- подтянута."
                            $ Girl.Statup("Love", 80, 2)
                            $ Girl.Statup("Obed", 60, 2)
                            $ Girl.Statup("Inbt", 90, 2)
                            $ Girl.FaceChange("bemused",1)
                            ch_j "Но, по крайней мере, ты обращаешь внимание."
                    elif Girl is StormX:
                            ch_s "Ты уделяешь слишком много внимания моему телу."
                    elif Girl is JubesX:
                            ch_v "Ладно, чудила. . ."
                    elif Girl is GwenX:
                            ch_g "Эм. . . ладно. . ."
                    elif Girl is BetsyX:
                            ch_b "Каждый делает то, что должен."
                    elif Girl is DoreenX:
                            ch_d "Понимаешь, я -стараюсь-!"
                    elif Girl is WandaX:
                            ch_w "Это был сарказм?"
                    $ Girl.Blush -= 1
                    $ Girl.Mouth = "normal"
            #"You're looking really toned lately",           #5
    elif Line == 6:
            #"You have some really nice tits",               #6
            if ApprovalCheck(Girl, 700, "I"):
                    pass
            elif not ApprovalCheck(Girl, 900):
                    $ D20 -= 15
            elif not ApprovalCheck(Girl, 1400):
                    $ D20 -= 10

            if Girl in (KittyX, EmmaX, WandaX):
                    $ D20 += 5
            else:
                if D20 >= 10:
                    $ Girl.FaceChange("bemused",2) #for Rogue and Laura's
                else:
                    $ Girl.FaceChange("angry",2) #for Rogue and Laura's
            if D20 >= 10:
                    $ Girl.Statup("Love", 90, 2)
                    $ Girl.Statup("Love", 200, 1)
                    $ Girl.Statup("Obed", 80, 4)
                    $ Girl.Statup("Inbt", 80, 3)
                    $ Girl.Statup("Inbt", 200, 1)
                    $ Girl.Statup("Lust", 50, 3)
                    if Girl is KittyX:
                            $ Girl.FaceChange("bemused",2,Mouth="smile")
                            ch_k "Серьезно? Спасибо. . ."
                    elif Girl is EmmaX:
                            $ Girl.FaceChange("bemused",1,Mouth="smile")
                            ch_e "Чудесные, правда?"
                    elif Girl is JeanX:
                            $ Girl.FaceChange("bemused",1,Eyes="down")
                            ch_j ". . ."
                            $ Girl.Eyes = "squint"
                            if not Player.Male:
                                ch_j "Ага. . . какая ты наблюдательная."
                            else:
                                ch_j "Ага. . . какой ты наблюдательный."
                    elif Girl is StormX:
                            ch_s ". . . да, пожалуй, что так. . ."
                    elif Girl is GwenX:
                            ch_g "Я рада, что они тебе нравятся. . ."
                    elif Girl is BetsyX:
                            if not Player.Male:
                                ch_b "Пожалуй, ты права. . ."
                            else:
                                ch_b "Пожалуй, ты прав. . ."
                    elif Girl is DoreenX:
                            $ Girl.FaceChange("confused",2)
                            ch_d "Ох. . . эм, наверное. . ."
                    elif Girl is WandaX:
                            ch_w "Я. . . спасибо? . ."
            else:
                    $ Girl.Statup("Love", 70, -1)
                    $ Girl.Statup("Obed", 60, 3)
                    $ Girl.Statup("Obed", 80, 2)
                    $ Girl.Statup("Inbt", 80, 3)
                    if Girl is KittyX:
                        if D20 <= 5:
                            $ Girl.FaceChange("angry",2)
                            $ Girl.Statup("Love", 60, -3)
                            $ Girl.Statup("Love", 90, -1)
                            if not Player.Male:
                                ch_k "Дура!"
                            else:
                                ch_k "Козел!"
                        else:
                            $ Girl.FaceChange("sadside",2,Mouth="smile")
                            ch_k "Я понимаю, к чему ты клонишь, но. . ."
                        $ Girl.FaceChange(5,1)
                    elif Girl is EmmaX:
                            $ Girl.FaceChange("bemused",1)
                            ch_e "Может прекратишь на них пялиться?"
                            if D20 >= 5:
                                    $ Girl.FaceChange("angry",1)
                                    ch_e ". . ."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 90, 2)
                                    $ Girl.Statup("Lust", 70, 5)
                                    ch_e "Мои глаза выше!"
                    elif Girl is JeanX:
                            $ Girl.FaceChange("bemused",1,Eyes="down")
                            $ Girl.Statup("Love", 90, 2)
                            if not Player.Male:
                                ch_j "Думаю, мне стоило бы обидеться, но ты права."
                            else:
                                ch_j "Думаю, мне стоило бы обидеться, но ты прав."
                    elif Girl is StormX:
                            ch_s "[Girl.Petname]! Пожалуйста, обуздай свою похоть."
                    elif Girl is GwenX:
                            ch_g ". . . Уверена, так не делают комплименты девушкам. . ."
                    elif Girl is BetsyX:
                            ch_b "Какой ужас."
                    elif Girl is DoreenX:
                            ch_d "Твой комментарий. . . не к месту. . ."
                    elif Girl is WandaX:
                            ch_w "Это перебор. . ."
            if Girl is RogueX:
                    ch_r "Я ценю твои попытки."
            elif Girl is LauraX:
                    ch_l "Наверное?"
            elif Girl is JubesX:
                    ch_v "Нууу. . . ладно?"
            if Girl is not KittyX:
                    $ Girl.FaceChange("bemused",1)
            #"You have some really nice tits",               #6
    elif Line == 7:
            #"Your ass looks really great",                  #7
            if ApprovalCheck(Girl, 700, "I"):
                    pass
            elif not ApprovalCheck(Girl, 900):
                    $ D20 -= 15
            elif not ApprovalCheck(Girl, 1300):
                    $ D20 -= 10

            if Girl in (RogueX,EmmaX,StormX,BetsyX,DoreenX):
                    $ D20 += 5

            if D20 >= 10:
                    $ Girl.FaceChange("bemused",2)
                    $ Girl.Statup("Love", 80, 2)
                    $ Girl.Statup("Love", 90, 1)
                    $ Girl.Statup("Obed", 60, 1)
                    $ Girl.Statup("Inbt", 60, 1)
                    $ Girl.Statup("Lust", 30, 2)
                    if Girl is RogueX:
                            ch_r "Не знаю, кажется, мои джинсы стали слегка тесноваты. . ."
                    elif Girl is KittyX:
                            ch_k "Наверное? То есть. . ."
                    elif Girl is EmmaX:
                            ch_e "Боже, у тебя очень хороший вкус. . ."
                            $ Girl.FaceChange("confused",1)
                            ch_e "И, пожалуй, плохие манеры. . ."
                    elif Girl is LauraX:
                            $ Girl.FaceChange("smile",1)
                            ch_l "Рада это слышать."
                    elif Girl is JeanX:
                            ch_j "Хочешь, я ей немного потрясу?"
                    elif Girl is StormX:
                            ch_s "Ты так думаешь? Забавно."
                    elif Girl is JubesX:
                            ch_v "Правда?"
                    elif Girl is GwenX:
                            ch_g "Ну, я не зря ношу этот костюм. . ."
                    elif Girl is BetsyX:
                            ch_b "Я упорно тренируюсь."
                    elif Girl is DoreenX:
                            ch_d "Наверное. . ."
                    elif Girl is WandaX:
                            ch_w "Хмм. . . спасибо. . ."
                    $ Girl.FaceChange("bemused",1)
            else:
                    $ Girl.FaceChange("angry",1)
                    $ Girl.Statup("Love", 60, -1)
                    $ Girl.Statup("Love", 70, -2)
                    $ Girl.Statup("Obed", 60, 3)
                    $ Girl.Statup("Inbt", 50, 2)
                    if Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Ты не должна комментировать фигуру девушки."
                            else:
                                ch_e "Ты не должен комментировать фигуру девушки."
                    elif Girl is LauraX:
                            $ Girl.FaceChange("confused",1)
                            ch_l "Верно. . ."
                    elif Girl is JeanX:
                            $ Girl.Statup("Love", 60, 3)
                            ch_j "Это и так понятно."
                    elif Girl is StormX:
                            ch_s "[Girl.Petname], пожалуйста, будь серьёзней."
                    elif Girl is GwenX:
                            ch_g "Мне не нужно этого слышать."
                    elif Girl is BetsyX:
                            ch_b "Веди себя прилично."
                    else:
                            call AnyLine(Girl,"Как грубо.")
                    $ Girl.FaceChange("normal",1)

            if Girl is JubesX and Girl.Acc:
                    ch_v "Откуда ты знаешь?"
            #"Your ass looks really great",                  #7
    elif Line == 8:
            #"Oh, what's that fragrance? It suits you",      #8
            if ApprovalCheck(Girl, 800, "L"):
                    pass
            elif not ApprovalCheck(Girl, 1300):
                    $ D20 -= 10
            if Girl in (EmmaX,LauraX,StormX,BetsyX):
                    $ D20 += 15

            if D20 >= 10:
                    $ Girl.FaceChange("bemused",1,Mouth="smile")
                    $ Girl.Statup("Love", 90, 2)
                    $ Girl.Statup("Love", 200, 1)
                    $ Girl.Statup("Obed", 60, 2)
                    $ Girl.Statup("Inbt", 80, 3)
                    $ Girl.Statup("Lust", 50, 2)
                    if Girl is RogueX:
                            ch_r "А? Спасибо. . . наверное?"
                    elif Girl is KittyX:
                            ch_k "А? . . Не знаю, наверное, это мой повседневный шампунь. . ."
                    elif Girl is EmmaX:
                            ch_e "Благодарю, я достала его во время прошлой поездки в Грасе."
                    elif Girl is LauraX:
                            ch_l "Возможно, это запах крови."
                    elif Girl is JeanX:
                            $ Line = renpy.random.choice([RogueX.Name_rod,KittyX.Name_rod,EmmaX.Name_rod])
                            ch_j "А, это всего-лишь духи [Line]."
                            $ Line = 8
                    elif Girl is StormX:
                            ch_s "Ах, это все цветок в форме сердца, который я обнаружила во время своих путешествий. . ."
                    elif Girl is JubesX:
                            ch_v "Ох, это, наверное, лосьон для загар. . ."
                    elif Girl is GwenX:
                            ch_g "Эм. . . это, наверное, зефирки?"
                    elif Girl is BetsyX:
                            ch_b "Это аромат сирени."
                    elif Girl is DoreenX:
                            $ Girl.FaceChange("confused",1)
                            ch_d "От меня пахнет в основном. . . шерстью. . ."
                    elif Girl is WandaX:
                            ch_w "Я недавно сварила зелье по одному интересному рецепту. . ."
            else:
                    $ Girl.FaceChange("angry",2,Mouth="grimace")
                    $ Girl.Statup("Love", 60, -1)
                    $ Girl.Statup("Obed", 60, 2)
                    $ Girl.Statup("Inbt", 50, 1)
                    if Girl is RogueX:
                            ch_r "Пожалуй, лучше не говорить о запахе женщины."
                    elif Girl is KittyX:
                            ch_k "Как грубо. . ."
                    elif Girl is EmmaX:
                            ch_e "Полагаю, тогда тебе стоит немного отойти. . ."
                    elif Girl is LauraX:
                            $ Girl.FaceChange("confused",1)
                            $ Girl.Statup("Lust", 50, 2)
                            ch_l "Не знаю, наверное, я немного вспотела. . ."
                    elif Girl is JeanX:
                            $ Girl.Statup("Love", 60, 1)
                            $ Girl.Statup("Love", 80, 1)
                            $ Girl.Statup("Obed", 60, 2)
                            $ Girl.FaceChange("bemused",1)
                            ch_j "Не знаю, я просто нашла какой-то флакончик и побрызгалась. . ."
                    elif Girl is StormX:
                            ch_s ". . . возможно, ты стоишь слишком близко. . ."
                    elif Girl is JubesX:
                            ch_v "А не пойти ли тебе \"на хер.\""
                    elif Girl is GwenX:
                            ch_g "Это звучит -очень- жутко."
                            if not Player.Male:
                                ch_g "Просто чтобы ты знал."
                            else:
                                ch_g "Просто чтобы ты знала."
                    elif Girl is BetsyX:
                            ch_b "Мне кажется, тебе не стоит комментировать запах женщин. . ."
                    elif Girl is DoreenX:
                            ch_d "Давай не будем это обсуждать. . ."
                    elif Girl is WandaX:
                            ch_w "Ох, эм, наверное, это все из-за свеч и прочего. . ."
                    $ Girl.FaceChange("bemused",1)
            #"Oh, what's that fragrance? It suits you",      #8
    elif Line == 9:
            #"I'm so into you"                               #9
            if ApprovalCheck(Girl, 900, "L"):
                    pass
            elif not ApprovalCheck(Girl, 1100):
                    $ D20 -= 10
            if Girl in (RogueX, LauraX, JeanX):
                    $ D20 += 5

            if D20 >= 10:
                    $ Girl.FaceChange("sly",1)
                    $ Girl.Statup("Love", 80, 1)
                    $ Girl.Statup("Love", 90, 1)
                    $ Girl.Statup("Obed", 70, 2)
                    $ Girl.Statup("Inbt", 80, 3)
                    $ Girl.Statup("Lust", 30, 5)
                    $ Girl.Statup("Lust", 60, 5)
                    if Girl is RogueX:
                            ch_r "Я рада. . ."
                    elif Girl is KittyX:
                            ch_k "А ты мне пока еще нет. . ."
                            ch_k "Но в будущем все может измениться. . ."
                    elif Girl is EmmaX:
                            ch_e "Хмм, да. . . заметно."
                    elif Girl is LauraX:
                            ch_l "А ты мне пока еще нет."
                    elif Girl is JeanX:
                            ch_j "Еще бы. . ."
                    elif Girl is StormX:
                            ch_s "Ох, как мило. . ."
                    elif Girl is JubesX:
                            ch_v "О, да. . ."
                    elif Girl is GwenX:
                            ch_g "Ну, это может быть выгодно. . ."
                    elif Girl is BetsyX:
                            ch_b "Думаю, это взаимно."
                    elif Girl is DoreenX:
                            ch_d "Ты. . . ты мне тоже. . ."
                            ch_d "Вроде бы. . ."
                    elif Girl is WandaX:
                            ch_w "Надеюсь, что это правда. . ."
            else:
                    $ Girl.Statup("Love", 60, -2)
                    $ Girl.Statup("Obed", 60, 1)
                    $ Girl.Statup("Inbt", 50, 1)
                    if Girl is EmmaX:
                            $ Girl.FaceChange("angry",1,Mouth="smirk")
                            ch_e "Это не совсем уместное замечание."
                    elif Girl is JeanX:
                            $ Girl.FaceChange("sly",1)
                            $ Girl.Statup("Love", 80, 3)
                            $ Girl.Statup("Obed", 60, 1)
                            ch_j "Держи себя в руках. . ."
                    elif Girl is DoreenX:
                            ch_d "Конечно. . . как скажешь. . ."
                    else:
                            $ Girl.FaceChange("bemused",1)
                            call AnyLine(Girl,"Ладно. . .")
            #"I'm so into you"                               #9

    if D20 < 10:
        menu:
            "Извини":
                    if Girl not in (LauraX,JeanX):
                            $ Girl.Statup("Love", 60, 1)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Obed", 40, -2)
                            $ Girl.Statup("Obed", 70, -1)
                            $ Girl.FaceChange("sadside")
                    if Girl is RogueX:
                            ch_r "Ну, спасибо. . ."
                    elif Girl is KittyX:
                            ch_k "Думаю, мне не стоит держать на тебя зла. . ."
                    elif Girl is EmmaX:
                            ch_e "Ладно, извинения приняты."
                    elif Girl is LauraX:
                            $ Girl.FaceChange("normal")
                            ch_l "Как скажешь."
                    elif Girl is JeanX:
                            $ Girl.FaceChange("angry",Eyes="side")
                            $ Girl.Statup("Love", 60, 1)
                            $ Girl.Statup("Obed", 70, -1)
                            ch_j ". . ."
                            if D20 < 7:
                                    $ Girl.FaceChange("bemused")
                                    $ Girl.Statup("Love", 60, 1)
                                    $ Girl.Statup("Obed", 50, 1)
                                    ch_j "Ладно, извинения приняты."
                            if D20 < 5:
                                    $ Girl.Statup("Love", 90, 1)
                                    $ Girl.Statup("Obed", 40, 2)
                                    ch_j "Главное не позволяй подобному повториться."
                    elif Girl is StormX:
                            ch_s "Не извиняйся, а старайся стать лучше."
                    elif Girl is JubesX:
                            $ Girl.Statup("Love", 70, 1)
                            ch_v "Ага, ладно. . ."
                    elif Girl is GwenX:
                            ch_g "Ничего страшного. Разговоры - это сложно."
                    elif Girl is BetsyX:
                            ch_b "Тебе стоит стараться стать лучше."
                    elif Girl is DoreenX:
                            ch_d "Ага. . . думаю, все нормально. . ."
                    elif Girl is WandaX:
                            ch_w "Ничего страшного не случилось. . ."
                    $ Girl.FaceChange("normal")
            ". . .":
                pass
    elif bg_current == "date":
            #if your compliment landed, you get a date bonus while on a date
            if "compliment" not in Girl.RecentActions:
                    $ Girl.AddWord(1,"compliment",0,0,0)
                    call Date_Bonus(Girl,5)
    return
# End Compliments / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Love You Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Love_You(Girl=0): #rkeljsvgbdw
        # Called whenever you say "I love you" in the flirt menu
        # Rejects attempts before the girl confesses

        ch_p "[Girl.Name], я люблю тебя."
        if bg_current == "HW Party":
                call AnyLine(Girl,". . . нам лучше поговорить после вечеринки. . .")
                return

        if "lover" not in Girl.Petnames:
            #if you didn't clear the love scene with her. . .
            if "love" in Girl.History:
                    #you've tried this before. . .
                    if ApprovalCheck(Girl, 800,"L"):
                            #she kind of likes you
                            $ Girl.Statup("Love", 90, 2)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.Statup("Lust", 30, 5)
                            $ Girl.FaceChange("bemused",2,Brows="confused")
                            if Girl is RogueX:
                                    ch_r "Не наседай на меня. . ."
                            elif Girl is KittyX:
                                    ch_k "Не могу ответить взаимностью. . ."
                            elif Girl is EmmaX:
                                    ch_e "Лучше не надо такого говорить. . ."
                            elif Girl is LauraX:
                                    ch_l "Я не хочу слышать подобное. . ."
                            elif Girl is JeanX:
                                    ch_j "Ну, я не знаю, что мне делать с этой информацией. . ."
                            elif Girl is StormX:
                                    ch_s "Не играй со мной. . ."
                            elif Girl is JubesX:
                                    ch_v "Я даже не знаю, что мне ответить. . ."
                            elif Girl is GwenX:
                                    ch_g "Ты, эм. . . меня пугаешь. . ."
                            elif Girl is BetsyX:
                                    ch_b "Пожалуйста, держи себя в руках."
                            elif Girl is DoreenX:
                                    ch_d "Эм. . . расслабься!"
                            elif Girl is WandaX:
                                    ch_w "Дай мне больше времени."

                    elif ApprovalCheck(Girl, 600,"L"):
                            #she is friendly enough. . .
                            $ Girl.Statup("Love", 95, 2)
                            $ Girl.Statup("Obed", 80, 3)
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.FaceChange("bemused",2)
                            if Girl is RogueX:
                                    ch_r "Даже не знаю, любишь? . ."
                            elif Girl is KittyX:
                                    ch_k "Не знаю, чувствую ли я тоже самое . ."
                            elif Girl is EmmaX:
                                    ch_e "Это крайне неуместно. . ."
                            elif Girl is LauraX:
                                    ch_l "А я тебя нет. . ."
                            elif Girl is JeanX:
                                    $ Girl.Statup("Love", 50, 1)
                                    ch_j "Хорошо, но. . ."
                            elif Girl is StormX:
                                    ch_s "Ты так говоришь, но. . ."
                            elif Girl is JubesX:
                                    ch_v "Ты слишком спешишь. . ."
                            elif Girl is GwenX:
                                    ch_g "Ты, эм, не слишком спешишь?"
                            elif Girl is BetsyX:
                                    ch_b "Я ценю твои слова, но не могу ответить взаимностью."
                            elif Girl is DoreenX:
                                    ch_d "Я. . . это очень мило, но. . . я - нет. . ."
                            elif Girl is WandaX:
                                    ch_w "Я пока не готова к этому разговору."
                    else:
                            #she doesn't like you. . .
                            $ Girl.Statup("Love", 95, -5)
                            $ Girl.Statup("Obed", 90, 5)
                            $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.FaceChange("angry",1)

                            if Girl is RogueX:
                                    ch_r "Бред."
                            elif Girl is KittyX:
                                    ch_k "Хватит меня троллить!"
                            elif Girl is EmmaX:
                                    ch_e "Ох, забудь уже про эту чепуху. . ."
                            elif Girl is LauraX:
                                    if not Player.Male:
                                        ch_l "ДА ПОШЛА ТЫ. . ."
                                    else:
                                        ch_l "ДА ПОШЕЛ ТЫ. . ."
                            elif Girl is JeanX:
                                    $ Girl.Statup("Love", 60, 2)
                                    if Player.Male:
                                            ch_j "Ох, держи его в штанах. . ."
                                    else:
                                            ch_j "Ох, успокой свои сисечки. . ."
                            elif Girl is StormX:
                                    ch_s "Ох, ты ведешь себя как ребенок. . ."
                            elif Girl is JubesX:
                                    ch_v "Боже, успокойся. . ."
                            elif Girl is GwenX:
                                    ch_g "Ох, да ладно тебе."
                            elif Girl is BetsyX:
                                    ch_b "Я не согласна."
                            elif Girl is DoreenX:
                                    ch_d "Я просто. . . извини. . ."
                            elif Girl is WandaX:
                                    ch_w "Что? Нет."

            #if this is the first time you've tried this but you haven't agreed to love her yet. . .
            $ Girl.AddWord(1,"love","love",0,"love") #adds the "love" trait to recent and daily actions, and history


            if not Girl.Event[6]:
                    # if you've never had the "love" talk. . .
                    $ Line = "never"
            elif Girl.Event[6] >= 20:
                    # if she's asked you, but you refused before. . .
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Ты уже однажды причинила мне боль [RogueX.Petname]."
                            else:
                                ch_r "Ты уже однажды причинил мне боль [RogueX.Petname]."
#                            call Rogue_Love_Redux #she doesn't have one of these, skip it.
                    elif Girl is JeanX:
                            $ Girl.Statup("Love", 90, 10)
                            $ Girl.Statup("Love", 200, 40)
                            ch_j "Приятно слышать, что ты это признаешь."
                    else:
                            call expression Girl.Tag+"_Love_Redux"

            if Line == "never":
                    # if you've never had the "love" talk. . .
                    if ApprovalCheck(Girl, 800,"L"):
                            $ Girl.Statup("Love", 90, 10)
                            $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("smile",2,Eyes="surprised")
                    elif ApprovalCheck(Girl, 600,"L"):
                            $ Girl.Statup("Love", 90, 5)
                            $ Girl.FaceChange("confused",2,Eyes="surprised")
                    else:
                            $ Girl.FaceChange("angry",1,Brows="confused")
                            $ Girl.Statup("Love", 90, -5)
                            $ Girl.Statup("Obed", 90, 5)
                    $ Girl.Statup("Obed", 70, 5)
                    $ Girl.Statup("Inbt", 60, 5)
                    if Girl is RogueX:
                            ch_r "Чтооо? . ."
                            ch_r "Это что? Шутка какая-то?"
                    elif Girl is KittyX:
                            ch_k "Что это было? . ."
                            ch_k ". . . Эм, мне пора идти!"
                    elif Girl is EmmaX:
                            ch_e "Что? Я. . . Я не знаю, что и ответить."
                            ch_e "Я. . . я свяжусь с тобой позже."
                    elif Girl is LauraX:
                            ch_l "А? Ты-"
                            ch_l "Эм. . ."
                            ch_l "Пока."
                    elif Girl is JeanX:
                            ch_j "Хмм, пища для размышлений. . ."
                    elif Girl is StormX:
                            ch_s "Позволь мне обдумать это. . ."
                    elif Girl is JubesX:
                            ch_v "Я. . . не сейчас. . ."
                    elif Girl is GwenX:
                            ch_g ". . . все происходит слишком быстро. . ."
                    elif Girl is BetsyX:
                            ch_b "Боюсь, что я об этом даже не думала. . ."
                    elif Girl is DoreenX:
                            ch_d "Что? . . Я не. . . Я не могу сейчас даже думать об этом. . ."
                    elif Girl is WandaX:
                            ch_w "Я. . . Я пока не готова к подобному разговору."

                    "[Girl.Name] уходит."
                    call Remove_Girl(Girl)
                    jump Misplaced
            return
        # End if you never cleared the love scene stuff

        if "love" in Girl.DailyActions:
                #if you've said it today
                $ Girl.Statup("Love", 95, 5)
                $ Girl.Statup("Obed", 70, 2)
                $ Girl.Statup("Inbt", 60, 1)
                $ Girl.Statup("Lust", 50, 5)
                $ Girl.FaceChange("smile",1)
                if Girl is RogueX:
                        if not Player.Male:
                            ch_r "По-моему, ты уже говорила мне об этом. . ."
                        else:
                            ch_r "По-моему, ты уже говорил мне об этом. . ."
                        ch_r "Но скажи еще раз, ради меня, [RogueX.Petname]."
                elif Girl is KittyX:
                        if not Player.Male:
                            ch_k "Разве ты уже этого не говорила? . ."
                        else:
                            ch_k "Разве ты уже этого не говорил? . ."
                        ch_k ". . . но скажи-ка еще раз."
                elif Girl is EmmaX:
                        if not Player.Male:
                            ch_e "Так ты уже это говорила мне. . ."
                            ch_e "но я готова слушать эти слова вечно, [EmmaX.Petname]."
                        else:
                            ch_e "Так ты уже это говорил мне. . ."
                            ch_e "но я готова слушать эти слова вечно, [EmmaX.Petname]."
                elif Girl is LauraX:
                        ch_l "Да, я знаю. . ."
                        ch_l "но можешь продолжать повторять, [LauraX.Petname]."
                elif Girl is JeanX:
                        $ Girl.Statup("Love", 80, -2)
                        $ Girl.Statup("Obed", 70, -2)
                        ch_j "Ты начинаешь повторяться. . ."
                elif Girl is StormX:
                        ch_s "Это уже не первый раз за сегодня. . ."
                        ch_s "Но я не буду тебя останавливать. . ."
                elif Girl is JubesX:
                        ch_v "Серьезно, дай мне время подумать. . ."
                elif Girl is GwenX:
                        if not Player.Male:
                            ch_g "Ты должна дать мне немного времени. . ."
                        else:
                            ch_g "Ты должен дать мне немного времени. . ."
                elif Girl is BetsyX:
                        ch_b "Мне не больно слышать эти слова снова."
                elif Girl is DoreenX:
                        ch_d "Оу, я тоже тебя люблю."
                elif Girl is WandaX:
                        ch_w "Ага, я тоже тебя люблю."

        elif ApprovalCheck(Girl, 800,"L"):
                #if she still loves you
                $ Girl.Statup("Love", 90, 5)
                $ Girl.Statup("Love", 200, 5)
                $ Girl.Statup("Obed", 70, 1)
                $ Girl.Statup("Inbt", 60, 1)
                $ Girl.Statup("Lust", 30, 5)
                $ Girl.FaceChange("smile",1)
                if Girl is RogueX:
                        ch_r "Я тоже люблю тебя, [RogueX.Petname]."
                elif Girl is KittyX:
                        ch_k "Оуууу! Я тоже люблю тебя, [KittyX.Petname]."
                elif Girl is EmmaX:
                        ch_e "И я тоже люблю тебя, [EmmaX.Petname]."
                elif Girl is LauraX:
                        ch_l "Ага, я тоже люблю тебя."
                elif Girl is JeanX:
                        ch_j ". . ."
                        $ Girl.Statup("Obed", 90, 2)
                        $ Girl.Statup("Inbt", 80, 1)
                        ch_j "Я тоже люблю тебя, так нормально?"
                elif Girl is StormX:
                        ch_s "И я тоже тебя люблю. . ."
                elif Girl is JubesX:
                        ch_v "Оу, я тоже люблю тебя!"
                elif Girl is GwenX:
                        ch_g "Оу, я тоже люблю тебя. . ."
                elif Girl is BetsyX:
                        ch_b "И я тебя, [Girl.Petname]."
                elif Girl is DoreenX:
                        ch_d "Оу, я тоже тебя люблю, [Girl.Petname]."
                elif Girl is WandaX:
                        ch_w "Ага, я тоже тебя люблю."
        else:
                #if she doesn't love you anymore
                $ Girl.Statup("Love", 90, 5)
                $ Girl.Statup("Love", 50, -10, 1)
                $ Girl.Statup("Obed", 70, 3)
                $ Girl.FaceChange("sadside",1)
                if Girl is RogueX:
                        ch_r "Уже слишком поздно."
                elif Girl is KittyX:
                        if not Player.Male:
                            ch_k "Как будто это правда. Ну ты и дура."
                        else:
                            ch_k "Как будто это правда. Придурок."
                elif Girl is EmmaX:
                        ch_e "Хотела бы я в это верить."
                elif Girl is LauraX:
                        if not Player.Male:
                            ch_l "Ты уже все испортила."
                        else:
                            ch_l "Ты уже все испортил."
                elif Girl is JeanX:
                        ch_j "Ага. . . чушь. . ."
                elif Girl is StormX:
                        ch_s "Если бы только это было правдой. . ."
                elif Girl is JubesX:
                        ch_v "Слова ничего не стоят. . ."
                elif Girl is GwenX:
                        ch_g "Поздно, слишком поздно. . ."
                elif Girl is BetsyX:
                        ch_b "И я тебя, [Girl.Petname], к большому сожалению. . ."
                elif Girl is DoreenX:
                        ch_d "Не усложняй все. . ."
                elif Girl is WandaX:
                        ch_w "Да-да, я знаю."

        $ Girl.AddWord(1,"love","love",0,"love") #adds the "love" trait to recent and daily actions, and history
        return


# End Love You Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Touch Cheek / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label TouchCheek(Girl=0): #rkeljsvgbdw
        if Girl not in TotalGirls:
                return
        call Shift_Focus(Girl)
        $ Girl.FaceChange("surprised", 1)
        if "no cheek" in Girl.DailyActions:
                "Вы протягиваете руку, чтобы погладить рукой лицо [Girl.Name_rod], но она отмахивается."
                $ Girl.FaceChange("angry")
                if Girl is RogueX:
                        ch_r "Отвали."
                elif Girl is EmmaX:
                        ch_e "Что ты делаешь, [Girl.Petname]?"
                elif Girl is JeanX:
                        $ Girl.Eyes = "psychic"
                        ch_j "Я сказала тебе, держись подальше."
                        $ Girl.Eyes = "squint"
                elif Girl is StormX:
                        ch_s "Не надо."
                elif Girl is BetsyX:
                        ch_b "Веди себя прилично!"
                elif Girl is DoreenX:
                        ch_d "Это очень жутко."
                else:
                        call AnyLine(Girl,"Убери свои грязные руки.")
                $ Girl.Statup("Love", 50, -2)
                return
        else:
                "Вы протягиваете руку и начинаете гладить рукой лицо [Girl.Name_rod], по ее телу пробегают мурашки."
        $ Girl.Statup("Obed", 50, 1)

        if Girl is RogueX or "addictive" in Player.Traits:
                $ Girl.Addict -= 2
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0
                $ Girl.Addictionrate = 3 if Girl.Addictionrate < 3 else Girl.Addictionrate
                $ Girl.Statup("Lust", 70, 5)
        else:
                $ Girl.Addict -= 2
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0
                $ Girl.Statup("Lust", 40, 5)

        if ApprovalCheck(Girl, 1000):
                $ Girl.FaceChange("sexy", 1)
                if Girl is RogueX:
                        ch_r "С намеком на продолжение, [Girl.Petname]?"
                elif Girl is EmmaX:
                        ch_e "Мило, для чего это все, [Girl.Petname]?"
                elif Girl is JeanX:
                        ch_j "Ох, эм. . ."
                else:
                        call AnyLine(Girl,"Хммм, о чем ты думаешь, " + Girl.Petname + "?")
                $ Girl.Statup("Love", 80, 1)
        elif ApprovalCheck(Girl, 800,Alt=[[RogueX],500]) or ApprovalCheck(Girl, 700,"L"):
                $ Girl.FaceChange("smile", 1)
                if Girl is RogueX:
                        ch_r "Это. . . приятно."
                elif Girl is EmmaX:
                        ch_e "Ммммм. . ."
                elif Girl is JeanX:
                        ch_j "Ох. . ."
                elif Girl is WandaX:
                        ch_w "Ну привет. . ."
                else:
                        call AnyLine(Girl,"Мило. . .")
        elif "cheek" in Girl.DailyActions:
                $ Girl.FaceChange("angry", 1)
                if Girl is RogueX:
                        ch_r "Эй, я же сказала, чтобы ты прекратил."
                elif Girl is EmmaX:
                        ch_e "[Girl.Petname], я не буду предупреждать тебя снова."
                elif Girl is StormX:
                        ch_s "Я предупреждала тебя держать дистанцию. . ."
                elif Girl is BetsyX:
                        ch_b "Мне кажется, я выразилась достаточно ясно. . ."
                else:
                        call AnyLine(Girl,"Эй, я же тебя предупреждала, "+Girl.Petname+".")
                $ Girl.Statup("Love", 50, -2)
                $ Girl.DailyActions.append("no cheek")
        elif ApprovalCheck(Girl, 250): #400
                $ Girl.Mouth = "smile"
                $ Girl.Brows = "normal"
                if Girl is RogueX:
                        ch_r "Эм. . . в следующий раз, может, сначала спросишь?"
                elif Girl is EmmaX:
                        ch_e "Хмм, думаю, нам стоит обсудить \"границы.\""
                elif Girl is JeanX:
                        ch_j "Эй! Не прикасайся ко мне."
                elif Girl is StormX:
                        ch_s "Держись подальше. . ."
                elif Girl is JubesX:
                        ch_v "Назад!"
                elif Girl is BetsyX:
                        ch_b "Как необычно. . ."
                else:
                        call AnyLine(Girl,"Эм, это было странно.")
        else:
                $ Girl.FaceChange("angry", 1)
                if Girl is RogueX:
                        ch_r "Не надо. . . не делай этого."
                elif Girl is EmmaX:
                        ch_e "[Girl.Petname], ты неподобающе себя ведешь."
                elif Girl is StormX:
                        ch_s "Я не думаю, что это уместно. . ."
                elif Girl is BetsyX:
                        ch_b "Пожалуйста, [Girl.Petname], веди себя прилично. . ."
                else:
                        call AnyLine(Girl,"Отвали, чудила.")
                $ Girl.Statup("Love", 50, -3)
                $ Girl.Statup("Obed", 50, 1)
                $ Girl.Statup("Inbt", 30, 1)

        if "no cheek" in Girl.DailyActions:
            menu:
                "Прости-прости, подобного больше не повторится.":
                        if ApprovalCheck(Girl, 300):
                                $ Girl.FaceChange("sexy", 1)
                                if Girl is RogueX:
                                        ch_r "Ну, ладно, только перестань."
                                elif Girl is EmmaX:
                                        ch_e "Проследи за этим."
                                elif Girl is StormX:
                                        if not Player.Male:
                                            ch_s "Ладно, надеюсь, ты и правда всё поняла. . ."
                                        else:
                                            ch_s "Ладно, надеюсь, ты и правда всё понял. . ."
                                else:
                                        call AnyLine(Girl,"Ладно. . .")
                                $ Girl.Statup("Love", 80, 2)
                        else:
                                $ Girl.FaceChange("angry", 1)
                                $ Girl.Eyes = "side"
                                if Girl is RogueX:
                                        ch_r "Похоже на правду. . ."
                                elif Girl is EmmaX:
                                        ch_e "В этом я уверена."
                                elif Girl is StormX:
                                        ch_s "Хорошо. . ."
                                elif Girl is BetsyX:
                                        ch_b "Принято. . ."
                                else:
                                        call AnyLine(Girl,"Угу-м.")
                                $ Girl.Statup("Obed", 20, 1)
                # end "Sorry, sorry, won't happen again.":

                "Мне показалось, ты и сама этого хочешь.":
                        if ApprovalCheck(Girl, 400, "OI",Alt=[[RogueX],300]) or ApprovalCheck(Girl, 800,Alt=[[RogueX,LauraX],1500]):
                                $ Girl.FaceChange("normal", 1)
                                $ Girl.Eyes = "squint"
                                if Girl is RogueX:
                                        ch_r "Ну. . . может быть. . ."
                                elif Girl is JeanX:
                                        ch_j "Что? Нет. . ."
                                elif Girl is JubesX:
                                        ch_v "Посмотрим, что из этого выйдет!"
                                elif Girl is GwenX:
                                        ch_g "Я так не думаю!"
                                elif Girl is DoreenX:
                                        ch_d "Эм. . . я так не думаю. . ."
                                elif Girl is WandaX:
                                        ch_w "Хех, чушь."
                                else:
                                        call AnyLine(Girl,"Всего лишь показалось.")
                                $ Girl.Statup("Love", 60, -1)
                                $ Girl.Statup("Obed", 30, 2)
                                $ Girl.Statup("Inbt", 40, 2)
                        else:
                                $ Girl.FaceChange("angry", 2)
                                $ Girl.Eyes = "squint"
                                if Girl is RogueX:
                                        ch_r "Чёрта с два."
                                elif Girl is EmmaX:
                                        ch_e "У тебя {i}хорошая{/i} фантазия."
                                elif Girl is StormX:
                                        ch_s "Это вряд ли. . ."
                                elif Girl is BetsyX:
                                        ch_b "Точно нет. . ."
                                elif Girl is WandaX:
                                        ch_w "Это нездоровое отношение ко мне."
                                else:
                                        call AnyLine(Girl,"Нет, только ты.")
                                $ Girl.Blush = 1
                                $ Girl.Statup("Love", 60, -3)
                                $ Girl.Statup("Obed", 30, 3)
                                $ Girl.Statup("Inbt", 40, 2)
                #end "You know you wanted it."
        else:
            menu:
                "Прости, ты просто выглядишь такой милой.":
                        if ApprovalCheck(Girl, 850, "LI"):
                                $ Girl.FaceChange("sexy", 1)
                                if Girl is RogueX:
                                        ch_r "Да, да."
                                elif Girl is KittyX:
                                        ch_k "Ага[KittyX.like]но перестань вести себя странно."
                                elif Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Могла бы придумать что-нибудь получше."
                                        else:
                                            ch_e "Мог бы придумать что-нибудь получше."
                                elif Girl is LauraX:
                                        ch_l "Ты должен придумать что-нибудь получше."
                                elif Girl is JeanX:
                                        ch_j "Конечно!"
                                        if not Player.Male:
                                            ch_j "Но ты должна была придумать что-то получше. . ."
                                        else:
                                            ch_j "Но ты должен был придумать что-то получше. . ."
                                elif Girl is StormX:
                                        ch_s "У тебя странное чувство юмора. . ."
                                elif Girl is JubesX:
                                        ch_v "Оу."
                                elif Girl is GwenX:
                                        ch_g ". . . серьезно?"
                                elif Girl is BetsyX:
                                        ch_b "Конечно. . ."
                                elif Girl is DoreenX:
                                        if not Player.Male:
                                            ch_d "Оу, ты такая очаровательная."
                                        else:
                                            ch_d "Оу, ты такой очаровательный."
                                elif Girl is WandaX:
                                        ch_w "М?"
                                $ Girl.Statup("Love", 80, 2)
                        elif ApprovalCheck(Girl, 500, "LI"):
                                $ Girl.FaceChange("smile", 1)
                                if Girl is RogueX:
                                        ch_r "Оу, это так неожиданно и приятно."
                                elif Girl is KittyX:
                                        ch_k "Не только я выгляжу мило, [LauraX.Petname]."
                                elif Girl is EmmaX:
                                        ch_e "Ты тоже выглядишь неплохо, [EmmaX.Petname]."
                                elif Girl is LauraX:
                                        ch_l "Эмм, да. . . ты, наверное, тоже?"
                                elif Girl is JeanX:
                                        ch_j "Конечно, это так!"
                                        ch_j "Это неизменно. . ."
                                elif Girl is StormX:
                                        ch_s "Хммм, ты неплохо умеешь льстить. . ."
                                elif Girl is JubesX:
                                        ch_v "Оу."
                                elif Girl is GwenX:
                                        ch_g "Оу. . ."
                                elif Girl is BetsyX:
                                        ch_b "Конечно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Оу. . ."
                                elif Girl is WandaX:
                                        ch_w "М?"
                                $ Girl.Statup("Love", 80, 2)
                        else:
                                $ Girl.FaceChange("angry", 1)
                                $ Girl.Eyes = "side"
                                if Girl is RogueX:
                                        ch_r "Не называй меня \"милой\", просто прекрати. . ."
                                elif Girl is KittyX:
                                        ch_k "Слишком мило для тебя."
                                elif Girl is EmmaX:
                                        ch_e "Это очевидно."
                                elif Girl is LauraX:
                                        ch_l "Я не \"милая.\""
                                elif Girl is JeanX:
                                        ch_j "Конечно, это так!"
                                        ch_j "Но это не значит, что ты просто так можешь трогать меня. . ."
                                elif Girl is StormX:
                                        ch_s "Ты, должно быть, шутишь. . ."
                                elif Girl is JubesX:
                                        ch_v "Пока. . ."
                                elif Girl is GwenX:
                                        ch_g ". . . это не оправдание. . ."
                                elif Girl is BetsyX:
                                        ch_b "Мне все равно, что ты думаешь. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох. . . ты правда так думаешь?"
                                elif Girl is WandaX:
                                        ch_w "Ладно?"
                                $ Girl.Statup("Obed", 20, 1)
                # end "Sorry, you looked so cute there."

                "На тебе сидела муха.":
                        if ApprovalCheck(Girl, 850, "LI"):
                                $ Girl.FaceChange("sexy", 1)
                                if Girl is RogueX:
                                        ch_r "Oх? И это вся твоя отмазка. . ?"
                                elif Girl is EmmaX:
                                        ch_e "Ох? Наверное, {i}так{/i} оно и было. . ."
                                elif Girl is JeanX:
                                        ch_j "Мухи понимают, что не стоит садиться на меня."
                                elif Girl is StormX:
                                        ch_s "Я в этом сомневаюсь. . ."
                                        "Ее начинают окружать потоки ветра."
                                elif Girl is JubesX:
                                        ch_v "Сомневаюсь."
                                elif Girl is GwenX:
                                        ch_g "Как странно. . ."
                                else:
                                        call AnyLine(Girl,"А? Извини. . .")
                                $ Girl.Statup("Love", 60, 1)
                                $ Girl.Statup("Inbt", 40, 1)
                        elif ApprovalCheck(Girl, 600):
                                $ Girl.FaceChange("normal")
                                call AnyLine(Girl,"Муха, ага. . .")
                        else:
                                $ Girl.FaceChange("angry", 1)
                                if Girl is RogueX:
                                        ch_r "Как правдоподобно, послушай, просто не трогай меня."
                                elif Girl is EmmaX:
                                        ch_e "Это не оправдание."
                                elif Girl is JeanX:
                                        ch_j "Мухи понимают, что не стоит садиться на меня."
                                elif Girl is StormX:
                                        ch_s "Они понимают, что им лучше держать дистанцию. . ."
                                        "Ее начинают окружать потоки ветра."
                                elif Girl is JubesX:
                                        ch_v "Такого больше не случается. . ."
                                elif Girl is GwenX:
                                        ch_g "Как странно. . ."
                                elif Girl is BetsyX:
                                        ch_b "Я в этом сомневаюсь. . ."
                                else:
                                        call AnyLine(Girl,"Лаааадно, вот только не нужно меня трогать.")
                                $ Girl.Statup("Obed", 50, 2)
                #end "fly on you"

                "Уверена, что тебе не понравилось?":
                        if ApprovalCheck(Girl, 650, "LI") or ApprovalCheck(Girl, 1000):
                                $ Girl.FaceChange("sexy", 1)
                                $ Girl.Eyes = "side"
                                if Girl is RogueX:
                                        ch_r "Наверное."
                                elif Girl is EmmaX:
                                        ch_e "Нужно попробовать еще раз, чтобы убедиться. . ."
                                elif Girl is JeanX:
                                        ch_j ". . ."
                                        ch_j "Наверное. . ."
                                elif Girl is StormX:
                                        ch_s "Возможно. . ."
                                elif Girl is JubesX:
                                        ch_v "Нуу, давай это выясним. . ."
                                elif Girl is GwenX:
                                        ch_g ". . . ну. . ."
                                elif Girl is BetsyX:
                                        if not Player.Male:
                                            ch_b "Возможно, если бы ты меня еще немного погладила. . ."
                                        else:
                                            ch_b "Возможно, если бы ты меня еще немного погладил. . ."
                                else:
                                        call AnyLine(Girl,"Возможно, если бы это было что-то большее. . .")
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 30, 1)
                                $ Girl.Statup("Inbt", 40, 1)
                        elif ApprovalCheck(Girl, 500, "OI"):
                                $ Girl.FaceChange("normal", 1)
                                if Girl is EmmaX:
                                        ch_e "Не дави на меня. . . слишком сильно."
                                elif Girl is JeanX:
                                        ch_j ". . ."
                                        ch_j "Наверное. . ."
                                elif Girl is StormX:
                                        ch_s "Я. . . нет. . ."
                                elif Girl is JubesX:
                                        ch_v "Не особо. . ."
                                elif Girl is BetsyX:
                                        ch_b "Было не так уж и плохо, но. . . прекрати."
                                else:
                                        call AnyLine(Girl,"Ну. . . думаю, может быть. . . нет, прекращай.")
                                $ Girl.Statup("Love", 60, -1)
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 30, 2)
                                $ Girl.Statup("Inbt", 40, 2)
                        else:
                                $ Girl.FaceChange("angry", 1)
                                $ Girl.Eyes = "side"
                                if Girl is KittyX:
                                        ch_k "Мне это не интересно."
                                elif Girl is EmmaX:
                                        ch_e "Уверена."
                                elif Girl is JeanX:
                                        ch_j "Определенно."
                                elif Girl is StormX:
                                        ch_s "Конечно."
                                elif Girl is GwenX:
                                        ch_g "Вполне уверена. . ."
                                elif Girl is BetsyX:
                                        ch_b "Конечно нет. . ."
                                else:
                                        call AnyLine(Girl,"Грррр. . .")
                                $ Girl.Statup("Love", 60, -3)
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 30, 3)
                                $ Girl.Statup("Inbt", 40, 2)
                #end "Are you sure you didn't enjoy that?"

        $ Girl.RecentActions.append("cheek")
        $ Girl.DailyActions.append("cheek")
        return
# End touch cheek/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Hold Hands / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Hold_Hands(Girl=0,Gloves=0): #rkeljsvgbdw
        # Called whenever you say "Hold Hands" in the flirt menu
        if Girl.Arms == "gloves":
            menu:
                "С перчатками или без?"
                "С перчатками":
                    pass
                "Без перчаток":
                    ch_p "Не могла бы ты снять перчатки ненадолго?"
                    if Girl is EmmaX:
                            ch_e "Хорошо, [Girl.Petname]. . ."
                    elif Girl is GwenX:
                            ch_g "Ладно? . ."
                    else:
                            call AnyLine(Girl,"Ладно, "+Girl.Petname+". . .")
                    $ Gloves = "gloves"
                    $ Girl.Arms = 0
        "Вы наклоняетесь и берете [Girl.Name_vin] за руку."
        if ApprovalCheck(Girl, 800,"L"):
                $ Girl.FaceChange("smile",1,Eyes="closed")
                "Она сжимает вашу руку и прислоняется своим плечом к вашему."
                $ Count = 10
        elif ApprovalCheck(Girl, 1200):
                $ Girl.FaceChange("bemused",1,Brows="confused")
                "Она слегка сжимает вашу руку в ответ."
                $ Count = 4
        elif ApprovalCheck(Girl, 800):
                $ Girl.FaceChange("bemused",2,Brows="confused")
                "Она слегка напрягается, но оставляет свою руку в вашей."
                $ Girl.FaceChange("bemused",1,Eyes="down")
                $ Count = 2
        else:
                #not cool with it
                $ Girl.FaceChange("angry",1)
                $ Girl.Statup("Love", 40, -1)
                $ Girl.Statup("Love", 60, -1)
                $ Girl.Statup("Obed", 60, 2)
                $ Girl.Statup("Obed", 80, 1)
                $ Girl.Statup("Inbt", 50, 1)
                if not Girl.Arms and Girl.Resistance:
                        $ Girl.Statup("Obed", 60, 2)
                        $ Girl.Statup("Lust", 30, 5)
                        $ Girl.Addict -= 2
                        $ Girl.Addictionrate += 1 if RogueX.Addictionrate < 5 else 0
                if Gloves == "gloves":
                        $ Girl.Arms = "gloves"
                        "Она шлепает вас по руке и снова надевает перчатки."
                else:
                        "Она шлепает вас по руке."
                call AnyLine(Girl,"Не веди себя так, будто мы давно знакомы.")
                return

        if Girl.Arms != "gloves":
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0

        while Count:
            $ Round -= 5
            if ApprovalCheck(Girl, 800,"L"):
                if Count >= 8:
                    $ Girl.Statup("Love", 90, 2)
                    $ Girl.Statup("Obed", 70, 2)
                    $ Girl.Statup("Lust", 30, 2)
            elif ApprovalCheck(Girl, 1200):
                if Count >= 3:
                    $ Girl.Statup("Love", 80, 3)
                    $ Girl.Statup("Obed", 70, 2)
                    $ Girl.Statup("Lust", 30, 1)
            elif ApprovalCheck(Girl, 800):
                    $ Girl.Statup("Love", 70, 2)
                    $ Girl.Statup("Obed", 50, 2)
            if Girl.Arms != "gloves" and Girl.Addictionrate >= 3 and Girl.Addict >= 5:
                    $ Girl.Statup("Lust", 50, 3)
                    $ Girl.Addict -= 2
                    $ Count += 1 if Count <= 1 else 0 #she keeps it up
                    if Girl.Lust >= 30:
                        $ Girl.FaceChange("sly",2)

            menu:
                "Продолжать держаться за руки.":
                        pass
                "Прекратить держаться за руки.":
                        $ Count = 0
                        $ Girl.FaceChange("bemused",1)
                        return
            $ Count -= 1
            $ Count = 0 if Round <= 10 else Count

        #loop breaks. . .

        $ Girl.AddWord(1,"holdhands","holdhands") #adds the "holdhands" trait to recent and daily actions

        if not ApprovalCheck(Girl, 800,"L") and not ApprovalCheck(Girl, 1200):
                # she's a little creeped out
                $ Girl.FaceChange("sadside",1,Brows="confused")
                $ Girl.Statup("Love", 60, -2)
                $ Girl.Statup("Obed", 60, -2)
                $ Girl.Statup("Inbt", 50, 3)
                $ Girl.Statup("Lust", 60, -5)
        else:
                $ Girl.FaceChange("smile",1)
        if Gloves == "gloves":
                $ Girl.Arms = "gloves"
        $ Gloves = 0
        call AnyLine(Girl,"Ладно, хватит. . .")
        return

# End Hold Hands / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Head Pat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Headpat(Girl=0): #rkeljsvgbdw
    $ Girl = GirlCheck(Girl)
    call Shift_Focus(Girl)
    $ Girl.FaceChange("surprised", 1)
    if "no headpat" in Girl.DailyActions:
            "Вы протягиваете руку, чтобы погладить [Girl.Name_vin] по голове, но она отмахивается от нее."
            $ Girl.FaceChange("angry")
            if Girl is RogueX:
                    ch_r "Держи руки при себе, [Girl.Petname]."
            elif Girl is KittyX:
                    ch_k "Я говорила тебе, это странно."
                    ch_k "Чудила."
            elif Girl is EmmaX:
                    ch_e "Мы разве уже не говорили об этой твоей одержимости \"поглаживаниями по голове\"?"
            elif Girl is LauraX:
                    ch_l "Руки прочь, серьезно."
            elif Girl is JeanX:
                    $ Girl.Eyes = "psychic"
                    ch_j "Я сказала тебе, держись подальше."
                    $ Girl.Eyes = "squint"
            elif Girl is StormX:
                    ch_s "Держись подальше от моих волос."
            elif Girl is JubesX:
                    ch_v "Эй, следи за руками!"
            elif Girl is GwenX:
                    ch_g "Вавава! [[размахивает руками над головой] . ."
            elif Girl is BetsyX:
                    ch_b "Что?"
            elif Girl is DoreenX:
                    ch_d "А? Хватит!"
            elif Girl is WandaX:
                    ch_w "Прекрати!"
            $ Girl.Statup("Love", 50, -2)
            return
    else:
            "Вы протягиваете руку и гладите [Girl.Name_vin] по голове."
    $ Girl.Statup("Obed", 50, 2)

    if ApprovalCheck(Girl, 1200,Alt=[[LauraX],1000]):
            $ Girl.FaceChange("sexy", 1)
            if Girl is EmmaX:
                    ch_e "Хмммм?"
            else:
                    call AnyLine(Girl,"Ммммм. . .")
            $ Girl.Statup("Love", 85, 1)
    elif ApprovalCheck(Girl, 800,Alt=[[EmmaX],1200]) or ApprovalCheck(Girl, 750, "L",Alt=[[LauraX],600]):
            $ Girl.FaceChange("smile", 1)
            call AnyLine(Girl,"Ммммм. . .")
    elif "headpat" in Girl.DailyActions:
            $ Girl.FaceChange("angry", 1)
            if Girl is RogueX:
                    ch_r "Держи руки при себе, [Girl.Petname]."
            elif Girl is KittyX:
                    ch_k "Эй, прекрати."
            elif Girl is EmmaX:
                    ch_e "Я похожа на ребенка или питомца?"
            elif Girl is LauraX:
                    ch_l "Я предупреждала тебя, не делать этого."
            elif Girl is JeanX:
                    ch_j "Эй! Испортишь прическу!"
            elif Girl is StormX:
                    ch_s "Назад. Сейчас же."
            elif Girl is JubesX:
                    ch_v "Что я тебе говорила?"
            elif Girl is GwenX:
                    ch_g "Прекрати!"
            elif Girl is BetsyX:
                    ch_b "Не желаешь прекратить?"
            elif Girl is DoreenX:
                    ch_d "-Хватит.-"
            elif Girl is WandaX:
                    ch_w "Прекрати!"
            $ Girl.Statup("Love", 50, -2)
            $ Girl.DailyActions.append("no headpat")
    elif ApprovalCheck(Girl, 400,Alt=[[EmmaX],600]):
            $ Girl.Mouth = "smile"
            $ Girl.Brows = "normal"
            if Girl is RogueX:
                    ch_r "Это как-то. . . странно."
            elif Girl is KittyX:
                    ch_k "Эм, ладно. . ."
            elif Girl is EmmaX:
                    ch_e "Хм. У тебя какие-то странные интересы."
            elif Girl is LauraX:
                    ch_l "Эм, это было странно."
            elif Girl is JeanX:
                    ch_j "Что за черт?"
            elif Girl is StormX:
                    ch_s "Что это значит?"
            elif Girl is JubesX:
                    ch_v "Чудила."
            elif Girl is GwenX:
                    ch_g "Что с тобой?"
            elif Girl is BetsyX:
                    ch_b "Мне. . . некомфортно."
            elif Girl is DoreenX:
                    ch_d "Эм. . . ой. . ."
            elif Girl is WandaX:
                    ch_w "Прекращай. . ."
    else:
            $ Girl.FaceChange("angry", 1)
            if Girl is RogueX:
                    "Она шлепает вас по руке и начинает сердито смотреть на вас."
                    ch_r "Прекрати!"
            elif Girl is KittyX:
                    "Она шлепает вас по руке и начинает сердито смотреть на вас."
                    ch_k "Прекращай!"
            elif Girl is EmmaX:
                    "Она хватает вас за запястье и убирает вашу руку от своих волос."
                    ch_e "Я предупреждаю тебя только один раз. Прекрати."
            elif Girl is LauraX:
                    "Она махает руками, отбивая вашу руку."
                    ch_l "Отойди от меня."
            elif Girl is JeanX:
                    $ Girl.Eyes = "psychic"
                    ch_j "Прекрати!"
                    $ Girl.Eyes = "squint"
            elif Girl is StormX:
                    ch_s "Остановись."
            elif Girl is JubesX:
                    ch_v "Эй. . ."
            elif Girl is GwenX:
                    ch_g "Прекрати!"
            elif Girl is BetsyX:
                    ch_b "Тебе стоит прекратить."
            elif Girl is DoreenX:
                    ch_d ". . . Хватит. . ."
            elif Girl is WandaX:
                    ch_w "Прекращай. . ."
            $ Girl.Statup("Love", 50, -3)
            $ Girl.Statup("Obed", 50, 1)
            $ Girl.Statup("Inbt", 30, 1)

    if "no headpat" in Girl.DailyActions:
        menu:
            "Прости-прости, подобного больше не повторится.":
                if ApprovalCheck(Girl, 300):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                ch_r "Я это уже слышала. . ."
                        elif Girl is KittyX:
                                ch_k "Угум."
                        elif Girl is EmmaX:
                                ch_e "Надеюсь, что так."
                        elif Girl is LauraX:
                                if not Player.Male:
                                    ch_l "Ага, перестань быть такой странной."
                                else:
                                    ch_l "Ага, перестань быть таким странным."
                        elif Girl is JeanX:
                                ch_j "Тогда ладно. . ."
                        elif Girl is StormX:
                                ch_s "Хорошо. . ."
                        elif Girl is JubesX:
                                ch_v "Нууу, прекращай."
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Ты это уже говорила. . ."
                                else:
                                    ch_g "Ты это уже говорил. . ."
                        elif Girl is BetsyX:
                                ch_b "Надеюсь. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . ладно. . ."
                        elif Girl is WandaX:
                                ch_w "Конечно, как скажешь."
                        $ Girl.Statup("Love", 80, 2)
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Eyes = "side"
                        if Girl is RogueX:
                                ch_r "Чертовски верно. . ."
                        elif Girl is KittyX:
                                ch_k "Лучше не надо."
                        elif Girl is EmmaX:
                                "[EmmaX.Name] молча смотрит на вас."
                        elif Girl is LauraX:
                                ch_l "Угу-м."
                        elif Girl is JeanX:
                                ch_j "Лучше не надо."
                        elif Girl is StormX:
                                ch_s "Надеюсь, что нет. . ."
                        elif Girl is JubesX:
                                ch_v "Конечно. . ."
                        elif Girl is GwenX:
                                ch_g "Угу-м. . ."
                        elif Girl is BetsyX:
                                ch_b "Надеюсь, что нет. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . ладно. . ."
                        elif Girl is WandaX:
                                ch_w "Угу-м. . ."
                        $ Girl.Statup("Obed", 20, 1)

            "Мне показалось, ты сама этого хочешь.":
                if ApprovalCheck(Girl, 400, "OI",Alt=[[EmmaX],600]) or ApprovalCheck(Girl, 800,Alt=[[EmmaX],900]):
                        $ Girl.FaceChange("normal", 1)
                        $ Girl.Eyes = "squint"
                        if Girl is RogueX:
                                ch_r "Я. . . ну, может быть?"
                        elif Girl is KittyX:
                                ch_k "Моооожет быыыть. . ."
                        elif Girl is EmmaX:
                                ch_e "Хммм. . ."
                        elif Girl is LauraX:
                                ch_l "Эм. . ."
                        elif Girl is JeanX:
                                ch_j "Эм. . . ладно. . ."
                        elif Girl is StormX:
                                ch_s "Что ж. . ."
                        elif Girl is JubesX:
                                ch_v "Хмм. . ."
                        elif Girl is GwenX:
                                ch_g ". . ."
                        elif Girl is BetsyX:
                                ch_b "Возможно. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . эм. . ."
                        elif Girl is WandaX:
                                ch_w "Не правда."
                        $ Girl.Statup("Love", 60, -1)
                        $ Girl.Statup("Obed", 30, 2)
                        $ Girl.Statup("Inbt", 40, 2)
                else:
                        $ Girl.FaceChange("angry", 2)
                        $ Girl.Eyes = "squint"
                        if Girl is RogueX:
                                ch_r "На твоем месте, я бы на это не рассчитывала."
                        elif Girl is KittyX:
                                ch_k "Эм. . ."
                        elif Girl is EmmaX:
                                ch_e "Что за ерунда. . ."
                        elif Girl is LauraX:
                                ch_l "Нет!"
                        elif Girl is JeanX:
                                ch_j "Ты меня не знаешь."
                        elif Girl is StormX:
                                ch_s "Значит, ты плохо меня знаешь."
                        elif Girl is JubesX:
                                ch_v "Хочешь узнать?"
                        elif Girl is GwenX:
                                ch_g ". . . Не-а!"
                        elif Girl is BetsyX:
                                ch_b "Я в этом сомневаюсь. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . что?"
                        elif Girl is WandaX:
                                ch_w "Не правда."
                        $ Girl.Blush = 1
                        $ Girl.Statup("Love", 60, -3)
                        $ Girl.Statup("Obed", 30, 3)
                        $ Girl.Statup("Inbt", 40, 2)

    else:
        #if she hasn't refused this today. . .
        menu:
            "Прости, ты просто выглядишь такой милой.":
                if ApprovalCheck(Girl, 850, "LI",Alt=[[EmmaX],1050]):
                        $ Girl.FaceChange("sexy", 1)
                        $ Count = 7
                        if Girl is RogueX:
                                "Она слегка наклоняет голову."
                                ch_r "Мммм. . ."
                        elif Girl is KittyX:
                                "Она наклоняется к вам."
                                ch_k "Муррррр. . ."
                        elif Girl is EmmaX:
                                "Она мгновение колеблется, но потом медленно закрывает глаза."
                                if not Player.Male:
                                    ch_e "Будь благодарна. Я никому больше не позволила бы сделать подобное."
                                else:
                                    ch_e "Будь благодарен. Я никому больше не позволила бы сделать подобное."
                                $ Count -= 2
                        elif Girl is LauraX:
                                "Она наклоняется к вам."
                                ch_l "Ммммм. . ."
                        elif Girl is JeanX:
                                ch_j "Я всегда выгляжу мило. . ."
                        elif Girl is StormX:
                                ch_s "Полагаю, так и есть. . ."
                        elif Girl is JubesX:
                                ch_v "Я всегда такая. . ."
                        elif Girl is GwenX:
                                $ Girl.FaceChange("smile", 1,Eyes="closed")
                                ch_g ". . ."
                                $ Girl.FaceChange("sly", 1)
                        elif Girl is BetsyX:
                                ch_b "В самом деле? . ."
                        elif Girl is DoreenX:
                                ch_d "Эм. . . ладно. . ."
                        elif Girl is WandaX:
                                ch_w "Ага."
                        $ Girl.Statup("Love", 80, 2)
                elif ApprovalCheck(Girl, 500, "LI",Alt=[[EmmaX],700]):
                        $ Girl.FaceChange("smile", 1)
                        $ Count = 5
                        if Girl is RogueX:
                                ch_r "Ну что ж, продолжай. . ."
                        elif Girl is KittyX:
                                ch_k "Скажи мне что-нибудь, чего я не знаю."
                        elif Girl is EmmaX:
                                ch_e "Просто мило? Должно быть я теряю хватку."
                                $ Count -= 1
                        elif Girl is LauraX:
                                ch_l "Я не милая."
                                ch_l "Но продолжай."
                        elif Girl is JeanX:
                                ch_j "Я всегда выгляжу мило. . ."
                        elif Girl is StormX:
                                ch_s "Полагаю, так и есть. . ."
                        elif Girl is JubesX:
                                ch_v "Конечно. . ."
                        elif Girl is GwenX:
                                ch_g "Ну. . . ладно. . ."
                        elif Girl is BetsyX:
                                ch_b "Я надеялась, что ты оценишь меня повыше. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . Правда?"
                        elif Girl is WandaX:
                                ch_w "Правда?"
                        $ Girl.Statup("Love", 80, 2)
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Eyes = "side"
                        if Girl is RogueX:
                                ch_r "Ты что-то замышляешь. . ."
                        elif Girl is KittyX:
                                ch_k "Да, конечно. Не надо врать."
                        elif Girl is EmmaX:
                                ch_e "Тебе придется придумать что-то получше, [Girl.Petname]. Намного лучше."
                        elif Girl is LauraX:
                                ch_l "Эта милашка может откусить тебе руку."
                        elif Girl is JeanX:
                                ch_j "Я всегда выгляжу мило. Можешь смотреть, но не трогать."
                        elif Girl is StormX:
                                ch_s "Я в этом не уверена. . ."
                        elif Girl is JubesX:
                                ch_v "Ага, верно."
                        elif Girl is GwenX:
                                ch_g "Как скажешь. . ."
                        elif Girl is BetsyX:
                                ch_b "Я не вижу причинно-следственную связь. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . и что? . ."
                        elif Girl is WandaX:
                                ch_w "Просто. . . успокойся."
                        $ Girl.Statup("Obed", 20, 1)
                        $ Count = 1

            "Я хотел поправить твою прическу." if Player.Male:
                if ApprovalCheck(Girl, 700, "LI",Alt=[[EmmaX,JeanX],850]):
                        $ Girl.FaceChange("sexy", 1)
                        $ Count = 4
                        if Girl is RogueX:
                                ch_r "Да? Тогда тебе лучше продолжить. . ."
                        elif Girl is KittyX:
                                ch_k "Поправить прическу? Мне?"
                        elif Girl is EmmaX:
                                ch_e "Поправить прическу, говоришь? Полагаю, тогда тебе стоит помочь мне."
                                $ Count += 1
                        elif Girl is LauraX:
                                ch_l "А? Как скажешь. . ."
                        elif Girl is JeanX:
                                ch_j "Хмм. . ."
                        elif Girl is StormX:
                                ch_s "Ох? . ."
                        elif Girl is JubesX:
                                ch_v "Не с таким стилем."
                        elif Girl is GwenX:
                            if Girl.Hat:
                                ch_g ". . . как?"
                            else:
                                ch_g "Ну. . . ладно. . ."
                        elif Girl is BetsyX:
                                ch_b "Я надеюсь, что нет. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . ладно. . ."
                        elif Girl is WandaX:
                                ch_w "Конечно. . ."
                        $ Girl.Statup("Love", 60, 1)
                        $ Girl.Statup("Inbt", 40, 1)
                elif ApprovalCheck(Girl, 700):
                        $ Girl.FaceChange("normal")
                        $ Count = 3
                        if Girl is RogueX:
                                ch_r "Что-то здесь не так. . ."
                        elif Girl is KittyX:
                                ch_k "Прическа, точно. . ."
                        elif Girl is EmmaX:
                                ch_e "Поправить прическу? Ох, [Girl.Petname]. Я думала, ты будешь более изобретательным."
                        elif Girl is LauraX:
                                ch_l "Прическа, ага. . ."
                        elif Girl is JeanX:
                                ch_j "Как-то подозрительно. . ."
                        elif Girl is StormX:
                                ch_s "Ох? . ."
                        elif Girl is JubesX:
                                ch_v "Не с таким стилем."
                        elif Girl is GwenX:
                            if Girl.Hat:
                                ch_g ". . . как?"
                            else:
                                ch_g "Ну. . . ладно. . ."
                        elif Girl is BetsyX:
                                ch_b "Я в этом сомневаюсь. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . ладно. . ."
                        elif Girl is WandaX:
                                ch_w "Конечно. . ."
                else:
                        $ Girl.FaceChange("angry", 1)
                        if Girl is RogueX:
                                ch_r "Это не повод портить отношения."
                        elif Girl is KittyX:
                                ch_k "Угу, только. . . только смотри, ладно?"
                        elif Girl is EmmaX:
                                ch_e "Я могу справиться с этим сама."
                        elif Girl is LauraX:
                                ch_l "Угу, только не трогай меня."
                        elif Girl is JeanX:
                                ch_j "Как-то слабо верится."
                        elif Girl is StormX:
                                ch_s "Как правдоподобно. . ."
                        elif Girl is JubesX:
                                ch_v "Не с таким стилем."
                        elif Girl is GwenX:
                            if Girl.Hat:
                                ch_g ". . . как?!"
                            else:
                                ch_g "Нууу. . . прекрати!"
                        elif Girl is BetsyX:
                                ch_b "Это очень маловероятно. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . но все равно не делай этого."
                        elif Girl is WandaX:
                                ch_w "Оставь ее в покое!"
                        $ Girl.Statup("Obed", 50, 2)
                        $ Count = 1

            "Я хотела поправить твою прическу." if not Player.Male:
                if ApprovalCheck(Girl, 700, "LI",Alt=[[EmmaX,JeanX],850]):
                        $ Girl.FaceChange("sexy", 1)
                        $ Count = 4
                        if Girl is RogueX:
                                ch_r "Да? Тогда тебе лучше продолжить. . ."
                        elif Girl is KittyX:
                                ch_k "Поправить прическу? Мне?"
                        elif Girl is EmmaX:
                                ch_e "Поправить прическу, говоришь? Полагаю, тогда тебе стоит помочь мне."
                                $ Count += 1
                        elif Girl is LauraX:
                                ch_l "А? Как скажешь. . ."
                        elif Girl is JeanX:
                                ch_j "Хмм. . ."
                        elif Girl is StormX:
                                ch_s "Ох? . ."
                        elif Girl is JubesX:
                                ch_v "Не с таким стилем."
                        elif Girl is GwenX:
                            if Girl.Hat:
                                ch_g ". . . как?"
                            else:
                                ch_g "Ну. . . ладно. . ."
                        elif Girl is BetsyX:
                                ch_b "Я надеюсь, что нет. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . ладно. . ."
                        elif Girl is WandaX:
                                ch_w "Конечно. . ."
                        $ Girl.Statup("Love", 60, 1)
                        $ Girl.Statup("Inbt", 40, 1)
                elif ApprovalCheck(Girl, 700):
                        $ Girl.FaceChange("normal")
                        $ Count = 3
                        if Girl is RogueX:
                                ch_r "Что-то здесь не так. . ."
                        elif Girl is KittyX:
                                ch_k "Прическа, точно. . ."
                        elif Girl is EmmaX:
                                ch_e "Поправить прическу? Ох, [Girl.Petname]. Я думала, ты будешь более изобретательной."
                        elif Girl is LauraX:
                                ch_l "Прическа, ага. . ."
                        elif Girl is JeanX:
                                ch_j "Как-то подозрительно. . ."
                        elif Girl is StormX:
                                ch_s "Ох? . ."
                        elif Girl is JubesX:
                                ch_v "Не с таким стилем."
                        elif Girl is GwenX:
                            if Girl.Hat:
                                ch_g ". . . как?"
                            else:
                                ch_g "Ну. . . ладно. . ."
                        elif Girl is BetsyX:
                                ch_b "Я в этом сомневаюсь. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . ладно. . ."
                        elif Girl is WandaX:
                                ch_w "Конечно. . ."
                else:
                        $ Girl.FaceChange("angry", 1)
                        if Girl is RogueX:
                                ch_r "Это не повод портить отношения."
                        elif Girl is KittyX:
                                ch_k "Угу, только. . . только смотри, ладно?"
                        elif Girl is EmmaX:
                                ch_e "Я могу справиться с этим сама."
                        elif Girl is LauraX:
                                ch_l "Угу, только не трогай меня."
                        elif Girl is JeanX:
                                ch_j "Как-то слабо верится."
                        elif Girl is StormX:
                                ch_s "Как правдоподобно. . ."
                        elif Girl is JubesX:
                                ch_v "Не с таким стилем."
                        elif Girl is GwenX:
                            if Girl.Hat:
                                ch_g ". . . как?!"
                            else:
                                ch_g "Нууу. . . прекрати!"
                        elif Girl is BetsyX:
                                ch_b "Это очень маловероятно. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. . . но все равно не делай этого."
                        elif Girl is WandaX:
                                ch_w "Оставь ее в покое!"
                        $ Girl.Statup("Obed", 50, 2)
                        $ Count = 1

            "Уверена, что тебе не понравилось?":
                if ApprovalCheck(Girl, 850,Alt=[[EmmaX,JeanX],1000]):
                        $ Girl.FaceChange("sexy", 1)
                        $ Girl.Eyes = "side"
                        if Girl is RogueX:
                                ch_r "Ну, может и понравилось. . ."
                        elif Girl is KittyX:
                                ch_k "Хммм. . . может быть, а может и нет."
                        elif Girl is EmmaX:
                                ch_e "Что ж, пожалуй, понравилось."
                        elif Girl is LauraX:
                                ch_l "Ну. . . понравилось. . ."
                        elif Girl is JeanX:
                                ch_j "Хмм. . . ."
                        elif Girl is StormX:
                                ch_s "Хмм. . ."
                        elif Girl is JubesX:
                                ch_v "Ну. . ."
                        elif Girl is GwenX:
                                ch_g "Ладно, понравилось. . ."
                        elif Girl is BetsyX:
                                ch_b "Все возможно. . ."
                        elif Girl is DoreenX:
                                ch_d "Эм. . . может и понравилось. . ."
                        elif Girl is WandaX:
                                ch_w ". . ."
                        $ Girl.Statup("Obed", 50, 2)
                        $ Girl.Statup("Obed", 30, 1)
                        $ Girl.Statup("Inbt", 40, 1)
                        $ Count = 4
                elif ApprovalCheck(Girl, 500, "OI"):
                        $ Girl.FaceChange("normal", 1)
                        $ Count = 2
                        if Girl is RogueX:
                                ch_r "Не. . . совсем?"
                        elif Girl is KittyX:
                                ch_k "Ну. . . думаю, возмооожно. . . неее. . . не понравилось."
                        elif Girl is EmmaX:
                                ch_e "Ах. . . нет-нет. У леди должны быть свои секреты."
                                $ Count += 1
                        elif Girl is LauraX:
                                ch_l "Ну. . . думаю, возможно. . . нет, не понравилось, хватит."
                        elif Girl is JeanX:
                                ch_j "Хмм. . . у-гум."
                        elif Girl is StormX:
                                ch_s "Да, скорее всего - да. . ."
                        elif Girl is JubesX:
                                ch_v "Честно говоря, так себе."
                        elif Girl is GwenX:
                                ch_g "Не понравилось. . ."
                        elif Girl is BetsyX:
                                ch_b "На это я отвечать не собираюсь. . ."
                        elif Girl is DoreenX:
                                ch_d "Эм. . . вполне. . ."
                        elif Girl is WandaX:
                                ch_w "Да."
                        $ Girl.Statup("Love", 60, -1)
                        $ Girl.Statup("Obed", 50, 2)
                        $ Girl.Statup("Obed", 30, 2)
                        $ Girl.Statup("Inbt", 40, 2)
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Eyes = "side"
                        if Girl is RogueX:
                                ch_r "Ох, уверена."
                        elif Girl is KittyX:
                                ch_k "Грррр. . ."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Если бы ты попробовала это несколько лет назад. . ."
                                else:
                                    ch_e "Если бы ты попробовал это несколько лет назад. . ."
                        elif Girl is LauraX:
                                ch_l "Грррр. . ."
                        elif Girl is JeanX:
                                ch_j "Уверена."
                        elif Girl is StormX:
                                ch_s "Мне определенно не понравилось."
                        elif Girl is JubesX:
                                ch_v "Мне точно не понравилось."
                        elif Girl is GwenX:
                                ch_g "Ага!"
                        elif Girl is BetsyX:
                                ch_b "Вполне."
                        elif Girl is DoreenX:
                                ch_d "Черт, конечно же я уверена."
                        elif Girl is WandaX:
                                ch_w "Да, абсолютно."
                        $ Girl.Statup("Love", 60, -3)
                        $ Girl.Statup("Obed", 50, 2)
                        $ Girl.Statup("Obed", 30, 3)
                        $ Girl.Statup("Inbt", 40, 2)
                        $ Count = 1
        while Count > 0 and Round >= 10:
            $ Count -= 1 if Count != 4 else 0
            $ Round -= 1
            menu:
                "Продолжите?"
                "Да":
                    "Вы продолжаете держать свою руку на голове [Girl.Name_rod], нежно поглаживая."
                    if Count <= 0:
                        #timed out
                        if ApprovalCheck(Girl, 800):
                                $ Girl.FaceChange("bemused", 2)
                                $ Girl.Statup("Love", 80, 2)
                                $ Girl.Statup("Inbt", 40, 2)
                                if Girl is RogueX:
                                        ch_r "Эй, ладно, больше не надо. . ."
                                elif Girl is KittyX:
                                        ch_k "Эй, ладно, думаю, хватит. . ."
                                elif Girl is EmmaX:
                                        ch_e "Думаю. . . достаточно."
                                elif Girl is LauraX:
                                        ch_l "Ладно, хватит. . ."
                                elif Girl is JeanX:
                                        ch_j "Ладно, хватит."
                                elif Girl is StormX:
                                        ch_s "Ладно, можешь остановиться."
                                elif Girl is JubesX:
                                        ch_v "Ладно, хорошо."
                                elif Girl is GwenX:
                                        ch_g "Ладно-ладно. . . хватит. . ."
                                elif Girl is BetsyX:
                                        ch_b "Я думаю, этого достаточно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ладно. . . хватит."
                                elif Girl is WandaX:
                                        ch_w "Ладно, ладно, прекращай уже."
                                "Она выскользает из-под вашей руки."
                                $ Girl.FaceChange("bemused", 1)
                        else:
                                $ Girl.FaceChange("angry", 2)
                                $ Girl.Statup("Love", 60, -5)
                                $ Girl.Statup("Inbt", 40, 3)
                                if Girl is RogueX:
                                        ch_r "Ну хватит уже."
                                elif Girl is KittyX:
                                        ch_k "Ладно, думаю, хватит. . ."
                                elif Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Думаю, ты уже достаточно повеселилась. . ."
                                        else:
                                            ch_e "Думаю, ты уже достаточно повеселился. . ."
                                elif Girl is LauraX:
                                        ch_l "Ладно, хватит уже. . ."
                                elif Girl is JeanX:
                                        ch_j "Прекрати сейчас же."
                                elif Girl is StormX:
                                        ch_s "Остановись сейчас же."
                                elif Girl is JubesX:
                                        ch_v "Ладно, прекращай."
                                elif Girl is GwenX:
                                        ch_g "Ладно, хватит."
                                elif Girl is BetsyX:
                                        ch_b "Достаточно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ладно. . . прекращай."
                                elif Girl is WandaX:
                                        ch_w "Довольно."
                                "Она откидывает вашу руку."
                                $ Girl.FaceChange("angry", 1)
                    elif Count == 1:
                        #nearly timed out
                        if ApprovalCheck(Girl, 800,Alt=[[EmmaX],900]):
                                $ Girl.FaceChange("bemused", 1)
                                $ Girl.Statup("Love", 80, 1)
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Inbt", 40, 2)
                                if Girl is RogueX:
                                        ch_r "Эм, может, ты хочешь. . ."
                                elif Girl is KittyX:
                                        ch_k "Наверное, нам пора заняться чем-нибудь другим. . ."
                                elif Girl is EmmaX:
                                        if Taboo > 20:
                                                ch_e "Нам не стоит заниматься таким на людях. . . мне нужно поддерживать свою репутацию."
                                        else:
                                                ch_e "Только давай осторожнее, мы все-таки на людях. . . и мне нужно поддерживать свою репутацию."
                                elif Girl is LauraX:
                                        ch_l "Нам лучше заняться чем-нибудь другим. . ."
                                elif Girl is JeanX:
                                        ch_j "Тебе лучше прекратить."
                                elif Girl is StormX:
                                        ch_s "Ты собираешься. . . тогда ладно. . ."
                                elif Girl is JubesX:
                                        ch_v "Наверное, стоит дать ей отдохнуть."
                                elif Girl is GwenX:
                                        ch_g "Наверное, нам стоит прекратить. . ."
                                elif Girl is BetsyX:
                                        ch_b "Мне кажется, этого достаточно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ладно. . . скоро надо будет остановиться. . ."
                                elif Girl is WandaX:
                                        ch_w "Думаю, уже хватит."
                        else:
                                $ Girl.FaceChange("angry", 2)
                                $ Girl.Statup("Love", 60, -2)
                                $ Girl.Statup("Obed", 60, 2)
                                $ Girl.Statup("Obed", 30, 2)
                                if Girl is RogueX:
                                        ch_r "Тебе лучше прекратить. . ."
                                elif Girl is KittyX:
                                        ch_k "Знаешь, [Girl.Name] может и поцарапать."
                                elif Girl is EmmaX:
                                        ch_e "Не испытывай свою удачу."
                                elif Girl is LauraX:
                                        ch_l "Ты хочешь потерять эту руку?"
                                elif Girl is JeanX:
                                        ch_j "Тебе лучше прекратить."
                                elif Girl is StormX:
                                        ch_s "Довольно."
                                elif Girl is JubesX:
                                        ch_v "Ладно, прекращай."
                                elif Girl is GwenX:
                                        ch_g "Ладно, остановись. . ."
                                elif Girl is BetsyX:
                                        ch_b "Довольно."
                                elif Girl is DoreenX:
                                        ch_d "Ладно. . . хватит."
                                elif Girl is WandaX:
                                        ch_w "Ладно, достаточно."
                    else:
                        #she's ok with it. . .
                        if ApprovalCheck(Girl, 800,Alt=[[EmmaX],900]):
                                $ Girl.FaceChange("bemused", 2,Eyes="closed")
                                if Count > 5:
                                        $ Girl.Statup("Love", 90, 1)
                                        $ Girl.Statup("Love", 70, 1)
                                        $ Girl.Statup("Obed", 50, 1)
                                if Girl is RogueX:
                                        ch_r "Уххх. . ."
                                elif Girl is KittyX:
                                        ch_k "Ммммм. . ."
                                        "Она практически мурчит."
                                elif Girl is EmmaX:
                                        ch_e "Ммммм. . . тебе правда не стоит. . ."
                                        "Похоже, ей очень нравится. . ."
                                elif Girl is JeanX:
                                        ch_j "Хмммм. . ."
                                else:
                                        call AnyLine(Girl,"Ммммм. . .")
                        else:
                                $ Girl.FaceChange("angry", 1)
                                $ Girl.Statup("Love", 60, -1)
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 30, 2)
                                $ Girl.Statup("Inbt", 40, 2)
                                if Girl is EmmaX:
                                        ch_e "Эм. . ."
                                else:
                                        call AnyLine(Girl,"Эм. . .")
                                $ Count -= 1 if Count > 2 else 0
                "Нет":
                    $ Count = 0
    $ Count = 0
    $ Girl.RecentActions.append("headpat")
    $ Girl.DailyActions.append("headpat")
    return
# End Head Pat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Kiss Cheek / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Kiss_Cheek:
        "Вы наклоняетесь, откидываете ее волосы в сторону и целуете ее в щеку."
        if ApprovalCheck(Girl, 650, "L", TabM=1):
                    $ Girl.FaceChange("sexy", 1)
                    $ Girl.Statup("Love", 90, 1)
                    $ Girl.Statup("Obed", 40, 2)
                    if Girl is RogueX:
                            ch_r "Это было  очень мило, [Girl.Petname]."
                    elif Girl is KittyX:
                            ch_k ". . ."
                            ch_k "Ох, ого."
                    elif Girl is EmmaX:
                            ch_e ". . ."
                            ch_e "Ну здравствуй. . ."
                    elif Girl is LauraX:
                            ch_l ". . ."
                            $ Girl.FaceChange("sexy", 1, Eyes="side")
                            ch_l "Хм."
                    elif Girl is JeanX:
                            ch_j "Хм."
                    elif Girl is StormX:
                            ch_s "Ох, ну здравствуй. . ."
                    elif Girl is JubesX:
                            ch_v "Ох, приветик. . ."
                    elif Girl is GwenX:
                            ch_g "Ооох. . ."
                    elif Girl is BetsyX:
                            ch_b "Ох. . ."
                    elif Girl is DoreenX:
                            ch_d "Ох, -ну привет.-"
                    elif Girl is WandaX:
                            ch_w "Это было мило. . ."
        elif ApprovalCheck(Girl, 500, "L", TabM=1):
                    $ Girl.FaceChange("surprised", 1)
                    $ Girl.Statup("Love", 70, 2)
                    $ Girl.Statup("Obed", 40, 2)
                    $ Girl.Statup("Inbt", 20, 1)
                    if Girl is RogueX:
                            ch_r "Что это было, [Girl.Petname]?"
                    elif Girl is KittyX:
                            ch_k ". . . эй! В чем дело?"
                    elif Girl is EmmaX:
                            ch_e ". . . чем обязана такому удовольствию?"
                    elif Girl is LauraX:
                            ch_l ". . . эй!"
                            ch_l "Что это значит?"
                    elif Girl is JeanX:
                            ch_j "Эм. . ."
                    elif Girl is StormX:
                            ch_s "Ох?"
                    elif Girl is JubesX:
                            ch_v "Эй. . ."
                    elif Girl is GwenX:
                            ch_g "Ну привет. . ."
                    elif Girl is BetsyX:
                            ch_b "Здравствуй. . ."
                    elif Girl is DoreenX:
                            ch_d "Ох, привет."
                    elif Girl is WandaX:
                            ch_w "Эй, что это было?"
        elif ApprovalCheck(Girl, 300, "L", TabM=1):
                    $ Girl.FaceChange("angry", 1)
                    $ Girl.Statup("Love", 90, -1,Alt=[[JeanX],50,2])
                    $ Girl.Statup("Obed", 60, 2)
                    $ Girl.Statup("Inbt", 40, 1)
                    if Girl is RogueX:
                            ch_r "Эй, держи дистанцию, [Girl.Petname]!"
                    elif Girl is KittyX:
                            ch_k "Я[Girl.like]не понимаю, почему тебе такое нравится?"
                    elif Girl is EmmaX:
                            ch_e "Это совершенно неуместно, [Girl.Petname]"
                            ch_e "[[бормочет себе под нос] -по крайней мере, на людях. . ."
                    elif Girl is LauraX:
                            ch_l "Ты слишком спешишь."
                    elif Girl is JeanX:
                            $ Girl.Brows = "confused"
                            ch_j "Эй, это что еще такое?"
                    elif Girl is StormX:
                            ch_s "Это совершенно неуместно. . ."
                    elif Girl is JubesX:
                            ch_v "Что это было? . ."
                    elif Girl is GwenX:
                            ch_g "Эй!"
                    elif Girl is BetsyX:
                            ch_b "Ох! Ну и ну. . ."
                    elif Girl is DoreenX:
                            ch_d "Ох, что?"
                    elif Girl is WandaX:
                            ch_w "Эй, что это было?"
        else:
                    $ Girl.FaceChange("angry", 1)
                    $ Girl.Statup("Love", 90, -5,Alt=[[JeanX],50,2])
                    $ Girl.Statup("Obed", 90, 5)
                    $ Girl.Statup("Inbt", 40, 3)
                    if Girl is RogueX:
                            ch_r "Эй, отойди!"
                    elif Girl is KittyX:
                            ch_k "Отстань от меня!"
                    elif Girl is EmmaX:
                            ch_e "Прекрати, сейчас же."
                    elif Girl is LauraX:
                            ch_l "Отойди!"
                    elif Girl is JeanX:
                            $ Girl.Eyes = "psychic"
                            ch_j "Назад!"
                            $ Girl.Eyes = "sexy"
                    elif Girl is StormX:
                            $ Girl.Eyes = "white"
                            ch_s "Что ты делаешь?!"
                            $ Girl.Eyes = "sexy"
                    elif Girl is JubesX:
                            ch_v "Эй!"
                    elif Girl is GwenX:
                            ch_g "Какого черта. . ."
                    elif Girl is BetsyX:
                            ch_b "Что?"
                    elif Girl is DoreenX:
                            ch_d "Эй!"
                    elif Girl is WandaX:
                            ch_w "Эй, что это было?"
        $ Girl.Addict -= 1
        $ Girl.Addictionrate += 1
        $ Girl.Addictionrate = 3 if Girl.Addictionrate < 3 else Girl.Addictionrate
        return

#End Kiss Cheek / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Kiss lips / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Kiss_Lips:
        if ApprovalCheck(Girl, 1000, TabM=2,Alt=[[RogueX],800]) or ApprovalCheck(Girl, 600, "L", TabM=2):
                $ Line = renpy.random.choice(["Вы наклоняетесь, кладете руку ей на щеку и целуете в губы.",
                                                "Вы наклоняетесь, откидываете ее голову назад и целуете в губы.",
                                                "Вы наклоняетесь к "+Girl.Name_dat+" и целуете ее в губы."])
                "[Line]"
        elif ApprovalCheck(Girl, 1000,Alt=[[RogueX],800]) or ApprovalCheck(Girl, 600, "L"):
                $ Girl.FaceChange("bemused", 1)
                $ Girl.Eyes = "side"
                $ Girl.Statup("Obed", 50, -1,Alt=[[JeanX],50,2])
                $ Girl.Statup("Inbt", 40, 2)
                if Girl is RogueX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] кладет руку вам на лицо и отталкивает назад."
                        ch_r "[Girl.Petname], разве здесь не слишком людно?"
                elif Girl is KittyX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_k "Не на людях."
                elif Girl is EmmaX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] кладет руку вам на лицо и отталкивает назад."
                        ch_e "Не на людях, [Girl.Petname]."
                elif Girl is LauraX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_l "Не здесь, [Girl.Petname]."
                elif Girl is JeanX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_j "Эм, не здесь, [Girl.Petname]."
                elif Girl is StormX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_s "Не на людях, [Girl.Petname]."
                elif Girl is JubesX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_v "Нет, не на людях. . ."
                elif Girl is GwenX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_g "Эй! Не здесь, ладно. . .?"
                elif Girl is BetsyX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_b "На людях держи дистанцию. . ."
                elif Girl is DoreenX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_d "Эй, не здесь. . ."
                elif Girl is WandaX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] мягко отталкивает вас."
                        ch_w "Слушай, что это было?"
                return
        else:
                $ Girl.FaceChange("angry", 1)
                $ Girl.Statup("Love", 90, -5,Alt=[[JeanX],50,2])
                $ Girl.Statup("Obed", 50, -1,Alt=[[JeanX],50,1])
                $ Girl.Statup("Inbt", 40, 5)
                if Girl is RogueX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] кладет руку вам на лицо и отталкивает назад."
                        ch_r "[Girl.Petname], какого черта?"
                elif Girl is KittyX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_k "Держись подальше."
                elif Girl is EmmaX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] кладет руку вам на лицо и отталкивает назад."
                        ch_e "Нет."
                elif Girl is LauraX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_l "[Girl.Petname], держи себя в руках."
                elif Girl is JeanX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_j "Назад, [Girl.Petname]."
                elif Girl is StormX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_s "Ох, нет, благодарю, [Girl.Petname]"
                elif Girl is JubesX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_v "Ох, эм, нет, спасибо. . ."
                elif Girl is GwenX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_g "Эм, не лезь в мое личное пространство. . ."
                elif Girl is BetsyX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_b "[Girl.Petname], тебе стоит сохранять дистанцию. . ."
                elif Girl is DoreenX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] осторожно толкает вас локтем в ребра."
                        ch_d "Эй, не подходи слишком близко. . ."
                elif Girl is WandaX:
                        "Вы наклоняетесь к ней для поцелуя, но [Girl.Name] мягко отталкивает вас."
                        ch_w "И что это было?"
                return
        if Girl.Kissed:
                #if this wasn't the first kiss. . .
                if ApprovalCheck(Girl, 750, "L", TabM=1):
                        $ Girl.FaceChange("sexy", 1)
                        $ Girl.Statup("Love", 90, 2)
                        $ Girl.Statup("Obed", 50, 2)
                        if Girl is RogueX:
                                ch_r "Хмм, мы должны повторить, [Girl.Petname]."
                        else:
                                call AnyLine(Girl,"Мммммм. . .")
                elif ApprovalCheck(Girl, 650, "L", TabM=1):
                        $ Girl.FaceChange("sexy", 1)
                        $ Girl.Statup("Love", 90, 2)
                        $ Girl.Statup("Obed", 50, 2)
                        if Girl is RogueX:
                                ch_r "Хмм, это был приятный сюрприз, [Girl.Petname]?"
                        elif Girl is KittyX:
                                ch_k "Хмм, и тебе \"привет\", [Girl.Petname]?"
                        elif Girl is EmmaX:
                                ch_e "Хмм, здравствуй, [Girl.Petname]. . ."
                        elif Girl is LauraX:
                                ch_l "Хмм, как мило. . ."
                        elif Girl is JeanX:
                                ch_j "Хмм. . ."
                        elif Girl is StormX:
                                ch_s "Хмм. . ."
                        elif Girl is JubesX:
                                ch_v "Ммммм. . ."
                        elif Girl is GwenX:
                                ch_g "Ммммм. . ."
                        elif Girl is BetsyX:
                                ch_b "Это был прекрасный сюрприз. . ."
                        elif Girl is DoreenX:
                                ch_d "Ну, это было приятно. . ."
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"
                elif ApprovalCheck(Girl, 500, "L", TabM=1):
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Statup("Love", 70, 3)
                        $ Girl.Statup("Obed", 50, 2)
                        if Girl is RogueX:
                                ch_r "Эй, ты хоть когда-нибудь думаешь, что делаешь, [Girl.Petname]?"
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Тебе не кажется, что[Girl.like]ты слегка поторопилась?"
                                else:
                                    ch_k "Тебе не кажется, что[Girl.like]ты слегка поторопился?"
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Ты неисправима."
                                else:
                                    ch_e "Ты неисправим."
                        elif Girl is LauraX:
                                ch_l "Не знаю, что и думать."
                        elif Girl is JeanX:
                                ch_j "Эй!"
                        elif Girl is StormX:
                                ch_s "Эй. . ."
                        elif Girl is JubesX:
                                ch_v "Эй, это не круто. . ."
                        elif Girl is GwenX:
                                ch_g "Эй, это немного. . ."
                        elif Girl is BetsyX:
                                ch_b "Держи себя в руках. . ."
                        elif Girl is DoreenX:
                                ch_d "Эм. . ."
                        elif Girl is WandaX:
                                ch_w "И что это было?"
                elif ApprovalCheck(Girl, 300, "L", TabM=1):
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 90, -3,Alt=[[JeanX],50,-1])
                        $ Girl.Statup("Obed", 60, 3)
                        $ Girl.Statup("Inbt", 40, 2)
                        if Girl is RogueX:
                                ch_r "Это совсем не к месту, [Girl.Petname]!"
                        elif Girl is KittyX:
                                ch_k "Ну блин!"
                        elif Girl is EmmaX:
                                ch_e "Абсолютно неуместно!"
                                $ Girl.FaceChange("bemused", Eyes="side")
                                ch_e "-по крайней мере, на людях. . ."
                        elif Girl is LauraX:
                                ch_l "Отстань, [Girl.Petname]."
                        elif Girl is JeanX:
                                ch_j "Назад!"
                        elif Girl is StormX:
                                ch_s "Держи дистанцию."
                        elif Girl is JubesX:
                                ch_v "Назад."
                        elif Girl is GwenX:
                                ch_g "Воу, назад!"
                        elif Girl is BetsyX:
                                ch_b "Это было совершенно неуместно. . ."
                        elif Girl is DoreenX:
                                ch_d "Эй, сдай назад!"
                        elif Girl is WandaX:
                                ch_w "Слушай, что это было?"
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 90, -8,Alt=[[JeanX],50,-3])
                        $ Girl.Statup("Obed", 90, 6)
                        $ Girl.Statup("Inbt", 40, 3)
                        if Girl is RogueX:
                                ch_r "Это совсем не круто, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k "Отстань, [Girl.Petname]."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Девочка, полегче."
                                else:
                                    ch_e "Мальчик, полегче."
                        elif Girl is LauraX:
                                ch_l "Отъебись."
                        elif Girl is JeanX:
                                ch_j "Эй!"
                        elif Girl is StormX:
                                ch_s "[Player.Name]!"
                        elif Girl is JubesX:
                                ch_v "Неа."
                        elif Girl is GwenX:
                                ch_g "Какого черта?!"
                        elif Girl is BetsyX:
                                ch_b "Извини?!"
                        elif Girl is DoreenX:
                                ch_d "Воу! Держи дистанцию!"
                        elif Girl is WandaX:
                                ch_w "И что это было?"
        else:
                #If this is the first kiss
                if ApprovalCheck(Girl, 750, "L", TabM=1):
                        $ Girl.FaceChange("kiss", 2)
                        $ Girl.Statup("Love", 70, 45)
                        $ Girl.Statup("Obed", 50, 20)
                        $ Girl.Statup("Inbt", 50, 35)
                        if Girl is RogueX:
                                ch_r "Хм, это был приятный сюрприз. . ."
                                $ Girl.FaceChange("sexy",1)
                                ch_r "Возможно, нам стоит повторить, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k ". . ."
                                ch_k "Хммм, это было здорово. . ."
                                $ Girl.FaceChange("sexy",1)
                                ch_k "Дай мне знать, если захочешь повторить, [Girl.Petname]."
                        elif Girl is EmmaX:
                                ch_e ". . ."
                                ch_e "Хммм, это было очень приятно. . ."
                                $ Girl.FaceChange("sexy",1)
                                ch_e "Но мне всегда не помешает еще больше, [Girl.Petname]."
                        elif Girl is LauraX:
                                $ Girl.FaceChange("normal",1,Eyes="side")
                                ch_l ". . ."
                                $ Girl.FaceChange("sexy",Eyes="side")
                                ch_l "Хммм, это было здорово. . ."
                                $ Girl.FaceChange("sexy")
                        elif Girl is JeanX:
                                ch_j "Ох. . ."
                                $ Girl.FaceChange("sly", 1)
                        elif Girl is StormX:
                                ch_s ". . ."
                                $ Girl.FaceChange("surprised", 1)
                                ch_s "Хммм, что это было, [Girl.Petname]. . ."
                                $ Girl.FaceChange("sexy")
                                ch_s "Я бы не отказалась повторить. . ."
                        elif Girl is JubesX:
                                ch_v "Ммммм. . ."
                                $ Girl.FaceChange("surprised", 1)
                                ch_v "Ох, подожди. . . Что это было?"
                                $ Girl.FaceChange("sly")
                        elif Girl is GwenX:
                                ch_g "Ммммм. . ."
                                $ Girl.FaceChange("surprised", 1)
                                ch_g "Подожди, что это было?!"
                                $ Girl.FaceChange("sexy",1)
                                if not Player.Male:
                                    ch_g "Ты сейчас меня поцеловала?"
                                else:
                                    ch_g "Ты сейчас меня поцеловал?"
                        elif Girl is BetsyX:
                                $ Girl.FaceChange("surprised", 1)
                                ch_b ". . . "
                                $ Girl.FaceChange("sexy",1)
                                ch_b "Мы должны повторить. . ."
                        elif Girl is DoreenX:
                                $ Girl.FaceChange("surprised", 1)
                                ch_d ". . . "
                                $ Girl.FaceChange("smile",1)
                                ch_d "Ох, слушай. . . это. . . приятно. . ."
                        elif Girl is WandaX:
                                $ Girl.FaceChange("surprised", 1)
                                ch_w ". . . "
                                $ Girl.FaceChange("sly",1)
                                ch_w "Эй, что это было?"
                elif ApprovalCheck(Girl, 650, "L", TabM=1):
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Statup("Love", 80, 30)
                        $ Girl.Statup("Obed", 50, 25)
                        $ Girl.Statup("Inbt", 50, 35)
                        if Girl is RogueX:
                                ch_r "Какого-. . . что это было, [Girl.Petname]?"
                                ch_r "Хмм, не то чтобы это было совсем уж неприятно. . ."
                        elif Girl is KittyX:
                                ch_k "А?"
                                ch_k "Я, эм[Girl.like]не знаю, что и думать. . ."
                        elif Girl is EmmaX:
                                ch_e "Хмм?"
                                ch_e "Значит, мы уже созрели для этого? . ."
                        elif Girl is LauraX:
                                ch_l " ! "
                                ch_l "Я не знаю, что и думать. . ."
                        elif Girl is JeanX:
                                ch_j "Хм."
                        elif Girl is StormX:
                                ch_s "Ох!"
                        elif Girl is JubesX:
                                ch_v "Ммммм. . . подожди, что?"
                                ch_v "Что это такое было?"
                        elif Girl is GwenX:
                                ch_g "Ммммм. . ."
                                ch_g "Подожди, что это было?!"
                                if not Player.Male:
                                    ch_g "Ты сейчас меня поцеловала?"
                                else:
                                    ch_g "Ты сейчас меня поцеловал?"
                        elif Girl is BetsyX:
                                ch_b "Ох! . . "
                                ch_b "Какая. . . приятная неожиданность. . ."
                        elif Girl is DoreenX:
                                ch_d "Мммм. . ."
                                ch_d "Ох. . . это было. . . приятно."
                        elif Girl is WandaX:
                                ch_w "Мммм. . ."
                                ch_w "Эй, что это было?"
                elif ApprovalCheck(Girl, 500, "L", TabM=1):
                        $ Girl.FaceChange("surprised", 1)
                        $ Girl.Statup("Obed", 70, 30)
                        $ Girl.Statup("Inbt", 70, 35)
                        if Girl is RogueX:
                                ch_r "Эй, ты хоть когда-нибудь думаешь, что делаешь, [Girl.Petname]?"
                        elif Girl is KittyX:
                                ch_k "В чем дело, [Girl.Petname]?!"
                        elif Girl is EmmaX:
                                ch_e "Не думаю, что это уместно, [Girl.Petname]."
                        elif Girl is LauraX:
                                ch_l "О чем ты только думаешь, [Girl.Petname]?!"
                        elif Girl is JeanX:
                                ch_j "Что это было? . ."
                        elif Girl is StormX:
                                ch_s "Это неуместно."
                        elif Girl is JubesX:
                                ch_v "Это было. . . словно некое предостережение. . ."
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Подожди, ты что, сейчас меня поцеловала?"
                                else:
                                    ch_g "Подожди, ты что, сейчас меня поцеловал?"
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ты меня удивила. . ."
                                else:
                                    ch_b "Ты меня удивил. . ."
                        elif Girl is DoreenX:
                                ch_d ". . . эм. . ."
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"
                elif ApprovalCheck(Girl, 700, TabM=1):
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 60, -5,Alt=[[JeanX],50,-2])
                        $ Girl.Statup("Obed", 70, 40)
                        $ Girl.Statup("Inbt", 70, 40)
                        if Girl is RogueX:
                                ch_r "Ч- Что, черт возьми, это было?!"
                        elif Girl is KittyX:
                                ch_k "Какого черта, [Girl.Petname]?!"
                        elif Girl is EmmaX:
                                ch_e "Нас не должны увидеть за подобным занятием, [Girl.Petname]."
                        elif Girl is LauraX:
                                ch_l "Какого черта, [Girl.Petname]?!"
                        elif Girl is JeanX:
                                ch_j "Эй!"
                        elif Girl is StormX:
                                ch_s "[Player.Name]!"
                        elif Girl is JubesX:
                                ch_v "Эй!"
                        elif Girl is GwenX:
                                ch_g "Воу!"
                        elif Girl is BetsyX:
                                ch_b "Что?!"
                        elif Girl is DoreenX:
                                ch_d "Воу!"
                        elif Girl is WandaX:
                                ch_w "И что это было?"
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 60, -15,Alt=[[JeanX],50,-5])
                        $ Girl.Statup("Obed", 70, 50)
                        $ Girl.Statup("Inbt", 70, 40)
                        if Girl is RogueX:
                                ch_r "Это не круто, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k "[Girl.Like]ЧТОЗАНАХ?!"
                        elif Girl is EmmaX:
                                ch_e "Как ты посмел?"
                        elif Girl is LauraX:
                                ch_l "Отъебись."
                        elif Girl is JeanX:
                                ch_j "Что за чертовщина?!"
                        elif Girl is StormX:
                                ch_s "Держи дистанцию!"
                        elif Girl is JubesX:
                                if not Player.Male:
                                    ch_v "Отвали, курва!"
                                else:
                                    ch_v "Отвали, подонок!"
                        elif Girl is GwenX:
                                ch_g "Отойди!"
                        elif Girl is BetsyX:
                                ch_b "Назад!"
                        elif Girl is DoreenX:
                                ch_d "Предупреждай о таком!"
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"

        $ Girl.Kissed += 1
        $ Girl.Addict -= 1
        $ Girl.Addictionrate += 1
        $ Girl.Addictionrate = 3 if Girl.Addictionrate < 3 else Girl.Addictionrate

        if Girl.Taboo and Girl is EmmaX:
                    if "three" not in EmmaX.History:
                        if not AloneCheck(EmmaX):
                                # if there are other girls in the room. . .
                                call Emma_ThreeCheck
#                                        $ Girl.FaceChange("sad")
#                                        ch_e "But we just can't."
#                                        ch_e "Not here."
        if ApprovalCheck(Girl, 650, TabM=1):
            if Girl.Love > Girl.Obed and Girl.Love > Girl.Inbt:
                    if Girl is RogueX:
                            ch_r "Хочу больше сладенького, [Girl.Petname]."
                    elif Girl is KittyX:
                            ch_k "Больше поцелуйчиков, [Girl.Petname]!"
                    elif Girl is EmmaX:
                            ch_e "Надеюсь на продолжение. . ."
                    elif Girl is LauraX:
                            ch_l "Думаю, я хочу еще."
                    elif Girl is JeanX:
                            if not Player.Male:
                                ch_j "Ты такая милая. . ."
                            else:
                                ch_j "Ты такой милый. . ."
                    elif Girl is StormX:
                            ch_s "У тебя нежные губы, [Girl.Petname]."
                    elif Girl is JubesX:
                            ch_v "Нууу, я бы не отказалась попробовать еще раз. . ."
                    elif Girl is GwenX:
                            ch_g "Лучше бы тебе продолжить. . ."
                    elif Girl is BetsyX:
                            ch_b "Надеюсь, ты не хочешь на этом останавливаться. . ."
                    elif Girl is DoreenX:
                            ch_d "Ох. Хочешь продолжить?"
                    elif Girl is WandaX:
                            ch_w "Иди ко мне. . ."
            elif Girl.Obed > Girl.Inbt:
                    if Girl is RogueX:
                            ch_r "Хочешь продолжить?"
                    elif Girl is KittyX:
                            ch_k "Я открыта для большего, если ты хочешь."
                    elif Girl is EmmaX:
                            ch_e "Я не откажусь от продолжения. . ."
                    elif Girl is LauraX:
                            ch_l "Хочешь продолжить?"
                    elif Girl is JeanX:
                            ch_j "Хочешь чего-то большего?"
                    elif Girl is StormX:
                            if not Player.Male:
                                ch_s "Это все, чего ты хотела?"
                            else:
                                ch_s "Это все, чего ты хотел?"
                    elif Girl is JubesX:
                            ch_v "Хочешь еще? . ."
                    elif Girl is GwenX:
                            ch_g "Прошу, я хочу еще. . ."
                    elif Girl is BetsyX:
                            ch_b "Я могу расчитывать на продолжение?"
                    elif Girl is DoreenX:
                            ch_d "Мы продолжим?"
                    elif Girl is WandaX:
                            ch_w "Ты хочешь продолжить?"
            else:
                    if Girl is RogueX:
                            ch_r "Лучше бы тебе продолжить, [Girl.Petname]."
                    elif Girl is KittyX:
                            ch_k "Мы должны продолжить, [Girl.Petname]."
                    elif Girl is EmmaX:
                            ch_e "Иди ко мне. . ."
                    elif Girl is LauraX:
                            ch_l "Мы должны продолжить, [Girl.Petname]."
                    elif Girl is JeanX:
                            ch_j "Что ж, это было весело. . ."
                    elif Girl is StormX:
                            ch_s "Эй. . ."
                    elif Girl is JubesX:
                            ch_v "Ну? . ."
                    elif Girl is GwenX:
                            ch_g "Неплохо. . ."
                    elif Girl is BetsyX:
                            ch_b "Ооох, замечательно."
                    elif Girl is DoreenX:
                            ch_d "Ох. Здорово."
                    elif Girl is WandaX:
                            ch_w "Ну вот, теперь мы целуемся."
            menu:
                "Продолжать целоваться?"
                "Продолжить.":
                        $ Girl.Statup("Lust", 60, 3)
                        $ Girl.Statup("Love", 90, 1)
                        $ Girl.Statup("Love", 60, 3)
                        $ Girl.Statup("Inbt", 50, 2)
                        if bg_current == "HW Party":
                                "Она отмахивается от вас и подмигивает."
                                call AnyLine(Girl,"Не сейчас. . .")
                        else:
                                call SexAct("kissing") # call expression Girl.Tag + "_SexAct" pass ("kissing")
                                call Trig_Reset(1)
                        return
                "Это лишь затравка [[не продолжать].":
                        $ Girl.FaceChange("bemused", 1)
                        $ Girl.Statup("Lust", 40, 1)
                        $ Girl.Statup("Lust", 60, 4)
                        $ Girl.Statup("Obed", 70, 2)
                        $ Girl.Statup("Inbt", 50, 2)
                        if Girl is RogueX:
                                ch_r "Однажды мы дойдем до конца, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k "Ох, нельзя так[Girl.like]мучить девушку!"
                        elif Girl is EmmaX:
                                ch_e "Дразнишь значит. . ."
                        elif Girl is LauraX:
                                ch_l "Ах, да ты издеваешься."
                        elif Girl is JeanX:
                                ch_j "Ох, ладно. . ."
                        elif Girl is StormX:
                                ch_s "Значит дразнишь меня."
                        elif Girl is JubesX:
                                ch_v "О, позже ты заплатишь за это. . ."
                        elif Girl is GwenX:
                                ch_g "Значит так. . ."
                        elif Girl is BetsyX:
                                ch_b "Печально. . ."
                        elif Girl is DoreenX:
                                ch_d "Оу, облом."
                        elif Girl is WandaX:
                                ch_w "Затравка. . ?"
                "Нет.":
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 80, -2)
                        $ Girl.Statup("Obed", 70, 3)
                        $ Girl.Statup("Inbt", 50, 1)
                        if Girl is RogueX:
                                ch_r "Если не можешь закончить, не предлагай, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k "Не динамь меня, [Girl.Petname]."
                        elif Girl is EmmaX:
                                ch_e "Я не люблю такие игры, [Girl.Petname]."
                        elif Girl is LauraX:
                                ch_l "Ах, да ты издеваешься."
                        elif Girl is JeanX:
                                ch_j "Лаааадно. . ."
                        elif Girl is StormX:
                                ch_s "Не играй с моим сердцем."
                        elif Girl is JubesX:
                                ch_v "Оу. . ."
                        elif Girl is GwenX:
                                ch_g ". . . оу."
                        elif Girl is BetsyX:
                                ch_b "Боже, это печально. . ."
                        elif Girl is DoreenX:
                                ch_d "Оу, облом."
                        elif Girl is WandaX:
                                if not Player.Male:
                                    ch_w "Подразнила и все. . ?"
                                else:
                                    ch_w "Подразнил и все. . ?"
        else:
            if Girl is RogueX:
                    ch_r "Нельза целовать девушку без спроса."
            elif Girl is KittyX:
                    ch_k "Ну[Girl.like]больше так не делай."
            elif Girl is EmmaX:
                    ch_e "Не пытайся сделать это снова."
            elif Girl is LauraX:
                    ch_l "Не дави на меня."
            elif Girl is JeanX:
                    ch_j "Держи свои желания при себе."
            elif Girl is StormX:
                    ch_s "Больше так не делай."
            elif Girl is JubesX:
                    ch_v "Нууу, сначала нужно было предупредить. . ."
            elif Girl is GwenX:
                    ch_g "Хоть предупредил бы сначала. . ."
            elif Girl is BetsyX:
                    ch_b "Не мешало бы предупредить. . ."
            elif Girl is DoreenX:
                    if not Player.Male:
                        ch_d "Знаешь, не помешало бы, чтобы ты сперва сказала: \"слушай, я сейчас тебя поцелую.\""
                    else:
                        ch_d "Знаешь, не помешало бы, чтобы ты сперва сказал: \"слушай, я сейчас тебя поцелую.\""
            elif Girl is WandaX:
                    ch_w "Предупреди меня в следующий раз. . ."
                    ch_w "Если настанет этот \"следующий раз.\""
        #end Kiss
        return


#end Kiss lips / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start hug/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Hug:
        if ApprovalCheck(Girl, 200, TabM=1):
                "Вы наклоняетесь и заключаете [Girl.Name_vin] в теплые объятия."
        else:
                $ Girl.FaceChange("angry", 1)
                "Вы наклоняетесь, широко раскинув руки, но [Girl.Name] хватает вас за плечи и оттолкает назад."
                if Girl is RogueX:
                        ch_r "Эй, что ты делаешь, [Girl.Petname]?"
                elif Girl is KittyX:
                        ch_k "В чем дело, [Girl.Petname]?"
                elif Girl is EmmaX:
                        ch_e "Что это значит, [Girl.Petname]?"
                elif Girl is LauraX:
                        ch_l "Что это было, [Girl.Petname]?"
                elif Girl is JeanX:
                        ch_j "Эй, назад."
                elif Girl is StormX:
                        ch_s "Отойди на шаг назад."
                elif Girl is JubesX:
                        ch_v "Эй, отойди. . ."
                elif Girl is GwenX:
                        ch_g "Воу, назад!"
                elif Girl is BetsyX:
                        ch_b "Тебе следует держать дистанцию!"
                elif Girl is DoreenX:
                        ch_d "Воу! . . не заходи в мое личное пространство!"
                elif Girl is WandaX:
                        ch_w "Эй, что это было?"
                return
        if Girl.SEXP >= 30:
                $ Girl.Statup("Lust", 60, 3)
                $ Girl.Statup("Love", 90, 1)
                $ Girl.Statup("Obed", 90, 3)
                $ Girl.Statup("Inbt", 90, 3)
                $ Girl.FaceChange("sexy")
                if Girl is RogueX:
                        ch_r "Хмм, ты на что-то намекаешь, [Girl.Petname]?"
                elif Girl is KittyX:
                        ch_k "Ты меня согреваешь, [Girl.Petname]."
                elif Girl is EmmaX:
                        ch_e "Хммм, что у тебя на уме, [Girl.Petname]."
                elif Girl is LauraX:
                        ch_l "Что-то во мне щелкнуло, [Girl.Petname]."
                elif Girl is JeanX:
                        ch_j "Что, ты думаешь, сейчас время для интима?"
                elif Girl is StormX:
                        ch_s "Хм, что ты имеешь в виду?"
                elif Girl is JubesX:
                        ch_v "О, что это было. . ."
                elif Girl is GwenX:
                        ch_g "О, приветик. . ."
                elif Girl is BetsyX:
                        ch_b "Ох! Ну и ну. . ."
                elif Girl is DoreenX:
                        ch_d "Ох! . ."
                elif Girl is WandaX:
                        ch_w "Эй. . ."
        elif ApprovalCheck(Girl, 600, "L", TabM=1):
                $ Girl.FaceChange("sexy")
                $ Girl.Statup("Love", 90, 1)
                $ Girl.Statup("Obed", 40, 2)
                $ Girl.Statup("Inbt", 30, 1)
                if Girl is RogueX:
                        ch_r "Хмм, я тоже рада тебя видеть, [Girl.Petname]."
                elif Girl is KittyX:
                        ch_k "Хмм, теплые обнимашки."
                elif Girl is EmmaX:
                        ch_e "Хмм, по правде говоря, мне это очень нравится. . ."
                elif Girl is LauraX:
                        ch_l "Хммммм. . ."
                elif Girl is JeanX:
                        ch_j "м, ну блин!"
                elif Girl is StormX:
                        ch_s "Хмммм."
                elif Girl is JubesX:
                        ch_v "Ох. . ."
                elif Girl is GwenX:
                        ch_g "О, приветик. . ."
                elif Girl is BetsyX:
                        ch_b "Ох! Ну хорошо?"
                elif Girl is DoreenX:
                        ch_d "Ох! . ."
                elif Girl is WandaX:
                        ch_w "Слушай, что это было?"
        elif ApprovalCheck(Girl, 450, TabM=1,Alt=[[JeanX],500]):
                $ Girl.FaceChange("surprised", 1)
                $ Girl.Statup("Love", 90, 1)
                $ Girl.Statup("Love", 70, 1)
                $ Girl.Statup("Obed", 40, 2)
                $ Girl.Statup("Inbt", 30, 1)
                if Girl is RogueX:
                        ch_r "Эм, [Girl.Petname]. В чём дело?"
                elif Girl is KittyX:
                        ch_k "Эй[Girl.like]что это значит?"
                elif Girl is EmmaX:
                        if not Player.Male:
                            ch_e "Хм? Что ты хотела?"
                        else:
                            ch_e "Хм? Что ты хотел?"
                elif Girl is LauraX:
                        ch_l "Эм, [Girl.Petname]? Что это?"
                elif Girl is JeanX:
                        ch_j "Эм, что ты делаешь?"
                elif Girl is StormX:
                        ch_s "О, здравствуй."
                elif Girl is JubesX:
                        ch_v "Привет. . ."
                elif Girl is GwenX:
                        ch_g "О, приветик. . ."
                elif Girl is BetsyX:
                        ch_b "Ох! Что ты- . . ?"
                elif Girl is DoreenX:
                        ch_d "Ох! . . эм. . . "
                elif Girl is WandaX:
                        ch_w "Слушай, что это было?"
        elif ApprovalCheck(Girl, 350, TabM=1,Alt=[[JeanX],400]):
                $ Girl.FaceChange("angry", 1)
                $ Girl.Statup("Love", 70, 1)
                $ Girl.Statup("Obed", 50, 3)
                $ Girl.Statup("Inbt", 30, 2)
                if Girl is RogueX:
                        ch_r "Я не очень хорошо тебя знаю."
                elif Girl is KittyX:
                        ch_k "Мне это не нравится. . ."
                elif Girl is EmmaX:
                        ch_e "Нас не должны увидеть. . ."
                elif Girl is LauraX:
                        ch_l "Мне неловко. . ."
                elif Girl is JeanX:
                        ch_j "Это. . . странно."
                elif Girl is StormX:
                        ch_s "Эм, отпусти меня сейчас же."
                elif Girl is JubesX:
                        ch_v "Ладно, пока все в порядке. . ."
                elif Girl is GwenX:
                        ch_g "Эм, что мы сейчас делаем. . ."
                elif Girl is BetsyX:
                        ch_b "Мне довольно некомфортно . ."
                elif Girl is DoreenX:
                        ch_d "Ох! . . Я. . . не знаю, что и думать. . ."
                elif Girl is WandaX:
                        ch_w "И что это было?"
        else:
                $ Girl.FaceChange("angry", 1)
                $ Girl.Statup("Love", 10, -1)
                $ Girl.Statup("Love", 40, -1)
                $ Girl.Statup("Obed", 20, 2)
                $ Girl.Statup("Obed", 50, 2)
                $ Girl.Statup("Inbt", 30, 2)
                if Girl is RogueX:
                        ch_r "Может хватит, [Girl.Petname]?"
                elif Girl is KittyX:
                        ch_k "Что это было, [Girl.Petname]?"
                elif Girl is EmmaX:
                        ch_e "Что это было, [Girl.Petname]?"
                elif Girl is LauraX:
                        ch_l "Эй, отвали."
                elif Girl is JeanX:
                        ch_j "Что с тобой?"
                elif Girl is StormX:
                        ch_s "Что это было?"
                elif Girl is JubesX:
                        ch_v "Нууу, сначала нужно было предупредить. . ."
                elif Girl is GwenX:
                        ch_g "Не делай так!"
                elif Girl is BetsyX:
                        ch_b "Тебе следует избегать подобных контактов в будущем. . ."
                elif Girl is DoreenX:
                        ch_d "Воу! Не делай так!"
                elif Girl is WandaX:
                        ch_w "И что это было?"
        # end hug
        return

#End Hug/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start rub shoulders / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rub_Shoulders:
        "Вы подходите к [Girl.Name_dat] сзади и начинаете нежно массировать ее плечи."
        if Girl.SEXP >= 30:
                $ Girl.FaceChange("sexy")
                $ Girl.Statup("Lust", 60, 3)
                $ Girl.Statup("Love", 90, 2)
                "Она обмякает от ваших прикосновений."
                if Girl is RogueX:
                        ch_r "Хмм, ты на что-то намекаешь, [Girl.Petname]?"
                elif Girl is KittyX:
                        ch_k "Хмм, игривое настроение, [Girl.Petname]?"
                elif Girl is EmmaX:
                        ch_e "Хмм, чем обязана такому удовольствию, [Girl.Petname]?"
                elif Girl is LauraX:
                        ch_l "Хмм, ты думаешь о том же, о чем и я, [Girl.Petname]?"
                elif Girl is JeanX:
                        ch_j "Ооох, да, продолжай. . ."
                elif Girl is StormX:
                        ch_s "Хммм. . ."
                elif Girl is JubesX:
                        ch_v "Оххх. . . эй там. . ."
                elif Girl is GwenX:
                        ch_g "Ох. . . приветик. . ."
                elif Girl is BetsyX:
                        ch_b "Ох, ну и ну. . ."
                elif Girl is DoreenX:
                        ch_d "Ох! . . Oooooooх."
                elif Girl is WandaX:
                        ch_w "Ох, это так приятно. . ."
        elif ApprovalCheck(Girl, 650, "L",Alt=[[RogueX],600]):
                $ Girl.FaceChange("sexy")
                $ Girl.Statup("Lust", 60, 1)
                $ Girl.Statup("Love", 90, 2)
                if Girl is RogueX:
                        ch_r "Хмм, так приятно, [Girl.Petname]."
                elif Girl is KittyX:
                        ch_k "Муррр, мне так хорошо, [Girl.Petname]."
                elif Girl is EmmaX:
                        ch_e "Прекрасно, [Girl.Petname]."
                elif Girl is LauraX:
                        ch_l "Хммм, приятно, [Girl.Petname]."
                elif Girl is JeanX:
                        ch_j "Эй, а это приятно. . ."
                elif Girl is StormX:
                        ch_s "Восхитительно, [Girl.Petname]."
                elif Girl is JubesX:
                        ch_v "Оххх. . . эй там. . ."
                elif Girl is GwenX:
                        ch_g "Ммм, так хорошо. . ."
                elif Girl is BetsyX:
                        ch_b "Ох, замечательно. . ."
                elif Girl is DoreenX:
                        ch_d "Ох! . . спасибо. . ."
                elif Girl is WandaX:
                        ch_w "Ох, это так приятно. . ."
        elif ApprovalCheck(Girl, 500,Alt=[[RogueX],450]):
                $ Girl.FaceChange("surprised", 1)
                $ Girl.Statup("Love", 90, 1)
                if Girl is EmmaX:
                        ch_e "Ну и ну, [Girl.Petname]."
                elif Girl is LauraX:
                        ch_l "Ох, [Girl.Petname]."
                elif Girl is StormX:
                        ch_s "Ну здравствуй, [Girl.Petname]."
                elif Girl is BetsyX:
                        ch_b "Ох! здравствуй? . ."
                else:
                        call AnyLine(Girl,"Ох, "+Girl.Petname+". Что случилось?")
        elif ApprovalCheck(Girl, 350):
                $ Girl.FaceChange("angry", 1)
                $ Girl.Statup("Love", 90, -1)
                if Girl is RogueX:
                        if Girl.Taboo:
                            ch_r "Эй, эм, полегче, у меня тут КПК, [Girl.Petname]."
                        else:
                            ch_r "Воу, не нарушай мое личное пространство."
                elif Girl is KittyX:
                        if Girl.Taboo:
                            ch_k "Эй[Girl.like]полегче, [Girl.Petname]?"
                        else:
                            ch_k "Воу, назад."
                elif Girl is EmmaX:
                        if Girl.Taboo:
                            ch_e "Мне расчертить границы, [Girl.Petname]?"
                        else:
                            ch_e "Лучше не надо. . ."
                elif Girl is LauraX:
                        if Girl.Taboo:
                            ch_l "Может отойдешь на шаг назад, [Girl.Petname]?"
                        else:
                            ch_l "Воу, назад."
                elif Girl is JeanX:
                        if Girl.Taboo:
                            ch_j "Не на людях. . ."
                        else:
                            ch_j "Эй. . ."
                elif Girl is StormX:
                        if Girl.Taboo:
                            ch_s "Только не на людях, [Girl.Petname]."
                        else:
                            if not Player.Male:
                                ch_s "Не могла бы ты прекратить?"
                            else:
                                ch_s "Не мог бы ты прекратить?"
                elif Girl is JubesX:
                        if Girl.Taboo:
                            ch_v "Не здесь, ладно, [Girl.Petname]?"
                        else:
                            ch_v "Мне это не нравится, [Girl.Petname]."
                elif Girl is GwenX:
                        if Girl.Taboo:
                            ch_g "Ты слишком близко. . . не стоит вести себя так на людях. . ."
                        else:
                            ch_g "Ты слишком близко. . ."
                elif Girl is BetsyX:
                        if Girl.Taboo:
                            ch_b "Держи себя в руках на людях. . ."
                        else:
                            ch_b "Пожалуйста, держи себя в руках. . ."
                elif Girl is DoreenX:
                        if Girl.Taboo:
                            ch_d "Воу! . . эм. . . На людях соблюдай дистанцию. . ."
                        else:
                            ch_d "Воу! . . эм. . . Соблюдай дистанцию. . ."
                elif Girl is WandaX:
                        if Girl.Taboo:
                            ch_w "Отойди. . . не видишь, что вокруг люди?"
                        else:
                            ch_w "Отойди. . ."
        else:
                    $ Girl.FaceChange("angry", 1)
                    "Она шлепает вас по рукам."
                    if Girl is RogueX:
                            ch_r "Не совсем то время и место, [Girl.Petname]?"
                    elif Girl is KittyX:
                            ch_k "Не прикасайся!"
                    elif Girl is EmmaX:
                            ch_e "Довольно."
                    elif Girl is LauraX:
                            ch_l "Никаких рук, иначе их лишишься."
                    elif Girl is JeanX:
                            ch_j "Прекращай."
                    elif Girl is StormX:
                            ch_s "Прекрати."
                    elif Girl is JubesX:
                            ch_v "Прекрати, черт возьми. . ."
                    elif Girl is GwenX:
                            ch_g "Эм, нет?"
                    elif Girl is BetsyX:
                            ch_b "Прошу, не надо. . ."
                    elif Girl is DoreenX:
                            ch_d "Воу! . . эм. . ."
                    elif Girl is WandaX:
                            ch_w "Прекрати. . ."
        $ Girl.Statup("Obed", 30, 3)
        $ Girl.Statup("Inbt", 30, 2)
        return
        #End "Rub shoulders"

#end Rub Shoulders / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Pinch Ass / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Pinch_Ass:
        $ Girl.FaceChange("surprised", 1)
        if Girl.SEXP < 5 or not ApprovalCheck(Girl, 600, TabM=1):
                "Вы подходите к [Girl.Name_dat] сзади и быстро щипаете ее за задницу."
                $ Girl.FaceChange("angry")
                $ Girl.Statup("Love", 90, -4)
                $ Girl.Statup("Love", 60, -4)
                "Она резко щлепает вас по руке и сразу же оборачивается."
                if Girl is RogueX:
                        ch_r "Эй, что ты делаешь, [Girl.Petname]?"
                elif Girl is KittyX:
                        ch_k "Эй! Больно!"
                elif Girl is EmmaX:
                        if not Player.Male:
                            ch_e "Девочка, полегче!"
                        else:
                            ch_e "Мальчик, полегче!"
                elif Girl is LauraX:
                        ch_l "О чем ты только думаешь?"
                elif Girl is JeanX:
                        ch_j "Эй!"
                elif Girl is StormX:
                        ch_s "Прошу прощения?!"
                elif Girl is JubesX:
                        ch_v "Эй!"
                elif Girl is GwenX:
                        ch_g "Ай!"
                elif Girl is BetsyX:
                        ch_b "Веди себя прилично!"
                elif Girl is DoreenX:
                        ch_d "Иу! . . Эй!"
                elif Girl is WandaX:
                        ch_w "Эй, что это было?"
                return
        if Girl.SEXP >= 30:
                $ Girl.Statup("Lust", 60, 3)
                $ Girl.Statup("Love", 90, 1)
                $ Girl.Statup("Obed", 60, 2)
                $ Girl.Statup("Obed", 90, 1)
                $ Girl.Statup("Inbt", 50, 3)
                $ Girl.FaceChange("sexy")
                if Girl is RogueX:
                        ch_r "Ох! Ты на что-то намекаешь, да, [Girl.Petname]?"
                elif Girl is KittyX:
                        ch_k "Мурррр, Китти нравится."
                elif Girl is EmmaX:
                        ch_e "Ммм, на что-то намекаешь?"
                elif Girl is LauraX:
                        ch_l "Ооох! Что-то не так?"
                elif Girl is JeanX:
                        ch_j "Оох!"
                elif Girl is StormX:
                        ch_s "Ох!"
                elif Girl is JubesX:
                        ch_v "Ооох!"
                elif Girl is GwenX:
                        ch_g "Иу! Ох, привет. . ."
                elif Girl is BetsyX:
                        ch_b "Ооох! Ну и ну. . ."
                elif Girl is DoreenX:
                        ch_d "Иу! . . эм. . ."
                elif Girl is WandaX:
                        ch_w "Эй, что это было?"
        elif ApprovalCheck(Girl, 800, "L", TabM=1):
                $ Girl.FaceChange("sexy")
                $ Girl.Statup("Love", 90, 1)
                $ Girl.Statup("Obed", 60, 2)
                $ Girl.Statup("Obed", 90, 1)
                $ Girl.Statup("Inbt", 50, 2)
                if Girl is RogueX:
                        ch_r "Хмм, я тоже рада тебя видеть, [Girl.Petname]."
                elif Girl is KittyX:
                        ch_k "Мммм, [Girl.Petname]."
                elif Girl is EmmaX:
                        ch_e "Ооох!"
                elif Girl is LauraX:
                        ch_l "Тебе понравилось, [Girl.Petname]?"
                elif Girl is JeanX:
                        ch_j "Ох. . . эм, ого."
                elif Girl is StormX:
                        ch_s "Здравствуй. . ."
                elif Girl is JubesX:
                        ch_v "Ооо. . . привет. . ."
                elif Girl is GwenX:
                        ch_g "Иу!"
                elif Girl is BetsyX:
                        ch_b "Ооох! Здравствуй. . ."
                elif Girl is DoreenX:
                        ch_d "Иу! . ."
                elif Girl is WandaX:
                        ch_w "И что это было?"
        elif ApprovalCheck(Girl, 900, TabM=1):
                $ Girl.FaceChange("surprised")
                $ Girl.Statup("Love", 90, 1)
                $ Girl.Statup("Obed", 60, 3)
                $ Girl.Statup("Obed", 90, 2)
                $ Girl.Statup("Inbt", 50, 2)
                if Girl is RogueX:
                        ch_r "Оох! Что случилось?"
                elif Girl is KittyX:
                        ch_k "Оох! Эй!"
                elif Girl is EmmaX:
                        ch_e "Ммм, осторожней."
                elif Girl is LauraX:
                        ch_l "Какого-?!"
                elif Girl is JeanX:
                        ch_j "В чем дело?"
                elif Girl is StormX:
                        ch_s "Что это было?"
                elif Girl is JubesX:
                        if not Player.Male:
                            ch_v "Что ты задумала?"
                        else:
                            ch_v "Что ты задумал?"
                elif Girl is GwenX:
                        ch_g "Эй! . ."
                elif Girl is BetsyX:
                        ch_b "Оооох! Ну хорошо? . ."
                elif Girl is DoreenX:
                        ch_d "Иу! . . эм. . . что?"
                elif Girl is WandaX:
                        ch_w "И что это было?"
        elif ApprovalCheck(Girl, 800, TabM=1):
                $ Girl.FaceChange("angry")
                $ Girl.Statup("Love", 60, -3)
                $ Girl.Statup("Love", 90, -1)
                $ Girl.Statup("Obed", 60, 4)
                $ Girl.Statup("Obed", 90, 3)
                $ Girl.Statup("Inbt", 50, 2)
                if Girl is RogueX:
                        ch_r "Эй, это не прикольно."
                elif Girl is KittyX:
                        ch_k "Ну блин!"
                elif Girl is EmmaX:
                        if not Player.Male:
                            ch_e "Ты не должна делать подобное на людях."
                        else:
                            ch_e "Ты не должен делать подобное на людях."
                elif Girl is LauraX:
                        ch_l "Эй!"
                elif Girl is JeanX:
                        ch_j "Что с тобой случилось?"
                elif Girl is StormX:
                        ch_s "Держи дистанцию."
                elif Girl is JubesX:
                        ch_v "Назад."
                elif Girl is GwenX:
                        ch_g "Эй ты!"
                elif Girl is BetsyX:
                        ch_b "Оооох! . ."
                elif Girl is DoreenX:
                        ch_d "Иу! . . Эй!"
                elif Girl is WandaX:
                        ch_w "Эй, что это было?"
        else:
                $ Girl.FaceChange("angry")
                $ Girl.Statup("Love", 60, -3)
                $ Girl.Statup("Love", 90, -3)
                $ Girl.Statup("Obed", 60, 5)
                $ Girl.Statup("Obed", 90, 4)
                $ Girl.Statup("Inbt", 50, 3)
                if Girl is RogueX:
                        ch_r "Ай! Перестань."
                elif Girl is KittyX:
                        ch_k "Ай! Больно!"
                elif Girl is EmmaX:
                        ch_e "Ты хочешь, чтобы я сломала тебе пальцы?"
                elif Girl is LauraX:
                        ch_l "Ауч! Что за нахер?!"
                elif Girl is JeanX:
                        ch_j "Что за хрень?"
                elif Girl is StormX:
                        ch_s "[Player.Name]!"
                elif Girl is JubesX:
                        ch_v "Отъебись!"
                elif Girl is GwenX:
                        ch_g "Ой, отвали!"
                elif Girl is BetsyX:
                        ch_b "Никогда больше не делай так."
                elif Girl is DoreenX:
                        ch_d "Воу!"
                elif Girl is WandaX:
                        ch_w "Эй, что это было?"
        return
        #End pinch her ass


#end Pinch Ass / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Flip Skirt / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Flip_Skirt:
        $ Girl.FaceChange("surprised", 1)
        $ Girl.Upskirt = 1
        pause 1
        $ Girl.Upskirt = 0
        "Вы подкрадываетесь незаметно к [Girl.Name_dat] сзади и быстро задираете ее юбку!"
        $ Girl.Upskirt = 0
        if Girl.Panties and not Girl.Taboo:
                #if this is in private and she's wearing panties
                if ApprovalCheck(Girl, 750, "L", TabM=2):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                ch_r "Ох, шалунишка, [Girl.Petname]!"
                                if not Player.Male:
                                    ch_r "Ты могла бы просто попросить, знаешь ли. . ."
                                else:
                                    ch_r "Ты мог бы просто попросить, знаешь ли. . ."
                        elif Girl is KittyX:
                                ch_k "Как мило!"
                                if not Player.Male:
                                    ch_k "Ты не могла просто[Girl.like]попросить? . ."
                                else:
                                    ch_k "Ты не мог просто[Girl.like]попросить? . ."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Нахальная девчонка. . ."
                                    ch_e "Могла бы просто попросить."
                                else:
                                    ch_e "Нахал. . ."
                                    ch_e "Мог бы просто попросить."
                        elif Girl is LauraX:
                                ch_l "Эй!"
                                if not Player.Male:
                                    ch_l "Ты хотела увидеть мои трусики?"
                                else:
                                    ch_l "Ты хотел увидеть мои трусики?"
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Ты могла бы попросить."
                                else:
                                    ch_j "Ты мог бы попросить."
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "А ты дерзкая."
                                else:
                                    ch_s "А ты дерзкий."
                        elif Girl is JubesX:
                                ch_v "Хех, эй ты!"
                        elif Girl is GwenX:
                                ch_g "Какого-! Ха. . ."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ох! А ты дерзкая. . . Могла бы сначала спросить."
                                else:
                                    ch_b "Ох! А ты дерзкий. . . Мог бы сначала спросить."
                        elif Girl is DoreenX:
                                ch_d "Ох! . . тебе стоило сначала спросить!"
                        elif Girl is WandaX:
                                ch_w "И что это было?"
                        $ Girl.Statup("Love", 90, 3)
                elif ApprovalCheck(Girl, 650, "L", TabM=2):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                ch_r "Шалунишка, [Girl.Petname]!"
                        elif Girl is KittyX:
                                ch_k "Очень мило, [Girl.Petname]."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Нахальная девчонка."
                                else:
                                    ch_e "Нахал."
                        elif Girl is LauraX:
                                ch_l "В чем дело, [Girl.Petname]?"
                        elif Girl is JeanX:
                                ch_j "Что?"
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "А ты дерзкая."
                                else:
                                    ch_s "А ты дерзкий."
                        elif Girl is JubesX:
                                ch_v "Хех, эй ты!"
                        elif Girl is GwenX:
                                ch_g "О, привет. . ."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ох! А ты дерзкая. . ."
                                else:
                                    ch_b "Ох! А ты дерзкий. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох! . ."
                        elif Girl is WandaX:
                                ch_w "И что это было?"
                elif ApprovalCheck(Girl, 300, "I", TabM=1):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is KittyX:
                                ch_k "В чем дело?"
                        else:
                                call AnyLine(Girl,"Слушай, "+Girl.Petname+", ты когда-нибудь вообще думаешь, что делаешь?")
                elif ApprovalCheck(Girl, 300, TabM=1) or Girl is LauraX:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 90, -3)
                        $ Girl.Statup("Obed", 80, 1)
                        if Girl is EmmaX:
                                ch_e "Это абсолютно неуместно, [Girl.Petname]."
                        elif Girl is LauraX:
                                ch_l "А?"
                        elif Girl is StormX:
                                ch_s "Какое неподобающее поведение."
                        elif Girl is BetsyX:
                                ch_b "Какая наглость!"
                        else:
                                call AnyLine(Girl,"Это совсем не прикольно, "+Girl.Petname+".")
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 90, -5)
                        $ Girl.Statup("Obed", 80, 2)
                        if Girl is RogueX:
                                ch_r "Какого хрена, [Girl.Petname]!"
                                ch_r "Так не обращаются с дамами!"
                        elif Girl is KittyX:
                                ch_k "Какого хрена?"
                        elif Girl is EmmaX:
                                ch_e "Это абсолютно неуместно!"
                                ch_e "Похоже, мне придется повлиять на твое будущее в этом институте."
                        elif Girl is LauraX:
                                ch_l "ЭЙ!"
                        elif Girl is JeanX:
                                ch_j "Какого черта?!"
                        elif Girl is StormX:
                                ch_s "[Player.Name]!"
                        elif Girl is JubesX:
                                ch_v "-какого черта?"
                        elif Girl is GwenX:
                                ch_g "Воу, какого черта?!. . ."
                        elif Girl is BetsyX:
                                ch_b "Извини?!"
                        elif Girl is DoreenX:
                                ch_d "Эй! . . тебе стоило сначала спросить!"
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"
                $ Girl.Statup("Obed", 80, 5)
                $ Girl.Statup("Inbt", 30, 2)
                $ Girl.Statup("Inbt", 80, 3)
                $ Girl.SeenPanties = 1
        #end in private and she's wearing panties

        elif Girl.Panties:
                #panties on, but in public
                if ApprovalCheck(Girl, 750, "L") and ApprovalCheck(Girl, 1300, TabM=2):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                ch_r "Ох, шалунишка, [Girl.Petname]!"
                                if not Player.Male:
                                    ch_r "Ты могла бы просто попросить, знаешь ли. . ."
                                else:
                                    ch_r "Ты мог бы просто попросить, знаешь ли. . ."
                        elif Girl is KittyX:
                                ch_k "Как мило!"
                                if not Player.Male:
                                    ch_k "Ты не могла просто[Girl.like]попросить? . ."
                                else:
                                    ch_k "Ты не мог просто[Girl.like]попросить? . ."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Нахальная девчонка. . ."
                                    ch_e "Могла бы просто попросить."
                                else:
                                    ch_e "Нахал. . ."
                                    ch_e "Мог бы просто попросить."
                        elif Girl is LauraX:
                                ch_l "Эй!"
                                if not Player.Male:
                                    ch_l "Ты хотела увидеть мои трусики?"
                                else:
                                    ch_l "Ты хотел увидеть мои трусики?"
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Ты могла бы попросить."
                                else:
                                    ch_j "Ты мог бы попросить."
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "А ты дерзкая."
                                else:
                                    ch_s "А ты дерзкий."
                        elif Girl is JubesX:
                                ch_v "Хех, эй ты!"
                        elif Girl is GwenX:
                                ch_g "Какого-! Ха. . ."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ох! А ты дерзкая. . . Могла бы сначала спросить."
                                else:
                                    ch_b "Ох! А ты дерзкий. . . Мог бы сначала спросить."
                        elif Girl is DoreenX:
                                ch_d "Ох! . . тебе стоило сначала спросить!"
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"
                        $ Girl.Statup("Love", 90, 3)
                elif ApprovalCheck(Girl, 600, "L") and ApprovalCheck(Girl, 1200, TabM=2):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "[Girl.Petname]! Предупредила бы!"
                                else:
                                    ch_r "[Girl.Petname]! Предупредил бы!"
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "[Girl.Petname]! Могла хотя бы предупредить."
                                else:
                                    ch_k "[Girl.Petname]! Мог хотя бы предупредить."
                        elif Girl is EmmaX:
                                ch_e "[Girl.Petname]!"
                                ch_e "Ох, не смотри на меня так."
                        elif Girl is LauraX:
                                ch_l "Эй, мы вроде как на людях."
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Ты могла бы попросить."
                                else:
                                    ch_j "Ты мог бы попросить."
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "А ты дерзкая."
                                else:
                                    ch_s "А ты дерзкий."
                        elif Girl is JubesX:
                                ch_v "Хех, ну не здесь же!"
                        elif Girl is GwenX:
                                ch_g "Воу, не здесь. . ."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ох! Нахальная девица. . ."
                                else:
                                    ch_b "Ох! Нахал. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох! . ."
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"
                elif ApprovalCheck(Girl, 600, "L"):
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 90, -3)
                        $ Girl.Statup("Obed", 80, 3)
                        if Girl is RogueX:
                                ch_r "[Girl.Petname]! Сейчас не время и не место!"
                        elif Girl is KittyX:
                                ch_k "[Girl.Petname]! Не на людях!"
                        elif Girl is EmmaX:
                                ch_e "[Girl.Petname]! Мне нужно поддерживать свою  репутацию."
                        elif Girl is LauraX:
                                ch_l "Эй, полегче."
                        elif Girl is JeanX:
                                ch_j "Прекращай."
                        elif Girl is StormX:
                                ch_s "Что ты делаешь?"
                        elif Girl is JubesX:
                                ch_v "-что за нах?"
                        elif Girl is GwenX:
                                ch_g "Какого черта?!"
                        elif Girl is BetsyX:
                                ch_b "Какая наглость!"
                        elif Girl is DoreenX:
                                ch_d "Воу!"
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"
                elif ApprovalCheck(Girl, 800, TabM=2):
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 90, -5)
                        $ Girl.Statup("Obed", 80, 2)
                        if Girl is EmmaX:
                                ch_e "Ты в своем уме, [Girl.Petname]?"
                        elif Girl is LauraX:
                                ch_l "Эй!"
                        elif Girl is StormX:
                                ch_s "Что это было?"
                        else:
                                call AnyLine(Girl,"Какого-! "+Girl.Petname+"!")
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 90, -10)
                        $ Girl.Statup("Obed", 80, 2)
                        $ Girl.Statup("Inbt", 80, 1)
                        if Girl is EmmaX:
                                ch_e "Ты в своем уме, [Girl.Petname]?"
                        elif Girl is LauraX:
                                ch_l "Блин!"
                        elif Girl is StormX:
                                ch_s ". . ."
                        else:
                                call AnyLine(Girl,"Какого хрена, "+Girl.Petname+"?!")
                        call AnyLine(Girl,"Зачем тебе вообще делать подобное на людях?")
                $ Girl.Statup("Obed", 80, 7)
                $ Girl.Statup("Inbt", 30, 3)
                $ Girl.Statup("Inbt", 80, 3)
                $ Girl.SeenPanties = 1
        #end panties on, but in public

        elif not Girl.Taboo:
                #no panties, in private
                if ApprovalCheck(Girl, 850, "L"):
                        if Girl is RogueX:
                                ch_r "Ох, шалунишка, [Girl.Petname]!"
                                if not Player.Male:
                                    ch_r "Ты могла бы просто попросить, знаешь ли. . ."
                                else:
                                    ch_r "Ты мог бы просто попросить, знаешь ли. . ."
                        elif Girl is KittyX:
                                ch_k "Как мило!"
                                if not Player.Male:
                                    ch_k "Ты не могла просто[Girl.like]попросить? . ."
                                else:
                                    ch_k "Ты не мог просто[Girl.like]попросить? . ."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Какая нахальная девица. . ."
                                    ch_e "Могла бы просто попросить."
                                else:
                                    ch_e "Нахал. . ."
                                    ch_e "Мог бы просто попросить."
                        elif Girl is LauraX:
                                ch_l "Эй!"
                                ch_l "Понравилось увиденное?"
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Подловила."
                                else:
                                    ch_j "Подловил."
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "А ты дерзкая."
                                else:
                                    ch_s "А ты дерзкий."
                        elif Girl is JubesX:
                                ch_v "Хех, эй ты!"
                        elif Girl is GwenX:
                                ch_g "Понравилось увиденное? . ."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ох! А ты дерзкая. . . тебе стоило сначала спросить."
                                else:
                                    ch_b "Ох! А ты дерзкий. . . тебе стоило сначала спросить."
                        elif Girl is DoreenX:
                                ch_d "Ох! . . тебе стоило сначала спросить!"
                        elif Girl is WandaX:
                                ch_w "И что это было?"
                elif ApprovalCheck(Girl, 700, "L"):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "[Girl.Petname]! Предупредила бы!"
                                else:
                                    ch_r "[Girl.Petname]! Предупредил бы!"
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "[Girl.Petname]! Могла хотя бы предупредить."
                                else:
                                    ch_k "[Girl.Petname]! Мог хотя бы предупредить."
                        elif Girl is EmmaX:
                                ch_e "[Girl.Petname]!"
                                ch_e "Ох, не смотри на меня так."
                        elif Girl is LauraX:
                                ch_l "Эй, в чем дело?"
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Подловила."
                                else:
                                    ch_j "Подловил."
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "А ты дерзкая."
                                else:
                                    ch_s "А ты дерзкий."
                        elif Girl is JubesX:
                                ch_v "Хех, эй ты!"
                        elif Girl is GwenX:
                                ch_g "Какого-! Ха. . ."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ох! А ты дерзкая. . ."
                                else:
                                    ch_b "Ох! А ты дерзкий. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох! . ."
                        elif Girl is WandaX:
                                ch_w "И что это было?"
                elif ApprovalCheck(Girl, 600, "L"):
                        $ Girl.FaceChange("bemused", 1)
                        $ Girl.Statup("Love", 90, -3)
                        $ Girl.Statup("Obed", 80, 3)
                        if Girl is RogueX:
                                ch_r "Какого-?! [Girl.Petname]? . . Обычно, я таким не занимаюсь. . ."
                        elif Girl is KittyX:
                                ch_k "Какого-?! [Girl.Petname]? . ."
                                ch_k "Обычно, я таким не занимаюсь. . ."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Какого-?! [Girl.Petname]?"
                                    ch_e "Ты ожидала чего-то другого?"
                                else:
                                    ch_e "Какого-?! [Girl.Petname]?"
                                    ch_e "Ты ожидал чего-то другого?"
                        elif Girl is LauraX:
                                ch_l "Какого-?! [Girl.Petname]?"
                        elif Girl is JeanX:
                                ch_j "Эй!"
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "Удивлена?"
                                else:
                                    ch_s "Удивлен?"
                        elif Girl is JubesX:
                                if not Player.Male:
                                    ch_v "Эм, удивлена?"
                                else:
                                    ch_v "Эм, удивлен?"
                        elif Girl is GwenX:
                                ch_g "Какого-! Ха. . ."
                        elif Girl is BetsyX:
                                ch_b "Какая наглость!"
                        elif Girl is DoreenX:
                                ch_d "Воу! . . тебе стоило сначала спросить!"
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"
                elif ApprovalCheck(Girl, 500):
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 90, -5)
                        $ Girl.Statup("Obed", 80, 2)
                        if Girl is EmmaX:
                                ch_e "Ты в своем уме, [Girl.Petname]?"
                        elif Girl is LauraX:
                                ch_l "Эй!"
                        elif Girl is StormX:
                                ch_s ". . ."
                        else:
                                call AnyLine(Girl,"Какого-! "+Girl.Petname+"!")
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 90, -10)
                        $ Girl.Statup("Obed", 80, 2)
                        $ Girl.Statup("Inbt", 80, 1)
                        if Girl is EmmaX:
                                ch_e "Ты в своем уме, [Girl.Petname]?"
                                ch_e "Даже если бы на мне были трусики. . ."
                        elif Girl is LauraX:
                                ch_l "Блин!"
                        elif Girl is JeanX:
                                ch_j "Эй! Это слишком."
                        elif Girl is StormX:
                                ch_s "Это совсем неуместно."
                        elif Girl is BetsyX:
                                ch_b "Обычно я не занимаюсь подобным. . ."
                        elif Girl is DoreenX:
                                if not Player.Male:
                                    ch_d "Воу! . . эм. . . ты ничего не видела."
                                else:
                                    ch_d "Воу! . . эм. . . ты ничего не видел."
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"
                        else:
                                call AnyLine(Girl,"Какого хрена, "+Girl.Petname+"?!")
                                call AnyLine(Girl,"Я- Обычно я таким не занимаюсь, знаешь ли. . .")
                $ Girl.Statup("Obed", 80, 7)
                $ Girl.Statup("Inbt", 30, 3)
                $ Girl.Statup("Inbt", 80, 4)
                call Girl_First_Bottomless(Girl)

        #end no panties, in private
        else:
                #no panties, in public
                if ApprovalCheck(Girl, 850, "L") and ApprovalCheck(Girl, 1500):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                ch_r "Ох, шалунишка, [Girl.Petname]!"
                                if not Player.Male:
                                    ch_r "Ты могла бы просто попросить, знаешь ли. . ."
                                else:
                                    ch_r "Ты мог бы просто попросить, знаешь ли. . ."
                        elif Girl is KittyX:
                                ch_k "Как мило!"
                                if not Player.Male:
                                    ch_k "Ты не могла просто[Girl.like]попросить? . ."
                                else:
                                    ch_k "Ты не мог просто[Girl.like]попросить? . ."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Какая нахальная девица. . ."
                                    ch_e "Могла бы просто попросить."
                                else:
                                    ch_e "Нахал. . ."
                                    ch_e "Мог бы просто попросить."
                        elif Girl is LauraX:
                                ch_l "Эй!"
                                ch_l "Понравилось увиденное?"
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Подловила."
                                else:
                                    ch_j "Подловил."
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "А ты дерзкая."
                                else:
                                    ch_s "А ты дерзкий."
                        elif Girl is JubesX:
                                ch_v "Хех, эй ты!"
                        elif Girl is GwenX:
                                ch_g "Понравилось увиденное? . ."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ох! А ты дерзкая. . . тебе стоило сначала спросить."
                                else:
                                    ch_b "Ох! А ты дерзкий. . . тебе стоило сначала спросить."
                        elif Girl is DoreenX:
                                ch_d "Ох! . . тебе стоило сначала спросить!"
                        elif Girl is WandaX:
                                ch_w "И что это было?"
                elif ApprovalCheck(Girl, 700, "L") and ApprovalCheck(Girl, 1500):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "[Girl.Petname]! Предупредила бы!"
                                else:
                                    ch_r "[Girl.Petname]! Предупредил бы!"
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "[Girl.Petname]! Могла хотя бы предупредить."
                                else:
                                    ch_k "[Girl.Petname]! Мог хотя бы предупредить."
                        elif Girl is EmmaX:
                                ch_e "[Girl.Petname]!"
                                ch_e "Ох, не смотри на меня так."
                        elif Girl is LauraX:
                                ch_l "Эй, в чем дело?"
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Подловила."
                                else:
                                    ch_j "Подловил."
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "А ты дерзкая."
                                else:
                                    ch_s "А ты дерзкий."
                        elif Girl is JubesX:
                                ch_v "Хех, эй ты!"
                        elif Girl is GwenX:
                                ch_g "Какого-! Ха. . ."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Ох! А ты дерзкая. . ."
                                else:
                                    ch_b "Ох! А ты дерзкий. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох! . ."
                        elif Girl is WandaX:
                                ch_w "И что это было?"
                elif ApprovalCheck(Girl, 700):
                        $ Girl.FaceChange("bemused", 1)
                        $ Girl.Statup("Love", 90, -3)
                        $ Girl.Statup("Obed", 80, 3)
                        if Girl is RogueX:
                                ch_r "[Girl.Petname]! Сейчас не время и не место!"
                        elif Girl is KittyX:
                                ch_k "[Girl.Petname]! Не на людях!"
                        elif Girl is EmmaX:
                                ch_e "[Girl.Petname]! Мне нужно поддерживать свою  репутацию."
                        elif Girl is LauraX:
                                ch_l "Эй, полегче."
                        elif Girl is JeanX:
                                ch_j "Эй! Эм. . . не здесь, ладно?"
                        elif Girl is StormX:
                                ch_s "Лучше не на людях."
                        elif Girl is JubesX:
                                ch_v "Может не здесь?"
                        elif Girl is GwenX:
                                ch_g "Воу. . . давай не здесь. . ."
                        elif Girl is BetsyX:
                                ch_b "Сомневаюсь, что это подходящее место для подобного. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох! . . мы в неподходящем месте!"
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"
                elif ApprovalCheck(Girl, 1000):
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 90, -5)
                        $ Girl.Statup("Obed", 80, 2)
                        if Girl is EmmaX:
                                ch_e "Ты в своем уме, [Girl.Petname]?"
                        elif Girl is LauraX:
                                ch_l "Эй!"
                        elif Girl is JeanX:
                                ch_j "Эй! Я бы не хотела заниматься подобным. . . здесь."
                        elif Girl is StormX:
                                ch_s "Не здесь."
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"
                        else:
                                call AnyLine(Girl,"Какого-! "+Girl.Petname+"!")
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Statup("Love", 90, -10)
                        $ Girl.Statup("Obed", 80, 2)
                        $ Girl.Statup("Inbt", 80, 1)
                        if Girl is EmmaX:
                                ch_e "Ты в своем уме, [Girl.Petname]?"
                                ch_e "Даже если бы на мне были трусики. . ."
                        elif Girl is LauraX:
                                ch_l "Блин!"
                        elif Girl is JeanX:
                                ch_j "Эй! Эм. . ."
                        elif Girl is StormX:
                                ch_s "Лучше бы тебе этого не делать. . ."
                        elif Girl is BetsyX:
                                ch_b ". . . Это неподходящее место для подобного."
                        elif Girl is DoreenX:
                                if not Player.Male:
                                    ch_d "Воу! . . эм. . . ты ничего не видела."
                                else:
                                    ch_d "Воу! . . эм. . . ты ничего не видел."
                        elif Girl is WandaX:
                                ch_w "Эй, что это было?"
                        else:
                                call AnyLine(Girl,"Какого хрена, "+Girl.Petname+"?!")
                                call AnyLine (Girl, "Я- Обычно я таким не занимаюсь, знаешь ли. . .")
                $ Girl.Statup("Obed", 80, 7)
                $ Girl.Statup("Inbt", 30, 4)
                $ Girl.Statup("Inbt", 80, 4)
                call Girl_First_Bottomless(Girl)
        #end no panties, in public
        $ Girl.Statup("Lust", 60, 1)
        if "exhibitionist" in Girl.Traits:
            $ Girl.Statup("Lust", 200, 4)
        return
        #End Flip her Skirt

#end Flip Skirt / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Grab_Tit / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Grab_Tit:
        $ Girl.FaceChange("surprised", 1)
        "Вы подходите к [Girl.Name_dat] и быстро жамкаете ее грудь."
        if Girl.SEXP < 5 or not ApprovalCheck(Girl, 600, TabM=2):
                "Вы подходите к [Girl.Name_dat] и быстро жамкаете ее грудь."
                $ Girl.FaceChange("angry")
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Love", 60, -5)
                call Punch
                if Girl is RogueX:
                        "Она шлепает вас сначала по руке, а затем по лицу."
                        ch_r "Какого хрена, [Girl.Petname]?"
                elif Girl is KittyX:
                        "Она шлепает вас сначала по руке, а затем бьет локтем под ребра."
                        ch_k "[Girl.Like]ЧТОЗАНАХ, [Girl.Petname]?"
                elif Girl is EmmaX:
                        "Она шлепает вас сначала по руке, а затем бьет локтем под ребра."
                        ch_e "Ты должен научиться сопротивляться искушениям, [Girl.Petname]."
                elif Girl is LauraX:
                        "Она переворачивает вас на спину."
                        ch_l "Что за хуйня?!"
                elif Girl is JeanX:
                        $ JeanX.Eyes = "psychic"
                        "Вы чувствуете, как что-то стукает вас по затылку."
                        ch_j "Руки!"
                        $ JeanX.Eyes = "squint"
                elif Girl is StormX:
                        "Она переворачивает вас на спину."
                        ch_s "Я могу тебе помочь?"
                elif Girl is JubesX:
                        $ JubesX.ArmPose = 1
                        show Fireworks onlayer black as Fire1:
                                pos (JubesX.SpriteLoc+160,270)
                        show Fireworks onlayer black as Fire2:
                                pos (JubesX.SpriteLoc+160,270)
                        ch_v "Назад. . ."
                elif Girl is GwenX:
                        "Она переворачивает вас на спину."
                        ch_g "Сначала тебе стоило спросить. . ."
                elif Girl is BetsyX:
                        "Она переворачивает вас на спину."
                        ch_b "Сперва -стоит- спрашивать. . ."
                elif Girl is DoreenX:
                        "Она шлепает вас по руке и пинает по голени."
                        ch_d "Какого черта?!"
                elif Girl is WandaX:
                        ch_w "Эй, что это было?"
                return
        if Girl.SEXP >= 40:
                $ Girl.Statup("Lust", 60, 5)
                $ Girl.Statup("Love", 90, 2)
                $ Girl.FaceChange("sexy")
                if Girl is RogueX:
                        ch_r "Ох! Ты на что-то намекаешь, да, [Girl.Petname]?"
                elif Girl is KittyX:
                        ch_k "Хмм, я рада, что сейчас не могу воспользоваться своей способностью, [Girl.Petname]."
                elif Girl is EmmaX:
                        ch_e "Мне очень даже приятно, [Girl.Petname]. . ."
                elif Girl is LauraX:
                        ch_l "Хмм, так приятно."
                elif Girl is JeanX:
                        ch_j "Хмм. . ."
                elif Girl is StormX:
                        ch_s "Ну здравствуй. . ."
                elif Girl is JubesX:
                        ch_v "Ох, ну привет. . ."
                elif Girl is GwenX:
                        ch_g "Я не против. . ."
                elif Girl is BetsyX:
                        ch_b "Хмммм. . ."
                elif Girl is DoreenX:
                        ch_d "Ох. . ."
                elif Girl is WandaX:
                        ch_w "Слушай, что это было?"
                $ Count = 10
        elif ApprovalCheck(Girl, 800, "L", TabM=1):
                $ Girl.FaceChange("sexy")
                $ Girl.Statup("Lust", 60, 2)
                $ Girl.Statup("Love", 90, 1)
                if Girl is RogueX:
                        ch_r "Хмм, прикладываешь руку к моему сердцу, [Girl.Petname]?"
                elif Girl is KittyX:
                        ch_k "Хмм, прикоснись-ка вот тут, [Girl.Petname]."
                elif Girl is EmmaX:
                        ch_e "Мммммм. . ."
                elif Girl is LauraX:
                        ch_l "Хм, тебе это нравится так же, как и мне?"
                elif Girl is JeanX:
                        ch_j "Ну привет."
                elif Girl is StormX:
                        ch_s "Ну здравствуй. . ."
                elif Girl is JubesX:
                        ch_v "Ох, ну привет. . ."
                elif Girl is GwenX:
                        ch_g "Я не против. . ."
                elif Girl is BetsyX:
                        ch_b "Это довольно. . . смело. . ."
                elif Girl is DoreenX:
                        ch_d "Ох. . ."
                elif Girl is WandaX:
                        ch_w "И что это было?"
                $ Count = 7
        elif ApprovalCheck(Girl, 1000, TabM=1):
                $ Girl.FaceChange("perplexed")
                $ Girl.Statup("Lust", 60, 1)
                if Girl is RogueX:
                        ch_r "Ох! А ты не слишком ли сильно распускаешь руки, [Girl.Petname]?"
                elif Girl is KittyX:
                        ch_k "Ты слишком спешишь, [Girl.Petname]."
                elif Girl is EmmaX:
                        ch_e "Ты слегка поспешил, [Girl.Petname]."
                elif Girl is LauraX:
                        ch_l "Это немного неуместно, [Girl.Petname]."
                elif Girl is JeanX:
                        ch_j "Эй, это немного. . ."
                elif Girl is StormX:
                        ch_s "Это ведь моя грудь. . . Хммм. . ."
                elif Girl is JubesX:
                        ch_v "Ты слишком распускаешь руки, [Girl.Petname]. . ."
                elif Girl is GwenX:
                        ch_g "Следи за руками. . ."
                elif Girl is BetsyX:
                        ch_b "-Следи- за своими руками. . ."
                elif Girl is DoreenX:
                        ch_d "Воу. . ."
                elif Girl is WandaX:
                        ch_w "Эй, что это было?"
                $ Count = 5
        elif ApprovalCheck(Girl, 800, TabM=1):
                $ Girl.FaceChange("angry")
                $ Girl.Statup("Love", 90, -3)
                $ Girl.Statup("Obed", 90, 4)
                $ Girl.Statup("Inbt", 90, 3)
                if Girl is RogueX:
                        ch_r "Кажется, у тебя что-то не на своем месте. . ."
                elif Girl is KittyX:
                        ch_k "Можешь убрать ее?"
                elif Girl is EmmaX:
                        ch_e "Ты должен немедленно ее убрать."
                elif Girl is LauraX:
                        ch_l "Ты убирешь ее или придется, все-таки, мне?"
                elif Girl is JeanX:
                        ch_j "Кхм, ты вообще собираешься ее убрать?"
                elif Girl is StormX:
                        ch_s "Это ведь моя грудь. . ."
                elif Girl is JubesX:
                        ch_v "Тебе стоит следить за руками, [Girl.Petname]. . ."
                elif Girl is GwenX:
                        ch_g "Воу, не лезь в мое личное пространство. . ."
                elif Girl is BetsyX:
                        if not Player.Male:
                            ch_b "Похоже, ты схватила меня за грудь. . ."
                        else:
                            ch_b "Похоже, ты схватил меня за грудь. . ."
                elif Girl is DoreenX:
                        ch_d "Ох. Это. . . моя грудь. . ."
                elif Girl is WandaX:
                        ch_w "Эй, что это было?"
                $ Count = 3
        else:
                $ Girl.FaceChange("angry")
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Obed", 90, 5)
                $ Girl.Statup("Inbt", 90, 3)
                if Girl is RogueX:
                        ch_r "Убери ее или потеряешь, [Girl.Petname]."
                elif Girl is KittyX:
                        ch_k "Ты хочешь потерять свою руку?"
                elif Girl is EmmaX:
                        ch_e "Ты так хочешь потерять свою руку?"
                elif Girl is LauraX:
                        $ Girl.ArmPose = 2
                        $ LauraX.Claws = 1
                        ch_l "Ты что, хочешь потерять свою руку?"
                elif Girl is JeanX:
                        ch_j "Извини?"
                elif Girl is StormX:
                        ch_s "Это ведь моя грудь. . . тебе стоит ее отпустить."
                elif Girl is JubesX:
                        $ Girl.ArmPose = 1
                        ch_v "Мне что, стоит прикупить перцовый болончик, [Girl.Petname]?"
                elif Girl is GwenX:
                        ch_g "Я не хочу ломать тебе пальцы. . ."
                elif Girl is BetsyX:
                        ch_b "Ты хочешь пострадать от последствий. . ?"
                elif Girl is DoreenX:
                        ch_d "Эй!"
                elif Girl is WandaX:
                        ch_w "Эй, что это значит?"
                $ Count = 2
        $ Girl.Statup("Obed", 70, 3)
        $ Girl.Statup("Inbt", 70, 2)
        if Girl is RogueX:
                ch_r "Эм, ты собираешься отпустить меня?"
        elif Girl is KittyX:
                if not Player.Male:
                    ch_k "Эм, ты еще не закончила?"
                else:
                    ch_k "Эм, ты еще не закончил?"
        elif Girl is EmmaX:
                ch_e "Может хватит?"
        elif Girl is LauraX:
                if not Player.Male:
                    ch_l "Ты удовлетворена?"
                else:
                    ch_l "Ты удовлетворен?"
        elif Girl is JeanX:
                ch_j "Ты все?"
        elif Girl is StormX:
                ch_s "Тебе понравилось?"
        elif Girl is JubesX:
                ch_v "И? Веселишься?"
        elif Girl is GwenX:
                ch_g "Эм. . . Что мы сейчас делаем?"
        elif Girl is BetsyX:
                ch_b "Не хочешь убрать свою руку? . ."
        elif Girl is DoreenX:
                ch_d "Ты собираешься. . . отпускать? . ."
        elif Girl is WandaX:
                ch_w "Ты  -ведь- собираешься отпускать?"
        while Count > 0:
            if Count == 6:
                    $ Girl.FaceChange("sexy", 1)
                    if Girl is RogueX:
                            ch_r "Хммм, давай продолжиим. . ."
                    elif Girl is KittyX:
                            ch_k "Ммммм, мне нравится. . ."
                    elif Girl is EmmaX:
                            ch_e "Ммммм, мне очень нравится. . ."
                    elif Girl is LauraX:
                            ch_l "Очень приятно. . ."
                    elif Girl is JeanX:
                            ch_j "Ладно, продолжай. . ."
                    elif Girl is StormX:
                            ch_s "Хммм. . . пожалуй, я хочу большего. . ."
                    elif Girl is JubesX:
                            ch_v "Продолжай. . ."
                    elif Girl is GwenX:
                            ch_g "Думаю. . . можешь продолжать. . ."
                    elif Girl is BetsyX:
                            ch_b "Я. . . пожалуй, все нормально. . ."
                    elif Girl is DoreenX:
                            ch_d "Ладно, можешь продолжать. . ."
                    elif Girl is WandaX:
                            ch_w "Думаю, можешь продолжать. . ."
                    $ Girl.Statup("Lust", 90, 2)
                    $ Girl.Statup("Inbt", 70, 1)
            elif Count == 3:
                    $ Girl.FaceChange("perplexed")
                    $ Girl.Statup("Lust", 90, 1)
                    if Girl is RogueX:
                            ch_r "Это, конечно, хорошо, [Girl.Petname], но, может быть, хватит?"
                    elif Girl is KittyX:
                            ch_k "Не то, чтобы мне было неприятно, [Girl.Petname], но, может быть, хватит?"
                    elif Girl is EmmaX:
                            ch_e "Не то чтобы мне это не нравилось, [Girl.Petname]. . ."
                    elif Girl is LauraX:
                            ch_l "Мне нравится, но, может быть, пока остановимся?"
                    elif Girl is JeanX:
                            ch_j "Ладно, пожалуй хватит. . ."
                    elif Girl is StormX:
                            ch_s "А возможно, и нет. . ."
                    elif Girl is JubesX:
                            ch_v "Эм, наверное, хватит. . ."
                    elif Girl is GwenX:
                            ch_g "Пожалуй, эм, время остановиться. . ."
                    elif Girl is BetsyX:
                            ch_b "Мне кажется, с тебя хватит. . ."
                    elif Girl is DoreenX:
                            ch_d "Пожалуй. . . пора прекращать. . ."
                    elif Girl is WandaX:
                            ch_w "Наверное, тебе стоит остановиться. . ."
            elif Count == 2:
                    $ Girl.FaceChange("angry")
                    $ Girl.Statup("Love", 90, -1)
                    if Girl is RogueX:
                            ch_r "Ладно, прекрати сейчас же."
                    elif Girl is KittyX:
                            ch_k "Ладно, дай отдохнуть."
                    elif Girl is EmmaX:
                            ch_e "Ладно, хватит. . ."
                    elif Girl is LauraX:
                            ch_l "Хорошо, достаточно."
                    elif Girl is JeanX:
                            ch_j "Может остановимся? . ."
                    elif Girl is StormX:
                            ch_s "Ладно, достаточно. . ."
                    elif Girl is JubesX:
                            $ JubesX.ArmPose = 1
                            ch_v "Ладно, прекращай, или получишь под ребра. . ."
                    elif Girl is GwenX:
                            ch_g "Ладно, время остановиться. . ."
                    elif Girl is BetsyX:
                            ch_b "Довольно. . ."
                    elif Girl is DoreenX:
                            ch_d "Ладно, наверное, хватит. . ."
                    elif Girl is WandaX:
                            ch_w "Ладно, я серьезно. . ."
            elif Count == 1:
                    $ Girl.FaceChange("angry")
                    $ Girl.Statup("Love", 90, -5)
                    if Girl is RogueX:
                            ch_r "Отвали нахер, [Girl.Petname]!"
                            call Punch
                            "Она шлепает вас сначала по руке, а затем по лицу."
                            ch_r "Какого хрена, [Girl.Petname]?"
                    elif Girl is KittyX:
                            ch_k "Назад, [Girl.Petname]!"
                            call Punch
                            "Она бьет вас локтем под ребра."
                            ch_k "ЧТОЗАНАХ, [Girl.Petname]?"
                    elif Girl is EmmaX:
                            ch_e "Пора прекращать, [Girl.Petname]."
                            call Punch
                            "Она бьет вас локтем под ребра."
                            if not Player.Male:
                                ch_e "Ты должна понимать, когда стоит остановиться. . ."
                            else:
                                ch_e "Ты должен понимать, когда стоит остановиться. . ."
                    elif Girl is LauraX:
                            ch_l "Отойди на шаг назад, [Girl.Petname]!"
                            call Punch
                            "Она резко толкает вас."
                    elif Girl is JeanX:
                            $ JeanX.Eyes = "psychic"
                            call Punch
                            "Вы чувствуете, как что-то стукает вас по затылку."
                            ch_j "Ладно, хорошо."
                            $ JeanX.Eyes = "squint"
                    elif Girl is StormX:
                            ch_s "Довольно, [Girl.Petname]."
                            call Punch
                            "Она бьет вас локтем под ребра."
                            ch_s "Все должно быть в меру. . ."
                    elif Girl is JubesX:
                            $ JubesX.ArmPose = 1
                            show Fireworks onlayer black as Fire1:
                                    pos (JubesX.SpriteLoc+160,270)
                            show Fireworks onlayer black as Fire2:
                                    pos (JubesX.SpriteLoc+160,270)
                            ch_v "Я серьезно, [Girl.Petname]. . ."
                    elif Girl is GwenX:
                            ch_g "Серьезно, время вышло!"
                            call Punch
                            "Она бьет вас локтем под ребра."
                    elif Girl is BetsyX:
                            call Punch
                            "Она толкает вас локтем в ребра."
                            ch_b "Достаточно. . ."
                    elif Girl is DoreenX:
                            call Punch
                            "Она отталкивает вас обеими руками."
                            ch_d "Прекрати. . ."
                    elif Girl is WandaX:
                            call Punch
                            "Она отталкивает вас обеими руками."
                            ch_w "Ладно, довольно!"
                    $ Count = 1
            $ Count -= 1 if Count >= 0 else 0

            if Count > 0:
                menu:
                    "Ваша рука все еще на ее груди."
                    "Немедленно отпустить":
                        if Count >= 7:
                                if Girl is RogueX:
                                        ch_r "Хех, не могу сказать, что я разочарована. . ."
                                elif Girl is KittyX:
                                        ch_k "Это было не[Girl.like]так уж и плохо. . ."
                                elif Girl is EmmaX:
                                        ch_e "Не то, чтобы я была против. . ."
                                elif Girl is LauraX:
                                        ch_l "Я не особо-то и возражала. . ."
                                elif Girl is JeanX:
                                        ch_j "Оу, как жаль. . ."
                                elif Girl is StormX:
                                        ch_s "Ах, а все было очень даже хорошо. . ."
                                elif Girl is JubesX:
                                        ch_v "Может быть, позже продолжим. . ."
                                elif Girl is GwenX:
                                        ch_g "Оу, ты уже все? . ."
                                elif Girl is BetsyX:
                                        ch_b "Должна сказать, я надеялась на большее. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох. Ладно. . ."
                                elif Girl is WandaX:
                                        ch_w "Ох, ладно."
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Inbt", 70, 1)
                        elif Count <= 4:
                                if Girl is RogueX:
                                        ch_r "Мудрый выбор."
                                elif Girl is KittyX:
                                        ch_k "Наверное, это к лучшему."
                                elif Girl is EmmaX:
                                        ch_e "Полагаю, это к лучшему."
                                elif Girl is LauraX:
                                        ch_l "Наверное, это к лучшему."
                                elif Girl is JeanX:
                                        ch_j "Ага. . ."
                                elif Girl is StormX:
                                        ch_s "Ладно, достаточно. . ."
                                elif Girl is JubesX:
                                        ch_v "Ага. . ."
                                elif Girl is GwenX:
                                        ch_g "Именно . ."
                                elif Girl is BetsyX:
                                        ch_b "Мудрое решение. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох. Ладно. . ."
                                elif Girl is WandaX:
                                        ch_w "Ох. Хорошо. . ."
                        $ Count = 0

                    "Сжать еще раз и отпустить":
                        if Count >= 7:
                                if Girl is RogueX:
                                        ch_r "Хех, не могу сказать, что я разочарована. . ."
                                elif Girl is KittyX:
                                        ch_k "Это было[Girl.like]не так уж и плохо. . ."
                                elif Girl is EmmaX:
                                        ch_e "Ммм, забавно."
                                elif Girl is LauraX:
                                        ch_l "Если честно, я бы не возражала. . ."
                                elif Girl is JeanX:
                                        ch_j "Ах, как жаль. . ."
                                elif Girl is StormX:
                                        ch_s "Хмммм. . ."
                                elif Girl is JubesX:
                                        ch_v "Тц. . ."
                                elif Girl is GwenX:
                                        ch_g "Оу, ты уже все? . ."
                                elif Girl is BetsyX:
                                        ch_b "Должна сказать, я надеялась на большее. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох. Ладно. . ."
                                elif Girl is WandaX:
                                        ch_w "Хех."
                                $ Girl.Statup("Lust", 60, 4)
                                $ Girl.Statup("Inbt", 70, 1)
                        elif Count >= 4:
                                if Girl is RogueX:
                                        ch_r "Классно, [Girl.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Любишь пошутить, [Girl.Petname]?"
                                elif Girl is EmmaX:
                                        ch_e "Забавно."
                                elif Girl is LauraX:
                                        ch_l "Хах."
                                elif Girl is JeanX:
                                        ch_j "Хммммм. . ."
                                elif Girl is StormX:
                                        ch_s "Хммм. . ."
                                elif Girl is JubesX:
                                        ch_v "Хм. . ."
                                elif Girl is GwenX:
                                        ch_g "Эм. . ."
                                elif Girl is BetsyX:
                                        ch_b "Хммм. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох. . ."
                                elif Girl is WandaX:
                                        ch_w "Хех."
                        else:
                                $ Girl.FaceChange("angry")
                                if Girl is RogueX:
                                        ch_r "Хреновый выбор."
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Дура."
                                        else:
                                            ch_k "Придурок."
                                elif Girl is EmmaX:
                                        ch_e "Тебе лучше быть осторожнее."
                                elif Girl is LauraX:
                                        if not Player.Male:
                                            ch_l "Стерва."
                                        else:
                                            ch_l "Козел."
                                elif Girl is JeanX:
                                        if not Player.Male:
                                            ch_j "-сучка. . ."
                                        else:
                                            ch_j "-Гад. . ."
                                elif Girl is StormX:
                                        ch_s "Мило. . ."
                                elif Girl is JubesX:
                                        if not Player.Male:
                                            ch_v "Юмористка блин. . ."
                                        else:
                                            ch_v "Шутник нашелся. . ."
                                elif Girl is GwenX:
                                        if not Player.Male:
                                            ch_g "Ты думала, она бибикнет? . ."
                                        else:
                                            ch_g "Ты думал, она бибикнет? . ."
                                elif Girl is BetsyX:
                                        if not Player.Male:
                                            ch_b "Я не знаю, чего ты ожидала. . ."
                                        else:
                                            ch_b "Я не знаю, чего ты ожидал. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох. Что это было? . ."
                                elif Girl is WandaX:
                                        if not Player.Male:
                                            ch_w "Ты странная."
                                        else:
                                            ch_w "Ты странный."
                        $ Girl.Statup("Obed", 70, 3)
                        $ Girl.Statup("Inbt", 70, 2)
                        $ Count = 0

                    "Немного поласкать":
                            if Girl.FondleB and ApprovalCheck(Girl, 1000, TabM=2):
                                    $ Girl.FaceChange("sexy",1)
                                    $ Girl.Eyes = "closed"
                                    $ Girl.Statup("Lust", 90, 5)
                            else:
                                    $ Girl.FaceChange("perplexed")
                                    $ Girl.Statup("Lust", 90, 2)
                                    $ Count -= 1
                            $ Girl.Statup("Obed", 70, 4)
                            $ Girl.Statup("Inbt", 70, 2)
                            if Girl is EmmaX:
                                    ch_e "Ммм. . ."
                            elif Girl is LauraX:
                                    ch_l "Ммм. . ."
                            else:
                                    call AnyLine(Girl,"Эмм. . .")

                    "Оставить руку на груди.":
                        if Count == 5:
                                $ Girl.FaceChange("perplexed")
                                $ Girl.Statup("Lust", 90, 3)
                                if Girl is RogueX:
                                        ch_r "Это немного странно."
                                else:
                                        call AnyLine(Girl,"Хм.")
                        elif Count == 2:
                                $ Girl.FaceChange("perplexed")
                                $ Girl.Statup("Lust", 90, 1)
                                if Girl is EmmaX:
                                        ch_e "Эм, [EmmaX.Petname]."
                                elif Girl is LauraX:
                                        ch_l "Мне немного неприятно."
                                else:
                                        call AnyLine(Girl,"Становится немного неприятно.")
                        $ Girl.Statup("Obed", 70, 2)
                        $ Girl.Statup("Inbt", 70, 1)

        if Girl is LauraX:
                $ LauraX.ArmPose = 1
                $ LauraX.Claws = 0
        if Girl is EmmaX and Taboo and "taboo" not in EmmaX.History:
                ch_e "[EmmaX.Petname], на людях проявляй ко мне хоть немного уважения."
        elif bg_current == "HW Party":
                "Она отмахивается от вас и подмигивает."
                call AnyLine(Girl,"Не сейчас. . .")
        elif Girl.FondleB and ApprovalCheck(Girl, 1100, TabM = 3):
                $ Girl.FaceChange("sexy", 1)
                if Girl is RogueX:
                        ch_r "Знаешь, возможно, нам стоит продолжить. . ."
                elif Girl is KittyX:
                        ch_k "Я не против, если мы. . . продолжим. . ."
                elif Girl is EmmaX:
                        if "three" not in EmmaX.History and not AloneCheck(EmmaX):
                                    # if there are other girls in the room. . .
                                    call Emma_ThreeCheck
                        ch_e "Хочешь продолжить?"
                elif Girl is LauraX:
                        ch_l "Мы должны продолжить. . ."
                elif Girl is JeanX:
                        ch_j "У тебя есть еще какие-нибудь предложения? . ."
                elif Girl is StormX:
                        ch_s "Желаешь продолжить?"
                elif Girl is JubesX:
                        ch_v "Хочешь больше?"
                elif Girl is GwenX:
                        ch_g "К чему ты клонишь? Хочешь большего?"
                elif Girl is BetsyX:
                        ch_b "У тебя есть еще что-нибудь в планах? . ."
                elif Girl is DoreenX:
                        if not Player.Male:
                            ch_d "Ты. . . хотела бы продолжить? . ."
                        else:
                            ch_d "Ты. . . хотел бы продолжить? . ."
                elif Girl is WandaX:
                        ch_w "Хочешь продолжить еще немного?"
                menu:
                    extend ""
                    "Ага!":
                            $ Girl.Statup("Lust", 60, 5)
                            $ Girl.Statup("Love", 90, 2)
                            $ Girl.Statup("Obed", 60, 3)
                            $ Girl.Statup("Inbt", 60, 3)
                            call SexAct("breasts") # call expression Girl.Tag + "_SexAct" pass ("breasts")
                            call Trig_Reset(1)
                            return
                    "Нет, хватит.":
                            $ Girl.FaceChange("sad", 1)
                            $ Girl.Statup("Lust", 60, 2)
                            $ Girl.Statup("Love", 90, -1)
                            $ Girl.Statup("Obed", 60, 4)
                            $ Girl.Statup("Inbt", 60, 3)
                            if Girl is RogueX:
                                    ch_r "Как скажешь."
                            elif Girl is KittyX:
                                    ch_k "Как хочешь."
                            elif Girl is EmmaX:
                                    ch_e "Ох. Жаль."
                            elif Girl is LauraX:
                                    ch_l "Ладно."
                            elif Girl is JeanX:
                                    ch_j "Ах, как жаль. . ."
                            elif Girl is StormX:
                                    ch_s "Очень жаль."
                            elif Girl is JubesX:
                                    ch_v "Оу. . ."
                            elif Girl is GwenX:
                                    ch_g "Оу. . ."
                            elif Girl is BetsyX:
                                    ch_b "Печально. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ох, ладно. . ."
                            elif Girl is WandaX:
                                    ch_w "Ох. Ладно."
        elif ApprovalCheck(Girl, 800, TabM = 3):
                $ Girl.Brows = "confused"
                $ Girl.Eyes = "sexy"
                $ Girl.Mouth = "smile"
                if Girl is RogueX:
                        ch_r "Тебе было весело?"
                elif Girl is KittyX:
                        ch_k "Тебе понравилось?"
                elif Girl is EmmaX:
                        ch_e "Ну как, понравилось?"
                elif Girl is LauraX:
                        ch_l "Понравилось?"
                elif Girl is JeanX:
                        ch_j "Приятно, согласен?"
                elif Girl is StormX:
                        ch_s "Уверена, ты был впечатлён."
                elif Girl is JubesX:
                        ch_v "Нууу, если думаешь о продолжении. . ."
                elif Girl is GwenX:
                        ch_g "Как тебе?"
                elif Girl is BetsyX:
                        ch_b "Тебе понравилось?"
                elif Girl is DoreenX:
                        ch_d "Тебе было весело? . ."
                elif Girl is WandaX:
                        ch_w "Что думаешь?"
        elif ApprovalCheck(Girl, 800):
                $ Girl.FaceChange("angry", 1)
                if Girl is RogueX:
                        if not Player.Male:
                            ch_r "Не могу поверить, что ты пошла на такое при свидетелях!"
                        else:
                            ch_r "Не могу поверить, что ты пошел на такое при свидетелях!"
                elif Girl is KittyX:
                        if not Player.Male:
                            ch_k "Как ты могла сделать подобное на людях?"
                        else:
                            ch_k "Как ты мог сделать подобное на людях?"
                elif Girl is EmmaX:
                        if not Player.Male:
                            ch_e "Не могу поверить, что ты сделала такое на людях."
                        else:
                            ch_e "Не могу поверить, что ты сделал такое на людях."
                elif Girl is LauraX:
                        ch_l "Зачем нужно было на людях?"
                elif Girl is JeanX:
                        ch_j "Не привлекай лишнее внимание. . ."
                elif Girl is StormX:
                        ch_s "Не на людях."
                elif Girl is JubesX:
                        ch_v "Здесь не совсем подходящее место для этого. . ."
                elif Girl is GwenX:
                        if not Player.Male:
                            ch_g "Зачем ты сделала подобное здесь?!"
                        else:
                            ch_g "Зачем ты сделал подобное здесь?!"
                elif Girl is BetsyX:
                        ch_b "Я не могу смириться с твоей неосмотрительностью. . ."
                elif Girl is DoreenX:
                        ch_d "Здесь слишком людно!"
                elif Girl is WandaX:
                        ch_w "Здесь слишком людно."
        else:
                $ Girl.FaceChange("angry", 1)
                if Girl is RogueX:
                        ch_r "Не делай так больше!"
                elif Girl is KittyX:
                        ch_k "[Girl.like]держи свои руки при себе!"
                elif Girl is EmmaX:
                        ch_e "Держи свои руки при себе."
                elif Girl is LauraX:
                        ch_l "Держи свои руки при себе!"
                elif Girl is JeanX:
                        ch_j "Можешь смотреть, но не трогать."
                elif Girl is StormX:
                        ch_s "Я не давала тебе разрешения прикасаться так ко мне."
                elif Girl is JubesX:
                        ch_v "Сначала стоит спрашивать, понимаешь? . ."
                elif Girl is GwenX:
                        ch_g "Может. . . сначала стоило спросить?"
                elif Girl is BetsyX:
                        ch_b "Возможно. . . тебе стоило сперва предупредить. . ."
                elif Girl is DoreenX:
                        ch_d "Тебе стоит спрашивать, прежде чем делать что-то подобное. . ."
                elif Girl is WandaX:
                        ch_w "Держи руки при себе."
        return
#End Grab her tit

#end Grab Tit/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Ask for panties / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label AskPanties(Girl=0,Store = 0): #rkeljsvgbdw
    #called from Chat menu flirting options
    if Girl not in TotalGirls:
            return
    $ Store = Tempmod
    $ Line = 0
    if not Girl.Panties or Girl.Panties == "shorts":
            if ApprovalCheck(Girl, 900):
                $ Girl.FaceChange("sexy", 1)
                $ Girl.Statup("Lust", 80, 5)
                $ Girl.Statup("Lust", 60, 5)
                $ Girl.Statup("Lust", 40, 10)
                $ Girl.Statup("Inbt", 60, 5)
                $ Girl.Statup("Inbt", 30, 10)
                if Girl is RogueX:
                        ch_r "На мне их нет."
                elif Girl is KittyX:
                        ch_k "Я бы согласилась. . . если бы на мне они были. . ."
                elif Girl is EmmaX:
                        ch_e "Полагаю. . . я просто не смогу исполнить твое желание."
                elif Girl is LauraX:
                        ch_l "Я их не надела."
                elif Girl is JeanX:
                        ch_j "Ну, на мне их нет."
                elif Girl is StormX:
                        ch_s "В данный момент я их не ношу."
                elif Girl is JubesX:
                        ch_v "Я бы согласилась, если бы на мне они были."
                elif Girl is GwenX:
                        ch_g "Может. . . может хочешь, чтобы я сперва их надела?"
                elif Girl is BetsyX:
                        ch_b "Я решила не портить ими свой образ. . ."
                elif Girl is DoreenX:
                        ch_d "Я, эм, забыла их надеть. . ."
                elif Girl is WandaX:
                        ch_w "К сожалению, на мне их сейчас нет."
            elif Girl.Over == "towel" or not Girl.Legs:
                $ Girl.FaceChange("bemused", 2)
                if Girl is RogueX:
                        ch_r "Думаю, ты понимаешь, что я не могу."
                elif Girl is KittyX:
                        ch_k "И как, по-твоему, мне это сделать?"
                elif Girl is EmmaX:
                        if not Player.Male:
                            ch_e "Думаю, ты и сама видишь, что на мне их нет. . ."
                        else:
                            ch_e "Думаю, ты и сам видишь, что на мне их нет. . ."
                elif Girl is LauraX:
                        ch_l "Неужели ты думаешь, что на мне они надеты?"
                elif Girl is JeanX:
                        ch_j "Зачем мне их было надевать?"
                elif Girl is StormX:
                        if not Player.Male:
                            ch_s "С чего ты взяла, что на мне они надеты?"
                        else:
                            ch_s "С чего ты взял, что на мне они надеты?"
                elif Girl is JubesX:
                        ch_v "И где мне их взять?"
                elif Girl is GwenX:
                        ch_g "Может. . . может хочешь, чтобы я сперва их надела?"
                elif Girl is BetsyX:
                        ch_b "Очевидно, на мне их нет. . ."
                elif Girl is DoreenX:
                        ch_d "На мне их точно нет. . ."
                elif Girl is WandaX:
                        ch_w "Думаешь, они на мне?"
            else:
                $ Girl.FaceChange("bemused", 2, Eyes="side")
                $ Girl.Statup("Lust", 80, 5)
                $ Girl.Statup("Lust", 60, 5)
                $ Girl.Statup("Lust", 40, 10)
                $ Girl.Statup("Inbt", 60, 5)
                if Girl is RogueX:
                        ch_r "Извини, но я не могу."
                elif Girl is KittyX:
                        ch_k "Эм, нет. Не сейчас. Так. . . нужно."
                elif Girl is EmmaX:
                        ch_e "Хм, боюсь, что я вынуждена отказаться."
                elif Girl is LauraX:
                        ch_l "Сейчас я их не ношу."
                elif Girl is JeanX:
                        ch_j "Эм, нет. . ."
                elif Girl is StormX:
                        ch_s "В данный момент я их не ношу."
                elif Girl is JubesX:
                        ch_v "Сейчас я, эм, не могу."
                elif Girl is GwenX:
                        ch_g "Сечас. . . я. . . не могу."
                elif Girl is BetsyX:
                        ch_b "Боюсь. . . сейчас это невозможно. . ."
                elif Girl is DoreenX:
                        ch_d "Сечас. . . я. . . не могу. . ."
                elif Girl is WandaX:
                        ch_w "Я сейчас не могу, и объяснить тоже."
    else:
        #if she is wearing some panties
        if Girl.SeenPussy and ApprovalCheck(Girl, 500):
                    #You've seen her Pussy.
                    $ Tempmod += 15
        elif Girl.SeenPanties and ApprovalCheck(Girl, 500):
                    #You've seen her panties.
                    $ Tempmod += 5
        if "exhibitionist" in Girl.Traits:
                    $ Tempmod += (Girl.Taboo * 5)
        if Girl in Player.Harem or ("sex friend" in Girl.Petnames and not Taboo):
                    $ Tempmod += 10
        if "no bottomless" in Girl.RecentActions:
                    $ Tempmod -= 20

        $ Line = 0
        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 10:
                #pants or something similar
                if ApprovalCheck(Girl, 1000, "OI", TabM = 5) or "exhibitionist" in Girl.Traits:
                    $ Line = "here"
                elif ApprovalCheck(Girl, 900, TabM = 5):
                    $ Line = "change"
        elif Girl.PantsNum() == 5:
                #skirt
                if ApprovalCheck(Girl, 600, "OI", TabM = 5) or "exhibitionist" in Girl.Traits:
                    $ Line = "here"
                elif ApprovalCheck(Girl, 1100, TabM = 5):
                    $ Line = "change"
        else:
                if ApprovalCheck(Girl, 1200, TabM = 5) or "exhibitionist" in Girl.Traits:
                    $ Line = "here"

        if Girl is StormX and Line == "change":
                #Storm will not leave room unless it's in public and she's not dealt with Xavier.
                if not Taboo or StormX in Rules:
                        $ Line = "here"

        if Girl is KittyX and Line:
                #since Kitty has a trick, she's separate
                $ Girl.Statup("Lust", 60, 2)
                $ Girl.Statup("Obed", 60, 4)
                $ Girl.Statup("Inbt", 60, 4)
                call Remove_Panties(Girl)
                if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 10:
                            $ Girl.Statup("Lust", 60, 5)
                            $ Girl.Statup("Obed", 60, 5)
                            $ Girl.Statup("Inbt", 60, 5)
                elif Girl.PantsNum() == 5:
                            $ Girl.Statup("Lust", 60, 5)
                            $ Girl.Statup("Obed", 60, 4)
                            $ Girl.Statup("Inbt", 60, 4)
                else:
                            $ Girl.Statup("Lust", 60, 7)
                            $ Girl.Statup("Obed", 60, 6)
                            $ Girl.Statup("Inbt", 60, 8)
                $ Tempmod = Store
                $ Line = 0
                return
                #end Kitty has a trick, she's separate

        if Line == "here":
                #She's agreed to change and will do it here
                $ Girl.FaceChange("sly")
                if Girl.PantsNum() == 5:
                    #skirt
                    $ Girl.Statup("Obed", 60, 4)
                    $ Girl.Statup("Inbt", 60, 4)
                else: #no pants or skirt
                    $ Girl.Statup("Obed", 60, 6)
                    $ Girl.Statup("Inbt", 60, 6)

                $ Girl.Statup("Lust", 60, 5)
                call Remove_Panties(Girl)

                if Girl.Taboo:
                    $ Girl.Statup("Lust", 60, 5)
                    if "exhibitionist" in Girl.Traits:
                        $ Girl.Statup("Lust", 80, 5)
                        $ Girl.Statup("Lust", 200, 5)
                    $ Girl.Statup("Obed", 80, 10)
                    $ Girl.Statup("Inbt", 80, 10)
                #end She's agreed to change and will do it here

        elif Line:
                #She's agreed to change, but leaves the room to do it.
                if not Taboo and Girl is not StormX:
                    #If it's in one of your rooms
                    $ Girl.FaceChange("bemused", 1)
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Не могла бы ты выйти на секунду?"
                            else:
                                ch_r "Не мог бы ты выйти на секунду?"
                    elif Girl is KittyX:
                            if not Player.Male:
                                ch_k "Не могла бы ты отвернуться?"
                            else:
                                ch_k "Не мог бы ты отвернуться?"
                    elif Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Я была бы признательна, если бы ты ненадолго вышла."
                            else:
                                ch_e "Я была бы признательна, если бы ты ненадолго вышел."
                    elif Girl is LauraX:
                            ch_l "Можешь отвернуться?"
                    elif Girl is JeanX:
                            ch_j "Слушай, можешь оставить мне одну ненадолго?"
                    elif Girl is JubesX:
                            ch_v "Эм, отвернись."
                    elif Girl is GwenX:
                            ch_g "Эм. . . сначала тебе придется отвернуться. . ."
                    elif Girl is BetsyX:
                            if not Player.Male:
                                ch_b "Не могла бы ты оставить меня одну ненадолго?"
                            else:
                                ch_b "Не мог бы ты оставить меня одну ненадолго?"
                    elif Girl is DoreenX:
                            if not Player.Male:
                                ch_d "Ты не могла бы отвернуться?"
                            else:
                                ch_d "Ты не мог бы отвернуться?"
                    elif Girl is WandaX:
                            ch_w "Отвернись."
                    menu:
                        extend ""
                        "Ладно.":
                                $ Girl.Statup("Love", 90, 5)
                                $ Girl.FaceChange("smile", 1)
                                if Girl is RogueX:
                                        ch_r "Спасибо, [Girl.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Спасибо, [Girl.Petname]."
                                elif Girl is EmmaX:
                                        ch_e "Благодарю, [Girl.Petname]."
                                elif Girl is LauraX:
                                        ch_l "Спасибо."
                                elif Girl is JeanX:
                                        ch_j "Клево."
                                elif Girl is JubesX:
                                        ch_v "Отлично."
                                elif Girl is GwenX:
                                        ch_g "Здорово. . ."
                                elif Girl is BetsyX:
                                        ch_b "Замечательно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Спасибо. . ."
                                elif Girl is WandaX:
                                        ch_w "Вот и хорошо."
                                $ Girl.FaceChange("sly", 1)
                                $ Girl.Statup("Lust", 60, 2)
                                $ Girl.Statup("Obed", 60, 4)
                                $ Girl.Statup("Inbt", 60, 4)
                                show blackscreen onlayer black
                                "Вы ненадолго выходите."
                                hide blackscreen onlayer black
                                $ Girl.DailyActions.append("pantyless")
                                $ Girl.OutfitChange()
                                call OutfitShame(Girl,20)
                                "Когда вы возвращаетесь, она медленно протягивает вам свои скомканные трусики."
                                $ Line = 0

                        "И пропустить все самое интересное?":
                            if ApprovalCheck(Girl, 1000, "LI"):
                                    $ Girl.Statup("Lust", 70, 5)
                                    $ Girl.Statup("Obed", 60, 5)
                                    $ Girl.Statup("Inbt", 60, 5)
                                    $ Girl.FaceChange("sly", 1)
                                    if Girl is RogueX:
                                            ch_r "Ладно, хорошо."
                                    elif Girl is KittyX:
                                            ch_k "О, ты думаешь, что будет что-то интересное?"
                                    elif Girl is EmmaX:
                                            ch_e "Как предсказуемо."
                                    elif Girl is LauraX:
                                            ch_l "О, значит, хочешь посмотреть?"
                                    elif Girl is JeanX:
                                            ch_j "Ох, будет тебе интересное. . ."
                                    elif Girl is JubesX:
                                            ch_v "Хорошо. . ."
                                    elif Girl is GwenX:
                                            ch_g "Ну ладно. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Если ты настаиваешь. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ох. Значит, хочешь. . . посмотреть. . ."
                                    elif Girl is WandaX:
                                            ch_w "Хех."
                            else:
                                    $ Girl.FaceChange("angry", 1)
                                    $ Girl.Statup("Love", 90, -5)
                                    $ Girl.Statup("Obed", 60, -3)
                                    $ Girl.Statup("Inbt", 60, 5)
                                    if Girl is RogueX:
                                            ch_r "Тут не на что будет смотреть, [Girl.Petname]."
                                    elif Girl is KittyX:
                                            ch_k "Как знаешь."
                                    elif Girl is EmmaX:
                                            ch_e "Ты думаешь, что при тебе я на это пойду, [Player.Name]?"
                                    elif Girl is LauraX:
                                            ch_l "Ага."
                                    elif Girl is JeanX:
                                            ch_j "Ну, ты точно ничего не увидишь."
                                    elif Girl is JubesX:
                                            ch_v "Нет."
                                    elif Girl is GwenX:
                                            ch_g "Оох, ну нет так нет. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Тогда, боюсь, мне придется отказаться."
                                    elif Girl is DoreenX:
                                            ch_d "Ох. Значит, хочешь. . . посмотреть. . ."
                                            ch_d "Но при тебе я не могу. . ."
                                    elif Girl is WandaX:
                                            ch_w "Не будет ничего интересного."
                                    $ Line = 0

                        "Нет, я останусь.":
                            if ApprovalCheck(Girl, 600, "OI"):
                                    $ Girl.FaceChange("perplexed", 1)
                                    $ Girl.Statup("Lust", 70, 5)
                                    $ Girl.Statup("Obed", 60, 10)
                                    $ Girl.Statup("Inbt", 60, 5)
                                    if Girl is RogueX:
                                            ch_r "Ну, если тебе так хочется."
                                    elif Girl is KittyX:
                                            ch_k "Ладно."
                                    elif Girl is EmmaX:
                                            ch_e "Если тебе этого хочется."
                                    elif Girl is LauraX:
                                            ch_l "Ладно."
                                    elif Girl is JeanX:
                                            ch_j "Ладно."
                                    elif Girl is JubesX:
                                            ch_v ". . . Ладно."
                                    elif Girl is GwenX:
                                            ch_g "Ладно. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Если тебе этого хочется. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ох. Значит, хочешь. . . посмотреть. . ."
                                    elif Girl is WandaX:
                                            ch_w "Ох, конечно. . ."
                                    $ Girl.FaceChange("normal")
                            else:
                                    $ Girl.FaceChange("angry", 1)
                                    $ Girl.Statup("Love", 90, -10)
                                    $ Girl.Statup("Obed", 60, -5)
                                    $ Girl.Statup("Inbt", 60, 5)
                                    if Girl is RogueX:
                                            ch_r "Тогда я пас."
                                    elif Girl is KittyX:
                                            ch_k "Хм, а[Girl.like]проявить немного уважения?"
                                    elif Girl is EmmaX:
                                            ch_e "Тогда, полагаю, на этом мы закончим."
                                    elif Girl is LauraX:
                                            ch_l "Это совсем невежливо."
                                    elif Girl is JeanX:
                                            ch_j "Хорошо, тогда ты ничего не получишь."
                                    elif Girl is JubesX:
                                            ch_v "Тогда забудь."
                                    elif Girl is GwenX:
                                            ch_g "Ну нет так нет. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Тогда, боюсь, мне придется отказаться."
                                    elif Girl is DoreenX:
                                            ch_d "Ох. Значит, хочешь. . . посмотреть. . ."
                                            ch_d "Но при тебе я не могу. . ."
                                    elif Girl is WandaX:
                                            ch_w "Я не собираюсь устраивать представление для тебя."
                                    $ Line = 0
                    if Line:
                                    #She agreed to stay
                                    $ Girl.FaceChange("sly", 1)
                                    if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 10:
                                            $ Girl.Statup("Lust", 60, 5)
                                            $ Girl.Statup("Obed", 60, 5)
                                            $ Girl.Statup("Inbt", 60, 5)
                                    elif Girl.PantsNum() == 5:
                                            $ Girl.Statup("Lust", 60, 5)
                                            $ Girl.Statup("Obed", 60, 4)
                                            $ Girl.Statup("Inbt", 60, 4)
                                    call Remove_Panties(Girl)
                    #end If it's in one of your rooms

                else:
                    #if she's in public
                    $ Girl.FaceChange("sly", 1)
                    $ Girl.Statup("Lust", 60, 2)
                    $ Girl.Statup("Obed", 60, 4)
                    $ Girl.Statup("Inbt", 60, 4)
                    $ Girl.Loc = "hold"
                    call Set_The_Scene
                    "[Girl.Name] кивает и на минутку отходит."
                    $ Girl.DailyActions.append("pantyless")
                    $ Girl.OutfitChange()
                    call OutfitShame(Girl,20)
                    $ Girl.Loc = bg_current
                    call Set_The_Scene
                    "Она возвращается и медленно протягивает вам свои скомканные трусики."
                #end She's agreed to change, but leaves the room to do it.
        else:
            #She refuses.
            $ Girl.FaceChange("angry", 2)
            if not ApprovalCheck(Girl, 500):
                    $ Girl.Statup("Lust", 60, 5)
                    $ Girl.Statup("Love", 90, -10)
                    $ Girl.Statup("Obed", 60, 3)
                    $ Girl.Statup("Inbt", 60, 3)
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Не могу поверить, что ты попросила меня о чем-то подобном!"
                            else:
                                ch_r "Не могу поверить, что ты попросил меня о чем-то подобном!"
                    elif Girl is KittyX:
                            ch_k "Думаешь, я способна пойти на такое?"
                    elif Girl is EmmaX:
                            ch_e "Об этом не может быть и речи."
                    elif Girl is LauraX:
                            ch_l "Почему ты думаешь, что я могу согласиться?"
                    elif Girl is JeanX:
                            ch_j "Думаю, я оставлю их при себе, спасибо."
                    elif Girl is StormX:
                            ch_s "Я ношу их не просто так."
                    elif Girl is JubesX:
                            ch_v "Нет, спасибо."
                    elif Girl is GwenX:
                            ch_g "Эм. . . нет. . ."
                    elif Girl is BetsyX:
                            ch_b "Нет."
                    elif Girl is DoreenX:
                            ch_d "Иу, нет!"
                    elif Girl is WandaX:
                            ch_w "Ни за что, [Player.Name]."
                    $ Girl.RecentActions.append("angry")
                    $ Girl.DailyActions.append("angry")
            elif not ApprovalCheck(Girl, 500, TabM = 5):
                    $ Girl.Statup("Lust", 60, 5)
                    $ Girl.Statup("Love", 90, -5)
                    $ Girl.Statup("Obed", 60, 5)
                    $ Girl.Statup("Inbt", 60, 5)
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Не могу поверить, что ты попросила меня о чем-то подобном в таком месте!"
                            else:
                                ch_r "Не могу поверить, что ты попросил меня о чем-то подобном в таком месте!"
                    elif Girl is KittyX:
                            ch_k "Эм, здесь?"
                    elif Girl is EmmaX:
                            ch_e "Оглянись и узнаешь мой ответ."
                    elif Girl is LauraX:
                            ch_l "На людях?"
                    elif Girl is JeanX:
                            ch_j "Не. . . здесь."
                    elif Girl is StormX:
                            ch_s "Я не думаю, что здесь уместно делать нечто подобное."
                    elif Girl is JubesX:
                            ch_v "Эм, только не здесь."
                    elif Girl is GwenX:
                            ch_g "Эм. . . нет, спасибо? . ."
                    elif Girl is BetsyX:
                            ch_b "Я вынуждена отказаться."
                    elif Girl is DoreenX:
                            ch_d "Как я могу сделать что-то подобное в таком месте?"
                    elif Girl is WandaX:
                            ch_w "Ты просишь мои трусики -здесь?-"
                    $ Girl.RecentActions.append("angry")
                    $ Girl.DailyActions.append("angry")
            else:
                    $ Girl.FaceChange("bemused", 2)
                    $ Girl.Statup("Lust", 60, 3)
                    $ Girl.Statup("Inbt", 60, 1)
                    if Girl.Taboo:
                            $ Girl.Statup("Inbt", 60, 2)
                            if Girl is RogueX:
                                    ch_r "Прости, [Girl.Petname], я еще не готова."
                            elif Girl is KittyX:
                                    ch_k "Наверное, тебе сперва надо это заслужить, [Girl.Petname]."
                            elif Girl is EmmaX:
                                    ch_e "Знаешь, я бы с удовольствием, [Girl.Petname], но не здесь."
                            elif Girl is LauraX:
                                    ch_l "Может быть, когда-нибудь, [Girl.Petname]."
                            elif Girl is JeanX:
                                    ch_j "Только не здесь."
                            elif Girl is StormX:
                                    ch_s "Я не думаю, что здесь уместно делать нечто подобное."
                            elif Girl is JubesX:
                                    ch_v "Эм, только не здесь."
                            elif Girl is GwenX:
                                    ch_g "Эм. . . только не здесь. . ."
                            elif Girl is BetsyX:
                                    ch_b "В сложившихся обстоятельствах я вынуждена отказаться."
                            elif Girl is DoreenX:
                                    ch_d "Я не могу. . ."
                            elif Girl is WandaX:
                                    ch_w "Здесь слишком людно."
                    else:
                            $ Girl.FaceChange("perplexed")
                            $ Girl.Statup("Obed", 60, -2)
                            if Girl is RogueX:
                                    ch_r "Нет, тебе я их точно не дам."
                            elif Girl is KittyX:
                                    if not Player.Male:
                                        ch_k "Ты отвратительна, [Girl.Petname]."
                                    else:
                                        ch_k "Ты отвратителен, [Girl.Petname]."
                            elif Girl is EmmaX:
                                    ch_e "Тебе придется еще заслужить это, [Girl.Petname]."
                            elif Girl is LauraX:
                                    ch_l "Зачем они тебе?"
                            elif Girl is JeanX:
                                    ch_j "Хитрюга."
                            elif Girl is StormX:
                                    ch_s "Чем тебя они так заинтересовали?"
                            elif Girl is JubesX:
                                    ch_v "Я не хочу."
                            elif Girl is GwenX:
                                    ch_g "Эм. . . нет. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я вынуждена отказаться."
                            elif Girl is DoreenX:
                                    ch_d "Я не могу. . ."
                            elif Girl is WandaX:
                                    ch_w "Только не когда ты рядом."
            $ Girl.Blush = 1
            #end She refuses.
        #end if she is wearing some panties
    $ Tempmod = Store
    $ Line = 0
    return

label Remove_Panties(Girl = 0, Type=0,Store = 0, Store2 = 0):  #rkeljsvgbdw
    if Girl not in TotalGirls:
            return
    if Girl is KittyX:
            $ Girl.Panties = 0
            $ Girl.FaceChange("bemused")
            if Girl.PantsNum() >= 6:
                "[Girl.Name]  оглядывается по сторонам, залазит рукой в карман и вытаскивает свои трусики."
            elif Girl.PantsNum() == 5:
                "[Girl.Name] оглядывается по сторонам, засовывает руку под юбку и вытаскивает трусики."
            elif Girl.HoseNum() >= 5:
                "[Girl.Name] оглядывается по сторонам, просовывает руку в свои [get_clothing_name(Girl.Hose_key, vin)] и вытаскивает трусики."
            else:
                "[Girl.Name] оглядывается по сторонам и стягивает с себя трусики."

            $ Girl.FaceChange("sexy")
            "Она протягивает их вам с ухмылкой."

            if not Girl.Legs and Girl.HoseNum() <= 10:
                    call Girl_First_Bottomless(Girl)

            $ Girl.DailyActions.append("pantyless")
            $ Girl.OutfitChange()
            call OutfitShame(Girl,20)
            return
    elif Girl is JeanX and Girl.PantsNum() == 5 and not ApprovalCheck(Girl, 400, "L"): #skirt
            $ Girl.Panties = 0
            $ Girl.FaceChange("bemused",Eyes="psychic")
            "Вы чувствуете какое-то движение, и ее трусики падают к ее ногам, она быстро переступает через них."
            "Они у самой земли подлетают к вам, а затем заскакивают в вашу руку."
            $ Girl.FaceChange("sexy")

            if not Girl.Legs and Girl.HoseNum() <= 10:
                    call Girl_First_Bottomless(Girl)

            $ Girl.DailyActions.append("pantyless")
            $ Girl.OutfitChange()
            call OutfitShame(Girl,20)
            return

    $ Store = Girl.Legs
    $ Store2 = get_clothing_name(Girl.Hose_key, vin)
    if Girl.PantsNum() >= 6:
        #pants or shorts
        $ Girl.Legs = 0
        $ Type = 1
    elif Girl.PantsNum() == 5:
        #skirt
        $ Girl.Upskirt = 1
        $ Type = 2
    if Girl.HoseNum() >= 5:
        $ Girl.Hose = 0
        $ Type = 3 if Type == 2 else 4
        # 3 if skirt/hose, 4 if just hose
    $ Girl.Panties = 0

    if Girl.Taboo:
            if Type == 1:
                "[Girl.Name] оглядывается, затем стягивает с себя штаны и трусики вместе с ними."
            elif Type == 3:
                "[Girl.Name]  оглядывается, затем задирает юбку, стягивает с себя [Store2] и трусики вместе с ними."
            elif Type == 2:
                "[Girl.Name] оглядывается, затем она залезает себе под юбку и стягивает с себя трусики."
            elif Type == 4:
                "[Girl.Name] оглядывается, затем стягивает с себя [Store2] и трусики вместе с ними."
            else:
                "[Girl.Name] оглядывается, затем стягивает с себя трусики."
    else: #Not Taboo
            if Type == 1:
                "[Girl.Name], смотря вам в глаза, стягивает с себя штаны и трусики вместе с ними."
            elif Type == 3:
                "[Girl.Name], смотря вам в глаза, задирает юбку, стягивает с себя [Store2] и трусики вместе с ними."
            elif Type == 2:
                "[Girl.Name], смотря вам в глаза, залезает себе под юбку и стягивает с себя трусики."
            elif Type == 4:
                "[Girl.Name], смотря вам в глаза, стягивает с себя [Store2] и трусики вместе с ними."
            else:
                "[Girl.Name], смотря вам в глаза, стягивает с себя трусики."

    $ Girl.Legs = Store
    $ Girl.Hose = Store2
    if Girl.PantsNum() > 6:
        #pants
        "Она протягивает вам трусики, а затем натягивает штаны."
    elif Girl.PantsNum() == 6 or Girl.Panties == "shorts":
        #shorts
        "Она протягивает вам трусики, а затем натягивает шорты."
        $ Girl.Upskirt = 0
    elif Girl.PantsNum() == 5 and Girl.HoseNum() >= 5:
        #skirt and hose
        "Она протягивает вам трусики, а затем натягивает свои [get_clothing_name(Girl.Hose_key, vin)] и опускает юбку."
        $ Girl.Upskirt = 0
    elif Girl.PantsNum() == 5:
        #skirt
        "Она протягивает вам трусики и поправляет юбку."
        $ Girl.Upskirt = 0
    elif Girl.HoseNum() >= 5:
        #hose
        "Она протягивает вам трусики, а затем натягивает свои [get_clothing_name(Girl.Hose_key, vin)]."
    else:
        "[Girl.Name]  протягивает их вам скомканными."
    call Girl_First_Bottomless(Girl,1)

    $ Girl.DailyActions.append("pantyless")
    $ Girl.OutfitChange()
    call OutfitShame(Girl,20)
    return
# End Ask for panties / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# start Ask insert vibrator / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Ask_Vibrator(Girl=0,Store = 0): #rkeljsvgbdw
    #called from Chat menu flirting options
    if Girl not in TotalGirls:
            return
    $ Store = Tempmod
    $ Line = 0
    call Girl_Vibrator_Check(Girl)
    if not _return: #if nobody has a vibrator
            $ Girl.Chat[5] = 0
            return
    #provide one if they don't have one

    if "vibein" in Girl.DailyActions and "vibeout" not in Girl.DailyActions:
            #if the vibrator is in and you ask to remove it
            call AnyLine(Girl,"Что? Ты хочешь достать его?")

    #if she is wearing some panties
    if Girl.FondleP and ApprovalCheck(Girl, 500):
                #You've fondled her Pussy.
                $ Tempmod += 15
    if Girl.Vib:
                $ Tempmod += 15
    if "exhibitionist" in Girl.Traits:
                $ Tempmod += (Girl.Taboo * 5)
    if Girl in Player.Harem or ("sex friend" in Girl.Petnames and not Taboo):
                $ Tempmod += 10
    if "no vibrator" in Girl.RecentActions:
                $ Tempmod -= 20


    $ Line = 0
    if ApprovalCheck(Girl, 1000, "OI", TabM = 4) or "exhibitionist" in Girl.Traits:
            #she will do it here
            $ Line = "here"
    elif ApprovalCheck(Girl, 1200, TabM = 4):
            #she will do it elsewhere
            $ Line = "change"

    if Girl is KittyX and Line:
            #since Kitty has a trick, she's separate
            $ Girl.Statup("Obed", 60, 6)
            $ Girl.Statup("Inbt", 60, 8)
            call Girl_Insert_Vibrator(Girl)
            $ Girl.Statup("Lust", 60, 7)
            $ Tempmod = Store
            $ Line = 0
            return
            #end Kitty has a trick, she's separate

    if Line == "here":
            #She's agreed to use it and will do it here
            $ Girl.FaceChange("sly")
            $ Girl.Statup("Obed", 60, 6)
            $ Girl.Statup("Inbt", 60, 6)
            call Girl_Insert_Vibrator(Girl)
            $ Girl.Statup("Lust", 60, 5)

            if Girl.Taboo:
                if "exhibitionist" in Girl.Traits:
                    $ Girl.Statup("Lust", 80, 5)
                    $ Girl.Statup("Lust", 200, 5)
                $ Girl.Statup("Obed", 80, 10)
                $ Girl.Statup("Inbt", 80, 10)
            #end She's agreed to use it and will do it here

    elif Line:
            #She's agreed to use it, but leaves the room to do it.
            $ Girl.Statup("Obed", 70, 2)
            $ Girl.FaceChange("bemused", 1)
            if Girl is RogueX:
                    ch_r "Мне нужно это сделать. . . в другом месте. . ."
            elif Girl is EmmaX:
                    ch_e "Мне. . . нужно сделать это в более укромном месте."
            elif Girl is LauraX:
                    ch_l "Я все сделаю и вернусь."
            elif Girl is JeanX:
                    ch_j "Здесь?"
            elif Girl is StormX:
                    if not Player.Male:
                        ch_s "Ты уверена, что хочешь, чтобы я сделала это здесь?"
                    else:
                        ch_s "Ты уверен, что хочешь, чтобы я сделала это здесь?"
            elif Girl is JubesX:
                    ch_v "Я. . . скоро вернусь."
            elif Girl is GwenX:
                    ch_g "Эм. . . я скоро вернусь. . ."
            elif Girl is BetsyX:
                    ch_b "Пардон, один момент."
            elif Girl is DoreenX:
                    ch_d "Я. . . скоро вернусь. . ."
            elif Girl is WandaX:
                    ch_w "Хорошо, но я не хочу делать это здесь."
            menu:
                extend ""
                "Ладно.":
                        $ Girl.Statup("Love", 90, 5)
                        $ Girl.FaceChange("smile", 1)
                        if Girl is RogueX:
                                ch_r "Спасибо, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k "Спасибо, [Girl.Petname]."
                        elif Girl is EmmaX:
                                ch_e "Благодарю, [Girl.Petname]."
                        elif Girl is LauraX:
                                ch_l "Спасибо."
                        elif Girl is JeanX:
                                ch_j "Круто."
                        elif Girl is StormX:
                                ch_s "Благодарю."
                        elif Girl is JubesX:
                                ch_v "Лады."
                        elif Girl is GwenX:
                                ch_g "Здорово. . ."
                        elif Girl is BetsyX:
                                ch_b "Замечательно."
                        elif Girl is DoreenX:
                                ch_d "Ладно. . ."
                        elif Girl is WandaX:
                                ch_w "Секунду. . ."
                        $ Girl.FaceChange("sly", 1)
                        $ Girl.Statup("Obed", 60, 4)
                        $ Girl.Statup("Inbt", 60, 4)
                        show blackscreen onlayer black
                        "Она на минутку отходит."
                        hide blackscreen onlayer black
                        $ Girl.DailyActions.append("vibein")
                        $ Girl.Vib += 1
                        $ Girl.Statup("Lust", 60, 2)
                        "Она возвращается, немного покачиваясь."
                        $ Line = 0

                "И пропустить все самое интересное?":
                    if ApprovalCheck(Girl, 1000, "LI"):
                            $ Girl.Statup("Lust", 70, 5)
                            $ Girl.Statup("Obed", 60, 5)
                            $ Girl.Statup("Inbt", 60, 5)
                            $ Girl.FaceChange("sly", 1)
                            if Girl is RogueX:
                                    if not Player.Male:
                                        ch_r "Ладно, уговорила."
                                    else:
                                        ch_r "Ладно, уговорил."
                            elif Girl is KittyX:
                                    ch_k "О, ты думаешь, что будет что-то интересное?"
                            elif Girl is EmmaX:
                                    ch_e "Как мило."
                            elif Girl is LauraX:
                                    ch_l "О, значит хочешь посмотреть?"
                            elif Girl is JeanX:
                                    ch_j "Ох, будет тебе интересное. . ."
                            elif Girl is StormX:
                                    ch_s "Я не хочу тебя разочаровывать. . ."
                            elif Girl is JubesX:
                                    ch_v "Хорошо. . ."
                            elif Girl is GwenX:
                                    ch_g "Ну ладно. . ."
                            elif Girl is BetsyX:
                                    ch_b "Если ты настаиваешь. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ох. Значит, хочешь. . . посмотреть. . ."
                            elif Girl is WandaX:
                                    if not Player.Male:
                                        ch_w "Ты такой испорченная. . ."
                                    else:
                                        ch_w "Ты такой испорченный. . ."
                    else:
                            $ Girl.FaceChange("angry", 1)
                            $ Girl.Statup("Love", 90, -5)
                            $ Girl.Statup("Obed", 60, -3)
                            $ Girl.Statup("Inbt", 60, 5)
                            if Girl is RogueX:
                                    ch_r "Ты не увидишь ничего интересного, [Girl.Petname]."
                            elif Girl is KittyX:
                                    ch_k "Похоже, что так."
                            elif Girl is EmmaX:
                                    ch_e "Ты думаешь, что будет что-то интересное, [Player.Name]?"
                            elif Girl is LauraX:
                                    ch_l "Да."
                            elif Girl is JeanX:
                                    ch_j "Тут нет ничего интересного."
                            elif Girl is StormX:
                                    ch_s ". . . Не хочу тебя огорчать, но ты ничего не увидишь."
                            elif Girl is JubesX:
                                    ch_v "Не-а."
                            elif Girl is GwenX:
                                    ch_g "Ооо, вот я обломщица. . ."
                            elif Girl is BetsyX:
                                    ch_b "Тогда, боюсь, я вынуждена отказаться."
                            elif Girl is DoreenX:
                                    ch_d "Ох. Значит, хочешь. . . посмотреть. . ."
                                    ch_d "Но я не могу при тебе."
                            elif Girl is WandaX:
                                    ch_w "Прости, [Girl.Petname]."
                            $ Line = 0

                "Нет, делай это здесь.":
                    if ApprovalCheck(Girl, 600, "OI"):
                            $ Girl.FaceChange("perplexed", 1)
                            $ Girl.Statup("Lust", 70, 5)
                            $ Girl.Statup("Obed", 60, 10)
                            $ Girl.Statup("Inbt", 60, 5)
                            if Girl is RogueX:
                                    ch_r "Если ты настаиваешь."
                            elif Girl is KittyX:
                                    ch_k "Ладно."
                            elif Girl is EmmaX:
                                    ch_e "Если тебе так хочется."
                            elif Girl is LauraX:
                                    ch_l "Ладно."
                            elif Girl is JeanX:
                                    ch_j "Ладно."
                            elif Girl is StormX:
                                    ch_s ". . . Хорошо."
                            elif Girl is JubesX:
                                    ch_v ". . . Ладно."
                            elif Girl is GwenX:
                                    ch_g "Ладно. . ."
                            elif Girl is BetsyX:
                                    ch_b "Хорошо."
                            elif Girl is DoreenX:
                                    ch_d "Ох. Значит, хочешь. . . посмотреть. . ."
                            elif Girl is WandaX:
                                    ch_w "Хех, конечно."
                            $ Girl.FaceChange("normal")
                    else:
                            $ Girl.FaceChange("angry", 1)
                            $ Girl.Statup("Love", 90, -10)
                            $ Girl.Statup("Obed", 60, -5)
                            $ Girl.Statup("Inbt", 60, 5)
                            if Girl is RogueX:
                                    ch_r "Тогда, пожалуй, я оставлю все как есть."
                            elif Girl is KittyX:
                                    ch_k "Хм, может[Girl.like]проявишь хоть немного уважения?"
                            elif Girl is EmmaX:
                                    ch_e "Тогда, пожалуй, мы закончили."
                            elif Girl is LauraX:
                                    ch_l "Думаю, в данных обстоятельствах глупо просить о таком."
                            elif Girl is JeanX:
                                    ch_j "Ну ладно, нет так нет."
                            elif Girl is StormX:
                                    ch_s ". . . Хорошо, мне придется тебя огорчить."
                            elif Girl is JubesX:
                                    ch_v "Тогда забудь."
                            elif Girl is GwenX:
                                    ch_g "Ладно, облом тебе. . ."
                            elif Girl is BetsyX:
                                    ch_b "Тогда, боюсь, я вынуждена отказаться."
                            elif Girl is DoreenX:
                                    ch_d "Ох. Значит, хочешь. . . посмотреть. . ."
                                    ch_d "Но я не могу при тебе."
                            elif Girl is WandaX:
                                    ch_w "Прости, [Girl.Petname]."
                            $ Line = 0
            if Line:
                            #She agreed to stay
                            $ Girl.FaceChange("sly", 1)
                            $ Girl.Statup("Obed", 60, 4)
                            $ Girl.Statup("Inbt", 60, 4)
                            call Girl_Insert_Vibrator(Girl)
                            $ Girl.Statup("Lust", 60, 5)
            #end If it's in one of your rooms

            else:
                #if she's in public
                $ Girl.FaceChange("sly", 1)
                $ Girl.Statup("Obed", 60, 4)
                $ Girl.Statup("Inbt", 60, 4)
                $ Girl.Loc = "hold"
                call Set_The_Scene
                "[Girl.Name] кивает и на минуту отходит."
                $ Girl.DailyActions.append("vibein")
                $ Girl.Vib += 1
                $ Girl.Loc = bg_current
                call Set_The_Scene
                $ Girl.Statup("Lust", 60, 4)
                "Она возвращается, немного покачиваясь."
            #end She's agreed to change, but leaves the room to do it.
    else:
        #She refuses.
        $ Girl.FaceChange("angry", 2)
        $ Girl.RecentActions.append("no vibrator")
        if not ApprovalCheck(Girl, 500):
                #if she strongly dislikes you
                $ Girl.Statup("Lust", 60, 5)
                $ Girl.Statup("Love", 60, -3)
                $ Girl.Statup("Love", 90, -8)
                $ Girl.Statup("Inbt", 60, 3)
                if Girl is RogueX:
                        ch_r "Не могу поверить, что ты можешь себе позволить просить меня о подобном!"
                elif Girl is KittyX:
                        ch_k "Ты думаешь, я могу пойти на такое?"
                elif Girl is EmmaX:
                        ch_e "Об этом не может быть и речи."
                elif Girl is LauraX:
                        ch_l "Почему ты думаешь, что я могла согласиться?"
                elif Girl is JeanX:
                        ch_j "Я не думаю, что сделаю это, спасибо."
                elif Girl is StormX:
                        ch_s "Меня это не интересует."
                elif Girl is JubesX:
                        ch_v "Нет, спасибо."
                elif Girl is GwenX:
                        ch_g "Эм. . . нет. . ."
                elif Girl is BetsyX:
                        ch_b "Это неприемлемо."
                elif Girl is DoreenX:
                        ch_d "Ни. . . ни за что!"
                elif Girl is WandaX:
                        ch_w "Что? Я на подобное не соглашусь!"
                $ Girl.Statup("Obed", 60, 3)
                $ Girl.RecentActions.append("angry")
                $ Girl.DailyActions.append("angry")
        elif not ApprovalCheck(Girl, 500, TabM = 4):
                #if it's too public
                $ Girl.Statup("Lust", 60, 5)
                $ Girl.Statup("Love", 50, -2)
                $ Girl.Statup("Love", 90, -5)
                $ Girl.Statup("Obed", 60, 5)
                $ Girl.Statup("Inbt", 60, 5)
                if Girl is RogueX:
                        ch_r "Не могу поверить, что ты просишь меня о подобном!"
                elif Girl is KittyX:
                        ch_k "То есть, здесь?"
                elif Girl is EmmaX:
                        ch_e "Оглянись и найди хоть немного здравого смысла."
                elif Girl is LauraX:
                        ch_l "На людях?"
                elif Girl is JeanX:
                        ch_j "Я не могу. . . в таком месте."
                elif Girl is StormX:
                        ch_s "Не думаю, что здесь это будет уместно."
                elif Girl is JubesX:
                        ch_v "Эм, только не здесь."
                elif Girl is GwenX:
                        ch_g "Эм. . . нет, спасибо? . ."
                elif Girl is BetsyX:
                        ch_b "В сложившихся обстоятельствах я не могу этого сделать."
                elif Girl is DoreenX:
                        ch_d "Я не могу сделать что-то подобное в таком месте!"
                elif Girl is WandaX:
                        ch_w "Честно говоря, здесь не самое подходящее место для этого."
                $ Girl.RecentActions.append("angry")
                $ Girl.DailyActions.append("angry")
        else:
                #if she doesn't hate you
                $ Girl.FaceChange("bemused", 2)
                $ Girl.Statup("Lust", 60, 3)
                $ Girl.Statup("Inbt", 60, 1)
                $ Girl.Statup("Inbt", 80, 1)
                if Girl.Taboo:
                        #in public
                        $ Girl.Statup("Inbt", 60, 2)
                        if Girl is RogueX:
                                ch_r "Извини, [Girl.Petname], я пока не готова."
                        elif Girl is KittyX:
                                ch_k "Может быть, когда-нибудь, [Girl.Petname]."
                        elif Girl is EmmaX:
                                ch_e "Знаешь, я не против, [Girl.Petname], но не здесь."
                        elif Girl is LauraX:
                                ch_l "Когда-нибудь, [Girl.Petname]."
                        elif Girl is JeanX:
                                ch_j "Не здесь."
                        elif Girl is StormX:
                                ch_s "Не думаю, что здесь это будет уместно."
                        elif Girl is JubesX:
                                ch_v "Эм, не здесь."
                        elif Girl is GwenX:
                                ch_g "Эм. . . не здесь. . ."
                        elif Girl is BetsyX:
                                ch_b "В сложившихся обстоятельствах я не могу этого сделать."
                        elif Girl is DoreenX:
                                ch_d ". . . Я не могу сделать ничего подобного. . ."
                        elif Girl is WandaX:
                                ch_w "Это не самое подходящее место для этого."
                else:
                        #not in public
                        $ Girl.FaceChange("perplexed")
                        $ Girl.Statup("Love", 70, -1)
                        $ Girl.Statup("Obed", 60, -2)
                        if Girl is RogueX:
                                ch_r "Нет, уж точно не когда ты рядом."
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Ты мне противна, [Girl.Petname]."
                                else:
                                    ch_k "Ты мне противен, [Girl.Petname]."
                        elif Girl is EmmaX:
                                ch_e "Тебе придется это еще заслужить, [Girl.Petname]."
                        elif Girl is LauraX:
                                ch_l "Зачем тебе это?"
                        elif Girl is JeanX:
                                ch_j "Как грубо."
                        elif Girl is StormX:
                                ch_s "Я считаю, что это неуместно."
                        elif Girl is JubesX:
                                ch_v "Я не хочу."
                        elif Girl is GwenX:
                                ch_g "Эм. . . нет. . ."
                        elif Girl is BetsyX:
                                ch_b "Я вынуждена отказаться."
                        elif Girl is DoreenX:
                                ch_d "Я не могу сделать это здесь. . ."
                        elif Girl is WandaX:
                                ch_w "Прости, я не могу."
        $ Girl.Blush = 1
        #end She refuses.
    $ Tempmod = Store
    $ Line = 0
    return

label Girl_Insert_Vibrator(Girl = 0):  #rkeljsvgbdw
    if Girl not in TotalGirls:
            return

    if "vibein" in Girl.DailyActions:# and "vibeout" not in Girl.DailyActions:
            #if the vibrator is in and you ask to remove it
            $ Line = "достан"
    else:
            $ Line = "засун"
    menu:
        "Вы [Line]ете его.":
                if not ApprovalCheck(Girl, 1200, TabM = 4) and not ApprovalCheck(Girl, 500, "OI", TabM = 4):
                        #she won't let you.
                        "Когда вы начинаете тянуться к ней, она поднимает руку."
                        call AnyLine(Girl,"Я сама.")
                        menu:
                            extend ""
                            "Хорошо":
                                    $ Girl.Statup("Love", 90, 2)
                            "Я настаиваю.":
                                    if ApprovalCheck(Girl, 900) and ApprovalCheck(Girl, 500, "O"):
                                            $ Girl.Statup("Love", 90, -1)
                                            $ Girl.Statup("Obed", 60, 3)
                                            $ Girl.Statup("Inbt", 60, 1)
                                            call AnyLine(Girl,"Хорошо.")
                                    else:
                                            $ Girl.Statup("Love", 90, -3)
                                            $ Girl.Statup("Obed", 60, 1)
                                            $ Girl.Statup("Inbt", 60, 3)
                                            call AnyLine(Girl,"Тогда забудь.")
                                            $ Girl.RecentActions.append("no vibrator")
                                            $ Line = 0
                                            return

                call Insert_Vibrator(Girl)
                return
        "Она [Line]ет его.":
                pass
    if Girl is KittyX:
            $ Girl.FaceChange("bemused",1)
            if Girl.PantsNum() >= 6:
                "[Girl.Name] оглядывается по сторонам и залезает в карман."
            elif Girl.PantsNum() == 5:
                "[Girl.Name]  оглядывается по сторонам и засовывает руку под юбку."
            elif Girl.HoseNum() >= 5:
                "[Girl.Name] оглядывается по сторонам и просовывает руку сквозь [get_clothing_name(Girl.Hose_key, vin)]."
            elif "vibein" in Girl.DailyActions:
                "[Girl.Name] оглядывается по сторонам и прикладывает руку к своей киске."
            else:
                "[Girl.Name] оглядывается по сторонам и прикладывает вибратор к своей киске."
            $ Girl.FaceChange("sexy",2,Eyes="closed")
            "Немного повозившись, она слегка вздрагивает, а затем убирает руку."
    elif Girl is JeanX: #skirt
            $ Girl.FaceChange("bemused",Eyes="psychic")
            if "vibein" in Girl.DailyActions:
                $ Line = "выскакивает у нее между ног"
                "Немного повозившись, она слегка вздрагивает, а затем расслабляется."
            else:
                $ Line = "заскакивает к ней между ног"
            if Girl.Legs:
                "Вы видите, как вибратор [Line]."
            elif Girl.HoseNum() >= 5:
                "Вы видите, как вибратор [Line]."
            elif Girl.Panties:
                "Вы видите, как вибратор [Line]."
            else:
                "Вы видите, как вибратор [Line]."
            $ Girl.FaceChange("sexy",2,Eyes="closed")
            if Line == "down to":
                    "Немного повозившись, она слегка вздрагивает, а затем расслабляется."
    else:
            $ Girl.FaceChange("bemused",1)
            if "vibein" in Girl.DailyActions:
                $ Line = ""
            else:
                $ Line = "берет вибратор и "
            if Girl.Legs:
                "[Girl.Name] [Line]засовывает руку в [get_clothing_name(Girl.Legs_key, vin)]."
            elif Girl.HoseNum() >= 5:
                "[Girl.Name] [Line]засовывает руку в [get_clothing_name(Girl.Hose_key, vin)]."
            elif Girl.Panties:
                "[Girl.Name] [Line]засовывает руку в [get_clothing_name(Girl.Panties_key, vin)]."
            elif "vibein" in Girl.DailyActions:
                "[Girl.Name]  опускает руку к своей киске и погружает пальцы внутрь."
            else:
                "[Girl.Name]  берет вибратор и засовывает его в свою киску."
            $ Girl.FaceChange("sexy",2,Eyes="closed")
            if "vibein" in Girl.DailyActions:
                "Она медленно вытаскивает вибратор."
            else:
                "Немного повозившись, она слегка вздрагивает, а затем убирает руку."

    if Girl.Taboo and not ApprovalCheck(Girl, 500, "OI", TabM = 5) and "exhibitionist" not in Girl.Traits:
            "Затем она оглядывается по сторонам, чтобы посмотреть, заметил ли кто-нибудь."
    $ Girl.FaceChange("sexy",1)

    if "vibein" in Girl.DailyActions:
            $ Girl.DailyActions.append("vibeout")
            $ Girl.DrainWord("vibein")
    else:
            $ Girl.DailyActions.append("vibein")
            $ Girl.Vib += 1
    return

label Insert_Vibrator(Girl = 0):  #rkeljsvgbdw
    if Girl not in TotalGirls:
            return
    $ Girl.Statup("Obed", 90, 1)
    $ Girl.Statup("Inbt", 90, 1)
    if Girl.Panties:
        "Вы подходите к [Girl.Name_dat] и вводите руку в ее [get_clothing_name(Girl.Panties_key, vin)]."
    elif Girl.Legs:
        "Вы подходите к [Girl.Name_dat] и вводите руку в ее [get_clothing_name(Girl.Legs_key, vin)]."
    elif Girl.HoseNum() >= 5:
        "Вы подходите к [Girl.Name_dat] и вводите руку в ее [get_clothing_name(Girl.Hose_key, vin)]."
    else:
        "Вы подходите к [Girl.Name_dat] и проводите рукой вниз по ее животу."
    if "vibein" in Girl.DailyActions:
            "Вы медленно достаете вибратор из ее теплой киски, а затем вытаскиваете руку обратно."
            $ Girl.DailyActions.append("vibeout")
            $ Girl.DrainWord("vibein")
    else:
            "Вы медленно вводите вибратор в ее теплую киску, а затем вытаскиваете руку обратно."
            $ Girl.DailyActions.append("vibein")
            $ Girl.Vib += 1

    if Girl.Taboo and not ApprovalCheck(Girl, 500, "OI", TabM = 5) and "exhibitionist" not in Girl.Traits:
            $ Girl.Statup("Obed", 90, 3)
            $ Girl.Statup("Inbt", 90, 3)
            "Затем она оглядывается по сторонам, чтобы посмотреть, заметил ли кто-нибудь."
    $ Girl.FaceChange("sexy",1)

    if Girl.Lust >= 50:
            menu:
                "У вас влажные пальцы. . ."
                "Вытереть их.":
                    "Вы вытираете свои пальцы."
                "Облизать их.":
                    $ Girl.Statup("Obed", 80, 1)
                    $ Girl.Statup("Inbt", 80, 3)
                    "Вы слизываете ее соки со своих пальцев."
                "Приложить их к ее губам.":
                    $ Girl.Statup("Inbt", 80, 2)
                    "Вы прикладываете свои пальцы к ее губам."
                    if ApprovalCheck(Girl, 1400) or Girl is WandaX:
                            $ Girl.Statup("Obed", 60, 3)
                            $ Girl.Statup("Obed", 90, 1)
                            "Она начинает нежно сосать их."
                    else:
                            $ Girl.Statup("Love", 60, -1)
                            $ Girl.Statup("Obed", 60, -1)
                            "Она отстраняется от них."
                            if Girl is RogueX:
                                    ch_r "Только не это."
                            elif Girl is KittyX:
                                    ch_k "Ах!"
                            elif Girl is EmmaX:
                                    ch_e "Мне это неинтересно."
                            elif Girl is LauraX:
                                    ch_l "Нет, спасибо."
                            elif Girl is StormX:
                                    ch_s "Меня такое не интересует."
                            elif Girl is JubesX:
                                    ch_v "Хех, извини."
                            elif Girl is GwenX:
                                    ch_g "Фу."
                            elif Girl is BetsyX:
                                    ch_b "Благодарю, но нет."
                            elif Girl is DoreenX:
                                    ch_d "Ох! Эм. . . нет. . ."
                            elif Girl is WandaX:
                                    ch_w "Ох! Нет, спасибо."
    return
# End Ask to insert vibrator / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start daily vibrator / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Daily_Vibrator(Girl=0): #rkeljsvgbdw
    ch_p "Ты должна носить этот вибратор каждый день."
    if not Girl.Vib:
            call AnyLine(Girl,"Что? \"Нет.\"")
            call AnyLine(Girl,"Я никогда даже не пробовала ничего подобного.")
    elif "vibrator" not in Girl.Inventory:
            call AnyLine(Girl,"Сначала мне нужен собственный вибратор.")

    elif (Girl.Vib >= 3 and ApprovalCheck(Girl, 1000, "OI")) or ApprovalCheck(Girl, 1400, "OI"):
            $ Girl.FaceChange("sly",1)
            if Girl is RogueX:
                    ch_r "Если ты настаиваешь."
            elif Girl is KittyX:
                    ch_k "Ладно."
            elif Girl is EmmaX:
                    ch_e "Если тебе этого хочется."
            elif Girl is LauraX:
                    ch_l "Ладно."
            elif Girl is JeanX:
                    ch_j "Ладно."
            elif Girl is StormX:
                    ch_s ". . . Хорошо."
            elif Girl is JubesX:
                    ch_v ". . . Ладно."
            elif Girl is GwenX:
                    ch_g "Ладно. . ."
            elif Girl is BetsyX:
                    ch_b "Если я должна."
            elif Girl is DoreenX:
                    ch_d "Ох. . . ладно. . ."
            elif Girl is WandaX:
                    ch_w "Хорошо."
            $ Girl.AddWord(1,0,0,"dailyvibe") #traits
            $ Girl.DailyActions.append("vibein")
    else:
            if "dailyvibe" in Girl.DailyActions:
                    call AnyLine(Girl,"Я сказала \"нет.\"")
            else:
                    call AnyLine(Girl,"Я бы предпочла этого не делать.")

    if "dailyvibe" not in Girl.DailyActions:
            if "dailyvibe" in Girl.Traits:
                    $ Girl.Statup("Obed", 60, 4)
                    $ Girl.Statup("Obed", 95, 2)
                    $ Girl.Statup("Inbt", 80, 2)
                    $ Girl.Statup("Lust", 80, 5)
            else:
                    $ Girl.Statup("Love", 90, -2)
                    $ Girl.Statup("Obed", 80, 1)
                    $ Girl.Statup("Inbt", 60, 2)
    $ Girl.AddWord(1,0,"dailyvibe") #daily
    return
# end daily vibrator / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Start daily plug / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Daily_Plug(Girl=0): #rkeljsvgbdw
    ch_p "Ты должна носить анальную пробку каждый день.y."
    if "plug" not in Girl.Inventory:
            call AnyLine(Girl,"Что?")
    elif not Girl.Plugged:
            call AnyLine(Girl,"Что? \"Нет.\"")
            call AnyLine(Girl,"Я никогда даже не пробовала ничего подобного.")

    elif (Girl.Plugged >= 3 and ApprovalCheck(Girl, 1200, "OI")) or ApprovalCheck(Girl, 1700, "OI"):
            $ Girl.FaceChange("sly",1)
            if Girl is RogueX:
                    ch_r "Если ты настаиваешь."
            elif Girl is KittyX:
                    ch_k "Ладно."
            elif Girl is EmmaX:
                    ch_e "Если тебе этого хочется."
            elif Girl is LauraX:
                    ch_l "Ладно."
            elif Girl is JeanX:
                    ch_j "Ладно."
            elif Girl is StormX:
                    ch_s ". . . Хорошо."
            elif Girl is JubesX:
                    ch_v ". . . Ладно."
            elif Girl is GwenX:
                    ch_g "Ладно. . ."
            elif Girl is BetsyX:
                    ch_b "Если я должна."
            elif Girl is DoreenX:
                    ch_d "Ох. . . ладно. . ."
            elif Girl is WandaX:
                    ch_w "Хорошо."
            $ Girl.AddWord(1,0,0,"dailyplug") #traits
            if not Girl.Plug:
                    show blackscreen onlayer black with dissolve
                    "Она ненадолго отходит, чтобы вставить ее в себя."
                    hide blackscreen onlayer black with dissolve
            $ Girl.Plug = 1
    else:
            if "dailyplug" in Girl.DailyActions:
                    call AnyLine(Girl,"Я сказала \"нет.\"")
            else:
                    call AnyLine(Girl,"Я бы предпочла этого не делать.")

    if "dailyplug" not in Girl.DailyActions:
            if "dailyplug" in Girl.Traits:
                    $ Girl.Statup("Obed", 60, 4)
                    $ Girl.Statup("Obed", 95, 2)
                    $ Girl.Statup("Inbt", 80, 2)
                    $ Girl.Statup("Lust", 80, 5)
            else:
                    $ Girl.Statup("Love", 90, -2)
                    $ Girl.Statup("Obed", 80, 1)
                    $ Girl.Statup("Inbt", 60, 2)
    $ Girl.AddWord(1,0,"dailyplug") #daily
    return
# end daily plug / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Favorite sex acts / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Favorite_Actions(Chr=0, Quick=0, Temp=0, ATemp=0, PTemp=0, BTemp=0, TTemp=0, HTemp=0, FTemp=0, D20F=0, BOptions=0):
    # Character is the selected girl
    # if there's no selected character, it does it for all girls
    # if Quick is True, it just returns a string of the action as a value, otherwise it sets it as a lasting variable.
    # if female, swaps fingering in for foot and cun for TJ.

    if Chr:
            $ BOptions = [Chr]
    else:
            $ BOptions = ActiveGirls[:]
            #cycles through each girl possible

    python:
        for BX in BOptions:
            #ass, pussy, blow, tits, hand, fondling, kiss
            ATemp = BX.Anal + BX.DildoA + BX.FondleA + BX.InsertA + BX.LickA
            PTemp = BX.Sex + BX.DildoP + BX.FondleP + BX.LickP
            BTemp = BX.Blow if Player.Male else BX.CUN
            TTemp = BX.Tit if Player.Male else 0
            XTemp = BX.Foot if Player.Male else 0
            HTemp = BX.Hand if Player.Male else BX.Finger
            FTemp = BX.FondleB + BX.FondleT + BX.SuckB + BX.Hotdog

            #This portion sets a bonus based on the player's favorite activity with her.
            if BX.PlayerFav and ApprovalCheck(BX, 1500):
                    if BX.PlayerFav == "anal":
                        ATemp += 20
                    elif BX.PlayerFav == "sex":
                        PTemp += 20
                    elif BX.PlayerFav == "blow" or BX.PlayerFav == "cun":
                        BTemp += 20
                    elif BX.PlayerFav == "tit":
                        TTemp += 20
                    elif BX.PlayerFav == "foot":
                        XTemp += 20
                    elif BX.PlayerFav == "hand" or BX.PlayerFav == "finger":
                        HTemp += 20
                    else:
                        FTemp += 20
            elif BX.PlayerFav and ApprovalCheck(Chr, 800):
                    if BX.PlayerFav == "anal":
                        ATemp += 5
                    elif BX.PlayerFav == "sex":
                        PTemp += 5
                    elif BX.PlayerFav == "blow" or BX.PlayerFav == "cun":
                        BTemp += 5
                    elif BX.PlayerFav == "tit":
                        TTemp += 5
                    elif BX.PlayerFav == "foot":
                        XTemp += 5
                    elif BX.PlayerFav == "hand" or BX.PlayerFav == "finger":
                        HTemp += 5
                    else:
                        FTemp += 5

            #This adds the numbers together to make a large number, then generates a random number between 1 and that total
            Total = ATemp + PTemp + BTemp + TTemp + HTemp + XTemp + FTemp + BX.Kissed
            if Total <= 0:
                D20F = 999
            else:
                D20F = renpy.random.randint(1, Total)

            # This selects a favorite activity based on which number is picked.
            if D20F <= ATemp:
                        #if the result is someplace under the "anal" category. . .
                        if BX.Anal >= 5:
                            Temp = "anal"
                        elif BX.LickA >= 5:
                            Temp = "lick ass"
                        else:
                            Temp = "insert ass"
            elif D20F <= ATemp + PTemp:
                        #if the result is someplace under the "sex" category. . .
                        if BX.Sex >= 5:
                            Temp = "sex"
                        elif BX.LickP >= 5:
                            Temp = "lick pussy"
                        else:
                            Temp = "fondle pussy"
            elif D20F <= ATemp + PTemp + BTemp:
                            Temp = "blow" if Player.Male else "cun"
            elif D20F <= ATemp + PTemp + BTemp + TTemp:
                            Temp = "tit" if Player.Male else "cun"
            elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp:
                            Temp = "foot" if Player.Male else "finger"
            elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp:
                            Temp = "hand" if Player.Male else "finger"
            elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp + FTemp:
                        #if the result failed the higher tier categories. . .
                        D20F = renpy.random.randint(1, 20)
                        if D20F >= 15 and BX.Hotdog:
                            Temp = "hotdog"
                        elif D20F >= 10 and BX.SuckB:
                            Temp = "suck breasts"
                        elif D20F >= 5 and BX.FondleB:
                            Temp = "fondle breasts"
                        else:
                            Temp = "fondle thighs"
            else:
                            Temp = "kiss you"
            if Quick:
                break
            BX.Favorite = Temp
    if Quick:
        return Temp
    return

# End favorite sex acts / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Gifts menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gifts: #rkeljsvgbdw
    # call Gifts(RogueX)
    $ Girl = GirlCheck(Girl)
    call Shift_Focus(Girl)
    while True:
            if not Player.Inventory:
                "Вам нечего ей подарить."
                return
            menu:
                "Что бы вы хотели ей подарить?"
                "Игрушки и книги":
                    menu:
                        "Подарить ей фаллоимитатор." if "dildo" in Player.Inventory:
                            #If you have a Dildo, you'll give it.
                            if "dildo" not in Girl.Inventory:
                                    "Вы протягиваете [Girl.Name_dat] фаллоимитатор."
                                    $ Girl.Blush = 1
                                    $ Girl.ArmPose = 2
                                    $ Girl.Held = "dildo"
                                    if ApprovalCheck(Girl, 800):
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove("dildo")
                                            $ Girl.Inventory.append("dildo")
                                            $ Girl.Statup("Love", 200, 30)
                                            $ Girl.Statup("Obed", 200, 30)
                                            $ Girl.Statup("Inbt", 200, 30)
                                            if Girl is RogueX:
                                                    ch_r "Ну, у меня появились кое-какие идеи на его счет. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Ох, отлично, я давно хотела такую штуку. . ."
                                            else:
                                                    call AnyLine(Girl,"Уверена, я найду для него место. . .")
                                            $ Girl.Statup("Lust", 89, 10)
                                    elif ApprovalCheck(Girl, 500):
                                            $ Girl.FaceChange("confused")
                                            $ Player.Inventory.remove("dildo")
                                            $ Girl.Inventory.append("dildo")
                                            if Girl is not EmmaX:
                                                    $ Girl.Statup("Love", 200, 10)
                                                    $ Girl.Statup("Obed", 200, 10)
                                                    $ Girl.Statup("Inbt", 200, 10)
                                            if Girl is RogueX:
                                                    ch_r "Хм, ну, думаю, я смогу найти для него применение. . ."
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("surprised")
                                                    ch_r "Я- Я. . . Я просто спрячу его."
                                            elif Girl is KittyX:
                                                    ch_k "Я не знаю, что. . ."
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("surprised")
                                                    ch_k "О!"
                                                    ch_k "Ох. . . Мне[Girl.like]нужно спрятать его."
                                            elif Girl is EmmaX:
                                                    ch_e "Студентам не следует дарить такое. . ."
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("sadside",1)
                                                    ch_e "Хм. . ."
                                                    $ Girl.Statup("Love", 200, 10)
                                                    $ Girl.Statup("Obed", 200, 10)
                                                    $ Girl.Statup("Inbt", 200, 10)
                                                    $ Girl.FaceChange("sly")
                                                    ch_e "Полагаю, я смогу найти для него {i}кое-какое{/i} применение. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Хм, ты даришь странные вещи."
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("smile")
                                                    ch_l "Хотя, думаю, он мне пригодится."
                                            elif Girl is JeanX:
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    ch_j "Ну, мы знаем, к чему ты клонишь."
                                                    $ Girl.FaceChange("smile")
                                                    ch_j "Наверное, я должна быть польщена. . ."
                                            elif Girl is StormX:
                                                    if StormX not in Rules:
                                                            $ Girl.FaceChange("sadside",1)
                                                            ch_s "Я не знаю, стоит ли мне принимать такое от студента. . ."
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    ch_s "Хм. . ."
                                                    $ Girl.FaceChange("sly")
                                                    ch_s "Благодарю за заботу. . ."
                                            elif Girl is JubesX:
                                                    ch_v "Думаю, я найду для него какое-нибудь применение. . ."
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("surprised")
                                                    ch_v "Я- я. . . я дополню им интерьер."
                                            elif Girl is GwenX:
                                                    ch_g "Ну. . ."
                                                    ch_g "Кажется, я не взяла с собой ни одного. . ."
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("smile")
                                                    ch_g "Спасибо, что заботишься обо мне?"
                                            elif Girl is BetsyX:
                                                    ch_b "Неплохо. . ."
                                                    ch_b "Пожалуй, я могу найти ему применение. . ."
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("smile")
                                                    ch_b "Спасибо, что заботишься обо мне?"
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. . . эм. . ."
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("smile")
                                                    $ Girl.FaceChange("smile")
                                            elif Girl is WandaX:
                                                    ch_w "Ого, смело."
                                                    $ Girl.Statup("Love", 200, 10)
                                                    $ Girl.Statup("Obed", 200, 10)
                                                    $ Girl.Statup("Inbt", 200, 10)
                                                    $ Girl.FaceChange("sly")
                                                    ch_w "Ладно, [Girl.Petname]."
                                            $ Girl.FaceChange("bemused")
                                    elif "offered gift" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry")
                                            "Она возвращает его вам."
                                            if Girl is RogueX:
                                                    ch_r "Слушай, может тебе стоит пересмотреть свой выбор подарков?"
                                            elif Girl is KittyX:
                                                    ch_k "Думаю, Я[Girl.like]ясно дала понять насчет неуместных подарков?"
                                            elif Girl is EmmaX:
                                                    ch_e "Думаю, я ясно выразилась насчет неуместных подарков?"
                                            elif Girl is LauraX:
                                                    ch_l "Я же говорила, что не могу принять нечто подобное."
                                            elif Girl is JeanX:
                                                    ch_j "Мне это совсем не нужно."
                                            elif Girl is StormX:
                                                    ch_s "Повторяю, это не то, что мне нужно."
                                            elif Girl is JubesX:
                                                    ch_v "Это совсем не то, что мне нужно. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Эм, думаю, мне и без него хорошо. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Боже. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Мне он не нужен."
                                            elif Girl is WandaX:
                                                    ch_w "Мне он совсем не нужен."
                                    else:
                                            $ Girl.FaceChange("angry")
                                            $ Girl.Statup("Love", 50, -20)
                                            $ Girl.Statup("Obed", 20, 10)
                                            $ Girl.Statup("Inbt", 20, 20)
                                            if Girl is RogueX:
                                                if Player.Male:
                                                    ch_r "Довольно самонадеянно дарить такое даме. . ."
                                                else:
                                                    ch_r "Лучше мне не знать, чем ты занимаешься в свободное время. . ."
                                            elif Girl is KittyX:
                                                    if Player.Male:
                                                            ch_k "Я- ты не должен дарить девушкам такие вещи!"
                                                    else:
                                                            ch_k "Я- тебе не следует дарить другим девушкам такие вещи!"
                                            elif Girl is EmmaX:
                                                    ch_e "[Girl.Petname], я не думаю, что это подходящий подарок для студента."
                                            elif Girl is LauraX:
                                                    if Player.Male:
                                                            ch_l "Не думаю, что стоит дарить такое первой встречной."
                                                    else:
                                                            ch_l "Странно получать такой подарок от другой девушки. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Ты что, просто ходишь и раздаешь всем секс-игрушки?"
                                            elif Girl is StormX:
                                                    ch_s "Я не понимаю, что ты под этим подразумеваешь."
                                            elif Girl is JubesX:
                                                    ch_v "Какой-то странный дизайн для. . . подожди-ка."
                                            elif Girl is GwenX:
                                                    ch_g "Мне не нравится, на что ты намекаешь!"
                                            elif Girl is BetsyX:
                                                    ch_b "В Америке. . . так принято?"
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. . . эм. . . Мне это не нужно."
                                            elif Girl is WandaX:
                                                    ch_w "Это довольно смелый подарок."
                                            $ Girl.Statup("Lust", 89, 5)
                                            "Она возвращает его вам."
                                            $ Girl.DailyActions.append("offered gift")
                            elif Girl.Inventory.count("dildo") == 1:
                                    $ Player.Inventory.remove("dildo")
                                    $ Girl.Inventory.append("dildo")
                                    if Girl is RogueX:
                                            ch_r "Ну, пожалуй, мне всегда пригодится еще один. . ."
                                    elif Girl is KittyX:
                                            ch_k "Ну да, зачем останавливаться на одном. . ."
                                    elif Girl is EmmaX:
                                            ch_e "Полагаю, у меня всегда найдется местечко для еще одного. . ."
                                    elif Girl is LauraX:
                                            ch_l "Не знаю, нужен ли мне еще один. . ."
                                    elif Girl is JeanX:
                                            ch_j "О, смотри ка, еще один резиновый член. . ."
                                    elif Girl is StormX:
                                            ch_s "О, еще один. . ."
                                    elif Girl is JubesX:
                                            ch_v "Мне больше не нужно. . ."
                                    elif Girl is GwenX:
                                            ch_g "Ладно, еще один. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Пожалуй, их никогда не бывает слишком много."
                                    elif Girl is DoreenX:
                                            ch_d "Ох. . .Эм. . . еще один. . ."
                                    elif Girl is WandaX:
                                            ch_w "Еще?"
                            else:
                                    if Girl is RogueX:
                                            ch_r "Если честно, [Girl.Petname], У меня их и так достаточно."
                                    elif Girl is KittyX:
                                            ch_k "У меня не так много места для их хранения."
                                    elif Girl is EmmaX:
                                            ch_e "Ты считаешь, я их коллекционирую?"
                                    elif Girl is LauraX:
                                            ch_l "У меня уже не хватает места для них."
                                    elif Girl is JeanX:
                                            if Player.Male:
                                                    ch_j "Как ты думаешь, сколько дырок у девушки?"
                                            else:
                                                    ch_j "Сколько у тебя дырок?"
                                    elif Girl is StormX:
                                            ch_s "Сомневаюсь, что смогу найти для него место."
                                    elif Girl is JubesX:
                                            ch_v "Это уже перебор. . ."
                                    elif Girl is GwenX:
                                            ch_g "Мне. . . Мне не нужно так много, остановись."
                                    elif Girl is BetsyX:
                                            ch_b "Честно говоря, я думаю, это уже перебор."
                                    elif Girl is DoreenX:
                                            ch_d "Ох. . . эм. . . у меня их уже слишком много."
                                    elif Girl is WandaX:
                                            ch_w "Думаю, у меня их уже достаточно, [Girl.Petname]."
                            $ Girl.Held = 0
                            $ Girl.ArmPose = 2

                        "Подарить ей вибратор." if "vibrator" in Player.Inventory:
                            #If you have a vibrator, you'll give it.
                            if "vibrator" not in Girl.Inventory:
                                "Вы протягиваете [Girl.Name_dat] вибратор."
                                $ Girl.Blush = 1
                                $ Girl.ArmPose = 2
                                $ Girl.Held = "vibrator"
                                if ApprovalCheck(Girl, 700):
                                        $ Girl.FaceChange("bemused")
                                        $ Player.Inventory.remove("vibrator")
                                        $ Girl.Inventory.append("vibrator")
                                        $ Girl.Statup("Love", 200, 30)
                                        $ Girl.Statup("Obed", 200, 30)
                                        $ Girl.Statup("Inbt", 200, 30)
                                        if Girl is RogueX:
                                                ch_r "Ну, у меня появились кое-какие идеи на его счет. . ."
                                        elif Girl is KittyX:
                                                ch_k "Это. . . [[бзззз]- "
                                                ch_k "-интересный подарок. . ."
                                        elif Girl is EmmaX:
                                                ch_e "Как мило с твоей стороны. . ."
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("sly")
                                                ch_e "Уверена, я смогу найти ему достойное применение. . ."
                                        elif Girl is LauraX:
                                                ch_l "Это. . . [[бзззз]- "
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("sly")
                                                ch_l "-какая-то секс-штучка, да?. . ."
                                        elif Girl is JeanX:
                                                ch_j "Ох, отлично."
                                        elif Girl is StormX:
                                                ch_s "Ох!. . . ооооххх."
                                        elif Girl is JubesX:
                                                ch_v "О, это может быть здорово. . ."
                                        elif Girl is GwenX:
                                                ch_g "Хм, хорошо, я могу с ним поработать. . ."
                                        elif Girl is BetsyX:
                                                ch_b "Ох, как интересно."
                                        elif Girl is DoreenX:
                                                ch_d "Думаю. . . думаю, я смогу найти ему применение. . ."
                                        elif Girl is WandaX:
                                                ch_w "Ох, он такой аккуратный."
                                        $ Girl.Statup("Lust", 89, 10)
                                elif ApprovalCheck(Girl, 400):
                                        $ Girl.FaceChange("confused")
                                        $ Player.Inventory.remove("vibrator")
                                        $ Girl.Inventory.append("vibrator")
                                        $ Girl.Statup("Love", 200, 10)
                                        $ Girl.Statup("Obed", 200, 10)
                                        $ Girl.Statup("Inbt", 200, 10)
                                        if Girl is RogueX:
                                                ch_r "Думаю, он мне пригодится. . ."
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("surprised")
                                                ch_r "Эм, при спазмах в мышцах!"
                                        elif Girl is KittyX:
                                                ch_k "Я слышала, что они очень расслабляют. . ."
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("surprised")
                                                ch_k "-пригодится для моей спины!"
                                        elif Girl is EmmaX:
                                                ch_e "Как мило с твоей стороны. . ."
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("sly")
                                                ch_e "полагаю, сгодится в качестве массажера для спины. . ."
                                        elif Girl is LauraX:
                                                ch_l "Это. . . [[бзззз]- "
                                                $ Girl.FaceChange("sly")
                                                $ Girl.Statup("Lust", 89, 10)
                                                ch_l "-ооох. . ."
                                        elif Girl is JeanX:
                                                ch_j "Хм. Ладно."
                                        elif Girl is StormX:
                                                ch_s "Ох, нечто для физических упражнений. . ."
                                        elif Girl is JubesX:
                                                ch_v "Спасибо, моя, эм, спина доканала меня. . ."
                                        elif Girl is GwenX:
                                                ch_g "Ох, эм. . . Думаю, он мне пригодится. . ."
                                        elif Girl is BetsyX:
                                                ch_b "Мне. . . мне нужно его спрятать. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Думаю. . . думаю, я смогу найти ему применение. . ."
                                        elif Girl is WandaX:
                                                ch_w "Ох, он такой аккуратный."
                                        $ Girl.FaceChange("bemused", 1)
                                elif "offered gift" in Girl.DailyActions:
                                        $ Girl.FaceChange("angry")
                                        "Она возвращает его вам."
                                        if Girl is RogueX:
                                                ch_r "Слушай, может тебе стоит пересмотреть свой выбор подарков?"
                                        elif Girl is KittyX:
                                                ch_k "Думаю, я[Girl.like]ясно дала понять насчет неуместных подарков?"
                                        elif Girl is EmmaX:
                                                ch_e "Думаю, я ясно выразилась насчет неуместных подарков?"
                                        elif Girl is LauraX:
                                                ch_l "Мне он не нужен."
                                        elif Girl is JeanX:
                                                ch_j "Мне он совсем не нужен."
                                        elif Girl is StormX:
                                                ch_s "Повторяю, это не то, что мне нужно."
                                        elif Girl is JubesX:
                                                ch_v "Я не нуждаюсь в нем. . ."
                                        elif Girl is GwenX:
                                                ch_g "Мне. . . Мне он совсем не нужен. . ."
                                        elif Girl is BetsyX:
                                                ch_b "Сомневаюсь, что смогу найти ему применение."
                                        elif Girl is DoreenX:
                                                ch_d "Мне такое -совсем- не нужно. . ."
                                        elif Girl is WandaX:
                                                ch_w "Мне он не нужен."
                                else:
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 50, -20)
                                        $ Girl.Statup("Obed", 20, 10)
                                        $ Girl.Statup("Inbt", 20, 20)
                                        if Girl is RogueX:
                                                ch_r "Не думаю, что это мне пригодится."
                                        elif Girl is KittyX:
                                                ch_k "Я не вижу в нем смысла."
                                        elif Girl is EmmaX:
                                                ch_e "[Girl.Petname], я не думаю, что это подходящий подарок для студента."
                                        elif Girl is LauraX:
                                                ch_l "Мне он не нужен."
                                        elif Girl is JeanX:
                                                ch_j "Хм. Нет, мне он не нужен."
                                        elif Girl is StormX:
                                                ch_s "Для меня этот подарок бесполезен."
                                        elif Girl is JubesX:
                                                ch_v "Убери его подальше. . ."
                                        elif Girl is GwenX:
                                                ch_g "Эй! Не будь таким вульгарным!"
                                        elif Girl is BetsyX:
                                                ch_b "Ты меня оскорбляешь."
                                        elif Girl is DoreenX:
                                                ch_d "Мне. . . мне он не нужен. . ."
                                        elif Girl is WandaX:
                                                ch_w "Это неподходящий подарок."
                                        $ Girl.Statup("Lust", 89, 5)
                                        "Она возвращает его вам."
                                        $ Girl.DailyActions.append("offered gift")
                            else:
                                        if Girl is RogueX:
                                            ch_r "[Girl.Petname], мне нужен только один."
                                        elif Girl is EmmaX:
                                            ch_e "У меня их и так предостаточно."
                                        else:
                                            call AnyLine(Girl,"У меня уже есть один.")
                            $ Girl.Held = 0
                            $ Girl.ArmPose = 2

                        "Подарить ей анальную пробку." if "plug" in Player.Inventory:
                            #If you have a vibrator, you'll give it.
                            if "plug" not in Girl.Inventory:
                                "Вы дарите [Girl.Name_dat] анальную пробку."
                                $ Girl.Blush = 1
                                $ Girl.ArmPose = 2
                                if ApprovalCheck(Girl, 1400) and (Girl.Anal or Girl.DildoA):
                                        $ Girl.FaceChange("bemused")
                                        $ Player.Inventory.remove("plug")
                                        $ Girl.Inventory.append("plug")
                                        $ Girl.Statup("Love", 200, 10)
                                        $ Girl.Statup("Obed", 200, 35)
                                        $ Girl.Statup("Inbt", 200, 30)
                                        if Girl is RogueX:
                                                ch_r "Думаю, у тебя уже есть пару идей для ее применения. . ."
                                        elif Girl is KittyX:
                                                ch_k "Хммм. . ."
                                        elif Girl is EmmaX:
                                                ch_e "Вижу, у тебя есть на ее счет планы. . ."
                                                $ Girl.Statup("Lust", 89, 10)
                                        elif Girl is LauraX:
                                                ch_l "Ох. . ."
                                        elif Girl is JeanX:
                                                ch_j "Ох, я думаю, ты планируешь как-нибудь воспользоваться ею?"
                                        elif Girl is StormX:
                                                ch_s "Ты хочешь, чтобы я использовала ее?"
                                        elif Girl is JubesX:
                                                ch_v "Ох, она для. . ?"
                                        elif Girl is GwenX:
                                                ch_g "Она вставляется в- . . ох. . ."
                                        elif Girl is BetsyX:
                                                ch_b "Боже! Какой неприличный подарок. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Я. . . ох. . ."
                                        elif Girl is WandaX:
                                                ch_w "Ого. Какой пикантный подарок."
                                        $ Girl.Statup("Lust", 89, 10)
                                elif ApprovalCheck(Girl, 1100):
                                        $ Girl.FaceChange("confused")
                                        $ Player.Inventory.remove("plug")
                                        $ Girl.Inventory.append("plug")
                                        $ Girl.Statup("Obed", 200, 15)
                                        $ Girl.Statup("Inbt", 200, 10)
                                        if Girl is RogueX:
                                                ch_r "Это же. . . я сохраню ее для тебя. . ."
                                                ch_r "-но не думай, что я сама буду пользоваться ей. . ."
                                        elif Girl is KittyX:
                                                ch_k "Думаю, я могла бы взять ее, но не уверена, что я[Girl.Like]буду пользоваться ей. . ."
                                        elif Girl is EmmaX:
                                                ch_e "Я могу придержать ее на случай, если она тебе для чего-нибудь понадобится."
                                        elif Girl is LauraX:
                                                ch_l "Думаю, я могу придержать ее для тебя. . ."
                                        elif Girl is JeanX:
                                                ch_j "Ты хочешь, чтобы я использовала ее на тебе, или. . ."
                                        elif Girl is StormX:
                                                ch_s "Я могу придержать ее, если хочешь."
                                        elif Girl is JubesX:
                                                ch_v ". . . Не думаю, что она нужна мне, но я могу придержать ее. . ."
                                        elif Girl is GwenX:
                                                ch_g "Я. . . убери ее! . . Ладно, я сама уберу ее!"
                                        elif Girl is BetsyX:
                                                ch_b "Я. . . заберу ее у тебя."
                                        elif Girl is DoreenX:
                                                ch_d "Что это, желудь? . . Ох. . ."
                                        elif Girl is WandaX:
                                                ch_w "Ого. Какой пикантный подарок."
                                        $ Girl.FaceChange("bemused", 1)
                                elif "offered gift" in Girl.DailyActions:
                                        $ Girl.FaceChange("angry")
                                        "Она возвращает ее вам."
                                        if Girl is RogueX:
                                                ch_r "Слушай, может тебе стоит пересмотреть свой выбор подарков?"
                                        elif Girl is KittyX:
                                                ch_k "Думаю, Я[Girl.like]ясно дала понять насчет неуместных подарков?"
                                        elif Girl is EmmaX:
                                                ch_e "Думаю, я ясно выразилась насчет неуместных подарков?"
                                        elif Girl is LauraX:
                                                ch_l "Я не хочу ее."
                                        elif Girl is JeanX:
                                                ch_j "Мне она совсем не нужна."
                                        elif Girl is StormX:
                                                ch_s "Повторяю, это не то, что мне нужно."
                                        elif Girl is JubesX:
                                                ch_v "Я не нуждаюсь в ней. . ."
                                        elif Girl is GwenX:
                                                ch_g "Мне она совсем не нужна. . ."
                                        elif Girl is BetsyX:
                                                ch_b "Бесполезный подарок."
                                        elif Girl is DoreenX:
                                                ch_d "Мне это не нужно. . ."
                                        elif Girl is WandaX:
                                                ch_w "Мне это не нужно."
                                else:
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 50, -20)
                                        $ Girl.Statup("Obed", 20, 10)
                                        $ Girl.Statup("Inbt", 20, 20)
                                        if Girl is RogueX:
                                                ch_r "Я не собираюсь ничего засовывать себе в задницу."
                                        elif Girl is KittyX:
                                                ch_k "Я не хочу ничего подобного!"
                                        elif Girl is EmmaX:
                                                ch_e "Я не понимаю, почему ты думаешь, что мне нужна такая вещь."
                                        elif Girl is LauraX:
                                                ch_l "Мне она не нужна."
                                        elif Girl is JeanX:
                                                ch_j "Хм. Нет, мне она не нужна."
                                        elif Girl is StormX:
                                                ch_s "Для меня этот подарок бесполезен."
                                        elif Girl is JubesX:
                                                ch_v "Убери ее подальше. . ."
                                        elif Girl is GwenX:
                                                ch_g "Что это- ахх!"
                                        elif Girl is BetsyX:
                                                ch_b "Ты желаешь оскорбить меня?"
                                        elif Girl is DoreenX:
                                                ch_d "Мне. . . не нужно ничего подобного. . ."
                                        elif Girl is WandaX:
                                                ch_w "Слушай, зачем ты даешь мне это?"
                                        $ Girl.Statup("Lust", 89, 5)
                                        "Она возвращает ее вам."
                                        $ Girl.DailyActions.append("offered gift")
                            else:
                                        call AnyLine(Girl,"У меня уже есть одна.")
                            $ Girl.Held = 0
                            $ Girl.ArmPose = 2

                        "Подарить ей книгу \"Ослепительная и Счастливчик\"." if "Dazzler and Longshot" in Player.Inventory:
                            #If you have a the book, you'll give it.
                            if "Dazzler and Longshot" not in Girl.Inventory:
                                "Вы протягиваете [Girl.Name_tvo] книгу."
                                $ Girl.Blush = 1
                                if ApprovalCheck(Girl, 600, "L"):
                                        $ Girl.FaceChange("smile")
                                        if Girl is RogueX:
                                                ch_r "О, я слышала о ней. Говорят, это увлекательная история любви!"
                                        elif Girl is KittyX:
                                                ch_k "Ох, это так мило!"
                                        elif Girl is EmmaX:
                                                $ Girl.FaceChange("angry")
                                                ch_e "Так ты подобного ожидаешь от меня. . ."
                                                $ Girl.FaceChange("sadside", Mouth="lipbite")
                                                ch_e "посмотрим, как у нас все сложится. . ."
                                        elif Girl is LauraX:
                                                ch_l "Любовная история?"
                                        elif Girl is JeanX:
                                                ch_j "Ох. . . роман. . ."
                                        elif Girl is StormX:
                                                ch_s "Ты знаешь толк в романах?"
                                        elif Girl is JubesX:
                                                ch_v "Знаешь, у нас с Ослепительной много общего. . ."
                                        elif Girl is GwenX:
                                                ch_g "Ох, как в 80-ых? . ."
                                        elif Girl is BetsyX:
                                                ch_b "Ох, мне подобное всегда нравилось. . ."
                                        elif Girl is DoreenX:
                                                ch_d "По-моему, это очень милый подарок. . ."
                                        elif Girl is WandaX:
                                                ch_w "Я слышала, что это очень душевная история."
                                        $ Girl.Statup("Lust", 89, 10)
                                else:
                                        $ Girl.FaceChange("confused")
                                        if Girl is RogueX:
                                                ch_r "Ну, я слышала о ней много хорошего, попробую почитать."
                                        elif Girl is KittyX:
                                                ch_k "Хм, думаю, стоит почитать."
                                        elif Girl is EmmaX:
                                                $ Girl.FaceChange("angry")
                                                ch_e "Я не очень-то разбираюсь в этом дешевом мусоре. . ."
                                                $ Girl.FaceChange("sadside", Mouth="lipbite")
                                                ch_e "но я возьму ее. . ."
                                        elif Girl is LauraX:
                                                ch_l "Хм. А фильм есть?"
                                        elif Girl is JeanX:
                                                ch_j "На что ты намекаешь?"
                                        elif Girl is StormX:
                                                ch_s "Фильм мне понравился. . ."
                                        elif Girl is JubesX:
                                                ch_v "Ты хочешь сказать, что я похожа на нее?"
                                        elif Girl is GwenX:
                                                ch_g "Я больше предпочитаю оригинал. . ."
                                        elif Girl is BetsyX:
                                                ch_b "Я нахожу этих двоих довольно скучными."
                                        elif Girl is DoreenX:
                                                ch_d "Ох. Это очень милый подарок. . ."
                                        elif Girl is WandaX:
                                                ch_w "Я слышала, что это очень душевная история."
                                        $ Girl.FaceChange("bemused")
                                $ Player.Inventory.remove("Dazzler and Longshot")
                                $ Girl.Inventory.append("Dazzler and Longshot")
                                $ Girl.Statup("Love", 200, 50)
                            else:
                                if Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Ты уже дарила мне ее."
                                        else:
                                            ch_e "Ты уже дарил мне ее."
                                else:
                                        call AnyLine(Girl,"У меня уже есть такая.")

                        "Подарить книгу \"256 Оттенков Серого\"." if "256 Shades of Grey" in Player.Inventory:
                            #If you have a book, you'll give it.
                            if "256 Shades of Grey" not in Girl.Inventory:
                                "Вы протягиваете [Girl.Name_tvo] книгу."
                                $ Girl.Blush = 1
                                if ApprovalCheck(Girl, 500, "O"):
                                        $ Girl.FaceChange("bemused")
                                        if Girl is RogueX:
                                                ch_r "Я внимательно ее изучу."
                                        elif Girl is KittyX:
                                                ch_k "Я ее хорошенько изучу."
                                        elif Girl is EmmaX:
                                                ch_e "Думаю, она будет в какой-то степени занимательной."
                                        elif Girl is LauraX:
                                                ch_l "Похоже на какую-то похабщину."
                                        elif Girl is JeanX:
                                                ch_j "Ха!"
                                                ch_j "О, блин, интересные выйдут выходные. . ."
                                                $ Girl.Statup("Love", 50, 5)
                                                $ Girl.Statup("Love", 90, 3)
                                                $ Girl.Statup("Obed", 200, 5)
                                                ch_j "Хочешь попробовать что-нибудь из этой книги?"
                                        elif Girl is StormX:
                                                ch_s "Ох, ты серьезно?"
                                        elif Girl is JubesX:
                                                ch_v "Странное чтиво. . ."
                                        elif Girl is GwenX:
                                                ch_g "Подожди, это типа. . . О, я поняла, чего ты хочешь."
                                        elif Girl is BetsyX:
                                                ch_b "Там главная героиня похотливая маленькая девочка, так?"
                                        elif Girl is DoreenX:
                                                ch_d "Я слышала о ней. . ."
                                        elif Girl is WandaX:
                                                ch_w "Так вот чем занимается главная героиня?"
                                        $ Girl.Statup("Lust", 89, 10)
                                else:
                                        $ Girl.FaceChange("confused")
                                        if Girl is RogueX:
                                                ch_r "Хмм. Я слышала кое-что хорошее о ней. Думаю, я ее быстро прочитаю."
                                        elif Girl is KittyX:
                                                ch_k "Хм, думаю, я могла бы прочитать несколько глав."
                                        elif Girl is EmmaX:
                                                ch_e "Я слышала о ней."
                                        elif Girl is LauraX:
                                                ch_l "Загляну в нее."
                                        elif Girl is JeanX:
                                                ch_j "Ха!"
                                                ch_j "О, блин, интересные выйдут выходные. . ."
                                                $ Girl.Statup("Love", 50, -5)
                                                $ Girl.Statup("Obed", 200, 5)
                                                $ Girl.Statup("Inbt", 200, -5)
                                                if not Player.Male:
                                                    ch_j "Подожди, ты что, читала ее?"
                                                else:
                                                    ch_j "Подожди, ты что, читал ее?"
                                        elif Girl is StormX:
                                                ch_s "Я думаю, что мне нужно поговорить с той девушкой. . ."
                                        elif Girl is JubesX:
                                                ch_v "Для меня подобное чтиво немного мрачновато. . ."
                                        elif Girl is GwenX:
                                                ch_g "Мне не нужны плохие фанфики. . ."
                                        elif Girl is BetsyX:
                                                ch_b "На мой вкус, это немного пресноватое чтиво."
                                        elif Girl is DoreenX:
                                                ch_d "Ох. Я слышала о ней. . ."
                                        elif Girl is WandaX:
                                                ch_w "Ох, так вот чем занимается главная героиня?"
                                        $ Girl.FaceChange("bemused")
                                $ Player.Inventory.remove("256 Shades of Grey")
                                $ Girl.Inventory.append("256 Shades of Grey")
                                $ Girl.Statup("Obed", 200, 50,Alt=[[JeanX],200,10])
                            else:
                                if Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Ты уже дарила мне ее."
                                        else:
                                            ch_e "Ты уже дарил мне ее."
                                else:
                                        call AnyLine(Girl,"У меня уже есть такая.")

                        "Подарить книгу \"Пентхаус Башни Мстителей\"." if "Avengers Tower Penthouse" in Player.Inventory:
                            #If you have a book, you'll give it.
                            if "Avengers Tower Penthouse" not in Girl.Inventory:
                                "Вы протягиваете [Girl.Name_dat] книгу."
                                $ Girl.Blush = 1
                                if ApprovalCheck(Girl, 500, "I"):
                                        $ Girl.FaceChange("bemused")
                                        if Girl is RogueX:
                                                ch_r "Ох. . . Думаю, она мне понравится. . ."
                                        elif Girl is KittyX:
                                                ch_k "Она должна быть. . . интересной. . ."
                                        elif Girl is EmmaX:
                                                ch_e "В ближайшее время, не заходи ко мне без предупреждения. . ."
                                        elif Girl is LauraX:
                                                ch_l "Она довольно клевая. . ."
                                        elif Girl is JeanX:
                                                ch_j "Ну здравствуй, Мистер Роджерс. . ."
                                        elif Girl is StormX:
                                                ch_s "Ох, она очень. . . откровенная. . ."
                                        elif Girl is JubesX:
                                                ch_v "Вау. . .  просто вау. . ."
                                        elif Girl is GwenX:
                                                ch_g "Ох, ого, Кэрол, ты такая потаскуха. . ."
                                        elif Girl is BetsyX:
                                                ch_b "Ох, замечательно."
                                        elif Girl is DoreenX:
                                                ch_d "Ох. . . ого. . ."
                                        elif Girl is WandaX:
                                                ch_w "Ох, эм. . . думаешь, мне стоит ее прочесть?"
                                        $ Girl.Statup("Lust", 89, 10)
                                else:
                                        $ Girl.FaceChange("confused")
                                        if Girl is RogueX:
                                                ch_r "Ну. . . она немного. . . хм, думаю, ее надо получше изучить."
                                        elif Girl is KittyX:
                                                ch_k "Ну. . . она немного... хм, может, я смогу кое-чему из нее научиться."
                                        elif Girl is EmmaX:
                                                ch_e "Обычно я конфискую такие вещи. . . Так и сейчас сделаю. . ."
                                        elif Girl is LauraX:
                                                ch_l "Эм. . . ладно."
                                        elif Girl is JeanX:
                                                ch_j "Оох, странная книжка. . ."
                                        elif Girl is StormX:
                                                ch_s "О. . . боже. . ."
                                        elif Girl is JubesX:
                                                ch_v "Эм, она вроде как. . . слишком. . ."
                                        elif Girl is GwenX:
                                                ch_g "Я конфискую ее, спасибо."
                                        elif Girl is BetsyX:
                                                ch_b "Серьезно?"
                                        elif Girl is DoreenX:
                                                ch_d "Безумный подарок. . . но спасибо. . ."
                                        elif Girl is WandaX:
                                                ch_w "Ох, эм. . . думаешь, мне стоит ее прочесть?"
                                        $ Girl.FaceChange("bemused")
                                $ Player.Inventory.remove("Avengers Tower Penthouse")
                                $ Girl.Inventory.append("Avengers Tower Penthouse")
                                $ Girl.Statup("Inbt", 200, 50)
                            else:
                                if Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Ты уже дарила мне ее."
                                        else:
                                            ch_e "Ты уже дарил мне ее."
                                else:
                                        call AnyLine(Girl,"У меня уже есть такая.")

                        "Неважно":
                            pass
                #End Toys and Books

                "Одежда":
                    menu:
                        "Подарить ей зеленую ночнушку." if Girl.Tag + " nighty" in Player.Inventory:
                                #If you have a nighty, you'll give it.
                                if "nighty" not in Girl.Inventory:
                                    "Вы протягиваете [Girl.Name_dat] ночнушку."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 600):
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " nighty")
                                            $ Girl.Inventory.append("nighty")
                                            $ Girl.Statup("Love", 200, 40)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 30)
                                            ch_r "Уверена, она будет хорошо смотреться на мне. . ."
                                            $ Girl.Statup("Lust", 89, 10)
                                    else:
                                            $ Girl.FaceChange("confused")
                                            $ Player.Inventory.remove(Girl.Tag + " nighty")
                                            $ Girl.Inventory.append("nighty")
                                            $ Girl.Statup("Love", 200, 30)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 20)
                                            ch_r "Ну, хоть она и слегка откровенная, но все равно очень милая."
                                            $ Girl.FaceChange("bemused")
                                else:
                                            call AnyLine(Girl,"У меня уже есть такая.")

                        "Подарить ей корсет." if Girl.Tag + " corset" in Player.Inventory:
                                #If you have a bra, you'll give it.
                                if "corset" not in Girl.Inventory:
                                    "Вы протягиваете [Girl.Name_dat] корсет."
                                    if ApprovalCheck(Girl, 1000):
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                            $ Girl.Inventory.append("corset")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 10)
                                            if Girl is LauraX:
                                                    if not Player.Male:
                                                        ch_l "Я буду хорошо выглядеть в нем, согласна?"
                                                    else:
                                                        ch_l "Я буду хорошо выглядеть в нем, согласен?"
                                            elif Girl is JeanX:
                                                    ch_j "Ладно, я могу его примерить. . ."
                                            $ Girl.Statup("Lust", 89, 10)
                                    elif ApprovalCheck(Girl, 700) or Girl is JeanX:
                                            $ Girl.FaceChange("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                            $ Girl.Inventory.append("corset")
                                            $ Girl.Statup("Love", 200, 15)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 10)
                                            if Girl is LauraX:
                                                    ch_l "Он. . . вроде бы клевый. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Спасибо?"
                                            $ Girl.FaceChange("bemused",1)
                                    elif ApprovalCheck(Girl, 600):
                                            $ Girl.FaceChange("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                            $ Girl.Inventory.append("corset")
                                            $ Girl.Statup("Love", 200, 10)
                                            $ Girl.Statup("Obed", 200, 15)
                                            $ Girl.Statup("Inbt", 200, 15)
                                            if Girl is LauraX:
                                                    if not Player.Male:
                                                        ch_l "Не знаю, зачем ты мне его подарила, я все равно не буду его носить. . ."
                                                    else:
                                                        ch_l "Не знаю, зачем ты мне его подарил, я все равно не буду его носить. . ."
                                            $ Girl.FaceChange("bemused",1)
                                    elif "no gift bra" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            if Girl is LauraX:
                                                    ch_l "Я только что сказала тебе, нет."
                                    else:
                                            $ Girl.FaceChange("angry",2)
                                            $ Girl.Statup("Love", 50, -10)
                                            $ Girl.Statup("Obed", 20, 10)
                                            $ Girl.Statup("Inbt", 20, 20)
                                            if "no gift panties" in Girl.DailyActions:
                                                if Girl is LauraX:
                                                        ch_l "Это я тоже не хочу."
                                            else:
                                                if Girl is LauraX:
                                                        ch_l "У тебя слишком много свободного времени."
                                            $ Girl.Statup("Lust", 89, 5)
                                            $ Girl.Blush = 1
                                            "Она возвращает его вам."
                                            $ Girl.RecentActions.append("no gift bra")
                                            $ Girl.DailyActions.append("no gift bra")
                                else:
                                            call AnyLine(Girl,"У меня уже есть такой.")
                        #End Corset

                        "Подарить ей кружевной корсет." if Girl.Tag + " lace corset" in Player.Inventory:
                                #If you have a bra, you'll give it.
                                if "lace corset" not in Girl.Inventory:
                                    "Вы протягиваете [Girl.Name_dat] кружевной корсет."
                                    if ApprovalCheck(Girl, 1200):
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                            $ Girl.Inventory.append("lace corset")
                                            $ Girl.Statup("Love", 200, 25)
                                            $ Girl.Statup("Obed", 200, 30)
                                            $ Girl.Statup("Inbt", 200, 20)
                                            ch_l "Думаешь, он будет хорошо смотреться на мне?"
                                            $ Girl.Statup("Lust", 89, 10)
                                    elif ApprovalCheck(Girl, 1000):
                                            $ Girl.FaceChange("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                            $ Girl.Inventory.append("lace corset")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 30)
                                            $ Girl.Statup("Inbt", 200, 15)
                                            ch_l "Он. . . довольно прозрачный. . ."
                                            $ Girl.FaceChange("bemused",1)
                                    elif ApprovalCheck(Girl, 800):
                                            $ Girl.FaceChange("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                            $ Girl.Inventory.append("lace corset")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 25)
                                            if not Player.Male:
                                                ch_l "Не знаю, зачем ты мне его подарила, я все равно не буду его носить. . ."
                                            else:
                                                ch_l "Не знаю, зачем ты мне его подарил, я все равно не буду его носить. . ."
                                            $ Girl.FaceChange("bemused",1)
                                    elif "no gift bra" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            ch_l "Я только что сказала тебе, нет."
                                    else:
                                            $ Girl.FaceChange("angry",2)
                                            $ Girl.Statup("Love", 50, -10)
                                            $ Girl.Statup("Obed", 20, 10)
                                            $ Girl.Statup("Inbt", 20, 20)
                                            if "no gift panties" in Girl.DailyActions:
                                                ch_l "Это я тоже не хочу."
                                            else:
                                                ch_l "У тебя слишком много свободного времени."
                                            $ Girl.Statup("Lust", 89, 5)
                                            $ Girl.Blush = 1
                                            "Она возвращает его вам."
                                            $ Girl.RecentActions.append("no gift bra")
                                            $ Girl.DailyActions.append("no gift bra")
                                else:
                                            call AnyLine(Girl,"У меня уже есть такой.")
                        #End Lace Corset

                        "Подарить ей кружевной лифчик." if Girl.Tag + " lace bra" in Player.Inventory:
                                #If you have a bra, you'll give it. (not laura)
                                if "lace bra" not in Girl.Inventory:
                                    "Вы протягиваете [Girl.Name_dat] кружевной лифчик."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 1000) or Girl is JeanX:
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace bra")
                                            $ Girl.Inventory.append("lace bra")
                                            $ Girl.Statup("Love", 200, 30)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 30)
                                            if Girl is RogueX:
                                                    ch_r "Хмм, а он довольно хорошо подчеркивает мои достоинства. . ."
                                            elif Girl is KittyX:
                                                    ch_k "По крайней мере, ты ценишь мои достоинства."
                                            elif Girl is EmmaX:
                                                    ch_e "Я впечатлена, ты правильно подобрал размер. . ."
                                            elif Girl is JeanX:
                                                    ch_j "У тебя хороший вкус. . ."
                                            elif Girl is StormX:
                                                    ch_s "Как думаешь, мне он подойдет?"
                                            elif Girl is JubesX:
                                                    ch_v "Тебе понравится, как он будет выглядеть на мне. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Ох, он такой милый. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Он пркрасен."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. Выглядит очень мило!"
                                            elif Girl is WandaX:
                                                    ch_w "Он очень милый."
                                            $ Girl.Statup("Lust", 89, 10)
                                    elif ApprovalCheck(Girl, 700,Alt=[[EmmaX],600]):
                                            $ Girl.FaceChange("confused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace bra")
                                            $ Girl.Inventory.append("lace bra")
                                            $ Girl.Statup("Love", 200, 25)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 20)
                                            if Girl is RogueX:
                                                    ch_r "Не знаю, надену ли я его, ну, может быть, наедине."
                                            elif Girl is KittyX:
                                                    ch_k "Он. . . просвечивает. . ."
                                                    ch_k "Не знаю, зачем ты мне его подарил, я все равно не буду его носить. . ."
                                            elif Girl is EmmaX:
                                                    if ApprovalCheck(Girl, 700):
                                                        ch_e "У меня прилично таких вещей. . ."
                                                    else:
                                                        ch_e "Это. . . необычный подарок для студента. . ."
                                            elif Girl is StormX:
                                                    ch_s "Не то, чтобы я не ценила твой жест, но. . ."
                                            elif Girl is JubesX:
                                                    ch_v "Он не в моем обычном стиле. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Эм, спасибо за подарок? . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Выглядит. . . довольно мило. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Он немного откровенный. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Ох, такой сексуальный. . ."
                                    elif "no gift bra" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            if Girl is RogueX:
                                                    ch_r "Ты даже не можешь дать мне 24 часа?!"
                                            elif Girl is KittyX:
                                                    ch_k "Я не передумала, хватит меня беспокоить!"
                                            elif Girl is EmmaX:
                                                    ch_e "Я все еще не считаю его подходящим подарком для студента."
                                            elif Girl is StormX:
                                                    ch_s "Мне все еще он не нужен."
                                            elif Girl is JubesX:
                                                    ch_v "Серьезно, это уже чересчур. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Мне он совсем не нужен. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Мне он не нужен."
                                            elif Girl is DoreenX:
                                                    ch_d "Я не могу его надеть."
                                            elif Girl is WandaX:
                                                    ch_w "Хех, оставь его пока в покое."
                                    else:
                                            $ Girl.FaceChange("angry")
                                            $ Girl.Statup("Love", 50, -20)
                                            $ Girl.Statup("Obed", 20, 10)
                                            $ Girl.Statup("Inbt", 20, 20)
                                            if Girl is RogueX:
                                                    if "no gift panties" in Girl.DailyActions:
                                                        ch_r "Мне это тоже не нужно!"
                                                    else:
                                                        ch_r "Я не знаю, почему ты так сосредоточен на моей груди, [Girl.Petname]"
                                            elif Girl is KittyX:
                                                    if "no gift panties" in Girl.DailyActions:
                                                        ch_k "Мне это тоже не нужно!"
                                                    else:
                                                        ch_k "Просто. . . просто перестань думать о моей груди!"
                                            elif Girl is EmmaX:
                                                    if "no gift panties" in Girl.DailyActions:
                                                        ch_e "Это ничуть не лучше твоего прошлого предложения."
                                                    else:
                                                        ch_e "Не думаю, что тебе стоит так зацикливаться на моей груди."
                                            elif Girl is StormX:
                                                    ch_s "Мне ни к чему обновлять гардероб."
                                            elif Girl is JubesX:
                                                    ch_v "Я однозначно этого не хочу. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Мне это не нужно. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Думаю, я в состоянии сама купить себе одежду."
                                            elif Girl is DoreenX:
                                                    ch_d "Не думаю, что это мне подойдет."
                                            elif Girl is WandaX:
                                                    ch_w "Эм, нет, спасибо, может быть, в другой раз."
                                            $ Girl.Statup("Lust", 89, 5)
                                            "Она возвращает его вам."
                                            $ Girl.RecentActions.append("no gift bra")
                                            $ Girl.DailyActions.append("no gift bra")
                                    $ Girl.FaceChange("bemused")
                                else:
                                            call AnyLine(Girl,"У меня уже есть такой.")
                        #End Lace Bra

                        "Подарить ей кружевные трусики." if Girl.Tag + " lace panties" in Player.Inventory:
                                #If you have panties, you'll give it.
                                if "lace panties" not in Girl.Inventory:
                                    "Вы протягиваете [Girl.Name_dat] кружевные трусики."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 1100) or Girl is JeanX:
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace panties")
                                            $ Girl.Inventory.append("lace panties")
                                            $ Girl.Statup("Love", 200, 30)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 30)
                                            if Girl is RogueX:
                                                    ch_r "Хмм, они вообще ничего не прикрывают. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Они не оставляют ничего для воображения. . ."
                                            elif Girl is EmmaX:
                                                    ch_e "Неплохое дополнение для моего гардероба. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Красивые. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Ох, они очень милые. . ."
                                            elif Girl is StormX:
                                                    ch_s "Так, ты думаешь, я бы хорошо в них смотрелась?"
                                            elif Girl is JubesX:
                                                    ch_v "Ты считаешь, они подойдут к моему образу?"
                                            elif Girl is GwenX:
                                                    ch_g "Ох, они выглядят очень мило!"
                                            elif Girl is BetsyX:
                                                    ch_b "Они довольно милые."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. Они такие. . . милые. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Они выглядят очень сексуально."
                                            $ Girl.Statup("Lust", 89, 10)
                                    elif ApprovalCheck(Girl, 800):
                                            $ Girl.FaceChange("confused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace panties")
                                            $ Girl.Inventory.append("lace panties")
                                            $ Girl.Statup("Love", 200, 25)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 20)
                                            if Girl is RogueX:
                                                    ch_r "По-моему, они слишком прозрачные. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Я - Я бы не стала носить нечто подобное. . ."
                                                    $ KittyX.FaceChange("bemused",1)
                                                    ch_k "Но я все равно сохраню их. . ."
                                            elif Girl is EmmaX:
                                                    ch_e "Это. . . необычный подарок."
                                                    $ EmmaX.FaceChange("sly",1)
                                                    ch_e "Но я все равно сохраню их. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Я не думаю, что буду носить их. . ."
                                                    $ Girl.FaceChange("bemused",1)
                                                    ch_l "Но, возможно, они мне еще пригодятся. . ."
                                            elif Girl is StormX:
                                                    ch_s "Пожалуй, мне всегда пригодится еще одна пара. . ."
                                            elif Girl is JubesX:
                                                    ch_v "Они слегка. . . откровенны. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Ох, они такие. . . маленькие. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Возьму. . . на всякий случай."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. Они такие. . . милые. . ."
                                                    ch_d "-и очень тоненькие. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Они выглядят очень сексуально."
                                    elif "no gift panties" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            if Girl is RogueX:
                                                    ch_r "Не приставай ко мне сегодня с этим, [Girl.Petname]!"
                                            elif Girl is KittyX:
                                                    ch_k "Слушай, мой ответ по-прежнему \"нет\", перестань спрашивать!"
                                            elif Girl is EmmaX:
                                                    ch_e "В ближайшее время я не советую приставать ко мне с этим."
                                            elif Girl is LauraX:
                                                    ch_l "Мой ответ по-прежнему \"нет\", перестань спрашивать!"
                                            elif Girl is StormX:
                                                    ch_s "Я очень довольна своим нижним бельём."
                                            elif Girl is JubesX:
                                                    ch_v "Серьезно, прекрати. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Это неуместно!"
                                            elif Girl is BetsyX:
                                                    ch_b "Мне они не нужны."
                                            elif Girl is DoreenX:
                                                    ch_d "Я никак не могу их надеть."
                                            elif Girl is WandaX:
                                                    ch_w "Эм, оставь их в покое."
                                    else:
                                            $ Girl.FaceChange("angry")
                                            $ Girl.Statup("Love", 50, -20)
                                            $ Girl.Statup("Obed", 20, 10)
                                            $ Girl.Statup("Inbt", 20, 20)
                                            if Girl is RogueX:
                                                    if "no gift bra" in Girl.DailyActions:
                                                        ch_r "Мне это тоже не нужно!"
                                                    else:
                                                        ch_r "Знаешь, давай-ка лучше я сама буду выбирать себе нижнее белье."
                                            elif Girl is KittyX:
                                                    if "no gift bra" in Girl.DailyActions:
                                                        ch_k "Мне это тоже не нужно!"
                                                    elif Girl.SeenPanties:
                                                        if not Player.Male:
                                                            ch_k "Хоть ты и видела мои трусики, это еще не значит, что тебе позволено их выбрать."
                                                        else:
                                                            ch_k "Хоть ты и видел мои трусики, это еще не значит, что тебе позволено их выбрать."
                                                    else:
                                                        ch_k "Ох, хватит беспокоиться о том, что на мне надето."
                                            elif Girl is EmmaX:
                                                    if "no gift bra" in Girl.DailyActions:
                                                        ch_e "Это тоже не подходящий подарок."
                                                    elif Girl.SeenPanties:
                                                        if not Player.Male:
                                                            ch_e "Хоть ты и видела мои трусики, это еще не значит, что тебе позволено их выбрать."
                                                        else:
                                                            ch_e "Хоть ты и видел мои трусики, это еще не значит, что тебе позволено их выбрать."
                                                    else:
                                                        ch_e "Ох, тебя не должно волновать, что у меня там, снизу."
                                            elif Girl is LauraX:
                                                    if "no gift bra" in Girl.DailyActions:
                                                        ch_l "Мне это тоже не нужно!"
                                                    elif Girl.SeenPanties:
                                                        ch_l "Тебе не нравятся мои?"
                                                    else:
                                                        ch_l "Тебе не нужно беспокоиться о моем нижнем белье."
                                            elif Girl is StormX:
                                                    ch_s "У меня много нижнего белья, [Girl.Petname]."
                                            elif Girl is JubesX:
                                                    ch_v "Мне немного не по себе от этого. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Ого, это немного личное. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Они очень тонкие."
                                            elif Girl is DoreenX:
                                                    ch_d "Я никак не могу надеть что-то подобное. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Эм, нет, спасибо, может быть, как-нибудь в другой раз."
                                            $ Girl.Statup("Lust", 89, 5)
                                            "Она возвращает их вам."
                                            $ Girl.RecentActions.append("no gift panties")
                                            $ Girl.DailyActions.append("no gift panties")
                                    $ Girl.FaceChange("bemused")
                                else:
                                            call AnyLine(Girl,"У меня уже есть такие.")
                        #End Lace Panties

                        "Подарить ей чулки и пояс с подвязками." if "stockings and garterbelt" in Player.Inventory:
                                #If you have a stockings, you'll give it. (Rogue and Emma)
                                if "stockings and garterbelt" not in Girl.Inventory:
                                        "Вы протягиваете [Girl.Name_dat] чулки."
                                        $ Girl.Blush = 1
                                        $ Girl.FaceChange("bemused")
                                        $ Player.Inventory.remove("stockings and garterbelt")
                                        $ Girl.Inventory.append("stockings and garterbelt")
                                        $ Girl.Statup("Love", 200, 5)
                                        $ Girl.Statup("Obed", 200, 5)
                                        $ Girl.Statup("Inbt", 200, 5)
                                        if Girl is EmmaX:
                                                ch_e "Они очень красивые. . ."
                                        elif Girl is StormX:
                                                ch_s "Думаешь, я смогу их носить?"
                                        elif Girl is BetsyX:
                                                ch_b "Они весьма привлекательные."
                                        else:
                                                call AnyLine(Girl,"Они очень милые. . .")
                                        $ Girl.Statup("Lust", 89, 5)
                                else:
                                        call AnyLine(Girl,"У меня уже есть такие.")

                        "Подарить ей колготки." if Girl.Tag + " pantyhose" in Player.Inventory:
                                #If you have a stockings, you'll give it. (emma)
                                if "pantyhose" not in Girl.Inventory:
                                        "Вы протягиваете [Girl.Name_dat] колготки."
                                        $ Girl.FaceChange("bemused")
                                        $ Player.Inventory.remove(Girl.Tag + " pantyhose")
                                        $ Girl.Inventory.append("pantyhose")
                                        $ Girl.Statup("Love", 200, 5)
                                        $ Girl.Statup("Obed", 200, 5)
                                        $ Girl.Statup("Inbt", 200, 5)
                                        call AnyLine(Girl,"Они очень милые. . .")
                                else:
                                        call AnyLine(Girl,"У меня уже есть такие.")

                        "Подарить ей гольфы." if "knee" in Player.Inventory and Girl is KittyX:
                                #If you have a stockings, you'll give it. (Rogue and Emma)
                                if "knee" not in Girl.Inventory:
                                        "Вы протягиваете [Girl.Name_dat] гольфы."
                                        $ Girl.Blush = 1
                                        $ Girl.FaceChange("bemused")
                                        $ Player.Inventory.remove("knee")
                                        $ Girl.Inventory.append("knee")
                                        $ Girl.Statup("Love", 200, 5)
                                        $ Girl.Statup("Obed", 200, 5)
                                        $ Girl.Statup("Inbt", 200, 5)
                                        call AnyLine(Girl,"Они очень милые. . .")
                                else:
                                        call AnyLine(Girl,"У меня уже есть такие.")

                        "Подарить ей высокие носки." if "socks" in Player.Inventory:# and Girl is JubesX:
                                #If you have a stockings, you'll give it. (Rogue and Emma)
                                if "socks" not in Girl.Inventory:
                                        "Вы протягиваете [Girl.Name_dat] высокие носки."
                                        $ Girl.Blush = 1
                                        $ Girl.FaceChange("bemused")
                                        $ Player.Inventory.remove("socks")
                                        $ Girl.Inventory.append("socks")
                                        $ Girl.Statup("Love", 200, 5)
                                        $ Girl.Statup("Obed", 200, 5)
                                        $ Girl.Statup("Inbt", 200, 5)
                                        call AnyLine(Girl,"Они очень милые. . .")
                                else:
                                        call AnyLine(Girl,"У меня уже есть такие.")

                        "Подарить ей купальник." if Girl.Tag + " swimsuit" in Player.Inventory:
                                #If you have a suit, you'll give it.
                                if "swimsuit" not in Girl.Inventory:
                                    "Вы протягиваете [Girl.Name_dat] купальник."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 1200):
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " swimsuit")
                                            $ Girl.Inventory.append("swimsuit")
                                            $ Girl.Inventory.append("swimsuit")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 10)
                                            if Girl is BetsyX:
                                                    ch_b "А он симпатичный. . ."
                                    elif ApprovalCheck(Girl, 900):
                                            $ Girl.FaceChange("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " swimsuit")
                                            $ Girl.Inventory.append("swimsuit")
                                            $ Girl.Inventory.append("swimsuit")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            if Girl is BetsyX:
                                                    ch_b "Пожалуй, на меня он может хорошо сесть. . ."
                                            $ Girl.FaceChange("bemused",1)
                                    elif ApprovalCheck(Girl, 700):
                                            $ Girl.FaceChange("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " swimsuit")
                                            $ Girl.Inventory.append("swimsuit")
                                            $ Girl.Inventory.append("swimsuit")
                                            $ Girl.Statup("Love", 200, 10)
                                            $ Girl.Statup("Obed", 200, 5)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            if Girl is BetsyX:
                                                    ch_b "Мне кажется, он слишком. . . маленький. . ."
                                            $ Girl.FaceChange("bemused",1)
                                    elif "no gift bra" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            if Girl is BetsyX:
                                                    ch_b "Я все еще считаю, что он мне ни к чему."
                                    else:
                                        $ Girl.FaceChange("angry",2)
                                        $ Girl.Statup("Love", 50, -5)
                                        $ Girl.Statup("Obed", 20, 5)
                                        $ Girl.Statup("Inbt", 20, 10)
                                        if "no gift panties" in Girl.DailyActions:
                                                call AnyLine(Girl,"Мне это тоже не нужно!")
                                        else:
                                            if Girl is BetsyX:
                                                    ch_b "Я бы предпочла другой тип купальника. . ."
                                        $ Girl.Blush = 1
                                        "Она возвращает его вам."
                                        $ Girl.RecentActions.append("no gift bra")
                                        $ Girl.DailyActions.append("no gift bra")
                                    if "swimsuit" in Girl.Inventory:
                                        $ Girl.Swim[0] = 1
                                else:
                                        call AnyLine(Girl,"У меня уже есть такой.")

                        #end swimsuit

                        "Подарить ей лифчик бикини." if Girl.Tag + " bikini top" in Player.Inventory:
                                #If you have a bra, you'll give it.
                                if "bikini top" not in Girl.Inventory:
                                    "Вы протягиваете [Girl.Name_dat] лифчик бикини."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 1200):
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " bikini top")
                                            $ Girl.Inventory.append("bikini top")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 10)
                                            if Girl is RogueX:
                                                    ch_r "Какой приятный цвет. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Мне нравится. . ."
                                            elif Girl is EmmaX:
                                                    ch_e "Подчеркивает мои прелести, верно?. . ."
                                            elif Girl is LauraX:
                                                    ch_l "\"Икс\", так мило. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Ох, стильно. . ."
                                            elif Girl is StormX:
                                                    ch_s "Ох! Что-то знакомое."
                                            elif Girl is JubesX:
                                                    ch_v "Ого. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Ох, мне нравится. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох, он такой милый!"
                                            elif Girl is WandaX:
                                                    ch_w "Охх, он очень -милый.-"
                                    elif ApprovalCheck(Girl, 900) or Girl is JeanX:
                                            $ Girl.FaceChange("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini top")
                                            $ Girl.Inventory.append("bikini top")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            if Girl is RogueX:
                                                    ch_r "Слишком простой, но пойдет. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Слишком откровенный, но пойдет. . ."
                                            elif Girl is EmmaX:
                                                    ch_e "Он в моем вкусе. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Ладно, клево. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Ага, подойдет. . ."
                                            elif Girl is StormX:
                                                    ch_s "Думаю, я узнаю дизайн. . ."
                                            elif Girl is JubesX:
                                                    ch_v "Неплохой выбор. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Ох, кажется, у меня был такой. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. Мне нравится. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Охх, он очень -милый.-"
                                            $ Girl.FaceChange("bemused",1)
                                    elif ApprovalCheck(Girl, 700):
                                            $ Girl.FaceChange("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini top")
                                            $ Girl.Inventory.append("bikini top")
                                            $ Girl.Statup("Love", 200, 10)
                                            $ Girl.Statup("Obed", 200, 5)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            if Girl is RogueX:
                                                    ch_r "Я как раз думала о загаре. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Ах, милая Китти. . ."
                                            elif Girl is EmmaX:
                                                    ch_e "Интересный. . . подарок. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Пригодится. . ."
                                            elif Girl is StormX:
                                                    ch_s "Пожалуй, мне бы не помешал новый купальник."
                                            elif Girl is JubesX:
                                                    ch_v "Думаю, он мне подойдет. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Пойдет. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "А он милый. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Он довольно симпатичный."
                                            $ Girl.FaceChange("bemused",1)
                                    elif "no gift bra" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            if Girl is RogueX:
                                                    ch_r "Мой ответ по-прежнему \"нет\", перестань спрашивать!"
                                            elif Girl is KittyX:
                                                    ch_k "Слушай, мой ответ по-прежнему \"нет\", перестань спрашивать!"
                                            elif Girl is EmmaX:
                                                    ch_e "В ближайшее время я не советую приставать ко мне с этим."
                                            elif Girl is LauraX:
                                                    ch_l "Мой ответ по-прежнему \"нет\", перестань спрашивать!"
                                            elif Girl is StormX:
                                                    ch_s "Мне не нужны советы по моде, спасибо."
                                            elif Girl is JubesX:
                                                    ch_v "Он мне совсем не подойдет. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Как я уже сказала, мне он не нужен. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Мне он совсем не нужен. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Оставь его в покое. . ."
                                    else:
                                        $ Girl.FaceChange("angry",2)
                                        $ Girl.Statup("Love", 50, -5)
                                        $ Girl.Statup("Obed", 20, 5)
                                        $ Girl.Statup("Inbt", 20, 10)
                                        if "no gift panties" in Girl.DailyActions:
                                                call AnyLine(Girl,"Мне это тоже не нужно!")
                                        else:
                                            if Girl is RogueX:
                                                    ch_r "Не волнуйся о том, чтомне надеть."
                                            elif Girl is KittyX:
                                                    ch_k "Ох, не волнуйся о том, что мне надеть."
                                            elif Girl is EmmaX:
                                                    ch_e "Думаю, что мои купальники тебя не касаются."
                                            elif Girl is LauraX:
                                                    ch_l "Не беспокойся о том, что мне надеть."
                                            elif Girl is StormX:
                                                    ch_s "Нет, благодарю."
                                            elif Girl is JubesX:
                                                    ch_v "Нее, не думаю, что мне он подойдет. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Я даже не знаю. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Мне он совсем не нужен. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Эм, нет, спасибо, может быть, как-нибудь в другой раз."
                                        $ Girl.Blush = 1
                                        "She hands it back to you."
                                        $ Girl.RecentActions.append("no gift bra")
                                        $ Girl.DailyActions.append("no gift bra")
                                    if "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                        if Girl is StormX:
                                                ch_s "Ох! Теперь я понимаю предназначение лоскутов!"
                                        if Girl is KittyX:
                                            if Girl.Inbt >= 400 or "blue skirt" in Girl.Inventory:
                                                    $ Girl.Swim[0] = 1
                                        else:
                                                    $ Girl.Swim[0] = 1
                                else:
                                        call AnyLine(Girl,"У меня уже есть такой.")

                        #end bikini top

                        "Подарить трусики бикини." if Girl.Tag + " bikini bottoms" in Player.Inventory:
                                #If you have a bra, you'll give it.
                                if "bikini bottoms" not in Girl.Inventory:
                                    "Вы протягиваете [Girl.Name_dat] трусики бикини."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 1200):
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " bikini bottoms")
                                            $ Girl.Inventory.append("bikini bottoms")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 10)
                                            if Girl is RogueX:
                                                    ch_r "Они очень милые. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Они очень милые. . ."
                                            elif Girl is EmmaX:
                                                    ch_e "Они довольно стильные. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Хм, хороший выбор. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Ох, сексуальные. . ."
                                            elif Girl is StormX:
                                                    ch_s "Прелестные, но где то я уже видела подобные раньше. . ."
                                            elif Girl is JubesX:
                                                    ch_v "Ого, очень сексуальные. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Ого, они такие. . . милые. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох, они очень милые. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Я их уже обожаю!"
                                    elif ApprovalCheck(Girl, 900) or Girl is JeanX:
                                            $ Girl.FaceChange("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini bottoms")
                                            $ Girl.Inventory.append("bikini bottoms")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            if Girl is RogueX:
                                                    ch_r "Они такие маленькие. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Немного неудобные. . ."
                                            elif Girl is EmmaX:
                                                    ch_e "Довольно смело. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Ладно, они клевые. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Ооо, приятные. . ."
                                            elif Girl is StormX:
                                                    ch_s "Где-то я видела этот вырез раньше. . ."
                                            elif Girl is JubesX:
                                                    ch_v "Возможно, они немного маленькие. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Немного простоваты. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Они милые. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Я их уже обожаю!"
                                            $ Girl.FaceChange("bemused",1)
                                    elif ApprovalCheck(Girl, 700):
                                            $ Girl.FaceChange("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini bottoms")
                                            $ Girl.Inventory.append("bikini bottoms")
                                            $ Girl.Statup("Love", 200, 10)
                                            $ Girl.Statup("Obed", 200, 5)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            if Girl is RogueX:
                                                    ch_r "Я как раз думала о загаре. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Самое время для бикини. . ."
                                            elif Girl is EmmaX:
                                                    ch_e "Я не уверена, студент не должен покупать мне купальники. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Странный подарок, но на улице как раз тепло. . ."
                                            elif Girl is StormX:
                                                    ch_s "Какой необычный дизайн."
                                            elif Girl is JubesX:
                                                    ch_v "Я не уверена, что смогу это надеть. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Я не знаю, смогу ли я это надеть. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. Думаю, я могла бы попробовать их надеть. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Они очень милые."
                                            $ Girl.FaceChange("bemused",1)
                                    elif "no gift panties" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            if Girl is RogueX:
                                                    ch_r "Мой ответ по-прежнему \"нет\", перестань спрашивать!"
                                            elif Girl is KittyX:
                                                    ch_k "Слушай, мой ответ по-прежнему \"нет\", перестань спрашивать!"
                                            elif Girl is EmmaX:
                                                    ch_e "В ближайшее время я не советую приставать ко мне с этим."
                                            elif Girl is LauraX:
                                                    ch_l "Мой ответ по-прежнему \"нет\", перестань спрашивать!"
                                            elif Girl is StormX:
                                                    ch_s "Снова нет."
                                            elif Girl is JubesX:
                                                    ch_v "Точно нет."
                                            elif Girl is GwenX:
                                                    ch_g "Как я уже сказала, \"нет\". . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Я никак не могу их надеть. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Оставь их в покое."
                                    else:
                                            $ Girl.FaceChange("angry",2)
                                            $ Girl.Statup("Love", 50, -5)
                                            $ Girl.Statup("Obed", 20, 5)
                                            $ Girl.Statup("Inbt", 20, 10)
                                            if "no gift bra" in Girl.DailyActions:
                                                call AnyLine(Girl,"Мне это тоже не нужно!")
                                            else:
                                                if Girl is RogueX:
                                                        ch_r "Не волнуйся о том, что мне надеть."
                                                elif Girl is KittyX:
                                                        ch_k "Ох, хватит беспокоиться о том, что мне надеть."
                                                elif Girl is EmmaX:
                                                        ch_e "Думаю, что мои купальники тебя не касаются."
                                                elif Girl is LauraX:
                                                        ch_l "Не беспокойся о том, что мне надеть."
                                                elif Girl is StormX:
                                                        ch_s "Нет, благодарю."
                                                elif Girl is JubesX:
                                                        ch_v "Ох, нет. . ."
                                                elif Girl is GwenX:
                                                        ch_g "Эм, нет, спасибо. . ."
                                                elif Girl is DoreenX:
                                                        ch_d "Я не могу это надеть. . ."
                                                elif Girl is WandaX:
                                                        ch_w "Эм, нет, спасибо, может быть, как-нибудь в другой раз."
                                            $ Girl.Blush = 1
                                            "Она возвращает их вам."
                                            $ Girl.RecentActions.append("no gift panties")
                                            $ Girl.DailyActions.append("no gift panties")
                                    if "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                        if Girl is StormX:
                                                ch_s "Ох! Теперь я понимаю предназначение лоскутов!"
                                        if Girl is KittyX:
                                            if Girl.Inbt >= 400 or "blue skirt" in Girl.Inventory:
                                                    $ Girl.Swim[0] = 1
                                        else:
                                                    $ Girl.Swim[0] = 1
                                else:
                                        call AnyLine(Girl,"У меня уже есть такие.")
                        #end bikini bottoms

                        "Подарить ей синюю юбку." if Girl.Tag + " blue skirt" in Player.Inventory:
                                #If you have a bra, you'll give it.
                                if "blue skirt" not in Girl.Inventory:
                                    "Вы протягиваете [Girl.Name_dat] синюю юбку."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 1000):
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " blue skirt")
                                            $ Girl.Inventory.append("blue skirt")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 10)
                                            ch_k "Какая милая юбочка. . ."
                                    elif ApprovalCheck(Girl, 800):
                                            $ Girl.FaceChange("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " blue skirt")
                                            $ Girl.Inventory.append("blue skirt")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            ch_k "Смелый выбор. . ."
                                            $ Girl.FaceChange("bemused",1)
                                    elif ApprovalCheck(Girl, 600):
                                            $ Girl.FaceChange("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " blue skirt")
                                            $ Girl.Inventory.append("blue skirt")
                                            $ Girl.Statup("Love", 200, 10)
                                            $ Girl.Statup("Obed", 200, 5)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            ch_k "Она будет хорошо сочетаться с купальником. . ."
                                            $ Girl.FaceChange("bemused",1)
                                    elif "no gift skirt" in Girl.RecentActions:
                                            $ Girl.FaceChange("angry",2)
                                            ch_k "Я не хочу ее."
                                    elif "no gift skirt" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            ch_k "Слушай, мой ответ по-прежнему \"нет\", перестань спрашивать!"
                                    else:
                                            $ Girl.FaceChange("angry",2)
                                            $ Girl.Statup("Love", 50, -5)
                                            $ Girl.Statup("Obed", 20, 5)
                                            $ Girl.Statup("Inbt", 20, 10)
                                            ch_k "Я сама решаю, что мне надевать."
                                            $ Girl.Blush = 1
                                            "Она возвращает ее вам."
                                            $ Girl.RecentActions.append("no gift skirt")
                                            $ Girl.DailyActions.append("no gift skirt")
                                    if Girl is KittyX and "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                            $ Girl.Swim[0] = 1
                                else:
                                        call AnyLine(Girl,"У меня уже есть такая.")
                        #end blue skirt

                        "Неважно":
                            pass
                    #end Clothing

                "Гардероб" if bg_current != "bg shop":
                        if not Player.Male:
                            ch_p "Я хотела бы поговорить о твоем стиле."
                        else:
                            ch_p "Я хотел бы поговорить о твоем стиле."
                        call Taboo_Level
                        $ Line = "Giftstore"
                        call expression Girl.Tag + "_Clothes" #call Rogue_Clothes

                "Переключиться на. . .":
                        call Switch_Chat (1) #on Gift settings, only allows locals
                        ch_p "У меня кое-что для тебя есть."
#                        if Girl.Loc != bg_current:
#                                call AnyLine(Girl,"I don't see how, if I'm not there.")
#                                return
                        jump Gifts
                "Выход":
                    return
    return

#End Gift Menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Girl Settings / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Settings: #rkeljsvgbdw
    if Girl not in TotalGirls:
        $ Girl is Ch_Focus
    call Shift_Focus(Girl)
    while True:
        menu:
            ch_p "Давай поговорим о тебе."
            "Гардероб":
                        if not Player.Male:
                            ch_p "Я хотела бы поговорить о твоем стиле."
                        else:
                            ch_p "Я хотел бы поговорить о твоем стиле."
                        if bg_current == "HW Party":
                                call AnyLine(Girl,"Давай не на вечеринке. . .")
                        else:
                                call Taboo_Level
                                call expression Girl.Tag + "_Clothes" #call Rogue_Clothes

            "Изменить ее личность" if ApprovalCheck(Girl, 900, "L", TabM=0) or ApprovalCheck(Girl, 900, "O", TabM=0)or ApprovalCheck(Girl, 900, "I", TabM=0):
                        ch_p "Мы можем поговорить о нас?"
                        call expression Girl.Tag + "_Personality" #call Rogue_Personality

            "Ваше прозвище":
                        ch_p "Мы можем поговорить о моем прозвище?"
                        call expression Girl.Tag + "_Names"  #call Rogue_Names

            " Сменить прозвище [Girl.Name_rod]":
                        ch_p "Ты знаешь, что у меня есть для тебя новое прозвище?"
                        call expression Girl.Tag + "_Pet" #call Rogue_Pet

            "Сменить имя [Girl.Name_rod]" if len(Girl.Names) > 1:
                        ch_p "Помнишь, ты говорила мне, что у тебя есть другое имя?"
                        call expression Girl.Tag + "_Rename" #call Rogue_Rename

            "По поводу того, как она иногда просит вас проследовать за ней" if "follow" in Girl.Traits:
                        ch_p "Помнишь, как ты просишь иногда пойти за тобой?"
                        $ Line = 0
                        if Girl in (RogueX,EmmaX,StormX,BetsyX):
                                call AnyLine(Girl,"Да?")
                        elif Girl is JeanX:
                                ch_j "Не совсем, но продолжай?"
                        else: #Kitty, Laura, Jubilee
                                call AnyLine(Girl,"Да?")
                        menu:
                            extend ""
                            "Просто иди куда хочешь, не жди меня." if "freetravels" not in Girl.Traits:
                                    $ Girl.FaceChange("perplexed")
                                    if Girl is RogueX:
                                            ch_r "Ох, хорошо, без проблем."
                                    elif Girl is KittyX:
                                            ch_k "Эм[Girl.like]ладно."
                                    elif Girl is EmmaX:
                                            ch_e "Хорошо, не буду задавать лишних вопросов."
                                    elif Girl is LauraX:
                                            ch_l "Ох. . . ладно."
                                    elif Girl is JeanX:
                                            ch_j "Лаааадно?"
                                    elif Girl is StormX:
                                            ch_s "Хорошо?"
                                    elif Girl is JubesX:
                                            ch_v "Ох, конечно, ладно. . ."
                                    elif Girl is GwenX:
                                            ch_g "Да? . ."
                                    elif Girl is BetsyX:
                                            ch_b "Ох, хорошо."
                                    elif Girl is DoreenX:
                                            ch_d "Ох, ладно."
                                    elif Girl is WandaX:
                                            ch_w "Поняла."
                                    if "follow" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 90, -2)
                                        $ Girl.Statup("Obed", 30, 5)
                                    $ Line = "free"

                            "Спрашивай, хочу ли я пойти с тобой." if "asktravels" not in Girl.Traits or "freetravels" in Girl.Traits:
                                    $ Girl.FaceChange("perplexed")
                                    if Girl is RogueX:
                                            ch_r "Ох, хорошо, без проблем."
                                    elif Girl is KittyX:
                                            ch_k "Эм[Girl.like]ладно."
                                    elif Girl is EmmaX:
                                            ch_e "Не хочешь оставаться один?"
                                    elif Girl is LauraX:
                                            ch_l "Ладно. . ."
                                    elif Girl is JeanX:
                                            ch_j "Приму к сведению."
                                    elif Girl is StormX:
                                            ch_s "Хорошо?"
                                    elif Girl is JubesX:
                                            ch_v "Ладно, ага, не хотелось бы, чтобы ты отставал. . ."
                                    elif Girl is GwenX:
                                            ch_g "Хорошо, как скажешь. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Это я могу."
                                    elif Girl is DoreenX:
                                            ch_d "Хорошо, буду иметь в виду."
                                    elif Girl is WandaX:
                                            ch_w "Буду иметь в виду."
                                    if "follow" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 70, 2)
                                        $ Girl.Statup("Inbt", 60, 2)
                                    $ Line = "ask"

                            "Никогда никуда не уходи, когда я рядом." if "lockedtravels" not in Girl.Traits or "freetravels" in Girl.Traits:
                                if ApprovalCheck(Girl, 500, "O",Alt=[[EmmaX,JeanX],600]) or ApprovalCheck(Girl, 900, "L"):
                                    $ Girl.FaceChange("sexy")
                                    if Girl is RogueX:
                                            ch_r "Ох, хорошо."
                                    elif Girl is KittyX:
                                            ch_k "Ах, значит, ты скучаешь, когда меня нет рядом!"
                                    elif Girl is EmmaX:
                                            $ Girl.FaceChange("angry", Eyes="side")
                                            ch_e "Не знаю, почему я вообще терплю твой бредни."
                                            $ Girl.FaceChange("sexy",1)
                                            ch_e "Но {i}ладно.{/i}"
                                    elif Girl is LauraX:
                                            ch_l "Это так мило."
                                    elif Girl is JeanX:
                                            ch_j ". . ."
                                            ch_j "Посмотрим. . ."
                                    elif Girl is StormX:
                                            ch_s "Пожалуй, соглашусь. . ."
                                    elif Girl is JubesX:
                                            ch_v "Ох, хорошо. . ."
                                    elif Girl is GwenX:
                                            ch_g "Эм, конечно. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Хм, интересно, я бы не подумала, что тебе бывает одиноко."
                                    elif Girl is DoreenX:
                                            ch_d "Ох, ладно. . ."
                                    elif Girl is WandaX:
                                            ch_w "Вау, ладно."
                                    if "follow" not in Girl.DailyActions:
                                        if Girl.Love > 90:
                                            $ Girl.Statup("Love", 99, 2)
                                        $ Girl.Statup("Obed", 60, 5)
                                    $ Girl.Statup("Inbt", 50, -5, 1)
                                    $ Line = "lock"
                                else:
                                    $ Girl.FaceChange("angry")
                                    if Girl is RogueX:
                                            ch_r "Мне плевать, чего ты хочешь."
                                    elif Girl is KittyX:
                                            ch_k "Кого вообще волнует твое мнение?"
                                    elif Girl is EmmaX:
                                            ch_e "Это решать только мне."
                                    elif Girl is LauraX:
                                            ch_l "Ну кого вообще волнует, что ты думаешь?"
                                    elif Girl is JeanX:
                                            ch_j "Я не стану этого делать. . ."
                                    elif Girl is StormX:
                                            ch_s "Не вздумай меня контролировать."
                                    elif Girl is JubesX:
                                            ch_v "Ну, посмотрим. . ."
                                    elif Girl is GwenX:
                                            ch_g "Со мной это не сработает. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Боюсь, я не смогу удовлетворить твою просьбу."
                                    elif Girl is DoreenX:
                                            ch_d "Иногда мне нужно время \"на себя\". . ."
                                    elif Girl is WandaX:
                                            ch_w "Посмотрим."

                            "Неважно.":
                                    if Girl is RogueX:
                                            ch_r "Ох, хорошо."
                                    elif Girl is KittyX:
                                            ch_k "Лаааадно."
                                    elif Girl is EmmaX:
                                            ch_e "Как скажешь."
                                    elif Girl is LauraX:
                                            ch_l "Ладно. . ."
                                    elif Girl is JeanX:
                                            ch_j "Ладно?"
                                    elif Girl is StormX:
                                            ch_s "Хорошо."
                                    elif Girl is JubesX:
                                            ch_v "Ладно. . ."
                                    elif Girl is GwenX:
                                            ch_g "Лаааадно? . ."
                                    elif Girl is BetsyX:
                                            ch_b "Хорошо? . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ладно?"
                                    elif Girl is WandaX:
                                            ch_w "Конечно."

                        if Line:
                                    $ Girl.DailyActions.append("follow")
                                    if "freetravels" in Girl.Traits:
                                        $ Girl.Traits.remove("freetravels")
                                    if "asktravels" in Girl.Traits:
                                        $ Girl.Traits.remove("asktravels")
                                    if "lockedtravels" in Girl.Traits:
                                        $ Girl.Traits.remove("lockedtravels")

                                    if Line == "free":
                                        $ Girl.Traits.append("freetravels")
                                    elif Line == "ask":
                                        $ Girl.Traits.append("asktravels")
                                    elif Line == "lock":
                                        $ Girl.Traits.append("lockedtravels")
                                    $ Line = 0

            "Изменить ее слово-паразит" if Girl is KittyX:
                    ch_p "Ты[Girl.like]слишком часто употребляешь \"[Girl.like]\". . ."
                    if ApprovalCheck(Girl, 800):
                            call KittyLike
                    else:
                            ch_k "[Girl.Like]а тебе-то что?"

            "Личная территория":
                        menu:
                            "Позволите ли вы ей приходить без предупреждения?"
                            "Да [[по умолчанию]":
                                    ch_p "Ты можешь приходить, когда захочешь."
                                    $ Girl.FaceChange("smile")
                                    if Girl is RogueX:
                                            ch_r "Хорошо."
                                    elif Girl is KittyX:
                                            ch_k "[Girl.Like]отлично."
                                    elif Girl is EmmaX:
                                            ch_e "Хорошо, учту."
                                    elif Girl is LauraX:
                                            ch_l "Ох. . . ладно."
                                    elif Girl is JeanX:
                                            ch_j "Как скажешь."
                                    elif Girl is StormX:
                                            ch_s "Рада слышать."
                                    elif Girl is JubesX:
                                            ch_v "Хорошо, тогда как-нибудь увидимся. . ."
                                    elif Girl is GwenX:
                                            ch_g "Клево, тогда увидимся. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Тогда скоро увидимся у тебя."
                                    elif Girl is DoreenX:
                                            ch_d "Клево!"
                                    elif Girl is WandaX:
                                            ch_w "Хорошо, это я могу."
                                    $ Girl.DrainWord("lockedout",0,0,1)
                            "Нет":
                                    ch_p "Не могла бы ты не заходить без предупреждения?"
                                    $ Girl.FaceChange("perplexed")
                                    if Girl is RogueX:
                                            ch_r "Ох, хорошо, без проблем."
                                    elif Girl is KittyX:
                                            ch_k "Эм[Girl.like]ладно."
                                    elif Girl is EmmaX:
                                            ch_e "Хорошо, сначала буду спрашивать у тебя."
                                    elif Girl is LauraX:
                                            ch_l "Ох. . . ладно."
                                    elif Girl is JeanX:
                                            ch_j "Как скажешь."
                                    elif Girl is StormX:
                                            ch_s "Понимаю."
                                    elif Girl is JubesX:
                                            ch_v "Конечно, я могу дать тебе пространство. . ."
                                    elif Girl is GwenX:
                                            ch_g "Ох. . . ладно?"
                                    elif Girl is BetsyX:
                                            ch_b "Понимаю."
                                    elif Girl is DoreenX:
                                            ch_d "Ага, поняла."
                                    elif Girl is WandaX:
                                            ch_w "Конечно, конечно."
                                    $ Girl.FaceChange("smile")
                                    $ Girl.AddWord(1,0,0,"lockedout")
            "Переключиться на. . .":
                    call Switch_Chat

            "Неважно.":
                        return
    #end loop

# End Girl_Settings / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# AskDateOther start / / / /

label AskDateOther: #rkeljsvgbdw
        #called if you ask a girlfriend about dating a different girl. "Girl" is passed from the prior chat.
        if Girl not in Player.Harem:
            return
        menu:
            "Ты не думала о том, чтобы позволить мне встречаться с. . ."
            "[RogueX.Name_tvo]" if Girl is not RogueX and RogueX not in Player.Harem:
                    call Poly_Start(RogueX,1,Girl)
            "[KittyX.Name_tvo]" if Girl is not KittyX and KittyX not in Player.Harem and "met" in KittyX.History:
                    call Poly_Start(KittyX,1,Girl)
            "[EmmaX.Name_tvo]" if Girl is not EmmaX and EmmaX not in Player.Harem and "met" in EmmaX.History:
                    call Poly_Start(EmmaX,1,Girl)
            "[LauraX.Name_tvo]" if Girl is not LauraX and LauraX not in Player.Harem and "met" in LauraX.History:
                    call Poly_Start(LauraX,1,Girl)
            "[JeanX.Name_tvo]" if Girl is not JeanX and JeanX not in Player.Harem and "met" in JeanX.History:
                    call Poly_Start(JeanX,1,Girl)
            "[StormX.Name_tvo]" if Girl is not StormX and StormX not in Player.Harem and "met" in StormX.History:
                    call Poly_Start(StormX,1,Girl)
            "[JubesX.Name_tvo]" if Girl is not JubesX and JubesX not in Player.Harem and "met" in JubesX.History:
                    call Poly_Start(JubesX,1,Girl)
            "[GwenX.Name_tvo]" if Girl is not GwenX and GwenX not in Player.Harem and "met" in GwenX.History:
                    call Poly_Start(GwenX,1,Girl)
            "[BetsyX.Name_tvo]" if Girl is not BetsyX and BetsyX not in Player.Harem and "met" in BetsyX.History:
                    call Poly_Start(BetsyX,1,Girl)
            "[DoreenX.Name_tvo]" if Girl is not DoreenX and DoreenX not in Player.Harem and "met" in DoreenX.History:
                    call Poly_Start(DoreenX,1,Girl)
            "[WandaX.Name_tvo]" if Girl is not WandaX and WandaX not in Player.Harem and "met" in WandaX.History:
                    call Poly_Start(WandaX,1,Girl)
            "Неважно":
                    pass
        return




#Labels:
#Chat
#Chat_Menu
#Girl_Dismissed
#Flirt
#Compliment
#Love_You
#TouchCheek
#Hold_Hands
#Girl_Headpat
#AskPanties
#Remove_Panties
#Favorite_Actions
#Gifts
#Girl_Settings
