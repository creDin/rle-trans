
# start WandaMeet//////////////////////////////////////////////////////////

#        if WandaX in ActiveGirls:
#                    if "switchcheck" in WandaX.Traits:
#                            pass
#                    elif "witch" not in WandaX.History and ApprovalCheck(WandaX, 1200) and WandaX.Loc == bg_current:
#                            #Shows off MCU costume
#                            call Wanda_Witch
#                            return

#        elif "met" not in WandaX.History and "met" in BetsyX.History:
#                    elif bg_current != "bg classroom" and Time_Count == 1 and "Intro" not in Player.DailyActions:
#                            #You hadn't asked Wanda yet
#                            call WandaMeet
#                            jump Misplaced

label WandaMeet:
        #set-up
        $ Situation = bg_current
        $ bg_current = "bg campus"
        $ WandaX.OutfitDay = "casual1"
        $ WandaX.Outfit = "casual1"
        $ WandaX.OutfitChange("casual1")
        call CleartheRoom("All",0,1)
        $ WandaX.Love = 300
        $ WandaX.Obed = 0
        $ WandaX.Inbt = 200
        if not Player.Male:
            $ WandaX.Petname = "сис"
            $ WandaX.Petname_rod = "сис"
            $ WandaX.Petname_dat = "сис"
            $ WandaX.Petname_vin = "сис"
            $ WandaX.Petname_tvo = "сис"
            $ WandaX.Petname_pre = "сис"
        else:
            $ WandaX.Petname = "бро"
            $ WandaX.Petname_rod = "бро"
            $ WandaX.Petname_dat = "бро"
            $ WandaX.Petname_vin = "бро"
            $ WandaX.Petname_tvo = "бро"
            $ WandaX.Petname_pre = "бро"
        $ WandaX.Names = ["Wanda"]
        $ WandaX.Name = "? ? ?"
        $ WandaX.Name_rod = "? ? ?"
        $ WandaX.Name_dat = "? ? ?"
        $ WandaX.Name_vin = "? ? ?"
        $ WandaX.Name_tvo = "? ? ?"
        $ WandaX.Name_pre = "? ? ?"
        call Shift_Focus(WandaX)
        $ WandaX.Loc = "hold"
        $ WandaX.SpriteLoc = StageCenter
        call Set_The_Scene
        if "Wanda" not in GwenX.History:
                $ GwenX.History.append("Wanda")

        #start
        "Пока вы идете, раздается какой-то свист, а затем-"
        show blackscreen onlayer black with dissolve
        "Все у вас перед глазами погружается во тьму."
        ". . ."
        ch_w "Ой, ты в порядке [[Ориг. Whoa, are you ok]?"
        $ Count = 4
        while Count > 0:
            #"knocked out" loop, ends after four turns or when you wake up
            menu:
                extend ""
                ". . .":
                        if Count == 4:
                            ch_w "Эй?"
                        elif Count == 3:
                            ch_w ". . . Эй?!"
                        elif Count == 2:
                            $ WandaX.Statup("Obed", 200, 1)
                            $ WandaX.Statup("Inbt", 200, -1)
                            ch_w "Блин, еще обвинения в убийстве мне не хватало. . ."
                        else:
                            ch_w "-Очнись!-"
                            "Она начинает трясти вас изо всех сил."
                        $ Count -= 1
                ". . . Ага.":
                        $ WandaX.Statup("Love", 200, 1)
                        $ WandaX.Statup("Inbt", 200, 1)
                        if Count == 1:
                                ch_w "Слава богу."
                        else:
                                ch_w "Ох. . . ну и хорошо."
                        $ Count = 0
                ". . . Что меня ударило?":
                        ch_w "О. . . это. . ."
                        ch_w "Эм. . . думаю, это была белка-летяга!"
                        $ WandaX.RecentActions.append("squirrel")
                        $ Count = 0
                "Бастер. . . вулф. [[{a=https://youtu.be/XsCRYrOVT9A?t=111}Buster Wolf{/a}]" if "buster" not in WandaX.RecentActions:
                        ch_w "Черт, должно быть, удар был сильнее, чем я думала. . ."
                        $ WandaX.RecentActions.append("buster")
                        $ Count = 2 if Count >= 2 else Count
            #end "knocked out" loop
        $ WandaX.Loc = "bg campus"
        $ WandaX.SpriteLoc = StageCenter
        call Set_The_Scene
        hide blackscreen onlayer black
        "Вы открываете глаза и видите перед собой девушку."
        $ WandaX.FaceChange("smile",2)
        ch_w ". . . привет."
        "Вы также видите что-то похожее на крышку канализационного люка, лежащее примерно в паре метров от вас."
        $ Count = 2
        while Count > 0:
            #"what hit me" loop ends when you respond twice
            menu:
                extend ""
                ". . . Что меня ударило?" if "squirrel" not in WandaX.RecentActions:
                        $ WandaX.FaceChange("smile",2,Eyes="side")
                        ch_w "О. . . это. . ."
                        $ WandaX.FaceChange("smile",1)
                        ch_w "Эм. . . думаю, это была белка-летяга!"
                        $ WandaX.RecentActions.append("squirrel")
                ". . .":
                        if "squirrel" in WandaX.RecentActions:
                                ch_w "Хехе. . ."
                        else:
                                ch_w "Ох, ого, ты видел, как быстро эта белка пролетела?"
                                $ WandaX.RecentActions.append("squirrel")

                "Ты уверена, что это была не крышка люка?" if "squirrel" in WandaX.RecentActions:
                        $ WandaX.Statup("Love", 200, 3)
                        $ WandaX.Statup("Obed", 200, 5)
                        $ WandaX.FaceChange("sadside",2,Mouth="smile")
                        ch_w "Ну. . ."
                        $ Count = 1
                ". . . О, ну ладно." if "squirrel" in WandaX.RecentActions:
                        $ WandaX.Statup("Obed", 200, -2)
                        $ WandaX.Statup("Inbt", 200, 4)
                        $ WandaX.FaceChange("surprised",1,Mouth="side")
                        ch_w "Ты поверил?"
                        $ WandaX.FaceChange("smirk",1,Eyes="side")
                        if not Player.Male:
                            ch_w ". . . [[возможно, ей досталось сильнее, чем я думала. . .]"
                        else:
                            ch_w ". . . [[возможно, ему досталось сильнее, чем я думала. . .]"
            $ Count -= 1
            #end "what hit me" loop
        $ WandaX.FaceChange("smile",2,Eyes="side")
        ch_w "Хорошо, это сделала я."
        $ WandaX.FaceChange("smile",1,Brows="sad")
        ch_w "Это произошло случайно, ясно?"
        ch_w "Мои силы иногда выходят из-под контроля."
        $ WandaX.FaceChange("sadside",2,Mouth="smile")
        ch_w "-самую малость."
        $ Count = 5
        while Count > 0:
            #"Q&A" loop ends after all questions out or manually
            $ Count -= 1
            menu:
                extend ""
                "Какие силы?" if "powers" not in WandaX.RecentActions:
                        $ WandaX.Statup("Obed", 200, 2)
                        $ WandaX.Statup("Inbt", 200, 1)
                        call Wanda_Scene_Powers
                "Я могу отключать силы других мутантов." if "zero" not in WandaX.RecentActions:
                        $ WandaX.Statup("Love", 200, 2)
                        call Wanda_Scene_Zero_Powers
                "Я [Player.Name]." if  WandaX.Petname != Player.Name and WandaX.Petname != "Вижн" and WandaX.Name != "Ванда":
                        $ WandaX.Petname = Player.Name
                        $ WandaX.Petname_rod = Player.Name_rod
                        $ WandaX.Petname_dat = Player.Name_dat
                        $ WandaX.Petname_vin = Player.Name_vin
                        $ WandaX.Petname_tvo = Player.Name_tvo
                        $ WandaX.Petname_pre = Player.Name_pre
                        $ WandaX.Statup("Love", 50, 4)
                        $ WandaX.Statup("Love", 200, 1)
                        $ WandaX.Statup("Obed", 200, 1)
                        $ WandaX.FaceChange("smile",1)
                        ch_w "О, поняла. . . А я Ванда. Ванда Максимофф."
                        $ WandaX.Name = "Ванда"
                        $ WandaX.Name_rod = "Ванды"
                        $ WandaX.Name_dat = "Ванде"
                        $ WandaX.Name_vin = "Ванду"
                        $ WandaX.Name_tvo = "Вандой"
                        $ WandaX.Name_pre = "Ванде"
                "Кто ты?" if WandaX.Name != "Ванда":
                        $ WandaX.Statup("Love", 200, -1)
                        $ WandaX.Statup("Obed", 200, 4)
                        $ WandaX.FaceChange("smile",1)
                        ch_w "О. . . эм. . . Меня зовут Ванда. Ванда Максимофф."
                        $ WandaX.Name = "Ванда"
                        $ WandaX.Name_rod = "Ванды"
                        $ WandaX.Name_dat = "Ванде"
                        $ WandaX.Name_vin = "Ванду"
                        $ WandaX.Name_tvo = "Вандой"
                        $ WandaX.Name_pre = "Ванде"
                        ch_w "А тебя как зовут?"
                        menu:
                            extend ""
                            "Я [Player.Name]":
                                    $ WandaX.Statup("Love", 200, 4)
                                    $ WandaX.Petname = Player.Name
                                    $ WandaX.Petname_rod = Player.Name_rod
                                    $ WandaX.Petname_dat = Player.Name_dat
                                    $ WandaX.Petname_vin = Player.Name_vin
                                    $ WandaX.Petname_tvo = Player.Name_tvo
                                    $ WandaX.Petname_pre = Player.Name_pre
                            ". . .":
                                    $ WandaX.Statup("Obed", 200, 1)
                                    $ WandaX.FaceChange("perplexed",1)
                            "Не твое дело.":
                                    $ WandaX.Statup("Love", 200, -3)
                                    $ WandaX.Statup("Obed", 200, 3)
                                    $ WandaX.FaceChange("angry",1)
                            "Можешь звать меня. . . \"Вижн.\"":
                                    $ WandaX.Statup("Love", 200, 4)
                                    $ WandaX.FaceChange("smile",1)
                                    $ WandaX.Petname = "Вижн"
                                    $ WandaX.Petname_rod = "Вижн"
                                    $ WandaX.Petname_dat = "Вижн"
                                    $ WandaX.Petname_vin = "Вижн"
                                    $ WandaX.Petname_tvo = "Вижн"
                                    $ WandaX.Petname_pre = "Вижн"
                                    $ WandaX.Petnames.append("Vision")
                        ch_w "Ну, наверное, приятно познакомиться."
                "И зачем ты здесь?" if "jail" not in WandaX.RecentActions:
                        $ WandaX.Statup("Love", 200, 1)
                        $ WandaX.Statup("Obed", 200, 1)
                        $ WandaX.Statup("Inbt", 200, 1)
                        $ WandaX.FaceChange("smile",1)
                        ch_w "О. . . ну, эм, меня сюда пригласили."
                        ch_w "Видишь ли. . ."
                        call Wanda_Scene_Jail
                "Мне пора.":
                        $ WandaX.Statup("Love", 200, 1)
                        $ WandaX.Statup("Obed", 200, 1)
                        $ WandaX.Statup("Inbt", 200, 1)
                        $ WandaX.FaceChange("smile",1)
                        if Count >= 2:
                            #you asked several questions
                            ch_w "Ага, конечно."
                        else:
                            ch_w "Ох. Ладно."
                        $ Count = 0
            #end "Q&A" loop

        if "powers" not in WandaX.RecentActions:
            ch_w "В общем, мои силы слегка вышли из-под контроля, прости."
            call Wanda_Scene_Powers


        $ RogueX.Loc = "bg campus"
        $ RogueX.SpriteLoc = StageRight
        call Set_The_Scene
        #finale, Rogue shows up to fill gaps
        if ApprovalCheck(RogueX, 1200) and RogueX.SEXP >= 10:
                    $ RogueX.FaceChange("smile",1)
                    $ WandaX.FaceChange("surprised",1)
                    "[RogueX.Name] проходит мимо и целует вас в щеку."
                    ch_r "Привет, [RogueX.Petname]. . . Привет, Ванда. . ."
                    $ WandaX.Name = "Ванда"
                    $ WandaX.Name_rod = "Ванды"
                    $ WandaX.Name_dat = "Ванде"
                    $ WandaX.Name_vin = "Ванду"
                    $ WandaX.Name_tvo = "Вандой"
                    $ WandaX.Name_pre = "Ванде"
                    $ RogueX.FaceChange("sly",1)
                    $ WandaX.FaceChange("sly",1,Eyes="leftside")
                    ch_r "Будь с ней осторожнее."
        else:
                    $ RogueX.FaceChange("sly",1)
                    "[RogueX.Name] проходит мимо и дает вам легкий подзатыльник."
                    $ RogueX.FaceChange("angry",1,Eyes="side")
                    $ WandaX.FaceChange("sly",1,Eyes="leftside")
                    ch_r "Слушай, [RogueX.Petname], тебе следует быть с ней осторожнее."
        ch_r "У нее. . . богатое прошлое. . ."
        menu:
            "Ты, наверное, про то, что она была за решеткой? Ага, она рассказывала." if "jail" in WandaX.RecentActions:
                    $ WandaX.Statup("Love", 200, 5)
                    $ WandaX.Statup("Obed", 200, 2)
                    $ WandaX.FaceChange("sly",1)
                    $ RogueX.Statup("Obed", 50, 2)
                    $ RogueX.FaceChange("sadside",2)
                    ch_r "О, вот как. Хм."
            "Что она сделала?":
                    $ WandaX.Statup("Love", 200, 2)
                    $ WandaX.Statup("Inbt", 200, 3)
                    $ WandaX.FaceChange("sly",1)
                    $ RogueX.Statup("Love", 90, 2)
                    $ RogueX.Statup("Obed", 50, 2)
                    $ RogueX.FaceChange("surprised",1)
                    ch_r "О, много всего."
                    $ RogueX.FaceChange("sly",1)
            "Пикантное?":
                    $ WandaX.Statup("Love", 200, 2)
                    $ WandaX.Statup("Obed", 200, 2)
                    $ WandaX.Statup("Inbt", 200, 3)
                    $ WandaX.FaceChange("sly",1)
                    $ RogueX.Statup("Inbt", 70, 3)
                    $ RogueX.FaceChange("sadside",2)
                    ch_r "Хех, еще какое. . . ну, думаю, не мне об этом рассказывать."
                    $ WandaX.FaceChange("smile",1,Eyes="leftside")
                    ch_r "Я не уверена, что из этого правда, а что лишь слухи. . ."
                    $ RogueX.FaceChange("sly",1)
                    $ WandaX.FaceChange("angry",1,Eyes="leftside")
                    ch_r "Но напакостничала она знатно."
            "Ясно.":
                    $ WandaX.Statup("Love", 200, 4)
                    $ WandaX.Statup("Obed", 200, 2)
                    $ WandaX.Statup("Inbt", 200, 1)
                    $ WandaX.FaceChange("smile",1)
                    $ RogueX.Statup("Love", 90, -2)
                    $ RogueX.FaceChange("sadside",2)
                    ch_r "Я серьезно, [RogueX.Petname]!"

        if "jail" not in WandaX.RecentActions:
                $ WandaX.FaceChange("angry",1,Eyes="leftside")
                $ RogueX.FaceChange("sly",1,Eyes="side")
                ch_r "Эта маленькая ведьма натворила тут всякого."
                ch_w "Эй!"
                ch_w "Не говори обо мне гадостей, болотная крыса!"
                $ WandaX.FaceChange("sadside",2)
                ch_w ". . ."
                ch_w "Послушайте, все сложно."
                call Wanda_Scene_Jail
                $ WandaX.FaceChange("sly",1,Eyes="leftside")
                $ RogueX.FaceChange("sly",1,Eyes="side")
                ch_r "Полагаю, тогда прошлое можно оставить в прошлом, верно?"


        if "zero" not in WandaX.RecentActions:
                #if you haven't told her about your powers.
                $ WandaX.FaceChange("surprised",1)
                $ RogueX.FaceChange("sly",1,Eyes="side")
                if not Player.Male:
                    ch_w ". . . Так, секундочку, она же тебя коснулась. Почему ты не. . . упала?"
                else:
                    ch_w ". . . Так, секундочку, она же тебя коснулась. Почему ты не. . . упал?"
                menu:
                    extend ""
                    "Я могу отключать силы других мутантов.":
                            call Wanda_Scene_Zero_Powers
                    "Секрет. . .":
                            $ WandaX.FaceChange("surprised",1)
                            $ RogueX.FaceChange("normal",1,Eyes="side")
                            if not Player.Male:
                                ch_r "О, она может отключать силы других мута-"
                            else:
                                ch_r "О, он может отключать силы других мута-"
                            $ RogueX.FaceChange("sad",2,Mouth="smile")
                            ch_r "Эм. . . упс."
                            $ RogueX.FaceChange("sly",1)
                            if not Player.Male:
                                ch_r "Извини, [RogueX.Petname], если ты хотела, чтобы это осталось тайной. . ."
                            else:
                                ch_r "Извини, [RogueX.Petname], если ты хотел, чтобы это осталось тайной. . ."
                            $ RogueX.FaceChange("smile",1)
                            call Wanda_Scene_Zero_Powers
                    ". . .":
                            $ WandaX.FaceChange("surprised",1)
                            $ RogueX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_r "О, она может отключать силы других мутантов."
                            else:
                                ch_r "О, он может отключать силы других мутантов."
                            $ RogueX.FaceChange("sly",1)
                            call Wanda_Scene_Zero_Powers
        $ RogueX.FaceChange("sly",1,Eyes="side")
        ch_r "Мне пора. Ванда, [Player.Name], увидимся позже."
        $ WandaX.FaceChange("sly",1,Eyes="leftside")
        ch_w "Ага, пока, Роуг. . ."
        $ RogueX.FaceChange("sly",1)
        $ RogueX.Loc = "bg rogue"
        hide Rogue_Sprite

        if WandaX.Petname == "Вижн":
                $ WandaX.Statup("Love", 200, -7)
                $ WandaX.Statup("Obed", 200, 1)
                $ WandaX.FaceChange("surprised",1,Brows="angry")
                ch_w "Так, погоди!"
                if not Player.Male:
                    ch_w "Ты сказала, что тебя зовут \"Вижн?\""
                else:
                    ch_w "Ты сказал, что тебя зовут \"Вижн?\""
                menu:
                    extend ""
                    "Извини, просто пошутила." if not Player.Male:
                            $ WandaX.Statup("Love", 200, 5)
                            $ WandaX.Statup("Obed", 200, 1)
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Думаю, я это заслужила."
                    "Извини, просто пошутил." if Player.Male:
                            $ WandaX.Statup("Love", 200, 5)
                            $ WandaX.Statup("Obed", 200, 1)
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Думаю, я это заслужила."
                    "[[пожать плечами]":
                            $ WandaX.Statup("Obed", 200, 5)
                            $ WandaX.FaceChange("perplexed",1)
                            ch_w "Ну и?"
                    ". . .":
                            $ WandaX.Statup("Love", 200, -2)
                            $ WandaX.Statup("Obed", 200, 2)
                            $ WandaX.FaceChange("perplexed",1)
                            ch_w "Ну и?"
                    "Мне просто хотелось посмотреть на твою реакцию. . .":
                            $ WandaX.Statup("Love", 200, 5)
                            $ WandaX.Statup("Inbt", 200, 1)
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Хех, правда. . ?"
                menu:
                    extend ""
                    "Меня зовут [Player.Name].":
                            $ WandaX.Statup("Love", 200, 4)
                            $ WandaX.FaceChange("smile",1)
                            ch_w "Ага, приятно познакомиться, [Player.Name]."
                            $ WandaX.Petname = Player.Name
                            $ WandaX.Petname_rod = Player.Name_rod
                            $ WandaX.Petname_dat = Player.Name_dat
                            $ WandaX.Petname_vin = Player.Name_vin
                            $ WandaX.Petname_tvo = Player.Name_tvo
                            $ WandaX.Petname_pre = Player.Name_pre
                    ". . .":
                            $ WandaX.Statup("Love", 200, 2)
                            $ WandaX.Statup("Obed", 200, 3)
                            $ WandaX.FaceChange("sly",1)
                            if not Player.Male:
                                ch_w "Как хочешь, \"таинственная дева.\""
                            else:
                                ch_w "Как хочешь, \"таинственный парень.\""
                            $ WandaX.Petname = Player.Name
                            $ WandaX.Petname_rod = Player.Name_rod
                            $ WandaX.Petname_dat = Player.Name_dat
                            $ WandaX.Petname_vin = Player.Name_vin
                            $ WandaX.Petname_tvo = Player.Name_tvo
                            $ WandaX.Petname_pre = Player.Name_pre
                    "Если хочешь, можешь звать меня \"Вижн\". . .":
                            $ WandaX.Statup("Love", 200, 5)
                            $ WandaX.Statup("Obed", 200, 3)
                            $ WandaX.Statup("Inbt", 200, 1)
                            $ WandaX.FaceChange("sly",1)
                            ch_w "Хех, может, так и поступлю."
        elif WandaX.Petname != Player.Name:
                $ WandaX.Petname = Player.Name
                $ WandaX.Petname_rod = Player.Name_rod
                $ WandaX.Petname_dat = Player.Name_dat
                $ WandaX.Petname_vin = Player.Name_vin
                $ WandaX.Petname_tvo = Player.Name_tvo
                $ WandaX.Petname_pre = Player.Name_pre
                $ WandaX.FaceChange("sly",1)
                ch_w "Значит, тебя зовут [Player.Name], да?"
                ch_w "Я Ванда Максимофф, приятно познакомиться."
                $ WandaX.Name = "Ванда"
                $ WandaX.Name_rod = "Ванды"
                $ WandaX.Name_dat = "Ванде"
                $ WandaX.Name_vin = "Ванду"
                $ WandaX.Name_tvo = "Вандой"
                $ WandaX.Name_pre = "Ванде"
        $ WandaX.FaceChange("sly",1)
        $ WandaX.Loc = "bg wanda"
        hide Wanda_Sprite
        "Ванда уходит, а вы продолжаете свой путь в противоположную сторону."
        $ WandaX.AddWord(1,0,0,0,"met") #adds "word" tag to History
        $ ActiveGirls.append(WandaX) if WandaX not in ActiveGirls else ActiveGirls
        $ bg_current = Situation
        jump Misplaced
        #end main scene


label Wanda_Scene_Powers:
        #called when you ask about her powers
        $ WandaX.RecentActions.append("powers")
        $ WandaX.FaceChange("smile",1)
        ch_w "Они подобны хаосу."
        ch_w "Когда я их активирую, вокруг начинают летать предметы, мне сложно их контролировать."
        ch_w "Но в последнее время у меня более или менее получается."
        $ WandaX.FaceChange("sly",1)
        ch_w "Правда, не всегда."
        menu:
            extend ""
            "Я могу отключать силы других мутантов.":
                    $ WandaX.Statup("Love", 200, 1)
                    $ WandaX.Statup("Obed", 200, 1)
                    call Wanda_Scene_Zero_Powers
            "Тебе, наверное, тяжело.":
                    $ WandaX.Statup("Love", 200, 1)
                    $ WandaX.FaceChange("surprised",1)
                    ch_w "Что?! Да нет. . ."
                    $ WandaX.FaceChange("sly",1,Eyes="side")
                    ch_w "Ну ладно, иногда."
                    $ WandaX.FaceChange("normal",1)
        return

label Wanda_Scene_Zero_Powers:
        #called when you tell her about your powers or Rogue does
        $ WandaX.RecentActions.append("zero")
        $ WandaX.FaceChange("surprised",1)
        ch_w "А? Серьезно?"
        $ WandaX.FaceChange("smile",1)
        ch_w "Это клево."
        ch_w "Когда-нибудь это может пригодиться."
        ch_w "Может, попробуем прямо сейчас?"
        menu:
            extend ""
            "Конечно.":
                    $ WandaX.Statup("Love", 200, 3)
                    $ WandaX.Statup("Obed", 200, 1)
                    $ WandaX.FaceChange("smile",1)
                    "Вы берете ее за руку."
                    $ WandaX.Addictionrate += 2
                    $ WandaX.Statup("Lust", 90, 5)
                    ch_w "Ох, щекотно. . ."
                    ch_w "Ладно, теперь я попробую применить магию. . ."
            "Нет, спасибо.":
                    $ WandaX.Statup("Love", 200, -3)
                    $ WandaX.Statup("Inbt", 200, 2)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Да ладно тебе, мне же ужасно интересно."
                    $ WandaX.FaceChange("sly",1,Eyes="psychic")
                    "Ее глаза загораются, магическая энергия окутывает вас."
                    "Вы хватаете ее руку, прежде чем ситуация усугубится."
                    $ WandaX.FaceChange("surprised",1)
                    $ WandaX.Addictionrate += 2
                    $ WandaX.Statup("Lust", 90, 5)
                    ch_w "Ох, щекотно. . ."
                    "Жуткая энергия пропадает."
        $ WandaX.FaceChange("surprised",2)
        ch_w ". . ."
        ch_w "Хм, ничего."
        $ WandaX.FaceChange("smile",1)
        ch_w "Клево."
        $ WandaX.Statup("Love", 200, 1)
        $ WandaX.Statup("Obed", 200, 1)
        $ WandaX.FaceChange("sly",1)
        ch_w "Стоит держать тебя поблизости. . ."
        ch_w "На случай если я. . ."
        $ WandaX.Statup("Obed", 200, 2)
        $ WandaX.FaceChange("sly",1,Eyes="side")
        ch_w "-неважно."
        $ WandaX.FaceChange("normal",1)
        return

label Wanda_Scene_Jail:
        #called when her jail time comes up
        $ WandaX.RecentActions.append("jail")
        ch_w "Я. . . недавно вышла из тюрьмы."
        menu:
            extend ""
            "За что сидела?":
                    $ WandaX.Statup("Love", 200, 2)
                    $ WandaX.Statup("Obed", 200, 1)
                    $ WandaX.Statup("Inbt", 200, 1)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Я натворила всякого. . ."
            "О, ну ладно.":
                    $ WandaX.Statup("Love", 200, 2)
                    $ WandaX.Statup("Inbt", 200, 2)
                    $ WandaX.FaceChange("smile",1)
            ". . .":
                    $ WandaX.Statup("Obed", 200, 3)
                    $ WandaX.FaceChange("perplexed",1)
        ch_w "Не переживай, ничего серьезного я не сделала."
        $ WandaX.FaceChange("sadside",1,Mouth="smirk")
        ch_w "Так, попортила имущества и нанесла мелкие травмы студентам."
        $ WandaX.FaceChange("sadside",1)
        ch_w "Мои силы слегка вышли из под контроля."
        $ WandaX.FaceChange("angry",1,Eyes="side")
        ch_w "Ксавье мог все замять, но не стал."
        $ WandaX.FaceChange("sadside",1,Mouth="smirk")
        ch_w "Сказал: \"Тебе нужно время, чтобы разобраться в себе.\""
        ch_w ". . ."
        $ WandaX.FaceChange("sly",1)
        ch_w "Не скажу, что он уж совсем был неправ. . ."
        ch_w "После освобождения он предложил мне пожить здесь."
        return
#end Wanda Meet content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Wanda_Key:
        call Shift_Focus(WandaX)
        $ WandaX.Loc = bg_current
        call Set_The_Scene
        $ WandaX.FaceChange("bemused")
        $ Event_Queue = [0,0]
        ch_w "Раз уж ты часто заглядываешь ко мне. . ."
        ch_w "-вот. . ."
        "Она вручает вам ключ с маленькой пентаграммой на нем."
        $ Keys.append(WandaX) if WandaX not in Keys else Keys
        $ WandaX.Event[0] = 1
        ch_p "Спасибо."
        return

label Wanda_Witch:
        #scene for when Wanda looks like Scarlet Witch
        #elif "witch" not in WandaX.History and ApprovalCheck(WandaX, 1200) and WandaX.Loc == bg_current:
        #        #Shows off MCU costume
        #        call Wanda_Witch
        #        return
        $ WandaX.AddWord(1,0,0,0,"witch") #history

        $ WandaX.OutfitDay = "casual3"
        $ WandaX.Outfit = "casual3"
        $ WandaX.OutfitChange("casual3")
        $ WandaX.Hair = "long"
        call CleartheRoom("All",0,1)
        call Shift_Focus(WandaX)
        $ WandaX.Loc = bg_current
        $ WandaX.SpriteLoc = StageCenter
        call Set_The_Scene

        $ WandaX.FaceChange("sly",1)
        ch_u "Привет, [Player.Name]."
        menu:
            extend ""
            "Ты кто?":
                    $ WandaX.Statup("Love", 60, -1)
                    $ WandaX.Statup("Love", 90, -2)
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.FaceChange("confused",1)
                    ch_u "А?"
            "[WandaX.Name]?":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.FaceChange("confused",1)
                    ch_w "Да?"
            ". . .":
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.FaceChange("confused",1)
                    ch_u "В чем дело?"
        ch_w "Ты меня не узнаешь?"
        menu:
            extend ""
            "Ты вообще видела себя в зеркале?":
                    ch_w "Ну, в ближайшее время нет. . ."
            "Ты выглядишь иначе.":
                    $ WandaX.Statup("Obed", 50, 1)
                    ch_w "Да?"
            "Кто -ты-?":
                    $ WandaX.Statup("Love", 80, -1)
                    ch_w "Это я! [WandaX.Name]!"
            ". . .":
                    $ WandaX.Statup("Obed", 50, 1)
                    ch_w "Ты меня пугаешь. . ."
        "Она смотрит на свое отражение в экране телефона."
        $ WandaX.FaceChange("surprised",1)
        ch_w "Ой!"
        $ WandaX.FaceChange("smile",1)
        ch_w "Я и -правда- не похожа на себя. . ."
        menu:
            extend ""
            "Что случилось?":
                    $ WandaX.Statup("Inbt", 50, 1)
            "Это часто бывает?":
                    $ WandaX.FaceChange("sly",1)
                    ch_w ". . . иногда. . ."
            "Ага.":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.Statup("Inbt", 50, 1)
        $ WandaX.FaceChange("sly",1)
        ch_w "Время от времени происходит что-то. . . странное, вроде этого."
        ch_w "Вокруг меня что-то \"меняется,\" становится не таким, как раньше."
        ch_w "Мой старый наставник считает, что я способна притягивать части другой вселенной или что-то в этом роде."
        $ WandaX.FaceChange("sly",1,Eyes="down")
        ch_w "Должно быть, так я выгляжу где-то. . . в другом месте. . ."
        $ WandaX.FaceChange("sly",1)
        menu:
            extend ""
            "Безумие.":
                    $ WandaX.Statup("Love", 80, 3)
                    $ WandaX.Statup("Inbt", 50, 1)
                    $ WandaX.Statup("Inbt", 80, 1)
                    ch_w "Ага, в каком-то роде."
            "Круто.":
                    $ WandaX.Statup("Love", 80, 4)
                    $ WandaX.Statup("Inbt", 60, 1)
                    ch_w ". . . Ага. . . "
            "Как странно.":
                    $ WandaX.Statup("Love", 80, -1)
                    $ WandaX.Statup("Obed", 60, 2)
                    $ WandaX.FaceChange("sly",1,Brows="angry")
                    ch_w "Пожалуй. . ."
            "Хм.":
                    $ WandaX.Statup("Love", 80, -2)
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.FaceChange("sly",1,Brows="sad")
                    ch_w "Ага. . ."
        ch_w "Что думаешь?"
        ch_w "Мне идет новый образ?"
        $ WandaX.Names.append("Scarlet Witch")
        menu:
            extend ""
            "Ага, мне нравится!":
                    $ WandaX.Statup("Love", 70, 2)
                    $ WandaX.Statup("Love", 90, 3)
                    $ WandaX.Statup("Inbt", 70, 1)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Это очень мило. Думаю, я побуду в таком виде еще какое-то время."
                    $ WandaX.RecentActions.append("keep")
            "Раньше ты выглядела лучше.":
                    $ WandaX.Statup("Love", 70, 2)
                    $ WandaX.Statup("Love", 90, 3)
                    $ WandaX.Statup("Obed", 70, 2)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Оу, как мило."
            "Норм.":
                    $ WandaX.Statup("Love", 80, -1)
                    $ WandaX.Statup("Obed", 50, 2)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Ты прямо пышешь энтузиазмом."
            "Наверное?":
                    $ WandaX.Statup("Love", 80, -2)
                    $ WandaX.Statup("Obed", 70, 1)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Ну, спасибо!"
        if "keep" not in WandaX.RecentActions:
                $ WandaX.OutfitDay = "casual1"
                $ WandaX.Outfit = "casual1"
                $ WandaX.OutfitChange("casual1")
                $ WandaX.Hair = "short"
                call Set_The_Scene
                "Она вспыхивает и возвращает свой прежний облик."
                ch_w "Ну вот."
                ch_w "Думаю, если захочу, я смогу вернуться к тому облику."
        return

label Wanda_Asylum:
        $ WandaX.AddWord(1,0,0,0,"asylum") #history
        $ WandaX.FaceChange("sad",1)
        if not Player.Male:
            ch_w "Не знаю, слышал ли ты об этом, но несколько лет назад я застряла в. . ."
        else:
            ch_w "Не знаю, слышал ли ты об этом, но несколько лет назад я застряла в. . ."
        $ WandaX.FaceChange("sadside",2)
        ch_w "В психиатрической лечебнице. . . для умалишенных."
        menu:
            extend ""
            "Как так получилось?":
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Ну, в некотором роде я это заслужила."
            "Я думала, ты была в \тюрьме.\"" if not Player.Male:
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.FaceChange("sad",1)
                    ch_w "Тюрьма была гораздо позже. "
            "Я думала, ты была в \тюрьме.\"" if Player.Male:
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.FaceChange("sad",1)
                    ch_w "Тюрьма была гораздо позже. "
            "Ладно.":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Я думала, ты сильнее удивишься."
            "Мы все по своему двинутые. . ." :
                    $ WandaX.Statup("Inbt", 50, 1)
                    $ WandaX.FaceChange("confused",1)
                    ch_w "Ага. . . погоди, что?"
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.Statup("Obed", 50, -1)
        $ WandaX.FaceChange("sad",1)
        ch_w "Мой отец отправил меня туда, когда больше не мог со мной справляться."
        ch_w "Мои силы вышли из-под контроля, и я тихонько начала сходить с ума."
        ch_w "Так что, думаю, мне не стоит слишком расстраиваться, но все равно. . ."
        menu:
            extend ""
            "Должен был быть способ получше.":
                    $ WandaX.Statup("Love", 70, 3)
                    $ WandaX.Statup("Love", 90, 2)
                    $ WandaX.FaceChange("sly",1,Eyes="side")
                    ch_w "Ага, в то время я так и думала."
                    $ WandaX.Statup("Obed", 50, -1)
                    $ WandaX.FaceChange("sadside",1)
                    ch_w "Но теперь уже так в этом не уверена."
            "Жестко.":
                    $ WandaX.Statup("Love", 70, 1)
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.FaceChange("sad",1,Brows="sad")
                    ch_w "Ага. . ."
            "Я понимаю, почему они это сделали.":
                    $ WandaX.Statup("Love", 80, -1)
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.Statup("Obed", 70, 2)
                    $ WandaX.FaceChange("sad",1,Mouth="smile")
                    ch_w "Мне неприятно это слышать."
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.FaceChange("sadside",1,Mouth="smile")
                    ch_w "-но, возможно, иного выбора не было. . ."
            "Ага.":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.FaceChange("sad",1,Mouth="smile")
                    ch_w "Ага. . ."
            ". . .":
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.FaceChange("sad",1,Mouth="smile")
        ch_w "Я смогла научиться лучше контролировать свои силы, но для этого потребовалось много усилий."
        $ WandaX.FaceChange("sad",1,Mouth="smile")
        ch_w "Прости, я слишком многое вывалила на тебя, да?"
        ch_w "Наверное, я просто подумала, что тебе следует больше узнать о моем прошлом."
        $ WandaX.Statup("Love", 80, 10)
        $ WandaX.Statup("Obed", 70, 10)
        $ WandaX.FaceChange("sly",1)
        ch_w "Я чувствую себя гораздо более. . . комфортно рядом с тобой, чем раньше."
        return

label Wanda_BF(BO=[]):
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(WandaX,"bemused","краснеет. . .")
                return
        call Shift_Focus(WandaX)
        if WandaX.Loc != bg_current:
            $ WandaX.Loc = bg_current
            if WandaX not in Party:
                "[WandaX.Name] подходит к вам и показывает жестом, что хочет поговорить с вами наедине."
            else:
                "[WandaX.Name] поворачивается к вам и показывает жестом, что хочет поговорить с вами наедине."
        $ Event_Queue = [0,0]
        $ WandaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene(0)
        call Display_Girl(WandaX)
        $ WandaX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in WandaX.History:
                call expression WandaX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        $ WandaX.Event[5] += 1
        call Taboo_Level
        call CleartheRoom(WandaX)
        $ WandaX.FaceChange("normal",1)
        if "asked boyfriend" not in WandaX.DailyActions:
                ch_w "Послушай, [WandaX.Petname]. Мы можем поговорить?"
        else:
                ch_w "Сначала, позволь мне спросить тебя. . ."
        if not Player.Male:
            ch_w "Ты когда-нибудь слышала о Магнето?"
        else:
            ch_w "Ты когда-нибудь слышал о Магнето?"
        menu:
            extend ""
            "Он ведь суперзлодей?":
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Ага, его часто так называют."
            "Это друг Ксавье?":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Когда-то да. Хотя и сейчас они порой сходятся. . ."
            "Это ведь он выступает за права мутантов?":
                    $ WandaX.Statup("Obed", 70, 1)
                    $ WandaX.Statup("Inbt", 70, 1)
                    $ WandaX.FaceChange("surprised",1)
                    if not Player.Male:
                        ch_w "Ого, ты довольно хорошо его описала. . ."
                    else:
                        ch_w "Ого, ты довольно хорошо его описал. . ."
                    $ WandaX.FaceChange("sly",1)
            "Он ведь военный преступник?":
                    $ WandaX.Statup("Love", 80, -1)
                    $ WandaX.Statup("Obed", 70, 1)
                    $ WandaX.Statup("Inbt", 70, 1)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "В какой-то степени. . ."
            "Кто это?":
                    $ WandaX.Statup("Love", 80, -2)
                    $ WandaX.Statup("Obed", 70, -1)
                    $ WandaX.Statup("Inbt", 50, 2)
                    $ WandaX.FaceChange("sly",1)
                    if not Player.Male:
                        ch_w "Не могу поверить, что ты никогда не слышала о нем."
                    else:
                        ch_w "Не могу поверить, что ты никогда не слышал о нем."
        ch_w "Он невероятно могущественный мутант, \"Мастер магнетизма.\""
        $ WandaX.FaceChange("sly",1,Eyes="side")
        ch_w "Они с Ксавье раньше работали вместе, но Магнето стал использовать гораздо более. . . радикальне методы."
        ch_w "Он начал использовать насилие как инструмент для достижения превосходства мутантов. . ."
        $ WandaX.FaceChange("sly",1,Brows="sad")
        ch_w ". . . а еще он мой отец."
        menu:
            extend ""
            "Тебе, наверное, тяжело.":
                    $ WandaX.Statup("Love", 70, 3)
                    $ WandaX.Statup("Love", 90, 3)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Ага. . ."
            "Ага, я знаю.":
                    $ WandaX.FaceChange("confused",1)
                    ch_w "Правда?"
                    menu:
                        extend ""
                        "Ага.":
                                $ WandaX.Statup("Love", 80, 1)
                                $ WandaX.Statup("Obed", 80, 2)
                                $ WandaX.FaceChange("sly",1,Eyes="side")
                                ch_w "О, ну да, это никогда не было секретом. . ."
                        "Шучу.":
                                $ WandaX.Statup("Love", 90, 1)
                                $ WandaX.Statup("Inbt", 70, 1)
                                $ WandaX.FaceChange("sly",1)
                                ch_w "Угу-м. . ."
                        "У тебя такая же фамилия.":
                                $ WandaX.FaceChange("smile",1)
                                ch_w ". . ."
                                $ WandaX.Statup("Love", 80, -1)
                                $ WandaX.Statup("Obed", 50, -1)
                                $ WandaX.Statup("Inbt", 50, 2)
                                $ WandaX.Statup("Inbt", 70, 3)
                                $ WandaX.FaceChange("sly",1,Brows="angry")
                                ch_w ". . . нет, это не так."
            "Безумие.":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.Statup("Obed", 50, 1)
                    $ WandaX.Statup("Inbt", 50, 1)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Можно и так сказать."
            "Круто.":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.Statup("Inbt", 70, 1)
                    $ WandaX.FaceChange("confused",1)
                    ch_w "Серьезно? Ну, может быть. . ."
                    $ WandaX.FaceChange("sly",1)
            "Нихуя себе!!!":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.Statup("Obed", 80, -1)
                    $ WandaX.FaceChange("surprised",1,Mouth="open")
                    ch_w "Ага!"
                    $ WandaX.Statup("Obed", 50, -1)
                    $ WandaX.Statup("Inbt", 70, 2)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Но не волнуйся, тебе ничего не угрожает!"
        ch_w "Он совершил много ужасных поступков, но он мой отец."
        $ WandaX.FaceChange("sly",1)
        ch_w "Но, несмотря на это, я стараюсь придерживаться своего пути."
        ch_w "Я просто подумала, что тебе следует это знать. . ."

        if WandaX in Player.Harem:
                #if she somehow already ended up in the harem
                if "WandaYes" in Player.Traits:
                        $ Player.Traits.remove("WandaYes")
                if "boyfriend" not in WandaX.Petnames:
                        $ WandaX.Petnames.append("boyfriend")
                return

        $ WandaX.FaceChange("sly",1,Eyes="side")
        ch_w ". . . перед тем, как я спрошу. . ."
        $ WandaX.FaceChange("sly",1,Brows="sad")
        if not Player.Male:
            ch_w "Ты. . . хочешь стать моей девушкой?"
        else:
            ch_w "Ты. . . хочешь стать моим парнем?"
label Wanda_BF_Redux:
        $ Line = "start"
        call Shift_Focus(WandaX)
        while Line != "yes":
            menu:
                extend ""
                "Конечно." if Line != "maybe":
                        $ WandaX.FaceChange("smile",1)
                        $ WandaX.Statup("Love", 200, 6)
                        $ WandaX.Statup("Obed", 80, 2)
                        ch_w "Отлично!"
                        $ Line = "yes"
                "Ладно." if Line == "maybe":
                        $ WandaX.FaceChange("normal",1)
                        $ WandaX.Statup("Love", 200, 4)
                        $ WandaX.Statup("Obed", 80, 2)
                        $ WandaX.Statup("Inbt", 60, 1)
                        $ WandaX.Statup("Inbt", 80, 2)
                        ch_w "Эм. . . ладно?"
                        $ Line = "yes"

                "Мне это не особо интересно." if Line != "maybe":
                        $ WandaX.FaceChange("sad",1)
                        $ WandaX.Statup("Love", 200, -3)
                        $ WandaX.Statup("Obed", 80, 3)
                        ch_w "Ох. . . понимаю."
                        $ Line = "maybe"
                "Мне это -совсем- не интересно." if Line == "maybe":
                        $ WandaX.FaceChange("sad",1)
                        $ WandaX.Statup("Love", 200, -5)
                        $ WandaX.Statup("Obed", 60, 1)
                        $ WandaX.Statup("Obed", 80, 3)
                        ch_w "Ох. . ."
                        $ Line = "no"

                "Нет, не думаю, что [Player.Harem[0].Name] меня поймет." if len(Player.Harem) == 1:
                        $ WandaX.Statup("Love", 200, -15)
                        $ WandaX.Statup("Obed", 80, 7)
                        $ WandaX.FaceChange("sadside",1)
                        $ WandaX.GLG(Player.Harem[0],800,-10,1)
                        ch_w "Ох. . . ладно. . ."
                        $ Line = "no"
                "Другим девушкам это не понравится." if len(Player.Harem) > 1:
                        $ WandaX.Statup("Love", 200, -15)
                        $ WandaX.Statup("Obed", 80, 7)
                        $ WandaX.FaceChange("sad",1)
                        call HaremStatup(WandaX,700,-10) #lowers like of all Harem girls by 10
                        ch_w "Оооох. . . значит, есть и другие. . ."
                        $ Line = "no"

            if Player.Harem and Line == "yes":
                #if you agreed, but have other girls. . .
                if not ApprovalCheck(WandaX, 1400):
                    $ WandaX.FaceChange("sadside",1)
                    ch_w "Думаю, ты уже с кем-то встречаешься. . ."
                    $ Line = "no"
                else:
                    if len(Player.Harem) >= 2:
                        ch_w "Другие девушки не будут против?"
                    else:
                        ch_w "[Player.Harem[0].Name] не будет против?"
                    menu:
                        extend ""
                        "Нет, все будет нормально." if "WandaYes" in Player.Traits:
                                $ WandaX.Statup("Love", 200, 5)
                                $ WandaX.Statup("Obed", 80, 10)
                                $ WandaX.Statup("Inbt", 80, 5)
                                $ WandaX.FaceChange("surprised",1)
                                ch_w "Ого, ладно."
                        "Честно говоря. . . Сперва нужно это узнать." if "WandaYes" not in Player.Traits:
                                $ WandaX.Statup("Love", 200, 3)
                                $ WandaX.Statup("Obed", 80, 3)
                                $ WandaX.Statup("Inbt", 80, 1)
                                $ WandaX.Statup("Lust", 80, 1)
                                $ WandaX.FaceChange("confused",1)
                                ch_w "О. . . ну ладно. . . дашь мне знать, если что-то изменится?"
                                $ WandaX.Event[5] = 20
                                call Remove_Girl(WandaX)
                                $ Line = 0
                                return
                    call HaremStatup(WandaX,900,20) #raises like of all Harem girls by 20

            if Line == "no":
                    $ WandaX.FaceChange("sadside",1)
                    ch_w "Думаю, тебе не захочется быть с кем-то настолько ненормальным. . ."
                    "[WandaX.Name] расстроенная уходит."
                    $ WandaX.Event[5] = 20
                    call Remove_Girl(WandaX)
                    $ Line = 0
                    return
            # end menu

        if "Historia" not in Player.Traits:
            $ Player.Harem.append(WandaX)
            if "WandaYes" in Player.Traits:
                    $ Player.Traits.remove("WandaYes")
            $ WandaX.Petnames.append("boyfriend")
            call Harem_Initiation
        $ WandaX.Statup("Love", 200, 3)
        $ WandaX.Statup("Obed", 80, 3)
        $ WandaX.Statup("Inbt", 80, 1)
        $ WandaX.Statup("Lust", 80, 1)
        $ WandaX.FaceChange("sly",1)
        ch_w "Теперь, когда с тяжелыми разговорами покончено. . ."
        if "Historia" in Player.Traits:
                return 1
        $ Tempmod = 10
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        $ Tempmod = 0
        return




## start Wanda_Love//////////////////////////////////////////////////////////


label Wanda_Love(BO=[]):
        call Shift_Focus(WandaX)
        if bg_current != "bg wanda":
            if WandaX.Loc == bg_current or WandaX in Party:
                "Внезапно [WandaX.Name] изъявляет желание поговорить с вами в своей комнате, после чего утягивает вас туда."
            else:
                "[WandaX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить с вами в своей комнате, после чего утягивает вас туда."
        else:
                "[WandaX.Name] внезапно начинает очень пристально смотреть на вас."
        $ bg_current = "bg wanda"
        $ WandaX.Loc = bg_current
        $ Event_Queue = [0,0]

        $ WandaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene(0)
        call Display_Girl(WandaX)
        $ WandaX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in WandaX.History:
                call expression WandaX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        call CleartheRoom(WandaX)
        $ WandaX.FaceChange("normal",1)
        ch_w "Послушай, [WandaX.Petname]. Мы можем поговорить?"
        if "asylum" not in WandaX.History:
                #if you haven't done her sub event already
                call Wanda_Asylum
                #ch_w "I've felt a lot more. . . comfortable around you than I used to be."
        else:
                #if you've done her sub event already
                if not Player.Male:
                    ch_w "Думаю, ты мне очень помогла."
                else:
                    ch_w "Думаю, ты мне очень помог."
                if not Player.Male:
                    ch_w "Ты привнесла в мою жизнь стабильность, которой у меня никогда не было."
                else:
                    ch_w "Ты привнес в мою жизнь стабильность, которой у меня никогда не было."
        ch_w "Я чувствую, что теперь лучше справляюсь со своими эмоциями. . ."
        $ WandaX.FaceChange("smile",1)
        ch_w "Я хочу сказать тебе, что. . . я люблю тебя."

        menu:
            extend ""
            "Я тоже тебя люблю!":
                $ WandaX.FaceChange("smile",1)
                $ WandaX.Statup("Love", 200, 20)
                $ WandaX.Statup("Inbt", 90, 5)
                ch_w "Да?!"
                $ WandaX.Petnames.append("lover")
                jump Wanda_Love_End
            "Я знаю.":
                $ WandaX.FaceChange("confused",1)
                $ WandaX.Statup("Love", 200, -5)
                $ WandaX.Statup("Obed", 90, 5)
                $ WandaX.Statup("Inbt", 90, 5)
                ch_w "Что?"
                $ WandaX.Statup("Love", 200, 15)
                $ WandaX.Statup("Inbt", 90, 5)
                $ WandaX.FaceChange("normal",2,Mouth="smirk")
                ch_w "Уверена, ты говоришь это всем девушкам. . ."
                $ WandaX.FaceChange("normal",1,Mouth="smirk")
                $ WandaX.Petnames.append("lover")
                jump Wanda_Love_End
            "Круто?":
                $ WandaX.FaceChange("confused",1,Mouth="smile")
                $ WandaX.Statup("Obed", 90, 5)
                ch_w "Ага. . . круто. . ."
            "Хм.":
                $ WandaX.FaceChange("confused",1)
                $ WandaX.Statup("Love", 200, -5)
                $ WandaX.Statup("Obed", 90, 10)
                ch_w "Значит, мои чувства не взаимны. . ."
        menu:
            extend ""
            "Ох, я тоже тебя люблю!":
                $ WandaX.FaceChange("smile",1)
                $ WandaX.Statup("Love", 200, 15)
                $ WandaX.Statup("Obed", 90, 5)
                ch_w "Ох. . . "
                $ WandaX.FaceChange("sly",1)
                $ WandaX.Statup("Inbt", 90, 5)
                ch_w "Здорово!"
                $ WandaX.Petnames.append("lover")
                jump Wanda_Love_End
            "Я. . . тоже тебя люблю?":
                $ WandaX.FaceChange("confused",1)
                $ WandaX.Statup("Love", 200, 5)
                $ WandaX.Statup("Obed", 90, 5)
                if not Player.Male:
                    ch_w "Ты заставила меня поволноваться, [WandaX.Petname]."
                else:
                    ch_w "Ты заставил меня поволноваться, [WandaX.Petname]."
                $ WandaX.FaceChange("bemused",1)
                $ WandaX.Petnames.append("lover")
                jump Wanda_Love_End
            "Это, конечно, круто и все такое. . .":
                $ WandaX.FaceChange("sad",1)
                $ WandaX.Statup("Love", 200, -5)
                $ WandaX.Statup("Obed", 90, 10)
                $ WandaX.Statup("Inbt", 90, -5)
                ch_w ". . . Нет, я все понимаю, это уже перебор. . ."
            "Мне. . . некомфортно от этого.":
                $ WandaX.FaceChange("confused",1)
                $ WandaX.Statup("Love", 200, -10)
                $ WandaX.Statup("Obed", 90, 15)
                $ WandaX.Statup("Inbt", 90, -5)
                ch_w "Ох. . ."
                $ WandaX.FaceChange("sad",1)

        if "sexfriend" in WandaX.Petnames:
                $ WandaX.FaceChange("sly",1)
                ch_w "Мы все еще можем. . . \"развлекаться\" вместе, правда. . ?"
        elif "sir" in WandaX.Petnames:
                $ WandaX.FaceChange("sad",1,Mouth="normal")
                ch_w "Надеюсь, ты и дальше сможешь держать меня под контролем. . ."
        else:
                $ WandaX.FaceChange("sad",1)
                ch_w "Мы все еще можем проводить время вместе. . ."
                $ WandaX.FaceChange("sadside",1,Mouth="smirk")
                ch_w "-или еще чем-нибудь заниматься. . ?"
        menu:
            extend ""
            "Ага. . .":
                    $ WandaX.FaceChange("sad",1)
                    ch_w "Ну тогда ладно. . ."
            ". . .":
                    $ WandaX.FaceChange("sad",1)
            "Поговорим в другой раз":
                    ch_w "Ну ладно. . ."
                    $ WandaX.FaceChange("sad",1)
        hide Wanda_Sprite with easeoutright
        call Remove_Girl(WandaX)
        $ WandaX.Loc = "hold" #puts her off the board for the day
        "Она уходит."
        $ WandaX.Event[6] = 20
        $ Line = 0
        jump Misplaced
        return

label Wanda_Love_End:
        $ WandaX.Event[6] = 5
        "[WandaX.Name] бросается к вам и целует."
        $ WandaX.Statup("Love", 200, 25)
        $ WandaX.Statup("Lust", 90, 5)
        $ WandaX.FaceChange("sly",1)
        ch_w "Фух, я все испереживалась. . ."
        $ WandaX.Statup("Lust", 90, 10)

        if not WandaX.Sex:
                $ WandaX.FaceChange("bemused",2)
                ch_w "Может. . ."
        ch_w "-займемся чем-нибудь?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Ага, давай. . . [[заняться сексом]":# (locked)":   #fix, unlock once sex becomes an option
                    $ WandaX.Statup("Inbt", 30, 20)
                    $ WandaX.Statup("Obed", 70, 10)
                    ch_w "Ммм. . ."
                    if Player.Male:
                            call SexAct("sex") # call Wanda_SexAct("sex")
                    else:
                            call SexAct("blow") # call Wanda_SexAct("blow")
                "У меня есть пара идей. . .[[выбрать другое занятие]":
                    $ WandaX.Brows = "confused"
                    $ WandaX.Statup("Obed", 70, 25)
                    ch_w "Например? . ."
                    $ Tempmod = 20
                    call SexMenu
        jump Misplaced

label Wanda_Love_Redux:
         #this is for if you rejected her but want a second chance
        $ Line = 0
        $ WandaX.DailyActions.append("relationship")

        if WandaX.Event[6] >= 25:
                #if this is the second time through
                ch_p "Надеюсь, ты простила меня, я все еще люблю тебя."
                $ WandaX.Statup("Love", 95, 10)
                if "syke" in WandaX.History:
                    $ WandaX.Statup("Love", 200, -5)
                if ApprovalCheck(WandaX, 950, "L"):
                    $ Line = "love"
                else:
                    $ WandaX.FaceChange("sad",1)
                    ch_w "Я. . . я не могу ответить тебе тем же. Пока не могу, [WandaX.Petname]."
                    $ WandaX.FaceChange("sadside",Mouth="lipbite")
                    ch_w ". . ."
                    ch_w "Почему именно сейчас? . ."
        else:
                    if not Player.Male:
                        ch_p "Помнишь, я сказала тебе, что не люблю тебя?"
                    else:
                        ch_p "Помнишь, я сказал тебе, что не люблю тебя?"
                    $ WandaX.FaceChange("perplexed",1)
                    ch_w ". . ."
                    $ WandaX.FaceChange("sadside",1)
                    ch_w "Эм. . . да? . ."

        if Line != "love":
                menu:
                    extend ""
                    "Прости, я не хотела так говорить." if not Player.Male:
                        $ WandaX.FaceChange("confused",1)
                        ch_w ". . ."
                        ch_w "Ох. . ."
                        ch_p "Что ж. . . я люблю тебя, [WandaX.Name]."
                        $ WandaX.Statup("Love", 200, 10)
                        if ApprovalCheck(WandaX, 950, "L"):
                            $ Line = "love"
                            $ WandaX.FaceChange("surprised",1,Mouth="normal")
                        else:
                            $ WandaX.FaceChange("sadside")
                            ch_w "А я. . . наверное, теперь не уверена. . ."
                    "Прости, я не хотел так говорить." if Player.Male:
                        $ WandaX.FaceChange("confused",1)
                        ch_w ". . ."
                        ch_w "Ох. . ."
                        ch_p "Что ж. . . я люблю тебя, [WandaX.Name]."
                        $ WandaX.Statup("Love", 200, 10)
                        if ApprovalCheck(WandaX, 950, "L"):
                            $ Line = "love"
                            $ WandaX.FaceChange("surprised",1,Mouth="normal")
                        else:
                            $ WandaX.FaceChange("sadside")
                            ch_w "А я. . . наверное, теперь не уверена. . ."
                    "Я передумала, я люблю тебя, так что. . ." if not Player.Male:
                        if ApprovalCheck(WandaX, 950, "L"):
                            $ Line = "love"
                            $ WandaX.FaceChange("surprised",1,Mouth="normal")
                            ch_w "Да?"
                        else:
                            $ WandaX.Mouth = "sad"
                            ch_w "Хм. . ."
                            $ WandaX.Statup("Inbt", 90, 10)
                            $ WandaX.FaceChange("sadside")
                            ch_w ". . . Думаю, мне лучше оставить свои чувства в прошлом. . ."
                    "Я передумал, я люблю тебя, так что. . ." if Player.Male:
                        if ApprovalCheck(WandaX, 950, "L"):
                            $ Line = "love"
                            $ WandaX.FaceChange("surprised",1,Mouth="normal")
                            ch_w "Да?"
                        else:
                            $ WandaX.Mouth = "sad"
                            ch_w "Хм. . ."
                            $ WandaX.Statup("Inbt", 90, 10)
                            $ WandaX.FaceChange("sadside")
                            ch_w ". . . Думаю, мне лучше оставить свои чувства в прошлом. . ."
                    "Эм, неважно.":
                            $ WandaX.Statup("Love", 200, -30)
                            $ WandaX.Statup("Obed", 50, 10)
                            $ WandaX.FaceChange("angry")
                            ch_w "Похоже, ты любишь рисковать. . ."
                            $ WandaX.RecentActions.append("angry")
                            $ WandaX.DailyActions.append("angry")
        if Line == "love":
                $ WandaX.Statup("Love", 200, 40)
                $ WandaX.Statup("Obed", 90, 10)
                $ WandaX.Statup("Inbt", 90, 10)
                $ WandaX.FaceChange("normal")
                if not Player.Male:
                    ch_w "Я. . . рада, что ты все обдумала. . ."
                else:
                    ch_w "Я. . . рада, что ты все обдумал. . ."
                ch_w "Я тоже тебя люблю, [WandaX.Petname]!"
                $ WandaX.Petnames.append("lover")
        $ WandaX.Event[6] = 25
        return

# end Wanda_Love//////////////////////////////////////////////////////////


# start Wanda_Sub//////////////////////////////////////////////////////////

label Wanda_Sub:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(WandaX,"bemused","выглядит тихой. . .")
                return
        $ WandaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(WandaX)
        if WandaX.Loc != bg_current and WandaX not in Party:
            "Внезапно [WandaX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить."

        $ Event_Queue = [0,0]
        $ WandaX.Loc = bg_current
        call Set_The_Scene(0)
        call Display_Girl(WandaX)
        call CleartheRoom(WandaX)
        call Set_The_Scene
        call Taboo_Level
        $ WandaX.DailyActions.append("relationship")
        $ WandaX.FaceChange("bemused", 1)
        if not Player.Male and "girltalk" not in WandaX.History:
                call expression WandaX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return

        if "asylum" not in WandaX.History:
                #if you haven't done her love you event already
                call Wanda_Asylum
                #ch_w "I've felt a lot more. . . comfortable around you than I used to be."
        else:
                #if you've done her love you event already
                ch_w "Я рада, что смогла рассказать тебе о своей. . . семье."
        ch_w "После этого разговора я поняла, чего мне до сих пор не хватало в моей жизни."
        ch_w "В моей жизни было слишком много плохих ориентиров и дурных установок."
        $ WandaX.FaceChange("sly",1)
        ch_w "Но, думаю. . . ты меня понимаешь."
        $ WandaX.History.append("sir")
        menu:
            extend ""
            "Ага.":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.Statup("Obed", 90, 5)
            "Конечно.":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.Statup("Obed", 90, 8)
            "Наверное.":
                    $ WandaX.Statup("Obed", 90, 2)
                    $ WandaX.FaceChange("confused",1)
                    ch_w "Наверное? . ."
            ". . .":
                    $ WandaX.Statup("Obed", 90, 1)
            "Что?":
                    $ WandaX.Statup("Love", 80, -1)
                    $ WandaX.Statup("Obed", 90, -1)
                    $ WandaX.Statup("Inbt", 80, 1)
                    ch_w "То есть. . . ты, кажется, понимаешь, что мне нужно."
        ch_w "Мне нужен ориентир, мне нужна хоть какая-то ясность. . . Мне нужен кто-то, кто поможет с этим."
        $ WandaX.FaceChange("sly",1)
        menu:
            extend ""
            "Это я могу тебе дать.":
                    $ WandaX.Statup("Obed", 200, 10)
                    $ WandaX.Statup("Inbt", 70, 2)
                    $ WandaX.FaceChange("smile",1)
                    ch_w "Приятно это знать. . ."
                    $ WandaX.FaceChange("sly",1)
                    if not Player.Male:
                        ch_w ". . . госпожа."
                    else:
                        ch_w ". . . господин."
            "О, ладно.":
                    $ WandaX.Statup("Inbt", 70, 3)
                    if not Player.Male:
                        ch_w "Что ж, прозвучало так, будто ты \"согласна,\" . . госпожа."
                    else:
                        ch_w "Что ж, прозвучало так, будто ты \"согласен,\" . . господин."
            "Это слишком хлопотно.":
                    $ WandaX.Statup("Love", 80, -5)
                    $ WandaX.Statup("Obed", 200, -10)
                    $ WandaX.Statup("Inbt", 70, -2)
                    $ WandaX.FaceChange("sadside",2)
                    ch_w "Ох. . . ладно. . ."
                    return  #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
            "Мне не интересно.":
                    $ WandaX.Statup("Obed", 200, -5)
                    $ WandaX.Statup("Inbt", 70, -2)
                    $ WandaX.FaceChange("sadside",2)
                    ch_w "Ох. . . ладно. . ."
                    return  #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
            ". . .":
                    $ WandaX.Statup("Obed", 200, 2)
                    $ WandaX.Statup("Inbt", 70, 3)
                    if not Player.Male:
                        ch_w "Буду считать, что ты согласилась. . . госпожа."
                    else:
                        ch_w "Буду считать, что ты согласился. . . господин."
        $ WandaX.Petnames.append("sir")
        menu:
            extend ""
            "Да, [WandaX.Pet].":
                    $ WandaX.Statup("Love", 80, 2)
                    $ WandaX.Statup("Obed", 200, 10)
                    $ WandaX.Statup("Inbt", 70, 2)
                    $ WandaX.NameCheck() #checks reaction to petname
                    if not Player.Male:
                        $ WandaX.Petname = "госпожа"
                        $ WandaX.Petname_rod = "госпожи"
                        $ WandaX.Petname_dat = "госпоже"
                        $ WandaX.Petname_vin = "госпожу"
                        $ WandaX.Petname_tvo = "госпожой"
                        $ WandaX.Petname_pre = "госпоже"
                    else:
                        $ WandaX.Petname = "господин"
                        $ WandaX.Petname_rod = "господина"
                        $ WandaX.Petname_dat = "господину"
                        $ WandaX.Petname_vin = "господина"
                        $ WandaX.Petname_tvo = "господином"
                        $ WandaX.Petname_pre = "господине"
            ". . .":
                    $ WandaX.Statup("Obed", 200, 7)
                    if not Player.Male:
                        $ WandaX.Petname = "госпожа"
                        $ WandaX.Petname_rod = "госпожи"
                        $ WandaX.Petname_dat = "госпоже"
                        $ WandaX.Petname_vin = "госпожу"
                        $ WandaX.Petname_tvo = "госпожой"
                        $ WandaX.Petname_pre = "госпоже"
                    else:
                        $ WandaX.Petname = "господин"
                        $ WandaX.Petname_rod = "господина"
                        $ WandaX.Petname_dat = "господину"
                        $ WandaX.Petname_vin = "господина"
                        $ WandaX.Petname_tvo = "господином"
                        $ WandaX.Petname_pre = "господине"
            "Только не зови меня \"госпожой\"." if not Player.Male:
                    $ WandaX.Statup("Obed", 200, 10)
                    $ WandaX.Statup("Inbt", 70, -1)
                    $ WandaX.FaceChange("sadside",2)
                    ch_w "Ох, конечно, [WandaX.Petname]."
                    $ WandaX.FaceChange("sly",1)
            "Только не зови меня \"господином\"." if Player.Male:
                    $ WandaX.Statup("Obed", 200, 10)
                    $ WandaX.Statup("Inbt", 70, -1)
                    $ WandaX.FaceChange("sadside",2)
                    ch_w "Ох, конечно, [WandaX.Petname]."
                    $ WandaX.FaceChange("sly",1)
        ch_w "Итак. . . я могу что-нибудь для тебя сделать? . ."
        $ WandaX.FaceChange("sly",1)
        ch_w "Можешь просить \"что угодно.\""
        return

label Wanda_Sub_Asked:
        $ Line = 0
        $ WandaX.FaceChange("sadside", 1)
        if not Player.Male:
            ch_w "Ты. . . кажется, не хотела этого."
        else:
            ch_w "Ты. . . кажется, не хотел этого."
        menu:
            extend ""
            "Ну, я хочу извиниться. Надеюсь, ты дашь мне второй шанс.":
                    if "sir" in WandaX.Petnames and ApprovalCheck(WandaX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(WandaX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            $ WandaX.FaceChange("angry", 1)
                            ch_w "Я. . . думаю, что на пока нашла отдушину в другом." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ WandaX.Statup("Love", 90, 10)
                            $ WandaX.FaceChange("sly", 1)
                            ch_w "Ну. . . Мы можем попробовать. . ."

            "Послушай. . . я знаю, что ты этого хочешь. Ты согласна попробовать еще раз, или нет?":
                    $ WandaX.FaceChange("bemused", 1)
                    if "sir" in WandaX.Petnames:
                        if ApprovalCheck(WandaX, 850, "O"):
                            if not Player.Male:
                                ch_w "Да, госпожа. . ."
                            else:
                                ch_w "Да, господин. . ."
                        else:
                            ch_w ". . . Я так не думаю. . ."
                            $ Line = "rude"
                    elif ApprovalCheck(WandaX, 600, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            $ WandaX.FaceChange("confused", 1)
                            ch_w "Ну. . ."
                            $ WandaX.FaceChange("sly", 1)
                            ch_w ". . . может быть."
                            ch_w "Ты правда этого хочешь?"
                            menu:
                                extend ""
                                "Да, извини, что я была довольно груба." if not Player.Male:
                                                $ WandaX.Statup("Love", 90, 15)
                                                $ WandaX.Statup("Inbt", 50, 10)
                                                $ WandaX.FaceChange("bemused", 1)
                                                $ WandaX.Eyes = "side"
                                                ch_w "Ну тогда ладно."
                                "Да, извини, что я был довольно груб." if Player.Male:
                                                $ WandaX.Statup("Love", 90, 15)
                                                $ WandaX.Statup("Inbt", 50, 10)
                                                $ WandaX.FaceChange("bemused", 1)
                                                $ WandaX.Eyes = "side"
                                                ch_w "Ну тогда ладно."
                                "Ты пиздец как права, сучка.":
                                        if "sir" in WandaX.Petnames and ApprovalCheck(WandaX, 900, "O"):
                                                $ WandaX.Statup("Love", 200, -5)
                                                $ WandaX.Statup("Obed", 200, 10)
                                                ch_w ". . ."
                                        elif ApprovalCheck(WandaX,500, "O"):
                                                $ WandaX.Statup("Love", 200, -5)
                                                $ WandaX.Statup("Obed", 200, 10)
                                                ch_w ". . . Что?"
                                                ch_w "Мне кажется, ты слишком стараешься."
                                        else: #if it failed both those things,
                                                $ WandaX.Statup("Love", 200, -10)
                                                $ WandaX.Statup("Obed", 90, -10)
                                                $ WandaX.Statup("Obed", 200, -10)
                                                $ WandaX.Statup("Inbt", 50, -15)
                                                $ WandaX.FaceChange("angry", 1)
                                                ch_w "Воу, успокойся."
                                                $ Line = "rude"
                                "Ладно, тогда не бери в голову.":
                                                $ WandaX.FaceChange("angry", 1)
                                                $ WandaX.Statup("Love", 200, -10)
                                                $ WandaX.Statup("Obed", 90, -10)
                                                $ WandaX.Statup("Obed", 200, -10)
                                                $ WandaX.Statup("Inbt", 50, -15)
                                                ch_w ". . ."
                                                ch_w "Зачем тогда было заводить этот тупой разговор?!"
                                                $ Line = "rude"

        $ WandaX.RecentActions.append("asked sub")
        $ WandaX.DailyActions.append("asked sub")
        if Line == "rude":
                #If line hasn't been set to "rude" by something above, then it skips right past this
                hide Wanda_Sprite with easeoutright
                call Remove_Girl(WandaX)
                $ WandaX.RecentActions.append("angry")
                if "Historia" not in Player.Traits:
                        $ renpy.pop_call()
                "[WandaX.Name] выбегает из комнаты."
        elif "sir" in WandaX.Petnames:
                #it didn't fail and "sir" was covered
                $ WandaX.Statup("Obed", 200, 50)
                $ WandaX.Petnames.append("master")
                if not Player.Male:
                    $ WandaX.Petname = "хозяйка"
                    $ WandaX.Petname_rod = "хозяйки"
                    $ WandaX.Petname_dat = "хозяйке"
                    $ WandaX.Petname_vin = "хозяйку"
                    $ WandaX.Petname_tvo = "хозяйкой"
                    $ WandaX.Petname_pre = "хозяйке"
                else:
                    $ WandaX.Petname = "хозяин"
                    $ WandaX.Petname_rod = "хозяина"
                    $ WandaX.Petname_dat = "хозяину"
                    $ WandaX.Petname_vin = "хозяина"
                    $ WandaX.Petname_tvo = "хозяином"
                    $ WandaX.Petname_pre = "хозяине"
                $ WandaX.Eyes = "sly"
                if not Player.Male:
                    ch_w ". . . хозяйка. . ."
                else:
                    ch_w ". . . хозяин. . ."
        else:
                #it didn't fail
                $ WandaX.Statup("Obed", 200, 30)
                $ WandaX.Petnames.append("sir")
                if not Player.Male:
                    $ WandaX.Petname = "госпожа"
                    $ WandaX.Petname_rod = "госпожи"
                    $ WandaX.Petname_dat = "госпоже"
                    $ WandaX.Petname_vin = "госпожу"
                    $ WandaX.Petname_tvo = "госпожой"
                    $ WandaX.Petname_pre = "госпоже"
                else:
                    $ WandaX.Petname = "господин"
                    $ WandaX.Petname_rod = "господина"
                    $ WandaX.Petname_dat = "господину"
                    $ WandaX.Petname_vin = "господина"
                    $ WandaX.Petname_tvo = "господином"
                    $ WandaX.Petname_pre = "господине"
                $ WandaX.FaceChange("sly", 1)
                if not Player.Male:
                    ch_w ". . . госпожа."
                else:
                    ch_w ". . . господин."
        return

# end Wanda_Sub//////////////////////////////////////////////////////////


# start Wanda_Master//////////////////////////////////////////////////////////

label Wanda_Master:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(WandaX,"bemused","выглядит необычайно покорной. . .")
                return
        $ WandaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(WandaX)
        if WandaX.Loc != bg_current and WandaX not in Party:
            "Внезапно [WandaX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить."

        $ Event_Queue = [0,0]
        $ WandaX.Loc = bg_current
        call Set_The_Scene(0)
        call Display_Girl(WandaX)
        call CleartheRoom(WandaX)
        $ WandaX.ArmPose = 2
        call Set_The_Scene
        $ WandaX.DailyActions.append("relationship")
        call Taboo_Level
        $ Line = 0
        $ WandaX.FaceChange("sly", 1)
        ch_w "Итак. . . [WandaX.Petname]. . ."
        ch_w "Как я справлялась?"
        $ WandaX.FaceChange("sly", 1,Brows="sad")
        ch_w "Как думаешь, я стала лучше?"
        $ Line = 0
        menu:
            extend ""
            "Конечно.":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.Statup("Obed", 90, 1)
                    $ WandaX.FaceChange("sly",1,Brows="surprised")
                    ch_w "Я серьезно!"
                    $ WandaX.FaceChange("sly",1)
                    $ Line = "yes"
            "Что ты имеешь в виду?":
                    $ WandaX.Statup("Love", 80, 1)
                    $ WandaX.Statup("Inbt", 60, 1)
                    $ WandaX.FaceChange("sly",1)
            "Не особо.":
                    $ WandaX.Statup("Love", 80, -1)
                    $ WandaX.Statup("Obed", 200, 3)
                    $ WandaX.FaceChange("sad",1)
                    ch_w "Ох. . ."
                    $ Line = "no"
            "Наверное?":
                    $ WandaX.Statup("Love", 80, -1)
                    $ WandaX.Statup("Obed", 200, -1)
                    $ WandaX.FaceChange("sad",1)
            ". . .":
                    $ WandaX.Statup("Love", 80, -1)
        ch_w "Я о том, что. . . помнишь, я просила у тебя помощи в поддержании равновесия в душе. . ?"
        ch_w "Как считаешь, что-то с тех пор изменилось в лучшую сторону?"
        menu:
            extend ""
            "Я поняла, что ты имела в виду." if not Player.Male:
                    if Line == "yes":
                            $ WandaX.Statup("Love", 200, 2)
                            $ WandaX.Statup("Obed", 200, 5)
                            $ WandaX.Statup("Inbt", 80, 2)
                            $ WandaX.FaceChange("smile",1)
                            ch_w "О, хорошо. . ."
                    elif Line == "no":
                            $ WandaX.Statup("Love", 80, -1)
                            $ WandaX.Statup("Obed", 200, 10)
                            $ WandaX.Statup("Inbt", 50, -3)
                            $ WandaX.FaceChange("sadside",1)
                            ch_w "Ох. . ."
                    else:
                            $ WandaX.Statup("Inbt", 90, -1)
                            $ WandaX.FaceChange("sad",1)
                            ch_w "Эм. . ."
            "Я понял, что ты имела в виду." if Player.Male:
                    if Line == "yes":
                            $ WandaX.Statup("Love", 200, 2)
                            $ WandaX.Statup("Obed", 200, 5)
                            $ WandaX.Statup("Inbt", 80, 2)
                            $ WandaX.FaceChange("smile",1)
                            ch_w "О, хорошо. . ."
                    elif Line == "no":
                            $ WandaX.Statup("Love", 80, -1)
                            $ WandaX.Statup("Obed", 200, 10)
                            $ WandaX.Statup("Inbt", 50, -3)
                            $ WandaX.FaceChange("sadside",1)
                            ch_w "Ох. . ."
                    else:
                            $ WandaX.Statup("Inbt", 90, -1)
                            $ WandaX.FaceChange("sad",1)
                            ch_w "Эм. . ."
            "Думаю, да.":
                    $ WandaX.Statup("Love", 90, 2)
                    $ WandaX.Statup("Obed", 200, 4)
                    $ WandaX.FaceChange("sly",1)
                    $ Line = "yes"
                    ch_w "О, хорошо. . ."
            "Я так не думаю.":
                    $ WandaX.Statup("Love", 80, -2)
                    $ WandaX.Statup("Obed", 200, 5)
                    $ WandaX.FaceChange("sad",1)
                    $ Line = "no"
                    ch_w "Ох. . ."
            ". . .":
                    $ WandaX.Statup("Love", 90, -5)
                    $ WandaX.Statup("Obed", 200, 3)
                    $ WandaX.Statup("Inbt", 80, 2)
                    $ WandaX.FaceChange("angry",1)
        if not Line:
            ch_w "Мне бы очень хотелось получить ответ."
            menu:
                extend ""
                "Думаю, да.":
                        $ WandaX.Statup("Love", 90, 2)
                        $ WandaX.Statup("Obed", 200, 4)
                        $ WandaX.FaceChange("sly",1)
                        $ Line = "yes"
                        ch_w "О, хорошо. . ."
                "Я так не думаю.":
                        $ WandaX.Statup("Love", 80, -2)
                        $ WandaX.Statup("Obed", 200, 5)
                        $ WandaX.FaceChange("sad",1)
                        $ Line = "no"
                        ch_w "Ох. . ."
                ". . .":
                        $ WandaX.Statup("Love", 80, -2)
                        $ WandaX.Statup("Love", 90, -2)
                        $ WandaX.Statup("Obed", 200, 2)
                        $ WandaX.FaceChange("sad",1)
                        if not Player.Male:
                            ch_w "Буду считать, что ты ответила \"нет.\""
                        else:
                            ch_w "Буду считать, что ты ответил \"нет.\""
                        $ Line = "no"
        if Line == "yes":
                ch_w "Тогда, думаю, нам нужно продолжать в том же духе."
        else:
                ch_w "Тогда, возможно, нам придется внести некие правки. . ."
        $ WandaX.History.append("master")
        menu:
            extend ""
            "Зови теперь меня \"хозяйкой\"" if not Player.Male:
                    $ WandaX.Statup("Love", 90, 1)
                    $ WandaX.Statup("Obed", 200, 15)
                    $ WandaX.FaceChange("sly",1)
                    $ WandaX.Petnames.append("master")
                    ch_w "Я надеялась, что ты так скажешь. . ."
            "Зови теперь меня \"хозяином\"" if Player.Male:
                    $ WandaX.Statup("Love", 90, 1)
                    $ WandaX.Statup("Obed", 200, 15)
                    $ WandaX.FaceChange("sly",1)
                    $ WandaX.Petnames.append("master")
                    ch_w "Я надеялась, что ты так скажешь. . ."
            "Чего ты хочешь?":
                    $ WandaX.Statup("Love", 90, 1)
                    $ WandaX.Statup("Obed", 200, 5)
                    $ WandaX.FaceChange("sly",1)
            "Что?":
                    $ WandaX.Statup("Obed", 200, -3)
                    $ WandaX.FaceChange("confused",1)
            ". . .":
                    $ WandaX.Statup("Obed", 200, 5)
                    $ WandaX.Statup("Inbt", 80, 3)
                    $ WandaX.FaceChange("sly",1)
                    $ WandaX.Petnames.append("master")
                    if not Player.Male:
                        ch_w "В молчании мудрость. . . хозяйка."
                    else:
                        ch_w "В молчании мудрость. . . хозяин."

        while "master" not in WandaX.Petnames:
            if not Player.Male:
                ch_w "Могу я звать тебя своей. . . хозяйкой?"
            else:
                ch_w "Могу я звать тебя своим. . . хозяином?"
            menu:
                extend ""
                "Безусловно.":
                        $ WandaX.Petnames.append("master")
                        $ WandaX.Statup("Love", 200, 1)
                        $ WandaX.Statup("Obed", 200, 2)
                        ch_w "Великолепно."
                "Конечно.":
                        $ WandaX.Petnames.append("master")
                        $ WandaX.FaceChange("confused",1,Eyes="side")
                        $ WandaX.Statup("Obed", 200, -1)
                        ch_w "Ладно. . . клево. . ."
                        $ WandaX.FaceChange("normal",1)
                "Мне не хочется ничего менять.":
                        $ WandaX.FaceChange("sadside",2)
                        $ WandaX.Statup("Love", 80, -1)
                        $ WandaX.Statup("Obed", 200, -2)
                        $ WandaX.Statup("Inbt", 70, -2)
                        ch_w "Ох. . . ладно. . ."
                        $ WandaX.FaceChange("normal",1)
                        ch_w "Тогда оставим все, как есть. . ."
                        return
                "Нет.":
                        $ WandaX.FaceChange("sad",2,Eyes="surprised")
                        $ WandaX.Statup("Love", 80, -1)
                        $ WandaX.Statup("Obed", 200, -4)
                        $ WandaX.Statup("Inbt", 70, -2)
                        ch_w "Ох. . ."
                        $ WandaX.FaceChange("sad",2)
                        ch_w "Думаю, я слишком многого хочу. . ."
                        hide Wanda_Sprite with easeoutright
                        call Remove_Girl(WandaX)
                        $ WandaX.FaceChange("normal",1)
                        $ WandaX.Loc = "hold" #puts her off the board for the day
                        "Она уходит."
                        return
                "Что ты имеешь в виду?" if "what" not in WandaX.RecentActions:
                        $ WandaX.RecentActions.append("what")
                        $ WandaX.Statup("Obed", 200, -1)
                        ch_w "Мне было бы легче, если бы я могла звать тебя так. . ."
        if not Player.Male:
            ch_w ". . . хозяйка."
        else:
            ch_w ". . . хозяин."
        menu:
            extend ""
            ". . .":
                    if not Player.Male:
                        $ WandaX.Petname = "хозяйка"
                        $ WandaX.Petname_rod = "хозяйки"
                        $ WandaX.Petname_dat = "хозяйке"
                        $ WandaX.Petname_vin = "хозяйку"
                        $ WandaX.Petname_tvo = "хозяйкой"
                        $ WandaX.Petname_pre = "хозяйке"
                    else:
                        $ WandaX.Petname = "хозяин"
                        $ WandaX.Petname_rod = "хозяина"
                        $ WandaX.Petname_dat = "хозяину"
                        $ WandaX.Petname_vin = "хозяина"
                        $ WandaX.Petname_tvo = "хозяином"
                        $ WandaX.Petname_pre = "хозяине"
                    $ WandaX.FaceChange("smile", 2, Eyes="side")
                    $ WandaX.Statup("Obed", 200, 2)
            "А хорошо звучит.":
                    if not Player.Male:
                        $ WandaX.Petname = "хозяйка"
                        $ WandaX.Petname_rod = "хозяйки"
                        $ WandaX.Petname_dat = "хозяйке"
                        $ WandaX.Petname_vin = "хозяйку"
                        $ WandaX.Petname_tvo = "хозяйкой"
                        $ WandaX.Petname_pre = "хозяйке"
                    else:
                        $ WandaX.Petname = "хозяин"
                        $ WandaX.Petname_rod = "хозяина"
                        $ WandaX.Petname_dat = "хозяину"
                        $ WandaX.Petname_vin = "хозяина"
                        $ WandaX.Petname_tvo = "хозяином"
                        $ WandaX.Petname_pre = "хозяине"
                    $ WandaX.FaceChange("normal", 1)
                    $ WandaX.Statup("Love", 90, 1)
                    $ WandaX.Statup("Obed", 200, 2)
                    $ WandaX.Statup("Inbt", 80, 2)
            "Мне не нравится термин \"хозяйка\"." if Player.Male:
                    $ WandaX.FaceChange("sad", 1,Mouth="smile")
                    $ WandaX.Statup("Love", 90, 2)
                    $ WandaX.Statup("Obed", 200, 3)
                    ch_w "Но я ведь могу считать тебя ей, правда?"
                    menu:
                        extend ""
                        "Да.":
                                $ WandaX.Statup("Love", 90, 1)
                                $ WandaX.FaceChange("sly", 1)
                                ch_w "Хорошо!"
                                ch_w ". . . [WandaX.Petname]."
                        "Нет.":
                                $ WandaX.FaceChange("sad", 1)
                                ch_w "Ладно. . ."
                                $ WandaX.FaceChange("sly", 1)
                                ch_w "Буду звать тебя просто [WandaX.Petname_tvo]."
                        ". . .":
                                $ WandaX.FaceChange("sly", 1)
                                ch_w "Ладно, значит \"нет\". . ."
                                ch_w "Буду звать тебя просто [WandaX.Petname_tvo]."
            "Мне не нравится термин \"хозяин\"." if not Player.Male:
                    $ WandaX.FaceChange("sad", 1,Mouth="smile")
                    $ WandaX.Statup("Love", 90, 2)
                    $ WandaX.Statup("Obed", 200, 3)
                    ch_w "Но я ведь могу считать тебя им, правда?"
                    menu:
                        extend ""
                        "Да.":
                                $ WandaX.Statup("Love", 90, 1)
                                $ WandaX.FaceChange("sly", 1)
                                ch_w "Хорошо!"
                                ch_w ". . . [WandaX.Petname]."
                        "Нет.":
                                $ WandaX.FaceChange("sad", 1)
                                ch_w "Ладно. . ."
                                $ WandaX.FaceChange("sly", 1)
                                ch_w "Буду звать тебя просто [WandaX.Petname_tvo]."
                        ". . .":
                                $ WandaX.FaceChange("sly", 1)
                                ch_w "Ладно, значит \"нет\". . ."
                                ch_w "Буду звать тебя просто [WandaX.Petname_tvo]."
        $ WandaX.FaceChange("sly",1)
        ch_w "Скажи мне, какие у тебя желания."
        ch_w "Я готова их исполнить. . ."
        return

# end Wanda_Master//////////////////////////////////////////////////////////



# start Wanda_Sexfriend//////////////////////////////////////////////////////////

label Wanda_Sexfriend:   #Wanda_Update
        $ WandaX.Loc = bg_current
        $ WandaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ Event_Queue = [0,0]
        call Set_The_Scene
        $ WandaX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in WandaX.History:
                call expression WandaX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        $ Line = 0
        call Shift_Focus(WandaX)
        $ WandaX.FaceChange("smile",2)
        "[WandaX.Name] подходит к вам и отводит в сторону."
        $ WandaX.Petnames.append("sex friend")

        if WandaX.SEXP >= 20:
                if not Player.Male:
                    ch_w "Знаешь, ты очень хорошая любовница."
                else:
                    ch_w "Знаешь, ты очень хороший любовник."
        else:
                $ WandaX.FaceChange("sly",2,Brows="angry")
                if not Player.Male:
                    ch_w "Я уже устала ждать, когда ты станешь серьезной."
                else:
                    ch_w "Я уже устала ждать, когда ты станешь серьезным."
        ch_w "Я не была такой нервной со времен тюрьмы. . ."
        menu:
            extend ""
            "Да?":
                    $ WandaX.FaceChange("sly",2)
                    ch_w "Однозначно."
            "Что ты хочешь этим сказать?":
                    $ WandaX.Statup("Inbt", 200, 5)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Думаю, тут не сложно догадаться."
            ". . .":
                    $ WandaX.Statup("Obed", 200, 2)
                    $ WandaX.FaceChange("sly",2,Brows="angry")
        ch_w "Если захочешь пошалить, просто дай мне знать."

        $ WandaX.Statup("Inbt", 90, 15)
        if Taboo:
            ch_w "Может, прямо сейчас отойдем куда-нибудь и займемся чем-нибудь?"
            menu:
                extend ""
                "Ага.":
                        $ WandaX.Statup("Love", 90, 3)
                        $ WandaX.Statup("Inbt", 200, 5)
                        ch_w "-Отлично.-"
                        if bg_current == "bg player":
                                $ bg_current = "bg wanda"
                        else:
                                $ bg_current = "bg player"
                        $ WandaX.Loc = bg_current
                        $ Party = []
                        call Set_The_Scene
                        call CleartheRoom(WandaX)
                        call Set_The_Scene
                        $ Taboo = 0
                        $ WandaX.Taboo = 0

                "Нет, давай здесь.":
                        $ WandaX.Statup("Obed", 80, 5)
                        $ WandaX.Statup("Inbt", 90, 15)
                        ch_w ". . . Ну ладно. . ."
                "Не сейчас.":
                        $ WandaX.FaceChange("sad", 1)
                        $ WandaX.Statup("Love", 90, -3)
                        $ WandaX.Statup("Obed", 90, 5)
                        ch_w "Тебе же хуже. . ."
                        return
        else:
            if not Player.Male:
                ch_w "Итак, ты сейчас занята?"
            else:
                ch_w "Итак, ты сейчас занят?"
            menu:
                extend ""
                "Сейчас я не свободна." if not Player.Male:
                        $ WandaX.Statup("Love", 90, 3)
                        $ WandaX.Statup("Inbt", 90, 5)
                        ch_w "Это я и хотела услышать. . ."
                "Сейчас я не свободен." if Player.Male:
                        $ WandaX.Statup("Love", 90, 3)
                        $ WandaX.Statup("Inbt", 90, 5)
                        ch_w "Это я и хотела услышать. . ."
                "Мне сейчас не до этого.":
                        $ WandaX.FaceChange("sad", 1)
                        $ WandaX.Statup("Love", 90, -3)
                        $ WandaX.Statup("Obed", 90, 5)
                        if not Player.Male:
                            ch_w "Жаль, дай знать, когда будешь готова. . ."
                        else:
                            ch_w "Жаль, дай знать, когда будешь готов. . ."
                        return
        $ Situation = WandaX
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        #end "if no relationship"
        return

# end Wanda_Sexfriend//////////////////////////////////////////////////////////


# start Wanda_Fuckbuddy//////////////////////////////////////////////////////////

label Wanda_Fuckbuddy:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(WandaX,"sly","выглядит взволнованной. . .")
                return
        $ WandaX.DailyActions.append("relationship")
        $ WandaX.Lust = 60
        $ WandaX.Wet = 2
        $ WandaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        #change Wanda's outfit to default
        $ Event_Queue = [0,0]
        if WandaX.Loc != bg_current:
                $ WandaX.Loc = bg_current
                "[WandaX.Name] появляется перед вами."
        else:
                "[WandaX.Name] поворачивается к вам."
        call Shift_Focus(WandaX)
        call Set_The_Scene(0)
        call Display_Girl(WandaX)
        call Taboo_Level
        #$ WandaX.Event[10] += 1
        $ WandaX.Petnames.append("fuck buddy")
        $ WandaX.FaceChange("sly",1)
        ch_w "Я не знаю, что со мной происходит в последнее время."
        $ WandaX.FaceChange("sly",1,Eyes="side")
        ch_w "Я чувствую, что теряю контроль над собой, но. . ."
        $ WandaX.FaceChange("sly",2)
        ch_w "-это больше меня не беспокоит."
        ch_w "Я могу немного потерять голову, не беспокоясь о том, что это может привести к катастрофе."
        ch_w ". . ."
        $ WandaX.FaceChange("sly",1)
        ch_w "Спасибо тебе за это. . ."
        if Taboo and not ApprovalCheck(WandaX, 2000):
                #if in public and with not high stats. . .
                ch_w "Следуй за мной, смотри, не отставай. . ."
                if bg_current == "bg player":
                        $ bg_current = "bg wanda"
                else:
                        $ bg_current = "bg player"
                $ WandaX.Loc = bg_current
                call CleartheRoom(WandaX)
                call Set_The_Scene
                $ Taboo = 0
                $ WandaX.Taboo = 0
        if WandaX.Over or WandaX.Chest or WandaX.Legs or WandaX.Panties:
                $ WandaX.OutfitChange("nude")
                "[WandaX.Name] ненадолго активирует силы, и ее одежда исчезает в потоке энергии."

        ch_w "Итак. . . чем займемся?"
        menu:
            extend ""
            "У меня есть пара идей.":
                    $ WandaX.Statup("Love", 90, 3)
                    $ WandaX.Statup("Inbt", 200, 5)
                    ch_w "Это я и хотела услышать. . ."
            "Давай не сейчас.":
                    $ WandaX.FaceChange("sad", 1)
                    $ WandaX.Statup("Love", 90, -3)
                    $ WandaX.Statup("Obed", 90, 5)
                    ch_w "Жаль. . ."
                    return
        $ WandaX.Statup("Inbt", 200, 10)
        $ Situation = WandaX
        $ Player.AddWord(1,"interruption") #adds to Recent
#        call Wanda_SexPrep              #she offers sex
        call SexMenu
        return
# end Wanda_Fuckbuddy//////////////////////////////////////////////////////////

# start Wanda_Daddy//////////////////////////////////////////////////////////

#Not updated

label Wanda_Daddy:       #Wanda_Update
        $ WandaX.DailyActions.append("relationship")
        $ WandaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(WandaX)
        $ Event_Queue = [0,0]
        if WandaX.Loc != bg_current:
                $ WandaX.Loc = bg_current
                "[WandaX.Name] подходит к вам."
        call Set_The_Scene
        $ WandaX.FaceChange("sadside",1,Mouth="normal")
        ch_w "Думаю, я как-то говорила про своего отца. . ."
        if Player.Male != 1:
            ch_w "а вот свою маму я никогда не видела. . ."
        menu:
            extend ""
            "Я помню.":
                    $ WandaX.Statup("Love", 80, 2)
                    $ WandaX.FaceChange("smile",1)
                    pass
            "Да?":
                    pass
            "Что?":
                    $ WandaX.Statup("Love", 80, -1)
                    $ WandaX.Statup("Obed", 80, 1)
                    $ WandaX.FaceChange("confused",1)
                    ch_w "Говорила, говорила про отца."
            ". . .":
                    $ WandaX.Statup("Obed", 60, 1)
                    $ WandaX.FaceChange("sly",1)
                    ch_w "Так вот. . ."
        $ WandaX.FaceChange("sadside",1,Mouth="smirk")
        if not Player.Male:
            ch_w "Поскольку мне очень комфортно с тобой, я подумала, что ты могла бы мне помочь. . ."
        else:
            ch_w "Поскольку мне очень комфортно с тобой, я подумала, что ты мог бы мне помочь. . ."
        $ WandaX.FaceChange("sadside",2,Mouth="smirk")
        ch_w "-с небольшой. . . ролевой игрой?"
        ch_w "Могу я звать тебя. . ."
        $ WandaX.FaceChange("sadside",2,Mouth="normal")
        if not Player.Male:
            ch_w "\"мамочкой?\""
        else:
            ch_w "\"папочкой?\""
        menu:
            extend ""
            "Хорошо?":
                $ WandaX.FaceChange("smile")
                $ WandaX.Statup("Love", 90, 20)
                $ WandaX.Statup("Obed", 60, 10)
                $ WandaX.Statup("Inbt", 80, 30)
                ch_w "Ох. . . замечательно."
            "Зачем все это?":
                $ WandaX.FaceChange("bemused")
                ch_w "Ну, мне просто захотелось. . ."
                if WandaX.Love > WandaX.Obed and WandaX.Love > WandaX.Inbt:
                        ch_w "Поскольку ты так поддерживаешь меня. . ."
                elif WandaX.Obed > WandaX.Inbt:
                        if not Player.Male:
                            ch_w "Поскольку ты стала такой напористой. . ."
                        else:
                            ch_w "Поскольку ты стал таким напористым. . ."
                else:
                        ch_w "Это очень возбуждает, правда?"

                menu:
                    extend ""
                    "Ладно, можешь звать меня так.":
                            $ WandaX.FaceChange("smile")
                            $ WandaX.Statup("Love", 90, 15)
                            $ WandaX.Statup("Obed", 60, 20)
                            $ WandaX.Statup("Inbt", 80, 25)
                            ch_w "Клево!"
                            $ WandaX.FaceChange("sly",2)
                            if not Player.Male:
                                ch_w " . . . мамочка."
                            else:
                                ch_w " . . . папочка."
                            $ WandaX.FaceChange("sly",1)
                            if not Player.Male:
                                $ WandaX.Petname = "мамочка"
                                $ WandaX.Petname_rod = "мамочки"
                                $ WandaX.Petname_dat = "мамочке"
                                $ WandaX.Petname_vin = "мамочку"
                                $ WandaX.Petname_tvo = "мамочкой"
                                $ WandaX.Petname_pre = "мамочке"
                            else:
                                $ WandaX.Petname = "папочка"
                                $ WandaX.Petname_rod = "папочки"
                                $ WandaX.Petname_dat = "папочке"
                                $ WandaX.Petname_vin = "папочку"
                                $ WandaX.Petname_tvo = "папочкой"
                                $ WandaX.Petname_pre = "папочке"
                    "Не могла бы ты не звать меня так, пожалуйста?":
                            $ WandaX.Statup("Love", 90, 5)
                            $ WandaX.Statup("Obed", 80, 40)
                            $ WandaX.Statup("Inbt", 80, 20)
                            $ WandaX.FaceChange("sad")
                            ch_w ". . ."
                            ch_w "Ладно. . ."
                    "Тебя настолько беспокоит ситуация с отцом, да?" if Player.Male:
                            $ WandaX.Statup("Love", 90, -15)
                            $ WandaX.Statup("Obed", 80, 45)
                            $ WandaX.Statup("Inbt", 70, 5)
                            $ WandaX.FaceChange("sadside",2)
                            ch_w "О, ты даже не представляешь, насколько глубока эта кроличья нора. . ."
                            $ WandaX.FaceChange("sadside",1)
                    "Тебя настолько беспокоит ситуация с матерью, да?" if not Player.Male:
                            $ WandaX.Statup("Love", 90, -15)
                            $ WandaX.Statup("Obed", 80, 45)
                            $ WandaX.Statup("Inbt", 70, 5)
                            $ WandaX.FaceChange("sadside",2)
                            ch_w "О, ты даже не представляешь, насколько глубока эта кроличья нора. . ."
                            $ WandaX.FaceChange("sadside",1)

            "Тебя настолько беспокоит ситуация с отцом, да?" if Player.Male:
                    $ WandaX.Statup("Love", 90, -15)
                    $ WandaX.Statup("Obed", 80, 45)
                    $ WandaX.Statup("Inbt", 70, 5)
                    $ WandaX.FaceChange("sadside",2)
                    ch_w "О, ты даже не представляешь, насколько глубока эта кроличья нора. . ."
                    $ WandaX.FaceChange("sadside",1,Mouth="normal")
            "Тебя настолько беспокоит ситуация с матерью, да?" if not Player.Male:
                    $ WandaX.Statup("Love", 90, -15)
                    $ WandaX.Statup("Obed", 80, 45)
                    $ WandaX.Statup("Inbt", 70, 5)
                    $ WandaX.FaceChange("sadside",2)
                    ch_w "О, ты даже не представляешь, насколько глубока эта кроличья нора. . ."
                    $ WandaX.FaceChange("sadside",1,Mouth="normal")
        $ WandaX.Petnames.append("daddy")
        return

# end Wanda_Daddy//////////////////////////////////////////////////////////



# Start Character Meet Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gwen Meet Wanda / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Wanda_Meet:
        # GwenX.Event[2] tracks number of girls she knows you're dating
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = bg_current
        $ WandaX.Loc = bg_current
        call Shift_Focus(GwenX)
        $ GwenX.ArmPose = 2
        call Set_The_Scene
        $ GwenX.FaceChange("normal",1)
        $ WandaX.FaceChange("smile",1)
        ch_w "Hey, [WandaX.Petname]. . ."
        if WandaX.Petname in ("хозяин", "господин", "хозяйка", "госпожа"):
                $ GwenX.Statup("Obed", 60, 2)
                $ GwenX.Statup("Obed", 80, 5)
        $ GwenX.ArmPose = 1
        $ WandaX.ArmPose = 2
        hide Wanda_Seated
        show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc)
        hide Gwen_Seated
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom -1
        $ GwenX.Hat = 0
        $ GwenX.FaceChange("confused",1,Eyes="side")
        ch_g "О, ты такая. . . готичная."
        $ WandaX.FaceChange("confused",1,Eyes="side")
        ch_w "Меня зовут Ванда Максимофф."
        if WandaX.Hair == "long" or WandaX.Hair == "longwet":
                $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
                ch_g "О, точно!"
        else:
                $ GwenX.FaceChange("perplexed",1,Eyes="side")
                ch_g "Правда?"
                ch_g "Ты. . . интересно выглядишь."
                $ GwenX.FaceChange("smile",1,Eyes="side")
                ch_g "Тебе идет."
        ch_w "А кто ты?"
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "О. . . Я Гвен. Гвен Пул."
        ch_g "Значит, ты из Мстителей?"
        ch_w "Что? Из Мстителей?"
        $ WandaX.FaceChange("bemused",1,Eyes="side")
        ch_w "Хех, не думаю, что они могут меня принять."
        $ GwenX.FaceChange("sly",1,Eyes="side")
        ch_g "Почему? Слишком активно домогалась их роботов?"
        $ WandaX.FaceChange("perplexed",1,Eyes="side")
        ch_w "Что?! Нет!"
        $ WandaX.FaceChange("sadside",1,Mouth="normal")
        ch_w "Просто. . . у меня, эм, криминальное прошлое."
        $ GwenX.FaceChange("smile",2,Eyes="side")
        ch_g "О, у меня тоже."
        $ WandaX.FaceChange("surprised",1,Eyes="side")
        ch_w "Ты сидела?"
        $ WandaX.FaceChange("bemused",1,Eyes="side")
        $ GwenX.FaceChange("smile",1,Eyes="leftside")
        ch_g "Ну, всего пару ночей я провела в камере."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "Я одно время работала наемницей."
        ch_w "А, понятно. Я много таких повстречала за решеткой."
        ch_w "Работала на Гидру или А.И.М.?"
        ch_g "О, ни на тех, ни на других. . . хотя, наверное, в каком-то роде на А.И.М.?"
        $ GwenX.FaceChange("sly",2,Eyes="leftside")
        ch_g "Одно время я работала на МОДОКА."
        $ WandaX.FaceChange("bemused",1,Eyes="leftside")
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_w "Уфф, не продолжай. . ."
        $ WandaX.FaceChange("sly",1,Eyes="side")
        ch_w "Ты мне нравишься. Ты забавная. А какие у тебя способности?"
        ch_g "О, всякие \"мета\" штучки. Я знаю, что все это игра, и могу менять ее правила."
        ch_w "Да? Мы с тобой похожи."
        $ GwenX.FaceChange("surprised",1,Eyes="side")
        ch_g "Правда? А ты знала, что мы в -эроигре-?"
        $ WandaX.FaceChange("perplexed",1,Eyes="side")
        ch_w "Что?"
        menu:
            extend ""
            "[GwenX.Name] думает, что мы в игре.":
                    $ GwenX.FaceChange("sly",1)
                    $ GwenX.Statup("Love", 70, 2)
                    $ GwenX.Statup("Love", 90, 2)
                    $ GwenX.Statup("Obed", 80, 2)
                    ch_w "Ох, эм. . ."
            "Не обращай на нее внимание.":
                    $ GwenX.FaceChange("angry",1)
                    $ GwenX.Statup("Love", 90, -2)
                    $ GwenX.Statup("Obed", 70, 2)
                    ch_w "М? Ладно. . ."
            "Она сумасшедшая.":
                    $ GwenX.FaceChange("angry",2,Mouth="open")
                    $ GwenX.Statup("Love", 70, -2)
                    $ GwenX.Statup("Love", 90, -2)
                    ch_g "Эй!"
                    $ GwenX.FaceChange("angry",1,Eyes="side")
                    $ GwenX.Statup("Obed", 80, 3)
                    $ GwenX.Statup("Inbt", 70, 3)
                    ch_g "Я не сумасшедшая, просто я лучше информирована. . ."
            ". . .":
                    ch_g ". . ."
        $ WandaX.FaceChange("bemused",1,Eyes="side")
        $ GwenX.FaceChange("sad",1,Eyes="leftside")
        ch_g "А, ты просто сравнила наши силы. . ."
        ch_g "Поняла."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_w "У меня был некоторый опыт общения с альтернативными реальностями, ты застряла здесь?"
        ch_g "Вроде того?"
        ch_w "Ты бы хотела, чтобы я отправила тебя домой?"
        ch_g "А ты можешь?"
        if ApprovalCheck(GwenX, 1500):
                ch_g ". . ."
                ch_g "Нет, я думаю, что пока мне и здесь хорошо."
                ch_w "Ладно, это клево."
        else:
                $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
                ch_g "Правда? Да!"
                ch_w "Конечно, сейчас попробую. . ."
                $ WandaX.FaceChange("angry",1,Eyes="psychic")
                $ GwenX.FaceChange("smile",1,Eyes="closed")
                "Магическая энергия накапливается вокруг [WandaX.Name_rod], а затем окутывает [GwenX.Name_vin]."
                "Но, похоже, ничего не происходит."
                $ WandaX.FaceChange("sadside",1)
                ch_w "Хм. Думаю, не сработало."
                $ GwenX.FaceChange("smile",1)
                ch_g "Наверное, я слишком важна для успеха этой игры, меня так просто не удалить."
                $ WandaX.FaceChange("perplexed",1,Eyes="side")
                $ GwenX.FaceChange("angry",1,Mouth="open")
                ch_g "Эй! Вы! Там! Слышали?! Я очень важна!"
                ch_w "Ла. . .дно?"
                $ GwenX.FaceChange("sly",1,Eyes="side")
                ch_g "Я не к тебе обращалась."
                $ GwenX.FaceChange("sly",1)
                $ WandaX.FaceChange("perplexed",1)
                ch_w "Ла. . .дно."
        $ WandaX.FaceChange("bemused",1,Eyes="side")
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_w "В общем, рада была с тобой познакомиться."
        ch_g "Ага, надеюсь, мы сможем с тобой поладить."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        if not Player.Male:
            ch_g "Думаю, ты уже знакома с ней? . ."
        else:
            ch_g "Думаю, ты уже знакома с ним? . ."
        if WandaX in Player.Harem:
                $ WandaX.FaceChange("sly",1)
                $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
                $ WandaX.Statup("Obed", 80, 1)
                $ WandaX.Statup("Inbt", 80, 2)
                if not Player.Male:
                    ch_w "О да, я с ней \"знакома\". . ."
                else:
                    ch_w "О да, я с ним \"знакома\". . ."
                $ GwenX.FaceChange("surprised",1,Eyes ="side")
                if GwenX.Event[2] > 1:
                        #if wanda heard you were dating two+ girls
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "И ты тоже? . ."
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_w "Хех. . . ага."
                elif GwenX.Event[2]:
                        #if wanda heard you were dating someone else
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 3)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "И ты тоже? . ."
                        $ GwenX.Statup("Obed", 50, 4)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_w "Хех. . . ага."
                else:
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Obed", 60, 2)
                        $ GwenX.Statup("Obed", 80, 2)
                        $ GwenX.FaceChange("sly",1)
                        ch_g "О. . . круто, круто. . ."
                $ GwenX.Event[2] += 1
        elif WandaX.Petname in ("хозяин", "господин", "хозяйка", "госпожа"):
                $ WandaX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                if not Player.Male:
                    ch_w "Ага, она моя [WandaX.Petname]. . ."
                else:
                    ch_w "Ага, он мой [WandaX.Petname]. . ."
        elif not ApprovalCheck(WandaX, 500, "L"):
                $ WandaX.FaceChange("normal",0)
                if not Player.Male:
                    ch_w "Ага, она. . . помогает мне держать себя в руках. . ."
                else:
                    ch_w "Ага, он. . . помогает мне держать себя в руках. . ."
        else:
                $ WandaX.FaceChange("sad",1,Eyes="leftside")
                if not Player.Male:
                    ch_w "Ага, она. . . присматривает за мной. . ."
                else:
                    ch_w "Ага, он. . . присматривает за мной. . ."
        $ GwenX.FaceChange("normal",1,Eyes="side")
        $ WandaX.FaceChange("smile",1,Eyes="side",Mouth="open")
        ch_g "Что ж, как-нибудь еще увидимся."
        ch_w "Конечно. До встречи."
        $ GwenX.FaceChange("normal",1)
        $ WandaX.FaceChange("smile",1)
        $ WandaX.GirlLikeUp(GwenX,100)
        $ GwenX.GirlLikeUp(WandaX,100)
        $ GwenX.DrainWord("Wanda",0,0,0,1)
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
        return

# End Gwen Meet Wanda / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# End Character Meet Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Wanda_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        if "switched" in WandaX.History:
                jump Wanda_Switch2
        $ WandaX.FaceChange("confused", 1)
        ch_w "Хмммм. . ."
        ch_w ". . ."
        $ WandaX.FaceChange("sly", 1)
        ch_w "Знаешь, ты мне очень напоминаешь [Player.XName_vin]. . ."
        ch_w "У меня тоже есть брат-близнец, хотя мы не очень похожи."
        if not Player.Male:
            ch_w "Ты ее близнец?"
        else:
            ch_w "Ты его близнец?"
        menu:
            extend ""
            "Это я, [Player.XName].":
                    $ WandaX.FaceChange("smile", 1)
                    ch_w "О!"
                    $ WandaX.AddWord(1,"switch") #recent

            "Нет.":
                if Player.Male:
                    ch_w "Хм. Вы очень похожи."
                else:
                    ch_w "Ха. Вы очень похожи, но ты, пожалуй, сексуальнее."
            "Возможно?":
                    ch_w "\"Возможно?\" . ."
                    ch_w "Ага, понимаю. У меня тоже \"возможно\" есть сестра."

        if "switch" not in WandaX.RecentActions:
                    $ WandaX.FaceChange("confused", 1)
                    ch_w ". . . подожди-ка!"
                    $ WandaX.FaceChange("surprised", 1,Mouth= "open")
                    ch_w "Ты и -есть- [Player.XName]!"
                    $ WandaX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Ага, это я, [Player.XName].":
                                $ WandaX.FaceChange("smile", 1)
                                $ WandaX.Statup("Love", 90, 1)
                                $ WandaX.Statup("Obed", 70, 1)
                                ch_w "Тебе удалось меня на мгновение обмануть!"
                                $ WandaX.FaceChange("sly", 1)
                        "Нет.":
                                $ WandaX.FaceChange("bemused", 1)
                                $ WandaX.Statup("Obed", 60, 1)
                                $ WandaX.Statup("Obed", 70, 1)
                                ch_w "Конееечно."
                        "Возможно?":
                                $ WandaX.FaceChange("sly", 1)
                                $ WandaX.Statup("Love", 80, 1)
                                $ WandaX.Statup("Obed", 70, 1)
                                $ WandaX.Statup("Inbt", 60, 1)
                                ch_w "Я тебя раскусила."
                    ch_w "К чему все это?"
                    menu:
                        extend ""
                        "Извини, хотелось пошутить.":
                                $ WandaX.FaceChange("sly", 1)
                                $ WandaX.Statup("Love", 70, 1)
                        "Молодец, тебя не обманешь.":
                                $ WandaX.FaceChange("sly", 1)
                                $ WandaX.Statup("Obed", 70, 1)
                                $ WandaX.Statup("Inbt", 80, 1)
                                ch_w "Ну еще бы."
                        "Хех.":
                                $ WandaX.FaceChange("sly", 1,Eyes="side")
                                $ WandaX.Statup("Love", 70, 1)
                                $ WandaX.Statup("Love", 90, 1)
                                $ WandaX.Statup("Inbt", 70, 1)
                                ch_w "Мило. . ."
#                    ch_w "Anyway, I get it. . ."
        #end "tried to lie"
        $ WandaX.FaceChange("smile", 1)
        ch_w "Это какое-то колдовство или что-то в этом роде?"
        menu:
            extend ""
            "Просто по приколу захотелось сменить облик.":
                    $ WandaX.Statup("Inbt", 70, 1)
                    $ WandaX.FaceChange("sly", 1)
                    ch_w "Ага, понимаю."
            "Я так себя сейчас ощущаю.":
                    ch_w "Клево."
            "Колдовство не виновато, я даже не знаю, почему мне захотелось сменить облик.":
                    ch_w "Колдовство лучше всего все объясняет!"

        if [Player.Name] != [Player.XName]:
                ch_p "А еще меня теперь зовут [Player.Name]."
                ch_w "[Player.Name], интересно."

        if WandaX.SEXP >= 15:
                $ WandaX.FaceChange("sly", 1)
                ch_w "Я тебе все еще нравлюсь?"
                menu:
                    extend ""
                    "Конечно!":
#                            $ WandaX.FaceChange("normal", 1)
                            $ WandaX.Statup("Love", 70, 2)
                            $ WandaX.Statup("Love", 90, 1)
                            ch_w "Потрясающе."
                    "Не особо.":
                            $ WandaX.FaceChange("sad", 1)
                            $ WandaX.Statup("Love", 80, -2)
                            $ WandaX.Statup("Obed", 60, 2)
                            $ WandaX.Statup("Obed", 80, 2)
                            ch_w ". . . жаль. . ."
                    "А ты как думаешь?":
                            $ WandaX.FaceChange("sly", 1)
                            $ WandaX.Statup("Obed", 70, 1)
                            $ WandaX.Statup("Inbt", 70, 1)
                            ch_w "Приятно слышать."

        if not Player.Male and WandaX.Les > 5:
                $ WandaX.FaceChange("sly", 1)
                ch_w "Это может быть весело. . ."
#        if ApprovalCheck(WandaX, 1200):
#                ch_w "I guess we could give this a try. . ."
#                $ WandaX.AddWord(1,0,0,0,"girltalk") #history
#        else:
#                $ WandaX.FaceChange("normal", 1,Eyes="side")
        ch_w "В общем, еще увидимся. . ."
        $ WandaX.AddWord(1,0,0,0,"girltalk") #history
        $ WandaX.Traits.remove("switchcheck")
        $ WandaX.AddWord(1,0,0,0,"switched") #history
        return

label Wanda_Switch2:
        #when you switch for a 2+ time
        $ WandaX.FaceChange("smile", 1)
        if not Player.Male:
            ch_w "Ох, [Player.Name], ты вернула свой прежний облик."
        else:
            ch_w "Ох, [Player.Name], ты вернул свой прежний облик."
        $ WandaX.Traits.remove("switchcheck")
        $ WandaX.History.remove("switched")
        $ WandaX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Wanda_Girltalk(Auto=0,Other=0):
        # if Auto Wanda starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in WandaX.History:
                return
        if "nogirls" in WandaX.History:
                jump Wanda_Girltalk_Redux
        $ WandaX.FaceChange("sly", 1)
        if Auto:
                ch_w "Слушай, [Player.Name]. . ."
                ch_w "Должна спросить, я тебе нравлюсь?"
        else:
                ch_w "Слушай, должна спросить, я тебе нравлюсь?"
        menu:
            extend ""
            "Да?":
                    $ WandaX.FaceChange("sly", 1)
                    $ WandaX.Statup("Love", 70, 2)
                    $ WandaX.Statup("Love", 90, 2)
                    $ WandaX.Statup("Obed", 70, 1)
                    ch_w "Приятно слышать. . ."
            "Возможно?":
                    $ WandaX.FaceChange("confused", 1)
                    $ WandaX.Statup("Love", 70, 1)
                    $ WandaX.Statup("Obed", 80, 2)
                    $ WandaX.Statup("Inbt", 80, 2)
                    ch_w "А я думала. . ."
                    ch_w "В общем, дай мне знать, если определишься."
            "Не особо.":
                    $ WandaX.Statup("Love", 90, -1)
                    $ WandaX.Statup("Obed", 60, 2)
                    $ WandaX.Statup("Obed", 80, 2)
                    if ApprovalCheck(WandaX, 1200):
                            $ WandaX.FaceChange("sad", 1)
                            ch_w "Оу, жаль."
                            $ WandaX.FaceChange("sly", 1)
                    else:
                            $ WandaX.FaceChange("sly", 1)
                            ch_w "Ты не знаешь, чего лишаешься."
                    ch_w "Хотя я тебя понимаю. . ."
        $ WandaX.FaceChange("sly", 1)
#        if not WandaX.Les:
#                ch_w "I don't usually. . ."
#                $ WandaX.FaceChange("sly", 2,Eyes="side")
#                ch_w "-I haven't been with many people. . ."
#        if not ApprovalCheck(WandaX, 900) and not ApprovalCheck(WandaX, 600, "L") and not WandaX.Les:
#                ch_w "I. . . don't know how I feel about that. . ."
#                $ WandaX.AddWord(1,0,0,0,"nogirls") #history
#                call Girltalk_Check(WandaX)
#                return

        ch_w "Это может быть весело. . ."
        $ WandaX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(WandaX)
        return

label Wanda_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing

        $ WandaX.AddWord(1,0,0,0,"girltalk") #history
        return


        if ApprovalCheck(WandaX, 1000) or ApprovalCheck(WandaX, 600, "L"):
                $ WandaX.FaceChange("sly", 1)
                if Other in TotalGirls and "nogirls" in Other.History:
                        ch_w "Что ж. . ."
                ch_w "Пожалуй. . . почему бы и нет?"
                $ WandaX.DrainWord("nogirls",0,0,0,1) #history
                $ WandaX.AddWord(1,0,0,0,"girltalk") #history
        elif "nogirls" not in WandaX.History:
                $ WandaX.AddWord(1,0,0,0,"nogirls") #history
                ch_w "Хмм. . . я не уверена. . ."
        elif "nogirls" in WandaX.DailyActions:
                $ WandaX.FaceChange("angry", 1)
                if WandaX.Forced:
                        #if Forced, she will just go with it anyway
                        if "nogirls" not in WandaX.RecentActions:
                                $ WandaX.Statup("Love", 80, -2)
                                $ WandaX.Statup("Obed", 80, 2)
                                $ WandaX.AddWord(1,"nogirls",0,0,0) #recent
                        return
                ch_w "Перестань спрашивать."
        else:
                $ WandaX.Statup("Inbt", 50, 2)
                ch_w "Я не думаю, что из этого что-то выйдет. . ."
                $ WandaX.AddWord(1,0,"nogirls",0,0) #daily
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Wanda_69_Intro:
        if "69" in WandaX.History:
                return
        if Trigger == "lick pussy" and WandaX.LickP >= 3:
                if WandaX.Blow or (ApprovalCheck(WandaX, 1300) and WandaX.SeenPeen):
                        #if licking pussy but have gotten blowjob
                        $ WandaX.AddWord(1,0,0,0,"69") #history
                        ch_w "Итак. . . раз уж ты делаешь мне приятно. . ."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        if "cockout" not in Player.RecentActions:
                                $ Player.RecentActions.append("cockout")
                                "Она вытаскивает ваш член и начинает его сосать."
                        else:
                                "Она обнажает вашу киску и начинает ее лизать."
                        $ WandaX.Pose = "69"
                        call Wanda_BJ_Launch
                        if not Player.Male:
                            ch_w "Не могла бы ты, эм. . ."
                        else:
                            ch_w "Не мог бы ты, эм. . ."
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ WandaX.Statup("Love", 95, 3)
                                    $ WandaX.Statup("Inbt", 70, 2)
                                    $ WandaX.Statup("Inbt", 90, 1)
                                    ch_w "Хех, спасибо."
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ WandaX.Statup("Love", 80, -8)
                                    $ WandaX.Statup("Obed", 80, 3)
                                    $ WandaX.Statup("Obed", 90, 1)
                                    $ WandaX.Statup("Inbt", 70, -1)
                                    ch_w "Оу, жаль."
                        $ Situation = "69"
                        call SexAct("blow") # call Wanda_SexAct("blow")
                        $ renpy.pop_call() #causes it to skip past the Escalation
                        $ renpy.pop_call() #causes it to skip past the last activity
                return
        elif Trigger == "blow" and WandaX.Blow >= 3:
                #if licked pussy
                $ WandaX.AddWord(1,0,0,0,"69") #history
                ch_w "Слушай, эм. . . раз я уже здесь. . ."
                "Она прижимает вас к земле и забирается на вас сверху."
                $ WandaX.Pose = "69"
                call Wanda_BJ_Launch
                if not Player.Male:
                    ch_w "Не могла бы ты, эм. . ."
                else:
                    ch_w "Не мог бы ты, эм. . ."
                ch_w "-отплатить мне?"
                menu:
                    extend ""
                    "Приступить к работе.":
                            $ Trigger2 = "lick pussy"
                            $ WandaX.Statup("Love", 95, 3)
                            $ WandaX.Statup("Inbt", 70, 2)
                            $ WandaX.Statup("Inbt", 90, 1)
                            ch_w "Хех, спасибо."
                            if not WandaX.LickP:
                                $ WandaX.LickP += 1
                    "Расслабиться, оставив ее киску без внимания.":
                            $ WandaX.Statup("Love", 80, -5)
                            $ WandaX.Statup("Obed", 80, 3)
                            $ WandaX.Statup("Obed", 90, 1)
                            $ WandaX.Statup("Inbt", 70, -1)
                            ch_w "Оу, жаль."
                #returns to BJ already in progress
                return
        else:
                return
        return
