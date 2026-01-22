# start EmmaMeet //////////////////////////////////////////////////////////
# Check  #Emma_Update   to see what needs fixing still
label EmmaMeet:
    $ bg_current = "bg classroom"
    $ EmmaX.OutfitDay = "casual1"
    $ EmmaX.Outfit = "casual1"
    $ EmmaX.OutfitChange("casual1")
    call CleartheRoom(EmmaX,0,1)
    $ EmmaX.Loc = "bg emma"
    $ EmmaX.Love = 300
    $ EmmaX.Obed = 0
    $ EmmaX.Inbt = 200
    call Shift_Focus(EmmaX)
    call Set_The_Scene
    $ EmmaX.SpriteLoc = StageRight
    call LastNamer
    $ EmmaX.Petnames.append(_return)
    $ EmmaX.Petname = _return

    "Вы входите в аудиторию и присаживаетесь."
    "Раздается звонок на занятие, но профессор МакКой так и не приходит."
    "Вместо него в комнату входит странная женщина и царственным шагом направляется к подиуму."
    $ EmmaX.FaceChange("normal")
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) with easeinright
    $ EmmaX.Loc = "bg classroom"
    $ EmmaX.ArmPose = 1
    ch_u "Здравствуйте, студенты. Меня зовут Эмма Фрост, меня пригласили преподавать этот предмет."
    $ EmmaX.Name = "Эмма Фрост"
    $ EmmaX.Name_rod = "Эммы Фрост"
    $ EmmaX.Name_dat = "Эмме Фрост"
    $ EmmaX.Name_vin = "Эмму Фрост"
    $ EmmaX.Name_tvo = "Эммой Фрост"
    $ EmmaX.Name_pre = "Эмме Фрост"
    $ EmmaX.Petname = Player.Name
    $ EmmaX.Petname_rod = Player.Name_rod
    $ EmmaX.Petname_dat = Player.Name_dat
    $ EmmaX.Petname_vin = Player.Name_vin
    $ EmmaX.Petname_tvo = Player.Name_tvo
    $ EmmaX.Petname_pre = Player.Name_pre
    ch_e "Надеюсь, что за время моего пребывания здесь вы продемонстрируете таланты и трудолюбие, достойные моего уважения."
    "Она оглядывает комнату, проходя мимо каждого студента."
    $ EmmaX.FaceChange("surprised")
    pause 1
    $ EmmaX.FaceChange("sly",Mouth="sad")
    $ EmmaX.Statup("Love", 90, -10)
    $ EmmaX.Lust += 5
    "Когда ее глаза находят вас, они мгновенно расширяются, но вскоре сужаются."
    $ EmmaX.FaceChange("sly")
    ch_e "Хорошо, начнем наше занятие."
    $ EmmaX.FaceChange("normal")
    "Сегодняшнее занятие довольно простое: лекция по ее специализации - психологии и литературе."
    $ EmmaX.Lust += 5
    "Она задает много вопросов студентам и не раз обращается к вам. Вы замечаете, что она поглядывает в вашу сторону, пока другие студенты отвечают."
    $ EmmaX.Lust += 5
    call Wait
    call CleartheRoom(EmmaX,0,1)
    $ EmmaX.Loc = "bg classroom"
    call Set_The_Scene
    ch_e "Хорошо, студенты, занятие окончено."
    ch_e "[EmmaX.Petname], можешь задержаться на минутку? Мне нужно с тобой поговорить."
    menu:
        extend ""
        "Да?":
                $ EmmaX.Statup("Love", 70, 10)
                $ EmmaX.FaceChange("normal")
        "У меня дела.":
                $ EmmaX.Statup("Love", 70, -15)
                $ EmmaX.Statup("Obed", 80, 10)
                $ EmmaX.FaceChange("angry")
                ch_e "[Player.Name], тебе не стоит так вести себя со мной."
                "Она встает в дверной проем, не давая вам уйти."
        "Для такого сексуального преподавателя у меня всегда найдется время.":
                $ EmmaX.Statup("Love", 70, -5)
                $ EmmaX.Statup("Obed", 80, 5)
                $ EmmaX.FaceChange("angry",1, Mouth="smirk")
                ch_e "Твое замечание довольно. . . неприемлемо."
                $ EmmaX.FaceChange("bemused", Mouth="smile")
                $ EmmaX.Statup("Love", 70, 20)
                $ EmmaX.Statup("Lust", 50, 5)
                $ EmmaX.Statup("Inbt", 25, 15)
                ch_e "Но я не могу сердиться на тебя из-за этого."

    ch_e "Я слышала о тебе от профессора Ксавье и. . . других."

    if Player.Rep <= 200:
        $ EmmaX.Statup("Obed", 80, 10)
        $ EmmaX.Statup("Inbt", 90, 15)
        $ EmmaX.Statup("Lust", 50, 5)
        $ EmmaX.FaceChange("angry", Brows="confused")
        ch_e "У тебя очень плохая репутация. . ."
    elif Player.Rep < 600:
        $ EmmaX.Statup("Obed", 80, 5)
        $ EmmaX.Statup("Inbt", 90, 5)
        $ EmmaX.Statup("Lust", 50, 5)
        $ EmmaX.FaceChange("sly")
        ch_e "У тебя неплохая репутация в кампусе. . ."
    else:
        $ EmmaX.FaceChange("smile")
        ch_e "You have managed a reasonable reputation. . ."

    if TotalSEXP >= 110 or (len(Player.Harem) >= 2 and "Historia" not in Player.Traits):
        $ EmmaX.Statup("Love", 70, 5)
        $ EmmaX.Statup("Obed", 80, 10)
        $ EmmaX.Statup("Inbt", 200, 10)
        $ EmmaX.Statup("Lust", 50, 5)
        $ EmmaX.FaceChange("sly")
        ch_e "также за тобой числится ряд любовных побед. . ."
    elif TotalSEXP >= 60:
        $ EmmaX.Statup("Love", 70, 5)
        $ EmmaX.Statup("Obed", 80, 5)
        $ EmmaX.Statup("Inbt", 200, 5)
        $ EmmaX.Statup("Lust", 50, 2)
        $ EmmaX.FaceChange("smile")
        ch_e "и, конечно, не обошлось без романтических интрижек. . ."
    else:
        $ EmmaX.FaceChange("smile", Brows="confused")
        $ EmmaX.AddWord(1,0,0,0,"loser") #adds "word" to Recent
        ch_e "однако я почти ничего не слышала о твоей личной жизни. . ."

    if Player.Lvl >= 7:
        $ EmmaX.Statup("Love", 70, 5)
        $ EmmaX.Statup("Obed", 80, 5)
        $ EmmaX.FaceChange("smile")
        ch_e "но у тебя отличные оценки."
    elif Player.Lvl >= 3:
        $ EmmaX.FaceChange("normal", Brows="confused")
        ch_e "но твои достижения в учебе могли бы быть получше."
    else:
        $ EmmaX.Statup("Love", 70, -5)
        $ EmmaX.Statup("Lust", 10, -5, 1)
        $ EmmaX.FaceChange("normal", Brows="sad")
        $ EmmaX.AddWord(1,0,0,0,"idiot") #adds "word" to Recent
        ch_e "но вот с учебой у тебя не все гладко."

    $ EmmaX.FaceChange("normal", Eyes="side")
    if not Player.Male:
        ch_e "Ладно, отбросим формальности, ты меня заинтересовала. . ."
    else:
        ch_e "Ладно, отбросим формальности, ты меня заинтересовал. . ."
    $ EmmaX.FaceChange("sly")
    ch_e "так как я не могу тебя \"прочитать\"."
    $ EmmaX.FaceChange("sly", Mouth="normal")
    ch_e "Моя способность - телепатия, так же, как у профессора Ксавье."
    ch_e "Я привыкла знать, что думают окружающие."
    $ EmmaX.FaceChange("bemused", Eyes="side")
    ch_e "С тобой. . . Я не могу этого сделать, что представляет собой интересный. . ."
    $ EmmaX.FaceChange("sly")
    ch_e "вызов. . ."
    menu:
        extend ""
        "Я вас поняла." if not Player.Male:
                $ EmmaX.Statup("Love", 70, 5)
                $ EmmaX.Statup("Inbt", 200, 5)
                $ EmmaX.FaceChange("normal")
                ch_e "Хмм, да."
        "Я вас понял." if Player.Male:
                $ EmmaX.Statup("Love", 70, 5)
                $ EmmaX.Statup("Inbt", 200, 5)
                $ EmmaX.FaceChange("normal")
                ch_e "Хмм, да."
        "Эм. . .":
                $ EmmaX.Statup("Love", 70, -1)
                $ EmmaX.Statup("Obed", 80, -1)
                $ EmmaX.FaceChange("confused", Mouth="normal")
                ch_e ". . . да."
                $ EmmaX.FaceChange("normal")
        "Выходит, вы не знаете о чем я сейчас думаю?":
                $ EmmaX.Statup("Obed", 80, 5)
                $ EmmaX.FaceChange("bemused")
                if Player.Male:
                        pause 0.5
                        $ EmmaX.FaceChange("bemused", Eyes="down")
                        "Ее взгляд устремляется вниз."
                        $ EmmaX.FaceChange("sly")
                        $ EmmaX.Statup("Love", 70, 10)
                        $ EmmaX.Statup("Inbt", 200, 10)
                        $ EmmaX.Statup("Lust", 50, 15)
                        ch_e "Я не могу прочитать твои мысли, но я не слепая, [EmmaX.Petname]."
                ch_e "Представляю, что может быть сейчас у тебя голове. . ."
    ch_e "В любом случае, думаю, нам необходимо немного пообщаться."
    ch_e "Я бы хотела выделить на тебя отдельный проект, чтобы лучше изучить этот феномен."
    menu:
        extend ""
        "Я не против.":
                $ EmmaX.Statup("Love", 70, 5)
                $ EmmaX.Statup("Inbt", 200, 5)
                $ EmmaX.FaceChange("smile")
                ch_e "Отлично, буду с нетерпением этого ждать."
        "Сомневаюсь, что вам стоит ставить опыты над со своими студентами.":
                $ EmmaX.Statup("Love", 70, -5)
                $ EmmaX.FaceChange("normal", Mouth="sad")
                ch_e "Тебе не о чем беспокоиться."
                $ EmmaX.FaceChange("sly")
                ch_e "Я буду. . . нежной."
        "Я не против, если для этого нужно будет проводить больше времени с вами. . .":
                if ApprovalCheck(EmmaX, 295, "L"):
                    $ EmmaX.Statup("Inbt", 200, 5)
                    $ EmmaX.Statup("Lust", 50, 5)
                    $ EmmaX.FaceChange("sly")
                    ch_e "О, уверена, мы будем проводить очень много времени вместе. . ."
                else:
                    $ EmmaX.FaceChange("angry")
                    ch_e "Мне придется на это пойти, как мне это не было бы неприятно. . ."
                    $ EmmaX.FaceChange("normal")
        "Что я с этого получу?":
                if not ApprovalCheck(EmmaX, 290, "L"):
                    $ EmmaX.Statup("Love", 70, -5)
                    $ EmmaX.Statup("Obed", 80, 5)
                    $ EmmaX.Statup("Inbt", 200, 5)
                    $ EmmaX.FaceChange("angry")
                    ch_e "У тебя появится шанс закончить мой курс, [EmmaX.Petname]."
                    $ EmmaX.FaceChange("normal")
                else:
                    if EmmaX.Obed > 0:
                        $ EmmaX.FaceChange("confused", Mouth="smirk")
                        if not Player.Male:
                            ch_e "А что бы ты сама -хотела- \"получить?\""
                        else:
                            ch_e "А что бы ты сам -хотел- \"получить?\""
                        menu:
                            extend ""
                            "Радость от помощи вашему \"исследованию\". . .":
                                    $ EmmaX.Statup("Love", 70, 10)
                                    $ EmmaX.Statup("Obed", 80, -5)
                                    $ EmmaX.FaceChange("smile")
                                    ch_e "Мне нравится такой ответ."
                            "Если мы будем больше времени проводить вместе, меня это устроит. . .":
                                    $ EmmaX.Statup("Love", 70, 5)
                                    $ EmmaX.Statup("Obed", 80, 5)
                                    $ EmmaX.Statup("Lust", 20, 5)
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "Можешь даже не беспокоиться об этом."
                            "Поцелуй?":
                                    $ EmmaX.Statup("Love", 70, -5)
                                    $ EmmaX.Statup("Obed", 80, 10)
                                    $ EmmaX.FaceChange("surprised",1, Mouth="surprised")
                                    ch_e "[EmmaX.Petname], это невозможно!"
                                    $ EmmaX.FaceChange("sadside",0,Brows="angry")
                                    ch_e "Я бы -никогда- даже не подумала совершить такое со студентом."
                                    if ApprovalCheck(EmmaX, 220, "I"):
                                        $ EmmaX.FaceChange("sly",1)
                                        $ EmmaX.Statup("Love", 70, 5)
                                        $ EmmaX.Statup("Obed", 80, 5)
                                        $ EmmaX.Statup("Inbt", 200, 5)
                                        $ EmmaX.Statup("Lust", 50, 5)
                                        ch_e ". . .никогда. . ."
                            "Думаю, вы знаете, чего я хочу. . .":
                                    $ EmmaX.Statup("Obed", 80, 5)
                                    $ EmmaX.Statup("Lust", 50, 5)
                                    $ EmmaX.FaceChange("sly",Brows="angry")
                                    ch_e "Да, могу представить. . ."
                                    if ApprovalCheck(EmmaX, 220, "I"):
                                        $ EmmaX.FaceChange("sly",1)
                                        $ EmmaX.Statup("Love", 70, 5)
                                        $ EmmaX.Statup("Obed", 80, 5)
                                        $ EmmaX.Statup("Inbt", 200, 10)
                                        $ EmmaX.Statup("Lust", 50, 5)
                                        ch_e "И мы, возможно, сможем прийти к некому \"взаимовыгодному\" соглашению."
                                    else:
                                        $ EmmaX.FaceChange("bemused",0)
                                        $ EmmaX.Statup("Love", 70, -5)
                                        ch_e "Но главное - проверить мои предположения."
                    else: #if 0 Obedience
                        $ EmmaX.FaceChange("normal")
                        ch_e "Удовольствие от помощи моему. . . исследованию."
                        if ApprovalCheck(EmmaX, 300, "L"):
                            $ EmmaX.FaceChange("sly")
                            $ EmmaX.Statup("Obed", 80, 5)
                            $ EmmaX.Statup("Inbt", 200, 5)
                            $ EmmaX.Statup("Lust", 50, 5)
                            ch_e "-и, возможно, если ты будешь хорошо себя вести, что-нибудь еще. . ."
                        else:
                            ch_e "-и ничего больше."

    $ EmmaX.FaceChange("normal",0)
    ch_e "Что ж, занятие окончено, но мне нужно еще закончить кое-какую бумажную работу, так что увидимся. . ."
    ch_e ". . . позже. . ."
    hide Emma_Sprite with easeoutright
    "Она выходит из комнаты и удаляется по коридору."
    $ EmmaX.Loc = "bg emma"
    if EmmaX in Present:
            $ Present.remove(EmmaX)
    $ EmmaX.History.append("met")
    $ Player.AddWord(1,0,"Intro",0,0) #adds tag to Daily
    $ ActiveGirls.append(EmmaX) if EmmaX not in ActiveGirls else ActiveGirls
    $ Round -= 10
    return

# end EmmaMeet //////////////////////////////////////////////////////////


# Event Emma_Teacher_Caught /////////////////////////////////////////////////////
label Emma_Teacher_Caught(Girl = 0):
    #add this scene for when Emma is a teacher, and catches one of the girls fucking around in class.
    #add options for getting away with it
    if  "noticed " + Girl.Tag in EmmaX.RecentActions:
            return

    if "EmmaStorm" in EmmaX.History:
        if ApprovalCheck(EmmaX, 1200) and ApprovalCheck(StormX, 1200): #and "EmmaStormQueue" not in EmmaX.Traits:
            $ EmmaX.AddWord(1,0,0,"EmmaStormQueue") #adds to Traits, queuing up a redo of event
    elif len(Rules) >= 3 and "classcaught" in EmmaX.History and "met" in StormX.History and (EmmaX.SEXP >= 15 or StormX.SEXP >= 15):
            $ EmmaX.AddWord(1,0,0,"EmmaStormQueue") #adds to Traits, queuing up a redo of event
    if ApprovalCheck(EmmaX, 500, "I") and ApprovalCheck(EmmaX, 1500) and EmmaX.GirlLikeCheck(Girl) >= 500:
            "[EmmaX.Name] замечает вас двоих, она лишь наклоняет голову в знак одобрения, а затем продолжает занятие."
            $ EmmaX.GLG(Girl,800,3,1)
            $ Girl.GLG(EmmaX,800,3,1)
            $ EmmaX.RecentActions.append("noticed " + Girl.Tag)
            return

    ch_e "[Player.Name]? [Girl.Name]? Не могли бы вы немедленно прекратить?"
    call Checkout(1)

    $ Girl.FaceChange("bemused", 2, Eyes="side")
    call AllReset(Girl)
    if ApprovalCheck(Girl, 700, "I"):
            $ Girl.FaceChange("bemused", 1)
            "[Girl.Name] пожимает плечами и возвращается на свое место."
            call Partner_Like(EmmaX,2,-1,500,Girl) #if likes emma 500+, +2, else -1
    else:
            "[Girl.Name] вскакивает и выбегает из комнаты."
            call Partner_Like(EmmaX,-2,-3,500,Girl) #if likes emma 500+, -2, else -3
            call Remove_Girl(Girl)

    $ Girl.Rep -= 1
    call Partner_Like(Girl,3,2,800,EmmaX)  #if likes the girl 800+, +3, else +2
    $ EmmaX.GLG(Girl,800,3,1)

    $ Player.Rep -= 1
    ch_e "Благодарю."
    ch_e "И, [Player.Name], задержись после занятий. . ."

    $ renpy.pop_call()
    $ renpy.pop_call()
    $ Player.Traits.append("detention")
    $ Player.DailyActions.append("detention")
    jump Class_Room

# end Emma_Teacher_Caught //////////////////////////////////////////////////////////

# Event Emma_Caught_Classroom  /////////////////////////////////////////////////////

label Emma_Caught_Classroom:
            #This label is called from a Location
            call Shift_Focus(EmmaX)
            "Вы идете по коридору и вдруг слышите странные звуки, доносящиеся из аудитории."                         #fix this scene, pants option
            show blackscreen onlayer black
            $ Player.AddWord(1,"interruption") #adds to Recent
            $ bg_current = "bg classroom"
            call CleartheRoom(EmmaX,0,1)
            $ EmmaX.OutfitChange(Changed=1)
            $ EmmaX.Loc = 0
            call Set_The_Scene
            $ EmmaX.Loc = "bg desk"
            $ Taboo = 0
            $ EmmaX.FaceChange("sexy")
            $ EmmaX.Eyes = "closed"
            $ EmmaX.ArmPose = 1
            $ Count = 0
            call Shift_Focus(EmmaX)
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
#            $ Trigger3 = "fondle pussy"
#            $ Trigger5 = "fondle breasts"
            $ EmmaX.Offhand = "fondle pussy"
            $ EmmaX.RecentActions.append("classcaught")
            $ EmmaX.DailyActions.append("unseen")
            $ EmmaX.RecentActions.append("unseen")
            $ Line = 0
            $ Player.AddWord(1,"interruption") #adds to Recent
            call SexAct("masturbate") #call Emma_M_Loop #this has an added loop to account for popped calls

#After caught masturbating. . .
            if "angry" not in EmmaX.RecentActions:
                    $ EmmaX.Eyes = "sexy"
                    $ EmmaX.Brows = "confused"
                    $ EmmaX.Mouth = "normal"
            $ EmmaX.ArmPose = 1
            $ EmmaX.OutfitChange()
            $ bg_current = "bg classroom"
            $ EmmaX.Loc = "bg classroom"
            call Display_Girl(EmmaX)
            if "classcaught" in EmmaX.History:
                if ApprovalCheck(EmmaX, 1500):
                    ch_e "О, здравствуй."
                else:
                    ch_e "Я заметила, что у тебя появилась привычка подглядывать."
                    $ EmmaX.OutfitChange()
            else:
                    # First time caught
                    $ EmmaX.History.append("classcaught")
                    if "Historia" not in Player.Traits:
                        $ Tempmod = 25
                    ch_e "Что ж."
                    $ EmmaX.FaceChange("angry", Eyes="side")
                    if not Player.Male:
                        ch_e "Похоже, ты застала меня в. . . компрометирующем положении. . ."
                    else:
                        ch_e "Похоже, ты застал меня в. . . компрометирующем положении. . ."
                    menu:
                        extend ""
                        "Агась.":
                                $ EmmaX.FaceChange("perplexed", Mouth="normal")
                                $ EmmaX.Statup("Love", 70, -1)
                                $ EmmaX.Statup("Obed", 50, -2)
                                $ EmmaX.Statup("Lust", 80, -5)
                                ch_e "Эм. . . что ж. . ."
                        "Вам обязательно заниматься подобным в аудитории?":
                                $ EmmaX.FaceChange("angry", Eyes="side")
                                $ EmmaX.Statup("Obed", 50, 5)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                ch_e "Хмм."
                                $ EmmaX.FaceChange("sly", Brows="angry")
                                $ EmmaX.Statup("Lust", 80, 3)
                                ch_e "Пожалуй, не обязательно, но ты ведь знаешь, как это бывает,"
                                $ EmmaX.Brows = "normal"
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "-тяжело весь день находиться в окружении привлекательных студентов. . ."
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "включая тебя. . ."
                        "По-моему, это было очень сексуально.":
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Love", 70, 5)
                                $ EmmaX.Statup("Obed", 50, 10)
                                $ EmmaX.Statup("Inbt", 70, 10)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Хмм, ну, пожалуй, я не могу винить тебя за такие мысли. . ."
                        "Вы о чем?":
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Love", 70, -10)
                                $ EmmaX.Statup("Obed", 50, -5)
                                ch_e "Я занималась. . ."
                                $ EmmaX.FaceChange("surprised")
                                $ EmmaX.Statup("Love", 70, 15)
                                $ EmmaX.Statup("Obed", 50, 15)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                ch_e "О!"
                                $ EmmaX.FaceChange("perplexed")
                                ch_e "Да так, ни о чем, я просто. . ."
                                $ EmmaX.Eyes = "side"
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "занималась бумажной работой. . ."
                                $ EmmaX.FaceChange("sly")
                                $ Line = 1
                    ch_e "Итак, мы как-то можем замять эту. . . ситуацию?"
                    menu:
                        extend ""
                        "Думаю, я могу обо всем забыть.":
                                $ EmmaX.FaceChange("smile")
                                $ EmmaX.Statup("Love", 80, 10)
                                $ EmmaX.Statup("Obed", 60, 10)
                                $ EmmaX.Statup("Inbt", 70, 15)
                                ch_e "Благодарю, [EmmaX.Petname]. Я ценю твое благоразумие."
                                $ EmmaX.FaceChange("sly")
                                if not Player.Male:
                                    ch_e "Ты -точно- уверена, что я не могу ничего для тебя сделать?"
                                else:
                                    ch_e "Ты -точно- уверен, что я не могу ничего для тебя сделать?"
                        "Что вы предлагаете?":
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Love", 70, 5)
                                $ EmmaX.Statup("Obed", 60, 15)
                                $ EmmaX.Statup("Inbt", 70, 15)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Ох, я уверена, что это будет стоить твоего времени. . ."
                        "Какую ситуацию?":
                                if Line != 1:
                                        $ EmmaX.FaceChange("confused")
                                        $ EmmaX.Statup("Love", 70, -10)
                                        $ EmmaX.Statup("Obed", 50, -5)
                                        ch_e "Что ж, я ведь. . ."
                                        $ EmmaX.FaceChange("surprised")
                                        $ EmmaX.Statup("Love", 70, 15)
                                        $ EmmaX.Statup("Obed", 50, 15)
                                        $ EmmaX.Statup("Inbt", 70, 5)
                                        ch_e "О!"
                                        $ EmmaX.FaceChange("perplexed")
                                        ch_e "Да, никакую, я ведь просто. . ."
                                        $ EmmaX.Eyes = "side"
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "занималась бумажной работой. . ."
                                        $ EmmaX.FaceChange("sly")
                                else:
                                        $ EmmaX.FaceChange("angry")
                                        $ EmmaX.Statup("Love", 70, -5)
                                        $ EmmaX.Statup("Inbt", 70, 5)
                                        ch_e "Полагаю, до тебя не дошло. . ."
                                        $ EmmaX.FaceChange("sly")
                                        ch_e "До сих пор. . ."
                    $ Line = 0
                    $ MultiAction = 0
                    $ Tempmod = 25
                    menu:
                        extend ""
                        "Не могли бы вы раздеться?":
                                $ EmmaX.Statup("Love", 70, 5)
                                $ EmmaX.Statup("Obed", 50, 10)
                                $ EmmaX.Statup("Inbt", 70, 15)
                                ch_e "Значит, ты хочешь лучше разглядеть происходящее?"
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Полагаю, это можно устроить. . ."
                                ch_e "В какой-то степени. . ."
                                "Мисс Фрост подходит к двери и запирает ее."
                                $ Taboo = 0
                                $ EmmaX.Taboo = 0
                                if "Historia" in Player.Traits:
                                        return 1
                                call Group_Strip(EmmaX)
                        "Не могли бы вы просто продолжить?":
                                $ EmmaX.Statup("Love", 70, 10)
                                $ EmmaX.Statup("Obed", 50, 15)
                                $ EmmaX.Statup("Inbt", 70, 15)
                                ch_e "Ох, ты хочешь посмотреть еще немного?"
                                ch_e "Я не могу винить тебя за это желание."
                                $ EmmaX.Eyes = "down"
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Может тоже устроишь. . . что-нибудь подобное?"
                                menu:
                                    "Ага!":
                                        $ EmmaX.Statup("Love", 70, 5)
                                        $ EmmaX.Statup("Inbt", 70, 10)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "Замечательно."
                                        if "Historia" not in Player.Traits:
                                            call Seen_First_Peen(EmmaX)
                                        if Player.Male:
                                                "Вы начинаете мастурбировать свой член."
                                                $ Trigger2 = "jackin"
                                        else:
                                                "Вы начинаете ласкать свою киску."
                                                $ Trigger2 = "jilling"
                                    "Нет, просто продолжайте.":
                                        $ EmmaX.FaceChange("sad")
                                        $ EmmaX.Statup("Love", 70, -10)
                                        $ EmmaX.Statup("Obed", 50, 5)
                                        $ EmmaX.Statup("Inbt", 70, 5)
                                        ch_e "Pity."
                                $ EmmaX.FaceChange("sly")
                                "[EmmaX.Name] подходит к двери и запирает ее."
                                $ Taboo = 0
                                $ EmmaX.Taboo = 0
                                $Trigger = "masturbation"
#                                $Trigger3 = "fondle breasts"
                                $ EmmaX.Offhand = "fondle breasts"
                                "Она откидывается назад и проводит кончиками пальцев по своей груди."
                                if "Historia" in Player.Traits:
                                        return 1
                                call Girl_M_Cycle
                        "Могу я прикоснуться к вам?":
                                $ EmmaX.Statup("Love", 70, 5)
                                $ EmmaX.Statup("Obed", 50, 10)
                                $ EmmaX.Statup("Inbt", 70, 10)
                                ch_e "Хмм, мне бы не помешала помощь. . . "
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "возможно, у тебя найдутся какие-нибудь идеи?"
                                "[EmmaX.Name] подходит к двери и запирает ее."
                                $ Taboo = 0
                                $ EmmaX.Taboo = 0
                                if "Historia" in Player.Traits:
                                        return 1
                                call Girl_FB_Prep
                        "Не могли бы вы дать мне руку? [[показать на свой член]" if Player.Male:
                                $ EmmaX.Statup("Love", 70, -5)
                                $ EmmaX.Statup("Obed", 50, 5)
                                $ EmmaX.Brows = "surprised"
                                ch_e "Я ценю твою смелость, [EmmaX.Petname], но будь реалистом."
                                $ EmmaX.Brows = "normal"
                                $ EmmaX.Statup("Love", 70, 10)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Вместо этого я могла бы просто предложить немного. . . другой признательности."
                                "[EmmaX.Name] подходит к двери и запирает ее."
                                $ Taboo = 0
                                $ EmmaX.Taboo = 0
                                if "Historia" in Player.Traits:
                                        return 1
                                call Group_Strip(EmmaX)
                        "Не могли бы вы дать мне руку? [[показать на свою киску]" if not Player.Male:
                                $ EmmaX.Statup("Love", 70, -5)
                                $ EmmaX.Statup("Obed", 50, 5)
                                $ EmmaX.Brows = "surprised"
                                ch_e "Я ценю твою смелость, [EmmaX.Petname], но будь реалисткой."
                                $ EmmaX.Brows = "normal"
                                $ EmmaX.Statup("Love", 70, 10)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Вместо этого я могла бы просто предложить немного. . . другой признательности."
                                "[EmmaX.Name] подходит к двери и запирает ее."
                                $ Taboo = 0
                                $ EmmaX.Taboo = 0
                                if "Historia" in Player.Traits:
                                        return 1
                                call Group_Strip(EmmaX)
                        "Я, пожалуй, пойду.":
                                $ EmmaX.FaceChange("surprised")
                                $ EmmaX.Statup("Obed", 50, 5)
                                ch_e "Ох."
                                $ EmmaX.FaceChange("confused")
                                $ EmmaX.Statup("Love", 70, -5)
                                $ EmmaX.Statup("Inbt", 70, -5)
                                ch_e "Что ж, полагаю. . ."
                                $ EmmaX.FaceChange("perplexed")
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Тогда увидимся. . . на занятиях. . ."
                    $ EmmaX.OutfitChange()
                    "Затем, [EmmaX.Name] собирает свои вещи и подходит к двери."
                    "Она оборачивается, держа руку на ручке двери."
                    $ EmmaX.FaceChange("sly")
                    ch_e "О, и [EmmaX.Petname]?"
                    ch_e "Ты можешь звать меня просто \"Эмма.\""
                    $ EmmaX.Name = "Эмма"
                    $ EmmaX.Name_rod = "Эммы"
                    $ EmmaX.Name_dat = "Эмме"
                    $ EmmaX.Name_vin = "Эмму"
                    $ EmmaX.Name_tvo = "Эммой"
                    $ EmmaX.Name_pre = "Эмме"
                    $ EmmaX.Names.append("Emma")
                    $ EmmaX.Loc = "bg emma"
                    hide Emma_Sprite with easeoutleft
                    if EmmaX in Present:
                            $ Present.remove(EmmaX)
                    $ Round = 20 if Round > 20 else Round
                    $ MultiAction = 1
            return

# end Emma_Caught_Classroom/////////////////////////////////////////////////////

label Emma_M_Loop:
        if "Historia" in Player.Traits:
                call Girl_M_Interupted
        else:
                call Girl_M_Cycle
        return

# Event Emma_Detention  /////////////////////////////////////////////////////

label Emma_Detention:
            #This label is called from a Location
            call Shift_Focus(EmmaX)
            call CleartheRoom(EmmaX,0,1)
            if "traveling" in Player.RecentActions:
                    "Вы входите в комнату и видите, что [EmmaX.Name] ждет вас в дальнем конце комнаты."
            else:
                    "После занятий студенты расходятся, вы ждете несколько минут, пока все не уйдут."
                    "Как только последний студент уходит, [EmmaX.Name] подходит к вам."
            show blackscreen onlayer black
            $ bg_current = "bg classroom"
            $ EmmaX.Loc = "bg classroom"
            $ EmmaX.OutfitChange()
            call Set_The_Scene
            $ EmmaX.FaceChange("sly")
            $ EmmaX.ArmPose = 2
            $ Count = 0
            call CleartheRoom(EmmaX,0,1)
            hide blackscreen onlayer black
            $ Line = 0
            if "detention" in Player.DailyActions:
                    ch_e "Я рада, что ты серьезно относишься к своему. . . образованию."
            else:
                    #if you skipped detention
                    $ EmmaX.FaceChange("surprised")
                    ch_e "Ох, [EmmaX.Petname], тебе не стоит пропускать свое наказание. . ."
            $ Player.Traits.remove("detention")
            $ EmmaX.RecentActions.append("detention")
            $ EmmaX.DailyActions.append("detention")
            $ EmmaX.FaceChange("sly")
            $ EmmaX.Statup("Lust", 80, 3)
            if not Player.Male:
                ch_e "Ты была такой непослушной студенткой. . ."
            else:
                ch_e "Ты был таким непослушным студентом. . ."
            $ EmmaX.ArmPose = 1
            $ EmmaX.FaceChange("sadside", Brows="normal")
            $ EmmaX.Statup("Lust", 80, 5)
            ch_e "Как тебе не стыдно ухлестывать за девчушками при всех. . ."
            $ EmmaX.FaceChange("sly")
            $ EmmaX.Statup("Lust", 80, 3)
            if "detention" in EmmaX.History:
                    ch_e "И чем мы займемся на этот раз?"
            else:
                    #first time
                    ch_e "И что же мне с тобой делать. . ."
                    $ EmmaX.History.append("detention")

            "[EmmaX.Name] подходит к двери и запирает ее."
            $ Taboo = 0
            $ EmmaX.Taboo = 0
            $ Player.Traits.append("locked")
            menu:
                extend ""
                "Думаю, мне стоит сосредоточиться на учебе.":
                        if ApprovalCheck(EmmaX, 900) and "classcaught" in EmmaX.History:
                                $ EmmaX.FaceChange("perplexed")
                                $ EmmaX.Statup("Inbt", 70, -3)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Ох. Ты серьезно? Я думала, мы займемся чем-то более. . . веселым."
                                menu:
                                    extend ""
                                    "Шучу, конечно, чем займемся? [[Сексуальные действия]":
                                        $ EmmaX.FaceChange("sly")
                                        $ EmmaX.Statup("Love", 90, 3)
                                        $ EmmaX.Statup("Obed", 60, 5)
                                        $ EmmaX.Statup("Inbt", 70, 5)
                                        ch_e "Почему я вообще терплю тебя?"
                                        call SexMenu
                                    "Нет, ты права, я слишком легкомысленно отношусь к своему образованию.":
                                        $ EmmaX.Statup("Love", 80, 1)
                                        $ EmmaX.Statup("Inbt", 70, -2)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "Ох. Ладно. Эм. . ."
                                        $ EmmaX.FaceChange("sad")
                                        $ EmmaX.Statup("Obed", 60, 5)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "Полагаю, тогда мы могли бы пройтись по нескольким темам сегодняшнего занятия. . ."
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        $ Player.XP += 10
                        else:
                                        #She's not into you yet.
                                        $ EmmaX.FaceChange("sad", Mouth="normal")
                                        $ EmmaX.Statup("Love", 50, 5)
                                        $ EmmaX.Statup("Love", 80, 5)
                                        $ EmmaX.Statup("Obed", 60, 5)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "Да. . . Точно. . ."
                                        $ EmmaX.Statup("Inbt", 50, 5)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        ch_e "Полагаю, тогда мы могли бы пройтись по нескольким темам сегодняшнего занятия. . ."
                                        $ EmmaX.Statup("Inbt", 70, 5)
                                        $ EmmaX.Statup("Lust", 80, 5)
                                        $ Player.XP += 10
                "У меня есть пара идей. . . [[Сексуальные действия]":
                        if ApprovalCheck(EmmaX, 900) and "classcaught" in EmmaX.History:
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Love", 90, 5)
                                $ EmmaX.Statup("Obed", 60, 5)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                ch_e "Я не сомневаюсь. . ."
                                call SexMenu
                        else:
                                #She's not into you yet.
                                $ EmmaX.FaceChange("sad", Mouth="smirk")
                                $ EmmaX.Statup("Love", 80, 5)
                                $ EmmaX.Statup("Obed", 60, 5)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Не сомневаюсь. . . но, к сожалению, сейчас не время для этого."
                                $ EmmaX.Statup("Inbt", 50, 5)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                $ EmmaX.Statup("Lust", 80, 5)
                                ch_e "Нам нужно пройтись по нескольким темам сегодняшнего занятия. . ."
                                $ EmmaX.Statup("Inbt", 50, 5)
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ Player.XP += 10
            $ Round -= 20 if Round > 20 else 0
            ch_e "Хорошо, я думаю, на сегодня этого достаточно. . ."
            ch_e "Мы ведь не хотим, чтобы это вошло в привычку. . ."
            $ Tempmod = 0
            $ EmmaX.OutfitChange()
            $ Player.DrainWord("locked",0,0,1)
            return

# end Emma_Detention/////////////////////////////////////////////////////


# Event Emma_Key /////////////////////////////////////////////////////

#Not updated

label Emma_Key: #Emma_Update
        call Shift_Focus(EmmaX)
        $ EmmaX.Loc = bg_current
        call Set_The_Scene
        $ EmmaX.FaceChange("bemused")
        $ EmmaX.ArmPose = 2
        $ Event_Queue = [0,0]
        ch_e "Ты приходишь довольно часто. . ."
        ch_e ". . . тебе может понадобиться ключ. . ."
        ch_p "Спасибо."
        $ EmmaX.ArmPose = 1
        $ Keys.append(EmmaX) if EmmaX not in Keys else Keys
        $ EmmaX.Event[0] = 1
        return
# end Event Emma_Key /////////////////////////////////////////////////////



# Emma Taboo Talk Start < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

label Emma_Taboo_Talk:
        # This scene plays when you first try to do sexy stuff with Emma in public

        if "taboo" in EmmaX.History:
            return

        call Shift_Focus(EmmaX)
        $ EmmaX.FaceChange("sly")
        if "taboocheck" not in EmmaX.History:
                ch_e "[EmmaX.Petname], я знаю, мы порой. . . развлекаемся,"
                $ EmmaX.FaceChange("sly", Eyes="side")
                ch_e "но все это должно остаться только между нами."
                $ EmmaX.FaceChange("sly")
                ch_e "Я не могу позволить, чтобы о наших встречах узнали другие."
                ch_e "Понимаешь, я все-таки преподаватель."
                if not Player.Male:
                    ch_e "А ты студентка."
                else:
                    ch_e "А ты студент."
                $ EmmaX.FaceChange("sadside")
                ch_e "Все непросто."
                ch_e "Так что, боюсь, что мы можем. . ."
                $ EmmaX.FaceChange("sad")
                ch_e ". . .\"общаться\", только когда мы наедине."
                ch_e "Понимаешь?"
        else:
                ch_e "Уверена, я ясно дала понять, почему мы не можем заниматься подобным на людях. . ."

        $ Line = 1
        while Line >= 1:
            menu:
                extend ""
                "Да, пожалуй.":
                    $ EmmaX.FaceChange("smile")
                    if "taboocheck" in EmmaX.History:
                            pass
                    elif Line != 4:
                            #if you didn't ask all the questions first
                            $ EmmaX.Statup("Love", 60, 10)
                            $ EmmaX.Statup("Love", 70, 10)
                            $ EmmaX.Statup("Love", 90, 10)
                            $ EmmaX.Statup("Obed", 60, 5)
                            $ EmmaX.Statup("Inbt", 70, 5)
                    else:
                            $ EmmaX.Statup("Love", 60, 10)
                            $ EmmaX.Statup("Love", 90, 10)

                    ch_e "Спасибо за твою осмотрительность."
                    $ EmmaX.FaceChange("sly")
                    if ApprovalCheck(EmmaX, 2000) and "taboocheck" in EmmaX.History:
                            ch_e "Хотя. . . я полагаю, мы могли бы сделать исключение. . ."
                            $ EmmaX.Statup("Inbt", 90, 10)
                            $ Line = -1
                    else:
                            ch_e "Надеюсь, мы еще найдем время встретиться."
                            $ Line = 0

                "Мне плевать, что нас увидят." if Line != 2 and Line != 4:
                    if "taboocheck" in EmmaX.History:
                            ch_e "Я в курсе. . ."
                            if ApprovalCheck(EmmaX, 500, "I"):
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "Честно говоря, мне тоже."
                                    $ EmmaX.FaceChange("angry", Eyes="side")
                                    ch_e "Но дело в том, если нас застукают, меня уволят."
                                    $ EmmaX.FaceChange("angry")
                                    ch_e "А если меня уволят, я не смогу здесь оставаться."
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "Так что это точно не вариант."
                            else:
                                    $ EmmaX.FaceChange("confused", 1)
                                    ch_e "Если ты не в курсе, мне нужно поддерживать свою репутация."
                    elif ApprovalCheck(EmmaX, 500, "I"):
                                    $ EmmaX.Statup("Lust", 80, 5)
                                    $ EmmaX.Statup("Inbt", 70, 5)
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "Честно говоря, мне тоже."
                                    $ EmmaX.FaceChange("angry", Eyes="side")
                                    ch_e "Но дело в том, если нас застукают, меня уволят."
                                    $ EmmaX.FaceChange("angry")
                                    $ EmmaX.Statup("Love", 90, 10)
                                    $ EmmaX.Statup("Obed", 60, 10)
                                    ch_e "А если меня уволят, я не смогу здесь оставаться."
                                    $ EmmaX.FaceChange("sly")
                                    ch_e "Так что это точно не вариант."
                    else:
                                    $ EmmaX.Statup("Lust", 80, 5)
                                    $ EmmaX.Statup("Love", 90, 10)
                                    $ EmmaX.Statup("Obed", 60, 10)
                                    $ EmmaX.FaceChange("confused", 1)
                                    ch_e "Если ты не в курсе, мне нужно поддерживать свою репутация."
                    $ EmmaX.FaceChange("sly")
                    ch_e "Итак, теперь ты понимаешь, почему нас не должны видеть вместе?"
                    $ Line = 4 if Line != 1 else 2

                "Ты ведь можешь стереть память всем, кто увидит?" if Line != 3 and Line != 4:
                    if "taboocheck" in EmmaX.History:
                            ch_e "Да, мы уже обсуждали, почему это не вариант."
                    else:
                            if ApprovalCheck(EmmaX, 500, "I"):
                                $ EmmaX.FaceChange("sly")
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Love", 80, 5)
                                $ EmmaX.Statup("Obed", 60, 5)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                ch_e "Ты, должно быть, читаешь мои мысли."
                            elif ApprovalCheck(EmmaX, 800, "LO"):
                                $ EmmaX.FaceChange("sly",1)
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Love", 90, 10)
                                $ EmmaX.Statup("Obed", 60, 10)
                                $ EmmaX.Statup("Inbt", 70, 5)
                                if not Player.Male:
                                    ch_e "Ох, какая же ты проказница."
                                else:
                                    ch_e "Ох, какой же ты проказник."
                            else:
                                $ EmmaX.FaceChange("surprised",1)
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Obed", 60, 10)
                                $ EmmaX.Statup("Inbt", 50, 15)
                                $ EmmaX.Statup("Inbt", 70, 10)
                                ch_e "Что? Я бы никогда так не поступила!"
                            $ EmmaX.FaceChange("angry",Eyes="side")
                            ch_e "В любом случае, это тоже не вариант."
                    ch_e "Я не могу слишком долго возиться с мыслями студентов, иначе Чарльз все поймет."
                    ch_e "Небрежное стирание памяти тоже не останется незамеченным."
                    if EmmaX in Rules:
                            #if Xavier ignores you
                            ch_p "Но Ксавье теперь вне игры. . ."
                            $ EmmaX.FaceChange("sly")
                            ch_e "Твоя правда. . ."
                            ch_e "Небольшие правки не повредят. . ."
                            $ Line = -1
                    else:
                            $ EmmaX.FaceChange("confused",Mouth="normal")
                            ch_e "Надеюсь, мы заодно?"
                            $ Line = 4 if Line != 1 else 3

                "Мне все равно, давай повеселимся." if Line == 4:
                    $ Line = 0
                    if ApprovalCheck(EmmaX, 2000):
                            $ EmmaX.FaceChange("surprised", Eyes="side")
                            $ EmmaX.Statup("Lust", 80, 5)
                            $ EmmaX.Statup("Inbt", 50, 15)
                            $ EmmaX.Statup("Inbt", 70, 10)
                            ch_e "Ох, у меня будет столько неприятностей из-за этого. . ."
                            $ EmmaX.Statup("Love", 90, 5)
                            $ EmmaX.Statup("Obed", 60, 15)
                            $ EmmaX.FaceChange("sly")
                            ch_e "но ты того стоишь."
                            $ Line = -1
                    elif ApprovalCheck(EmmaX, 800, "I"):
                            $ EmmaX.FaceChange("surprised", Eyes="side")
                            $ EmmaX.Statup("Lust", 80, 5)
                            $ EmmaX.Statup("Obed", 60, 15)
                            ch_e "Ох, у меня будет столько неприятностей из-за этого. . ."
                            $ EmmaX.FaceChange("sly")
                            ch_e "но это будет очень весело."
                            $ Line = -1
                    elif "taboocheck" in EmmaX.History:
                            $ EmmaX.FaceChange("angry")
                            $ EmmaX.Statup("Love", 90, -5)
                            $ EmmaX.Statup("Obed", 60, -5)
                            ch_e "Тебе стоит знать границы."
                            $ EmmaX.RecentActions.append("angry")
                            $ EmmaX.DailyActions.append("angry")
                            $ renpy.pop_call() #drops it past the sex menu
                    else:
                            $ EmmaX.FaceChange("angry")
                            $ EmmaX.Statup("Love", 90, -5)
                            $ EmmaX.Statup("Obed", 60, -5)
                            $ EmmaX.Statup("Inbt", 70, 10)
                            ch_e "Это очень плохо."
                            ch_e "Если ты не можешь соблюдать такое простое ограничение, то думаю, на данный момент мы закончили."
                            $ EmmaX.RecentActions.append("angry")
                            $ EmmaX.DailyActions.append("angry")
                            $ renpy.pop_call() #drops it past the sex menu
        #end loop if Line < 1

        if "taboocheck" not in EmmaX.History:
                $ EmmaX.History.append("taboocheck")
        if Line == -1:
                #if she agrees to do it
                $ EmmaX.History.append("taboo")
                $ EmmaX.History.remove("taboocheck")
        $ Line = 0
        return

# Emma Taboo Talk End < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Emma Threesome Talk Start < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
label Emma_ThreeCheck(Pass=3,Quest=[],Girl=0,BO=[]): #rkeljsvg
        # This is called when Emma is asked whether to do a threesome
        if EmmaX.SEXP <= 30:
                $ EmmaX.FaceChange("confused")
                ch_e "[EmmaX.Petname], я едва терплю тебя, даже не пытайся приводить других девушек."
                return
        if "three" in EmmaX.History:
                return

        call Shift_Focus(EmmaX)
        $ Line = 0
        $ BO = TotalGirls[:]
        $ BO.remove(EmmaX)
        while BO:
                if "saw with " + BO[0].Tag in EmmaX.Traits:
                        $ Line = "Я видела тебя кое с кем"
                if BO[0].Loc == bg_current:
                        $ Girl = BO[0]
                        $ BO = [1]
                $ BO.remove(BO[0])

        if not Girl or Girl not in TotalGirls:
            $ Quest.append(2)
            if Line:
                $ EmmaX.FaceChange("angry", Eyes = "side")
                if Line:
                        ch_e "[Line]. Я не знаю, что и думать." #"I saw you with Rogue"
                $ Line = 0
                if "sleeptime" in EmmaX.History:
                        # if you tried to have a sleepover
                        ch_e "Я знаю, что ты хочешь, чтобы я заночевала с этой. . . девочкой. . ."
                        $ EmmaX.History.remove("sleeptime")

        if "threecheck" not in EmmaX.History:
                $ EmmaX.FaceChange("bemused", Eyes = "side")
                "[EmmaX.Name] приближается к вам и шепчет:"
                if ApprovalCheck(EmmaX, 900, "L"):
                        if not Player.Male:
                            ch_e "[EmmaX.Petname], ты мне совсем. . . небезразлична. . ."
                        else:
                            ch_e "[EmmaX.Petname], ты мне совсем. . . небезразличен. . ."
                elif ApprovalCheck(EmmaX, 800, "L"):
                        if not Player.Male:
                            ch_e "[EmmaX.Petname], я думаю, ты очень. . . интересна. . ."
                        else:
                            ch_e "[EmmaX.Petname], я думаю, ты очень. . . интересный. . ."
                elif ApprovalCheck(EmmaX, 500, "O"):
                        ch_e "[EmmaX.Petname], в тебе есть что-то. . . неотразимое. . ."
                elif ApprovalCheck(EmmaX, 500, "I"):
                        ch_e "[EmmaX.Petname], ты же знаешь, что я готова. . . пойти на уступки,"
                else:
                        ch_e "[EmmaX.Petname], я пока не знаю, что это за чувство, но. . ."
                ch_e "Я преподаватель нашего института, меня не должны уличить в создании чего-то вроде. . ."
                ch_e "-гарема из студентов."
                ch_e "Одни только наши отношения вызвали бы переполох, но несколько студентов?"
                ch_e "Это может спровоцировать настоящую катастрофу."
        else:
                ch_e "Я уже объясняла, почему я не могу."
        while Pass > 0:
            menu:
                extend ""
                "Да, я понимаю.":
                        $ EmmaX.FaceChange("smile")
                        if "threecheck" not in EmmaX.History:
                                $ EmmaX.Statup("Love", 60, 10)
                                $ EmmaX.Statup("Love", 90, 10)

                        ch_e "Спасибо, что не настаиваешь."
                        $ EmmaX.FaceChange("sly")
                        if Pass == 1 and ApprovalCheck(EmmaX, 2000):
                            ch_e "Хотя, полагаю. . . возможно, я могу сделать исключение. . ."
                            $ Pass = 0
                        else:
                            ch_e "Я очень надеюсь, мы все еще можем проводить время вместе?"
                            $ Pass = -1

                "Но она не против." if 2 not in Quest:
                        # This can add up to 2 if both girls refuse, or -2 if both are really into it.
                        # -1 more likely
                        $ Quest.append(2)
                        if Girl.Loc == bg_current:
                                $ Pass -= 1
                                if "poly Emma" in Girl.Traits:
                                                #If Rogue is already on board
                                                if Girl == RogueX:
                                                        ch_r "Ага, как я и говорила, я готова."
                                                elif Girl == KittyX:
                                                        ch_k "Ага, это звучит весело."
                                                elif Girl == LauraX:
                                                        ch_l "Да, я в деле."
                                                elif Girl == JeanX:
                                                        ch_j "Конечно."
                                                elif Girl == StormX:
                                                        ch_s "Я не против."
                                                elif Girl == JubesX:
                                                        ch_v "Конечно."
                                                elif Girl == GwenX:
                                                        ch_g "Ты шутишь? Конечно, я не против!"
                                                elif Girl == BetsyX:
                                                        ch_b "Конечно, это может быть интересно!"
                                                elif Girl == DoreenX:
                                                        ch_d "Я готова!"
                                                elif Girl == WandaX:
                                                        ch_w "Я не против."
                                else:
                                        $ Girl.Traits.append("poly Emma")
                                        if ApprovalCheck(Girl, 1500) and Girl.LikeEmma >= 800:
                                                if Girl == RogueX:
                                                        ch_r "Да."
                                                elif Girl == KittyX:
                                                        ch_k "Да, конечно."
                                                elif Girl == LauraX:
                                                        ch_l "Конечно."
                                                elif Girl == JeanX:
                                                        ch_j "Конечно."
                                                elif Girl == StormX:
                                                        ch_s "Я не против."
                                                elif Girl == JubesX:
                                                        ch_v "Конечно."
                                                elif Girl == GwenX:
                                                        ch_g "Ты шутишь? Конечно, я не против!"
                                                elif Girl == BetsyX:
                                                        ch_b "Конечно."
                                                elif Girl == DoreenX:
                                                        ch_d "Я готова!"
                                                elif Girl == WandaX:
                                                        ch_w "Ага."
                                        elif ApprovalCheck(Girl, 1500) and Girl.LikeEmma >= 600:
                                                if Girl == RogueX:
                                                        ch_r "Да, ты справишься."
                                                elif Girl == KittyX:
                                                        ch_k "Да, все будет в порядке."
                                                elif Girl == LauraX:
                                                        ch_l "Да, все будет клево."
                                                elif Girl == JeanX:
                                                        ch_j "Конечно."
                                                elif Girl == StormX:
                                                        ch_s "Я не против."
                                                elif Girl == JubesX:
                                                        ch_v "Конечно."
                                                elif Girl == GwenX:
                                                        ch_g "Ты шутишь? Конечно, я не против!"
                                                elif Girl == BetsyX:
                                                        ch_b "Конечно."
                                                elif Girl == DoreenX:
                                                        ch_d "Я готова!"
                                                elif Girl == WandaX:
                                                        ch_w "Я совсем не против."
                                        elif ApprovalCheck(Girl, 2000) or Girl == GwenX:
                                                if Girl == RogueX:
                                                        if not Player.Male:
                                                            ch_r "Мы с тобой ладим как кошка с собакой. . ."
                                                            ch_r "но я хочу ее осчастливить."
                                                        else:
                                                            ch_r "Мы с тобой ладим как кошка с собакой. . ."
                                                            ch_r "но я хочу его осчастливить."
                                                elif Girl == KittyX:
                                                        if not Player.Male:
                                                            ch_k "Ты мне не очень нравишься, но я хочу, чтобы она была счастлива."
                                                        else:
                                                            ch_k "Ты мне не очень нравишься, но я хочу, чтобы он был счастлив."
                                                elif Girl == LauraX:
                                                        ch_l "Пфф, ага. . ."
                                                        if not Player.Male:
                                                            ch_l "Похоже, ты ей нравишься."
                                                        else:
                                                            ch_l "Похоже, ты ему нравишься."
                                                elif Girl == JeanX:
                                                        ch_j "Приводи кого хочешь."
                                                elif Girl == StormX:
                                                        if not Player.Male:
                                                            ch_s "Ладно, ради нее я не против."
                                                        else:
                                                            ch_s "Ладно, ради него я не против."
                                                elif Girl == JubesX:
                                                        if not Player.Male:
                                                            ch_v ". . . если этого хочет она."
                                                        else:
                                                            ch_v ". . . если этого хочет он."
                                                elif Girl == GwenX:
                                                        ch_g "Ты шутишь? Конечно, я не против!"
                                                elif Girl == BetsyX:
                                                        if not Player.Male:
                                                            ch_b "Может, мы с тобой и не особо ладим, но я готова пойти на это ради нее."
                                                        else:
                                                            ch_b "Может, мы с тобой и не особо ладим, но я готова пойти на это ради него."
                                                elif Girl == DoreenX:
                                                        ch_d "Я готова!"
                                                elif Girl == WandaX:
                                                        if not Player.Male:
                                                            ch_w "Я не против ради нее."
                                                        else:
                                                            ch_w "Я не против ради него."
                                        elif ApprovalCheck(Girl, 500) and Girl.LikeEmma >= 800:
                                                if Girl == RogueX:
                                                        if not Player.Male:
                                                            ch_r "Мне плевать на эту девку, но ты такая ухоженная и симпатичная."
                                                        else:
                                                            ch_r "Мне плевать на этого парня, но ты такая ухоженная и симпатичная."
                                                elif Girl == KittyX:
                                                        if not Player.Male:
                                                            ch_k "Ну, я не уверена насчет этой девки, но. . . Ты милая."
                                                        else:
                                                            ch_k "Ну, я не уверена насчет этого парня, но. . . Ты милая."
                                                elif Girl == LauraX:
                                                        ch_l "Эй, даже без [Player.Name], ты просто находка."
                                                elif Girl == JeanX:
                                                        ch_j "Конечно, почему нет?"
                                                elif Girl == StormX:
                                                        ch_s "Я была бы рада."
                                                elif Girl == JubesX:
                                                        ch_v "Конечно!"
                                                elif Girl == GwenX:
                                                        ch_g "Ты шутишь? Конечно, я не против!"
                                                elif Girl == BetsyX:
                                                        ch_b "Ты мне небезразлична."
                                                elif Girl == DoreenX:
                                                        ch_d "Я готова!"
                                                elif Girl == WandaX:
                                                        ch_w "Я совсем не против."
                                        else:
                                                if Girl == RogueX:
                                                        ch_r "Я ничего такого не говорила!"
                                                elif Girl == KittyX:
                                                        ch_k "Я ничего подобного не говорила!"
                                                elif Girl == LauraX:
                                                        ch_l "Что ты щас сказал?"
                                                elif Girl == JeanX:
                                                        ch_j "А? Ни за что."
                                                elif Girl == StormX:
                                                        ch_s "Я бы никогда на это не согласилась."
                                                elif Girl == JubesX:
                                                        ch_v "Ни за что."
                                                elif Girl == GwenX:
                                                        ch_g "Эм. . . нет, спасибо. . ."
                                                elif Girl == BetsyX:
                                                        ch_b "Это ошибка, я такого не говорила."
                                                elif Girl == DoreenX:
                                                        ch_d "Это ложь!"
                                                elif Girl == WandaX:
                                                        ch_w "Я на такое не подписывалась."
                                                $ Girl.Traits.remove("poly Emma")
                                                $ Pass += 1
                        if EmmaX.GirlLikeCheck(Girl) >= 700:
                                ch_e "И ты очень привлекательная, дорогая. . ."
                                $ Pass -= 1 if Pass > 0 else 0
                        elif EmmaX.GirlLikeCheck(Girl) >= 500:
                                ch_e "И ты. . . приятная. . ."
                        else:
                                ch_e "И это просто прекрасно, правда. . ."
                                $ Pass += 1
                        ch_e "Но я боюсь, что любые отношения будут проблемой."
                #end "she's cool with it"

                "Ксавье все равно." if Taboo and EmmaX in Rules and 3 not in Quest:
                                $ Quest.append(3)
                                ch_e "Что ж, может и так, но наше тайное может стать явным."
                                $ Pass -= 1

                "Ксавье ничего не узнает." if not Taboo and 3 not in Quest:
                                $ Quest.append(3)
                                ch_e "Что ж, может и так, но наше тайное может стать явным."
                                $ Pass -= 1

                "Мне все равно, давай сделаем это." if Quest:
                        if ApprovalCheck(EmmaX, 2000) and Pass <= 2:
                                $ EmmaX.FaceChange("surprised", Eyes="side")
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Inbt", 50, 15)
                                $ EmmaX.Statup("Inbt", 70, 10)
                                $ EmmaX.Statup("Love", 90, 5)
                                $ EmmaX.Statup("Obed", 60, 15)
                                ch_e "Ох, Из-за этого у меня могут быть большие неприятности. . ."
                                $ EmmaX.FaceChange("sly")
                                ch_e "но ты того стоишь."
                                $ Pass = 0
                        elif ApprovalCheck(EmmaX, 800, "I") and Pass <= 2:
                                $ EmmaX.FaceChange("surprised", Eyes="side")
                                $ EmmaX.Statup("Lust", 80, 5)
                                $ EmmaX.Statup("Obed", 60, 15)
                                ch_e "Ох, Из-за этого у меня могут быть большие неприятности. . ."
                                $ EmmaX.FaceChange("sly")
                                ch_e "но это будет очень весело."
                                $ Pass = 0
                        elif "threecheck" not in EmmaX.History:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Love", 90, -5)
                                $ EmmaX.Statup("Obed", 60, -5)
                                ch_e "Тебе придется научиться принимать ответ \"нет\"."
                                $ EmmaX.RecentActions.append("angry")
                                $ EmmaX.DailyActions.append("angry")
                                $ Pass = -1
                        else:
                                $ EmmaX.FaceChange("angry")
                                $ EmmaX.Statup("Love", 90, -5)
                                $ EmmaX.Statup("Obed", 60, -5)
                                $ EmmaX.Statup("Inbt", 70, 10)
                                ch_e "Это очень плохо."
                                ch_e "Если ты не можешь соблюдать такое простое ограничение, то думаю, на данный момент мы закончили."
                                $ EmmaX.RecentActions.append("angry")
                                $ EmmaX.DailyActions.append("angry")
                                $ Pass = -1

        if "threecheck" not in EmmaX.History:
                $ EmmaX.History.append("threecheck")
        if Pass == -1:
                # if the conditions added up to failure state, it exits the sex menu
                $ renpy.pop_call() #drops it past the sex menu
        else:
                #if the conditions don't add up to failure, then it results in a success state
                $ EmmaX.History.append("three")
                $ EmmaX.History.remove("threecheck")
                if Girl in TotalGirls:
                        if "poly " + Girl.Tag not in EmmaX.Traits:
                                $ EmmaX.Traits.append("poly " + Girl.Tag)
                        $ EmmaX.RecentActions.append("noticed " + Girl.Tag)
                        $ Girl.RecentActions.append("noticed Emma")
        return
# Emma Threesome Talk End < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# start Emma_BF//////////////////////////////////////////////////////////


label Emma_BF:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(EmmaX,"bemused","выглядит нервной. . .")
                return
        $ EmmaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(EmmaX)
        if EmmaX.Loc != bg_current:
            $ EmmaX.Loc = bg_current
            if EmmaX not in Party:
                "[EmmaX.Name] подходит к вам и спрашивает, можете ли вы поговорить."
            else:
                "[EmmaX.Name] поворачивается к вам и спрашивает, можете ли вы поговорить."

        $ Event_Queue = [0,0]
        call Set_The_Scene(0)
        call Display_Girl(EmmaX)
        "You can tell she's a bit uncomfortable about whatever she has to say."
        call Taboo_Level
        call CleartheRoom(EmmaX)
        $ EmmaX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in EmmaX.History:
                call expression EmmaX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        $ EmmaX.FaceChange("bemused", 1)

        if len(Player.Harem) >= 1 and "loser" in EmmaX.History and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Loser
        if Player.Lvl >= 7 and "idiot" in EmmaX.History and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Idiot
        ch_e "[EmmaX.Petname], мы уже достаточно долго. . . развлекаемся."
        ch_e ". . ."
        $ EmmaX.Eyes = "sexy"
        menu:
            ch_e "Тебе ведь тоже понравилось время, проведенное вместе?"
            "Да. Все было потрясающе.":
                $ EmmaX.Statup("Love", 200, 20)
            "Ага, наверное":
                $ EmmaX.Statup("Love", 200, 10)
            "Эм. . . возможно?":
                $ EmmaX.Statup("Love", 200, -10)
                $ EmmaX.Statup("Obed", 200, 30)
        if EmmaX.SEXP >= 10:
            ch_e "Думаю, мы ведем себя довольно неприлично. . ."
        if EmmaX.SEXP >= 15:
            ch_e "-по крайней мере, для студента и преподавателя. . ."

        if EmmaX in Player.Harem:
                #if she somehow already ended up in the harem
                ch_e "Полагаю, ты со всем справишься. . ."
                if "EmmaYes" in Player.Traits:
                        $ Player.Traits.remove("EmmaYes")
                if "boyfriend" not in EmmaX.Petnames:
                        $ EmmaX.Petnames.append("boyfriend")
                return

        if len(Player.Harem) >= 2:
            ch_e "Я понимаю, тебе для тебя это уже не впервой. . ."
        elif Player.Harem:
            ch_e "Я понимаю, что ты уже встречаешься с [Player.Harem[0].Name_tvo]. . ."

        if not EmmaX.Event[5]:
            ch_e "В общем. . ."
            ch_e "Я хочу спросить, не хочешь ли ты сделать наши отношения немного более. . . официальными."
            if not Player.Male:
                ch_e "Как думаешь, могу я считать тебя своей. . ."
                ch_e ". . .девушкой?"
                ch_e "-или кем-то вроде нее."
            else:
                ch_e "Как думаешь, могу я считать тебя своим. . ."
                ch_e ". . .парнем?"
                ch_e "-или кем-то вроде него."
        elif Player.Harem:
            if not Player.Male:
                ch_e ". . . но я бы тоже хотела считать тебя своей девушкой."
            else:
                ch_e ". . . но я бы тоже хотела считать тебя своим парнем."
        else:
            ch_e "Я не знаю, как я вообще терплю тебя, но я все равно хочу быть твоей девушкой."
        $ EmmaX.Event[5] += 1
        menu:
            extend ""
            "Ты шутишь? Мне бы тоже этого хотелось!":
                $ EmmaX.Statup("Love", 200, 25)
                "[EmmaX.Name] обхватывает вас руками и страстно целует."
                $ EmmaX.FaceChange("kiss")
                call Girl_Kissing_Launch(EmmaX,"kiss you")
                $ EmmaX.Kissed += 1
            "Эм, ладно.":
                $ EmmaX.Brows = "confused"
                "[EmmaX.Name] выглядит немного озабоченной тем, насколько небрежно вы воспринимаете ситуацию."
            "Я сейчас встречаюсь с другой." if Player.Harem:
                $ EmmaX.FaceChange("sad",1)
                ch_e "Я понимаю. Но я подумала, что, возможно, ты также сможешь встречаться и со мной?"
                menu:
                    extend ""
                    "Да. Конечно." if "EmmaYes" in Player.Traits:
                        $ EmmaX.Statup("Love", 200, 30)
                        "[EmmaX.Name] обхватывает вас руками и страстно целует."
                        $ EmmaX.FaceChange("kiss")
                        call Girl_Kissing_Launch(EmmaX,"kiss you")
                        $ EmmaX.Kissed += 1
                    "Она этого не поймет." if len(Player.Harem) == 1:
                        $ Line = "no"
                    "Они этого не поймут." if len(Player.Harem) > 1:
                        $ Line = "no"
                    "Извини, но. . . нет." if EmmaX.Event[5] != 20:
                        $ Line = "no"
                    "Ни за что.":
                        jump Emma_BF_Jerk
                if Line == "Нет":
                        $ EmmaX.Statup("Love", 200, -10)
                        ch_e "Что ж. . ."
                        ch_e "Я понимаю."
                        $ EmmaX.Event[5] = 20
                        call Remove_Girl(EmmaX)
                        $ Line = 0
                        return
            "Я так не думаю.":
                jump Emma_BF_Jerk

        if "Historia" not in Player.Traits:
                $ Player.Harem.append(EmmaX)
                if "EmmaYes" in Player.Traits:
                        $ Player.Traits.remove("EmmaYes")
        $ EmmaX.Petnames.append("boyfriend")
        $ EmmaX.FaceChange("sexy")
        if not Player.Male:
            ch_e "Итак. . . как бы ты хотела отпраздновать такое событие?"
        else:
            ch_e "Итак. . . как бы ты хотел отпраздновать такое событие?"
        if "Historia" in Player.Traits:
                return 1
        $ Tempmod = 10
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        $ Tempmod = 0
        return

label Emma_BF_Jerk:
        $ EmmaX.FaceChange("angry", 1)
        ch_e "Хорошо! Как знаешь."
        $ EmmaX.Statup("Obed", 50, 40)
        if EmmaX.Event[5] != 20:
                $ EmmaX.Statup("Obed", 200, (20* EmmaX.Event[5]))
        if 20 > EmmaX.Event[5] >= 3:
                $ EmmaX.FaceChange("sad")
                ch_e "Понимаешь, я устала беспокоиться о том, что ты думаешь по этому поводу."
                ch_e "Я буду считать нас парой независимо от того, хочешь ты этого или нет."
                ch_e "Оставляю тебя с этим. Прощай."
                if "Historia" in Player.Traits:
                        return 1
                $ EmmaX.Petnames.append("boyfriend")
                $ Achievements.append("I am not your Boyfriend!")
                $ bg_current = "bg player"
                call Remove_Girl(EmmaX)
                call Set_The_Scene
                $ renpy.pop_call()
                jump Player_Room
        if EmmaX.Event[5] > 1:
                ch_e "Было ошибкой просить тебя снова. Тебе все еще нужно повзрослеть."
        if EmmaX.Event[5] != 20:
                $ EmmaX.Statup("Love", 200, -(50* EmmaX.Event[5]))
        else:
                $ EmmaX.Statup("Love", 200, -50)
        ch_e "Уходи."
        if "Historia" in Player.Traits:
                return
        $ bg_current = "bg player"
        call Remove_Girl(EmmaX)
        $ renpy.pop_call()
        jump Player_Room

## start Emma_Love//////////////////////////////////////////////////////////
label Emma_Love(Shipping=[],Shipshape=0,BO=[]):   #rkeljsvg
        $ EmmaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        # Shipping is used to track who else you're involved with
        $ BO = TotalGirls[:]
        $ BO.remove(EmmaX)
        while BO:
            if ApprovalCheck(BO[0], 1200, "LO"):
                    $ Shipping.append(BO[0])
            $ BO.remove(BO[0])
        $ Shipshape = len(Shipping)

        if EmmaX.Loc == bg_current or EmmaX in Party:
                "[EmmaX.Name] бросает на тебя оценивающий взгляд."
        else:
                "[EmmaX.Name] выходит из-за угла и замечает вас."
        if bg_current != "bg emma" and bg_current != "bg player":
                "Не говоря ни слова, она берет вас за руку и отводит в свою комнату."
                $ bg_current = "bg emma"
        $ Event_Queue = [0,0]
        $ EmmaX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(EmmaX)
        call Shift_Focus(EmmaX)
        call Taboo_Level
        $ EmmaX.DailyActions.append("relationship")

        $ EmmaX.FaceChange("sexy",Eyes="side")
        if len(Player.Harem) >= 1 and "loser" in EmmaX.History and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Loser
        if Player.Lvl >= 7 and "idiot" in EmmaX.History and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Idiot
        ch_e "Как ты знаешь, наша. . . -ситуация- длится уже довольно долго."
        ch_e "Что меня более чем устраивает."
        $ EmmaX.FaceChange("sexy")
        ch_e "Мне нравится твоя компания. . . вот, что я пытаюсь сказать."
        menu:
                extend ""
                "Думаю, это нечто большее, чем просто совместное времяпрепровождение.":
                        $ EmmaX.FaceChange("smile",1)
                        $ EmmaX.Statup("Love", 200, 10)
                        $ EmmaX.Statup("Inbt", 90, 5)
                        ch_e "Да!"
                        ch_e "Да, конечно, нечто большее."
                        $ EmmaX.FaceChange("sly")
                        ch_e "Ты прямо читаешь мои мысли."
                "А мне твоя.":
                        $ EmmaX.FaceChange("sly")
                        $ EmmaX.Statup("Love", 200, 5)
                        $ EmmaX.Statup("Obed", 90, 2)
                        ch_e "Да, не сомневаюсь."
                        ch_e "Хотя, мне кажется, между нами нечто большее. . ."
                "Да, мы неплохо так веселимся вместе.":
                        $ EmmaX.FaceChange("confused")
                        $ EmmaX.Statup("Obed", 90, 5)
                        ch_e "Да, \"веселимся.\""
                        $ EmmaX.FaceChange("angry",Eyes="side")
                        ch_e "Весело, конечно, было, но я думала. . . а, неважно. . ."
                        $ EmmaX.FaceChange("sly")
                "Ну, ладно.":
                        $ EmmaX.FaceChange("confused",Eyes="side")
                        ch_e "Эм, да. . ."
                        ch_e ". . ."
                        $ EmmaX.FaceChange("confused")
                        ch_e "Я не уверена, что ясно выразилась. . ."
                "Ага, из тебя хорошая наездница.":
                    $ EmmaX.FaceChange("angry")
                    if not ApprovalCheck(EmmaX, 1600):
                            $ EmmaX.Statup("Obed", 90, -5)
                            $ EmmaX.Statup("Inbt", 90, -5)
                            $ EmmaX.Eyes="side"
                            ch_e "Неважно, это была плохая идея."
                            jump Emma_Love_End
                    if not Player.Male:
                        ch_e "Нахалка!"
                    else:
                        ch_e "Нахал!"
                    if ApprovalCheck(EmmaX, 1000, "OI"):
                            $ EmmaX.FaceChange("sly",2)
                            $ EmmaX.Statup("Obed", 90, 10)
                            $ EmmaX.Statup("Inbt", 90, 5)
                            $ EmmaX.Statup("Lust", 70, 5)
                            ch_e "Хотя да, это так."
                            $ EmmaX.Blush = 1
                    else:
                            $ EmmaX.FaceChange("sexy")
                            $ EmmaX.Statup("Obed", 90, 5)
                            $ EmmaX.Statup("Inbt", 90, 5)
                            ch_e "Хотя, пожалуй, в твоем замечании есть некое очарование."

        if not Player.Male:
            ch_e "Ты мне небезразлична. . ."
        else:
            ch_e "Ты мне небезразличен. . ."
        ch_e "Возможно, я ни с кем так не сближалась в последнее время."
        if ApprovalCheck(EmmaX, 1600):
                $ EmmaX.FaceChange("sexy",Eyes="side")
                ch_e "Возможно, даже никогда."
        ch_e ". . ."
        ch_e "В общем. . ."
        $ EmmaX.FaceChange("sexy",Brows="sad")
        ch_e "Я люблю тебя."
        menu:
                extend ""
                "Я тоже тебя люблю, [EmmaX.Pet]!":
                    $ EmmaX.FaceChange("smile",2)
                    $ EmmaX.Statup("Love", 200, 20)
                    $ EmmaX.Statup("Inbt", 90, 10)
                    ch_e "Я очень надеялась, что ты так скажешь!"
                    $ EmmaX.Petnames.append("lover")
                    jump Emma_Love_End
                "Ничего себе! Круто.":
                    $ EmmaX.FaceChange("confused")
                    $ EmmaX.Statup("Love", 200, 5)
                    ch_e "Круто?"
                    ch_e "Это все, что ты можешь ответить?"
                    $ EmmaX.FaceChange("sadside",2)
                "О, ладно.":
                    $ EmmaX.FaceChange("confused",2)
                    $ EmmaX.Statup("Obed", 90, 5)
                    $ EmmaX.Statup("Inbt", 90, -5)
                    ch_e "Ладно?"
                    $ EmmaX.FaceChange("angry")
                    ch_e "И это все, что ты можешь сказать?"
                "Ха!":
                    $ EmmaX.FaceChange("surprised",2)
                    $ EmmaX.Statup("Love", 200, -5)
                    $ EmmaX.Statup("Obed", 90, 10)
                    $ EmmaX.Statup("Inbt", 90, -5)
                    ch_e "!"
                    $ EmmaX.FaceChange("angry",2)
                    ch_e "Да, не такого ответа я ожидала."
        ch_e "Я надеюсь, что ты тоже меня любишь. . ."
        menu:
                extend ""
                "О! Да, конечно, я тебя люблю, [EmmaX.Pet]!":
                            $ EmmaX.NameCheck() #checks reaction to petname
                            $ EmmaX.FaceChange("smile",2)
                            $ EmmaX.Statup("Love", 90, 15)
                            $ EmmaX.Statup("Obed", 90, 2)
                            ch_e "Я очень хотела услышать такой ответ!"
                            $ EmmaX.Petnames.append("lover")
                            jump Emma_Love_End
                "Оооох! Да, конечно.":
                    if ApprovalCheck(EmmaX, 1200, "OI"):
                            $ EmmaX.FaceChange("sly",1)
                            $ EmmaX.Statup("Love", 200, 5)
                            $ EmmaX.Statup("Obed", 90, 10)
                    if ApprovalCheck(EmmaX, 1200, "OI"):
                            $ EmmaX.FaceChange("sly",1,Brows="angry")
                            $ EmmaX.Statup("Love", 200, 5)
                            $ EmmaX.Statup("Obed", 90, 5)
                            $ EmmaX.Statup("Inbt", 90, -5)
                    ch_e "Я рада, что мы все прояснили."
                "Ох. Мне стало как-то неловко.":
                            $ EmmaX.FaceChange("angry",2)
                            $ EmmaX.Statup("Love", 200, -15)
                            $ EmmaX.Statup("Obed", 90, 15)
                            $ EmmaX.Statup("Inbt", 90, -10)
                            ch_e "Неловко?!"
                            ch_e "Все вот-вот станет больше, чем \"неловко.\""
                            $ EmmaX.Blush = 1
                            $ Line = "angry"

        ch_e "Я даю тебе последний шанс."
        ch_e "Сейчас не время валять дурака."
        ch_e "Ты любишь меня или нет?"
        menu:
                extend ""
                "Да, конечно, я люблю тебя, [EmmaX.Pet]!":
                            $ EmmaX.NameCheck() #checks reaction to petname
                            $ EmmaX.FaceChange("sly",2)
                            $ EmmaX.Statup("Love", 90, 5)
                            $ EmmaX.Statup("Obed", 90, 15)
                            $ EmmaX.Statup("Inbt", 90, 5)
                            if not Player.Male:
                                ch_e "Долго же ты тянула с ответом."
                            else:
                                ch_e "Долго же ты тянул с ответом."
                            $ EmmaX.Petnames.append("lover")
                            jump Emma_Love_End
                "Я пока не уверена." if not Player.Male:
                    if Line != "angry" or ApprovalCheck(EmmaX, 800, "OI"):
                            $ EmmaX.FaceChange("sadside")
                            $ EmmaX.Statup("Obed", 90, 5)
                    else:
                            $ EmmaX.FaceChange("angry")
                            $ EmmaX.Statup("Love", 200, -5)
                            $ EmmaX.Statup("Obed", 90, 5)
                            $ EmmaX.Statup("Inbt", 90, -5)
                    ch_e "Ох."
                "Я пока не уверен." if Player.Male:
                    if Line != "angry" or ApprovalCheck(EmmaX, 800, "OI"):
                            $ EmmaX.FaceChange("sadside")
                            $ EmmaX.Statup("Obed", 90, 5)
                    else:
                            $ EmmaX.FaceChange("angry")
                            $ EmmaX.Statup("Love", 200, -5)
                            $ EmmaX.Statup("Obed", 90, 5)
                            $ EmmaX.Statup("Inbt", 90, -5)
                    ch_e "Ох."
                "Нет.":
                    if Line == "angry" or not ApprovalCheck(EmmaX, 800, "OI"):
                            $ EmmaX.FaceChange("angry")
                            $ EmmaX.Statup("Love", 200, -10)
                            $ EmmaX.Statup("Obed", 90, 10)
                            $ EmmaX.Statup("Inbt", 90, -5)
                    else:
                            $ EmmaX.FaceChange("sadside")
                            $ EmmaX.Statup("Love", 200, -10)
                            $ EmmaX.Statup("Obed", 90, 10)
                            $ EmmaX.Statup("Inbt", 90, -5)
                    ch_e "Ох."

        ch_e "Это из-за другой?"
        $ Line = 0
        menu:
                extend ""
                "Да, из-за другой." if Shipping and Shipshape < 3:
                    menu:       #rkeljsvgb
                        "Из-за [RogueX.Name_rod]." if RogueX in Shipping:
                                $ Line = RogueX
                        "Из-за [KittyX.Name_rod]." if KittyX in Shipping:
                                $ Line = KittyX
                        "Из-за [LauraX.Name_rod]." if LauraX in Shipping:
                                $ Line = LauraX
                        "Из-за [JeanX.Name_rod]." if JeanX in Shipping:
                                $ Line = JeanX
                        "Из-за [StormX.Name_rod]." if StormX in Shipping:
                                $ Line = StormX
                        "Из-за [JubesX.Name_rod]." if JubesX in Shipping:
                                $ Line = JubesX
                        "Из-за [GwenX.Name_rod]." if GwenX in Shipping:
                                $ Line = GwenX
                        "Из-за [BetsyX.Name_rod]." if BetsyX in Shipping:
                                $ Line = BetsyX
                        "Из-за [DoreenX.Name_rod]." if DoreenX in Shipping:
                                $ Line = DoreenX
                        "Мне бы не хотелось произносить ее имя.":
                                $ EmmaX.Statup("Obed", 90, 15)
                                $ EmmaX.Statup("Inbt", 90, 5)
                                $ EmmaX.Statup("Lust", 90, 5)
                                $ EmmaX.FaceChange("sadside",1)
                                ch_e "Пожалуй, я не могу тебя винить."

                "Да, из-за других" if Shipshape > 1:
                    $ EmmaX.Statup("Obed", 90, 15)
                    $ EmmaX.Statup("Inbt", 90, 5)
                    $ EmmaX.Statup("Lust", 90, 5)
                    ch_e "Пожалуй, я не могу тебя винить."
                "У меня никого нет.":
                    $ EmmaX.FaceChange("sadside")
                    $ EmmaX.Statup("Love", 200, -15)
                    $ EmmaX.Statup("Obed", 90, 15)
                    $ EmmaX.Statup("Inbt", 90, 5)
                    if ApprovalCheck(EmmaX, 1000, "OI"):
                        ch_e "Хммм. . . Что ж, хоть какое-то утешение."
                    else:
                        ch_e "Ясно."
                "Дело в тебе.":
                    $ EmmaX.FaceChange("angry")
                    $ EmmaX.Statup("Love", 200, -25)
                    $ EmmaX.Statup("Obed", 90, 15)
                    ch_e "Ох, вот значит как?"
                    $ EmmaX.Statup("Love", 200, -10)
                    ch_e "Ну хорошо."
                    $ EmmaX.RecentActions.append("angry")
                    $ EmmaX.DailyActions.append("angry")
        if Line:
                #If you called out a girl,
                if EmmaX.GirlLikeCheck(Line) >= 800:
                        $ EmmaX.Statup("Love", 200, 5)
                        $ EmmaX.Statup("Obed", 90, 20)
                        $ EmmaX.Statup("Inbt", 90, 5)
                        $ EmmaX.Statup("Lust", 90, 5)
                        ch_e "Да, она замечательная."
                else:
                        $ EmmaX.FaceChange("angry",Eyes="side")
                        $ EmmaX.Statup("Love", 200, -5)
                        $ EmmaX.Statup("Obed", 90, 20)
                        ch_e "Из-за этой коровы?!"
                        $ EmmaX.RecentActions.append("angry")
                        $ EmmaX.GLG(Line,800,-50,1)
        ch_e "Полагаю, мне просто придется забыть об этом."
        ch_e "Я. . . увидимся позже."
        ch_e "Мне нужно время все обдумать."


label Emma_Love_End:
        if "lover" not in EmmaX.Petnames:
                hide Emma_Sprite with easeoutright
                call Remove_Girl(EmmaX)
                $ EmmaX.Loc = "hold" #puts her off the board for the day
                jump Misplaced
                return

        "[EmmaX.Name] крепко обнимает вас."
        $ EmmaX.Statup("Love", 200, 25)
        $ EmmaX.Statup("Lust", 90, 5)
        ch_e "Итак. . . теперь, когда мы вместе. . ."
        $ EmmaX.Statup("Lust", 90, 10)

        if not EmmaX.Sex:
            ch_e "Думаю, мы достаточно долго ждали. . ."
        else:
            ch_e "Не желаешь. . . уединиться?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Да, давай сделаем это. . . [[заняться сексом]":
                    $ EmmaX.Statup("Inbt", 30, 20)
                    $ EmmaX.Statup("Obed", 70, 10)
                    ch_e "Ммм. . ."
                    call SexAct("sex") # call Emma_SexAct("sex")
                "У меня есть другая идея. . .[[выбрать другое занятие]":
                    $ EmmaX.Brows = "confused"
                    $ EmmaX.Statup("Obed", 70, 25)
                    ch_e "Намекни. . ."
                    $ Tempmod = 20
                    call SexMenu
        jump Misplaced
        return

label Emma_Love_Redux:
         #this is for if you rejected her but want a second chance
        $ Line = 0
        call Shift_Focus(EmmaX)
        $ EmmaX.DailyActions.append("relationship")
        if EmmaX.Event[6] >= 25:
                #if this is the second time through
                ch_p "Надеюсь, ты меня простила, я все еще люблю тебя."
                $ EmmaX.Statup("Love", 95, 10)
                if ApprovalCheck(EmmaX, 950, "L"):
                    $ Line = "love"
                else:
                    $ EmmaX.FaceChange("angry")
                    ch_e "Я не верю, что ты достаточно раскаиваешься, [EmmaX.Petname]."
                    $ EmmaX.Eyes="side"
                    ch_e ". . ."
                    $ EmmaX.FaceChange("angry",Mouth="lipbite")
                    ch_e "Не я решила порвать с тобой."
        else:
                    if not Player.Male:
                        ch_p "Помнишь, я как-то сказала тебе, что не люблю тебя?"
                    else:
                        ch_p "Помнишь, я как-то сказал тебе, что не люблю тебя?"
                    $ EmmaX.FaceChange("perplexed",1)
                    ch_e ". . ."
                    $ EmmaX.FaceChange("angry", Eyes="side")
                    ch_e "Что-то такое припоминаю, да."
        if Line != "love":
                menu:
                    extend ""
                    "Прости, я не хотела так говорить." if not Player.Male:
                            $ EmmaX.Eyes = "surprised"
                            ch_e "Ох? Так значит ты меня любишь?"
                            ch_p "Ага. То есть, да я люблю тебя, [EmmaX.Name]."
                            $ EmmaX.Statup("Love", 200, 10)
                            if ApprovalCheck(EmmaX, 950, "L"):
                                $ Line = "love"
                            else:
                                $ EmmaX.FaceChange("sadside")
                                ch_e "Я не уверена, что у меня все еще остались чувства к тебе. . ."
                    "Прости, я не хотел так говорить." if Player.Male:
                            $ EmmaX.Eyes = "surprised"
                            ch_e "Ох? Так значит ты меня любишь?"
                            ch_p "Ага. То есть, да я люблю тебя, [EmmaX.Name]."
                            $ EmmaX.Statup("Love", 200, 10)
                            if ApprovalCheck(EmmaX, 950, "L"):
                                $ Line = "love"
                            else:
                                $ EmmaX.FaceChange("sadside")
                                ch_e "Я не уверена, что у меня все еще остались чувства к тебе. . ."
                    "Я передумала, я люблю тебя, так что. . ." if not Player.Male:
                            if ApprovalCheck(EmmaX, 950, "L"):
                                $ Line = "love"
                                $ EmmaX.Eyes = "surprised"
                                ch_e "М?"
                            else:
                                $ EmmaX.Mouth = "sad"
                                ch_e "Ох, ты передумала. Замечательно."
                                $ EmmaX.Statup("Inbt", 90, 10)
                                $ EmmaX.FaceChange("sadside")
                                ch_e "Полагаю, я тоже. . ."
                    "Я передумал, я люблю тебя, так что. . ." if Player.Male:
                            if ApprovalCheck(EmmaX, 950, "L"):
                                $ Line = "love"
                                $ EmmaX.Eyes = "surprised"
                                ch_e "М?"
                            else:
                                $ EmmaX.Mouth = "sad"
                                ch_e "Ох, ты передумал. Замечательно."
                                $ EmmaX.Statup("Inbt", 90, 10)
                                $ EmmaX.FaceChange("sadside")
                                ch_e "Полагаю, я тоже. . ."
                    "Эм, неважно.":
                                $ EmmaX.Statup("Love", 200, -30)
                                $ EmmaX.Statup("Obed", 50, 10)
                                $ EmmaX.FaceChange("angry")
                                ch_e "Да как ты смеешь."
                                $ EmmaX.RecentActions.append("angry")
        if Line == "love":
                $ EmmaX.Statup("Love", 200, 40)
                $ EmmaX.Statup("Obed", 90, 10)
                $ EmmaX.Statup("Inbt", 90, 10)
                $ EmmaX.FaceChange("smile")
                ch_e "Я так счастлива!"
                ch_e "Я тоже люблю тебя, [EmmaX.Petname]!"
                if EmmaX.Event[6] < 25:
                        $ EmmaX.FaceChange("sly")
                        "Она хватает вас и притягивает к себе."
                        ch_e "Тебе не стоило заставлять меня ждать."
                $ EmmaX.Petnames.append("lover")
        $ EmmaX.Event[6] = 25
        return

# start Emma_Sub//////////////////////////////////////////////////////////

label Emma_Sub:     #Emma_Update
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(EmmaX,"bemused","выглядит тихой. . .")
                return
        $ EmmaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(EmmaX)
        $ Event_Queue = [0,0]

        if EmmaX.Loc != bg_current and EmmaX not in Party:
                "[EmmaX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить."
        else:
                "[EmmaX.Name] подходит к вам с явным желанием поговорить."
        $ EmmaX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(EmmaX)
        call Taboo_Level
        $ EmmaX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in EmmaX.History:
                call expression EmmaX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        $ EmmaX.FaceChange("bemused", 1)

        $ Line = 0
        if len(Player.Harem) >= 1 and "loser" in EmmaX.History and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Loser
        if Player.Lvl >= 7 and "idiot" in EmmaX.History and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Idiot
        ch_e "Я давно заметила, что ты пытаешься быть более"
        if not Player.Male:
            ch_e ". . . властной, [EmmaX.Petname]."
        else:
            ch_e ". . . властным, [EmmaX.Petname]."
        menu:
            extend ""
            "Верно. Для меня это естественно.":
                            $ EmmaX.Statup("Obed", 200, 10)
                            $ EmmaX.Statup("Inbt", 50, 5)
            "Извини, я не хотела вести себя так." if not Player.Male:
                            $ EmmaX.FaceChange("startled", 2)
                            $ EmmaX.Statup("Love", 80, 5)
                            $ EmmaX.Statup("Obed", 200, -5)
                            $ EmmaX.Statup("Inbt", 50, -5)
                            ch_e "О, не извиняйся. . ."
            "Извини, я не хотел вести себя так." if Player.Male:
                            $ EmmaX.FaceChange("startled", 2)
                            $ EmmaX.Statup("Love", 80, 5)
                            $ EmmaX.Statup("Obed", 200, -5)
                            $ EmmaX.Statup("Inbt", 50, -5)
                            ch_e "О, не извиняйся. . ."
            "Ага. Смирись.":
                    if ApprovalCheck(EmmaX, 1000, "LO"):
                            $ EmmaX.Statup("Obed", 200, 20)
                            $ EmmaX.Statup("Inbt", 50, 10)
                            ch_e "Кхм. . ."
                    else:
                            $ EmmaX.Statup("Love", 200, -10)
                            $ EmmaX.Statup("Obed", 200, 10)
                            $ EmmaX.Statup("Inbt", 50, 5)
                            $ EmmaX.FaceChange("angry")
                            ch_e "Это не совсем то, что я имела в виду." #(Loss of points)
                            menu:
                                extend ""
                                "Похоже, ты меня не так хорошо знаешь, а?":
                                        ch_e "Похоже, что так."
                                        $ Line = "rude"
                                "Извини. Мне показалось, что ты ждешь от меня именно этого.":
                                        $ EmmaX.FaceChange("sexy", 2)
                                        $ EmmaX.Eyes = "side"
                                        $ EmmaX.Statup("Love", 95, 5)
                                        $ EmmaX.Statup("Obed", 200, 5)
                                        $ EmmaX.Statup("Inbt", 50, 5)
                                        ch_e "Нет. . . это не совсем так. . ."

        if not Line:
                # She's advancing to the next stage
                ch_e "Я хотела сказать, что я. . ."
                $ EmmaX.FaceChange("sly", 2)
                if not Player.Male:
                    ch_e "-обожаю, когда ты тверда со мной."
                else:
                    ch_e "-обожаю, когда ты тверд со мной."
                $ EmmaX.FaceChange("smile", 1)
                menu:
                    extend ""
                    "Хорошо. Если ты хочешь быть со мной, то выполняй мои приказы.":
                            if ApprovalCheck(EmmaX, 1000, "LO"):
                                $ EmmaX.Statup("Obed", 200, 15)
                                $ EmmaX.Statup("Inbt", 50, 10)
                            else:
                                $ EmmaX.FaceChange("sadside", 1)
                                $ EmmaX.Statup("Love", 200, -5)
                                $ EmmaX.Statup("Obed", 200, 10)
                            if not Player.Male:
                                ch_e "Возможно, тебе стоит быть хоть иногда более чуткой, [EmmaX.Petname]. . ."
                            else:
                                ch_e "Возможно, тебе стоит быть хоть иногда более чутким, [EmmaX.Petname]. . ."
                            menu:
                                extend ""
                                "Плевать. Все так, как есть. Смирись или проваливай.":
                                        $ EmmaX.FaceChange("angry")
                                        $ EmmaX.Statup("Love", 200, -10)
                                        $ EmmaX.Statup("Obed", 200, 5)
                                        if not Player.Male:
                                            ch_e "Повзрослей прежде, чем говорить такое."
                                        else:
                                            ch_e "Стань более мужественным прежде, чем говорить такое."
                                        $ Line = "rude"
                                "Ну, может, ты и права.":
                                        $ EmmaX.FaceChange("bemused", 2)
                                        $ EmmaX.Eyes = "side"
                                        $ EmmaX.Statup("Love", 95, 5)
                                        $ EmmaX.Statup("Obed", 200, 3)
                                        $ EmmaX.Statup("Inbt", 50, 5)
                                        ch_e "Приятно слышать."

                    "Да? Так тебя это возбуждает?":
                                $ EmmaX.FaceChange("bemused", 2)
                                $ EmmaX.Eyes = "side"
                                $ EmmaX.Statup("Obed", 200, 5)
                                $ EmmaX.Statup("Inbt", 50, 10)


                    "Ты уверена, что не хочешь, чтобы я немного сбавила обороты?" if not Player.Male:
                            $ EmmaX.FaceChange("startled", 1)
                            $ EmmaX.Statup("Obed", 200, -5)
                            menu:
                                ch_e "Я не хочу, чтобы ты. . . чувствовала себя неловко."
                                "Если ты не против этого, то и я тоже.":
                                    $ EmmaX.FaceChange("bemused", 2)
                                    $ EmmaX.Statup("Love", 95, 10)
                                    $ EmmaX.Statup("Inbt", 50, 10)
                                    $ Line = 0
                                "Эм. . . ага, я странно чувствую себя из-за всего этого.  Извини.":
                                    $ EmmaX.Statup("Love", 200, -15)
                                    $ EmmaX.Statup("Obed", 200, -5)
                                    $ EmmaX.Statup("Inbt", 50, -10)
                                    $ Line = "embarrassed"

                    "Ты уверена, что не хочешь, чтобы я немного сбавил обороты?" if Player.Male:
                            $ EmmaX.FaceChange("startled", 1)
                            $ EmmaX.Statup("Obed", 200, -5)
                            menu:
                                ch_e "Я не хочу, чтобы ты. . . чувствовала себя неловко."
                                "Если ты не против этого, то и я тоже.":
                                    $ EmmaX.FaceChange("bemused", 2)
                                    $ EmmaX.Statup("Love", 95, 10)
                                    $ EmmaX.Statup("Inbt", 50, 10)
                                    $ Line = 0
                                "Эм. . . ага, я странно чувствую себя из-за всего этого.  Извини.":
                                    $ EmmaX.Statup("Love", 200, -15)
                                    $ EmmaX.Statup("Obed", 200, -5)
                                    $ EmmaX.Statup("Inbt", 50, -10)
                                    $ Line = "embarrassed"

                    "Меня не волнует, что тебе хочется. Я делаю то, что хочу.":
                                    $ EmmaX.Statup("Love", 200, -10)
                                    $ EmmaX.Statup("Obed", 200, 15)
                                    $ EmmaX.FaceChange("angry")
                                    ch_e "Эм. Мне кажется, я недооценила тебя."
                                    $ Line = "rude"

        if not Line:
            $ EmmaX.FaceChange("bemused", 1, Eyes="side")
            ch_e "Я привыкла всегда контролировать ситуацию."
            ch_e "Но когда это делаешь ты. . ."
            ch_e "Меня это очень. . . возбуждает."
            menu:
                extend ""
                "Ты не считаешь такие отношения несколько. . . ненормальными?":
                        $ EmmaX.Statup("Love", 200, -5)
                        $ EmmaX.Statup("Inbt", 50, -15)
                        ch_e "Вовсе нет, они просто немного. . . необычные."
                "Думаю, я смогу привыкнуть к таким отношениям.":
                        $ EmmaX.Statup("Obed", 200, 5)
                        $ EmmaX.Statup("Inbt", 50, 5)
                        $ EmmaX.FaceChange("smile", 1)

        if not Line:
            $ EmmaX.FaceChange("smile", 1)
            if not Player.Male:
                ch_e "Замечательно. Если я буду звать тебя. . . \"госпожой\". . ."
            else:
                ch_e "Замечательно. Если я буду звать тебя. . . \"господином\". . ."
            $ EmmaX.FaceChange("sly", 2)
            ch_e "Ты не будешь против?"
            $ EmmaX.Blush = 1
            menu:
                extend ""
                "Мне нравится.":
                                $ EmmaX.Statup("Love", 95, 5)
                                $ EmmaX.Statup("Obed", 200, 15)
                                $ EmmaX.Statup("Inbt", 50, 5)
                                if not Player.Male:
                                    ch_e "Отлично. . . {i}госпожа{/i}."
                                    $ EmmaX.Petname = "госпожа"
                                else:
                                    ch_e "Отлично. . . {i}господин{/i}."
                                    $ EmmaX.Petname = "господин"
                                if not Player.Male:
                                    $ EmmaX.Petname = "госпожа"
                                    $ EmmaX.Petname_rod = "госпожи"
                                    $ EmmaX.Petname_dat = "госпоже"
                                    $ EmmaX.Petname_vin = "госпожу"
                                    $ EmmaX.Petname_tvo = "госпожой"
                                    $ EmmaX.Petname_pre = "госпоже"
                                else:
                                    $ EmmaX.Petname = "господин"
                                    $ EmmaX.Petname_rod = "господина"
                                    $ EmmaX.Petname_dat = "господину"
                                    $ EmmaX.Petname_vin = "господина"
                                    $ EmmaX.Petname_tvo = "господином"
                                    $ EmmaX.Petname_pre = "господине"
                "Не надо меня так звать, ладно?":
                    $ EmmaX.FaceChange("confused", 2)
                    ch_e "Хмм."
                    $ EmmaX.Statup("Inbt", 50, -5)
                    $ EmmaX.FaceChange("sadside", 1)
                    menu:
                        ch_e ". . . но ты же будешь брать на себя инициативу?"
                        "Да, конечно.":
                                $ EmmaX.Statup("Obed", 200, 10)
                                $ EmmaX.FaceChange("smile", 1)
                                ch_e "Я рада, [EmmaX.Petname]."
                        "Мне от всего этого неловко.":
                                $ EmmaX.Statup("Love", 200, -10)
                                $ EmmaX.Statup("Obed", 200, -50)
                                $ EmmaX.Statup("Inbt", 50, -15)
                                $Line = "embarrassed"

#Emma_Sub_Bad_End:
        $ EmmaX.History.append("sir")
        if not Line:
                $ EmmaX.Blush = 1
                $ EmmaX.Petnames.append("sir")
                #put in stuff that happens if this succeeds
        elif Line == "rude":
                hide Emma_Sprite with easeoutright
                call Remove_Girl(EmmaX)
                $ renpy.pop_call()
                "[EmmaX.Name] в гневе выходит за дверь, оставляя вас в одиночестве."
        elif Line == "embarrassed":
                $ EmmaX.FaceChange("sad", 2)
                ch_e "Что ж, я. . . эм. . ."
                $ EmmaX.FaceChange("sly", 1)
                ch_e "Я тебя просто проверяла. Разумеется. Я не могу позволить себе выходить за рамки профессиональной этики."
                $ EmmaX.FaceChange("sadside", 2)
                ch_e "Мне пора идти. Кажется, я вижу студента, которому срочно необходима моя помощь."
                $ EmmaX.Blush = 1
                hide Emma_Sprite with easeoutright
                call Remove_Girl(EmmaX)
                $ renpy.pop_call()
                "[EmmaX.Name] выскакивает за дверь, оставляя вас в одиночестве."
        jump Misplaced
        return

label Emma_Sub_Asked: #Emma_Update
        $ Line = 0
        $ EmmaX.FaceChange("sadside", 1)
        call Shift_Focus(EmmaX)
        ch_e "Возможно."
        if not Player.Male:
            ch_e "Но также я вспомнила, что ты, кажется, не готова к подобной роли."
        else:
            ch_e "Но также я вспомнила, что ты, кажется, не готов к подобной роли."
        menu:
            extend ""
            "Извини. У меня еще есть возможность передумать?":
                    if "sir" in EmmaX.Petnames and ApprovalCheck(EmmaX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(EmmaX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            ch_e "Возможно, я смогу дать тебе еще шанс, когда ты немного разберешься в себе. . ." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ EmmaX.Statup("Love", 90, 10)
                            $ EmmaX.FaceChange("sly", 1)
                            ch_e "Полагаю, я могу дать тебе еще один шанс."
                            ch_e "Я рада, что ты признаешь свою ошибку."

            "Я знаю, что ты этого хочешь. Хочешь попробовать еще раз или нет?":
                    $ EmmaX.FaceChange("bemused", 1)
                    if "sir" in EmmaX.Petnames and ApprovalCheck(EmmaX, 850, "O"):
                            ch_e "Ладно."
                    elif not ApprovalCheck(EmmaX, 600, "O"):
                            ch_e "Нет. Не сейчас."
                            $ Line = "rude"
                    else:
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            $ EmmaX.FaceChange("sadside", 1)
                            ch_e "Ты испытываешь свою удачу."
                            $ EmmaX.Eyes = "squint"
                            if not Player.Male:
                                ch_e "Возможно, ты и права, но я считаю, что тебе стоит извиниться."
                            else:
                                ch_e "Возможно, ты и прав, но я считаю, что тебе стоит извиниться."
                            menu:
                                extend ""
                                "Ладно, извини, что я была так груба." if not Player.Male:
                                                $ EmmaX.Statup("Love", 90, 15)
                                                $ EmmaX.Statup("Inbt", 50, 10)
                                                $ EmmaX.FaceChange("bemused", 1, Eyes="side")
                                                ch_e "Извинения приняты. . ."
                                "Ладно, извини, что я был так груб." if Player.Male:
                                                $ EmmaX.Statup("Love", 90, 15)
                                                $ EmmaX.Statup("Inbt", 50, 10)
                                                $ EmmaX.FaceChange("bemused", 1, Eyes="side")
                                                ch_e "Извинения приняты. . ."
                                "Не дождешься.":
                                        if "sir" in EmmaX.Petnames and ApprovalCheck(EmmaX, 900, "O"):
                                                $ EmmaX.Statup("Love", 200, -5)
                                                $ EmmaX.Statup("Obed", 200, 10)
                                                ch_e ". . ."
                                        elif ApprovalCheck(EmmaX,650, "O"):
                                                $ EmmaX.Statup("Love", 200, -5)
                                                $ EmmaX.Statup("Obed", 200, 10)
                                                ch_e "Я- эм. . . хммм. . ."
                                        else: #if it failed both those things,
                                                $ EmmaX.Statup("Love", 200, -10)
                                                $ EmmaX.Statup("Obed", 90, -10)
                                                $ EmmaX.Statup("Obed", 200, -10)
                                                $ EmmaX.Statup("Inbt", 50, -15)
                                                "[EmmaX.Name] вздыхает и закатывает глаза."
                                                $ EmmaX.FaceChange("angry", 1, Eyes="side")
                                                if not Player.Male:
                                                    ch_e "Ты ничему так и не научилась, не так ли?"
                                                else:
                                                    ch_e "Ты ничему так и не научился, не так ли?"
                                                $ Line = "rude"
                                "Ладно, тогда забудь.":
                                                $ EmmaX.FaceChange("angry", 1)
                                                $ EmmaX.Statup("Love", 200, -10)
                                                $ EmmaX.Statup("Obed", 90, -10)
                                                $ EmmaX.Statup("Obed", 200, -10)
                                                $ EmmaX.Statup("Inbt", 50, -15)
                                                ch_e "Не знаю, что я в тебе вообще нашла."
                                                $ Line = "rude"

        $ EmmaX.RecentActions.append("asked sub")
        $ EmmaX.DailyActions.append("asked sub")
        if Line == "rude":
                #If line hasn't been set to "rude" by something above, then it skips right past this
                hide Emma_Sprite with easeoutright
                call Remove_Girl(EmmaX)
                $ EmmaX.RecentActions.append("angry")
                $ renpy.pop_call()
                "[EmmaX.Name] выходит за дверь, оставляя вас в одиночестве. Она выглядела очень расстроенной."
        elif "sir" in EmmaX.Petnames:
                #it didn't fail and "sir" was covered
                $ EmmaX.Statup("Obed", 200, 50)
                $ EmmaX.Petnames.append("master")
                if not Player.Male:
                    $ EmmaX.Petname = "хозяйка"
                    $ EmmaX.Petname_rod = "хозяйки"
                    $ EmmaX.Petname_dat = "хозяйке"
                    $ EmmaX.Petname_vin = "хозяйку"
                    $ EmmaX.Petname_tvo = "хозяйкой"
                    $ EmmaX.Petname_pre = "хозяйке"
                else:
                    $ EmmaX.Petname = "хозяин"
                    $ EmmaX.Petname_rod = "хозяина"
                    $ EmmaX.Petname_dat = "хозяину"
                    $ EmmaX.Petname_vin = "хозяина"
                    $ EmmaX.Petname_tvo = "хозяином"
                    $ EmmaX.Petname_pre = "хозяине"
                $ EmmaX.Eyes = "sly"
                if not Player.Male:
                    ch_e ". . . хозяйка. . ."
                else:
                    ch_e ". . . хозяин. . ."
        else:
                #it didn't fail
                $ EmmaX.Statup("Obed", 200, 30)
                $ EmmaX.Petnames.append("sir")
                if not Player.Male:
                    $ EmmaX.Petname = "госпожа"
                    $ EmmaX.Petname_rod = "госпожи"
                    $ EmmaX.Petname_dat = "госпоже"
                    $ EmmaX.Petname_vin = "госпожу"
                    $ EmmaX.Petname_tvo = "госпожой"
                    $ EmmaX.Petname_pre = "госпоже"
                else:
                    $ EmmaX.Petname = "господин"
                    $ EmmaX.Petname_rod = "господина"
                    $ EmmaX.Petname_dat = "господину"
                    $ EmmaX.Petname_vin = "господина"
                    $ EmmaX.Petname_tvo = "господином"
                    $ EmmaX.Petname_pre = "господине"

                $ EmmaX.Eyes = "sly"
                if not Player.Male:
                    ch_e ". . . госпожа."
                else:
                    ch_e ". . . господин."
        return

# end Emma_Sub//////////////////////////////////////////////////////////


# start Emma_Master//////////////////////////////////////////////////////////

label Emma_Master:  #Emma_Update
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(EmmaX,"bemused","выглядит необычайно покорной. . .")
                return
        $ EmmaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Shift_Focus(EmmaX)
        $ EmmaX.Loc = bg_current
        call Set_The_Scene
        if EmmaX.Loc != bg_current and EmmaX not in Party:
            "[EmmaX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить."
        else:
            "[EmmaX.Name] подходит к вам с явным желанием поговорить."
        $ Event_Queue = [0,0]
        call CleartheRoom(EmmaX)
        $ EmmaX.DailyActions.append("relationship")
        call Taboo_Level
        $ Line = 0
        $ EmmaX.FaceChange("bemused", 1)
        if len(Player.Harem) >= 1 and "loser" in EmmaX.History and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Loser
        if Player.Lvl >= 7 and "idiot" in EmmaX.History and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Idiot
        ch_e "[EmmaX.Petname], если ты не против, я начну. . ."
        ch_e "По правде говоря, я нахожу твою. . . настойчивость довольно. . ."
        ch_e ". . . возбуждающей."
        menu:
            extend ""
            "Мне тоже нравится.":
                    $ EmmaX.FaceChange("sly", 1)
                    ch_e "Хорошо, хорошо. . ."
                    ch_e "В таком случае, возможно, мы сможем. . ."
                    ch_e "Зайти немного дальше?"
                    menu:
                        extend ""
                        "Нет. Все и так идеально.":
                                $ EmmaX.FaceChange("sad", 1)
                                $ EmmaX.Statup("Obed", 200, -15)
                                $ EmmaX.Statup("Inbt", 50, 10)
                                if not Player.Male:
                                    ch_e "М? Пожалуй, ты права. . ."
                                else:
                                    ch_e "М? Пожалуй, ты прав. . ."
                                $ Line = "fail"
                        "Что ты имеешь в виду?":
                                $ EmmaX.Eyes = "side"
                                ch_e "Хм, что ж, я просто подумала, что, возможно, я могла бы обращаться к тебе. . ."
                                if not Player.Male:
                                    ch_e ". . . -хозяйка-?"
                                else:
                                    ch_e ". . . -хозяин-?"
                                $ EmmaX.Eyes = "squint"
                                ch_e "Как ты на это смотришь?"
                                menu:
                                    extend ""
                                    "О да. Мне нравится.":
                                            ch_e "Замечательно. . ."
                                    "Эм. . .нет.  Это слишком.":
                                            $ EmmaX.FaceChange("sad", 1)
                                            $ EmmaX.Statup("Obed", 200, -15)
                                            $ EmmaX.Statup("Inbt", 50, 5)
                                            ch_e "Ох. Хорошо, тогда забудь, что я сказала."
                                            ch_e "Забудь. . . забудь. . . "
                                            ch_e "Ох, не обращай внимания, я забыла, что это на тебя не действует."
                                            if not Player.Male:
                                                ch_e "Просто будь осторожна."
                                            else:
                                                ch_e "Просто будь осторожен."
                                            $ Line = "fail"

                        "Честно говоря, я предпочла бы быть менее властной." if not Player.Male:
                                $ EmmaX.FaceChange("sly", 1)
                                $ EmmaX.Statup("Love", 200, 15)
                                $ EmmaX.Statup("Obed", 200, -10)
                                $ EmmaX.Statup("Inbt", 50, 10)
                                ch_e "Что ж, полагаю, ты должна быть верна себе. . ."
                                $ Line = "fail"

                        "Честно говоря, я предпочел бы быть менее властной." if Player.Male:
                                $ EmmaX.FaceChange("sly", 1)
                                $ EmmaX.Statup("Love", 200, 15)
                                $ EmmaX.Statup("Obed", 200, -10)
                                $ EmmaX.Statup("Inbt", 50, 10)
                                ch_e "Что ж, полагаю, ты должна быть верна себе. . ."
                                $ Line = "fail"

                        "Знаешь, давай все это прекратим. Меня это начинает пугать.":
                                $ EmmaX.FaceChange("perplexed", 2)
                                $ EmmaX.Statup("Love", 200, -10)
                                $ EmmaX.Statup("Obed", 200, -50)
                                $ EmmaX.Statup("Inbt", 50, -15)
                                ch_e "Что ж. Мне бы не хотелось пугать тебя."
                                $ EmmaX.Blush = 1
                                $ Line = "embarrassed"

            "Будто меня волнует твое мнение, шлюха.":
                    $ EmmaX.FaceChange("angry", 1)
                    $ EmmaX.Statup("Love", 200, -20)
                    $ EmmaX.Statup("Obed", 200, 10)
                    $ EmmaX.Statup("Inbt", 50, -10)
                    menu:
                        ch_e "Что это было?"
                        "Извиняюсь. Мне просто все равно, чего ты хочешь.":
                                if ApprovalCheck(EmmaX, 1400, "LO"):
                                        $ EmmaX.Statup("Obed", 200, 10)
                                        ch_e "Что-то. . ."
                                        $ EmmaX.FaceChange("sly", 1)
                                        $ EmmaX.Statup("Love", 200, 20)
                                        $ EmmaX.Statup("Inbt", 50, 15)
                                        ch_e ". . .у меня пошло не по плану."
                                else:
                                        $ EmmaX.Statup("Love", 200, -15)
                                        $ EmmaX.Statup("Obed", 200, -10)
                                        $ EmmaX.Statup("Inbt", 50, 5)
                                        $ EmmaX.FaceChange("angry", 1)
                                        ch_e "!!!"
                                        $ Line = "rude"

                        "Извини. Я просто пытаюсь быть более -властной-. Я думала тебе понравится. Это перебор?" if not Player.Male:
                                $ EmmaX.Statup("Love", 200, 10)
                                $ EmmaX.Statup("Obed", 200, 10)
                                $ EmmaX.Statup("Inbt", 50, 5)
                                ch_e "Тебе. . . просто надо немного поработать над этим."

                        "Извини. Я просто пытаюсь быть более -властным-. Я думал тебе понравится. Это перебор?" if Player.Male:
                                $ EmmaX.Statup("Love", 200, 10)
                                $ EmmaX.Statup("Obed", 200, 10)
                                $ EmmaX.Statup("Inbt", 50, 5)
                                ch_e "Тебе. . . просто надо немного поработать над этим."

            "Но не я. Это до жути странно.":
                        $ EmmaX.FaceChange("sad", 2)
                        $ EmmaX.Statup("Love", 200, -10)
                        $ EmmaX.Statup("Obed", 200, -20)
                        $ EmmaX.Statup("Inbt", 50, -25)
                        ch_e "Ох. Что ж, я не хочу, чтобы тебе было некомфортно. . ."
                        $ Line = "embarrassed"

        $ EmmaX.History.append("master")
        if Line == "rude":
                $ EmmaX.RecentActions.append("angry")
                call Remove_Girl(EmmaX)
                $ renpy.pop_call()
                "[EmmaX.Name] в гневе вылетает за дверь."
        elif Line == "embarrassed":
                call Remove_Girl(EmmaX)
                $ renpy.pop_call()
                "[EmmaX.Name] выскакивает из комнаты, оставляя вас в одиночестве. Она выглядела очень смущенной."
        elif Line != "fail":
                $ EmmaX.Statup("Obed", 200, 50)
                $ EmmaX.Petnames.append("master")
                if not Player.Male:
                    $ EmmaX.Petname = "хозяйка"
                    $ EmmaX.Petname_rod = "хозяйки"
                    $ EmmaX.Petname_dat = "хозяйке"
                    $ EmmaX.Petname_vin = "хозяйку"
                    $ EmmaX.Petname_tvo = "хозяйкой"
                    $ EmmaX.Petname_pre = "хозяйке"
                else:
                    $ EmmaX.Petname = "хозяин"
                    $ EmmaX.Petname_rod = "хозяина"
                    $ EmmaX.Petname_dat = "хозяину"
                    $ EmmaX.Petname_vin = "хозяина"
                    $ EmmaX.Petname_tvo = "хозяином"
                    $ EmmaX.Petname_pre = "хозяине"
                if not Player.Male:
                    $ EmmaX.Petname = "хозяйка"
                    ch_e ". . .хозяйка."
                else:
                    $ EmmaX.Petname = "хозяин"
                    ch_e ". . .хозяин."
        return

# end Emma_Master//////////////////////////////////////////////////////////


# start Emma_Sexfriend//////////////////////////////////////////////////////////

label Emma_Sexfriend:   #Emma_Update
#        if bg_current == "bg classroom" and (EmmaX.Loc == "bg teacher" or EmmaX.Loc == "bg classroom"):
#                call Emma_Sexfriend
#                return

        $ Event_Queue = [0,0]
        $ EmmaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        #set this to occur after class
        if EmmaX in Player.Harem:
                $ EmmaX.Petnames.append("sex friend")
                return
        $ EmmaX.Loc = bg_current
        call Shift_Focus(EmmaX)
        call Set_The_Scene
        call CleartheRoom(EmmaX,1,1)
        $ EmmaX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in EmmaX.History:
                call expression EmmaX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                return
        call Taboo_Level
        $ Line = 0
        "После занятия студенты толпой выходят из аудитории."
        $ EmmaX.FaceChange("bemused", 1)
        ch_e "[Player.Name], мы можем поговорить?" #blushing expression
        menu:
                extend ""
                "Я спешу.":
                        $ EmmaX.FaceChange("angry", 1)
                        ch_e "Это. . . неверный ответ." #Angry expression.  Loss of points
                        $ EmmaX.Statup("Love", 200, -20)
                        $ EmmaX.Statup("Obed", 50, 3)
                        $ Line = "rude"

                "Мне уже не нравится этот разговор.":
                        $ EmmaX.FaceChange("sly", 1)
                        ch_e "Успокойся, не будет ничего. . . неприятного."

                "Да. Что случилось?":
                        pass

        if not Line: #all this gets skipped if the "rude" response was procced above
                if ApprovalCheck(EmmaX, 850, "L"):
                        $ EmmaX.FaceChange("sly", 1)
                        ch_e "Ты же знаешь, что мне очень нравится проводить с тобой время?"
                        menu:
                            extend ""
                            "Конечно.":
                                    $ EmmaX.FaceChange("sexy", 1)
                                    $ EmmaX.Statup("Love", 90, 10)
                                    $ EmmaX.Statup("Inbt", 80, 5)
                                    ch_e "Я надеялась, что ты так скажешь, [EmmaX.Petname]."
                            "Правда?":
                                    $ EmmaX.FaceChange("perplexed", 1)
                                    ch_e "Эм, да." #Blushing expression

                            "Не усложняй все.":
                                    $ EmmaX.FaceChange("angry", 1)
                                    $ EmmaX.Statup("Love", 200, -10)
                                    $ EmmaX.Statup("Obed", 50, 5)
                                    $ EmmaX.Statup("Inbt", 80, -5)
                                    ch_e "Жаль, что ты думаешь, словно я все \"усложняю.\""
                                    $ Line = "rude"
                elif ApprovalCheck(EmmaX, 1000, "LI"):
                        $ EmmaX.FaceChange("sexy", 1)
                        if not Player.Male:
                            ch_e "Я просто подумала, что ты должна знать, что. . . ты мне интересна."
                        else:
                            ch_e "Я просто подумала, что ты должен знать, что. . . ты мне интересен."
                        menu:
                            extend ""
                            "Очень мило с твоей стороны.":
                                    $ EmmaX.Statup("Love", 80, 5)
                                    $ EmmaX.Statup("Inbt", 80, 5)
                                    ch_e "Разумеется." #Blushing expression
                            "Я? Ты правда так думаешь?":
                                    if not Player.Male:
                                        ch_e "Не будь такой скромной, [EmmaX.Petname]." #Blushing expression
                                    else:
                                        ch_e "Не будь таким скромным, [EmmaX.Petname]." #Blushing expression
                            "Ты к чему-то клонишь?":
                                    $ EmmaX.FaceChange("angry")
                                    ch_e "Видимо, уже нет." #Angry expression.  Loss of points
                                    $ Line = "rude"
                else: #if it reaches this block, it's because it failed the "like" check above.
                        $ EmmaX.Mouth = "smile"
                        $ EmmaX.Brows = "sad"
                        $ EmmaX.Eyes = "side"
                        ch_e "Это может прозвучать немного. . . странно."
                        menu:
                            extend ""
                            "Что ж, ты меня заинтриговала. Теперь ты просто обязана мне все рассказать.":
                                ch_e "Обещаешь, что разговор останется только между нами?"
                                menu:
                                    extend ""
                                    "[EmmaX.Name]. . . Ты мне очень нравишься. Обещаю.":
                                            $ EmmaX.FaceChange("smile")
                                            $ EmmaX.Statup("Love", 90, 10)
                                            $ EmmaX.Statup("Inbt", 80, 5)
                                            ch_e "Отлично. . ."
                                    "Эм. . . ладно?":
                                            ch_e "Что ж. . ."
                                    "Ничего не обещаю.":
                                            $ EmmaX.FaceChange("perplexed",2)
                                            $ EmmaX.Statup("Inbt", 80, -5)
                                            ch_e "Хмм. . . тогда забудь."
                                            $ Line = "embarrassed"
                            "Эм, думаю я сыта по горло всякими {i}странностями{/i}, спасибо." if not Player.Male:
                                            $ EmmaX.FaceChange("angry",1)
                                            ch_e "Тогда живи в неведении."
                                            $ Line = "rude"
                            "Эм, думаю я сыт по горло всякими {i}странностями{/i}, спасибо." if Player.Male:
                                            $ EmmaX.FaceChange("angry",1)
                                            ch_e "Тогда живи в неведении."
                                            $ Line = "rude"

        if not Line:
                ch_e "Я тут подумала. . . "
                ch_e "Возможно, мы могли бы продвинуться дальше в наших отношениях, если ты, конечно, этого хочешь."
                menu:
                    extend ""
                    "Ты намекаешь на. . . {i}секс без обязательств{/i}?":
                            ch_e "Полагаю, можно сказать и так."
                            ch_e "Что думаешь?" #Blushing expression
                            menu:
                                extend ""
                                "Звучит потрясающе! Я за.":
                                            $ EmmaX.FaceChange("smile",1)
                                            $ EmmaX.Statup("Love", 80, 10)
                                            $ EmmaX.Statup("Obed", 50, 10)
                                            $ EmmaX.Statup("Inbt", 200, 50)
                                            $ EmmaX.Statup("Lust", 200, 5)
                                            "[EmmaX.Name] наклоняется и одаривает вас страстным поцелуем."
                                            $ EmmaX.Kissed += 1
                                            ch_e "Не могу дождаться, когда мы начнем, [EmmaX.Petname]."
                                "Это слишком развратно, [EmmaX.Name].":
                                        if ApprovalCheck(EmmaX, 2000):
                                            $ EmmaX.FaceChange("angry",1,Brows="confused")
                                            $ EmmaX.Statup("Love", 200, -10)
                                            $ EmmaX.Statup("Obed", 50, 15)
                                            if not Player.Male:
                                                ch_e "Полагаю, ты права."
                                            else:
                                                ch_e "Полагаю, ты прав."
                                        else:
                                            $ EmmaX.FaceChange("angry",1)
                                            $ EmmaX.Statup("Love", 200, -30)
                                            $ EmmaX.Statup("Obed", 50, 10)
                                            $ EmmaX.Statup("Inbt", 80, -20)
                                            ch_e "Тогда, думаю, мне придется предложить это кому-нибудь еще!"
                                            $ Line = "rude"
                    "Если честно, мне бы этого не хотелось.":
                                            $ EmmaX.FaceChange("sadside",2)
                                            $ EmmaX.Statup("Obed", 50, 15)
                                            $ EmmaX.Statup("Inbt", 80, -15)
                                            if not Player.Male:
                                                ch_e "Ох. Полагаю, свой выбор ты сделала."
                                            else:
                                                ch_e "Ох. Полагаю, свой выбор ты сделал."
                                            ch_e "Я должна уйти."
                                            $ Line = "sad"

        if Line == "rude":
                $ EmmaX.FaceChange("angry",1)
                $ EmmaX.RecentActions.append("angry")
                $ EmmaX.Statup("Love", 200, -20)
                $ EmmaX.Statup("Obed", 50, 5)
                $ EmmaX.Statup("Inbt", 80, -10)
                hide Emma_Sprite with easeoutright
                $ EmmaX.RecentActions.append("angry")
                "[EmmaX.Name] в гневе уносится прочь. Она выглядела очень злой."
        elif Line == "embarrassed":
                $ EmmaX.FaceChange("perplexed",1)
                $ EmmaX.Statup("Love", 200, -10)
                $ EmmaX.Statup("Obed", 50, 5)
                $ EmmaX.Statup("Inbt", 80, -20)
                hide Emma_Sprite with easeoutright
                "[EmmaX.Name] выскакивает из комнаты, оставляя вас в одиночестве. Это было очень странно."
        elif Line == "sad":
                hide Emma_Sprite with easeoutbottom
                "[EmmaX.Name] выходит в коридор, оставляя вас в одиночестве. Вы предполагаете, что могли задеть ее чувства."
        else: #if you kept Line unused throughout, then you passed all the checks, so. . .
                $ EmmaX.Petnames.append("sex friend")
                $ EmmaX.FaceChange("sly",2)
                $ EmmaX.Statup("Inbt", 80, 10)
                $ EmmaX.Statup("Lust", 80, 10)
                "[EmmaX.Name] наклоняется и обнимает вас."
                if Player.Male:
                        "Когда она это делает, вы чувствуете, словно ее рот касается вашего член."
                else:
                        "Когда она это делает, вы чувствуете, словно ее рот касается вашей киски."
                "Вы непонимающе смотрите на нее, и она вам подмигивает."
                ch_e "У меня припрятано пара тузов в рукаве, [EmmaX.Petname]."
                ch_e "Надеюсь, скоро увидимся."
                hide Emma_Sprite with easeoutright
                "Она выходит из комнаты, и фантомные \"губы\" дарят вам последний поцелуй. "
        call Remove_Girl(EmmaX)
        jump Misplaced

# end Emma_Sexfriend//////////////////////////////////////////////////////////


# start Emma_Fuckbuddy//////////////////////////////////////////////////////////

label Emma_Fuckbuddy:   #Emma_Update
        $ Event_Queue = [0,0]
        $ EmmaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ EmmaX.DailyActions.append("relationship")
        if Player.Male:
                "Ни с того ни с сего, вы чувствуете, словно язык облизывает ваш член."
                "Несмотря на то, что вы полностью одеты, вы абсолютно уверены, что чей-то рот ласкает ваш член."
                "Вы смотрите вниз, но ничего не видите, хотя ваш член стал твердым подобно алмазу."
                "Пока вы пытаетесь совладать со своей очевидной эрекцией, в вашей голове возникает знакомый голос,"
        else:
                "Ни с того ни с сего, вы чувствуете, словно язык облизывает вашу киску."
                "Несмотря на то, что вы полностью одеты, вы абсолютно уверены, что чей-то рот ласкает вашу киску."
                "Вы смотрите вниз, но ничего не видите, хотя ваш клитор стал твердым подобно алмазу."
                "Пока вы пытаетесь совладать со своим очевидным возбуждением, в вашей голове возникает знакомый голос,"
        ch_e "Ко мне, мой Человек-Икс. . ."
        "-и воздействие резко пропадает."
        "Вы оглядываетесь вокруг, но не видите никого поблизости, и похоже, никто ничего не заметил."
        "Возможно, в ближайшее время вам стоит навестить [EmmaX.Name_vin]. . ."
        $ EmmaX.Petnames.append("fuck buddy")
        $ EmmaX.Event[10] += 1
        return
# end Emma_Fuckbuddy//////////////////////////////////////////////////////////

# start Emma_Daddy//////////////////////////////////////////////////////////

label Emma_Daddy:       #Emma_Update
        $ Event_Queue = [0,0]
        $ EmmaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ EmmaX.DailyActions.append("relationship")
        call Shift_Focus(EmmaX)
        if EmmaX.Loc != bg_current:
                $ EmmaX.Loc = bg_current
                "[EmmaX.Name] подходит к вам."
        call Set_The_Scene
        ch_e ". . ."
        if len(Player.Harem) >= 1 and "loser" in EmmaX.History and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Loser
        if Player.Lvl >= 7 and "idiot" in EmmaX.History and "first" not in EmmaX.DailyActions:
            #calls action if she mocked you in first appearance
            call Emma_Idiot
        if EmmaX in Player.Harem:
            ch_e "[EmmaX.Petname], мы уже давно встречаемся,"
        else:
            ch_e "Мы уже давно наслаждаемся обществом друг друга,"
        if EmmaX.Love > EmmaX.Obed and EmmaX.Love > EmmaX.Inbt:
            if not Player.Male:
                ch_e "и ты очень милая. . ."
            else:
                ch_e "и ты очень милый. . ."
        elif EmmaX.Obed > EmmaX.Inbt:
            ch_e "и ты знаешь, как меня заинтересовать. . ."
        else:
            ch_e "и я провела много. . . исследований. . ."
        if not Player.Male:
            ch_e "Так вот, я тут подумала, ты ведь не будешь возражать, если я буду звать тебя \"мамочкой?\""
        else:
            ch_e "Так вот, я тут подумала, ты ведь не будешь возражать, если я буду звать тебя \"папочкой?\""
        menu:
            extend ""
            "Хорошо, я не против.":
                $ EmmaX.FaceChange("smile")
                $ EmmaX.Statup("Love", 90, 20)
                $ EmmaX.Statup("Obed", 60, 10)
                $ EmmaX.Statup("Inbt", 80, 30)
                ch_e "Замечательно."
            "Что ты имеешь в виду?":
                $ EmmaX.FaceChange("bemused")
                ch_e "Меня возбуждает, когда я представляю себя твоей доченькой. . ."
                if not Player.Male:
                    ch_e "Я бы хотела иногда звать тебя \"мамочкой\"."
                else:
                    ch_e "Я бы хотела иногда звать тебя \"папочкой\"."
                menu:
                    extend ""
                    "Звучит интересно, мне нравится.":
                        $ EmmaX.FaceChange("smile")
                        $ EmmaX.Statup("Love", 90, 15)
                        $ EmmaX.Statup("Obed", 60, 20)
                        $ EmmaX.Statup("Inbt", 80, 25)
                        ch_e "Отлично!"
                        $ EmmaX.FaceChange("sly",2)
                        if not Player.Male:
                            ch_e " . . . мамочка."
                        else:
                            ch_e " . . . папочка."
                        $ EmmaX.FaceChange("sly",1)
                        if not Player.Male:
                            $ EmmaX.Petname = "мамочка"
                            $ EmmaX.Petname_rod = "мамочки"
                            $ EmmaX.Petname_dat = "мамочке"
                            $ EmmaX.Petname_vin = "мамочку"
                            $ EmmaX.Petname_tvo = "мамочкой"
                            $ EmmaX.Petname_pre = "мамочке"
                        else:
                            $ EmmaX.Petname = "папочка"
                            $ EmmaX.Petname_rod = "папочки"
                            $ EmmaX.Petname_dat = "папочке"
                            $ EmmaX.Petname_vin = "папочку"
                            $ EmmaX.Petname_tvo = "папочкой"
                            $ EmmaX.Petname_pre = "папочке"
                    "Можешь, пожалуйста, так меня не звать?":
                        $ EmmaX.Statup("Love", 90, 5)
                        $ EmmaX.Statup("Obed", 80, 40)
                        $ EmmaX.Statup("Inbt", 80, 20)
                        $ EmmaX.FaceChange("sad")
                        ch_e "   . . .   "
                        ch_e "Что ж, ладно."
                    "У тебя были непростые отношения с отцом, да?" if Player.Male:
                        $ EmmaX.Statup("Love", 90, -15)
                        $ EmmaX.Statup("Obed", 80, 45)
                        $ EmmaX.Statup("Inbt", 70, 5)
                        $ EmmaX.FaceChange("angry")
                        ch_e "Давай не будем вдаваться в подробности."
                    "У тебя были непростые отношения с мамой, да?" if not Player.Male:
                        $ EmmaX.Statup("Love", 90, -15)
                        $ EmmaX.Statup("Obed", 80, 45)
                        $ EmmaX.Statup("Inbt", 70, 5)
                        $ EmmaX.FaceChange("angry")
                        ch_e "Давай не будем вдаваться в подробности."
            "Разве ты не слишком стара для этого?":
                        $ EmmaX.Statup("Love", 90, -15)
                        $ EmmaX.Statup("Obed", 80, 40)
                        $ EmmaX.Statup("Inbt", 70, 10)
                        $ EmmaX.FaceChange("angry")
                        ch_e "Похоже, это была плохая идея."
        $ EmmaX.Petnames.append("daddy")
        return

# end Emma_Daddy//////////////////////////////////////////////////////////


# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        call LastNamer
        if "switched" in EmmaX.History:
                jump Emma_Switch2
        $ EmmaX.FaceChange("smile", 1)
        ch_e "Здравствуй?"
        ch_e "Ох. . . [Player.Name]."
        menu:
            extend ""
            "Ага, это я, [Player.Name].":
                    $ EmmaX.FaceChange("confused", 1)
                    ch_e "Я знаю."
                    $ EmmaX.FaceChange("smile", 1)
                    ch_e "Несмотря на кардинальные изменения в твоей внешности."
                    $ EmmaX.AddWord(1,"switch") #recent

            "Нет.":
                    $ EmmaX.FaceChange("confused", 1)
                    ch_e "Нет смысла притворяться."
                    $ EmmaX.FaceChange("smile", 1)
                    if not Player.Male:
                        ch_e "Я телепат, дорогая."
                    else:
                        ch_e "Я телепат, дорогой."
            "Может быть?":
                    $ EmmaX.FaceChange("confused", 1)
                    ch_e "О боже, должно быть, все гораздо серьезнее, чем я думала."

        if "switch" not in EmmaX.RecentActions:
                    ch_e "К чему эти попытки обмануть меня?"
                    $ EmmaX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Извини, хотелось пошутить.":
                                $ EmmaX.FaceChange("sly", 1)
                                $ EmmaX.Statup("Love", 70, 1)
                                ch_e "Ох, с натяжкой это и правда можно назвать \"шуткой.\" . ."
                        "Молодец, ты все поняла.":
                                $ EmmaX.FaceChange("sly", 1)
                                $ EmmaX.Statup("Obed", 70, 1)
                                $ EmmaX.Statup("Inbt", 80, 1)
                                if not Player.Male:
                                    ch_e "Ты правда думала, что у тебя получится обмануть меня?"
                                else:
                                    ch_e "Ты правда думал, что у тебя получится обмануть меня?"
                        "Хех.":
                                $ EmmaX.FaceChange("sadside", 1)
                                $ EmmaX.Statup("Love", 70, 1)
                                $ EmmaX.Statup("Love", 90, 1)
                                $ EmmaX.Statup("Inbt", 70, 1)
                                ch_e "Ах, как смешно. . ."
        #end "tried to lie"
        $ EmmaX.FaceChange("smile", 1)
        if not Player.Male:
            ch_e "Почему ты вообще пошла на эти. . . изменения?"
        else:
            ch_e "Почему ты вообще пошел на эти. . . изменения?"
        menu:
            extend ""
            "Да так, по приколу.":
                    $ EmmaX.Statup("Inbt", 70, 1)
                    $ EmmaX.FaceChange("surprised", 2)
                    ch_e "Что ж, дело твое, не мне давать тебе советы. . ."
                    $ EmmaX.FaceChange("sly", 1)
            "Я так себя сейчас ощущаю.":
                    ch_e "Хорошо, я понимаю."
            "У меня не было каких-то особых причин.":
                    ch_e "Ясно, значит захотелось экспериментов. . ."

        if [Player.Name] != [Player.XName]:
                ch_p "А еще теперь меня зовут [Player.Name_tvo]."
                ch_e "Да, я как раз хотела спросить тебя об этом."

        if EmmaX.SEXP >= 15:
                $ EmmaX.FaceChange("sad", 1,Mouth="smile")
                ch_e "Эти. . . изменения, как-то влияют на нашу договоренность?"
                menu:
                    extend ""
                    "Нет!":
                            $ EmmaX.FaceChange("smile", 1)
                            $ EmmaX.Statup("Love", 70, 2)
                            $ EmmaX.Statup("Love", 90, 1)
                            ch_e "Рада это слышать. . ."
                    "Вроде как.":
                            $ EmmaX.FaceChange("sad", 1)
                            $ EmmaX.Statup("Love", 80, -2)
                            $ EmmaX.Statup("Obed", 60, 2)
                            $ EmmaX.Statup("Obed", 80, 2)
                            ch_e "Ах. . ."
                            $ EmmaX.FaceChange("sadside", 1)
                            ch_e "Ясно. . ."
                            if ApprovalCheck(EmmaX, 1500):
                                    $ EmmaX.FaceChange("sadside", 1,Mouth="smirk")
                                    ch_e "Но я должна сама в этом убедиться. . ."
                    "А ты как думаешь?":
                            $ EmmaX.FaceChange("sly", 1)
                            $ EmmaX.Statup("Obed", 70, 1)
                            $ EmmaX.Statup("Inbt", 70, 1)
                            ch_e "Я думаю. . . тебе интересны новые ощущения. . ."

        if ApprovalCheck(EmmaX, 1500):
                ch_e "Я ожидаю, что ты достаточно скоро освоишься в новом теле. . ."
                $ EmmaX.AddWord(1,0,0,0,"girltalk") #history
        else:
                $ EmmaX.FaceChange("normal", 1,Eyes="side")
                ch_e "Я дам тебе немного времени, чтобы разобраться в себе. . ."
        $ EmmaX.Traits.remove("switchcheck")
        $ EmmaX.AddWord(1,0,0,0,"switched") #history
        return

label Emma_Switch2:
        #when you switch for a 2+ time
        $ EmmaX.FaceChange("smile", 1)
        if not Player.Male:
            ch_e "Я вижу, ты вернулась к своему прежнему облику."
        else:
            ch_e "Я вижу, ты вернулся к своему прежнему облику."
        ch_e "Тебе идет."
        $ EmmaX.Traits.remove("switchcheck")
        $ EmmaX.History.remove("switched")
        $ EmmaX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_Girltalk(Auto=0,Other=0):
        # if Auto Emma starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in EmmaX.History:
                return
        if "nogirls" in EmmaX.History:
                jump Emma_Girltalk_Redux
        if Auto:
                $ EmmaX.FaceChange("sadside", 2)
                ch_e "Мне любопытно, [Player.Name]. . ."
                ch_e "Я тебе нравлюсь?"


        else:
                $ EmmaX.FaceChange("confused", 1)
                ch_e "Ох, значит, я тебе нравлюсь?"
        menu:
            extend ""
            "Да?":
                    $ EmmaX.FaceChange("sly", 1)
                    $ EmmaX.Statup("Love", 70, 2)
                    $ EmmaX.Statup("Love", 90, 2)
                    ch_e "Конечно. . ."
                    $ Auto = 0
            "Наверное?":
                    $ EmmaX.FaceChange("smile", 1)
                    $ EmmaX.Statup("Obed", 80, 2)
                    $ EmmaX.Statup("Inbt", 80, 2)
                    ch_e "Такой уклончивый ответ. . ."
                    $ EmmaX.FaceChange("sly", 1)
            "Не особо.":
                    $ EmmaX.FaceChange("sly", 1)
                    $ EmmaX.Statup("Obed", 60, 2)
                    $ EmmaX.Statup("Obed", 80, 2)
                    ch_e "Ясно. . ."
        ch_e "Что ж, я нахожу тебя привлекательной. . ."
        if not Auto:
                ch_e "Я ожидаю, что ты не будешь руководствоваться своими желаниями, как парни из твоей группы."
                ch_e "В то же время тебе не стоит полностью их. . . игнорировать. . ."
        if not ApprovalCheck(EmmaX, 1000):
                $ EmmaX.FaceChange("sad", 1)
                ch_e "Хотя ты и прекрасна, но в данный момент я не ищу подобных отношений. . ."
                $ EmmaX.AddWord(1,0,0,0,"nogirls") #history
                call Girltalk_Check(EmmaX)
                return
        ch_e "Знаешь, в прошлом у меня был некий опыт общения с прекрасным полом. . ."
        ch_e "Он может быть. . . весьма полезным."
        $ EmmaX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(EmmaX)
        return

label Emma_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing
        if ApprovalCheck(EmmaX, 1000):
                $ EmmaX.FaceChange("sly", 1)
                if Other in TotalGirls and "nogirls" in Other.History:
                        ch_e "Я не уверена. . ."
                ch_e "Ох, хорошо. . ."
                ch_e "Знаешь, в прошлом у меня был некий опыт общения с прекрасным полом. . ."
                ch_e "Он может быть. . . весьма полезным."
                $ EmmaX.DrainWord("nogirls",0,0,0,1) #history
                $ EmmaX.AddWord(1,0,0,0,"girltalk") #history
        elif "nogirls" not in EmmaX.History:
                $ EmmaX.AddWord(1,0,0,0,"nogirls") #history
                $ EmmaX.FaceChange("sad", 1)
                ch_e "Хотя ты и прекрасна, но в данный момент я не ищу подобных отношений. . ."
        elif "nogirls" in EmmaX.DailyActions:
                $ EmmaX.FaceChange("angry", 1)
                if EmmaX.Forced:
                        #if Forced, she will just go with it anyway
                        if "nogirls" not in EmmaX.RecentActions:
                                $ EmmaX.Statup("Love", 80, -2)
                                $ EmmaX.Statup("Obed", 80, 2)
                                $ EmmaX.AddWord(1,"nogirls",0,0,0) #recent
                        return
                ch_e "Не переусердствуй. . ."
        else:
                $ EmmaX.Statup("Inbt", 50, 2)
                ch_e "Ты прекрасна, но в данный момент я не ищу подобные отношения. . ."
                $ EmmaX.AddWord(1,0,"nogirls",0,0) #daily
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_69_Intro:
        if "69" in EmmaX.History:
                return
        if Trigger == "lick pussy" and EmmaX.LickP:
                if EmmaX.Blow or EmmaX.CUN or (ApprovalCheck(EmmaX, 1300) and EmmaX.SeenPeen):
                        #if licking pussy but have gotten blowjob
                        $ EmmaX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_e "Я не люблю быть в долгу. . ."
                        "Она прижимает вас к полу и забирается на вас сверху."
                        if "cockout" not in Player.RecentActions:
                                $ Player.RecentActions.append("cockout")
                                if Player.Male:
                                        "Она вытаскивает ваш член и начинает его сосать."
                                else:
                                        "Она обнажает вашу киску и начинает лизать ее."
                        else:
                                if Player.Male:
                                        "Она берет в руки ваш член и располагается над ним."
                                else:
                                        "Она начинает лизать вашу киску."
                        $ EmmaX.Pose = "69"
                        call Emma_BJ_Launch
                        ch_e "Продолжай, [EmmaX.Petname] . ."
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ EmmaX.Statup("Love", 95, 3)
                                    $ EmmaX.Statup("Inbt", 70, 2)
                                    $ EmmaX.Statup("Inbt", 90, 1)
                                    ch_e "Прекрасно."
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ EmmaX.Statup("Love", 80, -8)
                                    $ EmmaX.Statup("Obed", 80, 3)
                                    $ EmmaX.Statup("Obed", 90, 1)
                                    $ EmmaX.Statup("Inbt", 70, -1)
                                    ch_e "Очень жаль."
                        $ Situation = "69"
                        call SexAct("blow") # call Emma_SexAct("blow")
                        $ renpy.pop_call() #causes it to skip past the Escalation
                        $ renpy.pop_call() #causes it to skip past the last activity
        elif (Trigger == "blow" or Trigger == "cun") and (EmmaX.Blow or EmmaX.CUN):
                        #if licked pussy
                        $ EmmaX.AddWord(1,0,0,0,"69") #history
                        $ Player.AddWord(1,0,0,0,"69")
                        ch_e "Пока я делаю тебе приятно. . ."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        $ EmmaX.Pose = "69"
                        call Emma_BJ_Launch
                        if Player.Male:
                            ch_e ". . .не мог бы ты отплатить мне тем же? . ."
                        else:
                            ch_e ". . .не могла бы ты отплатить мне тем же? . ."
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ EmmaX.Statup("Love", 95, 3)
                                    $ EmmaX.Statup("Inbt", 70, 2)
                                    $ EmmaX.Statup("Inbt", 90, 1)
                                    ch_e "Прекрасно."
                                    if not EmmaX.LickP:
                                        $ EmmaX.LickP += 1
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ EmmaX.Statup("Love", 80, -5)
                                    $ EmmaX.Statup("Obed", 80, 3)
                                    $ EmmaX.Statup("Obed", 90, 1)
                                    $ EmmaX.Statup("Inbt", 70, -1)
                                    ch_e "Очень жаль."
                        #returns to BJ already in progress
        return

label Emma_Loser:
        #called when she mocks you when first meeting, but changes her impression of you.
        ch_e "Боюсь, я недооценила тебя."
        ch_e "Когда мы впервые встретились, я пренебрегла твоим обаянием."
        $ EmmaX.Statup("Love", 90, 5)
        $ EmmaX.Statup("Obed", 90, 10)
        if not Player.Male:
            ch_e "Но теперь все ясно — ты начинала раскрываться."
        else:
            ch_e "Но теперь все ясно — ты начинал раскрываться."
        $ EmmaX.Statup("Love", 200, 5)
        $ EmmaX.Statup("Inbt", 200, 10)
        $ EmmaX.Statup("Lust", 50, 5)
        ch_e "Даже я не устояла. . ."
        $ EmmaX.AddWord(1,0,"first",0,0) #adds "word" to Daily
        $ EmmaX.DrainWord("loser",0,0,0,1) # removes from history
        return
label Emma_Idiot:
        #called when she mocks you when first meeting, but changes her impression of you.
        ch_e "Должна отдать тебе должное, я недооценила твои способности, когда мы впервые встретились."
        $ EmmaX.Statup("Love", 80, 2)
        $ EmmaX.Statup("Obed", 200, 5)
        if not Player.Male:
            ch_e "Ты усердной работой добилась многого."
        else:
            ch_e "Ты усердной работой добился многого."
        $ EmmaX.Statup("Love", 90, 3)
        $ EmmaX.Statup("Obed", 200, 3)
        ch_e "Я горжусь тем, что являюсь одной из твоих преподавателей."
        $ EmmaX.AddWord(1,0,"first",0,0) #adds "word" to Daily
        $ EmmaX.DrainWord("idiot",0,0,0,1) # removes from history
        return


label Emma_and_Storm_Redux:
        #launch conditions,if Time_Count == 2 and "EmmaStormQueue" in EmmaX.Traits and bg_current != "bg classroom" and not Party
        # if "EmmaStorm" in EmmaX.History and "EmmaStorm" not in EmmaX.DailyActions:, add queue if you get caught doing stuff.
        if EmmaX.Loc == bg_current:
                "[EmmaX.Name] резко поворачивается к вам."
                if not Player.Male:
                    ch_e "[EmmaX.Petname], не могла бы ты, пожалуйста, явиться в аудиторию?"
                else:
                    ch_e "[EmmaX.Petname], не мог бы ты, пожалуйста, явиться в аудиторию?"
        else:
                "Вы получаете звонок от [EmmaX.Name_rod]."
                if not Player.Male:
                    ch_e "[EmmaX.Petname], не могла бы ты, пожалуйста, явиться в аудиторию?"
                else:
                    ch_e "[EmmaX.Petname], не мог бы ты, пожалуйста, явиться в аудиторию?"

        menu:
            extend ""
            "Хорошо, уже иду.":
                    pass
            "Это может подождать?":
                    ch_e "Полагаю, что да, до завтра подождет."
                    menu:
                        extend ""
                        "Ага, тогда завтра зайду.":
                                $ EmmaX.AddWord(1,0,"EmmaStorm") #adds to daily
                                return
                        "Давай лучше сейчас.":
                                ch_e "Хорошо, тогда до встречи."
                        "Я вообще не хочу приходить.":
                                ch_e "Что ж, хорошо, просто скажу Чарльзу, что мы пытались."
                                $ EmmaX.DrainWord("EmmaStormQueue",0,0,1) #removes from Traits
                                #remove flag for now
                                return

            "Не хочу.":
                    ch_e "Точно? Может, сможешь подойти завтра?"
                    menu:
                        extend ""
                        "Ага, тогда завтра зайду.":
                                $ EmmaX.AddWord(1,0,"EmmaStorm") #adds to daily
                                return
                        "Давай лучше сейчас.":
                                ch_e "Хорошо, тогда до встречи."
                        "Точно.":
                                ch_e "Что ж, хорошо, просто скажу Чарльзу, что мы пытались."
                                $ EmmaX.DrainWord("EmmaStormQueue",0,0,1) #removes from Traits
                                #remove flag for now
                                return
        "Вы направляетесь в аудиторию."

        call Shift_Focus(EmmaX)
        $ Player.AddWord(1,"interruption") #adds to Recent
        $ bg_current = "bg classroom"
        call CleartheRoom(EmmaX,0,1)
        $ EmmaX.OutfitChange(Changed=1)
        $ EmmaX.Loc = "bg classroom"
        $ StormX.OutfitChange(Changed=1)
        $ StormX.Loc = "bg classroom"
        $ EmmaX.FaceChange("sly",0)
        $ StormX.FaceChange("sly",0)
        call Set_The_Scene
        $ Taboo = 0
        $ EmmaX.Taboo = 0
        $ StormX.Taboo = 0
        $ Line = 0
        $ EmmaX.DrainWord("EmmaStormQueue",0,0,1) #removes from Traits

        if not Player.Male:
            ch_e "Я рада, что ты пришла."
        else:
            ch_e "Я рад, что ты пришел."
        ch_e "Чарльз снова связался с нами и попросил, чтобы мы предприняли еще одну попытку \"исправить тебя.\""
        if "EmmaStormFail" in EmmaX.History:
                # if you failed last time.
                ch_e "Знаю, в прошлый раз мы не смогли прийти к соглашению, но надеюсь, что в этот раз все пройдет иначе."
        ch_e "Ты же -желаешь- \"исправиться,\" не так ли?"
        jump Emma_and_Storm_Main

label Emma_and_Storm: #/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        #stuff
        #launch conditions,if Time_Count == 2 and "EmmaStormQueue" in EmmaX.Traits and bg_current != "bg classroom" and not Party
        #Queue gets added when you get caught having sex if "EmmaStorm" not in EmmaX.History and "classcaught" in EmmaX.History and "met" in StormX.History and (EmmaX.SEXP >= 15 or StormX.SEXP >= 15):
        "Вы получаете сообщение от Ксавье."
        call XavierFace("angry")
        ch_x "[Player.Name], надеюсь, мы сможем с тобой немного поговорить."
        ch_x "Пожалуйста, подойди в аудиторию."
        menu:
            extend ""
            "Хорошо, уже иду.":
                    pass
            "Это может подождать?":
                    ch_x "Полагаю, что мы и так уже достаточно долго откладывали этот разговор."
                    ch_x "У тебя есть десять минут, поторопись, иначе мне, возможно, придется тебя исключить."
                    "Похоже, у вас нет выбора."
            "Не хочу.":
                ch_x "Боюсь, я вынужден настаивать."
                menu:
                    extend ""
                    "Ну ладно, скоро буду.":
                            pass
                    "Не, все равно не хочу.":
                            ch_x "Если ты не придешь, мне, возможно, придется тебя исключить."
                            "Похоже, у вас нет выбора."
        $ EmmaX.DrainWord("EmmaStormQueue",0,0,1) #removes from Traits
        "Вы отправляетесь в аудиторию."
        $ Round -= 5 if Round > 5 else (Round-1)

        call Shift_Focus(EmmaX)
        $ Player.AddWord(1,"interruption") #adds to Recent
        $ bg_current = "bg classroom"
        call CleartheRoom(EmmaX,0,1)
        $ EmmaX.OutfitChange(Changed=1)
        $ EmmaX.Loc = "bg classroom"
        $ StormX.OutfitChange(Changed=1)
        $ StormX.Loc = "bg classroom"
        $ EmmaX.FaceChange("sly",0)
        $ StormX.FaceChange("sly",0)
        call Set_The_Scene
        $ Taboo = 0
        $ EmmaX.Taboo = 0
        $ StormX.Taboo = 0
        $ Line = 0
        show Professor at SpriteLoc(StageLeft) zorder 25

        "Когда вы входите, вы замечаете, что [EmmaX.Name] с [StormX.Name_tvo] тоже пришли."
        ch_x "Прошу прощения, если это покажется тебе несколько конфронтационным, но я счел важным привлечь твоих наставниц."
        if not Player.Male:
            ch_x "Я полагаю, ты оказала довольно дурное влияние на это учреждение."
        else:
            ch_x "Я полагаю, ты оказал довольно дурное влияние на это учреждение."
        $ EmmaX.FaceChange("sly",0,Eyes="side")
        $ StormX.FaceChange("sly",0,Eyes="side")
        ch_x "Твоя внеучебная деятельность была. . . весьма деструктивной."
        if len(Rules) >= 3:
            #if you've locked out a lot of girls
            ch_x "Кроме того, ты смог довольно умело связать мне руки. . ."
        if EmmaX.Caught or StormX.Caught:
            $ EmmaX.FaceChange("sadside",2,Eyes="leftside")
            $ StormX.FaceChange("sadside",2,Eyes="leftside")
            $ EmmaX.Statup("Obed", 70, 2)
            $ EmmaX.Statup("Inbt", 70, 2)
            $ StormX.Statup("Obed", 70, 2)
            $ StormX.Statup("Inbt", 70, 2)
            if EmmaX.Caught and StormX.Caught:
                    ch_x "И, боюсь, возможно, эти двое также стали частью проблемы."
            elif EmmaX.Caught:
                    $ StormX.FaceChange("sly",1,Eyes="side")
                    ch_x "И, боюсь, возможно, мисс Фрост также стала частью проблемы."
            else: #StormX.Caught:
                    $ EmmaX.FaceChange("sly",1,Eyes="leftside")
                    ch_x "И, боюсь, возможно, мисс Манро также стала частью проблемы."
            ch_x "Тем не менее, я дам им возможность все исправить."
        else:
            ch_x "Но у нас по крайней мере есть две прекрасные наставницы."
        $ EmmaX.FaceChange("sexy",1,Eyes="side")
        $ StormX.FaceChange("sexy",1,Eyes="side")
        if not Player.Male:
            ch_x "Мне нужно, чтобы вы объяснили ей серьезность ее поступков."
            ch_x "Надеюсь, вы сможете убедить ее держать свои позывы под контролем. . ."
        else:
            ch_x "Мне нужно, чтобы вы объяснили ему серьезность его поступков."
            ch_x "Надеюсь, вы сможете убедить его держать свои позывы под контролем. . ."
        ch_x "-с этим я, очевидно, не смог справиться."
        if not Player.Male:
            ch_x "Вы сами вольны определить наказания, главное - добейтесь изменений в ее поведении."
        else:
            ch_x "Вы сами вольны определить наказания, главное - добейтесь изменений в его поведении."
        ch_x "Жду от вас полный отчет утром."
        #xavier leaves
        hide Professor with easeoutleft
        call XavierFace("happy")
        "Ксавье отправляется обратно в свой кабинет."

        $ EmmaX.FaceChange("sly",1)
        $ StormX.FaceChange("sly",1)
        ch_e "Что ж."
        ch_e "Это была неприятная сцена. . ."
        ch_s "Да, пожалуй, ты права."
        if (EmmaX in Player.Harem and StormX in Player.Harem) or "poly Emma" in StormX.Traits:
            pass #if they have done stuff together already
        else:
            #only plays if the two are not fully aware of each other.
            if "taboo" not in EmmaX.History:
                    #Emma is at least pretending to not be doing anything.
                    $ EmmaX.Statup("Obed", 50, 2)
                    $ StormX.Statup("Obed", 50, 2)
                    ch_e "Я видела, чем ты занимаешься с и юными леди."
                    if StormX.Caught:
                            #if you've been caught doing it with Storm
                            $ EmmaX.FaceChange("sly",1,Eyes="leftside")
                            $ StormX.FaceChange("sly",2,Eyes="side",Brows="sad")
                            $ EmmaX.Statup("Obed", 70, 2)
                            $ EmmaX.Statup("Inbt", 70, 2)
                            $ StormX.Statup("Inbt", 70, 2)
                            ch_e "И с Ороро. . ."

                    if EmmaX.SEXP >= 15:
                            #if you've done stuff with Emma
                            $ EmmaX.FaceChange("sly",2,Eyes="leftside")
                            $ EmmaX.Statup("Obed", 70, 2)
                            $ EmmaX.Statup("Inbt", 70, 2)
                            $ StormX.Statup("Obed", 70, 2)
                            $ StormX.Statup("Inbt", 70, 2)
                            ch_s "О, Эмма, прошу, не надо, ты и сама не была невинной."
                    elif StormX.Caught:
                            #no stuff with Emma, but Storm's been caught before
                            $ EmmaX.Statup("Obed", 70, 2)
                            $ EmmaX.Statup("Inbt", 70, 2)
                            $ StormX.Statup("Inbt", 70, 2)
                            ch_s "Возможно, мне следовало быть немного более осмотрительной."
                    elif StormX.SEXP >= 15:
                            #no stuff with Emma, but with Storm
                            $ EmmaX.Statup("Obed", 70, 2)
                            $ EmmaX.Statup("Inbt", 70, 2)
                            $ StormX.Statup("Inbt", 70, 2)
                            ch_s "Да, хотя, полагаю, и у меня не самая идеальная репутация."
                    else:
                            #no stuff with either
                            ch_s "Да, это очень тревожно."
            else:
                    #Emma's been caught with you before.
                            $ EmmaX.FaceChange("sly",2)
                            $ StormX.FaceChange("sly",1,Eyes="side")
                            $ EmmaX.Statup("Obed", 70, 2)
                            $ StormX.Statup("Obed", 70, 2)
                            $ StormX.Statup("Inbt", 70, 2)
                            if not Player.Male:
                                ch_e "Полагаю, я получала слишком много удовольствия от наших с ним взаимодействий."
                            else:
                                ch_e "Полагаю, я получала слишком много удовольствия от наших с ним взаимодействий."
            #end comments based on Emma and Storm's shared history with you

            if EmmaX.SEXP >= 15:
                    #if you've done stuff with Emma
                    $ EmmaX.FaceChange("sly",1,Eyes="leftside")
                    $ StormX.FaceChange("sly",1,Eyes="side")
                    ch_e "Теперь уже нет смысла что-либо отрицать. . ."
                    $ EmmaX.FaceChange("sly",1,Eyes="leftside")
                    $ StormX.FaceChange("surprised",2,Eyes="side")
                    $ EmmaX.Statup("Obed", 70, 2)
                    $ EmmaX.Statup("Inbt", 70, 2)
                    $ StormX.Statup("Obed", 70, 2)
                    ch_e "Мы с [Player.Name_tvo] хорошо повеселились."
                    if StormX.SEXP >= 15:
                            $ StormX.FaceChange("sly",2,Eyes="leftside")
                            $ EmmaX.Statup("Obed", 70, 1)
                            $ StormX.Statup("Inbt", 70, 1)
                            ch_s "Признаюсь, Эмма, мы с [Player.Name_tvo] тоже неплохо проводили время."
                    else:
                            $ EmmaX.Statup("Inbt", 70, 1)
                            $ StormX.Statup("Obed", 70, 1)
                            ch_s "Эмма! Как же это непрофессионально с твоей стороны!"
            else: #StormX.SEXP >= 15:
                    #if you've done stuff with Storm
                    $ EmmaX.FaceChange("sly",1,Eyes="leftside")
                    $ StormX.FaceChange("sly",1,Eyes="leftside")
                    $ EmmaX.Statup("Obed", 70, 2)
                    $ EmmaX.Statup("Inbt", 70, 2)
                    $ StormX.Statup("Obed", 70, 2)
                    $ StormX.Statup("Inbt", 70, 2)
                    ch_s "Должна признаться, Эмма, мы с [Player.Name_tvo] неплохо проводили время вместе."
                    ch_e "Боже, как возмутительно."
        # end if EmmaX not in Player.Harem or StormX not in Player.Harem:

        $ EmmaX.FaceChange("sly",1)
        $ StormX.FaceChange("sly",1)
label Emma_and_Storm_Main: #/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        ch_e "Я не знаю, что мы можем сделать, чтобы убедить тебя \"измениться.\""
        ch_s "Да, у нас, безусловно, определенные трудности."

        ch_e "Полагаю, нам просто придется обеспечить тебя кое-какими альтернативными отвлечениями. . ."
        $ Player.Traits.append("locked")
        "Она подходит к двери и запирает ее."
        ch_s "Да. . ."
        if StormX.SEXP < 15:
                $ StormX.FaceChange("confused",2,Eyes="side")
                ch_s "Подожди, что?"
                $ EmmaX.FaceChange("sly",1,Eyes="leftside")
                ch_e "Oh, come on, dear."
                ch_e "Лучший способ предотвратить будущие неприятности - научить [Player.Name_vin] держать свои позывы под контролем."
                ch_s "И как ты предлагаешь это сделать?"
        $ EmmaX.FaceChange("sly",1)
        if not Player.Male:
            ch_e "Для начала нам нужно обучить ее \"общественно полезному труду\"."
        else:
            ch_e "Для начала нам нужно обучить его \"общественно полезному труду\"."
        scene bg_classzoom onlayer backdrop
#        scene bg_class onlayer backdrop:
#                zoom 4.5
#                offset (-1500,-900)#(-1400,-900)
        "Они подводят вас к передней части аудитории."
#start Emma cunnilingus / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        $ Player.Statup("Focus", 70, 5)
        if EmmaX.PantsNum() > 5:
                $ EmmaX.Upskirt = 1
                $ EmmaX.PantiesDown = 1
                "[EmmaX.Name] спускает штаны и облокачивается на стол."
        elif EmmaX.PantsNum():
                $ EmmaX.Upskirt = 1
                $ EmmaX.PantiesDown = 1
                "[EmmaX.Name] приподнимает юбку и облокачивается на стол."
        else:
                "[EmmaX.Name] облокачивается на стол."
        $ EmmaX.Pose = "doggy"
        show Storm_Sprite at Sprite_Set(850,0,ZM=1.25)
        call Emma_Sex_Launch
        $ StormX.FaceChange("sly",2,Eyes="side")
        ch_e "Мне нужно, чтобы ты начал лизать, [EmmaX.Petname]."
        menu:
            extend ""
            "Конечно.":
                    $ EmmaX.Statup("Love", 90, 2)
                    $ StormX.Statup("Love", 90, 2)
                    $ StormX.Statup("Inbt", 70, 2)
                    "Вы наклоняетесь и начинаете работать языком."
            "Я не собираюсь этого делать.":
                    $ EmmaX.Statup("Love", 80, -1)
                    $ EmmaX.Statup("Obed", 70, 2)
                    $ StormX.Statup("Love", 80, -1)
                    $ StormX.Statup("Obed", 70, 2)
                    ch_e "В другой ситуации мне было бы все равно, но в данном случае я вынуждена настаивать."
                    menu:
                        extend ""
                        "Ладно.":
                                $ EmmaX.Statup("Obed", 70, 1)
                                $ EmmaX.Statup("Inbt", 70, 1)
                                $ StormX.Statup("Obed", 70, 1)
                                $ StormX.Statup("Inbt", 70, 2)
                                "Вы наклоняетесь и начинаете работать языком."
                        "Нет. [[прям точно нет]":
                                $ EmmaX.Statup("Love", 80, -2)
                                $ EmmaX.Statup("Obed", 80, 2)
                                $ StormX.Statup("Love", 80, -2)
                                $ StormX.Statup("Obed", 80, 2)
                                jump Emma_and_Storm_Bad_End
            "Я бы лучше вставил в тебя член." if Player.Male:
                    $ EmmaX.Statup("Obed", 70, 2)
                    $ EmmaX.Statup("Inbt", 70, 1)
                    $ StormX.Statup("Obed", 70, 2)
                    $ StormX.Statup("Inbt", 70, 2)
                    if EmmaX.Sex or EmmaX.Anal:
                            ch_e "В другой ситуации я была бы не против, но в данном случае я вынуждена настаивать."
                    else:
                            $ EmmaX.Statup("Obed", 80, 1)
                            $ StormX.Statup("Obed", 80, 1)
                            ch_e "Возможно, со временем мы до этого дойдем."
                            ch_e "А пока начинай лизать."
                    menu:
                        extend ""
                        "Ладно.":
                                $ EmmaX.Statup("Obed", 70, 1)
                                $ EmmaX.Statup("Inbt", 70, 1)
                                $ StormX.Statup("Obed", 70, 1)
                                $ StormX.Statup("Inbt", 70, 2)
                                "Вы наклоняетесь и начинаете работать языком."
                        "Нет. [[прям точно нет]":
                                $ EmmaX.Statup("Love", 80, -2)
                                $ EmmaX.Statup("Obed", 80, 2)
                                $ StormX.Statup("Love", 80, -2)
                                $ StormX.Statup("Obed", 80, 2)
                                jump Emma_and_Storm_Bad_End
            ". . .":
                    $ EmmaX.Statup("Obed", 50, 2)
                    $ EmmaX.Statup("Inbt", 70, 2)
                    $ StormX.Statup("Obed", 50, 2)
                    $ StormX.Statup("Inbt", 70, 2)
                    ch_e "Молчишь?"
                    ch_e "В другой ситуации мне было бы все равно, но в данном случае я вынуждена настаивать."
                    menu:
                        extend ""
                        "Ладно.":
                                $ EmmaX.Statup("Obed", 70, 1)
                                $ EmmaX.Statup("Inbt", 70, 1)
                                $ StormX.Statup("Obed", 70, 1)
                                $ StormX.Statup("Inbt", 70, 2)
                                "Вы наклоняетесь и начинаете работать языком."
                        "Нет. [[прям точно нет]":
                                $ EmmaX.Statup("Love", 80, -2)
                                $ EmmaX.Statup("Obed", 80, 2)
                                $ StormX.Statup("Love", 80, -2)
                                $ StormX.Statup("Obed", 80, 2)
                                jump Emma_and_Storm_Bad_End
        $ EmmaX.Statup("Lust", 60, 5)
        $ StormX.Statup("Lust", 60, 3)
        $ Player.Statup("Focus", 70, 3)
        $ Trigger = "lick pussy"
        $ EmmaX.LickP += 1
        #start visuals for licking Emma
        if StormX.SEXP < 15:
                $ EmmaX.FaceChange("sly",1)
                $ StormX.FaceChange("surprised",2,Eyes="side")
                ch_s "О, боже. . ."
        $ EmmaX.FaceChange("sly",1,Eyes="leftside")
        if not Player.Male:
            ch_e "Знаешь, Ороро, она весьма талантлива в этом."
        else:
            ch_e "Знаешь, Ороро, он весьма талантлив в этом."
        $ StormX.FaceChange("sly",1,Eyes="side")
        $ StormX.Statup("Lust", 60, 3)
        $ Player.Statup("Focus", 70, 3)
        if StormX.LickP:
                ch_s "Да, мне это хорошо известно. . ."
                ch_e "Ах, ты плутовка. . ."
        else:
                ch_s "Да, я вижу. . ."
        $ Partner = StormX

        call JackCheck(1)
        $ EmmaX.Facing = 0
        if _return:
                #you tried to jack it
                $ EmmaX.Statup("Inbt", 70, 2)
                $ StormX.Statup("Love", 90, 2)
                $ StormX.Statup("Inbt", 70, 2)
                $ EmmaX.FaceChange("angry",1)
                $ StormX.FaceChange("sly",1)
                ch_e "Нет, нет, нет, [EmmaX.Petname], подобного я не допущу."
        else:
                $ EmmaX.FaceChange("sly",1)
                $ StormX.FaceChange("sly",1)
                ch_e "Хочу предупредить, [EmmaX.Petname]. . ."
        $ EmmaX.FaceChange("sly",1)
        ch_e "Пока мы не закончим, тебе не положено получать удовольствие."

        $ Partner.Offhand = "fondle pussy"
        $ StormX.FaceChange("sly",2,Eyes="side",Brows="sad")
        $ EmmaX.Statup("Lust", 60, 5)
        $ StormX.Statup("Lust", 60, 5)
        $ Player.Statup("Focus", 70, 3)
        $ Round -= 5 if Round > 5 else (Round-1)
        if StormX.SEXP < 15:
                $ StormX.Statup("Obed", 70, 2)
                $ StormX.Statup("Inbt", 50, 1)
                $ StormX.Statup("Inbt", 70, 2)
                "Спустя минуту или около того [StormX.Name] опускает руку к своей промежности."
                $ EmmaX.FaceChange("sly",1,Eyes="side")
                show Emma_Doggy_Animation:
                        xzoom -1
                        pos (StageCenter+50,50)
                "[EmmaX.Name] бросает взгляд на нее."
        else:
                "[StormX.Name] опускает руку к своей промежности, а затем начинает ласкать ее."
                show Emma_Doggy_Animation:
                        xzoom -1
                        pos (StageCenter+50,50)
                $ EmmaX.FaceChange("sly",1,Eyes="side")
                "Спустя минуту или около того [EmmaX.Name] бросает взгляд на нее."
        ch_e "Ороро, прошу меня простить, ты тоже должна поучавствовать в этой воспитательной работе."
        if StormX.SEXP < 15:
                $ StormX.Statup("Inbt", 70, 2)
                $ Partner.Offhand = 0
                $ StormX.FaceChange("surprised",2,Eyes="side")
                "[StormX.Name] прекращает свои действия."
                ch_s "В этом нет необходимости, правда."
                ch_e "Я настаиваю."
        if not ApprovalCheck(StormX, 1200):
                $ StormX.Statup("Obed", 70, 2)
                $ StormX.Statup("Inbt", 70, 2)
                ch_s "Что ж, полагаю, без этого наказание нельзя будет назвать законченным. . ."
                ch_s "-но тебе лучше к этому не привыкать, [StormX.Petname]."
        $ Trigger = 0
        show Emma_Doggy_Animation:
                xzoom 1
        hide Emma_Doggy_Animation
        show Emma_Sprite at Sprite_Set(900,0,ZM=1.3)
        $ EmmaX.FaceChange("sly",1,Eyes="leftside")
        $ StormX.Statup("Lust", 60, 3)
        ch_e "Подойдите сюда, мисс Манро, и прилягте на стол."
        $ Partner.Offhand = 0
        $ StormX.FaceChange("sly",1,Eyes="side")
        ch_s "Ох, Эмма, прошу, давай без этого."
#start Storm cunnilingus / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        call Shift_Focus(StormX)
        #start visuals for Storm sex pose, move Emma to the side
        if StormX.PantsNum() > 5:
                "[StormX.Name] сбрасывает штаны и ложится на стол."
        elif StormX.PantsNum():
                "[StormX.Name] задирает юбку и ложится на стол."
        else:
                "[StormX.Name] ложится на стол."
        $ StormX.Upskirt = 1
        $ StormX.PantiesDown = 1
        $ StormX.Pose = "sex"
        hide Storm_Sprite
        show Storm_SexSprite zorder 150: #call Storm_Sex_Launch
                zoom 1.15
                ypos 230
        show Emma_Sprite at Sprite_Set(900,0,ZM=1.3) zorder 160
        $ StormX.FaceChange("sly",1,Eyes="down")
        $ EmmaX.FaceChange("sly",1,Eyes="side")
        $ EmmaX.Statup("Lust", 60, 3)
        $ StormX.Statup("Lust", 60, 5)
        "[EmmaX.Name] нежно подталкивает вас к [StormX.Name_dat], и вы начинаете лизать ее."
        $ Trigger = "lick pussy"
        $ Partner.Offhand = "fondle pussy"
        $ EmmaX.Statup("Lust", 60, 4)
        $ StormX.Statup("Lust", 60, 4)
        $ Player.Statup("Focus", 70, 3)
        "В это время [EmmaX.Name] начинает ласкать свою киску."
        if not StormX.LickP:
                $ StormX.FaceChange("sly",1,Eyes="leftside")
                if not Player.Male:
                    ch_s "Ах, она весьма искусна!"
                else:
                    ch_s "Ах, он весьма искусен!"
        $ StormX.LickP += 1
#        show Emma_Sprite at Sprite_Set(750,150,ZM=1.3) zorder 140
        show Emma_Sprite zorder 140:
                 ease 1 pos(700,150) zoom 1.3
        $ EmmaX.FaceChange("sly",1,Eyes="closed",Mouth="tongue")
        $ EmmaX.Statup("Lust", 60, 4)
        $ StormX.Statup("Lust", 60, 4)
        $ Player.Statup("Focus", 70, 3)
        "Через несколько мгновений [EmmaX.Name] также начинает облизывать грудь [StormX.Name_rod]."
        $ StormX.FaceChange("surprised",2,Eyes="down")
        ch_s "Эмма!"
        ch_s "В этом днет необходимости. . ."
        $ StormX.Uptop = 1
        $ StormX.FaceChange("sly",1,Eyes="down")
        ch_s "Ооох. . . но я тебе благодарна. . ."
        $ EmmaX.Statup("Lust", 60, 5)
        $ StormX.Statup("Lust", 60, 5)
        $ Player.Statup("Focus", 70, 3)
        $ StormX.FaceChange("sly",1,Eyes="closed")
        call Girl_First_Bottomless(StormX,1)
        call Girl_First_Topless(StormX,1)
        call Girl_First_Bottomless(EmmaX,1)

#start Emma getting your cock out / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        $ Trigger = 0
        $ EmmaX.Offhand = 0
#        call Storm_Sex_Reset
        $ EmmaX.FaceChange("sly",1)
        $ StormX.FaceChange("surprised",2,Eyes="leftside")
        show Emma_Sprite zorder 160:
                 ease .5 pos(750,0) zoom 1.4
        $ Round -= 5 if Round > 5 else (Round-1)
        "Еще через несколько минут [EmmaX.Name] усаживает вас на стул."
        call Shift_Focus(EmmaX)
        ch_e "Пока этого достаточно."
        ch_s "Эмма! Я же почти закончила!"
        $ EmmaX.FaceChange("sly",1,Eyes="side")
        $ StormX.FaceChange("sadside",1)
        ch_e "Прости, дорогая, закончишь немного позже."
        $ EmmaX.FaceChange("sly",1,Eyes="down")
        $ StormX.FaceChange("surprised",1,Eyes="down")
        $ Player.AddWord(1,"cockout",0,0,0)
        "Она протягивает руку и расстегивает молнию на ваших брюках."
        $ StormX.FaceChange("sly",1,Eyes="down")
        $ EmmaX.Statup("Lust", 70, 3)
        $ StormX.Statup("Lust", 70, 3)
        $ Player.Statup("Focus", 70, 3)
        ch_e "Я думаю, кое-кому тоже нужно уделить немного внимания. . ."
        call Seen_First_Peen(StormX,EmmaX,0)
        $ EmmaX.Statup("Lust", 70, 3)
        $ StormX.Statup("Lust", 70, 3)
        $ Player.Statup("Focus", 70, 3)
        if not Player.Male:
            "Она начинает нежно ласкать вашу киску."
        else:
            "Она начинает нежно ласкать ваш член."
        if Player.Male:
            $ EmmaX.Hand += 1
        else:
            $ EmmaX.Finger += 1

#start Emma licking Storm / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        "Она останавливается так же внезапно, как и начала."
        #Storm is in sex pose, add Emma doggy here
        $ EmmaX.Facing = 1
        hide Emma_Sprite
        show Emma_Doggy_Animation zorder 160:
                zoom 1.1
                pos (StageCenter+100,350)
        "Затем она снова поворачивается к [StormX.Name_dat] и начинает лизать ее киску."
        $ EmmaX.Statup("Lust", 80, 3)
        $ StormX.Statup("Lust", 80, 5)
        $ Player.Statup("Focus", 70, 3)
        ch_s "Ох, Эмма. . ."
        $ StormX.FaceChange("sly",1,Eyes="stunned")
        $ EmmaX.Statup("Lust", 80, 3)
        $ StormX.Statup("Lust", 80, 5)
        $ Player.Statup("Focus", 70, 3)
        ch_s "О, светлая госпожа. . ."
        $ EmmaX.Les += 1
        $ StormX.Les += 1
        $ EmmaX.AddWord(1,0,0,0,"les Storm")
        $ StormX.AddWord(1,0,0,0,"les Emma")
        $ EmmaX.AddWord(1,"lesbian",0,0,0) #adds "lesbian" to recent actions for both girls
        $ StormX.AddWord(1,"lesbian",0,0,0) #adds "lesbian" to recent actions for both girls
        call JackCheck(1)
        $ EmmaX.Facing = 0
        if Trigger2 and ApprovalCheck(EmmaX, 1500):
                ch_e "Так трудно было воздержаться?"
        $ EmmaX.FaceChange("sly",1)
        $ StormX.FaceChange("sly",1)
        if Trigger2:
                $ EmmaX.Statup("Lust", 80, 3)
                $ StormX.Statup("Lust", 80, 3)
                $ EmmaX.Statup("Love", 80, -2)
                $ EmmaX.Statup("Obed", 50, 2)
                $ StormX.Statup("Love", 80, 2)
                $ StormX.Statup("Inbt", 50, 2)
                #you tried to jack it
                if not Player.Male:
                    ch_e "Ты думала, я не замечу?"
                else:
                    ch_e "Ты думал, я не замечу?"
                if "warning" in Player.RecentActions:
                        "Они тут же останавливаются и одеваются."
                        jump Emma_and_Storm_Bad_End
                $ Player.AddWord(1,"warning") #recent
                menu:
                    "Остановиться?"
                    "Да":
                            $ EmmaX.Statup("Inbt", 60, 2)
                            $ StormX.Statup("Inbt", 60, 2)
                            "Вы останавливаетесь."
                    "Нет":
                            $ EmmaX.Statup("Love", 80, -2)
                            $ EmmaX.Statup("Obed", 50, 3)
                            $ StormX.Statup("Love", 80, -1)
                            $ StormX.Statup("Obed", 50, 2)
                            "Вы продолжаете."
                            "Они тут же останавливаются и одеваются."
                            $ StormX.FaceChange("angry",2)
                            "[StormX.Name] выглядит особенно раздраженной вашими действиями."
                            jump Emma_and_Storm_Bad_End
        else:
                ch_e "Я еще раз напомню тебе, что ты здесь не для того, чтобы \"получать удовольствие\". . ."
        ch_e "Ты здесь лишь для того, чтобы радовать глаза Ороро."
        if _return:
                ch_e "Если ты будешь продолжать, мы немедленно все прекратим и сообщим, что наши усилия не увенчались успехом."
        $ StormX.FaceChange("sly",1,Eyes="down")
        $ EmmaX.Statup("Lust", 60, 5)
        $ StormX.Statup("Lust", 60, 5)
        ch_s "Как жестоко, Эмма."
        $ StormX.FaceChange("sly",1)
        ch_s "Мне очень жаль, [StormX.Petname], но это мне кажется достойным \"наказанием.\""
        $ StormX.FaceChange("sly",1,Eyes="down")
        ch_s "Что ж, прошу, Эмма, продолжай."
        $ EmmaX.Facing = 1
        $ EmmaX.Offhand = "fondle pussy"
        $ StormX.FaceChange("sexy",1,Eyes="closed")
        $ EmmaX.Statup("Lust", 80, 5)
        $ StormX.Statup("Lust", 80, 5)
        $ Player.Statup("Focus", 70, 3)
        "[EmmaX.Name] продолжает вылизывать киску [StormX.Name_rod], не забывая и про себя."
        call JackCheck(2)
        if Trigger2 and ApprovalCheck(StormX, 1500):
                $ Player.Statup("Focus", 80, 3)
                $ StormX.Statup("Love", 80, 1)
                $ StormX.Statup("Inbt", 70, 1)
                "[StormX.Name], кажется, замечает, что вы удовлетворяете себя, но ее это лишь забавляет."
                $ StormX.AddWord(1,"sawyou") #recent
        elif Trigger2:
                #you tried to jack it
                $ StormX.FaceChange("sly",1)
                $ StormX.Statup("Love", 80, 1)
                $ StormX.Statup("Inbt", 70, 2)
                ch_s "Я все вижу, [StormX.Petname], прекрати, немедленно."
                $ Player.AddWord(1,"warning") #recent
                menu:
                    "Остановиться?"
                    "Да":
                            $ EmmaX.Statup("Inbt", 60, 2)
                            $ StormX.Statup("Inbt", 60, 2)
                            "Вы останавливаетесь."
                    "Нет":
                            $ EmmaX.Statup("Love", 80, -2)
                            $ EmmaX.Statup("Obed", 50, 3)
                            $ StormX.Statup("Love", 80, -1)
                            $ StormX.Statup("Obed", 50, 2)
                            "Вы продолжаете."
                            "Они тут же останавливаются и одеваются."
                            jump Emma_and_Storm_Bad_End
        $ StormX.FaceChange("sexy",2,Eyes="closed")
        show Storm_SexSprite:
                parallel:
                    pause .25
                    easein .5 xpos 660
                    easein .5 xpos 640
                    easein .5 xpos 660
                    easein .5 xpos 640
                parallel:
                    easein .5 ypos 220
                    easein .5 ypos 210
                    easein .5 ypos 200
                    easein .5 ypos 185
                    easein .25 ypos 180
                block:
                    easein .5 xpos 655
                    easein .5 xpos 645
                    repeat
        $ EmmaX.Statup("Lust", 80, 5)
        $ StormX.Statup("Lust", 94, 5)
        $ Player.Statup("Focus", 70, 3)
        "По прошествии некоторого времени [StormX.Name] начинает слегка дрожать, немного приподнимаясь над столешницей."
        show Storm_SexSprite zorder 150: #call Storm_Sex_Launch
                zoom 1.15
                ypos 230
        call Punch
        $ EmmaX.Statup("Lust", 80, 10)
        $ Player.Statup("Focus", 70, 5)
        $ StormX.Lust = 20
        "Волны экстаза одна за другой проходят по ее телу. Содрогнувшись в последний раз, она опускается на стол."
        call JackCheck(2)

        #animation of Emma moving up Storm
        show Emma_Doggy_Animation: # starts
                pos (650,350)
                parallel:
                    pause .25
                    easein 1 xpos 680
                    easein 1 xpos 610
                parallel:
                    easein 2.25 ypos 150
        $ EmmaX.Statup("Lust", 80, 5)
        $ StormX.Statup("Lust", 80, 5)
        $ Player.Statup("Focus", 70, 3)
        "[EmmaX.Name] покрывает поцелуями тело [StormX.Name_rod], поднимаясь всё выше, и задерживается на её покачивающейся груди."
        $ StormX.FaceChange("tongue",2)
        show Emma_Doggy_Animation: # starts
                pos (610,150)
                parallel:
                    pause .25
                    easein 1 xpos 670
                    easein 1 xpos 650
                parallel:
                    easein 2.25 ypos 50
        $ EmmaX.Statup("Lust", 80, 5)
        $ StormX.Statup("Lust", 80, 5)
        $ Player.Statup("Focus", 70, 3)
        "В завершение она страстно целует ее в губы."
        $ EmmaX.FaceChange("sly",1,Eyes="side",Mouth="tongue")
        show Emma_Doggy_Animation: # starts
                pos (650,50)
                parallel:
                    easein 2 xpos 750
        pause 1
        $ EmmaX.Facing = 0
        $ StormX.FaceChange("sly",1)
        "Она отстраняется, оставляя после себя тоненькую дорожку из соков [StormX.Name_rod]."
        if Trigger2 and ApprovalCheck(StormX, 1500):
                $ Player.Statup("Focus", 80, 3)
                if "sawyou" not in StormX.RecentActions:
                        $ StormX.Statup("Obed", 70, 2)
                        $ StormX.Statup("Inbt", 70, 1)
                        "[StormX.Name], кажется, замечает, что вы удовлетворяете себя, но она принимает это как должное."
                        $ StormX.AddWord(1,"sawyou") #recent
        elif Trigger2:
                #you tried to jack it
                $ EmmaX.FaceChange("angry",1)
                $ EmmaX.Statup("Love", 80, -1)
                $ EmmaX.Statup("Obed", 50, 1)
                $ EmmaX.Statup("Inbt", 50, 2)
                $ StormX.Statup("Obed", 50, 1)
                if not Player.Male:
                    ch_s "Неужели ты думала, что в своем состоянии я не замечу, чем ты занимаешься?"
                else:
                    ch_s "Неужели ты думал, что в своем состоянии я не замечу, чем ты занимаешься?"
                if "warning" in Player.RecentActions:
                        "Они тут же останавливаются и одеваются."
                        jump Emma_and_Storm_Bad_End
                $ Player.AddWord(1,"warning") #recent
                menu:
                    "Остановиться?"
                    "Да":
                            $ EmmaX.Statup("Inbt", 60, 2)
                            $ StormX.Statup("Inbt", 60, 2)
                            "Вы останавливаетесь."
                    "Нет":
                            $ EmmaX.Statup("Love", 80, -2)
                            $ EmmaX.Statup("Obed", 50, 3)
                            $ StormX.Statup("Love", 80, -1)
                            $ StormX.Statup("Obed", 50, 2)
                            "Вы продолжаете."
                            "Они тут же останавливаются и одеваются."
                            $ StormX.FaceChange("angry",2)
                            "[StormX.Name] выглядит особенно раздраженной вашими действиями."
                            jump Emma_and_Storm_Bad_End
#start Storm licking Emma   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        $ EmmaX.Offhand = 0 #stops masturbating
        $ StormX.FaceChange("sly",2,Eyes="leftside")
#        $ EmmaX.FaceChange("sly",1,Eyes="side",Mouth="tongue")
        $ EmmaX.FaceChange("sly",1,Eyes="side")
        $ Round -= 5 if Round > 5 else 0
        ch_s "Я. . . очень признательна за этот небольшой \"урок\". . ."
        $ StormX.Statup("Lust", 70, 5)
        ch_e "Мне бы тоже не помешало немного \"освежиться\", если у тебя есть время."
        $ EmmaX.FaceChange("sly",1,Eyes="leftside")
        $ StormX.FaceChange("sly",1,Eyes="side")
        hide Storm_SexSprite
        show Storm_Sprite at Sprite_Set(650,0,ZM=1.3) zorder 140
        show Storm_Sprite:
            ease 1 xpos 900
        $ EmmaX.Statup("Lust", 70, 5)
        ch_s "Думаю, я найду для тебя окно в своем расписании."
        hide Emma_Doggy_Animation with dissolve
        show Emma_69_Animation with dissolve:
            zoom .5
            pos (525,-180)
        show Storm_Sprite zorder 160
        $ EmmaX.Statup("Lust", 80, 3)
        $ StormX.Statup("Lust", 60, 3)
        $ Player.Statup("Focus", 70, 5)
        "[EmmaX.Name] встает коленями на столешницу, [StormX.Name] придвигается к ней."

        #Emma 69 posing here, and Storm doggy posing, facing 1, and drip animations as well
        hide Storm_Sprite with dissolve
        $ StormX.Facing = 1
        show Storm_Doggy_Animation zorder 150 with dissolve:
                zoom 1.2
                pos (900,0)
        show Storm_Doggy_Animation:
                ease 1 pos (800,150)
        $ EmmaX.Statup("Lust", 85, 5)
        $ StormX.Statup("Lust", 80, 5)
        $ Player.Statup("Focus", 80, 3)
        "Она крепко обхватывает [EmmaX.Name_vin] за задницу, прежде чем прижаться к ней лицом."
        show Storm_Doggy_Animation:
                xpos 800
                block:
                    ease 1 ypos 160
                    ease .5 ypos 150
                    repeat
        $ EmmaX.Statup("Lust", 90, 5)
        $ StormX.Statup("Lust", 80, 5)
        $ Player.Statup("Focus", 80, 3)
        "Вы слышите ее голодное рычание, когда она впивается в киску [EmmaX.Name_vin]."
        show Wet_Drip2 zorder 145:
                pos (510,280)
                zoom 2
        $ EmmaX.Statup("Lust", 90, 5)
        $ StormX.Statup("Lust", 80, 5)
        $ Player.Statup("Focus", 80, 3)
        "Соки ручьем стекают с ее подбородка."

        call JackCheck(2)

        if (EmmaX in Player.Harem and StormX in Player.Harem) or "poly Emma" in StormX.Traits:
                pass #if they have done stuff together already
        else:
                ch_e "Ого, раньше я только слышала, насколько ты талантлива. . ."
        $ EmmaX.Statup("Lust", 94, 5)
        $ StormX.Statup("Lust", 80, 5)
        $ Player.Statup("Focus", 80, 3)
        ch_e "Ты не. . . поверишь, как я сейчас. . . возбуждена."
        show Storm_Doggy_Animation:
                xpos 800
                ease 1 ypos 150
        "[StormX.Name] на мгновение останавливается."
        ch_s "Ох, я это чувствую, Эмма."
        if not Player.Male:
            ch_s "Уверена, наша студентка сейчас не менее. . . возбуждена."
        else:
            ch_s "Уверена, наш студент сейчас не менее. . . возбужден."
        $ StormX.Facing = 0
        if Trigger2 and ApprovalCheck(StormX, 1500):
                $ StormX.Statup("Lust", 80, 5)
                $ Player.Statup("Focus", 80, 3)
                if "sawyou" not in StormX.RecentActions:
                        $ StormX.Statup("Love", 80, 1)
                        $ StormX.Statup("Obed", 70, 2)
                        "[StormX.Name], кажется, замечает, что вы удовлетворяете себя, но она лишь подмигивает вам."
                        $ StormX.AddWord(1,"sawyou") #recent
        elif Trigger2:
                #you tried to jack it
                $ StormX.Statup("Obed", 50, 2)
                if not Player.Male:
                    ch_s "Неужели ты думала, что я слишком занят, чтобы заметить?"
                else:
                    ch_s "Неужели ты думал, что я слишком занят, чтобы заметить?"
                if "warning" in Player.RecentActions:
                        "Они тут же останавливаются и одеваются."
                        jump Emma_and_Storm_Bad_End
                $ Player.AddWord(1,"warning") #recent
                menu:
                    "Остановиться?"
                    "Да":
                            $ EmmaX.Statup("Inbt", 60, 2)
                            $ StormX.Statup("Inbt", 60, 2)
                            "Вы останавливаетесь."
                    "Нет":
                            $ EmmaX.Statup("Love", 80, -2)
                            $ EmmaX.Statup("Obed", 50, 3)
                            $ StormX.Statup("Love", 80, -1)
                            $ StormX.Statup("Obed", 50, 2)
                            "Вы продолжаете."
                            "Они тут же останавливаются и одеваются."
                            "[EmmaX.Name_vin], похоже, это особенно расстроило."
                            jump Emma_and_Storm_Bad_End
        $ StormX.FaceChange("sly",1)
        if not Player.Male:
            ch_s "Да, она действительно довольно возбуждена. . ."
        else:
            ch_s "Да, он действительно довольно возбужден. . ."
        show Storm_Doggy_Animation:
                xpos 800
                block:
                    ease 1 ypos 160
                    ease .5 ypos 150
                    repeat
        $ StormX.Facing = 1
        $ EmmaX.Statup("Lust", 94, 5)
        $ StormX.Statup("Lust", 80, 5)
        $ Player.Statup("Focus", 80, 3)
        "Она продолжает еще немного, дыхание [EmmaX.Name_rod] становится все более прерывистым."
        show Emma_69_Animation:
            ease .2 pos (525,-80)
        show Storm_Doggy_Animation:
            xpos 800
            ease 1 ypos 150
        show Wet_Drip2 zorder 145:
                pos (510,430)
        call Punch
        $ EmmaX.Lust = 20
        $ EmmaX.Statup("Lust", 80, 5)
        $ StormX.Statup("Lust", 90, 5)
        $ Player.Statup("Focus", 80, 3)
        $ Round -= 5 if Round > 5 else 0
        "Наконец, она достигает предела и, содрогнувшись в последний раз, обмякает на столе."
        hide Wet_Drip2
        hide Storm_Doggy_Animation
        show Storm_Sprite at Sprite_Set(650,200,ZM=1.3) zorder 98
        show Storm_Sprite:
            ease 1 pos (900,0)
        ch_e "Дорогая. . . ты. . . превзошла саму себя. . ."
        show Emma_69_Animation:
            ease .5 pos (525,-180)
        pause .5
        hide Emma_69_Animation
        show Emma_Sprite at Sprite_Set(450,0,ZM=1.35) zorder 99
        "Спустя несколько мгновений, придя в себя, [EmmaX.Name] с трудом садится."
        hide Emma_Sprite
        show Emma_FJ_Animation:
            zoom 1.5
            pos (1150,-40)
        show Emma_FJ_Animation:
            ease .5 pos (1150,-50)
        $ Player.Statup("Focus", 85, 3)
        "Она кладет ногу вам на плечо."
#start finale / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        #Use FJ pose, set on desk, hide chair.
        $ EmmaX.FaceChange("sly",1)
        $ StormX.FaceChange("sly",1)
        if not Player.Male:
            ch_s "Теперь остается лишь решить, что нам делать с этой непутевой девушкой?"
        else:
            ch_s "Теперь остается лишь решить, что нам делать с этим непутевым юношей?"
        ch_e "И правда. . ."
        if "warning" in Player.RecentActions:
                if not Player.Male:
                    ch_e "Ты уже почувствовала наше милосердие. . ."
                else:
                    ch_e "Ты уже почувствовал наше милосердие. . ."
        ch_e "Как -ты- думаешь, что нам лучше с тобой сделать?"
        menu:
            extend ""
            "Отпустить с предупреждением?":
                    $ EmmaX.Statup("Love", 70, -1)
                    $ EmmaX.Statup("Obed", 50, -1)
                    ch_e "Ох, как скучно."
                    if not Player.Male:
                        ch_e "Не знаю, Ороро, стоит ли нам отпускать ее с предупреждением."
                    else:
                        ch_e "Не знаю, Ороро, стоит ли нам отпускать его с предупреждением."
            "Позволить мне трахнуть вас?":
                    $ EmmaX.Statup("Lust", 80, 3)
                    $ StormX.Statup("Lust", 80, 3)
                    $ EmmaX.Statup("Love", 80, 2)
                    $ StormX.Statup("Obed", 80, 2)
                    $ EmmaX.FaceChange("smile",1)
                    $ StormX.FaceChange("smile",1)
                    ch_e "Хахаха!"
                    ch_e "Это было ужасно смело!"
                    $ EmmaX.FaceChange("sly",1,Eyes="leftside")
                    $ StormX.FaceChange("sly",1,Eyes="side")
                    $ EmmaX.Statup("Obed", 50, 1)
                    $ StormX.Statup("Love", 80, 1)
                    $ EmmaX.Statup("Obed", 80, 2)
                    ch_e "Наглости тебе не занимать."
            "Позволить мне кончить?":
                    $ EmmaX.Statup("Lust", 80, 3)
                    $ StormX.Statup("Lust", 80, 3)
                    $ EmmaX.Statup("Obed", 70, -2)
                    $ StormX.Statup("Love", 80, 1)
                    ch_e "О, неужели ты так отчаянно нуждаешься во внимании?"
                    $ EmmaX.Statup("Inbt", 70, 2)
                    $ StormX.Statup("Inbt", 70, 2)
                    ch_e "Как думаешь, сможешь дойти до ближайшего туалета?"
            "Я не знаю.":
                    $ EmmaX.Statup("Love", 80, 2)
                    $ StormX.Statup("Love", 80, 1)
                    ch_e "Возможно, это самое умное, что ты сказал за весь день."
                    $ EmmaX.Statup("Inbt", 50, 1)
                    $ StormX.Statup("Inbt", 50, 1)
                    ch_e "Ты явно не знаешь, как избежать нежелательного внимания. . ."
            ". . .":
                    $ EmmaX.Statup("Obed", 70, 2)
                    $ StormX.Statup("Obed", 70, 1)
                    ch_e "Даже ничего не попросишь?"
                    ch_e "Полагаю, я уважаю такое решение, но даже так. . ."
        $ EmmaX.FaceChange("sly",1)
        $ StormX.FaceChange("sly",1)
        if "warning" in Player.RecentActions and ApprovalCheck(EmmaX, 1500):
                $ EmmaX.Statup("Inbt", 60, 2)
                $ StormX.Statup("Inbt", 60, 2)
                ch_e "Пожалуй, мы сможем проигнорировать твои попытки нарушить правила. . ."
        elif "warning" in Player.RecentActions:
                $ EmmaX.FaceChange("sad",1)
                $ StormX.FaceChange("sad",1)
                ch_e "Боюсь, из-за твоих попыток нарушить правила, на сегодня нам придется закончить."
                if not ApprovalCheck(StormX, 1500):
                        jump Emma_and_Storm_End
        $ EmmaX.FaceChange("sly",1)
        $ StormX.FaceChange("sly",1,Eyes="side",Brows="sad")
        ch_s "Эмма, я считаю, что мы должны что-то сделать, чтобы помочь этой измученной душе. . ."
        $ EmmaX.FaceChange("sly",1,Eyes="leftside")
        if not Player.Male:
            ch_e "'Ро, ты ее избалуешь!"
        else:
            ch_e "'Ро, ты его избалуешь!"
        $ StormX.FaceChange("smile",1,Eyes="side")
        $ Player.Statup("Focus", 90, 3)
        if not Player.Male:
            ch_s "О, да, давай -очень- избалуем его."
        else:
            ch_s "О, да, давай -очень- избалуем его."
        ch_e "Что ж, тогда. . ."
        $ EmmaX.Uptop = 1
        call Girl_First_Topless(EmmaX,1)
        $ EmmaX.FaceChange("sly",1)
        $ StormX.FaceChange("sly",1)
        ch_e "Давай позволим ему выбрать. . ."
        menu Emma_Storm_Menu:
            "Кому из нас лучше закончить с тобой?"
            "[EmmaX.Name_dat]?":
                    $ EmmaX.Statup("Love", 80, 2)
                    $ EmmaX.Statup("Inbt", 70, 2)
                    call Shift_Focus(EmmaX)
                    $ EmmaX.FaceChange("smile",1)
                    $ StormX.FaceChange("sad",2)
                    ch_p "[EmmaX.Name_dat]?"
                    $ StormX.FaceChange("sly",1,Brows="sad")
                    $ StormX.Statup("Obed", 70, 2)
                    ch_s "Жаль. . ."
            "[StormX.Name_dat]?":
                    $ EmmaX.Statup("Love", 80, -1)
                    $ StormX.Statup("Love", 80, 2)
                    $ StormX.Statup("Obed", 50, 2)
                    call Shift_Focus(StormX)
                    $ StormX.FaceChange("smile",1)
                    $ EmmaX.FaceChange("sad",2)
                    ch_p "[StormX.Name_dat]?"
                    $ EmmaX.FaceChange("sly",1,Eyes="leftside",Brows="sad")
                    $ EmmaX.Statup("Obed", 50, 2)
                    $ EmmaX.Statup("Obed", 70, 2)
                    hide Emma_FJ_Animation
                    show Emma_Sprite at Sprite_Set(650,0,ZM=1.3) zorder 140
                    if not Player.Male:
                        ch_e "Что ж, тогда она вся твоя."
                    else:
                        ch_e "Что ж, тогда он весь твой."
            "Никому, мне и так неплохо." if "neither" not in Player.RecentActions:
                    $ EmmaX.FaceChange("smile",1)
                    ch_e "Хорошо, тогда я-"
                    $ EmmaX.FaceChange("confused",1)
                    $ StormX.FaceChange("confused",1)
                    ch_e "Подожди, что?"
                    $ EmmaX.Statup("Obed", 50, 2)
                    $ StormX.Statup("Obed", 50, 2)
                    $ StormX.Statup("Inbt", 50, 1)
                    if not Player.Male:
                        ch_e "Ты уверена, что тебе не нужна никакая. . . \"помощь?\""
                    else:
                        ch_e "Ты уверен, что тебе не нужна никакая. . . \"помощь?\""
                    menu:
                        extend ""
                        "Хотя да, от помощи я все же не откажусь. . .":
                                $ EmmaX.FaceChange("smile",1)
                                $ StormX.FaceChange("smile",1)
                                $ EmmaX.Statup("Love", 80, 1)
                                $ EmmaX.Statup("Inbt", 70, 1)
                                $ StormX.Statup("Love", 80, 1)
                                $ StormX.Statup("Inbt", 70, 1)
                        "Да я просто пошутил, я не хочу отказываться от вашей помощи.":
                                $ StormX.FaceChange("smile",1)
                                $ EmmaX.Statup("Love", 80, 2)
                                $ EmmaX.Statup("Inbt", 70, 1)
                                $ StormX.Statup("Love", 90, 1)
                                $ StormX.Statup("Inbt", 70, 2)
                        "Ага, давайте уже закончим и я пойду?":
                                $ StormX.FaceChange("sad",1)
                                $ EmmaX.Statup("Obed", 70, 2)
                                $ EmmaX.Statup("Obed", 90, 1)
                                $ StormX.Statup("Obed", 90, 2)
                                ch_e "Полагаю, я даже уважаю такое решение."
                                jump Emma_and_Storm_End
                    $ Player.AddWord(1,"neither") #recent
                    ch_e "Конечно. . ."
                    jump Emma_Storm_Menu
        #end menu Emma_Storm_Menu:

        $ Partner.Statup("Lust", 80, 5)
        $ Player.Statup("Focus", 93, 3)
        if Player.Male:
                "[Ch_Focus.Name] сближается с вами, забирается на вас сверху и склоняется над вашим членом."
        else:
                "[Ch_Focus.Name] сближается с вами, забирается на вас сверху и склоняется над вашей киской."

        if Ch_Focus is EmmaX:
                $ EmmaX.Pose = "69"
                call Emma_BJ_Launch
        else:
                show Emma_Sprite:
                    ease 1 xpos 900
                $ StormX.Pose = "69"
                call Storm_BJ_Launch

        $ EmmaX.FaceChange("sly",1)
        $ StormX.FaceChange("sly",1)
        ch_e "Пришло время твоего выпускного экзамена."
        ch_s "Сейчас посмотрим, насколько хорошо ты справишься. . ."
        $ Partner.Offhand = "fondle pussy"
#start final 69 activity / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        if Player.Male:
                #final 69 actions, male
                $ Speed = 1
                $ Ch_Focus.Statup("Lust", 80, 5)
                $ Partner.Statup("Lust", 70, 5)
                $ Player.Statup("Focus", 96, 3)
                "[Ch_Focus.Name] плавно проводит язычком по вашему члену."
                $ Speed = 6
                $ Ch_Focus.Statup("Lust", 90, 5)
                $ Partner.Statup("Lust", 80, 5)
                $ Player.Statup("Focus", 96, 3)
                "Достигнув головки, она обхватывает ее губами и опускаясь до основания одним движением."
                $ Speed = 4
                $ Ch_Focus.Statup("Lust", 90, 5)
                $ Partner.Statup("Lust", 80, 5)
                $ Player.Statup("Focus", 96, 3)
                "Она ненадолго задерживается там, прежде чем начать движения вверх-вниз."
                $ EmmaX.Blow += 1
        else:
                #final 69 actions, female
                $ Speed = 1
                $ Ch_Focus.Statup("Lust", 80, 5)
                $ Partner.Statup("Lust", 70, 5)
                $ Player.Statup("Focus", 96, 3)
                "[Ch_Focus.Name] плавно проводит языком по вашей киске."
                $ Speed = 2
                $ Ch_Focus.Statup("Lust", 90, 5)
                $ Partner.Statup("Lust", 80, 5)
                $ Player.Statup("Focus", 96, 3)
                "Достигнув клитора, она начинает водить по нему язычком взад-вперед."
                $ Speed = 3
                $ Ch_Focus.Statup("Lust", 90, 5)
                $ Partner.Statup("Lust", 80, 5)
                $ Player.Statup("Focus", 96, 3)
                "Затем она обхватывает его губами, глубоко втягивает в рот, не прекращая ласкать его языком."
                $ EmmaX.CUN += 1

        $ Ch_Focus.AddWord(1,0,0,0,"69") #history
        $ Player.AddWord(1,0,0,0,"69")
        $ Player.Statup("Focus", 94, 5)
        "Делая это, она подставляет свою киску в надежде, что вы ответите ей взаимностью."
        menu:
            "Начать лизать ее?"
            "Да":
                    $ Trigger2 = "lick pussy"
                    $ Ch_Focus.Statup("Lust", 94, 5)
                    $ Partner.Statup("Lust", 90, 5)
                    $ Ch_Focus.Statup("Love", 95, 3)
                    $ Ch_Focus.Statup("Inbt", 50, 2)
                    "Вы начинаете лизать ее, она положительно реагирует на ваши действия."
                    $ Ch_Focus.Statup("Lust", 94, 5)
                    $ Partner.Statup("Lust", 90, 5)
                    $ Partner.Statup("Love", 80, 2)
                    $ Partner.Statup("Inbt", 70, 1)
            "Нет":
                    $ Ch_Focus.Statup("Love", 90, -2)
                    $ Ch_Focus.Statup("Obed", 60, 2)
                    $ Ch_Focus.Statup("Obed", 80, 2)
                    $ Partner.FaceChange("sad",1)
                    "Не дождавшись ответных действий, она кажется немного разочаровывается вами."
                    $ Partner.Statup("Love", 90, -2)
                    $ Partner.Statup("Obed", 80, 3)
                    "С цокающим звуком неодобрения, [Partner.Name] наклоняется и помогает ей вместо вас."
                    $ Partner.FaceChange("sly",1)
                    $ Partner.Offhand = "lick girl pussy"
        $ Speed = 6
        $ Player.Statup("Focus", 200, 20)
        call Punch
        $ Round -= 5 if Round > 5 else 0
        "Спустя несколько минут, что кажутся мгновением, вы переступаете край и взрываетесь."

        $ Ch_Focus.Statup("Lust", 200, 20)
        $ Partner.Statup("Lust", 200, 20)

        $ Ch_Focus.Spunk.append("mouth")
        $ Ch_Focus.Spunk.append("chin")
        $ Player.Spunk = 1
        $ Player.Focus = 5
        if Player.Male:
                "Ваша сперма с громким звуком устремляется ей в глотку, но её это, похоже, особо не беспокоит."
        else:
                "Ваши соки разбрызгиваются по всему её лицу, но её это, похоже, особо не беспокоит."
        $ Partner.Offhand = 0
        if Ch_Focus.Lust >= 100:
                call Punch
                "[Ch_Focus.Name], кажется, начинает дрожать сильнее, чем раньше. . ."
                $ Ch_Focus.Lust = 25
        if Partner.Lust >= 100:
                call Punch
                "Вы также отмечаете, что, похоже, и [Partner.Name] в этот момент кончила. . ."
                $ Partner.Lust = 25

        $ Speed = 0
        $ Partner.Offhand = 0
        $ Trigger2 = 0
        #renpyshow show Emma_Sprite at Sprite_Set(650,0,ZM=1.3) zorder 140
        if Ch_Focus is EmmaX:
                call Emma_BJ_Reset
                show Emma_Sprite at Sprite_Set(650,0,ZM=1.35) zorder EmmaX.Layer
#                show Emma_Sprite:
#                    ease 1 xpos 650
        else:
                call Storm_BJ_Reset
                show Storm_Sprite at Sprite_Set(650,0,ZM=1.35) zorder StormX.Layer
#                show Storm_Sprite:
#                    ease 1 xpos 650
        call AnyLine(Ch_Focus,"Это было впечатляюще, "+Ch_Focus.Petname+".")
        call AnyLine(Partner,"Даже очень. . .")

label Emma_and_Storm_End: # / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        #reset screen to classroom
        $ EmmaX.OutfitChange(Changed=1)
        $ StormX.OutfitChange(Changed=1)
        scene bg_class onlayer backdrop
        call Girl_Hide(EmmaX)
        call Girl_Hide(StormX)
        show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
                zoom 1
        show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
                zoom 1
        $ EmmaX.Offhand = 0
        $ EmmaX.Pose = 0
        $ EmmaX.Spunk =[]
        $ StormX.Offhand = 0
        $ StormX.Pose = 0
        $ StormX.Spunk =[]
        call Checkout(1)
        "Они приводят себя в порядок."
        $ EmmaX.FaceChange("sly",1)
        $ StormX.FaceChange("sly",1)
        ch_e "Я думаю, что, по крайней мере, на сегодня мы добились успеха."
        ch_e "Постарайся осмыслить наш небольшой \"урок\". . ."
        ch_e "Пожалуй, мы не будем против, если ты будешь \"осмысливать\" всю ночь. . ."
        ch_s "Мы доложим Чарльзу, что наш маленький эксперимент увенчался успехом."
        ch_s "Я сомневаюсь, что он перестанет следить за твоими действиями."
        ch_s "Но, по крайней мере, он должен дать тебе немного больше времени, чтобы пересмотреть свое поведение."
        $ Player.DrainWord("locked",0,0,1)
        $ EmmaX.DrainWord("EmmaStormFail",0,0,0,1) #clears failed condition on success
        call Remove_Girl("All")
        "Они отпирают дверь и выходят."
        ch_e "И приберись перед уходом!"
        $ EmmaX.AddWord(1,0,"EmmaStorm",0,"EmmaStorm") #adds to History and daily
        return


label Emma_and_Storm_Bad_End:# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        #reset screen to classroom
        $ EmmaX.FaceChange("sad",1)
        $ StormX.FaceChange("sad",1)
        $ EmmaX.OutfitChange(Changed=1)
        $ StormX.OutfitChange(Changed=1)
        scene bg_class onlayer backdrop
        call Girl_Hide(EmmaX)
        call Girl_Hide(StormX)
        show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
                zoom 1
        show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
                zoom 1
        $ EmmaX.Offhand = 0
        $ EmmaX.Pose = 0
        $ EmmaX.Spunk =[]
        $ StormX.Offhand = 0
        $ StormX.Pose = 0
        $ StormX.Spunk =[]
        call Checkout(1)
        "Они встают и приводят себя в порядок."


#        call Sex_Over #change to simpler version


        ch_e "Well that's unfortunate."
        ch_s "Мы доложим Чарльзу, что наш маленький эксперимент провалился."
        $ Player.DrainWord("locked",0,0,1)
        call Remove_Girl("All")
        $ EmmaX.AddWord(1,0,"EmmaStorm",0,"EmmaStorm") #adds to History and daily
        if "EmmaStormFail" in EmmaX.History:
                return
        $ EmmaX.AddWord(1,0,0,0,"EmmaStormFail") #adds to History
        if not Player.Male:
            "Они оставляют вас в комнате одну, а позже вы получаете альтернативное наказание от Ксавье."
        else:
            "Они оставляют вас в комнате одного, а позже вы получаете альтернативное наказание от Ксавье."
        "В итоге вам придется каждый вечер в течение следующей недели писать рефераты на тему \"хороший моральный облик.\""
        return

#End  Emma_and_Storm content  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
