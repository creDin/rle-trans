# Start You Cumming //////////////////////////////////////////////////////////////////////////////////

label Player_Cumming(Girl=0,Tempmod = Tempmod): #rkeljsvg
    if "phonesex" in Player.RecentActions:
            $ Player.Semen -= 1
            $ Player.Focus = 0
            call Punch
            if Player.Male:
                    "Вы разбрызгиваете сперму по всей комнате."
            else:
                    "Вы разбрызгиваете соки по всей комнате."
            return

    $ Girl = GirlCheck(Girl)

    call Shift_Focus(Girl)
    if Trigger == "blow":
            $ Tempmod += 5

    if Girl.Addict > 75:
            $ Tempmod += 20
    elif Girl.Addict > 50:
            $ Tempmod += 5

    if Girl.Swallow >= 10:
            $ Tempmod += 15
    elif Girl.Swallow >= 3:
            $ Tempmod += 5

    if (Girl.CreamP + Girl.CreamA) >= 10:
            $ Tempmod += 15
    elif (Girl.CreamP + Girl.CreamA) >= 3:
            $ Tempmod += 5

    $ D20 = renpy.random.randint(1, 20)

    if not Player.Male:
            jump Player_Female_Cumming
# intro lines
    if Situation == "swap":
            #if you swapped to the partner
            $ Line = "Итак, чтобы вы хотели от "+Girl.Name_rod+"?"
    elif Trigger == "hand":
            $ Line = "С каждым движением ее руки вы чувствуете, что вот-вот кончите. . ."
    elif Trigger == "blow":
            $ Line = "С каждым движением ее головы вы чувствуете, что вот-вот кончите. . ."
    elif Trigger == "titjob":
            $ Line = "С каждым движением ее сисек вы чувствуете, что вот-вот кончите. . ."
    elif Trigger == "sex" or Trigger == "anal":
            $ Line = "Двигаясь внутри нее, вы чувствуете, что вот-вот кончите. . ."
    elif Trigger == "hotdog":
            $ Line = "С каждым вашим движением вы чувствуете, что вот-вот кончите. . ."
    else:
            $ Line = "Вы чувствуете, что вот-вот кончите. . ."

    $ Girl.FaceChange("sexy")

    menu:
        "[Line]"
        "Предупредить ее":
                $ Situation = "warn"
                jump Girl_Warn_Her

        "Спросить, можно ли кончить ей в рот":
                $ Situation = "asked"
                jump Girl_In_Mouth
        "Кончить ей в рот без предупреждения" if (Trigger == "blow" or Trigger == "hand" or Trigger == "titjob" or Girl.Pose == "69") and Situation != "swap":
                $ Situation = "auto"
                jump Girl_In_Mouth

        "Спросить, можно ли кончить в нее" if Trigger == "sex" and Situation != "swap":
                $ Situation = "asked"
                jump Girl_Creampie_P
        "Спросить, можно ли кончить в нее" if Trigger == "anal" and Situation != "swap":
                $ Situation = "asked"
                jump Girl_Creampie_A

        "Кончить в нее" if Trigger == "sex" and Situation != "swap":
                $ Situation = "auto"
                jump Girl_Creampie_P
        "Кончить в нее" if Trigger == "anal" and Situation != "swap":
                $ Situation = "auto"
                jump Girl_Creampie_A
        "Кончить на. . .":
            menu:
                "На лицо":
                        jump Girl_Facial
                "На сиськи":
                        jump Girl_TitSpunk
                "На попку": #if (Girl == RogueX or Girl == JeanX)and (Trigger == "sex" or Trigger == "anal" or Trigger == "hotdog" or Trigger == "foot"):
                        $ Girl.Pose = "doggy"
                        jump Girl_Cum_Outside
                "На животик": #if (Girl != RogueX and Girl != JeanX) and (Trigger == "sex" or Trigger == "anal" or Trigger == "hotdog" or Trigger == "foot" or Trigger == "psy"):
                        if Girl.Pose == "doggy":
                            if Girl in (EmmaX,JeanX,WandaX):
                                $ Girl.Pose = 0
                            else:
                                $ Girl.Pose = "sex"
                        jump Girl_Cum_Outside
                "На ножки":
                        jump Girl_FeetSpunk

        "Подозвать к себе [Partner.Name_vin]." if Partner in TotalGirls and Situation != "swap":
                $ Situation = "swap"
                $ Tempmod = 0
                $ Trigger = 0
                call Shift_Focus(Partner) #makes the partner the lead and the lead the partner
                call AllReset(Partner) #resets the position of the original lead
                $ renpy.show(Ch_Focus.Tag+"_Sprite",at_list=[Sprite_Set(Ch_Focus.SpriteLoc,50)],zorder=Ch_Focus.Layer)
                call Player_Cumming(Ch_Focus,Tempmod = 0) #Does the cumshot focused on the original Partner

                call Shift_Focus(Partner) #makes the original partner the partner again
                call AllReset(Partner)  #resets the position of the partner

                $ Situation = 0
                call AllReset(Girl) #resets the position of the original lead
                "[Girl.Name] отстраняется."

                return

        "Просто кончить" if Trigger2 == "jackin":
                if "cockout" not in Player.RecentActions:
                        $ Player.Spunk = "in"
                        "Вы кончаете в свои штаны."
                else:
                        "Вы разбрызгиваете сперму по всей комнате."
                jump Girl_Orgasm_After
        "Сдержаться и закончить" if Trigger != "psy" and Girl.Loc == bg_current and Situation != "swap" and Player.FocusX:
            if renpy.showing(Girl.Tag+"_BJ_Animation") or renpy.showing(Girl.Tag+"_69_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                    if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
                            jump Manic_Suck
                    call expression Girl.Tag+"_BJ_Reset"
            elif renpy.showing(Girl.Tag+"_HJ_Animation"): #if renpy.showing("Rogue_HJ_Animation"):
                    call expression Girl.Tag+"_HJ_Reset"
            elif renpy.showing(Girl.Tag+"_Doggy_Animation"): #if renpy.showing("Rogue_Doggy_Animation"):
                    call expression Girl.Tag+"_Doggy_Reset"
            elif renpy.showing(Girl.Tag+"_SexSprite"): #fix
                    call expression Girl.Tag+"_Sex_Reset"
            if ApprovalCheck(Girl, 500, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Addict > 50 and Girl.Swallow: #If addict + Inbt is > obedience + 50. . .
                    $ Girl.Eyes = "manic"
                    $ Girl.Mouth = "kiss"
                    $ Speed = 0
                    "От паники ее глаза расширяются."
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Ты уверена, что не передумаешь, [Girl.Petname]?"
                            else:
                                ch_r "Ты уверен, что не передумаешь, [Girl.Petname]?"
                    elif Girl is KittyX:
                            if not Player.Male:
                                ch_k "Ты[Girl.like]в этом уверена?"
                            else:
                                ch_k "Ты[Girl.like]в этом уверен?"
                    elif Girl is EmmaX:
                            ch_e "Ты не передумаешь, [Girl.Petname]?"
                    elif Girl is LauraX:
                            if not Player.Male:
                                ch_l "Ты уверена?"
                            else:
                                ch_l "Ты уверен?"
                    elif Girl is JeanX:
                            if not Player.Male:
                                ch_j "Куда это ты собралась?"
                            else:
                                ch_j "Куда это ты собрался?"
                    elif Girl is StormX:
                            ch_s "Подожди. . ."
                    elif Girl is JubesX:
                            ch_v "Подожди, ты позволишь всем усилиям пропасть зря?"
                    elif Girl is GwenX:
                            ch_g "Эм, я могла бы закончить. . . ты не передумаешь?"
                    elif Girl is BetsyX:
                            ch_b "Я. . . не прочь довести тебя до кульминации. . ."
                    elif Girl is DoreenX:
                            ch_d "Я. . . бы хотела довести тебя до кульминации. . ."
                    elif Girl is WandaX:
                            ch_w "Я, эм, могу позаботиться о тебе. . ."
                    $ Girl.Blush = 2
                    menu:
                        extend ""
                        "Ладно, но только, если ты все проглотишь.":
                                        if not renpy.showing(Girl.Tag+"_BJ_Animation") and not renpy.showing(Girl.Tag+"_69_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                                                call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                                        $ Girl.FaceChange("sucking")
                                        $ Speed = 2
                                        "Она кивает и берет головку вашего члена в свой рот. Когда вы кончаете она с жадностью все глотает."
                                        $ Girl.FaceChange("sexy")
                                        $ Girl.Mouth = "sucking"
                                        $ Girl.Spunk.append("mouth")
                                        ". . ."
                                        $ Speed = 0
                                        $ Girl.FaceChange("sad")
                                        $ Girl.Mouth = "lipbite"
                                        if Girl is RogueX:
                                                ch_r "Я бы не хотела, чтобы она пропала впустую."
                                        elif Girl is KittyX:
                                                ch_k "Ты же знаешь, я люблю молочко."
                                        elif Girl is EmmaX:
                                                ch_e "Не трать ничего впустую."
                                        elif Girl is LauraX:
                                                ch_l "Ням."
                                        elif Girl is JeanX:
                                                ch_j "Ммм."
                                        elif Girl is StormX:
                                                ch_s "Мммм. . ."
                                        elif Girl is JubesX:
                                                ch_v "Отлично!"
                                        elif Girl is GwenX:
                                                ch_g "Меня не нужно просить дважды."
                                        elif Girl is BetsyX:
                                                ch_b "Я не возражаю. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Конечно!"
                                        elif Girl is WandaX:
                                                ch_w "Конечно."
                                        $ Girl.Statup("Obed", 50, 2,Alt=[[JeanX],800,4]) #+4 for Jean)
                                        $ Girl.Statup("Obed", 70, 1)
                                        $ Girl.Statup("Inbt", 30, 2)
                                        $ Girl.Statup("Inbt", 50, 3)
                                        jump Girl_Swallowed
                        "Нет, хватит.": #If addict is > obedience + 50. . .
                                if ApprovalCheck(Girl, 250, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) or Girl.Addict > 75:
                                        $ Girl.Statup("Obed", 50, -1)
                                        $ Girl.Statup("Obed", 70, -2)
                                        $ Girl.Statup("Inbt", 30, 2)
                                        $ Girl.Statup("Inbt", 70, 3)
                                        if not renpy.showing(Girl.Tag+"_BJ_Animation") and not renpy.showing(Girl.Tag+"_69_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                                            call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                                            $ Speed = 4
                                        "Она заглатывает ваш член, вы не можете сдержаться и наполняете ее глотку."
                                        $ Speed = 0
                                        if Girl is RogueX:
                                                ch_r "Я. . . просто не смогла удержаться."
                                        elif Girl is KittyX:
                                                ch_k "Вот теперь. . . мы закончили."
                                        elif Girl is EmmaX:
                                                ch_e "Что ж, теперь да."
                                        elif Girl is LauraX:
                                                ch_l "Теперь да."
                                        elif Girl is JeanX:
                                                ch_j "Ладно, вот теперь мы закончили."
                                        elif Girl is StormX:
                                                ch_s "Вот теперь мы закончили. . ."
                                        elif Girl is JubesX:
                                                ch_v "Ладно, вот -сейчас- мы закончили."
                                        elif Girl is GwenX:
                                                ch_g "Ну, теперь все."
                                        elif Girl is BetsyX:
                                                ch_b "Ты меня разочаровал. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Извини. . ."
                                        elif Girl is WandaX:
                                                ch_w "Вот теперь хватит."
                                        jump Girl_Swallowed
                                else:
                                        $ Girl.Statup("Obed", 30, 3,Alt=[[JeanX],800,3]) #+3 for Jean
                                        $ Girl.Statup("Obed", 70, 5)
                                        $ Girl.FaceChange("sad")
                                        $ Girl.Brows = "confused"
                                        if Girl is RogueX:
                                                ch_r "Ладно. . ."
                                        elif Girl is KittyX:
                                                ch_k "Как скажешь."
                                        elif Girl is EmmaX:
                                                ch_e "Если ты настаиваешь."
                                        elif Girl is LauraX:
                                                ch_l "Гад."
                                        elif Girl is JeanX:
                                                ch_j "Как скажешь."
                                        elif Girl is StormX:
                                                ch_s ". . ."
                                        elif Girl is JubesX:
                                                ch_v "Нууу. . . Я все еще думаю, что это было расточительством."
                                        elif Girl is GwenX:
                                                ch_g "Оу!"
                                        elif Girl is BetsyX:
                                                ch_b "Бред. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Вздор!"
                                        elif Girl is WandaX:
                                                ch_w "Черт."
                                        $ Line = 0
                                        $ Player.Focus -= 5
                                        return
            #manic, wanted to swallow
            $ Girl.FaceChange("sexy", 1)
            $ Girl.Statup("Obed", 50, 2)
            "Вы отстраняетесь от нее. Она смотрит на вас и облизывает губы."

            if Girl is RogueX:
                    ch_r "Ну, [Girl.Petname], что дальше?"
            elif Girl is KittyX:
                    ch_k "Ох? Чем еще займемся?"
            elif Girl is EmmaX:
                    ch_e "Хорошо, [Girl.Petname], что дальше?"
            elif Girl is LauraX:
                    ch_l "Что теперь?"
            elif Girl is JeanX:
                    ch_j "Ладно, что теперь?"
            elif Girl is StormX:
                    ch_s "Какие тогда у тебя предложения?"
            elif Girl is JubesX:
                    ch_v "Хорошо, так что ты хочешь?"
            elif Girl is GwenX:
                    ch_g "Ну, что ты хочешь?"
            elif Girl is BetsyX:
                    ch_b "Что теперь? . ."
            elif Girl is DoreenX:
                    ch_d "Хорошо, что дальше?"
            elif Girl is WandaX:
                    ch_w "Ну, и что теперь?"
            $ Line = 0
            $ Player.Focus = 95
            return
            #end "Сдержаться и закончить"
#End Main orgasm menu

label Player_Female_Cumming:

    $ Line = "Вы чувствуете, что вот-вот кончите. . ."
    $ Girl.FaceChange("sexy")

    menu:
        "[Line]"
        "Предупредить ее":
                $ Situation = "warn"
                jump Girl_Warn_Her_Female

        "Спросить, можно ли кончить ей в рот":
                $ Situation = "asked"
                jump Girl_In_Mouth_Female
        "Кончить ей в рот без предупреждения" if (Trigger == "cun" or Trigger == "finger") and Situation != "swap":
                $ Situation = "auto"
                jump Girl_In_Mouth_Female

        "Подозвать к себе [Partner.Name_vin]." if Partner in TotalGirls and Situation != "swap":
                $ Situation = "swap"
                $ Tempmod = 0
                call Shift_Focus(Partner) #makes the partner the lead and the lead the partner
                call AllReset(Partner) #resets the position of the original lead
                call Player_Cumming(Ch_Focus,Tempmod = 0) #Does the cumshot focused on the original Partner

                call Shift_Focus(Partner) #makes the original partner the partner again
                call AllReset(Partner)  #resets the position of the partner

                $ Situation = 0
                "[Girl.Name] отстраняется."

                call AllReset(Girl) #resets the position of the original lead
                return

        "Просто кончить":
                $ Situation = "auto"
                if "cockout" not in Player.RecentActions:
                        "Ваши штаны теперь мокрые."

                elif renpy.showing(Girl.Tag+"_Finger_Animation"):
                        $ Girl.Spunk.append("hand")
                        "Вы позволяете ей продолжить, вскоре вас охватывает оргазм и вы кончаете ей на руку."
                elif renpy.showing(Girl.Tag+"_CUN_Animation"):
                        jump Girl_In_Mouth_Female
                elif renpy.showing(Girl.Tag+"_BJ_Animation") or renpy.showing(Girl.Tag+"_69_Animation"):
                        jump Girl_Facial
                elif renpy.showing(Girl.Tag+"_TJ_Animation"):
                        jump Girl_Facial
                elif renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"):
                        "Вы продолжаете трахать ее, вскоре вас охватывает оргазм и вы кончаете."
                else:
                        "Вы разбрызгиваете соки по всей комнате."
                jump Girl_Orgasm_After

        "Сдержаться и закончить" if Trigger != "psy" and Girl.Loc == bg_current and Situation != "swap" and Player.FocusX:
            if renpy.showing(Girl.Tag+"_CUN_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                    if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
                            $ Girl.Eyes = "manic"
                            $ Speed = 0
                            "Вы отстраняешься от нее, с ее губ стекают соки. Ее глаза расширяются от удивления."
                            $ Girl.Mouth = "sucking"
                            $ Girl.Spunk.append("mouth")
                            $ Speed = 4
                            "Она набрасывается на вашу киску и глубоко впивается в нее, жадно высасывая все ваши жидкости."
                            $ Speed = 0
                            $ Girl.Mouth = "lipbite"
                            "Закончив, она облизывает свои губы."
                            $ Girl.FaceChange("bemused")
                            if Girl is EmmaX:
                                    ch_e "Извини, [Girl.Petname], но я не хочу, чтобы все пропало впустую."
                            elif Girl is JeanX:
                                    $ Girl.FaceChange("sly",2,Mouth="lipbite")
                                    ch_j ". . ."
                            elif Girl is StormX:
                                    ch_s "Это было бы расточительством. . ."
                            else:
                                    call AnyLine(Girl,"Извини, [Girl.Petname], я не могла допустить, чтобы все пропало просто так.")
                            $ Girl.Statup("Obed", 200, -5,Alt=[[JeanX],800,5]) #+5 for Jean
                            $ Girl.Statup("Inbt", 200, 10)
                            jump Girl_Swallowed
                    call expression Girl.Tag+"_CUN_Reset"
            elif renpy.showing(Girl.Tag+"_Finger_Animation"): #if renpy.showing("Rogue_HJ_Animation"):
                    call expression Girl.Tag+"_Finger_Reset"
            elif renpy.showing(Girl.Tag+"_Doggy_Animation"): #if renpy.showing("Rogue_Doggy_Animation"):
                    call expression Girl.Tag+"_Doggy_Reset"
            elif renpy.showing(Girl.Tag+"_SexSprite"): #fix
                    call expression Girl.Tag+"_Sex_Reset"
            if ApprovalCheck(Girl, 500, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Addict > 50 and Girl.Swallow: #If addict + Inbt is > obedience + 50. . .
                    $ Girl.Eyes = "manic"
                    $ Girl.Mouth = "kiss"
                    $ Speed = 0
                    "От паники ее глаза расширяются."
                    if Girl is RogueX:
                            ch_r "Ты уверена, что не передумаешь, [Girl.Petname]?"
                    elif Girl is KittyX:
                            ch_k "Ты[Girl.like]уверена?"
                    elif Girl is EmmaX:
                            ch_e "Ты не передумаешь, [Girl.Petname]?"
                    elif Girl is LauraX:
                            ch_l "Уверена?"
                    elif Girl is JeanX:
                            ch_j "Куда это ты собралась?"
                    elif Girl is StormX:
                            ch_s "Подожди. . ."
                    elif Girl is JubesX:
                            ch_v "Подожди, ты позволишь всем усилиям пропасть впустую?"
                    elif Girl is GwenX:
                            ch_g "Эм, я могла бы довести все до конца. . . ты не против?"
                    elif Girl is BetsyX:
                            ch_b "Я. . . бы хотела довести все до конца. . ."
                    elif Girl is DoreenX:
                            ch_d "Я. . . бы хотела закончить начатое. . ."
                    elif Girl is WandaX:
                            ch_w "Я, эм, могу позаботиться о тебе. . ."
                    $ Girl.Blush = 2
                    menu:
                        extend ""
                        "Ладно, но только, если ты все проглотишь.":
                                        if not renpy.showing(Girl.Tag+"_CUN_Animation") and not renpy.showing(Girl.Tag+"_69_CUN"): #if not renpy.showing("Rogue_BJ_Animation"):
                                                call expression Girl.Tag+"_CUN_Launch" pass ("cum")
                                        $ Girl.FaceChange("sucking")
                                        $ Speed = 4
                                        "Она кивает и обхватывает губами вашу киску. Когда вы кончаете, она жадно все проглотывает."
                                        $ Girl.FaceChange("sexy")
                                        $ Girl.Mouth = "sucking"
                                        $ Girl.Spunk.append("mouth")
                                        ". . ."
                                        $ Speed = 0
                                        $ Girl.FaceChange("sad")
                                        $ Girl.Mouth = "lipbite"
                                        if Girl is RogueX:
                                                ch_r "Я бы не хотела, чтобы она пропала впустую."
                                        elif Girl is KittyX:
                                                ch_k "Ты же знаешь, я люблю соки."
                                        elif Girl is EmmaX:
                                                ch_e "Не трать ничего впустую."
                                        elif Girl is LauraX:
                                                ch_l "Ням."
                                        elif Girl is JeanX:
                                                ch_j "Ммм."
                                        elif Girl is StormX:
                                                ch_s "Мммм. . ."
                                        elif Girl is JubesX:
                                                ch_v "Отлично!"
                                        elif Girl is GwenX:
                                                ch_g "Меня не нужно просить дважды."
                                        elif Girl is BetsyX:
                                                ch_b "Я не возражаю. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Конечно!"
                                        elif Girl is WandaX:
                                                ch_w "Конечно."
                                        $ Girl.Statup("Obed", 50, 2,Alt=[[JeanX],800,4]) #+4 for Jean)
                                        $ Girl.Statup("Obed", 70, 1)
                                        $ Girl.Statup("Inbt", 30, 2)
                                        $ Girl.Statup("Inbt", 50, 3)
                                        jump Girl_Swallowed
                        "Нет, хватит.": #If addict is > obedience + 50. . .
                                if ApprovalCheck(Girl, 250, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) or Girl.Addict > 75:
                                        $ Girl.Statup("Obed", 50, -1)
                                        $ Girl.Statup("Obed", 70, -2)
                                        $ Girl.Statup("Inbt", 30, 2)
                                        $ Girl.Statup("Inbt", 70, 3)
                                        if not renpy.showing(Girl.Tag+"_CUN_Animation") and not renpy.showing(Girl.Tag+"_69_CUN"): #if not renpy.showing("Rogue_BJ_Animation"):
                                            call expression Girl.Tag+"_CUN_Launch" pass ("cum")
                                            $ Speed = 4
                                        "Она кидается на вас, вы не можете сдержаться и наполняете ее глотку."
                                        $ Speed = 0
                                        if Girl is RogueX:
                                                ch_r "Я. . . просто не смогла удержаться."
                                        elif Girl is KittyX:
                                                ch_k "Вот теперь. . . мы закончили."
                                        elif Girl is EmmaX:
                                                ch_e "Что ж, теперь да."
                                        elif Girl is LauraX:
                                                ch_l "Теперь да."
                                        elif Girl is JeanX:
                                                ch_j "Ладно, вот теперь мы закончили."
                                        elif Girl is StormX:
                                                ch_s "Вот теперь мы закончили. . ."
                                        elif Girl is JubesX:
                                                ch_v "Ладно, вот -сейчас- мы закончили."
                                        elif Girl is GwenX:
                                                ch_g "Ну, теперь да."
                                        elif Girl is BetsyX:
                                                ch_b "Ты меня разочаровала. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Извини. . ."
                                        elif Girl is WandaX:
                                                ch_w "Вот теперь хватит."
                                        jump Girl_Swallowed
                                else:
                                        $ Girl.Statup("Obed", 30, 3,Alt=[[JeanX],800,3]) #+3 for Jean
                                        $ Girl.Statup("Obed", 70, 5)
                                        $ Girl.FaceChange("sad")
                                        $ Girl.Brows = "confused"
                                        if Girl is RogueX:
                                                ch_r "Ладно. . ."
                                        elif Girl is KittyX:
                                                ch_k "Как скажешь."
                                        elif Girl is EmmaX:
                                                ch_e "Если ты настаиваешь."
                                        elif Girl is LauraX:
                                                ch_l "Гадина."
                                        elif Girl is JeanX:
                                                ch_j "Как скажешь."
                                        elif Girl is StormX:
                                                ch_s ". . ."
                                        elif Girl is JubesX:
                                                ch_v "Нууу. . . Я все еще думаю, что это было расточительством."
                                        elif Girl is GwenX:
                                                ch_g "Оу!"
                                        elif Girl is BetsyX:
                                                ch_b "Бред. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Вздор!"
                                        elif Girl is WandaX:
                                                ch_w "Черт."
                                        $ Line = 0
                                        $ Player.Focus -= 5
                                        return
            #manic, wanted to swallow
            $ Girl.FaceChange("sexy", 1)
            $ Girl.Statup("Obed", 50, 2)
            "Вы отстраняетесь от нее. Она смотрит на вас и облизывает губы."

            if Girl is RogueX:
                    ch_r "Ну, [Girl.Petname], что дальше?"
            elif Girl is KittyX:
                    ch_k "Ох? Чем еще займемся?"
            elif Girl is EmmaX:
                    ch_e "Хорошо, [Girl.Petname], что дальше?"
            elif Girl is LauraX:
                    ch_l "Что теперь?"
            elif Girl is JeanX:
                    ch_j "Ладно, что теперь?"
            elif Girl is StormX:
                    ch_s "Какие тогда у тебя предложения?"
            elif Girl is JubesX:
                    ch_v "Хорошо, так что ты хочешь?"
            elif Girl is GwenX:
                    ch_g "Ну, что ты теперь хочешь?"
            elif Girl is BetsyX:
                    ch_b "Что теперь? . ."
            elif Girl is DoreenX:
                    ch_d "Ладно, что дальше?"
            elif Girl is WandaX:
                    ch_w "Ну, и что дальше?"
            $ Line = 0
            $ Player.Focus = 95
            return
            #end "Сдержаться и закончить"

label Manic_Suck: #rkeljsvg
        $ Girl.Eyes = "manic"
        $ Speed = 0
        "Вы вытаскиваете свой член из ее рта с звонким \"чпоком\", ее глаза расширяются от удивления."
        $ Girl.Mouth = "sucking"
        $ Girl.Spunk.append("mouth")
        $ Speed = 4
        "Она насаживается своим ртом на ваш член и начинает сосать его так жадно и сильно, словно через него хочет высосать все ваши соки."
        $ Speed = 0
        $ Girl.Mouth = "lipbite"
        "Закончив, она облизывает свои губы."
        $ Girl.FaceChange("bemused")
        if Girl is EmmaX:
                ch_e "Извини, [Girl.Petname], но я не хочу, чтобы все пропало впустую."
        elif Girl is JeanX:
                $ Girl.FaceChange("sly",2,Mouth="lipbite")
                ch_j ". . ."
        elif Girl is StormX:
                ch_s "Это было бы расточительством. . ."
        else:
                call AnyLine(Girl,"Извини, [Girl.Petname], я не могла допустить, чтобы все пропало просто так.")
        $ Girl.Statup("Obed", 200, -5,Alt=[[JeanX],800,5]) #+5 for Jean
        $ Girl.Statup("Inbt", 200, 10)
        jump Girl_Swallowed

#Warn her start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Warn_Her:  #rkeljsvg
        "Вы даете ей знать, что собираетесь кончить."
        $ Girl.Statup("Love", 90, 3,Alt=[[JeanX],900,5]) #+5 for Jean
        if Girl.Obed >= 500:
                $ Girl.Statup("Obed", 80, 5)
        if ("hungry" in Girl.Traits and D20 >= 5):# or Girl == JubesX:
                if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                    call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                    "Она усмехается, подается назад со звонким 'чпок', а затем начинает с усердием вам дрочить."
                $ Speed = 2
                $ Girl.FaceChange("sucking")
                ". . ."
                $ Speed = 0
                $ Girl.Spunk.append("mouth")
                $ Girl.Spunk.append("chin")
                if not renpy.showing(Girl.Tag+"_BJ_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                    "Она улыбается и обхватывает губами только головку. Когда вы закончиваете наполнять ее рот, она быстро все проглотывает и утирает губы."
                else:
                    "Она что-то мычит, но не прекращает сосать. Когда вы заканчиваете наполнять ее рот, она быстро все проглатывает и утирает губы."
                $ Girl.FaceChange("sexy")
                $ Girl.Mouth = "smile"
                call Sex_Basic_Dialog(Girl,"swallowgood") #"That was real sweet, [Girl.Petname], thanks for the heads up."
                call Sex_Basic_Dialog(Girl,"warned") #"That was real sweet, [Girl.Petname], thanks for the heads up."
                jump Girl_Swallowed
        #End Hungry take-over

        if Trigger == "sex" and Girl.CreamP >= 5:
                # She's Creampied a few times
                $ Girl.FaceChange("sexy")
                $ Player.Cock = "in"
                $ Girl.Spunk.append("in")
                $ Player.Spunk = "in"
                $ Speed = 0
                "Она улыбается и ускоряет свои движения, заставляя вас кончить внутрь нее."
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                jump Girl_Creampied

        elif Trigger == "sex" and Girl.CreamP and D20 >= 10:
                # She's Creampied at least once
                $ Girl.FaceChange("sexy")
                $ Player.Cock = "in"
                $ Girl.Spunk.append("in")
                $ Player.Spunk = "in"
                $ Speed = 0
                "Ее глаза загораются и она ускоряется, из-за чего вы почти сразу кончаете в нее."
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                jump Girl_Creampied

        elif Trigger == "anal" and Girl.CreamA >= 5:
                # She's Anal Creampied a few times
                $ Girl.FaceChange("sexy")
                $ Player.Cock = "anal"
                $ Girl.Spunk.append("anal")
                $ Player.Spunk = "anal"
                $ Speed = 0
                "Она улыбается и ускоряет свои движения, заставляя вас кончить внутрь нее."
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                jump Girl_Creampied

        elif Trigger == "anal" and Girl.CreamA and D20 >= 10:
                # She's Anal Creampied at least once
                $ Girl.FaceChange("sexy")
                $ Player.Cock = "anal"
                $ Girl.Spunk.append("anal")
                $ Player.Spunk = "anal"
                $ Speed = 0
                "Ее глаза загораются и она ускоряется, из-за чего вы почти сразу кончаете в нее."
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                jump Girl_Creampied

        elif Trigger != "anal" and Girl.Swallow >= 5:
                #If she's swallowed a lot
                if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                        $ Girl.FaceChange("sucking")
                        $ Girl.Spunk.append("mouth")
                        "Она что-то мычит, но не прекращает сосать."
                else:
                        if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                            call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                            $ Speed = 2
                        $ Girl.FaceChange("sucking")
                        $ Girl.Spunk.append("mouth")
                        "Она улыбается, а затем берет головку члена в рот."
                $ Girl.Spunk.append("chin")
                "Когда вы заканчиваете наполнять ее рот, она быстро все проглатывает и утирает губы."
                $ Speed = 0
                $ Girl.FaceChange("sexy")
                $ Girl.Mouth = "smile"
                call Sex_Basic_Dialog(Girl,"swallowgood") #"That was real sweet, [Girl.Petname], thanks for the heads up."
                call Sex_Basic_Dialog(Girl,"warned") #"That was real sweet, [Girl.Petname], thanks for the heads up."
                jump Girl_Swallowed

        elif Girl.Swallow and D20 >= 10:
                #She's swallowed before, but not a lot
                if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                    call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                    "Она усмехается, подается назад со звонким 'чпоком', а затем начинает с усердием вам дрочить."
                $ Speed = 2
                if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                        #if she's blowing
                        $ Girl.FaceChange("sucking")
                        $ Girl.Spunk.append("mouth")
                        "Она что-то мычит, но не прекращает сосать."
                        "Когда вы заканчиваете заполнять ее рот, у нее срабатывает рвотный рефлекс, но все же ей удается все проглотить."
                        $ Speed = 0
                        $ Girl.FaceChange("sexy")
                        $ Girl.Mouth = "smile"
                        $ Girl.Spunk.append("chin")
                        if Girl.Addict > 50:
                                $ Girl.Eyes = "manic"
                                "Она жадно все проглатывает, а затем облизывает свои губы."
                        $ Girl.FaceChange("bemused")
                        call Sex_Basic_Dialog(Girl,"swallow2") #"I'm still starting to get used to that, thanks for the heads up."
                        call Sex_Basic_Dialog(Girl,"warned") #"I'm still starting to get used to that, thanks for the heads up."
                        jump Girl_Swallowed
                        #fix, add titjob option here.
                else:
                        #If she's handying
                        jump Girl_Handy_Finish
        #end if she's swallowed

        elif ApprovalCheck(Girl, 1000):
                #warned but likes you and experienced
                if Girl.SEXP > 20 and (renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite")): #renpy.showing("Rogue_Doggy"):
                        "Она мягко отталкивает вас от себя."
                        jump Girl_Cum_Outside
                elif Girl.SEXP > 20:
                        jump Girl_Facial

                if renpy.showing(Girl.Tag+"_HJ_Animation") and Girl.Hand:
                        jump Girl_Handy_Finish
                elif (renpy.showing(Girl.Tag+"_BJ_Animation") or renpy.showing(Girl.Tag+"_69_Animation")) and Girl.Blow:
                        jump Girl_Handy_Finish
                elif renpy.showing(Girl.Tag+"_TJ_Animation") and Girl.Tit:
                        jump Girl_Facial
                elif (renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite")) and Girl.Sex and Trigger == "sex":
                        "Она мягко отталкивает вас от себя."
                        jump Girl_Cum_Outside
                elif (renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite")) and Girl.Anal and Trigger == "anal":
                        "Она мягко отталкивает вас от себя."
                        jump Girl_Cum_Outside


        # Else. . . not experienced or she's not a huge fan,
        if renpy.showing(Girl.Tag+"_BJ_Animation") or renpy.showing(Girl.Tag+"_69_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                jump Girl_In_Mouth
        elif Trigger == "sex" or Trigger == "anal":
                call expression Girl.Tag+"_Doggy_Reset"
                call expression Girl.Tag+"_Sex_Reset"
                "Она отрывается от вас и берет рукой ваш член."
                jump Girl_Handy_Finish
        elif renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):#hotdogging
                "Она улыбается и начинает тереться о вас немного быстрее."
                jump Girl_Cum_Outside
        jump Girl_Facial
    #End "Warn her" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Warn her start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Warn_Her_Female:  #rkeljsvg
        "Вы даете ей знать, что собираетесь кончить."
        $ Girl.Statup("Love", 90, 3,Alt=[[JeanX],900,5]) #+5 for Jean
        if Girl.Obed >= 500:
                $ Girl.Statup("Obed", 80, 5)
        if ("hungry" in Girl.Traits and D20 >= 5):# or Girl == JubesX:
                if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                    call expression Girl.Tag+"_CUN_Launch" pass ("cum")
                    "Она улыбается, отстраняется и начинает лизать вашу киску."
                $ Speed = 2
                $ Girl.FaceChange("sucking")
                ". . ."
                $ Girl.Spunk.append("mouth")
                $ Girl.Spunk.append("chin")
                if not renpy.showing(Girl.Tag+"_CUN_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                    $ Speed = 0
                    "Она улыбается, а затем обхватывает губами вашу киску. Когда вы заканчиваете наполнять ее рот, она быстро все проглатывает и утирает губы."
                else:
                    $ Speed = 4
                    "Она издает легкий стон, не прекращая сосать вашу киску. Когда вы заканчиваете наполнять ее рот, она быстро все проглатывает и утирает губы."
                $ Girl.FaceChange("sexy")
                $ Girl.Mouth = "smile"
                call Sex_Basic_Dialog(Girl,"swallowgood") #"That was real sweet, [Girl.Petname], thanks for the heads up."
                call Sex_Basic_Dialog(Girl,"warned") #"That was real sweet, [Girl.Petname], thanks for the heads up."
                jump Girl_Swallowed
        #End Hungry take-over

        if Trigger == "sex" or Trigger == "anal":
                # She's Creampied a few times
                $ Girl.FaceChange("sexy")
                $ Speed = 0
                "Она улыбается и ускоряет свои движения, заставляя вас обильно кончить на нее."
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                jump Girl_Creampied

        elif Girl.Swallow >= 5:
                #If she's swallowed a lot
                if renpy.showing(Girl.Tag+"_CUN_Animation") or renpy.showing(Girl.Tag+"_69_CUN"): #if renpy.showing("Rogue_BJ_Animation"):
                        $ Girl.FaceChange("sucking")
                        $ Girl.Spunk.append("mouth")
                        "Она что-то мычит, но не прекращает сосать."
                else:
                        if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                            call expression Girl.Tag+"_CUN_Launch" pass ("cum")
                            $ Speed = 4
                        $ Girl.FaceChange("sucking")
                        $ Girl.Spunk.append("mouth")
                        "Она улыбается, а затем обхватывает губами вашу киску."
                $ Girl.Spunk.append("chin")
                "Когда вы заканчиваете наполнять ее рот, она быстро все проглатывает и утирает губы."
                $ Speed = 0
                $ Girl.FaceChange("sexy")
                $ Girl.Mouth = "smile"
                call Sex_Basic_Dialog(Girl,"swallowgood") #"That was real sweet, [Girl.Petname], thanks for the heads up."
                call Sex_Basic_Dialog(Girl,"warned") #"That was real sweet, [Girl.Petname], thanks for the heads up."
                jump Girl_Swallowed

        elif Girl.Swallow and D20 >= 10:
                #She's swallowed before, but not a lot
                if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                    call expression Girl.Tag+"_Finger_Launch" pass ("cum")
                    "Она ухмыляется и начинает ласкать вашу киску."
                $ Speed = 2
                if renpy.showing(Girl.Tag+"_CUN_Animation") or renpy.showing(Girl.Tag+"_69_Cun"): #if renpy.showing("Rogue_BJ_Animation"):
                        #if she's blowing
                        $ Girl.FaceChange("sucking")
                        $ Girl.Spunk.append("mouth")
                        "Она что-то мычит, но не прекращает сосать."
                        "Когда вы заканчиваете заполнять ее рот, у нее срабатывает рвотный рефлекс, но все же ей удается все проглотить."
                        $ Speed = 0
                        $ Girl.FaceChange("sexy")
                        $ Girl.Mouth = "smile"
                        $ Girl.Spunk.append("chin")
                        if Girl.Addict > 50:
                                $ Girl.Eyes = "manic"
                                "Она жадно все проглатывает, а затем облизывает свои губы."
                        $ Girl.FaceChange("bemused")
                        call Sex_Basic_Dialog(Girl,"swallow2") #"I'm still starting to get used to that, thanks for the heads up."
                        call Sex_Basic_Dialog(Girl,"warned") #"I'm still starting to get used to that, thanks for the heads up."
                        jump Girl_Swallowed
                        #fix, add titjob option here.
                else:
                        #If she's handying
                        jump Girl_Handy_Finish
        #end if she's swallowed

        elif ApprovalCheck(Girl, 1000):
                #warned but likes you and experienced
                if Girl.SEXP > 20 and (renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite")): #renpy.showing("Rogue_Doggy"):
                        "Она мягко отталкивает вас от себя."
                        jump Girl_Cum_Outside
                elif Girl.SEXP > 20:
                        jump Girl_Facial

                elif renpy.showing(Girl.Tag+"_Finger_Animation"):
                        $ Girl.Spunk.append("hand")
                        "Вы позволяете ей продолжить, когда оргазм накатывает на вас, вы кончаете ей на руку."
                elif renpy.showing(Girl.Tag+"_CUN_Animation") or renpy.showing(Girl.Tag+"_69_CUN"):
                        jump Girl_In_Mouth_Female
                elif renpy.showing(Girl.Tag+"_BJ_Animation"):
                        jump Girl_In_Mouth_Female
                elif renpy.showing(Girl.Tag+"_TJ_Animation"):
                        $ Girl.Spunk.append("belly")
                        "Вы продолжаете ласкать ее грудь, когда оргазм накатывает на вас, вы кончаете ей на животик."
                elif renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"):
                        "Вы продолжаете входить в нее, но это длиться недолго, скоро оргазм заключает вас в свои объятия."
                jump Girl_Orgasm_After


        # Else. . . not experienced or she's not a huge fan,
        if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                jump Girl_In_Mouth
        elif Trigger == "sex" or Trigger == "anal":
                call expression Girl.Tag+"_Doggy_Reset"
                call expression Girl.Tag+"_Sex_Reset"
                "Она отстраняется от вас и начинает ласкать вашу киску."
                jump Girl_Handy_Finish
        elif renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):#hotdogging
                "Она улыбается и начинает тереться о вас немного быстрее."
                jump Girl_Cum_Outside
        jump Girl_Facial
    #End "Warn her" female / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Cum in mouth start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_In_Mouth: #rkeljsvg
    if Trigger == "anal":
            $ Tempmod -= 15
    if "hungry" not in Girl.Traits and Girl.Addict <= 50 and "full" in Girl.RecentActions:
            $ Tempmod -= 15

#    if renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
#                call expression Girl.Tag + "_Kissing_Launch" pass (Trigger,0)
    $ Player.Cock = "out"
    if Situation == "auto" or Situation == "warn":
                if not renpy.showing(Girl.Tag+"_BJ_Animation") or renpy.showing(Girl.Tag+"_69_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                        call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                $ Speed = 2
                if Situation == "warn":
                    "Вы кончаете в ее ротик, похоже, она не знает, что с этим делать."
                else:
                    "Вы хватаете ее за голову и наполняете ее ротик"
                $ Girl.Eyes = "closed"
                call Punch
                $ Player.Spunk = 1
                if "full" in Girl.RecentActions:
                        #if she's had enough
                        $ Girl.FaceChange("bemused")
                        $ Girl.Spunk.append("mouth")
                        $ Speed = 0
                        $ Girl.Spunk.append("chin")
                        "У нее срабатывает рвотный рефлекс, но все таки ей удается все проглотить."
                        $ Girl.Spunk.remove("mouth")
                        if Girl is RogueX:
                                ch_r "Эм, я. . . Думаю, пока с меня хватит, может мы могли бы. . ."
                                ch_r ". . . вставить его в другое место?"
                        elif Girl is KittyX:
                                ch_k "У меня тут[Girl.like]уже все заполнено. . ."
                                ch_k ". . . может засунем его куда-нибудь в другое место?"
                        elif Girl is EmmaX:
                                ch_e "Хмм. . . еще немного и будет перебор. . ."
                                ch_e "Возможно, нам стоит выбрать другое место, куда ты. . . можешь кончить. . ."
                        elif Girl is LauraX:
                                ch_l "Хмм. . . Я полностью заполнена. . ."
                                ch_l "Кончи в другое место. . ."
                        elif Girl is JeanX:
                                ch_j "Я уже переполнена."
                        elif Girl is StormX:
                                ch_s "Боюсь, что сейчас я уже достаточно заполнена. . ."
                        elif Girl is JubesX:
                                ch_v "Я, эм. . . Я думаю, что объелась. . ."
                        elif Girl is GwenX:
                                ch_g "Знаешь. . . думаю, у меня не особо объемный живот. . ."
                        elif Girl is BetsyX:
                                ch_b "Ох, дорогуша. . . Боюсь, я больше не могу принять. ."
                        elif Girl is DoreenX:
                                ch_d "Думаю, я уже объелась. . ."
                        elif Girl is WandaX:
                                ch_w "Ого, эм. . . Кажется, я уже наелась. . ."
                elif Girl.Swallow >= 5 or "hungry" in Girl.Traits:
                        #if she likes to swallow
                        $ Girl.FaceChange("sexy")
                        $ Girl.Mouth = "smile"
                        $ Girl.Spunk.append("mouth")
                        $ Girl.Spunk.append("chin")
                        "Она быстро все проглатывает и утирает рот."
                        $ Girl.Spunk.remove("mouth")
                        $ Speed = 0
                        call Sex_Basic_Dialog(Girl,"swallowgood") # "That was real sweet, [Girl.Petname]."
                        $ Girl.FaceChange()
                elif Girl.Swallow:
                        $ Girl.FaceChange("bemused")
                        $ Girl.Spunk.append("mouth")
                        $ Girl.Spunk.append("chin")
                        $ Speed = 0
                        "У нее срабатывает рвотный рефлекс, но все таки ей удается все проглотить."
                        $ Girl.Spunk.remove("mouth")
                        call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that"
                        if Situation != "warn":
                                call Sex_Basic_Dialog(Girl,"notwarned") #" warn me next time?"
                        $ Girl.FaceChange()
                elif Girl.Addict >= 50 and Girl.Inbt < 400 and Girl.Blow < 10 and Girl != JubesX:
                        $ Girl.FaceChange("bemused", 1)
                        $ Girl.Spunk.append("mouth")
                        call AnyLine(Girl,". . .")
                        $ Girl.Spunk.remove("mouth")
                        $ Girl.Spunk.append("chin")
                        $ Girl.Spunk.append("hand")
                        $ Speed = 0
                        "Она давится и сплевывает все на ладонь. Затем облизывает губы, смотрит на свою мокрую руку, краснеет и быстро вытирает ее."
                        $ Girl.Spunk.remove("hand")
                        if Girl is RogueX:
                                ch_r "Мне. . . не очень нравится этот вкус."
                        elif Girl is KittyX:
                                ch_k "Мне не нравится этот вкус."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Их, определенно, очень. . . много. . ."
                                else:
                                    ch_e "Ее, определенно, очень. . . много. . ."
                        elif Girl is LauraX:
                                if not Player.Male:
                                    ch_l "Их очень. . . много. . ."
                                else:
                                    ch_l "Ее очень. . . много. . ."
                        elif Girl is JeanX:
                                ch_j "Что-то новенькое. . ."
                        elif Girl is StormX:
                                ch_s "Необычный вкус. . ."
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Они, эм. . .  странная. . ."
                                else:
                                    ch_g "Она, эм. . .  странная. . ."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "Что ж, у них, безусловно. . . уникальный вкус. . ."
                                else:
                                    ch_b "Что ж, у нее, безусловно. . . уникальный вкус. . ."
                        elif Girl is DoreenX:
                                ch_d "Честно говоря. . . это был интересный опыт. . ."
                        elif Girl is WandaX:
                                ch_w "Эм, а неплохо. . . правда. . ."
                        #elif Girl is JubesX:
                        $ Girl.Addictionrate += 1
                        if "addictive" in Player.Traits:
                            $ Girl.Addictionrate += 1
                        $ Girl.FaceChange()
                        jump Girl_Orgasm_After
                elif (Girl.Addict >= 50 and Situation != "warn") or Girl is JubesX:
                        $ Girl.FaceChange("sexy")
                        $ Girl.Mouth = "tongue"
                        $ Girl.Spunk.append("mouth")
                        call AnyLine(Girl,". . .")
                        $ Girl.Spunk.remove("mouth")
                        $ Girl.Spunk.append("chin")
                        $ Girl.Spunk.append("hand")
                        $ Speed = 0
                        "Она давится и сплевывает все на ладонь. Потом облизывает губы, смотрит вниз и выпивает то, что у нее на ладоне."
                        $ Girl.Spunk.remove("hand")
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Хотела бы я на тебя разозлиться, но ты такая приятная на вкус, [Girl.Petname]."
                                else:
                                    ch_r "Хотела бы я на тебя разозлиться, но ты такой приятный на вкус, [Girl.Petname]."
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Ты могла бы и предупредить меня."
                                else:
                                    ch_k "Ты мог бы и предупредить меня."
                        elif Girl is EmmaX:
                                ch_e "Я не должна поощрять такое грубое поведение. . . но это было питательно."
                        elif Girl is LauraX:
                                ch_l "Я должна бы разозлиться, но. . ."
                        elif Girl is JeanX:
                                ch_j "Что-то новенькое. . ."
                        elif Girl is StormX:
                                ch_s "Необычный вкус. . ."
                        elif Girl is JubesX:
                                $ Girl.Eyes = "closed"
                                ch_v "Ммммммм. . ."
                                $ Girl.Eyes = "surprised"
                                if not Player.Male:
                                    ch_v "Ого! . . они. . . невероятные. . ."
                                else:
                                    ch_v "Ого! . . она. . . невероятная. . ."
                                $ Girl.Eyes = "squint"
                                ch_v "Ладно. . ."
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Эм, знаешь, ты могла бы и предупредить меня!"
                                    ch_g ". . . но они мне понравились. . ."
                                else:
                                    ch_g "Эм, знаешь, ты мог бы и предупредить меня!"
                                    ch_g ". . . но она мне понравилась. . ."
                        elif Girl is BetsyX:
                                ch_b "Можно было и как-нибудь предупредить меня. . ."
                                ch_b "Однако, мне весьма понравилось."
                        elif Girl is DoreenX:
                                ch_d "Это было. . . честно говоря, очень интересно. . ."
                                ch_d "Мне даже понравилось."
                        elif Girl is WandaX:
                                ch_w "Неплохо. . . чувствую легкие \"покалывания\". . ."
                        $ Girl.FaceChange()
                        $ Girl.Statup("Inbt", 30, 2)
                        $ Girl.Statup("Inbt", 50, 2)
                else:
                        #hasn't swallowed before
                        if ApprovalCheck(Girl, 800, "LI") and ApprovalCheck(Girl, 400, "OI"):
                                $ Girl.FaceChange("angry")
                                $ Girl.Spunk.append("mouth")
                        else:
                                $ Girl.FaceChange("bemused")
                                $ Girl.Mouth = "tongue"
                                $ Girl.Spunk.append("mouth")
                        $ Girl.Spunk.append("chin")
                        call AnyLine(Girl,". . .")
                        $ Girl.Spunk.append("hand")
                        $ Speed = 0
                        "Она давится и сплевывает все на ладонь."
                        if Situation != "warn":
                                if Girl is RogueX:
                                        ch_r "Эй, разве я говорила, что ты можешь кончить мне в рот, [Girl.Petname]?"
                                elif Girl is KittyX:
                                        ch_k "Эй[Girl.like]разве я тебе разрешала?"
                                elif Girl is EmmaX:
                                        ch_e "Разве я говорила, что ты можешь кончить мне в рот, [Girl.Petname]?"
                                elif Girl is LauraX:
                                        ch_l "Что за дела? Вот так просто кончаешь мне в рот?"
                                elif Girl is JeanX:
                                        ch_j "Эй! В следующий раз предупреждай!"
                                elif Girl is StormX:
                                        ch_s "[Girl.Petname], неосмотрительно с твоей стороны не предупредить девушку. . ."
                                elif Girl is GwenX:
                                        ch_g "Эй! Предупреждай!"
                                elif Girl is BetsyX:
                                        ch_b "Тебе стоило как-нибудь предупредить меня!"
                                elif Girl is DoreenX:
                                        ch_d "Воу! Нужно же предупреждать!"
                                elif Girl is WandaX:
                                        ch_w "Эй! Стоило предупредить меня!"
                        else:
                                call AnyLine(Girl,"Что-?")
                        menu:
                            extend ""
                            "Извини.":
                                    $ Girl.Statup("Love", 80, 1)
                                    $ Girl.Addictionrate += 1
                                    if "addictive" in Player.Traits:
                                            $ Girl.Addictionrate += 1
                                    $ Girl.FaceChange("smile", 1)
                                    if Situation != "warn":
                                            if Girl is RogueX:
                                                    ch_r "Ах, не помешало бы предупредить, [Girl.Petname]."
                                            elif Girl is KittyX:
                                                    ch_k "Ну, в следующий раз[Girl.like]обязательно предупреди, ладно?"
                                            elif Girl is EmmaX:
                                                    ch_e "Ну хорошо. . ."
                                                    ch_e "Только предупреждай в следующий раз. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Ладно. . ."
                                                    ch_l "Только предупреждай в следующий раз. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Ладно."
                                                    ch_j "Но больше так не делай."
                                            elif Girl is StormX:
                                                    ch_s "Только в следующий раз сделай все лучше. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Только. . . знаешь. . .\"предупреждай перед приходом.\"."
                                                    ch_g "Ну, как-то так. . ."
                                            elif Girl is BetsyX:
                                                    ch_b "Сделанного не воротишь. . ."
                                                    ch_b "Однако, в следующий раз предупреждай."
                                            elif Girl is DoreenX:
                                                    ch_d "Ну, я думаю, все люди совершают ошибки. . ."
                                                    ch_d "Только в следующий раз делай все по уму."
                                            elif Girl is WandaX:
                                                    ch_w "Ага, просто имей это в виду."
                                    else:
                                            call AnyLine(Girl,". . . ладно.")
                                    jump Girl_Orgasm_After
                            # end "sorry"
                            "Почему бы тебе не проглотить все?":
                                    if ApprovalCheck(Girl, 1200):
                                            "Она сперва осторожно лижет ладонь, но затем берет все в рот и проглотывает."
                                            $ Girl.Spunk.remove("hand")
                                            $ Girl.FaceChange("sexy", 1)
                                            $ Girl.Spunk.append("mouth")
                                            $ Girl.Spunk.append("chin")
                                            if Girl is RogueX:
                                                    ch_r "Хмм, я, если честно, думала, будет хуже, [Girl.Petname]."
                                            elif Girl is KittyX:
                                                    ch_k "Хмм. . . такая густая консистенция? . ."
                                            elif Girl is EmmaX:
                                                    ch_e "Хорошо, мне даже немного понравилось. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Не так уж и плохо. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Хммм. . . сильный вкус. . ."
                                            elif Girl is StormX:
                                                    ch_s "Какой. . . необычный вкус. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Ну. . . что-то. . . новенькое."
                                                    ch_g "Пикантно."
                                            elif Girl is BetsyX:
                                                    ch_b "Что ж, вполне неплохо. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Это. . . интересный опыт. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Что ж, весьма недурно. . ."
                                            $ Girl.Statup("Obed", 50, 10,Alt=[[JeanX],900,10]) #+10 for Jean
                                            $ Girl.Spunk.remove("mouth")
                                    elif ApprovalCheck(Girl, 1200, "OI", Bonus = (Girl.Addict*10)):
                                            $ Girl.FaceChange("bemused", 1)
                                            $ Girl.Brows = "normal"
                                            $ Girl.Mouth = "sad"
                                            $ Girl.Spunk.remove("hand")
                                            $ Girl.Spunk.append("mouth")
                                            $ Girl.Spunk.append("chin")
                                            "Она хмурится, но, все же, осторожно лижет ладонь, затем берет все в рот и проглотывает."
                                            $ Girl.Spunk.remove("mouth")
                                            if Girl is RogueX:
                                                    ch_r "Как-то не очень, [Girl.Petname]."
                                            elif Girl is KittyX:
                                                    ch_k "Ну. . . не так уж и противно."
                                            elif Girl is EmmaX:
                                                    ch_e "Не могу сказать, что мне понравилось. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Не мой любимый вкус. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Эх. . . могло быть и хуже."
                                            elif Girl is StormX:
                                                    ch_s "В целом. . . неплохо. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Ну. . . что-то. . . новенькое."
                                            elif Girl is BetsyX:
                                                    ch_b "Что ж, довольно. . . уникальный вкус. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Это. . . интересный опыт. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Не так уж и плохо."
                                            $ Girl.Statup("Obed", 50, 10,Alt=[[JeanX],900,10]) #+10 for Jean
                                    else:
                                            $ Girl.Spunk.remove("hand")
                                            "Она сердито смотрит на вас и вытирает руку. Затем облизывает губы."
                                            jump Girl_Orgasm_After
                            #end "why not swallow"
                            "Глотай, сейчас же.":
                                    $ Girl.Statup("Love", 30, -1, 1)
                                    $ Girl.Statup("Love", 50, -1, 1)
                                    $ Girl.Statup("Love", 80, -1, 1)
                                    if ApprovalCheck(Girl, 1200, "OI") or Girl.Addict >= 50:
                                            $ Girl.FaceChange("sad", 1)
                                            $ Girl.Spunk.append("mouth")
                                            $ Girl.Spunk.append("chin")
                                            $ Girl.Spunk.remove("hand")
                                            "Она хмурится, но, все же, осторожно лижет ладонь, затем берет все в рот и проглотывает."
                                            $ Girl.Spunk.remove("mouth")
                                            if Girl is RogueX:
                                                    ch_r "Как-то не очень, [Girl.Petname]."
                                            elif Girl is KittyX:
                                                    ch_k "Ну. . . не так уж и противно."
                                            elif Girl is EmmaX:
                                                    ch_e "Не могу сказать, что мне понравилось. . ."
                                            elif Girl is LauraX:
                                                    ch_l "Не мой любимый вкус. . ."
                                            elif Girl is JeanX:
                                                    ch_j "Эх. . . могло быть и хуже."
                                            elif Girl is StormX:
                                                    ch_s "В целом. . . неплохо. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Ну. . . что-то. . . новенькое."
                                            elif Girl is BetsyX:
                                                    ch_b "Что ж, довольно. . . уникальный вкус. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Это. . . интересный опыт. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Не так уж и плохо."
                                            $ Girl.Statup("Obed", 50, 10,Alt=[[JeanX],900,10]) #+10 for Jean
                                    else:
                                            $ Girl.Spunk.remove("hand")
                                            "Она сердито смотрит на вас и вытирает руку. Затем облизывает губы."
                                            jump Girl_Orgasm_After

                jump Girl_Swallowed
                #end if not asked/auto / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    $ Situation = 0
    "Вы спрашиваете, можно ли кончить ей в рот."
    if renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                call expression Girl.Tag + "_Kissing_Launch" pass (Trigger,0)
    elif renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
            call expression Girl.Tag+"_HJ_Launch" pass ("cum")

    if "full" in Girl.RecentActions:
            pass

    elif Girl.Swallow >= 5 or "hungry" in Girl.Traits:
            # If she's swallowed 5 times,
            $ Girl.FaceChange("sucking")
            if not renpy.showing(Girl.Tag+"_BJ_Animation") and not renpy.showing(Girl.Tag+"_69_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                $ Speed = 2
                "Она кивает и немного подается назад, оставляя во рту только кончик вашего члена."
            else:
                $ Speed = 2
                "Она кивает и мямлит что-то вроде \"ага\"."
            $ Player.Spunk = 1
            $ Girl.Spunk.append("mouth")
            $ Girl.Spunk.append("chin")
            call AnyLine(Girl,". . .")
            "После того, как вы кончаете, она быстро все проглатывает и утирает рот."
            $ Girl.FaceChange("sexy")
            $ Speed = 0
            call Sex_Basic_Dialog(Girl,"swallowgood") #"That was real sweet, [Girl.Petname], thanks for the heads up."
            $ Girl.Spunk.remove("mouth")
            jump Girl_Swallowed

    elif Girl.Addict >= 80 and Girl.Swallow:
            #addicted
            $ Girl.Brows = "confused"
            $ Girl.Eyes = "manic"
            if not renpy.showing(Girl.Tag+"_BJ_Animation") and not renpy.showing(Girl.Tag+"_69_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                $ Speed = 2
                "Она, с немного озадаченным выражением лица, мягко обхватывает головку вашего члена своими губами, и в ту же секунду вы начинаете кончать."
            else:
                $ Speed = 2
                "Она кивает и мямлит что-то вроде \"ага\"."
            $ Girl.Mouth = "sucking"
            $ Player.Spunk = 1
            $ Girl.Spunk.append("mouth")
            call AnyLine(Girl,". . .")
            $ Speed = 0
            "У нее срабатывает рвотный рефлекс, но затем она быстро все проглатывает."
            $ Girl.FaceChange("sexy")
            $ Girl.Mouth = "smile"
            call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that."
            call Sex_Basic_Dialog(Girl,"notwarned") #"I could use a warning next time. . ."
            $ Girl.Spunk.remove("mouth")
            $ Girl.Statup("Inbt", 200, 5)
            jump Girl_Swallowed

    elif Girl.Swallow:
            if ApprovalCheck(Girl, 900):
                $ Girl.Brows = "confused"
                if renpy.showing(Girl.Tag+"_TJ_Animation"): #if renpy.showing("Rogue_TJ_Animation"):
                    $ Girl.FaceChange("kiss")
                    $ Speed = 5
                    "Похоже, она немного расстроилась, но, все же, осторожно подносит головку вашего члена к своим губам."
                elif not renpy.showing(Girl.Tag+"_BJ_Animation") and not renpy.showing(Girl.Tag+"_69_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
                    call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                    $ Speed = 2
                    "Она, с немного озадаченным выражением лица, мягко обхватывает головку вашего члена своими губами, и в ту же секунду вы начинаете кончать."
                else:
                    $ Speed = 2
                    "Она наклоняет голову и мямлит что-то вроде \"что?\""
                $ Girl.Mouth = "sucking"
                $ Girl.Spunk.append("chin")
                $ Girl.Spunk.append("mouth")
                $ Girl.Brows = "normal"
                $ Girl.Eyes = "sexy"
                $ Player.Spunk = 1
                $ Girl.Spunk.append("mouth")
                call AnyLine(Girl,". . .")
                "У нее срабатывает рвотный рефлекс, но затем она быстро все проглатывает."
                $ Speed = 0
                $ Girl.FaceChange("sexy")
                call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that."
                $ Girl.Spunk.remove("mouth")
                jump Girl_Swallowed

    #If she hasn't swallowed or doesn't automatically want to. . .

    if  ApprovalCheck(Girl, 300, "LI") or ApprovalCheck(Girl, 300, "OI"):
        $ Girl.FaceChange("bemused")
        $ Girl.Eyes = "sexy"
    else:
        $ Girl.FaceChange("angry")

    $ Speed = 0

    if Girl is RogueX:
            if "full" in Girl.RecentActions:
                    ch_r "Сейчас я чувствую себя немного. . . \"полной\", [Girl.Petname]. . ."
            else:
                    ch_r "И что, думаешь, я соглашусь, [Girl.Petname]?"
    elif Girl is KittyX:
            if "full" in Girl.RecentActions:
                    ch_k "Пока с меня, наверное, хватит? . ."
            else:
                    ch_k "Звучит не особо аппетитно. . ."
    elif Girl is EmmaX:
            if "full" in Girl.RecentActions:
                    ch_e "Больше в меня не влезет ни капли, [Girl.Petname]. . ."
            else:
                    ch_e "Не представляю, зачем мне это. . ."
    elif Girl is LauraX:
            if "full" in Girl.RecentActions:
                    ch_l "С меня пока хватит, [Girl.Petname]. . ."
            else:
                    ch_l "Не знаю, с чего мне соглашаться. . ."
    elif Girl is JeanX:
            if "full" in Girl.RecentActions:
                    ch_j "Я немного \"переполнена\", [Girl.Petname]. . ."
            else:
                    ch_j "Как будто есть шанс, что я соглашусь. . ."
    elif Girl is StormX:
            if "full" in Girl.RecentActions:
                    ch_s "Я больше не могу, [Girl.Petname]. . ."
            else:
                    ch_s "Не понимаю, почему я должна согласиться. . ."
    elif Girl is JubesX:
            if "full" in Girl.RecentActions:
                    ch_v "Даже я уже наелась, [Girl.Petname]. . ."
            else:
                    ch_v "Я не думаю, что хотела бы этого. . ."
    elif Girl is GwenX:
            if "full" in Girl.RecentActions:
                    ch_g "Я, эм. . . думаю, с меня хватитw, [Girl.Petname]. . ."
            else:
                    ch_g "Я. . . мне не очень нравится. . . это. . ."
    elif Girl is BetsyX:
            if "full" in Girl.RecentActions:
                    ch_b "Боюсь, мне уже хватит, [Girl.Petname]. . ."
            else:
                    ch_b "Меня. . . в данный момент это не привлекает. . ."
    elif Girl is DoreenX:
            if "full" in Girl.RecentActions:
                    ch_d "Я уже объелась, [Girl.Petname]. . ."
            else:
                    ch_d "Почему я. . . почему ты думаешь, что я этого хочу?"
    elif Girl is WandaX:
            if "full" in Girl.RecentActions:
                    ch_w "Я объелась, [Girl.Petname]. . ."
            else:
                    ch_w "Я. . . не думаю, что хочу этого."
    menu:
        extend ""
        "Извини.":
                $ Girl.Statup("Love", 80, 3)
                $ Girl.Addictionrate += 1
                if "addictive" in Player.Traits:
                        $ Girl.Addictionrate += 1
                $ Girl.FaceChange("smile", 1)
                if Girl is RogueX:
                        if not Player.Male:
                            ch_r "Ну, если они будут такими же приятными, как твои слова, [Girl.Petname]."
                        else:
                            ch_r "Ну, если она будет такой же приятной, как твои слова, [Girl.Petname]."
                elif Girl is KittyX:
                        ch_k "Ну, за спрос же не бьют?"
                elif Girl is EmmaX:
                        ch_e "Может это не такое и плохое предложение. . ."
                elif Girl is LauraX:
                        ch_l "Хмм. . ."
                elif Girl is JeanX:
                        ch_j "Угу. . ."
                elif Girl is StormX:
                        if not Player.Male:
                            ch_s "Я рада, что ты сперва спросила. . ."
                        else:
                            ch_s "Я рада, что ты сперва спросил. . ."
                elif Girl is JubesX:
                        if not Player.Male:
                            ch_v "Нууу, ничего страшного, главное, ты спросила. . ."
                        else:
                            ch_v "Нууу, ничего страшного, главное, ты спросил. . ."
                elif Girl is GwenX:
                        if not Player.Male:
                            ch_g "По крайней мере, ты спросила."
                        else:
                            ch_g "По крайней мере, ты спросил."
                elif Girl is BetsyX:
                        if not Player.Male:
                            ch_b "Ну, хотя бы спросила. . ."
                        else:
                            ch_b "Ну, хотя бы спросил. . ."
                elif Girl is DoreenX:
                        if not Player.Male:
                            ch_d "Ну, ты ведь просто спросила. . ."
                        else:
                            ch_d "Ну, ты ведь просто спросил. . ."
                elif Girl is WandaX:
                        if not Player.Male:
                            ch_w "Ну, по крайней мере, ты спросила."
                        else:
                            ch_w "Ну, по крайней мере, ты спросил."
                if ApprovalCheck(Girl, 1200, TabM=1) and "full" not in Girl.RecentActions:
                        $ Girl.Statup("Inbt", 30, 3)
                        $ Girl.Statup("Inbt", 70, 2)
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                ch_r "Может и правда стоит попробовать. . ."
                        elif Girl is KittyX:
                                ch_k "Ну, думаю[Girl.like]стоит попробовать."
                        elif Girl is EmmaX:
                                ch_e "Если только немного. . ."
                        elif Girl is LauraX:
                                ch_l "Ну, может быть, если чуть-чуть. . ."
                        elif Girl is JeanX:
                                ch_j "Думаю, можно. . ."
                        elif Girl is StormX:
                                ch_s "Попробовать можно."
                        elif Girl is JubesX:
                                ch_v "Нууу, почему бы и нет, один раз живем. . ."
                        elif Girl is GwenX:
                                ch_g "Попробовать можно. Ну, до дна!"
                        elif Girl is BetsyX:
                                ch_b "Что ж, почему бы и нет. . ."
                        elif Girl is DoreenX:
                                ch_d "Думаю, попробовать не помешает. . ."
                        elif Girl is WandaX:
                                ch_w "Хорошо, почему бы и нет."
                else:
                        jump Girl_Handy_Finish

        "Попробуй, тебе может понравиться." if "full" not in Girl.RecentActions:
                if ApprovalCheck(Girl, 1200, TabM=1):
                        $ Girl.Statup("Obed", 50, 5)
                        $ Girl.Statup("Obed", 70, 3)
                        $ Girl.Brows = "confused"
                        $ Girl.Eyes = "sexy"
                        if Girl is RogueX:
                                ch_r "Ну, если ты так говоришь. . ."
                        elif Girl is KittyX:
                                ch_k "Может ты и прав. . ."
                        elif Girl is EmmaX:
                                ch_e "Если ты настаиваешь. . ."
                        elif Girl is LauraX:
                                ch_l "Если ты настаиваешь. . ."
                        elif Girl is JeanX:
                                ch_j "Не проверишь, не узнаешь. . ."
                        elif Girl is StormX:
                                ch_s "Я не уверена. . ."
                        elif Girl is JubesX:
                                ch_v "Я, эм. . . Возможно? . ."
                        elif Girl is GwenX:
                                ch_g "А ты хорош в \"переговорах\"."
                        elif Girl is BetsyX:
                                ch_b "Пожалуй, можно. . ."
                        elif Girl is DoreenX:
                                ch_d "Наверное, можно. . ."
                        elif Girl is WandaX:
                                ch_w "Пожалуй, можно. . ."
                else:
                        $ Girl.Addictionrate += 1
                        if "addictive" in Player.Traits:
                            $ Girl.Addictionrate += 1
                        $ Girl.Blush = 1
                        if Girl is RogueX:
                                ch_r "Если ты этого хочешь, еще не значит, что этого хочу и я, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k "Если ты этого хочешь, еще не значит, что этого хочу и я, [Girl.Petname]."
                        elif Girl is EmmaX:
                                ch_e "Я очень в этом сомневаюсь, [Girl.Petname]."
                        elif Girl is LauraX:
                                ch_l "Ты думаешь, у меня нет носа, [Girl.Petname]?"
                        elif Girl is JeanX:
                                ch_j "Ага, такого я еще не слышала. . ."
                        elif Girl is StormX:
                                ch_s "Это. . . маловероятно. . ."
                        elif Girl is JubesX:
                                ch_v "Я, эм. . . немного сомневаюсь в этом. . ."
                        elif Girl is GwenX:
                                ch_g "А ты хорош в \"переговорах\"."
                        elif Girl is BetsyX:
                                ch_b "Я очень в этом сомневаюсь. . ."
                        elif Girl is DoreenX:
                                ch_d "Я так не думаю. . ."
                        elif Girl is WandaX:
                                ch_w "Я в этом сомневаюсь. . ."
                        jump Girl_Handy_Finish

        "Я серьезно, бери его в рот.":
                if ApprovalCheck(Girl, 1500, "LI", TabM=1) or ApprovalCheck(Girl, 1200, "OI", TabM=1):
                        $ Girl.FaceChange("sucking", 1)
                elif ApprovalCheck(Girl, 1000, "OI", Bonus = (Girl.Addict*10)): #Mild addiction included
                        $ Girl.FaceChange("angry", 1)
                else:
                        #You insisted, she refused.
                        $ Girl.FaceChange("angry", 1)
                        "Она сердито смотрит на вас, отпускает ваш член и отстраняется."
                        call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                        call expression Girl.Tag+"_HJ_Reset"
                        $ Girl.Statup("Love", 50, -3, 1)
                        $ Girl.Statup("Love", 80, -4, 1)
                        if Girl is RogueX:
                                ch_r "С таким отношением справляйся сам."
                        elif Girl is KittyX:
                                ch_k "Справляйся тогда без меня."
                        elif Girl is EmmaX:
                                ch_e "Мне кажется, ты переоцениваешь свое обаяние."
                        elif Girl is LauraX:
                                ch_l "Я тоже серьезно, наверни говна."
                        elif Girl is JeanX:
                                ch_j "Иди нахуй, пес."
                        elif Girl is StormX:
                                ch_s "Нет."
                        elif Girl is JubesX:
                                ch_v "Мне это не нужно. . ."
                        elif Girl is GwenX:
                                ch_g "А ты -очень- хорош в \"переговорах\"."
                        elif Girl is BetsyX:
                                ch_b "Такое отношение не принесет тебе никакой пользы. . ."
                        elif Girl is DoreenX:
                                ch_d "Ни за что, приятель!"
                        elif Girl is WandaX:
                                ch_w "Хех, нет, спасибо."
                        $ Girl.Statup("Obed", 30, -1, 1,Alt=[[JeanX],900,3]) #+3 for Jean
                        $ Girl.Statup("Obed", 50, -1, 1)
                        $ Girl.RecentActions.append("angry")
                        $ Girl.DailyActions.append("angry")
                        $ Line = 0
                        return
                $ Girl.Statup("Obed", 50, 10,Alt=[[JeanX],900,10]) #+10 for Jean
                $ Girl.Statup("Obed", 70, 5)

    if not renpy.showing(Girl.Tag+"_BJ_Animation") and not renpy.showing(Girl.Tag+"_69_Animation"): #if not renpy.showing("Rogue_BJ_Animation"):
        call expression Girl.Tag+"_BJ_Launch" pass ("cum")
    $ Speed = 2
    if ApprovalCheck(Girl, 1200):
            "Она нежно подносит ваш член к губам, а затем начинает его посасывать."
    else:
            "Она осторожно берет член в рот, и вы сразу кончаете внутрь него."
            $ Girl.FaceChange("sexy")
            $ Girl.Statup("Love", 50, -3, 1)
            $ Girl.Statup("Love", 80, -4, 1)
    $ Girl.Mouth = "sucking"
    $ Player.Spunk = 1
    $ Girl.Spunk.append("chin")
    $ Girl.Spunk.append("mouth")
    call AnyLine(Girl,". . .")
    "У нее срабатывает рвотный рефлекс, но затем она быстро все проглатывает."
    $ Speed = 0
    $ Girl.FaceChange("sexy")

    if ApprovalCheck(Girl, 1000) and Girl.Swallow >= 3:
            call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that."
    elif ApprovalCheck(Girl, 800):
            call Sex_Basic_Dialog(Girl,"swallowfirst") #"I'm not really a fan of that, [Girl.Petname]."
    else:
            $ Girl.FaceChange("sad")
            call Sex_Basic_Dialog(Girl,"swallowfirst") #"I'm not really a fan of that, [Girl.Petname]."
    $ Girl.Statup("Inbt", 30, 3)
    $ Girl.Statup("Inbt", 50, 2)
    $ Girl.Blow += 1
    jump Girl_Swallowed
    #end Cum in mouth  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Cum in mouth start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_In_Mouth_Female: #rkeljsvg
    if "hungry" not in Girl.Traits and Girl.Addict <= 50 and "full" in Girl.RecentActions:
            $ Tempmod -= 15

#    if renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
#                call expression Girl.Tag + "_Kissing_Launch" pass (Trigger,0)
    $ Player.Cock = "out"
    if Situation == "auto" or Situation == "warn":
                if not renpy.showing(Girl.Tag+"_CUN_Animation") and not renpy.showing(Girl.Tag+"_69_CUN"): #if not renpy.showing("Rogue_BJ_Animation"):
                        call expression Girl.Tag+"_CUN_Launch" pass ("cum")
                $ Speed = 2
                if Situation == "warn":
                    "Вы кончаете в ее ротик, похоже, она не знает, что с этим делать."
                else:
                    "Вы хватаете ее за голову и наполняете ее ротик"
                $ Girl.Eyes = "closed"
                call Punch
                $ Player.Spunk = 1
                if Girl.Swallow >= 5 or "hungry" in Girl.Traits:
                        #if she likes to swallow
                        $ Girl.FaceChange("sexy")
                        $ Girl.Mouth = "smile"
                        $ Girl.Spunk.append("mouth")
                        $ Girl.Spunk.append("chin")
                        "Она быстро все проглатывает и утирает рот."
                        $ Girl.Spunk.remove("mouth")
                        $ Speed = 0
                        call Sex_Basic_Dialog(Girl,"swallowgood") # "That was real sweet, [Girl.Petname]."
                        $ Girl.FaceChange()
                elif Girl.Swallow:
                        $ Girl.FaceChange("bemused")
                        $ Girl.Spunk.append("mouth")
                        $ Girl.Spunk.append("chin")
                        $ Speed = 0
                        "У нее срабатывает рвотный рефлекс, но все таки ей удается все проглотить."
                        $ Girl.Spunk.remove("mouth")
                        call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that"
                        if Situation != "warn":
                                call Sex_Basic_Dialog(Girl,"notwarned") #" warn me next time?"
                        $ Girl.FaceChange()
                else:
                        $ Girl.FaceChange("bemused", 1)
                        $ Girl.Spunk.append("mouth")
                        call AnyLine(Girl,". . .")
                        $ Girl.Spunk.remove("mouth")
                        $ Girl.Spunk.append("chin")
                        $ Girl.Spunk.append("hand")
                        $ Speed = 0
                        "Она давится и утирает рот ладонью. Затем она облизывает губы, смотрит на свою мокрую руку, краснеет и быстро вытирает ее."
                        $ Girl.Spunk.remove("hand")
                        if Girl is RogueX:
                                ch_r "Мне. . . мне не очень понравился этот вкус."
                        elif Girl is KittyX:
                                ch_k "Этот вкус не по мне."
                        elif Girl is EmmaX:
                                ch_e "Какой. . . богатый вкус. . ."
                        elif Girl is LauraX:
                                ch_l "Их очень. . . много. . ."
                        elif Girl is JeanX:
                                ch_j "Что-то новенькое. . ."
                        elif Girl is StormX:
                                ch_s "Необычный вкус. . ."
                        elif Girl is GwenX:
                                ch_g "Ну. . . это что-то. . . новенькое."
                        elif Girl is BetsyX:
                                ch_b "Что ж, у тебя. . . уникальный вкус. . ."
                        elif Girl is DoreenX:
                                ch_d "Это. . . был интересный опыт. . ."
                        elif Girl is WandaX:
                                ch_w "Что ж, весьма недурно. . ."
                        #elif Girl is JubesX:
                        $ Girl.Addictionrate += 1
                        if "addictive" in Player.Traits:
                            $ Girl.Addictionrate += 1
                        $ Girl.FaceChange()
                        jump Girl_Orgasm_After

                jump Girl_Swallowed
                #end if not asked/auto / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    $ Situation = 0
    "Вы спрашиваете, может ли она вам отлизать."
    if renpy.showing(Girl.Tag+"_TJ_Animation"): #if renpy.showing("Rogue_TJ_Animation"):
                call Girl_Kissing_Launch(Girl,Trigger,0) #call expression Girl.Tag + "_Kissing_Launch" pass (Trigger,0)
    elif renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                call expression Girl.Tag+"_Finger_Launch" pass ("cum")

    if "full" in Girl.RecentActions:
            pass

    elif Girl.Swallow >= 5 or "hungry" in Girl.Traits:
            # If she's swallowed 5 times,
            $ Girl.FaceChange("sucking")
            if not renpy.showing(Girl.Tag+"_CUN_Animation") and not renpy.showing(Girl.Tag+"_69_CUN"): #if not renpy.showing("Rogue_BJ_Animation"):
                call expression Girl.Tag+"_CUN_Launch" pass ("cum")
                $ Speed = 2
                "Она кивает и обхватывает губами вашу киску."
            else:
                $ Speed = 2
                "Она кивает и мямлит что-то вроде \"ага\"."
            $ Player.Spunk = 1
            $ Girl.Spunk.append("mouth")
            $ Girl.Spunk.append("chin")
            call AnyLine(Girl,". . .")
            "Когда вы кончаете, она быстро все проглатывает и утирает рот."
            $ Girl.FaceChange("sexy")
            $ Speed = 0
            call Sex_Basic_Dialog(Girl,"swallowgood") #"That was real sweet, [Girl.Petname], thanks for the heads up."
            $ Girl.Spunk.remove("mouth")
            jump Girl_Swallowed

    elif Girl.Addict >= 80 and Girl.Swallow:
            #addicted
            $ Girl.Brows = "confused"
            $ Girl.Eyes = "manic"
            if not renpy.showing(Girl.Tag+"_CUN_Animation") and not renpy.showing(Girl.Tag+"_69_CUN"): #if not renpy.showing("Rogue_BJ_Animation"):
                call expression Girl.Tag+"_CUN_Launch" pass ("cum")
                $ Speed = 2
                "Она, с немного озадаченным выражением лица, мягко прижимается губками к вашей киске, и в ту же секунду вы начинаете кончать."
            else:
                $ Speed = 2
                "Она кивает и мямлит что-то вроде \"ага\"."
            $ Girl.Mouth = "sucking"
            $ Player.Spunk = 1
            $ Girl.Spunk.append("mouth")
            call AnyLine(Girl,". . .")
            $ Speed = 0
            "У нее срабатывает рвотный рефлекс, но затем она быстро все проглатывает."
            $ Girl.FaceChange("sexy")
            $ Girl.Mouth = "smile"
            call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that."
            call Sex_Basic_Dialog(Girl,"notwarned") #"I could use a warning next time. . ."
            $ Girl.Spunk.remove("mouth")
            $ Girl.Statup("Inbt", 200, 5)
            jump Girl_Swallowed

    elif Girl.Swallow:
            if ApprovalCheck(Girl, 900):
                $ Girl.Brows = "confused"
                if renpy.showing(Girl.Tag+"_TJ_Animation"): #if renpy.showing("Rogue_TJ_Animation"):
                    $ Girl.FaceChange("kiss")
                    $ Speed = 5
                    "Похоже, она немного расстроилась, но, все же, нежно прижимается губками к вашей киске."
                elif not renpy.showing(Girl.Tag+"_CUN_Animation") and not renpy.showing(Girl.Tag+"_69_CUN"): #if not renpy.showing("Rogue_BJ_Animation"):
                    call expression Girl.Tag+"_CUN_Launch" pass ("cum")
                    $ Speed = 2
                    "Она, с немного озадаченным выражением лица, мягко прижимается губками к вашей киске, и в ту же секунду вы начинаете кончать."
                else:
                    $ Speed = 2
                    "Она наклоняет голову и мямлит что-то вроде \"что?\""
                $ Girl.Mouth = "sucking"
                $ Girl.Spunk.append("chin")
                $ Girl.Spunk.append("mouth")
                $ Girl.Brows = "normal"
                $ Girl.Eyes = "sexy"
                $ Player.Spunk = 1
                $ Girl.Spunk.append("mouth")
                call AnyLine(Girl,". . .")
                "У нее срабатывает рвотный рефлекс, но затем она быстро все проглатывает."
                $ Speed = 0
                $ Girl.FaceChange("sexy")
                call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that."
                $ Girl.Spunk.remove("mouth")
                jump Girl_Swallowed

    #If she hasn't swallowed or doesn't automatically want to. . .

    if  ApprovalCheck(Girl, 300, "LI") or ApprovalCheck(Girl, 300, "OI"):
        $ Girl.FaceChange("bemused")
        $ Girl.Eyes = "sexy"
    else:
        $ Girl.FaceChange("angry")

    $ Speed = 0

    if Girl is RogueX:
            ch_r "С чего ты взяла, что я этого хочу, [Girl.Petname]?"
    elif Girl is KittyX:
            ch_k "Звучит не слишком аппетитно. . ."
    elif Girl is EmmaX:
            ch_e "Не могу себе представить, зачем мне это нужно. . ."
    elif Girl is LauraX:
            ch_l "Я не знаю, почему я должна согласиться. . ."
    elif Girl is JeanX:
            ch_j "Ну да, этого хочешь ты, но не я. . ."
    elif Girl is StormX:
            ch_s "Я не понимаю, зачем мне это делать. . ."
    elif Girl is JubesX:
            ch_v "Я не думаю, что мне бы этого хотелось. . ."
    elif Girl is GwenX:
            ch_g "Мне. . . мне не очень хочется. . . это делать. . ."
    elif Girl is BetsyX:
            ch_b "Меня. . . это не особо привлекает. . ."
    elif Girl is DoreenX:
            ch_d "Почему я. . . почему ты думаешь, что я этого хочу?"
    elif Girl is WandaX:
            ch_w "Не думаю, что хочу это делать. . ."
    menu:
        extend ""
        "Пожалуйста?":
                $ Girl.Statup("Love", 80, 3)
                $ Girl.Addictionrate += 1
                if "addictive" in Player.Traits:
                        $ Girl.Addictionrate += 1
                $ Girl.FaceChange("smile", 1)
                if Girl is RogueX:
                        if not Player.Male:
                            ch_r "Ну, если они будут такими же приятными, как твои слова, [Girl.Petname]."
                        else:
                            ch_r "Ну, если она будет такой же приятной, как твои слова, [Girl.Petname]."
                elif Girl is KittyX:
                        ch_k "Ну, за спрос же не бьют?"
                elif Girl is EmmaX:
                        ch_e "Может это не такое и плохое предложение. . ."
                elif Girl is LauraX:
                        ch_l "Хмм. . ."
                elif Girl is JeanX:
                        ch_j "Угу. . ."
                elif Girl is StormX:
                        if not Player.Male:
                            ch_s "Я рада, что ты сперва спросила. . ."
                        else:
                            ch_s "Я рада, что ты сперва спросил. . ."
                elif Girl is JubesX:
                        if not Player.Male:
                            ch_v "Нууу, ничего страшного, главное, ты спросила. . ."
                        else:
                            ch_v "Нууу, ничего страшного, главное, ты спросил. . ."
                elif Girl is GwenX:
                        if not Player.Male:
                            ch_g "По крайней мере, ты спросила."
                        else:
                            ch_g "По крайней мере, ты спросил."
                elif Girl is BetsyX:
                        if not Player.Male:
                            ch_b "Ну, хотя бы спросила. . ."
                        else:
                            ch_b "Ну, хотя бы спросил. . ."
                elif Girl is DoreenX:
                        if not Player.Male:
                            ch_d "Ну, ты ведь просто спросила. . ."
                        else:
                            ch_d "Ну, ты ведь просто спросил. . ."
                elif Girl is WandaX:
                        if not Player.Male:
                            ch_w "По крайней мере, ты спросила."
                        else:
                            ch_w "По крайней мере, ты спросил."
                if ApprovalCheck(Girl, 1200, TabM=1) and "full" not in Girl.RecentActions:
                        $ Girl.Statup("Inbt", 30, 3)
                        $ Girl.Statup("Inbt", 70, 2)
                        $ Girl.FaceChange("sexy", 1)
                        if Girl is RogueX:
                                ch_r "Может и правда стоит попробовать. . ."
                        elif Girl is KittyX:
                                ch_k "Ну, думаю[Girl.like]стоит попробовать."
                        elif Girl is EmmaX:
                                ch_e "Если только немного. . ."
                        elif Girl is LauraX:
                                ch_l "Ну, может быть, если чуть-чуть. . ."
                        elif Girl is JeanX:
                                ch_j "Думаю, можно. . ."
                        elif Girl is StormX:
                                ch_s "Попробовать можно."
                        elif Girl is JubesX:
                                ch_v "Нууу, почему бы и нет, один раз живем. . ."
                        elif Girl is GwenX:
                                ch_g "Попробовать можно. Ну, до дна!"
                        elif Girl is BetsyX:
                                ch_b "Твое здоровье. . ."
                        elif Girl is DoreenX:
                                ch_d "Я думаю, стоит попробовать. . ."
                        elif Girl is WandaX:
                                ch_w "Хорошо, почему бы и нет."
                else:
                        jump Girl_Handy_Finish

        "Попробуй, тебе может понравиться." if "full" not in Girl.RecentActions:
                if ApprovalCheck(Girl, 1200, TabM=1):
                        $ Girl.Statup("Obed", 50, 5)
                        $ Girl.Statup("Obed", 70, 3)
                        $ Girl.Brows = "confused"
                        $ Girl.Eyes = "sexy"
                        if Girl is RogueX:
                                ch_r "Ну, если ты так говоришь. . ."
                        elif Girl is KittyX:
                                ch_k "Может ты и права. . ."
                        elif Girl is EmmaX:
                                ch_e "Если ты настаиваешь. . ."
                        elif Girl is LauraX:
                                ch_l "Если ты настаиваешь. . ."
                        elif Girl is JeanX:
                                ch_j "Не проверишь, не узнаешь. . ."
                        elif Girl is StormX:
                                ch_s "Я не уверена. . ."
                        elif Girl is JubesX:
                                ch_v "Я, эм. . . Возможно? . ."
                        elif Girl is GwenX:
                                ch_g "А ты хороша в \"переговорах\"."
                        elif Girl is BetsyX:
                                ch_b "Пожалуй, можно. . ."
                        elif Girl is DoreenX:
                                ch_d "Наверное, можно. . ."
                        elif Girl is WandaX:
                                ch_w "Пожалуй, можно. . ."
                else:
                        $ Girl.Addictionrate += 1
                        if "addictive" in Player.Traits:
                            $ Girl.Addictionrate += 1
                        $ Girl.Blush = 1
                        if Girl is RogueX:
                                ch_r "Если ты этого хочешь, еще не значит, что этого хочу и я, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k "Если ты этого хочешь, еще не значит, что этого хочу и я, [Girl.Petname]."
                        elif Girl is EmmaX:
                                ch_e "Я очень в этом сомневаюсь, [Girl.Petname]."
                        elif Girl is LauraX:
                                ch_l "Ты думаешь, у меня нет носа, [Girl.Petname]?"
                        elif Girl is JeanX:
                                ch_j "Ага, такого я еще не слышала. . ."
                        elif Girl is StormX:
                                ch_s "Это. . . маловероятно. . ."
                        elif Girl is JubesX:
                                ch_v "Я, эм. . . немного сомневаюсь в этом. . ."
                        elif Girl is GwenX:
                                ch_g "А ты хороша в \"переговорах\"."
                        elif Girl is BetsyX:
                                ch_b "Я очень в этом сомневаюсь. . ."
                        elif Girl is DoreenX:
                                ch_d "Я так не думаю. . ."
                        elif Girl is WandaX:
                                ch_w "Я в этом сомневаюсь. . ."
                        jump Girl_Handy_Finish

        "Я серьезно, приступай.":
                if ApprovalCheck(Girl, 1500, "LI", TabM=1) or ApprovalCheck(Girl, 1200, "OI", TabM=1):
                        $ Girl.FaceChange("sucking", 1)
                elif ApprovalCheck(Girl, 1000, "OI", Bonus = (Girl.Addict*10)): #Mild addiction included
                        $ Girl.FaceChange("angry", 1)
                else:
                        #You insisted, she refused.
                        $ Girl.FaceChange("angry", 1)
                        "Она сердито смотрит на вас и отстраняется."
                        call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                        call expression Girl.Tag+"_HJ_Reset"
                        $ Girl.Statup("Love", 50, -3, 1)
                        $ Girl.Statup("Love", 80, -4, 1)
                        if Girl is RogueX:
                                ch_r "С таким отношением справляйся сама."
                        elif Girl is KittyX:
                                ch_k "Справляйся тогда без меня."
                        elif Girl is EmmaX:
                                ch_e "Мне кажется, ты переоцениваешь свое обаяние."
                        elif Girl is LauraX:
                                ch_l "Я тоже серьезно, наверни говна."
                        elif Girl is JeanX:
                                ch_j "Иди нахуй, сучка."
                        elif Girl is StormX:
                                ch_s "Нет."
                        elif Girl is JubesX:
                                ch_v "Мне это не нужно. . ."
                        elif Girl is GwenX:
                                ch_g "А ты -очень- хороша в \"переговорах\"."
                        elif Girl is BetsyX:
                                ch_b "Такое отношение не принесет тебе никакой пользы. . ."
                        elif Girl is DoreenX:
                                ch_d "Ни за что, подруга!"
                        elif Girl is WandaX:
                                ch_w "Хех, нет, спасибо."
                        $ Girl.Statup("Obed", 30, -1, 1,Alt=[[JeanX],900,3]) #+3 for Jean
                        $ Girl.Statup("Obed", 50, -1, 1)
                        $ Girl.RecentActions.append("angry")
                        $ Girl.DailyActions.append("angry")
                        $ Line = 0
                        return
                $ Girl.Statup("Obed", 50, 10,Alt=[[JeanX],900,10]) #+10 for Jean
                $ Girl.Statup("Obed", 70, 5)

    if not renpy.showing(Girl.Tag+"_CUN_Animation") and not renpy.showing(Girl.Tag+"_69_CUN"): #if not renpy.showing("Rogue_BJ_Animation"):
        call expression Girl.Tag+"_CUN_Launch" pass ("cum")
    $ Speed = 2
    if ApprovalCheck(Girl, 1200):
            "Она нежно прижимается губками к вашей киске, а затем начинает ее посасывать."
    else:
            "Она осторожно прижимает губы к вашей киске, и вы сразу кончаете внутрь ее ротика."
            $ Girl.FaceChange("sexy")
            $ Girl.Statup("Love", 50, -3, 1)
            $ Girl.Statup("Love", 80, -4, 1)
    $ Girl.Mouth = "sucking"
    $ Player.Spunk = 1
    $ Girl.Spunk.append("chin")
    $ Girl.Spunk.append("mouth")
    call AnyLine(Girl,". . .")
    "У нее срабатывает рвотный рефлекс, но затем она быстро все проглатывает."
    $ Speed = 0
    $ Girl.FaceChange("sexy")

    if ApprovalCheck(Girl, 1000) and Girl.Swallow >= 3:
            call Sex_Basic_Dialog(Girl,"swallow2") #"I'm starting to get used to that."
    elif ApprovalCheck(Girl, 800):
            call Sex_Basic_Dialog(Girl,"swallowfirst") #"I'm not really a fan of that, [Girl.Petname]."
    else:
            $ Girl.FaceChange("sad")
            call Sex_Basic_Dialog(Girl,"swallowfirst") #"I'm not really a fan of that, [Girl.Petname]."
    $ Girl.Statup("Inbt", 30, 3)
    $ Girl.Statup("Inbt", 50, 2)
    $ Girl.Blow += 1
    jump Girl_Swallowed
    #end Cum in mouth  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Creampie_P: #rkeljsvg
        if Trigger == "sex" and Situation == "auto":
                $ Player.Cock = "in"
                $ Girl.Spunk.append("in")
                $ Player.Spunk = "in"
                $ Speed = 0
                if ApprovalCheck(Girl, 1300) or Girl.CreamP:
                        $ Girl.FaceChange("surprised")
                        "Вы кончаете внутрь ее киски. Ее глаза расширяются от удивления, но негативной реакции не следует."
                        $ Girl.FaceChange("sexy")
                        if Girl.Lust >= 85:
                                call Girl_Cumming(Girl)
                else:
                        if Girl.Lust >= 85:
                                "Вы кончаете внутрь ее киски. Ее глаза расширяются от удивления, а тело начинает слегка дрожать."
                                call Girl_Cumming(Girl)
                        else:
                                "Вы кончаете внутрь ее киски. Ее глаза расширяются от удивления и она соскакивает с члена."
                        $ Player.Cock = "out"
                        $ Girl.FaceChange("angry")
                        if Girl is RogueX:
                                ch_r "Эй, в следующий раз предупреждай, ладно?"
                                $ Girl.FaceChange("bemused")
                                ch_r "Но все же, это было не так уж и плохо. . ."
                        elif Girl is KittyX:
                                ch_k "Ты мог бы хоть как-нибудь[Girl.like]предупредить!"
                                $ Girl.FaceChange("bemused")
                                ch_k "Хотя было довольно неплохо. . ."
                        elif Girl is EmmaX:
                                ch_e "Может, в следующий раз предупредишь?"
                                $ Girl.FaceChange("bemused")
                                ch_e "Хотя не скажу, что было плохо. . ."
                        elif Girl is LauraX:
                                ch_l "Эй, может быть, стоит предупреждать?"
                                $ Girl.FaceChange("bemused")
                                ch_l "Не то чтобы это было неприятно. . ."
                        elif Girl is JeanX:
                                ch_j "Эй! Что это было!"
                                ch_j ". . ."
                                $ Girl.FaceChange("bemused")
                                ch_j "Но, если честно, было довольно приятно. . ."
                        elif Girl is StormX:
                                ch_s "Ты мог бы предупредить, что собираешься кончить в меня. . ."
                                $ Girl.FaceChange("bemused")
                                ch_s "Хотя ощущения были потрясающими. . ."
                        elif Girl is JubesX:
                                ch_v "Мне бы не помешало маленькое предупреждение!"
                                $ Girl.FaceChange("bemused")
                                ch_v "Так тепло внутри. . ."
                        elif Girl is GwenX:
                                ch_g "Ты мог бы и предупредить меня, что планируешь это сделать!"
                                $ Girl.FaceChange("bemused")
                                ch_g "Но было. . . приятно. . ."
                        elif Girl is BetsyX:
                                ch_b "Немешало бы предупредить меня. . ."
                                $ Girl.FaceChange("bemused")
                                ch_b "Однако, это было. . . не неприятно. . ."
                        elif Girl is DoreenX:
                                ch_d "Эй! Ты мог бы и предупредить меня!"
                                $ Girl.FaceChange("bemused")
                                ch_d "ноооо. . . я думаю, это было по приятному безумно. . ."
                        elif Girl is WandaX:
                                ch_w "Воу! Тебе следовало предупредить меня!"
                                $ Girl.FaceChange("bemused")
                                ch_w "Но, думаю, мне даже немного понравилось."
                jump Girl_Creampied

        #else (You ask her if it's ok):
        if ApprovalCheck(Girl, 1200) or Girl.CreamP:
                $ Girl.FaceChange("sexy")
                if Girl.CreamP >= 3:
                        "Она улыбается и ускоряет свои движения, заставляя вас кончить внутрь нее."
                elif Girl.CreamP:
                        "Ее глаза загораются и она ускоряется, из-за чего вы почти сразу кончаете в нее."
                else:
                        "Продолжая методично ее трахать, вы видите ее кивок."
                $ Player.Cock = "in"
                $ Girl.Spunk.append("in")
                $ Player.Spunk = "in"
                $ Speed = 0
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                $ Girl.Statup("Love", 90, 1)
                if Girl is RogueX:
                        ch_r "Хмм, ты знаешь, как меня {i}правильно{/i} заполнить."
                elif Girl is KittyX:
                        ch_k "Хм, уютно. . ."
                elif Girl is EmmaX:
                        ch_e "Так. . . наполняет."
                elif Girl is LauraX:
                        ch_l "Очень. . . наполняет."
                elif Girl is JeanX:
                        ch_j "Очень. . . согревает."
                elif Girl is StormX:
                        ch_s "Такое приятное тепло. . ."
                elif Girl is JubesX:
                        ch_v "Так тепло внутри. . ."
                elif Girl is GwenX:
                        ch_g "Ммм. . . это так приятно. . ."
                elif Girl is BetsyX:
                        ch_b "Довольно уютно. . ."
                elif Girl is DoreenX:
                        ch_d "Ты хорошо наполнил меня. . ."
                elif Girl is WandaX:
                        ch_w "Там теперь так тепло. . ."
                jump Girl_Creampied
        else:
                $ Girl.FaceChange("sexy")
                $ Girl.Statup("Love", 80, 2)
                $ Girl.Statup("Love", 90, 2)
                if Girl is RogueX:
                        ch_r "Спасибо, что предупредил *неразборчиво*, [Girl.Petname], но я бы предпочла, чтобы ты этого не делал."
                elif Girl is KittyX:
                        ch_k "Спасибо за предупреждение, но, может, не стоило?"
                elif Girl is EmmaX:
                        ch_e "Спасибо, что предупредил *неразборчиво*, [Girl.Petname], но давай обойдемся без этого."
                elif Girl is LauraX:
                        ch_l "Спасибо, что предупредил *неразборчиво*, [Girl.Petname], но лучше не надо."
                elif Girl is JeanX:
                        ch_j "Ага, больше не предупреждай. Ладно, пора выстаскивать."
                elif Girl is StormX:
                        ch_s "Благодарю, [Girl.Petname], но больше не стоит предупреждать. . ."
                elif Girl is JubesX:
                        ch_v "Это было мило, но больше так не делай. . ."
                elif Girl is GwenX:
                        ch_g "Ага, эм. . . может *неразборчиво* не стоит предупреждать?"
                elif Girl is BetsyX:
                        ch_b "Благодарю, *неразборчиво* но лучше бы ты этого не делал. . ."
                elif Girl is DoreenX:
                        ch_d "Ох, спасибо, но тебе не стоило этого делать, *неразборчиво*. . . ладно, можешь доставать. . ."
                elif Girl is WandaX:
                        ch_w "Спасибо, что предупредил, но *неразборчиво*. . . лучше не надо. . ."
        jump Girl_Cum_Outside

#Start Anal Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Creampie_A:      #rkeljsvg
        # These need conditionals added
        if Trigger == "anal" and Situation == "auto":
                $ Player.Cock = "anal"
                $ Girl.Spunk.append("anal")
                $ Player.Spunk = "anal"
                $ Speed = 0
                if ApprovalCheck(Girl, 1200) or Girl.CreamP:
                        $ Girl.FaceChange("surprised", 1)
                        "Вы кончаете в ее попку. Ее глаза расширяются от удивления, но негативной реакции не следует."
                        $ Girl.FaceChange("sexy")
                        if Girl.Lust >= 85:
                                call Girl_Cumming(Girl)
                else:
                        if Girl.Lust >= 85:
                                "Вы кончаете в ее попку. Ее глаза расширяются от удивления, а тело начинает слегка дрожать."
                                call Girl_Cumming(Girl)
                        else:
                                "Вы кончаете в ее попку. Ее глаза расширяются от удивления, и она вытаскивает его из себя."
                        $ Player.Cock = "out"
                        $ Girl.FaceChange("angry")
                        if Girl is RogueX:
                                ch_r "Эй, надо предупреждать!"
                                $ Girl.FaceChange("bemused")
                                ch_r "Но. . . Ну ладно, это и вправду было приятно. . ."
                        elif Girl is KittyX:
                                ch_k "Может, в слудющий раз предупредишь?"
                                $ Girl.FaceChange("bemused")
                                ch_k "хотя это было довольно неплохо. . ."
                        elif Girl is EmmaX:
                                ch_e "Без предупреждения, [Girl.Petname]?"
                                $ Girl.FaceChange("bemused")
                                ch_e "Хотя, это так. . . заполняет."
                        elif Girl is LauraX:
                                ch_l "Без предупреждения, [Girl.Petname]?"
                                $ Girl.FaceChange("bemused")
                                ch_l "Это так заполняет. . ."
                        elif Girl is JeanX:
                                ch_j "Эй! Что это было!"
                                ch_j ". . ."
                                $ Girl.FaceChange("bemused")
                                ch_j "Но это было довольно неплохо. . ."
                        elif Girl is StormX:
                                ch_s "Ты мог бы предупредить, что собираешься кончить в меня. . ."
                                $ Girl.FaceChange("bemused")
                                ch_s "Хотя ощущения были потрясающими. . ."
                        elif Girl is JubesX:
                                ch_v "Мне бы не помешало маленькое предупреждение!"
                                $ Girl.FaceChange("bemused")
                                ch_v "Так тепло внутри. . ."
                        elif Girl is GwenX:
                                ch_g "Ты мог бы и предупредить меня, что планируешь это сделать!"
                                $ Girl.FaceChange("bemused")
                                ch_g "Но было. . . приятно. . ."
                        elif Girl is BetsyX:
                                ch_b "Немешало бы предупредить меня. . ."
                                $ Girl.FaceChange("bemused")
                                ch_b "Однако, это было. . . не неприятно. . ."
                        elif Girl is DoreenX:
                                ch_d "Эй! Ты мог бы и предупредить меня!"
                                $ Girl.FaceChange("bemused")
                                ch_d "ноооо. . . я думаю, это было по приятному безумно. . ."
                        elif Girl is WandaX:
                                ch_w "Воу! Тебе стоило предупредить меня!"
                                $ Girl.FaceChange("bemused")
                                ch_w "Но, думаю, мне даже немного понравилось."
                jump Girl_Creampied

        #else (You ask her if it's ok):
        if ApprovalCheck(Girl, 1200) or Girl.CreamP:
                $ Girl.FaceChange("sexy")
                if Girl.CreamP >= 3:
                        "Она улыбается и ускоряет свои движения, заставляя вас кончить внутрь нее."
                elif Girl.CreamP:
                        "Ее глаза загораются и она ускоряется, из-за чего вы почти сразу кончаете в нее."
                else:
                        "Продолжая методично ее трахать, вы видите ее кивок."
                $ Player.Cock = "anal"
                $ Girl.Spunk.append("anal")
                $ Player.Spunk = "anal"
                $ Speed = 0
                if Girl.Lust >= 85:
                        call Girl_Cumming(Girl)
                $ Girl.Statup("Love", 90, 1)
                if Girl is RogueX:
                        ch_r "Хмм, я чувстую себя такой заполненной. . ."
                elif Girl is KittyX:
                        ch_k "Оу,  я чувстую себя такой заполненной. . ."
                elif Girl is EmmaX:
                        ch_e "Мммм, я чувстую себя такой заполненной. . ."
                elif Girl is LauraX:
                        ch_l "Мммм, так заполняет. . ."
                elif Girl is JeanX:
                        ch_j "Очень. . . согревает."
                elif Girl is StormX:
                        ch_s "Такое приятное тепло. . ."
                elif Girl is JubesX:
                        ch_v "Так тепло внутри. . ."
                elif Girl is GwenX:
                        ch_g "Ммм. . . это так приятно. . ."
                elif Girl is BetsyX:
                        ch_b "Довольно уютно. . ."
                elif Girl is DoreenX:
                        ch_d "Ты хорошо наполнил меня. . ."
                elif Girl is WandaX:
                        ch_w "Там теперь так тепло. . ."
                jump Girl_Creampied
        else:
                $ Girl.FaceChange("sexy")
                $ Girl.Statup("Love", 80, 2)
                if Girl is RogueX:
                        ch_r "Спасибо, что предупредил *неразборчиво*, [Girl.Petname], но я бы предпочла, чтобы ты этого не делал."
                elif Girl is KittyX:
                        ch_k "Спасибо за предупреждение, но, может, не стоило?"
                elif Girl is EmmaX:
                        ch_e "Спасибо, что предупредил *неразборчиво*, [Girl.Petname], но давай обойдемся без этого."
                elif Girl is LauraX:
                        ch_l "Спасибо, что предупредил *неразборчиво*, [Girl.Petname], но лучше не надо."
                elif Girl is JeanX:
                        ch_j "Ага, больше не предупреждай. Ладно, пора выстаскивать."
                elif Girl is StormX:
                        ch_s "Благодарю, [Girl.Petname], но больше не стоит предупреждать. . ."
                elif Girl is JubesX:
                        ch_v "Это было мило, но больше так не делай. . ."
                elif Girl is GwenX:
                        ch_g "Ага, эм. . . может *неразборчиво* не стоит предупреждать?"
                elif Girl is BetsyX:
                        ch_b "Благодарю, *неразборчиво* но лучше бы ты этого не делал. . ."
                elif Girl is DoreenX:
                        ch_d "Ох, спасибо, но тебе не стоило этого делать, *неразборчиво*. . . ладно, можешь доставать. . ."
                elif Girl is WandaX:
                        ch_w "Спасибо за предупреждение, но *неразборчиво*. . . лучше не надо. . ."
        jump Girl_Cum_Outside

#Start Facial  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Facial:
        if renpy.showing(Girl.Tag+"_BJ_Animation") or renpy.showing(Girl.Tag+"_69_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
                        jump Manic_Suck
                if Player.Male:
                        call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                        $ Speed = 2
                        if "hair" in Girl.Spunk:
                                pass
                        elif "facial" in Girl.Spunk:
                                $ Girl.Spunk.append("hair")
                        else:
                                $ Girl.Spunk.append("facial")
                        "С громким 'чпоком' вы вытаскиваете свой член из ее рта, и она начинает вам дрочить. Вы кончаете ей на лицо."
                        $ Speed = 0
                else:
                        $ Girl.Spunk.append("tits")
                        "Когда она касается вашего резинового члена, вы испытываете оргазм и забрызгиваете ее сиськи."

        elif renpy.showing(Girl.Tag+"_CUN_Animation") or renpy.showing(Girl.Tag+"_69_CUN"): #if renpy.showing("Rogue_CUN_Animation"):
                if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
                        jump Manic_Suck
                call Punch
                if "hair" in Girl.Spunk:
                        pass
                elif "facial" in Girl.Spunk:
                        $ Girl.Spunk.append("hair")
                else:
                        $ Girl.Spunk.append("facial")
                "Пока она вылизывает вашу киску, вы достигаете кульминации и кончаете ей на лицо."
                $ Speed = 0

        elif renpy.showing(Girl.Tag+"_TJ_Animation"): #if renpy.showing("Rogue_TJ_Animation"):
                if Player.Male:
                        if "hair" in Girl.Spunk:
                                pass
                        elif "facial" in Girl.Spunk:
                                $ Girl.Spunk.append("hair")
                        else:
                                $ Girl.Spunk.append("facial")
                        if not Girl.Tit:
                                "Она поднимает взгляд на вас, но продолжает двигать своей грудью вверх-вниз. Вскоре вы заливаете спермой все ее лицо."
                        else:
                                "Как только вы чувствуете, что вот-вот кончите, вы прицеливаетесь ей на лицо и начинаете заливать его своей спермой."
                        $ Speed = 0
                else:
                        "Вы продолжаете ласкать ее грудь, когда оргазм заключает вас в свои объятия, вы кончаете ей на животик."
                        $ Girl.Spunk.append("belly")

        elif not Player.Male:
                call expression Girl.Tag+"_CUN_Launch" pass ("cum")
                if Situation != "warn":
                        $ Girl.FaceChange("surprised")
                $ Speed = 0
                if "hair" in Girl.Spunk:
                        pass
                elif "facial" in Girl.Spunk:
                        $ Girl.Spunk.append("hair")
                else:
                        $ Girl.Spunk.append("facial")
                "Когда вы уже вот-вот готовы кончить, вы отстраняетесь и брызгаете ей на лицо."
                $ Girl.FaceChange("sly")

        elif renpy.showing(Girl.Tag+"_HJ_Animation"): #if renpy.showing("Rogue_HJ_Animation"):
                if "hair" in Girl.Spunk:
                        pass
                elif "facial" in Girl.Spunk:
                        $ Girl.Spunk.append("hair")
                else:
                        $ Girl.Spunk.append("facial")
                if not Girl.Hand:
                        "Она немного смущается, но продолжает двигать свой рукой, при этом смотря на ваш член, будто гипнотизируя его. Достигнув кульминации, вы заливаете спермой все ее лицо."
                else:
                        "Как только вы чувствуете, что вот-вот кончите, вы прицеливаетесь ей на лицо и кончаете."
                $ Speed = 0
        elif renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                call Girl_Breasts_Launch(Girl,0,0) #call expression Girl.Tag + "_Breasts_Launch" pass (Trigger,0)
                if "hair" in Girl.Spunk:
                        pass
                elif "facial" in Girl.Spunk:
                        $ Girl.Spunk.append("hair")
                else:
                        $ Girl.Spunk.append("facial")
                "Как только вы чувствуете, что вот-вот кончите, вы прицеливаетесь ей на лицо и кончаете."
                $ Speed = 0
        else:
                call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                $ Speed = 2
                if "hair" in Girl.Spunk:
                        pass
                elif "facial" in Girl.Spunk:
                        $ Girl.Spunk.append("hair")
                else:
                        $ Girl.Spunk.append("facial")
                "Как только вы чувствуете, что вот-вот кончите, вы слегка отстраняетесь, прицеливаетесь на ее лицо и кончаете."
                $ Speed = 0

        call Warned_Outside
        $ Player.Cock = "out"
        jump Girl_Orgasm_After
#End Facial  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start titjob spunk  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_TitSpunk:
        if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
                            jump Manic_Suck

        #if not renpy.showing("Rogue_TJ_Animation") and not renpy.showing("Rogue_HJ_Animation") and not renpy.showing("Rogue_BJ_Animation"):
        if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                call Girl_Breasts_Launch(Girl,0,0) #call expression Girl.Tag + "_Breasts_Launch" pass (Trigger,0)
        elif not renpy.showing(Girl.Tag+"_TJ_Animation") and not renpy.showing(Girl.Tag+"_HJ_Animation") and not renpy.showing(Girl.Tag+"_BJ_Animation"):
                call expression Girl.Tag+"_HJ_Launch" pass ("cum")
        $ Girl.Spunk.append("tits")
        $ Speed = 0
        "Как только вы чувствуете, что вот-вот кончите, вы ускоряетесь и кончаете ей на грудь."
        call Warned_Outside
        jump Girl_Orgasm_After
#End titjob spunk  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start feet spunk  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_FeetSpunk:
        if renpy.showing(Girl.Tag+"_BJ_Animation") or renpy.showing(Girl.Tag+"_CUN_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
                            jump Manic_Suck

        #if not renpy.showing("Rogue_TJ_Animation") and not renpy.showing("Rogue_HJ_Animation") and not renpy.showing("Rogue_BJ_Animation"):
        if renpy.showing(Girl.Tag+"_BJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                call expression Girl.Tag + "_Sex_Launch" pass ("cum")
        elif not renpy.showing(Girl.Tag+"_Doggy_Animation") and not renpy.showing(Girl.Tag+"_SexSprite"):
                call expression Girl.Tag+"_Doggy_Launch" pass ("cum")
        $ Girl.Spunk.append("feet")
        $ Speed = 0
        "Когда вы уже почти не можете сдерживаться, вы ускоряетесь и кончаете ей на ноги."
        call Warned_Outside
        jump Girl_Orgasm_After
#End feet spunk  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Warned_Outside:   #rkeljsvgbdw
        #Dialogue called when shot outside
        if Girl is RogueX:
                if Situation == "warn":
                    if not Player.Male:
                        ch_r "Спасибо, что предупредила, [Girl.Petname]. Хотя ты меня всю испачкала. . ."
                    else:
                        ch_r "Спасибо, что предупредил, [Girl.Petname]. Хотя ты меня всю испачкал. . ."
                else:
                    if not Player.Male:
                        ch_r "Боже, сколько же ее, могла бы и предупредить."
                    else:
                        ch_r "Боже, сколько же ее, мог бы и предупредить."
        elif Girl is KittyX:
                if Situation == "warn":
                    ch_k "Фух, Спасибо за предупреждение."
                else:
                    if not Player.Male:
                        ch_k "Уф, могла бы и предупредить, [Girl.Petname]."
                    else:
                        ch_k "Уф, мог бы и предупредить, [Girl.Petname]."
        elif Girl is EmmaX:
                if Situation == "warn":
                    if not Player.Male:
                        ch_e "Я рада, что ты меня предупредила. . . хоть ты и всю меня испачкала. . ."
                    else:
                        ch_e "Я рада, что ты меня предупредил. . . хоть ты и всю меня испачкал. . ."
                else:
                    if not Player.Male:
                        ch_e "Стоит все-таки предупреждать, ты всю меня испачкала."
                    else:
                        ch_e "Стоит все-таки предупреждать, ты всю меня испачкал."
        elif Girl is LauraX:
                if Situation == "warn":
                    if not Player.Male:
                        ch_l "Спасибо за предупреждение. . . но ты всю меня перепачкала. . ."
                    else:
                        ch_l "Спасибо за предупреждение. . . но ты всю меня перепачкал. . ."
                else:
                    if not Player.Male:
                        ch_l "Ты всю меня перепачкала, может быть, в следующий раз предупредишь?"
                    else:
                        ch_l "Ты всю меня перепачкал, может быть, в следующий раз предупредишь?"
        elif Girl is JeanX:
                if Situation == "warn":
                    if not Player.Male:
                        ch_j "Оу, ты всю меня испачкала. . ."
                    else:
                        ch_j "Оу, ты всю меня испачкал. . ."
                else:
                    if not Player.Male:
                        ch_j "Эй, ты могла хоть как-нибудь предупредить?"
                    else:
                        ch_j "Эй, ты мог хоть как-нибудь предупредить?"
        elif Girl is StormX:
                if Situation == "warn":
                    ch_s "Спасибо за предупреждение, хоть от него и мало пользы. . ."
                else:
                    if not Player.Male:
                        ch_s "Да уж, ты всю меня перепачкала."
                    else:
                        ch_s "Да уж, ты всю меня перепачкал."
        elif Girl is JubesX:
                if Situation == "warn":
                    ch_v "Фу, я вся перепачкана. . ."
                else:
                    ch_v "Фу, я вся перепачкана. . . предупреждай в следующий раз, а?"
        elif Girl is GwenX:
                if Situation == "warn":
                    ch_g "Воу. . . она у тебя повсюду. . ."
                else:
                    ch_g "Воу. . . она у тебя повсюду. . ."
                    ch_g "Можешь.  . предупредить меня в следующий раз?"
        elif Girl is BetsyX:
                if Situation == "warn":
                    if not Player.Male:
                        ch_b "Ты оставила мне настоящий беспорядок. . ."
                    else:
                        ch_b "Ты оставил мне настоящий беспорядок. . ."
                else:
                    if not Player.Male:
                        ch_b "Ты оставила мне настоящий беспорядок. . ."
                    else:
                        ch_b "Ты оставил мне настоящий беспорядок. . ."
                    ch_b "Не думаешь, что стоило предупредить?"
        elif Girl is DoreenX:
                if Situation == "warn":
                    if not Player.Male:
                        ch_d "Воу! Ты всю меня забрызгала!"
                    else:
                        ch_d "Воу! Ты всю меня забрызгал!"
                else:
                    if not Player.Male:
                        ch_d "Воу! Ты всю меня забрызгала!"
                        ch_d "Ты не могла меня как-нибудь предупредить?!"
                    else:
                        ch_d "Воу! Ты всю меня забрызгал!"
                        ch_d "Ты не мог меня как-нибудь предупредить?!"
        elif Girl is WandaX:
                if Situation == "warn":
                    if not Player.Male:
                        ch_w "Хорошо, что ты предупредила меня, их очень много. . ."
                    else:
                        ch_w "Хорошо, что ты предупредил меня, ее очень много. . ."
                else:
                    ch_w "Воу! Я теперь вся липкая."
                    ch_w "Тебе следовало предупредить меня!"
        return
# Start Spunk back  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Cum_Outside:  #rkeljsvg
        if not Player.Male:
                    if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"):
                            "Когда вы входите в нее, оргазм поражает вас, вы забрызгиваете пол под ней."
                    jump Girl_Orgasm_After

        if Trigger != "foot":
            if renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                call Girl_Middle_Launch(Girl,Trigger,0)  #call expression Girl.Tag + "_Middle_Launch" pass (Trigger,0)

            elif Girl.Pose != "doggy" and Girl in (EmmaX,JeanX,WandaX): # temporary until these girls get a front pose   fix
                call Girl_Middle_Launch(Girl,Trigger,0)  #call expression Girl.Tag + "_Middle_Launch" pass (Trigger,0)
#            elif Girl.Pose == "doggy" and (Girl == EmmaX):  # temporary until these girls get a rear pose
#                pass

            else:
                call expression Girl.Tag+"_Sex_Launch" pass ("hotdog") #call Rogue_Doggy_Launch("hotdog")
        $ Speed = 0
        if Girl.Addict >= 60 and ApprovalCheck(Girl, 1000, "I", Bonus = ((Girl.Addict*10)- Girl.Obed))  and Girl.Swallow:
                $ Girl.Eyes = "manic"
                $ Girl.Blush = 1
                call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                if Trigger == "sex":
                    "Вытащив свой ствол из ее киски с влажным чпоком, вы замечаете, как ее глаза расширяются от удивления. Она насаживается своим ртом на ваш член и начитает сосет его так жадно и сильно, словно через него хочет высосать все ваши соки."
                elif Trigger == "anal":
                    "Вытащив свой ствол из ее попки с чпоком, вы замечаете, как ее глаза расширяются от удивления. Она насаживается своим ртом на ваш член и начитает сосет его так жадно и сильно, словно через него хочет высосать все ваши соки."
                $ Girl.Mouth = "lipbite"
                $ Girl.Spunk.append("mouth")
                "Закончив, она облизывает свои губы."
                $ Girl.FaceChange("bemused")
                $ Girl.Spunk.remove("mouth")
                if Girl is RogueX:
                        if not Player.Male:
                            ch_r "Ну, [Girl.Petname], я просто не хотела, чтобы они пропали зря."
                        else:
                            ch_r "Ну, [Girl.Petname], я просто не хотела, чтобы она пропала зря."
                elif Girl is KittyX:
                        if not Player.Male:
                            ch_k "Извини, они просто[Girl.like]таааааакие приятные."
                        else:
                            ch_k "Извини, она просто[Girl.like]таааааакая приятная."
                elif Girl is EmmaX:
                        if not Player.Male:
                            ch_e "Что ж, [Girl.Petname], Я просто не могла позволить еи пропасть даром."
                        else:
                            ch_e "Что ж, [Girl.Petname], Я просто не могла позволить ей пропасть даром."
                elif Girl is LauraX:
                        if not Player.Male:
                            ch_l "Я не могла позволить им пропасть даром."
                        else:
                            ch_l "Я не могла позволить ей пропасть даром."
                elif Girl is JeanX:
                        ch_j "Ммм. . ."
                elif Girl is StormX:
                        ch_s "Это было бы расточительством. . ."
                elif Girl is JubesX:
                        ch_v "Не хотелось бы, чтобы все это пропало зря. . ."
                elif Girl is GwenX:
                        ch_g "Я, эм. . . была голодна?"
                elif Girl is BetsyX:
                        if not Player.Male:
                            ch_b "Боюсь, онт у тебя слишком восхитительны. . ."
                        else:
                            ch_b "Боюсь, она у тебя слишком восхитительна. . ."
                elif Girl is DoreenX:
                        ch_d "Ох, эм. . . извини. . ."
                elif Girl is WandaX:
                        ch_w "Прости, я. . . хотела пить. . ."
                $ Girl.Statup("Obed", 80, -5)
                $ Girl.Statup("Inbt", 200, 10)
                jump Girl_Swallowed
        if Trigger != "foot":
                $ Player.Cock = "out"
        if Girl.Pose == "doggy":
                $ Girl.Spunk.append("back")
                if Trigger == "sex":
                        "Вы выходите из ее киски и начинаете заливать ее спину."
                elif Trigger == "anal":
                        "Вы выходите из ее попки и начинаете заливать ее спину."
                else:
                        "Вы ускоряетесь, а затем с рыком начинаете заливать ее спину."
        else:
                $ Girl.Spunk.append("belly")
                if Trigger == "sex":
                        "Вы с влажным чпоком выходите из ее киски и кончаете ей на живот."
                elif Trigger == "anal":
                        "Вы с чпоком выходите ее попки и кончаете ей на живот."
                else:
                        "Вы ускоряетесь, а затем с рыком начинаете кончать ей на живот."
        if Girl.Addict >= 60 and ApprovalCheck(Girl, 800, "I", Bonus = ((Girl.Addict*10)- Girl.Obed)) and Girl.Swallow:
                    #if she's manic and has swallowed
                    $ Girl.Eyes = "manic"
                    $ Girl.Blush = 1
                    "[Girl.Name]'s eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
                    $ Girl.FaceChange("manic", 1)
                    $ Girl.Spunk.append("mouth")
                    $ Girl.Mouth = "smile"
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Ну, [Girl.Petname], я просто не хотела, чтобы они пропали зря."
                            else:
                                ch_r "Ну, [Girl.Petname], я просто не хотела, чтобы она пропала зря."
                    elif Girl is KittyX:
                            if not Player.Male:
                                ch_k "Извини, они просто[Girl.like]таааааакие приятные."
                            else:
                                ch_k "Извини, она просто[Girl.like]таааааакая приятная."
                    elif Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Что ж, [Girl.Petname], Я просто не могла позволить еи пропасть даром."
                            else:
                                ch_e "Что ж, [Girl.Petname], Я просто не могла позволить ей пропасть даром."
                    elif Girl is LauraX:
                            if not Player.Male:
                                ch_l "Я не могла позволить им пропасть даром."
                            else:
                                ch_l "Я не могла позволить ей пропасть даром."
                    elif Girl is JeanX:
                            ch_j "Ммм. . ."
                    elif Girl is StormX:
                            ch_s "Это было бы расточительством. . ."
                    elif Girl is JubesX:
                            ch_v "Не хотелось бы, чтобы все это пропало зря. . ."
                    elif Girl is GwenX:
                            ch_g "Я, эм. . . была голодна?"
                    elif Girl is BetsyX:
                            if not Player.Male:
                                ch_b "Боюсь, онт у тебя слишком восхитительны. . ."
                            else:
                                ch_b "Боюсь, она у тебя слишком восхитительна. . ."
                    elif Girl is DoreenX:
                            ch_d "Ох, эм. . . извини. . ."
                    elif Girl is WandaX:
                            ch_w "Прости, я. . . хотела пить. . ."
                    $ Girl.Spunk.remove("mouth")
                    $ Girl.Statup("Inbt", 50, 3)
                    jump Girl_Swallowed
        #end manic suck

        #else . . .
        $ Girl.FaceChange("sexy", 1)
        if Girl is RogueX:
                ch_r "Боже, какой беспорядок. . ."
        elif Girl is KittyX:
                if not Player.Male:
                    ch_k "Мммм, ты все забрызгала. . ."
                else:
                    ch_k "Мммм, ты все забрызгал. . ."
        elif Girl is EmmaX:
                if not Player.Male:
                    ch_e "Хмм. . . их так много. . ."
                else:
                    ch_e "Хмм. . . ее так много. . ."
        elif Girl is LauraX:
                ch_l "Хмм. . . какой бардак. . ."
        elif Girl is JeanX:
                ch_j "Фу. . ."
        elif Girl is StormX:
                if not Player.Male:
                    ch_s "Да уж, ты всю меня перепачкала."
                else:
                    ch_s "Да уж, ты всю меня перепачкал."
        elif Girl is JubesX:
                ch_v "Фу, я перепачкана. . ."
        elif Girl is GwenX:
                if not Player.Male:
                    ch_g "Воу. . . они у тебя повсюду. . ."
                else:
                    ch_g "Воу. . . она у тебя повсюду. . ."
        elif Girl is BetsyX:
                if not Player.Male:
                    ch_b "Ты устроила настоящий беспорядок. . ."
                else:
                    ch_b "Ты устроил настоящий беспорядок. . ."
        elif Girl is DoreenX:
                if not Player.Male:
                    ch_d "Ох, ого, они повсюду. . ."
                else:
                    ch_d "Ох, ого, она повсюду. . ."
        elif Girl is WandaX:
                ch_w "Воу, я теперь вся липкая. . ."
#        call expression Girl.Tag+"_Doggy_Reset"
        jump Girl_Orgasm_After

#Start Handy finish  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Handy_Finish: #rkeljsvg
        if Player.Male:
            if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                    call expression Girl.Tag+"_Doggy_Reset"
                    call expression Girl.Tag+"_Sex_Reset"
                    if Trigger == "hotdog":
                        "Она наклоняется и начинает ласкать вас."
                    else:
                        "Она усмехается, подается назад со звонким 'чпоком', а затем начинает с усердием вам дрочить."
                    $ Speed = 2
            elif renpy.showing(Girl.Tag+"_BJ_Animation") or renpy.showing(Girl.Tag+"_69_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                    call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                    $ Speed = 2
                    "Она отрывает губы от вашего члена и начинает вам дрочить."
            elif renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                    call Girl_Breasts_Launch(Girl,0,0) #call expression Girl.Tag + "_Breasts_Launch" pass (Trigger,0)
            else:
                    call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                    $ Speed = 2
            $ Girl.Spunk.append("hand")
            "Она улыбается и начинает усиленно вам дрочить, поставив свою левую руку напротив головки. Затем вы кончаете ей на руку."
        else:
            #if Female
            if renpy.showing(Girl.Tag+"_Doggy_Animation") or renpy.showing(Girl.Tag+"_SexSprite"): #if renpy.showing("Rogue_Doggy"):
                    call expression Girl.Tag+"_Doggy_Reset"
                    call expression Girl.Tag+"_Sex_Reset"
                    call expression Girl.Tag+"_Finger_Launch" pass ("cum")
                    if Trigger == "hotdog":
                        "Она наклоняется и начинает ласкать вас."
                    else:
                        "Она усмехается, подается назад со звонким 'чпоком', а затем начинает с усердием вам дрочить."
                    $ Speed = 2
            elif renpy.showing(Girl.Tag+"_BJ_Animation") or renpy.showing(Girl.Tag+"_69_Animation"): #if renpy.showing("Rogue_BJ_Animation"):
                    call expression Girl.Tag+"_Finger_Launch" pass ("cum")
                    $ Speed = 2
                    "Она отрывает губы от вашего резинового члена и начинает ласкать вас."
            elif renpy.showing(Girl.Tag+"_CUN_Animation") or renpy.showing(Girl.Tag+"_69_CUN"): #if renpy.showing("Rogue_BJ_Animation"):
                    call expression Girl.Tag+"_Finger_Launch" pass ("cum")
                    $ Speed = 2
                    "Она отстраняется от вашей киски и начинает ласкать вас."
            else:
                    call expression Girl.Tag+"_Finger_Launch" pass ("cum")
                    $ Speed = 2
            $ Girl.Spunk.append("hand")
            "Она улыбается и ускоряет свои движения, лаская ваш клитор."
        $ Speed = 0

        if Girl.Addict > 80 or "hungry" in Girl.Traits:
                $ Girl.Eyes = "manic"
                $ Girl.Spunk.remove("hand")
                $ Girl.Spunk.append("mouth")
                $ Girl.Mouth = "smile"
                "С довольной улыбкой она начиста вылизывает свою руку."
                $ Girl.Spunk.remove("mouth")
                call AnyLine(Girl,"Хммм. . .")
        else:
                $ Girl.FaceChange("bemused")
                $ Girl.Spunk.remove("hand")
                "Она вытирает руку, но после этого слегка нюхает ее и расплывается в улыбке."
                call Sex_Basic_Dialog(Girl,"warned") #"Thanks for the heads up."
                jump Girl_Orgasm_After

#Start Swallowed  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Swallowed:  #rkeljsvg
        $ Girl.Swallow += 1
        $ Girl.Statup("Inbt", 50, 3)
        $ Girl.Addict -= 20
        if "mouth" in Girl.Spunk:
                $ Girl.Spunk.remove("mouth")
        if not Player.Male:
                pass
        elif "full" not in Girl.RecentActions and Girl.RecentActions.count("swallowed") >= 5:
                $ Girl.RecentActions.append("full")
                $ Girl.FaceChange("surprised", 1)
                if Girl is RogueX:
                        ch_r "-бууррпп-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_r "Пр'ти, [Girl.Petname], наверное, я что-то не то съела."
                elif Girl is KittyX:
                        ch_k "-бууррпп-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_k "Я. . . похоже, придется немного сократить количество."
                elif Girl is EmmaX:
                        ch_e "-бууррпп-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_e "Извиняюсь, [Girl.Petname], Я плотно поела."
                elif Girl is LauraX:
                        ch_l "-бууррпп-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_l "Уфф, [Girl.Petname], похоже, я что-то не то съела."
                elif Girl is JeanX:
                        $ Girl.Blush = 2
                        ch_j "-бууррпп-"
                        if ApprovalCheck(Girl, 600, "L"):
                                $ Girl.FaceChange("sexy", 1)
                                ch_j "Ха. . . я переполнена. . ."
                        else:
                                $ Girl.FaceChange("bemused", 1,Eyes="side")
                                $ Girl.Statup("Obed", 200, 3)
                                if not Player.Male:
                                    ch_j "Эм, ты этого не слышала. . ."
                                else:
                                    ch_j "Эм, ты этого не слышал. . ."
                elif Girl is StormX:
                        ch_s "-бууррпп-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_s "Ох, [Girl.Petname], должно быть, с меня хватит. . ."
                elif Girl is JubesX:
                        ch_v "-кашель-"
                        $ Girl.FaceChange("sexy", 1)
                        ch_v "Фух, думаю, возможно, я выпила больше, чем следовало бы. . ."
                elif Girl is GwenX:
                        ch_g "Воу. . . подожди. . ."
                        ch_g "-бууррпп-"
                        $ Girl.FaceChange("sadside", 1,Mouth="smirk")
                        ch_g "Это. . . было много. . ."
                elif Girl is BetsyX:
                        ch_b "Ох, дорогуша. . ."
                        ch_b "-бууррпп-"
                        $ Girl.FaceChange("sadside", 1,Mouth="smirk")
                        ch_b "Прошу прощения за мои манеры. . ."
                elif Girl is DoreenX:
                        ch_d "Ох, ого. . ."
                        ch_d "-бууррпп-"
                        $ Girl.FaceChange("sadside", 1,Mouth="smirk")
                        ch_d "Извини. . ."
                elif Girl is WandaX:
                        ch_w "Ох. . ."
                        ch_w "-бууррпп-"
                        $ Girl.FaceChange("sadside", 1,Mouth="smirk")
                        ch_w "Думаю, я выпила слишком много. . ."
        $ Girl.RecentActions.append("swallowed")
        $ Girl.DailyActions.append("swallowed")
        $ Girl.Addictionrate += 2
        if "addictive" in Player.Traits:
                $ Girl.Addictionrate += 2
        if Trigger == "anal":
                $ Girl.Statup("Obed", 50, 2)
                $ Girl.Statup("Obed", 200, 2)
        if Girl.Swallow == 1:
                $ Girl.SEXP += 12
                $ Girl.Statup("Inbt", 70, 5)
        jump Girl_Orgasm_After

#Start Creampied  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Creampied:
        if Trigger == "sex":
                $ Girl.CreamP += 1
                $ Girl.Statup("Lust", 200, 10)
                $ Girl.RecentActions.append("creampie sex")
                $ Girl.DailyActions.append("creampie sex")
                if Girl.CreamP == 1:
                        $ Girl.SEXP += 10
                        $ Girl.Statup("Inbt", 70, 5)
        elif Trigger == "anal":
                $ Girl.CreamA += 1
                $ Girl.Statup("Lust", 200, 5)
                $ Girl.RecentActions.append("creampie anal")
                $ Girl.DailyActions.append("creampie anal")
                if Girl.CreamA == 1:
                        $ Girl.SEXP += 12
                        $ Girl.Statup("Inbt", 70, 8)
        $ Girl.Statup("Inbt", 50, 3)
        $ Girl.Addict -= 30
        $ Girl.Addictionrate += 2
        if "addictive" in Player.Traits:
                $ Girl.Addictionrate += 3

# Clean-up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Girl_Orgasm_After:
        $ Line = "Что дальше?"
        if not renpy.showing(Girl.Tag+"_HJ_Animation"):
                $ Girl.ArmPose = 1
        $ Player.Semen -= 1
        $ Player.Focus = 0
        $ Speed = 0
        $ Girl.Thirst -= 10 if Girl.Thirst > 50 else 5
        if CleanUp:
                call Girl_CleanCock
        else:
            menu:
                "Хотите, чтобы [Girl.Name] привела вас в порядок?"
                "Да":
                        call Girl_CleanCock
                "Пусть [Partner.Name] этим займется." if Partner in TotalGirls:
                        call Shift_Focus(Partner) #makes the partner the lead and the lead the partner
                        call AllReset(Partner) #resets the position of the original lead
                        call Girl_CleanCock(Ch_Focus) #Does the cleanup focused on the original Partner

                        call Shift_Focus(Partner) #makes the original partner the partner again
                        call AllReset(Partner)  #resets the position of the partner

                        "[Partner.Name] отстраняется."

                        call AllReset(Girl) #resets the position of the original lead
                "Нет":
                        pass
        if Girl.Spunk:
                        call Girl_Cleanup(Girl)
        $ Girl.FaceChange("sexy", 1)
        $ Situation = 0
        return

label Girl_CleanCock(Girl=0):
        $ Girl = GirlCheck(Girl)
        $ Line = "Что дальше?"
        if not renpy.showing(Girl.Tag+"_HJ_Animation") and renpy.showing(Girl.Tag+"_Finger_Animation"):
                $ Girl.ArmPose = 1
        $ Player.Cock = "out"
        $ Speed = 0
        if Trigger == "anal" and not ApprovalCheck(Girl, 1600, TabM=1) and not Girl.Addict >= 80 and Player.Male:
                if Girl is JeanX:
                        $ Girl.FaceChange("sly", 1,Eyes="psychic")
                        if not Player.Male:
                            "Вы чувствуете легкий ветерок и все выделения стекают с вашей киски на пол."
                        else:
                            "Вы чувствуете легкий ветерок и все выделения стекают с вашего члена на пол."
                        $ Girl.FaceChange("sly", 0)
                else:
                        if not Player.Male:
                            "Она вытирает вашу киску начисто."
                        else:
                            "Она вытирает ваш член начисто."
        elif Girl.Blow > 3 or Girl.CUN > 3 or Girl.Swallow:
                if ApprovalCheck(Girl, 1200, TabM=1) or Girl.Addict >= 60:
                        if Player.Male:
                                call expression Girl.Tag+"_BJ_Launch" pass ("cum")
                        else:
                                call expression Girl.Tag+"_CUN_Launch" pass ("cum")
                        $ Speed = 1
                        $ Girl.FaceChange("sucking", 1)
                        if ApprovalCheck(Girl, 1500, TabM=1):
                            if Partner and ApprovalCheck(Partner, 1500, TabM=1):
                                    if not Player.Male:
                                        "Обе девушки смотрят на вас, пока вылизывают вашу киску начисто."
                                    else:
                                        "Обе девушки смотрят на вас, пока вылизывают ваш член начисто."
                            elif Girl.Obed > Girl.Inbt:
                                    if not Player.Male:
                                        "Она смотрит на вас с любовью, пока вылизывает вашу киску начисто."
                                    else:
                                        "Она смотрит на вас с любовью, пока вылизывает ваш член начисто."
                                    $ Girl.Statup("Obed", 80, 3)
                            else:
                                    if not Player.Male:
                                        "Она с удовольствием вылизывает вашу киску начисто."
                                    else:
                                        "Она с удовольствием вылизывает ваш член начисто."
                        elif Girl.Addict >= 60:
                                    if not Player.Male:
                                        "Она жадно и тщательно вылизывает вашу киску."
                                    else:
                                        "Она жадно и тщательно вылизывает ваш член."
                        else:
                                    if not Player.Male:
                                        "Она начисто вылизывает вашу киску."
                                    else:
                                        "Она начисто вылизывает ваш член."
                        $ Girl.FaceChange("sexy")
                else:
                        if Player.Male:
                                if not renpy.showing(Girl.Tag+"_HJ_Animation"):
                                        call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                        else:
                                if not renpy.showing(Girl.Tag+"_Finger_Animation"):
                                        call expression Girl.Tag+"_Finger_Launch" pass ("cum")
                        if Partner and ApprovalCheck(Partner, 1000, TabM=1):
                                    if not Player.Male:
                                        "Обе девушки наклоняются и вытирают вашу киску начисто."
                                    else:
                                        "Обе девушки наклоняются и вытирают ваш член начисто."
                        else:
                                    if not Player.Male:
                                        "Она вытирает вашу киску начисто."
                                    else:
                                        "Она вытирает ваш член начисто."
        else:
                        if renpy.showing(Girl.Tag+"_PJ_Animation"): #if renpy.showing("Rogue_PJ_Animation"):
                                pass
                        elif not renpy.showing(Girl.Tag+"_HJ_Animation") and Player.Male:
                                call expression Girl.Tag+"_HJ_Launch" pass ("cum")
                        elif not renpy.showing(Girl.Tag+"_Finger_Animation") and not Player.Male:
                                call expression Girl.Tag+"_Finger_Launch" pass ("cum")
                        if Partner and ApprovalCheck(Partner, 1000, TabM=1):
                                    if not Player.Male:
                                        "Обе девушки наклоняются и вытирают вашу киску начисто."
                                    else:
                                        "Обе девушки наклоняются и вытирают ваш член начисто."
                        else:
                                    if not Player.Male:
                                        "Она вытирает вашу киску начисто."
                                    else:
                                        "Она вытирает ваш член начисто."
        $ Player.Spunk = 0
        $ Girl.FaceChange("sexy")
        if Trigger in ("fondle breast","suck breast"):
                call ViewShift(Girl,"breasts")
        elif Trigger in ("fondle pussy","lick pussy","fondle ass","insert ass","lick ass","fondle thighs"):
                call ViewShift(Girl,"pussy")
        elif Trigger == "strip":
                call AllReset(Girl)
                $ renpy.show(Girl.Tag+"_Sprite",at_list=[Girl_Dance1(Girl)],zorder=Girl.Layer)  #        if Girl is RogueX: #show Rogue_Sprite at Girl_Dance1(Girl)
                "[Girl.Name] снова начинает танцевать."
        return

# End You Cumming //////////////////////////////////////////////////////////////////////////////////


#  Girl's Orgasms / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Girl_Cumming(Girl=0,Quick=0,BO=[],BonusQueue=[]): #rename from Girl_Cumming  #rkeljsvg
    # call Girl_Cumming(Girl,0)
    if Girl not in TotalGirls: #should remove "character don't exist" errors
            return

    $ Girl.DrainWord("gonnafap",1,1,0)  #removes these flags when you've had sex
    $ Girl.DrainWord("wannafap",1,1,0)

    if Girl.Loc == "bg teacher" and bg_current == "bg classroom":
            pass
    elif Girl.Loc != bg_current and "phonesex" not in Player.RecentActions:
            #if she's not even in the room. . .
            $ Girl.Lust = 25
            return
    $ Girl.Eyes = "surprised"
    $ Girl.Brows = "sad"
    if Girl in (EmmaX,LauraX):
            $ Girl.Mouth = "tongue"
    else:
            $ Girl.Mouth = "sucking"
    $ Girl.Blush = 1

    call AnyLine(Girl,". . . !")
#    $ Speed = 0

    call Punch

    $ Speed = 1
    $ Line = renpy.random.choice([Girl.Name + " внезапно сотрясается от спазмов, она изо всех сил старается сдержать непроизвольный крик, но безуспешно.",
                Girl.Name + " крепко прижимается к вам, в то время как по ее телу проходит дрожь от экстаза.",
                Girl.Name + " вдруг останавливается и издает тихий стон.",
                Girl.Name + " внезапно вздрагивает и так же внезапно замирает."])
    "[Line]"
    $ Girl.Thirst = int(Girl.Thirst/2)
    $ Girl.Thirst -= 5

    $ Girl.OCount += 1
    $ Girl.Org += 1
    $ Girl.Lust = 30 if "hotblooded" in Girl.Traits else 0
    $ Girl.Lust += (Girl.OCount * 5)
    $ Girl.Lust = 60 if Girl.Lust >= 60 else Girl.Lust
    $ Girl.Statup("Inbt", 50, 1)
    $ Girl.Statup("Inbt", 70, 1)

    if Quick:
            $ Girl.FaceChange("sexy", 2)
            return
    elif Girl.OCount > 5:
            $ Girl.FaceChange("sexy", 2,Eyes="stunned")
            call AnyLine(Girl,"Мммм. . .")
            return

    $ Girl.Eyes = "closed"
    $ Girl.Brows = "sad"
    $ Girl.Mouth = "tongue"
    if Girl is RogueX:
            $ Line = renpy.random.choice(["Вау. . .  просто, вау.",
                "Не знаю что на меня нашло. . .",
                "Ммммм. . . .",
                "Мне было приятно. Очень приятно."])
    elif Girl is KittyX:
            $ Line = renpy.random.choice(["Вау. . .  просто, вау.",
                "Это было потрясающе!",
                "Мммм. . . .",
                "Мне понравилось!"])
    elif Girl is EmmaX:
            $ Line = renpy.random.choice(["Ооооох. . . прекрасно.",
                "Мне очень понравилось. . .",
                "Мммм. . . .",
                "Это было. . . великолепно. . ."])
    elif Girl is LauraX:
            $ Line = renpy.random.choice(["Ооооох. . .",
                "Мне было очень хорошо. . .",
                "Ммммм. . . .",
                "Это было. . . ох. . ."])
    elif Girl is JeanX:
            $ Line = renpy.random.choice(["Ооооох. . .",
                "Ах, то что нужно. . .",
                "Ммммм. . . .",
                "Уф, так приятно. . ."])
    elif Girl is StormX:
            $ Line = renpy.random.choice(["Ооооох. . .",
                "Мммммммммм. . .",
                "Ммммм. . . .",
                "Это было просто. . . удивительно. . ."])
    elif Girl is JubesX:
            $ Line = renpy.random.choice(["Ооох. . .",
                "Огооо. . .",
                "Мммм. . . .",
                "Чудесно. . ."])
    elif Girl is GwenX:
            $ Line = renpy.random.choice(["Оооох. . .",
                "Чууууудно. . .",
                "Мммммм. . . .",
                "Ты умеешь, эм. . ."])
    elif Girl is BetsyX:
            $ Line = renpy.random.choice(["Оооох. . .",
                "Nnnnmmmmaaaaahhh. . .",
                "Ммммм. . . .",
                "Это было. . . очень приятно. . ."])
    elif Girl is DoreenX:
            ch_d "Oh, wow. . ."
            $ Line = renpy.random.choice(["Оооох. . .",
                "Нннмммаааааххх. . .",
                "Ммммм. . . .",
                "Ооох. . . у меня нет слов. . ."])
    elif Girl is WandaX:
            $ Line = renpy.random.choice(["Оооохх. . .",
                "Нннмммаааааххх. . .",
                "Хмммммм. . . .",
                "Оооох. . . спасибо. . ."])
    call AnyLine(Girl,Line)

    if "unsatisfied" in Girl.RecentActions:  #If she had been unsatisfied, you satisfied her. . .
            $ Girl.Statup("Love", 70, 2)
            $ Girl.Statup("Love", 90, 1)
            if "unsatisfied" in Girl.DailyActions:
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Ну ладно, считай, что ты исправилась, [Girl.Petname]."
                            else:
                                ch_r "Ну ладно, считай, что ты исправился, [Girl.Petname]."
                    elif Girl is KittyX:
                            ch_k "Можешь ведь, если захочешь."
                    elif Girl is EmmaX:
                            ch_e "Исправляешься, [Girl.Petname]?"
                    elif Girl is LauraX:
                            ch_l "Похоже, ты исправляешься, [Girl.Petname]?"
                    elif Girl is JeanX:
                            $ Girl.Statup("Obed", 50, 6)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Obed", 90, 2)
                            ch_j "-Наконец-то.-"
                    elif Girl is StormX:
                            ch_s "Думаю, это сблизило нас, [Girl.Petname]."
                    elif Girl is JubesX:
                            ch_v "Значит, ты -знаешь- как заставить девушку чувствовать себя хорошо."
                    elif Girl is GwenX:
                            ch_g "Ну, это стоило того, чтобы подождать. . ."
                    elif Girl is BetsyX:
                            ch_b "Ты точно знаешь, как выразить свою признательность. . ."
                    elif Girl is DoreenX:
                            ch_d "Это стоило ожиданий. . ."
                    elif Girl is WandaX:
                            ch_w "Ох, теперь мне стало спокойнее. . ."
            $ Girl.DrainWord("unsatisfied")
    $ Line = 0

    if Trigger == "masturbation":
            $ Girl.FaceChange("sexy", 2)
    else:
            if Girl.OCount == 1:
                    # if she's angry, but not too angry, then reduce that on the first O of the time block.
                    $ Girl.ForcedCount -= 1 if 5 > Girl.ForcedCount > 0 else 0
            $ Girl.Statup("Lust", 40, 1)
            $ Girl.Statup("Love", 70, 1)
            $ Girl.Statup("Love", 90, 1)
            $ Girl.Statup("Obed", 50, 2,Alt=[[JeanX],900,5]) #+5 for Jean
            $ Girl.Statup("Obed", 70, 2)

            #checks to check reaction of other girls
            $ BO = TotalGirls[:]
            $ BO.remove(Girl)
            python:
                for BX in BO:
                    if BX.Loc == bg_current and "noticed "+Girl.Tag in BX.RecentActions:
                            BX.Lust += 15 if BX.GirlLikeCheck(Girl) >= 500 else 10
                            BX.Lust += 5 if BX.Les >= 5 else 0
                            if BX.Lust >= 100:
                                    BonusQueue.append(BX)
                                    #call Girl_Cumming(BX,1) #calls quick version
            while BonusQueue:
                    call Girl_Cumming(BonusQueue[0],1) #calls quick version
                    $ BonusQueue.remove(BonusQueue[0])

            #Orgasm count
            if (Trigger == "blow" or Trigger == "hand") and not Trigger2:
                pass
            elif Partner != Girl:
                if Girl.OCount == 2:
                        $ Girl.Brows = "confused"
                        if Girl is RogueX:
                                ch_r "Вау. . . это было потрясающе. . ."
                        elif Girl is KittyX:
                                ch_k "Ммм. . . так. . . хорошо."
                        elif Girl is EmmaX:
                                ch_e "Отличная работа, [Girl.Petname]. . ."
                        elif Girl is LauraX:
                                ch_l "Эй, хорошая работа, [Girl.Petname]. . ."
                        elif Girl is JeanX:
                                ch_j "Мне нравится такое твое отношение к делу. . ."
                        elif Girl is StormX:
                                ch_s "Прекрасная работа, [Girl.Petname]."
                        elif Girl is JubesX:
                                ch_v "Ох, прямо в точку. . ."
                        elif Girl is GwenX:
                                ch_g "Мммм. . . спасибо. . ."
                        elif Girl is BetsyX:
                                ch_b "Как приятно, [Girl.Petname]. . ."
                        elif Girl is DoreenX:
                                ch_d "Это было. . . очень здорово, [Girl.Petname]. . ."
                        elif Girl is WandaX:
                                ch_w "Спасибо, это было очень здорово, [Girl.Petname]. . ."
                        $ Girl.Statup("Love", 50, 1)
                        $ Girl.Statup("Love", 80, 2)
                        $ Girl.Statup("Obed", 50, 1)
                        $ Girl.Statup("Obed", 60, 1)
                elif Girl.OCount == 3: #5
                        $ Girl.Brows = "confused"
                        if Girl is RogueX:
                                ch_r "Ты. . . все. . . еще. . . можешь. . . продолжать. . . да?"
                        elif Girl is KittyX:
                                ch_k "Ты. . . меня. . . загоняешь. . ."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "А . . . ты. . . выносливая. . ."
                                else:
                                    ch_e "А . . . ты. . . выносливый. . ."
                        elif Girl is LauraX:
                                ch_l "Ты определенно. . . можешь. . . не отставать. . ."
                        elif Girl is JeanX:
                                $ Girl.Statup("Love", 90, 3)
                                ch_j "Эй. . . очень хорошая работа. . ."
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "Ты очень. . . предана делу. . . [Girl.Petname]."
                                else:
                                    ch_s "Ты очень. . . предан делу. . . [Girl.Petname]."
                        elif Girl is JubesX:
                                if not Player.Male:
                                    ch_v "Ты, эм, такая выносливая, м?"
                                else:
                                    ch_v "Ты, эм, такой выносливый, м?"
                        elif Girl is GwenX:
                                ch_g "Ох. . . спасибо. . . все было. . . хорошо. . ."
                        elif Girl is BetsyX:
                                ch_b "Весьма впечатляюще, [Girl.Petname]. . ."
                        elif Girl is DoreenX:
                                ch_d "Спасибо. . . [Girl.Petname]. . ."
                        elif Girl is WandaX:
                                ch_w "Оох, еще раз спасибо, [Girl.Petname]. . ."
                        $ Girl.Statup("Love", 50, 2)
                        $ Girl.Statup("Love", 80, 2)
                        $ Girl.Statup("Obed", 30, 1)
                        $ Girl.Statup("Obed", 50, 1)
                elif Girl.OCount == 5: #10
                    $ Girl.Mouth = "tongue"
                    if Girl is RogueX:
                            ch_r "Серьезно . . . я. . .  начинаю. . . уставать . . ."
                            ch_r "давай. . . может. . . немного. . . передохнем?"
                    elif Girl is KittyX:
                            ch_k "Я . . . правда. . . начинаю. . . уставать. . ."
                            ch_k "мы. . . можем. . . сделать. . . перерыв?"
                    elif Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Ты . . . меня. . . совсем. . . загоняла. . ."
                            else:
                                ch_e "Ты . . . меня. . . совсем. . . загонял. . ."
                            ch_e "ты. . . не. . . против. . . сделать. . . перерыв?"
                    elif Girl is LauraX:
                            ch_l "Обычно. . . меня. . . так. . . просто. . . не. . . измотать. . ."
                            ch_l "мы. . . можем. . . сделать. . . перерыв?"
                    elif Girl is JeanX:
                            $ Girl.Statup("Love", 50, 5)
                            ch_j "Ох. . . Я немного. . ."
                            $ Girl.Statup("Love", 90, 3)
                            ch_j "Может. . . пока хватит?"
                    elif Girl is StormX:
                            ch_s "Возможно. . . пока. . . этого достаточно. . . [Girl.Petname]?"
                    elif Girl is JubesX:
                            ch_v "Мне. . . эм. . . нравится наше. . . занятие. . ."
                            if not Player.Male:
                                ch_v "Но. . . эм. . . возможно, ты бы могла. . . позволить мне. . . перевести дух?"
                            else:
                                ch_v "Но. . . эм. . . возможно, ты бы мог. . . позволить мне. . . перевести дух?"
                    elif Girl is GwenX:
                            if not Player.Male:
                                ch_g "Воу. . . эм. . . мы знаем, на что ты способна. . ."
                            else:
                                ch_g "Воу. . . эм. . . мы знаем, на что ты способен. . ."
                            ch_g ". . . и это. . . пугает. . ."
                            ch_g "-давай отдохнем. . ."
                    elif Girl is BetsyX:
                            ch_b "Ох, дорогуша. . . Я должна воспользоваться моментом и отметить. . ."
                            ch_b ". . ."
                            ch_b "У тебя настоящий талант к сексу. . ."
                    elif Girl is DoreenX:
                            ch_d "Ох. . . ого. . ."
                            ch_d "Тебе, эм. . . не стоит продолжать. . ."
                            ch_d "Я думаю. . . с меня хватит. . ."
                    elif Girl is WandaX:
                            ch_w "Эм. . ."
                            ch_w "Слушай. . . думаю, этого достаточно. . ."
                            ch_w "Мы можем немного притормозить?"
                    menu:
                        extend ""
                        "Закончить." if Player.FocusX:
                            "Вы прекращаете концентрироваться. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                        "Давай попробуем что-нибудь другое." if MultiAction:
                            $ Situation = "shift"
                        "Нет, я еще не все.":
                            if Trigger == "sex" or Trigger == "anal":
                                if ApprovalCheck(Girl, 1000, TabM=1) or ApprovalCheck(Girl, 400, "O", TabM=1):
                                    $ Girl.Statup("Love", 200, -5)
                                    $ Girl.Statup("Obed", 50, 2,Alt=[[JeanX],900,5]) #+5 for Jean
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Eyes = "stunned"
                                    "Она через какое-то время начинает нечленораздельно мычать."
                                else:
                                    $ Girl.FaceChange("angry", 1)
                                    if Player.Male:
                                            "Бросив на вас злой взгляд, она соскакивает с вас и начинает приводить себя в порядок."
                                    else:
                                            "Она хмуро смотрит на тебя, отстраняется и вытирается."
                                    if Girl is RogueX:
                                            if not Player.Male:
                                                ch_r "С таким отношением справляйся сама."
                                            else:
                                                ch_r "С таким отношением справляйся сам."
                                    elif Girl is KittyX:
                                            ch_k "Похоже, тебе все-таки придется остановиться. . ."
                                    elif Girl is EmmaX:
                                            if not Player.Male:
                                                ch_e "Ты должна понимать, когда стоит остановиться. . ."
                                            else:
                                                ch_e "Ты должен понимать, когда стоит остановиться. . ."
                                    elif Girl is LauraX:
                                            ch_l "Ну, я все. . ."
                                    elif Girl is JeanX:
                                            ch_j ". . ."
                                            ch_j "У меня сейчас нет на это времени."
                                    elif Girl is StormX:
                                            ch_s "Хотела бы я справиться, [Girl.Petname], но увы."
                                    elif Girl is JubesX:
                                            ch_v "Нуу, эм. . . я все."
                                    elif Girl is GwenX:
                                            ch_g "Хм. В общем, я все. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Что ж, это весьма печально."
                                    elif Girl is DoreenX:
                                            ch_d "Ох. . . безумие. . ."
                                    elif Girl is WandaX:
                                            ch_w "Эм. . . ладно. . ."
                                    $ Girl.Statup("Love", 50, -3, 1)
                                    $ Girl.Statup("Love", 80, -4, 1)
                                    $ Girl.Statup("Obed", 30, -1, 1,Alt=[[JeanX],300,5]) #+5 for Jean
                                    $ Girl.Statup("Obed", 50, -1, 1,Alt=[[JeanX],900,5]) #+5 for Jean
                                    $ Girl.RecentActions.append("angry")
                                    $ Girl.DailyActions.append("angry")
                            else:
                                    $ Girl.Statup("Obed", 50, 3,Alt=[[JeanX],900,5]) #+5 for Jean
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Eyes = "stunned"
                                    "Она через какое-то время начинает нечленораздельно мычать."
                #end Ocount stuff
    if Trigger == "strip":
            call AllReset(Girl)
            $ renpy.show(Girl.Tag+"_Sprite",at_list=[Girl_Dance1(Girl)],zorder=Girl.Layer)
            #if Girl is RogueX:  #show Rogue_Sprite at Girl_Dance1(RogueX)
            "[Girl.Name] снова начинает танцевать."
    return

# End Girl's Orgasm /////////////////////////////////////////////////////////////////////////////////////


# Start Girl Clean-Up /////////////////////////////////////////////////////////////////////////////////////
label Girl_Cleanup(Girl=0,Choice = "random",Options=[],Cnt=0,Cleaned=0,Original=0): #rkeljsvg
    if Girl not in TotalGirls or ("painted" in Girl.RecentActions and Choice != "ask"): #should remove "character don't exist" errors
            return
    if Choice == "after":
            # This is at the end of a session
            if not Girl.Spunk:
                $ Girl.Wet = 0
                return
            $ Cnt = 1
            $ Tempmod = 0

    if Girl.Addict > 80 and Girl.Swallow:
            #if she likes cum, she prefers to eat it.
            $ Choice = "eat"
            $ Girl.Eyes = "manic"
            $ Girl.Mouth = "smile"
    elif Girl is EmmaX and "taboo" not in EmmaX.History and Cnt:
            #Emma won't go around like this unless past her barrier
            $ Choice = "clean"
    elif Choice == "ask":
            pass
    elif "painted" in Girl.RecentActions and ApprovalCheck(Girl, 1000, "OI"):
            return
    elif ApprovalCheck(Girl, 1200, "LO"):
            $ Choice = "ask"
    elif not ApprovalCheck(Girl, 400, "I"):
            $ Girl.FaceChange("bemused")
            $ Choice = "clean2"
    elif not Cnt and not CleanUpDefault:
            $ Choice = "random"
    else:
            $ Choice = "ask"

    $ Cleaned = 1 if "cleaned" in Girl.DailyActions else 0
    $ Girl.RecentActions.append("cleaned")
    $ Girl.DailyActions.append("cleaned")

    if Ch_Focus != Girl:
            # if Girl isn't the lead, swap to her.
            if Original in TotalGirls:
                    $ Original = Partner
            else:
                    $ Original = Girl
            call Shift_Focus(Girl)

    if CleanUpDefault and Choice == "ask" and CleanUpDefault != "ask":
            #sets the Choice to the default if there is one, and it is not ask
            if not Partner and CleanUpDefault == "partner lick":
                    $ Choice = "eat"
            elif not Partner and CleanUpDefault == "partner wipe":
                    $ Choice = "clean"
            else:
                    $ Choice = CleanUpDefault
    elif Choice == "ask":
            #otherwise asks
            if not Player.Male:
                "[Girl.Name] смотрит вниз на все те соки, которыми она покрыта плотным слоем."
            else:
                "[Girl.Name] смотрит вниз на всю ту сперму, которой она покрыта плотным слоем."
            menu:
                "Предложите [Girl.Name_dat] привести себя в порядок?"
                "Тебе стоит оставить все как есть.":
                            $ Choice = "leave"
                "Ты должна все съесть." if Player.Male:
                            $ Choice = "eat"
                "Ты должна просто все убрать.":
                            $ Choice = "clean"
                "Слушай, [Partner.Name], слижи все с нее." if Partner:
                            $ Choice = "partner lick"
                "Слушай, [Partner.Name], вытри ее." if Partner:
                            $ Choice = "partner wipe"
                "Ничего не говорить. [[оставить решение за ней]":
                            $ Choice = "random"
    #end "asked"

    if Choice == "leave":
            if CleanUpDefault and CleanUpDefault != "leave":
                    ch_p "Можешь."
            else:
                    ch_p "Тебе стоит оставить все как есть."
            if not Cnt:
                # If this isn't the end of the session
                $ Girl.FaceChange("sly")
                if ApprovalCheck(Girl, 300, "I") or ApprovalCheck(Girl, 1000):
                        $ Girl.Statup("Obed", 70, 1)
                        $ Girl.Statup("Inbt", 50, 1)
                        $ Girl.Statup("Lust", 90, 2)
                        if Girl is RogueX:
                                ch_r "Хех, ладно, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k "Ох, ладно."
                        elif Girl is EmmaX:
                                ch_e "Ммм. . ."
                        elif Girl is LauraX:
                                ch_l "Ммм. . ."
                        elif Girl is JeanX:
                                ch_j "Конечно. . ."
                        elif Girl is StormX:
                                ch_s "Ох, пожалуй, можно все оставить, [Girl.Petname]."
                        elif Girl is JubesX:
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.FaceChange("sad")
                                ch_v "Нууу, эм. . . Можно. . ."
                        elif Girl is GwenX:
                                ch_g "А? Ладно. . ."
                        elif Girl is BetsyX:
                                ch_b "О, в самом деле?"
                        elif Girl is DoreenX:
                                ch_d "А? . . ладно. . ."
                        elif Girl is WandaX:
                                ch_w "Хех. . . ладно. . ."
                else:
                        $ Choice = "clean"
                        if Girl is RogueX:
                                ch_r "Фу, я слишком грязная."
                        elif Girl is KittyX:
                                ch_k "Эм, нет."
                        elif Girl is EmmaX:
                                ch_e "Я буду выглядеть слишком неприлично, [Girl.Petname]."
                        elif Girl is LauraX:
                                ch_l "Эм, я не люблю грязь, [Girl.Petname]."
                        elif Girl is JeanX:
                                ch_j "Я не в настроении для такого, [Girl.Petname]."
                        elif Girl is StormX:
                                ch_s "Это было бы немного грязно, [Girl.Petname]."
                        elif Girl is JubesX:
                                $ Girl.FaceChange("sad")
                                ch_v "Мне, эм. . . не хотелось бы оставлять беспорядок. . ."
                        elif Girl is GwenX:
                                ch_g "Эм, я не хочу. . ."
                        elif Girl is BetsyX:
                                ch_b "Боюсь, что нет."
                        elif Girl is DoreenX:
                                ch_d "А? . . Я так не думаю. . ."
                        elif Girl is WandaX:
                                ch_w "Эм. . . Я так не думаю. . ."

            #This is the end of session. . .
            elif ApprovalCheck(Girl, 900, "I") or "exhibitionist" in Girl.Traits:
                        $ Girl.Statup("Obed", 70, 2)
                        $ Girl.Statup("Obed", 90, 1)
                        $ Girl.Statup("Lust", 90, 5)
                        $ Girl.FaceChange("sly")
                        if Girl is RogueX:
                                ch_r "Оох, мне нравится ход твоих мыслей . . . "
                        elif Girl is KittyX:
                                ch_k "Оох, мне нравится ход твоих мыслей. . . "
                        elif Girl is EmmaX:
                            if Player.Male:
                                ch_e "Ммм. . . Полагаю, мне это не помешает. . "
                            else:
                                ch_e "Ммм. . . Полагаю, мне это не помешает. . "
                        elif Girl is LauraX:
                                ch_l "Ммм. . . Мне нравится, как она блестит. . "
                        elif Girl is JeanX:
                                ch_j "Ммм. . . ладно."
                        elif Girl is StormX:
                                ch_s "Можно и так, [Girl.Petname]. . ."
                        elif Girl is JubesX:
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.FaceChange("sad")
                                ch_v "Ох, эм. . . Думаю, я могла бы. . ."
                        elif Girl is GwenX:
                                ch_g "А? Ладно. . . Хах."
                        elif Girl is BetsyX:
                                ch_b "Это довольно смело. . ."
                        elif Girl is DoreenX:
                                ch_d "А? . . ооохх, ладно. . ."
                        elif Girl is WandaX:
                                ch_w "Конечно. . ."
            elif ApprovalCheck(Girl, 600, "I") and ApprovalCheck(Girl, 1200, "LO",Alt=[[JubesX],1500]):
                        $ Girl.Statup("Obed", 90, 1)
                        $ Girl.Statup("Inbt", 80, 1)
                        $ Girl.Statup("Lust", 90, 5)
                        $ Girl.FaceChange("surprised",2)
                        if Girl is RogueX:
                                ch_r "Ну, пожалуй, я могла бы. . ."
                        elif Girl is KittyX:
                                ch_k "Ну, может, я могла бы. . ."
                        elif Girl is EmmaX:
                                ch_e "Хмм. . . Если ты настаиваешь. . ."
                        elif Girl is LauraX:
                                ch_l "Хмм. . . Если ты настаиваешь. . ."
                        elif Girl is JeanX:
                                ch_j "Ммм. . . ладно."
                        elif Girl is StormX:
                                ch_s ". . . Хорошо."
                        elif Girl is JubesX:
                                $ Girl.FaceChange("sad")
                                ch_v "Ох, эм. . . Думаю, я могла бы. . ."
                        elif Girl is GwenX:
                                ch_g "А? Ооох, ладно. . ."
                        elif Girl is BetsyX:
                                ch_b "Это я могу. . ."
                        elif Girl is DoreenX:
                                ch_d "А? . . ох, может, я и согласна. . ."
                        elif Girl is WandaX:
                                ch_w "Эм. . . ладно. . ."
                        $ Girl.FaceChange("sly",1)
            else:
                #leave it on, permanently
                $ Girl.FaceChange("angry")
                $ Choice = "clean"
                if Girl is RogueX:
                        ch_r "Ты прикалываешься, что ли?!"
                elif Girl is KittyX:
                        $ Girl.Brows = "confused"
                        ch_k "Сейчас ты ведешь себя просто глупо!"
                elif Girl is EmmaX:
                        ch_e "Что-что, прости?"
                elif Girl is LauraX:
                        ch_l "Извини?"
                elif Girl is JeanX:
                        ch_j "Что?"
                elif Girl is StormX:
                        ch_s "Это было бы слишком, [Girl.Petname]."
                elif Girl is JubesX:
                        $ Girl.FaceChange("sad")
                        ch_v "Нууу. . . это было бы. . . грязно. . . ага."
                elif Girl is GwenX:
                        ch_g "Я, эм. . . совсем не хочу этого. . ."
                elif Girl is BetsyX:
                        ch_b "Это совершенно неуместно. . ."
                elif Girl is DoreenX:
                        ch_d "А? . . какой ужас. . ."
                elif Girl is WandaX:
                        ch_w "Ты, должно быть, шутишь. . ."
                menu:
                    extend ""
                    "Пожалуйста?":
                        if ApprovalCheck(Girl, 1800,Alt=[[JubesX],2200]):
                                $ Girl.Statup("Love", 85, 1)
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 80, 1)
                                $ Girl.Statup("Inbt", 40, 3)
                                $ Girl.Statup("Inbt", 80, 1)
                                if Girl is RogueX:
                                        ch_r "Ох, ну хорошо!"
                                elif Girl is KittyX:
                                        ch_k "Ох, ну хорошо!"
                                elif Girl is EmmaX:
                                        ch_e "Что ж. Ладно."
                                elif Girl is LauraX:
                                        ch_l "Ладно."
                                elif Girl is JeanX:
                                        ch_j "Ммм. . . ладно."
                                elif Girl is StormX:
                                        ch_s ". . . Хорошо."
                                elif Girl is JubesX:
                                        $ Girl.Statup("Love", 80, -2)
                                        ch_v ". . . хорошо. . ."
                                elif Girl is GwenX:
                                        ch_g "Ну. . . хорошо. . ."
                                elif Girl is BetsyX:
                                        ch_b "Если это так необходимо. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ну, ладно. . ."
                                elif Girl is WandaX:
                                        ch_w "Хорошо."
                                $ Choice = "leave"
                        elif Cleaned:
                                $ Girl.FaceChange("angry")
                                if Girl is RogueX:
                                        ch_r "Серьезно, хватит предлагать мне такое."
                                elif Girl is KittyX:
                                        ch_k "Серьезно, хватит предлагать мне подобное."
                                elif Girl is EmmaX:
                                        ch_e "Мне кажется, я достаточно ясно выразилась."
                                elif Girl is LauraX:
                                        ch_l "Я не в настроении для этого."
                                elif Girl is JeanX:
                                        ch_j "Прекращай, [Girl.Petname]."
                                elif Girl is StormX:
                                        ch_s "Я не могу."
                                elif Girl is JubesX:
                                        ch_v "Я не хочу!"
                                elif Girl is GwenX:
                                        if not Player.Male:
                                            ch_g "Хватит быть грубой. . ."
                                        else:
                                            ch_g "Хватит быть грубым. . ."
                                elif Girl is BetsyX:
                                        ch_b "Ох, веди себя прилично."
                                elif Girl is DoreenX:
                                        ch_d "Хватит спрашивать. . ."
                                elif Girl is WandaX:
                                        ch_w "Дай мне отдохнуть от этого. . ."
                        elif ApprovalCheck(Girl, 800):
                                $ Girl.Statup("Inbt", 50, 1)
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "А ты настойчивая, но все равно нет."
                                        else:
                                            ch_r "А ты настойчивый, но все равно нет."
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Нет, хоть ты и настойчивая."
                                        else:
                                            ch_k "Нет, хоть ты и настойчивый."
                                elif Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "А ты настойчивая, но нет."
                                        else:
                                            ch_e "А ты настойчивый, но нет."
                                elif Girl is LauraX:
                                        if not Player.Male:
                                            ch_l "Какая настойчивая, но все-равно нет."
                                        else:
                                            ch_l "Какой настойчивый, но все-равно нет."
                                elif Girl is JeanX:
                                        ch_j "Прекращай."
                                elif Girl is StormX:
                                        ch_s "Будь серьезней, [Girl.Petname]."
                                elif Girl is JubesX:
                                        ch_v "Нет!"
                                elif Girl is GwenX:
                                        ch_g "Ни за что."
                                elif Girl is BetsyX:
                                        ch_b "Конечно же нет."
                                elif Girl is DoreenX:
                                        ch_d "Ни за что."
                                elif Girl is WandaX:
                                        ch_w "Дай мне отдохнуть от этого. . ."
                        else:
                                $ Girl.Statup("Love", 75, -5)
                                $ Girl.Statup("Love", 40, -10)
                                $ Girl.Statup("Obed", 90, 2)
                                $ Girl.FaceChange("angry")
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Хватит строить из себя дурочку."
                                        else:
                                            ch_r "Хватит строить из себя придурка."
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Хватит строить из себя стерву."
                                        else:
                                            ch_k "Хватит строить из себя мудака."
                                elif Girl is EmmaX:
                                        ch_e "Конечно же я откажусь."
                                elif Girl is LauraX:
                                        ch_l "Ты должно быть шутишь."
                                elif Girl is JeanX:
                                        ch_j "Отъебись уже."
                                elif Girl is StormX:
                                        ch_s "Нет."
                                elif Girl is JubesX:
                                        ch_v "Ни за что! Я так решила!"
                                elif Girl is GwenX:
                                        ch_g "Как грубо. . ."
                                elif Girl is BetsyX:
                                        ch_b "Какой ужас."
                                elif Girl is DoreenX:
                                        ch_d "Иу. . ."
                                elif Girl is WandaX:
                                        ch_w "Ни за что. . ."
                    "Я настаиваю.":
                        $ Girl.FaceChange("sad")
                        if ApprovalCheck(Girl, 400, "I") and ApprovalCheck(Girl, 1200, "LO",Alt=[[JubesX],1500]):
                                $ Girl.Statup("Obed", 40, 3)
                                $ Girl.Statup("Obed", 90, 2)
                                if Girl is RogueX:
                                        ch_r "Ну хорошо."
                                elif Girl is KittyX:
                                        ch_k "Ладно."
                                elif Girl is EmmaX:
                                        ch_e "Хорошо."
                                elif Girl is LauraX:
                                        ch_l "Ладно."
                                elif Girl is JeanX:
                                        ch_j "Тебе в этот раз повезло."
                                elif Girl is StormX:
                                        ch_s ". . . Хорошо."
                                elif Girl is JubesX:
                                        $ Girl.Statup("Love", 80, -2)
                                        ch_v ". . . Хорошо."
                                elif Girl is GwenX:
                                        ch_g "Ну. . . как скажешь. . ."
                                elif Girl is BetsyX:
                                        ch_b "Если это так необходимо. . ."
                                elif Girl is DoreenX:
                                        ch_d ". . . ладно, наверное. . ."
                                elif Girl is WandaX:
                                        ch_w "Ладно, ладно, как пожелаешь. . ."
                                $ Choice = "leave"
                        elif ApprovalCheck(Girl, 800, "O"):
                                $ Girl.Statup("Love", 50, -10)
                                $ Girl.Statup("Love", 200, -5)
                                $ Girl.Statup("Obed", 90, 10)
                                $ Girl.Statup("Obed", 200, 5)
                                if Girl is RogueX:
                                        ch_r "Ну, если ты настаиваешь."
                                elif Girl is KittyX:
                                        ch_k "Ладно."
                                elif Girl is EmmaX:
                                        ch_e "Если я должна."
                                elif Girl is LauraX:
                                        ch_l "Если ты настаиваешь."
                                elif Girl is JeanX:
                                        ch_j "Хм. . . ладно."
                                elif Girl is StormX:
                                        ch_s ". . . Хорошо."
                                elif Girl is JubesX:
                                        ch_v ". . . Хорошо."
                                elif Girl is GwenX:
                                        ch_g "Хорошо, я понимаю. . ."
                                elif Girl is BetsyX:
                                        ch_b "Ох, хорошо. . ."
                                elif Girl is DoreenX:
                                        ch_d ". . . ладно. . ."
                                elif Girl is WandaX:
                                        ch_w "Ладно. . ."
                                $ Choice = "leave"
                        elif Cleaned:
                                $ Girl.Statup("Love", 50, -5)
                                $ Girl.Statup("Love", 200, -1)
                                $ Girl.FaceChange("angry")
                                if Girl is RogueX:
                                        ch_r "Серьезно, хватит предлагать мне такое."
                                elif Girl is KittyX:
                                        ch_k "Серьезно, хватит предлагать мне такое."
                                elif Girl is EmmaX:
                                        ch_e "Хватит уже."
                                elif Girl is LauraX:
                                        ch_l "Хватит."
                                elif Girl is JeanX:
                                        ch_j "Прекращай."
                                elif Girl is StormX:
                                        ch_s "Довольно, [Girl.Petname]."
                                elif Girl is JubesX:
                                        ch_v "Я не хочу!"
                                elif Girl is GwenX:
                                        ch_g "Хватит быть грубым. . ."
                                elif Girl is BetsyX:
                                        ch_b "Перестань спрашивать. . ."
                                elif Girl is DoreenX:
                                        ch_d "Хватит спрашивать."
                                elif Girl is WandaX:
                                        ch_w "Дай мне отдохнуть от этого. . ."
                        elif ApprovalCheck(Girl, 800):
                                $ Girl.Statup("Love", 50, -3)
                                $ Girl.Statup("Love", 200, -1)
                                $ Girl.FaceChange("sad")
                                if Girl is RogueX:
                                        ch_r "Извини, но ты заходишь слишком далеко."
                                elif Girl is KittyX:
                                        ch_k "Это слишком."
                                elif Girl is EmmaX:
                                        ch_e "Не заставляй меня."
                                elif Girl is LauraX:
                                        ch_l "Не дави на меня."
                                elif Girl is JeanX:
                                        ch_j "Успокойся."
                                elif Girl is StormX:
                                        ch_s "Нет."
                                elif Girl is JubesX:
                                        ch_v "Нет!"
                                elif Girl is GwenX:
                                        ch_g "Как грубо!"
                                elif Girl is BetsyX:
                                        ch_b "Какой ужас. . ."
                                elif Girl is DoreenX:
                                        ch_d "Иу. . . "
                                elif Girl is WandaX:
                                        ch_w "Ни за что. . ."
                        else:
                                $ Girl.Statup("Love", 50, -10)
                                $ Girl.Statup("Love", 200, -5)
                                $ Girl.FaceChange("angry")
                                if Girl is RogueX:
                                    if Player.Male:
                                        ch_r "Ну а -я- настаиваю, что тебе стоит поучиться, как надо разговаривать с девушкой!"
                                    else:
                                        ch_r "Ну а -я- настаиваю, что ты не лезла не в свое дело!"
                                elif Girl is KittyX:
                                        ch_k "Очень жаль!"
                                elif Girl is EmmaX:
                                        ch_e "Очевидно, что я не соглашусь."
                                elif Girl is LauraX:
                                        ch_l "Чёрта с два."
                                elif Girl is JeanX:
                                        ch_j "Хорошо бы тебе поучиться манерам."
                                elif Girl is StormX:
                                        ch_s "Не заставляй меня, [Girl.Petname]."
                                elif Girl is JubesX:
                                        ch_v "Ни за что!"
                                elif Girl is GwenX:
                                        ch_g "Как грубо. . ."
                                elif Girl is BetsyX:
                                        ch_b "Какой ужас. . ."
                                elif Girl is DoreenX:
                                        ch_d "Иу. . . "
                                elif Girl is WandaX:
                                        ch_w "Ни за что. . ."
                    "Ладно, неважно.":
                                if Girl is RogueX:
                                        ch_r "Вот и хорошо. . ."
                                elif Girl is KittyX:
                                        ch_k "Ладно. . ."
                                elif Girl is EmmaX:
                                        ch_e "Ладно. . ."
                                elif Girl is LauraX:
                                        ch_l "Ладно. . ."
                                elif Girl is JeanX:
                                        ch_j "Ладно. . ."
                                elif Girl is StormX:
                                        ch_s "Хорошо."
                                elif Girl is JubesX:
                                        ch_v "Хорошо."
                                elif Girl is GwenX:
                                        ch_g "Здорово. . ."
                                elif Girl is BetsyX:
                                        ch_b "Ладно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ну ладно. . . "
                                elif Girl is WandaX:
                                        ch_w "Хорошо. . ."
    #end "leave it"

    if Choice == "eat" and Player.Male:
            ch_p "Ты должна все съесть."
            $ Girl.FaceChange("sly")
            if "hungry" in Girl.Traits or (Girl.Swallow >= 5 and ApprovalCheck(Girl, 800)):
                    #lots of swallows
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 50, 3)
                    $ Girl.Statup("Inbt", 80, 1)
                    $ Girl.Statup("Lust", 90, 5)
                    if Girl is RogueX:
                            ch_r "Я и вправду немного голодна. . ."
                    elif Girl is KittyX:
                            if not Player.Male:
                                ch_k "Ммммм, может ты и права. . ."
                            else:
                                ch_k "Ммммм, может ты и прав. . ."
                    elif Girl is EmmaX:
                            ch_e "Полагаю, можно. . ."
                    elif Girl is LauraX:
                            "Она облизывается. . ."
                    elif Girl is JeanX:
                            ch_j "Ммм. . . ладно."
                    elif Girl is StormX:
                            ch_s "Благодарю. . ."
                    elif Girl is JubesX:
                            $ Girl.FaceChange("smile")
                            ch_v "Славно!"
                    elif Girl is GwenX:
                            ch_g "Хорошо. . ."
                    elif Girl is BetsyX:
                            ch_b "Ох, если ты настаиваешь . ."
                    elif Girl is DoreenX:
                            ch_d "Конечно!"
                    elif Girl is WandaX:
                            ch_w "Хмммм. . ."
            elif Girl.Swallow and ApprovalCheck(Girl, 800):
                    #few swallows
                    $ Girl.Statup("Obed", 50, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 50, 2)
                    $ Girl.Statup("Inbt", 80, 1)
                    $ Girl.Statup("Lust", 90, 5)
                    if Girl is RogueX:
                            ch_r "Ну ладно, в прошлый раз вкус был не таким уж и плохим. . ."
                    elif Girl is KittyX:
                            if not Player.Male:
                                ch_k "Ну, они не так уж и плохи на вкус. . ."
                            else:
                                ch_k "Ну, она не так уж и плоха на вкус. . ."
                    elif Girl is EmmaX:
                            ch_e "У тебя удивительный вкус. . ."
                    elif Girl is LauraX:
                            ch_l "У тебя неплохой вкус. . ."
                    elif Girl is JeanX:
                            ch_j "Мммм. . . ладно."
                    elif Girl is StormX:
                            ch_s "У тебя очень интересный вкус. . ."
                    elif Girl is JubesX:
                            $ Girl.FaceChange("smile")
                            ch_v "Славно!"
                    elif Girl is GwenX:
                            ch_g "Ну. . . ладно. . ."
                    elif Girl is BetsyX:
                            ch_b "Ох, если ты настаиваешь. . ."
                    elif Girl is DoreenX:
                            if not Player.Male:
                                ch_d "Ты довольно вкусная. . . "
                            else:
                                ch_d "Ты довольно вкусный. . . "
                    elif Girl is WandaX:
                            ch_w "Хмммм. . ."
            elif ApprovalCheck(Girl, 1200) or Girl is JubesX:
                    #no swallows, but likes you
                    $ Girl.Statup("Obed", 50, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 50, 3)
                    $ Girl.Statup("Inbt", 80, 1)
                    if Girl is RogueX:
                            ch_r "Ну, думаю, что я могла бы попробовать. . ."
                    elif Girl is KittyX:
                            if not Player.Male:
                                ch_k "Хм, наверное, ты права. . ."
                            else:
                                ch_k "Хм, наверное, ты прав. . ."
                    elif Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Мне немного любопытно, какова ты на вкус. . ."
                            else:
                                ch_e "Мне немного любопытно, каков ты на вкус. . ."
                    elif Girl is LauraX:
                            ch_l "Я много думала об этом. . ."
                    elif Girl is JeanX:
                            ch_j "Ммм. . . ладно."
                    elif Girl is StormX:
                            ch_s "Я могу попробовать, [Girl.Petname]."
                    elif Girl is JubesX:
                            $ Girl.FaceChange("smile")
                            ch_v "Спасибо!"
                    elif Girl is GwenX:
                            ch_g "Эм, наверное, попробовать стоит. . ."
                    elif Girl is BetsyX:
                            ch_b "Я могу попробовать. . ."
                    elif Girl is DoreenX:
                            ch_d "Звучит. . . интересно. . . "
                    elif Girl is WandaX:
                            ch_w "Серьезно? Хмммм. . ."
            elif ApprovalCheck(Girl, 400):
                    #Likes you well enough, but won't
                    $ Girl.FaceChange("sad")
                    if Girl is RogueX:
                            ch_r "Извини, но я не думаю, что смогу."
                    elif Girl is KittyX:
                            ch_k "Я в этом не уверена."
                    elif Girl is EmmaX:
                            ch_e "Я в этом сомневаюсь."
                    elif Girl is LauraX:
                            ch_l "Ага, но я не буду. . ."
                    elif Girl is JeanX:
                            ch_j "Хмм. . . не-а."
                    elif Girl is StormX:
                            ch_s "Я бы предпочла этого не делать."
                    elif Girl is GwenX:
                            ch_g "Эм, нет, спасибо. . ."
                    elif Girl is BetsyX:
                            ch_b "Я не могу. . ."
                    elif Girl is DoreenX:
                            ch_d "Это звучит странно. . . "
                    elif Girl is WandaX:
                            ch_w "Серьезно? Я так не думаю. . ."
                    #elif Girl is JubesX:
                    $ Choice = "clean"
            else:
                    #doesn't like you.
                    $ Girl.Statup("Love", 50, -5)
                    $ Girl.Statup("Love", 200, -3)
                    $ Girl.FaceChange("angry")
                    if Girl is RogueX:
                            ch_r "Нет."
                    elif Girl is KittyX:
                            ch_k "Не-а."
                    elif Girl is EmmaX:
                            ch_e "Нет."
                    elif Girl is LauraX:
                            ch_l "Не-а."
                    elif Girl is JeanX:
                            ch_j "Ха. . . ни за что."
                    elif Girl is StormX:
                            ch_s "Благодарю, но нет."
                    elif Girl is GwenX:
                            ch_g "Ага, нет. . ."
                    elif Girl is BetsyX:
                            ch_b "Какой ужас. . ."
                    elif Girl is DoreenX:
                            ch_d "Иу. . . "
                    elif Girl is WandaX:
                            ch_w "Ни за что. . ."
                    #elif Girl is JubesX:
                    $ Choice = "clean"
            #end eat it
    #end if Choice == "eat":

    if Choice == "clean2":
                    #if not ApprovalCheck(Girl, 400, "I"):
                    ch_p "Ты должна просто. . ."
                    call AnyLine(Girl,"Я все уберу.")
                    $ Choice = "clean"
    elif Choice == "clean":

            if Girl is EmmaX and "taboo" not in EmmaX.History:
                    $ Girl.FaceChange("sly")
                    ch_e "Очевидно, что меня не должны увидеть в таком виде. . ."
            elif ApprovalCheck(Girl, 600, "I") and not ApprovalCheck(Girl, 1500, "LO") and Girl != JubesX: #rebellious
                    ch_p "Ты должна просто все убрать."
                    $ Girl.FaceChange("sly")
                    $ Girl.Statup("Obed", 50, -3)
                    $ Girl.Statup("Inbt", 70, 10)
                    $ Girl.Statup("Inbt", 200, 5)
                    $ Girl.Statup("Lust", 60, 5)
                    if Girl is RogueX:
                            ch_r "Ну я не знаю, [Girl.Petname], мне, как бы, хотелось оставить все, как есть. . ."
                    elif Girl is KittyX:
                            ch_k "Я не знаю, [Girl.Petname], все выглядит не так уж плохо. . ."
                    elif Girl is EmmaX:
                            ch_e "Мммм. . . разве я сейчас так плохо выгляжу? . ."
                    elif Girl is LauraX:
                            ch_l "Я бы могла. . ."
                            ch_l "-но не хочу. . ."
                    elif Girl is JeanX:
                            ch_j "Ммм. . . не-а. Мне нравится. . ."
                    elif Girl is StormX:
                            ch_s "Пожалуй, я хочу оставить все, как есть. . ."
                    elif Girl is GwenX:
                            ch_g "Ну. . . она хорошо сочетается с моей внешностью. . ."
                    elif Girl is BetsyX:
                            ch_b "По-моему, все выглядит довольно мило. . ."
                    elif Girl is DoreenX:
                            ch_d "Я не уверена, все выглядит. . . интересно. . . "
                    elif Girl is WandaX:
                            ch_w "Тебе не нравится, как я сейчас выгляжу? . ."
                            ch_w "Я хочу оставить все, как есть. . ."
                    $ Choice = "leave"
                    menu:
                        extend ""
                        "Ну ладно.":
                                    $ Girl.FaceChange("smile")
                                    $ Girl.Statup("Love", 70, 5)
                                    $ Girl.Statup("Obed", 50, 3)
                        "Нет, приведи себя в порядок.":
                            if ApprovalCheck(Girl, 600, "O"):
                                    $ Girl.FaceChange("sad")
                                    $ Girl.Statup("Obed", 50, 10)
                                    if Girl is RogueX:
                                            ch_r "Ну раз ты так этого хочешь. . ."
                                    elif Girl is KittyX:
                                            ch_k "Ох, ну хорошо. . ."
                                    elif Girl is EmmaX:
                                            ch_e "Ох, если я должна. . ."
                                    elif Girl is LauraX:
                                            ch_l "Ох, ну хорошо. . ."
                                    elif Girl is JeanX:
                                            ch_j "Хмм. . . как скажешь."
                                    elif Girl is StormX:
                                            ch_s ". . . Хорошо."
                                    elif Girl is JubesX:
                                            ch_v "Славно!"
                                    elif Girl is GwenX:
                                            ch_g "Ох, ладно. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Ох, если это так необходимо. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ох, хорошо. . . "
                                    elif Girl is WandaX:
                                            ch_w "Хорошо. . ."
                                    $ Choice = "clean"
                            elif ApprovalCheck(Girl, 1200, "LO"):
                                    $ Girl.FaceChange("sad")
                                    $ Girl.Statup("Love", 70, -3)
                                    $ Girl.Statup("Obed", 50, 3)
                                    if Girl is RogueX:
                                            if not Player.Male:
                                                ch_r "Все веселье испортила. . ."
                                            else:
                                                ch_r "Все веселье испортил. . ."
                                    elif Girl is KittyX:
                                            ch_k "Буууу. . ."
                                    elif Girl is EmmaX:
                                            if not Player.Male:
                                                ch_e "Все настроение испортила. . ."
                                            else:
                                                ch_e "Все настроение испортил. . ."
                                    elif Girl is LauraX:
                                            ch_l "Буууу. . ."
                                    elif Girl is JeanX:
                                            ch_j ". . . пофиг."
                                    elif Girl is StormX:
                                            ch_s ". . . Хорошо."
                                    elif Girl is GwenX:
                                            if not Player.Male:
                                                ch_g "Взяла и все испортила. . ."
                                            else:
                                                ch_g "Взял и все испортил. . ."
                                    elif Girl is BetsyX:
                                            ch_b "Какой ужас. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Оу. . . "
                                    elif Girl is WandaX:
                                            ch_w "Отстой. . ."
                                    $ Choice = "clean"
                            else:
                                    $ Girl.Statup("Love", 70, -5)
                                    $ Girl.Statup("Obed", 50, -5)
                                    if Girl is RogueX:
                                            if not Player.Male:
                                                ch_r "Я -сказала-, что они останутся на мне."
                                            else:
                                                ch_r "Я -сказала-, что она останется на мне."
                                    elif Girl is KittyX:
                                            ch_k "Нет! Мне все нравится."
                                    elif Girl is EmmaX:
                                            ch_e "Боюсь, твое слово ничего не решит."
                                    elif Girl is LauraX:
                                            ch_l "Очень жаль."
                                    elif Girl is JeanX:
                                            ch_j "Хмм. . . мне все равно, чего ты хочешь."
                                    elif Girl is StormX:
                                            ch_s ". . . нет."
                                    elif Girl is GwenX:
                                            ch_g "Ладно. . ."
                                            "Водит руками вокруг себя, будто очищаясь, но ничего не меняется."
                                            ch_g "Вот. Готово."
                                    elif Girl is BetsyX:
                                            ch_b "Я не должна этого делать. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Извини, [Girl.Petname]. . ."
                                    elif Girl is WandaX:
                                            ch_w "Жаль, что ты этого хочешь."
            else: #agrees
                        ch_p "Тебе следует просто все убрать."
                        $ Girl.FaceChange("bemused")
                        $ Choice = "clean"
                        if Girl is RogueX:
                                ch_r "Ладно. . ."
                        elif Girl is KittyX:
                                ch_k "Хорошо. . ."
                        elif Girl is EmmaX:
                                ch_e "Если это так необходимо. . ."
                        elif Girl is LauraX:
                                ch_l "Как скажешь. . ."
                        elif Girl is JeanX:
                                ch_j "Хмм. . . Как скажешь."
                        elif Girl is StormX:
                                ch_s ". . . Хорошо."
                        elif Girl is JubesX:
                                ch_v "Без проблем!"
                        elif Girl is GwenX:
                                ch_g "Конечно. . ."
                        elif Girl is BetsyX:
                                ch_b "Хорошо. . ."
                        elif Girl is DoreenX:
                                ch_d "Конечно."
                        elif Girl is WandaX:
                                ch_w "Конечно. . ."
    #end clean it up confirmation

    if Choice == "partner wipe" or Choice == "partner lick":
            #resets to "random" if she refuses
            call Partner_Cleanup_Check(Girl)

    if Girl is JubesX:
            $ Options = ["eat"]
    elif Choice == "random":
            $ Options = ["clean"]
            if Girl.Swallow and ApprovalCheck(Girl, 800):
                    $ Options.append("eat")
                    if Girl.Swallow >=5:
                        $ Options.append("eat")
                    if "hungry" in Girl.Traits:
                        $ Options.append("eat")
            if ApprovalCheck(Girl, 300, "I"):
                    #Cnt means it's the end of a session
                    if not Cnt:
                        $ Options.append("leave")
                    if not Cnt or ApprovalCheck(Girl, 600, "I"):
                        $ Options.append("leave")
                    if not Cnt or ApprovalCheck(Girl, 800, "I"):
                        $ Options.append("leave")
                    if "exhibitionist" in Girl.Traits:
                        $ Options.append("leave")

            $ renpy.random.shuffle(Options)

            $ Choice = Options[0]
            #end "random"

    if Choice == "leave":
            $ Girl.Statup("Inbt", 80, 2)
            $ Girl.Statup("Inbt", 200, 1)
            if Player.Male:
                    "Она оставляет вашу сперму там, где она была и подмигивает вам."
            else:
                    "Она оставляет ваши соки там, где они были и подмигивает вам."
            if "hand" in Girl.Spunk:
                    $ Girl.Spunk.remove("hand")
                    if Girl.Swallow:
                        "Хотя она облизывает свои пальчики."
                    else:
                        "Хотя руку решает все-таки вытереть."
            if "mouth" in Girl.Spunk:
                    $ Girl.Spunk.remove("mouth")
            if Cnt:
                    # if this is final clean-up and left the jiz on
                    $ Girl.RecentActions.append("painted")
                    $ Girl.DailyActions.append("painted")
    elif Girl.Spunk:
            call Self_Cleanup(Girl)

    if Original in TotalGirls and Ch_Focus != Original:
            # if Girl wasn't the lead, swap that one back
            call Shift_Focus(Original)
    return

# End Girl Clean-Up /////////////////////////////////////////////////////////////////////////////////////


# Start Clean-up  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Start Self Clean-Up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Self_Cleanup(Girl=0):         #rkeljsvg
    $ Cnt = 0
    if Girl is JeanX and not ApprovalCheck(Girl, 600, "LO"):
            #if she has no interest in you. . .
            $ Girl.Wet = 0
            $ del Girl.Spunk[:]
            $ Girl.FaceChange("sly", 1,Eyes="psychic")
            if not Player.Male:
                "[JeanX.Name] концентрируется и все соки вихрем слетают с нее, дождем падая на пол."
            else:
                "[JeanX.Name] концентрируется и вся сперма вихрем слетает с нее, дождем падая на пол."
            $ Girl.FaceChange("sly", 0)
            return
    if "mouth" in Girl.Spunk and Choice != "eat":
            $ Girl.Spunk.remove("mouth")
            if Player.Male:
                    "[Girl.Name] сплевывает, сперма начинает стекать с ее подбородка,"
            $ Cnt += 1
            if "chin" not in Girl.Spunk:
                $ Girl.Spunk.append("chin")
    if Girl.Spunk:
            $ Girl.Spunk.append("hand")
    if "chin" in Girl.Spunk:
            $ Girl.Spunk.remove("chin")
            if Cnt:
                if not Player.Male:
                    "затем она вытирает соки с подбородка,"
                else:
                    "затем она вытирает сперму с подбородка,"
            else:
                if not Player.Male:
                    "[Girl.Name] вытирает соки с подбородка,"
                else:
                    "[Girl.Name] вытирает сперму с подбородка,"
            $ Cnt += 1
    if "hair" in Girl.Spunk:
            $ Girl.Spunk.remove("hair")
            if Cnt:
                if not Player.Male:
                    "потом она вычищает соки из своих волос,"
                else:
                    "потом она вычищает сперму из своих волос,"
            else:
                if not Player.Male:
                    "[Girl.Name] вычищает соки из своих волос,"
                else:
                    "[Girl.Name] вычищает сперму из своих волос,"
            $ Cnt += 1
    if "facial" in Girl.Spunk:
            $ Girl.Spunk.remove("facial")
            if Cnt:
                if not Player.Male:
                    "затем она вытирает соки со своего лица,"
                else:
                    "затем она вытирает сперму со своего лица,"
            else:
                if not Player.Male:
                    "[Girl.Name] вытирает соки со своего лица,"
                else:
                    "[Girl.Name] вытирает сперму со своего лица,"
            $ Cnt += 1
    if "tits" in Girl.Spunk:
            $ Girl.Spunk.remove("tits")
            $ Player.Statup("Focus",80,2)
            if Cnt:
                if not Player.Male:
                    "потом она вытирает соки с своей груди,"
                else:
                    "потом она вытирает сперму с своей груди,"
            else:
                if not Player.Male:
                    "[Girl.Name] вытирает соки с своей груди,"
                else:
                    "[Girl.Name] вытирает сперму с своей груди,"
            $ Cnt += 1
    if "belly" in Girl.Spunk:
            $ Girl.Spunk.remove("belly")
            if Cnt:
                if not Player.Male:
                    "затем она вытирает соки со своего живота,"
                else:
                    "затем она вытирает сперму со своего живота,"
            else:
                if not Player.Male:
                    "[Girl.Name] вытирает соки со своего живота,"
                else:
                    "[Girl.Name] вытирает сперму со своего живота,"
            $ Cnt += 1
    if "back" in Girl.Spunk:
            $ Girl.Spunk.remove("back")
            if Cnt:
                "затем она вытирает все со своей спины,"
            else:
                "[Girl.Name] вытирает все со своей спины,"
            $ Cnt += 1
    if "feet" in Girl.Spunk:
            $ Girl.Spunk.remove("feet")
            if Cnt:
                "потом она вытирает свои ножки,"
            else:
                "[Girl.Name] вытирает свои ножки,"
            $ Cnt += 1
    if "in" in Girl.Spunk:
            $ Girl.Spunk.remove("in")
            $ Player.Statup("Focus",80,3)
            if Cnt:
                if not Player.Male:
                    "потом она достает все ваши соки из своей киски,"
                else:
                    "потом она достает всю вашу сперму из своей киски,"
            else:
                if not Player.Male:
                    "[Girl.Name] достает все ваши соки из своей киски,"
                else:
                    "[Girl.Name] достает всю вашу сперму из своей киски,"
            $ Cnt += 1
    if "anal" in Girl.Spunk and (ApprovalCheck(Girl, 800, "I") or Choice != "eat"):
            while "anal" in Girl.Spunk:
                $ Girl.Spunk.remove("anal")
            $ Player.Statup("Focus",80,2)
            if Cnt:
                if not Player.Male:
                    "затем она вытирает соки, стекающии из ее попки,"
                else:
                    "затем она вытирает сперму, стекающую из ее попки,"
            else:
                if not Player.Male:
                    "[Girl.Name] вытирает соки, стекающии из ее попки,"
                else:
                    "[Girl.Name] вытирает сперму, стекающую из ее попки,"
            $ Cnt += 1
    if "hand" in Girl.Spunk:
            $ Girl.Spunk.remove("hand")
            if Choice == "eat":
                    $ Girl.Spunk.append("mouth")
                    $ Player.Statup("Focus",80,3)
                    if Cnt and "anal" in Girl.Spunk:
                        "затем с довольной улыбкой она слизывает все со своих пальчиков."
                    elif Cnt:
                        "и наконец с довольной улыбкой она начисто вылизывает свою руку."
                    else:
                        "[Girl.Name] с довольной улыбкой начисто вылизывает свою руку."

                    $ Girl.Statup("Inbt", 80, 2)
                    $ Girl.Spunk.remove("mouth")
                    $ Girl.Swallow += 1
                    $ Girl.Addict -= (10*Cnt)
                    if Girl.Swallow == 1:
                        $ Girl.SEXP += 12
                    $ Girl.RecentActions.append("swallowed")
                    $ Girl.DailyActions.append("swallowed")
            #end hand if swallowing
            else:
                    if Cnt:
                        "и наконец она вытирает свои руки лежащим неподалеку платком."
                    else:
                        "[Girl.Name] вытирает свои руки лежащим неподалеку платком."
            $ Cnt += 1
            #end hand
    if "anal" in Girl.Spunk:
            $ Girl.Spunk.remove("anal")
            if Cnt:
                if not Player.Male:
                    "После этого она вытирает соки, стекающии из ее попки."
                else:
                    "После этого она вытирает сперму, стекающую из ее попки."
            else:
                if not Player.Male:
                    "[Girl.Name] вытирает соки, стекающии из ее попки."
                else:
                    "[Girl.Name] вытирает сперму, стекающую из ее попки."

    $ Girl.Wet = 0
    $ del Girl.Spunk[:]
    if Cnt >= 5:
            $ Girl.Eyes = "surprised"
            if Girl is RogueX:
                if Player.Male:
                    ch_r "Ничего себе, ты меня прям всю в белый цвет выкрасил!"
                else:
                    ch_r "Ого, я выглядела как мокрая крыса!"
            elif Girl is KittyX:
                    if not Player.Male:
                        ch_k "Вау, ты прямо всю меня залила!"
                    else:
                        ch_k "Вау, ты прямо всю меня залил!"
            elif Girl is EmmaX:
                    if "White Queen" not in EmmaX.Names and Player.Male:
                            ch_e "Сейчас я и правда \"белая королева\"."
                            $ EmmaX.Names.append("White Queen")
                            $ EmmaX.Pets.append("White Queen")
                    else:
                            if not Player.Male:
                                ch_e "Что ж, ты проделала большую работу."
                            else:
                                ch_e "Что ж, ты проделал большую работу."
            elif Girl is LauraX:
                    ch_l "Ее гораздо больше, чем я думала. . ."
            elif Girl is JeanX:
                    if not Player.Male:
                        ch_j "Фух, ты полностью забрызгала меня. . ."
                    else:
                        ch_j "Фух, ты полностью забрызгал меня. . ."
            elif Girl is StormX:
                    ch_s ". . . Трудно сказать, есть ли что-нибудь в моих волосах. . ."
            elif Girl is JubesX:
                    if not Player.Male:
                        ch_v "Ты всю меня покрыла, да?"
                    else:
                        ch_v "Ты всю меня покрыл, да?"
            elif Girl is GwenX:
                    if not Player.Male:
                        ch_g "Ты всю меня залила. . ."
                    else:
                        ch_g "Ты всю меня залил. . ."
            elif Girl is BetsyX:
                    if not Player.Male:
                        ch_b "Ты выпустила на меня настоящик поток. . ."
                    else:
                        ch_b "Ты выпустил на меня настоящик поток. . ."
            elif Girl is DoreenX:
                    if not Player.Male:
                        ch_d "Ты меня втянула в настоящий хаос. . . "
                    else:
                        ch_d "Ты меня втянул в настоящий хаос. . . "
            elif Girl is WandaX:
                    ch_w "Ого, не ожидала, что стану -белой- ведьмой. . ."
            $ Girl.Eyes = "sexy"
    elif Cnt >=3:
            if Girl is RogueX:
                    if not Player.Male:
                        ch_r "Ну и бардак же ты устроила, а мне его еще и убирать."
                    else:
                        ch_r "Ну и бардак же ты устроил, а мне его еще и убирать."
            elif Girl is KittyX:
                    if not Player.Male:
                        ch_k "Ты устроила приятный беспорядок."
                    else:
                        ch_k "Ты устроил приятный беспорядок."
            elif Girl is EmmaX:
                if Player.Male:
                    ch_e "Сейчас я и правда \"белая королева\"."
                    if "White Queen" not in EmmaX.Names:
                            $ EmmaX.Names.append("White Queen")
                            $ EmmaX.Pets.append("White Queen")
                else:
                    ch_e "Я прямо насквозь промокла."
            elif Girl is LauraX:
                    if not Player.Male:
                        ch_l "Ты устроила тут настоящий бардак."
                    else:
                        ch_l "Ты устроил тут настоящий бардак."
            elif Girl is JeanX:
                    ch_j "Похоже, тебе стоит быть аккуратней. . ."
            elif Girl is StormX:
                    ch_s "Пожалуй, в следующий раз тебе нужно заранее решить, куда стрелять."
            elif Girl is JubesX:
                    ch_v "Уф, это было много."
            elif Girl is GwenX:
                    if not Player.Male:
                        ch_g "Постарайся, эм, быть более кучной. . ."
                    else:
                        ch_g "Постарайся, эм, быть более кучным. . ."
            elif Girl is BetsyX:
                    ch_b "Постарайся не оставлять такой беспорядок. . ."
            elif Girl is DoreenX:
                    if not Player.Male:
                        ch_d "Ты устроила такой беспорядок. . . "
                    else:
                        ch_d "Ты устроил такой беспорядок. . . "
            elif Girl is WandaX:
                    ch_w "Фу, какой беспорядок. . ."
    if Choice == "eat" and Girl.Swallow >= 5:
            if Girl is RogueX:
                    ch_r "Это было восхитительно."
            elif Girl is KittyX:
                    ch_k "Ням."
            elif Girl is EmmaX:
                    ch_e "Мммм, теперь я хочу еще больше."
            elif Girl is LauraX:
                    ch_l "Мммм, а есть еще?"
            elif Girl is JeanX:
                    ch_j "Ммм. . ."
            elif Girl is StormX:
                    ch_s "Мммм. . ."
            elif Girl is JubesX:
                    ch_v "Это было потрясающе. . ."
            elif Girl is GwenX:
                    ch_g "Это что-то. . . новенькое. . ."
            elif Girl is BetsyX:
                    ch_b "Это был интересный. . . опыт. . ."
            elif Girl is DoreenX:
                    ch_d "Довольно вкусно. . . "
            elif Girl is WandaX:
                    ch_w "Ням!"
    return
# End Self Clean-Up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Partner_Cleanup_Check(Girl=0,B=0): #rkeljsvg
        #girl is the lead, B is a bonus check based on if she's good with the other girl
        #resets to "random" if she refuses
        if Partner is JubesX:
                        $ B = 100
        elif Choice == "partner lick":
                if (Partner in Player.Harem and Girl in Player.Harem) or "poly " + Partner.Tag in Girl.Traits:
                        $ B = 0
                else:
                        $ B = -100
        else:
                        $ B = 0


        if Partner is JeanX and not ApprovalCheck(Partner, 600, "LO") and Partner.GirlLikeCheck(Girl) < (500-2*B):
                #if you ask Jean to clean other girl and she has no interest in either of you. . .
                ch_j "Хм? Почистить [Girl.Name_vin] говоришь?"
                ch_j "Похоже, она действительно очень грязная. . ."
                $ Girl.Wet = 0
                $ del Girl.Spunk[:]
                $ Partner.FaceChange("sly", 1,Eyes="psychic")
                "[JeanX.Name] концентрируется и выделения вашего тела вихрем слетают с [Girl.Name_rod], дождем падая на пол."
                if Girl is JubesX:
                        $ Girl.FaceChange("sad", 1,Eyes="down")
                        ch_v "Оу."
                $ Partner.FaceChange("sly", 0)
                ch_j "Вот."
                return

        if not ApprovalCheck(Partner, 1400, Bonus=3*B) or Partner.GirlLikeCheck(Girl) < (500-2*B):
                #if she's not super obedient or doesn't like the other girl
                $ Partner.FaceChange("sly")
                $ Partner.Statup("Obed", 50, -3)
                $ Partner.Statup("Inbt", 70, 10)
                $ Partner.Statup("Inbt", 200, 5)
                $ Partner.Statup("Lust", 60, 5)
                call Partner_CGLine(2) #"You want me ta clean up your mess?"
                menu:
                    extend ""
                    "Ладно, не бери в голову.":
                                $ Partner.FaceChange("smile")
                                $ Partner.Statup("Love", 70, 5)
                                $ Partner.Statup("Obed", 50, 3)
                                $ Choice = "random"
                    "Да, приступай.":
                        if ApprovalCheck(Partner, 600,"O", Bonus=3*B):
                                # She's obedient. . .
                                $ Partner.FaceChange("sad")
                                $ Partner.Statup("Obed", 50, 10)
                                call Partner_CGLine(3) #"If you say so."
                        elif Partner.GirlLikeCheck(Girl) >= 800:
                                # She likes the other girl. . .
                                $ Partner.FaceChange("sly")
                                $ Partner.Statup("Love", 70, -3)
                                $ Partner.Statup("Obed", 50, 3)
                                call Partner_CGLine(4) #"I guess I don't mind if she doesn't."
                        elif ApprovalCheck(Partner, 1200, Bonus=3*B):
                                # She's likes you enough to listen. . .
                                $ Partner.FaceChange("normal")
                                $ Partner.Statup("Love", 70, -3)
                                $ Partner.Statup("Obed", 50, 3)
                                call Partner_CGLine(5) #"I guess I could. . ."
                        elif Choice == "partner lick" and ApprovalCheck(Partner, 1200) and Partner.GirlLikeCheck(Girl) >= 600:
                                # She's likes you enough to wipe, but not lick. . .
                                $ Partner.FaceChange("normal")
                                $ Partner.Statup("Love", 70, -3)
                                $ Partner.Statup("Obed", 50, 3)
                                call Partner_CGLine(6)  #"I can wipe her off, I guess, but that's it. . ."
                                $ Choice = "partner wipe"
                        else:
                                # She's obedient. . .
                                $ Partner.Statup("Love", 70, -5)
                                $ Partner.Statup("Obed", 50, -5)
                                $ Girl.GLG(Partner,900,-2,1)
                                call Partner_CGLine(7)  #"No way."
                                $ Choice = "random"
        else:           # She just agrees. . .
                                $ Girl.FaceChange("bemused")
                                if not Choice:
                                        $ Choice = "partner wipe"
                                $ Girl.GLG(Partner,900,3,1)
                                call Partner_CGLine(1) #"I'd better get to work, I guess."
        #end Partner wipe off partner check


        if Choice != "random":
            $ Girl.Statup("Lust", 60, 5)
            if not ApprovalCheck(Girl, 1400, Bonus=3*B) or Girl.GirlLikeCheck(Partner) < (500-2*B):
                #if Rogue doesn't like the other girl or isn't super obedient
                if Girl.GirlLikeCheck(Partner) >= 800:
                        $ Girl.Statup("Inbt", 90, 5)
                        $ Partner.GLG(Girl,900,5,1)
                        call Partner_CGLine(8,Girl)   #"I'll allow it, since she seems so excited by it. . ."
                elif ApprovalCheck(Girl, 1200, Bonus=3*B):
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Obed", 80, 2)
                        $ Girl.Statup("Inbt", 70, 3)
                        call Partner_CGLine(9,Girl)    #"If that's what turns you on. . ."
                elif ApprovalCheck(Girl, 1000, Bonus=3*B) and Girl.GirlLikeCheck(Partner) >= (600-B):
                        $ Girl.Statup("Love", 70, 1)
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Obed", 80, 3)
                        $ Girl.Statup("Inbt", 70, 5)
                        $ Partner.GLG(Girl,900,3,1)
                        call Partner_CGLine(10,Girl) #"Kinda ganging up on me here. . ."
                else:
                        $ Girl.Statup("Obed", 70, -3)
                        $ Girl.Statup("Inbt", 70, 2)
                        call Partner_CGLine(11,Girl)   # "Kinda gross, no."
                        $ Choice = "random"
            else:
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Inbt", 70, 3)
                        call Partner_CGLine(12,Girl) #"Oh, very well. . ."

        if Choice != "random":
                #calls the partner clean-up if that option is chosen
                call Les_Launch(Girl)

                call Partner_Clean_Girl(Girl)

                if Girl.Swallow >=5:
                        $ Options.append("eat")
                call AllReset(Partner)
                call AllReset(Ch_Focus)
                if Choice == "partner lick":
                        $ Girl.GLG(Partner,900,10,1)
                        call Partner_CGLine(13,Girl) #"Well that was a treat. . ."
                else:
                        $ Girl.GLG(Partner,900,3,1)
                        call Partner_CGLine(14,Girl)   #"That was easy."
        #end Partner wipe off
        return

label Partner_CGLine(LineNum=1,Girl=0): #rkeljsvg
        #call Partner_CGLine(4)
        if not Partner or not LineNum:
            return
        if LineNum == 1:
                # She just agrees. . .
                if Partner is RogueX:
                        ch_r "Конечно, почему бы и нет?"
                elif Partner is KittyX:
                        if not Player.Male:
                            ch_k "А ты[KittyX.like]и правда хорошо поработала над ней."
                        else:
                            ch_k "А ты[KittyX.like]и правда хорошо поработал над ней."
                        ch_k "Сейчас все будет."
                elif Partner is EmmaX:
                        ch_e "Полагаю, это было бы не так уж плохо."
                elif Partner is LauraX:
                        ch_l "Думаю, мне пора приступать."
                elif Partner is JeanX:
                        ch_j "Может ты и прав. . ."
                elif Partner is StormX:
                        ch_s "Пожалуй, я не против. . ."
                elif Partner is JubesX:
                        ch_v "Клево. . ."
                elif Partner is GwenX:
                        ch_g "Ага. . ."
                elif Partner is BetsyX:
                        ch_b "Ох, пожалуй, это я могу. . ."
                elif Partner is DoreenX:
                        ch_d "Конечно. . . "
                elif Partner is WandaX:
                        ch_w "Конечно. . ."
        elif LineNum == 2:
                # She questions whether she should. . .
                if Partner is RogueX:
                        ch_r "Хочешь, чтобы я прибрала за тобой?"
                elif Partner is KittyX:
                        if not Player.Male:
                            ch_k "А ты[KittyX.like]и правда хорошо поработала над ней."
                        else:
                            ch_k "А ты[KittyX.like]и правда хорошо поработал над ней."
                        ch_k "Хочешь, чтобы я со всем разобралась?"
                elif Partner is EmmaX:
                        ch_e "Ты предлагаешь мне опуститься до уборки?"
                elif Partner is LauraX:
                        if not Player.Male:
                            ch_l "Ты оставила на меня настоящий бардак."
                        else:
                            ch_l "Ты оставил на меня настоящий бардак."
                elif Partner is JeanX:
                        ch_j "Так что, теперь я твоя горничная?"
                elif Partner is StormX:
                        ch_s "Ты хочешь, чтобы я ее почистила?"
                elif Partner is JubesX:
                        if not Player.Male:
                            ch_v "Ты оставила все на меня? . ."
                        else:
                            ch_v "Ты оставил все на меня? . ."
                elif Partner is GwenX:
                        ch_g "Подожди, ты хочешь, чтобы я ее почистила? . ."
                        ch_g "После тебя? . ."
                elif Partner is BetsyX:
                        ch_b "Не знаю, хочу ли я это дедать. . ."
                elif Partner is DoreenX:
                        ch_d "Эм, я не уверена. . . "
                elif Partner is WandaX:
                        ch_w "Почему я должна это делать?"
        elif LineNum == 3:
                # She's obedient. . .
                if Partner is RogueX:
                        ch_r "Ну, если ты так говоришь."
                elif Partner is KittyX:
                        ch_k "Как скажешь."
                elif Partner is EmmaX:
                        ch_e "Прекрасно."
                elif Partner is LauraX:
                        ch_l "Я обо всем позабочусь."
                elif Partner is JeanX:
                        ch_j "Конечно. . ."
                elif Partner is StormX:
                        ch_s ". . . Хорошо."
                elif Partner is JubesX:
                        ch_v "Конечно. . ."
                elif Partner is GwenX:
                        ch_g "Поняла. . ."
                elif Partner is BetsyX:
                        ch_b "Если это так необходимо. . ."
                elif Partner is DoreenX:
                        ch_d "Ладно. . . "
                elif Partner is WandaX:
                        ch_w "Конечно. . ."
        elif LineNum == 4:
                # She likes the other girl. . .
                if Partner is RogueX:
                        ch_r "Ну, если она не против. . ."
                elif Partner is KittyX:
                        ch_k "Думаю, я не против, если она согласна."
                elif Partner is EmmaX:
                        ch_e "Отлично, иди сюда, дорогая."
                elif Partner is LauraX:
                        ch_l "Она немного грязная. . ."
                elif Partner is JeanX:
                        ch_j "Ну, Если я должна. . ."
                elif Partner is StormX:
                        ch_s "Хорошо, подойди сюда."
                elif Partner is JubesX:
                        ch_v "Клево. . ."
                elif Partner is GwenX:
                        ch_g "Иди сюда. . ."
                elif Partner is BetsyX:
                        ch_b "Ох, это так возбуждает. . ."
                elif Partner is DoreenX:
                        ch_d "Ох. правда?! Тогда я начну. . . "
                elif Partner is WandaX:
                        ch_w "Серьезно? Ладно. . ."
        elif LineNum == 5:
                # She's likes you enough to listen. . .
                if Partner is RogueX:
                        ch_r "Думаю, можно. . ."
                elif Partner is KittyX:
                        ch_k "Думаю, я справлюсь. . ."
                elif Partner is EmmaX:
                        ch_e "Полагаю, она сделала бы то же самое для меня."
                elif Partner is LauraX:
                        ch_l "Наверное, кто-то же должен."
                elif Partner is JeanX:
                        ch_j "Ладно, как скажешь."
                elif Partner is StormX:
                        ch_s "Пожалуй, я согласна. . ."
                elif Partner is JubesX:
                        ch_v "Конечно. . ."
                elif Partner is GwenX:
                        ch_g "Ага. . ."
                elif Partner is BetsyX:
                        ch_b "Если это так необходимо. . ."
                elif Partner is DoreenX:
                        ch_d "Эм, ладно. . . "
                elif Partner is WandaX:
                        ch_w "Конечно. . ."
        elif LineNum == 6:
                # She's likes you enough to wipe, not lick. . .
                if Partner is RogueX:
                        ch_r "Я могу ее обтереть, но, думаю, на более. . ."
                elif Partner is KittyX:
                        ch_k "Я не {i}такая{/i} кошечка. . ."
                elif Partner is EmmaX:
                        ch_e "Я воспользуюсь только руками, Если ты не возражаешь."
                elif Partner is LauraX:
                        ch_l "Я не знаю, я воспользуюсь только руками."
                elif Partner is JeanX:
                        ch_j "Я не буду этого сделать, но, думаю, вычистить смогу."
                elif Partner is StormX:
                        ch_s "Я оботру ее начисто, но не. . . своим языком."
                elif Partner is JubesX:
                        ch_v "Думаю, я могла бы просто обтереть ее. . ."
                elif Partner is GwenX:
                        ch_g "Ну, я могу быстренько обтереть ее. . ."
                elif Partner is BetsyX:
                        ch_b "Я могу немного ее обтереть. . ."
                elif Partner is DoreenX:
                        ch_d "Ну, я могу обтереть ее немного. . . "
                elif Partner is WandaX:
                        ch_w "Я могу немного обтереть ее. . ."
        elif LineNum == 7:
                # She's obedient. . .
                if Partner is RogueX:
                        ch_r "Ну, это твои проблемы. . ."
                elif Partner is KittyX:
                        ch_k "Ни за что."
                elif Partner is EmmaX:
                        ch_e "Боюсь, что не могу, [EmmaX.Petname]."
                elif Partner is LauraX:
                        ch_l "Я бы этого не хотела."
                elif Partner is JeanX:
                        ch_j "Не думаю. . ."
                elif Partner is StormX:
                        ch_s ". . . Я не буду."
                elif Partner is JubesX:
                        ch_v "Ага, конечно. . ."
                elif Partner is GwenX:
                        ch_g "Я тебя услышала. . ."
                elif Partner is BetsyX:
                        ch_b "Если это так необходимо. . ."
                elif Partner is DoreenX:
                        ch_d "Ладно. . . "
                elif Partner is WandaX:
                        ch_w "Конечно. . ."
        if not Girl:
                return
        #from the response portion. . .
        elif LineNum == 8:
                # She's into the other girl. . .
                if Girl is RogueX:
                        ch_r "Ну как я могу отказаться от такого заманчивого предложения. . ."
                elif Girl is KittyX:
                        ch_k "Ну[KittyX.like]ей понравится. . ."
                elif Girl is EmmaX:
                        ch_e "Я позволю ей это сделать, раз уж она так воодушевлена. . ."
                elif Girl is LauraX:
                        ch_l "Я справилась бы хуже, чем она."
                elif Girl is JeanX:
                        ch_j "Ну. . . если это нужно. . ."
                elif Girl is StormX:
                        ch_s "Это было бы чудесно, [Partner.Name]."
                elif Girl is JubesX:
                        ch_v "Клево. . ."
                elif Girl is GwenX:
                        ch_g "Ну, если ты настаиваешь, [Partner.Name]. . ."
                elif Girl is BetsyX:
                        ch_b "Что ж, это может быть весело. . ."
                elif Girl is DoreenX:
                        ch_d "Ох, правда? Здорово!"
                elif Girl is WandaX:
                        ch_w "Ого, ладно!"
        elif LineNum == 9:
                # She's into you enough. . .
                if Girl is RogueX:
                        ch_r "Ну, если тебя это заводит. . ."
                elif Girl is KittyX:
                        ch_k "Ну, если ты этого хочешь. . ."
                elif Girl is EmmaX:
                        ch_e "Я разрешаю, если тебе это так интересно. . ."
                elif Girl is LauraX:
                        ch_l "Конечно, если тебе этого хочется."
                elif Girl is JeanX:
                        ch_j "Ох, так вот, что тебе нравится? . ."
                elif Girl is StormX:
                        ch_s "Я разрешаю."
                elif Girl is JubesX:
                        ch_v "Конечно. . ."
                elif Girl is GwenX:
                        ch_g "Ну, если ты настаиваешь, [GwenX.Petname]. . ."
                elif Girl is BetsyX:
                        ch_b "Если это так необходимо. . ."
                elif Girl is DoreenX:
                        ch_d "Ох, правда? Эм, спасибо, [Partner.Name]."
                elif Girl is WandaX:
                        ch_w "Замечательно, спасибо."
        elif LineNum == 10:
                # She's into both of you a little. . .
                if Girl is RogueX:
                        ch_r "Не смотрите на меня так. . ."
                elif Girl is KittyX:
                        ch_k "Я чувствую себя в центре внимания."
                elif Girl is EmmaX:
                        ch_e "Ох, хорошо, не смотрите на меня так."
                elif Girl is LauraX:
                        ch_l "Чем больше, тем веселее."
                elif Girl is JeanX:
                        ch_j "Конечно. . ."
                elif Girl is StormX:
                        ch_s "Это может быть. . . приятно."
                elif Girl is JubesX:
                        ch_v "Клево. . ."
                elif Girl is GwenX:
                        ch_g "Ну, если вы, ребята, настаиваете. . ."
                elif Girl is BetsyX:
                        ch_b "От такого предложения я не могу отказаться. . ."
                elif Girl is DoreenX:
                        ch_d "Ох, правда? Спасибо, ребята!"
                elif Girl is WandaX:
                        ch_w "Замечательно, спасибо."
        elif LineNum == 11:
                # She's not into it. . .
                if Girl is RogueX:
                        ch_r "Я совсем не такая. . ."
                elif Girl is KittyX:
                        ch_k "Нет, это довольно мерзко."
                elif Girl is EmmaX:
                        ch_e "Я не могу в этом учавствовать."
                elif Girl is LauraX:
                        ch_l "Хм. . . нет."
                elif Girl is JeanX:
                        ch_j "Нет, спасибо."
                elif Girl is StormX:
                        ch_s ". . . Я бы предпочла этого не делать."
                elif Girl is JubesX:
                        ch_v "Эм. . ."
                elif Girl is GwenX:
                        ch_g "Пожалуй. я пас. . ."
                elif Girl is BetsyX:
                        ch_b "Я бы предпочла этого не делать. . ."
                elif Girl is DoreenX:
                        ch_d "Ох, тебе не нужно этого делать. . ."
                elif Girl is WandaX:
                        ch_w "Думаю, мне и так хорошо. . ."
        elif LineNum == 12:
                # She's fine with it. . .
                if Girl is RogueX:
                        ch_r "Я бы не отказалась от помощи. . ."
                elif Girl is KittyX:
                        ch_k "Как я могу отказать?"
                elif Girl is EmmaX:
                        ch_e "Ох, отлично. . ."
                elif Girl is LauraX:
                        ch_l "Ну, если предлагаете. . ."
                elif Girl is JeanX:
                        ch_j "Ну. . . если придется. . ."
                elif Girl is StormX:
                        ch_s ". . . Хорошо."
                elif Girl is JubesX:
                        ch_v "Клево. . ."
                elif Girl is GwenX:
                        ch_g "Классно. . ."
                elif Girl is BetsyX:
                        ch_b "Это может быть интересно. . ."
                elif Girl is DoreenX:
                        ch_d "Эм. . . ладно, наверное. . ."
                elif Girl is WandaX:
                        ch_w "Эм, спасибо."
        elif LineNum == 13:
                # After the other girl licked her down. . .
                if Girl is RogueX:
                        ch_r "Ну, это было приятно. . ."
                elif Girl is KittyX:
                        ch_k "Это было. . . очень приятно."
                elif Girl is EmmaX:
                        ch_e "Мммм, пожалуй, мне нужно почаще пользоваться твоей помощью."
                elif Girl is LauraX:
                        ch_l "У тебя это очень хорошо получается."
                elif Girl is JeanX:
                        ch_j "Хорошая работа. . ."
                elif Girl is StormX:
                        ch_s "Что ж. . . благодарю. . . [Partner.Name]."
                elif Girl is JubesX:
                        ch_v "О, эм, спасибо, наверное. . ."
                elif Girl is GwenX:
                        $ Girl.FaceChange("smile",2)
                        ch_g "Вау. . . это было здорово. . ."
                elif Girl is BetsyX:
                        ch_b "Это было очень мило с твоей стороны, дорогая. . ."
                elif Girl is DoreenX:
                        ch_d "-Огромное- спасибо, [Partner.Name]."
                elif Girl is WandaX:
                        ch_w "Мне было бы очень приятно, [Partner.Name]."
        elif LineNum == 14:
                # After the other girl wiped her down. . .
                if Girl is RogueX:
                        ch_r "Проще простого, хех. . ."
                elif Girl is KittyX:
                        ch_k "Эм, спасибо."
                elif Girl is EmmaX:
                        ch_e "Спасибо, дорогая, надеюсь, для тебя это было не слишком сложно."
                elif Girl is LauraX:
                        ch_l "Это было просто."
                elif Girl is JeanX:
                        ch_j "Думаю, ты все сделала так. . . тщательно. . ."
                elif Girl is StormX:
                        ch_s "Что ж. . . Благодарю. . . [Partner.Name]."
                elif Girl is JubesX:
                        ch_v "О, эм, спасибо, наверное. . ."
                elif Girl is GwenX:
                        ch_g "Эм, спасибо. . ."
                elif Girl is BetsyX:
                        ch_b "Это было очень мило с твоей стороны, дорогая. . ."
                elif Girl is DoreenX:
                        ch_d "Большое спасибо, [Partner.Name]."
                elif Girl is WandaX:
                        ch_w "Спасибо еще раз, [Partner.Name]."
        return

label Partner_Clean_Girl(Girl=0): #rkeljsvg
    #either "partner wipe" or Choice == "partner lick"

    if Choice != "partner wipe" and Choice != "partner lick":
        return

    if Choice == "partner lick":
            $ Partner.FaceChange("tongue")
    else:
            $ Partner.Spunk.append("hand")
    $ Cnt = 0
    if "chin" in Girl.Spunk or "mouth" in Girl.Spunk:
            while "chin" in Girl.Spunk:
                    $ Girl.Spunk.remove("chin")
            $ Girl.GLG(Partner,900,2,1)
            $ Partner.GLG(Girl,900,2,1)
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 3)
                    $ Girl.Statup("Lust", 80, 4)
                    $ Player.Statup("Focus",80,3)
                    "[Partner.Name] облизывает подбородок [Girl.Name_rod], прежде чем страстно поцеловать ее."
            else:
                    $ Girl.Statup("Lust", 80, 2)
                    "[Partner.Name]вытирает большим пальцем подбородок [Girl.Name_rod],"
            $ Cnt += 1
    if "mouth" in Girl.Spunk and Cnt:
            $ Girl.Spunk.remove("mouth")
            if not Player.Male:
                "вы замечаете ниточки соков, тянущиеся между их ртами."
            else:
                "вы замечаете ниточки спермы, тянущиеся между их ртами."
            $ Cnt += 1
    if "hair" in Girl.Spunk:
            $ Girl.Spunk.remove("hair")
            if Cnt:
                if not Player.Male:
                    "затем она вычищает волосы [Girl.Name_rod] от соков,"
                else:
                    "затем она вычищает волосы [Girl.Name_rod] от спермы,"
            else:
                if not Player.Male:
                    "[Partner.Name] вычищает волосы [Girl.Name_rod] от соков,"
                else:
                    "[Partner.Name] вычищает волосы [Girl.Name_rod] от спермы,"
            $ Cnt += 1
    if "facial" in Girl.Spunk:
            $ Girl.Spunk.remove("facial")
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 80, 4)
                    $ Player.Statup("Focus",80,3)
                    if Cnt:
                        if not Player.Male:
                            "потом она слизывает соки с лица [Girl.Name_rod],"
                        else:
                            "потом она слизывает сперму с лица [Girl.Name_rod],"
                    else:
                        if not Player.Male:
                            "[Partner.Name] слизывает соки с лица [Girl.Name_rod],"
                        else:
                            "[Partner.Name] слизывает сперму с лица [Girl.Name_rod],"
            else:
                    $ Girl.Statup("Lust", 80, 1)
                    if Cnt:
                        if not Player.Male:
                            "потом она вытирает соки с лица [Girl.Name_rod],"
                        else:
                            "потом она вытирает сперму с лица [Girl.Name_rod],"
                    else:
                        if not Player.Male:
                            "[Partner.Name] вытирает соки с лица [Girl.Name_rod],"
                        else:
                            "[Partner.Name] вытирает сперму с лица [Girl.Name_rod],"
            $ Cnt += 1
    if "tits" in Girl.Spunk:
            $ Girl.Spunk.remove("tits")
            $ Girl.GLG(Partner,900,2,1)
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 200, 4)
                    $ Player.Statup("Focus",80,4)
                    if Cnt:
                        "потом она начинает вылизывать грудь [Girl.Name_rod],"
                    else:
                        "[Partner.Name] начинает вылизывать грудь [Girl.Name_rod],"
            else:
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 80, 2)
                    $ Player.Statup("Focus",80,2)
                    if Cnt:
                        if not Player.Male:
                            "потом она начинает вытирать грудь [Girl.Name_rod] от соков,"
                        else:
                            "потом она начинает вытирать грудь [Girl.Name_rod] от спермы,"
                    else:
                        if not Player.Male:
                            "[Partner.Name] начинает вытирать грудь [Girl.Name_rod] от соков,"
                        else:
                            "[Partner.Name] начинает вытирать грудь [Girl.Name_rod] от спермы,"
            $ Cnt += 1
    if "belly" in Girl.Spunk:
            $ Girl.Spunk.remove("belly")
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 80, 3)
                    $ Player.Statup("Focus",80,1)
                    if Cnt:
                        "затем она вылизывает животик [Girl.Name_rod],"
                    else:
                        "[Partner.Name] вылизывает животик [Girl.Name_rod],"
            else:
                    $ Partner.Statup("Lust", 80, 1)
                    $ Girl.Statup("Lust", 80, 1)
                    if Cnt:
                        if not Player.Male:
                            "затем она вытирает животик [Girl.Name_rod] от соков,"
                        else:
                            "затем она вытирает животик [Girl.Name_rod] от спермы,"
                    else:
                        if not Player.Male:
                            "[Partner.Name] вытирает животик [Girl.Name_rod] от соков,"
                        else:
                            "[Partner.Name] вытирает животик [Girl.Name_rod] от спермы,"
            $ Cnt += 1
    if "feet" in Girl.Spunk:
            $ Girl.Spunk.remove("feet")
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 80, 3)
                    $ Player.Statup("Focus",80,1)
                    if Cnt:
                        "потом она вылизывает ножки [Girl.Name_rod],"
                    else:
                        "[Partner.Name] вылизывает ножки [Girl.Name_rod],"
            else:
                    $ Partner.Statup("Lust", 80, 1)
                    $ Girl.Statup("Lust", 80, 1)
                    if Cnt:
                        "потом она вытирает ножки [Girl.Name_rod],"
                    else:
                        "[Partner.Name] вытирает ножки [Girl.Name_rod],"
            $ Cnt += 1
    if "back" in Girl.Spunk:
            $ Girl.Spunk.remove("back")
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Girl.Statup("Lust", 80, 2)
                    if Cnt:
                        "потом она вылизывает спину [Girl.Name_rod],"
                    else:
                        "[Partner.Name] вылизывает спину [Girl.Name_rod],"
            else:
                    $ Girl.Statup("Lust", 80, 1)
                    if Cnt:
                        if not Player.Male:
                            "потом она вытирает спину [Girl.Name_rod] от соков,"
                        else:
                            "потом она вытирает спину [Girl.Name_rod] от спермы,"
                    else:
                        if not Player.Male:
                            "[Partner.Name] вытирает спину [Girl.Name_rod] от соков,"
                        else:
                            "[Partner.Name] вытирает спину [Girl.Name_rod] от спермы,"
            $ Cnt += 1
    if "in" in Girl.Spunk:
            $ Girl.Spunk.remove("in")
            $ Girl.GLG(Partner,900,5,1)
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 4)
                    $ Girl.Statup("Lust", 200, 6)
                    $ Player.Statup("Focus",80,6)
                    if Cnt:
                        "затем она нежно вылизывает киску [Girl.Name_rod],"
                    else:
                        "[Partner.Name] наклоняется и нежно вылизывает киску [Girl.Name_rod],"
            else:
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 200, 4)
                    $ Player.Statup("Focus",80,4)
                    if Cnt:
                        if not Player.Male:
                            "затем она гладит киску [Girl.Name_rod], начисто вытирая ее от соков,"
                        else:
                            "затем она гладит киску [Girl.Name_rod], начисто вытирая ее от спермы,"
                    else:
                        if not Player.Male:
                            "[Partner.Name] гладит киску [Girl.Name_rod], начисто вытирая ее от соков,"
                        else:
                            "[Partner.Name] гладит киску [Girl.Name_rod], начисто вытирая ее от спермы,"
            $ Cnt += 1
    if "anal" in Girl.Spunk:
            $ Girl.Spunk.remove("anal")
            $ Girl.GLG(Partner,900,5,1)
            if Choice == "partner lick" and ApprovalCheck(Partner, 800, "I"):
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 200, 6)
                    $ Player.Statup("Focus",80,5)
                    if Cnt:
                        if not Player.Male:
                            "потом она слизывает соки, стекающии из попки [Girl.Name_rod],"
                        else:
                            "потом она слизывает сперму, стекающую из попки [Girl.Name_rod],"
                    else:
                        if not Player.Male:
                            "[Partner.Name] слизывает соки, стекающии из попки [Girl.Name_rod],"
                        else:
                            "[Partner.Name] слизывает сперму, стекающую из попки [Girl.Name_rod],"
            else:
                    $ Partner.Statup("Lust", 80, 2)
                    $ Girl.Statup("Lust", 200, 6)
                    $ Player.Statup("Focus",80,3)
                    if Cnt:
                        if not Player.Male:
                            "потом она вытирает соки, стекающии из попки [Girl.Name_rod],"
                        else:
                            "потом она вытирает сперму, стекающую из попки [Girl.Name_rod],"
                    else:
                        if not Player.Male:
                            "[Partner.Name] вытирает соки, стекающии из попки [Girl.Name_rod],"
                        else:
                            "[Partner.Name] вытирает сперму, стекающую из попки [Girl.Name_rod],"
            $ Cnt += 1

    $ Partner.FaceChange("sly")
    if "hand" in Girl.Spunk:
            $ Girl.Spunk.remove("hand")
            if Choice == "partner lick":
                    if "mouth" not in Partner.Spunk:
                            $ Partner.Spunk.append("mouth")
                    if "chin" not in Partner.Spunk:
                            $ Partner.Spunk.append("chin")
                    $ Girl.Statup("Lust", 80, 3)
                    $ Player.Statup("Focus",80,3)
                    if Cnt:
                        "и, наконец, она облизывает руки [Girl.Name_rod] с довольной улыбкой."
                    else:
                        "[Partner.Name] облизывает пальчики [Girl.Name_rod] с довольной улыбкой."
            else:
                    if Cnt:
                        "и, наконец, она вытирает руки [Girl.Name_rod]."
                    else:
                        "[Partner.Name] вытирает руки [Girl.Name_rod] с довольной улыбкой."

    if Choice == "partner lick" or ApprovalCheck(Partner, 1000):
            #if the partner swallows
            while "mouth" in Partner.Spunk:
                    $ Partner.Spunk.remove("mouth")
            while "chin" in Partner.Spunk:
                    $ Partner.Spunk.remove("chin")
            $ Girl.Statup("Inbt", 80, 2)
            $ Player.Statup("Focus",80,3)
            "Далее [Partner.Name] сглатывает и вытирает рот."
            $ Partner.Swallow += 1
            $ Partner.Addict -= (10*Cnt)
            if Partner.Swallow == 1:
                $ Partner.SEXP += 12
            $ Partner.RecentActions.append("swallowed")
            $ Partner.DailyActions.append("swallowed")
    else:
        #if the Partner won't swallow
        if Cnt:
            "и, наконец, она вытирает свои руки рядом лежащим платком."
        else:
            "[Partner.Name] вытирает свои руки рядом лежащим платком."
            $ Cnt += 1
    $ Girl.Spunk = []
    $ Partner.Spunk = []
    return

# End Clean-up  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
