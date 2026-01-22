#Start Date_Shopping   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Mall_Entry(First=0,Second=0,Girl=0,Cart=[]):
        # Modification mode
        $ play_music(name=audio.mall_location)
        # -----------------
        call Jubes_Entry_Check
        $ Player.DrainWord("locked",0,0,1)
        call Drain_Nearby #empties .Loc "nearby"
        $ bg_current = "bg mall"
        call Gym_Clothes_Off #call Gym_Clothes
        call Taboo_Level
        $ Player.RecentActions.append("traveling")
        call EventCalls

label Shopping_Mall(First=0,Second=0,Girl=0,Cart=[]):
        # Modification mode
        if is_playing_music(audio.mall_location):
            $ play_music(name=audio.mall_location)
        # -----------------
        #this is the mall
        $ bg_current = "bg mall"
        $ Player.RecentActions.append("shopping")
        $ Player.DailyActions.append("shopping")
        python:
            for BX in Party:
                BX.Loc = "bg mall"

        call Set_The_Scene #should remove anyone extra to "nearby."
        "Вы находитесь в торговом центре Salem Center."
        if len(Party) >= 2:
                $ First = Party[0]
                $ Second = Party[1]
                "Вы ходите по различным магазинам с девушками и рассматриваете предлагаемый ассортимент товаров. . ."
        elif len(Party) >= 1:
                $ First = Party[0]
                $ Second = 0
                "Вы с [Party[0].Name_tvo] ходите по различным магазинам и рассматриваете предлагаемый ассортимент товаров. . ."
        else:
                "Вы ходите по различным магазинам и рассматриваете предлагаемый ассортимент товаров. . ."
        if First in TotalGirls:
                call Shift_Focus(First)
        menu Mall_Menu:
            "Куда бы вы хотели пойти?"
            "Войти в Секс-Шоп" if Round > 20:
                    call Sex_Shop

            "Войти в Магазин Нижнего Белья" if Round > 20:
                    call Lingerie_Shop

            "Войти в Магазин Купальников" if Round > 20:
                    call Swim_Shop

            "Переместиться ближе к другим девушкам" if Nearby and "date" not in Player.RecentActions:
                    call Swap_Nearby("menu")

            #special dating options
            "Просто бродить и разглядывать витрины" if Round > 20:
                    #only during date
                    if len(Party) >= 2:
                            if renpy.random.randint(1, 20) > 10:
                                    $ Party[0].Statup("Love", 80, 1)
                                    $ Party[0].Statup("Obed", 50, 1)
                                    $ Party[0].Statup("Inbt", 50, 1)
                                    $ Party[1].Statup("Love", 80, 1)
                                    $ Party[1].Statup("Obed", 50, 1)
                                    $ Party[1].Statup("Inbt", 50, 1)
                            "Вы ходите с девушками и смотрите, какие товары есть в наличии."
                    elif Party:
                            if renpy.random.randint(1, 20) > 10:
                                    $ Party[0].Statup("Love", 80, 1)
                                    $ Party[0].Statup("Obed", 50, 1)
                                    $ Party[0].Statup("Inbt", 50, 1)
                            "Вы с [Party[0].Name_tvo] гуляете и смотрите, какие товары есть в наличии."
                    else:
                            "Вы ходите и смотрите, какие товары есть в наличии."
                    $ Round -= 10

            "Заняться чем-нибудь другим" if "date" in Player.RecentActions and Round > 20:
                    #only during date
                    jump Date_Location

            "Вернуться в институт" if "date" in Player.RecentActions:
                    #only during date
                    if "movie" in Player.RecentActions or "dinner" in Player.RecentActions or Round < 30 or not Party:
                            show blackscreen onlayer black with dissolve
                            "Уже поздно, вы возвращаетесь в общежитие. . ."
                            jump Date_End
                    else:
                            #if there's still time and not much has happened. . .
                            if Party[0] in (EmmaX,StormX):
                                    call AnyLine(Party[0],"Ох, я ожидала большего. . .")
                            elif Party[0] in (JeanX,LauraX):
                                    call AnyLine(Party[0],"Это все?")
                            else:
                                    call AnyLine(Party[0],"Оу. . . мы больше никуда не пойдем?")
                            menu:
                                "Продолжить Покупки":
                                        jump Mall_Menu
                                "Заняться чем-нибудь другим":
                                        jump Date_Location
                                "Вернуться в институт [[на этот раз серьезно]":
                                        ch_p "Ага, пора возвращаться."
                                        call AnyLine(Party[0],"Ладно. . .")
                                        show blackscreen onlayer black with dissolve
                                        "Уже поздно, вы возвращаетесь в общежитие. . ."
                                        jump Date_End

            "Немного подождать" if "date" not in Player.RecentActions:
                    #set to not during date
                    "Вы немного ждете."
                    call Wait
                    call EventCalls
                    call Girls_Location
                    if Time_Count >= 3: #night time
                        ch_u "Торговый центр закрывается, пожалуйста, пройдите к ближайшему выходу. . ."
                        "Вы возвращаетесь в кампус."
                        jump Campus_Entry

            "Вернуться в институт" if "date" not in Player.RecentActions:
                    #set to not during date
                    jump Campus_Entry

        if Time_Count >= 3 or Round < 20:
                if "date" in Player.RecentActions:
                        #if on a date
                        show blackscreen onlayer black with dissolve
                        "Уже поздно, вы возвращаетесь в общежитие. . ."
                        jump Date_End
                ch_u "Торговый центр закрывается, пожалуйста, пройдите к ближайшему выходу. . ."
                "Вы возвращаетесь в кампус."
                jump Campus_Entry
        if not Party:
                if "date" in Player.RecentActions:
                        #if on a date
                        $ Player.DrainWord("date",1,0,0)
        jump Mall_Menu


label Sex_Shop: #rkeljsvgb
        # Modification mode
        if is_playing_music(audio.mall_location):
            $ play_music(name=audio.mall_location)
        # -----------------
        # jumped to from Mall Menu
        $ bg_current = "bg shop"
        python:
            for BX in Party:
                BX.Loc = "bg shop"

        call Set_The_Scene
        $ Girl = 0
        "Вы направляетесь в \"Спираль\", магазин товаров для взрослых . . ."
        while True:
                if Round <= 20:
                    "Уже поздно, вы возвращаетесь в торговый центр. . ."
                    $ Girl = 0
                    return
                menu:
                    "Что вы хотели бы приобрести?"
                    "Купить фаллоимитатор за $20.":
                            if Player.Inventory.count("dildo") >= 10:
                                "У вас в наличии гораздо больше фаллоимитаторов, чем вам нужно. 2, 4, 6. . . да, слишком много."
                            elif Player.Cash >= 20:
                                "Вы покупаете один фаллоимитатор."
                                $ Player.Inventory.append("dildo")
                                $ Player.Cash -= 20
                                if First and "buy dildo" not in Player.DailyActions:
                                    if ApprovalCheck(First, 800) or not Player.Male:
                                        $ First.FaceChange("sly")
                                        $ First.Statup("Love", 80, 1)
                                        $ First.Statup("Obed", 50, 3)
                                        $ First.Statup("Inbt", 50, 3)
                                        if First is RogueX:
                                                ch_r "О, а это для чего, [First.Petname]?"
                                        elif First is KittyX:
                                                ch_k "Это для. . ."
                                        elif First is EmmaX:
                                                ch_e "Хмм. . ."
                                        elif First is LauraX:
                                                ch_l ". . ."
                                        elif First is JeanX:
                                                pass
                                        elif First is StormX:
                                                ch_s "Что ж, это, безусловно, интересно. . ."
                                        elif First is JubesX:
                                                ch_v "Что ты собираешься с этим делать. . ."
                                        elif First is GwenX:
                                                ch_g "Ох, интересная покупка. . ."
                                        elif First is BetsyX:
                                                ch_b "Что ж, это довольно необычно. . ."
                                        elif First is DoreenX:
                                                ch_d "Ох, хех. . ."
                                        elif First is WandaX:
                                                ch_w "Ладно. . ."
                                    else:
                                        $ First.FaceChange("confused",2)
                                        $ First.Statup("Love", 60, -2)
                                        $ First.Statup("Obed", 70, 4)
                                        $ First.Statup("Inbt", 50, 2)
                                        if First is RogueX:
                                                ch_r "Это. . . ох. . ."
                                        elif First is KittyX:
                                                ch_k "Эм, что это значит. . ."
                                        elif First is EmmaX:
                                                ch_e "Это определенно необычная прогулка. . ."
                                        elif First is LauraX:
                                                ch_l ". . ."
                                        elif First is JeanX:
                                                pass #ch_j "Eye on the prize, [First.Petname]."
                                        elif First is StormX:
                                                ch_s "Интересный выбор. . ."
                                        elif First is JubesX:
                                                ch_v "Что ты собираешься с этим делать. . ?"
                                        elif First is GwenX:
                                                ch_g "Хм. . ."
                                        elif First is BetsyX:
                                                ch_b "Это. . . ох, ясно. . ."
                                        elif First is DoreenX:
                                                ch_d "Ох, хех. . . а мне точно нужно здесь быть?"
                                        elif First is WandaX:
                                                if Player.Male:
                                                        ch_w "Ты не мог купить игрушки без меня? . ."
                                                else:
                                                        ch_w "Ты не могла купить игрушки без меня? . ."
                                        $ First.FaceChange("confused",1)
                                    $ First.Statup("Lust", 60, 5)
                                    $ Player.AddWord(1,0,"buy dildo",0,0) #daily
                            else:
                                    "У Вас не хватит на это денег."

                    "Купить вибратор за $25.":
                            if Player.Inventory.count("vibrator") >= 10:
                                "Если вы купите еще один вибратор, вы рискуете вызвать геологическую катастрофу."
                            elif Player.Cash >= 25:
                                "Вы покупаете один вибратор."
                                $ Player.Inventory.append("vibrator")
                                $ Player.Cash -= 25
                                if First and "buy vibe" not in Player.DailyActions:
                                    if ApprovalCheck(First, 800) or not Player.Male:
                                        $ First.FaceChange("sly")
                                        $ First.Statup("Love", 80, 2)
                                        $ First.Statup("Obed", 50, 2)
                                        $ First.Statup("Inbt", 50, 3)
                                        if First is RogueX:
                                                ch_r "О, а это для чего, [First.Petname]?"
                                        elif First is KittyX:
                                                ch_k "Это для. . ."
                                        elif First is EmmaX:
                                                ch_e "Хмм. . ."
                                        elif First is LauraX:
                                                ch_l ". . ."
                                        elif First is JeanX:
                                                pass
                                        elif First is StormX:
                                                ch_s "Что ж, это, безусловно, интересно. . ."
                                        elif First is JubesX:
                                                ch_v "Что ты собираешься с этим делать. . ."
                                        elif First is GwenX:
                                                ch_g "Это же. . ."
                                        elif First is BetsyX:
                                                ch_b "Ох, ясно. . ."
                                        elif First is DoreenX:
                                                ch_d "Ох, хех. . ."
                                        elif First is WandaX:
                                                ch_w "Ладно. . ."
                                        $ First.Statup("Lust", 60, 5)
                                    else:
                                        $ First.FaceChange("confused",2)
                                        $ First.Statup("Obed", 70, 2)
                                        $ First.Statup("Inbt", 50, 2)
                                        if First is RogueX:
                                                ch_r "Это. . . ох. . ."
                                        elif First is KittyX:
                                                ch_k "Эм, что это значит. . ."
                                        elif First is EmmaX:
                                                ch_e "Это определенно необычная прогулка. . ."
                                        elif First is LauraX:
                                                ch_l ". . ."
                                        elif First is JeanX:
                                                pass
                                        elif First is StormX:
                                                ch_s "Интересный выбор. . ."
                                        elif First is JubesX:
                                                ch_v "Что ты собираешься с этим делать. . ?"
                                        elif First is GwenX:
                                                ch_g "Хм. . ."
                                        elif First is BetsyX:
                                                ch_b "Ох, это точно не какое-то недоразумение? . ."
                                        elif First is DoreenX:
                                                ch_d "Ох, хех. . . а мне точно нужно здесь быть?"
                                        elif First is WandaX:
                                                if Player.Male:
                                                        ch_w "Ты не мог купить игрушки без меня? . ."
                                                else:
                                                        ch_w "Ты не могла купить игрушки без меня? . ."
                                        $ First.FaceChange("confused",1)
                                    $ Player.AddWord(1,0,"buy vibe",0,0) #daily
                            else:
                                        "У Вас не хватит на это денег."
                    "Купить анальную пробку за $30.":
                            if Player.Inventory.count("plug") >= 10:
                                "У вас в наличии гораздо больше анальных пробок, чем вам понадобится. 2, 4, 6. . . да, очень много."
                            elif Player.Cash >= 30:
                                "Вы покупаете одну анальную пробку."
                                $ Player.Inventory.append("plug")
                                $ Player.Cash -= 30
                                if First and "buy plug" not in Player.DailyActions:
                                    if ApprovalCheck(First, 900) or not Player.Male:
                                        $ First.FaceChange("sly")
                                        $ First.Statup("Obed", 50, 5)
                                        $ First.Statup("Inbt", 50, 4)
                                        if First is RogueX:
                                                ch_r "Для чего это, [First.Petname]?"
                                        elif First is KittyX:
                                                ch_k "Она для. . ."
                                        elif First is EmmaX:
                                                ch_e "Интересно. . ."
                                        elif First is LauraX:
                                                ch_l "Ох, ты значит из этих. . ."
                                        elif First is JeanX:
                                                ch_j "Хм. . ."
                                        elif First is StormX:
                                                ch_s "Ты покупаешь интересные вещи. . ."
                                        elif First is JubesX:
                                                ch_v "Это для. . ?"
                                        elif First is GwenX:
                                                ch_g "Ох, эм. . ."
                                        elif First is BetsyX:
                                                ch_b "Я несколько озадачена. . ."
                                        elif First is DoreenX:
                                                ch_d "О, что это? Какой-то игрушечный желудь?"
                                        elif First is WandaX:
                                                ch_w "Выглядит. . . интересно. . ."
                                    else:
                                        $ First.FaceChange("confused",2)
                                        $ First.Statup("Love", 60, -5)
                                        $ First.Statup("Love", 80, -1)
                                        $ First.Statup("Obed", 80, 4)
                                        $ First.Statup("Inbt", 70, 2)
                                        if First is RogueX:
                                                ch_r "Это. . . ох. . ."
                                        elif First is KittyX:
                                                ch_k "Эм, что это значит. . ."
                                        elif First is EmmaX:
                                                ch_e "Я не знала, что ты увлекаешься такими вещами. . ."
                                        elif First is LauraX:
                                                ch_l "Для тебя или. . ."
                                        elif First is JeanX:
                                                ch_j "Тебе нужна помощь, чтобы вставить ее?"
                                        elif First is StormX:
                                                ch_s "Интересный выбор. . ."
                                        elif First is JubesX:
                                                ch_v "Что ты собираешься с этим делать. . ?"
                                        elif First is GwenX:
                                                ch_g "Это же не для. . ?"
                                        elif First is BetsyX:
                                                ch_b "Это же не для. . ?"
                                        elif First is DoreenX:
                                                ch_d "Воу, это какой-то игрушечный желудь?"
                                        elif First is WandaX:
                                                ch_w "Покупай подобные вещи без меня."
                                        $ First.FaceChange("confused",1)
                                    $ First.Statup("Lust", 60, 5)
                                    $ Player.AddWord(1,0,"buy plug",0,0) #daily
                            else:
                                    "У Вас не хватит на это денег."



                    "Сделать подарок [First.Name_dat]." if First:
                            $ Girl = First
                            call Gifts
                            $ Girl = 0
                    "Сделать подарок [Second.Name_dat]." if Second:
                            $ Girl = Second
                            call Gifts
                            $ Girl = 0
                    "Выход.":
                            "Вы возвращаетесь в торговый центр. . ."
                            $ Round -= 10 if Round > 20 else (Round-10) #reduces Round to at minimum 10
                            $ Girl = 0
                            $ bg_current = "bg mall"
                            python:
                                for BX in Party:
                                    BX.Loc = "bg mall"

                            call Set_The_Scene
                            return

                #End shop menu
        # end Body Shoppe while loop
        return

#End Sex Shop   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Swim_Shop: #rkeljsvgb
        #this one will loop the "try something on menu" until you leave,
        #if you pick a girl, it sees if she's willing to try stuff on.
        #if she is, it loops the "dressing room" area until you try to leave
        #then it loops the "empty cart" menu until it's empty.

        # Modification mode
        if is_playing_music(audio.mall_location):
            $ play_music(name=audio.mall_location)
        # -----------------
        $ bg_current = "bg shop"
        python:
            for BX in Party:
                BX.Loc = "bg shop"

        call Set_The_Scene
        $ Girl = 0
        "Вы направляетесь в \"Купальный Вопрос\". . ."
        while True:
                if Round <= 20:
                    "Уже поздно, вы возвращаетесь в торговый центр. . ."
                    $ Girl = 0
                    return
                menu:
                    "Что вы хотели бы?"
                    "Пусть [First.Name] что-нибудь примерит." if First:
                            $ Girl = First
                    "Пусть [Second.Name] что-нибудь примерит." if Second:
                            #swaps first and second
                            $ Girl = Second
                            $ Second = First
                            $ First = Girl
                    "Купить что-нибудь на потом" if not First:
                            call Swim_Shop_Menu
                    "Выход.":
                            "Вы возвращаетесь в торговый центр. . ."
                            $ Girl = 0
                            $ bg_current = "bg mall"
                            python:
                                for BX in Party:
                                    BX.Loc = "bg mall"

                            call Set_The_Scene
                            return
                #End shop menu

                if Girl:
                        #checks if they are ok with shopping for bikinis with you, kicks out if not
                        $ Girl.FaceChange("smile",1)
                        if Girl.Swim[0] and not ApprovalCheck(Girl, 1200):
                            #if she already has a suit. . .
                            if Girl is RogueX:
                                    ch_r "У меня уже есть комплект. . ."
                            elif Girl is KittyX:
                                    ch_k "Я[KittyX.like]не думаю, что мне очень уж нужен -еще- один. . ."
                            elif Girl is EmmaX:
                                    ch_e "Мне больше не нужен купальник. . ."
                            elif Girl is LauraX:
                                    ch_l "У меня уже есть купальник. . ."
                            elif Girl is JeanX:
                                    ch_j "О, мне не нужен еще один купальник."
                            elif Girl is StormX:
                                    ch_s "У меня их предостаточно . ."
                            elif Girl is JubesX:
                                    ch_v "У меня уже есть один!"
                            elif Girl is GwenX:
                                    ch_g "Мне он больше не нужен."
                            elif Girl is BetsyX:
                                    ch_b "Пожалуй, я уже хорошо подготовлена. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ну, у меня уже есть купальник. . ."
                            elif Girl is WandaX:
                                    ch_w "У меня уже есть купальник. . ."
                            $ Girl = 0
                        elif ApprovalCheck(Girl, 800) or ApprovalCheck(Girl, 600, "L") or ApprovalCheck(Girl, 300, "O") or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                            #if she agrees. . .
                            if Girl is RogueX:
                                    ch_r "Ох, мы ищем миленький купальник?"
                            elif Girl is KittyX:
                                    ch_k "Ох, эм, думаю, мы могли бы купить купальник. . ."
                            elif Girl is EmmaX:
                                    ch_e "Полагаю, мы могли бы что-нибудь выбрать. . ."
                            elif Girl is LauraX:
                                    ch_l "Ох, думаю, мне на самом деле нужен купальник. . ."
                            elif Girl is JeanX:
                                    ch_j "Ох, к чему ты клонишь?"
                            elif Girl is StormX:
                                    ch_s "Пожалуй, мне стоит купить что-нибудь для бассейна. . ."
                            elif Girl is JubesX:
                                    ch_v "Думаю, мне нужен новый купальник. . ."
                            elif Girl is GwenX:
                                    ch_g "Думаю, мне не помешает новый купальник. . ."
                            elif Girl is BetsyX:
                                    ch_b "Пожалуй, мне не помешал бы новый купальник. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ну, у нас в кампусе есть хороший бассейн. . ."
                            elif Girl is WandaX:
                                    ch_w "Пожалуй, мне не помешал бы какой-нибудь купальник. . ."
                        else:
                            if Girl is RogueX:
                                    ch_r "Ох, нет, спасибо."
                            elif Girl is KittyX:
                                    ch_k "Ох, эм, мне он совсем не нужен. . ."
                            elif Girl is EmmaX:
                                    ch_e "Думаю, это слегка неуместно.. . ."
                            elif Girl is LauraX:
                                    ch_l "Не интересует. . ."
                            elif Girl is JeanX:
                                    ch_j "Нет, не нужно."
                            elif Girl is StormX:
                                    ch_s "Не думаю, что мне следует. . ."
                            elif Girl is JubesX:
                                    ch_v "Я не очень хочу покупать это. . ."
                            elif Girl is GwenX:
                                    ch_g "Я, наверное, возьму какой-нибудь, когда у меня будет свободное время. . ."
                            elif Girl is BetsyX:
                                    ch_b "Если он мне понадобится, я уверена, что смогу сама его купить. . ."
                            elif Girl is DoreenX:
                                    ch_d "Мне. . . не особо нужен купальник. . ."
                            elif Girl is WandaX:
                                    ch_w "Нет, мне ничего не нужно. . ."
                            $ Girl = 0
                #end checks if they are ok with shopping for bikinis with you, kicks out if not

                if Girl:
                    #if she agreed to shop for a suit. . .
                    call Shift_Focus(Girl)
                    "Вы берете вещи и направляетесь в одну из раздевалок с [Girl.Name_tvo]."
                    $ bg_current = "bg dressing"
                    $ Girl.Loc = "bg dressing"
                    if Second:
                        #if there is a second girl
                        "Стоит ли [Second.Name_dat] к вам присоединиться?"
                        menu:
                            "Конечно":
                                    "[Second.Name] следует за вами."
                                    $ Second.Loc = "bg dressing"
                            "Это вряд ли.":
                                    ch_p "[Second.Name], тебе, пожалуй, стоит остаться."
                                    call AnyLine(Second,"Ладно. Я подожду здесь.")
                    if Second and Second.Loc == bg_current:
                            #if the other girl agreed to come along
                            call Set_The_Scene
                    else:
                            #if the other girl didn't agree to come along
                            show blackscreen onlayer black
                            call AllHide
                            call Display_Background
                            $ Girl.SpriteLoc = StageCenter
                            $ Girl.Layer = 100
                            call Display_Girl(Girl,0,0)

                            hide blackscreen onlayer black
                    $ Player.Traits.append("locked")
                    call Taboo_Level

                    while Girl:
                        menu:
                            "Что вы хотели бы примерить?"
                            "Лифчик бикини (locked)" if Girl.Chest == "bikini top":
                                            pass
                            "Лифчик бикини" if Girl.Chest != "bikini top" and Girl is not BetsyX:
                                            if Girl.SeenChest or ApprovalCheck(Girl, 1100, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                call Dressing_Strip_Bra("bikini top")
                                            else:
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                if Girl is JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                $ Girl.Over = 0
                                                $ Girl.Chest = "bikini top"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black
                                            if "bikini top" in Cart:
                                                pass
                                            elif "bikini top" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобный.")
                                            else:
                                                $ Cart.append("bikini top")
                                                if Girl is StormX and Girl.Chest == "bikini top" and Girl.Panties == "bikini bottoms":
                                                        ch_s "Ох! Теперь я понимаю в чем смысл лоскутов!"
                            #End bikini top


                            "Трусики Бикини (locked)" if Girl.Panties == "bikini bottoms":
                                            pass
                            "Трусики Бикини" if Girl.Panties != "bikini bottoms" and Girl is not BetsyX:
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                call Dressing_Strip_Panties("bikini bottoms")
                                            else:
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Legs = 0
                                                $ Girl.Hose = 0
                                                $ Girl.Panties = "bikini bottoms"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black
                                            if "bikini bottoms" in Cart:
                                                pass
                                            elif "bikini bottoms" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобные.")
                                            else:
                                                $ Cart.append("bikini bottoms")
                                                if Girl is StormX and Girl.Chest == "bikini top" and Girl.Panties == "bikini bottoms":
                                                        ch_s "Ох! Теперь я понимаю в чем смысл лоскутов!"
                            #End bikini bottoms


                            "Синюю Юбку (locked)" if Girl is KittyX and Girl.Legs == "blue skirt":
                                            pass
                            "Синюю Юбку" if Girl is KittyX and Girl.Legs != "blue skirt":
                                            $ Girl.FaceChange("smile")
                                            if (Girl.Panties and ApprovalCheck(Girl, 900, TabM=2)) or ApprovalCheck(Girl, 1200, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                call AnyLine(Girl,"Конечно. . .")
                                                $ Girl.Upskirt = 1
                                                pause 0.3
                                                $ Girl.Legs = 0
                                                call Girl_First_Bottomless(Girl)
                                                pause 0.3
                                                $ Girl.Legs = "blue skirt"
                                                $ Girl.Upskirt = 0
                                            else:
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Legs = "blue skirt"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black
                                            if "blue skirt" in Cart:
                                                pass
                                            elif "blue skirt" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобная.")
                                            else:
                                                $ Cart.append("blue skirt")

                            "Купальник (locked)" if (Girl.Chest == "swimsuit" or Girl.Panties == "swimsuit") and Girl is BetsyX:
                                            pass
                            "Купальник" if (Girl.Chest != "swimsuit" or Girl.Panties != "swimsuit") and Girl is BetsyX:
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                call Dressing_Strip_Both("swimsuit","swimsuit")
                                            else:
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Over = 0
                                                $ Girl.Chest = "swimsuit"
                                                $ Girl.Panties = "swimsuit"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black
                                            if "swimsuit" in Cart:
                                                pass
                                            elif "swimsuit" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобный.")
                                            else:
                                                $ Cart.append("swimsuit")

                            "Немного пошалить.":
                                    #ask for sex stuff
                                    if Girl.Love >= Girl.Obed:
                                            ch_p "Хочешь пошалить?"
                                    else:
                                            ch_p "Я хочу пошалить."

                                    if not Player.Male and "girltalk" not in Girl.History:
                                            call expression Girl.Tag + "_Girltalk" #call Rogue_Girltalk
                                    if not "girltalk" not in Girl.History:
                                            pass #if you cleared it on the first pass, then this will skip, otherwise, it locks out sexy mode

                                    elif "angry" in Girl.RecentActions:
                                            if Girl is RogueX:
                                                    ch_r "Я не хочу сейчас иметь с тобой дел."
                                            elif Girl is KittyX:
                                                    ch_k "Даже не думай!"
                                            elif Girl is EmmaX:
                                                    ch_e "Думаю, ты знаешь мой ответ."
                                            elif Girl is LauraX:
                                                    ch_l "Плохая идея."
                                            elif Girl is JeanX:
                                                    ch_j "-Совсем- не интересно."
                                            elif Girl is StormX:
                                                    ch_s "Мне неинтересно."
                                            elif Girl is JubesX:
                                                    ch_v "Я не в настроении, [Girl.Petname]."
                                            elif Girl is GwenX:
                                                    ch_g "Это маловероятно. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Не понимаю, чего ты от меня ждешь. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Я сейчас немного зла на тебя. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Не сейчас."
                                    elif ApprovalCheck(Girl, 600, "LI"):
                                            $ Girl.FaceChange("sexy")
                                            if Girl is RogueX:
                                                    ch_r "Хех, хорошо, [Girl.Petname]."
                                            elif Girl is KittyX:
                                                    ch_k "Мммм, хорошо, [Girl.Petname]."
                                            elif Girl is EmmaX:
                                                    ch_e "Возможно, я и не против"
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
                                                    ch_b "Ох?"
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. Да?"
                                            elif Girl is WandaX:
                                                    ch_w "Конечно."
                                            call SexMenu # call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu
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
                                                    ch_j "Как скажешь. . ."
                                            elif Girl is StormX:
                                                    ch_s "Ладно."
                                            elif Girl is JubesX:
                                                    if not Player.Male:
                                                        ch_v "Что ты хотела бы, [Girl.Petname]?"
                                                    else:
                                                        ch_v "Что ты хотел бы, [Girl.Petname]?"
                                            elif Girl is GwenX:
                                                    ch_g "Что у тебя на уме? . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Да?"
                                            elif Girl is DoreenX:
                                                    ch_d "Ладно."
                                            elif Girl is WandaX:
                                                    ch_w "Конечно."
                                            call SexMenu # call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu
                                    else:
                                            if Girl is RogueX:
                                                    ch_r "Мне это не особо интересно, [Girl.Petname]."
                                            elif Girl is KittyX:
                                                    ch_k "Нет, спасибо, [Girl.Petname]."
                                            elif Girl is EmmaX:
                                                    ch_e "Нет, благодарю, [Girl.Petname]."
                                            elif Girl is LauraX:
                                                    ch_l "Нет, спасибо, [Girl.Petname]."
                                            elif Girl is JeanX:
                                                    ch_j "Не интересует."
                                            elif Girl is StormX:
                                                    ch_s "Мне неинтересно."
                                            elif Girl is JubesX:
                                                    ch_v "Не, я таким не увлекаюсь."
                                            elif Girl is GwenX:
                                                    ch_g "Не-а. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Я не в настроении, [Girl.Petname]. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох, эм. . . нет. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Хех, нет."
                                    #End fool around
                                    if Second and Second.Loc != bg_current:
                                            #if you scared the partner off somehow. . .
                                            $ Second = 0
                                    if First and First.Loc != bg_current:
                                            #if you scared the primary off somehow. . .
                                            $ First = 0
                                            if Second:
                                                    $ First = Second
                                    if Girl.Loc != bg_current:
                                            #if you scared the girl off somehow. . .
                                            $ Round -= 20 if Round > 30 else (Round-10) #reduces Round to at minimum 10
                                            $ Player.DrainWord("locked",0,0,1)
                                            $ bg_current = "bg shop"
                                            python:
                                                for BX in Party:
                                                    BX.Loc = "bg shop"

                                            call Taboo_Level
                                            call Set_The_Scene
                                            "Вы возвращаетесь в магазин."
                                            $ Cart = []

                            "Покинуть Примерочную.":
                                    if Cart and Second:
                                        if Second.Loc == bg_current and Second not in (LauraX,JeanX) and Second.GirlLikeCheck(Girl) >= 500:
                                            $ Second.FaceChange("smile")
                                            if Second is RogueX:
                                                    ch_r "Хорошо смотрится на тебе. . ."
                                            elif Second is KittyX:
                                                    ch_k "Ох, тебе очень идет!"
                                            elif Second is EmmaX:
                                                    ch_e "Тебе прямо идет. . ."
                                            elif Second is StormX:
                                                    ch_s "Тебе очень идет. . ."
                                            elif Second is JubesX:
                                                    ch_v "Ты выглядишь такой милой!"
                                            elif Second is GwenX:
                                                    ch_g "Ты выглядишь великолепно!"
                                            elif Second is BetsyX:
                                                    ch_b "Ох, ты хорошо выглядишь. . ."
                                            elif Second is DoreenX:
                                                    ch_d "Ты отлично смотришься в этом!"
                                            elif Second is WandaX:
                                                    ch_w "Вау, ты выглядишь супер сексуально, [Girl.Name]."

                                            $ Girl.FaceChange("smile")
                                            if Girl is RogueX:
                                                    ch_r "Ах, спасибо. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Правда?"
                                            elif Girl is EmmaX:
                                                    ch_e "Разумеется. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Ладно, клево. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Ну еще бы. . ."
                                            elif Girl is StormX:
                                                    ch_s "Ох, благодарю. . ."
                                            elif Girl is JubesX:
                                                    ch_v "Я знаю, хорошо?"
                                            elif Girl is GwenX:
                                                    ch_g "Правда? Мне нравится."
                                            elif Girl is BetsyX:
                                                    ch_b "Как любезно с твоей стороны. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Оу. . . правда?"
                                            elif Girl is WandaX:
                                                    ch_w "Ты так думаешь?"
                                            $ Girl.GirlLikeUp(Second,5)
                                            $ Second.GirlLikeUp(Girl,3)


                                    $ Girl.OutfitChange(Changed=0) #puts clothes back on
                                    $ Round -= 20 if Round > 30 else (Round-10) #reduces Round to at minimum 10
                                    $ Player.DrainWord("locked",0,0,1)
                                    $ bg_current = "bg shop"
                                    python:
                                        for BX in Party:
                                            BX.Loc = "bg shop"

                                    call Taboo_Level
                                    call Set_The_Scene
                                    if not Cart:
                                            "Это было весело, но так как ее ничего не заинтересовало, она возвращает все обратно."
                                    if Player.Cash < 50:
                                        "У вас недостаточно средств, поэтому вам приходится вернуть все обратно."
                                        $ Girl.FaceChange("sad")
                                        if "shopblock" not in Girl.DailyActions:
                                                $ Girl.Statup("Love", 50, -2)
                                                $ Girl.Statup("Love", 90, -2)
                                                $ Girl.Statup("Obed", 50, 3)
                                                $ Girl.Statup("Obed", 80, 3)
                                                $ Girl.AddWord(1,"shopblock","shopblock") #recent and daily
                                        if Girl in (EmmaX,StormX):
                                                call AnyLine(Girl,"Какое разочарование.")
                                        elif Girl in (JeanX,LauraX):
                                                pass
                                        else:
                                                call AnyLine(Girl,"Оу. . .")
                                        $ Cart = []

                                    while Cart:
                                        menu:
                                            "Что вы хотели бы купить?"
                                            "Лифчик" if "bikini top" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] лифчик бикини."
                                                    if Girl.Tag + " bikini top" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такой."
                                                            "Вы достаете тот, что у вас в рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " bikini top")
                                                    elif Girl in (KittyX,EmmaX,StormX):
                                                        if Player.Cash < 60:
                                                            "Вы смотрите на ценник, $60, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("bikini top")
                                                        else:
                                                            $ Player.Cash -= 60
                                                    elif Player.Cash < 50:
                                                            "Вы смотрите на ценник, $50, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("bikini top")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "bikini top" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("bikini top")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("bikini top")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 20)
                                                            $ Girl.Statup("Obed", 200, 10)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            if Girl is RogueX:
                                                                    ch_r "Немного откровенный. . ."
                                                            elif Girl is KittyX:
                                                                    ch_k "Ах, милая Китти. . ."
                                                            elif Girl is EmmaX:
                                                                    ch_e "Подчеркивает мои прелести, верно. . .?"
                                                            elif Girl is LauraX:
                                                                    ch_l "\"Икс\", мило. . ."
                                                            elif Girl is JeanX:
                                                                    ch_j "Да, подойдет. . ."
                                                            elif Girl is StormX:
                                                                    ch_s "Думаю, я узнаю дизайн. . ."
                                                            elif Girl is JubesX:
                                                                    ch_v "Ооо, круто. . ."
                                                            elif Girl is GwenX:
                                                                    ch_g "Почему они в таком стиле?"
                                                            elif Girl is DoreenX:
                                                                    ch_d "Думаю, он очень милый!"
                                                            elif Girl is WandaX:
                                                                    ch_w "Он довольно симпатичный."
                                            #end buy bikini top

                                            "Трусики" if "bikini bottoms" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] трусики бикини."
                                                    if Girl.Tag + " bikini bottoms" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такие."
                                                            "Вы вытаскиваете трусики из своего рюкзака."
                                                            $ Player.Inventory.remove(Girl.Tag + " bikini bottoms")
                                                    elif Girl in (KittyX,EmmaX,StormX):
                                                        if Player.Cash < 60:
                                                            "Вы смотрите на ценник, $60, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("bikini bottoms")
                                                        else:
                                                            $ Player.Cash -= 60
                                                    elif Player.Cash < 50:
                                                            "Вы смотрите на ценник, $50, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("bikini bottoms")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "bikini bottoms" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("bikini bottoms")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("bikini bottoms")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 20)
                                                            $ Girl.Statup("Obed", 200, 10)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            if Girl is RogueX:
                                                                    ch_r "Я как раз думала о загаре. . ."
                                                            elif Girl is KittyX:
                                                                    ch_k "Слегка обтягивающие. . ."
                                                            elif Girl is EmmaX:
                                                                    if not Player.Male:
                                                                        ch_e "Я не уверена, должна ли студентка покупать мне купальники. . ."
                                                                    else:
                                                                        ch_e "Я не уверена, должен ли студент покупать мне купальники. . ."
                                                            elif Girl is LauraX:
                                                                    ch_l "Ладно, клево. . ."
                                                            elif Girl is JeanX:
                                                                    ch_j "Ооо, они милые. . ."
                                                            elif Girl is StormX:
                                                                    ch_s "Где-то я видела такой вырез раньше. . ."
                                                            elif Girl is JubesX:
                                                                    ch_v "Мне кажется, они немного маленькие. . ."
                                                            elif Girl is GwenX:
                                                                    ch_g "Он не прикрывают так, как мой старые, но. . ."
                                                            elif Girl is DoreenX:
                                                                    ch_d "Они очень милые!"
                                                            elif Girl is WandaX:
                                                                    ch_w "Они очень милые."
                                            #end buy bikini bottoms

                                            "Купальник" if "swimsuit" in Cart:
                                                    "Вы соглашаетесь [Girl.Name_dat] купальник."
                                                    if Girl.Tag + " swimsuit" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такой."
                                                            "Вы достаете тот, что у вас в рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " swimsuit")
                                                    elif Player.Cash < 110:
                                                            "Вы смотрите на ценник, $110, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("swimsuit")
                                                    else:
                                                            $ Player.Cash -= 110
                                                    if "swimsuit" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("swimsuit")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("swimsuit")
                                                            $ Girl.Swim[0] = 1
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 30)
                                                            $ Girl.Statup("Obed", 200, 15)
                                                            $ Girl.Statup("Inbt", 200, 15)
                                                            if Girl is BetsyX:
                                                                    ch_b "Хм, мне кажется, он мне в самый раз. . ."
                                            #end buy swimsuit

                                            "Юбку" if "blue skirt" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] синюю юбку."
                                                    if Girl.Tag + " blue skirt" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такая."
                                                            "Вы достаете ту, что у вас в рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " blue skirt")
                                                    if Player.Cash < 50:
                                                            "Вы смотрите на ценник, $50, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("blue skirt")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "blue skirt" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("blue skirt")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("blue skirt")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 20)
                                                            $ Girl.Statup("Obed", 200, 10)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            ch_k "Какая милая юбочка. . ."
                                            #end buy blue skirt

                                            "Ничего" if "purchased" not in Player.RecentActions:
                                                    $ Girl.FaceChange("sad")
                                                    if "shopblock" not in Girl.DailyActions:
                                                            $ Girl.Statup("Love", 50, -2)
                                                            $ Girl.Statup("Love", 90, -2)
                                                            $ Girl.Statup("Obed", 50, 3)
                                                            $ Girl.Statup("Obed", 80, 3)
                                                            $ Girl.AddWord(1,"shopblock","shopblock") #recent and daily
                                                    "Вы все возвращаете."
                                                    if Girl in (EmmaX,StormX):
                                                            call AnyLine(Girl,"Какое разочарование.")
                                                    elif Girl in (JeanX,LauraX):
                                                            pass
                                                    else:
                                                            call AnyLine(Girl,"Оу. . .")
                                                    $ Cart = []
                                            "Больше ничего" if "purchased" in Player.RecentActions:
                                                    $ Girl.FaceChange("sad")
                                                    if "shopblock" not in Girl.DailyActions:
                                                            $ Girl.Statup("Love", 50, -1)
                                                            $ Girl.Statup("Obed", 50, 3)
                                                            $ Girl.Statup("Obed", 90, 2)
                                                    "Вы возвращаете все оставшееся."
                                                    $ Cart = []
                                    #End while Cart: loop


                                    $ Player.DrainWord("purchased") #removes purchased token
                                    if Girl is KittyX:
                                        if ("blue skirt" in Girl.Inventory or Girl.Inbt >= 400) and "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                                $ Girl.Swim[0] = 1
                                    elif "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                                $ Girl.Swim[0] = 1
                                    $ Girl = 0
                    #end Dressing room loop"

                # End Swimwear while loop
        return

#End Swim Shop   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Lingerie_Shop: #rkeljsvgb
        #this one will loop the "try something on menu" until you leave,
        #if you pick a girl, it sees if she's willing to try stuff on.
        #if she is, it loops the "dressing room" area until you try to leave
        #then it loops the "empty cart" menu until it's empty.

        # Modification mode
        if is_playing_music(audio.mall_location):
            $ play_music(name=audio.mall_location)
        # -----------------

        $ bg_current = "bg shop"
        python:
            for BX in Party:
                BX.Loc = "bg shop"

        call Set_The_Scene
        $ Girl = 0
        "Вы направляетесь в \"Стейси\". . ."
        while True:
                if Round <= 20:
                    "Уже поздно, вы возвращаетесь в торговый центр. . ."
                    $ Girl = 0
                    return
                menu:
                    "Что вы хотели бы?"
                    "Пусть [First.Name] что-нибудь примерит." if First:
                            $ Girl = First
                    "Пусть [Second.Name] что-нибудь примерит." if Second:
                            #swaps first and second
                            $ Girl = Second
                            $ Second = First
                            $ First = Girl
                    "Купить что-нибудь на потом" if not First:
                            call Lingerie_Shop_Menu
                    "Выход.":
                            "Вы возвращаетесь в торговый центр. . ."
                            $ Girl = 0
                            $ bg_current = "bg mall"
                            python:
                                for BX in Party:
                                    BX.Loc = "bg mall"
                            call Set_The_Scene
                            return
                #End shop menu

                if Girl:
                        #checks if they are ok with shopping for lingerie with you, kicks out if not
                        $ Girl.FaceChange("smile",1)
                        if ApprovalCheck(Girl, 800) or ApprovalCheck(Girl, 600, "L") or ApprovalCheck(Girl, 300, "O"):
                            #if she agrees. . .
                            if Girl is RogueX:
                                    ch_r "Ох, как пикантно. . ."
                            elif Girl is KittyX:
                                    ch_k "Эм, я не уверена. . ."
                            elif Girl is EmmaX:
                                    ch_e "Я не уверена, к чему все идет. . ."
                            elif Girl is LauraX:
                                    ch_l "Ох?"
                            elif Girl is JeanX:
                                    ch_j "Ох, к чему ты клонишь?"
                            elif Girl is StormX:
                                    ch_s "Я понимаю, к чему ты клонишь. . ."
                            elif Girl is JubesX:
                                    ch_v "Так, интересный ход. . ."
                            elif Girl is GwenX:
                                    ch_g "Думаю, я все еще могу подобрать себе несколько вещей. . ."
                            elif Girl is BetsyX:
                                    ch_b "Это довольно -смелый- бутик. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ох, эм. . . это место немного. . . подозрительное. . ."
                            elif Girl is WandaX:
                                    ch_w "Оооох, что мы здесь ищем?"
                        elif not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History:
                            #if you're a girl and she hasn't clocked you
                            if Girl is RogueX:
                                    ch_r "О, это может быть весело. . ."
                            elif Girl is KittyX:
                                    ch_k "Эм, я даже не знаю. . ."
                            elif Girl is EmmaX:
                                    ch_e "Я не уверена, к чему все идет. . ."
                            elif Girl is LauraX:
                                    ch_l "Ох?"
                            elif Girl is JeanX:
                                    ch_j "Ох, ты чего-то от меня хочешь?"
                            elif Girl is StormX:
                                    ch_s "Посмотрим, к чему все идет. . ."
                            elif Girl is JubesX:
                                    if not Player.Male:
                                        ch_v "Ладно, интересную игру ты затеяла. . ."
                                    else:
                                        ch_v "Ладно, интересную игру ты затеял. . ."
                            elif Girl is GwenX:
                                    ch_g "Ох, о чем ты только думаешь?"
                            elif Girl is BetsyX:
                                    ch_b "Это довольно милый маленький бутик. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ох, эм. . . ты хочешь купить какое-то нижнее белье? . ."
                            elif Girl is WandaX:
                                    ch_w "Мы пришли за нижним бельем? Замечательно. . ."
                        else:
                            if Girl is RogueX:
                                    ch_r "Ох, нет, спасибо."
                            elif Girl is KittyX:
                                    ch_k "Ох, эм, мне ничего не нужно отсюда. . ."
                            elif Girl is EmmaX:
                                    ch_e "Думаю, это слегка неуместно.. . ."
                            elif Girl is LauraX:
                                    ch_l "Не интересует. . ."
                            elif Girl is JeanX:
                                    ch_j "Нет, не нужно."
                            elif Girl is StormX:
                                    ch_s "Не думаю, что мне следует. . ."
                            elif Girl is JubesX:
                                    ch_v "Я не очень хочу покупать это. . ."
                            elif Girl is GwenX:
                                    ch_g "Я зайду сюда в свободное время."
                                    ch_g "И, может быть. . . что-нибудь прикуплю. . ."
                            elif Girl is BetsyX:
                                    ch_b "Возможно, я зайду сюда за покупками чуть позже. . ."
                            elif Girl is DoreenX:
                                    ch_d "Ох, эм. . . нет. . ."
                            elif Girl is WandaX:
                                    ch_w "Хех, может, в другой раз, [Girl.Petname]."
                            $ Girl = 0
                #end checks if they are ok with shopping for bikinis with you, kicks out if not

                if Girl:
                    #if she agreed to shop for a suit. . .
                    call Shift_Focus(Girl)
                    "Вы берете вещи и направляетесь в одну из раздевалок с [Girl.Name_tvo]."
                    $ bg_current = "bg dressing"
                    $ Girl.Loc = "bg dressing"
                    if Second:
                        #if there is a second girl
                        "Стоит ли [Second.Name_dat] к вам присоединиться?"
                        menu:
                            "Конечно":
                                    "[Second.Name] следует за вами."
                                    $ Second.Loc = "bg dressing"
                            "Это вряд ли.":
                                    ch_p "[Second.Name], тебе, пожалуй, стоит остаться."
                                    call AnyLine(Second,"Ладно. Я подожду здесь.")
                    if Second and Second.Loc == bg_current:
                            #if the other girl agreed to come along
                            call Set_The_Scene
                    else:
                            #if the other girl didn't agree to come along
                            show blackscreen onlayer black
                            call AllHide
                            call Display_Background
                            $ Girl.SpriteLoc = StageCenter
                            $ Girl.Layer = 100
                            call Display_Girl(Girl,0,0)

                            hide blackscreen onlayer black
                    $ Player.Traits.append("locked")
                    call Taboo_Level

                    while Girl:
                        menu:
                            "Что вы хотели бы примерить?"
                            "Кружевной Лифчик (locked)" if Girl.Chest == "lace bra":
                                            pass
                            "Кружевной Лифчик" if Girl.Chest != "lace bra" and Girl != LauraX:
                                    if "no gift bra" in Girl.RecentActions:
                                                call AnyLine(Girl,"Я сказала \"нет\". . .")
                                    elif not Girl.SeenChest and not ApprovalCheck(Girl, 900) and Player.Male:
                                                #if she refuses to even try that on because she isn't willing to let you see her in it
                                                $ Girl.FaceChange("angry",2)
                                                if Girl in (EmmaX,StormX,BetsyX):
                                                        call AnyLine(Girl,"Не думаю, что это будет уместно.")
                                                elif Girl in (JeanX,LauraX):
                                                        call AnyLine(Girl,"Нет, спасибо. . .")
                                                else:
                                                        call AnyLine(Girl,"Эм, нет, однозначно нет. . .")
                                                $ Girl.FaceChange("angry",1)
                                                $ Girl.RecentActions.append("no gift bra")
                                    else:
                                            if Girl.SeenChest or ApprovalCheck(Girl, 1000, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                #she is willing to change into it in front of you
                                                call Dressing_Strip_Bra("lace bra")
                                            else:
                                                #she is willing to wear it, but not change into it in front of you
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                if Girl is JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                $ Girl.Over = 0
                                                $ Girl.Chest = "lace bra"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black

                                            if "lace bra" in Cart:
                                                pass
                                            elif "lace bra" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобный.")
                                            else:
                                                $ Cart.append("lace bra")
                                    #End lace bra

                            "Корсет (locked)" if Girl.Chest == "corset":
                                                pass
                            "Корсет" if Girl.Chest != "corset" and Girl in (LauraX,JeanX):
                                    if "no gift bra" in Girl.RecentActions:
                                                call AnyLine(Girl,"Я сказала \"нет\". . .")
                                    elif not Girl.SeenChest and not ApprovalCheck(Girl, 900) and Player.Male:
                                                #if she refuses to even try that on because she isn't willing to let you see her in it
                                                $ Girl.FaceChange("angry",2)
                                                if Girl in (EmmaX,StormX):
                                                        call AnyLine(Girl,"Не думаю, что это будет уместно.")
                                                elif Girl in (JeanX,LauraX):
                                                        call AnyLine(Girl,"Нет, спасибо. . .")
                                                else:
                                                        call AnyLine(Girl,"Эм, нет, однозначно нет. . .")
                                                $ Girl.FaceChange("angry",1)
                                                $ Girl.RecentActions.append("no gift bra")
                                    else:
                                            if Girl.SeenChest or ApprovalCheck(Girl, 1000, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                #she is willing to change into it in front of you
                                                call Dressing_Strip_Bra("corset")
                                            else:
                                                #she is willing to wear it, but not change into it in front of you
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                if Girl is JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                $ Girl.Over = 0
                                                $ Girl.Chest = "corset"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black

                                            if "corset" in Cart:
                                                pass
                                            elif "corset" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобный.")
                                            else:
                                                $ Cart.append("corset")
                                    #End corset

                            "Кружевной Корсет (locked)" if Girl.Chest == "lace corset":
                                            pass
                            "Кружевной Корсет" if Girl.Chest != "lace corset" and Girl is LauraX:
                                    if "no gift bra" in Girl.RecentActions:
                                                call AnyLine(Girl,"Я сказала \"нет\". . .")
                                    elif not Girl.SeenChest and not ApprovalCheck(Girl, 900) and Player.Male:
                                                #if she refuses to even try that on because she isn't willing to let you see her in it
                                                $ Girl.FaceChange("angry",2)
                                                if Girl in (EmmaX,StormX):
                                                        call AnyLine(Girl,"Не думаю, что это будет уместно.")
                                                elif Girl in (JeanX,LauraX):
                                                        call AnyLine(Girl,"Нет, спасибо. . .")
                                                else:
                                                        call AnyLine(Girl,"Эм, нет, однозначно нет. . .")
                                                $ Girl.FaceChange("angry",1)
                                                $ Girl.RecentActions.append("no gift bra")
                                    else:
                                            if Girl.SeenChest or ApprovalCheck(Girl, 1000, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                #she is willing to change into it in front of you
                                                call Dressing_Strip_Bra("lace corset")
                                            else:
                                                #she is willing to wear it, but not change into it in front of you
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                if Girl is JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                $ Girl.Over = 0
                                                $ Girl.Chest = "lace corset"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black

                                            if "lace corset" in Cart:
                                                pass
                                            elif "lace corset" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобный.")
                                            else:
                                                $ Cart.append("lace corset")
                                    #End lace corset

                            "Кружевные Трусики (locked)" if Girl.Panties == "lace panties":
                                            pass
                            "Кружевные Трусики" if Girl.Panties != "lace panties":
                                    if "no gift panties" in Girl.RecentActions:
                                                call AnyLine(Girl,"Я сказала \"нет\". . .")
                                    elif not Girl.SeenPussy and not ApprovalCheck(Girl, 1000) and Player.Male:
                                                #if she refuses to even try that on because she isn't willing to let you see her in it
                                                $ Girl.FaceChange("angry",2)
                                                if Girl in (EmmaX,StormX,BetsyX):
                                                        call AnyLine(Girl,"Не думаю, что это будет уместно.")
                                                elif Girl in (JeanX,LauraX):
                                                        call AnyLine(Girl,"Нет, спасибо. . .")
                                                else:
                                                        call AnyLine(Girl,"Эм, нет, однозначно нет. . .")
                                                $ Girl.FaceChange("angry",1)
                                                $ Girl.RecentActions.append("no gift panties")
                                    else:
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                #she is willing to change into it in front of you
                                                call Dressing_Strip_Panties("lace panties")
                                            else:
                                                #she is willing to wear it, but not change into it in front of you
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Legs = 0
                                                $ Girl.Hose = 0
                                                $ Girl.Panties = "lace panties"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black

                                            if "lace panties" in Cart:
                                                pass
                                            elif "lace panties" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобные.")
                                            else:
                                                $ Cart.append("lace panties")
                                    #End lace panties

                            "Сетчатые брюки (locked)" if Girl.Legs == "mesh pants":
                                            pass
                            "Ажурные брюки" if Girl.Legs != "mesh pants" and Girl is LauraX:
                                    if "no gift panties" in Girl.RecentActions:
                                                call AnyLine(Girl,"Я сказала \"нет\". . .")
                                    elif not Girl.SeenPussy and not ApprovalCheck(Girl, 1100) and Player.Male:
                                                #if she refuses to even try that on because she isn't willing to let you see her in it
                                                $ Girl.FaceChange("angry",2)
                                                call AnyLine(Girl,"Нет, спасибо. . .")
                                                $ Girl.FaceChange("angry",1)
                                                $ Girl.RecentActions.append("no gift panties")
                                    else:
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 1000, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                #she is willing to change into it in front of you
                                                if Girl.Legs:
                                                        $ Girl.Upskirt = 1
                                                        pause 0.3
                                                        $ Girl.Legs = 0
                                                        pause 0.3
                                                        $ Girl.Upskirt = 0
                                                $ Girl.Legs = "mesh pants"
                                            else:
                                                #she is willing to wear it, but not change into it in front of you
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Legs = "mesh pants"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black

                                            if "mesh pants" in Cart:
                                                pass
                                            elif "mesh pants" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобные.")
                                            else:
                                                $ Cart.append("mesh pants")
                                    #End mesh pants

                            "Трусики в тигровую полоску (locked)" if Girl.Panties == "tiger panties":
                                            pass
                            "Трусики в тигровую полоску" if Girl.Panties != "tiger panties" and Girl is JubesX:
                                    if "no gift panties" in Girl.RecentActions:
                                                call AnyLine(Girl,"Я сказала \"нет\". . .")
                                    elif not Girl.SeenPussy and not ApprovalCheck(Girl, 1000) and Player.Male:
                                                #if she refuses to even try that on because she isn't willing to let you see her in it
                                                $ Girl.FaceChange("angry",2)
                                                call AnyLine(Girl,"Эм, нет, мне это совсем не интересно. . .")
                                                $ Girl.FaceChange("angry",1)
                                                $ Girl.RecentActions.append("no gift panties")
                                    else:
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                #she is willing to change into it in front of you
                                                call Dressing_Strip_Panties("tiger panties")
                                            else:
                                                #she is willing to wear it, but not change into it in front of you
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Legs = 0
                                                $ Girl.Hose = 0
                                                $ Girl.Panties = "tiger panties"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black

                                            if "tiger panties" in Cart:
                                                pass
                                            elif "tiger panties" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобные.")
                                            else:
                                                $ Cart.append("tiger panties")
                                    #End tiger panties

                            "Чулки и Пояс с Подвязками (locked)" if Girl.Hose == "stockings and garterbelt":
                                            pass
                            "Чулки и Пояс с Подвязками" if Girl.Hose != "stockings and garterbelt":
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 900, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                #she is willing to change into it in front of you
                                                $ Girl.FaceChange("sexy")
                                                call AnyLine(Girl,"Конечно. . .")
                                                $ Girl.Upskirt = 1
                                                pause 0.3
                                                $ Girl.Legs = 0
                                                pause 0.3
                                                $ Girl.Hose = 0
                                                call Girl_First_Bottomless(Girl)
                                                pause 0.3
                                                $ Girl.Hose = "stockings and garterbelt"
                                                $ Girl.PantiesDown = 0
                                                $ Girl.Upskirt = 0
                                                if Second and Second.Loc == bg_current and "stockings and garterbelt" not in Cart:
                                                    $ Girl.GirlLikeUp(Second,1)
                                                    $ Second.GirlLikeUp(Girl,2)
                                            else:
                                                #she is willing to wear it, but not change into it in front of you
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Hose = "stockings and garterbelt"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black

                                            if "stockings and garterbelt" in Cart:
                                                pass
                                            elif "stockings and garterbelt" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобные.")
                                            else:
                                                $ Cart.append("stockings and garterbelt")
                                    #End Stockings and Garterbelt

                            "Гольфы (locked)" if Girl.Hose == "knee stockings":
                                            pass
                            "Гольфы" if Girl.Hose != "knee stockings" and Girl is KittyX:
                                            $ Girl.FaceChange("sexy")
                                            call AnyLine(Girl,"Конечно. . .")
                                            $ Girl.Hose = 0
                                            pause 0.3
                                            $ Girl.Hose = "knee stockings"

                                            if "knee stockings" in Cart:
                                                pass
                                            elif "knee stockings" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобные.")
                                            else:
                                                $ Cart.append("knee stockings")
                                    #End Knee Stockings

                            "Высокие Носки (locked)" if Girl.Hose == "socks":
                                            pass
                            "Высокие Носки" if Girl.Hose != "socks" and Girl is JubesX:
                                            $ Girl.FaceChange("sexy")
                                            call AnyLine(Girl,"Конечно. . .")
                                            $ Girl.Hose = 0
                                            pause 0.3
                                            $ Girl.Hose = "socks"

                                            if "socks" in Cart:
                                                pass
                                            elif "socks" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобные.")
                                            else:
                                                $ Cart.append("socks")
                                    #End Knee Stockings

                            "Колготки (locked)" if Girl.Hose == "pantyhose":
                                            pass
                            "Колготки" if Girl.Hose != "pantyhose":
                                            if Girl.SeenPussy or ApprovalCheck(Girl, 900, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                #she is willing to change into it in front of you
                                                $ Girl.FaceChange("sexy")
                                                call AnyLine(Girl,"Конечно. . .")
                                                $ Girl.Upskirt = 1
                                                pause 0.3
                                                $ Girl.Legs = 0
                                                pause 0.3
                                                $ Girl.Hose = 0
                                                call Girl_First_Bottomless(Girl)
                                                pause 0.3
                                                $ Girl.Hose = "pantyhose"
                                                $ Girl.PantiesDown = 0
                                                $ Girl.Upskirt = 0
                                                if Second and Second.Loc == bg_current and "pantyhose" not in Cart:
                                                    $ Girl.GirlLikeUp(Second,1)
                                                    $ Second.GirlLikeUp(Girl,2)
                                            else:
                                                #she is willing to wear it, but not change into it in front of you
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                $ Girl.Hose = "pantyhose"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black

                                            if "pantyhose" in Cart:
                                                pass
                                            elif "pantyhose" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобные.")
                                            else:
                                                $ Cart.append("pantyhose")
                                    #End Pantyhose

                            "Сними [get_clothing_name(Girl.Hose_key, vin)]" if Girl.Hose:
                                            if Girl.HoseNum() < 10 or ApprovalCheck(Girl, 900, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                #she is willing to change into it in front of you
                                                if Girl in (EmmaX,StormX,BetsyX):
                                                        call AnyLine(Girl,"Полагаю, это можно. . .")
                                                else:
                                                        call AnyLine(Girl,"Ладно. . .")
                                                $ Girl.Hose = 0
                                                call Girl_First_Bottomless(Girl)
                                            else:
                                                if Girl in (EmmaX,StormX):
                                                        call AnyLine(Girl,"Я не думаю, что это разумно. . .")
                                                else:
                                                        call AnyLine(Girl,"Нет, спасибо. . .")

                            "Ночнушку (locked)" if Girl.Over == "nighty":
                                            pass
                            "Ночнушку" if Girl.Over != "nighty" and Girl is RogueX:
                                    if "no gift bra" in Girl.RecentActions:
                                            call AnyLine(Girl,"Я сказала \"нет\". . .")
                                    elif not Girl.SeenChest and not ApprovalCheck(Girl, 900) and Player.Male:
                                            #if she refuses to even try that on because she isn't willing to let you see her in it
                                            $ Girl.FaceChange("angry",2)
                                            if Girl in (EmmaX,StormX):
                                                    call AnyLine(Girl,"Не думаю, что это будет уместно.")
                                            elif Girl in (JeanX,LauraX):
                                                    call AnyLine(Girl,"Нет, спасибо. . .")
                                            else:
                                                    call AnyLine(Girl,"Эм, нет, однозначно нет. . .")
                                            $ Girl.FaceChange("angry",1)
                                            $ Girl.RecentActions.append("no gift bra")
                                    else:
                                            if Girl.SeenChest or ApprovalCheck(Girl, 900, TabM=2) or (not Player.Male and "girltalk" not in Girl.History and "nogirls" not in Girl.History):
                                                #she is willing to change into it in front of you
                                                $ Girl.FaceChange("sexy")
                                                call AnyLine(Girl,"Конечно. . .")
                                                if Girl is JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                        pause 0.3
                                                $ Girl.Over = 0
                                                call Girl_First_Topless(Girl)
                                                call Girl_First_Bottomless(Girl,1)
                                                pause 0.3
                                                $ Girl.Over = "nighty"
                                                pause 0.3
                                                $ Girl.Uptop = 0
                                                if Second and "nighty" not in Cart:
                                                    $ Girl.GirlLikeUp(Second,1)
                                                    $ Second.GirlLikeUp(Girl,3)
                                            else:
                                                #she is willing to wear it, but not change into it in front of you
                                                call AnyLine(Girl,"Оставь меня одну ненадолго. . .")
                                                show blackscreen onlayer black
                                                if Girl is JubesX: #removes coat
                                                        $ Girl.Acc = 0
                                                $ Girl.Over = "nighty"
                                                "Вы ненадолго выходите из комнаты. . ."
                                                hide blackscreen onlayer black
                                            if "nighty" in Cart:
                                                pass
                                            elif "nighty" in Girl.Inventory:
                                                call AnyLine(Girl,"Думаю, у меня уже есть подобная.")
                                            else:
                                                $ Cart.append("nighty")
                                    #End nighty

                            "Немного пошалить.":
                                    #ask for sex stuff
                                    if Girl.Love >= Girl.Obed:
                                            ch_p "Хочешь пошалить?"
                                    else:
                                            ch_p "Я хочу пошалить."

                                    if not Player.Male and "girltalk" not in Girl.History:
                                            call expression Girl.Tag + "_Girltalk" #call Rogue_Girltalk
                                    if not Player.Male and "girltalk" not in Girl.History:
                                            pass #if you cleared it on the first pass, then this will skip, otherwise, it locks out sexy mode

                                    elif "angry" in Girl.RecentActions:
                                            if Girl is RogueX:
                                                    ch_r "Я не хочу сейчас иметь с тобой дел."
                                            elif Girl is KittyX:
                                                    ch_k "Даже не думай!"
                                            elif Girl is EmmaX:
                                                    ch_e "Думаю, ты знаешь мой ответ."
                                            elif Girl is LauraX:
                                                    ch_l "Плохая идея."
                                            elif Girl is JeanX:
                                                    ch_j "-Совсем- не интересно."
                                            elif Girl is StormX:
                                                    ch_s "Мне неинтересно."
                                            elif Girl is JubesX:
                                                    ch_v "Я не в настроении, [Girl.Petname]."
                                            elif Girl is GwenX:
                                                    ch_g "Это маловероятно. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Не понимаю, чего ты от меня ждешь. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Я сейчас немного зла на тебя. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Не сейчас."
                                    elif ApprovalCheck(Girl, 600, "LI"):
                                            $ Girl.FaceChange("sexy")
                                            if Girl is RogueX:
                                                    ch_r "Хех, хорошо, [Girl.Petname]."
                                            elif Girl is KittyX:
                                                    ch_k "Мммм, хорошо, [Girl.Petname]."
                                            elif Girl is EmmaX:
                                                    ch_e "Возможно, я и не против. . ."
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
                                                    ch_b "Ох?"
                                            elif Girl is DoreenX:
                                                    ch_d "Ох. Да?"
                                            elif Girl is WandaX:
                                                    ch_w "Конечно."
                                            call SexMenu # call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu
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
                                                    ch_j "Как скажешь. . ."
                                            elif Girl is StormX:
                                                    ch_s "Ладно."
                                            elif Girl is JubesX:
                                                    if not Player.Male:
                                                        ch_v "Что бы ты хотела, [Girl.Petname]?"
                                                    else:
                                                        ch_v "Что бы ты хотел, [Girl.Petname]?"
                                            elif Girl is GwenX:
                                                    ch_g "Что у тебя на уме? . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Да?"
                                            elif Girl is DoreenX:
                                                    ch_d "Ладно."
                                            elif Girl is WandaX:
                                                    ch_w "Конечно."
                                            call SexMenu # call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu
                                    else:
                                            if Girl is RogueX:
                                                    ch_r "Мне это не особо интересно, [Girl.Petname]."
                                            elif Girl is KittyX:
                                                    ch_k "Нет, спасибо, [Girl.Petname]."
                                            elif Girl is EmmaX:
                                                    ch_e "Нет, благодарю, [Girl.Petname]."
                                            elif Girl is LauraX:
                                                    ch_l "Нет, спасибо, [Girl.Petname]."
                                            elif Girl is JeanX:
                                                    ch_j "Не интересует."
                                            elif Girl is StormX:
                                                    ch_s "Мне неинтересно."
                                            elif Girl is JubesX:
                                                    ch_v "Не, я таким не увлекаюсь."
                                            elif Girl is GwenX:
                                                    ch_g "Неа. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Я не в настроении, [Girl.Petname]. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Ох, эм. . . нет. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Хех, нет."
                                    #End fool around
                                    if Second and Second.Loc != bg_current:
                                            #if you scared the partner off somehow. . .
                                            $ Second = 0
                                    if First and First.Loc != bg_current:
                                            #if you scared the primary off somehow. . .
                                            $ First = 0
                                            if Second:
                                                    $ First = Second
                                    if Girl.Loc != bg_current:
                                            #if you scared the girl off somehow. . .
                                            $ Round -= 20 if Round > 30 else (Round-10) #reduces Round to at minimum 10
                                            $ Player.DrainWord("locked",0,0,1)
                                            $ bg_current = "bg shop"
                                            python:
                                                for BX in Party:
                                                    BX.Loc = "bg shop"

                                            call Taboo_Level
                                            call Set_The_Scene
                                            "Вы возвращаетесь в магазин."
                                            $ Cart = []


                            "Покинуть Примерочную.":
                                    if Cart and Second:
                                        if Second.Loc == bg_current and Second not in (LauraX,JeanX) and Second.GirlLikeCheck(Girl) >= 500:
                                            $ Second.FaceChange("sexy")
                                            if Second is RogueX:
                                                    ch_r "Тебе очень идет. . ."
                                            elif Second is KittyX:
                                                    ch_k "Ох, тебе очень идет!"
                                            elif Second is EmmaX:
                                                    ch_e "Тебе прямо идет. . ."
                                            elif Second is StormX:
                                                    ch_s "Тебе очень идет. . ."
                                            elif Second is JubesX:
                                                    ch_v "Так мило!"
                                            elif Second is GwenX:
                                                    ch_g "Ты выглядишь великолепно!"
                                            elif Second is BetsyX:
                                                    ch_b "Ох, ты хорошо выглядишь. . ."
                                            elif Second is DoreenX:
                                                    ch_d "Ты выглядишь просто отлично!"
                                            elif Girl is WandaX:
                                                    ch_w "Ты сейчас такая сексуальная, [Second.Name]."

                                            $ Girl.FaceChange("sexy")
                                            if Girl is RogueX:
                                                    ch_r "Ах, спасибо. . ."
                                            elif Girl is KittyX:
                                                    ch_k "Правда?"
                                            elif Girl is EmmaX:
                                                    ch_e "Разумеется. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Ладно, клево. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Ну еще бы. . ."
                                            elif Girl is StormX:
                                                    ch_s "Ох, благодарю. . ."
                                            elif Girl is JubesX:
                                                    ch_v "Я знаю, хорошо?"
                                            elif Girl is GwenX:
                                                    ch_g "Правда? Мне нравится."
                                            elif Girl is BetsyX:
                                                    ch_b "Как любезно с твоей стороны. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Оу. . . правда?"
                                            elif Girl is WandaX:
                                                    ch_w "Ты так думаешь? Мне приятно."
                                            $ Girl.GirlLikeUp(Second,5)
                                            $ Second.GirlLikeUp(Girl,3)

                                    $ Round -= 20 if Round > 30 else (Round-10) #reduces Round to at minimum 10
                                    $ Player.DrainWord("locked",0,0,1)
                                    $ bg_current = "bg shop"
                                    python:
                                        for BX in Party:
                                            BX.Loc = "bg shop"

                                    call Taboo_Level
                                    call Set_The_Scene

                                    $ Girl.OutfitChange(Changed=0) #puts clothes back on
                                    if not Cart:
                                            "Это было весело, но так как ее ничего не заинтересовало, она возвращает все обратно."
                                    if Player.Cash < 50:
                                        "У вас недостаточно средств, поэтому вам приходится вернуть все обратно."
                                        $ Girl.FaceChange("sad")
                                        if "shopblock" not in Girl.DailyActions:
                                                $ Girl.Statup("Love", 50, -2)
                                                $ Girl.Statup("Love", 90, -2)
                                                $ Girl.Statup("Obed", 50, 3)
                                                $ Girl.Statup("Obed", 80, 3)
                                                $ Girl.AddWord(1,"shopblock","shopblock") #recent and daily
                                        if Girl in (EmmaX,StormX,BetsyX):
                                                call AnyLine(Girl,"Какое разочарование.")
                                        elif Girl in (JeanX,LauraX):
                                                pass
                                        else:
                                                call AnyLine(Girl,"Оу. . .")
                                        $ Cart = []

                                    while Cart:
                                        menu:
                                            "Что вы хотели бы купить?"
                                            "Кружевной лифчик" if "lace bra" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] кружевной лифчик."
                                                    if Girl.Tag + " lace bra" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такой."
                                                            "Вы достаете тот, что у вас в рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " lace bra")
                                                    elif Player.Cash < 90:
                                                            "Вы смотрите на ценник, $90, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("lace bra")
                                                    else:
                                                            $ Player.Cash -= 90
                                                    if "lace bra" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("lace bra")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("lace bra")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 25)
                                                            $ Girl.Statup("Obed", 200, 20)
                                                            $ Girl.Statup("Inbt", 200, 20)
                                                            if Girl is RogueX:
                                                                    ch_r "Не знаю, надену ли я его, ну, может быть, если только мы будем наедине."
                                                            elif Girl is KittyX:
                                                                    ch_k "По крайней мере, ты ценишь мои достоинства."
                                                            elif Girl is EmmaX:
                                                                    ch_e "У меня не так уж и мало таких вещей. . ."
                                                            elif Girl is StormX:
                                                                    ch_s "Не то, чтобы я не ценила твой жест, но. . ."
                                                            elif Girl is JeanX:
                                                                    ch_j "Хороший вкус. . ."
                                                            elif Girl is JubesX:
                                                                    ch_v "Это не в моем обычном стиле. . ."
                                                            elif Girl is GwenX:
                                                                    ch_g "Ну, он вроде как милый. . ."
                                                            elif Girl is BetsyX:
                                                                    ch_b "Он. . . довольно симпатичный. . ."
                                                            elif Girl is DoreenX:
                                                                    ch_d "Ох. Он выглядит очень мило!"
                                                            elif Girl is WandaX:
                                                                    ch_w "Спасибо, он выглядит неплохо. . ."
                                            #end lace bra

                                            "Корсет" if "corset" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] корсет."
                                                    if Girl.Tag + " corset" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такой."
                                                            "Вы достаете тот, что у вас в рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                                    elif Player.Cash < 70:
                                                            "Вы смотрите на ценник, $70, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove(Girl.Tag + " corset")
                                                    else:
                                                            $ Player.Cash -= 70
                                                    if "corset" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("corset")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("corset")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 15)
                                                            $ Girl.Statup("Obed", 200, 20)
                                                            $ Girl.Statup("Inbt", 200, 10)
                                                            if Girl is LauraX:
                                                                    ch_l "Он. . . вроде бы клевый. . ."
                                                            elif Girl is JeanX:
                                                                    ch_j "Спасибо?"
                                            #end lace corset

                                            "Кружевной корсет" if "lace corset" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] кружевной корсет."
                                                    if Girl.Tag + " lace corset" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такой."
                                                            "Вы достаете тот, что у вас в рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                                    elif Player.Cash < 90:
                                                            "Вы смотрите на ценник, $90, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("lace corset")
                                                    else:
                                                            $ Player.Cash -= 90
                                                    if "lace corset" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("lace corset")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("lace corset")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 25)
                                                            $ Girl.Statup("Obed", 200, 30)
                                                            $ Girl.Statup("Inbt", 200, 20)
                                                            ch_l "Думаешь, он будет хорошо смотреться на мне?"
                                            #end lace corset

                                            "Кружевные трусики" if "lace panties" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] кружевные трусики."
                                                    if Girl.Tag + " lace panties" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такие."
                                                            "Вы достаете те, что в вашем рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " lace panties")
                                                    elif Player.Cash < 110:
                                                            "Вы смотрите на ценник, $110, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("lace panties")
                                                    else:
                                                            $ Player.Cash -= 110
                                                    if "lace panties" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("lace panties")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("lace panties")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 25)
                                                            $ Girl.Statup("Obed", 200, 20)
                                                            $ Girl.Statup("Inbt", 200, 20)
                                                            if Girl is RogueX:
                                                                    ch_r "По-моему, они слишком прозрачные. . ."
                                                            elif Girl is KittyX:
                                                                    ch_k "Они не оставляют места для воображения. . ."
                                                            elif Girl is EmmaX:
                                                                    ch_e "Это. . . необычный подарок."
                                                                    $ EmmaX.FaceChange("sly",1)
                                                                    ch_e "Но я его сохраню.. . ."
                                                            elif Girl is LauraX:
                                                                    ch_l "Они очень сексуальные. . ."
                                                            elif Girl is JeanX:
                                                                    ch_j "Ох, они очень милые. . ."
                                                            elif Girl is StormX:
                                                                    ch_s "Думаю, мне всегда пригодится еще одна пара. . ."
                                                            elif Girl is JubesX:
                                                                    ch_v "Немного. . . откровенные. . ."
                                                            elif Girl is GwenX:
                                                                    ch_g "Они довольно маленькие. . ."
                                                            elif Girl is BetsyX:
                                                                    ch_b "Они довольно. . . тонкие."
                                                            elif Girl is DoreenX:
                                                                    ch_d "Ох. Они. . . очень. . ."
                                                                    ch_d "-очень тонкие. . ."
                                                            elif Girl is WandaX:
                                                                    ch_w "Спасибо, они мне очень идут. . ."
                                            #end lace panties

                                            "Трусики в тигровую полоску" if "tiger panties" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] трусики в тигровую полоску."
                                                    if Girl.Tag + " tiger panties" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такие."
                                                            "Вы достаете те, что в вашем рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " tiger panties")
                                                    elif Player.Cash < 100:
                                                            "Вы смотрите на ценник, $100, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("tiger panties")
                                                    else:
                                                            $ Player.Cash -= 100
                                                    if "tiger panties" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("tiger panties")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("tiger panties")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 25)
                                                            $ Girl.Statup("Obed", 200, 20)
                                                            $ Girl.Statup("Inbt", 200, 20)
                                                            ch_v "Они очень милые. . ."
                                            #end tiger panties

                                            "Ажурные брюки" if "mesh pants" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] ажурные брюки."
                                                    if Player.Cash < 90:
                                                            "Вы смотрите на ценник, $90, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("mesh pants")
                                                    else:
                                                            $ Player.Cash -= 90
                                                    if "mesh pants" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("mesh pants")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("mesh pants")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 15)
                                                            $ Girl.Statup("Obed", 200, 30)
                                                            $ Girl.Statup("Inbt", 200, 30)
                                                            ch_l "Думаешь, они мне подойдут?"
                                            #end mesh pants

                                            "Чулки и пояс с подвязками" if "stockings and garterbelt" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] чулки и пояс с подвязками."
                                                    if Girl.Tag + " stockings and garterbelt" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такие."
                                                            "Вы достаете те, что в вашем рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " stockings and garterbelt")
                                                    elif Player.Cash < 100:
                                                            "Вы смотрите на ценник, $100, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("stockings and garterbelt")
                                                    else:
                                                            $ Player.Cash -= 100
                                                    if "stockings and garterbelt" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("stockings and garterbelt")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("stockings and garterbelt")
                                                            $ Player.AddWord(1,"purchased") #recent
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
                                            #end buy S&G

                                            "Гольфы" if "knee stockings" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] гольфы."
                                                    if "knee" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такие."
                                                            "Вы достаете те, что в вашем рюкзаке."
                                                            $ Player.Inventory.remove("knee")
                                                    elif Player.Cash < 50:
                                                            "Вы смотрите на ценник, $50, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("knee stockings")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "knee stockings" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("knee stockings")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("knee")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 5)
                                                            $ Girl.Statup("Obed", 200, 5)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            call AnyLine(Girl,"Они очень милые. . .")
                                            #end buy knee stockings

                                            "Высокие носки" if "socks" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] носки."
                                                    if Girl.Tag + " socks" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такие."
                                                            "Вы достаете те, что в вашем рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " socks")
                                                    elif Player.Cash < 50:
                                                            "Вы смотрите на ценник, $50, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("socks")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "socks" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("socks")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("socks")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 5)
                                                            $ Girl.Statup("Obed", 200, 5)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            call AnyLine(Girl,"Они очень милые. . .")
                                            #end buy socks

                                            "Колготки" if "pantyhose" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] колготки."
                                                    if Girl.Tag + " pantyhose" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такие."
                                                            "Вы достаете те, что в вашем рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " pantyhose")
                                                    elif Player.Cash < 50:
                                                            "Вы смотрите на ценник, $50, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("pantyhose")
                                                    else:
                                                            $ Player.Cash -= 50
                                                    if "pantyhose" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("pantyhose")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("pantyhose")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 5)
                                                            $ Girl.Statup("Obed", 200, 5)
                                                            $ Girl.Statup("Inbt", 200, 5)
                                                            call AnyLine(Girl,"Они очень красивые. . .")
                                            #end buy pantyhose

                                            "Ночнушку" if "nighty" in Cart:
                                                    "Вы соглашаетесь купить [Girl.Name_dat] ночнушку."
                                                    if Girl.Tag + " nighty" in Player.Inventory:
                                                            "Подождите-ка, у вас уже есть такая."
                                                            "Вы достаете ту, что у вас в рюкзаке."
                                                            $ Player.Inventory.remove(Girl.Tag + " nighty")
                                                    elif Player.Cash < 75:
                                                            "Вы смотрите на ценник, $75, вы не можете позволить себе такую покупку."
                                                            $ Cart.remove("nighty")
                                                    else:
                                                            $ Player.Cash -= 75
                                                    if "nighty" in Cart:
                                                            #if you successfully got it for her. . .
                                                            $ Cart.remove("nighty")
                                                            $ Girl.FaceChange("bemused",1)
                                                            $ Girl.Inventory.append("nighty")
                                                            $ Player.AddWord(1,"purchased") #recent
                                                            $ Girl.Statup("Love", 200, 40)
                                                            $ Girl.Statup("Obed", 200, 20)
                                                            $ Girl.Statup("Inbt", 200, 30)
                                                            ch_r "Ну, она слегка откровенная, но все равно очень милая."
                                                            $ Girl.Statup("Lust", 89, 10)
                                            #end buy nighty

                                            "Ничего" if "purchased" not in Player.RecentActions:
                                                    $ Girl.FaceChange("sad")
                                                    if "shopblock" not in Girl.DailyActions:
                                                            $ Girl.Statup("Love", 50, -2)
                                                            $ Girl.Statup("Love", 90, -2)
                                                            $ Girl.Statup("Obed", 50, 3)
                                                            $ Girl.Statup("Obed", 80, 3)
                                                            $ Girl.AddWord(1,"shopblock","shopblock") #recent and daily
                                                    "Вы все возвращаете."
                                                    if Girl in (EmmaX,StormX,BetsyX):
                                                            call AnyLine(Girl,"Какое разочарование.")
                                                    elif Girl in (JeanX,LauraX):
                                                            pass
                                                    else:
                                                            call AnyLine(Girl,"Оу. . .")
                                                    $ Cart = []
                                            "Больше ничего" if "purchased" in Player.RecentActions:
                                                    $ Girl.FaceChange("sad")
                                                    if "shopblock" not in Girl.DailyActions:
                                                            $ Girl.Statup("Love", 50, -1)
                                                            $ Girl.Statup("Obed", 50, 3)
                                                            $ Girl.Statup("Obed", 90, 2)
                                                    "Вы возвращаете все оставшееся."
                                                    $ Cart = []
                                    #End while Cart: loop


                                    $ Player.DrainWord("purchased") #removes purchased token
                                    $ Girl = 0
                    #end Dressing room loop"
                # End Lingerie while loop
        return
#End Lingerie shop   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Lingerie Shop menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Lingerie_Shop_Menu(Girl=0): #rkeljsvgbdw
    #called from Lingerie Shop when nobody is around, call Lingerie_Shop_Menu
    while True:
        menu:
            "Что вы хотели бы купить? У вас $[Player.Cash]."
            "Купить кружевной лифчик за $90.":            #not Laura
                    call Store_Girl_Select("lace bra",[LauraX])
                    if not Girl:
                            pass
                    elif Player.Cash >= 90:
                            "Вы покупаете кружевной лифчик, он идеально подойдет [Girl.Name_dat]."
                            $ Player.Inventory.append(Girl.Tag+" lace bra")
                            $ Player.Cash -= 90
                    else:
                            "У Вас не хватит на это денег."
            "Купить кружевные трусики за $110.":
                    call Store_Girl_Select("lace panties")
                    if not Girl:
                            pass
                    elif Player.Cash >= 110:
                            "Вы покупаете кружевные трусики, они идеально подойдут [Girl.Name_dat]."
                            $ Player.Inventory.append(Girl.Tag+" lace panties")
                            $ Player.Cash -= 110
                    else:
                            "У Вас не хватит на это денег."
            "Купить колготки за $50.":  #no for Rogue?, no Laura
                    call Store_Girl_Select("pantyhose")
                    if not Girl:
                            pass
                    elif Player.Cash >= 50:
                        "Вы покупаете колготки, они неплохо впишутся в образ [Girl.Name_rod]."
                        $ Player.Inventory.append(Girl.Tag+" pantyhose")
                        $ Player.Cash -= 50
                    else:
                        "У Вас не хватит на это денег."
            "Купить чулки и пояс с подвязками за $100.":
                    call Store_Girl_Select("stockings and garterbelt")
                    if not Girl:
                            pass
                    elif Player.Cash >= 100:
                        "Вы покупаете чулки и пояс с подвязками, они неплохо впишутся в образ [Girl.Name_rod]."
                        $ Player.Inventory.append(Girl.Tag+" stockings and garterbelt")
                        $ Player.Cash -= 100
                    else:
                        "У Вас не хватит на это денег."

            "Уникальные Предметы":
                    menu:
                        "Купить кружевную ночнушку для [RogueX.Name_rod] за $75." if "met" in RogueX.History and "nighty" not in RogueX.Inventory and "Rogue nighty" not in Player.Inventory:
                            if Player.Cash >= 75:
                                "Вы покупаете ночнушку, она будет хорошо смотреться на [RogueX.Name_dat]."
                                $ Player.Inventory.append("Rogue nighty")
                                $ Player.Cash -= 75
                            else:
                                "У Вас не хватит на это денег."
                        "Купить гольфы для [KittyX.Name_rod] за $50." if "met" in KittyX.History and "knee" not in KittyX.Inventory and "knee" not in Player.Inventory:
                            if Player.Cash >= 50:
                                "Вы покупаете гольфы, они неплохо впишутся в образ [KittyX.Name_rod]."
                                $ Player.Inventory.append("knee")
                                $ Player.Cash -= 50
                            else:
                                "У Вас не хватит на это денег."
                        "Купить красный корсет для [LauraX.Name_rod] за $70." if "met" in LauraX.History and "corset" not in LauraX.Inventory and "Laura corset" not in Player.Inventory:
                            if Player.Cash >= 70:
                                "Вы покупаете корсет, он будет хорошо смотреться на [LauraX.Name_dat]."
                                $ Player.Inventory.append("Laura corset")
                                $ Player.Cash -= 70
                            else:
                                "У Вас не хватит на это денег."
                        "Купить кружевной корсет для [LauraX.Name_rod] за $90." if "met" in LauraX.History and "lace corset" not in LauraX.Inventory and "Laura lace corset" not in Player.Inventory:
                            if Player.Cash >= 90:
                                "Вы покупаете корсет, он будет хорошо смотреться на [LauraX.Name_dat]."
                                $ Player.Inventory.append("Laura lace corset")
                                $ Player.Cash -= 90
                            else:
                                "У Вас не хватит на это денег."
                        "Купить черный корсет для [JeanX.Name_rod] за $70." if "met" in JeanX.History and "corset" not in JeanX.Inventory and "Jean corset" not in Player.Inventory:
                            if Player.Cash >= 70:
                                "Вы покупаете корсет, он будет хорошо смотреться на [JeanX.Name_dat]."
                                $ Player.Inventory.append("Jean corset")
                                $ Player.Cash -= 70
                            else:
                                "У Вас не хватит на это денег."
                        "Купить высокие носки для [JubesX.Name_rod] за $50." if "met" in JubesX.History and "socks" not in JubesX.Inventory and "socks" not in Player.Inventory:
                            if Player.Cash >= 50:
                                "Вы покупаете высокие носки, они неплохо впишутся в образ [JubesX.Name_rod]."
                                $ Player.Inventory.append("socks")
                                $ Player.Cash -= 50
                            else:
                                "У Вас не хватит на это денег."
                        "Назад":
                            pass
            # end "Unique Items" submenu

            "Готово.":
                    return
#End Lingerie Shop menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Swim Shop menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Swim_Shop_Menu(Girl=0): #rkeljsvgbdw
    #called from Swim Shop when nobody is around, call Swim_Shop_Menu
    while True:
        menu:
            "Что вы хотели бы купить? У вас $[Player.Cash]."
            "Купить лифчик бикини за $50.":
                    call Store_Girl_Select("bikini top",[BetsyX])
                    if not Girl:
                            pass
                    elif Player.Cash >= 50:
                            "Вы покупаете верх бикини, он будет хорошо смотреться на [Girl.Name_dat]."
                            $ Player.Inventory.append(Girl.Tag+" bikini top")
                            $ Player.Cash -= 50
                    else:
                            "У Вас не хватит на это денег."
            "Купить трусики бикини за $50.":
                    call Store_Girl_Select("bikini bottoms",[BetsyX])
                    if not Girl:
                            pass
                    elif Player.Cash >= 50:
                            "Вы покупаете трусики бикини, они будут хорошо смотреться на [Girl.Name_dat]."
                            $ Player.Inventory.append(Girl.Tag+" bikini bottoms")
                            $ Player.Cash -= 50
                    else:
                            "У Вас не хватит на это денег."

            "Купить купальник для [BetsyX.Name_rod] за $110." if "swimsuit" not in BetsyX.Inventory and "Betsy swimsuit" not in Player.Inventory:
                    if Player.Cash >= 110:
                        "Вы покупаете купальник, он будет хорошо смотреться на [BetsyX.Name_dat]."
                        $ Player.Inventory.append("Betsy swimsuit")
                        $ Player.Cash -= 110
                    else:
                        "У Вас не хватит на это денег."
            "Купить синюю мини-юбку для [KittyX.Name_rod] за $50." if "blue skirt" not in KittyX.Inventory and "Kitty blue skirt" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "Вы покупаете мини-юбку, она будет хорошо смотреться на [KittyX.Name_dat]."
                        $ Player.Inventory.append("Kitty blue skirt")
                        $ Player.Cash -= 50
                    else:
                        "У Вас не хватит на это денег."
            "I'm done.":
                    return
#End Swim Shop menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Store Girl selection menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Store_Girl_Select(Subject="",Excluded=[]): #rkeljsvgbdw
        # call Store_Girl_Select("Which girl?","bikini top")
        #"Girl" must be defined by prior function, Intro line is what is asked of the player.
        # Subject is the object being discussed, ie "bikini top".
        menu:
            "Для кого?"
            "Роуг" if "met" in RogueX.History and Subject not in RogueX.Inventory and "Rogue "+Subject not in Player.Inventory and RogueX not in Excluded:
                    $ Girl = RogueX
            "Китти" if "met" in KittyX.History and Subject not in KittyX.Inventory and "Kitty "+Subject not in Player.Inventory and KittyX not in Excluded:
                    $ Girl = KittyX
            "Эммы" if "met" in EmmaX.History and Subject not in EmmaX.Inventory and "Emma "+Subject not in Player.Inventory and EmmaX not in Excluded:
                    $ Girl = EmmaX
            "Лоры" if "met" in LauraX.History and Subject not in LauraX.Inventory and "Laura "+Subject not in Player.Inventory and LauraX not in Excluded:
                    $ Girl = LauraX
            "Джин" if "met" in JeanX.History and Subject not in JeanX.Inventory and "Jean "+Subject not in Player.Inventory and JeanX not in Excluded:
                    $ Girl = JeanX
            "Шторм" if "met" in StormX.History and Subject not in StormX.Inventory and "Storm "+Subject not in Player.Inventory and StormX not in Excluded:
                    $ Girl = StormX
            "Джубс" if "met" in JubesX.History and Subject not in JubesX.Inventory and "Jubes "+Subject not in Player.Inventory and JubesX not in Excluded:
                    $ Girl = JubesX
            "Гвен" if "met" in GwenX.History and Subject not in GwenX.Inventory and "Gwen "+Subject not in Player.Inventory and GwenX not in Excluded:
                    $ Girl = GwenX
            "Бетси" if "met" in BetsyX.History and Subject not in BetsyX.Inventory and "Betsy "+Subject not in Player.Inventory and BetsyX not in Excluded:
                    $ Girl = BetsyX
            "Дорин" if "met" in DoreenX.History and Subject not in DoreenX.Inventory and "Doreen "+Subject not in Player.Inventory and DoreenX not in Excluded:
                    $ Girl = DoreenX
            "Ванда" if "met" in WandaX.History and Subject not in WandaX.Inventory and "Wanda "+Subject not in Player.Inventory and WandaX not in Excluded:
                    $ Girl = WandaX

            #grayed out
            #shows if you or the girl already have the item
            "Роуг (locked)" if "met" in RogueX.History and (Subject in RogueX.Inventory or "Rogue "+Subject in Player.Inventory) and RogueX not in Excluded:
                    $ Girl = RogueX
            "Китти (locked)" if "met" in KittyX.History and (Subject in KittyX.Inventory or "Kitty "+Subject in Player.Inventory) and KittyX not in Excluded:
                    $ Girl = KittyX
            "Эммы (locked)" if "met" in EmmaX.History and (Subject in EmmaX.Inventory or "Emma "+Subject in Player.Inventory) and EmmaX not in Excluded:
                    $ Girl = EmmaX
            "Лоры (locked)" if "met" in LauraX.History and (Subject in LauraX.Inventory or "Laura "+Subject in Player.Inventory) and LauraX not in Excluded:
                    $ Girl = LauraX
            "Джин (locked)" if "met" in JeanX.History and (Subject in JeanX.Inventory or "Jean "+Subject in Player.Inventory) and JeanX not in Excluded:
                    $ Girl = JeanX
            "Шторм (locked)" if "met" in StormX.History and (Subject in StormX.Inventory or "Storm "+Subject in Player.Inventory) and StormX not in Excluded:
                    $ Girl = StormX
            "Джубс (locked)" if "met" in JubesX.History and (Subject in JubesX.Inventory or "Jubes "+Subject in Player.Inventory) and JubesX not in Excluded:
                    $ Girl = JubesX
            "Гвен (locked)" if "met" in GwenX.History and (Subject in GwenX.Inventory or "Gwen "+Subject  in Player.Inventory) and GwenX not in Excluded:
                    $ Girl = GwenX
            "Бетси (locked)" if "met" in BetsyX.History and (Subject in BetsyX.Inventory or "Betsy "+Subject in Player.Inventory) and BetsyX not in Excluded:
                    $ Girl = BetsyX
            "Дорин (locked)" if "met" in DoreenX.History and (Subject in DoreenX.Inventory or "Doreen "+Subject in Player.Inventory) and DoreenX not in Excluded:
                    $ Girl = DoreenX
            "Ванда (locked)" if "met" in WandaX.History and (Subject in WandaX.Inventory or "Wanda "+Subject in Player.Inventory) and WandaX not in Excluded:
                    $ Girl = WandaX

            "Неважно":
                    $ Girl = 0
        return
#End Store Girl selection menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



label Dressing_Strip_Bra(Item=0):
        #called if girl decides to strip panties in shops
        # call Dressing_Strip_Bra("lace bra")
        if not Item:
                return
        $ Girl.FaceChange("sexy")
        call AnyLine(Girl,"Конечно. . .")
        if Girl.Over or Girl.Chest:
                $ Girl.Uptop = 1
                pause 0.3
        if Girl in (JubesX,DoreenX) and Girl.Acc: #removes coat
                $ Girl.Acc = 0
                pause 0.3
        if Girl.Over:
                $ Girl.Over = 0
                pause 0.3
        if Girl.Chest:
                $ Girl.Chest = 0
        call Girl_First_Topless(Girl)
        pause 0.3
        $ Girl.Chest = Item
        pause 0.3
        $ Girl.Uptop = 0
        if Second and Second.Loc == bg_current and Item not in Cart:
                $ Girl.GirlLikeUp(Second,2)
                $ Second.GirlLikeUp(Girl,5)
        call AnyLine(Girl,". . .")
        return

label Dressing_Strip_Panties(Item=0):
        #called if girl decides to strip panties in shops
        # call Dressing_Strip_Panties("lace panties")
        if not Item:
                return
        $ Girl.FaceChange("sexy")
        call AnyLine(Girl,"Конечно. . .")
        if Girl.Legs:
                $ Girl.Upskirt = 1
                pause 0.3
                $ Girl.Legs = 0
                pause 0.3
        if Girl.Hose:
                $ Girl.Hose = 0
                pause 0.3
        if Girl.Panties:
                $ Girl.PantiesDown = 1
                pause 0.2
                $ Girl.Panties = 0
        call Girl_First_Bottomless(Girl)
        pause 0.3
        $ Girl.Panties = Item
        $ Girl.PantiesDown = 0
        $ Girl.Upskirt = 0
        if Second and Second.Loc == bg_current and Item not in Cart:
            $ Girl.GirlLikeUp(Second,3)
            $ Second.GirlLikeUp(Girl,5)
        call AnyLine(Girl,". . .")
        return


label Dressing_Strip_Both(Item=0,ItemB=0):
        #called if girl decides to strip both in shops
        # call Dressing_Strip_Both("bikini top","bikini bottoms")
        if not Item:
                return
        $ Girl.FaceChange("sexy")
        call AnyLine(Girl,"Конечно. . .")
        #top off
        if Girl.Over or Girl.Chest:
                $ Girl.Uptop = 1
                pause 0.3
        if Girl in (JubesX,DoreenX) and Girl.Acc: #removes coat
                $ Girl.Acc = 0
                pause 0.3
        if Girl.Over:
                $ Girl.Over = 0
                pause 0.3
        if Girl.Chest:
                $ Girl.Chest = 0
        call Girl_First_Topless(Girl)

        #bottoms off
        if Girl.Legs:
                $ Girl.Upskirt = 1
                pause 0.3
                $ Girl.Legs = 0
                pause 0.3
        if Girl.Hose:
                $ Girl.Hose = 0
                pause 0.3
        if Girl.Panties:
                $ Girl.PantiesDown = 1
                pause 0.2
                $ Girl.Panties = 0
        call Girl_First_Bottomless(Girl)

        #bottoms on
        pause 0.3
        $ Girl.Panties = ItemB
        $ Girl.PantiesDown = 0
        $ Girl.Upskirt = 0
        #top on
        pause 0.3
        $ Girl.Chest = Item
        pause 0.3
        $ Girl.Uptop = 0
        if Second and Second.Loc == bg_current and Item not in Cart:
                $ Girl.GirlLikeUp(Second,5)
                $ Second.GirlLikeUp(Girl,10)
        call AnyLine(Girl,". . .")
        return
#End Date_Shopping   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
