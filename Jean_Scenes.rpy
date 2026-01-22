
# Start JeanMeet / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label JeanMeet:
        call Shift_Focus(JeanX)

        $ JeanX.Name = "???"
        $ JeanX.AddWord(1,"showered","showered",0,0)
        call Remove_Girl("All")
        call JeanName(1)


        $ JeanX.Loc = "bg showerroom"
        $ bg_current = "bg showerroom"
        $ ActiveGirls.append(JeanX) if JeanX not in ActiveGirls else ActiveGirls
        $ Line = 0

        $ JeanX.OutfitChange("casual1")
        $ JeanX.Outfit = "casual1"
        $ JeanX.FaceChange("sly",0)
        call Set_The_Scene(0,1,0)
        "Когда вы подходите к душевой, вы замечаете, что там кто-то одевается."
        call Set_The_Scene(1,0,0)
        $ Player.AddWord(1,0,"Intro",0,0) #adds tag to Daily

        ch_j "Хм. . . Что-то я не помню, чтобы видела тебя раньше."
        ch_j "Ты [JeanX.Petname], так?"
        ch_g "Готова поспорить, кто-то по имени [JeanX.Petname] сейчас в шоке. . ."
        "(Не обращайте внимание на эту розовую особу.)"
        menu:
            ch_j "Ты [JeanX.Petname], так?"
            "Нет, вообще-то, я [Player.Name].":
                    call JeanName #sets new Petname
                    $ JeanX.Statup("Love", 90, -2)
                    $ JeanX.Statup("Obed", 200, 2)
                    ch_j "Хорошо, [JeanX.Petname], я поняла."
            "Ага, я [JeanX.Petname].":
                    $ JeanX.FaceChange("sly",Mouth="smile")
                    $ JeanX.Statup("Love", 90, 5)
                    $ JeanX.IX -= 5
                    ch_j "Ты просто выглядишь как \"[JeanX.Petname].\""
            "Я [Player.Name], запомни.":
                    call JeanName #sets new Petname
                    $ JeanX.FaceChange("confused")
                    $ JeanX.Statup("Love", 90, -5)
                    $ JeanX.Statup("Obed", 200, 5)
                    ch_j "Хорошо, [JeanX.Petname], я тебя услышала!"

        $ JeanX.FaceChange("sly")
        menu:
            extend ""
            "Нет, серьезно, я [Player.Name]." if Player.Name != JeanX.Petname:
                    $ JeanX.FaceChange("angry",1)
                    $ JeanX.Statup("Love", 90, -5)
                    $ JeanX.Statup("Obed", 200, 5)
                    $ JeanX.IX -= 5
                    ch_j "Я ЗНАЮ!!!"
                    $ JeanX.FaceChange("bemused",0,Eyes="side")
                    ch_j "Серьезно, [JeanX.Petname], тебе нужно немного -расслабиться.-"
            "Нет, я. . . а, точно, я [Player.Name]." if Player.Name == JeanX.Petname:
                    $ JeanX.Statup("Love", 90, 5)
                    $ JeanX.Statup("Obed", 200, 2)
                    $ JeanX.IX -= 5
                    ch_j "Видишь? Мозг как стальной капкан."
            "Ага.":
                    $ JeanX.Statup("Love", 90, 5)
                    $ JeanX.Statup("Obed", 200, 5)
                    $ JeanX.IX -= 5
            "Слушай, ты, дура. . ." if Player.Name != JeanX.Petname:
                    $ JeanX.FaceChange("confused")
                    $ JeanX.Statup("Love", 90, -10)
                    $ JeanX.Statup("Obed", 200, 2)
                    ch_j "Я тебя перебью, [JeanX.Petname]."
                    $ JeanX.FaceChange("angry",Eyes="psychic")
                    ch_j "Если я сказала, что тебя зовут [JeanX.Petname], значит ты [JeanX.Petname]."
                    $ JeanX.FaceChange("sly")
                    ch_j "Так ведь. . . [JeanX.Petname]?"

                    menu:
                        extend ""
                        "А, да. Я [JeanX.Petname].":
                                $ JeanX.FaceChange("confused",1,Eyes="side")
                                $ JeanX.Statup("Love", 90, 5)
                                $ JeanX.Statup("Obed", 200, 5)
                                ch_j "Хорошо. . ."
                        "Как скажешь.":
                                $ JeanX.FaceChange("confused",1,Eyes="side")
                                $ JeanX.Statup("Obed", 200, 10)
                                ch_j ". . ."
                                ch_j "Правильно. . ."
                        "Нет, я [Player.Name], услышь уже меня!":
                                $ JeanX.FaceChange("confused",1,Eyes="side")
                                $ JeanX.Statup("Love", 90, -10)
                                $ JeanX.Statup("Obed", 200, 10)
                                $ JeanX.Statup("Inbt", 200, -10)
                                ch_j "А?"
                                ch_j "Но я. . ."
                                $ JeanX.FaceChange("angry",1,Eyes="psychic")
                                ch_j "Крякай как утка!"
                                menu:
                                    extend ""
                                    "Кря [[подыграть]":
                                            $ JeanX.FaceChange("smile",0)
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Obed", 200, -5)
                                            $ JeanX.Statup("Inbt", 200, 10)
                                            ch_j "Ах, хорошо."
                                    "Кря [[с сарказмом]":
                                            $ JeanX.FaceChange("angry",0,Eyes="squint")
                                            $ JeanX.Statup("Love", 90, -3)
                                            $ JeanX.Statup("Obed", 200, 10)
                                            $ JeanX.Statup("Inbt", 200, -5)
                                            ch_j ". . ."
                                            $ JeanX.FaceChange("sly")
                                            ch_j "Неплохо. . ."
                                    "Нет.":
                                            $ JeanX.FaceChange("confused",1,Eyes="side")
                                            $ JeanX.Statup("Love", 90, -10)
                                            $ JeanX.Statup("Obed", 200, 15)
                                            $ JeanX.Statup("Inbt", 200, -5)
                                            ch_j "Ничего не понимаю. . ."
                                            $ JeanX.FaceChange("angry",1,Eyes="psychic")
                                            if not Player.Male:
                                                ch_j "Может, ты просто слишком тупая, что на тебя не действует? . . "
                                            else:
                                                ch_j "Может, ты просто слишком тупой, что на тебя не действует? . . "
                                            $ JeanX.FaceChange("confused",1,Eyes="psychic")
                                            ch_j "Нет, на Логане же сработало. . ."
                                            $ Line = "argued"
                    #end "you argue with her about the name thing"

        if not Line:#Line != "argued":
                #if you went along with her nickname
                $ JeanX.FaceChange("sly")
                ch_j "Кстати, я знаю, зачем ты здесь. . ."
                if Player.Male == 1:
                        ch_j "Уверена, ты надеялся застать меня голой, так?"
                        ch_j "Хотел увидеть эти сисечки?"
                else:
                        ch_j "Уверена, ты надеялась застать меня голой, так?"
                        ch_j "Услышала, какие красивые у меня сисечки, и захотела сама посмотреть?"
                $ JeanX.ArmPose = 2
                $ JeanX.Uptop = 1 #Uptop up
                pause 1
                $ JeanX.Uptop = 0 #Uptop up
                $ JeanX.FaceChange("sly",0,Eyes="side")
                $ JeanX.ArmPose = 1
                ch_j "Я тебя не виню, так поступают все извращенцы."
                menu:
                    extend ""
                    ". . . Спасибо?":
                            $ JeanX.FaceChange("bemused")
                            $ JeanX.Statup("Love", 90, 10)
                            $ JeanX.Statup("Obed", 200, 5)
                            $ JeanX.IX -= 10
                            ch_j "Не за что, я не против побыть великодушной. . ."
                    "Вау, это было здорово!":
                            $ JeanX.FaceChange("smile")
                            $ JeanX.Statup("Love", 90, 15)
                            $ JeanX.Statup("Obed", 200, 5)
                            $ JeanX.IX -= 15
                            ch_j "Я знаю, приятно иногда выставлять их напоказ. . ."
                    "Не слишком ли просто?":
                            $ JeanX.FaceChange("smile",Brows="confused")
                            $ JeanX.Statup("Love", 90, -3)
                            $ JeanX.Statup("Obed", 200, 10)
                            $ JeanX.Statup("Inbt", 200, -5)
                            ch_j "Ну, мне стесняться нечего, я знаю, насколько они великолепны. . ."
                call Girl_First_Topless(JeanX,0,1)
                $ JeanX.FaceChange("bemused")
                ch_j ". . . через пять минут ты забудешь об увиденном."
                $ JeanX.FaceChange("bemused",Eyes="psychic")
                ch_j "Итак, что сейчас произошло?"
                $ JeanX.FaceChange("bemused")
                menu:
                    extend ""
                    "Ничего необычного.":
                            $ JeanX.Statup("Love", 90, 5)
                            ch_j "Именно, [JeanX.Petname]."
                    "Я. . . не знаю?":
                            $ JeanX.Statup("Love", 90, 5)
                            $ JeanX.Statup("Obed", 200, 10)
                            $ JeanX.Statup("Inbt", 200, -5)
                            ch_j "Верно."
                            $ JeanX.FaceChange("perplexed",0)
                            ch_j ". . ."
                    "Ты только что показала мне сиськи.":
                            $ JeanX.Statup("Love", 90, 5)
                            ch_j "Имен-{w=0.3}{nw}"
                            $ JeanX.FaceChange("surprised",2)
                            $ JeanX.Statup("Love", 90, -10)
                            $ JeanX.Statup("Obed", 200, 10)
                            $ JeanX.Statup("Inbt", 200, -5)
                            $ JeanX.ArmPose = 2
                            ch_j "Имен- подожди, что?"
                            $ JeanX.FaceChange("surprised",1)
                            menu:
                                extend ""
                                "То есть, ничего необычного?":
                                        $ JeanX.FaceChange("confused",1)
                                        $ JeanX.Statup("Love", 90, 5)
                                        $ JeanX.Statup("Obed", 200, 5)
                                        ch_j ". . ."
                                        $ JeanX.FaceChange("confused",1,Eyes="side")
                                        ch_j "Верно. . ."
                                "Ты только что показала мне сиськи.":
                                        $ JeanX.FaceChange("confused",2)
                                        $ JeanX.Statup("Love", 90,-5)
                                        $ JeanX.Statup("Obed", 200, 10)
                                        ch_j "Почему ты помнишь. . ."
                                        $ JeanX.FaceChange("angry",1)
                                        if not Player.Male:
                                            ch_j "Ты должна была забыть об этом!"
                                        else:
                                            ch_j "Ты должен был забыть об этом!"
                                        ch_j "Я же воздействовала на твой разум!"
                                        $ Line = "power"
                                "Ты показала мне сиськи, дура!":
                                        $ JeanX.FaceChange("angry",2)
                                        $ JeanX.Statup("Love", 90, -20)
                                        $ JeanX.Statup("Obed", 200, 20)
                                        ch_j "Не разговаривай со мной так!"
                                        $ JeanX.FaceChange("confused",1)
                                        ch_j "Почему ты помнишь. . ."
                                        $ JeanX.FaceChange("angry",1)
                                        if not Player.Male:
                                            ch_j "Ты должна была забыть об этом!"
                                        else:
                                            ch_j "Ты должен был забыть об этом!"
                                        ch_j "Я же воздействовала на твой разум!"
                                        $ Line = "power"
                            $ JeanX.ArmPose = 1
        #end flashing sequence

        if not Line:
                #if you've managed to not get outed yet. . .
                ch_j "Так, похоже, зеркало все запотело. . ."
                $ JeanX.FaceChange("sly",Eyes="psychic")
                ch_j "Тогда я воспользуюсь твоими глазами. . ."
                $ JeanX.FaceChange("confused",1)
                ch_j ". . ."
                $ JeanX.FaceChange("angry",1)
                $ JeanX.Statup("Love", 90, -5)
                $ JeanX.Statup("Obed", 200, 5)
                $ JeanX.Statup("Inbt", 200, -5)
                ch_j "Что происходит? Почему я не могу проникнуть в твою голову?"
        # end "she tries to see through your eyes"

        menu:
            extend ""
            "У меня иммунитет к способностям мутантов.":
                    $ JeanX.FaceChange("confused",1)
                    $ JeanX.Statup("Love", 90, -10)
                    $ JeanX.Statup("Obed", 200, 10)
                    ch_j "А?"
                    ch_j "Так в этом дело?!"
                    $ JeanX.FaceChange("angry",1)
                    ch_j "Почему никто не сказал мне об этом?!"
            "Я уже в твоей голове.":
                    $ JeanX.FaceChange("surprised",2)
                    $ JeanX.Statup("Love", 90, -5)
                    $ JeanX.Statup("Obed", 200, 30)
                    ch_j "Что?!"
                    $ JeanX.FaceChange("confused",1)
                    ch_j "Подожди. . ."
                    $ JeanX.FaceChange("angry",1)
                    $ JeanX.Statup("Love", 90, -15)
                    $ JeanX.Statup("Obed", 200, -10)
                    ch_j "Это не так!"
                    if not Player.Male:
                        ch_j "Ты просто типа. . . невосприимчива к контролю разума или что-то вроде этого!"
                    else:
                        ch_j "Ты просто типа. . . невосприимчив к контролю разума или что-то вроде этого!"
            "Я есть плод твоего воображения.":
                    $ JeanX.FaceChange("angry",2)
                    $ JeanX.Statup("Love", 90, -5)
                    $ JeanX.Statup("Obed", 200, 15)
                    ch_j "А теперь ты издеваешься надо мной."
                    $ JeanX.FaceChange("angry",1,Mouth="surprised")
                    $ JeanX.Statup("Love", 90, -5)
                    ch_j "Охренеть!"
                    $ JeanX.FaceChange("angry",1)
                    if not Player.Male:
                        ch_j "Ты просто типа. . . невосприимчива к контролю разума или что-то вроде этого!"
                    else:
                        ch_j "Ты просто типа. . . невосприимчив к контролю разума или что-то вроде этого!"
        $ JeanX.Statup("Inbt", 200, -200)
        if JeanX.SeenChest:
                $ JeanX.FaceChange("angry",1)
                if not Player.Male:
                    ch_j "Так, ты видела мои. . ."
                else:
                    ch_j "Так, ты видел мои. . ."
                menu:
                    "Ага.":
                            $ JeanX.Statup("Obed", 200, 3)
                            $ JeanX.Statup("Inbt", 200, -5)
                    ". . .":
                            $ JeanX.Statup("Obed", 200, 7)
                    "Что?":
                            pass
                $ JeanX.FaceChange("angry",2)
                ch_j "И ты помнишь? . ."
                menu:
                    "Ага.":
                            $ JeanX.Statup("Love", 90, -3)
                            $ JeanX.Statup("Obed", 200, 10)
                    ". . .":
                            $ JeanX.Statup("Obed", 200, 10)
                    "Я не помню, конечно, как ты показывала их мне":
                            $ JeanX.FaceChange("smile",0)
                            $ JeanX.Statup("Love", 90, 10)
                            $ JeanX.Statup("Inbt", 200, 50)
                            ch_j "О, хоро- {w=0.3}{nw}"
                            $ JeanX.FaceChange("angry",2)
                            $ JeanX.Statup("Love", 90, -20)
                            $ JeanX.Statup("Obed", 200, 20)
                            $ JeanX.Statup("Inbt", 200, -40)
                            ch_j "О, хоро- ты снова меня обманываешь!"
        $ JeanX.FaceChange("angry",1,Eyes="psychic")
        ch_j "Аргх!"
        "Вы чувствуете легкий ветерок на своей щеке."
        $ JeanX.FaceChange("angry",1)
        $ JeanX.Statup("Love", 90, -10)
        $ JeanX.Statup("Obed", 200, 10)
        $ JeanX.Statup("Inbt", 200, -20)
        if not Player.Male:
            ch_j "Ты еще и невосприимчива к моему телекинезу?!"
        else:
            ch_j "Ты еще и невосприимчив к моему телекинезу?!"
        menu:
            "Пока я этого хочу, да.":
                    pass
            "Агась.":
                    $ JeanX.Statup("Love", 90, -5)
                    $ JeanX.Statup("Obed", 200, 10)
            ". . .":
                    $ JeanX.Statup("Love", 90, 3)
        $ JeanX.Statup("Obed", 200, 10)
        $ JeanX.FaceChange("angry",1,Eyes="psychic")
        "Шкафчик отрывается от стены и направляется в вашу сторону."
        "От воздействия вашей силы, он падает."
        $ JeanX.FaceChange("angry",1,Eyes="side")
        $ JeanX.Statup("Obed", 200, 10)
        $ JeanX.Statup("Inbt", 200, -10)
        ch_j ". . ."
        ch_j "Как же неудобно."
        ch_j "Я не знаю, что с тобой делать. . ."
        $ JeanX.FaceChange("angry",1)
        ch_j "Я не привыкла к тому, что кто-то может вот так просто. . ."
        $ JeanX.FaceChange("angry",2,Eyes="side")
        ch_j ". . . игнорировать меня. . ."
        if Player.Male != 1:
                ch_j "Наверное, она даже не по девочкам. . ."
        ch_j "Мне нужно подумать. . ."
        #end powers talk

        $ JeanX.History.append("met")
        $ bg_current = "bg showerroom"
        $ Round -= 10
        call Shift_Focus(RogueX)
        $ JeanX.Loc = "hold"
        call Set_The_Scene
        $ JeanX.Outfit = "casual1"
        $ JeanX.OutfitDay = "casual1"
        $ JeanX.OutfitChange("casual1")

        "Она собирает свои вещи и выходит из комнаты."
        ch_p "Кто она такая, черт возьми? . ."
        $ EmmaX.OutfitChange("casual1")
        show JeanMFGrey zorder 150:
                pos (-200,100)
                rotate 0
                parallel:
                    ease .5 pos (350,100)
                parallel:
                    pause .4
                    ease .1 rotate 10
                    ease .1 rotate 0
                block:
                    ease .1 pos (350,105)
                    ease .1 pos (350,100)
                    repeat 4
        ". . ."
        hide JeanMFGrey with easeoutleft
        $ EmmaX.FaceChange("angry",1,Eyes="leftside")
        show Emma_Sprite at SpriteLoc(-100) zorder 25
        show Emma_Sprite at SpriteLoc(500) zorder 25 with easeinleft
        call Shift_Focus(EmmaX)
        ch_e "Это была Джин, мать ее, Грей."
        $ JeanX.Name = "Джин"
        $ JeanX.Name_rod = "Джин"
        $ JeanX.Name_dat = "Джин"
        $ JeanX.Name_vin = "Джин"
        $ JeanX.Name_tvo = "Джин"
        $ JeanX.Name_pre = "Джин"
        pause .1
        ch_e "Ее иногда. . . сильно заносит."
        menu:
            "Ясно.":
                    $ EmmaX.FaceChange("sly")
                    $ EmmaX.Statup("Love", 90, 5)
                    $ EmmaX.Statup("Obed", 60, 3)
                    $ EmmaX.Statup("Inbt", 60, 2)
            "Похоже на правду.":
                    $ EmmaX.FaceChange("sly")
                    $ EmmaX.Statup("Obed", 70, 5)
            "А она сексуальная.":
                    $ EmmaX.FaceChange("angry",1)
                    $ EmmaX.Statup("Love", 90, -5)
                    $ EmmaX.Statup("Obed", 40, 3)
                    $ EmmaX.Statup("Obed", 80, 7)
                    ch_e "Ты играешь с огнем, [EmmaX.Petname]."
        ch_e "В общем, я просто проходила мимо."
        $ EmmaX.FaceChange("angry",1,Eyes="side")
        ch_e "Постарайся, чтобы она тебя не поглотила. . ."
        show Emma_Sprite at SpriteLoc(-100) with easeinleft
        pause 0.2
        call Remove_Girl(EmmaX)
        call Shift_Focus(RogueX)
        call Set_The_Scene
        return
# End JeanMeet / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image JeanMFGrey:
        "images/JeanSprite/JeanMF.png"
        #pos (500,700)


label Jean_Key:
        call Shift_Focus(JeanX)
        $ JeanX.Loc = bg_current
        call Set_The_Scene
        $ JeanX.FaceChange("bemused")
        $ Event_Queue = [0,0]
        ch_j "О, вот, держи на всякий случай, вдруг ты захочешь заглянуть."
        "Она кидает вам ключ, который вы успешно ловите."
        $ Keys.append(JeanX) if JeanX not in Keys else Keys
        $ JeanX.Event[0] = 1
        ch_p "Спасибо."
        return



# Start JeanLike / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jean_BF:
label Jean_Like:
        #if Jean's Love value hits 500
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(JeanX,"bemused","выглядит раздраженной. . .")
                return
        if JeanX.Loc != bg_current:
                $ JeanX.Loc = bg_current
                "[JeanX.Name] подходит к вам."
        $ Event_Queue = [0,0]
        call Set_The_Scene(0)
        call Display_Girl(JeanX)
        call CleartheRoom(JeanX)
        call Set_The_Scene
        call Shift_Focus(JeanX)
        $ JeanX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in JeanX.History:
                call expression JeanX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        $ Line = 0
        $ JeanX.FaceChange("sly",1,Eyes="down")
        ". . .{w=0.5}{nw}"
        $ JeanX.FaceChange("sly",1)
        "Она оценивающе оглядывает вас."

        ch_j "А знаешь. . . с тобой гораздо веселее, чем я ожидала."
        $ Line = "Т"
        if JeanX.Massage >= 5:
                $ JeanX.Statup("Lust", 60, 5)
                ch_j "Ты делаешь очень хороший массаж. . ."
                $ Line = "и т"
        if JeanX.Org >= 10:
                $ JeanX.FaceChange("sly",1)
                $ JeanX.Statup("Lust", 70, 5)
                ch_j "[Line]ы знаешь, как доставить удовольствие. . ."
                $ Line = "и т"
                if JeanX.Org >= 30:
                        $ JeanX.Statup("Lust", 80, 10)
                        ch_j ". . . серьезно. . ."
        if JeanX.SeenPeen and Player.Male:
                $ JeanX.FaceChange("sly",1)
                $ JeanX.Statup("Love", 200, 5)
                $ JeanX.Statup("Obed", 90, 10)
                $ JeanX.Statup("Inbt", 200, 5)
                $ JeanX.Statup("Lust", 85, 5)
                ch_j "[Line]вой член весьма хорош. . ."
        if JeanX.SeenPuss and not Player.Male:
                $ JeanX.FaceChange("sly",1)
                $ JeanX.Statup("Love", 200, 5)
                $ JeanX.Statup("Obed", 90, 10)
                $ JeanX.Statup("Inbt", 200, 5)
                $ JeanX.Statup("Lust", 85, 5)
                ch_j "[Line]вое тело весьма полтянутое. . ."
        $ Line = 0

        ch_j "Секс-игрушки лучше не найти."
        menu:
                    extend ""
                    "Мне тоже все нравится.":
                            $ JeanX.FaceChange("sly",1)
                            $ JeanX.Statup("Love", 200, 10)
                            $ JeanX.Statup("Obed", 90, 5)
                            $ JeanX.Statup("Inbt", 200, 5)
                            if not Player.Male:
                                ch_j "Хорошая девочка. . ."
                            else:
                                ch_j "Хороший мальчик. . ."
                            ch_j "Продолжай в том же духе, и я буду тебя почаще \"вознаграждать\."
                    "А если я захочу чего-то большего?":
                            $ JeanX.Brows = "confused"
                            $ JeanX.Statup("Obed", 90, 10)
                            ch_j "А?"
                            $ Line = "more"
                    "Я тебе не игрушка.":
                            $ JeanX.Brows = "confused"
                            $ JeanX.Statup("Obed", 90, 15)
                            ch_j "Что?"

        $ JeanX.History.append("sexfriend")
        if Line == "more":
                $ JeanX.Brows = "confused"
                ch_j "Чего еще ты хочешь?"
                menu:
                    extend ""
                    "Не хочешь стать моей девушкой?":
                            $ JeanX.FaceChange("surprised",2)
                            $ JeanX.Statup("Love", 200, 5)
                            $ JeanX.Statup("Obed", 90, -5)
                            ch_j "Ха! Девушкой значит. . ."
                            $ JeanX.FaceChange("bemused",1,Eyes="side")
                            ch_j "Как мило!"

                            $ JeanX.FaceChange("sly",1)
                            if JeanX.Org >= 10:
                                    if not Player.Male:
                                        ch_j "Послушай, ты довольно горяча и, думаю, ты этого достойна. . ."
                                    else:
                                        ch_j "Послушай, ты довольно горячий парень и, думаю, ты этого достоин. . ."
                            else:
                                    if not Player.Male:
                                        ch_j "Послушай, ты довольно горяча. . ."
                                    else:
                                        ch_j "Послушай, ты довольно горячий парень. . ."
                            ch_j "но я не считаю тебя предметом для \"отношений\". . ."

                    "Мы могли бы стать секс-партнерами?":
                            $ JeanX.FaceChange("bemused",1,Eyes="side")
                            $ JeanX.Statup("Love", 200, 5)
                            $ JeanX.Statup("Obed", 90, 10)
                            $ JeanX.Statup("Inbt", 80, 5)
                            $ JeanX.Statup("Inbt", 200, 5)
                            $ JeanX.Statup("Lust", 85, 10)
                            ch_j "Хмм. . ."
                            ch_j "Партнерами по. . . сексу? . ."
                            $ JeanX.FaceChange("bemused",1)
                            ch_j "Думаю, это можно устроить. . ."
                            $ Line = 0
                    "Да так, ничего. . .":
                            $ JeanX.FaceChange("bemused",1)
                            $ JeanX.Statup("Love", 200, 5)
                            ch_j "Вот и славно."
                            $ Line = 0
        if Line:
                menu:
                    extend ""
                    "Итак, что я могу сделать, чтобы ты передумала?":
                            $ JeanX.FaceChange("surprised",1)
                            $ JeanX.Statup("Obed", 90, -10)
                            ch_j "Откуда мне знать?!"
                            $ JeanX.FaceChange("bemused",1,Eyes="side")
                            if not Player.Male:
                                ch_j "Думаю, ты должна дать мне повод тебя уважать или что-нибудь в этом духе?"
                            else:
                                ch_j "Думаю, ты должен дать мне повод тебя уважать или что-нибудь в этом духе?"
                            $ JeanX.FaceChange("sly",1)
                            ch_j "То есть, я согласна просто трахаться, но не хотела бы все усложнять."
                    "Я думаю, это нормально.":
                            $ JeanX.FaceChange("sly",1)
                            $ JeanX.Statup("Love", 200, 5)
                            $ JeanX.Statup("Obed", 90, -5)
                            $ JeanX.Statup("Inbt", 200, 5)
                            ch_j "Рада, что мы все прояснили."
                    "Ну ты и сучка.":
                            $ JeanX.FaceChange("sly",1)
                            $ JeanX.Statup("Obed", 90, 5)
                            $ JeanX.Statup("Inbt", 200, 10)
                            $ JeanX.Statup("Lust", 85, 2)
                            ch_j "Ага, знаю."
        if not Player.Male:
            $ JeanX.Petname = "секс-партнерша"
            $ JeanX.Petname_rod = "секс-партнерши"
            $ JeanX.Petname_dat = "секс-партнерше"
            $ JeanX.Petname_vin = "секс-партнершу"
            $ JeanX.Petname_tvo = "секс-партнершей"
            $ JeanX.Petname_pre = "секс-партнерше"
        else:
            $ JeanX.Petname = "секс-партнер"
            $ JeanX.Petname_rod = "секс-партнера"
            $ JeanX.Petname_dat = "секс-партнеру"
            $ JeanX.Petname_vin = "секс-партнера"
            $ JeanX.Petname_tvo = "секс-партнером"
            $ JeanX.Petname_pre = "секс-партнере"
        $ JeanX.Petnames.append("sex friend")
        return

label Jean_Love:
        #if her Love hits 800 and Obed over 600
        if JeanX.Loc != bg_current:
                "[JeanX.Name] подходит к вам и требует, чтобы вы проследовали за ней."
                $ bg_current = "bg jean"
        elif bg_current != "bg jean" and bg_current != "bg player" :
                "[JeanX.Name] внезапно начинает требовать, чтобы вы проследовали за ней."
                $ bg_current = "bg jean"
        $ Event_Queue = [0,0]
        $ JeanX.Loc = bg_current

        call Set_The_Scene(0)
        call Display_Girl(JeanX)
        call CleartheRoom(JeanX)
        call Set_The_Scene
        call Shift_Focus(JeanX)
        $ JeanX.DailyActions.append("relationship")
        call Taboo_Level
        $ Line = 0
        $ JeanX.FaceChange("sly",1)
        ch_j "Так вот. . . [JeanX.Petname]."
        ch_j "Мы уже довольно давно проводим время вместе."
        ch_j "Думаю, что мое уважение к тебе сильно возросло."
        if JeanX.SEXP >= 30:
                $ JeanX.Statup("Lust", 70, 5)
                ch_j "Ты всегда знаешь, что делать."
        if JeanX.Obed < 900:
                $ JeanX.FaceChange("sly",1,Eyes="side")
                $ JeanX.Statup("Love", 200, 5)
                if not Player.Male:
                    ch_j "И ты так мила со мной. . ."
                else:
                    ch_j "И ты такой милый со мной. . ."
        ch_j "Я чувствую что-то странное. . ."
        $ Line = 0
        menu:
            extend ""
            "Я люблю тебя.":
                    $ Line = "love"
                    $ JeanX.FaceChange("sly",2)
                    ch_j "Я лю-"
                    $ JeanX.FaceChange("surprised",2)
                    $ JeanX.Statup("Love", 90, 10)
                    $ JeanX.Statup("Love", 200, 10)
                    $ JeanX.Statup("Obed", 90, 10)
                    ch_j ". . ."
                    $ JeanX.Statup("Inbt", 200, 5)
                    ch_j "Да, я хотела сказать тоже самое!"
            ". . .":
                    $ JeanX.Statup("Obed", 90, 10)
                    $ JeanX.Statup("Obed", 200, 5)
                    ch_j "Я. . ."
            "Смотрю, ты влюбилась в меня.":
                    $ JeanX.FaceChange("surprised",2)
                    $ JeanX.Statup("Love", 200, 5)
                    $ JeanX.Statup("Obed", 90, 10)
                    $ JeanX.Statup("Obed", 200, 5)
                    ch_j ". . ."
                    $ JeanX.Statup("Inbt", 200, 5)
                    ch_j "Ну. . .  да."
        $ JeanX.FaceChange("sly",1)
        ch_j "Я люблю тебя. . ."
        if Line != "love":
                menu JeanLove_Menu:
                    extend ""
                    "Я тоже тебя люблю.":
                            $ JeanX.Statup("Love", 90, 5)
                            $ JeanX.Statup("Love", 200, 10)
                            $ JeanX.Statup("Obed", 90, 10)
                            $ JeanX.Statup("Inbt", 200, 5)
                            $ JeanX.FaceChange("smile",1)
                            ch_j "Отлично!"
                    ". . ." if not Line:
                            $ Line = "repeat"
                            $ JeanX.FaceChange("sad",2)
                            $ JeanX.Statup("Love", 200, -5)
                            $ JeanX.Statup("Obed", 90, 10)
                            $ JeanX.Statup("Obed", 200, 10)
                            $ JeanX.Statup("Inbt", 200, -5)
                            ch_j "Ну скажи хоть что-нибудь. . ."
                            jump JeanLove_Menu
                    "Клево." if Line != "cool":
                            $ Line = "cool"
                            $ JeanX.FaceChange("angry",1)
                            $ JeanX.Statup("Love", 200, -5)
                            $ JeanX.Statup("Obed", 90, 10)
                            $ JeanX.Statup("Inbt", 200, -5)
                            ch_j "Чувствую, что для тебя все это не серьезно."
                            jump JeanLove_Menu
                    "Извини. . . я хотела сказать, \"это клево.\"" if Line == "cool" and not Player.Male:
                            ch_j ". . ."
                            $ JeanX.Statup("Love", 200, -3)
                            $ JeanX.Statup("Inbt", 200, -3)
                            ch_j "Все еще не похоже. . ."
                            $ JeanX.Statup("Love", 200, 5)
                            ch_j "на подходящий ответ. . ."
                    "Извини. . . я хотел сказать, \"это клево.\"" if Line == "cool" and Player.Male:
                            ch_j ". . ."
                            $ JeanX.Statup("Love", 200, -3)
                            $ JeanX.Statup("Inbt", 200, -3)
                            ch_j "Все еще не похоже. . ."
                            $ JeanX.Statup("Love", 200, 5)
                            ch_j "на подходящий ответ. . ."
                    "Я не могу ответить взаимностью.":
                            $ JeanX.FaceChange("surprised",2)
                            $ JeanX.Statup("Love", 200, -5)
                            $ JeanX.Statup("Obed", 90, 10)
                            $ JeanX.Statup("Obed", 200, 5)
                            $ JeanX.Statup("Inbt", 200, -5)
                            ch_j "Ох. . ."
                            $ JeanX.FaceChange("sadside",1)
                            ch_j "Все номально."
                            ch_j "Не обращай внимание."
        if not Player.Male:
            ch_j "Я просто хотела, чтобы ты знала."
        else:
            ch_j "Я просто хотела, чтобы ты знал."
        $ JeanX.Event[5] = 1
        if not Player.Male:
            $ JeanX.Petname = "любимая"
            $ JeanX.Petname_rod = "любимой"
            $ JeanX.Petname_dat = "любимой"
            $ JeanX.Petname_vin = "любимую"
            $ JeanX.Petname_tvo = "любимой"
            $ JeanX.Petname_pre = "любимой"
        else:
            $ JeanX.Petname = "любимый"
            $ JeanX.Petname_rod = "любимого"
            $ JeanX.Petname_dat = "любимому"
            $ JeanX.Petname_vin = "любимого"
            $ JeanX.Petname_tvo = "любимым"
            $ JeanX.Petname_pre = "любимом"
        $ JeanX.Petnames.append("lover")
        if Player.Harem:
                ch_j "Если ты хочешь, чтобы я присоединилась к твоей маленькой девичьей компании, то я согласна."
        else:
                ch_j "Мы могли бы сделать наши отношения официальными, я могла бы стать твоей девушкой. . ."
        menu:
            extend ""
            "Конечно, чем вас больше, тем веселее." if Player.Harem:
                    $ JeanX.Statup("Love", 200, 5)
                    $ JeanX.Statup("Obed", 90, 10)
                    $ JeanX.Statup("Obed", 200, 10)
                    $ JeanX.Statup("Inbt", 200, 5)
                    $ Player.Harem.append(JeanX)
            "Конечно, я только за." if not Player.Harem:
                    $ JeanX.Statup("Love", 200, 5)
                    $ JeanX.Statup("Obed", 90, 10)
                    $ JeanX.Statup("Obed", 200, 10)
                    $ JeanX.Statup("Inbt", 200, 5)
                    $ Player.Harem.append(JeanX)
            "Мне это не интересно.":
                    $ JeanX.FaceChange("surprised",2)
                    $ JeanX.Statup("Love", 200, -5)
                    $ JeanX.Statup("Obed", 90, 5)
                    $ JeanX.Statup("Inbt", 200, -5)
                    ch_j "Что?"
                    $ JeanX.FaceChange("angry",2)
                    ch_j "Почему?!"
                    if len(Player.Harem) >= 2:
                        ch_j "Это из-за твоих подруг?"
                    elif Player.Harem:
                        ch_j "Это из-за [Player.Harem[0].Name_rod]?"
                    menu:
                        extend ""
                        "Ага" if Player.Harem:
                                $ JeanX.FaceChange("angry",1,Eyes="side")
                                call HaremStatup(JeanX,700,-5) #lowers like of all Harem girls by 5
                                if len(Player.Harem) >= 2:
                                        ch_j "Вот сучки."
                                elif Player.Harem:
                                        ch_j "Вот сучка."
                        "Просто ты мне не нравишься.":
                                $ JeanX.FaceChange("sad",2,Eyes="surprised")
                                $ JeanX.Statup("Love", 90, -5)
                                $ JeanX.Statup("Love", 200, -5)
                                $ JeanX.Statup("Obed", 90, 5)
                                $ JeanX.Statup("Obed", 200, 10)
                                $ JeanX.Statup("Inbt", 200, -5)
                                ch_j "Ох."
                                $ JeanX.FaceChange("sadside",1)
                                ch_j "."
                                ch_j ". ."
                                ch_j ". . ."
                    $ JeanX.FaceChange("smile",1,Brows="angry")
                    ch_j "Ну что ж, надеюсь, ты придешь в себя."
                    ch_j "Не каждый день выпадает возможность начать встречаться с такой девушкой, как я."
            #not interested

        if JeanX in Player.Harem:
            $ JeanX.FaceChange("sly",1)
            ch_j "Хорошо."
            if len(Player.Harem) >= 2:
                #if there are other girls in it
                if len(Player.Harem) >= 3:
                    ch_j "А ты не думаешь, что остальные будут возражать?"
                    $ Line = "они"
                else:
                    ch_j "А ты не думаешь, что [Player.Harem[0].Name] будет возражать?"
                    $ Line = "она"
                menu:
                    extend ""
                    "Нет, [Line] не против." if "JeanYes" in Player.Traits:
                            $ JeanX.Statup("Love", 200, 5)
                            $ JeanX.Statup("Obed", 80, 10)
                            $ JeanX.Statup("Inbt", 80, 5)
                            $ JeanX.FaceChange("surprised",1)
                            ch_j "Ох, хорошо."
                    "Нууу. . . это сперва еще нужно узнать." if "JeanYes" not in Player.Traits:
                            $ JeanX.Statup("Inbt", 200, 5)
                            $ JeanX.Statup("Lust", 80, 3)
                            $ JeanX.FaceChange("confused",1)
                            ch_j "Думаю, я и сама смогу все уладить. . ."
                            menu:
                                extend ""
                                "Нет! Не делай этого!":
                                        $ JeanX.FaceChange("sly",1)
                                        $ JeanX.Statup("Obed", 80, 5)
                                        ch_j "Хорошо."
                                        ch_j ". . ."
                                        $ JeanX.Statup("Inbt", 200, 5)
                                        $ JeanX.Statup("Lust", 80, 2)
                                        ch_j "-подмигивает-"
                                        menu:
                                            extend ""
                                            "Нет! Я знаю, что ты хочешь сделать.":
                                                    $ JeanX.FaceChange("sly",1,Eyes="stunned")
                                                    $ JeanX.Statup("Obed", 50, 5)
                                                    $ JeanX.Statup("Obed", 90, 3)
                                                    pause 0.3
                                                    $ JeanX.FaceChange("sly",1)
                                                    ch_j "ЛАДНО."
                                                    ch_j "Как все уладишь, возвращайся ко мне."
                                                    ch_j ". . . давай только не -слишком- долго."
                                                    $ Player.Harem.remove(JeanX)
                                                    $ JeanX.Event[5] = 20
                                                    jump Misplaced
                                                    return
                                            "[[смириться. . .]":
                                                    ch_j "Ха."
                                "А это хорошая идея. . .":
                                                    $ JeanX.Statup("Love", 200, 3)
                                                    $ JeanX.Statup("Obed", 80, 3)
                                                    $ JeanX.Statup("Inbt", 80, 1)
                                                    $ JeanX.FaceChange("sly",0)
                                                    ch_j "Ага."
            $ JeanX.Petnames.append("boyfriend")
        #end if Player Harem
        $ Line = 0
        jump Misplaced
        return
# End JeanLike / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start JeanSub / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jean_Sub:
        # if her Obedience hits 500
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(JeanX,"bemused","выглядит тихой. . .")
                return
        if JeanX.Loc != bg_current:
                $ JeanX.Loc = bg_current
                "[JeanX.Name] подходит к вам."
        $ Event_Queue = [0,0]
        call Set_The_Scene(0)
        call Display_Girl(JeanX)
        call CleartheRoom(JeanX)
        call Set_The_Scene
        call Shift_Focus(JeanX)
        $ JeanX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in JeanX.History:
                call expression JeanX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        $ Line = 0
        $ JeanX.FaceChange("sly",1,Eyes="side")
        ch_j "Слушай. . . [JeanX.Petname]."
        $ JeanX.Eyes="squint"
        ch_j "Нам нужно поговорить."
        $ JeanX.FaceChange("sadside",1)
        ch_j ". . ."
        ch_j "Когда мы впервые встретились. . . я вела себя грубо."
        ch_j "Признаю."
        $ JeanX.FaceChange("sly",1,Eyes="leftside")
        ch_j "Когда ты, практически, совершенна во всем, возникает желание всех презирать."
        $ JeanX.FaceChange("angry",1,Eyes="leftside")
        ch_j ". . ."
        ch_j "Возможно, это был неправильный подход."
        $ JeanX.FaceChange("sly",1)
        ch_j "Так вот, я хочу сказать, что я узнала много нового о себе, после времени проведенного с тобой."
        ch_j "Ты знаешь, как воздействовать на меня. . ."
        ch_j "Знаешь, как заставить меня делать то, чего я никогда от себя не ожидала. . ."
        ch_j ". . . -Знаешь, как заставить меня. . . -чувствовать- нечто непривычное. . ."
        menu:
            extend ""
            "Так, чего ты от меня хочешь?":
                    $ JeanX.Statup("Love", 80, -3)
                    $ JeanX.Statup("Obed", 90, -3)
                    $ JeanX.Statup("Inbt", 80, 2)
                    ch_j "Ну. . . Не хочу тебе все разжевывать. . ."
            "Хорошо, что ты все поняла.":
                    $ JeanX.Statup("Obed", 80, 3)
                    ch_j ". . ."
            "Да? Как мило!":
                    $ JeanX.FaceChange("confused",1)
                    $ JeanX.Statup("Obed", 80, -3)
                    ch_j "Эм, думаю, до тебя не дошло. . ."

        $ JeanX.History.append("sir")
        menu:
            extend ""
            "Скажи мне, чего ты хочешь.":
                    $ JeanX.FaceChange("sly",1,Eyes="side")
                    $ JeanX.Statup("Love", 80, 5)
                    $ JeanX.Statup("Obed", 90, 2)
                    ch_j "Ну. . ."
                    $ JeanX.Statup("Obed", 90, 2)
                    $ JeanX.Statup("Inbt", 200, 1)
                    $ JeanX.Statup("Lust", 80, 5)
                    if not Player.Male:
                        ch_j "Ты могла бы. . ."
                    else:
                        ch_j "Ты мог бы. . ."
                    $ JeanX.Statup("Obed", 80, 2)
                    $ JeanX.Statup("Inbt", 200, 2)
                    $ JeanX.Statup("Lust", 80, 5)
                    ch_j "приказывать мне побольше?"
            "Зови меня \"Хозяйкой\"" if not Player.Male:
                    $ JeanX.Statup("Love", 200, 5)
                    $ JeanX.Statup("Obed", 90, 10)
                    $ JeanX.Statup("Inbt", 200, 5)
                    $ JeanX.Statup("Lust", 85, 10)
                    $ JeanX.FaceChange("surprised",2)
                    ch_j "!!!"
                    $ JeanX.FaceChange("sly",1,Eyes="side")
                    $ JeanX.Statup("Obed", 90, -5)
                    ch_j "Ну. . . я даже не знаю!"
                    ch_j "Может быть. . . лучше я буду звать тебя. . ."
                    $ JeanX.FaceChange("sly",1)
                    $ JeanX.Statup("Obed", 90, 5)
                    $ JeanX.Statup("Lust", 85, 5)
                    ch_j ". . . госпожой?"
            "Зови меня \"Хозяином\"" if Player.Male:
                    $ JeanX.Statup("Love", 200, 5)
                    $ JeanX.Statup("Obed", 90, 10)
                    $ JeanX.Statup("Inbt", 200, 5)
                    $ JeanX.Statup("Lust", 85, 10)
                    $ JeanX.FaceChange("surprised",2)
                    ch_j "!!!"
                    $ JeanX.FaceChange("sly",1,Eyes="side")
                    $ JeanX.Statup("Obed", 90, -5)
                    ch_j "Ну. . . я даже не знаю!"
                    ch_j "Может быть. . . лучше я буду звать тебя. . ."
                    $ JeanX.FaceChange("sly",1)
                    $ JeanX.Statup("Obed", 90, 5)
                    $ JeanX.Statup("Lust", 85, 5)
                    ch_j ". . . господином?"
            "Ладно?":
                    $ JeanX.FaceChange("confused",1)
                    $ JeanX.Statup("Love", 200, 3)
                    ch_j ". . ."
                    ch_j "Мне кажется, ты еще не совсем понимаешь. . ."
                    ch_j "Возможно, я не совсем ясно выразилась, но. . ."
                    $ JeanX.FaceChange("angry",1,Eyes="side")
                    $ JeanX.Statup("Obed", 80, -3)
                    ch_j "Если мне придется все разжевывать, то значит я ошиблась на твой счет."
                    menu:
                        extend ""
                        "Ты хочешь, чтобы я указывала тебе, что делать." if not Player.Male:
                                $ JeanX.Statup("Love", 200, 3)
                                $ JeanX.Statup("Obed", 90, 5)
                                $ JeanX.Statup("Inbt", 200, 2)
                                ch_j ". . ."
                                $ JeanX.FaceChange("sly",1)
                                $ JeanX.Statup("Obed", 80, 3)
                                $ JeanX.Statup("Lust", 80, 3)
                                ch_j "Да. . ."
                                menu:
                                    extend ""
                                    "И как ты будешь обращаться ко мне?":
                                            $ JeanX.Eyes="side"
                                            ch_j "Как насчет. . ."
                                            $ JeanX.FaceChange("sly",1)
                                            $ JeanX.Statup("Love", 200, 5)
                                            $ JeanX.Statup("Obed", 80, 10)
                                            $ JeanX.Statup("Inbt", 90, 3)
                                            $ JeanX.Statup("Lust", 80, 3)
                                            ch_j ". . . \"госпожа?\""
                                    ". . .":
                                            ch_j "Как насчет того, чтобы я обращалась к тебе. . ."
                                            $ JeanX.Statup("Obed", 80, 10)
                                            $ JeanX.Statup("Inbt", 200, 10)
                                            $ JeanX.Statup("Lust", 80, 3)
                                            ch_j "\"госпожа?\""
                                    "Зови меня \"госпожой.\"":
                                            $ JeanX.Statup("Love", 200, 10)
                                            $ JeanX.Statup("Obed", 90, 15)
                                            $ JeanX.Statup("Lust", 85, 10)
                                            ch_j ". . ."
                                            $ JeanX.Statup("Obed", 90, 5)
                                            ch_j "Да. . . госпожа."
                                # end "You want me to tell you what to do."
                        "Ты хочешь, чтобы я указывал тебе, что делать." if Player.Male:
                                $ JeanX.Statup("Love", 200, 3)
                                $ JeanX.Statup("Obed", 90, 5)
                                $ JeanX.Statup("Inbt", 200, 2)
                                ch_j ". . ."
                                $ JeanX.FaceChange("sly",1)
                                $ JeanX.Statup("Obed", 80, 3)
                                $ JeanX.Statup("Lust", 80, 3)
                                ch_j "Да. . ."
                                menu:
                                    extend ""
                                    "И как ты будешь обращаться ко мне?":
                                            $ JeanX.Eyes="side"
                                            ch_j "Как насчет. . ."
                                            $ JeanX.FaceChange("sly",1)
                                            $ JeanX.Statup("Love", 200, 5)
                                            $ JeanX.Statup("Obed", 80, 10)
                                            $ JeanX.Statup("Inbt", 90, 3)
                                            $ JeanX.Statup("Lust", 80, 3)
                                            ch_j ". . . \"господин?\""
                                    ". . .":
                                            ch_j "Как насчет того, чтобы я обращалась к тебе. . ."
                                            $ JeanX.Statup("Obed", 80, 10)
                                            $ JeanX.Statup("Inbt", 200, 10)
                                            $ JeanX.Statup("Lust", 80, 3)
                                            ch_j "\"господин?\""
                                    "Зови меня \"господином.\"":
                                            $ JeanX.Statup("Love", 200, 10)
                                            $ JeanX.Statup("Obed", 90, 15)
                                            $ JeanX.Statup("Lust", 85, 10)
                                            ch_j ". . ."
                                            $ JeanX.Statup("Obed", 90, 5)
                                            ch_j "Да. . . господин."
                                # end "You want me to tell you what to do."

                        "Думаю, мне все ясно. . .":
                                $ JeanX.Statup("Love", 200, -5)
                                $ JeanX.Statup("Obed", 80, -10)
                                $ JeanX.Statup("Inbt", 90, -10)
                                ch_j "Хмм. . . может и так. . ."
                                return
                    #end "ok?"
        if not Player.Male:
            $ JeanX.Petname = "госпожа"
            $ JeanX.Petname_rod = "госпожи"
            $ JeanX.Petname_dat = "госпоже"
            $ JeanX.Petname_vin = "госпожу"
            $ JeanX.Petname_tvo = "госпожой"
            $ JeanX.Petname_pre = "госпоже"
        else:
            $ JeanX.Petname = "господин"
            $ JeanX.Petname_rod = "господина"
            $ JeanX.Petname_dat = "господину"
            $ JeanX.Petname_vin = "господина"
            $ JeanX.Petname_tvo = "господином"
            $ JeanX.Petname_pre = "господине"
        $ JeanX.Petnames.append("sir")
        $ JeanX.RecentActions.append("asked sub")
        $ JeanX.DailyActions.append("asked sub")
        return


# End JeanSub / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start JeanMaster / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jean_Master:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(JeanX,"bemused","выглядит необычайно тихой. . .")
                return
        if JeanX.Loc != bg_current:
                $ JeanX.Loc = bg_current
                "[JeanX.Name] подходит к вам."
        $ Event_Queue = [0,0]
        call Set_The_Scene(0)
        call Display_Girl(JeanX)
        call CleartheRoom(JeanX)
        call Set_The_Scene
        call Shift_Focus(JeanX)
        $ JeanX.DailyActions.append("relationship")
        call Taboo_Level
        $ Line = 0
        $ JeanX.FaceChange("sly",1,Eyes="side")
        ch_j "Слушай. . . [JeanX.Petname]."
        if not Player.Male:
            ch_j "Ты бы хотела. . . чтобы я звала тебя. . ."
            ch_j ". . .\"хозяйкой?\""
        else:
            ch_j "Ты бы хотел. . . чтобы я звала тебя. . ."
            ch_j ". . .\"хозяином?\""
        $ JeanX.History.append("master")
        menu:
            "Да, хочу.":
                    $ JeanX.FaceChange("sly",1,Eyes="side")
                    $ JeanX.Statup("Love", 200, 5)
                    $ JeanX.Statup("Obed", 200, 5)
                    ch_j "Ну. . . тогда ладно."
                    if not Player.Male:
                        $ JeanX.Petname = "хозяйка"
                        $ JeanX.Petname_rod = "хозяйки"
                        $ JeanX.Petname_dat = "хозяйке"
                        $ JeanX.Petname_vin = "хозяйку"
                        $ JeanX.Petname_tvo = "хозяйкой"
                        $ JeanX.Petname_pre = "хозяйке"
                    else:
                        $ JeanX.Petname = "хозяин"
                        $ JeanX.Petname_rod = "хозяина"
                        $ JeanX.Petname_dat = "хозяину"
                        $ JeanX.Petname_vin = "хозяина"
                        $ JeanX.Petname_tvo = "хозяином"
                        $ JeanX.Petname_pre = "хозяине"
            "Что? Зачем?":
                    $ JeanX.FaceChange("sly",1)
                    $ JeanX.Statup("Obed", 200, 5)
                    $ JeanX.Statup("Inbt", 200, 10)
                    $ JeanX.Statup("Lust", 80, 5)
                    ch_j "Потому, что меня это -заводит!-"
                    ch_j "Ага."
            ". . .":
                    $ JeanX.Statup("Love", 80, -3)
                    $ JeanX.Statup("Obed", 200, 10)
                    $ JeanX.Statup("Inbt", 80, -2)
                    ch_j "Ну. . ."
                    ch_j ". . ."
                    $ JeanX.FaceChange("sly",1)
                    $ JeanX.Statup("Inbt", 80, 10)
                    $ JeanX.Statup("Inbt", 200, 5)
                    if not Player.Male:
                        ch_j "Чтобы ты не сказала, я буду звать тебя так."
                    else:
                        ch_j "Чтобы ты не сказал, я буду звать тебя так."
            "Не особо.":
                    $ JeanX.Statup("Love", 80, -3)
                    $ JeanX.Statup("Obed", 80, 3)
                    $ JeanX.Statup("Inbt", 80, -5)
                    ch_j "Ох. . ."
                    ch_j "Ну, ладно. . ."
                    return
        $ JeanX.Statup("Obed", 200, 5)
        $ JeanX.Statup("Inbt", 200, 5)
        $ JeanX.Statup("Lust", 80, 5)
        $ JeanX.Petnames.append("master")
        $ JeanX.FaceChange("sly",1)
        if not Player.Male:
            ch_j ". . .хозяйка."
        else:
            ch_j ". . .хозяин."
        menu:
            "Ну. . . Ладно.":
                    $ JeanX.FaceChange("confused",1)
                    $ JeanX.Statup("Inbt", 80, -1)
                    ch_j ". . . хорошо?"
            "Думаю, ты не понимаешь, к чему это обязывает.":
                    $ JeanX.FaceChange("confused",1)
                    $ JeanX.Statup("Love", 200, -2)
                    $ JeanX.Statup("Obed", 80, 1)
                    ch_j "Да, не понимаю."
                    menu:
                        "Ничего страшного.":
                                $ JeanX.FaceChange("sly",1)
                                $ JeanX.Statup("Love", 200, 5)
                                $ JeanX.Statup("Obed", 200, 5)
                                $ JeanX.Statup("Inbt", 200, 2)
                                ch_j "Хорошо!"
                        "Ты должна выполнять все мои указания. . .":
                                $ JeanX.Statup("Love", 200, 5)
                                $ JeanX.Statup("Obed", 200, 10)
                                ch_j "Эм, ага."
                                $ JeanX.FaceChange("sly",1)
                                ch_j "С этим я справлюсь!"
            "Не надо.":
                    $ JeanX.FaceChange("sadside",1)
                    $ JeanX.Statup("Love", 80, -10)
                    $ JeanX.Statup("Obed", 80, -5)
                    $ JeanX.Statup("Inbt", 80, -10)
                    ch_j "Ох. . ."
                    if not Player.Male:
                        ch_j "Ты мне все обломал."
                    else:
                        ch_j "Ты мне все обломала."
                    return
        $ JeanX.FaceChange("sly",1)
        if not Player.Male:
            $ JeanX.Petname = "хозяйка"
            $ JeanX.Petname_rod = "хозяйки"
            $ JeanX.Petname_dat = "хозяйке"
            $ JeanX.Petname_vin = "хозяйку"
            $ JeanX.Petname_tvo = "хозяйкой"
            $ JeanX.Petname_pre = "хозяйке"
        else:
            $ JeanX.Petname = "хозяин"
            $ JeanX.Petname_rod = "хозяина"
            $ JeanX.Petname_dat = "хозяину"
            $ JeanX.Petname_vin = "хозяина"
            $ JeanX.Petname_tvo = "хозяином"
            $ JeanX.Petname_pre = "хозяине"
        $ JeanX.Statup("Obed", 90, 50)
        $ JeanX.Statup("Obed", 200, 25)
        pause 0.1
        return

# end JeanMaster / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# start Jean_Daddy//////////////////////////////////////////////////////////

#Not updated

label Jean_Daddy:       #Jean_Update
        $ JeanX.DailyActions.append("relationship")
        if JeanX.Loc != bg_current:
                $ JeanX.Loc = bg_current
                "[JeanX.Name] подходит к вам."
        $ Event_Queue = [0,0]
        call Shift_Focus(JeanX)
        call Set_The_Scene
        ch_j ". . ."
        if JeanX in Player.Harem:
            ch_j "Ладно, я знаю, что мы уже встречаемся. . ."
        else:
            ch_j "Я. . . ведь тебе нравлюсь, так?"
        if JeanX.Love > JeanX.Obed and JeanX.Love > JeanX.Inbt:
            ch_j "И я вся горю. . ."
        elif JeanX.Obed > JeanX.Inbt:
            ch_j "И я. . . \"уважаю\" тебя? . ."
        else:
            ch_j "и все было весело. . ."
        ch_j "Я тут подумала, знаешь, что было бы очень сексуально? . ."
        if not Player.Male:
            ch_j "Если бы я начала звать тебя. . . \"мамочкой.\" Что скажешь?"
        else:
            ch_j "Если бы я начала звать тебя. . . \"папочкой.\" Что скажешь?"
        menu:
            extend ""
            "Хорошо?":
                $ JeanX.FaceChange("smile")
                $ JeanX.Statup("Love", 90, 20)
                $ JeanX.Statup("Obed", 60, 10)
                $ JeanX.Statup("Inbt", 80, 30)
                ch_j "Клево."
            "Что это значит?":
                $ JeanX.FaceChange("bemused")
                ch_j "Это немного странно, согласна. . ."
                if not Player.Male:
                    ch_j "Но я хочу звать тебя \"мамочкой\"."
                else:
                    ch_j "Но я хочу звать тебя \"папочкой\"."

                menu:
                    extend ""
                    "Звучит интересно, я за.":
                            $ JeanX.FaceChange("smile")
                            $ JeanX.Statup("Love", 90, 15)
                            $ JeanX.Statup("Obed", 60, 20)
                            ch_j "Хорошо."
                            ch_j "Nice."
                            $ JeanX.FaceChange("sly",2)
                            if not Player.Male:
                                ch_j " . . . мамочка."
                            else:
                                ch_j " . . . папочка."
                            $ JeanX.FaceChange("sly",1)
                            if not Player.Male:
                                $ JeanX.Petname = "мамочка"
                                $ JeanX.Petname_rod = "мамочки"
                                $ JeanX.Petname_dat = "мамочке"
                                $ JeanX.Petname_vin = "мамочку"
                                $ JeanX.Petname_tvo = "мамочкой"
                                $ JeanX.Petname_pre = "мамочке"
                            else:
                                $ JeanX.Petname = "папочка"
                                $ JeanX.Petname_rod = "папочки"
                                $ JeanX.Petname_dat = "папочке"
                                $ JeanX.Petname_vin = "папочку"
                                $ JeanX.Petname_tvo = "папочкой"
                                $ JeanX.Petname_pre = "папочке"
                    "Пожалуйста, не надо.":
                            $ JeanX.Statup("Love", 90, 5)
                            $ JeanX.Statup("Obed", 80, 40)
                            $ JeanX.Statup("Inbt", 80, 20)
                            $ JeanX.FaceChange("angry",2)
                            ch_j "   . . .   "
                            ch_j "Ладно, как хочешь!"
                            $ JeanX.FaceChange("angry",1,Eyes="side")
                    "У тебя были непростые отношения с матерью, да?" if not Player.Male:
                            $ JeanX.Statup("Love", 90, -15)
                            $ JeanX.Statup("Obed", 80, 45)
                            $ JeanX.Statup("Inbt", 70, 5)
                            $ JeanX.FaceChange("angry",2)
                            ch_j "Ох, забудь, будто ты что-то знаешь!"
                            $ JeanX.FaceChange("angry",1,Eyes="side")
                    "У тебя были непростые отношения с отцом, да?" if Player.Male:
                            $ JeanX.Statup("Love", 90, -15)
                            $ JeanX.Statup("Obed", 80, 45)
                            $ JeanX.Statup("Inbt", 70, 5)
                            $ JeanX.FaceChange("angry",2)
                            ch_j "Ох, забудь, будто ты что-то знаешь!"
                            $ JeanX.FaceChange("angry",1,Eyes="side")
            "У тебя были непростые отношения с матерью, да?" if not Player.Male:
                            $ JeanX.Statup("Love", 90, -15)
                            $ JeanX.Statup("Obed", 80, 45)
                            $ JeanX.Statup("Inbt", 70, 5)
                            $ JeanX.FaceChange("angry",2)
                            ch_j "Ох, забудь, будто ты что-то знаешь!"
                            $ JeanX.FaceChange("angry",1,Eyes="side")
            "У тебя были непростые отношения с отцом, да?" if Player.Male:
                            $ JeanX.Statup("Love", 90, -15)
                            $ JeanX.Statup("Obed", 80, 45)
                            $ JeanX.Statup("Inbt", 70, 5)
                            $ JeanX.FaceChange("angry",2)
                            ch_j "Ох, забудь, будто ты что-то знаешь!"
                            $ JeanX.FaceChange("angry",1,Eyes="side")
        $ JeanX.Petnames.append("daddy")
        return

# end Jean_Daddy//////////////////////////////////////////////////////////


label JeanName(Base=0,JNNum=0,Alpha=0,JeanNames={}):
        if Base == 1:
                $ Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЮЭЯЬЪ"
                $ JNNum = renpy.random.randint(0,58)
                $ Base = str(Alpha[JNNum]) #peels off random number from alphabet
        elif Base:
                pass
        else:
                $ Base = Player.Name[:1] #takes first letter of player's name
        if Player.Male:
            #guy names
            $ JeanNames = { "A":"Эйб",
                            "B":"Барри",
                            "C":"Карл",
                            "D":"Деннис",
                            "E":"Эрик",
                            "F":"Фогги",
                            "G":"Джил",
                            "H":"Хэнк",
                            "I":"Айк",
                            "J":"Джеф",
                            "K":"Кирк",
                            "L":"Ленс",
                            "M":"Митч",
                            "N":"Норм",
                            "O":"Олли",
                            "P":"Пит",
                            "Q":"Квинс",
                            "R":"Рори",
                            "S":"Сонни",
                            "T":"Тодд Говард",
                            "U":"Юри",
                            "V":"Винс",
                            "W":"Уолли",
                            "X":"Рэй",
                            "Y":"Юрий",
                            "Z":"Зоро",
                            "А":"Эйб",
                            "Б":"Барри",
                            "В":"Винс",
                            "Г":"Ганс",
                            "Д":"Джил",
                            "Е":"Энди",
                            "Ё":"Йож",
                            "Ж":"Жан",
                            "З":"Зоро",
                            "И":"Ирвин",
                            "К":"Кирк",
                            "Л":"Ленс",
                            "М":"Митч",
                            "Н":"Норм",
                            "О":"Олли",
                            "П":"Пит",
                            "Р":"Рори",
                            "С":"Сонни",
                            "Т":"Тодд Говард",
                            "У":"Уль",
                            "Ф":"Фогги",
                            "Х":"Хэнк",
                            "Ц":"Цэрри",
                            "Ч":"Чэс",
                            "Ш":"Шон",
                            "Щ":"Щен",
                            "Ь":"Ъуъ",
                            "Ъ":"Ъуъ",
                            "Ы":"Ын",
                            "Э":"Эскобар",
                            "Ю":"Юсуф",
                            "Я":"Ян",
                            "Й":"Йож"
                            }
        else:
            #girl names
            $ JeanNames = { "A":"Элли",
                            "B":"Бетти",
                            "C":"Карла",
                            "D":"Деннис",
                            "E":"Эрика",
                            "F":"Фран",
                            "G":"Джил",
                            "H":"Хильда",
                            "I":"Ирма",
                            "J":"Дженни",
                            "K":"Кирстен",
                            "L":"Люси",
                            "M":"Мэри Джейн",
                            "N":"Норма",
                            "O":"Оливия",
                            "P":"Пэг",
                            "Q":"Квинелла",
                            "R":"Рори",
                            "S":"Сьюзи",
                            "T":"Трейси",
                            "U":"Ума",
                            "V":"Вин",
                            "W":"Венди",
                            "X":"Рэй",
                            "Y":"Юри",
                            "Z":"Зи",
                            "А":"Анна",
                            "Б":"Бетти",
                            "В":"Вин",
                            "Г":"Гретта",
                            "Д":"Джил",
                            "Е":"Эрика",
                            "Ё":"Йожа",
                            "Ж":"Жанна",
                            "З":"Зираэль",
                            "И":"Ирка",
                            "К":"Клара",
                            "Л":"Ленка",
                            "М":"Мина",
                            "Н":"Норма",
                            "О":"Олли",
                            "П":"Пенни",
                            "Р":"Рори",
                            "С":"Соня",
                            "Т":"Тамара",
                            "У":"Ульяна",
                            "Ф":"Фрея",
                            "Х":"Хелена",
                            "Ц":"Цирилла",
                            "Ч":"Черри",
                            "Ш":"Шильда",
                            "Щ":"Щерри",
                            "Ь":"Ъуъ",
                            "Ъ":"Ъуъ",
                            "Ы":"Ыбба",
                            "Э":"Элли",
                            "Ю":"Юлька",
                            "Я":"Яна",
                            "Й":"Йожа"
                            }
        $ Base = Base.upper() #should return the upper case version of a lowercase letter?
        if Base in JeanNames and JeanNames[Base] != Player.Name:
                $ JeanX.Petname = JeanNames[Base]
        else:
                #If the name is a dupe or not a valid name, pick a random letter
                $ Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЮЭЯЬЪ"
                $ JNNum = renpy.random.randint(0,58)
                $ Base = str(Alpha[JNNum]) #peels off random number from alphabet
                $ JeanX.Petname = JeanNames[Base]

        return
# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jean_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        if "switched" in JeanX.History:
                jump Jean_Switch2
        $ JeanX.FaceChange("angry", 1)
        ch_j "Извини."
        if not Player.Male:
            ch_j "Ты не видела [JeanX.Petname_vin]?"
        else:
            ch_j "Ты не видел [JeanX.Petname_vin]?"
        menu:
            extend ""
            "Это я и есть, [JeanX.Petname].":
                    $ JeanX.FaceChange("confused", 1)
                    ch_j "О."
                    $ JeanX.FaceChange("smile", 1)
                    ch_j "Мне показалось, что ты выглядишь по-другому."
                    $ JeanX.AddWord(1,"switch") #recent
            "Нет.":
                    ch_j ". . ."
            "Возможно?":
                    ch_j "Не надо со мной играть."

        if "switch" not in JeanX.RecentActions:
                    $ JeanX.FaceChange("confused", 1)
                    ch_j ". . ."
                    $ JeanX.FaceChange("angry", 1,Eyes="psychic")
                    ch_j ". . ."
                    ch_j "О, ты и -есть- [JeanX.Petname]."
                    $ JeanX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Ага, это я.":
                                $ JeanX.Statup("Love", 70, 1)
                                $ JeanX.Statup("Love", 90, 1)
                                $ JeanX.Statup("Obed", 80, 1)
                                $ JeanX.Statup("Obed", 90, 2)
                                ch_j "Кажется, в тебе что-то изменилось. . ."
                        "Нет.":
                                $ JeanX.FaceChange("angry", 1)
                                $ JeanX.Statup("Obed", 80, 2)
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j ". . ."
                        "Возможно?":
                                $ JeanX.FaceChange("angry", 1)
                                $ JeanX.Statup("Love", 80, 1)
                                $ JeanX.Statup("Obed", 90, 1)
                                $ JeanX.Statup("Inbt", 60, 1)
                                ch_j ". . ."
                    ch_j "К чему была эта ложь?"
                    menu:
                        extend ""
                        "Извини, хотелось пошутить.":
                                $ JeanX.FaceChange("angry", 1)
                                $ JeanX.Statup("Love", 70, 1)
                                $ JeanX.Statup("Obed", 60, 1)
                                $ JeanX.Statup("Obed", 70, 1)
                                ch_j ". . ."
                        "Молодец, ты все поняла.":
                                $ JeanX.FaceChange("sly", 1)
                                $ JeanX.Statup("Love", 70, 1)
                                $ JeanX.Statup("Obed", 60, 1)
                                $ JeanX.Statup("Obed", 70, 1)
                                $ JeanX.Statup("Inbt", 80, 1)
                                ch_j "Еще бы."
                        "Хех.":
                                $ JeanX.FaceChange("confused", 1,Eyes="side")
                                $ JeanX.Statup("Love", 70, 1)
                                $ JeanX.Statup("Love", 90, 1)
                                $ JeanX.Statup("Inbt", 70, 1)
                                ch_j "Ха. . ."
        #end "tried to lie"
        $ JeanX.FaceChange("smile", 1)
        if Player.Male:
                ch_j "Ты. . . теперь выше?"
                ch_p "Я теперь парень."
        else:
                ch_j "Ты. . . теперь ниже?"
                ch_p "Я теперь девушка."
        ch_j "Так. . . ты. . . не. . ."
        ch_j "Да, я заметила."
        ch_j "К чему эти перемены?"
        menu:
            extend ""
            "Да так, по приколу.":
                    pass
            "Я так себя сейчас ощущаю.":
                    pass
            "У меня не было каких-то особых причин.":
                    pass
        ch_j "Ох. ладно"

        if [Player.Name] != [Player.XName]:
                ch_p "А еще теперь меня зовут [Player.Name]."
                call JeanName
                ch_j "Для меня ты все равно, [JeanX.Petname]."
        $ JeanX.Traits.remove("switchcheck")
        $ JeanX.AddWord(1,0,0,0,"switched") #history
        return

label Jean_Switch2:
        #when you switch for a 2+ time
        call JeanName
        $ JeanX.Traits.remove("switchcheck")
        $ JeanX.History.remove("switched")
        $ JeanX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jean_Girltalk(Auto=0,Other=0):
        # if Auto Jean starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in JeanX.History:
                return
#        if "nogirls" in JeanX.History: #unneeded, she never refuses
#                jump Jean_Girltalk_Redux
        if Auto:
                $ JeanX.DrainWord("nogirls",0,0,0,1) #history
                $ JeanX.AddWord(1,0,0,0,"girltalk") #history
                return
                #Jean does not care.
        else:
                $ JeanX.FaceChange("confused", 1)
                ch_j "О, ты пытаешься заигрывать со мной?"
        menu:
            extend ""
            "Да?":
                    $ JeanX.FaceChange("normal",1,Eyes="side")
                    $ JeanX.Statup("Love", 90, 2)
                    $ JeanX.Statup("Obed", 70, 1)
                    $ JeanX.Statup("Obed", 90, 2)
                    ch_j "Хмм. . ."
            "Возможно?":
                    $ JeanX.FaceChange("confused", 2)
                    $ JeanX.Statup("Obed", 60, 2)
                    $ JeanX.Statup("Obed", 80, 2)
                    $ JeanX.Statup("Inbt", 80, 2)
                    ch_j "Ты не знаешь?"
            "Да нет.":
                    $ JeanX.FaceChange("angry", 1)
                    $ JeanX.Statup("Love", 50, -2)
                    $ JeanX.Statup("Love", 90, -2)
                    $ JeanX.Statup("Obed", 60, 2)
                    $ JeanX.Statup("Obed", 80, 2)
                    ch_j "Кого ты обманываешь, я же вижу. . ."
        $ JeanX.FaceChange("sly", 1)
        ch_j "Что ж. . . Я думаю, ты, наверное, знаешь, как обращаться с женским телом. . ."
        $ JeanX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(JeanX)
        return

label Jean_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing
        $ JeanX.FaceChange("sly", 1)
        if not JeanX.Forced:
                #if Forced, she will just go with it anyway
                ch_j "Что ж. . . Я думаю, ты, наверное, знаешь, как обращаться с женским телом. . ."
        $ JeanX.DrainWord("nogirls",0,0,0,1) #history
        $ JeanX.AddWord(1,0,0,0,"girltalk") #history
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Jean_69_Intro:
    return
