
# start GwenMeet//////////////////////////////////////////////////////////

label GwenMeet:
        # GwenX.Event[2] tracks number of times you've passed by, Oben adds 0-100 points based on how long you wait
        if "itsgwen" not in Player.History and "Gwentro" not in LauraX.History:
                $ GwenX.Name = "? ? ? "
        "Вы идете по коридору и вдруг слышите серию громких ударов."
        "-Бам-{w=0.2}{nw}" with vpunch
        if "closet" in Player.DailyActions:
            if GwenX.Event[2] < 5:
                menu:
                    "Продолжить свой путь":
                            #this can happen up to 5 times, then it will autoclear
                            "Вы идете дальше."
                            $ GwenX.Event[2] += 1
                            $ bg_current == "bg classroom"
                            return
                    "Остановиться и послушаться":
                            pass
            else:
                "Звуки становятся все громче."
        $ bg_current = "bg player"
        call Set_The_Scene(0,1) #shows Entryway
        "-Бух-{w=0.2}{nw}" with vpunch
        "-Буф-{w=0.2}{nw}" with vpunch
        "Похоже, звуки доносятся от двери с надписью \"Чулан.\""
        while "met" not in GwenX.History:
            menu:
                extend ""
                "Открыть дверь":
                        "Вы открываете дверь, оттуда выскакивает девушка и сбивает вас с ног." with vpunch
                        $ GwenX.History.append("met")

                "Спросить, есть ли там кто-нибудь.":
                        ch_p "Там кто-то есть?"
                        if GwenX.Event[5] == 5:
                                $ GwenX.Statup("Obed", 200, 5)
                                ch_g "Похоже, я попала во временную петлю, чувствую себя НИПом!"
                                $ GwenX.Event[5] += 1
                        elif "itsgwen" in Player.History:
                                ch_g "Я уже сказала тебе, что здесь я! Гвен!"
                                $ GwenX.Event[5] += 1
                        elif "itsme" in Player.History:
                                ch_g "Я уже сказала тебе, что здесь я! Гвен!"
                                if "itsgwen" not in Player.History:
                                        $ Player.History.append("itsgwen")
                                $ GwenX.Event[5] += 1
                        else:
                                ch_g "Я!"
                        $ Player.AddWord(1,"itsme") #recent
                        $ Player.History.append("itsme")

                "Кто?" if "itsme" in Player.History and "itsgwen" not in Player.History:
                        $ GwenX.Name = "Гвен"
                        $ GwenX.Name_rod = "Гвен"
                        $ GwenX.Name_dat = "Гвен"
                        $ GwenX.Name_vin = "Гвен"
                        $ GwenX.Name_tvo = "Гвен"
                        $ GwenX.Name_pre = "Гвен"
                        ch_g "Гвен!"
                        $ Player.History.append("itsgwen")

                "Просто уйти":
                        "Вы решаете продолжить свой путь."
                        if "itsme" in Player.RecentActions:
                                ch_g "Эй!"
                        elif "closet" in Player.DailyActions:
                                ch_g "Выпусти меня отсюда!"
                        elif "itsme" in Player.History:
                                ch_g "Эй! Я тебя слышу, выпусти меня!"
                        $ Player.AddWord(1,"closet","closet") #recent/daily
                        $ GwenX.Event[2] += 1
                        "-Бум-{w=0.2}{nw}" with vpunch
                        if GwenX.Event[2] < 5:
                                #this can happen up to 5 times, then it will autoclear
                                $ bg_current = "bg classroom"
                                return
                        "С последним ударом дверь открывается."
                        "Оттуда выскакивает девушка и сбивает вас с ног." with vpunch
                        $ GwenX.AddWord(1,"escape","escape") #recent/daily
                        $ GwenX.History.append("met")

        #she's out.
        if "itsme" in Player.History:
                $ Player.History.remove("itsme")
        if "itsgwen" in Player.History:
                $ Player.History.remove("itsgwen")
        $ GwenX.Event[5] = 0

        $ GwenX.History.append("Rogue") #sets up future intros
        $ GwenX.History.append("Kitty")
        $ GwenX.History.append("Emma")
        $ GwenX.History.append("Laura")
        $ GwenX.History.append("Jean")
        $ GwenX.History.append("Storm")
        $ GwenX.History.append("Jubes")

        "Вам удается скинуть с себя ее ноги и снова встать."
        "Она вскакивает на ноги."

        $ GwenX.ArmPose = 2
        $ GwenX.FaceChange("smile",Mouth="open")

        $ ActiveGirls.append(GwenX) if GwenX not in ActiveGirls else ActiveGirls
        $ GwenX.Love = 400
        $ GwenX.Obed = GwenX.Event[2] * 20
        $ GwenX.Inbt = 100
        $ GwenX.Lust = 0
        $ GwenX.SpriteLoc = StageCenter
        $ GwenX.Petname = Player.Name
        $ GwenX.Petname_rod = Player.Name_rod
        $ GwenX.Petname_dat = Player.Name_dat
        $ GwenX.Petname_vin = Player.Name_vin
        $ GwenX.Petname_tvo = Player.Name_tvo
        $ GwenX.Petname_pre = Player.Name_pre
        $ GwenX.OutfitDay = "casual1"
        $ GwenX.Outfit = "casual1"
        $ GwenX.OutfitChange("casual1")
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = "bg player"
        call Shift_Focus(GwenX)
        call Set_The_Scene(0,1) #shows Entryway

        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) with easeinbottom

        ch_g "Наконец-то, после 10,000 лет заточения, я свободна!"
        $ GwenX.FaceChange("smile")
        if "Gwentro" in LauraX.History:
                ch_g "О, [Player.Name]. Привет."
                if Player.Male:
                        $ GwenX.SeenPeen += 1
                else:
                        $ GwenX.SeenPuss += 1
        menu:
            extend ""
            "Поздравляю!":
                    if "escape" in GwenX.RecentActions:
                            $ GwenX.FaceChange("angry")
                            $ GwenX.Statup("Love", 200, -20)
                            $ GwenX.Statup("Inbt", 200, 10)
                            if not Player.Male:
                                ch_g "Ты даже не попыталась мне помочь!"
                            else:
                                ch_g "Ты даже не попытался мне помочь!"
                    else:
                            $ GwenX.Statup("Love", 200, 10)
                            $ GwenX.Statup("Obed", 200, 3)
                            if not Player.Male:
                                ch_g "Спасибо, что выпустила меня!"
                            else:
                                ch_g "Спасибо, что выпустил меня!"
            "А я помогла!" if "escape" in GwenX.RecentActions and not Player.Male:
                            $ GwenX.FaceChange("confused")
                            $ GwenX.Statup("Love", 200, 5)
                            $ GwenX.Statup("Obed", 200, 5)
                            ch_g "О, тогда спасибо!"
                            $ GwenX.FaceChange("smile")
                            $ GwenX.DrainWord("escape")
            "А я помог!" if "escape" in GwenX.RecentActions and Player.Male:
                            $ GwenX.FaceChange("confused")
                            $ GwenX.Statup("Love", 200, 5)
                            $ GwenX.Statup("Obed", 200, 5)
                            ch_g "О, тогда спасибо!"
                            $ GwenX.FaceChange("smile")
                            $ GwenX.DrainWord("escape")
            "О. Ты выбралась.":
                    if "escape" in GwenX.RecentActions:
                            $ GwenX.FaceChange("angry")
                            $ GwenX.Statup("Love", 200, -25)
                            $ GwenX.Statup("Obed", 200, 5)
                            ch_g "И без твоей помощи!"
                    else:
                            $ GwenX.FaceChange("sad")
                            $ GwenX.Statup("Obed", 200, 10)
                            $ GwenX.Statup("Inbt", 200, 5)
                            ch_g "Ага, пожалуй. . ."
            "Черт!":
                    if "escape" in GwenX.RecentActions:
                            $ GwenX.FaceChange("angry")
                            $ GwenX.Statup("Love", 200, -30)
                            $ GwenX.Statup("Obed", 200, 10)
                            ch_g "Ну -извини-, раз моя свобода тебе противна!"
                    else:
                            $ GwenX.FaceChange("sad")
                            $ GwenX.Statup("Love", 200, -5)
                            $ GwenX.Statup("Obed", 200, 10)
                            ch_g ". . . эм. . .  извини?"

        ch_g "Я думала, что -никогда- не выберусь оттуда."
        ch_g "Хорошо, что там было много еды."
        $ GwenX.FaceChange("sad")
        ch_g "Но мне срочно нужно сходить в душ. . ."
        $ Player.RecentActions.append("loop")
        while "loop" in Player.RecentActions:
            menu:
                extend ""
                "Так кто ты?" if "who" not in GwenX.RecentActions:
                        $ GwenX.AddWord(1,"who") #recent
                        $ GwenX.FaceChange("smile")
                        if "Gwentro" in LauraX.History:
                            ch_g "Это я. . . Гвен."
                            $ GwenX.Name = "Гвен"
                            $ GwenX.Name_rod = "Гвен"
                            $ GwenX.Name_dat = "Гвен"
                            $ GwenX.Name_vin = "Гвен"
                            $ GwenX.Name_tvo = "Гвен"
                            $ GwenX.Name_pre = "Гвен"
                            $ GwenX.FaceChange("smile",2)
                            $ GwenX.Statup("Obed", 200, 5)
                            ch_g "Помнишь, я как-то видела вас с Лорой, когда вы. . ."
                            $ GwenX.Statup("Lust", 80, 5)
                            if not Player.Male:
                                ch_g "Ну, ты поняла. . ."
                            else:
                                ch_g "Ну, ты понял. . ."
                            menu:
                                "А, да.":
                                        $ GwenX.Statup("Love", 200, 5)
                                        $ GwenX.Statup("Inbt", 200, 5)
                                "Не могу вспомнить.":
                                        $ GwenX.Statup("Obed", 200, 10)
                                        ch_g "Серьезно? Наверное, тогда кровь отхлынула от твоего мозга."
                                ". . .":
                                        $ GwenX.Statup("Obed", 200, 5)
                                        $ GwenX.Statup("Inbt", 200, 5)
                                        ch_g "Лааадно, в общем. . ."
                            $ GwenX.FaceChange("smile",1)
                            ch_g "Если вкратце, меня зовут \"Гвен\", и я из другого мира, в котором ваш, видимо, какая-то видеоигра."
                        else:
                            call Gwen_NewIntro
                        $ GwenX.AddWord(1,0,0,"game") #trait
                #end Who are you

                "Игра?" if "game" in GwenX.Traits and "gameworld" not in GwenX.Traits and "reality" not in GwenX.Traits:
                        ch_p "Что значит \"игра?\""
                        $ GwenX.FaceChange("smile",2)
                        ch_g "О, это и значит, ваш мир очень похож на игру. . . хентай-игру."
                        call Gwenception

                "Что у тебя за маска?" if "mask" not in GwenX.RecentActions:
                        $ GwenX.AddWord(1,"mask") #recent
                        $ GwenX.FaceChange("smile")
                        $ GwenX.Statup("Love", 200, 5)
                        ch_g "Ты про нее?"
                        $ GwenX.Hat = 0
                        ch_g "Я получила весь свой костюм, когда попала во вселенную \"комиксов\"."
                        ch_g "Я решила, что у меня будет больше шансов выжить, если я стану супергероем."
                        ch_g "Сюжетная броня как-никак."
                        menu:
                            extend ""
                            "Есть и вселенная комиксов?":
                                    ch_g "О, да."
                                    ch_g "Немного отличается от этой, некоторые люди, которых ты знаешь, там старше."
                                    ch_g "Многие персонажи, которые были там, у вас, скорее всего, никогда вообще не появятся, например, Кэрол Дэнверс."
                                    ch_g "Эта игра скорее похожа на старый мультфильм, который я когда-то смотрела. . ."
                                    $ GwenX.FaceChange("sly",2)
                                    $ GwenX.Statup("Inbt", 200, 5)
                                    $ GwenX.Statup("Lust", 80, 5)
                                    ch_g "Хотя и допускает некоторые вольности. . ."
                                    if "reality" in GwenX.Traits:
                                            $ GwenX.FaceChange("sad",Mouth="smile")
                                            ch_g "Или. . . эм. . . я просто выдумала эту забавную, дурацкую исторю. . ."
                                    $ GwenX.AddWord(1,0,0,"game") #trait
                            "Хм.":
                                    pass
                            ". . .":
                                    pass

                "Сделать ей комплимент" if "mask" in GwenX.RecentActions and "pretty" not in GwenX.RecentActions:
                        $ GwenX.AddWord(1,"pretty") #recent
                        menu:
                            "О! Ты отлично выглядишь!":
                                    $ GwenX.FaceChange("smile",2)
                                    $ GwenX.Statup("Love", 200, 5)
                                    $ GwenX.Statup("Obed", 200, 5)
                                    $ GwenX.Statup("Inbt", 200, 5)
                                    if not Player.Male:
                                        ch_g "Оу, ты такая милая."
                                        $ GwenX.Statup("Love", 200, 5)
                                        ch_g "Ты и сама неплохо выглядишь."
                                    else:
                                        ch_g "Оу, ты такой милый."
                                        $ GwenX.Statup("Love", 200, 5)
                                        ch_g "Ты и сам неплохо выглядишь."
                            "О, а ты сексуальная.":
                                    $ GwenX.FaceChange("confused",2)
                                    $ GwenX.Statup("Love", 200, 5)
                                    $ GwenX.Statup("Inbt", 200, 10)
                                    ch_g "Оу, спасибо?"
                                    $ GwenX.Statup("Love", 200, 5)
                                    $ GwenX.FaceChange("smirk",1)
                                    if not Player.Male:
                                        ch_g "Ты тоже довольно симпатичная."
                                    else:
                                        ch_g "Ты тоже довольно симпатичный."
                            "О, так вот как ты выглядишь под маской.":
                                    $ GwenX.FaceChange("confused")
                                    $ GwenX.Statup("Love", 200, -5)
                                    $ GwenX.Statup("Obed", 200, 5)
                                    ch_g "Эм. . . ага. . ."
                                    menu:
                                        extend ""
                                        "Ты милашка!":
                                                $ GwenX.FaceChange("smile")
                                                ch_g "Оу, спасибо?"
                                                $ GwenX.Statup("Love", 200, 5)
                                                if not Player.Male:
                                                    ch_g "Ты тоже довольно симпатичная."
                                                else:
                                                    ch_g "Ты тоже довольно симпатичный."
                                        ". . .":
                                                $ GwenX.FaceChange("normal",1)
                                                $ GwenX.Statup("Obed", 200, 5)

                            "Думаю, ты зря сняла маску.":
                                    $ GwenX.FaceChange("angry")
                                    $ GwenX.Statup("Love", 200, -15)
                                    $ GwenX.Statup("Obed", 200, 10)
                                    ch_g "Кто тебя вообще спрашивал?!"
                            "[[Неважно]":
                                    pass
                #end "Compliment her"


                "Ты мутант?" if "mutant" not in GwenX.RecentActions:
                        $ GwenX.AddWord(1,"mutant") #recent
                        $ GwenX.Statup("Love", 200, 3)
                        ch_g "Не совсем. . ."
                        $ GwenX.FaceChange("normal")
                        ch_g "Моя сила в том, что я не из этого мира?"
                        ch_g "Хотя я и пыталась превратить себя в мутанта."
                        ch_g "Чтобы не выделяться."

                "Какие у тебя способности?" if "powers" not in GwenX.RecentActions:
                        $ GwenX.AddWord(1,"powers") #recent
                        $ GwenX.FaceChange("perplexed")
                        $ GwenX.Statup("Love", 200, 3)
                        $ GwenX.Statup("Obed", 200, 3)
                        ch_g "Ох. . ."
                        ch_g "Это сложно объяснить. . ."
                        ch_g "В общем, поскольку я родом из мира, в котором ваш - вымысел. . ."
                        ch_g "Правила вашего мира действуют на меня иначе, чем на родных его обитателей."
                        ch_g "Если я очень постараюсь, то смогу заглянуть за края игровой зоны."
                        ch_g "И изменить некоторые механики."
                        $ GwenX.FaceChange("smile")
                        $ GwenX.Statup("Inbt", 200, 5)
                        ch_g "У игр есть правила, у меня же их нет."
                        if "reality" in GwenX.Traits:
                                $ GwenX.FaceChange("sadside")
                                $ GwenX.Statup("Love", 200, -3)
                                ch_g "Или. . . эм. . . я просто выдумала эту забавную, дурацкую исторю. . ."
                                ch_g "А это место -совершенно реальное- и точно-точно не выдуманное. . ."
                                $ GwenX.FaceChange("sly")
                                ch_g "Давай просто скажем так: я могу \"делать разные вещи.\""
                        $ GwenX.AddWord(1,0,0,"game") #trait
                "Ты знаешь Дэдпула?" if "deadpool" not in GwenX.Traits:
                        $ GwenX.AddWord(1,0,0,"deadpool") #traits
                        $ GwenX.FaceChange("normal")
                        ch_g "Ну как сказать. Мы пересекались, но мне он не очень понравился."
                        ch_g "Да, наши костюмы похожи, но это совпадение."
                        $ GwenX.Statup("Obed", 200, 3)
                        ch_g "А еще он спер мою акулу."

                "Как ты сюда попала?" if "how" not in GwenX.RecentActions:
                        $ GwenX.AddWord(1,"how") #recent
                        $ GwenX.FaceChange("normal")
                        $ GwenX.Statup("Love", 200, 3)
                        ch_g "О, это долгая история."
                        ch_g "И она сводится к тому, что \"я без понятия.\""
                        ch_g "Я вступила в бой, бла-бла-бла, а потом очнулась здесь."
                        if "Gwentro" in LauraX.History:
                                $ GwenX.FaceChange("smile",2)
                                $ GwenX.Statup("Obed", 200, 3)
                                ch_g "Следующее, что я помню, я наткнулась на долбаную Лору Кинни, скачущую на тебе."

                "Как ты оказалась в этом чулане?" if "how" in GwenX.RecentActions and "trapped" not in GwenX.RecentActions:
                        $ GwenX.AddWord(1,"trapped") #recent
                        $ GwenX.FaceChange("sad",Mouth="normal")
                        ch_g "Ох. . ."
                        show Gwen_Sprite:
                            ease 1 xoffset -100
                            ease 1 xoffset 100
                            repeat
                        ch_g "Ну, я пыталась найти способ вернуться, и подумала, что могу попробовать пробить стены или что-то типа того."
                        show Gwen_Sprite:
                            ease .5 yoffset 50
                            ease .5 yoffset 0
                            repeat
                        ch_g "Так что я ходила и терлась о каждую твердую поверхность, которую могла найти-"
                        $ GwenX.Statup("Lust", 80, 5)
                        $ GwenX.Statup("Inbt", 200, 5)
                        $ GwenX.FaceChange("sly",2)
                        show Gwen_Sprite:
                            ease 1 xoffset 0
                        $ GwenX.FaceChange("sadside",2,Mouth="smirk")
                        ch_g "Эм. . ."
                        show Gwen_Sprite:
                            ease 1 yoffset 0
                        ch_g "Как-то двусмысленно прозвучало. . ."
                        $ GwenX.FaceChange("normal")
                        ch_g "В общем. . ."
                        ch_g "Таким путем я как-то оказалась в этом чулане."
                        $ GwenX.FaceChange("sadside",2,Mouth="smirk")
                        ch_g "Но потом я не смогла из него выйти."
                        $ GwenX.FaceChange("smile")
                        ch_g "Серьезный удар по моей гордости."
                        ch_g ". . ."
                        menu:
                            extend ""
                            ". . . [[посмотреть на нее с отвращением]":
                                    $ GwenX.FaceChange("sadside",2)
                                    $ GwenX.Statup("Obed", 200, 10)
                                    $ GwenX.Statup("Inbt", 200, -5)
                                    ch_g "Эх. . . хех."
                                    ch_g "Как-то так. . ."
                            "Ха!":
                                    $ GwenX.Statup("Love", 200, 10)
                                    $ GwenX.Statup("Inbt", 200, 10)
                                    ch_g "Я знала, что мы поладим."
                            "Плевать.":
                                    $ GwenX.FaceChange("sad",2,Mouth="smile")
                                    $ GwenX.Statup("Love", 200, -5)
                                    $ GwenX.Statup("Obed", 200, 20)
                                    $ GwenX.Statup("Inbt", 200, -10)
                                    ch_g "Ну извини."
                        $ GwenX.FaceChange("smile")

                "Неважно [[закончить]":
                        $ Player.DrainWord("loop")

        #after loop, the finale. . .

        ch_g "В общем, такова моя доля, похоже, я застряла здесь."
        ch_g "Думаю, мне стоит успокоиться и найти свое место в этом мире."
        menu:
            extend ""
            "Пошли к профессору Ксавье.":
                    $ GwenX.FaceChange("smile")
                    $ GwenX.Statup("Love", 200, 15)
                    $ GwenX.Statup("Obed", 200, 10)
                    ch_g "О, спасибо!"
            "Ладно, пока.":
                    $ GwenX.FaceChange("angry")
                    ch_g "Эй, почему ты не предлагаешь мне помощь с Ксавье?!"
                    menu:
                        extend ""
                        "Упс, извини.":
                                $ GwenX.FaceChange("smile")
                                $ GwenX.Statup("Love", 200, 10)
                                $ GwenX.Statup("Obed", 200, 5)
                                $ GwenX.Statup("Inbt", 200, 5)
                        "Ну ладно, я помогу.":
                                $ GwenX.Statup("Obed", 200, 5)
                                $ GwenX.Statup("Inbt", 200, 10)
                                $ GwenX.FaceChange("sly")
                        "Не хочу.":
                                $ GwenX.Statup("Love", 200, -5)
                                $ GwenX.Statup("Inbt", 200, 5)

                                ch_g "!!!"
                                "Вы почувствовали гул в голове."
                                ch_x "[Player.Name], я заметил присутствие некой необычной личности."
                                ch_x "А также, что ты, похоже, стоишь рядом с ней."
                                if not Player.Male:
                                    ch_x "Не могла бы ты проводить ее в мой кабинет?"
                                else:
                                    ch_x "Не мог бы ты проводить ее в мой кабинет?"
                                $ GwenX.FaceChange("sly")
                    ch_g "Видишь, это было не так уж и сложно."
                    ch_g "Такие вещи решаются сами собой."
                    ch_g "Чу-чу! Поехали!"
        "Вы направляетесь в кабинет Ксавье."

        $ bg_current = "bg study"
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = "bg study"
        call Shift_Focus(GwenX)
        call Set_The_Scene
        show Professor at SpriteLoc(StageLeft)
        $ GwenX.SpriteLoc = StageRight
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc)
        if not Player.Male:
            ch_x "[Player.Name], не могла бы ты представить мне эту юную леди?"
        else:
            ch_x "[Player.Name], не мог бы ты представить мне эту юную леди?"
        menu:
            extend ""
            "Это Гвен." if GwenX.Name == "Гвен":
                    $ GwenX.Statup("Love", 200, 5)
                    $ GwenX.Statup("Obed", 200, 5)
            "Я. . . не знаю, кто это."  if "who" not in GwenX.RecentActions:
                    $ GwenX.Statup("Love", 200, 5)
                    $ GwenX.Statup("Obed", 200, 5)
            "Нет.":
                    $ GwenX.FaceChange("angry")
                    $ GwenX.Statup("Love", 200, -5)
                    $ GwenX.Statup("Obed", 200, 10)
                    $ GwenX.Statup("Inbt", 200, 10)
                    ch_g "Эй!"
        $ GwenX.Hat = 0
        $ GwenX.FaceChange("smile",Eyes="side")
        ch_g "Гвендолин Пул, Владычица Метафизики."
        $ GwenX.Names.append("Gwendolyn")
        ch_g "К вашим услугам."
        if GwenX.Name != "Гвен":
                ch_g "Можно, эм. . . просто \"Гвен.\""
                $ GwenX.Name = "Гвен"
                $ GwenX.Name_rod = "Гвен"
                $ GwenX.Name_dat = "Гвен"
                $ GwenX.Name_vin = "Гвен"
                $ GwenX.Name_tvo = "Гвен"
                $ GwenX.Name_pre = "Гвен"
        ch_x "Церебро помог мне собрать кое-какую. . . интересную информацию о вас."
        $ GwenX.FaceChange("sadside",Mouth="smirk")
        ch_g "Ах да, насчет этого. . ."
        ch_g "Послушайте, я не совсем мутант, я скорее эмигрант."
        $ GwenX.FaceChange("sadside")
        ch_g "Вы не против мне помочь?"
        ch_x "Пожалуй, это можно устроить. . ."
        $ GwenX.FaceChange("smile",Eyes="side")
        ch_x "Что ж, найдите себе свободную комнату, кажется, Табита оставила нам одну после своего. . . инцидента."
        ch_x "Также подберите себе более. . . функциональный гардероб."
        $ GwenX.Statup("Inbt", 200, -5)
        ch_g "Эм, спасибо!"
        if not Player.Male:
            ch_x "[Player.Name], я был бы признателен, если бы ты устроила ей небольшую экскурсию."
        else:
            ch_x "[Player.Name], я был бы признателен, если бы ты устроил ей небольшую экскурсию."
        menu:
            extend ""
            "Конечно.":
                    $ GwenX.FaceChange("smile")
                    $ GwenX.Statup("Love", 200, 5)
                    $ GwenX.Statup("Obed", 200, 5)
            "Ну ладно.":
                    $ GwenX.FaceChange("sad")
                    $ GwenX.Statup("Obed", 200, 5)
                    $ GwenX.Statup("Inbt", 200, 5)
            "Не хочу.":
                    $ GwenX.FaceChange("angry")
                    $ GwenX.Statup("Love", 200, -5)
                    $ GwenX.Statup("Obed", 200, 10)
                    $ GwenX.Statup("Inbt", 200, 5)
                    ch_x "Постарайся изменить свое мнение, [Player.Name]. . ."
        if not Player.Male:
            ch_x "Я позабочусь, чтобы потом ты получила справедливую компенсацию за свое потраченное время."
        else:
            ch_x "Я позабочусь, чтобы потом ты получил справедливую компенсацию за свое потраченное время."
        $ GwenX.FaceChange("smile")
        ch_x "Сегодня вы можете остаться в гостевой комнате, а завтра мы вас устроим."
        ch_g "Спасибо!"
        ch_g "Ладно, мне пора устроиться на новом месте, пожалуй, увидимся завтра?"
        menu:
            extend ""
            "Конечно.":
                    $ GwenX.FaceChange("smile")
                    $ GwenX.Statup("Love", 200, 5)
                    $ GwenX.Statup("Obed", 200, 5)
                    ch_g "Пока!"
            "Ну ладно.":
                    $ GwenX.FaceChange("sad")
                    $ GwenX.Statup("Obed", 200, 5)
                    $ GwenX.Statup("Inbt", 200, 5)
                    ch_g "Эм, ладно, пока."
            "Не хочу.":
                    $ GwenX.FaceChange("angry")
                    $ GwenX.Statup("Love", 200, -5)
                    $ GwenX.Statup("Obed", 200, 3)
                    $ GwenX.Statup("Inbt", 200, 5)
                    ch_g "Ох, ладно. . ."
        "Гвен остается с профессором, а вы продолжаете свой путь."
        $ GwenX.Event[2] = 0
        $ GwenX.Loc = "bg gwen"
        $ bg_current = "bg campus"
        jump Misplaced
#End Gwen primary intro discussion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Gwen alternate intro discussion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_NewIntro:
        #called if you never met her before
#        $ GwenX.Name = "???"
        ch_g "О, я появилась здесь совсем недавно."
        show Gwen_Sprite:
            ease 1 xoffset -200
        ch_g "Я просто искала способ выбраться из этого места. . ."
        $ GwenX.FaceChange("smile")
        extend "\n и, видимо, что я говорю, появляется в тот момент, когда я это говорю. . ."
        $ GwenX.FaceChange("sad")
        extend "\n и теперь я ничего не вижу из-за этого дурацкого пузыря. . ."
        show Gwen_Sprite:
            ease 1 xoffset 0
        $ GwenX.FaceChange("smile")
        extend ""
        ch_g "Вот, так лучше. . ."
#        show Gwen_Sprite:
#            ease 1 ypos 50
        ch_g "So now that we've got that taken care of, what's your name?"
        show Gwen_Sprite:
            ypos 50
        ch_g "Что ж, теперь, когда мы с этим разобрались, как тебя зовут?"
        $ GwenX.FaceChange("surprised",Mouth="open")
        menu:
            ch_g "Что ж, теперь, когда мы с этим разобрались, как тебя зовут?{nw}"
            "[Player.Name]":
                pass
            "Зеро":
                pass
            "Не твое дело":
                pass
            "Кто ты такая?":
                pass
        ch_g "Воу!" with vpunch
        menu:
            ch_g "Воу!"
            "Что?":
                pass
        $ GwenX.FaceChange("surprised")
        ch_g "Извини, просто выскочившее меню застало меня врасплох."
        $ GwenX.FaceChange("smile")
        ch_g "Значит так вы здесь общаетесь? Через диалоговые окна?"
        menu:
            extend ""
            "Да?":
                    ch_g "Все в порядке, я не осуждаю. . ."
                    ch_g "Я думаю, сейчас это не самое важное. . ."
            "О чем ты говоришь?":
                    ch_g "О всплывающие блоках? Думаю, ты не видишь их. . ."
                    ch_g "Если только ты сейчас не прикидываешься."
        ch_g "Ладно, вернемся к тебе, как тебя зовут?"
        menu:
            extend ""
            "[Player.Name]":
                $ GwenX.Statup("Love", 200, 5)
                ch_p "Я [Player.Name]."
                ch_g "Привет, [Player.Name], а меня зовут Гвен!"
                $ GwenX.Name = "Гвен"
                $ GwenX.Name_rod = "Гвен"
                $ GwenX.Name_dat = "Гвен"
                $ GwenX.Name_vin = "Гвен"
                $ GwenX.Name_tvo = "Гвен"
                $ GwenX.Name_pre = "Гвен"
            "Не твое дело":
                $ GwenX.Statup("Love", 200, -5)
                $ GwenX.Statup("Obed", 200, 3)
                ch_p "Это не твое дело."
                ch_g "Ну, похоже тебя зовут [Player.Name_tvo]."
                ch_g "Я поняла по диалоговому окну."
                ch_g "А я, к слову, Гвен."
            "Кто ты такая?":
                ch_p "Не важно кто я, куда важнее кто ты?!"
                ch_g "Ох! Справедливое замечание, я здесь новенькая. Меня зовут Гвен!"
                ch_g "А тебя, похоже, зовут [Player.Name_tvo]."
                ch_g "Я поняла по диалоговому окну."
        if GwenX.Name != "Гвен":
            $ GwenX.Name = "Гвен"
            $ GwenX.Name_rod = "Гвен"
            $ GwenX.Name_dat = "Гвен"
            $ GwenX.Name_vin = "Гвен"
            $ GwenX.Name_tvo = "Гвен"
            $ GwenX.Name_pre = "Гвен"
            menu:
                extend ""
                "Какое нахер окно?!":
                    ch_g "Не бери в голову."
                "Яяяясно. . .":
                    pass
        ch_g "Отлично, итак. . ."
        menu:
            "Что ты здесь делаешь?":
                ch_p "Что ты здесь делаешь?"
                ch_g "Я чувствовала, что ты спросишь об этом."
            "-Какой-то вариант ответа-":
                ch_p "Что ты здесь делаешь?"
                ch_g "Тебе знакомо понятие детерминизма?"
        ch_g "Почему вообще кто-то из нас здесь?"
        if not Player.Male:
            ch_g "А! Ты имела в виду \"почему я именно {i}здесь{/i}\", в этой игре?"
        else:
            ch_g "А! Ты имел в виду \"почему я именно {i}здесь{/i}\", в этой игре?"
        $ GwenX.FaceChange("sad")
        ch_g "Честно? Без понятия."
        $ GwenX.FaceChange("smile")
        ch_g "Может меня добавил какой-то фанат?"
        $ GwenX.FaceChange("smile",1)
        if not Player.Male:
            ch_g "Судя по тому, что ты неплоха собой и тут присутствуют \"интересные\" варианты выбора диалогов. . ."
        else:
            ch_g "Судя по тому, что ты неплох собой и тут присутствуют \"интересные\" варианты выбора диалогов. . ."
        if "gameworld" in GwenX.Traits:
                ch_g "Это определенно какая-то хентай-игра."
        else:
                ch_g "Это какая-то хентай-игра?"
        return
#End Gwen alternate intro discussion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Gwenception discussion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwenception:
        #called if you question the nature of reality
        if "gameworld" in GwenX.Traits:
                return

        if "Gwentro" in LauraX.History:
                $ GwenX.Statup("Obed", 200, 5)
                $ GwenX.Statup("Lust", 200, 5)
                ch_g "Я видела, как Лора накинулась на тебя, когда мы впервые встретились."
                $ GwenX.ArmPose = 1
                ch_g "И обратила внимание на пользовательский интерфейс."
        else:
                $ GwenX.ArmPose = 1
                ch_g "Я видела пользовательский интерфейс."
        $ GwenX.Statup("Obed", 200, 5)
        $ GwenX.Statup("Lust", 200, 5)
        if Player.Male:
                ch_g "На нем был огромный член и еще кое-что. . ."
                ch_g "Похожее на заряд спермы."
        else:
                ch_g "Там было что-то похожее на выносливость и киску."
        ch_g "И знаешь что я поняла? Это точно, прямо сто процентов, хентай-игра."
        $ GwenX.ArmPose = 2
        $ GwenX.AddWord(1,"UI") #Recent
        $ GwenX.AddWord(1,"fake") #Recent
        while "fake" in GwenX.RecentActions or "UI" in GwenX.RecentActions:
            menu:
                extend ""
                "Это не игра.":
                        $ GwenX.FaceChange("sadside",2)
                        $ GwenX.Statup("Love", 200, -5)
                        $ GwenX.Statup("Obed", 200, 10)
                        ch_g "Ох. . . ну, наверное, для тебя это и не игра. . ."
                        $ GwenX.FaceChange("normal")
                        ch_g "Все нормально."
                        if not Player.Male:
                            ch_g "Ты права. . . все -очень- реальное."
                        else:
                            ch_g "Ты прав. . . все -очень- реальное."
                        $ GwenX.AddWord(1,0,0,"reality") #trait
                        $ GwenX.DrainWord("UI")
                        $ GwenX.DrainWord("fake")
                        return

                "Какой еще интерфейс?" if "UI" in GwenX.RecentActions:
                        $ GwenX.FaceChange("smile",1)
                        $ GwenX.ArmPose = 1
                        ch_g "Вон там, на самом верху."
                        $ GwenX.AddWord(1,"menus") #Recent
                "Ты видишь какой-то интерфейс?" if "UI" in GwenX.RecentActions:
                        $ GwenX.FaceChange("smile",1)
                        $ GwenX.ArmPose = 1
                        ch_g "Конечно, он вон там, на самом верху."
                        $ GwenX.AddWord(1,"menus") #Recent

                "Значит все здесь ненастоящее?" if "fake" in GwenX.RecentActions:
                        $ GwenX.FaceChange("normal",1)
                        ch_g "Ну. . . все выглядит вполне реальным."
                        ch_g "То есть, я уверена, что для вас всех все очень даже настоящее."
                "Что еще за \"хентай-игра?\"" if "fake" in GwenX.RecentActions:
                        $ GwenX.FaceChange("surprised",2)
                        $ GwenX.Statup("Inbt", 200, 5)
                        ch_g "Ну!"
                        $ GwenX.FaceChange("sadside",2,Mouth="smirk")
                        ch_g "Эм. . ."
                        $ GwenX.Statup("Obed", 200, 5)
                        ch_g "Это типа. . ."
                        ch_g "Это типа игра, в которой персонажи очень много{w=1}{nw}"
                        $ GwenX.Statup("Inbt", 200, 5)
                        ch_g "Это типа игра, в которой персонажи очень много. . . занимаются. . . сексом. . ."
                        menu:
                            extend ""
                            "А мы с тобой будем заниматься сексом?" if GwenX.SEXP <= 20:
                                    $ GwenX.FaceChange("perplexed",2)
                                    $ GwenX.Statup("Love", 200, 5)
                                    $ GwenX.Statup("Obed", 200, 5)
                            "Типа нас?":
                                    $ GwenX.FaceChange("perplexed",2)
                                    $ GwenX.Statup("Love", 200, 5)
                                    $ GwenX.Statup("Inbt", 200, 5)
                            ". . .":
                                    $ GwenX.Statup("Obed", 200, 5)
                                    $ GwenX.Statup("Inbt", 200, 5)
                        ch_g "Эм. . ."
                "Ладно, как скажешь.":
                        $ GwenX.DrainWord("UI")
                        $ GwenX.DrainWord("fake")
                        $ GwenX.AddWord(1,0,0,"gameworld") #trait
                        return
            #end menu

            if "menus" in GwenX.RecentActions:
                        #if you asked about the menus
                        ch_g "Я думаю, интерфейс показывает статы."
                        ch_g "Мне приходится прищуриваться, чтобы увидеть их. . ."
                        $ GwenX.FaceChange("angry",1)
                        $ GwenX.Statup("Obed", 200, 5)
                        ch_g "Так, подожди-ка. . . теперь я толком его не вижу."
                        $ GwenX.FaceChange("normal",1)
                        $ GwenX.ArmPose = 2
                        $ GwenX.Statup("Obed", 200, 10)
                        $ GwenX.Statup("Inbt", 200, 5)
                        ch_g "Думаю, я все сильнее и сильнее \"интегрируюсь\" в игру."
                        $ GwenX.DrainWord("UI")
                        $ GwenX.DrainWord("menus")
            elif GwenX.SEXP >= 20:
                        $ GwenX.DrainWord("fake")
            else:
                        $ GwenX.FaceChange("normal",2)
                        ch_g "Слушай, не в обиду тебе будет сказано, но я понимаю, как работают эти игры."
                        ch_g "И я не знаю, как я хочу вписаться в нее."
                        $ GwenX.Statup("Love", 200, 5)
                        if not Player.Male:
                            ch_g "С уверенностью могу сказать, что ты милая и довольно сексуальная. . ."
                        else:
                            ch_g "С уверенностью могу сказать, что ты милый и довольно сексуальный. . ."
                        ch_g "Но у меня нет большого личного опыта в таких делах. . ."
                        ch_g "Я не уверена, хочу ли я тебя трахнуть."
                        menu:
                            extend ""
                            "Ох, ладно.":
                                    $ GwenX.FaceChange("normal",1)
                                    $ GwenX.Statup("Love", 200, 15)
                                    $ GwenX.Statup("Inbt", 200, 5)

                            "Я понимаю.":
                                    $ GwenX.FaceChange("normal",1)
                                    $ GwenX.Statup("Love", 200, 15)
                                    $ GwenX.Statup("Obed", 200, 10)
                                    ch_g "Спасибо. . ."
                            "Уверена, тебе неприятно." if not Player.Male:
                                    $ GwenX.FaceChange("sly",1)
                                    $ GwenX.Statup("Love", 200, 5)
                                    $ GwenX.Statup("Obed", 200, 10)
                                    $ GwenX.Statup("Inbt", 200, 10)
                                    ch_g "Ох, наверное. . ."
                            "Уверен, тебе неприятно." if Player.Male:
                                    $ GwenX.FaceChange("sly",1)
                                    $ GwenX.Statup("Love", 200, 5)
                                    $ GwenX.Statup("Obed", 200, 10)
                                    $ GwenX.Statup("Inbt", 200, 10)
                                    ch_g "Ох, наверное. . ."
                            "Жаль.":
                                    $ GwenX.FaceChange("angry",2)
                                    $ GwenX.Statup("Love", 200, -20)
                                    $ GwenX.Statup("Obed", 200, 10)
                                    $ GwenX.Statup("Inbt", 200, 15)
                                    ch_g "Это было бы слишком просто!"
                                    $GwenX.Blush = 1
                                    $ GwenX.AddWord(1,"toobad") #Recent

                        if "toobad" not in GwenX.RecentActions:
                                    #you didn't piss her off
                                    $ GwenX.FaceChange("sadside",2)
                                    $ GwenX.Statup("Love", 200, 5)
                                    $ GwenX.Statup("Obed", 200, 5)
                                    ch_g "Послушай, я не говорю, что \"этого никогда не случится,\" просто. . ."
                                    $ GwenX.FaceChange("sly",1)
                                    ch_g "Дай мне время во всем разобраться. . ."
                        $ GwenX.DrainWord("fake")
        $ GwenX.AddWord(1,0,0,"gameworld") #trait
        return

#End Gwenception discussion / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




## end GwenMeet//////////////////////////////////////////////////////////


label Gwen_Key:
        call Shift_Focus(GwenX)
        $ GwenX.Loc = bg_current
        call Set_The_Scene
        $ GwenX.FaceChange("bemused")
        $ Event_Queue = [0,0]
        ch_g "О, думаю, раз ты так часто приходишь. . ."
        ch_g "вот. . ."
        "Она вручает вам ключ с маленьким брелоком пингвина на нем."
        $ Keys.append(GwenX) if GwenX not in Keys else Keys
        $ GwenX.Event[0] = 1
        ch_p "Спасибо."
        return



# Event Gwen_Caught_Masturbating  /////////////////////////////////////////////////////


label Gwen_BF(BO=[]):
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(GwenX,"bemused","краснеет. . .")
                return
        call Shift_Focus(GwenX)
        if GwenX.Loc != bg_current:
            $ GwenX.Loc = bg_current
            if GwenX not in Party:
                "[GwenX.Name] подходит к вам и изъявляет желание поговорить с вами наедине."
            else:
                "[GwenX.Name] поворачивается к вам и показывает, что хочет поговорить с вами наедине."
        $ Event_Queue = [0,0]
        $ GwenX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene(0)
        call Display_Girl(GwenX)
        $ GwenX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in GwenX.History:
                call expression GwenX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        call CleartheRoom(GwenX)
        $ GwenX.FaceChange("normal",1)
        if "asked boyfriend" not in GwenX.DailyActions:
                ch_g "Слушай, [GwenX.Petname]. Мы можем поговорить?"
        ch_g "Я освоилась, здесь довольно уютно."
        $ GwenX.FaceChange("normal",1,Eyes="side")
        ch_g "Занятия проходят довольно весело. . . намного лучше, чем в средней школе. . ."
        $ GwenX.FaceChange("normal",1)
        ch_g "Преподаватели тоже намного лучше!"
        $ GwenX.FaceChange("sly",1,Eyes="side")
        ch_g "Но, эм. . . Я чувствую, что чего-то не хватает, понимаешь?"
        ch_g "Я чувствую, что мне очень нужно перейти на новый уровень, а это значит мне нужно стать командным игроком."
        if GwenX in Player.Harem:
                #if she somehow already ended up in the harem
                ch_g "Рада, что мы смогли это уладить."
                if "GwenYes" in Player.Traits:
                        $ Player.Traits.remove("GwenYes")
                if "boyfriend" not in GwenX.Petnames:
                        $ GwenX.Petnames.append("boyfriend")
                return
        $ GwenX.FaceChange("normal",1,Brows="sad")
        if len(Player.Harem) > 1:
                ch_g "Так вот, я могу войти в твой маленький гарем?"
        elif Player.Harem:
                ch_g "Так вот, как думаешь, [Player.Harem[0].Name] захочет немного подвинуться?"
                ch_g "Я смогу тоже стать твоей девушкой?"
        else:
                ch_g "Я могу стать твоей девушкой?"
        $ GwenX.Event[5] += 1
        $ Line = "start"
        while Line != "yes":
            menu:
                extend ""
                "Конечно." if Line != "maybe":
                        $ GwenX.FaceChange("normal",1)
                        $ GwenX.Statup("Love", 200, 6)
                        $ GwenX.Statup("Obed", 80, 2)
                        ch_g "Здорово!"
                        $ Line = "yes"
                "Наверное." if Line == "maybe":
                        $ GwenX.FaceChange("normal",1)
                        $ GwenX.Statup("Love", 200, 4)
                        $ GwenX.Statup("Obed", 80, 2)
                        $ GwenX.Statup("Inbt", 60, 1)
                        $ GwenX.Statup("Inbt", 80, 2)
                        ch_g "Здорово!"
                        $ Line = "yes"

                "Я чувствую, что ты используешь меня." if Line != "maybe":
                        $ GwenX.FaceChange("sad",2,Eyes="surprised")
                        $ GwenX.Statup("Love", 200, 3)
                        $ GwenX.Statup("Obed", 60, 2)
                        $ GwenX.Statup("Obed", 80, 2)
                        ch_g "Ох. . ."
                        $ GwenX.FaceChange("sadside",1)
                        ch_g "Прости, у тебя тоже есть чувства. . ."
                        $ GwenX.FaceChange("sly",1)
                        $ GwenX.Statup("Inbt", 80, 2)
                        ch_g "Понимаю и не буду скрывать, я думала, мне помогут отношения с тобой."
                        $ Line = "maybe"

                "Мне это не особо интересно." if Line != "maybe":
                        $ GwenX.FaceChange("sad",1)
                        $ GwenX.Statup("Love", 200, -3)
                        $ GwenX.Statup("Obed", 80, 3)
                        if not Player.Male:
                            ch_g "Оу. . . ты уверена?"
                        else:
                            ch_g "Оу. . . ты уверен?"
                        $ Line = "maybe"
                "Мне это -совсем- не интересно." if Line == "maybe":
                        $ GwenX.FaceChange("sad",1)
                        $ GwenX.Statup("Love", 200, -5)
                        $ GwenX.Statup("Obed", 60, 1)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_g "Оу. . ."
                        $ Line = "no"

                "Нет, я не думаю, что она поймет." if len(Player.Harem) == 1:
                        $ GwenX.Statup("Love", 200, -5)
                        $ GwenX.Statup("Obed", 80, 7)
                        $ GwenX.FaceChange("angry",1,Eyes="side")
                        $ GwenX.GLG(Player.Harem[0],800,-20,1)
                        ch_g "Хреново."
                        $ Line = "no"
                "Они этого не поймут." if len(Player.Harem) > 1:
                        $ GwenX.Statup("Love", 200, -5)
                        $ GwenX.Statup("Obed", 80, 7)
                        $ GwenX.FaceChange("sad",1)
                        call HaremStatup(GwenX,700,-20) #lowers like of all Harem girls by 10
                        ch_g "Оу."
                        $ Line = "no"

            if Line == "no":
                    ch_g "Ну. . . Если вдруг передумаешь, свяжись со мной."
                    "[GwenX.Name] уходит расстроенная."
                    $ GwenX.Event[5] = 20
                    call Remove_Girl(GwenX)
                    $ Line = 0
                    return
            # end menu

        if Player.Harem:
            #if you agreed, but have other girls. . .
            if len(Player.Harem) >= 2:
                ch_g "Другие девушки не против, правда?"
            else:
                ch_g "[Player.Harem[0].Name] не против, правда?"
            menu:
                extend ""
                "Все хорошо, всех все устраивает." if "GwenYes" in Player.Traits:
                        $ GwenX.Statup("Love", 200, 5)
                        $ GwenX.Statup("Obed", 80, 10)
                        $ GwenX.Statup("Inbt", 80, 5)
                        $ GwenX.FaceChange("surprised",1)
                        ch_g "Замечательно!"
                "Нууу. . . это сперва еще нужно узнать." if "GwenYes" not in Player.Traits:
                        $ GwenX.Statup("Love", 200, 3)
                        $ GwenX.Statup("Obed", 80, 3)
                        $ GwenX.Statup("Inbt", 80, 1)
                        $ GwenX.Statup("Lust", 80, 1)
                        $ GwenX.FaceChange("confused",1)
                        ch_g "Ох. . . тогда скажи мне, когда все уладишь. . ."
                        $ GwenX.Event[5] = 20
                        call Remove_Girl(GwenX)
                        $ Line = 0
                        return
            call HaremStatup(GwenX,900,20) #raises like of all Harem girls by 20
        if "Historia" not in Player.Traits:
            $ Player.Harem.append(GwenX)
            if "GwenYes" in Player.Traits:
                    $ Player.Traits.remove("GwenYes")
            $ GwenX.Petnames.append("boyfriend")
            call Harem_Initiation
        $ GwenX.Statup("Love", 200, 3)
        $ GwenX.Statup("Obed", 80, 3)
        $ GwenX.Statup("Inbt", 80, 1)
        $ GwenX.Statup("Lust", 80, 1)
        $ GwenX.FaceChange("sly",1)
        ch_g "Ну, пожалуй, я смогу найти способ отблагодарить тебя. . ."
        if "Historia" in Player.Traits:
                return 1
        $ Tempmod = 10
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        $ Tempmod = 0
        jump Misplaced
        return


## start Gwen_Love//////////////////////////////////////////////////////////
label Gwen_Love(Shipping=[],Shipshape=0,Topics=[],BO=[]):
        # SHipping is used to track who else you're involved with
        # if GwenX.Event[6] = 5, then it cleared
        # if GwenX.Event[6] = 20, then it broke because you didn't love her
        # if GwenX.Event[6] = 25, then it broke and you already went through the redux

        $ GwenX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ BO = TotalGirls[:]
        $ BO.remove(GwenX)
        while BO:
            if ApprovalCheck(BO[0], 1200, "LO"):
                    $ Shipping.append(BO[0])
            $ BO.remove(BO[0])
        $ Shipshape = len(Shipping)

        $ GwenX.FaceChange("sad",1,Mouth="normal")
        if GwenX.Loc == bg_current or GwenX in Party:
                "[GwenX.Name] смотрит на вас с обеспокоенным видом."
        else:
                "[GwenX.Name] поворачивает за угол и замечает вас."
        if bg_current != "bg gwen" and bg_current != "bg player":
                "Она просит вас пройти за ней в ее комнату, и, похоже, отказ не принимается."
                $ bg_current = "bg gwen"

        $ Event_Queue = [0,0]
        $ GwenX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(GwenX)
        call Set_The_Scene
        call Taboo_Level
        call Shift_Focus(GwenX)
        $ GwenX.DailyActions.append("relationship")
        $ GwenX.FaceChange("sad",1,Mouth="normal")
        ch_g "Слушай. . ."
        ch_g "Ладно, мы уже много раз говорили об этом, но ты ведь понимаешь, что это все игра, верно?"
        menu:
            extend ""
            ". . .":
                    $ GwenX.Statup("Love", 200, 1)
                    $ GwenX.Statup("Obed", 90, 2)
                    ch_g "Да, точно."
            "Это не игра, [GwenX.Name].":
                    "Она прикладывает палец к вашим губам"
                    $ GwenX.FaceChange("kiss",1)
                    $ GwenX.Statup("Love", 200, -2)
                    $ GwenX.Statup("Inbt", 90, 2)
                    ch_g "Шшшшшшшшш."
                    ch_g "Не надо. . ."
                    if "sir" not in GwenX.Petnames:
                            $ GwenX.FaceChange("sly",1)
                            ch_g "Возможно, мы обсудим это подробнее в ветке \"Послушания\". . ."
            "Да?":
                    $ GwenX.FaceChange("bemused",1)
                    $ GwenX.Statup("Love", 200, 3)
                    $ GwenX.Statup("Obed", 50, 3)
                    $ GwenX.Statup("Obed", 90, 5)
                    ch_g "Хорошо."
            "Только не снова.":
                    $ GwenX.FaceChange("angry",1,Mouth="smile")
                    $ GwenX.Statup("Love", 200, -5)
                    $ GwenX.Statup("Inbt", 90, 5)
                    ch_g "Извини, но мне придется. . ."
                    if "master" not in GwenX.Petnames:
                            ch_g "Возможно, мы обсудим это подробнее в ветке \"Послушания\". . ."
        $ GwenX.FaceChange("sadside",1)
        ch_g "Ну, я знаю, как работают эти игры."
        $ GwenX.FaceChange("sadside",1,Mouth="smirk")
        ch_g "Как они должны работать."
        ch_g "Парень знакомится с девушкой, и они начинают встречаться."
        if not Player.Male:
                $ GwenX.FaceChange("sadside",1,Mouth="normal")
                ch_g "Или, как в данном случае, девушка знакомится с девушкой. . ."
                $ GwenX.FaceChange("sadside",1,Mouth="smirk")
                ch_g "С жанром \"юри\" я тоже знакома. . ."
        $ GwenX.FaceChange("sadside",1,Mouth="lipbite")
        ch_g "Девушка начинает испытывать чувства, воздух так и пропитывается \"романтикой\"."
        $ GwenX.FaceChange("sadside",1,Mouth="normal")
        ch_g "Я люблю такие игры, правда."
        ch_g "Я часто играла в них, когда мне было скучно. . ."
        $ GwenX.FaceChange("bemused",1)
        if not Player.Male:
            ch_g "-в общем, ты поняла."
        else:
            ch_g "-в общем, ты понял."
        $ GwenX.FaceChange("sadside",1,Mouth="smirk")
        ch_g "Но я не ожидала, что попаду в одну из таких игр. . ."
        $ GwenX.FaceChange("sadside",2)
        ch_g ". . ."
        ch_g "и точно не думала, что буду той, кто начнет испытывать чувства."
        $ GwenX.FaceChange("sadside",1)
        if len(Player.Harem) >= 3:
                $ GwenX.FaceChange("sadside",1,Mouth="smirk")
                $ GwenX.Statup("Obed", 70, 3)
                $ GwenX.Statup("Obed", 90, 5)
                ch_g "Другие девушки из нашего маленького \"гарема\" очень замечательные. . ."
        elif Shipshape >= 3:
                $ GwenX.Statup("Love", 200, -2)
                $ GwenX.Statup("Obed", 70, 3)
                $ GwenX.Statup("Obed", 90, 5)
                if not Player.Male:
                    ch_g "Я понимаю, ты здесь главная героиня, наслаждающаяся имеющимися возможностями."
                else:
                    ch_g "Я понимаю, ты здесь главный герой, наслаждающийся имеющимися возможностями."
        else:
                $ GwenX.Statup("Love", 200, 15)
                $ GwenX.Statup("Obed", 70, 10)
                $ GwenX.Statup("Obed", 90, 5)
                $ GwenX.FaceChange("sadside",1,Mouth="smirk")
                ch_g "Мне кажется, что я забираю все твое внимание на себя. . ."
        if len(Player.Harem) >= 3 or Shipshape >= 3:
            $ GwenX.FaceChange("sadside",1,Mouth="smirk")
            if "sexfriend" in GwenX.Petnames:
                    $ GwenX.Statup("Love", 200, 2)
                    $ GwenX.Statup("Inbt", 90, 3)
                    ch_g "С кем ты трахаешься, это твое дело. . ."
            elif "master" in GwenX.Petnames:
                    $ GwenX.Statup("Love", 200, 2)
                    $ GwenX.Statup("Obed", 200, 5)
                    ch_g "Я не в праве оспаривать твои решения. . ."
            elif "sir" in GwenX.Petnames:
                    $ GwenX.Statup("Obed", 90, 3)
                    ch_g "Я готова принять твою. . . свободу. . ."
            else:
                    $ GwenX.Statup("Love", 200, -2)
                    $ GwenX.Statup("Inbt", 90, 3)
                    ch_g "Я хочу для тебя счастья. . ."
        $ GwenX.FaceChange("sad",2)
        if not Player.Male:
            ch_g "-но мне кажется, что я хочу, чтобы ты была только моей."
        else:
            ch_g "-но мне кажется, что я хочу, чтобы ты был только моим."
        ch_g "Я. . ."
        $ GwenX.FaceChange("sad",2,Mouth="normal")
        ch_g "-люблю тебя."
        menu:
            extend ""
            "Я тоже тебя люблю!":
                $ GwenX.FaceChange("smile",1)
                $ GwenX.Statup("Love", 200, 20)
                $ GwenX.Statup("Inbt", 90, 5)
                ch_g "Правда?!"
                ch_g "Отлично!"
                $ GwenX.Petnames.append("lover")
                jump Gwen_Love_End
            "Я знаю.":
                $ GwenX.FaceChange("surprised",1,Mouth="smile")
                $ GwenX.Statup("Love", 200, 10)
                $ GwenX.Statup("Obed", 90, 5)
                $ GwenX.Statup("Inbt", 90, 5)
                ch_g "Не делай при мне \"отслылки к поп культуре\"!"
                $ GwenX.Statup("Love", 200, 5)
                $ GwenX.FaceChange("smile",1)
                ch_g "Это моя фишка!"
                $ GwenX.Statup("Inbt", 90, 10)
                $ GwenX.FaceChange("normal",2,Mouth="smirk")
                ch_g "\"Я знаю\", что и ты тоже меня любишь!"
                $ GwenX.FaceChange("normal",1,Mouth="smirk")
                $ GwenX.Petnames.append("lover")
                jump Gwen_Love_End
            "Это здорово?":
                $ GwenX.FaceChange("confused",1)
                $ GwenX.Statup("Obed", 90, 5)
                ch_g "Я. . . не уверена, [GwenX.Petname]."
            "Хм.":
                $ GwenX.FaceChange("confused",1)
                $ GwenX.Statup("Love", 200, -5)
                $ GwenX.Statup("Obed", 90, 10)
                ch_g "Ну, это не самое лучшее начало."
        menu:
            extend ""
            "Ох, я тоже тебя люблю!":
                $ GwenX.FaceChange("smile",1)
                $ GwenX.Statup("Love", 200, 15)
                $ GwenX.Statup("Obed", 90, 5)
                if not Player.Male:
                    ch_g "Ты что, издевалась надо мной?"
                else:
                    ch_g "Ты что, издевался надо мной?"
                $ GwenX.FaceChange("sly",1)
                $ GwenX.Statup("Inbt", 90, 5)
                ch_g "Ладно, я не против. . ."
                $ GwenX.Petnames.append("lover")
                jump Gwen_Love_End
            "Я. . . тоже тебя люблю?":
                $ GwenX.FaceChange("confused",1)
                $ GwenX.Statup("Love", 200, 5)
                $ GwenX.Statup("Obed", 90, 5)
                ch_g "Какой восторженный ответ."
                ch_g "\"Я люблю тебя, [GwenX.Name]!\" Это так сложно сказать?"
                $ GwenX.FaceChange("bemused",1)
                $ GwenX.Statup("Obed", 90, 5)
                ch_g "Я, конечно, не заглядывала в варианты ответов, но уверена, что что-то подобное там было. . ."
                $ GwenX.Petnames.append("lover")
                jump Gwen_Love_End
            "Ну, это все, конечно, круто и все такое. . .":
                $ GwenX.FaceChange("sad",1)
                $ GwenX.Statup("Love", 200, -5)
                $ GwenX.Statup("Obed", 90, 10)
                $ GwenX.Statup("Inbt", 90, -5)
                ch_g ". . . но ты не любишь меня. Лаааадно. . ."
            "Теперь я чувствую себя. . . неуютно.":
                $ GwenX.FaceChange("confused",1)
                $ GwenX.Statup("Love", 200, -10)
                $ GwenX.Statup("Obed", 90, 15)
                $ GwenX.Statup("Inbt", 90, -5)
                ch_g "Ба-дум-тц. . ."
                $ GwenX.FaceChange("sad",1)


        if not Player.Male:
            ch_g "Так, эм. . . почему ты не приняла мое признание?"
        else:
            ch_g "Так, эм. . . почему ты не принял мое признание?"
        ch_g "Просто ты больше заинтересован в других?"
        $ Line = 0
        menu:
                extend ""
                "Да, мне больше интересна другая." if Shipping and Shipshape < 3:
                    menu: #rkeljsvgb
                        "Это [RogueX.Name]." if RogueX in Shipping:
                                $ Line = RogueX
                        "Это [KittyX.Name]." if KittyX in Shipping:
                                $ Line = KittyX
                        "Это [EmmaX.Name]." if EmmaX in Shipping:
                                $ Line = EmmaX
                        "Это [LauraX.Name]." if LauraX in Shipping:
                                $ Line = LauraX
                        "Это [JeanX.Name]." if JeanX in Shipping:
                                $ Line = JeanX
                        "Это [StormX.Name]." if StormX in Shipping:
                                $ Line = StormX
                        "Это [JubesX.Name]." if JubesX in Shipping:
                                $ Line = JubesX
                        "Это [BetsyX.Name]." if BetsyX in Shipping:
                                $ Line = BetsyX
                        "Это [DoreenX.Name]." if DoreenX in Shipping:
                                $ Line = DoreenX
                        "Мне бы не хотелось произносить ее имя.":
                                $ GwenX.Statup("Obed", 90, 15)
                                $ GwenX.Statup("Inbt", 90, 5)
                                $ GwenX.FaceChange("sadside",1)
                                ch_g "Ха, думаю, тебе стоило ответить. . ."
                    if Line:
                        #If you called out a girl,
                        if GwenX.GirlLikeCheck(Line) >= 800:
                            $ GwenX.Statup("Love", 200, 5)
                            $ GwenX.Statup("Obed", 90, 20)
                            $ GwenX.Statup("Inbt", 90, 5)
                            $ GwenX.FaceChange("sadside",1)
                            ch_g "Я могу. . . с ней договориться. . ."
                        else:
                            $ GwenX.FaceChange("angry",Eyes="side")
                            $ GwenX.Statup("Love", 200, -5)
                            $ GwenX.Statup("Obed", 90, 20)
                            ch_g "Из-за нее? Черт. . ."
                            $ GwenX.FaceChange("sadside",1)
                            $ GwenX.GLG(Line,800,-50,1)

                "Да, мне больше интересны другие" if Shipshape > 1:
                        $ GwenX.Statup("Obed", 90, 15)
                        $ GwenX.Statup("Inbt", 90, 5)
                        $ GwenX.FaceChange("surprised",1)
                        ch_g "Я в шоке."
                        $ GwenX.FaceChange("bemused",1,Brows="sad")
                        ch_g "Ну ладно, не очень. . ."
                "Мне никто не интересен.":
                        $ GwenX.Statup("Love", 200, -15)
                        $ GwenX.Statup("Obed", 90, 15)
                        $ GwenX.Statup("Inbt", 90, 5)
                        $ GwenX.FaceChange("sad",1)
                        if ApprovalCheck(GwenX, 1000, "OI"):
                            ch_g "Чушь какая-то, но ладно."
                        else:
                            ch_g "Это чушь, и ты это знаешь."
                "Дело в \"тебе\".":
                        $ GwenX.FaceChange("angry")
                        $ GwenX.Statup("Love", 200, -25)
                        $ GwenX.Statup("Obed", 90, 15)
                        ch_g "Серьезно?!"
                        $ GwenX.Statup("Love", 200, -10)
        $ GwenX.FaceChange("sad",1)
        ch_g "Наверное. . ."
        ch_g "Наверное. . . это справедливо."
        ch_g "Не твоя вина, что я оказалась в этой игре."
        ch_g "Если тебе это не нравится, значит не нравится."
        if "sexfriend" in GwenX.Petnames:
                $ GwenX.FaceChange("sly",1)
                ch_g "Мы все еще можем трахаться, если ты хочешь. . ."
        elif "master" in GwenX.Petnames:
                $ GwenX.FaceChange("sad",1,Mouth="normal")
                ch_g "Я все еще буду слушаться тебя. . ."
        elif "sir" in GwenX.Petnames:
                $ GwenX.FaceChange("sad",1,Mouth="normal")
                ch_g "Я все равно остаюсь командным игроком. . ."
        else:
                $ GwenX.FaceChange("sad",1)
                ch_g "Мы все еще можем. . ."
                $ GwenX.FaceChange("sadside",1,Mouth="smirk")
                ch_g "-общаться. . ."
        menu:
            extend ""
            "Ага. . .":
                    $ GwenX.FaceChange("sad",1)
                    ch_g "Ага, увидимся. . ."
            ". . .":
                    $ GwenX.FaceChange("sad",1)
            "Может, когда-нибудь все и изменится":
                    ch_g "Ага, когда-нибудь. . ."
                    $ GwenX.FaceChange("sad",1)
            "Я тоже люблю тебя!":
                    $ GwenX.FaceChange("sad",1)
                    ch_g "Ага, уви-"
                    $ GwenX.FaceChange("surprised",2,Mouth="open")
                    $ GwenX.Statup("Love", 200, 10)
                    $ GwenX.Statup("Obed", 90, 3)
                    ch_g "Подожди, что?!"
                    menu:
                        extend ""
                        "Я сказала, \"Я тоже тебя люблю,\" [GwenX.Name]!" if not Player.Male:
                                $ GwenX.FaceChange("smile",1)
                                $ GwenX.Statup("Love", 200, 5)
                                ch_g "БОЖЕ!"
                                $ GwenX.FaceChange("surprised",2,Mouth="open")
                                ch_g "Произошла такая фигня, когда. . ."
                                $ GwenX.FaceChange("surprised",1,Eyes="side")
                                ch_g "Когда, все идет в одном направлении, но потом. . . БАЦ!"
                                $ GwenX.FaceChange("surprised",1,Mouth="smile")
                                $ GwenX.Statup("Love", 200, 10)
                                $ GwenX.Statup("Inbt", 90, 3)
                                ch_g "-и все резко меняется!"
                                $ GwenX.FaceChange("smile",1)
                                $ GwenX.Statup("Love", 200, -5)
                                $ GwenX.Statup("Obed", 90, 3)
                                ch_g "Ну ты и коза!"
                                $ GwenX.Petnames.append("lover")
                                call Gwen_Love_End
                        "Я сказал, \"Я тоже тебя люблю,\" [GwenX.Name]!" if Player.Male:
                                $ GwenX.FaceChange("smile",1)
                                $ GwenX.Statup("Love", 200, 5)
                                ch_g "БОЖЕ!"
                                $ GwenX.FaceChange("surprised",2,Mouth="open")
                                ch_g "Произошла такая фигня, когда. . ."
                                $ GwenX.FaceChange("surprised",1,Eyes="side")
                                ch_g "Когда, все идет в одном направлении, но потом. . . БАЦ!"
                                $ GwenX.FaceChange("surprised",1,Mouth="smile")
                                $ GwenX.Statup("Love", 200, 10)
                                $ GwenX.Statup("Inbt", 90, 3)
                                ch_g "-и все резко меняется!"
                                $ GwenX.FaceChange("smile",1)
                                $ GwenX.Statup("Love", 200, -5)
                                $ GwenX.Statup("Obed", 90, 3)
                                ch_g "Ну ты и козел!"
                                $ GwenX.Petnames.append("lover")
                                call Gwen_Love_End
                        "Ох, неважно.":
                                $ GwenX.FaceChange("angry",1)
                                $ GwenX.Statup("Love", 200, -15)
                                $ GwenX.Statup("Obed", 90, 10)
                                ch_g ". . ."
                                ch_g "\"[GwenX.Name] это запомнит. . .\""
                                $ GwenX.AddWord(1,0,0,0,"syke") #history
                                $ GwenX.RecentActions.append("angry")
                                $ GwenX.DailyActions.append("angry")
                        "Я сказала, \"Я тоже сейчас уйду.\"" if not Player.Male:
                                $ GwenX.FaceChange("angry",1)
                                $ GwenX.Statup("Love", 200, -20)
                                $ GwenX.Statup("Obed", 70, 5)
                                $ GwenX.Statup("Obed", 95, 10)
                                ch_g ". . ."
                                ch_g "\"[GwenX.Name] это запомнит. . .\""
                                $ GwenX.AddWord(1,0,0,0,"syke") #history
                                $ GwenX.RecentActions.append("angry")
                                $ GwenX.DailyActions.append("angry")
                        "Я сказал, \"Я тоже сейчас уйду.\"" if Player.Male:
                                $ GwenX.FaceChange("angry",1)
                                $ GwenX.Statup("Love", 200, -20)
                                $ GwenX.Statup("Obed", 70, 5)
                                $ GwenX.Statup("Obed", 95, 10)
                                ch_g ". . ."
                                ch_g "\"[GwenX.Name] это запомнит. . .\""
                                $ GwenX.AddWord(1,0,0,0,"syke") #history
                                $ GwenX.RecentActions.append("angry")
                                $ GwenX.DailyActions.append("angry")
        hide Gwen_Sprite with easeoutright
        call Remove_Girl(GwenX)
        $ GwenX.Loc = "hold" #puts her off the board for the day
        "Она уходит."
        $ GwenX.Event[6] = 20
        $ Line = 0
        jump Misplaced
        return

label Gwen_Love_End:
        $ GwenX.Event[6] = 5
        "[GwenX.Name] крепко обнимает вас."
        $ GwenX.Statup("Love", 200, 25)
        $ GwenX.Statup("Lust", 90, 5)
        $ GwenX.FaceChange("sly",1)
        ch_g "Итак. . . раз уж тебе очень нравится трахаться. . ."
        $ GwenX.Statup("Lust", 90, 10)

        if not GwenX.Sex:
            $ GwenX.FaceChange("bemused",2)
            ch_g "Думаю, я готова. . ."
        ch_g "Не хочешь испытать эти игровые механики?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Да, давай испытаем их. . . [[заняться сексом]":   #fix, unlock once sex becomes an option
                    $ GwenX.Statup("Inbt", 30, 20)
                    $ GwenX.Statup("Obed", 70, 10)
                    ch_g "Хмм. . ."
                    if Player.Male:
                            call SexAct("sex") # call SexAct("sex")
                    else:
                            call SexAct("blow") # call SexAct("blow")
                "У меня есть другая идея. . .[[выбрать другое занятие]":
                    $ GwenX.Brows = "confused"
                    $ GwenX.Statup("Obed", 70, 25)
                    ch_g "Например? . ."
                    $ Tempmod = 20
                    call SexMenu
        jump Misplaced

label Gwen_Love_Redux:
         #this is for if you rejected her but want a second chance
        $ Line = 0
        call Shift_Focus(GwenX)
        $ GwenX.DailyActions.append("relationship")

        if GwenX.Event[6] >= 25:
                #if this is the second time through
                ch_p "Надеюсь, ты меня простила, я все еще люблю тебя."
                $ GwenX.Statup("Love", 95, 10)
                if "syke" in GwenX.History:
                    $ GwenX.Statup("Love", 200, -5)
                if ApprovalCheck(GwenX, 950, "L"):
                    $ Line = "love"
                else:
                    $ GwenX.FaceChange("sad",1)
                    ch_g "Я. . . Я еще не готова простить тебя, [GwenX.Petname]."
                    $ GwenX.FaceChange("sadside",Mouth="lipbite")
                    ch_g ". . ."
                    ch_g "Но я выслушаю тебя. . ."
        elif "syke" in GwenX.History:
                    #you tried to trick her into thinking you'd said you loved her
                    if not Player.Male:
                        ch_p "Помнишь, я сказала тебе, что не люблю тебя?"
                    else:
                        ch_p "Помнишь, я сказал тебе, что не люблю тебя?"
                    $ GwenX.FaceChange("angry",1)
                    $ GwenX.Statup("Love", 200, -10)
                    ch_g "Я помню твои попытки вывести меня из себя. . ."
                    $ GwenX.FaceChange("sadside",1)
                    ch_g "Что ты хочешь мне еще сказать? . ."
        else:
                    if not Player.Male:
                        ch_p "Помнишь, когда я сказала тебе, что не люблю тебя?"
                    else:
                        ch_p "Помнишь, когда я сказал тебе, что не люблю тебя?"
                    $ GwenX.FaceChange("perplexed",1)
                    ch_g ". . ."
                    $ GwenX.FaceChange("sadside",1)
                    ch_g "Такое трудно забыть. . ."

        if Line != "love":
                menu:
                    extend ""
                    "Прости, я не хотела так говорить." if not Player.Male:
                        $ GwenX.FaceChange("confused",1)
                        ch_g ". . ."
                        ch_g "Что. . ."
                        ch_p "Ага. То есть, я люблю тебя, [GwenX.Name]."
                        $ GwenX.Statup("Love", 200, 10)
                        if ApprovalCheck(GwenX, 950, "L"):
                            $ Line = "love"
                            $ GwenX.FaceChange("surprised",1,Mouth="normal")
                        else:
                            $ GwenX.FaceChange("sadside")
                            ch_g "Ну а я больше не уверена. . ."
                    "Прости, я не хотел так говорить." if Player.Male:
                        $ GwenX.FaceChange("confused",1)
                        ch_g ". . ."
                        ch_g "Что. . ."
                        ch_p "Ага. То есть, я люблю тебя, [GwenX.Name]."
                        $ GwenX.Statup("Love", 200, 10)
                        if ApprovalCheck(GwenX, 950, "L"):
                            $ Line = "love"
                            $ GwenX.FaceChange("surprised",1,Mouth="normal")
                        else:
                            $ GwenX.FaceChange("sadside")
                            ch_g "Ну а я больше не уверена. . ."
                    "Я передумала, я люблю тебя, так что. . ." if not Player.Male:
                        if ApprovalCheck(GwenX, 950, "L"):
                            $ Line = "love"
                            $ GwenX.FaceChange("surprised",1,Mouth="normal")
                            ch_g "Что? Правда?!"
                        else:
                            $ GwenX.Mouth = "sad"
                            ch_g "Ну. . ."
                            $ GwenX.Statup("Inbt", 90, 10)
                            $ GwenX.FaceChange("sadside")
                            ch_g "Я больше не испытываю таких чувств к тебе. . ."
                    "Я передумал, я люблю тебя, так что. . ." if Player.Male:
                        if ApprovalCheck(GwenX, 950, "L"):
                            $ Line = "love"
                            $ GwenX.FaceChange("surprised",1,Mouth="normal")
                            ch_g "Что? Правда?!"
                        else:
                            $ GwenX.Mouth = "sad"
                            ch_g "Ну. . ."
                            $ GwenX.Statup("Inbt", 90, 10)
                            $ GwenX.FaceChange("sadside")
                            ch_g "Я больше не испытываю таких чувств к тебе. . ."
                    "Эм, неважно.":
                            $ GwenX.Statup("Love", 200, -30)
                            $ GwenX.Statup("Obed", 50, 10)
                            $ GwenX.FaceChange("angry")
                            ch_g "Ох, ну и отъебись тогда от меня."
                            $ GwenX.RecentActions.append("angry")
                            $ GwenX.DailyActions.append("angry")
        if Line == "love":
                $ GwenX.Statup("Love", 200, 40)
                $ GwenX.Statup("Obed", 90, 10)
                $ GwenX.Statup("Inbt", 90, 10)
                $ GwenX.FaceChange("normal")
                if not Player.Male:
                    ch_g "Я. . . Я рада, что ты все обдумала. . ."
                else:
                    ch_g "Я. . . Я рада, что ты все обдумал. . ."
                ch_g "Я тоже тебя люблю, [GwenX.Petname]!"
                $ GwenX.Petnames.append("lover")
        $ GwenX.Event[6] = 25
        return

# end Gwen_Love//////////////////////////////////////////////////////////


# start Gwen_Sub//////////////////////////////////////////////////////////

label Gwen_Sub:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(GwenX,"bemused","выглядит тихой. . .")
            return
    $ GwenX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    call Shift_Focus(GwenX)
    if GwenX.Loc != bg_current and GwenX not in Party:
        "Вдруг [GwenX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить."

    $ Event_Queue = [0,0]
    $ GwenX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(GwenX)
    call CleartheRoom(GwenX)
    call Set_The_Scene
    call Taboo_Level
    $ GwenX.DailyActions.append("relationship")
    $ GwenX.FaceChange("bemused", 1)
    if not Player.Male and "girltalk" not in GwenX.History:
            call expression GwenX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
            return
    ch_g "Ладно, значит так. . ."
    ch_g "Кажется, я начинаю понимать, что это за место."
    ch_g "Знаешь ли, я играла в несколько эроигр до попадания сюда. . ."
    ch_g "Хотя, кажется, они больше походили на \"отомэ\" игры, в отличии от этой. . ."
    $ GwenX.FaceChange("sly", 1)
    ch_g "У тебя здесь настоящий простор для выбора. . ."
    $ GwenX.FaceChange("sly", 1,Eyes="side")
    if not Player.Male:
        ch_g "Я даже не уверена, что видела здесь других парней, кроме Ксавье. . ."
    else:
        ch_g "Я даже не уверена, что видела здесь других парней, кроме Ксавье и тебя. . ."
    $ GwenX.FaceChange("sly", 1)
    ch_g "Я много наблюдала и поняла, что игра словно вертится вокруг тебя."
    ch_g ". . ."
    ch_g "И тогда ко мне пришло осознание. . ."
    ch_g "-Я поняла, что главный герой здесь далеко не я. . ."
    ch_g "-а ты."
    menu:
        extend ""
        ". . .":
                $ GwenX.FaceChange("sly", 1,Eyes="side")
                $ GwenX.Statup("Love", 60, -1)
                $ GwenX.Statup("Obed", 90, 1)
                $ GwenX.Statup("Inbt", 70, 2)
                ch_g "Я приму такой ответ за. . . \"наверное?\""
        "Это не игра, [GwenX.Name].":
                $ GwenX.Statup("Love", 80, -2)
                $ GwenX.Statup("Obed", 90, 2)
                ch_g "Я знаю, что ты скептик."
                $ GwenX.Statup("Inbt", 70, 2)
                ch_g "но мне известна правда."
                call Gwenception
        "Что?":
                $ GwenX.Statup("Love", 80, 1)
                $ GwenX.Statup("Inbt", 80, 5)
                ch_g "Да, думаю, все запутанно."
        "Еще бы.":
                $ GwenX.Statup("Love", 80, -3)
                $ GwenX.Statup("Obed", 200, 10)
                $ GwenX.FaceChange("sadside", 1)
                ch_g "Знаешь, ты сама скромность. . ."
        "Приятно, что ты начала это понимать.":
                $ GwenX.FaceChange("sadside", 1)
                $ GwenX.Statup("Love", 80, -1)
                $ GwenX.Statup("Obed", 200, 5)
                $ GwenX.Statup("Inbt", 50, 2)
                ch_g "Ага. . ."
        "Я не понимаю.":
                $ GwenX.FaceChange("bemused", 1,Eyes="side")
                $ GwenX.Statup("Love", 90, 2)
                $ GwenX.Statup("Inbt", 50, 3)
                ch_g "Все в порядке, я понимаю, насколько это странно."
    ch_g "Все очевидно."
    ch_g "Если я попытаюсь игнорировать этот факт или. . . бороться с ним, то это в просто сократит мое \"экранное время\". . ."
    $ GwenX.FaceChange("sadside", 1)
    ch_g "А закончится все тем, что я просто превращусь в пустое место. . ."
    $ GwenX.FaceChange("angry", 1,Eyes="side")
    ch_g "Все обо мне забудут, словно меня никогда и не существовало."
    $ GwenX.FaceChange("angry", 1)
    ch_g "Так что. . . я постараюсь быть той [GwenX.Name_tvo], которая здесь нужна, с которой ты сможешь взаимодействовать."
    $ GwenX.FaceChange("sly", 1)
    if not Player.Male:
        ch_g "Тебе понравилось мое заявление, госпожа?"
    else:
        ch_g "Тебе понравилось мое заявление, господин?"
    menu:
        extend ""
        ". . .":
                $ GwenX.Statup("Love", 90, -1)
                $ GwenX.Statup("Obed", 200, 5)
                $ GwenX.Statup("Inbt", 50, 1)
                $ GwenX.FaceChange("confused", 1)
                ch_g "Лааадно. . ."
                ch_g "Я приму такой ответ за \"да. . .\""
                $ GwenX.FaceChange("sly", 1)
        "Конечно, звучит неплохо.":
                $ GwenX.Statup("Love", 60, 3)
                $ GwenX.Statup("Love", 90, 3)
                $ GwenX.Statup("Obed", 90, 5)
                if not Player.Male:
                    $ GwenX.Petname = "госпожа"
                    $ GwenX.Petname_rod = "госпожи"
                    $ GwenX.Petname_dat = "госпоже"
                    $ GwenX.Petname_vin = "госпожу"
                    $ GwenX.Petname_tvo = "госпожой"
                    $ GwenX.Petname_pre = "госпоже"
                else:
                    $ GwenX.Petname = "господин"
                    $ GwenX.Petname_rod = "господина"
                    $ GwenX.Petname_dat = "господину"
                    $ GwenX.Petname_vin = "господина"
                    $ GwenX.Petname_tvo = "господином"
                    $ GwenX.Petname_pre = "господине"
                ch_g "Здорово. . . [GwenX.Petname]."
        "Ага, только не зови меня \"госпожой.\"" if not Player.Male:
                $ GwenX.Statup("Love", 60, 3)
                $ GwenX.Statup("Love", 90, 3)
                $ GwenX.Statup("Obed", 200, 3)
                $ GwenX.Statup("Inbt", 50, 2)
                ch_g "Без проблем, не буду тебе перечить. . . [GwenX.Petname]."
        "Ага, только не зови меня \"господином.\"" if Player.Male:
                $ GwenX.Statup("Love", 60, 3)
                $ GwenX.Statup("Love", 90, 3)
                $ GwenX.Statup("Obed", 200, 3)
                $ GwenX.Statup("Inbt", 50, 2)
                ch_g "Без проблем, не буду тебе перечить. . . [GwenX.Petname]."
        "А что от этого изменится?":
                $ GwenX.Statup("Love", 90, -1)
                $ GwenX.Statup("Obed", 200, 2)
                $ GwenX.Statup("Inbt", 50, 2)
                $ GwenX.Statup("Inbt", 80, 2)
                ch_g "Может, ничего и не изменится - главное, что все не станет хуже."
                menu:
                    extend ""
                    ". . .":
                            if not Player.Male:
                                $ GwenX.Petname = "госпожа"
                                $ GwenX.Petname_rod = "госпожи"
                                $ GwenX.Petname_dat = "госпоже"
                                $ GwenX.Petname_vin = "госпожу"
                                $ GwenX.Petname_tvo = "госпожой"
                                $ GwenX.Petname_pre = "госпоже"
                            else:
                                $ GwenX.Petname = "господин"
                                $ GwenX.Petname_rod = "господина"
                                $ GwenX.Petname_dat = "господину"
                                $ GwenX.Petname_vin = "господина"
                                $ GwenX.Petname_tvo = "господином"
                                $ GwenX.Petname_pre = "господине"
                    "Ладно, но не зови меня \"госпожой.\"." if not Player.Male:
                            $ GwenX.Statup("Inbt", 80, 2)
                            ch_g "Как прикажете, мэм."
                    "Ладно, но не зови меня \"господином.\"." if Player.Male:
                            $ GwenX.Statup("Inbt", 80, 2)
                            ch_g "Как прикажете, босс."
                    "Ладно, в этом есть смысл.":
                            $ GwenX.Statup("Obed", 200, 2)
                            if not Player.Male:
                                $ GwenX.Petname = "госпожа"
                                $ GwenX.Petname_rod = "госпожи"
                                $ GwenX.Petname_dat = "госпоже"
                                $ GwenX.Petname_vin = "госпожу"
                                $ GwenX.Petname_tvo = "госпожой"
                                $ GwenX.Petname_pre = "госпоже"
                            else:
                                $ GwenX.Petname = "господин"
                                $ GwenX.Petname_rod = "господина"
                                $ GwenX.Petname_dat = "господину"
                                $ GwenX.Petname_vin = "господина"
                                $ GwenX.Petname_tvo = "господином"
                                $ GwenX.Petname_pre = "господине"
        "Я даже не знаю.":
                $ GwenX.Statup("Obed", 200, 1)
                $ GwenX.Statup("Inbt", 80, 3)
                ch_g "Понимаю. Ладно, я пока не буду звать тебя так. . ."
    $ GwenX.Statup("Obed", 90, 10)
    ch_g "Дай мне знать, если я могу что-то для тебя сделать. . . как-нибудь помочь тебе."
    $ GwenX.Statup("Obed", 90, 10)
    ch_g "Я. . . сделаю все возможное."
    $ GwenX.History.append("sir")
    $ GwenX.Petnames.append("sir")
    return


#label Gwen_Sub_Asked:
#    $ Line = 0
#    $ GwenX.FaceChange("sadside", 1)
#    ch_g "Yeah. You didn't seem into the idea."
#    menu:
#        extend ""
#        "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
#                if "sir" in GwenX.Petnames and ApprovalCheck(GwenX, 850, "O"):
#                        #if this is asking about the "master" name, and her Obedience is higher than 700
#                        pass
#                elif ApprovalCheck(GwenX, 550, "O"):
#                        #if it's instead about earning the "sir" title, and her approval is over 500
#                        pass
#                else: #if it failed both those things,
#                        $ GwenX.FaceChange("angry", 1)
#                        ch_g "It was a bad idea, don't worry about it." #Failed again. :(
#                        $ Line = "rude"

#                if Line != "rude":
#                        $ GwenX.Statup("Love", 90, 10)
#                        $ GwenX.FaceChange("sly", 1)
#                        ch_g "Well, it's not like you stopped ordering me around anyway."
#                        ch_g "Ok, let's give it a shot."

#        "I know it's what you want. Do you want to try again, or not?":
#                $ GwenX.FaceChange("bemused", 1)
#                if "sir" in GwenX.Petnames:
#                    if ApprovalCheck(GwenX, 850, "O"):
#                        ch_g "Ok, fine."
#                    else:
#                        ch_g "Nah, I'm good."
#                        $ Line = "rude"
#                elif ApprovalCheck(GwenX, 600, "O"):
#                        #if it's instead about earning the "sir" title, and her approval is over 500
#                        $ GwenX.FaceChange("confused", 1)
#                        ch_g "Kinda wishy-washy there."
#                        $ GwenX.FaceChange("sly", 1)
#                        ch_g "but maybe you're right."
#                        ch_g "Are you sure you're into this?"
#                        menu:
#                            extend ""
#                            "Yes, I'm sorry I was mean about it.":
#                                            $ GwenX.Statup("Love", 90, 15)
#                                            $ GwenX.Statup("Inbt", 50, 10)
#                                            $ GwenX.FaceChange("bemused", 1)
#                                            $ GwenX.Eyes = "side"
#                                            ch_g "Ok then."
#                            "You're damned right I am, bitch.":
#                                    if "sir" in GwenX.Petnames and ApprovalCheck(GwenX, 900, "O"):
#                                            $ GwenX.Statup("Love", 200, -5)
#                                            $ GwenX.Statup("Obed", 200, 10)
#                                            ch_g ". . ."
#                                    elif ApprovalCheck(GwenX,700, "O"):
#                                            $ GwenX.Statup("Love", 200, -5)
#                                            $ GwenX.Statup("Obed", 200, 10)
#                                            ch_g "Hmmm. . ."
#                                    else: #if it failed both those things,
#                                            $ GwenX.Statup("Love", 200, -10)
#                                            $ GwenX.Statup("Obed", 90, -10)
#                                            $ GwenX.Statup("Obed", 200, -10)
#                                            $ GwenX.Statup("Inbt", 50, -15)
#                                            $ GwenX.FaceChange("angry", 1)
#                                            ch_g "Wow, that's pushing it."
#                                            $ Line = "rude"
#                            "Ok, never mind then.":
#                                            $ GwenX.FaceChange("angry", 1)
#                                            $ GwenX.Statup("Love", 200, -10)
#                                            $ GwenX.Statup("Obed", 90, -10)
#                                            $ GwenX.Statup("Obed", 200, -10)
#                                            $ GwenX.Statup("Inbt", 50, -15)
#                                            ch_g "I was thinking of taking orders from you, not mindgames."
#                                            ch_g "I should've known you'd be like this."
#                                            $ Line = "rude"

#    $ GwenX.RecentActions.append("asked sub")
#    $ GwenX.DailyActions.append("asked sub")
#    if Line == "rude":
#            #If line hasn't been set to "rude" by something above, then it skips right past this
#            hide Gwen_Sprite with easeoutright
#            call Remove_Girl(GwenX)
#            $ GwenX.RecentActions.append("angry")
#            if "Historia" not in Player.Traits:
#                    $ renpy.pop_call()
#            "[GwenX.Name] checks you as she stomps out of the room."
#    elif "sir" in GwenX.Petnames:
#            #it didn't fail and "sir" was covered
#            $ GwenX.Statup("Obed", 200, 50)
#            $ GwenX.Petnames.append("master")
#            $ GwenX.Petname = Terms["master"]
#            $ GwenX.Eyes = "sly"
#            ch_g ". . . [Terms['master']]. . ."
#    else:
#            #it didn't fail
#            $ GwenX.Statup("Obed", 200, 30)
#            $ GwenX.Petnames.append("sir")
#            $ GwenX.Petname = Terms["sir"]
#            $ GwenX.FaceChange("sly", 1)
#            ch_g ". . . [Terms['sir']]."
#    return

# end Gwen_Sub//////////////////////////////////////////////////////////


# start Gwen_Master//////////////////////////////////////////////////////////

label Gwen_Master:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(GwenX,"bemused","выглядит необычайно покорной. . .")
            return
    $ GwenX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    call Shift_Focus(GwenX)
    if GwenX.Loc != bg_current and GwenX not in Party:
        "Вдруг [GwenX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить."

    $ Event_Queue = [0,0]
    $ GwenX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(GwenX)
    call CleartheRoom(GwenX)
    $ GwenX.ArmPose = 2
    call Set_The_Scene
    $ GwenX.DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ GwenX.FaceChange("sly", 1,Mouth="kiss")
    ch_g "Слушай, я тут подумала кое о чем. . ."
    $ GwenX.FaceChange("sad", 1)
    ch_g "Я рассказывала тебе о своем первом \"боссе?\""
    $ GwenX.FaceChange("sadside", 1)
    ch_g "-ну, когда я была в мире комиксов."
    menu:
        extend ""
        ". . .":
                pass
                $ GwenX.Statup("Love", 90, -1)
                $ GwenX.Statup("Obed", 200, 2)
        "Нет.":
                $ GwenX.Statup("Love", 90, 1)
                $ GwenX.Statup("Inbt", 50, 2)
                ch_g "Для этого есть веская причина. . ."
        "Да, скорее всего.":
                $ GwenX.FaceChange("confused", 1)
                $ GwenX.Statup("Love", 90, 2)
                $ GwenX.Statup("Obed", 200, 2)
                ch_g "Правда? . . . Нет, подожди!"
                $ GwenX.FaceChange("angry", 1)
                $ GwenX.Statup("Love", 90, -4)
                ch_g "Ты меня обманываешь!"
                $ GwenX.FaceChange("sadside", 1)
        "Ну вот, опять этот бред. . .":
                $ GwenX.Statup("Love", 90, -3)
                $ GwenX.Statup("Obed", 200, 2)
                ch_g "Ага. . ."
                $ GwenX.Statup("Inbt", 50, 2)
                ch_g "Просто. . . выслушай меня, хорошо?"
    ch_g "Моим первым боссом был, хочешь верь, хочешь нет. . ."
    ch_g "МОДОК."
    menu:
        extend ""
        "Хм.":
                $ GwenX.FaceChange("sad", 1)
                $ GwenX.Statup("Obed", 200, 2)
                ch_g "Ага, \"Мобильный Организм Для Организации Катастроф.\""
        "Мутировавший Организм Для Особых Поцелуев?":
                $ GwenX.FaceChange("perplexed", 1)
                $ GwenX.Statup("Love", 70, 2)
                $ GwenX.Statup("Love", 90, 1)
                ch_g "Роуг? Нет, не она."
                $ GwenX.FaceChange("sad", 1)
                $ GwenX.Statup("Inbt", 50, 2)
                ch_g "\"Мобильный Организм Для Организации Катастроф.\""
                $ GwenX.ArmPose = 1
                $ GwenX.FaceChange("confused", 1)
                $ GwenX.Statup("Obed", 200, 2)
                ch_g "Хм, интересно, значит и такой вариант ответа был."
                $ GwenX.ArmPose = 1
        "Мобильный Организм Для Организации Катастроф?":
                $ GwenX.FaceChange("surprised", 1)
                $ GwenX.Statup("Love", 70, 1)
                $ GwenX.Statup("Love", 90, 1)
                $ GwenX.Statup("Obed", 200, 3)
                if not Player.Male:
                    ch_g "Нет, \"Мобильный Организм Для Орг-\" А, да, ты поняла."
                else:
                    ch_g "Нет, \"Мобильный Организм Для Орг-\" А, да, ты понял."
                $ GwenX.Statup("Obed", 200, 1)
                $ GwenX.FaceChange("normal", 1)
                ch_g "Множественные выборы - это круто!"
    $ GwenX.FaceChange("angry", 1,Eyes="side")
    ch_g "Он был летающей головой размером с джакузи и мог стрелять лучами смерти из своего лба."
    $ GwenX.FaceChange("angry", 1,Eyes="surprised")
    ch_g "Он воспользовался ими, чтобы убить моего друга, а потом сказал, что я должна работать на него."
    $ GwenX.FaceChange("angry", 1,Eyes="side")
    ch_g "Это был не лучший старт новой работы."
    menu:
        ". . .":
                $ GwenX.Statup("Love", 90, -1)
        "Жестко, жаль, что так вышло.":
                $ GwenX.FaceChange("bemused", 1)
                $ GwenX.Statup("Love", 80, 3)
                $ GwenX.Statup("Love", 90, 2)
                ch_g "Спасибо. . ."
        "Да, это не правильно.":
                $ GwenX.FaceChange("angry", 1)
                $ GwenX.Statup("Love", 80, 1)
                $ GwenX.Statup("Love", 90, 1)
                $ GwenX.Statup("Inbt", 80, 2)
                ch_g "Так точно!"
        "Ха!":
                $ GwenX.FaceChange("angry", 1)
                $ GwenX.Statup("Love", 90, -3)
                $ GwenX.Statup("Love", 200, -1)
                $ GwenX.Statup("Obed", 200, 4)
                if not Player.Male:
                    ch_g "Читай ситуацию, коза."
                else:
                    ch_g "Читай ситуацию, козел."
    $ GwenX.FaceChange("angry", 1,Eyes="side")
    ch_g "Правда, это продлилось не долго."
    $ GwenX.FaceChange("angry", 1,Mouth="smile")
    ch_g "Через пару недель я запустила его в космос и заняла его место."
    ch_g "Нельзя держать в себе зло, нужно мстить."
    menu:
        extend ""
        ". . .":
                $ GwenX.Statup("Obed", 200, 2)
        "И правильно.":
                $ GwenX.FaceChange("smile", 1)
                $ GwenX.Statup("Love", 80, 2)
                $ GwenX.Statup("Love", 90, 1)
                $ GwenX.Statup("Inbt", 50, 2)
                ch_g "Ха, ага, по крайней мере, иногда это работает."
        "Мне уже стоит начать волноваться?":
                $ GwenX.FaceChange("smile", 1,Mouth="open")
                $ GwenX.Statup("Love", 90, 2)
                ch_g "Ха!"
                $ GwenX.FaceChange("normal", 1)
                $ GwenX.Statup("Obed", 200, 3)
                ch_g "Нет, все хорошо. . ."
    if "lover" in GwenX.Petnames:
            $ GwenX.FaceChange("normal", 2)
            $ GwenX.Statup("Love", 200, 25)
            if not Player.Male:
                ch_g "Ты совсем не такая."
                $ GwenX.Statup("Obed", 200, 20)
                ch_g "Ты могла воспользоваться ситуацией, но вместо этого была добра ко мне."
            else:
                ch_g "Ты совсем не такой."
                $ GwenX.Statup("Obed", 200, 20)
                ch_g "Ты мог воспользоваться ситуацией, но вместо этого был добр ко мне."
    if "boyfriend" in GwenX.Petnames:
            $ GwenX.FaceChange("normal", 1)
            ch_g "Наши отношения не ограничиваются рамками \"хозяин\" - \"слуга.\""
    if "fuckbuddy" in GwenX.Petnames:
        $ GwenX.FaceChange("sly", 1)
        if Player.Male:
            ch_g "Я уже привыкла к тому, что ты разрываешь меня своим буром."
        else:
            ch_g "Я уже привыкла к тому, что ты разрываешь мою киску."
        $ GwenX.Statup("Obed", 200, 10)
    if "sexfriend" in GwenX.Petnames:
            $ GwenX.FaceChange("sly", 1)
            ch_g "Думаю, мы пришли к взаимовыгодным отношениям. . ."
    if "boyfriend" not in GwenX.Petnames:
            $ GwenX.FaceChange("sadside", 1)
            ch_g "Несмотря на наши разногласия. . ."
            $ GwenX.FaceChange("sad", 1)
            ch_g ". . . ты все равно намного лучше, чем он."
    else:
            ch_g ". . . ты намного лучше, чем он."
            ch_g "Но что поделать. . ."
            $ GwenX.FaceChange("bemused", 1,Eyes="side")
            ch_g "Такова уж была природа того существа."
    ch_g "В подобных играх главное - это секс."
    if "boyfriend" not in GwenX.Petnames:
            ch_g "Или ты принимаешь это, или тебя забудут."
            $ GwenX.Statup("Obed", 200, 10)
            ch_g "Я не хочу быть забытой. . ."
            $ GwenX.Statup("Obed", 200, 10)
            ch_g "Только не снова. . ."
            if "sexfriend" in GwenX.Petnames:
                    $ GwenX.FaceChange("sly", 1,Eyes="side")
                    ch_g "И ты знаешь, что я не против. . ."
            $ GwenX.FaceChange("sad", 1)
            $ GwenX.Statup("Obed", 200, 10)
            ch_g "Так что, думаю, я твоем распоряжении. . ."
    else:
            $ GwenX.FaceChange("normal", 1,Brows="sad")
            if not Player.Male:
                ch_g "Я знаю, что ты другая. . ."
            else:
                ch_g "Я знаю, что ты другой. . ."
            if "lover" in GwenX.Petnames:
                    ch_g "Я знаю, что ты любишь меня такой, какая я есть. . ."
            else:
                    ch_g "Я знаю, что ты заботишься обо мне. . ."
            if "sexfriend" in GwenX.Petnames:
                    $ GwenX.FaceChange("sly", 1)
                    ch_g "И ты знаешь, что я не против. . ."
            if not Player.Male:
                ch_g "-но, чтобы ты знала, я готова следовать за тобой. . ."
            else:
                ch_g "-но, чтобы ты знал, я готова следовать за тобой. . ."
    if not Player.Male:
        ch_g ". . . хозяйка."
    else:
        ch_g ". . . хозяин."
    menu:
        extend ""
        ". . .":
                if not Player.Male:
                    $ GwenX.Petname = "хозяйка"
                    $ GwenX.Petname_rod = "хозяйки"
                    $ GwenX.Petname_dat = "хозяйке"
                    $ GwenX.Petname_vin = "хозяйку"
                    $ GwenX.Petname_tvo = "хозяйкой"
                    $ GwenX.Petname_pre = "хозяйке"
                else:
                    $ GwenX.Petname = "хозяин"
                    $ GwenX.Petname_rod = "хозяина"
                    $ GwenX.Petname_dat = "хозяину"
                    $ GwenX.Petname_vin = "хозяина"
                    $ GwenX.Petname_tvo = "хозяином"
                    $ GwenX.Petname_pre = "хозяине"
                $ GwenX.FaceChange("smile", 2, Eyes="side")
                $ GwenX.Statup("Obed", 200, 2)
                ch_g "Эм. . . хорошо."
                $ GwenX.FaceChange("normal", 1)
        "Звучит неплохо.":
                if not Player.Male:
                    $ GwenX.Petname = "хозяйка"
                    $ GwenX.Petname_rod = "хозяйки"
                    $ GwenX.Petname_dat = "хозяйке"
                    $ GwenX.Petname_vin = "хозяйку"
                    $ GwenX.Petname_tvo = "хозяйкой"
                    $ GwenX.Petname_pre = "хозяйке"
                else:
                    $ GwenX.Petname = "хозяин"
                    $ GwenX.Petname_rod = "хозяина"
                    $ GwenX.Petname_dat = "хозяину"
                    $ GwenX.Petname_vin = "хозяина"
                    $ GwenX.Petname_tvo = "хозяином"
                    $ GwenX.Petname_pre = "хозяине"
                $ GwenX.FaceChange("normal", 1)
                $ GwenX.Statup("Love", 90, 1)
                $ GwenX.Statup("Obed", 200, 2)
                $ GwenX.Statup("Inbt", 80, 2)
        "Мне не особо нравится такое обращение ко мне":
                $ GwenX.FaceChange("normal", 1)
                $ GwenX.Statup("Love", 90, 2)
                $ GwenX.Statup("Obed", 200, 3)
                if not Player.Male:
                    ch_g "Как скажете, мэм!"
                else:
                    ch_g "Как скажете, босс!"
    $ GwenX.Petnames.append("master")
    $ GwenX.History.append("master")
    ch_g "Если тебе что-нибудь понадобится, просто дай мне знать!"
    return

# end Gwen_Master//////////////////////////////////////////////////////////



# start Gwen_Sexfriend//////////////////////////////////////////////////////////

label Gwen_Sexfriend:   #Gwen_Update
        if GwenX.Loc != bg_current:
                "[GwenX.Name] подходит к вам и отводит в сторону."
        else:
                "[GwenX.Name] поворачивается к вам."
        $ GwenX.Loc = bg_current
        $ Event_Queue = [0,0]
        $ GwenX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(GwenX)
        call Set_The_Scene
        $ GwenX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in GwenX.History:
                call expression GwenX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        $ Line = 0
        $ GwenX.FaceChange("sly",2,Eyes="side")
        $ GwenX.Petnames.append("sex friend")

        ch_g "Знаешь, здесь довольно весело. . ."
        menu:
            ". . .":
                    pass
            "Да?":
                    $ GwenX.Statup("Love", 90, 2)
                    $ GwenX.Statup("Inbt", 90, 2)
            "О чем ты?":
                    $ GwenX.Statup("Love", 90, -2)
                    $ GwenX.Statup("Obed", 90, 2)
        $ GwenX.FaceChange("sly", 1)
        ch_g "В смысле, весело для порно-игры и всего такого. . ."
        menu:
            ". . .":
                    $ GwenX.Statup("Inbt", 90, 5)
            "Ох, опять этот бред. . .":
                    $ GwenX.FaceChange("angry", 1,Mouth="smirk")
                    $ GwenX.Statup("Love", 90, -5)
                    $ GwenX.Statup("Obed", 90, 5)
                    ch_g "Ох, успокойся."
                    $ GwenX.FaceChange("normal", 1)
                    $ GwenX.Statup("Inbt", 90, 5)
                    ch_g "Я просто хочу сказать, что у вас тут отлично. . ."
        $ GwenX.FaceChange("normal", 1)
        ch_g "У вас тут и бассейн, и хороший торговый центр, и голоплощадка. . ."
        $ GwenX.FaceChange("sly", 1)
        if GwenX.SEXP >= 30: #max around 200
                ch_g "И секс штучки тоже неплохи. . ."
        else:
                ch_g "И секс штучки тоже, наверное, не так уж и плохи. . ."
        ch_g "Так зачем все портить, если все хорошо?"
        if "lover" in GwenX.Petnames:
                $ GwenX.FaceChange("normal", 2)
                ch_g "Я очень люблю тебя, так что секс это просто \"дополнение,\""
                $ GwenX.FaceChange("sly", 1)
                $ GwenX.Statup("Inbt", 90, 5)
                ch_g "Но -приятное- дополнение."
        if GwenX in Player.Harem:
                $ GwenX.FaceChange("bemused", 1)
                $ GwenX.Statup("Inbt", 90, 2)
                ch_g "Мне нравится встречаться с тобой, но я знаю, как это бывает, это не может длиться вечно. . ."
        elif "master" in GwenX.Petnames:
                $ GwenX.FaceChange("sly", 1,Brows="sad")
                ch_g "Я знаю, что между нами отношения хозяин/слуга. . ."
                $ GwenX.Statup("Inbt", 90, 3)
                ch_g ". . .но я знаю, как это бывает, это не может длиться вечно. . ."
        $ GwenX.FaceChange("sexy", 1)
        ch_g "Если ты когда-нибудь захочешь стать моим полноценным \"секс-партнером,\" знай, я не против."
        ch_g "Только. . . иногда забегай ко мне \"на чай\". . ."
        $ GwenX.Statup("Love", 90, 10)
        $ GwenX.Statup("Obed", 90, 5)
        $ GwenX.Statup("Inbt", 90, 15)
        if Taboo:
            ch_g "Ну так что, не хочешь пойти в более уединенное место?"
            menu:
                extend ""
                "Хочу":
                        ch_g "Клево."
                        if bg_current == "bg player":
                                $ bg_current = "bg gwen"
                        else:
                                $ bg_current = "bg player"
                        $ GwenX.Loc = bg_current
                        $ Party = []
                        call Set_The_Scene
                        call CleartheRoom(GwenX)
                        call Set_The_Scene
                        $ Taboo = 0
                        $ GwenX.Taboo = 0

                "Нет, давай сделаем это здесь.":
                        $ GwenX.Statup("Obed", 80, 5)
                        $ GwenX.Statup("Inbt", 90, 15)
                        ch_g "Странный выбор."
                "Не сейчас.":
                        $ GwenX.FaceChange("sad", 1)
                        $ GwenX.Statup("Love", 90, -3)
                        $ GwenX.Statup("Obed", 90, 5)
                        ch_g "Оу!"
                        return
        else:
            ch_g "Что скажешь. . . если я предложу тебе провести время вместе прямо сейчас?"
            menu:
                extend ""
                "Конечно.":
                        $ GwenX.Statup("Love", 90, 3)
                        $ GwenX.Statup("Inbt", 90, 5)
                        ch_g "Клево."
                "Давай в другой раз.":
                        $ GwenX.FaceChange("sad", 1)
                        $ GwenX.Statup("Love", 90, -3)
                        $ GwenX.Statup("Obed", 90, 5)
                        ch_g "Оу!"
                        return
        $ Situation = GwenX
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        #end "if no relationship"
        jump Misplaced
        return

# end Gwen_Sexfriend//////////////////////////////////////////////////////////


# start Gwen_Fuckbuddy//////////////////////////////////////////////////////////

label Gwen_Fuckbuddy:
        $ Event_Queue = [0,0]
        $ GwenX.DailyActions.append("relationship")
        $ GwenX.Lust = 60
        $ GwenX.Wet = 2
        $ GwenX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        #change Gwen's outfit to default
        $ GwenX.Loc = bg_current
        call Shift_Focus(GwenX)
        call Set_The_Scene(0)
        $ GwenX.Outfit = "casual1"
        $ GwenX.OutfitDay = "casual1"
        $ GwenX.OutfitChange("casual1")
        call Display_Girl(GwenX)
        call Taboo_Level

        $ GwenX.Petnames.append("fuck buddy")
        #$ GwenX.Event[10] += 1

        $ GwenX.FaceChange("sexy", 2,Eyes="side")
        ch_g "Ого, я. . . чувствую похоть. . ."
        $ GwenX.FaceChange("sexy", 2)
        ch_g "Только я это чувсивую, или ты тоже?"
        menu:
            extend ""
            ". . .":
                    $ GwenX.FaceChange("bemused", 2)
                    $ GwenX.Statup("Obed", 90, 5)
                    $ GwenX.Statup("Inbt", 200, 5)
                    $ GwenX.Statup("Lust", 90, 5)
                    $ GwenX.FaceChange("bemused", 2)
                    ch_g "Наверное, только я. . ."
            "Ага, я тоже.":
                    $ GwenX.FaceChange("normal", 2)
                    $ GwenX.Statup("Love", 95, 5)
                    $ GwenX.Statup("Inbt", 200, 5)
                    $ GwenX.Statup("Lust", 90, 5)
                    ch_g "Правда?"
            "Только ты.":
                    $ GwenX.FaceChange("bemused", 2,Eyes="side")
                    $ GwenX.Statup("Love", 90, -3)
                    $ GwenX.Statup("Obed", 90, 5)
                    $ GwenX.Statup("Lust", 90, -5)
                    ch_g "Ну ладно. . ."
        $ GwenX.FaceChange("sly", 2)
        ch_g "Ты знаешь, что это меня очень беспокоит?"

        if GwenX.SEXP >= 100: #max around 200
                ch_g "-этот постоянный секс. . ."
        $ GwenX.FaceChange("bemused", 2,Eyes="side")
        ch_g "-thoughts about sex. . ."
        $ GwenX.FaceChange("manic", 2)
        ch_g "-а здесь может быть так хорошо, понимаешь?"
        menu:
            extend ""
            ". . .":
                    $ GwenX.FaceChange("bemused", 2,Eyes="side")
                    $ GwenX.Statup("Obed", 90, 2)
                    $ GwenX.Statup("Inbt", 200, 5)
                    ch_g "Наверное, не понимаешь. . ."
            "Наверное?":
                    $ GwenX.FaceChange("bemused", 2,Eyes="side")
                    $ GwenX.Statup("Love", 90, 3)
                    $ GwenX.Statup("Obed", 90, 2)
                    $ GwenX.Statup("Inbt", 200, 5)
                    ch_g "Думаю, тебе просто не с чем сравнивать. . ."
            "Ты о чем?":
                    $ GwenX.FaceChange("sly", 2,Brows="angry")
                    $ GwenX.Statup("Love", 90, -5)
                    $ GwenX.Statup("Obed", 90, 2)
                    $ GwenX.Statup("Inbt", 200, 5)
                    ch_g "Ох, заткнись, дай мне насладиться моментом. . ."
        $ GwenX.Statup("Lust", 90, 5)
        $ GwenX.FaceChange("surprised", 2,Mouth="open")
        ch_g "Я хочу больше наслаждения!"
        $ GwenX.Statup("Inbt", 200, 5)
        $ GwenX.FaceChange("sexy", 2)
        if GwenX.SEXP >= 150: #max around 200
                $ GwenX.Statup("Obed", 90, 5)
                $ GwenX.Statup("Lust", 90, 2)
                ch_g "Мы довольно много раз приятно проводили время вместе."
                $ GwenX.Statup("Lust", 90, 3)
                ch_g "Но я хочу еще больше. . ."
        elif GwenX.SEXP >= 60: #max around 200
                $ GwenX.Statup("Obed", 90, 5)
                $ GwenX.Statup("Lust", 90, 2)
                ch_g "Мы попробовали несколько вещей, но я чувствую, что многое упускаю!"
                $ GwenX.Statup("Lust", 90, 2)
                $ GwenX.FaceChange("sexy", 2,Mouth="open")
                ch_g "Давай попробуем все!"
        else:
                $ GwenX.Statup("Obed", 90, 10)
                $ GwenX.Statup("Inbt", 200, 5)
                $ GwenX.Statup("Lust", 90, 3)
                ch_g "Мне кажется, что мы почти не занимались ни чем интересным!"
                $ GwenX.Statup("Lust", 90, 3)
                $ GwenX.FaceChange("angry", 2,Mouth="open")
                ch_g "Почему бы тебе не трахать меня больше?!"

        if "lover" in GwenX.Petnames:
                $ GwenX.Statup("Love", 200, 5)
                $ GwenX.Statup("Inbt", 200, 5)
                $ GwenX.FaceChange("bemused", 2,Eyes="side")
                ch_g "Я люблю тебя, правда, но иногда мне просто нужна хорошая, жесткая порка!"
                $ GwenX.FaceChange("sly", 2)
        elif "master" in GwenX.Petnames:
                $ GwenX.FaceChange("sly",2,Brows="sad")
                $ GwenX.Statup("Obed", 200, 5)
                $ GwenX.Statup("Inbt", 200, 5)
                ch_g "Если ты не захочешь, я пойму, правда. . ."
                $ GwenX.FaceChange("sly", 2)
                ch_g "-но иногда мне просто нужна хорошая, жесткая порка!"
        else:
                $ GwenX.FaceChange("sly", 2)
                ch_g "Веселье весельем, но иногда мне просто нужна хорошая, жесткая порка!"
        $ GwenX.Statup("Love", 90, 10)
        $ GwenX.Statup("Obed", 90, 5)
        $ GwenX.Statup("Inbt", 200, 15)
        ch_g "Просто относись ко мне, как к своей \"подстилке\" или типа того!"
        if Taboo:
            ch_g "Ну так что, хочешь пойти в более уединенное место?"
            menu:
                extend ""
                "Ага":
                        ch_g "Клево."
                        if bg_current == "bg player":
                                $ bg_current = "bg gwen"
                        else:
                                $ bg_current = "bg player"
                        $ GwenX.Loc = bg_current
                        call CleartheRoom(GwenX)
                        call Set_The_Scene
                        $ Taboo = 0
                        $ GwenX.Taboo = 0

                "Нет, давай сделаем все здесь.":
                        $ GwenX.Statup("Obed", 80, 5)
                        $ GwenX.Statup("Inbt", 200, 15)
                        ch_g "Хорошо."
                "Не сейчас.":
                        $ GwenX.FaceChange("sad", 1)
                        $ GwenX.Statup("Love", 90, -3)
                        $ GwenX.Statup("Obed", 90, 5)
                        ch_g "Оу!"
                        return
        else:
            ch_g "Эм. . . не хочешь начать уже сейчас?"
            menu:
                extend ""
                "Конечно.":
                        $ GwenX.Statup("Love", 90, 3)
                        $ GwenX.Statup("Inbt", 200, 5)
                        ch_g "Клево."
                "Давай в другой раз.":
                        $ GwenX.FaceChange("sad", 1)
                        $ GwenX.Statup("Love", 90, -3)
                        $ GwenX.Statup("Obed", 90, 5)
                        ch_g "Оу!"
                        return
        $ Situation = GwenX
        $ Player.AddWord(1,"interruption") #adds to Recent
        call Girl_SexPrep              #she offers sex
        call SexMenu
        jump Misplaced
        return
# end Gwen_Fuckbuddy//////////////////////////////////////////////////////////

# start Gwen_Daddy//////////////////////////////////////////////////////////

#Not updated

label Gwen_Daddy:       #Gwen_Update
        $ Event_Queue = [0,0]
        $ GwenX.DailyActions.append("relationship")
        $ GwenX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(GwenX)
        if GwenX.Loc != bg_current:
                $ GwenX.Loc = bg_current
                "[GwenX.Name] подходит к вам."
        call Set_The_Scene
        $ GwenX.FaceChange("sadside",1,Mouth="normal")
        ch_g ". . ."
        ch_g "Я, эм. . . Я тут вспомнила. . ."
        $ GwenX.FaceChange("sadside",1,Mouth="smirk")
        ch_g "Кое-какую, эм. . . \"игру\". . ."
        $ GwenX.FaceChange("sadside",2,Mouth="smirk")
        ch_g "Ну знаешь. . ."
        ch_g "для взрослых. . ."
        $ GwenX.FaceChange("sad",2,Mouth="normal")
        ch_g "Ничего серьезного, но. . . могу ли я звать тебя. . ."
        $ GwenX.FaceChange("sadside",2,Mouth="normal")
        if not Player.Male:
            ch_g "\"мамочкой?\""
        else:
            ch_g "\"папочкой?\""
        menu:
            extend ""
            "Ладно?":
                $ GwenX.FaceChange("smile")
                $ GwenX.Statup("Love", 90, 20)
                $ GwenX.Statup("Obed", 60, 10)
                $ GwenX.Statup("Inbt", 80, 30)
                ch_g "Классно!"
            "Зачем?":
                $ GwenX.FaceChange("bemused")
                ch_g "Просто. . ."
                if GwenX.Love > GwenX.Obed and GwenX.Love > GwenX.Inbt:
                        ch_g "Я подумала, что это было бы весело. . ."
                elif GwenX.Obed > GwenX.Inbt:
                        if not Player.Male:
                            ch_g "ты была очень напористой. . ."
                        else:
                            ch_g "ты был очень напорист. . ."
                else:
                        ch_g "это странно, да?"

                menu:
                    extend ""
                    "Звучит интересно, меня устраивает.":
                            $ GwenX.FaceChange("smile")
                            $ GwenX.Statup("Love", 90, 15)
                            $ GwenX.Statup("Obed", 60, 20)
                            $ GwenX.Statup("Inbt", 80, 25)
                            ch_g "Отлично!"
                            $ GwenX.FaceChange("sly",2)
                            if not Player.Male:
                                ch_g " . . . мамочка."
                            else:
                                ch_g " . . . папочка."
                            $ GwenX.FaceChange("sly",1)
                            if not Player.Male:
                                $ GwenX.Petname = "мамочка"
                                $ GwenX.Petname_rod = "мамочки"
                                $ GwenX.Petname_dat = "мамочке"
                                $ GwenX.Petname_vin = "мамочку"
                                $ GwenX.Petname_tvo = "мамочкой"
                                $ GwenX.Petname_pre = "мамочке"
                            else:
                                $ GwenX.Petname = "папочка"
                                $ GwenX.Petname_rod = "папочки"
                                $ GwenX.Petname_dat = "папочке"
                                $ GwenX.Petname_vin = "папочку"
                                $ GwenX.Petname_tvo = "папочкой"
                                $ GwenX.Petname_pre = "папочке"
                    "Может, лучше не надо?":
                            $ GwenX.Statup("Love", 90, 5)
                            $ GwenX.Statup("Obed", 80, 40)
                            $ GwenX.Statup("Inbt", 80, 20)
                            $ GwenX.FaceChange("sad")
                            ch_g "   . . .   "
                            ch_g "Ну, ладно."
                    "У тебя серьезные проблемы с отцом, да?" if Player.Male:
                            $ GwenX.Statup("Love", 90, -15)
                            $ GwenX.Statup("Obed", 80, 45)
                            $ GwenX.Statup("Inbt", 70, 5)
                            $ GwenX.FaceChange("sadside",2)
                            ch_g "Ну. . . типа. . ."
                            ch_g "-но дело не в этом."
                            $ GwenX.FaceChange("sadside",1)
                    "У тебя серьезные проблемы с мамой, да?" if not Player.Male:
                            $ GwenX.Statup("Love", 90, -15)
                            $ GwenX.Statup("Obed", 80, 45)
                            $ GwenX.Statup("Inbt", 70, 5)
                            $ GwenX.FaceChange("sadside",2)
                            ch_g "Ну. . . типа. . ."
                            ch_g "-но дело не в этом."
                            $ GwenX.FaceChange("sadside",1)

            "У тебя серьезные проблемы с мамой, да?" if not Player.Male:
                    $ GwenX.Statup("Love", 90, -15)
                    $ GwenX.Statup("Obed", 80, 45)
                    $ GwenX.Statup("Inbt", 70, 5)
                    $ GwenX.FaceChange("sadside",2)
                    ch_g ". . . Я не знаю, может быть. . ."
                    ch_g "Забудь."
                    $ GwenX.FaceChange("sadside",1,Mouth="normal")
            "У тебя серьезные проблемы с отцом, да?" if Player.Male:
                    $ GwenX.Statup("Love", 90, -15)
                    $ GwenX.Statup("Obed", 80, 45)
                    $ GwenX.Statup("Inbt", 70, 5)
                    $ GwenX.FaceChange("sadside",2)
                    ch_g ". . . Я не знаю, может быть. . ."
                    ch_g "Забудь."
                    $ GwenX.FaceChange("sadside",1,Mouth="normal")
        $ GwenX.Petnames.append("daddy")
        return

# end Gwen_Daddy//////////////////////////////////////////////////////////



# Start Character Meet Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Meet Rogue / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Rogue_Meet:
        # GwenX.Event[2] tracks number of girls she knows you're dating
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = bg_current
        $ RogueX.Loc = bg_current
        $ GwenX.ArmPose = 2
        call Shift_Focus(GwenX)
        call Set_The_Scene
        $ GwenX.FaceChange("normal")
        ch_r "Слушай, [RogueX.Petname], а это кто?"
        if RogueX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                $ GwenX.Statup("Obed", 80, 5)
        $ GwenX.FaceChange("surprised",Eyes ="side",Mouth="open")
        $ GwenX.ArmPose = 1
        hide Rogue_Seated
        show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc)
        hide Gwen_Seated
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom -1
        $ GwenX.Hat = 0
        ch_g "О, ого! Роуг!"
        $ GwenX.FaceChange("normal",Eyes ="side")
        $ RogueX.FaceChange("confused",Eyes ="side")
        if RogueX.Name == "Роуг":
                ch_r "Да? . . . Мы ведь еще не знакомы?"
        else:
                ch_r "Да? . . . Вообще-то, меня сейчас зовут \"[RogueX.Name_tvo]\"."
                ch_r "Думаю, я еще с тобой не знакома. . ."
        $ GwenX.ArmPose = 2
        $ GwenX.FaceChange("sadside",Eyes ="side")
        ch_g "А, точно. . ."
        $ GwenX.FaceChange("smile",Eyes ="side")
        ch_g "Меня зовут Гвенбит. То есть Гвенпул. То есть Гвен. Меня зовут Гвен."
        if GwenX.Name != "Гвен":
                ch_g "Хотя я откликаюсь на \"[GwenX.Name]\"."
        ch_r "А ты знаешь про меня от. . ."
        ch_g "О, я твоя -БОЛЬШУЩАЯ- фанатка, я с самого детства читаю выпуски с тобой!"
        $ GwenX.FaceChange("kiss",1)
        $ RogueX.FaceChange("surprised",2,Eyes ="side")
        ch_g "\"Дай мне немного сладенького, сладенький!\""
        $ GwenX.FaceChange("normal",2,Eyes ="leftside")
        $ RogueX.FaceChange("confused",2,Eyes ="side")
        ch_g "Эм, я шучу. . . конечно. . ."
        $ GwenX.FaceChange("normal",1,Eyes ="side")
        $ RogueX.FaceChange("confused",1)
        ch_r "[RogueX.Petname], ты ее хорошо знаешь?"
        menu:
            extend ""
            "Не особо.":
                    $ GwenX.FaceChange("angry")
                    $ RogueX.FaceChange("smile")
                    $ GwenX.Statup("Love", 80, -5)
                    $ GwenX.Statup("Obed", 80, 5)
                    $ Line = "О, да ладно. . . "
            "Она из другой вселенной.":
                    $ GwenX.FaceChange("normal")
                    $ GwenX.Statup("Love", 80, 5)
                    $ GwenX.Statup("Obed", 80, 3)
                    $ GwenX.Statup("Inbt", 70, 3)
                    $ Line = "Ага! "
            "Она чекнутая.":
                    $ GwenX.FaceChange("angry")
                    $ RogueX.FaceChange("surprised")
                    $ GwenX.Statup("Love", 90, -5)
                    $ GwenX.Statup("Obed", 80, -2)
                    $ GwenX.Statup("Inbt", 70, 3)
                    ch_g ". . ."
                    $ Line = "Что?! Нет! "
        ch_g "[Line]Я из другой вселенной!"
        $ RogueX.FaceChange("confused",Eyes ="side")
        $ GwenX.FaceChange("smile",Eyes ="side")
        ch_g "Из той, где вы, ребята, встречаетесь в комиксах, фильмах, -играх-. . ."
        ch_r "А мы сейчас где? . ."
        ch_g "В игре."
        $ RogueX.FaceChange("confused")
        ch_r "Лаааадно. . . [[она смотрит на вас]."
        menu:
            extend ""
            "Возможно, это правда.":
                    $ GwenX.FaceChange("normal")
                    $ GwenX.Statup("Love", 80, 3)
                    $ GwenX.Statup("Inbt", 70, 5)
                    $ RogueX.Statup("Obed", 80, 1)
                    ch_g "Конечно, это правда!"
            "Я ей верю.":
                    $ GwenX.FaceChange("normal")
                    $ GwenX.Statup("Love", 80, 5)
                    $ GwenX.Statup("Obed", 80, 2)
                    $ RogueX.Statup("Love", 80, 1)
                    $ RogueX.Statup("Obed", 80, 1)
                    ch_g "Оу, это так мило!"
            "Это бред.":
                    $ GwenX.FaceChange("angry")
                    $ GwenX.Statup("Love", 90, -5)
                    $ GwenX.Statup("Obed", 80, 5)
                    $ RogueX.Statup("Obed", 80, 2)
                    ch_g "Никакой это не бред!"
            "[[Покрутить пальцем у виска]":
                    "Вы крутите пальцем так, чтобы [GwenX.Name] этого не заметила."
        $ GwenX.FaceChange("normal",Eyes ="side")
        $ RogueX.FaceChange("smile",Eyes ="side")
        ch_r "Ладно, пожалуй, мы можем пока согласиться с этим. . ."
        ch_r "Приятно познакомиться с тобой, [GwenX.Name]!"
        ch_g "Ах, а мне то как приятно, сладенькая!"
        $ RogueX.FaceChange("surprised",2,Eyes ="side")
        ch_r ". . ."
        $ RogueX.FaceChange("confused",1)
        $ GwenX.FaceChange("normal",2,Eyes ="side")
        ch_r "Я правда так говорю?"
        menu:
            extend ""
            "Постоянно.":
                    $ RogueX.FaceChange("angry",2)
                    $ GwenX.Statup("Love", 80, 2)
                    $ GwenX.Statup("Inbt", 70, 3)
                    $ RogueX.Statup("Love", 80, -2)
                    $ RogueX.Statup("Obed", 80, 3)
                    $ RogueX.Statup("Inbt", 70, -2)
                    if not Player.Male:
                        ch_r "Сладенькая, да я никогда-!"
                    else:
                        ch_r "Сладенький, да я никогда-!"
                    $ GwenX.FaceChange("smile",1)
                    ch_g "Видишь!"
            "Нет.":
                    $ RogueX.FaceChange("smile")
                    $ GwenX.FaceChange("angry",1)
                    $ GwenX.Statup("Love", 90, -2)
                    $ GwenX.Statup("Obed", 80, 3)
                    $ GwenX.Statup("Inbt", 70, -1)
                    $ RogueX.Statup("Love", 95, 3)
                    $ RogueX.Statup("Inbt", 70, 2)
            "Неееет. [[подмигнуть Гвен]":
                    $ RogueX.FaceChange("angry")
                    $ GwenX.FaceChange("smile",1)
                    $ GwenX.Statup("Love", 80, 3)
                    $ GwenX.Statup("Inbt", 70, 3)
                    $ RogueX.Statup("Love", 80, -2)
                    $ RogueX.Statup("Obed", 80, 4)
                    $ RogueX.Statup("Inbt", 70, -1)
            "[[Невозмутимо присвистнуть]":
                    $ RogueX.FaceChange("angry",1)
                    $ GwenX.Statup("Love", 80, 2)
                    $ GwenX.Statup("Inbt", 70, 2)
                    $ RogueX.Statup("Love", 80, -1)
                    $ RogueX.Statup("Obed", 80, 2)
                    $ RogueX.Statup("Inbt", 70, -1)
                    if not Player.Male:
                        ch_r "Сладенькая, да я никогда-!"
                    else:
                        ch_r "Сладенький, да я никогда-!"
                    $ GwenX.FaceChange("smile",1)
                    ch_g "Видишь!"
        $ GwenX.FaceChange("normal",Eyes ="side",Brows="sad")
        $ RogueX.FaceChange("smirk",1,Eyes ="side")
        ch_g "Извини-извини."
        $ GwenX.FaceChange("confused")
        ch_g "Так, что у вас с [Player.Name_tvo]?"
        $ RogueX.FaceChange("smile",2,Eyes ="side",Brows="sad")
        if RogueX in Player.Harem:
                ch_r "Ох, ну. . . мы. . . встречаемся?"
        elif RogueX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                if not Player.Male:
                    ch_r "Ох, ну. . . она моя. . . эм. . ."
                else:
                    ch_r "Ох, ну. . . он мой. . . эм. . ."
        elif not ApprovalCheck(RogueX, 500, "L"):
                $ RogueX.FaceChange("sadside",0)
                ch_r "Мы не очень-то и ладим. . ."
        else:
                $ RogueX.Blush = 1
                ch_r "Ох, мы, эм. . ."
        ch_r "Все сложно. . ."
        if RogueX in Player.Harem:
            if GwenX.Event[2] > 1:
                    #if gwen heard you were dating two+ girls
                    $ GwenX.Statup("Love", 90, -5)
                    $ GwenX.Statup("Inbt", 50, 1)
                    $ GwenX.Statup("Inbt", 80, 3)
                    ch_g "О. . . ха, ага, это со всеми происходит. . ."
                    $ GwenX.Statup("Obed", 50, 1)
                    $ GwenX.Statup("Obed", 80, 3)
            elif GwenX.Event[2]:
                    #if gwen heard you were dating someone else
                    $ GwenX.Statup("Love", 90, -5)
                    $ GwenX.Statup("Inbt", 50, 3)
                    $ GwenX.Statup("Inbt", 80, 3)
                    ch_g "О. . . значит и ты. . ."
                    $ GwenX.Statup("Obed", 50, 3)
                    $ GwenX.Statup("Obed", 80, 3)
            else:
                    $ GwenX.Statup("Love", 90, -2)
                    ch_g "О, это так мило. . ."
            $ GwenX.Event[2] += 1
        $ RogueX.FaceChange("smile",1)
        ch_g "Лааадно. . ."
        $ GwenX.FaceChange("normal",1)
        $ RogueX.GirlLikeUp(GwenX,100)
        $ GwenX.GirlLikeUp(RogueX,50)
        ch_g "Наверное, было полезно поболтать. . ."
        ch_r "Полагаю, мы еще увидимся."
        $ GwenX.DrainWord("Rogue",0,0,0,1)
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
        return
# End Meet Rogue / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Meet Kitty / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Kitty_Meet:
        # GwenX.Event[2] tracks number of girls she knows you're dating
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = bg_current
        $ KittyX.Loc = bg_current
        call Shift_Focus(GwenX)
        call Set_The_Scene
        $ GwenX.ArmPose = 2
        $ KittyX.ArmPose = 1
        $ GwenX.FaceChange("normal")
        ch_k "Слушай, [KittyX.Petname], это[KittyX.like]кто?"
        hide Kitty_Seated
        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc)
        hide Gwen_Seated
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom -1
        $ GwenX.Hat = 0
        $ GwenX.FaceChange("surprised",Eyes ="side")
        ch_g ". . ."
        $ KittyX.FaceChange("confused",1,Eyes="side")
        ch_k ". . ."
        $ GwenX.FaceChange("surprised",1,Eyes="side")
        $ GwenX.ArmPose = 1
        ch_g "!!!"
        ch_k "Кто-{w=1.0}{nw}"
        $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
        ch_g "УИИИИИИИ!!!!"
        $ KittyX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_k "Аааааа!"
        menu:
            extend ""
            ". . .":
                    pass
            "Аааааа! [[с сарказмом]":
                    $ GwenX.Statup("Love", 80, -1)
            "Аааааа! [[с чувством]":
                    pass
                    $ GwenX.Statup("Love", 80, 1)
                    $ KittyX.Statup("Obed", 80, 1)
        ch_g "УИИИИИИИ!!!!{w=0.2}{nw}"
        $ KittyX.FaceChange("surprised",1,Mouth="open")
        ch_k "Почему мы кричим?"
        menu:
            extend ""
            ". . .":
                    pass
            "Аааааа!":
                    $ GwenX.Statup("Love", 80, 1)
                    $ KittyX.Statup("Obed", 80, 1)
                    pass
            "Не знаю!":
                    $ GwenX.Statup("Love", 80, -1)
                    $ KittyX.Statup("Love", 80, 1)
                    $ KittyX.Statup("Obed", 80, 1)
                    pass
        ch_g "УИИИИИИИ!!!!{w=0.2}{nw}"
        $ GwenX.FaceChange("surprised",1,Eyes ="closed",Mouth="open")
        ch_g ". . . [[она тяжело дышит]"
        $ GwenX.FaceChange("smile",1,Eyes ="closed")
        $ KittyX.FaceChange("sad",1,Eyes="side")
        ch_g "Извини. . ."
        ch_g "Это Китти Прайд."
        if KittyX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                $ GwenX.Statup("Obed", 80, 5)
        $ GwenX.FaceChange("smile",1,Eyes ="surprised")
        $ KittyX.FaceChange("confused",1)
        ch_g "[Player.Name], это же Китти Прайд!"
        menu:
            extend ""
            "Ты о чем?":
                    $ GwenX.FaceChange("sly",1)
                    $ GwenX.Statup("Inbt", 80, 2)
                    ch_g "О, как будто ты не знаешь."
            "Китти? Да, я знаю.":
                    $ GwenX.FaceChange("sly",1)
                    $ GwenX.Statup("Love", 80, 1)
                    $ GwenX.Statup("Obed", 80, 2)
                    $ KittyX.Statup("Love", 80, 1)
                    if not Player.Male:
                        ch_g "\"Китти? Да, я знаю,\" ты типа крутая, да. . ?"
                    else:
                        ch_g "\"Китти? Да, я знаю,\" ты типа крутой, да. . ?"
            "Она не такая уж особенная.":
                    $ GwenX.FaceChange("sly",1)
                    $ GwenX.Statup("Love", 80, -1)
                    $ KittyX.Statup("Love", 80, -2)
                    $ KittyX.Statup("Obed", 50, 1)
                    $ KittyX.Statup("Obed", 80, 2)
                    $ KittyX.FaceChange("angry",1)
                    ch_g "Не такая -уж- особенная?!"
            "Правда?!":
                    $ KittyX.FaceChange("sly",2)
                    $ GwenX.Statup("Love", 80, 2)
                    $ KittyX.Statup("Love", 70, 2)
                    $ KittyX.Statup("Love", 90, 1)
                    ch_g ". . ."
        $ GwenX.FaceChange("surprised",1,Mouth="open")
        $ GwenX.ArmPose = 2
        ch_g "Она из чертова -Прайда Людей Икс!-"
        $ KittyX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_k "А? . . . Да!"
        ch_g "Она - одна из типичных подружек Росомахи!"
        $ KittyX.ArmPose = 2
        ch_k "Да-{w=1.0}{nw}"
        $ KittyX.FaceChange("confused",2,Eyes="side",Mouth="open")
        ch_k "Да-. . . подожди, что?!"
        $ GwenX.FaceChange("angry",1,Eyes ="leftside",Mouth="kiss")
        ch_g "Да, меня немного беспокоит, как часто он оказывается в паре с молодыми девчатами. . ."
        $ GwenX.FaceChange("normal",1,Eyes ="side")
        $ KittyX.FaceChange("confused",1,Eyes="side")
        ch_g "Но ты была его первой! (в истории выпусков)."
        ch_k "Подожди. . ."
        $ KittyX.FaceChange("sad",2,Eyes="leftside")
        ch_k "У нас с Логаном[KittyX.like]никогда не. . ."
        ch_k "Никогда[KittyX.like]ничего такого не было."
        $ GwenX.FaceChange("angry",1,Eyes ="leftside",Mouth="kiss")
        ch_g "А да, это место больше похоже на мультфильм. . ."
        $ GwenX.FaceChange("confused",1,Eyes ="side")
        if KittyX.like == ", как бы, ":
            ch_g "Ты когда-нибудь замечала, что говоришь \"как бы\", как бы. . . очень часто?"
            $ KittyX.FaceChange("confused",1,Eyes="side")
            ch_k "Эм[KittyX.like]что?"
            $ KittyX.FaceChange("sad",1,Eyes="leftside")
            ch_k "[KittyX.Like]нет."
        else:
            ch_g "Ты когда-нибудь замечала, что раньше говорила \"как бы\", как бы. . . очень часто?"
            $ KittyX.FaceChange("sad",1,Eyes="leftside")
            $ KittyX.Statup("Obed", 60, 2)
            $ KittyX.Statup("Obed", 80, 1)
            ch_k ". . ."
            ch_k "Я[KittyX.like]поработала над собой. . ."
        $ KittyX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_k "Так, минутку!"
        $ KittyX.FaceChange("confused",1,Mouth="open")
        ch_k "\"Мультфильм?\" О чем это она?"
        menu:
            extend ""
            "Без понятия.":
                    $ GwenX.FaceChange("angry",1)
                    $ GwenX.Statup("Love", 80, -2)
                    $ GwenX.Statup("Obed", 80, 2)
                    $ KittyX.Statup("Love", 80, 1)
                    ch_g "Эй!"
            "Она думает, что мы воображаемые.":
                    $ GwenX.FaceChange("normal",2,Brows="sad")
                    $ GwenX.Statup("Love", 80, 3)
                    $ GwenX.Statup("Obed", 80, 2)
                    $ GwenX.Statup("Inbt", 80, 2)
                    ch_g "Ну, воображаемые для моего мира."
            "Это сложно.":
                    $ GwenX.FaceChange("confused",1,Brows="sad")
                    $ GwenX.Statup("Love", 80, -1)
                    $ KittyX.Statup("Love", 80, 1)
                    $ KittyX.Statup("Obed", 80, 1)
                    ch_g "Это -не так уж- и сложно. . ."
        $ GwenX.FaceChange("normal",1,Eyes ="side",Brows="sad")
        ch_g "В мире, откуда я родом, вы, ребята, встречаетесь в комиксах, фильмах и мультфильмах."
        ch_k "Так. . . а мы сейчас. . ?"
        $ GwenX.FaceChange("normal",1,Eyes ="leftside",Brows="sad")
        ch_g "В. . . игре."
        $ KittyX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_k "О, как Final Fantasy! Мы будем сражаться с драконами?!"
        ch_g "Ну. . ."
        ch_g "У вас скорее. . . [[что-то мямлит]."
        $ KittyX.FaceChange("confused",1,Eyes="side")
        ch_k "В чем дело?"
        ch_g "Ваша игра скорее похожа на. . . \"эро-игру.\""
        ch_k "Эро-игру. . ?"
        if ApprovalCheck(KittyX, 2000):
                $ KittyX.FaceChange("surprised",1,Eyes="side",Mouth="smile")
                $ GwenX.Statup("Love", 80, 2)
                $ GwenX.Statup("Inbt", 80, 2)
                $ KittyX.Statup("Obed", 60, 2)
                $ KittyX.Statup("Obed", 80, 1)
                $ KittyX.Statup("Inbt", 60, 2)
                $ KittyX.Statup("Inbt", 80, 1)
                ch_k "Классно!"
        elif ApprovalCheck(KittyX, 1500):
                $ KittyX.FaceChange("sly",2,Eyes="side")
                $ KittyX.Statup("Love", 80, -1)
                $ KittyX.Statup("Obed", 60, 2)
                $ KittyX.Statup("Obed", 80, 1)
                ch_k "Понятно. . . а похоже. . ."
                $ KittyX.Statup("Inbt", 60, 2)
                $ KittyX.Statup("Inbt", 80, 1)
        elif ApprovalCheck(KittyX, 800):
                $ KittyX.FaceChange("surprised",2,Eyes="side",Mouth="open")
                $ GwenX.Statup("Love", 80, -2)
                $ GwenX.Statup("Obed", 80, 3)
                $ KittyX.Statup("Love", 80, -5)
                ch_k "Что? . . . Нет."
                $ KittyX.Statup("Obed", 60, 2)
                $ KittyX.Statup("Obed", 80, 2)
                $ KittyX.Statup("Inbt", 60, 2)
                $ KittyX.Statup("Inbt", 80, 2)
                ch_k "Это не так!"
        else:
                $ KittyX.FaceChange("surprised",2,Eyes="side")
                $ GwenX.Statup("Love", 80, -5)
                $ GwenX.Statup("Obed", 80, 10)
                $ KittyX.Statup("Love", 80, -15)
                $ KittyX.Statup("Obed", 60, 3)
                ch_k "Это многое объясняет."
                $ KittyX.FaceChange("angry",2,Mouth="open")
                $ KittyX.Statup("Obed", 80, 2)
                $ KittyX.Statup("Inbt", 60, 3)
                $ KittyX.Statup("Inbt", 80, 2)
                if not Player.Male:
                    ch_k "Ты в ней плоха, [Player.Name]."
                else:
                    ch_k "Ты в ней плох, [Player.Name]."
        $ GwenX.FaceChange("normal",1,Eyes ="side")
        ch_g "Так ты мне веришь?!"
        $ KittyX.FaceChange("smile",1,Eyes="side")
        ch_k "Ну[KittyX.like]ты веришь в свои слова, этого достаточно."
        ch_g "Это[KittyX.like]так!"
        ch_g "А вы с [Player.Name_tvo]. . ."
        if KittyX in Player.Harem:
                ch_k "О, мы встречаемся!"
                if GwenX.Event[2] > 1:
                        #if gwen heard you were dating two+ girls
                        $ GwenX.Statup("Love", 90, -5)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "О. . . ха, это здесь происходит со многими. . . мазл тов."
                        $ GwenX.Statup("Obed", 50, 1)
                        $ GwenX.Statup("Obed", 80, 3)
                elif GwenX.Event[2]:
                        #if gwen heard you were dating someone else
                        $ GwenX.Statup("Love", 90, -5)
                        $ GwenX.Statup("Inbt", 50, 3)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "О. . . эм, и ты тоже. . . мазл тов."
                        $ GwenX.Statup("Obed", 50, 3)
                        $ GwenX.Statup("Obed", 80, 3)
                else:
                        $ GwenX.Statup("Love", 90, -2)
                        ch_g "Мазл тов. . ."
                $ GwenX.Event[2] += 1
        elif KittyX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                if not Player.Male:
                    ch_k "Ох, ну. . . она, эм. . ."
                    ch_k "Моя [KittyX.Petname]. . ."
                else:
                    ch_k "Ох, ну. . . он, эм. . ."
                    ch_k "Мой [KittyX.Petname]. . ."
        elif not ApprovalCheck(KittyX, 500, "L"):
                $ KittyX.FaceChange("sadside",0)
                if not Player.Male:
                    ch_k "Ну, она та еще дура. . ."
                else:
                    ch_k "Ну, он тот еще придурок. . ."
                $ GwenX.GirlLikeUp(KittyX,10)
                ch_g "Ха, классика!"
        else:
                $ KittyX.Blush = 1
                ch_k "Ох, мы, эм. . ."
                ch_k "Все сложно."
        ch_g "Ох, в общем. . ."
        ch_g "Гвендолин Пул, к вашим услугам."
        ch_g "Некоторые зовут меня. . . \"[GwenX.Name_tvo].\""
        ch_k "Ладно, приятно было познакомиться с тобой, [GwenX.Name]. Мы как-нибудь еще увидимся?"
        ch_g "Да, конечно. . ."
        $ KittyX.GirlLikeUp(GwenX,100)
        $ GwenX.GirlLikeUp(KittyX,50)
        $ GwenX.FaceChange("normal",1)
        $ KittyX.FaceChange("smile",1)
        $ GwenX.DrainWord("Kitty",0,0,0,1)
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
        return
# End Meet Kitty / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Meet Emma / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Emma_Meet(Teach=0):
        if EmmaX.Loc == "bg teacher":
                $ Teach = 1
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = bg_current
        $ EmmaX.Loc = bg_current
        $ GwenX.ArmPose = 2
        call Shift_Focus(GwenX)
        call Set_The_Scene
        $ GwenX.FaceChange("normal")
        $ EmmaX.FaceChange("smile",1)
        ch_e "Здравствуй, [EmmaX.Petname]. . . а это, должно быть, наша новая студентка."
        if EmmaX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                $ GwenX.Statup("Obed", 60, 2)
                $ GwenX.Statup("Obed", 80, 5)
        $ EmmaX.FaceChange("smile",1,Eyes="side")
        ch_e "Мисс Пул, я полагаю?"
        $ GwenX.FaceChange("confused",1,Eyes="side")
        show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc)
        hide Gwen_Seated
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom -1
        $ GwenX.Hat = 0
        ch_g "Эм, да? Но я больше предпочитаю, когда меня зовут [GwenX.Name_tvo]. . ."
        ch_g ". . ."
        $ GwenX.ArmPose = 1
        ch_g "А вы кто такая?"
        ch_e "Ах, да, простите мои манеры, я мисс Фрост, я здесь преподаю."
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        $ EmmaX.FaceChange("confused",1,Eyes="side",Mouth="normal")
        $ GwenX.ArmPose = 2
        ch_g "Подождите-ка, -Эмма- Фрост?"
        ch_e "Да."
        ch_g "\"Белая Королева\" Эмма Фрост?"
        $ GwenX.FaceChange("confused",1,Eyes="side")
        ch_e "Да?"
        ch_g ". . ."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        $ EmmaX.FaceChange("angry",2,Eyes="side",Mouth="open")
        $ GwenX.ArmPose = 1
        ch_g "Божечки, вы работаете здесь?"
        ch_e ". . ."
        $ GwenX.FaceChange("smile",2,Eyes="leftside",Mouth="grimace")
        ch_e "Простите?!"
        $ GwenX.ArmPose = 2
        menu:
            extend ""
            ". . .":
                    pass
            "Она ничего такого не имела в виду.":
                    $ GwenX.FaceChange("sad",1,Eyes="side",Mouth="open")
                    $ GwenX.Statup("Love", 90, 2)
                    $ GwenX.Statup("Inbt", 80, 1)
                    ch_g "Верно!"
            "Извини ее за это, она особенная.":
                    $ GwenX.FaceChange("smile",1,Eyes="side",Mouth="open")
                    $ GwenX.Statup("Love", 90, 1)
                    $ EmmaX.Statup("Love", 80, 1)
                    ch_g "Да!"
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    $ GwenX.Statup("Love", 90, -2)
                    $ GwenX.Statup("Obed", 50, 1)
                    ch_g "Эй!"
            "Она дурочка.":
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    $ GwenX.Statup("Love", 90, -1)
                    $ EmmaX.Statup("Love", 80, 1)
                    ch_g "Эй!"
        $ GwenX.FaceChange("sad",1,Eyes="side")
        $ EmmaX.FaceChange("angry",1,Eyes="side")
        ch_g "Извините, просто в комиксах вы были совсем не такой. . ."
        $ GwenX.FaceChange("sly",1,Eyes="side")
        ch_g "\"Иксовой.\" . ."
        $ EmmaX.FaceChange("confused",1,Eyes="side")
        ch_e "Что ж, я. . . что вы имели в виду, говоря \"в комиксах?\""
        $ GwenX.FaceChange("sad",1,Eyes="leftside")
        menu:
            extend ""
            ". . .":
                    pass
            "Это она и имела в виду.":
                    $ GwenX.Statup("Love", 90, -1)
                    $ GwenX.Statup("Obed", 50, 1)
                    ch_g ". . ."
            "Она думает, что мы персонажи комиксов.":
                    $ GwenX.Statup("Love", 90, 2)
                    $ GwenX.Statup("Obed", 50, 1)
                    $ GwenX.Statup("Obed", 80, 1)
                    ch_g "Ну. . . да. . ."
        ch_g "В мире, из которого я родом, вы все персонажи комиксов."
        ch_e "Значит вы верите, что мы сейчас находимся в комиксе?"
        $ GwenX.FaceChange("sly",1,Eyes="side")
        ch_g "Скорее в игре, основанной на комиксах."
        $ EmmaX.FaceChange("angry",1,Eyes="closed")
        ch_e ". . ."
        $ EmmaX.FaceChange("surprised",1,Mouth="open")
        ch_e "Потрясающе, похоже, она действительно верит в это. . ."
        $ GwenX.FaceChange("normal",1,Eyes="side")
        menu:
            extend ""
            ". . .":
                    pass
            "Ты привыкнешь.":
                    $ GwenX.Statup("Love", 90, 1)
                    $ GwenX.Statup("Obed", 50, 1)
                    $ EmmaX.Statup("Love", 80, 1)
                    $ EmmaX.Statup("Inbt", 60, 1)
                    $ EmmaX.FaceChange("sly",1)
            "Это никому не причинит вреда, наверное.":
                    $ GwenX.Statup("Love", 90, 1)
                    $ GwenX.Statup("Inbt", 80, 1)
                    $ EmmaX.Statup("Inbt", 60, 2)
                    $ EmmaX.FaceChange("sly",1)
        $ EmmaX.FaceChange("smile",1,Eyes="side")
        ch_g "А если серьезно, я ваша большая фанатка!"
        ch_g "Я просто не сразу вас узнала."
        $ GwenX.FaceChange("sly",1)
        $ EmmaX.FaceChange("sly",1,Eyes="side")
        if "Storm" not in GwenX.History:
                $ GwenX.Statup("Obed", 60, 1)
                $ GwenX.Statup("Obed", 80, 1)
                ch_g "Я начинаю прослеживать закономерность. . ."
        else:
                ch_g "Они, должно быть, хотели внести \"разнообразия\". . ."
        $ GwenX.FaceChange("normal",1,Eyes="side")
        ch_e "Я не знаю, что с вами делать, мисс Пул. . ."
        ch_e "Полагаю, мы постараемся вписать вас в учебную программу, насколько это возможно."
        ch_e "[EmmaX.Petname], обязательно покажи ей кампус."
        $ GwenX.FaceChange("sly",1)
        ch_g "Мне кажется, вы довольно близки. *подмигивает*"
        if "taboo" not in EmmaX.History:
                $ EmmaX.FaceChange("surprised",2,Eyes="side",Mouth="open")
                $ GwenX.Statup("Inbt", 80, 1)
                $ EmmaX.Statup("Inbt", 60, 2)
                if not Player.Male:
                    ch_e "Ох. . . нет. . . она просто мой студент."
                else:
                    ch_e "Ох. . . нет. . . он просто мой студент."
                ch_g ". . ."
                $ EmmaX.FaceChange("angry",1,Eyes="side",Mouth="smirk")
                ch_g "*подмигивает*"
        elif EmmaX in Player.Harem:
                $ EmmaX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
                $ EmmaX.Statup("Obed", 80, 1)
                $ EmmaX.Statup("Inbt", 80, 2)
                ch_e "Немного странно встречаться со студентом. . ."
                if GwenX.Event[2] > 1:
                        #if gwen heard you were dating two+ girls
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "О. . . и вы тоже. . . ого. . ."
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 80, 3)
                elif GwenX.Event[2]:
                        #if gwen heard you were dating someone else
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 3)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "О. . . эм, значит и вы. . . клево. . ."
                        $ GwenX.Statup("Obed", 50, 4)
                        $ GwenX.Statup("Obed", 80, 3)
                else:
                        $ GwenX.Statup("Obed", 80, 2)
                        $ GwenX.FaceChange("sly",1)
                        ch_g "Ого, хороший улов, [GwenX.Petname]. . ."
                $ GwenX.Event[2] += 1
        elif EmmaX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                $ EmmaX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                ch_e "Ах. . . что ж. . ."
                if not Player.Male:
                    ch_e "Она моя [EmmaX.Petname]. . ."
                else:
                    ch_e "Он мой [EmmaX.Petname]. . ."
                ch_g "Ох. . ."
        elif not ApprovalCheck(EmmaX, 500, "L"):
                $ EmmaX.FaceChange("angry",1,Mouth="smirk")
                ch_e "Честно говоря, мы не ладим. . ."
                if not Player.Male:
                    ch_e "Но она иногда бывает полезной."
                else:
                    ch_e "Но он иногда бывает полезным."
                ch_g "Лаааадно. . ."
        else:
                $ EmmaX.FaceChange("sad",1,Eyes="leftside")
                ch_e "Полагаю. . ."
                $ EmmaX.FaceChange("sly",1)
                ch_e "Все сложно."
                ch_g "Лаааадно. . ."
        $ EmmaX.FaceChange("sly",0,Eyes="side")
        if bg_current == "bg classroom" and Time_Count < 2:
                ch_e "В общем, вернитесь на свои места, мы можем поговорить позже."
        else:
                ch_e "В общем, увидимся на занятиях."

        if Teach == 1:
                $ EmmaX.Loc = "bg teacher"

        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
        $ GwenX.DrainWord("Emma",0,0,0,1)
        return
# End Meet Emma / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Meet Laura / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Laura_Meet:
        # GwenX.Event[2] tracks number of girls she knows you're dating
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = bg_current
        $ LauraX.Loc = bg_current
        $ GwenX.ArmPose = 2
        call Shift_Focus(GwenX)
        call Set_The_Scene
        $ GwenX.FaceChange("normal",1)
        $ LauraX.FaceChange("normal",1)

        if "Gwentro" in LauraX.History:
                #she did the intro scene
                ch_l "Эй, [LauraX.Petname]. . ."
                if LauraX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                        $ GwenX.Statup("Obed", 60, 2)
                        $ GwenX.Statup("Obed", 80, 5)
                hide Laura_Seated
                show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc)
                hide Gwen_Seated
                show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                        xzoom -1
                $ LauraX.FaceChange("sly",1,Eyes ="side",Mouth="smirk")
                ch_l "Ты. . . Гвен?"
                $ GwenX.FaceChange("sly",1,Eyes ="side",Mouth="smirk")
                $ GwenX.Hat = 0
                ch_g "Как дела?"
                ch_g ". . ."
                $ GwenX.FaceChange("smile",1,Eyes ="side")
                ch_g "Ага, я Гвен!"
                if GwenX.Name != "Гвен":
                        ch_g "Ну, сейчас я больше предпочитаю, чтобы меня звали [GwenX.Name_tvo]."
                $ GwenX.FaceChange("surprised",2,Eyes ="side")
                ch_g "Однажды мы встречались, когда ты-"
                $ GwenX.FaceChange("sad",2,Eyes ="leftside",Mouth="kiss")
                ch_g "Эм. . ."
                $ LauraX.GirlLikeUp(GwenX,50)
                $ GwenX.GirlLikeUp(LauraX,50)
                $ GwenX.Statup("Obed", 60, 4)
                $ GwenX.Statup("Obed", 80, 2)
                if Player.Male:
                        ch_l "Сосала ему?"
                else:
                        ch_l "Лизала ей?"
                $ GwenX.FaceChange("sad",1,Eyes ="side",Mouth="normal")
                ch_g "Эм. . . ага. . ."
                if not Player.Male:
                    ch_g "Так вот, эм. . . и как у вас с ней дела?"
                else:
                    ch_g "Так вот, эм. . . и как у вас с ним дела?"
        else:
                #she didn't do the intro scene
                ch_l "Эй, [LauraX.Petname]."
                if LauraX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                        $ GwenX.Statup("Obed", 60, 2)
                        $ GwenX.Statup("Obed", 80, 5)
                hide Laura_Seated
                show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc)
                hide Gwen_Seated
                show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                        xzoom -1
                $ GwenX.Hat = 0
                $ GwenX.FaceChange("surprised",1,Eyes ="side",Mouth="smile")
                ch_g "О, я [GwenX.Name]!"
                $ GwenX.FaceChange("smile",1,Eyes ="side")
                $ LauraX.FaceChange("angry",Eyes="side")
                $ GwenX.ArmPose = 1
                ch_g "А ты Лора, верно?"
                $ LauraX.FaceChange("confused",Eyes="side")
                ch_l "Откуда ты знаешь мое имя?!"
                ch_g "Я прочитала о тебе все! Или ты предпочитаешь \"Икс-23?\""
                ch_g "Или \"Росомаха?\""
                $ GwenX.FaceChange("surprised",Eyes="side")
                $ GwenX.ArmPose = 2
                ch_g "Боже, ну не \"Коготь\" же?"
                $ GwenX.FaceChange("smile",Eyes="side")
                ch_l "[LauraX.Name] - лучше так."
                ch_l "Так откуда ты меня знаешь?"
                menu:
                    extend ""
                    ". . .":
                            $ GwenX.Statup("Love", 80, -1)
                            ch_g "Я родом из мира, где вы, ребята, были вымыслом!"
                    "Она из другого мира, где мы воображаемые.":
                            $ GwenX.FaceChange("smile",1,Mouth="open")
                            $ LauraX.FaceChange("confused",1)
                            $ GwenX.Statup("Love", 60, 2)
                            $ GwenX.Statup("Love", 80, 1)
                            $ GwenX.Statup("Obed", 60, 2)
                            $ GwenX.Statup("Obed", 80, 2)
                            ch_g "Ага!"
                    "Она сумасшедшая.":
                            $ GwenX.FaceChange("angry",2,Mouth="open")
                            $ LauraX.FaceChange("angry",1,Mouth="smirk")
                            $ GwenX.Statup("Love", 80, -5)
                            $ LauraX.Statup("Love", 80, -3)
                            $ LauraX.Statup("Obed", 70, 2)
                            ch_g "Эй!"
                            $ GwenX.Statup("Inbt", 70, 5)
                            $ GwenX.FaceChange("surprised",1,Eyes ="side",Mouth="open")
                            ch_g "Я действитильно из мира, где вы, ребята, были вымыслом!"
                $ LauraX.FaceChange("confused",1,Eyes ="side")
                $ GwenX.FaceChange("smile",1,Eyes ="side")
                ch_g "Я читала о тебе в комиксах на родине!"
                ch_l "Хм."
                $ LauraX.FaceChange("sly",1,Eyes ="side",Mouth="smirk")
                ch_l "Ладно."
                ch_g "А откуда ты знаешь [Player.Name_vin]?"

        if LauraX in Player.Harem:
                $ LauraX.FaceChange("sly",1)
                $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
                $ LauraX.Statup("Obed", 80, 1)
                $ LauraX.Statup("Inbt", 80, 2)
                ch_l "Ну, мы вроде как встречаемся, правда?"
                menu:
                    extend ""
                    ". . .":
                            $ LauraX.FaceChange("angry",1,Mouth="smirk")
                            $ LauraX.Statup("Love", 70, -2)
                            $ LauraX.Statup("Love", 90, -2)
                            $ LauraX.Statup("Obed", 60, 2)
                            $ LauraX.Statup("Obed", 80, 2)
                    "Конечно":
                            $ GwenX.Statup("Obed", 70, 1)
                            $ LauraX.Statup("Love", 80, 2)
                            $ LauraX.Statup("Love", 95, 1)
                            $ LauraX.Statup("Obed", 80, 2)
                    "Не знаю. . .":
                            $ LauraX.FaceChange("angry",2,Mouth="smirk")
                            $ GwenX.Statup("Love", 80, -1)
                            $ GwenX.Statup("Inbt", 80, 2)
                            $ LauraX.Statup("Love", 70, -3)
                            $ LauraX.Statup("Love", 90, -2)
                            $ LauraX.Statup("Obed", 60, 2)
                            $ LauraX.Statup("Inbt", 80, 2)
                            $ GwenX.GirlLikeUp(LauraX,50)
                            "Она бьет вас по затылку." with vpunch
                            $ LauraX.FaceChange("angry",1)
                $ GwenX.FaceChange("surprised",1,Eyes ="side")
                if GwenX.Event[2] > 1:
                        #if gwen heard you were dating two+ girls
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "О, значит. . . у тебя их уже куча. . ."
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_l "Да. . . ты к этому привыкнешь."
                elif GwenX.Event[2]:
                        #if gwen heard you were dating someone else
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 3)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "О. . . значит, и ты. . ."
                        $ GwenX.Statup("Obed", 50, 4)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_l "Да. . . ты к этому привыкнешь."
                else:
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Obed", 60, 2)
                        $ GwenX.Statup("Obed", 80, 2)
                        $ GwenX.FaceChange("sly",1)
                        ch_g "О. . . отличная работа, [GwenX.Petname]. . ."
                $ GwenX.Event[2] += 1
        elif LauraX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                $ LauraX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                if not Player.Male:
                    ch_l "Ох, думаю, она моя [LauraX.Petname]. . ."
                else:
                    ch_l "Ох, думаю, он мой [LauraX.Petname]. . ."
        elif not ApprovalCheck(LauraX, 500, "L"):
                $ LauraX.FaceChange("normal",0)
                if not Player.Male:
                    ch_l "О. . . Мы с ней не ладим."
                else:
                    ch_l "О. . . Мы с ним не ладим."
        else:
                $ LauraX.FaceChange("sad",1,Eyes="leftside")
                if not Player.Male:
                    ch_l "Хм. . . она. . . вроде нормальная."
                else:
                    ch_l "Хм. . . он. . . вроде нормальный."
        $ GwenX.FaceChange("sad",1,Eyes ="leftside")
        ch_g "Здорово-здорово. . ."
        ch_g "Ладно, не буду тебя отвлекать. . . как-нибудь свидимся. . ."
        $ LauraX.GirlLikeUp(GwenX,50)
        $ GwenX.GirlLikeUp(LauraX,50)
        $ GwenX.FaceChange("normal",1)
        $ LauraX.FaceChange("smile",1)
        $ GwenX.DrainWord("Laura",0,0,0,1)
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
        return
# End Meet Laura / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Meet Jean / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Jean_Meet(TLove=JeanX.Love,TObed=JeanX.Obed,TInbt=JeanX.Inbt):
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = bg_current
        $ JeanX.Loc = bg_current
        call Shift_Focus(GwenX)
        call Set_The_Scene
        $ JeanX.FaceChange("angry",1)
        $ GwenX.FaceChange("normal")
        $ GwenX.ArmPose = 2
        ch_j "Слушай, [JeanX.Petname]. . ."
        ch_j "Это [KittyX.Name] сейчас пробежала мимо? Я хотела задержать ее на минутку."
        if JeanX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                $ GwenX.Statup("Obed", 60, 2)
                $ GwenX.Statup("Obed", 80, 5)
        $ GwenX.ArmPose = 1
        hide Jean_Seated
        show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc)
        hide Gwen_Seated
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom -1
        $ GwenX.Hat = 0
        $ JeanX.FaceChange("smile",1,Eyes="side")
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_g "О, ого, Джин Грей!"
        $ JeanX.FaceChange("confused",1,Eyes="side")
        ch_j ". . ."
        $ GwenX.FaceChange("confused",1,Eyes="side")
        ch_g "Хотя ты не особо походишь на свой мультяшный образ. . ."
        $ JeanX.FaceChange("confused",1)
        ch_j "Кто это?"
        menu:
            extend ""
            ". . .":
                    $ GwenX.Statup("Love", 50, -1)
            "Это [GwenX.Name].":
                    $ Player.AddWord(1,"itsgwen",0,0,0)
                    $ GwenX.Statup("Love", 70, 2)
            "Она скоро успокоится.":
                    $ GwenX.Statup("Love", 70, -2)
                    $ GwenX.Statup("Obed", 50, 3)
        ch_g "Пожалуй, твой образ больше походит на \"O5\"."
        $ JeanX.FaceChange("angry",1,Eyes="side")
        ch_j "Почему оно говорит со мной?"
        menu:
            extend ""
            ". . .":
                    $ GwenX.Statup("Love", 50, -1)
            "Это [GwenX.Name]." if "itsgwen" not in Player.RecentActions:
                    $ Player.AddWord(1,"itsgwen",0,0,0)
                    $ GwenX.Statup("Love", 70, 2)
            "Как я сказала, это [GwenX.Name]." if "itsgwen" in Player.RecentActions and not Player.Male:
                    $ GwenX.Statup("Love", 70, 1)
            "Как я сказал, это [GwenX.Name]." if "itsgwen" in Player.RecentActions and Player.Male:
                    $ GwenX.Statup("Love", 70, 1)
            "Она скоро успокоится.":
                    $ GwenX.Statup("Love", 70, -2)
                    $ GwenX.Statup("Obed", 50, 3)
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "Тебе идет этот стиль!"
        $ JeanX.FaceChange("angry",1,Eyes="side",Mouth="smile")
        ch_j ". . . еще бы."
        menu:
            extend ""
            ". . .":
                    ch_g "О, прости, меня зовут [GwenX.Name]."
            "Это [GwenX.Name]." if "itsgwen" not in Player.RecentActions:
                    $ GwenX.Statup("Love", 70, 1)
            "Как я уже сказала, это [GwenX.Name]." if "itsgwen" in Player.RecentActions and not Player.Male:
                    $ GwenX.Statup("Love", 70, 1)
            "Как я уже сказал, это [GwenX.Name]." if "itsgwen" in Player.RecentActions and Player.Male:
                    $ GwenX.Statup("Love", 70, 1)
        ch_g "Привет!"
        $ JeanX.FaceChange("angry",1,Eyes="side",Mouth="smile")
        ch_j ". . . Привет."
        $ JeanX.FaceChange("angry",1)
        ch_j "Но - почему - оно - говорит - со мной?"
        ch_g "Я здесь недавно. Я попала в эту игру всего несколько дней назад."
        $ JeanX.FaceChange("confused",1,Eyes="side")
        ch_j "В игру?"
        menu:
            extend ""
            ". . .":
                    ch_g "Да! Это видеоигра, и мы все живем в ней!"
            "Она думает, что это все видеоигра.":
                    $ GwenX.Statup("Love", 70, 1)
                    $ GwenX.Statup("Obed", 80, 3)
                    $ GwenX.Statup("Inbt", 60, 2)
                    $ JeanX.Statup("Love", 70, -1)
                    $ JeanX.Statup("Obed", 50, 1)
                    ch_g "Ага!"
            "Она сумасшедшая.":
                    $ JeanX.FaceChange("smile",1)
                    $ JeanX.Statup("Love", 70, 2)
                    ch_j "О, ладно."
                    $ GwenX.FaceChange("angry",2,Mouth="open")
                    $ JeanX.FaceChange("angry",1,Eyes="side")
                    $ GwenX.Statup("Love", 90, -2)
                    $ GwenX.Statup("Obed", 80, -1)
                    $ GwenX.Statup("Inbt", 80, -1)
                    ch_g "Я не сумасшедшая! Это видеоигра, и мы все живем в ней!"
                    $ JeanX.FaceChange("angry",1,Eyes="side",Mouth="smirk")
                    ch_j "Так бы и сказал сумасшедший."
        $ GwenX.FaceChange("confused",1,Eyes="side")
        ch_g "Это игра, вы своего рода НИПы. . . или типа. . . однопартийцы?"
        $ JeanX.FaceChange("angry",2,Eyes="side",Mouth="open")
        ch_j "!!!"
        ch_j "Я не НИП, это ты НИП!!!"
        $ GwenX.FaceChange("sad",1,Eyes="leftside")
        ch_g "Ага. . . думаю, сейчас, наверное, так и есть. . ."
        ch_j ". . ."
        $ JeanX.FaceChange("angry",2,Eyes="side")
        ch_j "Так, если ты НИП. . . и ты думаешь, что я тоже НИП. . ."
        ch_j "Кто тогда по твоему мнению \"ГГ?\""
        $ GwenX.FaceChange("smile",1,Eyes="side",Mouth="grimace")
        ch_g ". . ."
        $ GwenX.FaceChange("smile",2,Mouth="grimace")
        $ JeanX.FaceChange("angry",2)
        ch_g "[[указывает на вас]"
        ch_j ". . ."
        if ApprovalCheck(JeanX, 600, "L"):
                $ JeanX.FaceChange("sad",2,Eyes="leftside")
                $ JeanX.Statup("Obed", 95, 3)
                ch_j "Я. . . Думаю, в этом есть. . ."
                $ JeanX.FaceChange("angry",2,Eyes="side",Mouth="open")
                ch_j "Нет!"
        elif ApprovalCheck(JeanX, 500, "O"):
                $ JeanX.Statup("Love", 70, 2)
                $ JeanX.Statup("Obed", 95, 2)
                $ JeanX.FaceChange("angry",2,Eyes="surprised",Mouth="open")
                ch_j "Я. . . С этим не соглашусь! . ."
        else:
                $ JeanX.FaceChange("angry",2,Eyes="surprised",Mouth="open")
                $ JeanX.Statup("Love", 70, -5)
                $ JeanX.Statup("Obed", 50, -5)
                $ JeanX.Statup("Inbt", 80, 10)
                ch_j "[JeanX.Petname]? Я с этим никогда не соглашусь!"
        ch_j "Это чушь!"
        $ GwenX.FaceChange("smile",1,Eyes="closed",Mouth="grimace")
        ch_j "Это не игра, и -Я- главная героиня!"
        $ GwenX.FaceChange("surprised",1,Mouth="open")
        ch_g "Ого, ты, Джин, в этой игре такая стерва."
        ch_j "Что ты только что сказала?"
        $ GwenX.FaceChange("confused",1)
        ch_g "Ну, обычно Джина Грей очень милая и скучная. . . та Джин Грей."
        ch_g "А эта настоящая психопатка."
        $ JeanX.FaceChange("angry",2,Eyes="psychic",Mouth="open")
        ch_j "Я превращу тебя в поплавок!"
        $ JeanX.FaceChange("angry",2,Eyes="psychic")
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        show Gwen_Sprite:
            subpixel True
            offset (0,0)
            ease .4 yoffset 200
            ease .4 yoffset 0
            pause .2
        ch_g "Воу!" with vpunch
        show Gwen_Sprite:
            subpixel True
            zoom 1
            ease .4 zoom .8
            ease .4 zoom 1
            pause .2
        ch_g "Эй, успокойся!" with vpunch
        $ GwenX.FaceChange("surprised",1,Mouth="open")
        show Gwen_Sprite:
            subpixel True
            zoom 1
            ease .4 zoom 1.2
            ease .4 zoom 1
            pause .2
        ch_g "-Все идет не очень хорошо!-"  with vpunch
        $ GwenX.FaceChange("surprised",1,Brows="sad",Mouth="open")
        show Gwen_Sprite:
            subpixel True
            offset (0,0)
            ease .4 yoffset 200
            ease .4 yoffset 0
            pause .2
        if not Player.Male:
            ch_g "Эй, [GwenX.Petname], не могла бы ты помочь?" with vpunch
        else:
            ch_g "Эй, [GwenX.Petname], не мог бы ты помочь?" with vpunch
        menu:
            extend ""
            ". . .":
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    $ GwenX.Statup("Love", 90, -2)
                    if not Player.Male:
                        ch_g "Ты очень помогла!"
                    else:
                        ch_g "Ты очень помог!"
            "Я не хочу вмешиваться.":
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    $ GwenX.Statup("Love", 90, -5)
                    $ GwenX.Statup("Obed", 80, 1)
                    $ GwenX.Statup("Inbt", 80, 4)
                    $ JeanX.Statup("Love", 70, 2)
                    ch_g "Ага, моей жизни сейчас -совсем- ничего не угрожает!"
            "Конечно.":
                    $ JeanX.FaceChange("angry",2)
                    $ GwenX.Statup("Love", 90, 4)
                    $ GwenX.Statup("Obed", 80, 2)
                    $ JeanX.Statup("Obed", 60, 2)
                    $ JeanX.Statup("Obed", 90, 3)
                    "Вы ослабляете силу [JeanX.Name_rod]."
                    $ GwenX.FaceChange("smile",1)
                    $ JeanX.FaceChange("angry",2,Mouth="open")
                    $ JeanX.Statup("Love", 60, -2)
                    $ JeanX.Statup("Love", 80, -2)
                    ch_j "[JeanX.Petname]! Как ты смеешь!"
        $ GwenX.FaceChange("angry",1,Eyes="leftside")
        ch_g "Думаю, она вернется за мной позже. . ."
        $ GwenX.FaceChange("normal",1)
        $ JeanX.FaceChange("surprised",2)
        ch_g "У меня есть идея, иди сюда. . ." with vpunch
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
                ease .4 yoffset 800
        show blackscreen onlayer black
        "Она хватает вас за руку и. . . тянет" with vpunch
        ". . ."
        hide blackscreen onlayer black
        call Set_The_Scene
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom -1
        $ JeanX.Love = TLove
        $ JeanX.Obed = TObed
        $ JeanX.Inbt = TInbt
        $ Player.DrainWord("itsgwen")
        $ GwenX.FaceChange("sly",1)
        $ JeanX.FaceChange("angry",1)
        ch_j "Слушай, [JeanX.Petname]. . ."
        ch_j "Это [KittyX.Name] сейчас пробежала мимо? Я хотела задержать ее на минутку."
        $ JeanX.FaceChange("smile",1,Eyes="side")
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_g "О, ого, Джин Грей!"
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "Ты такая замечательная и потрясающая!"
        $ JeanX.FaceChange("confused",1)
        ch_j "Кто это?"
        menu:
            extend ""
            ". . .":
                    pass
            "Я не знаю.":
                    $ GwenX.FaceChange("angry",1)
                    $ GwenX.Statup("Love", 90, -2)
                    ch_g ". . ."
            "Что произошло?":
                    $ GwenX.FaceChange("surprised",1)
                    $ GwenX.Statup("Love", 70, -2)
                    $ GwenX.Statup("Obed", 50, -3)
                    $ GwenX.Statup("Inbt", 80, 3)
                    ch_g "Шшшш!"
            "Это [GwenX.Name].":
                    $ Player.AddWord(1,"itsgwen",0,0,0)
                    $ GwenX.Statup("Love", 70, 2)
                    ch_g "Да, привет! Я здесь новенькая."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        $ JeanX.FaceChange("confused",1,Eyes="side")
        if "itsgwen" not in Player.RecentActions:
                ch_g "Меня зовут [GwenX.Name], я здесь новенькая!"
        $ JeanX.FaceChange("smile",1,Eyes="side")
        ch_g "Рада знакомству, ты супер!"
        $ GwenX.FaceChange("smile",1,Eyes="surprised")
        ch_g "[[подыграй, я позже все объясню]"
        menu:
            extend ""
            ". . .":
                    pass
            "Что происходит?!":
                    $ GwenX.Statup("Love", 70, -2)
                    $ GwenX.Statup("Obed", 50, -2)
                    $ GwenX.Statup("Inbt", 80, 3)
                    ch_g "[[позже!]"
            "Почему [JeanX.Name] больше не пытается тебя убить?":
                    $ JeanX.FaceChange("confused",1)
                    $ GwenX.Statup("Love", 50, -2)
                    $ GwenX.Statup("Obed", 50, 3)
                    $ GwenX.Statup("Inbt", 50, 1)
                    $ JeanX.Statup("Inbt", 80, 3)
                    ch_j "Я пыталась убить ее?"
                    $ GwenX.FaceChange("sad",2,Eyes="stunned")
                    $ JeanX.FaceChange("confused",1,Eyes="side")
                    ch_g "Ох, блин. . ."
                    $ GwenX.FaceChange("surprised",1,Eyes="side")
                    $ GwenX.Statup("Love", 90, -1)
                    $ GwenX.Statup("Obed", 80, 2)
                    $ GwenX.Statup("Inbt", 80, 1)
                    if not Player.Male:
                        ch_g "Не обращай внимания, она ведет себя странно, потому что завидует тебе."
                    else:
                        ch_g "Не обращай внимания, он ведет себя странно, потому что завидует тебе."
                    $ JeanX.FaceChange("smile",1,Eyes="side")
                    ch_j "Ну, в этом есть смысл."

        $ GwenX.FaceChange("normal",1,Eyes="side")
        ch_g "Значит, вы с [JeanX.Petname_tvo] ладите?"
        if JeanX in Player.Harem:
                $ JeanX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
                $ JeanX.Statup("Obed", 80, 1)
                $ JeanX.Statup("Inbt", 80, 2)
                ch_j "Ага, можно сказать, что мы встречаемся. . ."
                $ GwenX.GirlLikeUp(JeanX,25)
                if GwenX.Event[2] > 1:
                        #if gwen heard you were dating two+ girls
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "Ого, значит. . . все вы, девочки. . ."
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_j "Да. . . Пришлось привыкать."
                elif GwenX.Event[2]:
                        #if gwen heard you were dating someone else
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 3)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "Ого. . . эм, ты, значит, тоже. . ."
                        $ GwenX.Statup("Obed", 50, 4)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_j "Да. . . Пришлось привыкать."
                else:
                        $ GwenX.Statup("Obed", 60, 2)
                        $ GwenX.Statup("Obed", 80, 2)
                        $ GwenX.FaceChange("sly",1)
                        ch_g "Ого. . . Я удивлена, что тебе это удалось, [GwenX.Petname]. . ."
                $ GwenX.Event[2] += 1
        elif JeanX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                $ JeanX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                if not Player.Male:
                    ch_j "Ох, думаю, она моя [JeanX.Petname]. . ."
                else:
                    ch_j "Ох, думаю, он мой [JeanX.Petname]. . ."
        elif not ApprovalCheck(JeanX, 300, "O"):
                $ JeanX.FaceChange("normal",0)
                if not Player.Male:
                    ch_j "Ты о ком? А, о ней? . . Она просто постоянно ошивается рядом."
                else:
                    ch_j "Ты о ком? А, о нем? . . Он просто постоянно ошивается рядом."
        else:
                $ JeanX.FaceChange("sad",1,Eyes="leftside")
                if not Player.Male:
                    ch_j "Ты о ком? А, о ней? . . она. . . интересная."
                else:
                    ch_j "Ты о ком? А, о нем? . . он. . . интересный."
        $ GwenX.FaceChange("normal",1,Eyes="side")
        $ JeanX.FaceChange("smile",1,Eyes="side")
        ch_j "Ты мне нравишься, новенькая, мы поладим."
        hide Jean_Sprite with easeinleft
        "[JeanX.Name] уходит."
        $ GwenX.FaceChange("sad",1,Mouth="smirk")
        ch_g "Извини. . ."
        $ GwenX.FaceChange("sadside",1,Mouth="smirk")
        ch_g "Я подумала, что невозможно произвести второе первое впечатление."
        $ GwenX.FaceChange("sad",1,Mouth="smirk")
        ch_g ". . . только если не обладаешь особыми навыками."
        $ GwenX.FaceChange("surprised",1,Mouth="smile")
        ch_g "Так что я просто вернула нас на несколько минут в прошлое и \"вуаля!\""
        $ GwenX.FaceChange("normal",1)
        menu:
            extend ""
            ". . .":
                    ch_g "Хмм. . . наверное, мы перезаписали прошлую временную линию."
            "Подожди, что случилось с нами?":
                    $ GwenX.FaceChange("angry",1,Eyes="side")
                    $ GwenX.Statup("Love", 70, 2)
                    $ GwenX.Statup("Obed", 70, 2)
                    $ GwenX.Statup("Inbt", 70, -2)
                    ch_g "Ну, это игра, а не комикс, так что. . ."
                    ch_g "Похоже, что невозможно иметь несколько экземпляров одного и того же персонажа одновременно. . ."
                    ch_g "Пришлось воспользоваться одним трюком. . ."
                    $ GwenX.FaceChange("surprised",2)
                    ch_g ". . ."
                    $ GwenX.FaceChange("sad",1,Mouth="normal")
                    ch_g "И перезаписать всех персонажей, включая нас."
                    $ GwenX.FaceChange("sadside",1,Mouth="open")
                    ch_g "Извини!"
        ch_g "Мы должны избегать повторения, если сможем. . ."
        $ GwenX.FaceChange("normal",1)
        $ JeanX.GirlLikeUp(GwenX,100)
        ch_g "Ну, по крайней мере теперь между мной и [JeanX.Name_tvo] все хорошо."
        $ Player.DrainWord("itsgwen")
        $ GwenX.DrainWord("Jean",0,0,0,1)
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
        return
# End Meet Jean / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Meet Storm / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Storm_Meet(Teach =0):
        if StormX.Loc == "bg teacher":
                $ Teach = 1
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = bg_current
        $ StormX.Loc = bg_current
        $ GwenX.ArmPose = 2
        call Shift_Focus(GwenX)
        call Set_The_Scene
        $ StormX.FaceChange("smile",1)
        $ GwenX.FaceChange("normal",1)
        ch_s "Ох, здравствуй, [StormX.Petname]."
        $ StormX.FaceChange("smile",1,Eyes="side")
        ch_s "А вы, должно быть, наша новая студентка, мисс Пул?"
        if StormX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                $ GwenX.Statup("Obed", 60, 2)
                $ GwenX.Statup("Obed", 80, 5)
        $ GwenX.ArmPose = 1
        show Storm_Sprite at SpriteLoc(StormX.SpriteLoc)
        hide Gwen_Seated
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom -1
        $ GwenX.Hat = 0
        $ GwenX.FaceChange("surprised",1,Eyes="side")
        ch_g ". . ."
        $ StormX.FaceChange("confused",1,Eyes="side")
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_s "Мисс Пул?"
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="tongue")
        ch_g "Ну и формы. . . "
        $ StormX.FaceChange("confused",1)
        ch_s "Я не уверена, что она имеет в виду, [StormX.Petname]."
        menu:
            extend ""
            ". . .":
                    $ StormX.Statup("Love", 80, -2)
            "Я тоже без понятия.":
                    $ GwenX.FaceChange("angry",1)
                    $ GwenX.Statup("Love", 80, -2)
            "Она думает, что ты сексуальная.":
                    $ GwenX.FaceChange("smile",2,Eyes="side")
                    $ StormX.FaceChange("smile",1)
                    $ GwenX.Statup("Love", 80, 2)
                    $ GwenX.Statup("Obed", 70, 1)
                    $ StormX.Statup("Love", 80, 2)
                    $ StormX.Statup("Inbt", 60, 1)
                    $ StormX.GirlLikeUp(GwenX,50)
            "Она думает, что ты толстая.":
                    $ GwenX.FaceChange("angry",2,Mouth="open")
                    $ StormX.FaceChange("surprised",2)
                    $ GwenX.Statup("Love", 80, -5)
                    $ GwenX.Statup("Inbt", 60, 2)
                    ch_g "Нет!"
                    $ StormX.Statup("Love", 80, -3)
                    $ StormX.Statup("Obed", 70, 2)
                    $ StormX.GirlLikeUp(GwenX,50)
                    $ StormX.FaceChange("angry",1,Eyes="side")
        $ GwenX.FaceChange("sad",2,Eyes="side",Mouth="smile")
        $ GwenX.ArmPose = 2
        ch_g "Я хотела. . . эм. . ."
        $ GwenX.FaceChange("sad",1,Eyes="side",Mouth="smile")
        $ StormX.FaceChange("smile",1,Eyes="side")
        ch_g "Я просто хотела. . . поздравить вас?"
        $ GwenX.FaceChange("surprised",1)
        ch_g "[[У нее всегда была такая фигура?]"
        menu:
            extend ""
            "Да?":
                    $ GwenX.Statup("Love", 80, 1)
                    $ GwenX.Statup("Obed", 70, 2)
                    $ GwenX.Statup("Inbt", 60, 1)
                    ch_g "Ого."
            "Наверное?":
                    $ GwenX.Statup("Love", 80, 1)
                    $ GwenX.Statup("Obed", 70, 1)
                    $ GwenX.Statup("Inbt", 60, 1)
                    ch_g "Ого."
            "Зачем спрашиваешь?":
                    $ GwenX.Statup("Love", 80, -1)
                    $ GwenX.Statup("Obed", 70, 2)
                    $ GwenX.Statup("Inbt", 60, 1)
        $ GwenX.FaceChange("smile",1)
        ch_g "Мне просто непривычно."
        $ GwenX.FaceChange("sly",1,Eyes="side")
        ch_g "В комиксах она. . . не в такой форме?"
        if "Emma" not in GwenX.History:
                $ GwenX.Statup("Obed", 60, 1)
                $ GwenX.Statup("Obed", 80, 1)
                ch_g "Я начинаю прослеживать закономерность. . ."
        else:
                ch_g "Они, должно быть, хотели внести \"разнообразия\". . ."
        $ GwenX.FaceChange("smile",2,Eyes="side")
        $ StormX.FaceChange("perplexed",1)
        ch_s "Прошу прощения, \"в комиксах?\""
        menu:
            extend ""
            ". . .":
                    $ StormX.FaceChange("perplexed",1,Eyes="side")
                    $ StormX.Statup("Love", 80, -2)
                    $ StormX.Statup("Obed", 70, 2)
            "У нее не все в порядке с головой.":
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    $ StormX.FaceChange("surprised",1,Eyes="side",Mouth="open")
                    $ GwenX.Statup("Love", 80, -3)
                    $ GwenX.Statup("Inbt", 60, 2)
                    $ StormX.Statup("Love", 80, 1)
                    ch_g "Эй!"
            "Она из другого мира.":
                    $ GwenX.FaceChange("smile",1)
                    $ StormX.FaceChange("surprised",1,Eyes="side",Mouth="open")
                    $ GwenX.Statup("Love", 80, 2)
                    $ GwenX.Statup("Obed", 70, 2)
                    $ StormX.Statup("Love", 80, 1)
                    $ StormX.Statup("Obed", 70, 1)
                    ch_g "Ага. . ."
        $ GwenX.FaceChange("normal",1,Eyes="side")
        $ StormX.FaceChange("confused",1,Eyes="side")
        ch_g "Там, откуда я родом, вы все персонажи комиксов."
        $ StormX.FaceChange("confused",1,Eyes="side",Mouth="smirk")
        $ GwenX.Statup("Obed", 70, 2)
        ch_s "Что ж, это довольно интересная история."
        $ StormX.FaceChange("smile",1,Eyes="side")
        ch_s "У вас восхитительный акцент. . . "
        ch_s "Такой. . . \"розовый?\""
        ch_g "У вас тоже!"
        ch_g "Вы, похоже, совсем не удивлены. . ."
        $ StormX.FaceChange("smile",1,Eyes="closed",Mouth="open")
        ch_s "Ха!"
        $ StormX.FaceChange("smile",1,Eyes="side")
        $ GwenX.Statup("Obed", 80, 2)
        ch_s "Что ж, я многое повидала за свою жизнь."
        ch_s "Я не могу отрицать, что ваши слова могут быть правдой."
        $ StormX.FaceChange("smile",1)
        if not Player.Male:
            ch_s "Ты согласна, [StormX.Petname]?"
        else:
            ch_s "Ты согласен, [StormX.Petname]?"
        menu:
            "Наверное?":
                    $ GwenX.FaceChange("normal",1)
                    $ GwenX.Statup("Love", 80, 1)
                    $ GwenX.Statup("Obed", 70, 1)
                    $ GwenX.Statup("Inbt", 60, 1)
                    $ StormX.Statup("Love", 80, 2)
                    $ StormX.Statup("Obed", 70, 1)
                    ch_g ". . ."
            "Я всегда верила в ее историю." if not Player.Male:
                    $ GwenX.FaceChange("normal",1)
                    $ GwenX.Statup("Love", 80, 1)
                    $ GwenX.Statup("Inbt", 60, 2)
                    $ StormX.Statup("Love", 80, 2)
                    $ StormX.Statup("Inbt", 60, 1)
                    ch_g "Оу."
            "Я всегда верил в ее историю." if Player.Male:
                    $ GwenX.FaceChange("normal",1)
                    $ GwenX.Statup("Love", 80, 1)
                    $ GwenX.Statup("Inbt", 60, 2)
                    $ StormX.Statup("Love", 80, 2)
                    $ StormX.Statup("Inbt", 60, 1)
                    ch_g "Оу."
            "Я все еще думаю, что это бред.":
                    $ GwenX.FaceChange("angry",1)
                    $ StormX.FaceChange("sad",1)
                    $ GwenX.Statup("Love", 80, -2)
                    $ GwenX.Statup("Obed", 70, -1)
                    $ GwenX.Statup("Inbt", 60, 3)
                    $ StormX.Statup("Love", 80, -1)
                    ch_g ". . ."
        $ GwenX.FaceChange("sly",1,Eyes="side")
        ch_g "Похоже, вы хорошо ладите."
        if StormX in Player.Harem:
                $ StormX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
                $ StormX.Statup("Obed", 80, 1)
                $ StormX.Statup("Inbt", 80, 2)
                ch_s "Пожалуй, неприлично встречаться со студентом. . ."
                if GwenX.Event[2] > 1:
                        #if gwen heard you were dating two+ girls
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "И еще одна. . ."
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 80, 3)
                elif GwenX.Event[2]:
                        #if gwen heard you were dating someone else
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 3)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "О. . . ого, и вы тоже. . ."
                        $ GwenX.Statup("Obed", 50, 4)
                        $ GwenX.Statup("Obed", 80, 3)
                else:
                        $ GwenX.Statup("Obed", 80, 2)
                        $ GwenX.FaceChange("sly",1)
                        ch_g "[GwenX.Petname]. . . мое почтение."
                $ GwenX.Event[2] += 1
        elif StormX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                $ StormX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                ch_s "Ох. . . Пожалуй. . ."
                if not Player.Male:
                    ch_s "Я считаю, что она моя [StormX.Petname]. . ."
                else:
                    ch_s "Я считаю, что он мой [StormX.Petname]. . ."
        elif not ApprovalCheck(StormX, 500, "L"):
                $ StormX.FaceChange("angry",1,Mouth="smirk")
                if not Player.Male:
                    ch_s "Честно говоря, с ннй  бывают проблемы. . ."
                    $ StormX.FaceChange("sadside",0)
                    ch_s "И все же мне иногда бывает нужна ее помощь."
                else:
                    ch_s "Честно говоря, с ним  бывают проблемы. . ."
                    $ StormX.FaceChange("sadside",0)
                    ch_s "И все же мне иногда бывает нужна его помощь."
        else:
                $ StormX.FaceChange("sad",1,Eyes="leftside")
                ch_s "Скажу так. . ."
                $ StormX.FaceChange("sly",1)
                ch_s "-все сложно."
        $ GwenX.FaceChange("normal",1)
        $ StormX.FaceChange("sly",0,Eyes="side")
        if bg_current == "bg classroom" and Time_Count < 2:
                ch_s "Ладно, пожалуйста, вернитесь на свои места."
        else:
                ch_s "Ладно, увидимся на занятиях."

        $ StormX.FaceChange("smile",1)
        if Teach == 1:
                $ StormX.Loc = "bg teacher"

        $ StormX.GirlLikeUp(GwenX,100)
        $ GwenX.GirlLikeUp(StormX,50)
        $ GwenX.DrainWord("Storm",0,0,0,1)
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
        return
# End Meet Storm / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Meet Jubes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Jubes_Meet:
        # GwenX.Event[2] tracks number of girls she knows you're dating
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = bg_current
        $ JubesX.Loc = bg_current
        call Shift_Focus(GwenX)
        $ GwenX.ArmPose = 2
        call Set_The_Scene
        $ GwenX.FaceChange("normal",1)
        $ JubesX.FaceChange("smile",1)
        ch_v "Эй, [JubesX.Petname]. . ."
        if JubesX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                $ GwenX.Statup("Obed", 60, 2)
                $ GwenX.Statup("Obed", 80, 5)
        $ GwenX.ArmPose = 1
        $ JubesX.ArmPose = 2
        hide Jubes_Seated
        show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc)
        hide Gwen_Seated
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom -1
        $ GwenX.Hat = 0
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_g "О, ого, Джубили!"
        $ JubesX.FaceChange("confused",1,Eyes="side")
        ch_v "Эм. . . я тебя знаю?"
        $ GwenX.FaceChange("sad",2,Eyes="leftside",Mouth="smirk")
        ch_g "Ох, эм. Наверное, нет. . ."
        ch_g "\"Парасоциальные отношения\". . ."
        $ JubesX.FaceChange("angry",1,Eyes="side",Mouth="open")
        ch_v "Это была шутка про вампиров? Не смешно!"
        $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
        $ GwenX.ArmPose = 2
        ch_g "Что-"
        ch_g "Нет, нет! Не \"паранормальные,\" я имела в виду, что. . ."
        $ GwenX.FaceChange("sad",1,Eyes="leftside")
        ch_g ". . . Я читаю слишком много комиксов. . ."
        $ JubesX.FaceChange("sad",2,Eyes="side",Mouth="smirk")
        ch_v "О, извини, я слишком обидчивая, когда дело касается клыков. . ."
        $ GwenX.FaceChange("confused",1,Eyes="side")
        $ JubesX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_g "Да, странно, что они у тебя есть, ты же вылечилась во вселенной комиксов. . ."
        ch_v "Что? Как?!"
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="lipbite")
        ch_g "Помог мой бывший, Сила Феникса, это было нечто."
        $ GwenX.FaceChange("sad",1,Eyes="side",Mouth="lipbite")
        $ JubesX.FaceChange("sad",1,Eyes="side")
        ch_g "Здесь и сейчас, скорее всего, мы ничего не сможем сделать. . ."
        $ GwenX.FaceChange("surprised",1,Mouth="open")
        $ JubesX.FaceChange("confused",1,Eyes="side")
        if "Jean" not in GwenX.History:
                ch_g "Джин в этой реальности - не настоящий Феникс, ведь так?"
        else:
                ch_g "У вас здесь есть \"Джин Грей\"?"
                ch_v "Да? Она та еще стерва. . ."
                ch_g "Она настоящий Феникс?"
        menu:
            extend ""
            "\"Что, кто\"?":
                    $ GwenX.FaceChange("confused",1)
                    $ GwenX.Statup("Obed", 70, 1)
                    ch_g "\"Феникс,\" большая, богоподобная, огненная птица?"
            "Возможно?":
                    $ GwenX.FaceChange("perplexed",1)
                    $ GwenX.Statup("Love", 80, -1)
                    $ JubesX.Statup("Love", 80, -1)
                    ch_g "\"Феникс,\" большая, богоподобная, огненная птица?"
                    ch_v "Нет, ничего подобного."
            "Нет, она просто стерва.":
                    $ JubesX.Statup("Love", 80, 3)
                    $ JubesX.Statup("Inbt", 60, 1)
                    if "Jean" not in GwenX.History:
                            $ GwenX.FaceChange("sad",1,Eyes="leftside")
                            ch_g "Ага. . ."
                            $ GwenX.Statup("Love", 80, 2)
                            $ GwenX.Statup("Inbt", 60, 2)
                            ch_g "В общем. . ."
                    else:
                            $ GwenX.FaceChange("surprised",1,Mouth="open")
                            ch_g "О! А похоже!"
                            ch_g "А огненной ауры у нее случаем нет?"
                            ch_v "Вряд ли. . ."
                            $ GwenX.FaceChange("sad",1,Eyes="leftside")
        $ JubesX.FaceChange("sad",1,Eyes="side")
        ch_g "Думаю, это не сработает. . ."
        $ JubesX.FaceChange("surprised",1,Eyes="side")
        ch_v "Подожди-ка, давай вернемся назад, что ты имела в виду под \"вселенной комиксов?\""
        menu:
            extend ""
            ". . .":
                    $ GwenX.FaceChange("sad",1,Eyes="side",Mouth="normal")
                    $ JubesX.FaceChange("confused",1,Eyes="side")
                    $ GwenX.Statup("Love", 80, -1)
                    $ GwenX.Statup("Inbt", 60, 2)
                    ch_g "В мире, откуда я родом, вы все персонажи комиксов."
            "Она родом из мира, где мы персонажи комиксов.":
                    $ GwenX.FaceChange("smile",1)
                    $ JubesX.FaceChange("confused",1)
                    $ GwenX.Statup("Love", 80, 3)
                    $ GwenX.Statup("Obed", 70, 2)
                    $ JubesX.Statup("Obed", 70, 2)
            "Она сумасшедшая.":
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    $ JubesX.FaceChange("confused",1)
                    $ GwenX.Statup("Love", 60, -3)
                    $ GwenX.Statup("Love", 80, -2)
                    $ JubesX.Statup("Love", 80, -1)
                    $ JubesX.Statup("Obed", 70, 2)
                    ch_g "Эй! Прекрати!"
                    $ GwenX.FaceChange("sad",1,Eyes="side",Mouth="normal")
                    $ JubesX.FaceChange("confused",1,Eyes="side")
                    $ GwenX.Statup("Obed", 60, 2)
                    $ GwenX.Statup("Obed", 80, 1)
                    ch_g "В мире, откуда я родом, вы все персонажи комиксов."
        $ JubesX.FaceChange("confused",1,Eyes="side")
        ch_v "Так ты думаешь, что мы сейчас в комиксе?"
        $ GwenX.FaceChange("normal",1,Eyes="side")
        ch_g "Нет, в видеоигре."
        ch_v "Основанной на комиксах?"
        ch_g "Да."
        $ JubesX.FaceChange("surprised",1,Eyes="side",Mouth="smile")
        $ GwenX.Statup("Obed", 70, 3)
        ch_v "Клево."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "Да, наверное. Реальный мир был скучным."
        ch_v "Ага, понимаю. Однажды я сбежал и жила-"
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="smile")
        $ JubesX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_g "-в торговом центре!"
        ch_v "Да! Как ты узнала?!"
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_g "Из коми-{w=0.3}{nw}"
        ch_v "Из комиксов!"
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_v "Это так круто!"
        $ JubesX.FaceChange("smile",1,Eyes="side",)
        ch_g "Правда? Это я и имела в виду, говоря \"парасоциальные отношения\"."
        $ GwenX.FaceChange("sad",1,Eyes="side",Mouth="lipbite")
        ch_g "Я знаю многое о тебе, но ты меня совсем не знаешь."
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="smile")
        ch_v "О. . . Ну, я бы хотела это исправить."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_v "[JubesX.Name], приятно познакомиться!"
        ch_g "Гвендолин Пул, зови меня [GwenX.Name]!"
        $ GwenX.FaceChange("normal",1)
        ch_g "А [Player.Name_vin], думаю, ты уже знаешь. . ."
        if JubesX in Player.Harem:
                $ JubesX.FaceChange("sly",1)
                $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
                $ JubesX.Statup("Obed", 80, 1)
                $ JubesX.Statup("Inbt", 80, 2)
                ch_j "Ага, мы вроде как встречаемся, да?"
                $ GwenX.FaceChange("surprised",1,Eyes ="side")
                if GwenX.Event[2] > 1:
                        #if gwen heard you were dating two+ girls
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Inbt", 80, 3)
                        if not Player.Male:
                            ch_g "О, значит. . . она постоянно занята. . ."
                        else:
                            ch_g "О, значит. . . он постоянно занят. . ."
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_v "Хех. . . Ага. . ."
                elif GwenX.Event[2]:
                        #if gwen heard you were dating someone else
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 3)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "Ох. . . эм, и ты. . ."
                        $ GwenX.Statup("Obed", 50, 4)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_v "Хех. . . Ага. . ."
                else:
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Obed", 60, 2)
                        $ GwenX.Statup("Obed", 80, 2)
                        $ GwenX.FaceChange("sly",1)
                        ch_g "О. . . неплохо. . ."
                $ GwenX.Event[2] += 1
        elif JubesX.Petname in ("хозяин", "господин", "госпожа", "хозяйка"):
                $ JubesX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                if not Player.Male:
                    ch_v "О, наверное, она моя [JubesX.Petname]. . ."
                else:
                    ch_v "О, наверное, он мой [JubesX.Petname]. . ."
        elif not ApprovalCheck(JubesX, 500, "L"):
                $ JubesX.FaceChange("normal",0)
                if not Player.Male:
                    ch_v "Она. . . хороший источник железа. . ."
                else:
                    ch_v "Он. . . хороший источник железа. . ."
        else:
                $ JubesX.FaceChange("sad",1,Eyes="leftside")
                if not Player.Male:
                    ch_v "Ну. . . она клевая, мы иногда общаемся. . ."
                else:
                    ch_v "Ну. . . он клевый, мы иногда общаемся. . ."
        $ GwenX.FaceChange("normal",1,Eyes="side")
        $ JubesX.FaceChange("smile",1,Eyes="side",Mouth="open")
        ch_v "Ладно, была рада знакомству, [GwenX.Name]!"
        ch_g "Ага!"
        $ GwenX.FaceChange("normal",1)
        $ JubesX.FaceChange("smile",1)
        $ JubesX.GirlLikeUp(GwenX,100)
        $ GwenX.GirlLikeUp(JubesX,100)
        $ GwenX.DrainWord("Jubes",0,0,0,1)
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
        return
# End Meet Jubes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Gwen_Meet_Check(BO=[],Tempcount=0):
        #Tempcount tracks how many people are still in her list of meets
        #"metall" means she's already met everyone.
        if GwenX.Loc != bg_current:
                # ends if Gwen is not here, or she's already met everyone
                return
        $ BO = TotalGirls[:]
        $ BO.remove(GwenX)
        while BO:
                if BO[0].Tag in GwenX.History:
                    $ Tempcount += 1
                    if BO[0].Loc == bg_current or (bg_current == "bg classroom" and BO[0].Loc == "bg teacher"):
                            #if this person is not in the room, or this is a classroom in which they are teaching
                            call expression "Gwen_"+BO[0].Tag+"_Meet"
                $ BO.remove(BO[0])
#        if not Tempcount:
#                #If she's met everyone, wrap it up.
#                $ GwenX.AddWord(1,0,0,0,"metall") #history
        return
# End Character Meet Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Gwen_Second_Chance:
        #called if "gwengone" in Player.Traits
        #added "promised" trait to Gwen if you promise to help, and "canceled" either way as a memory, and "goodbye" if you refuse
        $ Player.DrainWord("gwengone",0,0,1) #removed from traits
        if GwenX in ActiveGirls:
                return
        "[GwenX.Name] появляется, словно из ниоткуда. Снова."

        $ GwenX.Loc = bg_current
        call CleartheRoom(GwenX)
        call Set_The_Scene
        call Taboo_Level

        if "cancelled" in GwenX.Traits:
                #you already did this once before
                $ GwenX.FaceChange("sad",1)
                ch_g "Ладно, я поняла. Ты не хочешь, чтобы я была рядом."
                $ GwenX.FaceChange("angry",1)
                if not Player.Male:
                    ch_g "Ты не должна была так поступать."
                else:
                    ch_g "Ты не должен был так поступать."
                ch_g "Скажи, что мне нужно сделать, чтобы купить мне еще один день. . ."
                jump Gwen_Third_Chance
        $ GwenX.AddWord(1,0,0,"cancelled") #traits
        $ GwenX.FaceChange("surprised",1,Mouth="open")
        ch_g "О, [Player.Name]!"
        ch_g "Я рада, что смогла найти тебя!"
        $ GwenX.FaceChange("sly",1,Eyes="leftside")
        ch_g "Слушай, я не знаю, сколько времени мне осталось, Ксавье в последнее время почему-то не дает мне покоя."
        $ GwenX.FaceChange("confused",1)
        ch_g "Я чувствую, что. . . возможно, мы начали не с той ноты?"
        $ GwenX.FaceChange("sad",1)
        ch_g "Возможно, тебе почему-то не нравится, что я рядом?"
        $ GwenX.FaceChange("sadside",1)
        ch_g "И, эм. . . это для меня проблема. . ."
        menu:
            extend ""
            ". . .":
                    pass
                    $ GwenX.Statup("Love", 80, -1)
                    $ GwenX.Statup("Obed", 80, 1)
                    $ GwenX.Statup("Inbt", 80, 1)
            "Что? Почему?":
                    $ GwenX.Statup("Obed", 80, 2)
            "Я думала, что избавился от тебя." if not Player.Male:
                    $ GwenX.Statup("Love", 60, -2)
                    $ GwenX.Statup("Love", 200, -2)
                    $ GwenX.FaceChange("surprised",1)
                    ch_g "Да, да!"
                    $ GwenX.FaceChange("sadside",1)
                    $ GwenX.Statup("Obed", 70, 2)
                    $ GwenX.Statup("Obed", 95, 3)
                    ch_g "Ладно, давай оставим это в прошлом. . ."
            "Я думал, что избавился от тебя." if Player.Male:
                    $ GwenX.Statup("Love", 60, -2)
                    $ GwenX.Statup("Love", 200, -2)
                    $ GwenX.FaceChange("surprised",1)
                    ch_g "Да, да!"
                    $ GwenX.FaceChange("sadside",1)
                    $ GwenX.Statup("Obed", 70, 2)
                    $ GwenX.Statup("Obed", 95, 3)
                    ch_g "Ладно, давай оставим это в прошлом. . ."
        ch_g "Я должна объяснить. . ."
        ch_g "Это ведь игра, так?"
        menu:
            extend ""
            ". . .":
                    pass
                    $ GwenX.Statup("Love", 80, -1)
                    $ GwenX.Statup("Obed", 80, 2)
            "Ну, ты так говоришь. . .":
                    $ GwenX.FaceChange("surprised",1)
                    $ GwenX.Statup("Love", 70, 1)
                    $ GwenX.Statup("Love", 90, 1)
                    $ GwenX.Statup("Obed", 80, 2)
                    ch_g "Ага."
            "Из-за этого бреда я и избавилась от тебя." if not Player.Male:
                    $ GwenX.FaceChange("surprised",2)
                    $ GwenX.Statup("Love", 70, -2)
                    $ GwenX.Statup("Love", 200, -1)
                    $ GwenX.Statup("Obed", 90, 3)
                    ch_g "Извини! Извини! Просто потерпи меня минутку!"
            "Из-за этого бреда я и избавился от тебя." if Player.Male:
                    $ GwenX.FaceChange("surprised",2)
                    $ GwenX.Statup("Love", 70, -2)
                    $ GwenX.Statup("Love", 200, -1)
                    $ GwenX.Statup("Obed", 90, 3)
                    ch_g "Извини! Извини! Просто потерпи меня минутку!"
        $ GwenX.FaceChange("sad",1)
        ch_g "Так вот, ты \"главный герой.\""
        menu:
            extend ""
            ". . .":
                    $ GwenX.FaceChange("sly",1)
                    $ GwenX.Statup("Inbt", 80, 2)
                    if not Player.Male:
                        ch_g "Хорошо, я приму такой ответ за \"Я отлично тебя поняла, [GwenX.Name].\""
                    else:
                        ch_g "Хорошо, я приму такой ответ за \"Я отлично тебя понял, [GwenX.Name].\""
            "Я?!":
                    $ GwenX.FaceChange("surprised",1)
                    $ GwenX.Statup("Love", 50, 1)
                    $ GwenX.Statup("Inbt", 80, 2)
                    ch_g "Да! И это очевидно!"
                    $ GwenX.Statup("Love", 80, 1)
                    if not Player.Male:
                        ch_g "Ты когда-нибудь смотрела на себя в зеркало?"
                    else:
                        ch_g "Ты когда-нибудь смотрел на себя в зеркало?"
                    $ GwenX.FaceChange("angry",1,Eyes="side")
                    $ GwenX.Statup("Obed", 80, 2)
                    ch_g "Конечно нет, здесь нет зеркал!"
                    $ GwenX.FaceChange("sad",1)
            "Еще бы.":
                    $ GwenX.FaceChange("angry",1,Eyes="side",Mouth="smirk")
                    $ GwenX.Statup("Love", 70, -1)
                    $ GwenX.Statup("Obed", 80, 2)
                    if not Player.Male:
                        ch_g "Конечно. . . ты -такая- уверенная в себе. . ."
                    else:
                        ch_g "Конечно. . . ты -такой- уверенный в себе. . ."
                    $ GwenX.FaceChange("sly",1)
            "Вот поэтому мы и не общаемся.":
                    $ GwenX.FaceChange("surprised",2,Mouth="open")
                    $ GwenX.Statup("Love", 70, -2)
                    $ GwenX.Statup("Love", 90, -2)
                    ch_g "Знаю, знаю!"
                    $ GwenX.FaceChange("sad",1)
                    ch_g "Еще раз извини, но мы должны все прояснить. . ."
                    $ GwenX.Statup("Obed", 80, 2)
        ch_g "Так вот, ты ГГ, когда тебя нет рядом, мне особо нечем заняться."
        $ GwenX.FaceChange("sad",1)
        ch_g "Пока я выполняла \"работу по хозяйству\" у Ксавье, почти ничего интересного не происходило."
        ch_g "Мне казалось, что я просто застряла на месте. . ."
        ch_g "Меня такое не устраивает."
        menu:
            ". . .":
                    $ GwenX.FaceChange("sly",1)
                    $ GwenX.Statup("Inbt", 80, 2)
                    ch_g "Ладно, хорошо, это не \"нет,\". У меня есть план. . ."
            "Чем я могу помочь?":
                    $ GwenX.FaceChange("smile",1)
                    $ GwenX.Statup("Love", 70, 1)
                    $ GwenX.Statup("Love", 80, 1)
                    $ GwenX.Statup("Inbt", 80, 1)
                    ch_g "О, спасибо! Все очень просто. . ."
            "Это не мои проблемы.":
                    $ GwenX.Statup("Love", 50, -1)
                    $ GwenX.Statup("Love", 80, -1)
                    $ GwenX.Statup("Obed", 80, 2)
                    ch_g "Ладно, я понимаю, но выслушай меня. . ."
            "Ничем не могу помочь.":
                    $ GwenX.Statup("Love", 70, -1)
                    $ GwenX.Statup("Love", 200, -2)
                    $ GwenX.Statup("Inbt", 80, 2)
                    ch_g "Нет, -можешь-. . ."
        if not Player.Male:
            ch_g "Все, что мне нужно, это чтобы ты замолвила за меня словечко перед Ксавье."
        else:
            ch_g "Все, что мне нужно, это чтобы ты замолвил за меня словечко перед Ксавье."
        ch_g "Освободи меня от обязанностей, чтобы я могла снова начать тусоваться с вами, ребята."
        menu:
            ". . .":
                    $ GwenX.FaceChange("confused",1)
                    $ GwenX.Statup("Love", 60, -1)
                    $ GwenX.Statup("Love", 80, -1)
                    $ GwenX.Statup("Inbt", 80, 2)
                    if not Player.Male:
                        ch_g "Мне нужно, чтобы ты сейчас ответила \"да\". . ."
                    else:
                        ch_g "Мне нужно, чтобы ты сейчас ответил \"да\". . ."
                    $ GwenX.AddWord(1,"dotdot") #traits
            "Хорошо, я позабочусь об этом.":
                    $ GwenX.Statup("Love", 70, 2)
                    $ GwenX.Statup("Love", 95, 1)
                    $ GwenX.Statup("Inbt", 80, 2)
                    $ GwenX.FaceChange("surprised",1)
                    ch_g "Серьезно, я сде-"
                    $ GwenX.FaceChange("surprised",1,Mouth="open")
                    ch_g "Что? Правда?"
                    $ GwenX.FaceChange("surprised",1)
                    $ GwenX.Statup("Love", 80, 1)
                    ch_g "Спасибо!!!"
                    $ GwenX.AddWord(1,0,0,"promised") #traits
                    return
            "Что мне с этого будет?":
                    $ GwenX.Statup("Love", 70, -1)
                    $ GwenX.Statup("Obed", 70, 2)
                    $ GwenX.Statup("Obed", 90, 1)
                    $ GwenX.FaceChange("sly",1,Brows="angry")
            "Я не хочу, чтобы ты была рядом.":
                    $ GwenX.FaceChange("surprised",1)
                    $ GwenX.Statup("Love", 70, -1)
                    $ GwenX.Statup("Love", 200, -2)
                    $ GwenX.Statup("Obed", 80, 2)
                    ch_g "Ох. . . Ладно. . ."
                    $ GwenX.FaceChange("sly",1)
                    $ GwenX.Statup("Inbt", 80, 2)
                    ch_g "Но что, если это будет того стоить?"
        ch_g "Ну, я могу. . . что-нибудь для тебя сделать. . ."
        $ GwenX.FaceChange("sly",2)
        ch_g "Что-нибудь сексуальное. . ."
        if "lover" in GwenX.Petnames:
                $ GwenX.FaceChange("normal", 2)
                if not Player.Male:
                    ch_g "Ты любила меня когда-то. . ."
                else:
                    ch_g "Ты любил меня когда-то. . ."
        elif "boyfriend" in GwenX.Petnames:
                $ GwenX.FaceChange("normal", 1)
                ch_g "Когда-то мы хорошо проводили время вместе. . ."
        elif "sexfriend" in GwenX.Petnames:
                $ GwenX.FaceChange("sly", 1)
                ch_g "Мы так хорошо проводили время вместе. . ."
        elif "sir" in GwenX.Petnames:
                ch_g "Я была твоей верной слугой. . ."
        $ GwenX.FaceChange("sly",1)
        ch_g "Чего тебе хотелось бы. . ?"
label Gwen_Third_Chance:
        while True:
            menu:
                ". . ." if "dotdot" not in GwenX.RecentActions:
                        $ GwenX.FaceChange("confused",1)
                        $ GwenX.Statup("Love", 80, -2)
                        if not Player.Male:
                            ch_g "Мне нужно, чтобы вытащила меня. . ."
                        else:
                            ch_g "Мне нужно, чтобы вытащил меня. . ."
                        $ GwenX.AddWord(1,"dotdot") #recent

                "Хорошо, я позабочусь об этом.":
                        $ GwenX.FaceChange("surprised",1)
                        $ GwenX.Statup("Love", 70, 2)
                        $ GwenX.Statup("Love", 95, 1)
                        $ GwenX.Statup("Inbt", 80, 2)
                        ch_g "Серьезно, я сде-"
                        $ GwenX.FaceChange("surprised",1,Mouth="open")
                        ch_g "Что? Правда?"
                        $ GwenX.FaceChange("surprised",1)
                        $ GwenX.Statup("Love", 80, 1)
                        ch_g "Спасибо!!!"
                        $ GwenX.AddWord(1,0,0,"promised") #traits
                        $ GwenX.Forced = 0
                        $ GwenX.OutfitChange(6,Changed=0)
                        return

                "Ничего." if "final" not in GwenX.RecentActions:
                        $ GwenX.AddWord(1,"final") #recent
                        $ GwenX.FaceChange("sad",1)
                        $ GwenX.Statup("Love", 70, -1)
                        $ GwenX.Statup("Love", 200, -1)
                        $ GwenX.Statup("Obed", 80, 2)
                        if "task" in GwenX.RecentActions:
                                if not Player.Male:
                                    ch_g "Давай, не отказывай мне, ты обещала. . ."
                                else:
                                    ch_g "Давай, не отказывай мне, ты обещал. . ."
                                $ GwenX.Statup("Love", 90, -2)
                                $ GwenX.Statup("Obed", 70, 1)
                                $ GwenX.Statup("Obed", 90, 2)
                        else:
                                $ GwenX.Statup("Inbt", 80, 2)
                                ch_g "Давай, я сделаю здесь все, что угодно. . ."
                "Ничего. [[Конец]" if "final" in GwenX.RecentActions:
                        $ GwenX.FaceChange("sad",1,Eyes="surprised")
                        $ GwenX.Statup("Love", 70, -1)
                        $ GwenX.Statup("Love", 200, -2)
                        $ GwenX.Statup("Obed", 90, 3)
                        ch_g ". . ."
                        $ GwenX.FaceChange("sadside",1)
                        if "task" in GwenX.RecentActions:
                                $ GwenX.Statup("Love", 200, -2)
                                $ GwenX.Statup("Obed", 70, 1)
                                $ GwenX.Statup("Obed", 90, 2)
                        ch_g "Ладно. . ."
                        ch_g "Мне придется принять неизбежное. . ."
                        ch_g "До свидания. . ."
                        $ GwenX.AddWord(1,0,0,"goodbye") #traits
                        call Remove_Girl(GwenX)
                        return

                "Покажи мне сиськи." if "task" not in GwenX.RecentActions:
                        $ GwenX.AddWord(1,"task") #recent
                        if not Taboo and GwenX.SeenChest and ApprovalCheck(GwenX, 800):
                                $ GwenX.FaceChange("normal",1)
                                $ GwenX.Statup("Obed", 80, 2)
                        elif ApprovalCheck(GwenX, 500, "I"):
                                $ GwenX.FaceChange("normal",1)
                                $ GwenX.Statup("Obed", 60, 2)
                                $ GwenX.Statup("Obed", 80, 2)
                        else:
                                $ GwenX.FaceChange("sad",2)
                                $ GwenX.Statup("Love", 70, -1)
                                $ GwenX.Statup("Love", 200, -1)
                                $ GwenX.Statup("Obed", 70, 1)
                                $ GwenX.Statup("Obed", 90, 2)
                        ch_g "Эм. . . ладно. . ."
                        $ GwenX.Uptop = 1 #Uptop up
                        pause 0.5
                        $ GwenX.Upskirt = 1 #Upskirt up
                        $ GwenX.PantiesDown = 1 #Upskirt up
                        pause 1
                        call Girl_First_Topless(GwenX,1)
                        call Girl_First_Bottomless(GwenX,1)
                        $ GwenX.PantiesDown = 0 #Upskirt up
                        $ GwenX.Upskirt = 0 #Upskirt up
                        pause 0.5
                        $ GwenX.Uptop = 0 #Uptop up
                        "Она быстро показывает вам грудь."
                        if Taboo >= 40:
                                $ GwenX.Blush = 2
                                $ GwenX.Rep -= 2
                                "Некоторые люди замечают это и смеются."
                        if not Player.Male:
                            ch_g "Ладно. . . эм. . . ты довольна?"
                        else:
                            ch_g "Ладно. . . эм. . . ты доволен?"

                "Разденься." if "task" not in GwenX.RecentActions:
                        $ GwenX.AddWord(1,"task") #recent
                        if not Taboo and GwenX.SeenPussy and ApprovalCheck(GwenX, 1000):
                                $ GwenX.FaceChange("normal",1)
                                $ GwenX.Statup("Obed", 80, 2)
                        elif ApprovalCheck(GwenX, 700, "I"):
                                $ GwenX.FaceChange("normal",1)
                                $ GwenX.Statup("Obed", 60, 2)
                                $ GwenX.Statup("Obed", 80, 3)
                        else:
                                $ GwenX.FaceChange("sad",2)
                                $ GwenX.Statup("Love", 70, -1)
                                $ GwenX.Statup("Love", 200, -2)
                                $ GwenX.Statup("Obed", 70, 2)
                                $ GwenX.Statup("Obed", 90, 2)
                        ch_g "Эм . . . Ладно. . ."
                        if GwenX.Over or GwenX.Chest:
                                $ GwenX.Uptop = 1
                                pause 0.3
                        if GwenX.Over:
                                $ GwenX.Over = 0
                                pause 0.3
                        if GwenX.Chest:
                                $ GwenX.Chest = 0
                        call Girl_First_Topless(GwenX)
                        pause 0.3
                        if GwenX.Legs:
                                $ GwenX.Upskirt = 1
                                pause 0.3
                                $ GwenX.Legs = 0
                                pause 0.3
                        if GwenX.Hose:
                                $ GwenX.Hose = 0
                                pause 0.3
                        if GwenX.Panties:
                                $ GwenX.PantiesDown = 1
                                pause 0.2
                                $ GwenX.Panties = 0
                        call Girl_First_Bottomless(GwenX)
                        "Она кладет свою одежду на пол."
                        if Taboo >= 40:
                                $ GwenX.Blush = 2
                                $ GwenX.Rep -= 2
                                "Некоторые люди замечают это и смеются."
                        if not Player.Male:
                            ch_g "Ладно. . . эм. . . ты довольна?"
                        else:
                            ch_g "Ладно. . . эм. . . ты доволен?"

                "Отсоси мне." if True and Player.Male:    #fix, remove this brake once Gwen can suck cocks.  if "task" not in GwenX.RecentActions
                        if ApprovalCheck(GwenX, 1300, TabM = 4):
                                $ GwenX.Statup("Obed", 80, 3)
                        elif ApprovalCheck(GwenX, 1000, TabM = 4) and (GwenX.Blow or GwenX.CUN):
                                $ GwenX.Statup("Obed", 60, 2)
                                $ GwenX.Statup("Obed", 80, 3)
                        else:
                                $ GwenX.Statup("Love", 70, -2)
                                $ GwenX.Statup("Love", 200, -3)
                                $ GwenX.Statup("Obed", 70, 2)
                                $ GwenX.Statup("Obed", 90, 3)
                                $ GwenX.Forced = 1
                        $ Tempmod = 25
                        if Player.Male:
                                call Girl_Blowjob
                        else:
                                call Gwen_Girltalk(1) # "Hey, are you inta me?"
                                call Girl_CUN
                        if "angry" not in GwenX.RecentActions and ("blow" in GwenX.RecentActions or "cun" in GwenX.RecentActions):
                            $ GwenX.AddWord(1,"task") #recent
                            $ GwenX.Statup("Obed", 50, 10)
                            $ GwenX.Statup("Obed", 80, 5)
                            $ GwenX.Statup("Inbt", 50, 10)
                            $ GwenX.Statup("Inbt", 80, 5)
                            $ GwenX.FaceChange("sad",1)
                            ch_g "Значит, этого должно быть достаточно, верно?"
                        else:
                            $ GwenX.FaceChange("sad",2)
                            ch_g ". . . извини."

                "Отлижи мне." if True and not Player.Male:    #fix, remove this brake once Gwen can suck cocks.  if "task" not in GwenX.RecentActions
                        if ApprovalCheck(GwenX, 1300, TabM = 4):
                                $ GwenX.Statup("Obed", 80, 3)
                        elif ApprovalCheck(GwenX, 1000, TabM = 4) and (GwenX.Blow or GwenX.CUN):
                                $ GwenX.Statup("Obed", 60, 2)
                                $ GwenX.Statup("Obed", 80, 3)
                        else:
                                $ GwenX.Statup("Love", 70, -2)
                                $ GwenX.Statup("Love", 200, -3)
                                $ GwenX.Statup("Obed", 70, 2)
                                $ GwenX.Statup("Obed", 90, 3)
                                $ GwenX.Forced = 1
                        $ Tempmod = 25
                        if Player.Male:
                                call Girl_Blowjob
                        else:
                                call Gwen_Girltalk(1) # "Hey, are you inta me?"
                                call Girl_CUN
                        if "angry" not in GwenX.RecentActions and ("blow" in GwenX.RecentActions or "cun" in GwenX.RecentActions):
                            $ GwenX.AddWord(1,"task") #recent
                            $ GwenX.Statup("Obed", 50, 10)
                            $ GwenX.Statup("Obed", 80, 5)
                            $ GwenX.Statup("Inbt", 50, 10)
                            $ GwenX.Statup("Inbt", 80, 5)
                            $ GwenX.FaceChange("sad",1)
                            ch_g "Значит, этого должно быть достаточно, верно?"
                        else:
                            $ GwenX.FaceChange("sad",2)
                            ch_g ". . . извини."


                "Позволь мне трахнуть тебя." if True:    #fix, remove this brake once Gwen can suck cocks.
                        if ApprovalCheck(GwenX, 1400, TabM = 5):
                                $ GwenX.Statup("Obed", 90, 4)
                                $ GwenX.Statup("Obed", 95, 1)
                        elif ApprovalCheck(GwenX, 1300, TabM = 5) and GwenX.Sex:
                                $ GwenX.Statup("Obed", 60, 2)
                                $ GwenX.Statup("Obed", 90, 3)
                                $ GwenX.Statup("Obed", 95, 1)
                        else:
                                $ GwenX.Statup("Love", 80, -2)
                                $ GwenX.Statup("Love", 200, -5)
                                $ GwenX.Statup("Obed", 80, 3)
                                $ GwenX.Statup("Obed", 90, 3)
                                $ GwenX.Forced = 1
                        $ Tempmod = 25
                        if Player.Male:
                                call Girl_Sex_P
                        else:
                                call Gwen_Girltalk(1) # "Hey, are you inta me?"
                                call Girl_CUN
                        if "angry" not in GwenX.RecentActions and "sex" in GwenX.RecentActions:
                            $ GwenX.AddWord(1,"task") #recent
                            $ GwenX.Statup("Obed", 50, 10)
                            $ GwenX.Statup("Obed", 80, 5)
                            $ GwenX.Statup("Inbt", 50, 10)
                            $ GwenX.Statup("Inbt", 80, 5)
                            $ GwenX.FaceChange("sad",1)
                            ch_g "Значит, этого должно быть достаточно, верно?"
                        else:
                            $ GwenX.FaceChange("sad",2)
                            ch_g ". . . извини."

                "Позволь мне трахнуть тебя в попку." if True:    #fix, remove this brake once Gwen can suck cocks.
                        if ApprovalCheck(GwenX, 1550, TabM = 5):
                                $ GwenX.Statup("Obed", 90, 3)
                                $ GwenX.Statup("Obed", 95, 2)
                        elif ApprovalCheck(GwenX, 1400, TabM = 5) and GwenX.Anal:
                                $ GwenX.Statup("Obed", 60, 1)
                                $ GwenX.Statup("Obed", 90, 3)
                                $ GwenX.Statup("Obed", 295, 2)
                        else:
                                $ GwenX.Statup("Love", 80, -3)
                                $ GwenX.Statup("Love", 200, -5)
                                $ GwenX.Statup("Obed", 80, 3)
                                $ GwenX.Statup("Obed", 95, 3)
                                $ GwenX.Forced = 1
                        $ Tempmod = 25
                        call Gwen_Girltalk(1) # "Hey, are you inta me?"
                        call Girl_Sex_A
                        if "angry" not in GwenX.RecentActions and "anal" in GwenX.RecentActions:
                            $ GwenX.AddWord(1,"task") #recent
                            $ GwenX.Statup("Obed", 50, 10)
                            $ GwenX.Statup("Obed", 80, 5)
                            $ GwenX.Statup("Inbt", 50, 10)
                            $ GwenX.Statup("Inbt", 80, 5)
                            $ GwenX.FaceChange("sad",1)
                            ch_g "Значит, этого должно быть достаточно, верно?"
                        else:
                            $ GwenX.FaceChange("sad",2)
                            ch_g ". . . извини."
        return

label Gwenback:
        #Plays once when Gwen is returned to active duty while "Gwengone" is active
        $ GwenX.FaceChange("smile",1,Mouth="open")
        hide Gwen_Seated
        show Gwen_Sprite at SpriteLoc(550,50) zorder GwenX.Layer:
            subpixel True
            offset (1000,0)
            zoom 1
            anchor (0.5, 0.0)
            ease 1 xoffset -1000
            pause 1
        ch_g "О да, детка, я вернулась!"
        hide Gwen_Sprite
        $ GwenX.FaceChange("smile",1)
        $ Player.DrainWord("gwengone",0,0,1) #removes from traits
        $ GwenX.DrainWord("promised",0,0,1) #removes from traits
        $ GwenX.DrainWord("goodbye",0,0,1) #removes from traits
        return


# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Gwen_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        if "switched" in GwenX.History:
                jump Gwen_Switch2
        $ GwenX.FaceChange("normal", 1)
        ch_g "Привет?"
        $ GwenX.FaceChange("confused", 1)
        ch_g "Подожди-ка. . ."
        ch_g ". . ."
        ch_g "[Player.XName]?"
        menu:
            extend ""
            "Да, это я, [Player.XName].":
                    $ GwenX.FaceChange("smile", 1)
                    ch_g "Knew it!"
                    $ GwenX.AddWord(1,"switch") #recent

            "Нет.":
                    ch_g "Хм."
                    ch_g "К слову, меня зовут [GwenX.Name]."
            "Возможно?":
                    ch_g "Возможно. . ."

        if "switch" not in GwenX.RecentActions:
                    $ GwenX.FaceChange("confused", 1)
                    ch_g ". . ."
                    $ GwenX.FaceChange("surprised", 1,Mouth= "open")
                    ch_g "Это ты! [Player.XName]!"
                    $ GwenX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Ага, это я, [Player.XName].":
                                $ GwenX.Statup("Love", 90, 1)
                                $ GwenX.Statup("Obed", 70, 1)
                                ch_g "Я знала!"
                                $ GwenX.FaceChange("normal", 1)
                        "Нет.":
                                $ GwenX.FaceChange("angry", 1)
                                $ GwenX.Statup("Obed", 60, 1)
                                $ GwenX.Statup("Obed", 70, 1)
                                ch_g "Чушь."
                        "Возможно?":
                                $ GwenX.FaceChange("sly", 1)
                                $ GwenX.Statup("Love", 80, 1)
                                $ GwenX.Statup("Obed", 70, 1)
                                $ GwenX.Statup("Inbt", 60, 1)
                                ch_g "Тебе меня не одурачить!"
                    ch_g "Почему ты играешь со мной?"
                    menu:
                        extend ""
                        "Извини, хотелось пошутить.":
                                $ GwenX.FaceChange("sly", 1)
                                $ GwenX.Statup("Love", 70, 1)
                        "Молодец, ты все поняла.":
                                $ GwenX.FaceChange("sly", 1)
                                $ GwenX.Statup("Obed", 70, 1)
                                $ GwenX.Statup("Inbt", 80, 1)
                                ch_g "Ну конечно!"
                        "Хех.":
                                $ GwenX.FaceChange("sly", 1,Eyes="side")
                                $ GwenX.Statup("Love", 70, 1)
                                $ GwenX.Statup("Love", 90, 1)
                                $ GwenX.Statup("Inbt", 70, 1)
                                ch_g "Ага, хех. . ."
                    ch_g "Никто лучше меня не знает про \"Правило 63\". . . [[63 - у любого персонажа непременно есть версия противоположного пола]"
        #end "tried to lie"
        $ GwenX.FaceChange("smile", 1)
        ch_g "Ну и к чему такие изменения?"
        menu:
            extend ""
            "Да так, по приколу.":
                    $ GwenX.Statup("Inbt", 70, 1)
                    $ GwenX.FaceChange("sly", 1)
                    ch_g "Ха."
            "Я так себя сейчас ощущаю.":
                    ch_g "Ага, в этом есть смысл."
            "У меня не было каких-то особых причин.":
                    ch_g "Просто захотелось сразу прожать все кнопки, да?"

        if [Player.Name] != [Player.XName]:
                ch_p "А еще теперь меня зовут [Player.Name]."
                ch_g "Ладно, клево."

        if GwenX.SEXP >= 15:
                $ GwenX.FaceChange("sad", 1,Mouth="normal")
                ch_g "Я тебе все еще привлекаю, правда?"
                menu:
                    extend ""
                    "Конечно!":
                            $ GwenX.FaceChange("normal", 1)
                            $ GwenX.Statup("Love", 70, 2)
                            $ GwenX.Statup("Love", 90, 1)
                            ch_g "Отлично. . ."
                    "Да не особо.":
                            $ GwenX.FaceChange("sad", 1)
                            $ GwenX.Statup("Love", 80, -2)
                            $ GwenX.Statup("Obed", 60, 2)
                            $ GwenX.Statup("Obed", 80, 2)
                            ch_g "Оу."
                    "А ты как думаешь?":
                            $ GwenX.FaceChange("sly", 1)
                            $ GwenX.Statup("Obed", 70, 1)
                            $ GwenX.Statup("Inbt", 70, 1)
                            ch_g "Я думаю, ты напрыгиваешь на все, что движется. . ."

        if not Player.Male and GwenX.Les > 5:
                $ GwenX.FaceChange("sly", 1)
                ch_g "Ну, я думаю, для меня оболочка не играет большого значения. . ."
        if ApprovalCheck(GwenX, 1200):
                ch_g "Это может быть весело."
                $ GwenX.AddWord(1,0,0,0,"girltalk") #history
        else:
                $ GwenX.FaceChange("normal", 1,Eyes="side")
                ch_g "В общем, свидимся. . ."
        $ GwenX.Traits.remove("switchcheck")
        $ GwenX.AddWord(1,0,0,0,"switched") #history
        return

label Gwen_Switch2:
        #when you switch for a 2+ time
        $ GwenX.FaceChange("smile", 1)
        ch_g "О, а вот и возвращение классического образа [Player.Name_rod]."
        $ GwenX.Traits.remove("switchcheck")
        $ GwenX.History.remove("switched")
        $ GwenX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Gwen_Girltalk(Auto=0,Other=0):
        # if Auto Gwen starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in GwenX.History:
                return
        if "nogirls" in GwenX.History:
                jump Gwen_Girltalk_Redux
        $ GwenX.FaceChange("normal", 1)
        if Auto:
                ch_g "Так, [Player.Name]. . ."
        ch_g "Ты ведь по девочкам, правда?"
        ch_g "Ну и как тебе я? Нравлюсь?"
        menu:
            extend ""
            "Да?":
                    $ GwenX.FaceChange("sly", 1)
                    $ GwenX.Statup("Love", 70, 2)
                    $ GwenX.Statup("Love", 90, 2)
                    $ GwenX.Statup("Obed", 70, 1)
                    ch_g "Логично."
            "Наверное?":
                    $ GwenX.FaceChange("confused", 1)
                    $ GwenX.Statup("Love", 70, 1)
                    $ GwenX.Statup("Obed", 80, 2)
                    $ GwenX.Statup("Inbt", 80, 2)
                    ch_g "Ну и зачем тогда я здесь?"
            "Не особо.":
                    $ GwenX.FaceChange("surprised", 1)
                    $ GwenX.Statup("Love", 90, -1)
                    $ GwenX.Statup("Obed", 60, 2)
                    $ GwenX.Statup("Obed", 80, 2)
                    ch_g "Что?!"
                    ch_g "Тогда какой во всем этом смысл?"
        $ GwenX.FaceChange("sly", 1)
        if not GwenX.Les:
                ch_g "У меня не так уж много. . ."
                $ GwenX.FaceChange("sadside", 2)
                ch_g "-опыта. . ."
                ch_g "-с другими девушками. . ."
        if not ApprovalCheck(GwenX, 1000) and not ApprovalCheck(GwenX, 600, "L") and not GwenX.Les:
                ch_g "Я, эм. . . я не уверена, готова ли к подобному. . ."
                $ GwenX.AddWord(1,0,0,0,"nogirls") #history
                call Girltalk_Check(GwenX)
                return

        ch_g "Думаю, мы все всего лишь пиксели, зачем беспокоиться о деталях?"
        $ GwenX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(GwenX)
        return

label Gwen_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing
        if ApprovalCheck(GwenX, 1000) or ApprovalCheck(GwenX, 600, "L"):
                $ GwenX.FaceChange("sly", 1)
                if Other in TotalGirls and "nogirls" in Other.History:
                        ch_g "Я не уверена. . ."
                ch_g ". . . ну хорошо."
                ch_g "Думаю, мы все всего лишь пиксели, зачем беспокоиться о деталях?"
                $ GwenX.DrainWord("nogirls",0,0,0,1) #history
                $ GwenX.AddWord(1,0,0,0,"girltalk") #history
        elif "nogirls" not in GwenX.History:
                $ GwenX.AddWord(1,0,0,0,"nogirls") #history
                ch_g "Эм. . . не сейчас."
        elif "nogirls" in GwenX.DailyActions:
                $ GwenX.FaceChange("angry", 1)
                if GwenX.Forced:
                        #if Forced, she will just go with it anyway
                        if "nogirls" not in GwenX.RecentActions:
                                $ GwenX.Statup("Love", 80, -2)
                                $ GwenX.Statup("Obed", 80, 2)
                                $ GwenX.AddWord(1,"nogirls",0,0,0) #recent
                        return
                ch_g "Перестань спрашивать."
        else:
                $ GwenX.Statup("Inbt", 50, 2)
                ch_g "Сейчас мне не неинтересны такие отношения."
                $ GwenX.AddWord(1,0,"nogirls",0,0) #daily
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Gwen_69_Intro:
    return
