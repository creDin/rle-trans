# star Kitty chat interface

#Kitty Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Kitty_Relationship: #rkelj
    while True:
        menu:
            ch_k "О чем ты хочешь поговорить?"
            "Хочешь стать моей девушкой?" if KittyX not in Player.Harem and "ex" not in KittyX.Traits:
                    $ KittyX.DailyActions.append("relationship")
                    if "asked boyfriend" in KittyX.DailyActions and "angry" in KittyX.DailyActions:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Серьезно, отвали."
                            return
                    elif "asked boyfriend" in KittyX.DailyActions:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Все еще \"нет.\""
                            return
                    elif KittyX.Break[0]:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Не когда ты встречаешься с ней. . ."
                            if Player.Harem:
                                    $ KittyX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "Это уже в прошлом."

                    $ KittyX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "KittyYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_k "Не думаю, что другим это понравится, [KittyX.Petname]."
                        else:
                            ch_k "Не думаю, что [Player.Harem[0].Name] будет рада, [KittyX.Petname]."
                        return

                    if KittyX.Event[5]:
                            $ KittyX.FaceChange("bemused", 1)
                            ch_k "Я {i}уже{/i} заводила этот разговор. . ."
                    else:
                            $ KittyX.FaceChange("surprised", 2)
                            ch_k "Я не уверена, [KittyX.Petname]. . ."
                            $ KittyX.FaceChange("smile", 1)

                    call Kitty_OtherWoman

                    if KittyX.Love >= 800:
                            $ KittyX.FaceChange("surprised", 1)
                            $ KittyX.Mouth = "smile"
                            if not KittyX.Event[5]:
                                    $ KittyX.Statup("Love", 200, 10)
                                    call Kitty_BF
                                    return
                            $ KittyX.Statup("Love", 200, 40)
                            ch_k "ДА!"
                            if "boyfriend" not in KittyX.Petnames:
                                        $ KittyX.Petnames.append("boyfriend")
                            if "KittyYes" in Player.Traits:
                                    $ Player.Traits.remove("KittyYes")
                            $ Player.Harem.append(KittyX)
                            call Harem_Initiation
                            "[KittyX.Name] подпрыгивает и страстно целует вас."
                            $ KittyX.FaceChange("kiss", 1)
                            $ KittyX.Kissed += 1
                    elif KittyX.Obed >= 500:
                            $ KittyX.FaceChange("perplexed")
                            ch_k "Я не особо хочу \"встречаться\". . ."
                    elif KittyX.Inbt >= 500:
                            $ KittyX.FaceChange("smile")
                            ch_k "Меня[KittyX.like]устраивают наши текущие отношения."
                    else:
                            $ KittyX.FaceChange("perplexed", 1)
                            ch_k "[KittyX.Petname], я не испытваю к тебе особых чувств сейчас."

            "Может, начнем все сначала?" if "ex" in KittyX.Traits:
                    $ KittyX.DailyActions.append("relationship")
                    if "asked boyfriend" in KittyX.DailyActions and "angry" in KittyX.DailyActions:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Серьезно, отвали."
                            return
                    elif "asked boyfriend" in KittyX.DailyActions:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Я все еще не согласна."
                            return

                    $ KittyX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "KittyYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_k "Не думаю, что другим это понравится, [KittyX.Petname]."
                            else:
                                ch_k "Не думаю, что [Player.Harem[0].Name] будет рада, [KittyX.Petname]."
                            return

                    $ Cnt = 0
                    call Kitty_OtherWoman

                    if KittyX.Love >= 800:
                            $ KittyX.FaceChange("surprised", 1)
                            $ KittyX.Mouth = "smile"
                            $ KittyX.Statup("Love", 90, 5)
                            ch_k "Ну конечно!"
                            if "boyfriend" not in KittyX.Petnames:
                                        $ KittyX.Petnames.append("boyfriend")
                            $ KittyX.Traits.remove("ex")
                            if "KittyYes" in Player.Traits:
                                    $ Player.Traits.remove("KittyYes")
                            $ Player.Harem.append(KittyX)
                            call Harem_Initiation
                            "[KittyX.Name] подпрыгивает и страстно целует вас."
                            $ KittyX.FaceChange("kiss", 1)
                            $ KittyX.Kissed += 1
                    elif KittyX.Love >= 600 and ApprovalCheck(KittyX, 1500):
                            $ KittyX.FaceChange("smile", 1)
                            $ KittyX.Statup("Love", 90, 5)
                            ch_k "Эм, ладно, наверное."
                            if "boyfriend" not in KittyX.Petnames:
                                        $ KittyX.Petnames.append("boyfriend")
                            $ KittyX.Traits.remove("ex")
                            if "KittyYes" in Player.Traits:
                                    $ Player.Traits.remove("KittyYes")
                            $ Player.Harem.append(KittyX)
                            call Harem_Initiation
                            $ KittyX.FaceChange("kiss", 1)
                            "[KittyX.Name] дарит вам легкий поцелуй."
                            $ KittyX.FaceChange("smile", 1)
                            $ KittyX.Kissed += 1
                    elif KittyX.Obed >= 500:
                            $ KittyX.FaceChange("sad")
                            ch_k "Думаю, лучше нам оставить все как есть."
                    elif KittyX.Inbt >= 500:
                            $ KittyX.FaceChange("perplexed")
                            ch_k "Мне нравится то, что сейчас между нами."
                    else:
                            $ KittyX.FaceChange("perplexed", 1)
                            ch_k "Я не готова снова обжечься."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if KittyX in Player.Harem:
                        call AskDateOther

            "Думаю, мы должны расстаться." if KittyX in Player.Harem:
                        if "breakup talk" in KittyX.RecentActions:
                                ch_k "Мы только что все обсудили, это совсем не смешно."
                        elif "breakup talk" in KittyX.DailyActions:
                                ch_k "Я не хочу снова это обсуждать, [KittyX.Petname]."
                        else:
                                call Breakup(KittyX)


            "О разговоре, который у нас был ранее. . .":
                menu:
                        "Помнишь, ты признавалась мне в любви. . ." if "lover" not in KittyX.Traits and KittyX.Event[6] >= 20:
                                call Kitty_Love_Redux

                        "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировала?" if "sir" not in KittyX.Petnames and "sir" in KittyX.History and not Player.Male:
                                if "asked sub" in KittyX.RecentActions:
                                        ch_k "Мы[KittyX.like]только что это обсудили."
                                elif "asked sub" in KittyX.DailyActions:
                                        ch_k "Думаю, ты уже ясно высказалась по этому поводу. . ."
                                else:
                                        call Kitty_Sub_Asked
                        "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировал?" if "sir" not in KittyX.Petnames and "sir" in KittyX.History and Player.Male:
                                if "asked sub" in KittyX.RecentActions:
                                        ch_k "Мы[KittyX.like]только что это обсудили."
                                elif "asked sub" in KittyX.DailyActions:
                                        ch_k "Думаю, ты уже ясно высказался по этому поводу. . ."
                                else:
                                        call Kitty_Sub_Asked
                        "Помнишь, ты говорила, что хочешь, чтобы я стала твоей хозяйкой?" if "master" not in KittyX.Petnames and "master" in KittyX.History and not Player.Male:
                                if "asked sub" in KittyX.RecentActions:
                                        ch_k "Мы[KittyX.like]только что это обсудили."
                                elif "asked sub" in KittyX.DailyActions:
                                            ch_k "Думаю, ты уже ясно высказалась по этому поводу. . ."
                                else:
                                        call Kitty_Sub_Asked
                        "Помнишь, ты говорила, что хочешь, чтобы я стал твоим хозяином?" if "master" not in KittyX.Petnames and "master" in KittyX.History and Player.Male:
                                if "asked sub" in KittyX.RecentActions:
                                        ch_k "Мы[KittyX.like]только что это обсудили."
                                elif "asked sub" in KittyX.DailyActions:
                                            ch_k "Думаю, ты уже ясно высказался по этому поводу. . ."
                                else:
                                        call Kitty_Sub_Asked

                        "О подарке для [LauraX.Name_rod]. . ." if "dress1" in LauraX.History and "dress2" not in LauraX.History and "dress3" not in LauraX.History:
                                call Laura_Dressup2

                        "Неважно":
                                pass
            "Неважно":
                return
    return

label Kitty_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((KittyX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ KittyX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_k "Но ты же сейчас с [Player.Harem [0].Name_tvo] и другими девушками!"
    else:
        ch_k "Но ты же сейчас с [Player.Harem[0].Name_tvo]!"
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "KittyYes" in Player.Traits:
                if ApprovalCheck(KittyX, 1800, Bonus = Cnt):
                    $ KittyX.FaceChange("smile", 1)
                    if KittyX.Love >= KittyX.Obed:
                            ch_k "Я смирюсь, пока мы можем быть вместе."
                    elif KittyX.Obed >= KittyX.Inbt:
                            ch_k "Если все так, я не против."
                    else:
                            ch_k "Да, думаю, я согласна."
                else:
                    $ KittyX.FaceChange("angry", 1)
                    ch_k "Может и так, но я не хочу делиться."
                    $ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "KittyYes" not in Player.Traits and not Player.Male:
                if ApprovalCheck(KittyX, 1800, Bonus = Cnt):
                        $ KittyX.FaceChange("smile", 1)
                        if KittyX.Love >= KittyX.Obed:
                            ch_k "Я смирюсь с этим, пока мы можем быть вместе."
                        elif KittyX.Obed >= KittyX.Inbt:
                            ch_k "Если она согласится, я не против."
                        else:
                            ch_k "Да, думаю, тогда я буду непротив."
                        ch_k "Спроси ее и сразу же расскажи мне о ее решении."
                else:
                        $ KittyX.FaceChange("angry", 1)
                        ch_k "Даже если она будет непротив, я не хочу делиться."
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "KittyYes" not in Player.Traits and Player.Male:
                if ApprovalCheck(KittyX, 1800, Bonus = Cnt):
                        $ KittyX.FaceChange("smile", 1)
                        if KittyX.Love >= KittyX.Obed:
                            ch_k "Я смирюсь с этим, пока мы можем быть вместе."
                        elif KittyX.Obed >= KittyX.Inbt:
                            ch_k "Если она согласится, я не против."
                        else:
                            ch_k "Да, думаю, тогда я буду непротив."
                        ch_k "Спроси ее и сразу же расскажи мне о ее решении."
                else:
                        $ KittyX.FaceChange("angry", 1)
                        ch_k "Даже если она будет непротив, я не хочу делиться."
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
                if not ApprovalCheck(KittyX, 1800, Bonus = -Cnt): #checks if Kitty likes you more than Kitty
                        $ KittyX.FaceChange("angry", 1)
                        if not ApprovalCheck(KittyX, 1800):
                                ch_k "Я не готова обманывать ради тебя."
                        else:
                                ch_k "Меня такое не устраивает, [Player.Harem[0].Name] моя подруга."
                        $ renpy.pop_call()
                else:
                        $ KittyX.FaceChange("smile", 1)
                        if KittyX.Love >= KittyX.Obed:
                                ch_k "Я очень хочу быть с тобой."
                        elif KittyX.Obed >= KittyX.Inbt:
                                ch_k "Если ты этого хочешь."
                        else:
                                ch_k "Пожалуй, и правда."
                        $ KittyX.Traits.append("downlow")

        "Я могу порвать с ней.":
                    $ KittyX.FaceChange("sad")
                    ch_k "Тогда давай встретимся завтра, после того, как ты со всем разберешься."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ KittyX.FaceChange("sad")
                    ch_k "Думаешь?"
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ KittyX.FaceChange("sad")
                    ch_k "Думаешь?"
                    $ renpy.pop_call()

    return


label KittyLike:
    menu:
        ch_k "Тогда[KittyX.like]что мне говорить?"
        "Как бы":
            $ KittyX.like = ", как бы, "
            $ KittyX.Like = "Как бы, "
            ch_k "Наверное, я[KittyX.like]слишком часто так говорю, да?"
        "Эм":
            $ KittyX.like = ", эм, "
            $ KittyX.Like = "Эм, "
            ch_k "[KittyX.Like]как скажешь."
        "Так вот и хм":
            $ KittyX.like = ", хм, "
            $ KittyX.Like = "Так вот, "
            ch_k "[KittyX.Like]думаю я могу[KittyX.like]говорить это чаще."
        "Няя":
            if ApprovalCheck(KittyX, 1400):
                $ KittyX.like = ", няя, "
                $ KittyX.Like = "Няя, "
                if not Player.Male:
                    ch_k "[KittyX.Like]ты такая дурочка."
                else:
                    ch_k "[KittyX.Like]ты такой придурок."
            elif ApprovalCheck(KittyX, 1000, "LO"):
                $ KittyX.like = ", няя, "
                $ KittyX.Like = "Няя, "
                ch_k "[KittyX.Like]если ты этого хочешь."
            else:
                ch_k "[KittyX.Like]ни за что, чудила."
        "Бля":
            if ApprovalCheck(KittyX, 400, "I"):
                $ KittyX.like = ", блять, "
                $ KittyX.Like = "Бля, "
                ch_k "[KittyX.Like]так и сделаю."
            elif ApprovalCheck(KittyX, 1000, "LO"):
                $ KittyX.like = ", блять, "
                $ KittyX.Like = "Бля, "
                ch_k "Если ты[KittyX.like]этого хочешь."
            else:
                ch_k "Я, блять, не хочу такое говорить."
                ch_k ". . .больше, чем обычно."
        "Ничего":
            if ApprovalCheck(KittyX, 900, "LO"):
                $ KittyX.like = " "
                $ KittyX.Like = ". . . "
                ch_k "[KittyX.Like]ладно . . ."
            else:
                ch_k "Не думаю, что я[KittyX.like]смогу."

    return


label Kitty_About(Check=0): #rkeljsg
    if Check not in TotalGirls:
            ch_k "Кто это?"
            return
    ch_k "Что я думаю о ней? Ну. . ."
    if Check == RogueX:
            if "poly Rogue" in KittyX.Traits:
                if not Player.Male:
                    ch_k "Ты должна знать, что[KittyX.like]мы очень близки. . ."
                else:
                    ch_k "Ты должен знать, что[KittyX.like]мы очень близки. . ."
            elif KittyX.LikeRogue >= 900:
                ch_k "Она[KittyX.like]очень сексуальная. . ."
            elif KittyX.LikeRogue >= 800:
                ch_k "Она моя лучшая подруга, и, может быть. . ."
            elif KittyX.LikeRogue >= 700:
                ch_k "Она[KittyX.like]моя лучшая подруга!"
            elif KittyX.LikeRogue >= 600:
                ch_k "Мы[KittyX.like]подружки и все такое."
            elif KittyX.LikeRogue >= 500:
                ch_k "Она[KittyX.like]не дура или типа того."
            elif KittyX.LikeRogue >= 400:
                ch_k "Она типа меня[KittyX.like]раздражает."
            elif KittyX.LikeRogue >= 300:
                ch_k "Да пошла эта сучка."
            else:
                ch_k "Это та шлюха?"
    elif Check == EmmaX:
            if "poly Emma" in KittyX.Traits:
                ch_k "Ты же знаешь, что мы трахаемся?"
            elif KittyX.LikeEmma >= 900:
                ch_k "У нее[KittyX.like]потрясающие сиськи. . ."
            elif KittyX.LikeEmma >= 800:
                ch_k "Она очень красивая. . ."
            elif KittyX.LikeEmma >= 700:
                ch_k "Думаю, мы стали хорошими подругами."
            elif KittyX.LikeEmma >= 600:
                ch_k "Она[KittyX.like]мой любимый преподватель."
            elif KittyX.LikeEmma >= 500:
                ch_k "Она[KittyX.like]нормальная."
            elif KittyX.LikeEmma >= 400:
                ch_k "Она задает[KittyX.like]слишком много домашки."
            elif KittyX.LikeEmma >= 300:
                ch_k "Пф, она ведьма."
            else:
                ch_k "Ты про эту шлюшку?"
    elif Check == LauraX:
            if "poly Laura" in KittyX.Traits:
                if not Player.Male:
                    ch_k "Ты должна знать, что мы[KittyX.like]иногда развлекаемся. . ."
                else:
                    ch_k "Ты должен знать, что мы[KittyX.like]иногда развлекаемся. . ."
            elif KittyX.LikeLaura >= 900:
                ch_k "Она[KittyX.like]словно зверь. . ."
            elif KittyX.LikeLaura >= 800:
                ch_k "В последнее время мы очень сблизились. . ."
            elif KittyX.LikeLaura >= 700:
                ch_k "Она[KittyX.like]очень хорошая подруга."
            elif KittyX.LikeLaura >= 600:
                ch_k "Мы[KittyX.like]команда."
            elif KittyX.LikeLaura >= 500:
                ch_k "Она[KittyX.like]не полная дура."
            elif KittyX.LikeLaura >= 400:
                ch_k "Она вроде как меня[KittyX.like]раздражает."
            elif KittyX.LikeLaura >= 300:
                ch_k "Это которая одичавшая девка?"
            else:
                ch_k "Она бешенная сучка."
    elif Check == JeanX:
            if "poly Jean" in KittyX.Traits:
                if not Player.Male:
                    ch_k "Ты должна знать, что[KittyX.like]мы очень близки. . ."
                else:
                    ch_k "Ты должен знать, что[KittyX.like]мы очень близки. . ."
            elif KittyX.LikeJean >= 900:
                ch_k "Она[KittyX.like]очень сексуальная. . ."
            elif KittyX.LikeJean >= 800:
                ch_k "Я думаю. . . Она очень хорошая. . ."
            elif KittyX.LikeJean >= 700:
                ch_k "Она[KittyX.like]моя лучшая подруга!"
            elif KittyX.LikeJean >= 600:
                ch_k "Мы, наверное[KittyX.like]друзья."
            elif KittyX.LikeJean >= 500:
                ch_k "Она[KittyX.like]не -так- уж плоха. . ."
            elif KittyX.LikeJean >= 400:
                ch_k "Она вроде как меня[KittyX.like]раздражает."
            elif KittyX.LikeJean >= 300:
                ch_k "Она[KittyX.like]очень приставучая!"
            else:
                ch_k "Ты про ту сучку?"
    elif Check == StormX:
            if "poly Storm" in KittyX.Traits:
                ch_k "Мы. . . вроде как занимались сексом?"
            elif KittyX.LikeStorm >= 900:
                ch_k "У нее[KittyX.like]шикарные формы. . ."
            elif KittyX.LikeStorm >= 800:
                ch_k "Она очень потрясающая. . ."
            elif KittyX.LikeStorm >= 700:
                ch_k "Мы[KittyX.like]близкие подруги."
            elif KittyX.LikeStorm >= 600:
                ch_k "Она[KittyX.like]мой любимый преподватель."
            elif KittyX.LikeStorm >= 500:
                ch_k "Она[KittyX.like]нормальная."
            elif KittyX.LikeStorm >= 400:
                ch_k "Она задает[KittyX.like]слишком много домашки."
            elif KittyX.LikeStorm >= 300:
                ch_k "Пфф, Ты про ту сучку?"
            else:
                ch_k "Ты про эту шлюшку?"
    elif Check == JubesX:
            if "poly Jubes" in KittyX.Traits:
                if not Player.Male:
                    ch_k "Ты должна знать, что мы[KittyX.like]иногда развлекаемся. . ."
                else:
                    ch_k "Ты должен знать, что мы[KittyX.like]иногда развлекаемся. . ."
            elif KittyX.LikeJubes >= 900:
                ch_k "Она[KittyX.like]настоящая бестия. . ."
            elif KittyX.LikeJubes >= 800:
                ch_k "В последнее время мы очень сблизились. . ."
            elif KittyX.LikeJubes >= 700:
                ch_k "Она[KittyX.like]очень хорошая подруга."
            elif KittyX.LikeJubes >= 600:
                ch_k "Мы[KittyX.like]команда."
            elif KittyX.LikeJubes >= 500:
                ch_k "Она[KittyX.like]не полная дура."
            elif KittyX.LikeJubes >= 400:
                ch_k "Она вроде как меня[KittyX.like]раздражает."
            elif KittyX.LikeJubes >= 300:
                ch_k "Ты про ту кусачую девку?"
            else:
                ch_k "Она бешенная сучка."
    elif Check == GwenX:
            if "poly Gwen" in KittyX.Traits:
                if not Player.Male:
                    ch_k "Ты должна знать, что мы[KittyX.like]иногда развлекаемся. . ."
                else:
                    ch_k "Ты должен знать, что мы[KittyX.like]иногда развлекаемся. . ."
            elif KittyX.LikeGwen >= 900:
                ch_k "Она[KittyX.like]такая игривая. . ."
            elif KittyX.LikeGwen >= 800:
                ch_k "В последнее время мы очень сблизились. . ."
            elif KittyX.LikeGwen >= 700:
                ch_k "Она[KittyX.like]очень хорошая подруга."
            elif KittyX.LikeGwen >= 600:
                ch_k "Мы, наверное[KittyX.like]друзья."
            elif KittyX.LikeGwen >= 500:
                ch_k "Я[KittyX.like]ее где-то видела."
            elif KittyX.LikeGwen >= 400:
                ch_k "Она вроде как меня[KittyX.like]раздражает."
            elif KittyX.LikeGwen >= 300:
                ch_k "Ты про ту девку, что постоянно говорит про \"Игровую вселенную\"?"
            else:
                ch_k "Она сучка."
    elif Check == BetsyX:
            if "poly Betsy" in KittyX.Traits:
                if not Player.Male:
                    ch_k "Ты должна знать, что мы[KittyX.like]иногда развлекаемся. . ."
                else:
                    ch_k "Ты должен знать, что мы[KittyX.like]иногда развлекаемся. . ."
            elif KittyX.LikeBetsy >= 900:
                ch_k "Она[KittyX.like]просто зверь. . ."
            elif KittyX.LikeBetsy >= 800:
                ch_k "В последнее время мы очень сблизились. . ."
            elif KittyX.LikeBetsy >= 700:
                ch_k "Она[KittyX.like]очень хорошая подруга."
            elif KittyX.LikeBetsy >= 600:
                ch_k "Мы[KittyX.like]с ней ладим."
            elif KittyX.LikeBetsy >= 500:
                ch_k "Она[KittyX.like]не совсем дура."
            elif KittyX.LikeBetsy >= 400:
                ch_k "Она вроде как меня[KittyX.like]раздражает."
            elif KittyX.LikeBetsy >= 300:
                ch_k "Ты про эту маленькую принцесску?"
            else:
                ch_k "Ты про эту заносчивую сучку?"
    elif Check == DoreenX:
            if "poly Doreen" in KittyX.Traits:
                if not Player.Male:
                    ch_k "Ты должна знать, что мы[KittyX.like]иногда развлекаемся. . ."
                else:
                    ch_k "Ты должен знать, что мы[KittyX.like]иногда развлекаемся. . ."
            elif KittyX.LikeDoreen >= 900:
                ch_k "Она[KittyX.like]такая очаровательная. . ."
            elif KittyX.LikeDoreen >= 800:
                ch_k "В последнее время мы очень сблизились. . ."
            elif KittyX.LikeDoreen >= 700:
                ch_k "Она[KittyX.like]очень хорошая подруга."
            elif KittyX.LikeDoreen >= 600:
                ch_k "Мы[KittyX.like]с ней подружились."
            elif KittyX.LikeDoreen >= 500:
                ch_k "Я[KittyX.like]ее пару раз видела."
            elif KittyX.LikeDoreen >= 400:
                ch_k "Она вроде как меня[KittyX.like]раздражает."
            elif KittyX.LikeDoreen >= 300:
                ch_k "Ты про \"Белку\"? Приглядывай за своими орешками."
            else:
                ch_k "Она сучка."
    elif Check == WandaX:
            if "poly Wanda" in KittyX.Traits:
                ch_k "Ты же знаешь, что мы[KittyX.like]иногда с ней целуемся. . ."
            elif KittyX.LikeWanda >= 900:
                ch_k "Она[KittyX.like]очень сексуальная. . ."
            elif KittyX.LikeWanda >= 800:
                ch_k "За последнее время мы стали довольно близки. . ."
            elif KittyX.LikeWanda >= 700:
                ch_k "Она[KittyX.like]очень хорошая подруга."
            elif KittyX.LikeWanda >= 600:
                ch_k "Мы[KittyX.like]подруги и все."
            elif KittyX.LikeWanda >= 500:
                ch_k "Ну, она[KittyX.like]не бесит."
            elif KittyX.LikeWanda >= 400:
                ch_k "Мы[KittyX.like]с ней особо-то и не встречались."
            elif KittyX.LikeWanda >= 300:
                ch_k "Лучше бы этой ведьмы тут не было."
            else:
                ch_k "Ты про эту шлюху?"
    else:
                ch_k "Я думаю. . . хотя нет, забудь."

    return

label Kitty_Monogamy:
        #called from Kitty_Settings to ask her not to hook up wiht other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in KittyX.Traits:
                    if KittyX.Thirst >= 60 and not ApprovalCheck(KittyX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ KittyX.FaceChange("sly",1)
                            if "mono" not in KittyX.DailyActions:
                                    $ KittyX.Statup("Obed", 90, -2)
                            ch_k "Я[KittyX.like]ценю твое участие, но я не хочу. . ."
                            return
                    elif ApprovalCheck(KittyX, 1100, "LO", TabM=0) and KittyX.Love >= KittyX.Obed:
                            #she cares
                            $ KittyX.FaceChange("sly",1)
                            if "mono" not in KittyX.DailyActions:
                                    $ KittyX.Statup("Love", 90, 1)
                            ch_k "А, ты о какой-то милашке?"
                            ch_k "Наверное, я смогу совладать с собой. . ."
                    elif ApprovalCheck(KittyX, 600, "O", TabM=0):
                            #she is obedient
                            $ KittyX.FaceChange("sly",1,Eyes="side")
                            ch_k "Если ты этого хочешь. . ."
                    else:
                            #she doesn't care
                            $ KittyX.FaceChange("sly",1,Brows="confused")
                            ch_k "Я буду общаться с кем захочу!"
                            return
                    if "mono" not in KittyX.DailyActions:
                            $ KittyX.Statup("Obed", 90, 3)
                    $ KittyX.AddWord(1,0,"mono") #Daily
                    $ KittyX.Traits.append("mono")
            "Не встречайся с другими девушками." if "mono" not in KittyX.Traits:
                    if ApprovalCheck(KittyX, 800, "O", TabM=0):
                            #she is obedient
                            $ KittyX.FaceChange("sly",1,Eyes="side")
                            ch_k "Ладно."
                    elif KittyX.Thirst >= 60 and not ApprovalCheck(KittyX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ KittyX.FaceChange("sly",1)
                            if "mono" not in KittyX.DailyActions:
                                    $ KittyX.Statup("Obed", 90, -2)
                            ch_k "Я[KittyX.like]ценю твое участие, но я не хочу. . ."
                            return
                    elif ApprovalCheck(KittyX, 500, "O", TabM=0):
                            #she is obedient
                            $ KittyX.FaceChange("sly",1,Eyes="side")
                            ch_k "Если ты этого хочешь. . ."
                    elif ApprovalCheck(KittyX, 1200, "LO", TabM=0):
                            #she cares
                            $ KittyX.FaceChange("sly",1)
                            ch_k "Тебе не кажется, что указывать невежливо?"
                            ch_k "Но ладно, я сделаю это для тебя. . ."
                    else:
                            #she doesn't care
                            $ KittyX.FaceChange("sly",1,Brows="confused")
                            ch_k "Я буду общаться с кем захочу!"
                            return
                    if "mono" not in KittyX.DailyActions:
                            $ KittyX.Statup("Obed", 90, 3)
                    $ KittyX.AddWord(1,0,"mono") #Daily
                    $ KittyX.Traits.append("mono")
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in KittyX.Traits:
                    if ApprovalCheck(KittyX, 650, "O", TabM=0):
                            $ KittyX.FaceChange("sly",1,Eyes="side")
                            ch_k "Хорошо, я поняла."
                    elif ApprovalCheck(KittyX, 800, "L", TabM=0):
                            $ KittyX.FaceChange("sly",1)
                            ch_k "С тобой у меня остается не так много времени на это. . ."
                            ch_k "Верно?"
                    else:
                            $ KittyX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in KittyX.DailyActions:
                                    $ KittyX.Statup("Love", 90, -2)
                            ch_k "Ты не владеешь моей киской!"
                    if "mono" not in KittyX.DailyActions:
                            $ KittyX.Statup("Obed", 90, 3)
                    if "mono" in KittyX.Traits:
                            $ KittyX.Traits.remove("mono")
                    $ KittyX.AddWord(1,0,"mono") #Daily
            "Неважно":
                pass
        return

# end Kitty monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Kitty_Jumped:
        #called from Kitty_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ KittyX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_k "Эм. . . Наверное?"
            "На будущее, можешь сначала спрашивать?" if "chill" not in KittyX.Traits:
                    if KittyX.Thirst >= 60 and not ApprovalCheck(KittyX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ KittyX.FaceChange("surprised",2)
                            if "chill" not in KittyX.DailyActions:
                                    $ KittyX.Statup("Obed", 90, -2)
                            ch_k "Ну, ты не уделяешь мне должного внимания!"
                            $ KittyX.FaceChange("angry",1,Eyes="side")
                            return
                    elif ApprovalCheck(KittyX, 900, "LO", TabM=0) and KittyX.Love >= KittyX.Obed:
                            #she cares
                            $ KittyX.FaceChange("sadside",1)
                            if "chill" not in KittyX.DailyActions:
                                    $ KittyX.Statup("Love", 90, 1)
                            ch_k "Извини, [KittyX.Petname]. . ."
                            ch_k "Я не могу держать себя в руках. . ."
                            ch_k "Но я постараюсь. . ."
                    elif ApprovalCheck(KittyX, 400, "O", TabM=0):
                            #she is obedient
                            $ KittyX.FaceChange("sly",1,Eyes="side")
                            ch_k "Я попытаюсь. . ."
                    else:
                            #she doesn't care
                            $ KittyX.FaceChange("sly",1)
                            ch_k "Я не могу держать себя в руках. . ."
                            return
                    if "chill" not in KittyX.DailyActions:
                            $ KittyX.Statup("Obed", 90, 3)
                    $ KittyX.AddWord(1,0,"chill") #Daily
                    $ KittyX.Traits.append("chill")
            "Больше так не делай." if "chill" not in KittyX.Traits:
                    if ApprovalCheck(KittyX, 900, "O", TabM=0):
                            #she is obedient
                            $ KittyX.FaceChange("sly",1,Eyes="side")
                            ch_k "Ладно."
                    elif KittyX.Thirst >= 60 and not ApprovalCheck(KittyX, 600, "O", TabM=0):
                            #she's too thirsty
                            $ KittyX.FaceChange("angry",1)
                            if "chill" not in KittyX.DailyActions:
                                    $ KittyX.Statup("Obed", 90, -2)
                            ch_k "Тогда уделяй мне больше внимания!"
                            return
                    elif ApprovalCheck(KittyX, 400, "O", TabM=0):
                            #she is obedient
                            $ KittyX.FaceChange("sly",1,Eyes="side")
                            ch_k "Хорошо. . ."
                    elif ApprovalCheck(KittyX, 500, "LO", TabM=0) and not ApprovalCheck(KittyX, 500, "I", TabM=0):
                            #she cares
                            $ KittyX.FaceChange("sly",1)
                            ch_k "Это слишком жестоко."
                            ch_k ". . . Но я постараюсь. . ."
                    else:
                            #she doesn't care
                            $ KittyX.FaceChange("sly",1,Brows="confused")
                            ch_k "Я пока не уверена. Время покажет. . ."
                            return
                    if "chill" not in KittyX.DailyActions:
                            $ KittyX.Statup("Obed", 90, 3)
                    $ KittyX.AddWord(1,0,"chill") #Daily
                    $ KittyX.Traits.append("chill")
            "Делай что хочешь.":
                    if ApprovalCheck(KittyX, 800, "L", TabM=0):
                            $ KittyX.FaceChange("sly",1)
                            ch_k "Принято. . ."
                    elif ApprovalCheck(KittyX, 700, "O", TabM=0):
                            $ KittyX.FaceChange("sly",1,Eyes="side")
                            ch_k "Конечно!"
                    else:
                            $ KittyX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in KittyX.DailyActions:
                                    $ KittyX.Statup("Love", 90, -2)
                            ch_k "Я не знаю."
                            ch_k "Если бы у меня еще было много времени."
                            ch_k "Ладно, посмотрим."
                    if "chill" not in KittyX.DailyActions:
                            $ KittyX.Statup("Obed", 90, 3)
                    if "chill" in KittyX.Traits:
                            $ KittyX.Traits.remove("chill")
                    $ KittyX.AddWord(1,0,"chill") #Daily
            "Эм, неважно.":
                pass
        return

# end Kitty jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start kitty hungry //////////////////////////////////////////////////////////
label Kitty_Hungry:
    if KittyX.Chat[3]:
        ch_k "Знаешь, кисоньке нравится ее молочко. . ."
    elif KittyX.Chat[2]:
        if not Player.Male:
            ch_k "Знаешь, в этой твоей сыворотке есть что-то особенное. Ты должна продавать ее!"
        else:
            ch_k "Знаешь, в этой твоей сыворотке есть что-то особенное. Ты должен продавать ее!"
    else:
        ch_k "Знаешь, кисоньке нравится ее молочко. . ."
    $ KittyX.Traits.append("hungry")
return


# end kitty hungry //////////////////////////////////////////////////////////

# Kitty Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Kitty_SexChat:
    $ Line = "Ага, о чем ты хочешь поговорить?" if not Line else Line
    while True:
            menu:
                ch_k "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in KittyX.DailyActions:
                        if not Player.Male:
                            ch_k "Ага, я знаю. Ты уже говорила мне об этом."
                        else:
                            ch_k "Ага, я знаю. Ты уже говорил мне об этом."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ KittyX.FaceChange("sly")
                                        if KittyX.PlayerFav == "sex":
                                            $ KittyX.Statup("Lust", 80, 5)
                                            ch_k "Ага, я знаю. . ."
                                        elif KittyX.Favorite == "sex":
                                            $ KittyX.Statup("Love", 90, 5)
                                            $ KittyX.Statup("Lust", 80, 10)
                                            ch_k "Мне тоже это очень нравится!"
                                        elif KittyX.Sex >= 5:
                                            ch_k "Ну, я не против."
                                        elif not KittyX.Sex:
                                            $ KittyX.FaceChange("perplexed")
                                            ch_k "Кто с тобой спит? Мисс Фрост?!"
                                        else:
                                            $ KittyX.FaceChange("bemused")
                                            ch_k "Хихи, эм, ага, это приятно. . ."
                                        $ KittyX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ KittyX.FaceChange("sly")
                                        if KittyX.PlayerFav == "anal":
                                            $ KittyX.Statup("Lust", 80, 5)
                                            if not Player.Male:
                                                ch_k "Ты уже говорила. . ."
                                            else:
                                                ch_k "Ты уже говорил. . ."
                                        elif KittyX.Favorite == "anal":
                                            $ KittyX.Statup("Love", 90, 5)
                                            $ KittyX.Statup("Lust", 80, 10)
                                            ch_k "Мне тоже нравится!"
                                        elif KittyX.Anal >= 10:
                                            ch_k "Ага, это. . . приятно. . ."
                                        elif not KittyX.Anal:
                                            $ KittyX.FaceChange("perplexed")
                                            ch_k "Кто с тобой спит? Мисс Фрост?!"
                                        else:
                                            $ KittyX.FaceChange("bemused",Eyes="side")
                                            ch_k "Хихи, ага, эм, ладно. . ."
                                        $ KittyX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ KittyX.FaceChange("sly")
                                        if KittyX.PlayerFav == "blow":
                                            $ KittyX.Statup("Lust", 80, 3)
                                            ch_k "Ага, я знаю."
                                        elif KittyX.Favorite == "blow":
                                            $ KittyX.Statup("Love", 90, 5)
                                            $ KittyX.Statup("Lust", 80, 5)
                                            ch_k "Я люблю твой член!"
                                        elif KittyX.Blow >= 10:
                                            ch_k "Да, ты довольно вкусный."
                                        elif not KittyX.Blow:
                                            $ KittyX.FaceChange("perplexed")
                                            ch_k "Кто сосет твой член?! Мисс Фрост?!"
                                        else:
                                            $ KittyX.FaceChange("bemused")
                                            ch_k "Я. . . начинаю привыкать к его вкусу. . ."
                                        $ KittyX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ KittyX.FaceChange("sly")
                                        if KittyX.PlayerFav == "cun":
                                            $ KittyX.Statup("Lust", 80, 3)
                                            ch_k "Ага, я знаю."
                                        elif KittyX.Favorite == "cun":
                                            $ KittyX.Statup("Love", 90, 5)
                                            $ KittyX.Statup("Lust", 80, 5)
                                            ch_k "Я люблю твою киску!"
                                        elif KittyX.CUN >= 10:
                                            ch_k "Да, ты довольно вкусная."
                                        elif not KittyX.CUN:
                                            $ KittyX.FaceChange("perplexed")
                                            ch_k "Кто тебе лижет?! Мисс Фрост?!"
                                        else:
                                            $ KittyX.FaceChange("bemused")
                                            ch_k "Я. . . начинаю привыкать к ее вкусу. . ."
                                        $ KittyX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ KittyX.FaceChange("sly")
                                        if KittyX.PlayerFav == "titjob":
                                            $ KittyX.Statup("Lust", 80, 5)
                                            ch_k "Ага, ты уже об этом говорил. . ."
                                        elif KittyX.Favorite == "titjob":
                                            $ KittyX.Statup("Love", 90, 5)
                                            $ KittyX.Statup("Lust", 80, 7)
                                            ch_k "Ага, мне тоже нравится. . ."
                                        elif KittyX.Tit >= 10:
                                            ch_k "Это, безусловно, интересный опыт . . ."
                                        elif not KittyX.Tit:
                                            $ KittyX.FaceChange("perplexed")
                                            ch_k "Кто дрочил тебе грудью? Мисс фрост, да?!"
                                        else:
                                            $ KittyX.FaceChange("bemused")
                                            ch_k "Мило с твоей стороны это упомянуть. . ."
                                            $ KittyX.Statup("Love", 80, 5)
                                            $ KittyX.Statup("Inbt", 50, 10)
                                        $ KittyX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ KittyX.FaceChange("sly")
                                        if KittyX.PlayerFav == "foot":
                                            $ KittyX.Statup("Lust", 80, 5)
                                            if not Player.Male:
                                                ch_k "Да, ты уже говорила это. . ."
                                            else:
                                                ch_k "Да, ты уже говорил это. . ."
                                        elif KittyX.Favorite == "foot":
                                            $ KittyX.Statup("Love", 90, 5)
                                            $ KittyX.Statup("Lust", 80, 7)
                                            ch_k "Приятные ощущения. . ."
                                        elif KittyX.Foot >= 10:
                                            ch_k "Мне это тоже нравится . . ."
                                        elif not KittyX.Foot:
                                            $ KittyX.FaceChange("perplexed")
                                            ch_k "Кто игрался с тобой ножками? Мисс Фрост?!"
                                        else:
                                            $ KittyX.FaceChange("bemused")
                                            ch_k "Ага, это приятно. . ."
                                        $ KittyX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ KittyX.FaceChange("sly")
                                        if KittyX.PlayerFav == "hand":
                                            $ KittyX.Statup("Lust", 80, 5)
                                            ch_k "Да, ты уже говорил это. . ."
                                        elif KittyX.Favorite == "hand":
                                            $ KittyX.Statup("Love", 90, 5)
                                            $ KittyX.Statup("Lust", 80, 7)
                                            ch_k "Он комфортно лежит в руке. . ."
                                        elif KittyX.Hand >= 10:
                                            ch_k "Мне это тоже нравится . . ."
                                        elif not KittyX.Hand:
                                            $ KittyX.FaceChange("perplexed")
                                            ch_k "Кто дрочил тебе? Мисс Фрост?!"
                                        else:
                                            $ KittyX.FaceChange("bemused")
                                            ch_k "Ага, это приятно. . ."
                                        $ KittyX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ KittyX.FaceChange("sly")
                                        if KittyX.PlayerFav == "finger":
                                            $ KittyX.Statup("Lust", 80, 5)
                                            ch_k "Да, ты уже говорила это. . ."
                                        elif KittyX.Favorite == "finger":
                                            $ KittyX.Statup("Love", 90, 5)
                                            $ KittyX.Statup("Lust", 80, 7)
                                            ch_k "Она приятная на ощупь. . ."
                                        elif KittyX.Finger >= 10:
                                            ch_k "Мне это тоже нравится . . ."
                                        elif not KittyX.Finger:
                                            $ KittyX.FaceChange("perplexed")
                                            ch_k "Кто ласкал тебя? Мисс Фрост?!"
                                        else:
                                            $ KittyX.FaceChange("bemused")
                                            ch_k "Ага, это приятно. . ."
                                        $ KittyX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = KittyX.FondleB + KittyX.FondleT + KittyX.SuckB + KittyX.Hotdog
                                        $ KittyX.FaceChange("sly")
                                        if KittyX.PlayerFav == "fondle":
                                            $ KittyX.Statup("Lust", 80, 3)
                                            ch_k "Ага, думаю, все уже поняли. . ."
                                        elif KittyX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ KittyX.Statup("Love", 90, 5)
                                            $ KittyX.Statup("Lust", 80, 5)
                                            ch_k "Мне нравится, когда ты прикасаешься ко мне. . ."
                                        elif Cnt >= 10:
                                            ch_k "Ага, это очень приятно. . ."
                                        elif not Cnt:
                                            $ KittyX.FaceChange("perplexed")
                                            if not Player.Male:
                                                ch_k "Кого это ты лапала? Мисс Фрост?!"
                                            else:
                                                ch_k "Кого это ты лапал? Мисс Фрост?!"
                                        else:
                                            $ KittyX.FaceChange("bemused")
                                            ch_k "Мне нравятся эти ощущения. . ."
                                        $ KittyX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ KittyX.FaceChange("sly")
                                        if KittyX.PlayerFav == "kiss you":
                                            $ KittyX.Statup("Love", 90, 3)
                                            ch_k "Как романтично. . ."
                                        elif KittyX.Favorite == "kiss you":
                                            $ KittyX.Statup("Love", 90, 5)
                                            $ KittyX.Statup("Lust", 80, 5)
                                            ch_k "Ммм, твой вкус на моих губах. . ."
                                        elif KittyX.Kissed >= 10:
                                            ch_k "Я тоже люблю тебя целовать . . ."
                                        elif not KittyX.Kissed:
                                            $ KittyX.FaceChange("perplexed")
                                            ch_k "С кем это ты целуешься? С мисс Фрост?!"
                                        else:
                                            $ KittyX.FaceChange("bemused")
                                            ch_k "Мне тоже нравится целовать тебя. . ."
                                        $ KittyX.PlayerFav = "kiss you"

                        $ KittyX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(KittyX, 800):
                                        $ KittyX.FaceChange("perplexed")
                                        ch_k "Невежливо спрашивать девушку об этом."
                                else:
                                        if KittyX.SEXP >= 50:
                                            $ KittyX.FaceChange("sly")
                                            if not Player.Male:
                                                ch_k "Ты должна знать это. . ."
                                            else:
                                                ch_k "Ты должен знать это. . ."
                                        else:
                                            $ KittyX.FaceChange("bemused")
                                            $ KittyX.Eyes = "side"
                                            ch_k "Хмм, Я не знаю. . ."


                                        if not KittyX.Favorite or KittyX.Favorite == "kiss you":
                                            ch_k "Мне нравится, когда мы целуемся. . ."
                                        elif KittyX.Favorite == "anal":
                                            if KittyX.Anal >= 10:
                                                ch_k "Мне нравится, когда ты. . . трахаешь меня в попку."
                                            else:
                                                ch_k "Мне нравится. . . в попку."
                                        elif KittyX.Favorite == "lick ass":
                                                ch_k "Мне нравится, когда ты вылизываешь мою. . . попку."
                                        elif KittyX.Favorite == "insert ass":
                                                ch_k "Мне нравится, когда ты играешься пальцем. . . с моей попкой."
                                        elif KittyX.Favorite == "sex":
                                                ch_k "Мне нравится, когда ты трахаешь меня."
                                        elif KittyX.Favorite == "lick pussy":
                                                ch_k "Мне нравится, когда ты лижешь мою киску."
                                        elif KittyX.Favorite == "fondle pussy":
                                                ch_k "Мне нравится, когда ты играешься с моей киской."
                                        elif KittyX.Favorite == "blow":
                                                ch_k "Мне, вроде как, нравится сосать твой член."
                                        elif KittyX.Favorite == "cun":
                                                ch_k "Мне, вроде как, нравится вылизывать твою киску."
                                        elif KittyX.Favorite == "tit":
                                                ch_k "Я не против использовать свои сиськи."
                                        elif KittyX.Favorite == "foot":
                                                ch_k "Я, вроде как, люблю дрочить тебе ногам."
                                        elif KittyX.Favorite == "hand":
                                                ch_k "Мне нравится дрочить тебе."
                                        elif KittyX.Favorite == "finger":
                                                ch_k "Мне нравится ласкать твою киску."
                                        elif KittyX.Favorite == "hotdog":
                                                ch_k "Мне нравится, когда ты трешься о меня."
                                        elif KittyX.Favorite == "suck breasts":
                                                ch_k "Мне нравится, когда ты сосешь мои сиськи."
                                        elif KittyX.Favorite == "fondle breasts":
                                                ch_k "Мне нравится, когда ты ласкаешь мои сиськи."
                                        elif KittyX.Favorite == "fondle thighs":
                                                ch_k "Мне нравится, когда ты массируешь мои ножки."
                                        else:
                                                ch_k "Я даже не знаю. . ."

                                # End Kitty's favorite things.

                "Не болтай так много во время секса." if "vocal" in KittyX.Traits:
                        if "setvocal" in KittyX.DailyActions:
                            $ KittyX.FaceChange("perplexed")
                            ch_k "Мы уже говорили об этом."
                        else:
                            if ApprovalCheck(KittyX, 1000) and KittyX.Obed <= KittyX.Love:
                                $ KittyX.FaceChange("bemused")
                                $ KittyX.Statup("Obed", 90, 1)
                                ch_k "Ну, думаю, я могу быть потише. . ."
                                $ KittyX.Traits.remove("vocal")
                            elif ApprovalCheck(KittyX, 700, "O"):
                                $ KittyX.FaceChange("sadside")
                                $ KittyX.Statup("Obed", 90, 1)
                                ch_k "Эм, ладно, [KittyX.Petname]."
                                $ KittyX.Traits.remove("vocal")
                            elif ApprovalCheck(KittyX, 600):
                                $ KittyX.FaceChange("sly")
                                $ KittyX.Statup("Love", 90, -3)
                                $ KittyX.Statup("Obed", 50, -1)
                                $ KittyX.Statup("Inbt", 90, 5)
                                ch_k "Ты этого хочешь, не я, [KittyX.Petname]."
                            else:
                                $ KittyX.FaceChange("angry")
                                $ KittyX.Statup("Love", 90, -5)
                                $ KittyX.Statup("Obed", 60, -3)
                                $ KittyX.Statup("Inbt", 90, 10)
                                ch_k "О, неужели я настолько {i}болтлива{/i}, когда отшиваю тебя?"

                            $ KittyX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in KittyX.Traits:
                        if "setvocal" in KittyX.DailyActions:
                            $ KittyX.FaceChange("perplexed")
                            ch_k "Мы уже говорили об этом."
                        else:
                            if ApprovalCheck(KittyX, 1000) and KittyX.Obed <= KittyX.Love:
                                $ KittyX.FaceChange("sly")
                                $ KittyX.Statup("Obed", 90, 2)
                                ch_k "Хмм, ладно. . ."
                                $ KittyX.Traits.append("vocal")
                            elif ApprovalCheck(KittyX, 700, "O"):
                                $ KittyX.FaceChange("sadside")
                                $ KittyX.Statup("Obed", 90, 2)
                                ch_k "Думаю, можно попробовать, [KittyX.Petname]."
                                $ KittyX.Traits.append("vocal")
                            elif ApprovalCheck(KittyX, 600):
                                $ KittyX.FaceChange("sly")
                                $ KittyX.Statup("Obed", 90, 3)
                                ch_k "Думаю, можно, [KittyX.Petname]."
                                $ KittyX.Traits.append("vocal")
                            else:
                                $ KittyX.FaceChange("angry")
                                $ KittyX.Statup("Inbt", 90, 5)
                                ch_k "Хмм, насчет этого не уверена."

                            $ KittyX.DailyActions.append("setvocal")
                        # End Kitty Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in KittyX.Traits:
                        if "initiative" in KittyX.DailyActions:
                            $ KittyX.FaceChange("perplexed")
                            ch_k "Мы уже говорили об этом."
                        else:
                            if ApprovalCheck(KittyX, 1000) and KittyX.Obed <= KittyX.Love:
                                $ KittyX.FaceChange("bemused")
                                $ KittyX.Statup("Obed", 90, 1)
                                ch_k "Хихи, если ты настаиваешь. . ."
                                $ KittyX.Traits.append("passive")
                            elif ApprovalCheck(KittyX, 700, "O"):
                                $ KittyX.FaceChange("sadside")
                                $ KittyX.Statup("Obed", 90, 1)
                                ch_k "Я постараюсь держать себя в руках, [KittyX.Petname]."
                                $ KittyX.Traits.append("passive")
                            elif ApprovalCheck(KittyX, 600):
                                $ KittyX.FaceChange("sly")
                                $ KittyX.Statup("Love", 90, -3)
                                $ KittyX.Statup("Obed", 50, -1)
                                $ KittyX.Statup("Inbt", 90, 5)
                                ch_k "Ты этого хочешь, не я, [KittyX.Petname]."
                            else:
                                $ KittyX.FaceChange("angry")
                                $ KittyX.Statup("Love", 90, -5)
                                $ KittyX.Statup("Obed", 60, -3)
                                $ KittyX.Statup("Inbt", 90, 10)
                                ch_k "Если мне когда-нибудь этого захочется."

                            $ KittyX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in KittyX.Traits:
                        if "initiative" in KittyX.DailyActions:
                                $ KittyX.FaceChange("perplexed")
                                ch_k "Мы уже говорили об этом."
                        else:
                            if ApprovalCheck(KittyX, 1000) and KittyX.Obed <= KittyX.Love:
                                $ KittyX.FaceChange("bemused")
                                $ KittyX.Statup("Obed", 90, 1)
                                ch_k "Хихи, посмотрим, что можно сделать. . ."
                                $ KittyX.Traits.remove("passive")
                            elif ApprovalCheck(KittyX, 700, "O"):
                                $ KittyX.FaceChange("sadside")
                                $ KittyX.Statup("Obed", 90, 1)
                                ch_k "Думаю, с этим я справлюсь, [KittyX.Petname]."
                                $ KittyX.Traits.remove("passive")
                            elif ApprovalCheck(KittyX, 600):
                                $ KittyX.FaceChange("sly")
                                $ KittyX.Statup("Obed", 90, 3)
                                ch_k "Я могу попробовать, [KittyX.Petname]."
                                $ KittyX.Traits.remove("passive")
                            else:
                                $ KittyX.FaceChange("angry")
                                $ KittyX.Statup("Inbt", 90, 5)
                                ch_k "Ты мне не указ!"

                            $ KittyX.DailyActions.append("initiative")

                "О том, как ты накидываешься" if "jumped" in KittyX.History:
                        call Kitty_Jumped
                "О твоей мастурбации":
                        call NoFap(KittyX)

                "Всегда носи с вибратор" if "dailyvibe" not in KittyX.Traits:
                        call Daily_Vibrator(KittyX)
                "Перестань всегда носить вибратор" if "dailyvibe" in KittyX.Traits:
                        ch_k "Ладно. . ."
                        $ KittyX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи с собой анальную пробку" if "dailyplug" not in KittyX.Traits:
                        call Daily_Plug(KittyX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in KittyX.Traits:
                        ch_k "Ладно. . ."
                        $ KittyX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Неважно" if Line == "Ага, о чем ты хочешь поговорить?":
                        return
                "На этом все." if Line != "Ага, о чем ты хочешь поговорить?":
                        return
            if Line == "Ага, о чем ты хочешь поговорить?":
                $ Line = "Что-нибудь еще?"
    return
# End Kitty Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Kitty Chitchat /////////////////// #Work in progress
label Kitty_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if KittyX not in Digits:
                if ApprovalCheck(KittyX, 500, "L") or ApprovalCheck(KittyX, 250, "I"):
                    ch_k "Знаешь, я ведь так и не успела дать тебе свой номер. Вот, держи."
                    $ Digits.append(KittyX)
                    return
                elif ApprovalCheck(KittyX, 250, "O"):
                    ch_k "Слушай, тебе, наверное, стоит взять мой номер. Вот, держи."
                    $ Digits.append(KittyX)
                    return

        if "hungry" not in KittyX.Traits and (KittyX.Swallow + KittyX.Chat[2]) >= 10 and KittyX.Loc == bg_current:  #She's swallowed a lot
                    call Kitty_Hungry
                    return
        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(KittyX, 800, "I")):
                    if KittyX.Loc == bg_current and KittyX.Thirst >= 30 and "refused" not in KittyX.DailyActions and "quicksex" not in KittyX.DailyActions:
                            $ KittyX.FaceChange("smile",2,Brows="sad")
                            ch_k "Слушай, эм . . . ты не против. . ."
                            ch_k ". . . заняться сексом?"
                            call Quick_Sex(KittyX)
                            return

#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in KittyX.DailyActions:
#            $ Options.append("caught")
        if KittyX.Event[0] and "key" not in KittyX.Chat:
            $ Options.append("key")
        if "lover" in KittyX.Petnames and ApprovalCheck(KittyX, 900, "L"): # luvy dovey
            $ Options.append("luv")
        if "Kate" in KittyX.Names and "Katherine" not in KittyX.Names:
            #You don't know Kitty's full name
            $ Options.append("Katherine")
        if KittyX.Lvl >= 3 and "Shadowcat" not in KittyX.Names:
            #You don't know Kitty's full name
            $ Options.append("Shadowcat")

        if "mandrill" in Player.Traits and "cologne chat" not in KittyX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in KittyX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in KittyX.DailyActions:
            $ Options.append("corruption")

        if "seenpeen" in KittyX.History:
            $ Options.append("seenpeen")
        if "topless" in KittyX.History:
            $ Options.append("topless")
        if "bottomless" in KittyX.History:
            $ Options.append("bottomless")

        if KittyX.Date >= 1 and bg_current != "bg restaurant":
            #if you've dated before
            $ Options.append("dated")
        if "cheek" in KittyX.DailyActions and "cheek" not in KittyX.Chat:
            #If you've touched her cheek today
            $ Options.append("cheek")
        if KittyX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "kappa" in Player.History:
            $ Options.append("kappa")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in KittyX.DailyActions and (Player.Male or "girltalk" in KittyX.History):
            #If you've caught Kitty showering today
            $ Options.append("showercaught")
        if "fondle breasts" in KittyX.DailyActions or "fondle pussy" in KittyX.DailyActions or "fondle ass" in KittyX.DailyActions:
            #If you've fondled Kitty today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in KittyX.Inventory and "256 Shades of Grey" in KittyX.Inventory and "Avengers Tower Penthouse" in KittyX.Inventory:
            #If you've given Kitty the books
            if "book" not in KittyX.Chat:
                $ Options.append("booked")
        if "lace bra" in KittyX.Inventory or "lace panties" in KittyX.Inventory:
            #If you've given Kitty the lingerie
            if "lingerie" not in KittyX.Chat:
                $ Options.append("lingerie")
        if KittyX.Hand and Player.Male:
            #If Kitty's given a handjob
            $ Options.append("handy")
        if KittyX.Blow and Player.Male:
            #If Kitty's given a blowjob
            $ Options.append("blow")
        if KittyX.Swallow:
            #If Kitty's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in KittyX.DailyActions or "painted" in KittyX.DailyActions:
            #If Kitty's been facialed
            $ Options.append("facial")
        if KittyX.Sleep:
            #If Kitty's slept over
            $ Options.append("sleep")
        if (KittyX.CreamP or KittyX.CreamA) and Player.Male:
            #If Kitty's been creampied
            $ Options.append("creampie")
        if KittyX.Sex or KittyX.Anal:
            #If Kitty's been sexed
            $ Options.append("sexed")
        if KittyX.Anal:
            #If Kitty's been analed
            $ Options.append("anal")

#        if not KittyX.Chat[0] and KittyX.Sex:
#            $ Options.append("virgin")

        if (bg_current == "bg kitty" or bg_current == "bg player") and "relationship" not in KittyX.DailyActions:
            if "lover" not in KittyX.Petnames and KittyX.Love >= 950 and KittyX.Event[6] != 20: # KittyX.Event[6]
                $ Options.append("lover?")
            elif "sir" not in KittyX.Petnames and KittyX.Obed >= 500 and "sir" not in KittyX.History: # KittyX.Event[7]
                $ Options.append("sir?")
            elif "daddy" not in KittyX.Petnames and ApprovalCheck(KittyX, 750, "L") and ApprovalCheck(KittyX, 500, "O") and ApprovalCheck(KittyX, 500, "I"): # KittyX.Event[5]
                $ Options.append("daddy?")
            elif "master" not in KittyX.Petnames and KittyX.Obed >= 800 and "sir" in KittyX.Petnames and "master" not in KittyX.History: # KittyX.Event[8]
                $ Options.append("master?")
            elif "sex friend" not in KittyX.Petnames and ApprovalCheck(KittyX, 500, "I"): # KittyX.Event[9]
                $ Options.append("sexfriend?")


        if not ApprovalCheck(KittyX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ KittyX.DailyActions.append("cologne chat")
        $ KittyX.FaceChange("confused")
        ch_k "(нюх-нюх). . . это. . . шимпанзе? . . ."
        $ KittyX.FaceChange("perplexed", 1)
        ch_k ". . . но не простое, а[KittyX.like]{i}сексуальное{/i} шимпанзе?"
    elif Options[0] == "purple":
        $ KittyX.DailyActions.append("cologne chat")
        $ KittyX.FaceChange("sly",1)
        ch_k "(нюх-нюх). . . хм, что это за запах? . ."
        ch_k ". . . могу я что-нибудь сделать для тебя?"
    elif Options[0] == "corruption":
        $ KittyX.DailyActions.append("cologne chat")
        $ KittyX.FaceChange("confused")
        ch_k "(нюх-нюх). . . довольно давящий аромат. . ."
        $ KittyX.FaceChange("sly")
        ch_k ". . . похоже, я не смогу держать себя в руках. . ."

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in KittyX.Chat:
                    ch_k "Нам нужно избавиться от привычки попадаться."
                    if not ApprovalCheck(KittyX, 500, "I"):
                         ch_k "Ну, или нет. . ."
            else:
                    ch_k "Мне не нравится, что меня постоянно вызывают в кабинет Профессора."
                    if not ApprovalCheck(KittyX, 500, "I"):
                        ch_k "Я больше не знаю, как заниматься подобным на людях."
                    else:
                        ch_k "Хотя это очень возбуждает. . ."
                    $ KittyX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if KittyX.SEXP <= 15:
                ch_k "Я рада, что теперь у тебя есть мой ключ, только не используй его по пустякам. . ."
            else:
                ch_k "Я рада, что теперь у тебя есть мой ключ, думаю, тебе стоит как-нибудь. . .  \"удивить\" меня. . ."
            $ KittyX.Chat.append("key")

    elif Options[0] == "cheek":
            #Kitty's response to having her cheek touched.
            if not Player.Male:
                ch_k "Итак, [KittyX.Petname]. . . помнишь, как ты ранее[KittyX.like]погладила меня по щеке?"
            else:
                ch_k "Итак, [KittyX.Petname]. . . помнишь, как ты ранее[KittyX.like]погладил меня по щеке?"
            ch_p "Да? Все было нормально?"
            $ KittyX.FaceChange("smile",1)
            ch_k "Больше, чем просто {i}нормально{/i}."
            $ KittyX.Chat.append("cheek")

    elif Options[0] == "dated":
            #Kitty's response to having gone on a date with the Player.
            ch_k "Приветик, [KittyX.Petname]. [KittyX.Like]я вчера очень хорошо провела вечер.  Мы должны как-нибудь повторить."

    elif Options[0] == "kissed":
            #Kitty's response to having been kissed by the Player.
            $ KittyX.FaceChange("sly",1)
            ch_k "[KittyX.Like]тебе кто-нибудь уже говорил, как хорошо ты целуешься, [KittyX.Petname]?"
            menu:
                extend ""
                "Хех. . . когда все делаешь как надо, ты хорош.":
                        $ KittyX.FaceChange("smile",1)
                        ch_k "Думаю, тебе стоит почаще показывать мне {i}как{/i}[KittyX.like]правильно."
                "Нет. Ты правда так думаешь?":
                        if not Player.Male:
                            ch_k "Да. Ты хороша и[KittyX.Like]даже {i}очень{/i}."
                        else:
                            ch_k "Да. Ты хорош и[KittyX.Like]даже {i}очень{/i}."

    elif Options[0] == "dangerroom":
            #Kitty's response to Player working out in the Danger Room while Kitty is present
            $ KittyX.FaceChange("sly",1)
            if not Player.Male:
                ch_k "Слушай, [KittyX.Petname]. Я как-то видела, как ты тренируешься в комнате Опасности. Ты[KittyX.like]{i}такая{/i} милая в своей форме Людей-Икс!"
            else:
                ch_k "Слушай, [KittyX.Petname]. Я как-то видела, как ты тренируешься в комнате Опасности. Ты[KittyX.like]{i}такой{/i} милый в своей форме Людей-Икс!"

    elif Options[0] == "showercaught":
            #Kitty's response to being caught in the shower.
            if "shower" in KittyX.Chat:
                ch_k "Надеюсь, тебе понравился вид в прошлый раз. . ."
            else:
                ch_k "Ты за всеми подглядываешь в душевой. . . или только[KittyX.like]за мной?"
                $ KittyX.Chat.append("shower")
                menu:
                    extend ""
                    "Это чистая случайность! Клянусь!":
                            $ KittyX.Statup("Love", 50, 5)
                            $ KittyX.Statup("Love", 90, 2)
                            if ApprovalCheck(KittyX, 1200):
                                $ KittyX.FaceChange("sly",1)
                                ch_k "Да? {i}Возможно{/i}, тебе стоит[KittyX.like]почаще попадать в такие случайности."
                            $ KittyX.FaceChange("smile")
                            ch_k "Все нормально, [KittyX.Petname]. Все ошибаются. . . иногда."
                    "Только за тобой.":
                            $ KittyX.Statup("Obed", 40, 5)
                            if ApprovalCheck(KittyX, 1000) or ApprovalCheck(KittyX, 700, "L"):
                                    $ KittyX.Statup("Love", 90, 3)
                                    $ KittyX.FaceChange("sly",1)
                                    ch_k "Ты знаешь, как заставить девушку почувствовать себя особенной, [KittyX.Petname]."
                            else:
                                    $ KittyX.Statup("Love", 70, -5)
                                    $ KittyX.FaceChange("angry")
                                    if not Player.Male:
                                        ch_k "Ты знала, что иногда бываешь {i}очень{/i} жуткой, а, [Player.Name]?"
                                    else:
                                        ch_k "Ты знал, что иногда бываешь {i}очень{/i} жутким, а, [Player.Name]?"
                    "Я заглянула умышленно. Но я ни о чем не жалею." if not Player.Male:
                            if ApprovalCheck(KittyX, 1200):
                                    $ KittyX.Statup("Love", 90, 3)
                                    $ KittyX.Statup("Obed", 70, 10)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    $ KittyX.FaceChange("sly",1)
                                    ch_k "Хмм. . . в следующий раз нам придется[KittyX.like]воспользоваться моментом."
                            elif ApprovalCheck(KittyX, 800):
                                    $ KittyX.Statup("Obed", 60, 5)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    $ KittyX.FaceChange("perplexed",2)
                                    ch_k "Каког-. . . эм. . . ладно?"
                                    $ KittyX.Blush = 1
                            else:
                                    $ KittyX.Statup("Love", 50, -10)
                                    $ KittyX.Statup("Love", 80, -10)
                                    $ KittyX.Statup("Obed", 50, 10)
                                    $ KittyX.FaceChange("angry")
                                    ch_k "Знаешь, ты иногда {i}такая{/i} жуткая, [Player.Name]."
                    "Я заглянул умышленно. Но я ни о чем не жалею." if Player.Male:
                            if ApprovalCheck(KittyX, 1200):
                                    $ KittyX.Statup("Love", 90, 3)
                                    $ KittyX.Statup("Obed", 70, 10)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    $ KittyX.FaceChange("sly",1)
                                    ch_k "Хмм. . . в следующий раз нам придется[KittyX.like]воспользоваться моментом."
                            elif ApprovalCheck(KittyX, 800):
                                    $ KittyX.Statup("Obed", 60, 5)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    $ KittyX.FaceChange("perplexed",2)
                                    ch_k "Каког-. . . эм. . . ладно?"
                                    $ KittyX.Blush = 1
                            else:
                                    $ KittyX.Statup("Love", 50, -10)
                                    $ KittyX.Statup("Love", 80, -10)
                                    $ KittyX.Statup("Obed", 50, 10)
                                    $ KittyX.FaceChange("angry")
                                    ch_k "Знаешь, ты иногда {i}такой{/i} жуткий, [Player.Name]."

    elif Options[0] == "fondled":
            #Kitty's response to being felt up.
            if KittyX.FondleB + KittyX.FondleP + KittyX.FondleA >= 15:
                ch_k "Я хочу почувствовать твои прикосновения."
            else:
                if not Player.Male:
                    ch_k "Помнишь, как ты ранее прикасалась ко мне? Я могу[KittyX.like]и привыкнуть к твоим прикосновениям."
                else:
                    ch_k "Помнишь, как ты ранее прикасался ко мне? Я могу[KittyX.like]и привыкнуть к твоим прикосновениям."

    elif Options[0] == "booked":
            #Kitty's response after a Player gives her the books from the shop.
            if not Player.Male:
                ch_k "Итак. . . Я[KittyX.like]прочитала книги, которые ты мне подарила."
            else:
                ch_k "Итак. . . Я[KittyX.like]прочитала книги, которые ты мне подарил."
            menu:
                extend ""
                "Да? Они тебе понравились?":
                        $ KittyX.FaceChange("sly",2)
                        ch_k "Они[KittyX.like]. . .{i}интересные{/i}."
                "Хорошо. Пожалуй, ты могла бы чему-нибудь из них научиться.":
                        $ KittyX.Statup("Love", 90, -3)
                        $ KittyX.Statup("Obed", 70, 5)
                        $ KittyX.Statup("Inbt", 50, 5)
                        $ KittyX.FaceChange("angry")
                        ch_k "Наверное, {i}ты{/i} никогда этого не узнаешь."
            $ KittyX.Blush = 1
            $ KittyX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Kitty's response to being given lingerie.
            $ KittyX.FaceChange("sly",2)
            if not Player.Male:
                ch_k "[KittyX.Petname], Я хотела еще раз поблагодарить тебя за. . .{i}вещи{/i}, которые ты мне подарила. Они такие милые!"
            else:
                ch_k "[KittyX.Petname], Я хотела еще раз поблагодарить тебя за. . .{i}вещи{/i}, которые ты мне подарил. Они такие милые!"
            $ KittyX.Blush = 1
            $ KittyX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Kitty's response after giving the Player a handjob.
            $ KittyX.FaceChange("sly",2)
            ch_k "Я тут вспомнила, как на днях я[KittyX.like]ласкала твой член. . ."
            ch_k "Видел бы ты в тот момент свое лицо."
            $ KittyX.Blush = 1

    elif Options[0] == "blow":
            if "blow" not in KittyX.Chat:
                    #Kitty's response after giving the Player a blowjob.
                    $ KittyX.FaceChange("sly",2)
                    ch_k "Так вот. . . эммм, ответишь мне честно, [KittyX.Petname]?"
                    ch_k "Тебе было хорошо, когда я. . . взяла твою головку в рот?"
                    ch_k "Просто, мне было трудно заглотить его полностью."
                    menu:
                        extend ""
                        "Ты была великолепна.":
                                    $ KittyX.Statup("Love", 90, 5)
                                    $ KittyX.Statup("Inbt", 60, 10)
                                    $ KittyX.FaceChange("sexy",1)
                                    ch_k "Замечательно. Потому что мне не терпится попробовать снова."
                        "Честно? Все было хорошо. . . но, думаю, тебе не помешает еще немного попрактиковаться.":
                                if ApprovalCheck(KittyX, 300, "I") or not ApprovalCheck(KittyX, 800):
                                    $ KittyX.Statup("Love", 90, -5)
                                    $ KittyX.Statup("Obed", 60, 10)
                                    $ KittyX.Statup("Inbt", 50, 10)
                                    $ KittyX.FaceChange("perplexed",1)
                                    ch_k "Да? Ну тогда мне стоит немного потренироваться, прежде чем мы повторим."
                                else:
                                    $ KittyX.Statup("Obed", 70, 15)
                                    $ KittyX.Statup("Inbt", 50, 5)
                                    $ KittyX.FaceChange("sexy",1)
                                    ch_k "Да? Ну, тогда, [KittyX.Petname], я с нетерпением жду нашей следующей тренировки."
                        "Угу, если бы мне нравились стремные звуки и шкрябанье зубов по члену, но это далеко не так.":
                                $ KittyX.Statup("Love", 90, -10)
                                $ KittyX.Statup("Obed", 60, 10)
                                $ KittyX.FaceChange("angry",2)
                                ch_k "Ну, тогда[KittyX.like]справляйся сам. . .{i}мудак{/i}."
                    $ KittyX.Blush = 1
                    $ KittyX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["Знаешь, мне вроде как нравится твой вкус.",
                            "Ты настоящий разрыватель челюстей.",
                            "Дай мне знать, если захочешь предложить свой чупа-чупс снова.",
                            "Хмммм. . . [Стучит языком по внутренней стороне щеки.]"])
                    ch_k "[Line]"

    elif Options[0] == "swallowed":
            #Kitty's response after swallowing the Player's cum.
            if "swallow" in KittyX.Chat:
                ch_k "Я хотела бы как-нибудь попробовать тебя снова."
            else:
                ch_k "Так вот. . .Я тут[KittyX.like]вспомнила, что произошло на днях."
                ch_k "Знаешь, это был мой первый раз, когда я[KittyX.like]проглотила."
                $ KittyX.FaceChange("sly",1)
                ch_k "Было вполне неплохо. . ."
                $ KittyX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Kitty's response after taking a facial from the Player.
            ch_k "Эм. . .это прозвучит немного[KittyX.like]странно, но. . ."
            $ KittyX.FaceChange("sexy",2)
            ch_k "Я чувствую себя такой {i}сексуальной{/i}, когда ты кончаешь мне на лицо."
            $ KittyX.Blush = 1

    elif Options[0] == "sleepover":
            #Kitty's response after sleeping with the Player.
            ch_k "Я[KittyX.like]никак не могу перестать думать о той ночи."
            ch_k "Все прошло {i}просто{/i} идеально."

    elif Options[0] == "creampie":
            #Another of Kitty's responses after having sex with the Player.
            "[KittyX.Name] сближается с вами, чтобы прошептать вам на ухо:"
            if not Player.Male:
                ch_k "Я все еще чувствую, как твои. . . стекают по внутренней стороне моего бедра."
            else:
                ch_k "Я все еще чувствую, как твоя. . . стекает по внутренней стороне моего бедра."

    elif Options[0] == "sexed":
            #A final response from Kitty after having sex with the Player.
            if not Player.Male:
                ch_k "Так вот. . . я хочу, чтобы ты кое-что знала. . ."
                $ KittyX.FaceChange("sexy",2)
                ch_k ". . .[KittyX.Like]каждый раз, когда я мастурбирую. . ."
                ch_k "Я вспоминаю, что чувствовала, когда ты была внутри меня."
            else:
                ch_k "Так вот. . . я хочу, чтобы ты кое-что знал. . ."
                $ KittyX.FaceChange("sexy",2)
                ch_k ". . .[KittyX.Like]каждый раз, когда я мастурбирую. . ."
                ch_k "Я вспоминаю, что чувствовала, когда ты был внутри меня."
            $ KittyX.Blush = 1

    elif Options[0] == "anal":
            #Kitty's response after getting anal from the Player.
            $ KittyX.FaceChange("sly",2)
            ch_k "Слушай. . . после той ночи, мне типа стало[KittyX.like]тяжело сидеть."
            $ KittyX.FaceChange("sexy",2)
            ch_k "Хотя, оно того {i}точно{/i} стоило."
            $ KittyX.Blush = 1
    elif Options[0] == "kappa":
            #Kitty's response to having failed at project Kappa
            ch_k "Ты же помнишь, как Ксавье[KittyX.like]застукал нас в прошлый раз?"
            ch_k "Уверена, если бы мы нашли на него компромат, мы смогли бы заставить его уволиться. . ."
            ch_k "Может, у него есть что-нибудь в кабинете. . ."
    elif Options[0] == "Shadowcat":
            $ KittyX.Names.append("Shadowcat")
            ch_k "Знаешь, я хожу на задания под псевдонимом \"Призрачная кошка.\""
            menu:
                extend ""
                "Ох, ну ладно.":
                        $ KittyX.FaceChange("perplexed", 1)
                        $ KittyX.Statup("Love", 60, 2)
                        ch_k ". . ."
                "Ага, я знаю.":
                        $ KittyX.Statup("Love", 90, 5)
                "Хм, может, будешь всегда использовать это имя?":
                        if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "0"):
                                $ KittyX.Name = "Призрачная кошка"
                                $ KittyX.Name_rod = "Призрачной кошки"
                                $ KittyX.Name_dat = "Призрачной кошке"
                                $ KittyX.Name_vin = "Призрачную кошку"
                                $ KittyX.Name_tvo = "Призрачной кошкой"
                                $ KittyX.Name_pre = "Призрачной кошке"
                                $ KittyX.Statup("Obed", 90, 5)
                                ch_k "Ладно? . ."
                        else:
                                ch_k "Это довольно глупое имя, чтобы пользоваться им всегда. . ."
                                menu:
                                    extend ""
                                    "Ладно, тогда оставим \"[KittyX.Name]\".":
                                            $ KittyX.FaceChange("smile", 1)
                                    "Я настаиваю.":
                                            $ KittyX.Statup("Love", 90, -10)
                                            $ KittyX.Statup("Obed", 50, 10)
                                            $ KittyX.FaceChange("angry", 2)
            ch_k ". . ."
            #end "why not Katherine"
    elif Options[0] == "Katherine":
            $ KittyX.Names.append("Katherine")
            ch_k "Мое полное имя \"Кэтрин Прайд.\""
            if not Player.Male:
                ch_k "Ты, наверное, этого не знала."
            else:
                ch_k "Ты, наверное, этого не знал."
            menu:
                extend ""
                "Ох, ну ладно.":
                        $ KittyX.FaceChange("perplexed", 1)
                        $ KittyX.Statup("Love", 60, 2)
                        ch_k ". . ."
                "Мне больше нравится \"[KittyX.Name].\"":
                        $ KittyX.Statup("Love", 90, 5)
                        $ KittyX.Statup("Inbt", 50, 5)
                        if ApprovalCheck(KittyX, 800, "LO"):
                                $ KittyX.Statup("Obed", 70, 5)
                        ch_k "Ага, мне тоже. . ."
                "Может, тогда стоит звать тебя \"Кэтрин\"?":
                        if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "0"):
                                $ KittyX.Name = "Кэтрин"
                                $ KittyX.Name_rod = "Кэтрин"
                                $ KittyX.Name_dat = "Кэтрин"
                                $ KittyX.Name_vin = "Кэтрин"
                                $ KittyX.Name_tvo = "Кэтрин"
                                $ KittyX.Name_pre = "Кэтрин"
                                $ KittyX.Statup("Obed", 90, 5)
                                ch_k "Думаю, да, можешь звать меня так. . ."
                        else:
                                ch_k "Если честно, мне это имя не особо нравится. . ."
                                menu:
                                    extend ""
                                    "Ладно, тогда оставим \"[KittyX.Name]\".":
                                            $ KittyX.FaceChange("smile", 1)
                                    "Я настаиваю.":
                                            $ KittyX.Statup("Love", 90, -10)
                                            $ KittyX.Statup("Obed", 50, 10)
                                            $ KittyX.FaceChange("angry", 2)
                                            ch_k "!!!"
            #end "why not Katherine"

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ KittyX.FaceChange("sly",2)
            ch_k "Может быть, я не упоминала об этом раньше, но. . ."
            if not Player.Male:
                ch_k "Она у тебя. . . впечатляет."
            else:
                ch_k "У тебя впечатляющий. . . член."
            $ KittyX.FaceChange("bemused",1)
            $ KittyX.Statup("Love", 90, 3)
            $ KittyX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            $ KittyX.FaceChange("bemused",2,Eyes="side")
            if not Player.Male:
                ch_k "Эмм, когда ты впервые увидела мою. . . обнаженную грудь, ты почти ничего не сказала. . ."
            else:
                ch_k "Эмм, когда ты впервые увидел мою. . . обнаженную грудь, ты почти ничего не сказал. . ."
            ch_k "Что ты о ней думаешь?"
            call Girl_First_TMenu
            $ KittyX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            $ KittyX.FaceChange("bemused",2,Eyes="side")
            if not Player.Male:
                ch_k "Эмм, когда ты впервые увидела мою. . . киску. . ."
                ch_k "Ты почти ничего не сказала. . . "
            else:
                ch_k "Эмм, когда ты впервые увидел мою. . . киску. . ."
                ch_k "Ты почти ничего не сказал. . . "
            ch_k "Что ты о ней думаешь?"
            call Girl_First_BMenu
            $ KittyX.History.remove("bottomless")

    elif Options[0] == "boyfriend?":
        call Kitty_BF
    elif Options[0] == "lover?":
        call Kitty_Love
    elif Options[0] == "sir?":
        call Kitty_Sub
    elif Options[0] == "master?":
        call Kitty_Master
    elif Options[0] == "sexfriend?":
        call Kitty_Sexfriend
    elif Options[0] == "fuckbuddy?":
        call Kitty_Fuckbuddy
    elif Options[0] == "daddy?":
        call Kitty_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Отойди от меня.",
                "Я не хочу видеть твоего лица.",
                "Отстань от меня.",
                "Оставь меня в покое."])
        ch_k "[Line]"

    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)
            if D20 == 1:
                    $ KittyX.FaceChange("smile")
                    ch_k "Я[KittyX.like]в {i}таком{/i} восторге, [KittyX.Petname]! Я {i}успешно{/i} сдала тест Профессора МакКоя по информатике!"
            elif D20 == 2:
                    $ KittyX.FaceChange("sad")
                    ch_k "У тебя бывало такое[KittyX.like]когда кажется, что весь мир против тебя?"
            elif D20 == 3:
                    $ KittyX.FaceChange("surprised")
                    ch_k "Не могу поверить, мне сколько всего нужно сегодня сделать!"
            elif D20 == 4:
                    $ KittyX.FaceChange("sad")
                    ch_k "Кстати, [KittyX.Petname]. Прошлой ночью[KittyX.like]я так паршиво спала. Чувствую, что я готова[KittyX.like]свернуться калачиком и лечь спать прямо здесь."
            elif D20 == 5:
                    $ KittyX.FaceChange("smile")
                    ch_k "Вау! Разве сейчас[KittyX.like]на улице не {i}замечательно{/i}?"
            elif D20 == 6:
                    $ KittyX.FaceChange("perplexed")
                    ch_k "Прошлой ночью[KittyX.like]мне приснился ужасный кошмар. Мне снилось, что демон Н'Гарай гоняется за мной по всему особняку!"
            elif D20 == 7:
                    $ KittyX.FaceChange("smile")
                    ch_k "Это так круто. У меня[KittyX.like]завтра обед с моей лучшей подругой!"
            elif D20 == 8:
                    $ KittyX.FaceChange("sad")
                    ch_k "Знаешь, мне очень нравится здесь, в Салем Центре. Но я должна признать. . . Иногда я немного скучаю по Дирфилду."
            elif D20 == 9:
                    $ KittyX.FaceChange("confused")
                    ch_k "Это так странно. С тех пор, как профессор Ксавье телепатически научил меня русскому, я, вроде как, обнаружила, что теперь[KittyX.like]даже думаю на кириллице."
            elif D20 == 10:
                    $ KittyX.FaceChange("smile")
                    ch_k "Позанудствую. Сегодня в душе, у меня[KittyX.like]возникла офигенная идея для ОС, которую я пишу для компьютеров!"
            elif D20 == 11:
                    $ KittyX.FaceChange("smile")
                    ch_k "Я[KittyX.like]все никак не могу дождаться завтрашнего урока танцев! В этом семестре мы начинаем модерн!"
            elif D20 == 12:
                    $ KittyX.FaceChange("sad")
                    ch_k "Я слышала, что наши студенты собираются отдохнуть завтра в Харрис Хайдвэй. Но у меня[KittyX.like]{i}так{/i} много домашней работы!"
            elif D20 == 13:
                    $ KittyX.FaceChange("smile")
                    ch_k "Сейчас бы[KittyX.like]мороженное!"
            elif D20 == 14:
                    $ KittyX.FaceChange("sad")
                    ch_k "Когда я вспомнинаю[KittyX.like]как много людей ненавидят мутантов, мне становится грустно."
            elif D20 == 15:
                    $ KittyX.FaceChange("perplexed")
                    ch_k "Вчера[KittyX.like]что-то ударило меня по бедру в комнате Опасности. Такое ощущение, что у меня теперь синяк на всю ногу!"
            else:
                    $ KittyX.FaceChange("perplexed")
                    ch_k "С тобой весело проводить время."

    $ Line = 0
    return


# start Kitty_Names//////////////////////////////////////////////////////////
label Kitty_Names:
    menu:
        ch_k "А? Как бы тебе хотелось, чтобы я тебя звала?"
        "Милая в самый раз." if not Player.Male:
            $ KittyX.Petname_rod = "милой"
            $ KittyX.Petname_dat = "милой"
            $ KittyX.Petname_vin = "милую"
            $ KittyX.Petname_tvo = "милой"
            $ KittyX.Petname_pre = "милой"
            $ KittyX.Petname = "милая"
            ch_k "Поняла, милая."
        "Милый в самый раз." if Player.Male:
            $ KittyX.Petname = "милый"
            $ KittyX.Petname_rod = "милого"
            $ KittyX.Petname_dat = "милому"
            $ KittyX.Petname_vin = "милого"
            $ KittyX.Petname_tvo = "милым"
            $ KittyX.Petname_pre = "милом"
            ch_k "Поняла, милый."
        "Зови по инициалам.":
            $ KittyX.Petname = Player.Name[:1]  #fix test this
            $ KittyX.Petname_rod = Player.Name[:1]
            $ KittyX.Petname_dat = Player.Name[:1]
            $ KittyX.Petname_vin = Player.Name[:1]
            $ KittyX.Petname_tvo = Player.Name[:1]
            $ KittyX.Petname_pre = Player.Name[:1]
            ch_k "Поняла, [KittyX.Petname]."
        "Зови меня по имени.":
            $ KittyX.Petname = Player.Name
            $ KittyX.Petname_rod = Player.Name_rod
            $ KittyX.Petname_dat = Player.Name_dat
            $ KittyX.Petname_vin = Player.Name_vin
            $ KittyX.Petname_tvo = Player.Name_tvo
            $ KittyX.Petname_pre = Player.Name_pre
            ch_k "Если ты этого хочешь, [KittyX.Petname]."
        "Зови меня\"моя девушка\"." if "boyfriend" in KittyX.Petnames and not Player.Male:
            $ KittyX.Petname = "моя девушка"
            $ KittyX.Petname_rod = "моей девушки"
            $ KittyX.Petname_dat = "моей девушке"
            $ KittyX.Petname_vin = "мою девушку"
            $ KittyX.Petname_tvo = "моей девушкой"
            $ KittyX.Petname_pre = "моей девушке"
            ch_k "Конечно, [KittyX.Petname]."
        "Зови меня\"мой парень\"." if "boyfriend" in KittyX.Petnames and Player.Male:
            $ KittyX.Petname = "мой парень"
            $ KittyX.Petname_rod = "моего парня"
            $ KittyX.Petname_dat = "моему парню"
            $ KittyX.Petname_vin = "моего парня"
            $ KittyX.Petname_tvo = "моим парнем"
            $ KittyX.Petname_pre = "моем парне"
            ch_k "Конечно, [KittyX.Petname]."
        "Зови меня\"любимая\"." if "lover" in KittyX.Petnames and not Player.Male:
            $ KittyX.Petname = "любимая"
            $ KittyX.Petname_rod = "любимой"
            $ KittyX.Petname_dat = "любимой"
            $ KittyX.Petname_vin = "любимую"
            $ KittyX.Petname_tvo = "любимой"
            $ KittyX.Petname_pre = "любимой"
            ch_k "Ооох, мне нравится, [KittyX.Petname]."
        "Зови меня\"любимый\"." if "lover" in KittyX.Petnames and Player.Male:
            $ KittyX.Petname = "любимый"
            $ KittyX.Petname_rod = "любимого"
            $ KittyX.Petname_dat = "любимому"
            $ KittyX.Petname_vin = "любимого"
            $ KittyX.Petname_tvo = "любимым"
            $ KittyX.Petname_pre = "любимом"
            ch_k "Ооох, мне нравится, [KittyX.Petname]."
        "Зови меня\"госпожа\"." if "sir" in KittyX.Petnames and not Player.Male:
            $ KittyX.Petname = "госпожа"
            $ KittyX.Petname_rod = "госпожи"
            $ KittyX.Petname_dat = "госпоже"
            $ KittyX.Petname_vin = "госпожу"
            $ KittyX.Petname_tvo = "госпожой"
            $ KittyX.Petname_pre = "госпоже"
            ch_k "Да, [KittyX.Petname]."
        "Зови меня\"господин\"." if "sir" in KittyX.Petnames and Player.Male:
            $ KittyX.Petname = "господин"
            $ KittyX.Petname_rod = "господина"
            $ KittyX.Petname_dat = "господину"
            $ KittyX.Petname_vin = "господина"
            $ KittyX.Petname_tvo = "господином"
            $ KittyX.Petname_pre = "господине"
            ch_k "Да, [KittyX.Petname]."
        "Зови меня\"хозяйка\"." if "master" in KittyX.Petnames and not Player.Male:
            $ KittyX.Petname = "хозяйка"
            $ KittyX.Petname_rod = "хозяйки"
            $ KittyX.Petname_dat = "хозяйке"
            $ KittyX.Petname_vin = "хозяйку"
            $ KittyX.Petname_tvo = "хозяйкой"
            $ KittyX.Petname_pre = "хозяйке"
            ch_k "Как пожелаешь, [KittyX.Petname]."
        "Зови меня\"хозяин\"." if "master" in KittyX.Petnames and Player.Male:
            $ KittyX.Petname = "хозяин"
            $ KittyX.Petname_rod = "хозяина"
            $ KittyX.Petname_dat = "хозяину"
            $ KittyX.Petname_vin = "хозяина"
            $ KittyX.Petname_tvo = "хозяином"
            $ KittyX.Petname_pre = "хозяине"
            ch_k "Как пожелаешь, [KittyX.Petname]."
        "Зови меня\"любовница\"." if "sex friend" in KittyX.Petnames and not Player.Male:
            $ KittyX.Petname = "любовница"
            $ KittyX.Petname_rod = "любовницы"
            $ KittyX.Petname_dat = "любовнице"
            $ KittyX.Petname_vin = "любовницу"
            $ KittyX.Petname_tvo = "любовницей"
            $ KittyX.Petname_pre = "любовнице"
            ch_k "Хихи, очень смело, [KittyX.Petname]."
        "Зови меня\"любовник\"." if "sex friend" in KittyX.Petnames and Player.Male:
            $ KittyX.Petname = "любовник"
            $ KittyX.Petname_rod = "любовника"
            $ KittyX.Petname_dat = "любовнику"
            $ KittyX.Petname_vin = "любовника"
            $ KittyX.Petname_tvo = "любовником"
            $ KittyX.Petname_pre = "любовнике"
            ch_k "Хихи, очень смело, [KittyX.Petname]."
        "Зови меня\"секс-партнерша\"." if "fuck buddy" in KittyX.Petnames and not Player.Male:
            $ KittyX.Petname = "секс-партнерша"
            $ KittyX.Petname_rod = "секс-партнерши"
            $ KittyX.Petname_dat = "секс-партнерше"
            $ KittyX.Petname_vin = "секс-партнершу"
            $ KittyX.Petname_tvo = "секс-партнершей"
            $ KittyX.Petname_pre = "секс-партнерше"
            h_k "Я в деле, если ты готова, [KittyX.Petname]."
        "Зови меня\"секс-партнер\"." if "fuck buddy" in KittyX.Petnames and Player.Male:
            $ KittyX.Petname = "секс-партнер"
            $ KittyX.Petname_rod = "секс-партнера"
            $ KittyX.Petname_dat = "секс-партнеру"
            $ KittyX.Petname_vin = "секс-партнера"
            $ KittyX.Petname_tvo = "секс-партнером"
            $ KittyX.Petname_pre = "секс-партнере"
            h_k "Я в деле, если ты готов, [KittyX.Petname]."
        "Зови меня\"мамочка\"." if "daddy" in KittyX.Petnames and not Player.Male:
            $ KittyX.Petname = "мамочка"
            $ KittyX.Petname_rod = "мамочки"
            $ KittyX.Petname_dat = "мамочке"
            $ KittyX.Petname_vin = "мамочку"
            $ KittyX.Petname_tvo = "мамочкой"
            $ KittyX.Petname_pre = "мамочке"
            ch_k "Ох! Буду, можешь не сомневаться, [KittyX.Petname]."
        "Зови меня\"папочка\"." if "daddy" in KittyX.Petnames and Player.Male:
            $ KittyX.Petname = "папочка"
            $ KittyX.Petname_rod = "папочки"
            $ KittyX.Petname_dat = "папочке"
            $ KittyX.Petname_vin = "папочку"
            $ KittyX.Petname_tvo = "папочкой"
            $ KittyX.Petname_pre = "папочке"
            ch_k "Ох! Буду, можешь не сомневаться, [KittyX.Petname]."
        "Неважно.":
            return
    return
# end Kitty_Names//////////////////////////////////////////////////////////

label Kitty_Pet:
    while 1:
        menu:
            extend ""
            "Обходительно":
                menu:
                    extend ""
                    "Пожалуй, я буду звать тебя просто Китти.":
                        $ KittyX.Pet = "Китти"
                        $ KittyX.Pet_rod = "Китти"
                        $ KittyX.Pet_dat = "Китти"
                        $ KittyX.Pet_vin = "Китти"
                        $ KittyX.Pet_tvo = "Китти"
                        $ KittyX.Pet_pre = "Китти"
                        ch_k "Конечно, почему бы и нет, [KittyX.Petname]."

                    "Думаю, буду звать тебя \"моя девушка\".":
                        if "boyfriend" in KittyX.Petnames:
                            $ KittyX.Pet = "моя девушка"
                            $ KittyX.Pet_rod = "моей девушки"
                            $ KittyX.Pet_dat = "моей девушке"
                            $ KittyX.Pet_vin = "мою девушку"
                            $ KittyX.Pet_tvo = "моей девушкой"
                            $ KittyX.Pet_pre = "моей девушке"
                            $ KittyX.FaceChange("sexy", 1)
                            ch_k "Я полностью твоя, [KittyX.Petname]."
                        else:
                            $ KittyX.FaceChange("angry")
                            ch_k "Я НЕ твоя девушка, [KittyX.Petname]."

                    "Думаю, я буду звать тебя \"детка\".":
                        if "boyfriend" in KittyX.Petnames or ApprovalCheck(KittyX, 500, "L"):
                            $ KittyX.Pet = "детка"
                            $ KittyX.Pet_rod = "детки"
                            $ KittyX.Pet_dat = "детке"
                            $ KittyX.Pet_vin = "детку"
                            $ KittyX.Pet_tvo = "деткой"
                            $ KittyX.Pet_pre = "детке"
                            $ KittyX.FaceChange("sexy", 1)
                            ch_k "Оу, я твоя детка, [KittyX.Petname]."
                        else:
                            $ KittyX.FaceChange("angry")
                            ch_k "Я тебе НЕ детка, [KittyX.Petname]."

                    "Думаю, я буду звать тебя \"крошка\".":
                        if "boyfriend" in KittyX.Petnames or ApprovalCheck(KittyX, 500, "L"):
                            $ KittyX.Pet = "крошка"
                            $ KittyX.Pet_rod = "крошки"
                            $ KittyX.Pet_dat = "крошке"
                            $ KittyX.Pet_vin = "крошку"
                            $ KittyX.Pet_tvo = "крошкой"
                            $ KittyX.Pet_pre = "крошке"
                            $ KittyX.FaceChange("sexy", 1)
                            ch_k "Оу, Я твоя крошка, [KittyX.Petname]."
                        else:
                            $ KittyX.FaceChange("angry")
                            ch_k "Я тебе НЕ крошка, [KittyX.Petname]."

                    "Думаю, я буду звать тебя \"малышка\".":
                        if "boyfriend" in KittyX.Petnames or ApprovalCheck(KittyX, 500, "L"):
                            $ KittyX.Pet = "малышка"
                            $ KittyX.Pet_rod = "малышки"
                            $ KittyX.Pet_dat = "малышке"
                            $ KittyX.Pet_vin = "малышку"
                            $ KittyX.Pet_tvo = "малышкой"
                            $ KittyX.Pet_pre = "малышке"
                            $ KittyX.FaceChange("sexy", 1)
                            ch_k "Оу, как мило, [KittyX.Petname]."
                        else:
                            $ KittyX.FaceChange("angry")
                            ch_k "Я тебе НЕ малышка!"


                    "Думаю, я буду звать тебя \"милая\".":
                        if "boyfriend" in KittyX.Petnames or ApprovalCheck(KittyX, 500, "L"):
                            $ KittyX.Pet = "милая"
                            $ KittyX.Pet_rod = "милой"
                            $ KittyX.Pet_dat = "милой"
                            $ KittyX.Pet_vin = "милую"
                            $ KittyX.Pet_tvo = "милой"
                            $ KittyX.Pet_pre = "милой"
                            ch_k "Оу, как мило, [KittyX.Petname]."
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Слишком слащаво, [KittyX.Petname]."

                    "Думаю, я буду звать тебя \"секси\".":
                        if "lover" in KittyX.Petnames or ApprovalCheck(KittyX, 900):
                            $ KittyX.Pet = "секси"
                            $ KittyX.Pet_rod = "секси"
                            $ KittyX.Pet_dat = "секси"
                            $ KittyX.Pet_vin = "секси"
                            $ KittyX.Pet_tvo = "секси"
                            $ KittyX.Pet_pre = "секси"
                            $ KittyX.FaceChange("sexy", 1)
                            ch_k "Мяу, [KittyX.Petname]."
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Не на людях, [KittyX.Petname]."

                    "Думаю, я буду звать тебя \"любимая\".":
                        if "lover" in KittyX.Petnames or ApprovalCheck(KittyX, 900, "L") or ApprovalCheck(KittyX, 1400):
                            $ KittyX.Pet = "любимая"
                            $ KittyX.Pet_rod = "любимой"
                            $ KittyX.Pet_dat = "любимой"
                            $ KittyX.Pet_vin = "любимую"
                            $ KittyX.Pet_tvo = "любимой"
                            $ KittyX.Pet_pre = "любимой"
                            $ KittyX.FaceChange("sexy", 1)
                            ch_k "Я тоже тебя люблю, [KittyX.Petname]!"
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Не в этой жизни, [KittyX.Petname]."

                    "Думаю, буду звать тебя \"кисонька\".":
                        if "boyfriend" in KittyX.Petnames or ApprovalCheck(KittyX, 500, "L"):
                            $ KittyX.Pet = "кисонька"
                            $ KittyX.Pet_rod = "кисоньки"
                            $ KittyX.Pet_dat = "кисоньке"
                            $ KittyX.Pet_vin = "кисоньку"
                            $ KittyX.Pet_tvo = "кисонькой"
                            $ KittyX.Pet_pre = "кисоньке"
                            $ KittyX.FaceChange("sexy", 1)
                            ch_k "Муррр, [KittyX.Petname]."
                        else:
                            $ KittyX.FaceChange("angry")
                            ch_k "Это не так уж и мило, [KittyX.Petname]"

                    "Назад":
                        pass

            "Грубо":
                menu:
                    "Думаю, я буду звать тебя \"рабыня\".":
                        if "master" in KittyX.Petnames or ApprovalCheck(KittyX, 700, "O"):
                            $ KittyX.Pet = "рабыня"
                            $ KittyX.Pet_rod = "рабыни"
                            $ KittyX.Pet_dat = "рабыне"
                            $ KittyX.Pet_vin = "рабыню"
                            $ KittyX.Pet_tvo = "рабыней"
                            $ KittyX.Pet_pre = "рабыне"
                            $ KittyX.FaceChange("bemused", 1)
                            ch_k "Как пожелаешь, [KittyX.Petname]."
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Я тебе не рабыня, [KittyX.Petname]."

                    "Думаю, я буду звать тебя \"питомец\".":
                        if "master" in KittyX.Petnames or ApprovalCheck(KittyX, 600, "O"):
                            $ KittyX.Pet = "питомец"
                            $ KittyX.Pet_rod = "питомце"
                            $ KittyX.Pet_dat = "питомцу"
                            $ KittyX.Pet_vin = "питомца"
                            $ KittyX.Pet_tvo = "питомцем"
                            $ KittyX.Pet_pre = "питомце"
                            $ KittyX.FaceChange("bemused", 1)
                            ch_k "Хммм. Не забудь погладить меня, [KittyX.Petname]."
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Я не домашняя кошка, [KittyX.Petname]."

                    "Думаю, я буду звать тебя \"шлюха\".":
                        if "sex friend" in KittyX.Petnames or ApprovalCheck(KittyX, 1000, "OI"):
                            $ KittyX.Pet = "шлюха"
                            $ KittyX.Pet_rod = "шлюхи"
                            $ KittyX.Pet_dat = "шлюхе"
                            $ KittyX.Pet_vin = "шлюху"
                            $ KittyX.Pet_tvo = "шлюхой"
                            $ KittyX.Pet_pre = "шлюхе"
                            $ KittyX.FaceChange("sexy")
                            ch_k "Если ты так хочешь, [KittyX.Petname]."
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            $ KittyX.Mouth = "surprised"
                            ch_k "Нет, если ты, конечно, не хочешь потерять зубы!"

                    "Думаю, я буду звать тебя \"блядь\".":
                        if "fuckbuddy" in KittyX.Petnames or ApprovalCheck(KittyX, 1100, "OI"):
                            $ KittyX.Pet = "блядь"
                            $ KittyX.Pet_rod = "бляди"
                            $ KittyX.Pet_dat = "бляде"
                            $ KittyX.Pet_vin = "блядь"
                            $ KittyX.Pet_tvo = "блядью"
                            $ KittyX.Pet_pre = "бляде"
                            $ KittyX.FaceChange("sly")
                            ch_k "Но только твоя. . ."
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Сможешь повторить это с разбитой губой, [KittyX.Petname]?"

                    "Думаю, я буду звать тебя \"сладкогрудая\".":
                        if "sex friend" in KittyX.Petnames or ApprovalCheck(KittyX, 1400):
                            $ KittyX.Pet = "сладкогрудая"
                            $ KittyX.Pet_rod = "сладкогрудой"
                            $ KittyX.Pet_dat = "сладкогрудой"
                            $ KittyX.Pet_vin = "сладкогрудую"
                            $ KittyX.Pet_tvo = "сладкогрудой"
                            $ KittyX.Pet_pre = "сладкогрудой"
                            $ KittyX.FaceChange("sly", 1)
                            ch_k "Ты про этих крошек?"
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Надеюсь, что нет, [KittyX.Petname]."

                    "Думаю, я буду звать тебя \"любовница\".":
                        if "sex friend" in KittyX.Petnames or ApprovalCheck(KittyX, 600, "I"):
                            $ KittyX.Pet = "любовница"
                            $ KittyX.Pet_rod = "любовницы"
                            $ KittyX.Pet_dat = "любовнице"
                            $ KittyX.Pet_vin = "любовницу"
                            $ KittyX.Pet_tvo = "любовницей"
                            $ KittyX.Pet_pre = "любовнице"
                            $ KittyX.FaceChange("sly")
                            ch_k "Мрряу. . ."
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Не произноси такого, [KittyX.Petname]."

                    "Думаю, я буду звать тебя \"секс-партнерша\".":
                        if "fuckbuddy" in KittyX.Petnames or ApprovalCheck(KittyX, 700, "I"):
                            $ KittyX.Pet = "секс-партнерша"
                            $ KittyX.Pet_rod = "секс-партнерши"
                            $ KittyX.Pet_dat = "секс-партнерше"
                            $ KittyX.Pet_vin = "секс-партнершу"
                            $ KittyX.Pet_tvo = "секс-партнершей"
                            $ KittyX.Pet_pre = "секс-партнерше"
                            $ KittyX.FaceChange("sly")
                            ch_k "Агась."
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            $ KittyX.Mouth = "surprised"
                            ch_k "Не шути так, [KittyX.Petname]."

                    "Думаю, я буду звать тебя \"доченька\".":
                        if "daddy" in KittyX.Petnames or ApprovalCheck(KittyX, 1200):
                            $ KittyX.Pet = "доченька"
                            $ KittyX.Pet_rod = "доченьки"
                            $ KittyX.Pet_dat = "доченьке"
                            $ KittyX.Pet_vin = "доченьку"
                            $ KittyX.Pet_tvo = "доченькой"
                            $ KittyX.Pet_pre = "доченьке"
                            $ KittyX.FaceChange("smile", 1)
                            ch_k "Тебе виднее, [KittyX.Petname]."
                        else:
                            $ KittyX.FaceChange("angry", 1)
                            ch_k "Я не твой ребенок!"

                    "Назад":
                        pass

            "Неважно.":
                return
    return

#label Kitty_Namecheck(KittyX.Pet = KittyX.Pet, Cnt = 0, Ugh = 0):#$ Girl.NameCheck() #checks reaction to petname

# start Kitty_Rename//////////////////////////////////////////////////////////
label Kitty_Rename:
        #Sets alternate names from Kitty
        $ KittyX.Mouth = "smile"
        ch_k "Да?"
        menu:
            extend ""
            "Думаю, \"Китти\" красивое имя." if KittyX.Name != "Китти" and "Kitty" in KittyX.Names:
                            $ KittyX.Name = "Китти"
                            $ KittyX.Name_rod = "Китти"
                            $ KittyX.Name_dat = "Китти"
                            $ KittyX.Name_vin = "Китти"
                            $ KittyX.Name_tvo = "Китти"
                            $ KittyX.Name_pre = "Китти"
                            ch_k "Я тоже!"
            "Думаю, \"Кейт\" клевое имя." if KittyX.Name != "Кейт" and "Kate" in KittyX.Names:
                            if "namechange" not in KittyX.DailyActions:
                                    $ KittyX.Statup("Love", 70, 1)
                                    $ KittyX.Statup("Inbt", 60, 2)
                                    $ KittyX.Statup("Inbt", 80, 1)
                            $ KittyX.Name = "Кейт"
                            $ KittyX.Name_rod = "Кейт"
                            $ KittyX.Name_dat = "Кейт"
                            $ KittyX.Name_vin = "Кейт"
                            $ KittyX.Name_tvo = "Кейт"
                            $ KittyX.Name_pre = "Кейт"
                            ch_k "Ага, я тоже так думаю. . ."
            "Как насчет \"Кэтрин?\"" if KittyX.Name != "Кэтрин" and "Katherine" in KittyX.Names:
                    if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "0"):
                            if "namechange" not in KittyX.DailyActions:
                                    $ KittyX.Statup("Obed", 70, 2)
                            $ KittyX.Name = "Кэтрин"
                            $ KittyX.Name_rod = "Кэтрин"
                            $ KittyX.Name_dat = "Кэтрин"
                            $ KittyX.Name_vin = "Кэтрин"
                            $ KittyX.Name_tvo = "Кэтрин"
                            $ KittyX.Name_pre = "Кэтрин"
                            ch_k "Думаю. . . можно?"
                    else:
                            ch_k "Мне оно не особо нравится. . ."
            "Как насчет \"Призрачной Кошки?\"" if KittyX.Name != "Призрачная кошка" and "Shadowcat" in KittyX.Names:
                    if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "0"):
                            $ KittyX.FaceChange("confused")
                            $ KittyX.Name = "Призрачная кошка"
                            $ KittyX.Name_rod = "Призрачной кошки"
                            $ KittyX.Name_dat = "Призрачной кошке"
                            $ KittyX.Name_vin = "Призрачную кошку"
                            $ KittyX.Name_tvo = "Призрачной кошкой"
                            $ KittyX.Name_pre = "Призрачной кошке"
                            ch_k "Думаю. . . можно?"
                    else:
                            $ KittyX.FaceChange("perplexed")
                            ch_k "Меня так должны звать только во время операций!"
                    $ KittyX.FaceChange()
            "Неважно.":
                    pass
        $ KittyX.AddWord(1,0,"namechange")
        return
# end Kitty_Rename//////////////////////////////////////////////////////////


# start Kitty_Personality//////////////////////////////////////////////////////////
label Kitty_Personality(Cnt = 0):
    if not KittyX.Chat[4] or Cnt:
        "Поскольку у вас все хорошо получается в одной области, вы можете убедить Китти сосредоточиться на любой другой."
        "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
        "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
    menu:
        ch_k "Конечно, что такое?"
        "Больше Послушания. [[Любовь в Послушание]" if KittyX.Love > 900:
            ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
            ch_k "Если[KittyX.like]это то, чего ты хочешь, Я могу попробовать быть немного более послушной."
            $ KittyX.Chat[4] = 1
        "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if KittyX.Love > 900:
            ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
            ch_k "Я всегда могу быть немного более дикой, если ты этого хочешь."
            $ KittyX.Chat[4] = 2

        "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if KittyX.Obed > 900:
            ch_p "Я хочу, чтобы ты была более раскрепощенной."
            ch_k "Хорошо, я могу открыться сильнее."
            $ KittyX.Chat[4] = 3
        "Больше Любви. [[Повиновение в Любовь]" if KittyX.Obed > 900:
            ch_p "Я хочу, чтобы ты училась любить меня."
            ch_k "Я попробую."
            $ KittyX.Chat[4] = 4

        "Больше Повиновения. [[Раскрепощенность в Повиновение]" if KittyX.Inbt > 900:
            ch_p "Я знаю, что нам и так весело, но разве ты не можешь иногда слушаться меня?"
            ch_k "Ооох. . ."
            $ KittyX.Chat[4] = 5

        "Больше Любви. [[Раскрепощенность в Любовь]" if KittyX.Inbt > 900:
            ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
            ch_k "Мы повеселимся вместе. . ."
            $ KittyX.Chat[4] = 6

        "Просто делай то, что тебе нравится. . .[[Сбросить]" if KittyX.Chat[4]:
            ch_p "Помнишь, что мы обсуждали? Забудь."
            ch_k "Эм, ладно."
            $ KittyX.Chat[4] = 0
        "Повторить правила":
            call Kitty_Personality(1)
            return
        "Неважно.":
            return
    return
# end Kitty_Personality//////////////////////////////////////////////////////////




# Kitty_Summon//////////////////////////////////////////////////////////

label Kitty_Summon(Tempmod=Tempmod):
    $ KittyX.OutfitChange()
    if "no summon" in KittyX.RecentActions:
                if "angry" in KittyX.RecentActions:
                    ch_k "Догадайся, каков мой ответ, [KittyX.Petname]!"
                elif KittyX.RecentActions.count("no summon") > 1:
                    ch_k "Я сказала тебе, оставь меня в покое!"
                    $ KittyX.RecentActions.append("angry")
                elif Time_Count >= 3: #night time
                    ch_k "Как я уже сказала, для этого уже слишком поздно."
                else:
                    ch_k "Как я уже сказала, я занята."
                $ KittyX.RecentActions.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if KittyX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif KittyX.Loc == "bg dangerroom":
        $ Tempmod = -10
    elif KittyX.Loc == "bg showerroom":
        $ Tempmod = -30

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"

    elif Time_Count >= 3: #night time
                if ApprovalCheck(KittyX, 700, "L") or ApprovalCheck(KittyX, 300, "O"):
                        #It's night time but she likes you.
                        ch_k "Уже[KittyX.like]довольно поздно, но мы можем немного пообщаться."
                        $ KittyX.Loc = bg_current
                        call Taboo_Level
                        call Set_The_Scene
                else:
                        #It's night time and she isn't into you
                        ch_k "Уже ведь так поздно? Может, завтра?"
                        $ KittyX.RecentActions.append("no summon")
                return
    elif "les" in KittyX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(KittyX, 2000):
                    ch_k "Я сейчас кое с кем. . . общаюсь, [KittyX.Petname], хочешь к нам?"
                    menu:
                        extend ""
                        "Конечно.":
                            $ Line = "go to"
                        "Нет, спасибо.":
                            ch_k "Ну и ладно."
                            return
            else:
                    ch_k "Эм, нет, у нас здесь и без этого хорошо."
                    ch_k "Может, увидимся в другой раз?"
                    $ KittyX.RecentActions.append("no summon")
                    return
    elif not ApprovalCheck(KittyX, 700, "L") or not ApprovalCheck(KittyX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(KittyX, 300):
                ch_k "Я немного занята, [KittyX.Petname]."
                $ KittyX.RecentActions.append("no summon")
                return


        if "summoned" in KittyX.RecentActions:
                pass
        elif "goto" in KittyX.RecentActions:
                if not Player.Male:
                    ch_k "Ты {i}только что{/i} ушла отсюда, почему бы тебе не вернуться?"
                else:
                    ch_k "Ты {i}только что{/i} ушел отсюда, почему бы тебе не вернуться?"
        elif KittyX.Loc == "bg classroom":
                if not Player.Male:
                    ch_k "Я[KittyX.like]в аудитории, [KittyX.Petname], ты готова прийти?"
                else:
                    ch_k "Я[KittyX.like]в аудитории, [KittyX.Petname], ты готов прийти?"
        elif KittyX.Loc == "bg dangerroom":
                ch_k "Я в Комнате Опасности, [KittyX.Petname], хочешь прийти?"
        elif KittyX.Loc == "bg campus":
                ch_k "Я прохлаждаюсь на площади, [KittyX.Petname], хочешь прийти?"
        elif KittyX.Loc == "bg kitty":
                ch_k "Я в своей комнате, [KittyX.Petname], хочешь составить компанию?"
        elif KittyX.Loc == "bg player":
                ch_k "Я в твоей комнате, [KittyX.Petname], приходи. . ."
        elif KittyX.Loc == "bg showerroom":
            if ApprovalCheck(KittyX, 1600):
                ch_k "Я[KittyX.like]сейчас в душе, [KittyX.Petname], хочешь освежиться?"
            else:
                ch_k "Я[KittyX.like]сейчас в душе, [KittyX.Petname], увидимся позже."
                $ KittyX.RecentActions.append("no summon")
                return
        elif KittyX.Loc == "hold":
                ch_k "Я[KittyX.like]сейчас, вроде как, очень занята. Извини?"
                $ KittyX.RecentActions.append("no summon")
                return
        else:
                ch_k "Почему бы тебе не подойти сюда, [KittyX.Petname]?"


        if "summoned" in KittyX.RecentActions:
            ch_k "Ладно, лаааадно, но зачем ты таскаешь меня повсюду?"
            $ Line = "yes"
        elif "goto" in KittyX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
#                                ch_k "KK, Cya!"
                                $ Line = "go to"
                "Нет.":
                                ch_k "Ладно."
                "Мне бы {i}очень{/i} хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(KittyX, 600, "L") or ApprovalCheck(KittyX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(KittyX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(KittyX, 1400):
                                #she is generally favorable
                                ch_k "Ладно, хорошо."
                                $ Line = "yes"
                        elif ApprovalCheck(KittyX, 200, "O"):
                                #she is not obedient
                                ch_k "Да мне пофиг."
                                ch_k "Если что, ты знаешь где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(KittyX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(KittyX, 1400):
                                #she is generally favorable
                                ch_k "Ладно, хорошо."
                                $ Line = "yes"
                        elif ApprovalCheck(KittyX, 200, "O"):
                                #she is not obedient
                                ch_k "Да мне пофиг."
                                ch_k "Если что, ты знаешь где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Конечно, сейчас приду.":
                    $ KittyX.Statup("Love", 55, 1)
                    $ KittyX.Statup("Inbt", 30, 1)
#                    ch_k "See ya!"
                    $ Line = "go to"

                "Нет, поговорим позже.":
                    $ KittyX.Statup("Obed", 50, 1)
                    $ KittyX.Statup("Obed", 30, 2)
                    ch_k "Ох, хорошо. Тогда увидимся в другой раз."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                    if ApprovalCheck(KittyX, 600, "L") or ApprovalCheck(KittyX, 1400):
                        $ KittyX.Statup("Love", 70, 1)
                        $ KittyX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ KittyX.Statup("Inbt", 30, 1)
                        $ Line = "no"

                "Пошли ко мне, будет весело.":
                        if ApprovalCheck(KittyX, 400, "L") and ApprovalCheck(KittyX, 800):
                            $ KittyX.Statup("Love", 70, 1)
                            $ KittyX.Statup("Obed", 50, 1)
                            $ Line = "fun"
                        else:
                            $ KittyX.Statup("Inbt", 30, 1)
                            $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                    if ApprovalCheck(KittyX, 600, "O"):
                        #she is obedient
                        $ KittyX.Statup("Love", 50, 1, 1)
                        $ KittyX.Statup("Love", 40, -1)
                        $ KittyX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(KittyX, 1400):
                        #she is generally favorable
                        $ KittyX.Statup("Love", 70, -2)
                        $ KittyX.Statup("Love", 90, -1)
                        $ KittyX.Statup("Obed", 50, 2)
                        $ KittyX.Statup("Obed", 90, 1)
                        ch_k "Ладно, [KittyX.Petname]."
                        $ Line = "yes"

                    elif ApprovalCheck(KittyX, 200, "O"):
                        #she is not obedient
                        $ KittyX.Statup("Love", 70, -4)
                        $ KittyX.Statup("Love", 90, -2)
                        ch_k "Ты мне не указ!"
                        $ KittyX.Statup("Inbt", 40, 2)
                        $ KittyX.Statup("Inbt", 60, 1)
                        $ KittyX.Statup("Obed", 70, -2)
                        ch_k "Если что, ты знаешь, где меня найти."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ KittyX.Statup("Inbt", 30, 1)
                        $ KittyX.Statup("Inbt", 50, 1)
                        $ KittyX.Statup("Love", 50, -1, 1)
                        $ KittyX.Statup("Obed", 70, -1)
                        $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                    if ApprovalCheck(KittyX, 600, "O"):
                        #she is obedient
                        $ KittyX.Statup("Love", 50, 1, 1)
                        $ KittyX.Statup("Love", 40, -1)
                        $ KittyX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(KittyX, 1400):
                        #she is generally favorable
                        $ KittyX.Statup("Love", 70, -2)
                        $ KittyX.Statup("Love", 90, -1)
                        $ KittyX.Statup("Obed", 50, 2)
                        $ KittyX.Statup("Obed", 90, 1)
                        ch_k "Ладно, [KittyX.Petname]."
                        $ Line = "yes"

                    elif ApprovalCheck(KittyX, 200, "O"):
                        #she is not obedient
                        $ KittyX.Statup("Love", 70, -4)
                        $ KittyX.Statup("Love", 90, -2)
                        ch_k "Ты мне не указ!"
                        $ KittyX.Statup("Inbt", 40, 2)
                        $ KittyX.Statup("Inbt", 60, 1)
                        $ KittyX.Statup("Obed", 70, -2)
                        ch_k "Если что, ты знаешь, где меня найти."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ KittyX.Statup("Inbt", 30, 1)
                        $ KittyX.Statup("Inbt", 50, 1)
                        $ KittyX.Statup("Love", 50, -1, 1)
                        $ KittyX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if KittyX.Love > KittyX.Obed:
            ch_k "Конечно!"
        else:
            ch_k "Ладно, скоро буду, [KittyX.Petname]."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ KittyX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            if KittyX.Loc == "bg classroom":
                ch_k "Мне[KittyX.like]нужно заниматься, [KittyX.Petname]."
            elif KittyX.Loc == "bg dangerroom":
                ch_k "Мне нужно тренироваться."
            else:
                ch_k "Извини, [KittyX.Petname], но я, вроде как, занята."
            $ KittyX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ KittyX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            $ Line = 0
            $ Nearby = []
            $ Party = [KittyX]
            if KittyX.Loc == "bg classroom":
                    ch_k "Я займу для тебя местечко!"
                    jump Class_Room
            elif KittyX.Loc == "bg dangerroom":
                    ch_k "Я пока разомнусь!"
                    jump Danger_Room
            elif KittyX.Loc == "bg kitty":
                    ch_k "Я пока приберусь."
                    jump Kitty_Room
            elif KittyX.Loc == "bg player":
                    ch_k "Я буду ждать тебя."
                    jump Player_Room
            elif KittyX.Loc == "bg showerroom":
                    ch_k "Пожалуй, я пока намылюсь."
                    jump Shower_Room
            elif KittyX.Loc == "bg campus":
                    ch_k "Я знаю хорошее местечко в тени."
                    jump Campus
            elif KittyX.Loc != "hold":
                    ch_k "Скоро увидимся. . ."
                    $ bg_current = KittyX.Loc
                    jump Misplaced
            else:
                    ch_k "Слушай, встретимся у меня в комнате."
                    $ KittyX.Loc = "bg kitty"
                    jump Kitty_Room

    #She's agreed to come over
    elif Line == "lonely":
            ch_k "Ооооу, это так мило!"
    elif Line == "command":
            ch_k "Хорошо, [KittyX.Petname]."
    elif Line == "fun":
            ch_k "Конечно."

    $ KittyX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(KittyX)
            return
    $ KittyX.Loc = bg_current
    call Taboo_Level(0)
    $ KittyX.OutfitChange()
    call Set_The_Scene
    return

# End Kitty Summon ///////////////////


label Kitty_Leave(Tempmod=Tempmod, GirlsNum = 0):
    if "leaving" in KittyX.RecentActions:
        $ KittyX.DrainWord("leaving")
    else:
        return

    if KittyX.Loc == "hold":
            # Activates if she's being moved out of play
            ch_k "Я[KittyX.like]ухожу, увидимся позже."
            return

    if KittyX in Party or "lockedtravels" in KittyX.Traits:
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ KittyX.Loc = bg_current
            return

    elif "freetravels" in KittyX.Traits or not ApprovalCheck(KittyX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.
            $ KittyX.OutfitChange()
            if GirlsNum: #if someone left before her
                        ch_k "Ага, я тоже ухожу."

            if KittyX.Loc == "bg classroom":
                        ch_k "Я[KittyX.like]сейчас направляюсь в аудиторию."
            elif KittyX.Loc == "bg dangerroom":
                        ch_k "Я[KittyX.like]иду в комнату Опасности."
            elif KittyX.Loc == "bg campus":
                        ch_k "Я[KittyX.like]собираюсь посидеть на площади кампуса."
            elif KittyX.Loc == "bg kitty":
                        ch_k "Я[KittyX.like]возвращаюсь в свою комнату."
            elif KittyX.Loc == "bg player":
                        ch_k "Я[KittyX.like]собираюсь в твою комнату."
            elif KittyX.Loc == "bg pool":
                        ch_k "Я[KittyX.like]собираюсь в бассейн."
            elif KittyX.Loc == "bg showerroom":
                if ApprovalCheck(KittyX, 1400):
                        ch_k "Я собираюсь принять душ, увидимся позже!"
                else:
                        ch_k "Я ухожу, увидимся!"
            else:
                        ch_k "Я ухожу, увидимся позже."
            hide Kitty_Sprite
            hide Kitty_Seated
            return
            #End Free Travels

    if bg_current == "bg dangerroom":
            call Gym_Exit([KittyX])

    $ KittyX.OutfitChange(Changed=0)

    if "follow" not in KittyX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ KittyX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    # Sets her preferences
    if KittyX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif KittyX.Loc == "bg dangerroom":
        $ Tempmod = 20
    elif KittyX.Loc == "bg showerroom":
        $ Tempmod = 40


    if GirlsNum: #if someone left before her
                ch_k "Ага, я тоже ухожу."

    if KittyX.Loc == "bg classroom":
        ch_k "Я сейчас иду на занятия, ты можешь[KittyX.like]присоединиться ко мне."
    elif KittyX.Loc == "bg dangerroom":
        ch_k "Я иду в Комнату Опасности[KittyX.like]присоединишься ко мне?"
    elif KittyX.Loc == "bg campus":
        ch_k "Я собираюсь[KittyX.like]на площадь кампуса, хочешь отдохнуть со мной?"
    elif KittyX.Loc == "bg kitty":
        ch_k "Я возвращаюсь в свою комнату, зайдешь[KittyX.like]ко мне?"
    elif KittyX.Loc == "bg player":
        ch_k "Я[KittyX. like]зайду в твою комнату."
    elif KittyX.Loc == "bg mall":
        ch_k "Я собираюсь[KittyX.like]погулять по торговому центру, хочешь отдохнуть со мной?"
    elif KittyX.Loc == "bg showerroom":
        if ApprovalCheck(KittyX, 1600):
            ch_k "Я[KittyX.like]собираюсь в душ, хочешь присоединиться ко мне?"
        else:
            ch_k "Я иду в душ, может, возможно[KittyX.like]увидимся позже."
            return
    elif KittyX.Loc == "bg pool":
            ch_k "Я[KittyX.like]направляюсь в бассейн. Ты идешь?"
    else:
            ch_k "Хочешь[KittyX.like]со мной, [KittyX.Petname]?"

    menu:
        extend ""
        "Конечно, я сразу за тобой.":
                if "followed" not in KittyX.RecentActions:
                    $ KittyX.Statup("Love", 55, 1)
                    $ KittyX.Statup("Inbt", 30, 1)
                $ Line = "go to"

        "Нет, поговорим позже.":
                if "followed" not in KittyX.RecentActions:
                    $ KittyX.Statup("Obed", 50, 1)
                    $ KittyX.Statup("Obed", 30, 2)
                ch_k "Ладно. Тогда до встречи."

        "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                if ApprovalCheck(KittyX, 600, "L") or ApprovalCheck(KittyX, 1400):
                    if "followed" not in KittyX.RecentActions:
                        $ KittyX.Statup("Love", 70, 1)
                        $ KittyX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else:
                    if "followed" not in KittyX.RecentActions:
                        $ KittyX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Останься со мной, будет весело.":
                if ApprovalCheck(KittyX, 400, "L") and ApprovalCheck(KittyX, 800):
                    $ KittyX.Statup("Love", 70, 1)
                    $ KittyX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else:
                    $ KittyX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Нет, останься здесь.":
                if ApprovalCheck(KittyX, 600, "O"):
                    #she is obedient
                    if "followed" not in KittyX.RecentActions:
                        if KittyX.Love >= 50:
                            $ KittyX.Statup("Love", 90, 1)
                        $ KittyX.Statup("Love", 40, -1)
                        $ KittyX.Statup("Obed", 90, 1)
                    $ Line = "command"

                elif D20 >= 7 and ApprovalCheck(KittyX, 1400):
                    #she is generally favorable
                    if "followed" not in KittyX.RecentActions:
                        $ KittyX.Statup("Love", 70, -2)
                        $ KittyX.Statup("Love", 90, -1)
                        $ KittyX.Statup("Obed", 50, 2)
                        $ KittyX.Statup("Obed", 90, 1)
                    ch_k "Эм, конечно, наверное."
                    $ Line = "yes"

                elif ApprovalCheck(KittyX, 200, "O"):
                    #she is not obedient
                    if "followed" not in KittyX.RecentActions:
                        $ KittyX.Statup("Love", 70, -4)
                        $ KittyX.Statup("Love", 90, -2)
                    ch_k "[KittyX.Like]в твоих мечтах, [KittyX.Petname]."
                    if "followed" not in KittyX.RecentActions:
                        $ KittyX.Statup("Inbt", 40, 2)
                        $ KittyX.Statup("Inbt", 60, 1)
                        $ KittyX.Statup("Obed", 70, -2)
                    ch_k "Я пошла."
                else:
                    #she is obedient, but you failed to meet the checks
                    if "followed" not in KittyX.RecentActions:
                        $ KittyX.Statup("Inbt", 30, 1)
                        $ KittyX.Statup("Inbt", 50, 1)
                        $ KittyX.Statup("Love", 50, -1, 1)
                        $ KittyX.Statup("Obed", 70, -1)
                    $ Line = "no"
                #End ordered to stay

    $ KittyX.RecentActions.append("followed")
    if not Line:
            #You end the dialog neutrally
            hide Kitty_Sprite
            hide Kitty_Seated
            call Gym_Clothes_Off([KittyX])
            return

    if Line == "no":
            # She's refused, context based dialog
            if KittyX.Loc == "bg classroom":
                ch_k "Никак не могу, [KittyX.Petname], нужно готовиться к тесту."
            elif KittyX.Loc == "bg dangerroom":
                ch_k "Извини, [KittyX.Petname], но мне[KittyX.like]нужно попрактиковаться."
            else:
                ch_k "[KittyX.Like]извини, [KittyX.Petname], но у меня дела."
            hide Kitty_Sprite
            hide Kitty_Seated
            call Gym_Clothes_Off([KittyX])
            return

    elif Line == "go to":
            #You agreed to go to her instead
            #$ Party.append(KittyX)
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")
            $ KittyX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            hide Kitty_Sprite
            hide Kitty_Seated
            $ Nearby = []
            $ Party = [KittyX]
            call Gym_Clothes_Off([KittyX])
            if KittyX.Loc == "bg classroom":
                if not Player.Male:
                    ch_k "Круто, напарница!"
                else:
                    ch_k "Круто, напарник!"
                jump Class_Room_Entry
            elif KittyX.Loc == "bg dangerroom":
                ch_k "Я буду ждать тебя!"
                jump Danger_Room_Entry
            elif KittyX.Loc == "bg kitty":
                ch_k "Встретимся там."
                jump Kitty_Room
            elif KittyX.Loc == "bg player":
                ch_k "Я буду ждать."
                jump Player_Room
            elif KittyX.Loc == "bg showerroom":
                ch_k "Думаю, увидимся там."
                jump Shower_Room_Entry
            elif KittyX.Loc == "bg campus":
                ch_k "Давай пойдем туда."
                jump Campus_Entry
            elif KittyX.Loc == "bg pool":
                ch_k "Хорошо, пойдем."
                jump Pool_Entry
            elif KittyX.Loc == "bg mall":
                ch_k "Хорошо, пойдем."
                jump Mall_Entry
            else:
                ch_k "Слушай, встретимся у меня в комнате."
                $ KittyX.Loc = "bg kitty"
                jump Kitty_Room
            #End "goto" where she's at

    #She's agreed to come over
    elif Line == "lonely":
            if not Player.Male:
                ch_k "Думаю[KittyX.like]я не могу оставить тебя одну. . ."
            else:
                ch_k "Думаю[KittyX.like]я не могу оставить тебя одного. . ."
    elif Line == "command":
            ch_k "Пфф, ладно."
    elif Line:
            ch_k "Конечно."

    $ Line = 0
    ch_k "Наверное, я могу остаться."
    $ KittyX.Loc = bg_current
    call Taboo_Level(0)
    return

# End Kitty Leave ///////////////////


## Kitty's Clothes  // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
label Kitty_Clothes:
    if KittyX.Taboo:
            if "exhibitionist" in KittyX.Traits:
                ch_k "Мммммм. . ."
            elif ApprovalCheck(KittyX, 900, TabM=4) or ApprovalCheck(KittyX, 400, "I", TabM=3):
                ch_k "Здесь[KittyX.like]довольно. . . открыто. . ."
            else:
                ch_k "Здесь[KittyX.like]довольно открыто, верно?"
                ch_k "Разве мы не можем поговорить об этом в одной из наших комнат?"
                return
    elif ApprovalCheck(KittyX, 900, TabM=4) or ApprovalCheck(KittyX, 600, "L") or ApprovalCheck(KittyX, 300, "O"):
                ch_k "[KittyX.Like]о чем ты вообще думаешь?"
    else:
                ch_k "Я дам тебе знать, когда мне будет не наплевать на твое мнение."
                return

    if Girl != KittyX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = KittyX
    call Shift_Focus(Girl)

label Kitty_Wardrobe_Menu:
    $ Trigger = 1 # to prevent Focus swapping. . .
    $ KittyX.FaceChange()
    while True:
        menu:
            ch_k "Итак, ты[KittyX.like]хочешь поговорить о моей одежде?"
            "Верх":
                        call Kitty_Clothes_Over
            "Низ":
                        call Kitty_Clothes_Legs
            "Нижнее белье":
                        call Kitty_Clothes_Under
            "Аксессуары":
                        call Kitty_Clothes_Misc
            "Управление нарядами":
                        call Kitty_Clothes_Outfits
            "Давай поговорим о том, что ты носишь":
                        call Clothes_Schedule(KittyX)

            "Могу я посмотреть?" if KittyX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(KittyX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_k "Миленько, да? . ."
                    hide PhoneSex
            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(KittyX,0,2)
                    if _return:
                        hide DressScreen
            "Может, тебе будет комфортнее за ширмой? (locked)" if KittyX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if KittyX.Loc == bg_current and not KittyX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if not Player.Male and "girltalk" not in KittyX.History and "nogirls" not in KittyX.History:
                            ch_k "Эм, нет, мне и так хорошо."
                    elif ApprovalCheck(KittyX, 1500) or (KittyX.SeenChest and KittyX.SeenPussy):
                            ch_k "Скорее всего она не понадобится, но спасибо."
                    else:
                            show DressScreen zorder 150
                            ch_k "Ага, с ней мне будет немного комфортней, спасибо."

            "У меня есть подарок для тебя (locked)" if KittyX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if KittyX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(KittyX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ KittyX.OutfitChange()
                    $ KittyX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != KittyX:
                            ch_p "Я хочу поговорить о твоей одежде."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = KittyX
                    call Shift_Focus(Girl)

            "Сменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current:
                    pass
            "Сменить вид" if Girl.Loc == bg_current:
                    call WardrobeView(KittyX)

            "Неважно, ты и так хорошо выглядишь":
                    call Girl_Pos_Reset(KittyX)
                    if "wardrobe" not in KittyX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if KittyX.Chat[1] <= 1:
                                    $ KittyX.Statup("Love", 70, 15)
                                    $ KittyX.Statup("Obed", 40, 20)
                                    ch_k "Приятно[KittyX.like]слышать это от тебя."
                            elif KittyX.Chat[1] <= 10:
                                    $ KittyX.Statup("Love", 70, 5)
                                    $ KittyX.Statup("Obed", 40, 7)
                                    ch_k "Я себе тоже нравлюсь."
                            elif KittyX.Chat[1] <= 50:
                                    $ KittyX.Statup("Love", 70, 1)
                                    $ KittyX.Statup("Obed", 40, 1)
                                    ch_k "Ага."
                            else:
                                    ch_k "Конечно."
                            $ KittyX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(KittyX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ KittyX.OutfitChange()
                    #sets up a temporary outfit
                    $ KittyX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ KittyX.Chat[1] += 1
                    $ Trigger = 0
                    if KittyX.Panties and "pantyless" in KittyX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ KittyX.DailyActions.remove("pantyless")
                    return

        #Loops back up
        #jump Kitty_Clothes
        #End of Kitty Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Kitty_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(KittyX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(KittyX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(KittyX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(KittyX,4,1)
                    "Одежда для сна":
                                call OutfitShame(KittyX,7,1)
                    "Купальник":
                                call OutfitShame(KittyX,10,1)

                    "Повседневка 1" if ApprovalCheck(KittyX, 2500):
                                call OutfitShame(KittyX,11,1)
                    "Повседневка 2" if ApprovalCheck(KittyX, 2500):
                                call OutfitShame(KittyX,12,1)
                    "Неважно":
                                pass

        "Мне очень нравятся твой розовый топ и капри.":
                #pink shirt
                $ KittyX.OutfitChange("casual1")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                        $ KittyX.Outfit = "casual1"
                        $ KittyX.Shame = 0
                        ch_k "Раньше я[KittyX.like]одевалась так каждый день!"
                    "Давай попробуем что-нибудь другое.":
                        ch_k "Ладно."

        "Красная рубашка и черные джинсы очень хорошо сидят на тебе.":
                #red shirt
                $ KittyX.OutfitChange("casual2")
                menu:
                    "Ты должна носить их. [[Выбрать текущий наряд]":
                        $ KittyX.Outfit = "casual2"
                        $ KittyX.Shame = 0
                        ch_k "Это моя[KittyX.like]любимая одежда!"
                    "Давай попробуем что-нибудь другое.":
                        ch_k "Ладно."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not KittyX.Custom1[0] and not KittyX.Custom2[0] and not KittyX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if KittyX.Custom1[0] or KittyX.Custom2[0] or KittyX.Custom3[0]:
                $ Cnt = 0
                while 1:
                    menu:
                        "Надень Пользовательский 1 (locked)" if not KittyX.Custom1[0]:
                                pass
                        "Надень Пользовательский 1" if KittyX.Custom1[0]:
                                $ KittyX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Надень Пользовательский 2 (locked)" if not KittyX.Custom2[0]:
                                pass
                        "Надень Пользовательский 2" if KittyX.Custom2[0]:
                                $ KittyX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Надень Пользовательский 3 (locked)" if not KittyX.Custom3[0]:
                                pass
                        "Надень Пользовательский 3" if KittyX.Custom3[0]:
                                $ KittyX.OutfitChange("custom3")
                                $ Cnt = 6

                        "Ты должна одеваться так, когда мы наедине (locked)" if not Cnt:
                                pass
                        "Ты должна одеваться так, когда мы наедине" if Cnt:
                                if Cnt == 5:
                                    $ KittyX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ KittyX.Clothing[9] = "custom3"
                                else:
                                    $ KittyX.Clothing[9] = "custom1"
                                ch_k "Конечно."

                        "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                menu:
                                    "Пользовательский 1 [[очистить слот 1]" if KittyX.Custom1[0]:
                                        ch_k "Ладно, без проблем."
                                        $ KittyX.Custom1[0] = 0
                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not KittyX.Custom1[0]:
                                        pass
                                    "Пользовательский 2 [[очистить слот 2]" if KittyX.Custom2[0]:
                                        ch_k "Ладно, без проблем."
                                        $ KittyX.Custom2[0] = 0
                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not KittyX.Custom2[0]:
                                        pass
                                    "Пользовательский 3 [[очистить слот 3]" if KittyX.Custom3[0]:
                                        ch_k "Ладно, без проблем."
                                        $ KittyX.Custom3[0] = 0
                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not KittyX.Custom3[0]:
                                        pass
                                    "Неважно [[назад]":
                                        pass

                        "Тебе следует надеть его [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                pass
                        "Тебе следует надеть его" if Cnt:
                            call Custom_Out(KittyX,Cnt)
                        "Ладно, вернемся к началу нашего разговора. . .":
                            $ Cnt = 0
                            return

        "Наденешь спортивную одежду?" if not KittyX.Taboo or bg_current == "bg dangerroom":
                $ KittyX.OutfitChange("gym")

        "Наденешь одежду для сна?" if not KittyX.Taboo:
                if ApprovalCheck(KittyX, 1200):
                        $ KittyX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(KittyX)
                        if _return:
                            $ KittyX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (KittyX.Taboo and bg_current != "bg pool" and not ApprovalCheck(KittyX, 800, TabM=2)) or not KittyX.Swim[0]:
                $ KittyX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not KittyX.Taboo or bg_current == "bg pool" or ApprovalCheck(KittyX, 800, TabM=2)) and KittyX.Swim[0]:
                $ KittyX.OutfitChange("swimwear")

        "Наденешь хэллоуинский костюм?" if "halloween" in KittyX.History:
                ch_k "Конечно."
                $ KittyX.OutfitChange("costume")

        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ KittyX.FaceChange("sexy", 1)
                $ Line = 0
                if not KittyX.Chest and not KittyX.Panties and not KittyX.Over and not KittyX.Legs and not KittyX.Hose:
                    ch_k "Ты же шутишь, да?"
                elif KittyX.SeenChest and KittyX.SeenPussy and ApprovalCheck(KittyX, 1200, TabM=4):
                    ch_k "[KittyX.Like]мрряу. . ."
                    $ Line = 1
                elif ApprovalCheck(KittyX, 2000, TabM=4):
                    ch_k "Ты же[KittyX.like]не валяешь дурака, да?"
                    $ Line = 1
                elif KittyX.SeenChest and KittyX.SeenPussy and ApprovalCheck(KittyX, 1200, TabM=0):
                    ch_k "[KittyX.Like]в таком виде меня можно хорошо разглядеть. . ."
                elif ApprovalCheck(KittyX, 2000, TabM=0):
                    ch_k "Может, когда мы будем наедине?"
                elif ApprovalCheck(KittyX, 1000, TabM=0):
                    $ KittyX.FaceChange("surprised", 2)
                    ch_k "[KittyX.Like]сначала тебе нужно сблизиться с девушкой, а потом уже просить о таком, [KittyX.Petname]."
                    $ KittyX.Blush = 1
                else:
                    $ KittyX.FaceChange("angry", 1)
                    ch_k "Ага[KittyX.like]так и есть."

                call expression KittyX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in KittyX.History:
                        $ Line = 0
                if Line:                                                            #If she got nude. . .
                    $ KittyX.OutfitChange("nude")
                    "Она позволяет всей своей одежде упасть к ее ногам."
                    call Girl_First_Topless(KittyX)
                    call Girl_First_Bottomless(KittyX,1)
                    $ KittyX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется. что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in KittyX.Traits:
                                ch_k "Я[KittyX.like]становлюсь влажной даже от одной мысли об этом."
                                $ KittyX.Outfit = "nude"
                                $ KittyX.Statup("Lust", 50, 10)
                                $ KittyX.Statup("Lust", 70, 5)
                                $ KittyX.Shame = 50
                            elif ApprovalCheck(KittyX, 800, "I") or ApprovalCheck(KittyX, 2800, TabM=0):
                                ch_k "Думаю, можно. . ."
                                $ KittyX.Outfit = "nude"
                                $ KittyX.Shame = 50
                            else:
                                $ KittyX.FaceChange("sexy", 1)
                                $ KittyX.Eyes = "surprised"
                                ch_k "Ни за что! Мне будет[KittyX.like]слишком неловко!"

                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in KittyX.Traits:
                                ch_k "Оу, неужели мне не придется?"
                            elif ApprovalCheck(KittyX, 800, "I") or ApprovalCheck(KittyX, 2800, TabM=0):
                                $ KittyX.FaceChange("bemused", 1)
                                if not Player.Male:
                                    ch_k "Хорошо, что ты не попросила меня ходить в подобном виде снаружи."
                                else:
                                    ch_k "Хорошо, что ты не попросил меня ходить в подобном виде снаружи."
                                ch_k ". . .Хорошо. . ."
                            else:
                                $ KittyX.FaceChange("confused", 1)
                                ch_k "Я бы[KittyX.like]не возражала против этого в наших комнатах, но точно не снаружи."
                $ Line = 0

        "Неважно":
            return #jump Kitty_Clothes

    return #jump Kitty_Clothes
    #End of Kitty Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Kitty_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять [get_clothing_name(KittyX.Over_key, vin)]?" if KittyX.Over:
                call Wardrobe_Remove(KittyX)

        "Примерь розовый топ." if KittyX.Over != "pink top":
                $ KittyX.FaceChange("bemused")
                if KittyX.Chest or KittyX.SeenChest:
                    ch_k "Ладно."
                elif ApprovalCheck(KittyX, 800, TabM=0):
                    ch_k "Ага, хорошо."
                else:
                    call Display_DressScreen(KittyX)
                    if not _return:
                            $ KittyX.FaceChange("bemused", 1)
                            ch_k "Без лифчика я буду выглядеть слегка непристойно."
                            return #jump Kitty_Clothes
                $ KittyX.Over = "pink top"

        "Как насчет твоей красной рубашки?" if KittyX.Over != "red shirt":
                $ KittyX.Over = "red shirt"
                ch_k "Ты про нее?"

        "Примерь красную куртку." if KittyX.Over != "jacket" and "halloween" in KittyX.History:
                $ KittyX.FaceChange("bemused")
                if KittyX.Chest or KittyX.SeenChest:
                    ch_k "Ладно."
                elif ApprovalCheck(KittyX, 900, TabM=0):
                    ch_k "Ага, хорошо."
                else:
                    call Display_DressScreen(KittyX)
                    if not _return:
                            $ KittyX.FaceChange("bemused", 1)
                            ch_k "Без лифчика я буду выглядеть слегка непристойно."
                            return #jump Kitty_Clothes
                $ KittyX.Over = "jacket"

        "Может, просто накинешь полотенце?" if KittyX.Over != "towel":
                $ KittyX.FaceChange("bemused", 1)
                if KittyX.Chest or KittyX.SeenChest:
                    ch_k "Чудила."
                elif ApprovalCheck(KittyX, 1000, TabM=0): #or showing screen
                    $ KittyX.FaceChange("perplexed", 1)
                    ch_k "Ладно? . ."
                else:
                    call Display_DressScreen(KittyX)
                    if not _return:
                            ch_k "Что-то не хочется."
                            return #jump Kitty_Clothes
                $ KittyX.Over = "towel"

        "Неважно":
            pass
    return #jump Kitty_Clothes
    #End of Kitty Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Kitty_NoBra: #fix test this
        menu:
            ch_k "Под [get_clothing_name(KittyX.Over_key, tvo)] у меня совсем ничего нет. . ."
            "Тогда надень какой-нибудь. . .":
                        if KittyX.SeenChest and ApprovalCheck(KittyX, 1000, TabM=3):
                                $ KittyX.Blush = 2
                                ch_k "-хотя это не такая уж и проблема. . ."
                                $ KittyX.Blush = 1
                        elif ApprovalCheck(KittyX, 1200, TabM=4):
                                $ KittyX.Blush = 2
                                ch_k "-хотя это не такая уж и проблема. . ."
                                $ KittyX.Blush = 1
                        elif ApprovalCheck(KittyX, 900, TabM=2) and "lace bra" in KittyX.Inventory:
                                ch_k "У меня есть{i}кое-что{/i} на примете."
                                $ KittyX.Chest  = "lace bra"
                                "Она достает кружевной лифчик и надевает его сквозь [get_clothing_name(KittyX.Over_key, vin)]."
                        elif ApprovalCheck(KittyX, 800, TabM=2):
                                ch_k "Да, наверное, твоя правда."
                                $ KittyX.Chest = "bra"
                                "Она достает лифчик и надевает его сквозь [get_clothing_name(KittyX.Over_key, vin)]."
                        elif ApprovalCheck(KittyX, 700, TabM=2):
                                ch_k "Да, наверное, твоя правда."
                                $ KittyX.Chest = "cami"
                                "Она достает ками и надевает его сквозь [get_clothing_name(KittyX.Over_key, vin)]."
                        elif ApprovalCheck(KittyX, 600, TabM=2):
                                ch_k "Да, наверное, твоя правда."
                                $ KittyX.Chest = "sports bra"
                                "Она достает спортивный лифчик и надевает его сквозь [get_clothing_name(KittyX.Over_key, vin)]."
                        else:
                                ch_k "Я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(KittyX, 1100, "LI", TabM=2) and KittyX.Love > KittyX.Inbt:
                                ch_k "Ну, наверное. . ."
                        elif ApprovalCheck(KittyX, 700, "OI", TabM=2) and KittyX.Obed > KittyX.Inbt:
                                ch_k "Конечно. . ."
                        elif ApprovalCheck(KittyX, 600, "I", TabM=2):
                                ch_k "Ага. . ."
                        elif ApprovalCheck(KittyX, 1300, TabM=2):
                                ch_k "Согласна."
                        else:
                                $ KittyX.FaceChange("surprised")
                                $ KittyX.Brows = "angry"
                                if KittyX.Taboo > 20:
                                    ch_k "Но не на людях, [KittyX.Petname]!"
                                else:
                                    ch_k "Ты мне не -настолько- нравишься, [KittyX.Petname]!"
                                call expression KittyX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0


            "Неважно":
                        ch_k "Ладно. . ."
                        return 0
        return 1
        #End of Kitty bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Kitty_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(KittyX.Legs_key, vin)]?" if KittyX.Legs:
                call Wardrobe_Remove(KittyX,1)

        "Ты отлично смотришься в капри." if KittyX.Legs != "capris":
                ch_k "Ага, хорошо."
                $ KittyX.Legs = "capris"

        "Тебе тебе очень идут черные джинсы." if KittyX.Legs != "black jeans":
                ch_k "Ладно, без проблем."
                $ KittyX.Legs = "black jeans"

        "Ты отлично смотришься в штанах для йоги." if KittyX.Legs != "yoga pants":
                ch_k "Ага, хорошо."
                $ KittyX.Legs = "yoga pants"

        "Как насчет надеть желтые шорты?" if KittyX.Legs != "shorts":
                ch_k "Ладно, без проблем."
                $ KittyX.Legs = "shorts"

        "Как насчет надеть синюю юбку?" if KittyX.Legs != "blue skirt" and "blue skirt" in KittyX.Inventory:
                if KittyX.Panties or ApprovalCheck(KittyX,500,"I",TabM=2):
                        ch_k "Ага, хорошо."
                        $ KittyX.Legs = "blue skirt"
                else:
                        ch_k "Она слегка откровенная. . ."

        "Примерь то розовое платье." if KittyX.Legs != "dress" and "halloween" in KittyX.History:
                menu:
                    ch_k "Полностью или только юбку?"
                    "Полностью.":
                            $ KittyX.Chest = "dress"
                    "Только юбку.":
                            pass
                $ KittyX.Legs = "dress"

        "Сними обувь (locked)" if not KittyX.Boots:
                pass
        "Сними [get_clothing_name(KittyX.Boots_key, vin)]" if KittyX.Boots:
                ch_p "Может, снимешь [get_clothing_name(KittyX.Boots_key, vin)]?"
                ch_k "Ладно, без проблем."
                $ KittyX.Boots = 0
#        "Add Boots" if KittyX.Boots != "boots":
#                ch_p "Maybe put your boots on."
#                ch_k "K, no problem."
#                $ KittyX.Boots = "boots"
        "Надень сандалии" if KittyX.Boots != "sandals":
                ch_p "Может, наденешь сандалии?"
                ch_k "Ладно, без проблем."
                $ KittyX.Boots = "sandals"

        "Неважно":
                pass
    return #jump Kitty_Clothes
    #End of Kitty Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Kitty_NoPantiesOn: #fix test this
        menu:
            ch_k "На мне[KittyX.like]нет трусиков."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if KittyX.SeenPussy and ApprovalCheck(KittyX, 1100, TabM=4):
                                $ KittyX.Blush = 2
                                ch_k "Я не говорила, что меня это беспокоит. . ."
                                $ KittyX.Blush = 1
                        elif ApprovalCheck(KittyX, 1500, TabM=4):
                                $ KittyX.Blush = 2
                                ch_k "Я не говорила, что меня это беспокоит. . ."
                                $ KittyX.Blush = 1
                        elif ApprovalCheck(KittyX, 800, TabM=4) and "lace panties" in KittyX.Inventory:
                                ch_k "Мне нравится ход твоих мыслей."
                                $ KittyX.Panties  = "lace panties"
                                "Она достает свои кружевные трусики и натягивает их на себя сквозь [get_clothing_name(KittyX.Panties_key, vin)]."
                        elif ApprovalCheck(KittyX, 700, TabM=4):
                                ch_k "Ага, пожалуй, стоит."
                                $ KittyX.Panties = "green panties"
                                "Она достает свои зеленые трусики и натягивает их на себя сквозь [get_clothing_name(KittyX.Panties_key, vin)]."
                        else:
                                ch_k "Я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(KittyX, 1100, "LI", TabM=3) and KittyX.Love > KittyX.Inbt:
                                ch_k "Ну, я не против, что ты все увидишь. . ."
                        elif ApprovalCheck(KittyX, 700, "OI", TabM=3) and KittyX.Obed > KittyX.Inbt:
                                ch_k "Наверное так. . ."
                        elif ApprovalCheck(KittyX, 600, "I", TabM=3):
                                ch_k "Хммм. . ."
                        elif ApprovalCheck(KittyX, 1300, TabM=3):
                                ch_k "Ага."
                        else:
                                $ KittyX.FaceChange("surprised")
                                $ KittyX.Brows = "angry"
                                if KittyX.Taboo > 20:
                                    ch_k "Но не на людях, [KittyX.Petname]!"
                                else:
                                    ch_k "Ты мне не -настолько- нравишься, [KittyX.Petname]!"
                                call expression KittyX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0

            "Неважно":
                ch_k "Ладно. . ."
                return 0
        return 1
        #End of Kitty Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Kitty_Clothes_Under:
        "Верх":
            menu:
                "Может, снимешь [KittyX.Chest]?" if KittyX.Chest:
                        $ KittyX.FaceChange("bemused", 1)
                        if KittyX.SeenChest and ApprovalCheck(KittyX, 900, TabM=2.7):
                            ch_k "Конечно."
                        elif ApprovalCheck(KittyX, 1100, TabM=2):
                            if KittyX.Taboo:
                                ch_k "Я немного нервничаю. . ."
                            else:
                                ch_k "Если только ради тебя. . ."
                        elif KittyX.Over == "pink top" and ApprovalCheck(KittyX, 600, TabM=2):
                            ch_k "Я буду выглядеть немного непристойно. . ."
                        elif KittyX.Over == "red shirt" and ApprovalCheck(KittyX, 500, TabM=2):
                            ch_k "Думаю, можно. . ."
                        elif not KittyX.Over:
                            call Display_DressScreen(KittyX)
                            if not _return:
                                ch_k "Я не могу. . ."
                                return #jump Kitty_Clothes
                        else:
                            call Display_DressScreen(KittyX)
                            if not _return:
                                ch_k "Я так не думаю, [KittyX.Petname]."
                                return #jump Kitty_Clothes

                        if KittyX.Over:
                            $ Line = get_clothing_name(KittyX.Chest_key, vin)
                            $ KittyX.Chest = 0
                            "Она вытягивает [Line] сквозь [get_clothing_name(KittyX.Over_key, vin)] и бросает на пол."
                        else:
                            $ Line = get_clothing_name(KittyX.Chest_key, dat)
                            $ KittyX.Chest = 0
                            "Она позволяет [Line] упасть на пол."
                            if not renpy.showing('DressScreen'):
                                call Girl_First_Topless(KittyX)

                "Примерь ками." if KittyX.Chest != "cami":
                        ch_k "Ладно."
                        $ KittyX.Chest = "cami"

                "Мне нравится твой лифчик без бретелек." if KittyX.Chest != "bra":
                        if KittyX.SeenChest or ApprovalCheck(KittyX, 1200, TabM=2):
                            ch_k "Ладно."
                            $ KittyX.Chest = "bra"
                        else:
                            call Display_DressScreen(KittyX)
                            if not _return:
                                ch_k "Мне не очень комфортно в нем. . ."
                            else:
                                $ KittyX.Chest = "bra"

                "Мне нравится твой кружевной лифчик." if "lace bra" in KittyX.Inventory and KittyX.Chest != "lace bra":
                        if KittyX.SeenChest or ApprovalCheck(KittyX, 1300, TabM=2):
                            ch_k "Ладно."
                            $ KittyX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(KittyX)
                            if not _return:
                                ch_k "Он очень прозрачный. . ."
                            else:
                                $ KittyX.Chest = "lace bra"

                "Мне нравится твой спортивный лифчик." if KittyX.Chest != "sports bra":
                        if KittyX.SeenChest or ApprovalCheck(KittyX, 1000, TabM=2):
                            ch_k "Ладно."
                            $ KittyX.Chest = "sports bra"
                        else:
                            call Display_DressScreen(KittyX)
                            if not _return:
                                ch_k "Я не уверена, что хочу его надевать. . ."
                            else:
                                $ KittyX.Chest = "sports bra"

                "Мне нравится твой лифчик бикини." if KittyX.Chest != "bikini top" and "bikini top" in KittyX.Inventory:
                        if bg_current == "bg pool":
                                ch_k "Ладно."
                                $ KittyX.Chest = "bikini top"
                        else:
                                if KittyX.SeenChest or ApprovalCheck(KittyX, 1000, TabM=2):
                                    ch_k "Ладно."
                                    $ KittyX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(KittyX)
                                    if not _return:
                                            ch_k "Боже, ну не здесь же!"
                                    else:
                                            $ KittyX.Chest = "bikini top"

                "Примерь то розовое платье." if KittyX.Chest != "dress" and "halloween" in KittyX.History:
                    if KittyX.SeenChest or ApprovalCheck(KittyX, 1000, TabM=2):
                            ch_k "Ладно."
                    else:
                        call Display_DressScreen(KittyX)
                        if not _return:
                            ch_k "Я не уверена, что хочу это делать. . ."
                            jump Kitty_Clothes_Under
                    menu:
                        ch_k "Полностью или только верхнюю часть?"
                        "Полностью.":
                                $ KittyX.Legs = "dress"
                        "Только верх.":
                                pass
                    $ KittyX.Chest = "dress"

                "Неважно":
                        pass
            jump Kitty_Clothes_Under

        "Варианты колготок и чулок":
                menu:
                    "Сними [get_clothing_name(KittyX.Hose_key, vin)]." if KittyX.Hose:
                            $ KittyX.Hose = 0
                    "Чулки дополнили бы твой образ." if KittyX.Hose != "stockings":
                            $ KittyX.Hose = "stockings"
                    "Гольфы дополнили бы твой образ." if KittyX.Hose != "knee stockings" and "knee" in KittyX.Inventory:
                            $ KittyX.Hose = "knee stockings"
                    "Колготки дополнили бы твой образ." if KittyX.Hose != "pantyhose" and "pantyhose" in KittyX.Inventory:
                            $ KittyX.Hose = "pantyhose"
                    "Рваные колготки дополнили бы твой образ." if KittyX.Hose != "ripped pantyhose" and "ripped pantyhose" in KittyX.Inventory:
                            $ KittyX.Hose = "ripped pantyhose"
                    "Чулки и пояс с подвязками дополнили бы твой образ." if KittyX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in KittyX.Inventory:
                            $ KittyX.Hose = "stockings and garterbelt"
                    "Может, наденешь только пояс с подвязками?" if KittyX.Hose != "garterbelt" and "stockings and garterbelt" in KittyX.Inventory:
                            $ KittyX.Hose = "garterbelt"
                    "Неважно":
                            pass
                jump Kitty_Clothes_Under

        #Panties
        "Низ":
            menu:
                "Ты должна снять [get_clothing_name(KittyX.Panties_key, vin)]. . ." if KittyX.Panties:
                        $ KittyX.FaceChange("bemused", 1)
                        if ApprovalCheck(KittyX, 900) and (KittyX.Legs or (KittyX.SeenPussy and not KittyX.Taboo)):
                            #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                            if ApprovalCheck(KittyX, 850, "L"):
                                    ch_k "Ну, если вежливо попросишь. . ."
                            elif ApprovalCheck(KittyX, 500, "O"):
                                    ch_k "Ладно, но только ради тебя."
                            elif ApprovalCheck(KittyX, 350, "I"):
                                    ch_k "[[фыркает]."
                            else:
                                    if not Player.Male:
                                        ch_k "Ага, наверное ты права."
                                    else:
                                        ch_k "Ага, наверное ты прав."
                        else:                       #low approval or not wearing pants or in public
                            if ApprovalCheck(KittyX, 1100, "LI", TabM=3) and KittyX.Love > KittyX.Inbt:
                                    ch_k "Ну, я не против, что ты все увидишь. . ."
                            elif ApprovalCheck(KittyX, 700, "OI", TabM=3) and KittyX.Obed > KittyX.Inbt:
                                    ch_k "Наверное. . ."
                            elif ApprovalCheck(KittyX, 600, "I", TabM=3):
                                    ch_k "Хммм. . ."
                            elif ApprovalCheck(KittyX, 1300, TabM=3):
                                    ch_k "Ладно-ладно."
                            else:
                                call Display_DressScreen(KittyX)
                                if not _return:
                                    $ KittyX.FaceChange("surprised")
                                    $ KittyX.Brows = "angry"
                                    if KittyX.Taboo > 20:
                                        ch_k "Не на людях, [KittyX.Petname]!"
                                    else:
                                        ch_k "Ты мне не так сильно нравишься, [KittyX.Petname]!"
                                    return #jump Kitty_Clothes

                        if KittyX.Legs:
                            $ Line = get_clothing_name(KittyX.Panties_key, vin)
                            $ KittyX.Panties = 0
                            "Она залазит в карман, хватает что-то, а затем вытаскивает [Line] и кидает их на пол."
                        else:
                            $ Line = get_clothing_name(KittyX.Panties_key, dat)
                            $ KittyX.Panties = 0
                            "Она позволяет [Line] упасть на пол."
                            if  not renpy.showing('DressScreen'):
                                call Girl_First_Bottomless(KittyX)
                                $ KittyX.Statup("Inbt", 50, 2)

                "Почему бы тебе вместо этих не надеть зеленые трусики?" if KittyX.Panties and KittyX.Panties != "green panties":
                        if ApprovalCheck(KittyX, 1100, TabM=3):
                                ch_k "Ладно."
                                $ KittyX.Panties = "green panties"
                        else:
                                call Display_DressScreen(KittyX)
                                if not _return:
                                    ch_k "Не думаю, что тебя это должно волновать."
                                else:
                                    $ KittyX.Panties = "green panties"

                "Почему бы тебе вместо этих не надеть кружевные трусики?" if "lace panties" in KittyX.Inventory and KittyX.Panties and KittyX.Panties != "lace panties":
                        if ApprovalCheck(KittyX, 1300, TabM=3):
                                ch_k "Думаю, можно."
                                $ KittyX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(KittyX)
                                if not _return:
                                    ch_k "Не лезь[KittyX.like]не в свое дело."
                                else:
                                    $ KittyX.Panties = "lace panties"

                "Мне нравятся твои трусики бикини." if KittyX.Panties != "bikini bottoms" and "bikini bottoms" in KittyX.Inventory:
                        if bg_current == "bg pool":
                                ch_k "Ладно."
                                $ KittyX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(KittyX, 1000, TabM=2):
                                    ch_k "Ладно."
                                    $ KittyX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(KittyX)
                                    if not _return:
                                        ch_k "Боже, ну не здесь же!"
                                    else:
                                        $ KittyX.Panties = "bikini bottoms"

                "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not KittyX.Panties:
                        $ KittyX.FaceChange("bemused", 1)
                        if KittyX.Legs and (KittyX.Love+KittyX.Obed) <= (2 * KittyX.Inbt):
                            $ KittyX.Mouth = "smile"
                            ch_k "Думаю, я. . . предпочла бы не делать это."
                            menu:
                                "Ну ладно.":
                                    return #jump Kitty_Clothes
                                "Я настаиваю, надевай.":
                                    if (KittyX.Love+KittyX.Obed) <= (1.5 * KittyX.Inbt):
                                        $ KittyX.FaceChange("angry", Eyes="side")
                                        ch_k "Не хочу тебя расстраивать, но нет."
                                        return #jump Kitty_Clothes
                                    else:
                                        $ KittyX.FaceChange("sadside")
                                        ch_k "Ладно, ЛАДНО."
                        menu:
                            ch_k "Наверное. . ."
                            "Как насчет зеленых?":
                                ch_k "Ладно, конечно."
                                $ KittyX.Panties = "green panties"
                            "Как насчет кружевных?" if "lace panties" in KittyX.Inventory:
                                ch_k "Ладно."
                                $ KittyX.Panties  = "lace panties"
                "Неважно":
                        pass
            jump Kitty_Clothes_Under
        "Неважно":
                pass
    return #jump Kitty_Clothes
    #End of Kitty Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Kitty_Clothes_Misc:
        #Misc
        "Хвост" if KittyX.Hair != "evo":
                ch_p "Тебе идет хвост."
                if ApprovalCheck(KittyX, 600):
                    ch_k "Типа так?"
                    $ KittyX.Hair = "evo"
                else:
                    ch_k "Ага, я знаю."

        "Распущенные волосы" if KittyX.Hair != "long":
                ch_p "Тебе идут распущенные волосы."
                if ApprovalCheck(KittyX, 600):
                    ch_k "Думаешь?"
                    $ KittyX.Hair = "long"
                else:
                    ch_k "Я[KittyX.like]не собираюсь ничего менять."

        "Влажная укладка волос" if KittyX.Hair != "wet":
                ch_p "Тебе стоит увлажнить волосы."
                if ApprovalCheck(KittyX, 800):
                    ch_k "Ты так думаешь?"
                    "Она роется в сумке, затем достает немного геля и втирает его в волосы."
                    ch_k "Типа так?"
                    $ KittyX.Hair = "wet"
                else:
                    ch_k "Это слишком сложно устроить."

        "Отрасти волосы на лобке" if not KittyX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может отрастишь?"
                call expression KittyX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in KittyX.Todo:
                    ch_k "[[фыркает] Тебе придется подождать!"
                else:
                    $ KittyX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(KittyX, 1150, TabM=0)
                    if ApprovalCheck(KittyX, 850, "L", TabM=0) or (Approval and KittyX.Love > 2 * KittyX.Obed):
                        ch_k "Думаю, можно. . ."
                    elif ApprovalCheck(KittyX, 500, "I", TabM=0) or (Approval and KittyX.Inbt > KittyX.Obed):
                        ch_k "Ты хочешь ласкать пушистую кисоньку?"
                    elif ApprovalCheck(KittyX, 400, "O", TabM=0) or Approval:
                        ch_k "Если ты так этого хочешь. . ."
                    else:
                        $ KittyX.FaceChange("surprised")
                        $ KittyX.Brows = "angry"
                        ch_k "Тебя это не касается, [KittyX.Petname]."
                        return #jump Kitty_Clothes
                    $ KittyX.Todo.append("pubes")
                    $ KittyX.PubeC = 6

        "Побрей лобок" if KittyX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression KittyX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ KittyX.FaceChange("bemused", 1)
                if "shave" in KittyX.Todo:
                        ch_k "Знаю, знаю. Я позабочусь об этом попозже."
                else:
                        $ Approval = ApprovalCheck(KittyX, 1150, TabM=0)

                        if ApprovalCheck(KittyX, 850, "L", TabM=0) or (Approval and KittyX.Love > 2 * KittyX.Obed):
                            ch_k "Думаю, я могла бы побрить. . ."
                        elif ApprovalCheck(KittyX, 500, "I", TabM=0) or (Approval and KittyX.Inbt > KittyX.Obed):
                            ch_k "Я буду держать его гладеньким."
                        elif ApprovalCheck(KittyX, 400, "O", TabM=0) or Approval:
                            ch_k "Я все сделаю."
                        else:
                            $ KittyX.FaceChange("surprised")
                            $ KittyX.Brows = "angry"
                            ch_k "Тебя это не касается, [KittyX.Petname]."
                            return #jump Kitty_Clothes
                        $ KittyX.Todo.append("shave")

        "Пирсинг [[Сначала посмотрите, как она выглядит без него] (locked)" if not KittyX.SeenPussy and not KittyX.SeenChest:
            pass

        "Надень пирсинг-кольца" if KittyX.Pierce != "ring" and (KittyX.SeenPussy or KittyX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсингом-кольцами."
                if "ring" in KittyX.Todo:
                    ch_k "Знаю, знаю. Я позабочусь об этом попозже."
                else:
                    $ KittyX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(KittyX, 1350, TabM=0)
                    if ApprovalCheck(KittyX, 900, "L", TabM=0) or (Approval and KittyX.Love > 2* KittyX.Obed):
                        ch_k "Ну, если ты думаешь, что он будут мне к лицу. . ."
                    elif ApprovalCheck(KittyX, 600, "I", TabM=0) or (Approval and KittyX.Inbt > KittyX.Obed):
                        ch_k "Я тоже думаю, что он будет отлично смотреться на мне!"
                    elif ApprovalCheck(KittyX, 500, "O", TabM=0) or Approval:
                        ch_k "Ладно, я позабочусь об этом."
                    else:
                        $ KittyX.FaceChange("surprised")
                        $ KittyX.Brows = "angry"
                        ch_k "Тебя это не касается, [KittyX.Petname]."
                        return #jump Kitty_Clothes
                    $ KittyX.Todo.append("ring")

        "Надень пирсинг-штанги" if KittyX.Pierce != "barbell" and (KittyX.SeenPussy or KittyX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in KittyX.Todo:
                    ch_k "Знаю, знаю. Я позабочусь об этом попозже."
                else:
                    $ KittyX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(KittyX, 1350, TabM=0)
                    if ApprovalCheck(KittyX, 900, "L", TabM=0) or (Approval and KittyX.Love > 2 * KittyX.Obed):
                        ch_k "Ну, если ты думаешь, что он будут мне к лицу. . ."
                    elif ApprovalCheck(KittyX, 600, "I", TabM=0) or (Approval and KittyX.Inbt > KittyX.Obed):
                        ch_k "Я тоже думаю, что он будет отлично смотреться на мне!"
                    elif ApprovalCheck(KittyX, 500, "O", TabM=0) or Approval:
                        ch_k "Ладно, я позабочусь об этом."
                    else:
                        $ KittyX.FaceChange("surprised")
                        $ KittyX.Brows = "angry"
                        ch_k "Тебя это не касается, [KittyX.Petname]."
                        return #jump Kitty_Clothes
                    $ KittyX.Todo.append("barbell")

        "Сними пирсинг" if KittyX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ KittyX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(KittyX, 1350, TabM=0)
                if ApprovalCheck(KittyX, 950, "L", TabM=0) or (Approval and KittyX.Love > KittyX.Obed):
                    ch_k "Ну, если он тебе мешает. . ."
                elif ApprovalCheck(KittyX, 700, "I", TabM=0) or (Approval and KittyX.Inbt > KittyX.Obed):
                    ch_k "Он начал меня раздражать."
                elif ApprovalCheck(KittyX, 600, "O", TabM=0) or Approval:
                    ch_k "Тогда я его сниму."
                else:
                    $ KittyX.FaceChange("surprised")
                    $ KittyX.Brows = "angry"
                    ch_k "Ну, {i}мне{/i} он, вроде как, нравится."
                    return #jump Kitty_Clothes
                $ KittyX.Pierce = 0

        "Надень золотое ожерелье" if KittyX.Neck != "gold necklace":
                ch_p "Почему бы тебе не надеть золотое ожерелье?"
                ch_k "Ладно. . ."
                $ KittyX.Neck = "gold necklace"
        "Надень ожерелье со звездой" if KittyX.Neck != "star necklace":
                ch_p "Почему бы тебе не надеть ожерелье со звездой?"
                ch_k "Ладно. . ."
                $ KittyX.Neck = "star necklace"
        "Надень ожерелье с цветком" if KittyX.Neck != "flower necklace" and "halloween" in KittyX.History:
                ch_p "Почему бы тебе не надеть ожерелье с цветком?"
                ch_k "Ладно. . ."
                $ KittyX.Neck = "flower necklace"

        "Сними украшение с шеи" if KittyX.Neck:
                ch_k "Ладно. . ."
                $ KittyX.Neck = 0


        "Неважно":
            pass
    return #jump Kitty_Clothes
    #End of Kitty Misc Wardrobe

return
#End Kitty Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
