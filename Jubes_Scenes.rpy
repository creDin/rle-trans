
#Start Jubes_Meet / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_Meet:
        #jubilee's introduction scene
        #called from Sleepover if bg_current == "bg player" and "met" in StormX.History and "met" not in JubesX.History:

        show blackscreen onlayer black
        $ JubesX.OutfitDay = "casual2"
        $ JubesX.Outfit = "casual2"
        $ JubesX.OutfitChange("casual2")
        call CleartheRoom("All",0,1)
        $ JubesX.Loc = bg_current
        $ JubesX.Love = 500
        $ JubesX.Obed = 50
        $ JubesX.Inbt = 50
        $ JubesX.SpriteLoc = StageCenter
        if not Player.Male:
            $ JubesX.Petname = "сис"
            $ JubesX.Petname_rod = "сис"
            $ JubesX.Petname_dat = "сис"
            $ JubesX.Petname_vin = "сис"
            $ JubesX.Petname_tvo = "сис"
            $ JubesX.Petname_pre = "сис"
        else:
            $ JubesX.Petname = "бро"
            $ JubesX.Petname_rod = "бро"
            $ JubesX.Petname_dat = "бро"
            $ JubesX.Petname_vin = "бро"
            $ JubesX.Petname_tvo = "бро"
            $ JubesX.Petname_pre = "бро"
        $ JubesX.Names = []
        $ JubesX.Name = "???"

        $ Player.AddWord(1,0,"Intro",0,0) #adds tag to Daily
        $ Player.AddWord(1,"interruption") #prevents interruption
        $ Player.Focus = 30
        ch_u "\"Хлюп, хлюп, хлюп.\""

        $ Player.Statup("Focus", 80, 5)
        $ JubesX.Statup("Lust", 80, 5)

#        $ JubesX.RecentActions.append("blanket")
#        call expression JubesX.Tag + "_BJ_Launch"

        $ JubesX.FaceChange("sucking",1)

        "Вы испытываете приятные ощущения. . ."
        ch_u "\"Хлюп, хлюп, хлюп.\""
        $ Player.Statup("Focus", 80, 5)
        $ JubesX.Statup("Lust", 80, 5)
        $ JubesX.Addictionrate += 1 #starts her addiction path

        "В области чуть ниже талии. . ."
        ch_u "\"Хлюп, хлюп, хлюп.\""
        $ Player.Statup("Focus", 80, 10)
        $ JubesX.Statup("Lust", 80, 5)

        "Хотя нет. . . вы ошиблись. . ."
        call Shift_Focus(JubesX)

        $ JubesX.ArmPose = 2
        show Jubes_Sprite at SpriteLoc(StageRight) zorder JubesX.Layer:
            ease 0.1 offset (100,50) zoom 2.5 alpha 1
            block:
                ease 1 yoffset 100
                pause .2
                ease 1 yoffset 50
                repeat

        "Вы открываете глаза. . ."
        hide blackscreen onlayer black

        $ Count = 3
        $ Line = 0
        "Кажется, кто-то присосался к вашей шее. . ."
        while Count > 0:
                #Looping portion
                $ Player.Statup("Focus", 80, 10)
                $ JubesX.Statup("Lust", 80, 5)
                menu:
                    extend ""
                    "Молчать":
                        $ JubesX.Statup("Inbt", 90, 2)
                        $ JubesX.Statup("Lust", 80, 5)
                        $ JubesX.Addictionrate += 1
                        if Count > 2:
                            "Вы позволяете ей продолжать, притворившись, что все еще спите."
                            ch_v "\"Хлюп, хлюп, хлюп.\""
                            ". . ."
                        elif Count > 1:
                            "Это очень приятно. . ."
                            ch_v "\"Хлюп, хлюп, хлюп.\""
                            ". . ."
                        else:
                            "Вы не хотите ее беспокоить. . ."
                            ch_v "\"Хлюп, хлюп, хлюп.\""
                            show blackscreen onlayer black
                            ". . ."
                            $ JubesX.Statup("Love", 90, 2)
                            $ JubesX.FaceChange("surprised",2)
                            show Jubes_Sprite:
                                ease 0.2 offset (100,50) zoom 2.5 alpha 1
                            ch_v "Ой! Эм. . . это плохо. . ."
                            ch_v "Проснись! Проснись! Извини!!!!"
                            "Вы медленно приходите в себя. . ."
                            hide blackscreen onlayer black
                            ch_v "Извини!"
                            show Jubes_Sprite:
                                ease 0.5 offset (100,0) zoom 1.5 alpha 1
                            ch_v "Думаю, я, наверное, слишком много выпила!"
                            $ JubesX.FaceChange("sadside",1)
                            ch_v "Меня просто. . . мучила дикая жажда. . ."
                    "Эм. . .  дамочка? Что ты делаешь?":
                            $ JubesX.Statup("Obed", 90, 5)
                            $ JubesX.Statup("Inbt", 90, -1)
                            $ JubesX.FaceChange("surprised",2)
                            show Jubes_Sprite:
                                ease 0.5 offset (100,0) zoom 1.5 alpha 1
                            ch_v "Ах!"
                            $ JubesX.FaceChange("sadside",1,Mouth="normal")
                            ch_v "О, я. . . эм. . ."
                            $ Count = 1
                    "Как же классно, продолжай. . .":
                            $ JubesX.Statup("Love", 90, 2)
                            $ JubesX.Statup("Inbt", 90, 2)
                            $ JubesX.FaceChange("surprised",2)
                            show Jubes_Sprite:
                                ease 0.5 offset (100,0) zoom 1.5 alpha 1
                            ch_v "Ох!"
                            $ JubesX.FaceChange("sadside",1,Mouth="smile")
                            ch_v "Я, эм. . . не ожидала такой реакции. . ."
                            $ JubesX.FaceChange("sad",1,Mouth="smile")
                            $ Count = 1
                    "Эй, прекрати!":
                            $ JubesX.Statup("Obed", 90, 10)
                            $ JubesX.Statup("Inbt", 90, -3)
                            $ JubesX.FaceChange("surprised",2)
                            show Jubes_Sprite:
                                ease 0.5 offset (100,0) zoom 1.5 alpha 1
                            ch_v "Ах!"
                            $ JubesX.FaceChange("sadside",1,Mouth="normal")
                            ch_v "Извини!"
                            $ Count = 1
                $ Count -= 1
        $ JubesX.Blush = 1
        show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc,50)
        $ Count = 3
        while Count > 0:
            menu:
                extend ""
                "Ты кто?" if "Jubilee" not in JubesX.Names:
                        $ JubesX.Statup("Love", 90, 2)
                        $ JubesX.Statup("Obed", 90, 1)
                        $ JubesX.FaceChange("smile",1)
                        ch_v "О, думаю, мне стоит представиться."
                        ch_v "Меня зовут \"Джубили.\""
                        $ JubesX.Names.append("Jubilee")
                        $ JubesX.Name = "Джубили"
                        $ JubesX.Petname_rod = "Джубили"
                        $ JubesX.Petname_dat = "Джубили"
                        $ JubesX.Petname_vin = "Джубили"
                        $ JubesX.Petname_tvo = "Джубили"
                        $ JubesX.Petname_pre = "Джубили"
                        ch_v "Приятно поза- познакомиться."
                        menu:
                            extend ""
                            "Ладно. . .":
                                    $ JubesX.FaceChange("confused",1)
                                    $ JubesX.Statup("Obed", 90, 3)
                                    ch_v ". . ."
                            "А я [Player.Name].":
                                    $ JubesX.Statup("Love", 90, 3)
                                    $ JubesX.Statup("Obed", 90, 2)
                                    ch_v "О, да, Я знаю."
                                    $ JubesX.Statup("Inbt", 90, 2)
                                    ch_v "Я. . . слышала о тебе."
                            "Хм.":
                                    $ JubesX.FaceChange("confused",1)
                                    ch_v ". . ."
                #end "who are you"


                "Интересное имя." if "Jubilee" in JubesX.Names and "Jubilation" not in JubesX.Names:
                        #only plays after Jubilee but before this bit
                        $ JubesX.FaceChange("smile",1)
                        ch_v "Ну, да. Это все мои странные родители."
                        ch_v "На самом деле, мое полное имя \"Джубилейшен Ли,\" но знаешь. . ."
                        ch_v "Наверное, мне стоит от него отречься?"
                        $ JubesX.Names.append("Jubilation")
                        $ JubesX.Names.append("Miss Lee")
                        $ JubesX.Pets.append("Miss Lee")
                        menu:
                            extend ""
                            "Да, конечно.":
                                    $ JubesX.Statup("Love", 90, 1)
                                    $ JubesX.Statup("Obed", 90, 3)
                                    ch_v ". . ."
                            "Тебе идет это имя.":
                                    $ JubesX.Statup("Love", 90, 5)
                                    $ JubesX.Statup("Inbt", 90, 2)
                                    ch_v ". . ."
                            "Стремное имечко.":
                                    $ JubesX.FaceChange("angry",1)
                                    $ JubesX.Statup("Love", 90, -3)
                                    $ JubesX.Statup("Obed", 90, 3)
                                    $ JubesX.Statup("Inbt", 90, 1)
                                    ch_v ". . ."
                                    $ JubesX.FaceChange("normal",1)
                #end "interesting name"


                "Что ты делаешь в моей комнате?!" if "thirst" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 90, -1)
                        $ JubesX.Statup("Obed", 90, 7)
                        $ JubesX.Statup("Inbt", 90, -2)
                        $ JubesX.FaceChange("startled",2)
                        ch_v "Ох, меня просто. . . мучила жажда?"
                        $ JubesX.FaceChange("smile",1)
                        $ JubesX.AddWord(1,"thirst",0,0,0) #adds "word" tag to Recent

                #end "what are you in my room"
                "Что ты делала?" if "thirst" not in JubesX.RecentActions:
                        $ JubesX.Statup("Inbt", 90, 1)
                        $ JubesX.FaceChange("startled",2)
                        ch_v "Я просто. . . пила?"
                        $ JubesX.FaceChange("smile",1)
                        $ JubesX.AddWord(1,"thirst",0,0,0) #adds "word" tag to Recent

                #end "what are you doing"


                "Значит, ты пьешь кровь?" if "vamp" in JubesX.RecentActions and "blood" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 90, 1)
                        $ JubesX.FaceChange("sadside",2)
                        ch_v "Ага, мне вроде как это необходимо. . ."
                        $ JubesX.FaceChange("sad",1)
                        ch_v "Извини еще раз. . ."
                        $ JubesX.AddWord(1,"blood",0,0,0) #adds "word" tag to Recent
                "Ты можешь превращаться в летучую мышь?" if "vamp" in JubesX.RecentActions and "bat" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 90, 1)
                        $ JubesX.FaceChange("confused",1)
                        ch_v "Нууу, нет. . ."
                        $ JubesX.FaceChange("sly",1)
                        ch_v "Но я сильная и могу превращаться в туман."
                        ch_v "Иногда."
                        $ JubesX.AddWord(1,"bat",0,0,0) #adds "word" tag to Recent
                "Это заразно?" if "vamp" in JubesX.RecentActions and "contagious" not in JubesX.History:
                        $ JubesX.FaceChange("sadside",2)
                        ch_v "Когда-то было. . ."
                        $ JubesX.FaceChange("surprised",1,Mouth="sucking")
                        ch_v "- но теперь нет!"
                        $ JubesX.FaceChange("sadside",1)
                        ch_v "Доктор Стрэндж позаботился об этом."
                        if not Player.Male:
                            ch_v "Так что не волнуйся, ты не станешь такой, как я."
                        else:
                            ch_v "Так что не волнуйся, ты не станешь таким, как я."
                        $ JubesX.FaceChange("sad",1)
                        $ JubesX.AddWord(1,0,0,0,"contagious") #adds "word" tag to History
                "Почему я?" if "vamp" in JubesX.RecentActions and "devamp" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 90, 1)
                        $ JubesX.FaceChange("sly",1,Eyes="side")
                        ch_v "Нууу. . ."
                        ch_v "Я подумала. . ."
                        ch_v "Что раз ты можешь сводить на нет силы других, то, возможно. . ."
                        $ JubesX.FaceChange("smile",1)
                        ch_v "Ты сможешь \"де-вампиризировать\" меня?"
                        $ JubesX.AddWord(1,"devamp",0,0,0) #adds "word" tag to Recent
                        menu:
                            extend ""
                            "Ты не хочешь быть вампиром?":
                                    $ JubesX.Statup("Love", 90, 2)
                                    $ JubesX.Statup("Obed", 90, 1)
                                    ch_v "Нууу, нет. . ."
                            "Возможно.":
                                    $ JubesX.FaceChange("confused",1)
                                    $ JubesX.Statup("Love", 90, -1)
                                    ch_v ". . ."
                        ch_v "Способности - это круто и все такое, но я даже не могу выйти на улицу днем!"
                        ch_v "и, конечно, мне постоянно нужна кровь."
                        $ JubesX.FaceChange("normal",1)

                        menu:
                            extend ""
                            "Я понимаю, это неприятно.":
                                    $ JubesX.Statup("Love", 90, 2)
                                    $ JubesX.Statup("Inbt", 90, 1)
                                    ch_v ". . ."
                            "Угу. . .":
                                    $ JubesX.Statup("Obed", 90, 1)
                                    $ JubesX.Statup("Inbt", 90, 1)
                                    ch_v ". . ."


                "Ты мутант?" if "mutant" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 90, 2)
                        $ JubesX.FaceChange("smile",1)
                        ch_v "Да! Конечно!"
                        $ JubesX.FaceChange("smile",1,Eyes="side")
                        if "vamp" in JubesX.RecentActions:
                                ch_v "Помимо всего прочего, я мутант. . ."
                        else:
                                ch_v ". . . в том числе и мутант. . ."
                        $ JubesX.AddWord(1,"mutant",0,0,0) #adds "word" tag to Recent
                        menu:
                            extend ""
                            "Какая у тебя способность?":
                                    $ JubesX.Statup("Love", 90, 3)
                                    $ JubesX.Statup("Inbt", 90, 1)
                                    ch_v ". . ."
                            "Ладно.":
                                    $ JubesX.Statup("Love", 90, -1)
                                    $ JubesX.Statup("Obed", 90, 3)
                                    $ JubesX.FaceChange("confused",1)
                                    ch_v "Тебе даже не любопытно, какие у меня способности?"
                        $ JubesX.FaceChange("smile",1)
                        ch_v "Я умею стрелять фейерверками."
                        $ JubesX.ArmPose = 1
                        show Fireworks onlayer black as Fire1:
                                pos (JubesX.SpriteLoc+300,350)#+160,270)
                        show Fireworks onlayer black as Fire2:
                                pos (JubesX.SpriteLoc+300,350)
                        ch_v "Пиу-пиу!"
                        menu:
                            extend ""
                            "Круто!":
                                    $ JubesX.Statup("Love", 90, 3)
                                    $ JubesX.Statup("Inbt", 90, 5)
                                    ch_v "Спасибо!"
                            "Ну ладно.":
                                    $ JubesX.Statup("Obed", 90, 2)
                                    $ JubesX.Statup("Inbt", 90, -1)
                                    $ JubesX.FaceChange("angry",1,Eyes="side")
                                    ch_v "Ладно, это, конечно, не так круто, как \"отмена способностей мутантов\" или что-то подобное. . ."
                                    ch_v "Но я могу делать и другие вещи. . ."
                                    $ JubesX.FaceChange("normal",1)
                            ". . .":
                                    $ JubesX.Statup("Obed", 90, 2)
                                    ch_v ". . ."


                "Что ж, думаю, у меня больше нет вопросов.":
                    $ JubesX.AddWord(1,"thirst",0,0,0) #adds "word" tag to Recent if she's missed it so far
                    $ Count = 0

            if "thirst" in JubesX.RecentActions and "vamp" not in JubesX.RecentActions:
                    "Вы чувствуете, как что-то щекочет вам шею, вы протираете это место рукой, а затем осматриваете руку. Она в крови."
                    menu:
                        extend ""
                        "О. Кровь. . .":
                                $ JubesX.Statup("Love", 90, 2)
                                $ JubesX.Statup("Obed", 90, 3)
                                $ JubesX.Statup("Inbt", 90, -2)
                                $ JubesX.FaceChange("angry",1,Eyes="squint",Mouth="kiss")
                                if not Player.Male:
                                    ch_v "Ты -удивительно- спокойна."
                                else:
                                    ch_v "Ты -удивительно- спокоен."
                                $ JubesX.FaceChange("smile",1,Eyes="surprised", Brows = "sad")
                                ch_v "Может, я переборщила? . ."
                        "Почему у меня кровоточит шея?":
                                $ JubesX.Statup("Love", 90, 4)
                                $ JubesX.Statup("Obed", 90, 2)
                                $ JubesX.FaceChange("sadside",1)
                                ch_v "Нууу. . . ты это. . ."
                                ch_v "Извини."
                        "Какого хуя?!":
                                $ JubesX.Statup("Love", 90, -2)
                                $ JubesX.Statup("Obed", 90, 10)
                                $ JubesX.Statup("Inbt", 90, -2)
                                $ JubesX.FaceChange("startled",2)
                                ch_v "Извини! Извини!"
                                $ JubesX.FaceChange("startled",1)
                                ch_v "Позволь мне объясниться!"
                    $ JubesX.FaceChange("sadside",1)
                    ch_v "Так вот. . . я. . . вампир?"
                    $ JubesX.AddWord(1,"vamp",0,0,0) #adds "word" tag to Recent
                    menu:
                        extend ""
                        "Я тебе не киоск с закусками!":
                                $ JubesX.Statup("Love", 90, 1)
                                $ JubesX.Statup("Obed", 90, 3)
                                $ JubesX.Statup("Inbt", 90, 1)
                                $ JubesX.FaceChange("sly",1)
                                ch_v "Это ты так думаешь."
                        "Вампир. . ?":
                                ch_v ". . . Ага. . ."
                        "Ага. Вот ты и попалась.":
                                $ JubesX.Statup("Love", 90, 2)
                                $ JubesX.Statup("Obed", 90, 2)
                                $ JubesX.Statup("Inbt", 90, -1)
                                $ JubesX.FaceChange("perplexed",1)
                                ch_v "Наверное, нам стоит отвести тебя в медблок. . ."
                    $ Count += 1

            #loops back into menu

        # End while loop

        if "Jubilee" not in JubesX.Names:
                $ JubesX.Statup("Love", 90, -5)
                $ JubesX.Statup("Obed", 90, 10)
                $ JubesX.FaceChange("angry",1)
                ch_v "Серьезно? Ты даже не хочешь узнать мое гребаное имя?"
                $ JubesX.FaceChange("sadside",1,Brows="angry")
                ch_v "Как много девушек прошло через тебя?"
                ch_v ". . ."
                $ JubesX.FaceChange("angry",1)
                ch_v "Я \"Джубили,\" между прочим."
                menu:
                    extend ""
                    "Что? Юбилей?":
                            $ JubesX.Statup("Obed", 90, 1)
                            $ JubesX.Statup("Inbt", 90, 1)
                            ch_v "Меня -зовут- Джубили, тупица."
                    "Так тебя зовут? Ладно.":
                            $ JubesX.Statup("Love", 90, 3)
                            $ JubesX.Statup("Obed", 90, 5)
                            $ JubesX.Statup("Inbt", 90, 15)
                            $ JubesX.FaceChange("smile",1)
                            ch_v "You catch on quick. . ."
                    "Ага, я тоже немного \"джуби\".":
                            $ JubesX.FaceChange("confused",1)
                            ch_v "Что-. . . О."
                            $ JubesX.Statup("Love", 90, 10)
                            $ JubesX.Statup("Obed", 90, 5)
                            $ JubesX.Statup("Inbt", 90, 15)
                            $ JubesX.FaceChange("smile",1)
                            ch_v "Хах."
                            ch_v "Хорошо, это было круто. Но я имела в виду, что меня -зовут- Джубили."
                            ch_v "На самом деле, мое полное имя \"Джубилейшен Ли\". . ."
                $ JubesX.Name = "Джубили"
                $ JubesX.Petname_rod = "Джубили"
                $ JubesX.Petname_dat = "Джубили"
                $ JubesX.Petname_vin = "Джубили"
                $ JubesX.Petname_tvo = "Джубили"
                $ JubesX.Petname_pre = "Джубили"
                $ JubesX.Names.append("Jubilation")
                $ JubesX.Names.append("Miss Lee")
                $ JubesX.Pets.append("Miss Lee")
                ch_v "И я знаю, что тебя зовут [Player.Name]."
        if "devamp" not in JubesX.RecentActions:
                $ JubesX.FaceChange("sadside",1)
                ch_v "В общем, я просто подумала, что, возможно, твоя кровь поможет мне избавиться от моей \"вампирской\" сущности."
        menu:
            extend ""
            "Ну и? Чувствуешь себя иначе?":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("smile",1)
            ". . .":
                $ JubesX.Statup("Love", 90, -2)
                $ JubesX.Statup("Obed", 90, 2)
                $ JubesX.FaceChange("perplexed",1)
                ch_v "Ты даже не хочешь спросить, чувствую ли я изменения?"
                menu:
                    extend ""
                    "А, да, как ты себя чувствуешь?":
                            $ JubesX.Statup("Love", 90, 1)
                            $ JubesX.Statup("Inbt", 90, 1)
                            $ JubesX.FaceChange("smile",1)
                    "Не, не особо.":
                            $ JubesX.Statup("Love", 90, -3)
                            $ JubesX.Statup("Obed", 90, 3)
                            $ JubesX.FaceChange("angry",1)
                            ch_v "Н-да, плохое начало!"
                    "Ох. . . ладно, говори.":
                            $ JubesX.FaceChange("confused",1)
                            ch_v ". . ."

        ch_v "Похоже. . . особо изменений нет."
        ch_v "Все еще остались зубы. . . жажда."
        $ JubesX.FaceChange("sadside",1)
        ch_v "Думаю, я все еще вампир."
        $ JubesX.FaceChange("normal",1)
        ch_v "Но я чувствую себя немного лучше. . ."
        $ JubesX.FaceChange("sad",1)
        ch_v "Прости, мне не стоило так накидываться на тебя."
        ch_v "Это не хорошо, я знаю."
        menu:
            extend ""
            "Все в порядке, я понимаю.":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Obed", 90, -1)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Спасибо."
                    ch_v "Могу ли я как-то загладить свою вину?"
            "Почему бы тебе не загладить свою вину?":
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.FaceChange("sexy",1)
                    ch_v "А?"
            "Как ты посмела!":
                    $ JubesX.Statup("Obed", 90, 3)
                    $ JubesX.Statup("Inbt", 90, -1)
                    $ JubesX.FaceChange("surprised",1)
                    ch_v "Я знаю, знаю!"
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Я могу загладить свою вину!"
            ". . .":
                    $ JubesX.Statup("Inbt", 90, 3)
                    $ JubesX.FaceChange("sly",1)
                    ch_v "Так вот. . . я, наверное, могла бы как-то загладить свою вину?"
        menu:
            extend ""
            "В этом нет необходимости.":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Inbt", 90, 1)
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Это очень мило с твоей стороны."
                    ch_v "А если серьезно, я что-нибудь придумаю. . ."
            "Может, поцелуешь меня?":
                    $ JubesX.Statup("Love", 90, 3)
                    $ JubesX.Statup("Obed", 90, 3)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("sly",1)
                    ch_v "Я слышала, что ты очаровашка."
                    ch_v "Нууу, если только. . . разок. . ."
                    $ JubesX.FaceChange("kiss")
                    show Jubes_Sprite:
                        ease 0.5 offset (0,0) zoom 2
                    pause 1
                    show Jubes_Sprite:
                        ease 0.5 offset (100,0) zoom 1.5
                    $ JubesX.FaceChange("sly",1)
                    ch_v ". . ."
            "Может, покажешь сисечки?":
                    $ JubesX.Statup("Obed", 90, 3)
                    if ApprovalCheck(JubesX, 620):
                            $ JubesX.Statup("Love", 90, 2)
                            $ JubesX.Statup("Inbt", 90, 1)
                            $ JubesX.FaceChange("sly",1)
                            ch_v "Думаю, я могла бы, но. . ."
                            $ JubesX.FaceChange("smile",1,Mouth="sucking")
                    else:
                            $ JubesX.Statup("Love", 90, -2)
                            $ JubesX.Statup("Obed", 90, 1)
                            $ JubesX.FaceChange("angry",1,Mouth="sucking")
                    $ JubesX.ArmPose = 1
                    show Fireworks onlayer black as Fire1:
                            pos (JubesX.SpriteLoc+250,350)
                    show Fireworks onlayer black as Fire2:
                            pos (JubesX.SpriteLoc+250,350)
                    ch_v "Это вряд ли."
                    $ JubesX.FaceChange("smile",1)
                    menu:
                        extend ""
                        ". . .":
                            pass
                        "Ха!":
                            $ JubesX.Statup("Love", 90, 2)
                            $ JubesX.Statup("Inbt", 90, 1)
                        "Нет. . . Я серьезно.":
                            $ JubesX.Statup("Love", 90, -2)
                            $ JubesX.Statup("Obed", 90, 2)
                            $ JubesX.FaceChange("angry",1)
                            ch_v "Ага, как и я."
                    call expression JubesX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

            "Может, отлижешь мне?" if not Player.Male:
                    if ApprovalCheck(JubesX, 620):
                            $ JubesX.Statup("Love", 90, 1)
                            $ JubesX.Statup("Obed", 90, 5)
                            $ JubesX.Statup("Inbt", 90, 1)
                            $ JubesX.FaceChange("smile",1,Mouth="sucking")
                    else:
                            $ JubesX.Statup("Love", 90, -5)
                            $ JubesX.Statup("Obed", 90, 2)
                            $ JubesX.FaceChange("angry",1,Mouth="sucking")

                    ch_v "Послушай, может я и сосу больше, чем остальные, но даже я не настолько доступна!"
                    $ JubesX.FaceChange("smile",1)
                    call expression JubesX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

            "Может, отсосешь мне?" if Player.Male:
                    if ApprovalCheck(JubesX, 620):
                            $ JubesX.Statup("Love", 90, 1)
                            $ JubesX.Statup("Obed", 90, 5)
                            $ JubesX.Statup("Inbt", 90, 1)
                            $ JubesX.FaceChange("smile",1,Mouth="sucking")
                    else:
                            $ JubesX.Statup("Love", 90, -5)
                            $ JubesX.Statup("Obed", 90, 2)
                            $ JubesX.FaceChange("angry",1,Mouth="sucking")

                    ch_v "Послушай, может я и сосу больше, чем остальные, но даже я не настолько доступна!"
                    $ JubesX.FaceChange("smile",1)
                    call expression JubesX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

        ch_v "В общем, мне нужно идти, пока не наступил рассвет."
        ch_v "Может, как-нибудь еще увидимся."
        ch_v "В свете луны. . ."
#        $ JubesX.AddWord(1,0,0,0,"bit") #adds "word" tag to History
        $ JubesX.AddWord(1,0,0,0,"met") #adds "word" tag to History
        $ ActiveGirls.append(JubesX) if JubesX not in ActiveGirls else ActiveGirls
        hide Jubes_Sprite with easeoutright
        call Remove_Girl(JubesX)
        "[JubesX.Name] покидает комнату, вы, наконец-то, можете немного поспать. . ."
        return

#End Jubes_Meet / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Jubes_Sunshock / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_Sunshine:
        #called from EventCalls if "sunshine" not in JubesX.History and "traveling" in Player.RecentActions and bg_current in ("bg classroom","bg campus"):
        call Shift_Focus(JubesX)
        $ bg_current = "bg campus"
        $ JubesX.Loc = "bg campus"
        call CleartheRoom(JubesX,0,1)
        call AltClothes(JubesX,1)
        call Set_The_Scene
        $ JubesX.FaceChange("smile")
        "Проходя через площадь, вы видите фигуру, несущуюся к вам."
        call Punch
        "[JubesX.Name] врезается в вас."
        $ JubesX.FaceChange("smile",1,Mouth="sucking")
        ch_v "Привет, [Player.Name]!"
        $ JubesX.FaceChange("smile",1)
        ch_v "Смотри!"
        menu:
            extend ""
            "О, привет. . .":
                    $ JubesX.Statup("Love", 90, 2)
                    $ JubesX.FaceChange("smile",1,Mouth="sucking")
                    ch_v "Да-да, \"привет,\" но смотри, я -на улице!-"
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Днем!"
            "Ты на улице днем!":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Inbt", 90, 2)
            "На что смотреть?":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Видишь?!"
                    ch_v "Я -на улице!-"
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("smile",1,Mouth="sucking")
                    ch_v "-Днем!-"
                    $ JubesX.FaceChange("smile")
            "Какого черта?":
                    $ JubesX.Statup("Love", 90, -3)
                    $ JubesX.Statup("Obed", 90, 5)
                    $ JubesX.FaceChange("surprised",2,Mouth="sucking")
                    ch_v "Извини! Просто я очень рада!"
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Я на улице, днем!"
        menu:
            extend ""
            "Отличные новости!":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    $ JubesX.FaceChange("surprised",1,Mouth="sucking")
                    ch_v "Правда?!"
                    $ JubesX.FaceChange("smile",1)
            "И что? Я тоже.":
                    $ JubesX.Statup("Love", 90, -5)
                    $ JubesX.Statup("Obed", 90, 5)
                    $ JubesX.FaceChange("confused",1)
                    ch_v "Да. . ."
                    if not Player.Male:
                        ch_v "Но я -вампир-, не забыла?"
                    else:
                        ch_v "Но я -вампир-, не забыл?"
            "Ну и ладно.":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("confused",1)
                    ch_v ". . . но я же -вампир?-"
        $ JubesX.FaceChange("surprised",1,Mouth="sucking")
        ch_v "Раньше я не могла этого сделать, не загоревшись!"
        $ JubesX.FaceChange("smile",1)
        menu:
            extend ""
            "Ты знаешь почему?":
                    $ JubesX.Statup("Love", 90, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
            "Ну, для меня это никогда не было проблемой.":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 90, 3)
                    $ JubesX.FaceChange("confused",1)
                    ch_v ". . ."
                    ch_v "Я знаю. . ."
                    $ JubesX.FaceChange("normal",1)
            "Классно.":
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    $ JubesX.FaceChange("confused",1)
                    ch_v ". . ."
                    $ JubesX.FaceChange("normal",1)
            "Ладно.":
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("angry",1)
                    ch_v ". . ."
                    $ JubesX.FaceChange("normal",1)
        ch_v "Я не знаю, чем это вызвано, но думаю, это связано с твоей кровью. . ."
        $ JubesX.FaceChange("smile",1)
        ch_v "В любом случае, я просто хотела сказать тебе \"спасибо,\" это так здорово!"
        $ JubesX.AddWord(1,0,0,0,"sunshine") #adds "word" tag to History
        hide Jubes_Sprite with easeoutright
        call Remove_Girl(JubesX)
        "[JubesX.Name] убегает, а вы продолжаете свой путь. . ."
        return

#End Jubes_Sunshine / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Jubes_Sunshock / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_Entry_Check:
        #checks to see if she is trying to follow you and if she will.
        if JubesX not in Party:
                return
        call Jubes_Sunshock #checks to see if she has to stay
        if _return:
                #if she couldn't go with you
                menu:
                    "Хорошо, тогда мы можем остаться здесь.":
                            if "stayed" in JubesX.RecentActions:
                                    # you stay, but not for the first time recently
                                    $ JubesX.Statup("Love", 80, -2)
                                    ch_v "Теперь мне кажется, что ты просто издеваешься надо мной. . ."
                            elif ApprovalCheck(JubesX, 1300) or ApprovalCheck(JubesX, 400, "O"):
                                ch_v "В этом нет необходимости, не буду тебя задерживать."
                                menu:
                                    extend ""
                                    "Я настаиваю.":
                                        # you stay
                                        $ JubesX.FaceChange("smile",1)
                                        $ JubesX.Statup("Love", 80, 2)
                                        $ JubesX.Statup("Inbt", 60, 2)
                                        ch_v "Оу, спасибо. Это очень мило с твоей стороны."
                                    "Хорошо, извини.":
                                        # you go
                                        $ JubesX.Statup("Obed", 90, 2)
                                        $ JubesX.FaceChange("sad",1)
                                        $ Party.remove(JubesX)
                                        "Вы оставляеете ее."
                                        return
                                    "Круто, тогда увидимся позже.":
                                        # you go
                                        $ JubesX.Statup("Love", 80, -2)
                                        $ JubesX.Statup("Obed", 90, 2)
                                        $ JubesX.FaceChange("sad",1)
                                        $ Party.remove(JubesX)
                                        "Вы оставляеете ее."
                                        return
                            else:
                                        # you stay
                                        ch_v "Спасибо, это очень мило с твоей стороны."
                            $ JubesX.AddWord(1,"stayed",0,0,0) #adds "word" tag to recent
                            jump Misplaced
                    "Ох, жаль, тогда можешь остаться здесь.":
                            # you go
                            $ Party.remove(JubesX)
                            $ JubesX.Statup("Love", 80, -2)
                            $ JubesX.Statup("Obed", 70, 2)
                            if ApprovalCheck(JubesX, 1300) or ApprovalCheck(JubesX, 400, "O"):
                                    $ JubesX.Statup("Obed", 90, 2)
                                    $ JubesX.FaceChange("sad",1)
                                    ch_v "Я понимаю, увидимся позже. . ."
                            else:
                                    $ JubesX.Statup("Love", 80, -4)
                                    $ JubesX.FaceChange("angry",1,Mouth="sucking")
                            "Вы оставляеете ее."
                            $ JubesX.FaceChange("sad",1)
        return


label Jubes_Sunshock:
        #this is called when Jubilee is asked to go out in the sublight with higher than 50% addiction
        #returns 1 if she doesn't go along with it.

        if JubesX.Addict <= 50 or Time_Count > 2:
                #if below the threshold or it's night time, ignore this
                return 0
        $ JubesX.FaceChange("sad",1)
        if "sunshock" in JubesX.RecentActions:
                ch_v "Как я уже говорила, я не готова выйти на солнце."
                return 1
        $ JubesX.AddWord(1,"sunshock",0,0,0) #adds "word" tag to recent
        ch_v "О, подожди-ка, у меня сейчас \"заряд на нуле\", так что я совсем не хочу выходить на солнце."
        menu:
            extend ""
            "Ох, извини, все в порядке.":
                    $ JubesX.Statup("Love", 90, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Спасибо за понимание. . ."
                    return 1

            "Я всегда могу. . . прийти к тебе сам." if bg_current != JubesX.Loc and JubesX not in Party and not Player.Male:
                    #if she's not local. . .
                    ch_v "О, это было бы здорово. Тогда до встречи."
                    return 1

            "Я всегда могу. . . прийти к тебе сама." if bg_current != JubesX.Loc and JubesX not in Party and Player.Male:
                    #if she's not local. . .
                    ch_v "О, это было бы здорово. Тогда до встречи."
                    return 1

            "Я всегда могу. . . подзарядить тебя." if bg_current == JubesX.Loc or JubesX in Party:
                    # only works if she is local to you
                    $ JubesX.Statup("Love", 80, 1)
                    $ JubesX.FaceChange("confused",1)
                    ch_v "А? Ты хочешь чего-то конкретного?"
                    menu:
                        extend ""
                        "Нет, можешь касаться меня так, как тебе хочется.":
                            if JubesX.Petname in ("хозяин", "господин", "хозяйка", "госпожа"):
                                    $ JubesX.Statup("Lust", 80, 3)
                                    $ JubesX.Statup("Love", 70, 1)
                                    $ JubesX.Statup("Love", 95, 1)
                                    $ JubesX.FaceChange("sexy")
                                    ch_v "Тогда, пожалуй, я выбираю. . ."
                                    "Она наклоняется, чтобы поцеловать вас."
                                    call KissPrep
                            elif ApprovalCheck(JubesX, 650, "LI"):
                                    $ JubesX.Statup("Lust", 80, 3)
                                    $ JubesX.Statup("Love", 80, 5)
                                    $ JubesX.FaceChange("sexy")
                                    ch_v "О! Тогда как насчет того, чтобы я просто попробовала простенькое прикосновение. . ."
                                    "Она наклоняется, чтобы поцеловать вас."
                                    call KissPrep
                            else:
                                    $ JubesX.Statup("Lust", 80, 3)
                                    $ JubesX.Statup("Love", 80, 6)
                                    $ JubesX.FaceChange("smile")
                                    call Girl_Tag(JubesX)
                            while JubesX.Addict > 20 and Round > 10:
                                    #should remove addiction by 1 unit per round until either it stabilizes or time runs out.
                                    $ JubesX.Addict -= 1
                                    $ Round -= 1
                                    if Round == 10:
                                            call AnyLine(JubesX,"Думаю, у нас нет времени на что-то большее.")
                        #end "Nothing, just touch whatever you like.":

                        "Как насчет поцелуя?":
                                if JubesX.Kissed or ApprovalCheck(JubesX, 600, "LI") or JubesX.Petname in ("хозяин", "господин", "хозяйка", "госпожа"):
                                        $ JubesX.Forced = 0
                                        $ JubesX.Statup("Lust", 80, 3)
                                        $ JubesX.Statup("Love", 80, 6)
                                        $ JubesX.FaceChange("sexy")
                                        if not Player.Male:
                                            ch_v "Ты меня убедила. . ."
                                        else:
                                            ch_v "Ты меня убедил. . ."
                                        "Она наклоняется, чтобы поцеловать вас."
                                        call KissPrep
                                        $ JubesX.Addict = 20 if JubesX.Addict > 20 else JubesX.Addict
                                else:
                                        if not Player.Male:
                                            ch_v "Ты мне не нравишься такой. . ."
                                        else:
                                            ch_v "Ты мне не нравишься таким. . ."

                        "Могу я тебя потрогать?":
                                ch_v "Ох, я даже не знаю. . ."
                                call expression JubesX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                                menu:
                                    extend ""
                                    "Позволишь мне потрогать твою грудь?":
                                            $ CountStore = Tempmod
                                            call Top_Off(JubesX,2)
                                            $ Tempmod = CountStore
                                            call Girl_Fondle_Breasts
                                            if "fondle breasts" in JubesX.RecentActions:
                                                    $ JubesX.Statup("Obed", 80, 10)
                                                    $ JubesX.Statup("Inbt", 80, 10)
                                                    ch_v "Значит, равноценный обмен?"

                                    "Позволишь мне потрогать твои бедра?":
                                            $ CountStore = Tempmod
                                            call Bottoms_Off(JubesX,2)
                                            $ Tempmod = CountStore
                                            if JubesX.PantsNum() > 6 or JubesX.HoseNum() >= 5:
                                                    ch_v "Ну, посмотрим. . ."
                                            call Girl_Fondle_Thighs
                                            if "fondle thighs" in JubesX.RecentActions:
                                                    $ JubesX.Statup("Obed", 50, 5)
                                                    $ JubesX.Statup("Inbt", 50, 5)
                                                    ch_v "Значит, равноценный обмен?"
                                                    if JubesX.PantsNum() > 6 or JubesX.HoseNum() >= 5:
                                                            call Girl_Tag(JubesX)

                                    "Позволишь мне потрогать твою киску?":
                                            $ CountStore = Tempmod
                                            call Bottoms_Off(JubesX,0)
                                            $ Tempmod = CountStore
                                            call Girl_Fondle_Pussy
                                            if "fondle pussy" in JubesX.RecentActions:
                                                    $ JubesX.Statup("Obed", 50, 10)
                                                    $ JubesX.Statup("Obed", 80, 5)
                                                    $ JubesX.Statup("Inbt", 50, 10)
                                                    $ JubesX.Statup("Inbt", 80, 5)
                                                    ch_v "Этого ведь будет достаточно, да?"

                                    "Неважно":
                                            $ JubesX.Statup("Love", 90, -3)
                                            $ JubesX.Statup("Obed", 70, 1)
                                            $ JubesX.Statup("Obed", 90, 2)
                                            $ JubesX.FaceChange("angry",1)
                        "А, неважно.":
                                $ JubesX.Statup("Love", 70, -2)
                                $ JubesX.Statup("Love", 90, -2)
                                $ JubesX.Statup("Obed", 70, 1)
                                $ JubesX.Statup("Obed", 90, 2)
                                $ JubesX.FaceChange("angry",1)

                        #end Sunshock treatment menu

                    if JubesX.Addict >= 70:
                            $ JubesX.Statup("Inbt", 70, 1)
                            $ JubesX.Statup("Inbt", 80, 1)
                            ch_v "Могу я просто быстренько коснуться тебя?"
                            menu:
                                extend ""
                                "Конечно.":
                                        $ JubesX.Statup("Lust", 80, 3)
                                        $ JubesX.Statup("Love", 80, 6)
                                        $ JubesX.FaceChange("smile")
                                        call Girl_Tag(JubesX)
                                "Не-а, извини.":
                                        $ JubesX.Statup("Love", 80, -3)
                                        $ JubesX.Statup("Obed", 70, 2)
                                        if ApprovalCheck(JubesX, 1300) or ApprovalCheck(JubesX, 400, "O"):
                                                $ JubesX.FaceChange("sad",1)
                                                ch_v "Ох."
                                        else:
                                                $ JubesX.Statup("Love", 90, -2)
                                                $ JubesX.Statup("Obed", 90, 2)
                                                $ JubesX.FaceChange("angry",1)
                                                if not Player.Male:
                                                    ch_v "Вот ты дура."
                                                else:
                                                    ch_v "Вот ты придурок."

                    if JubesX.Addict >= 70:
                            #this is too high, she will refuse outright.
                            if ApprovalCheck(JubesX, 1300) or ApprovalCheck(JubesX, 400, "O"):
                                    $ JubesX.FaceChange("sad",1)
                                    ch_v "Прости, я не могу, для меня это будет подобно пытке."
                            else:
                                    $ JubesX.FaceChange("angry",1)
                                    ch_v "Ты, должно быть, шутишь! Я же сгорю!"
                            return 1
                    elif ApprovalCheck(JubesX, 1600) or ApprovalCheck(JubesX, 500, "O"):
                            $ JubesX.Statup("Obed", 90, 2)
                            $ JubesX.Statup("Inbt", 80, 2)
                            ch_v "Думаю, если недолго, я справлюсь. . ."
                    else:
                            ch_v "Повзрослей. . ."
                            return 1
            #end "I could always. . . top you off?":

            "Да ладно, не будь такой.":
                    $ JubesX.Statup("Love", 70, -2)
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.FaceChange("sad",1)
                    if JubesX.Addict >= 70:
                            #this is too high, she will refuse outright.
                            if ApprovalCheck(JubesX, 1300) or ApprovalCheck(JubesX, 400, "O"):
                                    $ JubesX.Statup("Obed", 90, 2)
                                    ch_v "Прости, я не могу, для меня это будет подобно пытке."
                            else:
                                    $ JubesX.FaceChange("angry",1)
                                    ch_v "Ты, должно быть, шутишь! Я же сгорю!"
                            return 1
                    elif ApprovalCheck(JubesX, 1600) or ApprovalCheck(JubesX, 500, "O"):
                            $ JubesX.Statup("Obed", 90, 2)
                            $ JubesX.Statup("Inbt", 80, 2)
                            ch_v "Думаю, если недолго, я справлюсь. . ."
                    else:
                            ch_v "Повзрослей. . ."
                            return 1
        return 0


#End Jubes_Sunshock / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Jubes_Mall / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jubes_Mall(BO=[]):
        #this is called to introduce the mall element

        call Shift_Focus(JubesX)
        call Set_The_Scene
        if JubesX.Loc == bg_current:
                "[JubesX.Name] внезапно замирает, затем поворачивается к вам."
        else:
                $ JubesX.Loc = bg_current
                "[JubesX.Name] врывается в комнату."
        call CleartheRoom(JubesX,0,0) #she asks
        call Set_The_Scene
        $ Player.AddWord(1,0,0,0,"mall") #history

        $ JubesX.FaceChange("surprised",1,Mouth="sucking")
        ch_v "Слушай, я только что кое-что поняла!"
        $ JubesX.FaceChange("smile")
        menu:
            extend ""
            "Круто.":
                    $ JubesX.Statup("Love", 80, 1)
            "О, и что?":
                    $ JubesX.Statup("Love", 90, 2)
                    $ JubesX.Statup("Inbt", 60, 1)
            "Угу-м.":
                    $ JubesX.Statup("Love", 80, -1)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Obed", 60,1)
                    $ JubesX.Statup("Inbt", 50, -1)
                    $ JubesX.FaceChange("angry",1,Mouth="sucking")
                    ch_v "Это серьезно!"
            ". . .":
                $ JubesX.Statup("Love", 90, -1)
                $ JubesX.FaceChange("confused")
                ch_v "И даже не спросишь меня \"что?\""
                menu:
                    extend ""
                    "О, конечно, что ты поняла?":
                            $ JubesX.Statup("Love", 90, 2)
                            $ JubesX.Statup("Obed", 50, 1)
                            $ JubesX.Statup("Inbt", 50, 1)
                    "Нет.":
                            $ JubesX.Statup("Love", 80, -2)
                            $ JubesX.Statup("Obed", 70, 2)
                            $ JubesX.Statup("Inbt", 30, -1)
                            $ JubesX.FaceChange("angry")
                            if not Player.Male:
                                ch_v "Вот ты сучка."
                            else:
                                ch_v "Ну ты и говнюк."
                    ". . .":
                            $ JubesX.Statup("Love", 90, -1)
                            $ JubesX.Statup("Obed", 60, 1)
                            ch_v "Лааааадно. . ."
        $ JubesX.FaceChange("surprised",1,Mouth="sucking")
        ch_v "Теперь, когда мне можно выходить на улицу днем, я вновь могу ходить в торговый центр!"
        menu:
            extend ""
            "Отлично!":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    ch_v "Я знаю."
                    menu:
                        extend ""
                        "Подожди-ка, здесь есть торговый центр?":
                                $ JubesX.Statup("Love", 80, 1)
                                $ JubesX.Statup("Inbt", 70, 1)
                                $ JubesX.FaceChange("confused")
                                ch_v "Конечно! В каком городе нет торгового центра?!"
                        "Хочешь туда сходить?":
                                $ JubesX.Statup("Love", 80, 2)
                                $ JubesX.Statup("Love", 90, 1)
                                $ JubesX.Statup("Inbt", 70, 1)
            "Ну ладно.":
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.FaceChange("sad")
            "Подожди-ка, здесь есть торговый центр?":
                    $ JubesX.Statup("Love", 80, 1)
                    $ JubesX.Statup("Inbt", 70, 1)
                    $ JubesX.FaceChange("confused")
                    ch_v "Конечно! В каком городе нет торгового центра?!"
            "Ладно, мне все равно.":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Inbt", 50, -1)
        $ JubesX.FaceChange("surprised",1,Mouth="sucking")
        ch_v "Мы должны сходить туда прямо сейчас!"
        $ JubesX.FaceChange("smile")
        $ Party = [JubesX]
        menu:
            "Хорошо, давай сходим.":
                    $ JubesX.Statup("Love", 80, 2)
                    $ JubesX.Statup("Love", 90, 1)
                    $ JubesX.Statup("Inbt", 60, 1)
                    show blackscreen onlayer black with dissolve
                    if not Player.Male:
                        "Вы обе выходите из комнаты."
                    else:
                        "Вы оба выходите из комнаты."
            "Можешь идти, мне там ничего не нужно.":
                    $ JubesX.Statup("Love", 80, 2)
                    $ JubesX.Statup("Obed", 60, 1)
                    $ JubesX.Statup("Obed", 80, 1)
                    if not Player.Male:
                            ch_v "Давай, ты должна пойти!"
                    else:
                            ch_v "Давай, ты должен пойти!"
                    ch_v "Ты не знаешь, от чего отказываешься!"
                    show blackscreen onlayer black with dissolve
                    "[JubesX.Name] может быть удивительно сильной. . ."
            "Не.":
                    $ JubesX.Statup("Love", 50, -2)
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Inbt", 50, 2)
                    $ JubesX.Statup("Inbt", 60, 2)
                    $ JubesX.FaceChange("angry",1,Mouth="sucking")
                    ch_v "Соберись и пошли!"
                    $ JubesX.FaceChange("smile")
                    show blackscreen onlayer black with dissolve
                    "[JubesX.Name] может быть удивительно сильной. . ."
            "Вообще-то, я планировала-" if not Player.Male:
                    $ JubesX.Statup("Love", 50, -1)
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Inbt", 50, 1)
                    $ JubesX.Statup("Inbt", 60, 1)
                    $ JubesX.FaceChange("surprised",1,Mouth="sucking")
                    ch_v "У нас мало времени! Пошли!"
                    $ JubesX.FaceChange("smile")
                    show blackscreen onlayer black with dissolve
                    "[JubesX.Name] может быть удивительно сильной. . ."
            "Вообще-то, я планировал-" if Player.Male:
                    $ JubesX.Statup("Love", 50, -1)
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Inbt", 50, 1)
                    $ JubesX.Statup("Inbt", 60, 1)
                    $ JubesX.FaceChange("surprised",1,Mouth="sucking")
                    ch_v "У нас мало времени! Пошли!"
                    $ JubesX.FaceChange("smile")
                    show blackscreen onlayer black with dissolve
                    "[JubesX.Name] может быть удивительно сильной. . ."
        "Вы добираетесь до пригородного торгового комплекса средних размеров, часто именуемого \"торговым центром.\""

        $ bg_current = "bg mall"
        $ JubesX.Loc = bg_current
        call CleartheRoom(JubesX,0,1) #it's silent
        call Set_The_Scene

        $ JubesX.FaceChange("smile")
        ch_v "Добро пожаловать в Salem Centre Mall!"
        ch_v "Он открыт от рассвета до заката, вот почему я какое-то время не могла сюда приходить. . ."
        ch_v "Здесь тонна различных магазинчиков, хотя, я думаю, что далеко не все из них будут тебе интересны."
        $ Line = 0
        $ BO = TotalGirls[:]
        while BO and not Line:
                if BO[0].Date:
                        $ Line = 1
                $ BO.remove(BO[0])
        if Line:
                #if you've been on dates
                "Вы понимаете, что местный кинотеатр находится в одном конце торгового центра."
                "А ресторан, который вы часто посещаете, в другом конце."
                "Как вы раньше не замечали, что между ними торговый центр? . ."
                menu:
                    "Избирательная амнезия":
                            "А, да, наверное."
                    "Я не очень умный":
                            "Что есть, то есть."
                    "Это все реткон":
                            "Такое бывает."
        else:
                #if you haven't been on dates
                "Вы отмечаете, что кинотеатр находится в одном конце торгового центра, а красивый ресторанчик в другом."
                "Возможно, вам стоит сводить кого-нибудь в эти места. . ."
        if not Player.Male:
            ch_v "И ты раньше не бывала здесь?"
        else:
            ch_v "И ты раньше не бывал здесь?"
        menu:
            extend ""
            "Видимо, нет.":
                    pass
            "Думаю, я часто была близка к этому. . ." if not Player.Male:
                    pass
            "Думаю, я часто был близок к этому. . ." if Player.Male:
                    pass
            "Не-а.":
                    $ JubesX.Statup("Love", 70, -1)
        $ JubesX.FaceChange("confused",1)
        ch_v "Странно."
        ch_v "Кстати, в детстве я проводила -кучу- времени в торговом центре."
        $ JubesX.FaceChange("sadside")
        ch_v "Я сбежала из приемной семьи и ночевала в закрытых магазинах. . ."
        ch_v "Лучше так, чем на улице."
        menu:
            extend ""
            "Жестко.":
                    $ JubesX.Statup("Love", 80, 3)
                    $ JubesX.Statup("Love", 90, 1)
                    $ JubesX.Statup("Obed", 50, 1)
            "Должно быть, это было тяжело для тебя.":
                    $ JubesX.Statup("Love", 60, 5)
                    $ JubesX.Statup("Love", 80, 3)
                    $ JubesX.Statup("Love", 90, 1)
            "Пожалуй.":
                    $ JubesX.Statup("Love", 70, -1)
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Inbt", 50, 1)
                    $ JubesX.FaceChange("confused",1)
                    ch_v ". . ."
            "Зато была бесплатная еда, да?":
                    $ JubesX.Statup("Love", 70, 1)
                    $ JubesX.Statup("Inbt", 60, 1)
                    $ JubesX.FaceChange("smile",1,Eyes="side")
                    ch_v "Да, когда у меня получалось попасть в ресторан . ."
                    $ JubesX.Statup("Love", 70, -2)
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Obed", 80, 1)
                    $ JubesX.FaceChange("angry",1)
                    ch_v ". . ."

        ch_v "Да, но это было нормально. . ."
        $ JubesX.FaceChange("smile",Eyes="side")
        ch_v "В общем, потом я наткнулась на нескольких студентов Ксавье и нашла путь в институт."
        $ JubesX.FaceChange("smile")
        ch_v "Ксавье согласился взять меня, и все стало гораздо лучше."
        $ JubesX.FaceChange("sadside")
        ch_v "Ну, насколько это возможно с моим \"вампиризмом\"."
        menu:
            "Понятно. . .":
                    $ JubesX.Statup("Obed", 30, 1)
                    $ JubesX.Statup("Obed", 60, 1)
            "Теперь все будет еще лучше.":
                    $ JubesX.Statup("Love", 80, 2)
            "Угу-м.":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.FaceChange("angry")
                    ch_v ". . ."
        $ JubesX.FaceChange("smile")
        ch_v "Нууу. . . раз уж мы здесь, не хочешь пройтись по магазинам?"
        menu:
            "Конечно, давай осмотримся.":
                    $ JubesX.Statup("Love", 60, 5)
                    $ JubesX.Statup("Love", 80, 3)
                    $ JubesX.Statup("Love", 90, 1)
                    $ JubesX.Statup("Inbt", 50, 1)
                    ch_v "Клево."
                    call Shopping_Mall
            "Нет, нам пора возвращаться.":
                    $ JubesX.Statup("Love", 60, -3)
                    $ JubesX.Statup("Love", 80, -2)
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    $ JubesX.FaceChange("sad")
                    ch_v "Оу, ладно. По крайней мере, теперь я могу приходить сюда, когда захочу. . ."
                    $ JubesX.Statup("Obed", 50, 3)
                    $ JubesX.Statup("Obed", 90, 2)

        if not Player.Male:
            "Вы обе возвращаетесь обратно в кампус."
        else:
            "Вы оба возвращаетесь обратно в кампус."
        $ bg_current = "bg campus"
        $ JubesX.Loc = bg_current
        call CleartheRoom(JubesX,0,1) #it's silent
        call Set_The_Scene
        ch_v "Ладно, было приятно пообщаться с тобой."
        ch_v "Надеюсь, мы сможем как-нибудь повторить!"
        jump Misplaced
        return

#End Jubes_Mall / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_Key:
        call Shift_Focus(JubesX)
        $ JubesX.Loc = bg_current
        call Set_The_Scene
        $ JubesX.FaceChange("bemused")
        $ Event_Queue = [0,0]
        ch_v "О, эм. . ."
        ch_v "Мы уже какое-то время спим вместе и. . ."
        ch_v "Вот."
        "Она берет вас за руку и вручает вам ключ от своей комнаты."
        $ Keys.append(JubesX) if JubesX not in Keys else Keys
        $ JubesX.Event[0] = 1
        ch_p "Спасибо."
        return



# Event Jubes_Caught_Masturbating  /////////////////////////////////////////////////////

#bf
## start Jubes_BF//////////////////////////////////////////////////////////


label Jubes_BF(BO=[]):
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(JubesX,"bemused","краснеет. . .")
                return
        call Shift_Focus(JubesX)
        if JubesX.Loc != bg_current:
            $ JubesX.Loc = bg_current
            if JubesX not in Party:
                "[JubesX.Name] подходит к вам и жестом показывает, что хочет поговорить с вами наедине."
            else:
                "[JubesX.Name] поворачивается к вам и жестом показывает, что хочет поговорить с вами наедине."
        $ JubesX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ Event_Queue = [0,0]
        call Set_The_Scene(0)
        call Display_Girl(JubesX)
        call Taboo_Level
        call CleartheRoom(JubesX)
        $ JubesX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in JubesX.History:
                call expression JubesX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        $ Line = 0
        $ JubesX.FaceChange("smile",1,Eyes="side")
        if "asked boyfriend" not in JubesX.DailyActions:
                ch_v "Слушай, [JubesX.Petname], я тут подумала и решила, что. . ."
        else:
                ch_v "Сперва. . ."
        ch_v "Хочу рассказать тебе о своем прошлом. . ."
        menu:
            extend ""
            "Желаешь рассказать что-то о торговом центре, да?":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.FaceChange("perplexed")
                    ch_v "А? Нет, не о торговом центре."
                    $ JubesX.FaceChange("confused")
                    ch_v "О том, почему я вампир."
            "Желаешь рассказать о вампиризме?":
                    $ JubesX.Statup("Love", 90, 2)
                    $ JubesX.Statup("Love", 200, 1)
                    $ JubesX.FaceChange("sadside")
                    ch_v ". . . ага."
                    $ JubesX.FaceChange("angry",Eyes="side")
                    ch_v "О \"вампиризме.\""
            "Да не надо.":
                    $ JubesX.Statup("Love", 90, -3)
                    $ JubesX.Statup("Obed", 80, 1)
                    $ JubesX.FaceChange("confused")
                    $ JubesX.AddWord(1,"notcurious",0,0,0) #adds "word" tag to Recent
                    ch_v "О, так я тебе совсем не интересна?"
                    ch_v "Ты не хочешь знать, как я стала вампиром?"
            "А?":
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Obed", 80, -1)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.FaceChange("angry")
                    ch_v "Хочу поведать тебе о том, как я стала вампиром."
        menu:
            extend ""
            "Так как ты -стала- вампиром?":
                    $ JubesX.FaceChange("sadside")
                    $ JubesX.Statup("Love", 200, 5)
                    $ JubesX.Statup("Obed", 80, 1)
                    ch_v "Ну. . ."
            "Ты вампир?!":
                    $ JubesX.FaceChange("perplexed")
                    $ JubesX.Statup("Love", 95, -5)
                    $ JubesX.Statup("Inbt", 50, 2)
                    ch_v ". . . да?"
                    $ JubesX.Statup("Inbt", 80, 3)
                    ch_v "Ты уже об этом знаешь."
            "Ты не обязана это рассказывать.":
                    $ JubesX.FaceChange("smile")
                    $ JubesX.Statup("Love", 200, 3)
                    $ JubesX.Statup("Obed", 80, -2)
                    $ JubesX.Statup("Inbt", 80, 2)
                    if "notcurious" not in JubesX.RecentActions:
                            $ JubesX.Statup("Love", 200, 3)
                            $ JubesX.Statup("Obed", 80, 1)
                    if not Player.Male:
                        ch_v "Что ж, я это ценю, но я хочу, чтобы ты знала."
                    else:
                        ch_v "Что ж, я это ценю, но я хочу, чтобы ты знал."
            "Да мне как-то все равно.":
                    $ JubesX.FaceChange("angry")
                    $ JubesX.Statup("Love", 95, -10)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Obed", 80, 1)
                    if not Player.Male:
                        ch_v "Довольно стервозный способ выразить свое отношение."
                    else:
                        ch_v "Довольно мудацкий способ выразить свое отношение."
                    $ JubesX.Statup("Inbt", 50, 2)
                    $ JubesX.Statup("Inbt", 80, 1)
                    if not Player.Male:
                        ch_v "-но ты все равно должна это услышать."
                    else:
                        ch_v "-но ты все равно должен это услышать."
        $ JubesX.FaceChange("sadside")

        show blackscreen onlayer black
        ch_v ". . . это долгая история. . ."
        hide blackscreen onlayer black
        ch_v ". . .  в общем, вот так я и стала вампиром."

        menu:
            extend ""
            "Что это было? Ты только сказала \"это долгая история\" и сразу же \"вот так я и стала вампиром.\"":
                    $ JubesX.FaceChange("smile",2,Brows="sad")
                    $ JubesX.Statup("Love", 200, 3)
                    $ JubesX.Statup("Obed", 80, 2)
                    ch_v "А. . .  и правда. . ."
                    ch_v "Думаю, я пропустила часть с \"историей\", да. . ."
            "Ну, ладно.":
                    ch_v "Да, так что- {w=0.3}{nw}"
                    $ JubesX.FaceChange("angry",2,Eyes="side")
                    $ JubesX.Statup("Inbt", 50, 1)
                    $ JubesX.Statup("Inbt", 80, 1)
                    ch_v "-нет, я должна рассказать тебе больше, извини."
            "Крутая история.":
                    $ JubesX.Statup("Love", 90, -2)
                    ch_v "Ага. . . так что- {w=0.4}{nw}"
                    $ JubesX.FaceChange("angry",2,Eyes="side")
                    $ JubesX.Statup("Inbt", 50, 1)
                    $ JubesX.Statup("Inbt", 80, 1)
                    ch_v "-нет, я должна рассказать тебе больше, извини."
        $ JubesX.FaceChange("smile",1)
        ch_v "Просто для меня это немного болезненно. . ."
        $ JubesX.FaceChange("sadside")
        ch_v "Мне не хочется снова переживать те события. . ."
        ch_v "Итак, все произошло пару лет назад."
        ch_v "Я уже какое-то время находилась у Ксавье и была на задании."
        $ JubesX.FaceChange("angry",Mouth="smirk")
        ch_v "Мы выслеживали вампиров, которые досаждали мутантам."
        $ JubesX.FaceChange("angry",Mouth="smile")
        ch_v "Оказалось, что мои маленькие плазмоиды могут быть довольно эффективны против них."
        ch_v "Пиу-пиу!"
        $ JubesX.FaceChange("angry",Brows="side")
        ch_v "Но, несмотря на это, один из них смог достать меня. . ."
        ch_v "Это был их лидер, Ксарус, сын Дракулы."
        menu:
            extend ""
            "Мне казалось, что сына Дракулы зовут \"Алукард.\"":
                    $ JubesX.AddWord(1,0,0,0,"Alucard") #adds "word" tag to Recent
                    $ JubesX.FaceChange("confused")
                    $ JubesX.Statup("Love", 90, -3)
                    $ JubesX.Statup("Obed", 80, 1)
                    ch_v "Что? Типа \"Дракула\" наоборот?"
                    $ JubesX.FaceChange("confused",Eyes="side")
                    ch_v "Что это за имя такое?"
                    menu:
                        "Ксарус типа лучше?":
                                $ JubesX.FaceChange("surprised")
                                $ JubesX.Statup("Love", 90, -1)
                                $ JubesX.Statup("Obed", 80, 1)
                                ch_v "Да, Ксарус луч-"
                                $ JubesX.FaceChange("angry",Eyes="side")
                                $ JubesX.Statup("Love", 90, 1)
                                ch_v ". . . ладно, Ксарус не лучше."
                                menu:
                                    "Наоборот будет \"Сураск\". Несуразица какая-то.":
                                            $ JubesX.FaceChange("smile")
                                            $ JubesX.Statup("Love", 200, 5)
                                            $ JubesX.Statup("Obed", 50, 2)
                                            $ JubesX.Statup("Obed", 80, 3)
                                            $ JubesX.Statup("Inbt", 80, 1)
                                            ch_v "Ну да. . ."
                                    ". . .":
                                            $ JubesX.Statup("Love", 200, 1)
                                            $ JubesX.Statup("Inbt", 80, 1)
                        "Ладно, это бредовое имя.":
                                $ JubesX.Statup("Love", 200, 1)
                                $ JubesX.Statup("Obed", 80, 1)
                                $ JubesX.Statup("Inbt", 80, 1)
                                $ JubesX.FaceChange("smile")
                        ". . .":
                                $ JubesX.Statup("Inbt", 50, 1)
                                $ JubesX.Statup("Inbt", 80, 1)
                    ch_v "Возможно, у него было два сына, я не знаю. В обшем. . ."
            ". . .":
                    $ JubesX.Statup("Love", 90, 1)
                    $ JubesX.Statup("Inbt", 50, 1)
                    pass
            "Как такое произошло?":
                    $ JubesX.Statup("Love", 200, 3)
                    $ JubesX.Statup("Obed", 80, 1)
                    ch_v "Не знаю, должно быть, я была недостаточно осторожна."
        ch_v "Он смог превратиться в туман и проскользнуть за мою спину."
        $ JubesX.FaceChange("sad",Eyes="leftside")
        ch_v "Он вонзил свои клыки прежде, чем я успела выстрелить."
        $ JubesX.FaceChange("sad",Eyes="closed")
        ch_v "И осушил меня. . ."
        menu:
            "Но сейчас ты в порядке?":
                    $ JubesX.Statup("Love", 200, 1)
                    $ JubesX.Statup("Inbt", 80, 1)
                    ch_v "Типа того. . ."
            "Жестко.":
                    $ JubesX.Statup("Love", 200, 3)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.FaceChange("smile",Brows="sad")
                    ch_v "Ага, спасибо. . ."
            ". . .":
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Inbt", 50, 1)
                    $ JubesX.Statup("Inbt", 80, 1)
                    pass
            "Ошибка новичка.":
                    $ JubesX.Statup("Love", 90, -3)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Obed", 80, 1)
                    $ JubesX.FaceChange("angry")
                    ch_v "Да-да, может быть!"
        ch_v "Я умерла."
        $ JubesX.FaceChange("sadside")
        ch_v "Типа. . . реально умерла."
        ch_v "Была мертвее мертвого."
        ch_v ". . . но затем я очнулась."
        menu:
            "Мертвые на такое не способны.":
                    $ JubesX.Statup("Love", 200, -1)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.FaceChange("angry")
                    ch_v "Я знаю, что- Знаю, что мертвые на такое не способны."
                    $ JubesX.Statup("Love", 200, 2)
            ". . .":
                    $ JubesX.Statup("Love", 200, 1)
                    $ JubesX.Statup("Inbt", 80, 1)
            "Хм.":
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Obed", 80, 1)
                    $ JubesX.Statup("Inbt", 80, 1)
                    $ JubesX.FaceChange("confused")
        ch_v "Я стала нежитью, вампиром."
        $ JubesX.FaceChange("angry",Eyes="side")
        ch_v "Должно быть, он дал мне немного своей крови, когда я умирала."
        $ JubesX.FaceChange("sad",Eyes="closed")
        ch_v "Что-то меня понесло. . ."
        $ JubesX.FaceChange("sad")
        ch_v "Я не хотела обременять тебя всем этим."
        menu:
            "Нет, мне интересно узнать подробности твоей жизни.":
                    $ JubesX.FaceChange("smile",Brows="sad")
                    $ JubesX.Statup("Love", 200, 7)
                    ch_v ". . ."
                    ch_v "Я благодарна за эти слова. . ."
            "Я так рада, что ты поделилась этим со мной." if not Player.Male:
                    $ JubesX.FaceChange("smile")
                    $ JubesX.Statup("Love", 200, 5)
                    $ JubesX.Statup("Inbt", 80, 3)
                    $ JubesX.Statup("Inbt", 80, 2)
                    ch_v "Мне показалось, что ты должна знать."
            "Я так рад, что ты поделилась этим со мной." if Player.Male:
                    $ JubesX.FaceChange("smile")
                    $ JubesX.Statup("Love", 200, 5)
                    $ JubesX.Statup("Inbt", 80, 3)
                    $ JubesX.Statup("Inbt", 80, 2)
                    ch_v "Мне показалось, что ты должен знать."
            "Мне же нужно знать, с чем или с кем я имею дело.":
                    $ JubesX.FaceChange("sly")
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 50, 3)
                    $ JubesX.Statup("Obed", 80, 2)
                    ch_v "Ну, теперь ты -знаешь.-"
            "Но тем не менее ты это сделала.":
                    $ JubesX.FaceChange("angry")
                    $ JubesX.Statup("Love", 90, -5)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Obed", 80, 1)
                    ch_v "Ну прости, если я -раздражаю- тебя."
                    $ JubesX.Statup("Inbt", 50, 1)
                    $ JubesX.Statup("Inbt", 80, 2)
        ch_v "-Причина-, по которой я хотела поделиться этим с тобой. . ."
        $ JubesX.FaceChange("sly",Eyes="side")
        ch_v "С тех пор, как мы встретились, я очень привязалась к тебе."
        menu:
            "Ага, я тоже.":
                    $ JubesX.FaceChange("smile",2,Mouth="open")
                    $ JubesX.Statup("Love", 200, 10)
                    $ JubesX.Statup("Inbt", 80, 1)
                    ch_v ". . ."
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Приятно это слышать. . ."
            "Я знаю.":
                    $ JubesX.FaceChange("smile",2,Mouth="open")
                    $ JubesX.Statup("Love", 200, 3)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Obed", 80, 2)
                    ch_v "Думаю, это довольно очевидно, да. . ."
                    $ JubesX.FaceChange("smile",1)
            ". . .":
                    $ JubesX.FaceChange("sly",2,Eyes="side")
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Obed", 80, 1)
                    $ JubesX.Statup("Inbt", 50, 2)
                    $ JubesX.Statup("Inbt", 80, 1)
                    ch_v "Ну, эм. . ."
            "Из-за моих соков, да?" if not Player.Male:
                    $ JubesX.Statup("Love", 200, 1)
                    ch_v "Да, из-за-"
                    $ JubesX.FaceChange("surprised",2)
                    $ JubesX.Statup("Love", 90, -5)
                    $ JubesX.Statup("Obed", 50, 3)
                    $ JubesX.Statup("Obed", 80, 1)
                    ch_v "-НЕТ! Не \"из-за твоих соков!\""
                    $ JubesX.FaceChange("smile",1,Eyes="down",Brows="angry")
                    $ JubesX.Statup("Love", 200, 1)
                    $ JubesX.Statup("Inbt", 80, 1)
                    ch_v "Извращенка."
                    $ JubesX.Statup("Lust", 80, 5)
                    if ApprovalCheck(JubesX, 200, "I"):
                            $ JubesX.FaceChange("sly",2,Eyes="side")
                            $ JubesX.Statup("Love", 200, 4)
                            $ JubesX.Statup("Inbt", 50, 2)
                            $ JubesX.Statup("Inbt", 80, 1)
                            ch_v "Нууу, может быть, самую малость из-за них."
                    $ JubesX.FaceChange("sly",1,Eyes="side")
            "Из-за моей спермы, да?" if Player.Male:
                    $ JubesX.Statup("Love", 200, 1)
                    ch_v "Да, из-за-"
                    $ JubesX.FaceChange("surprised",2)
                    $ JubesX.Statup("Love", 90, -5)
                    $ JubesX.Statup("Obed", 50, 3)
                    $ JubesX.Statup("Obed", 80, 1)
                    ch_v "-НЕТ! Не \"из-за твоей спермы!\""
                    $ JubesX.FaceChange("smile",1,Eyes="down",Brows="angry")
                    $ JubesX.Statup("Love", 200, 1)
                    $ JubesX.Statup("Inbt", 80, 1)
                    ch_v "Извращенец."
                    $ JubesX.Statup("Lust", 80, 5)
                    if ApprovalCheck(JubesX, 200, "I"):
                            $ JubesX.FaceChange("sly",2,Eyes="side")
                            $ JubesX.Statup("Love", 200, 4)
                            $ JubesX.Statup("Inbt", 50, 2)
                            $ JubesX.Statup("Inbt", 80, 1)
                            ch_v "Нууу, может быть, самую малость из-за нее."
                    $ JubesX.FaceChange("sly",1,Eyes="side")

        if JubesX in Player.Harem:
                #if she somehow already ended up in the harem
                ch_v "Рада, что мы смогли с этим разобраться."
                if "JubesYes" in Player.Traits:
                        $ Player.Traits.remove("JubesYes")
                if "boyfriend" not in JubesX.Petnames:
                        $ JubesX.Petnames.append("boyfriend")
                return

        ch_v "Надеюсь, что наши отношения могут стать более серьезными."
        $ JubesX.FaceChange("sad",1,Mouth="lipbite")
        ch_v "Может, ты не против, чтобы я стала твоей девушкой?"
        if Player.Harem:
                $ JubesX.Statup("Inbt", 80, 2)
                ch_v "И, возможно, частью твоего ковена?"

        $ JubesX.Event[5] += 1
        menu:
            extend ""
            "Да, думаю, это было бы здорово.":
                    $ JubesX.Statup("Love", 200, 6)
                    $ JubesX.Statup("Obed", 80, 2)
                    $ JubesX.Statup("Inbt", 80, 3)
                    $ JubesX.FaceChange("smile",1,Eyes="side")
                    ch_v "Вот и славно."
            "Хмм? Ладно.":
                    $ JubesX.Statup("Love", 80, 3)
                    $ JubesX.Statup("Obed", 80, 5)
                    $ JubesX.Statup("Inbt", 80, 3)
                    $ JubesX.FaceChange("confused",1,Eyes="side")
                    ch_v "Лаааа. . . дно?"
            "Мне не очень нравится эта идея.":
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 80, 5)
                    $ JubesX.Statup("Inbt", 80, -5)
                    $ JubesX.FaceChange("sad",1)
                    if len(Player.Harem) >= 2:
                            ch_v "Это из-за [Player.Harem[0].Name_rod] и других?"
                    elif Player.Harem:
                            ch_v "Это из-за [Player.Harem[0].Name_rod]?"
                    else:
                            ch_v "А? Почему?"
                    menu:
                        extend ""
                        "Да, я не думаю, что она это поймет." if len(Player.Harem) == 1:
                                $ JubesX.Statup("Love", 200, -5)
                                $ JubesX.Statup("Obed", 80, 7)
                                $ JubesX.FaceChange("angry",1,Eyes="side")
                                $ JubesX.GLG(Player.Harem[0],800,-20,1)
                                ch_v "Мда, проблема. . ."
                        "Они этого не поймут." if len(Player.Harem) > 1:
                                $ JubesX.Statup("Love", 200, -5)
                                $ JubesX.Statup("Obed", 80, 7)
                                $ JubesX.FaceChange("angry",1,Eyes="side")
                                call HaremStatup(JubesX,700,-20) #lowers like of all Harem girls by 10
                                ch_v "Черт."
                        "Все. . . сложно.":
                                $ JubesX.Statup("Love", 200, -20)
                                $ JubesX.Statup("Obed", 80, 8)
                                $ JubesX.Statup("Inbt", 80, -5)
                                $ JubesX.FaceChange("angry",1)
                                ch_v "Я могу все упростить. . ."
                                $ JubesX.FaceChange("angry",1,Eyes="side")
                                if len(Player.Harem) >= 2:
                                    ch_v "Наверное, это из-за твоих подруг. . ."
                                    call HaremStatup(JubesX,700,-10) #lowers like of all Harem girls by 10
                                elif Player.Harem:
                                    ch_v "Значит это из-за [Player.Harem[0].Name_rod]. . ."
                                    $ JubesX.GLG(Player.Harem[0],800,-20,1)
                                $ Line = "no"
                        "Просто я не вижу тебя в этой роли.":
                                $ JubesX.Statup("Love", 200, -10)
                                $ JubesX.FaceChange("surprised",1)
                                ch_v "Ох."
                                $ JubesX.Statup("Obed", 80, 10)
                                $ JubesX.Statup("Inbt", 80, 5)
                                $ JubesX.FaceChange("sadside",1)
                                ch_v "Нууу, это, наверное, нормально? . ."
                    #end "why not?"

                    $ JubesX.FaceChange("sad",1)
                    if Line != "no":
                            ch_v "Думаю. . ."
                    ch_v "Мне, наверное, пора идти. . ."
                    "[JubesX.Name] уходит в неком оцепенении."
                    $ JubesX.Event[5] = 20
                    call Remove_Girl(JubesX)
                    $ Line = 0
                    return

        if Player.Harem:
                if len(Player.Harem) >= 2:
                    ch_v "Остальные не против?"
                else:
                    ch_v "[Player.Harem[0].Name] не против?"
                menu:
                    extend ""
                    "Все хорошо, всех все устраивает." if "JubesYes" in Player.Traits:
                            $ JubesX.Statup("Love", 200, 5)
                            $ JubesX.Statup("Obed", 80, 10)
                            $ JubesX.Statup("Inbt", 80, 5)
                            $ JubesX.FaceChange("surprised",1)
                            ch_v "О, класс!"
                    "Нууу. . . это сперва еще нужно узнать." if "JubesYes" not in Player.Traits:
                            $ JubesX.Statup("Love", 200, 3)
                            $ JubesX.Statup("Obed", 80, 3)
                            $ JubesX.Statup("Inbt", 80, 1)
                            $ JubesX.Statup("Lust", 80, 1)
                            $ JubesX.FaceChange("confused",1)
                            ch_v "Тогда, эм, потом дай мне знать, хорошо?"
                            $ JubesX.Event[5] = 20
                            call Remove_Girl(JubesX)
                            $ Line = 0
                            return
                call HaremStatup(JubesX,900,20) #raises like of all Harem girls by 20
        # end harem stuff

        if "Historia" not in Player.Traits:
            $ Player.Harem.append(JubesX)
            if "JubesYes" in Player.Traits:
                    $ Player.Traits.remove("JubesYes")
            $ JubesX.Petnames.append("boyfriend")
            call Harem_Initiation
        $ JubesX.Statup("Love", 200, 3)
        $ JubesX.Statup("Obed", 80, 3)
        $ JubesX.Statup("Inbt", 80, 1)
        $ JubesX.Statup("Lust", 80, 1)
        $ JubesX.FaceChange("sly",1)
        ch_v "Думаю, я знаю, как это отпраздновать. . ."
        if "Historia" in Player.Traits:
                return 1
        $ Tempmod = 10
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        $ Tempmod = 0
        return
## end Jubes_BF//////////////////////////////////////////////////////////



## start Jubes_Love//////////////////////////////////////////////////////////

label Jubes_Love(BO=[]):
        call Shift_Focus(JubesX)
        if bg_current != "bg jubes":
            if JubesX.Loc == bg_current or JubesX in Party:
                "Внезапно [JubesX.Name] изъявляет желание поговорить с вами в своей комнате и утягивает вас туда."
            else:
                "[JubesX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить с вами в своей комнате, затем она утягивает вас туда."
        else:
                "[JubesX.Name] внезапно очень пристально начинает смотреть на вас."

        $ bg_current = "bg jubes"
        $ JubesX.Loc = bg_current
        $ Event_Queue = [0,0]

        $ JubesX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene(0)
        call Display_Girl(JubesX)
        call Taboo_Level
        call CleartheRoom(JubesX)
        $ JubesX.DailyActions.append("relationship")
        $ Line = 0
        $ JubesX.FaceChange("sad",1,Eyes="side")
        ch_v "[JubesX.Petname], помнишь, я как-то рассказала тебе историю?"
        menu:
            extend ""
            "О торговом центре?":
                    $ JubesX.FaceChange("angry",1,Eyes="surprised",Mouth="open")
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Inbt", 90, 5)
                    ch_v "Нет, не -о торговом центре!-"
                    $ JubesX.FaceChange("angry",1)
                    $ JubesX.Statup("Inbt", 80, 2)
                    ch_v "Я про историю о том, как я стала вампиром!"
            "О том, как ты стала вампиром?":
                    $ JubesX.FaceChange("sad",1)
                    $ JubesX.Statup("Love", 200, 2)
                    ch_v "Ага. . ."
            "Нет.":
                    $ JubesX.FaceChange("angry",1)
                    $ JubesX.Statup("Love", 200, -4)
                    $ JubesX.Statup("Obed", 80, 2)
                    ch_v "Тебе стоит иногда обращать на меня внимание!"
                    $ JubesX.Statup("Inbt", 80, 2)
                    ch_v "Я про историю о том, как я стала вампиром!"
            "Которую из?":
                    $ JubesX.FaceChange("angry",1)
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Obed", 80, 1)
                    ch_v "О, значит я зря трачу твое время, рассказывая слишком много историй, за которыми ты не можешь уследить?"
                    $ JubesX.Statup("Inbt", 80, 2)
                    ch_v "Я про историю о том, как я стала вампиром!"
            "А?":
                    $ JubesX.FaceChange("angry",1)
                    $ JubesX.Statup("Love", 200, -5)
                    ch_v "-Ты меня вообще не слушаешь?!-"
                    $ JubesX.Statup("Inbt", 90, 3)
                    ch_v "Я про историю о том, как я стала вампиром."

        ch_v "Мне нужно закончить рассказ. . ."
        $ JubesX.FaceChange("sadside",1)
        ch_v ". . . рассказать всю правду о том, как мы встретились."
        menu:
            extend ""
            "Я помню, как мы встретились.":
                    $ JubesX.Statup("Love", 200, 3)
                    $ JubesX.FaceChange("sadside",1,Mouth="smile")
                    ch_v "Нет, я про то, как мы дошли до этой встречи."
            "Хорошо, что тогда произошло?":
                    $ JubesX.Statup("Love", 200, 2)
                    $ JubesX.Statup("Obed", 90, 1)
            ". . .":
                    $ JubesX.Statup("Love", 200, 2)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    pass
            "Это надолго, да?":
                    $ JubesX.FaceChange("angry",1,Mouth="open")
                    $ JubesX.Statup("Love", 200, -3)
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Inbt", 90, 1)
                    ch_v "Это займет столько времени, сколько потребуется!"
            "Мне все равно.":
                    $ JubesX.FaceChange("angry",1,Mouth="open")
                    $ JubesX.Statup("Love", 200, -4)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 3)
                    ch_v "Ох, садись и слушай!"
        $ JubesX.FaceChange("sad",1)
        ch_v "Мне нужно пить кровь, чтобы выжить."
        $ JubesX.FaceChange("sadside",1)
        if not Player.Male:
            ch_v "Ты видела, какой я становлюсь, когда не пью."
        else:
            ch_v "Ты видел, какой я становлюсь, когда не пью."
        menu:
            extend ""
            "Да, ты не можешь выйти на улицу.":
                    $ JubesX.Statup("Love", 200, 2)
                    ch_v "Дело не только в этом. . ."
            "Ага, твои глаза светятся красным.":
                    $ JubesX.FaceChange("angry",1,Mouth="open")
                    $ JubesX.Statup("Love", 200, -3)
                    ch_v "Нет, не правда!"
            ". . .":
                    $ JubesX.Statup("Love", 200, 1)
                    $ JubesX.Statup("Obed", 90, 1)
            "Правда?":
                    $ JubesX.FaceChange("perplexed",1)
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Obed", 90, 1)
                    if not Player.Male:
                        ch_v "Ты должна была заметить!"
                    else:
                        ch_v "Ты должен был заметить!"
        ch_v "Я не только не могу выходить на улицу при дневном свете. . ."
        $ JubesX.FaceChange("sadside",1)
        ch_v "Но также немного. . ."
        ch_v "Зверею."
        menu:
            extend ""
            "А, становишься \"мягкой и пушистой.\" Понял.":
                    $ JubesX.FaceChange("angry",1,Mouth="open")
                    $ JubesX.Statup("Love", 200, -4)
                    ch_v "Я не становлюсь -пушистой,- я -зверею!-"
                    $ JubesX.FaceChange("angry",1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    ch_v "Это значит, что я становлюсь жестокой и неуправляемой."
            "Становишься жестокой?":
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Ага. . . жестокой."
                    $ JubesX.Statup("Inbt", 90, 2)
                    ch_v "Неуправляемой. . ."
            "Ты никому не причинила вреда?":
                    $ JubesX.FaceChange("surprised",1,Brows="sad")
                    $ JubesX.Statup("Love", 200, 2)
                    $ JubesX.Statup("Obed", 90, 3)
                    ch_v ". . . {w=0.3}{nw}"
            "О, ладно.":
                    $ JubesX.FaceChange("angry",1,Mouth="open")
                    $ JubesX.Statup("Love", 200, -3)
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Ты слишком спокойно относишься к этому!"
                    $ JubesX.Statup("Inbt", 90, 3)
                    ch_v "Я становлюсь жестокой!"
                    $ JubesX.FaceChange("angry",1)
                    ch_v "Это тебе не \"ладно!\""
        $ JubesX.FaceChange("sadside",1)
        ch_v "Ранее меня удерживали товарищи от приченения вреда невиновным."
        ch_v "Но я отправила нескольких из них в лазарет. . ."
        menu:
            extend ""
            "Это должно быть тяжело.":
                    $ JubesX.FaceChange("sad",1,Mouth="smile")
                    $ JubesX.Statup("Love", 200, 3)
                    $ JubesX.Statup("Inbt", 90, 2)
                    ch_v "Так и есть, спасибо. . ."
            "Ну, это не самый плохой расклад.":
                    $ JubesX.Statup("Love", 200, 4)
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Ага. . ."
            "Повезло.":
                    $ JubesX.Statup("Love", 200, -1)
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Ага, \"повезло.\" . ."
            "Хм.":
                    $ JubesX.FaceChange("angry",1,Eyes="side")
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Inbt", 90, 3)
                    ch_v "По крайней мере, они обращали на меня больше внимания, чем ты!"

        $ JubesX.FaceChange("sadside",1,Mouth="smirk")
        ch_v "Мне повезло, что у меня были хорошие друзья."
        ch_v "Но мне все равно нужно было есть."
        $ JubesX.FaceChange("sadside",1)
        ch_v "Какое-то время я держалась на крови Логана."
        ch_v "Она утоляла даже самый сильный голод, но я все еще была вампиром."
        ch_v "Мне все еще приходилось прятаться от солнца."
        $ JubesX.FaceChange("sad",1)
        ch_v "А потом я услышала о тебе."
        $ JubesX.FaceChange("sad",1,Eyes="leftside")
        ch_v "\"Новый мутант в городе,\""
        ch_v "\"-прикосновение, которое может свести на нет способности мутантов.\""
        $ JubesX.FaceChange("sad",1)
        ch_v "И я подумала, \"может, это сработает и с моим вампиризмом?\""
        ch_v "Стоило попробовать, ведь так?"
        $ JubesX.FaceChange("sadside",1)
        ch_v "И вот я стала понемногу следить за тобой по ночам."
        if not Player.Male:
            ch_v "Выбрала ночь, когда ты была одна, и. . ."
        else:
            ch_v "Выбрала ночь, когда ты был один, и. . ."
        $ JubesX.Eyes="closed"
        ch_v "Укусила."
        menu:
            extend ""
            "Эту часть я помню.":
                    $ JubesX.Statup("Love", 200, 3)
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Inbt", 90, 1)
                    ch_v "Ага. . ."
            ". . .":
                    $ JubesX.Statup("Love", 200, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
            "Ага, было больно!":
                    $ JubesX.FaceChange("surprised",2,Mouth="open",Brows="sad")
                    $ JubesX.Statup("Love", 200, 1)
                    $ JubesX.Statup("Obed", 90, 3)
                    ch_v "Прости, виновата."
            "И что произошло дальше?":
                    $ JubesX.FaceChange("surprised",2,Mouth="open")
                    $ JubesX.Statup("Love", 200, -1)
                    $ JubesX.Statup("Inbt", 90, 3)
                    if not Player.Male:
                        ch_v "Ты там была!"
                    else:
                        ch_v "Ты там был!"
                    $ JubesX.FaceChange("confused",1)
                    ch_v "Не помнишь?"
                    ch_v "Когда мы впервые встретились?"
                    ch_v "В твоей постели?"
        $ JubesX.FaceChange("sad",1)
        ch_v "Итак, теперь мы знаем, что это действительно работает."
        ch_v "Быть с тобой, прикасаться к тебе, пить. . ."
        if JubesX.Swallow:
                $ JubesX.Statup("Lust", 80, 5)
                $ JubesX.FaceChange("sly",2,Eyes="down")
                ch_v ". . . {w=0.3}{nw}"
        $ JubesX.FaceChange("sly",1)
        ch_v ". . . твою кровь."
        ch_v "Все это помогает оттеснить вампиризм."
        menu:
            extend ""
            "Я рада, что смогла помочь тебе." if not Player.Male:
                    $ JubesX.Statup("Love", 200, 8)
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Ага, спасибо. . ."
            "Я рад, что смог помочь тебе." if Player.Male:
                    $ JubesX.Statup("Love", 200, 8)
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Ага, спасибо. . ."
            "Мне тоже это было полезно.":
                    $ JubesX.Statup("Love", 200, 5)
                    $ JubesX.Statup("Obed", 90, 5)
                    ch_v "Пожалуй, так и есть. . ."
            "Ага, ты ради этого готова на все.":
                    $ JubesX.FaceChange("sly",1,Brows="confused")
                    $ JubesX.Statup("Obed", 90, 5)
                    $ JubesX.Statup("Inbt", 90, 5)
                    if not Player.Male:
                        ch_v "Нууу, могла бы сказать и помягче. . ."
                    else:
                        ch_v "Нууу, мог бы сказать и помягче. . ."
            ". . .":
                    $ JubesX.Statup("Love", 200, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
        $ JubesX.FaceChange("smile",1,Mouth="open")
        ch_v "Но я еще не закончила!"
        $ JubesX.FaceChange("smile",1)
        ch_v "Дело не только в том. . ."
        if not Player.Male:
            ch_v "Что я хочу быть с тобой, потому что ты мне полезна. . ."
        else:
            ch_v "Что я хочу быть с тобой, потому что ты мне полезен. . ."
        $ JubesX.FaceChange("smile",1,Eyes="side")
        ch_v "Я также. . ."
        $ JubesX.FaceChange("smile",1)
        ch_v "Люблю тебя."
        menu:
                extend ""
                "Я тоже тебя люблю!":
                    $ JubesX.FaceChange("smile",1)
                    $ JubesX.Statup("Love", 200, 20)
                    $ JubesX.Statup("Inbt", 90, 5)
                    if not Player.Male:
                        ch_v "Фух, я рада, что ты это сказала."
                    else:
                        ch_v "Фух, я рада, что ты это сказал."
                    $ JubesX.Petnames.append("lover")
                    jump Jubes_Love_End
                "Я знаю.":
                    $ JubesX.FaceChange("smile",1)
                    $ JubesX.Statup("Love", 200, 5)
                    $ JubesX.Statup("Obed", 90, 5)
                    $ JubesX.Statup("Inbt", 90, 5)
                    ch_v "Эм. Не совсем такой ответ я ждала. . ."
                "Это здорово?":
                    $ JubesX.FaceChange("sad",1)
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 90, 5)
                    ch_v "Ох. . . здорово. . ."
                "Хм.":
                    $ JubesX.FaceChange("angry",1)
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 90, 10)
                    ch_v "Так себе ответ."
        menu:
                extend ""
                "Ох, я тоже тебя люблю!":
                    $ JubesX.FaceChange("smile",1)
                    $ JubesX.Statup("Love", 200, 15)
                    $ JubesX.Statup("Obed", 90, 5)
                    $ JubesX.Statup("Inbt", 90, 5)
                    if not Player.Male:
                        ch_v "Фух, я рада, что ты это сказала."
                    else:
                        ch_v "Фух, я рада, что ты это сказал."
                    $ JubesX.Petnames.append("lover")
                    jump Jubes_Love_End
                "Я. . . тоже тебя люблю?":
                    $ JubesX.FaceChange("confused",1)
                    $ JubesX.Statup("Love", 200, 5)
                    $ JubesX.Statup("Obed", 90, 10)
                    ch_v "Хорошо, я тебе верю."
                    $ JubesX.Petnames.append("lover")
                    jump Jubes_Love_End
                "Это, конечно, круто и все такое. . .":
                    $ JubesX.FaceChange("sadside",1)
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 90, 10)
                    $ JubesX.Statup("Inbt", 90, -5)
                    ch_v ". . . но. . . ты не можешь ответить мне взаимностью. . ."
                "Мне. . . не по себе от твоих слов.":
                    $ JubesX.FaceChange("angry",1)
                    $ JubesX.Statup("Love", 200, -10)
                    $ JubesX.Statup("Obed", 90, 15)
                    $ JubesX.Statup("Inbt", 90, -5)
                    ch_v "А вот теперь я действительно обеспокоена."

        $ JubesX.FaceChange("sad",1)
        ch_v "Значит, ты не чувствуешь того же?"
        ch_v "Это из-за другой?"
        $ Line = 0
        menu:
                extend ""
                "Да. . .":
                        $ JubesX.Statup("Obed", 90, 10)
                        $ JubesX.Statup("Inbt", 90, 10)
                        $ JubesX.FaceChange("sadside",1)
                        ch_v "Ну, у тебя есть выбор."
                        ch_v "Мне не обязательно знать, кто это."
                "Да, у меня есть другие.":
                        $ JubesX.Statup("Obed", 90, 15)
                        $ JubesX.Statup("Inbt", 90, 5)
                        $ JubesX.Statup("Lust", 90, 5)
                        $ JubesX.FaceChange("sadside",1)
                        ch_v "Ну, у тебя есть выбор."
                "У меня никого нет.":
                        $ JubesX.Statup("Love", 200, -15)
                        $ JubesX.Statup("Obed", 90, 15)
                        $ JubesX.Statup("Inbt", 90, 5)
                        $ JubesX.FaceChange("sad",1)
                        if ApprovalCheck(JubesX, 1000, "OI"):
                            ch_v "Ох, значит я просто \"не та\", кто тебе нужен. . ."
                        else:
                            ch_v ". . ."
                "Просто ты мне не настолько нравишься.":
                        $ JubesX.FaceChange("sad")
                        $ JubesX.Statup("Love", 200, -25)
                        $ JubesX.Statup("Obed", 90, 15)
                        ch_v "Ох."
                        $ JubesX.Statup("Love", 200, -10)
                        ch_v "Ладно."
        ch_v "Думаю, если ты так к этому относишься. . ."
        ch_v "Я. . . увидимся."

label Jubes_Love_End:
        if "lover" not in JubesX.Petnames:
                $ JubesX.Event[6] = 20
                hide Jubes_Sprite with easeoutright
                call Remove_Girl(JubesX)
                $ JubesX.Loc = "hold" #puts her off the board for the day
                jump Misplaced
                return

        $ JubesX.Event[6] = 5
        "[JubesX.Name] обнимает вас."
        $ JubesX.Statup("Love", 200, 25)
        $ JubesX.Statup("Lust", 90, 5)
        $ JubesX.FaceChange("sly",1)
        ch_v "Итак, лапочка. . ."
        $ JubesX.Statup("Lust", 90, 10)

        if not JubesX.Sex:
            $ JubesX.FaceChange("bemused",2)
            ch_v "Думаю, теперь я готова к этому шагу. . ."
        else:
            if not Player.Male:
                ch_v "Ты бы хотела немного пошалить?"
            else:
                ch_v "Ты бы хотел немного пошалить?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
#                "Yeah, let's do this. . . [[have sex]":
#                    $ JubesX.Statup("Inbt", 30, 20)
#                    $ JubesX.Statup("Obed", 70, 10)
#                    ch_v "Mmmm. . ."
#                    call SexAct("sex") # call Jubes_SexAct("sex")
#                "I have something else in mind. . . a blowjob?":
                "Ага, давай сделаем это!":
                    $ JubesX.FaceChange("surprised",1,Mouth="open")
                    $ JubesX.Statup("Love", 200, 5)
                    $ JubesX.Statup("Inbt", 30, 10)
                    $ JubesX.Statup("Obed", 70, 20)
                    ch_v "О, мы и -правда- с тобой на одной волне!"
                    $ Tempmod = 20
                    call SexAct("blow") # call Jubes_SexAct("blow")
                "У меня есть другая идея. . .[[выбрать другое занятие]":
                    $ JubesX.Brows = "confused"
                    $ JubesX.Statup("Obed", 70, 25)
                    ch_v "Например? . ."
                    $ Tempmod = 20
                    call SexMenu
        jump Misplaced
        return

label Jubes_Love_Redux:
         #this is for if you rejected her but want a second chance
        $ Line = 0
        $ JubesX.DailyActions.append("relationship")
        call Shift_Focus(JubesX)

        if JubesX.Event[6] >= 25:
                #if this is the second time through
                ch_p "Надеюсь, ты меня простила, я все еще люблю тебя."
                $ JubesX.Statup("Love", 95, 10)
                if ApprovalCheck(JubesX, 950, "L"):
                    $ Line = "love"
                else:
                    $ JubesX.FaceChange("sad")
                    ch_v "Я не знаю, [JubesX.Petname]. . ."
                    $ JubesX.Eyes="side"
                    ch_v ". . ."
                    $ JubesX.FaceChange("sad",Mouth="lipbite")
                    ch_v "Но я выслушаю тебя. . ."
        elif JubesX.Event[6] >= 23:
                #if you pissed her off the first time
                if not Player.Male:
                    ch_p "Я была слишком груба, когда ты открылась мне."
                else:
                    ch_p "Я был слишком груб, когда ты открылась мне."
                $ JubesX.Statup("Love", 95, 10)
                if ApprovalCheck(JubesX, 950, "L"):
                    ch_v "И. . ."
                else:
                    $ JubesX.FaceChange("sad")
                    ch_v "Я не знаю, что и думать, [JubesX.Petname]. . ."
                    $ JubesX.Eyes="side"
                    ch_v ". . ."
                    $ JubesX.FaceChange("sad",Mouth="lipbite")
                    ch_v "Но я выслушаю тебя. . ."
        else:
                    if not Player.Male:
                        ch_p "Помнишь, я сказала тебе, что не люблю тебя?"
                    else:
                        ch_p "Помнишь, я сказал тебе, что не люблю тебя?"
                    $ JubesX.FaceChange("confused",1)
                    ch_v ". . ."
                    $ JubesX.FaceChange("sad")
                    ch_v "Думаю, да?"

        if Line != "love":
                menu:
                    extend ""
                    "Прости, я не хотела так говорить." if not Player.Male:
                        $ JubesX.Eyes = "surprised"
                        ch_v "А?"
                        ch_v "Теперь хочешь сказать что-то другое?"
                        ch_p "Ага. То есть, да, я люблю тебя, [JubesX.Name]."
                        $ JubesX.Statup("Love", 200, 10)
                        if ApprovalCheck(JubesX, 950, "L"):
                            $ Line = "love"
                        else:
                            $ JubesX.FaceChange("sadside")
                            ch_v "Я не уверена, что мои чувства к тебе взаимны. . ."
                    "Прости, я не хотел так говорить." if Player.Male:
                        $ JubesX.Eyes = "surprised"
                        ch_v "А?"
                        ch_v "Теперь хочешь сказать что-то другое?"
                        ch_p "Ага. То есть, да, я люблю тебя, [JubesX.Name]."
                        $ JubesX.Statup("Love", 200, 10)
                        if ApprovalCheck(JubesX, 950, "L"):
                            $ Line = "love"
                        else:
                            $ JubesX.FaceChange("sadside")
                            ch_v "Я не уверена, что мои чувства к тебе взаимны. . ."
                    "Я передумала, я люблю тебя, так что. . ." if not Player.Male:
                        if ApprovalCheck(JubesX, 950, "L"):
                            $ Line = "love"
                            ch_v "Ох."
                        else:
                            $ JubesX.Mouth = "sad"
                            ch_v "Нууу. . ."
                            $ JubesX.Statup("Inbt", 90, 10)
                            $ JubesX.FaceChange("sadside")
                            ch_v "Я тоже передумала. . ."
                    "Я передумал, я люблю тебя, так что. . ." if Player.Male:
                        if ApprovalCheck(JubesX, 950, "L"):
                            $ Line = "love"
                            ch_v "Ох."
                        else:
                            $ JubesX.Mouth = "sad"
                            ch_v "Нууу. . ."
                            $ JubesX.Statup("Inbt", 90, 10)
                            $ JubesX.FaceChange("sadside")
                            ch_v "Я тоже передумала. . ."
                    "Эм, неважно.":
                            $ JubesX.Statup("Love", 200, -30)
                            $ JubesX.Statup("Obed", 50, 10)
                            $ JubesX.FaceChange("angry")
                            if not Player.Male:
                                ch_v "Ну и пошла отсюда, блядина грязная."
                            else:
                                ch_v "Ну и пошел отсюда, пидор грязный."
                            $ JubesX.RecentActions.append("angry")
                            $ JubesX.DailyActions.append("angry")
        if Line == "love":
                $ JubesX.Statup("Love", 200, 40)
                $ JubesX.Statup("Obed", 90, 10)
                $ JubesX.Statup("Inbt", 90, 10)
                $ JubesX.FaceChange("smile")
                ch_v "Я тоже тебя люблю, [JubesX.Petname]!"
                if JubesX.Event[6] < 25:
                        $ JubesX.FaceChange("sly")
                        "Она обнимает вас и притягивает к себе."
                        ch_v "Я знала, что ты передумаешь."
                $ JubesX.Petnames.append("lover")
        $ JubesX.Event[6] = 25
        jump Misplaced
        return
# end Jubes_Love//////////////////////////////////////////////////////////



# start Jubes_Sub//////////////////////////////////////////////////////////

label Jubes_Sub(BO=[]):
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(JubesX,"bemused","выглядит тихой. . .")
                return
        call Shift_Focus(JubesX)
        if JubesX.Loc != bg_current:
            $ JubesX.Loc = bg_current
            if JubesX not in Party:
                "[JubesX.Name] подходит к вам и жестом показывает, что хочет поговорить с вами наедине."
            else:
                "[JubesX.Name] поворачивается к вам и жестом показывает, что хочет поговорить с вами наедине."
        $ Event_Queue = [0,0]
        $ JubesX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene(0)
        call Display_Girl(JubesX)
        call Taboo_Level
        call CleartheRoom(JubesX)
        $ JubesX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in JubesX.History:
                call expression JubesX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        $ Line = 0
        $ JubesX.FaceChange("sadside",1)
        ch_v "[JubesX.Petname]?"
        ch_v "Все эти. . . дела с \"солнечным светом\". . ."
        ch_v "Я очень привыкла полагаться на тебя."
        ch_v "Больше, чем обычно на кого-либо другого. . ."
        menu:
            extend ""
            "Это, должно быть, тяжело для тебя.":
                    $ JubesX.Statup("Love", 90, 2)
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Ага, немного."
                    $ JubesX.FaceChange("sadside", 1,Mouth="smile")
                    ch_v "Но мне стало даже нравиться. . ."
            "Да, меня это тоже раздражает.":
                    $ JubesX.FaceChange("angry", 1)
                    $ JubesX.Statup("Love", 80, -3)
                    $ JubesX.Statup("Love", 90, -2)
                    ch_v "Ну прости, что я так -обременяю- тебя."
                    $ JubesX.FaceChange("sly", 1,Eyes="side")
                    $ JubesX.Statup("Inbt", 80, 2)
                    ch_v "Но. . . мне это стало нравиться. . ."
            "О, тебе это нравится?":
                    $ JubesX.Statup("Obed", 200, 5)
                    ch_v "Нууу. . ."
                    $ JubesX.FaceChange("sly", 1)
                    $ JubesX.Statup("Inbt", 90, 5)
                    ch_v "Немного?"
            "Ладно?":
                    $ JubesX.Statup("Love", 90, -2)
                    ch_v "Так вот. . ."
                    $ JubesX.FaceChange("sly", 1)
                    $ JubesX.Statup("Inbt", 90, 5)
                    $ JubesX.Statup("Obed", 70, 3)
                    ch_v ". . . Мне это стало нравиться. . ."
        menu:
            extend ""
            "Тебе нравится полагаться на меня?":
                    $ JubesX.FaceChange("smile", 1)
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Obed", 200, 3)
                    ch_v "Ага. . . это. . .  приятно."
                    ch_v "И мне от этого тепло."
            "Тебе нравится быть обузой?":
                    $ JubesX.FaceChange("confused", 2)
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Нууу, -не совсем!-"
                    $ JubesX.FaceChange("angry", 1)
                    ch_v "Мне нравится другая часть всего этого."
                    $ JubesX.FaceChange("angry", 1,Eyes="side")
                    ch_v ". . ."
                    $ JubesX.FaceChange("sad", 1)
                    ch_v "Извини."
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Мне просто нравится, что я могу положиться на тебя. . ."
            "Тебе нравится, когда я контролирую тебя?":
                    $ JubesX.Statup("Obed", 200, 5)
                    $ JubesX.FaceChange("sadside", 2,Mouth="smirk")
                    ch_v ". . ."
                    $ JubesX.Statup("Inbt", 80, 5)
                    ch_v "Ага."
                    $ JubesX.FaceChange("sly", 1)
                    ch_v "Нравится."
            "Клево.":
                    $ JubesX.FaceChange("confused", 1)
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Inbt", 50, -1)
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Ага. . ."
                    ch_v "Клево. . ."
        menu:
            extend ""
            "Так что ты хотела?":
                    $ JubesX.FaceChange("sly", 1,Eyes="side")
                    $ JubesX.Statup("Obed", 200, 3)
                    ch_v "Нууу, я вроде как хотела. . ."
                    ch_v "Хотела, чтобы ты, возможно. . ."
                    $ JubesX.FaceChange("sly", 1)
                    $ JubesX.Statup("Inbt", 80, 5)
                    if not Player.Male:
                        ch_v "Начала \"контролировал\" меня немного больше?"
                    else:
                        ch_v "Начал \"контролировал\" меня немного больше?"
            "Похоже, мне никуда от тебя не деться.":
                    $ JubesX.FaceChange("angry", 1)
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 90, 3)
                    ch_v "Нууу. . . да."
                    $ JubesX.FaceChange("sad", 1)
                    ch_v "Извини."
                    $ JubesX.Statup("Inbt", 90, 5)
                    ch_v "Но это может понравиться и тебе тоже. . ."
            "Ты хочешь, чтобы я больше контролировала тебя." if not Player.Male:
                    $ JubesX.FaceChange("perplexed", 2)
                    $ JubesX.Statup("Obed", 90, 5)
                    ch_v "Эм. . ."
                    $ JubesX.FaceChange("sexy", 1)
                    ch_v "Я не. . . Нет, ты права. . ."
            "Ты хочешь, чтобы я больше контролировал тебя." if Player.Male:
                    $ JubesX.FaceChange("perplexed", 2)
                    $ JubesX.Statup("Obed", 90, 5)
                    ch_v "Эм. . ."
                    $ JubesX.FaceChange("sexy", 1)
                    ch_v "Я не. . . Нет, ты прав. . ."
            "Иии. . ?":
                    $ JubesX.FaceChange("confused", 1)
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Inbt", 60, -2)
                    ch_v "-Так вот-. . ."
        ch_v "Я бы хотела. . . Не знаю. . ."
        menu:
            "Чтобы я дала тебе немного пространства?" if not Player.Male:
                    $ JubesX.FaceChange("surprised", 1)
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Inbt", 60, 2)
                    ch_v "Нет!"
                    $ JubesX.FaceChange("sad", 1,Eyes="surprised")
                    ch_v "Я не хочу этого, я хочу быть с тобой!"
                    $ JubesX.FaceChange("sadside", 2,Mouth="smirk")
                    $ JubesX.Statup("Inbt", 60, 2)
                    ch_v "Я хочу, чтобы ты. . . слегка командовала мной?"
            "Чтобы я дал тебе немного пространства?" if Player.Male:
                    $ JubesX.FaceChange("surprised", 1)
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Inbt", 60, 2)
                    ch_v "Нет!"
                    $ JubesX.FaceChange("sad", 1,Eyes="surprised")
                    ch_v "Я не хочу этого, я хочу быть с тобой!"
                    $ JubesX.FaceChange("sadside", 2,Mouth="smirk")
                    $ JubesX.Statup("Inbt", 60, 2)
                    ch_v "Я хочу, чтобы ты. . . слегка командовал мной?"
            "Ты хочешь, чтобы я говорила тебе, что делать." if not Player.Male:
                    $ JubesX.Statup("Love", 200, 2)
                    $ JubesX.Statup("Obed", 200, 10)
                    $ JubesX.FaceChange("surprised", 2)
                    ch_v ". . ."
                    $ JubesX.FaceChange("sly", 1)
                    ch_v "Ага. . ."
            "Ты хочешь, чтобы я говорил тебе, что делать." if Player.Male:
                    $ JubesX.Statup("Love", 200, 2)
                    $ JubesX.Statup("Obed", 200, 10)
                    $ JubesX.FaceChange("surprised", 2)
                    ch_v ". . ."
                    $ JubesX.FaceChange("sly", 1)
                    ch_v "Ага. . ."
            "Мы закончили?":
                    $ JubesX.Statup("Love", 200, -3)
                    $ JubesX.FaceChange("surprised", 1)
                    ch_v "Нет!"
                    $ JubesX.FaceChange("sadside", 1)
                    ch_v ". . ."
                    ch_v "Я надеялась, что ты сможешь. . ."
                    $ JubesX.FaceChange("sly", 1)
                    $ JubesX.Statup("Inbt", 60, 2)
                    ch_v "Слегка командовал мной?"
        menu:
            "Это я могу.":
                    $ JubesX.Statup("Love", 90, 3)
                    $ JubesX.Statup("Obed", 200, 10)
                    $ JubesX.FaceChange("smile", 1)
                    ch_v "Отлично. . ."
                    $ JubesX.FaceChange("sly", 1,Brows="sad")
                    if not Player.Male:
                        ch_v "Я могу звать тебя. . . \"госпожой?\""
                    else:
                        ch_v "Я могу звать тебя. . . \"господином?\""
                    menu:
                        extend ""
                        "Да.":
                                if not Player.Male:
                                    $ JubesX.Petname = "госпожа"
                                    $ JubesX.Petname_rod = "госпожи"
                                    $ JubesX.Petname_dat = "госпоже"
                                    $ JubesX.Petname_vin = "госпожу"
                                    $ JubesX.Petname_tvo = "госпожой"
                                    $ JubesX.Petname_pre = "госпоже"
                                else:
                                    $ JubesX.Petname = "господин"
                                    $ JubesX.Petname_rod = "господина"
                                    $ JubesX.Petname_dat = "господину"
                                    $ JubesX.Petname_vin = "господина"
                                    $ JubesX.Petname_tvo = "господином"
                                    $ JubesX.Petname_pre = "господине"
                                $ JubesX.Statup("Inbt", 80, 2)
                                $ JubesX.Statup("Obed", 200, 1)
                                $ JubesX.FaceChange("smile", 1)
                                if not Player.Male:
                                    ch_v "Хорошо. . . госпожа."
                                else:
                                    ch_v "Хорошо. . . господин."
                        "Может, когда-нибудь потом. . .":
                                $ JubesX.FaceChange("sad", 1)
                                ch_v "Ох. . . ладно. . ."
                    $ JubesX.FaceChange("sly", 1)
                    $ JubesX.Petnames.append("sir")
            "Мне совсем этого не хочется.":
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Inbt", 80, -2)
                    $ JubesX.Statup("Obed", 200, -2)
                    $ JubesX.FaceChange("sad", 1)
                    ch_v "Ох. . . Я понимаю."
                    $ JubesX.FaceChange("sadside", 1)
                    ch_v "Эм. . . тогда забудь. . ."
                    ch_v "Извини за беспокойство. . ."
            "Не, мне это не интересно.":
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Inbt", 80, -2)
                    $ JubesX.FaceChange("sad", 1)
                    ch_v "Ох. . . Я понимаю."
                    $ JubesX.FaceChange("sadside", 1)
                    ch_v "Эм. . . тогда забудь. . ."
                    ch_v "Извини за беспокойство. . ."

#Jubes_Sub_Bad_End:
        $ JubesX.History.append("sir")
        if "sir" not in JubesX.Petnames:
                $ JubesX.FaceChange("sadside", 2)
                ch_v "Ох, что ж. . ."
                hide Jubes_Sprite with easeoutright
                call Remove_Girl(JubesX)
                if "Historia" not in Player.Traits:
                        $ renpy.pop_call()
                "[JubesX.Name] выходит из комнаты."
        return

label Jubes_Sub_Asked:
        $ Line = 0
        $ JubesX.FaceChange("sadside", 1)
        call Shift_Focus(JubesX)
        ch_v "Ага. Тебе, похоже, эта идея не понравилась."
        menu:
            extend ""
            "Я хочу извиниться. Надеюсь, мы можем попробовать еще раз?":
                    if "sir" in JubesX.Petnames and ApprovalCheck(JubesX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(JubesX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            $ JubesX.FaceChange("sadside", 1)
                            if not Player.Male:
                                ch_v "Нет, ты была права, я заблуждалась. . ." #Failed again. :(
                            else:
                                ch_v "Нет, ты был прав, я заблуждалась. . ." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ JubesX.Statup("Love", 90, 10)
                            $ JubesX.FaceChange("sly", 1)
                            if not Player.Male:
                                ch_v "Я рада, что ты все обдумала. . ."
                            else:
                                ch_v "Я рада, что ты все обдумал. . ."
                            ch_v "Ага, давай попробуем. . ."

            "Послушай. . . Я знаю, что ты этого хочешь. Так попробуем еще раз, или нет?":
                    $ JubesX.FaceChange("bemused", 1)
                    if "sir" in JubesX.Petnames:
                        if ApprovalCheck(JubesX, 850, "O"):
                            ch_v "Хмм. . . ладно."
                        else:
                            $ JubesX.FaceChange("sadside", 1)
                            if not Player.Male:
                                ch_v "Думаю, в тот раз ты была права. . ."
                            else:
                                ch_v "Думаю, в тот раз ты был прав. . ."
                            $ Line = "rude"
                    elif ApprovalCheck(JubesX, 600, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            $ JubesX.FaceChange("confused", 1)
                            ch_v "Нууу. . ."
                            $ JubesX.FaceChange("sly", 1)
                            if not Player.Male:
                                ch_v "возможно, ты и права."
                                ch_v "Но ты сама поначалу была против. . ."
                            else:
                                ch_v "возможно, ты и прав."
                                ch_v "Но ты сам поначалу был против. . ."
                            menu:
                                extend ""
                                "Я могла бы стать твоей госпожой." if not Player.Male:
                                                $ JubesX.Statup("Love", 90, 15)
                                                $ JubesX.Statup("Inbt", 50, 10)
                                                $ JubesX.FaceChange("bemused", 1)
                                                $ JubesX.Eyes = "side"
                                                ch_v ". . . Тогда ладно."
                                "Я мог бы стать твоим господином." if Player.Male:
                                                $ JubesX.Statup("Love", 90, 15)
                                                $ JubesX.Statup("Inbt", 50, 10)
                                                $ JubesX.FaceChange("bemused", 1)
                                                $ JubesX.Eyes = "side"
                                                ch_v ". . . Тогда ладно."
                                "Я уже твоя госпожа, сученька." if not Player.Male:
                                        if "sir" in JubesX.Petnames and ApprovalCheck(JubesX, 900, "O"):
                                                $ JubesX.Statup("Love", 200, -5)
                                                $ JubesX.Statup("Obed", 200, 10)
                                                ch_v ". . ."
                                        elif ApprovalCheck(JubesX,700, "O"):
                                                $ JubesX.Statup("Love", 200, -5)
                                                $ JubesX.Statup("Obed", 200, 10)
                                                ch_v "Хмммм. . ."
                                        else: #if it failed both those things,
                                                $ JubesX.Statup("Love", 200, -10)
                                                $ JubesX.Statup("Obed", 90, -10)
                                                $ JubesX.Statup("Obed", 200, -10)
                                                $ JubesX.Statup("Inbt", 50, -15)
                                                $ JubesX.FaceChange("angry", 1)
                                                ch_v "Эм, это немного перебор. . ."
                                                $ Line = "rude"
                                "Я уже твой господин, сученька." if Player.Male:
                                        if "sir" in JubesX.Petnames and ApprovalCheck(JubesX, 900, "O"):
                                                $ JubesX.Statup("Love", 200, -5)
                                                $ JubesX.Statup("Obed", 200, 10)
                                                ch_v ". . ."
                                        elif ApprovalCheck(JubesX,700, "O"):
                                                $ JubesX.Statup("Love", 200, -5)
                                                $ JubesX.Statup("Obed", 200, 10)
                                                ch_v "Хмммм. . ."
                                        else: #if it failed both those things,
                                                $ JubesX.Statup("Love", 200, -10)
                                                $ JubesX.Statup("Obed", 90, -10)
                                                $ JubesX.Statup("Obed", 200, -10)
                                                $ JubesX.Statup("Inbt", 50, -15)
                                                $ JubesX.FaceChange("angry", 1)
                                                ch_v "Эм, это немного перебор. . ."
                                                $ Line = "rude"
                                "Ладно, тогда не бери в голову.":
                                                $ JubesX.FaceChange("angry", 1)
                                                $ JubesX.Statup("Love", 200, -10)
                                                $ JubesX.Statup("Obed", 90, -10)
                                                $ JubesX.Statup("Obed", 200, -10)
                                                $ JubesX.Statup("Inbt", 50, -15)
                                                ch_v "Мда."
                                                ch_v "Я ожидала от тебя большего."
                                                $ Line = "rude"

        $ JubesX.RecentActions.append("asked sub")
        $ JubesX.DailyActions.append("asked sub")
        if Line == "rude":
                #If line hasn't been set to "rude" by something above, then it skips right past this
                hide Jubes_Sprite with easeoutright
                call Remove_Girl(JubesX)
                $ JubesX.RecentActions.append("angry")
                if "Historia" not in Player.Traits:
                        $ renpy.pop_call()
                "[JubesX.Name] выходит из комнаты."
        elif "sir" in JubesX.Petnames:
                #it didn't fail and "sir" was covered
                $ JubesX.Statup("Obed", 200, 50)
                $ JubesX.Petnames.append("master")
                if not Player.Male:
                    $ JubesX.Petname = "хозяйка"
                    $ JubesX.Petname_rod = "хозяйки"
                    $ JubesX.Petname_dat = "хозяйке"
                    $ JubesX.Petname_vin = "хозяйку"
                    $ JubesX.Petname_tvo = "хозяйкой"
                    $ JubesX.Petname_pre = "хозяйке"
                else:
                    $ JubesX.Petname = "хозяин"
                    $ JubesX.Petname_rod = "хозяина"
                    $ JubesX.Petname_dat = "хозяину"
                    $ JubesX.Petname_vin = "хозяина"
                    $ JubesX.Petname_tvo = "хозяином"
                    $ JubesX.Petname_pre = "хозяине"
                $ JubesX.Eyes = "sly"
                if not Player.Male:
                    ch_v ". . . хозяйка. . ."
                else:
                    ch_v ". . . хозяин. . ."
        else:
                #it didn't fail
                $ JubesX.Statup("Obed", 200, 30)
                $ JubesX.Petnames.append("sir")
                if not Player.Male:
                    $ JubesX.Petname = "госпожа"
                    $ JubesX.Petname_rod = "госпожи"
                    $ JubesX.Petname_dat = "госпоже"
                    $ JubesX.Petname_vin = "госпожу"
                    $ JubesX.Petname_tvo = "госпожой"
                    $ JubesX.Petname_pre = "госпоже"
                else:
                    $ JubesX.Petname = "господин"
                    $ JubesX.Petname_rod = "господина"
                    $ JubesX.Petname_dat = "господину"
                    $ JubesX.Petname_vin = "господина"
                    $ JubesX.Petname_tvo = "господином"
                    $ JubesX.Petname_pre = "господине"
                $ JubesX.FaceChange("sly", 1)
                if not Player.Male:
                    ch_v ". . . госпожа."
                else:
                    ch_v ". . . господин."
        return

# end Jubes_Sub//////////////////////////////////////////////////////////



# start Jubes_Master//////////////////////////////////////////////////////////
#master

label Jubes_Master:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(JubesX,"bemused","выглядит необычайно покорной. . .")
                return
        call Shift_Focus(JubesX)
        if JubesX.Loc != bg_current:
            $ JubesX.Loc = bg_current
            if JubesX not in Party:
                "[JubesX.Name] подходит к вам и жестом показывает, что хочет поговорить с вами наедине."
            else:
                "[JubesX.Name] поворачивается к вам и жестом показывает, что хочет поговорить с вами наедине."
        $ Event_Queue = [0,0]
        $ JubesX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene(0)
        call Display_Girl(JubesX)
        call Taboo_Level
        call CleartheRoom(JubesX)
        $ JubesX.DailyActions.append("relationship")
        $ Line = 0
        $ JubesX.FaceChange("sadside",1)
        ch_v "[JubesX.Petname]?"
        ch_v "Я кое о чем думала прошлой ночью."
        $ JubesX.FaceChange("sly", 1)
        ch_v "И я хотела бы рассказать тебе об этом."
        menu:
            extend ""
            "Давай.":
                    $ JubesX.Statup("Love", 90, 2)
                    $ JubesX.Statup("Obed", 200, 2)
            "Ладно.":
                    $ JubesX.Statup("Obed", 200, 3)
            "Это может подождать?":
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.Statup("Obed", 200, 2)
                    $ JubesX.FaceChange("angry", 1)
                    ch_v "Нет!"
                    $ JubesX.FaceChange("sly", 1)
                    ch_v "Выслушай меня, думаю, тебе понравится."
            "О, я тоже [[вместо этого рассказать свою историю].":
                    $ JubesX.Statup("Love", 200, -5)
                    if not Player.Male:
                        ch_p "Так вот, была я значит в Комнате Оп-"
                    else:
                        ch_p "Так вот, был я значит в Комнате Оп-"
                    $ JubesX.ArmPose = 1
                    $ JubesX.FaceChange("angry", 1,Eyes="closed")
                    "Она прикладывает палец к вашим губам."
                    $ JubesX.ArmPose = 2
                    $ JubesX.FaceChange("sly", 1)
                    $ JubesX.Statup("Inbt", 80, 3)
                    ch_v "На этом я остановлю тебя."
                    ch_v "Ага."
                    ch_v "Пришло время закончить мой рассказ."
        ch_v "Это произошло, когда я еще была с вампирами, до того, как меня спасли от них."
        if "boyfriend" in JubesX.Petnames:
                #if you've done the boyfriend story aready, she told you about Xarus
                ch_v "Помнишь, я говорила, что Ксарус обратил меня?"
                menu:
                    "Да?":
                            $ JubesX.Statup("Love", 200, 3)
                            $ JubesX.Statup("Obed", 200, 3)
                            $ JubesX.FaceChange("sly", 1)
                            ch_v "Хорошо, так вот. . ."
                    "Не особо.":
                            $ JubesX.Statup("Love", 200, -5)
                            ch_v "Не помнишь? Парень по имени Ксарус обратил меня? Сын Дракулы?"
                            menu:
                                extend ""
                                "Я думала, что сына Дракулы зовут \"Алукард.\"" if not Player.Male:
                                        if "Alucard" in JubesX.History:
                                                $ JubesX.Statup("Love", 200, -5)
                                                $ JubesX.FaceChange("angry", 1,Mouth="open")
                                                ch_v "Мы больше не будем это обсуждать!"
                                        else:
                                                $ JubesX.FaceChange("confused")
                                                $ JubesX.Statup("Love", 90, -3)
                                                $ JubesX.Statup("Obed", 80, 1)
                                                ch_v "Что? Типа \"Дракула\" наоб-"
                                                ch_v "Неважно, вернемся к рассказу!"
                                        $ JubesX.FaceChange("angry", 1)
                                "Я думал, что сына Дракулы зовут \"Алукард.\"" if Player.Male:
                                        if "Alucard" in JubesX.History:
                                                $ JubesX.Statup("Love", 200, -5)
                                                $ JubesX.FaceChange("angry", 1,Mouth="open")
                                                ch_v "Мы больше не будем это обсуждать!"
                                        else:
                                                $ JubesX.FaceChange("confused")
                                                $ JubesX.Statup("Love", 90, -3)
                                                $ JubesX.Statup("Obed", 80, 1)
                                                ch_v "Что? Типа \"Дракула\" наоб-"
                                                ch_v "Неважно, вернемся к рассказу!"
                                        $ JubesX.FaceChange("angry", 1)
                                "Хм, ладно.":
                                        $ JubesX.FaceChange("angry", 1)
                                        ch_v "Жаль, что ты не помнишь этого."

                    "Кто?":
                            $ JubesX.Statup("Love", 200, -5)
                            $ JubesX.FaceChange("angry", 1)
                            ch_v "Не парься, это не важно."
                            $ JubesX.FaceChange("normal", 1)
        ch_v "После того, как меня обратили, я почувствовала некое притяжение вдалеке."
        $ JubesX.FaceChange("sadside", 1)
        if "boyfriend" in JubesX.Petnames:
                ch_v "Это был Ксарус, он мог звать меня."
        else:
                ch_v "Это был вампир, который обратил меня, он мог звать меня."
        ch_v "По ночам я чувствовала нечто типа непрерывного потока, и, в конце концов, я позволила ему унести меня."
        ch_v "Я оказалась в каком-то заброшенном здании в центре города."
        ch_v "Оно было переделан в какой-то салон, смешанный с антикварным магазином."
        ch_v "Он был там, вместе со своим кланом."
        while "done" not in JubesX.RecentActions:
            menu:
                extend ""
                "Он был сексуальным?" if "hot" not in JubesX.RecentActions:
                        $ JubesX.AddWord(1,"hot",0,0,0) #adds "word" tag to Recent
                        $ JubesX.Statup("Inbt", 90, 5)
                        $ JubesX.Statup("Obed", 200, 2)
                        $ JubesX.FaceChange("perplexed", 2)
                        ch_v ". . ."
                        $ JubesX.FaceChange("sly", 1,Eyes="side")
                        ch_v "Думаю, в то время я так и считала."
                        $ JubesX.FaceChange("sly", 1)
                        ch_v "Но скорее всего это было связано с вампиризмом."
                        $ JubesX.Statup("Obed", 200, 2)
                        ch_v "Он тебе и в подметки не годится."
                "\"Гнездо.\"" if "nest" not in JubesX.RecentActions:
                        $ JubesX.AddWord(1,"nest",0,0,0) #adds "word" tag to Recent
                        $ JubesX.FaceChange("confused", 1)
                        ch_v "Что?"
                        menu:
                            extend ""
                            "Неважно.":
                                    $ JubesX.Statup("Love", 200, 2)
                                    $ JubesX.Statup("Obed", 200, 2)
                                    ch_v "Ладно. . ."
                            "Группа вампиров есть \"Гнездо.\"":
                                    $ JubesX.Statup("Love", 200, -3)
                                    $ JubesX.Statup("Obed", 200, 2)
                                    ch_p "\"Гнездо вампиров.\""
                                    ch_v "О, нет. . . "
                                    $ JubesX.Statup("Obed", 200, 2)
                                    $ JubesX.FaceChange("confused", 1,Eyes="side")
                                    ch_v "-ну, или просто они сами называли себя \"кланом\". . ."
                                    $ JubesX.Statup("Inbt", 80, -2)
                                    $ JubesX.Statup("Obed", 200, 3)
                                    ch_v "Пожалуй, вполне можно называть их и \"гнездом\. . ."
                        $ JubesX.FaceChange("sly", 1)
                ". . .":
                        $ JubesX.AddWord(1,"done",0,0,0) #adds "word" tag to Recent

                "Там были какие-нибудь дамочки?" if "ladies" not in JubesX.RecentActions:
                        $ JubesX.AddWord(1,"ladies",0,0,0) #adds "word" tag to Recent
                        $ JubesX.Statup("Love", 200, -3)
                        $ JubesX.Statup("Obed", 200, 3)
                        $ JubesX.FaceChange("confused", 1)
                        ch_v ". . ."
                        ch_v "Даааа. . . там были какие-то \"дамочки\". . ."
                        menu:
                            extend ""
                            "Хорошо, просто хотелось уточнить.":
                                    $ JubesX.Statup("Obed", 200, 1)
                                    ch_v "Ага, ладно."
                            "Сексуальные?":
                                    $ JubesX.Statup("Love", 80, -2)
                                    $ JubesX.Statup("Obed", 200, 5)
                                    $ JubesX.FaceChange("angry", 1)
                                    ch_v ". . ."
                                    $ JubesX.Statup("Inbt", 90, 5)
                                    $ JubesX.FaceChange("sly", 1)
                                    ch_v "Да."
                                    if "hot" in JubesX.RecentActions: #asked after Xarus
                                            ch_v "Да, вампирши тоже были довольно сексуальными."
                                    else:
                                            ch_v "Да, вампирши были довольно сексуальными."
                            "Ладно, мне все равно.":
                                    ch_v "Хорошо."
                        $ JubesX.FaceChange("sly", 1)
        #end "remember Xarus
        $ JubesX.DrainWord("done")
        $ JubesX.FaceChange("sly", 1,Eyes="side")
        ch_v "Я приходила туда ночами, и он искушал меня."
        ch_v "Искушал меня разными вещами. . ."
        menu:
            extend ""
            "Кровью?":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.Statup("Obed", 200, 2)
                    $ JubesX.FaceChange("sadside", 1)
                    ch_v "Иногда. . . "
                    ch_v "-не уверена, откуда он ее брал."
            "Например?":
                    $ JubesX.Statup("Obed", 200, 4)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("sadside", 1)
                    ch_v "Ох, иногда кровью. . ."
            ". . .":
                    $ JubesX.Statup("Love", 200, 2)
                    $ JubesX.Statup("Obed", 200, 2)
                    $ JubesX.Statup("Inbt", 80, 2)
            "Анальными утехами?":
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 70, 3)
                    $ JubesX.FaceChange("confused", 2)
                    ch_v ". . ."
                    $ JubesX.Statup("Inbt", 90, 5)
                    $ JubesX.FaceChange("angry", 1)
                    ch_v "Нет, такого он не пытался сделать."
            "Девушками?":
                    $ JubesX.Statup("Inbt", 200, 5)
                    $ JubesX.Statup("Obed", 200, 5)
                    $ JubesX.FaceChange("sly", 2,Eyes="side")
                    ch_v ". . . иногда, да."
        $ JubesX.FaceChange("sadside", 1)
        ch_v ". . . иногда красивыми подарками. . ."
        ch_v "Иногда возможностью совершить насилие. . ."
        ch_v "Я бродила во тьме. . ."
        ch_v "В конце концов, остальные выследили клан."
        $ JubesX.FaceChange("smile", 1,Eyes="closed")
        if "boyfriend" in JubesX.Petnames:
                ch_v "Они убили Ксаруса и освободили меня."
        else:
                ch_v "Они убили их всех, включая того, кто обратил меня, и освободили меня."
        $ JubesX.FaceChange("sad", 1,Eyes="closed")
        ch_v "Но. . ."
        menu:
            extend ""
            "Но. . ?":
                    $ JubesX.Statup("Love", 200, 2)
                    $ JubesX.Statup("Inbt", 90, 3)
                    $ JubesX.Statup("Obed", 200, 5)
                    $ JubesX.FaceChange("sad", 1)
                    ch_v "Но. . . я скучаю по некоторым моментам. . ."
            "Но тебе вроде как это нравилось?":
                    $ JubesX.Statup("Love", 200, 2)
                    $ JubesX.Statup("Inbt", 90, 3)
                    $ JubesX.Statup("Obed", 200, 10)
                    $ JubesX.FaceChange("sly", 2,Eyes="closed")
                    ch_v ". . ."
                    $ JubesX.FaceChange("sly", 1)
                    ch_v "Ага, немного. . ."
            ". . .":
                    $ JubesX.Statup("Inbt", 90, 7)
                    $ JubesX.Statup("Obed", 200, 5)
                    ch_v "Но. . . я скучаю по некоторым моментам. . ."
            "Но ты скучаешь по анальным утехам?":
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 200, 5)
                    $ JubesX.FaceChange("surprised", 2)
                    ch_v "!!!"
                    $ JubesX.Statup("Inbt", 90, 5)
                    $ JubesX.FaceChange("angry", 2)
                    ch_v "Я же сказала тебе, не было там никаких анальных утех!"
                    $ JubesX.Statup("Obed", 200, 3)
                    $ JubesX.FaceChange("angry", 1,Eyes="side")
                    ch_v "Но. . . по -кое-чему- я скучаю. . ."
            "Но ты скучаешь по девушкам?":
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Obed", 200, 3)
                    $ JubesX.FaceChange("confused", 1)
                    ch_v ". . ."
                    $ JubesX.Statup("Inbt", 90, 10)
                    $ JubesX.Statup("Obed", 200, 2)
                    $ JubesX.FaceChange("sly", 1,Eyes="side")
                    ch_v "Я немного скучаю по ним, они были не так уж плохи."
                    $ JubesX.Statup("Obed", 200, 3)
                    ch_v "Но. . . в основном я скучаю по -другим- моментам. . ."
        $ JubesX.FaceChange("sly", 1)
        ch_v "Я скучаю по \"притяжению\". . ."
        ch_v "По некому чувство, что заставляло меня выполнять чужие приказы. . ."
        $ JubesX.FaceChange("sly", 1,Eyes="side")
        ch_v "В этом было что-то поистине замечательное. . ."
        ch_v "И мне этого не хватало."
        $ JubesX.FaceChange("sly", 1)
        ch_v "Пока я не встретила тебя."
        ch_v "Теперь я снова обрела это чувство. . ."
        ch_v ". . . если ты попросишь меня о чем-нибудь. . ."
        ch_v ". . . я это сделаю."
        menu:
            extend ""
            "Значит ты хочешь, чтобы я была твоей хозяйкой." if not Player.Male:
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Obed", 70, 5)
                    $ JubesX.AddWord(1,"asked",0,0,0) #adds "word" tag to Recent
                    ch_v "Да."
            "Значит ты хочешь, чтобы я была твоим хозяином." if Player.Male:
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Obed", 70, 5)
                    $ JubesX.AddWord(1,"asked",0,0,0) #adds "word" tag to Recent
                    ch_v "Да."
            "И чего ты хочешь?":
                    $ JubesX.Statup("Inbt", 90, 3)
                    $ JubesX.Statup("Obed", 200, 10)
                    ch_v "Я хочу. . ."
            "Согласилась бы даже на анальные утехи?":
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Inbt", 90, 3)
                    $ JubesX.Statup("Obed", 200, 2)
                    $ JubesX.FaceChange("angry", 1,Eyes="side")
                    ch_v ". . ."
                    $ JubesX.FaceChange("sly", 1)
                    ch_v "Да. . . -даже- на анальные утехи. . ."
                    "[[дисклеймер] \"анальных утех\", пенетрейшена вагинального, кисочно-хуевых ласк с Джубили эта версия игры не имеет."
                    "Все это будет позже, обещаем."
                    ". . ."
                    "Хотя нет, все это уже есть в игре, наслаждайтесь."
            ". . .":
                    $ JubesX.Statup("Inbt", 90, 3)
                    $ JubesX.Statup("Obed", 200, 3)
                    ch_v "Я хочу. . ."
            "Клево.":
                    $ JubesX.Statup("Love", 200, -3)
                    $ JubesX.Statup("Inbt", 80,-30)
                    $ JubesX.FaceChange("confused", 1)
                    ch_v "Ага. . . эм. . . ладно. . ."
                    $ JubesX.FaceChange("sly", 1)
        menu:
            extend ""
            "Скажи это.":
                    $ JubesX.Statup("Inbt", 60, 3)
                    $ JubesX.Statup("Inbt", 90, 3)
                    $ JubesX.Statup("Obed", 200, 10)
                    if not Player.Male:
                        ch_v "Я хочу, чтобы ты стала моей хозяйкой."
                    else:
                        ch_v "Я хочу, чтобы ты стал моим хозяином."
            "Попроси вежливо.":
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Obed", 200, 15)
                    $ JubesX.FaceChange("sly", 2)
                    if not Player.Male:
                        ch_v ". . . пожалуйста, стань моей хозяйкой."
                    else:
                        ch_v ". . . пожалуйста, стань моим хозяином."
            ". . .":
                    $ JubesX.Statup("Inbt", 60, 3)
                    $ JubesX.Statup("Inbt", 90, 4)
                    $ JubesX.Statup("Obed", 200, 5)
                    if not Player.Male:
                        ch_v "Я хочу, чтобы ты стала моей хозяйкой."
                    else:
                        ch_v "Я хочу, чтобы ты стал моим хозяином."
            "Ага, ладно." if "asked" not in JubesX.RecentActions:
                    $ JubesX.FaceChange("confused", 1)
                    ch_v "Я даже не сказала, чего хочу."
                    menu:
                        extend ""
                        "Ты хочешь, чтобы я стала твоей хозяйкой, правильно?" if not Player.Male:
                                $ JubesX.Statup("Love", 80, 5)
                                $ JubesX.Statup("Love", 200, 3)
                                $ JubesX.Statup("Obed", 200, 5)
                                ch_v ". . . ага."
                        "Ты хочешь, чтобы я стал твоим хозяином, правильно?" if Player.Male:
                                $ JubesX.Statup("Love", 80, 5)
                                $ JubesX.Statup("Love", 200, 3)
                                $ JubesX.Statup("Obed", 200, 5)
                                ch_v ". . . ага."
                        "О. Ну говори тогда.":
                                $ JubesX.Statup("Inbt", 60, 3)
                                $ JubesX.Statup("Inbt", 90, 4)
                                $ JubesX.Statup("Obed", 200, 5)
                                $ JubesX.FaceChange("sly", 1)
                                if not Player.Male:
                                    ch_v "Я хочу, чтобы ты стала моей хозяйкой."
                                else:
                                    ch_v "Я хочу, чтобы ты стал моим хозяином."

        $ JubesX.FaceChange("sly", 1)
        $ JubesX.History.append("master")
        menu:
            extend ""
            "Да.":
                    $ JubesX.Statup("Love", 80, 3)
                    $ JubesX.Statup("Love", 200, 3)
                    $ JubesX.Statup("Obed", 200, 10)
                    $ JubesX.Petnames.append("master")
                    if not Player.Male:
                        $ JubesX.Petname = "хозяйка"
                        $ JubesX.Petname_rod = "хозяйки"
                        $ JubesX.Petname_dat = "хозяйке"
                        $ JubesX.Petname_vin = "хозяйку"
                        $ JubesX.Petname_tvo = "хозяйкой"
                        $ JubesX.Petname_pre = "хозяйке"
                    else:
                        $ JubesX.Petname = "хозяин"
                        $ JubesX.Petname_rod = "хозяина"
                        $ JubesX.Petname_dat = "хозяину"
                        $ JubesX.Petname_vin = "хозяина"
                        $ JubesX.Petname_tvo = "хозяином"
                        $ JubesX.Petname_pre = "хозяине"
                    $ JubesX.FaceChange("smile", 1)
                    ch_v "!!!"
            "Эм. . . извини.":
                    $ JubesX.Statup("Love", 200, -3)
                    $ JubesX.Statup("Inbt", 200, -2)
                    $ JubesX.Statup("Obed", 200, 2)
                    $ JubesX.FaceChange("sad", 1,Eyes="surprised")
                    ch_v "Что-. . . почему?"
            "Ни за что.":
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Inbt", 200, -2)
                    $ JubesX.Statup("Obed", 200, 4)
                    $ JubesX.FaceChange("sad", 1,Eyes="surprised")
                    ch_v "Что-. . . почему?"

            "Ага, ладно.":
                    $ JubesX.Statup("Love", 200, -2)
                    $ JubesX.Statup("Inbt", 200, -2)
                    $ JubesX.Statup("Obed", 200, 12)
                    $ JubesX.Petnames.append("master")
                    if not Player.Male:
                        $ JubesX.Petname = "хозяйка"
                        $ JubesX.Petname_rod = "хозяйки"
                        $ JubesX.Petname_dat = "хозяйке"
                        $ JubesX.Petname_vin = "хозяйку"
                        $ JubesX.Petname_tvo = "хозяйкой"
                        $ JubesX.Petname_pre = "хозяйке"
                    else:
                        $ JubesX.Petname = "хозяин"
                        $ JubesX.Petname_rod = "хозяина"
                        $ JubesX.Petname_dat = "хозяину"
                        $ JubesX.Petname_vin = "хозяина"
                        $ JubesX.Petname_tvo = "хозяином"
                        $ JubesX.Petname_pre = "хозяине"
                    $ JubesX.FaceChange("confused", 1)
                    ch_v "Эм. . . клево."
                    ch_v "Клево."
                    $ JubesX.FaceChange("sly", 1)

        if JubesX.Petname == "хозяйка":
                $ JubesX.Statup("Obed", 200, 30)
                ch_v ". . .  хозяйка."
                return
        if JubesX.Petname == "хозяин":
                $ JubesX.Statup("Obed", 200, 30)
                ch_v ". . . хозяин."
                return
        menu:
            extend ""
            "Я не хочу, чтобы ты так меня звала.":
                    $ JubesX.Statup("Love", 80, 3)
                    $ JubesX.Statup("Love", 200, 5)
                    $ JubesX.Statup("Obed", 200, 5)
                    ch_v "Ладно, мне не обязательно так к тебе обращаться. . ."
                    $ JubesX.Statup("Inbt", 90, 3)
                    $ JubesX.FaceChange("sly", 1)
                    if not Player.Male:
                        ch_v "Но не могла бы ты. . . немного -принуждать- меня?"
                    else:
                        ch_v "Но не мог бы ты. . . немного -принуждать- меня?"
                    menu:
                        extend ""
                        "Конечно.":
                                $ JubesX.Statup("Love", 200, 5)
                                $ JubesX.Statup("Obed", 200, 10)
                                $ JubesX.Statup("Inbt", 90, 5)
                                $ JubesX.Petnames.append("master")
                                ch_v "Клево. . ."
                        "Нет, это странная херня.":
                                $ JubesX.Statup("Love", 90, -5)
                                $ JubesX.Statup("Inbt", 90, -2)
                                $ JubesX.Statup("Obed", 200, 5)
                                $ JubesX.FaceChange("angry", 2)
                                ch_v "Нууу. . . это было грубо!"
                        "Да, наверное. . .":
                                $ JubesX.Statup("Love", 200, 3)
                                $ JubesX.Statup("Inbt", 90, 2)
                                $ JubesX.Petnames.append("master")
                                $ JubesX.FaceChange("confused", 1)
                                ch_v "Клево. . ."
                                $ JubesX.FaceChange("sly", 1)
            "Это нездоровая херня.":
                    $ JubesX.Statup("Love", 90, -5)
                    $ JubesX.Statup("Inbt", 90, -2)
                    $ JubesX.Statup("Obed", 200, 5)
                    $ JubesX.FaceChange("angry", 2)
                    ch_v "Нууу. . . это было грубо!"
            "Мне это не нравится.":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 200, 5)
                    $ JubesX.FaceChange("sadside", 1)
                    ch_v "Ладно. . . хорошо."
        if  "master" not in JubesX.Petnames:
                #if you never agree to it. . .
                $ JubesX.RecentActions.append("angry")
                hide Jubes_Sprite with easeoutright
                call Remove_Girl(JubesX)
                if "Historia" not in Player.Traits:
                        $ renpy.pop_call()
                "[JubesX.Name] выбегает из комнаты."
                $ JubesX.FaceChange("normal", 1)
        return

# end Jubes_Master//////////////////////////////////////////////////////////


# start Jubes_Sexfriend//////////////////////////////////////////////////////////

label Jubes_Sexfriend:   #Jubes_Update
        #set this to occur after class
        $ Event_Queue = [0,0]
        if not Player.Male and "girltalk" not in JubesX.History:
                call expression JubesX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        $ JubesX.Lust = 70
        call Set_The_Scene
        "Вы чувствуете, как сзади вас кто-то обнимает и начинает целовать вашу шею."
        "Затем вы чувствуете острые зубы, которые медленно двигаются к вашему горлу."
        $ JubesX.FaceChange("sly",1)
        menu:
            "Отталкнуть ее":
                    $ JubesX.Statup("Love", 90, -5)
                    $ JubesX.Statup("Obed", 80, 5)
                    $ JubesX.Statup("Inbt", 200, -5)
                    ch_v "Оу, с тобой совсем не весело. . ."
            "Отдаться моменту":
                    $ JubesX.Statup("Love", 90, 3)
                    $ JubesX.Statup("Inbt", 200, 5)
                    ch_v "Не волнуйся. . . Я не буду кусаться. . ."
                    "Ее руки скользят вниз по вашему телу, прямиком в ваши штаны. . ."
                    if not Player.Male:
                            "Она касается вашей киски, поворачиваясь к вам лицом."
                    else:
                            "Она берет ваш член в свою руку, поворачиваясь к вам лицом."
        $ JubesX.Loc = bg_current
        $ JubesX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(JubesX)
        call Set_The_Scene
        $ JubesX.DailyActions.append("relationship")
        call Taboo_Level
        $ Line = 0
        ch_v "Я просто подумала. . . зачем нам сдерживаться?"
        ch_v "Мы можем немного повеселиться. . ."

        if JubesX in Player.Harem:
                ch_v "Я знаю, что теперь мы \"вместе\" и все такое. . ."
        if "master" in JubesX.Petnames  or "sir" in JubesX.Petnames:
                #if you have done the lover thing
                ch_v ". . . ты всегда получаешь удовлетворение своих потребностей. . ."
        ch_v ". . . Я лишь хочу убедиться, что мы не потеряем. . ."
        $ JubesX.Petnames.append("sex friend")
        $ JubesX.FaceChange("smile",1,Mouth="open")
        $ JubesX.ArmPose = 1
        show Fireworks onlayer black as Fire1:
                pos (JubesX.SpriteLoc+300,350)#+160,270)
        show Fireworks onlayer black as Fire2:
                pos (JubesX.SpriteLoc+300,350)
        ch_v "искру."
        $ JubesX.FaceChange("sly",1)
        $ JubesX.ArmPose = 2
        if not Player.Male:
            ch_v "Я хочу отлизать твою. . . ну, ты понимаешь."
        else:
            ch_v "Я хочу отсосать твой. . . ну, ты понимаешь."
        menu:
            extend ""
            "Не сейчас":
                    $ JubesX.Statup("Love", 200, -10)
                    $ JubesX.Statup("Obed", 90, 15)
                    $ JubesX.Statup("Inbt", 90, 10)
                    $ JubesX.FaceChange("sad",2)
                    ch_v "Оу. . . облом."
                    ch_v "Дай мне знать, если передумаешь."
                    $ JubesX.FaceChange("sadside",1)
                    if Player.Harem:
                            ch_v "Может, [Player.Harem[0].Name] готова к чему-нибудь. . ."
                            $ JubesX.GLG(Player.Harem[0],500,25,1)
                    else:
                            ch_v "Интересно, занята ли Роуг. . ."
                            $ JubesX.GLG("Rogue",500,25,1)
            "Конечно.":
                $ JubesX.Statup("Love", 90, 10)
                $ JubesX.Statup("Obed", 90, 5)
                $ JubesX.Statup("Inbt", 90, 15)
                $ JubesX.FaceChange("sly",1,Mouth="smile")
                if Taboo:
                    ch_v "Хорошо, пошли. . ."
                    menu:
                        extend ""
                        "Ага":
                                ch_v "Отлично."
                                if bg_current == "bg player":
                                        $ bg_current = "bg jubes"
                                else:
                                        $ bg_current = "bg player"
                                $ JubesX.Loc = bg_current
                                $ Party = []
                                call Set_The_Scene
                                call CleartheRoom(JubesX)
                                call Set_The_Scene
                                $ Taboo = 0
                                $ JubesX.Taboo = 0

                        "Нет, давай здесь.":
                                $ JubesX.Statup("Obed", 80, 5)
                                $ JubesX.Statup("Inbt", 90, 15)
                                ch_v "Ooo. . . ладно."

                $ Situation = JubesX
                $ Player.AddWord(1,"interruption") #adds to Recent
                if Player.Male:
                        call Girl_BJ_Prep              #she offers sex
                else:
                        call Girl_CUN_Prep
                call SexMenu
                jump Misplaced

                #end "if no relationship"

        return

# end Jubes_Sexfriend//////////////////////////////////////////////////////////


# start Jubes_Fuckbuddy//////////////////////////////////////////////////////////

label Jubes_Fuckbuddy:
        $ JubesX.DailyActions.append("relationship")
        $ JubesX.Lust = 80
        $ JubesX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        # Conditions, in your room, jubes not there.
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(JubesX,"sly","выглядит взволнованной. . .")
                return
        #change jubes's outfit to default
        $ Event_Queue = [0,0]
        call Shift_Focus(JubesX)
        call Set_The_Scene(0)
        $ JubesX.Outfit = "casual2"
        $ JubesX.OutfitDay = "casual2"
        $ JubesX.OutfitChange("casual2")
        if JubesX.Loc != bg_current:
                "Вы слышите стук в дверь, после чего идете открывать."
                "[JubesX.Name] стоит прямо за дверью, и, как только вы открываете ее, она врывается в комнату."
        else:
                "[JubesX.Name] поворачивается к вам с голодными глазами."
        $ JubesX.Loc = bg_current
        call Display_Girl(JubesX)
        call Taboo_Level

        $ JubesX.FaceChange("sly",2)
        $ JubesX.Petnames.append("fuck buddy")
        $ JubesX.Event[10] += 1
        $ Situation = JubesX

        "Она толкает вас на кровать и срывает с вас штаны."
        $ Player.AddWord(1,"cockout",0,0,0)
        menu:
            "Остановить ее":
                    $ JubesX.Statup("Love", 90, -5)
                    $ JubesX.Statup("Obed", 90, 10)
                    "Вы хватаете ее за плечи и отталкиваете, снова натягивая штаны."
                    $ JubesX.FaceChange("sad",2)
                    ch_v "Ох."
                    $ JubesX.FaceChange("sadside",2)
                    ch_v "Извини. . ."
                    $ JubesX.Statup("Inbt", 200, 5)
                    ch_v "Я просто, эм. . ."
                    $ JubesX.Statup("Inbt", 200, 5)
                    if not Player.Male:
                        ch_v "-Очень- хотела отлизать тебе, понимаешь?"
                    else:
                        ch_v "-Очень- хотела отсосать тебе, понимаешь?"
                    menu:
                        extend ""
                        "О, тогда ладно.":
                                $ JubesX.FaceChange("smile",1)
                                $ JubesX.Statup("Love", 90, 5)
                                $ JubesX.Statup("Obed", 80, 5)
                                $ JubesX.Statup("Inbt", 200, 5)
                                ch_v "Отлично. . . "
                        "Прекрати.":
                                $ JubesX.Statup("Love", 90, -5)
                                $ JubesX.Statup("Obed", 90, 5)
                                $ JubesX.FaceChange("sad",2)
                                ch_v "Ох."
                                $ JubesX.FaceChange("sadside",1)
                                ch_v "Ладно."
                                $ JubesX.FaceChange("sad",2,Mouth="smile")
                                ch_v "Только имейте в виду, что для тебя я всегда свободна."
                                $ JubesX.Statup("Inbt", 200, 10)
                                ch_v "Тебе стоит лишь позвать. . ."
                                $ JubesX.RecentActions.append("angry")
                                hide Jubes_Sprite with easeoutright
                                call Remove_Girl(JubesX)
                                if "Historia" not in Player.Traits:
                                        $ renpy.pop_call()
                                "[JubesX.Name] выбегает из комнаты."
                                $ JubesX.FaceChange("normal",1)
                                return

            "Посмотрим, к чему это приведет":
                    $ JubesX.Statup("Inbt", 200, 30)

        $ MultiAction = 0
        if Player.Male:
                call Jubes_BJ_Launch
                "Она опускается на колени и обхватывает губами ваш член."
                $ Speed = 3
                call SexAct("blow") # call Jubes_SexAct("blow")
        else:
                call Jubes_CUN_Launch
                "Она опускается на колени и обхватывает губами ваш клитор."
                $ Speed = 3
                call SexAct("blow") # call Jubes_SexAct("blow")
        $ MultiAction = 1
        if "swallowed" in JubesX.RecentActions:
                $ JubesX.FaceChange("smile",1)
                ch_v "Ммм, это было приятно. . ."
                ch_v "Я просто не могу насытиться. . ."
        ch_v "Имей в виду, что для тебя я всегда свободна."
        ch_v "Тебе стоит лишь позвать. . ."
        return

# end Jubes_Fuckbuddy//////////////////////////////////////////////////////////

# start Jubes_Daddy//////////////////////////////////////////////////////////


label Jubes_Daddy:       #Jubes_Update
        $ JubesX.DailyActions.append("relationship")
        $ JubesX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(JubesX)
        if JubesX.Loc != bg_current:
                $ JubesX.Loc = bg_current
                "[JubesX.Name] подходит к вам."
        call Set_The_Scene
        $ Event_Queue = [0,0]
        ch_v ". . ."
        if JubesX in Player.Harem:
            ch_v "Слушай, ты ведь в курсе, что мы уже некоторое время встречаемся?"
        else:
            ch_v "Слушай, мы ведь весело проводим время, правда?"
        ch_v "На днях я посмотрела кое-какое шоу, и. . ."
        ch_v ". . . тебе бы понравилось, если бы я звала тебя. . ."
        if not Player.Male:
            ch_v "\"Мамочкой?\""
        else:
            ch_v "\"Папочкой?\""
        menu:
            extend ""
            "Конечно.":
                $ JubesX.FaceChange("smile")
                $ JubesX.Statup("Love", 90, 20)
                $ JubesX.Statup("Obed", 60, 10)
                $ JubesX.Statup("Inbt", 80, 30)
                ch_v "Клево."
            "Что ты имеешь в виду?":
                $ JubesX.FaceChange("bemused")
                ch_v "Ох! Эм, я услышала это в том шоу, понимаешь?"
                ch_v "И мне показалось, что. . ."
                if JubesX.Love > JubesX.Obed and JubesX.Love > JubesX.Inbt:
                    ch_v "Это было бы мило, правда?"
                else:
                    ch_v "Это было бы довольно сексуально, правда?"

                menu:
                    extend ""
                    "Звучит интересно, мне нравится.":
                            $ JubesX.FaceChange("smile")
                            $ JubesX.Statup("Love", 90, 15)
                            $ JubesX.Statup("Obed", 60, 20)
                            $ JubesX.Statup("Inbt", 80, 25)
                            ch_v "Отлично."
                            $ JubesX.FaceChange("sly",2)
                            if not Player.Male:
                                ch_v " . . . мамочка."
                            else:
                                ch_v " . . . папочка."
                            $ JubesX.FaceChange("sly",1)
                            if not Player.Male:
                                $ JubesX.Petname = "мамочка"
                                $ JubesX.Petname_rod = "мамочки"
                                $ JubesX.Petname_dat = "мамочке"
                                $ JubesX.Petname_vin = "мамочку"
                                $ JubesX.Petname_tvo = "мамочкой"
                                $ JubesX.Petname_pre = "мамочке"
                            else:
                                $ JubesX.Petname = "папочка"
                                $ JubesX.Petname_rod = "папочки"
                                $ JubesX.Petname_dat = "папочке"
                                $ JubesX.Petname_vin = "папочку"
                                $ JubesX.Petname_tvo = "папочкой"
                                $ JubesX.Petname_pre = "папочке"
                    "Прошу, не надо.":
                            $ JubesX.Statup("Love", 90, 5)
                            $ JubesX.Statup("Obed", 80, 40)
                            $ JubesX.Statup("Inbt", 80, 20)
                            $ JubesX.FaceChange("sad")
                            ch_v ". . ."
                            ch_v "Хорошо."
                            $ JubesX.FaceChange("angry")
                            ch_v "Зануда."
                            $ JubesX.FaceChange("sad")
                    "У тебя были непростые отношения с матерью, да?" if not Player.Male:
                            $ JubesX.Statup("Love", 90, -15)
                            $ JubesX.Statup("Obed", 80, 45)
                            $ JubesX.Statup("Inbt", 70, 5)
                            $ JubesX.FaceChange("surprised",2)
                            ch_v "Я. . ."
                            $ JubesX.FaceChange("angry",1)
                            ch_v "Нет!"
                    "У тебя были непростые отношения с отцом, да?" if Player.Male:
                            $ JubesX.Statup("Love", 90, -15)
                            $ JubesX.Statup("Obed", 80, 45)
                            $ JubesX.Statup("Inbt", 70, 5)
                            $ JubesX.FaceChange("surprised",2)
                            ch_v "Я. . ."
                            $ JubesX.FaceChange("angry",1)
                            ch_v "Нет!"
            "У тебя были непростые отношения с матерью, да?" if not Player.Male:
                    $ JubesX.Statup("Love", 90, -15)
                    $ JubesX.Statup("Obed", 80, 45)
                    $ JubesX.Statup("Inbt", 70, 5)
                    $ JubesX.FaceChange("surprised",2)
                    ch_v "Я. . ."
                    $ JubesX.FaceChange("angry",1)
                    ch_v "Нет!"
            "У тебя были непростые отношения с отцом, да?" if Player.Male:
                    $ JubesX.Statup("Love", 90, -15)
                    $ JubesX.Statup("Obed", 80, 45)
                    $ JubesX.Statup("Inbt", 70, 5)
                    $ JubesX.FaceChange("surprised",2)
                    ch_v "Я. . ."
                    $ JubesX.FaceChange("angry",1)
                    ch_v "Нет!"
        $ JubesX.Petnames.append("daddy")
        return

# end Jubes_Daddy//////////////////////////////////////////////////////////


# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        if "switched" in JubesX.History:
                jump Jubes_Switch2
        $ JubesX.FaceChange("smile", 1)
        ch_v "Эм, привет?"
        ch_v "Ты выглядишь знакомо. . ."
        menu:
            extend ""
            "Это я, [Player.XName].":
                    $ JubesX.FaceChange("confused", 1)
                    ch_v "Что?"
                    $ JubesX.FaceChange("surprised", 1)
                    ch_v "Ох!"
                    $ JubesX.FaceChange("smile", 1)
                    ch_v "Ого, тебя прямо не узнать."
                    $ JubesX.AddWord(1,"switch") #recent

            "Тебе кажется.":
                    ch_v "Ох, ладно. Кстати, я [JubesX.Name]."
            "Может, мы встречались?":
                    ch_v "Меня зовут [JubesX.Name], тебе знакомо мое имя?"

        if "switch" not in JubesX.RecentActions:
                    $ JubesX.FaceChange("confused", 1)
                    ch_v ". . ."
                    ch_v "Серьезно, ты выглядишь очень знакомо. . ."
                    $ JubesX.FaceChange("surprised", 1)
                    ch_v "Подожди-ка. . ."
                    ch_v "Ты [Player.XName]!"
                    $ JubesX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Ага, это я, [Player.XName].":
                                $ JubesX.Statup("Love", 90, 1)
                                $ JubesX.Statup("Obed", 70, 1)
                                ch_v "Ох!"
                                $ JubesX.FaceChange("smile", 1)
                                ch_v "Ого, такие перемены."
                        "Нет.":
                                $ JubesX.FaceChange("angry", 1)
                                $ JubesX.Statup("Obed", 60, 1)
                                $ JubesX.Statup("Obed", 70, 1)
                                ch_v "Я же вижу, что это ты, [Player.XName]."
                        "Возможно?":
                                $ JubesX.FaceChange("sly", 1)
                                $ JubesX.Statup("Love", 80, 1)
                                $ JubesX.Statup("Obed", 70, 1)
                                $ JubesX.Statup("Inbt", 60, 1)
                                ch_v "Ага, это ты, [Player.XName]."
                    ch_v "Зачем ты так шифруешься?"
                    menu:
                        extend ""
                        "Извини, хотелось пошутить.":
                                $ JubesX.FaceChange("sly", 1)
                                $ JubesX.Statup("Love", 70, 1)
                                ch_v "Угу-м. . ."
                        "Молодец, ты меня раскусила.":
                                $ JubesX.FaceChange("sly", 1)
                                $ JubesX.Statup("Obed", 70, 1)
                                $ JubesX.Statup("Inbt", 80, 1)
                                ch_v "Хех, ага. . ."
                        "Хех.":
                                $ JubesX.FaceChange("sly", 1,Eyes="side")
                                $ JubesX.Statup("Love", 70, 1)
                                $ JubesX.Statup("Love", 90, 1)
                                $ JubesX.Statup("Inbt", 70, 1)
                                ch_v "Ахаха. . ."
                    ch_v "В свое время меня пытались запутать летучие мыши."
        #end "tried to lie"
        $ JubesX.FaceChange("smile", 1)
        ch_v "А к чему все эти. . . перемены?"
        menu:
            extend ""
            "Да так, по приколу.":
                    $ JubesX.Statup("Inbt", 70, 1)
                    $ JubesX.FaceChange("surprised", 2)
                    ch_v "Хех, понимаю. . ."
                    $ JubesX.FaceChange("sly", 1)
            "Я так себя сейчас ощущаю.":
                    ch_v "Понимаю."
            "У меня не было каких-то особых причин.":
                    ch_v "Ну ладно, дело твое. . ."

        if [Player.Name] != [Player.XName]:
                ch_p "А еще теперь меня зовут [Player.Name]."
                ch_v "Ладно, приятно снова познакомиться, [Player.Name]."

        if JubesX.SEXP >= 15:
                $ JubesX.FaceChange("sad", 1,Mouth="smile")
                ch_v ". . . мы все еще будем. . . проводить время вместе?"
                menu:
                    extend ""
                    "Конечно!":
                            $ JubesX.FaceChange("smile", 1)
                            $ JubesX.Statup("Love", 70, 2)
                            $ JubesX.Statup("Love", 90, 1)
                            ch_v "Отлично. . ."
                    "Я так не думаю.":
                            $ JubesX.FaceChange("sad", 1)
                            $ JubesX.Statup("Love", 80, -2)
                            $ JubesX.Statup("Obed", 60, 2)
                            $ JubesX.Statup("Obed", 80, 2)
                            ch_v "Ох. . ."
                            $ JubesX.FaceChange("sadside", 1)
                            ch_v "Ладно. . ."
                    "А ты как думаешь?":
                            $ JubesX.FaceChange("sly", 1)
                            $ JubesX.Statup("Obed", 70, 1)
                            $ JubesX.Statup("Inbt", 70, 1)
                            ch_v "Я думаю, что ты не сможешь устоять передо мной."

        if not Player.Male and JubesX.Les > 5:
                $ JubesX.FaceChange("sly", 1)
                ch_v "Мне всегда хотелось попробовать что-то новое. . ."
        if ApprovalCheck(JubesX, 1500):
                ch_v "Думаю, я смогу привыкнуть к твоему новому обличию."
                $ JubesX.AddWord(1,0,0,0,"girltalk") #history
        else:
                $ JubesX.FaceChange("normal", 1,Eyes="side")
                ch_v "Мне нужно немного времени, чтобы привыкнуть к тебе. . ."
        $ JubesX.Traits.remove("switchcheck")
        $ JubesX.AddWord(1,0,0,0,"switched") #history
        return

label Jubes_Switch2:
        #when you switch for a 2+ time
        $ JubesX.FaceChange("surprised", 1)
        ch_v "О!"
        $ JubesX.FaceChange("confused", 1)
        ch_v "Ты снова выглядишь как прежде. . ."
        $ JubesX.FaceChange("smile", 1)
        ch_v "Клево."
        $ JubesX.Traits.remove("switchcheck")
        $ JubesX.History.remove("switched")
        $ JubesX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_Girltalk(Auto=0,Other=0):
        # if Auto Jubes starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in JubesX.History:
                return
        if "nogirls" in JubesX.History:
                jump Jubes_Girltalk_Redux
        if Auto:
                $ JubesX.FaceChange("sadside", 2)
                ch_v "Эм, [Player.Name]. . ."
                ch_v ". . . я тебе нравлюсь?"
        else:
                $ JubesX.FaceChange("confused", 1)
                ch_v "А? Я тебе нравлюсь?"
        menu:
            extend ""
            "Да?":
                    $ JubesX.FaceChange("surprised", 2)
                    $ JubesX.Statup("Love", 70, 2)
                    $ JubesX.Statup("Love", 90, 2)
                    $ JubesX.Statup("Obed", 70, 1)
                    ch_v "Хм. . ."
                    $ JubesX.FaceChange("smile", 1, Eyes="side")
            "Наверное?":
                    $ JubesX.FaceChange("confused", 2)
                    $ JubesX.Statup("Obed", 80, 2)
                    $ JubesX.Statup("Inbt", 80, 2)
                    ch_v "Хех. . ."
                    $ JubesX.FaceChange("sly", 1)
            "Не особо.":
                    $ JubesX.FaceChange("sadside", 2)
                    $ JubesX.Statup("Love", 50, -2)
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 60, 2)
                    $ JubesX.Statup("Obed", 80, 2)
                    ch_v "Ох. . . ну понятно. . ."

        if not ApprovalCheck(JubesX, 1100) and not JubesX.Les:
                $ JubesX.FaceChange("sadside", 1)
                ch_v "Я не уверена. . . это как-то странно. . ."
                $ JubesX.AddWord(1,0,0,0,"nogirls") #history
                call Girltalk_Check(JubesX)
                return
        ch_v "Ладно. . ."
        ch_v "У меня, эм. . . у меня уже был опыт с девушкой ранее. . ."
        $ JubesX.FaceChange("sly", 1)
        ch_v "А ты ужасно привлекательна. . ."
        $ JubesX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(JubesX)
        return

label Jubes_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing
        if ApprovalCheck(JubesX, 1100):
                $ JubesX.FaceChange("sly", 1)
                if Other in TotalGirls and "nogirls" in Other.History:
                        ch_v "Я даже не знаю. . ."
                ch_v ". . . нууу, ты ужасно привлекательна. . ."
                $ JubesX.DrainWord("nogirls",0,0,0,1) #history
                $ JubesX.AddWord(1,0,0,0,"girltalk") #history
        elif "nogirls" not in JubesX.History:
                $ JubesX.AddWord(1,0,0,0,"nogirls") #history
                $ JubesX.FaceChange("sadside", 1)
                ch_v "Я не уверена. . . это как-то странно. . ."
        elif "nogirls" in JubesX.DailyActions:
                $ JubesX.FaceChange("angry", 1)
                if JubesX.Forced:
                        #if Forced, she will just go with it anyway
                        if "nogirls" not in JubesX.RecentActions:
                                $ JubesX.Statup("Love", 80, -2)
                                $ JubesX.Statup("Obed", 80, 2)
                                $ JubesX.AddWord(1,"nogirls",0,0,0) #recent
                        return
                ch_v "Дай мне немного пространства. . ."
        else:
                $ JubesX.Statup("Inbt", 50, 2)
                ch_v "Я уже говорила тебе, что не уверена, что хочу таких отношений. . ."
                $ JubesX.AddWord(1,0,"nogirls",0,0) #daily
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Jubes_69_Intro:
    return
