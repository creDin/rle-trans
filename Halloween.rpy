# Start Chat menus / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Halloween_Chat(Girl=0):  #rkeljsvgbds
        show blackscreen onlayer black
        if Girl is RogueX and renpy.showing("Rogue_Sprite"):
                pass
        elif Girl is KittyX and renpy.showing("Kitty_Sprite"):
                pass
        elif Girl is EmmaX and renpy.showing("Emma_Sprite"):
                pass
        elif Girl is LauraX and renpy.showing("Laura_Sprite"):
                pass
        elif Girl is JeanX and renpy.showing("Jean_Sprite"):
                pass
        elif Girl is StormX and renpy.showing("Storm_Sprite"):
                pass
        elif Girl is JubesX and renpy.showing("Jubes_Sprite"):
                pass
        elif Girl is GwenX and renpy.showing("Gwen_Sprite"):
                pass
        elif Girl is BetsyX and renpy.showing("Betsy_Sprite"):
                pass
        elif Girl is DoreenX and renpy.showing("Doreen_Sprite"):
                pass
        elif Girl is WandaX and renpy.showing("Wanda_Sprite"):
                pass
        else:
            "Вы подходите к [Girl.Name_dat]"
            call AllHide(1) #removes all girls
            while Present:
                    # Removes all girls from Present to Nearby
                    $ Nearby.append(Present[0])
                    $ Present[0].Loc = "nearby"
                    $ Present.remove(Present[0])
            #Makes the current focus girl present and at the party location.
            $ Nearby.remove(Girl)
            $ Present.append(Girl)
            $ Girl.Loc = "HW Party"

            call Display_Girl(Girl)
        hide blackscreen onlayer black

        if Girl == EmmaX and "classcaught" not in EmmaX.History:
                jump Emma_HWChat_Minimal

        if Girl is RogueX:
                if not Player.Male:
                    ch_r "Ну, о чем ты хотела поговорить, [Girl.Petname]?"
                else:
                    ch_r "Ну, о чем ты хотел поговорить, [Girl.Petname]?"
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
                ch_j "Что такое?"
        elif Girl is StormX:
                ch_s "Что я могу для тебя сделать, [Girl.Petname]?"
        elif Girl is JubesX:
                ch_v "Привет, что я могу сделать для тебя, [Girl.Petname]?"
        elif Girl is GwenX:
                ch_g "Привет, [Girl.Petname]. Что случилось?"
        elif Girl is BetsyX:
                ch_b "Могу я nt,t чем-нибудь помочь?"
        elif Girl is DoreenX:
                ch_d "Привет, что случилось?"
        elif Girl is WandaX:
                ch_w "Да, что такое?"

        call Halloween_Chat_Menu
        return

# Start Main Chat menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Halloween_Chat_Menu: #rkeljsvgbdw
        $ Girl = GirlCheck(Girl)
        $ Girl.FaceChange()
        call Shift_Focus(Girl)

        if "angry" in Girl.RecentActions:
                    if Girl is RogueX:
                            ch_r "Я совсем не хочу сейчас с тобой разговаривать."
                    elif Girl is KittyX:
                            ch_k "Я[Girl.like]очень зла на тебя сейчас!"
                    elif Girl is EmmaX:
                            ch_e "На твоем месте я бы не стала искушать судьбу."
                    elif Girl is LauraX:
                            ch_l "Лучше тебе сейчас держаться от меня подальше."
                    elif Girl is JeanX:
                            ch_j "Отойди от меня."
                    elif Girl is StormX:
                            ch_s "Тебе лучше сейчас держаться от меня подальше."
                    elif Girl is JubesX:
                            ch_v "Я не в настроении, [Girl.Petname]."
                    elif Girl is GwenX:
                            ch_g "Я не хочу проблем. . ."
                    elif Girl is BetsyX:
                            ch_b "Я бы предпочла избежать дальнейшей драмы. . ."
                    elif Girl is DoreenX:
                            ch_d "Ты в игноре."
                    elif Girl is WandaX:
                            ch_w "Не сейчас."
                    return

        menu:
            "Ухаживать":
                    menu:
                        "Флиртовать (locked)" if Girl.Chat[5]:
                                    pass
                        "Флиртовать" if not Girl.Chat[5]:
                                    call Flirt(Girl)
                                    return

                        "Секс-меню (locked)" if Girl.Loc != bg_current:
                                    pass
                        "Секс-меню" if Girl.Loc == bg_current:
                                    if Girl.Love >= Girl.Obed:
                                            ch_p "Не хочешь поразвлечься?"
                                    else:
                                            ch_p "Я хочу пошалить."
                                    if "angry" in Girl.RecentActions:
                                            if Girl is RogueX:
                                                    ch_r "Я не хочу сейчас с тобой связываться."
                                            elif Girl is KittyX:
                                                    ch_k "Даже не мечтай!"
                                            elif Girl is EmmaX:
                                                    ch_e "Тебе должен быть известен мой ответ."
                                            elif Girl is LauraX:
                                                    ch_l "Плохая идея."
                                            elif Girl is JeanX:
                                                    ch_j "-Совсем- не интересно."
                                            elif Girl is StormX:
                                                    ch_s "Мне это неинтересно."
                                            elif Girl is JubesX:
                                                    ch_v "Я не в настроении, [Girl.Petname]?"
                                            elif Girl is GwenX:
                                                    ch_g "Это вряд ли. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "И ты расчитываешь на положительный ответ. . ?"
                                            elif Girl is DoreenX:
                                                    ch_d "Я сейчас немного зла. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Не сейчас."
                                    elif ApprovalCheck(Girl, 800):
                                            $ Girl.FaceChange("sexy")
                                            if Girl is RogueX:
                                                    ch_r "Хех, может после вечеринки, [Girl.Petname]?"
                                            elif Girl is KittyX:
                                                    ch_k "Ха! Я не хочу портить вечеринку, [Girl.Petname]."
                                            elif Girl is EmmaX:
                                                    ch_e "Ох, и испачкать это платье травой?"
                                            elif Girl is LauraX:
                                                    ch_l "Хех, может позже."
                                            elif Girl is JeanX:
                                                    ch_j "Я сейчас немного занята вечеринкой."
                                            elif Girl is StormX:
                                                    ch_s "Возможно, позже, [Girl.Petname]"
                                            elif Girl is JubesX:
                                                    ch_v "Может позже?"
                                            elif Girl is GwenX:
                                                    ch_g "Эм. . . может после вечеринки. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "М?"
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. Ты правда этого хочешь?"
                                            elif Girl is WandaX:
                                                    ch_w "Давай поговорим об этом после вечеринки?"
                                    else:
                                            if Girl is RogueX:
                                                    ch_r "Мне это совсем неинтересно, [Girl.Petname]."
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
                                                    ch_v "Я не в настроении, [Girl.Petname]?"
                                            elif Girl is GwenX:
                                                    ch_g "Неа. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Я не в настроении, [Girl.Petname]. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох, эм. . . нет. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Хех, нет."

                                    return

                        "Грязный разговор (locked)":
                                        pass
                        "Свидание (locked)":
                                        pass

                        "Подарок (locked)":
                                        pass
                        "Назад":
                                        pass

            "Поговорить":
                    menu:
                        "Я просто хочу поговорить. . .":
                                    call expression Girl.Tag + "_Chitchat" #call Rogue_Chitchat
                                    return
                        "Об отношениях":
                                    ch_p "Мы можем поговорить о нас?"
                                    if Girl is RogueX:
                                            ch_r "Мне кажется, сейчас не совсем подходящий момент."
                                            ch_r "Может, позже?"
                                    elif Girl is KittyX:
                                            ch_k "Думаю, мы могли бы поговорить после вечеринки."
                                            ch_k "Может, позже?"
                                    elif Girl is EmmaX:
                                            ch_e "Мне кажется, это слегка серьезный разговор для вечеринки."
                                            ch_e "Возможно, позже."
                                    elif Girl is LauraX:
                                            ch_l "Похоже, это тяжелый разговор."
                                            ch_l "Может, позже?"
                                    elif Girl is JeanX:
                                            ch_j "Мне кажется, такие разговоры нужно вести -не- на вечеринке?"
                                    elif Girl is StormX:
                                            ch_s "Мне кажется, нам стоит обсудить это не на вечеринке."
                                            ch_s "Возможно, позже."
                                    elif Girl is JubesX:
                                            ch_v "Эм. . . Сейчас на самом деле время для этого?"
                                    elif Girl is GwenX:
                                            ch_g "Воу, как серьезно то звучит. . ."
                                            ch_g "Давай просто наслаждаться вечеринкой. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Боюсь, сейчас разговаривать об этом немного. . . странно. . ."
                                            ch_b "Пожалуйста, дождись окончания вечеринки."
                                    elif Girl is DoreenX:
                                            ch_d "Ох. . . похоже, это серьезный разговор."
                                            ch_d "Может, дождемся окончания вечеринки?"
                                    elif Girl is WandaX:
                                            ch_w "Этот разговор может подождать."
                                    return

                        "О других девушках":
                                    menu:
                                        "О [RogueX.Name_dat]?" if Girl is not RogueX:
                                                call expression Girl.Tag + "_About" pass (RogueX)
                                        "О [KittyX.Name_dat]?" if Girl is not KittyX and "met" in KittyX.History:
                                                call expression Girl.Tag + "_About" pass (KittyX)
                                        "О [EmmaX.Name_dat]?" if Girl is not EmmaX and "met" in EmmaX.History:
                                                call expression Girl.Tag + "_About" pass (EmmaX)
                                        "О [LauraX.Name_dat]?" if Girl is not LauraX and "met" in LauraX.History:
                                                call expression Girl.Tag + "_About" pass (LauraX)
                                        "О [JeanX.Name_dat]?" if Girl is not JeanX and "met" in JeanX.History:
                                                call expression Girl.Tag + "_About" pass (JeanX)
                                        "О [StormX.Name_dat]?" if Girl is not StormX and "met" in StormX.History:
                                                call expression Girl.Tag + "_About" pass (StormX)
                                        "О [JubesX.Name_dat]?" if Girl is not JubesX and "met" in JubesX.History:
                                                call expression Girl.Tag + "_About" pass (JubesX)
                                        "О [GwenX.Name_dat]?" if Girl is not GwenX and "met" in GwenX.History:
                                                call expression Girl.Tag + "_About" pass (GwenX)
                                        "О [BetsyX.Name_dat]?" if Girl is not BetsyX and "met" in BetsyX.History:
                                                call expression Girl.Tag + "_About" pass (BetsyX)
                                        "О [DoreenX.Name_dat]?" if Girl is not DoreenX and "met" in DoreenX.History:
                                                call expression Girl.Tag + "_About" pass (DoreenX)
                                        "О [WandaX.Name_dat]?" if Girl is not WandaX and "met" in WandaX.History:
                                                call expression Girl.Tag + "_About" pass (WandaX)
                                        "Поговорим о твоем отношение к другим девушкам. . .":
                                                call expression Girl.Tag + "_Monogamy" #call Rogue_Monogamy
                                        "Неважно.":
                                                pass

                        "Назад":
                                    pass

            "Изменить что-нибудь в ней":
                        call Girl_Settings

            "Неважно.":
                        if Girl is RogueX:
                                ch_r "Хорошо, тогда увидимся позже."
                        elif Girl is KittyX:
                                ch_k "Хорошо, пока."
                        elif Girl is EmmaX:
                                ch_e "Мы поговорим позже."
                        elif Girl is LauraX:
                                ch_l "Ладно."
                        elif Girl is JeanX:
                                ch_j "Ладно?"
                        elif Girl is StormX:
                                ch_s "Очень хорошо."
                        elif Girl is JubesX:
                                ch_v "Ладно?"
                        elif Girl is GwenX:
                                ch_g "Ладно. . ."
                        elif Girl is BetsyX:
                                ch_b "До свидания."
                        elif Girl is DoreenX:
                                ch_d "Ладно, пока. . ."
                        elif Girl is WandaX:
                                ch_w "Ладно, увидимся."
                        return
        jump Halloween_Chat_Menu
# End Main Chat menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_HWChat_Minimal:
    $ EmmaX.FaceChange()
    call Shift_Focus(EmmaX)
    menu:
        ch_e "[EmmaX.Petname], что ты желаешь обсудить?"
        "Ухаживать":
                menu:
                    "Флиртовать (locked)" if EmmaX.Chat[5]:
                                pass
                    "Флиртовать" if not EmmaX.Chat[5]:
                                call Emma_Flirt_Minimal
                    "Секс-меню":
                                ch_p "Не хочешь поразвлечься?"
                                if not Player.Male:
                                    ch_e "Со студенткой? Тебе должен быть известен мой ответ, [EmmaX.Petname]."
                                else:
                                    ch_e "Со студентом? Тебе должен быть известен мой ответ, [EmmaX.Petname]."
                    "Назад":
                                pass
        "Поговорить":
                menu:
                    "Я просто хочу поговорить. . .":
                                call Emma_Chitchat
                    "Об отношениях":
                                ch_p "Мы можем поговорить о нас?"
                                ch_e "Я не уверена, что сейчас подходящий момент для подобных разговоров."
                    "Назад":
                                pass
        "Изменить внешний вид [EmmaX.Name_vin]":
                    ch_p "Давай поговорим о тебе."
                    ch_e "Сомневаюсь, что тебя это касается."
        "Неважно.":
                    $ EmmaX.FaceChange("bemused",2)
                    ch_e "Хорошо. . ."
                    ch_e "Мне еще нужно. . .  кое-что уладить."
                    return
    jump Emma_HWChat_Minimal


label HWStatup(Girl=0,HWType=0,HWCheck=0,HWValue=0,HWStore=0):
        # to $ Girl.Statup("Love", 90, 1)
        # call HWStatup(RogueX,"Love", 90, 1)
        #used for applying stats only if this is the first time through.
        if Girl not in TotalGirls:
                return
        $ HWStore = getattr(Girl,HWType) #saves original value
        $ Girl.Statup(HWType,HWCheck,HWValue)
        if "halloween" in Girl.History:
                $ setattr(Girl, HWType, HWStore) #restores original value if they've done this before
        return


label Halloween_Party_Entry(HWEvents=[],HWParty=[],Costume=0,HWLine=[]): #rkeljsv
        # HWEvents is a list of events that get cycled through
        # HW Party is the girls currently at the party
        # Costume is the number of the costume you picked, one, pirate, ninja, and fireman
        # HWLine is used to play lines related to your costume
        #add introductory scene-setting here
        $ bg_current = "HW Party"
        call Remove_Girl("All")
        call Display_Background(0)
        $ Party = []
        $ Present = []
        $ Nearby = []
        "Вы выходите на площадь института, сейчас, похоже, самый разгар вечеринки."
        "Повсюду установлены столы с едой; кто-то из разодетых студентов общается друг с другой, а кто-то танцует."

        #Start Rogue Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        # Modification mode
        if "halloween" in RogueX.History:
            jump Halloween_Rogue2
        "[RogueX.Name] подходит к вам."
        # -----------------

        #display Rogue here in costume
#        call AllHide(1) #removes all girls
        $ Present.append(RogueX)
        $ RogueX.Loc = "HW Party"
        $ RogueX.AddWord(1,0,RogueX.Hair,0,"halloween")#adds "hair style" to Daily #adds "halloween" to History
        $ RogueX.OutfitDay = "costume"
        $ RogueX.Outfit = RogueX.OutfitDay
        $ RogueX.OutfitChange(Changed=1)
#        call Display_Girl(RogueX)
        call Shift_Focus(RogueX)
        show Rogue_Sprite at SpriteLoc(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        $ RogueX.FaceChange("smile")
        if not Player.Male:
            ch_r "Привет, [RogueX.Petname], приятно, что ты пришла."
            $ RogueX.FaceChange("smile",Eyes="down")
            ch_r "Похоже, ты одета как. . ."
        else:
            ch_r "Привет, [RogueX.Petname], приятно, что ты пришел."
            $ RogueX.FaceChange("smile",Eyes="down")
            ch_r "Похоже, ты одет как. . ."
        $ RogueX.FaceChange("smile")
        menu:
            extend ""
            "Пират":
                call HWStatup(RogueX,"Love", 90, 2)
                call HWStatup(RogueX,"Inbt", 50, 1)
                call HWStatup(RogueX,"Inbt", 80, 1)
                call HWStatup(RogueX,"Lust", 50, 2)
                $ Costume = 1
            "Ниндзя":
                call HWStatup(RogueX,"Love", 70, 1)
                call HWStatup(RogueX,"Love", 80, 1)
                $ Costume = 2
            "Пожарный":
                call HWStatup(RogueX,"Love", 70, 1)
                call HWStatup(RogueX,"Love", 80, 1)
                call HWStatup(RogueX,"Lust", 50, 1)
                $ Costume = 3
            "Никак":
                call HWStatup(RogueX,"Love", 80, -2)
                call HWStatup(RogueX,"Obed", 50, 1)
                call HWStatup(RogueX,"Inbt", 50, 1)
                $ RogueX.FaceChange("confused")

        if not Player.Male:
            $ HWLine = ["Ох. . . я так и подумала. . .","Ну, тогда \"Ахой\".","Оооох, выглядишь опасно. . .","Что ж, у меня наверняка найдется огонь, который ты просто обязана будешь потушить. . ."]
        else:
            $ HWLine = ["Ох. . . я так и подумала. . .","Ну, тогда \"Ахой\".","Оооох, выглядишь опасно. . .","Что ж, у меня наверняка найдется огонь, который ты просто обязан будешь потушить. . ."]
        $ HWLine = HWLine[Costume]
        ch_r "[HWLine]"
        if not Costume:
                $ RogueX.FaceChange("smile")
                ch_r "И тем не менее, добро пожаловать на вечеринку. . ."
        ch_r "Можешь угадать, кем я оделась?"
        menu:
            extend ""
            "Ада?":
                    $ RogueX.FaceChange("confused")
                    call HWStatup(RogueX,"Love", 80, -2)
                    if not Player.Male:
                        ch_r "Ну, было близко, по крайней мере, ты правильно определила игру."
                    else:
                        ch_r "Ну, было близко, по крайней мере, ты правильно определил игру."
                    $ RogueX.FaceChange("normal")
                    call HWStatup(RogueX,"Inbt", 50, 3)
                    call HWStatup(RogueX,"Inbt", 70, 2)
                    ch_r "Но нет, на самом деле, я в образе Джилл."
            "Джилл?":
                    call HWStatup(RogueX,"Love", 80, 2)
                    call HWStatup(RogueX,"Love", 90, 2)
                    call HWStatup(RogueX,"Inbt", 50, 1)
                    $ RogueX.FaceChange("smile",Eyes="surprised")
                    pause 0.4
                    $ RogueX.FaceChange("smile")
                    ch_r "В точку, [RogueX.Petname]. Ты хорошо разбираешься в персонажах."
            "Какая-то проститутка?":
                    if ApprovalCheck(RogueX, 1600) or ApprovalCheck(RogueX, 700, "O"):
                            $ RogueX.FaceChange("perplexed",2)
                            call HWStatup(RogueX,"Love", 90, -1)
                            ch_r "Что-. . . "
                            call HWStatup(RogueX,"Obed", 90, 2)
                            ch_r ". . ."
                            $ RogueX.FaceChange("sexy",1)
                            call HWStatup(RogueX,"Love", 90, 1)
                            call HWStatup(RogueX,"Lust", 50, 2)
                            ch_r "Наверное, ты очень хочешь видеть именно это. . ."
                    elif ApprovalCheck(RogueX, 1300):
                            $ RogueX.FaceChange("angry",Eyes="side")
                            call HWStatup(RogueX,"Love", 70, -2)
                            call HWStatup(RogueX,"Love", 90, -2)
                            call HWStatup(RogueX,"Obed", 50, 1)
                            ch_r "Сделаю вид, что не слышала этого. . ."
                            call HWStatup(RogueX,"Obed", 70, 1)
                            call HWStatup(RogueX,"Inbt", 50, -2)
                    else:
                            $ RogueX.FaceChange("angry")
                            call HWStatup(RogueX,"Love", 70, -2)
                            call HWStatup(RogueX,"Love", 90, -2)
                            ch_r "Ты ходишь по краю, [RogueX.Petname]. . ."
                            call HWStatup(RogueX,"Obed", 50, 1)
                            call HWStatup(RogueX,"Obed", 50, 1)
                    ch_r "Но, вообще-то, я в образе Джилл, из той игры про зомби."
            "Без понятия.":
                    call HWStatup(RogueX,"Love", 80, -2)
                    call HWStatup(RogueX,"Love", 90, -1)
                    call HWStatup(RogueX,"Inbt", 50, 1)
                    ch_r "Ладно. . . я в образе Джилл, из той игры про зомби."
            "Пропустить вступление." if "halloween" in Player.History:
                    menu:
                        "Вы уверены, что хотите пропустить вступления и сразу перейти к вечеринке?"
                        "Да":
                            jump Halloween_Skip
                        "Нет":
                            if not Player.Male:
                                ch_p "Извини, я задумалась."
                            else:
                                ch_p "Извини, я задумался."
        menu:
            extend ""
            "Выглядишь мило.":
                    $ RogueX.FaceChange("smile")
                    call HWStatup(RogueX,"Love", 80, 1)
                    call HWStatup(RogueX,"Love", 90, 2)
                    ch_r "Большое тебе спасибо, [RogueX.Petname]."
                    call HWStatup(RogueX,"Inbt", 50, 2)
                    call HWStatup(RogueX,"Inbt", 60, 1)
            "Выглядишь сексуально.":
                    $ RogueX.FaceChange("sexy",1)
                    call HWStatup(RogueX,"Love", 80, 3)
                    call HWStatup(RogueX,"Obed", 80, 2)
                    call HWStatup(RogueX,"Lust", 60, 2)
                    ch_r "Оооох, я рада, что тебе понравился мой наряд. . ."
                    call HWStatup(RogueX,"Inbt", 60, 3)
            "Мне нравится твоя прическа.":
                    $ RogueX.FaceChange("smile",1)
                    call HWStatup(RogueX,"Love", 80, 2)
                    call HWStatup(RogueX,"Love", 90, 2)
                    call HWStatup(RogueX,"Inbt", 50, 2)
                    ch_r "Ах, спасибо [RogueX.Petname]."
                    call HWStatup(RogueX,"Inbt", 70, 2)
                    ch_r "Мне тоже нравится."
            "Хорошо, а ты видела [KittyX.Name_vin]?" if "met" in KittyX.History:
                    $ RogueX.FaceChange("angry",Brows="confused")
                    call HWStatup(RogueX,"Love", 80, -2)
                    call HWStatup(RogueX,"Lust", 50, -2)
                    ch_r ". . ."
                    call HWStatup(RogueX,"Obed", 70, 2)
                    call HWStatup(RogueX,"Obed", 90, 1)
                    call HWStatup(RogueX,"Inbt", 70, 2)
                    ch_r "Да. Видела."
                    $ RogueX.FaceChange("angry",Eyes="side")
                    ch_r "Ты найдешь ее вон там."
        ch_r "В общем, мне пора, увидимся позже. . ."
        $ RogueX.FaceChange("smile")
        $ Present.remove(RogueX)
        $ Nearby.append(RogueX)
        $ RogueX.Loc = "nearby"
        show Rogue_Sprite:
                ease 0.8 pos (-200,50)
        pause 0.8
        "[RogueX.Name] уходит искать того, с кем можно еще пообщаться."
        call AllHide(1) #removes all girls
#End Rogue Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Modification mode
label Halloween_Kitty:
# -----------------
        if "met" not in KittyX.History:
                jump Halloween_Party
#Start Kitty Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        #hide Rogue here

        #display Kitty here in costume
        $ Present.append(KittyX)
        $ KittyX.Loc = "HW Party"
        $ KittyX.AddWord(1,0,KittyX.Hair,0,"halloween") #adds "halloween" to History
        $ KittyX.OutfitDay = "costume"
        $ KittyX.Outfit = KittyX.OutfitDay
        $ KittyX.OutfitChange(Changed=1)
#        call Display_Girl(KittyX)
        call Shift_Focus(KittyX)
        show Kitty_Sprite at SpriteLoc(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        $ KittyX.FaceChange("confused",Eyes="down")
        "Возле стола с закусками, вы находите [KittyX.Name_vin], рассматривающую чипсы."
        $ KittyX.FaceChange("smile")
        ch_k "О, привет!"
        $ KittyX.FaceChange("smile",Eyes="down")
        ch_k "Дай угадаю, ты. . ."
        $ KittyX.FaceChange("smile")
        if not Player.Male:
            $ HWLine = ["Ты просто "+Player.Name+" да?","Ты таинственная морячка. . .","Ооо, ты опасная убийца. . .","Ты благородная героиня."]
        else:
            $ HWLine = ["Ты просто "+Player.Name+" да?","Ты таинственный моряк. . .","Ооо, ты опасный убийца. . .","Ты благородный герой."]
        $ HWLine = HWLine[Costume]
        ch_k "[HWLine]"
        menu:
            extend ""
            "Ага.":
                    call HWStatup(KittyX,"Love", 80, 1)
                    call HWStatup(KittyX,"Love", 90, 1)
                    ch_k "Угадала с первого раза."
            "Хорошая догадка":
                    call HWStatup(KittyX,"Love", 80, 2)
                    call HWStatup(KittyX,"Love", 90, 1)
                    call HWStatup(KittyX,"Inbt", 50, 1)
                    ch_k "Оу, спасибо."
            "Нет, я [Player.Name].":
                    $ KittyX.FaceChange("confused")
                    call HWStatup(KittyX,"Love", 70, -1)
                    call HWStatup(KittyX,"Obed", 50, -1)
                    if not Costume:
                        ch_k ". . . да ну?"
                    else:
                        ch_k "Нет[KittyX.like]я знаю как тебя зовут, я имела в виду. . ."
                    ch_k "Ладно, неважно."
            "Пропустить вступление." if "halloween" in Player.History:
                    menu:
                        "Вы уверены, что хотите пропустить вступления и сразу перейти к вечеринке?"
                        "Да":
                            jump Halloween_Skip
                        "Нет":
                            if not Player.Male:
                                ch_p "Извини, я задумалась."
                            else:
                                ch_p "Извини, я задумался."
        $ KittyX.FaceChange("smile")
        ch_k "Кстати, сможешь угадать кто я?"
        menu:
            extend""
            "Аэрис":
                    call HWStatup(KittyX,"Love", 60, 4)
                    call HWStatup(KittyX,"Love", 80, 2)
                    call HWStatup(KittyX,"Love", 200, 2)
                    if not Player.Male:
                        ch_k "Ты поняла!"
                    else:
                        ch_k "Ты понял!"
            "Маленький домик в прериях?":
                    $ KittyX.FaceChange("confused",Eyes="side")
                    call HWStatup(KittyX,"Love", 70, -1)
                    call HWStatup(KittyX,"Inbt", 50, -1)
                    ch_k "А? Я думаю, это немного. . . \"по-фермерски.\"[[ПП. Не знаком с т\с \"Маленький домик в прериях\". Смысл этого варианта не уловил]"
                    $ KittyX.FaceChange("sad")
                    ch_k "Но нет, я Аэрис."
            "Китти.":
                    $ KittyX.FaceChange("confused")
                    call HWStatup(KittyX,"Love", 80, -1)
                    call HWStatup(KittyX,"Obed", 30, -1)
                    ch_k "Я. . . Да[KittyX.like]я Китти, но я спрашивала про образ."
                    ch_k "Сейчас, как бы. . . Хеллоуин?"
                    $ KittyX.FaceChange("confused",Eyes="stunned")
                    call HWStatup(KittyX,"Inbt", 50, 3)
                    call HWStatup(KittyX,"Inbt", 70, 3)
                    ch_k "Боже."
                    $ KittyX.FaceChange("angry")
                    ch_k "Я в образе Аэрис!"
                    $ KittyX.FaceChange("normal")
            "Нет?":
                    $ KittyX.FaceChange("sad")
                    call HWStatup(KittyX,"Love", 70, -1)
                    call HWStatup(KittyX,"Obed", 50, 1)
                    call HWStatup(KittyX,"Obed", 60, 1)
                    if not Player.Male:
                        ch_k "Бууу, ты могла хотя бы попытаться."
                    else:
                        ch_k "Бууу, ты мог бы хотя бы попытаться."
                    $ KittyX.FaceChange("normal")
                    ch_k "Я в образе Аэрис!"
        menu:
            extend ""
            "Выглядишь мило.":
                    $ KittyX.FaceChange("smile")
                    call HWStatup(KittyX,"Love", 80, 2)
                    call HWStatup(KittyX,"Love", 90, 1)
                    call HWStatup(KittyX,"Obed", 50, 1)
                    ch_k "Ах, спасибо, [KittyX.Petname]."
                    call HWStatup(KittyX,"Inbt", 50, 2)
            "Выглядишь сексуально.":
                    $ KittyX.FaceChange("smile",2)
                    call HWStatup(KittyX,"Love", 80, 1)
                    call HWStatup(KittyX,"Inbt", 50, 2)
                    ch_k "Думаю, мой костюм довольно простой. . ."
                    $ KittyX.FaceChange("smile",1,Eyes="side")
                    call HWStatup(KittyX,"Love", 90, 1)
                    call HWStatup(KittyX,"Obed", 50, 1)
                    ch_k "По крайней мере на фоне других. . ."
                    menu:
                        extend ""
                        "Мне интересно, что под ним.":
                                $ KittyX.FaceChange("sexy",2)
                                call HWStatup(KittyX,"Love", 60, -1)
                                call HWStatup(KittyX,"Love", 90, 1)
                                call HWStatup(KittyX,"Lust", 60, 3)
                                # Modification mode
                                if ApprovalCheck(KittyX, 750, "L") and ApprovalCheck(KittyX, 1300, TabM=2):
                                    $ KittyX.Blush = 1
                                    ch_k "Любопытной варваре на базаре нос оторвали, но, думаю, за смелость тебе полагается награда."
                                    $ KittyX.Upskirt = 1
                                    "Она приподнимает переднюю часть юбки, давая вам возможность хорошо рассмотреть ее кружевные трусики"
                                    "Несколько из студентов также мельком это видят."
                                    "Но, похоже, ее это не особо волнует."
                                    call HWStatup(KittyX,"Obed", 70, 3)
                                    call HWStatup(KittyX,"Obed", 90, 6)
                                    call HWStatup(KittyX,"Inbt", 80, 10)
                                    $ KittyX.Upskirt = 0
                                    ch_k "Ладно, хватит. . . пока."
                                elif ApprovalCheck(KittyX, 750, "L"):
                                    $ KittyX.Blush = 1
                                    "Она оглядывается по сторонам, чтобы убедиться, что никто не смотрит в ее сторону."
                                    ch_k "Ладно, взгляни одним глазком."
                                    $ KittyX.Upskirt = 1
                                    "Она приподнимает переднюю часть юбки, давая вам возможность хорошо рассмотреть ее кружевные трусики"
                                    $ KittyX.Upskirt = 0
                                    "Она быстро поправляет юбку, когда понимает, что один студент вот-вот посмотрит в ее сторону."
                                    call HWStatup(KittyX,"Obed", 70, 1)
                                    call HWStatup(KittyX,"Obed", 90, 2)
                                    call HWStatup(KittyX,"Inbt", 80, 5)
                                    ch_k "Ладно, хватит. . . пока."
                                else:
                                # ----------------
                                    ch_k "Ну, если ты будешь хорошо себя вести. . ."
                                    $ KittyX.Blush = 1
                                    call HWStatup(KittyX,"Obed", 60, 1)
                                    call HWStatup(KittyX,"Obed", 80, 2)
                                    call HWStatup(KittyX,"Inbt", 70, 1)
                        "Ага, думаю, ты права.":
                                $ KittyX.FaceChange("sad")
                                call HWStatup(KittyX,"Love", 80, -1)
                                call HWStatup(KittyX,"Love", 90, -1)
                                ch_k ". . . ох."
                                $ KittyX.FaceChange("sadside")
                                call HWStatup(KittyX,"Obed", 50, 1)
                                call HWStatup(KittyX,"Obed", 80, 1)
                                ch_k ". . ."
                                call HWStatup(KittyX,"Inbt", 50, 1)
                                ch_k "Ну, мне все равно понравился твой комплимент."
                                $ KittyX.FaceChange("normal")
            "Мне нравится твоя прическа.":
                    $ KittyX.FaceChange("confused")
                    call HWStatup(KittyX,"Love", 70, -1)
                    call HWStatup(KittyX,"Love", 90, -1)
                    ch_k "Что? . . но я. . . Ничего не делала со своими волосами. . ."
                    $ KittyX.FaceChange("normal")
            "Ладно, а ты видела других девушек?" if "met" in EmmaX.History:
                    $ KittyX.FaceChange("confused")
                    call HWStatup(KittyX,"Love", 80, -1)
                    call HWStatup(KittyX,"Obed", 50, 1)
                    call HWStatup(KittyX,"Obed", 60, 1)
                    ch_k "Ну. . ."
                    $ KittyX.FaceChange("normal",Eyes="leftside")
                    if "met" in LauraX.History:
                            ch_k "Да, [LauraX.Name] прямо вон там."
                            ch_k "Эй, [LauraX.Name]?!"
                    else:
                            ch_k "[KittyX.Like]нет?"
                    $ KittyX.FaceChange("normal")



        if "met" not in LauraX.History:
                ch_k "Ладно, я хочу сходить[KittyX.like]посмотреть на сценку вон там."
                ch_k "Может, позже еще встретимся, [KittyX.Petname]."
                call AllHide(1) #removes all girls
                $ Present.remove(KittyX)
                $ Nearby.append(KittyX)
                $ KittyX.Loc = "nearby"
                jump Halloween_Jean

#Start Laura Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        "[LauraX.Name] поднимает глаза от чаши с пуншем и замечает вас обоих."
        show Kitty_Sprite:
                ease 0.8 pos (1200,50)
        pause 0.8

        #display Laura here in costume
        $ Present.append(LauraX)
        $ LauraX.Loc = "HW Party"
        $ LauraX.AddWord(1,0,LauraX.Hair,0,"halloween") #adds "halloween" to History
        $ LauraX.OutfitDay = "costume"
        $ LauraX.Outfit = LauraX.OutfitDay
        $ LauraX.OutfitChange(Changed=1)
#        call Display_Girl(LauraX)
        call Shift_Focus(LauraX)
        show Laura_Sprite at SpriteLoc(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        show Kitty_Sprite:
                ease 0.8 pos (StageFarRight,50)
        pause 0.8
        "Она подходит к вам."

        $ LauraX.FaceChange("normal")
        ch_l "О, привет, [KittyX.Name], [Player.Name]."
        if not Player.Male:
            $ HWLine = ["Мне нравится твой образ.","Ты бездомная?","Ты ниндзя Руки?","Ты дровосек?"]
        else:
            $ HWLine = ["Мне нравится твой образ.","Ты бомж?","Ты ниндзя Руки?","Ты дровосек?"]
        $ HWLine = HWLine[Costume]
        ch_l "[HWLine]"
        if Costume:
            menu:
                extend ""
                "Ага.":
                        call HWStatup(LauraX,"Love", 80, 1)
                        ch_l "Здорово."
                "Не-а.":
                        $ LauraX.FaceChange("confused")
                        call HWStatup(LauraX,"Obed", 50, 1)
                        ch_l "Ох."
                        if Costume == 2:
                            call HWStatup(LauraX,"Love", 80, -1)
                            call HWStatup(LauraX,"Inbt", 60, 1)
                            ch_l "Ты один в один Ниндзя Руки."
                        $ LauraX.FaceChange("normal")
                "Даже не близко.":
                        $ LauraX.FaceChange("confused")
                        call HWStatup(LauraX,"Love", 80, -1)
                        call HWStatup(LauraX,"Obed", 70, 2)
                        ch_l "Ох."
                        if Costume == 2:
                            call HWStatup(LauraX,"Love", 80, -2)
                            call HWStatup(LauraX,"Inbt", 60, 2)
                            if not Player.Male:
                                ch_l "И все же ты -вылитая- Ниндзя Руки."
                            else:
                                ch_l "И все же ты -вылитый- Ниндзя Руки."
        $ KittyX.FaceChange("smile",Eyes="side")
        if not Player.Male:
            $ HWLine = ["Правда?","Она пират, глупышка!","Да, думаю, он могла бы им быть. . .","Она пожарный, глупышка!"]
        else:
            $ HWLine = ["Правда?","Он пират, глупышка!","Да, думаю, он мог бы им быть. . .","Он пожарный, глупышка!"]
        $ HWLine = HWLine[Costume]
        ch_k "[HWLine]"
        $ KittyX.FaceChange("smile")
        ch_k "Теперь угадай кто [LauraX.Name]!"
        menu:
            extend ""
            "Боксер?":
                $ LauraX.FaceChange("normal",Eyes="down")
                ch_l ". . ."
                $ LauraX.FaceChange("normal")
                call HWStatup(LauraX,"Love", 80, 1)
                ch_l "Нет."
                $ KittyX.FaceChange("angry")
                call HWStatup(KittyX,"Love", 70, -2)
                call HWStatup(KittyX,"Love", 90, 2)
                call HWStatup(KittyX,"Inbt", 50, 2)
                ch_k "Она - Тифа!"
                $ KittyX.FaceChange("smile")
            "Проститутка?":
                $ LauraX.FaceChange("sad",2)
                if ApprovalCheck(LauraX, 1600) or ApprovalCheck(LauraX, 700, "O"):
                        #she accepts this, but doesn't like it
                        call HWStatup(LauraX,"Love", 80, -2)
                        call HWStatup(LauraX,"Love", 90, -3)
                        ch_l "Обидно. . . знаешь ли. . ."
                        call HWStatup(LauraX,"Obed", 80, 3)
                        call HWStatup(LauraX,"Obed", 200, 1)
                else:
                        call Punch
                        if "partyfix" in LauraX.History:
                                call HWStatup(LauraX,"Love", 80, -2)
                                call HWStatup(LauraX,"Love", 90, -3)
                                ch_l "Только не снова эта хрень!"
                                call HWStatup(LauraX,"Obed", 80, 3)
                                call HWStatup(LauraX,"Obed", 200, 1)
                        elif "lover" in LauraX.Petnames:
                                #you should know this
                                call HWStatup(LauraX,"Love", 80, -2)
                                call HWStatup(LauraX,"Love", 90, -3)
                                ch_l "Ты же знаешь, что это не так. . ."
                                call HWStatup(LauraX,"Obed", 80, 3)
                                call HWStatup(LauraX,"Obed", 200, 1)
                                $ LauraX.AddWord(1,0,0,0,"partyfoul") #adds "partyfoul" to History
                        else:
                                #maybe you just don't know
                                call HWStatup(LauraX,"Love", 80, -2)
                                call HWStatup(LauraX,"Love", 90, -3)
                                ch_l ". . ."
                                if not Player.Male:
                                    ch_l "Если бы ты знала. . ."
                                else:
                                    ch_l "Если бы ты знал. . ."
                                $ LauraX.AddWord(1,0,0,0,"partyfoul") #adds "partyfoul" to History
                        $ LauraX.FaceChange("angry")

                        $ LauraX.AddWord(1,"angry","angry",0,0) #adds "angry" to recent/daily

                        #you pissed her off and she leaves
                        ch_l "У меня нет на это времени."
                        show Laura_Sprite:
                                ease 0.8 pos (1200,50)
                        pause 0.8
                        "[LauraX.Name] уходит с вечеринки, наверное, этим вечером вы уже ее не увидите."
                        call Remove_Girl(LauraX)

                        $ KittyX.FaceChange("angry")
                        call HWStatup(KittyX,"Love", 70, 2)
                        call HWStatup(KittyX,"Love", 90, 2)
                        ch_k "Это было грубо!"
                        ch_k "Пожалуй, я схожу[KittyX.like]посмотреть на сценку вон там."
                        show Kitty_Sprite:
                                ease 0.8 pos (1200,50)
                        pause 0.8
                        "[KittyX.Name] уходит."
                        $ KittyX.FaceChange("normal")
                        call AllHide(1) #removes all girls
                        $ Present.remove(KittyX)
                        $ Nearby.append(KittyX)
                        $ KittyX.Loc = "nearby"
                        jump Halloween_Jean

            "Тифа?":
                $ KittyX.FaceChange("smile")
                $ LauraX.FaceChange("smile")
                call HWStatup(KittyX,"Love", 60, 2)
                call HWStatup(KittyX,"Love", 90, 1)
                call HWStatup(LauraX,"Love", 90, 1)
                call HWStatup(LauraX,"Inbt", 50, 1)
                ch_l "Да, именно."
            "Откуда мне знать?":
                call HWStatup(LauraX,"Love", 90, 1)
                call HWStatup(LauraX,"Obed", 50, 1)
                call HWStatup(LauraX,"Inbt", 50, 1)
                call HWStatup(LauraX,"Inbt", 70, 1)
                ch_l "Да, и правда?"
                $ KittyX.FaceChange("surprised")
                call HWStatup(KittyX,"Love", 70, -1)
                call HWStatup(KittyX,"Love", 90, -2)
                ch_k "Она - Тифа!"
                $ KittyX.FaceChange("smile")
            "Пропустить вступление." if "halloween" in Player.History:
                    menu:
                        "Вы уверены, что хотите пропустить вступления и сразу перейти к вечеринке?"
                        "Да":
                            jump Halloween_Skip
                        "Нет":
                            if not Player.Male:
                                ch_p "Извини, я задумалась."
                            else:
                                ch_p "Извини, я задумался."

        #you didn't piss her off. . .
        ch_k "У нас связанные костюмы!"
        ch_l ". . . ага."
        ch_l "Видимо."
        menu:
            extend ""
            "Ты выглядишь великолепно!":
                    $ LauraX.FaceChange("smile")
                    call HWStatup(LauraX,"Love", 70, 1)
                    call HWStatup(LauraX,"Love", 90, 1)
                    call HWStatup(LauraX,"Inbt", 60, 2)
                    ch_l "Ага, наверное."
            "Мне нравятся твои подтяжки.":
                    $ LauraX.FaceChange("normal",Eyes="down")
                    call HWStatup(LauraX,"Love", 70, 1)
                    call HWStatup(LauraX,"Love", 90, 1)
                    ch_l "А?"
                    $ LauraX.FaceChange("smile")
                    $ LauraX.Acc = "suspenders2"
                    call HWStatup(LauraX,"Inbt", 50, 1)
                    call HWStatup(LauraX,"Inbt", 60, 1)
                    ch_l "Ага. . ."
                    $ LauraX.Acc = "suspenders"
            "Какие отличия от твоего обычного образа?":
                    $ LauraX.FaceChange("normal",Eyes="down")
                    call HWStatup(LauraX,"Love", 80, -1)
                    call HWStatup(LauraX,"Obed", 50, 1)
                    ch_l ". . ."
                    call HWStatup(LauraX,"Inbt", 50, -1)
                    ch_l "Ну. . . у меня теперь белая майка. И юбка без застежек."
                    $ LauraX.FaceChange("normal")
                    call HWStatup(LauraX,"Love", 80, -1)
                    call HWStatup(LauraX,"Inbt", 50, -1)
                    ch_l "А еще подтяжки."
        ch_k "Ладно, мы сходим[KittyX.like]посмотреть на сценку вон там."
        $ LauraX.FaceChange("normal",Eyes="leftside")
        ch_l "Мы?"
        ch_k "Ага. Пошли."
        ch_k "До скорого, [KittyX.Petname]!"
        show Kitty_Sprite:
                ease 0.8 pos (1200,50)
        show Laura_Sprite:
                ease 0.8 pos (1200,50)
        pause 0.8
        "[KittyX.Name] с [LauraX.Name_tvo] вместе уходят."
        $ LauraX.FaceChange("normal")

        call AllHide(1) #removes all girls
        $ Present.remove(KittyX)
        $ Nearby.append(KittyX)
        $ KittyX.Loc = "nearby"
        $ Present.remove(LauraX)
        $ Nearby.append(LauraX)
        $ LauraX.Loc = "nearby"

#End LauraPortion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Halloween_Jean:
        #Start Jean Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        if "met" not in JeanX.History:
                "Что ж, это показалось немного поспешным."
                # Modification mode
                jump Halloween_Storm
                # -----------------
        "Вы видите, как [JeanX.Name] подходит к столу."
        "Оооооох. . . ладно."
        "Кажется, она кричит на кого-то в бейсболке, это, возможно, Расти?"
        ch_j "Мне -все равно- что ты \"должен поймать их всех\", ты все равно не в моей лиге! [[ПП. Покемоны ориг. \"gotta catch'em all\"]"

        #add Jean arriving
        $ Present.append(JeanX)
        $ JeanX.Loc = "HW Party"
        $ JeanX.AddWord(1,0,JeanX.Hair,0,"halloween") #adds "halloween" to History
        $ JeanX.OutfitDay = "costume"
        $ JeanX.Outfit = JeanX.OutfitDay
        $ JeanX.OutfitChange(Changed=1)
#        call Display_Girl(JeanX)
        call Shift_Focus(JeanX)
        show Jean_Sprite at SpriteLoc(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        $ JeanX.FaceChange("angry",Eyes="side")
        ch_j ". . ."
        $ JeanX.FaceChange("normal",Brows="angry")
        ch_j "О, привет. . . ты выглядишь знакомо."
        $ Line = JeanX.Petname
        menu:
            extend ""
            "Это я, [Player.Name].":
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "О. Ага. Здравствуй, [JeanX.Petname]."
                ch_j "Я едва тебя узнала."
            "Это я, [Player.Name], я пират." if Costume == 1:
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "О. Да. Здравствуй, [JeanX.Petname]."
                ch_j "Я думала, ты трансвестит."
            "Я пират." if Costume == 1:
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "О, ладно. Здравствуй, \"Пират.\""
                $ JeanX.Petname = "Пират"
            "Это я, [Player.Name], я ниндзя." if Costume == 2:
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "О. Ага. Здравствуй, [JeanX.Petname]."
                ch_j "Я думала, что ты работник сцены."
            "Я ниндзя." if Costume == 2:
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "О, ладно. Здравствуй, \"Ниндзя.\""
                $ JeanX.Petname = "Ниндзя"
            "Это я, [Player.Name], я пожарный." if Costume == 3:
                $ JeanX.FaceChange("normal")
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Inbt", 50, 1)
                ch_j "О. Ага. Здравствуй, [JeanX.Petname]."
                $ JeanX.FaceChange("normal",Brows="angry")
                ch_j ". . ."
                $ JeanX.FaceChange("confused")
                ch_j "Я думала, у тебя \"способность отменять\" способности."
                ch_j "Теперь, значит, ты владеешь огнем? [[ПП. Fireman - пожарный, но Fire Man - Человек-Огонь?]"
                $ JeanX.AddWord(1,"fire",0) #adds "fire" to Recent
            "Я пожарный." if Costume == 3:
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Obed", 50, 1)
                call HWStatup(JeanX,"Inbt", 50, 1)
                $ JeanX.Petname = "Человек-Огонь"
                ch_j "О, ладно. Здравствуй, \"Человек-Огонь.\" [[ПП. Fireman - пожарный, но Fire Man - Человек-Огонь]"
                $ JeanX.AddWord(1,"fire",0) #adds "fire" to Recent
            "Пропустить вступление." if "halloween" in Player.History:
                    menu:
                        "Вы уверены, что хотите пропустить вступления и сразу перейти к вечеринке?"
                        "Да":
                            jump Halloween_Skip
                        "Нет":
                            if not Player.Male:
                                ch_p "Извини, я задумалась."
                            else:
                                ch_p "Извини, я задумался."
        if "fire" in JeanX.RecentActions:
            menu:
                extend ""
                "Нет, я одета как та, кто -тушит- огонь." if not Player.Male:
                        $ JeanX.FaceChange("surprised")
                        call HWStatup(JeanX,"Love", 90, -1)
                        call HWStatup(JeanX,"Obed", 50, 2)
                        ch_j ". . ."
                        $ JeanX.FaceChange("normal")
                        call HWStatup(JeanX,"Obed", 90, 1)
                        ch_j ". . . конечно."
                        $ JeanX.FaceChange("smile")
                        call HWStatup(JeanX,"Inbt", 80, -1)
                        ch_j "Я просто пошутила."
                "Нет, я одет как тот, кто -тушит- огонь." if Player.Male:
                        $ JeanX.FaceChange("surprised")
                        call HWStatup(JeanX,"Love", 90, -1)
                        call HWStatup(JeanX,"Obed", 50, 2)
                        ch_j ". . ."
                        $ JeanX.FaceChange("normal")
                        call HWStatup(JeanX,"Obed", 90, 1)
                        ch_j ". . . конечно."
                        $ JeanX.FaceChange("smile")
                        call HWStatup(JeanX,"Inbt", 80, -1)
                        ch_j "Я просто пошутила."
                "Да. Да, теперь я владею силой огня.":
                        $ JeanX.FaceChange("normal")
                        call HWStatup(JeanX,"Obed", 30, 1)
                        call HWStatup(JeanX,"Obed", 70, 1)
                        ch_j "Безумие."
                        call HWStatup(JeanX,"Love", 70, 2)
                        call HWStatup(JeanX,"Love", 90, 1)
                        call HWStatup(JeanX,"Lust", 50, 1)
                        ch_j "Когда-то я владела силой огня."
                        $ JeanX.FaceChange("angry",Eyes="side")
                        ch_j "Все закончилось не очень хорошо."
                        ch_j "Для узколобых дураков."

        if JeanX.Petname in ("Pirate","Ninja","Fire "+Terms['man'],"Пират","Ниндзя","Человек-Огонь"):
                menu:
                    extend ""
                    "И ты должна звать меня [Player.Name], запомнила?":
                            $ JeanX.FaceChange("normal")
                            call HWStatup(JeanX,"Love", 90, 1)
                            call HWStatup(JeanX,"Obed", 50, 1)
                            call HWStatup(JeanX,"Obed", 70, 1)
                            ch_j "О. Точно. [Line]."
                            $ JeanX.Petname = Line
                            $ Line = 0
                    "И ты должна звать меня [Line], запомнила?" if Line != Player.Name:
                            $ JeanX.FaceChange("normal")
                            call HWStatup(JeanX,"Love", 70, 1)
                            call HWStatup(JeanX,"Love", 90, 1)
                            call HWStatup(JeanX,"Obed", 70, 1)
                            ch_j "Ох. Точно. [Line]."
                            $ JeanX.Petname = Line
                            $ Line = 0
                    "Оставить уточнения":
                            $ JeanX.FaceChange("normal")
                            call HWStatup(JeanX,"Inbt", 50, 1)
        "Вы осматриваете ее костюм сверху до низу."
        menu:
            "Вы осматриваете ее костюм сверху до низу."
            "Что у тебя за образ?":
                    $ JeanX.FaceChange("smile",Eyes="side")
                    call HWStatup(JeanX,"Love", 70, 1)
                    ch_j "О. . . Я заставила одного задрота сделать мне костюм персонажа с рыжими волосами."
                    $ JeanX.FaceChange("normal")
                    ch_j "Я не знаю, какой у меня образ, но, думаю, это нормально."
                    menu:
                        extend ""
                        "Ага, я тоже не знаю.":
                                call HWStatup(JeanX,"Love", 90, 1)
                                call HWStatup(JeanX,"Obed", 50, 1)
                                call HWStatup(JeanX,"Obed", 70, 1)
                        "Ты в образе Мисти.":
                                call HWStatup(JeanX,"Love", 90, -1)
                                call HWStatup(JeanX,"Obed", 30, -1)
                                call HWStatup(JeanX,"Inbt", 50, 2)
                                ch_j "Ох, ну ладно, задрот."
            "Ты, должно быть, Мисти?":
                    $ JeanX.FaceChange("confused")
                    call HWStatup(JeanX,"Love", 90, -1)
                    call HWStatup(JeanX,"Obed", 30, -1)
                    call HWStatup(JeanX,"Inbt", 50, 2)
                    ch_j "Что еще за \"Мисти?\""
                    $ JeanX.FaceChange("angry",Eyes="side")
                    ch_j "Это та девушка, у которой сила воды?"
                    $ JeanX.FaceChange("angry",Mouth="surprised")
                    ch_j "Подожди-ка, у нас вообще есть девушка с силой воды?"
                    $ JeanX.FaceChange("normal")
                    ch_j "Короче. . . Я заставила одного задрота сделать мне костюм персонажа с рыжими волосами."
                    ch_j "У этой \"Мисти\" рыжие волосы?"
                    menu:
                        extend ""
                        "Я без понятия.":
                                call HWStatup(JeanX,"Love", 90, 1)
                                call HWStatup(JeanX,"Obed", 50, 1)
                                call HWStatup(JeanX,"Obed", 70, 1)
                        "Ага.":
                                call HWStatup(JeanX,"Love", 90, -1)
                                call HWStatup(JeanX,"Obed", 30, -1)
                                call HWStatup(JeanX,"Inbt", 50, 2)
                                ch_j "Ох, ну ладно, задрот."
            ". . . [[ничего не говорить]":
                    pass

        menu:
            extend ""
            "Ты выглядишь великолепно.":
                    $ JeanX.FaceChange("smile")
                    call HWStatup(JeanX,"Love", 70, 2)
                    call HWStatup(JeanX,"Love", 90, 1)
                    call HWStatup(JeanX,"Obed", 70, 1)
                    ch_j "Да? Неудивительно."
                    call HWStatup(JeanX,"Inbt", 50, 1)
                    ch_j "Я всегда выгляжу хорошо."
            "Мне нравится твоя прическа.":
                    $ JeanX.FaceChange("smile")
                    call HWStatup(JeanX,"Love", 70, 1)
                    call HWStatup(JeanX,"Love", 90, 1)
                    call HWStatup(JeanX,"Obed", 70, 1)
                    ch_j "Какая неожиданность."
                    call HWStatup(JeanX,"Inbt", 50, 2)
                    ch_j "Я даже могу пошевелить хвостом."
            "Почему ты не выбрала \"Джесси?\" [[\"Команда R на службе зла\" которая]":
                    $ JeanX.FaceChange("normal",Mouth="kiss")
                    call HWStatup(JeanX,"Obed", 50, 1)
                    ch_j ". . ."
                    ch_j "Что за \"Джесси?!\""
                    $ JeanX.FaceChange("angry",Eyes="side")
                    "Она оглядывается и заглядывает в глаза одному студенту."
                    $ JeanX.FaceChange("angry",Eyes="psychic")
                    ch_j "Что за \"Джесси?\""
                    $ JeanX.FaceChange("normal",Eyes="psychic")
                    ch_j ". . ."
                    $ JeanX.FaceChange("surprised")
                    call HWStatup(JeanX,"Inbt", 50, 1)
                    ch_j "О. . . она довольно крутая."
                    $ JeanX.FaceChange("angry",Eyes="side")
                    call HWStatup(JeanX,"Inbt", 50, 1)
                    ch_j "Наверное, мне стоило пойти в ее образе."
                    $ JeanX.FaceChange("normal",Eyes="psychic")
                    call HWStatup(JeanX,"Obed", 70, 1)
                    call HWStatup(JeanX,"Inbt", 70, 1)
                    ch_j "Все вы, представляйте до конца вечеринки, что я \"Джесси\"."
                    $ JeanX.FaceChange("smile",Eyes="surprised")
                    call HWStatup(JeanX,"Inbt", 70, 2)
                    "Вы слышите дружное бормотание \"да, Джесси\". . ."
                    $ JeanX.AddWord(1,"jessie",0) #adds "jessie" to Recent
        $ JeanX.FaceChange("smile")
        show Jean_Sprite:
                ease 1 pos (300,50)
        pause 1
        "[JeanX.Name] собирается уходить."
        menu:
            extend ""
            "Джин?":
                call HWStatup(JeanX,"Love", 90, 1)
                call HWStatup(JeanX,"Obed", 70, 1)
                $ JeanX.FaceChange("confused")
                ch_j "А. Да, ты еще здесь."
                $ JeanX.FaceChange("confused",Eyes="side")
                ch_j "Я собиралась по-быстрому проверить, как там обстоят дела с музыкой."
                $ JeanX.FaceChange("smile",Eyes="side")
                ch_j "Позже я, может, вернусь."
            "Пусть уходит":
                pass
        show Jean_Sprite:
                ease 0.8 pos (-200,50)
        pause 0.8
        "Она растворяется в толпе."

        call AllHide(1) #removes all girls
        $ Present.remove(JeanX)
        $ Nearby.append(JeanX)
        $ JeanX.Loc = "nearby"
        $ JeanX.FaceChange("normal")

        #End Jean Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Modification mode
label Halloween_Storm:
# -----------------
        #Start Storm Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        if "met" not in StormX.History:
                jump Halloween_Emma
        "Вы видите девушку на танцполе, и она замечает, что вы наблюдаете за ней."
        "Она, пританцовывая, направляется к вам."
        #display Storm
        $ Present.append(StormX)
        $ StormX.FaceChange("smile")
        $ StormX.Loc = "HW Party"
        $ StormX.AddWord(1,0,StormX.Hair,0,"halloween") #adds "halloween" to History
        $ StormX.OutfitDay = "costume"
        $ StormX.Outfit = StormX.OutfitDay
        $ StormX.OutfitChange(Changed=1)
#        call Display_Girl(StormX)
        call Shift_Focus(StormX)
        show Storm_Sprite at SpriteLoc(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        ch_s "Веселого Хеллоуина, [Player.Name]!"
        ch_s "Позволь мне угадать. . ."
        $ StormX.FaceChange("smile",Eyes="down")
        "Она оглядывает вас сверху вниз."
        $ StormX.FaceChange("smile")
        if not Player.Male:
            $ HWLine = ["Ты кто-то вроде бродяги? Да?","Ты - лихая разбойница!","Ты - смертоносная ниндзя Руки.",". . . Ах! Ты - доблестный борец с огнем!"]
        else:
            $ HWLine = ["Ты кто-то вроде бродяги? Да?","Ты - лихой разбойник!","Ты - смертоносный ниндзя Руки.",". . . Ах! Ты - доблестный борец с огнем!"]
        $ HWLine = HWLine[Costume]
        ch_s "[HWLine]"
        menu:
            extend ""
            "Ага, ты угадала.":
                    call HWStatup(StormX,"Love", 90, 1)
                    ch_s "Превосходно, у тебя замечательный костюм."
            "Нет, я в обычной одежде." if not Costume:
                    $ StormX.FaceChange("surprised",Eyes="normal")
                    ch_s "Ох."
                    $ StormX.FaceChange("smile")
                    ch_s "Я даже и не поняла."
                    ch_s "Пожалуй, нам с тобой стоит как-нибудь сходить по магазинам. . ."
                    ch_s "У меня есть друг, который может помочь нам с этим. . ."
            "Нет, теперь я всегда одеваюсь вот так." if Costume:
                    $ StormX.FaceChange("smile",Eyes="side")
                    call HWStatup(StormX,"Obed", 40, 1)
                    ch_s "Ох."
                    $ StormX.FaceChange("smile")
                    ch_s "Что ж, у тебя нтересный вкус."
                    call HWStatup(StormX,"Inbt", 50, 1)
                    $ StormX.FaceChange("normal",Eyes="down")
                    pause 0.4
                    $ StormX.FaceChange("smile")
                    ch_s "Пожалуй, как и у меня."
                    $ StormX.FaceChange("smile")
            "Пропустить вступление." if "halloween" in Player.History:
                    menu:
                        "Вы уверены, что хотите пропустить вступления и сразу перейти к вечеринке?"
                        "Да":
                            jump Halloween_Skip
                        "Нет":
                            if not Player.Male:
                                ch_p "Извини, я задумалась."
                            else:
                                ch_p "Извини, я задумался."
        ch_s "Сможешь угадать мой образ?"
        menu:
            extend ""
            "Ты Елена?":
                    $ StormX.FaceChange("surprised",Mouth="smile")
                    call HWStatup(StormX,"Love", 80, 1)
                    call HWStatup(StormX,"Love", 90, 1)
                    if not Player.Male:
                        ch_s "Да! Угадала!"
                    else:
                         ch_s "Да! Угадал!"
                    $ StormX.FaceChange("smile")
                    ch_s "Мне сказали, что она была популярным персонажем видеоигр."
                    $ StormX.FaceChange("smile",Eyes="stunned")
                    ch_s "И у нас с ней похожие волосы."
                    $ StormX.FaceChange("smile")
            "Это одежда с твоей родины?":
                    $ StormX.FaceChange("surprised",2,Mouth="open")
                    call HWStatup(StormX,"Love", 90, 1)
                    call HWStatup(StormX,"Obed", 50, 1)
                    ch_s "О, нет, я добивалась совсем не такой реакции."
                    $ StormX.FaceChange("normal",1)
                    ch_s "Но я понимаю свой промах."
                    $ StormX.FaceChange("smile",Eyes="down")
                    ch_s "Я действительно носила что-то подобное в Кении. . ."
                    $ StormX.FaceChange("sly")
                    call HWStatup(StormX,"Love", 90, 1)
                    ch_s "Правда топлесс."
            "Палка для колец?":
                    $ StormX.FaceChange("angry",2,Mouth="open")
                    call HWStatup(StormX,"Love", 90, -2)
                    call HWStatup(StormX,"Obed", 50, 1)
                    ch_s "Как грубо!"
                    $ StormX.FaceChange("angry",1,Mouth="open")
                    if not Player.Male:
                        ch_s "Я хочу, чтобы ты знала, это культурные украшения моего народа!"
                    else:
                        ch_s "Я хочу, чтобы ты знал, это культурные украшения моего народа!"
                    menu:
                        extend ""
                        "Извини!":
                            $ StormX.FaceChange("angry")
                            ch_s "Ох. . ."
                            call HWStatup(StormX,"Love", 70, 1)
                            call HWStatup(StormX,"Love", 90, 1)
                        "Но ты выглядишь очень сексуально.":
                            $ StormX.FaceChange("sexy")
                            ch_s "Ох, неужели?"
                            call HWStatup(StormX,"Love", 80, 1)
                            call HWStatup(StormX,"Obed", 60, 1)
                            call HWStatup(StormX,"Inbt", 80, 1)
                        "Ох, ладно.":
                            $ StormX.FaceChange("angry",Eyes="side")
                            call HWStatup(StormX,"Love", 90, -1)
                            call HWStatup(StormX,"Obed", 60, 1)
                            ch_s ". . ."
                    $ StormX.FaceChange("smile")
                    call HWStatup(StormX,"Love", 90, 2)
                    ch_s "Я просто шучу!"
                    ch_s "Я оделась как персонаж из видеоигры."
                    ch_s "Полагаю, эти кольца были придуманы кем-то в Японии."
        menu:
            extend ""
            "Ты выглядишь великолепно!":
                    call HWStatup(StormX,"Love", 80, 1)
                    call HWStatup(StormX,"Love", 90, 1)
                    ch_s "Ох, что ж, благодарю."
                    ch_s "Это очень мило с твоей стороны."
                    ch_s "Я рада, что костюм тебе понравился."
            "Мне нравится твоя новая прическа.":
                    call HWStatup(StormX,"Love", 80, 1)
                    call HWStatup(StormX,"Love", 90, 1)
                    call HWStatup(StormX,"Inbt", 70, 1)
                    ch_s "Да, и совсем не затратная."
                    ch_s "Можно носить и вне вечеринки."
            "Выглядишь очень сексуально.":
                    $ StormX.FaceChange("smile",Mouth="kiss")
                    call HWStatup(StormX,"Love", 80, 1)
                    call HWStatup(StormX,"Obed", 50, 1)
                    call HWStatup(StormX,"Inbt", 50, 1)
                    ch_s "Ох!"
                    $ StormX.FaceChange("sexy")
                    call HWStatup(StormX,"Inbt", 70, 1)
                    call HWStatup(StormX,"Lust", 60, 1)
                    ch_s "Что ж, мне тоже так кажется. . ."
            "А ты знаешь где [EmmaX.Name]?":
                    $ StormX.FaceChange("smile",Brows="confused")
                    call HWStatup(StormX,"Love", 90, -1)
                    call HWStatup(StormX,"Obed", 50, 1)
                    call HWStatup(StormX,"Obed", 70, 1)
                    if not Player.Male:
                        ch_s "Ты так быстро устала от моего общества?"
                    else:
                        ch_s "Ты так быстро устал от моего общества?"
                    $ StormX.FaceChange("smile",Eyes="side")
                    ch_s "Да, думаю, я видела ее вон под тем деревом."
                    ch_s "Передавай ей привет от меня."
        $ StormX.FaceChange("smile")
        ch_s "В общем, мне все еще нужно \"поймать волну\"."
        ch_s "Возможно, увидимся позже."
        show Storm_Sprite:
                ease 0.8 pos (1200,50)
        pause 0.8
        "[StormX.Name] скользит обратно на танцпол, а вы направляетесь к деревьям."

        call AllHide(1) #removes all girls
        $ Present.remove(StormX)
        $ Nearby.append(StormX)
        $ StormX.Loc = "nearby"

        #End Storm Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Halloween_Emma:
        #Start Emma Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        if "met" not in EmmaX.History:
                # Modification mode
                jump Halloween_Gwen
                # -----------------
        "Вы находите [EmmaX.Name_vin], стоящую под деревьями и разговаривающею с одним из студентов."

        #display Emma here in costume
        $ Present.append(EmmaX)
        $ EmmaX.Loc = "HW Party"
        $ EmmaX.FaceChange("smile")
        $ EmmaX.AddWord(1,0,EmmaX.Hair,0,"halloween") #adds "halloween" to History
        $ EmmaX.OutfitDay = "costume"
        $ EmmaX.Outfit = EmmaX.OutfitDay
        $ EmmaX.OutfitChange(Changed=1)
#        call Display_Girl(EmmaX)
        call Shift_Focus(EmmaX)
        show Emma_Sprite at SpriteLoc(-200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (-200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        ch_e "О, [EmmaX.Petname], прекрасный вечер, не правда ли?"
        menu:
            extend ""
            "Ага.":
                    pass
            "Дай угадаю, Леди Ди?":
                    $ EmmaX.FaceChange("confused")
                    call HWStatup(EmmaX,"Love", 90, -1)
                    call HWStatup(EmmaX,"Obed", 50, 1)
                    ch_e "Принцесса Диана?"
                    if not Player.Male:
                        ch_e "Нет, я понятия не имею, с чего ты это взялf, я [EmmaX.Name]."
                    else:
                        ch_e "Нет, я понятия не имею, с чего ты это взял, я [EmmaX.Name]."
                    ch_e "[EmmaX.Name]."
                    menu:
                        extend ""
                        "Ох. . . ладно.":
                                call HWStatup(EmmaX,"Love", 90, 1)
                                call HWStatup(EmmaX,"Obed", 50, 1)
                                call HWStatup(EmmaX,"Inbt", 50, 1)
                                call HWStatup(EmmaX,"Lust", 50, 1)
                                ch_e "Юная мисс Грей случайно не вторгалась в твой разум? . ."
                        "Я знаю!":
                                call HWStatup(EmmaX,"Love", 90, 1)
                                call HWStatup(EmmaX,"Obed", 50, 1)
                                call HWStatup(EmmaX,"Inbt", 50, 1)
                                call HWStatup(EmmaX,"Lust", 50, 1)
                                ch_e "Не сомневаюсь. . ."
                        "Я имела в виду гигантскую леди-вампиршу!" if not Player.Male:
                                $ EmmaX.FaceChange("confused",2,Eyes="surprised")
                                $ EmmaX.AddWord(1,"vampire",0) #adds "vampire" to Recent
                        "Я имел в виду гигантскую леди-вампиршу!" if Player.Male:
                                $ EmmaX.FaceChange("confused",2,Eyes="surprised")
                                $ EmmaX.AddWord(1,"vampire",0) #adds "vampire" to Recent
            "Дай угадаю, ты гигантская леди-вампирша?":
                    $ EmmaX.FaceChange("confused",2)
                    $ EmmaX.AddWord(1,"vampire","vampire") #adds "vampire" to Recent and Daily
            "Пропустить вступление." if "halloween" in Player.History:
                    menu:
                        "Вы уверены, что хотите пропустить вступления и сразу перейти к вечеринке?"
                        "Да":
                            jump Halloween_Skip
                        "Нет":
                            if not Player.Male:
                                ch_p "Извини, я задумалась."
                            else:
                                ch_p "Извини, я задумался."


        if "vampire" in EmmaX.RecentActions:
                call HWStatup(EmmaX,"Love", 70, -2)
                call HWStatup(EmmaX,"Love", 90, -1)
                call HWStatup(EmmaX,"Obed", 50, 1)
                #you implied that she was giant
                $ EmmaX.FaceChange("angry",1,Eyes="side")
                ch_e "Что ж, я не уверена, насколько я должна быть оскорблена твоим замечанием."
                ch_e "Не так часто меня называют \"гигантской.\""
                menu:
                    extend ""
                    "Я про твой костюм! Я имел в виду, что ты в образе гигантской леди-вампирши из игры!":
                            $ EmmaX.FaceChange("surprised",1)
                            call HWStatup(EmmaX,"Love", 90, -1)
                            ch_e "Костюм?"
                            $ EmmaX.FaceChange("confused")
                            ch_e "Какой костюм?"
                            $ EmmaX.DrainWord("vampire",1,0,0)
                    "Ну, я лишь имела в виду. . . определенные области." if not Player.Male:
                            $ EmmaX.FaceChange("angry")
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            call HWStatup(EmmaX,"Obed", 70, 1)
                            call HWStatup(EmmaX,"Inbt", 50, 1)
                            if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 400, "O"):
                                    ch_e ". . ."
                                    $ EmmaX.FaceChange("sexy")
                                    call HWStatup(EmmaX,"Love", 90, 1)
                                    call HWStatup(EmmaX,"Inbt", 50, 1)
                                    call HWStatup(EmmaX,"Lust", 50, 1)
                                    ch_e "Считай, что тебе удалось выйти сухой из воды."
                            else:
                                    call HWStatup(EmmaX,"Obed", 50, 1)
                                    ch_e "Это все еще совершенно неподобающий способ разговаривать с дамой."
                    "Ну, я лишь имел в виду. . . определенные области." if Player.Male:
                            $ EmmaX.FaceChange("angry")
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            call HWStatup(EmmaX,"Obed", 70, 1)
                            call HWStatup(EmmaX,"Inbt", 50, 1)
                            if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 400, "O"):
                                    ch_e ". . ."
                                    $ EmmaX.FaceChange("sexy")
                                    call HWStatup(EmmaX,"Love", 90, 1)
                                    call HWStatup(EmmaX,"Inbt", 50, 1)
                                    call HWStatup(EmmaX,"Lust", 50, 1)
                                    ch_e "Считай, что тебе удалось выйти сухим из воды."
                            else:
                                    call HWStatup(EmmaX,"Obed", 50, 1)
                                    ch_e "Это все еще совершенно неподобающий способ разговаривать с дамой."
                    "У тебя прямо гигантские сиськи.":
                            $ EmmaX.FaceChange("angry")
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            call HWStatup(EmmaX,"Obed", 70, 1)
                            call HWStatup(EmmaX,"Inbt", 70, 1)
                            if ApprovalCheck(EmmaX, 1300) or ApprovalCheck(EmmaX, 500, "O"):
                                    ch_e ". . ."
                                    $ EmmaX.FaceChange("sexy")
                                    call HWStatup(EmmaX,"Love", 90, 1)
                                    call HWStatup(EmmaX,"Inbt", 50, 1)
                                    call HWStatup(EmmaX,"Lust", 50, 1)
                                    call HWStatup(EmmaX,"Lust", 60, 1)
                                    ch_e "Пожалуй, я не могу не согласиться."
                            else:
                                    call HWStatup(EmmaX,"Love", 90, -1)
                                    call HWStatup(EmmaX,"Inbt", 50, 1)
                                    call HWStatup(EmmaX,"Lust", 50, 1)
                                    ch_e "-Тебе- стоит очистить свой разум от мусора."
                    "Извини, не бери в голову. . .":
                            $ EmmaX.FaceChange("angry",Eyes="side")
                            call HWStatup(EmmaX,"Love", 90, 1)
                            call HWStatup(EmmaX,"Inbt", 50, 1)
                            ch_e "Что ж. . . Полагаю, я могу спустить тебе это с рук."
                            $ EmmaX.FaceChange("normal")
                            ch_e "Тем не менее, это было очень необычное замечание."
        if "vampire" in EmmaX.RecentActions:
                $ EmmaX.FaceChange("normal",Brows="confused")
                ch_e "И почему \"вампирша?\""
                ch_e "Ты думаешь, я провожу слишком много времени с мисс Ли?"
                menu:
                    extend ""
                    "Эм, ага.":
                            $ EmmaX.FaceChange("normal",Eyes="side")
                            call HWStatup(EmmaX,"Love", 90, 2)
                            ch_e "Но не настолько же, чтобы заразиться ее. . . недугом."
                    "Что? О, не бери в голову.":
                            $ EmmaX.FaceChange("normal")
                            call HWStatup(EmmaX,"Love", 90, 1)
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            ch_e "Что ж, как скажешь. . ."
                    "Я про твой костюм! Я имел в виду, что ты в образе гигантской леди-вампирши из игры!" if Player.Male:
                            $ EmmaX.FaceChange("surprised",1)
                            call HWStatup(EmmaX,"Love", 90, -1)
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            ch_e "Костюм?"
                            $ EmmaX.FaceChange("confused")
                            ch_e "Какой костюм?"
                            $ EmmaX.DrainWord("vampire",1,0,0)
                    "Я про твой костюм! Я имела в виду, что ты в образе гигантской леди-вампирши из игры!" if not Player.Male:
                            $ EmmaX.FaceChange("surprised",1)
                            call HWStatup(EmmaX,"Love", 90, -1)
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            ch_e "Костюм?"
                            $ EmmaX.FaceChange("confused")
                            ch_e "Какой костюм?"
                            $ EmmaX.DrainWord("vampire",1,0,0)
        $ EmmaX.FaceChange("normal",Eyes="down")
        ch_e "Я слышала, что это будет \"костюмированная\" вечеринка, так что я просто оделась по случаю."
        $ EmmaX.FaceChange("angry",Eyes="side")
        if not Player.Male:
            ch_e "Теперь, когда ты об этом упомянула, я вижу, что многие студенты одеты немного. . . вычурно."
        else:
            ch_e "Теперь, когда ты об этом упомянул, я вижу, что многие студенты одеты немного. . . вычурно."
        $ EmmaX.FaceChange("angry",Eyes="down")
        if not Player.Male:
            ch_e "Это объясняет, почему ты одета как. . ."
        else:
            ch_e "Это объясняет, почему ты одет как. . ."
        if not Player.Male:
            $ HWLine = ["Что ж, полагаю, ты выглядишь как и всегда.","Морская разбойница?","Воришка?","Пожарный?"]
        else:
            $ HWLine = ["Что ж, полагаю, ты выглядишь как и всегда.","Морской разбойник?","Воришка?","Пожарный?"]
        $ EmmaX.FaceChange("normal",Brows="confused")
        $ HWLine = HWLine[Costume]
        if not Player.Male and Costume == 1:
            $ HWLine = "Своенравная цыганка?"
        ch_e "[HWLine]"
        if Costume == 1:
            menu:
                extend ""
                "Так точно, я \"морской насильник.\"" if Player.Male:
                        $ EmmaX.FaceChange("smile",Brows="surprised")
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 70, 1)
                        call HWStatup(EmmaX,"Lust", 50, 2)
                        ch_e "Ха! У тебя такие грязные мыслишки."
                        $ EmmaX.FaceChange("sly")
                        ch_e "Нам лучше найти им достойное применение. . ."
                "Береги свои прелести. . ." if not Player.Male:
                        $ EmmaX.FaceChange("smile",)
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 70, 1)
                        call HWStatup(EmmaX,"Lust", 50, 2)
                        ch_e "Ха! У тебя такие грязные мыслишки."
                        $ EmmaX.FaceChange("sly")
                        ch_e "Нам лучше найти им достойное применение. . ."
                "Я пират, вообще-то. . .":
                        $ EmmaX.FaceChange("smile")
                        call HWStatup(EmmaX,"Love", 90, 1)
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        ch_e "О, да! Из тебя получился настоящий мародер."
        elif Costume == 2:
            menu:
                extend ""
                "Думаю, кое-что я могла бы прикарманить. . ." if not Player.Male:
                        $ EmmaX.FaceChange("smile",Brows="confused")
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 50, 1)
                        ch_e "Наверное, лучше не надо. . ."
                "Думаю, кое-что я мог бы прикарманить. . ." if Player.Male:
                        $ EmmaX.FaceChange("smile",Brows="confused")
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 50, 1)
                        ch_e "Наверное, лучше не надо. . ."
                "Я ниндзя, вообще-то.":
                        $ EmmaX.FaceChange("smile")
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 50, 1)
                        ch_e "Ах! Мне кажется, ты немного смахиваешь на Ниндзя Руки."
            $ EmmaX.FaceChange("smile")
        elif Costume == 3:
            menu:
                extend ""
                "Нет, я. . . а, да, я пожарный.":
                        $ EmmaX.FaceChange("smile")
                        call HWStatup(EmmaX,"Love", 90, 1)
                        call HWStatup(EmmaX,"Obed", 60, 1)
                        call HWStatup(EmmaX,"Inbt", 60, 1)
                        ch_e "Я сразу это поняла. . ."
                "Ты угадала!":
                        $ EmmaX.FaceChange("smile")
                        call HWStatup(EmmaX,"Love", 90, 1)
                        call HWStatup(EmmaX,"Inbt", 50, 1)
                        call HWStatup(EmmaX,"Inbt", 70, 1)
                        ch_e "Конечно!"
            $ EmmaX.FaceChange("sly")
            call HWStatup(EmmaX,"Lust", 50, 2)
            call HWStatup(EmmaX,"Lust", 70, 1)
            ch_e "У меня есть небольшой опыт общения с пожарными. . ."
        else:
            menu:
                extend ""
                "О, да?":
                        $ EmmaX.FaceChange("sad")
                        call HWStatup(EmmaX,"Love", 90, -1)
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        ch_e "Это. . . нормально."
                "Мне не хотелось наряжаться.":
                        call HWStatup(EmmaX,"Love", 90, -1)
                        call HWStatup(EmmaX,"Obed", 50, 1)
                        call HWStatup(EmmaX,"Obed", 70, 1)
                        ch_e "Я. . . понимаю. . ."
            $ EmmaX.FaceChange("angry", Eyes="side")
            ch_e "Впрочем, как-нибудь нам с тобой нужно будет пройтись по магазинам. . ."
        $ EmmaX.FaceChange("normal",Brows="sad")
        ch_e "А тебе есть что сказать обо мне?"
        menu:
            extend ""
            "Да не особо.":
                    if ApprovalCheck(EmmaX, 1200) or ApprovalCheck(EmmaX, 400, "O"):
                            $ EmmaX.FaceChange("sadside")
                            call HWStatup(EmmaX,"Love", 90, -1)
                            call HWStatup(EmmaX,"Obed", 70, 2)
                            call HWStatup(EmmaX,"Obed", 90, 1)
                            ch_e "Ох. . ."
                            ch_e "Жаль."
                    else:
                            $ EmmaX.FaceChange("angry")
                            call HWStatup(EmmaX,"Love", 80, -2)
                            call HWStatup(EmmaX,"Love", 90, -1)
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            ch_e "Ну хорошо!"
                            ch_e "Пожалуй, мне не стоило спрашивать прямо."

            "О, хорошо выглядишь.":
                    $ EmmaX.FaceChange("smile")
                    call HWStatup(EmmaX,"Love", 70, 2)
                    call HWStatup(EmmaX,"Love", 90, 1)
                    call HWStatup(EmmaX,"Inbt", 50, 1)
                    ch_e "Я рада, что ты умеешь ценить прекрасное."
            "Мне нравится твоя шляпа.":
                    $ EmmaX.FaceChange("smile",Eyes="stunned")
                    call HWStatup(EmmaX,"Love", 80, 1)
                    call HWStatup(EmmaX,"Love", 90, 2)
                    call HWStatup(EmmaX,"Obed", 70, 1)
                    call HWStatup(EmmaX,"Inbt", 70, 1)
                    ch_e "О, да, я увидела ее в магазине и подумала, что она должна быть у меня. . ."
                    $ EmmaX.FaceChange("smile")
            "Ты прямо вылитая леди-вампирша.":
                    if "vampire" in EmmaX.RecentActions:
                            $ EmmaX.FaceChange("angry",2,Eyes="surprised")
                            call HWStatup(EmmaX,"Love", 80, -1)
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            ch_e "Я понятия не имею, о чем ты говоришь!"
                    else:
                            $ EmmaX.FaceChange("angry",2)
                            call HWStatup(EmmaX,"Obed", 50, 1)
                            call HWStatup(EmmaX,"Obed", 70, 1)
                            ch_e "Что ж, я уверена, что любое сходство -абсолютно- случайно."
                            $ EmmaX.FaceChange("angry",1)
                            ch_e "Тебе все -ясно?-"
                    $ EmmaX.FaceChange("normal",1)
        ch_e "В общем. . ."
        ch_e "Приятно было немного поболтать. . . Надеюсь, позже увидимся."
        ch_e "А сейчас я должна удалиться."
        show Emma_Sprite:
                ease 0.8 pos (-200,50)
        pause 0.8
        "[EmmaX.Name] уходит в направлении стола с закусками."

        call AllHide(1) #removes all girls
        $ Present.remove(EmmaX)
        $ Nearby.append(EmmaX)
        $ EmmaX.Loc = "nearby"

        #End Emma Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Modification mode
label Halloween_Gwen:
# -----------------
        #Start Gwen portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        "Вы видите, как кто-то кого-то подбадривает у аттракциона по прыжкам за яблоками. Вы решаете сходить и посмотреть в чем дело."
        if "met" not in GwenX.History:
                # Modification mode
                jump Halloween_Jubes
                # -----------------
        "Вы замечаете какую-то движуху на краю вечеринки и направляетесь туда."
        #display Gwen
        $ Present.append(GwenX)
        $ GwenX.FaceChange("smile")
        $ GwenX.Loc = "HW Party"
        $ GwenX.AddWord(1,0,GwenX.Hair,0,"halloween") #adds "halloween" to History
        $ GwenX.OutfitDay = "costume"
        $ GwenX.Outfit = GwenX.OutfitDay
        $ GwenX.OutfitChange(Changed=1)
#        call Display_Girl(GwenX)
        call Shift_Focus(GwenX)
        show Gwen_Sprite at SpriteLoc(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8
        ch_g "О, [Player.Name]. Я так и думала, что рано или поздно ты появишься."
        if not Player.Male:
            ch_g "Так, и кем же ты вырядилась?"
            $ HWLine = ["Ты выглядишь как героиня какой-то хентай-игры.","Ты Владыка пиратов?","О, от тебя так и веет японщиной!","А, пожарный, классика."]
        else:
            ch_g "Так, и кем же ты вырядился?"
            $ HWLine = ["Ты выглядишь как герой какой-то хентай-игры.","Ты Владыка пиратов?","О, от тебя так и веет японщиной!","А, пожарный, классика."]
        $ HWLine = HWLine[Costume]
        ch_g "[HWLine]"
        menu:
            extend ""
            "Угадала.":
                    call HWStatup(GwenX,"Love", 80, 1)
                    call HWStatup(GwenX,"Obed", 70, 1)
                    $ GwenX.FaceChange("smile",Mouth="smirk")
                    if not Player.Male:
                        ch_g "Ты хорошо подготовилась, мне нравится."
                    else:
                        ch_g "Ты хорошо подготовился, мне нравится."
            "Я не знаю, почему все думают, что я кем-то вырядился." if not Costume and Player.Male:
                    call HWStatup(GwenX,"Love", 80, 2)
                    call HWStatup(GwenX,"Obed", 70, 1)
                    call HWStatup(GwenX,"Inbt", 70, 1)
                    $ GwenX.FaceChange("smile",Mouth="smirk")
                    ch_g "Ха, ну значит я угадала."
            "Я не знаю, почему все думают, что я кем-то вырядилась." if not Costume and not Player.Male:
                    call HWStatup(GwenX,"Love", 80, 2)
                    call HWStatup(GwenX,"Obed", 70, 1)
                    call HWStatup(GwenX,"Inbt", 70, 1)
                    $ GwenX.FaceChange("smile",Mouth="smirk")
                    ch_g "Ха, ну значит я угадала."
            "Я ниндзя." if Costume == 2:
                    $ GwenX.FaceChange("smile",Mouth="smirk")
                    if not Player.Male:
                        ch_g "Конечно, милая."
                    else:
                        ch_g "Конечно, милый."
            "А почему не \"Королева пиратов?\"" if Costume == 1 and not Player.Male:
                    ch_g "Я выбрала гендерно нейтральный термин."
            "А почему не пожарная?" if Costume == 3 and not Player.Male:
                    ch_g "Я выбрала гендерно нейтральный термин."
            "Близко.":
                    $ GwenX.FaceChange("confused")
                    ch_g "Ладно. . ."
        $ GwenX.FaceChange("smile")
        ch_g "Уверена, ты не сможешь разгадать мой образ."
        $ Line = 0
        while Line < 2:
            menu:
                extend ""
                "Стриптизерша?":
                        if ApprovalCheck(GwenX, 1200):
                                call HWStatup(GwenX,"Love", 90, 1)
                                call HWStatup(GwenX,"Obed", 60, 2)
                                call HWStatup(GwenX,"Obed", 80, 1)
                                $ GwenX.FaceChange("smile",Mouth="smirk")
                        else:
                                call HWStatup(GwenX,"Love", 60, -1)
                                call HWStatup(GwenX,"Love", 80, -2)
                                call HWStatup(GwenX,"Obed", 70, 1)
                                $ GwenX.FaceChange("angry",Mouth="smirk")
                        ch_g "Уверена, ты говоришь это всем девушкам. . ."
                        $ Line = 2
                "Чирлидерша?":
                        $ GwenX.FaceChange("smile",Eyes="side")
                        ch_g "Так-то да, но. . ."
                        $ Line = 2
                "Образ из игры Lollipop. . . что-то там?":
                        ch_g "Нет, ты никогда-"
                        call HWStatup(GwenX,"Love", 60, 1)
                        call HWStatup(GwenX,"Obed", 70, 1)
                        ch_g "Нет, ты никогда- Да!"
                        call HWStatup(GwenX,"Love", 95, 2)
                        if not Player.Male:
                            ch_g "В точку, не могу поверить, что ты угадала."
                        else:
                            ch_g "В точку, не могу поверить, что ты угадал."
                        $ Line = 2
                "Школьница?":
                        call HWStatup(GwenX,"Love", 90, -1)
                        call HWStatup(GwenX,"Inbt", 70, -1)
                        $ GwenX.FaceChange("smile",Eyes="side")
                        ch_g "В каком-то роде. . ."
                        $ Line = 2
                "Маленькая девочка?":
                        call HWStatup(GwenX,"Love", 80, -2)
                        call HWStatup(GwenX,"Inbt", 70, -1)
                        $ GwenX.FaceChange("angry",2)
                        ch_g "Эм. . . нет."
                        $ Line = 2
                "Я не хочу гадать." if Line < 1:
                        call HWStatup(GwenX,"Obed", 50, 1)
                        call HWStatup(GwenX,"Obed", 80, 1)
                        ch_g "Давай, здесь множественный выбор!"
                        call HWStatup(GwenX,"Love", 70, -1)
                        ch_g "Один из вариантов -должен- быть верным."
                        $ Line = 1
        $ Line = 0
        $ GwenX.FaceChange("smile",1)
        ch_g "Я героиня из зомби файтинга, мне всегда нравился ее внешний вид."
        menu:
            extend ""
            "Ну, тебе отлично подходит этот костюм.":
                    call HWStatup(GwenX,"Love", 90, 1)
                    call HWStatup(GwenX,"Inbt", 50, 1)
                    call HWStatup(GwenX,"Inbt", 70, 1)
                    ch_g "Правда?"
            "Выглядишь очень сексуально.":
                    call HWStatup(GwenX,"Obed", 70, 1)
                    call HWStatup(GwenX,"Inbt", 50, 1)
                    call HWStatup(GwenX,"Inbt", 70, 1)
                    if ApprovalCheck(GwenX, 1000):
                            call HWStatup(GwenX,"Love", 90, 1)
                            $ GwenX.FaceChange("smile",2)
                            ch_g "Хехе. . ."
                    else:
                            call HWStatup(GwenX,"Obed", 70, 1)
                            ch_g "Ага, наверное, так оно и есть, спасибо."
                    $ GwenX.FaceChange("smile",1)
            "Мне нравится твоя прическа.":
                    call HWStatup(GwenX,"Love", 90, 1)
                    call HWStatup(GwenX,"Inbt", 70, 1)
                    $ GwenX.FaceChange("smile",Eyes="side")
                    ch_g "Спасибо, я могла бы ходить с ней чаще. . ."
            "Могу поспорить, я тебя заборю.":
                    call HWStatup(GwenX,"Obed", 70, 1)
                    if ApprovalCheck(GwenX, 1200):
                            call HWStatup(GwenX,"Love", 90, 1)
                            call HWStatup(GwenX,"Inbt", 50, 1)
                            call HWStatup(GwenX,"Inbt", 70, 1)
                            $ GwenX.FaceChange("smile",2,Eyes="side")
                            ch_g "Хехе."
                    elif GwenX.SEXP >= 15:
                            call HWStatup(GwenX,"Love", 80, -1)
                            $ GwenX.FaceChange("confused",2)
                            ch_g "Ну, наверное, но это прозвучало грубо."
                    else:
                            call HWStatup(GwenX,"Love", 70, -2)
                            call HWStatup(GwenX,"Love", 90, -1)
                            call HWStatup(GwenX,"Obed", 80, 1)
                            ch_g "Вот можешь ты настроение испортить. . ."
            "Ладно, пока.":
                    call HWStatup(GwenX,"Love", 90, -1)
                    call HWStatup(GwenX,"Obed", 50, 1)
                    call HWStatup(GwenX,"Obed", 70, 1)
                    $ GwenX.FaceChange("smile",Brows="sad")
                    ch_g "Уже двигаешься дальше по сюжету, да?"
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "В любом случае, тут обстановка накаляется, поговорим позже."
        "Она возвращается к наблюдению за аттракционом по ныряниям за яблоками."
        $ GwenX.FaceChange("smile",Eyes="down",Mouth="open")
        ch_g "Давай, ты сможешь!"
        ch_g "Вгрызайся в это яблоко!"
        ch_g "Я знаю, ты можешь лучше!"
        show Gwen_Sprite:
                ease 0.8 pos (1200,50)
        pause 0.8
        "Вы продолжаете свой обход вечеринки. . ."
        $ GwenX.FaceChange("smile")
        call AllHide(1) #removes all girls
        $ Present.remove(GwenX)
        $ Nearby.append(GwenX)
        $ GwenX.Loc = "nearby"
        #End Gwen portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


        #Start Jubes Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Halloween_Jubes:
        if "met" not in JubesX.History:
        # Modification mode
                jump Halloween_Betsy
        if "halloween" in JubesX.History:
            jump Halloween_Jubes2
        # -----------------
        "Вы замечаете какую-то движуху на краю вечеринки и направляетесь туда."
        #display Jubes
        $ Present.append(JubesX)
        $ JubesX.FaceChange("smile")
        $ JubesX.Loc = "HW Party"
        $ JubesX.AddWord(1,0,JubesX.Hair,0,"halloween") #adds "halloween" to History
        $ JubesX.OutfitDay = "costume"
        $ JubesX.Outfit = JubesX.OutfitDay
        $ JubesX.OutfitChange(Changed=1)
#        call Display_Girl(JubesX)
        call Shift_Focus(JubesX)
        show Jubes_Sprite at SpriteLoc(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        $ JubesX.ArmPose = 2
        ch_v "О, привет, [Player.Name]."
        ch_v "Хм, дай-ка я рассмотрю тебя. . ."
        $ JubesX.FaceChange("smile",Eyes="down")
        "Она оглядывает вас сверху вниз."
        $ JubesX.FaceChange("smile")
        if not Player.Male:
            $ HWLine = ["Пришла как \"бродяга?\"","Йо хо хо хо хо!","Нин-нин, да?","О, мне кажется, я начинаю пылать. . ."]
        else:
            $ HWLine = ["Пришел как \"случайный придурок?\"","Йо хо хо хо хо!","Нин-нин, да?","О, мне кажется, я начинаю пылать. . ."]
        $ HWLine = HWLine[Costume]
        $ JubesX.ArmPose = 1
        ch_v "[HWLine]"
        menu:
            extend ""
            "Ага.":
                    $ JubesX.ArmPose = 2
                    call HWStatup(JubesX,"Love", 90, 1)
                    if not Costume:
                            call HWStatup(JubesX,"Love", 90, 1)
                            ch_v "[[Ха]"
                    ch_v "Тебе идет."
            "Эй!" if not Costume:
                    $ JubesX.ArmPose = 2
                    $ JubesX.FaceChange("smile",Mouth="open",Eyes="closed")
                    ch_v "Ахахаха!"
                    $ JubesX.FaceChange("sadside",Mouth="normal")
                    ch_v "Извини. . ."
                    $ JubesX.FaceChange("smile")
                    ch_v "Но я ни о чем не жалею."
            "Нет, теперь я всегда одеваюсь вот так." if Costume:
                    $ JubesX.ArmPose = 2
                    $ JubesX.FaceChange("smile")
                    call HWStatup(JubesX,"Obed", 40, 1)
                    ch_v "Хех, конечно."
                    call HWStatup(JubesX,"Inbt", 50, 1)
                    ch_v "Нууу, тебе идет."
            "Пропустить вступление." if "halloween" in Player.History:
                    $ JubesX.ArmPose = 2
                    menu:
                        "Вы уверены, что хотите пропустить вступления и сразу перейти к вечеринке?"
                        "Да":
                            jump Halloween_Skip
                        "Нет":
                            if not Player.Male:
                                ch_p "Извини, я задумалась."
                            else:
                                ch_p "Извини, я задумался."
        ch_v "Ладно, а как ты думаешь, кто я?"
        menu:
            extend ""
            "Кармилла?":
                    $ JubesX.FaceChange("confused")
                    ch_v "Кто?"
                    $ JubesX.FaceChange("smile")
                    ch_v "Нет, я Ада из той же игры, что и [RogueX.Name] с [EmmaX.Name_tvo]."
                    ch_v "Я решила, что платье мне к лицу."
            "Ада?":
                    $ JubesX.FaceChange("surprised",Mouth="open")
                    call HWStatup(JubesX,"Love", 80, 1)
                    call HWStatup(JubesX,"Love", 90, 1)
                    $ JubesX.ArmPose = 1
                    ch_v "Ага!"
                    $ JubesX.FaceChange("sly")
                    ch_v "Я подумала, раз [EmmaX.Name] взяла на себя роль \"вампирши\", то это может быть забавно."
                    ch_v "Да и красный мне идет. . ."
                    $ JubesX.ArmPose = 2
            "Откуда мне знать? Ты просто в красном платье.":
                    $ JubesX.FaceChange("angry",2,Mouth="open")
                    call HWStatup(JubesX,"Love", 90, -2)
                    call HWStatup(JubesX,"Obed", 50, 1)
                    ch_v "Эй!"
                    $ JubesX.FaceChange("sadside",1)
                    ch_v "Хорошо. . . Признаю, что это немного \"халтурный косплей\". . ."
                    $ JubesX.FaceChange("sly",1)
                    ch_v "У меня в шкафу висело это сексуальное платье и я решила его надеть. . ."
                    ch_v "В общем, я -типа- Ада из той же игры, что и [RogueX.Name] с [EmmaX.Name_tvo]."
        ch_v "У меня даже есть подходящая мини-юбка в моем шкафу."
        menu:
            extend ""
            "Ты выглядишь великолепно!":
                    call HWStatup(JubesX,"Love", 80, 1)
                    call HWStatup(JubesX,"Love", 90, 1)
                    ch_v "Оу, спасибо."
                    if not Player.Male:
                        ch_v "Я рада, что ты оценила. . ."
                    else:
                        ch_v "Я рада, что ты оценил. . ."
            "Мне нравится твоя новая прическа.":
                    call HWStatup(JubesX,"Love", 80, -2)
                    $ JubesX.FaceChange("confused")
                    ch_v ". . . Это моя обычная прическа."
                    ch_v "То есть, я, конечно, сняла очки и все такое, но. . ."
            "Выглядишь очень сексуально.":
                    $ JubesX.FaceChange("sly")
                    call HWStatup(JubesX,"Obed", 50, 1)
                    call HWStatup(JubesX,"Inbt", 50, 1)
                    call HWStatup(JubesX,"Lust", 60, 1)
                    if not Player.Male:
                        ch_v "Рада, что ты заметила. . ."
                    else:
                        ch_v "Рада, что ты заметил. . ."
                    call HWStatup(JubesX,"Inbt", 70, 1)
                    call HWStatup(JubesX,"Love", 80, 1)
            "Я не помню, чтобы у тебя были чулки. . ." if "stockings and garterbelt" not in JubesX.Inventory:
                    call HWStatup(JubesX,"Love", 90, 1)
                    call HWStatup(JubesX,"Obed", 80, 1)
                    $ JubesX.FaceChange("smile",Eyes="down")
                    ch_v "Ну, да. . ."
                    $ JubesX.FaceChange("smile")
                    ch_v "Я одолжила их для вечеринки. . ."
                    menu:
                        extend ""
                        "Они подчеркивают твой образ.":
                                call HWStatup(JubesX,"Love", 90, 1)
                                call HWStatup(JubesX,"Obed", 80, 1)
                                $ JubesX.FaceChange("sly",2,Eyes="side")
                                if "lace bra" not in JubesX.Inventory or "lace panties" not in JubesX.Inventory:
                                        ch_v "Мне, эм. . . также пришлось одолжить нижнее белье. . ."
                                        $ JubesX.FaceChange("sexy",1)
                        "Ох, ладно.":
                                call HWStatup(JubesX,"Love", 90, -1)
                                call HWStatup(JubesX,"Obed", 80, 2)
                                $ JubesX.FaceChange("angry")
                                ch_v ". . ."
                                $ JubesX.FaceChange("normal")

        ch_v "Я немного сомневалась насчет вечеринки в честь Хэллоуина. . ."
        menu:
            extend ""
            "Из-за клоунов?":
                    $ JubesX.FaceChange("perplexed")
                    call HWStatup(JubesX,"Inbt", 70, 1)
                    ch_v "Что?"
                    $ JubesX.FaceChange("smile")
                    ch_v "Нет. . . меня совсем не волнуют клоуны. . ."
                    $ JubesX.FaceChange("sadside")
                    ch_v "Все из-за того, что я вампир. . ."
            "Потому что ты вампир?":
                    call HWStatup(JubesX,"Love", 80, 1)
                    call HWStatup(JubesX,"Love", 90, 1)
                    $ JubesX.FaceChange("sadside")
                    ch_v ". . . Ага."
            "Почему?":
                    $ JubesX.FaceChange("sadside")
                    ch_v "Ну, понимаешь. . . "
                    ch_v "-потому что я теперь вампир. . ."
        menu:
            extend ""
            "О, да, я понимаю.":
                    call HWStatup(JubesX,"Love", 80, 1)
                    call HWStatup(JubesX,"Love", 90, 1)
                    $ JubesX.FaceChange("normal",Brows="sad")
                    ch_v "Спасибо. . ."
            "Это совсем не важно.":
                    call HWStatup(JubesX,"Love", 80, 2)
                    $ JubesX.FaceChange("normal")
                    ch_v ". . . да, спасибо. . ."
            "Как глупо.":
                    $ JubesX.FaceChange("angry")
                    call HWStatup(JubesX,"Love", 90, -2)
                    call HWStatup(JubesX,"Obed", 50, 1)
                    call HWStatup(JubesX,"Obed", 80, 1)
                    ch_v ". . ."
        ch_v "Я понимаю, что на самом деле это не так уж и важно, ну, что такое еще один \"монстр\" на Хэллоуин?"
        ch_v ". . ."
        $ JubesX.FaceChange("smile")
        ch_v "Но хватит об этом, мы же все-таки на вечеринке!"
        ch_v "Что ж, увидимся позже?"
        show Jubes_Sprite:
                ease 0.8 pos (1200,50)
        pause 0.8
        "[JubesX.Name] уходит общаться с остальными."

        call AllHide(1) #removes all girls
        $ Present.remove(JubesX)
        $ Nearby.append(JubesX)
        $ JubesX.Loc = "nearby"

        #End Jubes Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Modification mode
label Halloween_Betsy:
# -----------------
        #Start Betsy Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        if "met" not in BetsyX.History:
        # Modification mode
                jump Halloween_Doreen
        if "halloween" in BetsyX.History:
            jump Halloween_Betsy2
        # -----------------
        "Вы замечаете новую гостью на вечеринке."
        "Увидев вас, она направилась в вашу сторону."
        #display Betsy
        $ Present.append(BetsyX)
        $ BetsyX.FaceChange("smile")
        $ BetsyX.Loc = "HW Party"
        $ BetsyX.AddWord(1,0,BetsyX.Hair,0,"halloween") #adds "halloween" to History
        $ BetsyX.OutfitDay = "costume"
        $ BetsyX.Outfit = BetsyX.OutfitDay
        $ BetsyX.OutfitChange(Changed=1)
#        call Display_Girl(BetsyX)
        call Shift_Focus(BetsyX)
        show Betsy_Sprite at SpriteLoc(1200,50):
                offset (0,0)
                anchor (0.5, 0.0)
                pos (1200,50)
                ease 0.8 pos (StageCenter,50)
        pause 0.8

        ch_b "Какой прекрасный вечер, [Player.Name]!"
        ch_b "Я всегда мечтала побывать на \"настоящей американской Хэллоуин-вечеринке!\""
        ch_b "О! Позволь мне угадать твой образ. . ."
        $ BetsyX.FaceChange("smile",Eyes="down")
        "Она оценивающе оглядывает вас с ног до головы."
        $ BetsyX.FaceChange("smile")
        if not Player.Male:
            $ HWLine = ["Что ж, похоже, ты вообще не старалась, да?","А, ты, наверное, лихая пиратка!","Узнаю этот стиль — ты ниндзя из клана Руки.","О! Ты пожарная, не так ли?"]
        else:
            $ HWLine = ["Что ж, похоже, ты вообще не старался, да?","А, ты, наверное, лихой корсар!","Узнаю этот стиль — ты ниндзя из клана Руки.","О! Ты пожарный, не так ли?"]
        $ HWLine = HWLine[Costume]
        ch_b "[HWLine]"
        menu:
            extend ""
            "Ага, ты угадала.":
                    call HWStatup(BetsyX,"Love", 90, 1)
                    if not Costume:
                            ch_b "Что ж, не все разделяют праздничный настрой."
                    else:
                            ch_b "Это очень увлекательно."
            "Ага, пожалуй." if not Costume:
                    $ BetsyX.FaceChange("smile")
                    ch_b "Что ж."
                    ch_b "Видимо, дух Хэллоуина тебе не близок."
            "Нет, сейчас это мой повседневный образ." if Costume:
                    $ BetsyX.FaceChange("smile",Eyes="side")
                    call HWStatup(BetsyX,"Obed", 40, 1)
                    ch_b "Разумеется."
                    $ BetsyX.FaceChange("smile")
                    ch_b "Должна признать, ты очень выделяешься из толпы. . ."
            "Пропустить вступление." if "halloween" in Player.History:
                    menu:
                        "Вы уверены, что хотите пропустить вступления и сразу перейти к вечеринке?"
                        "Да":
                            jump Halloween_Skip
                        "Нет":
                            if not Player.Male:
                                ch_p "Извини, я задумалась."
                            else:
                                ch_p "Извини, я задумался."
        ch_b "Сможешь угадать мой костюм?"
        menu:
            extend ""
            "Инструктор по физ. подготовке?":
                    $ BetsyX.FaceChange("smirk")
                    call HWStatup(BetsyX,"Obed", 50, 1)
                    ch_b "Мне кажется, я приложила больше усилий!"
                    $ BetsyX.FaceChange("smile")
                    ch_b "Я нарядилась британкой Кэмми из одной популярной серии видеоигр!"
                    ch_b "Хотя это куртка у меня уже была. . ."
            "Кэмми?":
                    $ BetsyX.FaceChange("surprised",Mouth="smile")
                    call HWStatup(BetsyX,"Love", 80, 1)
                    call HWStatup(BetsyX,"Love", 90, 1)
                    if not Player.Male:
                        ch_b "О, угадала!"
                    else:
                        ch_b "О, угадал!"
                    $ BetsyX.FaceChange("smile")
                    ch_b "Ее новый дизайн мне показался очаровательным, да и подходящая куртка у меня уже была."
            "Билли Айдол?":
                    $ BetsyX.FaceChange("surprised")
                    ch_b "Я. . ."
                    $ BetsyX.FaceChange("bemused")
                    call HWStatup(BetsyX,"Obed", 50, 1)
                    call HWStatup(BetsyX,"Inbt", 50, 1)
                    ch_b "Нет, но твоя догадка весьма. . . оригинальна."
                    $ BetsyX.FaceChange("smile")
                    ch_b "Я в образе \"Кэмми,\" из одного популярного файтинга."
        menu:
            extend ""
            "Ты выглядишь потрясающе!":
                    call HWStatup(BetsyX,"Love", 80, 1)
                    call HWStatup(BetsyX,"Love", 90, 1)
                    ch_b "О, как мило с твоей стороны."
                    ch_b "Мне самой нравится этот образ."
            "Мне нравится твоя новая прическа.":
                    call HWStatup(BetsyX,"Love", 80, 1)
                    call HWStatup(BetsyX,"Love", 90, 1)
                    call HWStatup(BetsyX,"Inbt", 70, 1)
                    ch_b "Мне тоже она очень нравится. . ."
                    ch_b "Возможно, я оставлю ее."
            "Выглядишь очень сексуально.":
                    $ BetsyX.FaceChange("sexy")
                    call HWStatup(BetsyX,"Love", 80, 1)
                    call HWStatup(BetsyX,"Obed", 50, 1)
                    call HWStatup(BetsyX,"Inbt", 50, 1)
                    ch_b "Ты правда так думаешь?"
                    $ BetsyX.FaceChange("sexy")
                    call HWStatup(BetsyX,"Inbt", 70, 1)
                    call HWStatup(BetsyX,"Lust", 60, 1)
                    ch_b "Тогда, пожалуй, я сохраню этот наряд. . ."
        $ BetsyX.FaceChange("smile")
        ch_b "Было приятно пообщаться, но мне нужно идти."
        ch_b "Не терпится поучавствовать в \"сладость или гадость!\""
        show Betsy_Sprite:
                ease 0.8 pos (1200,50)
        pause 0.8
        "[BetsyX.Name] уходит в сторону общежития, а вы продолжаете искать того, с кем можно пообщаться."

        call AllHide(1) #removes all girls
        $ Present.remove(BetsyX)
        $ Nearby.append(BetsyX)
        $ BetsyX.Loc = "nearby"

        #End Betsy Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Modification mode
label Halloween_Doreen:
# -----------------
        #Start Doreen Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        if "met" not in DoreenX.History:
                jump Halloween_Party
        "Вы замечаете кого-то ползающего возле кустов."
        "Подозрительно. . ."
        "Наверное, вам стоит проверить. . ."
        #display Doreen
        $ Present.append(DoreenX)
        $ DoreenX.FaceChange("smile")
        $ DoreenX.Loc = "HW Party"
        $ DoreenX.AddWord(1,0,DoreenX.Hair,0,"halloween") #adds "halloween" to History
        $ DoreenX.OutfitDay = "costume"
        $ DoreenX.Outfit = DoreenX.OutfitDay
        $ DoreenX.OutfitChange(Changed=1)
        $ DoreenX.Hat = 0
        call Shift_Focus(DoreenX)
        $ Player.Sprite = 0
        show Doreen_69_Animation zorder 150:
            zoom .5
            ypos 50
        ". . ."
        # Modification mode
        if "met" in DoreenX.History:
            call Halloween_Doreen_Fix
        # -----------------
        hide Doreen_69_Animation with easeoutbottom
        pause 0.8
        show Doreen_Sprite at SpriteLoc(StageCenter,50) with easeinbottom
        pause 0.8

        ch_d "О, привет, [Player.Name]!"
        $ DoreenX.Hat = "glasses"
        $ DoreenX.FaceChange("smile",Eyes="side")
        ch_d "Я, эм. . . обронила очки. . ."
        menu:
            extend ""
            "Ты носишь очки?":
                $ DoreenX.FaceChange("smile")
                ch_d "Ну, обычно - нет."
            "А, понятно.":
                $ DoreenX.FaceChange("smile")
                ch_d "Обычно мне очки не нужны, конечно."
            ". . .":
                pass
        ch_d "Они просто часть костюма."
        ch_d "Для вечеринки. . ."
        menu:
            extend ""
            "Тебе они идут.":
                $ DoreenX.FaceChange("smile",2)
                ch_d "О. . . спасибо."
                $ DoreenX.FaceChange("smile",1)
            "Выглядишь как настоящий ботан.":
                $ DoreenX.FaceChange("smile",1,Mouth="open")
                ch_d "Ну я и так ботан!"
                $ DoreenX.AddWord(1,"dork") #Recent
            ". . .":
                pass
        $ DoreenX.FaceChange("smile",Eyes="down")
        "Она оценивающе смотрит на вас."
        $ DoreenX.FaceChange("smile")
        ch_d "Дай-ка угадаю, ты. . ."
        if not Player.Male:
            $ HWLine = ["Просто крутая девчонка, которой не нужен костюм?","-Аррр, пиратка!","Скрытный ниндзя!","Пожарная, да?"]
        else:
            $ HWLine = ["Просто крутой парень, которому не нужен костюм?","-Аррр, пират!","Скрытный ниндзя!","Пожарный, да?"]
        $ HWLine = HWLine[Costume]
        ch_d "[HWLine]"
        menu:
            extend ""
            "Ага, угадала.":
                    call HWStatup(DoreenX,"Love", 90, 1)
                    ch_d "Здорово!"
            "Ага, я просто без костюма." if not Costume:
                    $ DoreenX.FaceChange("smile")
                    ch_d "Ну, а я не могла упустить шанс нарядиться."
            "Нет, это мой новый повседневный образ." if Costume:
                    $ DoreenX.FaceChange("smile",Eyes="side")
                    call HWStatup(DoreenX,"Obed", 40, 1)
                    ch_d "Хм."
                    $ DoreenX.FaceChange("smile")
                    ch_d "Ну ладно."
            "Пропустить вступление." if "halloween" in Player.History:
                    menu:
                        "Вы уверены, что хотите пропустить вступления и сразу перейти к вечеринке?"
                        "Да":
                            jump Halloween_Skip
                        "Нет":
                            if not Player.Male:
                                ch_p "Извини, я задумалась."
                            else:
                                ch_p "Извини, я задумался."
        ch_d "Как думаешь, кто я?"
        menu:
            extend ""
            "Ты [DoreenX.Name].":
                    ch_d "Я про костюм!"
                    ch_d "Я в образе \"Велмы\"!"
            "Я же сказал — ботан." if "dork" in DoreenX.RecentActions and Player.Male:
                    call HWStatup(DoreenX,"Obed", 50, 1)
                    ch_d "А я сказала, что так и есть."
                    ch_d "Но это не относится к костюму, я сейчас в образе \"Велмы\"."
            "Я же сказала — ботан." if "dork" in DoreenX.RecentActions and not Player.Male:
                    call HWStatup(DoreenX,"Obed", 50, 1)
                    ch_d "А я сказала, что так и есть."
                    ch_d "Но это не относится к костюму, я сейчас в образе \"Велмы\"."
            "Велма?":
                    $ DoreenX.FaceChange("surprised",Mouth="smile")
                    call HWStatup(DoreenX,"Love", 80, 1)
                    call HWStatup(DoreenX,"Love", 90, 1)
                    $ DoreenX.FaceChange("smile")
                    ch_d "Ага!"
            "[[пожать плечами]":
                    call HWStatup(DoreenX,"Obed", 50, 1)
                    ch_d "Я в образе \"Велмы\"!"



        ch_d "Расследую тайну этой вечеринки!"
        ch_d "Куда подевались мини Сникерсы?!"
        show Doreen_Sprite:
                ease 0.8 pos (1200,50)
        pause 0.8
        "[DoreenX.Name] отходит от вас и растворяется в толпе."

        call AllHide(1) #removes all girls
        $ Present.remove(DoreenX)
        $ Nearby.append(DoreenX)
        $ DoreenX.Loc = "nearby"

        #End Doreen Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Modification mode
label Halloween_Wanda:
# -----------------
        #Start Wanda Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        if "met" not in WandaX.History:
                jump Halloween_Party
        ch_u "Hey!"

        "Кто-то, спотыкаясь, отделяется от толпы, похоже, ее толкнула пробегающая мимо [DoreenX.Name]."
        #display Wanda
        $ Present.append(WandaX)
        $ WandaX.FaceChange("angry",Eyes="leftside")
        $ WandaX.Loc = "HW Party"
#        $ WandaX.AddWord(1,0,WandaX.Hair,0,"halloween") #adds "halloween" to History
#        $ WandaX.OutfitDay = "costume"
#        $ WandaX.Outfit = WandaX.OutfitDay
#        $ WandaX.OutfitChange(Changed=1)
        call Shift_Focus(WandaX)
        $ Player.Sprite = 0
        show Wanda_Sprite at SpriteLoc(StageCenter,50)
        ch_w "Кто-нибудь ее запомнил?"
        $ WandaX.FaceChange("sly")
        ch_w "О, привет, [Player.Name]!"
        ch_w "Тут какая-то вечеринка, да?"
        menu:
            extend ""
            "Ты не в костюме?":
                    $ WandaX.FaceChange("confused")
                    call HWStatup(WandaX,"Obed", 80, 1)
                    ch_w "Нет. . . тут проходит брифинг к какой-то миссии или что?"
            "Милый костюмчик.":
                    call HWStatup(WandaX,"Love", 80, 2)
                    call HWStatup(WandaX,"Obed", 50, 1)
                    $ WandaX.FaceChange("confused")
                    ch_w "Кос. . . -тюм?"
            "Какой образ ты выбрала?":
                    call HWStatup(WandaX,"Obed", 70, 1)
                    $ WandaX.FaceChange("confused")
                    ch_w "Ты про что? Я оделась как обычно. . ."
            ". . .":
                    call HWStatup(WandaX,"Obed", 70, 1)
                    call HWStatup(WandaX,"Inbt", 70, 1)
                    $ WandaX.FaceChange("confused")
        "Она оглядывается по сторонам, и на ее лице появляется растерянное выражение."
        $ WandaX.Blush = 2
        menu:
            extend ""
            "Ты на костюмированной вечеринке в честь Хэллоуина.":
                    call HWStatup(WandaX,"Obed", 80, 1)
                    $ WandaX.FaceChange("surprised",1)
                    ch_w "Черт."
            "Ты в курсе, что сегодня Хэллоуин?":
                    call HWStatup(WandaX,"Love", 80, 1)
                    call HWStatup(WandaX,"Love", 98, 1)
                    call HWStatup(WandaX,"Obed", 50, 1)
                    call HWStatup(WandaX,"Inbt", 50, 1)
                    $ WandaX.FaceChange("angry",1,Eyes="side")
                    ch_w "Ох, конечно. Хэллоуин."
            "Ты не получила приглашение?":
                    call HWStatup(WandaX,"Obed", 60, 1)
                    call HWStatup(WandaX,"Obed", 80, 1)
                    $ WandaX.FaceChange("surprised",1)
                    ch_w "Я не знаю! Кто вообще проверяет почту?!"
                    $ WandaX.FaceChange("normal",1,Eyes="side")
                    ch_w "Тут типа проходит вечеринка в честь Хэллоуина, да?"
            ". . .":
                    call HWStatup(WandaX,"Obed", 70, 1)
                    call HWStatup(WandaX,"Inbt", 70, 1)
                    $ WandaX.FaceChange("angry",1,Eyes="side")
                    ch_w "Черт. Я на вечеринке в честь Хэллоуина, да?"
        $ WandaX.FaceChange("smile",1,Eyes="down")
        "Она оглядывает вас с головы до ног."
        $ WandaX.FaceChange("sly")
        if not Player.Male:
            ch_w "Думаю, это объясняет, почему ты одета. . ."
            $ HWLine = ["Как ты?","Как я?","-в пижаму?","-как пожарная, я полагаю?"]
        else:
            ch_w "Думаю, это объясняет, почему ты одет. . ."
            $ HWLine = ["Как ты?","Как я?","-в пижаму?","-как пожарный, я полагаю?"]
        $ HWLine = HWLine[Costume]
        ch_w "[HWLine]"
        menu:
            extend ""
            "Ага, ты угадала.":
                    call HWStatup(WandaX,"Love", 90, 1)
                    ch_w "Ну и хорошо."
            "Ага, я в повседневной одежде." if not Costume:
                    $ WandaX.FaceChange("smile")
                    call HWStatup(WandaX,"Love", 80, 1)
                    call HWStatup(WandaX,"Love", 99, 2)
                    ch_w "Ну вот видишь? Не одна я пришла без костюма."
            "Нет, это мой новый повседневный образ." if Costume:
                    call HWStatup(WandaX,"Love", 90, 1)
                    call HWStatup(WandaX,"Obed", 80, 1)
                    $ WandaX.FaceChange("smile")
                    ch_w "Конечно."
            "Пропустить вступление." if "halloween" in Player.History:
                    menu:
                        "Вы уверены, что хотите пропустить вступления и сразу перейти к вечеринке?"
                        "Да":
                            jump Halloween_Skip
                        "Нет":
                            if not Player.Male:
                                ch_p "Извини, я задумалась."
                            else:
                                ch_p "Извини, я задумался."
        ch_w "И все же, раз я на костюмированной вечеринке, думаю, я не должна выделяться."
        "Она щелкает пальцами, и ее окутывает голубое свечение."
        #puts costume on:
        $ WandaX.AddWord(1,0,WandaX.Hair,0,"halloween") #adds "halloween" to History
        $ WandaX.OutfitDay = "costume"
        $ WandaX.Outfit = WandaX.OutfitDay
        $ WandaX.OutfitChange(Changed=1)
        "Когда свечение пропадает, на ней оказывается новый наряд."
        $ WandaX.FaceChange("sly")
        ch_w "Так-то лучше."
        ch_w "Как думаешь, кто я?"
        menu:
            extend ""
            "Ты [WandaX.Name].":
                    call HWStatup(WandaX,"Love", 80, 2)
                    $ WandaX.FaceChange("confused",Eyes="down")
                    ch_w "Я про костюм!"
                    ch_w "Фиолетовая юбка, шарф. . ."
                    $ WandaX.FaceChange("confused",Eyes="stunned")
                    "Она дотрагивается до своей головы."
                    ch_w"Длинные волосы, лента для волос. . ."
                    $ WandaX.FaceChange("confused")
                    ch_w "Я похожа на Дафну из того мультфильма?"
            "Дафна?":
                    $ WandaX.FaceChange("surprised",Mouth="smile")
                    call HWStatup(WandaX,"Love", 80, 2)
                    call HWStatup(WandaX,"Love", 99, 1)
                    call HWStatup(WandaX,"Inbt", 70, 1)
                    $ WandaX.FaceChange("smile")
                    ch_w "Из мультфильма?"
            "[[пожать плучами]":
                    call HWStatup(WandaX,"Obed", 60, 1)
                    call HWStatup(WandaX,"Inbt", 80, 1)
                    $ WandaX.FaceChange("confused",Eyes="down")
                    ch_w "Фиолетовая юбка, шарф. . ."
                    $ WandaX.FaceChange("confused",Eyes="stunned")
                    "Она дотрагивается до своей головы."
                    ch_w"Длинные волосы, лента для волос. . ."
                    $ WandaX.FaceChange("confused")
                    ch_w "Я похожа на Дафну из того мультфильма?"
        $ WandaX.FaceChange("surprised")
        ch_w "О, должно быть, на мои мысли повлияла та девушка в свитере, с которой я столкнулся ранее!"
        $ WandaX.FaceChange("sly")
        ch_w "Забавно, думаю, мне очень идет. . ."
        if not Costume:
                ch_w "И тебе тоже!"
                call HWStatup(WandaX,"Inbt", 80, 1)
                "Она снова щелкает пальцами, и вы оказываетесь в костюме пирата."
                $ Costume = 1
        ch_w "Теперь мне нужно найти Велму. . ."
        show Wanda_Sprite:
                ease 0.8 pos (1200,50)
        pause 0.8
        "[WandaX.Name] убегает в толпу."
        if DoreenX.Tail:
                ch_w "У нее был хвост? . . ."
        else:
                ch_w "Она была довольно толстой. . ."
        call AllHide(1) #removes all girls
        $ Present.remove(WandaX)
        $ Nearby.append(WandaX)
        $ WandaX.Loc = "nearby"

        #End Wanda Portion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        #End all intros / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        jump Halloween_Party

        return

label Halloween_Skip:
        call AllHide(1) #removes all girls
        $ Options = ActiveGirls[:]  #loads up all local girls
        if LauraX in Options and "angry" in LauraX.RecentActions:
                #if you pissed her off, leave her out of it.
                $ Options.remove(LauraX)
#        if WandaX in Options:
#                #remove new girl until she's an option
#                $ Options.remove(WandaX)
        while Options:
                while Options[0] in Present:
                        $ Present.remove(Options[0])
                if Options[0] not in Nearby:
                        $ Nearby.append(Options[0])
                $ Options[0].Loc = "HW Party"
                # Modification mode
                if Options[0].OutfitDay != "costume2":
                    $ Options[0].OutfitDay = "costume"
                # -----------------
                $ Options[0].Outfit = "costume"
                $ Options[0].OutfitChange(Changed=1)
                $ Options[0].AddWord(1,0,0,0,"halloween") #adds "halloween" to History

                $ Options.remove(Options[0])


label Halloween_Party: #rkeljsvgbdw
        #the looping portion of the party
        call Halloween_Events #spits out a randomized description of the party.
        if Round <= 10:
            call Halloween_Ending
        "Вы находитесь на вечеринке в честь Хэллоуина."
        menu:
            "С кем бы вы хотели поговорить?"
            "С [RogueX.Name_tvo]." if RogueX.Loc == "HW Party" or RogueX.Loc == "nearby":
                        call Halloween_Chat(RogueX)
            "С [KittyX.Name_tvo]." if KittyX.Loc == "HW Party" or KittyX.Loc == "nearby":
                        call Halloween_Chat(KittyX)
            "С [EmmaX.Name_tvo]." if EmmaX.Loc == "HW Party" or EmmaX.Loc == "nearby":
                        call Halloween_Chat(EmmaX)
            "С [LauraX.Name_tvo]." if LauraX.Loc == "HW Party" or LauraX.Loc == "nearby":
                        call Halloween_Chat(LauraX)
            "С [JeanX.Name_tvo]." if JeanX.Loc == "HW Party" or JeanX.Loc == "nearby":
                        call Halloween_Chat(JeanX)
            "С [StormX.Name_tvo]." if StormX.Loc == "HW Party" or StormX.Loc == "nearby":
                        call Halloween_Chat(StormX)
            "С [JubesX.Name_tvo]." if JubesX.Loc == "HW Party" or JubesX.Loc == "nearby":
                        call Halloween_Chat(JubesX)
            "С [GwenX.Name_tvo]." if GwenX.Loc == "HW Party" or GwenX.Loc == "nearby":
                        call Halloween_Chat(GwenX)
            "С [BetsyX.Name_tvo]." if BetsyX.Loc == "HW Party" or BetsyX.Loc == "nearby":
                        call Halloween_Chat(BetsyX)
            "С [DoreenX.Name_tvo]." if DoreenX.Loc == "HW Party" or DoreenX.Loc == "nearby":
                        call Halloween_Chat(DoreenX)
            "С [WandaX.Name_tvo]." if WandaX.Loc == "HW Party" or WandaX.Loc == "nearby":
                        call Halloween_Chat(WandaX)
            "Покинуть вечеринку":
                        call Halloween_Ending
        jump Halloween_Party


label Halloween_Events:
        if not HWEvents:
                #first time through for the night
                $ Round -= 15
                $ HWEvents = ["Скотт одет как Рю. Он пытается сделать Хадоукен, но своими глазами.",
                            "Курт одет как Саске. Он постоянно телепортируется и разбрасывает повсюду бревна.",
                            "Бобби одет как Саб Зиро. Он часто выкрикивает \"иди сюда!\" [[Ориг. get over here!], чем сбивает всех с толку.",
                            "Профессор Маккой качается на одном из деревьев. Он выкрасил свой мех в зеленый цвет, с оранжевой гривой.",
                            "Хисако нагромаздила картонные коробки поверх своей брони, так что она похожа на меха[[Бронетехника].",

                            "Лин, похоже, вырядилась в Чоппер, с рогами в качестве руля.",
                            "Тревор прилепил к своему телу кучу щупалец с глазными стеблями и выкрасил себя в фиолетовый цвет.",
                            "Иаре удалось победить в конкурсе по срыванию яблок, но потом она может остаться там навсегда.",
                            "Герман каким-то образом выкрасился в бирюзовый цвет и надел штаны, похожие на гигантского волка.",
                            "Дуг одет как блестящий золотой дроид. Держу пари, он свободно владеет более чем 6 миллионами языков.",

                            "Эрнст одет в черный костюм ведьмы с гигантской шляпой. У Марты маленькие кошачьи ушки.",
                            "Сессили добавила несколько различных металлических деталей к своему образу, чтобы выглядеть как что-то с обложки Heavy Metal группы.",
                            "Ииииии, видимо, Табби кинула бомбу в корыто с яблоками. Яблочное месиво повсюду.",
                            "Пьетро ест - нет, он танцует - нет, подождите, он играет в видео- нет... А, неважно. Он просто на вечеринке.",
                            "Уоррен одет как Мерси. У него довольно приличный костюм для правила 63.",

                            ]
                $ renpy.random.shuffle(HWEvents)
                $ Player.AddWord(1,"halloween","halloween",0,"halloween") #adds "halloween" to History
                "Все представления закончены, теперь можно осмотреть вечеринку."
        "[HWEvents[0]]"
        $ Round -= 5
        $ HWEvents.remove(HWEvents[0])
        return

label Halloween_Ending(Girl=0): #rkeljsvgbdw
        "Вечер подходит к концу, хотели бы вы встретиться с кем-то конкретным?"
        menu:
            "Поговорить с. . ."
            "[RogueX.Name_tvo]." if RogueX.Loc == "HW Party" or RogueX.Loc == "nearby":
                            $ Girl = RogueX
            "[KittyX.Name_tvo]." if KittyX.Loc == "HW Party" or KittyX.Loc == "nearby":
                            $ Girl = KittyX
            "[EmmaX.Name_tvo]." if EmmaX.Loc == "HW Party" or EmmaX.Loc == "nearby":
                    if "classcaught" in EmmaX.History:
                            $ Girl = EmmaX
                    else:
                            ch_e "Сегодня я прекрасно провела время, но мне пора."
                            ch_e "Надеюсь, завтра увидимся. . ."
                            $ EmmaX.Loc = "bg emma"
                            call Halloween_Ending
            "[LauraX.Name_tvo]." if LauraX.Loc == "HW Party" or LauraX.Loc == "nearby":
                            $ Girl = LauraX
            "[JeanX.Name_tvo]." if JeanX.Loc == "HW Party" or JeanX.Loc == "nearby":
                            $ Girl = JeanX
            "[StormX.Name_tvo]." if StormX.Loc == "HW Party" or StormX.Loc == "nearby":
                            $ Girl = StormX
            "[JubesX.Name_tvo]." if JubesX.Loc == "HW Party" or JubesX.Loc == "nearby":
                            $ Girl = JubesX
            "[GwenX.Name_tvo]." if GwenX.Loc == "HW Party" or GwenX.Loc == "nearby":
                            $ Girl = GwenX
            "[BetsyX.Name_tvo]." if BetsyX.Loc == "HW Party" or BetsyX.Loc == "nearby":
                            $ Girl = BetsyX
            "[DoreenX.Name_tvo]." if DoreenX.Loc == "HW Party" or DoreenX.Loc == "nearby":
                            $ Girl = DoreenX
            "[WandaX.Name_tvo]." if WandaX.Loc == "HW Party" or WandaX.Loc == "nearby":
                            $ Girl = WandaX
            "Ни с кем не разговаривать.":
                            $ Girl = 0

        $ bg_current = "bg player"
        call Wait
        call Girls_Location
        if Girl:
            $ Girl.Loc = "bg player"
            #put girl in costume
            call Set_The_Scene(Quiet=1)
            $ Girl.FaceChange("smile",1)
            if Girl is RogueX:
                    ch_r "Ну, это была ужасно веселая вечеринка."
                    ch_r "Ну? Что у тебя на уме. . .?"
            elif Girl is KittyX:
                    ch_k "Вечеринка мне[Girl.like]очень понравилась!"
                    if not Player.Male:
                        ch_k "Итак, зачем ты привела меня сюда. . .?"
                    else:
                        ch_k "Итак, зачем ты привел меня сюда. . .?"
            elif Girl is EmmaX:
                    ch_e "Сегодня я прекрасно провела время, надеюсь, на уме у тебя есть нечто. . . большее."
            elif Girl is LauraX:
                    ch_l "Тебе что? Так понравился костюм?"
            elif Girl is JeanX:
                    if not Player.Male:
                        ch_j "Привет, ну, о чем ты хотела поговорить?"
                    else:
                        ch_j "Привет, ну, о чем ты хотел поговорить?"
            elif Girl is StormX:
                    ch_s "Фух. . . Мне очень понравилась эта вечеринка. . ."
                    if not Player.Male:
                        ch_s "Что ты хотела обсудить?"
                    else:
                        ch_s "Что ты хотел обсудить?"
            elif Girl is JubesX:
                    ch_v "Отличная вечеринка, не хочешь пообщаться после нее?"
            elif Girl is GwenX:
                    ch_g "Это было потрясающе, мне понравились костюмы всех присутствующих!"
                    ch_g "Ну что, продолжим теперь наедине?"
            elif Girl is BetsyX:
                    ch_b "Что ж, это было чудесное мероприятие!"
                    ch_b "Ты хочешь что-то обсудить?"
            elif Girl is WandaX:
                    ch_w "Это была дикая вечеринка."
                    ch_w "Ну что, у тебя есть какие-то планы на остаток вечера?"
        $ bg_current = "bg player"
        jump Misplaced
        return
