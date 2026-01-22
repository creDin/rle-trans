# SexMenu //////////////////////////////////////////////////////////////////////
label SexAct(Act = 0): #rkeljsvgb
        if AloneCheck(Ch_Focus) and Ch_Focus.Taboo == 20:
                $ Ch_Focus.Taboo = 0
                $ Taboo = 0
#        call Shift_Focus(Ch_Focus)
        if Act == "SkipTo":
            $ renpy.pop_call() #causes it to skip past the Trigger Swap
            $ renpy.pop_call() #causes it to skip past the cycle you were in before
            #$ renpy.pop_call() #causes it to skip past the sex menu you were in before that
            call SkipTo(Ch_Focus)
        elif Act == "switch":
            $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
            #$ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
            # drops through to sex menu
        elif Act == "masturbate":
            call Girl_M_Prep
            if not Situation:
                return
        elif Act == "lesbian":
            call Les_Prep #nee call Girl_Les_Prep
            if not Situation:
                return
        elif Act == "kissing":
            call KissPrep
            if not Situation:
                return
        elif Act == "breasts":
            call Girl_Fondle_Breasts
            if not Situation:
                return
        elif Act == "blow":
            if Player.Male:
                call Girl_BJ_Prep
            else:
                call Girl_CUN
            if not Situation:
                return
        elif Act == "hand":
            if Player.Male:
                call Girl_HJ_Prep
            else:
                call Girl_Finger
            if not Situation:
                return
        elif Act == "sex":
            call Girl_SexPrep
            if not Situation:
                return

label SexMenu: #rkeljsvgbdw
        # Modification mode
        $ play_music()
        $ play_sound()
        # -----------------

        if "sexit" in Player.RecentActions:
                return
        if Ch_Focus is EmmaX:
                if "three" not in EmmaX.History and not AloneCheck(EmmaX):
                    # if there are other girls in the room. . .
                    call Emma_ThreeCheck
                if Taboo > 20 and "taboo" not in EmmaX.History:
                    # If she's yet to agree to taboo stuff
                    call Emma_Taboo_Talk
                    if bg_current == "bg classroom" or bg_current in PersonalRooms and AloneCheck(EmmaX):
                            ch_p "Мы ведь можем просто закрыть дверь, верно?"
                            ch_e "Конечно, можем. . ."
                            "[EmmaX.Name] подходит к двери и запирает ее."
                            $ Player.Traits.append("locked")
                            call Taboo_Level
                    else:
                            return
        #end Emma stuff
#        call Shift_Focus(Ch_Focus)
        $ Trigger = 0
        $ Trigger2 = 0
        $ Ch_Focus.Offhand = 0
        $ Situation = 0
        call Girl_Hide(Ch_Focus)
        $ Ch_Focus.ArmPose = 1
        call Set_The_Scene(1,0,0,0,1)
        if not Player.Semen:
                "В данный момент у вас почти нет сил, вам нужно немного подождать."
        if Player.Focus >= 95:
                "Вы уже почти на пределе, малейшиее прикосновение может довести вас до оргазма."
        if not Ch_Focus.Action:
                "[Ch_Focus.Name] выглядит слегка уставшей, стоит дать ей немного отдохнуть."

        if "caught" in Ch_Focus.RecentActions or "angry" in Ch_Focus.RecentActions:
                if Ch_Focus.Loc == bg_current:
                        call Sex_Menu_Dialog(Ch_Focus,"caught") #ch_d "I'm just happy to be here, I don't want to get in trouble."
                $ Ch_Focus.OutfitChange()
                $ Ch_Focus.DrainWord("caught",1,0)
                return
        if Round < 5:
                call Sex_Menu_Dialog(Ch_Focus,5) #ch_d "I think I could use a break."
                call Sex_Over
                return

        call expression Ch_Focus.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
        if not Player.Male and "nogirls" in Ch_Focus.History and not Ch_Focus.Forced:
                #if she isn't into girls but isn't coerced. . .
                return

        menu SMenu:
            # Modification mode
            "{color=#FDCA6E}Режим тройничка?{/color}" if not Partner:
                call Sex_Menu_Threesome(Ch_Focus)
                call MenuThreesome
                jump SMenu
            # -----------------

            "Может, начнем целоваться?":
                    if Ch_Focus.Action:
                        call Makeout
                    else:
                        call Sex_Menu_Dialog(Ch_Focus,"minute") #ch_d "Maybe in a minute, I need a break."

            "Могу я. . .? [[Потрогать ее]":
                    if Ch_Focus.Action:
                        $ Ch_Focus.Mouth = "smile"
                        menu:
                            "Сделать тебе массаж?":
                                    call Massage
                            "Потрогать твою грудь?":
                                    call Girl_Fondle_Breasts
                            "Пососать твою грудь?" if Ch_Focus.Action and Ch_Focus.SuckB:
                                    call Girl_Suck_Breasts
                            "Потрогать твои бедра?" if Ch_Focus.Action:
                                    call Girl_Fondle_Thighs
                            "Потрогать твою киску?" if Ch_Focus.Action:
                                    call Girl_Fondle_Pussy
                            "Вылизать твою киску?" if Ch_Focus.Action and Ch_Focus.LickP:
                                    call Girl_Lick_Pussy
                            "Потрогать твою попку?":
                                    call Girl_Fondle_Ass
                            "Неважно [[заняться чем-нибудь другим]":
                                    jump SMenu
                    else:
                                call Sex_Menu_Dialog(Ch_Focus,"minute") #ch_d "Maybe in a minute, I need a break."

            "Не могла бы ты позаботиться кое о чем для меня? [[Член, вы имеете в виду свой член]" if Player.Male:
                    if Player.Semen and Ch_Focus.Action:
                        menu:
                            "Можешь подрочить мне рукой?":
                                call Girl_Handjob
                            "Можешь подрочить мне с помощью телекинеза?" if "psysex" in Ch_Focus.History:
                                if ApprovalCheck(JeanX, 1000):
                                        #sees if you're up for psychic handy
                                        call Jean_PJ_Prep
                                else:
                                        ch_j "Я бы этого не хотела."
                            "Можешь подрочить мне сиськами?":# (locked)":
                                call Girl_Titjob
                            "Может, отсосешь?":# (locked)":
                                call Girl_Blowjob
                            "Можешь подрочить мне ногами?":# (locked)" if Ch_Focus is not WandaX:
                                call Girl_Footjob
                            "Неважно [[заняться чем-нибудь другим]":
                                jump SMenu
                    elif not Ch_Focus.Action:
                                call Sex_Menu_Dialog(Ch_Focus,"minute") #ch_d "Maybe in a minute, I need a break."
                    else:
                                "Вы устали, похоже, вам не помешает отдохнуть."

            "Не могла бы ты позаботиться кое о чем для меня? [[Киска, вы имеете в виду свою киску]" if not Player.Male:
                    if Player.Semen and Ch_Focus.Action:
                        menu:
                            "Можешь поласкать мою киску?":
                                call Girl_Finger
                            "Можешь поласкать мою киску с помощью телекинеза?" if "psysex" in Ch_Focus.History:
                                if ApprovalCheck(JeanX, 1000):
                                        #sees if you're up for psychic handy
                                        call Jean_PJ_Prep
                                else:
                                        ch_j "Я бы этого не хотела."
                            "Можешь вылизать мою киску?":# (locked)":
                                call Girl_CUN
                            "Неважно [[заняться чем-нибудь другим]":
                                jump SMenu
                    elif not Ch_Focus.Action:
                                call Sex_Menu_Dialog(Ch_Focus,"minute") #ch_d "Maybe in a minute, I need a break."
                    else:
                                "Вы устали, похоже, вам не помешает отдохнуть."

            "Можешь устроить для меня небольшое представление?":
                        menu:
                            "Станцуешь для меня?":
                                    if Ch_Focus.Action:
                                        call Group_Strip(Ch_Focus)
                                    else:
                                        call Sex_Menu_Dialog(Ch_Focus,"minute") #ch_d "Maybe in a minute, I need a break."

                            "Можешь раздеться для меня?":
                                        call Girl_Undress(Ch_Focus)

                            "На тебе что-то есть. . . [[привести ее в порядок]" if Ch_Focus.Spunk:
                                        call Sex_Menu_Dialog(Ch_Focus,"clean") #ch_d "What? Where?"
                                        call Girl_Cleanup(Ch_Focus,"ask")

                            "Можно мне посмотреть, как ты кончаешь? [[мастурбация]":
                                    if Ch_Focus.Action:
                                        call Girl_Masturbate
                                    else:
                                        call Sex_Menu_Dialog(Ch_Focus,"minute") #ch_d "Maybe in a minute, I need a break."

                            "Может, начнешь целоваться с [RogueX.Name_tvo]?" if RogueX.Loc == bg_current and Ch_Focus is not RogueX:
                                        call LesScene
                            "Может, начнешь целоваться с [KittyX.Name_tvo]?" if KittyX.Loc == bg_current and Ch_Focus is not KittyX:
                                        call LesScene
                            "Может, начнешь целоваться с [EmmaX.Name_tvo]?" if EmmaX.Loc == bg_current and Ch_Focus is not EmmaX:
                                        call LesScene
                            "Может, начнешь целоваться с [LauraX.Name_tvo]?" if LauraX.Loc == bg_current and Ch_Focus is not LauraX:
                                        call LesScene
                            "Может, начнешь целоваться с [JeanX.Name_tvo]?" if JeanX.Loc == bg_current and Ch_Focus is not JeanX:
                                        call LesScene
                            "Может, начнешь целоваться с [StormX.Name_tvo]?" if StormX.Loc == bg_current and Ch_Focus is not StormX:
                                        call LesScene
                            "Может, начнешь целоваться с [JubesX.Name_tvo]?" if JubesX.Loc == bg_current and Ch_Focus is not JubesX:
                                        call LesScene
                            "Может, начнешь целоваться с [GwenX.Name_tvo]?" if GwenX.Loc == bg_current and Ch_Focus is not GwenX:
                                        call LesScene
                            "Может, начнешь целоваться с [BetsyX.Name_tvo]?" if BetsyX.Loc == bg_current and Ch_Focus is not BetsyX:
                                        call LesScene
                            "Может, начнешь целоваться с [DoreenX.Name_tvo]?" if DoreenX.Loc == bg_current and Ch_Focus is not DoreenX:
                                        call LesScene
                            "Может, начнешь целоваться с [WandaX.Name_tvo]?" if WandaX.Loc == bg_current and Ch_Focus is not WandaX:
                                        call LesScene

                            "Неважно [[заняться чем-нибудь другим]":
                                        jump SMenu


            "Слушай, у меня есть кое-какая идея. . . [[секс]":
                    if Ch_Focus.Action:
                        menu:
                            "Я хочу потереться о тебя. . .":# (locked)":
                                        if Player.Semen:
                                            call Girl_Sex_H
                                        else:
                                            "Вы сильны духом, но слабы телом."
                            "Я хочу трахнуть твою киску.":# (locked)":
                                        if Player.Semen:
                                            call Girl_Sex_P
                                        else:
                                            "Вы сильны духом, но слабы телом."
                            "Я хочу трахнуть твою попку.":# (locked)":
                                        if Player.Semen:
                                            call Girl_Sex_A
                                        else:
                                            "Вы сильны духом, но слабы телом."
                            "Как насчет ножниц?" if Player.Male != 1:# (locked)" if Player.Male != 1:
                                        if Player.Semen:
                                            call Girl_SC
                                        else:
                                            "Вы сильны духом, но слабы телом."
                            "Как насчет игрушек? [[Киска]":
                                        call Girl_Dildo("pussy") #call Girl_Dildo_Pussy
                            "Как насчет игрушек? [[Попка]":
                                        call Girl_Dildo("anal") #call Girl_Dildo_Ass
                            "Неважно [[заняться чем-нибудь другим]":
                                        jump SMenu
                    else:
                                        call Sex_Menu_Dialog(Ch_Focus,"minute") #ch_d "Maybe in a minute, I need a break."

            "Слушай, не хочешь поучавствовать в групповухе? [[Тройничек]" if not Partner:
                        call Sex_Menu_Threesome(Ch_Focus)
                        jump SMenu

            "Эй, [Partner.Name]? [[переключить свое внимание на другую]" if Partner:
                        call Shift_Focus(Partner)
                        call SexAct("switch")
#                        call expression Partner.Tag + "_SexAct" pass ("switch") #call Rogue_SexAct("switch")
                        return

            "Чит-меню" if config.developer:
                        call Cheat_Menu(Ch_Focus)
            "Неважно. [[выход]":
                    if Ch_Focus.Lust >= 50 or Ch_Focus.Addict >= 50:
                            $ Ch_Focus.FaceChange("sad")
                            if Ch_Focus.Action and Ch_Focus.SEXP >= 15 and Round > 20:
                                    if "round2" not in Ch_Focus.RecentActions:
                                            call Sex_Menu_Dialog(Ch_Focus,"round1")
                                            $ Ch_Focus.Statup("Inbt", 30, 2)
                                            $ Ch_Focus.Statup("Inbt", 50, 1)
                                    elif Ch_Focus.Addict >= 50:
                                            call Sex_Menu_Dialog(Ch_Focus,"addict") #ch_d "I'm kinda still buzzing here. . ."
                                    else:
                                            call Sex_Menu_Dialog(Ch_Focus,"wanting") #ch_d "I um, need a little help here. . ."
                                    menu:
                                        extend ""
                                        "Пока хватит." if Player.Semen and "round2" not in Ch_Focus.RecentActions:
                                            if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                                $ Ch_Focus.FaceChange("angry")
                                                $ Ch_Focus.Eyes = "side"
                                                $ Ch_Focus.Statup("Love", 70, -2)
                                                $ Ch_Focus.Statup("Love", 90, -4)
                                                $ Ch_Focus.Statup("Obed", 30, 2)
                                                $ Ch_Focus.Statup("Obed", 70, 1)
                                                call Sex_Menu_Dialog(Ch_Focus,"doneunhappy") #ch_d "Aw!"
                                            else:
                                                $ Ch_Focus.FaceChange("bemused", 1)
                                                $ Ch_Focus.Statup("Obed", 50, 2)
                                                call Sex_Menu_Dialog(Ch_Focus,"donesatisfied") #ch_d "Aw. . ."
                                        "Я сделала все, что могла." if "round2" in Ch_Focus.RecentActions and not Player.Male:
                                            if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                                $ Ch_Focus.FaceChange("sadside")
                                                call Sex_Menu_Dialog(Ch_Focus,"triedunhappy") #ch_d "Really? . ."
                                            else:
                                                $ Ch_Focus.FaceChange("bemused", 1)
                                                call Sex_Menu_Dialog(Ch_Focus,"triedsatisfied") #ch_d "I guess so. . ."
                                        "Я сделал все, что мог." if "round2" in Ch_Focus.RecentActions and Player.Male:
                                            if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                                $ Ch_Focus.FaceChange("sadside")
                                                call Sex_Menu_Dialog(Ch_Focus,"triedunhappy") #ch_d "Really? . ."
                                            else:
                                                $ Ch_Focus.FaceChange("bemused", 1)
                                                call Sex_Menu_Dialog(Ch_Focus,"triedsatisfied") #ch_d "I guess so. . ."
                                        "Эй, я так старалась." if Ch_Focus.OCount > 2 and not Player.Male:
                                                $ Ch_Focus.FaceChange("sly", 1)
                                                call Sex_Menu_Dialog(Ch_Focus,"didit") #ch_d "Ok, sure. . ."
                                        "Эй, я так старался." if Ch_Focus.OCount > 2 and Player.Male:
                                                $ Ch_Focus.FaceChange("sly", 1)
                                                call Sex_Menu_Dialog(Ch_Focus,"didit") #ch_d "Ok, sure. . ."
                                        "У меня нет сил, давай потом." if not Player.Semen:
                                                $ Ch_Focus.FaceChange("normal")
                                                call Sex_Menu_Dialog(Ch_Focus,"tapped") #ch_d "Well, could do some other stuff. . ."
                                        "Ладно, давай попробуем что-нибудь еще." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                                $ Ch_Focus.FaceChange("smile")
                                                $ Ch_Focus.Statup("Love", 70, 2)
                                                $ Ch_Focus.Statup("Love", 90, 1)
                                                call Sex_Menu_Dialog(Ch_Focus,"somethingelse") #ch_d "Neat!"
                                                $ Ch_Focus.RecentActions.append("round2")
                                                $ Ch_Focus.DailyActions.append("round2")
                                                jump SexMenu
                                        "Снова? Ну ладно." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                                $ Ch_Focus.FaceChange("sly")
                                                call Sex_Menu_Dialog(Ch_Focus,"again") #ch_d "Nice. . ."
                                                jump SexMenu
                                    #End "if Ch_Focus is still up for more"
                            else:
                                                $ Ch_Focus.FaceChange("bemused", 1)
                                                call Sex_Menu_Dialog(Ch_Focus,"breaktime") #ch_d "I guess we could take a break. . ."
                                                $ Ch_Focus.Statup("Inbt", 30, 2)
                                                $ Ch_Focus.Statup("Inbt", 50, 1)
                            $ Ch_Focus.FaceChange()
                    else:
                                                call Sex_Menu_Dialog(Ch_Focus,"fine") #ch_d "Oh, ok. . ."

                    call Sex_Over
                    return
        if Ch_Focus.Loc != bg_current:
            call Set_The_Scene
            call Trig_Reset
            call Sex_Over
            return
        if not MultiAction:
            call Set_The_Scene
            call Sex_Menu_Dialog(Ch_Focus,"done") #ch_d "That's it. . . for now at least."
            $ Ch_Focus.OCount = 0
            call Trig_Reset
            call Sex_Over
            return
        call GirlsAngry
        jump SexMenu
# end SexMenu //////////////////////////////////////////////////////////////////////


# start Sex_Menu_Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Sex_Menu_Dialog(Girl=0,Type=0): #rkeljsvgbdw
        # call Sex_Menu_Dialog(Girl,"done")
        #called from during sex scenes if a girl is getting tired. . .
        if Girl not in TotalGirls:
                return
        if Girl is RogueX:
                if Type == "caught": #if you'd been recently caught doing stuff in public
                                ch_r "Я не хочу сейчас иметь с тобой никаких дел."
                elif Type == 5: #when the timer hits 5
                                ch_r "Давай немного передохнем."
                elif Type == "minute": #when asked to do something with no actions left
                                ch_r "Извини, [RogueX.Petname], но я немного устала."
                elif Type == "clean": #when you want them to clean up
                                ch_r "Да?"
                #from Wanting More dialogues:
                elif Type == "round1": #if "round2" not in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_r "Ты уверена, [RogueX.Petname]? Мне бы не помешала компания."
                                else:
                                    ch_r "Ты уверен, [RogueX.Petname]? Мне бы не помешала компания."
                elif Type == "addict": #elif Ch_Focus.Addict >= 50:
                                ch_r "Мне нужно еще немного. . . близости."
                elif Type == "wanting":
                                ch_r "Не оставляй меня в таком состояние, [RogueX.Petname]."
                elif Type == "doneunhappy":  #"Yeah, I'm done for now." if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                ch_r "Значит, бросаешь девушку в беде. . ."
                elif Type == "donesatisfied":  #"Yeah, I'm done for now.", else
                                if not Player.Male:
                                    ch_r "Ну, по крайней мере, ты выполнила свою часть. . ."
                                else:
                                    ch_r "Ну, по крайней мере, ты выполнил свою часть. . ."
                elif Type == "triedunhappy": #"I gave it a shot."  if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCoun
                                ch_r "Значит, бросаешь девушку в беде. . ."
                elif Type == "triedsatisfied": #"I gave it a shot." else
                                if not Player.Male:
                                    ch_r "Ну, хоть ответила честно. . ."
                                else:
                                    ch_r "Ну, хоть ответил честно. . ."
                elif Type == "didit": #"Hey, I did my part." if Ch_Focus.OCount > 2:
                                ch_r "Наверное, так оно и было. . ."
                elif Type == "tapped": #"I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                ch_r "Пожалуй, с этим ничего уже не поделаешь."
                elif Type == "somethingelse": # "Ok, we can try something else." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                ch_r "Мммм. . ."
                elif Type == "again": # "Again? Ok, fine." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                ch_r "Ага, снова. . ."
                elif Type == "breaktime": #if she's tired too
                                ch_r "Наверное, я тоже устала, [RogueX.Petname]. Думаю, мы можем немного передохнуть."
                elif Type == "fine": #if she's not bothered
                                ch_r "А? Ладно."
                elif Type == "done": #after dropping out of the menu for lack of actions
                                ch_r "На этом все. . . пока."
        elif Girl is KittyX:
                if Type == "caught": #if you'd been recently caught doing stuff in public
                                ch_k "Я не хочу сейчас иметь с тобой никаких дел."
                elif Type == 5: #when the timer hits 5
                                ch_k "Давай немного передохнем."
                elif Type == "minute": #when asked to do something with no actions left
                                ch_k "Извини, [KittyX.Petname], но я немного устала."
                elif Type == "clean": #when you want them to clean up
                                ch_k "Что?"
                #from Wanting More dialogues:
                elif Type == "round1": #if "round2" not in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_k "Ты уверена, [KittyX.Petname]? Я не совсем. . . закончила."
                                else:
                                    ch_k "Ты уверен, [KittyX.Petname]? Я не совсем. . . закончила."
                elif Type == "addict": #elif Ch_Focus.Addict >= 50:
                                ch_k "Мне нужно больше контакта."
                elif Type == "wanting":
                                ch_k "Мне нужно больше внимания."
                elif Type == "doneunhappy":  #"Yeah, I'm done for now." if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                if not Player.Male:
                                    ch_k "Коза!"
                                else:
                                    ch_k "Козел!"
                elif Type == "donesatisfied":  #"Yeah, I'm done for now.", else
                                ch_k "Ну, наверное, хорошего понемногу. . ."
                elif Type == "triedunhappy": #"I gave it a shot."  if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCoun
                                if not Player.Male:
                                    ch_k "Коза!"
                                else:
                                    ch_k "Козел!"
                elif Type == "triedsatisfied": #"I gave it a shot." else
                                ch_k "Ну, наверное, хорошего понемногу. . ."
                elif Type == "didit": #"Hey, I did my part." if Ch_Focus.OCount > 2:
                                ch_k "Ну. . . да, но. . ."
                elif Type == "tapped": #"I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                ch_k "Ну. . . да, но[KittyX.like]. . ."
                elif Type == "somethingelse": # "Ok, we can try something else." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                ch_k "Хихи. . ."
                elif Type == "again": # "Again? Ok, fine." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                ch_k "Ты же меня знаешь. . ."
                elif Type == "breaktime": #if she's tired too
                                ch_k "Ну ладно, я тоже немного устала, [KittyX.Petname]. Давай передохнем. . ."
                                ch_k ". . .чуть-чуть."
                elif Type == "fine": #if she's not bothered
                                ch_k "Хорошо."

                elif Type == "done": #after dropping out of the menu for lack of actions
                                ch_k "На этом все. . . пока."
        elif Girl is EmmaX:
                if Type == "caught": #if you'd been recently caught doing stuff in public
                                ch_e "Я бы пока не хотела иметь с тобой никаких дел."
                elif Type == 5: #when the timer hits 5
                                ch_e "Думаю, нам обоим не помешает небольшой перерыв."
                elif Type == "minute": #when asked to do something with no actions left
                                ch_e "Извини, [EmmaX.Petname], но мне нужен перерыв."
                elif Type == "clean": #when you want them to clean up
                                ch_e "Что?"
                #from Wanting More dialogues:
                elif Type == "round1": #if "round2" not in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_e "Ты уверена, [EmmaX.Petname]? Ты точно ничего не забыла?"
                                else:
                                    ch_e "Ты уверен, [EmmaX.Petname]? Ты точно ничего не забыл?"
                elif Type == "addict": #elif Ch_Focus.Addict >= 50:
                                ch_e "Мне нужно больше."
                elif Type == "wanting":
                                ch_e "Боюсь, этого мне этого все еще недостаточно."
                elif Type == "doneunhappy":  #"Yeah, I'm done for now." if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                ch_e "Что ж, хорошо! Я тебе это припомню в следующий раз."
                elif Type == "donesatisfied":  #"Yeah, I'm done for now.", else
                                ch_e "Наверное, из меня плохой педагог."
                elif Type == "triedunhappy": #"I gave it a shot."  if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCoun
                                ch_e "Да, и от этого еще хуже. . ."
                elif Type == "triedsatisfied": #"I gave it a shot." else
                                if not Player.Male:
                                    ch_e "Полагаю, так и есть. . . жаль, что ты не способна на большее. . ."
                                else:
                                    ch_e "Полагаю, так и есть. . . жаль, что ты не способен на большее. . ."
                elif Type == "didit": #"Hey, I did my part." if Ch_Focus.OCount > 2:
                                ch_e "Но я все равно ожидала большего."
                elif Type == "tapped": #"I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                ch_e "Полагаю, тут уже ничего не поделаешь. . ."
                elif Type == "somethingelse": # "Ok, we can try something else." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                ch_e "Превосходно. . ."
                elif Type == "again": # "Again? Ok, fine." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                ch_e "Замечательно. . ."
                elif Type == "breaktime": #if she's tired too
                                ch_e "Пожалуй, я тоже устала, [EmmaX.Petname]. Нам пора отдохнуть. . ."
                elif Type == "fine": #if she's not bothered
                                ch_e "Хорошо."
                elif Type == "done": #after dropping out of the menu for lack of actions
                                ch_e "На этом все. . . пока."
        elif Girl is LauraX:
                if Type == "caught": #if you'd been recently caught doing stuff in public
                                ch_l "Лучше не трогай меня сейчас."
                elif Type == 5: #when the timer hits 5
                                if not Player.Male:
                                    ch_l "Ты выглядишь слегка уставшей, тебе стоит отдохнуть."
                                else:
                                    ch_l "Ты выглядишь слегка уставшим, тебе стоит отдохнуть."
                elif Type == "minute": #when asked to do something with no actions left
                                ch_l "Может, через пару минут, мне нужно отдохнуть."
                elif Type == "clean": #when you want them to clean up
                                ch_l "Что?"
                #from Wanting More dialogues:
                elif Type == "round1": #if "round2" not in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_l "Ты уверена, [LauraX.Petname]?"
                                else:
                                    ch_l "Ты уверен, [LauraX.Petname]?"
                                ch_l "Я могу еще раз. . . или два. . ."
                elif Type == "addict": #elif Ch_Focus.Addict >= 50:
                                ch_l "Мне нужно больше."
                elif Type == "wanting":
                                if not Player.Male:
                                    ch_l "Ты ничего не забыла?"
                                else:
                                    ch_l "Ты ничего не забыл?"
                elif Type == "doneunhappy":  #"Yeah, I'm done for now." if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                ch_l "Ты еще пожалеешь об этом."
                elif Type == "donesatisfied":  #"Yeah, I'm done for now.", else
                                if not Player.Male:
                                    ch_l "Эгоистка. . ."
                                else:
                                    ch_l "Эгоист. . ."
                elif Type == "triedunhappy": #"I gave it a shot."  if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCoun
                                if not Player.Male:
                                    ch_l "Могла бы и получше."
                                else:
                                    ch_l "Мог бы и получше."
                elif Type == "triedsatisfied": #"I gave it a shot." else
                                if not Player.Male:
                                    ch_l "Эгоистка. . ."
                                else:
                                    ch_l "Эгоист. . ."
                elif Type == "didit": #"Hey, I did my part." if Ch_Focus.OCount > 2:
                                ch_l "Ну. . . да, но. . ."
                elif Type == "tapped": #"I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                ch_l "Ну, ты всегда можешь попробовать что-нибудь другое. . ."
                elif Type == "somethingelse": # "Ok, we can try something else." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                ch_l "Хорошо. . ."
                elif Type == "again": # "Again? Ok, fine." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                ch_l "Хорошо. . ."
                elif Type == "breaktime": #if she's tired too
                                ch_l "Ага, я тоже немного устала. Давай передохнем. . ."
                                ch_l ". . .немного."
                elif Type == "fine": #if she's not bothered
                                ch_l "Хорошо."
                elif Type == "done": #after dropping out of the menu for lack of actions
                                ch_l "На этом все. . . по крайней мере, пока."
        elif Girl is JeanX:
                if Type == "caught": #if you'd been recently caught doing stuff in public
                                ch_j "Лучше не трогай меня сейчас."
                elif Type == 5: #when the timer hits 5
                                if not Player.Male:
                                    ch_j "Ты выглядишь слегка уставшей, тебе стоит отдохнуть."
                                else:
                                    ch_j "Ты выглядишь слегка уставшим, тебе стоит отдохнуть."
                elif Type == "minute": #when asked to do something with no actions left
                                ch_j "Дай мне минутку, ладно?"
                elif Type == "clean": #when you want them to clean up
                                ch_j "Что?"
                #from Wanting More dialogues:
                elif Type == "round1": #if "round2" not in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_j "Ты уверена, [JeanX.Petname]?"
                                else:
                                    ch_j "Ты уверен, [JeanX.Petname]?"
                                ch_j "Я могу еще разок. . . или два. . ."
                elif Type == "addict": #elif Ch_Focus.Addict >= 50:
                                ch_j "Мне нужно больше близости."
                                ch_j "Ты ведь не хочешь оставить меня в таком состояние?"
                elif Type == "wanting":
                                ch_j "Знаешь, тебе лучше бы закончить начатое."
                                ch_j "Ты ведь не хочешь оставить меня в таком состояние?"
                elif Type == "doneunhappy":  #"Yeah, I'm done for now." if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                ch_j "Ну что ж, жребий брошен."
                elif Type == "donesatisfied":  #"Yeah, I'm done for now.", else
                                ch_j "Бууу. . ."
                elif Type == "triedunhappy": #"I gave it a shot."  if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCoun
                                ch_j "Я бы назвала это по-другому. . ."
                elif Type == "triedsatisfied": #"I gave it a shot." else
                                ch_j "Бууу. . ."
                elif Type == "didit": #"Hey, I did my part." if Ch_Focus.OCount > 2:
                                if not Player.Male:
                                    ch_j "Плохо старалась. . ."
                                else:
                                    ch_j "Плохо старался. . ."
                elif Type == "tapped": #"I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                ch_j "Но твои руки не выглядят сломанными."
                elif Type == "somethingelse": # "Ok, we can try something else." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                ch_j "Хорошо. . ."
                elif Type == "again": # "Again? Ok, fine." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                ch_j "Хорошо. . ."
                elif Type == "breaktime": #if she's tired too
                                ch_j "Ладно, звучит неплохо. . ."
                elif Type == "fine": #if she's not bothered
                                ch_j "Хорошо."
                elif Type == "done": #after dropping out of the menu for lack of actions
                                ch_j "На этом все. . . по крайней мере, сейчас."
        elif Girl is StormX:
                if Type == "caught": #if you'd been recently caught doing stuff in public
                                ch_s "Сейчас я не хочу иметь с тобой никаких дел."
                elif Type == 5: #when the timer hits 5
                                if not Player.Male:
                                    ch_s "Думаю, нам обеим не помешает небольшой перерыв."
                                else:
                                    ch_s "Думаю, нам обоим не помешает небольшой перерыв."
                elif Type == "minute": #when asked to do something with no actions left
                                ch_s "Прости, [StormX.Petname], мне нужно отдохнуть."
                elif Type == "clean": #when you want them to clean up
                                if not Player.Male:
                                    ch_s "Ох, ты уверена?"
                                else:
                                    ch_s "Ох, ты уверен?"
                #from Wanting More dialogues:
                elif Type == "round1": #if "round2" not in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_s "Ты уверена, [StormX.Petname]? Ты точно ничего не забыла?"
                                else:
                                    ch_s "Ты уверен, [StormX.Petname]? Ты точно ничего не забыл?"
                elif Type == "addict": #elif Ch_Focus.Addict >= 50:
                                ch_s "Мне нужен контакт с тобой."
                elif Type == "wanting":
                                ch_s "Этого было недостаточно, чтобы удовлетворить меня."
                elif Type == "doneunhappy":  #"Yeah, I'm done for now." if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                if not Player.Male:
                                    ch_s "Возможно, мне стоит научить тебя быть более щедрой."
                                else:
                                    ch_s "Возможно, мне стоит научить тебя быть более щедрым."
                elif Type == "donesatisfied":  #"Yeah, I'm done for now.", else
                                if not Player.Male:
                                    ch_s "Возможно, мне стоит научить тебя быть более щедрой."
                                else:
                                    ch_s "Возможно, мне стоит научить тебя быть более щедрым."
                elif Type == "triedunhappy": #"I gave it a shot."  if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCoun
                                if not Player.Male:
                                    ch_s "Что ж, как я понимаю, на большее ты не способна. . ."
                                else:
                                    ch_s "Что ж, как я понимаю, на большее ты не способен. . ."
                elif Type == "triedsatisfied": #"I gave it a shot." else
                                if not Player.Male:
                                    ch_s "Что ж, как я понимаю, на большее ты не способна. . ."
                                else:
                                    ch_s "Что ж, как я понимаю, на большее ты не способен. . ."
                elif Type == "didit": #"Hey, I did my part." if Ch_Focus.OCount > 2:
                                ch_s "Я надеялась на большее. . ."
                elif Type == "tapped": #"I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                ch_s "Что ж, я не буду заставлять тебя перешагивать через себя. . ."
                elif Type == "somethingelse": # "Ok, we can try something else." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                ch_s "Благодарю."
                elif Type == "again": # "Again? Ok, fine." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                ch_s "Замечательно. . ."
                elif Type == "breaktime": #if she's tired too
                                ch_s "Мне тоже не помешает немного отдохнуть, [StormX.Petname]."
                elif Type == "fine": #if she's not bothered
                                ch_s "Все в порядке."
                elif Type == "done": #after dropping out of the menu for lack of actions
                                ch_s "Думаю, пока с тебя достаточно."
        elif Girl is JubesX:
                if Type == "caught": #if you'd been recently caught doing stuff in public
                                ch_v "Мне сейчас совсем не до тебя."
                elif Type == 5: #when the timer hits 5
                                ch_v "Слушай, мне бы не помешал перерыв, а как насчет тебя?"
                elif Type == "minute": #when asked to do something with no actions left
                                ch_v "Сначала мне не помешал бы небольшой перерыв."
                elif Type == "clean": #when you want them to clean up
                                ch_v "Что?"
                #from Wanting More dialogues:
                elif Type == "round1": #if "round2" not in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_v "Ты уверена, [JubesX.Petname]?"
                                else:
                                    ch_v "Ты уверен, [JubesX.Petname]?"
                                ch_v "Я могу продолжать. . ."
                elif Type == "addict": #elif Ch_Focus.Addict >= 50:
                                ch_v "Я немного опустошена, мне нужно больше контакта."
                elif Type == "wanting":
                                ch_v "Эй! Не оставляй меня в таком состояние."
                elif Type == "doneunhappy":  #"Yeah, I'm done for now." if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                ch_v "Нууу и отстой."
                elif Type == "donesatisfied":  #"Yeah, I'm done for now.", else
                                ch_v "Как эгоистично. . ."
                elif Type == "triedunhappy": #"I gave it a shot."  if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCoun
                                ch_v "Нууу, попробуй еще раз."
                elif Type == "triedsatisfied": #"I gave it a shot." else
                                ch_v "Как эгоистично. . ."
                elif Type == "didit": #"Hey, I did my part." if Ch_Focus.OCount > 2:
                                ch_v "Ага, но. . . продолжай. . ."
                elif Type == "tapped": #"I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                ch_v "Нууу, ты всегда можешь попробовать что-нибудь другое. . ."
                elif Type == "somethingelse": # "Ok, we can try something else." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                ch_v "Клево. . ."
                elif Type == "again": # "Again? Ok, fine." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                ch_v "Ага. . ."
                elif Type == "breaktime": #if she's tired too
                                ch_v "Конечно, я думаю, мы можем сделать небольшой перерыв. . ."
                elif Type == "fine": #if she's not bothered
                                ch_v "Конечно, хорошо."
                elif Type == "done": #after dropping out of the menu for lack of actions
                                ch_v "Хорошо, пока этого должно быть достаточно."
        elif Girl is GwenX:
                if Type == "caught": #if you'd been recently caught doing stuff in public
                                ch_g "С меня хватит твоих проделок."
                elif Type == 5: #when the timer hits 5
                                ch_g "Мне бы не помешал перерыв."
                elif Type == "minute": #when asked to do something with no actions left
                                ch_g "Дай мне минутку, мне нужно отдохнуть."
                elif Type == "clean": #when you want them to clean up
                                ch_g "Что?"
                #from Wanting More dialogues:
                elif Type == "round1": #if "round2" not in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_g "Ты уверена, [GwenX.Petname]?"
                                else:
                                    ch_g "Ты уверен, [GwenX.Petname]?"
                                ch_g "Я бы хотела продолжения. . ."
                elif Type == "addict": #elif Ch_Focus.Addict >= 50:
                                h_g "Я думаю, ты забываешь о небольшой. . . проблеме."
                elif Type == "wanting":
                                ch_g "Ты же не собираешься меня вот так просто отпускать?"
                elif Type == "doneunhappy":  #"Yeah, I'm done for now." if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                ch_g "Черт!"
                elif Type == "donesatisfied":  #"Yeah, I'm done for now.", else
                                ch_g "Это не хорошо. . ."
                elif Type == "triedunhappy": #"I gave it a shot."  if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCoun
                                ch_g "И ты называешь это попыткой?"
                elif Type == "triedsatisfied": #"I gave it a shot." else
                                ch_g "Пожалуй. . ."
                elif Type == "didit": #"Hey, I did my part." if Ch_Focus.OCount > 2:
                                ch_g "Ну. . . да, но. . ."
                elif Type == "tapped": #"I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                ch_g "Ну, ты всегда можешь попробовать что-нибудь другое. . ."
                elif Type == "somethingelse": # "Ok, we can try something else." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                ch_g "Здорово. . ."
                elif Type == "again": # "Again? Ok, fine." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_g "Всегда готова, это хорошо. . ."
                                else:
                                    ch_g "Всегда готов, это хорошо. . ."
                elif Type == "breaktime": #if she's tired too
                                ch_g "Ага, ладно. Мы можем сделать перерыв. . ."
                elif Type == "fine": #if she's not bothered
                                ch_g "Ох, ладно."
                elif Type == "done": #after dropping out of the menu for lack of actions
                                ch_g "Ну вот и все. . . по крайней мере, пока."
        elif Girl is BetsyX:
                if Type == "caught": #if you'd been recently caught doing stuff in public
                                ch_b "Я бы предпочла не привлекать к себе лишнего внимания."
                elif Type == 5: #when the timer hits 5
                                ch_b "Мне бы не помешал небольшой отдых."
                elif Type == "minute": #when asked to do something with no actions left
                                ch_b "Возможно, немного позже, мне нужно отдохнуть."
                elif Type == "clean": #when you want them to clean up
                                ch_b "М?"
                #from Wanting More dialogues:
                elif Type == "round1": #if "round2" not in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_b "Ты совершенно уверена, [BetsyX.Petname]?"
                                else:
                                    ch_b "Ты совершенно уверен, [BetsyX.Petname]?"
                                ch_b "Я бы предпочла продолжить. . ."
                elif Type == "addict": #elif Ch_Focus.Addict >= 50:
                                ch_b "Я думаю, ты забываешь кое-какой. . . проблеме."
                elif Type == "wanting":
                                if not Player.Male:
                                    ch_b "Боюсь, ты оставила меня весьма неудовлетворенной."
                                else:
                                    ch_b "Боюсь, ты оставил меня весьма неудовлетворенной."
                elif Type == "doneunhappy":  #"Yeah, I'm done for now." if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                ch_b "Какая жалость."
                elif Type == "donesatisfied":  #"Yeah, I'm done for now.", else
                                ch_b "Жаль. . ."
                elif Type == "triedunhappy": #"I gave it a shot."  if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCoun
                                ch_b "Это ты так думаешь. . ."
                elif Type == "triedsatisfied": #"I gave it a shot." else
                                ch_b "Пожалуй. . ."
                elif Type == "didit": #"Hey, I did my part." if Ch_Focus.OCount > 2:
                                ch_b "И даже очень. . ."
                elif Type == "tapped": #"I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                ch_b "Есть доступные альтернативы. . ."
                elif Type == "somethingelse": # "Ok, we can try something else." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                ch_b "Замечательно. . ."
                elif Type == "again": # "Again? Ok, fine." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                ch_b "Благодарю. . ."
                elif Type == "breaktime": #if she's tired too
                                ch_b "Пожалуй, нам не помешает немного отдохнуть. . ."
                elif Type == "fine": #if she's not bothered
                                ch_b "Ох, хорошо."
                elif Type == "done": #after dropping out of the menu for lack of actions
                                ch_b "Вот и все. . . на данный момент."
        elif Girl is DoreenX:
                if Type == "caught": #if you'd been recently caught doing stuff in public
                                ch_d "Я рада даже просто быть здесь, я не хочу проблем."
                elif Type == 5: #when the timer hits 5
                                cch_d "Думаю, мне бы не помешало отдохнуть."
                elif Type == "minute": #when asked to do something with no actions left
                                ch_d "Давай позже, мне нужно отдохнуть."
                elif Type == "clean": #when you want them to clean up
                                ch_d "Что? Где?"
                #from Wanting More dialogues:
                elif Type == "round1": #if "round2" not in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_d "Ты уверена, [DoreenX.Petname]?"
                                else:
                                    ch_d "Ты уверен, [DoreenX.Petname]?"
                                ch_d "Я бы хотела продолжить. . ."
                elif Type == "addict": #elif Ch_Focus.Addict >= 50:
                                ch_d "Я все еще чувствую напряжение. . ."
                elif Type == "wanting":
                                h_d "Мне, эм, нужна небольшая помощь. . ."
                elif Type == "doneunhappy":  #"Yeah, I'm done for now." if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                ch_d "Aw!"
                elif Type == "donesatisfied":  #"Yeah, I'm done for now.", else
                                ch_d "Оу!"
                elif Type == "triedunhappy": #"I gave it a shot."  if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCoun
                                ch_d "Серьезно? . ."
                elif Type == "triedsatisfied": #"I gave it a shot." else
                                ch_d "Ага, наверное. . ."
                elif Type == "didit": #"Hey, I did my part." if Ch_Focus.OCount > 2:
                                ch_d "Пожалуй. . ."
                elif Type == "tapped": #"I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                ch_d "Ну, мы могли бы заняться чем-нибудь другим. . ."
                elif Type == "somethingelse": # "Ok, we can try something else." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                ch_d "Здорово!"
                elif Type == "again": # "Again? Ok, fine." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                ch_d "Отлично. . ."
                elif Type == "breaktime": #if she's tired too
                                ch_d "Думаю, мы можем отдохнуть. . ."
                elif Type == "fine": #if she's not bothered
                                ch_d "Ох, ладно. . ."
                elif Type == "done": #after dropping out of the menu for lack of actions
                                ch_d "На этом все. . . пока."
        elif Girl is WandaX:
                if Type == "caught": #if you'd been recently caught doing stuff in public
                                ch_w "Послушай, я только недавно вышла, я не хочу проблем."
                elif Type == 5: #when the timer hits 5
                                ch_w "Думаю, мне не помешал бы перерыв."
                elif Type == "minute": #when asked to do something with no actions left
                                ch_w "Дай мне минутку, мне нужно отдохнуть."
                elif Type == "clean": #when you want them to clean up
                                ch_w "Да? Где?"
                #from Wanting More dialogues:
                elif Type == "round1": #if "round2" not in Ch_Focus.RecentActions:
                                if not Player.Male:
                                    ch_w "Ты уверена, [WandaX.Petname]?"
                                else:
                                    ch_w "Ты уверен, [WandaX.Petname]?"
                                ch_w "Я могу продолжать. . ."
                elif Type == "addict": #elif Ch_Focus.Addict >= 50:
                                ch_w "Мне очень нужно больше внимания. . ."
                elif Type == "wanting":
                                ch_w "Мне не помешала бы помощь. . ."
                elif Type == "doneunhappy":  #"Yeah, I'm done for now." if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCount:
                                if not Player.Male:
                                    ch_w "Слабачка."
                                else:
                                    ch_w "Слабак."
                elif Type == "donesatisfied":  #"Yeah, I'm done for now.", else
                                ch_w "Да ладно тебе. . ."
                elif Type == "triedunhappy": #"I gave it a shot."  if "unsatisfied" in Ch_Focus.RecentActions and not Ch_Focus.OCoun
                                ch_w "Правда? . ."
                elif Type == "triedsatisfied": #"I gave it a shot." else
                                ch_w "Ну, раз так. . ."
                elif Type == "didit": #"Hey, I did my part." if Ch_Focus.OCount > 2:
                                ch_w "Конечно. . ."
                elif Type == "tapped": #"I'm tapped out for the moment, let's try again later." if not Player.Semen:
                                ch_w "Это не повод останавливаться. . ."
                elif Type == "somethingelse": # "Ok, we can try something else." if MultiAction and "round2" not in Ch_Focus.RecentActions:
                                ch_w "Отлично."
                elif Type == "again": # "Again? Ok, fine." if MultiAction and "round2" in Ch_Focus.RecentActions:
                                ch_w "Клево. . ."
                elif Type == "breaktime": #if she's tired too
                                ch_w "Думаю, можно и отдохнуть. . ."
                elif Type == "fine": #if she's not bothered
                                ch_w "Конечно. . ."
                elif Type == "done": #after dropping out of the menu for lack of actions
                                ch_w "Ладно, пора отдохнуть."

        return
# end Sex_Menu_Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

##  Ch_Focus.Masturbating //////////////////////////////////////////////////////////////////////
label Girl_Masturbate:  #rkeljsvgb
    # Modification mode
    if is_playing_music(audio.masturbate):
        $ play_music(name=audio.masturbate, loop=True)
    # -----------------

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Ch_Focus)
    if Ch_Focus.Mast:
        $ Tempmod += 10
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 3
    if Ch_Focus.SEXP >= 50:
        $ Tempmod += 25
    elif Ch_Focus.SEXP >= 30:
        $ Tempmod += 15
    elif Ch_Focus.SEXP >= 15:
        $ Tempmod += 5
    if Ch_Focus.Lust >= 90:
        $ Tempmod += 20
    elif Ch_Focus.Lust >= 75:
        $ Tempmod += 5
    if "exhibitionist" in Ch_Focus.Traits:
        $ Tempmod += (3*Taboo)
    if Ch_Focus in Player.Harem or "sex friend" in Ch_Focus.Petnames:
        $ Tempmod += 10
    elif "ex" in Ch_Focus.Traits:
        $ Tempmod -= 40
    if Ch_Focus.ForcedCount and not Ch_Focus.Forced:
        $ Tempmod -= 5 * Ch_Focus.ForcedCount

    $ Approval = ApprovalCheck(Ch_Focus, 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)

    $ Ch_Focus.DrainWord("unseen",1,0) #She sees you, so remove unseens

    if Situation == "join":       # This triggers if you ask to join in
                $ Player.AddWord(1,"join")
                if Approval > 1 or (Approval and Ch_Focus.Lust >= 50):
                    menu:
                        extend ""
                        "Может, тебе протянуть руку помощи? . ."  if Player.Semen and Ch_Focus.Action:
                                $ Ch_Focus.Statup("Love", 90, 1)
                                $ Ch_Focus.Statup("Obed", 50, 2)
                                $ Ch_Focus.FaceChange("sexy")
                                if Ch_Focus is RogueX:
                                        ch_r "Ну, [RogueX.Petname], думаю, мне и правда пригодится твоя помощь. . ."
                                elif Ch_Focus is KittyX:
                                        ch_k "Эм, знаешь, может, начнешь сверху?"
                                elif Ch_Focus is EmmaX:
                                        ch_e "Хм, и правда, мои руки скйчас сильно заняты. . ."
                                elif Ch_Focus is LauraX:
                                        if not Player.Male:
                                            ch_l "А? Ну, думаю, ты могла бы заняться моей грудью?"
                                        else:
                                            ch_l "А? Ну, думаю, ты мог бы заняться моей грудью?"
                                elif Ch_Focus is JeanX:
                                        ch_j "Хмм, ладно, сожми их хорошенько. . ."
                                elif Ch_Focus is StormX:
                                        ch_s "Ты можешь помассировать мне грудь. . ."
                                elif Ch_Focus is JubesX:
                                        ch_v "Нууу, ладно, поможешь мне?"
                                elif Ch_Focus is GwenX:
                                        if not Player.Male:
                                            ch_g "Ну. . . Думаю, ты могла бы помочь им?"
                                        else:
                                            ch_g "Ну. . . Думаю, ты мог бы помочь им?"
                                elif Ch_Focus is BetsyX:
                                        ch_b "Что ж. . . можешь помочь с верхом?"
                                elif Ch_Focus is DoreenX:
                                        ch_d "Ну. . . поможешь с верхом?"
                                elif Ch_Focus is WandaX:
                                        ch_w "Ну. . . ты можешь поработать над моими сиськами."
                                $ Ch_Focus.Statup("Obed", 70, 2)
                                $ Ch_Focus.Statup("Inbt", 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ Ch_Focus.Mast += 1
                                jump Girl_M_Cycle
                        "Может, тебе нужна помощь? Я могу. . . ну, тебе решать." if Player.Semen and Ch_Focus.Action:
                                $ Ch_Focus.Statup("Love", 70, 2)
                                $ Ch_Focus.Statup("Love", 90, 1)
                                $ Ch_Focus.FaceChange("sexy")
                                if Ch_Focus is RogueX:
                                        ch_r "Хорошо, [RogueX.Petname], не откажусь от твоего предложения. . ."
                                elif Ch_Focus is KittyX:
                                        ch_k "Я[KittyX.like]с радостью приму от тебя помощь. . ."
                                elif Ch_Focus is EmmaX:
                                        ch_e "Полагаю, мне пригодится больше внимания. . ."
                                elif Ch_Focus is LauraX:
                                        ch_l "Ага, наверное? . ."
                                elif Ch_Focus is JeanX:
                                        ch_j "Конечно. . ."
                                elif Ch_Focus is StormX:
                                        ch_s "Ты можешь помассировать мне грудь. . ."
                                elif Ch_Focus is JubesX:
                                        ch_v "Клево. . ."
                                elif Ch_Focus is GwenX:
                                        ch_g "О, спасибо за предложение. . ."
                                elif Ch_Focus is BetsyX:
                                        ch_b "Ох, прекрасное предложение. . ."
                                elif Ch_Focus is DoreenX:
                                        ch_d "Спасибо за милое предложение. . . я им воспользуюсь."
                                elif Ch_Focus is WandaX:
                                        if not Player.Male:
                                            ch_w "Хорошо, ты могла бы поработать над моими сиськами. . ."
                                        else:
                                            ch_w "Хорошо, ты мог бы поработать над моими сиськами. . ."
                                $ Ch_Focus.Statup("Obed", 70, 2)
                                $ Ch_Focus.Statup("Inbt", 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ Ch_Focus.Mast += 1
                                jump Girl_M_Cycle
                        "Почему бы нам не позаботиться друг о друге?" if Player.Semen and Ch_Focus.Action:
                                $ Ch_Focus.FaceChange("sexy")
                                if Ch_Focus is RogueX:
                                        ch_r "Что ты имеешь в виду?"
                                elif Ch_Focus is KittyX:
                                        ch_k "Думаю, это можно. . ."
                                elif Ch_Focus is EmmaX:
                                        ch_e "Полагаю, ты заслуживаешь немного внимания. . ."
                                elif Ch_Focus is LauraX:
                                        ch_l "Например?"
                                elif Ch_Focus is JeanX:
                                        ch_j "Например?"
                                elif Ch_Focus is StormX:
                                        ch_s "Ох, что ты имеешь в виду?"
                                elif Ch_Focus is JubesX:
                                        cch_v "Например?"
                                elif Ch_Focus is GwenX:
                                        ch_g "Что именно ты предлагаешь?"
                                elif Ch_Focus is BetsyX:
                                        ch_b "Что ты имеешь в виду?"
                                elif Ch_Focus is DoreenX:
                                        ch_d "О, например?"
                                elif Ch_Focus is WandaX:
                                        ch_w "Как именно?"
                                $ renpy.pop_call()          #removes the call to this label
                                return                      #returns to sexmenu=
                        "Похоже, у тебя все под контролем. . .":
                                if Ch_Focus.Lust >= 50:
                                    $ Ch_Focus.Statup("Love", 70, 2)
                                    $ Ch_Focus.Statup("Love", 90, 1)
                                    $ Ch_Focus.FaceChange("sexy")
                                    if Ch_Focus is RogueX:
                                            ch_r "Ну, [RogueX.Petname], наверное, так и есть. . ."
                                    elif Ch_Focus is KittyX:
                                            cch_k "Ну, думаю, да. . ."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Значит, предпочитаешь смотреть. . ."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Я уже совсем на пределе. . ."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Угу. . ."
                                    elif Ch_Focus is StormX:
                                            ch_s "Как я понимаю, ты предпочитаешь смотреть. . ."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Конечно, секунду. . ."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Ага, я уже почти. . ."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Конечно, но помощь не бывает лишней. . ."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Я уже. . . почти. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Ох. .  еще секунду. . ."
                                    $ Ch_Focus.Statup("Obed", 80, 3)
                                    $ Ch_Focus.Statup("Inbt", 80, 5)
                                    jump Girl_M_Cycle
                                elif ApprovalCheck(Ch_Focus, 1200):
                                    $ Ch_Focus.FaceChange("sly")
                                    if Ch_Focus is RogueX:
                                            ch_r "Так и есть, но, думаю, мне уже хватит. . ."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Ага. . . но мне, как бы, уже хватит. . ."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Верно, но я не собиралась устраивать никаких представлений."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Ага. . . но я могу прерваться. . ."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Ага. . . но я могу прерваться. . ."
                                    elif Ch_Focus is StormX:
                                            ch_s "Верно, но я не ждала зрителей."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Ага. . . Но я могла бы сделать перерыв. . ."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Конечно, но мне бы не помешала помощь. . ."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Конечно, но помощь не бывает лишней. . ."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Ага. . . но вдвоем всегда веселее. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Знаешь, так и было, но. . ."
                                else:
                                    $ Ch_Focus.FaceChange("angry")
                                    if Ch_Focus is RogueX:
                                            if not Player.Male:
                                                ch_r "Так и было, но ты мне весь настрой сбила."
                                            else:
                                                ch_r "Так и было, но ты мне весь настрой сбил."
                                    elif Ch_Focus is KittyX:
                                            if not Player.Male:
                                                ch_k "Пфф, так и -было.- Пока ты все не испортила."
                                            else:
                                                ch_k "Пфф, так и -было.- Пока ты все не испортил."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Так и было, но теперь момент испорчен. . ."
                                    elif Ch_Focus is LauraX:
                                            if not Player.Male:
                                                ch_l "-так и было, пока ты все не испортила."
                                            else:
                                                ch_l "-так и было, пока ты все не испортил."
                                    elif Ch_Focus is JeanX:
                                            ch_j "-так и -было.-"
                                    elif Ch_Focus is StormX:
                                            if not Player.Male:
                                                ch_s "Что ж, все было замечательно, пока ты не прервала меня. . ."
                                            else:
                                                ch_s "Что ж, все было замечательно, пока ты не прервал меня. . ."
                                    elif Ch_Focus is JubesX:
                                            ch_v "-Было-"
                                    elif Ch_Focus is GwenX:
                                            ch_g "-но потом вторгся народ Огня. . ."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "-Так и было, прежде чем меня прервали. . ."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "-Было,- но теперь я не уверена. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Черт, теперь мне придется начинать сначала, после того как ты уйдешь."

                #else: You've failed all checks so she kicks you out.
                $ Ch_Focus.ArmPose = 1
                $ Ch_Focus.OutfitChange()
                $ Ch_Focus.Action -= 1
                $ Player.Statup("Focus", 50, 30)
                call Checkout(1)
                $ Line = 0
                $ Situation = 0
                $ renpy.pop_call()          #removes the call to this label
                if Approval:
                        $ Ch_Focus.FaceChange("bemused", 2)
                        if Ch_Focus is RogueX:
                            if bg_current == Ch_Focus.Home:
                                if not Player.Male:
                                    ch_r "Так, зачем ты вообще пришла, [RogueX.Petname]?"
                                else:
                                    ch_r "Так, зачем ты вообще пришел, [RogueX.Petname]?"
                            else:
                                ch_r "Я. . . не ожидала тебя тут увидеть, [RogueX.Petname]. . ."
                        elif Ch_Focus is KittyX:
                            if bg_current == Ch_Focus.Home:
                                ch_k "Что ты[KittyX.like]вообще здесь делаешь?"
                            else:
                                ch_k "Я[KittyX.like]не ожидала увидеть тебя здесь. . ."
                        elif Ch_Focus is EmmaX:
                            if bg_current == Ch_Focus.Home:
                                ch_e "Что ты вообще делаешь в моей комнате?"
                            else:
                                ch_e "Я не ждала гостей. . ."
                        elif Ch_Focus is LauraX:
                            if bg_current == Ch_Focus.Home:
                                ch_l "Почему ты в моей комнате?"
                            else:
                                ch_l "Я никого не ждала. . ."
                        elif Ch_Focus is JeanX:
                            if bg_current == Ch_Focus.Home:
                                ch_j "Почему ты в моей комнате?"
                            else:
                                ch_j "Я никого не приглашала. . ."
                        elif Ch_Focus is StormX:
                            if bg_current == Ch_Focus.Home:
                                ch_s "Что привело тебя сюда?"
                            else:
                                ch_s "Я не ожидала, что меня прервут. . ."
                        elif Ch_Focus is JubesX:
                            if bg_current == Ch_Focus.Home:
                                ch_v "Итак, что ты здесь делаешь?"
                            else:
                                ch_v "Я не думала, что кто-нибудь зайдет. . ."
                        elif Ch_Focus is GwenX:
                            if bg_current == Ch_Focus.Home:
                                ch_g "Так, что ты делаешь в моей комнате?"
                            else:
                                ch_g "Я не ожидала, что кто-то появится. . ."
                        elif Ch_Focus is BetsyX:
                            if bg_current == Ch_Focus.Home:
                                ch_b "У тебя какое-то дело ко мне?"
                            else:
                                ch_b "Я не ждала компании. . ."
                        elif Ch_Focus is DoreenX:
                            if bg_current == Ch_Focus.Home:
                                ch_d "Тебе что-то нужно?"
                            else:
                                ch_d "Я не ожидала, что ты заглянешь. . ."
                        elif Ch_Focus is WandaX:
                            if bg_current == Ch_Focus.Home:
                                ch_w "Что ты ищешь?"
                            else:
                                ch_w "Я не ожидала твоего визита. . ."
                        $ Ch_Focus.Blush = 1
                else:
                        $ Ch_Focus.Statup("Love", 200, -5)
                        $ Ch_Focus.FaceChange("angry")
                        if "classcaught" not in Ch_Focus.RecentActions:
                                $ Ch_Focus.RecentActions.append("angry")
                                $ Ch_Focus.DailyActions.append("angry")
                        if bg_current == Ch_Focus.Home:
                            if Ch_Focus is RogueX:
                                    ch_r "Хорошо, я буду тебе признательна, если ты сейчас уйдешь. Не думаешь, что тебе стоит начать стучаться?"
                            elif Ch_Focus is KittyX:
                                    if not Player.Male:
                                        ch_k "Если ты сразу не поняла, я вообще-то была немного -занята.- Не думала иногда стучаться?"
                                    else:
                                        ch_k "Если ты сразу не понял, я вообще-то была немного -занята.- Не думал иногда стучаться?"
                            elif Ch_Focus is EmmaX:
                                    if not Player.Male:
                                        ch_e "Если ты не заметила, мне нужно кое с чем закончить, так что оставь меня одну. . ."
                                    else:
                                        ch_e "Если ты не заметил, мне нужно кое с чем закончить, так что оставь меня одну. . ."
                            elif Ch_Focus is LauraX:
                                    ch_l "Я была немного занята, так что убирайся."
                            elif Ch_Focus is JeanX:
                                    ch_j "Я была занята, убирайся."
                            elif Ch_Focus is StormX:
                                    ch_s "Боюсь, у меня сейчас нет времени возиться с тобой. . ."
                            elif Ch_Focus is JubesX:
                                    ch_v "Мне тут кое с чем нужно закончить, пока."
                            elif Ch_Focus is GwenX:
                                    ch_g "Мне нужно кое-что сделать, так что выметайся."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Я сейчас очень занята, поэтому, прошу, уходи."
                            elif Ch_Focus is DoreenX:
                                    ch_d "Я, эм. . . сейчас занята, поэтому, пожалуйста, уходи."
                            elif Ch_Focus is WandaX:
                                    ch_w "Мне кое-что нужно уладить, увидимся позже."
                            "[Ch_Focus.Name] выгоняет вас из своей комнаты."
                            $ renpy.pop_call()
                            jump Campus_Map
                        else:
                            if Ch_Focus is RogueX:
                                    ch_r "Ну, если ты не против, я пошла. В следующий раз стучись, ладно?"
                            elif Ch_Focus is KittyX:
                                    ch_k "Ну. . . Я собираюсь уходить. В следующий раз стучись, ладно?"
                                    hide Kitty_Sprite with easeoutbottom
                            elif Ch_Focus is EmmaX:
                                if bg_current == "bg classroom":
                                    ch_e "В общем. . ."
                                    return
                                else:
                                    ch_e "Я, пожалуй, пойду, если ты не против."
                            elif Ch_Focus is LauraX:
                                    ch_l "Я собираюсь уходить. Тебе стоит научиться стучаться."
                            elif Ch_Focus is JeanX:
                                    ch_j "Я ухожу, и, может быть, в будущем будешь стучаться?"
                            elif Ch_Focus is StormX:
                                    ch_s "Я пошла, если ты не возражаешь."
                            elif Ch_Focus is JubesX:
                                    ch_v "Уфф, мне все равно пора идти."
                            elif Ch_Focus is GwenX:
                                    ch_g "Я ухожу, а ты запомни, что в следующий раз нужно стучаться."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Мне пора уходить, но, возможно, в будущем тебе стоит стучаться?"
                            elif Ch_Focus is DoreenX:
                                    ch_d "Мне пора идти, но, может быть, теперь ты будешь сначала стучаться?"
                            elif Ch_Focus is WandaX:
                                    ch_w "Ладно, мне пора идти, но ты не думаешь, что сперва стоит стучаться?"
                            call Remove_Girl(Ch_Focus)
                return                      #returns to sexmenu, which returns to original
    #End of "Join" option



    if Situation == Ch_Focus:
                #Girl auto-starts
                if Approval > 2:                                                      # fix, add auto stuff here
                        if Ch_Focus.PantsNum() == 5:
                            "[Ch_Focus.Name] опускает руку вниз и задирает юбку."
                            $ Ch_Focus.Upskirt = 1
                        elif Ch_Focus.PantsNum() >= 6:
                            "[Ch_Focus.Name] опускает свою руку вниз прямиком под шорты."
                        elif Ch_Focus.HoseNum() >= 5:
                            "[Ch_Focus.Name] опускает свою руку вниз прямиком под [get_clothing_name(Ch_Focus.Hose_key, vin)]."
                        elif Ch_Focus.Panties:
                            "[Ch_Focus.Name] опускает свою руку вниз прямиком в [get_clothing_name(Ch_Focus.Panties_key, vin)]."
                        else:
                            "[Ch_Focus.Name] опускает руку вниз к своей киске."
                        $ Ch_Focus.SeenPanties = 1
                        call Girl_First_Bottomless(Ch_Focus,1)
                        "Она медленно начинает ласкать себя."
                        menu:
                            "Что будете делать?"
                            "Ничего не делать.":
                                    $ Ch_Focus.Statup("Inbt", 80, 3)
                                    $ Ch_Focus.Statup("Inbt", 60, 2)
                                    "[Ch_Focus.Name] начинает мастурбировать."
                            "Подбодрить.":
                                    $ Ch_Focus.FaceChange("sexy, 1")
                                    $ Ch_Focus.Statup("Inbt", 80, 3)
                                    ch_p "[Ch_Focus.Pet], до чего же это сексуально."
                                    $ Ch_Focus.NameCheck() #checks reaction to petname
                                    "Вы откидываетесь назад и наслаждаетесь представлением."
                                    $ Ch_Focus.Statup("Love", 80, 1)
                                    $ Ch_Focus.Statup("Obed", 90, 1)
                                    $ Ch_Focus.Statup("Obed", 50, 2)
                            "Сказать ей остановиться.":
                                    $ Ch_Focus.FaceChange("surprised")
                                    $ Ch_Focus.Statup("Inbt", 70, 1)
                                    ch_p "[Ch_Focus.Pet], давай пока не будем."
                                    $ Ch_Focus.NameCheck() #checks reaction to petname
                                    "[Ch_Focus.Name] убирает от себя руки."
                                    $ Ch_Focus.OutfitChange()
                                    $ Ch_Focus.Statup("Obed", 90, 1)
                                    $ Ch_Focus.Statup("Obed", 50, 1)
                                    $ Ch_Focus.Statup("Obed", 30, 2)
                                    return
                        jump Girl_M_Prep
                else:
                        $ Tempmod = 0                               # fix, add auto stuff here
                        $ Trigger2 = 0
                return
    #End if Girl initiates this action

    #first time
    if not Ch_Focus.Mast:
            $ Ch_Focus.FaceChange("surprised", 2)
            $ Ch_Focus.Mouth = "kiss"
            if Ch_Focus is RogueX:
                    ch_r "Ты хочешь, чтобы я кончила, пока ты смотришь?"
            elif Ch_Focus is KittyX:
                    ch_k "Ты хочешь, чтобы я. . . потрогала себя?"
                    ch_k "А ты в это время будешь. . . смотреть?"
            elif Ch_Focus is EmmaX:
                    ch_e "Значит, тебе нравится хорошее представление. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Так ты хочешь, чтобы я мастурбировала, пока ты смотришь?"
            elif Ch_Focus is JeanX:
                    ch_j "О, так ты хочешь посмотреть, как я кончу?"
            elif Ch_Focus is StormX:
                    ch_s "О, так тебе нравятся наблюдать? . ."
            elif Ch_Focus is JubesX:
                    ch_v "Значит, тебе нравится смотреть, как я мастурбирую?"
            elif Ch_Focus is GwenX:
                    ch_g "О, ты любишь смотреть, да?"
            elif Ch_Focus is BetsyX:
                    ch_b "Ох, ты, значит, у нас вуайерист?"
            elif Ch_Focus is DoreenX:
                    ch_d "Ох. . . ты, эм. . . ты хочешь понаблюдать за мной. . ?"
            elif Ch_Focus is WandaX:
                    ch_w "О, значит, тебе нравится наблюдать. . &"
            if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    if Ch_Focus is RogueX:
                            ch_r "Значит, ты хочешь только смотреть?"
                    elif Ch_Focus is KittyX:
                            ch_k "Значит, ты хочешь -только- смотреть. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "но. . . ты будешь. . . -только- смотреть?"
                    elif Ch_Focus is LauraX:
                            ch_l "И ты будешь -только- смотреть. . ?"
                    elif Ch_Focus is JeanX:
                            ch_j "Но будешь -только- смотреть, да? . ."
                    elif Ch_Focus is StormX:
                            ch_s "и это все, чего ты хочешь?"
                    elif Ch_Focus is JubesX:
                            ch_v "И не более? . ."
                    elif Ch_Focus is GwenX:
                            ch_g "И ты будешь держать руки при себе? . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "И не будешь распускать руки? . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "-и ты не будешь распускать руки? . ."
                    elif Ch_Focus is WandaX:
                            ch_w "-ты будешь держать свои руки при себе? . ."


    #First time dialog
    if not Ch_Focus.Mast and Approval:
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Love", 70, -3, 1)
                $ Ch_Focus.Statup("Love", 20, -2, 1)
            elif Ch_Focus.Love >= Ch_Focus.Obed and Ch_Focus.Love >= Ch_Focus.Inbt:
                $ Ch_Focus.FaceChange("sexy")
                $ Ch_Focus.Brows = "sad"
                $ Ch_Focus.Mouth = "smile"
                if Ch_Focus is RogueX:
                        ch_r "С тех пор как моя личная жизнь стала полна. . . ограничений, я \"набила\" руку."
                elif Ch_Focus is KittyX:
                        ch_k "Это довольно -интимное- дело. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Обычно я не показываю себя с этой стороны . . ."
                elif Ch_Focus is LauraX:
                        if not Player.Male:
                            ch_l "Я не знаю, ты уверена?"
                        else:
                            ch_l "Я не знаю, ты уверен?"
                elif Ch_Focus is JeanX:
                        ch_j "Что ж. . ."
                elif Ch_Focus is StormX:
                        ch_s "Обычно в такие моменты я нахожусь одна. . ."
                elif Ch_Focus is JubesX:
                        if not Player.Male:
                            ch_v "Я не знаю, ты уверена?"
                        else:
                            ch_v "Я не знаю, ты уверен?"
                elif Ch_Focus is GwenX:
                        ch_g "Ну, я не привыкла к зрителям. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Честно говоря. . . я не привыкла к зрителям. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Эм. . . я не привыкла к тому, что на меня смотрят. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Я не уверена, хочу ли я показывать тебе свои фокусы. . ."
            elif (Ch_Focus.Obed >= Ch_Focus.Inbt) or (Ch_Focus is JeanX and JeanX.Obed >= (JeanX.Inbt - JeanX.IX)):
                $ Ch_Focus.FaceChange("normal")
                if Ch_Focus is RogueX:
                        ch_r "Если ты так этого хочешь, [RogueX.Petname]. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Ладно, я не против, [KittyX.Petname]. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Если тебе нравится такое, [EmmaX.Petname]. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Если тебе нравится такое. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Если тебе нравится такое. . ."
                elif Ch_Focus is StormX:
                        ch_s "Если тебе нравится смотреть, [StormX.Petname]. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Если тебе нравится такое. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Возможно, я могла бы сделать это. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Возможно, я не против. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Думаю, это не так уж плохо. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Думаю, от этого не будет никакого вреда. . ."
            else: # Uninhibited
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Mouth = "smile"
                if Ch_Focus is RogueX:
                        ch_r "Думаю, так даже интереснее. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Это даже может быть весело. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Мне нравятся хорошие выступления. . ."
                elif Ch_Focus is LauraX:
                        ch_l "У меня есть немного свободного времени. . ."
                elif Ch_Focus is JeanX:
                        ch_j "У меня есть немного времени. . ."
                elif Ch_Focus is StormX:
                        ch_s "Я не возражаю против зрителей . . ."
                elif Ch_Focus is JubesX:
                        ch_v "Я могла бы немного снять стресс. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Я немного волнуюсь. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Я немного волнуюсь. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Мне бы не помешало немного снять стресс. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Думаю, было бы неплохо это сделать. . ."


    #Second time+ initial dialog
    elif Approval:
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Love", 70, -3, 1)
                $ Ch_Focus.Statup("Love", 20, -2, 1)
                if Ch_Focus is RogueX:
                        ch_r "Ты снова хочешь понаблюдать за мной?"
                elif Ch_Focus is KittyX:
                        ch_k "Снова? Только смотреть?"
                elif Ch_Focus is EmmaX:
                        ch_e "Снова? Ты хочешь просто смотреть?"
                elif Ch_Focus is LauraX:
                        ch_l "Хммм, опять?"
                elif Ch_Focus is JeanX:
                        ch_j "Хммм, опять?"
                elif Ch_Focus is StormX:
                        ch_s "Тебе нравится только смотреть?"
                elif Ch_Focus is JubesX:
                        ch_v "Хммм, снова?"
                elif Ch_Focus is GwenX:
                        ch_g "Хммм, снова?"
                elif Ch_Focus is BetsyX:
                        ch_b "Хмм, снова?"
                elif Ch_Focus is DoreenX:
                        ch_d "Хмм, хочешь снова понаблюдать за мной?"
                elif Ch_Focus is WandaX:
                        ch_w "Хочешь посмотреть еще раз?"
            elif Approval and "masturbation" in Ch_Focus.RecentActions:
                $ Ch_Focus.FaceChange("sexy", 1)
                if Ch_Focus is RogueX:
                        ch_r "Наверное, можно еще разочек. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Думаю, можно попробовать еще раз. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "У меня еще остались. . . дела, которые я хотела бы закончить. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Думаю, от еще одного раза ничего плохого не случится. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Мммм . . ."
                elif Ch_Focus is StormX:
                        ch_s "Пожалуй, я не. . . закончила. . ."
                elif Ch_Focus is JubesX:
                        ch_v "У меня накопилось много стресса. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Я создала еще большее напряжение. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Я оставила дело незавершенным. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я еще не совсем закончила. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Мне бы не помешало еще немного расслабиться. . ."
                jump Girl_M_Prep
            elif Approval and "masturbation" in Ch_Focus.DailyActions:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Тебе это так нравится?",
                    "Тебе все мало?",
                    "Должно быть, тебе очень нравится наблюдать за мной.",
                    "Приятно иметь зрителей. . .",
                    "Мне нравится при зрителях. . ."])
                call AnyLine(Ch_Focus,Line)
            elif Ch_Focus.Mast < 3:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Brows = "confused"
                if Ch_Focus is RogueX:
                        ch_r "Тебе нравится смотреть, да?"
                elif Ch_Focus is KittyX:
                        ch_k "Тебе. . . понравилось в прошлый раз?"
                elif Ch_Focus is EmmaX:
                        ch_e "Тебе нравится наблюдать?"
                elif Ch_Focus is LauraX:
                        ch_l "Тебе. . . понравилось в прошлый раз?"
                elif Ch_Focus is JeanX:
                        ch_j "Значит, тебе понравилось, хм."
                elif Ch_Focus is StormX:
                        ch_s "Тебе нравится наблюдать?"
                elif Ch_Focus is JubesX:
                        ch_v "В прошлый раз было весело?"
                elif Ch_Focus is GwenX:
                        ch_g "Неплохое представление. . . правда?"
                elif Ch_Focus is BetsyX:
                        ch_b "Я устраиваю неплохие представления, верно?"
                elif Ch_Focus is DoreenX:
                        ch_d "Это было. . . сексуально?"
                elif Ch_Focus is WandaX:
                        ch_w "Рада, что тебе нравится смотреть."
            else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.ArmPose = 2
                $ Line = renpy.random.choice(["Тебе нравится смотреть, да?",
                    "Снова?",
                    "Должно быть, тебе очень нравится наблюдать за мной.",
                    "Ты хочешь снова увидеть, как я ублажаю себя?",
                    "Ты хочешь, чтобы я снова помастурбировала?",
                    "Тебе в самом деле нравится наблюдать за мной.",
                    "Ты хочешь, чтобы я сама о себе позаботилась?",
                    "Так ты хочешь, чтобы я кончила снова?"])
                call AnyLine(Ch_Focus,Line)
                $ Line = 0
    #End second time+ initial dialog

    #If she's into it. . .
    if Approval >= 2:
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                $ Ch_Focus.Statup("Obed", 90, 1)
                $ Ch_Focus.Statup("Inbt", 60, 1)
                if Ch_Focus is RogueX:
                        ch_r "Дай мне только устроиться поудобнее. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Ладно. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Хорошо. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Как скажешь. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Ох. . . ладно. . ."
                elif Ch_Focus is StormX:
                        ch_s ". . .Хорошо"
                elif Ch_Focus is JubesX:
                        ch_v "Как скажешь. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Как скажешь. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Если тебе так этого хочется. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Наверное, можно. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Пожалуй, можно. . ."
            else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Statup("Love", 90, 1)
                $ Ch_Focus.Statup("Inbt", 50, 3)
                if Ch_Focus in (EmmaX,StormX,BetsyX):
                    $ Line = renpy.random.choice(["Ах. Конечно.",
                        "Это не повредит. . .",
                        "Хорошо.",
                        "[[хихикает]. . . ладно.",
                        "Замечательно.",
                        "Хех, конечно."])
                else:
                    $ Line = renpy.random.choice(["Ну. . . ладно.",
                        "Это не повредит. . .",
                        "Ага, ладно.",
                        "Пожалуй, это может быть интересно. . .",
                        "Твое общество мне не помешает. . .",
                        "Конечно, почему бы и нет?",
                        "Конечно!",
                        "Как скажешь. . . сейчас все будет.",
                        "Здорово.",
                        "Хех, конечно."])
                call AnyLine(Ch_Focus,Line)
                $ Line = 0
            $ Ch_Focus.Statup("Obed", 20, 1)
            $ Ch_Focus.Statup("Obed", 60, 1)
            $ Ch_Focus.Statup("Inbt", 70, 2)
            jump Girl_M_Prep

    #If she's not into it, but maybe. . .
    else:
        if Ch_Focus is RogueX:
                ch_r "Это. . .  немного интимное дело, [RogueX.Petname]."
        elif Ch_Focus is KittyX:
                ch_k "Знаешь. . . Это. . . довольно интимное дело."
        elif Ch_Focus is EmmaX:
                ch_e "Я не уверена, хочу ли я заниматься этим при тебе."
        elif Ch_Focus is LauraX:
                ch_l "Я не знаю, хочу ли я сейчас этого."
        elif Ch_Focus is JeanX:
                ch_j "Я не уверена, думаю, сейчас не самое подходящее время. . ."
        elif Ch_Focus is StormX:
                ch_s "Я в этом не уверена."
        elif Ch_Focus is JubesX:
                ch_v "Не знаю, я сейчас не в настроении."
        elif Ch_Focus is GwenX:
                ch_g "Мне не нравится атмосфера."
        elif Ch_Focus is BetsyX:
                ch_b "Я сейчас не совсем в настроении."
        elif Ch_Focus is DoreenX:
                ch_d "Я сейчас совсем не в настроении."
        elif Ch_Focus is WandaX:
                ch_w "Мне сейчас не до этого."
        menu:
            extend ""
            "Может, в другой раз?":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    if Ch_Focus.Lust > 70:
                        if Ch_Focus is RogueX:
                                ch_r "Ну, потом-то конечно. . . но мне нужно будет хорошенько подумать насчет тебя."
                        elif Ch_Focus is KittyX:
                                ch_k "Ну, я то знаю, чем буду потом заниматься. Вот только не уверена, сможешь ли ты прийти."
                                ch_k "То есть, ну, знаешь. . ."
                                ch_k "Не уверена, что тебе стоит в этот момент. . ."
                                ch_k ". . .быть рядом."
                        elif Ch_Focus is EmmaX:
                                if not Player.Male:
                                    ch_e "У меня есть кое-какие планы на. . . потом, и, возможно, ты могла бы в них поучавствовать."
                                else:
                                    ch_e "У меня есть кое-какие планы на. . . потом, и, возможно, ты мог бы в них поучавствовать."
                        elif Ch_Focus is LauraX:
                                ch_l "Я, скорее всего, займусь этим, но без зрителей."
                        elif Ch_Focus is JeanX:
                                ch_j "Что ж. . . я займусь этим, но после того, как ты уйдешь."
                        elif Ch_Focus is StormX:
                                ch_s "Я расчитываю, что к тому времени я уже закончу. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Может быть, только не при таком количестве лишних глаз. . ."
                        elif Ch_Focus is GwenX:
                                ch_g "Ох, может быть. . . когда я буду -совсем- одна."
                        elif Ch_Focus is BetsyX:
                                ch_b "Ох, может быть. . . когда я буду -совсем- одна."
                        elif Ch_Focus is DoreenX:
                                ch_d "Ох, эм, может быть. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "О, возможно. . ."
                    else:
                        $ Ch_Focus.FaceChange("surprised", 2)
                        if Ch_Focus is RogueX:
                                ch_r "Хмм, может быть. . . Я дам тебе знать."
                        elif Ch_Focus is KittyX:
                                ch_k "Хмм, может. . . Я тебе напишу, ладно?"
                        elif Ch_Focus is EmmaX:
                                ch_e "Не могу сказать."
                        elif Ch_Focus is LauraX:
                                ch_l "Хмм, может быть. . ."
                        elif Ch_Focus is JeanX:
                                ch_j "Ну. . . может быть. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Посмотрим."
                        elif Ch_Focus is JubesX:
                                ch_v "Хммм, возмооожно. . ."
                        elif Ch_Focus is GwenX:
                                ch_g "Хмм, может быть. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Хмм, может быть. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "Хмм. . . нет, скорее всего, нет. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Хмм. . . скорее нет, чем да. . ."
                        $ Ch_Focus.FaceChange("smile", 1)
                    $ Ch_Focus.Statup("Love", 80, 2)
                    $ Ch_Focus.Statup("Inbt", 70, 2)
                    return
            "Похоже, тебе это не помешает. . .":
                    if Approval:
                        $ Ch_Focus.FaceChange("sexy")
                        $ Ch_Focus.Statup("Obed", 90, 2)
                        $ Ch_Focus.Statup("Obed", 50, 2)
                        $ Ch_Focus.Statup("Inbt", 70, 3)
                        $ Ch_Focus.Statup("Inbt", 40, 2)
                        if Ch_Focus in (EmmaX,StormX,BetsyX):
                            $ Line = renpy.random.choice(["Ах, конечно.",
                                "Это не повредит. . .",
                                "Хорошо. . .",
                                "[[хихикает]. . . ладно.",
                                "Замечательно.",
                                "Хех, конечно."])
                        else:
                            $ Line = renpy.random.choice(["Ну. . . ладно.",
                                "Это не повредит. . .",
                                "Ага, ладно.",
                                "Пожалуй, это может быть интересно. . .",
                                "Твое общество мне не помешает. . .",
                                "Конечно, почему бы и нет?",
                                "Конечно!",
                                "Как скажешь. . . сейчас все будет.",
                                "Здорово.",
                                "Хех, конечно."])
                        call AnyLine(Ch_Focus,Line)
                        $ Line = 0
                        jump Girl_M_Prep

            "Просто приступай.":                                               # Pressured into it
                    $ Approval = ApprovalCheck(Ch_Focus, 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and Ch_Focus.Forced):
                        $ Ch_Focus.FaceChange("sad")
                        $ Ch_Focus.Statup("Love", 70, -5, 1)
                        $ Ch_Focus.Statup("Love", 200, -5)
                        if Ch_Focus is RogueX:
                                ch_r "Ладно-ладно. Я попробую."
                        elif Ch_Focus is KittyX:
                                ch_k "Боже, лаааадно."
                        elif Ch_Focus is EmmaX:
                                ch_e "Ох, если это поможет заткнуть тебя."
                        elif Ch_Focus is LauraX:
                                ch_l "Как скажешь."
                        elif Ch_Focus is JeanX:
                                ch_j "Ох. . . ладно. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Хорошо, если ты настаиваешь."
                        elif Ch_Focus is JubesX:
                                ch_v "А, пофиг."
                        elif Ch_Focus is GwenX:
                                ch_g "Ладно-ладно. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Ладно, если это так необходимо. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "Ох. . . ладно. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Это было грубо, но. . ."
                        $ Ch_Focus.Statup("Obed", 80, 4)
                        $ Ch_Focus.Statup("Inbt", 80, 1)
                        $ Ch_Focus.Statup("Inbt", 60, 3)
                        $ Ch_Focus.Forced = 1
                        jump Girl_M_Prep
                    else:
                        $ Ch_Focus.Statup("Love", 200, -20)
                        $ Ch_Focus.RecentActions.append("angry")
                        $ Ch_Focus.DailyActions.append("angry")
    # end of asking her to do it

    #She refused all offers.
    $ Ch_Focus.ArmPose = 1
    if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("sad", 2)
            if Ch_Focus is RogueX:
                    ch_r "Я не хочу делать что-то настолько. . . интимное, когда ты смотришь."
            elif Ch_Focus is KittyX:
                    ch_k "Я. . . не могу, пока ты смотришь."
            elif Ch_Focus is EmmaX:
                    ch_e "Я не буду этого делать."
            elif Ch_Focus is LauraX:
                    ch_l "Это слишком странно для меня."
            elif Ch_Focus is JeanX:
                    ch_j "Не-а, это слишком странно."
            elif Ch_Focus is StormX:
                    ch_s "Я этого не сделаю."
            elif Ch_Focus is JubesX:
                    ch_v "Это не то, чем я увлекаюсь."
            elif Ch_Focus is GwenX:
                    ch_g "Мне от этого совсем не по себе."
            elif Ch_Focus is BetsyX:
                    ch_b "Мне неловко выставлять себя напоказ."
            elif Ch_Focus is DoreenX:
                    ch_d "Мне. . . мне слишком неловко. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Мне не кажется это веселым. . ."
            $ Ch_Focus.Statup("Lust", 90, 5)
            if Ch_Focus.Love > 300:
                $ Ch_Focus.Statup("Love", 70, -2)
            $ Ch_Focus.Statup("Obed", 50, -2)
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
            $ Ch_Focus.RecentActions.append("no masturbation")
            $ Ch_Focus.DailyActions.append("no masturbation")
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            $ Ch_Focus.FaceChange("angry", 1)
            $ Ch_Focus.DailyActions.append("tabno")
            call Sex_Basic_Dialog(Ch_Focus,"tabno")
            $ Ch_Focus.Statup("Lust", 90, 5)
            $ Ch_Focus.Statup("Obed", 50, -3)
            return
    elif Ch_Focus.Mast:
            $ Ch_Focus.FaceChange("sad")
            if Ch_Focus is RogueX:
                    ch_r "Нет, больше нет, тебе придется вернуться к порно в интернете."
            elif Ch_Focus is KittyX:
                    ch_k "Извини, может, попробуешь сыграть в порно игру или что-нибудь типа того?"
            elif Ch_Focus is EmmaX:
                    ch_e "Уверена, ты можешь понаблюдать за кем-нибудь еще."
            elif Ch_Focus is LauraX:
                    ch_l "Мне сейчас не до этого."
            elif Ch_Focus is JeanX:
                    ch_j "Эм, мне и без этого сейчас хорошо. . ."
            elif Ch_Focus is StormX:
                    ch_s "Пожалуй, ты сможешь найти себе развлечение где-нибудь в другом месте."
            elif Ch_Focus is JubesX:
                    ch_v "Мне сейчас не до этого."
            elif Ch_Focus is GwenX:
                    ch_g "Мне не нравится атмосфера."
            elif Ch_Focus is BetsyX:
                    ch_b "В данный момент меня это не интересует."
            elif Ch_Focus is DoreenX:
                    ch_d "Это довольно интимное занятие, так что. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Я недостаточно хорошо тебя знаю. . ."
    else:
            $ Ch_Focus.FaceChange("normal", 1)
            if Ch_Focus is RogueX:
                    ch_r "Хех. Нет, я не буду этого делать."
            elif Ch_Focus is KittyX:
                    ch_k "Эм, нет."
            elif Ch_Focus is EmmaX:
                    ch_e "Я так не думаю, [EmmaX.Petname]."
            elif Ch_Focus is LauraX:
                    ch_l "Эм, нет."
            elif Ch_Focus is JeanX:
                    ch_j "Эм, нет."
            elif Ch_Focus is StormX:
                    ch_s "Я так не думаю, [StormX.Petname]."
            elif Ch_Focus is JubesX:
                    ch_v "Эм. . . нет."
            elif Ch_Focus is GwenX:
                    ch_g "Эм. . . нет."
            elif Ch_Focus is BetsyX:
                    ch_b "Пожалуй, я. . . откажусь."
            elif Ch_Focus is DoreenX:
                    ch_d "Я не могу сделать что-то подобное. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Мне не нравится эта идея. . ."
    $ Ch_Focus.RecentActions.append("no masturbation")
    $ Ch_Focus.DailyActions.append("no masturbation")
    $ Tempmod = 0
    return

label Girl_M_Prep:  #rkeljsvgb
    $ Ch_Focus.Upskirt = 1
    $ Ch_Focus.PantiesDown = 1
    call Girl_First_Bottomless(Ch_Focus,1)
    if Ch_Focus.Loc == bg_current:
            call QuickDisplay(Ch_Focus) #call Set_The_Scene(Dress=0)

    #if she hasn't seen you yet. . .
    if Ch_Focus.Loc == "bg desk":
            "Вы видите, как [Ch_Focus.Name], прислонившись спиной к своему столу, медленно водит своими руками по телу."
    elif "unseen" in Ch_Focus.RecentActions:
            $ Ch_Focus.FaceChange("sexy")
            $ Ch_Focus.Eyes = "closed"
            $ Ch_Focus.ArmPose = 2
            "Вы видите, как [Ch_Focus.Name], откинувшись назад, мастурбирует. Похоже, она вас еще не заметила."
    else:
            $ Ch_Focus.FaceChange("sexy")
            $ Ch_Focus.ArmPose = 2
            "[Ch_Focus.Name] откидывается назад и начинает играться с собой."
            if not Ch_Focus.Mast:#First time
                    if Ch_Focus.Forced:
                        $ Ch_Focus.Statup("Love", 90, -20)
                        $ Ch_Focus.Statup("Obed", 70, 45)
                        $ Ch_Focus.Statup("Inbt", 80, 35)
                    else:
                        $ Ch_Focus.Statup("Love", 90, 15)
                        $ Ch_Focus.Statup("Obed", 70, 35)
                        $ Ch_Focus.Statup("Inbt", 80, 40)


    $ Trigger = "masturbation"
#    if not Trigger3:
#        $ Trigger3 = "fondle pussy"
    if not Ch_Focus.Offhand:
        $ Ch_Focus.Offhand = "fondle pussy"

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    if Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no masturbation")
    $ Ch_Focus.RecentActions.append("masturbation")
    $ Ch_Focus.DailyActions.append("masturbation")

label Girl_M_Cycle:
    if Situation == "join":
        $ renpy.pop_call()
        $ Situation = 0
    $ Trigger = "masturbation"

    while Round > 0:
        #call Girl_Pos_Reset(Ch_Focus)("masturbation")
        call ViewShift(Ch_Focus,Ch_Focus.Pose,0,"masturbation")
#        call Shift_Focus(Ch_Focus)
        $ Ch_Focus.LustFace()
        if "unseen" in Ch_Focus.RecentActions and Ch_Focus.Loc == bg_current:
                $ Ch_Focus.Eyes = "closed"

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать смотреть.":
                                pass

                        "[Ch_Focus.Name]. . .[[вмешаться]" if "unseen" not in Ch_Focus.RecentActions and "join" not in Player.RecentActions and Ch_Focus.Loc == bg_current:
                                # Modification mode
                                if is_playing_music(audio.masturbate):
                                    $ play_music(name=audio.masturbate, loop=True)
                                # -----------------

                                "[Ch_Focus.Name] с хитрой ухмылкой немного замедляет свои движения."
                                if Ch_Focus is RogueX:
                                        if not Player.Male:
                                            ch_r "Да, ты что-то хотела, [RogueX.Petname]?"
                                        else:
                                            ch_r "Да, ты что-то хотел, [RogueX.Petname]?"
                                elif Ch_Focus is KittyX:
                                        ch_k "Наслаждаешься видом?"
                                elif Ch_Focus is EmmaX:
                                        ch_e "Наслаждаешься представлением?"
                                elif Ch_Focus is LauraX:
                                        ch_l "Нравится?"
                                elif Ch_Focus is JeanX:
                                        ch_j "Наслаждаешься видом?"
                                elif Ch_Focus is StormX:
                                        ch_s "Наслаждаешься?"
                                elif Ch_Focus is JubesX:
                                        ch_v "О, веселишься?"
                                elif Ch_Focus is GwenX:
                                        ch_g "Наслаждаешься представлением?"
                                elif Ch_Focus is BetsyX:
                                        ch_b "Наслаждаешься представлением?"
                                elif Ch_Focus is DoreenX:
                                        ch_d "Наслаждаешься представлением?"
                                elif Ch_Focus is WandaX:
                                        ch_w "Веселишься?"
                                $ Situation = "join"
                                call Girl_Masturbate
                        "\"Кхм-кхм. . .\"" if "unseen" in Ch_Focus.RecentActions:
                                jump Girl_M_Interupted

                        "Начать дрочить." if Trigger2 != "jackin" and Player.Male:
                                call Jackin(Ch_Focus)
                        "Перестать дрочить." if Trigger2 == "jackin" and Player.Male:
                                $ Trigger2 = 0
                        "Начать мастурбировать." if Trigger2 != "jilling" and not Player.Male:
                                call Jilling(Ch_Focus)
                        "Перестать мастурбировать." if Trigger2 == "jilling" and not Player.Male:
                                $ Trigger2 = 0

                        "Шлепнуть ее по заднице" if Ch_Focus.Loc == bg_current:
                                if "unseen" in Ch_Focus.RecentActions:
                                        "Вы смачно шлепаете [Ch_Focus.Name_vin] по заднице!"
                                        jump Girl_M_Interupted
                                else:
                                        call Slap_Ass(Ch_Focus)
                                        $ Cnt += 1
                                        $ Round -= 1
                                        jump Girl_M_Cycle
                        "Концентрироваться на продолжительности [[Не открыто] (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Концентрироваться на продолжительности" if not Player.FocusX and "focus" in Player.Traits:
                                    "Вы собираете волю в кулак, чтобы не кончить слишком быстро."
                                    $ Player.FocusX = 1
                        "Прекратить концентрироваться." if Player.FocusX:
                                    "Вы расслабляетесь. . ."
                                    $ Player.FocusX = 0

                        "Сменить вид" if "unseen" not in Ch_Focus.RecentActions:
                                    call ViewShift(Ch_Focus,"menu")
                                    jump Girl_M_Cycle

                        "Другие варианты":
                                menu:
                                    "Дополнительное действие" if Ch_Focus.Loc == bg_current:
                                            if Ch_Focus.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                    $ Ch_Focus.Action -= 1
                                            else:
                                                    call Sex_Basic_Dialog(Ch_Focus,"tired")

                                    "Тройничек (locked)" if not Partner or "unseen" in Ch_Focus.RecentActions or Ch_Focus.Loc != bg_current:
                                        pass
                                    "Тройничек" if Partner and "unseen" not in Ch_Focus.RecentActions and Ch_Focus.Loc == bg_current:
                                        menu:
                                            "Пусть [Partner.Name] займется чем-нибудь другим":
                                                        call Three_Change(Ch_Focus)
                                            "Переключиться на [Partner.Name_vin]":
                                                        call Trigger_Swap(Ch_Focus)
                                            "Раздеть [Partner.Name_vin]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump Girl_M_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_M_Cycle
                                            "Неважно":
                                                        jump Girl_M_Cycle

                                    "Показывать ее ноги" if not ShowFeet:# and Ch_Focus.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet:# and Ch_Focus.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Вставить анальную пробку" if not Ch_Focus.Plug and "plug" in Ch_Focus.Inventory and "unseen" not in Ch_Focus.RecentActions:
                                            call Insert_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку" if Ch_Focus.Plug and "unseen" not in Ch_Focus.RecentActions:
                                            call Remove_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку (locked)" if "plug" not in Ch_Focus.Inventory or "unseen" in Ch_Focus.RecentActions:
                                            pass

                                    "Псионический Нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            if "unseen" in Ch_Focus.RecentActions:
                                                    ch_p "О, да, сними это. . ."
                                                    jump Girl_M_Interupted
                                            else:
                                                    call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            if "unseen" in Ch_Focus.RecentActions:
                                                    ch_p "На тебе что-то есть. . ."
                                                    jump Girl_M_Interupted
                                            else:
                                                    call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                                    jump Girl_M_Cycle

                        "Вернуться к Секс-меню" if MultiAction and Ch_Focus.Loc == bg_current:
                                    ch_p "Думаю, нам стоит попробовать что-нибудь другое."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_M_Interupted
                        "Закончить" if not MultiAction or Ch_Focus.Loc != bg_current:
                                    ch_p "Думаю, нам стоит пока остановиться."
                                    call Girl_Pos_Reset(Ch_Focus)
                                    $ Line = 0
                                    jump Girl_M_Interupted
        #End menu (if Line)

        call Shift_Focus(Ch_Focus)
        call Sex_Dialog(Ch_Focus,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or Ch_Focus.Lust >= 100:
                    #If you can cum:
                    if Player.Focus >= 100:
                        if "unseen" not in Ch_Focus.RecentActions:
                            #if she knows you're there
                            call Player_Cumming(Ch_Focus)
                            if "angry" in Ch_Focus.RecentActions:
                                call Girl_Pos_Reset(Ch_Focus)
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                $ Ch_Focus.RecentActions.append("unsatisfied")
                                $ Ch_Focus.DailyActions.append("unsatisfied")
                            $ Line = "came"
                        else: #If she wasn't aware you were there
                            "Вы изо всех сил стараетесь не кончить."
                            $ Player.Focus = 95
                            if Ch_Focus.Loc == bg_current or Ch_Focus.Loc == "bg desk" or Ch_Focus.Loc == "nearby":
                                    jump Girl_M_Interupted

                    #If Girl can cum
                    if Ch_Focus.Lust >= 100:
                        call Girl_Cumming(Ch_Focus)
                        if Ch_Focus.Loc == bg_current or Ch_Focus.Loc == "bg desk" or Ch_Focus.Loc == "nearby":
                                jump Girl_M_Interupted

                    if Line == "came":
                        $ Line = 0
                        if not Player.Semen:
                            "Вы истощены, вам, наверное, пора взять перерыв."
                            $ Trigger2 = 0 if Trigger2 not in ("jackin","jilling") else Trigger2


                        if "unsatisfied" in Ch_Focus.RecentActions:#And Ch_Focus is unsatisfied,
                            "[Ch_Focus.Name] все еще выглядит слегка неудовлетворенной."
                            menu:
                                "Хотите завершить начатое?"
                                "Продолжим еще немного.":
                                    $ Line = "Вы позволяете ей вернуться к процессу"
                                    jump Girl_M_Cycle
                                "С меня хватит.":
                                    "Вы просите ее остановиться."
                                    return
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        if "unseen" in Ch_Focus.RecentActions:
                if Round == 10:
                    "Уже довольно поздно, [Ch_Focus.Name] вероятно, скоро захочет остановиться."
                elif Round == 5:
                    "Она вот-вот остановится."
        else:
                if Ch_Focus.Loc == bg_current:
                        call Escalation(Ch_Focus) #sees if she wants to escalate things

                if Round == 10:
                    if Ch_Focus is RogueX:
                            ch_r "Наверное, нам стоит закругляться, уже поздно."
                    elif Ch_Focus is KittyX:
                            ch_k "Наверное, нам стоит закругляться, уже поздно."
                    elif Ch_Focus is EmmaX:
                            ch_e "Думаю, скоро я сделаю перерыв."
                    elif Ch_Focus is LauraX:
                            ch_l "Наверное, нам стоит закругляться, уже поздно."
                    elif Ch_Focus is JeanX:
                            ch_j "Ого, посмотри-ка на время. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Вероятно, скоро я возьму перерыв."
                    elif Ch_Focus is JubesX:
                            call Sex_Basic_Dialog(JubesX,10)
                    elif Ch_Focus is GwenX:
                            ch_g "Ты уже скоро? . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Ты скоро? . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ты. . . скоро? . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Слушай, ты. . . уже. . . скоро? . ."
                    $ Ch_Focus.Lust += 10
                elif Round == 5:
                    if Ch_Focus is RogueX:
                            ch_r "Серьезно, нам скоро придется закончить."
                    elif Ch_Focus is KittyX:
                            ch_k "Нам скоро придется закончить, правда."
                    elif Ch_Focus is EmmaX:
                            ch_e "Угмм, я почти закончила. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Давай еще 5 минут, не больше."
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно, может сделаем перерыв?"
                    elif Ch_Focus is StormX:
                            ch_s "Ах! Я почти закончила. . ."
                    elif Ch_Focus is JubesX:
                            call Sex_Basic_Dialog(JubesX,5)   #". . . I could really use a break here. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Меня. . . эм, хватит только на пару минут. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "У меня осталось совсем немного времени. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Мне скоро нужен будет перерыв. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Мне скоро нужен будет перерыв. . ."
                    $ Ch_Focus.Lust += 25

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    if "unseen" not in Ch_Focus.RecentActions:
            if Ch_Focus is RogueX:
                    ch_r "Ладно, [RogueX.Petname], пока хватит."
            elif Ch_Focus is KittyX:
                    ch_k "Серьезно, нам скоро придется закончить."
            elif Ch_Focus is EmmaX:
                    ch_e "Этого, пожалуй, хватит."
            elif Ch_Focus is LauraX:
                    ch_l "Ладно, пока что хватит, мне надо передохнуть."
            elif Ch_Focus is JeanX:
                    ch_j "Ладно, вот и все, время сделать перерыв."
            elif Ch_Focus is StormX:
                    ch_s "Этого достаточно."
            elif Ch_Focus is JubesX:
                    call Sex_Basic_Dialog(JubesX,"done") # ch_s "Ok, that's it, I need a break."
            elif Ch_Focus is GwenX:
                    ch_g "Ладно, я. . . эм. . закончила. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Я. . . вот-вот. . . закончу. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Я. . . все. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Я. . . все. . ."

label Girl_M_Interupted:
    # If she hasn't noticed you're there before cumming
    if "unseen" in Ch_Focus.RecentActions:
                $ Ch_Focus.FaceChange("surprised", 2)
                $ Trigger = 0
                $ Ch_Focus.Offhand = 0
                "[Ch_Focus.Name] вдруг останавливается и широко открывает глаза."
                if Ch_Focus.Loc == "bg desk":
                        $ Ch_Focus.Loc = bg_current
                        call QuickDisplay(Ch_Focus) #call Set_The_Scene(Dress=0)
                        "Она подходит к вам."
                call Girl_First_Bottomless(Ch_Focus,1)
                $ Ch_Focus.FaceChange("surprised", 2)

                if Ch_Focus is RogueX:
                        ch_r "К- как долго ты здесь стоишь, [RogueX.Petname]?"
                elif Ch_Focus is KittyX:
                        ch_k "Ой!"
                        ch_k "Ты давно здесь?!"
                elif Ch_Focus is EmmaX:
                        ch_e "!"
                        ch_e "Как долго ты здесь?!"
                elif Ch_Focus is LauraX:
                        ch_l "Хм."
                        ch_l "Ты давно здесь?"
                elif Ch_Focus is JeanX:
                        ch_j "О, привет. . .[JeanX.Petname]."
                        ch_j "Ты давно здесь?"
                elif Ch_Focus is StormX:
                        ch_s "!"
                        ch_s "Как долго ты здесь?!"
                elif Ch_Focus is JubesX:
                        ch_v "Ох!"
                        ch_v "Как долго ты там стоишь?"
                elif Ch_Focus is GwenX:
                        ch_g "Подожди. . ."
                        if not Player.Male:
                            ch_g "Ты когда сюда пришла?"
                        else:
                            ch_g "Ты когда сюда пришел?"
                elif Ch_Focus is BetsyX:
                        ch_b "Ох!"
                        ch_b "Как долго ты здесь находишься?"
                elif Ch_Focus is DoreenX:
                        ch_d "Ой!"
                        ch_d "Как долго ты здесь?"
                elif Ch_Focus is WandaX:
                        ch_w "Воу!"
                        ch_w "Как давно ты здесь?"
                if Trigger2 == "jackin" or Trigger2 == "jilling":
                        #If you've been jacking it
                        $ Ch_Focus.Eyes = "down"
                        if Ch_Focus is EmmaX:
                                if not Player.Male:
                                    ch_e "И, как я понимаю, время ты зря не теряла. . . "
                                else:
                                    ch_e "И, как я понимаю, время ты зря не терял. . . "
                        elif Ch_Focus is JeanX:
                                ch_j "Вижу, ты здесь как дома. . . "
                        elif Ch_Focus is StormX:
                                if not Player.Male:
                                    ch_s ". . . Вижу, ты решила позаботиться о себе. . . "
                                else:
                                    ch_s ". . . Вижу, ты решил позаботиться о себе. . . "
                        elif Ch_Focus is BetsyX:
                                ch_b "У тебя, эм. . . кажется, все под контролем. . . "
                        elif Ch_Focus is WandaX:
                                if not Player.Male:
                                    ch_w "Похоже, ты не теряла времени даром. . . "
                                else:
                                    ch_w "Похоже, ты не терял времени даром. . . "
                        elif Trigger2 == "jackin":
                            if Ch_Focus is RogueX:
                                ch_r "И почему у тебя член торчит?!"
                            elif Ch_Focus is KittyX:
                                ch_k "И, эм. . . у тебя член торчит. . . "
                            elif Ch_Focus is LauraX:
                                ch_l "И эм. . . у тебя член торчит. . . "
                            elif Ch_Focus is JubesX:
                                ch_v "И, эм. . . ты достал свой пенис. . . "
                            elif Ch_Focus is GwenX:
                                ch_g "Ты, эм. . . кажется, не забыл позаботиться о себе. . . "
                            elif Ch_Focus is DoreenX:
                                ch_d "Ты, эм. . . похоже, завелся. . . "
                        elif Trigger2 == "jilling":
                            if Ch_Focus is RogueX:
                                ch_r "И почему у тебя рука между ног?!"
                            elif Ch_Focus is KittyX:
                                ch_k "И, эм. . . ты трогала себя. . ? "
                            elif Ch_Focus is LauraX:
                                ch_l "И эм. . . я вижу твою киску. . . "
                            elif Ch_Focus is JubesX:
                                ch_v "И, эм. . . у тебя рука. . . между ног. . ."
                            elif Ch_Focus is GwenX:
                                ch_g "Ты, эм. . . кажется, не забыла позаботиться о себе. . . "
                            elif Ch_Focus is DoreenX:
                                ch_d "Ты, эм. . . похоже, завелась. . . "
                        menu:
                            extend ""
                            "Достаточно долго, и, надо отметить, это было прекрасное представление.":
                                    $ Ch_Focus.FaceChange("sadside",2,Mouth="smirk")
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 70, 2)
                                    if Ch_Focus is RogueX:
                                            if not Player.Name:
                                                ch_r "Ну, наверное, ты права. . ."
                                            else:
                                                ch_r "Ну, наверное, ты прав. . ."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Эм, ну. . . ага. . ."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Очевидно, что это так. . ."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Серьезно? Странно. . ."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Верно. . ."
                                    elif Ch_Focus is StormX:
                                            ch_s "Верно. . ."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Ох. . . эм. . .спасибо?"
                                    elif Ch_Focus is GwenX:
                                            ch_g "Правда?{w=1.0}{nw}"
                                            ch_g "Правда? Подожди! Речь не об этом!"
                                    elif Ch_Focus is BetsyX:
                                            ch_b "В самом деле?"
                                    elif Ch_Focus is DoreenX:
                                            cch_d "Ох. . . эм. . . это. . . ладно. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Серьезно. . ?"
                                    if Ch_Focus.Love >= 800 or Ch_Focus.Obed >= 500 or Ch_Focus.Inbt >= 500:
                                        $ Tempmod += 10
                                        $ Ch_Focus.Statup("Lust", 90, 5)
                                        if Ch_Focus is RogueX:
                                                if not Player.Male:
                                                    ch_r "Да ты сама тоже ничего. . ."
                                                else:
                                                    ch_r "Да ты сам тоже ничего. . ."
                                        elif Ch_Focus is KittyX:
                                                ch_k "Мне, эмм. . . тоже нравится то, что я вижу. . ."
                                        elif Ch_Focus is LauraX:
                                                if not Player.Male:
                                                    ch_l "Я. . . эм. . . ты и сама не так уж плоха. . ."
                                                else:
                                                    ch_l "Я. . . эм. . . ты и сам не так уж плох. . ."
                                        elif Ch_Focus is JeanX:
                                                if not Player.Male:
                                                    ch_j "Да ты и сама устроила неплохое представление. . ."
                                                else:
                                                    ch_j "Да ты и сам устроил неплохое представление. . ."
                                        elif Ch_Focus is StormX:
                                                ch_s "и, пожалуй, я сама много чего пропустила. . ."
                                        elif Ch_Focus is JubesX:
                                                if not Player.Male:
                                                    ch_v "Я, эм. . . ты и сама не так уж плоха. . ."
                                                else:
                                                    ch_v "Я, эм. . . ты и сам не так уж плох. . ."
                                        elif Ch_Focus is GwenX:
                                                if not Player.Male:
                                                    ch_g "Я, эм. . . ты и сама не так уж плоха. . ."
                                                else:
                                                    ch_g "Я, эм. . . ты и саа не так уж плох. . ."
                                        elif Ch_Focus is BetsyX:
                                                if not Player.Male:
                                                    ch_b "Что ж. . . ты и сама устроила неплохое представление. . ."
                                                else:
                                                    ch_b "Что ж. . . ты и сам устроил неплохое представление. . ."
                                        elif Ch_Focus is DoreenX:
                                                ch_d "Похоже. . . я привлекла повышенное внимание. . ."
                                        elif Ch_Focus is WandaX:
                                                ch_w "-приятно слышать."
                                    if Ch_Focus is EmmaX:
                                                ch_e "и, полагаю, мне тоже есть на что посмотреть. . ."

                            "Я. . . здесь недавно?":
                                    $ Ch_Focus.FaceChange("bemused",2,Eyes="down")
                                    $ Ch_Focus.Statup("Love", 70, 2)
                                    $ Ch_Focus.Statup("Love", 90, 1)
                                    $ Ch_Focus.Statup("Obed", 50, 2)
                                    $ Ch_Focus.Statup("Obed", 70, 2)
                                    if Player.Male:
                                            "Она многозначительно смотрит на ваш член."
                                            if Ch_Focus is KittyX:
                                                    ch_k "Но достаточно долго, чтобы вытащить свою штуку?"
                                            elif Ch_Focus is EmmaX:
                                                    $ EmmaX.Eyes = "squint"
                                                    ch_e "Но достаточно долго, чтобы у тебя кое-что поднялось?"
                                            elif Ch_Focus is LauraX:
                                                    ch_l "Но достаточно долго, чтобы вытащить свою штуку?"
                                    else:
                                            if Ch_Focus is KittyX:
                                                    ch_k "Но достаточно долго, что успела намокнуть?"
                                            elif Ch_Focus is EmmaX:
                                                    $ EmmaX.Eyes = "squint"
                                                    ch_e "Но достаточно долго, чтобы испортить мой коврик?"
                                            elif Ch_Focus is LauraX:
                                                    ch_l "Но достаточно долго, чтобы намокнуть?"
                                    if Ch_Focus is RogueX:
                                            ch_r "Дааа, так я тебе и поверила . . ."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Так я тебе и поверила. . ."
                                    elif Ch_Focus is StormX:
                                            ch_s "Но все-таки достаточно долго. . ."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Судя по всему, ты мне лжешь."
                                    elif Ch_Focus is GwenX:
                                            if Player.Male:
                                                ch_g "Похоже, ты уже усердно поработал."
                                            else:
                                                ch_g "Похоже, ты уже усердно поработала."
                                    elif Ch_Focus is BetsyX:
                                            if not Player.Male:
                                                ch_b "Тогда ты точно времени зря не теряла."
                                            else:
                                                ch_b "Тогда ты точно времени зря не терял."
                                    elif Ch_Focus is DoreenX:
                                            if Player.Male:
                                                    ch_d "Ты пришел сюда с этим?"
                                            else:
                                                    ch_d "Ты пришла сюда с этим?"
                                    if Ch_Focus.Love >= 800 or Ch_Focus.Obed >= 500 or Ch_Focus.Inbt >= 500:
                                            $ Tempmod += 10
                                            $ Ch_Focus.Statup("Lust", 90, 5)
                                            $ Ch_Focus.FaceChange("bemused", 1)
                                            if Ch_Focus is RogueX:
                                                    ch_r "Тем не менее, я не могу винить тебя."
                                            elif Ch_Focus is KittyX:
                                                    ch_k "Ну, эм. . . наверное, я должна быть польщена?"
                                            elif Ch_Focus is EmmaX:
                                                    ch_e "Что ж, при таких обстоятельствах, полагаю, тебе было просто тяжело удержаться. . ."
                                            elif Ch_Focus is LauraX:
                                                    ch_l "Было в самом деле так интересно?"
                                            elif Ch_Focus is JeanX:
                                                    ch_j "Думаю, я не могу винить тебя. . ."
                                            elif Ch_Focus is StormX:
                                                    if not Player.Male:
                                                        ch_s "Я совсем не удивлена, что ты не смогла сдержать свой энтузиазм. . ."
                                                    else:
                                                        ch_s "Я совсем не удивлена, что ты не смог сдержать свой энтузиазм. . ."
                                            elif Ch_Focus is JubesX:
                                                    ch_v "Думаю, я произвела впечатление на тебя?"
                                            elif Ch_Focus is GwenX:
                                                    ch_g "Должно быть, я тебя вдохновила. . ."
                                            elif Ch_Focus is BetsyX:
                                                    ch_b "Пожалуй, мне следует отдать тебе должное. . ."
                                            elif Ch_Focus is DoreenX:
                                                    ch_d "Думаю, тебе. . . понравилось увиденное? . ."
                                            elif Ch_Focus is WandaX:
                                                    ch_w "Должно быть, тебе понравилось мое маленькое представление. . ."
                                    else:
                                            $ Tempmod -= 10
                                            $ Ch_Focus.Statup("Lust", 200, -5)
                        $ Ch_Focus.FaceChange("sexy",1)
                        call Seen_First_Peen(Ch_Focus,Partner)
                        call AnyLine(Ch_Focus,"Хмм. . .")

                #you haven't been jacking it
                else:
                        menu:
                            extend ""
                            "Я здесь довольно давно.":
                                    $ Ch_Focus.FaceChange("sadside",2,Mouth="smirk")
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 70, 2)
                                    if Ch_Focus is RogueX:
                                            ch_r "Ну, я надеюсь, тебе понравилось представление. . ."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Надеюсь, я достаточно развлекла тебя. . ."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "И как тебе представлением?"
                                    elif Ch_Focus is LauraX:
                                            ch_l "Похоже, я устроила небольшое представление для тебя. . ."
                                    elif Ch_Focus is JeanX:
                                            if not Player.Male:
                                                ch_j "Приятно, что ты дала мне об этом знать. . ."
                                            else:
                                                ch_j "Приятно, что ты дал мне об этом знать. . ."
                                    elif Ch_Focus is StormX:
                                            ch_s "И, полагаю, тебе понравилось представление?"
                                    elif Ch_Focus is JubesX:
                                            ch_v "Наверное, это было интересно. . ."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Должно быть, я тебя вдохновила. . ."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Пожалуй, мне следует отдать тебе должное. . ."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Похоже. . . я привлекла твое внимание. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Серьезно. . ?"
                                            ch_w "-приятно это знать."
                            "Я здесь не так давно.":
                                    $ Ch_Focus.FaceChange("bemused", 1)
                                    $ Ch_Focus.Statup("Love", 70, 2)
                                    $ Ch_Focus.Statup("Love", 90, 1)
                                    if Ch_Focus is RogueX:
                                            ch_r "Да, да. . ."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Ага, не сомневаюсь. . ."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Да, конечно. . ."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Угум. . ."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Угум. . ."
                                    elif Ch_Focus is StormX:
                                            ch_s "Похоже на правду. . ."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Ну да, ну да. . ."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Угум. . ."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Конечно. . ."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Агааа. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Ага, конечно."
                                            ch_w "Должно быть, тебе понравилось мое маленькое представление. . ."
                                    $ Ch_Focus.Statup("Obed", 50, 2)
                                    $ Ch_Focus.Statup("Obed", 70, 2)
                #end response menu
                $ Ch_Focus.DrainWord("unseen",1,0) #She sees you, so remove unseens
                $ Ch_Focus.Mast += 1
                if Round <= 10:
                    if Ch_Focus is RogueX:
                            ch_r "Но сейчас слишком поздно чем-либо заниматься."
                    elif Ch_Focus is KittyX:
                            ch_k "Сейчас уже поздно что-либо делать. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "К сожалению, уже довольно поздно."
                    elif Ch_Focus is LauraX:
                            ch_l "Мне все равно нужен был перерыв. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "В любом случае, мне бы не помешал перерыв. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Кажется, прошло немало времени, пока я была. . . занята."
                    elif Ch_Focus is JubesX:
                            ch_v "Ну, мне в любом случае нужен был перерыв. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Мне все равно нужен был перерыв. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "В любом случае, мне нужен был небольшой перерыв. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ну, в любом случае, мне нужен был перерыв. . ."
                    elif Ch_Focus is WandaX:
                            ch_d "Что ж, в любом случае, мне нужен был перерыв. . ."
                    return
                $ Situation = "join"
                call Girl_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen

    #else, if She's seen you already
    $ Ch_Focus.Action -= 1
    $ Ch_Focus.Mast += 1
    call Checkout
    if Situation == "shift":
        #$ Situation = 0
        return
    $ Situation = 0

    if Partner in (EmmaX,WandaX):
        call Partner_Like(Ch_Focus,3)
    else:
        call Partner_Like(Ch_Focus,2)

    if Ch_Focus.Loc != bg_current:
        return

    if Round <= 10:
            if Ch_Focus is RogueX:
                    ch_r "[RogueX.Petname], мне нужно немного передохнуть."
            elif Ch_Focus is KittyX:
                    ch_k "Дай мне минутку, мне нужно прийти в себя. . ."
            elif Ch_Focus is EmmaX:
                    ch_e "Позволь мне прийти в себя. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Дай мне минуту. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Дай мне минутку. . ."
            elif Ch_Focus is StormX:
                    ch_s "Дай мне время прийти в себя. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Мне все равно нужен перерыв. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Мне нужна минутка отдыха. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Мне нужно немного передохнуть. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Мне нужно отдохнуть. . ."
            elif Ch_Focus is WandaX:
                    ch_d "Мне нужно отдохнуть. . ."
            return
    $ Ch_Focus.FaceChange("sexy", 1)
    if Ch_Focus.Lust < 20:
        if Ch_Focus is RogueX:
                ch_r "Мне вполне этого достаточно, [RogueX.Petname]. А что насчет тебя?"
        elif Ch_Focus is KittyX:
                ch_k "Ну, я довольна, а ты?"
        elif Ch_Focus is EmmaX:
                ch_e "По крайней мере, я удовлетворила свои потребности."
        elif Ch_Focus is LauraX:
                ch_l "Наверное, я довольна, а ты?"
        elif Ch_Focus is JeanX:
                ch_j "Мне хватило, что насчет тебя?"
        elif Ch_Focus is StormX:
                ch_s "По крайней мере, мне понравилось."
        elif Ch_Focus is JubesX:
                ch_v "Нууу. . . Мне все очень понравилось. . ."
        elif Ch_Focus is GwenX:
                ch_g "Ммм. . . я довольна, а ты?"
        elif Ch_Focus is BetsyX:
                ch_b "Ммм. . . думаю, я довольна, а ты?"
        elif Ch_Focus is DoreenX:
                ch_d ". . . эм. . . Думаю, я получила то, что мне было необходимо, а как насчет тебя?"
        elif Ch_Focus is WandaX:
                ch_w "Я получила то, что мне было необходимо, а как насчет тебя?"
    else:
        if Ch_Focus is RogueX:
                ch_r "Ага, чего ты хочешь?"
        elif Ch_Focus is KittyX:
                ch_k "Эм, да?"
        elif Ch_Focus is EmmaX:
                ch_e "Да?"
        elif Ch_Focus is LauraX:
                ch_l "И что дальше?"
        elif Ch_Focus is JeanX:
                ch_j "Так, что дальше?"
        elif Ch_Focus is StormX:
                ch_s "Да?"
        elif Ch_Focus is JubesX:
                ch_v "Итак, чем ты хочешь заняться дальше?"
        elif Ch_Focus is GwenX:
                ch_g "Ну. . . что дальше?"
        elif Ch_Focus is BetsyX:
                ch_b "Что дальше?"
        elif Ch_Focus is DoreenX:
                ch_d "У тебя есть еще какие-то идеи?"
        elif Ch_Focus is WandaX:
                ch_w "У тебя есть еще какие-то идеи?"
    menu:
        extend ""
        "Ну, ты могла бы кое о чем позаботиться для меня" if Player.Semen and Ch_Focus.Action:
                $ Situation = "shift"
                return
        "Тебе следует продолжить. . ." if Player.Semen:
                $ Ch_Focus.FaceChange("sly")
                if Ch_Focus.Action and Round >= 10:
                    if Ch_Focus is RogueX:
                            ch_r "Ну, ладно. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Конечно. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Пожалуй, соглашусь. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Ладно. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Если ты так этого хочешь. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Ладно. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Как скажешь. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Это можно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Пожалуй, моэно. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Конечно. . ."
                    jump Girl_M_Cycle
                else:
                    if Ch_Focus is RogueX:
                            ch_r "Я немного устала, возможно, пора сделать перерыв. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Дай мне минутку, мне нужно прийти в себя. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Дай мне минутку, мне нужно прийти в себя. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Дай мне минутку. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Дай мне минутку. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Дай мне время прийти в себя. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Дай мне минутку. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Дай мне минутку на отдых. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Мне нужно передохнуть. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Мне нужно отдохнуть. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Мне нужно отдохнуть. . ."
                #end "You could just keep going. . ." if Player.Semen:
        "Все нормально [[Остановиться]":
                if Ch_Focus.Love < 800 and Ch_Focus.Inbt < 500 and Ch_Focus.Obed < 500:
                    $ Ch_Focus.OutfitChange()
                $ Ch_Focus.FaceChange("normal")
                $ Ch_Focus.Brows = "confused"
                if Ch_Focus is RogueX:
                        ch_r "Ну. . . ладно тогда. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Ну. . . ладно. . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Что ж . . . хорошо . ."
                elif Ch_Focus is LauraX:
                        ch_l "Ладно."
                elif Ch_Focus is JeanX:
                        ch_j "Ладно."
                elif Ch_Focus is StormX:
                        ch_s ". . . что ж, хорошо. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Ладно, клево. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Ладно.."
                elif Ch_Focus is BetsyX:
                        ch_b "Конечно."
                elif Ch_Focus is DoreenX:
                        ch_d "Ох, ладно. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Конечно. . ."
                $ Ch_Focus.Brows = "normal"
        "Тебе, наверное, стоит пока что остановиться." if Ch_Focus.Lust > 30:
                $ Ch_Focus.FaceChange("sad")
                if Ch_Focus is RogueX:
                        ch_r "Ну, если ты так говоришь."
                elif Ch_Focus is KittyX:
                        ch_k "Наверное? . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Я . . . да . ."
                elif Ch_Focus is StormX:
                        ch_s "Я . . . ладно . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Ох."
                elif Ch_Focus is WandaX:
                        ch_w "Конечно. . ."
                else:
                        call AnyLine(Ch_Focus,"Хммм.")
                #"I'm good here. [[Stop]":
    if Trigger2 == "jackin" or Trigger2 == "jilling":
        $ Trigger2 = 0
    return

## end Ch_Focus.Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# Start Girl Sex pose //////////////////////////////////////////////////////////////////////////////////
# Ch_Focus.Sex_P //////////////////////////////////////////////////////////////////////

label Girl_Sex_P:   #rkeljsvg
##    #fix remove
#    if Ch_Focus is WandaX:
#        "Not currently available."
#        return
##    #fix remove
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Ch_Focus)
    if Ch_Focus.Sex >= 7: # She loves it
        $ Tempmod += 15
    elif Ch_Focus.Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif Ch_Focus.Sex: #You've done it before
        $ Tempmod += 10
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 15

    if not Player.Male:
        $ Tempmod += 5
    elif Ch_Focus.Addict >= 75 and (Ch_Focus.CreamP + Ch_Focus.CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif Ch_Focus.Addict >= 75:
        $ Tempmod += 15

    if Ch_Focus.Lust > 85:
        $ Tempmod += 10
    elif Ch_Focus.Lust > 75: #She's really horny
        $ Tempmod += 5

    if Situation == "shift":
        $ Tempmod += 10
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

    if "no sex" in Ch_Focus.DailyActions:
        $ Tempmod -= 15 if "no sex" in Ch_Focus.RecentActions else 5


    $ Approval = ApprovalCheck(Ch_Focus, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if Situation == "auto":
                if not Player.Male and "strapon" not in Player.RecentActions:
                        "Вы достаете свой резиновый член."
                        $ Player.AddWord(1,"strapon",0,0,0) #Recent
                if renpy.showing(Ch_Focus.Tag+"_SexSprite") or renpy.showing(Ch_Focus.Tag+"_Doggy_Animation"):
                        pass
                else:
                        call expression Ch_Focus.Tag + "_Sex_Launch" pass ("sex") #call expression Ch_Focus.Tag + "_Sex_Launch" pass ("sex")
                        if Ch_Focus.PantsNum() == 5:
                            "Вы прижимаетесь к [Ch_Focus.Name_dat], в процессе задирая ее юбку."
                        elif Ch_Focus.PantsNum() >= 6:
                            "Вы прижимаетесь к [Ch_Focus.Name_dat], в процессе стягивая ее штаны."
                        else:
                            "Вы прижимаетесь к [Ch_Focus.Name_dat]."
                        $ Ch_Focus.SeenPanties = 1
                $ Ch_Focus.Upskirt = 1
                $ Ch_Focus.PantiesDown = 1
                if not Player.Male:
                    "Вы начинаете водить кончиком своего резинового члена о ее влажную щелку."
                else:
                    "Вы начинаете водить кончиком своего члена о ее влажную щелку."
                $ Ch_Focus.FaceChange("surprised", 1)

                if "sex" in Ch_Focus.RecentActions:
                        jump Girl_SexPrep

                if (Ch_Focus.Sex and Approval):# or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it
                    "[Ch_Focus.Name] опускает взгляд, а затем расплывается в улыбке."
                    $ Ch_Focus.FaceChange("sly")
                    $ Ch_Focus.Statup("Obed", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 3)
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    if Ch_Focus is RogueX:
                            ch_r "Ладно, [RogueX.Petname], давай сделаем это."
                    elif Ch_Focus is KittyX:
                            ch_k "Ох. . . продолжай, [KittyX.Petname]."
                    elif Ch_Focus is EmmaX:
                            ch_e "Ммм, если ты настаиваешь, [EmmaX.Petname]."
                    elif Ch_Focus is LauraX:
                            ch_l "Меня все устраивает, [LauraX.Petname]."
                    elif Ch_Focus is JeanX:
                            ch_j "Оох, если тебе это так нужно, [JeanX.Petname]."
                    elif Ch_Focus is StormX:
                            ch_s "Ммм, если ты настаиваешь, [StormX.Petname]."
                    elif Ch_Focus is JubesX:
                            ch_v "Меня это устраивает, [JubesX.Petname]."
                    elif Ch_Focus is GwenX:
                            ch_g "Ооох. . . ладно, [GwenX.Petname]."
                    elif Ch_Focus is BetsyX:
                            ch_b "OОоох. . . конечно, [BetsyX.Petname]."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ооо. . . ладно, [Ch_Focus.Petname]."
                    elif Ch_Focus is WandaX:
                            ch_w "Ну ладно, [WandaX.Petname]."
                    jump Girl_SexPrep
                else:
                    #she's questioning it
                    $ Ch_Focus.Brows = "angry"
                    if Ch_Focus is RogueX:
                            ch_r "Эй, что ты там делаешь?!"
                    elif Ch_Focus is KittyX:
                            ch_k "Эм, что ты делаешь?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Ты правда думаешь, что справишься со мной?"
                    elif Ch_Focus is LauraX:
                            ch_l "Ох, хочешь так просто взять и трахнуть меня?"
                    elif Ch_Focus is JeanX:
                            ch_j "Хочешь просто так взять и засадить?"
                    elif Ch_Focus is StormX:
                            ch_s "Ты точно хочешь именно этого?"
                    elif Ch_Focus is JubesX:
                            ch_v "Ох! Хочешь вставить его прямо туда, да?"
                    elif Ch_Focus is GwenX:
                            ch_g "Эй! Подожди!"
                    elif Ch_Focus is BetsyX:
                            ch_b "Пардон?!"
                    elif Ch_Focus is DoreenX:
                            ch_d "Воу! Что ты-?. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Эй, подожди секунду!"
                    menu:
                        extend ""
                        "Извини-извини! Я уже ничего не делаю.":
                            if Approval:
                                    $ Ch_Focus.FaceChange("sexy", 1)
                                    $ Ch_Focus.Statup("Obed", 70, 3)
                                    $ Ch_Focus.Statup("Inbt", 50, 3)
                                    $ Ch_Focus.Statup("Inbt", 70, 1)
                                    if Ch_Focus is RogueX:
                                            if not Player.Male:
                                                ch_r "Ну, раз уж ты поубавила свой пыл, думаю, мы можем попробовать. . ."
                                            else:
                                                ch_r "Ну, раз уж ты поубавил свой пыл, думаю, мы можем попробовать. . ."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Ну. . . Я не говорила, что не хочу. . ."
                                    elif Ch_Focus is EmmaX:
                                            if not Player.Male:
                                                ch_e "Я готова попробовать, если ты тоже готова. . ."
                                            else:
                                                ch_e "Я готова попробовать, если ты тоже готов. . ."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Нет-нет, все нормально. . ."
                                    elif Ch_Focus is JeanX:
                                            ch_j "О, нет, все нормально."
                                    elif Ch_Focus is StormX:
                                            if not Player.Male:
                                                ch_s "Я готова попробовать, если ты готова. . ."
                                            else:
                                                ch_s "Я готова попробовать, если ты готов. . ."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Эй, я не говорила останавливаться. . ."
                                    elif Ch_Focus is GwenX:
                                            if not Player.Male:
                                                ch_g "Ох, прости, ты просто удивила меня. . ."
                                            else:
                                                ch_g "Ох, прости, ты просто удивил меня. . ."
                                    elif Ch_Focus is BetsyX:
                                            if not Player.Male:
                                                ch_b "Ты застала меня врасплох, можешь продолжать. . ."
                                            else:
                                                ch_b "Ты застал меня врасплох, можешь продолжать. . ."
                                    elif Ch_Focus is DoreenX:
                                            if not Player.Male:
                                                ch_d "Ох! Ох. . . ты застала меня врасплох. . ."
                                            else:
                                                ch_d "Ох! Ох. . . ты застал меня врасплох. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "Я сказала \"подожди,\" а не \"остановись.\" . ."
                                    jump Girl_SexPrep
                            else:
                                    "Вы отстраняетесь, прежде чем успеваете войти внутрь."
                                    $ Ch_Focus.FaceChange("bemused", 1)
                                    if Ch_Focus is RogueX:
                                            if Ch_Focus.Sex:
                                                ch_r "Ну ладно, [RogueX.Petname], никто не пострадал, только в будущем предупреждай."
                                            else:
                                                ch_r "Ну ладно, [RogueX.Petname], я еще не совсем готов к этому, но, может быть, если ты в следующий раз вежливо попросишь . . ."
                                    elif Ch_Focus is KittyX:
                                            if Ch_Focus.Sex:
                                                ch_k "Может, стоило сначала[KittyX.like]предупредить меня?"
                                            else:
                                                ch_k "Может, стоило сначала[KittyX.like]предупредить меня? Я не думаю, что[KittyX.like]готова к таким вещам. . ."
                                    elif Ch_Focus is EmmaX:
                                            if Ch_Focus.Sex:
                                                ch_e "Может, сначала стоит спросить, [EmmaX.Petname]?"
                                            else:
                                                ch_e "Возможно в другой раз, когда ты вежливо попросишь."
                                    elif Ch_Focus is LauraX:
                                            if Ch_Focus.Sex:
                                                ch_l "Может быть, сначала стоит спрашивать, [LauraX.Petname]?"
                                            else:
                                                if not Player.Male:
                                                    ch_l "Может, если бы ты сначала спросила. . ."
                                                else:
                                                    ch_l "Может, если бы ты сначала спросил. . ."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Тебе стоило бы сначала спросить, [JeanX.Petname]."
                                    elif Ch_Focus is StormX:
                                            if Ch_Focus.Sex:
                                                ch_s "Может, сначала стоит спросить, [StormX.Petname]?"
                                            else:
                                                ch_s "Возможно, в другой раз. . ."
                                    elif Ch_Focus is JubesX:
                                            if Ch_Focus.Sex:
                                                ch_v "Сложно сначала просто спросить, [JubesX.Petname]?"
                                            else:
                                                ch_v "Тебе следовало бы сначала спросить. . ."
                                    elif Ch_Focus is GwenX:
                                            if Ch_Focus.Sex:
                                                ch_g "Ты можешь сначала спрашивать, [GwenX.Petname]?"
                                            else:
                                                ch_g "Сначала стоит спрашивать. . ."
                                    elif Ch_Focus is BetsyX:
                                            if Ch_Focus.Sex:
                                                ch_b "Тебе не кажется, что стоило сперва предупредить, [BetsyX.Petname]?"
                                            else:
                                                if not Player.Male:
                                                    ch_b "Было бы неплохо, если бы ты сначала предупредила. . ."
                                                else:
                                                    ch_b "Было бы неплохо, если бы ты сначала предупредил. . ."
                                    elif Ch_Focus is DoreenX:
                                            if Ch_Focus.Sex:
                                                ch_d "Тебе следовало сперва спросить, [DoreenX.Petname]. . ."
                                            else:
                                                ch_d "Я. . . следует сперва спрашивать, прежде чем делать что-то подобное. . ."
                                    elif Ch_Focus is WandaX:
                                            if Ch_Focus.Sex:
                                                if not Player.Male:
                                                    ch_w "Послушай, если бы ты сперва спросила, я бы, возможно, согласилась. . ."
                                                else:
                                                    ch_w "Послушай, если бы ты сперва спросил, я бы, возможно, согласилась. . ."
                                            else:
                                                if not Player.Male:
                                                    ch_w "Послушай, если бы ты сперва спросила, то, возможно. . . ладно, не важно. . ."
                                                else:
                                                    ch_w "Послушай, если бы ты сперва спросил, то, возможно. . . ладно, не важно. . ."
                        "Просто начать трахать.":
                            $ Ch_Focus.Statup("Love", 80, -10, 1)
                            $ Ch_Focus.Statup("Love", 200, -10)
                            "Вы слегка входите в нее."
                            $ Ch_Focus.Statup("Obed", 70, 3)
                            $ Ch_Focus.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(Ch_Focus, 800, "O", TabM=1):   #Checks if Obed is 700+
                                $ Ch_Focus.FaceChange("angry")
                                "[Ch_Focus.Name] отталкивает вас и наотмашь бьет по лицу."
                                if Ch_Focus is RogueX:
                                        if not Player.Male:
                                            ch_r "Манда!"
                                        else:
                                            ch_r "Мудак!"
                                        ch_r "Если ты хочешь так со мной обращаться, то мы закончили!"
                                elif Ch_Focus is KittyX:
                                        if not Player.Male:
                                            ch_k "Дура!"
                                        else:
                                            ch_k "Придурок!"
                                        ch_k "Я не потерплю такого дерьма!"
                                elif Ch_Focus is EmmaX:
                                        if not Player.Male:
                                            ch_e "Нахалка!"
                                        else:
                                            ch_e "Нахал!"
                                        ch_e "Не испытывай мое терпение."
                                elif Ch_Focus is LauraX:
                                        if not Player.Male:
                                            ch_l "Сука."
                                        else:
                                            ch_l "Гондон."
                                        ch_l "Не зли меня."
                                elif Ch_Focus is JeanX:
                                        ch_j "Знай, мне не нужны никакие суперсилы, чтобы избить тебя."
                                elif Ch_Focus is StormX:
                                        ch_s "Очень жаль."
                                        ch_s "Боюсь, этого не произойдет."
                                elif Ch_Focus is JubesX:
                                        ch_v "Со мной такое не пройдет!"
                                elif Ch_Focus is GwenX:
                                        ch_g "Эй!"
                                        ch_g "Не нарушай мои личные границы."
                                elif Ch_Focus is BetsyX:
                                        ch_b "Ну и ну!"
                                        ch_b "Боюсь, ты переходишь все границы."
                                elif Ch_Focus is DoreenX:
                                        ch_d "Эй!"
                                        ch_d "Не. . . не шути так."
                                elif Ch_Focus is WandaX:
                                        ch_w "Воу!"
                                        ch_w "Довольно."
                                $ Ch_Focus.Statup("Love", 50, -10, 1)
                                $ Ch_Focus.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                call expression Ch_Focus.Tag + "_Sex_Reset"
                                $ Ch_Focus.RecentActions.append("angry")
                                $ Ch_Focus.DailyActions.append("angry")
                            else:
                                $ Ch_Focus.FaceChange("sad")
                                $ Ch_Focus.Statup("Love", 200, -10)
                                $ Ch_Focus.Statup("Obed", 99, 10)
                                if Ch_Focus is JeanX:
                                        "Похоже, [JeanX.Name] не в восторге от этого, но вам повезло, что она готова попробовать."
                                else:
                                        "Похоже, [Ch_Focus.Name_dat] это не нравится, вам повезло, что она такая послушная."
                                jump Girl_SexPrep
                return
    #End Auto


    if not Ch_Focus.Sex and "no sex" not in Ch_Focus.RecentActions:
            #first time
            $ Ch_Focus.FaceChange("surprised", 1)
            $ Ch_Focus.Mouth = "kiss"
            if Ch_Focus is RogueX:
                    ch_r "Значит, ты хочешь перейти на следующий уровень? Настоящий секс? . . ."
            elif Ch_Focus is KittyX:
                    ch_k "У меня не так уж и много опыта в этом. . . "
            elif Ch_Focus is EmmaX:
                    if not Player.Male:
                        ch_e "Хм, ты уверена, что действительно готова к этому? . . "
                    else:
                        ch_e "Хм, ты уверен, что действительно готов к этому? . . "
            elif Ch_Focus is LauraX:
                    ch_l "Хм, ты хочешь трахнуть меня? . . "
            elif Ch_Focus is JeanX:
                    ch_j "О, значит, ты хочешь трахнуться . . "
            elif Ch_Focus is StormX:
                    if not Player.Male:
                        ch_s "Хм, а ты уверена, что готова к этому? . . "
                    else:
                        ch_s "Хм, а ты уверен, что готов к этому? . . "
            elif Ch_Focus is JubesX:
                    ch_v "Ох. . . ты хочешь потрахаться. . . "
            elif Ch_Focus is GwenX:
                    ch_g "Ох, эм. . . секс . . "
            elif Ch_Focus is BetsyX:
                    ch_b "Ох, ты не прочь потрахаться . . "
            elif Ch_Focus is DoreenX:
                    ch_d "Ох. Значит, ты хочешь, эм. . . "
                    ch_d "Ты хочешь. . . заняться \"этим\". . ."
            elif Ch_Focus is WandaX:
                    ch_w "Ты хочешь потрахаться?"
            if not Player.Male:
                if Ch_Focus is RogueX:
                        ch_r "Я чего-то о тебе не знаю?"
                elif Ch_Focus is KittyX:
                        ch_k "Как ты[KittyX.like]собираешься. . .?"
        #        elif Ch_Focus is EmmaX:
        #                pass
                elif Ch_Focus is LauraX:
                        ch_l "Мне кажется, у тебя кое-чего нет. . ."
                elif Ch_Focus is JeanX:
                        cch_j "Я не вижу у тебя члена."
        #        elif Ch_Focus is StormX:
        #                pass
                elif Ch_Focus is JubesX:
                        ch_v "И как именно ты собираешься это сделать?"
                elif Ch_Focus is GwenX:
                        ch_g "Как ты. . . собираешься это сделать? . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Но как нам это. . . сделать? . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Как ты. . . это сделаешь? . ."
                elif Ch_Focus is WandaX:
                        ch_w "У тебя с собой игрушки, я права?"
                menu:
                    "Ага. . ." if Ch_Focus in (EmmaX,StormX):
                            pass
                    "Я подготовилась. . ." if Ch_Focus not in (EmmaX,StormX):
                            pass
                    "Скоро ты поймешь. . .":
                            $ Ch_Focus.Statup("Obed", 90, 3)
                            $ Tempmod -= 5
            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                if Ch_Focus is RogueX:
                        ch_r "Ты правда хочешь зайти так далеко?"
                elif Ch_Focus is KittyX:
                        ch_k "Ты правда хочешь это сделать?"
                elif Ch_Focus is EmmaX:
                        if not Player.Male:
                            ch_e "Ты уверена, что именно так хочешь воспользоваться своим. . . влиянием?"
                        else:
                            ch_e "Ты уверен, что именно так хочешь воспользоваться своим. . . влиянием?"
                elif Ch_Focus is LauraX:
                        ch_l "Довольно смело с твоей стороны. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Довольно смело с твоей стороны. . ."
                elif Ch_Focus is StormX:
                        ch_s "Так ты этого от меня хочешь?"
                elif Ch_Focus is JubesX:
                        ch_v "Мне кажется, ты перегибаешь. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Я предполагала, что дойдет до этого. . ."
                        if not GwenX.Anal:
                            ch_g "По крайней мере, не анал. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Я ожидала этого. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я. . . думаю, мне не следует удивляться. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Я даже не предполагала, что все будет так. . ."
    #End first time question


    if not Ch_Focus.Sex and Approval:
            #First time dialog
            if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -30, 1)
                    $ Ch_Focus.Statup("Love", 20, -20, 1)
            elif Ch_Focus.Love >= (Ch_Focus.Obed + Ch_Focus.Inbt):
                    $ Ch_Focus.FaceChange("sexy")
                    $ Ch_Focus.Brows = "sad"
                    $ Ch_Focus.Mouth = "smile"
                    if Ch_Focus is RogueX:
                            ch_r "Ну, я никогда раньше не могла этим заняться, так что это может быть весело."
                    elif Ch_Focus is KittyX:
                            if not Player.Male:
                                ch_k "Я не хочу, чтобы ты думала, что я какая-то шлюха. . ."
                            else:
                                ch_k "Я не хочу, чтобы ты думал, что я какая-то шлюха. . ."
                    elif Ch_Focus is EmmaX:
                            if not Player.Male:
                                ch_e "Я бы не хотела, чтобы ты пострадала. . ."
                            else:
                                ch_e "Я бы не хотела, чтобы ты пострадал. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Ну, ты выглядишь так мило, когда просишь. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "А я все думала, когда же это произойдет. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Я бы не хотела. . . перегружать тебе. . ."
                    elif Ch_Focus is JubesX:
                            if not Player.Male:
                                ch_v "Оу, так мило, что ты спросила. . ."
                            else:
                                ch_v "Оу, так мило, что ты спросил. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Мне интересно, почему ты так долго. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Мне даже немного интересно, почему ты предлагаешь так поздно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я. . . я вроде как надеялась, что однажды ты этого захочешь. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Я надеялась, что однажды до этого дойдет. . ."
            elif (Ch_Focus.Obed >= Ch_Focus.Inbt) or (Ch_Focus is JeanX and JeanX.Obed >= (JeanX.Inbt - JeanX.IX)):
                    $ Ch_Focus.FaceChange("normal")
                    if Ch_Focus in (EmmaX,StormX,BetsyX):
                            call AnyLine(Ch_Focus,"Если это то, чего ты хочешь, "+Ch_Focus.Petname+". . .")
                    else:
                            call AnyLine(Ch_Focus,"Если ты так этого хочешь, "+Ch_Focus.Petname+". . .")
            else: # Uninhibited
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Mouth = "smile"
                    if Ch_Focus is RogueX:
                            ch_r "Ммм, я всегда хотела попробовать. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Не могу сказать, что это не приходило мне в голову. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Я надеялась, что ты спросишь. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Я надеялась, что ты спросишь. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "А я все думала, когда же это произойдет. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Я надеялась, что ты спросишь. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Я надеялась, что ты спросишь. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Мне интересно, почему ты так долго. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Мне даже немного интересно, почему ты предлагаешь так поздно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Мне немного любопытно, каково это. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Я надеялась, что однажды до этого дойдет. . ."
    #End first time dialog

    elif Approval:
            #Second time+ dialog
            $ Ch_Focus.FaceChange("sexy", 1)
            if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -3, 1)
                    $ Ch_Focus.Statup("Love", 20, -2, 1)
                    if Ch_Focus is RogueX:
                            ch_r "Ты правда этого хочешь?"
                    elif Ch_Focus is KittyX:
                            ch_k "Опять? Зачем ты так со мной?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Снова? Похоже, ты хочешь меня совсем загонять."
                    elif Ch_Focus is LauraX:
                            ch_l "Надеюсь, я тебя не измотаю."
                    elif Ch_Focus is JeanX:
                            ch_j "Когда-нибудь ты за это заплатишь. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Ох, снова?"
                    elif Ch_Focus is JubesX:
                            ch_v "Что ж. . . не привыкай к этому."
                    elif Ch_Focus is GwenX:
                            ch_g "Наверно, можно. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Полагаю, что можно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я. . . если это так необходимо. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Хорошо, если так нужно. . ."
            elif not Taboo and "tabno" in Ch_Focus.DailyActions:
                    call Sex_Basic_Dialog(Ch_Focus,"tabyes") #"This -would- be a better place for it. . ."
            elif "sex" in Ch_Focus.RecentActions:
                    if Ch_Focus is RogueX:
                            ch_r "Хочешь повторить? Ладно."
                    elif Ch_Focus is KittyX:
                            ch_k "Еще раз? Ладно."
                    elif Ch_Focus is EmmaX:
                            if not Player.Male:
                                ch_e "Снова? [EmmaX.Petname], Ты такая ненасытная!"
                            else:
                                ch_e "Снова? [EmmaX.Petname], Ты такой ненасытный!"
                    elif Ch_Focus is LauraX:
                            ch_l "Снова? Ну, пеняй на себя."
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно, [JeanX.Petname]. . ."
                    elif Ch_Focus is StormX:
                            if not Player.Male:
                                ch_s "Снова? [StormX.Petname], ну ты и львица!"
                            else:
                                ch_s "Снова? [StormX.Petname], ну ты и лев!"
                    elif Ch_Focus is JubesX:
                            ch_v "Снова? Хм. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Снова? И почему я не удивлена. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Снова? Я не должна от тебя отставать. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Снова? Ох. . . хорошо. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Снова? Ого. . ."
                    jump Girl_SexPrep
            elif "sex" in Ch_Focus.DailyActions:
                    if Ch_Focus in (EmmaX,StormX,BetsyX):
                        $ Line = renpy.random.choice(["Снова?",
                            "Хочешь еще раз?",
                            "Должно быть, я талантливее, чем я думала.",
                            "Тебе все еще мало?",
                            "Снова? Что ж, я не должна от тебя отставать. . ." ])
                    else:
                        $ Line = renpy.random.choice(["Желаешь добавки?",
                            "Желаешь еще разок?",
                            "Наверное, я лучше, чем я думала.",
                            "Тебе все еще мало?",
                            Ch_Focus.Petname + " ты меня совсем загоняешь."])
                    call AnyLine(Ch_Focus,Line)
            else:
                    if Ch_Focus in (EmmaX,StormX,BetsyX):
                        $ Line = renpy.random.choice(["Я просто слишком неотразима?",
                            "Хочешь еще заход?",
                            "Должно быть, я талантливее, чем я думала.",
                            "Думаю, я знаю, чего ты хочешь.",
                            "Хочешь взять меня?"])
                    else:
                        $ Line = renpy.random.choice(["Хочешь меня?",
                            "Желаешь еще заход?",
                            "Должно быть, я лучше, чем я думала.",
                            "Я думаю, ты знаешь, что делаешь.",
                            "Ты хочешь. . . сделать это?"])
                    call AnyLine(Ch_Focus,Line)
            $ Line = 0
    #end Second time+ dialog

    if Approval >= 2:
            #She's into it. . .
            if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 1)
                    if Ch_Focus is RogueX:
                            ch_r "Хорошо."
                    elif Ch_Focus is KittyX:
                            ch_k "Лаааадно."
                    elif Ch_Focus is EmmaX:
                            ch_e "Ох, хорошо, если ты заткнешься."
                    elif Ch_Focus is LauraX:
                            ch_l "Ладно. Только сделай все хорошо."
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно. Только сделай все хорошо."
                    elif Ch_Focus is StormX:
                            ch_s "Ох, хорошо, если это тебя удовлетворит."
                    elif Ch_Focus is JubesX:
                            ch_v "Лучше бы это того стоило."
                    elif Ch_Focus is GwenX:
                            ch_g "Ладно, думаю, будет весело."
                    elif Ch_Focus is BetsyX:
                            ch_b "Конечно, пожалуй, я смогу это вынести."
                    elif Ch_Focus is DoreenX:
                            ch_d "Хорошо, тогда давай займемся делом."
                    elif Ch_Focus is WandaX:
                            ch_w "Ладно, давай сделаем это."
            else:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Love", 90, 1)
                    $ Ch_Focus.Statup("Inbt", 50, 3)
                    $ Line = renpy.random.choice(["Ну. . . ладно, давай займемся этим.",
                        "Конечно.",
                        "Наверное, можно.",
                        "Хмммм, конечно.",
                        "Звучит весело."])
                    call AnyLine(Ch_Focus,Line)
                    $ Line = 0
            $ Ch_Focus.Statup("Obed", 20, 1)
            $ Ch_Focus.Statup("Obed", 60, 1)
            $ Ch_Focus.Statup("Inbt", 70, 2)
            jump Girl_SexPrep

    else:
            #She's not into it, but maybe. . .
            $ Ch_Focus.FaceChange("angry")
            if "no sex" in Ch_Focus.DailyActions:
                    call Sex_Basic_Dialog(Ch_Focus,"norecent")
            elif Taboo and "tabno" in Ch_Focus.DailyActions:
                    call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
            elif not Ch_Focus.Sex:
                $ Ch_Focus.FaceChange("bemused")
                if Ch_Focus is RogueX:
                        ch_r "Я не уверена, что уже готова, [RogueX.Petname]. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Я не думаю, что я[KittyX.like]готова? . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Я очень сомневаюсь, что ты понимаешь, во что ввязываешься. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Ох, ты и понятия не имеешь, что тебя ждет. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Ох, это могло бы быть интересно, но. . ."
                elif Ch_Focus is StormX:
                        ch_s "Я очень сомневаюсь, что ты понимаешь, что тебя ждет. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Хм, тебе следовало лучше подготовиться. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Наверное, это было неизбежно. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Пожалуй, рано или поздно до этого должно было дойти, но я пока не готова. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "У меня, эм. . . нет нужного опыта. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Пожалуй, я знала, что это однажды произойдет. . ."
            else:
                $ Ch_Focus.FaceChange("bemused")
                if Ch_Focus is RogueX:
                        ch_r "Не сейчас, [RogueX.Petname]. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Может[KittyX.like]не сейчас? . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Возможно, лучше в другой раз? . ."
                elif Ch_Focus is LauraX:
                        ch_l "Может быть, позже? . ."
                elif Ch_Focus is JeanX:
                        ch_j "Я сейчас не в настроении. . ."
                elif Ch_Focus is StormX:
                        ch_s "Возможно, в другой раз? . ."
                elif Ch_Focus is JubesX:
                        ch_v "Может, быть позже? . ."
                elif Ch_Focus is GwenX:
                        ch_g "Я не уверена, может, не сейчас? . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Я сомневаюсь, возможно, позже? . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я, эм. . . я пока не готова. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Я не уверена, что хочу этого сейчас. . ."
            menu:
                extend ""
                "Извини, забудь." if "no sex" in Ch_Focus.DailyActions:
                        $ Ch_Focus.FaceChange("bemused")
                        call Sex_Basic_Dialog(Ch_Focus,"noproblem")  # ch_d "Aw, don't worry about it. . ."
                        return
                "Может, в другой раз?" if "no sex" not in Ch_Focus.DailyActions:
                        $ Ch_Focus.FaceChange("sexy")
                        call Sex_Basic_Dialog(Ch_Focus,"maybe")  # ch_d "I'll think about it, [Ch_Focus.Petname]."
                        $ Ch_Focus.Statup("Love", 80, 2)
                        $ Ch_Focus.Statup("Inbt", 70, 2)
                        if Taboo:
                            $ Ch_Focus.RecentActions.append("tabno")
                            $ Ch_Focus.DailyActions.append("tabno")
                        $ Ch_Focus.RecentActions.append("no sex")
                        $ Ch_Focus.DailyActions.append("no sex")
                        return
                "Думаю, тебе понравится не меньше, чем мне. . .":
                        if Approval:
                            $ Ch_Focus.FaceChange("sexy")
                            $ Ch_Focus.Statup("Obed", 90, 2)
                            $ Ch_Focus.Statup("Obed", 50, 2)
                            $ Ch_Focus.Statup("Inbt", 70, 3)
                            $ Ch_Focus.Statup("Inbt", 40, 2)
                            $ Line = renpy.random.choice(["Ага, может быть. . .",
                                "Наверное. . .",
                                "Ну хорошо, вставляй его.",
                                ". . . хорошее замечание. . ."])
                            call AnyLine(Ch_Focus,Line)
                            $ Line = 0
                            jump Girl_SexPrep
                "Просто смирись.":                                               # Pressured into it
                        $ Approval = ApprovalCheck(Ch_Focus, 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and Ch_Focus.Forced):
                            $ Ch_Focus.FaceChange("sad")
                            $ Ch_Focus.Statup("Love", 70, -5, 1)
                            $ Ch_Focus.Statup("Love", 200, -5)
                            if Ch_Focus is RogueX:
                                    ch_r "Ладно. Давай уже побыстрее закончим."
                            elif Ch_Focus is KittyX:
                                    ch_k "Хорошо! . .  ладно, вставляй его."
                            elif Ch_Focus is EmmaX:
                                    ch_e "Хорошо, если ты заткнешься."
                            elif Ch_Focus is LauraX:
                                    ch_l "Хорошо, если ты заткнешься."
                            elif Ch_Focus is JeanX:
                                    ch_j ". . ."
                                    ch_j ". . . ладно. . ."
                            elif Ch_Focus is StormX:
                                    ch_s "Ладно, только замолчи."
                            elif Ch_Focus is JubesX:
                                    ch_v ". . . похоже, мне придется. . ."
                            elif Ch_Focus is GwenX:
                                    ch_g "О, пожалуй, мне придется."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Ох, если это так необходимо. . ."
                            elif Ch_Focus is DoreenX:
                                    ch_d "\"Смириться.\" . . Ну ладно. . . "
                                    ch_d "Ладно. . ."
                            elif Ch_Focus is WandaX:
                                    ch_w ". . . ладно."
                            $ Ch_Focus.Statup("Obed", 80, 4)
                            $ Ch_Focus.Statup("Inbt", 80, 1)
                            $ Ch_Focus.Statup("Inbt", 60, 3)
                            $ Ch_Focus.Forced = 1
                            jump Girl_SexPrep
                        else:
                            $ Ch_Focus.Statup("Love", 200, -20)
                            if Ch_Focus is DoreenX:
                                    ch_d "Я не собираюсь с этим \"мириться!\""
                            $ Ch_Focus.RecentActions.append("angry")
                            $ Ch_Focus.DailyActions.append("angry")
                #end menu
    #end Approval check

    #She refused all offers.
    $ Ch_Focus.ArmPose = 1
    if "no sex" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"noday") #"Stop asking."
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("angry", 1)
            if Ch_Focus is RogueX:
                    ch_r "Можешь даже не пытаться."
            elif Ch_Focus is KittyX:
                    ch_k "Даже не пытайся."
            elif Ch_Focus is EmmaX:
                    ch_e "Не переоценивай свое влияние."
            elif Ch_Focus is LauraX:
                    ch_l "Я больше не подчиняюсь приказам."
            elif Ch_Focus is JeanX:
                    ch_j "Я королева!"
            elif Ch_Focus is StormX:
                    ch_s "Не переоценивай свою власть."
            elif Ch_Focus is JubesX:
                    ch_v "У меня есть принципы."
            elif Ch_Focus is GwenX:
                    ch_g "Это. . . слишком."
            elif Ch_Focus is BetsyX:
                    ch_b "Боюсь, я не должна этого делать"
            elif Ch_Focus is DoreenX:
                    ch_d "Это. . . уже слишком."
            elif Ch_Focus is WandaX:
                    ch_w "Я не собираюсь с этим мириться."
            $ Ch_Focus.Statup("Lust", 200, 5)
            if Ch_Focus.Love > 300:
                    $ Ch_Focus.Statup("Love", 70, -2)
            $ Ch_Focus.Statup("Obed", 50, -2)
            if Ch_Focus is JeanX:
                    ch_j "Я не подчиняюсь приказам."
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ Ch_Focus.FaceChange("angry", 1)
            $ Ch_Focus.RecentActions.append("tabno")
            $ Ch_Focus.DailyActions.append("tabno")
            call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You picked a bad place for this. . ."
            $ Ch_Focus.Statup("Lust", 200, 5)
            $ Ch_Focus.Statup("Obed", 50, -3)
    elif Ch_Focus.Sex:
            $ Ch_Focus.FaceChange("sad")
            if Ch_Focus is RogueX:
                    if not Player.Male:
                        ch_r "Вместо этого можешь пойти и трахнуть себя сама."
                    else:
                        ch_r "Вместо этого можешь пойти и трахнуть себя сам."
            elif Ch_Focus is KittyX:
                    if not Player.Male:
                        ch_k "Может возьмешь[KittyX.like]и трахнешь себя сама, а?"
                    else:
                        ch_k "Может возьмешь[KittyX.like]и трахнешь себя сам, а?"
            elif Ch_Focus is EmmaX:
                    ch_e "Думаю, ты и без меня справишься."
            elif Ch_Focus is LauraX:
                    ch_l "Пойди и просто подрочи."
            elif Ch_Focus is JeanX:
                    ch_j "Иди и трахни кого-нибудь другого."
            elif Ch_Focus is StormX:
                    ch_s "Уверена, ты сможешь справиться и без меня."
            elif Ch_Focus is JubesX:
                    ch_v "Придумай, чем еще можно заняться."
            elif Ch_Focus is GwenX:
                    ch_g "Уверена, ты сможешь найти кого-нибудь другого, кто поможет тебе. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Уверена, ты сможешь найти множество альтернатив. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Если ты этого хочешь. . . тебе придется поискать где-нибудь в другом месте. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Найди для этого кого-нибдуь другого. . ."
    else:
            $ Ch_Focus.FaceChange("normal", 1)
            if Ch_Focus is RogueX:
                    ch_r "Ни за что."
            elif Ch_Focus is KittyX:
                    ch_k "Ненене."
            elif Ch_Focus is EmmaX:
                    ch_e "Боюсь, что нет."
            elif Ch_Focus is LauraX:
                    ch_l "Ага, но нет."
            elif Ch_Focus is JeanX:
                    ch_j "Мне не интересно."
            elif Ch_Focus is StormX:
                    ch_s "Я вынуждена отказаться."
            elif Ch_Focus is JubesX:
                    ch_v "Ага, но нет."
            elif Ch_Focus is GwenX:
                    ch_g "Я не могу."
            elif Ch_Focus is BetsyX:
                    ch_b "Я не могу."
            elif Ch_Focus is DoreenX:
                    ch_d "Это. . . очень интимное дело, так что. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Нет."
    $ Ch_Focus.RecentActions.append("no sex")
    $ Ch_Focus.DailyActions.append("no sex")
    $ Tempmod = 0
    return

label Girl_SexPrep: #rkeljsvg
    # Modification mode
    if is_playing_music(audio.girl_sex):
        $ play_music(name=audio.girl_sex, loop=True)
    # -----------------

##    #fix remove
#    if Ch_Focus is WandaX:
#        "Not currently available."
#        return
##    #fix remove
    call Seen_First_Peen(Ch_Focus,Partner,React=Situation)
    call expression Ch_Focus.Tag + "_Sex_Launch" pass ("hotdog")

    if Situation == Ch_Focus:
            #Girl auto-starts
            $ Situation = 0
            call Girl_PantsOff(Ch_Focus)   #"Girl rolls back and pulls you toward her, sliding her pants down as she does so."
            $ Ch_Focus.Upskirt = 1
            $ Line = 0
            $ Ch_Focus.SeenPanties = 1
            if not Player.Male:
                "Она проводит кончиком резинового члена по своей киске, похоже, она хочет, чтобы вы вставили его."
            else:
                "Она проводит головкой вашего члена по своей киске, похоже, она хочет, чтобы вы вставили его."
            menu:
                "Что будете делать?"
                "Не сопротивляться.":
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 2)
                    "[Ch_Focus.Name] вставляет его внутрь."
                "Похвалить ее.":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    ch_p "О да, [Ch_Focus.Pet], давай сделаем это."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] вставляет его внутрь."
                    $ Ch_Focus.Statup("Love", 85, 1)
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    $ Ch_Focus.FaceChange("surprised")
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    ch_p "[Ch_Focus.Pet], давай пока не будем."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] отстраняется."
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 1)
                    $ Ch_Focus.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ Ch_Focus.AddWord(1,"refused","refused")
                    return
            $ Ch_Focus.PantiesDown = 1
            call Girl_First_Bottomless(Ch_Focus,1)

    elif Situation != "auto":
            call AutoStrip(Ch_Focus)
            call Girl_Initiates(Ch_Focus)      #"She presses against you and your cock pops in."

    else:  #if Situation == "auto"
            if (Ch_Focus.PantsNum() >= 6 and not Ch_Focus.Upskirt) and (Ch_Focus.Panties and not Ch_Focus.PantiesDown):
                "Вы быстро стягиваете с нее штаны и [get_clothing_name(Ch_Focus.Panties, vin)] и прижимаетесь к ее щелке."
            elif (Ch_Focus.Panties and not Ch_Focus.PantiesDown):
                "Вы быстро стягиваете с нее [get_clothing_name(Ch_Focus.Panties, vin)] и прижимаетесь к ее щелке."
            $ Ch_Focus.Upskirt = 1
            $ Ch_Focus.PantiesDown = 1
            $ Ch_Focus.SeenPanties = 1
            call Girl_First_Bottomless(Ch_Focus,1)

    if Player.Focus >= 50:
            if Ch_Focus is RogueX:
                    ch_r "Вижу, тебе уже не терпится. . ."
            elif Ch_Focus is KittyX:
                if not Ch_Focus.Sex:
                    if not Player.Male:
                        ch_k "Ох, похоже, ты. . . готова. . ."
                    else:
                        ch_k "Ох, похоже, ты. . . готов. . ."
            elif Ch_Focus is EmmaX:
                if Player.Male:
                    ch_e "Честное слово, [EmmaX.Petname], твой член достаточно тверд, чтобы расколоть алмаз."
                else:
                    ch_e "Честное слово, [EmmaX.Petname], твоя киска блестит подобно алмазу."
            elif Ch_Focus is LauraX:
                    if not Player.Male:
                        ch_l "Приятно видеть, что ты уже готова. . ."
                    else:
                        ch_l "Приятно видеть, что ты уже готов. . ."
            elif Ch_Focus is JeanX:
                    ch_j "Я смотрю, тебя даже не нужно подбадривать. . ."
            elif Ch_Focus is StormX:
                    if not Player.Male:
                        ch_s "Должна отметить, [StormX.Petname], ты выглядишь очень. . . возбужденной."
                    else:
                        ch_s "Должна отметить, [StormX.Petname], ты выглядишь очень. . . возбужденным."
            elif Ch_Focus is JubesX:
                    if not Player.Male:
                        ch_v "Нууу, по крайней мере, ты, кажется, рада этому. . ."
                    else:
                        ch_v "Нууу, по крайней мере, ты, кажется, рад этому. . ."
            elif Ch_Focus is GwenX:
                    if not Player.Male:
                        ch_g "По крайней мере, ты возбуждена. . ."
                    else:
                        ch_g "По крайней мере, ты возбужден. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Я вижу, что добилась желаемого эффекта. . ."
            elif Ch_Focus is DoreenX:
                    if not Player.Male:
                        ch_d "Ох! Похоже, ты уже готова. . ."
                    else:
                        ch_d "Ох! Похоже, ты уже готов. . ."
            elif Ch_Focus is WandaX:
                    if not Player.Male:
                        ch_w "Хорошо, ты уже готова. . ."
                    else:
                        ch_w "Хорошо, ты уже готов. . ."
    if not Ch_Focus.Sex:
        if Ch_Focus.Forced:
                $ Ch_Focus.Statup("Love", 90, -150)
                $ Ch_Focus.Statup("Obed", 70, 60)
                $ Ch_Focus.Statup("Inbt", 80, 50)
        else:
                $ Ch_Focus.Statup("Love", 90, 30)
                $ Ch_Focus.Statup("Obed", 70, 30)
                $ Ch_Focus.Statup("Inbt", 80, 60)

    if Situation:
            $ renpy.pop_call()
            $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Player.Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
            $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no sex")
    $ Ch_Focus.RecentActions.append("sex")
    $ Ch_Focus.DailyActions.append("sex")

label Girl_Sex_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(Ch_Focus)
        call expression Ch_Focus.Tag + "_Sex_Launch" pass ("sex")
        if Speed >= 4:
                $ Speed = 2
    #            call Speed_Shift(2)
        $ Ch_Focus.LustFace()
        $ Player.Cock = "in"
        $ Trigger = "sex"
        $ Ch_Focus.Upskirt = 1
        $ Ch_Focus.PantiesDown = 1

        if Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . ." if Speed:
                                    pass
                        "Продолжать. . . (locked)" if not Speed:
                                    pass

                        "Начать? . ." if not Speed:
                                    # Modification mode
                                    if is_playing_music(audio.girl_doggy) and Ch_Focus.Pose == "doggy":
                                        $ play_music(name=audio.girl_doggy, loop=True)
                                    else:
                                        $ play_music(name=audio.girl_sex, loop=True)
                                    # -----------------

                                    $ Speed = 1
#                                    call Speed_Shift(1)
                        "Быстрее. . ." if 0 < Speed < 3:
                                    $ Speed += 1
#                                    call Speed_Shift(Speed+1)
                                    "Вы немного ускоряетесь."
                        "Быстрее. . . (locked)" if Speed >= 3:
                                    pass

                        "Помедленнее. . ." if Speed:
                                    $ Speed -= 1
#                                    call Speed_Shift(Speed-1)
                                    "Вы немного замедляетесь."
                        "Помедленнее. . . (locked)" if not Speed:
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_Sex_Cycle

                        "Развернуть ее":
                                    # Modification mode
                                    if is_playing_music(audio.girl_doggy) and Ch_Focus.Pose == "doggy":
                                        $ play_music(name=audio.girl_doggy, loop=True)
                                    else:
                                        $ play_music(name=audio.girl_sex, loop=True)
                                    # -----------------

                                    $ Ch_Focus.Pose = "doggy" if Ch_Focus.Pose != "doggy" else 0
                                    "Вы разворачиваете ее. . ."
                                    call View_Facing(Ch_Focus)
                                    jump Girl_Sex_Cycle

                        "Повернуть ее голову" if Ch_Focus.Pose == "doggy":
                                    call View_Facing(Ch_Focus,1)
                                    jump Girl_Sex_Cycle

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
                                                        "Как насчет в попку?":
                                                                $ Situation = "shift"
                                                                call Girl_SexAfter
                                                                call Girl_Sex_A
                                                        "Просто вставить прибор ей в попку [[не спрашивая].":
                                                                $ Situation = "auto"
                                                                call Girl_SexAfter
                                                                call Girl_Sex_A
                                                        "Потереться о ее киску.":
                                                                $ Situation = "pullback"
                                                                call Girl_SexAfter
                                                                call Girl_Sex_H
                                                        "Неважно":
                                                                jump Girl_Sex_Cycle
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
                                                        jump Girl_Sex_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_Sex_Cycle
                                            "Неважно":
                                                        jump Girl_Sex_Cycle
                                    "Просто посмотреть на нее.":
                                            $ Player.Cock = 0
                                            $ Speed = 0

                                    "Показывать ее ноги" if not ShowFeet:# and Ch_Focus.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet:# and Ch_Focus.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Вставить анальную пробку" if not Ch_Focus.Plug and "plug" in Ch_Focus.Inventory:
                                            call Insert_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку" if Ch_Focus.Plug:
                                            call Remove_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку (locked)" if "plug" not in Ch_Focus.Inventory:
                                            pass

                                    "Псионический Нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_Sex_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Думаю, нам стоит попробовать что-нибудь другое."
                                    call expression Ch_Focus.Tag + "_Sex_Reset"
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_SexAfter
                        "Закончить" if not MultiAction:
                                    ch_p "Думаю, нам стоит пока остановиться."
                                    call expression Ch_Focus.Tag + "_Sex_Reset"
                                    $ Line = 0
                                    jump Girl_SexAfter
        #End menu (if Line)

        call Shift_Focus(Ch_Focus)
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
                                call expression Ch_Focus.Tag + "_Sex_Reset"
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                    $ Ch_Focus.RecentActions.append("unsatisfied")
                                    $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_SexAfter
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If you're still going at it and Girl can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_SexAfter

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                if Player.Male:
                                        "Она выжала из вас все соки, вам нужно передохнуть."
                                else:
                                        "Она вас утомила, вам нужно передохнуть."
                                jump Girl_SexAfter
                            elif "unsatisfied" in Ch_Focus.RecentActions:
                                #And Ch_Focus is unsatisfied,
                                $ Line = renpy.random.choice(["Она продолжает слегка дрожать от удовольствия.",
                                    "Она тяжело дышит, пока вы ее трахаете.",
                                    "Она медленно поворачивается к вам и улыбается.",
                                    "Кажется, она не собирается останавливаться."])
                                "[Line] Продолжите?"
                                menu:
                                    extend ""
                                    "Да. Продолжим еще немного." if Player.Semen:
                                        $ Line = "Вы возвращаетесь к процессу"
                                        jump Girl_Sex_Cycle
                                    "С меня хватит." if Player.Semen:
                                        "Вы заканчиваете веселье."
                                        jump Girl_SexAfter
                                    "Нет, у меня нет сил." if not Player.Semen:
                                        "Вы заканчиваете веселье."
                                        jump Girl_SexAfter
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.Sex):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Ты уже скоро? Мне немного больно."
                    elif Ch_Focus is KittyX:
                            ch_k "Ты уже[KittyX.like]скоро?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Мы уже скоро?"
                    elif Ch_Focus is LauraX:
                            ch_l "Мы уже скоро?"
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно, может хватит уже?"
                    elif Ch_Focus is StormX:
                            ch_s "Ты скоро?"
                    elif Ch_Focus is JubesX:
                            ch_v "Эм, ты как?"
                    elif Ch_Focus is GwenX:
                            ch_g "Ты как?"
                    elif Ch_Focus is BetsyX:
                            if not Player.Male:
                                ch_b "Все так, как ты и ожидала?"
                            else:
                                ch_b "Все так, как ты и ожидал?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Ты. . . как?"
                    elif Ch_Focus is WandaX:
                            ch_w "Ты уже скоро?"
        elif Cnt == (10 + Ch_Focus.Sex):
                    $ Ch_Focus.Brows = "angry"
                    if Ch_Focus is RogueX:
                            ch_r "У меня . . .начинает . . .натирать. . . там . . [RogueX.Petname]."
                            ch_r "Мы может. . . заняться. . . чем-нибудь. . . другим?"
                    elif Ch_Focus is KittyX:
                            ch_k "Я . . . уже . . немного. . . устала. . ."
                            ch_k "Мы может. . . заняться. . . чем-нибудь. . . другим?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Я . . . немного. . . устала. . ."
                            ch_e "Может. . . займемся. . . чем-нибудь. . . другим?"
                    elif Ch_Focus is LauraX:
                            ch_l "Слушай. . . мы можем. . . попробовать что-нибудь. . . другое?"
                    elif Ch_Focus is JeanX:
                            ch_j "Слушай. . . давай. . . может быть. . . закончим?"
                    elif Ch_Focus is StormX:
                            ch_s "Я. . . потихоньку. . . устаю. . ."
                            ch_s "У тебя есть. . . другие. . . предложения?"
                    elif Ch_Focus is JubesX:
                            ch_v "Слушай. . . мы можем. . . попробовать что-нибудь. . . другое?"
                    elif Ch_Focus is GwenX:
                            ch_g "Эм. . . мы можем. . . попробовать что-нибудь. . . другое?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Эм. . . мы можем. . . попробовать что-нибудь. . . другое?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Эм. . . может. . . мы могли бы. . . попробовать. . . что-нибудь другое?"
                    elif Ch_Focus is WandaX:
                            ch_w "Послушай. . . может. . .  мы могли бы. . . попробовать. . . что-нибудь другое?"
                    menu:
                        extend ""
                        "Как насчет отсоса?" if Ch_Focus.Action and MultiAction and Player.Male:
                                $ Situation = "shift"
                                call Girl_SexAfter
                                call Girl_Blowjob
                        "Как насчет вылизать мою киску?" if Ch_Focus.Action and MultiAction and not Player.Male:
                                $ Situation = "shift"
                                call Girl_SexAfter
                                call Girl_CUN
                        "Закончить." if Player.FocusX:
                                "Вы расслабляетесь. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Girl_Sex_Cycle
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                call expression Ch_Focus.Tag + "_Sex_Reset"
                                $ Situation = "shift"
                                jump Girl_SexAfter
                        "Нет, давай за работу.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она ворчит, но продолжает."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call expression Ch_Focus.Tag + "_Sex_Reset"
                                    "Она хмурится и отстраняется."
                                    if Ch_Focus is RogueX:
                                            ch_r "С таким отношением, ты и без меня отлично справишься."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Не с таким отношением!"
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Я так не думаю."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Не с таким отношением."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Не переоценивай себя."
                                    elif Ch_Focus is StormX:
                                            ch_s "Нет, я так не думаю."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Точно не сейчас."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Хорошо, тогда мы закончили."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Что ж, тогда мы закончили."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Ну, мы так точно не договаривались!"
                                    elif Ch_Focus is WandaX:
                                            ch_w "Ладно, игры кончились!"
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_SexAfter
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

label Girl_SexAfter:
    # Modification mode
    $ play_music()
    $ play_sound()
    # -----------------

    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
            $ Player.Sprite = 0
            $ Player.Cock = "out"
            call expression Ch_Focus.Tag + "_Sex_Reset"

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.Sex += 1
    $ Ch_Focus.Action -=1
    if Player.Male:
            $ Ch_Focus.Addictionrate += 1
            if "addictive" in Player.Traits:
                $ Ch_Focus.Addictionrate += 1
    $ Ch_Focus.Statup("Inbt", 30, 2)
    $ Ch_Focus.Statup("Inbt", 70, 1)

    call Partner_Like(Ch_Focus,3,2)

    if Ch_Focus.Tag+" Sex Addict" in Achievements:
            pass

    elif Ch_Focus.Sex >= 10:
            $ Ch_Focus.SEXP += 5
            $ Achievements.append(Ch_Focus.Tag+" Sex Addict")
            if not Situation:
                $ Ch_Focus.FaceChange("smile", 1)
                if Ch_Focus is RogueX:
                        ch_r "Думаю, я подсела на это."
                elif Ch_Focus is KittyX:
                        ch_k "Я совсем не могу бросить тебя."
                elif Ch_Focus is EmmaX:
                        ch_e "Кажется, я подхожу тебе, как перчатка. . ."
                elif Ch_Focus is LauraX:
                        ch_l "Хм, похоже, это входит у нас в привычку. . ."
                elif Ch_Focus is JeanX:
                        ch_j "Слушай, я только сейчас поняла, как часто мы этим занимаемся. . ."
                elif Ch_Focus is StormX:
                        ch_s "Мы очень хорошо подходим друг другу. . ."
                elif Ch_Focus is JubesX:
                        ch_v "Слушай, а у меня неплохо получается. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Наверное. . . я привыкаю к ​​тебе. . ."
                        ch_g "Чувствую себя естественно. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Должен сказать, я не понимаю, как раньше жила без этого. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я. . . я думаю, мне это очень нравится! . ."
                        ch_d "С тобой. . . по крайней мере. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Ладно, это входит у нас в привычку."
    elif Ch_Focus.Sex == 1:
                $ Ch_Focus.SEXP += 20
#            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                        if Ch_Focus is RogueX:
                                ch_r "Это было очень здорово, [RogueX.Petname], нам нужно будет как-нибудь повторить."
                        elif Ch_Focus is KittyX:
                                ch_k "Мне кажется, что я ждала уже[KittyX.like]миллион лет."
                        elif Ch_Focus is EmmaX:
                                ch_e "Полагаю, я перевернула весь твой мир."
                        elif Ch_Focus is LauraX:
                                ch_l "Могу с уверенностью сказать, что у тебя лучше меня никого не было."
                        elif Ch_Focus is JeanX:
                                ch_j "Крышесносно, а?"
                        elif Ch_Focus is StormX:
                                ch_s "Надеюсь, тебе было так же приятно, как и мне."
                        elif Ch_Focus is JubesX:
                                ch_v "Это было невероятно, [JubesX.Petname]."
                        elif Ch_Focus is GwenX:
                                ch_g "Вау, это было удивительно!"
                        elif Ch_Focus is BetsyX:
                                ch_b "Наши занятия бодрят!"
                        elif Ch_Focus is DoreenX:
                                ch_d "Ох. . . ого. . ."
                                ch_d "Это было очень здорово. . ."
                                ch_d "Спасибо. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Ого, это было просто потрясающе."
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                        $ Ch_Focus.Mouth = "sad"
                        if Ch_Focus is RogueX:
                                if not Player.Male:
                                    ch_r "Ты получила то, что тебе было нужно?"
                                else:
                                    ch_r "Ты получил то, что тебе было нужно?"
                        elif Ch_Focus is KittyX:
                                ch_k "Надеюсь, это стоило всех ожиданий."
                        elif Ch_Focus is EmmaX:
                                ch_e "Надеюсь, тебе понравилось."
                        elif Ch_Focus is LauraX:
                                if not Player.Male:
                                    ch_l "Удовлетворена?"
                                else:
                                    ch_l "Удовлетворен?"
                        elif Ch_Focus is JeanX:
                                ch_j "Крышесносно, а?"
                        elif Ch_Focus is StormX:
                                if not Player.Male:
                                    ch_s "Надеюсь, ты удовлетворена."
                                else:
                                    ch_s "Надеюсь, ты удовлетворен."
                        elif Ch_Focus is JubesX:
                                if not Player.Male:
                                    ch_v "Ты получила то, что тебе было нужно?"
                                else:
                                    ch_v "Ты получил то, что тебе было нужно?"
                        elif Ch_Focus is GwenX:
                                ch_g "Ну? Достаточно хорошо?"
                        elif Ch_Focus is BetsyX:
                                ch_b "Полагаю, этого достаточно?"
                        elif Ch_Focus is DoreenX:
                                ch_d "Ладно. . . эм. . ."
                                ch_d "Надеюсь. . ."
                                ch_d "Тебе. . . понравилось?"
                        elif Ch_Focus is WandaX:
                                ch_w "Твои потребности удовлетворены?"
    #end first time
    elif Ch_Focus.Sex == 5:
            if Ch_Focus is RogueX:
                    ch_r "Похоже, у нас это вошло в привычку."
            elif Ch_Focus is KittyX:
                    ch_k "Почему мы не сделали этого раньше?!"
            elif Ch_Focus is EmmaX:
                    ch_e "Нам действительно следовало сделать это раньше."
                    ch_e "Не могу понять, почему я так долго ждала."
            elif Ch_Focus is LauraX:
                    ch_l "Знаешь, это была хорошая идея."
            elif Ch_Focus is JeanX:
                    ch_j "У тебя неплохо получается. . ."
            elif Ch_Focus is StormX:
                    if not Player.Male:
                        ch_s "Ты довольно опытна."
                        ch_s "Я рада, что ты \"столкнулась\" со мной."
                    else:
                        ch_s "Ты довольно опытен."
                        ch_s "Я рада, что ты \"столкнулся\" со мной."
            elif Ch_Focus is JubesX:
                    if not Player.Male:
                        ch_v "Я стараюсь сделать из тебя свою лучшую любовницу."
                    else:
                        ch_v "Я стараюсь сделать из тебя своего лучшего любовника."
            elif Ch_Focus is GwenX:
                    ch_g "Я действительно начинаю привыкать к этому. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "С каждым разом мне нравится все больше и больше. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Мне. . . мне было очень весело!"
            elif Ch_Focus is WandaX:
                    if not Player.Male:
                        ch_w "Ты просто великолепна, я до сих пор не могу прийти в себя."
                    else:
                        ch_w "Ты просто великолепен, я до сих пор не могу прийти в себя."
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        if "unsatisfied" in Ch_Focus.RecentActions:
            $ Ch_Focus.FaceChange("angry")
            $ Ch_Focus.Eyes = "side"
            if Ch_Focus is RogueX:
                    ch_r "Я не получила от процесса ничего хорошего. . ."
            elif Ch_Focus is KittyX:
                    if not Player.Male:
                        ch_k "Не могла бы ты уделить мне больше внимания? . ."
                    else:
                        ch_k "Не мог бы ты уделить мне больше внимания? . ."
            elif Ch_Focus is EmmaX:
                    if not Player.Male:
                        ch_e "Не могла бы ты быть более внимательной? . ."
                    else:
                        ch_e "Не мог бы ты быть более внимательным? . ."
            elif Ch_Focus is LauraX:
                    if not Player.Male:
                        ch_l "Ничего не забыла? . ."
                    else:
                        ch_l "Ничего не забыл? . ."
            elif Ch_Focus is JeanX:
                    ch_j "Думаю, тебе нужно продолжить."
            elif Ch_Focus is StormX:
                    ch_s "Мне бы не помешало больше внимания к моим потребностям. . ."
            elif Ch_Focus is JubesX:
                    if not Player.Male:
                        ch_v "Знаешь, ты могла бы стараться и лучше. . ."
                    else:
                        ch_v "Знаешь, ты мог бы стараться и лучше. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Эй! Разве ты не собираешься \"покончить со мной?\""
            elif Ch_Focus is BetsyX:
                    ch_b "Не думаешь, что тебе нужно кое с чем закончить?"
            elif Ch_Focus is DoreenX:
                    ch_d "Так и планировалось, что я. . . эм. . . не смогу. . ."
                    ch_d "\"Кончить?\""
            elif Ch_Focus is WandaX:
                    ch_w "Послушай, мне бы не помешало больше внимания."

    $ Tempmod = 0
#    if Situation == "shift":
#        ch_d "Did you[Ch_Focus.like]want to try something else?"
    call Checkout
    return

# End Girl sex //////////////////////////////////////////////////////////////////////////////////


# Girl anal //////////////////////////////////////////////////////////////////////

label Girl_Sex_A: #rkeljsvg
##    #fix remove
#    if Ch_Focus is WandaX:
#        "Not currently available."
#        return
##    #fix remove
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Ch_Focus)
    if Ch_Focus.Anal >= 7: # She loves it
        $ Tempmod += 20
    elif Ch_Focus.Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif Ch_Focus.Anal: #You've done it before
        $ Tempmod += 15
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 10

    if not Player.Male:
        $ Tempmod += 5
    elif Ch_Focus.Addict >= 75 and (Ch_Focus.CreamP + Ch_Focus.CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif Ch_Focus.Addict >= 75:
        $ Tempmod += 15

    if Ch_Focus.Lust > 85:
        $ Tempmod += 10
    elif Ch_Focus.Lust > 75: #She's really horny
        $ Tempmod += 5

    $ Tempmod += 10  # she starts out loose

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
    if "no anal" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no anal" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if Situation == "auto":
            if not Player.Male and "strapon" not in Player.RecentActions:
                    "Вы достаете свой резиновый член."
                    $ Player.AddWord(1,"strapon",0,0,0) #Recent
            if renpy.showing(Ch_Focus.Tag+"_SexSprite") or renpy.showing(Ch_Focus.Tag+"_Doggy_Animation"):
                    pass
            else:
                    call expression Ch_Focus.Tag + "_Sex_Launch" pass ("anal")
                    if Ch_Focus.PantsNum() == 5:
                        "Вы прижимаетесь к [Ch_Focus.Name_dat], в процессе задирая ее юбку."
                    elif Ch_Focus.PantsNum() >= 6:
                        "Вы прижимаетесь к [Ch_Focus.Name_dat], в процессе стягивая ее штаны."
                    else:
                        "Вы прижимаетесь к [Ch_Focus.Name_dat]."
                    $ Ch_Focus.SeenPanties = 1
            $ Ch_Focus.Upskirt = 1
            $ Ch_Focus.PantiesDown = 1
            if not Player.Male:
                "Вы начинаете водить кончиком резинового члена о ее тугой анус."
            else:
                "Вы начинаете водить кончиком своего члена о ее тугой анус."
            $ Ch_Focus.FaceChange("surprised", 1)
            call Girl_First_Bottomless(Ch_Focus,1)

            if "anal" in Ch_Focus.RecentActions:
                    jump Girl_AnalPrep

            if (Ch_Focus.Anal and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it
                    $ Ch_Focus.Statup("Obed", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 3)
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    "[Ch_Focus.Name] вздрагивает, а затем расплывается в улыбке."
                    if Ch_Focus is RogueX:
                            ch_r "Хмм, вставляй. . ."
                    elif Ch_Focus is KittyX:
                        if KittyX.Loose:
                            ch_k "Хмм, вставляй его. . ."
                        else:
                            ch_k "Лаааадно. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Ооох, шалунишка. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Ага, ладно. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Ох! Конечно. . ."
                    elif Ch_Focus is StormX:
                            ch_s "[StormX.Petname], я тебе удивляюсь. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Меня это устраивает, [JubesX.Petname]."
                    elif Ch_Focus is GwenX:
                            ch_g "Ооох. . . да, [GwenX.Petname]."
                    elif Ch_Focus is BetsyX:
                            ch_b "Ооох, вставляй скорее. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ооо. . . ладно, [Ch_Focus.Petname]."
                    elif Ch_Focus is WandaX:
                            ch_w "Ну ладно, [WandaX.Petname]."
                    jump Girl_AnalPrep
            else:
                #she's questioning it
                $ Ch_Focus.Brows = "angry"
                if Ch_Focus is RogueX:
                        ch_r "Эй, что ты там делаешь?!"
                elif Ch_Focus is KittyX:
                        ch_k "Эм[KittyX.like]что ты делаешь?!"
                elif Ch_Focus is EmmaX:
                        ch_e "Ох? Что ты там делаешь?"
                elif Ch_Focus is LauraX:
                        ch_l "А? Хочешь ворваться через \"заднюю\" дверь?"
                elif Ch_Focus is JeanX:
                        ch_j "Ну и зачем так прилипать ко мне?"
                elif Ch_Focus is StormX:
                        ch_s "Прошу прощения, к чему все идет?"
                elif Ch_Focus is JubesX:
                        ch_v "Ох! Не та дверь. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Помогите! Враг у задних врат!"
                        ch_g "Подкрадываешься ко мне?"
                elif Ch_Focus is BetsyX:
                        ch_b "Что ты такое делаешь?"
                elif Ch_Focus is DoreenX:
                        ch_d "Ой!"
                        ch_d "Что- эм. . . что ты делаешь?"
                elif Ch_Focus is WandaX:
                        ch_w "Воу, хочешь вставить в попку?"
                menu:
                    extend ""
                    "Извини-извини! Я уже ничего не делаю.":
                            if Approval:
                                $ LauraX.FaceChange("sexy", 1)
                                $ Ch_Focus.Statup("Obed", 70, 3)
                                $ Ch_Focus.Statup("Inbt", 50, 3)
                                $ Ch_Focus.Statup("Inbt", 70, 1)
                                if Ch_Focus is RogueX:
                                        ch_r "Думаю, я не против, если ты действительно этого хочешь. . ."
                                elif Ch_Focus is KittyX:
                                        ch_k "Ну[KittyX.like]только не торопись, ладно? . ."
                                elif Ch_Focus is EmmaX:
                                        ch_e "Что ж, пока ты знаешь, что делаешь. . ."
                                        ch_e "Я не буду против. . ."
                                elif Ch_Focus is LauraX:
                                        ch_l "Слушай, давай только полегче. . ."
                                        ch_l ". . . с моей попкой."
                                elif Ch_Focus is JeanX:
                                        ch_j "Ладно, тебе повезло. . ."
                                        ch_j "Я позволю тебе вставить его."
                                elif Ch_Focus is StormX:
                                        ch_s "Ох, очень жаль. . ."
                                        ch_s "Я ведь не сказала, что против. . ."
                                elif Ch_Focus is JubesX:
                                        $ Ch_Focus.FaceChange("sadside", 2,Mouth="smile")
                                        ch_v "Нууу. . ."
                                        $ JubesX.FaceChange("sexy", 1)
                                        ch_v "Я думаю, ничего страшного."
                                elif Ch_Focus is GwenX:
                                        $ Ch_Focus.FaceChange("sadside", 2,Mouth="smile")
                                        ch_g ". . ."
                                        $ GwenX.FaceChange("sexy", 1)
                                        if not Player.Male:
                                            ch_g "Врата открыты, миледи. . ."
                                        else:
                                            ch_g "Врата открыты, милорд. . ."
                                elif Ch_Focus is BetsyX:
                                        $ Ch_Focus.FaceChange("sadside", 2,Mouth="smile")
                                        ch_b ". . ."
                                        $ BetsyX.FaceChange("sexy", 1)
                                        if not Player.Male:
                                            ch_b "Пожалуй, ты можешь продолжить, просто сперва ты застала меня врасплох. . ."
                                        else:
                                            ch_b "Пожалуй, ты можешь продолжить, просто сперва ты застал меня врасплох. . ."
                                elif Ch_Focus is DoreenX:
                                        $ Ch_Focus.FaceChange("sadside", 2,Mouth="smile")
                                        ch_d ". . ."
                                        $ Ch_Focus.FaceChange("sexy", 1)
                                        ch_d "Я думаю, мы можем попробовать. . ."
                                elif Ch_Focus is WandaX:
                                        $ Ch_Focus.FaceChange("sexy", 1)
                                        ch_w "Послушай, мне нравятся твои действия, не отступай."
                                jump Girl_AnalPrep
                            #end if approved
                            "Вы отстраняетесь, прежде чем успеваете войти внутрь."
                            $ Ch_Focus.FaceChange("bemused", 1)
                            if Ch_Focus is RogueX:
                                    if RogueX.Anal:
                                        ch_r "Ну ладно, [RogueX.Petname], никто не пострадал, только в будущем предупреждай."
                                    else:
                                        ch_r "Ну ладно, [RogueX.Petname], я еще не совсем готов к этому, но, может быть, если ты в следующий раз вежливо попросишь . . ."
                            elif Ch_Focus is KittyX:
                                    if KittyX.Anal:
                                        ch_k "Может, стоило сначала[KittyX.like]предупредить меня?"
                                    else:
                                        ch_k "Может, стоило сначала[KittyX.like]предупредить меня? Я не думаю, что[KittyX.like]готова к таким вещам. . ."
                            elif Ch_Focus is EmmaX:
                                    if EmmaX.Anal:
                                        if not Player.Male:
                                            ch_e "Я была бы признательна, если бы ты соизволила предупредить. . ."
                                        else:
                                            ch_e "Я была бы признательна, если бы ты соизволил предупредить. . ."
                                    else:
                                        ch_e "Возможно, мы могли бы поработать над этим. . ."
                            elif Ch_Focus is LauraX:
                                    if LauraX.Anal:
                                        ch_l "Тебе стоило сперва предупредить меня. . ."
                                    else:
                                        ch_l "Слушай, все, чего я прошу, так это небольшого предупреждение. . ."
                            elif Ch_Focus is JeanX:
                                            ch_j "Эй, тебе следовало предупредить меня. . ."
                            elif Ch_Focus is StormX:
                                    if StormX.Anal:
                                        ch_s "Я была бы благодарна за предупреждение. . ."
                                    else:
                                        ch_s "Возможно, мы могли бы над этим поработать. . ."
                            elif Ch_Focus is JubesX:
                                    if JubesX.Anal:
                                        ch_v "Небольшого предупреждения не помешало бы. . ."
                                    else:
                                        ch_v "Просто, эм. . . предупреждай. . ."
                            elif Ch_Focus is GwenX:
                                    if GwenX.Anal:
                                            ch_g "Ты можешь сначала спрашивать, [GwenX.Petname]?"
                                    else:
                                            ch_g "Сначала стоит спрашивать. . ."
                            elif Ch_Focus is BetsyX:
                                    if BetsyX.Anal:
                                            ch_b "Тебе не кажется, что стоило сперва предупредить, [BetsyX.Petname]?"
                                    else:
                                            if not Player.Male:
                                                ch_b "Было бы неплохо, если бы ты сначала предупредила. . ."
                                            else:
                                                ch_b "Было бы неплохо, если бы ты сначала предупредил. . ."
                            elif Ch_Focus is DoreenX:
                                    if Ch_Focus.Anal:
                                            ch_d "Всегда стоит сперва спросить, [DoreenX.Petname]."
                                    else:
                                            ch_d "Всегда стоит сперва спрашивать. . ."
                            elif Ch_Focus is WandaX:
                                            ch_w "Сперва следовало меня предупредить."
                    #end "Извини-извини! Я уже ничего не делаю.":
                    "Просто начать трахать.":
                            $ Ch_Focus.Statup("Love", 80, -10, 1)
                            $ Ch_Focus.Statup("Love", 200, -8)
                            "Вы начинаете входить в нее."
                            $ Ch_Focus.Statup("Obed", 70, 3)
                            $ Ch_Focus.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(Ch_Focus, 700, "O", TabM=1):
                                    $ Ch_Focus.FaceChange("angry")
                                    "[Ch_Focus.Name] отталкивает вас."
                                    if Ch_Focus is RogueX:
                                            if not Player.Male:
                                                ch_r "Манда!"
                                            else:
                                                ch_r "Мудак!"
                                            ch_r "Если ты хочешь так со мной обращаться, то мы закончили!"
                                    elif Ch_Focus is KittyX:
                                            if not Player.Male:
                                                ch_k "Манда!"
                                            else:
                                                ch_k "Мудак!"
                                            ch_k "Тебе нельзя было этого делать!"
                                    elif Ch_Focus is EmmaX:
                                            if not Player.Male:
                                                ch_e "Нахалка!"
                                            else:
                                                ch_e "Нахал!"
                                            ch_e "Сначала следует спрашивать."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Умерь свой пыл."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Тц-тц."
                                    elif Ch_Focus is StormX:
                                            ch_s "Очень жаль."
                                            ch_s "Боюсь, этого не произойдет."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Я так не думаю."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Там тебя не ждут!"
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Ну и ну!"
                                            ch_b "Боюсь, ты переходишь все границы."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Туда нельзя!"
                                    elif Ch_Focus is WandaX:
                                            ch_w "Хорошая попытка, но тебе следовало сперва вежливо спросить."
                                    $ Ch_Focus.Statup("Love", 50, -10, 1)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ renpy.pop_call()
                                    if Situation:
                                        $ renpy.pop_call()
                                    call expression Ch_Focus.Tag + "_Sex_Reset"
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                            else:
                                    $ Ch_Focus.FaceChange("sad")
                                    "Похоже [Ch_Focus.Name_dat] это не нравится, вам повезло, что она такая послушная."
                                    jump Girl_AnalPrep
                    #end "Just fucking.":
            return
    #end "auto"


    if not Ch_Focus.Anal and "no anal" not in Ch_Focus.RecentActions:
            #first time
            $ Ch_Focus.FaceChange("surprised", 1)
            $ Ch_Focus.Mouth = "kiss"
            if Ch_Focus is RogueX:
                    ch_r "Подожди, ты хочешь вставить его мне в попку?!"
            elif Ch_Focus is KittyX:
                    ch_k "Ты хочешь открыть \"ту\" дверь?!"
            elif Ch_Focus is EmmaX:
                    ch_e "Ооох, шалунишка. Анал?"
            elif Ch_Focus is LauraX:
                    ch_l "Хм, анал?"
            elif Ch_Focus is JeanX:
                    ch_j "О, так тебя привлекает анал?"
            elif Ch_Focus is StormX:
                    ch_s "Я в шоке! Анал?"
            elif Ch_Focus is JubesX:
                    ch_v "Ох. . . ты хочешь заняться аналом?"
            elif Ch_Focus is GwenX:
                    ch_g "Ох. . . эм. . . анал?"
            elif Ch_Focus is BetsyX:
                    ch_b "Ох. . . ясно. . . анал?"
            elif Ch_Focus is DoreenX:
                    ch_d "Эм. . . ты хочешь. . ."
                    ch_d ". . . в попку?"
            elif Ch_Focus is WandaX:
                    ch_w "Ого, анал? Ладно. . ."
            if not Player.Male:
                if Ch_Focus is RogueX:
                        ch_r "Я чего-то о тебе не знаю?"
                elif Ch_Focus is KittyX:
                        ch_k "Как ты[KittyX.like]собираешься. . .?"
        #        elif Ch_Focus is EmmaX:
        #                pass
                elif Ch_Focus is LauraX:
                        ch_l "Мне кажется, у тебя кое-чего нет. . ."
                elif Ch_Focus is JeanX:
                        cch_j "Я не вижу у тебя члена."
        #        elif Ch_Focus is StormX:
        #                pass
                elif Ch_Focus is JubesX:
                        ch_v "И как именно ты собираешься это сделать?"
                elif Ch_Focus is GwenX:
                        ch_g "Как ты. . . собираешься это сделать? . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Но как нам это. . . сделать? . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Как ты. . . это сделаешь? . ."
                elif Ch_Focus is WandaX:
                        ch_w "У тебя с собой игрушки, я права?"
                menu:
                    extend ""
                    "Я подготовилась. . .":
                            pass
                    "Скоро ты поймешь. . .":
                            $ Ch_Focus.Statup("Obed", 90, 3)
                            $ Tempmod -= 5

            if Ch_Focus.Forced:
                $ Ch_Focus.FaceChange("sad")
                if Ch_Focus is RogueX:
                        ch_r "Серьезно?"
                elif Ch_Focus is KittyX:
                        ch_k "Анал? Серьезно?"
                elif Ch_Focus is EmmaX:
                        ch_e "Анал? Таков твой выбор?"
                elif Ch_Focus is LauraX:
                        ch_l "Анал? Так вот чего ты хочешь?"
                elif Ch_Focus is JeanX:
                        ch_j "Ты собираешься разыграть именно эту карту?"
                elif Ch_Focus is StormX:
                        ch_s "Ох. И, конечно, это должен быть анал."
                elif Ch_Focus is JubesX:
                        ch_v "Ох. . . значит анал, да?"
                elif Ch_Focus is GwenX:
                        ch_g "Думаю, это будет следующим шагом. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Не сомневаюсь, что тебе понравится. . ."
                elif Ch_Focus is DoreenX:
                        ch_d ". . . Кажется, я поняла. . ."
                        if not Ch_Focus.Sex:
                                ch_d "Тебе захотелось перепрыгнуть через один этап. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Почему-то я не смогла это предвидеть. . ."

    if "anal" in Ch_Focus.DailyActions:
        if not Ch_Focus.Loose and ("dildo anal" in Ch_Focus.DailyActions or "anal" in Ch_Focus.DailyActions):
                $ Ch_Focus.FaceChange("perplexed", 1)
                if Ch_Focus is RogueX:
                        ch_r "Она все еще немного побаливает после прошлого раза."
                elif Ch_Focus is KittyX:
                        ch_k "Я еще не отошла от прошлого раза, но. . ."
                else:
                        call AnyLine(Ch_Focus,"Ох. . .")
        elif Approval:
            $ Ch_Focus.FaceChange("sexy", 1)
            if Ch_Focus is RogueX:
                    ch_r "Хочешь повторить? Ладно."
            elif Ch_Focus is KittyX:
                    ch_k "Снова?"
            elif Ch_Focus is EmmaX:
                    ch_e "Хорошо. . ."
            elif Ch_Focus is LauraX:
                    ch_l "Конечно, я позволю тебе вставить его."
            elif Ch_Focus is JeanX:
                    ch_j "Конечно."
            elif Ch_Focus is StormX:
                    ch_s "Конечно. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Ага, ладно."
            elif Ch_Focus is GwenX:
                    ch_g "Ладно, Гвен, тебе нужно открыться. . ."
            elif Ch_Focus is BetsyX:
                    ch_b "Пожалуй, мы можем сделать еще один заход. . ."
            elif Ch_Focus is DoreenX:
                    ch_d "Хорошо!"
            elif Ch_Focus is WandaX:
                    ch_w "Снова?"
            jump Girl_AnalPrep
    #end already did it today

    if not Ch_Focus.Anal and Approval:
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
                            ch_r "Думаю, я не против, если ты действительно этого хочешь. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Наверное, можно? . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Мне было интересно, когда же ты спросишь. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Я надеялась, что ты спросишь. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Я ожидала этого. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Я надеялась, что ты спросишь. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Ох, как пикантно. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Думаю, это может быть весело. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Пожалуй, это может быть весело. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я. . . наверное, это может быть весело. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Я вроде как давно хотела этим заняться."
            elif Ch_Focus.Obed >= Ch_Focus.Inbt:
                    $ Ch_Focus.FaceChange("normal")
                    if Ch_Focus in (EmmaX,StormX,BetsyX):
                            call AnyLine(Ch_Focus,"Если это то, чего ты хочешь, "+Ch_Focus.Petname+". . .")
                    else:
                            call AnyLine(Ch_Focus,"Если ты так этого хочешь, "+Ch_Focus.Petname+". . .")
            else: # Uninhibited
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Mouth = "smile"
                    if Ch_Focus is RogueX:
                            ch_r "Ммм, я всегда хотела попробовать. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Не могу сказать, что это не приходило мне в голову. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Я надеялась, что ты спросишь. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Я надеялась, что ты спросишь. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "А я все думала, когда же это произойдет. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Я надеялась, что ты спросишь. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Я надеялась, что ты спросишь. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Мне интересно, почему ты так долго. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Мне даже немного интересно, почему ты предлагаешь так поздно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Мне немного любопытно, каково это. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Я надеялась, что однажды до этого дойдет. . ."

    elif Approval:
            #Second time+ dialog
            if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -3, 1)
                    $ Ch_Focus.Statup("Love", 20, -2, 1)
                    if Ch_Focus is RogueX:
                            ch_r "Ты правда этого хочешь?"
                    elif Ch_Focus is KittyX:
                            ch_k "Ты просишь слишком многого. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Снова? Похоже, ты хочешь меня совсем загонять."
                    elif Ch_Focus is LauraX:
                            ch_l "Надеюсь, я тебя не измотаю."
                    elif Ch_Focus is JeanX:
                            if not Player.Male:
                                ch_j "А ты, я смотрю, оптимистка. . ."
                            else:
                                ch_j "А ты, я смотрю, оптимист. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Ох, снова?"
                    elif Ch_Focus is JubesX:
                            ch_v "Что ж. . . не привыкай к этому."
                    elif Ch_Focus is GwenX:
                            ch_g "Наверно, можно. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "В процессе мне лишь нужно думать об Англии. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я. . . если это так необходимо. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Хорошо, если так нужно. . ."
            elif not Taboo and "tabno" in Ch_Focus.DailyActions:
                    call Sex_Basic_Dialog(Ch_Focus,"tabyes") #"This -would- be a better place for it. . ."
            elif "anal" in Ch_Focus.DailyActions and not Ch_Focus.Loose:
                pass
            elif "anal" in Ch_Focus.RecentActions:
                    if Ch_Focus is RogueX:
                            ch_r "Думаю, я уже разогрелась. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Наверное, я уже разогрелась. . ."
                    elif Ch_Focus is EmmaX:
                            if not Player.Male:
                                ch_e "Снова? [EmmaX.Petname], Ты такая ненасытная!"
                            else:
                                ch_e "Снова? [EmmaX.Petname], Ты такой ненасытный!"
                    elif Ch_Focus is LauraX:
                            ch_l "Снова? Ну, пеняй на себя."
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно, [JeanX.Petname]. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Я как следует размялась. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Снова? Хм. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Думаю, я уже расслабилась. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Пожалуй, я уже достаточно разогрета. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ну, теперь я точно готова. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Снова? Ого. . ."
                    jump Girl_AnalPrep
            elif "anal" in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    if Ch_Focus in (EmmaX,StormX,BetsyX):
                        $ Line = renpy.random.choice(["Снова?",
                            "Хочешь еще раз?",
                            "Должно быть, я талантливее, чем я думала.",
                            "Тебе все еще мало?",
                            "Снова? Что ж, я не должна от тебя отставать. . ." ])
                    else:
                        $ Line = renpy.random.choice(["Желаешь добавки?",
                            "Желаешь еще разок?",
                            "Наверное, я лучше, чем я думала.",
                            "Тебе все еще мало?",
                            Ch_Focus.Petname + " ты меня совсем загоняешь."])
                    call AnyLine(Ch_Focus,Line)
            else:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    if Ch_Focus in (EmmaX,StormX,BetsyX):
                        $ Line = renpy.random.choice(["Я просто слишком неотразима?",
                            "Хочешь еще заход?",
                            "Должно быть, я талантливее, чем я думала.",
                            "Подалуй, ты знаешь, чего хочешь.",
                            "Хочешь взять меня?"])
                    else:
                        $ Line = renpy.random.choice(["Хочешь меня?",
                            "Желаешь еще заход?",
                            "Должно быть, я лучше, чем я думала.",
                            "Я думаю, ты знаешь, что делаешь.",
                            "Ты хочешь. . . сделать это?"])
                    call AnyLine(Ch_Focus,Line)
            $ Line = 0
    #end First time dialog

    if Approval >= 2:
            #She's into it. . .
            if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 1)
                    if Ch_Focus is RogueX:
                            ch_r "Хорошо."
                    elif Ch_Focus is KittyX:
                            ch_k "Ладно."
                    elif Ch_Focus is EmmaX:
                            ch_e "Я смотрю, у тебя нет тормозов. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Как скажешь."
                    elif Ch_Focus is JeanX:
                            ch_j "Как скажешь."
                    elif Ch_Focus is StormX:
                            ch_s "Ох. хорошо."
                    elif Ch_Focus is JubesX:
                            ch_v "Как пожелаешь."
                    elif Ch_Focus is GwenX:
                            ch_g "Ладно, Гвен, тебе нужно открыться. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "В процессе мне лишь нужно думать об Англии. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ладно, расслабься, Дорин. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Ладно."
            else:
                $ Ch_Focus.FaceChange("sexy", 1)
                $ Ch_Focus.Statup("Love", 90, 1)
                $ Ch_Focus.Statup("Inbt", 50, 3)
                $ Line = renpy.random.choice(["Ну. . . ладно.",
                    "Конечно.",
                    "Пожалуй, можно.",
                    "Эм, ага.",
                    "Хех, ладно, ладно."])
                call AnyLine(Ch_Focus,Line)
                $ Line = 0
            $ Ch_Focus.Statup("Obed", 20, 1)
            $ Ch_Focus.Statup("Obed", 60, 1)
            $ Ch_Focus.Statup("Inbt", 70, 2)
            jump Girl_AnalPrep

    else:
            #She's not into it, but maybe. . .
            $ Ch_Focus.FaceChange("angry")
            if "no anal" in Ch_Focus.DailyActions:
                    call Sex_Basic_Dialog(Ch_Focus,"norecent")
            elif Taboo and "tabno" in Ch_Focus.DailyActions:
                    call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
            elif not Ch_Focus.Anal:
                    $ Ch_Focus.FaceChange("bemused")
                    if Ch_Focus is RogueX:
                            ch_r "Мне это как-то не нравится, [RogueX.Petname]. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Не уверена, что я. . . из таких[KittyX.like]девушек?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Я очень сомневаюсь, что ты понимаешь, во что ввязываешься. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Ох, ты и понятия не имеешь, что тебя ждет. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Ох, это могло бы быть интересно, но. . ."
                    elif Ch_Focus is StormX:
                            if not Player.Male:
                                ch_s "Я не уверена, готова ли ты уже к этому."
                            else:
                                ch_s "Я не уверена, готов ли ты уже к этому."
                    elif Ch_Focus is JubesX:
                            ch_v "Я совсем не готова к этому. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Я не готова к этому. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Почему-то я ожидала такого от тебя, но. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я не уверена. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Пожалуй, я знала, что это однажды произойдет. . ."
            elif not Ch_Focus.Loose and "anal" not in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("perplexed")
                    if Ch_Focus is RogueX:
                            ch_r "В прошлый раз тебе следовало быть немного нежнее, [RogueX.Petname]. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "В прошлый раз все прошло как-то. . . грубо?"
                    else:
                            call AnyLine(Ch_Focus,"По крайней мере, на этот раз будь осторожнее.")
            else:
                $ Ch_Focus.FaceChange("bemused")
                if Ch_Focus is RogueX:
                        ch_r "Не сейчас, [RogueX.Petname]. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Может[KittyX.like]не сейчас? . ."
                elif Ch_Focus is EmmaX:
                        ch_e "Возможно, лучше в другой раз? . ."
                elif Ch_Focus is LauraX:
                        ch_l "Может быть позже? . ."
                elif Ch_Focus is JeanX:
                        ch_j "Я сейчас не в настроении. . ."
                elif Ch_Focus is StormX:
                        ch_s "Возможно, в другой раз? . ."
                elif Ch_Focus is JubesX:
                        ch_v "Может, быть позже? . ."
                elif Ch_Focus is GwenX:
                        ch_g "Я не уверена, может, не сейчас? . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Я сомневаюсь, возможно, позже? . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я, эм. . . я пока не готова. . ."
                elif Ch_Focus is WandaX:
                        ch_w "Я не уверена, что хочу этого сейчас. . ."
            menu:
                extend ""
                "Извини, забудь." if "no anal" in Ch_Focus.DailyActions:
                        $ Ch_Focus.FaceChange("bemused")
                        if Ch_Focus is EmmaX:
                                ch_e "Я не виню тебя за твой. . . задор."
                        elif Ch_Focus is JeanX:
                                ch_j "Ясно."
                        elif Ch_Focus is StormX:
                                ch_s "Я не могу винить тебя за твое. . . желание."
                        elif Ch_Focus is JubesX:
                                ch_v "Похоже, тебе это очень нравится. . ."
                        elif Ch_Focus is GwenX:
                                ch_g "Это звучит. . . интересно. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Это звучит. . . интересно. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "Мне просто нужно немного времени, чтобы все обдумать. . ."
                        else:
                                call Sex_Basic_Dialog(Ch_Focus,"noproblem")  # ch_d "Aw, don't worry about it. . ."
                        return
                "Может, в другой раз?" if "no anal" not in Ch_Focus.DailyActions:
                        $ Ch_Focus.FaceChange("sexy")
                        if Ch_Focus is RogueX:
                                ch_r "Я подумаю, [RogueX.Petname]."
                        elif Ch_Focus is KittyX:
                                ch_k "Может быть, невозможно знать все наперед."
                        elif Ch_Focus is EmmaX:
                                ch_e "Полагаю, мы будем заниматься подобным. . ."
                                ch_e ". . . и часто."
                        elif Ch_Focus is LauraX:
                                ch_l "Ох, возможно. . ."
                                ch_l ". . . и часто."
                        elif Ch_Focus is JeanX:
                                ch_j "Ох, возможно. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Полагаю, наступит момент, когда мы будем заниматься этим. . ."
                                ch_s ". . . регулярно."
                        elif Ch_Focus is JubesX:
                                ch_v "Эм. . ."
                                ch_v ". . . может быть."
                        elif Ch_Focus is GwenX:
                                ch_g "Я не-"
                                ch_g ". . . то есть, возможно?"
                        elif Ch_Focus is BetsyX:
                                ch_b "Я не-"
                                ch_b ". . . Пожалуй, я не могу исключать такого исхода. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "Я не-"
                                ch_d ". . . может быть?"
                        elif Ch_Focus is WandaX:
                                ch_w "Конечно, все может быть."
                        $ Ch_Focus.Statup("Love", 80, 2)
                        $ Ch_Focus.Statup("Inbt", 70, 2)
                        if Taboo:
                            $ Ch_Focus.RecentActions.append("tabno")
                            $ Ch_Focus.DailyActions.append("tabno")
                        $ Ch_Focus.RecentActions.append("no anal")
                        $ Ch_Focus.DailyActions.append("no anal")
                        return
                "Тебе может понравится. . .":
                        if Approval:
                            $ Ch_Focus.FaceChange("sexy")
                            $ Ch_Focus.Statup("Obed", 90, 2)
                            $ Ch_Focus.Statup("Obed", 50, 2)
                            $ Ch_Focus.Statup("Inbt", 70, 3)
                            $ Ch_Focus.Statup("Inbt", 40, 2)
                            $ Line = renpy.random.choice(["Ага, возможно. . .",
                                    "Пожалуй. . .",
                                    "Хорошее замечание. . ."])
                            call AnyLine(Ch_Focus,Line)
                            $ Line = 0
                            jump Girl_AnalPrep
#                        else:
#                            pass

                "Просто смирись.":
                        # Pressured into it
                        $ Approval = ApprovalCheck(Ch_Focus, 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                        if Approval > 1 or (Approval and Ch_Focus.Forced):
                            $ Ch_Focus.FaceChange("sad")
                            $ Ch_Focus.Statup("Love", 70, -5, 1)
                            $ Ch_Focus.Statup("Love", 200, -5)
                            if Ch_Focus is RogueX:
                                    ch_r "Ладно. Давай уже побыстрее закончим."
                            elif Ch_Focus is KittyX:
                                    ch_k "Хорошо! . .  ладно, вставляй его."
                            elif Ch_Focus is EmmaX:
                                    ch_e "Хорошо, если ты заткнешься."
                            elif Ch_Focus is LauraX:
                                    ch_l "Хорошо, если ты заткнешься."
                            elif Ch_Focus is JeanX:
                                    ch_j ". . ."
                                    ch_j ". . . ладно. . ."
                            elif Ch_Focus is StormX:
                                    ch_s "Ладно, только замолчи."
                            elif Ch_Focus is JubesX:
                                    ch_v ". . . похоже, мне придется. . ."
                            elif Ch_Focus is GwenX:
                                    ch_g "О, пожалуй, мне придется."
                            elif Ch_Focus is BetsyX:
                                    ch_b "Ох, если это так необходимо. . ."
                            elif Ch_Focus is DoreenX:
                                    ch_d "\"Смириться.\" . . Ну ладно. . . "
                                    ch_d "Ладно. . ."
                            elif Ch_Focus is WandaX:
                                    ch_w ". . . ладно."
                            $ Ch_Focus.Statup("Obed", 80, 4)
                            $ Ch_Focus.Statup("Inbt", 80, 1)
                            $ Ch_Focus.Statup("Inbt", 60, 3)
                            $ Ch_Focus.Forced = 1
                            jump Girl_AnalPrep
                        else:
                            $ Ch_Focus.Statup("Love", 200, -20)
                            $ Ch_Focus.RecentActions.append("angry")
                            $ Ch_Focus.DailyActions.append("angry")

    #She refused all offers.
    $ Ch_Focus.ArmPose = 1
    if "no anal" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"noday") #"Stop asking."
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
    elif Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("angry", 1)
            if Ch_Focus is RogueX:
                    ch_r "Это слишком, даже для тебя."
            elif Ch_Focus is KittyX:
                    ch_k "Это слишком, даже для тебя."
            elif Ch_Focus is EmmaX:
                    ch_e "Осторожней с тем, что говоришь."
            elif Ch_Focus is LauraX:
                    ch_l "Ты заходишь слишком далеко."
            elif Ch_Focus is JeanX:
                    ch_j "Ты переоцениваешь свое влияние."
            elif Ch_Focus is StormX:
                    ch_s "Ты, определенно, цепляешься за каждую возможность."
            elif Ch_Focus is JubesX:
                    if not Player.Male:
                        ch_v "Ты слишком настойчива."
                    else:
                        ch_v "Ты слишком настойчив."
            elif Ch_Focus is GwenX:
                    ch_g "Это. . . слишком."
            elif Ch_Focus is BetsyX:
                    ch_b "Я не могу."
            elif Ch_Focus is DoreenX:
                    ch_d "Это. . . уже слишком."
            elif Ch_Focus is WandaX:
                    ch_w "Это слишком, серьезно. . ."
            $ Ch_Focus.Statup("Lust", 200, 5)
            if Ch_Focus.Love > 300:
                    $ Ch_Focus.Statup("Love", 70, -2)
            $ Ch_Focus.Statup("Obed", 50, -2)
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
    elif Taboo:
            # she refuses and this is too public a place for her
            $ Ch_Focus.FaceChange("angry", 1)
            $ Ch_Focus.RecentActions.append("tabno")
            $ Ch_Focus.DailyActions.append("tabno")
            call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You picked a bad place for this. . ."
            $ Ch_Focus.Statup("Lust", 200, 5)
            $ Ch_Focus.Statup("Obed", 50, -3)
    elif Ch_Focus.Anal:
            $ Ch_Focus.FaceChange("sad")
            if Ch_Focus is RogueX:
                    ch_r "Единственное что ты можешь сделать с моей задницей - это поцеловать ее, [RogueX.Petname]."
                    ch_r ". . .О другом даже не смей мечтать."
            elif Ch_Focus is KittyX:
                    ch_k "Это[KittyX.like]даже не обсуждается."
            elif Ch_Focus is EmmaX:
                    ch_e "Тебе придется еще раз доказать мне, что ты этого заслуживаешь."
            elif Ch_Focus is LauraX:
                    ch_l "Тебе придется это заслужить."
            elif Ch_Focus is JeanX:
                    ch_j "Ты придется это заслужить. . ."
            elif Ch_Focus is StormX:
                    ch_s "Тебе придется еще раз показать мне свою ценность."
            elif Ch_Focus is JubesX:
                    ch_v "Может быть, в другой раз."
            elif Ch_Focus is GwenX:
                    ch_g "Я пас."
            elif Ch_Focus is BetsyX:
                    ch_b "Боюсь, что эта \"дверь\" закрыта для тебя."
            elif Ch_Focus is DoreenX:
                    ch_d "Нет, я не могу."
            elif Ch_Focus is WandaX:
                    ch_w "Нет."
    else:
            $ Ch_Focus.FaceChange("normal", 1)
            if Ch_Focus is RogueX:
                    ch_r "Этого не произойдет."
            elif Ch_Focus is KittyX:
                    ch_k "Неееее-а."
            elif Ch_Focus is EmmaX:
                    ch_e "Боюсь, что нет."
            elif Ch_Focus is LauraX:
                    if not Player.Male:
                        ch_l "Ты еще не заслужила этого."
                    else:
                        ch_l "Ты еще не заслужил этого."
            elif Ch_Focus is JeanX:
                    if not Player.Male:
                        ch_j "Ты еще не заслужила этого."
                    else:
                        ch_j "Ты еще не заслужил этого."
            elif Ch_Focus is StormX:
                    if not Player.Male:
                        ch_s "Я не думаю, что ты уже это заслужила."
                    else:
                        ch_s "Я не думаю, что ты уже это заслужил."
            elif Ch_Focus is JubesX:
                    ch_v "Мне нужно еще немного времени. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Я. . . эм. . . должна подумать об этом."
            elif Ch_Focus is BetsyX:
                    ch_b "Я. . . подумаю над этим."
            elif Ch_Focus is DoreenX:
                    ch_d "Это. . . очень интимное дело, так что. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Нет."
    $ Ch_Focus.RecentActions.append("no anal")
    $ Ch_Focus.DailyActions.append("no anal")
    $ Tempmod = 0
    return

label Girl_AnalPrep:  #rkeljsvg
    # Modification mode
    if is_playing_music(audio.girl_sex):
        $ play_music(name=audio.girl_sex, loop=True)
    # -----------------

##    #fix remove
#    if Ch_Focus is WandaX:
#        "Not currently available."
#        return
##    #fix remove
    call Seen_First_Peen(Ch_Focus,Partner,React=Situation)
    call expression Ch_Focus.Tag + "_Sex_Launch" pass ("hotdog")

    if Ch_Focus.Plug:
            "Сначала вы убираете ее анальную пробку. . ."
            call Remove_Anal_Plug(Ch_Focus)
    if Situation == Ch_Focus:
            #Girl auto-starts
            $ Situation = 0
            call Girl_PantsOff(Ch_Focus)   #"Girl rolls back and pulls you toward her, sliding her pants down as she does so."
            $ Line = 0
            $ Ch_Focus.SeenPanties = 1
            $ Ch_Focus.Upskirt = 1
            if not Player.Male:
                "Она прижимает кончик резинового члена к своему анусу, кажется, она хочет, чтобы вы вставили его."
            else:
                "Она прижимает головку вашего члена к своему анусу, кажется, она хочет, чтобы вы вставили его."

            menu:
                "Что будете делать?"
                "Не сопротивляться.":
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 2)
                    "[Ch_Focus.Name] вставляет его внутрь."
                "Похвалить ее.":
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Inbt", 80, 3)
                    ch_p "О да, [Ch_Focus.Pet], давай сделаем это."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] вставляет его внутрь."
                    $ Ch_Focus.Statup("Love", 85, 1)
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 2)
                "Сказать ей остановиться.":
                    $ Ch_Focus.FaceChange("surprised")
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    ch_p "[Ch_Focus.Pet], давай пока не будем."
                    $ Ch_Focus.NameCheck() #checks reaction to petname
                    "[Ch_Focus.Name] отстраняется."
                    $ Ch_Focus.Statup("Obed", 90, 1)
                    $ Ch_Focus.Statup("Obed", 50, 1)
                    $ Ch_Focus.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ Ch_Focus.AddWord(1,"refused","refused")
                    return
            $ Ch_Focus.PantiesDown = 1
            call Girl_First_Bottomless(Ch_Focus,1)
    elif Situation != "auto":
        call AutoStrip(Ch_Focus)
        call Girl_Initiates(Ch_Focus)      #"She presses against you and your cock pops in."

    else: #if Situation == "auto"
        if (Ch_Focus.PantsNum() >= 6 and not Ch_Focus.Upskirt) and (Ch_Focus.Panties and not Ch_Focus.PantiesDown):
            "Вы быстро стягиваете с нее штаны и [get_clothing_name(Ch_Focus.Panties_key, vin)], затем прижимаетесь к ее анусу."
        elif (Ch_Focus.Panties and not Ch_Focus.PantiesDown):
            "Вы быстро стягиваете с нее [get_clothing_name(Ch_Focus.Panties_key, vin)], затем прижимаетесь к ее анусу."
        $ Ch_Focus.Upskirt = 1
        $ Ch_Focus.PantiesDown = 1
        $ Ch_Focus.SeenPanties = 1
        call Girl_First_Bottomless(Ch_Focus,1)

    if not Ch_Focus.Anal:
        #First time stat buffs
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -150)
            $ Ch_Focus.Statup("Obed", 70, 70)
            $ Ch_Focus.Statup("Inbt", 80, 40)
        else:
            $ Ch_Focus.Statup("Love", 90, 10)
            $ Ch_Focus.Statup("Obed", 70, 30)
            $ Ch_Focus.Statup("Inbt", 80, 70)
    elif not Ch_Focus.Loose:
        #first few times stat buffs
        if Ch_Focus.Forced:
            $ Ch_Focus.Statup("Love", 90, -20)
            $ Ch_Focus.Statup("Obed", 70, 10)
            $ Ch_Focus.Statup("Inbt", 80, 5)
        else:
            $ Ch_Focus.Statup("Obed", 70, 7)
            $ Ch_Focus.Statup("Inbt", 80, 5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Player.Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no anal")
    $ Ch_Focus.RecentActions.append("anal")
    $ Ch_Focus.DailyActions.append("anal")

label Girl_Anal_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(Ch_Focus)
        call expression Ch_Focus.Tag + "_Sex_Launch" pass ("anal")
        if Speed >= 4:
            $ Shift = 2
#            call Speed_Shift(2)
        $ Ch_Focus.LustFace()
        $ Player.Cock = "anal"
        $ Trigger = "anal"
        $ Ch_Focus.Upskirt = 1
        $ Ch_Focus.PantiesDown = 1

        if Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . ." if Speed:
                                    pass
                        "Продолжать. . . (locked)" if not Speed:
                                    pass

                        "Начать? . ." if not Speed:
                                    # Modification mode
                                    if is_playing_music(audio.girl_doggy) and Ch_Focus.Pose == "doggy":
                                        $ play_music(name=audio.girl_doggy, loop=True)
                                    else:
                                        $ play_music(name=audio.girl_sex, loop=True)
                                    # -----------------

                                    $ Speed = 1
#                                    call Speed_Shift(1)
                        "Быстрее. . ." if 0 < Speed < 3:
                                    $ Speed += 1
#                                    call Speed_Shift(Speed+1)
                                    "Вы немного ускоряетесь."
                        "Быстрее. . . (locked)" if Speed >= 3:
                                    pass

                        "Помедленнее. . ." if Speed:
                                    $ Speed -= 1
#                                    call Speed_Shift(Speed-1)
                                    "Вы немного замедляетесь."
                        "Помедленнее. . . (locked)" if not Speed:
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_Anal_Cycle

                        "Развернуть ее":
                                    # Modification mode
                                    if is_playing_music(audio.girl_doggy) and Ch_Focus.Pose == "doggy":
                                        $ play_music(name=audio.girl_doggy, loop=True)
                                    else:
                                        $ play_music(name=audio.girl_sex, loop=True)
                                    # -----------------

                                    $ Ch_Focus.Pose = "doggy" if Ch_Focus.Pose != "doggy" else 0
                                    "Вы разворачиваете ее. . ."
                                    call View_Facing(Ch_Focus)
                                    jump Girl_Anal_Cycle

                        "Повернуть ее голову" if Ch_Focus.Pose == "doggy":
                                    call View_Facing(Ch_Focus,1)
                                    jump Girl_Anal_Cycle

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
                                                        "Как насчет вагинального секса?":
                                                                $ Situation = "shift"
                                                                call Girl_AnalAfter
                                                                call Girl_Sex_P
                                                        "Просто вставить ей в киску [[не спрашивая].":
                                                                $ Situation = "auto"
                                                                call Girl_AnalAfter
                                                                call Girl_Sex_P
                                                        "Потереться о ее киску.":
                                                                $ Situation = "pullback"
                                                                call Girl_AnalAfter
                                                                call Girl_Sex_H
                                                        "Неважно":
                                                                jump Girl_Anal_Cycle
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
                                                        jump Girl_Anal_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_Anal_Cycle
                                            "Неважно":
                                                        jump Girl_Anal_Cycle
                                    "Просто посмотреть на нее.":
                                            $ Player.Cock = 0
                                            $ Speed = 0

                                    "Показывать ее ноги" if not ShowFeet:# and Ch_Focus.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet:# and Ch_Focus.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_Anal_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Думаю, нам стоит попробовать что-нибудь другое."
                                    call expression Ch_Focus.Tag + "_Sex_Reset"
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_AnalAfter
                        "Закончить" if not MultiAction:
                                    ch_p "Думаю, нам стоит пока остановиться."
                                    call expression Ch_Focus.Tag + "_Sex_Reset"
                                    $ Line = 0
                                    jump Girl_AnalAfter
        #End menu (if Line)

        call Shift_Focus(Ch_Focus)
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
                                call expression Ch_Focus.Tag + "_Sex_Reset"
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                    $ Ch_Focus.RecentActions.append("unsatisfied")
                                    $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_AnalAfter
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If you're still going at it and Girl can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_AnalAfter

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                if Player.Male:
                                        "Она выжала из вас все соки, вам нужно передохнуть."
                                else:
                                        "Она вас утомила, вам нужно передохнуть."
                                jump Girl_AnalAfter
                            elif "unsatisfied" in Ch_Focus.RecentActions:
                                #And Ch_Focus is unsatisfied,
                                $ Line = renpy.random.choice(["Она продолжает слегка дрожать от удовольствия.",
                                    "Она тяжело дышит, пока вы ее трахаете.",
                                    "Она медленно поворачивается к вам и улыбается.",
                                    "Кажется, она не собирается останавливаться."])
                                "[Line] Продолжите?"
                                menu:
                                    extend ""
                                    "Да. Продолжим еще немного." if Player.Semen:
                                        $ Line = "Вы возвращаетесь к процессу"
                                        jump Girl_Anal_Cycle
                                    "С меня хватит." if Player.Semen:
                                        "Вы заканчиваете веселье."
                                        jump Girl_AnalAfter
                                    "Нет, у меня нет сил." if not Player.Semen:
                                        "Вы заканчиваете веселье."
                                        jump Girl_AnalAfter
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.Anal):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Ты уже скоро? Мне немного больно."
                    elif Ch_Focus is KittyX:
                            if KittyX.Loose:
                                ch_k "Ты уже[KittyX.like]скоро?"
                            else:
                                ch_k "Ты уже[KittyX.like]скоро? Это не очень приятно. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Мы скоро?"
                    elif Ch_Focus is LauraX:
                            ch_l "Мы уже скоро?"
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно, тебе достаточно хорошо?"
                    elif Ch_Focus is StormX:
                            ch_s "Ты уже скоро?"
                    elif Ch_Focus is JubesX:
                            ch_v "Как тебе?"
                    elif Ch_Focus is GwenX:
                            ch_g "Ох. . . эм. . . ты как?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Боже. . . эм. . . ты как?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Ох. . . эм. . . тебе нравится?"
                    elif Ch_Focus is WandaX:
                            ch_w "Ты уже скоро?"
        elif Cnt == (10 + Ch_Focus.Anal):
                    $ Ch_Focus.Brows = "angry"
                    if Ch_Focus is RogueX:
                            ch_r "У меня . . .начинает . . .натирать. . . там . . [RogueX.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Я . . .немного . . уже. . . устала. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Я . . .уже . . немного. . . устала. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Мы может. . . заняться. . . чем-нибудь. . . другим?"
                    elif Ch_Focus is JeanX:
                            ch_j "Мы может. . . заняться. . . чем-нибудь. . . другим?"
                    elif Ch_Focus is StormX:
                            ch_s "Мне . . .немного . . неприятно. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Мы может. . . заняться. . . чем-нибудь. . . другим?"
                    elif Ch_Focus is GwenX:
                            ch_g "Слушай. . . мы можем. . . заняться чем-нибудь. . . другим?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Ох. . . мы можем. . . заняться чем-нибудь. . . другим?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Эм. . . не могли бы мы. . . заняться. . . чем-нибудь. . . другим?"
                    elif Ch_Focus is WandaX:
                            ch_w "Послушай. . . может. . .  мы могли бы. . . попробовать. . . что-нибудь другое?"
                    menu:
                        extend ""
                        "Как насчет отсоса?" if Ch_Focus.Action and MultiAction and Player.Male:
                                $ Situation = "shift"
                                call Girl_AnalAfter
                                call Girl_Blowjob
                        "How about a Handy?" if Ch_Focus.Action and MultiAction and Player.Male:
                                $ Situation = "shift"
                                call Girl_AnalAfter
                                call Girl_Handjob
                        "Как насчет вылизать мою киску?" if Ch_Focus.Action and MultiAction and not Player.Male:
                                $ Situation = "shift"
                                call Girl_AnalAfter
                                call Girl_CUN
                        "Может, поиграешь с моей киской?" if Ch_Focus.Action and MultiAction and not Player.Male:
                                $ Situation = "shift"
                                call Girl_AnalAfter
                                call Girl_Finger
                        "Закончить." if Player.FocusX:
                                "Вы расслабляетесь. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Girl_Anal_Cycle
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                call expression Ch_Focus.Tag + "_Sex_Reset"
                                $ Situation = "shift"
                                jump Girl_AnalAfter
                        "Нет, давай за работу.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она ворчит, но продолжает."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call expression Ch_Focus.Tag + "_Sex_Reset"
                                    "Она хмурится и отстраняется."
                                    if Ch_Focus is RogueX:
                                            ch_r "С таким отношением, ты и без меня отлично справишься."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Не с таким отношением!"
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Я так не думаю."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Не с таким отношением."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Не переоценивай себя."
                                    elif Ch_Focus is StormX:
                                            ch_s "Нет, я так не думаю."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Точно не сейчас."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Хорошо, тогда мы закончили."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Что ж, тогда мы закончили."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Ну, мы так точно не договаривались!"
                                    elif Ch_Focus is WandaX:
                                            ch_w "Ладно, игры кончились!"
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_AnalAfter
        #End Count check

        if Round == 10:
            call Sex_Basic_Dialog(Ch_Focus,10)  #ch_d "It's getting late, we should wrap this up."
        elif Round == 5:
            call Sex_Basic_Dialog(Ch_Focus,5)  #ch_d "Tic tock, [Ch_Focus.Petname]."

    #Round = 0 loop breaks
    $ Ch_Focus.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Ch_Focus,"done")  # ch_d "Ok, [Ch_Focus.Petname], breaktime."

label Girl_AnalAfter:
    # Modification mode
    $ play_music()
    $ play_sound()
    # -----------------

    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call expression Ch_Focus.Tag + "_Sex_Reset"

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.Anal += 1
    $ Ch_Focus.Action -=1
    if Player.Male:
            $ Ch_Focus.Addictionrate += 1
            if "addictive" in Player.Traits:
                $ Ch_Focus.Addictionrate += 1
    $ Ch_Focus.Statup("Inbt", 30, 3)
    $ Ch_Focus.Statup("Inbt", 70, 1)

    call Partner_Like(Ch_Focus,3,2)

    if Ch_Focus.Tag+" Anal Addict" in Achievements:
            pass

    elif Ch_Focus.Anal >= 10:
            $ Ch_Focus.SEXP += 7
            $ Achievements.append(Ch_Focus.Tag+" Anal Addict")
            if not Situation:
                $ Ch_Focus.FaceChange("bemused", 1)
                if Ch_Focus is RogueX:
                        ch_r "Я. . . похоже, мне это действительно очень нравится. . ."
                elif Ch_Focus is KittyX:
                        ch_k "Я не думала, что мне это так понравится!"
                elif Ch_Focus is EmmaX:
                        if not Player.Male:
                            ch_e "Ты одна из лучших партнеров, которые у меня были."
                        else:
                            ch_e "Ты один из лучших партнеров, которые у меня были."
                elif Ch_Focus is LauraX:
                        ch_l "Думаю, у тебя к этому талант."
                elif Ch_Focus is JeanX:
                        ch_j "Весело поупражнялись."
                elif Ch_Focus is StormX:
                        ch_s "Мне определенно это нравится."
                elif Ch_Focus is JubesX:
                        ch_v "Теперь я вроде как в это втянулась. . ."
                elif Ch_Focus is GwenX:
                        ch_g "Я никогда бы не подумала, что мне это так понравится. . ."
                elif Ch_Focus is BetsyX:
                        ch_b "Если бы меня сейчас видели мои старые обидчицы. . ."
                elif Ch_Focus is DoreenX:
                        ch_d "Я и не осознавала, насколько это может быть приятно!"
                elif Ch_Focus is WandaX:
                        ch_w "Я и не подозревала, насколько сильно мне стало это нравится!"
    elif Ch_Focus.Anal == 1:
            $Ch_Focus.SEXP += 25
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                        if Ch_Focus is RogueX:
                                ch_r "Это было . . . интересно, [RogueX.Petname]. Нам нужно будет как-нибудь повторить."
                        elif Ch_Focus is KittyX:
                                ch_k "Анальный секс. . . хихи, кто бы мог подумать?"
                        elif Ch_Focus is EmmaX:
                                if not Player.Male:
                                    ch_e "Ты очень хорошо справилась."
                                else:
                                    ch_e "Ты очень хорошо справился."
                        elif Ch_Focus is LauraX:
                                ch_l "Похоже ты знаешь, что делаешь."
                        elif Ch_Focus is JeanX:
                                ch_j "Мммм, это было приятно. . ."
            #            elif Ch_Focus is StormX:
                        elif Ch_Focus is JubesX:
                                ch_v "Ты, эм. . . знаешь, что нужно делать. . ."
                        elif Ch_Focus is GwenX:
                                ch_g "Оооох. . . это, эм. . . ."
                                ch_g "Было не так уж плохо. . ."
                        elif Ch_Focus is BetsyX:
                                ch_b "Ооох. . . это, эм. . . ."
                                ch_b "Должна признать, это было не так уж и неприятно. . ."
                        elif Ch_Focus is DoreenX:
                                ch_d "То. . . что, эм. . . ."
                                ch_d "-произошло. . ."
                                ch_d ". . ."
                                ch_d ". . . было не так уж и плохо. . ."
                        elif Ch_Focus is WandaX:
                                ch_w "Это. . . было очень здорово.."
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                        $ Ch_Focus.Mouth = "sad"
                        if Ch_Focus is RogueX:
                                ch_r "Ай."
                                if not Player.Male:
                                    ch_r "Ты получила то, что тебе было нужно?"
                                else:
                                    ch_r "Ты получил то, что тебе было нужно?"
                        elif Ch_Focus is KittyX:
                                ch_k "Ай."
                                if not Player.Male:
                                    ch_k "Думаю, ты получила то, что хотела?"
                                else:
                                    ch_k "Думаю, ты получил то, что хотел?"
                        elif Ch_Focus is EmmaX:
                                ch_e "Ооох."
                                ch_e "Давно я не испытывала подобного."
                        elif Ch_Focus is LauraX:
                                ch_l "Это было приятно."
                        elif Ch_Focus is JeanX:
                                ch_j "Это было здорово. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Что ж. . ."
                        elif Ch_Focus is JubesX:
                                ch_v "Это было. . . неплохо."
                        elif Ch_Focus is GwenX:
                                ch_g "Это было. . . неплохо."
                        elif Ch_Focus is BetsyX:
                                ch_b "Это было. . . терпимо."
                        elif Ch_Focus is DoreenX:
                                ch_d "Это было, эм. . . думаю, неплохо."
                        elif Ch_Focus is WandaX:
                                ch_w "Ладно, это закончилось. . ."
                if Ch_Focus is StormX:
                        ch_s "Это было очень интересно. . ."
    elif Ch_Focus.Anal == 5:
            if Ch_Focus is RogueX:
                    ch_r "Похоже, у нас это вошло в привычку."
            elif Ch_Focus is KittyX:
                    ch_k "Мне это правда начинает нравиться."
            elif Ch_Focus is EmmaX:
                    if not Player.Male:
                        ch_e "А ты довольно хороша."
                    else:
                        ch_e "А ты довольно хорош."
            elif Ch_Focus is LauraX:
                    ch_l "Я рада, что занимаюсь этим с тобой."
            elif Ch_Focus is JeanX:
                    ch_j "Я рада, что у нас похожие интересы. . ."
            elif Ch_Focus is StormX:
                    ch_s "Ты, безусловно, делаешь процесс приятным."
            elif Ch_Focus is JubesX:
                    ch_v "Это довольно весело."
            elif Ch_Focus is GwenX:
                    ch_g "Это. . . намного лучше, чем я ожидала."
            elif Ch_Focus is BetsyX:
                    ch_b "Это. . . гораздо более занимательно, чем я ожидала."
            elif Ch_Focus is DoreenX:
                    ch_d "Думаю. . . я смогу привыкнуть. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Я уже с нетерпением жду следующего раза."
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        if "unsatisfied" in Ch_Focus.RecentActions:
            $ Ch_Focus.FaceChange("angry")
            $ Ch_Focus.Eyes = "side"
            if Ch_Focus is RogueX:
                    if not Player.Male:
                        ch_r "Хмм, похоже ты получила от этого больше удовольствия, чем я. . ."
                    else:
                        ch_r "Хмм, похоже ты получил от этого больше удовольствия, чем я. . ."
            elif Ch_Focus is KittyX:
                    if not Player.Male:
                        ch_k "Хмм, похоже ты получила от этого больше пользы, чем я. . ."
                    else:
                        ch_k "Хмм, похоже ты получил от этого больше пользы, чем я. . ."
            elif Ch_Focus is EmmaX:
                    if not Player.Male:
                        ch_e "Хм, похоже, ты получила больше удовольствия, чем я. . ."
                    else:
                        ch_e "Хм, похоже, ты получил больше удовольствия, чем я. . ."
            elif Ch_Focus is LauraX:
                    if not Player.Male:
                        ch_l "Ничего не забыла? . ."
                    else:
                        ch_l "Ничего не забыл? . ."
            elif Ch_Focus is JeanX:
                    ch_j "Думаю, тебе нужно продолжить."
            elif Ch_Focus is StormX:
                    ch_s "Боюсь, что тебе понравилось больше, чем мне. . ."
            elif Ch_Focus is JubesX:
                    ch_v "Эй, закончи со мной!"
            elif Ch_Focus is GwenX:
                    ch_g "Слушай. . . я не совсем. . . довольна. . ."
            elif Ch_Focus is BetsyX:
                    ch_b  "Боюсь, тебе еще есть над чем поработать. . ."
            elif Ch_Focus is DoreenX:
                    ch_d  "Мне. . . не понравилось. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Послушай, тебе нужно довести меня до оргазма."

    $ Tempmod = 0
#    if Situation == "shift":
#        ch_d "Mmm, so what else did you have in mind?"
    call Checkout
    return


# End Girl Anal //////////////////////////////////////////////////////////////////////////////////



# Girl hotdog //////////////////////////////////////////////////////////////////////

label Girl_Sex_H: #rkeljsvg
##    #fix remove
#    if Ch_Focus is WandaX:
#        "Not currently available."
#        return
##    #fix remove
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Ch_Focus)
    if Ch_Focus.Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif Ch_Focus.Hotdog: #You've done it before
        $ Tempmod += 5
    elif Ch_Focus is DoreenX:               #You haven't done it before
        $ Tempmod -= 3

    if not Player.Male:
        $ Tempmod += 5

    if Ch_Focus.Lust > 85:
        $ Tempmod += 10
    elif Ch_Focus.Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
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

    if "no hotdog" in Ch_Focus.DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no hotdog" in Ch_Focus.RecentActions else 0

    $ Approval = ApprovalCheck(Ch_Focus, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if Situation == "auto":
            if not Player.Male and "strapon" not in Player.RecentActions:
                    "Вы достаете свой резиновый член."
                    $ Player.AddWord(1,"strapon",0,0,0) #Recent
            if renpy.showing(Ch_Focus.Tag+"_SexSprite") or renpy.showing(Ch_Focus.Tag+"_Doggy_Animation"):
                    pass
            else:
                    call expression Ch_Focus.Tag + "_Sex_Launch" pass ("hotdog")
                    if Ch_Focus.Pose == "doggy":
                            if not Player.Male:
                                "Вы прижимаете свой резиновый член к ее попке."
                            else:
                                "Вы прижимаете свой член к ее попке."
                    else:
                            if not Player.Male:
                                "Вы толкаете ее на спину и прижимаетесь к ней своим резиновым членом."
                            else:
                                "Вы толкаете ее на спину и прижимаетесь к ней своим твердым членом."
            $ Ch_Focus.FaceChange("surprised", 1)

            if "hotdog" in Ch_Focus.RecentActions:
                    jump Girl_HotdogPrep

            if (Ch_Focus.Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[Ch_Focus.Name] опускает взгляд, а затем расплывается в улыбке."
                    $ Ch_Focus.FaceChange("sly")
                    $ Ch_Focus.Statup("Obed", 70, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 3)
                    $ Ch_Focus.Statup("Inbt", 70, 1)
                    if Ch_Focus is RogueX:
                            ch_r "Ладно, [RogueX.Petname], давай сделаем это."
                    elif Ch_Focus is KittyX:
                            ch_k "Ох. . . продолжай, [KittyX.Petname]."
                    elif Ch_Focus is EmmaX:
                            ch_e "Ммм, если ты настаиваешь, [EmmaX.Petname]."
                    elif Ch_Focus is LauraX:
                            ch_l "Меня все устраивает, [LauraX.Petname]."
                    elif Ch_Focus is JeanX:
                            ch_j "Оох, если тебе это так нужно, [JeanX.Petname]."
                    elif Ch_Focus is StormX:
                            ch_s "Ммм, если ты настаиваешь, [StormX.Petname]."
                    elif Ch_Focus is JubesX:
                            ch_v "Меня это устраивает, [JubesX.Petname]."
                    elif Ch_Focus is GwenX:
                            ch_g "Ооох. . . ладно, [GwenX.Petname]."
                    elif Ch_Focus is BetsyX:
                            ch_b "OОоох. . . конечно, [BetsyX.Petname]."
                    elif Ch_Focus is DoreenX:
                            ch_d "Ооо. . . ладно, [Ch_Focus.Petname]."
                    elif Ch_Focus is WandaX:
                            ch_w "Ну ладно, [WandaX.Petname]."
                    jump Girl_HotdogPrep
            else:                                                                                                            #she's questioning it
                    $ Ch_Focus.Brows = "angry"
                    if Ch_Focus is RogueX:
                            ch_r "Хмм, это было довольно грубо, [RogueX.Petname]."
                    elif Ch_Focus is KittyX:
                            ch_k "Хмм, это было довольно грубо, [KittyX.Petname]."
                    elif Ch_Focus is EmmaX:
                            ch_e "[EmmaX.Petname], может, сбавишь обороты?"
                    elif Ch_Focus is LauraX:
                            ch_l "[LauraX.Petname], может, сбавишь обороты?"
                    elif Ch_Focus is JeanX:
                            ch_j "[JeanX.Petname], ты не слишком близко?"
                    elif Ch_Focus is StormX:
                            ch_s "[StormX.Petname], ты довольно близко. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Ох! Это то, о чем я думаю?"
                    elif Ch_Focus is GwenX:
                            ch_g "Эй! Подожди!"
                    elif Ch_Focus is BetsyX:
                            ch_b "Пардон?!"
                    elif Ch_Focus is DoreenX:
                            ch_d "Эй, что ты делаешь?"
                    elif Ch_Focus is WandaX:
                            ch_w "Эй, подожди секунду!"
                    menu:
                        extend ""
                        "Извини-извини! Я уже ничего не делаю.":
                            if Approval:
                                    $ Ch_Focus.FaceChange("sexy", 1)
                                    $ Ch_Focus.Statup("Obed", 70, 3)
                                    $ Ch_Focus.Statup("Inbt", 50, 3)
                                    $ Ch_Focus.Statup("Inbt", 70, 1)
                                    if Ch_Focus is RogueX:
                                            ch_r "Думаю, это не так уж плохо. . ."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Думаю, это не так уж плохо. . ."
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Или не надо. . ."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Или не надо. . ."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Я не сказала, что против. . ."
                                    elif Ch_Focus is StormX:
                                            ch_s "Ну, или нет. . ."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Ох, я не говорила тебе остановиться. . ."
                                    elif Ch_Focus is GwenX:
                                            if not Player.Male:
                                                ch_g "Ох, ты только что собиралась. . ."
                                            else:
                                                ch_g "Ох, ты только что собирался. . ."
                                            ch_g "Ладно. . ."
                                    elif Ch_Focus is BetsyX:
                                            if not Player.Male:
                                                ch_b "Ты хотела. . ."
                                                ch_b "Ппросто ты застала меня врасплох, можешь продолжать. . ."
                                            else:
                                                ch_b "Ты хотел. . ."
                                                ch_b "Просто ты застал меня врасплох, можешь продолжать. . ."
                                    elif Ch_Focus is DoreenX:
                                            if not Player.Male:
                                                ch_d "Ох, ты хотела просто. . ."
                                            else:
                                                ch_d "Ох, ты хотел просто. . ."
                                            ch_d "Ладно. . ."
                                    elif Ch_Focus is WandaX:
                                            ch_w "О, я поняла, можешь продолжать."
                                    jump Girl_HotdogPrep
                            "Вы отстраняетесь от нее."
                            $ Ch_Focus.FaceChange("bemused", 1)
                            if Ch_Focus is RogueX:
                                    ch_r "Ну ладно, [RogueX.Petname], я еще не совсем готов к этому, но, может быть, если ты в следующий раз вежливо попросишь . . ."
                            elif ChFocus is KittyX:
                                    ch_k "Может, стоило сначала[KittyX.like]предупредить меня? Я не думаю, что[KittyX.like]готова к таким вещам. . ."
                            elif Ch_Focus is EmmaX:
                                    ch_e "Возможно в другой раз, когда ты вежливо попросишь."
                            elif Ch_Focus is LauraX:
                                    if not Player.Male:
                                        ch_l "Может, если бы ты сначала спросила. . ."
                                    else:
                                        ch_l "Может, если бы ты сначала спросил. . ."
                            elif Ch_Focus is JeanX:
                                    ch_j "Тебе стоило бы сначала спросить, [JeanX.Petname]."
                            elif Ch_Focus is StormX:
                                    ch_s "Возможно, в другой раз. . ."
                            elif Ch_Focus is JubesX:
                                    ch_v "Тебе следовало бы сначала спросить. . ."
                            elif Ch_Focus is GwenX:
                                    ch_g "Сначала стоит спрашивать. . ."
                            elif Ch_Focus is BetsyX:
                                    if not Player.Male:
                                        ch_b "Было бы неплохо, если бы ты сначала предупредила. . ."
                                    else:
                                        ch_b "Было бы неплохо, если бы ты сначала предупредил. . ."
                            elif Ch_Focus is DoreenX:
                                    ch_d "Я. . . следует сперва спрашивать, прежде чем делать что-то подобное. . ."
                            elif Ch_Focus is WandaX:
                                    if not Player.Male:
                                        ch_w "Послушай, если бы ты сперва спросила, то, возможно. . . ладно, не важно. . ."
                                    else:
                                        ch_w "Послушай, если бы ты сперва спросил, то, возможно. . . ладно, не важно. . ."
                        #end "Извини-извини! Я уже ничего не делаю.":

                        "Сейчас ты все узнаешь.":
                                $ Ch_Focus.Statup("Love", 80, -10, 1)
                                $ Ch_Focus.Statup("Love", 200, -8)
                                "Вы начинаете тереться о ее промежность."
                                $ Ch_Focus.Statup("Obed", 70, 3)
                                $ Ch_Focus.Statup("Inbt", 50, 3)
                                if not ApprovalCheck(Ch_Focus, 500, "O", TabM=1): #Checks if Obed is 700+
                                    $ Ch_Focus.FaceChange("angry")
                                    "[Ch_Focus.Name] отталкивает вас."
                                    if Ch_Focus is RogueX:
                                            if not Player.Male:
                                                ch_r "Вот сучка!"
                                            else:
                                                ch_r "Гондон!"
                                            ch_r "Если ты хочешь вести себя так, я ухожу!"
                                    elif Ch_Focus is KittyX:
                                            if not Player.Male:
                                                ch_k "Дура!"
                                            else:
                                                ch_k "Придурок!"
                                            ch_k "Я на такое не подписывалась!"
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Не искушай судьбу, [EmmaX.Petname]."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Не наглей, [LauraX.Petname]."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Не наглей, [JeanX.Petname]."
                                    elif Ch_Focus is StormX:
                                            ch_s "Не перебарщивай, [StormX.Petname]."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Держи его подальше от меня, [JubesX.Petname]."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Эй!"
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Я так не думаю!"
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Эй!"
                                    elif Ch_Focus is WandaX:
                                            ch_w "Воу!"
                                    $ Ch_Focus.Statup("Love", 50, -10, 1)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ renpy.pop_call()
                                    if Situation:
                                        $ renpy.pop_call()
                                    call expression Ch_Focus.Tag + "_Sex_Reset"
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                else:
                                    $ Ch_Focus.FaceChange("sad")
                                    "[Ch_Focus.Name_dat] это не нравится, но она знает свое место."
                                    jump Girl_HotdogPrep
            return
            #end auto


    if not Ch_Focus.Hotdog and "no hotdog" not in Ch_Focus.RecentActions:
            #first time
            $ Ch_Focus.FaceChange("surprised", 1)
            $ Ch_Focus.Mouth = "kiss"
            if Ch_Focus is RogueX:
                    ch_r "Подожди, так ты хочешь потереться о меня?!"
            elif Ch_Focus is KittyX:
                    ch_k "Так что, хочешь просто потереться о меня?"
            elif Ch_Focus is EmmaX:
                    ch_e "Ты хочешь просто потереться о меня?"
            elif Ch_Focus is LauraX:
                    ch_l "Что, хочешь просто потереться?"
            elif Ch_Focus is JeanX:
                    ch_j "Что, хочешь просто потереться?"
            elif Ch_Focus is StormX:
                    ch_s "Тебе просто хочется потереться о меня?"
            elif Ch_Focus is JubesX:
                    ch_v "Ты просто хочешь потереться о меня?"
            elif Ch_Focus is GwenX:
                    ch_g "О, ты хочешь. . . [[трет руками друг о друга]?"
            elif Ch_Focus is BetsyX:
                    ch_b "О, ты хочешь только потереться о меня?"
            elif Ch_Focus is DoreenX:
                    ch_d "Значит. . . ты хочешь просто потереться о меня. . ."
            elif Ch_Focus is WandaX:
                    ch_w "Хочешь потереться о меня?"
            if not Player.Male:
                    if Ch_Focus is RogueX:
                            ch_r "Я чего-то о тебе не знаю?"
                    elif Ch_Focus is KittyX:
                            ch_k "Как ты[KittyX.like]собираешься. . .?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Могу спросить, как ты собираешься это сделать. . ?"
                    elif Ch_Focus is LauraX:
                            ch_l "Мне кажется, у тебя кое-чего нет. . ."
                    elif Ch_Focus is JeanX:
                            cch_j "Я не вижу у тебя члена."
                    elif Ch_Focus is StormX:
                            ch_s "Могу я спросить \"Как?\""
                    elif Ch_Focus is JubesX:
                            ch_v "Как?!"
                    elif Ch_Focus is GwenX:
                            ch_g "Хорошо, что у тебя нет-"
                    elif Ch_Focus is BetsyX:
                            ch_b "Пожалуй, поскольку у тебя нет- . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Но у тебя ведь нет-"
                    elif Ch_Focus is WandaX:
                            ch_w "Ты захватила игрушки?"
                    menu:
                        "Я подготовилась. . .":
                                pass
                        "Скоро ты поймешь. . .":
                                $ Ch_Focus.Statup("Obed", 90, 2)

            if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    if Ch_Focus is RogueX:
                            ch_r ". . . И все?"
                    elif Ch_Focus is KittyX:
                            ch_k ". . . И все?"
                    elif Ch_Focus is EmmaX:
                            ch_e ". . . и не более?"
                    elif Ch_Focus is LauraX:
                            ch_l ". . . и все?"
                    elif Ch_Focus is JeanX:
                            ch_j ". . . и все?"
                            if Approval and Player.Male == 1:
                                if not Player.Male:
                                    ch_j "У кого из нас тут самая лучшая киска?"
                                else:
                                    ch_j "У кого из нас тут киска?"
                    elif Ch_Focus is StormX:
                            ch_s ". . . и не более?"
                    elif Ch_Focus is JubesX:
                            ch_v ". . . и все?"
                    elif Ch_Focus is GwenX:
                            ch_g ". . . и все?"
                    elif Ch_Focus is BetsyX:
                            ch_b ". . . и все?"
                    elif Ch_Focus is DoreenX:
                            ch_d ". . . и все?"
                    elif Ch_Focus is WandaX:
                            ch_w ". . . и все?"
    #end first time


    if not Ch_Focus.Hotdog and Approval:
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
                            ch_r "Похоже, тебе не повредит небольшая разрядка. . ."
                    elif Ch_Focus is KittyX:
                            if not Player.Male:
                                ch_k "Она выглядит немного опухшой. . ."
                            else:
                                ch_k "Он выглядит немного опухшим. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Я не хотела бы оставлять тебя. . . без внимания. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Если тебе такое нравится. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Хорошо, мы можем начать с этого. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Я бы не хотела оставлять тебя. . . без присмотра. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Ох, ладно. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Не вижу в этом проблемы. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Я не вижу в этом проблемы. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я. . . думаю, это может быть не так уж и плохо. . ."
                    elif Ch_Focus is WandaX:
                            ch_d "Я. . . думаю, это нормально. . ."
            elif Ch_Focus.Obed >= Ch_Focus.Inbt:
                    $ Ch_Focus.FaceChange("normal")
                    if Ch_Focus in (EmmaX,StormX,BetsyX):
                            call AnyLine(Ch_Focus,"Если это то, чего ты хочешь, "+Ch_Focus.Petname+". . .")
                    else:
                            call AnyLine(Ch_Focus,"Если ты так этого хочешь, "+Ch_Focus.Petname+". . .")
            else: # Uninhibited
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Mouth = "smile"
                    if Ch_Focus is RogueX:
                            if not Player.Male:
                                ch_r "Хмм, по крайней мере, похоже, что ты готова. . ."
                            else:
                                ch_r "Хмм, по крайней мере, похоже, что ты готов. . ."
                    elif Ch_Focus is KittyX:
                            if not Player.Male:
                                ch_k "Хм, похоже, ты уже готова. . ."
                            else:
                                ch_k "Хм, похоже, ты уже готов. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Хорошо, если это тебя так заводит. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Хорошо, если это тебя так заводит. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Хорошо, мы можем начать с этого. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Что ж, если ты получишь от этого удовольствие. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Конечно. . . наверное. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Думаю, это может быть весело. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Пожалуй, это может юыть довольно забавно. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Наверное, это может быть весело. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Наверное, это может быть весело. . ."
    #end first time approval

    elif Approval:
            #Second time+ dialog
            if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Love", 70, -3, 1)
                    $ Ch_Focus.Statup("Love", 20, -2, 1)
                    if Ch_Focus is RogueX:
                            ch_r "Это все, что тебе нужно?"
                    elif Ch_Focus is KittyX:
                            ch_k "Это все, чего ты хочешь?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Возможно, все заходит слишком далеко. . ."
                    elif Ch_Focus is LauraX:
                            if not Player.Male:
                                ch_l "Лучше бы ты не давила. . ."
                            else:
                                ch_l "Лучше бы ты не давил. . ."
                    elif Ch_Focus is JeanX:
                            if not Player.Male:
                                ch_j "Ты странная. . ."
                            else:
                                ch_j "Ты странный. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Возможно, все заходит слишком далеко. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Это. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Я не уверена. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Меня все это несколько смущает. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Я не уверена. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Думаешь, все так просто. . ?"
            elif not Taboo and "tabno" in Ch_Focus.DailyActions:
                    call Sex_Basic_Dialog(Ch_Focus,"tabyes") #"This -would- be a better place for it. . ."
            elif "hotdog" in Ch_Focus.RecentActions:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    if Ch_Focus is RogueX:
                            ch_r "Хочешь повторить? Ладно."
                    elif Ch_Focus is KittyX:
                            ch_k "Еще раз? Ладно."
                    elif Ch_Focus is EmmaX:
                            ch_e "Снова? Ох, хорошо."
                    elif Ch_Focus is LauraX:
                            ch_l "Снова? Ну, пеняй на себя."
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно, [JeanX.Petname]. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Снова? Ох, хорошо."
                    elif Ch_Focus is JubesX:
                            ch_v "Снова? Хм. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Снова? И почему я не удивлена. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Снова? Хорошо."
                    elif Ch_Focus is DoreenX:
                            ch_d "Снова? Ох. . . хорошо. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Снова? Ого, ну ладно. . ."
                    jump Girl_HotdogPrep
            elif "hotdog" in Ch_Focus.DailyActions:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    if Ch_Focus in (EmmaX,StormX,BetsyX):
                        $ Line = renpy.random.choice(["Снова?",
                            "Хочешь еще раз?",
                            "Должно быть, я талантливее, чем я думала.",
                            "Тебе все еще мало?",
                            "Снова? Что ж, я не должна от тебя отставать. . ." ])
                    elif Ch_Focus is RogueX:
                        $ Line = renpy.random.choice(["Снова так скоро?",
                            "Хочешь еще заход?",
                            "Похоже, ты без ума от этого. . .",
                            "Это точно все, чего ты хочешь?"])
                    else:
                        $ Line = renpy.random.choice(["Желаешь добавки?",
                            "Желаешь еще разок?",
                            "Наверное, я лучше, чем я думала.",
                            "Тебе все еще мало?",
                            Ch_Focus.Petname + " ты меня совсем загоняешь."])
                    call AnyLine(Ch_Focus,Line)
            else:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.ArmPose = 2
                    $ Line = renpy.random.choice(["Я настолько сексуальна?",
                        "Желаешь еще заход?",
                        "Должно быть, я лучше, чем я думала.",
                        "Я думаю, ты знаешь, что делаешь.",
                        "Хочешь снова потереться о меня?"])
                    call AnyLine(Ch_Focus,Line)

                    if Ch_Focus in (EmmaX,StormX,BetsyX):
                        $ Line = renpy.random.choice(["Я просто слишком неотразима?",
                            "Хочешь еще заход?",
                            "Должно быть, я талантливее, чем я думала.",
                            "Полагаю, ты знаешь, чего хочешь.",
                            "Хочешь взять меня?"])
                    else:
                        $ Line = renpy.random.choice(["Я настолько сексуальна?",
                            "Желаешь еще заход?",
                            "Должно быть, я лучше, чем я думала.",
                            "Я думаю, ты знаешь, что делаешь.",
                            "Хочешь снова потереться о меня?"])
                    call AnyLine(Ch_Focus,Line)
            $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if Ch_Focus.Forced:
                    $ Ch_Focus.FaceChange("sad")
                    $ Ch_Focus.Statup("Obed", 80, 1)
                    $ Ch_Focus.Statup("Inbt", 60, 1)
                    if Ch_Focus is RogueX:
                            ch_r "Хорошо."
                    elif Ch_Focus is KittyX:
                            ch_k "Лаааадно."
                    elif Ch_Focus is EmmaX:
                            ch_e "Ох, хорошо, если ты заткнешься."
                    elif Ch_Focus is LauraX:
                            ch_l "Ладно. Только сделай все хорошо."
                    elif Ch_Focus is JeanX:
                            ch_j "Ладно. Только сделай все хорошо."
                    elif Ch_Focus is StormX:
                            ch_s "Ох, хорошо, если это тебя удовлетворит."
                    elif Ch_Focus is JubesX:
                            ch_v "Лучше бы это того стоило."
                    elif Ch_Focus is GwenX:
                            ch_g "Ладно, думаю, будет весело."
                    elif Ch_Focus is BetsyX:
                            ch_b "Конечно, пожалуй, я смогу это вынести."
                    elif Ch_Focus is DoreenX:
                            ch_d "Хорошо, тогда давай займемся делом."
                    elif Ch_Focus is WandaX:
                            ch_w "Ладно, давай сделаем это."
            else:
                    $ Ch_Focus.FaceChange("sexy", 1)
                    $ Ch_Focus.Statup("Love", 80, 1)
                    $ Ch_Focus.Statup("Inbt", 50, 2)
                    $ Line = renpy.random.choice(["Ну конечно.",
                        "Ну. . . ладно.",
                        "Хорошо!",
                        "Думаю, можно.",
                        "О, да!",
                        "Хех, ладно."])
                    call AnyLine(Ch_Focus,Line)
                    $ Line = 0
            $ Ch_Focus.Statup("Obed", 60, 1)
            $ Ch_Focus.Statup("Inbt", 70, 2)
            jump Girl_HotdogPrep

    else:
            #She's not into it, but maybe. . .
            $ Ch_Focus.FaceChange("angry")
            if "no hotdog" in Ch_Focus.DailyActions:
                    call Sex_Basic_Dialog(Ch_Focus,"norecent")
            elif Taboo and "tabno" in Ch_Focus.DailyActions:
                    call Sex_Basic_Dialog(Ch_Focus,"tabnoday")
            elif not Ch_Focus.Hotdog:
                    $ Ch_Focus.FaceChange("bemused")
                    if Ch_Focus is RogueX:
                            ch_r "Это очень неприлично, [RogueX.Petname]. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Меня это заводит, [KittyX.Petname], но. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Хм, это не самое странное предложение, [EmmaX.Petname]. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Хм, это может быть весело, [LauraX.Petname], но. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Хм, это не самое странное предложение, [JeanX.Petname]. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Хм, это может быть интересно, [StormX.Petname], но. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Хм, это может быть весело, [JubesX.Petname]. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Ну.  . . Думаю, это не самая странная идея. . ."
                    elif Ch_Focus is BetsyX:
                            ch_b "Что ж. . . пожалуй, это не самая необычная идея. . ."
                    elif Ch_Focus is DoreenX:
                            ch_d "Наверное. . . это не самое плохое предложение, но. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Могло быть и хуже. . ."
            else:
                    $ Ch_Focus.FaceChange("bemused")
                    if Ch_Focus is RogueX:
                            ch_r "Не сейчас, [RogueX.Petname]. . ."
                    elif Ch_Focus is KittyX:
                            ch_k "Не. . . сейчас. . ."
                    elif Ch_Focus is EmmaX:
                            ch_e "Не думаю, что это вообще уместно. . ."
                    elif Ch_Focus is LauraX:
                            ch_l "Это было бы неправильно. . ."
                    elif Ch_Focus is JeanX:
                            ch_j "Не думаю, что это вообще уместно. . ."
                    elif Ch_Focus is StormX:
                            ch_s "Я не думаю, что это было бы уместно. . ."
                    elif Ch_Focus is JubesX:
                            ch_v "Нее. . ."
                    elif Ch_Focus is GwenX:
                            ch_g "Я просто. . . зачем. . ?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Я должна спросить. . . зачем мне это. . ?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Я просто. . ."
                    elif Ch_Focus is WandaX:
                            ch_w "Я просто. . ."
            menu:
                extend ""
                "Извини, забудь." if "no hotdog" in Ch_Focus.DailyActions:
                        $ Ch_Focus.FaceChange("bemused")
                        call Sex_Basic_Dialog(Ch_Focus,"noproblem")  # ch_d "Aw, don't worry about it. . ."
                        return
                "Может, в другой раз?" if "no hotdog" not in Ch_Focus.DailyActions:
                        $ Ch_Focus.FaceChange("sexy")
                        call Sex_Basic_Dialog(Ch_Focus,"maybe")  # ch_d "I'll think about it, [Ch_Focus.Petname]."
                        $ Ch_Focus.Statup("Love", 80, 1)
                        $ Ch_Focus.Statup("Inbt", 50, 1)
                        if Taboo:
                            $ Ch_Focus.RecentActions.append("tabno")
                            $ Ch_Focus.DailyActions.append("tabno")
                        $ Ch_Focus.RecentActions.append("no hotdog")
                        $ Ch_Focus.DailyActions.append("no hotdog")
                        return
                "Тебе может понравится. . .":
                        if Approval:
                            $ Ch_Focus.FaceChange("sexy")
                            $ Ch_Focus.Statup("Obed", 60, 2)
                            $ Ch_Focus.Statup("Inbt", 50, 2)
                            $ Line = renpy.random.choice(["Ага, возможно. . .",
                                    "Пожалуй. . .",
                                    "Хорошее замечание. . ."])
                            call AnyLine(Ch_Focus,Line)
                            $ Line = 0
                            jump Girl_HotdogPrep
                        else:
                            pass

                "Просто смирись.":                                               # Pressured into it
                        $ Approval = ApprovalCheck(Ch_Focus, 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                        if Approval > 1 or (Approval and Ch_Focus.Forced):
                            $ Ch_Focus.FaceChange("sad")
                            $ Ch_Focus.Statup("Love", 70, -2, 1)
                            $ Ch_Focus.Statup("Love", 200, -2)
                            call AnyLine(Ch_Focus,"Ладно.")
                            $ Ch_Focus.Statup("Obed", 80, 4)
                            $ Ch_Focus.Statup("Inbt", 60, 2)
                            $ Ch_Focus.Forced = 1
                            jump Girl_HotdogPrep
                        else:
                            $ Ch_Focus.Statup("Love", 200, -10)
                            $ Ch_Focus.RecentActions.append("angry")
                            $ Ch_Focus.DailyActions.append("angry")

    #She refused all offers.
    $ Ch_Focus.ArmPose = 1

    if "no hotdog" in Ch_Focus.DailyActions:
            call Sex_Basic_Dialog(Ch_Focus,"noday") #"Stop asking."
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
    if Ch_Focus.Forced:
            $ Ch_Focus.FaceChange("angry", 1)
            if Ch_Focus is RogueX:
                    ch_r "Не стоит."
            elif Ch_Focus is KittyX:
                    ch_k "Ага, этого не случится."
            elif Ch_Focus is EmmaX:
                    ch_e "Я не вижу в этом никакого смысла."
            elif Ch_Focus is LauraX:
                    ch_l "Можешь больше не пытаться."
            elif Ch_Focus is JeanX:
                    ch_j "Можешь больше не пытаться."
            elif Ch_Focus is StormX:
                    ch_s "Я совсем не понимаю, в чем тут моя выгода."
            elif Ch_Focus is JubesX:
                    ch_v "Определенно нет."
            elif Ch_Focus is GwenX:
                    ch_g "Я просто. . . в чем вообще смысл?"
            elif Ch_Focus is BetsyX:
                    ch_b "Я никак. . . не могу понять, в чем смысл?"
            elif Ch_Focus is DoreenX:
                    ch_d "Я просто. . . не могу?"
            elif Ch_Focus is WandaX:
                    ch_w "Я просто. . . не могу?"
            $ Ch_Focus.Statup("Lust", 200, 5)
            if Ch_Focus.Love > 300:
                    $ Ch_Focus.Statup("Love", 70, -1)
            $ Ch_Focus.Statup("Obed", 50, -1)
            $ Ch_Focus.RecentActions.append("angry")
            $ Ch_Focus.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
            $ Ch_Focus.FaceChange("angry", 1)
            $ Ch_Focus.RecentActions.append("tabno")
            $ Ch_Focus.DailyActions.append("tabno")
            call Sex_Basic_Dialog(Ch_Focus,"tabno") #"You picked a bad place for this. . ."
            $ Ch_Focus.Statup("Lust", 200, 5)
            $ Ch_Focus.Statup("Obed", 50, -3)
    elif Ch_Focus.Hotdog:
            $ Ch_Focus.FaceChange("sad")
            if Ch_Focus is RogueX:
                    ch_r "Кхм, я больше не хочу, [RogueX.Petname]."
            elif Ch_Focus is KittyX:
                    ch_k "Ага, только не снова."
            elif Ch_Focus is EmmaX:
                    ch_e "Не при таких обстоятельствах."
            elif Ch_Focus is LauraX:
                    ch_l "Больше не хочу."
            elif Ch_Focus is JeanX:
                    ch_j "Я больше не хочу."
            elif Ch_Focus is StormX:
                    ch_s "Не при таких обстоятельствах."
            elif Ch_Focus is JubesX:
                    ch_v "Я больше не хочу."
            elif Ch_Focus is GwenX:
                    ch_g "Я больше не хочу."
            elif Ch_Focus is BetsyX:
                    ch_b "Боюсь, что нет."
            elif Ch_Focus is DoreenX:
                    ch_d "Не-а."
            elif Ch_Focus is WandaX:
                    ch_w "Нет."
    else:
            $ Ch_Focus.FaceChange("normal", 1)
            if Ch_Focus is RogueX:
                    ch_r "Ни за что."
            elif Ch_Focus is KittyX:
                    ch_k "Ненене."
            elif Ch_Focus is EmmaX:
                    ch_e "Боюсь, что нет."
            elif Ch_Focus is LauraX:
                    ch_l "Ага, но нет."
            elif Ch_Focus is JeanX:
                    ch_j "Мне не интересно."
            elif Ch_Focus is StormX:
                    ch_s "Я вынуждена отказаться."
            elif Ch_Focus is JubesX:
                    ch_v "Ага, но нет."
            elif Ch_Focus is GwenX:
                    ch_g "Я не могу."
            elif Ch_Focus is BetsyX:
                    ch_b "Я не могу."
            elif Ch_Focus is DoreenX:
                    ch_d "Нет, спасибо, мне и так хорошо."
            elif Ch_Focus is WandaX:
                    ch_w "Нет."
    $ Ch_Focus.RecentActions.append("no hotdog")
    $ Ch_Focus.DailyActions.append("no hotdog")
    $ Tempmod = 0
    return

label Girl_HotdogPrep: #rkeljsvg
    # Modification mode
    if is_playing_music(audio.girl_sex):
        $ play_music(name=audio.girl_sex, loop=True)
    # -----------------

#    #fix remove
#    "Not currently available."
#    return
#    #fix remove
    call Seen_First_Peen(Ch_Focus,Partner,React=Situation)
    call expression Ch_Focus.Tag + "_Sex_Launch" pass ("hotdog")

    if Situation == Ch_Focus:
            #Girl auto-starts
            $ Situation = 0
            if not Player.Male:
                "[Ch_Focus.Name] прижимается к вашему резиновому члену."
            else:
                "[Ch_Focus.Name] прижимается к вашему твердому члену."
            menu:
                "Что будете делать?"
                "Не сопротивляться.":
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
                    ch_p "[Ch_Focus.Pet], давай пока не будем."
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
        call Girl_Initiates(Ch_Focus)      #"She presses against you and your cock pops in."

    else: #if Situation == "auto"
        if not Player.Male:
            "[Ch_Focus.Name] прижимается к вашему резиновому члену."
        else:
            "[Ch_Focus.Name] прижимается к вашему твердому члену."

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
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        $ Ch_Focus.DrainWord("tabno")
    $ Ch_Focus.DrainWord("no hotdog")
    $ Ch_Focus.RecentActions.append("hotdog")
    $ Ch_Focus.DailyActions.append("hotdog")

label Girl_Hotdog_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(Ch_Focus)
        call expression Ch_Focus.Tag + "_Sex_Launch" pass ("hotdog")
        if Speed >= 4:
            $ Speed = 2
#            call Speed_Shift(2)
        $ Ch_Focus.LustFace()
        $ Player.Cock = "out"
        $ Trigger = "hotdog"

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Продолжать. . ." if Speed:
                                    pass
                        "Продолжать. . . (locked)" if not Speed:
                                    pass

                        "Начать? . ." if not Speed:
                                    # Modification mode
                                    if is_playing_music(audio.girl_doggy) and Ch_Focus.Pose == "doggy":
                                        $ play_music(name=audio.girl_doggy, loop=True)
                                    else:
                                        $ play_music(name=audio.girl_sex, loop=True)
                                    # -----------------

                                    $ Speed = 1
#                                    call Speed_Shift(1)
                        "Быстрее. . ." if 0 < Speed < 3:
                                    $ Speed += 1
#                                    call Speed_Shift(Speed+1)
                                    "Вы немного ускоряетесь."
                        "Быстрее. . . (locked)" if Speed >= 3:
                                    pass

                        "Помедленнее. . ." if Speed:
                                    $ Speed -= 1
#                                    call Speed_Shift(Speed-1)
                                    "Вы немного замедляетесь."
                        "Помедленнее. . . (locked)" if not Speed:
                                    pass

                        "Шлепнуть ее по заднице":
                                    call Slap_Ass(Ch_Focus)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump Girl_Hotdog_Cycle

                        "Развернуть ее":
                                    # Modification mode
                                    if is_playing_music(audio.girl_doggy) and Ch_Focus.Pose == "doggy":
                                        $ play_music(name=audio.girl_doggy, loop=True)
                                    else:
                                        $ play_music(name=audio.girl_sex, loop=True)
                                    # -----------------

                                    $ Ch_Focus.Pose = "doggy" if Ch_Focus.Pose != "doggy" else 0
                                    "Вы разворачиваете ее. . ."
                                    call View_Facing(Ch_Focus)
                                    jump Girl_Hotdog_Cycle

                        "Повернуть ее голову" if Ch_Focus.Pose == "doggy":
                                    call View_Facing(Ch_Focus,1)
                                    jump Girl_Hotdog_Cycle

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
                                                        "Как насчет вагинального секса?":
                                                            $ Situation = "shift"
                                                            call Girl_HotdogAfter
                                                            call Girl_Sex_P
                                                        "Просто вставить ей в киску [[не спрашивая].":
                                                            $ Situation = "auto"
                                                            call Girl_HotdogAfter
                                                            call Girl_Sex_P
                                                        "Как насчет в попку?":
                                                            $ Situation = "shift"
                                                            call Girl_HotdogAfter
                                                            call Girl_Sex_A
                                                        "Просто вставить прибор ей в попку [[не спрашивая].":
                                                            $ Situation = "auto"
                                                            call Girl_HotdogAfter
                                                            call Girl_Sex_A
                                                        "Неважно":
                                                                jump Girl_Hotdog_Cycle
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
                                                        jump Girl_Hotdog_Cycle
                                            "Привести в порядок [Partner.Name_vin]":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        jump Girl_Hotdog_Cycle
                                            "Неважно":
                                                        jump Girl_Hotdog_Cycle
                                    "Просто посмотреть на нее.":
                                            $ Player.Cock = 0
                                            $ Speed = 0

                                    "Показывать ее ноги" if not ShowFeet:# and Ch_Focus.Pose == "doggy":
                                            $ ShowFeet = 1
                                    "Спрятать ее ноги" if ShowFeet:# and Ch_Focus.Pose == "doggy":
                                            $ ShowFeet = 0

                                    "Вставить анальную пробку" if not Ch_Focus.Plug and "plug" in Ch_Focus.Inventory:
                                            call Insert_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку" if Ch_Focus.Plug:
                                            call Remove_Anal_Plug(Ch_Focus)
                                    "Убрать анальную пробку (locked)" if "plug" not in Ch_Focus.Inventory:
                                            pass

                                    "Псионический Нож" if Ch_Focus is BetsyX and "knife" in BetsyX.History:
                                            call Betsy_Psyknife

                                    "Раздеть [Ch_Focus.Name_vin]":
                                            call Girl_Undress(Ch_Focus)
                                    "Привести в порядок [Ch_Focus.Name_vin] (locked)" if not Ch_Focus.Spunk:
                                            pass
                                    "Привести в порядок [Ch_Focus.Name_vin]" if Ch_Focus.Spunk:
                                            call Girl_Cleanup(Ch_Focus,"ask")
                                    "Неважно":
                                            jump Girl_Hotdog_Cycle

                        "Вернуться к Секс-меню" if MultiAction:
                                    ch_p "Думаю, нам стоит попробовать что-нибудь другое."
                                    call expression Ch_Focus.Tag + "_Sex_Reset"
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Girl_HotdogAfter
                        "Закончить" if not MultiAction:
                                    ch_p "Думаю, нам стоит пока остановиться."
                                    call expression Ch_Focus.Tag + "_Sex_Reset"
                                    $ Line = 0
                                    jump Girl_HotdogAfter
        #End menu (if Line)

        call Shift_Focus(Ch_Focus)
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
                                call expression Ch_Focus.Tag + "_Sex_Reset"
                                return
                            $ Ch_Focus.Statup("Lust", 200, 5)
                            if 100 > Ch_Focus.Lust >= 70 and Ch_Focus.OCount < 2:
                                    $ Ch_Focus.RecentActions.append("unsatisfied")
                                    $ Ch_Focus.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Girl_HotdogAfter
                            $ Line = "came"

                    if Ch_Focus.Lust >= 100:
                            #If you're still going at it and Girl can cum
                            call Girl_Cumming(Ch_Focus)
                            if Situation == "shift" or "angry" in Ch_Focus.RecentActions:
                                jump Girl_HotdogAfter

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                if Player.Male:
                                        "Она выжала из вас все соки, вам нужно передохнуть."
                                else:
                                        "Она вас утомила, вам нужно передохнуть."
                                jump Girl_HotdogAfter
                            elif "unsatisfied" in Ch_Focus.RecentActions:
                                #And Ch_Focus is unsatisfied,
                                $ Line = renpy.random.choice(["Она продолжает слегка дрожать от удовольствия.",
                                    "Она тяжело дышит, пока вы ее трахаете.",
                                    "Она медленно поворачивается к вам и улыбается.",
                                    "Кажется, она не собирается останавливаться."])
                                "[Line] Продолжите?"
                                menu:
                                    extend ""
                                    "Да. Продолжим еще немного." if Player.Semen:
                                        $ Line = "Вы возвращаетесь к процессу"
                                        jump Girl_Hotdog_Cycle
                                    "С меня хватит." if Player.Semen:
                                        "Вы заканчиваете веселье."
                                        jump Girl_HotdogAfter
                                    "Нет, у меня нет сил." if not Player.Semen:
                                        "Вы заканчиваете веселье."
                                        jump Girl_HotdogAfter
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if Ch_Focus.SEXP >= 100 or ApprovalCheck(Ch_Focus, 1200, "LO"):
            pass
        elif Cnt == (5 + Ch_Focus.Hotdog):
                    $ Ch_Focus.Brows = "confused"
                    if Ch_Focus is RogueX:
                            ch_r "Ты уже скоро?"
                    elif Ch_Focus is KittyX:
                            ch_k "Ты уже скоро?"
                    elif Ch_Focus is EmmaX:
                            ch_e "Ты уже скоро?"
                    elif Ch_Focus is LauraX:
                            ch_l "Ты уже скоро?"
                    elif Ch_Focus is JeanX:
                            ch_j "Ты собираешься заканчивать?"
                    elif Ch_Focus is StormX:
                            if not Player.Male:
                                ch_s "Ты еще не удовлетворена?"
                            else:
                                ch_s "Ты еще не удовлетворен?"
                    elif Ch_Focus is JubesX:
                            if not Player.Male:
                                ch_v "Ты хоть немного довольна?"
                            else:
                                ch_v "Ты хоть немного доволен?"
                    elif Ch_Focus is GwenX:
                            if not Player.Male:
                                ch_g "Ну. . . эм. . . ты довольна?"
                            else:
                                ch_g "Ну. . . эм. . . ты доволен?"
                    elif Ch_Focus is BetsyX:
                            ch_b "Это. . . эм. . . соответствует твоим ожиданиям?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Так. . . эм. . . тебе нравится?"
                    elif Ch_Focus is WandaX:
                            ch_w "Итак. . . эм. . . тебе нравится?"
        elif Cnt == (10 + Ch_Focus.Hotdog):
                    $ Ch_Focus.Brows = "angry"
                    if Ch_Focus is RogueX:
                            ch_r "[RogueX.Petname], думаю, с меня этого хватит."
                    elif Ch_Focus is KittyX:
                            ch_k "Я уже начинаю скучать."
                    elif Ch_Focus is EmmaX:
                            ch_e "Мне уже это надоело."
                    elif Ch_Focus is LauraX:
                            ch_l "Мне скучно."
                    elif Ch_Focus is JeanX:
                            ch_j "Ну, уже не весело."
                    elif Ch_Focus is StormX:
                            ch_s "Я потихоньку начинаю уставать."
                    elif Ch_Focus is JubesX:
                            ch_v "Мне как-то скучновато."
                    elif Ch_Focus is GwenX:
                            ch_g "Я, эм. . . хочу заняться чем-нибудь другим."
                    elif Ch_Focus is BetsyX:
                            ch_b "Возможно, нам стоит заняться чем-нибудь другим?"
                    elif Ch_Focus is DoreenX:
                            ch_d "Я, эм. . . мы можем заняться чем-нибудь другим?"
                    elif Ch_Focus is WandaX:
                            ch_w "Послушай, может, нам стоит заняться чем-нибудь другим?"
                    menu:
                        extend ""
                        "Как насчет отсоса?" if Ch_Focus.Action and MultiAction and Player.Male:
                                $ Situation = "shift"
                                call Girl_HotdogAfter
                                call Girl_Blowjob
                        "Как насчет вылизать мою киску?" if Ch_Focus.Action and MultiAction and not Player.Male:
                                $ Situation = "shift"
                                call Girl_HotdogAfter
                                call Girl_CUN
                        "Закончить." if Player.FocusX:
                                "Вы расслабляетесь. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                jump Girl_Hotdog_Cycle
                        "Давай попробуем что-нибудь другое." if MultiAction:
                                $ Line = 0
                                call expression Ch_Focus.Tag + "_Sex_Reset"
                                $ Situation = "shift"
                                jump Girl_HotdogAfter
                        "Нет, давай за работу.":
                                if ApprovalCheck(Ch_Focus, 1200) or ApprovalCheck(Ch_Focus, 500, "O"):
                                    $ Ch_Focus.Statup("Love", 200, -5)
                                    $ Ch_Focus.Statup("Obed", 50, 3)
                                    $ Ch_Focus.Statup("Obed", 80, 2)
                                    "Она ворчит, но продолжает."
                                else:
                                    $ Ch_Focus.FaceChange("angry", 1)
                                    call expression Ch_Focus.Tag + "_Sex_Reset"
                                    "Она сердито смотрит на вас и отстраняется."
                                    if Ch_Focus is RogueX:
                                            ch_r "С таким отношением, ты и без меня отлично справишься."
                                    elif Ch_Focus is KittyX:
                                            ch_k "Не с таким отношением!"
                                    elif Ch_Focus is EmmaX:
                                            ch_e "Я так не думаю."
                                    elif Ch_Focus is LauraX:
                                            ch_l "Не с таким отношением."
                                    elif Ch_Focus is JeanX:
                                            ch_j "Не переоценивай себя."
                                    elif Ch_Focus is StormX:
                                            ch_s "Нет, я так не думаю."
                                    elif Ch_Focus is JubesX:
                                            ch_v "Точно не сейчас."
                                    elif Ch_Focus is GwenX:
                                            ch_g "Хорошо, тогда мы закончили."
                                    elif Ch_Focus is BetsyX:
                                            ch_b "Что ж, тогда мы закончили."
                                    elif Ch_Focus is DoreenX:
                                            ch_d "Ну, мы так точно не договаривались!"
                                    elif Ch_Focus is WandaX:
                                            ch_w "Ладно, игры кончились!"
                                    $ Ch_Focus.Statup("Love", 50, -3, 1)
                                    $ Ch_Focus.Statup("Love", 80, -4, 1)
                                    $ Ch_Focus.Statup("Obed", 30, -1, 1)
                                    $ Ch_Focus.Statup("Obed", 50, -1, 1)
                                    $ Ch_Focus.RecentActions.append("angry")
                                    $ Ch_Focus.DailyActions.append("angry")
                                    jump Girl_HotdogAfter
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

label Girl_HotdogAfter:
    # Modification mode
    $ play_music()
    $ play_sound()
    # -----------------

    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        call expression Ch_Focus.Tag + "_Sex_Reset"

    $ Ch_Focus.FaceChange("sexy")

    $ Ch_Focus.Hotdog += 1
    $ Ch_Focus.Action -=1
    if Player.Male:
            $ Ch_Focus.Addictionrate += 1
            if "addictive" in Player.Traits:
                $ Ch_Focus.Addictionrate += 1
    $ Ch_Focus.Statup("Inbt", 30, 1)
    $ Ch_Focus.Statup("Inbt", 70, 1)

    call Partner_Like(Ch_Focus,2)

    if Ch_Focus.Hotdog == 10:
        $ Ch_Focus.SEXP += 5
    elif Ch_Focus.Hotdog == 1:
            $Ch_Focus.SEXP += 10
            if not Situation:
                if Ch_Focus.Love >= 500 and "unsatisfied" not in Ch_Focus.RecentActions:
                        if Ch_Focus is RogueX:
                                ch_r "Меня заводят даже мысли об этом, [RogueX.Petname], нам нужно будет как-нибудь повторить."
                        elif Ch_Focus is KittyX:
                                ch_k "Мне. . . очень понравилось."
                        elif Ch_Focus is EmmaX:
                                ch_e "Это было. . . очень приятно."
                        elif Ch_Focus is LauraX:
                                ch_l "Это было. . . приятно."
                        elif Ch_Focus is JeanX:
                                ch_j "Ладно, это было. . . неплохо."
                        elif Ch_Focus is StormX:
                                ch_s "Это было. . . очень приятно."
                        elif Ch_Focus is JubesX:
                                ch_v "Это было. . . весело."
                        elif Ch_Focus is GwenX:
                                ch_g "Это было. . . здорово."
                        elif Ch_Focus is BetsyX:
                                ch_b "Это было. . . весьма весело."
                        elif Ch_Focus is DoreenX:
                                ch_d "Это было. . . здорово."
                        elif Ch_Focus is WandaX:
                                ch_w "Это было довольно весело."
                elif Ch_Focus.Obed <= 500 and Player.Focus <= 20:
                        $ Ch_Focus.Mouth = "sad"
                        if Ch_Focus is RogueX:
                                if not Player.Male:
                                    ch_r "Ты получила то, что тебе было нужно?"
                                else:
                                    ch_r "Ты получил то, что тебе было нужно?"
                        elif Ch_Focus is KittyX:
                                if not Player.Male:
                                    ch_k "Ну, ты довольна?"
                                else:
                                    ch_k "Ну, ты доволен?"
                        elif Ch_Focus is EmmaX:
                                if not Player.Male:
                                    ch_e "Ты удовлетворена?"
                                else:
                                    ch_e "Ты удовлетворен?"
                        elif Ch_Focus is LauraX:
                                if not Player.Male:
                                    ch_l "Ты довольна?"
                                else:
                                    ch_l "Ты доволен?"
                        elif Ch_Focus is JeanX:
                                ch_j "Наверное, могло быть и хуже. . ."
                        elif Ch_Focus is StormX:
                                ch_s "Тебе понравилось?"
                        elif Ch_Focus is JubesX:
                                ch_v "Тебе понравилось?"
                        elif Ch_Focus is GwenX:
                                if not Player.Male:
                                    ch_g "Ты довольна?"
                                else:
                                    ch_g "Ты доволен?"
                        elif Ch_Focus is BetsyX:
                                ch_b "Тебе этого достаточно?"
                        elif Ch_Focus is DoreenX:
                                ch_d "Я делала все правильно?"
                        elif Ch_Focus is WandaX:
                                ch_w "Ну как?"
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        if "unsatisfied" in Ch_Focus.RecentActions:
            $ Ch_Focus.FaceChange("angry")
            $ Ch_Focus.Eyes = "side"
            if Ch_Focus is RogueX:
                    ch_r "Я не получила от процесса ничего хорошего. . ."
            elif Ch_Focus is KittyX:
                    if not Player.Male:
                        ch_k "Не могла бы ты уделить мне больше внимания? . ."
                    else:
                        ch_k "Не мог бы ты уделить мне больше внимания? . ."
            elif Ch_Focus is EmmaX:
                    if not Player.Male:
                        ch_e "Не могла бы ты быть более внимательной? . ."
                    else:
                        ch_e "Не мог бы ты быть более внимательным? . ."
            elif Ch_Focus is LauraX:
                    if not Player.Male:
                        ch_l "Ничего не забыла? . ."
                    else:
                        ch_l "Ничего не забыл? . ."
            elif Ch_Focus is JeanX:
                    ch_j "Думаю, тебе нужно продолжить."
            elif Ch_Focus is StormX:
                    ch_s "Мне бы не помешало больше внимания к моим потребностям. . ."
            elif Ch_Focus is JubesX:
                    if not Player.Male:
                        ch_v "Знаешь, ты могла бы стараться и лучше. . ."
                    else:
                        ch_v "Знаешь, ты мог бы стараться и лучше. . ."
            elif Ch_Focus is GwenX:
                    ch_g "Эй! Разве ты не собираешься \"покончить со мной?\""
            elif Ch_Focus is BetsyX:
                    ch_b "Не думаешь, что тебе нужно кое с чем закончить?"
            elif Ch_Focus is DoreenX:
                    ch_d "Так и планировалось, что я. . . эм. . . не смогу. . ."
                    ch_d "\"Кончить?\""
            elif Ch_Focus is WandaX:
                    ch_w "Послушай, мне бы не помешало больше внимания."

    $ Tempmod = 0
#    if Situation == "shift":
#        ch_d "Mmm, so what else did you have in mind?"
    call Checkout
    return

# End Girl hotdogging //////////////////////////////////////////////////////////////////////////////////
