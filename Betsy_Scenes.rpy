
# start BetsyMeet//////////////////////////////////////////////////////////

label BetsyMeet:
        $ BetsyX.Name = "? ? ?"
        $ Player.AddWord(1,0,"Intro",0,0) #adds tag to Daily
        "Вы почувствовали гул в своей голове."
        ch_x "[Player.Name], сегодня к нам должна прибыть студентка по обмену."
        if not Player.Male:
            ch_x "Не могла бы ты проводить ее в мой кабинет?"
        else:
            ch_x "Не мог бы ты проводить ее в мой кабинет?"
        $ Line = 0
        $ BetsyX.Event[2] = 0
        while Line:
            #loops until player accepts
            menu:
                extend ""
                "Без проблем.":
                        $ Line = 0
                "Нет, спасибо.":
                        if not Player.Male:
                            ch_x "Я был бы очень признателен, если бы ты позаботилась об этом."
                        else:
                            ch_x "Я был бы очень признателен, если бы ты позаботился об этом."
                        menu:
                            extend ""
                            "Ну ладно,я  все сделаю.":
                                pass
                            "Не, у меня дела.":
                                ch_x ". . ."
                                ch_x "А если я предложу тебе небольшую компенсацию за твое потраченное время?"
                                menu:
                                    extend ""
                                    "Ладно, я все сделаю.":
                                        $ Player.Cash += 5
                                    "Нет, меня это не интересует.":
                                        ch_x ". . . Что ж, хорошо. . ."
                                        $ BetsyX.Event[2] = 2
                                        $ BetsyX.History.append("luggage")
                                        "Вы возвращаетесь к своему прошлому занятию."
                                        return
                        $ Line = 0

                "Хм, новое мясо, ну и кто это?" if Line != "who":
                        $ Line = "who"
                        ch_x "Прошу, [Player.Name], будь серьезнее."

        ch_x "Благодарю. Ты найдешь ее у ворот."
        "Вы направляетесь к главным воротам, возле площади кампуса."
        $ bg_current = "bg campus"
        call Set_The_Scene(0)
        $ BetsyX.FaceChange("smile",Mouth="open")
        $ BetsyX.Love = 500
        $ BetsyX.Obed = 0
        $ BetsyX.Inbt = 200
        $ BetsyX.Lust = 0
        $ BetsyX.SpriteLoc = StageCenter
        $ BetsyX.Petname = Player.Name
        $ BetsyX.Petname_rod = Player.Name_rod
        $ BetsyX.Petname_dat = Player.Name_dat
        $ BetsyX.Petname_vin = Player.Name_vin
        $ BetsyX.Petname_tvo = Player.Name_tvo
        $ BetsyX.Petname_pre = Player.Name_pre
        $ BetsyX.OutfitDay = "casual1"
        $ BetsyX.Outfit = "casual1"
        $ BetsyX.OutfitChange("casual1")
        call CleartheRoom("All",0,1)
        $ BetsyX.Loc = "bg campus"
        $ BetsyX.FaceChange("smile",0)
        $ BetsyX.ArmPose = 2
        if "metall" in GwenX.History:
                #adds a "meet Gwen" sequence
                $ GwenX.History.remove("metall")
                $ GwenX.History.append("Betsy")

        $ DoreenX.Name = "? ? ?"
        $ DoreenX.Loc = "bg campus"
        "Вы видите девушку, которую раньше не встречали в кампусе. Должно быть, про нее и говорил профессор."
        menu:
            "Привет, ты новенькая?":
                    call Shift_Focus(DoreenX)
                    call Display_Girl(DoreenX)
                    ch_d "Я? Да вроде бы нет."
            "Привет.":
                    call Shift_Focus(DoreenX)
                    call Display_Girl(DoreenX)
                    ch_d "Привет!"
                    menu:
                        extend ""
                        "Ты новенькая?":
                                ch_d "Я? Да вроде бы нет."
                        "Мне нужно отвести тебя к Ксавье.":
                                if not Player.Male:
                                    ch_d "Меня? Мне кажется, ты ошиблась."
                                else:
                                    ch_d "Меня? Мне кажется, ты ошибся."
                        "Ладно, пока.":
                                ch_d "Пока!"
                                ch_d "Подожди, мне кажется, там была девушка, которой, возможно, нужна помощь!"
                        "[[развернуться и уйти.]":
                                ch_d "Если ты ищешь новенькую студентку, то это не я."
            "[[развернуться и уйти.]":
                    "Вы возвращаетесь в свою комнату."
                    $ DoreenX.History.append("missed")
                    $ BetsyX.History.append("luggage")
                    $ BetsyX.Event[2] = 2
                    $ bg_current = "bg player"
                    jump Misplaced
        ch_d ". . ."
        ch_d "Должна объяснить, я здесь не учусь, по крайней мере пока."
        ch_d "Я не успела поступить до начала семестра, но я в списке на зачисление. Вот я и приехала осмотреться."
        ch_d "Как-то так. . . В общем, по пути сюда я встретила девушку с кучей сумок, уверена, ей не помешала бы помощь."
        ch_d "Ну, если тебе это, конечно, интересно. . ."
        menu:
            extend ""
            "Спасибо за помощь, увидимся!":
                    ch_d "Ага, -надеюсь!-"
                    hide Doreen_Sprite with easeoutright
            "Ну ладно.":
                    ch_d ". . . ага. . . ладно. . ."
                    hide Doreen_Sprite with easeoutright
                    "She slowly moves away."
            ". . .":
                    ch_d "Ну ладно. . . пока!"
                    hide Doreen_Sprite with easeoutright
                    "Она уходит."
            "[[идти дальше]":
                    ch_d "Ну ладно. . . пока!"
                    hide Doreen_Sprite with easeoutright
        $ DoreenX.Loc = "hold"


        "Вы видите еще одну девушку, которую раньше не встречали в кампусе. Возможно, именно ее вы и ищите."
        menu:
            "Привет, ты новенькая?":
                    call Shift_Focus(BetsyX)
                    call Display_Girl(BetsyX)
                    ch_b "Пожалуй, можно и так сказать. . ."
                    ch_b "Кажется, мы не представлены? . ."
            "Привет.":
                    call Shift_Focus(BetsyX)
                    call Display_Girl(BetsyX)
                    ch_b "Да? Кажется, мы не представлены? . ."
            "[[развернуться и уйти.]":
                    "Вы возвращаетесь в свою комнату."
                    $ BetsyX.History.append("luggage")
                    $ BetsyX.Event[2] = 2
                    $ bg_current = "bg player"
                    jump Misplaced
        $ BetsyX.History.append("met")
        $ ActiveGirls.append(BetsyX) if BetsyX not in ActiveGirls else ActiveGirls
        menu:
            extend ""
            "Нет, я [Player.Name].":
                    $ BetsyX.Statup("Love", 200, 2)
                    ch_b "Тогда приятно с тобой познакомиться, [Player.Name]."
            "Нет.":
                    $ BetsyX.History.append("name none")
                    $ BetsyX.FaceChange("perplexed")
                    ch_b "Я так и думала."
            "Нет, я Чарьз Ксавье." if Player.Male:
                    $ BetsyX.FaceChange("perplexed")
                    $ BetsyX.Statup("Love", 200, -1)
                    ch_b "Ха, боюсь, нет, приятель."
                    $ BetsyX.FaceChange("sly",0)
                    ch_b "Мы с Чарльзом знаком, и ты - не он."
                    menu:
                        extend ""
                        "Извини, я [Player.Name].":
                                $ BetsyX.FaceChange("smile",0)
                                $ BetsyX.Statup("Love", 200, 2)
                                $ BetsyX.Statup("Obed", 200, 1)
                                ch_b "Не волнуйся, ты меня позабавил."
                        "Подловила, я [Player.Name].":
                                $ BetsyX.FaceChange("smile",0)
                                $ BetsyX.Statup("Love", 200, 2)
                                $ BetsyX.Statup("Inbt", 200, 1)
                                ch_b "Не волнуйся, ты меня позабавил."
                        "Это довольно распространенное имя.":
                                $ BetsyX.FaceChange("perplexed",2)
                                $ BetsyX.History.append("name xavier")
                                $ BetsyX.Statup("Obed", 200, 10)
                                ch_b "Неужели? . .  Хотя. . . мы сейчас в Америке, все может быть."
                        "Как скажешь.":
                                $ BetsyX.History.append("name none")
                                $ BetsyX.FaceChange("perplexed",0)
                                $ BetsyX.Statup("Love", 200, -1)
                                ch_b ". . . эм, конечно."
                    $ BetsyX.FaceChange("smile",0)
            "Представлены. . .":
                    $ BetsyX.History.append("name none")
                    $ BetsyX.FaceChange("perplexed",1)
                    $ BetsyX.Statup("Obed", 200, 2)
                    ch_b "Ах. . . да. . . конечно. . ."
        call AboutBetsy #discusses her name and details
        $ BetsyX.FaceChange("smile",0)
        if not Player.Male:
            ch_b "Ох, не могла бы ты. . ?"
        else:
            ch_b "Ох, не мог бы ты. . ?"
        "Она указывает на небольшую гору чемоданов и сумок."
        menu:
            "С удовольствием помогу тебе.":
                    $ BetsyX.Statup("Love", 200, 5)
                    ch_b "Надеюсь, это не доставит тебе неудобств."
                    menu:
                        extend ""
                        "Конечно нет.":
                                $ BetsyX.FaceChange("sadside",1,Mouth="smile")
                                if not Player.Male:
                                    ch_b "Думаю, ты очень добра."
                                else:
                                    ch_b "Думаю, ты очень добр."
                        "Я уже к этому привыкла." if not Player.Male:
                                $ BetsyX.FaceChange("sad",1,Mouth="smile")
                                ch_b "Прошу прощение за навязчивость."
                        "Я уже к этому привык." if Player.Male:
                                $ BetsyX.FaceChange("sad",1,Mouth="smile")
                                ch_b "Прошу прощение за навязчивость."
                    $ BetsyX.FaceChange("smile",0)
                    ch_b "Уверена, ты справишься."
                    $ BetsyX.FaceChange("sly",1)
                    ch_b "Мне кажется, ты. . . в -хорошей- форме."
            "Нет, спасибо.":
                    $ BetsyX.FaceChange("angry",1,Mouth="open")
                    $ BetsyX.Statup("Love", 200, -2)
                    $ BetsyX.Statup("Obed", 200, 4)
                    ch_b ". . ."
                    $ BetsyX.FaceChange("angry",1,Mouth="normal")
                    ch_b "Хорошо. . ."
                    $ BetsyX.FaceChange("sadside",1,Brows="normal")
                    ch_b "Уверена, мы сможем. . . найти -кого-нибудь-, кто сможет помочь. . ."
            "О, для этого у нас есть персонал.":
                    $ BetsyX.FaceChange("smile",Brows="surprised")
                    $ BetsyX.Statup("Obed", 200, 3)
                    ch_b "Ах! Конечно."
                    "[[На самом деле в институте нет обслуживающего персонала.]"
                    $ BetsyX.Statup("Love", 200, -5)
                    "[[Ее багаж никто не перенесет.]"
        "Вы вместе доходите до кабинета Ксавье и входите внутрь."

        $ bg_current = "bg study"
        call Set_The_Scene(0)
        show Professor at SpriteLoc(StageLeft)
        show Betsy_Sprite at SpriteLoc(OffStage)
        show Betsy_Sprite at SpriteLoc(StageRight) with ease
        $ BetsyX.FaceChange("smile",Eyes="side")
        ch_x "А, вот и вы, дорогая мисс Брэддок. Надеюсь, ваша поездка прошла хорошо."
        $ BetsyX.FaceChange("sly",Eyes="side")
        ch_b "Конечно, Чарльз. . . или мне следует звать вас \"Профессор?\""
        ch_x "Как вам больше нравится."
        $ BetsyX.FaceChange("smile",Eyes="side")
        ch_b "Замечательно. Тогда буду звать вас \"Чарльз\"."
        ch_x "Я полагаю, вы уже представились друг другу?"
        if "Elizabeth" not in BetsyX.Names or "name xavier" in BetsyX.History or "name none" in BetsyX.History:
                $ BetsyX.FaceChange("smile")
                if "Elizabeth" not in BetsyX.Names:
                        ch_b "На самом деле, еще нет. . ."
                        ch_b "Меня зовут Элизабет, хотя я больше предпочитаю, чтобы меня звали \"Бетси.\""
                        $ BetsyX.Name = "Бетси"
                        $ BetsyX.Name_rod = "Бетси"
                        $ BetsyX.Name_dat = "Бетси"
                        $ BetsyX.Name_vin = "Бетси"
                        $ BetsyX.Name_tvo = "Бетси"
                        $ BetsyX.Name_pre = "Бетси"
                        $ BetsyX.Names.append("Elizabeth")
                else:
                        ch_b "Конечно, я представилась. . ."
                if "name xavier" in BetsyX.History:
                        $ BetsyX.FaceChange("smile",Brows="surprised")
                        ch_b "А этот молодой человек сообщил мне, что его зовут так же, как и вас!"
                        ch_x "Правда?"
                        $ BetsyX.FaceChange("sly",1,Brows="angry")
                        $ BetsyX.Statup("Love", 200, -3)
                        $ BetsyX.Statup("Obed", 200, 3)
                        ch_x "Что ж, мне жаль говорить вам, но это была какая-то шутка."
                        $ BetsyX.Statup("Love", 200, -2)
                        ch_x "Его на самом деле зовут [Player.Name]."
                elif "name none" in BetsyX.History:
                        $ BetsyX.FaceChange("smile")
                        if not Player.Male:
                            ch_b ". . . Но эта молодая леди нет. . ."
                            ch_x "Правда? Что ж, тогда позвольте мне представить ее вам."
                            ch_x "Ее зовут [Player.Name]."
                        else:
                            ch_b ". . . Но этот молодой человек нет. . ."
                            ch_x "Правда? Что ж, тогда позвольте мне представить его вам."
                            ch_x "Его зовут [Player.Name]."
                else:
                        $ BetsyX.FaceChange("smile")
                        if not Player.Male:
                            ch_b "А эта молодая леди сообщила мне, что ее зовут \"[Player.Name]\"."
                        else:
                            ch_b "А этот молодой человек сообщил мне, что его зовут \"[Player.Name]\"."
        else:
                        ch_b "Конечно."
        $ BetsyX.FaceChange("normal")
        if not Player.Male:
            ch_x "Я предполагаю, что она еще не рассказала вам, что ее способности позволяют ей сводить на нет способности других мутантов."
        else:
            ch_x "Я предполагаю, что он еще не рассказал вам, что его способности позволяют ему сводить на нет способности других мутантов."
        $ BetsyX.FaceChange("surprised")
        ch_b "В самом деле? Как интересно!"
        $ BetsyX.FaceChange("smile")
        ch_b "Я просто обязана это проверить."
        $ BetsyX.FaceChange("sly",Eyes="psychic")
        ch_b ". . ."
        menu:
            "Вы чувствуете гул в своей голове."
            "Сосредоточиться, чтобы отразить ментальное вторжение.":
                    $ BetsyX.FaceChange("angry",1,Eyes="psychic")
                    $ BetsyX.Statup("Obed", 200, 5)
                    ch_b "Ничего не получается. . ."
            "Впустить ее в свой разум.":
                    $ BetsyX.FaceChange("perplexed",1,Eyes="psychic")
                    $ BetsyX.Statup("Love", 200, 2)
                    $ BetsyX.Statup("Inbt", 200, 1)
                    ch_b "Ничего необычного я не обнаружила, кроме коллекции обнаженных образов. . ."
                    $ BetsyX.FaceChange("surprised",2,Mouth="open")
                    $ BetsyX.Statup("Love", 200, -2)
                    $ BetsyX.Statup("Obed", 200, 3)
                    $ BetsyX.Statup("Inbt", 200, 3)
                    ch_b "Весьма неплохая коллекция, должна отметить. . ."
                    $ BetsyX.FaceChange("sly",1,Brows="angry")
                    $ BetsyX.Statup("Love", 200, 2)
                    if not Player.Male:
                        ch_x "Похоже, что наша мисс [Player.Name] просто играет с вами."
                        ch_x "Уверяю вас, если она захочет, она без проблем отразит вторжение в свою голову."
                    else:
                        ch_x "Похоже, что наш мистер [Player.Name] просто играет с вами."
                        ch_x "Уверяю вас, если он захочет, он без проблем отразит вторжение в свою голову."
            "\"Ммммм, тако.\"":
                    $ BetsyX.FaceChange("perplexed",1,Eyes="psychic")
                    $ BetsyX.Statup("Love", 200, 1)
                    $ BetsyX.Statup("Inbt", 200, 2)
                    if not Player.Male:
                        ch_b "Я не знаю Чарльза, она мне кажется довольно. . . заурядным человеком."
                    else:
                        ch_b "Я не знаю Чарльза, он мне кажется довольно. . . заурядным человеком."
                    $ BetsyX.FaceChange("sly",1,Brows="angry")
                    $ BetsyX.Statup("Love", 200, 1)
                    $ BetsyX.Statup("Inbt", 200, 3)
                    if not Player.Male:
                        ch_x "Похоже, что наша мисс [Player.Name] просто играет с вами."
                        ch_x "Уверяю вас, если она захочет, она без проблем отразит вторжение в свою голову."
                    else:
                        ch_x "Похоже, что наш мистер [Player.Name] просто играет с вами."
                        ch_x "Уверяю вас, если он захочет, он без проблем отразит вторжение в свою голову."
        $ BetsyX.FaceChange("smile",Brows = "surprised")
        ch_b "Боже, это действительно интересная способность."
        $ BetsyX.FaceChange("sly")
        $ BetsyX.ArmPose = 2
        $ BetsyX.Knife = 1
        ch_b "Я просто -обязана- воспользоваться своим ножом."
        ch_x "Возможно, позже, дорогая."
        $ BetsyX.FaceChange("sadside",2)
        ch_b "Ах. . . да. . .  конечно."
        $ BetsyX.Knife = 0
        $ BetsyX.FaceChange("sly",1)
        ch_b "Я буду присматривать за тобой."
        if "powers" not in BetsyX.History:
                if not Player.Male:
                    ch_x "Мисс Брэддок тоже телепат, если ты еще не заметила. . ."
                else:
                    ch_x "Мисс Брэддок тоже телепат, если ты еще не заметил. . ."
                $ BetsyX.History.append("powers")
        ch_x "В общем, [Player.Name], ты можешь идти. Нам с мисс Брэддок нужно еще многое обсудить."
        menu:
            extend""
            "Пока.":
                $ BetsyX.FaceChange("smile")
                $ BetsyX.Statup("Love", 200, 5)
            "Ладно.":
                $ BetsyX.FaceChange("confused")
                $ BetsyX.Statup("Love", 200, -1)
            "Я останусь.":
                $ BetsyX.FaceChange("smile")
                $ BetsyX.Statup("Love", 200, 1)
                $ BetsyX.Statup("Obed", 200, 3)
                $ BetsyX.Statup("Inbt", 200, 2)
                ch_x "Боюсь, я вынужден настаивать."
                "Пока профессор вас выводит, [BetsyX.Name] бросает вам в спину. . ."
            ". . .":
                $ BetsyX.FaceChange("sad")
                $ BetsyX.Statup("Love", 200, -2)
        ch_b "До скорых встреч. . ."
        "Вы возвращаетесь в свою комнату."
        if "Betsy" not in GwenX.History:
                $ GwenX.History.append("Betsy")
        $ bg_current = "bg player"
        jump Misplaced

label AboutBetsy:
        #called from various intros
        while True:
            menu:
                extend ""
                "Ты кто?" if "Elizabeth" not in BetsyX.Names:
                        $ BetsyX.FaceChange("smile",2,Mouth="open",Brows="surprised")
                        ch_b "Ох, прости мои манеры. . ."
                        $ BetsyX.FaceChange("smile",1)
                        ch_b "Я Элизабет Брэддок, рада познакомиться с тобой."
                        $ BetsyX.Name = "Элизабет"
                        $ BetsyX.Name_rod = "Элизабет"
                        $ BetsyX.Name_dat = "Элизабет"
                        $ BetsyX.Name_vin = "Элизабет"
                        $ BetsyX.Name_tvo = "Элизабет"
                        $ BetsyX.Name_pre = "Элизабет"
                        $ BetsyX.Names.append("Elizabeth")
                        ch_b "Однако, я предпочитаю, чтобы меня звали \"Бетси\"."
                        $ BetsyX.Name = "Бетси"
                        $ BetsyX.Name_rod = "Бетси"
                        $ BetsyX.Name_dat = "Бетси"
                        $ BetsyX.Name_vin = "Бетси"
                        $ BetsyX.Name_tvo = "Бетси"
                        $ BetsyX.Name_pre = "Бетси"
                        menu:
                            ch_b "Однако, я предпочитаю, чтобы меня звали \"Бетси\"."
                            "Приятно познакомиться.":
                                    $ BetsyX.Statup("Love", 200, 3)
                                    ch_b "Я просто очарована."
                            "Очень приятно познакомиться с тобой.":
                                    $ BetsyX.FaceChange("sly",1)
                                    $ BetsyX.Statup("Love", 200, 3)
                                    $ BetsyX.Statup("Obed", 200, 2)
                                    if not Player.Male:
                                        ch_b "Ох, какая леди. . ."
                                    else:
                                        ch_b "Ох, какой джентльмен. . ."
                            "Ладно.":
                                    $ BetsyX.FaceChange("perplexed")
                                    $ BetsyX.Statup("Love", 200, -2)
                                    $ BetsyX.Statup("Obed", 200, 2)
                                    $ BetsyX.Statup("Inbt", 200, 1)
                                    ch_b "Да. . . я прямо очарована. . ."
                        menu:
                            extend ""
                            "\"Бетси\" - прекрасное имя.":
                                    $ BetsyX.FaceChange("smile",0)
                                    $ BetsyX.Statup("Love", 200, 4)
                                    $ BetsyX.Statup("Inbt", 200, 1)
                                    ch_b "Благодарю, мне и самой оно нравится."
                            "Мне больше нравится имя \"Элизабет\".":
                                    $ BetsyX.FaceChange("smile",0,Brows="surprised")
                                    $ BetsyX.Statup("Love", 200, 2)
                                    $ BetsyX.Statup("Obed", 200, 3)
                                    ch_b "Ох. Тогда, пожалуй, ты можешь звать меня так."
                                    $ BetsyX.Name = "Элизабет"
                                    $ BetsyX.Name_rod = "Элизабет"
                                    $ BetsyX.Name_dat = "Элизабет"
                                    $ BetsyX.Name_vin = "Элизабет"
                                    $ BetsyX.Name_tvo = "Элизабет"
                                    $ BetsyX.Name_pre = "Элизабет"
                            ". . .":
                                    pass
                        $ BetsyX.FaceChange("smile",0)

                "Почему ты говоришь как Мэри Поппинс?" if "british" not in BetsyX.RecentActions:
                        $ BetsyX.Statup("Love", 200, -2)
                        $ BetsyX.Statup("Inbt", 200, 1)
                        $ BetsyX.FaceChange("surprised",2)
                        ch_b "! ! !"
                        $ BetsyX.FaceChange("sly",1)
                        ch_b "Наверное, потому, что я практически идеальна во всех отношениях."
                        menu:
                            "Ха.":
                                    $ BetsyX.Statup("Love", 200, 4)
                                    $ BetsyX.Statup("Inbt", 200, 2)
                                    $ BetsyX.FaceChange("smile",1)
                            ". . .":
                                    $ BetsyX.Statup("Love", 200, -1)
                                    $ BetsyX.Statup("Obed", 200, 5)
                                    $ BetsyX.Statup("Inbt", 200, -2)
                                    $ BetsyX.FaceChange("smile",2,Brows="sad")
                                    ch_b ". . . эм, я пошутила."
                                    $ BetsyX.FaceChange("sadside",2,Mouth="smile")
                                    ch_b "Или, что вероятнее всего, попыталась пошутить. . ."
                        ch_b "Я. . . Британка, если это было непонятно."
                        $ BetsyX.FaceChange("smile",1)
                        $ BetsyX.RecentActions.append("british")
                        $ BetsyX.RecentActions.append("cockney")
                        $ BetsyX.RecentActions.append("cockney")
                "Откуда ты?" if "british" not in BetsyX.RecentActions:
                        $ BetsyX.FaceChange("smile")
                        ch_b "О, я родилась в Эссексе. Училась в Уайкомбе."
                        menu:
                            "О, ты еще поди из аристократических кругов?":
                                    $ BetsyX.FaceChange("sly")
                                    $ BetsyX.Statup("Love", 200, 2)
                                    $ BetsyX.Statup("Obed", 200, 1)
                                    ch_b "Увы, можно и так сказать."
                            "О, значит ты из Англии.":
                                    $ BetsyX.Statup("Love", 200, 3)
                                    ch_b "Безусловно."
                            "Я не знаю, что означают эти слова.":
                                    $ BetsyX.FaceChange("sly",1,Brows="sad",Eyes="side")
                                    $ BetsyX.Statup("Love", 200, -2)
                                    $ BetsyX.Statup("Inbt", 200, 3)
                                    ch_b "Ах. . . Американцы. . ."
                                    $ BetsyX.FaceChange("sly",0)
                                    ch_b "Я из -Британии-, дорогуша."
                            "Эссекси. . .":
                                    $ BetsyX.FaceChange("sly",1,Brows="confused")
                                    $ BetsyX.Statup("Love", 200, -1)
                                    $ BetsyX.Statup("Obed", 200, 2)
                                    $ BetsyX.Statup("Inbt", 200, 3)
                                    ch_b "Как смешно."
                                    $ BetsyX.FaceChange("sly",0)
                                    ch_b "Я британка, дорогуша."
                        $ BetsyX.RecentActions.append("cockney")
                        $ BetsyX.RecentActions.append("cockney")
                        $ BetsyX.RecentActions.append("british")
                "М? *спародировать ее акцент [[Непереводимая игра слов]*!" if "cockney" in BetsyX.RecentActions:
                        $ BetsyX.RecentActions.remove("cockney")
                        $ BetsyX.FaceChange("surprised",2)
                        $ BetsyX.Statup("Love", 200, -10)
                        $ BetsyX.Statup("Inbt", 200, 3)
                        ch_b ". . ."
                        $ BetsyX.FaceChange("angry",1)
                        ch_b "Нет. Только не это."
                        ch_b "Опять."
                        menu:
                            extend ""
                            "Извини. . .":
                                    $ BetsyX.Statup("Love", 200, 5)
                                    $ BetsyX.Statup("Inbt", 200, 2)
                                    $ BetsyX.FaceChange("normal",0)
                                    ch_b "Я буду. . . работать над собой. . ."
                            "Ох, ладно.":
                                    $ BetsyX.Statup("Love", 200, -2)
                                    $ BetsyX.Statup("Obed", 200, 2)
                                    $ BetsyX.FaceChange("perplexed",1)
                                    ch_b "Прошу. . . не надо снова так делать."
                                    $ BetsyX.FaceChange("normal",0)
                            "*спародировать ее акцент снова [[Непереводимая игра слов]*!":
                                    $ BetsyX.Statup("Love", 200, -10)
                                    $ BetsyX.Statup("Obed", 200, 5)
                                    $ BetsyX.FaceChange("sadside",0)
                                    ch_b "Боюсь, мне, возможно, придется покинуть эту страну."

                "Так что у тебя?" if "powers" not in BetsyX.History:
                        $ BetsyX.FaceChange("smile",Brows="confused")
                        ch_b "Что \"что у меня\"?"
                        menu:
                            extend ""
                            "Какие у тебя способности?":
                                    pass
                            "Ну, что в тебе мутанского?":
                                    $ BetsyX.Statup("Love", 200, -1)
                            "А, неважно.":
                                    $ BetsyX.FaceChange("sly",0)
                                    if not Player.Male:
                                        ch_b "О, ты, должно быть, имела в виду мои способности мутанта. . ."
                                    else:
                                        ch_b "О, ты, должно быть, имел в виду мои способности мутанта. . ."
                        call BetsyPowers
                "Хорошо, пойдем." if "luggage" not in BetsyX.History:
                        ch_b "Ох, хорошо."
                        $ BetsyX.FaceChange("smile",0)
                        if "Elizabeth" not in BetsyX.Names:
                                ch_b "К слову, меня зовут Бетси."
                                $ BetsyX.Name = "Бетси"
                                $ BetsyX.Name_rod = "Бетси"
                                $ BetsyX.Name_dat = "Бетси"
                                $ BetsyX.Name_vin = "Бетси"
                                $ BetsyX.Name_tvo = "Бетси"
                                $ BetsyX.Name_pre = "Бетси"
                                ch_b "На самом деле Элизабет. . ."
                                ch_b "Но я предпочитаю, чтобы меня звали Бетси."
                                $ BetsyX.Names.append("Elizabeth")
                        ch_b "Веди."
                        return
                "Что ж, приятно познакомиться." if "luggage" in BetsyX.History:
                        $ BetsyX.DrainWord("luggage",0,0,0,1)      #removes from history
                        ch_b "Ох."
                        $ BetsyX.FaceChange("smile",0)
                        if "Elizabeth" not in BetsyX.Names:
                                ch_b "К слову, меня зовут Бетси."
                                $ BetsyX.Name = "Бетси"
                                $ BetsyX.Name_rod = "Бетси"
                                $ BetsyX.Name_dat = "Бетси"
                                $ BetsyX.Name_vin = "Бетси"
                                $ BetsyX.Name_tvo = "Бетси"
                                $ BetsyX.Name_pre = "Бетси"
                                ch_b "На самом деле, Элизабет. . ."
                                ch_b "Но я предпочитаю, чтобы меня звали Бетси."
                                $ BetsyX.Names.append("Elizabeth")
                        ch_b "Прошу, проводи меня к профессору."
                        return
            if "cockney" in BetsyX.RecentActions:
                    $ BetsyX.RecentActions.remove("cockney")
        #end white loop

label BetsyPowers:
        #called when asked about her powers.
        $ BetsyX.FaceChange("smile",1)
        ch_b "Пожалуй, я. . . кто-то вроде телепата."
        menu:
            extend ""
            "О, здорово.":
                    $ BetsyX.Statup("Love", 200, 1)
                    $ BetsyX.FaceChange("smile",0)
            "Еще один телепат?":
                    $ BetsyX.Statup("Love", 200, -1)
                    $ BetsyX.Statup("Obed", 200, 1)
                    $ BetsyX.FaceChange("sly",1,Brows="angry")
            "О, это -такая- редкая способность.":
                    $ BetsyX.Statup("Love", 200, -2)
                    $ BetsyX.Statup("Obed", 200, 4)
                    $ BetsyX.Statup("Inbt", 200, -1)
                    $ BetsyX.FaceChange("angry",2)
        ch_b "Да-да, я знаю, что мы далеко не вымирающий вид. . ."
        $ BetsyX.FaceChange("sly",0)
        $ BetsyX.Knife = 1
        ch_b "Тем не менее, я считаю, что мои способности весьма оригинальны. . ."
        $ BetsyX.Knife = 0
        $ BetsyX.History.append("powers")
        #knife out
        return


label BetsyMeet2:
        #called if "luggage" in BetsyX.History and BetsyX.Event[2] < 1
        $ BetsyX.FaceChange("smile")
        ch_b "Ох, думаю, мы не представлены. . ."
        call AboutBetsy
        $ BetsyX.FaceChange("smile")
        ch_b "Я знаю, что тебя зовут [Player.Name], если верить слухам."
        $ BetsyX.History.append("met")
        $ ActiveGirls.append(BetsyX) if BetsyX not in ActiveGirls else ActiveGirls
        $ BetsyX.Event[2] = 0
        if "Betsy" not in GwenX.History:
                $ GwenX.History.append("Betsy")
        menu:
            extend ""
            "Ага, приятно познакомиться.":
                    $ BetsyX.Statup("Love", 200, 5)
                    ch_b "И мне."
            "Агась.":
                    $ BetsyX.FaceChange("smile",Brows="confused")
                    $ BetsyX.Statup("Love", 200, 2)
                    $ BetsyX.Statup("Obed", 200, 2)
                    ch_b "Конечно. . ."
                    $ BetsyX.FaceChange("smile")
            "И -что же- ты слышала обо мне?":
                    $ BetsyX.FaceChange("sly",2)
                    $ BetsyX.Statup("Love", 200, 2)
                    $ BetsyX.Statup("Obed", 200, 3)
                    $ BetsyX.Statup("Inbt", 200, 1)
                    ch_b "Я бы сказала \"много хорошего,\" . ."
                    $ BetsyX.FaceChange("smile",1)
                    ch_b "Но. . . давай отложим этот разговор на потом."
        if len(Present) > 1 and Nearby < 3:
            $ BetsyX.Loc = "nearby"
            $ Nearby.append(BetsyX)
        call Class_Nearby(0)
        return
# End Betsy intro content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
## end BetsyMeet//////////////////////////////////////////////////////////


label Betsy_Key:
        call Shift_Focus(BetsyX)
        $ BetsyX.Loc = bg_current
        call Set_The_Scene
        $ BetsyX.FaceChange("bemused")
        $ Event_Queue = [0,0]
        ch_b "Ох, пожалуй, раз уж ты так часто заходишь ко мне. . ."
        ch_b "-возьми. . ."
        "Она вручает вам ключ с маленьким брелоком в виде бабочки."
        $ Keys.append(BetsyX) if BetsyX not in Keys else Keys
        $ BetsyX.Event[0] = 1
        ch_p "Спасибо."
        return


label Betsy_BF(BO=[]):
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(BetsyX,"bemused","покраснела. . .")
                return
        call Shift_Focus(BetsyX)
        if BetsyX.Loc != bg_current:
            $ BetsyX.Loc = bg_current
            if BetsyX not in Party:
                "[BetsyX.Name] подходит к вам и изъявляет желание поговорить с вами наедине."
            else:
                "[BetsyX.Name] поворачивается к вам и показывает жестом, что хочет поговорить с вами наедине."
        $ Event_Queue = [0,0]
        $ BetsyX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene(0)
        call Display_Girl(BetsyX)
        $ BetsyX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in BetsyX.History:
                call expression BetsyX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        call CleartheRoom(BetsyX)
        $ BetsyX.FaceChange("normal",1)
        if "asked boyfriend" not in BetsyX.DailyActions:
                ch_b "Ох, [BetsyX.Petname]. У тебя есть минутка?"
                $ BetsyX.FaceChange("smile",1)
                if not Player.Male:
                    ch_b "Я просто хотела бы поблагодарить тебя за то, что ты помогла мне здесь освоиться."
                else:
                    ch_b "Я просто хотела бы поблагодарить тебя за то, что ты помог мне здесь освоиться."
        else:
                if not Player.Male:
                    ch_b "Понимаешь, сперва я хотела просто поблагодарить тебя за то, что ты помогла мне здесь устроиться."
                else:
                    ch_b "Понимаешь, сперва я хотела просто поблагодарить тебя за то, что ты помог мне здесь устроиться."
        if not Player.Male:
            ch_b "Я прибыла издалека, как же приятно, что в новом месте я нашла подругу."
        else:
            ch_b "Я прибыла издалека, как же приятно, что в новом месте я нашла друга."
        $ BetsyX.FaceChange("bemused",1,Eyes="side")
        ch_b "Порой сложно дается смена обстановки."
        $ BetsyX.FaceChange("sadside",1,Mouth="normal")
        ch_b "Когда я перешла в государственную школу, выяснилось, что новеньких там не особо любят."
        $ BetsyX.FaceChange("sadside",1)
        ch_b "Особенно если они. . . отличаются от других."
        menu:
            extend ""
            "Ты имеешь в виду фиолетовые волосы?":
                    $ BetsyX.FaceChange("surprised",1)
                    ch_b "М? Нет, я. . . честно говоря, я раньше красила волосы в черный. . ."
                    ch_b "Но потом оказалось, что фиолетовый цвет популярен среди молодежи."
            "Что ты имеешь в виду?":
                    $ BetsyX.Statup("Love", 90, 1)
                    $ BetsyX.Statup("Inbt", 50, 2)
            "Потому что ты мутант?":
                    $ BetsyX.FaceChange("normal",1)
                    $ BetsyX.Statup("Obed", 70, 1)
                    ch_b "Ну, тогда про мутантов еще не особо знали."
                    ch_b "Если не считать моих волос, по мне и не скажешь, что я мутант."
            "Это из-за твоей. . .":
                    ch_b "Да, из-за моей внешности."
            ". . .":
                    pass
        $ BetsyX.FaceChange("sadside",1,Mouth="normal")
        ch_b ". . . У меня не совсем. . . хорошие манеры."
        ch_b "По крайней мере, по их \"стандартам.\""
        $ BetsyX.FaceChange("sadside",1,Mouth="smirk")
        ch_b "Я не соответствовала образу \"настоящей британской леди.\""
        ch_b "И мои одноклассники, конечно, дали мне это ясно понять."
        menu:
            extend ""
            "Какой ужас.":
                    $ BetsyX.Statup("Love", 90, 3)
                    ch_b "О да, это было ужасно неприятно."
            "Ага, представляю.":
                    $ BetsyX.FaceChange("confused",1)
                    $ BetsyX.Statup("Love", 90, -1)
                    $ BetsyX.Statup("Obed", 80, 2)
                    ch_b "Эм. . . верю."
            "Ну, в этом есть смысл.":
                    $ BetsyX.FaceChange("confused",1)
                    $ BetsyX.Statup("Love", 90, -3)
                    $ BetsyX.Statup("Obed", 80, 3)
                    ch_b ". . . Возможно."
            "Расизм так же отвратителен, как и чертовы наркотики.":
                    $ BetsyX.FaceChange("sly",1)
                    $ BetsyX.Statup("Love", 90, 4)
                    $ BetsyX.Statup("Inbt", 50, 2)
                    ch_b "Хехе, какой интересный взгляд на происходящее."
            ". . .":
                    pass
        $ BetsyX.FaceChange("sadside",1,Mouth="normal")
        ch_b "Видишь ли, мой отец был дворянином, \"Лордом Брэддоком\". . ."
        ch_b "-Мама-, напротив, была японкой, смотрительницей музея, с которой он познакомился во время своих путешествий."
        $ BetsyX.FaceChange("sadside",1,Mouth="smile")
        ch_b "Они, конечно же, безумно влюбились друг в друга и наплевали на все приличия."
        ch_b "Мой брат невероятно похож на нашего отца, но я явно больше похожа на маму."
        $ BetsyX.FaceChange("sadside",1)
        ch_b "В детстве я почти не замечала этого, но в школе мне открыли глаза."
        menu:
            extend ""
            "Мне жаль это слышать.":
                    $ BetsyX.FaceChange("sad",1,Mouth="smile")
                    $ BetsyX.Statup("Love", 90, 2)
                    ch_b "Это очень мило с твоей стороны. . ."
            "Я рада, что ты мне открылась." if not Player.Male:
                    $ BetsyX.FaceChange("sad",1,Mouth="normal")
                    $ BetsyX.Statup("Love", 90, 3)
                    $ BetsyX.Statup("Inbt", 50, 2)
                    ch_b "Ты до сих пор была так добра ко мне."
            "Я рад, что ты мне открылась." if Player.Male:
                    $ BetsyX.FaceChange("sad",1,Mouth="normal")
                    $ BetsyX.Statup("Love", 90, 3)
                    $ BetsyX.Statup("Inbt", 50, 2)
                    ch_b "Ты до сих пор был так добр ко мне."
            "Ясно. . .":
                    $ BetsyX.FaceChange("confused",1,Mouth="normal")
                    $ BetsyX.Statup("Love", 90, -4)
                    $ BetsyX.Statup("Obed", 80, 3)
                    $ BetsyX.Statup("Inbt", 70, -2)
                    ch_b "Прошу прощения, если моя детская травма тебе наскучила."
                    menu:
                        extend ""
                        "Извини, это было грубо." :
                                $ BetsyX.FaceChange("sad",1,Mouth="normal")
                                $ BetsyX.Statup("Love", 90, 2)
                                $ BetsyX.Statup("Obed", 60, -1)
                                ch_b "Хорошо, я принимаю твои извинения. . ."
                        "Я в порядке, не волнуйся.":
                                $ BetsyX.FaceChange("angry",1)
                                $ BetsyX.Statup("Love", 90, -2)
                                $ BetsyX.Statup("Obed", 80, 5)
                                ch_b "Возможно, я неправильно истолковала свои чувства."
                                "[BetsyX.Name] уходит в подавленном состоянии."
                                $ BetsyX.Event[5] = 20
                                call Remove_Girl(BetsyX)
                                $ Line = 0
                                return
                        ". . .":
                                $ BetsyX.Statup("Love", 90, -1)
                                ch_b ". . ."
                    $ BetsyX.FaceChange("sad",1,Mouth="normal")
            "Ха!":
                    $ BetsyX.FaceChange("confused",2)
                    $ BetsyX.Statup("Love", 90, -5)
                    $ BetsyX.Statup("Obed", 200, 2)
                    $ BetsyX.Statup("Inbt", 50, -3)
                    ch_b "Что?!"
                    $ BetsyX.FaceChange("angry",1)
                    ch_b "Возможно, я неправильно истолковала свои чувства."
                    "[BetsyX.Name] уходит в подавленном состоянии."
                    $ BetsyX.Event[5] = 20
                    call Remove_Girl(BetsyX)
                    $ Line = 0
                    return
            ". . .":
                    pass
        $ BetsyX.FaceChange("sadside",1,Mouth="normal")
        ch_b "В общем, приятно начать все сначала в более гостеприимном месте."
        $ BetsyX.FaceChange("smile",1)
        if not Player.Male:
            ch_b "И ты сыграла в этом большую роль."
        else:
            ch_b "И ты сыграл в этом большую роль."

        if BetsyX in Player.Harem:
                #if she somehow already ended up in the harem
                ch_b "На этом все."
                if "BetsyYes" in Player.Traits:
                        $ Player.Traits.remove("BetsyYes")
                if "boyfriend" not in BetsyX.Petnames:
                        $ BetsyX.Petnames.append("boyfriend")
                return

        if not Player.Male:
            ch_b "Если позволишь, я хотела бы узнать, не рассматривала ли ты возможность стать. . ."
        else:
            ch_b "Если позволишь, я хотела бы узнать, не рассматривал ли ты возможность стать. . ."
        $ BetsyX.FaceChange("sly",2)
        ch_b "Ближе?"
#        if len(Player.Harem) > 1:
#                ch_b "Would there perhaps be room for one more in your little. . . fiefdom?"
#        elif Player.Harem:
#                ch_b "Do you think perhaps [Player.Harem[0].Name] would be willing to share?"
#                ch_b "Might I be your girlfriend as well?"
#        else:
        ch_b "Может, я могу стать твоей девушкой?"
        $ BetsyX.Event[5] += 1
        $ Line = "start"
        while Line != "yes":
            menu:
                extend ""
                "Конечно." if Line != "maybe":
                        $ BetsyX.FaceChange("smile",1)
                        $ BetsyX.Statup("Love", 200, 6)
                        $ BetsyX.Statup("Obed", 80, 2)
                        ch_b "Ох, чудесно!"
                        $ Line = "yes"
                "Ну ладно." if Line == "maybe":
                        $ BetsyX.FaceChange("normal",1)
                        $ BetsyX.Statup("Love", 200, 4)
                        $ BetsyX.Statup("Obed", 80, 2)
                        $ BetsyX.Statup("Inbt", 60, 1)
                        $ BetsyX.Statup("Inbt", 80, 2)
                        ch_b "Эм. . . чудесно!"
                        $ Line = "yes"

                "Мне это не особо интересно." if Line != "maybe":
                        $ BetsyX.FaceChange("sad",1)
                        $ BetsyX.Statup("Love", 200, -3)
                        $ BetsyX.Statup("Obed", 80, 3)
                        if not Player.Male:
                            ch_b "Ах. . . ты уверена?"
                        else:
                            ch_b "Ах. . . ты уверен?"
                        $ Line = "maybe"
                "Мне это -совсем- интересно." if Line == "maybe":
                        $ BetsyX.FaceChange("sad",1)
                        $ BetsyX.Statup("Love", 200, -5)
                        $ BetsyX.Statup("Obed", 60, 1)
                        $ BetsyX.Statup("Obed", 80, 3)
                        ch_b "Ах. . . понятно."
                        $ Line = "no"

                "Нет, не думаю, что [Player.Harem[0].Name] это поймет." if len(Player.Harem) == 1:
                        $ BetsyX.Statup("Love", 200, -15)
                        $ BetsyX.Statup("Obed", 80, 7)
                        $ BetsyX.FaceChange("sadside",1)
                        $ BetsyX.GLG(Player.Harem[0],800,-10,1)
                        ch_b "Ах, понятно."
                        $ Line = "no"
                "Другим девушкам это не понравится." if len(Player.Harem) > 1:
                        $ BetsyX.Statup("Love", 200, -15)
                        $ BetsyX.Statup("Obed", 80, 7)
                        $ BetsyX.FaceChange("sad",1)
                        call HaremStatup(BetsyX,700,-10) #lowers like of all Harem girls by 10
                        ch_b "Ах, понятно."
                        $ Line = "no"

            if Player.Harem and Line == "yes":
                #if you agreed, but have other girls. . .
                if not ApprovalCheck(BetsyX, 1400):
                    $ BetsyX.FaceChange("sadside",1)
                    if not Player.Male:
                        ch_b "Хотя на данный момент я не думаю, что смогу быть с тобой, пока ты занята кем-то другим. . ."
                    else:
                        ch_b "Хотя на данный момент я не думаю, что смогу быть с тобой, пока ты занят кем-то другим. . ."
                    $ Line = "no"
                else:
                    if len(Player.Harem) >= 2:
                        ch_b "Другие девушки это примут, верно?"
                    else:
                        ch_b "[Player.Harem[0].Name] это примет, верно?"
                    menu:
                        extend ""
                        "Все хорошо, всех все устраивает." if "BetsyYes" in Player.Traits:
                                $ BetsyX.Statup("Love", 200, 5)
                                $ BetsyX.Statup("Obed", 80, 10)
                                $ BetsyX.Statup("Inbt", 80, 5)
                                $ BetsyX.FaceChange("surprised",1)
                                ch_b "Чудесно!"
                        "Нууу. . . это сперва еще нужно выяснить." if "BetsyYes" not in Player.Traits:
                                $ BetsyX.Statup("Love", 200, 3)
                                $ BetsyX.Statup("Obed", 80, 3)
                                $ BetsyX.Statup("Inbt", 80, 1)
                                $ BetsyX.Statup("Lust", 80, 1)
                                $ BetsyX.FaceChange("confused",1)
                                ch_b "Ах. . . Пожалуй, тогда нам придется вернуться к этому вопросу позже. . ."
                                $ BetsyX.Event[5] = 20
                                call Remove_Girl(BetsyX)
                                $ Line = 0
                                return
                    call HaremStatup(BetsyX,900,20) #raises like of all Harem girls by 20

            if Line == "no":
                    $ BetsyX.FaceChange("sadside",1)
                    ch_b ". . . Пожалкй, мы оставим все как есть."
                    ch_b "По крайней мере, пока."
                    "[BetsyX.Name] уходит в подавленном состоянии."
                    $ BetsyX.Event[5] = 20
                    call Remove_Girl(BetsyX)
                    $ Line = 0
                    return
            # end menu

        if "Historia" not in Player.Traits:
            $ Player.Harem.append(BetsyX)
            if "BetsyYes" in Player.Traits:
                    $ Player.Traits.remove("BetsyYes")
            $ BetsyX.Petnames.append("boyfriend")
            call Harem_Initiation
        $ BetsyX.Statup("Love", 200, 3)
        $ BetsyX.Statup("Obed", 80, 3)
        $ BetsyX.Statup("Inbt", 80, 1)
        $ BetsyX.Statup("Lust", 80, 1)
        $ BetsyX.FaceChange("sly",1)
        ch_b "В таком случае, пожалуй, мне следует тебя как-нибудь отблагодарить. . ."
        if "Historia" in Player.Traits:
                return 1
        $ Tempmod = 10
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        $ Tempmod = 0
        return


## start Betsy_Love//////////////////////////////////////////////////////////
label Betsy_Love(Shipping=[],Shipshape=0,Topics=[],BO=[]):
        # SHipping is used to track who else you're involved with
        # if BetsyX.Event[6] = 5, then it cleared
        # if BetsyX.Event[6] = 20, then it broke because you didn't love her
        # if BetsyX.Event[6] = 25, then it broke and you already went through the redux

        $ BetsyX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ BO = TotalGirls[:]
        $ BO.remove(BetsyX)
        while BO:
            if ApprovalCheck(BO[0], 1200, "LO"):
                    $ Shipping.append(BO[0])
            $ BO.remove(BO[0])
        $ Shipshape = len(Shipping)

        $ BetsyX.FaceChange("sad",1,Mouth="normal")
        if BetsyX.Loc == bg_current or BetsyX in Party:
                "[BetsyX.Name] бросает на вас обеспокоенный взгляд."
        else:
                "[BetsyX.Name] выходит из-за угла и замечает вас."
        if bg_current != "bg betsy" and bg_current != "bg player":
                "Она просит вас проследовать за ней в ее комнату и, похоже, ответ \"нет\" не принимается."
                $ bg_current = "bg betsy"
        $ Event_Queue = [0,0]
        $ BetsyX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(BetsyX)
        call Set_The_Scene
        call Taboo_Level
        call Shift_Focus(BetsyX)
        $ BetsyX.DailyActions.append("relationship")
        $ BetsyX.FaceChange("sad",1,Mouth="normal")
        ch_b "Я давно хотела с тобой поговорить. . ."
        ch_b "-о нас. . ."
        ch_b "Насколько я понимаю, в этом институте много телепатов."
        if EmmaX in Player.Harem or JeanX in Player.Harem:
                $ BetsyX.FaceChange("sly",1)
                if not Player.Male:
                    ch_b "С некоторыми из них ты даже сблизилась. . ."
                else:
                    ch_b "С некоторыми из них ты даже сблизился. . ."
        $ BetsyX.FaceChange("sad",1,Mouth="normal")
        ch_b "Как бы то ни было, я часто рассматривала свой собственный \"дар\" больше как бремя, чем что-либо еще."
        ch_b "Как я уже говорила, я проходила обучение в довольно враждебной среде."
        ch_b "Все стало только хуже, когда проявилась моя телепатия."
        $ BetsyX.FaceChange("sadside",1,Mouth="normal")
        ch_b "Я могла \"слышать\" не только то, что они говорили мне в лицо, но и то, что они думали обо мне."
        ch_b "И как только это началось, я изо всех сил старалась подавлять ее."
        $ BetsyX.FaceChange("sadside",1,Mouth="smirk")
        ch_b "Но только когда Чарльз нашел меня и научил сдерживать свои способности, я обрела хоть какую-то степень контроля."
        $ BetsyX.FaceChange("normal",1)
        ch_b "С тех пор я выгляжу холодной, можно сказать, что я выставила вокруг себя эмоциональный барьер. "
        ch_b "Когда мы с тобой стали ближе. . ."
        ch_b ". . .Я начала задумываться, стоит ли впустить тебя внутрь. . . и я решилась. . ."
        menu:
            extend ""
            "Мне очень приятно это слышать.":
                    $ BetsyX.FaceChange("normal",1)
                    $ BetsyX.Statup("Love", 200, 3)
                    $ BetsyX.Statup("Inbt", 70, 2)
            "Что ты имеешь в виду?":
                    $ BetsyX.Statup("Love", 200, -1)
            "Я уже была внутри тебя." if (BetsyX.Sex or BetsyX.Anal) and not Player.Male:
                    $ BetsyX.FaceChange("sly",2)
                    $ BetsyX.Statup("Obed", 200, 2)
                    $ BetsyX.Statup("Inbt", 50, 3)
                    $ BetsyX.Statup("Inbt", 80, 2)
                    ch_b "[BetsyX.Petname], я скорее. . ."
                    ch_b "Больше об. . . эмоциональной стороне."
            "Я уже был внутри тебя." if (BetsyX.Sex or BetsyX.Anal) and Player.Male:
                    $ BetsyX.FaceChange("sly",2)
                    $ BetsyX.Statup("Obed", 200, 2)
                    $ BetsyX.Statup("Inbt", 50, 3)
                    $ BetsyX.Statup("Inbt", 80, 2)
                    ch_b "[BetsyX.Petname], я скорее. . ."
                    ch_b "Больше об. . . эмоциональной стороне."
            "Я бы хотела войти в тебя." if (not BetsyX.Sex and not BetsyX.Anal) and not Player.Male:
                    $ BetsyX.FaceChange("sly",2)
                    $ BetsyX.Statup("Obed", 200, 2)
                    $ BetsyX.Statup("Inbt", 50, 3)
                    $ BetsyX.Statup("Inbt", 80, 2)
                    ch_b "[BetsyX.Petname], я скорее. . ."
                    ch_b "Больше об. . . эмоциональной стороне."
            "Я бы хотел войти в тебя." if (not BetsyX.Sex and not BetsyX.Anal) and Player.Male:
                    $ BetsyX.FaceChange("sly",2)
                    $ BetsyX.Statup("Obed", 200, 2)
                    $ BetsyX.Statup("Inbt", 50, 3)
                    $ BetsyX.Statup("Inbt", 80, 2)
                    ch_b "[BetsyX.Petname], я скорее. . ."
                    ch_b "Больше об. . . эмоциональной стороне."
            ". . .":
                    pass
        $ BetsyX.FaceChange("sad",2)
        ch_b "Я. . ."
        $ BetsyX.FaceChange("sad",2,Mouth="normal")
        ch_b "-люблю тебя."
        menu:
            extend ""
            "Я тоже тебя люблю!":
                $ BetsyX.FaceChange("smile",1)
                $ BetsyX.Statup("Love", 200, 20)
                $ BetsyX.Statup("Inbt", 90, 5)
                ch_b "Правда?!"
                ch_b "Это просто изумительно!"
                $ BetsyX.Petnames.append("lover")
                jump Betsy_Love_End
            "Я знаю.":
                $ BetsyX.FaceChange("confused",1,Mouth="smile")
                $ BetsyX.Statup("Love", 200, -5)
                $ BetsyX.Statup("Obed", 90, 5)
                $ BetsyX.Statup("Inbt", 90, 5)
                ch_b "Ох."
                $ BetsyX.Statup("Love", 200, 20)
                $ BetsyX.FaceChange("smile",1)
                ch_b "О! Я поняла!"
                $ BetsyX.Statup("Inbt", 90, 5)
                $ BetsyX.FaceChange("normal",2,Mouth="smirk")
                ch_b "\"Я знаю\", что ты тоже меня любишь!"
                $ BetsyX.FaceChange("normal",1,Mouth="smirk")
                $ BetsyX.Petnames.append("lover")
                jump Betsy_Love_End
            "Это здорово?":
                $ BetsyX.FaceChange("confused",1)
                $ BetsyX.Statup("Obed", 90, 5)
                if not Player.Male:
                    ch_b "Тебе. . . тебе нужно решить это самой, [BetsyX.Petname]."
                else:
                    ch_b "Тебе. . . тебе нужно решить это самому, [BetsyX.Petname]."
            "Хм.":
                $ BetsyX.FaceChange("confused",1)
                $ BetsyX.Statup("Love", 200, -5)
                $ BetsyX.Statup("Obed", 90, 10)
                ch_b "О боже, какое плохое начало."
        menu:
            extend ""
            "Ох, я тоже люблю тебя!":
                $ BetsyX.FaceChange("smile",1)
                $ BetsyX.Statup("Love", 200, 15)
                $ BetsyX.Statup("Obed", 90, 5)
                ch_b "Неужели? . . "
                $ BetsyX.FaceChange("sly",1)
                $ BetsyX.Statup("Inbt", 90, 5)
                ch_b "Я принимаю твои слова. . ."
                $ BetsyX.Petnames.append("lover")
                jump Betsy_Love_End
            "Я. . . тоже тебя люблю?":
                $ BetsyX.FaceChange("confused",1)
                $ BetsyX.Statup("Love", 200, 5)
                $ BetsyX.Statup("Obed", 90, 5)
                ch_b "Было так сложно сказать \"Я люблю тебя, [BetsyX.Name]!\"?"
                $ BetsyX.FaceChange("bemused",1)
                $ BetsyX.Petnames.append("lover")
                jump Betsy_Love_End
            "Ну, это все, конечно, круто и все такое. . .":
                $ BetsyX.FaceChange("sad",1)
                $ BetsyX.Statup("Love", 200, -5)
                $ BetsyX.Statup("Obed", 90, 10)
                $ BetsyX.Statup("Inbt", 90, -5)
                ch_b ". . . но. . . ты не разделяешь моих чувств. . ."
            "Теперь я чувствую себя. . . неуютно.":
                $ BetsyX.FaceChange("confused",1)
                $ BetsyX.Statup("Love", 200, -10)
                $ BetsyX.Statup("Obed", 90, 15)
                $ BetsyX.Statup("Inbt", 90, -5)
                ch_b "О боже. . ."
                $ BetsyX.FaceChange("sad",1)


        ch_b "Могу я узнать твои причины?"
        ch_b "Это из-за другой?"
        $ Line = 0
        menu:
                extend ""
                "Да, из-за другой." if Shipping and Shipshape < 3:
                    menu: #rkeljsvgb
                        "Из-за [RogueX.Name_pre]." if RogueX in Shipping:
                                $ Line = RogueX
                        "Из-за [KittyX.Name_pre]." if KittyX in Shipping:
                                $ Line = KittyX
                        "Из-за [EmmaX.Name_pre]." if EmmaX in Shipping:
                                $ Line = EmmaX
                        "Из-за [LauraX.Name_pre]." if LauraX in Shipping:
                                $ Line = LauraX
                        "Из-за [JeanX.Name_pre]." if JeanX in Shipping:
                                $ Line = JeanX
                        "Из-за [StormX.Name_pre]." if StormX in Shipping:
                                $ Line = StormX
                        "Из-за [JubesX.Name_pre]." if JubesX in Shipping:
                                $ Line = JubesX
                        "Из-за [GwenX.Name_pre]." if GwenX in Shipping:
                                $ Line = GwenX
                        "Из-за [DoreenX.Name_pre]." if DoreenX in Shipping:
                                $ Line = DoreenX
                        "Мне бы не хотелось произносить ее имя.":
                                $ BetsyX.Statup("Obed", 90, 15)
                                $ BetsyX.Statup("Inbt", 90, 5)
                                $ BetsyX.FaceChange("sadside",1)
                                ch_b "Пожалуй, это справедливо. . ."
                    if Line:
                        #If you called out a girl,
                        if BetsyX.GirlLikeCheck(Line) >= 800:
                            $ BetsyX.Statup("Love", 200, 5)
                            $ BetsyX.Statup("Obed", 90, 20)
                            $ BetsyX.Statup("Inbt", 90, 5)
                            $ BetsyX.FaceChange("sadside",1)
                            ch_b "Она. . . довольно милая. . ."
                        else:
                            $ BetsyX.FaceChange("angry",Eyes="side")
                            $ BetsyX.Statup("Love", 200, -5)
                            $ BetsyX.Statup("Obed", 90, 20)
                            ch_b "Ох, да, пожалуй, я понимаю. . ."
                            $ BetsyX.FaceChange("sadside",1)
                            $ BetsyX.GLG(Line,800,-50,1)

                "Да, из-за других" if Shipshape > 1:
                        $ BetsyX.Statup("Obed", 90, 15)
                        $ BetsyX.Statup("Inbt", 90, 5)
                        $ BetsyX.FaceChange("surprised",2)
                        ch_b "Ах. . . ."
                        $ BetsyX.FaceChange("sadside",1)
                        ch_b "Теперь все ясно. . ."
                "У меня никого нет.":
                        $ BetsyX.Statup("Love", 200, -15)
                        $ BetsyX.Statup("Obed", 90, 15)
                        $ BetsyX.Statup("Inbt", 90, 5)
                        $ BetsyX.FaceChange("sad",1)
                        ch_b "Я сильно в этом сомневаюсь."
                "Дело в \"тебе\".":
                        $ BetsyX.FaceChange("angry")
                        $ BetsyX.Statup("Love", 200, -25)
                        $ BetsyX.Statup("Obed", 90, 15)
                        ch_b "Что?!"
                        $ BetsyX.Statup("Love", 200, -10)
        $ BetsyX.FaceChange("sad",1)
        ch_b "Что ж, я должна с этим смириться. . ."
        if "sexfriend" in BetsyX.Petnames:
                $ BetsyX.FaceChange("sly",1)
                ch_b "Хотя мы можем продолжать поддерживать физическую близость. . ."
        elif "sir" in BetsyX.Petnames:
                $ BetsyX.FaceChange("sad",1,Mouth="normal")
                ch_b "Хотя мне по-прежнему нравятся наши. . . профессиональные отношения. . ."
        else:
                $ BetsyX.FaceChange("sad",1)
                ch_b "Пожалуй, мы можем остаться друзьями. . ."
                $ BetsyX.FaceChange("sadside",1,Mouth="smirk")
                ch_b "-или как там говорят. . ."
        menu:
            extend ""
            "Ага. . .":
                    $ BetsyX.FaceChange("sad",1)
                    ch_b "Да. . ."
            ". . .":
                    $ BetsyX.FaceChange("sad",1)
            "Может, когда-нибудь все и изменится":
                    ch_b "Да. . ."
                    $ BetsyX.FaceChange("sad",1)
            "Я тоже люблю тебя!":
                    $ BetsyX.FaceChange("sad",1)
                    ch_b "Понимаю-"
                    $ BetsyX.FaceChange("surprised",2,Mouth="open")
                    $ BetsyX.Statup("Love", 200, 10)
                    $ BetsyX.Statup("Obed", 90, 3)
                    ch_b ". . . Что?!"
                    menu:
                        extend ""
                        "Я сказала, \"Я тоже люблю тебя,\" [BetsyX.Name]!" if not Player.Male:
                                ch_b ". . . Пожалуй, я должна быть рада, что ты это сказала. . ."
                                ch_b "Но, боюсь, ты зашла в своей шутке слишком далеко."
                                ch_b "Ты очень сильно ранила меня, [Player.Name]."
                                menu:
                                    extend ""
                                    "Извини, мне нужно было время, чтобы все обдумать.":
                                            ch_b "Справедливо."
                                    "Извини.":
                                            ch_b "Пожалуй, я могу простить тебя."
                                    "Ага.":
                                            ch_b "Ясно. . ."
                                    ". . .":
                                            ch_b "Я не уверена, как к этому относиться. . ."
                                $ BetsyX.Statup("Love", 200, 10)
                                $ BetsyX.Statup("Obed", 90, 5)
                                ch_b "Я действительно люблю тебя, [BetsyX.Petname], и хочу быть с тобой."
                                ch_b "Но мне понадобится немного времени, чтобы прийти в себя. . ."
                                $ BetsyX.Petnames.append("lover")
                                $ BetsyX.Event[6] = 5
                                jump Misplaced

                        "Я сказал, \"Я тоже люблю тебя,\" [BetsyX.Name]!" if Player.Male:
                                ch_b ". . . Пожалуй, я должна быть рада, что ты это сказал. . ."
                                ch_b "Но, боюсь, ты зашёл в своей шутке слишком далеко."
                                ch_b "Ты очень сильно ранил меня, [Player.Name]."
                                menu:
                                    extend ""
                                    "Извини, мне нужно было время, чтобы все обдумать.":
                                            ch_b "Справедливо."
                                    "Извини.":
                                            ch_b "Пожалуй, я могу простить тебя."
                                    "Ага.":
                                            ch_b "Ясно. . ."
                                    ". . .":
                                            ch_b "Я не уверена, как к этому относиться. . ."
                                $ BetsyX.Statup("Love", 200, 10)
                                $ BetsyX.Statup("Obed", 90, 5)
                                ch_b "Я действительно люблю тебя, [BetsyX.Petname], и хочу быть с тобой."
                                ch_b "Но мне понадобится немного времени, чтобы прийти в себя. . ."
                                $ BetsyX.Petnames.append("lover")
                                $ BetsyX.Event[6] = 5
                                jump Misplaced

                        "Ох, не обращай внимание.":
                                $ BetsyX.FaceChange("angry",1)
                                $ BetsyX.Statup("Love", 200, -15)
                                $ BetsyX.Statup("Obed", 90, 10)
                                ch_b ". . ."
                                ch_b "У меня нет настроения играть в подобные игры. . ."
                                $ BetsyX.AddWord(1,0,0,0,"syke") #history
                                $ BetsyX.RecentActions.append("angry")
                                $ BetsyX.DailyActions.append("angry")

                        "Я сказала \"Я скоро уйду.\"" if not Player.Male:
                                $ BetsyX.FaceChange("angry",1)
                                $ BetsyX.Statup("Love", 200, -20)
                                $ BetsyX.Statup("Obed", 70, 5)
                                $ BetsyX.Statup("Obed", 95, 10)
                                ch_b ". . ."
                                ch_b "У меня нет настроения играть в подобные игры. . ."
                                $ BetsyX.AddWord(1,0,0,0,"syke") #history
                                $ BetsyX.RecentActions.append("angry")
                                $ BetsyX.DailyActions.append("angry")

                        "Я сказал \"Я скоро уйду.\"" if Player.Male:
                                $ BetsyX.FaceChange("angry",1)
                                $ BetsyX.Statup("Love", 200, -20)
                                $ BetsyX.Statup("Obed", 70, 5)
                                $ BetsyX.Statup("Obed", 95, 10)
                                ch_b ". . ."
                                ch_b "У меня нет настроения играть в подобные игры. . ."
                                $ BetsyX.AddWord(1,0,0,0,"syke") #history
                                $ BetsyX.RecentActions.append("angry")
                                $ BetsyX.DailyActions.append("angry")
        hide Betsy_Sprite with easeoutright
        call Remove_Girl(BetsyX)
        $ BetsyX.Loc = "hold" #puts her off the board for the day
        "Она уходит."
        $ BetsyX.Event[6] = 20
        $ Line = 0
        jump Misplaced
        return

label Betsy_Love_End:
        $ BetsyX.Event[6] = 5
        "[BetsyX.Name] заключает вас в крепкие объятия."
        $ BetsyX.Statup("Love", 200, 25)
        $ BetsyX.Statup("Lust", 90, 5)
        $ BetsyX.FaceChange("sly",1)
        if not Player.Male:
            ch_b "А теперь, раз уж ты впустила меня в свое сердце. . ."
        else:
            ch_b "А теперь, раз уж ты впустил меня в свое сердце. . ."
        $ BetsyX.Statup("Lust", 90, 10)

        if not BetsyX.Sex:
                $ BetsyX.FaceChange("bemused",2)
                ch_b "Думаю, возможно, я готова. . ."
        ch_b "Не желаешь взять меня?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Конечно же желаю. . . [[секс]":   #fix, unlock once sex becomes an option
                    $ BetsyX.Statup("Inbt", 30, 20)
                    $ BetsyX.Statup("Obed", 70, 10)
                    ch_b "Хмм. . ."
                    if Player.Male:
                            call SexAct("sex") # call Betsy_SexAct("sex")
                    else:
                            call SexAct("blow") # call Betsy_SexAct("blow")
                "У меня есть другая идея. . .[[выбрать другое занятие]":
                    $ BetsyX.Brows = "confused"
                    $ BetsyX.Statup("Obed", 70, 25)
                    ch_b "Например? . ."
                    $ Tempmod = 20
                    call SexMenu
        jump Misplaced

label Betsy_Love_Redux:
         #this is for if you rejected her but want a second chance
        $ Line = 0
        $ BetsyX.DailyActions.append("relationship")
        call Shift_Focus(BetsyX)

        if BetsyX.Event[6] >= 25:
                #if this is the second time through
                ch_p "Надеюсь, ты меня простила, я все еще люблю тебя."
                $ BetsyX.Statup("Love", 95, 10)
                if "syke" in BetsyX.History:
                    $ BetsyX.Statup("Love", 200, -5)
                if ApprovalCheck(BetsyX, 950, "L"):
                    $ Line = "love"
                else:
                    $ BetsyX.FaceChange("sad",1)
                    ch_b "Я. . . Я еще не готова тебя простить, [BetsyX.Petname]."
                    $ BetsyX.FaceChange("sadside",Mouth="lipbite")
                    ch_b ". . ."
                    ch_b "Однако я тебя выслушаю. . ."
        elif "syke" in BetsyX.History:
                    #you tried to trick her into thinking you'd said you loved her
                    if not Player.Male:
                        ch_p "Помнишь момент, я сказала тебе, что не люблю тебя?"
                    else:
                        ch_p "Помнишь момент, я сказал тебе, что не люблю тебя?"
                    $ BetsyX.FaceChange("angry",1)
                    $ BetsyX.Statup("Love", 200, -10)
                    ch_b "Что-то такое припоминаю. . ."
                    $ BetsyX.FaceChange("sadside",1)
                    ch_b "Что ты хочешь теперь мне сказать? . ."
        else:
                    if not Player.Male:
                        ch_p "Помнишь момент, когда я сказала тебе, что не люблю тебя?"
                    else:
                        ch_p "Помнишь момент, когда я сказал тебе, что не люблю тебя?"
                    $ BetsyX.FaceChange("perplexed",1)
                    ch_b ". . ."
                    $ BetsyX.FaceChange("sadside",1)
                    ch_b "Возможно, я уже забыла этот травмирующий опыт. . ."

        if Line != "love":
                menu:
                    extend ""
                    "Прости, я не хотела так говорить." if not Player.Male:
                        $ BetsyX.FaceChange("confused",1)
                        ch_b ". . ."
                        ch_b "Ясно. . ."
                        ch_p "Ага. То есть, я люблю тебя, [BetsyX.Name]."
                        $ BetsyX.Statup("Love", 200, 10)
                        if ApprovalCheck(BetsyX, 950, "L"):
                            $ Line = "love"
                            $ BetsyX.FaceChange("surprised",1,Mouth="normal")
                        else:
                            $ BetsyX.FaceChange("sadside")
                            ch_b "Довольно. . . мне кажется, я больше тебя не люблю. . ."
                    "Прости, я не хотел так говорить." if Player.Male:
                        $ BetsyX.FaceChange("confused",1)
                        ch_b ". . ."
                        ch_b "Ясно. . ."
                        ch_p "Ага. То есть, я люблю тебя, [BetsyX.Name]."
                        $ BetsyX.Statup("Love", 200, 10)
                        if ApprovalCheck(BetsyX, 950, "L"):
                            $ Line = "love"
                            $ BetsyX.FaceChange("surprised",1,Mouth="normal")
                        else:
                            $ BetsyX.FaceChange("sadside")
                            ch_b "Довольно. . . мне кажется, я больше тебя не люблю. . ."
                    "Я передумала, я люблю тебя, так что. . ." if not Player.Male:
                        if ApprovalCheck(BetsyX, 950, "L"):
                            $ Line = "love"
                            $ BetsyX.FaceChange("surprised",1,Mouth="normal")
                            ch_b "Ох? Правда?!"
                        else:
                            $ BetsyX.Mouth = "sad"
                            ch_b "Ясно. . ."
                            $ BetsyX.Statup("Inbt", 90, 10)
                            $ BetsyX.FaceChange("sadside")
                            ch_b ". . . но мне кажется, я больше тебя не люблю. . ."
                    "Я передумал, я люблю тебя, так что. . ." if not Player.Male:
                        if ApprovalCheck(BetsyX, 950, "L"):
                            $ Line = "love"
                            $ BetsyX.FaceChange("surprised",1,Mouth="normal")
                            ch_b "Ох? Правда?!"
                        else:
                            $ BetsyX.Mouth = "sad"
                            ch_b "Ясно. . ."
                            $ BetsyX.Statup("Inbt", 90, 10)
                            $ BetsyX.FaceChange("sadside")
                            ch_b ". . . но мне кажется, я больше тебя не люблю. . ."
                    "Эм, неважно.":
                            $ BetsyX.Statup("Love", 200, -30)
                            $ BetsyX.Statup("Obed", 50, 10)
                            $ BetsyX.FaceChange("angry")
                            if not Player.Male:
                                ch_b "Ох, да пошла ты."
                            else:
                                ch_b "Ох, да пошел ты."
                            $ BetsyX.RecentActions.append("angry")
                            $ BetsyX.DailyActions.append("angry")
        if Line == "love":
                $ BetsyX.Statup("Love", 200, 40)
                $ BetsyX.Statup("Obed", 90, 10)
                $ BetsyX.Statup("Inbt", 90, 10)
                $ BetsyX.FaceChange("normal")
                if not Player.Male:
                    ch_b "Я. . . Я очень ценю, что ты хорошенько все обдумала. . ."
                else:
                    ch_b "Я. . . Я очень ценю, что ты хорошенько все обдумал. . ."
                ch_b "Я тоже тебя люблю, [BetsyX.Petname]!"
                $ BetsyX.Petnames.append("lover")
        $ BetsyX.Event[6] = 25
        return

# end Betsy_Love//////////////////////////////////////////////////////////


# start Betsy_Sub//////////////////////////////////////////////////////////

label Betsy_Sub:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(BetsyX,"bemused","кажется тихой. . .")
            return
    $ BetsyX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    call Shift_Focus(BetsyX)
    if BetsyX.Loc != bg_current and BetsyX not in Party:
        "Вдруг [BetsyX.Name] внезапно появляется перед вами и изъявляет желание поговорить."

    $ Event_Queue = [0,0]
    $ BetsyX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(BetsyX)
    call CleartheRoom(BetsyX)
    call Set_The_Scene
    call Taboo_Level
    $ BetsyX.DailyActions.append("relationship")
    $ BetsyX.FaceChange("bemused", 1)
    if not Player.Male and "girltalk" not in BetsyX.History:
            call expression BetsyX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
            return

    ch_b "[BetsyX.Petname], я уже довольно давно кое о чем думаю. . ."
    ch_b "Это связано с тем, насколько решительно ты командуешь окружающими."
    ch_b "Я нахожу это весьма. . ."
    $ BetsyX.FaceChange("sly",1)
    ch_b "-притягательным."
    menu:
        extend ""
        "Приятно слышать.":
                $ BetsyX.Statup("Obed", 200, 2)
                $ BetsyX.Statup("Inbt", 70, 1)
        "Еще бы." :
                $ BetsyX.Statup("Obed", 200, 4)
                $ BetsyX.Statup("Inbt", 70, 1)
        "Серьезно?":
                $ BetsyX.Statup("Obed", 200, 1)
                ch_b "Да, серьезно. . ."
        "Ладно.":
                $ BetsyX.FaceChange("confused",1)
                $ BetsyX.Statup("Love", 200, -1)
                $ BetsyX.Statup("Obed", 200, -1)
                ch_b ". . ."
        ". . .":
                pass
    ch_b "И мою голову посетила мысль, что раньше моя жизнь была несколько. . ."
    $ BetsyX.FaceChange("bemused",1)
    ch_b ". . . сдержанной."
    ch_b "Контроль, подавление эмоций, \"закусывание нижней губы,\" и все такое."
    ch_b "Я всю жизнь боролась с собой. . ."
    ch_b "Следила за своим поведением. . ."
    $ BetsyX.FaceChange("normal",1)
    ch_b "Буду откровенна, это очень утомительно!"
    menu:
        extend ""
        "Верю.":
                $ BetsyX.Statup("Love", 80, 2)
                $ BetsyX.Statup("Obed", 200, 1)
                ch_b "В общем. . ."
        "Понимаю." :
                $ BetsyX.Statup("Obed", 200, 1)
                ch_b "Разумеется."
        "Уверена, все так и было." if not Player.Male:
                ch_b "В общем. . ."
        "Уверен, все так и было." if Player.Male:
                ch_b "В общем. . ."
        "С тебя этого хватит?":
                $ BetsyX.FaceChange("sly",1)
                $ BetsyX.Statup("Inbt", 70, 2)
                ch_b "Я как раз подходила к этому моменту. . ."
        ". . .":
                ch_b "В общем. . ."
    ch_b "Я надеялась, что ты, возможно, захочешь взять на себя часть этого бремени."
    if not Player.Male:
        ch_b "Если ты не возражаешь, не могла бы ты давать мне указания?"
    else:
        ch_b "Если ты не возражаешь, не мог бы ты давать мне указания?"
    ch_b "Руководить моим поведением, чтобы облегчить мою ношу?"
    $ BetsyX.FaceChange("sly",1)
    if not Player.Male:
        ch_b "Может, тебе понравится, если я буду звать тебя . . госпожа?"
    else:
        ch_b "Может, тебе понравится, если я буду звать тебя . . господин?"
    $ BetsyX.History.append("sir")
    while "sir" not in BetsyX.Petnames:
        menu:
            extend ""
            "Меня это устраивает.":
                    $ BetsyX.Statup("Love", 60, 3)
                    $ BetsyX.Statup("Love", 90, 3)
                    $ BetsyX.Statup("Obed", 90, 5)
                    if not Player.Male:
                        $ BetsyX.Petname = "госпожа"
                        $ BetsyX.Petname_rod = "госпожи"
                        $ BetsyX.Petname_dat = "госпоже"
                        $ BetsyX.Petname_vin = "госпожу"
                        $ BetsyX.Petname_tvo = "госпожой"
                        $ BetsyX.Petname_pre = "госпоже"
                    else:
                        $ BetsyX.Petname = "господин"
                        $ BetsyX.Petname_rod = "господина"
                        $ BetsyX.Petname_dat = "господину"
                        $ BetsyX.Petname_vin = "господина"
                        $ BetsyX.Petname_tvo = "господином"
                        $ BetsyX.Petname_pre = "господине"
                    $ BetsyX.Petnames.append("sir")
                    ch_b "Замечательно. . . [BetsyX.Petname]."
            "Меня все устраивает, но не надо звать меня \"госпожой.\"" if not Player.Male:
                    $ BetsyX.Statup("Love", 60, 3)
                    $ BetsyX.Statup("Love", 90, 3)
                    $ BetsyX.Statup("Obed", 200, 3)
                    $ BetsyX.Statup("Inbt", 50, 2)
                    ch_b "Я постараюсь этого избегать. . . [BetsyX.Petname]."
                    $ BetsyX.Petnames.append("sir")
            "Меня все устраивает, но не надо звать меня \"господином.\"" if Player.Male:
                    $ BetsyX.Statup("Love", 60, 3)
                    $ BetsyX.Statup("Love", 90, 3)
                    $ BetsyX.Statup("Obed", 200, 3)
                    $ BetsyX.Statup("Inbt", 50, 2)
                    ch_b "Я постараюсь этого избегать. . . [BetsyX.Petname]."
                    $ BetsyX.Petnames.append("sir")
            "Я не понимаю, что от этого изменится?":
                    $ BetsyX.Statup("Love", 90, -1)
                    $ BetsyX.Statup("Obed", 200, 2)
                    $ BetsyX.Statup("Inbt", 50, 2)
                    $ BetsyX.Statup("Inbt", 80, 2)
                    $ BetsyX.FaceChange("bemused",1)
                    ch_b "Возможно, ничего, но, думаю, мне будет легче."
                    menu:
                        extend ""
                        ". . .":
                                if not Player.Male:
                                    $ BetsyX.Petname = "госпожа"
                                    $ BetsyX.Petname_rod = "госпожи"
                                    $ BetsyX.Petname_dat = "госпоже"
                                    $ BetsyX.Petname_vin = "госпожу"
                                    $ BetsyX.Petname_tvo = "госпожой"
                                    $ BetsyX.Petname_pre = "госпоже"
                                else:
                                    $ BetsyX.Petname = "господин"
                                    $ BetsyX.Petname_rod = "господина"
                                    $ BetsyX.Petname_dat = "господину"
                                    $ BetsyX.Petname_vin = "господина"
                                    $ BetsyX.Petname_tvo = "господином"
                                    $ BetsyX.Petname_pre = "господине"
                        "Только не зови меня \"госпожой.\"" if not Player.Male:
                                $ BetsyX.Statup("Inbt", 80, 2)
                                ch_b "Конечно."
                        "Только не зови меня \"господином.\"" if Player.Male:
                                $ BetsyX.Statup("Inbt", 80, 2)
                                ch_b "Конечно."
                        "Пожалуй, в этом действительно есть какой-то смысл.":
                                $ BetsyX.Statup("Obed", 200, 2)
                                if not Player.Male:
                                    $ BetsyX.Petname = "госпожа"
                                    $ BetsyX.Petname_rod = "госпожи"
                                    $ BetsyX.Petname_dat = "госпоже"
                                    $ BetsyX.Petname_vin = "госпожу"
                                    $ BetsyX.Petname_tvo = "госпожой"
                                    $ BetsyX.Petname_pre = "госпоже"
                                else:
                                    $ BetsyX.Petname = "господин"
                                    $ BetsyX.Petname_rod = "господина"
                                    $ BetsyX.Petname_dat = "господину"
                                    $ BetsyX.Petname_vin = "господина"
                                    $ BetsyX.Petname_tvo = "господином"
                                    $ BetsyX.Petname_pre = "господине"
                    $ BetsyX.Petnames.append("sir")
            "Я не уверена." if not Player.Male:
                    $ BetsyX.Statup("Obed", 200, 1)
                    $ BetsyX.Statup("Inbt", 80, 3)
                    ch_b "Я понимаю твои сомнения, в конце концов, они отражают мои собственные. . ."
                    ch_b "Возможно, тебе надо время все обдумать. . ."
                    return
            "Я не уверен." if Player.Male:
                    $ BetsyX.Statup("Obed", 200, 1)
                    $ BetsyX.Statup("Inbt", 80, 3)
                    ch_b "Я понимаю твои сомнения, в конце концов, они отражают мои собственные. . ."
                    ch_b "Возможно, тебе надо время все обдумать. . ."
                    return
            ". . ." if ". . ." not in BetsyX.RecentActions:
                    $ BetsyX.RecentActions.append(". . .")
                    $ BetsyX.Statup("Love", 90, -1)
                    $ BetsyX.Statup("Obed", 200, 5)
                    $ BetsyX.Statup("Inbt", 50, 1)
                    $ BetsyX.FaceChange("confused", 1)
                    ch_b "Что ж. . ."
                    $ BetsyX.FaceChange("sly", 1)
                    ch_b "Боюсь, что мне нужен более четкий ответ. . ."
            ". . ." if ". . ." in BetsyX.RecentActions:
                    $ BetsyX.Statup("Love", 90, -3)
                    $ BetsyX.Statup("Obed", 200, -1)
                    $ BetsyX.Statup("Inbt", 50, 2)
                    $ BetsyX.FaceChange("confused", 1)
                    ch_b "Ясно. . ."
                    $ BetsyX.FaceChange("sly", 1)
                    ch_b "Пожалуй, мне придется расценить этот ответ, как \"нет\". . ."
                    ch_b "Возможно, тебе надо время все обдумать. . ."
                    return

    $ BetsyX.Statup("Obed", 90, 10)
    ch_b "Прошу, дай мне знать, если я смогу тебе как-то помочь. . ."
    $ BetsyX.Statup("Obed", 90, 10)
    ch_b "Я готова на -любую- помощь. . ."
    return


label Betsy_Sub_Asked:
    $ Line = 0
    $ BetsyX.FaceChange("sadside", 1)
    call Shift_Focus(BetsyX)
    ch_b "Как я поняла, тебе не интересна такая перспектива."
    menu:
        extend ""
        "Ну, я хочу извиниться. У меня еще есть возможность передумать?":
                if "sir" in BetsyX.Petnames and ApprovalCheck(BetsyX, 850, "O"):
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck(BetsyX, 550, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        pass
                else: #if it failed both those things,
                        $ BetsyX.FaceChange("angry", 1)
                        ch_b "Давай просто забудем об этом." #Failed again. :(
                        $ Line = "rude"

                if Line != "rude":
                        $ BetsyX.Statup("Love", 90, 10)
                        $ BetsyX.FaceChange("sly", 1)
                        ch_b "Пожалуй, можно попробовать еще раз. . ."

        "Я знаю, что ты этого хочешь. Попробуем еще раз или нет?":
                $ BetsyX.FaceChange("bemused", 1)
                if "sir" in BetsyX.Petnames:
                    if ApprovalCheck(BetsyX, 850, "O"):
                        ch_b "Как пожелаешь. . ."
                    else:
                        ch_b "Я предпочла бы пока воздержаться от этого."
                        $ Line = "rude"
                elif ApprovalCheck(BetsyX, 600, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        $ BetsyX.FaceChange("confused", 1)
                        ch_b "Ты, кажется, довольно смутно представляешь себе детали. . ."
                        $ BetsyX.FaceChange("sly", 1)
                        if not Player.Male:
                            ch_b "но, возможно, ты права."
                            ch_b "Ты точно уверена, что тебе понравится?"
                        else:
                            ch_b "но, возможно, ты прав."
                            ch_b "Ты точно уверен, что тебе понравится?"
                        menu:
                            extend ""
                            "Да, извини, что я была довольно груба." if not Player.Male:
                                            $ BetsyX.Statup("Love", 90, 15)
                                            $ BetsyX.Statup("Inbt", 50, 10)
                                            $ BetsyX.FaceChange("bemused", 1)
                                            $ BetsyX.Eyes = "side"
                                            ch_b "Ну хорошо."
                            "Да, извини, что я был довольно груб." if Player.Male:
                                            $ BetsyX.Statup("Love", 90, 15)
                                            $ BetsyX.Statup("Inbt", 50, 10)
                                            $ BetsyX.FaceChange("bemused", 1)
                                            $ BetsyX.Eyes = "side"
                                            ch_b "Ну хорошо."
                            "Ты охуеть как права, сучка.":
                                    if "sir" in BetsyX.Petnames and ApprovalCheck(BetsyX, 900, "O"):
                                            $ BetsyX.Statup("Love", 200, -5)
                                            $ BetsyX.Statup("Obed", 200, 10)
                                            ch_b ". . ."
                                    elif ApprovalCheck(BetsyX,700, "O"):
                                            $ BetsyX.Statup("Love", 200, -5)
                                            $ BetsyX.Statup("Obed", 200, 10)
                                            ch_b ". . . Что?"
                                    else: #if it failed both those things,
                                            $ BetsyX.Statup("Love", 200, -10)
                                            $ BetsyX.Statup("Obed", 90, -10)
                                            $ BetsyX.Statup("Obed", 200, -10)
                                            $ BetsyX.Statup("Inbt", 50, -15)
                                            $ BetsyX.FaceChange("angry", 1)
                                            ch_b "Мне кажется, это не совсем то, чего я хотела."
                                            $ Line = "rude"
                            "Ладно, тогда не бери в голову.":
                                            $ BetsyX.FaceChange("angry", 1)
                                            $ BetsyX.Statup("Love", 200, -10)
                                            $ BetsyX.Statup("Obed", 90, -10)
                                            $ BetsyX.Statup("Obed", 200, -10)
                                            $ BetsyX.Statup("Inbt", 50, -15)
                                            ch_b "Я бы предпочла не играть в эти игры."
                                            ch_b "Мне следовало лучше подготовиться."
                                            $ Line = "rude"

    $ BetsyX.RecentActions.append("asked sub")
    $ BetsyX.DailyActions.append("asked sub")
    if Line == "rude":
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Betsy_Sprite with easeoutright
            call Remove_Girl(BetsyX)
            $ BetsyX.RecentActions.append("angry")
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[BetsyX.Name] широкими шагами выходит из комнаты."
    elif "sir" in BetsyX.Petnames:
            #it didn't fail and "sir" was covered
            $ BetsyX.Statup("Obed", 200, 50)
            $ BetsyX.Petnames.append("master")
            if not Player.Male:
                $ BetsyX.Petname = "хозяйка"
                $ BetsyX.Petname_rod = "хозяйки"
                $ BetsyX.Petname_dat = "хозяйке"
                $ BetsyX.Petname_vin = "хозяйку"
                $ BetsyX.Petname_tvo = "хозяйкой"
                $ BetsyX.Petname_pre = "хозяйке"
            else:
                $ BetsyX.Petname = "хозяин"
                $ BetsyX.Petname_rod = "хозяина"
                $ BetsyX.Petname_dat = "хозяину"
                $ BetsyX.Petname_vin = "хозяина"
                $ BetsyX.Petname_tvo = "хозяином"
                $ BetsyX.Petname_pre = "хозяине"
            $ BetsyX.Eyes = "sly"
            if not Player.Male:
                ch_b ". . . хозяйка. . ."
            else:
                ch_b ". . . хозяин. . ."
    else:
            #it didn't fail
            $ BetsyX.Statup("Obed", 200, 30)
            $ BetsyX.Petnames.append("sir")
            if not Player.Male:
                $ BetsyX.Petname = "госпожа"
                $ BetsyX.Petname_rod = "госпожи"
                $ BetsyX.Petname_dat = "госпоже"
                $ BetsyX.Petname_vin = "госпожу"
                $ BetsyX.Petname_tvo = "госпожой"
                $ BetsyX.Petname_pre = "госпоже"
            else:
                $ BetsyX.Petname = "господин"
                $ BetsyX.Petname_rod = "господина"
                $ BetsyX.Petname_dat = "господину"
                $ BetsyX.Petname_vin = "господина"
                $ BetsyX.Petname_tvo = "господином"
                $ BetsyX.Petname_pre = "господине"
            $ BetsyX.FaceChange("sly", 1)
            if not Player.Male:
                ch_b ". . . госпожа. . ."
            else:
                ch_b ". . . господин. . ."
    return

# end Betsy_Sub//////////////////////////////////////////////////////////


# start Betsy_Master//////////////////////////////////////////////////////////

label Betsy_Master:
    if bg_current not in PersonalRooms:
            #if you aren't in someone's rooms, it tries again later
            call AskedMeet(BetsyX,"bemused","выглядит необычайно покорной. . .")
            return
    $ BetsyX.DrainWord("asked meet")
    $ Player.DrainWord("meet girl")
    call Shift_Focus(BetsyX)
    if BetsyX.Loc != bg_current and BetsyX not in Party:
        "Вдруг [BetsyX.Name] появляется словно из ниоткуда и изъявляет желание поговорить."

    $ Event_Queue = [0,0]
    $ BetsyX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(BetsyX)
    call CleartheRoom(BetsyX)
    $ BetsyX.ArmPose = 2
    call Set_The_Scene
    $ BetsyX.DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ BetsyX.FaceChange("sly", 1,Mouth="kiss")
    ch_b "Ох, [BetsyX.Petname]. . ."
    ch_b "Я хотел бы кое-что обсудить с тобой."
    $ BetsyX.FaceChange("sly",1,Eyes="side")
    ch_b "Нечто довольно. . . деликатное."
    ch_b "Твоя \"направляющая рука\" оказалась весьма привлекательной."
    $ BetsyX.FaceChange("sly",2,Eyes="side")
    ch_b "С каждым днем меня все больше возбуждает ситуация, сложившаяся между нами!"
    $ BetsyX.FaceChange("sly",1)
    ch_b "Как считаешь, может ли она вообще. . . перерасти во что-то большее?"
    $ BetsyX.History.append("master")
    while "master" not in BetsyX.Petnames:
        menu:
            extend ""
            "Конечно.":
                    $ BetsyX.Petnames.append("master")
                    $ BetsyX.Statup("Love", 200, 1)
                    $ BetsyX.Statup("Obed", 200, 2)
                    ch_b "Мне очень приятно это слышать. . ."
            "Я ждала этих слов." if "expected" not in BetsyX.RecentActions and not Player.Male:
                    $ BetsyX.RecentActions.append("expected")
                    $ BetsyX.Statup("Obed", 200, 4)
                    $ BetsyX.Statup("Inbt", 70, 2)
                    ch_b "Я рада. . ."
            "Я ждал этих слов." if "expected" not in BetsyX.RecentActions and Player.Male:
                    $ BetsyX.RecentActions.append("expected")
                    $ BetsyX.Statup("Obed", 200, 4)
                    $ BetsyX.Statup("Inbt", 70, 2)
                    ch_b "Я рада. . ."
            "Агась.":
                    $ BetsyX.Petnames.append("master")
                    $ BetsyX.FaceChange("confused",1,Eyes="side")
                    $ BetsyX.Statup("Obed", 200, -1)
                    ch_b "Я. . . рада это слышать. . ."
                    $ BetsyX.FaceChange("normal",1)
            "Меня устраивают наши текущие отношения.":
                    $ BetsyX.FaceChange("sadside",2)
                    $ BetsyX.Statup("Love", 80, -1)
                    $ BetsyX.Statup("Obed", 200, -2)
                    $ BetsyX.Statup("Inbt", 70, -2)
                    ch_b "Ох, что ж, я немного опечалена твоими словами. . ."
                    $ BetsyX.FaceChange("normal",1)
                    ch_b "Тем не менее, мне нравятся наши нынешние отношения."
                    return
            "Не-а.":
                    $ BetsyX.FaceChange("sad",2,Eyes="surprised")
                    $ BetsyX.Statup("Love", 80, -1)
                    $ BetsyX.Statup("Obed", 200, -4)
                    $ BetsyX.Statup("Inbt", 70, -2)
                    ch_b "Ох, дорогуша. . ."
                    $ BetsyX.FaceChange("sad",2)
                    ch_b "Боюсь, не такого ответа я ждала от тебя. . ."
                    hide Betsy_Sprite with easeoutright
                    call Remove_Girl(BetsyX)
                    $ BetsyX.FaceChange("normal",1)
                    $ BetsyX.Loc = "hold" #puts her off the board for the day
                    "Она уходит."
                    return
            "Что ты имеешь в виду?" if "what" not in BetsyX.RecentActions:
                    $ BetsyX.RecentActions.append("what")
                    $ BetsyX.Statup("Obed", 200, -1)
                    if not Player.Male:
                        ch_b "Я надеялась, что ты, возможно, согласишься стать моей хозяйкой?"
                    else:
                        ch_b "Я надеялась, что ты, возможно, согласишься стать моим хозяином?"
                    ch_b "Я же буду твоей верной слугой. . ."
            ". . ." if ". . ." not in BetsyX.RecentActions:
                    $ BetsyX.RecentActions.append(". . .")
                    $ BetsyX.Statup("Love", 90, -1)
                    $ BetsyX.Statup("Obed", 200, 5)
                    $ BetsyX.Statup("Inbt", 50, 1)
                    $ BetsyX.FaceChange("confused", 1)
                    ch_b "Ясно. . ."
                    $ BetsyX.FaceChange("sly", 1)
                    ch_b "Боюсь, мне нужен более четкий ответ. . ."
            ". . ." if ". . ." in BetsyX.RecentActions:
                    $ BetsyX.Statup("Love", 90, -3)
                    $ BetsyX.Statup("Obed", 200, -1)
                    $ BetsyX.Statup("Inbt", 50, 2)
                    $ BetsyX.FaceChange("confused", 1)
                    ch_b "Все понятно. . ."
                    $ BetsyX.FaceChange("sly", 1)
                    ch_b "Пожалуй, мне придется расценить такой ответ, как \"нет\". . ."
                    ch_b "Возможно, тебе надо время, чтобы все обдумать. . ."
                    return

    if not Player.Male:
        ch_b ". . . хозяйка."
    else:
        ch_b ". . . хозяин."
    menu:
        extend ""
        ". . .":
                if not Player.Male:
                    $ BetsyX.Petname = "хозяйка"
                    $ BetsyX.Petname_rod = "хозяйки"
                    $ BetsyX.Petname_dat = "хозяйке"
                    $ BetsyX.Petname_vin = "хозяйку"
                    $ BetsyX.Petname_tvo = "хозяйкой"
                    $ BetsyX.Petname_pre = "хозяйке"
                else:
                    $ BetsyX.Petname = "хозяин"
                    $ BetsyX.Petname_rod = "хозяина"
                    $ BetsyX.Petname_dat = "хозяину"
                    $ BetsyX.Petname_vin = "хозяина"
                    $ BetsyX.Petname_tvo = "хозяином"
                    $ BetsyX.Petname_pre = "хозяине"
                $ BetsyX.FaceChange("smile", 2, Eyes="side")
                $ BetsyX.Statup("Obed", 200, 2)
        "Слушай, а хорошо звучит.":
                if not Player.Male:
                    $ BetsyX.Petname = "хозяйка"
                    $ BetsyX.Petname_rod = "хозяйки"
                    $ BetsyX.Petname_dat = "хозяйке"
                    $ BetsyX.Petname_vin = "хозяйку"
                    $ BetsyX.Petname_tvo = "хозяйкой"
                    $ BetsyX.Petname_pre = "хозяйке"
                else:
                    $ BetsyX.Petname = "хозяин"
                    $ BetsyX.Petname_rod = "хозяина"
                    $ BetsyX.Petname_dat = "хозяину"
                    $ BetsyX.Petname_vin = "хозяина"
                    $ BetsyX.Petname_tvo = "хозяином"
                    $ BetsyX.Petname_pre = "хозяине"
                $ BetsyX.FaceChange("normal", 1)
                $ BetsyX.Statup("Love", 90, 1)
                $ BetsyX.Statup("Obed", 200, 2)
                $ BetsyX.Statup("Inbt", 80, 2)
        "Мне не нравится, когда ты называешь меня \"хозяйка.\"" if not Player.Male:
                $ BetsyX.FaceChange("normal", 1)
                $ BetsyX.Statup("Love", 90, 2)
                $ BetsyX.Statup("Obed", 200, 3)
                ch_b "Хорошо, буду продолжать звать тебя [BetsyX.Petname_tvo]."
        "Мне не нравится, когда ты называешь меня \"хозяин.\"" if Player.Male:
                $ BetsyX.FaceChange("normal", 1)
                $ BetsyX.Statup("Love", 90, 2)
                $ BetsyX.Statup("Obed", 200, 3)
                ch_b "Хорошо, буду продолжать звать тебя [BetsyX.Petname_tvo]."
    $ BetsyX.FaceChange("sly",1)
    ch_b "Прошу, дай мне знать, если тебе что-нибудь понадобится."
    ch_b "Я приложу все усилия, чтобы доставить тебе удовольствие. . ."
    return

# end Betsy_Master//////////////////////////////////////////////////////////



# start Betsy_Sexfriend//////////////////////////////////////////////////////////

label Betsy_Sexfriend:   #Betsy_Update
        if BetsyX.Loc != bg_current:
                "[BetsyX.Name] подходит к вам и отводит вас в сторону."
        else:
                "[BetsyX.Name] поворачивается к вам лицом."
        $ BetsyX.Loc = bg_current
        $ BetsyX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene
        $ Event_Queue = [0,0]
        $ BetsyX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in BetsyX.History:
                call expression BetsyX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        call Shift_Focus(BetsyX)
        $ Line = 0
        $ BetsyX.FaceChange("smile",2)
        $ BetsyX.Petnames.append("sex friend")
        if not Player.Male:
            ch_b "Этот институт интересное и дикое место, согласна?"
        else:
            ch_b "Этот институт интересное и дикое место, согласен?"
        ch_b "Мне было так весело с тех пор, как я прибыла сюда!"
        ch_b "Здесь гораздо менее душно, чем там, где я обучалась в прошлом."
        if Terms["he"] == "he":
                $ BetsyX.FaceChange("sly",2)
                ch_b "-и мне нравится, что тут есть симпатичные мальчики. . ."
        $ BetsyX.FaceChange("sly",1)
        ch_b "Поступление к вам для меня это было прекрасной возможностью \"распустить волосы.\""

        if BetsyX in Player.Harem:
                ch_b "Очень надеюсь, что мы еще долго будем вместе. . ."
                ch_b "Во всех смыслах. . ."
        elif "sir" in BetsyX.Petnames:
                ch_b "Я очень надеюсь, что мы долго сможем поддерживать наши. . . \"профессиональные отношения\". . ."
        else:
                ch_b "Я знаю, что у нас было не так уж много времени, чтобы развить наши отношения. . ."
                ch_b "Но я нахожу тебя очень хорошим товарищем."
        ch_b "Если что-то вдруг изменится в худшую сторону, сомневаюсь, что смогу обойтись без твоего тела. . ."
        ch_b "Так что. . . Я надеюсь, мы сможем также стать. . . \"секс-партнерами?\""
        $ BetsyX.Statup("Love", 90, 10)
        $ BetsyX.Statup("Obed", 90, 5)
        $ BetsyX.Statup("Inbt", 90, 15)
        if Taboo:
            ch_b "А теперь, может отойдем в более укромное место?"
            menu:
                extend ""
                "Ага":
                        $ BetsyX.Statup("Love", 90, 3)
                        $ BetsyX.Statup("Inbt", 200, 5)
                        ch_b "-Замечательно.-"
                        if bg_current == "bg player":
                                $ bg_current = "bg betsy"
                        else:
                                $ bg_current = "bg player"
                        $ BetsyX.Loc = bg_current
                        $ Party = []
                        call Set_The_Scene
                        call CleartheRoom(BetsyX)
                        call Set_The_Scene
                        $ Taboo = 0
                        $ BetsyX.Taboo = 0

                "Нет, давай сделаем это здесь.":
                        $ BetsyX.Statup("Obed", 80, 5)
                        $ BetsyX.Statup("Inbt", 90, 15)
                        ch_b "Ооох. . . шалунишка."
                "Не сейчас.":
                        $ BetsyX.FaceChange("sad", 1)
                        $ BetsyX.Statup("Love", 90, -3)
                        $ BetsyX.Statup("Obed", 90, 5)
                        ch_b "Жаль."
                        return
        else:
            ch_b "Пожалуй, сейчас самое время начать?"
            menu:
                extend ""
                "Конечно.":
                        $ BetsyX.Statup("Love", 90, 3)
                        $ BetsyX.Statup("Inbt", 90, 5)
                        ch_b "-Замечательно.-"
                "Давай не сейчас.":
                        $ BetsyX.FaceChange("sad", 1)
                        $ BetsyX.Statup("Love", 90, -3)
                        $ BetsyX.Statup("Obed", 90, 5)
                        ch_b "Жаль."
                        return
        $ Situation = BetsyX
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        #end "if no relationship"
        jump Misplaced
        return

# end Betsy_Sexfriend//////////////////////////////////////////////////////////


# start Betsy_Fuckbuddy//////////////////////////////////////////////////////////

label Betsy_Fuckbuddy:
        $ BetsyX.DailyActions.append("relationship")
        $ BetsyX.Lust = 60
        $ BetsyX.Wet = 2
        $ BetsyX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        #change Betsy's outfit to default
        $ BetsyX.Loc = bg_current
        $ Event_Queue = [0,0]
        call Shift_Focus(BetsyX)
        call Set_The_Scene(0)
        call Display_Girl(BetsyX)
        call Taboo_Level

        #$ BetsyX.Event[10] += 1

        "[BetsyX.Name] поворачивается к вам и выкрикивает:"
        $ BetsyX.FaceChange("surprised",1,Mouth="open")
        if Player.Male:
                ch_b "-Я позволю тебе пососать мои сиськи, если ты позволишь мне заглотить твой член!-"
        else:
                ch_b "-Я позволю тебе пососать мои сиськи, если ты позволишь мне окунуться в твою киску!-"
        while "fuck buddy" not in BetsyX.Petnames:
            menu:
                extend ""
                "Ладно!":
                        $ BetsyX.Petnames.append("fuck buddy")
                        $ BetsyX.FaceChange("smile",1)
                        $ BetsyX.Statup("Love", 90, 5)
                        $ BetsyX.Statup("Obed", 80, 2)
                        $ BetsyX.Statup("Inbt", 200, 5)
                        ch_b "Великолепно!"
                "Ты чо?!" if "what" not in BetsyX.RecentActions:
                        $ BetsyX.RecentActions.append("what")
                        $ BetsyX.FaceChange("surprised",2)
                        $ BetsyX.Statup("Inbt", 200, -2)
                        ch_b "О. . . прошу прощения, если это прозвучало слишком резко."
                        $ BetsyX.FaceChange("normal",1,Eyes="side")
                        ch_b "Так просто было в одной манге. . ."
                        ch_b "Я решила повторить."
                        $ BetsyX.FaceChange("sly",1)
                "Нет!" if "noschlong" not in BetsyX.RecentActions:
                        $ BetsyX.RecentActions.append("noschlong")
                        $ BetsyX.FaceChange("surprised",2)
                        $ BetsyX.Statup("Love", 80, -1)
                        $ BetsyX.Statup("Obed", 80, 2)
                        $ BetsyX.Statup("Inbt", 200, -2)
                        if not Player.Male:
                            ch_b "Ох, дорогуша, возможно, ты неправильно меня поняла."
                        else:
                            ch_b "Ох, дорогуша, возможно, ты неправильно меня понял."
                "Все равно нет!" if "noschlong" in BetsyX.RecentActions:
                        $ BetsyX.RecentActions.append("noschlong")
                        $ BetsyX.Petnames.append("fuck buddy")
                        $ BetsyX.FaceChange("sadside",2)
                        $ BetsyX.Statup("Love", 80, -2)
                        $ BetsyX.Statup("Obed", 90, 5)
                        $ BetsyX.Statup("Inbt", 200, -5)
                        ch_b "Ясно."
                        $ BetsyX.FaceChange("sly",1)
                        ch_b "Ну что ж, надеюсь, если тебе захочется хорошего секса, ты обратишься ко мне."
                ". . ." if ". . ." not in BetsyX.RecentActions:
                        $ BetsyX.RecentActions.append(". . .")
                        $ BetsyX.FaceChange("confused", 1)
                        $ BetsyX.Statup("Obed", 90, 3)
                        $ BetsyX.Statup("Inbt", 200, -1)
                        ch_b "Ясно. . ."
                        $ BetsyX.FaceChange("sly", 1)
                        ch_b "Я должна воспринимать это как \"да?\" . ."
                ". . ." if ". . ." in BetsyX.RecentActions:
                        $ BetsyX.Petnames.append("fuck buddy")
                        $ BetsyX.FaceChange("sly",1)
                        $ BetsyX.Statup("Love", 80, -2)
                        $ BetsyX.Statup("Obed", 90, 2)
                        $ BetsyX.Statup("Inbt", 200, -3)
                        ch_b "Ах, ну ладно, прошу, приходи ко мне, если тебе понадобится хороший секс."
        $ BetsyX.FaceChange("surprised",1,Mouth="open")
        ch_b "Америка - страна свободы!!!"
        menu:
            extend ""
            "О да!":
                    $ BetsyX.Statup("Love", 90, 3)
                    $ BetsyX.Statup("Inbt", 200, 5)
                    ch_b "О да!"
            "Я не думаю, что наша \"Америка\" такая.":
                    $ BetsyX.FaceChange("surprised",2)
                    $ BetsyX.Statup("Obed", 80, 2)
                    $ BetsyX.Statup("Inbt", 200, -2)
                    ch_b "О, правда?"
                    $ BetsyX.FaceChange("surprised",2,Eyes="side")
                    $ BetsyX.Statup("Inbt", 200, -1)
                    ch_b "Это просто мне так кажется?"
                    menu:
                        extend ""
                        "Может да, а может и нет.":
                            $ BetsyX.FaceChange("sad",2,Mouth="smile")
                            $ BetsyX.Statup("Love", 80, 2)
                            $ BetsyX.Statup("Inbt", 200, 1)
                            ch_b ". . . Я надеюсь, что нет. . ."
                        "Возможно.":
                            $ BetsyX.FaceChange("angry",1,Eyes="side")
                            $ BetsyX.Statup("Love", 80, -1)
                            $ BetsyX.Statup("Obed", 90, 3)
                            $ BetsyX.Statup("Inbt", 200, -2)
                            ch_b "Ясно. . ."
                        ". . .":
                            $ BetsyX.FaceChange("angry",1,Eyes="side",Mouth="smirk")
                            $ BetsyX.Statup("Inbt", 200, 2)
                            ch_b "Что ж, ясно. . ."
            "Я тебя не понимаю.":
                    $ BetsyX.FaceChange("smile",1)
                    ch_b "Просто здесь меня не \"осуждают\" так, как дома."
                    menu:
                        extend ""
                        "Наверное.":
                            $ BetsyX.Statup("Love", 80, 2)
                            ch_b ". . . Я должна в это верить. . ."
                        "Еще бы.":
                            ch_b "Ага. . ."
                        ". . .":
                            $ BetsyX.Statup("Inbt", 200, 1)
                            ch_b "По крайней мере, я так предполагаю. . ."
            ". . .":
                    pass
        $ BetsyX.FaceChange("sly",1)
        if Taboo:
            ch_b "Ну так что, не хочешь присоединиться ко мне в каком-нибудь более укромном месте?"
            menu:
                extend ""
                "Хочу":
                        $ BetsyX.FaceChange("smile",1)
                        $ BetsyX.Statup("Love", 80, 2)
                        $ BetsyX.Statup("Inbt", 200, 10)
                        ch_b "Великолепно!"
                        if bg_current == "bg player":
                                $ bg_current = "bg betsy"
                        else:
                                $ bg_current = "bg player"
                        $ BetsyX.Loc = bg_current
                        call CleartheRoom(BetsyX)
                        call Set_The_Scene
                        $ Taboo = 0
                        $ BetsyX.Taboo = 0

                "Нет, давай сделаем это здесь.":
                        $ BetsyX.Statup("Obed", 80, 5)
                        $ BetsyX.Statup("Inbt", 200, 15)
                        ch_b "Ох, веди себя прилично. . ."
                "Не сейчас.":
                        $ BetsyX.FaceChange("sad", 1)
                        $ BetsyX.Statup("Love", 90, -3)
                        $ BetsyX.Statup("Obed", 90, 5)
                        if not Player.Male:
                            ch_b "Обломщица!"
                        else:
                            ch_b "Обломщик!"
                        return
        else:
            ch_b "Ну. . . хочешь пососать мои сиськи?"
            menu:
                extend ""
                "Конечно.":
                        $ BetsyX.Statup("Love", 90, 3)
                        $ BetsyX.Statup("Inbt", 200, 5)
                        ch_b "Восхитительно."
                "Не сейчас.":
                        $ BetsyX.FaceChange("sad", 1)
                        $ BetsyX.Statup("Love", 90, -3)
                        $ BetsyX.Statup("Obed", 90, 5)
                        if not Player.Male:
                            ch_b "Обломщица!"
                        else:
                            ch_b "Обломщик!"
                        return
        $ Situation = BetsyX
        $ Player.AddWord(1,"interruption") #adds to Recent
#        call Betsy_SexPrep              #she offers sex
        call SexMenu
        jump Misplaced
        return
# end Betsy_Fuckbuddy//////////////////////////////////////////////////////////

# start Betsy_Daddy//////////////////////////////////////////////////////////

#Not updated

label Betsy_Daddy:       #Betsy_Update
        $ BetsyX.DailyActions.append("relationship")
        $ BetsyX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ Event_Queue = [0,0]
        call Shift_Focus(BetsyX)
        if BetsyX.Loc != bg_current:
                $ BetsyX.Loc = bg_current
                "[BetsyX.Name] подходит к вам."
        call Set_The_Scene
        $ BetsyX.FaceChange("sadside",1,Mouth="normal")
        ch_b ". . ."
        ch_b "У меня, возможно, довольно необычная. . . просьба. . ."
        $ BetsyX.FaceChange("sadside",1,Mouth="smirk")
        ch_b "Я тут думала об одной. . . \"ролевой игре\". . ."
        $ BetsyX.FaceChange("sadside",2,Mouth="smirk")
        ch_b "Просто так. . ."
        ch_b "Веселья ради. . ."
        $ BetsyX.FaceChange("sad",2,Mouth="normal")
        ch_b ". . . что скажешь, если я буду звать тебя. . ."
        $ BetsyX.FaceChange("sadside",2,Mouth="normal")
        if not Player.Male:
            ch_b "\"мамочкой?\""
        else:
            ch_b "\"папочкой?\""
        menu:
            extend ""
            "Ладно, давай?":
                $ BetsyX.FaceChange("smile")
                $ BetsyX.Statup("Love", 90, 20)
                $ BetsyX.Statup("Obed", 60, 10)
                $ BetsyX.Statup("Inbt", 80, 30)
                ch_b "Ох, отлично!"
            "Зачем?":
                $ BetsyX.FaceChange("bemused")
                ch_b "Ох, дорогуша. . . что ж. . ."
                if BetsyX.Love > BetsyX.Obed and BetsyX.Love > BetsyX.Inbt:
                        ch_b "Мне просто показалось это забавным. . ."
                elif BetsyX.Obed > BetsyX.Inbt:
                        if not Player.Male:
                            ch_b "Ты просто так строга со мной. . ."
                        else:
                            ch_b "Ты просто такой строгий со мной. . ."
                else:
                        ch_b "Это весьма неприлично, не находишь?"

                menu:
                    extend ""
                    "Звучит интересно, меня устраивает.":
                            $ BetsyX.FaceChange("smile")
                            $ BetsyX.Statup("Love", 90, 15)
                            $ BetsyX.Statup("Obed", 60, 20)
                            $ BetsyX.Statup("Inbt", 80, 25)
                            ch_b "Вот и славно!"
                            $ BetsyX.FaceChange("sly",2)
                            if not Player.Male:
                                ch_b " . . . мамочка."
                            else:
                                ch_b " . . . папочка."
                            $ BetsyX.FaceChange("sly",1)
                            if not Player.Male:
                                $ BetsyX.Petname = "мамочка"
                                $ BetsyX.Petname_rod = "мамочки"
                                $ BetsyX.Petname_dat = "мамочке"
                                $ BetsyX.Petname_vin = "мамочку"
                                $ BetsyX.Petname_tvo = "мамочкой"
                                $ BetsyX.Petname_pre = "мамочке"
                            else:
                                $ BetsyX.Petname = "папочка"
                                $ BetsyX.Petname_rod = "папочки"
                                $ BetsyX.Petname_dat = "папочке"
                                $ BetsyX.Petname_vin = "папочку"
                                $ BetsyX.Petname_tvo = "папочкой"
                                $ BetsyX.Petname_pre = "папочке"
                    "Может лучше не надо, пожалуйста?":
                            $ BetsyX.Statup("Love", 90, 5)
                            $ BetsyX.Statup("Obed", 80, 40)
                            $ BetsyX.Statup("Inbt", 80, 20)
                            $ BetsyX.FaceChange("sad")
                            ch_b "   . . .   "
                            ch_b "Ну хорошо."
                    "У тебя серьезные проблемы с отцом, да?" if Player.Male:
                            $ BetsyX.Statup("Love", 90, -15)
                            $ BetsyX.Statup("Obed", 80, 45)
                            $ BetsyX.Statup("Inbt", 70, 5)
                            $ BetsyX.FaceChange("sadside",2)
                            ch_b "Что ж. . . может быть. . ."
                            ch_b "-однако дело не в этом!"
                            $ BetsyX.FaceChange("sadside",1)
                    "У тебя серьезные проблемы с матерью, да?" if not Player.Male:
                            $ BetsyX.Statup("Love", 90, -15)
                            $ BetsyX.Statup("Obed", 80, 45)
                            $ BetsyX.Statup("Inbt", 70, 5)
                            $ BetsyX.FaceChange("sadside",2)
                            ch_b "Что ж. . . может быть. . ."
                            ch_b "-однако дело не в этом!"
                            $ BetsyX.FaceChange("sadside",1)

            "У тебя серьезные проблемы с матерью, да?" if not Player.Male:
                    $ BetsyX.Statup("Love", 90, -15)
                    $ BetsyX.Statup("Obed", 80, 45)
                    $ BetsyX.Statup("Inbt", 70, 5)
                    $ BetsyX.FaceChange("sadside",2)
                    ch_b "Что ж. . . может быть. . ."
                    ch_b "Ладно, давай забудем об этом."
                    $ BetsyX.FaceChange("sadside",1,Mouth="normal")
            "У тебя серьезные проблемы с отцом, да?" if Player.Male:
                    $ BetsyX.Statup("Love", 90, -15)
                    $ BetsyX.Statup("Obed", 80, 45)
                    $ BetsyX.Statup("Inbt", 70, 5)
                    $ BetsyX.FaceChange("sadside",2)
                    ch_b "Что ж. . . может быть. . ."
                    ch_b "Ладно, давай забудем об этом."
                    $ BetsyX.FaceChange("sadside",1,Mouth="normal")
        $ BetsyX.Petnames.append("daddy")
        return

# end Betsy_Daddy//////////////////////////////////////////////////////////



# Start Character Meet Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gwen Meet Betsy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Betsy_Meet:
        # GwenX.Event[2] tracks number of girls she knows you're dating
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = bg_current
        $ BetsyX.Loc = bg_current
        call Shift_Focus(GwenX)
        $ GwenX.ArmPose = 2
        call Set_The_Scene
        $ GwenX.FaceChange("normal",1)
        $ BetsyX.FaceChange("smile",1)
        ch_b "Здравствуй, [BetsyX.Petname]. . ."
        if BetsyX.Petname in ("хозяин","господин","хозяйка","госпожа"):
                $ GwenX.Statup("Obed", 60, 2)
                $ GwenX.Statup("Obed", 80, 5)
        $ GwenX.ArmPose = 1
        $ BetsyX.ArmPose = 2
        hide Betsy_Seated
        show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc)
        hide Gwen_Seated
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom -1
        $ GwenX.Hat = 0
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_g "Фиолетовые волосы, британский акцент. . . Псайлок?"
        $ BetsyX.FaceChange("confused",1,Eyes="side")
        ch_b "Эм. . . Элизабет Брэддок, вообще-то, хотя мне больше нравится Бетси."
        ch_b "Думаю, мы не представлены?"
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "О! Прости. Забегаю вперед."
        ch_g "Гвендолин Пул, зови меня Гвен!"
        ch_g "Мне нравится твой акцент. *пародирует ее говор [[Извинте, но перевести это не могу]*"
        $ BetsyX.FaceChange("confused",1,Eyes="side",Mouth="smile")
        ch_b "Спасибо? Я уже к этому привыкла."
        ch_g "Хех! *пародирует ее говор [[Извините, но перевести это не могу]*"
        $ BetsyX.FaceChange("angry",1,Eyes="side")
        $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="sad")
        ch_b "Прошу, не надо."
        $ GwenX.FaceChange("sad",1,Eyes="side")
        menu:
            extend ""
            ". . .":
                    pass
            "Мы уже это проходили.":
                    $ BetsyX.FaceChange("sly",1)
                    $ GwenX.FaceChange("smile",1,Eyes="side")
                    $ BetsyX.Statup("Love", 80, 3)
                    ch_b "Не напоминай мне."
        $ BetsyX.FaceChange("smile",1,Eyes="side")
        $ GwenX.FaceChange("sad",1,Eyes="side",Mouth="open")
        ch_g "О, извини!"
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "Твои волосы выглядят просто великолепно."
        ch_b "Благодарю?"
        $ BetsyX.FaceChange("smile",1)
        $ GwenX.FaceChange("confused",1,Eyes="side")
        ch_b "Боже, ее легко возбудить, да?"
        menu:
            extend ""
            "Ага.":
                    $ BetsyX.Statup("Love", 80, 2)
                    $ GwenX.Statup("Obed", 90, 2)
                    $ GwenX.FaceChange("surprised",1,Mouth="open")
            "Пожалуй.":
                    $ GwenX.FaceChange("surprised",1,Mouth="open")
            "Ты даже не представляешь насколько.":
                    $ GwenX.Statup("Love", 80, -2)
                    $ GwenX.Statup("Obed", 80, 3)
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    ch_g "Эй!"
            "Она сумасшедшая.":
                    $ BetsyX.FaceChange("confused",1)
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    $ GwenX.Statup("Love", 80, -4)
                    $ GwenX.Statup("Obed", 90, 5)
                    ch_g "Эй!"
            ". . .":
                    $ BetsyX.Statup("Love", 80, -1)
        $ BetsyX.FaceChange("confused",1,Eyes="side")
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "Значит и Кваннон где-то рядом? [[В комиксах Бетси поменялась телами с Кваннон]"
        ch_b "Кто?"
        $ GwenX.FaceChange("confused",1,Eyes="side")
        ch_g ". . . Кваннон?"
        ch_b ". . . ты имеешь в виду \"Каннон,\" Бодхисаттву? [[Каннон - богиня плодородия в яп мифологии, RLE позновательная]"
        $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
        ch_b "Я не буддистка."
        $ BetsyX.FaceChange("surprised",2,Eyes="side")
        ch_b "Ты что, думаешь, что я буддистка?"
        $ BetsyX.FaceChange("angry",1)
        ch_g "Нет! Нетнетнет. . ."
        $ GwenX.FaceChange("sad",1)
        ch_g "Я просто. . . [[памагите!]"
        menu:
            extend ""
            "Я вообще ничего не понимаю.":
                    $ GwenX.Statup("Obed", 90, 2)
                    ch_g "Эх. . ."
            "Ты знала, что она наполовину японка?" if "boyfriend" in BetsyX.Petnames:
                    $ BetsyX.Statup("Love", 90, 2)
                    $ GwenX.Statup("Love", 80, 2)
                    $ GwenX.Statup("Obed", 60, 1)
                    $ GwenX.FaceChange("surprised",1,Mouth="open")
                    ch_g "Ох!"
                    $ GwenX.FaceChange("surprised",1)
                    ch_g "Ох."
                    $ GwenX.FaceChange("sad",1)
                    ch_g "Эм. . ."
            "Ты сама по себе.":
                    $ GwenX.Statup("Love", 80, -2)
                    $ GwenX.Statup("Obed", 90, 2)
                    $ GwenX.FaceChange("angry",2)
                    ch_g "!!!"
            ". . .":
                    $ GwenX.Statup("Love", 80, -1)
                    $ GwenX.Statup("Obed", 90, 3)
                    ch_g "Спасибо. . ."
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_g "Извини!"
        ch_g "Я тебе перепутала с другой девушкой!"
        $ GwenX.FaceChange("sad",1,Eyes="side")
        ch_g "Но мне интересно. . ."
        $ BetsyX.FaceChange("confused",1,Eyes="side",Mouth="smirk")
        ch_b "Как я могу быть одновременно британкой и азиаткой?"
        $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
        ch_g "Нет! . . эм, нет. . ."
        ch_g "Вовсе нет. . ."
        $ BetsyX.FaceChange("sad",1,Eyes="leftside")
        $ GwenX.FaceChange("sad",1,Eyes="side")
        ch_b "*вздыхает*"
        ch_b "Пожалуй, я не должна так удивляться."
        $ BetsyX.FaceChange("sad",1,Eyes="side")
        ch_b "Я наполовину японка, но родилась и выросла в Англии, как и сотни тысяч британцев."
        ch_b "Это не так уж и необычно."
        ch_b "Для этого не нужна сложная предыстория."
        $ BetsyX.FaceChange("confused",1,Eyes="side",Mouth="normal")
        ch_b "Разве ты не видела в фильмах британцев азиатского происхождения?"
        ch_g "Навеееерное вииидела?"
        $ BetsyX.FaceChange("normal",1,Eyes="side")
        $ GwenX.FaceChange("sad",1,Eyes="side",Mouth="normal")
        ch_g "Извини еще раз!"
        ch_g "Я вела себя как дура!"
        $ BetsyX.FaceChange("confused",1,Eyes="side")
        $ GwenX.FaceChange("sly",1,Eyes="side")
        ch_g "[[умно адаптировали персонажа. . .]"
        ch_b ". . ."
        $ BetsyX.FaceChange("normal",1,Eyes="side")
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_b "Все нормально, правда."
        $ BetsyX.FaceChange("smile",1,Eyes="side")
        ch_b "Я уверена, что ты ничего такого не имела в виду, да и [BetsyX.Petname_dat], похоже, ты нравишься."
        menu:
            extend ""
            "Ага, она клевая.":
                    $ GwenX.Statup("Love", 80, 3)
                    ch_g "Ага, я клевая!"
            "Ты привыкнешь к ней.":
                    $ GwenX.Statup("Love", 80, 2)
                    ch_g "Не сомневаюсь!"
            "Что? Нет, она мне не нравится.":
                    $ GwenX.Statup("Love", 80, -2)
                    $ GwenX.Statup("Obed", 90, 2)
                    $ GwenX.FaceChange("angry",2,Mouth="open")
                    ch_g "Эй!"
            ". . .":
                    $ GwenX.Statup("Love", 80, -1)
                    $ GwenX.Statup("Obed", 90, 2)
                    $ GwenX.FaceChange("angry",1,Mouth="open")
                    ch_g "Ничего не скажешь?!"

        $ GwenX.FaceChange("smile",1,Eyes="side")
        if not Player.Male:
            ch_g "Ты, наверное, хорошо знакома с ней? . ."
        else:
            ch_g "Ты, наверное, хорошо знакома с ним? . ."
        if BetsyX in Player.Harem:
                $ BetsyX.FaceChange("sly",1)
                $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
                $ BetsyX.Statup("Obed", 80, 1)
                $ BetsyX.Statup("Inbt", 80, 2)
                ch_b "Ну конечно, мы встречаемся."
                $ GwenX.FaceChange("surprised",1,Eyes ="side")
                if GwenX.Event[2] > 1:
                        #if betsy heard you were dating two+ girls
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Inbt", 80, 3)
                        if not Player.Male:
                            ch_g "Ох, ого. . . похоже, у нее сейчас очень мало свободного времени. . ."
                        else:
                            ch_g "Ох, ого. . . похоже, у него сейчас очень мало свободного времени. . ."
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_b "Хехе. . . ага. . ."
                elif GwenX.Event[2]:
                        #if betsy heard you were dating someone else
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 3)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "Ох. . . ого, значит, вы обе. . ."
                        $ GwenX.Statup("Obed", 50, 4)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_b "Хехе. . . ага. . ."
                else:
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Obed", 60, 2)
                        $ GwenX.Statup("Obed", 80, 2)
                        $ GwenX.FaceChange("sly",1)
                        ch_g "Ох. . . клево, клево. . ."
                $ GwenX.Event[2] += 1
        elif BetsyX.Petname in ("хозяин","господин","хозяйка","госпожа"):
                $ BetsyX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                if not Player.Male:
                    ch_b "Ох. . . она моя [BetsyX.Petname]. . ."
                else:
                    ch_b "Ох. . . он мой [BetsyX.Petname]. . ."
        elif not ApprovalCheck(BetsyX, 500, "L"):
                $ BetsyX.FaceChange("normal",0)
                if not Player.Male:
                    ch_b "Что ж, она мой. . . замечательный экскурсовод. . ."
                else:
                    ch_b "Что ж, он мой. . . замечательный экскурсовод. . ."
        else:
                $ BetsyX.FaceChange("sad",1,Eyes="leftside")
                if not Player.Male:
                    ch_b "Что ж. . . она та, кто умеет обращаться с багажом. . ."
                else:
                    ch_b "Что ж. . . он тот, кто умеет обращаться с багажом. . ."
        $ GwenX.FaceChange("normal",1,Eyes="side")
        $ BetsyX.FaceChange("smile",1,Eyes="side",Mouth="open")
        ch_g "Мне, эм. . . в общем, как-нибудь свидимся!"
        ch_b "Конечно, прощай!"
        $ GwenX.FaceChange("normal",1)
        $ BetsyX.FaceChange("smile",1)
        $ BetsyX.GirlLikeUp(GwenX,100)
        $ GwenX.GirlLikeUp(BetsyX,100)
        $ GwenX.DrainWord("Betsy",0,0,0,1)
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
        return

# End Gwen Meet Betsy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# End Character Meet Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Betsy_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        if "switched" in BetsyX.History:
                jump Betsy_Switch2
        $ BetsyX.FaceChange("normal", 1)
        ch_b "Здравствуй?"
        $ BetsyX.FaceChange("confused", 1)
        ch_b "Хм, слушай. . ."
        ch_b ". . ."
        ch_b "Вы с [Player.XName_tvo], случайно, не родственники?"
        menu:
            extend ""
            "Это я и есть, я [Player.XName].":
                    $ BetsyX.FaceChange("smile", 1)
                    ch_b "Ох!"
                    $ BetsyX.AddWord(1,"switch") #recent

            "Нет.":
                    ch_b "Хм. Знаешь, вы очень похожи."
                    ch_b "Кстати, меня зовут [BetsyX.Name], не желаешь представиться? . ."
            "Возможно?":
                    ch_b "\"Возможно?\" . ."

        if "switch" not in BetsyX.RecentActions:
                    $ BetsyX.FaceChange("confused", 1)
                    ch_b ". . ."
                    $ BetsyX.FaceChange("surprised", 1,Mouth= "open")
                    ch_b "[Player.XName]! Это ты!"
                    $ BetsyX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Ага, это я, [Player.XName].":
                                $ BetsyX.Statup("Love", 90, 1)
                                $ BetsyX.Statup("Obed", 70, 1)
                                ch_b "Тебе удалось на минуту меня запутать."
                                $ BetsyX.FaceChange("normal", 1)
                        "Нет.":
                                $ BetsyX.FaceChange("bemused", 1)
                                $ BetsyX.Statup("Obed", 60, 1)
                                $ BetsyX.Statup("Obed", 70, 1)
                                ch_b "Чушь."
                        "Возможно?":
                                $ BetsyX.FaceChange("sly", 1)
                                $ BetsyX.Statup("Love", 80, 1)
                                $ BetsyX.Statup("Obed", 70, 1)
                                $ BetsyX.Statup("Inbt", 60, 1)
                                ch_b "Тебе меня не обмануть."
                    ch_b "К чему эти попытки обмануть меня?"
                    menu:
                        extend ""
                        "Извини, хотелось пошутить.":
                                $ BetsyX.FaceChange("sly", 1)
                                $ BetsyX.Statup("Love", 70, 1)
                        "Молодец, ты все поняла.":
                                $ BetsyX.FaceChange("sly", 1)
                                $ BetsyX.Statup("Obed", 70, 1)
                                $ BetsyX.Statup("Inbt", 80, 1)
                                ch_b "Это было очевидно."
                        "Хех.":
                                $ BetsyX.FaceChange("sly", 1,Eyes="side")
                                $ BetsyX.Statup("Love", 70, 1)
                                $ BetsyX.Statup("Love", 90, 1)
                                $ BetsyX.Statup("Inbt", 70, 1)
                                ch_b "Ну и ну. . ."
                    ch_b "Я понимаю, когда людям необходимы перемены в жизни. . ."
        #end "tried to lie"
        $ BetsyX.FaceChange("smile", 1)
        if not Player.Male:
            ch_b "Могу я спросить, почему ты решилась на такие перемены?"
        else:
            ch_b "Могу я спросить, почему ты решился на такие перемены?"
        menu:
            extend ""
            "Да так, по приколу.":
                    $ BetsyX.Statup("Inbt", 70, 1)
                    $ BetsyX.FaceChange("sly", 1)
                    ch_b "Ясно."
            "Я так себя сейчас ощущаю.":
                    ch_b "Я могу тебя понять."
            "У меня не было каких-то особых причин.":
                    ch_b "Мне кажется, тебе просто захотелось \"разнообразия\"."

        if [Player.Name] != [Player.XName]:
                ch_p "А еще теперь меня зовут [Player.Name]."
                ch_b "Приятно познакомиться, [Player.Name]."

        if BetsyX.SEXP >= 15:
                $ BetsyX.FaceChange("sad", 1,Mouth="normal")
                ch_b "Я тебя еще. . . привлекаю?"
                menu:
                    extend ""
                    "Конечно!":
                            $ BetsyX.FaceChange("normal", 1)
                            $ BetsyX.Statup("Love", 70, 2)
                            $ BetsyX.Statup("Love", 90, 1)
                            ch_b "Ох, приятно слышать. . ."
                    "Да не особо.":
                            $ BetsyX.FaceChange("sad", 1)
                            $ BetsyX.Statup("Love", 80, -2)
                            $ BetsyX.Statup("Obed", 60, 2)
                            $ BetsyX.Statup("Obed", 80, 2)
                            ch_b "Я понимаю."
                    "А ты как думаешь?":
                            $ BetsyX.FaceChange("sly", 1)
                            $ BetsyX.Statup("Obed", 70, 1)
                            $ BetsyX.Statup("Inbt", 70, 1)
                            if not Player.Male:
                                ch_b "Думаю, тогда бы ты избегала меня. . ."
                            else:
                                ch_b "Думаю, тогда бы ты избегал меня. . ."

        if not Player.Male and BetsyX.Les > 5:
                $ BetsyX.FaceChange("sly", 1)
                ch_b "Что ж, думаю, мне нравится твой новый облик. . ."
        if ApprovalCheck(BetsyX, 1200):
                ch_b "Думаю, я смогу привыкнуть к твоему новому облику. . ."
                $ BetsyX.AddWord(1,0,0,0,"girltalk") #history
        else:
                $ BetsyX.FaceChange("normal", 1,Eyes="side")
                ch_b "Думаю, мне нужно немного времени, чтобы привыкнуть к твоему новому облику. . ."
        $ BetsyX.Traits.remove("switchcheck")
        $ BetsyX.AddWord(1,0,0,0,"switched") #history
        return

label Betsy_Switch2:
        #when you switch for a 2+ time
        $ BetsyX.FaceChange("smile", 1)
        if not Player.Male:
            ch_b "Ох, [Player.Name], ты вернула свой прежний облик."
        else:
            ch_b "Ох, [Player.Name], ты вернул свой прежний облик."
        $ BetsyX.Traits.remove("switchcheck")
        $ BetsyX.History.remove("switched")
        $ BetsyX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Betsy_Girltalk(Auto=0,Other=0):
        # if Auto Betsy starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in BetsyX.History:
                return
        if "nogirls" in BetsyX.History:
                jump Betsy_Girltalk_Redux
        $ BetsyX.FaceChange("normal", 1)
        if Auto:
                ch_b "[Player.Name]. . ."
        ch_b "Как я поняла, ты, кажется, предпочитаешь. . . девушек?"
        ch_b "Мне любопытно, я тебе тоже нравлюсь. . ?"
        menu:
            extend ""
            "Да?":
                    $ BetsyX.FaceChange("sly", 1)
                    $ BetsyX.Statup("Love", 70, 2)
                    $ BetsyX.Statup("Love", 90, 2)
                    $ BetsyX.Statup("Obed", 70, 1)
                    ch_b "Я это ценю. . ."
            "Наверное?":
                    $ BetsyX.FaceChange("confused", 1)
                    $ BetsyX.Statup("Love", 70, 1)
                    $ BetsyX.Statup("Obed", 80, 2)
                    $ BetsyX.Statup("Inbt", 80, 2)
                    ch_b "Ясно. . ."
            "Разве ты не знаешь, что нравишься мне?":
                    $ BetsyX.FaceChange("sly", 1)
                    $ BetsyX.Statup("Love", 70, 3)
                    $ BetsyX.Statup("Love", 90, 2)
                    $ BetsyX.Statup("Obed", 70, 1)
                    ch_b "Пожалуй, у меня были подобные мысли. . ."
            "Не особо.":
                    $ BetsyX.FaceChange("surprised", 1)
                    $ BetsyX.Statup("Love", 90, -1)
                    $ BetsyX.Statup("Obed", 60, 2)
                    $ BetsyX.Statup("Obed", 80, 2)
                    ch_b "Ох?"
                    ch_b "Это сильный удар по моему самолюбию. . ."
        $ BetsyX.FaceChange("sly", 1)
        if not BetsyX.Les:
                ch_b "У меня нет значительного. . ."
                $ BetsyX.FaceChange("sadside", 2)
                ch_b "-опыта с девушками. . ."
        if not ApprovalCheck(BetsyX, 1000) and not ApprovalCheck(BetsyX, 600, "L") and not BetsyX.Les:
                ch_b "Я. . . не уверена, готова ли к новому опыту. . ."
                $ BetsyX.AddWord(1,0,0,0,"nogirls") #history
                call Girltalk_Check(BetsyX)
                return

        ch_b "Пожалуй, это может быть восхитительный опыт, почему бы не попробовать?"
        $ BetsyX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(BetsyX)
        return

label Betsy_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing
        if ApprovalCheck(BetsyX, 1000) or ApprovalCheck(BetsyX, 600, "L"):
                $ BetsyX.FaceChange("sly", 1)
                if Other in TotalGirls and "nogirls" in Other.History:
                        ch_b "Я не уверена. . ."
                ch_b "Пожалуй, это может быть восхитительный опыт, почему бы не попробовать?"
                $ BetsyX.DrainWord("nogirls",0,0,0,1) #history
                $ BetsyX.AddWord(1,0,0,0,"girltalk") #history
        elif "nogirls" not in BetsyX.History:
                $ BetsyX.AddWord(1,0,0,0,"nogirls") #history
                ch_b "Хмм. . . не в данный момент."
        elif "nogirls" in BetsyX.DailyActions:
                $ BetsyX.FaceChange("angry", 1)
                if BetsyX.Forced:
                        #if Forced, she will just go with it anyway
                        if "nogirls" not in BetsyX.RecentActions:
                                $ BetsyX.Statup("Love", 80, -2)
                                $ BetsyX.Statup("Obed", 80, 2)
                                $ BetsyX.AddWord(1,"nogirls",0,0,0) #recent
                        return
                ch_b "Перестань спрашивать."
        else:
                $ BetsyX.Statup("Inbt", 50, 2)
                ch_b "Я совсем не готова к такого рода отношениям."
                $ BetsyX.AddWord(1,0,"nogirls",0,0) #daily
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Betsy_Psyknife_Intro:
        #when she introduces the Psyknife
        $ BetsyX.Loc = bg_current
        call Set_The_Scene
        call Shift_Focus(BetsyX)
        call CleartheRoom(BetsyX)
        if not Player.Male and "girltalk" not in BetsyX.History:
                call expression BetsyX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        $ Line = 0
        $ BetsyX.FaceChange("smile",1)
        ch_b "[BetsyX.Petname], я бы хотела с тобой кое-что обсудить. . ."
        ch_b "Помнишь, как я показывала тебе свой \"псионический нож?\""
        menu:
            extend ""
            "Ага, что ты хотела обсудить?":
                    $ BetsyX.FaceChange("sly",1)
                    $ BetsyX.Statup("Love", 80, 2)
                    ch_b "Хорошо, что тебе интересно. . ."
            "Ага.":
                    $ BetsyX.Statup("Love", 80, 1)
                    $ BetsyX.Statup("Obed", 60, 1)
                    ch_b "Хорошо, я боялась, что нам придется проходить через это снова. . ."
            "Не особо.":
                    $ BetsyX.FaceChange("confused",1)
                    $ BetsyX.Statup("Love", 80, -1)
                    $ BetsyX.Statup("Obed", 80, 2)
                    ch_b "Какая жалость. В общем. . ."
            ". . .":
                    $ BetsyX.FaceChange("confused",1)
                    $ BetsyX.Statup("Inbt", 70, 1)
                    ch_b "В общем. . ."
        $ BetsyX.FaceChange("smile",1)
        ch_b "Этот клинок - сосредоточенная совокупность моих психических сил, отточенных до идеала."
        ch_b "В бою он может обезвредить даже самых сильных противников."
        menu:
            extend ""
            "Здорово!":
                    $ BetsyX.Statup("Love", 70, 1)
                    $ BetsyX.Statup("Love", 80, 1)
                    ch_b "Ага."
            "Это угроза?!":
                    $ BetsyX.FaceChange("surprised",2)
                    $ BetsyX.Statup("Obed", 50, -1)
                    $ BetsyX.Statup("Inbt", 70, 2)
                    ch_b "Конечно же нет!"
            "Вааау! [[попятиться]":
                    $ BetsyX.FaceChange("surprised",2)
                    $ BetsyX.Statup("Love", 80, -1)
                    $ BetsyX.Statup("Obed", 50, 2)
                    $ BetsyX.Statup("Obed", 70, 1)
                    $ BetsyX.Statup("Inbt", 70, 2)
            ". . .":
                    $ BetsyX.Statup("Inbt", 70, 2)
        $ BetsyX.FaceChange("sly",1)
        ch_b "Не волнуйся, я не собираюсь причинять тебе вред."
        $ BetsyX.FaceChange("sly",2,Eyes="side")
        ch_b "Я подняла эту тему, потому что у него есть. . . и другие применения."
        ch_b "Более. . . бодрящии."
        $ BetsyX.FaceChange("sly",1)
        ch_b "Благодаря нему я могу поделиться своими чувствами с кем-то другим."
        ch_b "Конечно, сюда входят и сексуальные чувства. . ."
        menu:
            extend ""
            "Я понимаю, это может быть весело.":
                    $ BetsyX.Statup("Love", 80, 2)
                    $ BetsyX.Statup("Inbt", 70, 1)
                    if not Player.Male:
                        ch_b "Я рада, что ты оценила его. . . потенциал."
                    else:
                        ch_b "Я рада, что ты оценил его. . . потенциал."
            "Не думаю, что тебе он нужен, чтобы завести меня.":
                    $ BetsyX.Statup("Love", 70, 2)
                    $ BetsyX.Statup("Love", 90, 1)
                    $ BetsyX.Statup("Inbt", 70, 1)
                    ch_b "Ох, я это прекрасно понимаю."
            "Ты когда-нибудь использовала второй вариант применения в бою?":
                    $ BetsyX.FaceChange("surprised",2)
                    $ BetsyX.Statup("Obed", 70, 2)
                    $ BetsyX.Statup("Inbt", 70, 1)
                    ch_b " . . ."
                    $ BetsyX.FaceChange("sly",2,Eyes="side")
                    $ BetsyX.Statup("Inbt", 80, 2)
                    ch_b "Я не буду отвечать."
            "Мы можем попробовать?":
                    $ BetsyX.Statup("Obed", 70, 1)
                    $ BetsyX.Statup("Inbt", 70, 2)
                    ch_b "Я надеялась, что ты попросишь. . ."
                    $ BetsyX.RecentActions.append("doit")
            "Продолжай. . . [[продолжить диалог].":
                    $ BetsyX.Statup("Love", 70, -1)
                    $ BetsyX.Statup("Obed", 70, 2)
                    $ BetsyX.Statup("Inbt", 70, -1)
        if "doit" not in BetsyX.RecentActions:
            $ BetsyX.FaceChange("sly",1)
            ch_b "Хочешь попробовать?"
            menu:
                extend ""
                "Ага!":
                    $ BetsyX.Statup("Love", 80, 1)
                    $ BetsyX.Statup("Inbt", 70, 1)
                    ch_b "Замечательно."
                "Давай.":
                    $ BetsyX.Statup("Obed", 80, 2)
                    $ BetsyX.Statup("Inbt", 80, 1)
                    ch_b "Конечно."
                "Если ты этого хочешь.":
                    $ BetsyX.FaceChange("sly",1,Brows="sad")
                    $ BetsyX.Statup("Love", 80, -1)
                    $ BetsyX.Statup("Obed", 60, 1)
                    $ BetsyX.Statup("Inbt", 70, 2)
                    ch_b "Не вижу в тебе энтузиазма. . ."
                "Не-а.":
                    $ BetsyX.FaceChange("sad",2)
                    $ BetsyX.Statup("Love", 80, -1)
                    $ BetsyX.Statup("Obed", 50, 2)
                    $ BetsyX.Statup("Obed", 70, 2)
                    ch_b "Ох. . . жаль."
                    ch_b "Дай мне знать, если передумаешь."
                    $ BetsyX.AddWord(1,0,0,0,"knife") #discussed the knife, but did not use it
                    jump Misplaced
        if BetsyX.Lust < 50:
            $ BetsyX.FaceChange("sly",2,Eyes="side")
            $ BetsyX.Statup("Inbt", 80, 2)
            ch_b "Дайте мне минутку. . . подготовиться. . ."
            $ BetsyX.FaceChange("sly",2,Eyes="closed")
            "Она проводит рукой по телу и начинает ласкать себя."
            $ BetsyX.Lust += 20
            $ BetsyX.FaceChange("sly",2)
            "Она смотрит вам в глаза и становится все более и более возбужденной."
            $ BetsyX.Lust += 20
            ch_b "Ах. . . Пожалуй, этого должно быть достаточно. . ."

        #stab
        $ Player.Focus += BetsyX.Lust
        $ Player.Focus = 100 if Player.Focus > 100 else Player.Focus
        $ BetsyX.ArmPose = 2
        $ BetsyX.Knife = 1
        show Betsy_Butterfly onlayer black
        call Punch
        $ BetsyX.AddWord(1,"knife","knife",0,"knife")
        "Она вонзает свой псионический нож вам в голову, и мир перед вашими глазами вспыхивает фиолетовым."
        hide Betsy_Butterfly onlayer black
        $ BetsyX.ArmPose = 1
        $ BetsyX.Knife = 0

        if Player.Focus >= 100:
                if "focus" in Player.Traits:
                        menu:
                            "Сосредоточиться или нет?"
                            "Да, нужно держать себя в руках.":
                                        $ Player.FocusX = 1
                            "Нет, отдаться моменту.":
                                        pass
                call Player_Cumming(BetsyX)
                $ Player.FocusX = 0
                if Player.Focus <= 50:
                        $ BetsyX.Statup("Love", 80, 1)
                        $ BetsyX.Statup("Inbt", 70, 2)
                        $ BetsyX.Statup("Lust", 200, 10)
                        $ Line = "came"
                else:
                        $ BetsyX.Statup("Obed", 60, 2)
                        $ BetsyX.Statup("Obed", 80, 1)

        if BetsyX.Lust >= 100:
                call Girl_Cumming(BetsyX)
                $ BetsyX.FaceChange("sly",2)
                $ BetsyX.Statup("Inbt", 70, 2)
                ch_b ". . . мне это никогда не надоест. . ."

        $ BetsyX.FaceChange("sly",1)
        ch_b "Так, похоже, ты хорошо переносишь мое воздействие. . ."
        ch_b "Боюсь, я не смогу пользоваться им слишком часто."
        ch_b "Самое большее раз в несколько часов."
        ch_b "Но теперь, когда мы попробовали. . ."
        $ BetsyX.FaceChange("sly",2,Eyes="down")
        if Line == "came":
                ch_b "Хочешь продолжить?"
        else:
                $ Line = 0
                if not Player.Male:
                    ch_b "Пожалуй, я оставила тебя несколько возбужденной. . ."
                else:
                    ch_b "Пожалуй, я оставила тебя несколько возбужденным. . ."
                ch_b "И что нам с этим делать?"
        $ BetsyX.FaceChange("sly",1)
        $ Line = 0
        call SexMenu
        return

label Betsy_Psyknife:
        #Raises your focus by her lust
        #if "knife" in BetsyX.History:
        if BetsyX.Loc != bg_current:
                ch_b "Боюсь, для этого я должна быть рядом с тобой."
                return
        if "knife" in BetsyX.RecentActions:
                ch_b "Боюсь, я не могу сосредоточиться, [BetsyX.Petname]."
                return
        $ Player.Focus += BetsyX.Lust
        $ Player.Focus = 100 if Player.Focus > 100 else Player.Focus
        $ BetsyX.Lust = 100 if Player.Focus > 100 else BetsyX.Lust
        if "knife" not in BetsyX.DailyActions:
                $ BetsyX.Statup("Inbt", 80, 2)
        show Betsy_Butterfly onlayer black
        call Punch
        $ BetsyX.AddWord(1,"knife","knife",0,"knife")
        if not renpy.showing("Betsy_HJ_Animation"):
                $ BetsyX.ArmPose = 2
        $ BetsyX.Knife = 1
        "Она вонзает свой псионическийй нож вам в голову."
        hide Betsy_Butterfly onlayer black
        $ BetsyX.ArmPose = 1
        $ BetsyX.Knife = 0
        return

label Betsy_69_Intro:
        if "69" in BetsyX.History:
                return
        if Trigger == "lick pussy" and BetsyX.LickP:
                if BetsyX.Blow or BetsyX.CUN or (ApprovalCheck(BetsyX, 1300) and BetsyX.SeenPeen):
                        #if licking pussy but have gotten blowjob
                        $ BetsyX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_b "Знаешь, я считаю, что ты заслуживаешь. . . особого внимания. . ."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        if "cockout" not in Player.RecentActions:
                                $ Player.RecentActions.append("cockout")
                                if Player.Male:
                                        "Она вытаскивает ваш член и начинает его сосать."
                                else:
                                        "Она обнажает вашу киску и начинает ее лизать."
                        else:
                                if Player.Male:
                                        "Она хватает ваш член и располагается над ним."
                                else:
                                        "Она начинает лизать вашу киску."
                        $ BetsyX.Pose = "69"
                        call Betsy_BJ_Launch
                        if Player.Male:
                            ch_b "Будь добр, не мог бы ты. . .?"
                        else:
                            ch_b "Будь добра, не могла бы ты. . .?"
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ BetsyX.Statup("Love", 95, 3)
                                    $ BetsyX.Statup("Inbt", 70, 2)
                                    $ BetsyX.Statup("Inbt", 90, 1)
                                    ch_b "Ах, то что надо."
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ BetsyX.Statup("Love", 80, -8)
                                    $ BetsyX.Statup("Obed", 80, 3)
                                    $ BetsyX.Statup("Obed", 90, 1)
                                    $ BetsyX.Statup("Inbt", 70, -1)
                                    ch_b "Какое ужасное разочарование."
                        $ Situation = "69"
                        call SexAct("blow") # call Betsy_SexAct("blow")
                        $ renpy.pop_call() #causes it to skip past the Escalation
                        $ renpy.pop_call() #causes it to skip past the last activity
        elif (Trigger == "blow" or Trigger == "cun") and (BetsyX.Blow or BetsyX.CUN):
                        #if licked pussy
                        $ BetsyX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        if Player.Male:
                                ch_b "Знаешь, ты мог бы сделать кое-что и для меня."
                        else:
                                ch_b "Знаешь, ты могла бы сделать кое-что и для меня."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        $ BetsyX.Pose = "69"
                        call Betsy_BJ_Launch
                        if Player.Male:
                                ch_b "Будь добр, не мог бы ты. . .?"
                        else:
                                ch_b "Будь добра, не могла бы ты. . .?"
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ BetsyX.Statup("Love", 95, 3)
                                    $ BetsyX.Statup("Inbt", 70, 2)
                                    $ BetsyX.Statup("Inbt", 90, 1)
                                    ch_b "Ах, то что надо."
                                    if not BetsyX.LickP:
                                        $ BetsyX.LickP += 1
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ BetsyX.Statup("Love", 80, -5)
                                    $ BetsyX.Statup("Obed", 80, 3)
                                    $ BetsyX.Statup("Obed", 90, 1)
                                    $ BetsyX.Statup("Inbt", 70, -1)
                                    ch_b "Какое ужасное разочарование."
                        #returns to BJ already in progress
        return
