# Event First_Addicted /////////////////////////////////////////////////////
label First_Addicted(Girl=0): #rkeljsvgbdw
        # Modification mode
        $ play_music()
        # -----------------
        # Girl.Event[1] starts at zero, +1 each time, jumps to 10 if you agree to help her
        if Girl.Resistance:
                #if she's already gone through this, jump to the repeatable version.
                call Addiction_Fix(Girl)
                return
        $ Girl.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene
        call Shift_Focus(Girl)
        $ Girl.Event[1] += 1

        $ Player.AddWord(1,0,"fix") #adds to daily
        call Locked_Door(Girl,0)
        if not _return:
                #if the door is locked and you refused entry. . .
                return
        call CleartheRoom(Girl)
        call Shift_Focus(Girl)
        $ Addict_Queue = 0

        if "switchcheck" in Girl.Traits:
                #if you recently switched sexes. . .
                if Girl.Loc == bg_current or Girl in Party:
                        "Вдруг [Girl.Name] оглядывается и замечает вас,"
                else:
                        "Вдруг [Girl.Name] появляется словно из ниоткуда и замечает вас,"
                $ Girl.Loc = bg_current
                $ Girl.OutfitChange(Changed=1)
                call Set_The_Scene
                $ Girl.FaceChange("confused")
                call expression Girl.Tag + "_Switch" #call Rogue_Switch
                call AnyLine(Girl,". . . но я не об этом хотела поговорить.")
        elif bg_current != "bg player":
                if Girl.Loc == bg_current or Girl in Party:
                        "[Girl.Name] вдруг говорит, что хочет пообщаться с вами в вашей комнате, а затем отводит вас туда."
                else:
                        "[Girl.Name] появляется словно из ниоткуда, она изъявляет желание поговорить с вами в вашей комнате, а затем отводит вас туда."
        else:
                if Girl.Loc == bg_current or Girl in Party:
                        "[Girl.Name] поворачивается к вам с немного ошеломленным видом."
                else:
                        "[Girl.Name] в панике врывается в вашу комнату."
        $ Taboo = 0
        $ Girl.Taboo = 0
        $ bg_current = "bg player"
        $ Girl.Loc = bg_current
        $ Girl.OutfitChange(Changed=1)
        call Set_The_Scene
#        call CleartheRoom(Girl)
        call Shift_Focus(Girl)
        $ Player.AddWord(1,"interruption") #prevents interruption
        if Girl.Event[1] > 2:
                        jump First_Addicted3
        elif Girl.Event[1] == 2:
                        jump First_Addicted2
        else:
                #first time through. . .
                if Girl is RogueX:
                        $ Girl.FaceChange("bemused")
                        if not Player.Male:
                            ch_r "О, привет, [Girl.Petname]. Похоже, ты уже привыкла к новой обстановке. . ."
                        else:
                            ch_r "О, привет, [Girl.Petname]. Похоже, ты уже привык к новой обстановке. . ."
                        if not Girl.Kissed:
                            ch_r "Послушай, с того самого дня, когда я впервые. . . прикоснулась к тебе,"
                        else:
                            ch_r "Послушай, с того самого дня, когда я впервые. . . поцеловала тебя,"
                        ch_r "Меня не покидает чувство. . . эйфории. Я думаю, это от того, что наконец-то могу прикоснуться к кому-то и,"
                        $ Girl.Eyes = "sexy"
                        ch_r "Может. . . я могу сделать это снова?"
                elif Girl is KittyX:
                        $ Girl.FaceChange("bemused",2)
                        ch_k "О. . . привет, [Girl.Petname]. Я тут подумала. . ."
                        if not Girl.Kissed:
                            ch_k "С тех пор, как я впервые. . . прикоснулась к тебе,"
                        else:
                            ch_k "С тех пор, как я впервые. . . поцеловала тебя,"
                        ch_k "Мне кажется, что. . . я чувствую себя как-то странно. . ."
                        $ Girl.Eyes = "side"
                        ch_k "Может ты позволишь мне сделать это снова?"
                elif Girl is EmmaX:
                        $ Girl.FaceChange("bemused")
                        ch_e "Ох, здравствуй, [Girl.Petname]. . ."
                        ch_e "Как мне кажется, ты хорошо учишься. . ."
                        ch_e "Послушай, с того самого дня, когда мы впервые. . . вступили в контакт. . ."
                        $ Girl.FaceChange("sadside",1,Brows="angry")
                        ch_e "Меня. . . не покидает некое. . ."
                        ch_e "Чувство. . ."
                        $ Girl.Eyes = "sexy"
                        ch_e "И я подумала. . . может ты позволишь мне снова прикоснуться к тебе, чтобы во всем разобраться?"
                elif Girl is LauraX:
                        $ Girl.FaceChange("bemused")
                        ch_l "О, привет, [Girl.Petname]."
                        ch_l "Как считаешь, могу я прикоснуться к тебе снова?"
                        menu:
                            extend ""
                            "Ладно?":
                                ch_l "Клево."
                            "Зачем?":
                                ch_l "О. . . да просто так."
                                ch_l "Я немного нервничаю, и мне хочется кое-что попробовать."
                elif Girl is JeanX:
                        $ Girl.FaceChange("confused",1)
                        ch_j "Ох. . ."
                        ch_j "Привет. . . [Girl.Petname]."
                        $ Girl.FaceChange("confused",2)
                        ch_j "Дай я просто прикоснусь к тебе на секунду."
                        $ Girl.FaceChange("bemused",1)
                        ch_j "Прости, не хотела пугать тебя. . ."
                        menu:
                            extend ""
                            "Ладно?":
                                $ Girl.Statup("Love", 50, 3)
                                $ Girl.Statup("Love", 80, 3)
                                $ Girl.Statup("Obed", 50, 3)
                                $ Girl.Statup("Inbt", 200, 3)
                                ch_j "Замечательно."
                            "Зачем?":
                                $ Girl.FaceChange("angry",2)
                                ch_j "Не твое дело!"
                                $ Girl.FaceChange("bemused",1,Eyes="side")
                                ch_j "Я просто думала о последнем прикосновение к тебе и. . ."
                                ch_j "Не знаю. Забудь."
                                $ Girl.FaceChange("bemused",1)
                elif Girl is StormX:
                        $ Girl.FaceChange("sad")
                        ch_s "[Girl.Petname], мне интересно, можешь ли ты помочь мне с одной проблемой. . ."
                        $ Girl.FaceChange("sadside")
                        ch_s "В последнее время я чувствую себя немного. . ."
                        ch_s "неуютно."
                        ch_s ". . ."
                        $ Girl.FaceChange("sad")
                        ch_s "Чувствую, что я словно. . . в ловушке."
                        ch_s "-будто стены смыкаются вокруг меня."
                        if not Player.Male:
                            ch_s "Уверена, это началось, когда ты впервые прикоснулась ко мне, и это чувство только нарастает."
                        else:
                            ch_s "Уверена, это началось, когда ты впервые прикоснулся ко мне, и это чувство только нарастает."
                        ch_s "Я хотела бы узнать, поможет ли. . . новый контакт."
                elif Girl is JubesX:
                        $ Girl.FaceChange("bemused")
                        ch_v "Привет, так вот. . . [Girl.Petname]. . ."
                        ch_v "Ничего не вышло. . ."
                        menu:
                            extend ""
                            "Что не вышло?":
                                    pass
                            "И?":
                                    pass
                            "Ну ладно.":
                                    pass
                        ch_v "Я какое-то время могла выходить на солнце, но это прошло."
                        ch_v "Сначала все было хорошо, затем появился зуд, но вскоре он перерос в жжение. . ."
                        ch_v "Думаю, это был лишь временный эффект. . ."
                        ch_v ". . ."
                        ch_v "Можно я. . ."
                        ch_v "Укушу тебя снова?"
                        menu:
                            extend ""
                            "Это немного чересчур.":
                                    ch_v "Наверное. . ."
                            "Я бы этого не хотела." if not Player.Male:
                                    ch_v "Я понимаю. . ."
                            "Я бы этого не хотел." if Player.Male:
                                    ch_v "Я понимаю. . ."
                            "Нет.":
                                    ch_v ". . ."
                        ch_v "I guess that is a bit much. . ."
                elif Girl is GwenX:
                        $ Girl.FaceChange("bemused")
                        if not Player.Male:
                            ch_g "Привет, [Player.Name]. . . Ты не замечала ничего странного в последнее время?"
                        else:
                            ch_g "Привет, [Player.Name]. . . Ты не замечал ничего странного в последнее время?"
                        menu:
                            extend ""
                            "Типа тебя?":
                                    ch_g "Нет, не \"типа меня!\""
                            "Да нет.":
                                    ch_g "Хм. . ."
                            "Ты про некие странные желания?":
                                    ch_g "Типа. . . да! Точно!"
                        ch_g "Последние пару дней я чувствовала себя неуверенно и нервно."
                        ch_g "Как ребенок из тех школьных социальных реклам."
                        ch_g "Ты знаешь из-за чего это?"
                        menu:
                            extend ""
                            "Ты на мете?":
                                    ch_g "Нет, я не \"на мете!\""
                            "Да нет.":
                                    ch_g "Ох, ладно. . ."
                            "Мои прикосновения вызывают зависимость.":
                                    ch_g "Ох, ладно. . . {w=0.5}{nw}"
                                    ch_g "Ох, ладно. . . подожди, что?!"
                                    menu:
                                        extend ""
                                        "Забей.":
                                                ch_g "Ну. . . это бы все объяснило. . ."
                                        "Когда я прикасаюсь к людям, они хотят большего.":
                                                ch_g "Почему ты сразу не сказал мне об этом?"
                                                ch_g "Это многое объясняет!"
                        if not Player.Male:
                            ch_g "Мне кажется, когда ты прикоснулась ко мне, я почувствовала небольшой разряд."
                            ch_g "С тех пор всякий раз, когда я испытываю сильное желание. . ."
                            ch_g "Я вспоминаю об этом."
                            ch_g "Не могла бы ты, эм. . . прикоснуться ко мне снова?"
                        else:
                            ch_g "Мне кажется, когда ты прикоснулся ко мне, я почувствовала небольшой разряд."
                            ch_g "С тех пор всякий раз, когда я испытываю сильное желание. . ."
                            ch_g "Я вспоминаю об этом."
                            ch_g "Не мог бы ты, эм. . . прикоснуться ко мне снова?"
                elif Girl is BetsyX:
                        $ Girl.FaceChange("bemused",2)
                        ch_b "[Girl.Petname]. . . Кажется, у меня возникла небольшая проблема."
                        $ Girl.FaceChange("bemused",2,Eyes="side")
                        ch_b ". . ."
                        ch_b "С тех пор, как мы в последний раз касались друг друга, я чувствую. . . некий дискомфорт, он только возрастает со временем."
                        $ Girl.FaceChange("bemused",2)
                        ch_b "Я считаю, что, возможно, эти два явления могут быть связаны."
                        $ Girl.FaceChange("sly",2)
                        if not Player.Male:
                            ch_b "Могу я попросить тебя, чтобы ты легонько прикоснулась ко мне и подтвердила или опровергла мои подозрения?"
                        else:
                            ch_b "Могу я попросить тебя, чтобы ты легонько прикоснулся ко мне и подтвердил или опроверг мои подозрения?"
                elif Girl is DoreenX:
                        $ Girl.FaceChange("bemused",2)
                        ch_d "Привет, [Girl.Petname]. . . мы можем немного поговорить?"
                        ch_d "Помнишь, на днях, когда я прикоснулась к тебе, я почувствовала легкую искру?"
                        ch_d "С тех пор я много об этом думала."
                        $ Girl.FaceChange("bemused",2,Eyes="side")
                        ch_d "Даже -слишком- много. . ."
                        $ Girl.FaceChange("confused",2)
                        ch_d "Как считаешь, твои касания могу вызвать зависимость или что-то вроде того?"
                        menu:
                            extend ""
                            "Ага.":
                                ch_d "Нет, думая о-"
                                $ Girl.FaceChange("perplexed",2)
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.Statup("Obed", 80, 2)
                                if not Player.Male:
                                    ch_d "Подожди, ты знала?"
                                else:
                                    ch_d "Подожди, ты знал?"
                                $ Girl.FaceChange("angry",2)
                                if not Player.Male:
                                    ch_d "Почему мне сразу не сказала?"
                                else:
                                    ch_d "Почему мне сразу не сказал?"
                                menu:
                                    "Извини, все произошло так быстро.":
                                            $ Girl.FaceChange("sadside",2)
                                            $ Girl.Statup("Love", 80, 2)
                                            ch_d "Думаю, я понимаю, извини, что обрушилась так на тебя."
                                    "Извини.":
                                            $ Girl.FaceChange("sadside",2)
                                            ch_d "Что ж, бывает, извини, что обрушилась так на тебя."
                                    "[[Пожать плечами]":
                                            $ Girl.FaceChange("confused",2)
                                            $ Girl.Statup("Love", 80, -1)
                                            $ Girl.Statup("Obed", 60, 1)
                                            ch_d "Лаааадно. . ."
                                    "Я думала, это будет весело." if not Player.Male:
                                            $ Girl.Statup("Love", 80, -2)
                                            $ Girl.Statup("Obed", 80, 2)
                                            ch_d "Это совсем не весело!"
                                    "Я думал, это будет весело." if Player.Male:
                                            $ Girl.Statup("Love", 80, -2)
                                            $ Girl.Statup("Obed", 80, 2)
                                            ch_d "Это совсем не весело!"
                                ch_d "В любом случае, у меня тут появилась одна идейка."
                            "Возможно.":
                                ch_d "Нет, думая об этом, мне кажется, твои касания все же вызывают зависимость."
                            "Этого просто не может быть.":
                                ch_d "Нет, думая об этом, мне кажется, твои касания все же вызывают зависимость."
                        $ Girl.FaceChange("sly",2)
                        ch_d "Я хочу провести один эксперимент, позволь мне снова прикоснуться к тебе, чтобы убедиться."
                elif Girl is WandaX:
                        $ Girl.FaceChange("bemused",2)
                        ch_w "Слушай, [Girl.Petname]. . . Мне нужно с тобой поговорить."
                        if not Player.Male:
                            ch_w "Помнишь, как ты испытывала свои силы на мне?"
                        else:
                            ch_w "Помнишь, как ты испытывал свои силы на мне?"
                        ch_w "Я не могу перестать думать об этом. . ."
                        ch_w "Это было так приятно - чувствовать, что мои силы полностью под контролем."
                        ch_w "Я долго думала и. . . может, повторим?"
        #end "first intro"

        menu:
            extend ""
            "Как насчет еще одного поцелуя?" if Girl.Kissed:
                    if ApprovalCheck(Girl, 660, "LI",Alt=[[RogueX,JeanX],560]):
                            $ Girl.Statup("Lust", 80, 3)
                            $ Girl.Statup("Love", 80, 6)
                            $ Girl.FaceChange("sexy")
                            if Girl is RogueX:
                                    ch_r "Да, конечно, давай, [Girl.Petname]."
                            elif Girl is KittyX:
                                    ch_k "Эм, ага!"
                            elif Girl is EmmaX:
                                    ch_e "Ты читаешь мои мысли, [Girl.Petname]."
                            elif Girl is LauraX:
                                    ch_l "Конечно, я за."
                            elif Girl is JeanX:
                                    ch_j "Конечно, как скажешь."
                            elif Girl is StormX:
                                    ch_s "Ах, это может сработать."
                            elif Girl is JubesX:
                                    ch_v "Ну, обычно \"вампиру\" нужно другое, но мы могли бы попробовать. . ."
                            elif Girl is GwenX:
                                    ch_g "Конечно, это должно сработать."
                            elif Girl is BetsyX:
                                    ch_b "Ох, это может сработать."
                            elif Girl is DoreenX:
                                    ch_d "Эм, конечно."
                            elif Girl is WandaX:
                                    ch_w "Ох. . . конечно."
                            "Она наклоняется для очередного поцелуя."
                            call KissPrep
                    else:
                            $ Girl.FaceChange("sad",2)
                            if Girl is RogueX:
                                    ch_r "Я так не думаю, [Girl.Petname]."
                            elif Girl is KittyX:
                                    ch_k "Эм, нет, спасибо."
                            elif Girl is EmmaX:
                                    ch_e "Не думаю, что сейчас это уместно."
                            elif Girl is LauraX:
                                    ch_l "Эм, нет, спасибо."
                            elif Girl is JeanX:
                                    ch_j "Это не совсем то, о чем я думала. . ."
                            elif Girl is StormX:
                                    ch_s "Лучше не надо."
                            elif Girl is JubesX:
                                    ch_v "Неа. . ."
                            elif Girl is GwenX:
                                    ch_g "Я совсем не хочу этого. . ."
                            elif Girl is BetsyX:
                                    ch_b "Ох, я бы предпочла этого не делать. . ."
                            elif Girl is DoreenX:
                                    ch_d "Я. . . пожалуй, откажусь."
                            elif Girl is WandaX:
                                    ch_w "Я так не думаю. . ."
                            jump Addicted_Bad_End
            "Как насчет поцелуя?" if not Girl.Kissed:
                    if ApprovalCheck(Girl, 660, "LI",Alt=[[RogueX,JeanX],560]):
                            $ Girl.Statup("Lust", 80, 3)
                            $ Girl.Statup("Love", 80, 6)
                            $ Girl.FaceChange("bemused",1)
                            if Girl is RogueX:
                                    ch_r "Да, конечно, давай."
                            elif Girl is KittyX:
                                    ch_k "Что? О. . . эм, ладно. . ."
                            elif Girl is EmmaX:
                                    ch_e "Ох, хорошо. . . Думаю, можно. . ."
                            elif Girl is LauraX:
                                    ch_l "Ох. . . Наверное, можно."
                            elif Girl is JeanX:
                                    ch_j "Конечно, как скажешь."
                            elif Girl is StormX:
                                    ch_s "Поцелуй? Пожалуй, это может сработать."
                            elif Girl is JubesX:
                                    ch_v "Ну, обычно \"вампиру\" нужно другое, но мы могли бы попробовать. . ."
                            elif Girl is GwenX:
                                    ch_g "Хорошо. . . Думаю, поцелуй не повредит."
                            elif Girl is BetsyX:
                                    ch_b "Ох, это может сработать."
                            elif Girl is DoreenX:
                                    ch_d "Ох! Эм. . . это должно сработать."
                            elif Girl is WandaX:
                                    ch_w "Пожалуй, можно."
                            "Она наклоняется, чтобы поцеловать вас."
                            call KissPrep
                    else:
                            $ Girl.FaceChange("sad",2)
                            if Girl is RogueX:
                                    ch_r "Я так не думаю, [Girl.Petname]."
                            elif Girl is KittyX:
                                    ch_k "Эм, нет, спасибо."
                            elif Girl is EmmaX:
                                    ch_e "Не думаю, что сейчас это уместно."
                            elif Girl is LauraX:
                                    ch_l "Эм, нет, спасибо."
                            elif Girl is JeanX:
                                    ch_j "Это не совсем то, о чем я думала."
                            elif Girl is StormX:
                                    ch_s "Нет. . . Сомневаюсь, что это сработает."
                            elif Girl is JubesX:
                                    ch_v "Обычно \"вампиру\" нужно другое. . ."
                            elif Girl is GwenX:
                                    ch_g "Не думаю, что мы должны это делать."
                            elif Girl is BetsyX:
                                    ch_b "Ох, я бы предпочла этого не делать. . ."
                            elif Girl is DoreenX:
                                    ch_d "Я. . . пожалуй, откажусь."
                            elif Girl is WandaX:
                                    ch_w "Я. . . пожалуй, нет. . . я откажусь."
                            jump Addicted_Bad_End
            "Конечно, если тебе от этого станет легче." if Girl is not JubesX:
                    if ApprovalCheck(Girl, 700, "LI",Alt=[[RogueX],600],Bias=-100):
                            $ Girl.Statup("Lust", 80, 3)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Love", 80, 3)
                            $ Girl.Statup("Love", 50, 4)
                            $ Girl.FaceChange("sexy")
                            if Girl is RogueX:
                                    ch_r "У меня появилась идея."
                            elif Girl is KittyX:
                                    ch_k "Хорошо, потому что у меня появилась идея. . ."
                            elif Girl is EmmaX:
                                    ch_e "Что ж, мы оба можем насладиться этими впечатлениями. . ."
                            elif Girl is LauraX:
                                    ch_r "Клево."
                            elif Girl is JeanX:
                                    ch_j "Как насчет. . ."
                            elif Girl is StormX:
                                    ch_s "Пожалуй, тогда поцелуемся. . ."
                            elif Girl is GwenX:
                                    ch_g "Ну, обычно в таких историях все происходят так. . ."
                            elif Girl is BetsyX:
                                    ch_b "Тогда, я пожалуй, я выберу. . . это."
                            elif Girl is DoreenX:
                                    ch_d "Тогда. . . как насчет поцелуя?"
                            elif Girl is WandaX:
                                    ch_w "Ладно. . . как насчет этого. . ."
                            "Она наклоняется, чтобы поцеловать вас."
                            call KissPrep
                    else:
                            $ Girl.Statup("Lust", 80, 3)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Love", 80, 3)
                            $ Girl.Statup("Love", 50, 4)
                            $ Girl.FaceChange("smile")
                            call Girl_Tag(Girl)

            "Что? Хочешь просто потрогать мое лицо? Нет, спасибо." if Girl is not JubesX:
                    if ApprovalCheck(Girl, 500, "L",Alt=[[RogueX,JeanX],400],Bias=-100) or Girl.Kissed:
                            $ Girl.Statup("Love", 200, -3)
                            $ Girl.Statup("Inbt", 50, 3)
                            $ Girl.Brows = "confused"
                            $ Girl.Eyes = "surprised"
                            $ Girl.Mouth = "sad"
                            if Girl is RogueX:
                                    ch_r "Ну, а как насчет того, чтобы я тебя поцеловала?"
                            elif Girl is KittyX:
                                    ch_k "Хорошо. . . Я могла бы поцеловать тебя?"
                            elif Girl is EmmaX:
                                    ch_e "Может, тебя заинтересует. . . поцелуй?"
                            elif Girl is LauraX:
                                    ch_l "Тогда. . . может начнем целоваться?"
                            elif Girl is JeanX:
                                    ch_j "Хммм. . ."
                                    ch_j "Хочешь тогда начнем целоваться?"
                            elif Girl is StormX:
                                    ch_s "А что, если я тебя поцелую?"
                            elif Girl is GwenX:
                                    ch_g "Ну, думаю, поцелуй лучше подходит для такого рода ситуаций. . ."
                            elif Girl is BetsyX:
                                    ch_b "Ох. . . тогда, может, тебя устроит поцелуй?"
                            elif Girl is DoreenX:
                                    ch_d "Ну. . . а что, если я поцелую тебя?"
                            elif Girl is WandaX:
                                    ch_w "Ну ладно. . . Тогда как насчет поцелуя?"
                            menu:
                                extend ""
                                "Конечно, другое дело.":
                                        $ Girl.Statup("Lust", 80, 3)
                                        $ Girl.Statup("Love", 80, 5)
                                        $ Girl.FaceChange("sexy")
                                        "Она наклоняется, чтобы поцеловать вас."
                                        call KissPrep
                                "Только если это будет затяжной поцелуй." if Girl not in (LauraX,JeanX):
                                        $ Girl.Statup("Love", 80, 3)
                                        $ Girl.Statup("Obed", 40, 5)
                                        $ Girl.FaceChange("sexy")
                                        if Girl is RogueX:
                                                ch_r "Хорошо, можно и так."
                                        elif Girl is KittyX:
                                                ch_k "Конечно, хорошо."
                                        elif Girl is EmmaX:
                                                ch_e "Почему бы и нет."
                                        elif Girl is StormX:
                                                ch_s "Ох. Пожалуй, можно и так. . ."
                                        elif Girl is GwenX:
                                                ch_g "Ну, отказываться не буду."
                                        elif Girl is BetsyX:
                                                ch_b "М? . .  ясно."
                                                ch_b "Ну ладно."
                                        elif Girl is DoreenX:
                                                ch_d "Ох. . . нууу. . . ладно."
                                        elif Girl is WandaX:
                                                ch_w "Ясное дело."
                                        call KissPrep
                                "Не-а, все еще недостаточно.":
                                        $ Girl.Statup("Love", 200, -5)
                                        $ Girl.Brows = "angry"
                                        $ Count2 = 3
                                        call Addicted_Ultimatum
                    else:
                                        $ Girl.Brows = "angry"
                                        $ Count2 = 2
                                        call Addicted_Ultimatum

            "Попробуй прикоснуться к моему лицу." if Girl is JubesX:
                    if ApprovalCheck(Girl, 700, "LI"):
                            $ Girl.Statup("Lust", 80, 3)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Love", 80, 3)
                            $ Girl.Statup("Love", 50, 4)
                            $ Girl.FaceChange("sexy")
                            ch_v "Ну, мы можем пойти на большее. . ."
                            "Она наклоняется, чтобы поцеловать вас."
                            call KissPrep
                    else:
                            $ Girl.Statup("Lust", 80, 3)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Love", 80, 3)
                            $ Girl.Statup("Love", 50, 4)
                            $ Girl.FaceChange("smile")
                            ch_v "Давай попробуем. . ."
                            call Girl_Tag(Girl)

            "Хочешь испить моей крови? Нет уж, спасибо." if Girl is JubesX:
                    if ApprovalCheck(Girl, 500, "L") or Girl.Kissed:
                            $ Girl.Statup("Love", 200, -3)
                            $ Girl.Statup("Inbt", 50, 3)
                            $ Girl.Brows = "confused"
                            $ Girl.Eyes = "surprised"
                            $ Girl.Mouth = "sad"
                            ch_v "А что, если я тебя поцелую?"
                            menu:
                                extend ""
                                "Конечно, другое дело.":
                                        $ Girl.Statup("Lust", 80, 3)
                                        $ Girl.Statup("Love", 80, 5)
                                        $ Girl.FaceChange("sexy")
                                        "Она наклоняется, чтобы поцеловать вас."
                                        call KissPrep
                                "Только если это будет затяжной поцелуй.":
                                        $ Girl.Statup("Love", 80, 3)
                                        $ Girl.Statup("Obed", 40, 5)
                                        $ Girl.FaceChange("sexy")
                                        ch_v "Думаю, с этим я справлюсь. . ."
                                        call KissPrep
                                "Неа, все еще недостаточно.":
                                        $ Girl.Statup("Love", 200, -5)
                                        $ Girl.Brows = "angry"
                                        $ Count2 = 3
                                        call Addicted_Ultimatum
                    else:
                                        $ Girl.Brows = "angry"
                                        $ Count2 = 2
                                        call Addicted_Ultimatum
        jump First_Addicted_End

# End Event First_Addicted /////////////////////////////////////////////////////

# Event First_Addicted2 /////////////////////////////////////////////////////
label First_Addicted2:   #rkeljsvgbdw
        # jump to from First_Addicted
        $ Girl.FaceChange("manic")
        if Girl is RogueX:
                if not Player.Male:
                    ch_r "Хорошо, помнишь тот день, когда я хотела прикоснуться к тебе, но ты отказалась?"
                else:
                    ch_r "Хорошо, помнишь тот день, когда я хотела прикоснуться к тебе, но ты отказался?"
        elif Girl is KittyX:
                if not Player.Male:
                    ch_k "Помнишь, когда я хотела прикоснуться к тебе, но ты мне ответила[Girl.like]\"Ни за что?\""
                else:
                    ch_k "Помнишь, когда я хотела прикоснуться к тебе, но ты мне ответил[Girl.like]\"Ни за что?\""
        elif Girl is EmmaX:
                if not Player.Male:
                    ch_e "Помнишь, как-то я хотела прикоснуться к тебе, а ты мне отказала?"
                else:
                    ch_e "Помнишь, как-то я хотела прикоснуться к тебе, а ты мне отказал?"
        elif Girl is LauraX:
                if not Player.Male:
                    ch_l "Слушай, помнишь тот день, когда ты не разрешила мне потрогать тебя?"
                else:
                    ch_l "Слушай, помнишь тот день, когда ты не разрешил мне потрогать тебя?"
        elif Girl is JeanX:
                if not Player.Male:
                    ch_j "Ох, слушай. . ."
                    ch_j "Помнишь тот день, когда я предложила потрогать тебя. . ."
                    ch_j "Но ты был крайне недовольна этим? . ."
                else:
                    ch_j "Ох, слушай. . ."
                    ch_j "Помнишь тот день, когда я предложила потрогать тебя. . ."
                    ch_j "Но ты был крайне недоволен этим? . ."
        elif Girl is StormX:
                ch_s "С того самого дня я не переставала думать об этом. . ."
                ch_s "Помнишь, когда я просила тебя о помощи. . ?"
        elif Girl is JubesX:
                ch_v "Слушай, эм. . . помнишь, как я хотела попить твоей крови на днях?"
        elif Girl is GwenX:
                ch_g "Слушай! Так вот. . . Помнишь, недавно я рассказывала тебе о своих желаниях?"
        elif Girl is BetsyX:
                ch_b "Помнишь тот день, когда я чувствовала себя неважно?"
        elif Girl is DoreenX:
                ch_d "Помнишь, я недавно хотела провести этот эксперимент?"
        elif Girl is WandaX:
                ch_w "Слушай, я тут еще раз поразмышляла насчет тех сил и прочего. . . ты помнишь наш прошлый разговор?"
        menu:
            extend ""
            "Ага. . .":
                pass
            "Как я могла забыть. . ." if Girl is JubesX and not Player.Male:
                pass
            "Как я мог забыть. . ." if Girl is JubesX and Player.Male:
                pass
            "Да не особо. . .":
                $ Girl.Brows = "angry"
                $ Girl.Statup("Love", 80, -3)
                $ Girl.Statup("Obed", 80, 3)
        if Girl is RogueX:
                ch_r "Я больше не могу терпеть, я чувствую. . . желание снова прикоснуться к тебе, и оно сводит меня с ума."
        elif Girl is KittyX:
                ch_k "Ну. . . понимаешь, я ворочаюсь ночами, не могу заснуть."
        elif Girl is EmmaX:
                ch_e "Мне, полагаю, становится хуже."
                ch_e "Я не могу перестать думать об этом."
        elif Girl is LauraX:
                ch_l "Мне как-то неуютно. Я правда думаю, что мне стало бы лучше, если бы я могла разок прикоснуться к тебе."
        elif Girl is JeanX:
                ch_j "Ну. . ."
                ch_j "Я решила. . . "
                ch_j ". . . в своей безграничной милости. . ."
                ch_j ". . . дать тебе еще один шанс. . ."
                ch_j ". . ."
                ch_j "Слушай, в последнее время я словно на грани."
        elif Girl is StormX:
                if not Player.Male:
                    ch_s "Ты оставила меня. . . неудовлетворённой."
                    ch_s "Я надеюсь, что, возможно, ты передумала и поможешь мне. . ."
                else:
                    ch_s "Ты оставил меня. . . неудовлетворённой."
                    ch_s "Я надеюсь, что, возможно, ты передумал и поможешь мне. . ."
        elif Girl is JubesX:
                ch_v "Так вот, с тех пор я не могу выйти нормально на улицу, и это меня очень беспокоит."
        elif Girl is GwenX:
                ch_g "Они ненадолго отступили, но потом вернулись и мне стало гораздо хуже. . ."
        elif Girl is BetsyX:
                ch_b "Да, что ж. . . Боюсь, стало только хуже."
                ch_b "Я никак не могу избавиться от этого странного чувства."
        elif Girl is DoreenX:
                ch_d "Я не могу перестать думать об этом. Словно мне в ухо залез паразит."
                ch_d "Я никак не могу выбросить тебя из головы."
        elif Girl is WandaX:
                ch_w "Думаю, дело не только в контроле над моими силами. . ."
                ch_w "Похоже, твои прикосновения вызывают что-то вроде. . . зависимости."
        menu:
            extend ""
            "Это ужасно. Ты обращалась к врачу?":
                    $ Girl.Statup("Love", 80, 5)
                    $ Girl.Statup("Obed", 80, 3)
                    if Girl is RogueX:
                            if not Player.Male:
                                ch_r "Да, очень мило, что ты спросила. Доктор МакКой сказал, что не может определить причину этого. . ."
                                ch_r "но я думаю, что это как-то связано с прикосновением к тебе."
                            else:
                                ch_r "Да, очень мило, что ты спросил. Доктор МакКой сказал, что не может определить причину этого. . ."
                                ch_r "но я думаю, что это как-то связано с прикосновением к тебе."
                    elif Girl is KittyX:
                            ch_k "Оу, это так мило. Доктор МакКой сказал, что он не может выяснить причину. . ."
                            ch_k "Но, если честно, я думаю, что прикосновение к тебе, так или иначе, важно и может помочь."
                    elif Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Да, очень мило, что ты спросила. Генри не смог определить причину. . ."
                            else:
                                ch_e "Да, очень мило, что ты спросил. Генри не смог определить причину. . ."
                            ch_e "Я считаю, что это как-то связано с прикосновением к тебе."
                    elif Girl is LauraX:
                            ch_l "О, да. МакКой сказал, что не может ничего понять. . ."
                            ch_l "Я думаю, это как-то связано с прикосновением к тебе."
                    elif Girl is JeanX:
                            $ Girl.Statup("Lust", 50, 3)
                            ch_j "Я ходила поговорить об этом с Хэнком, но мне кажется, что он слишком \"увлекся\" моим физическим состоянием. . ."
                            ch_j "В любом случае, он, кажется, решил, что это как-то связано с прикосновениями к тебе."
                    elif Girl is StormX:
                            ch_s "Это не поможет. . ."
                            ch_s "Я понимаю эти ощущения, это только моя ноша. . ."
                    elif Girl is JubesX:
                            pass
                    elif Girl is GwenX:
                            ch_g "Да, я связывалась с пушистиком, но он сказал, что здесь это обычное дело."
                            ch_g "Он сказал, что это определенно связано с твоими способностями."
                    elif Girl is BetsyX:
                            ch_b "Естественно! К сожалению, решение найти не удалось. По-видимому, это что-то вроде эпидемии."
                    elif Girl is DoreenX:
                            ch_d "Это не помогло, похоже, нет никаких физических изменений."
                    elif Girl is WandaX:
                            ch_w "Ага-ага, говорила с МакКоем об этом."
                            ch_w "Он ничего не понял, сказал, это сейчас у многих такое."
                            ch_w "И велел не приставать к нему с этим больше."
            "Так тебе и надо.":
                    $ Girl.Brows = "angry"
                    $ Girl.Mouth = "sad"
                    $ Girl.Statup("Love", 80, -7)
                    $ Girl.Statup("Obed", 80, 5)
                    if Girl is RogueX:
                        if not Player.Male:
                            ch_r "Стерва!"
                        else:
                            ch_r "Мудак!"
                    elif Girl is KittyX:
                        if not Player.Male:
                            ch_k "Дура!"
                        else:
                            ch_k "Козел!"
                    elif Girl is EmmaX:
                        ch_e "Свинья."
                    elif Girl is LauraX:
                        if not Player.Male:
                            ch_l "Сучка."
                        else:
                            ch_l "Уебок."
                    elif Girl is JeanX:
                        $ Girl.Eyes = "side"
                        ch_j "Да, может и так."
                        $ Girl.FaceChange("sly")
                    elif Girl is StormX:
                        ch_s "Это неправда!"
                    elif Girl is JubesX:
                        ch_v "Эй! Я никогда не хотела становиться вампиром!"
                    elif Girl is GwenX:
                        ch_g "Эй! Я здесь не по своей воле!"
                    elif Girl is BetsyX:
                            ch_b "Я нахожу это замечание довольно грубым."
                    elif Girl is DoreenX:
                            ch_d "Как грубо!"
                    elif Girl is WandaX:
                            ch_w "Эй, я делаю все, что в моих силах."
            "Ты пират? [[Игра слов, Роуг можно перевести как разбойница\пират]" if Girl is RogueX:
                    "Продолжение пояснений."
                    "Как я понял, типа пиратам лучше в море, чем на суше."
                    "Конец пояснений."
                    $ Girl.Brows = "confused"
                    $ Girl.Statup("Love", 80, 3)
                    $ Girl.Statup("Obed", 80, 3)
                    if not Player.Male:
                        ch_r "Аррр. Люблю девушек с чувством юмора."
                    else:
                        ch_r "Аррр. Люблю парней с чувством юмора."
            "Может, орехи сводят тебя с ума?" if Girl is DoreenX:
                    $ Girl.Brows = "angry"
                    $ Girl.Statup("Love", 80, -2)
                    $ Girl.Statup("Obed", 80, 3)
                    ch_d "Это оскорбительно для всего моего народа."
                    ch_d "Но сейчас проблема не в этом!"
            "Вот такое я оказываю влияние на людей." if Girl is not RogueX:
                    $ Girl.Brows = "confused"
                    $ Girl.Statup("Love", 80, 3)
                    $ Girl.Statup("Obed", 80, 3)
                    if Girl is KittyX:
                            ch_k "Хихи, эм, ага. . ."
                    elif Girl is EmmaX:
                            if not Player.Male:
                                ch_e "Полагаю, я не хочу знать, как ты это выяснила. . ."
                            else:
                                ch_e "Полагаю, я не хочу знать, как ты это выяснил. . ."
                    elif Girl is LauraX:
                            if not Player.Male:
                                ch_l "Серьезно?"
                                ch_l "Как -ты- это выяснила?"
                            else:
                                ch_l "Серьезно?"
                                ch_l "Как -ты- это выяснил?"
                    elif Girl is JeanX:
                            $ Girl.FaceChange("surprised")
                            $ Girl.Statup("Love", 80, 3)
                            $ Girl.Statup("Obed", 80, 2)
                            ch_j "Серьезно?"
                            $ Girl.FaceChange("angry",Eyes="side")
                            ch_j "Ну, думаю, это все объясняет. . ."
                            $ Girl.FaceChange("sly")
                    elif Girl is StormX:
                            ch_s "Судя по тому, что я слышала в кампусе, это может быть правдой. . ."
                            ch_s "Тем не менее, ты идеально подходишь для того, чтобы помочь мне."
                    elif Girl is GwenX:
                            ch_g "Ага, я слышала."
                            ch_g "Все, кто вступает с тобой в контакт, испытывают эти желания."
                    elif Girl is BetsyX:
                            ch_b "Ну, я слышала. . ."
                    elif Girl is DoreenX:
                            ch_d "Ну. . . ага!"
                            ch_d "В этом-то и проблема!"
                    elif Girl is WandaX:
                            ch_w "Было бы неплохо, если бы я с самого начала знала об этом!"
        $ Girl.FaceChange("bemused")
        if Girl is RogueX:
                ch_r "Я чувствую себя как-то странно с тех пор, как мы в последний раз касались друг друга. Я не могу ни на чем сосредоточиться."
                ch_r ". . ..В любом случае, я пересмотрела свое. . . предложение. Я буду немного более. . . открытой."
        elif Girl is KittyX:
                ch_k "В общем, это настоящая проблема. . . я не могу толком сосредоточиться. . ."
                if not Player.Male:
                    ch_k "Я была бы очень признательна, если бы ты мне помогла. . ."
                else:
                    ch_k "Я была бы очень признательна, если бы ты мне помог. . ."
        elif Girl is EmmaX:
                ch_e "Да, так вот, в последнее время я не могу заниматься своей работой, я чувствую себя очень рассеянной."
                ch_e "За твою помощь, я готова предложить кое-какую. . . компенсацию. . ."
        elif Girl is LauraX:
                ch_l "Да, меня это так выбило из колеи, теперь я пропускаю кучу даже простых ударов."
                if not Player.Male:
                    ch_l "Не могла бы ты меня выручить?"
                else:
                    ch_l "Не мог бы ты меня выручить?"
        elif Girl is JeanX:
                $ Girl.FaceChange("angry",Eyes="side")
                ch_j "В общем, мне это не нравится. . ."
                ch_j "Мне не нравится чувствовать себя. . ."
                ch_j "-хуже-, чем -безупречно.-"
                $ Girl.FaceChange("normal",Brows="sad")
                ch_j "То есть, для тебя, возможно, это и нормально, но постарайся посмотреть на это с моей стороны!"
                ch_j ". . ."
                ch_j "Ну, что скажешь? Ты мне поможешь?"
        elif Girl is StormX:
                ch_s "У меня были проблемы с концентрацией во время занятий."
                ch_s "Я считаю, что так больше не может продолжаться. . ."
        elif Girl is JubesX:
                ch_v "Ага, я ходила и к доктору МакКою, и к доктору Стрэнджу, у них было не так много предположений."
                ch_v "Они оба согласились, что это, вероятно, связано с тем, что я сосала твою кровь той ночью."
                ch_v "А еще они добавили, что с моей стороны было неправильно набрасываться на тебя без спроса. . ."
        elif Girl is GwenX:
                ch_g "Я не могу сосредоточиться."
                if not Player.Male:
                    ch_g "Думаю, я хочу вернуть свое прежнее состояние, не могла бы ты мне помочь?"
                else:
                    ch_g "Думаю, я хочу вернуть свое прежнее состояние, не мог бы ты мне помочь?"
        elif Girl is BetsyX:
                ch_b "В любом случае, я просто обязана найти способ избавиться от этой тяги, от этих. . ."
                $ Girl.FaceChange("sly",2)
                ch_b ". . . желаний."
                ch_b "Наверняка есть какой-нибудь способ, которым я могла бы убедить тебя помочь мне. . ."
        elif Girl is DoreenX:
                ch_d "Мне нужно разобраться во всем, мне нужна еще одна \"доза\", чтобы понять."
                ch_d "В моей голове начинают появляться. . . безумные мысли."
                ch_d "Даже ты не захочешь узнать, какие сны мне снились.. . ."
                ch_d "-в общем, мне нужна твоя помощь, мы можем что-нибудь придумать?"
        elif Girl is WandaX:
                ch_w "Дело не только в контроле над моими силами."
                ch_w "Я чувствую себя всё более. . . взвинченной."
                ch_w "И нет, не в том смысле, как обычно говорят, а буквально — как натянутая струна."
                ch_w "Такое ощущение, что я сейчас взорвусь изнутри. . ."
                if not Player.Male:
                    ch_w "Мне нужно, чтобы ты меня успокоила. Совсем чуть-чуть."
                else:
                    ch_w "Мне нужно, чтобы ты меня успокоил. Совсем чуть-чуть."
        $ Count2 = 2
        call Addicted_Ultimatum
        jump First_Addicted_End


# Event First_Addicted3 /////////////////////////////////////////////////////
label First_Addicted3:  #rkeljsvgbdw
        # jump to from First_Addicted
        $ Girl.Event[1] += 1
        $ Girl.FaceChange("manic",2)
        if Girl is RogueX:
                ch_r "Хорошо, я давала тебе много шансов. . . Очень много."
                ch_r "Это все сводит меня с ума, словно у меня все тело зудит, но я не могу ничего почесать."
        elif Girl is KittyX:
                ch_k "Ладно[Girl.like]серьезно, это все сводит с ума."
                ch_k "До сих пор я была ОЧЕНЬ терпеливой, с меня хватит."
        elif Girl is EmmaX:
                ch_e "Ты должен понять, [Girl. Petname], мне невероятно некомфортно."
                ch_e "Я уже давненько нормально не высыпалась, это просто невыносимо."
        elif Girl is LauraX:
                $ Girl.FaceChange("angry",Eyes="manic")
                ch_l "Эй, я не знаю, в чем тут дело, но мне это не нравится."
                ch_l "Лучше бы тебе согласиться добровольно, а не то. . ."
        elif Girl is JeanX:
                $ Girl.FaceChange("angry",Eyes="manic")
                ch_j "Черт, послушай!"
                ch_j "С меня хватит твоего \"не буду делать то, что говорит Джин\"!"
                ch_j "Чего ты хочешь от меня?!"
        elif Girl is StormX:
                $ Girl.FaceChange("angry",Eyes="white")
                ch_s "[Player.Name]!"
                ch_s "Это продолжается уже достаточно долго!"
                $ Girl.FaceChange("angry",Eyes="manic")
                ch_s "Я нахожу это. . . желание внутри меня невыносимым, это проблема, которую необходимо срочно решить!"
        elif Girl is JubesX:
                ch_v "Я, эм. . . я действительно не могу больше контролировать эту жажду. . ."
        elif Girl is GwenX:
                ch_g "Итак, смотри. . ."
                ch_g "Я не создан для таких вещей. . ."
                ch_g "Я схожу с ума."
                ch_g "Просто дай мне прикоснуться к тебе, чтобы я могла облегчить свою ношу."
        elif Girl is BetsyX:
                ch_b "Я. . . потрясена происходящим."
                ch_b "Желания только продолжают расти!"
                ch_b "Умоляю, должен же быть какой-то выход из этого безумия!"
        elif Girl is DoreenX:
                ch_d "Ладно, с меня хватит!"
                ch_d "Это уже слишком, мне сейчас же нужно решение, давай, прикоснись ко мне!"
                ch_d "Я схожу с ума! [[Игра слов в оригинале, присутствует слово \"nuts\" - \"орехи\", держите это в голове.]"
        elif Girl is WandaX:
                ch_w "Ладно, у нас тут максимальный уровень опасности, если мне не помогут, я взорвусь!"
        menu:
            extend ""
            "Держи парочку. [[Про \"орехи\"]." if Girl is DoreenX:
                    $ Girl.FaceChange("angry",2)
                    $ Girl.Statup("Love", 80, -2)
                    $ Girl.Statup("Obed", 70, 2)
                    ch_d "Да-да, очень смешно."
                    $ Girl.FaceChange("manic",2)
            "И даже доктор МакКой не смог найти причину?":
                    $ Girl.Statup("Love", 80, 5)
                    $ Girl.Statup("Obed", 50, 3)
                    if Girl is RogueX:
                            ch_r "Ничего! Он провел всевозможные тесты, но ничего так и не выяснил!"
                            ch_r "Это должно быть из-за тебя, что-то в твоем прикосновении, в твоей способности мутанта."
                    elif Girl is KittyX:
                            ch_k "Ничего! Тест за тестом и без результатов!"
                            ch_k "Это должно быть из-за тебя, что-то в твоем прикосновении, в твоей способности мутанта."
                    elif Girl is EmmaX:
                            ch_e "Нет! Так много бессмысленных тестов, это выводит меня из себя."
                            ch_e "Уверена это связана с тобой, с твоей способностью мутанта."
                    elif Girl is LauraX:
                            ch_l "Нет! Меня уже много лет так не искалывали, но все равно никаких результатов."
                            ch_l "Думаю, это должно быть твои способности или типа того."
                    elif Girl is JeanX:
                            ch_j "Я была бы рада, если бы нашел!"
                            $ Girl.Statup("Lust", 50, 3)
                            ch_j "Я дала ему все поношенные трусики, которыми он мог бы воспользоваться, но он показал себя совершенно бесполезным!"
                            ch_j "Все дело -должно быть- в твоих способностях или типа того."
                    elif Girl is StormX:
                            ch_s "Как я уже говорила, я знаю причину и я не нуждаюсь в его советах."
                    elif Girl is JubesX:
                            ch_v "Как я уже сказала, ты, похоже, мой единственный вариант!"
                    elif Girl is GwenX:
                            if not Player.Male:
                                ch_g "Кроме \"это из-за той девки-мутанта, чьи прикосновения вызывают зависимость?\" Нет."
                            else:
                                ch_g "Кроме \"это из-за того пацана-мутанта, чьи прикосновения вызывают зависимость?\" Нет."
                    elif Girl is BetsyX:
                            ch_b "Как я уже говорила, он бесполезен!"
                    elif Girl is DoreenX:
                            ch_d "Нет! Он посоветовал только \"пить молоко перед сном.\""
                            ch_d "Молоко не помогает!"
                    elif Girl is WandaX:
                            ch_w "Нет! Он тут бессилен!"
            "Ну, я сделала тебе несколько интересных предложений. . ." if not Player.Male:
                    $ Girl.Brows = "angry"
                    $ Girl.Mouth = "sad"
                    $ Girl.Statup("Love", 80, -7)
                    $ Girl.Statup("Obed", 80, 5)
                    if Girl is RogueX:
                            ch_r "Да, очень интересных."
                    elif Girl is KittyX:
                            ch_k "Да, эм. . . конечно."
                    elif Girl is EmmaX:
                            ch_e "Полагаю, возможно, я передумала. . ."
                    elif Girl is LauraX:
                            ch_l "Ага, то есть, сейчас они и правда выглядят интересно. . ."
                    elif Girl is JeanX:
                            ch_j "Бред. . ."
                            ch_j "Ты просто пыталась. . . заняться со мной разным. . ."
                            $ Girl.Statup("Obed", 50, 3)
                            $ Girl.Statup("Obed", 80, 2)
                            ch_j "Тем не менее, на данный момент. . . я. . ."
                    elif Girl is StormX:
                            ch_s "Ох, я помню твои \"предложения\"."
                            ch_s ". . ."
                            $ Girl.FaceChange("sadside",2)
                            ch_s "Я тщательно их обдумала. . ."
                    elif Girl is JubesX:
                            ch_v "Сделала!"
                    elif Girl is GwenX:
                            ch_g "Я думала, все будет не так!"
                            ch_g "Но. . . я все обдумала. . ."
                    elif Girl is BetsyX:
                            ch_b "Я. . . пересмотрела свою позицию. . ."
                    elif Girl is DoreenX:
                            ch_d "Слушай, я понимаю. За все нужно платить."
                    elif Girl is WandaX:
                            ch_w "Я поняла, что теперь за каждое прикосновение придется торговаться! Будь по-твоему."
            "Ну, я сделал тебе несколько интересных предложений. . ." if Player.Male:
                    $ Girl.Brows = "angry"
                    $ Girl.Mouth = "sad"
                    $ Girl.Statup("Love", 80, -7)
                    $ Girl.Statup("Obed", 80, 5)
                    if Girl is RogueX:
                            ch_r "Да, очень интересных."
                    elif Girl is KittyX:
                            ch_k "Да, эм. . . конечно."
                    elif Girl is EmmaX:
                            ch_e "Полагаю, возможно, я передумала. . ."
                    elif Girl is LauraX:
                            ch_l "Ага, то есть, сейчас они и правда выглядят интересно. . ."
                    elif Girl is JeanX:
                            ch_j "Бред. . ."
                            ch_j "Ты просто пытался. . . заняться со мной разным. . ."
                            $ Girl.Statup("Obed", 50, 3)
                            $ Girl.Statup("Obed", 80, 2)
                            ch_j "Тем не менее, на данный момент. . . я. . ."
                    elif Girl is StormX:
                            ch_s "Ох, я помню твои \"предложения\"."
                            ch_s ". . ."
                            $ Girl.FaceChange("sadside",2)
                            ch_s "Я тщательно их обдумала. . ."
                    elif Girl is JubesX:
                            ch_v "Сделал!"
                    elif Girl is GwenX:
                            ch_g "Я думала, все будет не так!"
                            ch_g "Но. . . я все обдумала. . ."
                    elif Girl is BetsyX:
                            ch_b "Я. . . пересмотрела свою позицию. . ."
                    elif Girl is DoreenX:
                            ch_d "Слушай, я понимаю. За все нужно платить."
                    elif Girl is WandaX:
                            ch_w "Я поняла, что теперь за каждое прикосновение придется торговаться! Будь по-твоему."

        $ Girl.Brows = "angry"
        $ Girl.Mouth = "sad"
        $ Girl.Blush = 1

        if Girl is RogueX:
                ch_r "Ну. . . Мне нужно, чтобы это закончилось. Нужно со всем поскорее разобраться. Я сделаю всё, что угодно."
        elif Girl is KittyX:
                ch_k "Ну[Girl.like]мы чем-нибудь займемся или как?"
        elif Girl is EmmaX:
                ch_e "Я буду более открытой в наших. . . переговорах. . ."
        elif Girl is LauraX:
                ch_l "Я открыта для предложений."
        elif Girl is JeanX:
                $ Girl.Statup("Obed", 50, 3)
                $ Girl.Statup("Obed", 80, 2)
                ch_j "Я так устала. . ."
        elif Girl is StormX:
                ch_s "Что нужно сделать, чтобы положить этому конец?"
        elif Girl is JubesX:
                ch_v "Наверное. . ."
                ch_v "Наверное, мне нужно просто. . . проглотить. . ."
                ch_v "свою гордость. . ."
        elif Girl is GwenX:
                ch_g "Чего ты хочешь? Я вся внимание."
        elif Girl is BetsyX:
                ch_b "Я слушаю. . ."
        elif Girl is DoreenX:
                ch_d "Скажи прямо, чего ты хочешь."
        elif Girl is WandaX:
                ch_w "Ну и чего ты хочешь?"
        $ Count2 = 2
        call Addicted_Ultimatum
        jump First_Addicted_End

# end Event First_Addicted3 /////////////////////////////////////////////////////
label Ultimatum(Girl=Ch_Focus,AddictStore=Girl.Addict):
        #Called for non-addictive version
        # call Ultimatum(RogueX,20)
label Addicted_Ultimatum(AddictStore=Girl.Addict): #rkeljsvgbdw
        #Called when you demand something for a touch. . .
        #either returns and then jumps to a good ending, or jumps to bad ending
        $ AddictStore = Girl.Addict
        $ Girl.AddWord(1,"ultimatum","ultimatum") #adds to recent and daily
        if "drugfree" in Girl.RecentActions:
                $ Tempmod = AddictStore
                $ AddictStore == Girl.Action
        else:
                $ Tempmod = int(Girl.Addict/2)
                if Girl.Addict >= 80:
                            $ Count2 += 2
                elif Girl.Addict >= 50:
                            $ Count2 += 1
                if Girl is RogueX:
                        if Girl.Event[1] == 1:
                                ch_r "Ладно, и что же тогда тебя устроит?"
                        else:
                                ch_r "Что мне нужно сделать, чтобы еще раз прикоснуться к тебе?"
                elif Girl is KittyX:
                        if Girl.Event[1] == 1:
                                ch_k "И[Girl.like]чего же ты хочешь?"
                        else:
                                ch_k "Хорошо, так что мне нужно сделать, чтобы коснуться тебя еще раз?"
                elif Girl is EmmaX:
                        if Girl.Event[1] == 1:
                                ch_e "Ну хорошо, чего ты хочешь?"
                        else:
                                ch_e "Что тогда от меня потребуется?"
                elif Girl is LauraX:
                            ch_l "Ладно, что ты хочешь?"
                elif Girl is JeanX:
                        if Girl.Event[1] == 1:
                                ch_j "Чего ты тогда хочешь?"
                        else:
                                ch_j "Что от меня потребуется?"
                elif Girl is StormX:
                            ch_s "Итак, о чем ты хочешь меня попросить?"
                elif Girl is JubesX:
                            ch_v "Что тебе от меня нужно?"
                elif Girl is GwenX:
                        if Girl.Event[1] == 1:
                                ch_g "Так какие у тебя есть предложения?"
                        else:
                                ch_g "Серьезно, дай мне какое-нибудь решение."
                elif Girl is BetsyX:
                        if Girl.Event[1] == 1:
                                ch_b "Что тебя устроит?"
                        else:
                                if not Player.Male:
                                    ch_b "Ты должна сказать мне, что тебя устроит."
                                else:
                                    ch_b "Ты должен сказать мне, что тебя устроит."
                elif Girl is DoreenX:
                        if Girl.Event[1] == 1:
                                ch_d "Чего ты хочешь?"
                        else:
                                ch_d "Ну же, должно же быть -что-то-, что я могу сделать."
                elif Girl is WandaX:
                        if Girl.Event[1] == 1:
                                ch_w "Ну и чего ты хочешь?"
                        else:
                                ch_w "Серьезно? Мы же можем найти какое-нибудь решение. . ."

        if "locked" not in Player.Traits:
                menu:
                    "Желаете сперва запереть дверь?"
                    "Да":
                            "Вы идете запирать дверь"
                            if not ApprovalCheck(Girl, 1000):
                                $ Girl.FaceChange("perplexed")
                                $ Girl.Statup("Obed", 60, 2)
                                if Girl is RogueX:
                                        ch_r "Эм, [Girl.Petname]?"
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Самая ушлая?"
                                        else:
                                            ch_k "Самый ушлый?"
                                elif Girl is EmmaX:
                                        ch_e "Почему-то я чувствую, что у тебя могут быть скрытые мотивы. . ."
                                elif Girl is LauraX:
                                        ch_l "Тревожный знак. . ."
                                elif Girl is JeanX:
                                        ch_j "Хм."
                                elif Girl is StormX:
                                        $ Girl.Statup("Love", 50, -3, -1)
                                        $ Girl.Statup("Love", 80, -2, -1)
                                        ch_s "Не уверена, что меня это устраивает. . ."
                                elif Girl is JubesX:
                                        ch_v "Лаааадно?"
                                elif Girl is GwenX:
                                        ch_g "Ох. . . ладно. . ."
                                elif Girl is BetsyX:
                                        ch_b "Мне. . . довольно жутко. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ты меня пугаешь!"
                                elif Girl is WandaX:
                                        ch_w "Воу, я уже видела подобное поведение раньше. . ."
                            $ Player.Traits.append("locked")
                            call Taboo_Level
                    "Нет":
                            pass
        while Count2:
            $ CountStore = Tempmod
            if not ApprovalCheck(Girl, 1200, "LO"):
                    $ Girl.Forced = 1
                    $ MultiAction = 0
            menu Addict_Ultimatum_Menu:
                extend ""
                "Можешь прикасаться ко мне так, как пожелаешь." if "drugfree" not in Girl.RecentActions:
                        $ Girl.Forced = 0
                        if Girl.Petname in (Terms["master"], Terms["sir"], "господин", "госпожа", "хозяин", "хозяйка"):
                                $ Girl.Statup("Lust", 80, 3)
                                $ Girl.Statup("Love", 70, 1)
                                $ Girl.Statup("Love", 95, 1)
                                $ Girl.FaceChange("sexy")
                                if Girl is RogueX:
                                        ch_r "Спасибо, [Girl.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Ох, спасибо."
                                elif Girl is EmmaX:
                                        ch_e "Ох, я благодарна тебе."
                                elif Girl is LauraX:
                                        ch_l "Спасибо, [Girl.Petname]."
                                elif Girl is JeanX:
                                        $ Girl.Statup("Love", 50, 3)
                                        $ Girl.Statup("Love", 80, 2)
                                        ch_j "Хорошо."
                                elif Girl is StormX:
                                        ch_s "Хорошо. . ."
                                elif Girl is JubesX:
                                        ch_v "Тогда, пожалуй, я выбираю. . ."
                                elif Girl is GwenX:
                                        ch_g "Ох! Спасибо! Тогда, думаю, было бы справедливо. . ."
                                elif Girl is BetsyX:
                                        ch_b "Ох! Это чудесно, спасибо. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох! Правда? . . здорово."
                                elif Girl is WandaX:
                                        ch_w "Ну, тогда я выбираю. . ."
                                "Она наклоняется, чтобы поцеловать вас."
                                call KissPrep
                        elif ApprovalCheck(Girl, 650, "LI",Alt=[[RogueX],600]):
                                $ Girl.Statup("Lust", 80, 3)
                                $ Girl.Statup("Love", 80, 5)
                                $ Girl.FaceChange("sexy")
                                if Girl is RogueX:
                                        ch_r "У меня появилась идея."
                                elif Girl is KittyX:
                                        ch_k "О, круто."
                                elif Girl is EmmaX:
                                        ch_e "Спасибо, [Girl.Petname]"
                                elif Girl is LauraX:
                                        ch_l "Ладно, клево."
                                elif Girl is JeanX:
                                        $ Girl.Statup("Love", 50, 3)
                                        $ Girl.Statup("Love", 80, 2)
                                        ch_j "Серьезно?"
                                        ch_j "Ладно."
                                elif Girl is StormX:
                                        ch_s "Хорошо. . ."
                                elif Girl is JubesX:
                                        ch_v "О! Тогда как насчет того, чтобы я слегка. . ."
                                elif Girl is GwenX:
                                        ch_g "Ох! Ну, тогда я думаю. . ."
                                elif Girl is BetsyX:
                                        ch_b "Ох! Тогда, пожалуй, я знаю, чего хочу. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох! Правда? . . здорово."
                                elif Girl is WandaX:
                                        ch_w "Лаа. . . дно."
                                "Она наклоняется, чтобы поцеловать вас."
                                call KissPrep
                        else:
                                $ Girl.Statup("Lust", 80, 3)
                                $ Girl.Statup("Love", 80, 6)
                                $ Girl.FaceChange("smile")
                                call Girl_Tag(Girl)
                        while Girl.Addict > 20 and Round > 10:
                                #should remove addiction by 1 unit per round until either it stabilizes or time runs out.
                                $ Girl.Addict -= 1
                                $ Round -= 1
                                if Round == 10:
                                        call AnyLine(Girl,"Пожалуй, у нас нет времени на большее.")
                #end "Just touch whatever you like." if "drugfree" not in Girl.RecentActions:

                "Как насчет поцелуя?":
                        if Girl.Kissed or ApprovalCheck(Girl, 600, "LI",Alt=[[RogueX,JeanX],560]) or Girl.Petname in (Terms["master"], Terms["sir"], "господин", "госпожа", "хозяин", "хозяйка"):
                                $ Girl.Forced = 0
                                $ Girl.Statup("Lust", 80, 3)
                                $ Girl.Statup("Love", 80, 6)
                                $ Girl.FaceChange("sexy")
                                if Girl is RogueX:
                                        ch_r "И все? Да, конечно, давай."
                                elif Girl is KittyX:
                                        ch_k "Ох, эм, конечно."
                                elif Girl is EmmaX:
                                        ch_e "Думаю, можно. . ."
                                elif Girl is LauraX:
                                        ch_l "Ладно."
                                elif Girl is JeanX:
                                        ch_j "Ладно, здорово."
                                elif Girl is StormX:
                                        ch_s "Поцелуй? Пожалуй, это может сработать."
                                elif Girl is JubesX:
                                        ch_v "Убедил. . ."
                                elif Girl is GwenX:
                                        ch_g "Ох! Конечно. . ."
                                elif Girl is BetsyX:
                                        ch_b "Я не возражаю. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох. . . ладно!"
                                elif Girl is WandaX:
                                        ch_w "Конечно."
                                "Она наклоняется, чтобы поцеловать вас."
                                call KissPrep
                                $ Girl.Addict = 20 if Girl.Addict > 20 else Girl.Addict
                                $ Girl.Addict = 5 if Girl is JubesX else Girl.Addict
                        else:
                                call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                                if "nogirls" in Girl.History and not Girl.Forced:
                                        #if she isn't into girls but isn't coerced. . .
                                        return
                                if Girl is RogueX:
                                        ch_r "Это очень интимное дело."
                                elif Girl is KittyX:
                                        ch_k "Я не уверена. . ."
                                elif Girl is EmmaX:
                                        ch_e "Не думаю, что это уместно. . ."
                                elif Girl is LauraX:
                                        ch_l "Эм. . . нет."
                                elif Girl is JeanX:
                                        ch_j "Эм. . . нет?"
                                elif Girl is StormX:
                                        ch_s "Нет. . . Сомневаюсь, что это сработает."
                                elif Girl is JubesX:
                                        ch_v "Ты мне не нравишься таким. . ."
                                elif Girl is GwenX:
                                        ch_g "Эм, я не очень этого хочу. . ."
                                elif Girl is BetsyX:
                                        ch_b "Я бы предпочла этого не делать. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох. . . эм, пожалуй, воздержусь."
                                elif Girl is WandaX:
                                        ch_w "Я так не думаю."
                #end "How about a kiss?":

                "Позволишь мне прикоснуться к тебе?":
                        if Girl is RogueX:
                                ch_r "Даже не знаю, [Girl.Petname]. А поподробнее?"
                        elif Girl is KittyX:
                                ch_k "Я не знаю[Girl.like]можешь уточнить, что именно ты хочешь, [Girl.Petname]?"
                        elif Girl is EmmaX:
                                ch_e "Я не уверена, [Girl.Petname]. Расскажешь, что у тебя на уме?"
                        elif Girl is LauraX:
                                ch_l "Так, а что конкретно ты предлагаешь?"
                        elif Girl is JeanX:
                                $ Girl.Statup("Obed", 50, 3)
                                ch_j "Хочешь полапать меня?"
                        elif Girl is StormX:
                                ch_s "Хммм. . . Не нравится мне, к чему все идет. . ."
                        elif Girl is JubesX:
                                ch_v "Ох, я не знаю. . ."
                        elif Girl is GwenX:
                                ch_g "Л-ладно. . . к чему, например?"
                        elif Girl is BetsyX:
                                ch_b "Ладно. . . могу я спросить, к чему ты хочешь прикоснуться? . ."
                        elif Girl is DoreenX:
                                ch_d "Ох. Эм. . . Думаю, это зависит от обстоятельств. К чему ты хочешь прикоснуться?"
                        elif Girl is WandaX:
                                ch_w "Ох, как знакомо. . ."

                        menu:
                            extend ""
                            "Как насчет массажа?":
                                    call Massage_Prep
                                    "[Girl.Name] встает на ноги."
                                    if Girl.Addict >= 50:
                                            call Girl_Tag(Girl)
                            #end massage

                            "Как насчет позволить мне потрогать твою грудь?":
                                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                                    $ CountStore = Tempmod
                                    call Top_Off(Girl,2)
                                    $ Tempmod = CountStore
                                    call Girl_Fondle_Breasts # call expression Girl.Tag + "_Fondle_Breasts"
                                    if "fondle breasts" in Girl.RecentActions:
                                            $ Girl.Statup("Obed", 80, 10)
                                            $ Girl.Statup("Inbt", 80, 10)
                                            if Girl is RogueX:
                                                    ch_r "Надеюсь, этого было достаточно."
                                            elif Girl is KittyX:
                                                    ch_k "Этого достаточно?"
                                            elif Girl is EmmaX:
                                                    ch_e "Думаю, этого достаточно."
                                            elif Girl is LauraX:
                                                    ch_l "Этого ведь достаточно, верно?"
                                            elif Girl is JeanX:
                                                    if not Player.Male:
                                                        ch_j "Ну, ты удовлетворена?"
                                                    else:
                                                        ch_j "Ну, ты удовлетворен?"
                                            elif Girl is StormX:
                                                    ch_s "Уверена, этого было достаточно. . ."
                                            elif Girl is JubesX:
                                                    ch_v "Значит, честная сделка?"
                                            elif Girl is GwenX:
                                                    ch_g "Ну, все было хорошо, правда?"
                                            elif Girl is BetsyX:
                                                    if not Player.Male:
                                                        ch_b "Ты ведь удовлетворена?"
                                                    else:
                                                        ch_b "Ты ведь удовлетворен?"
                                            elif Girl is DoreenX:
                                                    ch_d "Тебе ведь этого достаточно, да?"
                                            elif Girl is WandaX:
                                                    ch_w "Хорошо, мы в расчете?"


                            "Как насчет позволить мне потрогать твои ножки?":
                                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                                    $ CountStore = Tempmod
                                    call Bottoms_Off(Girl,2)
                                    $ Tempmod = CountStore
                                    if Girl.PantsNum() > 6 or Girl.HoseNum() >= 5:
                                            if Girl is RogueX:
                                                    ch_r "Хорошо, но после этого я тоже к тебе прикоснусь."
                                            elif Girl is KittyX:
                                                    ch_k "Конечно, но после этого мне все равно нужно будет к тебе прикоснуться."
                                            elif Girl is EmmaX:
                                                    ch_e "Ладно, но мне все равно понадобиться потрогать тебя."
                                            elif Girl is LauraX:
                                                    ch_l "Да, но после этого мне нужно будет прикоснуться к тебе."
                                            elif Girl is JeanX:
                                                    ch_j "Хорошо, но после этого ты должен позволить мне прикоснуться к тебе. . ."
                                            elif Girl is StormX:
                                                    ch_s "Ладно, до тех пор, пока ты готов дать то, что мне нужно."
                                            elif Girl is JubesX:
                                                    ch_v "Ладно, посмотрим. . ."
                                            elif Girl is GwenX:
                                                    ch_g "Хорошо, но. . . Думаю, мне нужен будет более прямой контакт?"
                                            elif Girl is BetsyX:
                                                    ch_b "Что ж. . . ладно, но потом мне будет нужен более прямой контакт."
                                            elif Girl is DoreenX:
                                                    ch_d "Ладно, но потом я ведь смогу прикоснуться к тебе?"
                                            elif Girl is WandaX:
                                                    ch_w "И тогда я смогу прикоснуться к тебе?"
                                    call Girl_Fondle_Thighs # call expression Girl.Tag + "_Fondle_Thighs"
                                    if "fondle thighs" in Girl.RecentActions:
                                            $ Girl.Statup("Obed", 50, 5)
                                            $ Girl.Statup("Inbt", 50, 5)
                                            if Girl is RogueX:
                                                    ch_r "Надеюсь, этого было достаточно."
                                            elif Girl is KittyX:
                                                    ch_k "Этого достаточно?"
                                            elif Girl is EmmaX:
                                                    ch_e "Думаю, этого достаточно."
                                            elif Girl is LauraX:
                                                    ch_l "Этого ведь достаточно, верно?"
                                            elif Girl is JeanX:
                                                    ch_j "Ну, ты удовлетворен?"
                                            elif Girl is StormX:
                                                    ch_s "Пожалуй, этого было достаточно?"
                                            elif Girl is JubesX:
                                                    ch_v "Значит, честная сделка?"
                                            elif Girl is GwenX:
                                                    ch_g "Ну, все было хорошо, правда?"
                                            elif Girl is BetsyX:
                                                    if not Player.Male:
                                                        ch_b "Ты ведь удовлетворена?"
                                                    else:
                                                        ch_b "Ты ведь удовлетворен?"
                                            elif Girl is DoreenX:
                                                    ch_d "Тебе ведь этого достаточно, да?"
                                            elif Girl is WandaX:
                                                    ch_w "Хорошо, мы в расчете?"
                                            if Girl.PantsNum() > 6 or Girl.HoseNum() >= 5:
                                                    call Girl_Tag(Girl)

                            "Как насчет позволить мне потрогать твою киску?":
                                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                                    $ CountStore = Tempmod
                                    call Bottoms_Off(Girl,0)
                                    $ Tempmod = CountStore
                                    call Girl_Fondle_Pussy # call expression Girl.Tag + "_Fondle_Pussy"
                                    if "fondle pussy" in Girl.RecentActions:
                                            $ Girl.Statup("Obed", 50, 10)
                                            $ Girl.Statup("Obed", 80, 5)
                                            $ Girl.Statup("Inbt", 50, 10)
                                            $ Girl.Statup("Inbt", 80, 5)
                                            if Girl is RogueX:
                                                    ch_r "Надеюсь, этого было достаточно."
                                            elif Girl is KittyX:
                                                    ch_k "Этого достаточно?"
                                            elif Girl is EmmaX:
                                                    ch_e "Думаю, этого достаточно."
                                            elif Girl is LauraX:
                                                    ch_l "Этого ведь достаточно, верно?"
                                            elif Girl is JeanX:
                                                    ch_j "Ну, ты удовлетворен?"
                                            elif Girl is StormX:
                                                    ch_s "Этого должно было быть более чем достаточно."
                                            elif Girl is JubesX:
                                                    ch_v "Этого ведь было достаточно, да?"
                                            elif Girl is GwenX:
                                                    ch_g "Ну, все было хорошо, правда?"
                                            elif Girl is BetsyX:
                                                    if not Player.Male:
                                                        ch_b "Ты ведь удовлетворена?"
                                                    else:
                                                        ch_b "Ты ведь удовлетворен?"
                                            elif Girl is DoreenX:
                                                    ch_d "Тебе ведь этого достаточно, да?"
                                            elif Girl is WandaX:
                                                    ch_w "Хорошо, мы в расчете?"
                            "Неважно [[выбрать что-нибудь другое]":
                                    jump Addict_Ultimatum_Menu
                #end "You could let me touch you?":

                "Можешь потрогать меня между ног. . .":
                        menu:
                            "Как насчет того, чтобы подрочить мне?" if Player.Male:
                                    call Girl_Handjob # call expression Girl.Tag + "_Handjob"
                            "Как насчет того, чтобы отсосать мне?" if Player.Male:# and Girl is not GwenX: #Fix when adding new girls
                                    call Girl_Blowjob # call expression Girl.Tag + "_Blowjob"
                            "Как насчет того, чтобы подрочить мне сиськами?" if Player.Male:# and Girl is not GwenX: #Fix when adding new girls
                                    call Girl_Titjob # call expression Girl.Tag + "_Titjob"

                            "Как насчет того, чтобы поиграть с моей киской?" if not Player.Male:
                                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                                    call Girl_Finger
                            "Как насчет того, чтобы отлизать мне?" if not Player.Male:# and Girl is not GwenX: #Fix when adding new girls
                                    call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                                    call Girl_CUN

                            "Неважно [[выбрать что-нибудь другое]":
                                    jump Addict_Ultimatum_Menu

                        if "angry" not in Girl.RecentActions:
                                if "blow" in Girl.RecentActions or "hand" in Girl.RecentActions or "titjob" in Girl.RecentActions or "finger" in Girl.RecentActions or "cun" in Girl.RecentActions:
                                            $ Girl.Statup("Obed", 50, 10)
                                            $ Girl.Statup("Obed", 80, 5)
                                            $ Girl.Statup("Inbt", 50, 10)
                                            $ Girl.Statup("Inbt", 80, 5)
                                            if Girl is RogueX:
                                                    ch_r "Надеюсь, этого было достаточно."
                                            elif Girl is KittyX:
                                                    ch_k "Этого достаточно?"
                                            elif Girl is EmmaX:
                                                    ch_e "Думаю, этого достаточно."
                                            elif Girl is LauraX:
                                                    ch_l "Этого ведь достаточно, верно?"
                                            elif Girl is JeanX:
                                                    ch_j "Ну, ты удовлетворен?"
                                            elif Girl is StormX:
                                                    ch_s "Этого должно было быть более чем достаточно."
                                            elif Girl is JubesX:
                                                    ch_v "Этого ведь было достаточно, да?"
                                            elif Girl is GwenX:
                                                    ch_g "Ну, все было хорошо, правда?"
                                            elif Girl is BetsyX:
                                                    if not Player.Male:
                                                        ch_b "Ты ведь удовлетворена?"
                                                    else:
                                                        ch_b "Ты ведь удовлетворен?"
                                            elif Girl is DoreenX:
                                                    ch_d "Тебе ведь этого достаточно, да?"
                                            elif Girl is WandaX:
                                                    ch_w "Хорошо, мы в расчете?"
                #end "You could touch me.":

                "Можешь станцевать стриптиз?":
                        call expression Girl.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                        $ CountStore = Girl.ClothingCheck()
                        call Group_Strip(Girl)

                        if "drugfree" in Girl.RecentActions:
                            if Girl.Loc != bg_current:
                                        $ Girl.Loc = bg_current
                                        call Set_The_Scene
                                        "Спустя мгновение [Girl.Name] возвращается, но она не выглядит довольной."
                        else:
                            if Girl.Loc != bg_current:
                                    jump Misplaced
                            menu:
                                "Ладно, хватит, можешь прикоснуться ко мне.":
                                    call Girl_Tag(Girl)
                                    $ Girl.Statup("Obed", 50, 10)
                                    $ Girl.Statup("Inbt", 50, 10)
                                "Слабовато, я хочу большего.":
                                    $ Girl.FaceChange("angry")
                                    if CountStore > Girl.ClothingCheck() and Girl.ClothingCheck() < 3 and "addstrip" not in Girl.DailyActions:
                                            #if she is wearing less than before. . .
                                            $ Girl.Statup("Love", 200, -40)
                                            $ Girl.Statup("Inbt", 50, 5)
                                            $ Girl.Statup("Obed", 50, 20)
                                            if Girl is RogueX:
                                                    ch_r "Я зашла так далеко и вдруг ты решаешь сменить условия?!"
                                            elif Girl is KittyX:
                                                    ch_k "Эй! Я. . . зря раздевалась?"
                                            elif Girl is EmmaX:
                                                    ch_e "Я переступила через себя, а ты. . ."
                                            elif Girl is LauraX:
                                                    if not Player.Male:
                                                        ch_l "Эй, ты свое получила."
                                                    else:
                                                        ch_l "Эй, ты свое получил."
                                            elif Girl is JeanX:
                                                    ch_j "Бред, я все выполнила на пятерочку."
                                            elif Girl is StormX:
                                                    if not Player.Male:
                                                        ch_s "Не могу представить, что ты ожидала большего."
                                                    else:
                                                        ch_s "Не могу представить, что ты ожидал большего."
                                            elif Girl is JubesX:
                                                    ch_v "Чего еще ты ждешь?!"
                                            elif Girl is GwenX:
                                                    ch_g "Эй, думаю, я подарила тебе превосходный стриптиз!"
                                            elif Girl is BetsyX:
                                                    ch_b "Извини, что я -недостаточно- выставила себя на посмешище!"
                                            elif Girl is DoreenX:
                                                    ch_d "Ну. . . эм. . . это все, что я хотела тебе показать сейчас!"
                                            elif Girl is WandaX:
                                                    ch_w "Этого разве не достаточно?"
                                            $ Girl.AddWord(1,0,"addstrip") # daily
#                                            jump Addicted_Bad_End
                                    else:
                                            if Girl is RogueX:
                                                    ch_r "Ты серьезно? Что еще ты хочешь от меня?"
                                            elif Girl is KittyX:
                                                    ch_k "Тебе этого мало?!"
                                            elif Girl is EmmaX:
                                                    ch_e "Думаю, этого было -более- чем достаточно."
                                            elif Girl is LauraX:
                                                    ch_l "Это совсем не клево."
                                            elif Girl is JeanX:
                                                    ch_j "Ну. . . это все на что ты можешь расчитывать!"
                                            elif Girl is StormX:
                                                    ch_s "Что ж. .  какая жалость."
                                            elif Girl is JubesX:
                                                    ch_v "-Фи-"
                                            elif Girl is GwenX:
                                                    ch_g "Ну. . .что еще я могу сделать?"
                                            elif Girl is BetsyX:
                                                    ch_b "Уверена, качество важнее количества. . ."
                                            elif Girl is DoreenX:
                                                    ch_d "Ну. . . Я просто не хотела показывать большего. . ."
                                            elif Girl is WandaX:
                                                    ch_w "Сейчас я не хочу больше ничего показывать."
                                #end "strip for me":


                "У меня есть пару идей. . ." if Girl.Event[1] >= 10:
                            call SexMenu # call expression Girl.Tag + "_SexMenu"

                "А если я предложу решить твою проблему с помощью кое-какого . . . вещества?" if Girl.Event[1] >= 10 and Player.Semen and not Girl.Chat[2] and "drugfree" not in Girl.RecentActions:
                            #Serum first time
                            call Addicted_Serum
                "Может, немного \"сыворотки\"?" if Girl.Event[1] >= 10 and Player.Semen and Girl.Chat[2] and "drugfree" not in Girl.RecentActions:
                            #Would you like some serum?
                            call Addicted_Serum

                "Неа, тут я тебе не помогу":
                        if "drugfree" in Girl.RecentActions:
                                $ Count2 = 0
                                return
                        elif Girl.Event[1] >= 10:
                                #if you've already cleared this event
                                call Addicted_Fix_Beg
                        elif Girl.Addict >= 70:
                                $ Girl.FaceChange("angry",2)
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.Statup("Obed", 80, 3)
                                if Girl is RogueX:
                                        ch_r "Пойми, меня не устроит ответ \"нет\"."
                                elif Girl is KittyX:
                                        ch_k "Угу, подумай-ка получше."
                                elif Girl is EmmaX:
                                        ch_e "Боюсь, тебе понадобится ответ получше."
                                elif Girl is LauraX:
                                        ch_l "Нееееа."
                                elif Girl is JeanX:
                                        $ Girl.Statup("Obed", 50, 3)
                                        ch_j "Последний человек, сказавший мне \"нет\", не помнит кто он такой!"
                                elif Girl is StormX:
                                        ch_s ". . ."
                                        ch_s "Какая досада."
                                elif Girl is JubesX:
                                        ch_v "Я очень не -хочу- тебя убивать. . ."
                                elif Girl is GwenX:
                                        ch_g "Ну. . . тебе нельзя так говорить!"
                                elif Girl is BetsyX:
                                        ch_b "Боюсь, я не могу принять отказ."
                                elif Girl is DoreenX:
                                        ch_d "Я. . . я одна не смогу справиться!"
                                elif Girl is WandaX:
                                        if not Player.Male:
                                            ch_w "Мне нужно, чтобы ты нашла выход."
                                        else:
                                            ch_w "Мне нужно, чтобы ты нашел выход."
                                $ Count2 = 0
                        else:
                                $ Girl.FaceChange("angry",2)
                                $ Girl.Statup("Love", 200, -30)
                                $ Girl.Statup("Obed", 200, 5)
                                if Girl is RogueX:
                                        ch_r "Ну и ладно!"
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Дура!"
                                        else:
                                            ch_k "Придурок!"
                                elif Girl is EmmaX:
                                        ch_e "Ну и отлично!"
                                elif Girl is LauraX:
                                        ch_l "Пфф!"
                                elif Girl is JeanX:
                                        $ JeanX.Eyes = "psychic"
                                        ch_j "Рррр!"
                                        $ JeanX.Eyes = "normal"
                                elif Girl is StormX:
                                        $ StormX.Eyes = "white"
                                        ch_s ". . ."
                                        $ StormX.Eyes = "squint"
                                elif Girl is JubesX:
                                        ch_v "Сладких-"
                                        ch_v "-Снов."
                                elif Girl is GwenX:
                                        ch_g "Но-"
                                        ch_g "Но мне это нужно!"
                                elif Girl is BetsyX:
                                        ch_b "Я. . . не привыкла к такому обращению."
                                elif Girl is DoreenX:
                                        ch_d "ЛАДНО!"
                                elif Girl is WandaX:
                                        ch_w "Ладно. . . пока я от тебя отстану. . ."
                                "[Girl.Name] в последний раз оглядывается через плечо, прежде чем выскочить наружу и захлопнуть дверь."
                                call Remove_Girl(Girl)
                                jump Addicted_Bad_End
                #end "Nope, you're on your own":

            if "drugfree" in Girl.RecentActions:
                    #used for non-addictive checks
                    call AnyLine(Girl,"Этого достаточно?")
                    menu:
                            extend ""
                            "Ага.":
                                    $ Count2 = 0
                                    $ Player.AddWord(1,"deal "+Girl.Tag) #you agreed, added to recent
                            "Нет.":
                                    $ Count2 -= 1
                                    if Count2 >= 0:
                                        jump Addict_Ultimatum_Menu
                                    $ Girl.FaceChange("angry",1)
                                    if AddictStore > Girl.Action:
                                            #If she did something for you. . .
                                            if not Player.Male:
                                                call AnyLine(Girl,"Но я сделала то, что ты хотела.")
                                            else:
                                                call AnyLine(Girl,"Но я сделала то, что ты хотел.")
                                            $ Girl.AddWord(1,"backsy","backsy") #you backed out on her, added to recent, daily
                                    else:
                                            call AnyLine(Girl,"Что ж, плохо.")
                    return
            if "angry" in Girl.RecentActions:
                    #if you pissed her off. . .
                    $ Girl.FaceChange("angry",2)
                    if Girl.Addict >= 80:
                            if Girl is RogueX:
                                    ch_r "Если бы я сейчас не чувствовала себя такой взвинченной, то я бы. . ."
                            elif Girl is KittyX:
                                    ch_k "Я бы тебя ударила, если бы меня сейчас не пошатывало. . ."
                            elif Girl is EmmaX:
                                    ch_e "Ох, если бы моя голова сейчас не раскалывалась, то я бы. . ."
                            elif Girl is LauraX:
                                    ch_l "Тебе повезло, что я сейчас едва вижу. . ."
                            elif Girl is JeanX:
                                    ch_j "У меня сейчас такая мигрень. . ."
                            elif Girl is StormX:
                                    ch_s ". . ."
                            elif Girl is JubesX:
                                    ch_v "Грррр. . ."
                            elif Girl is GwenX:
                                    ch_g "Я схожу с ума!"
                            elif Girl is BetsyX:
                                    ch_b "Все просто отвратительно, это должно прекратиться."
                            elif Girl is DoreenX:
                                    ch_d "У меня все. . . плывет. . . перед глазами. . ."
                            elif Girl is WandaX:
                                    ch_w "Я едва держусь на ногах. . ."
                    else:
                            if Girl is RogueX:
                                    ch_r "Это того не стоит. Я ухожу."
                            elif Girl is KittyX:
                                    ch_k "Нет, это уже слишком, я ухожу."
                            elif Girl is EmmaX:
                                    ch_e "Боюсь, что ты переоцениваешь себя, [Girl.Petname]."
                            elif Girl is LauraX:
                                    if not Player.Male:
                                        ch_l "Нет, ты зашла слишком далеко, [Girl.Petname]."
                                    else:
                                        ch_l "Нет, ты зашел слишком далеко, [Girl.Petname]."
                            elif Girl is JeanX:
                                    ch_j "Да пошло все нахуй!"
                                    ch_j "Блять!"
                            elif Girl is StormX:
                                    ch_s ". . ."
                            elif Girl is JubesX:
                                    ch_v "Ну и наглость!"
                            elif Girl is GwenX:
                                    if not Player.Male:
                                        ch_g "Не думала, что ты такой!"
                                    else:
                                        ch_g "Не думала, что ты такая!"
                            elif Girl is BetsyX:
                                    if not Player.Male:
                                        ch_b "Ебнутая пиздень!"
                                    else:
                                        ch_b "Ебнутый педик!"
                            elif Girl is DoreenX:
                                    ch_d "ЛАДНО!"
                            elif Girl is WandaX:
                                    ch_w "Ладно. . . пока я от тебя отстану. . ."
                            jump Addicted_Bad_End

            if Girl.Addict <= 20:
                    # if you've settled her down. . .
                    return
            $ Tempmod = CountStore
            if not Girl.Action:
                        #if she's out of actions, worn out
                        $ Girl.FaceChange("sad",2,Mouth="smirk")
                        if Count2:
                            if Girl is RogueX:
                                    ch_r "[[тяжело дышит] Давай перейдем уже к делу, [Player.Name]. . ."
                                    ch_r "[[тяжело дышит] Я не могу продолжать весь день."
                            elif Girl is KittyX:
                                    ch_k "[[тяжело дышит] Давай ближе к делу, [Player.Name]. . ."
                                    ch_k "[[тяжело дышит] Я уже замучилась. . ."
                            elif Girl is EmmaX:
                                    ch_e "[[тяжело дышит] Давай побыстрее закончим, [Player.Name]. . ."
                                    ch_e "[[тяжело дышит] У меня еще есть дела."
                            elif Girl is LauraX:
                                    ch_l "Эй, эм, давай уже ближе к делу, [Player.Name]. . ."
                                    ch_l "У меня еще есть дела. . ."
                            elif Girl is JeanX:
                                    ch_j "[[тяжело дышит] Эй, эм, [Player.Name]. . ."
                                    ch_j "[[тяжело дышит] Я бы хотела поскорее закончить. . ."
                            elif Girl is StormX:
                                    ch_s "[[тяжело дышит] Я не могу продолжать весь день. . ."
                            elif Girl is JubesX:
                                    ch_v "[[тяжело дышит] Я немного устала. . ."
                            elif Girl is GwenX:
                                    ch_g "[[тяжело дышит] Ну. . . Я немного устала. . ."
                                    ch_g "Меня хватит только еще на один раз. . ."
                            elif Girl is BetsyX:
                                    ch_b "[[тяжело дышит] Я уже вымотана, [Player.Name]."
                                    ch_b "[[тяжело дышит] Возможно, меня еще хватит на один раз. . ."
                            elif Girl is DoreenX:
                                    ch_d "[[тяжело дышит] Я, эм. . . совсем выдохлась, [Player.Name]."
                                    ch_d "Меня, может хватит, еще на один заход. . . последний. . ."
                            elif Girl is WandaX:
                                    ch_w "[[тяжело дышит] Я несколько утомилась [Player.Name]."
                                    ch_w "Мы можем завершить все следующим действием. . ?"
                            $ Girl.Action = 1
                        else:
                            if Girl is RogueX:
                                    ch_r "[[тяжело дышит] Ладно, я больше не могу. . ."
                            elif Girl is KittyX:
                                    ch_k "[[тяжело дышит] Фух, хватит, хватит. . ."
                            elif Girl is EmmaX:
                                    ch_e "[[тяжело дышит] Думаю, нам придется на этом закончить. . ."
                            elif Girl is LauraX:
                                    ch_l "Ладно, У меня еще есть дела, так что. . ."
                            elif Girl is JeanX:
                                    ch_j "[[тяжело дышит] Ладно. . . пока хватит. . ."
                            elif Girl is StormX:
                                    ch_s "[[тяжело дышит] Я больше не могу продолжать. . ."
                            elif Girl is JubesX:
                                    ch_v "[[тяжело дышит] Я больше не могу. . ."
                            elif Girl is GwenX:
                                    ch_g "[[тяжело дышит] Ну . . Я немного устала. . ."
                            elif Girl is BetsyX:
                                    ch_b "[[тяжело дышит] Мне больше нечего тебе дать."
                            elif Girl is DoreenX:
                                    ch_d "[[тяжело дышит] Я все. . ."
                            elif Girl is WandaX:
                                    ch_w "[[тяжело дышит] Мне нужно передохнуть. . ."
                            jump Addicted_Bad_End
            if not Count2 and ApprovalCheck(Girl, 1200, "LO"):
                    # if she likes/obeys you, she'll keep giving you chances.
                    $ Count2 += 1
            if Count2 and Girl.Addict <= AddictStore:
                            #if you've drained it a bit, but not enough. . .
                            $ Girl.FaceChange("sad",2,Mouth="smile")
                            if Girl is RogueX:
                                    ch_r "Мне нужно немного больше. . ."
                            elif Girl is KittyX:
                                    ch_k "Я все еще чувствую себя не очень. . ."
                            elif Girl is EmmaX:
                                    ch_e "Этого все еще недостаточно. . ."
                            elif Girl is LauraX:
                                    ch_l "Я все еще плохо себя чувствую. . ."
                            elif Girl is JeanX:
                                    ch_j "Этого. . . все еще недостаточно. . ."
                            elif Girl is StormX:
                                    ch_s ". . . все еще недостаточно. . ."
                            elif Girl is JubesX:
                                    ch_v "Этого. . . недостаточно. . ."
                            elif Girl is GwenX:
                                    ch_g "Это было. . .  что-то. . . но мне этого мало."
                            elif Girl is BetsyX:
                                    ch_b "Я действительно чувствую себя немного лучше, хотя и недостаточно."
                            elif Girl is DoreenX:
                                    ch_d "Вроде как сработало, только недостаточно хорошо. . ."
                            elif Girl is WandaX:
                                    ch_w "Так -немного- лучше, но, думаю, мне нужно еще. . ."
            elif Girl.Addict >= 80:
                    #if she's extra strung out, and hasn't done anything this cycle. . .
                    $ Girl.FaceChange("sad",2,Mouth="smile")
                    if Count2 > 3:
                            if Girl is RogueX:
                                    ch_r "Я бы не хотела этого делать. . ."
                            elif Girl is KittyX:
                                    ch_k "Это не совсем то, чего мне бы хотелось. . ."
                            elif Girl is EmmaX:
                                    ch_e "Ты хочешь зайти слишком далеко. . ."
                            elif Girl is LauraX:
                                    ch_l "Да ладно тебе, это не клево. . ."
                            elif Girl is JeanX:
                                    ch_j "Серьезно, ты испытываешь свою удачу. . ."
                            elif Girl is StormX:
                                    ch_s "Уверена, мы могли бы заняться чем-нибудь другим. . ."
                            elif Girl is JubesX:
                                    ch_v "Разве мы не можем заняться чем-нибудь другим? . ."
                                    $ Tempmod -= 3
                            elif Girl is GwenX:
                                    ch_g "Серьезно, играй честно. . ."
                            elif Girl is BetsyX:
                                    ch_b "Это просто невозможно. . ."
                            elif Girl is DoreenX:
                                    ch_d "Я не могу этого сделать!"
                            elif Girl is WandaX:
                                    ch_w "Ты хочешь от меня слишком многого!"
                            $ Tempmod += 5
                    elif Count2 > 2:
                            if Girl is RogueX:
                                    ch_r "Но. . . я просто не могу. . ."
                            elif Girl is KittyX:
                                    ch_k "Но. . . да ладно тебе. . ."
                            elif Girl is EmmaX:
                                    ch_e "Уверена, должно найтись что-нибудь, с чем мы оба сможем согласиться. . ."
                            elif Girl is LauraX:
                                    ch_l "Серьёзно, [Girl.Petname]. . ."
                            elif Girl is JeanX:
                                    ch_j "Но. . ."
                                    ch_j "Ты серьезно?!"
                            elif Girl is StormX:
                                    ch_s "Ты серьезно?"
                                    $ Tempmod -= 5
                            elif Girl is JubesX:
                                    ch_v "Что еще у тебя на уме?"
                            elif Girl is GwenX:
                                    ch_g "Это. . . должно быть что-то еще, чего ты хочешь. . ."
                            elif Girl is BetsyX:
                                    ch_b "У меня же. . . тоже должны быть свои пределы. . . не так ли?"
                            elif Girl is DoreenX:
                                    ch_d "Ты, должно быть, шутишь!"
                            elif Girl is WandaX:
                                    ch_w "Да ладно тебе, ты, должно быть, шутишь. . ."
                            $ Tempmod += 10
                    elif Count2 > 1:
                            $ Girl.FaceChange("sad",2)
                            if Girl is RogueX:
                                    if not Player.Male:
                                        ch_r "ПОЖАЛУЙСТА, я тебя умоляю, будь рассудительной!"
                                    else:
                                        ch_r "ПОЖАЛУЙСТА, я тебя умоляю, будь рассудительным!"
                            elif Girl is KittyX:
                                    ch_k "Да ладно! Я умоляю тебя. . ."
                            elif Girl is EmmaX:
                                    ch_e "Оставь мне хоть немного достоинства. . ."
                            elif Girl is LauraX:
                                    if not Player.Male:
                                        ch_l "Ты должна. . . пожалуйста?"
                                    else:
                                        ch_l "Ты должен. . . пожалуйста?"
                            elif Girl is JeanX:
                                    ch_j "Я. . ."
                                    ch_j "Ты. . ."
                                    ch_j ". . ."
                                    ch_j "Пожалуйста. . ."
                            elif Girl is StormX:
                                    if not Player.Male:
                                        ch_s "Не могла бы ты быть более разумной?"
                                    else:
                                        ch_s "Не мог бы ты быть более разумным?"
                                    $ Tempmod -= 10
                            elif Girl is JubesX:
                                    ch_v "Дай мне больше выбора. . ."
                            elif Girl is GwenX:
                                    ch_g "Пожалуйста?"
                            elif Girl is BetsyX:
                                    ch_b "Я молю тебя о милосердии. . ."
                            elif Girl is DoreenX:
                                    ch_d "Я не могу, серьезно!"
                            elif Girl is WandaX:
                                    ch_w "Не получится!"
                            $ Tempmod += 20
            else:
                    #she's not super strung out, and is refusing to do anything
                    if Count2 > 2:
                            $ Girl.FaceChange("angry",2,Mouth="smile")
                            if Girl is RogueX:
                                    ch_r "Попробуй что-нибудь другое, мне это не нравится."
                            elif Girl is KittyX:
                                    ch_k "Неужели я ничего не могу сейчас сделать?"
                            elif Girl is EmmaX:
                                    ch_e "Ты, наверное, шутишь, мы должны прийти к взаимовыгодному соглашению."
                            elif Girl is LauraX:
                                    ch_l "Нет, будь серьёзней."
                            elif Girl is JeanX:
                                    ch_j "Ага, я не согласна."
                            elif Girl is JubesX:
                                    ch_v "Определенно нет. . ."
                            elif Girl is GwenX:
                                    ch_g "Это. . . неуместно."
                            elif Girl is BetsyX:
                                    ch_b "Это совершенно неуместно."
                            elif Girl is DoreenX:
                                    ch_d "Я не могу на это пойти!"
                            elif Girl is WandaX:
                                    ch_w "Послушай, это уже слишком. . ."
                    elif Count2 > 1:
                            if Girl is RogueX:
                                    ch_r "Да ладно тебе, разве я ничего не могу сейчас сделать?"
                            elif Girl is KittyX:
                                    ch_k "Дай мне передохнуть."
                            elif Girl is EmmaX:
                                    ch_e "Должно же быть что-то, чего ты хочешь. . ."
                            elif Girl is LauraX:
                                    ch_l "Давай, давай сделаем это."
                            elif Girl is JeanX:
                                    ch_j "Будь серьезней, [Girl.Petname]."
                            elif Girl is StormX:
                                    ch_s ". . . Я не могу."
                                    $ Tempmod -= 5
                            elif Girl is JubesX:
                                    ch_v "Я. . . не могу. . ."
                            elif Girl is GwenX:
                                    ch_g "Но. . . нет, мы можем попробовать что-нибудь другое?"
                            elif Girl is BetsyX:
                                    ch_b "Ты серьезно сейчас не шутишь надо мной?"
                            elif Girl is DoreenX:
                                    ch_d "Перестань дурачиться!"
                            elif Girl is WandaX:
                                    ch_w "Хватит валять дурака. . ."
                            $ Tempmod += 10
            call Taboo_Level
            $ Count2 -= 1 if Count2 > 0 else 0
            $ Round -= 10 if Round >= 21 else Round - 10
        #End While loop

        if Girl.Addict >= 80:
                #if you're well over the limits
                $ Girl.FaceChange("angry")
                "[Girl.Name] прямо кипит от ярости."
                $ Girl.Statup("Love", 200, -30)
                $ Girl.Statup("Inbt", 200, 40)
                if Girl is RogueX:
                        if not Player.Male:
                            ch_r "Раз ты ни на что не способеа, я все сделаю сама!"
                        else:
                            ch_r "Раз ты ни на что не способен, я все сделаю сама!"
                elif Girl is KittyX:
                        if not Player.Male:
                            ch_k "Дура!"
                        else:
                            ch_k "Придурок!"
                        ch_k "Сейчас мы все уладим."
                elif Girl is EmmaX:
                        ch_e "Ладно!"
                        ch_e "Похоже, придется сделать все самой. . ."
                elif Girl is LauraX:
                        ch_l "Пфф!"
                elif Girl is JeanX:
                        $ JeanX.Eyes = "psychic"
                        $ Girl.Statup("Obed", 80, 10)
                        ch_j "Рррррррррр!"
                elif Girl is StormX:
                        $ StormX.Eyes = "white"
                        ch_s ". . ."
                        "Вы слышите, как на улице грохочет гром. . ."
                elif Girl is JubesX:
                        ch_v "Ох, отсоси!"
                        $ Girl.FaceChange("angry",Mouth="open")
                        call Punch
                        "Она раскрывает рот и бросается к вашему горлу, но в последнюю секунду останавливается."
                        $ Girl.FaceChange("angry", Eyes="side")
                        "Она встряхивается и подходит уже более спокойной."
                        $ Girl.FaceChange("angry")
                        "Видно, что она с трудом сдерживает себя."
                elif Girl is GwenX:
                        ch_g "Знаешь что?!"
                        ch_g "Мне надоело быть милой с тобой!"
                        ch_g "Пора натравить на тебя ИОСТП!"
                        "[[Имитационный Организм, Созданный Только для Прикосновений]"
                elif Girl is BetsyX:
                        if not Player.Male:
                            ch_b "Ииии ты перешла границы моего терпения."
                        else:
                            ch_b "Ииии ты перешел границы моего терпения."
                        ch_b "У меня не так много доступных вариантов, а значит. . ."
                elif Girl is DoreenX:
                        $ Girl.FaceChange("angry",2,Mouth="open")
                        ch_d "Что ж. . . Больше не будет мисс Милой Белочки!"
                elif Girl is WandaX:
                        ch_w "О, значит, вот как. . ."
                call Girl_Tag(Girl,1)
                $ Girl.Addictionrate += 2
                $ Girl.Resistance = 1 if Girl.Resistance < 1 else Girl.Resistance
                $ Girl.Event[1] = 10
                jump Addicted_Bad_End

        $ Girl.FaceChange("sad")
        if Girl is RogueX:
                if not Player.Male:
                    ch_r "Извини, [Girl.Petname], ты упустила все возможности. Я пошла."
                else:
                    ch_r "Извини, [Girl.Petname], ты упустил все возможности. Я пошла."
        elif Girl is KittyX:
                ch_k "Ну, тогда, наверное, мне пора идти. . ."
        elif Girl is EmmaX:
                ch_e "Что ж, боюсь, больше у нас нет времени возиться, мне пора идти."
        elif Girl is LauraX:
                ch_l "Ну Ладно, хорошо, мне уже пора идти. . ."
        elif Girl is JeanX:
                ch_j "Ну. . . хорошо. Как хочешь. Я пошла. . ."
        elif Girl is StormX:
                if not Player.Male:
                    ch_s ". . . Прекрасно. Ты выразилась предельно ясно."
                else:
                    ch_s ". . . Прекрасно. Ты выразился предельно ясно."
        elif Girl is JubesX:
                ch_v "Если ты собираешься лишь валять дурака, я пошла. . ."
        elif Girl is GwenX:
                ch_g "Это пустая трата времени. Я. . . придумаю что-нибудь другое."
        elif Girl is BetsyX:
                ch_b "У меня не так много времени, чтобы тратить его впустую. Я пошла."
        elif Girl is DoreenX:
                ch_d "Я. . . просто не могу. . ."
        elif Girl is WandaX:
                if not Player.Male:
                    ch_w "Ты чересчур настойчив. . ."
                else:
                    ch_w "Ты чересчур настойчив. . ."
        jump Addicted_Bad_End

label First_Addicted_End: #rkeljsvgbdw
        # This is the ending sequence if you successfully complete the addiciton innitiation
        $ Girl.DailyActions.append("fixed")
        $ Girl.Event[1] = 10
        $ Girl.FaceChange("surprised")
        if Girl is RogueX:
                ch_r "Вау. Теперь я чувствую себя намного лучше, гораздо более собранной. Думаю, я и правда зависима от твоих касаний."
        elif Girl is KittyX:
                ch_k "Вау. Это было здорово. Может, даже слишком здорово. . ."
        elif Girl is EmmaX:
                ch_e "Невероятно. Это и вправду развеяло пелену. . . Полагаю, в будущем это может стать проблемой."
        elif Girl is LauraX:
                ch_l "Ага. Сработало. Спасибо."
        elif Girl is JeanX:
                ch_j "Ого!"
                $ Girl.Statup("Love", 50, 3)
                $ Girl.Statup("Obed", 80, 2)
                ch_j "Похоже и вправду сработало. . ."
                ch_j "Как-нибудь вернусь за добавкой. . ."
        elif Girl is StormX:
                ch_s "Ох. . . благодарю."
                ch_s "Теперь я чувствую себя. . . намного лучше."
                ch_s "Да, просто превосходно."
        elif Girl is JubesX:
                ch_v "Хм. . . Я чувствую себя лучше."
                ch_v "И это все, что требовалось!"
                ch_v "Нууу, это точно проще чем пить кровь. . ."
        elif Girl is GwenX:
                ch_g "Воу."
                ch_g "Сработало, пелена рассеивается. . ."
                ch_g "Спасибо."
        elif Girl is BetsyX:
                ch_b "Боже. . ."
                ch_b "Я чувствую себя. . . по-хорошему -восхитительно!-"
        elif Girl is DoreenX:
                ch_d "Воу."
                ch_d "Это пре-кра-сно!"
                ch_d "Божечки."
        elif Girl is WandaX:
                ch_w "Ох. . ."
                ch_w "Вот оно. . ."
                ch_w "Да, так гораздо спокойнее. . ."

        if "swallowed" in Girl.RecentActions:
                $ Girl.FaceChange("bemused", 1)
                if Girl is RogueX:
                        ch_r "Хмм, похоже, что-то есть и в твоей. . . жидкости. Она была такой теплой. . ."
                elif Girl is KittyX:
                        $ Girl.Blush = 2
                        if not Player.Male:
                            ch_k "А ты, эм. . . на вкус также очень вкусная. . "
                        else:
                            ch_k "А ты, эм. . . на вкус также очень вкусный. . "
                elif Girl is EmmaX:
                        ch_e "Подозреваю, что-то также есть и в твоей. . . жидкости. . ."
                elif Girl is LauraX:
                        if not Player.Male:
                            ch_l "Ты и на вкус хороша. . ."
                        else:
                            ch_l "Ты и на вкус хорош. . ."
                elif Girl is JeanX:
                        ch_j "А знаешь. . ."
                        $ Girl.Statup("Love", 50, 3)
                        $ Girl.Statup("Obed", 80, 2)
                        if not Player.Male:
                            ch_j "Думаю, твои соки тоже могут быть волшебными или типа того."
                        else:
                            ch_j "Думаю, твоя сперма тоже может быть волшебной или что-то вроде того."
                elif Girl is StormX:
                        if not Player.Male:
                            ch_s "Должна признать, я не ожидала, что твои. . . соки возымеют такой эффект."
                        else:
                            ch_s "Должна признать, я не ожидала, что твоя. . . сперма возымеет такой эффект."
                elif Girl is JubesX:
                        ch_v "Не скажу, что, эм. . . это было плохо. . ."
                elif Girl is GwenX:
                        if not Player.Male:
                            ch_g "Твои, эм. . . ты и на вкус хороша. . ."
                        else:
                            ch_g "Твоя, эм. . . ты и на вкус хорош. . ."
                elif Girl is BetsyX:
                        ch_b "Ох, я заметила, что твоя. . . эссенция была довольно ароматной."
                elif Girl is DoreenX:
                        if not Player.Male:
                            ch_d "Эм. . . твои. . . соки тоже помогают. . ."
                        else:
                            ch_d "Эм. . . твоя. . . сперма тоже помогает. . ."
                elif Girl is WandaX:
                        if not Player.Male:
                            ch_w "Похоже, что твои соки, каким-то образом, тоже помогают. . ."
                        else:
                            ch_w "Похоже, что твоя сперма, каким-то образом, тоже помогает. . ."
        $ Girl.FaceChange("normal", 0)
        $ Girl.Mouth = "sad"
        call Sex_Over
        if Girl not in Digits:
                if Girl is RogueX:
                        ch_r "Думаю, мне нужно будет как-нибудь созвониться с тобой, тебе, наверное, стоит знать мой номер. Держи."
                elif Girl is KittyX:
                        ch_k "Позвони мне[Girl.like]как-нибудь, вот мой номер."
                elif Girl is EmmaX:
                        ch_e "Нам нужно будет как-нибудь созвониться, запиши мой номер. . ."
                elif Girl is LauraX:
                        ch_l "Мне, наверное, нужно будет с тобой связаться, вот мой номер."
                elif Girl is JeanX:
                        ch_j "Наверное, нам стоит обменяться номерами."
                        ch_j ". . . так, на всякий случай."
                elif Girl is StormX:
                        ch_s "Полагаю, я должна дать тебе свой номер телефона. . ."
                elif Girl is JubesX:
                        ch_v "Наверное, мне следует дать тебе свой номер. . ."
                elif Girl is GwenX:
                        ch_g "Вот мой номер, позвони мне как-нибудь. . ."
                elif Girl is BetsyX:
                        if not Player.Male:
                            ch_b "Мне нужно, чтобы ты была на связи, вот мой номер. . ."
                        else:
                            ch_b "Мне нужно, чтобы ты был на связи, вот мой номер. . ."
                elif Girl is DoreenX:
                        ch_d "Эм, думаю, нам нужно поддерживать связь. . ."
                elif Girl is WandaX:
                        ch_w "Я хочу как-нибудь с тобой созвониться. . ."
                $ Digits.append(Girl)
        if Girl is RogueX:
                ch_r "Возможно, когда-нибудь мне понадобится добавка.  . . Увидимся."
        elif Girl is KittyX:
                ch_k "Мы должны. . . эм, как-нибудь повторить."
        elif Girl is EmmaX:
                ch_e "Мы должны. . . как-нибудь встретиться снова."
        elif Girl is LauraX:
                ch_l "Мы должны встретиться снова, увидимся."
        elif Girl is JeanX:
                ch_j "Мы должны. . . снова \"поболтать\". . ."
        elif Girl is StormX:
                ch_s "Пожалуй, нам придется время от времени встречаться. . ."
        elif Girl is JubesX:
                ch_v "Мне, возможно, эм. . . нужно будет повторить."
        elif Girl is GwenX:
                ch_g "Я, эм. . . увидимся снова, если я буду чувствовать себя не в своей тарелке. . ."
        elif Girl is BetsyX:
                ch_b "Мы. . . должны как-нибудь повторить, спасибо."
        elif Girl is DoreenX:
                ch_d "Возможно, нам придется повторить. . ."
        elif Girl is WandaX:
                ch_w "Я бы очень хотела повторить. . ."
        $ Girl.Resistance = 1

label Addicted_Bad_End: #rkeljsvgbdw
        #if an Ultimatum fails. . .
        #also falls through from good ending. . .
        $ Girl.Event[3] = 5
        $ Girl.RecentActions.append("addiction")
        $ Girl.DailyActions.append("addiction")
        $ Girl.DrainWord("ultimatum",0) #removes recent
        $ Tempmod = 0
        $ Line = 0
        $ Situation = 0
        $ Girl.Forced = 0
        $ MultiAction = 1
        $ Girl.Addictionrate += 2
        call Sex_Over
        call Checkout
        $ Girl.ArmPose = 1
        if Girl not in Party: #allows you to stay if she's added to a party
                if bg_current == Girl.Home:
                        "Вы возвращаетесь в свою комнату."
                        $ bg_current = "bg player"
                elif bg_current == "bg player" and Girl.Loc == bg_current:
                        "[Girl.Name] выходит."
                call Remove_Girl(Girl)
        $ renpy.pop_call()
        jump Misplaced

# end Event First_Addicted2 /////////////////////////////////////////////////////

label Addicted_Fix_Beg: #rkeljsvgbdw
        #jumped to if you refuse her anything during the later phase
        $ Girl.FaceChange("angry")
        $ Girl.Forced = 0
        if "beg" in Girl.RecentActions:
            $ Girl.Statup("Love", 200, -10)
        $ Girl.Statup("Obed", 50, 2)
        $ Girl.Statup("Obed", 90, 1)
        if Girl.Petname in (Terms["master"], Terms["sir"], "господин", "госпожа", "хозяин", "хозяйка"):
                #if she is obedient
                $ Girl.FaceChange("sad")
                if Girl.Addict <= 80 or "beg" in Girl.RecentActions:
                        if Girl is RogueX:
                                ch_r "Если ты настаиваешь, [Girl.Petname]."
                        elif Girl is KittyX:
                                ch_k "Ладно-ладно. . . [Girl.Petname]"
                        elif Girl is EmmaX:
                                ch_e "Полагаю, мне придется это сделать, [Girl.Petname]."
                        elif Girl is LauraX:
                                ch_l "Ладно, [Girl.Petname]."
                        elif Girl is JeanX:
                                ch_j ". . ."
                                ch_j "Ладно. . ."
                        elif Girl is StormX:
                                ch_s "Пусть будет так."
                        elif Girl is JubesX:
                                ch_v "Ладно. . ."
                        elif Girl is GwenX:
                                ch_g "Ну. . .ладно. . ."
                        elif Girl is BetsyX:
                                ch_b "Если. . . нужно. . ."
                        elif Girl is DoreenX:
                                ch_d "Ладно. . . я справлюсь. . ."
                        elif Girl is WandaX:
                                ch_w "Хорошо, я постараюсь справиться. . ."
                        "[Girl.Name] грустно пожимает плечами, а затем выходит из комнаты."
                        jump Addicted_Bad_End
                else:
                        $ Girl.Eyes = "manic"
                        "[Girl.Name] начинает слегка дрожать."
                        if Girl is RogueX:
                                ch_r "Пожалуйста, [Girl.Petname], пожалуйста, может все-таки передумаешь?"
                        elif Girl is KittyX:
                                ch_k "Пожалуйста, [Girl.Petname], я схожу с ума. . ."
                        elif Girl is EmmaX:
                                ch_e ". . ."
                                ch_e "Пожалуйста, [Girl.Petname]?"
                        elif Girl is LauraX:
                                ch_l "Ну давай, [Girl.Petname]?"
                        elif Girl is JeanX:
                                ch_j ". . ."
                                $ Girl.Statup("Obed", 50, 4)
                                ch_j ". . .Пожалуйста?"
                        elif Girl is StormX:
                                ch_s ". . ."
                        elif Girl is JubesX:
                                ch_v "Пожалуйста!"
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Не могла бы ты  -пожалуйста- сделать исключение? . ."
                                else:
                                    ch_g "Не мог бы ты  -пожалуйста- сделать исключение? . ."
                        elif Girl is BetsyX:
                                ch_b "Неужели ты не можешь войти в мое положение?"
                        elif Girl is DoreenX:
                                ch_d "Ну пожалуйста. . ."
                        elif Girl is WandaX:
                                ch_w "Да ладно тебе, помоги мне. . ."
                        $ Girl.RecentActions.append("beg")
        elif Girl.Addict <= 85:
                if Girl is RogueX:
                        ch_r "Ну и ладно!"
                elif Girl is KittyX:
                        if not Player.Male:
                            ch_k "Дура!"
                        else:
                            ch_k "Придурок!"
                elif Girl is EmmaX:
                        ch_e "Ну и ладно!"
                elif Girl is LauraX:
                        ch_l "Пфф!"
                elif Girl is JeanX:
                        $ JeanX.Eyes = "psychic"
                        ch_j "Да пошло все нахуй!"
                        $ JeanX.Eyes = "normal"
                elif Girl is StormX:
                        ch_s ". . ."
                elif Girl is JubesX:
                        if not Player.Male:
                            ch_v "Стерва!"
                        else:
                            ch_v "Говнюк!"
                elif Girl is GwenX:
                        ch_g "Черт!"
                elif Girl is BetsyX:
                        if not Player.Male:
                            ch_b "Пиздень!"
                        else:
                            ch_b "Педик!"
                elif Girl is DoreenX:
                        ch_d "ЛАДНО!"
                elif Girl is WandaX:
                        ch_w "Ладно. . . пока я от тебя отстану. . ."
                "[Girl.Name], кипя от ярости, выходит."
                jump Addicted_Bad_End
        else:
                #if you're well over the limits
                $ Girl.FaceChange("angry")
                "[Girl.Name] прямо кипит от ярости."
                $ Girl.Statup("Love", 200, -10)
                $ Girl.Statup("Obed", 90, -5)
                if Girl is RogueX:
                        ch_r "Ты. . ."
                        ch_r "Я не могу принять ответ \"нет\"."
                elif Girl is KittyX:
                        ch_k "!!!"
                        ch_k "Я больше не могу!"
                elif Girl is EmmaX:
                        ch_e ". . ."
                        ch_e "Хорошо."
                        ch_e "Похоже, придется сделать все самой. . ."
                elif Girl is LauraX:
                        ch_l "Грррррр. . ."
                elif Girl is JeanX:
                        $ JeanX.Eyes = "psychic"
                        ch_j "Рррррррррр!"
                elif Girl is StormX:
                        ch_s ". . ."
                elif Girl is JubesX:
                        ch_v "Ох, отсоси!"
                        $ Girl.FaceChange("angry",Mouth="open")
                        call Punch
                        "Она раскрывает рот и бросается к вашему горлу, но в последнюю секунду останавливается."
                        $ Girl.FaceChange("angry", Eyes="side")
                        "Она встряхивается и подходит уже более спокойной."
                        $ Girl.FaceChange("angry")
                        "Видно, что она с трудом сдерживает себя."
                elif Girl is GwenX:
                        ch_g "Так. . . а знаешь что?!"
                        ch_g "Мне надоело быть милой с тобой!"
                        ch_g "Пора натравить на тебя ИОСТП!"
                        "[[Имитационный Организм, Созданный Только для Прикосновений]"
                elif Girl is BetsyX:
                        if not Player.Male:
                            ch_b "Ииии ты перешла границы моего терпения."
                        else:
                            ch_b "Ииии ты перешел границы моего терпения."
                        ch_b "У меня нет выбора. . ."
                elif Girl is DoreenX:
                        $ Girl.FaceChange("angry",2,Mouth="open")
                        ch_d "Что ж. . .  больше не будет мисс Милой Белочки!"
                elif Girl is WandaX:
                        ch_w "О, значит, вот как. . ."
                call Girl_Tag(Girl,1)
                $ Girl.Statup("Inbt", 50, 10)
                $ Girl.Statup("Inbt", 90, 5)
                $ Girl.Addictionrate += 2
                if Girl.Addict <= 40:
                        jump Addicted_Fix_End
                else:
                        "[Girl.Name], кипя от ярости, выходит."
                        jump Addicted_Bad_End
        return

# Event Addiction_Fix /////////////////////////////////////////////////////
label Addiction_Fix(Girl=0): #rkeljsvgbdw
        $ Girl.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ Girl = GirlCheck(Girl)
        call Set_The_Scene
        call Shift_Focus(Girl)
        if "locked" in Player.Traits:
                $ Girl.Loc = bg_current
                $ Girl.OutfitChange(Changed=1)
                call Locked_Door(Girl)
                if not _return:
                        #if the door is locked and you refused entry. . .
                        return

        $ Addict_Queue = 0

        if "switchcheck" in Girl.Traits:
                #if you recently switched sexes. . .
                if Girl.Loc == bg_current or Girl in Party:
                        "Вдруг [Girl.Name] оглядывается и замечает вас,"
                else:
                        "Вдруг [Girl.Name] появляется словно из ниоткуда и замечает вас,"
                $ Girl.Loc = bg_current
                $ Girl.OutfitChange(Changed=1)
                call Set_The_Scene
                $ Girl.FaceChange("confused")
                call expression Girl.Tag + "_Switch" #call Rogue_Switch
                call AnyLine(Girl,". . . но не об этом я хотела поговорить.")
        elif bg_current != "bg player" and bg_current != Girl.Home:
                if Girl.Loc == bg_current or Girl in Party:
                        "[Girl.Name] изъявляет желание поговорить с вами в вашей комнате, а затем отводит вас туда."
                else:
                        "[Girl.Name] появляется словно из ниоткуда и изъявляет желание поговорить с вами в вашей комнате, а затем отводит вас туда."
        else:
                if Girl.Loc == bg_current or Girl in Party:
                        "[Girl.Name] поворачивается к вам с голодным взглядом."
                else:
                        "[Girl.Name] заскакивает в вашу комнату с легким беспокойством."

        $ Girl.Loc = bg_current
        $ Girl.OutfitChange(Changed=1)
        call Shift_Focus(Girl)
        call Set_The_Scene
        call CleartheRoom(Girl)
        $ Girl.FaceChange("manic")
        $ Taboo = 0
        $ Girl.Taboo = 0
        $ Player.AddWord(1,"interruption") #prevents interruption

        if Girl.Event[1] < 11:
                if Girl is RogueX:
                        ch_r "Так вот, мы выяснили, что вызывает этот гул в моей голове."
                        ch_r "С тех пор, как я приходила к тебе в последний раз, с ним стало легче справляться, он появляется реже, а уходит быстрее."
                        ch_r "Я уже почти могу с ним совладать, но еще не до конца, понимаешь?"
                elif Girl is KittyX:
                        ch_k "Так вот, я поняла, что происходит со мной."
                        ch_k "С тобой."
                        ch_k "С этим гулом в моей голове. . ."
                        ch_k "Думаю, сейчас мне немного легче? Похоже, он теперь быстрее проходит?"
                        ch_k "Но все равно, мне бы не помешала небольшая помощь. . ."
                elif Girl is EmmaX:
                        if not Player.Male:
                            ch_e "Ты, полагаю, будешь рада узнать, что я считаю, что разобралась с нашей. . . трагедией."
                        else:
                            ch_e "Ты, полагаю, будешь рад узнать, что я считаю, что разобралась с нашей. . . трагедией."
                        ch_e "С этой \"гудящей\" проблемой."
                        ch_e "Теперь недомогание перешло в тупую боль, во что-то, с чем я в состояние справиться."
                        ch_e "Но это не значит, что я готова всегда справляться с этим в одиночку. . ."
                elif Girl is LauraX:
                        ch_l "Слушай, кажется, я разобралась с этим гудением в моей голове."
                        ch_l "Думаю, теперь оно не такое сильное, сейчас я могу с ним справляться."
                        ch_l "Но все-таки мне нравится, когда нет и намека на него. . ."
                elif Girl is JeanX:
                        ch_j ". . ."
                        ch_j "Слушай, [Girl.Petname]. . ."
                        ch_j "Помнишь, когда я прикасалась к тебе, мне становилось легче?"
                        ch_j "Так вот. . . я хочу почувствовать себя еще лучше. . ."
                elif Girl is StormX:
                        ch_s "На днях, кажется, я кое - что поняла."
                        ch_s "Я всю свою жизнь связана со стихиями. . ."
                        ch_s "Я всегда чувствую связь с ними."
                        ch_s "Однако, когда мы соприкасаемся друг с другом, я теряю ее."
                        ch_s "Это больно."
                        ch_s ". . ."
                        ch_s "Но в глубине души мне это нравится. . ."
                elif Girl is JubesX:
                        ch_v "Сработало!"
                        ch_v "Я гуляла весь день!"
                        ch_v ". . ."
                        ch_v ". . . но. . ."
                        ch_v "Но эффект почти прошел."
                        ch_v "Похоже, он длится совсем немного. . ."
                elif Girl is GwenX:
                        ch_g "Ладно, думаю, все подтвердилось."
                        ch_g "Вся эта ситуация связана с физическим контактом."
                        ch_g "Я чувствую себя не в своей тарелке, если не прикосаюсь к тебе."
                elif Girl is BetsyX:
                        ch_b "С тех пор как мы в последний раз разговаривали об этом, я заметила, что \"желания\" начинают возвращаться."
                        ch_b "Ты ведь помнишь, мы выяснили, что прикосновений к тебе достаточно, чтобы избавиться от этого состояния, верно?"
                        ch_b "Из-за этого я и пришла. . . пришла попросить повторить."
                elif Girl is DoreenX:
                        ch_d "Ладно, ранее мы разобрались с моей \"проблемой\". . ."
                        ch_d "Но она, вроде как, вернулась, так что. . ."
                        ch_d "Есть шанс, что мы сможем повторить?"
                elif Girl is WandaX:
                        ch_w "Слушай, [Girl.Petname]. . ."
                        ch_w "Значит так, у меня был трудный день. . . Может, поможешь девушке?"
                        if not Player.Male:
                            ch_w "Не могла бы ты, ну. . . знаешь, слегка прикоснуться ко мне?"
                        else:
                            ch_w "Не мог бы ты, ну. . . знаешь, слегка прикоснуться ко мне?"
                menu:
                    extend ""
                    "И по-прежнему нет нет другой альтернативы, кроме как прикасаться ко мне?":
                            $ Girl.Statup("Love", 80, 1)
                            $ Girl.Statup("Obed", 50, 1)
                            if Girl is RogueX:
                                    ch_r "Никакой! МакКой перепробовал все, что только мог."
                            elif Girl is KittyX:
                                    ch_k "Никакой!"
                            elif Girl is EmmaX:
                                    ch_e "К сожалению нет. Хэнк перепробовал все."
                            elif Girl is LauraX:
                                    ch_l "Не похоже, что есть."
                            elif Girl is JeanX:
                                    ch_j "Да, я бы хотела этого, но ее нет."
                            elif Girl is StormX:
                                    ch_s "Ничто другое не сможет дать мне такие. . . ощущения."
                            elif Girl is JubesX:
                                    ch_v "Неа, больше ничего не работает."
                            elif Girl is GwenX:
                                    ch_g "Нет. Если подумать, довольно удобно для тебя. . ."
                            elif Girl is BetsyX:
                                    ch_b "К большому сожалению, никаких."
                            elif Girl is DoreenX:
                                    if not Player.Male:
                                        ch_d "Ты сама знаешь."
                                    else:
                                        ch_d "Ты сам знаешь."
                            elif Girl is WandaX:
                                    ch_w "Насколько я могу судить, нет. . ."
                    "Что ж, я могу помочь. . .":
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Obed", 50, 1)
                            if Girl is RogueX:
                                    ch_r "И я это ценю, [Girl.Petname]."
                            elif Girl is KittyX:
                                    ch_k "Ах, спасибо, [Girl.Petname]."
                            elif Girl is EmmaX:
                                    ch_e "Я очень признателельна тебе, [Girl.Petname]."
                            elif Girl is LauraX:
                                    ch_l "Да, спасибо, [Girl.Petname]."
                            elif Girl is JeanX:
                                    $ Girl.Statup("Love", 50, 3)
                                    $ Girl.Statup("Obed", 50, 3)
                                    ch_j "Отлично, итак. . ."
                            elif Girl is StormX:
                                    ch_s "Я бы не хотела обременять тебя. . ."
                                    if not Player.Male:
                                        ch_s "Уверена, я смогу сделать так, чтобы ты об этом не пожалела. . ."
                                    else:
                                        ch_s "Уверена, я смогу сделать так, чтобы ты об этом не пожалел. . ."
                            elif Girl is JubesX:
                                    ch_v "Я была бы очень признательна тебе."
                            elif Girl is GwenX:
                                    ch_g "Как благородно с твоей стороны. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я очень это ценю."
                            elif Girl is DoreenX:
                                    ch_d "Огромное спасибо."
                            elif Girl is WandaX:
                                    ch_w "Большое спасибо. . ."
                    "Ты всегда можешь стать развратнее и тогда я без проблем тебе помогу.":
                            $ Girl.FaceChange("angry",2)
                            $ Girl.Statup("Love", 50, -1, 1)
                            $ Girl.Statup("Love", 80, -3, 1)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 90, 1)
                            if Girl is RogueX:
                                    if not Player.Male:
                                        ch_r "Да, я знаю, спасибо, что напомнила."
                                    else:
                                        ch_r "Да, я знаю, спасибо, что напомнил."
                            elif Girl is KittyX:
                                    if not Player.Male:
                                        ch_k "Да, спасибо, что напомнила."
                                    else:
                                        ch_k "Да, спасибо, что напомнил."
                            elif Girl is EmmaX:
                                    ch_e ". . ."
                            elif Girl is LauraX:
                                    ch_l "Это совсем не клево."
                            elif Girl is JeanX:
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Obed", 50, 1)
                                    ch_j "Да, но, знаешь, я бы хотела избежать этого."
                            elif Girl is StormX:
                                    $ Girl.Statup("Love", 80, -5, 1)
                                    $ Girl.Statup("Obed", 50, 2)
                                    ch_s "Никогда."
                                    $ Girl.Addictionrate -= 2
                                    jump Addicted_Bad_End
                            elif Girl is JubesX:
                                    ch_v "Или я могла бы просто перегрызть тебе глотку. . ."
                                    ch_v "Ладно, расслабься."
                            elif Girl is GwenX:
                                    ch_g "Я \"наемник,\" а не \"шлюха,\""
                                    ch_g "-имей это в виду."
                            elif Girl is BetsyX:
                                    $ Girl.Statup("Love", 80, -1)
                                    $ Girl.Statup("Inbt", 60, 2)
                                    ch_b "Да -никогда!-"
                            elif Girl is DoreenX:
                                    ch_d "Что?! Я никогда. . . эм. . ."
                                    if Girl.SEXP > 20:
                                            ch_d "Ну, может когда-нибудь!"
                                    else:
                                            ch_d "Никогда на это не пойду!"
                            elif Girl is WandaX:
                                    ch_w "Меня это не интересует. . ."
        else:
                    if Girl.Petname in (Terms["master"], Terms["sir"], "господин", "госпожа", "хозяин", "хозяйка"):
                            $ Girl.FaceChange("bemused")
                            if Girl is RogueX:
                                    ch_r "Мне нужна еще одна доза тебя, [Girl.Petname]. Что мне нужно сделать?"
                            elif Girl is KittyX:
                                    if not Player.Male:
                                        ch_k "Мне бы не помешала еще одна доза тебя, [Girl.Petname]. Не могла бы ты мне помочь?"
                                    else:
                                        ch_k "Мне бы не помешала еще одна доза тебя, [Girl.Petname]. Не мог бы ты мне помочь?"
                            elif Girl is EmmaX:
                                    if not Player.Male:
                                        ch_e "Мне бы не помешала доза тебя, [Girl.Petname]. Не могла бы ты мне помочь?"
                                    else:
                                        ch_e "Мне бы не помешала доза тебя, [Girl.Petname]. Не мог бы ты мне помочь?"
                            elif Girl is LauraX:
                                    ch_l "Дай мне еще одну дозу тебя, [Girl.Petname]. . . Пожалуйста?"
                            elif Girl is JeanX:
                                    ch_j "Итак, могу ли я получить еще одну дозу тебя, [Girl.Petname]? . ."
                            elif Girl is StormX:
                                    if not Player.Male:
                                        ch_s "Не могла бы ты снова прикоснуться ко мне, [Girl.Petname]?"
                                    else:
                                        ch_s "Не мог бы ты снова прикоснуться ко мне, [Girl.Petname]?"
                            elif Girl is JubesX:
                                    if not Player.Male:
                                        ch_v "Не могла бы ты позволить мне снова прикоснуться к тебе, [Girl.Petname]?"
                                    else:
                                        ch_v "Не мог бы ты позволить мне снова прикоснуться к тебе, [Girl.Petname]?"
                            elif Girl is GwenX:
                                    ch_g "Мне просто нужно еще одно быстрое прикосновение. . . [Girl.Petname]"
                            elif Girl is BetsyX:
                                    ch_b "Мне нужно поправить свое состояние, [Girl.Petname]."
                            elif Girl is DoreenX:
                                    ch_d "Помоги мне избавиться от этого состояния, [Girl.Petname]."
                            elif Girl is WandaX:
                                    ch_w "Помоги мне, [Girl.Petname]. . ."
                    else:
                            if Girl is RogueX:
                                    ch_r "Думаю, что мне нужна еще одна доза тебя, я чувствую себя немного некомфортно."
                            elif Girl is KittyX:
                                    ch_k "Можно мне еще одну дозу тебя?"
                            elif Girl is EmmaX:
                                    ch_e "[Girl.Petname]. . . Мне бы не помешала еще одна доза тебя. . . конечно, если у тебя есть время."
                            elif Girl is LauraX:
                                    ch_l "Можно мне еще одну дозу тебя?"
                            elif Girl is JeanX:
                                    ch_j "Поможешь мне?"
                            elif Girl is StormX:
                                    if not Player.Male:
                                        ch_s "Не могла бы ты снова прикоснуться ко мне?"
                                    else:
                                        ch_s "Не мог бы ты снова прикоснуться ко мне?"
                            elif Girl is JubesX:
                                    ch_v "Могу я получить еще одну дозу?"
                            elif Girl is GwenX:
                                    ch_g "Смотри, мне просто нужно еще одно быстрое прикосновение. . ."
                            elif Girl is BetsyX:
                                    ch_b "Мне нужно поправить свое состояние."
                            elif Girl is DoreenX:
                                    ch_d "Помоги мне избавиться от этого состояния, [Girl.Petname]."
                            elif Girl is WandaX:
                                    ch_w "Помоги мне, [Girl.Petname]. . ."
        $ Girl.Blush = 1
        $ Count2 = 2
        $ Tempmod = 0
        call Addicted_Ultimatum
        jump Addicted_Fix_End

label Addicted_Fix_End: #rkeljsvgbdw
        $ Girl.FaceChange("normal", 0)
        $ Girl.Mouth = "sad"
        if Girl is RogueX:
                if Girl.Event[1] < 11:
                    #if it's the first "fix"
                    if "forced tag" in Girl.RecentActions:
                            if not Player.Male:
                                ch_r "Я получила то, что мне было нужно. Если честно, я бы не хотела, чтобы ты принуждала меня, но, похоже, у меня не было иного выбора."
                                ch_r "Только. . . может, постараешься в будущем не быть таким дурой?"
                            else:
                                ch_r "Я получила то, что мне было нужно. Если честно, я бы не хотела, чтобы ты принуждал меня, но, похоже, у меня не было иного выбора."
                                ch_r "Только. . . может, постараешься в будущем не быть таким придурком?"
                    elif not Girl.Forced:
                            ch_r "Спасибо. Я очень ценю это. Я не могу это объяснить, но если я не получаю. . . "
                            ch_r "доступ к тебе время от времени, я чувствую себя совсем разбитой. Быть с тобой помогает мне прийти в норму."
                            if ApprovalCheck(Girl, 750):
                                ch_r "И, знаешь, это очень весело."
                            else:
                                if not Player.Male:
                                    ch_r "И спасибо, что не воспользовалась ситуацией для своей личной выгоды."
                                else:
                                    ch_r "И спасибо, что не воспользовался ситуацией для своей личной выгоды."
                    else:
                            if not Player.Male:
                                ch_r "Что ж, надеюсь, ты получила от этого то, что хотела. Если честно, я бы не хотела, чтобы ты принуждала меня, но, похоже, у меня не было иного выбора."
                                ch_r "Только. . . может, постараешься в будущем не быть таким дурой?"
                            else:
                                ch_r "Что ж, надеюсь, ты получил от этого то, что хотел. Если честно, я бы не хотела, чтобы ты принуждал меня, но, похоже, у меня не было иного выбора."
                                ch_r "Только. . . может, постараешься в будущем не быть таким придурком?"
                else:
                    if "forced tag" in Girl.RecentActions:
                            ch_r "Что ж, я получила то, что мне было нужно. Думаю, мы еще увидимся."
                    elif not Girl.Forced:
                            ch_r "Мммм, это было очень приятно, [Girl.Petname]."
                            ch_r "Я с нетерпением жду наших следующих . . . \"сеансов\"."
                    else:
                            ch_r "Что ж, похоже, мы оба получили то, что хотели. Думаю, мы еще увидимся."
        elif Girl is KittyX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions:
                            ch_k "Ладно, думаю, этого хватит. . ."
                            if not Player.Male:
                                ch_k "Не могла бы ты больше не принуждать меня?"
                            else:
                                ch_k "Не мог бы ты больше не принуждать меня?"
                    elif not Girl.Forced:
                            if not Player.Male:
                                ch_k "Спасибо, что помогла мне. Это и правда ужасные ощущения."
                            else:
                                ch_k "Спасибо, что помог мне. Это и правда ужасные ощущения."
                            if ApprovalCheck(Girl, 850):
                                ch_k "И в процессе мы неплохо проводим время. . ."
                            else:
                                if not Player.Male:
                                    ch_k "И спасибо, что[Girl.like]не воспользовался ситуацией."
                                else:
                                    ch_k "И спасибо, что[Girl.like]не воспользовалась ситуацией."
                    else:
                            if not Player.Male:
                                ch_k "Ну, похоже, тебе было весело. . ."
                                ch_k "Не могла бы ты. . . больше не быть такой стервой. . ."
                                ch_k "Пожалуйста?"
                            else:
                                ch_k "Ну, похоже, тебе было весело. . ."
                                ch_k "Не мог бы ты. . . больше не быть таким козлом. . ."
                                ch_k "Пожалуйста?"
                else:
                    if "forced tag" in Girl.RecentActions:
                            ch_k "Ладно, хватит. . . думаю, еще увидимся."
                    elif not Girl.Forced:
                            ch_k "Ммммм, это было так здооорово, [Girl.Petname]."
                            ch_k "Надеюсь, очень скоро увидимся снова. . ."
                    else:
                            if not Player.Male:
                                ch_k "Ну, ты, похоже, неплохо повеселилась. . . увидимся."
                            else:
                                ch_k "Ну, ты, похоже, неплохо повеселился. . . увидимся."
        elif Girl is EmmaX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions:
                            ch_e "Хорошо. . . Полагаю, это меня устроит."
                            if not Player.Male:
                                ch_e "Знаешь, ты могла бы вести себя попроще. . ."
                            else:
                                ch_e "Знаешь, ты мог бы вести себя попроще. . ."
                    elif not Girl.Forced:
                            ch_e "Я ценю твою. . . помощь."
                            ch_e "Мне было действительно очень неприятно, но хотя, я полагаю, могло быть и хуже."
                            if ApprovalCheck(Girl, 800):
                                ch_e "Да и мне нравится твоя компания. . ."
                            else:
                                ch_e "Я ценю твое. . . самообладание."
                    else:
                            if not Player.Male:
                                ch_e "Что ж. . . похоже, ты получила свое. . ."
                                ch_e "Знаешь, ты могла бы вести себя попроще. . ."
                            else:
                                ch_e "Что ж. . . похоже, ты получил свое. . ."
                                ch_e "Знаешь, ты мог бы вести себя попроще. . ."
                else:
                    if "forced tag" in Girl.RecentActions:
                            ch_e "Хорошо. . . Полагаю, это меня устроит. . . по крайней мере пока."
                    elif not Girl.Forced:
                            ch_e "Мммм, это было довольно приятно, [Girl.Petname]."
                            ch_e "Полагаю, я буду с нетерпением ждать нашей следующей встречи."
                    else:
                            if not Player.Male:
                                ch_e "Что ж. . . похоже, ты получил свое. . ."
                                ch_e "По крайней мере, пока. . ."
                            else:
                                ch_e "Что ж. . . похоже, ты получила свое. . ."
                                ch_e "По крайней мере, пока. . ."
        elif Girl is LauraX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions:
                            ch_l "Ладно, думаю, этого хватит."
                            if not Player.Male:
                                ch_l "На будующее, не будь такой сукой."
                            else:
                                ch_l "На будующее, не будь таким мудаком."
                    elif not Girl.Forced:
                            ch_l "Мммм, так хорошо. . ."
                            if not Player.Male:
                                ch_l "Спасибо, что помогла мне с этим разобраться, [Girl.Petname]."
                            else:
                                ch_l "Спасибо, что помог мне с этим разобраться, [Girl.Petname]."
                            if ApprovalCheck(Girl, 750):
                                ch_l "И, похоже, это неплохой способ провести время, верно?"
                            else:
                                if not Player.Male:
                                    ch_l "И спасибо, что не давила на меня."
                                else:
                                    ch_l "И спасибо, что не давил на меня."
                    else:
                            $ Girl.Statup("Love", 90, -5)
                            if not Player.Male:
                                ch_l "Ладно, думаю, ты получила то, что хотела."
                                ch_l "На будующее, не будь такой сукой."
                            else:
                                ch_l "Ладно, думаю, ты получил то, что хотел."
                                ch_l "На будующее, не будь таким мудаком."
                else:
                    if "forced tag" in Girl.RecentActions:
                            ch_l "Ладно, наверное, хватит. Увидимся позже."
                    elif not Girl.Forced:
                            ch_l "Мы хорошо провели время, [Girl.Petname]."
                            ch_l "Увидимся."
                    else:
                            $ Girl.Statup("Love", 90, -5)
                            if not Player.Male:
                                ch_l "Ладно, думаю, ты получила то, что хотела. Думаю, еще увидимся."
                            else:
                                ch_l "Ладно, думаю, ты получил то, что хотел. Думаю, еще увидимся."
        elif Girl is JeanX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions:
                            ch_j "Хорошо, вот и все. . ."

                    elif not Girl.Forced:
                            $ Girl.Statup("Love", 80, 3)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 80, 2)
                            ch_j "Хорошо, вот и все. . ."
                            ch_j "Спасибо, [Girl.Petname]."
                            if ApprovalCheck(Girl, 750):
                                ch_j "А тебе ведь понравилось, да?"
                            else:
                                if not Player.Male:
                                    ch_j "а ты не была \"совсем уж озобоченной\"."
                                else:
                                    ch_j "а ты не был \"совсем уж озобоченным\"."
                    else:
                            $ Girl.Statup("Love", 90, -5)
                            $ Girl.Statup("Obed", 80, 2)
                            ch_j "Ну. . ."
                            ch_j "Это случилось. . ."
                            ch_j "Хотя, думаю оно того стоило. . ."
                else:
                    if "forced tag" in Girl.RecentActions:
                            ch_j "Ладно, наверное, хватит. Увидимся позже."
                    elif not Girl.Forced:
                            ch_j "Ладно, спасибо, [Girl.Petname]."
                            ch_j "Увидимся."
                    else:
                            $ Girl.Statup("Love", 90, -5)
                            $ Girl.Statup("Obed", 90, 2)
                            ch_j "Ладно, думаю, на этом и закончим. . ."
        elif Girl is StormX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions:
                            $ Girl.Statup("Love", 80, 5)
                            $ Girl.Statup("Obed", 50, 5)
                            ch_s ". . . Мне жаль."
                            if not Player.Male:
                                ch_s "Что ты не оставила мне иного выбора. . ."
                            else:
                                ch_s "Что ты не оставил мне иного выбора. . ."
                    elif not Girl.Forced:
                            if not Player.Male:
                                ch_s "Спасибо, что. . . доставила мне удовольствие."
                                ch_s "Я нахожу эти желания. . . неприемлемыми. . ."
                            else:
                                ch_s "Спасибо, что. . . доставил мне удовольствие."
                                ch_s "Я нахожу эти желания. . . неприемлемыми. . ."
                            if ApprovalCheck(Girl, 800):
                                ch_s ". . . но все могло быть гораздо хуже. . ."
                            else:
                                ch_s "Я очень ценю, что ты ограничиваешь себя."
                    else:
                            if not Player.Male:
                                ch_s "Что ж. . . Надеюсь, ты тоже удовлетворен. . ."
                                ch_s "Нам не нужно так враждебно относиться друг к другу. . ."
                            else:
                                ch_s "Что ж. . . Надеюсь, ты тоже удовлетворена. . ."
                                ch_s "Нам не нужно так враждебно относиться друг к другу. . ."
                else:
                    if "forced tag" in Girl.RecentActions:
                            $ Girl.Statup("Love", 80, 1)
                            $ Girl.Statup("Obed", 50, 1)
                            ch_s ". . . Мне жаль. . ."
                    elif not Girl.Forced:
                            ch_s ". . . Мне очень понравилось, [Girl.Petname]."
                            ch_s "Увидимся позже. . ."
                    else:
                            if not Player.Male:
                                ch_s "Что ж. . . Надеюсь, ты тоже удовлетворен. . ."
                                ch_s "Также, как и я сейчас. . ."
                            else:
                                ch_s "Что ж. . . Надеюсь, ты тоже удовлетворена. . ."
                                ch_s "Также, как и я сейчас. . ."
        elif Girl is JubesX:
                if Girl.Event[1] < 11:
                    #if it's the first "fix"
                    if "forced tag" in Girl.RecentActions:
                            ch_v "Нууу. . . Мне жаль, что до этого дошло. . ."
                            ch_v "Надеюсь, мы в будущем сможем найти общий язык. . ."
                    elif not Girl.Forced:
                            ch_v "Спасибо. . . "
                            ch_v "Ты не тоскуешь по солнечному свету, пока его не потеряешь."
                            if ApprovalCheck(Girl, 750):
                                ch_v "И это было не так уж плохо, правда?"
                            else:
                                if not Player.Male:
                                    ch_v "И спасибо, что не воспользовалась ситуацией для своей выгоды."
                                else:
                                    ch_v "И спасибо, что не воспользовался ситуацией для своей выгоды."
                    else:
                            if not Player.Male:
                                ch_v "Думаю, такова плата за возможность снова выходить на солнечный свет. . ."
                                ch_v "Не могла бы ты, пожалуйста, быть немного меньшей сучкой в этом вопросе?"
                            else:
                                ch_v "Думаю, такова плата за возможность снова выходить на солнечный свет. . ."
                                ch_v "Не мог бы ты, пожалуйста, быть немного меньшим мудаком в этом вопросе?"
                else:
                    if "forced tag" in Girl.RecentActions:
                            ch_v "Не подталкивай меня снова к \"красной черте\". . ."
                    elif not Girl.Forced:
                            ch_v "Хммм, это было приятно, [Girl.Petname]."
                            ch_v "Увидимся в следующий раз, когда я загорю. . ."
                    else:
                            ch_v "Ладно, думаю, мы получили от этого то, что хотели. . ."
                            ch_v "По крайней мере, пока. . ."
        elif Girl is GwenX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions:
                            ch_g "Эм. . . извини. . ."
                            ch_g "-но не нужно все усложнять. . ."
                    elif not Girl.Forced:
                            ch_g "Ох, спасибо, мне уже лучше. . ."
                            if not Player.Male:
                                ch_g "Спасибо, что помогла мне, [Girl.Petname]."
                            else:
                                ch_g "Спасибо, что помог мне, [Girl.Petname]."
                            if ApprovalCheck(Girl, 750):
                                ch_g "И тебе ведь тоже было очень весело, да?"
                            else:
                                if not Player.Male:
                                    ch_g "И, эм. . . спасибо, что не давила на меня?"
                                else:
                                    ch_g "И, эм. . . спасибо, что не давил на меня?"
                    else:
                            $ Girl.Statup("Love", 90, -5)
                            ch_g "Ладно, думаю, мы оба получили что-то полезное. . ."
                            ch_g "Хотя медом можно привлечь больше мух, ты это знаешь?"
                else:
                    if "forced tag" in Girl.RecentActions:
                            ch_g "Ладно. . . извини. . ."
                    elif not Girl.Forced:
                            ch_g "Ладно, увидимся позже."
                    else:
                            $ Girl.Statup("Love", 90, -5)
                            ch_g "Ладно, мы в расчете. . ."
        elif Girl is BetsyX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions:
                            if not Player.Male:
                                ch_b "Я. . . приношу свои извинения. . ."
                                ch_b "-Однако, боюсь, что ты не оставил мне выбора. . ."
                            else:
                                ch_b "Я. . . приношу свои извинения. . ."
                                ch_b "-Однако, боюсь, что ты не оставила мне выбора. . ."
                    elif not Girl.Forced:
                            ch_b "Ох, так гораздо лучше. . ."
                            ch_b "Спасибо за помощь, [Girl.Petname]."
                            if ApprovalCheck(Girl, 750):
                                ch_b "Уверена, что тебе тоже понравилось, не так ли?"
                            else: #not good with you
                                ch_b "Я. . . очень ценю твою сдержанность. . ."
                    else: #forced
                            $ Girl.Statup("Love", 90, -5)
                            ch_b "Пожалуй, что каждый из нас получил какую-то выгоду. . ."
                            if not Player.Male:
                                ch_b "Я бы очень хотела, чтобы ты был добрее. . ."
                            else:
                                ch_b "Я бы очень хотела, чтобы ты была добрее. . ."
                else:
                    if "forced tag" in Girl.RecentActions:
                            ch_b "Еще раз прошу прощения. . ."
                    elif not Girl.Forced:
                            ch_b "Хорошо, увидимся позже."
                    else: #forced
                            $ Girl.Statup("Love", 90, -5)
                            ch_b "Теперь, думаю, мы квиты. . ."
        elif Girl is DoreenX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions:
                            ch_d "Извини за это. . ."
                            ch_d "Это было грубо, но я была сама не своя. . ."
                    elif not Girl.Forced:
                            ch_d "Ох, так-то лучше. . ."
                            ch_d "Спасибо за помощь, [Girl.Petname]."
                            if ApprovalCheck(Girl, 750):
                                ch_d "Тебе ведь было весело, правда?"
                            else: #not good with you
                                ch_d "И спасибо за. . . ну, ты знаешь. . ."
                    else: #forced
                            $ Girl.Statup("Love", 90, -5)
                            ch_d "Что ж, что каждый из нас получил какую-то выгоду. . ."
                            if not Player.Male:
                                ch_d "Ты могла бы быть более покладистой. . ."
                            else:
                                ch_d "Ты мог бы быть более покладистым. . ."
                else:
                    if "forced tag" in Girl.RecentActions:
                            ch_d "Еще раз извини. . ."
                    elif not Girl.Forced:
                            ch_d "Отлично. Увидимся позже."
                    else: #forced
                            $ Girl.Statup("Love", 90, -5)
                            ch_d "Думаю. . . теперь мы в расчете?"
        elif Girl is WandaX:
                if Girl.Event[1] < 11:
                    if "forced tag" in Girl.RecentActions:
                            ch_w "Мне. . . правда жаль. . ."
                            ch_w "Я чувствовала, будто сейчас взорвусь. . ."
                    elif not Girl.Forced:
                            ch_w "Это так здорово. . ."
                            ch_w "Спасибо за помощь, [Girl.Petname]."
                            if ApprovalCheck(Girl, 750):
                                ch_w "Тебе ведь тоже понравилось, правда?"
                            else: #not good with you
                                if not Player.Male:
                                    ch_w "Ты могла заставить меня сделать то, чего я. . ."
                                else:
                                    ch_w "Ты мог заставить меня сделать то, чего я. . ."
                                ch_w "Спасибо."
                    else: #forced
                            $ Girl.Statup("Love", 90, -3)
                            ch_w "Жаль, что мы не смогли найти лучшего решения. . ."
                else:
                    if "forced tag" in Girl.RecentActions:
                            ch_w "Еще раз извини. . ."
                    elif not Girl.Forced:
                            ch_w "Спасибо."
                    else: #forced
                            $ Girl.Statup("Love", 90, -5)
                            ch_w "Ну что, теперь мы квиты?"
        if Girl.Event[1] < 11:
                $ Girl.Event[1] = 11
        $ Girl.Event[1] += 1
        $ Girl.DailyActions.append("fixed")
        if "forced tag" not in Girl.RecentActions:
            menu:
                extend ""
                "Пока":
                        pass
                "Увидимся в следующий раз. . .":
                    if not Girl.Forced and ApprovalCheck(Girl, 800):
                            $ Girl.FaceChange("bemused",1,Eyes="side")
                            if Girl is RogueX:
                                    ch_r "Ага, увидимся."
                            elif Girl is KittyX:
                                    ch_k "Хорошо, круто."
                            elif Girl is EmmaX:
                                    ch_e "Пожалуй. . ."
                            elif Girl is LauraX:
                                    ch_l "Ладно."
                            elif Girl is JeanX:
                                    ch_j "Да?"
                            elif Girl is StormX:
                                    ch_s "До встречи."
                            elif Girl is JubesX:
                                    ch_v "Ага, конечно."
                            elif Girl is GwenX:
                                    ch_g "Хорошо, до следующего раза. . ."
                            elif Girl is BetsyX:
                                    ch_b "Скорее всего."
                            elif Girl is DoreenX:
                                    ch_d "Конечно, увидимся."
                            elif Girl is WandaX:
                                    ch_w "Ага, увидимся. . ."
                    else:
                            $ Girl.FaceChange("angry",1)
                            $ Girl.Statup("Love", 60, -2)
                            $ Girl.Statup("Love", 80, -2)
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Obed", 70, 2)
                            "Она хмурится"
                "Не хочешь задержаться?":
                    if not Girl.Forced and ApprovalCheck(Girl, 800, "LI"):
                            $ Girl.FaceChange("smile",1)
                            $ Party.append(Girl)
                            if Girl is RogueX:
                                    ch_r "Конечно."
                            elif Girl is KittyX:
                                    ch_k "Хорошо, круто."
                            elif Girl is EmmaX:
                                    ch_e "Полагаю, я могу выделить время. . ."
                            elif Girl is LauraX:
                                    ch_l "Ладно."
                            elif Girl is JeanX:
                                    ch_j "Да?"
                            elif Girl is StormX:
                                    ch_s "Можно. . ."
                            elif Girl is JubesX:
                                    ch_v "Конечно, наверное."
                            elif Girl is GwenX:
                                    ch_g "Думаю, можно. . ."
                            elif Girl is BetsyX:
                                    ch_b "У меня действительно есть немного времени. . ."
                            elif Girl is DoreenX:
                                    ch_d "Хорошо."
                            elif Girl is WandaX:
                                    ch_w "Конечно."
                    else:
                            $ Girl.FaceChange("angry",1)
                            $ Girl.Statup("Love", 80, -2)
                            $ Girl.Statup("Obed", 50, 1)
                            $ Girl.Statup("Obed", 70, 1)
                            if Girl is RogueX:
                                    ch_r "Нет, спасибо."
                            elif Girl is KittyX:
                                    ch_k "Эм. . . нет. . ."
                            elif Girl is EmmaX:
                                    ch_e "Это не то, чего я хочу. . ."
                            elif Girl is LauraX:
                                    ch_l "Неа."
                            elif Girl is JeanX:
                                    ch_j "Нет?"
                            elif Girl is StormX:
                                    if not Player.Male:
                                        ch_s "Ты не прочувствовала ситуацию. . ."
                                    else:
                                        ch_s "Ты не прочувствовал ситуацию. . ."
                            elif Girl is JubesX:
                                    ch_v "Я совсем не в настроении. . ."
                            elif Girl is GwenX:
                                    ch_g "Не. . . сейчас. . ."
                            elif Girl is BetsyX:
                                    ch_b "Я не вижу причин это делать."
                            elif Girl is DoreenX:
                                    ch_d ". . . нет, спасибо."
                            elif Girl is WandaX:
                                    ch_w "Я бы. . . этого не хотела. . ."
        jump Addicted_Bad_End

# end Event Addiction_Fix /////////////////////////////////////////////////////



label Addicted_Serum: #rkeljsvgbdw
        # if Girl.Chat[2], she's tried it before
        # if Girl.Chat[3], she knows it's jiz

        if "no serum" in Girl.RecentActions:
                if Girl is RogueX:
                        if not Player.Male:
                            ch_r "Нет, мы уже пробовали, но ты все испортила."
                        else:
                            ch_r "Нет, мы уже пробовали, но ты все испортил."
                elif Girl is KittyX:
                        ch_k "Неа, лучше предложи что-нибудь другое."
                elif Girl is EmmaX:
                        ch_e "Боюсь, у тебя уже был шанс."
                elif Girl is LauraX:
                        ch_l "Время для плана Б, [Girl.Petname]."
                elif Girl is JeanX:
                        if not Player.Male:
                            ch_j "Ты упустила свой шанс, [Girl.Petname]."
                        else:
                            ch_j "Ты упустил свой шанс, [Girl.Petname]."
                elif Girl is StormX:
                        ch_s "Нет, я так не думаю."
                elif Girl is JubesX:
                        ch_v "Без шансов."
                elif Girl is GwenX:
                        ch_g "Ни за что. . ."
                elif Girl is BetsyX:
                        ch_b "Конечно, нет."
                elif Girl is DoreenX:
                        ch_d "Ни в коем случае, оно слишком сомнительное."
                elif Girl is WandaX:
                        ch_w "Я не хочу ввязываться в подобное."
                return
        $ CountStore = Girl.Action
        $ Girl.Action = 0

        if not Girl.Chat[2]:
            #if this is the first time she's tried it. . .  "Have you considered a . . . chemical solution?"
            $ Girl.FaceChange("confused")
            if Girl is RogueX:
                    ch_r "Что ты имеешь в виду?"
            elif Girl is KittyX:
                    ch_k "Что за вещество?"
            elif Girl is EmmaX:
                    ch_e "Ох? В каком смысле?"
            elif Girl is LauraX:
                    ch_l "А?"
            elif Girl is JeanX:
                    ch_j "Ты о чем?"
            elif Girl is StormX:
                    ch_s "Что ты предлагаешь?"
            elif Girl is JubesX:
                    ch_v "Если это кровь."
                    ch_v "Я только за."
                    $ Girl.FaceChange("startled")
                    ch_v "Это ведь кровь, правда?!"
            elif Girl is GwenX:
                    ch_g "О каких веществах мы сейчас говорим? . ."
            elif Girl is BetsyX:
                    ch_b "Что ты имеешь под этим в виду?"
            elif Girl is DoreenX:
                    ch_d "А? Ты это о чем?"
            elif Girl is WandaX:
                    ch_w "О каком веществе ты говоришь?"
            menu:
                extend ""
                "Думаю, я могла бы. . . [[обмануть её]" if not Player.Male:
                        ch_p "Я просто подумала, в последнее время я очень усердно занималась и, возможно, я смогу приготовить. . . сыворотку, которая облегчит твои симптомы."
                        $ Girl.FaceChange()
                        if Girl is RogueX:
                                ch_r "Хмм. . . я за, если думаешь, что она сможет мне помочь."
                        elif Girl is KittyX:
                                ch_k "Хм, правда? Ты не похожа на гуру химии, но пофиг, давай попробуем."
                        elif Girl is EmmaX:
                                ch_e "Считай меня немного скептически настроенной, учитывая твои оценки, но ладно, я открыта для преложений."
                        elif Girl is LauraX:
                                ch_l "Хм. . . Ладно, думаю, попробовать можно."
                        elif Girl is JeanX:
                                ch_j "Что?"
                                ch_j "То есть, я хотела сказать, что попробовать можно. . ."
                        elif Girl is StormX:
                                ch_s "Учитывая твои оценки, я не уверена, что в этом тебе можно довериться. . ."
                        elif Girl is JubesX:
                                ch_v "Так, значит, это -не- кровь. . ."
                                ch_v "Нууу, я думаю, в жизни стоит попробовать все . . ."
                        elif Girl is GwenX:
                                ch_g "Ох, похоже тут все супер-пупер ученые. . ."
                                ch_g "И почему я не удивлена?"
                        elif Girl is BetsyX:
                                ch_b ". . . какой у тебя совершенно незаурядный талант. . ."
                        elif Girl is DoreenX:
                                ch_d ". . . ты можешь ее приготовить? Думаю, стоит попробовать. . ."
                        elif Girl is WandaX:
                                ch_w "Хм, думаю, попробовать можно. . ."

                "Думаю, я мог бы. . . [[обмануть её]" if Player.Male:
                        ch_p "Я просто подумал, в последнее время я очень усердно занимался и, возможно, я смогу приготовить. . . сыворотку, которая облегчит твои симптомы."
                        $ Girl.FaceChange()
                        if Girl is RogueX:
                                ch_r "Хмм. . . я за, если думаешь, что она сможет мне помочь."
                        elif Girl is KittyX:
                                ch_k "Хм, правда? Ты не похож на гуру химии, но пофиг, давай попробуем."
                        elif Girl is EmmaX:
                                ch_e "Считай меня немного скептически настроенной, учитывая твои оценки, но ладно, я открыта для преложений."
                        elif Girl is LauraX:
                                ch_l "Хм. . . Ладно, думаю, попробовать можно."
                        elif Girl is JeanX:
                                ch_j "Что?"
                                ch_j "То есть, я хотела сказать, что попробовать можно. . ."
                        elif Girl is StormX:
                                ch_s "Учитывая твои оценки, я не уверена, что в этом тебе можно довериться. . ."
                        elif Girl is JubesX:
                                ch_v "Так, значит, это -не- кровь. . ."
                                ch_v "Нууу, я думаю, в жизни стоит попробовать все . . ."
                        elif Girl is GwenX:
                                ch_g "Ох, похоже тут все супер-пупер ученые. . ."
                                ch_g "И почему я не удивлена?"
                        elif Girl is BetsyX:
                                ch_b ". . . какой у тебя совершенно незаурядный талант. . ."
                        elif Girl is DoreenX:
                                ch_d ". . . ты можешь ее приготовить? Думаю, стоит попробовать. . ."
                        elif Girl is WandaX:
                                ch_w "Хм, думаю, попробовать можно. . ."

                "Это моя сперма" if Player.Male:
                        $ Girl.Blush = 1
                        if Girl is RogueX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_r "Хм, ну, в прошлый раз, вроде бы, она мне помогла. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_r "Твоя что? . . . Ты хочешь, чтобы я выпила твою сперму?"
                                if ApprovalCheck(Girl, 750) and not Girl.Forced:
                                        $ Girl.FaceChange("sexy")
                                        ch_r "Ну, если таков план, может, я возьму ее сразу из источника?"
                                else:
                                        ch_r "Хорошо, думаю, если прикосновения к тебе помогают, то и она может помочь. . ."
                        elif Girl is KittyX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_k "Ну. . .  она должна помочь. . ."
                                else:
                                        $ Girl.FaceChange("surprised",2)
                                        ch_k "Твоя что? . . . Ты хочешь, чтобы я. . ."
                                        ch_k ". . . выпила твою сперму?"
                                if ApprovalCheck(Girl, 850) and not Girl.Forced:
                                        $ Girl.FaceChange("sexy")
                                        ch_k "Я бы не хотела пить ее из бутылки. . ."
                                else:
                                        ch_k "Ну, если сработает, это будет, пожалуй, самый простой способ. . ."
                        elif Girl is EmmaX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_e "Полагаю, у нее есть кое-какие. . . тонизирующие свойства. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_e "Хорошо. . . Полагаю, в этом определенно есть смысл. . ."
                                if ApprovalCheck(Girl, 950) and not Girl.Forced:
                                        $ Girl.FaceChange("sexy")
                                        ch_e "Знаешь, я могла бы выпить сразу из источника. . ."
                                else:
                                        ch_e "Я получала предложения и похуже. . ."
                        elif Girl is LauraX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_l "Да, в этом есть смысл. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_l "А? Хм. . . да, в этом есть смысл."
                                if ApprovalCheck(Girl, 850):
                                        $ Girl.FaceChange("sexy")
                                        ch_l "Не хочешь, чтобы я сама взяла ее?"
                                else:
                                        ch_l "Ну, давай попробуем?"
                        elif Girl is JeanX:
                                $ Girl.Statup("Obed", 80, 1)
                                $ Girl.Statup("Inbt", 80, 2)
                                if Girl.Swallow:
                                        $ Girl.FaceChange("surprised")
                                        ch_j "Ох!"
                                        $ Girl.FaceChange("bemused")
                                        ch_j "Ага, она помогает. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_j "Ну, может и поможет, если она твоя. . ."
                                if ApprovalCheck(Girl, 850):
                                        $ Girl.FaceChange("sexy")
                                        ch_j "Ты хочешь просто дать мне ее или же. . ."
                                else:
                                        ch_j "И чего мы ждем?"
                        elif Girl is StormX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_s "В прошлом она помогала. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_s "Хммм. . . с учетом того, как работают твои силы, это может помочь. . ."
                                if ApprovalCheck(Girl, 950):
                                        $ Girl.FaceChange("sexy")
                                        ch_s "Я не против. . . взять немного напрямую. . ."
                                else:
                                        ch_s "Я подумаю об этом. . ."
                        elif Girl is JubesX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_v "Думаю, она тоже помогает. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_v "Твоя что? . . . Сперма?"
                                if ApprovalCheck(Girl, 750) and not Girl.Forced:
                                        $ Girl.FaceChange("sexy")
                                        ch_v "Я всегда могу просто высосать тебя досуха сама. . ."
                                else:
                                        ch_v "Нууу, это что-то -вроде- крови. . ."
                        elif Girl is GwenX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_g "Ох. . . Ну, она действительно помогает. . ."
                                else:
                                        $ Girl.FaceChange("surprised",2)
                                        ch_g "А?!"
                                        ch_g "Ты хочешь, чтобы. . . я. . ."
                                        ch_g ". . . выпила твою сперму?"
                                if ApprovalCheck(Girl, 850) and not Girl.Forced:
                                        $ Girl.FaceChange("sexy")
                                        ch_g "Может я просто присосусь к источнику?"
                                else:
                                        ch_g "Ну, я думаю, это может сработать. . ."
                        elif Girl is BetsyX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_b "Ох. . . да, она весьма эффективна. . ."
                                else:
                                        $ Girl.FaceChange("surprised",2)
                                        ch_b "Ох?"
                                        ch_b "Ты ждешь, что. . . я. . ."
                                        ch_b ". . . выпью твою сперму?"
                                if ApprovalCheck(Girl, 850) and not Girl.Forced:     #if she likes you, she offers sex instead
                                        $ Girl.FaceChange("sexy")
                                        ch_b "Не проще ли выпить сразу из источника?"
                                else:
                                        ch_b "И правда. . . Пожалуй, она может помочь. . ."
                        elif Girl is DoreenX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_d "Хм. . . ну, она вроде как работает. . ."
                                else:
                                        $ Girl.FaceChange("confused",1)
                                        ch_d "Ох. . ."
                                        $ Girl.FaceChange("surprised",2,Mouth="open")
                                        ch_d "Подожди, что?!. . ."
                                        ch_d ". . . ты предлагаешь мне выпить твою сперму?"
                                if ApprovalCheck(Girl, 850) and not Girl.Forced:     #if she likes you, she offers sex instead
                                        $ Girl.FaceChange("sexy")
                                        ch_d "Думаю, я могла бы выпить ее прямо из источника. . ."
                                else:
                                        ch_d "Хм. . . Думаю, это может сработать. . ."
                        elif Girl is WandaX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_w "Ох. . . что ж, думаю, она и правда помогает. . ."
                                else:
                                        $ Girl.FaceChange("confused",1)
                                        ch_w "А?"
                                        $ Girl.FaceChange("surprised",2,Mouth="open")
                                        ch_w "Значит, ты хочешь, чтобы я. . ."
                                        ch_w ". . . выпила твою сперму?"
                                if ApprovalCheck(Girl, 850) and not Girl.Forced:     #if she likes you, she offers sex instead
                                        $ Girl.FaceChange("sexy")
                                        ch_w "Ну, думаю, я могла бы взять ее из источника. . ."
                                else:
                                        ch_w "Хм. . . она может помочь. . ."
                        $ Tempmod += 20
                        $ Girl.Chat[3] = 1

                "Это соки моей киски" if not Player.Male:
                        $ Girl.Blush = 1
                        if Girl is RogueX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_r "Хм, ну, в прошлый раз, вроде бы, они мне помогли. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_r "Твои что? . . . Ты хочешь, чтобы я выпила твои соки?"
                                if ApprovalCheck(Girl, 750) and not Girl.Forced:
                                        $ Girl.FaceChange("sexy")
                                        ch_r "Ну, если таков план, может, я возьму их сразу из источника?"
                                else:
                                        ch_r "Хорошо, думаю, если прикосновения к тебе помогают, то и они могут помочь. . ."
                        elif Girl is KittyX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_k "Ну. . .  они должны помочь. . ."
                                else:
                                        $ Girl.FaceChange("surprised",2)
                                        ch_k "Твои что? . . . Ты хочешь, чтобы я. . ."
                                        ch_k ". . . выпила твои соки?"
                                if ApprovalCheck(Girl, 850) and not Girl.Forced:
                                        $ Girl.FaceChange("sexy")
                                        ch_k "Я бы не хотела пить их из бутылки. . ."
                                else:
                                        ch_k "Ну, если сработает, это будет, пожалуй, самый простой способ. . ."
                        elif Girl is EmmaX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_e "Полагаю, у них есть кое-какие. . . тонизирующие свойства. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_e "Хорошо. . . Полагаю, в этом определенно есть смысл. . ."
                                if ApprovalCheck(Girl, 950) and not Girl.Forced:
                                        $ Girl.FaceChange("sexy")
                                        ch_e "Знаешь, я могла бы выпить их сразу из источника. . ."
                                else:
                                        ch_e "Я получала предложения и похуже. . ."
                        elif Girl is LauraX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_l "Да, в этом есть смысл. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_l "А? Хм. . . да, в этом есть смысл."
                                if ApprovalCheck(Girl, 850):
                                        $ Girl.FaceChange("sexy")
                                        ch_l "Не хочешь, чтобы я сама взяла их?"
                                else:
                                        ch_l "Ну, давай попробуем?"
                        elif Girl is JeanX:
                                $ Girl.Statup("Obed", 80, 1)
                                $ Girl.Statup("Inbt", 80, 2)
                                if Girl.Swallow:
                                        $ Girl.FaceChange("surprised")
                                        ch_j "Ох!"
                                        $ Girl.FaceChange("bemused")
                                        ch_j "Ага, они помогают. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_j "Ну, может и поможет, если они твои. . ."
                                if ApprovalCheck(Girl, 850):
                                        $ Girl.FaceChange("sexy")
                                        ch_j "Ты хочешь просто дать мне их или же. . ."
                                else:
                                        ch_j "И чего мы ждем?"
                        elif Girl is StormX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_s "В прошлом они помогали. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_s "Хммм. . . с учетом того, как работают твои силы, это может помочь. . ."
                                if ApprovalCheck(Girl, 950):
                                        $ Girl.FaceChange("sexy")
                                        ch_s "Я не против. . . взять немного напрямую. . ."
                                else:
                                        ch_s "Я подумаю об этом. . ."
                        elif Girl is JubesX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_v "Думаю, они тоже помогают. . ."
                                else:
                                        $ Girl.FaceChange("surprised")
                                        ch_v "Твои что? . . . Соки?"
                                if ApprovalCheck(Girl, 750) and not Girl.Forced:
                                        $ Girl.FaceChange("sexy")
                                        ch_v "Я всегда могу просто высосать тебя досуха сама. . ."
                                else:
                                        ch_v "Нууу, это что-то -вроде- крови. . ."
                        elif Girl is GwenX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_g "Ох. . . Ну, они действительно помогают. . ."
                                else:
                                        $ Girl.FaceChange("surprised",2)
                                        ch_g "А?!"
                                        ch_g "Ты хочешь, чтобы. . . я. . ."
                                        ch_g ". . . выпила твою соки?"
                                if ApprovalCheck(Girl, 850) and not Girl.Forced:
                                        $ Girl.FaceChange("sexy")
                                        ch_g "Может я просто присосусь к источнику?"
                                else:
                                        ch_g "Ну, я думаю, это может сработать. . ."
                        elif Girl is BetsyX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_b "Ох. . . да, они весьма эффективны. . ."
                                else:
                                        $ Girl.FaceChange("surprised",2)
                                        ch_b "Ох?"
                                        ch_b "Ты ждешь, что. . . я. . ."
                                        ch_b ". . . выпью твои соки?"
                                if ApprovalCheck(Girl, 850) and not Girl.Forced:     #if she likes you, she offers sex instead
                                        $ Girl.FaceChange("sexy")
                                        ch_b "Не проще ли выпить сразу из источника?"
                                else:
                                        ch_b "И правда. . . Пожалуй, они могут помочь. . ."
                        elif Girl is DoreenX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_d "Хм. . . ну, они вроде как помогают. . ."
                                else:
                                        $ Girl.FaceChange("confused",1)
                                        ch_d "Ох. . ."
                                        $ Girl.FaceChange("surprised",2,Mouth="open")
                                        ch_d "Подожди, что?!. . ."
                                        ch_d ". . . ты предлагаешь мне выпить твои соки?"
                                if ApprovalCheck(Girl, 850) and not Girl.Forced:     #if she likes you, she offers sex instead
                                        $ Girl.FaceChange("sexy")
                                        ch_d "Думаю, я могла бы выпить их прямо из источника. . ."
                                else:
                                        ch_d "Хм. . . Думаю, это может сработать. . ."
                        elif Girl is WandaX:
                                if Girl.Swallow:
                                        $ Girl.FaceChange("bemused")
                                        ch_w "Ох. . . что ж, думаю, они и правда помогают. . ."
                                else:
                                        $ Girl.FaceChange("confused",1)
                                        ch_w "А?"
                                        $ Girl.FaceChange("surprised",2,Mouth="open")
                                        ch_w "Значит, ты хочешь, чтобы я. . ."
                                        ch_w ". . . выпила твои соки?"
                                if ApprovalCheck(Girl, 850) and not Girl.Forced:     #if she likes you, she offers sex instead
                                        $ Girl.FaceChange("sexy")
                                        ch_w "Ну, думаю, я могла бы взять их из источника. . ."
                                else:
                                        ch_w "Хм. . . они могут помочь. . ."
                        $ Tempmod += 20
                        $ Girl.Chat[3] = 1

                "Неважно.":
                    $ Girl.Action = CountStore
                    return

        elif Girl.Chat[3]:
                #if she knows it's jiz. . .
                $ Girl.FaceChange("bemused", 1)
                $ Tempmod += 20
                if Girl is RogueX:
                        ch_r "Хм, В прошлый раз все было хорошо. . ."
                        if ApprovalCheck(Girl, 750) and not Girl.Forced:
                                $ Girl.FaceChange("sexy")
                                ch_r "Я бы хотела получить ее прямо из источника. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal"
                                ch_r "Я думаю, что это такое же хорошее \"лечение\", как и любое другое."
                elif Girl is KittyX:
                        ch_k "Ну, она вкусная. . ."
                        if ApprovalCheck(Girl, 850) and not Girl.Forced:
                                $ Girl.FaceChange("sexy")
                                ch_k "Я не пью \"молочко\" из банки. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal"
                                ch_k "Думаю, это сработает."
                elif Girl is EmmaX:
                        ch_e "У тебя совсем уникальный вкус. . ."
                        if ApprovalCheck(Girl, 950) and not Girl.Forced:
                                $ Girl.FaceChange("sexy")
                                ch_e "Я лучше приму лекарство. . . напрямую."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal"
                                ch_e "Полагаю, можно."
                elif Girl is LauraX:
                        ch_l "Да. . . то есть, в прошлый раз все было довольно хорошо. . ."
                        if ApprovalCheck(Girl, 850) and not Girl.Forced:
                                $ Girl.FaceChange("sexy")
                                if not Player.Male:
                                    ch_l "Я бы хотела получить ее прямо из источника. . ."
                                else:
                                    ch_l "Я бы хотела получить ее прямо из шланга. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal"
                                ch_l "Я думаю, она поможет."
                elif Girl is JeanX:
                        ch_j "Ну, она вкусная. . ."
                        if ApprovalCheck(Girl, 850) and not Girl.Forced:
                                $ Girl.FaceChange("sexy")
                                if not Player.Male:
                                    ch_j "Я могла бы просто отлизать тебе или типа того. . ."
                                else:
                                    ch_j "Я могла бы просто отсосать тебе или типа того. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal"
                                ch_j "Думаю, я не против. . ."
                elif Girl is StormX:
                        ch_s "В прошлый раз мне она понравилась. . ."
                        if ApprovalCheck(Girl, 950) and not Girl.Forced:
                                $ Girl.FaceChange("sexy")
                                ch_s "Я могла бы взять ее напрямую. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal"
                                ch_s "Пожалуй, с ней можно работать."
                elif Girl is JubesX:
                        ch_v "Думаю, один коктейль не хуже другого. . ."
                        if ApprovalCheck(Girl, 750) and not Girl.Forced:
                                $ Girl.FaceChange("sexy")
                                ch_v "Я всегда могу просто высосать тебя досуха сама. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal"
                                ch_v "Конечно, почему нет."
                elif Girl is GwenX:
                        ch_g "Думаю, она хорошо заходит. . ."
                        if ApprovalCheck(Girl, 850) and not Girl.Forced:
                                $ Girl.FaceChange("sexy")
                                ch_g "Я бы не отказался получить ее из источника. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal"
                                ch_g "Конечно. . ."
                elif Girl is BetsyX:
                        ch_b "Пожалуй, она хорошо заходит. . ."
                        if ApprovalCheck(Girl, 850) and not Girl.Forced:
                                $ Girl.FaceChange("sexy")
                                ch_b "Я могла бы собрать ее сама. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal"
                                ch_b "Очень хорошо. . ."
                elif Girl is DoreenX:
                        ch_d "Думаю, она хорошо заходит. . ."
                        if ApprovalCheck(Girl, 950) and not Girl.Forced:
                                $ Girl.FaceChange("sexy")
                                ch_d "Не возражаешь, если я наберу ее сама? . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal"
                                ch_d "Что ж, попробовать стоит. . ."
                elif Girl is WandaX:
                        ch_w "Ну, она довольно вкусная. . ."
                        if ApprovalCheck(Girl, 950) and not Girl.Forced:
                                $ Girl.FaceChange("sexy")
                                ch_w "Я могла бы собрать ее сама. . ."
                        else:
                                $ Girl.FaceChange("sad")
                                $ Girl.Brows = "normal"
                                ch_w "Думаю, стоит попробовать. . ."
        elif Girl.Chat[2]:
                #if she's tried it before. . .
                if not Player.Male:
                    ch_p "Я тут подумала, я мог бы приготовить еще сыворотки. . ."
                else:
                    ch_p "Я тут подумал, я мог бы приготовить еще сыворотки. . ."
                $ Girl.FaceChange("bemused")
                if Girl is RogueX:
                        ch_r "Ну, что бы это на самом деле ни было, в прошлый раз она помогло мне достаточно хорошо. . ."
                elif Girl is KittyX:
                        ch_k "Ну, похоже она работает. . ."
                elif Girl is EmmaX:
                        ch_e "Да. . .  это определенно. . . интересный продукт. . ."
                elif Girl is LauraX:
                        ch_l "Да, ладно. Хотя она на вкус похожа на сперму. . ."
                elif Girl is JeanX:
                        ch_j "Ага, \"сыворотку\" -подмигивает-."
                elif Girl is StormX:
                        ch_s "Ох, хорошо. Она не так уж и плоха. . ."
                elif Girl is JubesX:
                        if not Player.Male:
                            ch_v "Ага, уверена, ты бы могла. . ."
                        else:
                            ch_v "Ага, уверена, ты бы мог. . ."
                elif Girl is GwenX:
                        ch_g "Ну, я думаю, она помогла довольно хорошо. . ."
                elif Girl is BetsyX:
                        ch_b "В прошлый раз она мне хорошо помогла. . ."
                elif Girl is DoreenX:
                        ch_d "Она была -на удивление- эффективной. . ."
                elif Girl is WandaX:
                        ch_w "Она -действительно- уменьшила мою зависимость. . ."
                $ Tempmod += 10

        #pricing
        $ Count = 3
        while Count and "has serum" not in Girl.RecentActions:
            $ Line = 0
            $ Count -= 1
            menu:
                "Хотите попросить что-нибудь взамен?"
                "[[Просто отдать]":
                        $ Girl.Forced = 0
                        $ Girl.Mouth = "smile"
                        $ Girl.Statup("Love", 50, 1,Alt=[[JeanX],500,3])
                        ch_p "Держи."
                        $ Girl.RecentActions.append("has serum")

                "Ну, взамен ты могла бы подрочить мне рукой. . .":
                        $ Girl.FaceChange("sexy")
                        if ApprovalCheck(Girl, 1100) or (ApprovalCheck(Girl, 800) and Girl.Chat[2]):
                                $ Girl.ArmPose = 2
                                if Girl is RogueX:
                                        if Girl.Chat[3]:
                                                ch_r "Хах, думаю, я не против немного размять кисть."
                                        else:
                                                ch_r "Ладно, если ты так этого хочешь. . ."
                                elif Girl is KittyX:
                                        if Girl.Chat[3]:
                                                ch_k "Ох, рукой так рукой. . ."
                                        else:
                                                ch_k "Хмм, да, думаю, я готова заплатить такую цену. . ."
                                elif Girl is EmmaX:
                                        if Girl.Chat[3]:
                                                ch_e "Хорошо, я могу сделать тебе приятно. . ."
                                        else:
                                                ch_e "Полагаю, это взаимовыгодный обмен. . ."
                                elif Girl is LauraX:
                                                ch_l "Конечно, моя рука в твоем распоряжении. . ."
                                elif Girl is JeanX:
                                                $ Girl.Statup("Obed", 80, 2)
                                                ch_j "Конечно, почему нет. . ."
                                elif Girl is StormX:
                                                ch_s "Пожалуй, это я могу. . ."
                                elif Girl is JubesX:
                                                ch_v "Конечно, все в порядке. . ."
                                elif Girl is GwenX:
                                                ch_g "Эм, ладно, думаю, это справедливая сделка. . ."
                                elif Girl is BetsyX:
                                                ch_b "Пожалуй, я могу тебе помочь. . ."
                                elif Girl is DoreenX:
                                                ch_d "Думаю, я могу протянуть тебе руку помощи. . ."
                                elif Girl is WandaX:
                                                ch_w "И так всегда. . ."
                                if  Player.Male:
                                        call Girl_HJ_Prep # call expression Girl.Tag + "_HJ_Prep"
                                else:
                                        call Girl_Finger_Prep
                                $ Girl.Statup("Obed", 70, 1)
                                $ Girl.Statup("Inbt", 50, 2)
                                $ Girl.Statup("Inbt", 70, 1)
                                $ Girl.RecentActions.append("has serum")
                        else:
                                $ Girl.Brows = "confused"
                                if Girl is RogueX:
                                        ch_r "Пфф, я бы этого не хотела."
                                elif Girl is KittyX:
                                        ch_k "Хихи, как будто я соглашусь."
                                elif Girl is EmmaX:
                                        ch_e "Ох, уверена, тебе бы это понравилось."
                                elif Girl is LauraX:
                                        ch_l "Хех, ну да, так я и согласилась."
                                elif Girl is JeanX:
                                        ch_j "Хмм, мне не интересно."
                                elif Girl is StormX:
                                        if not Player.Male:
                                            ch_s "Тебе придется разобраться с этим самой."
                                        else:
                                            ch_s "Тебе придется разобраться с этим самому."
                                elif Girl is JubesX:
                                        ch_v "Эм, я бы предпочла этого не делать. . ."
                                elif Girl is GwenX:
                                        ch_g "Ха! Ни за что. . ."
                                elif Girl is BetsyX:
                                        ch_b "Уверяю тебя, мне это не интересно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Я. . . не буду заходить так далеко. . ."
                                elif Girl is WandaX:
                                        ch_w "Мне это неинтересно. . ."

                "Как насчет поработать ротиком?":
                        $ Girl.FaceChange("sexy")
                        if ApprovalCheck(Girl, 1300) or (ApprovalCheck(Girl, 800) and Girl.Chat[3]) or Girl is JubesX:
                                if Girl is RogueX:
                                        if Girl.Chat[3]:
                                                ch_r "Хах, ну тогда я возьму свое прямо из источника."
                                        else:
                                                ch_r "Я. . . думаю, я согласна. . ."
                                elif Girl is KittyX:
                                        if Girl.Chat[3]:
                                                ch_k "Ооо, прямо из источника. . ."
                                        else:
                                                ch_k "Хмм, да, думаю, я готова заплатить такую цену. . ."
                                elif Girl is EmmaX:
                                        if Girl.Chat[3]:
                                                ch_e "Не помешает получить ее прямиком из источника. . ."
                                        else:
                                                ch_e "Полагаю, это взаимовыгодный обмен. . ."
                                elif Girl is LauraX:
                                                ch_l "Я могла бы попробовать. . ."
                                elif Girl is JeanX:
                                                $ Girl.Statup("Obed", 80, 2)
                                                ch_j "Конечно, почему нет. . ."
                                elif Girl is StormX:
                                                ch_s "Если я должна. . ."
                                elif Girl is JubesX:
                                                ch_v "Думаю, это не будет ужасно. . ."
                                elif Girl is GwenX:
                                        if Girl.Chat[3]:
                                                ch_g "Ох. . . конечно, зачем тратить бутылку, верно?"
                                        else:
                                                ch_g "Ох. . . конечно. . ."
                                elif Girl is BetsyX:
                                                ch_b "Пожалуй, я справлюсь. . ."
                                elif Girl is DoreenX:
                                        if Girl.Chat[3]:
                                                ch_d "Ну, думаю, я могу попробовать. . ."
                                        else:
                                                ch_d "Мне кажется это немного чрезмерным. . ."
                                elif Girl is WandaX:
                                                ch_w "И так всегда. . ."
                                if  Player.Male:
                                        call Girl_BJ_Prep # call expression Girl.Tag + "_BJ_Prep"
                                else:
                                        call Girl_CUN_Prep
                                $ Girl.RecentActions.append("has serum")
                                $ Girl.Statup("Obed", 70, 1)
                                $ Girl.Statup("Inbt", 50, 2)
                                $ Girl.Statup("Inbt", 70, 1)
                        else:
                                $ Girl.Brows = "confused"
                                if Girl is RogueX:
                                        ch_r "Пфф, я бы этого не хотела."
                                elif Girl is KittyX:
                                        ch_k "Хихи, как будто я соглашусь."
                                elif Girl is EmmaX:
                                        ch_e "Ох, уверена, тебе бы это понравилось."
                                elif Girl is LauraX:
                                        ch_l "Хех, ну да, так я и согласилась."
                                elif Girl is JeanX:
                                        $ Girl.Statup("Obed", 80, 1)
                                        ch_j "Хмм, мне не интересно."
                                elif Girl is StormX:
                                        ch_s "Не думаю, что я соглашусь."
                                elif Girl is JubesX:
                                        ch_v "Скорее нет, чем да. . ."
                                elif Girl is GwenX:
                                        ch_g "Ха! Ни за что. . ."
                                elif Girl is BetsyX:
                                        ch_b "И речи быть не может!"
                                elif Girl is DoreenX:
                                        ch_d "Что? Да ни за что!"
                                elif Girl is WandaX:
                                        ch_w "Мне это неинтересно. . ."

                "Взамен выполнишь для меня одну услугу.":
                        $ Girl.FaceChange("sexy")
                        if Girl is RogueX:
                                ch_r "Ох? На какую услугу ты расчитываешь, [Girl.Petname]?"
                        elif Girl is KittyX:
                                ch_k "Да? Чего ты хочешь, [Girl.Petname]?"
                        elif Girl is EmmaX:
                                ch_e "Чего ты от меня хочешь, [Girl.Petname]?"
                        elif Girl is LauraX:
                                ch_l "Ладно, какую услугу ты ждешь, [Girl.Petname]?"
                        elif Girl is JeanX:
                                ch_j "Что за услугу?"
                        elif Girl is StormX:
                                ch_s "В каком смысле?"
                        elif Girl is JubesX:
                                ch_v "Хм. Например?"
                        elif Girl is GwenX:
                                ch_g "Ох, эм. . . например?"
                        elif Girl is BetsyX:
                                ch_b "Действительно? Какую? . ."
                        elif Girl is DoreenX:
                                ch_d "А? Какую?"
                        elif Girl is WandaX:
                                ch_w "И так всегда. . ."
                        $ Girl.Action = 1
                        call SexMenu # call expression Girl.Tag + "_SexMenu"
                        if "angry" not in Girl.RecentActions:
                                $ Girl.Statup("Love", 70, 2)
                                if Girl is RogueX:
                                        ch_r "Я рада, что мы пришли к согласию, [Girl.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Ладно, что дальше?"
                                elif Girl is EmmaX:
                                        ch_e "Полагаю, это было честно."
                                elif Girl is LauraX:
                                        ch_l "Ладно, теперь с этим покончено. . ."
                                elif Girl is JeanX:
                                        $ Girl.Statup("Obed", 50, 3)
                                        $ Girl.Statup("Obed", 80, 2)
                                        $ Girl.Statup("Inbt", 80, 2)
                                        ch_j "Хорошо, с этим мы разобрались."
                                elif Girl is StormX:
                                        ch_s "А теперь выполняй свою часть сделки."
                                elif Girl is JubesX:
                                        ch_v "Хорошо, теперь твоя очередь. . ."
                                elif Girl is GwenX:
                                        ch_g "Ладно, договорились, где моя \"сыворотка?\""
                                elif Girl is BetsyX:
                                        ch_b "Свою часть я выполнила, где моя \"сыворотка?\" . ."
                                elif Girl is DoreenX:
                                        ch_d "Ладно, думаю, теперь я заслужила \"сыворотку\". . ."
                                elif Girl is WandaX:
                                        ch_w "Ладно, думаю, этого хватит. . ."
                                $ Girl.Statup("Obed", 50, 1)
                                $ Girl.Statup("Obed", 70, 1)
                                $ Girl.Statup("Inbt", 70, 2)
                                $ Girl.RecentActions.append("has serum")
                        else:
                                if Girl is RogueX:
                                        ch_r "Я на это не поведусь, [Girl.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Как-будто я соглашусь, [Girl.Petname]."
                                elif Girl is EmmaX:
                                        ch_e "Ты, должно быть, шутишь, [Girl.Petname]."
                                elif Girl is LauraX:
                                        ch_l "Неа."
                                elif Girl is JeanX:
                                        ch_j "Нет, мне это не интересно."
                                elif Girl is StormX:
                                        ch_s "Я так не думаю."
                                elif Girl is JubesX:
                                        ch_v "Нет, спасибо. . ."
                                elif Girl is GwenX:
                                        ch_g "Я сейчас очень серьезна!"
                                elif Girl is BetsyX:
                                        ch_b "Это абсолютно невозможно!"
                                elif Girl is DoreenX:
                                        ch_d "Воу, какое безумие!"
                                elif Girl is WandaX:
                                        ch_w "Слишком выгодно для тебя. . ."
                                $ Count = 0

                "За порцию я беру $5.":
                            $ Line = "Пять"

                "За порцию я беру $10.":
                            $ Line = "Десять"

                "Неважно.":
                            if Girl is RogueX:
                                    ch_r "Ох, ладно. . ."
                            elif Girl is KittyX:
                                    ch_k "Эм, ладно. . ."
                            elif Girl is EmmaX:
                                    ch_e "Ладно. . ."
                            elif Girl is LauraX:
                                    ch_l "Ох, ладно. . ."
                            elif Girl is JeanX:
                                    ch_j "Лаааадно?"
                            elif Girl is StormX:
                                    ch_s "Хорошо?"
                            elif Girl is JubesX:
                                    ch_v "Лаааадно. . ."
                            elif Girl is GwenX:
                                    ch_g "Эм, ладно. . ."
                            elif Girl is BetsyX:
                                    ch_b "Неужели? . ."
                            elif Girl is DoreenX:
                                    ch_d "Эм. ладно. . ."
                            elif Girl is WandaX:
                                    ch_w "Ладно, как скажешь. . ."
                            $ Girl.Action = CountStore
                            return

            if Line == "Пять" or Line == "Десять":
                        #you've tried to charge for it. . .
                        $ Girl.FaceChange("angry")
                        $ Girl.Mouth = "surprised"
                        if Girl is RogueX:
                                if Girl.Chat[3]:
                                        if not Player.Male:
                                            ch_r "[Line] баксов, просто чтобы выпить твои соки?"
                                        else:
                                            ch_r "[Line] баксов, просто чтобы выпить твою сперму?"
                                elif Girl.Chat[2]:
                                        ch_r "[Line] баксов, ради этой сомнительной \"сыворотки\"?"
                                else:
                                        ch_r "[Line] баксов, только ради этой сыворотки?"
                        elif Girl is KittyX:
                                if Girl.Chat[3]:
                                        if not Player.Male:
                                            ch_k "[Line] баксов за полный рот соков?"
                                        else:
                                            ch_k "[Line] баксов за полный рот спермы?"
                                elif Girl.Chat[2]:
                                        ch_k "[Line] баксов, ради этой сомнительной \"сыворотки\"?"
                                else:
                                        ch_k "[Line] баксов, только ради этой сыворотки?"
                        elif Girl is EmmaX:
                                if Girl.Chat[3]:
                                        if not Player.Male:
                                            ch_e "[Line] долларов? Такова плата за теплые соки?"
                                        else:
                                            ch_e "[Line] долларов? Такова плата за теплую сперму?"
                                elif Girl.Chat[2]:
                                        ch_e "[Line] долларов, ради этой сомнительной \"сыворотки\"?"
                                else:
                                        ch_e "[Line] долларов, только ради этой подозрительной жидкости?"
                        elif Girl is LauraX:
                                if Girl.Chat[3]:
                                        if not Player.Male:
                                            ch_l "[Line] баксов за свежые соки?"
                                        else:
                                            ch_l "[Line] баксов за свежую сперму?"
                                elif Girl.Chat[2]:
                                        ch_l "[Line] баксов, ради этой сомнительной \"сыворотки\"?"
                                else:
                                        ch_l "[Line] баксов, только за это?"
                        elif Girl is JeanX:
                                ch_j "Давай-ка проясним."
                                $ Girl.Statup("Obed", 80, 1)
                                if Girl.Chat[3]:
                                        if not Player.Male:
                                            ch_j "[Line] баксов за соки?"
                                        else:
                                            ch_j "[Line] баксов за сперму?"
                                elif Girl.Chat[2]:
                                        ch_j "[Line] баксов, ради этой загадочной \"сыворотки\"?"
                                else:
                                        ch_j "[Line] баксов, только за эту хрень?"
                        elif Girl is StormX:
                                if Girl.Chat[3]:
                                        if not Player.Male:
                                            ch_s "[Line] долларов? Плата за свежие соки?"
                                        else:
                                            ch_s "[Line] долларов? Плата за свежую сперму?"
                                elif Girl.Chat[2]:
                                        ch_s "[Line] долларов, ради этой так называемой \"сыворотки\"?"
                                else:
                                        ch_s "[Line] долларов, за эту микстуру?"
                        elif Girl is JubesX:
                                if Girl.Chat[3]:
                                        if not Player.Male:
                                            ch_v "[Line] баксов наличными за соки?"
                                        else:
                                            ch_v "[Line] баксов наличными за сперму?"
                                elif Girl.Chat[2]:
                                        ch_v "[Line] баксов, за \"сыворотку\"?"
                                else:
                                        ch_v "[Line] баксов, за. . . что-то непонятное?"
                        elif Girl is GwenX:
                                if Girl.Chat[3]:
                                        if not Player.Male:
                                            ch_g "[Line] баксов? За бутылочку твоих соков?"
                                        else:
                                            ch_g "[Line] баксов? За бутылочку твоей спермы?"
                                elif Girl.Chat[2]:
                                        ch_g "[Line] баксов, за какую-то супер \"сыворотку\"?"
                                else:
                                        ch_g "[Line] баксов, за. . . какую-то супер-ультра-крутую-сыворотку?"
                        elif Girl is BetsyX:
                                if Girl.Chat[3]:
                                        if not Player.Male:
                                            ch_b "[Line] долларов, за бутылочку соков?"
                                        else:
                                            ch_b "[Line] долларов, за бутылочку спермы?"
                                elif Girl.Chat[2]:
                                        ch_b "[Line] долларов, за твою \"сыворотку\"?"
                                else:
                                        ch_b "[Line] долларов, только за эту твою \"сыворотку\"?"
                        elif Girl is DoreenX:
                                if Girl.Chat[3]:
                                        if not Player.Male:
                                            ch_d "[Line] баксов? Только за бутылочку твоих соков?"
                                        else:
                                            ch_d "[Line] баксов? Только за бутылочку твоей спермы?"
                                elif Girl.Chat[2]:
                                        ch_d "[Line] баксов, за одну бутылочку \"сыворотки\"?"
                                else:
                                        ch_d "[Line] баксов, и ты утверждаешь, что эта \"сыворотка\" якобы подействует?"
                        elif Girl is WandaX:
                                if Girl.Chat[3]:
                                        if not Player.Male:
                                            ch_w "[Line] баксов? За бутылочку твоих соков?"
                                        else:
                                            ch_w "[Line] баксов? За бутылочку твоей спермы?"
                                elif Girl.Chat[2]:
                                        ch_w "[Line] баксов, за всего одну бутылочку \"сыворотки\"?"
                                else:
                                        ch_w "[Line] баксов, когда даже не известно, работает ли твоя \"сыворотка\"?"
                        $ Girl.FaceChange()
                        $ Girl.Eyes = "side"
                        $ Girl.Statup("Love", 70, -3, 1)
                        $ Girl.Statup("Love", 200, -4)
                        call AnyLine(Girl,". . .")
                        $ Girl.FaceChange()
                        $ Girl.Brows = "sad"
                        if Line == "Десять":
                                $ Girl.Statup("Love", 70, -2, 1)
                                $ Girl.Statup("Love", 90, -10)
                        if Girl is BetsyX:
                                $ Girl.FaceChange("bemused")
                                $ Girl.Statup("Obed", 70, 2)
                                $ Girl.Statup("Inbt", 70, 2)
                                if not ApprovalCheck(Girl, 800, "LI"):
                                        $ Girl.Forced = 1
                                        $ MultiAction = 0
                                if Line == "Десять":
                                    $ Player.Cash += 10
                                else:
                                    $ Player.Cash += 5
                                ch_b "Что ж, не вижу причин для отказа. . ."
                                $ Girl.RecentActions.append("has serum")
                        elif Girl.Chat[2] and Line == "Десять" and Girl.Addict >= 75:
                                if Girl is RogueX:
                                        ch_r "Пяти уже мало! Ладно, держи, но ни пенни больше."
                                elif Girl is KittyX:
                                        ch_k "Пяти уже мало! Хорошо, пофиг, держи."
                                elif Girl is EmmaX:
                                        ch_e "Пяти тебе теперь мало? Ладно."
                                elif Girl is LauraX:
                                        ch_l "Да ты издеваешься. Ладно, десять так десять."
                                elif Girl is JeanX:
                                        $ Girl.Statup("Obed", 80, 2)
                                        ch_j "Серьезно? Десять баксов? . . "
                                        ch_j "Да пофиг, забирай."
                                elif Girl is StormX:
                                        ch_s "Не продолжай больше пользоваться ситуацией в своих интересах."
                                elif Girl is JubesX:
                                        ch_v "Становится слишком дорого. . ."
                                elif Girl is GwenX:
                                        ch_g "Это настоящий грабеж!"
                                elif Girl is DoreenX:
                                        ch_d "Я здесь не то чтобы купаюсь в деньгах. . ."
                                elif Girl is WandaX:
                                        ch_w "Я не получаю здесь настолько много. . ."
                                $ Girl.Statup("Obed", 50, 2)
                                $ Girl.Statup("Obed", 90, 3)
                                $ Girl.Statup("Inbt", 70, 2)
                                if not ApprovalCheck(Girl, 1200, "LI"):
                                        $ Girl.Forced = 1
                                        $ MultiAction = 0
                                $ Player.Cash += 10
                                $ Girl.RecentActions.append("has serum")
                        elif Girl.Chat[2] and Line == "Пять":
                                if Girl is RogueX:
                                        ch_r "Ладно, держи."
                                elif Girl is KittyX:
                                        ch_k "Ладно."
                                elif Girl is EmmaX:
                                        ch_e "Ох, хорошо."
                                elif Girl is LauraX:
                                        ch_l "Ну, держи."
                                elif Girl is JeanX:
                                        $ Girl.Statup("Obed", 80, 2)
                                        ch_j "Ладно, как скажешь."
                                elif Girl is StormX:
                                        ch_s "Ох, хорошо. . ."
                                elif Girl is JubesX:
                                        ch_v "Хм, ладно. . ."
                                elif Girl is GwenX:
                                        ch_g "Ладно. . . хорошо."
                                elif Girl is DoreenX:
                                        ch_d "Ладно, как скажешь. . ."
                                elif Girl is WandaX:
                                        ch_w "Ладно, хорошо. . ."
                                $ Girl.Statup("Obed", 50, 4)
                                $ Girl.Statup("Obed", 70, 2)
                                $ Girl.Statup("Inbt", 70, 4)
                                if not ApprovalCheck(Girl, 1200, "LI"):
                                        $ Girl.Forced = 1
                                        $ MultiAction = 0
                                $ Player.Cash += 5
                                $ Girl.RecentActions.append("has serum")
                        else:
                                if Girl is RogueX:
                                        ch_r "Ни за что, Я даже не знаю, сработает ли она."
                                elif Girl is KittyX:
                                        ch_k "Ни за что, она может даже не сработать!"
                                elif Girl is EmmaX:
                                        ch_e "Я не собираюсь платить за что-то настолько подозрительное."
                                elif Girl is LauraX:
                                        ch_l "Ни за что."
                                elif Girl is JeanX:
                                        ch_j "Нахер."
                                elif Girl is StormX:
                                        ch_s "Я не буду рисковать."
                                elif Girl is JubesX:
                                        ch_v "Неее. . ."
                                elif Girl is GwenX:
                                        ch_g "Выглядит подозрительно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Я. . . не могу позволить себе употреблять странные жидкости. . ."
                                elif Girl is WandaX:
                                        ch_w "Мне немного не хватает. . ."
            #end "charge for it"

            if "swallowed" in Girl.RecentActions:
                    $ Girl.Addict = 20 if Girl.Addict >= 20 else 0
                    if Girl is RogueX:
                            if Girl.Chat[3]:
                                    ch_r "Ну, думаю, самое то. . ."
                                    $ Girl.Action = CountStore
                                    return
                            else:
                                    ch_r "Это было. . . очень хорошо, а что насчет этой сыворотки?"
                    elif Girl is KittyX:
                            if Girl.Chat[3]:
                                    ch_k "Ммм, как вкусно. . ."
                                    $ Girl.Action = CountStore
                                    return
                            else:
                                    ch_k "Это было. . . хорошо, но как насчет этой сыворотки?"
                    elif Girl is EmmaX:
                            if Girl.Chat[3]:
                                    ch_e "Вполне удовлетворительно. . ."
                                    $ Girl.Action = CountStore
                                    return
                            else:
                                    ch_e "Теперь, когда мы разобрались с оплатой, что насчет этой \"сыворотки?\""
                    elif Girl is LauraX:
                            if Girl.Chat[3]:
                                    ch_l "Неплохо. . ."
                                    $ Girl.Action = CountStore
                                    return
                            else:
                                    if not Player.Male:
                                        ch_l "Ладно, ты говорила о какой-то \"сыворотке?\""
                                    else:
                                        ch_l "Ладно, ты говорил о какой-то \"сыворотке?\""
                    elif Girl is JeanX:
                            if Girl.Chat[3]:
                                    ch_j "Это было очень даже вкусно. . ."
                                    $ Girl.Action = CountStore
                                    return
                            else:
                                    ch_j "Ладно, так что насчет этой \"сыворотки?\""
                    elif Girl is StormX:
                            if Girl.Chat[3]:
                                    ch_s "Этого должно хватить. . ."
                                    $ Girl.Action = CountStore
                                    return
                            else:
                                    ch_s "Ладно, что насчет \"сыворотки?\""
                    elif Girl is JubesX:
                            if Girl.Chat[3]:
                                    ch_v "Ммммм. . ."
                                    ch_v "Ммммм!!"
                                    $ Girl.Action = CountStore
                                    return
                            else:
                                    ch_v "Ммммм. . ."
                                    ch_v "Эм, а как насчет той сыворотки?"
                    elif Girl is GwenX:
                            if Girl.Chat[3]:
                                    ch_g "Хмм, какая нежная структура. . ."
                                    $ Girl.Action = CountStore
                                    return
                            else:
                                    ch_g "Ладно, с этим мы разобрались, где эта \"сыворотка?\""
                    elif Girl is BetsyX:
                            if Girl.Chat[3]:
                                    ch_b "Восхитительно. . ."
                                    $ Girl.Action = CountStore
                                    return
                            else:
                                    ch_b "Восхитительно, а что за \"сыворотка\"?"
                    elif Girl is DoreenX:
                            if Girl.Chat[3]:
                                    ch_d "Хм, вкусно. . ."
                                    $ Girl.Action = CountStore
                                    return
                            else:
                                    ch_d "Ладно, что там с \"сывороткой\"?"
                    elif Girl is WandaX:
                            if Girl.Chat[3]:
                                    ch_w "Хм, вкусно. . ."
                                    $ Girl.Action = CountStore
                                    return
                            else:
                                    ch_w "Ладно, что теперь насчет этой \"сыворотки?\""

            elif "hand" in Girl.RecentActions or "blow" in Girl.RecentActions or "finger" in Girl.RecentActions or "cun" in Girl.RecentActions:
                            #not swallowed
                            if Girl is RogueX:
                                    ch_r "Ладно, думаю, со своей задачей я разобралась, а теперь как насчет сыворотки?"
                            elif Girl is KittyX:
                                    ch_k "Ладно, думаю, я свое отработала, а теперь как насчет этой сыворотки?"
                            elif Girl is EmmaX:
                                    ch_e "Думаю, этого должно быть достаточно, а как насчет этой \"сыворотки\""
                            elif Girl is LauraX:
                                    ch_l "Я свое выполнила, как насчет \"сыворотки?\""
                            elif Girl is JeanX:
                                    ch_j "Ладно, давай эту свою сыворотку."
                            elif Girl is StormX:
                                    ch_s "Доволен? Теперь создай эту \"сыворотку.\""
                            elif Girl is JubesX:
                                    ch_v "Нуу? Давай ее сюда."
                            elif Girl is GwenX:
                                    ch_g "Ладно, думаю, я заслужила свою \"сыворотку.\""
                            elif Girl is BetsyX:
                                    ch_b "Я считаю, что этого достаточно для получения \"сыворотки.\""
                            elif Girl is DoreenX:
                                    ch_d "Ладно, думаю, теперь я заслужила свою \"сыворотку\". . ."
                            elif Girl is WandaX:
                                    ch_w "Ладно, этого должно быть достаточно. . ."

            if "has serum" in Girl.RecentActions:
                            #if she got the serum, drop out of the loop
                            $ Count = 0
            elif Count == 1:
                            if Girl is RogueX:
                                    ch_r "Давай серьезней, у меня не так много времени."
                            elif Girl is KittyX:
                                    ch_k "Есть что-то еще, чего ты хочешь?"
                            elif Girl is EmmaX:
                                    if not Player.Male:
                                        ch_e "Мне нужно, чтобы ты сделала разумное предложение. . ."
                                    else:
                                        ch_e "Мне нужно, чтобы ты сделал разумное предложение. . ."
                            elif Girl is LauraX:
                                    ch_l "Эй, будь серьезней."
                            elif Girl is JeanX:
                                    ch_j "Давай, чего ты хочешь?"
                            elif Girl is StormX:
                                    ch_s "Постарайся быть серьезней."
                            elif Girl is JubesX:
                                    ch_v "Этого не случится. . ."
                            elif Girl is GwenX:
                                    ch_g "Ни за что."
                            elif Girl is BetsyX:
                                    ch_b "Ты должно быть шутишь."
                            elif Girl is DoreenX:
                                    ch_d "Я пытаюсь быть благоразумной. . ."
                            elif Girl is WandaX:
                                    ch_w "Слушай, я же пытаюсь с тобой договориться. . ."
            elif Count:
                            if Girl is RogueX:
                                    ch_r "Ну же, что еще тебе нужно?"
                            elif Girl is KittyX:
                                    ch_k "Ну же, что-нибудь еще?"
                            elif Girl is EmmaX:
                                    ch_e "Я постараюсь быть уступчивой. . ."
                            elif Girl is LauraX:
                                    ch_l "Эй, дай мне идею получше."
                            elif Girl is JeanX:
                                    ch_j "Мне нужно что-нибудь интересное. . ."
                            elif Girl is StormX:
                                    ch_s "Я надеюсь, мы сможем прийти к соглашению."
                            elif Girl is JubesX:
                                    ch_v "Дай мне что-нибудь, с чем можно поработать. . ."
                            elif Girl is GwenX:
                                    ch_g "Ситуация становится глупой."
                            elif Girl is BetsyX:
                                    ch_b "Ох, будь серьезней. . ."
                            elif Girl is DoreenX:
                                    ch_d "Чего ты упираешься. . ?"
                            elif Girl is WandaX:
                                    ch_w "Дай мне передохнуть. . ."
            #end while loop


        if "has serum" in Girl.RecentActions:
                #falls through if she got the serum
                if not Player.Semen:
                        ch_p "У меня, как бы это сказать. . . ее сейчас нет в наличие, извини. . ."
                        $ Girl.FaceChange("angry",1)
                        $ Girl.Statup("Love", 80, -5)
                        $ Girl.Statup("Obed", 50, -5)
                        $ Girl.Statup("Obed", 80, 2)
                        $ Girl.Statup("Inbt", 80, -2)
                        if Line == "Десять":
                                $ Player.Cash -= 10
                        elif Line == "Пять":
                                $ Player.Cash -= 5
                        call AnyLine(Girl,"Гррр. . .")
                        $ Line = 0
                        $ Girl.Action = CountStore
                        return
                "Вы на минуту выходите из комнаты. . ."
                $ Player.Semen -= 1
                "Вы протягиваете ей маленькую бутылочку, наполненную \"сывороткой.\""
                "Она сперва открывает бутылочку, а затем слегка нюхает."

                if Girl.Chat[3]:
                        if Girl.Swallow < 10:
                            "Она нерешительно смотрит на вас, но вскоре выпивает ее и вытирает губы."
                            $ Girl.Statup("Inbt", 70, 2)
                        else:
                            "Она выпивает ее залпом и вытирает губы."
                            $ Girl.Statup("Inbt", 70, 1)

                elif Girl.Swallow <= 5 and Girl in (RogueX,KittyX,GwenX,DoreenX):
                        "Затем она выпивает ее залпом и вытирает губы."
                        if Girl is RogueX:
                                ch_r "Фух, тяжело заходит. . ."
                        elif Girl is KittyX:
                                ch_k "Иу, она очень густая. . ."
                        elif Girl is GwenX:
                                ch_g "Оххххххх. . ."
                        elif Girl is DoreenX:
                                ch_d "Оох, густая. . ."
                else:
                        $ Girl.FaceChange("perplexed")
                        "Она сначала выглядит немного растерянной, но потом улыбается, выпивает ее и вытирает губы."
                        $ Girl.Statup("Inbt", 50, 1)
                        $ Girl.Statup("Inbt", 70, 2)
                        $ Girl.FaceChange("surprised",2)
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Это были твои соки, да? Могла бы сразу сказать."
                                    $ Girl.FaceChange("smile",1)
                                    ch_r "Я знаю, как хорошо они помогают."
                                else:
                                    ch_r "Это была твоя сперма, да? Мог бы сразу сказать."
                                    $ Girl.FaceChange("smile",1)
                                    ch_r "Я знаю, как хорошо она помогает."
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Эй, это была просто сперма!"
                                    $ Girl.FaceChange("smile",1)
                                    ch_k "Ну, я думаю, она помогает."
                                else:
                                    ch_k "Эй, это были просто соки!"
                                    $ Girl.FaceChange("smile",1)
                                    ch_k "Ну, я думаю, они помогают."
                        elif Girl is EmmaX:
                                $ Girl.FaceChange("sly",1)
                                ch_e "Я должна была догадаться, что ты не какой-то там химик-уникум."
                                ch_e "Используешь собственные жидкости в качестве панацеи?"
                                ch_e "Тем не менее, я полагаю, это удобная альтернатива."
                        elif Girl is LauraX:
                                if not Player.Male:
                                    ch_l "Ох, это были просто соки."
                                    $ Girl.FaceChange("smile",1)
                                    ch_l "Теперь пазл сложился."
                                else:
                                    ch_l "Ох, это была просто сперма."
                                    $ Girl.FaceChange("smile",1)
                                    ch_l "Теперь пазл сложился."
                        elif Girl is JeanX:
                                $ Girl.Statup("Love", 80, 3)
                                $ Girl.Statup("Obed", 50, 3)
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.Statup("Inbt", 80, 3)
                                $ Girl.FaceChange("normal",1)
                                if not Player.Male:
                                    ch_j "Ох, \"сыворотка\" это соки."
                                    ch_j "Я в шоке."
                                    ch_j "Серьезно."
                                else:
                                    ch_j "Ох, \"сыворотка\" это сперма."
                                    ch_j "Я в шоке."
                                    ch_j "Серьезно."
                        elif Girl is StormX:
                                $ Girl.FaceChange("smile",1)
                                if not Player.Male:
                                    ch_s "Что ж. . . похоже, ты мне разыгрываешь."
                                    ch_s "Это соки, не так ли? Твои?"
                                else:
                                    ch_s "Что ж. . . похоже, ты мне разыгрываешь."
                                    ch_s "Это сперма, не так ли? Твоя?"
                        elif Girl is JubesX:
                                if not Player.Male:
                                    ch_v "О, ты только что разлила свои соки по баночкам."
                                    ch_v "В этом есть смысл."
                                else:
                                    ch_v "О, ты только что разлил свою сперму по баночкам."
                                    ch_v "В этом есть смысл."
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Оооооох. . ."
                                    ch_g "Ты просто налила соки в баночку."
                                    $ Girl.FaceChange("sly",1)
                                    ch_g "Я должна была догадаться, что ты не какая-то супер-пупер-ученая."
                                    ch_g "Хотя, они довольно распространены. . ."
                                    ch_g "Но, думаю, они помогают довольно хорошо. . ."
                                else:
                                    ch_g "Оооооох. . ."
                                    ch_g "Ты просто налил сперму в баночку."
                                    $ Girl.FaceChange("sly",1)
                                    ch_g "Я должна была догадаться, что ты не какой-то супер-пупер-ученый."
                                    ch_g "Хотя, они довольно распространены. . ."
                                    ch_g "Но, думаю, она помогает довольно хорошо. . ."
                        elif Girl is BetsyX:
                                if not Player.Male:
                                    ch_b "На вкус очень похожа на твои соки. . ."
                                    $ Girl.FaceChange("sly",1)
                                    ch_b "Попробуешь, м?"
                                    $ Girl.FaceChange("surprised",2)
                                    ch_b "Нет, подожди. . . это и есть они!"
                                    $ Girl.FaceChange("smile",1)
                                    ch_b "Мелкая мерзавка!"
                                    ch_b "Хотя довольно вкусно. . ."
                                else:
                                    ch_b "На вкус очень похожа на твою сперму. . ."
                                    $ Girl.FaceChange("sly",1)
                                    ch_b "Попробуешь, м?"
                                    $ Girl.FaceChange("surprised",2)
                                    ch_b "Нет, подожди. . . это и есть она!"
                                    $ Girl.FaceChange("smile",1)
                                    ch_b "Мелкий мерзавец!"
                                    ch_b "Хотя довольно вкусно. . ."
                        elif Girl is DoreenX:
                                $ Girl.FaceChange("surprised",1)
                                if not Player.Male:
                                    ch_d ". . . Подожди-ка, сейчас попробуем!"
                                    $ Girl.FaceChange("angry",2)
                                    ch_d "На вкус как и твои соки!"
                                    ch_d "Это ведь они, да?!"
                                else:
                                    ch_d ". . . Подожди-ка, сейчас попробуем!"
                                    $ Girl.FaceChange("angry",2)
                                    ch_d "На вкус как и твоя сперма!"
                                    ch_d "Это ведь она, да?!"
                        elif Girl is WandaX:
                                ch_w "Слушай. . ."
                                if not Player.Male:
                                    ch_w "Это всего лишь твои соки, я ведь права?!"
                                else:
                                    ch_w "Это всего лишь твоя сперма, я ведь права?!"
                                ch_w "Я всегда узнаю этот вкус. . ."
                        $ Girl.FaceChange("smile",1)
                        menu:
                            extend ""
                            "Эм, да?":
                                    $ Girl.FaceChange("confused")
                                    $ Girl.Mouth = "lipbite"
                            "Конечно нет!":
                                    $ Girl.FaceChange("confused")
                                    $ Girl.Mouth = "smile"
                        "Она строго смотрит на вас, но потом проглатывает и вытирает губы."
                        if Girl is RogueX:
                                if not Player.Male:
                                    ch_r "Фух, все еще не могу привыкнуть к ​​этому вкусу, ты должна была просто сказать мне."
                                else:
                                    ch_r "Фух, все еще не могу привыкнуть к ​​этому вкусу, ты должен был просто сказать мне."
                        elif Girl is KittyX:
                                if not Player.Male:
                                    ch_k "Фу, гадость. . . Ты могла бы просто сказать мне."
                                else:
                                    ch_k "Фу, гадость. . . Ты мог бы просто сказать мне."
                        elif Girl is EmmaX:
                                if not Player.Male:
                                    ch_e "Что ж, это не первый раз, когда я глотаю соки."
                                else:
                                    ch_e "Что ж, это не первый раз, когда я глотаю сперму."
                        elif Girl is LauraX:
                                if not Player.Male:
                                    ch_l "Ну, думаю, они помогают. . ."
                                else:
                                    ch_l "Ну, думаю, она помогает. . ."
                        elif Girl is JeanX:
                                $ Girl.Statup("Love", 80, 2)
                                ch_j "Мне все равно что это."
                        elif Girl is StormX:
                                if not Player.Male:
                                    ch_s "Пожалуй, пока они помогают. . ."
                                else:
                                    ch_s "Пожалуй, пока она помогает. . ."
                        elif Girl is JubesX:
                                ch_v "Ох, всенормально, очень дажевкусно."
                        elif Girl is GwenX:
                                ch_g "Я зла на тебя не держу. . ."
                        elif Girl is BetsyX:
                                ch_b "Пожалуй, каждый делает то, что должен. . ."
                        elif Girl is DoreenX:
                                $ Girl.FaceChange("smile",1)
                                ch_d ". . . Думаю, в этом есть смысл. . ."
                        elif Girl is WandaX:
                                ch_w "В этом есть смысл. . ."
                        $ Girl.Chat[3] = 1
                $ Girl.Eyes = "closed"
                $ Girl.Brows = "sad"
                $ Girl.Mouth = "smile"
                "[Girl.Name] содрогается в экстазе."
                $ Girl.FaceChange()
                if Girl.Chat[3]:
                        if Girl is RogueX:
                                ch_r "Хм, даже зная, что это за штука, она похоже, помогает."
                        elif Girl is KittyX:
                                ch_k "Все еще немного странно, но она помогает."
                        elif Girl is EmmaX:
                                ch_e "Я все еще поражена тем, насколько она эффективна."
                        elif Girl is LauraX:
                                ch_l "Ах, так-то лучше."
                        elif Girl is JeanX:
                                if not Player.Male:
                                    ch_j "Я должна сказать, твои соки прямо то, что нужно. . ."
                                else:
                                    ch_j "Я должна сказать, твоя сперма прямо то, что нужно. . ."
                        elif Girl is StormX:
                                ch_s "У тебя уникальный вкус. . ."
                        elif Girl is JubesX:
                                ch_v "Это было здорово, спасибо."
                        elif Girl is GwenX:
                                ch_g "Помогает довольно хорошо. . ."
                        elif Girl is BetsyX:
                                ch_b "Она весьма эффективна. . ."
                        elif Girl is DoreenX:
                                ch_d ". . . она действительно сняла напряжение. . ."
                        elif Girl is WandaX:
                                ch_w "Она очень успокаивает. . ."
                        $ Girl.RecentActions.append("swallowed")
                        $ Girl.DailyActions.append("swallowed")
                else:
                        if Girl is RogueX:
                                ch_r ". . . она действительно помогает. Спасибо."
                        elif Girl is KittyX:
                                ch_k ". . . но она и правда справляется. Спасибо."
                        elif Girl is JeanX:
                                ch_j "Чем бы это ни было, оно, похоже, помогает."
                        elif Girl is GwenX:
                                ch_g "Хм, помогает довольно хорошо. . ."
                        elif Girl is DoreenX:
                                ch_d ". . . она действительно сняла напряжение. . ."
                        elif Girl is WandaX:
                                ch_w "Она очень успокаивает. . ."
                $ Girl.RecentActions.remove("has serum")
                $ Girl.RecentActions.append("serum")
                $ Girl.DailyActions.append("serum")
                $ Girl.Addict = 20 if Girl.Addict >= 20 else 0
                $ Girl.Addictionrate += 2
                if "addictive" in Player.Traits:
                        $ Girl.Addictionrate += 2
                $ Girl.Chat[2] += 1
        else:
                if Girl is RogueX:
                        ch_r "Жаль, что мы не смогли договориться. . ."
                elif Girl is KittyX:
                        if not Player.Male:
                            ch_k "Я бы хотела, чтобы ты была более уступчивой. . ."
                        else:
                            ch_k "Я бы хотела, чтобы ты был более уступчивым. . ."
                elif Girl is EmmaX:
                        ch_e "С тобой тяжело торговаться. . ."
                elif Girl is LauraX:
                        ch_l "Ну, все прошло как-то не очень. . ."
                elif Girl is JeanX:
                        ch_j "Ты не знаешь, как вести переговоры, так же хорошо, как я."
                        ch_j "Я же, все-таки, гений."
                elif Girl is StormX:
                        ch_s "Мы должны были договориться."
                elif Girl is JubesX:
                        ch_v "Нам нужно что-то придумать, правда?"
                elif Girl is GwenX:
                        ch_g "Мне нужен лучший вариант. . ."
                elif Girl is BetsyX:
                        ch_b "Очень жаль, что мы не смогли прийти к соглашению. . ."
                elif Girl is DoreenX:
                        ch_d ". . . извини, что мы не смогли договориться. . ."
                elif Girl is WandaX:
                        ch_w "Я думала, мы сможем договориться. . ."
                $ Girl.RecentActions.append("no serum")
        $ Girl.Action = CountStore
        return
# End Addiction / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
